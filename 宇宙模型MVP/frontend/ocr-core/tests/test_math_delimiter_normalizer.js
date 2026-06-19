#!/usr/bin/env node
const assert = require("assert");
const { normalizeMathDelimiters } = require("../normalization/mathDelimiterNormalizer");
const { validateMarkdownMathSyntax } = require("../validation/markdownMathSyntaxValidator");

function normalize(blockText, blockType = "unknown") {
  return normalizeMathDelimiters({ blockId: "test-block", blockText, blockType });
}

{
  const input = "$$\n$$\nE = mc^2\n$$\n$$";
  const actual = normalize(input);
  assert.strictEqual(actual.normalizedText, "$$\nE = mc^2\n$$");
  assert.strictEqual(actual.changed, true);
}

{
  const input = "```js\nconst price = '$100';\n```";
  const actual = normalize(input);
  assert.strictEqual(actual.normalizedText, input);
  assert.strictEqual(actual.changed, false);
}

{
  const input = "$$\nE = mc^2";
  const actual = normalize(input);
  assert.strictEqual(actual.normalizedText, "$$\nE = mc^2\n$$");
  assert.strictEqual(actual.errors.length, 0);
}

{
  const input = "The camera cost $100 and the guide scope cost HK$ 450.";
  const actual = normalize(input);
  assert.strictEqual(actual.normalizedText, input);
  assert.strictEqual(actual.changed, false);
}

{
  const validation = validateMarkdownMathSyntax({
    blockId: "bad-env",
    markdown: "$$\n\\begin{align}\na &= b\n$$",
  });
  assert.strictEqual(validation.ok, false);
  assert(validation.errors.some((item) => item.type === "unbalanced_latex_environment"));
}

{
  const validation = validateMarkdownMathSyntax({
    blockId: "bad-fence",
    markdown: "```python\nx = '$$'",
  });
  assert.strictEqual(validation.ok, true);
  assert(validation.warnings.some((item) => item.type === "unclosed_code_fence"));
}

console.log("math delimiter normalizer unit tests ok");
