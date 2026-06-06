import { useEffect, useRef, useState } from 'react'
import { A2UISurface, applyA2UILine, createEmptySurface } from './a2ui-engine/A2UIRuntime'
import { buildA2UILines } from './a2ui-engine/buildA2UILines'
import {
  askQuestion,
  fetchHealth,
  fetchKnowledgeBases,
  fetchStrategies,
  uploadDocument,
  type KnowledgeBase,
  type OrchestrationStep,
  type RagStrategy,
  type VisualizationInstruction,
} from './services/api'
import { createId, type ChatMessage } from './types'

const starterQuestions = [
  '查询 2050 年火星位置，要求精度小于 10^-6',
  '切比雪夫插值为什么适合 DE440？',
  '绘制 2050 年火星 VSOP 和 DE440 对照图',
]

const visualIntentMarkers = ['可视化', '展示', '绘制', '画', '图', '图示', '示意图', '演示', '模拟', '动画', '交互', 'visualize', 'show me', 'diagram', 'demo']
const planetComputeMarkers = ['vsop', 'de440', '星历', '行星位置', '精度', '误差', '坐标', '速度']
const visualizationStoragePrefix = 'universe-model-viz:'

function hasExplicitVisualizationIntent(text: string) {
  const lowered = text.toLowerCase()
  return visualIntentMarkers.some((marker) => lowered.includes(marker))
}

function wantsPlanetCalculation(text: string) {
  const lowered = text.toLowerCase()
  return planetComputeMarkers.some((marker) => lowered.includes(marker))
}

function buildRuntimeStages(useRag: boolean, question: string): OrchestrationStep[] {
  const wantsVisual = hasExplicitVisualizationIntent(question)
  const wantsCalculation = wantsPlanetCalculation(question)
  return [
    { id: 'intent', label: '确定任务意图', status: 'pending' },
    ...(wantsCalculation ? [{ id: 'calculation', label: 'Python 数值计算', status: 'pending' } as OrchestrationStep] : []),
    ...(useRag || wantsCalculation ? [{ id: 'retrieval', label: '检索本地知识库', status: 'pending' } as OrchestrationStep] : []),
    ...(wantsVisual ? [{ id: 'visualizer', label: '匹配 A2UI 能力', status: 'pending' } as OrchestrationStep] : []),
    { id: 'generation', label: '生成文字解释', status: 'pending' },
    ...(wantsVisual ? [{ id: 'validation', label: '校验并交给前端渲染', status: 'pending' } as OrchestrationStep] : []),
  ]
}

function suggestKbId(filename: string): string {
  const stem = filename.replace(/\.[^.]+$/, '')
  const parts = stem.split(/[\s._\-()（）【】\[\]、，,]+/).filter(Boolean)
  return parts.slice(0, 2).join('-') || 'default'
}

function buildSurfaceFromVisualizations(items: VisualizationInstruction[]) {
  let surface = createEmptySurface()
  const lines = items.flatMap((item) => buildA2UILines(item))
  for (const line of lines) {
    surface = applyA2UILine(surface, line)
  }
  return surface
}

function storeVisualizationForWindow(item: VisualizationInstruction) {
  const id = `${Date.now()}-${Math.random().toString(36).slice(2, 8)}`
  window.localStorage.setItem(`${visualizationStoragePrefix}${id}`, JSON.stringify(item))
  return id
}

function buildVisualizationWindowUrl(id: string) {
  const url = new URL(window.location.href)
  url.search = ''
  url.hash = ''
  url.searchParams.set('viz', id)
  return url.toString()
}

function loadVisualizationFromWindow(id: string): VisualizationInstruction | null {
  const raw = window.localStorage.getItem(`${visualizationStoragePrefix}${id}`)
  if (!raw) return null
  try {
    return JSON.parse(raw) as VisualizationInstruction
  } catch {
    return null
  }
}

function stageLabel(status: OrchestrationStep['status']) {
  if (status === 'completed') return '完成'
  if (status === 'running') return '进行中'
  if (status === 'skipped') return '跳过'
  return '等待'
}

function PipelineStatus({
  steps,
  activeIndex,
  loading,
}: {
  steps: OrchestrationStep[]
  activeIndex?: number
  loading?: boolean
}) {
  const visibleSteps = loading ? steps.slice(0, Math.min(steps.length, (activeIndex ?? 0) + 1)) : steps
  const resolved = visibleSteps.map((step, index) => ({
    ...step,
    status: (loading
      ? index < (activeIndex ?? 0)
        ? 'completed'
        : index === activeIndex
          ? 'running'
          : 'pending'
      : step.status) as OrchestrationStep['status'],
  }))

  return (
    <div className="pipeline-card">
      <p className="eyebrow">Orchestration</p>
      <div className="pipeline-steps">
        {resolved.map((step) => (
          <div className={`pipeline-step ${step.status}`} key={step.id}>
            <span />
            <div>
              <strong>{step.label}</strong>
              <small>{step.detail || stageLabel(step.status)}</small>
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}

function VisualizationFrame({ item }: { item: VisualizationInstruction }) {
  const [standaloneHref] = useState(() => buildVisualizationWindowUrl(storeVisualizationForWindow(item)))

  return (
    <section className="visualization-frame">
      <div className="visualization-toolbar">
        <span>{item.title}</span>
        <a href={standaloneHref} rel="noreferrer" target="_blank">
          新窗口打开
        </a>
      </div>
      <A2UISurface surface={buildSurfaceFromVisualizations([item])} />
    </section>
  )
}

function MessageVisualizations({ items }: { items: VisualizationInstruction[] }) {
  if (!items.length) return null
  return (
    <div className="message-visualization">
      {items.map((item) => (
        <VisualizationFrame item={item} key={item.id} />
      ))}
    </div>
  )
}

function StandaloneVisualizationPage({ item }: { item: VisualizationInstruction | null }) {
  return (
    <main className="standalone-viz-page">
      <section className="standalone-viz-shell">
        <div className="standalone-viz-head">
          <div>
            <p className="eyebrow">A2UI Standalone</p>
            <h1>{item?.title ?? '未找到可视化组件'}</h1>
          </div>
          <button type="button" onClick={() => window.close()}>
            关闭窗口
          </button>
        </div>
        {item ? (
          <A2UISurface surface={buildSurfaceFromVisualizations([item])} />
        ) : (
          <p className="muted">这个可视化指令不存在或已经被浏览器清理，请回到对话中重新打开。</p>
        )}
      </section>
    </main>
  )
}

function WorkspaceApp({ isGallery }: { isGallery: boolean }) {
  const [health, setHealth] = useState<string>('Checking')
  const [strategies, setStrategies] = useState<RagStrategy[]>([])
  const [kbs, setKbs] = useState<KnowledgeBase[]>([])
  const [selectedStrategy, setSelectedStrategy] = useState<string>('naive')
  const [selectedKb, setSelectedKb] = useState<string | null>(null)
  const [useRag, setUseRag] = useState(false)
  const [kbInput, setKbInput] = useState('')
  const [messages, setMessages] = useState<ChatMessage[]>([])
  const [input, setInput] = useState('')
  const [isLoading, setIsLoading] = useState(false)
  const [activeStage, setActiveStage] = useState(0)
  const [loadingStages, setLoadingStages] = useState<OrchestrationStep[]>(buildRuntimeStages(false, ''))
  const [evidenceOpen, setEvidenceOpen] = useState(false)
  const [status, setStatus] = useState('')
  const composerFileInputRef = useRef<HTMLInputElement | null>(null)

  const currentStrategy = strategies.find((item) => item.id === selectedStrategy)
  const latestAssistant = [...messages].reverse().find((item) => item.role === 'assistant')
  const latestContexts = latestAssistant?.role === 'assistant' ? latestAssistant.contexts ?? [] : []

  async function refresh() {
    const [healthResult, strategyResult, kbResult] = await Promise.all([
      fetchHealth(),
      fetchStrategies(),
      fetchKnowledgeBases(),
    ])
    setHealth(healthResult.ok ? 'Online' : 'Offline')
    setStrategies(strategyResult.items)
    setSelectedStrategy((current) => current || strategyResult.items[0]?.id || 'naive')
    setKbs(kbResult.items)
  }

  useEffect(() => {
    refresh().catch((error) => setStatus(error instanceof Error ? error.message : String(error)))
  }, [])

  useEffect(() => {
    if (!isLoading) {
      setActiveStage(0)
      return
    }

    const interval = window.setInterval(() => {
      setActiveStage((stage) => Math.min(stage + 1, loadingStages.length - 1))
    }, 750)
    return () => window.clearInterval(interval)
  }, [isLoading, loadingStages.length])

  useEffect(() => {
    if (useRag && !selectedKb && kbs[0]?.kb_id) {
      setSelectedKb(kbs[0].kb_id)
    }
  }, [useRag, selectedKb, kbs])

  useEffect(() => {
    setEvidenceOpen(false)
  }, [latestAssistant?.id])

  async function handleUpload(file: File | null) {
    if (!file) return
    const nextKbId = kbInput.trim() || suggestKbId(file.name)
    setKbInput(nextKbId)
    setStatus('正在上传并建立本地知识库...')
    const result = await uploadDocument(file, nextKbId)
    if (!result.ok) {
      setStatus(result.error || '上传失败')
      return
    }
    setStatus(`已上传到 ${result.kbId}，共摄入 ${result.chunks ?? '-'} 个文档块。`)
    setSelectedKb(result.kbId ?? nextKbId)
    await refresh()
  }

  async function sendQuestion(text = input) {
    const question = text.trim()
    if (!question || isLoading) return

    const history = messages
      .filter((message) => message.role === 'user' || message.role === 'assistant')
      .map((message) => ({ role: message.role, content: message.content }))

    setInput('')
    setIsLoading(true)
    setActiveStage(0)
    setLoadingStages(buildRuntimeStages(useRag, question))
    setMessages((prev) => [...prev, { id: createId('user'), role: 'user', content: question }])

    try {
      const response = await askQuestion({
        question,
        history,
        ragVariant: selectedStrategy,
        kbId: useRag ? selectedKb : null,
        useRag,
      })
      setMessages((prev) => [
        ...prev,
        {
          id: createId('assistant'),
          role: 'assistant',
          content: response.answer || '没有生成回答。',
          strategy: response.strategy,
          citations: response.citations,
          contexts: response.contexts,
          recommendedVisualizations: response.recommendedVisualizations,
          orchestration: response.orchestration,
          autoRagUsed: response.autoRagUsed,
          computedEphemeris: response.computedEphemeris,
        },
      ])
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        {
          id: createId('assistant'),
          role: 'assistant',
          content: error instanceof Error ? error.message : String(error),
        },
      ])
    } finally {
      setIsLoading(false)
    }
  }

  if (isGallery) {
    return (
      <main className="gallery-page">
        <section className="gallery-copy">
          <p className="eyebrow">A2UI Gallery</p>
          <h1>天文 A2UI 组件预览</h1>
        </section>
        <A2UISurface
          surface={buildSurfaceFromVisualizations([
            {
              id: 'ephemeris-comparison',
              title: '太阳系行星运动 VSOP / DE440 对照',
              description: '',
              a2uiInstruction: {
                componentId: 'astronomy-core.ephemeris-comparison',
                intentType: 'model_comparison',
                initialProps: {
                  bodies: ['earth', 'mars'],
                  date: '2050-01-01',
                },
              },
            },
          ])}
        />
      </main>
    )
  }

  return (
    <div className="app-shell">
      <div className="background-orbit" />
      <header className="top-nav">
        <div>
          <p className="eyebrow">Universe Model Agent</p>
          <strong>宇宙模型智能体</strong>
        </div>
        <div className="top-status">
          <span>{health}</span>
          <span>{useRag ? selectedStrategy : 'no RAG'}</span>
        </div>
      </header>

      <div className="workspace">
        <aside className="left-rail">
          <section>
            <div className="section-head">
              <span>RAG 知识库</span>
              <b>{kbs.length}</b>
            </div>
            <label className="rag-toggle">
              <input type="checkbox" checked={useRag} onChange={(event) => setUseRag(event.target.checked)} />
              <span>使用 RAG 知识库</span>
            </label>
            <label className="file-pick">
              <input type="file" accept=".txt,.md,.docx,.pdf" onChange={(event) => void handleUpload(event.target.files?.[0] ?? null)} />
              <span>选择本地文档</span>
            </label>
            <input
              className="field"
              value={kbInput}
              onChange={(event) => setKbInput(event.target.value)}
              placeholder="知识库 ID"
            />
            <select className="field" value={selectedKb ?? ''} onChange={(event) => setSelectedKb(event.target.value || null)} disabled={!useRag}>
              <option value="">选择知识库</option>
              {kbs.map((kb) => (
                <option key={kb.kb_id} value={kb.kb_id}>
                  {kb.kb_id} ({kb.doc_count ?? 0} 文档 / {kb.chunk_count ?? 0} 块)
                </option>
              ))}
            </select>
            {status && <p className="status-line">{status}</p>}
          </section>

          <section>
            <div className="section-head">
              <span>RAG 方案</span>
              <b>{strategies.length}</b>
            </div>
            <select className="field" value={selectedStrategy} onChange={(event) => setSelectedStrategy(event.target.value)}>
              {strategies.map((strategy) => (
                <option key={strategy.id} value={strategy.id}>
                  {strategy.label}
                </option>
              ))}
            </select>
            <p className="muted">{useRag ? currentStrategy?.summary : '默认不检索知识库；行星运动模型问题会自动检索 planet-motion。'}</p>
          </section>
        </aside>

        <main className="conversation">
          <div className="message-list">
            {messages.length === 0 ? (
              <section className="welcome-panel">
                <p className="eyebrow">Astronomy Chat</p>
                <h1>用真实 A2UI 组件解释宇宙模型</h1>
                <div className="starter-row">
                  {starterQuestions.map((question) => (
                    <button key={question} onClick={() => void sendQuestion(question)}>
                      {question}
                    </button>
                  ))}
                </div>
              </section>
            ) : (
              messages.map((message) => (
                <article key={message.id} className={`message ${message.role}`}>
                  <p className="message-role">{message.role === 'user' ? 'USER' : 'ASSISTANT'}</p>
                  <div className="message-bubble">{message.content}</div>
                  {message.role === 'assistant' ? (
                    <MessageVisualizations items={message.recommendedVisualizations ?? []} />
                  ) : null}
                </article>
              ))
            )}
            {isLoading && (
              <article className="message assistant">
                <p className="message-role">ASSISTANT</p>
                <PipelineStatus steps={loadingStages} activeIndex={activeStage} loading />
              </article>
            )}
          </div>

          <div className="composer-shell">
            {status ? <p className="composer-status">{status}</p> : null}
            <div className="bottom-input">
              <input
                ref={composerFileInputRef}
                className="bottom-input-file"
                type="file"
                accept=".txt,.md,.docx,.pdf"
                onChange={(event) => {
                  const file = event.target.files?.[0] ?? null
                  void handleUpload(file)
                  event.currentTarget.value = ''
                }}
              />
              <button
                className="attach-button"
                type="button"
                onClick={() => composerFileInputRef.current?.click()}
                disabled={isLoading}
                title="上传附件到知识库"
              >
                +
              </button>
              <input
                value={input}
                onChange={(event) => setInput(event.target.value)}
                onKeyDown={(event) => {
                  if (event.key === 'Enter') void sendQuestion()
                }}
                placeholder="输入你的问题，例如：绘制 2050 年火星 VSOP 和 DE440 对照图"
              />
              <button onClick={() => void sendQuestion()} disabled={!input.trim() || isLoading}>
                {isLoading ? '...' : '↑'}
              </button>
            </div>
          </div>
        </main>

        <aside className="right-rail">
          <section className="evidence-panel">
            <div className="right-section-title">
              <p className="eyebrow">Evidence</p>
              <button type="button" onClick={() => setEvidenceOpen((open) => !open)} disabled={!latestContexts.length}>
                {evidenceOpen ? '隐藏' : latestContexts.length ? `显示 ${latestContexts.length}` : '显示'}
              </button>
            </div>
            {!evidenceOpen ? (
              <p className="muted">{latestContexts.length ? '已有引用，点击显示来源片段。' : '检索证据默认隐藏；需要核对来源时点击显示。'}</p>
            ) : latestContexts.length ? (
              latestContexts.slice(0, 4).map((context, index) => (
                <div className="evidence" key={`${context.source}-${index}`}>
                  <strong>{context.source || `上下文 ${index + 1}`}</strong>
                  <span>score {typeof context.score === 'number' ? context.score.toFixed(3) : '-'}</span>
                  <p>{context.content}</p>
                </div>
              ))
            ) : (
              <p className="muted">暂无检索证据。</p>
            )}
          </section>
        </aside>
      </div>
    </div>
  )
}

export function App() {
  const searchParams = new URLSearchParams(window.location.search)
  const visualizationId = searchParams.get('viz')
  if (visualizationId) {
    return <StandaloneVisualizationPage item={loadVisualizationFromWindow(visualizationId)} />
  }
  return <WorkspaceApp isGallery={searchParams.get('gallery') === '1'} />
}
