核心改法是：第三栏不再直接用 MinerU 合并后的跨页 block，而是按 PDF 物理页面重建校对分段。

现在行为：

- 第 5 页 Block 6：第三栏 MinerU 渲染和“查看当前块 Markdown 源码”只保留第 5 页底部那两行，不再把第 6 页顶部 `of Robert Dicke...` 一起塞进来。
- 第 6 页：第三栏顶部新增真实的“跨页续段候选”，内容来自上一页 block 中 `cross_page: true` 的行；不再显示泛化的“页首正文候选”占位。
- 第 6 页正文 Block 1 仍从第二段开始，这样“跨页续段候选 + Block 1”拼起来才对应当前 PDF 第 6 页。
- accepted dry-run preview 也改为跟随第三栏的物理页面分段，避免 patch hash 和 UI 源码不一致。
- 原正式导出逻辑没有改；第二栏仍保留 MinerU 原始对照。