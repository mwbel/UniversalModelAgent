# ocr-core

`ocr-core` is the future home for testable pure-function logic used by the third-column OCR correction workbench.

Current scope:

- Store regression fixtures.
- Define fixture and test conventions.
- Keep current behavior observable before extracting modules from `frontend/ocr-compare.js`.

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

Fixture convention:

- `*.input.md` is the raw OCR or adapter input.
- `*.expected.md` is the intended target Markdown after the relevant pure-function pipeline.
- Fixture names should describe the failure mode, not the implementation detail.
