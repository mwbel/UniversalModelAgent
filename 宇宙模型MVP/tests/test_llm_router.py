import unittest

from backend.services.llm_registry import LlmEndpoint, LlmRegistry
from backend.services.llm_router import LlmRouter


def endpoint(
    model_id: str,
    capabilities: tuple[str, ...],
    *,
    privacy: str = "remote",
    cost: str = "paid",
    latency: str = "medium",
    priority: int = 50,
) -> LlmEndpoint:
    return LlmEndpoint(
        id=model_id,
        provider="openai-compatible",
        model=model_id.split(":", 1)[-1],
        base_url="http://llm.test/v1",
        chat_path="/chat/completions",
        capabilities=capabilities,
        privacy=privacy,
        cost=cost,
        latency=latency,
        priority=priority,
    )


class LlmRouterTest(unittest.TestCase):
    def test_direct_qa_prefers_local_chat_model(self) -> None:
        router = LlmRouter(
            registry=LlmRegistry(
                endpoints=[
                    endpoint(
                        "local:qwen",
                        ("chat", "chinese", "math", "rag_synthesis"),
                        privacy="local",
                        cost="free_local",
                        priority=70,
                    ),
                    endpoint(
                        "remote:strong",
                        ("chat", "chinese", "math", "reasoning", "rag_synthesis"),
                        privacy="remote",
                        cost="paid",
                        priority=90,
                    ),
                ]
            )
        )

        decision = router.route(task="direct_qa", question="解释月相变化")

        self.assertEqual(decision.selected.id, "local:qwen")
        self.assertIn("remote:strong", [item.id for item in decision.fallbacks])

    def test_computed_explanation_prefers_reasoning_math_model(self) -> None:
        router = LlmRouter(
            registry=LlmRegistry(
                endpoints=[
                    endpoint(
                        "local:qwen",
                        ("chat", "chinese", "math"),
                        privacy="local",
                        cost="free_local",
                        priority=70,
                    ),
                    endpoint(
                        "remote:strong",
                        ("chat", "chinese", "math", "reasoning", "rag_synthesis"),
                        privacy="remote",
                        cost="paid",
                        priority=100,
                    ),
                ]
            )
        )

        decision = router.route(task="computed_explanation", question="比较 VSOP 和 DE440 误差")

        self.assertEqual(decision.selected.id, "remote:strong")

    def test_embedding_models_are_not_chat_candidates(self) -> None:
        router = LlmRouter(
            registry=LlmRegistry(
                endpoints=[
                    endpoint("local:embed", ("embedding",), privacy="local", cost="free_local"),
                    endpoint("local:chat", ("chat", "chinese"), privacy="local", cost="free_local"),
                ]
            )
        )

        decision = router.route(task="direct_qa", question="你好")

        self.assertEqual(decision.selected.id, "local:chat")
        self.assertEqual(decision.fallbacks, [])


if __name__ == "__main__":
    unittest.main()
