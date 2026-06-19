#!/usr/bin/env node
const assert = require("assert");
const fs = require("fs");
const path = require("path");
const vm = require("vm");
const { createRequire } = require("module");

const source = fs
  .readFileSync("frontend/ocr-compare.js", "utf8")
  .replace(/\ninitialize\(\);\s*$/, "\n");

const context = {
  console,
  window: {
    __UMA_RUNTIME_CONFIG__: {},
    location: { protocol: "http:", port: "8787" },
    setTimeout() {},
  },
  document: {},
  navigator: {},
  Blob: function Blob() {},
  URL: { createObjectURL() { return ""; } },
  require: createRequire(path.resolve("frontend/ocr-compare.js")),
};

vm.createContext(context);
vm.runInContext(source, context);

function call(expression) {
  return vm.runInContext(expression, context);
}

const singleLineDisplay =
  "$$\\widehat {f}(x) = \\left\\{ \\begin{array}{ll}0, & 0 \\leq x < 1, \\\\ 1, & x \\geq 1. \\end{array} \\right.$$";
const singleLineHtml = call(
  `renderMarkdownHtml(normalizeMathMarkdown(${JSON.stringify(singleLineDisplay)}))`,
);
assert(singleLineHtml.includes('class="math-display"'), "single-line display math should render as display math");
assert(!singleLineHtml.includes("<p>$$"), "single-line display math should not render as raw paragraph text");

const brokenAligned = `$$\\begin{aligned}
$$
\\sqrt { x } & \\leq ...
$$
$$
& = ...
$$
\\end{aligned}$$`;
const repairedAligned = call(`prepareMathpixMarkdown(${JSON.stringify(brokenAligned)})`);
assert.strictEqual(
  repairedAligned,
  `$$
\\begin{aligned}
\\sqrt { x } & \\leq ...
& = ...
\\end{aligned}
$$`,
  "broken Mathpix aligned delimiters should be normalized into one display block",
);

const latexTable = "\\begin{array}{cc}\na & b \\\\ c & d\n\\end{array}";
const bareTableHtml = call(`renderMarkdownHtml(normalizeMathMarkdown(${JSON.stringify(latexTable)}))`);
const wrappedTableHtml = call(`renderMarkdownHtml(normalizeMathMarkdown(${JSON.stringify(`$$\n${latexTable}\n$$`)}))`);
assert(bareTableHtml.includes("latex-table-wrap"), "bare LaTeX table should render as a table");
assert(wrappedTableHtml.includes("latex-table-wrap"), "display-wrapped LaTeX table should render as a table");

function readFixture(name, kind) {
  return fs
    .readFileSync(`frontend/ocr-core/fixtures/math-delimiter/${name}.${kind}.md`, "utf8")
    .replace(/\r\n?/g, "\n")
    .trimEnd();
}

for (const fixtureName of [
  "extra_double_dollar",
  "missing_opening_dollar",
  "missing_closing_dollar",
  "inline_math_should_remain_inline",
  "markdown_table_with_formula",
  "code_block_should_not_change",
]) {
  const input = readFixture(fixtureName, "input");
  const expected = readFixture(fixtureName, "expected");
  const actual = call(`normalizeMathMarkdown(${JSON.stringify(input)})`).trimEnd();
  assert.strictEqual(actual, expected, `normalizeMathMarkdown wrapper should satisfy ${fixtureName}`);
}

call(`
  state.currentPage = 3;
  state.reviewExpanded.clear();
  state.reviewInitializedPages.clear();
  ensureDefaultReviewExpansion([{ blockIndex: "a" }, { blockIndex: "b" }]);
`);
assert(call('state.reviewExpanded.has("3:a")'), "first risk block should expand on first page render");
call(`ensureDefaultReviewExpansion([{ blockIndex: "b" }]);`);
assert(!call('state.reviewExpanded.has("3:b")'), "default expansion should only initialize once per page");
call(`expandOnlyReviewBlock(3, "b");`);
assert.strictEqual(
  call("JSON.stringify(Array.from(state.reviewExpanded))"),
  JSON.stringify(["3:b"]),
  "applied block should be the only expanded block",
);

call(`
  state.mineruInfo = {
    pdf_info: [
      {
        para_blocks: [
          { type: "text", lines: [{ spans: [{ content: "MinerU source" }] }] },
          { type: "text", lines: [{ spans: [{ content: "Second block" }] }] }
        ]
      }
    ]
  };
  getMathpixBlockDrafts(1).set("0", "Mathpix draft only");
`);
const draftOnlyExport = call("buildBookMarkdown(true)");
assert(draftOnlyExport.includes("MinerU source"), "draft-only Mathpix text should not enter corrected export");
assert(!draftOnlyExport.includes("Mathpix draft only"), "unapplied Mathpix draft should not be exportable");
call(`getBlockOverrides(1).set("0", "Applied correction");`);
const appliedExport = call("buildBookMarkdown(true)");
assert(appliedExport.includes("Applied correction"), "applied correction should enter corrected export");

const reviewHtml = call(`
  state.currentPage = 1;
  renderReviewItem(
    { blockIndex: "0", markdown: "MinerU source", kind: "text" },
    { reasons: ["split_formula_tokens"], bbox: [0, 0, 10, 10] },
    "Old applied correction",
    true,
    "New Mathpix draft"
  )
`);
assert(reviewHtml.includes("Mathpix 待应用"), "new Mathpix draft should be shown as pending even when an older correction exists");
assert(reviewHtml.includes("New Mathpix draft"), "pending Mathpix draft should be previewed");
assert(!reviewHtml.includes("Old applied correction</div>"), "old applied correction should not be the visible pending preview");

console.log("ocr compare frontend regressions ok");
