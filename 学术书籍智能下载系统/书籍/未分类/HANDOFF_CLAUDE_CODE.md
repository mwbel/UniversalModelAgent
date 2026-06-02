# 学术书籍智能下载系统 - Claude Code 交接说明

## 1. 当前状态

- 项目目录：`/Users/Min369/Documents/同步空间/Manju/Projects/共享/AIProjects/UnivModel/学术书籍智能下载系统`
- 当前数据库：`data/books.db`
- 当前书单：`行星运行轨道理论的相关书籍.v1.xlsx`

最新统计：

- 总书籍数：`95`
- 已完成下载：`11`
- 失败：`68`
- 已找到待下载：`0`
- 待处理：`16`
- 验证失败：`0`
- 搜索候选总数：`125`
- 当前成功率：`11.6%`

注意：这里是 `data/books.db` 的当前快照。数据库已按 `行星运行轨道理论的相关书籍.v1.xlsx` 和 `downloads/` 做过一轮人工对账，其中 `Solving Ordinary Differential Equations I + II` 已补记为 `completed`；这条在磁盘上对应卷 I 和卷 II 两个 PDF，所以用户口径里的“11 本”实际上包含一个两卷集合。

## 2. 已完成的系统能力

### 2.1 基础能力

- Excel 书单解析入库
- SQLite 数据库存储
- 搜索结果候选持久化
- 文件下载
- 文件验证
- 报告生成

### 2.2 已接入搜索源

- `arXiv`
- `Google Scholar`
- `Internet Archive`
- `Library Genesis`（代码已实现，但默认配置为关闭）

相关代码：

- [main.py](/Users/Min369/Documents/同步空间/Manju/Projects/共享/AIProjects/UnivModel/学术书籍智能下载系统/main.py)
- [src/searcher.py](/Users/Min369/Documents/同步空间/Manju/Projects/共享/AIProjects/UnivModel/学术书籍智能下载系统/src/searcher.py)
- [src/downloader.py](/Users/Min369/Documents/同步空间/Manju/Projects/共享/AIProjects/UnivModel/学术书籍智能下载系统/src/downloader.py)
- [src/database.py](/Users/Min369/Documents/同步空间/Manju/Projects/共享/AIProjects/UnivModel/学术书籍智能下载系统/src/database.py)
- [src/validator.py](/Users/Min369/Documents/同步空间/Manju/Projects/共享/AIProjects/UnivModel/学术书籍智能下载系统/src/validator.py)
- [src/reporter.py](/Users/Min369/Documents/同步空间/Manju/Projects/共享/AIProjects/UnivModel/学术书籍智能下载系统/src/reporter.py)

### 2.3 已做过的下载成功率增强

- 搜索候选结果落库，不再只保留单一下载链接
- 下载时按候选顺序自动回退
- 下载失败后自动尝试下一个候选
- 验证失败后自动尝试下一个候选
- 下载前过滤明显垃圾候选：
  - `preview`
  - `sample`
  - `cover`
  - `thumbnail`
  - `teacher / teachers manual`
  - `instructor / instructor manual`
  - `solutions manual`
  - `computer supplement`
  - 图片或元数据扩展名
  - 小于最小有效体积的候选
- 下载器增加：
  - 重试
  - `.part` 清理
  - 对 `archive.org` / `researchgate` 的备用请求头与变体请求
- 修复了“验证失败的坏文件会卡住后续候选”的问题

### 2.4 已人工判定的误下载与 wrong 目录同步

- `陈国良《并行计算导论》` 曾误下载为《天文学进展》论文《基于 Spark 分布式框架的海量星表数据时序重构方法研究》，已从 `completed` 改为 `failed`，并删除对应 ChinaXiv 错误候选。
- `Solar System Evolution (Chambers)` 曾误下载为 NASA Contractor Report 3077 `Significant Achievements in the Planetary Geology Program 1977-1978`，已从 `completed` 改为 `failed`，并删除对应 NTRS 错误候选。
- 现在可以直接运行 `python3 main.py --sync-wrong` 扫描 `downloads/**/wrong/*`，把人工放入 `wrong/` 的文件统一回写到数据库。
- 当前库已经跑过一轮 `--sync-wrong`：共匹配 `51` 个 wrong 文件，全部按人工判错回写为 `failed`，并删除各自当前错误候选链接。

## 3. 当前仍可确认的已完成下载

经过 `wrong/` 目录同步清洗后，当前数据库中仍保留为 `completed` 的主要书籍包括：

- `Introduction to Celestial Mechanics`
- `易照华《天体力学基础》南京大学出版社`
- `Theory of the Moon's Motion`
- `Lunar Sourcebook`
- `Physics of the Moon`
- `欧阳自远《月球科学概论》`
- `IERS Conventions (2010)`
- `Solving Ordinary Differential Equations I + II`
- `Numerical Recipes: The Art of Scientific Computing`
- `Time: From Earth Rotation to Atomic Physics`
- `The IAU 2000 Resolutions for Astrometry`

下载目录主要分布在：

- [downloads/月球物理](/Users/Min369/Documents/同步空间/Manju/Projects/共享/AIProjects/UnivModel/学术书籍智能下载系统/downloads/月球物理)
- [downloads/地球物理](/Users/Min369/Documents/同步空间/Manju/Projects/共享/AIProjects/UnivModel/学术书籍智能下载系统/downloads/地球物理)
- [downloads/太阳系多体动力学](/Users/Min369/Documents/同步空间/Manju/Projects/共享/AIProjects/UnivModel/学术书籍智能下载系统/downloads/太阳系多体动力学)
- [downloads/时间系统（TDB, TT, UTC）](/Users/Min369/Documents/同步空间/Manju/Projects/共享/AIProjects/UnivModel/学术书籍智能下载系统/downloads/时间系统（TDB,%20TT,%20UTC）)

## 4. 当前数据库中的失败书籍

当前 `status='failed'` 的 68 本里，既包括真实下载失败项，也包括用户人工放入 `wrong/` 后被系统打回的误下载项。下面这 17 本是接手时最值得优先关注的失败目标：

1. `Theory and Experiment in Gravitational Physics`
2. `Global Earth Physics: A Handbook`
3. `Introduction to Geophysics`
4. `Introduction to Space Dynamics`
5. `Accuracy and Stability of Numerical Algorithms`
6. `Explanatory Supplement to the Astronomical Almanac`
7. `The Moon: From Interior to Exterior`
8. `Data Analysis for Physical Applications`
9. `The Planetary and Lunar Ephemerides DE430 and DE440`
10. `Lunar Laser Ranging: A Continuing Legacy`
11. `Computer Arithmetic and Error Analysis`
12. `Approximation Theory and Practice`
13. `Fundamentals of Astrometry`
14. `Solving Ordinary Differential Equations II`
15. `Geometric Numerical Integration: Structure-Preserving Algorithms for Ordinary Differential Equations`
16. `Symplectic Geometric Algorithms for Hamiltonian Systems`
17. `A Hierarchical O(N log N) Force-Calculation Algorithm`

这几本的共同特征：

- 候选基本都已经在库里
- 主要卡在源站层面
- 常见报错：
  - `HTTP 401`
  - `HTTP 403`
  - `HTTP 500`
  - `SSLEOFError`
  - `RemoteDisconnected`

结论：这些失败项现在混合了两类来源：

- 真实源站失败：`401/403/500`、`SSLEOFError`、`RemoteDisconnected`
- 人工判错回写：文件已被用户放入 `wrong/`，系统通过 `--sync-wrong` 统一改回 `failed`

## 5. 用户确认的剩余目标清单

用户明确列出的剩余目标如下。注意：其中 `Post-Newtonian Geodesy and Relativistic Metrology` 和 `IAU Resolutions on Astronomical Constants & Reference Systems` 在当前数据库中已标记为 `completed`，Claude Code 接手时建议先用 `python3 main.py --stats` 和数据库查询核对落盘文件。

### 5.1 太阳系多体动力学

- [ ] `孙义燧《太阳系动力学》`

### 5.2 广义相对论

- [ ] `韦琳《相对论天体力学》`
- [ ] `Post-Newtonian Geodesy and Relativistic Metrology (Soffel et al.)`
- [ ] `IAU Resolutions on Astronomical Constants & Reference Systems`

### 5.3 月球物理

- [ ] `The Moon: From Interior to Exterior (Wieczorek et al.)`
- [ ] `Selenology: The Science of the Moon (Back)`

### 5.4 地球物理

- [ ] `陈颙《地球物理学基础》`

### 5.5 卫星轨道摄动

- [ ] `刘林《卫星轨道摄动》`

### 5.6 观测数据拟合（雷达测距、LLR、VLBI）

- [ ] `Data Analysis for Physical Applications (Bevington & Robinson)`
- [ ] `Lunar Laser Ranging: Science and Data Analysis`
- [ ] `JPL Planetary and Lunar Ephemerides (Standish et al.)`
- [ ] `The Planetary and Lunar Ephemerides DE430 and DE440 (Folkner et al.)`
- [ ] `Lunar Laser Ranging: A Continuing Legacy (Dickey et al., Science 1994)`
- [ ] `VLBI: A New Window on the Universe (Zensus et al.)`
- [ ] `冼鼎钧《天体测量学》`

### 5.7 数值积分（多步法、变步长）

- [ ] `Computer Arithmetic and Error Analysis (Wilkinson)`
- [ ] `徐树方《数值稳定性分析》`

### 5.8 坐标系变换

- [ ] `Fundamentals of Astrometry (Kovalevsky & Seidelmann)`

### 5.9 N-body 微分方程的数值积分

- [ ] `Solving Ordinary Differential Equations II (Hairer & Wanner)`
- [ ] `Geometric Numerical Integration: Structure-Preserving Algorithms (Hairer, Lubich, Wanner)`
- [ ] `Symplectic Geometric Algorithms for Hamiltonian Systems (Kang Feng/Mengzhao Qin)`
- [ ] `田刚《辛几何与哈密顿系统》`

### 5.10 大规模 N-body 和并行计算

- [ ] `A Hierarchical O(N log N) Force-Calculation Algorithm (Barnes & Hut, Nature 1986)`

## 6. 当前数据库中的 pending 书籍

当前还有 `16` 本 `pending`：

- `孙义燧《太阳系动力学》`
- `Gravitational Waves: Theory and Experiments`
- `梁灿彬《微分几何与广义相对论》科学出版社`
- `韦琳《相对论天体力学》`
- `俞允强《广义相对论引论》`
- `Selenology: The Science of the Moon`
- `陈颙《地球物理学基础》`
- `刘林《卫星轨道摄动》`
- `Lunar Laser Ranging: Science and Data Analysis`
- `JPL Planetary and Lunar Ephemerides`
- `VLBI: A New Window on the Universe`
- `冼鼎钧《天体测量学》`
- `徐树方《数值稳定性分析》`
- `Numerical Methods for Least Squares Problems`
- `崔希璋等《广义测量平差》武汉大学出版社`
- `田刚《辛几何与哈密顿系统》`

## 7. 可直接接手运行的命令

### 7.1 看总体状态

```bash
python3 main.py --stats
```

### 7.2 继续搜索待处理书籍

```bash
python3 main.py --search
```

说明：

- `--search` 只会处理 `pending`
- 如果搜索到候选，会写入 `search_results`
- 最佳结果会把该书状态改成 `found`

### 7.3 下载已找到的书籍

```bash
python3 main.py --download
```

说明：

- 当前实现会处理 `found`、`failed`、`validation_failed`
- 如果只想继续处理新找到的书，建议先确认数据库中 `found` 数量

### 7.4 查看候选结果

```bash
python3 main.py --candidates
python3 main.py --candidates --book-id 61
```

### 7.5 生成报告

```bash
python3 main.py --report --report-format md
python3 main.py --report --report-format xlsx
```

### 7.6 同步人工判错的 wrong 目录

```bash
python3 main.py --sync-wrong
```

说明：

- 扫描 `downloads/**/wrong/*`
- 优先按 `books.file_path` 文件名匹配
- 匹配不到时退化到“书名 + 作者规范化”弱匹配
- 一旦命中，统一将该书改为 `failed`
- 清空 `file_path` 与 `download_url`
- 删除该书当前 `download_url` 对应的错误候选
- 记录一条 `source='wrong_folder'`, `status='wrong_file'` 的日志
- 不删除 `wrong/` 目录中的原始文件

### 7.6 重新验证已下载文件

```bash
python3 main.py --validate
```

## 8. Claude Code 接手时建议的执行顺序

建议顺序：

1. 先跑：

```bash
python3 main.py --stats
```

2. 再跑搜索：

```bash
python3 main.py --search
```

3. 若 `found > 0`，再跑下载：

```bash
python3 main.py --download
```

4. 如果再次遇到长时间没有新命中：

- 不要反复只撞 `Google Scholar`
- 不要让 `failed` 项反复拖慢整批流程
- 优先继续挖 `pending`
- 对个别高价值失败项，单独定向补候选

## 9. 已知注意事项

### 9.1 当前最大瓶颈不是本地代码，而是外部源

最常见问题：

- `Google Scholar` 经常 `429`
- `arXiv` 偶发 SSL 中断
- `Internet Archive` 偶发 `401/403/500` 或 SSL 中断
- `Libgen` 在当前网络环境下常常是远端直接断开连接

### 9.2 不要误判“找到候选”就一定能下载

经验上：

- `found` 只表示候选存在
- 真正能否落盘，取决于候选链接当下是否可访问
- `archive.org` 很多候选元数据存在，但直链下载可能失败

### 9.3 当前下载逻辑中最重要的改动不要回退

不要丢掉这些行为：

- 候选自动回退
- 无效文件删除
- 垃圾候选过滤
- `archive.org` / `researchgate` 备用请求策略

否则会明显降低成功率。

## 10. 如果 Claude Code 想进一步提高成功率，优先建议

优先级从高到低：

1. 对剩余 `pending` 书目继续补新来源
2. 对当前 `failed` 的 6 本单独做定向候选补充
3. 必要时给 `--download` 增加“只下载 found、跳过 failed”的开关
4. 必要时给 `--search` 增加“按书名范围/ID范围搜索”的能力，便于断点推进

## 11. 已验证通过的测试

最近确认通过的本地测试：

```bash
python3 tests/test_download_fallback.py
python3 tests/test_candidate_filtering.py
python3 -m py_compile main.py src/downloader.py
```

这些测试覆盖了：

- 下载失败后回退
- 验证失败后回退
- 无效文件清理
- 垃圾候选过滤

## 12. 一句话交接结论

当前系统已经从“单链接碰运气下载”推进到“候选持久化 + 自动回退 + 文件验证 + 垃圾候选过滤 + 备用请求策略 + wrong目录人工纠错同步”的状态。当前数据库显示已正确完成 `10/95` 本、`68` 本已失败、`17` 本待继续搜索；后续 Claude Code 的重点不该放在重写下载器，而应放在围绕剩余 `pending` 和重点 `failed` 书目继续挖新的可靠候选来源。
