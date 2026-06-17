import unittest

from backend.services.ocr_correction import OCR_CORRECTION_SERVICE


class OcrCorrectionCandidateDetectionTest(unittest.TestCase):
    def test_html_table_with_compact_power_header_is_candidate(self) -> None:
        markdown = (
            "Table 3.2.1. Average number of correct significant decimal digits.\n"
            "<table><tr><td>Algorithm</td><td>w=1</td><td>w=27</td><td>w=214</td></tr>"
            "<tr><td>MGS</td><td>5.92</td><td>5.15</td><td>2.90</td></tr></table>"
        )

        result = OCR_CORRECTION_SERVICE.correct_markdown(
            {"markdown": markdown, "dryRun": True, "maxCandidates": 8}
        )

        self.assertTrue(result["ok"])
        self.assertEqual(len(result["candidates"]), 1)
        self.assertIn("compact_formula_maybe_missing_superscript", result["candidates"][0]["reasons"])

    def test_plain_html_numeric_table_is_not_candidate(self) -> None:
        markdown = (
            "<table><tr><td>Name</td><td>Value</td></tr>"
            "<tr><td>A</td><td>27</td></tr></table>"
        )

        result = OCR_CORRECTION_SERVICE.correct_markdown(
            {"markdown": markdown, "dryRun": True, "maxCandidates": 8}
        )

        self.assertTrue(result["ok"])
        self.assertEqual(result["candidates"], [])


if __name__ == "__main__":
    unittest.main()
