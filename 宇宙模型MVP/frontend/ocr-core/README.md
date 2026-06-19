# ocr-core

`ocr-core` is the future home for testable pure-function logic used by the third-column OCR correction workbench.

Current scope:

- Store regression fixtures.
- Define fixture and test conventions.
- Keep current behavior observable before extracting modules from `frontend/ocr-compare.js`.
- Provide isolated pure-function modules before they are wired into the OCR compare UI.

Planned modules:

- `blockParser`
- `mathDelimiterNormalizer`
- `mathpixToTargetMarkdownAdapter`
- `renderValidator`
- `patchGenerator`
- `patchMerger`

Rules:

- Pure-function modules must not call the Mathpix API.
- Pure-function modules must not access the DOM.
- Pure-function modules must not read or write the original Markdown file.
- Renderers must not modify source Markdown.
- UI code must not assemble final export Markdown.
- `mathpixToTargetMarkdownAdapter` only converts one Mathpix block into the third-column target Markdown dialect; it must not call Mathpix, patch files, or update UI state.
- `renderValidator` only reports static Markdown/LaTeX render risks for one block; it must not call MathJax, access the DOM, or repair Markdown.

Fixture convention:

- `*.input.md` is the raw OCR or adapter input.
- `*.expected.md` is the intended target Markdown after the relevant pure-function pipeline.
- Fixture names should describe the failure mode, not the implementation detail.
