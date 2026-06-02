<!-- source: 并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk).pdf -->

<!-- pdf_type: normal; pages: 451; chunk_pages: 70 -->


<!-- chunk 0001: pages 1-70 -->
# 面向21世纪课程教材 Textbook Series for 21st Century

# 并行计算

结构·算法·编程

陈国良编著

# Parallel Computing:

Architecture, Algorithm and Programming

# 面向21世纪课程教材 Textbook Series for 2lst Century

# 并行计算

结构·算法·编程

陈国良 编著

# 图书在版编目(CIP)数据

并行计算—-结构·算法·编程/陈国良编著．-北京：高等教育出版社,1999.10(2001重印）

21世纪课程教材

ISBN 7 - 04 - 007739 -6

I．并…Ⅱ.陈…Ⅲ.并行算法-高等学校-教材Ⅳ.T

P301.6

# 中国版本图书馆CIP数据核字(1999)第37258号

并行计算—结构·算法·编程陈国良编著

<table><tr><td colspan="2">出版发行</td><td>高等教育出版社</td><td colspan="2"></td><td></td></tr><tr><td>社</td><td>址</td><td>北京市东城区沙滩后街55号</td><td colspan="2">邮政编码100009</td><td></td></tr><tr><td>电</td><td>话</td><td>010 - 64054588</td><td></td><td></td><td>传真010-64014048</td></tr><tr><td>网</td><td></td><td>址http://www.hep.edu .cn</td><td></td><td></td><td></td></tr><tr><td>经</td><td></td><td>销新华书店北京发行所</td><td></td><td></td><td></td></tr><tr><td>印</td><td></td><td>刷北京地质印刷厂</td><td></td><td></td><td></td></tr><tr><td>开</td><td>本</td><td>：787×960 1/16</td><td>版</td><td>次</td><td>1999年10月第1版</td></tr><tr><td>印</td><td>张</td><td>28.25</td><td>印</td><td></td><td>次2001年5月第2次印刷</td></tr><tr><td>字</td><td>数</td><td>520 000</td><td>定</td><td></td><td>价23.70元</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

凡购买高等教育出版社图书，如有缺页、倒页、脱页等质量问题，请在所购图书销售部门联系调换。

# 作者简介

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0070/auto/images/cb8dabaad36d163e0724cea0f9f395488e8dd6d3eb1084206e3a0aa8b8ed693b.jpg)

陈国良,中国科学技术大学教授,博士生导师,1938年6月生于安徽省颖上县,1961年毕业于西安交通大学无线电系计算机专业。现任国家高性能计算中心（合肥)主任,国家教育部高等学校计算机科学技术教学指导委员会副主任，全国高等教育电子、电工与信息类专业自考指导委员会副主任，安徽省高校计算机基础课程教学指导委员会副主任，中国计算机学会理事，中国计算机学会开放系统专业委员会副主任，中国数学会计算数学并行计算专业委员会委员，中国计算机学会数据通信与计算机网络专业委员会委员，全国自然科学名词审定委员会委员。曾任中国科学技术大学计算机系主任和安徽省计算机学会理事长。享受国家政府特殊津贴。

陈国良教授长期从事计算机科学技术的教学与研究工作。主要研究领域为并行算法、计算机体系结构、计算机网络和神经计算等。先后主持完成了10多项国家863计划、国家攀登计划、国家自然基金、教育部博士基金等科研项目。取得了多项被国内外广泛引用的、达到国际先进水平的科研成果，发表论文100多篇，出版著作7部、译著5部,参与主编计算机类辞典、词汇5部，主审、主编计算机类各种教材8部。曾获国家级二等奖以及部、省、院级一等、二等、三等奖共10项。

十几年来，陈国良教授先后指导计算机专业硕士研究生40余名和博士研究生30余名，率先创建了我国第一个国家高性能计算中心，为我国培养了一批在国内外从事算法研究的高级人才。

# 前 言

写作背景近几年来，世界上和我国高性能并行计算机的发展取得长足进展，每秒数百亿次、数千亿次乃至数万亿次计算能力的高端并行机已相继研制成功，使得以前许多无法求解和研究的问题现在已经成为可能。随着计算技术和计算方法的飞速发展,当今几乎所有学科均趋向定量化和精确化，从而产生了诸如计算物理学、计算化学、计算材料学、计算力学、计算生物学、计算气象学和计算电子学等新兴学科,在世界上逐渐形成了所谓计算科学与工程CSE(Compu-tational Science and Engineering)的计算性学科分支。计算,增强了人们从事科学研究的能力，拓宽了人们洞察自然的视野，加速了科技转化为生产力的过程，深刻地改变着人类认识世界和改造世界的方法和途径。计算科学(Computa-tional Sciences)，已经和传统的理论科学与实验科学并列成为第三门学科，它们彼此相辅相成地推动着人类科技发展和社会进步。

在此情况下，为了适应高性能并行机迅速发展的形势，满足国家培养面向21世纪高科技人才的需求，在高校开设高性能并行计算(High-Performance Par-allel Computing)课程已提到了议事日程。为此，国家教育部高等学校计算机科学技术教学指导委员会经过多次讨论，把<并行计算>这本教材列为国家“九五”教材规划，并最后审定为“面向21世纪课程教材”。

篇章内容本书以并行计算为主题，主要讨论并行计算的硬件基础—当代并行计算机系统及其结构模型,并行计算的核心内容—并行算法设计与并行数值算法以及并行计算的软件支持一一并行程序的设计原理与方法。本书强调融并行机结构、并行算法和并行编程为一体，着重讨论并行算法的设计方法和并行数值算法，力图反映本学科的最新成就和发展趋势。

全书共十五章，分为四篇：第一篇为并行计算硬件基础，包括并行计算机系统及其结构模型(第一章),当代并行机系统 SMP、MPP和COW(第二章）,并行计算性能评测(第三章);第二篇为并行算法的设计，包括并行算法的设计基础(第四章),并行算法的一般设计方法(第五章),并行算法的基本设计技术(第六章）,并行算法的一般设计过程(第七章);第三篇为并行数值算法，包括基本通信操作(第八章),稠密矩阵运算(第九章),线性方程组的求解(第十章),快速傅里叶变换(第十一章);第四篇为并行程序设计,包括并行程序设计基础(第十二章),并行程序设计模型和共享存储系统编程(第十三章),分布存储系统并行编程(第十四章),并行程序设计环境与工具(第十五章)。书中取材新颖,内容丰富，体系完整，基本上包括了并行计算学科中的主要研究内容和主要研究方面。

使用方法国家教育部计算机科学与技术教学指导委员会，将并行计算课程定位在高等学校计算机及相关专业本科高年级学生和研究生层次上。学生应在学习过计算机体系结构、操作系统、编译原理以及最好学习过算法设计与分析(至少应学习过数据结构和图论)等课程之后学习本课程。全书内容可根据不同的教学对象进行不同的组合。但根据本课程的定位，作为必须讲授和最低60学时的教学要求,建议讲授章节和相应的学时分配如下：

<table><tr><td rowspan=1 colspan=1>章名</td><td rowspan=1 colspan=1>建议讲授节次</td><td rowspan=1 colspan=1>建议学时</td></tr><tr><td rowspan=1 colspan=1>第一章</td><td rowspan=1 colspan=1>1.1.1,1.1.2,1.2.2,1.2.3,1.2.4,1.3.1,1.3.2</td><td rowspan=1 colspan=1>4</td></tr><tr><td rowspan=1 colspan=1>第二章</td><td rowspan=1 colspan=1>2.1.1,2.2.1,2.3.1,2.4.1,2.4.2</td><td rowspan=1 colspan=1>4</td></tr><tr><td rowspan=1 colspan=1>第三章</td><td rowspan=1 colspan=1>3.1,3.2</td><td rowspan=1 colspan=1>4</td></tr><tr><td rowspan=1 colspan=1>第四章</td><td rowspan=1 colspan=1>4.2.1~4.2.6</td><td rowspan=1 colspan=1>4</td></tr><tr><td rowspan=1 colspan=1>第五章</td><td rowspan=1 colspan=1>5.1.1,5.2.1,5.2.3,5.3.2</td><td rowspan=1 colspan=1>2</td></tr><tr><td rowspan=1 colspan=1>第六章</td><td rowspan=1 colspan=1>6.1,6.2,6.5</td><td rowspan=1 colspan=1>4</td></tr><tr><td rowspan=1 colspan=1>第七章</td><td rowspan=1 colspan=1>7.1,7.2,7.4.1,7.5</td><td rowspan=1 colspan=1>2</td></tr><tr><td rowspan=1 colspan=1>第八章</td><td rowspan=1 colspan=1>8.1,8.3,8.4</td><td rowspan=1 colspan=1>2</td></tr><tr><td rowspan=1 colspan=1>第九章</td><td rowspan=1 colspan=1>9.1,9.3,9.4</td><td rowspan=1 colspan=1>4</td></tr><tr><td rowspan=1 colspan=1>第十章</td><td rowspan=1 colspan=1>10.1,10.2,10.3,10.4.2~10.4.4,10.4.6</td><td rowspan=1 colspan=1>6</td></tr><tr><td rowspan=1 colspan=1>第十一章</td><td rowspan=1 colspan=1>11.1.2~11.1.4,11.3.1,11.3.2,11.3.4</td><td rowspan=1 colspan=1>4</td></tr><tr><td rowspan=1 colspan=1>第十二章</td><td rowspan=1 colspan=1>12.1.1,12.1.3,12.3,12.5.3</td><td rowspan=1 colspan=1>2</td></tr><tr><td rowspan=1 colspan=1>第十三章</td><td rowspan=1 colspan=1>13.1.2,13.2,13.3.2</td><td rowspan=1 colspan=1>4</td></tr><tr><td rowspan=1 colspan=1>第十四章</td><td rowspan=1 colspan=1>14.2,14.5</td><td rowspan=1 colspan=1>6</td></tr><tr><td rowspan=1 colspan=1>第十五章</td><td rowspan=1 colspan=1>15.2,15.3.1,15.3.2</td><td rowspan=1 colspan=1>4</td></tr></table>

书中其余部分的内容可由任教老师任选，而带 $\pmb { \mathscr { k } }$ 号的章节是建议阅读的,它们或是预备性知识(希望不熟悉的读者课前预习),或是深人研究性内容(鼓励面向研究的读者深入阅读)。每章之末均有小结和导读(指导读者进一步追踪阅读),并附有适量的、密切结合课文的以及拓宽讲授内容的综合性习题。

为了配合讲授内容，有条件的学校应开设SMP平台、MPP平台和COW平台上的实验课程，每种平台至少安排 $2 \sim 3$ 个小型综合练习程序，并提倡利用In-ternet浏览本书末提供的有关 ${ \bf W } \mathrm { e b }$ 网址中的内容。确有困难的学校,应至少安排COW环境下的分布计算练习程序。

为了增强本书的好用性，撰写时尽量分点叙述、纲目清晰。全书除了提供必要的参考文献外，还开列了并行和分布计算 ${ \bf W } \mathbf { e b }$ 网址、算法清单、示范程序清单以及术语中-英对照及索引。尽管后者在使用上尚不如英文索引来得方便，但毕竟在一定程度上方便了读者的查阅。

相关读物本书在撰写时力图自成完备系统，但由于本书内容涉及面较广，所以读者参阅必要的相关教材是有益处的。特别是，在可扩放并行计算方面，建议配合阅读KaiHwang 和 Zhiwei $\mathbf { X } \mathbf { u }$ 的新著 Scalable Parallel Computing:Tech-nology,Architecture,Programming(McGraw-Hill,1998）;在并行算法方面,建议配合阅读陈国良编著的《并行算法的设计与分析>(高等教育出版社，1994)；在设计和构造并行程序方面,建议配合阅读I.Foster 的著作Designingand BuildingParallel Programs : Concepts and Tools for Parallel Software Engineering (Addi-son-Wesley,1995);在数值并行算法方面,建议配合阅读M.J.Quinn的著作Parallel Computing:Theory and Practice（McGraw-Hill,1994)和 V. Kumar 等的著作 Introduction to Parallel Computing: Design and Analysis of Algorithms(Benjamin/Cummings,1994）。

感谢本书在撰写中,曾直接或间接地引用了许多专家、学者的文献,特别是对我国计算机学科发展卓有贡献的世界著名计算机结构学家黄铠教授，他非常关心国内计算机教育事业,及时向我们提供了他和徐志伟教授的著名新作ScalableParallelComputing,从而丰富了本书的内容,作者尤为感谢。书稿付梓前承蒙清华大学王鼎兴教授抱病进行了审校，作者倍加感谢。他的严谨治学作风和顽强拚搏精神激励和鞭策作者努力把书稿写好、改好。

中国科学技术大学计算机系纪金龙老师、安虹和计永昶博士为本书的第十四章和第十五章的写作提供了丰富的素材，并帮助我完成第四篇的教学工作,作者甚为感谢。

中国科学技术大学计算机系的历届学生们,在听取我的讲授中,曾提出过很多可贵意见,不断充实和完善了书稿的内容,特别是张青山、孙伟、严宝拾、吴名桥、侯海龙和陈志辉等同学完成了本书的计算机绘图工作。对于他们的辛勤劳动和良好的愿望，作者深感欣慰和谢意。

最后，感谢国家高性能计算中心(合肥)和中国科学技术大学计算机系为本书的写作提供了良好的条件。

国家教育部将<并行计算>一书审定为“面向21世纪课程教材”,作者感到荣幸。但并行计算涉及学科很多，内容十分广泛，加上作者学识有限,写作时间仓促，书中错误和片面之处在所难免，恳请读者不吝批评指正。

陈国良

中国科学技术大学计算机系国家高性能计算中心(合肥)1999年5月

责任编辑 鲍湧  
封面设计 张楠  
版式设计 鲍湧 周顺银  
责任校对 马桂兰  
责任印制 宋克学

# 目 录

# 第一篇 并行计算硬件基础

# 第一章并行计算机系统及其结构模型

1.1并行计算与高端并行计算机 3

1.1.1并行计算与计算科学 31.1.2当代科学与工程问题的计算需求 4$\yen 12$ 万亿次高端并行机…

1.2并行计算机系统互连 9

1.2.1系统互连  
1.2.2静态互连网络 10  
1.2.3动态互连网络 13  
1.2.4宽带互连网络 17

1.3并行计算机系统结构. 21

1.3.1并行计算机结构模型 21  
1.3.2并行计算机访存模型 25  
$\yen 123,3$ 并行计算机存储组织 29

1.4小结和导读. 33 习题…· 34

# 第二章当代并行机系统:SMP、MPP和COW. 38

2.1对称多处理机 SM.… 38

2.1.1 SMP 和 CC-NUMA 结构特性. 38  
$\yen 2.1,2$ SGI/Cray Origin 2000 超级服务器… 40

.2大规模并行机MPP 47

2.2.1 MPP结构特性 47  
$\yen 2.2.2$ 机群型大规模并行机 SP2 51  
2.3工作站机群COW 57  
2.3.1 COW的基本原理与技术 58  
$\yen 2.3.2$ Berkeley 的 NOW计划 61

2.4国产曙光系列并行机系统 67

2.4.1全对称共享存储多处理机系统:曙光1号 68  
2.4.2大规模并行处理系统:曙光－1000 72  
$\times 2 . 4 . 3$ 超级并行计算机系统：曙光－2000 75

# 2.5小结和导读. 80

习题 81

# 第三章并行计算性能评.… 83

3.1加速比性能定律. 83

3.1.1 Amdahl 定律 83  
3.1.2 Gustafson 定律 85  
3.1.3Sun 和Ni定律 85  
3.1.4有关加速的讨论· 87

3.2可扩放性评测标准 88

3.2.1并行计算的可扩放性 88  
3.2.2等效率度量标准. 89  
3.2.3 等速度度量标准 91  
3.2.4平均延迟度量标准 95  
3.2.5有关可扩放性标准的讨论 97

$\yen 3.3$ 基准测试程序 99

3.3.1基本测试程序 99  
3.3.2数学库测试程序 100  
3.3.3并行测试程序 101

3.4小结和导读 102 习题… 102

# 第二篇并行算法的设计

# 第四章并行算法的设计基础… 107

$\yen 4.1$ 并行算法的基础知识 107

4.1.1并行算法的定义和分类 107  
4.1.2并行算法的表达 108  
4.1.3并行算法的复杂性度量 109  
4.1.4并行算法中的同步与通信 110

# 4.2并行计算模型 112

4.2.1 PRAM模型 112  
4.2.2异步 PRAM模型 113  
4.2.3 BSP模型… 114  
4.2.4logP模型 116  
4.2.5 ${ \mathrm { C } } ^ { 3 }$ 模型 118  
4.2.6对BSP和 $\mathrm { l o g P }$ 的评注 121

4.3小结和导读. 123 习题…· 124

# 第五章并行算法的一般设计方… 129

5.1串行算法的直接并行化 129

5.1.1 设计方法描述 129  
5.1.2快排序算法的并行化 130

5.2从问题描述开始设计并行算法… 132

5.2.1串匹配算法 132  
$\ast 5 . 2 . 2$ KMP串行串匹配算法… 133  
5.2.3并行串匹配算法的设计思路 136

5.3借用已有算法求解新问题 137

5.3.1设计方法描述 137  
5.3.2利用矩阵乘法求所有点对间最短路径 138

5.4小结和导读 141

习题…… 141

# 第六章并行算法的基本设计技… 144

6.1划分设计技术. 144

6.1.1 均匀划分技术 144  
6.1.2方根划分技术 146  
6.1.3对数划分技术 146  
6.1.4功能划分技术 148

6.2分治设计技… 149

6.2.1双调归并网络 149  
6.2.2凸壳问题 151

6.3平衡树设计技术 153

6.3.1求取最大值 153  
6.3.2计算前缀和 154

6.4倍增设计技… 155

6.4.1表序问题的计算 155  
6.4.2 求森林的根 156

6.5流水线设计技术 158

6.5.1一维心动阵列上的DFT计算 158  
6.5.2一维心动阵列上的卷积计算 159

6.6小结和导读… 161 习题… 162

# 第七章并行算法的一般设计过程. 164

7.1PCAM 设计方法学. 164

7.2划分 165

7.2.1域分解 166  
7.2.2功能分解 166  
7.2.3划分判据 167

7.3通信 167

7.3.1局部通信 168   
7.3.2全局通信 169   
7.3.3非结构化、动态和异步通信 170   
7.3.4通信判据 170

7.4 组合…· 171

7.4.1增加粒度 171  
7.4.2保持灵活性和减少软件工程成本 174  
7.4.3组合判据 174

7.5映射 175

7.5.1负载平衡算法 175   
7.5.2任务调度算法 177   
7.5.3映射判据… 177

7.6小结和导读 178 习题…· 179

# 第三篇 并行数值算法

第八章 基本通信操作 \*\*\*. 185

8.1选路方法与开关技术 185

8.1.1选路方法 185  
8.1.2开关技术 187

8.2单一信包一到一传输 189

8.3一到多播送 190

8.3.1 使用 SF进行一到多播送·… 190  
8.3.2使用CT进行一到多播送 191

# 8.4多到多播送 193

8.4.1 使用 SF进行多到多播送… 193  
8.4.2使用CT进行多到多播送· 195

8.5小结和导读 196

习题… 198

# 第九章稠密矩阵运算 203

9.1矩阵的划分 203

9.1.1带状划分 203   
9.1.2棋盘划分 204

9.2矩阵转置 205

9.2.1棋盘划分的矩阵转置 205   
9.2.2带状划分的矩阵转置 208

9.3矩阵-向量乘法· 209

9.3.1带状划分的矩阵-向量乘法 210   
9.3.2棋盘划分的矩阵-向量乘法 211

9.4矩阵乘法 213

9.4.1简单并行分块乘法 214   
9.4.2 Cannon乘法 215   
9.4.3 Fox乘法… 218   
9.4.4 DNS乘法 218

9.5小结和导读· 223 习题… 224

# 第十章线性方程组的求解 227

10.1三角形方程组的求解 227

10.1.1 基本术语 227  
10.1.2上三角方程组的求解 228

10.2三对角方程组的求解. 230

10.2.1三对角方程组直接求解法 230   
10.2.2三对角方程组奇偶归约求解法… 232

10.3稠密线性方程组的求解. 233

10.3.1有回代的高斯消去法 233   
10.3.2无回代的高斯－约旦法 237   
10.3.3迭代求解的高斯－赛德尔法 239

10.4稀疏线性方程组的求解 241

10.4.1稀疏矩阵的存储方式 … 241

10.4.2雅可比迭代法 243  
10.4.3 高斯-赛德尔迭代法 247  
10.4.4超松弛迭代法 249  
10.4.5多重网格法 249  
10.4.6共轭梯度法 251

10.5小结和导读…. 256 习题 257

# 第十一章快速傅里叶变换… 260

11.1离散傅氏变换 260

\*11.1.1预备知识 260  
11.1.2离散傅里叶变换 261  
11.1.3离散傅里叶逆变换 263  
11.1.4离散傅氏变换的蝶式计算 263

$\yen 12$ 快速傅氏变换串行算法… 265

11.2.1 串行FFT迭代算法 · 265   
11.2.2 串行FFT递归算法 267

11.3并行 FFT算法… 269

11.3.1 SIMD-MC²上FFT算法 269  
11.3.2 SIMD-BF上FFT算法 ： 272  
11.3.3 SIMD-CC上FFT算法 273  
11.3.4 MIMD-DM上FFT算法 275

11.4小结和导读 278 习题… 279

# 第四篇 并行程序设计

第十二章并行程序设计基础 283

12.1并行程序设计概述. 283

12.1.1申行程序设计与并行程序设计 283  
12.1.2并行程序设计环境 285  
12.1.3并行程序设计方法 285

$\yen 12.2$ 进程 287

12.2.1进程的基本概念 287  
12.2.2进程的并行执行 290  
12.2.3进程的相互作用 291

12.3线程 292

12.3.1线程的基本概念 293  
12.3.2线程的管理 293  
12.3.3线程的同步 295

$\yen 12.4$ 同步 295

12.4.1原子与互斥 295   
12.4.2高级同步结构 296   
12.4.3低级同步原语 297

12.5通信 299

12.5.1影响通信系统性能的因素 300  
12.5.2低级通信支持 301  
12.5.3TCP/IP通信协议组简介. 302

12.6小结和导.… 306

习题… 306

# 第十三章并行程序设计模型和共享存储系统编程 309

13.1并行编程风范和样本程序. 309

13.1.1 五种并行编程风范 309   
13.1.2计算 $\pmb { \pi }$ 样本程序 310

13.2并行程序设计模型 312

13.2.1隐式并行模型 312  
13.2.2数据并行模型 313  
13.2.3消息传递模型 314  
13.2.4共享变量模型 316  
13.2.5并行程序设计模型比较 317

.13.3共享存储并行编程 318

13.3.1 ANSIX3H5共享存储模型 320  
13.3.2 POSIX线程模型 322  
13.3.3 Open MP标准. 323

13.4小结和导读…. 326 习题 327

# 第十四章分布存储系统并行编程… 332

14.1基于消息传递的并行编程· 332

14.1.1 SPMD并行程序... 333  
14.1.2 MPMD并行程序 334

14.2MPI并行编程 335

14.2.1最基本的 MPI ·336

14.2.2群体通信 338  
14.2.3通信体 340  
14.2.4导出数据类型 342  
14.2.5点到点通信 343

\*14.3PVM并行编程. 348

14.3.1 PVM概貌 348   
14.3.2 PVM消息传递库 349

14.4基于数据并行的并行编程… 352

14.4.1数据并行模型的特点 352  
14.4.2数据并行编程的基本问题 352

14.5HPF并行编程 353

14.5.1 HPF的语言特点 354  
14.5.2 HPF的数据并行机制 354  
14.5.3 HPF使用中的若干问题 359

14.6小结和导读…. 361

习题…… 362  
附录一 MPI的函数的C语言说明 366  
附录二 MPI的函数的 Fortran语言说明 368

# 第十五章并行程序设计环境与工具… 371

$\yen 15.1$ 软件工具与环境… 371

15.1.1编码工具 371  
15.1.2 软件工程工具 372  
15.1.3集成工具 372  
15.1.4将来的工具与环境 373

15.2并行编译器... 374

15.2.1 编译及其并行化 375  
15.2.2相关分析 377  
15.2.3代码优化 379  
15.2.4代码生成 384

15.3并行程序调试和性能分析. 384

15.3.1并行程序的调试 384  
15.3.2并行程序的性能分析 387  
15.3.3并行程序的可视化设计环境与工具 389

# 15.4小结和导读. 390

习题 391

算法索引 394  
表格索引… 396  
示范程序索引 398  
参考文献… 399  
并行与分布计算Web 网址 409  
术语中－英对照及索引… 415

# 第一篇 并行计算硬件基础

# 第一章 并行计算机系统及其结构模型第二章 当代并行机系统:SMP、MPP和COW第三章 并行计算性能评测

这一篇主要研究并行计算的硬件基础，包括并行计算机系统及其结构模型(第一章),当代主流并行计算机系统 SMP、MPP和COW(第二章)以及并行计算系统的性能评测(第三章)。但它与高级计算机体系结构课程不一样,本篇只是从并行计算的角度,介绍一些与并行计算直接相关的并行计算机系统方面的知识。

本篇的第一章，首先从当代科学与工程问题的计算需求出发，简单介绍并行计算与计算科学以及万亿次高端并行机;接着讨论并行系统互连方式与技术；最后落实到并行计算机的结构模型与存储模型的介绍上，希望这些抽象的模型能够成为计算工作者与工程师的界面。第二章,将从并行机中抽出当代流行的可扩放的并行机类加以简单介绍,它们包括共享存储的对称多处理机(SMP)和分布存储的大规模并行机(MPP)以及松散耦合的分布式工作站机群(COW),这些都是并行计算工作者的最基本的硬件环境。第三章,将讨论并行计算性能评测问题,包括衡量并行计算性能的加速比、可扩放性以及基准测试程序，它们都是计算工作者、计算机厂商和计算机用户共同感兴趣的问题,而且能被一致认可和普遍接受。

# 第一章 并行计算机系统及其结构模型

简单地讲,并行计算就是在并行计算机或分布式计算机等高性能计算系统上所作的超级计算,其物质基础是高性能并行计算机(包括分布式网络计算机)。本章首先从当代科学与工程问题的计算需求出发,先简单地讨论并行计算与计算科学以及万亿次高端并行机(High-End Parallel Computer);然后讨论并行系统的互连,包括静态互连网络、动态互连网络和宽带互连网络;最后讨论并行计算机的系统结构模型(PVP、SMP、MPP、DSM和COW)、并行计算机的存储访问模型(UMA、NUMA、COMA、CC-NUMA和NORMA)以及并行计算机的存储组织(层次存储技术和高速缓存一致性问题)。

# 1.1 并行计算与高端并行计算机

# 1.1.1并行计算与计算科学·

并行计算(Parallel Computing),简单地讲,就是在并行计算机上所作的计算,它和常说的高性能计算（High Performance Computing）、超级计算（SuperComputing)是同义词,因为任何高性能计算和超级计算总离不开使用并行技术。随着计算机和计算方法的飞速发展,几乎所有的学科都走向定量化和精确化，从而产生了一系列诸如计算物理、计算化学、计算生物学、计算地质学、计算气象学和计算材料科学等的计算科学,在世界上逐渐形成了一门计算性的学科分支,即计算科学与工程,简称为 CSE(Computational Science & Engineering)。当今,计算科学已经和传统的两种科学,即理论科学和实验科学,并列成为第三门科学，它们彼此相辅相成地推动科学发展与社会进步。在许多情况下,或者是理论模型复杂甚至理论尚未建立,或者实验费用昂贵甚至实验无法进行,此时计算就成为求解问题的唯一或主要手段。计算极大地增强了人们从事科学研究的能力，大大地加速了把科技转化为生产力的过程,深刻地改变着人类认识世界和改造世界的方法和途径。计算科学的理论和方法,作为新的研究手段和新的设计与制造技术的理论基础,正推动着当代科学与技术向纵深发展。

计算科学涉及到大型科学工程计算,是一个多学科的交叉领域,往往需要数学家、工程师和计算机科学家进行跨学科和跨行业的协同研究。一方面，它需要运用许多基础数学理论(如非线性分析、现代偏微分方程理论、微分几何和近世代数等);另一方面又需要熟悉某一特定应用领域的背景知识;最后还需要充分掌握和运用先进的计算设备。所以今后的科学与工程计算工作者应尽可能兼备数学、物理、工程科学和计算机科学等多方面的知识,并善于应用超级计算机进行大规模数值试验与分析。

# 1.1.2当代科学与工程问题的计算需求

应用需求人类对计算机性能的要求是无止境的，在诸如预测模型的构造和模拟、工程设计和自动化、能源勘探、医学、军事以及基础理论研究等领域中都对计算提出了极高的具有挑战性的要求。例如，在作数值气象预报时,要提高全球气象预报的准确性，据估计在经度、纬度和大气层方向上至少要取 $2 0 0 \times 1 0 0$ $\times 2 0 = 4 0$ 万个网格点。目前中期天气预报有的模式需要635万个点，内存需要几十吉字节 $( 1 \mathrm { G B } = 1 0 ^ { 9 } \mathrm { B } )$ ，总运算量达 $2 5 \mathrm { T } ( \mathrm { T } = 1 0 ^ { 1 2 } ) \ .$ ），并要求在不到2小时内完成48小时的天气预报。当计算能力不足时，只好降低结果的分辨率，简化计算方案,从而就影响了预报的准确度。又如,在进行油田整体“油藏模拟”时,假定一个油田有上万口井，每口井模拟时至少要取8×8×50个点，则总的变量个数可高达千万量级,使得现今的一般计算机难以实现。其它的应用领域包括核武器数值模拟，航空航天高速飞行器的设计,原子物理过程微观世界的模拟，材料科学中计算，环境资源以及生物计算等。这些重大的计算问题，涉及到非规则的复杂结构、非均匀的复合材料、非线性的动力学系统以及奇性区域、活动边界、带约束条件等各种复杂的数学物理问题。要对这些复杂的非线性数学物理方程进行大规模和高精度的计算，在一般的计算机上用传统的计算方法往往是无能为力的。

对高速并行计算的需求是广泛的，但归纳起来主要有三种类型的应用需求：①计算密集(Compute-Intensive)型应用,如大型科学工程计算与数值模拟；②数据密集(Data-Intensive)型应用，如数字图书馆、数据仓库、数据开采和计算可视化等；③网络密集(Network-Intensive)型应用,如协同工作、遥控和远程医疗诊断等。

从另一方面讲，正是这些重大的应用需求推动了当代计算技术的迅速发展。这也可从评测计算机性能的单位量词证实之：20世纪70年代到80年代，常用Mflops(每秒百万次浮点运算)作为评测计算机性能的指标;到20世纪80年代中期又增用Gflops(每秒10亿次浮点运算)作为评测计算机性能的指标；近年来由于大规模并行机的问世,G(Giga=10)亦嫌太小，又出现了采用Tflops(每秒万亿次浮点运算)作为评测计算机性能的指标；现在Pflops（每秒千万亿次浮点运算）的计算机的预研工作正在进行。这种计算机速度单位量词的演变，从$\mathbf { M } ( \mathbf { M e g a } = \mathbf { 1 0 ^ { 6 } } )$ 到 $\mathrm { G } ( \mathrm { G i g a } = 1 0 ^ { 9 } )$ 到 $\mathrm { T } ( \mathrm { T e r a } = 1 0 ^ { 1 2 } ,$ 一直到 $\mathrm { P } ( \mathrm { P e t a } = 1 0 ^ { 1 5 } .$ ，反映了计算机本身速度的惊人的改变，而其背后的驱动力就是那些挑战性的应用需求（有关计算机中常用单位量词见本章表1.9)。

美国HPCC计划科学和工程计算中的重大挑战性课题,要求能提供1Tflops 计算能力、1TB主存容量和1TB/s的 $_ \mathrm { I } / \mathrm { O }$ 带宽，这就是所谓3T性能目标。为了保持在高性能计算与计算机通信领域中的世界领先地位，1993年美国科学、工程、技术联邦协调理事会向国会提交了题为"重大挑战项目：高性能计算和通信（High Performance Computing and Communication）”的报告,简称为HPCC计划,即美国总统科学战略项目,这些重大挑战性课题的应用领域汇总于表1.1中。

表1.1美国HPCC计划公布的重大挑战性应用课题一览表  

<table><tr><td rowspan=1 colspan=1>应用领域</td><td rowspan=1 colspan=1>计算任务和预期结果</td></tr><tr><td rowspan=1 colspan=1>磁记录技术</td><td rowspan=1 colspan=1>研究静磁和交互感应以降低高密度磁盘的噪音</td></tr><tr><td rowspan=1 colspan=1>新药设计</td><td rowspan=1 colspan=1>通过抑制人的免疫故障病毒蛋白酶的作用来研制治疗癌症和艾滋病的药物</td></tr><tr><td rowspan=1 colspan=1>高速民航</td><td rowspan=1 colspan=1>用计算流体动力学来研制超音速喷气发动机</td></tr><tr><td rowspan=1 colspan=1>催化作用</td><td rowspan=1 colspan=1>仿生催化剂计算机建模,分析合成过程中的酶作用</td></tr><tr><td rowspan=1 colspan=1>燃料燃烧</td><td rowspan=1 colspan=1>通过化学动力学计算,揭示流体力学的作用,设计新型发动机</td></tr><tr><td rowspan=1 colspan=1>海洋建模</td><td rowspan=1 colspan=1>对海洋活动与大气流的热交换进行整体海洋模拟</td></tr><tr><td rowspan=1 colspan=1>臭氧耗损</td><td rowspan=1 colspan=1>研究控制臭氧消耗过程的化学和动力学机制</td></tr><tr><td rowspan=1 colspan=1>数字解析</td><td rowspan=1 colspan=1>用计算机研究实时临床成像、计算层析术、磁共振成像</td></tr><tr><td rowspan=1 colspan=1>大气污染</td><td rowspan=1 colspan=1>对大气质量模型进行模拟研究，控制污染的传播，揭示其物理与化学机理</td></tr><tr><td rowspan=1 colspan=1>蛋白质结构设计</td><td rowspan=1 colspan=1>使用计算机模拟,对蛋白质组成的三维结构进行研究</td></tr><tr><td rowspan=1 colspan=1>图像理解</td><td rowspan=1 colspan=1>实时绘制图像或动画</td></tr><tr><td rowspan=1 colspan=1>密码破译</td><td rowspan=1 colspan=1>破译由长位数组成的密码,求找该数的两个乘积因子①</td></tr></table>

HPCC 计划所提出的某些重大挑战性课题的计算需求如图1.1所示。它列出了支持科学模拟、先进计算机辅助设计和大型数据库与信息检索操作的实时处理等所需要的处理速度和存储器容量的量级。

在HPCC计划提出的当时,性能最好的计算机与3T要求相比，速度慢 ${ \bf 1 0 0 } \sim$

1000倍,而存储容量太小,I/O带宽太窄。世界上第一台峰值速度超过1 Tflo-pos 的高性能计算机是由Intel公司于1996年12月研制成功的。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0070/auto/images/25d2e14fa7057f930ec69fdecad152db6da59c000c6b228c303981c36584e00b.jpg)  
图1.1HPCC方面的重大挑战性课题的需求

美国ASCI计划全面禁止核试验条约签订后，核武器的研究代之以实验室数值模拟。因此禁试后数值模拟成了唯一可能进行的全系统(虚拟)试验。这样,1996年6月由美国能源部联合美国三大核武器实验室(LawrenceLivermore国家实验室、Los Alamos国家实验室和Sandia国家实验室)共同提出了“加速战略计算创新"（Accelerated Strategic Computing Initiative,简称为 ASCI)项目计划。提出通过数值模拟,评估核武器的性能、安全性、可靠性、更新等。要求数值模拟达到高分辨率、高逼真度、三维、全物理、全系统的规模和能力。该计划被认为是与当年曼哈顿计划等同的一个巨大的挑战,不仅需要科学界的参与，也需要计算机工业界合作,提供保障ASCI应用所需的计算机平台。为此,三大核武器实验室分别向美国三大公司(Intel、IBM和SGI/CRAY)预定了峰值速度超过1Tflops的并行计算机。美国能源部计划在2003年要使用运算速度为100Tflops、内存容量为50TB的并行机（见表1.2)。目前ASCI计划正把各项应用需求与计算平台推进到万亿级规模的体系中去（即每秒可执行万亿次浮点运算，万亿个字节的RAM,数十万亿个字节的磁盘,千万亿个字节的档案存储器,数百亿个字节的网络带宽)。

表1.2 美国ASCI计划中的并行机一览表  

<table><tr><td rowspan=1 colspan=1>时间（年）</td><td rowspan=1 colspan=1>运算速度(OPS)</td><td rowspan=1 colspan=1>存储容量(TB)</td><td rowspan=1 colspan=1>海存容量(PB)</td><td rowspan=1 colspan=1>I/O传输率(GB/s)</td><td rowspan=1 colspan=1>网络传输率(GB/s)</td></tr><tr><td rowspan=1 colspan=1>1996</td><td rowspan=1 colspan=1>1011</td><td rowspan=1 colspan=1>0.05</td><td rowspan=1 colspan=1>0.13</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>0.13</td></tr><tr><td rowspan=1 colspan=1>1997</td><td rowspan=1 colspan=1>1012</td><td rowspan=1 colspan=1>0.5</td><td rowspan=1 colspan=1>1.3</td><td rowspan=1 colspan=1>50</td><td rowspan=1 colspan=1>1.3</td></tr><tr><td rowspan=1 colspan=1>2000</td><td rowspan=1 colspan=1>1013</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>13</td><td rowspan=1 colspan=1>500</td><td rowspan=1 colspan=1>13</td></tr><tr><td rowspan=1 colspan=1>2003</td><td rowspan=1 colspan=1>1014</td><td rowspan=1 colspan=1>50</td><td rowspan=1 colspan=1>130</td><td rowspan=1 colspan=1>5000</td><td rowspan=1 colspan=1>130</td></tr></table>

# \*1.1.3万亿次高端并行机

ASCIOption Red 是由Intel 公司和 Sandia国家实验室联合研制的一台MPP(Massively Parallel Processors)系统,完成于1997年6月,是世界上第一台万亿次的高端并行机,其I/O、存储器、计算节点与通信等性能都能被扩展到一个很高的水平，标准的并行接口可使用户较容易地把各种并行应用程序移植到该系统上。该系统使用两种操作系统，既配置用户很熟悉的Unix，又具备不是非法装人的适用于可扩展应用程序的Cougar系统。该系统使用CCOTS(Com-mercial Commodity Off The Shelf)技术,以降低系统维护费用。

系统结构 如图1.2所示,Option Red 是一台分布存储的 MPP系统，它由四部分构成：计算节点、服务节点、系统节点和I/O节点。其中,计算节点用于并行应用程序的执行;服务节点用于支持登录、软件开发和其它交互操作；I/O节点用于访问磁盘、磁带、网络(Ethernet、FDDI、ATM等)和其它I/O设备；系统节点用于支持系统的RAS(Reliability、Availability、Serviceability)能力。该系统的硬件参数列于表1.3中,其中 RAID(Redundant Array of Inexpensive Disk)是廉价冗余磁盘阵列。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0070/auto/images/57dd16e7ed724552f2baea5873ffcd95aa78519224af94d4254403a46b8c61e4.jpg)  
图1.2ASCI Option Red 系统结构

表1.3Option Red 系统硬件参数一览表  

<table><tr><td rowspan=1 colspan=1>名       称</td><td rowspan=1 colspan=1>参       数</td></tr><tr><td rowspan=1 colspan=1>计算节点</td><td rowspan=1 colspan=1>4 536</td></tr><tr><td rowspan=1 colspan=1>服务节点</td><td rowspan=1 colspan=1>32</td></tr><tr><td rowspan=1 colspan=1>硬盘I/O节点</td><td rowspan=1 colspan=1>24</td></tr><tr><td rowspan=1 colspan=1>系统节点(引导与节点站)</td><td rowspan=1 colspan=1>2</td></tr><tr><td rowspan=1 colspan=1>网络节点(Ethernet,ATM)</td><td rowspan=1 colspan=1>6</td></tr><tr><td rowspan=1 colspan=1>系统基座面积</td><td rowspan=1 colspan=1>1 000in²</td></tr><tr><td rowspan=1 colspan=1>机柜数</td><td rowspan=1 colspan=1>85</td></tr><tr><td rowspan=1 colspan=1>系统RAM</td><td rowspan=1 colspan=1>594 MB</td></tr><tr><td rowspan=1 colspan=1>拓扑结构</td><td rowspan=1 colspan=1>38×32×2</td></tr><tr><td rowspan=1 colspan=1>节点到节点带宽(双向）</td><td rowspan=1 colspan=1>800 MB/s</td></tr><tr><td rowspan=1 colspan=1>交叉段(Section）带宽</td><td rowspan=1 colspan=1>51.6 GB/s</td></tr><tr><td rowspan=1 colspan=1>Pentiumpro处理器数</td><td rowspan=1 colspan=1>9 216</td></tr><tr><td rowspan=1 colspan=1>处理器到存储器带宽</td><td rowspan=1 colspan=1>533 MB/s</td></tr><tr><td rowspan=1 colspan=1>计算节点峰值速度</td><td rowspan=1 colspan=1>400 Mflops</td></tr><tr><td rowspan=1 colspan=1>系统峰值性能</td><td rowspan=1 colspan=1>1.8 Tflops</td></tr><tr><td rowspan=1 colspan=1>RAID存储器(每个子系统)</td><td rowspan=1 colspan=1>1 TB</td></tr><tr><td rowspan=1 colspan=1>RAIDI/O带宽(每个子系统）</td><td rowspan=1 colspan=1>1.0 GB/s</td></tr></table>

系统软件 ASCI Option Red 的系统软件是从 Paragon 环境演变而来的。其中,系统、服务和I/O节点运行Paragon操作系统,它是一个基于OSF 的分布式Unix系统;计算节点运行Cougar操作系统,它是从Intel公司的Puma移植来的,是一个轻量级核 LWK(Light-Weight Kernel)。LWK 由两层组成:PCT(Pro-cess Control Thread)和Q-Kernel(Quintessential Kernel)。如图1.3 所示,每个节点都有一些用户进程、一个 PCT 和一个Q-Kermel。Q-Kernel 是唯一能直接访问地址映射和通信硬件的软件，它提供基本计算、通信和地址空间保护等功能；而PCT提供进程管理、名字服务和组保护(Group Protection)等功能。在Cougar 中的基本程序设计模式是建立在消息传送的基础上的。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0070/auto/images/f56c3403212a802fcc9e9132a1b696dca2465697c777aca0680b36620a0b59e8.jpg)  
图1.3LWK(Cougar)层结构

Red系统支持FORTRAN77、FORTRAN90、C与C++,并提供查错程序和性能分析工具等。

# 1.2 并行计算机系统互连

# 1.2.1系统互连

在多处理机、多计算机或分布式系统中，不同组成部分（CPU、存储模块、I/O设备、网络接口等）都要通过互连网络彼此连接起来。图1.4示出了当今不同网络拓扑和互连技术的关系图。其中，水平轴自左至右网络距离逐渐增加，垂直轴代表单位时间网络可传输的最大信息量。参照图1.5，一个系统域网络SAN(SystemAreaNetwork)可以将短距离(3～25m）内的不同节点连接起来形成单一系统；该系统可用于一个建筑物、校园或企业(500m～2km)内的局城网络LAN(LocalAreaNetwork)相连构成一个完整系统。在每个节点内，处理器芯片管脚形成了处理器总线；局部（本地）总线，存储器总线，将处理器与存储模块相连；I/O总线，系统总线，将I/O设备、网卡等连接起来(I/O总线有时也叫作小型机系统接口 SCSI(Small Computer System Interface)总线）。一个都域网MAN(MetropolitanArea Network)可以覆盖整个城市(≥25km)；而一个广域网WAN(WideAreaNetwork)甚至可覆盖全球，但本书不讨论它们,只讨论到LAN这一级,因为在构成网络工作站机群COW(Clusterof Workstations)时会用到LAN技术。下面将着重讨论节点内处理器、存储器和I/O设备之间的互连，包括静态互连网络和动态互连网络;而对构成高端并行计算机所需的宽带 SAN/LAN 网络技术只作简要介绍。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0070/auto/images/6cee87c19e09bef1e3f284031117a08fbac0fb645b40cb53572497ca7af7fbc5.jpg)  
图1.4系统互连和网络拓扑

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0070/auto/images/02abd50d75145143e189057bdf889ca79a63406f833dcedb16d8b007d32fe5f4.jpg)  
图1.5图示局部总线、I/O总线、SAN和 LAN

# 1.2.2静态互连网络

所谓静态网络(StaticNetworks)是指处理单元间有着固定连接的一类网络,在程序执行期间,这种点到点的链接保持不变;相反,动态网络(DynamicNetworks)是用开关单元构成的,可按应用程序的要求动态地改变连接组态。典型的静态网络有一维线性阵列、二维网孔、树连接、超立方网络、立方环、洗牌交换网、蝶形网络等;典型的动态网络包括总线、交叉开关和多级互连网络等。为讨论方便,兹作如下定义：

定义1.1 射人或射出一个节点的边数称为节点度(Node Degree)。在单向网络中,人射和出射边之和称为节点度。

定义1.2网络中任何两个节点之间的最长距离,即最大路径数,称为网络直径(Network Diameter）。

定义1.3对分网络各半所必须移去的最少边数称为对剖宽度（BisectionWidth)。

定义1.4如果从任一节点观看网络都一样,则称网络为对称的(Symmetry)。

一维线性阵列(1-DLinearArray）它是并行机中最简单、最基本的互连方式,其中每个节点只与其左、右近邻相连,故也叫二近邻连接。N个节点用N－1条边串接之,内节点度为2,直径为N-1,对剖宽度为1。当首、尾节点相连时可构成循环移位器,在拓扑结构上等同于环,环可以是单向的或双向的,其节点度恒为2,直径或为LN/2」(双向环)或为N-1(单向环),对剖宽度为2。

二维网孔 $( 2 - \mathrm { D } \mathrm { M e s h } )$ 在一个 $\sqrt { N } \times \sqrt { N }$ 的二维网孔网络中，每个节点只与其上、下、左、右的近邻相连(边界节点除外),故也称四近邻连接,因而节点度为4,网络直径为 $2 ( \sqrt { N } - 1 )$ ,对剖宽度为 $\sqrt { N }$ (见图1.6(a))。如果在垂直方向上带环绕,而水平方向呈蛇状,则2-D网孔就变成 Illiac 网孔了(见图1.6(b)),此时节点度恒为4,网络直径为 $\sqrt { N } - 1$ ，而对剖宽度为 $2 \sqrt { N }$ 。如果2-D网孔的垂直和水平方向均带环绕,则它就变成了2－D环绕(2-D Torus)（见图1.6(c)),其节点度恒为4,而网络直径为 $2 \lfloor \sqrt { N } / 2 \rfloor$ ，对剖宽度为 $2 \sqrt { N }$ 。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0070/auto/images/e3e0c2655dce05a53f6ad6ef8554942c77c6ea1123bf20c546715b40006f5fd0.jpg)  
图1.6四近邻连接

(a)2-D网孔；(b)lliac 网孔； $( { \mathsf { c } } ) 2 - { \mathsf { D } }$ 环绕

树二叉树除了根节点和叶节点之外,每个内节点只与其父节点和两个子节点相连,故也称为三近邻连接。如图1.7(a)所示,显然节点度为3，对剖宽度为1,而树的直径为 $2 ( \lceil \log N \rceil - 1 )$ （ $N$ 为树的总节点数)。为了减小直径，可使用X-树,将同级的兄弟节点彼此相连。如果尽量增大节点度为 $N - 1$ ,则直径缩小为2,此时就变成了如图1.7(b)所示的星形网络了，其对剖宽度为 $\lfloor N / 2 \rfloor$

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0070/auto/images/28a6fcc6219566f9e1217f2a1557486ef110f0d66d30bfcf9530c30c595a8752.jpg)  
图1.7树形连接  
(a)二叉树；(b)星形连接；(c)二叉胖树

传统二叉树的主要问题是根易成为通信瓶颈。1985年Leiserson[119]提出的胖树(Fat Tree)可缓解此问题。如图1.7(c)所示，胖树节点间的通路自叶向根逐渐变宽，它更像真实的树，连向根部的枝叉变得愈来愈粗。

超立方一个 $_ n -$ 立方由 $N { } = 2 ^ { n }$ 个顶点组成。3-立方如图1.8(a)所示；4-立方如图 $1 . 8 ( { \mathfrak { b } } )$ 所示，由两个3一立方的对应项点连接而成。 $_ { n } -$ 立方的节点度为 $\pmb { n }$ ,网络直径也是 $\pmb { n }$ ,而对剖宽度为 $N / 2$ 。由于该网络缺乏可扩放性和不易构成多维超立方，所以它正逐渐被其它的网络所代替。但过去在超立方上开发了很多优秀的算法，而像二叉树、网孔和很多其它低维网络均能嵌入超立方中，所以超立方具有学术研究的意义。如果将3-立方的每个顶点代之以一个环就构成了如图1.8(d)所示的3-立方环,此时每个顶点的度为3,而不像超立方那样节点度为 $\pmb { n } \circ$ 一般而言,可以从一个 $k ^ { - }$ 立方构成一个具有 $n = 2 ^ { k }$ 个带环顶点(每个顶点是 $\pmb { k }$ 个连成环的节点）的 $k -$ 立方环,此时 $\pmb { k } -$ 立方环中总共有 $N = k \cdot 2 ^ { k }$ 个节点 $( k \geqslant 3 )$ ，网络直径为 $2 k - 1 + \lfloor k / 2 \rfloor$ ，而对剖宽度为 $N / ( 2 k )$

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0070/auto/images/4751382b4ed8eb6f324c3bd2e8a9dd575e9b1ea1cd80bb9c2bd97ac24d848ab2.jpg)  
图1.8超立方

(a)3-立方；（b)4-立方；(c)顶点代之以环；（d)3-立方环

静态互连网络小结表1.4汇总了静态互连网络的重要特性。大多数网络的节点度都是个小的常数,这是比较理想的；随着选路技术的革新(例如虫蚀选路),网络的直径变得不那么重要了;对剖宽度会影响网络的带宽；网络的对称性与可扩放性和选路效率有关(注意表中对数以2为底)。

表1.4静态互连网络特性一览表  

<table><tr><td rowspan=1 colspan=1>网络名称</td><td rowspan=1 colspan=1>网络规模</td><td rowspan=1 colspan=1>节点度</td><td rowspan=1 colspan=1>网络直径</td><td rowspan=1 colspan=1>对剖宽度</td><td rowspan=1 colspan=1>对称</td><td rowspan=1 colspan=1>链路数</td></tr><tr><td rowspan=1 colspan=1>线性阵列</td><td rowspan=1 colspan=1>N个节点</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>N-1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>非</td><td rowspan=1 colspan=1>N-1</td></tr><tr><td rowspan=1 colspan=1>环形</td><td rowspan=1 colspan=1>N个节点</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>LN/2J(双向)</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>是</td><td rowspan=1 colspan=1>N</td></tr><tr><td rowspan=1 colspan=1>2-D网孔</td><td rowspan=1 colspan=1>(√NX√N)个节点</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>2(√N-1)</td><td rowspan=1 colspan=1>N</td><td rowspan=1 colspan=1>非</td><td rowspan=1 colspan=1>2(N-√N)</td></tr><tr><td rowspan=1 colspan=1>Iliac 网孔</td><td rowspan=1 colspan=1>(√NX√N）个节点</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>N-1</td><td rowspan=1 colspan=1>2N</td><td rowspan=1 colspan=1>非</td><td rowspan=1 colspan=1>2N</td></tr><tr><td rowspan=1 colspan=1>2-D环绕</td><td rowspan=1 colspan=1>（√N×√N）个节点</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>2L√N/2J</td><td rowspan=1 colspan=1>2N</td><td rowspan=1 colspan=1>是</td><td rowspan=1 colspan=1>2N</td></tr><tr><td rowspan=1 colspan=1>二叉树</td><td rowspan=1 colspan=1>N个节点</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>2([logN1-1)</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>非</td><td rowspan=1 colspan=1>N-1</td></tr><tr><td rowspan=1 colspan=1>星形</td><td rowspan=1 colspan=1>N个节点</td><td rowspan=1 colspan=1>N-1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>LN/2]</td><td rowspan=1 colspan=1>非</td><td rowspan=1 colspan=1>N-1</td></tr><tr><td rowspan=1 colspan=1>超立方</td><td rowspan=1 colspan=1>N=2&quot;个节点</td><td rowspan=1 colspan=1>n</td><td rowspan=1 colspan=1>n</td><td rowspan=1 colspan=1>N2</td><td rowspan=1 colspan=1>是</td><td rowspan=1 colspan=1>nN/2</td></tr><tr><td rowspan=1 colspan=1>立方环</td><td rowspan=1 colspan=1>N=k·2个节点</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>2k-1+Lk/2」</td><td rowspan=1 colspan=1>N/(2k)</td><td rowspan=1 colspan=1>是</td><td rowspan=1 colspan=1>3N/2</td></tr></table>

# 1.2.3动态互连网络

动态互连不是固定连接,而是在连接路径的交叉点处置以电子开关、选路器或仲裁器等以提供动态连接的特性。三类著名的动态互连网络是总线、交叉开关和多级互连网络。

总线总线 $\begin{array} { r } { ( \mathtt { B u s } ) } \end{array}$ 实际上是连接处理器、存储模块和I/O外围设备等的一组导线和插座。总线系统用以主设备(如处理器)和从设备(如存储器)之间的数据传输。公用总线以分时工作为基础,在多个请求情况下，总线的仲裁是重要的。

目前已有很多总线标准,例如PCI、VME、Multibus、SBus、Microchannel 和IEEEFuturebus。绝大多数标准总线都可低价构造单一处理系统(Uni-ProcessorSystem)。在构造多处理器系统时，常使用多总线和层状总线。

图1.9所示是个典型的多层总线系统。包括板级总线、底板级总线和I/O总线。在印刷电路板上实现的总线叫局部(或本地)总线(Local Bus),习惯上CPU板级上的总线叫本地总线,存储器板级上的总线叫存储器总线,I/O板级和通信板级上的总线叫数据总线。系统总线是在底板上实现的，它为所有插人板之间的通信提供了通路。在各插人板中均设有专用逻辑接口(IF)和专用控制器,包括I/O控制器(IOC)、存储器控制器(MC)和通信控制器(CC)。I/O设备是通过I/O总线(如 SCSI)与计算机系统连接的。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0070/auto/images/70df07f7eac6436e4da041218c5302b56bf9e28999264756cc6731c88082c190.jpg)  
图1.9板级、底板级和I/O级总线系统

设计多处理器总线系统的主要问题包括总线仲裁、中断处理、协议转换、快速同步、缓存一致性协议、总线桥接和层次总线的扩展等。通常,监听协议(SnoopyProtocol)均内置在多处理器总线中;硬件路障同步也常使用在多处理器总线中。

交叉开关交叉开关(Crossbar Switcher)是一种高带宽网络。像电话交换机一样,交叉点开关能在(源;目的)对之间建立动态连接。每个交叉点开关为一个(源;目的)对提供一条专用连接通路,其开关状态可根据程序的要求动态地置为"开"或"关”。图1.10是一个 $4 \times 4$ 的交叉开关,其中每个输人口有一接收器和输入缓冲器,以处理到达的请求;每个输出口有一个发送器，以传递输出数据信号至一条通信链上;开关控制仲裁开关的"开/关"状态。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0070/auto/images/3e717c35dd99505fc57c61da57a56f84d985b1cf27c47c354a392d8c6eb8027b.jpg)  
图1.10 $4 \times 4$ 的交叉开关

在并行处理中,交叉开关的使用通常有两种方式：一种是用于处理器之间的通信,此时每一行和每一列只能接通一个交叉点开关,所以一个 $\mathbf { \Omega } _ { n } \times \mathbf { \Omega } _ { n }$ 的交叉开关网络一次最多可接通 $_ n$ 个对；另一种是用于处理器和存储模块之间的通信,此时每个存储模块一次只能由一个处理器请求访问,所以每一列中只能接通一个交叉点开关,但为了支持并行(或交叉)存储访问,每一行可同时接通多个交叉点开关。

一般而言,交叉开关的成本为 $n ^ { 2 }$ ,其中 $_ n$ 为端口数,这样就限制了它在大型系统中的应用。

多级互连网络为了构筑大型开关网络，常可将单级交叉开关级联起来形成一个多级互连网络 MIN（Multistage Interconnection Network）,它已被用在MIMD和SIMD并行机中。一种通用多级互连网络如图1.11所示,其中每一级都用了多个a×b开关单元,相邻各级之间有着固定的级联拓扑。为了在输入和输出之间建立所需的连接，可以动态设置开关状态。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0070/auto/images/736ccf229adcbe5dc4d869131c9be6ff95fe1b193e4303418941b09c8f17a0ba.jpg)  
图1.11通用多级互连网络结构

目前已经提出了很多MIN,其差别就在于开关单元及其级间连接(ISC)方式不同。最简单的开关单元是2×2的开关单元;常用的ISC模式有均匀洗牌、蝶式、纵横交叉等。图1.12(e)就是著名的Ω网络,其中2×2的开关单元可有如图1.12(a)、(b)、(c)、(d)四种连接方式,而ISC是均匀洗牌连接模式。

对于一个n输人和n输出的Ω网络,共有logn级,每级包括n/2个开关单元,所以共有logn个开关单元。其它的MIN,还有基准网络、二进制立方网络和 Benes 网络等。

动态互连网络小结表1.5汇总了动态互连网络的重要特性。显然，总线造价最低,但易冲突；交叉开关造价最高，但带宽和选路性能最好;多级互连网络是总线与交叉开关的折衷,主要优点采用模块结构，可扩展性好，但延迟随网络尺寸对数增长。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0070/auto/images/a05775374743887ef1b4725f16e5f2c6fb1c6cfc3fa9fe745e2cd59fbb039834.jpg)  
图1.12 $\pmb { \Omega }$ 网络

(a)直通；（b)交叉：(c)上播；（d)下播； $( { \bf e } ) 1 6 \times 1 6$ 的 $\pmb { \Omega }$ 网络

表1.5动态互连网络特性一览表  

<table><tr><td rowspan=1 colspan=1>网络特性</td><td rowspan=1 colspan=1>总线系统n台处理器，总线宽度为ε位</td><td rowspan=1 colspan=1>多级互连网络nXnMIN采用k×k开关,线宽为ω位</td><td rowspan=1 colspan=1>交叉开关n×n交叉开关线宽为ω位</td></tr><tr><td rowspan=1 colspan=1>最小时延</td><td rowspan=1 colspan=1>恒定(轻负载)</td><td rowspan=1 colspan=1>O(nlogkn)</td><td rowspan=1 colspan=1>恒定</td></tr><tr><td rowspan=1 colspan=1>每台处理器带宽</td><td rowspan=1 colspan=1>O(w/n)至0(ω)</td><td rowspan=1 colspan=1>O(ω)至0(nw)</td><td rowspan=1 colspan=1>O(w)至0(nw)</td></tr><tr><td rowspan=1 colspan=1>开关复杂性</td><td rowspan=1 colspan=1>0(n)</td><td rowspan=1 colspan=1>O(nlogkn)</td><td rowspan=1 colspan=1>O(n²）</td></tr><tr><td rowspan=1 colspan=1>连线复杂性</td><td rowspan=1 colspan=1>0(ω)</td><td rowspan=1 colspan=1>O(nwlogkn)</td><td rowspan=1 colspan=1>O(n²ω)</td></tr><tr><td rowspan=1 colspan=1>连接特性</td><td rowspan=1 colspan=1>一次只能一对一</td><td rowspan=1 colspan=1>是阻塞型网络</td><td rowspan=1 colspan=1>全置换</td></tr></table>

# 1.2.4宽带互连网络

本节所介绍的高速宽带互连技术,对构筑一个分布式网络计算环境是十分有用的,这些互连技术均有普遍被接受的协议标准。

FDDI光纤分布式数据接口 FDDI(Fiber Distributed Data Interface)采用双向光纤令牌环可提供100～200Mb/s数据传输。彼此相反方向的双向环可提供冗余通路以提高可靠性。它能够连接大量的设备，其距离可达100m（使用铜线）、2km(使用多模式光纤)和60km(使用单模式光纤）,这使得有可能在LAN和 MAN中应用FDDI环。FDDI集中器采用孤立故障的办法可使网络更可靠。

100 Mb/s主干FDDI网络如图1.13所示。其中专门的路由器将 FDDI环连向以太集线器,后者可连接大量的桌面计算机。FDDI环可确保加入、删除、移动主机或设备而不会使网络崩溃。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0070/auto/images/bc3e9f377e8dbf6eb6e2c2352f949ffd8e7d63c86756b0a444ba3835387298eb.jpg)  
图1.13双向FDDI环作为主干网

FDDI的缺点是不能支持多媒体信息流，这就减弱了它与ATM技术的竞争力,但使用全双工模式的 FDDI(即FFDT)可以增强 FDDI的竞争力。

快速以太网以太网已历经三代：1982年引入的10 Mb/s网属第一代以太网;1994年宣布的100 Mb/s快速网属第二代以太网；1997年IEEE802.3工作.组宣布的1Gb/s千兆位网可谓第三代以太网，其特性汇总于表1.6中。

图1.14示出了如何由开关快速以太主干网升级到千兆位主干LAN。

MyrinetMyrinet是由Myricom公司生产的千兆位包开关网，其目的是互连商用产品以构筑计算机群,常用来构造机箱内SAN机群或基于LAN的桌面系统。Myrinet定义在数据链路层，包的长度可变,在每条链路上施行流控和差错控制，使用切通选路法和定制的可编程主机接口。图1.15示出了用4个Myrinet开关构造MyrinetLAN(连接工作站、PC)桌面系统、机箱内多机机群和单板多处理器机群。

表1.6三代以太网特性一览表  

<table><tr><td rowspan=1 colspan=2>代别(类型）</td><td rowspan=1 colspan=1>以太网10 BaseT</td><td rowspan=1 colspan=1>快速以太网100 BaseT</td><td rowspan=1 colspan=1>千兆位以太网1 Gb</td></tr><tr><td rowspan=1 colspan=2>引人年代</td><td rowspan=1 colspan=1>1982</td><td rowspan=1 colspan=1>1994</td><td rowspan=1 colspan=1>1997</td></tr><tr><td rowspan=1 colspan=2>速度(带宽)</td><td rowspan=1 colspan=1>10 Mb/s</td><td rowspan=1 colspan=1>100 Mb/s</td><td rowspan=1 colspan=1>1 Gb/s</td></tr><tr><td rowspan=4 colspan=1>最大距离</td><td rowspan=1 colspan=1>非屏蔽双扭对</td><td rowspan=1 colspan=1>100 m</td><td rowspan=1 colspan=1>100 m</td><td rowspan=1 colspan=1>25～100 m</td></tr><tr><td rowspan=1 colspan=1>屏蔽双扭对/同轴电缆</td><td rowspan=1 colspan=1>500 m</td><td rowspan=1 colspan=1>100 m</td><td rowspan=1 colspan=1>25~100 m</td></tr><tr><td rowspan=1 colspan=1>多模式光纤</td><td rowspan=1 colspan=1>2 km</td><td rowspan=1 colspan=1>412m(半双工）2 km(全双工）</td><td rowspan=1 colspan=1>500 m</td></tr><tr><td rowspan=1 colspan=1>单模式光纤</td><td rowspan=1 colspan=1>25 km</td><td rowspan=1 colspan=1>20 km</td><td rowspan=1 colspan=1>2 km</td></tr><tr><td rowspan=1 colspan=2>主要应用领域</td><td rowspan=1 colspan=1>文件共享,打印机共享等</td><td rowspan=1 colspan=1>COW 计算,C/S结构,大型数据库等</td><td rowspan=1 colspan=1>大型图像文件，多媒体,因特网，内部网,数据仓库等</td></tr></table>

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0070/auto/images/b23d642c549b6e14dad252f8b5be1a113ec4048b14b5ca6c228ae04ba5cd8ca4.jpg)  
图1.14千兆位以太主干网的构造

总之,Myrinet支持机群计算具有很大的潜力。但与总线有关的主机界面仍限制大量不同的主机连向Myrinet,其短于25m的电缆(使用铜线)使Myrinet作为SAN 使用受到了限制。

HiPPI 高性能并行接口HiPPI(High Performance Parallel Interface)已广泛用来构筑异构计算机系统，它是LosAlamos国家实验室1987年提出的一个标准,其目的是试图统一不同厂商的所有大型机和超级计算机的界面。HiPPI曾被大型机和超级计算机工业界作为高速I/O通道用于短距离的系统到系统和系统到外设的连接。1993年,ANSIX3T9.3批准了HiPPI标准，它覆盖了物理和数据链路层,而高层的东西留给了用户。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0070/auto/images/7cceb97acaa0a0fe89cf896682d2b1769b4fdd02b3a7516d383c5a1a2869a7c4.jpg)  
机箱内多计算机机群  
图1.154个8端口开关构筑的Myrinet群集

HiPPI是一个单工点到点的数据传输界面，其速度可达 $8 0 0 ~ \mathrm { M b / s }$ 到1.6Gb/s。随着工艺的进展和价格的降低,HiPPI已不再只为超级计算机所用。

图1.16展示出用HiPPI交叉开关连接各种大型机、服务器和超级计算机的LAN主千网。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0070/auto/images/baa559b24ff425fb3c03cdc206537d8b53951296191b0432025e09b0390ea3fb.jpg)  
图1.16使用HiPPI通道和开关构筑的LAN主干网

ATM异步传输模式 ATM(Asynchronous Transfer Mode)是在光纤通信基础上建立起来的一种新的宽带综合业务数字网(B-ISDN)的交换技术。根据CCITT1998年发表的蓝皮书1.121建议，它将是建立一个统一通信网络的最终解决方案。ATM是一种与介质无关的信息传输协议，采用53个字节的定长短数据单元(信元,Cell)进行传输。按此,如图1.17所示，一个长的包(Packet）经ATM网络传输之前须破成一些小的信元，在接收端再将它们重装起来。这些小的信元,可以使用逐段 $( { \mathrm { H o p } } - { \mathrm { b y } } - { \mathrm { H o p } } )$ 法进行选路。ATM网可以高速传输诸如声音、图像、视频和数据等所有形式的媒体;它可以加人到现存的LAN、MAN和WAN 中。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0070/auto/images/1cab50f7bf867b044de5c00a72d651952a042559e94aaf572d306e01c3718b7e.jpg)  
图1.17ATM网中的信元传输

ATM采用4层体系结构,它与 OSI(Open Systems Interoonnection)标准对应关系示于表1.7中。其中,CS(Convergence Sublayer)是汇聚子层;SAR(Segmentationand Reassembly Sublayer）是分段与组装子层；TC（Transmission ConvergenceSublayer)是传输汇聚子层;PMD(Physical Medium Dependent Sublayer)是物理介质相关子层和 AAL(ATM Adaptation Layer)是 ATM适配层。

表1.7ATM与OSI标准对应关系一览表  

<table><tr><td rowspan=1 colspan=1>OSI层</td><td rowspan=1 colspan=1>ATM层</td><td rowspan=1 colspan=1>·ATM子层</td><td rowspan=1 colspan=1>基本功能</td></tr><tr><td rowspan=2 colspan=1>3/4</td><td rowspan=2 colspan=1>AAL</td><td rowspan=1 colspan=1>CS</td><td rowspan=1 colspan=1>提供汇聚标准界面</td></tr><tr><td rowspan=1 colspan=1>SAR</td><td rowspan=1 colspan=1>分段和装配</td></tr><tr><td rowspan=1 colspan=1>2/3</td><td rowspan=1 colspan=1>ATM</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>流控,信元头的产生/消除，虚电路/路径的管理，信元的多路复用/分配</td></tr><tr><td rowspan=2 colspan=1>21</td><td rowspan=2 colspan=1>物理层</td><td rowspan=1 colspan=1>TC</td><td rowspan=1 colspan=1>信元速率匹配，信元的产生、打包/拆包，头检查和产生/验证</td></tr><tr><td rowspan=1 colspan=1>PMD</td><td rowspan=1 colspan=1>位定时，物理网络访问</td></tr></table>

如图1.18所示,ATM网络的端点设备通过用户网络接口UNI(User-Net-workInterface)连到ATM交换机上。一个网络可以有多个ATM交换设备，这些交换机连接在一起可形成更大的网络。ATM交换设备之间的接口称为网络到网络接口NNI(Network-Network Interface)。利用ATM技术可以构成宽带LAN主干网，其中交换机连接路由器和服务器，提供了可扩放和高带宽的交换能力，而高性能的服务器可直接与ATM交换机相连。也可以用ATM作为桌面网络技术组成高速用户机群局域网，然后通过路由器可以把ATM局域网与传统的主干网相连。ATM作为B-ISDN的交换技术,还可提供基于ATM的MAN/WAN的体系结构。

图1.19所示是一个基于ATM的多计算机机群实例,它由香港大学开发，专门应用于分布式多媒体和元计算（Metacomputing）。其中,HARNET代表Hong Kong Academic Research Net; IMSC 代表 Integrated Multimedia SystemCenter;WS 代表 Workstation;PC 代表 Personal Computer。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0070/auto/images/055079752b511d8835aa9cc1613295cc433ba2c8431581211f5b475446fa53de.jpg)  
图1.18 ATM网络中的UNI和 NNI

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0070/auto/images/436ee088beac495753f0ed05f9abc278b9a2a181c38e9e08961d78c7a58ded41.jpg)  
图1.19香港大学开发的珍珠机群

# 1.3 并行计算机系统结构

# 1.3.1并行计算机结构模型

大型并行机系统一般可分为6类：单指令多数据流机SIMD(Single-Instruc-tion Multiple-Data);并行向量处理机 PVP(Paralel Vector Processor);对称多处理机SMP(Symmetric Multiprocessor);大规模并行处理机 MPP(Massively Paral-lel Processor);工作站机群 COW(Cluster of Workstation)和分布共享存储 DSM(Distributed Shared Memory)多处理机。SIMD计算机多为专用,其余的5种均属于多指令多数据流 MIMD(Multiple-Instruction Multiple-Data)计算机。5种MIMD并行机的结构模型示于图1.20。其中B(Bridge)是存储总线和I/O总线间的接口,DIR(Cache Directory)是高速缓存目录,IOB(I/O Bus)是I/O总线,

LD(Local Disk)是本地磁盘，MB（Memory Bus）是存储器总线,NIC(NetworkInterface Circuitry)是网络接口电路,P/C(Microprocessor and Cache)是微处理器和高速缓存 SM(Shared Menory)是共享存储器。目前绝大多数近代并行机均用商品硬件构成,而PVP计算机的部件很多都是定制(Custom-Made)的。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0070/auto/images/7bbbace2671399036b1214faf44b6e9d9be83e08433edae2b79cee2bcf1c81b0.jpg)  
图1.205种并行机结构模型(a)PVP；（b)SMP；(c)MPP；(d)DSM；(e)COW

PVP典型的并行向量处理机的结构示于图1.20（a)。Cray C-90、CrayT-90、NEC SX-4和我国的银河1号等都是PVP。这样的系统中包含了少量的高性能专门设计定制的向量处理器VP,每个至少具有1Gflops的处理能力。系统中使用了专门设计的高带宽的交叉开关网络将VP连向共享存储模块，存储器可以兆字节每秒的速度向处理器提供数据。这样的机器通常不使用高速缓存，而是使用大量的向量寄存器和指令缓冲器。

SMP对称多处理机的结构示于图1.20(b)。IBMR50、SGI Power Chal-lenge、DECAlpha服务器 8400 和我国的曙光1号等都是这种类型的机器。SMP系统使用商品微处理器(具有片上或外置高速缓存),它们经由高速总线(或交叉开关)连向共享存储器。这种机器主要应用于商务，例如数据库、在线事务处理系统和数据仓库等。重要的是系统是对称的，每个处理器可等同的访问共享存储器、I/O设备和操作系统服务。正是对称，才能开拓较高的并行度;也正是共享存储，限制系统中的处理器不能太多(一般少于64个),同时总线和交叉开关互连一旦作成也难于扩展。

MPP大规模并行处理机的结构示于图 $1 . 2 0 ( \mathrm { c } )$ 。Intel Paragon、IBM SP2、IntelTFLOPS和我国的曙光-1000等都是这种类型的机器。MPP一般是指超大型(VeryLarge-Scale)计算机系统,它具有如下特性： $\textcircled{1}$ 处理节点采用商品微处理器； $\textcircled{2}$ 系统中有物理上的分布式存储器； $\textcircled{3}$ 采用高通信带宽和低延迟的互连网络(专门设计和定制的）； $\textcircled{4}$ 能扩放至成百上千个处理器; $\textcircled{5}$ 它是一种异步的MIMD机器,程序系由多个进程组成,每个都有其私有地址空间,进程间采用传递消息相互作用。MPP的主要应用是科学计算、工程模拟和信号处理等以计算为主的领域。

DSM分布式共享存储多处理机的结构示于图1.20(d)。Stanford DASH、Cray T3D和 SGI/Cray Origin2000 等属于此类结构。高速缓存目录DIR用以支持分布高速缓存的一致性。DSM和 SMP的主要差别是,DSM在物理上有分布在各节点中的局存从而形成了一个共享的存储器。对用户而言，系统硬件和软件提供了一个单地址的编程空间。DSM相对于MPP的优越性是编程较容易。

COW工作站机群的结构示于图1.20(e)。Berkeley NOW、Alpha Farm、DigitalTrucluster等都是COW结构。在有些情况下,机群往往是低成本的变形的MPP。COW的重要界线和特征是： $\textcircled{1} \mathrm { C O W }$ 的每个节点都是一个完整的工作站(不包括监视器、键盘、鼠标等),这样的节点有时叫作"无头工作站”,一个节点也可以是一台PC 或 SMP; $\textcircled{2}$ 各节点通过一种低成本的商品网络(如以太网、FDDI和ATM开关等)互连(有的商用机群也使用定做的网络）； $\textcircled{3}$ 各节点内总是有本地磁盘,而MPP节点内却没有； $\textcircled{4}$ 节点内的网络接口是松散耦合到I/O总线上的,而MPP内的网络接口是连到处理节点的存储总线上的,因而可谓是紧耦合式的； $\textcircled{5}$ 一个完整的操作系统驻留在每个节点中，而MPP中通常只是个微核,COW的操作系统是工作站UNIX,加上一个附加的软件层以支持单一系统映像、并行度、通信和负载平衡等。

现今,MPP和COW 之间的界线越来越模糊。例如,IBM SP2它虽视为MPP,但它却有一个机群结构。机群相对于MPP有性能/价格比高的优势，所以在发展可扩放并行计算机方面呼声很高。

公用结构 SMP、MPP、DSM和 COW 等并行结构渐趋一致,DSM是 SMP和MPP的自然结合,MPP和COW的界线逐渐不清,它们最终的结构趋向一致,形成当代并行机的公用结构(图1.21)。在这样的系统结构中,大量的节点可通过高速网络互连起来。节点通常遵循着一个Shell结构（ShellArchitec-ture),其中一个专门设计定制的电路(叫作 Shell)将商品微处理器和其余的节点,包括板级高速缓存、局存、NIC和磁盘连接起来。在一个节点内可有不止一个处理器。这种 Shell结构的优点是，当处理器芯片更新换代时只需改变 Shell。图1.21中示出了三种不同的共享结构,其中将无共享结构图(a)中节点内的磁盘(D)移出来就形成了共享磁盘的结构图(b),再把主存(M)移出来就变成了共享存储结构图(c)。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0070/auto/images/cb5816d9367a7889ff95e4133f9b6b2581ea8b9807b949ce0ff744712c07e220.jpg)  
图1.21可扩放并行机公用结构(a)无共享；(b)共享磁盘；(c)共享存储

小结表Ⅰ.8汇总了上述5种结构的特性比较，其中有关访存模型解释见第1.3.2节。

表1.85种结构特性一览表  

<table><tr><td rowspan=1 colspan=1>属性</td><td rowspan=1 colspan=1>PVP</td><td rowspan=1 colspan=1>SMP</td><td rowspan=1 colspan=1>MPP</td><td rowspan=1 colspan=1>DSM</td><td rowspan=1 colspan=1>Cow</td></tr><tr><td rowspan=1 colspan=1>结构类型</td><td rowspan=1 colspan=1>MIMD)</td><td rowspan=1 colspan=1>MIMD</td><td rowspan=1 colspan=1>MIMI)</td><td rowspan=1 colspan=1>MIMD</td><td rowspan=1 colspan=1>MIMD</td></tr><tr><td rowspan=1 colspan=1>处理器类型</td><td rowspan=1 colspan=1>专用定制</td><td rowspan=1 colspan=1>商用</td><td rowspan=1 colspan=1>商用</td><td rowspan=1 colspan=1>商用</td><td rowspan=1 colspan=1>商用</td></tr><tr><td rowspan=1 colspan=1>互连网络</td><td rowspan=1 colspan=1>定制交叉开关总线、交叉开关</td><td rowspan=1 colspan=1>定制交叉开关总线、交叉开关</td><td rowspan=1 colspan=1>定制网络</td><td rowspan=1 colspan=1>定制网络</td><td rowspan=1 colspan=1>商用网络（以太ATM）</td></tr></table>

续表

<table><tr><td rowspan=1 colspan=1>属性</td><td rowspan=1 colspan=1>PVP</td><td rowspan=1 colspan=1>SMP</td><td rowspan=1 colspan=1>MPP</td><td rowspan=1 colspan=1>DSM</td><td rowspan=1 colspan=1>cow</td></tr><tr><td rowspan=1 colspan=1>通信机制</td><td rowspan=1 colspan=1>共享变量</td><td rowspan=1 colspan=1>共享变量</td><td rowspan=1 colspan=1>消息传递</td><td rowspan=1 colspan=1>共享变量</td><td rowspan=1 colspan=1>消息传递</td></tr><tr><td rowspan=1 colspan=1>地址空间</td><td rowspan=1 colspan=1>单地址空间</td><td rowspan=1 colspan=1>单地址空间</td><td rowspan=1 colspan=1>多地址空间</td><td rowspan=1 colspan=1>单地址空间</td><td rowspan=1 colspan=1>多地址空间</td></tr><tr><td rowspan=1 colspan=1>系统存储器</td><td rowspan=1 colspan=1>集中共享</td><td rowspan=1 colspan=1>集中共享</td><td rowspan=1 colspan=1>分布非共享</td><td rowspan=1 colspan=1>分布共享</td><td rowspan=1 colspan=1>分布非共享</td></tr><tr><td rowspan=1 colspan=1>访存模型</td><td rowspan=1 colspan=1>UMA</td><td rowspan=1 colspan=1>UMA</td><td rowspan=1 colspan=1>NORMA</td><td rowspan=1 colspan=1>NUMA</td><td rowspan=1 colspan=1>NORMA</td></tr><tr><td rowspan=1 colspan=1>代表机器</td><td rowspan=1 colspan=1>Cray C-90,Cray T-90,银河1号</td><td rowspan=1 colspan=1>IBM R50,SGI PowerChallenge,曙光1号</td><td rowspan=1 colspan=1>IntelParagon,IBMSP2曙光-1000/2000</td><td rowspan=1 colspan=1>StanfordDASH,Cray T 3D</td><td rowspan=1 colspan=1>Berkeley NOW,Alpha Farm</td></tr></table>

# 1.3.2并行计算机访存模型

下面从系统访问存储器的模式来讨论多处理机和多计算机系统的访存模型,它和上节所讨论的结构模型,是实际并行计算机系统的两个方面。

UMA UMA(Uniform Memory Access)模型是均匀存储访问模型的简称。图1.22示出了UMA多处理机模型，其特点是： $\textcircled{1}$ 物理存储器被所有处理器均匀共享; $\textcircled{2}$ 所有处理器访问任何存储字取相同的时间(此即均匀存储访问名称的由来); $\textcircled{3}$ 每台处理器可带私有高速缓存; $\textcircled{4}$ 外围设备也可以一定形式共享。这种系统由于高度共享资源而称为紧耦合系统(Tightly Coupled System)。当所有的处理器都能等同的访问所有I/O设备、能同样地运行执行程序（如操作系统内核和I/O服务程序等）时称为对称多处理机 SMP(Symmetric Multiprocessor);如果只有一台或一组处理器(称为主处理器),它能执行操作系统并能操纵I/O,而其余的处理器无I/O能力(称为从处理器),只在主处理器的监控之下执行用户代码,这时称为非对称多处理机。一般而言，UMA结构适于通用或分时应用。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0070/auto/images/d598be91ef683cd2d77450db22c76625ad88081e821bcfa6112987dd1de66915.jpg)  
图1.22UMA多处理机模型

NUMA NUMA(Nonuniform Memory Access)模型是非均匀存储访问模型的简称。图1.23示出了NUMA多处理机模型，其中(a)为共享本地存储器的NUMA;(b)为层次式机群NUMA,NUMA的特点是： $\textcircled{1}$ 被共享的存储器在物理上是分布在所有的处理器中的,其所有本地存储器的集合就组成了全局地址空间； $\textcircled{2}$ 处理器访问存储器的时间是不一样的：访问本地存储器LM或群内共享存储器CSM较快,而访问外地的存储器或全局共享存储器GSM较慢(此即非均匀存储访问名称的由来); $\textcircled{3}$ 每台处理器照例可带私有高速缓存,且外设也可以某种形式共享。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0070/auto/images/b86cd64be92790204f2c1adb344f0df93d41d01b9f5dc1ee3aa7af5fbfb697d1.jpg)  
图1.23NUMA多处理机模型(a)共享本地存储器模型； (b)层次式机群模型

COMA COMA(Cache-Only Memory Access）模型是全高速缓存存储访问的简称。图1.24示出了COMA多处理机模型，它是NUMA的一种特例。其特点是：

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0070/auto/images/5ac9cf794075f52123484417e08679576c16e59a7862a3ddc54f2766a61b748c.jpg)  
图1.24COMA多处理机模型

$\textcircled{1}$ 各处理器节点中没有存储层次结构,全部高速缓存组成了全局地址空间; $\textcircled{2}$ 利用分布的高速缓存目录D进行远程高速缓存的访问； $\textcircled { 3 } \mathrm { C O M A }$ 中的高速缓存容量一般都大于2级高速缓存容量； $\textcircled{4}$ 使用COMA时，数据开始时可任意分配，因为在运行时它最终会被迁移到要用到它的地方。这种结构的机器实例有瑞典计算机科学研究所的 DDM和 Kendall Square Research 公司的KSR-1等。

CC-NUMA CC-NUMA(Coherent-Cache Nonuniform Memory Access)模型是高速缓存一致性非均匀存储访问模型的简称。图1.25示出了CC-NUMA多处理机模型,它实际上是将一些SMP机器作为一个单节点而彼此连接起来所形成的一个较大的系统。其特点是： $\textcircled{1}$ 绝大多数商用CC-NUMA多处理机系统都使用基于目录的高速缓存一致性协议; $\textcircled{2}$ 它在保留 SMP结构易于编程的优点的同时,也改善了常规SMP的可扩放性问题； $\textcircled { 3 } \mathbf { C C } \mathbf { \cdot N U M A }$ 实际上是一个分布共享存储的DSM多处理机系统； $\textcircled{4}$ 它最显著的优点是程序员无需明确地在节点上分配数据,系统的硬件和软件开始时自动在各节点分配数据,在运行期间，高速缓存一致性硬件会自动地将数据移至要用到它的地方。总之，CC-NUMA所发明的一些技术在开拓数据局部性和增强系统的可扩放性方面很有效。不少商业应用,大多数数据访问都可限制在本地节点内，网络上的主要通信不是传输数据,而是为高速缓存的无效性(Invalidation)所用。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0070/auto/images/ab2a649141872b3985172919da79d981bb2e7b63516ebabdcfd461e74be94b25.jpg)  
图1.25 CC-NUMA结构模型(RC:远程高速缓存）

NORMA NORMA( $\Nu _ { 0 }$ Remote Memory Access)模型是非远程存储访问模型的简称。在一个分布存储的多计算机系统中,如果所有的存储器都是私有的、仅能由其处理器所访问时就称为NORMA。图1.26示出了基于消息传递的多计算机一般模型,系统由多个计算节点通过消息传递互连网络连接而成,每个节点都是一台由处理器、本地存储器和/或I/O外设组成的自治计算机。NORMA的特点是： $\textcircled{1}$ 所有存储器均是私有的； $\textcircled{2}$ 绝大多数NUMA都不支持远程存储器的访问; $\textcircled{3}$ 在DSM中,NORMA 就消失了。

小结可以将上节所讲的并行机结构模型和本节所讲的并行机访存模型的相互关系汇总在图1.27中。注意，物理上分布的存储器从编程的观点看可以是共享的或非共享的;共享存储结构(多处理机)可同时支持共享存储和消息传递编程模型；共享存储的编程模型可同时执行于共享存储结构和分布式存储结构(多计算机)上。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0070/auto/images/04f330bd85eb477f02928b0d94b0c411f6023854414a481c22de133e2e1024a6.jpg)  
图1.26消息传递多计算机一般模型

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0070/auto/images/fd4f44165ea844c762272866f3317e4b70740851cfbf77cd3e35cdc1a126562a.jpg)  
图1.27构筑并行机系统的不同存储结构

# $\yen 1.3.3$ 并行计算机存储组织

下面从系统的存储器组织方式来讨论近代计算机中层次存储技术及其一致性管理。

层次存储技术在近代计算机中，存储设备都照例按图1.28所示的那样将按层次组织的寄存器和高速缓存装在处理器芯片或处理器板上的。寄存器的分配由编译器完成;高速缓存对程序员是透明的(它可按速度和应用要求有一级或多级);主存储器是计算机系统的基本存储器,它由存储管理部件和操作系统共同管理;磁盘存储器被看作是最高层的联机存储器,它保存系统程序(OS和编译器）、某些用户程序及其数据集;磁带机是脱机存储器，用作后援存储器,它保存当前或过去的用户程序副本、处理结果和文件等。磁盘驱动器和磁带机是由OS采取有限的用户干预方式进行管理的。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0070/auto/images/c2bd0a919872406ea74cdd09e372bea4189ea41808fa41fc9a6070d5fea4194e.jpg)  
图1.28存储器的层次结构

存储器相邻层之间的数据传输，是按图1.29所示的那样以不同的单位进行的:CPU 和高速缓存之间数据按字(4个字节)传输(高速缓存 $( \mathbf { M } _ { 1 }$ )通常分成一些高速缓存块,有的作者称之为高速缓存行(Cache Line),每块典型值是8个字);高速缓存和主存储器 $( \mathbf { M } _ { 2 } )$ )之间数据按块(32个字节)传输；主存储器和磁盘$\begin{array} { r } { ( \mathbf { M } _ { 3 } ) . } \end{array}$ )之间数据按页传输(每页可包含128个块);磁盘和磁带机 $( M _ { 4 } )$ 之间数据按段传输(段的大小由用户按需要而定）。

高速缓存一致性所谓一致性（Coherence）是指同一数据项应与后继存储

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0070/auto/images/1a88c2126d0247664ed70cfe69d2568e0d5a05686f8e7a17542633b5f26e9c4c.jpg)  
图1.29存储器相邻层之间的数据传输

1.从32字节高速缓存块（如块a） 按字（4个字节）存取。

2.从32块或1KB存储页面按块（32字节）存取，如从页面B按块存取。

3.从很多页面组成的文件按页（1KB）存取，如从段F中的页面A和页面B存取。

4.用不同页面数目的段传送。

器层次上的副本相一致。如果在高速缓存中的一个字被修改过，那么在其所有更高层上的该字的副本也必须立即或随后加以修改。层次结构照例必须这样维护。一致性维护一般有两种策略： $\textcircled{1}$ 写通过WT(Write-Through),即如果在 $\mathbf { M } _ { i }$ ${ \bf \Psi } ( i = 1 , 2 \cdots )$ 中修改了一个字，则在 $\mathbb { M } _ { i + 1 }$ 中需要立即修改； $\textcircled{2}$ 写回WB(Write-Back),即在 $\mathbf { M } _ { i + 1 }$ 中的修改延迟到 $\mathbf { M } _ { i }$ 中正在修改的字被替换或从 $\mathbf { M } _ { i }$ 中消除后才进行。在多处理机系统中，由于多台处理机异步地相互操作;因此多个高速缓存中的同一高速缓存行的副本可能不同。造成高速缓存不一致性的原因来源于： $\textcircled{1}$ 由共享可写数据所造成的不一致； $\textcircled{2}$ 由进程迁移所造成的不一致； $\textcircled{3}$ 由绕过高速缓存的I/O操作所造成的不一致。假定有一个由2台处理器组成的多处理机系统，每台处理器各有一个高速缓存，且它们共享主存。设X是两台处理器已访问过的共享数据，在修改之前，X的三个副本是一致的。如图1.30所示，如果 $\mathbf { P } _ { 1 }$ 使用WT策略将其高速缓存中的副本更改为 $\mathbf { X } ^ { \prime }$ ,则存储器中的副本也立即更改为 $\mathbf { X } ^ { \prime }$ ,此时两个高速缓存中的副本就不一致了；同样,如果使用WB策略时也会造成两个高速缓存的副本不一致。至于由进程迁移所造成的不一致性和由绕过高速缓存的I/O操作所造成的不一致性，读者可参阅本章习题1.8和1.9学习之。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0070/auto/images/7f4747bef8d39dc0634d381a4301be882ce5424633f4691d462b1c5f67897351.jpg)  
图1.30共享可写数据所造成的不一致性

监听总线协议在基于总线连接的多处理机系统中，总线是保证高速缓存--致性最方便的装置，因为它能使所有的处理器观察到存储器正在进行的业务活动。如果总线业务破坏了本地高速缓存中数据的一致性状态，那么高速缓存的控制器就应采取相应的动作使本地的副本无效。采用此机制保证高速缓存一致性的协议称为监听协议(Snoopy Prolocol)。

如果接在公共总线上的处理机均有自己的私有高速缓存，那么可使用写无效(Write-Invalidale)和写更新(Write-Update)两种策略来确保高速缓存的-致性，前者是在本地高速缓存的数据块更新时使所有远程的副本均无效;后者是把更新的数据块广播给含该数据块的所有高速缓存。

图1.31表示了采用WT策略的写无效和写更新的一致性协议是如何维护共享存储模块中X与3个本地高速缓存中的副本的一致性的。采用写无效协议时，如图1.31(b)所示，当处理器P将其高速缓存中的X修改为X时，通过总线使所有其它的高速缓存中的内容均无效(用I表示)；采用写更新协议时，如图1.31(c)所示，当处理器 $\mathrm { I ^ { 2 } } _ { \mathrm { : } }$ 将其高速缓存中的X修改为X'时，通过总线X广播给所有其它的高速缓存，因为是采用WT策略，还需要更新主存中的副本。至于采用WB策略的·致性维护过程，读者可参阅本章习题1.10理解之。

基于目录的协议上面介绍的监听协议为总线连接的多处理机系统所使用，对于多级I连网络连接的多处理机系统则使用基于目录的协议(DirectoryBascd Prolocol)，它就是使用一个日录来记录共享数据的所有高速缓存行的位置和状态

图1.32示出了基于目录的高速缓存一致性方案的基本原理，其存储器/高速缓存更新工作如下：高速缓存 $\Gamma _ { 2 }$ 的读缺失(Read-Miss)产生·个请求送给 $\mathrm { I } ) _ { 1 }$ （图中用细线表示）， $l ) _ { l }$ 指示在 ${ \bf \Xi } ( { \bf \Lambda } )$ 中有可用(Clean)副本，存储控制器再将请求传全 $C _ { 1 }$ ，它返回一个可用副本给 $\mathrm { M } _ { \mathrm { l } }$ 和 ${ \bf \Xi } ( { \bf \Lambda } )$ ；在 $\bf ( \dot { \omega } _ { 1 } \cdot \dot { \bf \delta } _ { j }$ 命中时（图中用粗线表示），它就发送·个命令给存储控制器，存储控制器再发·个无效命令给在D中有标记的所有高速缓存（在此为 $( \ Y _ { \frac { 3 } { 7 } } )$ 、

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0070/auto/images/fcbcacf43bb9a8880553d069ab294d556fc9e4b37b5314dd1a257e4836fe5e6d.jpg)  
图1.31采用WT策略的一致性维护(a)更新前； $( \mathfrak { b } ) \mathfrak { P } _ { 1 } \ ^ { \prime } \mathfrak { s }$ 无效操作后； $( \cos ) _ { \mathrm { } } \mathrm { p } _ { 1 } \mathrm { ~ } ^ { \prime } \mathrm { \pmb { \mathscr { s } } ~ }$ 更新操作后

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0070/auto/images/048e78cb68cab2819ebcc6b59c2f0480c33dc62282d18f4bded32577191ef152.jpg)  
图1.32基于目录的高速缓存一致性原理

总之，不用广播的高速缓存一致性协议,必须将所有高速缓存中每个共享数据块副本的地址存储起来，这张高速缓存地址表,不管它是集中的或分散的，都称之为高速缓存目录。每个数据块(即高速缓存行)的目录项包括大量的指针，用来指向该高速缓存行的所有远程副本的地址。每个目录项还包含一个重写位(Dirty Bit),用来说明是否有一个高速缓存允许把有关的数据块写人。

目前已有各种不同的目录协议,包括全映射(Full-Map)目录、有限(Limited)目录和链式(Chained)目录等。有兴趣的读者可参阅[100]。

# 1.4 小结和导读

小结本章从并行计算的角度出发，着重讨论当代科学和工程计算问题所要求的高性能并行计算系统，包括并行计算机系统的互连技术、并行计算机的系统结构模型、存储访问模型和存储结构组织等。值得注意的是,所介绍的并行计算机系统,与计算机体系结构或并行处理技术等课程所讲的出发点不一样,在此着重介绍一类并行计算机的体系结构，而不是某一具体并行机的详细介绍；着重介绍当代能满足高速并行计算要求的主流并行计算机类(SMP、MPP、COW等),而对历史上曾占主导地位的SIMD和PVP则不作重点介绍;同时所选讲的内容和叙述的深浅程度都是为了并行算法的设计和并行编程的需要,而对有些相关知识的介绍,也只能点到为止,不能深入全面展开讨论，尤望读者能以此为线索,进一步追踪和深入地学习。

最后,在电子学和计算机科学中,习惯上,常用的量词单位均以千进制表示，为了读者查阅方便,兹将它们列于表1.9中。

表1.9计算机科学中常用千进制单位量词一览表  

<table><tr><td rowspan=1 colspan=1>词头</td><td rowspan=1 colspan=1>缩写</td><td rowspan=1 colspan=1>英文含意</td><td rowspan=1 colspan=1>数值</td><td rowspan=1 colspan=1>中文名称</td></tr><tr><td rowspan=1 colspan=1>milli</td><td rowspan=1 colspan=1>m</td><td rowspan=1 colspan=1> one thousandth</td><td rowspan=1 colspan=1>10-3</td><td rowspan=1 colspan=1>毫</td></tr><tr><td rowspan=1 colspan=1>micro</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>one millionth</td><td rowspan=1 colspan=1>10-6</td><td rowspan=1 colspan=1>微</td></tr><tr><td rowspan=1 colspan=1>nano</td><td rowspan=1 colspan=1>n</td><td rowspan=1 colspan=1>one billionth</td><td rowspan=1 colspan=1>10-9</td><td rowspan=1 colspan=1>纳[诺]</td></tr><tr><td rowspan=1 colspan=1>pico</td><td rowspan=1 colspan=1>p</td><td rowspan=1 colspan=1>one trillionth</td><td rowspan=1 colspan=1>10-12</td><td rowspan=1 colspan=1>皮[可]</td></tr><tr><td rowspan=1 colspan=1>femto</td><td rowspan=1 colspan=1>f</td><td rowspan=1 colspan=1> one quadrillionth</td><td rowspan=1 colspan=1>10-15</td><td rowspan=1 colspan=1>飞[母托]</td></tr><tr><td rowspan=1 colspan=1>atta</td><td rowspan=1 colspan=1>a</td><td rowspan=1 colspan=1>one quintillionth</td><td rowspan=1 colspan=1>10-18</td><td rowspan=1 colspan=1>阿[托]</td></tr><tr><td rowspan=1 colspan=1>kilo</td><td rowspan=1 colspan=1>k</td><td rowspan=1 colspan=1>thousand</td><td rowspan=1 colspan=1>103</td><td rowspan=1 colspan=1>千</td></tr><tr><td rowspan=1 colspan=1>mega</td><td rowspan=1 colspan=1>M</td><td rowspan=1 colspan=1>million</td><td rowspan=1 colspan=1>106</td><td rowspan=1 colspan=1>兆</td></tr><tr><td rowspan=1 colspan=1>giga</td><td rowspan=1 colspan=1>G</td><td rowspan=1 colspan=1>billion</td><td rowspan=1 colspan=1>109</td><td rowspan=1 colspan=1>吉[咖]</td></tr><tr><td rowspan=1 colspan=1>tera</td><td rowspan=1 colspan=1>T</td><td rowspan=1 colspan=1>trillion</td><td rowspan=1 colspan=1>1012</td><td rowspan=1 colspan=1>太[拉]</td></tr><tr><td rowspan=1 colspan=1>peta</td><td rowspan=1 colspan=1>P</td><td rowspan=1 colspan=1>quadrillion</td><td rowspan=1 colspan=1>1015</td><td rowspan=1 colspan=1>拍[它]</td></tr><tr><td rowspan=1 colspan=1>exa</td><td rowspan=1 colspan=1>E</td><td rowspan=1 colspan=1>quintillion</td><td rowspan=1 colspan=1>1018</td><td rowspan=1 colspan=1>艾[可萨]</td></tr></table>

导读有关美国“高性能计算与通信"计划,读者可参阅[98],有关美国“加速战略计算创新"计划,读者可参阅[17],有关万亿次 ASCIOptionRed系统介绍,请参阅[123]。关于互连网络,[199]是一本基本的教材，近期有关互连网络方面的书可参见[62],有关构筑可扩放并行机的千兆位网可参阅[102],[164，165]综述了LAN、MAN 和ISDN 的新进展,有关FDDI环可参见FDDI手册[167],Gb以太网的描述可参见Gb以太网联盟公布的材料[75],有关Myrinet的介绍，读者可参阅[36],HiPPI网络情况读者可查阅[173],读者从ATM论坛那里可了解ATM[18]。有关当前并行计算机的介绍,读者可参阅[174]一书,[101]中对并行计算机的结构模型作了讨论，有关NUMA、CC-NUMA、CCMA的分析比较读者可参见[168]。关于高速缓存一致性方法的综合讨论读者可见[3],有关基于目录的高速缓存一致性协议读者可参阅[43]。最后,[103]是一本论述有关可扩放并行计算的新著，取材宽广、新颖，特推荐阅读。

# 习 题

1.1 对于一棵 $\kappa$ 级二叉树（根为0级，叶为 $\kappa { \bf - 1 }$ 级),共有 $N = 2 ^ { \kappa } - 1$ 个节,当推广至 $\pmb { m }$ -元树（即每个非叶节点有m个子节点)时，试写出总节点数N的表达式。

1.2二元胖树如图1.33所示,此时所有非根节点均有2个父节点。如果将图中的每个椭圆均视为单个节点，并且成对节点间的多条边视为一条边，则它实际上就是一棵二叉树。试问：如果不管椭圈，只把小方块视为节点，则它从叶到根形成一个什么样的多级互连网络？

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0070/auto/images/c461ea35fbf3f4755678af71c51e79f5afecc03a3cf6346765c94102b998f7ba.jpg)  
图1.33二元胖树

1.3四元胖树如图1.34所示，试间：每个内节点有几个子节点和几个父节点？你知道哪个机器使用了此种形式的胖树？

1.4试构造一个N=64的立方环网络，并将其直径和节点度与N=64的超立方比较之，你的结论是什么？

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0070/auto/images/6acafb233605041b9bbf28e753c0c653e1008b9c7c5d0cbbe03120eb8322fbce.jpg)  
图1.34四元胖树

1.5一个 $\therefore \lor = \underline { { ? } } ^ { k }$ 个节点的de Bruijn 网络如图1.35所示，令 $u _ { k - 1 } u _ { k - 2 } \cdots u _ { 1 } u _ { 1 } )$ 是一个节点的二进制表示，则该节点可达如下两个节点：

$$
\begin{array} { r } { a _ { k \textrm { - } 2 } a _ { k \textrm { - } 3 } \cdots a _ { 1 } a _ { 0 } ( ) } \\ { a _ { k \textrm { - } 2 } a _ { k \textrm { - } 3 } \cdots a _ { 1 } a _ { 0 } \} } \end{array}
$$

试问：该网络的直径和对剖宽度为多少?

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0070/auto/images/5fa17c30b2ed7142a76adb0263500b2274e23ad1fe6da80ebb5a1d922882957b.jpg)  
图1.35 $\mathbf { \nabla } \cdot \mathbf { V } = 8$ 的dc Bruijn 网络

1.6-个 $. \lor = 2 ^ { n }$ 个节点的洗牌交换网络如图1.36所示．试问：此网节点度 $= ?$ 网络直径$= ?$ 和网络对剂度 $= ?$

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0070/auto/images/7af23c68894190cf52e6c4967d3092ce524024e8e3e851dd5142564d5b3318c7.jpg)  
图1.36 $\mathbf { \nabla } \cdot \mathbf { V } = \mathbf { 8 }$ 的洗牌交换网络

1.7·个 $. \mathsf { V } = (  { k } + \mathsf { i } ) \underline { { \mathsf { \Omega } } } ^ { \prime }$ 个节点的蝶形网络如图1.37所示

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0070/auto/images/937ff6072098c4ac5dd1323aa97881438a2833c86a77b8550538814b2399f574.jpg)  
图1.37 $k = 3$ 的蝶形网络

试问：此网节点度 $= ?$ 网络直径 $=$ ？和网络对剖宽度 $= ?$

1.8参照图1.38,试解释为什么当采用WT策略进程从 ${ \sf P } _ { 2 }$ 迁移到 $\mathrm { P } _ { 1 }$ 时，或采用WB策略包含共享变量 $\mathbf { X }$ 的进程从 ${ \bf P } _ { 1 }$ 迁移到 ${ \bf P } _ { 2 }$ 时，会造成高速缓存的不一致。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0070/auto/images/3f2f041e9232612e6f31a407b4cae42a72f55ac07cb084879cbf112b4df1773a.jpg)  
图1.38进程迁移所造成的不一致性

1.9参照图1.39.试解释为什么：①当I/O处理器将--个新的数据X'写回主存而绕过采用WT策略的高速缓存时会造成高速缓存和主存间的不一致；②当直接从主存输出数据而绕过高速缓存采用WB策略时也会造成不·-致、

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0070/auto/images/0b8a62ceddcab5c1703188e438721eb80ffc040c9329d56c80c67abfc7bd7a2b.jpg)  
图1.39绕过高速缓存的I/操作所造成的不致性

1.10参照图1.40,试解释采用WB策略的写更新和写无效协议的一致性维护过程，其中，X为更新前高速缓存中的副本，X为修改后的高速缓存行，1为无效的高速缓存行，

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0070/auto/images/989235be1518179d2c1e609cad5537617640a692edbf65b53fe0e765301ec4a3.jpg)  
图1.40采用WB策略的写更新和写无效协议一致性维护$( \mathbf { a } ) ^ { \prime } ^ { \prime } \mathbf { j }$ 操作前；（b)山 ${ \bf f } _ { \parallel } ^ { 2 }$ 执行写无效后；（c）山 $\mathbf { P _ { f } }$ 执行写更新后

# 第二章 当代并行机系统：SMP、MPP 和 COW

自20世纪70年代初到现在，并行计算机的发展已有20多年的历史了。在此期间,出现了各种不同类型的并行机,包括向量机、SIMD计算机和MIMD 计算机。随着计算机的发展，曾经风行一时的向量机和SIMD计算机现已退出历史舞台，而MIMD类型的并行机却占了主导地位。当代主流的并行机是可扩放的并行机,包括共享存储的对称多处理机(SMP)和分布存储的大规模并行机(MPP)与工作站机群(COW)。本章首先讨论SMP的结构特性及其代表机器Origin2000;然后讨论MPP的结构特性及其代表机器SP2;接着讨论COW的基本原理及其代表系统NOW；最后介绍一下我国曙光系列并行机，包括曙光1号、曙光-1000 和曙光-2000,它们分别属于 SMP和MPP系统。

# 2.1 对称多处理机 SMP

对称多处理机 SMP(Symmetric Multiprocessor)结构在现今的并行服务器中几乎普遍采用。SMP 系统属于UMA（Uniform Memory Access）机,NUMA(Nonuniform Memory Access)机是 SMP 系统的自然推广,而 CC-NUMA(Coher-ent-CacheNUMA)实际上是将一些SMP作为单节点而彼此连接起来所构成的分布共享存储系统(见图1.25)。本节首先讨论多处理机系统(SMP和CC-NU-MA)的结构特性;然后简介一个当今有代表性的商用超级服务器系统Origin2000,以期对多处理机系统有个一般了解。

# 2.1.1 SMP和 CC-NUMA 结构特性

对称多处理器 SMP结构特性 参照图1.20(b),共享存储的 SMP系统结构具有如下特性： $\textcircled{1}$ 对称性：系统中任何处理器均可访问任何存储单元和I/O设备； $\textcircled{2}$ 单地址空间：单地址空间有很多好处,例如因为只有一个OS和DB 等副本驻留在共享存储器中，所以OS可按工作负载情况在多个处理器上调度进程从而易达到动态负载平衡，又如因为所有数据均驻留在同一共享存储器中,所以用户不必担心数据的分配和再分配； $\textcircled{3}$ 高速缓存及其一致性：多级高速缓存可支持数据的局部性，而其一致性可由硬件来增强； $\textcircled{4}$ 低通信延迟：处理器间的通信可用简单的读/写指令来完成(而多计算机系统中处理器间的通信要用多条指令才能完成发送/接收操作）。

目前大多数商用SMP系统都是基于总线连接的，占了并行计算机很大市场,但是 SMP也具有如下问题： $\textcircled{1}$ 欠可靠：总线、存储器或OS失效均会造成系统崩溃，这是SMP系统的最大问题； $\textcircled{2}$ 可观的延迟：尽管SMP比MPP通信延迟要小,但相对处理器速度而言仍相当可观(竞争会加剧延迟),一般为数百个处理器周期,长者可达数千个指令周期; $\textcircled{3}$ 慢速增加的带宽：有人估计，主存和磁盘容量每3年增加4倍,而SMP存储器总线带宽每3年只增加2倍,I/O总线带宽增加速率则更慢,这样存储器带宽的增长跟不上处理器速度或存储容量的步伐;$\textcircled{4}$ 不可扩放性：总线是不可扩放的,这就限制最大的处理器数一般不能超过10。为了增大系统的规模，可改用交叉开关连接,或改用CC-NUMA或机群结构。

CC-NUMA系统如图1.25所示，高速缓存一致性非均匀存储访问 CC-NUMA机,就是将一些小规模的SMP作为单节点,通过系统互连网络扩展至一个大规模多处理器系统。SMP节点中的所有局部存储器构成了共享主存,这样就可保持 SMP易编程的优点,同时由于可方便地加入更多的节点从而改善了常规 SMP系统的可扩放性。因为对于给定的应用,可利用数据局部性,在绝大部分时间内同时访问多个局部存储器，从而也缓解了竞争和带宽问题。

目前绝大多商用CC-NUMA均使用基于目录的高速缓存一致性协议。CC-NUMA机最显著的优点是程序员无需明确地在节点上分配数据,系统的硬件和软件开始时自动在各节点中分配数据,在应用程序运行期间,高速缓存一致性硬件设施会自动地将数据移至要使用它的地方。例如某一程序有P和Q两个进程,执行如下访问数组A和B的代码段：

P Q第一步：Use(A) Use(B)第二步：Use(B) Use(A)

图2.1(a)所示的初始数据分配是很适合上述代码段的第一步的;在第二步时,硬件能自动地将B移人节点1和将A移人节点2,程序员不必作这些,但在多计算机系统中却要求程序员作明确的数据分配。

商用 SMP服务器SMP 是现今最成功的并行计算机,它经常工作在网络环境中,所以其安全性、集成能力和易于管理是很重要的。表2.1综合比较了现今流行的5种商用 SMP 系统特性,这些参数均是最大或最优值(表中B为字节)。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0070/auto/images/0e43d3930947d3b63c15484ad75d7bcade60fca69f688531767829080e8e701a.jpg)  
图2.1CC-NUMA使用远程高速缓存重新分配数据（a)第一步的数据分配；(b)第二步的数据再分配

表2.15种商用SMP系统特性比较一览表  

<table><tr><td rowspan=1 colspan=1>系统特性</td><td rowspan=1 colspan=1>、DECAlphaserver84005/440</td><td rowspan=1 colspan=1>HP9000/T600</td><td rowspan=1 colspan=1>IBMRS600/R40</td><td rowspan=1 colspan=1>Sum UltraEnterprise6000</td><td rowspan=1 colspan=1>SGI PowerChallenge XL</td></tr><tr><td rowspan=1 colspan=1>处理器数目</td><td rowspan=1 colspan=1>：12福</td><td rowspan=1 colspan=1>：  心</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>厦   加：</td><td rowspan=1 colspan=1>36</td></tr><tr><td rowspan=1 colspan=1>处理器类型i</td><td rowspan=1 colspan=1>437 MHzAlpha21164E</td><td rowspan=1 colspan=1>180MHzPA8000</td><td rowspan=1 colspan=1>112MHzPowerPC604     1</td><td rowspan=1 colspan=1>167MHzUtraSPARC</td><td rowspan=1 colspan=1>195MHz： MIPSLR10000</td></tr><tr><td rowspan=1 colspan=1>处理器片外高速缓存容量</td><td rowspan=1 colspan=1>福4MB心</td><td rowspan=1 colspan=1>8MB</td><td rowspan=1 colspan=1>1 MB！</td><td rowspan=1 colspan=1>512MB</td><td rowspan=1 colspan=1>4MB</td></tr><tr><td rowspan=1 colspan=1>最大主存容量</td><td rowspan=1 colspan=1>28GB</td><td rowspan=1 colspan=1>116GB</td><td rowspan=1 colspan=1>i  .2GB</td><td rowspan=1 colspan=1>30GB</td><td rowspan=1 colspan=1>16GB</td></tr><tr><td rowspan=1 colspan=1>互连网络及带宽               ！</td><td rowspan=1 colspan=1>BUS2.1GB/</td><td rowspan=1 colspan=1>BUS960MB/s</td><td rowspan=1 colspan=1>1BUS+Xbar1.8GB/s</td><td rowspan=1 colspan=1>！BUS+Xbar2.6GB/s</td><td rowspan=1 colspan=1>BUS1:2 GB/s</td></tr><tr><td rowspan=1 colspan=1>外磁盘容量</td><td rowspan=1 colspan=1>192 GB</td><td rowspan=1 colspan=1>168GB</td><td rowspan=1 colspan=1>38 GB</td><td rowspan=1 colspan=1>63.GB</td><td rowspan=1 colspan=1>144GB：：！</td></tr><tr><td rowspan=1 colspan=1>I/O通道</td><td rowspan=1 colspan=1>12 PCI总线，每个133MB/s</td><td rowspan=1 colspan=1>N/A1</td><td rowspan=1 colspan=1>2MCA,每个160 MB/s</td><td rowspan=1 colspan=1>30 Sbus,每个200 MB/s</td><td rowspan=1 colspan=1>6 Power Channel-2HIO,每个320MB/s</td></tr><tr><td rowspan=1 colspan=1>I/O槽</td><td rowspan=1 colspan=1>144PCI精</td><td rowspan=1 colspan=1>112HPPB1</td><td rowspan=1 colspan=1>15MCA</td><td rowspan=1 colspan=1>45 Sbus</td><td rowspan=1 colspan=1>12 HIO槽</td></tr><tr><td rowspan=1 colspan=1>I/O带宽</td><td rowspan=1 colspan=1>1.2 GB/s</td><td rowspan=1 colspan=1>1GB/s！</td><td rowspan=1 colspan=1>320 MB/s</td><td rowspan=1 colspan=1>2.6GB/8</td><td rowspan=1 colspan=1>每个HIO槽320MB/s5</td></tr></table>

# $\times 2 . 1 . 2$ SGI/Cray Origin 2000超级服务器

1996年10月，SGI/Cray公司推出了Origin 2000系统，它采用了CC-NUMA结构，此结构也被称之为可扩放共享存储多处理机S2MP或S2MP(Scalable

Shared Memory Multiprocessor)。设计时吸取了DASH的经验,所设计的系统规模可达到1024个处理器和1TB主存，其中 $1 \sim 6 4$ 个处理器的系统叫SGIOri-gin 2000,而大于等于128个处理器的系统叫（ray Origin 2000。现有的Origin2000的结构配置属性综合于表2.2中。

表2.2Origin2000结构配置属性一览表  

<table><tr><td rowspan=1 colspan=1>属性</td><td rowspan=1 colspan=1>立式（Deskside)配置</td><td rowspan=1 colspan=1>装架式（Rack）配置</td></tr><tr><td rowspan=1 colspan=1>处理器数目</td><td rowspan=1 colspan=1>1~8</td><td rowspan=1 colspan=1>2~128</td></tr><tr><td rowspan=1 colspan=1>峰值速度(Gflops)</td><td rowspan=1 colspan=1>3.12</td><td rowspan=1 colspan=1>49.92</td></tr><tr><td rowspan=1 colspan=1>高速缓存容量（MB)</td><td rowspan=1 colspan=1>1~32</td><td rowspan=1 colspan=1>2~512</td></tr><tr><td rowspan=1 colspan=1>物理存储器容量(GB)</td><td rowspan=1 colspan=1>0.064~16</td><td rowspan=1 colspan=1>0.064~256</td></tr><tr><td rowspan=1 colspan=1>总计峰值存储带宽(GB/s)</td><td rowspan=1 colspan=1>3.12</td><td rowspan=1 colspan=1>49.92</td></tr><tr><td rowspan=1 colspan=1>I/端口数目</td><td rowspan=1 colspan=1>14</td><td rowspan=1 colspan=1>208</td></tr><tr><td rowspan=1 colspan=1>总计峰值I/O带宽(GB/s)</td><td rowspan=1 colspan=1>6.2</td><td rowspan=1 colspan=1>102</td></tr></table>

系统结构Origin2000系统结构如图2.2所示。它的每个节点包括1或2个 MIPSR10000处理器（时钟 $1 9 5 ~ \mathrm { M F z }$ ,峰值速度395Mllops)，-个可高达 $4 \ \mathrm { M B }$ 的高速缓存和-个DSM主存(物理上分散在各节点中，但可被所有节点访问),硬件增强了基于目录的高速缓存一致性。如图2.3所示，一个HUB(ASIC交叉开关)连接系统中的处理器、存储器、互连网络和I/O系统,HUB有4个双向端口，使用 $1 9 5 ~ \mathrm { M H z }$ 的时钟，每个口可提供单向 $7 8 0 ~ \mathrm { M B / s }$ 的峰值带宽和全双工1.56(GB/s的峰值带宽,它用于节点内和节点间通信选路,4个成对的接口电路(ififo,ofifo)负责内部和外部信息格式的转换。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0070/auto/images/ec0c5beeb0d9bf90eb65487a6de36c50aba959d8af257051c9357207b6299a33.jpg)  
图2.2Origin 2000系统结构

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0070/auto/images/67425eb9f31a0c84a8dfb1c4b9ceb06542748905390a81dc513f69236c036ee7.jpg)  
图2.3Origin 2000中交叉开关HUB芯片

①I/O子系统:Origin 2000的I/O子系统示于图2.4中,其中,XBOW是一个8端口的交叉开关(各口均使用XIO协议):2个连向节点,其余6个连向XIO设备或者ASIC小部件，包括图形小部件G(GraphicsWidget）和桥接小部件B(BridgeWidget)。通过 32位或 64位的PCI总线,不同的I/O设备（ATM、HiPPI、FDDI、SCSI等)均可连向Origin 2000。Origin 2000 可提供单- I/O空间，即任何处理器能访间任·[O设备。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0070/auto/images/fd01944a045c817e9f7c614aee8aadd5151e343603d587eec2cbd6ec15c52d10.jpg)  
图2.4Orgin 2000的I/0子系统

$\textcircled{2}$ 互连系统:Origin2000的互连系统由CrayLink电缆和图2.5所示的路出器组成。SGI SPIDER路由器提供可靠的虫蚀选路，它是6端口的交叉开关,这些端口连向节点或别的路由器。路由器允许6个端口同时全双工工作。由于外部频率$( 3 9 0 ~ \mathrm { M H z } )$ 和路由器芯片内部频率 $( 9 7 . 5 ~ \mathrm { M H z } )$ 的不同，所以需使用源同步驱动器SSD(Source Synchronous Driver)和源同步接收器 SSR(Source Synchronous Receiver)施行内/外频率 $( 9 7 . 5 ~ \mathrm { M H z } / 3 9 0 ~ \mathrm { M H z } )$ 和字长(64位/16位)的转换。链路级协议LLP(Link-Level Protocol)确保信息可靠传输（使用CRC误差检测和重发校正），施行流控、缓解竞争和拥挤等。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0070/auto/images/98c7c65bf763c0b024e46740468ae68f96d45e23f8e44d02a9090825685f7b0f.jpg)  
图2.5Origin 2000的 SPIDER 路由器芯片

$\textcircled{3}$ 胖超立方拓扑:Origin 2000 中采用了胖超立方(Fat Hypercube)拓扑。如图2.6所示，胖超立方是将传统的2元超立方加以修改而得，其优点是保持了超立方线性对剖宽度的优点且避免了节点度的增加。在此拓扑中,每个路由器R芯片有6个端口，其中的2个连向节点，其余的4个用于网络连接。按照一般的超立方，度为4的节点最多也只能构造16个顶点的超立方（即Origin 2000中的32个节点),但使用了胖超立方拓扑,可允许Origin 2000连接多达512个节点(1024个处理器)。图2.6(a)只有-个节点，它有2个处理器，还可连向XBOW交叉开关；图2.6(b)中，-个SPIDER路由器R连向2个节点;图2.6(c)中2个R连向4个节点；以此方式可达32个节点(图2.6(f)),至此，如果把R视为超立方的顶点，则它就是普通的2元超立方连接。注意，未被使用的路由器端可连向快速链路( $\operatorname { E x } -$ pressLink)以降低延迟和增大对剖带宽(如图2.6(d)中的虚线连接)。当超过32个节点时，Origin2000的胖超立方中使用了额外的路由器（称之为元路由器，Metaroutcr),8个元路由器构成·个（ray Rouler，这些元路由器只用作中间选路，不连向任何节点，·个64个节点(32个顶点，即路由器)的胖超立方拓扑如图2.6$( \mathbf { g } )$ 所示，其中4个8顶点的子立方中每个顶点都连向一个元路由器，这种胖超立方可·直扩放到1024个处理器，读者不妨想一想应如何构造？

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0070/auto/images/b2a48e88c7329597d22fb37518c742c989f421bb7148ffd78af9f6024ea6f591.jpg)  
图2.6Origin 2000的胖超立方拓扑

(a)2个处理器;(b)4个处理器； $\left( { \mathfrak { c } } \right) { \mathfrak { s } }$ 个处理器；(d)I6个处理器；(c)32个处理器；(f)64个处理器； $( \pmb { \mu } )$ 128个处理器

$\textcircled{4}$ 分布共享存储子系统：Origin 2000 系统中有一个分布式共享存储子系统，节点内的存储模块叫近存储器,别的节点中的存储模块叫远存储器。节点中的主存储器和目录存储器使用同步DRAM可组织成多达8个体(Bank),每个体提供4路交叉访问，使用4路交叉访间的存储子系统带宽高达 $78 0 ~ \mathrm { M B / s _ { o } }$

软件环境Origin 2000 运行细胞(Cellular)IRIX操作系统。其1996 年版本是--个64位的多线程、多道程序操作系统,它的设计目标要满足可兼容性、可扩放性（扩展到128个或更多处理器）可用性和高吞吐率的要求。

$\textcircled{1}$ 细胞概念：为了增强细胞IRIX的可扩放性,使用了细胞概念(Cell（oncept)和存储器管理软件的办法。前者能模块化操作系统核，后者能有效地开拓 S2MP的硬件。细胞IRIX结构把核文本和数据分散成 SMP大小的称作细胞的块,其中每个细胞包含一个核文本和数据结构的副本,并负责控制--个由--组处理器、存储器和IO设备组成的机器模块,细胞概念的关键特性是将操作系统服务分散化和局部化,多个细胞可驻留在--个Origin 2000 系统中，允许一些应用同时地、独立地

访问多个机器模块。

$\textcircled{2}$ 存储管理：细胞IRIX的存储管理软件包括存储器复制、迁移和置放机制(存储管理的基本单位是页)：复制机制复制一个只读页的副本。当一个页是只读时，硬件检测共享情况并调用存储管理子系统执行存储器复制;迁移机制移动页面靠近最经常访问它的处理器。当一页被访问时，硬件计数器记录外节点的访问次数,如其值超过某一阈值,则存储管理子系统将迁移该页面;置放机制是初始分配数据和线程以开拓局部性。细胞IRIX环境允许用户告诉系统页面彼此间应如何置放、如何映射线程到页面和如何定位线程离硬件资源的远近。

$\textcircled{3}$ 可用性支持：Origin2000的可用性支持包括硬件和软件：硬件设计使用冗余供电与冷却、热可插磁盘、廉价冗余磁盘阵列RAID(Redundant Array of Inexpen-sive Disks)等技术,因特网支持节点间多条路径、硬件链路层协议提供错误包的检测与重发等;IRIX系统软件包含进一步增强可用性支持(如文件系统快速再启动、监视通信故障时间、磁盘镜像等),提供访问保护权限和检查点再启动机制以及高有效网络、数据库与其它应用的附加支持(通过支持队列、套接字、XWindows、图形等）。

$\textcircled{4}$ 吞吐率支持：Origin2000 通过使用优化调度(它支持大量的处理器和用户进程)和一个64位的称之为xFS的日志文件系统(它支持高吞吐率和确保I/O速率)来有效地使用系统和增强系统吞吐率。细胞IRIX提供3种调度机制： $\textcircled{1}$ 帧调度(Frame Scheduling)：帧调度器能完全掌管调度和分发进程给一个或多个CPU以确保进程执行的精确速率； $\textcircled{2}$ 组调度(Gang Scheduling)：细胞IRIX能调度一组线程,这些线程可用锁或信号灯相互通信； $\textcircled{3}$ 处理器相似（Processor Affinity)：细胞IRIX能自动记下某一CPU,在该CPU上,上次运行的进程试图运行在同一CPU上。xFS文件系统采用范圈(Extent)概念和日志(Journaling)技术来达到高吞吐率;采用允许应用预约文件系统带宽来确保I/O速率。范围的使用有助于减少磁盘寻找时间和旋转延迟，因而增加了I/O吞吐率；日志(也称为记录,Logging)是一种记录所有文件系统变化的技术，此技术也有助于减少系统恢复时间，因为系统崩溃后,系统只访问少量的最近更新的文件登录，而不必像Unix文件系统那样执行很花时间的文件系统检查。

系统性能因为Origin2000 结构设计很注重整体特性，所以存储器、I/O互连网络的能力都能随机器规模的增大而成比例地增加。表2.3列出了Origin2000中不同层次存储器的读延迟;表2.4列出Origin 2000的总计带宽和存储器读延迟。

表2.3Origin2000不同层次存储读延迟一览表  

<table><tr><td rowspan=1 colspan=1>数据位置</td><td rowspan=1 colspan=1>读延迟(时钟数)</td></tr><tr><td rowspan=1 colspan=1>寄存器</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>1级高速缓存(片上)</td><td rowspan=1 colspan=1>1~3</td></tr><tr><td rowspan=1 colspan=1>2级高速缓存(片外)</td><td rowspan=1 colspan=1>10</td></tr><tr><td rowspan=1 colspan=1>本地存储器</td><td rowspan=1 colspan=1>61</td></tr><tr><td rowspan=1 colspan=1>远程存储器(1个路由器以远)</td><td rowspan=1 colspan=1>117</td></tr><tr><td rowspan=1 colspan=1>远程存储器(2个路由器以远)</td><td rowspan=1 colspan=1>137</td></tr><tr><td rowspan=1 colspan=1>远程存储器(3个路由器以远)</td><td rowspan=1 colspan=1>157</td></tr></table>

表2.4Origin 2000 带宽(GB/s)和延迟 $\mathbf { \eta } ( \mathbf { n s } )$ 一览表  

<table><tr><td rowspan=1 colspan=1>系统配置I/O:节点:CPU</td><td rowspan=1 colspan=1>总计峰值存储器带宽</td><td rowspan=1 colspan=1>总计峰值I/O带宽</td><td rowspan=1 colspan=1>互连网络对剖带宽</td><td rowspan=1 colspan=1>存储器读延迟</td></tr><tr><td rowspan=1 colspan=1>1:1:2</td><td rowspan=1 colspan=1>0.78</td><td rowspan=1 colspan=1>1.56</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>313</td></tr><tr><td rowspan=1 colspan=1>2:2:4</td><td rowspan=1 colspan=1>1.56</td><td rowspan=1 colspan=1>3.12</td><td rowspan=1 colspan=1>1.56</td><td rowspan=1 colspan=1>497</td></tr><tr><td rowspan=1 colspan=1>2:4:8</td><td rowspan=1 colspan=1>3.12</td><td rowspan=1 colspan=1>6.24</td><td rowspan=1 colspan=1>3.12</td><td rowspan=1 colspan=1>601</td></tr><tr><td rowspan=1 colspan=1>4:8:16</td><td rowspan=1 colspan=1>6.24</td><td rowspan=1 colspan=1>12.48</td><td rowspan=1 colspan=1>6.24</td><td rowspan=1 colspan=1>703</td></tr><tr><td rowspan=1 colspan=1>8:16:32</td><td rowspan=1 colspan=1>12.48</td><td rowspan=1 colspan=1>24.96</td><td rowspan=1 colspan=1>12.48</td><td rowspan=1 colspan=1>805</td></tr><tr><td rowspan=1 colspan=1>16:32:64</td><td rowspan=1 colspan=1>24.96</td><td rowspan=1 colspan=1>51.2</td><td rowspan=1 colspan=1>12.48</td><td rowspan=1 colspan=1>908</td></tr><tr><td rowspan=1 colspan=1>32 :64 :128</td><td rowspan=1 colspan=1>49.92</td><td rowspan=1 colspan=1>99.84</td><td rowspan=1 colspan=1>24.96</td><td rowspan=1 colspan=1>1 112</td></tr></table>

由此可看出,总计带宽(存储器、I/O和互连网络)几乎随处理器数线性增加,而延迟只是对数增长。这种低延迟和高带宽使得Origin 2000系统在市场上具有很大的优势。

小结表2.5列出了常用的4种CC-NUMA结构特性比较,其中DASH是个研究样机,而其它几种都已是商品。表中 SCI(Scalabel Coherence Interface)是可扩放一致性接口,它是将传统的总线式底板扩展至全双工、点到点互连结构,SCI互连可以是环形结构或交叉开关结构。

表2.54种CC-NUMA结构比较一览表  

<table><tr><td rowspan=1 colspan=1>结构特性</td><td rowspan=1 colspan=1> StanfordDash</td><td rowspan=1 colspan=1> SequentNUMA-Q</td><td rowspan=1 colspan=1>HP/ConvexEXemplar</td><td rowspan=1 colspan=1>SGI/CrayOrigin 2000</td></tr><tr><td rowspan=1 colspan=1>节点结构</td><td rowspan=1 colspan=1>4CPU SMP节点监听总线</td><td rowspan=1 colspan=1>4CPU SMP节点监听总线</td><td rowspan=1 colspan=1>8CPU SMP节点交叉开关</td><td rowspan=1 colspan=1>2CPU非SMP节点HUB</td></tr><tr><td rowspan=1 colspan=1>节点互连</td><td rowspan=1 colspan=1>2D网孔</td><td rowspan=1 colspan=1>SCI 环</td><td rowspan=1 colspan=1>多 2D SCI环</td><td rowspan=1 colspan=1>胖超立方</td></tr><tr><td rowspan=1 colspan=1>高速缓存一致性协议</td><td rowspan=1 colspan=1>节点内监听全局目录</td><td rowspan=1 colspan=1>SCI 链表一致性协议</td><td rowspan=1 colspan=1>修改的 SCI协议</td><td rowspan=1 colspan=1>修改的Dash协议</td></tr><tr><td rowspan=1 colspan=1>其它</td><td rowspan=1 colspan=1>节点内高速缓存到高速缓存共享</td><td rowspan=1 colspan=1>节点高速缓存组调度相似性调度</td><td rowspan=1 colspan=1>节点高速缓存</td><td rowspan=1 colspan=1>组调度、页面迁移、置放、复制</td></tr></table>

# 2.2大规模并行机 MPP

大规模并行处理机MPP(Massively Parallel Processor)一词的含义过去并不明确,其意义常随时间而变。按照现今的技术,它是指由成百上千个处理器组成的大型(Large-Scale)计算机系统。1997年7月由 Intel和 Sandia研制成的ASCI OptionRed,其处理器数已达9216个,是属于高端MPP系统。MPP系统是属于NORMA(No-Remote Memory Access)模型的机器。早期也曾把非高速缓存一致性NUMA，即NCC-NUMA(Non-Cache Coherent NUMA)模型的机器(例如 Cray T3E)也算作MPP系统,但现在看来T3E仍划分在NUMA类为宜(参见图1.27)。同样现在也把使用机群(Cluster)方法构造的MPP系统(例如 IBMSP2和曙光-2000)也有时单列为机群一类;而把CC-NUMA模型的机器(例如 SGI/Cray Origin 2000)算作是可扩放共享存储多处理机。本节首先讨论MPP的结构特性及其有关问题;然后简介一个当今颇为流行的机群型：大规模并行机 SP2,以期对 MPP系统有个初步了解。

# 2.2.1 MPP结构特性

MPP公共结构所有的 MPP均使用物理上分布的存储器，且使用分布的I/O也渐渐变多。现今的 MPP公共结构如图2.7所示,其中每个节点有一个或多个处理器和高速缓存(P/C)、一个局部存储器、有或没有磁盘和网络接口电路(NIC:Network Interface Circuitry),它们均连向本地互连网络(早期多为总线而近期多为交叉开关),而节点间通过高速网络(HSN:High Speed Network)相连。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0070/auto/images/19b9a9aeeb180a9910ffa9378b96cc18794547c645f075e14e8f0a2cccfba9ad.jpg)  
图2.7MPP公共系统结构

MPP设计问题设计MPP系统所应考虑的问题是：①可扩放性：MPP著名特性就是系统能扩展至成千个处理器，而存储器和I/O的容量及带宽亦能按比例的增加。为此，采用物理上分布的存储器结构，它能提供比集中存储器结构更高的总计存储带宽，因此有潜在的高可扩放性；要平衡处理能力与存储和I/O的能力，因为存储器和I/O子系统的速度不可能与处理器成比例地提高；要平衡计算能力与交互能力，因为进程/线程的管理、通信与同步等都相当费时间。②系统成本：因为MPP系统中包含大量的元件，为了保证系统的低成本应确保每个元件的低成本。为此，应采用现有的商用CMOS微处理器，这些芯片原为PC机、工作站和服务器开发的，自然成本要低，并且按照Mo0re定律其性能每一年半到二年要翻一番；要采用相对稳定的结构，如第一章第1.3.1节所讲的可扩放并行机Shel结构（图1.21)；要使用物理上分布的存储器结构，它比同规模机器的中央(集中）存储器结构要便宜；要采用SMP节点方式以削减互连规模。但是现有的商用微处理器是为小系统(如PC机、工作站和SMP服务器等)而不是为MPP设计的，使用它虽在可扩放性和低成本方面有所得益，但用于MPP也带来一些问题：诸如微处理器地址空间不足够大（例如使用在CrayT3DMPP中的Alpha21064微处理器，它只能提供33位物理地址空间，而T3D最大物理存储容量为128GB)，所以设计者必须加人专门硬件以扩大物理地址空间规模；微处理器和它的计算能力相比，它缺乏足够的操作系统支持，使其难以有效地支持进程管理、通信和同步等。③通用性和可用性：MPP要走向成功之路，它必须是个通用系统，能支持不同的应用(技术和商业）、不同算法范例、不同操作模式,而不能局限于很窄的应用。为此，MPP要支持异步MIMD模式(SIMD似已过时）；要支持流行的标准编程模式（如PVM、MPI和HPF)；诸节点应能按大、小作业要求进行不同的组合以支持交互和批处理模式；互连拓扑应对用户透明，对用户而言他(她)所看到的是一组全连接的节点；MPP应在不同层次上支持单一系统映像SSI(Single-SystemImage),因为紧耦合的MPP常使用分布式操作系统，所以要在硬件级和OS级提供此映像；据估计1000个处理器的MPP系统，每天至少有一个处理器失效，所以MPP必须使用高可用性的技术。④通信要求：MPP和COW的关键差别是节点间的通信，COW使用标准的

LAN,而MPP使用高速、专用高带宽、低延迟的互连网络,无疑在通信方面优于COW。然而通信技术的迅速发展,COW对MPP颇具威胁,从而MPP对通信技术也提出了更高的要求。 $\textcircled{5}$ 存储器和I/O能力：因为MPP是可扩放系统,所以就要求非常大的总计存储器和I/O设备容量，然而I/O方面的进展仍落后于系统中的其余部分,故如何提供一个可扩放的I/O子系统就成为MPP的热门研究课题。

MPP的过去和现在早期的 MPP主要应用于科学和工程超级计算,著名的系统有TM(Thinking Machine） CM2/CM5、NSSA/Goodyear MPP、nCUBE、CrayT3D/T3E、Intel Paragon、MasPar MP1、Fujitsu VPP500 和 KSR1 等。表2.6列出了部分MPP系统的特性比较。表2.7列出了MPP所用的几个典型微处理器特性参数,其中 SPEC(Standard Performance Evaluation Corporation)代表标准性能评价公司,它对目前高性能CPU等进行整数(int)和浮点数(fp)运算性能测试。当今微处理器系列及其代表性的CPU芯片如图2.8所示。现在，很多MPP都已成功地应用在商业和网络应用中。据统计，截止1997年所销售的 SP2系统,大约有一半用于商业(如仓库、决策支持系统和数字图书馆等),剩下的一半大部分用于LAN系统中，只有很少的部分用于科学超级计算。此外,美国开始执行的ASCI计划(见第一章第1.1.2节)也包括研制三台高端 MPP计算机,它们是Intel 公司与 SNL(Sandia 国家实验室)联合研制的Option Red(红选择）、IBM公司与LLNL(LawrenceLivermore国家实验室)联合研制的Blue Pacific(蓝太平洋）和SGI公司与LANL(Los Alamos 国家实验室)联合研制的 Blue Mountain(蓝山）,其主要性能综合于表2.8中。

表2.6典型MPP系统特性比较一览表  

<table><tr><td rowspan=1 colspan=1>结构特性</td><td rowspan=1 colspan=1>IBM SP2</td><td rowspan=1 colspan=1>Cray T3D</td><td rowspan=1 colspan=1>Cray T3E</td><td rowspan=1 colspan=1>Intel Paragon</td><td rowspan=1 colspan=1>Intel/Sandia Option Red</td></tr><tr><td rowspan=1 colspan=1>典型配置</td><td rowspan=1 colspan=1>400个节点100 Gflops</td><td rowspan=1 colspan=1>512个节点153 Gflops</td><td rowspan=1 colspan=1>512个节点1.2 Tflops</td><td rowspan=1 colspan=1>400个节点40 Gflops</td><td rowspan=1 colspan=1>4536个节点1.8 Tflops</td></tr><tr><td rowspan=1 colspan=1>推出日期</td><td rowspan=1 colspan=1>1994</td><td rowspan=1 colspan=1>1993</td><td rowspan=1 colspan=1>1996</td><td rowspan=1 colspan=1>1992</td><td rowspan=1 colspan=1>1996</td></tr><tr><td rowspan=1 colspan=1>CPU类型</td><td rowspan=1 colspan=1>67 MHz267 MflopsPOWER2</td><td rowspan=1 colspan=1>150 MHz150 MflopsAlpha 21064</td><td rowspan=1 colspan=1>300 MHz600 MflopsAlpha 21164</td><td rowspan=1 colspan=1>50 MHz100 MflopsInteli 860</td><td rowspan=1 colspan=1>200 MHz200 MflopsPentium Pro</td></tr><tr><td rowspan=1 colspan=1>节点结构数据存储</td><td rowspan=1 colspan=1>1 CPU64 MB~2 GB局存1~4.5GB本地磁盘</td><td rowspan=1 colspan=1>2 CPU64 MB主存50 GB共享磁盘</td><td rowspan=1 colspan=1>4~8 CPU256 MB~16 GB16～128 MBDSM主存，共享磁盘</td><td rowspan=1 colspan=1>1~2 CPU256 MB~16 GB16～128 MB局存，48GB共享磁盘</td><td rowspan=1 colspan=1>2 CPU32～256MB局存,共享磁盘</td></tr><tr><td rowspan=1 colspan=1>互连网络</td><td rowspan=1 colspan=1>多级互连网络</td><td rowspan=1 colspan=1>3-D环绕</td><td rowspan=1 colspan=1>3-D环绕</td><td rowspan=1 colspan=1>2-D网孔</td><td rowspan=1 colspan=1>Split2-D 网孔</td></tr><tr><td rowspan=1 colspan=1>访存模型</td><td rowspan=1 colspan=1>NORMA</td><td rowspan=1 colspan=1>NUMA</td><td rowspan=1 colspan=1>NCC-NUMA</td><td rowspan=1 colspan=1>NORMA</td><td rowspan=1 colspan=1>NORMA</td></tr><tr><td rowspan=1 colspan=1>节点OS</td><td rowspan=1 colspan=1>Complete AIX（IBM Unix)</td><td rowspan=1 colspan=1>微核</td><td rowspan=1 colspan=1>基于 Chorus微核</td><td rowspan=1 colspan=1>微核</td><td rowspan=1 colspan=1>轻量级核(LWK)</td></tr><tr><td rowspan=1 colspan=1>编程模型</td><td rowspan=1 colspan=1>消息传递</td><td rowspan=1 colspan=1>共享变量、消息传递、PVM</td><td rowspan=1 colspan=1>共享变量、消息传递、PVM</td><td rowspan=1 colspan=1>消息传递</td><td rowspan=1 colspan=1>基于PUMA Portals消息传递</td></tr><tr><td rowspan=1 colspan=1>编程语言</td><td rowspan=1 colspan=1>MPI、PVMHPF、Linda</td><td rowspan=1 colspan=1>MPI、HPF</td><td rowspan=1 colspan=1>MPI、HPF</td><td rowspan=1 colspan=1>NX、MPIPVM</td><td rowspan=1 colspan=1>NX、PVM、HPF</td></tr><tr><td rowspan=1 colspan=1>点到点通信延迟</td><td rowspan=1 colspan=1>40 μs</td><td rowspan=1 colspan=1>2us</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>30 us</td><td rowspan=1 colspan=1>10 μus</td></tr><tr><td rowspan=1 colspan=1>点到点带宽</td><td rowspan=1 colspan=1>35 MB/s</td><td rowspan=1 colspan=1>150 MB/s</td><td rowspan=1 colspan=1>480 MB/s</td><td rowspan=1 colspan=1>175 MB/s</td><td rowspan=1 colspan=1>380 MB/s</td></tr></table>

表2.7 MPP所用的高性能CPU特性参数一览表  

<table><tr><td></td><td rowspan=1 colspan=2>属性</td><td rowspan=1 colspan=1>Pentium Pro</td><td rowspan=1 colspan=1>Power PC620</td><td rowspan=1 colspan=1>Alpha 21164A Ultra SPARCI</td><td rowspan=1 colspan=1>Alpha 21164A Ultra SPARCI</td><td rowspan=1 colspan=1>MIPS R10000</td></tr><tr><td></td><td rowspan=1 colspan=2>工艺</td><td rowspan=1 colspan=1>BiCMOS</td><td rowspan=1 colspan=1>CMOS</td><td rowspan=1 colspan=1>CMOS</td><td rowspan=1 colspan=1>CMOS</td><td rowspan=1 colspan=1>CMOS</td></tr><tr><td></td><td rowspan=1 colspan=2>晶体管数</td><td rowspan=1 colspan=1>5.5 M/15.5 M</td><td rowspan=1 colspan=1>7 M</td><td rowspan=1 colspan=1>9.6 M</td><td rowspan=1 colspan=1>5.4 M</td><td rowspan=1 colspan=1>6.8 M</td></tr><tr><td></td><td rowspan=1 colspan=2>时钟频率</td><td rowspan=1 colspan=1>150 MHz</td><td rowspan=1 colspan=1>133 MHz</td><td rowspan=1 colspan=1>417 MHz</td><td rowspan=1 colspan=1>200 MHz</td><td rowspan=1 colspan=1>200 MHz</td></tr><tr><td></td><td rowspan=1 colspan=2>电压</td><td rowspan=1 colspan=1>2.9 V</td><td rowspan=1 colspan=1>3.3 V</td><td rowspan=1 colspan=1>2.2 V</td><td rowspan=1 colspan=1>2.5 V</td><td rowspan=1 colspan=1>3.3 V</td></tr><tr><td></td><td rowspan=1 colspan=2>功率</td><td rowspan=1 colspan=1>20 w</td><td rowspan=1 colspan=1>30 W</td><td rowspan=1 colspan=1>20 W</td><td rowspan=1 colspan=1>28W</td><td rowspan=1 colspan=1>30 W</td></tr><tr><td></td><td rowspan=1 colspan=2>字长</td><td rowspan=1 colspan=1>32位</td><td rowspan=1 colspan=1>64位</td><td rowspan=1 colspan=1>64位</td><td rowspan=1 colspan=1>64位</td><td rowspan=1 colspan=1>64位</td></tr><tr><td></td><td rowspan=1 colspan=2>I/O高速缓存</td><td rowspan=1 colspan=1>8 KB/8 KB</td><td rowspan=1 colspan=1>32 KB/32 KB</td><td rowspan=1 colspan=1>8 KB/8 KB</td><td rowspan=1 colspan=1>16 KB/16 KB</td><td rowspan=1 colspan=1>32 KB/32 KB</td></tr><tr><td></td><td rowspan=1 colspan=2>2级高速缓存</td><td rowspan=1 colspan=1>256 KB（多芯片模块）</td><td rowspan=1 colspan=1>1~128 MB（片外）</td><td rowspan=1 colspan=1>96 KB（片上）</td><td rowspan=1 colspan=1>16 MB（片外）</td><td rowspan=1 colspan=1>16 MB（片外）</td></tr><tr><td></td><td rowspan=1 colspan=1>执行单元</td><td></td><td rowspan=1 colspan=1>5个单元</td><td rowspan=1 colspan=1>6个单元</td><td rowspan=1 colspan=1>4个单元</td><td rowspan=1 colspan=1>9个单元</td><td rowspan=1 colspan=1>5个单元</td></tr><tr><td></td><td rowspan=1 colspan=2>超标量</td><td rowspan=1 colspan=2>3路(Way)</td><td rowspan=1 colspan=1>4路</td><td rowspan=1 colspan=1>4路</td><td rowspan=1 colspan=1>4路</td><td rowspan=1 colspan=1>4路</td></tr><tr><td></td><td rowspan=1 colspan=2>流水线深度</td><td rowspan=1 colspan=2>14级</td><td rowspan=1 colspan=1>4~8级</td><td rowspan=1 colspan=1>7~9级</td><td rowspan=1 colspan=1>9级</td><td rowspan=1 colspan=1>5~7级</td></tr><tr><td></td><td rowspan=1 colspan=1>SPECint 92</td><td rowspan=1 colspan=2>366</td><td rowspan=1 colspan=1>225</td><td rowspan=1 colspan=1>&gt;500</td><td rowspan=1 colspan=1>350</td><td rowspan=1 colspan=1>300</td></tr><tr><td></td><td rowspan=1 colspan=1>SPECfp 92</td><td rowspan=1 colspan=2>283</td><td rowspan=1 colspan=1>300</td><td rowspan=1 colspan=1>&gt;750</td><td rowspan=1 colspan=1>550</td><td rowspan=1 colspan=1>600</td></tr><tr><td></td><td rowspan=1 colspan=1>SPECint 95</td><td rowspan=1 colspan=2>8.09</td><td rowspan=1 colspan=1>225</td><td rowspan=1 colspan=1>&gt;11</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>7.4</td></tr><tr><td></td><td rowspan=1 colspan=1>SPECfp 95</td><td rowspan=1 colspan=2>6.70</td><td rowspan=1 colspan=1>300</td><td rowspan=1 colspan=1>&gt;17</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>15</td></tr><tr><td rowspan=1 colspan=2>其它特性</td><td rowspan=1 colspan=2>CISC/RISC混合</td><td rowspan=1 colspan=1>短流水线长L1高速缓存</td><td rowspan=1 colspan=1>最高时钟频率最大片上2级高速缓存</td><td rowspan=1 colspan=1>多媒体和图形指令</td><td rowspan=1 colspan=1>MP机群总线可支持4 CPU</td></tr></table>

表2.8ASCI计划的3个高端 MPP系统特性一览表  

<table><tr><td rowspan=1 colspan=1>特性</td><td rowspan=1 colspan=1>Intel/SNLOption Red</td><td rowspan=1 colspan=1>IBM/LLNLBlue Pacific</td><td rowspan=1 colspan=1>SGI/LANLBlue Mountain</td></tr><tr><td rowspan=1 colspan=1>处理器</td><td rowspan=1 colspan=1>Pentium Pro200 MHz200 Mflops</td><td rowspan=1 colspan=1>POWER3200 MHz 800 Mflops</td><td rowspan=1 colspan=1>MIPS1 Gflops</td></tr><tr><td rowspan=1 colspan=1>系统结构</td><td rowspan=1 colspan=1>NORMA-MPP</td><td rowspan=1 colspan=1>Cluster</td><td rowspan=1 colspan=1>CC-NUMA</td></tr><tr><td rowspan=1 colspan=1>处理器数</td><td rowspan=1 colspan=1>9 216</td><td rowspan=1 colspan=1>4 096</td><td rowspan=1 colspan=1>3072</td></tr><tr><td rowspan=1 colspan=1>峰值速度(T=1012)</td><td rowspan=1 colspan=1>1.8 Tflops</td><td rowspan=1 colspan=1>3.2 Tflops</td><td rowspan=1 colspan=1>&gt;3 Tflops</td></tr><tr><td rowspan=1 colspan=1>存储容量</td><td rowspan=1 colspan=1>594 GB</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>N/A</td></tr><tr><td rowspan=1 colspan=1>磁盘容量</td><td rowspan=1 colspan=1>1 TB</td><td rowspan=1 colspan=1>&gt;5 TB</td><td rowspan=1 colspan=1>N/A</td></tr><tr><td rowspan=1 colspan=1>推出时间</td><td rowspan=1 colspan=1>1997.6</td><td rowspan=1 colspan=1>1998.12</td><td rowspan=1 colspan=1>1998.12</td></tr></table>

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0070/auto/images/eb9039be60d1bffdc23cc85e9794fea0c7cf8e63f2d677bb258bb9dc369757d1.jpg)  
图2.8微处理器系列及其代表性CPU芯片

# \*2.2.2 机群型大规模并行机 SP2

1991年秋,IBM决定涉足于 MPP 的研究,开动了 SP(Scalable POWERpar-allel)计划。1992年2月开始组队,1993年4月就公布了第一个产品 SP1,继之于1994年7月就宣布了SP2。IBM的 SP是比较特殊的,它采用了机群的办法来构筑MPP。到1998 年之前,其在世界上的总装机量超过3000,实属MPP系统成功之例。

设计目标和策略IBM设计 SP系统时提出了如下目标： $\textcircled{1}$ 赶市场：遵循着


<!-- chunk 0002: pages 71-140 -->
Moore定律，为夺性能/价格之冠,产品必须在短期内开发成功； $\textcircled{2}$ 通用：SP必须是个能支持不同的技术和商业应用、流行的编程模式和不同操作模式的通用系统； $\textcircled{3}$ 高性能：SP必须提供整体性能,不仅是处理器速度快，而且存储器和通信系统要快，有优良的编译器和各种库等； $\textcircled{4}$ 有效性：SP必须呈现好的可靠性和可用性,使得用户能够方便地在其上运行商业成品代码。为了满足上述目的,IBM设计小分队采用的策略是：灵活的机群结构;专用互连网络;标准的系统环境；标准的编程模式和有选择的单一系统映像支持。

$\textcircled{1}$ 机群结构：为了达到赶市场和通用的目的,选用机群结构是个关键，其中每个节点都是个RS/6000工作站且各有本地磁盘;每个节点内驻留一个完整的AIX(IBM的Unix);各节点经其I/O总线(非本地存储总线)连向专门设计的多级高速网络。SP系列尽量使用标准的工作站组件,只有不能满足要求时才使用专用的硬件和软件。这样的结构既简单又灵活且系统的规模是可扩放的（从很少的几个节点到数百个节点)。

②标准环境:SP使用标准的、开放式的、分布式Unix环境，它能利用现存的标准软件以进行系统管理、作业管理、存储管理等,所有这些软件IBM工作站AIX操作系统中均有。对于那些AIX环境不能有效执行的应用,SP 提供了一组高性能服务，诸如高性能开关(HPS)、用户级通信协议(US协议）、优化的消息传递库(MPL）、并行程序开发和执行环境、并行文件系统、并行数据库和高性能I/O子系统等。

③标准编程模式：SP系统以标准编程模式支持以下三种应用方式：①串行计算：尽管 SP2是个并行机,但它允许现有的以C、C++和 Fortran编写的串行程序可不加修改地运行在单节点的SP系统上,这是可以理解的，因为机群结构和标准的环境确保了这一点;②并行科技计算:SP现在支持MPL、MPI、PVM、HPF模式,正打算支持共享存储的模式;③并行商用计算：IBM正在并行化一些关键数据库、事务监视子系统,现今IBMDB2数据库系统的并行版本已在 SP2上实现。

④系统可用性：SP系统由上千个部件组成，它们原先是为低价的、规模不大的工作站设计的,现把它们组织在一起必然经常失效。但SP是个机群结构，而机群结构意味着是一个分开的操作系统映像,它和SMP结构驻留在共享存储器中的单一操作系统映像不同(它的OS出错将导致全系统崩溃),机群结构一个节点映像失效不会导致全系统崩溃;另外SP的诸节点均同时连向以太网和高性能开关网,这样一个网络的失效，节点间还可使用另一个网络进行通信；还有 SP的软件基础设施也提供了故障检测、诊断、系统重组和故障恢复等服务。

③ 部分单一系统映像：在一个分布系统中,用户看到的是一些单独的、分开的工作站，真正的单一系统映像是很难实现的，且对某些商业应用它也不是个关键的要求。所以IBM的设计者们，只是在单进入点、单文件层、单控制点和单作业管理系统方面实现了单一系统映像，而在SP系统中并不实现单地址空间。

系统结构SP系统简化框图如图2.9所示。一个SP系统可含 $2 \sim 5 1 2$ 个节点，每个节点有其自己的局存和本地磁盘。所有的节点均连向两个网络：普通的以太网和HPS(High Performance Switch）。以太网虽慢但有很多好处：当HPS失效时，它可作为后援；当HPS正被开发或改进时，仍可利用以太网查错、测试和维持系统运行；此外以太网也可用来系统监视、引导、加载和管理等。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/942e4df6865015a4504a5d9222fb275e4871d88426ef523bc50a82be84fe3c9d.jpg)  
图2.9SP系统结构

①系统互连：高性能开关（HPS)由节点内的开关硬件和开关帧（SwitchFrames)组成。图2.10示出了IBMSP2中所使用的128路高性能开关，其中每帧由一个16路开关板所连接的16个处理节点(No～N15）所组成,8个帧再用一个附加级开关板连接起来(图中细线代表8位的双向链路，而粗线代表4个8位的双向链路）,每一开关板上有两级开关芯片，所以此多级互连网络(MIN)总共有4个开关板。HPS是一个使用此开关的由40MHz时钟驱动的带缓冲的多级Ω互连网络。它使用了虫蚀选路法，一个8位的flits在无竞争时穿过一级（即一个开关芯片）只需5个时钟（即125ns)。因此HPS无竞争时的硬件延迟是很小的，对于512个节点仅875ns。但实际延迟比此值高得多，一个进程发送一个空包给另一个进程至少花40μs,这种消息传递延迟大部分是由软件开销造成的。HPS能提供成对节点之间的双向传输带宽为40MB/s。

②节点结构：SP2有三种不同的节点，分别是宽节点（WideNode）、窄节点（ThinNode)和窄节点1,它们主要差别在于存储器的容量、数据路径宽度和I/O总线的槽数的不同，但是所有的这些节点都使用时钟为66.7MHz的POWER(Performance OptimizedWith Enhanced RISC)-2微处理器。每个处理器有一个32KB的指令高速缓存、256KB的数据高速缓存、指令和转移控制单元、两个定点运算单元、两个各能执行乘-加操作的浮点运算单元。由于定点和浮点运算可同时进行，所以 POWER-2具有4×66.7 Mflops=267 Mflops的峰值速度。POWER-2是个超标量处理器，它使用短指令流水线、先进的转移预测技术和寄存器重命名技术，使得它在每个时钟周期内能执行6条指令：两条取/存指令、两条浮点乘-加指令、一条变址增一指令和一条条件转移指令。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/44c18f7f8b91604ae47f2bf999fef37ed4911abaadffadd3ebdec2a4d03af0d8.jpg)  
图2.10 SP2中的128 路高性能开关(HPS)

I/O子系统和网络接口SP的I/O子系统如图2.11所示，它基本上是围绕着HPS构筑起来的,并用LAN的信关与 SP系统以外的机器相连。SP的节点有4类：主机节点 $( \mathrm { H } )$ 用于用户登录和交互处理;I/O节点主要执行I/O功能(如全局文件服务);信关节点(G)用于连网;计算节点(C)专负责计算。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/4efd3332b17686467549f1d6ead594e0190549ee9d36b670b0a0c7e11d05a95c.jpg)  
图2.11 SPI/O子系统

每个 SP 节点通过网络接口电路(NIC)与HPS 相连,NIC也叫作开关适配器或通信适配器。如图2.12所示,适配器包含-个8MB的DRAM和受控于-个40MHz的i860 微处理器。适配器经微通道接口搭在微通道（Micro（han-nel)上,它是一个标准的I/O总线并用于将外设连向RS/6000工作站和IBMPC机，同时适配器也经过存储和开关管理单元（MSMU:Memoryand SwitchManage-ment Unit)连向 HPS(经由各为8位宽的 IN-FIFO和OUT-FIFO)。除此之外,它还包含·些控制/状态寄存器和用作 i860总线控制器,检查和刷新DRAM。另外，个4 KB 的双向FIFO(BIDI)缓冲器用于连接微通道和 i860总线。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/a002d52cc56687b65d3eb427759733536042be43bd0a39e44071578d3a7ce5ce.jpg)  
图2.12SP通信适配器

参照图2.12来解释一下数据从节点发往HPS的过程：当节点处理器告诉适配器要发送数据时,i860 将直接存储访问DMA(DirectMemory Access)传输所必需的信息(称为Header)写人BIDI,当此Header抵达BIDI之首部时,左部DMA(L-DMA)负责将数据从节点(微通道)传人BIDI;完成时，L-DMA将硬件计数器增--,i860 写另一个Header至右部 DMA(R-DMA),R-DMA 负责将数据从BIDI传至MSMU中的OUT-FIFO,然后再将数据传送至 $\mathrm { H P S } _ { \circ }$

从HPS接收数据是类似的：当数据到达时，MSMU通知i860,它就写一个Header以启动R-DMA,R-DMA 就负责将数据从IN-FIFO传至BIDI;完成时，i860向BIDI写人一个Header,当它抵达 BIDI之首部时,L-DMA抽取此Head-er,并负责将数据从BIDI传至微通道。

系统软件SP系统软件层次如图2.13所示，其核心部分是IBMAIX操作系统。SP沿用了绝大部分RS/6000工作站环境，包括数据库管理系统（如DB2),在线事务处理监视器(如（ICS/6000),系统管理和作业管理,标准操作系统 AIX,Fortran、 $\therefore \ l ( \cdot + \cdot +$ 编译器,数学和工程库(如ESSL)以及上万个串行应用程序等。SP系统只加入了若干新软件和改进了某些现存的软件，它们都是可扩放并行机群系统所要求的。

图2.13SP系统软件层次  

<table><tr><td rowspan=1 colspan=4>应  用</td></tr><tr><td rowspan=1 colspan=4>应用子系统（数据库、事务处理监视器等）</td></tr><tr><td rowspan=1 colspan=1>系统管理</td><td rowspan=1 colspan=1>作业管理</td><td rowspan=1 colspan=1>并行环境</td><td rowspan=1 colspan=1>编译器等</td></tr><tr><td rowspan=1 colspan=4>全局服务（提供单一系统映像）</td></tr><tr><td rowspan=1 colspan=4>有效性服务</td></tr><tr><td rowspan=1 colspan=2>高性能服务</td><td rowspan=1 colspan=2>标准操作系统（AIX）</td></tr><tr><td rowspan=1 colspan=4>标准RS/6000硬件（处理器、存储器、I/O设备、适配器）</td></tr></table>

$\textcircled{1}$ 并行环境:AIX并行环境PE(Parallel Environment)为用户提供了开发和执行并行程序的平台，如图2.14所示，它包含4部分：

并行操作环境 POE（Parallel Operating Environment），消息传递库 MPL（Message Passing Library),可视化工具VT(Visualization Tool)和并行查错 Pdbx(ParallelDebugger)。其中POE用于控制并行程序的执行，它是由一个运行在家用节点(是一个连向 SP节点的RS/6000 工作站)上的划分管理程序(PartitionManager)来控制。家用节点是用户调用并行程序的地方，并行程序作为SP计算节点上--个或多个任务来运行。家用节点提供标准的UnixI/O设备（如Stdin、Stdout和 Stderr),它通过LAN(如以太网)与计算节点进行标准的I/O通信。例如用户从家用节点的键盘上按 $\mathsf { c u r l } + \mathsf { C }$ 键可终止所有的任务，用Printf语句就可在家用节点的屏幕上显示输出。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/04754da7107ddbadc8f7630ad8e2fba56c53f559a1f5cf6637bac78d409203c7.jpg)  
图2.14 SP机群的并行环境(PE)

消息传递通信是经由HPS或以太网执行专门MPL功能实现的,这个库提供诸如进程管理、点到点通信、整体通信等33种功能,IBM SP还支持MPI的不同版本。

②高性能服务：IBMSP除了能直接使用标准的、商用的原来为RS/6000工作站和基于TCP/IP网络的分布系统所开发的软件外，它还提供了一些高性能服务，包括高性能通信子系统、高性能文件系统、并行库、并行数据库和高性能1/0等。

SP支持两种通信协议：基于IP的协议(执行在核空间)和US协议(执行在用户空间),两者均可在HPS上或常规网（如以太网）上使用。但US协议具有较好的性能，可它每个节点中只允许有-个任务去使用US协议；当每个节点上有多个任务时，使用基于IP的协议可导致较好的整个系统的利用率。

③ 并行I/O文件系统:SP高性能文件系统称之为并行I/O文件系统PI-OFS(ParallelI/OFile System）,对绝大多数应用和系统实用程序它是与POSIX-致的，Unix 操作和命令(如 read、write、open、close、ls、cp 和mv 等）与顺序U-nix系统中的--样,除了允许传统的Unix文件系统接口外,PIOFS提供了并行接口以便能对文件进行并行分布和操作。

IBM开发了称之为DB2并行版本的并行数据库软件程序，它能运行在 SP和其它机群平台上。数据库分布在多个节点中，数据库功能则装人数据驻留的节点上。DB2并行版本在机器规模和问题规模两方面都是可扩放的，它能运行在数百个节点上并能处理多达万亿字节(Terabytes)的大型数据库。

$\textcircled{4}$ 有效性服务：SP系统由一组运行在节点上的守护程序(Daemon)提供软件有效性基础设施。心跳(Heartbeat)守护程序周期地也改变心跳信息以指示哪些节点是存在的。属籍(Membership)服务能识别节点和进程属于某一组。当属籍关系因节点失效、停机或再启动改变时，通告(Notification)服务用来通知活动的成员，并随后调用恢复(Recovery)服务协调恢复以使活动的成员继续工作。

$\textcircled{5}$ 全局服务：SP系统提供的全局服务有外部系统数据储存库 SDR(SystemDataRepository),它维持有关节点、开关和现行作业等全系统的信息。当部分系统失效时 SDR对重组系统是有用的,其内容能将系统带回失效前的状态。

采用通过HPS支持TCP/IP和UDP/IP可实现全局网络访问。通过网络文件系统(NFS)可提供单一文件系统。除了NFS外,SP还为全局磁盘访问提供虚拟共事磁盘VSD(Virtual Shared Disk)技术。VSD 是位于 AIX 逻辑盘组管理器LVM(LogicalVolume Manager)之顶的一个设备驱动层。当一个节点进程欲访问本地共享磁盘时，VSD直接传递请求至节点的LVM;当一个节点进程欲访问远程共享磁盘时,VSD传递请求至远程磁盘的VSD,然后再将其传至远程节点的LVM。

$\textcircled{6}$ 系统管理:SP系统控制台(C)是一台控制工作站(见图2.9)。SP系统管理器从此单控制点管理整个SP系统：包括系统安装、监视和配置、系统操作、用户管理、文件管理、作业记费、打印和邮件服务等。此外,SP中的每个节点、开关等都有一块能自动检测环境条件的监视卡以及时控制硬件部件。管理者能使用这些设施开/关电源和监视器,复位单节点和开关等部件。还有,SP支持用户交互和批处理两种作业模式，它们既可以是串行程序也可以是并行程序。

# 2.3工作站机群COW

工作站机群COW(Cluster ofWorkstations)是实现并行计算的一种新主流技术,是属于分布式存储的MIMD并行计算机结构，系由工作站和互连网络两部分组成。由于这种结构用于并行计算的主要资源是工作站,所以工作站机群的名称便由此产生。工作站机群COW这一名称,在早期的研究阶段，也曾被称为工作站网络 NOW(Network of Workstations);在近几年的商业和企业界的应用中，也把使用机群技术(Clustering)构筑的MPP(如前面第2.2.2节所讲的

SP2)有区别地称作机群。本节着重讨论早期带有研究性质的（OW，首先介绍其基本原理及其有关问题;然后介绍一下Berkeley 大学的NOW研究计划。

# 2.3.1 COW的基本原理与技术

什么是COW随着工作站性能迅速提高和价格日益下降以及高速网络产品陆续问世，--种新型的并行计算系统便应运而生。这种系统将一群工作站用某种结构的网络互连起来,充分利用各工作站的资源,统一调度、协调处理,以实现高效并行计算。图2.15示出了COW的硬件组成，它由工作站和互连网络两部分组成,工作站上增加一块主机接口板以实现连网。互连网络可以是普通的LAN(如以太网、令牌环和FDDI等),也可以是高速开关网络(如ATM、交换式高速以太网等)。工作站是个广义的称呼,它可以是高档微机,甚至也可以是个对称多处理机SMP。一个实用的COW还应有一个高效的软件环境,如图2.16所示,包括操作系统(可为通用的Unix、AIX,也可为改进和修改的操作系统）、通信协议(实现工作站到互连网络的数据通信服务）、可由用户调用的通信原语库以及并行程序设计环境与工具等。从用户、程序员和系统管理员的角度看，(OW 相当于单一并行系统,感觉不到多个工作站的实际存在;从程序设计模式的角度看,它与MPP一样可采用面向消息传递的 SPMD(Single Program Multi-ple Data)编程方式,即各个工作站均运行同一个程序,但分别加载不同的数据，从而可支持粗粒度的并行应用程序。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/e38e7eaf09dab43bf1c5d5c53e14cb95b1ac44165891dd666079c3c24454303c.jpg)  
图2.15（OW的一般结构  
图2.16（OW的软件结构

<table><tr><td rowspan=1 colspan=1>并行应用程序</td><td rowspan=1 colspan=1>并行工其包</td></tr><tr><td rowspan=1 colspan=1>并行程序设计环境、通信原语库</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=2>通信协议</td></tr><tr><td rowspan=1 colspan=2>操作系统</td></tr><tr><td rowspan=1 colspan=2>处理机与高速通信部件</td></tr></table>

为什么发展COW和前面所介绍的对称多处理机 SMP和大规模并行机

MPP相比，COW在实用上具有一些明显的优点： $\textcircled{1}$ 投资风险小：用户在购置传统巨型机或MPP系统时，总是担心使用效率不高和性能发挥得不好，如果购置后在一定程度上确实出现此问题，就相当于搁置或浪费了大批资金，但COW不存在此问题，因为即使COW在技术上不够先进，但每台高性能的工作站仍可照旧使用，不会浪费资金； $\textcircled{2}$ 编程方便：用户无需学用新的并行程序设计语言（如并行C、并行 $\ b { \mathbb { C } } + \ b { \mathbb { + } }$ 、并行Fortran等），只要利用所提供的并行程序设计环境，在常规 ${ \mathbb C } \mathrm { , } { \mathbb C } + +$ 和Fortran等程序中相应的地方插人少量的几条原语，即可使这些程序在COW上运行，这一点是最受用户欢迎的； $\textcircled{3}$ 系统结构灵活：用户将不同性能的工作站使用不同的体系结构和各种互连网络构成同构或异构的工作站机群系统，从而可弥补单一体系结构适应面窄的弱点，可更充分地满足各类应用要求； $\textcircled{4}$ 性能/价格比高：一般一台巨型机或MPP都很昂贵(费用常以几百万元、几千万元计),而一台高性能工作站相对便宜(费用仅以几万元或十几万元计），一个COW系统从浮点运算能力来看，虽然每台工作站只有几Mflops到几十Mflops,但一群工作站的总体运算性能可高达Gflops的量级，能接近一些巨型机的性能，但价格却低了很多； $\textcircled{5}$ 能充分利用分散的计算资源：当个人工作站处于空闲状态时,COW可在空闲时间内给这些工作站加载并行计算任务，从而工作站资源可得到充分利用； $\textcircled{6}$ 可扩放性好：用户可根据需要增加工作站的数目，以高带宽和低延迟的网络技术支持获得高的加速比，从而获得应用问题的高可扩放性。

COW的关键技术实现工作站机群需要解决的主要问题是通信性能和并行编程环境。因为组成COW的硬件环境中工作站的性能已相当高，且还在不断的提高，相对而言工作站性能不是关键问题;相反，负责数据通信的互连网络却是一项关键技术，因为COW系统中并行计算时各工作站之间需要经过互连网络交换数据，某些工作站上的程序所需要的数据也往往要通过网络获取或提交。如果网络通信延迟时间很长，再加上用于通信的软件开销(此部分不可忽视)可能就限制了COW技术对某些问题的适应性。近几年来网络技术发展很快,ATM给予COW技术强大的支持,其156Mb/s的传输速率以及高带宽的特性保证了数据通信的高速进行；另外 IEEE/ANSIP1596互连标准 SCI(ScalableCoherenceInterface)可支持多达64K个节点互连,并能实现二级高速缓存一致性协议，传输速率可以达到1Gb/s,从而可很好地支持工作站的互连。

伴随高速网络而产生的另一关键技术是工作站到网络的主机接口网络接口的设计，它应尽量保持网络的传输速度与主机数据收发速度相匹配,其中增加高速缓存或采用DMA是可供选择的两种技术。网络接口使工作站可以利用网络传输数据，但也增加了通信延迟,它占用工作站CPU时间，从而影响了COW的性能。一般,一次通信时间延迟可如图2.17所示，其中D为操作系统调度时间,A用于分配缓冲，C用于拷贝数据到系统缓冲区,S为启动发送/接收时间，T为链路传输时间,F用于定位中断源，X用于从接收队列获取数据。一般减少延迟的方法有： $\textcircled{1}$ 设计精简通信协议以减少数据移动的次数和协议处理时间； $\textcircled{2}$ 采用主动消息(ActiveMessage)携带数据处理命令以重叠计算和通信； $\textcircled{3}$ 定制通信处理单元以消除通信对工作站CPU的依赖。

另外，COW要走向实用必须为用户提供一个良好使用环境和一套完善的工具系统，主要包括： $\textcircled{1}$ 并行编程环境，如一些通信原语库、多种编程语言( $\mathrm { L } \mathbf { x } - \mathrm { \partial }$ press、PVM、Linda、 $\boldsymbol { \mathrm { P _ { + } } }$ 、MPI)的支持以及并行编译器等； $\textcircled{2}$ 可视化监视/调试器（如 Express 的 domtool、基于PVM的 XPVM等）; $\textcircled{3}$ 并行图形库（如基于Express的Plotix等）; $\textcircled{4}$ 并行文件系统和数据库，以适应开展分布式事务处理的研究与开发。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/3665163e00e50fcde518804dead9745a79103989a7effaa682a32833e0ac5865.jpg)  
图2.17-次通信的时间延迟

COW研究的新进展随着（OW研究的深人开展，很多大学和实验室都建立了各具特色的实验型（OW系统。表2.9列出了几例具有代表性的机群研究计划,它在一定程度上反映了COW技术的新进展。其中,NOW系统涉及到了机群计算的很多问题,包括结构、支持Web服务器的软件、单一系统映像、I/O和文件系统、有效通信和强化的可用性(我们在下一节专门讨论它);Princeton的 SHRIMP计划，集中研究在基于PC机的机群上，支持有效通信和共享存储，开发了专门的网络接口板，可以达页面迁移级共享虚拟存储器；Wisconsin的WindTunnel计划,正在调研如何用商用节点和网络构成的松散耦合机群上实现高速缓存-致性共享存储器;Rice的TreadMarks是一个软件实现共享存储的工作站机群的优秀例子,它用用广空间运行时的库来实现存储器共享;由Chica-go、Maryland 和 Pennsylvania 共同发起的 NSCP(National Scalable （luster Pro-jcct)计划,旨在研究异构机群上的元计算(Metacompuling),NSCP样机系统是由上述三所大学的局部网通过Intcrnet互连起来而构成;Argonne 的Globus计划也是研究元计算的，它将北美17个站点上的超级计算机、海量存储器和可视化设备用ATM网连起来;Syracuse 的 WWVM(Word-Wide Virtual Machine）计划,目的在 于使用 Internet 和 HPCC(High Performance Computing and Communi-cation)技术实现高性能计算；Virginia的Legion 计划,意在美国本土的国家虚拟计算机设施上开发元计算软件；香港大学的PearlCluster计划是一个用ATM连接的基于Unix 服务器和工作站(如 SUN、HP、Alpha、SGI)的机群系统(参见图1.19),其优异特性包括:支持 SSI的中间件(Middleware）、两种语言Internet搜索工具和Java接口的MPI通信子系统等,它们都用于财务数字库和分布式多媒体的应用。

表2.9典型的机群系统特点一览表  

<table><tr><td rowspan=1 colspan=1>名称</td><td rowspan=1 colspan=1>系统特点</td></tr><tr><td rowspan=1 colspan=1>Berkeley :NOW</td><td rowspan=1 colspan=1>非服务器工作站网络主动消息，协同文件系统，全局Unix扩展</td></tr><tr><td rowspan=1 colspan=1>Princeton :SHRIMP</td><td rowspan=1 colspan=1>PC商用组件，通过专用网络接口达到共享虚拟存储，支持有效通信</td></tr><tr><td rowspan=1 colspan=1>Karsruhe:Parastation</td><td rowspan=1 colspan=1>用于分布并行处理的有效通信网络和软件开发</td></tr><tr><td rowspan=1 colspan=1>Rice:Tread Marks</td><td rowspan=1 colspan=1>软件实现的分布共享存储的工作站机群</td></tr><tr><td rowspan=1 colspan=1>Wisconsin :Wind Tunnel</td><td rowspan=1 colspan=1>在经由商用网络互连的工作站机群上实现分布式共享存储</td></tr><tr><td rowspan=1 colspan=1>Chica、Maryl、Penns:NSCP</td><td rowspan=1 colspan=1>国家可扩放机群计划：在通过因特网互连的3个本地机群系统上进行元计算</td></tr><tr><td rowspan=1 colspan=1>Argonne:Globus</td><td rowspan=1 colspan=1>在由ATM连接的北美17个站点的WAN上开发元计算平台和软件</td></tr><tr><td rowspan=1 colspan=1> Syracuse:WWVM</td><td rowspan=1 colspan=1>使用因特网和HPCC技术，在世界范围的虚拟机上进行高性能计算</td></tr><tr><td rowspan=1 colspan=1>HKU:Pearl Cluster</td><td rowspan=1 colspan=1>研究机群在分布式多媒体和金融数字库方面的应用</td></tr><tr><td rowspan=1 colspan=1>Virginia:Legion</td><td rowspan=1 colspan=1>在国内虚拟计算机设施上开发元计算软件</td></tr></table>

# $\yen 2.3.2$ Berkeley的 NOW计划

NOW(Network of Workstation)是美国加州大学Berkeley分校所开发,是一个颇有影响的计划,采用了很多先进技术,涉及到工作站机群很多共同问题，而且具有很多优异的特性： $\textcircled{1}$ 采用商用千兆网络和主动消息通信协议支持有效的通信； $\textcircled{2}$ 通过用户级整个机群软件GLUnix提供单一系统映像、资源管理和可用性； $\textcircled{3}$ 开发了一种新的无服务器网络文件系统xFS以支持可扩放性和单一文件层次的高可用性; $\textcircled{4}$ 最近NOW的开发者们正在开发一个软件框架Webos以构筑高可用性、渐增可扩放的地理 $\mathbf { W } \mathbf { e b }$ 服务器。

主动消息主动消息(Active Message)是实现低开销通信的一种异步通信机制。其基本想法是在消息头部控制信息中携带一个用户级子例程(称作消息处理程序)的地址。当信息头到达目的节点时，调用消息处理程序从网络上抽取剩下的数据，并把它集成到正在进行的计算中。主动消息相当高效和灵活，以至于各种系统中都逐渐地以它为基本的通信机制。但在主动消息下，程序应是以SPMD方式设计的,因为允许发送者指定消息处理程序在接收方的地址，所以必须让所有的节点上有一致的代码映像。

在普通主动消息中提供了如图2.18所示的一组基本函数(原语)和实用函数。当发送请求消息W时，调用如下请求函数：

am- request-2(Destination,request- handler, $x , y )$ ；

其中请求消息W由 request-handler、两个整数 $_ { x }$ 和 $_ { y }$ 、隐含的请求进程的虚拟节点号组成。请求原语am-request- $\mathbf { M } ( \cdots )$ 有5个版本( $\pmb { M } = \pmb { 0 } \sim 4 )$ ，每个均有 $M$ 个整数变量。该请求发送W至Destination(目的)进程。am-request是阻塞式的,即直到W被发出才返回。当W到达时,Destination进程调用request_han-dler子例程进行处理。

# 基本函数：

int am-request_M(vnn-t dest,request_ handler,int arg0,.,int arg(M-1))   
int am-reply_M(vnn-t dest,reply-handler,int argO,.,int arg(M-1))   
int am-get(vnn-t source,void " Iva,void\* rva,int nbytes, handler-t request_handler,void\* handler-arg)   
int am-store(vnn-t dest,void\*rva,void"lva,int nbytes, handler-t reply-handler,void\* handler-arg)   
void am-poll( void)

实用函数：

int am- enable(.…) //initializes the active message layer// int am-disable(void)//exits the active message layer// int am- procs(void) //returns the total number of processes of program// int am-my- proc(void) //returns the caling process's virtual node number// int am-max- size(void)//returns the max.No.of bytes for a get/store//

类似地,当发送应答消息W时，调用如下的应答函数：

am-reply-2(Destination,reply-handler, $x , y )$ ；

其中应答消息W由 reply_handler、两个整数 $_ { \pmb { x } }$ 和 $\pmb { y }$ 、隐含的应答进程的虚拟节点号组成。应答原语am-reply-M(…)有5个版本(M=0～4),每个均有M个整数变量。该应答发送W至目的进程。am-reply是阻塞式的,即直到W被发出才返回。当W到达时，目的进程调用reply-handler子例程进行处理。

am-store和am-get两个函数是用来在两个进程间传送大块数据。其中，am-store函数定义如下：

am- store(Dest,lva, rva, $\mathbf { N }$ ,request_handler,handler-arg);它将请求进程中从地址lva开始的连续 $N$ 个字节传至目的进程中从地址rva开始的存储区中。当收完所有 $N$ 个字节后,目的进程(Dest)调用request-handler,并传给它下述参数:请求进程的 VNN(Virtual Node Number）、rva、N和 handler-arg。类似地,am-get函数定义如下：

am- get(source,rva,lva, $\mathbf { N }$ ,reply_handler,handler-arg);

它将应答进程中从地址rva开始连续的 $N$ 个字节取至源进程中从地址lva开始的存储区中。当收完所有 $N$ 个字节后,调用者调用reply-handler并传给它下述参数：源进程的VNN、lva、N和handler-arg。

主动消息是个一般通用的通信机制,与具体硬件和软件平台无关，它已经在MPP、COW甚至PVM上予以实现,并取得了低延迟、高带宽优良性能,之所以如此是因为： $\textcircled{1}$ 用户级底层功能：主动消息通信常可完全在用户空间实现,可消除上下文切换等所造成的开销,没有必要施行系统调用，用户可直接访问网络接口硬件,消息处理程序也就是普通的用户级子例程; $\textcircled{2}$ 简捷：普通主动消息只有5条原语,每个只具有非常简单的功能和协议,且没有像TCP协议中的缓冲管理或误差检测等额外开销； $\textcircled{3}$ 计算和通信重叠：一般的消息传递型软件(如 PVM和MPI)可通过非阻塞发送/接收操作支持计算和通信的重叠,但在发送和接收双方均要有消息缓冲。主动消息处理长、短消息是不同的,对于4个或更少字的短数据块,可使用阻塞式am-request进行发送,而对大块数据传输，则可使用am-store或am-get。在普通主动消息中,提供了非阻塞的am-store以方便通信与计算的重叠。

GLUnix机群需要能支持可用性和单一系统映像的新的操作系统功能，但传统的工作站OS均无此功能,为此需要对其进行扩充,其方法有二：微(内)核法与用户级守护程序和库方法。微核法(例如Mach和WindowsNT)就是将提供所有服务的整体核代之以一些模块，并且绝大多数最基本的服务只是由少量的称之为微核(Microkernel)的小模块提供,其它的服务均在用户模式下提供。这种模块化法便于移植且灵活,但也有一些缺点：①原始的OS模块须重写；②在不同的结构上进行移植仍需付出努力;③微核系统比整体系统开销大(涉及到上下文切换、进程间通信和交叉保护边界等)。用户级守护程序和库方法能够作为用户级服务和库被实现,此法的优点是不要求修改核且易于实现,但同样它也有着和微核一样的额外开销。

NOW使用了GLUnix方法,它代表全局层(GLobalLayer)Unix,是指运行在工作站标准Unix之上的一个软件层,属于自包含软件。其主要的想法是机群操作系统应由低层和高层两层组成：其中低层是执行在核模式下的节点商用操作系统；高层是能提供机群所需的一些新功能的用户级操作系统。特别是，新全局层能提供机群内节点的单一系统映像，使得所有的处理器、存储器、网络容量和磁盘带宽均能被分配给串行和并行应用，并且它能够作为被保护的、用户级操作系统库予以实现。GLUnix方法能使很多机群性质在用户级实现，其优点是： $\textcircled{1}$ 易于实现：GLUnix完全在用户级实现,不须修改核(第一个GLUnix原型只用3个月就完成了）； $\textcircled{2}$ 可移植性：因为它只依赖基本系统中很小一组标准性质,所以GLUnix能移植在任何支持进程间通信、进程信令(Signaling)和访问负载信息的操作系统上； $\textcircled{3}$ 有效性：在应用地址空间内，使用过程调用的办法能够调用机群所需的一些新性质,无须跨硬件的保护边界、无须核自陷和上下文切换,在GLUnix中删除了系统调用开销；可以使用共享存储段或进程间通信原语,协调多个节点上的GLUnix的多个副本； $\textcircled{4}$ 鲁棒性：因为GLUnix是在用户级，所以能够使用常规的查错工具对它进行测试，错误可被检测、诊断和删除。总之,GLUnix原型对下述的绝大部分特性都已提供：并行程序的共调度；空间资源的检测、进程的迁移和负载平衡；快速用户级通信；远程调页和可用性支持。

xFS无服务器文件系统将文件服务的功能分布到机群的所有节点上,它和传统的中央文件服务器的对照见图2.19。传统的中央文件服务器执行的主要功能是： $\textcircled{1}$ 中央存储：数据文件和元数据都存储在连向文件服务器的一个或多个稳定磁盘上。一个文件的元数据系由一组文件属性(例如文件类型、文件大小、设备ID、节点号、属主D和文件访问许可等)所组成； $\textcircled{2}$ 中央缓存：为了改进性能，每个客户可以缓存某些局部文件块，而文件服务器缓存其主存中经常使用的文件块；③中央管理：服务器执行所有文件系统管理功能，包括元数据和高速缓存一致性管理。在xFS中,所有的服务器和客户的功能由分散的所有节点实现之。xFS仅有的限制是，作为管理器也必须是个客户,因为管理器使用了客户接口。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/dfc58e3ae9565d4011bf334c12a88a710af9629b15170f38e5c9d99272b2443f.jpg)  
图2.19两类文件系统对照

(a）中央文件服务器系统；（b)xFS无服务器网络文件系统

$\textcircled{1}$ 廉价冗余磁盘阵列RAID(Redunant Array of Inexpensive Disks):无工作站文件系统能用来生成软件RAID以提供高性能和高可用性。现今,xFS使用单奇偶校验磁盘条(Striping)。一个文件数据块在多个存储服务器节点上按条划分,在另一节点上有奇偶校验块。如果一个节点失效,失效磁盘的内容,可利用其余盘和奇偶盘之异或操作重建之。RAID的缺点是所谓“小-写问题”(Small-Write Problem)：即如果一次写所修改的仅是条的一部分而不是整个条，则系统必须重新计算奇偶校验而导致大的开销。xFS使用登录条(Log-based striping)的方法解决此问题：每个客户首先将写接合到各用户的登录(Log)上(它就是记录所有写操作的一个存储缓存器);然后此登录采用登录段(Logsegment)提交给磁盘,每个段系由K-1登录片(LogFragment)组成,它与奇偶校验片一道送向K个存储服务器。但此法对大型多服务器机群也有问题：很多发往存储服务器的小片可能使登录存储器很大；很多客户同时写登录会造成竞争。xFS采用将存储服务器分成一些称之为条组(StripeGroup)的子集的办法来解决此问题。如图2.20所示,8个服务器分成2组，每组4个服务器。其中，A条组中，第一段由片1,2,3组成,相应的奇偶校验片为p;第二段由片4,5,6组成，相应的奇偶校验片q。B条组中情况类似。这样客户1和客户2可同时分别向各自组写人登录而不会冲突。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/a93721b4912b0f3de4c77c6dd8792664971ec1f66cb5ef91f9742c4c1d61124e.jpg)  
图2.20 $\tt { x F S }$ 中的条组方法

②协同文件缓存(Cooperalive File（aching)：协同文件缓存的思想很简单：机群每个客户节点都辟出--部分作为文件(高速)缓存。协同文件缓存算法利用所有这些存储器生成一个大的、全机群上的文件缓存。当一个客户未找到其本地文件缓存时，不需要到磁盘中去找，只要到另个客户的存储器中去找该数据。如图2.21所示，文件稳定地存在服务器磁盘中，习惯上这些文件也缓存至客户存储器中、客户本地磁盘中和服务器的存储器中。xFS也允许一个文件缓存在远地存储器中。有两种协同文件缓存算法：贪心转发法(Greedy Forward-ing)和N-概率转发法(N-Chance Forwarding)。贪心转发法工作原理是：一个访问文件和客户首先试用其本地高速缓存,如果数据块不在那里，它便将请求转发给服务器。服务器先搜索其本地高速缓存，若命中，便将数据返给客户并维护其高速缓存目录;若未找到，服务器便查阅其高速缓存目录并把请求转发给保存所请求数据的客户，然后该客户便直接将数据返回给请求的客户。贪心转发法的优点是实现简单,但其缺点是同一数据块可能被很多高速缓存所复制。当一客户第一次读一个数据块时,此块从服务器磁盘中读出并将其缓存在服务器高速缓存和客户高速缓存中，而另一读同一块的客户将把它缓存在其本地文件高速缓存中。这种重复降低了协同高速缓存的有效空间，因而也增加了命不中的比率,而且使高速缓存一致性管理更加困难。N-概率转发法是贪心转发法的一般化,它采用缓存一个数据块仅于一个客户高速缓存中的办法避免重复。这样的数据块叫作单块(Singlet)。当一个客户从另一客户的高速缓存中取出一块时，此块就被丢掉，并发一条消息给服务器告诉它此块已被移去。单块所带来的问题是，如果一个单块被丢掉，它就给后来的数据块腾出了位置，此单块也就从整个协同高速缓存中丢失。N-概率转发法可缓解此问题，只要客户高速缓存未满，它和贪心转发法完全一样。当任一客户的本地高速缓存满时，就要丢掉一个数据块，此时客户首先要检查一下此块是否为单块：如不是，客户就丢掉它；如是,客户就将块循环计数器置为N，并发送该块给一个随机的客户。如果第二个客户稍后要丢掉这一块,它就将循环计数器减一，并发送该块给另一客户。此过程一直继续到循环计数器为零,这时就把该块丢掉。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/d1ed05bfd0734bc463270d83ff5df253f667e7ec96d6bd6e4875767f4468df93.jpg)  
图2.21客户/服务器机群中缓存文件的不同方式

③分布式管理：xFS的文件系统管理功能是全分布的，它使用了位于多个节点上的多管理器(Manager)。为了理解如何达到分布管理,参照图2.22来看一下 xFS中一个文件的读过程：当一个客户试图读一个文件块时，它发送一个带有文件(路径)名和位移(Name& Offset)的请求,在xFS的目录(Dir)中使用文件名客户就能找到文件的索引(Index),用此索引客户搜索本地高速缓存（U-nix Cache),如果数据块在其中(命中),则数据就被读出;如果高速缓存未命中，那么客户用索引号查阅管理器映射表(ManagerMap)，此表指明哪个物理节点管理哪组索引号，也就是正确的管理者在哪里，于是索引和位移信息就经网络发正确的管理者，管理者留意诸如数据块是否在磁盘中或被缓存、块的精确位置、高速缓存块是否是一致的某信息。如果块被缓存在某一客户的本地高速缓存中且是一致的,那么管理者就转发读请求给那个客户,客户就从其本地高速缓存中读取数据并直接发给原先的客户；如果数据块不在协同高速缓存中，管理者就再查阅imap表以找到索引节点(inode),它包含了文件所有数据块的地址，此地址就可用来找到正确的存储服务器，于是数据块就可从那里读出并传给原先请求的客户。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/d8a6b5d6bbe2fa8bc4afd7d42feb2bd78e47447cb2ce92fe9f717412e7f4aa0c.jpg)  
图2.22xFS中一个简化文件的访问过程

一个xFS的原型已在32个节点的机群上实现，它展示了良好的可扩放性，其读带宽已达13.8 MB/s,而写带宽已达13.9 MB/s。

# 2.4国产曙光系列并行机系统

我国的高性能计算机的发展起步并不晚：早在20世纪60年代后期到70年代,我国就自行研制了大型计算机（MainframeComputer),其典型代表机器有150、905、718和 DJS260 等,它们采用单/双 CPU,其峰值速度约为1MOPS（Million Operations Per Second），即俗称的百万次机器;20世纪70 年代后期到80 年代,我国研制了向量机和多处理机,其典型代表机器有757、银河1/2号等，它们采用 $1 \sim 4$ 个CPU,其峰值速度达 $1 0 ^ { \mathrm { - } } 1 0 0 \ \mathrm { M O P S }$ ,即俗称的亿次机器；20世纪80年代后期到现在，我国研制了对称多处理机（SMP）、大规模并行机(MPP)和工作站机群(COW),其典型代表机器有曙光1号、曙光-1000/1000A、

YH-3和曙光-2000等,它们采用 $4 \sim 1 2 8$ 个 CPU,其峰值速度达1Gflops～几十Gflops,即俗称的百亿次机器，我国1999年将正式推出千亿次高性能计算机。表2.10列出了我国20世纪90年代自行研制的有代表性的几种并行机,虽不全面,但足以“管中窥豹,可见一斑”。

表2.1020世纪90年代我国自行研制的几种并行机一览表  

<table><tr><td rowspan=1 colspan=1>机器型号</td><td rowspan=1 colspan=1>完成年代</td><td rowspan=1 colspan=1>研制单位</td><td rowspan=1 colspan=1>CPU芯片</td><td rowspan=1 colspan=1>CPU数</td><td rowspan=1 colspan=1>峰值速度(Gflops)</td></tr><tr><td rowspan=1 colspan=1>BJ-02</td><td rowspan=1 colspan=1>1991</td><td rowspan=1 colspan=1>中科院计算所</td><td rowspan=1 colspan=1>TransputerT800</td><td rowspan=1 colspan=1>17</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Dawning-1</td><td rowspan=1 colspan=1>1993</td><td rowspan=1 colspan=1>国家智能机中心</td><td rowspan=1 colspan=1>M88000</td><td rowspan=1 colspan=1>4~16</td><td rowspan=1 colspan=1>0.03~0.1</td></tr><tr><td rowspan=1 colspan=1>BJ-1</td><td rowspan=1 colspan=1>1994</td><td rowspan=1 colspan=1>中科院计算所</td><td rowspan=1 colspan=1>i860/xp</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Dawning-1000</td><td rowspan=1 colspan=1>1995</td><td rowspan=1 colspan=1>国家智能机中心</td><td rowspan=1 colspan=1>i860/xr</td><td rowspan=1 colspan=1>36</td><td rowspan=1 colspan=1>2.5</td></tr><tr><td rowspan=1 colspan=1>PAR95</td><td rowspan=1 colspan=1>1995</td><td rowspan=1 colspan=1>631研究所</td><td rowspan=1 colspan=1>i860/xr</td><td rowspan=1 colspan=1>40</td><td rowspan=1 colspan=1>3.2</td></tr><tr><td rowspan=1 colspan=1>990-STAR</td><td rowspan=1 colspan=1>1996</td><td rowspan=1 colspan=1>709研究所</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>16</td><td rowspan=1 colspan=1>1.3</td></tr><tr><td rowspan=1 colspan=1>Dawning-1000A</td><td rowspan=1 colspan=1>1997</td><td rowspan=1 colspan=1>国家智能机中心</td><td rowspan=1 colspan=1>PowerPC</td><td rowspan=1 colspan=1>8~16</td><td rowspan=1 colspan=1>3.2~6.4</td></tr><tr><td rowspan=1 colspan=1>YH-3</td><td rowspan=1 colspan=1>1997</td><td rowspan=1 colspan=1>国防科大</td><td rowspan=1 colspan=1>MIPSR4000</td><td rowspan=1 colspan=1>128</td><td rowspan=1 colspan=1>13</td></tr><tr><td rowspan=1 colspan=1>Dawning-2000-I</td><td rowspan=1 colspan=1>1998</td><td rowspan=1 colspan=1>国家智能机中心</td><td rowspan=1 colspan=1>Power604e</td><td rowspan=1 colspan=1>32</td><td rowspan=1 colspan=1>20.0</td></tr></table>

# 2.4.1全对称共事存储多处理机系统：曙光1号

曙光1号是一台全对称紧耦合共享存储的多处理机系统，支持中细粒度并行计算,实现多线程技术,采用RISC和标准总线连接方法，系统配置灵活。采用SNIX(Symmetric UNIX)操作系统并在其上提供大量的 Unix实用程序、编程环境、用户图形介面,以支持人工智能、科学计算和信息处理系统的开发和应用，从而具有市场竞争能力。

硬件系统曙光1号的基本系统是图2.23所示的系统板。在一块系统板内通过100 MB/s带宽的高速局部总线实现了4个CPU、8个CMMU(CacheMemory Management Unit)共享 $6 4 ~ \mathrm { M B }$ 的内存以及与I/O总线、VME 总线、BIT总线的通信。曙光1号系统板,通过符合VME总线标准的底板上的9个插槽,可以配置1～4块模块系统板、1～2块存储扩展板和其它的I/O功能板而构成更大的曙光1号系统(图2.24)。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/bb0f3d2bdbbabdaa955daad9ef0f4e56331c61ddca0029f66be84b36f13cda32.jpg)  
图2.23曙光1号系统板

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/bb3c0d269ea1debde76731814b5039a26088d0602ef6009db56c5ad0927cd6d5.jpg)  
图2.24曙光1号系统

曙光1号硬件特性可汇总如下：

$\textcircled{1}$ 处理器：

·MC88100芯片， $4 \sim 1 6$ 个；主频 $2 5 ~ \mathrm { M H z }$ ；字长32位；指令系统共51条指令；4个CPU整数运算速度168VAXMIPS、浮点运算速度30 Mflops。

·MIC88200芯片， ${ \tt 8 } \sim 3 2$ 个;每个自带16 KB高速缓存,共 $1 2 8 \sim 5 1 2$ KB的高速缓存。

$\textcircled{2}$ 存储器： $6 4 ~ \mathrm { M B } { \sim } 7 6 8 ~ \mathrm { M B }$ 动态存储器，按字节奇偶校验，存储器分为4个体、4路交叉访问，页式管理。

$\textcircled{3}$ I/O功能：

·I/O总线：两个SCSI接口（单端的和差分的）；一个以太网接口（支持IEEE802.3协议）。  
·BIT总线： $4 \sim 1 6$ 异步通信接口；固化监控程序接口EPROM；日期时钟和系统保护接口NVRAM;中断控制接口等。  
·VME 总线:支持 VME Revision D C.1和 IEEE1014 以及 VEM RevisionD 协议;提供9插槽的VME机箱。

$\textcircled{4}$ 硬磁盘：5.25英寸的 $3 0 0 ~ \mathrm { M B } { \sim } 1 . 0 ~ \mathrm { G B } _ { \odot }$ $\textcircled{5}$ 磁带机：盒式磁带机320 Mb(600英尺）。$\textcircled{6}$ 任选件：终端服务器 $1 6 \sim 3 2$ 个。

软件系统曙光1号软件构成层次如图2.25所示，其设计目标为： $\textcircled{1}$ 采用国际标准，提供开放式计算环境； $\textcircled{2}$ 通过并行化操作系统核心及核心之上的各种实用程序，提高系统的响应及任务吞吐能力； $\textcircled{3}$ 通过增加各种并行机制，支持中细粒度的并行计算； $\textcircled{4}$ 在系统软件的各个层次上提供灵活的界面，支持不同用户的需求。图2.26以圆形方式对图2.25进行了说明，现从内到外对各层略作说明如下： $\textcircled{1}$ 监控器作为系统加电后首先运行的软件，其主要功能是硬件配置的设置、硬件测试及引导 Sysboot等，它被固化到512KBEPROM只读存储器中；Sysboot完成SNIX核心加载的主要工作，将根文件系统中的OS核心代码读人到DRAM的首地址，并控制所有处理器同时跳转到核心正文段起始地址执行，还对I/O设备做预处理操作等。 $\textcircled{2}$ 系统库函数包括标准Unix库函数与 SNIX扩展的库函数；前者包括C语言标准库函数Libc.a、数学运算库函数Libm.a、操作COFF文件格式库函数Libld.a和字符终端处理库函数Libcurses.a等；后者包括提供Pthreads并行线程函数以及实现虚处理器的低层库函数。 $\textcircled{3}$ SNIX核心是整个曙光1号软件运行的基础。核心之上的软件可视为多机硬件功能的扩展。从硬件角度看，SNIX核心又是一个多机资源管理与分配器；从核心构成看，它除保留单机Unix的基本成分外，还增加了处理器管理与处理器通信模块;从程序设计考虑,SNIX核心向用户程序提供一个真正的并行运行环境。在文件系统方面,SNIX核心对Unix System V进行了较多的功能扩展,同时支持系统V文件系统与BSD快速文件系统,并在两者之上实现了镜像文件系统与虚文件系统：镜像文件系统可将用户数据在多个磁盘上重复存放，以便当一个磁盘上的数据丢失时可从另一磁盘上恢复；虚文件系统删去了传统Unix 对用户数据文件大小的限制，以支持大规模的数据库处理系统。④SNIX保留了所有Unix实用程序：包括 Shell程序(sh、csh、ksh等）、编辑工具(vi、edit、view、cd 等）、网络实用程序(rlogin、telnet、ftp、mail 等）和一般工具(ls、rm、who、cp、cat等)；编译器(yacc、lex、cpp、cc、cflow、dis、lint 等）和调试程序(adb、sdb、ctrace、strip等);用户管理、文件管理、性能管理、打印机管理等。SNIX并行化的实用程序包括 make、fgrep、apply、find、fsck 等。③SNIX提供了较丰富的高级语言编译系统；曙光1号并行程序设计语言使用C+并行库函数(Pthreads）、并行For-tran 与并行 Ada,其中并行 Fortran 还提供了一个串行的 Fortran 程序并行识别器；曙光1号还提供了专门的并行程序Debugger。 $\textcircled{6}$ 曙光1号通过标准的以太网(TCP/IP)与其它计算机相连;SNIX提供的网络实用程序包括rlogin、telnet、call、rcp、mail等;用户还可通过电话线采用uucp访问曙光1号;曙光1号还通过网络文件系统NFS与不同的异种机相连，实现共享网络节点机的软硬件资源；使用 Socket还可进行分布式程序设计。 $\textcircled{7}$ 曙光1号提供MIT开发的窗口系统X Window和图形用户界面Motif。 $\textcircled{8}$ 曙光1号提供 Oracle、Ingres 和Postgres 数据库管理系统。 $\textcircled{9}$ 曙光1号提供了分布式程序设计环境Express,它将支持由2个或4个曙光1号系统板通过以太网或VME 总线构成的分布式系统,向用户提供一个同时使用8个或16个 MC88100 处理器进行计算的虚拟计算机;Ex-press 支持 SIMD与MIMD并行程序设计模型。 $\textcircled{10}$ 曙光1号支持的智能应用程序开发环境包括基于规则的推理机、面向对象推理机、框架管理系统、知识库管理系统和意见综合系统等;还提供“知识级的问题求解建模环境KMEPS”、“对象函数型人工智能语言系统”“面向对象的地图数据库系统MDB"和点方法几何定理证明软件系统等。

<table><tr><td rowspan=1 colspan=3>智能应用开发环境</td></tr><tr><td rowspan=1 colspan=3>分布式程序设计环境</td></tr><tr><td rowspan=1 colspan=3>数据库管理系统</td></tr><tr><td rowspan=1 colspan=3>XWindow/Motif图形用户界面</td></tr><tr><td rowspan=1 colspan=3>网络通信软件</td></tr><tr><td rowspan=1 colspan=3>程序设计语言开发环境</td></tr><tr><td rowspan=1 colspan=3>操作系统实用程序</td></tr><tr><td rowspan=1 colspan=3>操作系统SNIX核心界面库函数</td></tr><tr><td rowspan=1 colspan=1>监控器</td><td rowspan=1 colspan=1>OS引导程序Sysboot</td><td rowspan=1 colspan=1>SNIX核心</td></tr><tr><td rowspan=1 colspan=3>曙光1号硬件系统</td></tr></table>

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/a26853c5c11cdb5cb7b5cf3d998df25914b59782907e6ea504150c862cff5e29.jpg)  
图2.26曙光1号软件层次的圆形表示

# 2.4.2大规模并行处理系统：曙光-1000

曙光-1000 是一台分布存储的大规模并行处理·MPP(Massively Parallel Pro-cesing)系统,它突破了MPP中一些技术关键,采用20世纪90年代大量先进技术,其峰值速度达25亿次,可广泛应用于科学工程计算、气象预报、石油勘探、地震数据处理和银行等商务处理中。其技术特点是： $\textcircled{1}$ 良好的可扩放性,包括硬件和软件两个方面； $\textcircled{2}$ 大量的节点、强大的计算能力和大容量存储器; $\textcircled{3}$ 自行设计的稳定可靠的虫蚀通信芯片； $\textcircled{4}$ 使用带流控的消息传递协议； $\textcircled{5}$ 优良的优化并行编译器； $\textcircled{6}$ 先进的并行编程环境、并行查错工具、自动并行化工具和包括 PVM、MPI、Express、NX 等的编程工具。曙光-1000 整体性能达到 20 世纪90 年代初期世界先进水平,其主要技术指标是： $\textcircled{1}$ 使用 $6 \times 6$ 的二维网孔连接,共36个节点,其中计算节点32个，服务节点2个和I/O节点2个； $\textcircled{2}$ 峰值速度达单精度2.56 Gflops,双精度1.92 Gflops,实际速度为1.58 Gflops; $\textcircled{3}$ 存储容量为每个节点32MB,共1GB;④硬盘容量可超过5GB;③二维网孔连接、虫蚀选路，总通信容量为4.8GB/s;⑥计算节点和通信网络间带宽为2.8GB/s;?支持并行C、C++和Fortran,提供并行优化重构工具Port和自动并行化工具Autpar、动态监视和分析工具ParaVision以及单计算节点上源代码与目标代码的优化工具；③基于Unix的分布式并行操作系统;③提供并行程序查错环境NDB;①提供并行程序设计和运行环境 PVM、MPI、Express、NX 和 $\mathrm { P } _ { 4 }$ 等。

硬件系统曙光-1000是一台分布存储、消息传递的MPP系统,如图2.27所示，在6×6二维网孔的每个格点上有一个虫蚀路由芯片WRC（WormholeRouting Chip)和一个计算节点(或服务节点或I/O节点),系统监视器(Monitor)负责系统初始化和硬件故障诊断,用户工作平台可以是工作站 SUN Sparc-Ⅱ(或其它工作站)也可以是终端(它们都称为前端机),它们通过 $1 0 \ \mathrm { M b / s }$ 的以太网连向服务节点。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/5a533eb3ea6eb2fcd23fca8a8899ebf6ad900db2fae9e9e890c2ab149f12698c.jpg)  
图2.27曙光-1000系统框图

$\textcircled{1}$ 二维网孔和WRC：二维网孔是一种可扩展的互连网络。格点上的计算节点(或服务节点或I/O节点)都连向WRC。节点编号(物理地址)由X方向编号和Y方向编号两部分组成,节点间相对地址包含在消息中。一个WRC有10条输人/输出通道,每个通道包含8条数据线。一条指明消息结束的尾信号线、一条发送请求线REQ和一条应答线ACK。当一条消息自源发往目的时,它只穿过途中的WRC,并不进入与WRC相连的节点处理器。消息选路采用X-Y选路算法(见8.1.1节算法8.1)。

$\textcircled{2}$ 计算节点：它是一块插人板,其核心是一个 $\mathbf { i } 8 6 0 \mathbf { x } \mathbf { r }$ 芯片,其主频为 40$\mathbf { M H z }$ ,字长64位,单精度浮点运算速度为80 Mflops、双精度为60Mflops,标量计算速度为40 MIPS;它有带奇偶校验的32MBDRAM、8KB EPROM和2 KBNVRAM;节点与网孔的接口模块包含16KBFIFO,网孔与各节点间的通信带宽为 $3 3 \mathrm { \ M B / s }$ ,消息具有CRC校验,RS-232接口直接连向监视器上的多用户卡,以便监视器能监视与诊断所有的节点处理器。在所有的计算节点上运行OS与用户程序。

③服务节点：服务节点用于管理系统资源,它是一台50MHz的具有EISA总线的486PC机。EISA总线与网孔网络之间有一接口模块 EMI,在EMI卡上有DMA机制;在数据通路FIFO-网孔-FIFO上使用CRC校验;EMI卡和网孔之间的通信速度是16MB/s。如有较多的用户和图形显示设备，则可使用2个服务节点，两者可使用共享系统资源表的方法协同工作。

$\textcircled{4}$ I/O节点：和服务节点一样,I/O节点也是一台带有EISA总线、具有EMI插卡的486PC机。一个I/O节点使用插在EISA总线上的 SCSI卡可接人4GB硬盘。系统可提供一个或两个I/O节点，当用户要求大的I/O吞吐率时可使用更多的I/O节点，但计算节点则须相应减少。I/O节点和网孔之间的数据传输速度为16MB/s。每个I/O节点上运行并行文件系统,执行并行文件操作。

$\textcircled{5}$ 系统控制台：也就是监视器，它运行SCOUNIX,其中有一块多用户卡，连向32个RS-232串行口。控制台与计算节点可执行点到点通信，也可向所有计算节点同时播送消息。其主要功能是初始化系统、监视计算节点上操作系统和用户程序的运行、动态地查看节点处理器资源组态表和诊断失效的计算节点。

$\textcircled{6}$ 前端机：曙光-1000 用户工作平台是 SUN Sparc-Ⅱ或 SGI图形工作站或终端,所有这些设备均经由LAN(如以太网)连向系统服务节点。LAN遵从TCP/IP协议,其速率为10 Mb/s。事实上,网孔系统可视为前端系统的计算服务器，在前端机上用户程序被编辑、编译(使用C和Fortran77i860交叉编译器）、链接和查错，当编译成功后，应用程序的目标代码通过以太网传到服务节点；然后由服务节点发往计算节点;最终的计算结果由前端机显示输出。

系统软件曙光-1000系统软件包括操作系统、并行优化编译及工具和并行编程环境及并行查错工具等。

$\textcircled{1}$ 操作系统：曙光-1000的操作系统是基于Unix的分布式操作系统。在计算节点上运行微核操作系统,支持虚拟存储管理、自陷处理、作业管理和消息传递；在服务节点上运行基于Mach2.6操作系统，支持多线程，其主要功能是系统管理，特别是节点处理器的分配与去分配;在I/O节点上运行并行文件服务器PFS。服务节点和I/O节点与计算节点具有相同的消息传递接口。系统执行带有流控的消息传递协议。

$\textcircled{2}$ 并行优化编译和工具：节点程序编译优化包括源码级优化和目标码级优化,前者使用循环(Loop)交换、循环合并和循环分离的办法开拓并行性；后者采用充分利用流水线、双指令模式和双操作指令(由i860 所提供的)和浮点加载指令以向量化循环的方式开拓并行性。Autopar是自行开发的自动并行化工具,它能识别并行循环、执行数据划分和产生并行的Fortran 源代码。Paravision 是曙光-1000 并行程序的可视化工具,它能够移植到其它MPP系统上，用户使用它能观察程序动态运行过程,包括消息传递条件、负载平衡情况和是否出现死锁等。

$\textcircled{3}$ 并行编程环境和并行查错工具：为了便利用户编程和运行并行程序，曙光-1000 移植了4种成熟的界面环境,即 NX、Express、PVM和 MPI。其中 NX原是Paragon 系统上的用户并行编程界面,而 Express、PVM和 MPI均是世界上广泛使用的并行编程和运行环境。并行程序查错器包括源代码查错程序 NDB和汇编代码查错程序ADB,它们的主要功能是显示、设置和取消指令断点、读/写存储器、逐步或连续运行程序或发送和接收现行进程状态。它们能够查错运行在多个节点上的程序。

表2.11列出了曙光-1000与某些著名MPP系统的性能比较，性能指标是利用求解标准线性方程组测得的，其中 $\mathbf { R } \left( \mathbf { m a x } \right)$ 是机器能够达到的最高速度，$\mathrm { N } ( \mathrm { m a x } )$ 是速度达到 $\mathbf { R } ( \mathbf { m a x } )$ 时线性方程组的阶， $\mathrm { N } \left( { \frac { 1 } { 2 } } \right)$ 是速度达到 $\frac { 1 } { 2 } \mathrm { R } ( \operatorname* { m a x } )$ 时线性方程组的阶。

表2.11 曙光-1000与某些著名MPP系统性能比较一览表  

<table><tr><td rowspan=1 colspan=1>机器名称</td><td rowspan=1 colspan=1>计算节点数目</td><td rowspan=1 colspan=1>R(max)Gflops</td><td rowspan=1 colspan=1>N(max)阶数</td><td rowspan=1 colspan=1>N(1/2)阶数</td></tr><tr><td rowspan=1 colspan=1>曙光-1000</td><td rowspan=1 colspan=1>32</td><td rowspan=1 colspan=1>1. 12</td><td rowspan=1 colspan=1>15 000</td><td rowspan=1 colspan=1>4 000</td></tr><tr><td rowspan=3 colspan=1>Paragon XPS(50MHz)</td><td rowspan=1 colspan=1>256</td><td rowspan=1 colspan=1>7.6</td><td rowspan=1 colspan=1>16 000</td><td rowspan=1 colspan=1>4 000</td></tr><tr><td rowspan=1 colspan=1>128</td><td rowspan=1 colspan=1>4.0</td><td rowspan=1 colspan=1>12 000</td><td rowspan=1 colspan=1>3000</td></tr><tr><td rowspan=1 colspan=1>64</td><td rowspan=1 colspan=1>2.0</td><td rowspan=1 colspan=1>8000</td><td rowspan=1 colspan=1>2 000</td></tr><tr><td rowspan=4 colspan=1>Delta（40MHz)</td><td rowspan=1 colspan=1>192</td><td rowspan=1 colspan=1>5.2</td><td rowspan=1 colspan=1>15 000</td><td rowspan=1 colspan=1>4 500</td></tr><tr><td rowspan=1 colspan=1>128</td><td rowspan=1 colspan=1>3.5</td><td rowspan=1 colspan=1>12 500</td><td rowspan=1 colspan=1>3 500</td></tr><tr><td rowspan=1 colspan=1>64</td><td rowspan=1 colspan=1>1.7.</td><td rowspan=1 colspan=1>8 000</td><td rowspan=1 colspan=1>2 500</td></tr><tr><td rowspan=1 colspan=1>32</td><td rowspan=1 colspan=1>0.9</td><td rowspan=1 colspan=1>6000</td><td rowspan=1 colspan=1>2 000</td></tr><tr><td rowspan=2 colspan=1>IBMSP2</td><td rowspan=1 colspan=1>32</td><td rowspan=1 colspan=1>6.1</td><td rowspan=1 colspan=1>19 000</td><td rowspan=1 colspan=1>4 088</td></tr><tr><td rowspan=1 colspan=1>16</td><td rowspan=1 colspan=1>3.0</td><td rowspan=1 colspan=1>13 500</td><td rowspan=1 colspan=1>1</td></tr><tr><td rowspan=2 colspan=1>CM-5</td><td rowspan=1 colspan=1>128</td><td rowspan=1 colspan=1>7.7</td><td rowspan=1 colspan=1>18 432</td><td rowspan=1 colspan=1>8 192</td></tr><tr><td rowspan=1 colspan=1>64</td><td rowspan=1 colspan=1>3.8</td><td rowspan=1 colspan=1>13 056</td><td rowspan=1 colspan=1>6016</td></tr><tr><td rowspan=1 colspan=1>Cray T3D32</td><td rowspan=1 colspan=1>32</td><td rowspan=1 colspan=1>3.2</td><td rowspan=1 colspan=1>14 592</td><td rowspan=1 colspan=1>1 616</td></tr><tr><td rowspan=1 colspan=1> SGI Challenge</td><td rowspan=1 colspan=1>36</td><td rowspan=1 colspan=1>1.28</td><td rowspan=1 colspan=1>8000</td><td rowspan=1 colspan=1>2 000</td></tr><tr><td rowspan=1 colspan=1>Ncube-2</td><td rowspan=1 colspan=1>256</td><td rowspan=1 colspan=1>0.482</td><td rowspan=1 colspan=1>10 784</td><td rowspan=1 colspan=1>1 504</td></tr><tr><td rowspan=1 colspan=1>Maspar MP-1 266</td><td rowspan=1 colspan=1>16 384</td><td rowspan=1 colspan=1>0.47</td><td rowspan=1 colspan=1>11 264</td><td rowspan=1 colspan=1>1280</td></tr></table>

# $\times 2 . 4 . 3$ 超级并行计算机系统：曙光-2000

曙光天潮系列"曙光-2000"是基于分布存储和消息传递体系结构的通用可扩放并行计算机系统，其节点数为 $4 \sim 1 2 8$ 个，节点CPU采用先进的PowerPC604e微处理器,通过高速以太网和虫蚀路由芯片组成的二维网孔互连。每个节点上运行完整的IBMAIX操作系统,系统与IBMRS/6000二进制兼容。可广泛应用于科技计算和商业计算的多种领域中。

设计准则为了将曙光-2000设计成一种通用、灵活的可扩放并行机系统，设计者们在广泛分析和深入理解当前硬件、软件技术发展趋势，不同应用领域的需求和用户环境要求的基础上,遵循了一系列设计准则： $\textcircled{1}$ 一个高性能的可扩放并行系统必须采用标准的微处理器、软件构件(Component)和操作系统，只应在标准技术无法满足可扩放并行系统某些特殊要求(如通信延迟)时，才采用定制的硬件和软件； $\textcircled{2}$ 采用最新的技术，保证性能价格比的领先优势。为此必须尽可能少地依赖于技术供应商,低层的体系结构必须足够灵活,在OS级上对各节点采用松散耦合方式； $\textcircled{3}$ 对低延迟和高带宽的要求使得在今后几年内可扩放并行计算机系统仍然依赖于定制的内部网络和通信子系统； $\textcircled{4}$ 系统的编程和执行环境应与标准的、开放的、分布式Unix环境一致； $\textcircled{5}$ 系统应当有选择地在下列领域提供高性能服务：通信系统、高性能文件系统、并行库、并行数据库、高速I/O,以利于高效地进行超级计算、并行查询和高性能事务处理; $\textcircled{6}$ 消除造成系统崩溃的单一故障点和从失效中快速恢复，可获得系统高可用性。为此必须有足够的硬件和软件备份(Replication),同时提供支持可用性的基础软件(故障检测、诊断、系统重配置和恢复等)； $\textcircled{7}$ 对于单一系统映像进行有选择地支持，只进行重要资源(如文件、目录服务)和命令的全局化以及提供对系统管理的单点控制。

体系结构曙光-2000体系结构如图2.28所示。曙光-2000系统可由${ \pmb 4 } \sim { \pmb 1 } 2 { \pmb 8 }$ 个处理节点组成。每个节点包括可靠的高效的RISC微处理器 Power-PC,运行完整的IBMAIX操作系统。诸节点由高速以太网和二维网孔互连；通信网卡通过PCI总线与节点相连,外围子系统通过I/O接口与节点相连；系统管理员通过控制台管理系统;用户工作站或终端通过外部以太网访问节点。曙光-2000系统的节点可分为计算节点和I/O与登录服务节点：前者用于执行用户提交的任务;后者用于支持用户作业在计算节点上的运行。

$\textcircled{1}$ 节点处理器：PowerPC微处理器采用超标量技术（即每个周期同时执行多条指令)和很多复杂结构技术来获得高性能。它拥有6个处理单元(浮点单元FPU、转移处理单元BPU、存/取单元LSU、2个单周期整数单元 SCIU和多周期整数单元MCIU),可同时执行4条指令， $3 0 0 ~ \mathrm { M F l z }$ 主频的处理器可达到每秒6亿次浮点运算。每个处理器的一级高速缓存容量为 $3 2 \mathrm { \ K B }$ 数据/32KB指令,二级高速缓存容量为1MB;内存容量为 ${ \bf 1 } 2 8 \mathrm { - } 5 { \bf 1 } 2 { \mathrm { \ m B } }$ ；内置硬盘容量为4.3GB;I/O总线速率为 $1 3 3 \mathrm { \ M B / s } _ { \circ }$

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/78ce665c88cbdba66cd7d4806b04a81f66c0ca2e064d36ad189e21c20043b17c.jpg)  
图2.28曙光-2000体系结构框图

$\textcircled{2}$ 通信子系统：曙光-2000采用二维网孔互连，使用“虫蚀"选路，从而具有可扩放性、低延迟、高带宽、低处理器开销和可靠灵活之特性。在二维网孔中，点与点之间采用基于消息包的固定路由、无缓冲的传输机制，点与点之间的通信带宽保持常数，不依赖于拓扑中两节点的物理位置。WRC芯片有10个通道，如图2.29所示，每个通道16位数据宽度， ${ 5 0 ~ \mathrm { M H z } }$ 频率，数据带宽 $1 0 0 ~ \mathrm { M B / s } _ { \circ }$ 芯片内部有X、Y两个路选择控制器和4级16位数据缓冲器。曙光-2000节点通过一块PCI网络接口板与底板相连,其中PMI-16接口板由PCI的DMA引擎控制数据传输,PMI-960接口板由一个Intel960协处理器负责DMA传输和协议控制。接口板和节点内存之间采用DMA方式传输，减少了消息传递中处理器的开销。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/0f31e45be117c51b1af25ef5b81f211cfb147088d09d7519a79ec2f34f23b77b.jpg)  
图2.29WRC路由芯片结构示意图

软件系统曙光-2000软件逻辑结构如图2.30所示。其中，每个节点均由一个完整的AIX4.2以上操作系统管理,它提供了大量的多用户通信和系统管理技术、编译器等，符合主要的工业标准；在低层它提供了用于消息传递的基本通信库BCL、PVM和MPI;在高层提供集成并行程序设计环境IPPE、并行可视化工具ParaVT、并行调试器 DCDB、KISS(Keep It Simple and Scalable）、基于Web 的用户界面、自动并行化工具AutoPAR、可扩放文件系统COSMOS、批作业管理JOSS、资源管理RMS和曙光服务器聚集软件DSC;此外，曙光-2000系统还提供了一系列广泛的IBMRS/6000 兼容的开放软件工具来支持管理和操作，包括IBM的C和Fortran编译器、数学和工程库ESSL、数据库DB2等。

<table><tr><td rowspan=1 colspan=8>科学与工程计算应用</td><td rowspan=1 colspan=7>网络服务应用</td><td rowspan=1 colspan=5>数据库与事务处理应用</td><td rowspan=1 colspan=1>其它</td></tr><tr><td rowspan=1 colspan=20>应         用          层          软        件</td><td rowspan=2 colspan=1>中间件数据库</td></tr><tr><td rowspan=1 colspan=9>并行算法与数学库图形图像处理算法</td><td rowspan=1 colspan=4>新材料计算</td><td rowspan=1 colspan=4>气象气候计算</td><td rowspan=1 colspan=2>并行DB</td><td rowspan=1 colspan=1>其它</td></tr><tr><td rowspan=1 colspan=1>DSC</td><td rowspan=1 colspan=3>KISS</td><td rowspan=1 colspan=2>IPPE</td><td rowspan=1 colspan=3>AutoPAR</td><td rowspan=1 colspan=2>ParaVT</td><td rowspan=1 colspan=3>HPF</td><td rowspan=1 colspan=2>DCDB</td><td rowspan=1 colspan=4>分布共享存储软件包</td><td rowspan=1 colspan=1>ESSL</td></tr><tr><td rowspan=1 colspan=8>系统管理软件</td><td rowspan=1 colspan=4>上层通信库</td><td rowspan=2 colspan=9>编译器（C,Fortran,JAVA)基本函数库</td></tr><tr><td rowspan=1 colspan=2>资源管理</td><td rowspan=1 colspan=3>作业管理</td><td rowspan=1 colspan=3>机群管理</td><td rowspan=1 colspan=1>PVM</td><td rowspan=1 colspan=1>MPI</td><td rowspan=1 colspan=2>NX</td></tr><tr><td rowspan=1 colspan=21>HA核心和Agent</td></tr><tr><td rowspan=1 colspan=7>BCL通信库</td><td rowspan=1 colspan=14>COSMOS 库和 Daemon</td></tr><tr><td rowspan=1 colspan=21>PMI Driver   DNS,NFS,NIS                                                         文件系统核心扩展AIX操作系统</td></tr><tr><td rowspan=1 colspan=3>Monitor960</td><td></td><td rowspan=1 colspan=4>Monitor960BCL板上固件</td><td rowspan=2 colspan=14>硬                         件</td></tr><tr><td rowspan=1 colspan=7>PMI板</td></tr></table>

$\textcircled{1}$ 并行环境：它由BCL、IPPE、ParaVT和DCDB 组成,用户可用来开发、调试和修改并行Fortran 和C程序，并且可启动、监视和控制程序的运行。其中，BCL支持Fortran和C的显式消息传递模型,提供大量的函数集和子程序以支持进程间点到点通信和用户非阻塞通信，并支持多用户方式用户空间通信；IPPE 提供启动、监视、控制并行应用的用户环境，主要功能包括编译、链接并行代码和通信库,并行任务分区、并行作业加载和监视作业的运行,傻瓜界面KISS提供基于Web的查询和使用界面；ParaVT提供并行应用的性能监视和跟踪可视化,前者在程序运行时实时地显示系统的活动状态；后者用户可设置跟踪点以观察并行进程间的通信情况、识别死锁、负载变化和性能瓶颈等；DCDB是一个源代码级的调试器,支持图形化使用界面,是在Unix串行调试器dbx或gdb 基础上附加了一些专用的并行程序调试功能。

$\textcircled{2}$ 可扩放文件系统：COSMOS可有效解决超级计算应用对单个文件的可扩展高带宽的要求，并能提高网络文件系统吞吐量的可扩放性。它支持对条带化(Stripe)方式分布存储的文件的并行访问;它允许一个并行程序的多个进程对同一文件进行访问;可支持异步的I/O和规模大于2GB的文件;COSMOS支持标准Unix文件系统调用,用户通过UNIXioctl操作可获得其它的功能。由于每个计算节点上运行一个Client Daemon、每个COSMOS 服务节点土运行一个StorageDaemon(或有选择地运行ManagerDaemon),所以这些服务进程相互通信形成了一个可扩放服务器来满足用户请求。

$\textcircled{3}$ 可用性服务：曙光-2000所提供的可用性服务包括系统管理软件中的系统监控和NCIC-HA高可用软件包。目前曙光-2000 系统可用性服务的主要功能包括心跳服务、资源组服务、通知服务和恢复协调服务。其中心跳服务就是监视系统的状态是否正常,包括侦测和交换心跳信息;资源组服务就是定义节点和应用程序、系统资源(如IP)属于一个故障切换资源组,通常该组包括那些相关的应用服务成员；通知服务就是在组的结构和节点状态发生了变化时通知组内成员；恢复服务提供了当组内结构和节点状态发生变化时，当前组中备份节点恢复进程的启动机制,即故障切换(Takeover)。这些服务是由运行在节点上的HA守护进程(Daemon)所实现的。

$\textcircled{4}$ 全局服务：对于曙光-2000来说，一个全面的单一系统映像并不是迫切需要的,它只对特殊资源(包括磁盘、文件和通信网络等)提供单一系统映像。在曙光-2000中,通过网络文件系统NFS来提供对文件的全局访问,全局网络访问是通过网络路由机制和TCP/IP及UDP/IP对互连网络的支持来进行的。在此方式下,可使曙光-2000上的应用以单一的IP地址对外提供服务；曙光-2000 还打算使用虚拟共享磁盘VSD提供对磁盘的全局访问,使用VSD,运行在任何节点上的应用程序可以透明地访问任一其它节点上的磁盘，就像该磁盘是连接在自身节点上一样；另一个全局服务是系统数据储存库 SDR,它提供曙光-2000系统中各节点和控制工作上的数据存储和检索，这包括各个节点和互连网络的配置的全局信息以及系统中资源和作业的信息，这些重要的系统数据不仅要储存在实现这些系统功能的服务节点上,而且也应被保存在这些节点以外的全局储存库SDR上。当重要的系统服务发生故障时，故障节点可以通过查询SDR来重新恢复正常工作,在此期间,对服务的请求只是被延迟,但不会引起其它的故障

发生。

$\textcircled{5}$ 系统管理：曙光-2000的系统管理和监控软件是建立在大量的AIX工作站环境中已有的系统管理工具和命令的界面上的，它使得在多节点上可以运行传统的系统管理命令，这些命令的功能包括系统安装、重启/关机、系统操作、用户管理、安全管理、作业记帐、硬件监控、打印和邮件服务等;曙光-2000的单点控制在系统控制台上进行，它是一台独立的天演系列工作站,与系统中每一机柜相连,用户可从网络的任何一个地方登录到控制台；系统管理软件使用基于SN-MP 协议的客户/服务方式来从控制台启动系统管理命令，基于JAVA的图形化界面用于确定在哪一个节点上进行操作、修改和收集节点应答;硬件监控软件使得系统员可以监控曙光-2000系统的硬件状态。

$\textcircled{6}$ 作业管理：用户可以使用批处理或交互方式使用曙光-2000：在批处理方式中,作业是通过网络作业调度程序提交的;在交互方式中,用户使用Unixrlogin/telnet命令登录到曙光-2000系统上,通过相应的网络地址就可直接访问某个特定的节点。曙光-2000的资源管理器的主控服务运行在控制台上，它将相应的节点分配给并行作业，当并行作业被提交时，用户通过函数或命令向资源管理器申请作业所需的节点，如果有相应数量的可用节点,资源管理器就返回一个可用节点表,这些节点就构成了该并行作业的节点分区;当节点分区确定后，分区管理进程就在分区内的每个节点上加载一份作业的可执行代码,并通知该节点上的守护进程启动代码的执行;当作业完成后,分区管理进程负责清除和终止工作,并交回分区内的所有节点。

# 2.5小结和导读

小结本章讨论了当代三种并行计算机系统 SMP、MPP和COW,它们系统特性的比较可综合于表2.12中。注意,MPP 和COW之间的界线渐趋模糊，例如IBMSP2被视为MPP,但它具有机群结构(除了使用高性能开关网络作为通信网络外)。COW的性能/价格比优于MPP,所以机群技术是发展可扩放并行计算的主流趋势。

导读有关当代三种并行机系统的全面介绍,[103]是一本及时新作,有关Origin 2000的介绍,读者可参阅[117],[155]和[181];有关 SP2的介绍,读者可参阅[14],[169]和[163];有关COW的一般介绍,读者可参阅[200];Berkeley:NOW计划描述在[15]中;Princeton:SHRIMP 描述在[63]中;Karsruhe:Parasta-tion 描述在[180]中;Rice:TreadMarks 描述在[13]中;Wisconsin:Wind Tunnel描述在[144]中;NSCP 计划描述在[42]中;Argonne:Globus 描述在[57]中;Syra-cuse:WWVM描述在[60]中;Virginia:Legion描述在[83]中和香港大学:Pearl-cluster描述在[102]中。曙光-1号报导在[193]中;曙光-1000报导在[129]中和曙光-2000取材于[194]。

表2.12 SMP、MPP、COW性能比较一览表  

<table><tr><td rowspan=1 colspan=1>系统特性</td><td rowspan=1 colspan=1>SMP</td><td rowspan=1 colspan=2>MPP</td><td rowspan=1 colspan=1>COw</td></tr><tr><td rowspan=1 colspan=1>节点数目(N)</td><td rowspan=1 colspan=1>≤0(10)</td><td rowspan=1 colspan=2>0(100)~0(1000)</td><td rowspan=1 colspan=1>≤0(100)</td></tr><tr><td rowspan=1 colspan=1>节点复杂程度</td><td rowspan=1 colspan=1>中/粗粒度</td><td rowspan=1 colspan=2>细/中粒度</td><td rowspan=1 colspan=1>中粒度</td></tr><tr><td rowspan=1 colspan=1>节点间通信</td><td rowspan=1 colspan=1>共享存储</td><td rowspan=1 colspan=2>消息传递/共享存储</td><td rowspan=1 colspan=1>消息传递</td></tr><tr><td rowspan=1 colspan=1>作业调度</td><td rowspan=1 colspan=1>单一运行队列</td><td rowspan=1 colspan=2>主机上单一运行队列</td><td rowspan=1 colspan=1>多队列但协同</td></tr><tr><td rowspan=1 colspan=1>支持单一系统映像</td><td rowspan=1 colspan=1>总是</td><td rowspan=1 colspan=2>部分</td><td rowspan=1 colspan=1>希望</td></tr><tr><td rowspan=1 colspan=1>节点OS副本和类型</td><td rowspan=1 colspan=1>一个（单一）</td><td rowspan=1 colspan=2>N(微核）和1个主机OS（单一）</td><td rowspan=1 colspan=1>N(希望同构)</td></tr><tr><td rowspan=1 colspan=1>地址空间</td><td rowspan=1 colspan=1>单一</td><td rowspan=1 colspan=2>多个</td><td rowspan=1 colspan=1>多个</td></tr><tr><td rowspan=1 colspan=1>所有权</td><td rowspan=1 colspan=1>一个单位</td><td rowspan=1 colspan=2>一个单位</td><td rowspan=1 colspan=1>一个或多个单位</td></tr><tr><td rowspan=1 colspan=1>网络协议</td><td rowspan=1 colspan=1>非标准</td><td rowspan=1 colspan=2>非标准</td><td rowspan=1 colspan=1>标准/非标准</td></tr><tr><td rowspan=1 colspan=1>系统可用性</td><td rowspan=1 colspan=1>常常是低的</td><td rowspan=1 colspan=2>低中</td><td rowspan=1 colspan=1>高或容错</td></tr><tr><td rowspan=1 colspan=1>性能/价格比</td><td rowspan=1 colspan=1>一般</td><td rowspan=1 colspan=2>一般</td><td rowspan=1 colspan=1>高</td></tr><tr><td rowspan=1 colspan=1>处理器类型</td><td rowspan=1 colspan=1>商用</td><td rowspan=1 colspan=2>商用</td><td rowspan=1 colspan=1>商用</td></tr><tr><td rowspan=1 colspan=1>互连网络</td><td rowspan=1 colspan=1>总线/交叉开关</td><td rowspan=1 colspan=2>定制</td><td rowspan=1 colspan=1>商用</td></tr><tr><td rowspan=1 colspan=1>系统存储器</td><td rowspan=1 colspan=1>集中共享</td><td rowspan=1 colspan=2>分布共享</td><td rowspan=1 colspan=1>分布共享</td></tr><tr><td rowspan=1 colspan=1>访存模型</td><td rowspan=1 colspan=1>UMA</td><td rowspan=1 colspan=2>NORMA</td><td rowspan=1 colspan=1>NORMA</td></tr><tr><td rowspan=1 colspan=1>代表机器</td><td rowspan=1 colspan=1>Intel SHV,Sun Fire,DEC8400,IBMR60,SGI Power Challenge曙光1号</td><td rowspan=1 colspan=2>Intel Paragon,IBM SP2Intel/Sandia ASCIOption Red,曙光-1000/2000</td><td rowspan=1 colspan=1>Berkeley NOW,Princeton SHRIMP,Rice Tread Marks,HKU Pearlcluster</td></tr></table>

# 习 题

.2.1对于一个100 MHz时钟频率的总线连接的SMP系统,假定总线宽度为8个字节,为了传输16个字节的数据,那么总线带宽可达多少?

2.2试解释系统带宽与系统互连对剖宽度之间的关系,并举一例说明之。

2.3参照图2.6:

$\textcircled{1}$ 试重画图2.6(e),并补上快速链路;

$\textcircled{2}$ 试重画图2.6(f),并补上略去的节点；  
$\textcircled{3}$ 试画出128个节点(256个处理器)的胖超立方；  
$\textcircled{4}$ 试画出512个节点(1024个处理器)的胖超立方。

2.4下面是NOW中使用主动消息,两个进程施行短消息通信的过程,其中进程Q计算数组A,进程P计算标量 $\pmb { x }$ 最终的结果是 $\mathbf { x }$ 与A[7]之和。试解释远程读取的具体过程。

进程P 进程Q   
compute x compute A ： ：   
am- enable(··); am- enable(·…);   
am-request_1(Q,request_h,7); ：   
am - poll(); am- poll();   
$\mathbf { s u n } { \stackrel { \cdot \cdot } { - } } \mathbf { x } + \mathbf { y }$ ： ： am-disable();   
am-disable(); int request- h( vnn-t P,intk)   
int reply- $\mathtt { h } ( \mathtt { v m n \_ t } , \mathbf { Q } , \mathtt { i n t z } )$ {am-relpy-1(P,reply-h A[k]); $\left\{ \mathbf { y } { } = \mathbf { z } { } \right\}$

2.5根据 $\mathbf { x F S }$ ，试回答：

$\textcircled { 1 } \mathbf { x } \mathbf { F } \mathbf { S }$ 与集中式文件服务器之间的主要区别是什么？$\textcircled{2}$ 为了增强可用性， $\bf { x F S }$ 使用了哪些主要技术？

2.6根据2.2.2节有关 $\mathtt { S P 2 }$ 的介绍,试回答：

$\textcircled { 1 } \mathbf { S } \mathbf { P }$ 设计者为了赶上市场作了什么决策？  
$\textcircled{2} \mathbf { S } \mathbf { P }$ 设计者为了达到系统通用采用了什么相应技术？  
③SP系统是如何支持4种SSI的:单一进人点、单一文件层次、单一控制点和单一作业管理系统？  
$\textcircled{4} \textcircled { \mathbf { S P } }$ 设计者为了增加带宽,在通信子系统中主要使用了什么技术？

2.7试解释 RAID(Redundant Array of Inexpensive Disks)工作原理。

2.8试述曙光-2000 系统的可靠性和可用性特色。

2.9试比较 SMP,SSMP,CC-NUMA 和基于机群的MPP以及DSM在体系结构上的异同点。

# 第三章 并行计算性能评测

并行计算的性能评测与并行计算机体系结构、并行算法和并行程序设计一道构成了“并行计算"研究的四大分支,它们相辅相成的发展着。在并行系统上进行计算的主要目的就是要加速整个计算的过程,所以研究并行系统(并行算法并行程序)的加速比性能是最根本的；随着计算负载的增加和机器规模的扩大，研究计算系统的性能是否能随处理器数目的增加而按比例的增加也是很重要的,这就是所谓的并行计算的可扩放性(Scalability)问题；为了客观、公正地评估计算机的性能,提高并行机的使用水平和效率,减少用户引进和购买高性能计算机的盲目性，所以了解掌握一些基本的基准程序也是很必要的。本章将对以上三个问题逐一作简要讨论。

# 3.1加速比性能定律

简单地讲，并行系统的加速(比)是指对于一个给定的应用，并行算法(或并行程序)的执行速度相对于串行算法(或串行程序)的执行速度加快了多少倍，本节将要讨论三种加速比性能定律：适用于固定计算负载的AmdahI定律；适用于可扩放问题的Gustafson定律和受限于存储器的Sun和Ni定律。为了以下讨论方便,兹定义如下参数：令p是并行系统中处理器数；W是问题规模(下文中也常叫作计算负载、工作负载,它定义为给定问题的总计算量),W,是应用程序中的串行分量,W中可并行化部分为Wp(显然W+W,=W);f是串行分量比例(f=W/W,W=W1),1-f为并行分量比例(显然f+(1-f)=1);T,=T1为串行执行时间,T,为并行执行时间;S为加速(比),E为效率。

# 3.1.1 Amdahl 定律

Amdahl加速定律的基本出发点是：①对于很多科学计算，实时性要求很高，即在此类应用中时间是个关键因素，而计算负载是固定不变的。为此在一定的计算负载下，为达到实时性可利用增加处理器数来提高计算速度；②因为固定的计算负载是可分布在多个处理器上的，这样增加了处理器就加快了执行速度，从而达到了加速的目的。在此意义下,1967年Amdahl推导出了如下固定负载的加速公式：

$$
S = \frac { W _ { \mathrm { s } } + W _ { \mathrm { \theta } _ { \mathrm { p } } } } { W _ { \mathrm { s } } + \ W _ { \mathrm { p } } / p }
$$

为了归一化， $W _ { \mathrm { s } } + W _ { \mathrm { p } }$ 可相应地表示为 $f + ( 1 - f )$ ，所以

$$
S = { \frac { f + ( 1 - f ) } { f + { \frac { 1 - f } { p } } } } = { \frac { p } { 1 + f ( p - 1 ) } }
$$

当 $\hbar \to \infty$ 时,上式极限为：

$$
S = \frac { 1 } { f }
$$

这就是著名的Amdahl加速定律,它意味着随着处理器数目的无限增大，并行系统所能达到的加速之上限为 $1 / f$ ，此结论在历史上曾对并行系统的发展起到了悲观的作用。

Amdahl定律的几何意义可清楚地表示在图3.1(a)、(b)和(c)中。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/4e0b6a82a7c4f3620f74dcdc59dbd09e5d04798986b21f4461c0479c5501e4be.jpg)  
图3.1Amdahl加速定律

实际上并行加速不仅受限于程序的串行分量，而且也受并行程序运行时的

额外开销影响。令 $W _ { \mathrm { o } }$ 为额外开销，则(3.1)式应修改为：

$$
S = { \frac { W _ { \mathrm { s } } + W _ { \mathrm { p } } } { W _ { \mathrm { s } } + { \frac { W _ { \mathrm { p } } } { \dot { p } } } + W _ { \mathrm { o } } } } = { \frac { W } { f W + { \frac { W \left( 1 - f \right) } { \dot { p } } } + W _ { \mathrm { o } } } } = { \frac { \dot { p } } { 1 + f ( \dot { p } - 1 ) + W _ { \mathrm { o } } \dot { p } / W } }
$$

当 ${ p \to \infty }$ 时，上式变为：

$$
S = \frac { 1 } { f + W _ { o } / W }
$$

可见,串行分量越大和并行额外开销越大，则加速越小。

# 3.1.2 Gustafson 定律

Gustafson加速定律的基本出发点是： $\textcircled{1}$ 对于很多大型计算，精度要求很高，即在此类应用中精度是个关键因素，而计算时间是固定不变的。此时为了提高精度，必须加大计算量，相应地亦必须增多处理器数才能维持时间不变； $\textcircled{2}$ 除非学术研究，在实际应用中没有必要固定工作负载而使计算程序运行在不同数目的处理器上,增多处理器必须相应地增大问题规模才有实际意义。按此意义，1987年Gustafson给出了如下放大问题规模的加速公式：

$$
S ^ { ' } = \frac { W _ { \mathrm { s } } + \ p W _ { \mathrm { p } } } { W _ { \mathrm { s } } + \ p \cdot W _ { \mathrm { p } } / _ { p } } = \frac { W _ { \mathrm { s } } + \ p W _ { \mathrm { p } } } { W _ { \mathrm { s } } + \ W _ { \mathrm { p } } }
$$

归一化后可得

$$
S ^ { \prime } = f + \ p ( 1 - f ) = p + f ( 1 - p ) = p - f ( p - 1 )
$$

当 $\pmb { \hat { p } }$ 充分大时， $s ^ { \prime }$ 与 $\pmb { \mathscr { P } }$ 几乎成线性关系，其斜率为 $1 \mathrm { ~ - ~ } f$ 。这就是著名的Gustafson加速定律，它意味着随着处理器数目的增加,加速几乎与处理器数成比例的线性增加,串行比例 $f$ 不再是程序的瓶颈，这对并行系统的发展是个非常乐观的结论。

Gustafson 定律的几何意义可清楚地表示在图3.2(a)、(b)和 $\left( \mathbf { c } \right)$ 中。

同样,当考虑到并行程序运行时的额外开销 $\mathbf { { w } } _ { \mathbf { { o } } }$ 时,(3.6)式应修改为：

$$
S ^ { \prime } = \frac { W _ { s } + \ p W _ { p } } { W _ { s } + W _ { p } + W _ { o } } = \frac { f + \ p \left( 1 - f \right) } { 1 + W _ { o } / W }
$$

注意： ${ { \bf { W } } _ { \bf { 0 } } }$ 是 $\pmb { \hat { p } }$ 的函数,它可能随 $\pmb { \hat { p } }$ 增大、减小或不变。一般化的Gustafson定律欲达到线性加速必须使 $\Psi _ { \mathbf { 0 } }$ 随 $\pmb { \phi }$ 减小,但这常常是困难的。

# 3.1.3 Sun 和 Ni定律

Xian-He Sun 和Lionel Ni于1993 年曾将 Amdahl 定律和 Gustafson 定律一般化,提出了存储受限的加速定律。其基本思想是只要存储空间许可，应尽量增大问题规模以产生更好或更精确的解(此时可能使执行时间略有增加)。换句话说，假若有足够的存储容量,并且规模可扩放的问题满足Gustafson定律规定的时间要求，那么就有可能进一步增大问题规模求得更好或更精确的解。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/3879ee581fbd2cf223f1d5ab80a27c49b8759a3a37da3d9cf8f18e092bc4e587.jpg)  
图3.2Gustafson加速定律

给定·个存储受限问题，假定在单节点上使用了全部存储容量 $M$ 并在相应于W的时间内求解之,此时工作负载 $\boldsymbol { W } = \boldsymbol { \mathscr { J } } \boldsymbol { W } + \left( 1 - \boldsymbol { \mathscr { J } } \right) \boldsymbol { W }$ 。在 $\pmb { \mathscr { p } }$ 个节点的并行系统上,能够求解较大规模的问题是因为存储容量可增加到 $_ { \mathit { p M } }$ 。令因子${ \bf \Xi } ( { \bf \Lambda } _ { \bf \dot { J } } )$ 反映存储容量增加 $\pmb { \mathscr { p } }$ 倍时工作负载的增加量，所以扩大后的工作负载$W = \ j W + \left( 1 - f \right) \zeta i ( \ j ) W ,$ ，对照(3.6)式,存储受限的加速公式相应为：

$$
S ^ { \prime \prime } { = } \frac { \not { I W } + \left( 1 - \not { I ^ { \prime } } \right) \not { G } \left( p \right) W } { \not { J W } + \left( 1 - \not { I ^ { \prime } } \right) \not { G } \left( p \right) W \not { J p } }
$$

归一化后可得

$$
S ^ { \prime \prime } { = } \frac { \int { + \left( 1 - j ^ { \prime } \right) ( j ^ { } ( p ) } } { \int { + \left( 1 - j ^ { \prime } \right) ( j ^ { } ( p ) / p } }
$$

Sun 和 ${ \ N i }$ 定律的儿何意义可清楚地表示在图3.3(a)和(b)中。

同样，当考虑到并行程序运行时的额外开销 $W _ { \mathrm { 0 } }$ 时，(3.9)式和(3.10)式可修改为：

$$
S ^ { \prime \prime } { = } \frac { f W + \left( 1 - f \right) W G \left( \rlap { / } p \right) } { f W + \left( 1 - f \right) G \left( \rlap { / } p \right) W / \rlap { / } p + W _ { 0 } } { = } \frac { f + \left( 1 - f \right) G \left( \rlap { / } p \right) } { f + \left( 1 - f \right) G \left( \rlap { / } p \right) / \rlap { / } p + W _ { 0 } / W }
$$

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/dc8f2284af0f7b2f51d35692f9b914836194d5fd11893704c797ead1930ba4c0.jpg)  
图3.3Sun和 $\mathbf { N _ { i } }$ 加速定律

由(3.10)可知，当 $G ( \pmb { \mathscr { p } } ) = \mathbf { 1 }$ 时，它变为 $\frac { 1 } { f + ( 1 - f ) / \phi }$ ，这就是 Amdahl加速定律(3.2)式;当 $G ( { \boldsymbol { \mathbf { \mathit { \phi } } } } ) = \phi$ 时,它变为 $f + \phi ( 1 - f )$ ,这就是Gustafson 加速定律(3.7)式；当 $G ( { \pmb \cdot } ) > _ { P }$ 时,它相应于计算负载比存储要求增加得快,此时 $\mathtt { s u n }$ 和${ \bf N } _ { \mathbf { i } } ^ { \mathbf { \cdot } }$ 加速均比Amdahl加速和Gustafson加速为高。

# 3.1.4有关加速的讨论

在实际应用中,可供参考的加速经验公式是：

$$
\scriptstyle { \pmb { \mathscr { p } } } \lambda _ { 0 \pmb { \mathscr { g } } \pmb { \mathscr { p } } } { \leqslant } S { \leqslant } p
$$

可达线性加速的应用问题有诸如矩阵相加、内积运算等,此类问题几乎没有通信开销;对于分治类的应用问题,它类似于二叉树,树的同级可并行执行,但向根逐级推进时，并行度将逐渐减少,此类问题可望达到 $\pmb { \phi } \pmb { \Lambda } \infty \pmb { \Lambda } p$ 的加速;对于通信密集类的应用问题,其加速经验公式可参考下式：

$$
S = 1 / C ( \mathbf { \Omega } _ { \hat { P } } )
$$

其中 $C ( \pmb { \mathscr { p } } )$ 是 $\pmb { \mathscr { P } }$ 个处理器的某一通信函数,或为线性的或为对数的。

严格的线性加速是难以达到的，更何况超线性加速（Superlinear Speedup）。但在某些算法或程序中,可能会出现超线性加速现象：例如,在某些并行搜索算法中,允许不同的处理器在不同的分枝方向上同时搜索，当某一处理器一旦迅速地找到了解，它就向其余的处理器发出中止搜索的信号，这就会提前取消那些在串行算法中所作的无谓的搜索分枝，从而出现超线性加速现象；又如，在绝大多数并行机中，每个处理器均有少量的高速缓存，当某一问题执行在大量的处理器上,而其大多的数据均放在高速缓存中时，总的计算时间趋于减少，如果由于这种高速缓存效应所造成的计算时间下降补尝了由于通信等所造成的额外开销时间，则有可能造成超线性加速现象。

最后值得指出的是，加速的含意对科学研究者和工程实用者可能有所不同：前者乐于使用绝对加速(Absolute Speedup)的定义，即对于给定的问题,最佳串行算法所用的时间除以同一问题其并行算法所用的时间；后者乐于使用相对加速(Rel-ative Speedup)的定义,即对于给定的问题,同一个算法在单处理器上运行的时间除以在多个处理器上运行的时间。显然相对加速的定义是较宽松和实际的。

# 3.2 可扩放性评测标准

评价并行计算性能的指标，除了上节所介绍的加速比以外，并行计算的可扩放性(Scalability)也是主要性能指标之一。可扩放性最简朴的含意是在确定的应用背景下,计算机系统(或算法或编程等)性能随处理器数的增加而按比例提高的能力。现今它已成为并行处理中一个重要的研究问题，被越来越广泛地用来描述并行算法(并行程序)能否有效利用可扩充的处理器数的能力。

# 3.2.1并行计算的可扩放性

从上节所介绍的三种加速定律可知，增加处理器数和求解问题的规模都可能提高加速比，而影响加速的因素有： $\textcircled{1}$ 求解问题中的串行分量； $\textcircled{2}$ 并行处理所引起的额外开销(通信、等待、竞争、冗余操作和同步等); $\textcircled{3}$ 加大的处理器数超过了算法中的并发程度。增加问题的规模有利于提高加速的因素是： $\textcircled{1}$ 较大的问题规模可提供较高的并发度； $\textcircled{2}$ 额外开销的增加可能慢于有效计算的增加； $\textcircled{3}$ 算法中的串行分量比例不是固定不变的(串行部分所占的比例随着问题规模的增大而缩小)。一般情况下，增加处理器数，是会增大额外开销和降低处理器的利用率的,所以对于一个特定的并行系统、并行算法或并行程序，它们能否有效利用不断增加的处理器的能力应是受限的，而度量这种能力就是可扩放性这一指标。

按照Webster 字典所作的定义(Scalability is the ability to scale,i.e,the abili-ty to adjust according toaproportion),可扩放性涉及到调整什么和按什么比例两方面的问题。对于并行计算而言，要调整的是处理器数 $\pmb { \hat { p } }$ 和问题规模W,两者可按不同比例进行调整,此比例关系(可能是线性的、多项式的或指数的等)就反

映了可扩放的程度。

当研究可扩放性时，总是将并行算法和体系结构一并考虑，也就是说可扩放性应该是算法和结构的组合。所以当谈论算法的可扩放性时，实际上是指该算法针对某一特定机器结构的可扩放性；同样当谈论体系结构的可扩放性时，实际上是指运行于该体系结构的机器上的某一个(或某一类)并行算法的可扩放性。

进行可扩放性研究的主要目的是： $\textcircled{1}$ 确定解决某类问题用何种并行算法与何种并行体系结构的组合，可以有效地利用大量的处理器； $\textcircled{2}$ 对于运行于某种体系结构的并行机上的某种算法，根据算法在小规模处理机上的运行性能，预测该并行算法当移植到大规模处理机上后运行的性能； $\textcircled{3}$ 对固定的问题规模，确定在某类并行机上最优的处理器数与可获得的最大的加速比； $\textcircled{4}$ 用于指导改进并行算法和并行机体系结构,以使并行算法尽可能地充分利用可扩充的大量处理器。

尽管可扩放性如此重要,并且已被广泛的研究，但目前仍无一个公认的、标准的和被普遍接受的严格定义和评判它的标准。下面从不同的角度,介绍三种典型的可扩放性度量方法，即等效率、等速度和平均延迟方法。

# 3.2.2等效率度量标准

可扩放性的概念是与加速比和效率的概念紧密相关的，为此必须先从加速$s$ 和效率 $E$ 讲起。

令 $t _ { \mathrm { ~ e ~ } } ^ { i }$ 和 $t _ { 0 } ^ { i }$ 分别是并行系统上第 $\textbf { \em i }$ 个处理器的有用计算时间和额外开销时间(包括通信、同步和空闲等待时间等);所有 $t _ { e } ^ { i }$ 之和记之为 $T _ { \mathrm { e } } = \sum _ { i = 0 } ^ { { \boldsymbol { p } } - 1 } t _ { \mathrm { e } } ^ { i }$ ，所有 $t _ { 0 } ^ { i }$ 之和记之为 $T _ { 0 } = \sum _ { i = 0 } ^ { { p - 1 } } t _ { 0 } ^ { i }$ to;令Tp是p个处理器系统上并行算法的运行时间，对于任意 $_ i$ ,显然有 $T _ { \mathrm { p } } = \mathrm { \Delta } t _ { \mathrm { e } } ^ { i } + \mathrm { \Delta } t _ { 0 } ^ { i }$ ，且

$$
\begin{array} { r } { T _ { e } + \ T _ { o } = \ p T _ { p } } \end{array}
$$

问题的规模W可定义为由最佳串行算法所完成的计算量,也称工作负载或工作量，即 $W = T _ { \mathrm { e } }$ 。所以并行算法的加速和效率可分别定义如下：

$$
S = { \frac { T _ { \mathrm { e } } } { T _ { \mathrm { p } } } } = \underbrace { { \frac { T _ { \mathrm { e } } } { T _ { \mathrm { e } } + T _ { \mathrm { o } } } } } _ { \displaystyle { \hat { p } } } = { \frac { \displaystyle { \hat { p } } } { \displaystyle { 1 + { \frac { T _ { \mathrm { o } } } { T _ { \mathrm { e } } } } } } } = { \frac { \displaystyle { \hat { p } } } { \displaystyle { 1 + { \frac { T _ { \mathrm { o } } } { W } } } } }
$$

$$
E = { \frac { S } { \phi } } = { \frac { 1 } { 1 + { \frac { T _ { \circ } } { T _ { \mathrm { e } } } } } } = { \frac { 1 } { 1 + { \frac { T _ { \circ } } { W } } } }
$$

在通常情况下，如果问题规模W保持不变(即T。保持不变),则随着处理器数p的增加，开销T。也会随之增大,根据(3.16)式,效率E也会相应下降。为了维持效率E不变,就要保持T/T。的值不变,故需要在处理器数p增大的同时相应地增加问题规模W的值（即 $T _ { \epsilon }$ 的值)才有可能抵消由于 $\boldsymbol { p }$ 的增大而导致 $T _ { \mathrm { { o } } }$ 增大的影响，从而保持效率不变。也就是说，为了维持一定的效率（介于0与1之间),当处理数 $\pmb { \mathit { p } }$ 增大时，需要相应地增大问题规模W的值。由此定义函数 $f _ { \mathrm { { F } } } ( \mathbf { \Gamma } _ { P } )$ 为问题规模W随处理器数 $\boldsymbol { p }$ 变化的函数，称此函数为等效率函数(ISO-efficiency Function),它是由Kumar 等人1987年提出的。

按照等效率函数的定义，对于某一并行算法(或并行程序),为了维持运行效率保持不变，随着处理器数目的增加，若只需增加较小的工作量(即问题规模),比如说W随 $\pmb { \mathscr { p } }$ 呈线性或亚线性增长，则表示该算法具有良好的可扩放性;若需增加非常大的问题规模,比如说W随 $\pmb { \mathscr { p } }$ 呈指数级增长，则表示该算法是不可扩放的。

图3.4给出了三种等效率函数曲线，曲线1表示算法具有很好的扩放性;曲线2表示算法是可扩放的；曲线3表示算法是不可扩放的。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/c5bfc7384a6162eabda91d1af3d808250584b675a85a1719ba480db72891a43c.jpg)  
图3.4等效率函数曲线

下面使用等效率函数方法来分析超立方网络上的FFT算法的可扩放性。

对于 $_ { n }$ 点 FFT算法，假定一个计算单位的成本是 $t _ { \mathrm { c } }$ ，则 $T _ { \mathrm { c } } = \mathbf { \boldsymbol { W } } = t _ { \mathrm { c } } \pi \mathrm { l o g } n _ { \mathrm { ~ o ~ } }$ 假定使用 $\smash { p = 2 ^ { d } }$ 个处理器来进行计算，则每个处理器计算 $n / p$ 个值。因为在并行计算FFT时，最多只能使用 $^ { n }$ 个处理器(否则多余的处理器无事可做),所以等效率函数的下界为 $\Omega \big ( \hbar \log p \big )$ ,它是算法固有并行度的函数,与并行结构无关。

利用(3.16)式计算等效率函数时,关键是如何计算 $T _ { \mathrm { { o } } }$ 。在计算FFT时 $T _ { \mathrm { { o } } }$ 主要来源于两个处理器之间的通信,从一个处理器发送一条消息至另一个处理器所涉及到的开销包括： $\textcircled{1}$ 通信建立时间 $t _ { \textrm { s } }$ ，它与消息长短和所走过的距离无关； $\textcircled{2}$ 跨步 $\left( \mathrm { H o } _ { \mathfrak { g } } \ltimes \right)$ 延迟 $t _ { \mathfrak { h } }$ ,它等于相邻两计算节点之间一个单位消息的延迟时间（不包括$t _ { \mathrm { s } } ) { : \textcircled { \cdot } }$ 每个字节占用时间 $t _ { \mathrm { b } }$ ，它等于通信带宽 $B$ (字节/秒)的倒数。所以条长为$\nu \eta$ 的消息，从源到目的其间经由 $l$ 个跨步点时的通信开销为： $t _ { \mathrm { s } } + \big ( t _ { \mathfrak { h } } , m + t _ { \mathfrak { h } } \big ) l _ { \mathrm { ~ o ~ } }$ 令 $l _ { j }$ 是第 $j$ 次迭代计算时两通信处理器之间的海明距离，且假定它们等长；假定不同消息选路时互不重叠。因为每个处理器包含有 $n / p$ 个数据,所以总的通信开

销 $T _ { \circ }$ 为：

$$
T _ { \mathrm { o } } \mathrm { = } \phi \sum _ { j \mathrm { = 0 } } ^ { d \mathrm { - 1 } } \big [ t _ { \mathrm { s } } + \big ( t _ { \mathrm { h } } + t _ { \mathrm { b } } n / \phi \big ) l _ { j } \big ]
$$

在超立方网络中，所有成对通信的处理器之间的距离恒为1,所以(3.17)式变为：

$$
T _ { \circ } = \dot { p } \sum _ { j = 0 } ^ { \log \beta - 1 } \left( t _ { s } + t _ { \mathrm { h } } + t _ { \mathrm { b } } n / \dot { p } \right) = \left( t _ { \mathrm { h } } + t _ { s } \right) \dot { p } \log \phi + t _ { \mathrm { b } } \pi \log \phi \ .
$$

当 $\pmb { \hat { p } }$ 增加时,为了维持 $E$ 在某一值, $\pmb { n }$ 亦必须增加使得 $T _ { \mathrm { e } } = k T _ { \mathrm { o } }$ ,即

$$
t _ { \mathrm { c } } n \log n = k \left[ \left( t _ { \mathrm { h } } + t _ { \mathrm { s } } \right) \hbar \log \phi + t _ { \mathrm { b } } n \log \phi \right]
$$

其中 $k = E / ( 1 - E )$ 。由于 $n \log _ { \mathcal { P } } \gg _ { \mathcal { P } } \log _ { \mathcal { P } }$ ,所以(3.19)式中第二项为主项,即可考虑 $t _ { \mathrm { c } } n \log n = k t _ { \mathrm { b } } n \log \phi$ 之情况,经过简单代数变换，则得

$$
n = p ^ { k t } \mathfrak { { b } } ^ { / t } \mathfrak { { c } }
$$

因为 $\boldsymbol { W } = \boldsymbol { t } _ { \mathrm { c } } n \log \boldsymbol { n }$ ,所以等效率函数 $f _ { \mathbb { E } } ( \mathbf { \nabla } _ { \mathcal { P } } )$ 为：

$$
W = f _ { \mathrm { E } } ( \mathbf { \nabla } _ { \phi } ) = k t _ { \mathrm { b } } \mathbf { \nabla } \phi ^ { k t _ { \mathrm { b } } / t _ { \mathrm { c l o g } \phi } }
$$

上式中只要 ktb/t<1,则W的增长率小于O(plogp);-旦ktb/t>1,则等效率函数随着 $k \frac { t _ { \mathrm { b } } } { t _ { \mathrm { c } } }$ 的增大急剧恶化;当 $t _ { b } = t _ { c }$ 时，若 $k < 1$ （即 ${ E < } 0 . 5 )$ ，则W$\mathbf { \Psi } = \theta \left( \ p \log { \mathbf { \alpha } } \right)$ ；若 $k > 1$ （即 $\mathbf { \mathcal { E } } > \mathbf { 0 } \mathbf { \mathcal { . } } \mathbf { \mathcal { 5 } } )$ ，例如说 $E = 0 . 9$ ，则 $k = 9$ ，于是 $\pmb { W } =$ $\Theta \big ( \ b { \phi } ^ { \boldsymbol { \mathfrak { s } } } \mathrm { l o g } \ b { \phi } \big )$ 。此时的等效率函数要差得多。这说明,如果 $t _ { \mathrm { b } } = t _ { \mathrm { c } }$ ,在大的超立方网络上很难得到比0.5高得多的效率。

# 3.2.3等速度度量标准

等效率度量标准最大优点是，可用简单的、可定量计算的、少量的参数就能计算出等效率函数，并由其复杂性可指明算法的可扩放程度。这对于具有网络互连结构的并行机来说是很合适的,因为已如上一节例子那样，T。是可一步一步计算出的。也正是这个T。是计算等效率函数的唯一关键参数，所以如果它不能够方便地计算出，则等效率函数度量可扩放性的方法就受到了限制。我们知道开销T。通常包括了通信、同步、等待等非有效计算时间。不幸的是,在共享存储的并行计算机中,T。则主要是非局部访问的读/写时间、进程调度时间、存储竞争时间以及高速缓存一致性操作时间等,而这些时间都是难以准确计算的。所以用解析计算的方法度量可扩放性不应是一种唯一的方法。事实上，两位中国学者 Xian-He Sun 和 Xiao Dong Zhang于 1994 年分别提出了以试验测试为主要手段的两种评测可扩放性的标准，即等速度(ISO-speed)和平均延迟(AverageLatency)标准。本节先介绍前者，下节再介绍后者。

大家知道,速度是一个非常重要的机器参数，一般在机器性能指标中都明确地给出，并常以每秒多少次浮点运算(Flops)来表明(按照约定的含意，浮点运算数目就是工作负载W)。所以若用速度来度量可扩放性,在原理上讲是更方便的,而等速度方法的基本出发点就在于此。

在并行系统中，提高速度可以使用增加处理器数的办法，如果速度能以处理器数的增加而线性增加(此即意味着平均速度不变),则说明此系统具有很好的扩放性。为此先作如下定义：

令 $\pmb { \mathscr { p } }$ 表示处理器个数,W表示要求解问题的工作量或称问题规模(在此可指浮点操作个数)， $T$ 为并行执行时间，则定义并行计算的速度 $V$ 为工作量W除以并行时间 $T$ ：

$$
V = W / T
$$

而 $\pmb { \hat { p } }$ 个处理器的并行系统的平均速度定义为并行计算速度 $\boldsymbol { V }$ 除以处理器个数$\pmb { \phi }$ ：

$$
\overline { { V } } = \frac { V } { \rho } { \overset { . } { = } } \frac { \overline { { W } } } { \rho T }
$$

根据平均速度(3.23)式,就可定义等平均速度(简称为等速度)可扩放度量标准如下：

对于运行于并行机上的某个算法，当处理器数目增加时,若增大一定的工作量能维持整个并行系统的平均速度不变，则称该计算是可扩放的。

注意,平均速度为常数,意即速度与处理器数目成线性比例增长,亦即加速比为线性的。

按此定义,令W是使用 $\pmb { \mathscr { P } }$ 个处理器时算法的工作量,令 $\mathbf { \overrightarrow { W } } ^ { \prime }$ 表示当处理数从 $\pmb { \hat { p } }$ 增大到 $\pmb { \hat { p } } ^ { \prime }$ 时,为了保持整个系统的平均速度不变所需执行的工作量，则可得到处理器数从 $\pmb { \hat { p } }$ 到 $\pmb { \hat { p } } ^ { \prime }$ 时平均速度可扩放度量标准公式为：

$$
\Psi ( \boldsymbol { \phi } , \boldsymbol { \phi } ^ { \prime } ) = \frac { W / p } { W ^ { \prime } / p ^ { \prime } } = \frac { \boldsymbol { \phi } ^ { \prime } W } { \boldsymbol { \phi } W ^ { \prime } }
$$

用上述公式计算出的值介于0与1之间,值越大表示可扩放性越好。

当平均速度严格保持不变时,即

$$
\frac { W } { T \hat { p } } = \frac { W ^ { \prime } } { T ^ { \prime } \hat { p ^ { \prime } } } \to \frac { \hat { p ^ { \prime } } W } { \hat { p } W ^ { \prime } } = \frac { T } { T ^ { \prime } }
$$

所以，(3.24)式可变为：

$$
\Psi ^ { \prime } ( \phi , \phi ^ { \prime } ) = \frac { T } { T ^ { \prime } }
$$

当p=1时,记T=T;当处理器个数为p'时,记T=Tp;相应地记p=1时 $\boldsymbol { \Psi } ( \boldsymbol { 1 } , \boldsymbol { \phi } ^ { \prime } )$ 为 $\pmb { \varPsi } ( \pmb { \mathscr { p } } ^ { \prime } )$ ,于是有

$$
\Psi ( \ p ^ { ' } ) = \frac { \hbar ^ { 2 } W } { W ^ { ' } } = \frac { T _ { 1 } } { T _ { \mathrm { p ^ { ' } } } } = \frac { W } { W ^ { ' } / p ^ { ' } } = \frac  \frac { \hbar \pi } { \hbar \pi } \pm \frac { \hbar } { \hbar } . \pm \frac { \gamma } { \hbar } \ \frac { \hbar } { \hbar } \pm \frac { \gamma } { \hbar } \ \frac { \hbar } { \hbar } \pm \frac { \hbar } { \hbar } \pm \frac { \hbar } { \hbar } \pm \frac { \gamma } { \hbar \pi } \pm \frac { \hbar } { \hbar \pi } \pm \frac { \gamma } { \hbar \pi } \pm \frac { \hbar } { \hbar } \pm \frac { \gamma } { \hbar } \pm \frac { \hbar } { \hbar } \pm \frac { \gamma } { \hbar } \pm \frac { \hbar } { \hbar } \pm \frac { \gamma } { \hbar } \pm \frac { \hbar } { \hbar } \pm \frac { \gamma } { \hbar } \pm \frac { \hbar } { \hbar } \pm \frac { \gamma } { \hbar } \pm \frac { \hbar } { \hbar } \pm \frac { \gamma } { \hbar } \pm \frac { \hbar } { \hbar } \pm \frac { \gamma } { \hbar } \pm \frac { \gamma } { \hbar \pi } \pm \frac { \hbar } { \hbar } \pm \frac { \gamma } { \hbar } \pm \frac { \gamma } { \hbar } \pm \frac { \hbar } { \hbar } \pm \frac { \gamma } { \hbar } \pm \frac { \gamma } { \hbar \pi } \pm \frac { \hbar } { \hbar } \pm \frac { \gamma } { \hbar } \pm \frac { \gamma } { \hbar \pi } \pm \frac { \gamma } { \hbar \pi } \pm \frac { \gamma } { \hbar \pi } \pm \frac { \gamma } { \hbar \pi } \pm \frac { \gamma } { \hbar } \pm \frac { \gamma } { \hbar } \pm \frac { \gamma } { \hbar } \pm \frac { \gamma } { \hbar \pi } \pm \frac { \gamma } { \hbar \pi } \pm \frac { \gamma } { \hbar \pi } \pm \frac { \gamma } { \hbar \pi } \pm \frac { \gamma } { \hbar \pi } \pm \frac { \gamma } { \hbar } \pm \frac { \gamma } { \hbar } \pm \frac { \gamma } { \hbar } \pm \frac { \gamma } { \hbar \pi } \pm \frac { \gamma } { \hbar \pi } \pm \frac { \gamma } { \hbar \pi } \pm \frac { \gamma } { \hbar \pi } \pm \frac { \gamma } { \hbar } \pm \frac { \gamma } { \hbar } \pm \frac { \gamma } { \hbar } \pm \frac { \gamma } { \hbar } \pm \frac  
$$

(3.26)式给出的可扩放性定义与传统的加速比定义有点类似，其主要差别在于：加速比的定义是保持问题规模不变；而可扩放性定义是保持平均速度不变。如图3.5所示，加速比是标志并行处理相对于串行处理所获得性能增加；而如图3.6所示，可扩放性是标志从小规模系统到大规模系统所引起的性能衰减。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/3126c0a33f534b879d5991c2b8837c2c375a18009aa27a58cf1e231823166ec5.jpg)  
图3.5加速比：问题规模不变,时间变短

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/63118f117a3e66dc599541eb302a4ab3d6eeacc0e37a23b9eb2a7e6b136b4c7c.jpg)  
图3.6可扩放性：平均速度不变,时间加长

一般有三种方法可得到等速度可扩放性标准： $\textcircled{1}$ 测量法：使用软件方法，即采用控制程序去调用应用程序，找寻所希望的固定的平均速度；②计算法：首先找出平均速度和执行时间之间的关系，再使用(3.25)式计算之；③预计法：采用推导一般可扩放性公式来研究可扩放性。

下面，只简单介绍一下第二种方法，它结合一组测量的数据（V和T）借助几何作图法和通过使用公式(3.25),最终画出一组等速度可扩放性曲线,其具体步骤是：

① 测量平均速度V和并行执行时间T：给定某一应用程序，使其运行在m。个处理器的并行机上,固定mo,改变工作量范围W到W',测量相应平均速度和运行时间,改变mo到m1,固定m1,改变工作量范围W到W',测量相应平均速度和运行时间；重复之，可绘制出一组如图3.7所示的一组V-T曲线。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/aa3e8d1191139ca696bd3dbfe4f762f8c1480ea21f7d125ece0e1258051c86da.jpg)  
图3.7 ${ \overline { { \boldsymbol { v } } } } - { \boldsymbol { T } }$ 曲线

$\textcircled{2}$ 选择参考平均速度 $\overline { { V } } _ { \frac { 1 } { 2 } }$ ,求出不同处理器数时的执行时间 $T _ { \mathrm { i } }$ ：令 $\overline { { V } } _ { \infty }$ 是在单处理机上、 ${ \pmb W }  \infty$ 时的渐近平均速度;取其一半 $\frac { 1 } { 2 } \overline { { V } } _ { \infty }$ 作为参考平均速度$\overline { { V } } _ { \frac { 1 } { 2 } }$ ,在图3.7之纵坐标上，过点 $\overline { { V } } _ { \frac { 1 } { 2 } }$ 作平行于水平轴的直线;过该直线与诸曲线的交点,分别作平行于垂直轴的直线,它们与 $\pmb { X }$ 轴的交点就是相应于各处理器的执行时间。

$\textcircled{3}$ 根据(3.25)式，计算 $\Psi \big ( \boldsymbol { \phi } , \boldsymbol { \phi } ^ { \prime } \big )$ 之值,它就是所要求的等速度可扩放性标准。

对于某一应用程序,若取 $\overline { { V } } \frac { 1 } { 2 } = \frac { 1 } { 2 } \overline { { V } } _ { \infty } = \frac { 1 } { 2 } \times 1 . 7 \left( \mathrm { M f l o p s } \right) = 0 . 8 5 \left( \mathrm { M f l o p s } \right) ,$ 根据图3.7,可作出表3.1所示的处理器个数与相应执行时间表;当平均速度不变时，根据表3.1,利用(3.25)式，就可计算出如表3.2所示的诸 $\bar { \pmb { \Psi } } ( \pmb { \phi } , \pmb { \phi } ^ { \prime } )$ 之值；根据表3.2,再补充一些数据项,就可作出如表3.3所示的 $\Psi \big ( \ b { \phi } , \ b { \phi } ^ { \prime } \big )$ 上三角阵。

表3.1处理器数及其相应执行时间一览表  

<table><tr><td rowspan=1 colspan=1>处理器数</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>：  2</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>16</td><td rowspan=1 colspan=1>32</td><td rowspan=1 colspan=1>64</td><td rowspan=1 colspan=1>128</td></tr><tr><td rowspan=1 colspan=1>执行时间</td><td rowspan=1 colspan=1>0.004 029</td><td rowspan=1 colspan=1>0.09 13</td><td rowspan=1 colspan=1>0.013 62</td><td rowspan=1 colspan=1>0.017 44</td><td rowspan=1 colspan=1>0.021 44</td><td rowspan=1 colspan=1>0.025 61</td><td rowspan=1 colspan=1>0.029 6</td><td rowspan=1 colspan=1>0.033 38</td></tr></table>

表3.2 $\yen ( p , p ^ { \prime } )$ 一览表  

<table><tr><td rowspan=1 colspan=1>(1,2)</td><td rowspan=1 colspan=1>亚(2,4)</td><td rowspan=1 colspan=1>亚(4,8)</td><td rowspan=1 colspan=1>(8,16)</td><td rowspan=1 colspan=1>亚(16,32)</td><td rowspan=1 colspan=1>亚(32,64)</td><td rowspan=1 colspan=1>(64,128)</td></tr><tr><td rowspan=1 colspan=1>0.441</td><td rowspan=1 colspan=1>0.670</td><td rowspan=1 colspan=1>0.781</td><td rowspan=1 colspan=1>0.831</td><td rowspan=1 colspan=1>0.837</td><td rowspan=1 colspan=1>0.865</td><td rowspan=1 colspan=1>0.887</td></tr></table>

表3.3 $\yen ( p , p ^ { \prime } )$ 上三角阵  

<table><tr><td rowspan=1 colspan=1>处理器数</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>16</td><td rowspan=1 colspan=1>32</td><td rowspan=1 colspan=1>64</td><td rowspan=1 colspan=1>128</td></tr><tr><td rowspan=1 colspan=1>1248163264128</td><td rowspan=1 colspan=1>1.000</td><td rowspan=1 colspan=1>0.4411.000</td><td rowspan=1 colspan=1>0.2960.6701.000</td><td rowspan=1 colspan=1>0.2310.5240.7811.000</td><td rowspan=1 colspan=1>0.1880.4260.6350.8131.000</td><td rowspan=1 colspan=1>0.1570.3570.5320.6810.8371.000</td><td rowspan=1 colspan=1>0.1360.3080.4600.5890.7240.8651.000·</td><td rowspan=1 colspan=1>0.1210.2740.4080.5220.6420.7670.8871.000</td></tr></table>

$\textcircled{4}$ 根据表3.3,对其每一行都可作出一条 $\pmb { \psi } ( \pmb { \phi } ^ { \prime } )$ 与 $\pmb { \phi } ^ { \prime }$ 的变化曲线，显然增大起始的处理器数可改善系统的可扩放性。图3.8示出了 $\pmb { \psi } ( \pmb { \phi } ^ { \prime } )$ 与 $\pmb { \hat { p } ^ { \prime } }$ 变化曲线簇，曲线越平坦，可扩放性越好。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/02b97e76282e377706819e615103980d4f597d75449171607b9aadefa3b7f944.jpg)  
图3.8以 $\pmb { \hat { p } }$ 为参数的 $\pmb { \psi } ( \pmb { \phi } ^ { \prime } )$ 与 $\pmb { \hat { p } } ^ { \prime }$ 变化曲线簇

# 3.2.4平均延迟度量标准

等速度度量标准最大优点是，使用机器性能速度指标这一明确的物理量来度量可扩放性是比较直观的。它有一系列优点： $\textcircled{1}$ 速度是由工作负载W和执行时间 $T$ 决定的,而W反映了应用程序的性质， $T$ 反映了结构和程序效率的影响；②速度是各种结构的机器相互可比较的量;③执行时间包含了计算和延迟这两个主要的时间量；④速度是比较容易测量的，因为W可由所执行的浮点操作数决定。但它也有一些不足：①仅用浮点操作数作为W是不全面的，某些非浮点运算可能造成性能的主要变化；②延迟虽包含在执行时间中，但它未明确地定义为W的函数。实际上，可扩放性测定可以在系统和应用的更低层上，它们能更精确地抓住影响性能的结构因素和程序开销模式。下面将介绍使用测量平均延迟开销的办法来度量可扩放性。为此先作如下定义：

参照图3.9,令 $T _ { i }$ 为 $\boldsymbol { \mathrm { { P } } } _ { i }$ 的执行时间、它还包括在运行时所招致的延迟 $L _ { i }$ ，程序运行时还包括启动与停止时间。所以第 $i$ 个处理器 $\mathrm { \bf P } _ { i }$ 的总延迟时间为 ${ } ^ { \bullet } L _ { i }$ $+$ 启动时间 $^ +$ 停止时间”。定义系统平均延迟时间 $\overline { { L } } ( W , \boldsymbol { p } )$ 为：

$$
\overline { { L } } ( W , \ / p ) = \sum _ { i ^ { - } 1 } ^ { \prime ^ { \prime } } ( T _ { \mathrm { p a r a } } - T _ { i } + L _ { i } ) / p
$$

因为， $p T _ { \mathrm { p s t r a } } { = } T _ { \mathrm { o } } { + } T _ { \mathrm { s u t } } ( T _ { \mathrm { s u t } }$ 为串行执行时间)和 $T _ { \mathrm { o } } \mathrm { = } f \overline { { L } } \mathrm { ( } W , \mathbf { \phi } _ { p } \mathrm { ) }$ ，所以

$$
\overline { { L } } ( \ : W , / p ) = T _ { \mathrm { p a r a } } - T _ { \mathrm { s a q } } / p
$$

执行时间

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/3e049b90442328184f377925219e57c22fdc28593b1dac103d3a02957a9022a0.jpg)  
图3.9定义平均延迟示意图

对于一个算法-机器组合，令 $\overline { { L } } ( W , \boldsymbol { p } )$ 表示在 $p$ 个处理器上求解工作量为W问题的平均延迟; $\overline { { L } } ( \boldsymbol { W } ^ { \prime } , \boldsymbol { p } ^ { \prime } )$ 表示在 ${ \boldsymbol { p } } ^ { \prime }$ 个处理器上求解工作量为W'问题的平均延迟。当处理器数由 $\boldsymbol { \mathscr { p } }$ 变到 $p ^ { ' }$ ,而维持并行执行效率不变,则定义平均延迟可扩放性度量标准为：

$$
\bar { \phi } ( E , \boldsymbol { \rho } , \boldsymbol { \rho } ^ { \prime } ) = \frac { \overline { { L } } ( W , \boldsymbol { \rho } ) } { \overline { { L } } ( W ^ { \prime } , \boldsymbol { \rho } ^ { \prime } ) }
$$

用上述公式计算出的值介于0与1之间,值越大表示可扩放性越好。

下面,简单介绍一下使用平均延迟度量可扩放性的全过程：

①给定系统处理器数的变化范围和期望的效率E,按如下流程调整工作量W,直到满足所要求的E,最后计算出平均延迟。

②绘制延迟曲线：对于·个给定的应用问题，指定所要求的效率，变化处理器个数从 $\pmb { \hat { p } _ { 1 } }$ 到 $\pmb { \mathscr { p } } _ { i }$ ,按照图3.10流程调整W,就可画出一条曲线;变化不同的

$E$ ,就可画出一簇曲线。

$\textcircled{3}$ 根据上一步的结果，就可作出 $\overline { { L } } ( W , / )$ 与处理器个数变化关系表；由此表按照公式(3.29)就可计算出 $\Phi ( E , p , p ^ { \prime } )$ 之值；再由这些 $\Phi ( E , p , p ^ { \prime } )$ 就可构筑类似于表3.3的 $\Phi ( E , p , p ^ { \prime } )$ 上三角阵。文献[187]给出了这样的一个上三角阵，它是5000个元素的快排序算法，为了保持 $E = 0 . 2 5$ ,问题规模从在2个处理器上的 $W = 4 ~ 8 6 6$ 调整至32个处理器上的 $W = 9$ 753184,完整的上三角阵如表3.4所示，其中表项值越大，可扩放性越好。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/bf76e40e262b6b7b14b5c7dbf49e9e718ab910f10e9faefebe882707891441b9.jpg)  
图3.10调整问题规模W的过程

表3.4 $\Phi ( 0 , 2 5 , \rho , \rho ^ { \prime } )$ 上三角阵  

<table><tr><td>处理器数</td><td>2</td><td>4</td><td>8</td><td>16</td><td>24</td><td>32</td></tr><tr><td>2</td><td>1.000</td><td>0.941 9</td><td>0.695 7</td><td>0.220 4</td><td>0.032 9</td><td>0.0090</td></tr><tr><td>4</td><td></td><td>1.000 0</td><td>0.667 7</td><td>0.2116</td><td>0.031 6</td><td>.0.008 6</td></tr><tr><td>8</td><td></td><td></td><td>1.000</td><td>0.316 9</td><td>0.047 3</td><td>0.012 9</td></tr><tr><td>16</td><td></td><td></td><td></td><td>1.0000</td><td>0.149 3</td><td>0.040 8</td></tr><tr><td>24</td><td></td><td></td><td></td><td></td><td>1.000 0</td><td>0.273 2</td></tr><tr><td>32</td><td></td><td></td><td></td><td></td><td></td><td>1.000 0</td></tr></table>

# 3.2.5有关可扩放性标准的讨论

以上三节分别介绍了三种典型的可扩放性度量标准：等效率、等速度和平均延迟。等效率度量标准是在保持效率 $E$ 不变的前提下，研究问题规模W如何随处理器个数 $\pmb { \mathscr { P } }$ 而变化；等速度度量标准是在保持平均速度不变的前提下，研究处理器数 $\pmb { \mathscr { P } }$ 增多时应该相应地增加多少工作量W；平均延迟度量标准则是在效率 $E$ 不变的前提下，用平均延迟的比值来标志随着处理器数 $\pmb { \hat { p } }$ 的增加需要增加的工作量 $\mathbf { \Delta } \mathbf { w }$ 。三种评判可扩放性的标准的基本出发点都是抓住了影响算法可扩放性的基本参数 $T _ { \circ }$ ,只是等效率标准是采用解析计算的方法得到 $T _ { \circ }$ ；等速度标准是将 $T _ { \mathfrak { o } }$ 隐含在所测量的执行时间中；而平均延迟标准则是保持效率为恒值时,通过调节W与 $\pmb { \mathscr { p } }$ 来测量并行和串行执行时间,最终通过平均延迟反映出$T _ { o }$ ,所以等速度与平均延迟标准都是辅之以测试手段而得到有关性能参数（如速度与时间等)来评判可扩放性的;而等效率标准是通过解析计算开销参数 $T _ { o }$ 来评判可扩放性的。平均速度 $\overline { { V } }$ 和平均延迟 $\overline { L }$ 两个物理量的引入,目的近乎一样： $\varPsi ( \phi , \phi ^ { \prime } ) = T / T ^ { \prime }$ 保持不变，意即 $T _ { 0 }$ 随 $\pmb { \hat { p } }$ 变化很小； $\pmb { \mathscr { P } } \left( E , \pmb { \mathscr { p } } , \pmb { \mathscr { p } } ^ { \prime } \right) = \overline { { L } } \sqrt { L } ^ { \prime }$ 保持不变,亦意即 $T _ { \circ }$ 随 $\pmb { \hat { p } }$ 变化甚小。

事实上,三种度量可扩放性的标准是彼此等效的,这可简单推导如下：

由于运行在 $\pmb { \hat { p } }$ 个处理器上的工作量为 $\pmb { W }$ 的程序串行执行时间为 $\pmb { W } \pmb { t } _ { \pmb { c } }$ ,其效率 $E = \frac { W t _ { \mathrm { c } } } { \phi T _ { \mathrm { p } } }$ ,而程序的平均速度 $\overline { { V } } = \frac { W } { \rho T _ { \mathrm { ~ p ~ } } }$ ，所以 $E = \overline { { V } } \cdot \mathbf { \sigma } _ { t _ { \circ } }$ ,其中 $t _ { \mathfrak { c } }$ 为常数。这表明等效率与等速度两种度量可扩放性的标准在物理意义上是一致的

由于平均速度V=W $\overline { { V } } = \frac { \overrightarrow { W } } { \vert \overrightarrow { P } / } , \thinspace \thinspace \thinspace \phi T = T _ { \circ } + \ T _ { \mathrm { s e q } }$ ，而 $\mathcal { T } _ { \circ } \mathbf { = } \overset { \cdot } { p _ { \mathbf { \theta } } } \widetilde { L } ( \textbf { \em W } , \mathbf { \phi } )$ 且 $T _ { \mathrm { s e q } } = \mathbf { W } t _ { \mathrm { c } }$ 所以

$$
\overline { { V } } = \frac { W } { \hat { p } T } = \frac { W } { T _ { \mathrm { o } } + T _ { \mathrm { s e q } } } = \frac { W } { \hat { p } \widetilde { L } \left( W , \mathbf { \nabla } \mathbf { , } p \right) + W t _ { \mathrm { c } } } = \frac { W / p } { \widetilde { L } \left( W , \mathbf { \nabla } \mathbf { , } p \right) + W t _ { \mathrm { c } } / p }
$$

由此可推导出

$$
\overline { { L } } ( \mathrm { ~ W ~ } , \mathbf { \phi } ) = \frac { W } { \rho } \left( \frac { 1 } { \overline { { \mathbf { V } } } } - \mathbf { \phi } _ { t _ { c } } \right)
$$

当 $\widehat { V }$ 保持不变时， $\frac { 1 } { \overline { { V } } } - t _ { c }$ 为常数，所以

$$
\frac { \overline { { L } } ( \boldsymbol { W } , \boldsymbol { \phi } ) } { \overline { { L } } ( \boldsymbol { W } ^ { \prime } , \boldsymbol { \phi } ^ { \prime } ) } = \frac { \boldsymbol { W } } { \dot { p } } \Big / \frac { \boldsymbol { W } ^ { \prime } } { \dot { p } ^ { \prime } } = \frac { \boldsymbol { \phi } ^ { \prime } \boldsymbol { W } } { \dot { p } \boldsymbol { W } ^ { \prime } }
$$

根据(3.24)式和(3.29)式，(3.30)式表明从等速度度量标准可以导出平均延迟度量标准,两者是完全一致的。

最后要说的是，既然等速度和平均延迟两个可扩放性评判标准都是立足于测量的办法,那么就要为此提供一套测试手段、工具、环境以搜集、测量、分析有关数据并显示可扩放性性能。

# \*3.3 基准测试程序

基准测试程序(Benchmark)用于测试和预测计算机系统的性能，揭示不同结构机器的长处和短处，为用户决定购买或使用哪种机器最适合他们的应用要求提供决策。基准测试程序试图提供一个客观、公正的评价机器性能的标准。但真正做到完全公正并非易事，要涉及到的因素很多，包括硬件、体系结构、编译优化、编程环境、测试条件、解题算法等。一组标准的测试程序要提供一组控制测试条件和步骤的规则说明,包括测试平台环境、输入数据、输出结果和性能指标等。

不同的基准测试程序，侧重目的也有所不同：有的测试CPU性能，有的测试文件服务器性能,有的测试输入／输出界面,有的则测试网络通信速度等。根据不同用途,测试程序可有专用和通用之分。目前国际上流行的通用测试程序可分为好几类:①综合型（如Dhrystone、Whetstone 等）;②核心型（如LivermoreFortran Kernels、NASA 之 NAS 等）; $\textcircled{3}$ 数学库（如 Linpack、FFT等）; $\textcircled{4}$ 应用型（如 SPEC、Perfect、Splash 等）； $\textcircled{5}$ 并行型（如 NAS 之 NPB、PARKBENCH等）。本节仅仅介绍一些常见测试程序,它们很多都可在Internet上公开查到：http：//www.netlib.org/Liblist.html。在这里你可查到 LINPACK、LAPACK、BLAS、BLACS、Livermore Loops、Dhrystone、Whetstone、NAS、SPEC、 $\sin$ 等包含源代码的基准测试程序。

# 3.3.1基本测试程序

Whetstone它是为比较不同的计算机的浮点性能而设计的综合型基准测试程序，最早用Algol-60写成，后用Fortran改写。这是从英国国立物理实验室1970年时常用的数值计算程序中取出的最频繁使用的有代表性的程序段。这些程序段语句被转换到称之为Whetstone虚拟计算机上的指令，因而得名Whetstone基准程序。此基准程序既包括整数运算，又包括浮点运算，涉及到数组下标索引、子程序调用、参数传递、条件转移和三角/超越函数等，使用系统完成的Kwhetstone/s数来度量。

测试程序可访问Netlib/benchmark/whetstone

Dhrystone它主要为测试整数与逻辑运算性能而设计的综合型基准测试程序,用Ada、C和Pascal 写成,是一种CPU密集(CPU-intensive)型测试程序,由很多整型语句与逻辑语句的小循环组成。它使用系统完成的KDhrystone/s数来度量（注意VAX11/780 的性能为1.7KDhrystone/s,而VAX11/780 通常定义为1个 MIPS 性能标准,一个MIPS代表每秒 $1 0 ^ { 6 }$ 指令）。

测试程序可访问Netlib/benchmark/dhrystone

人们对Whetstone和Dhrystone这两个综合型基准程序的批评是，它们不能预测用户程序性能,这些基准程序的主要缺点是对编译程序比较敏感。

SPEC SPEC 是 Standard Performance Evaluation Cooperation 的 首字母缩写,它是作为 NCGA(National Computer Graphics Association)的一个小组于 20世纪80 年代创立,这个小组的创始者来源于Hewlett-Packard、DEC、MIPS 和Sun Microsystems,他们拥有一组基准测试程序以评测新机器的性能。第一组基准程序叫作 SPEC89,包含10个程序;SPEC92扩充至20个程序,6个整数程序和14个浮点程序分别称为 SPECint92和 SPECfp92。最近 SPEC又发布了一些新的基准测试程序（如 SPEC95、SPEChpc96、SPECweb96等）。SPEC 原主要是测试CPU性能的，现在强调开发能反映真实应用(如实际负载等)的基准测试程序,并已推广至客户/服务器计算、商业应用、I/O子系统等。

SPEC基准测试程序使用的单位是所测试机器执行性能与VAX11/780执行性能之比值。

# 3.3.2数学库测试程序

LinPACK自20世纪70年代中期以来,国际上曾开发过一批基于Fortran语言的求解线性代数方程组的子程序，于1979 年正式发布了LinPACK包。因为线性代数方程组在各个领域中应用甚广，所以该软件包就很自然地成为测试各种机器性能的测试程序。LinPACK测试的基准是用全精度64位字长的子程序求解100 阶线性方程组的速度,测试的结果以Mflops(每秒百万次浮点运算）作单位给出。LinPACK的测试报告由J.Dongarra经常更新发布(通常每月发布一次）。LinPACK 是使用 BLASI(Basic Algebra Subprograms1）的第一个线性代数软件包。BLAS1执行通常意义下的标量－向量运算(如标量乘向量、向量加、向量内积等),主要为向量计算机而设计的，它用Fortran77写成，但有些计算机商也提供汇编语言的BLAS1版本。

LAPACK尽管LinPACK作为测试程序现在仍很有生命力,但作为实际求解线性代数问题的软件包已经落伍了。所以1992年推出了代替LinPACK及EisPACK(特征值软件包)的LAPACK,它使用了数值线性代数中最新、最精确的算法，同时采用了将大型矩阵分解成小块矩阵的方法从而可有效地使用存储器。LAPACK 是建立在 BLAS1、BLAS2 和 BLAS3 基础上的,其中 BLAS2 执行矩阵－向量运算,BLAS3 执行矩阵-矩阵运算。

ScaLAPACK ScaLAPACK是LAPACK 的增强版,主要为可扩放的、分布存储的并行计算机而设计的。ScaLAPACK支持稠密和带状矩阵上各类操作，诸如乘法、转置和分解等。在国际上,ScaLAPACK例程可以加人多个并行算法，并且可根据数据分布、问题规模和机器大小选择这些算法，然而用户却不必关心这些细节。

# 3.3.3并行测试程序

NAS Parallel Benchmark(NPB） 它是 1991 年美国 NAS(Numerical Aero-dynamic Simulation)项目所开发的并行测试程序,其目的是为了比较各种并行机性能,有时也简称为NPB(NAS Parallel Benchmark)并行测试程序,系由8个程序组成,测试范围从整数排序到复杂的数值计算。测试结果以单处理机的CrayY-MP/1为单位(Class A)或 Cray C90/1为单位(ClassB)作比较。

NPB由5个核心程序组成： $\textcircled{1}$ EP(Embarrassingly Parallel):用于计算 Gauss伪随机数，因为它几乎不要求处理器之间相互通信，所以很适合于并行计算，而所测得的结果往往可以作为一个特定并行系统浮点计算性能可能达到的上限；$\textcircled { 2 } \mathrm { M G } ( \mathrm { M u l t i G r i d } )$ ：用4个V循环多重网格算法求解三维波松方程的离散周期近似解； $\textcircled{3} \textcircled { C }$ (ConjugateGradient)：用于求解大型稀疏对称正定矩阵的最小特征值的近似值,它表征了非结构风格计算和非规整远程通信计算类问题；④FT(Fast Fourier Transformation)：用于求解基于FFT谱分析法的三维偏微分方程，它也要求远程通信； $\textcircled{5}$ IS(Integer Sort)：用于基于桶排序的二维大整数排序,它要求大量的全交换通信。另外还有计算流体力学中3个模拟程序：①LU(LowerUpper Triangular)：用于基于对称超松弛法求解块稀疏方程组; $\textcircled{2}$ SP(Scalar Pen-ta-Diagonal)：用于求解5对角线方程组； $\textcircled{3}$ BT(Block Tri-Diagonal):用于求解3对角块方程组。

有关 NAS 并行基准程序的 WWW home Page 地址为:http://www.nas.nasa. gov/NAS/NPB/software/npbsoftware. html

PARKBENCH PARKBENCH(PARallel Kernels and BENCHmarks）是在1992年超级计算会议上确定的项目。与会者认为并行测试的重点应放在可扩放、分布存储、消息传递的体系结构上。主要目标是确定并行机用户与厂商双方都能接受的内容丰富的一批并行测试程序及标准，并把结果公布于网上,以减少不必要的重复工作。

现在的基准程序系为分布存储的多计算机编写，使用Fortran77加上PVM或MPI;为共享存储结构的Fortran90 和HPF版本的基准程序正在开发中。目前,PARKBENCH包括4类：①底层基准程序：测试一些基本结构参数，诸如算术运算速度、高速缓存和存储器速度、通信启动时间和带宽以及同步开销等；②核心基准程序：涉及到广泛的经常使用的科学计算子程序，诸如矩阵运算（稠密矩阵乘法、转置、LU分解、QR分解，矩阵三对角化等）、FFT运算、求解PDE 和NPB核基准程序等；③密集应用基准程序：目前仅包括谱变换、浅水（Shallow-

Water)模拟和3个NPB模似应用程序； $\textcircled{4}$ HPF编译基准程序：测试HPF编译器性能，主要集中在显式并行HPF结构的并行实现上。

PARKBENCH是个正在研究的课题，测试程序的内容尚未完全定型。目前所包含的核心测试程序主要来自 NPB。

# 3.4 小结和导读

小结本章仅讨论了并行计算的加速比、可扩放性和基准测试程序等基本性能评测问题。评价并行系统(并行计算)的性能指标还有其它一些。对于评价计算速度而言,就有算法(或程序)的执行时间，这对某些实时应用是很关键的；处理机每秒执行的指令数 MIPS(Million Instructions Persecond）、每秒执行的浮点运算数 FlOPS(Floating Point Operations Per Second);峰值速度 $R _ { \mathrm { p e a k } }$ （通常以Mflops/Gflops/Tflops/Pflops表示）、可达最大持续速度 $R _ { \operatorname* { m a x } }$ 。对于评价系统效率而言,就有效率(Efficiency) $E = S / _ { \mathcal { P } }$ ；利用率(Utility) $U = R _ { \mathrm { m a x } } / R _ { \mathrm { p e a k } }$ ;吞吐率（Throughput)W(即每秒执行的程序数，或单位时间内所能处理的作业数）。对于评价通信系统而言,就有通信容量(Capacity)、通信带宽(Bandwidth)和通信延迟(Latency)等。

此外,所介绍的基准测试程序大都限于科学和工程计算方面,其实在联机事务处理、商业计算、数据库等方面也有不少有名的基准测试程序。例如，TPC(Transaction Processing Council)基准程序就很流行,目前 TPC-A和 TPC-B已在1995年6月废弃，而TPC-C(测试事务处理价格/性能比）、TPC-D(测试决策支持系统)和TPC-E(测试大型企业支持计算环境的能力)在商业应用中广泛使用。

导读Amdahl加速定律最早描述在[12]中;Gustafson定律描述在[85]中；Sun和Ni加速定律描述在[170]中等效率标准是由Kumar等提出[112]；等速度标准是由Sun等提出[171];平均延迟标准由Zhang等提出[187];有关并行算法的可扩放性分析，读者可参阅[192],在那里还描述了很多其它的可扩放评判标准。有关计算机性能评价，[66]是篇很好的综述;LinPACK的使用手册，见[61]；LAPACK的使用手册，见[14];有关NAS并行基准程序，请见Ames研究中心报告[22]。最后读者可按下述WWW主页地址,在Internet上查阅到很多基准测试程序,它们还会给出程序的源代码和测试的结果：http://www.netlib.org/liblist . html。

# 习 题

3.1试讨论公式(3.4)、(3.8)和(3.11)三者的物理意义和相互关系。

3.2两个 $N \times N$ 阶的矩阵相乘，时间复杂度为 $T _ { 1 } = C N ^ { 3 } { \bf s }$ ,其中 $c$ 为常数；在 $\pmb { n }$ 节点的并行机上并行矩阵乘法的时间为 $T _ { n } = ( C N ^ { 3 } / n + b N ^ { 2 } / \sqrt { \ n } ) \mathbf { s } .$ 其中 $\pmb { b }$ 是另一常数,第一项代表计算时间，第二项代表通信开销；

$\textcircled{1}$ 试求固定负载时的加速并讨论其结果；  
$\textcircled{2}$ 试求固定时间时的加速并讨论其结果；  
$\textcircled{3}$ 试求存储受限时的加速并讨论其结果。

3.3试讨论本文所讲的三种加速定律的使用场合和它们的相互关系。

3.4试解释图3.8的物理意义。

3.5根据表3.1中的数据,试复算表3.3所有表项之值。

3.6试综合比较等效率、等速度和平均延迟三种可扩放性度量标准的异同点。

3.7试证明等效率、等速度和平均延迟三种可扩放性质量标准的相互等效性。

i.8用一台 $4 0 ~ \mathrm { M H z }$ 的处理机执行标准测试程序,它含的混合指令数和相应所需的时钟周期数如下：

<table><tr><td>指令类型</td><td>指令数</td><td>时钟周期数</td></tr><tr><td>整数运算</td><td>45 000</td><td>1</td></tr><tr><td>数据传送</td><td>32 000</td><td>2</td></tr><tr><td>浮点</td><td>15 000</td><td>2</td></tr><tr><td>控制传送</td><td>8000</td><td>2</td></tr></table>

试求有效每条指令执行的周期数CPI和每秒执行的指令数 ${ \bf M I P S } _ { \circ }$ 提示：令 $\pmb { \tau }$ 为时钟周期 $\bf ( n s )$ ， $f { = } 1 / \tau$ 为时钟频率( $\mathbf { \nabla } [ \mathbf { M H } \mathbf { z } )$ ， $T$ 为程序执行时的CPU时间， $I _ { \mathrm { c } }$ 为指令条数，C为程序执行的总周期数，则有 $T = I _ { \mathrm { c } } \times \mathrm { C P I } \times \tau$ 和 $\mathrm { M I P S } = { \frac { I _ { \mathrm { c } } } { T \times 1 0 ^ { 6 } } } = { \frac { f } { \mathrm { C P I } \times 1 0 ^ { 6 } } } =$ $\frac { f \times I _ { \mathrm { c } } } { \mathrm { C } \times 1 0 ^ { 6 } } ]$

3.9假定在一台 $4 0 ~ \mathrm { M F }$ 的处理机上运行200000条指令的目标代码，程序主要由4种指令组成,根据程序跟踪实验结果，已知指令混合比和每种指令所需周期数如下：

<table><tr><td>指令类型</td><td>CPI</td><td>指令混合比</td></tr><tr><td>算术和逻辑</td><td>1</td><td>60%</td></tr><tr><td>高速缓存命令中的加载/存放</td><td>2</td><td>18%</td></tr><tr><td>转移</td><td>4</td><td>12%</td></tr><tr><td>高速缓存缺失的存储访问</td><td>8</td><td>10%</td></tr></table>

$\textcircled{1}$ 计算在单处理机上用上述跟踪这些数据运行程序的平均CPI;  
$\textcircled{2}$ 根据 $\textcircled{1}$ 所得CPI,计算相应的MIPS速率。

3.10试分析行主编号的 $\sqrt { \pmb { p } } \times \sqrt { \pmb { p } }$ 网孔上 $\pmb { n }$ 点FFT算法的可扩放性。假定通信建立时间为$\pmb { t _ { s } }$ ，跨步延迟为 $t _ { \mathfrak { n } }$ ,传送单位信包的时间为 $\pmb { t _ { \mathrm { b } } }$ ,单位计算时间为 $\pmb { t _ { c 0 } }$

$\textcircled{1}$ 试计算处理器 $\mathrm { P } _ { i }$ 的通信跨步数hops；

$\textcircled{2}$ 试计算总的通信延迟 $T _ { \circ }$ ；

$\textcircled{3}$ 试计算等效率函数 $\begin{array} { r } { \mathbf { W } = f _ { \mathrm { E } } ( \mathbf { \Sigma } _ { \pmb { \phi } } ) } \end{array}$ 并加以讨论。[提示：对照FFT与网孔连接拓朴，可以发现处理器间的通信仅发生在同一行或同一列,且最大的通信 $h o p s = \sqrt { \ p } \cdot 2 _ { \circ } ]$

# 第二篇 并行算法的设计

第四章 并行算法的设计基础第五章 并行算法的一般设计方法第六章 并行算法的基本设计技术第七章 并行算法的一般设计过程

这一篇主要研究如何设计并行算法,包括并行算法的一般设计方法(第五章),并行算法的基本设计技术(第六章)和并行算法的一般设计过程(第七章)。而任何并行算法的设计都是基于某一特定的并行计算模型的，所以在本篇的开始,首先介绍了设计并行算法常用的并行计算模型,包括PRAM模型、APRAM模型、BSP模型、 $\mathrm { l o g P }$ 模型和 $\mathrm { C } ^ { 3 }$ 模型等。至于并行算法的具体实现(它主要涉及到并行程序设计),将放在本书的第四篇中讲述。

本篇第五章,将介绍并行算法的三种常用设计方法,包括“并行化"法（直接将一个串行算法并行化)，“全新"法(根据问题的特性,从头开始设计一个新的并行算法)和"借用"法(借用已知某类问题的现有算法,求解另一类与之有内在相似性的问题)。第六章,从利用并行处理技术最朴素的思想出发,介绍了算法设计的划分技术;从求解问题的方法和策略出发,介绍了算法设计的分治技术；从针对问题的特性出发,介绍了设计并行算法的平衡树法和倍增法;最后还介绍了基于重叠思想的并行处理技术中广泛使用的流水线设计技术。第七章,从设计方法学的角度,介绍如何从问题描述开始,逐步设计并行算法的全过程,包括任务划分、通信分析、任务组合和处理器映射等四个过程。它是实际设计一个并行算法的自然过程,其中前两个过程着重算法并发性和可扩放性的开拓；后两个过程着重优化算法的执行时间和均衡处理器的负载。

# 第四章 并行算法的设计基础

任何并行算法的设计都是基于某一特定的并行计算模型，而并行计算模型是从各种具体的并行机中抽象出来的，它能在一定程度上反映出具体并行机的属性，又可使算法研究不再局限于某一种具体的并行机。并行计算模型一般可分为抽象计算模型和实用计算模型。本章主要研究同步PRAM模型，异步APRAM模型,大同步BSP模型,异步LogP模型和粗粒度 $C ^ { 3 }$ 模型。但在讨论这些计算模型之前,先要简要地介绍一下并行算法的基础知识,包括并行算法的定义、分类，并行算法的表达，并行算法的复杂性度量以及并行算法中的同步和通信问题等。

# \*4.1 并行算法的基础知识

# 4.1.1并行算法的定义和分类

定义4.1 算法是解题方法的精确描述，是一组有穷的规则，它们规定了解决某一特定类型问题的一系列运算。

定义4.2 并行算法是一些可同时执行的诸进程的集合，这些进程互相作用和协调动作从而达到给定问题的求解。

并行算法可从不同的角度分类成数值计算的和非数值计算的并行算法；同步的、异步的和分布式的并行算法;共享存储的和分布存储的并行算法;确定的和随机的并行算法等等。

定义4.3数值计算是指基于代数关系运算的一类诸如矩阵运算、多项式求值、求解线性方程组等数字计算问题。求解数值计算问题的算法称为数值算法（Numerical Algorithm）。

定义4.4非数值计算是指基于比较关系运算的一类诸如排序、选择、搜索、匹配等符号处理问题。求解非数值计算问题的算法称为非数值算法（Non-numerical Algorithm）。

定义4.5 同步算法(Synchronized Algorithm)是指算法的诸进程的执行必须相互等待的一类并行算法。

定义4.6 异步算法(Asynchronized Algorithm)是指算法的诸进程的执行不必相互等待的一类并行算法。

定义4.7 分布算法(Distributed Algorithm)是指由通信链路连接的多个场点(Site)或节点,协同完成问题求解的一类并行算法。

按照上述意义,在局网环境下进行的计算称为分布计算(Distributed Com-puting)。在 Internet 流行的今天,可把工作站机群 COW(Cluster of Worksta-tions)环境下进行的计算称为网络计算(Network Computing)。推而广之,有人把基于Internet 的计算则称为元计算(Metacomputing)。

定义4.8 确定算法(Deterministic Algorithm)是指算法的每一步都能明确地指明下一步应该如何行进的一种算法。

定义4.9 随机算法(Randomized Algorithm)是指算法的每一步,随机地从指定范围内选取若干参数,由其来确定算法的下一步走向的一种算法。

# 4.1.2并行算法的表达

描述一个算法,可以使用自然语言进行物理描述;也可使用某种程序设计语言进行形式化描述。语言的选用，应避免二义性,且力图直观、易懂而不苛求严格的语法格式。像描述串行算法所选用的语言一样,类-Algol、Pidgin-Algol、类-Pascal等语言均可选用。在这些语言中,允许使用任何类型的数学描述,通常也无数据类型的说明部分，但只要需要，任何数据类型都可引进。

在描述并行算法时,所有描述串行算法的语句及过程调用等均可使用，而只是为了表达并行性而引人几条并行语句：

par-do语句当算法的若干步要并行执行时,我们可使用“Do in paralel"语句,简记之为"par-do"进行描述：

其中"end for"也可代之以"odrap”。

for all语句当几个处理器同时执行相同的操作时,可以使用“forall"语句描述之：

for all $\mathbf { P } _ { i }$ , where $0 { \leqslant } i { \leqslant } k$ do

end for

注意，为了算法书写简洁,在意义明确的前提下,参数类型总是省去,同时语句括弧"begin...end"的使用也比较随便。

# 4.1.3并行算法的复杂性度量

复杂度的渐近表示对算法进行分析时，常使用上界（Upper Bound）、下界（Lower Bound)和紧致界(Tightly Bound)的概念,现分别定义如下：

定义4.10令 $f ( n )$ 和 ${ \pmb g } ( { \pmb n } )$ 是定义在自然数集合 $N$ 上的两个函数,如存在两个正常数 $c$ 和 $\pmb { n _ { 0 } }$ ,使得对于所有 $n \geqslant n _ { 0 }$ 均有 $f ( n ) { \leqslant } c g \left( n \right)$ ,则称 ${ \pmb g } ^ { \prime } ( { \pmb n } )$ 是$f ( n )$ 的一个上界,记作 $f ( n ) = O ( g ( n ) )$ 。

定义 4.11 $f ( n )$ 和 $\mathbf { \delta } _ { g } ( { \boldsymbol { \mathbf { \mathit { n } } } } )$ 定义如上,如存在两个正常数 $c$ 和 $\pmb { n _ { 0 } }$ ,使得对于所有 $n \geqslant n _ { 0 }$ 均有 $f ( n ) { \ggeq } c g \left( n \right)$ ，则称 ${ \pmb g } ( { \pmb n } )$ 是 $f ( n )$ 的一个下界，记作 $f ( n ) =$ $\Omega ( \boldsymbol { g } ( \boldsymbol { n } ) )$ 。

定义4.12 $f ( n )$ 和 ${ \pmb g } ( { \pmb n } )$ 定义如上,如存在正常数 $c _ { 1 } 、 c _ { 2 }$ 和 $\pmb { n _ { 0 } }$ ,使得对于所有 $n { \geqslant } n _ { 0 }$ 均有 $c _ { 1 } g ( n ) { \leqslant } f ( n ) { \leqslant } c _ { 2 } g ( n )$ ,则称 ${ \pmb g } ( { \pmb n } )$ 是 $\scriptstyle f ( n )$ 的一个紧致界，记作 $f ( n ) = \Theta ( g ( n ) )$ 。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/42f14de528e17c4772beb36f1ee025c34b6dcc643afce5b8fb7af13b8af1b6dc.jpg)  
图4.1给出了上界、下界和紧致界的几何解释。  
图4.1上界(a)、下界(b)和紧致界(c)的几何解释

并行算法的复杂性度量在分析算法时,如果对算法的所有输入分析其平均性态时的复杂度则称之为期望复杂度(Expected Complexity),为此往往需要对输人的分布作某种假定,这在大多数情况下并非容易。所以感兴趣的是分析在某些输人时,使得算法的时、空复杂度呈现最坏情况下的算法复杂度,称之为最坏情况下的复杂度(Worst-Case Complexity）。

在分析并行算法时,通常要分析如下几个指标：

$\textcircled{1}$ 运行时间 $t ( n )$ ：运行时间就是算法运行在给定模型上求解问题所需的时间(它主要是输入规模n的函数),通常包含计算时间和通信时间,分别用计算时间步和选路时间步作单位。

$\textcircled{2}$ 处理器数 ${ \pmb { \hat { p } } } ( { \pmb { \hat { n } } } )$ ：它是求解给定问题所用的处理器数目,通常取 ${ \pmb { \phi } } ( { \pmb { n } } ) =$

$n ^ { 1 - \varepsilon } , 0 < \varepsilon < 1$ 是常见的。

$\textcircled{3}$ 并行算法的成本 $c ( n )$ ：它定义为并行算法的运行时间 $t ( n )$ 与其所需的处理器数 ${ \pmb { \mathscr { p } } } ^ { \prime } ( { \pmb { \mathscr { n } } } )$ 之乘积，即 $c ( \boldsymbol { n } ) = \boldsymbol { t } \left( \boldsymbol { n } \right) \cdot \boldsymbol { p } ( \boldsymbol { n } ) ,$

定义4.13如果求解一个问题的并行算法之成本,在数量级上等于最坏情况下串行求解此问题所需的执行步数，则称此并行算法是成本最优的。

$\textcircled{4}$ 总运算量 $\mathbf { \boldsymbol { W } } ( \boldsymbol { n } )$ ：即并行算法所完成的总的操作数量。此时我们并不关心也不必指明算法使用了多少台处理器。当给定了并行系统中的处理器数时，就可使用下述Brent 定理计算出相应的运行时间。

Brent定理令 $\mathbf { { \cal { W } } } ( n )$ 是某并行算法 $\pmb { A }$ 在运行时间 $T ( n )$ 内所执行的运算量,则 $A$ 使用 $\pmb { \mathscr { P } }$ 台处理器可在 $t ( n ) = O ( W ( n ) / p + T ( n ) )$ 时间内执行完毕。

$\textrm { \textbf { W } } ( \mathbf { \mu } _ { n } )$ 和 $c ( \pmb { n } )$ 密切相关。按照成本之定义和Brent定理，则有 $c \left( \varkappa \right) =$ $t ( n ) \cdot p = O ( \mathbf { \nabla } W ( n ) + p \cdot T ( n ) )$ 当 ${ \pmb { \phi } } = O ( { \pmb W } ( { \pmb n } ) / T ( { \pmb n } ) )$ 时， $\boldsymbol { W } ( n )$ 和 $c ( \pmb { n } )$ 两者是渐近一致的;而对于任意的 $\pmb { \hat { p } }$ ，则 $c ( n ) > W ( n )$ 。这说明一个算法在运行过程中，不一定都能充分地利用有效的处理器去工作。

# 4.1.4并行算法中的同步与通信

同步同步是在时间上强使各执行进程在某一点必须相互等待。在并行算法的各进程异步执行过程中,为了确保各处理器的正确工作顺序以及对共享可写数据的正确访问(互斥访问),程序员需在算法的适当点设置同步点。同步可用软件、硬件和固件的办法来实现。下面以MIMD-SM多处理器系统中 $\pmb { n }$ 个数的求和为例,说明如何用同步语句 $\mathbf { l o c k }$ 和unlock来确保对共享可写数据的互斥访问。假定系统中有p个处理器P,,Pp-1;输人数组A=(ao,,an-1)存放在共享存储器中;全局变量用于存放结果;局部变量L包含各处理器计算的子和;lock和unlock语句执行在临界区,加锁是个原子操作;在for循环中各进程异步地执行各语句,并结束在"endfor”。

# 算法4.1 共享存储多处理器上求和算法

输入： $A = \left( a _ { 0 } , \cdots , a _ { n - 1 } \right)$ ,处理器数 $\pmb { \mathscr { P } }$

输出： $S = \textstyle \sum a _ { i }$

# Begin

(1) $S = 0$   
(2） for all $\mathrm { P } _ { i }$ where $\scriptstyle 0 \leqslant i \leqslant j - 1$ do(2.1) $L = 0$ (2.2) for $j = i$ to $\pmb { n }$ step $\pmb { \mathscr { P } }$ do$L = L + a _ { j }$

end for(2.3) lock(S)$S = S + L$ (2.4） unlock（S)end for

End

通信通信是在空间上对各并发执行的进程施行数据交换。通信可使用通信原语来表达：在共享存储的多处理器中,可使用global read(X,Y)和globalwrite( $U , V )$ 来交换数据，前者将全局存储器中数据 $X$ 读人局部变量 $Y$ 中，后者将局部数据 $U$ 写人共享存储变量 $\boldsymbol { v }$ 中;在分布存储的多计算机中,可使用 send$( X , i )$ 和 receive( $\mathbf { \delta } _ { Y , j } )$ 来交换数据，前者是处理器发送数据 $\pmb { X }$ 给 $\mathbf { { P } } _ { i }$ ,后者是处理器从 $\mathrm { \bf P } _ { j }$ 接收数据 $\mathbf { r }$ 。下面以MIMD-DM多计算机系统中矩阵向量乘法为例说明之。假定分布式连接拓扑为环。矩阵A和向量X划分成p块;A=（A1，$\cdots , A _ { \phi } )$ 和 $\mathbf X = ( \ v x _ { 1 } , \cdots , \ v x _ { \phi } )$ ,其中 $\pmb { A } _ { i }$ 的大小为 ${ \pmb n } \times { \pmb r } , { \pmb x } _ { i }$ 的大小为 $r$ 。假定有 $\pmb { \hat { p } }$ $\leqslant n$ 个处理器, $r = n / \phi$ 为一整数。为了计算 $\mathbf { \mu } _ { \mathbf { y } } = \mathbf { \nabla } _ { \mathbf { A } } \mathbf { X }$ ，先由处理器 $_ i$ 计算 $\textstyle z _ { i } =$ $\mathbf { A } _ { i } x _ { i }$ $( 1 { \leqslant } i { \leqslant } p )$ ,再累加求和 $z _ { 1 } + \cdots + z _ { p } ,$ ，如果 $\mathbf { P } _ { i }$ 开始在其局存中保存 $\pmb { B } =$ $\mathbf { A } _ { i }$ 和 ${ \boldsymbol { \mathbf { \mathit { w } } } } = { \boldsymbol { \mathbf { \mathit { x } } } } _ { i }$ （则 $( 1 { \leqslant } i { \leqslant } p ) .$ ),则各处理器可局部计算乘积 $\pmb { { \cal B } } \mathbf { w } _ { i }$ ；然后采用在环中顺时针循环部分和的方法将这些向量累加起来;最终输出向量保存在P中。对于每个处理器都执行如下算法：

# 算法4.2 分布存储多计算机上矩阵向量乘算法

输入：处理器数 $\pmb { \phi }$ ,第 $_ i$ 个大小为 $\pmb { n } \times \pmb { r }$ 的子矩阵 $B = A \left( 1 \colon n , \left( i - 1 \right) r + 1 \right.$ $: i r )$ ,其中 $\gamma = { \mathfrak { n } } / { \mathfrak { p } }$ ；第 $_ i$ 个大小为 $\boldsymbol { r }$ 的子向量 ${ \pmb w } = x \big ( \big ( i - 1 \big ) r + 1$ ：$_ { i r }$ ）。

输出： $\mathbf { P } _ { i }$ 计算 $\mathbf { y } = \pmb { A } _ { 1 } x _ { 1 } + \cdots + \pmb { A } _ { i } x _ { i }$ ,并向右传送此结果;算法结束时， ${ \bf P } _ { 1 }$ 保存乘积 $\pmb { A } \pmb { X }$ 。

# Begin

(1） Compute $\boldsymbol { z } = \boldsymbol { B } \boldsymbol { w }$   
(2) if $i = 1$ then $y _ { i } = 0$ else receive $( y , l e f t )$ endif   
(3) $y = y + z$   
(4） send $( y , r i g h t )$   
(5) if $i = 1$ then receive $( y , l e f t )$ endif

End

# 4.2 并行计算模型

所谓计算模型实际上就是硬件和软件之间的一种桥梁，使用它能够设计分析算法，在其上高级语言能被有效地编译且能够用硬件来实现。在串行计算时，冯·诺依曼机就是一个理想的串行计算模型,在此模型上硬件设计者可设计多种多样的冯·诺依曼机而无须虑及被执行的软件；而软件工程师能够编写各种可在此模型上有效执行的程序而无须考虑所使用的硬件。但在并行计算时,尚未有一个类似于冯·诺依曼机的真正通用的并行计算模型。现在流行的计算模型要么过于简单、抽象(如PRAM);要么过于专用(如互连网络模型和VLSI计算模型)。因而急需发展一种更为实用、能够较真实反映现代并行机性能的并行计算模型。本节先简要讨论一下PRAM模型；然后分别介绍异步PRAM模型、BSP模型、logP模型和 ${ \bf C } ^ { 3 }$ 模型；最后对 BSP和logP进行了评注。

# 4.2.1 PRAM模型

PRAM模型描述 PRAM(Parallel Random Access Machine)模型,即并行随机存取机器,也称之为共享存储的 SIMD模型,是一种抽象的并行计算模型。在这种模型中，假定存在着一个容量无限大的共享存储器;有有限或无限个功能相同的处理器,且其均具有简单的算术运算和逻辑判断功能;在任何时刻各处理器均可通过共享存储单元相互交换数据。根据处理器对共享存储单元同时读、同时写的限制,PRAM模型又可分为： $\textcircled{1}$ 不允许同时读和同时写（Exclusive-Readand Exclusive-Write)的 PRAM模型,简记之为PRAM-EREW; $\textcircled{2}$ 允许同时读但不允许同时写(Concurrent-Read and Exclusive-Write)的 PRAM模型,简记之为PRAM-CREW。③允许同时读和同时写（Concurrent-Read and Concurrent-Write)的PRAM模型,简记之为PRAM-CRCW。显然,允许同时写是不现实的，于是又对PRAM-CRCW模型作了进一步的约定：①只允许所有的处理器同时写相同的数,此时称为公共(Common)的PRAM-CRCW,简记之为CPRAM-CR-CW;②只允许最优先的处理器先写，此时称为优先(Priority)的PRAM-CRCW，简记之为PPRAM-CRCW;③允许任意处理器自由写，此时称为任意(Arbitrary）的PRAM-CRCW,简记之为APRAM-CRCW。上述模型中,PRAM-EREW是最弱的计算模型,而PRAM-CRCW是最强的计算模型。令Tm表示某一并行算法在并行计算模型 $\mathbf { M }$ 上的运行时间,则

$$
T _ { \mathrm { E R E W } } { \geq } T _ { \mathrm { C R E W } } { \geq } T _ { \mathrm { C R C W } }
$$

$$
T _ { \mathrm { E R E W } } = O ( \ T _ { \mathrm { C R E W } } \cdot \log p ) = O ( \ T _ { \mathrm { C R C W } } \cdot \log p )
$$

其中, $\pmb { \mathscr { P } }$ 为处理器的数目。（4.2)式的含义是,一个具有时间复杂度为TcREw或TcRcw的算法,可在PRAM-EREW模型上花费 $\log p$ 倍时间模拟实现之。

PRAM模型优点著名的PRAM模型有很多优点：它特别适合于并行算法的表达、分析和比较;使用简单,很多诸如处理器间通信、存储管理和进程同步等并行机的低级细节均隐含于模型中;易于设计算法和稍加修改便可运行在不同的并行机上;且有可能在PRAM模型中加人一些诸如同步和通信等需要考虑的问题。

PRAM模型缺点PRAM是一个同步模型,这就意味着所有的指令均按锁步方式操作，用户虽感觉不到同步的存在,但它的确是很费时的;共享单一存储器的假定,显然不适合于分布存储的异步的MIMD机器;假定每个处理器均可在单位时间内访问任何存储单元而略去存取竞争和有限带宽等是不现实的。

PRAM模型推广随着人们对PRAM的理解深化,在使用它的过程中也对其做了若干推广,主要的有存储竞争模型,它将存储器分成一些模块,每个模块一次均可处理一个访问，从而可在模块级处理存储器的竞争;延迟模型,它考虑了信息的产生和能够使用之间的通信延迟；局部PRAM模型,此模型考虑到了通信带宽，它假定每个处理器均有无限的局存,而访问全局存储器是较昂贵的；分层存储模型,它将存储器视为分层的存储模块,每个模块由其大小和传送时间表征,多处理机由模块树表示,叶为处理器;异步PRAM模型,它是下一节我们要专门讨论的模型。

尽管PRAM模型是很不实际的并行计算模型,但在目前算法界仍被广泛使用,且被普遍地接受下来,特别是算法理论研究者非常喜欢它。

# 4.2.2异步 PRAM模型

模型特点 分相(Phase)PRAM模型是一个异步的 PRAM模型,简记之为APRAM,系由 $\pmb { \mathscr { P } }$ 个处理器组成，其特点是每个处理器都有其局存、局部时钟和局部程序;处理器间的通信经过共享全局存储器;无全局时钟,各处理器异步地独立执行各自的指令;处理器任何时间依赖关系需明确地在各处理器的程序中加人同步(路)障(Synchronization Barrier);一条指令可在非确定(无界)但有限的时间内完成。

APRAM模型中的指令类型APRAM模型中有四类指令： $\textcircled{1}$ 全局读：将全局存储单元中的内容读人局存单元中；②局部操作：对局存中的数执行操作，其结果存人局存中；③全局写：将局存单元中的内容写人全局存储单元中;④同步：同步是计算中的一个逻辑点,在该点各处理器均需等待别的处理器到达后才能继续执行其局部程序。

APRAM模型中的计算在APRAM中,计算系由一系列用同步障分开的全局相所组成。如图4.2所示，在各全局相内，每个处理器异步地运行其局部程序；每个局部程序中的最后一条指令是一条同步障指令；各处理器均可异步地读取和写入全局存储器,但在同一相内不允许两个处理器访问同一单元。正是因为不同的处理器访问存储单元总是由一同步障所分开,所以指令完成的时间上的差异并不影响整个计算。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/4b9a8dbafaba1acdbd63a4a145e77b47fce1d031490f6d42f687364ce5dac0f1.jpg)  
图4.2APRAM中的异步计算, $\star$ 表示局部操作

APRAM模型中的时间计算使用 APRAM模型计算算法的时间复杂度时,假定局部操作取单位时间；全局读／写时间为d,它定量化了通信延迟,代表读／写全局存储器的平均时间,d随机器中的处理器增加而增加;同步障的时间为 $B$ ,它是处理器数 $\pmb { \mathscr { P } }$ 的非降函数 $B = B ( { \boldsymbol { \mathbf { \rho } } } _ { \beta } )$ 。在APRAM中假定上述参数服从如下关系：

$$
2 { \leqslant } d { \leqslant } B { \leqslant } p
$$

同时 $B { \big ( } \phi { \big ) } \in O { \big ( } d \log \phi { \big ) }$ 或 $B ( \phi ) \in O ( d \log \phi / \log d )$ 。令 $t _ { p \mathbf { h } }$ 为全局相内各处理器指令执行时间中最长者，则整个程序运行时间T为各相的时间之和加上B乘以同步障次数,即

总之，APRAM模型比起PRAM来更接近于实际的并行机;且保留了PRAM编程的简捷性;由于使用了同步障,所以不管各处理器遭到的延迟多长，程序必定是正确的;且因为APRAM模型中的成本参数是定量化的,所以算法的分析也是不难的。

# 4.2.3BSP模型

BSP模型的基本参数 BSP(Bulk Synchronous Parallel)模型,字面的含义是“大"同步模型(相应地,APRAM模型也叫作"轻量"同步模型),早期最简单的版本叫作XPRAM模型,它是作为计算机语言和体系结构之间的桥梁,并以下述三个参数描述的分布存储的多计算机模型： $\textcircled{1}$ 处理器/存储器模块（下文也简称为处理器）； $\textcircled{2}$ 施行处理器/存储器模块对之间点到点传递消息的选路器； $\textcircled{3}$ 执行以时间间隔 $L$ 为周期的所谓路障同步器。所以BSP模型将并行机的特性抽象为三个定量参数 $\phi , g , L$ ,分别对应于处理器数、选路器吞吐率(亦称带宽因子）、全局同步之间的时间间隔。

BSP 模型中的计算在BSP模型中,计算系由一系列用全局同步分开的周期为 $L$ 的超级步(Superstep)所组成。在各超级步中,每个处理器均执行局部计算,并通过选路器接收和发送消息;然后作一全局检查,以确定该超级步是否已由所有的处理器完成：若是,则前进到下一超级步,否则下一个 $L$ 周期被分配给未曾完成的超级步。

BSP模型的性质和特点 BSP模型是个分布存储的MIMD计算模型,其特点是： $\textcircled{1}$ 它将处理器和选路器分开，强调了计算任务和通信任务的分开，而选路器仅施行点到点的消息传递，不提供组合、复制或广播等功能，这样做既掩盖了具体的互连网络拓扑，又简化了通信协议； $\textcircled{2}$ 采用路障方式的以硬件实现的全局同步是在可控的粗粒度级,从而提供了执行紧耦合同步式并行算法的有效方式，而程序员并无过分的负担； $\textcircled{3}$ 在分析BSP模型的性能时，假定局部操作可在一个时间步内完成,而在每一超级步中,一个处理器至多发送或接收 $h$ 条消息（称为h-relation)。假定 $\pmb { \mathscr { s } }$ 是传输建立时间,所以传送 $h$ 条消息的时间为 $g h + s$ ,如果 $_ { g h } \geqslant 2 s$ ,则 $L$ 至少应 $\geqslant g h$ 。很清楚,硬件可将 $L$ 设置尽量小（例如使用流水线或宽的通信带宽使 $\pmb { g }$ 尽量小),而软件可以设置 $L$ 之上限(因为 $L$ 愈大，并行粒度愈大)。在实际使用中， $\pmb { g }$ 可定义为每秒处理器所能完成的局部计算数目与每秒选路器所能传输的数据量之比。如果能合适地平衡计算和通信，则BSP模型在可编程性方面具有主要的优点,而直接在BSP模型上执行算法(不是自动地编译它们),此优点将随着 $\pmb { g }$ 的增加而更加明显； $\textcircled{4}$ 为PRAM模型所设计的算法,均可采用在每个BSP处理器上模拟一些PRAM处理器的方法实现之。理论分析证明,这种模拟在常数因子范围内是最佳的，只要并行宽松度（ParallelSlackness),即每个BSP处理器所能模拟的PRAM处理器的数目足够大。在并发情况下,多个处理器同时访问分布式的存储器会引起一些问题,但使用散列方法可使程序均匀地访问分布式存储器。在PRAM-EREW情况下，如果所选用的散列函数足够有效，则L至少是对数的,于是模拟可达最佳,这是因为我们欲在p个物理处理器的BSP模型上,模拟u≥plogp个虚拟处理器,可将u/p≥$\log \phi$ 个虚拟处理器分配给每个物理处理器。在一个超级步内， $_ { v }$ 次存取请求可均匀摊开，每个处理器大约u/p次，因此机器执行本次超级步的最佳时间为

$O ( v / p )$ ,且概率是高的。同样,在 $_ { v }$ 个处理器的PRAM-CRCW模型中,能够在$\boldsymbol { \mathscr { P } }$ 个处理器（如果 $v = \boldsymbol { \phi } ^ { 1 + \epsilon } , \epsilon > 0 )$ ,和 $L \geqslant \log \phi$ 的 BSP模型上用 $O ( v / \phi )$ 的时间也可达到最佳模拟。

对 BSP模型的评注 $\textcircled{1}$ 在并行计算时，Valiant试图也为软件和硬件之间架起一座类似于冯·诺依曼机的桥梁，他论证了BSP模型可以起到这样的作用,正是因为如此,BSP模型也常叫作桥模型; $\textcircled{2}$ 一般而言，分布存储的MIMD模型编程能力均较差,但在 BSP模型中,如果 计算和通信可合适的平衡(例如 $g = 1 \AA$ ），则它在可编程方面呈现出主要的优点； $\textcircled{3}$ 在 BSP模型上,曾直接实现了一些重要的算法(如矩阵乘、并行前缀运算、FFT和排序等),它们均避免了自动存储管理的额外开销； $\textcircled{4} \textcircled { 1 } \textcircled { < } \textcircled { 2 }$ 模型可有效地在超立方网络和光交叉开关互连技术上实现,呈现出该模型与特定的工艺技术无关,只要选路器有一定的通信吞吐率； $\textcircled{5}$ 在 BSP模型中,超级步的长度必须能充分地适应任意的h-relation,这一点是人们最不喜欢的; $\textcircled{6}$ 在BSP模型中,在超级步开始发送的消息,即使网络延迟时间比超级步的长度短,它也只能在下一个超级步才能使用； $\textcircled{7}$ BSP模型中的全局路障同步假定是用特殊的硬件支持的,这在很多并行机中可能没有相应的现成的硬件机构； $\textcircled{8}$ Valiant所提出的编程模拟环境，在算法模拟时的常数可能不是很小的,如果考虑到进程间的切换(可能不仅要设置寄存器，而且可能还有部分高速缓存)则此常数可能很大。

# 4.2.4 logP模型

logP模型提出的背景 $\textcircled{1}$ 根据技术发展的趋势：20世纪90年代末和未来的并行机发展的主流之一是巨量并行机,即MPC（MassivelyParallel Comput-ers),它系由成千个功能强大的处理器/存储器节点,通过受限带宽的和可观延迟的互连网络所构成。所以我们建立并行计算模型应充分考虑此情况，这样基于此模型的并行算法才能在现有和未来的并行机上有效运行；②根据已有的编程经验：现有的共享存储、消息传递和数据并行等编程风范都很流行，但尚无一个公认的和占支配地位的编程方式，因此应寻求一种与上述任一特定编程风格无关的计算模型;③根据现有的理论模型：共享存储PRAM模型和互连网络的SIMD模型作为开发并行算法还不够合适,因为它们既未包含分布存储的情况,也未考虑通信同步等实际因素，从而也不能精确地反映运行在真实并行机上的算法的性态。所以在此背景下，一个以MPC为背景的新计算模型，即logP 模型,便由D.Culler等人提出了。

logP模型的参数logP模型是一种分布存储的、点到点通信的多处理机模型,其中通信网络由一组参数来描述，但它并不涉及到具体的网络结构,也不假定算法一定要用显式的消息传递操作进行描述。很凑巧,logP恰好是以下几个定量参数的拼写，其中，①L(Latency)表示在网络中消息从源到目的地所遭到的延退； $\textcircled { 2 } \textcircled { \scriptsize { \times } } ( \textcircled { \scriptsize { \times } } \mathbf { v e r h e a d } )$ 表示处理器发送或接收一条消息所需的额外开销（包含操作系统核心开销和网络软件开销),在此期间内它不能进行其它的操作； $\textcircled{3} \textcircled { 8 }$ $\left( \mathsf { G a p } \right)$ 表示处理器可连续进行消息发送或接收的最小时间间隔； $\textcircled{4} \textcircled{4}$ (Processor)表示处理器/存储器模块数。很显然， $\pmb { g }$ 的倒数相应于处理器的通信带宽；而 $L$ 和 $\pmb { g }$ 反映了通信网络的容量。 $L , o$ 和 $\pmb { g }$ 都可以表示成处理器周期（假定一个周期完成一次局部操作，并定义为一个时间单位)的整倍数。

对logP模型的论证 $\textcircled { 1 } \log \tt { P }$ 模型充分揭示了分布存储并行机的性能瓶颈，用 $L \setminus o$ 和 $\pmb { g }$ 三个参数刻画了通信网络的特性，但却屏蔽了网络拓扑、选路算法和通信协议等具体细节。本质上讲,通信网络是一个启动率为 $\pmb { g }$ 、延迟为 $L$ 、端点处理器开销各为零的流水线部件；网络的容量假定是有限的，在任何时刻至多只能有 $L / g$ 条消息从一个处理器传到另一个处理器，且任何消息均可在有限但非确定的时间内到达目的地;在网络容限范围内,点到点的传输一条消息的时间为 $2 \cdot \bullet + L$ ； $\textcircled{2}$ 尽管拓扑结构对网络性能影响很大，但 $\scriptstyle \log \mathbf { P }$ 模型在计算通信时间时却屏蔽了这一点,这是因为通过上千个节点的网络(如超立方、蝶形网、网孔、胖树等)的平均距离分析,发现它们的差别仅为2倍,而这种差别对整个消息传输时间的影响是很小的;③对于一个具体的并行机，由通道带宽为w、经过H个跨步(Hops)的网络传送一个M位的消息所花的时间为T(M,H)=Tsend+「M/w]+H·r+Trev,其中Tsend为发送开销，即第一位数据被送上网络之前处理器为网络接口准备数据的时间；Trev为接收开销，即从最后一位数据到达直到接收处理器用此数据进行处理的时间；M/w1为将消息的最后一位送到网上所需的时间;H·r是最后一位数据通过网络达到目的节点的时间（r为中继节点的时延）。对于logP而言,合理的参数选取是:o=（Tsend+Trev)/2,L=H·r+「M/w],g=「M/b7(b为处理器对剖宽度)。此处,通过对具有上千个处理器的典型并行机的测试和分析，发现在网络空载或轻载时·T(M,H)中起主导作用的是 $T _ { \mathrm { s e n d } }$ 和 $T _ { r e v }$ (这就意味着通信接口部件对系统性能影响更大),而它们对网络和结构却不敏感。但是如果网络重载时就会出现竞争资源的现象，从而等待时间将迅速增加，正是因为如此，logP模型对网络的容量加以了限制；④在logP模型中，假定每个节点只有一个处理器，它既用于计算又负责接收和发送消息，所以为了发送或接收一个字处理器均要付出开销o。对于长的消息，某些并行机提供了专门的硬件支持，但这样作充其量也只不过能使每个节点的性能提高一倍。所以在logP模型中对长消息不作特别处理;③尽管在某些并行机中，使用了特殊的硬件支持数据的广播、前缀运算或全局同步等，但logP模型中必须通过隐含地发送消息来执行这些操作,因为用硬件完成这些操作，其功能是受到了限制的（例如它们可能只对整数有效而对浮点数则不行)。此外，对于logP模型设计算法时最普通的全局操作是路障，它是一种由硬件支持的原语操作。用硬件支持这一操作比对全局数据进行操作要简单，而且路障作为原语的优点是假定处理器以同步方式退出路障可简化算法的分析； $\textcircled{6}$ 在 $\scriptstyle \log \mathbf { P }$ 模型中使用了无竞争的通信模式，因为用这种模式重复传输时可以利用整个带宽,反之其它的通信模式往往依赖于选路算法、路由缓冲器数和互连拓扑结构，而 $\mathrm { l o g P }$ 模型将网络的内部结构抽象成了几个性能参数,它就不能区别互连结构的优劣了。logP模型能够反映各种通信模式的一种可能的推广方式是提供多种 $\pmb { g }$ ,对于特定的通信模式可以采用适当的 $\pmb { g }$ 进行算法分析； $\textcircled{7}$ 在 $\scriptstyle \log \mathbf { P }$ 模型中提倡使用多线程(Multithreading)技术来屏蔽网络延迟(但此技术受通信带宽和进程切换开销的限制）。

对logP模型的评注 $\textcircled { 1 } \log \tt { P }$ 模型将现代和将来的并行机的特性进行了精确的综合，以少量的参数 $L , o , g$ 和 $\pmb { \hat { p } }$ 刻画了并行机的主要瓶颈。这个模型的详尽程度足以反映了并行算法设计时的主要实际问题，而其简捷性也足以支持详细的算法分析。对于那些非平易的算法，用这种比较复杂的模型（显然比PRAM复杂得多)来分析时仍是可操作的，因为这些参数的重要程度在不同的环境下是不同的，往往可以略去其中的一个或几个参数而使模型更简单一些； $\textcircled{2}$ logP 模型无须说明编程风格或通信协议,它可以等同地用于共享存储、消息传递和数据并行等各种风范； $\textcircled { 3 } \log \textcircled { 2 }$ 模型的可用性已由诸如播送、求和、FFT、LU分解、排序、图的连通性等算法得以证实，并且它们都已在CM-5机器上加以实现； $\textcircled{4}$ 事实上,如果使 $\scriptstyle \log \mathbf { P }$ 模型中的参数 $g = 0 , L = 0$ 和 ${ \pmb o } = { \bf 0 }$ ，则 $\scriptstyle \log \mathbf { P }$ 就等同于PRAM;同时logP模型也是BSP模型的改进和细化：例如在一个超级步中并非要所有的处理器都发送或接收h条那么多的消息；在一个超级步中消息一旦到达处理器就可立即使用它，而不必像BSP那样一定要等到下一个超级步；logP模型全部采用消息同步而不像BSP那样要用专门的硬件支持。总之，尽管logP模型的可用性还有待于用大量的算法实例进一步证实，但它毕竟打开了研究模型的新途径，它不仅为算法设计者提供了设计适合于近代并行机的巨量并行算法的手段，而且对设计并行机体系结构也提供了指导性意见。

# 4.2.5 $\mathbf { C } ^ { 3 }$ 模型

动机与背景 ①C³（Computation,Communication,Congestion）模型是一个与体系结构无关的粗粒度的并行计算模型，它同时也考虑了由工作站或高档微机组成的高性能可扩放的并行机群系统为目标，旨在能反映计算复杂度、通信模式和通信期间潜在的拥挤诸因素对粗粒度网络算法的影响;②在粗粒度机器上，并行算法的性能非常敏感于通信模式,而前述的BSP和logP模型都只采用点到点的消息传递来进行通信，复杂的通信操作系由编程实现，这无疑加重了程序员的负担。而 $\mathrm { C } ^ { 3 }$ 模型强调用公用的通信操作来开发粗粒度的并行算法； $\textcircled{3}$ 以前所提出的模型,均未反映通信操作中所引起的潜在拥挤，而 ${ \bf C } ^ { 3 }$ 模型却考虑到了网络链路拥挤和处理器拥挤对并行算法性能的影响。

$C ^ { 3 }$ 模型中的计算在 $C ^ { 3 }$ 模型中，和BSP与 $\scriptstyle \log \bar { P }$ 相似,计算可划分为一系列超级步；同步出现在两超级步之间且用路障同步机构实现之；在每个超级步内施行局部计算继之以发送/接收消息；一个超级步的时间由所完成的计算单位数和通信单位数来度量，其中计算单位数取决于所作的局部计算量，而通信单位数取决于处理器所发送的数据量、处理器所接收的数据量、消息的传输延迟和处理器间超容限通信所引起的拥挤；在分析算法的时间复杂度时,必须累加每一个超级步中的计算和通信单位数,所有超级步中的总计算单位数与通信单位数之比可以指示算法的性态。

$\mathbf { C } ^ { 3 }$ 模型的参数及其计算首先定义用于确定计算和通信单位数的并行系统参数：令 $\pmb { \phi }$ 代表处理器数， $\iota$ 表示信包的长度， $\pmb { s }$ 表示执行发送的建立时间， $\pmb { h }$ 表示延迟(用两个处理器间平均距离表示，即 $h = \sum _ { 1 \leqslant i , j \leqslant p } d _ { i j } / \phi ^ { 2 }$ ,其中 $d _ { i j }$ 是两个处理器间的最小距离)。表4.1给出了常用互连结构的平均距离 $\boldsymbol { h }$ （也同时给出了对剖宽度 $^ { b }$ ）。

$\textcircled{1}$ 计算单位数：假定在一个超级步中,处理器 $\mathbf { P } _ { i }$ 访问 $t _ { i }$ 个字节,则超级步的计算单位数为： $\operatorname* { m a x } _ { 1 \leqslant i \leqslant p } \lceil t _ { i } / l \rceil _ { \circ }$

$\textcircled{2}$ 无拥挤时的通信单位数：通信单位数与不同的选路方案和不同的发送、接收原语有关。最常用的选路方案有存储转发和虫蚀两种；大多数机器都支持阻塞和非阻塞的发送和接收原语。施行存储转发选路时一个处理器可存储 $\pmb { k }$ 条信包，而虫蚀选路时一条信包存储于 $k$ 个(或更多)处理器中。所谓阻塞发送系指一个源处理器从开始发送

表4.1机器的平均距离和对剖宽度一览表  

<table><tr><td rowspan=1 colspan=1>互连结构</td><td rowspan=1 colspan=1>平均距离h</td><td rowspan=1 colspan=1>对剖宽度b</td></tr><tr><td rowspan=1 colspan=1>一维阵列</td><td rowspan=1 colspan=1>p/2</td><td rowspan=1 colspan=1>1</td></tr><tr><td rowspan=1 colspan=1>二叉树</td><td rowspan=1 colspan=1>O(logp)</td><td rowspan=1 colspan=1>1</td></tr><tr><td rowspan=1 colspan=1>二维网孔</td><td rowspan=1 colspan=1>2/3p</td><td rowspan=1 colspan=1>VP</td></tr><tr><td rowspan=1 colspan=1>三维网孔</td><td rowspan=1 colspan=1>p1</td><td rowspan=1 colspan=1>p2</td></tr><tr><td rowspan=1 colspan=1>蝶形网</td><td rowspan=1 colspan=1>O(logp)</td><td rowspan=1 colspan=1>0(p/logp)</td></tr><tr><td rowspan=1 colspan=1>洗牌交换</td><td rowspan=1 colspan=1>O(logp)</td><td rowspan=1 colspan=1>0（p/logp)</td></tr><tr><td rowspan=1 colspan=1>超立方</td><td rowspan=1 colspan=1>(logp)/2</td><td rowspan=1 colspan=1>p/2</td></tr><tr><td rowspan=1 colspan=1>胖树</td><td rowspan=1 colspan=1>4log4p-2/3</td><td rowspan=1 colspan=1>0(p)</td></tr><tr><td rowspan=1 colspan=1>完全图</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0(p²/4)</td></tr></table>

一条消息，直至它被目的处理器收到后源处理器的发送操作才终止；而非阻塞发送时源处理器在填满发送缓冲器后只要等到消息被取走即可。在无拥挤时处理器 $\mathbf { { P _ { i } } }$ 发送 $L _ { i , j }$ 个字节给 $\mathbf { P } _ { j }$ 时的发送和接收时间如表4.2所示。

在一个超级步中,令 $\pmb { n } _ { \mathrm { s } } ( i )$ 是 $\mathbf { P } _ { i }$ 所发送的消息数， ${ \pmb n } _ { \mathbf { r } } ( i )$ 是 $\mathbf { P } _ { i }$ 所接收的消息数， $S _ { i }$ 是处理器 $\mathbf { P } _ { i }$ 在无拥挤环境中发送 $\pmb { n } _ { \mathrm { s } } ( \pmb { i } )$ 条消息的总时间， $R _ { i }$ 为总接收时间，则无拥挤时的 $S _ { i }$ 和 $R _ { i }$ 如表4.3所示。所以一个超级步内无拥挤时的通信单位数 $= \operatorname* { m a x } _ { 1 \leqslant i \leqslant p } \left\{ \ S _ { i } + R _ { i } \right\}$

表4.2 $\mathbf { P } _ { i }$ 发送 $\mathbb { L } _ { i , j }$ 个字节给 $\mathbf { p } _ { j }$ 时发送和接收时间一览表  

<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2>非阻塞发送和接收</td><td rowspan=1 colspan=2>阻塞发送和非阻塞接收</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>发送时间si,j</td><td rowspan=1 colspan=1>接收时间rj</td><td rowspan=1 colspan=1>发送时间sij</td><td rowspan=1 colspan=1>接收时间ri,j</td></tr><tr><td rowspan=1 colspan=1>存储转发</td><td rowspan=1 colspan=1>ii*</td><td rowspan=1 colspan=1>i,i</td><td rowspan=1 colspan=1>2(s + h)+  Lii *h</td><td rowspan=1 colspan=1>s+h+            *h</td></tr><tr><td rowspan=1 colspan=1>虫蚀</td><td rowspan=1 colspan=1>s+            × h</td><td rowspan=1 colspan=1>L</td><td rowspan=1 colspan=1>2(s +h)+ Lii +h1</td><td rowspan=1 colspan=1>s+h+  Lii +h</td></tr></table>

表4.3一个超级步中的处理器发送和接收时间一览表  

<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2>非阻塞发送和接收</td><td rowspan=1 colspan=2>阻塞发送和非阻塞接收</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>发送时间S</td><td rowspan=1 colspan=1>接收时间R</td><td rowspan=1 colspan=1>发送时间S</td><td rowspan=1 colspan=1>接收时间R</td></tr><tr><td rowspan=1 colspan=1>存储转发</td><td rowspan=1 colspan=1>mLis*n(i)+1*h+M L1</td><td rowspan=1 colspan=1>新[]</td><td rowspan=1 colspan=1>2(s+h)*n(i)+h*M11jsp</td><td rowspan=1 colspan=1>(s+h)*n(i)+1&lt;p</td></tr><tr><td rowspan=1 colspan=1>虫蚀</td><td rowspan=1 colspan=1>s*n(i)+h+[]</td><td rowspan=1 colspan=1>M[]</td><td rowspan=1 colspan=1>2(s +h)*n(i)+h+M 11ip</td><td rowspan=1 colspan=1>+(s+h)*n(i)+h+ML11≤p</td></tr></table>

$\textcircled{3}$ 链路拥挤和处理器拥挤：拥挤是一种全局现象,与体系结构、选路策略和处理器对之间的传送数据量有关。度量拥挤是在所有消息都同时选路的假定下进行的。令cong表示通信处理器对的总数,即cong=∑n(i),其中1≤cong$\leqslant _ { \pmb { p } } ( _ { \pmb { \mathscr { p } } } - 1 ) ; _ { \pmb { \mathscr { b } } }$ 为机器对剖宽度,它被定义为将机器对分成处理器数彼此相当的两半所必须移去的最少链路数(参见表4.1);令 $L _ { \mathbf { m } }$ 是任意处理器对之间最大信包数，即 $L _ { \mathfrak { m } } = \operatorname* { m a x } _ { 1 \leqslant i , j \leqslant p } \biggl [ \frac { L _ { i , j } } { l } \biggr ] ; L _ { a }$ 为平均信包数，即 $L _ { a } = \frac { 1 } { c o n g } \sum _ { 1 \leqslant i , j \leqslant p } \left[ \frac { L _ { i , j } } { l } \right]$ ,则链路上的拥挤 $\displaystyle C _ { l } = L _ { \mathrm { m } } \star \left\lceil \frac { c o n g } { b } \right\rceil$ ;处理器上的拥挤 $C _ { \hat { P } } = L _ { a } \star \ \left\lceil \frac { c o n g } { \hat { P } } \right\rceil \star h$ 。所以，在一个超级步中总的通信单位数为 $\operatorname* { m a x } _ { 1 \leqslant i \leqslant p } \big \{ S _ { i } + R _ { i } \big \} + C _ { l } + C _ { p } \circ$

$\textcircled{4}$ 公共通信模式的通信单位数： $\mathrm { C } ^ { 3 }$ 模型的提出者,为常用的通信模式(如一到一、多到多、多到一、一到多等)计算出了非阻塞发送和接收时用虫蚀选路式的通信单位数，兹概括于表4.4中,其中为了简化表示,每条消息长度记为 $\mathrm { L } _ { \circ }$

表4.4非阻塞发送和接收虫蚀式选路的通信单位数一览表  

<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>S1</td><td rowspan=1 colspan=1>R1</td><td rowspan=1 colspan=1>C</td><td rowspan=1 colspan=1>C</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>一到s+[÷]+h</td><td rowspan=1 colspan=1>[]</td><td rowspan=1 colspan=1>[1]x[]</td><td rowspan=1 colspan=1>[11*h</td></tr><tr><td rowspan=1 colspan=1>多到多</td><td rowspan=1 colspan=1>(p-1)*(s+[÷])+h</td><td rowspan=1 colspan=1>[/]*（p-1)</td><td rowspan=1 colspan=1>1=11</td><td rowspan=1 colspan=1>[11*h*(p-1)</td></tr><tr><td rowspan=1 colspan=1>多到一</td><td rowspan=1 colspan=1>s+[1+h</td><td rowspan=1 colspan=1>[1*（0-1|[1</td><td rowspan=1 colspan=1>[1*（0-1|[1</td><td rowspan=1 colspan=1>[1*h</td></tr><tr><td rowspan=1 colspan=1>一到多</td><td rowspan=1 colspan=1>s+[/]*(p-1)+h</td><td rowspan=1 colspan=1>[]</td><td rowspan=1 colspan=1>[11</td><td rowspan=1 colspan=1>[]*h</td></tr></table>

对 ${ \bf C } ^ { 3 }$ 模型的评注 $\textcircled { 1 } \mathbf { C } ^ { 3 }$ 模型特别适合于粗粒度算法的开发与分析，模型特别强调了通信瓶颈的作用,在此方面它比BSP 和 $\scriptstyle \log \mathbf { P }$ 模型都要准确和详尽得多； $\textcircled { 2 } \textcircled { \times } 3$ 模型作为开发敏感于并行机参数的粗粒度算法的平台,已经研究了诸如各种通信模式、矩阵向量乘法、确定二元图像的连通性等并行算法,并已在Delta和Paragon机器上验证了 $\mathrm { C } ^ { 3 }$ 模型的有效性; $\textcircled{3}$ 粗粒度并行机上并行算法的性能非常敏感于通信模式,容易拥挤的通信模式很容易造成通信瓶颈,并行机参数之间的关系以及这些参数与通信数据量之间的关系对如何执行选路操作有着至关重要的影响，同时在准备信包和建立选路路径过程中所招致的大的软件开销也起着重要的作用。此外，粗粒度算法通常是将串行和并行解题方法结合在一起,决定哪些子问题以及多大的子问题应该串行解，哪些应是并行解,这对算法的总体性能也是个非常关键的问题。

# 4.2.6对BSP和logP的评注

从 BSP 到logPBSP 把所有的计算和通信视为一个整体行为而不是一个


<!-- chunk 0003: pages 141-210 -->
单独的进程和通信的个体活动，它采用各进程延迟通信的办法，将诸消息组合成一个尽可能大的通信实体施行选路传输，这就是所谓的整体大同步。它简化了算法(程序)的设计和分析，当然就牺牲了运行时间，因为延迟通信意味着所有的进程均必须等待最慢者。一种改进的办法是采用子集同步,即将所有的进程按快、慢程度分成若干个子集,于是整体的大同步就演变为子集内的同步。如果子集小到其中只包含成对的发/收者,则它就变成了异步的个体同步,这就是 logP模型了。也就是说,如果BSP中考虑到个体通信所造成的开销(Overhead)而去掉路障(Barrier)同步就变成了 $\mathrm { l o g P }$ ,即

$$
\mathrm { B S P + O v e r h e a d - B a r r i e r = l o g P }
$$

BSP 成本模型在 BSP的一个超级计算步中,其计算模型如图4.3所示。按此可抽象出 BSP的成本模型如下：

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0141-0210/auto/images/f5d9e76700cd655bb14771ccd73cd5b04b3df6613670cba7649286ef511ecdbc.jpg)  
图4.3BSP一个超级计算步中的计算模式

一个超级计算步成本 $= \operatorname* { m a x } \left\{ w _ { i } \right\} + \operatorname* { m a x } \left\{ h _ { i } g \right\} + L$ Processes

其中， ${ \boldsymbol { \ w } } _ { i }$ 是进程 $i ( \mathrm { P r o c e s s } _ { i } )$ 的局部计算时间， $h _ { i }$ 是 $\mathrm { P r o c e s s } _ { i }$ 发送或接收的最大信包数， $\pmb { g }$ 是带宽的倒数(时间步/信包)， $L$ 是路障同步时间(注意,在BSP 成本模型中并未考虑到I/O的传送时间)。所以,在BSP计算中,如果用了s个超级计算步,则总的运行时间为：

$$
T _ { \mathrm { B S P } } = \ \sum _ { i = 0 } ^ { s - 1 } \ w _ { i } + g \ \sum _ { i = 0 } ^ { s - 1 } \ h _ { i } + s L
$$

BSP的大同步机理BSP模型的创始人L.G.Valiant曾从理论上论证并行计算不必优化在单一消息级(Single-Message Level),他认为整体大同步能大大简化并行计算(算法和编程)的设计、分析、验证、性能预测和具体实现,而基于成对消息传递的个体异步并行计算(例如logP模型),在时间上的得益比起对计算性能上难以分析和预测来说，并不合算。目前，对BSP模型的质疑主要集中在两点，即延迟通信至某一特定点和频繁的路障同步，会不会造成性能下降和使成本过于昂贵。BSP模型的支持者们对这两个问题进行了研究，回答是：延迟通信能提供更多的优化通信的机会，采用组合小的消息和全局通信调度能减少拥挤和竞争;路障同步对共享存储结构是不太费时的，而对分布存储的结构，主要是目前低层软件绝大多数都不支持访问相应的硬件，所以比较昂贵，但不管怎样，路障同步所造成的成本可折合到全局通信中而予以部分地抵销。

BSP 和logP相互比较 $\textcircled{1}$ 现今最流行的并行计算模型是BSP和logP,已经证明两者本质上是等效的，且可以相互模拟：用BSP去模拟logP所进行的计算时,通常会慢常数倍,而用logP去模拟BSP所进行的计算时，通常会慢对数倍；$\textcircled{2}$ 直观上讲,BSP为算法(和程序)提供了更多的方便,而 logP却提供了较好的机器资源的控制； $\textcircled{3} \textcircled { 1 } \textcircled { \mathbf { S } } \mathbf { P }$ 所引起的精确度方面的损失比起其所提供的更结构化的编程风格的优点来是小的； $\textcircled{4}$ 总之,BSP模型在简明性、性能的可预测性、可移植性和结构化可编程性等方面更受人欢迎和喜爱。

# 4.3 小结和导读

小结并行计算模型是设计和分析并行算法的基础。PRAM模型由于过于抽象而不能很好地反映并行算法的实际运行性能，所以研究考虑通信、同步等因素的从而能较真实反映并行算法运行性能的所谓更实际的计算模型（MoreRealisticComputation Models)成为当今并行算法研究的主要动向之一。本节所讨论的APRAM、BSP、logP 和 ${ \sf C } ^ { 3 }$ 等模型就是属于这种模型。但过去几年来，主要是从理论分析的角度,来研究它们之上的一些典型的并行算法的设计与分析；而近期的研究热点却从这些模型上的算法研究转向这些模型的编程的研究，即从理论研究转向实际应用。因为任何并行算法的应用都最终落实到具体的编程上,所以这种转变是顺应应用要求的。例如，一些研究者就为BSP模型构造了一些函数库,这些BSP库就是一些为程序员编写BSP应用程序(这些应用程序按照 BSP的超级计算步的风格进行编写)所提供的一组简单有力的编程界面函数,此函数可改善程序的可移植性而不依赖于具体的并行机结构。尽管PVM和 MPI等也是目前可供使用的开发可移植并行代码的方法，但它们的功能过于复杂而不易被掌握，且它们均没有为编程者提供能设计高效代码的成本函数，而像BSP模型却提供了简单和可定量分析程序运行时间的成本函数。因此研究基于这些实用计算模型的并行编程方法是非常有意义的。

最后,将本章所讨论的几种并行计算模型综合比较于表4.5中。

表4.5并行计算模型综合比较一览表  

<table><tr><td rowspan=1 colspan=1>模型属性</td><td rowspan=1 colspan=1>PRAM</td><td rowspan=1 colspan=1>APRAM</td><td rowspan=1 colspan=1>BSP</td><td rowspan=1 colspan=1>logP</td><td rowspan=1 colspan=1>C</td></tr><tr><td rowspan=1 colspan=1>体系结构</td><td rowspan=1 colspan=1>SIMD-SM</td><td rowspan=1 colspan=1>MIMD-SM</td><td rowspan=1 colspan=1>MIMD-DM</td><td rowspan=1 colspan=1>MIMD-DM</td><td rowspan=1 colspan=1>MIMD-DM</td></tr><tr><td rowspan=1 colspan=1>计算模式</td><td rowspan=1 colspan=1>同步计算</td><td rowspan=1 colspan=1>异步计算</td><td rowspan=1 colspan=1>异步计算</td><td rowspan=1 colspan=1>异步计算</td><td rowspan=1 colspan=1>异步计算</td></tr><tr><td rowspan=1 colspan=1>同步方式</td><td rowspan=1 colspan=1>自动同步</td><td rowspan=1 colspan=1>路障同步</td><td rowspan=1 colspan=1>路障同步</td><td rowspan=1 colspan=1>隐式同步</td><td rowspan=1 colspan=1>路障同步</td></tr><tr><td rowspan=1 colspan=1>模型参数</td><td rowspan=1 colspan=1>1（单位时间步）</td><td rowspan=1 colspan=1>d,Bd:读/写时间B:同步时间</td><td rowspan=1 colspan=1>p,g,lp：处理器数g：带宽因子l:同步间隔</td><td rowspan=1 colspan=1>l,0,g,pl:通信延退0:额外开销g：带宽因子p:处理器数</td><td rowspan=1 colspan=1>l,s,h1：信包长度s:发送建立时间h：通信延迟</td></tr><tr><td rowspan=1 colspan=1>计算粒度</td><td rowspan=1 colspan=1>细粒度/中粒度</td><td rowspan=1 colspan=1>中粒度/大粒度</td><td rowspan=1 colspan=1>中粒度/大粒度</td><td rowspan=1 colspan=1>中粒度/大粒度</td><td rowspan=1 colspan=1>粗粒度</td></tr><tr><td rowspan=1 colspan=1>通信方式</td><td rowspan=1 colspan=1>读/写共享变量</td><td rowspan=1 colspan=1>读/写共享变量</td><td rowspan=1 colspan=1>发送/接收消息</td><td rowspan=1 colspan=1>发送/接收消息</td><td rowspan=1 colspan=1>发送/接收消息</td></tr><tr><td rowspan=1 colspan=1>编程地址空间</td><td rowspan=1 colspan=1>全局地址空间</td><td rowspan=1 colspan=1>单一地址空间</td><td rowspan=1 colspan=1>单地址/多地址空间</td><td rowspan=1 colspan=1>单地址/多地址空间</td><td rowspan=1 colspan=1>多地址空间</td></tr></table>

导读关于并行算法的设计和分析,读者可阅读[191]。最基本的PRAM模型来源于[65];推广的PRAM模型有存储竞争模型[108],延迟模型[138],局部PRAM[5],分层存储模型[11]等。关于更实际的并行计算模型综合介绍，读者可参阅[192];更为详细者,包括APRAM[76],BSP[176], $\mathrm { l o g P } [ 5 5 ]$ 和 $\mathbf { C } ^ { 3 } [ \mathbf { 8 } 7 ]$ 。关于并行计算模型的定量比较,读者可参阅[106]。对 BSP模型的质疑和回答，读者可参阅[162];有关 BSP 的函数库,读者可参阅[80,81]。如何使用 BSP模型进行编程,读者可参阅[82];如何使用大同步进行并行计算,读者可参阅[46]。

# 习 题

4.1试证明：

(1)如果 $f ( n ) = 1 0 n$ ，则 $f ( n ) = O ( n )$ 。

（2）如果 $f ( n ) = { \frac { 1 } { 3 } } n ^ { 3 } + { \frac { 1 } { 2 } } n ^ { 2 } + { \frac { 1 } { 6 } } n$ ，则 $f ( n ) = O ( n ^ { 3 } )$

(3）如果 $f ( n ) = n ^ { 2 } / 5$ ,则 $f ( n ) = \Omega ( n ^ { 2 } )$ 。

（4)如果 $f ( n ) = 0 . 0 0 1 n ^ { 2 }$ ，则 $f ( n ) = \Omega ( n ^ { 2 } ) ,$

4.2试证明 ${ \frac { 1 } { 2 } } n ^ { 2 } - 3 n = \Theta { \left( n ^ { 2 } \right) } ,$

[提示：按照紧致界 $\Theta ( \cdot )$ 的定义,求出满足要求的 ${ \pmb n } _ { \pmb 0 } \setminus { \pmb C } _ { 1 }$ 和 $c _ { 2 }$ 之值。]

4.3试证明 Brent定理：令 $\mathbf { { \cal { W } } } ( n )$ 是某并行算法 $\pmb { A }$ 在运行时间 $T ( n )$ 内所执行的运算数量，则 $A$ 使用 $\pmb { \mathscr { P } }$ 台处理器可在 $t ( n ) = O ( W ( n ) / p + T ( n ) )$ 时间内执行完毕。

4.4试分析算法4.2的执行过程。

4.5假定 $\bar { \mathsf { P } } _ { i } ( 1 { \leqslant i } { \leqslant n } )$ 开始时存有数据 $d _ { i }$ ，所谓累加求和系指用 $\sum _ { j = 1 } ^ { i } d _ { j }$ 来代替 $\mathtt { P } _ { i }$ 中的原始值 $d _ { i }$ 。算法4.3给出了在PRAM模型上累加求和算法：

# 算法4.3 PRAM-EREW上累加求和算法

输入： $\mathrm { \bf P } _ { i }$ 中保存有 $d _ { i }$ ：, $\iota \leqslant i \leqslant n$ 输出： $\mathrm { \bf P } _ { i }$ 中的内容为 $\sum _ { j = l } ^ { i } d _ { j }$

beginfor $j = 0$ to $\log n - 1$ dofor $i = 2 ^ { j } + 1$ to $\pmb { n }$ par-do$( \mathrm { i } ) \mathbf { P } _ { i } = d _ { i } - 2 ^ { i }$ $( \ddot { \mathrm { i } } ) d _ { i } = d _ { i } + d _ { i } - 2 ^ { j }$ endforendfor  
End(1)试用 $\pmb { n = 8 }$ 为例,按照上述算法逐步计算出累加和。  
(2)分析算法4.3的时间复杂度。

4.6在APRAM模型上设计算法时,应尽量使各处理器内的局部计算时间和读写时间大致与同步时间B相当。当在APRAM上计算n个数的和时,可以借用B叉树求和的办法。

假定有p个处理器计算n个数的和,此时每个处理器上分配n/p个数,各处理器先求出自身的局和;然后从共享存储器中读取它的B个孩子的局和，累加后置人指定的共享存储单元SM中;最后根处理器所计算的和即为全和。算法4.4示出了APRAM上的求和算法：

# 算法4.4 APRAM上求和算法

输入： $\pmb { n }$ 个待求和的数

输出：总和在共享存储单元SM中

# Begin

（1）各处理器求n/p个数的局和,并将其写人SM中(2) Barrier(3） for k=「logB(p(B-1)+1)]-2 downto 0 do(3.1) for all $\mathrm { \bf P } _ { i }$ $\bullet { \leqslant } i { \leqslant } p - 1$ ,d

if $\mathrm { P } _ { i }$ 在第 $k$ 级 then$\mathbf { P } _ { i }$ 计算其B个孩子的局和并与其自身局和相加,然后将结果写入SM中endifend for(3.2） Barrierend for

End

(1)试用APRAM模型之参数,写出算法的时间复杂度函数表达式。  
(2)试解释Barrier语句的作用。

4.7欲在BSP模型上计算 $_ { n }$ 个数的和，可以在 $^ { d }$ 叉树上进行。假定用 $\pmb { \mathscr { P } }$ 个处理器求 $\pmb { \mathscr { n } }$ 个数的和,则每个处理器分配有 $\pmb { n } / \pmb { \mathscr { p } }$ 个数。首先,各处理器求 $\pmb { n } / \pmb { p }$ 个数的局和;然后在 $^ d$ 叉树上自下而上求全和,其全过程如算法4.5所示。

# 算法4.5 BSP上求和算法

输入： $\pmb { n }$ 个待求和的数输出：总和在根处理器 ${ \bf P _ { 0 } }$ 中

#

Begin(1） for all $\mathbf { P } _ { i }$ $\scriptstyle \bigwedge _ { i } , 0 { \leqslant } i { \leqslant } p - 1 \ \mathbf { d } \mathbf { 0 }$ $\big / \star$ 各处理器求各自局和 $\star$ /(1.1) $\mathbf { P } _ { i }$ 计算 $\pmb { n } / \pmb { \mathscr { p } }$ 个数的局和(1.2) if $\mathtt { P } _ { i }$ 在第 $\lceil \log _ { \mathsf { B } } ( \phi ( B - 1 ) + 1 ) \rceil - 1$ 级 then$\mathrm { \bf P } _ { i }$ 将其局和发往父节点endifendfor(2） Barrier(3） ${ \mathrm { f o r ~ } } k = \lceil \log _ { B } ( { \boldsymbol { \beta } } - 1 ) + 1 ) \rceil - 2$ downto 0 do $\big / \ast$ 上播并求和 $\bigstar$ /(3.1) for all $\mathrm { \bf P } _ { i }$ $\ u _ { i } , 0 { \leqslant } i { \leqslant } p - 1$ doif $\mathbf { P } _ { i }$ 在第 $_ r$ 级 then$\mathbf { { P } } _ { i }$ 接收 $^ { d }$ 个孩子消息,并将它们与其本身局和相加;然后将结果发往父节点endifendfor(3.2） Barrierendfor  
End

(1)试分析算法4.5的时间复杂度。

$( 2 ) d$ 值如何确定？

4.8在给定时间 $\pmb { t }$ 内，尽可能多的计算输入值的和也是一个求和问题。如果在 $\scriptstyle \log \bar { \mathbf { P } }$ 模型上求此问题时,要是 $t < L + 2 { \cdot } 0$ ,则在一个单处理机上即可最快地完成；要是 $t > L + 2 \cdot 0$ 时,则根处理器应在 ${ \pmb t - 1 }$ 时间完成局和的接收工作，然后用一个单位时间完成加运算而得最终的全和。而根的远程子节点应在 $( t - 1 ) - ( L + 2 { \cdot } 0 )$ 时刻开始发送数据，其兄妹子节点应依次在 $\left( t - 1 \right) - \left( L + 2 { \cdot } 0 + g \right) , \left( t - 1 \right) - \left( L + 2 { \cdot } 0 + 2 g \right)$ ,…时刻开始发送数据。图4.4示出了 $\scriptstyle t = 2 8 , { \boldsymbol { \phi } } = 8 , L = 5 , \sigma = 2 , g = 4$ 的 $\scriptstyle \log \bar { P }$ 模型上的通信(即发送/接收)调度树。试分析此通信调度树的工作原理和图中节点中的数值是如何计算的？

$$
\begin{array} { r } { \overbrace { \bigodot \mathrm { P } _ { 1 } \bigoplus _ { \mathfrak { p } _ { 1 } } \mathrm { P } _ { 2 } \underbrace { \left( 1 ^ { 0 } \right) \mathrm { P } _ { 2 } \overbrace { \bigcirc \mathrm { P } _ { 3 } \overbrace { \bigcirc \mathrm { P } _ { 3 } \overbrace { \bigcirc \mathrm { P } _ { 4 } \overbrace { \bigcirc \mathrm { P } _ { 5 } \overbrace { \bigcirc \mathrm { P } _ { 6 } } } } } ^ { \bigcirc \ \ { \mathrm { P } _ { 6 } \large } } } } } ^ { \bigotimes \ \ \mathrm { P } _ { 0 } } } \end{array}
$$

图4.4 $\pmb { t = 2 8 }$ ， $\pmb { \hat { p } = 8 }$ ,L=5, $\scriptstyle \pmb { o } = 2$ ， $g = 4$ 的通信调度树

4.9按照图4.4通信调度树,在logP模型上的处理器进行连续接收和发送时必须相间时间间隔g,但可以用通信开销。和计算局和的时间来填充,从而可掩盖g的开销。一般而言,对于某处理器,若它有k个子节点，则它必须接收k个消息，所以至少要k（g－o）次局部加法来填充所有的g,因此在它接收k个消息中,至少要作.k(g－o-1)次自身内部数的加法来填充，这样才能充分掩盖g的开销。图4.5示出了按照图4.4所示的通信调度树时的计算时间调度图。试分析此计算调度图的工作原理和处理器Po与Ps填充计算情况。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0141-0210/auto/images/78f1459ecb0d8492ec117e3112209578c2352d3bc5451cb4469b005257ac3d1c.jpg)  
图4.5 $\scriptstyle t = 2 8 , \phi = 8 , L = 5 , o = 2 , g = 4$ 的计算调度图

4.10试分析如下用 BSPLib并行求4个整数1,2,3,4的前缀和的过程(参见图4.6)。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0141-0210/auto/images/750e321bd25c21c7aa17dc543c55182fd296f23fc8fe1d72d725ca686a0ee5e0.jpg)  
图4.6求整数1,2,3,4的前缀和过程

# $/ / \ast$ 用BSPLib求前缀和 $\pmb { \mathscr { k } }$ //

# include "bsp.h" int bsp._ allsums(int $_ { x }$ ） int i,left,right;

bsp-push-reg(&right,sizeof(int));   
bsp-push-reg(&letf,sizeof(int));   
bsp- sync();

right $\mathbf { \mu } = \mathbf { x }$ $\mathbf { f o r } ( i = 1 ; i < \mathrm { b s p } _ { - } \mathrm { n p r o c s } ( ) ; i \neq - 2 ) \left\{ \begin{array} { r l } \end{array} \right.$ if (bsp-pid() $^ +$ i<bsp- nprocs()) bsp-put(bsp-pid()+i,&right,&left,0,sizeof(int); bsp-sync(); ${ \mathrm { ~ ( b s p - p i d ( \lambda ) > \lambda } } = i { \mathrm { ~ ) ~ } } { \mathrm { ~ r i g h t = l e f t + r i g h t ; } }$ ！ bsp-pop-reg(&right); bsp-pop-reg(&left); returm right; 一 void main( bsp-begin(bsp-nprocs()); printf("On %d sum is %d\n",bsp-pid(),bsp-allsums( $1 +$ bsp- pid())); bsp-end(); ！

# 第五章 并行算法的一般设计方法

设计并行算法一般有三种方法： $\textcircled{1}$ 检测和开拓现有串行算法中的固有并行性而直接将其并行化,这种方法虽不是对所有问题总是可行的，但对很多应用问题仍不失为一种有效的方法； $\textcircled{2}$ 从问题本身的描述出发，根据问题固有的属性，从头开始设计一个全新的并行算法，这种方法虽有一定的难度;但所设计的并行算法通常是高效的； $\textcircled{3}$ 借用已有的并行算法使之可求解新的一类问题，这种方法对于一个初学者来说似乎有一定的难度，但对一个有经验的算法设计者来说有可能产生一个很优秀的并行算法。但是,并行算法的设计是复杂的且在发展中，目前尚无一套普遍适用的系统的设计方法。

# 5.1 串行算法的直接并行化

# 5.1.1设计方法描述

长期以来人们积累了大量优秀的串行算法，这是一批宝贵的财富。在设计并行算法时,要充分利用现有求解问题的串行算法,在其基础上而直接并行化,这显然是设计并行算法时一种优先考虑的方法。但使用这样方法时有两点需要考虑： $\textcircled{1}$ 对于一类具有内在顺序性的串行算法,则恐难于直接并行化。例如在某串行算法执行步中，每一步都要用到上一步的计算结果,则显然这样的串行算法步无法并行执行； $\textcircled{2}$ 并非任何优秀的串行算法都可以产生好的并行算法,相反一个不好的串行算法则有可能产生很优秀的并行算法。例如,枚举串行算法，显然是一种复杂度高的被视为不好的串行算法类,但其直接并行化所产生的并行算法则可能获得低复杂界的优秀的并行算法。所以，并不是说一个优秀的串行算法并行化后总能产生相应的好的并行算法。最后也须说明，直接并行化也并非想象的那样简单、直接。直接并行化的关键步是分析数据执行时的相关性以及检测算法结构的固有串行性。有时为了并行化，将原串行算法不作本质性修改也是需要的,例如调整执行顺序,复制共享变量等。

大家知道,科学和工程问题中的数值计算问题,依据其数值分析数学原理而产生了很多广泛使用的串行算法，在设计这些问题的并行算法时大多都是采用串行算法直接并行化的方法，这样诸如算法的稳定性、收敛性等复杂问题,在直接并行化后的算法中均无需考虑,这恐怕也是为什么现今的数值并行算法大都是已有串行算法直接并行化的结果的原因吧。

有关并行数值算法，本书专辟了第三篇进行了讨论，读者在学习后就会发现,在那些章节里的很多并行数值问题的算法都是已有的串行算法直接并行化的结果。下面举一个非数值串行算法直接并行化的例子。

# 5.1.2快排序算法的并行化

串行快排序 快排序(Quicksort)是常用的串行排序算法之一，虽然其最坏情况下的复杂度为 $O ( n ^ { 2 } )$ ,但其具有较好的平均复杂度 $\Theta \left( \pi \mathrm { l o g } n \right)$ 。快排序是基于分治策略的递归排序方法。其算法分为两步：首先将一个序列 $\left( A _ { q } , \cdots , A _ { r } \right)$ 分成两个非空子序列 $( A _ { q } , \cdots , A _ { s } )$ 和 $( A _ { s + 1 } , \cdots , A _ { r } )$ ,其中前一个子序列中的任一元素都小于等于后一个子序列中的任意元素;然后对该两子序列施行递归调用。此递归调用过程直至子序列中仅有两个元素为止。

如何按上述要求将一个序列划分成两个子序列？通常的办法是从（A,…,$A _ { r }$ )中选择一划分元素 $_ { x }$ ,也称之为主元(Pivot),由其将原序列划分成满足上述要求的两个子序列,选取此元素 $_ { _ x }$ 最简易的办法就是将 $( A _ { q } , \cdots , A _ { r } )$ 中的第一个元素作为主元。下面给出串行快排序的形式描述(算法5.1)：

算法5.1 SISD上快排序算法

输入：无序序列 $( A _ { q } , \cdots , A _ { r } )$   
输出：有序序列 $( A _ { q } , \cdots , A _ { r } )$   
Procedure QUICKSORT $( A , q , r )$   
Begin if $q < r$ then (1) $x = A _ { q }$ (2） $\mathbf { \vec { s } } = \mathbf { \vec { q } }$ (3) for $i = q + 1$ to $r$ do if $A _ { i } { \leqslant } x$ then (i) $\begin{array} { r } { s = s + 1 } \end{array}$ (ii $) \mathbf { \ s w a p } ( A _ { s } , A _ { i } )$

# endif

(4） swap $( A _ { q } , A _ { s } )$ （5）QUICKSORT $( A , q , s )$ （6）QUICKSORT $( A , s + 1 , r )$

# endif

# End

对于长度为 $\pmb { n }$ 的序列，在最坏情况下所划分的两个子序列长度分别为 $_ n -$ 1和1,相应的运行时间为 $t \left( n \right) = t \left( n - 1 \right) + \theta \left( n \right)$ ,其解为 $t \left( n \right) = \Theta { \left( n ^ { 2 } \right) }$ ；理想的情况是所划分的两个子序列等长，相应的运行时间为 $t \left( \pi \right) = 2 t \left( n / 2 \right) +$ $\Theta ( \mathfrak { n } )$ ,其解为 $t \left( n \right) = \Theta \left( n \ \log n \right)$ 。

快排序的并行化分析算法5.1,一种很自然的并行化方法是并行地调用快排序对两个所划分的子序列进行快排序(算法5.1.的第(5)和第(6)步)。这种并行化的方法并不改变串行算法本身的属性，所以将其很容易改写成并行执行的形式。但是用n个处理器排序n个数,如用一个处理器将(Ai,,A)划分成 $( A _ { 1 } , \cdots , A _ { s } )$ 和 $( A _ { s + 1 } , \cdots , A _ { n } )$ 是不会得到成本最优算法的，因为单是划分时间就是 $\Omega ( n )$ ,所以 $C ( n ) = \phi \left( n \right) \cdot t \left( n \right) = \Omega { \left( n ^ { 2 } \right) }$ 。可见只有将划分步(算法5.1的第(3)步)也进行并行化才有可能得到成本最优的算法。下面给出基于二叉树的并行选主元的 PRAM-CRCW模型上的快排序算法。

PRAM-CRCW上快排序算法 执行快排序可以看成是构造一棵二叉树，其中主元是根，小于等于主元的元素处于左子树，大于主元的元素处于右子树。算法首先从选第一个主元开始，它划分原序列为两个子序列;然后相继子序列中主元的选取则可并行执行。当这样的二叉树造好后，采用中序遍历的方法就可得到一个有序序列。令待排序的序列为（A,,A),处理器P;保存元素A;,LC[1:n]和RC[1:n]分别记录给定主元的左儿子和右儿子,fi中存有其元素是主元的处理器号。开始时所有处理器均将它们的处理器号写向变量root，但根据CRCW模型原理，最终只有一个处理器号写人变量root。Aroot中是第一个主元，并且root被复制给每个处理器i的f，然后那些其元素小于Af的处理器将其号码写人 $L C _ { f _ { i } }$ ,而大于 $A _ { f _ { i } }$ 的处理器将其号码写人 $R C _ { f _ { i } }$ 。因此所有那些其元素属于小序列的处理器便将其号码写人LCf,而所有那些其元素属于大序列的处理器便将其号码写人RCs。但是因为并发写操作只有两个值（一个对应于$L C _ { f _ { i } }$ ,另一个对应于 $R C _ { f _ { i } }$ )能被写进这些单元,所以这两个值就变成了下次迭代所需的主元的处理器号。按此算法一直继续到n个主元被选完。

# 算法5.2 PRAM-CRCW上为快排序构造二叉树算法

输入：序列 $( A _ { 1 } , \cdots , A _ { n } )$ 和 $\pmb { n }$ 个处理器

输出：供快排序用的一棵二叉树

# Begin

(1） for each processor $\textbf { \em i }$ do (1.1) $\mathfrak { r o o t } = \mathfrak { i }$

(1.2) $f _ { i } = { \mathrm { \bf { r o o t } } }$ (1.3) $L C _ { i } = R C _ { i } = n + 1$

# endfor

(2） repeat for each processor iroot ·do $\mathbf { i f } ( A _ { i } < A _ { f _ { i } } ) \lor ( A _ { i } = A _ { f _ { i } } \land i < f _ { i } ) \mathbf { t h e n }$ (2.1) $L C _ { f _ { i } } = i$ (2.2) if $i = L C _ { f _ { i } }$ then exit else $f _ { i } = L C _ { f _ { i } }$ endif else (2.3) $R C _ { f _ { i } } = i$ (2.4) if $\therefore R C _ { f _ { i } }$ then exit else $f _ { i } = R C _ { f _ { i } }$ endif endif end repeat

End

在算法每次迭代时,可在 $\Theta ( 1 )$ 时间内构造一级树,而树高为 $\Theta ( \log n )$ ,所以算法5.2的时间复杂度为 $\Theta ( \log n )$ 。

# 5.2从问题描述开始设计并行算法

对于有些问题,现有的串行算法恐难直接将其并行化,此时要从问题的描述出发,寻求可能的新途径,设计出一个新的并行算法。但这并不是说完全排除某些串行算法设计的基本思想,而是更着重从并行化的具体实现上开辟新的设计方法。本节拟以串匹配问题为例,来阐述这种设计方法。

# 5.2.1串匹配算法

定义5.1由字符集Σ(字符的非空有穷集合)中的字符所组成的任何有穷序列称之为串(又叫字符串)。串中包含的字符个数称为串的长度。

定义5.2给定长度为 $\pmb { n }$ 的正文串 text 和长度为 $_ { m }$ 的模式串pat( $\pmb { m } \leqslant$ $\pmb { n }$ ),欲找出 pat 在text 中出现的所有位置 $\pmb { i }$ ，如果找到就称之为匹配。

在以下的讨论中,约定 pat 和 text均以数组形式表示。按此,pat 出现在text的i位置,指的是 pat=text[i:i+m-1],此时则定义match(i)= true,否则定义match(i)=false。在下文中,为了书写方便,常将 text和pat也分别写作$T$ 和 $P$ 。

串匹配问题在诸如文字和图像处理中经常使用,是复杂性理论中最广泛研究的问题之一。串匹配问题的一种平易算法是把它视为以pat为键的搜索问题，即长度为 $\pmb { n }$ 的text可分成 $\pmb { n } - \pmb { m } + 1$ 个长度为 $\pmb { m }$ 的子串，检查各个子串是否与长度为 $\pmb { m }$ 的pat相匹配。这样在最坏情况下的时间复杂界为 $\left( \pmb { n } - \pmb { m } + 1 \right)$ $m = { \cal O } ( m n )$ ，所以这种古朴的串匹配算法是很少使用的。后来Knuth、Morris和Pratt三人提出了一个线性时间的经典的串匹配算法，通称之为KMP算法。但此算法一直没有发表,直至Boyer和 Moore两人也提出了设计串匹配的新算法时，这两种算法才同时发表，而相应地称后一种算法为BM算法。

目前已知的线性时间的串匹配算法均不易直接并行化，但参照串行算法的实质,结合使用申的周期数学性质却可开发出一些高效的并行串匹配算法。第一个最优的并行串匹配算法是由Galil提出，在PRAM-CRCW模型上,达到了$t \left( n \right) = O \left( \log n \right)$ 和 ${ \pmb { \mathscr { p } } } \left( \pmb { \mathscr { n } } \right) = \pmb { \mathscr { n } } \varLambda \mathrm { o g } n$ 的复杂界。后来Vishkin改进了Galil的算法,放宽了算法对字符集 $\sum$ 大小是固定的要求。可是由于Vishkin的并行算法十分复杂,所以本节只是着重介绍其设计思路(有兴趣的读者可参阅[191])。但在介绍这些内容之前,先来讨论一下KMP算法，以说明将其直接并行化的困难所在。

# \*5.2.2 KMP串行串匹配算法

定义5.3令串 $\mathbf { Y }$ 的长度为 $_ { m }$ ，如果 $Y = X ^ { k } X ^ { \prime }$ ，其中 $X ^ { k }$ 是 $\pmb { X }$ 本身重复 $\pmb { k }$ 次(k为正整数),X'是X的前缀(Prefix),则Y的子串X叫作Y的周期(Peri-od)。串Y的周期也就是Y的最短周期。如果串Y的周期长度p满足p≤m/2,则称串 $\mathbf { Y }$ 是周期的(Periodic)。

注意,在研究串匹配时，常将整个模式串(Pattern String)P本身当作正文串（Text String),而其从首字符起的子串当作模式串,这样我们如令 $D ( j )$ 是前缀P[1:j-1]的周期,其中D(1)=1,2≤j≤m+1,且P(m+1)是P中不出现的字符，则可定义模式串的失效函数(Failure Function） $\pmb { F }$ 如下：

$$
\left\{ \begin{array} { l } { F ( 1 ) = 0 } \\ { F ( j ) = j - D ( j ) \quad , \quad 2 \leqslant j \leqslant m + 1 } \end{array} \right.
$$

其几何意义如图5.1所示：(a)是为了计算失效函数的起始情况；(b)是计算的一般步骤。当P(j)=P(k)时,前移指针j和k且置F(k)=j;当P(j)≠P(k)时，则向右滑动，上面的模式使得F(j)和k对准，此时的F就是失效函数。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0141-0210/auto/images/0d8f78b527245d988b5aaace55890ec765537baa56d68cced10a1907b80757b4.jpg)  
图5.1失效函数的确定

可以设计如下算法来计算失效函数：

# 算法5.3失效函数的计算算法

输入：模式申 $P [ 1 : m ]$

输出：失效函数 $F ( k ) , 1 { \leqslant } k { \leqslant } m + 1$

# Begin

(1) $F ( 1 ) = 0 ; F ( 2 ) = 1 ; k = 2 ; j = 1$ (2） while $k { \leqslant } m$ do

(2.1) if $P ( k ) = P ( j )$ then  
(i) $j = j + 1$   
(ii) $k = k + 1$   
(ii） $F ( k ) = j$

# endif

(2.2) if $P ( k ) { \neq } P ( j )$ then(i) $\scriptstyle { j = F ( j ) }$ (ii） if ${ \bf { j } } ^ { \mathrm { ~ } } = \bf { 0 }$ then$\begin{array} { l } { k = k + 1 } \\ { j = 1 } \\ { F ( k ) = 1 } \end{array}$ endif

# endif

# endwhile

End

显然计算 $P [ 1 : m ]$ 的失效函数可在 $O ( m )$ 时间内完成。

有了失效函数的定义，就可以讨论KMP算法了：设想模式 $P$ 置于正文 $T$ 之上,令 $P$ 向右滑动，用两指针 $j$ 和 $k$ 分别指示字符 $P ( j )$ 和 $T ( k )$ 的现行位置。开始时， $j = k = 1$ 然后分两种情况讨论： $\textcircled{1}$ 当 $P ( j ) = T ( k )$ 时,两指针前进1,且如果 $j = m + 1$ ，则表示已找到匹配，置match $\left( k - m \right) = 1 ;$ $\textcircled{2}$ 当 $P ( j ) { \neq } T ( k )$ 时，表示现行位置不匹配，应向右滑动 $P _ { j }$ 位，其下一可能的位置由如上所述的$D ( j )$ 决定，即令 $\begin{array} { r } { j = j - D ( j ) } \end{array}$ 。所以KMP算法的关键就是当模式与正文不匹配时，应如何利用已得到的“部分匹配"的结果,将模式向右滑动一段距离后再施行继续比较,这一距离可由前面所讨论的失效函数 $F ( j )$ 来决定。

# 算法5.4 KMP串匹配算法

输入： $T [ 1 { : } n ] , P [ 1 { : } m ] , F [ 1 { : } m + 1 ]$

输出：match(i)

Begin

(1) $_ { j } = 1 ; k = 1$   
(2）while $\pmb { k } - j { \leqslant } n - m$ do (2.1) if $T ( k ) = P ( j ) \mathfrak { t }$ hen (i) $k = k + 1$ (ii) ${ j = j + 1 }$ (ii)if $j = m + 1$ then match $\left( k - m \right) = 1$ endlif

# endif

(2.2) if $T ( k ) { \neq } P ( j )$ then(i) ${ \bf \nabla } _ { j } = F ( j )$ (ii） if $j = 0$ then$k = k + 1 ;$ $j = 1$ endif

# endif

# endwhile

End

显然算法5.4的时间复杂度为 $O ( n )$ 。

KMP算法的精髓在于使用了失效函数，使用它来调整两指针 $j$ 和 $\pmb { k }$ 。这种指针来回移动的办法并不太容易并行化,因为并行算法设计的基本策略是试图将 $_ T$ 串分段并行处理,但上述的KMP顺序算法很难有效地使用在分段并行处理中。

# 5.2.3并行串匹配算法的设计思路

设计并行串匹配算法的出发点设计并行串匹配算法应从何处人手呢？为此我们要从问题的描述出发，研究串匹配的基本性质。实际上，两串是否能匹配,是与串的自身前缀有关,这种前缀特性就是串的周期性(Periodicity)。所以研究串的数学性质(即周期性)是寻找并行化的一种可能的途径。

研究并行串匹配的基本方法与步骤既然串的周期特性对研究匹配是至关重要的，那么用什么量来表征它呢？为此首先引人了失配见证函数(WitnessFunction),其定义如下：

定义5.4对于给定的 $j ( 1 { \leqslant } j { \leqslant } m / 2 )$ ，如果 $P [ j : m ] \neq P [ 1 : m - j + 1 ]$ 则存在某个 ${ \pmb w } ( 1 { \leqslant } { \pmb w } { \leqslant } { \pmb m } - { \pmb j } + 1 )$ 使得 $P ( \boldsymbol { \mathbf { \ell } } _ { w } ) { \neq } P ( \boldsymbol { \mathbf { \ell } } _ { s } )$ ，其中 $\textstyle s = j - 1 + \pi$ ,记WIT$( j ) = w$ 。

于是,可以根据 $\pmb { W } \mathbb { T } ( j )$ 函数来区分申是周期的还是非周期的： $\textcircled{1}$ 对于所有$2 { \leqslant } j { \leqslant } m / 2$ ,当且仅当 $\mathbf { W I T } ( j ) { \neq } \mathbf { 0 }$ 时则串是非周期的； $\textcircled{2}$ 对于所有 $2 \leqslant j \leqslant m /$ 2,若存在某个 $\pmb { j }$ ，使得 $\mathbf { W I T } ( \ j ) = \mathbf { 0 }$ ,则串是周期的。

一旦确定了串的周期特性,则可先研究非周期串(Aperiodic String)的匹配，然后在此基础上再研究周期串的匹配。

对于非周期串匹配的研究，就是如何利用已计算出的WIT(i)快速地找出$P$ 在 $T$ 中匹配的位置。为了减少 $P$ 与 $T$ 的比较次数,引人了一种竞争(Duel)函数 $\mathsf { d u e l } ( \pmb { \mathscr { p } } , \pmb { q } )$ 的概念,即当模式在某一位置 $\pmb { \phi }$ 匹配时，则在另一位置 $\pmb q$ 一定不匹配，这样就排除了q位置。可以设计一个算法来计算duel（力，q）（参见习题5.8)。在duel(p,q)算法中,参数p,q与n,m有关,且p与q的选取应先从小范围，逐步到大范围，且在每个限定范围内可并行地求duel（p，q)，以确定竞争的幸存者。这样整个过程就像分组比赛一样，逐渐淘汰小组中的获胜者，最终只可能保留少数几个幸存者，它们就是些可能的匹配位置号码，最后再进行一次正确性验证即可。

并行串匹配算法举例为了更好地理解上述思路与步骤，现举一例说明之。

例5.1 令 T= abaababaababaababaababa(n = 23),P=abaababa （m=8)。由所计算的模式P的WIT(1)=0,WIT(2)=1,WIT(3)=2,WIT(4)=4可知P是非周期串。为了计算此非周期串与T的匹配情况,先要计算P相对于T的WIT[ $1 : n - m + 1 ]$ 之值。然后由其来计算 $\mathtt { d u e l } ( \pmb { \mathscr { p } } , \pmb { q } )$ 之值。计算 $\mathsf { d u e l } ( \pmb { \mathscr { p } } , \pmb { q } )$ 时,将 $T$ 与 $P$ 由小到大划分成一些大小为 $( 2 ^ { 1 } , 2 ^ { 2 } , \cdots )$ 的块，在相同大小的各块内并行地计算 $\operatorname { d u e l } ( p , q )$ 的值。其过程为：先将 $P$ 与 $T$ 各自划分成大小为2的一些块,这样模式块(ab)与正文块 $( \mathbf { a b } ) ( \mathbf { a a } ) ( \mathbf { b a } ) ( \mathbf { b a } ) ( \mathbf { a b } ) ( \mathbf { a b } ) ( \mathbf { a b } ) ( \mathbf { a } ) ( \mathbf { b a } )$ 进行匹配,可知在位置1,4,6,8,9,11,14和16出现匹配(即 $\operatorname { d u e l } ( \pmb { \mathscr { p } } , \pmb { q } )$ 的获胜者)；再将 $P$ 与 $T$ 各自划分成大小为4的一些块,这样模式块(abaa)与正文块(abaa)(baba)(abab)(aaba)进行匹配,可知在位置1,6,11和16出现匹配,而位置4,8,9和14被淘汰;最后需用模式(ababbaba)在正文的位置1,6,11和16进行匹配检查,以验证其正确性。□

至于周期串的匹配,情况更复杂,在此不再讨论，感兴趣的读者可参阅文献[191]。

# 5.3 借用已有算法求解新问题

# 5.3.1 设计方法描述

所谓"借用法"是指借用已知的某类问题的求解算法来求解另一类问题。此两类问题表面上看是迥然不同的,或似乎是互不相干的，所以按照常规的办法，求解这两类问题的算法似乎也毫无“亲缘"关系，因而一般初学者难以设法通过某种内在关系,将两类不同的问题在求解方法上统一起来。这实质上也正是借用法的难点所在。“借用"不是毫不费力的直接拿来使用,相反地,当欲借用时，不但要从问题求解方法的相似性方面仔细观察，寻求问题解法的共同点；而且所借来的方法要用得上算,效率要高,从而能达借用的目的。显然这并非易事。一个好的借用法所设计的算法，往往给人们带来深刻的印象，常常被教科书作为范例加以引用。

借用法虽无一般规律可循，但往往从求解问题的数学方法上能得到某种启示。例如，求一个有向图的传递闭包(TransitiveClosure)问题可以使用布尔矩阵乘法来实现,其方法如下：

假定A是一个n点有向图G的n阶布尔邻接矩阵,其矩阵元素aij为1,当且仅当有向图中从顶点i到顶点j之间有一条边时。所谓传递闭包,记之为A+,实际上也是一个n阶布尔矩阵,其矩阵元素bi为1,当且仅当：①从i到j存在一条有向边;或②对于某一顶点k,存在有向边i到k和k到j;或③i=j。按此，根据上述定义，可利用布尔矩阵乘法来求传递闭包。事实上,如令【为单位矩阵(仅对角元素为1),则(A+I)=1,表示当且仅当i和j 之间的路径长度为0(即i=j),或为1(i和j之间有一条边);(A+I)²=1,表示当且仅当i和j之间的路径长度为2或小于2;((A+I)²)²=1,表示当且仅当i和j之间的路径长度为4或小于4,…因此作 $\log n$ 次 $( A + I )$ 自乘就可求得传递闭包 $A ^ { + }$ ，因为对于 $\pmb { n }$ 点有向图， $_ i$ 和 $j$ 之间若有一路径存在,则其长度至多为 $\pmb { n }$ 。

下面将介绍一种利用矩阵乘法求所有点对间的最短路径方法，它是一种比较典型的借用已有算法来求解另一类问题的并行算法设计方法。

# 5.3.2利用矩阵乘法求所有点对间最短路径

最短路径问题有两类：一类是单源最短路径(Single-Source Shortest Path)，即在一个图中寻找从一个指定顶点到所有其它顶点之间的最短路径;另一类是所有点对间最短路径(All Pairs Shortest Paths),仅讨论后者。

定义5.5假定一有向图各边赋于非负整数权,那么一条路径的长度就是沿该路径所有边权之和；而最短路径问题就是对每一点对 $_ i$ 和 $j$ ,求找其间任何最短长度的路径。

矩阵乘法在求点对间最短路径中的应用对于一个 $\pmb { n }$ 个顶点的加权有向图 $G ( V , E )$ ,其权矩阵由 $W _ { n \times n }$ 表示。为了计算其所有顶点对之间的最短路径,可以先构造一个 $\mathbf { \Omega } _ { n } \times \mathbf { \Omega } _ { n }$ 的矩阵 $\pmb { D }$ ，使得对于所有的 $\dot { \iota }$ 和j， $d _ { i j }$ 是从 $\pmb { v _ { i } }$ 到 $\boldsymbol { v } _ { j }$ 的最短路径长度。只要 $G$ 中无负长度的环,可以假定 $\mathbf { \Delta } \mathbf { W }$ 有正、负或零元素。

令 $d _ { i j } ^ { k }$ 表示从 ${ \pmb v } _ { i }$ 到 $v _ { j }$ ,其间经过至多 $k - 1$ 个中间顶点时的最短路径长度。因此 $d _ { i j } ^ { 1 } = \tau \upsilon _ { i j }$ 。特别是从 $\boldsymbol { v } _ { i }$ 到 $\boldsymbol { v } _ { j }$ 无边存在 $( i \neq j )$ 时,则 $d _ { i j } ^ { 1 } = \infty$ 。同样 $d _ { i i } ^ { 1 } = 0 _ { \circ }$ 因 $G$ 中不存在负权的环,所以 $d _ { i j } = d _ { i j } ^ { n - 1 }$ 。

为了计算 $d _ { i j } ^ { k } \left( k > 1 \right)$ ,可以使用组合最优原理（Combinatorial OptimizationPrinciple) :

$$
d _ { i j } ^ { k } = \operatorname* { m i n } _ { l } \{ d _ { i l } ^ { k / 2 } + d _ { l j } ^ { k / 2 } \}
$$

也就是说， $d _ { i j } ^ { k }$ 取所有 $\iota$ 条路径 $( d _ { i l } ^ { k / 2 } + d _ { l j } ^ { k / 2 } )$ 中的最短者。因此矩阵 $\pmb { D }$ 就可以从$\pmb { D } ^ { 1 }$ 逐次计算 $D ^ { 2 } , D ^ { 4 } , \cdots , D ^ { n - 1 }$ ,然后取 $\pmb { D } = \pmb { D } ^ { n - 1 }$ 而求得。为了从 $\pmb { D } ^ { k / 2 }$ 计算 $\pmb { D } \pmb { k }$ ，可以使用标准的矩阵乘法,只是将原矩阵乘法中的“ $^ \bullet \times$ "操作代之以(5.2)式中的“+"操作;而将原矩阵乘法中的“∑"操作代之以(5.2)式中的“min"操作,这样的操作共执行 $\lceil \log ( n - 1 ) ^ { - }$ 次。这就是借用法中最关键之处，如果没有观察和联想到这一点,则就难以做到巧妙的借用。

SIMD-CC模型上求所有点对间最短路径算法因为本节重点是介绍借用矩阵乘法来求所有点对间的最短路径,所以有关矩阵乘法的算法就不介绍了，只是在主算法中以调用的形式来使用。关于SIMD-CC的矩阵乘法，读者可参阅本书第九章第9.4.4节的DNS乘法。

如第9.4.4节所述那样,假定n³个处理器排成n×n×n的立方体，每个处理器有A(i,j,k)、B(i,j,k)和C(i,j,k)三个寄存器。开始时A(0,j,k)=${ w _ { j k } } \left( 0 { \leqslant } j , k { \leqslant } n - 1 \right)$ 即图的权矩阵开始时存放在 $\pmb { A }$ 寄存器中；算法执行中将调用算法9.6DNS乘法，按照上述借用方法来计算所有点对间的最短路径；算法结束时， $C ( 0 , j , k )$ 中就是 ${ \pmb v } _ { j }$ 到 ${ \pmb v } _ { k }$ 的最短路径。

算法5.5 SIMD-CC上求所有点对间最短路径算法

输入： $A \left( 0 , j , k \right) = w _ { j k } , 0 { \leqslant } j , k { \leqslant } n - 1$   
输出： $C ( 0 , j , k )$ 中是 ${ \pmb v } _ { j }$ 到 ${ \pmb v } _ { { \pmb k } }$ 的最短路径长度， $\textstyle , 0 \leqslant j , k \leqslant n - 1$   
Begin

(1) $\big / \big \varkappa$ 构筑矩阵 $D ^ { 1 }$ ,并将其存人 $\pmb { A }$ 和 $B$ 寄存器中 $\yen 7$ for ${ \bf { j } } = { \bf { 0 } }$ to n -1 par - do for $k = 0$ to n -1 par- do (1.1) if $j \neq k$ & $A \left( 0 , j , k \right) = 0$ then $B ( 0 , j , k ) = \infty$ endif (1.2) $B ( 0 , j , k ) = A \left( 0 , j , k \right)$ end for end for

(2) $\curvearrowright$ 调用算法9.6构筑矩阵 $D ^ { 2 } , D ^ { 4 } , \cdots , D ^ { n - 1 } * /$ for $i = 1$ to $\lceil \log ( n - 1 ) \rceil$ do （2.1）DNS MULTIPLICATION $( A , B , C )$ $\big / \ast$ 调用算法 $9 . 6 \ast /$ (2.2) for ${ \bf { j } } = { \bf { 0 } }$ to n -1 par-do for ${ \pmb k } = { \bf 0 }$ to $n - 1 \ \mathbf { p a r } - \mathbf { d o }$ (i) $A \left( 0 , j , k \right) = C ( 0 , j , k )$ (ii) $B ( 0 , j , k ) = C ( 0 , j , k )$ end for

# end for

end for

End

显然，上述算法的时间复杂度为O(log²n)次，因为算法第(2)步重复$O ( \log n )$ 次,每次乘法时间也为 $O ( \log n )$ ，而 $\smash { p ( n ) = O ( n ^ { 3 } ) }$ 。

为了更好地理解上述算法,兹举一例如下。

例5.2试求图5.2(a)所示的有向加权图中所有点对间的最短路径,其步骤如下：

$\textcircled{1}$ 由图5.2(a)构筑邻接权矩阵如图5.2(b)所示。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0141-0210/auto/images/844ff503c30dfefcbd704f4f062ff664362c274b343b1837a391c33e17f8bc45.jpg)  
图5.2利用矩阵乘法求所有点对间最短路径

$\textcircled{2}$ 算法开始前,用 $\boldsymbol { w } _ { j k }$ 之值初始化 $A \left( 0 , j , k \right) : A \left( 0 , 0 , 0 \right) = 0 , A \left( 0 , 0 , 1 \right) =$ $4 , A \left( 0 , 0 , 2 \right) = 1 , A \left( 0 , 0 , 3 \right) = 0 , A \left( 0 , 0 , 4 \right) = 7 , A \left( 0 , 0 , 5 \right) = 0 , x _ { 0 } = 1 2 .$ A(0,0,6)=0,A $\left( 0 , 1 , 0 \right) = 0 , A \left( 0 , 1 , 2 \right) = 8 , A \left( 0 , 1 , 3 \right) = 0 , A \left( 0 , 1 , 4 \right) = 0 , A \left( 0 , 2 , 2 \right) = 0 , A \left( 0 , 3 , 3 \right) = 0 , . $ ,1,5)=0,A(0, $1 , 6 ) = 0 , \cdots , A \left( 0 , 6 , 5 \right) = 1 , A \left( 0 , 6 , 6 \right) = 0 _ { \circ }$

$\textcircled{3}$ 由算法第(1)步计算出 $B ( 0 , j , k )$ ,它就是距离矩阵 $\pmb { D } ^ { 1 }$ （如图 ${ \mathfrak { s } } . 2 ( { \mathfrak { c } } )$ 所示）。$\textcircled{4}$ 由算法第(2)步的第1次循环计算 $\pmb { { \cal D } } ^ { 1 } \times \pmb { { \cal D } } ^ { 1 } = \pmb { { \cal D } } ^ { 2 }$ ,其中 $d _ { j k } ^ { 2 }$ 各元素计算如下：

$$
\begin{array} { l } { { d _ { 0 0 } ^ { 2 } = \displaystyle { \operatorname* { m i n } _ { 0 \leqslant t \leqslant 6 } \big \{ d _ { 0 0 } + d _ { 0 0 } , d _ { 0 1 } + d _ { 1 0 } , d _ { 0 2 } + d _ { 2 0 } , d _ { 0 3 } + d _ { 3 0 } , d _ { 0 4 } + d _ { 4 0 } , d _ { 0 5 } + d _ { 5 0 } , d _ { 0 6 } + d _ { 6 0 } , d _ { 7 } \leqslant 2 \big \} , } } } \\ { { d _ { 0 6 } + d _ { 6 0 } \big \} = 0 } } \end{array}
$$

$\begin{array} { l } { { d _ { 0 1 } ^ { 2 } = \displaystyle { \operatorname* { m i n } _ { 0 \leqslant i \leqslant 6 } \big \{ d _ { 0 0 } + d _ { 0 1 } , d _ { 0 1 } + d _ { 1 1 } , d _ { 0 2 } + d _ { 2 1 } , d _ { 0 3 } + d _ { 3 1 } , d _ { 0 4 } + d _ { 4 1 } , d _ { 0 5 } + d _ { 5 1 } \big \} } } } \\ { { \phantom { d _ { 0 1 } ^ { 2 } = d _ { 0 1 } ^ { 2 } } d _ { 0 6 } + d _ { 6 1 } \big \} = 4 } } \end{array}$ ，  
：  
$d _ { 6 6 } ^ { 2 } = \mathbf { 0 }$

$\pmb { D } ^ { 2 }$ 的整个矩阵如图5.2(d)所示。

$\textcircled{5}$ 由算法第(2)步的第2次迭代计算 $\pmb { D } ^ { 2 } \times \pmb { D } ^ { 2 } = \pmb { D } ^ { 4 }$ ，其结果如图5.2(e)所示。$\textcircled{6}$ 算法第(2)步最后一次迭代计算 $\scriptstyle D ^ { 4 } \times D ^ { 4 } = D ^ { 8 }$ ,其结果如图5.2(f)所示。□

# 5.4 小结和导读

小结设计并行算法是一件复杂的事,而并行算法的设计这门学科还属于发展中的一门学科，所以目前尚无一套普遍适用的、系统的设计方法学。本章只是给出一个非常一般的并行算法的设计方法，它不可能也不应该视为设计并行算法的全部方法。重要的是,通过所介绍的设计方法的学习,希望读者能从中得到更多的启迪,补充更多的算例,丰富、完善乃至开拓出更新更好的设计方法。

导读有关串行快排序算法,[95]和[154]是两篇很好参考文献；PRAM-CRCW上快排序算法,读者可参考[49]；超立方上的快排序算法,读者可参考[178];而网孔上的快排序算法,读者可参考[161]。有关并行串匹配算法，读者可参考[191]和[104];其中KMP算法来源于[110]和BM算法来源于[38];[72]和[177]是本章重点介绍的并行串匹配算法。有关图论问题的并行算法，[198]是本很全面的著作;本章所介绍的利用矩阵乘法求所有点对间的最短路径算法来源于[58]。

# 习 题

5.1试分析：

$\textcircled{1}$ 串行快排序算法最坏情况下的时间复杂度。  
$\textcircled{2}$ 串行快排序算法平均情况下的时间复杂度。

5.2给定序列(3,2,1,5,8,4,3,1),试用算法5.1逐步进行排序。

5.3给定序列(33,21,13,54,82,33,40,72)和8个处理器,试按照算法5.2构造一棵为在PRAM-CRCW模型上执行快排序所用的二叉树。

5.4令n是待排序的元素数,p=2d是d维超立方中处理器的数目。假定开始随机选定主元x,并将其播送给所有其它处理器,每个处理器按所接收到的x,对其n/p个元素按照≤x和>x进行划分,然后按维进行交换。这样在超立方上实现的快排序的算法如下：

# 算法5.6 超立方上快排序算法

输入： $\pmb { n }$ 个元素， $B = \pi / \beta$ ， $d = \log \phi$ 输出：按超立方编号进行全局排序

Begin

(1)u-piuwxvis lavi

(2) for $\dot { \iota } = 1$ to $^ d$ do (2.1) $\scriptstyle { \pmb { x } } = { \mathfrak { p i v o t } }$ $\big / \ast$ 选主元 $\yen 7$ (2.2）划分 $\pmb { B }$ 为 $\scriptstyle B _ { 1 }$ 和 $B _ { 2 }$ 满足 $B _ { 1 } { \leqslant } x { < } B _ { 2 }$ (2.3) if第 $\textbf { \em i }$ 位是零then (i）沿第 $\textbf { \em i }$ 维发送 $B _ { 2 }$ 给其邻者 (ii) $C =$ 沿第 $\textbf { \em i }$ 维接收的子序列 (ii） $B { = } B _ { 1 } \cup C$ else （i）沿第 $\textbf { \em i }$ 维发送 $\pmb { B _ { 1 } }$ 给其邻者 (ii) $C =$ 沿第 $\pmb { i }$ 维接收的子序列 (ii) $B = B _ { 2 } \bigcup C$

# endif

endfor

(3)使用串行快排序算法局部排序 $\scriptstyle B = n / _ { \beta }$ 个数End

$\textcircled{1}$ 试解释上述算法的原理。  
$\textcircled{2}$ 试举一例说明上述算法的逐步执行过程。

5.5令模式串 $\mathbf { { \nabla } } P =$ abcabcabcabcabcc。开始时， $j = 1$ 和 ${ \pmb k } = 2$ ，试按照算法5.3计算该模式 $\pmb { P }$ 的失效函数 $F ( 1 ) \sim F ( 1 6 )$ 。

5.6 $\textcircled{1}$ 令 $T =$ babaababaa, $\pmb { P } = \mathbf { a b } \mathbf { a b }$ ，试用算法5.4计算两者的匹配情况。$\textcircled{2}$ 试分析KMP算法为何不能简单并行化。

5.7假定 $P _ { 1 } =$ abaababa , $P _ { 2 } =$ abaabaab , $P _ { 3 } =$ abaabaaabaabab,试计算各自的 $\pmb { \ W } \pmb { \mathrm { T } } ( j )$ 函数，并判断它们的周期性。

5.8计算 $\mathbf { d u e l } ( \pmb { \mathscr { p } } , \pmb { q } )$ 函数的算法如下：

算法5.7计算串匹配的 $\mathbf { d u e l } ( \pmb { \mathscr { p } } , \pmb { q } )$ 的算法

输出：返回竞争幸存者的位置或null(表示 $\pmb { \mathscr { P } }$ 和 $\pmb q$ 之一不存在)

Procedure DUEL $( \pmb { \mathscr { p } } , \pmb { q } )$

Begin if ${ \pmb { \hat { p } } } =$ null then $\mathbf { d u e l } = \pmb q$ else if $q = \mathrm { \ n u l l }$ then duel $= \phi$ else

$$
\begin{array} { r } { j = q - p + 1 } \\ { w = \mathbf { W } \mathbf { I } \mathbf { T } ( j ) } \end{array}
$$

$$
\mathbf { W I T } ( q ) = \mathbf { \mathcal { w } }
$$

$$
\mathbf { d u e l } = \pmb { \mathscr { p } }
$$

$$
\begin{array} { l } { \displaystyle \mathtt { W I T } ( \pmb { \mathscr { p } } ) = \pmb { q } - \pmb { \mathscr { p } } + \pmb { 1 } } \\ { \displaystyle \mathtt { d u e l } = \pmb { q } } \end{array}
$$

# endif

# endif

$\textcircled{1}$ 令 $\mathbf { \nabla } T =$ abaababaababaababababa, $P =$ abaababa,试计算 $\pi \Pi ( i )$ ；  
$\textcircled{2}$ 试考虑 $\pmb { P = 6 , q = 9 }$ 的竞争情况。

5.9对于图5.2(a)的加权有向图,试用算法5.5,逐步求出 $\mathbf { D ^ { 2 } } , \mathbf { D ^ { 4 } }$ 和 $\mathbf { D } ^ { 8 }$ 中各元素 $d _ { i j } ^ { k }$

$$
\begin{array} { r l } { ( \begin{array} { c c c c c c c c } { { d _ { 0 0 } ^ { 2 } } } & { { d _ { 0 1 } ^ { 2 } } } & { { d _ { 0 2 } ^ { 2 } } } & { { d _ { 0 3 } ^ { 2 } } } & { { d _ { 0 4 } ^ { 2 } } } & { { d _ { 0 5 } ^ { 2 } } } & { { d _ { 0 6 } ^ { 2 } } } \\ { { d _ { 1 0 } ^ { 2 } } } & { { d _ { 1 1 } ^ { 2 } } } & { { d _ { 1 2 } ^ { 2 } } } & { { d _ { 1 3 } ^ { 2 } } } & { { d _ { 1 4 } ^ { 2 } } } & { { d _ { 1 5 } ^ { 2 } } } & { { d _ { 1 6 } ^ { 2 } } } \\ & & & { \vdots } & & & & & \\ & & & { \vdots } & & & & & & \\ { { d _ { 6 0 } ^ { 2 } } } & { { d _ { 6 1 } ^ { 2 } } } & { { d _ { 6 2 } ^ { 2 } } } & { { d _ { 6 3 } ^ { 2 } } } & { { d _ { 6 4 } ^ { 2 } } } & { { d _ { 6 5 } ^ { 2 } } } & { { d _ { 6 6 } ^ { 2 } } } \end{array} ) \qquad } &  ( \begin{array} { c c c c c c c } { { d _ { 0 0 } ^ { 4 } } } & { { d _ { 0 1 } ^ { 4 } } } & { { d _ { 0 2 } ^ { 4 } } } & { { d _ { 0 3 } ^ { 4 } } } & { { d _ { 0 4 } ^ { 4 } } } & { { d _ { 0 5 } ^ { 4 } } } & { { d _ { 0 6 } ^ { 4 } } } \\ { { d _ { 1 0 } ^ { 4 } } } & { { d _ { 1 1 } ^ { 4 } } } & { { d _ { 1 2 } ^ { 4 } } } & { { d _ { 1 3 } ^ { 4 } } } & { { d _ { 1 4 } ^ { 4 } } } & { { d _ { 1 5 } ^ { 4 } } } & { { d _ { 1 6 } ^ { 4 } } } \\ & & & { \vdots } & & \\ & & & & { d _ { 6 1 } ^ { 4 } } & { { d _ { 6 2 } ^ { 4 } } } & { { d _ { 6 3 } ^ { 4 } } } & { { d _ { 6 5 } ^ { 4 } } } & { { d _ { 6 6 } ^ { 4 } } } \\ & & & & { ( \mathbf { b } ) } &  D ^  4  \end{array} \end{array}
$$

$$
\left( \begin{array} { c c c c c c c } { { d _ { 0 0 } ^ { 8 } } } & { { d _ { 0 1 } ^ { 8 } } } & { { d _ { 0 2 } ^ { 8 } } } & { { d _ { 0 3 } ^ { 8 } } } & { { d _ { 0 4 } ^ { 8 } } } & { { d _ { 0 5 } ^ { 8 } } } & { { d _ { 0 6 } ^ { 8 } } } \\ { { d _ { 1 0 } ^ { 8 } } } & { { d _ { 1 1 } ^ { 8 } } } & { { d _ { 1 2 } ^ { 8 } } } & { { d _ { 1 3 } ^ { 8 } } } & { { d _ { 1 4 } ^ { 8 } } } & { { d _ { 1 5 } ^ { 8 } } } & { { d _ { 1 6 } ^ { 8 } } } \\ { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } \\ { { d _ { 6 0 } ^ { 8 } } } & { { d _ { 6 1 } ^ { 8 } } } & { { d _ { 6 2 } ^ { 8 } } } & { { d _ { 6 3 } ^ { 8 } } } & { { d _ { 6 4 } ^ { 8 } } } & { { d _ { 6 5 } ^ { 8 } } } & { { d _ { 6 6 } ^ { 8 } } } \end{array} \right)
$$

5.10对于图5.3所示的单位权有向图,试用布尔邻接矩阵乘法求出其传递闭包。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0141-0210/auto/images/cc98eaecfc1043c955c9b6c19aa457b9c42ef719393037ada0b9f7169d2cc9a1.jpg)  
图5.3单位权有向图

# 第六章 并行算法的基本设计技术

并行算法的设计虽然是复杂的，且目前技术上尚不甚成熟，似乎又依赖于某些技巧，但也不是无章可循。随着并行算法设计学科的不断发展，人们逐渐地总结出了一些最基本的设计技术可供参考使用。从使用并行处理操作最朴素的思想出发，就可导出所谓划分设计技术，它是将一原始问题分成若干个部分，然后各部分由相应的处理器同时执行。这是最基本的设计技术,包括均匀划分技术、方根划分技术、对数划分技术和功能划分技术。从求解问题的方法学和求解策略出发，则可导出所谓分治设计技术,它是将一个大而复杂的问题分解成若干个特性相同的子问题,然后使用"各个击破"的办法逐步求解之。这是算法设计的普遍技术,既适合于串行算法的设计,又适合于并行算法的设计。从针对求解问题的特性出发，也可导出一些有效的并行算法设计技术,包括平衡树技术和倍增技术等。众所周知,流水线技术是并行处理中最基本的技术之一，它也可以被使用在并行算法的设计中，形成了流水线设计技术。本章所介绍的设计技术并非全面，同时只能作为设计并行算法的一般性指南，而不能作为可直接引用的手册。

# 6.1划分设计技术

用划分(Partitioning)法求解问题可分为两步： $\textcircled{1}$ 将给定的问题劈成 $\pmb { \mathscr { P } }$ 个独立的几乎等尺寸的子问题; $\textcircled{2}$ 用 $\pmb { \phi }$ 台处理器并行求解诸子问题。划分时关键在于如何将问题进行分组，使得子问题较容易并行求解，或者子问题的解较容易被组合成原问题的解。

# 6.1.1 均匀划分技术

假定待处理的序列长为 $\pmb { n }$ ,现有 $\pmb { \mathscr { P } }$ 台处理器，一种最基本的划分方法就是均分划分(Uniform Partition),系将 $\pmb { n }$ 个元素分割成 $\pmb { \mathscr { P } }$ 段,每段含有 $n / \phi$ 个元素且分配给一台处理器。下面以PSRS(Parallel Sorting by Regular Sampling)算法为例,来阐述均匀划分法的使用。

# 算法6.1 MIMD机器上PSRS排序算法

输入：长度为 $\pmb { n }$ 的无序序列, $\pmb { \mathscr { P } }$ 台处理器,每台处理器有 $\spadesuit / \phi$ 个元素

输出：长度为 $\pmb { n }$ 的有序序列

# Begin

（1）均匀划分： $\pmb { n }$ 个元素均匀地划分成 $\pmb { \hat { p } }$ 段,每台处理器有 $\pmb { n } / \hbar$ 个元素。  
（2）局部排序：各处理器利用串行排序算法，排序 $\scriptstyle n / \phi$ 个数。  
（3）选择样本：每台处理器各从自己的有序段中选取 $\pmb { \hat { p } }$ 个样本元素。  
（4）样本排序：用一台处理器将所有 $\scriptstyle { \pmb { \mathscr { p } } } ^ { 2 }$ 个样本元素，用串行排序算法排序之。  
(5）选择主元：用一台处理器选取 $\pmb { \hat { p } } - \pmb { 1 }$ 个主元，并将其播送给其余处理器。  
（6）主元划分：各处理器按主元将各自的有序段划分成 $\pmb { \hat { p } }$ 段。  
（7）全局交换：各处理器将其辖段按段号交换到相应的处理器。  
（8）归并排序：处理器使用归并排序将所接收的诸段施行排序。

End

算法6.1中的第(1)步是使用了均匀划分技术,从而使各段(除零头外)的规模(大小)均匀相等。算法的第(6)步也使用了划分技术,但它是非均匀的,各段的大小可能不等。

由于我们只是着重划分技术的描述,所以有关算法6.1的复杂度就不再讨论了。

例6.1示例说明 PSRS 排序过程。假定序列长度 ${ \pmb n } = 2 7$ ， $\pmb { \mathscr { p } } = 3$ ,则 PSRS排序过程如图6.1所示。□

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0141-0210/auto/images/9ecef42e6a68132f144ab82c49f1ce75bf19373049860d0fe8624fe763e0cc1f.jpg)  
图6.1例示 PSRS排序过程

# 6.1.2方根划分技术

假定待处理的序列长为 $\pmb { n }$ ，现欲将其分段处理。一种称之为平方根划分(SquareRoot Partition)的方法,就是取每第 $i \ { \sqrt { n } } \left( { \it \Omega } i = 1 , 2 , \cdots \right)$ 个元素作为划分元素而将序列划分成若干段,然后分段处理之。下面以Valiant归并算法为例，来阐述方根划分法的使用。

# 算法6.2 SIMD-EREW上 Valiant 归并算法

输入：两有序段 $\pmb { A }$ 和 $B$ 段定长度各为 $\pmb { n }$ 输出：长度为 ${ \pmb 2 } { \pmb n }$ 的有序序列

# Begin

(1）方根划分：将 $\pmb { A }$ 和 $B$ 中的第 $i \ { \sqrt { n } } \left( { i = 1 , 2 , \cdots } \right)$ 个元素作为划分元素，而将 $\pmb { A }$ 和 $B$ 分成了若干段。

(2）段间比较： $\pmb { A }$ 中所有的划分元素与 $B$ 中所有划分元素进行比较，以确定 $\pmb { A }$ 中划分元素应插入 $B$ 序列的哪一段。

(3）段内比较;A中的划分元素与其所插人的 $B$ 相应段中的元素进行比较,以确定该划分元素应插入 $B$ 相应段的哪一位置,而这些插入位置又将B重新划分成了若干段。

（4）段组归并：B被重新划分的各段与原A中相应各段构成了成对的一些段组,在各段组内,递归地执行(1)到(3)步,直到段组中某一序列长度为零为止。

End

算法6.2的第(1)步是使用了平方根划分技术，而在第(4)步的各段组内的递归调用时，各段组内的序列也使用了平方根划分技术。所感兴趣的是，这种划分技术使得算法达到了非常好的时间界。可以证明,算法6.2使用n个处理器可在 $O \left( \log \log n \right)$ 时间内完成两长度各为 $\pmb { n }$ 的有序序列的归并(见习题6.2)。

# 6.1.3对数划分技术

假定待处理的序列长为n，现欲将其分段处理。一种和上节所述的方根划分法不同的划分是对数划分（Logarithmic Partition）法，即取每第ilogn（i=1,2,…)个元素作为划分元素,而将序列划分成若干段,然后分段处理之。下面仍以两有序序列的归并为例，来阐述对数划分法的使用。

如算法6.2所示，为了确定A序列中的划分元素在B序列中的全局位序，所以划分元素必须在各段之间施行全局比较(算法6.2的第(2)步)。如果在选取 $\pmb { A }$ 序列中的划分元素时，就考虑到了它在 $B$ 序列中的全局位序，那么就不必对划分元素施行段间的全局比较，而可直接对按划分元素所断开的各段组两两进行归并，便可完成两个原序列的归并。下面所要讨论的归并算法就是基于上述思想。

定义6.1令 $X = \left( x _ { 1 } , x _ { 2 } , \cdots , x _ { t } \right) , x _ { i } \in S , S$ 为具有偏序关系的集合。所谓$\pmb { x }$ 在 $\pmb { X }$ 中的位序(Rank),记之为 $\mathbf { r a n k } ( { \boldsymbol { x } } : { \boldsymbol { X } } )$ ，就是 $\pmb { X }$ 中小于等于 $\pmb { x }$ 的元素的数目。令 $Y = \left( _ { y _ { 1 } } , _ { y _ { 2 } } \cdots , _ { y _ { s } } \right) , _ { y _ { i } } \in \mathfrak { s }$ 。所谓 $\operatorname { r a n k } ( Y { \boldsymbol { : } } X ) = ( r _ { 1 } , r _ { 2 } , \cdots , r _ { s } )$ 就是 $\mathbf { Y }$ 在 $\pmb { X }$ 中的位序，其中 $r _ { i } = \mathrm { r a n k } \left( y _ { i } : X \right)$ 。

例6.2 令 X=(25,-13,26,31,54,7), $Y = ( 1 3 , 2 7 , - 2 7 )$ ，则 $\operatorname { r a n k } ( Y : X )$ $= ( 2 , 4 , 0 )$ 。□

这样一来，归并问题就能视为确定每个来自序列 $\pmb { A }$ 或 $B$ 中的元素 $\pmb { x }$ 在 $A \cup$ $B$ 中的位序。而求找一个元素在另一个序列中的位置可以使用对半搜索的方法,其时间界为 $O ( \log n )$ 。

下面给出PRAM模型上对数划分算法。

算法6.3PRAM上对数划分算法

输入：两非降有序序列 $A = \left( a _ { 1 } , \cdots , a _ { n } \right) , B = \left( b _ { 1 } , \cdots , b _ { m } \right)$ ，假定 $\log m$ 和$k \left( m \right) = m \Lambda \log m$ 均为整数

输出：将 $\pmb { A }$ 和 $B$ 划分成 $\pmb { k } ( \pmb { m } )$ 对段组 $( A _ { i } , B _ { i } )$ ，使得 $\mid B _ { i } \mid = \log m \ , \Sigma \mid A _ { i } \mid$ $\mathbf { \mu } = \mathbf { \mu } _ { \pmb { n } }$ ,且对于所有 $1 { \leqslant } i { \leqslant } k \left( m \right) - 1 , A _ { i }$ 和 $B _ { i }$ 中的每一个 $_ i$ 元素均大于 $A _ { i - 1 }$ 和 $B _ { i ^ { - 1 } }$ 中的每一个元素

# Begin

(1) $j ( 0 ) = 0 ; j \left( k \left( m \right) \right) = n$   
(2） for $\dot { \pmb { \imath } } = 1$ to $k \left( m \right) - 1 { \mathrm { ~ p a r } } - \mathbf { d o }$ (2.1)求 $\operatorname { r a n k } ( b _ { i \log m } : A )$ (2.2) $\begin{array} { r } { j \left( i \right) = \operatorname { r a n k } \left( b _ { i \log m } : A \right) } \end{array}$ end for

#

(3） for ${ \bf { \nabla } } _ { \pmb { \imath } } = \mathbf { 0 }$ to $\pmb { k } ( \pmb { m } ) - 1$ par -do(3.1) (3.2) $\begin{array} { r l } & { B _ { i } = \left( b _ { i \log m + 1 } , \cdots , b _ { \left( i + 1 \right) \log m } \right) } \\ & { A _ { i } = \left( a _ { j \left( i \right) + 1 } , \cdots , a _ { j \left( i + 1 \right) } \right) } \end{array}$

# endfor

End

上述算法所产生的划分如图6.2所示。

一旦使用上述算法完成了两个序列的独立划分后，归并A和B的问题就变成了并行地成对归并段组 $( A _ { i } , B _ { i } )$ 的问题了。

例6.3 令A=(4,6,7,10,12,15,18,20), $B = ( 3 , 9 , 1 6 , 2 1 )$ 。本例中 $\pmb { m } = 4$ ，$k \left( 4 \right) = 2$ 。因为 $\operatorname { r a n k } ( 9 : A ) = 3$ ，所以可以得两对划分： $A _ { 0 } = ( 4 , 6 , 7 )$ ， $B _ { 0 } = ( 3 , 9 )$ 和 $A _ { 1 } =$ (10,12,15,18,20), $B _ { 1 } ( 1 6 , 2 1 )$ 。显然， $\pmb { A _ { 1 } }$ 和 $B _ { 1 }$ 中的任一元素都大于$A _ { 0 }$ 和 $B _ { 0 }$ 中的每一元素。因此可以成对归并 $( A _ { 0 } , B _ { 0 } )$ 和 $( A _ { 1 } , B _ { 1 } )$ ,而最终将 $A$ 和 $B$ 归并之。□

$$
\begin{array} { r l } { B = } &  \underbrace { B _ { 0 } } _ { \begin{array} { l } { \overbrace { b _ { 1 } \mathrm { ~  ~ \cdot ~ } \mathrm { ~  ~ \cdot ~ } \ b _ { \mathrm { i o g m } } } ^ { B _ { 0 } } } \left[ \begin{array} { l } { B _ { 1 } } \\ { b _ { \mathrm { l o g m + 1 } } \mathrm { ~  ~ \cdot ~ } \mathrm { ~  ~ \cdot ~ } \mathrm { ~  ~ \cdot ~ } b _ { \mathrm { 2 l o g m } } } \end{array} \right] \mathrm { ~  ~ \cdot ~ } \cdot \mathrm { ~  ~ \cdot ~ } \left[ \begin{array} { l } { B _ { i } } \\ { b _ { \mathrm { i l o g m + 1 } } \mathrm { ~  ~ \cdot ~ } \mathrm { ~  ~ \cdot ~ } b _ { ( i + 1 ) \mathrm { l o g m } } \left[ \mathrm { ~  ~ \cdot ~ } \mathrm { ~  \cdot ~ } \mathrm { ~  \cdot ~ } \right] } \end{array} \right] } _ { \begin{array} { l } { A } \\ { A = } & { \underbrace { \left[ a _ { 1 } \mathrm { ~  ~ \cdot ~ } \mathrm { ~  ~ \cdot ~ } \mathrm { ~  ~ \cdot ~ } a _ { j ( 1 ) } \mathrm { ~  ~ \cdot ~ } a _ { j ( 1 ) + 1 } \mathrm { ~  ~ \cdot ~ } \mathrm { ~  ~ \cdot ~ } \mathrm { ~  ~ \cdot ~ } a _ { j ( 2 ) } \mathrm { ~  ~ \cdot ~ } \mathrm { ~  ~ \cdot ~ } \mathrm { ~  ~ \cdot ~ } \mathrm { ~  ~ \cdot } \mathrm { ~  ~ \cdot ~ } a _ { j ( i ) + 1 } \mathrm { ~  ~ \cdot ~ } \mathrm { ~  ~ \cdot } \mathrm { ~  ~ \cdot ~ } a _ { j ( i + 1 ) } \mathrm { ~  ~ \cdot ~ } \mathrm { ~  ~ \cdot } \mathrm { ~  ~ \cdot ~ } \mathrm { ~  \cdot ~ } \mathrm { ~  ~ \cdot } \mathrm { ~  ~ \cdot } \mathrm { ~  ~ \cdot ~ } a _ { j ( i + 1 ) } \mathrm { ~  ~ \cdot ~ } \mathrm { ~  ~ \cdot } \mathrm { ~  ~ \cdot ~ } \mathrm { ~  ~ \cdot } \mathrm { ~  ~ \cdot ~ } \mathrm { ~  ~ \cdot } \mathrm { ~  ~ \cdot ~ } a _ { j ( i ) + 1 } \mathrm { ~  ~ \cdot ~ } \mathrm { ~  ~ \cdot } \mathrm { ~  ~ \cdot ~ } \right]} \end{array}  } _ { A _ { 1 } } } \end{array} \end{array}
$$

图6.2算法6.3所产生的划分

# 6.1.4功能划分技术

假定欲从长为 $\pmb { n }$ 的序列中选取前 $\pmb { m }$ 个最小者（此即所谓的 $( m , n )$ -选择（（m,n）-Selection))问题,那么应如何对原序列施行划分以便并行处理呢？此时可以使用所谓功能划分(Functional Partition)法,即将长为 $\pmb { n }$ 的序列划分成等长的一些组，每组中的元素数应大于或等于 $\pmb { m }$ (最后一组除外)。然后各组可并行处理，其算法如下：

算法6.4 $( m , n )$ -选择网络算法输入：长为 $\pmb { n }$ 的无序序列 $A = ( a _ { 1 } , \cdots , a _ { n } )$ 输出：序列中前 $_ { m }$ 个最小者

Begin

（1）功能划分：将 $\pmb { A }$ 划分成 $\pmb { \mathrm { g } } = \pmb { \mathrm { n } } / m$ 组,每组含 $_ { \pmb { \mathscr { n } } }$ 个元素。  
（2）局部排序：使用Batcher排序网络将各组并行进行排序。  
（3）两两比较;将所排序的各组两两进行比较,从而形成MIN序列。  
(4）排序-比较:对各个MIN序列,重复执行第(2)和第(3)步，直至最终选出 $\pmb { m }$ 个最小者为止。

End

算法6.4的执行过程示于图6.3。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0141-0210/auto/images/dd6f690e59ebf76dc511e60b3800059e0620a905f0835e4baa6f9cb3bf68e846.jpg)  
图6.3 $( m - n )$ -选择过程(S表示排序，M表示归并）

# 6.2分治设计技术

分治(Divide-and-Conquer)策略是一种问题的求解技术,其思想是将一个大而复杂的问题分解成若干特性相同的子问题分而治之。若所得的子问题规模仍嫌过大，可反复使用分治策略,直至很容易求解诸子问题为止。使用分治法时，子问题的类型通常和原问题的类型相同,因此分治法很自然地导致递归(Recur-sion)过程。

一般而言，并行分治法分为三步： $\textcircled{1}$ 将输入划分成若干个规模近于相等的子问题； $\textcircled{2}$ 同时递归地求解各个子问题； $\textcircled{3}$ 归并各子问题的解成为原问题的解。用分治法和上节所介绍的划分法求解问题的共同点在于两者均试图将原问题分解成可并行求解的子问题,但分治法的侧重点在于子问题的归并上;而划分法的注意力则集中在原问题的划分上。

下面将通过两个例子来说明分治技术的使用。

# 6.2.1双调归并网络

定义6.2一个序列 $x _ { 0 } , x _ { 1 } , \cdots , x _ { n } \gets 1$ 是双调序列(Bitonic Sequence),如果：$\textcircled{1}$ 存在着一个 ${ \boldsymbol { x } } _ { k } ( 0 { \leqslant } k { \leqslant } n - 1 )$ 使得 $x _ { 0 } { \geqslant } \cdots { \geqslant } x _ { k } { \leqslant } x _ { k + 1 } { \leqslant } \cdots x _ { n - 1 }$ 成立；或者 $\textcircled{2}$ 此序列能够循环旋转使得条件 $\textcircled{1}$ 满足。

双调归并是基于下述的Batcher定理[26]：

Batcher定理:给定一个双调序列xo,x1,,xn-1,对于所有的0≤≤-1,执行 $x _ { i }$ 和 $x _ { i } + \frac { n } { 2 }$ 的比较交换得到 $s _ { i } = \operatorname* { m i n } \left\{ x _ { i } : x _ { i + { \frac { n } { 2 } } } \right\}$ 和 $l _ { i } = \operatorname* { m a x } \left\{ x _ { i } : x _ { i + \frac { n } { 2 } } \right\} \mathrm { ~ c ~ }$

则： $\textcircled{1}$ 所形成的小序列 $\mathbf { M I N } = ( s _ { 0 } , s _ { 1 } , \cdots , s _ { n / 2 - 1 } )$ 和大序列 $\mathbf { M A X } = \left( l _ { 0 } , l _ { 1 } \cdots , \right.$ $l _ { n / 2 - 1 } )$ 仍是双调序列； $\textcircled{2}$ 且对于所有 $0 { \leqslant } i , j { \leqslant } \frac { n } { 2 } - 1$ 满足 $\bullet _ { i } { \leqslant } l _ { j }$ 。

双调归并可以用比较器网络来实现，它是由Batcher比较器构成的。所谓比较器就是一个双输入和双输出的比较交换单元,它可将两输人中的小者置于上输出端,而大者置于下输出端。

下面是Batcher双调归并算法：

# 算法6.5Bateher双调归并算法

输入：双调序列 $X = \left( \ b { x _ { 0 } } , \ b { x _ { 1 } } , \cdots , \ b { x _ { n - 1 } } \right)$ 输出：非降有序序列Y=(yo,yi,,yn-1） Procedure BITONIC MERG（X) Begin

(1) $\mathbf { f o r } \ i = 0 \ \mathbf { t o } { \frac { n } { 2 } } - 1 \ \mathbf { p a r - d o }$ (1.1) $s _ { i } = \operatorname* { m i n } \{ x _ { i } : x _ { i + n / 2 } \}$ /\*":"表示比较 $\bigstar$ /(1.2) l= max|xi: xi +n/2l

end for

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0141-0210/auto/images/2dd6abfef7da83842a47bd354de4334c9c6c9d38763e9366ed4a16e4650e3d78.jpg)  
图6.4双调归并网络的递归构造

(2） Recursive Call:

(2.1) BITONIC MERG $\left( \mathbf { M I N } { = } \left( s _ { 0 } , \cdots , s _ { \frac { n } { 2 } - 1 } \right) \right)$

# (2.2） BITONIC MERG $( \mathbf { M A X } = ( l _ { 0 } , \cdots , l _ { \frac { n } { 2 } - 1 } ) )$

(3）output sequence MIN followed by sequence MAX

# End

双调归并网络的递归构造如图6.4所示。

# 6.2.2凸壳问题

定义6.3如果多边形 $\mathbf { Q }$ 上任意两点的连线均处于 $\pmb { Q }$ 之内,则此多边形 $\pmb { Q }$ 称之为凸多边形(Convex Polygon)。

定义6.4给定平面中 $\pmb { n }$ 点集合 $\pmb { S } = ( \mathbf { \nabla } _ { \pmb { p } _ { 1 } } , \cdots , \mathbf { \nabla } _ { \pmb { p } _ { n } } )$ ,所谓 $s$ 的凸亮（ConvexHull)就是包含 $s$ 中所有 $\pmb { n }$ 点的最小凸边形。

求平面凸壳的问题,就是要确定凸壳边界上的有序顶点表列 $C H ( s )$ 。

令 $\pmb { \mathscr { P } }$ 和 $\pmb q$ 是 $s$ 中具有最小和最大 $_ { x }$ 坐标的两个点。很清楚 $\pmb { \hat { p } }$ 和 $\pmb q$ 可将全凸壳CH(S)划分成上凸壳 UH(S)和下凸壳 LH(S),其中 UH(S)系由p到q的所有点组成,而 $L H ( S )$ 系由 $\pmb q$ 到 $\pmb { \hat { p } }$ 的所有点组成。

例如图6.5中,UH(S)=(v1,U2,U3,U4,Us),而 LH(S)=(vs,6,v7,vg,U1)。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0141-0210/auto/images/8e10b0f28f670fdab69af882eda50b33d20d4c780aea378c4a19a56ebd953d5c.jpg)  
图6.5集合 S的凸壳CH(S)=(v1,U2,U3,U4,Us,U6,U7,vg)

这样一来,一个完整的凸壳CH(S)就是由上凸壳(Upper Convex Hull)UH(S）和下凸壳(Lower Convex Hull）LH(S）组成。而求 LH(S)和 UH(S)是相似的,所以下面只讨论上凸壳UH(S)的求法。

令x(p:)是点pi的x坐标，假定集合S中的点已按x坐标从小到大排序好,即𝑥(pi)<𝑥(pz)<<𝑥(pn)。那么求上凸壳UH(S)时可以使用分治技术。令 S=(p1,p2,…,p)和 S=(pz+1,P2+2,,pn),那么-且 UH(S1)和UH(S)递归地求出后,只要再求出UH(Si)和UH(S2)的上公切线(Upper

Common Tangent),那么求 $U H ( S )$ 的主要问题就解决了(参照图6.6)。下面给出求上凸壳算法：

算法6.6 PRAM上求上凸壳算法

输入： $S = ( \mathbf { \Gamma } _ { p 1 } , \cdots , \mathbf { \Gamma } _ { \phi _ { n } } )$ ，且 $x ( p _ { 1 } ) { < } x ( p _ { 2 } ) { < } \cdots { < } x ( p _ { n } )$   
输出：返回上凸壳顶点表列 $U H ( S )$   
Procedure UPPER HULL $( S , U H ( S ) ) ,$   
Begin  
(1) if $\textstyle \pmb { n } \leqslant 4$ then use a brute - force to determine $U H ( S )$ endif  
(2) $S _ { 1 } = \left( \phi _ { 1 } , \phi _ { 2 } , \cdots , \phi _ { 2 } ^ { n } \right)$ and $S _ { 2 } = \left( / { p } _ { \frac { n } { 2 } + 1 } ^ { n } , / { p } _ { \frac { n } { 2 } + 2 } ^ { n } , \cdots , / { p } _ { n } \right)$   
（3）递归调用并行计算 $U H ( S _ { 1 } )$ ， $U H ( S _ { 2 } )$ ：(3.1） UPPER HULL $( S _ { 1 } , U H ( S _ { 1 } ) )$ (3.2） UPPER HULL $( S _ { 2 } , U H ( S _ { 2 } ) )$   
(4)求 $U H ( S _ { 1 } )$ 和 $U H ( S _ { 2 } )$ 间上公切线,构造 $U H ( S )$

End

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0141-0210/auto/images/afb358cc82cb55cafdea7f5c551c5712ea26fdede1157259466876db5e2b7b30.jpg)  
图6.6示例求两上凸壳的上公切线

在 PRAM上求下凸壳的算法和算法6.6雷同。组合上凸壳与下凸壳算法就可导出如下 PRAM上求凸壳算法。

算法6.7PRAM上求凸壳算法输入： S=(p1,…,Pn)，pi=(xi,yi)输出：返回凸壳顶点表列 $C H ( S )$ Procedure CONVEX HULL $( S , C H ( S ) ) ,$ Begin

(1) $\big / \ast$ 识别极点 $\yen 7$ (1.1) $\mathbf { X M I N } = \operatorname* { m i n } \left\{ x _ { i } \right.$ 坐标 (1.2) $\mathbf { X M A X } { = } \mathbf { m a x } \left\{ x _ { i } \right.$ 坐标

(2） $\big / \big \varkappa$ 按 $_ { x }$ 坐标进行划分 $\yen 7$ (2.1) $S _ { 1 } =$ vertices from ${ \pmb \phi } _ { { \bf X M I N } }$ to ${ \pmb { \phi } } _ { \mathbf { X M A x } }$ (2.2) $S _ { 2 } =$ vertices from $\pmb { \mathscr { P } }$ XMAx to $\pmb { \phi }$ XMIN   
(3) $\big / \ast$ 递归调用上凸壳和下凸壳算法 $\yen 7$ （3.1）UPPER HULL $( S _ { 1 } , U H ( S _ { 1 } ) )$ (3.2) LOWER HULL $( S _ { 2 } , U H ( S _ { 2 } ) )$   
(4) $\nearrow$ 并接 $U H ( S _ { 1 } )$ 和 $L H ( S _ { 2 } ) \ast \prime$ $C H ( S ) = U H ( S _ { 1 } ) + L H ( S _ { 2 } )$

End

上述算法中,求上(下)公切线是很关键的。由于主要目的是展示分治技术在算法设计中的应用，所以公切线的求法就不再讨论，感兴趣的读者可参阅[104]中的第六章。

# 6.3平衡树设计技术

平衡树(Balanced Tree)方法是将输入元素作为叶节点构筑一棵平衡二叉树，然后自叶向根往返遍历。此法成功的部分原因是在树中能快速地存取所需要的信息。平衡二叉树的方法可推广到内节点的子节点的数目不只两个的任意平衡树。这种方法对数据的播送、压缩、抽取和前缀计算等甚为有效。

# 6.3.1求取最大值

使用平衡二叉树求取数的最大值时,根节点给出问题的解;叶节点存放待处理的数据;内节点执行相应子问题的计算。在树的同一深度上各内节点并行计算。

令 ${ \pmb n } = 2 ^ { m }$ ， $\pmb { A }$ 是一个 $_ { 2 n }$ 维的数组;待求最大值的 $\pmb { n }$ 个数开始存放在 $\boldsymbol { A } ( \boldsymbol { n } )$ ，$A { \big ( } n + 1 { \big ) } , \cdots , A { \big ( } 2 n - 1 { \big ) }$ ;所求得的最大值置于 A(1),于是算法描述如下：

# 算法6.8 SIMD-TC上求最大值算法

输入： $\pmb { n } = 2 ^ { m }$ 个数存在数组 $\pmb { A } \left( \pmb { n } : 2 \pmb { n } - \pmb { 1 } \right)$ 中输出：最大数置于A(1)中

# Begin

for $k = m - 1$ to 0 do for $j = 2 ^ { k }$ to 2k +1 -1 par- do

$$
A \left( j \right) = \operatorname* { m a x } \left\{ A \left( 2 j \right) , A \left( 2 j + 1 \right) \right\}
$$

# end for

end for

End

显然算法的时间 $t \left( n \right) = O \left( \log n \right)$ ,总比较次数为 $O ( n )$ ,而最大的处理器数 ${ \pmb { \mathscr { p } } } ( { \pmb { \mathscr { n } } } ) = { \pmb { \mathscr { n } } } / 2$ 。

# 6.3.2计算前缀和

对于取值于集合S上的满足二元结合运算 $^ { \star }$ 的 $\pmb { n }$ 个元素 ${ ( \pmb { x } _ { 1 } , \pmb { x } _ { 2 } , \cdots , \pmb { x } _ { n } ) }$ 的序列,所谓 $\pmb { n }$ 个元素的前缀和(Prefix-Sums)是指如下定义的 $\pmb { n }$ 个部分和(或积):

$$
s _ { i } = x _ { 1 } * x _ { 2 } * \cdots * x _ { i } , 1 { \leqslant i } { \leqslant n }
$$

显然，使用等式 $s _ { i } = s _ { i - 1 } \star x _ { i } ( 2 { \leqslant } i { \leqslant } n )$ 计算前缀和的平易的申行算法具有固有的顺序性,且时间为 $O ( n )$ 。

使用平衡二叉树计算前缀和时，在自叶向根正向遍历过程中，各内节点对其相应的子节点应用一次 $\bigstar$ 运算，因此每个节点 $_ { v }$ 保存了根在 $\pmb { v }$ 的子树的叶中所存储元素的和;在自根向叶反向遍历过程中，将计算出给定高度上各节点中所存储的元素的前缀和。

下面给出一个非递归求前缀和算法。令 $A \left( i \right) = x _ { i } \left( 1 { \leqslant } i { \leqslant } n \right)$ ;令 $B ( h , j )$ 和$C ( \boldsymbol { h } , \boldsymbol { j } )$ 是辅助变量集 $( 0 { \leqslant } h { \leqslant } \log n , 1 { \leqslant } j { \leqslant } n / 2 ^ { h } )$ ，其中数组 $B$ 用于记录正向遍历时树中各节点的信息,而数组 $c$ 用于记录反向遍历时树中各节点的信息。

算法6.9 SIMD-TC上非递归求前缀和算法 输入： $n = 2 ^ { k }$ 的数组 $A , k$ 为非负整数 输出：数组 $c$ ,其中 $c ( \mathbf { 0 } , j )$ 是第 $\pmb { j }$ 个前缀和 $( 1 { \leqslant } j { \leqslant } n )$ (1) for $j = 1$ to $\pmb { n }$ par -do $\big / \ast$ 初始化 $\yen 7$ $B ( 0 , j ) = A \left( j \right)$ end for

(2） for $h = 1$ to $\log n$ do $\big / \big \varkappa$ 正向遍历 $\yen 7$ for $j = 1$ to $n / 2 ^ { h }$ par -do$B \left( h , j \right) = B \left( h - 1 , 2 j - 1 \right) \ast B \left( h - 1 , 2 j \right)$ end forend for  
(3) for $\pmb { h } = \log \pmb { n }$ to 0 do $\big / \ast$ 反向遍历 $\yen 7$

for $j = 1$ to $\pmb { n } / 2 ^ { h }$ par - do

(i）if $j = \mathrm { e v e n }$ then $C ( h , j ) = C ( h + 1 , j / 2 ) \epsilon$ end if (ii）if $j = 1$ then $C ( h , 1 ) = B { \left( h , 1 \right) }$ end if （iii）if $j = \cosh \cosh \cosh \cosh$ then $C ( h , j ) = C ( h + 1 , ( j - 1 ) / 2 ) *$ $B ( h , j ) \mathrm { e n d i f }$

end for end for

End

# 6.4 倍增设计技术

倍增技术(Doubling Technique)又叫指针跳越(Pointer Jumping)技术,特别适合处理以链表或有向有根树之类表示的数据结构,在图论和链表算法中有着广泛的应用。每当递归调用时,所要处理的数据之间的距离将逐步加倍，经过 $\pmb { k }$ 步后就可完成距离为 $2 ^ { k }$ 的所有数据的计算。下面以表列中元素的位序(Rank)[简称表序问题(List Ranking Problem)]和求找森林的根为例,来说明此项技术的具体使用。

# 6.4.1表序问题的计算

令L是n个元素的表列，且每个元素分配一个处理器。所谓表序问题就是给表中每个元素k指定一个它在表列中的次第号(rank(k)）,rank(k)可视为元素k至表尾的距离。为此每个元素k都有一个指向下一个元素的指针 nect(k)。如果k是表中最后一个元素,则next(k)=k。具体算法形式描述如下：

# 算法6.10 SIMD-EREW上求元素表序算法

输入： $\pmb { n }$ 个元素的表列 $L$ 输出： $r a n k \left( k \right) , k \in L$

Begin

(1） for all $k \in L$ par -do (1.1) $P ( k ) = n e x t \left( k \right)$ (1.2) if P(k)≠k then distance(k)=1 else distance(k)= O end if end for

(2) repeat log n ]times (2.1) for all $k \in L { \mathrm { ~ p a r } } - \mathrm { d } \mathbf { 0 }$ if $P \ ( k ) { \neq } P ( P ( k ) )$ then

$$
d i s t a n c e ( k ) = d i s t a n c e ( k ) + d i s t a n c e ( P ( k ) )
$$

$$
P ( k ) = P ( P ( k ) )
$$

end if end for (2.2) for all k ∈ L par-do $r a n k \left( k \right) = d i s t a n c e \left( k \right)$ end for end repeat

End

显然,算法6.10的 $t { \big ( } n { \big ) } = O { \big ( } \log n { \big ) }$ ， ${ p ( n ) = n }$ 。

例6.4令 ${ \pmb n } = 7 .$ 。图6.7示例出算法6.10的执行过程。其中带箭头的弧为指针 $P ( k )$ ;弧上的数字为 $d i s t a n c e ( k )$ 的值。开始时,在算法6.10第(1.1)步 $P ( k )$ 进行初始化;在第(1.2)步计算出distance $( k )$ 的值。算法总共迭代三次，各元素的指针 $P ( k )$ 和 distance $( k )$ 依次标注在图6.7中。□

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0141-0210/auto/images/6fe06258922894d39002f09d625ee9ad565f4868e3d1c4e5d95e455202161e16.jpg)  
图6.7 $\pmb { n } = 7$ 算法6.10的执行过程

# 6.4.2 求森林的根

令森林 $F$ 是一组有根有向树,其中 $F$ 由长为 $\pmb { n }$ 的数组 $P$ 指定,使得如果 $( i$ ，$j )$ 是 $F$ 中的一条弧,则 $P ( i ) = j$ ,即 $j$ 是 $i$ 的父亲;如果 $_ i$ 是一个根,则 $P ( i ) = i ,$ 所谓找森林的根(Finding Roots of a Forest)的问题,就是对于每个节点 $j ( 1 \leqslant j \leqslant$ $^ { \textit { \textbf { n } } ) }$ ,确定包含该节点的树的根 $S ( j )$ 。开始时,每个节点 $_ i$ 的后继 $S ( i )$ 定义为$P ( i )$ 。指针跳越技术就是用后继的后继去修改每个节点的后继。重复使用此法，一个节点的后继就变成了越来越靠近树根的祖先。所以节点及其后继之间的距离将逐次加倍，经过 $k$ 次迭代后， $\pmb { i }$ 和 $\mathbb { S } ( i )$ 之间的距离则为 $2 ^ { k }$ 。算法的描述如下：

算法6.11 SIMD-CREW上求森林根的算法   
输入：森林 $\pmb { F }$ ,弧由 $( i , P ( i ) )$ 指定， $1 { \leqslant } i { \leqslant } n$   
输出：对每个节点 $\textbf { \em i }$ ,输出包含 $\textbf { \em i }$ 的树的根 $S ( i )$   
Begin for $1 { \leqslant } i { \leqslant } n$ par-do (1) $S ( i ) = P ( i )$ (2）while $S ( \mathfrak { i } ) { \neq } S ( S ( \mathfrak { i } ) )$ do $S ( \mathfrak { i } ) = S ( S ( \mathfrak { i } ) )$ end while end for   
End

令 $\hbar$ 是森林中树的最大高度,不难看出算法将迭代 $O ( \log  n )$ 次，每次选代作了O（n）次运算而花费了O(1)时间。所以算法的t（n）=O（logn），$W ( n ) = O ( n \log n ) ,$

例6.5图6.8中示例了使用指针跳越技术求森林的根的过程。本例中，如图6.8(a)所示，森林由两棵根在8和13的树组成。图中的弧相应于(i,P(i)）$( 1 { \leqslant } i { \leqslant } 1 3 )$ 。算法执行while语句的第一次循环后的结果如图6.8(b)所示,致使节点1,2,3,4,5,9,10和11改变它们的后继;第二次循环后如图 ${ \pmb 6 . 8 ( \mathfrak { c } ) }$ 所示，使得两棵树的高度都变为1。现在对于所有i,有S(i)=S(S(i)),所以算法结束。□(a)起始森林；(b)第一次迭代后的森林;(c)第二次迭代后的森林

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0141-0210/auto/images/91364ed5a5d83cedb403a47456129fd7b6dc28c5ffe37816b48a8af87d444ab5.jpg)  
图6.8求森林的根

# 6.5流水线设计技术

并行处理中,流水线(Pipelining)技术是一项重要的并行技术。它在VLSI并行计算中表现得尤为突出。其基本思想是将一个计算任务 $\pmb { t }$ 分成一系列子任务$t _ { 1 } , t _ { 2 } , \cdots , t _ { m }$ ,使得一旦 $t _ { 1 }$ 完成,后继的子任务就可立即开始,并以同样的速率进行计算。下面以一维心动(Systolic)阵列上离散傅氏变换(DFT)和卷积计算为例，说明流水线技术的使用。

# 6.5.1一维心动阵列上的DFT计算

一个 $\pmb { n }$ 点的离散傅里叶变换(Discrete Fourier Transform）,简记之为DFT,可定义为：给定序列 $( a _ { 0 } , a _ { 1 } , \cdots , a _ { n - 1 } )$ ,按如下规则变换成序列 $( b _ { 0 } , b _ { 1 } , \cdots , b _ { n - 1 } )$ ：

$$
b _ { j } = \sum _ { k = 0 } ^ { n - 1 } a _ { k } \omega ^ { k j } , 0 { \leqslant } j { \leqslant } n - 1
$$

其中， $\pmb { \omega }$ 是单位 $\pmb { n }$ 次元根，即 $\omega = e ^ { 2 \pi i / n }$ ， $\mathbf { i } = { \sqrt { - 1 } }$ 。

事实上(6.1)式的计算,可以等效于多项式求值：设想有一多项式 $_ { y } ( { \boldsymbol { x } } ) =$ $\sum _ { k = 0 } ^ { n - 1 } a _ { k } x ^ { k }$ ，叙求其在 $x = \omega ^ { j }$ $( 0 { \leqslant } j { \leqslant } n - 1 )$ 处的 $_ y ( x )$ 之值，即 $y ( \omega ^ { j } ) = \sum _ { k = 0 } ^ { n - 1 } a _ { k } \omega ^ { j k }$ 则显然此式和(6.1)式是完全一样的。

例如,欲计算一个5点的DFT,可以通过计算 $_ { \pmb { x } }$ 等于 $\omega ^ { 0 } , \omega ^ { 1 } , \omega ^ { 2 } , \omega ^ { 3 }$ 和 $\omega ^ { 4 }$ 处的如下多项式的值而求得：

$y \left( ⨏ _ { x } = \omega ^ { j } \right) = a _ { 4 } ( \omega ^ { j } ) ^ { 4 } + a _ { 3 } ( \omega ^ { j } ) ^ { 3 } + a _ { 2 } ( \omega ^ { j } ) ^ { 2 } + a _ { 1 } ( \omega ^ { j } ) ^ { 1 } + a _ { 0 }$ 即

$$
\left. \begin{array} { c } { { y ^ { \left( \omega ^ { 0 } \right) } = \alpha _ { 4 } \omega ^ { 0 } + \alpha _ { 3 } \omega ^ { 0 } + \alpha _ { 2 } \omega ^ { 0 } + \alpha _ { 1 } \omega ^ { 0 } + \alpha _ { 0 } } } \\ { { } } \\ { { y ^ { \left( \omega ^ { 1 } \right) } = \alpha _ { 4 } \omega ^ { 4 } + \alpha _ { 3 } \omega ^ { 3 } + \alpha _ { 2 } \omega ^ { 2 } + \alpha _ { 1 } \omega ^ { 1 } + \alpha _ { 0 } } } \\ { { } } \\ { { y ^ { \left( \omega ^ { 2 } \right) } = \alpha _ { 4 } \omega ^ { 8 } + \alpha _ { 3 } \omega ^ { 6 } + \alpha _ { 2 } \omega ^ { 4 } + \alpha _ { 1 } \omega ^ { 2 } + \alpha _ { 0 } } } \\ { { } } \\ { { y ^ { \left( \omega ^ { 3 } \right) } = \alpha _ { 4 } \omega ^ { 1 2 } + \alpha _ { 3 } \omega ^ { 9 } + \alpha _ { 2 } \omega ^ { 6 } + \alpha _ { 1 } \omega ^ { 3 } + \alpha _ { 0 } } } \\ { { } } \\ { { y ^ { \left( \omega ^ { 4 } \right) } = \alpha _ { 4 } \omega ^ { 1 6 } + \alpha _ { 3 } \omega ^ { 1 2 } + \alpha _ { 2 } \omega ^ { 8 } + \alpha _ { 1 } \omega ^ { 4 } + \alpha _ { 0 } } } \end{array} \right\}
$$

根据 Horner规则,(6.3)式可变换为如下的等效形式：

$$
\begin{array} { r l } & { y \big ( \omega ^ { 0 } \big ) = y _ { 0 } = \big ( \big ( \big ( \alpha _ { 4 } \omega ^ { 0 } + \alpha _ { 3 } \big ) \omega ^ { 0 } + \alpha _ { 2 } \big ) \omega ^ { 0 } + \alpha _ { 1 } \big ) \omega ^ { 0 } + \alpha _ { 0 } } \\ & { y \big ( \omega ^ { 1 } \big ) = y _ { 1 } = \big ( \big ( \big ( \alpha _ { 4 } \omega ^ { 1 } + \alpha _ { 3 } \big ) \omega ^ { 1 } + \alpha _ { 2 } \big ) \omega ^ { 1 } + \alpha _ { 1 } \big ) \omega ^ { 1 } + \alpha _ { 0 } } \\ & { y \big ( \omega ^ { 2 } \big ) = y _ { 2 } = \big ( \big ( \big ( \alpha _ { 4 } \omega ^ { 2 } + \alpha _ { 3 } \big ) \omega ^ { 2 } + \alpha _ { 2 } \big ) \omega ^ { 2 } + \alpha _ { 1 } \big ) \omega ^ { 2 } + \alpha _ { 0 } } \\ & { y \big ( \omega ^ { 3 } \big ) = y _ { 3 } = \big ( \big ( \big ( \alpha _ { 4 } \omega ^ { 3 } + \alpha _ { 3 } \big ) \omega ^ { 3 } + \alpha _ { 2 } \big ) \omega ^ { 3 } + \alpha _ { 1 } \big ) \omega ^ { 3 } + \alpha _ { 0 } } \\ & { y \big ( \omega ^ { 4 } \big ) = y _ { 4 } = \big ( \big ( \big ( \alpha _ { 4 } \omega ^ { 4 } + \alpha _ { 3 } \big ) \omega ^ { 4 } + \alpha _ { 2 } \big ) \omega ^ { 4 } + \alpha _ { 1 } \big ) \omega ^ { 4 } + \alpha _ { 0 } } \end{array}
$$

很明显，(6.4)式中所有的 $y _ { i } ( 0 { \leqslant } i { \leqslant } 4 )$ 都可以在图6.9所示的一维线性阵列上以流水线方式计算之。可以看出,每个 $y _ { i }$ 初始化为 $\alpha _ { 4 }$ （一般为 $a _ { n - 1 } )$ ，然后收集其有关项向右行进,当其积累完了所有项后,从最右单元输出。显然,在n－1=$O ( n )$ 个单元的心动阵列上,计算 $\pmb { n }$ 点DFT可在 $2 { \mathfrak { n } } - 1 = O ( { \mathfrak { n } } )$ 时间内完成。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0141-0210/auto/images/c07cf84973bd52f9fac9aed9d50ac9b6d3af51da44cc6365c738e89728746e7f.jpg)  
图6.9(a)处理单元功能及其定义;(b)5点DFT在一维阵列上的计算过程

# 6.5.2一维心动阵列上的卷积计算

卷积(Convolution)在数学上可定义如下:给定权序列(wi,w2,,wn）和x序列(x1,x2,…,xm),m>n,试按下式计算 y序列(y1,y2,.,ym-n+1):

$$
y _ { j } = \ \sum _ { i = 1 } ^ { n } \ W _ { i } X _ { i + j - 1 } , \ 1 { \leqslant j } { \leqslant m - n + 1 }
$$

卷积在数字信号处理、模式识别、多项式求值等方面应用很广泛。例如(6.5)式中的乘、加代之以“比较”和“布尔与"操作，则卷积问题就变成了模式匹配问题。因为每个y；可在(n)时间内计算出，所以卷积可在@(nm)时间内计算完毕。

例如,给定4个权的序列(w1,W2,\~3,W4)和6个数的序列(𝑥1,x2,x3,$x _ { 4 } , x _ { 5 } , x _ { 6 } )$ ,则须计算如下的 $_ y$ 序列 $( y _ { 1 } , y _ { 2 } , y _ { 3 } )$ ：

$$
\left. { \begin{array} { r } { y _ { 1 } = x _ { 1 } w _ { 1 } + x _ { 2 } w _ { 2 } + x _ { 3 } w _ { 3 } + x _ { 4 } w _ { 4 } } \\ { y _ { 2 } = x _ { 2 } w _ { 1 } + x _ { 3 } w _ { 2 } + x _ { 4 } w _ { 3 } + x _ { 5 } w _ { 4 } } \\ { y _ { 3 } = x _ { 3 } w _ { 1 } + x _ { 4 } w _ { 2 } + x _ { 5 } w _ { 3 } + x _ { 6 } w _ { 4 } } \end{array} } \right\}
$$

当在一维心动阵列上计算上述卷积时需要4个处理单元 $C _ { 1 } { \setminus } C _ { 2 } \setminus C _ { 3 }$ 和 $C _ { 4 }$ ,其中每个 $C _ { i }$ 中存有 ${ \boldsymbol { \mathsf { w } } } _ { i }$ ,且执行(6.5)式计算。计算时，如图6.10所示，输人序列$x _ { 1 } \sim x _ { 6 }$ 由左方进人心动阵列，输出序列 $y _ { 1 } \sim y _ { 3 }$ 由右方进人心动阵列。开始时， $_ { \pmb { x } }$ 的元素每隔一拍流人阵列,而 $\pmb { y }$ 的元素须延迟3拍后也每隔一拍流人阵列。在前3拍时不作任何计算;而第4拍时 $C _ { 1 }$ 执行 $y _ { 1 } + x _ { 1 } \mathbf { w } _ { 1 }$ 操作( $\lvert _ { y _ { 1 } }$ 初始化为零)；类似地,在第5拍时C执行y1+xW2;在第6拍时,C和C分别同时计算y和y1所需的项。般而言,当C接收到xi和y；时,则执行操作xi+yj。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0141-0210/auto/images/3d4321887a0dd26ee4746e6885514f2587dd4c31bde0d3e570b0ba2947d6b481.jpg)  
图6.10卷积在一维心动阵列上的执行过程

一般情况下，当权数为n和输入序列长度为m时，须用n个心动单元，y序列需滞后n-1个拍。因为y需要计算(m－𝑛+1)个元素，所以总共约需2(m－n)个节拍。当n<m时,此算法的成本为@(mn),显然是成本最优的。

# 6.6小结和导读

小结本章所介绍的都是并行算法设计的最基本的技术,远非所有的设计技术。这些技术虽具有一定的普适性,但也并非对所有问题均行之有效,况且也不全面,同时也只能作为设计并行算法的一般性指南，绝非是可直接引用的手册。其它的设计技术还有破对称(Symmetry Breaking)技术,它是打破某些问题的对称性的一种设计方法，在图论问题和随机算法中经常使用；加速级联（Ac-celerated Cascading)技术,它试图将一个最优但相对不快的算法与另一个非常快但非最优的算法"串接"起来,形成一个快速最优的算法，此法虽不具有普适性，但对有些问题却效果甚佳;随机法是在算法设计时,引入随机性使得算法在执行时,可以随机地选择下一执行步，从而可望得到平均性能较好的算法(即其复杂度比同一问题的确定性算法的最坏情况的复杂度要好),随机算法设计简单，但分析较复杂，经常要分析算法可在多少时间步内以多大的概率结束，用随机法设计的算法，其运行结果也可能是不正确的,但这种错误的概率应是很小的；贪心法(Greedy Method)是一种最直接的设计技术,其设计特点是,在算法的每一步都力图确保获得局部最优，这种设计方法的副作用是容易陷人局部最优。对于组合问题的算法设计技术,有动态规划法(Dynamic Programming),它是在每一判定步,列出多种可能的解，然后按照某种条件，舍弃那些肯定不能导致最优解的局部解，它和贪心法的区别在于，贪心法仅产生一个判定序列,而动态规划法可能产生很多判定序列，但依据“最优性原理”,非局部最优解的序列肯定不是最优的，所以不予考虑；回溯法(Backtracking)是一种穷举法,在问题求解时常使用深度优先搜索(Depth-First Searching)法,在搜索过程中，一旦碰到某个无法搜索下去的分支，就向其父节点回溯,再搜索该父节点的其它分支，如果所有的分支节点均无希望的解,则再向上追溯，如此等等,回溯法虽提供了一种规律性求解的方法，但其时间复杂度较高;分支界限法(Branchand Bound)与回溯法颇类似,但它是基于广度优先搜索(Breadth-First Searching)法，它利用部分解的最优性信息，避免考虑那些不能导致最优的解，以加快问题的求解，其解题过程是：对解集合反复进行分支，即反复构造其子集合，每次分支时都对所得到的子集合计算最优解的界，若它不能优于当前已知的最优解，则对此子集合就不再进行分支，否则继续分支，以探索更好的解，直到所得的子集合仅有一个解为止。

导读有关PSRS排序算法的设计和分析，读者可参阅[157];使用平方根划分法的归并算法是由Valiant提出[175];使用对数划分法的归并算法,读者可参阅[158];有关(m,n)-选择算法，读者可参阅[189]。分治方法的一般介绍，读者可参阅[97]；双调归并网络是由Batcher提出[26];用分治法求凸壳问题，读者可参阅[156]。并行前缀和计算,读者可参阅[116]。表序计算问题,读者可参阅[185];倍增技术在图论中的应用,Hirschberg求连通分量是一篇常被人引用的文章[93]。关于心动阵列的并行计算,[115]是一篇很经典的文章。加速级联技术由Cole等人提出[51];破对称设计技术,读者可参阅[77]。在[104]书的第九章专门讨论了随机算法。组合问题的算法设计技术,读者可参阅[179]。

# 习 题

6.1 $\textcircled{1}$ 试证明：当 $\scriptstyle \pmb { n } \geqslant \pmb { \phi } ^ { 3 }$ 时，算法6.1的时间复杂度为 $O \left( { \frac { n } { p } } \log n \right)$

$\textcircled{2}$ 令 $\boldsymbol { w _ { i } ^ { j } }$ 表示 $P _ { i }$ 中第 $j$ 段中的元素数,试证明算法6.1在执行过程中，处理器中所积累的元素数目不会超过 $2 n / \beta$ ，即 $\sum _ { j = 1 } ^ { P } w _ { i } ^ { j } < \frac { 2 n } { p } ,$

6.2 $\textcircled{1}$ 试举一典型算例,说明Valiant归并算法的执行过程。

$\textcircled{2}$ 试分析算法6.2所需的处理器数 ${ p ( n ) = O ( n ) }$ 0$\textcircled{3}$ 试证明算法6.2的时间复杂度为： $2 \log \log n + \mathrm { c o n s t } _ { \circ }$

6.3 $\textcircled{1}$ 试分析算法6.3的复杂度。

$\textcircled{2}$ 令 $A =$ (0,1,2,7,9,11,16,17,18,19,23,24,25,27,28,30,33,34), $B = ( 3 , 4 , 5 , 6 , 8 ,$ 10,12,13,14,15,20,21,22,26,29,31)。试按算法6.3,将其进行对数划分,并最终 将它们归并之。

6.4 $\textcircled{1}$ 试举一例，说明算法6.4的执行过程。

$\textcircled{2}$ 试证明算法6.4的正确性。

6.5 $\textcircled{1}$ 试证明Batcher定理。

$\textcircled{2}$ 画出一个16个输入的双调归并网络。

6.6 $\textcircled{1}$ 试分析算法6.9的总运算量 $\textstyle \mathbf { W } ( n ) = ?$

$\textcircled{2}$ 假定序列为(1,2,3,4,5,6,7,8),试用算法6.9求其前缀和。

6.7定义 $\log ^ { ( i ) } x$ 如下： $\log ^ { ( 1 ) } x = \log x , \log ^ { ( 2 ) } x = \log \log x , \log ^ { ( i ) } x = \log ( \log ^ { ( i - 1 ) } x )$ 。令函数$\log ^ { * } x = \operatorname* { m i n } \{ i \mid \log ^ { ( i ) } x { \leqslant } 1 \} \ ,$

当 $x { \leqslant } 2 ^ { 6 5 5 3 6 }$ 时,此函数界限是什么？

6.8对于 $\pmb { n = 8 }$ ,按照DFT定义，计算 $\pmb { w }$ 矩阵之各元素。

6.9试解释在一维心动阵列上计算卷积时，序列 $_ { x }$ 和 $_ y$ 为何要各间隔一拍进人阵列。

6.10顶点倒塌法是非常有名的求图的连通分量的算法,其基本思想是：连通的相邻的顶点可以合并成一个超顶点,并以它们中最小标号者标记之；此过程可继续在已合并的超顶点之间进行。在下列的算法中， $C ( i )$ 表示与 $\pmb { i }$ 相邻的最小的超顶点号码； $D ( i )$ 表示顶点 $\dot { \pmb { \mathscr { \imath } } }$ 所属连通分量的最小标号的顶点； $C ( \mathbf { \Phi } _ { i } ) = \operatorname* { m i n } _ { \mathbf { \Phi } _ { j } } \{ D ( \mathbf { \Phi } _ { j } ) \ \mid \ _ { A ( \mathbf { \Phi } _ { i } , \mathbf { \Phi } _ { j } ) = 1 , D ( \mathbf { \Phi } _ { i } ) \neq D ( \mathbf { \Phi } _ { j } ) } \}$ 语句为每个顶点 $_ i$ 找与它不属于相同分量的相邻的最小号码的顶点 $j$ ；语句 $C \left( \mathrm { \ i \right) = }$ $\operatorname* { m i n } _ { j } \{ C ( j ) ~ \vert ~ \smash { \cal D } ( j ) = i , C ( j ) \ne i \}$ 表示把每个超顶点的根连到最小号码的相邻的超顶点的根上。Hirschberg的求连通分量算法如下：

# 算法6.12 PRAM-CREW上Hirschberg求连通分量算法

输入：邻接矩阵 $\mathbf { A } _ { n } \mathbf { \times } _ { n }$

输出：向量 $\pmb { D } [ \pmb 0 : \pmb { n } - 1 ]$ ,其中 $D ( i )$ 表示向量 $\pmb { D }$ 的分量

Begin(1） for all $i \colon 0 { \leqslant } i { \leqslant } n - 1$ par -do /\*初始化\*/$D ( i ) = i$ end fordo step (2)through ( $6 ) \mathrm { f o r } \Gamma \mathrm { l o g } n$ literations:(2) for all $i , j \colon 0 { \leqslant } i , j { \leqslant } n - 1 \quad \mathrm { p a r } ^ { - } \mathrm { d } \mathbf { 0 }$ $\big / \varkappa$ 找相邻的最小者 $\divideontimes$ /(2.1) $C ( \mathbf { \Phi } _ { i } ) = \operatorname* { m i n } _ { \mathbf { \Phi } _ { j } } \{ D ( \mathbf { \Phi } _ { j } ) \ \mid _ { \mathbf { \Phi } _ { A } ( \mathbf { \Phi } _ { i } , \mathbf { \Phi } _ { j } ) = 1 \mathrm { ~ a n d ~ } D ( \mathbf { \Phi } _ { i } ) \neq D ( \mathbf { \Phi } _ { j } ) } \}$ (2.2） if none then $C ( i ) = D ( i )$ endifend for(3) for all $i , j \colon 0 { \leqslant } i , j { \leqslant } n - 1 \quad \mathrm { p a r } ^ { - } \mathrm { d } \mathbf { 0 }$ $\big / \varkappa$ 找每个超顶点的最小相邻超顶点 $\divideontimes$ /(3.1) $C ( \mathbf { \phi } _ { i } ) = \underset { \mathbf { \phi } _ { j } } { \min } \{ C ( \mathbf { \phi } _ { j } ) ~ \left| ~ \ _ { D ( \mathbf { \phi } _ { j } ) } = \mathbf { \phi } _ { i } \ \mathrm { a n d } ~ C ( \mathbf { \phi } _ { j } ) \neq \mathbf { \phi } _ { i } ~ \right\}$ (3.2） if none then $C ( i ) = D ( i )$ endifend for(4) for all i: $0 { \leqslant } i { \leqslant } n - 1$ par-do $D ( i ) = C ( i )$ end for(5）for $\lceil \log n$ literations do $\big / \ast$ 指针跳越,找各顶点新的超顶点 $\yen 7$ for all i : $0 { \leqslant } i { \leqslant } n - 1 \quad { \mathrm { p a r } } - { \mathrm { d o } } \ C ( i ) = C ( C ( i ) )$ end forend for(6) for all i: $0 { \leqslant } i { \leqslant } n - 1$ par-do$D ( i ) { = } \operatorname* { m i n } \{ C ( i ) , D ( C ( i ) ) \}$ end for  
End

$\textcircled{1}$ 试分析算法6.12的复杂度 $\ t ( \pmb { n } ) = ?$ 和 $\textstyle \mathbf { \hat { \Gamma } } \mathbf { \hat { \Gamma } } ( { \boldsymbol { \mathsf { n } } } ) = ?$ $\textcircled{2}$ 给定如图6.11所示无向图,试用算法6.12逐步求出该图的连通分量。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0141-0210/auto/images/819cf614998d590b247bd20e7cf976eaa23cb082e47a549dd519dd064c2bad46.jpg)  
图6.11待求连通分量的无向图

# 第七章 并行算法的一般设计过程

设计一个高效的并行算法并非易事,其过程比较复杂,很难归结为一个单一化的过程而“一步到位”，往往需要几经反复方能达到要求。

本章试图从给定问题的描述出发，通过一系列步骤，最终设计出一个能展示出并发性、可扩放性、局部性和模块性的并行算法。此过程可分为四步，即任务划分（Partitioning）、通信（Communication）分析、任务组合（Agglomeration）和处理器映射(Mapping),简称为PCAM设计过程,它是一种设计方法学，是实际设计并行算法的自然过程,其基本要点是：首先尽量开拓算法的并发性和满足算法的可扩放性;然后着重优化算法的通信成本和全局执行时间，同时通过必要的整个过程的反复回溯,以期最终达到一个满意的设计选择。

上述设计过程的最后阶段是映射，也就是将经过优化的诸进程指派给具体的处理器去运行。这样PCAM算法设计过程的最终结果将是一个并行程序。所以就此意义而言,本章所讲的并行算法的设计过程,有时也不加严格区分地应用到并行程序的设计上。

# 7.1 PCAM设计方法学

已如上述,PCAM是 Partitioning、Communication、Agglomeration 和 Mapping首字母的拼写，它们代表了使用此法设计并行算法的四个阶段。其中在设计的前期主要考虑如并发性等与机器无关的特性，在设计的后期才考虑与机器有关的特性。也就是说,在设计的第一和第二阶段，关注的是并发性和可扩放性，并寻求开发出具有这些特性的并行算法，在设计的第三和第四阶段，才把注意力转移到局部性和别的与性能有关的问题上。并行算法设计的整个过程可概括于图7.1中，它从给定设计问题的说明开始，寻找一种计算任务的划分方法,确定诸任务的通信要求，组合可能的计算任务，最后将优化了的诸任务指派给实际的处理器。上述各阶段可简述如下：

$\textcircled{1}$ 划分：将整个计算分解成一些小的任务，其目的是尽量开拓并行执行的机会。  
$\textcircled{2}$ 通信：确定诸任务执行中所需交换的数据和协调诸任务的执行，由此可检测上述划分的合理性。

$\textcircled{3}$ 组合：按性能要求和实现的代价来考察前两阶段的结果,必要时可将一些小的任务组合成更大的任务以提高性能或减少通信开销。

$\textcircled{4}$ 映射：将每个任务分配到一个处理器上,其目的是最小化全局执行时间和通信成本以及最大化处理器的利用率。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0141-0210/auto/images/cf2afa34ed378b4d8d94ed91de2f335a4c29163b5096b817c85c434c99206390.jpg)  
图7.1算法的 PCAM设计过程

虽然上述的设计过程是一步一步进行的,但实际上它们可以同时一并考虑；同样，虽然我们希望一个算法能用上述四步一次设计成功，但实际上设计过程的回溯反复总是难免的。

# 7.2划 分

所谓划分，就是使用域分解或功能分解的办法将原计算问题分割成一些小的计算任务，以充分揭示并行执行的机会，这犹如细小的砂粒比大块的砖瓦易于灌注一样，划分以充分开拓算法的并发性和可扩放性为目的；其方法是先集中数据的分解(称域分解),然后是计算功能的分解(称功能分解),两者互为补充；划分的要点是力图避免数据和计算的复制，应使数据集和计算集互不相交。

# 7.2.1域分解

域分解(Domain Decomposition)也叫数据划分。所要划分的对象是些数据，这些数据可以是算法(或程序)的输入数据,计算的输出数据,或者算法所产生的中间结果。

域分解的步骤是，首先分解与问题相关的数据，如果可能的话，应使这些小的数据片尽可能大致相等；其次再将每个计算关联到它所操作的数据上。由此划分将会产生一系列的任务。每个任务包括一些数据及其上的操作。当一个操作可能需要别的任务中的数据时，就会产生通信要求。

域分解的经验方法是，优先集中在最大数据的划分；或者那些经常被访问的数据结构上。在计算的不同阶段，可能要对不同的数据结构进行操作，或者需要对同一数据结构进行不同的分解，在此情况下，我们要分别对待，然后考虑将各阶段设计的分解和算法装配到一起。

图7.2示出了一个三维网格的域分解方法，在各格点上计算都是重复执行的,分解在X,Y和/或Z维是可能的，开始时，应集中在能提供最大灵活性的三维(即3-D)分解上，即每一个格点定义一个计算任务，每个任务维护与其格点有关的各种数据，并负责计算以修改状态。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0141-0210/auto/images/f1a365697128ccce64bc9e838086906e65be82ab6a038c3e9b00281b957fbea8.jpg)  
图7.2三维网格问题的域分解法(各图中的阴影部分代表一个任务）

# 7.2.2功能分解

功能分解(FunctionalDecomposition)也叫计算划分,其基本出发点不同于域分解,它首先关注于被执行的计算上，而不是计算所需的数据上；然后，如果所作的计算划分是成功的，再继续研究计算所需的数据，这些数据可能是不相交的，这就意味着划分很成功；或者这些数据有相当的重叠，这就产生大量的通信，此时就暗示应考虑数据分解。

尽管域分解是绝大多数并行算法所使用的，但功能分解却有时能揭示问题的内在结构展示出优化的机遇，而对数据单独进行研究却往往难以作到这一点。

搜索树是功能分解的最好例子，此时无任何明显的可分解的数据结构，但却易于进行细粒度的功能分解：开始时根生成一个任务，对其评价后，如果它不是一个解，就生成一棵搜索子树,整个搜索过程如图7.3所示，自根以波前(Wave-front)形式逐级向树叶推进(见习题7.1)。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0141-0210/auto/images/cc012809f6392d39612913262dca603a84004595ee8252e63e13b7061bbd7135.jpg)  
图7.3功能分解的搜索树

# 7.2.3划分判据

下面的一组问答题,可检验你所作的划分有无明显的缺陷。原则上讲,它们应得到肯定的回答：

$\textcircled{1}$ 你所划分的任务数,是否至少高于目标机上处理器数目的一个量级？如果不是，则你在后继的设计步骤中将缺少灵活性。  
$\textcircled{2}$ 你的划分是否避免了冗余的计算和存储要求,如果不是,则所产生的算法对大型问题可能是不可扩放的。  
$\textcircled{3}$ 诸划分的任务是否尺寸大致相当,如果不是,则分配处理器时很难做到工作量均衡。  
$\textcircled{4}$ 划分的任务数是否与问题尺寸成比例？理想情况下,问题尺寸的增加应引起任务数的增加而不是任务尺寸的增加。如果不是这样，则你的算法可能不能求解更大的问题，尽管有更多的处理器。  
③确认你是否采用了几种不同的划分法，多考虑几种选择可提高灵活性，同时既要考虑域分解又要考虑功能分解。

# 7.3通 信

由划分所产生的诸并行执行的任务，一般而言都不能完全独立执行，一个任务中的计算可能需要用到另一个任务中的数据,从而就产生了通信要求。所谓通信，就是为了进行并行计算，诸任务之间所需进行的数据传输。

在域分解中，通常难以确定通信要求，因为将数据划分成不相交的子集并未充分考虑在数据上执行操作时可能产生的数据交换，在功能分解时，通常容易确定通信要求，因为并行算法中诸任务之间的数据流就相应于通信要求。

在讨论通信时，将通信分成以下四种模式：

$\textcircled{1}$ 局部/全局通信：局部通信时，每个任务只与较少的几个近邻通信；全局通信中，每个任务与很多别的任务通信。  
$\textcircled{2}$ 结构化/非结构化通信：结构化通信时，一个任务和其近邻形成规整结构（如树、网格等);非结构化通信中，通信网则可能是任意图。  
$\textcircled{3}$ 静态/动态通信：静态通信，通信伙伴的身份不随时间改变，动态通信中，通信伙伴的身份则可能由运行时所计算的数据决定且是可变的。  
$\textcircled{4}$ 同步/异步通信：同步通信时，接收方和发送方协同操作;异步通信中，接收方获取数据无需与发送方协同。

# 7.3.1局部通信

当某一操作仅要求从近邻的其它任务获取数据时，就呈现局部通信(LocalCommunication)模式。一个典型的例子就是数值计算中的雅可比有限差分法(Finite Difference Method)。对于二维网格,可以使用5点格式(Five-Point Sten-cil)计算诸格点 $_ { \pmb { x } }$ 之值(参见第十章第10.4.2节)：

在迭代过程中,要求计算一系列 $x _ { i , j } ( 1 ) , x _ { i , j } ( 2 ) , x _ { i , j } ( 3 ) \cdots$ 之值。如图7.4,每个 $x _ { i , j } ( k )$ 之计算,都用其周围四个格点的值,其算法如下：

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0141-0210/auto/images/56e97e97db9bfbbc622e0e2971bbd41fdbf2da68732f2f7b20124d4e73f07037.jpg)  
图7.4二维网格雅可比5点差分格式的局部(四近邻)通信模式

# Begin

$\mathbf { f } \mathbf { 0 r } k \ = \ 1$ to $T$ do

（1）send $x _ { i , j } \ ( \ k \ - 1 )$ to each neighbor （2）receive $x _ { i - 1 , j } ( k - 1 ) , x _ { i + 1 , j } ( k - 1 ) , x _ { i , j - 1 } ( k - 1 ) , x _ { i , j + 1 } ( k - 1 ) f r o m$ neighbors (3) compute xi, (k)using Equation(7.1) end for End

雅可比方法易于并行化，所有格点可同时更新，但收敛速度较慢。改进的Gauss - Seidel 法如下：.

$$
\tau _ { i , j } \left( k \right) = \frac { 4 x _ { i , j } \left( k - 1 \right) + x _ { i - 1 , j } \left( k \right) + x _ { i + 1 , j } \left( k - 1 \right) + x _ { i , j - 1 } \left( k \right) + x _ { i , j + 1 } \left( k - 1 \right) + x _ { i - 1 , j - 1 } \left( k \right) } { 8 } .
$$

它迭代时利用了一半新值，一半旧值，虽加快串行迭代速度，但都不易并行化，为此出现了不少变体方案，如著名的红－黑着色(Red-Black Coloring)法（详见第十章有关章节)。总之，简单的Gauss-Seidel更新策略在串行算法中很有效,而在并行机上不理想,朴素的雅可比更新策略在并行机上很有效，但收敛不快，而红黑着色的更新策略组合了它们的优点，故应用很广。

# 7.3.2全局通信

全局通信(GlobalCommunication)系指有很多任务参与交换数据的一种通信模式,这种方式，可能导致过多的通信从而限制了并行执行的机会。

一个顺序求和算法 $S = \sum _ { i = 0 } ^ { N - 1 } x _ { i }$ ,就呈现出全局通信要求。如图7.5所示，一个根进程 $s$ ,负责从 $\pmb { n }$ 个分布式任务中一次接收一个值并相加之：

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0141-0210/auto/images/ceb6871ff704ae1851a34821ef6998722cff411f9701ebb70516c22ba6257fda.jpg)  
图7.5集中式顺序求和

显然,这种集中控制式的依次求和方式,妨碍了有效并行执行,为此,可以使

用分治策略来开拓求和的并行性：

$$
\sum _ { i = 0 } ^ { 2 ^ { n } - 1 } \ = \ \sum _ { i = 0 } ^ { 2 ^ { n - 1 } - 1 } \ + \ \sum _ { i = 2 ^ { n - 1 } } ^ { 2 ^ { n } - 1 }
$$

上式右边的两个求和可同时进行，且每个仍可按同样方式进一步分解之。图7.6示出了 $N = 8$ 的分治求和树，由此可见，分治法一方面提高了算法的并行度；同时也可将全局通信化为局部通信。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0141-0210/auto/images/56ce126ad6151e0da83222eaf34e7ae4466d7de4480b19123e339d72dff7913b.jpg)  
图7.6 $N = 8$ 时的分治求和树

# 7.3.3非结构化、动态和异步通信

在静态的、结构化通信中,一个任务的通信伙伴形成一个规则的模式(如树、网格等),并且不随时间变化;而非结构化、动态通信则不然，模式不规整且又随时间变化。

非结构化的通信模式,对算法设计的前期不会造成实质性的困难，但却复杂化了任务的组合与处理器的映射,特别是当要求组合策略既能创建尺寸大致相等的任务，又能尽量减少任务间的通信要求时，就要求非常复杂的算法，而这些算法在通信要求是动态时又会在算法的执行中频繁地使用，所以必须权衡这些算法的利弊。

在同步通信中,通信中的双方均知道何时将要产生通信操作,所以发送者就显式地发送数据给接收者,在异步通信(Asynchronous Communication）中，发送者不能确定接收者何时需要数据,所以接收者要明确地(显式地)从发送者请求数据。例如,消息传递(Message-Passing)式通信方式就属异步通信。

# 7.3.4通信判据

下面的一组问答题,可检验你所作的通信设计是否合理。原则上讲,应给予它们肯定的回答：

$\textcircled{1}$ 所有任务是否均执行大致同样多的通信？如果不是，则所设计的算法的可扩放性可能是不好的。  
$\textcircled{2}$ 每个任务是否只与少许的近邻相通信？如果不是，则可能导致全局通信，在此情况下，应设法将全局通信结构化为局部通信结构。  
$\textcircled{3}$ 诸通信操作是否能并行执行？如果不是，则所设计的算法很可能是低效的和不可扩放的,在此情况下,设法试用分治技术来开发并行性。  
$\textcircled{4}$ 不同任务的计算能否并行执行？如果不是,则所设计的算法很可能是低效的和不可扩放的，在此情况下,可考虑重新安排通信/计算之次序等来改善之。

# 7.4组 合

在设计的第一和第二阶段,划分了任务并考虑了任务间的通信,不过所得到的算法仍是抽象的,因为并未考虑它在任何特定的并行机上的执行效率,在第三阶段，即组合(Agglomeration)阶段，将从抽象转到具体，即重新考察在划分和通信阶段所作的决择,力图得到一个在某一类并行机上能有效执行的并行算法。

组合的目的是通过合并小尺寸的任务来减少任务数，但它仍可能多于处理器的数目,理想的情况是,在组合时就将任务数减少到恰好每个处理器上一个，从而得到一个SPMD的程序,这时映射也宣告完成,另外,组合时我们也要考虑是否值得进行数据和/或计算的重复(Replication)。

用增加计算和通信的粒度的办法可减少通信成本,组合时要保持足够的灵活性同时要减少软件工程代价。这几个相互矛盾的准则在组合阶段要仔细考虑。

# 7.4.1增加粒度

在设计过程的划分阶段，致力于定义尽可能多的任务以增大并行执行的机会。但是定义大量的细粒度任务不一定能产生一个有效的并行算法，因为大量细粒度任务有可能增加通信代价和任务创建代价。

表面-容积效应(Surface-to-Volume Effects） 如果每个任务的通信伙伴是少的,则增加划分粒度常能减少通信次数，同时还能减少总通信量，参照图7.7来阐述所谓"表面-容积效应”：一个任务的通信需求比例于它所操作的子域的表面积,而计算需求却比例于子域的容积。在一个二维问题中，“表面积”比例于问题的尺寸,而"容积"比例于问题尺寸的平方。因此一个计算单元的通信/计算之比随问题(任务)尺寸的增加而减少。

图7.7(a)和(b)分别示出了细粒度和粗粒度的二维网格上5点法计算有限差分：在(a)中， ${ \bf 8 } \times { \bf 8 }$ 的网格上，计算被划分成 ${ 8 \times 8 = 6 4 }$ 个任务，每个任务负责计算一个格点;而在(b)中,同一计算问题被划分成 $2 \times 2 = 4$ 个任务，每个任务负责16个格点的计算。在(a)中，共需要 $6 4 \times 4 = 2 5 6$ 次通信，每个任务通信4次，总共传输256个数据值;而在(b)中，仅要求 $4 \times 4 = 1 6$ 次通信，总共传输 $1 6 \times 4$ $= 6 4$ 个数据值,可见同一计算问题,粗粒度划分的通信次数和通信量均比细粒度划分时有所下降。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0141-0210/auto/images/ebdd06e3d730330aba380ccf71e909a89f4fa3965998783a03e3618153636706.jpg)  
图7.7在二维网格5点差分格式中,增加粒度对通信成本的影响

表面-容积效应启发我们,在其它条件等同的情况下,高维分解一般更有效。因为相对于一个给 定的容积(计算)它减少了表面积(通信)。因此从效率的角度,增加粒度的最好办法是在所有的维组合任务。

重复计算（Replication Computation）它也称为冗余计算。有时候可以采用不必要的多余的计算的方法来减少通信要求和/或执行时间。仍以二叉树上的求和 $\sum _ { i \mathop { = } 0 } ^ { N - 1 } x _ { i }$ 为例来说明之。

假定在二叉树上用 $N$ 个处理器来求 $N$ 个数的全和，且要求每个处理器上均保持最终的全和。为此如图7.8所示，必须先自叶向根逐级求和；然后自根向叶将全和逐级播送给每个处理器，共需 $2 \log N$ 步。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0141-0210/auto/images/79fdff8d03950fc9bf5c0bddd45e78a9d9b3854b1c748369b22249adb1682332.jpg)  
图7.8二叉树上求全和

以上述方式求和时,处理器的利用率是逐级减半的,如果在树的每一级都充分利用所有的处理器参与计算，即在树的每一级,每个处理器(任务)均接收两个数据,执行一次局部求和,然后再发送结果至下一级的两个处理器,那么经过logN 级后，每个处理器中均积累了全和 $\sum _ { i = 0 } ^ { N - 1 } x _ { i }$ 。如图7.9所示,这实际上就是蝶式通信结构,它利用了重复计算的方法,只需 $\log N$ 步就可在各处理器中积累了最终的全和,但却以总共施行 $O \left( N \mathrm { l o g } N \right)$ 次计算和通信操作为代价。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0141-0210/auto/images/1f7c6eb03d577a9380fce0a7724ee9c9fea7d62b62eff1f854631307e41cc05e.jpg)  
图7.9使用蝶式通信结构求全和

当对通信需求分析揭示了一组任务不能同时执行时，组合总是有益的，例如,用图7.8所示二叉树和图7.9所示蝶式图进行求和时，只有在树的和蝶式图的同一级中的任务方能同时执行，这样不同级中的任务可组合到一起而不会减少并行执行的机会,同时也可能产生优化的通信结构(参见习题7.3和7.4)。

# 7.4.2保持灵活性和减少软件工程成本

组合的主要目的是提高效率和减少通信成本,但也要注意保持足够的灵活性和降低软件工程代价。

在组合时，易于作出对算法的可扩放性带来不必要限制的决定,要维持一个算法(或程序)的可移植性和可扩放性，则创建可变数目的任务是很关键的，而组合时往往会使问题的任务数的变化范围受到限制。为了易于在映射时平衡负载,组合后的任务数,按照经验，至少应比处理器的数目多一个量级。其最优的任务数可由分析模型和实际经验共同决定。但灵活性也不一定需要一个设计总是创建大量的任务。粒度可由编译或运行参数来控制。重要的是，一个设计不要对能够生成的任务数加人不必要的限制。

组合时另一个应关心的问题是尽量减少软件工程代价,当并行化一个串行代码时,应尽量减少代码的巨大变化以减少软件开发开销,由此观点出发,最感兴趣的策略就是那些在算法设计时不需要大量修改代码的策略。

# 7.4.3组合判据

下面的一组问答题,可检验组合设计是否合理,原则上讲,应给予它们肯定的回答：

$\textcircled{1}$ 用增加局部性方法施行组合是否减少了通信成本？如果不是,检查能否由别的组合策略来达到。  
$\textcircled{2}$ 如果组合已造成重复计算，是否已权衡了其得益？  
$\textcircled{3}$ 如果组合已重复了数据,是否已证实这不会因限制问题尺寸和处理器数的变化范围而牺牲了可扩放性？  
$\textcircled{4}$ 由组合所产生的任务是否具有类似的计算和通信代价？  
$\textcircled{5}$ 任务数目是否仍然与问题尺寸成比例？如果不是,算法则是不可扩放的。  
$\textcircled{6}$ 如果组合减少了并行执行的机会，是否已证实现在的并发性仍能适应目前和将来的并行机？  
②在不导致负载不平衡,不增加软件工程代价和不减少可扩放性的前提下,任务数能否再进一步减少,在其它条件等同时,创建较少的大粒度的任务算法通常是简单高效的。  
⑧如果并行化现有的串行程序,是否考虑了修改串行代码所增加的成本？如果此成本是高的，应考虑别的组合策略，它能增加代码重用的机会。

# 7.5映 射

在设计的最后阶段,我们要指定每个任务到哪里去执行,此即映射（Map-ping)。开发映射的主要目的是减少算法的总的执行时间，其策略有二：一是把那些能够并发执行的任务放在不同的处理器上以增强并行度；二是把那些需频繁通信的任务置于同一个处理器上以提高局部性。这两个策略有时会冲突，这就需要权衡。

对于两个处理器而言,映射问题有最佳解;当处理器的数目大于等于3时，此问题是NP完全问题,但我们可以利用关于特定策略的知识，用启发式算法来获得有效的解。

在进行映射时,对于许多用域分解技术开发的算法，有固定数目的等尺寸任务,有结构化的局部/全局通信,此时映射很简单；对于更复杂的域分解算法,每个任务的工作量可能不一样,通信也许是非结构化的，有效的组合就不那么容易，此时可能要采用负载平衡算法。

在基于功能分解的算法中，常常会产生一些由短暂任务组成的计算，它们只在执行的开始与结束时需与别的任务协调，此时我们可以用任务调度（Task-Scheduling)算法来分配任务给那些可能处于空闲状态的处理器。

# 7.5.1负载平衡算法

基于域分解技术的算法有很多专用和通用的负载平衡技术(Load-BalancingTechniques),它们都是试图将划分阶段产生的细粒度任务组合成每一个处理器一个粗粒度的任务。下面简单介绍几种有代表性的方法。

递归对剖(Recursive Bisection）递归对剖技术用来将一个域划分成计算成本大致相等的子域,同时试图使通信代价最小,为此常使用分治方法：域首先在一维方向上分割成两个子域;然后分割以递归的方式在两个子域中进行，直至子域数和所要求的任务数一样多。

最直截了当的递归对剖技术是递归坐标对剖（RecursiveCoordinate Bisec-tion)它通常应用于非规整格点。这种技术所作的分割是基于域中物理格点坐标,每一步都沿较长的维进行划分。其优点是简单和低价，其缺点是不能优化通信性能。

递归对剖的一种变体叫做非平衡递归对剖（Unbalanced RecursiveBisec-tion),它使用具有较好长宽比(AspectsRatios)的子格点以降低通信成本,虽增加了计算划分的成本但却减少了通信成本。

还有一种称为递归图对剖(Recursive Graph Bisection)的技术,对复杂的非结构化的格点很有用，它使用连通信息来减少跨子域的格边数，从而可降低通信要求。

局部算法上述描述的技术是很昂贵的，因为它们都要求计算状态的全局知识。相反，局部负载平衡算法，只是使用邻近处理器的负载信息，来周期性地调整自己的负载，或转移到邻居，或从邻居迁人。例如，对于如图7.10所示的网格问题，每个处理器周期地与周围的处理器比较它们的计算负载，如果它们的差异超过了某个阈值就施行计算负载的迁移。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0141-0210/auto/images/faff02f0ea2874ee8a3204e918a895b26393e14e2fb519cc1c85f15d8f677283.jpg)  
图7.10网格问题中的负载平衡

概率方法(Probabilistic Method）这是一种特别简单的方法，它将任务随机地分配给处理器。如果任务数足够多，则每个处理器预计能分配大致等量的计算,其优点是低价和可扩放性;缺点是要求跨处理器的通信和只有当任务数多于处理器数时才可能达到预期的负载分配。概率方法，当任务间很少有通信，和/或通信模式很少呈局部性时，才有可能最有效。

循环映射(Cyclic Mapping）如果知道每个格点计算负载是变化的,且呈现明显的空间局部性,则我们可以使用所谓循环指派法，即采用某种枚举方法，轮流地将各处理器分配给诸计算任务。这种方法可能使负载平衡，但牺牲了局部性且通信可能会增加。

此外,块循环分配(Block Cyclie Distribution)也是一种可能的处理器映射方法,此时,任务按块的形式轮流分配给处理器。

总之，递归对剖法需全局知识,性能好但代价高；局部算法代价小,但当负载变化大时调整很慢;概率方法代价低,可扩放性好，但通信代价可能较大，且只适用于任务数远多于处理器数时；循环映射技术实际是概率映射的一种形式，而概率方法比其它技术易于导致可观的通信。

# 7.5.2任务调度算法

当使用功能分解时，产生了很多弱局部性要求的任务。这些任务通常放在集中的或分散的任务池中,然后使用任务调度算法,将池中的任务分配给特定的处理器。

任务调度算法最关键之处是任务分配策略。策略的选择应在独立运算（以减少通信成本)和计算状态的全局知识(以改善负载平衡)之间折衷,常用的调度模式有经理/雇员方式和非集中方式,在非集中调度方案中,怎样检测整个问题的求解是否已经完成也是一个必须考虑的问题。

经理/雇员模式如图7.11所示，中心(经理)任务负责任务分配,每个雇员重复地从经理那里请求并执行具体任务。此策略的有效性依赖于雇员数和执行任务的成本，使用预取方法(以使计算和通信重叠)和缓存方法(使得雇员无任务时经理和雇员才通信)可以改善效率。这种方案的一种变体是层次经理/雇员模式,它将诸雇员分成不相交的集合,每一个都有一个小经理,雇员们从小经理那里领取任务,并周期地与经理和小经理施行通信。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0141-0210/auto/images/0493fd6e528e4bd1e813d77322334a2143f9385eb36071fe5464e869488bf815.jpg)  
图7.11经理/雇员调度模式

非集中模式它也就是无中心管理者的分布式调度法。在每个处理器中均维持一个任务池,这些任务池实际上就变成了可供请求者异步访问的分布的数据结构。

结束检测任务调度算法需要一种机构检测何时操作结束,否则,空闲的雇员们将永不停止地发出工作请求,这种检测机构在集中式算法中容易实现,因为经理能容易地决定何时雇员们都空闲了;在分布式算法中则较困难，因为没有一个中央机构记录雇员空闲状况。

# 7.5.3映射判据

下面的一组问答题,可检验你所作的映射设计是否合理。.原则上讲，应给予它们肯定的回答：

① 如果采用集中式负载平衡方案,你是否已验证中央管理者不会成为瓶颈?

$\textcircled{2}$ 如果采用动态负载平衡方案,你是否衡量过不同策略的成本？

$\textcircled{3}$ 如果采用概率或循环法，你是否有足够多的任务来保证合理的负载平衡？典型地，任务数应10倍于处理器数。

$\textcircled{4}$ 如果要为一个复杂问题设计一个SPMD程序，你是否考虑过基于动态任务创建和消除的算法：后者可能得到一个更简单的算法，但性能可能有问题。

# 7.6小结和导读

小结本章已经描述了并行算法设计的四个步骤：首先将给定问题划分成一些小的任务，划分方法可以使用域分解法或功能分解法;其次分析诸任务之间的通信需求,通信可以是局部的和全局的，静态的和动态的，结构化的和非结构化的以及同步的和异步的;然后使用组合方法，在尽可能保持灵活性的同时,减少通信和开发成本;最终以最小化总执行时间为目标将诸任务分配给处理器，使用负载平衡和任务调度技术可以改善映射的质量，在每个设计步骤之后均列出了相应的设计检验准则以评价设计的好坏。

经过上述四个步骤设计出的并行算法，在开始编码实现之前尚须考虑以下几件事：对算法进行性能分析以选择好的算法，根据要求证实所作的设计是否满意,考虑算法具体实现时的代价和代码重用的可能性;最终考虑如何将算法装配到一个更大的系统中去。

通过上面的学习之后,我们最好以一个实例来加深课文中所述设计原理的理解以及阐述开发设计一个并行算法的逐步过程,为此我们在本章的习题中给出了一个综合练习，通过它读者一方面可以了解针对给定问题设计一个并行算法的全过程;另一方面也促使读者独立回答一些问题，,以达到复习巩固的目的。

导读论述算法程序设计过程的一篇经典文章是[139]。在实用的、可扩放的并行机上设计并行算法,读者可参阅[69,71]。并行程序的设计,读者参阅[41]。

映射问题的研究在计算机科学中很受重视。有关递归坐标对剖算法，读者可参阅[28];非平衡递归对剖算法由[105]提出，使用连通信息的递归对剖算法，读者可参阅[142];[160]等比较了划分非结构化网孔的不同算法，包括坐标对剖部，图对剖等；[69,131]等描述了循环分解法：[120]等描述了局部算法；有关调度结束检测算法，读者可参阅[59,148]。其它相关的文献包括[29,86,56,89,121,113,152]。[67]中的第2章集中地讨论了并行算法的设计方法学,章末的注释中列举了大量的有关此方面的参考文献，有兴趣的读者可追踪阅读。

# 习 题

7.1算法7.1是一个组合搜索算法,每当调用该算法扩展一个搜索树节点时,就检查该节点是否代表了一个问题的解：如果不是，则算法作递归调用以扩展其子节点。

算法7.1 SISD上组合搜索算法   
输入：给定问题A   
输出：问题A的解   
Procedure : SEARCH( A)   
Begin if(Solution(A)) then $\mathsf { S c o r e } = \mathsf { e v a l } ( \mathbf { A } )$ Report Solution and Score else for each child $\mathsf { A } ( { \boldsymbol { \mathbf { \mathit { i } } } } )$ of A do SEARCH(A(i)) endfor endif   
End

(1)如何构造此问题的并行搜索算法?

7.2分治策略是常用的问题求解技术,其算法可形式描述如下：

算法7.2 SISD上分治(D&C)算法   
输入：问题输人集   
输出：问题的解   
Begin if base case then solve problem else (1)partition problem into subproblem L and R (2)solve L using D&C (3)solve R using D&C (4)combine solutions to problem L and R endif

试用此算法求解 $N = 3 2$ 的全和,并画出相应的求和树。

7.3画出图7.8二叉树的通信图,并分析其计算和通信次数。

7.4画出图7.9蝶式图的通信图,并分析其计算和通信次数。

7.5(1）对于 $1 2 \times 6 = 7 2$ 个网格点，如有 $\pmb { \hat { p } = 1 2 }$ 个处理器，如何用循环指派法分配处理器？

(2）对于 ${ 8 \times 8 } = 6 4$ 个网格点，如有 ${ \pmb \phi } = { \pmb 4 }$ 个处理器，如何用循环指派法分配处理器？

(3)对于(1)和(2)两种情况,如何用块循环指派法分配处理器?

7.6设计并实现使用3点格式的1-D有限差分并行算法,假定每个处理器上分配一个任务，试分析所设计算法的性能。

7.7设计并实现使用5点格式的2-D有限差分的2-D分解并行算法，假定每个处理器上分配一个任务。试分析该算法的性能。

7.8试设计一个1-D和2-D格点的Gauss-Seidel并行算法。

7.9综合练习一大气模型的算法设计。

# (1)背影知识

大气模型(AtmosphereModel)是模拟影响气候的大气过程(风、云、雨等)的计算机程序，它可用来研究龙卷风的演变,预测明天的天气,或者研究大气中 $\mathrm { C O } _ { 2 }$ 浓度对气候的影响。大气模型是求解一组PDE方程,它描述大气基本流体动力学行为。这组方程的连续空间行为可用空间中的有限的离散点的行为近似表征。典型地，这些离散点都位于长方形经纬网格$N _ { x } \times N _ { y } \times N _ { z }$ 上,其中 $\ N _ { x } { \approx } 2 N _ { y } , N _ { y }$ 的区间为 ${ \mathfrak { s o } } \sim { \mathfrak { s o } } 0 , N _ { z }$ 的区间为 $1 5 \sim 3 0$ （如图7.12所示)。在每个格点上用一向量表示,其值代表该格点的压力、温度、风速、湿度等。大气模型执行时间积分，它根据当前状态决定将来的大气状态,积分逐步前进,每计算一固定量就前进一步,假定使用9点格式(Nine-Point Stencil)有限差分方法修改格点在水平维运动之值，用3点格式修改垂直维运动之值(如图7.13所示)。大气模型涉及到在规整的三维网格上执行有限差分计算,它是一大类科学数值计算的代表,大气模型包含了如下的一组基本预测方程,其中$\phi$ 和 $\lambda$ 是纬线和经线， $\pmb { z }$ 是高度， $\pmb { u }$ 和 $_ { v }$ 是速度的水平分量， $\pmb { w }$ 是垂直分量， $\pmb { \mathscr { p } }$ 是压力， $\rho$ 是密度， $T$ 是温度， $f$ 是洛伦兹力， $\pmb { g }$ 是重力， $F$ 和 $\pmb { Q }$ 是外力， $C _ { p }$ 是热容， $^ a$ 是地球半经， $R$ 为常数：

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0141-0210/auto/images/d79936d179c878db011639291802039b5640ddaaf25d263c753a37fa5c6dfc14.jpg)  
图7.12大气状态三维格点表示

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0141-0210/auto/images/affa7b08bb6a2a95f8c07dc45abe6fba07cf7dad00be4af3d33886581386c9a4.jpg)  
图7.13大气模型中使用的有限差分格式

$$
\begin{array} { r l } & { \frac { \mathrm { d } u } { \mathrm { d } t } - ( f + u \frac { \tan \phi } { a } ) _ { v } = - \frac { 1 } { a \cos \phi } \frac { 1 } { \rho } \frac { \partial \phi } { \partial \lambda } + F _ { \lambda } } \\ & { \frac { \mathrm { d } v } { \mathrm { d } t } + ( f + u \frac { \tan \phi } { a } ) _ { u } = \frac { 1 } { \rho a } \frac { \partial \phi } { \partial \phi } + F _ { \phi } } \end{array}
$$

流体静力学方程：g=-1p

质量守恒 $\frac { \partial \phi } { \partial t } = - \frac { 1 } { a \cos \phi } ( \frac { \partial } { \partial \lambda } ( \rho u ) + \frac { \partial } { \partial \phi } ( \rho v \cos \phi ) ) - \frac { \partial } { \partial z } ( \rho w )$   
能量守恒 $C _ { P } \frac { \mathrm { d } T } { \mathrm { d } t } - \frac { 1 } { \rho } \frac { \mathrm { d } \phi } { \mathrm { d } t } = Q$   
大气状态方程： $\scriptstyle { p = \rho R T }$

# (2)设计分析

划分在大气模型中,可用格点代表大气的状态,所以域分解是很自然的。参照图7.2,分解在 $x , y , z$ 方向上均是可能的。如果为了开拓最大并行度,则可将每个格点定义为一个任务，试问总共有多少个任务？

通信在大气模型中有三种不同形式的通信： $\textcircled{1}$ 有限差分格点计算引起的通信：在细粒度分解时,每个格点代表一个任务。参照图7.13,如在水平维使用9点格式,垂直使用3点格式，则格点间的通信量是多少？②全局计算所引起的通信：大气模型中,要周期性地计算大气质量，令 $M _ { i , j , k }$ 表示格点 $( { \ : } _ { i } , { \ : } _ { j } , k )$ 处的大气质量,则总质量为：

$$
T o t a l M a s s = \sum _ { i = 0 } ^ { N _ { x } - 1 N _ { y } - 1 N _ { z } - 1 } \sum _ { j = 0 } ^ { J - 1 } M _ { i , j , k }
$$

试问如何并行计算(7.10)式？③物理计算所引起的通信：由于一个格点视为一个任务，则大气模型物理分量的计算要求相当多的通信,例如在第k层(k≥1)的全晴空(TCS)(Total ClearSky)定义如下：

$$
\mathrm { T C S } _ { k } = \ \prod _ { i = 1 } ^ { k } \ ( 1 - \mathrm { c l d } _ { i } ) \mathrm { T C S } _ { i } = \mathrm { T C S } _ { k - 1 } ( 1 - \mathrm { c l d } _ { k } )
$$

其中,第0层是大气顶层,cld;是第i层的云的比例小数。试问如何并行计算(7.11)式?此时每个格点每个时间步总共需要多少次通信？试用通信判据评价一下所作的通信设计。

组合当使用细粒度的域分解时,任务数似乎是大的，似应进行组合：参照图7.14,少量的组合(每个任务从1个格点到4个格点)能减少9点格式计算所引起的通信需求(每个任务每个时间步从8条信息到4条信息);水平维通信需求相对较小，仅4条信息(8个数据）,而在垂直时，除了有限差分格式的计算所需的通信外(2条信息,2个数据),还有不同物理分量的计算(见(7.11)式),所以组合应在哪个方向上进行？从软件工程的角度,为了减少开销，应允许现行的串行代码尽量能在并行程序中不加修改地被重用,试问组合应在什么方向上进行？为什么？经过上述的组合分析，组合后任务数大约是多少？

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0141-0210/auto/images/bb7eb3fd4b31e0e238b4c2157f7f3f79622cbe56c3cc783601a90bfd5ac93360.jpg)  
图7.14大气模型中的组合方法

映射在不存在负载不平衡的情况下，可以使用图7.15所示的简单映射策略,每个处理器指派给单一任务。此任务负责多列的计算，从而可产生一个 SPMD程序，此分配策略如果每个任务每个时间步内执行等量计算,则是很有效的,但在大气模型中其物理分量计算变化相当大,例如辐射计算不能在晚上，云雾形成必须温度超过一定阈值。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0141-0210/auto/images/c057959e39dd53a7b0b164d8a6599d1fe2ac35f3d1809dbade71d8d1aaea03c0.jpg)  
图7.15大气模型中的均匀映射

此类计算负载的变化能导至效率下降20%或更多，当此值不能接受时，应考虑别的映射方式,例如循环指派法，试解释采用循环映射的大气模型为何能改善负载平衡状态？

最后请你给出一个简短结论：即大气模型应使用几维划分？什么类型的分解？应该怎样组合？如何进行映射？

# 第三篇 并行数值算法

第八章 基本通信操作第九章 稠密矩阵运算第十章 线性方程组的求解第十一章 快速傅里叶变换

这一篇主要研究数值计算问题的并行算法,包括矩阵运算(第九章）、线性方程组的求解(第十章)和快速傅里叶变换(第十一章)。其中，矩阵运算是数值计算中最重要的一类运算，是线性代数和数值分析中最基本的运算操作；稠密和稀疏线性方程组是大型科学工程计算中最常用的数值计算问题;快速离散变换是数字信号处理等应用领域中最主要的数值计算形式。这些数值计算问题的特点是： $\textcircled{1}$ 计算量一般都涉及到一个具体的物理量,其数值可用实数(即浮点数),也可用虚数表示； $\textcircled{2}$ 求解问题的依据是基于数值分析中的数学原理； $\textcircled{3}$ 求解问题的算法可用直接法，但更普遍的是迭代法，且在理论上讲，每次迭代都应改善前一步的计算结果； $\textcircled{4}$ 计算结果，一般均应是满足预定精度要求的近似解。在讨论算法时，对数值计算的稳定性、收敛速度和精度分析等基本问题，乃是直接利用数值分析中的数学原理和结论，而着重讨论计算问题的基本原理,设计串行算法和分析串行算法中的并行性及并行化方法，对于有些典型问题还给出相应的并行算法。

由于任何并行算法，在执行时总会涉及到处理器之间的相互通信问题,所以本篇一开始(第八章)还讨论了在环、二维网孔和超立方等结构上,采用确定选路算法和存储转发与切通开关技术,进行一到一、一到多和多到多等一些基本通信操作。这些并非针对数值计算的问题,对于非数值并行算法也同样存在。

# 第八章 基本通信操作

大多数并行算法均会涉及到处理器间的数据(本章下文称消息)交换。数据交换方式可归结为处理器间的通信操作，而通信操作各式各样,本章只研究下一章矩阵运算中所使用的最频繁的一些基本通信操作，包括研究通信操作与处理器之间的互连拓扑，通信选路策略和消息传递机制关系。本章讨论采用确定的维序(Dimension-Ordering)选择方法,使用存储转发(Store-and-Forward,简记之为SF)和切通(Cut-Through,简记之为CT)开关技术，在环、二维网孔和超立方等连接上进行一到一、一到多、多到多等一些基本通信操作。：

# 8.1 选路方法与开关技术

# 8.1.1选路方法

所谓选路(Routing)系指消息从发源地到达目的地所取的走法，即行进的方法。-般可分为最短(Minimal)法和非最短(Nonminimal)法,有时相应地称为贪心(Greedy)法和随机(Random)法。贪心法总是在源和目的之间试图选择最短的路径,但往往会造成拥挤。随机法虽可能选路长度较长,但不易造成拥挤。选路方法也可分为确定的(Deterministic)和自适应的(Adaptive)：前者在源和目的之间确定一条唯一的路径;后者根据行进中的网络状态信息而自动地确定路径。

一种最常用确定的最短选路法是维序选路(Dimension-Ordered Routing)法，它是根据通信通道(下文也叫作链路、信道等)的维来确定消息如何穿越相继的通道。当此方法用于二维网孔中时就称为X-Y选路法,用于超立方网络中时就称为E-立方(E-Cube)选路法。

X-Y选路法在二维网孔中选路时,首先沿 $X$ 维方向确定路径,然后再沿$Y$ 维方向确定路径。

# 算法8.1 二维网孔上的X-Y选路算法

输入：待选路的信包(Packet)处于源处理器中输出：将各信包送至各自的目的地中

# Begin

（1）沿 $X$ 维将信包向左或向右选路至目的处理器所在的列(2）沿 $Y$ 维将信包向上或向下选路至目的处理器所在的行

End

例8.1 图8.1中示出了4个(源;目的)对的X-Y选路过程,其中节点(2,1)要选路到节点(7,6),节点(0,7)要选路到节点(4,2),节点(5,4)要选路到节点(2,0),节点(6,3)要选路到节点(1,5)。显然它们不会出现死锁或循环等待现象。□

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0141-0210/auto/images/c07c35fe5945a7305b90b3d868034c5e02ea9a288ff5181d3d3b91d5b536b2d4.jpg)  
图8.1 ${ \bf 8 \times 8 }$ 二维网孔中4个(源;目的)对的X-Y选路

E-立方选路法对于 $N = 2 ^ { n }$ 个节点的 $\pmb { n }$ 维立方体,令源节点的二进制编码为 $S = { s _ { n - 1 } } ^ { \dots } { s _ { 1 } } { s _ { 0 } }$ ,目的节点的二进制编码为 $D = d _ { n - 1 } \cdots d _ { 1 } d _ { 0 } ,$ 将 $\pmb { n }$ 维表示成i=1,2,…,n,其中第i维对应于节点地址的第i-1位。设V=Un-1,,10是路径中的任一中间节点，则确定一条从源 $S$ 到目的 $D$ 的E－立方选路算法如下：

# 算法8.2超立方网络上的E-立方选路算法

输入：待选路的信包在源处理器中输出：将源处理器中的信包送至其目的地

# Begin

(1)for $i = 1$ to $\pmb { n }$ do $\big / \ast$ 计算方向位 $\yen 7$ $r _ { i } = { { s _ { i - 1 } } \bigoplus { d _ { i - 1 } } }$ /\*为异-或运算符 $\star$ / end for   
(2) $i = 1 , V = S / \ast \sharp \sharp \sharp \ast /$   
(3）while $i \leqslant n$ do (3.1)if $r _ { i } = 1$ then从当前节点 $V$ 选路到节点为 $V \textcircled { + } 2 ^ { i - 1 }$ endif (3.2) $i = i + 1$

# endwhile

End

例8.2图8.2中示出了4维超立方的E-立方选路过程,其中 $\pmb { n } = 4$ ， $s =$ 0110, $D = 1 1 0 1 , R = r _ { 4 } r _ { 3 } r _ { 2 } r _ { 1 } = 1 0 1 1$ 。由于 $r _ { 1 } = 0 \oplus 1 = 1$ ,所以 $s$ 的下一节点为$s \oplus 2 ^ { 0 } = 0 1 1 1$ ；同样由于 $r _ { 2 } = 1 \oplus 0 = 1$ ，所以 $V = 0 1 1 1$ 的下一节点为 $V \bigoplus 2 ^ { 1 } =$ 0101;由于 $r _ { 3 } = 1 \oplus 1 = 0$ ,所以跳过第 ${ \dot { \pmb { \mathscr { i } } } } = 3$ 维；最后由于 ${ r _ { 4 } } = 0 \bigoplus 1 = 1$ ,所以 $v =$ 0101就选路到节点 $V \oplus 2 ^ { 3 } = 1 1 0 1$ ,它就是目的地。□

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0141-0210/auto/images/27f3b750e7565fef651eb25ad5b040b503be23d18f5f74664768eacd695a139a.jpg)  
图8.24维超立方中的E-立方选路

# 8.1.2开关技术

消息格式通信中乐于使用消息(Message)这一术语，它是节点间通信的逻辑单位，如图8.3所示，通常由一些定长的信包(Packet)组成。信包是带有选路信息的基本通信单位，可以把它分成一些定长的数据片,其中选路信息和顺序号作为(包)头，其余的是数据。消息格式的改进使开关技术由存储转发式演变成更先进的虫蚀(Wormhole)方式。

存储转发(SF)选路在存储转发网络中信包是基本的传输单位。在传输过程中，中间节点必须收齐且存储在缓冲器中后，它才可能传向下一节点（如图8.4(a)所示）。

令 $t _ { \textrm { s } }$ 是启动时间(包括打包、执行选路算法和建立通信介面的时间）， $t _ { \mathrm { h } }$ 是节点延迟时间(即包头穿越网络中两直接相连的处理器所需的时间）， $\pmb { t } _ { \mathbf { w } }$ 是传输每个字的时间(它是带宽的倒数）。

对于长度为 $_ { m }$ 的信包，穿越 $\iota$ 条链路,在存储转发的网络中总通信时间为：

$$
t _ { \mathrm { c o m m } } ( \mathrm { S F } ) = t _ { \mathrm { s } } + ( m t _ { \mathrm { w } } + t _ { \mathrm { h } } ) l
$$

如果 $t _ { \mathrm { h } } = t _ { \mathrm { s } } = 0 , t _ { \mathrm { w } } = 1$ ,则

$$
t _ { \mathrm { c o m m } } ( \mathrm { S F } ) = { \cal O } ( m \cdot l )
$$

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0141-0210/auto/images/c2340711f2f64f4d79265b821990142acb920fea9f22f405d8a48974e4e17fac.jpg)  
图8.3消息、信包和片的格式

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0141-0210/auto/images/397a683933c50b17f88cc213cf48630aa0a716d9d1f7bf4e5cdb7ddd47fe0d8f.jpg)  
图8.4两种开关技术的时间比较(a)SF通信时间；（b)CT通信时间

切通(CT)选路在切通网络中将信包进一步分成更小的片(数据片和包头)进行传输。虫蚀(Wormhole)选路是切通选路的一种形式。在传输过程中，中间节点只备有很小的片缓冲器，一旦收到包头就传至下一节点。同一信包中的所有片一同以流水线方式穿越网络(如图8.4(b)所示)。整个信包犹如一列火车,由火车头(包头)牵引着车厢(数据片)顺序前进。

对于长度为 $_ { \pmb { m } }$ 的信包,穿越 $\iota$ 条链路,在切通的网络中总通信时间为：

$$
t _ { \mathrm { c o m m } } ( \mathrm { C T } ) = t _ { s } + m t _ { \mathrm { w } } + l t _ { \mathrm { h } }
$$

如果 $t _ { \mathrm { s } } = 0 , t _ { \mathrm { h } } = t _ { \mathrm { w } } = 1$ ，则

$$
t _ { \mathrm { c o m m } } ( \mathbf { C T } ) = O ( m + l )
$$

一般情况下, $t _ { \textrm { s } }$ 是不容忽略的,而片的大小是远小于 $_ { m }$ 的,同时 $\pmb { t } _ { \mathbf { w } }$ 通常也比 $t _ { \boldsymbol { \mathrm { h } } }$ 大得多,所以(8.1)式和(8.2)式可近似写为：

$$
t _ { \mathrm { c o m m } } ( \mathrm { S F } ) = t _ { \mathrm { s } } + m t _ { \mathrm { w } } \cdot l
$$

$$
t _ { \mathrm { { c o m m } } } ( \mathrm { C T } ) = t _ { \mathrm { { s } } } + m t _ { \mathrm { { w } } }
$$

(8.1b)和(8.2b)式表明了这样的事实：存储转发网络的延迟与源和目的之间的距离成正比;而切通网络的延迟时间与源和目的之间的距离无关。

# 8.2单一信包一到一传输

单一信包施行点对点一到一传输是最基本的通信操作。当计算通信时间$t _ { \mathrm { c o m m } }$ 时， $l$ 是个重要参数。在具有 $\pmb { \mathscr { P } }$ 个处理器规则互连的网络中,它可定量计算之。

I的计算对于 $\pmb { \hat { p } }$ 个处理器连成环形， $\iota$ 至多为 $\pmb { \phi } / 2 . 1$ ;对于 $\sqrt { \pmb { \mathscr { p } } } \times \sqrt { \pmb { \mathscr { p } } }$ 个处理器连成周边环绕正方网孔(Wraparound Square Mesh),l至多为2L√p/2」；对于p个处理器连成超立方体,l至多为logp。一般的非规则互连的网络中的l并非容易计算。

SF网络传输时间上界单一信包用SF方式选路,在环上的通信时间为ts+twmLp/2」;在周边环绕正方网孔上的通信时间为ts+2twmL√p/2」;在超立方上的通信时间为ts+twmlogp。

CT网络传输时间使用CT方式,将单一信包从源直接发送至l远的目的地的通信时间为ts+twm+thl。对于m充分大的信包使用CT方式传输时,处理器之间传输单一信包的时间,与用SF方式在两直接相连的处理器之间传输单一信包的时间基本一样。

# 8.3一到多播送

所谓一到多播送(One-to-All Broadcast),是指开始时 $\mathrm { P } _ { 0 }$ 中保存有信包 $M$ ，播送结束后所有其它处理器中均得到信包 $m _ { \circ }$ 一到多播送的反操作叫作单点累积(Single-Node Accumulation),两者在以后讨论的数值算法中均经常使用。

# 8.3.1 使用 SF进行一到多播送

环约定环是双向的,且每个处理器一次只能发送一条信包。在8个处理器环上,使用 SF方式进行播送,其过程如图8.5所示,其中虚线箭头上的数字表示发送时间步。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0141-0210/auto/images/62c85a068a88ef762c478263f506188fe31d3d305a50c3f84198d4a37e7d8293.jpg)  
图8.58个处理器的环上以SF方式播送过程

显然,在 $\pmb { \phi }$ 个处理器的环上,用SF方式进行播送的通信时间为：

$$
t _ { \mathrm { o n e - t o - a l l } } ( \mathrm { S F } ) = ( t _ { s } + m t _ { \mathrm { w } } ) \lceil \hat { p } / 2 \rceil
$$

环绕网孔一个 $\hat { \pmb { p } }$ 个处理器的正方网孔可以视为其行和列均由 $\sqrt { \pmb { \phi } }$ 个处理器所组成的环，所以可以使用环上播送方法来讨论网孔上的播送。在16个处理器环绕网孔上,使用 SF方式进行播送,其过程如图8.6所示。同样，虚线箭头上的数字表示发送时间步。

在 $\pmb { \mathscr { P } }$ 个处理器的环绕网孔上用 SF方式进行播送时，先完成一行中的播送，再同时进行各列中的播送,显然其通信时间为：

$$
t _ { \mathrm { o n e - t o - a l l } } ( \mathrm { S F } ) { = } 2 ( t _ { \mathrm { s } } + m t _ { \mathrm { w } } ) \Gamma \sqrt { \hat { p } } / 2 \rceil
$$

不难推知在三维网孔上施行播送的通信时间为：

$$
t _ { \mathrm { o n e - t o - a l l } } ( \mathrm { S F } ) = 3 ( t _ { \mathrm { s } } + m t _ { \mathrm { w } } ) \lceil p ^ { 1 / 3 } / 2 \rceil
$$

超立方一个有2d个处理器的超立方可以视为每维仅有2个处理器的d维网孔，因此网孔上的播送方法可以推广到超立方上。在8个处理器的超立方上,使用SF方式进行播送,其过程如图8.7所示。照例，虚线箭头上的数字表示发送时间步。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0141-0210/auto/images/21bcc4e2850a9d82765845ef36b77a9a81d934b6b7e589d5d9585c5410091b4f.jpg)  
图8.616个处理器的环绕网孔上以 SF方式播送过程

不难计算出 $\pmb { \mathscr { P } }$ 个处理器的超立方上,用SF方式进行播送通信时间为：

$$
t _ { \mathrm { o n e - t o - a l i } } ( \mathrm { S F } ) = ( t _ { \mathrm { s } } + m t _ { \mathrm { w } } ) \log { \phi }
$$

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0141-0210/auto/images/40c388f45050b4f39a0b755293b7a7d8649507d0ff554d881a9d9c44000a8fa2.jpg)  
图8.78个处理器的超立方上以 SF方式播送过程

# 8.3.2使用CT进行一到多播送

环因为使用CT选路时,通信时间与中继节点无关,所以可以将超立方上的播送算法直接映射到环上。为此,对于一个如图8.8所示的8个处理器环，可以参照图8.7：先按高维播送，再按中维播送，最后按低维播送就可完成播送。剩下的问题是如何计算它的通信时间。

当按照图8.8所示的方式播送信包时，源处理器首先发送信包至p/2远的处理器;其次是已收到信包的处理器将它发送至p/4远的处理器。一般在第i步时信包发送的距离为p/2i,其通信时间为ts+mtw+thp/2i。因此总的通信时间为：

$$
t _ { \mathrm { o n e - t o - a l l } } ( \mathrm { C T } ) = \sum _ { i = 1 } ^ { \log p } ~ ( t _ { \mathrm { s } } + m t _ { \mathrm { w } } + t _ { \mathrm { h } } \phi / 2 ^ { i } )
$$


<!-- chunk 0004: pages 211-280 -->
$$
= t _ { \mathrm { s } } \mathrm { l o } 8 \phi + m t _ { \mathrm { w } } \mathrm { l o } 8 \phi + t _ { \mathrm { h } } \left( \frac { } { } \phi - 1 \right)
$$

对于充分大的 $m \mathrm { ~ , ~ } t _ { \mathrm { h } }$ 可忽略不计,所以上式可简化为：

$$
t _ { \mathrm { o n e - t o - a l l } } ( \mathbf { C T } ) = ( t _ { \mathrm { s } } + m t _ { \mathrm { w } } ) \log p
$$

它比(8.3)式大大改进。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0004_pages_0211-0280/auto/images/fdb5069e6cefa599d4882391cc4519a91fe99620178281c8a76ffcdeb19ed50c.jpg)  
图8.88个处理器环上以CT方式播送过程

网孔在如图8.9所示的二维网孔上用CT方式播送时可分为两步：先完成一行中 $\sqrt { \pmb { \phi } }$ 个处理器间的播送；再同时进行各列中 $\sqrt { \pmb { \phi } }$ 个处理器间的播送。参照(8.7)式,可知每步的通信时间为 $\begin{array} { r } { \big ( t _ { \mathrm { s } } + m t _ { \mathrm { w } } \big ) \log \sqrt { \hat { p } } + t _ { \mathrm { h } } \big ( \sqrt { \hat { p } } - 1 \big ) } \end{array}$ ,因此总的通信时间为：

$$
t _ { \mathrm { o n e - t o a l l } } ( \mathrm { C T } ) = ( t _ { \mathrm { s } } + m t _ { \mathrm { w } } ) \log { \phi } + 2 t _ { \mathrm { h } } ( \sqrt { \phi } - 1 )
$$

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0004_pages_0211-0280/auto/images/ef5b343d03eda0e3b430923d4606a47dae45e903443e9e11d741a1559c3dca85.jpg)  
图8.9 $4 \times 4$ 网孔上以CT方式播送过程

超立方已如前述,一个 $2 ^ { d }$ 个处理器可视为每维只有2个处理器的 $\pmb { d }$ 维网孔,所以在超立方上用CT方式播送其通信时间为：

$$
t _ { \mathrm { o n e - t o - a l l } } ( \mathrm { C T } ) = ( t _ { \mathrm { s } } + m t _ { \mathrm { w } } ) \log p
$$

# 8.4多到多播送

多到多播送(All-to-All Broadcast)也称为多节点播送(Multinode Broadcast），此时所有 $\pmb { \mathscr { P } }$ 个处理器同时启动播送，只是各处理器播送各自的信包。多到多播送的反操作叫作多点累积(Multinode Accumulation),两者在矩阵运算、归约操作和求前缀和中常使用。

# 8.4.1 使用SF进行多到多播送

环在p个处理器的环中进行多到多播送,实际上就是一系列以流水线方式工作的p个处理器将各自的信包依次同向传递。传递完毕后,每个处理器都接收到了来自其它 $\left( \pmb { \hat { p } } - \pmb { 1 } \right)$ 个处理器中的信包,其总的通信时间为：

$$
t _ { \mathrm { a i l - t o - a l l } } ( \mathrm { S F } ) = ( t _ { s } + m t _ { \mathrm { w } } ) ( \mathbf { \nabla } _ { P } - \mathbf { 1 } )
$$

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0004_pages_0211-0280/auto/images/00dbd22224168cd99a246252766a2935b33e71faea613ff5d675b1ced034e611.jpg)  
图8.108个处理器的环上用SF方式多到多播送过程

图8.10示出了8个处理器环上用SF方式施行多到多播送的过程。其中，虚线箭头上圆括弧外的数字是时间步，圆括弧内的数字是该时间步所发送的信包所属的处理器号；各节点旁的圆括弧中的数字是该节点所积累的信包所属的处理器号。

环绕网孔如一到多播送一样，二维网孔上多到多播送可以处理成行环和列环的播送。为此,先按行进行多到多播送；再按列进行多到多播送。在 $\sqrt { \pmb { \phi } } \times$ $\sqrt { \phi }$ 的环绕网孔上,各行多到多的播送时间为 $\left( { t _ { \mathrm { s } } + m t _ { \mathrm { w } } } \right) \left( { \sqrt { \ p } - 1 } \right)$ ;经过行播送后各处理器中的信包大小变为 $m ~ { \sqrt { \beta } }$ ，所以再按列施行多到多播送时其时间为$\big ( t _ { \mathrm { s } } + m \ \sqrt { / } t _ { \mathrm { w } } \big ) \big ( \sqrt { / } - 1 \big )$ 。因此总的通信时间为：

$$
t _ { \mathrm { a l l - t o - a l l } } \mathrm { ( S F ) } = 2 t _ { \mathrm { s } } \mathrm { ( } \sqrt { \mathcal { p } } - 1 \mathrm { ) } + m t _ { \mathrm { w } } \mathrm { ( } \mathbf { \nabla } \mathbf { \mathcal { p } } - 1 \mathrm { ) }
$$

图8.11示出了 $3 \times 3$ 环绕网孔(为了清楚起见,环绕线未画出)上用 SF方式施行多到多播送的过程。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0004_pages_0211-0280/auto/images/dc1cf9092005149a903aaaa623545ec67bf7fa7a505a28c5d42086809037a333.jpg)  
图8.11 $3 \times 3$ 环绕网孔上用SF方式进行多到多播送(a)起始数据分布；(b)行播送后的数据分布

超立方在超立方上施行多到多播送,很自然地是按超立方的维成对处理器交换数据(双向通道),各处理器中的信包大小每次加倍,第i步交换时信包大小为2i-1m,因此成对处理器交换信包的时间为ts+2i-1mtw,于是总的通信时间为：

$$
t _ { \mathrm { a l l - t o - a l l } } ( \mathrm { S F } ) = \sum _ { i = 1 } ^ { \log p } ~ ( t _ { \mathrm { i } } + 2 ^ { i - 1 } m t _ { \mathrm { w } } )
$$

$$
= t _ { s } \mathrm { l o g } p + m t _ { \mathrm { w } } ( \pmb { \phi } - 1 )
$$

图8.12示出了8个处理器的超立方上用SF方式施行多到多的播送过程。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0004_pages_0211-0280/auto/images/14f6a859c52057cee4a825dd635c35989417444af2cd8ff4ff4e8c55b942c576.jpg)  
图8.128个处理器的超立方上用SF方式进行多到多播送(a)起始状态;(b)第2步之前的状态；(c)第3步之前的状态；(d)最终状态

# 8.4.2使用CT进行多到多播送

如前所述，使用CT方式进行一到多播送时，为了在环和网孔上获得较好的结果,只要将超立方上的算法映射到它们之上即可。但对于多到多播送而言,这样作未必好，因为它会造成通道拥挤。例如,要是将图8.12(c)超立方上成对处理器间的交换操作直接映射到图8.13所示的环上时，就会发现有4条信包同时穿过环的一条通道,从而造成拥挤。

然而,在双向线性阵列(无环绕网孔)上,使用CT方式进行多到多播送的通信时间与在环(带环绕网孔)上使用 SF方式进行多到多播送的通信时间是一样的。

值得提出的是,对于任何并行结构,其多到多播送之通信时间的下界为$m t _ { \mathrm { w } } ( \pmb { \mathscr { p } } - 1 )$ ，这可从(8.10)、(8.11)和(8.12)式中看出。事实上，不管使用何种结构和选路方式,每个处理器至少要接收到 $m t _ { \mathrm { w } } ( \pmb { \phi } - 1 )$ 个数据字。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0004_pages_0211-0280/auto/images/f5f087c9fc387f51c300af3b25ac8403de99d84713274936d79bd71442d7b38d.jpg)  
图8.13图8.12(c)通信步映射到环上时所造成的拥挤

# 8.5小结和导读

小结在正文中已经讨论了一到多播送和多到多播送以及它们的反操作单点累积和多点累积。在章末习题8.6'和8.7也将介绍一到多个人通信(One-to-All Personalized Communication)和多到多个人通信(Al-t-All Personalized Com-munication)。为了更清楚地理解它们的含意,图8.14分别图示了它们的概念。

表8.1列出了本章所讨论的不同互连结构采用CT开关技术时的几种基本通信操作的通信时间,其中循环 $\mathbf { q } .$ 移位(Circular q-Shift）（见习题8.8)通信时间表达式中的 $r ( q )$ 是 $\pmb q$ 能被 $2 ^ { j }$ 整除的最大整数j。

表8.1通信时间汇总一览表(使用CT方式）  

<table><tr><td rowspan=1 colspan=1>通信操作</td><td rowspan=1 colspan=1>p-环</td><td rowspan=1 colspan=1>p×p-二维环绕网孔</td><td rowspan=1 colspan=1>p-超立方</td></tr><tr><td rowspan=1 colspan=1>一到多播送</td><td rowspan=1 colspan=1>(ts+ mtw)logp+th(p-1)</td><td rowspan=1 colspan=1>(ts+ mtw)logp+2th(p-1)</td><td rowspan=1 colspan=1>(ts+ mtw)logp</td></tr><tr><td rowspan=1 colspan=1>多到多播送</td><td rowspan=1 colspan=1>(t,+mtw)(p-1)</td><td rowspan=1 colspan=1>2t(p-1)+ mtw(p-1)</td><td rowspan=1 colspan=1>tslogp + mtw( p -1)</td></tr><tr><td rowspan=1 colspan=1>一到多个人通信</td><td rowspan=1 colspan=1>(ts+mtw)(p-1)</td><td rowspan=1 colspan=1>2ts(p-1)+ mtw(p-1)</td><td rowspan=1 colspan=1>tslogp +mtw(p-1)</td></tr></table>

（续表）

<table><tr><td rowspan=1 colspan=1>通信操作</td><td rowspan=1 colspan=1>p-环</td><td rowspan=1 colspan=1>p×√p-二维环绕网孔</td><td rowspan=1 colspan=1>p-超立方</td></tr><tr><td rowspan=1 colspan=1>多到多个人通信</td><td rowspan=1 colspan=1>(t,+ mtwp/2)(p-1)</td><td rowspan=1 colspan=1>(2tg+ mtwp)(p-1)</td><td rowspan=1 colspan=1>(t+mtw)(p-1)+p1o8p</td></tr><tr><td rowspan=1 colspan=1>循环q-移位</td><td rowspan=1 colspan=1>(t,+ mtw)Lp/2]</td><td rowspan=1 colspan=1>(t+mtw）（2L2+1)</td><td rowspan=1 colspan=1>t,+ mtw+th(logp -r(q))</td></tr></table>

# 一到多播送

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0004_pages_0211-0280/auto/images/de9a461ce45a34aa4eb85c882881c7f8c3c1c4caa916d64daa670e9af85b06aa.jpg)  
图8.14一到多和多到多个人通信(a)一到多播送和单点累积;(b)多到多播送和多点累积；(c)一到多个人通信和单点收集;(d)多到多个人通信

上表中的表达式对使用SF开关技术时绝大部分都相同,不同的是： $\textcircled{1}$ 对于一到多播送，在环上的通信时间为 $( t _ { \mathrm { s } } + m t _ { \mathrm { w } } ) \lceil \mathtt { \Delta } _ { P } / 2 \rceil$ ，在二维网孔上的通信时间为 $2 ( t _ { \mathrm { s } } + m t _ { \mathrm { w } } ) \lceil \sqrt { \hat { p } } / 2 \rceil$ ； $\textcircled{2}$ 对于多到多个人通信,在超立方上的通信时间为 $( { t _ { \mathrm { s } } } ^ { + }$ $m t _ { \mathbf { w } } \pmb { \mathscr { p } } \wedge 2 ) \log \pmb { \mathscr { p } } \circ$

本章所讨论的通信操作方法均可在SIMD机器上执行。然而由于在MIMD机器上施行同步比较复杂,所以本章所给出的通信时间表达式运用在MIMD机器上时可能相差很大。

导读关于多处理机的互连网络,读者可进一步参考互连网络综述[64]和互连网络专著[199]。有关通信选路策略和消息传递机制,读者可阅读[100]书中的第7.4节。[114]书中的第三章还详尽地讨论了诸如一到多个人通信、多到多个人通信和循环移位等其它一些基本通信操作。读者还可以从上述基本参考文献中追踪阅读一些更丰富和更新近的文献。

# 习 题

8.1对于一个 $\pmb { 8 } = 2 ^ { d }$ 个处理器(其编号从0到 $2 ^ { d } - 1 )$ 的环,如何将其嵌人 $\pmb { d }$ 维超立方中？[提示：可以使用8位Gray码对环上的处理器进行编号。一个8位Gray码为000,001，011,010,110,111,101,100.]

8.2对于一个 $2 \times 4$ 的网孔(处理器按行主方式依次编号为0,1,2,3,4,5,6,7),如何将其嵌人3维超立方中？[提示：将 $2 \times 4$ 的网孔使用Gray码按行主对其编号。]

8.3如图8.15所示,信包中的片0,1,2,3要分别去向目的地 $\mathbf { A } , \mathbf { B } , \mathbf { C } , \mathrm { D } _ { \circ }$ 此时片0占据信道CB,片1占据信道DC,片2占据信道AD,片3占信道 ${ \tt B A } _ { \tt o }$ 试问：

$\textcircled{1}$ 这将会产生什么现象？$\textcircled{2}$ 如果采用X-Y选路策略，可避免上述现象吗？为什么？

8.4假定在二叉树中,叶节点为处理器节点,内节点为开关节点(参照图8.16)。试证明在 $\pmb { \hat { p } }$ 个叶节点的二叉树中，进行 $\pmb { m }$ 个字的一到多播送的通信时间为：

$$
( t _ { \mathrm { s } } + m t _ { \mathrm { w } } + t _ { \mathrm { h } } ( \log { p } + 1 ) ) \log { p }
$$

[提示：信包穿越 $\mathbf { \nabla } _ { l } - \mathbf { 1 }$ 个开关节点所需的时间为 ${ \pmb t _ { s } } + m { \pmb t _ { \mathrm { w } } } + { \pmb t _ { \mathrm { h } } } { \pmb l } _ { \circ } ]$

8.5给定 $\pmb { \hat { p } }$ 个数 $n _ { 0 } , n _ { 1 } , \cdots , n _ { \hat { \rho } ^ { - 1 } }$ ，所谓前缀和(Prefix Sum)就是计算 $S _ { k } = \sum _ { i = 0 } ^ { k } n _ { i }$ ,其中 $0 \leqslant$ $\pmb { k } \leqslant _ { } p - 1$ 。算法8.3给出了超立方上求前缀和的方法。试按此算法，计算8个处理器的超立方上前缀和。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0004_pages_0211-0280/auto/images/e772a88246f32c8b4692913c467ca410cfc62d73ea6a65377f32bb0f5bfb48a5.jpg)  
图8.15虫蚀选路网络中所出现的现象

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0004_pages_0211-0280/auto/images/9dc0dbcbcaf284c816db377da243278281438ea86b15474efefff6187e0ebe38.jpg)  
图8.168个处理器的树上一到多播送过程

# 算法8.3 $\pmb { d }$ 维超立方上前缀和算法

输入： $\pmb { \mathscr { P } }$ 个数开始存在 $\pmb { \hat { p } }$ 个处理器中输出：第 $k$ 个处理器存有前缀和 $S _ { k } = \sum _ { i = 0 } ^ { k } n _ { i } , 0 { \leqslant } k { \leqslant } p - 1$ Begin

(1）result $=$ my - number (2) $\mathbf { m s g } =$ result

for $i = 0$ to $d - 1$ do (3.1） ${ \mathrm { P a r t n e r } } = \mathbf { m } \mathbf { y } _ { - } \mathbf { i d } \mathbf { \widehat { \mathrm { { + } } } } { 2 ^ { i } }$ (3.2） Send msg to Partner

(3.3）Receive number from Partner   
(3.4） ${ \mathrm { m s g } } { = } { \mathrm { m s g } } + { \mathrm { n u m b e r } }$   
(3.5）if(Partner<my- id)then resul $=$ result $^ +$ number endif

end for

End

8.6一到多个人通信又称之为单点散射(Single-Node Scatter),它与一到多播送不同之处是，此时源处理器有 $\pmb { \hat { p } }$ 个信包,每一个去向一个目的地(见图 $8 . 1 4 ( \mathfrak { c } ) )$ 。图8.17示出了8个处理器的超立方上单点散射的过程。试证明：使用 SF和CT方式在超立方上施行一到多个人通信的通信时间为：

$$
t _ { \mathrm { o n e - t o - a l l - p e r s } } = t _ { s } \mathrm { l o g } \phi + m t _ { \mathrm { w } } ( \phi - 1 )
$$

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0004_pages_0211-0280/auto/images/bee5785de3781847a5a7a28f82184f1e811e3155668549d3483cb65fe28df112.jpg)  
图8.178个处理器的超立方上单点散射过程(a)起始分布;(b)第2步之前的分布; $\left( \mathbf { c } \right)$ 第3步之前的分布；(d)最终分布

8.7多到多个人通信又称之为全交换(Total Exchange),每个处理器发送各自彼此不同的大小为m的信包给其余处理器(见图8.14(d))。图8.18示出了6个处理器的环上全交换的过程,其中，{x,y|表示{源处理器,目的处理器,（{x1,y1}，x2,y2},，xn,yn}）表示传输过程中的信包流,每个处理器只接收属于它的信包，下传其余的信包。试证明：利用 SF方式,在环上施行全交换的通信时间为：

$$
t _ { \mathrm { { u a l - e x c h a n g e } } } = { \big ( } t _ { \mathrm { s } } + { \frac { 1 } { 2 } } m t _ { \mathrm { w } } { p } { \big ) } { \big ( } { p - 1 } { \big ) }
$$

[提示：第 $\pmb { i }$ 步传送的信包大小为 $m ( \pmb { p } - i ) _ { \circ } ]$

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0004_pages_0211-0280/auto/images/6b29e5c9d201afea7af27ff1d12ddce0b5f77b90942bcec89de4e31f2e24d4e0.jpg)  
图8.186个处理器的环上全交换过程

8.8在 $\pmb { \mathscr { p } }$ 个处理器,所谓循环 $\mathbf { q } \mathrm { . }$ 移位系指处理器 $_ i$ 发送包给处理器 $( i + q ) { \bmod { p } }$ 。图8.19示出了按行主编号的 $\sqrt { \pmb { \mathscr { p } } \times \pmb { \mathscr { p } } } = 4 \times 4$ 环绕网孔上施行 5-移位的过程：首先按行同时循环移位(qmod√p=1)次;然后作Lq/√p」=1次列补偿移位(如图8.19(b)所示);最后再作一次列移位。试证明：利用SF方式在正方形环绕二维网孔上施行循环q-移位的通信时间为：

$$
t _ { \mathrm { c i r c u l a r - s h i f t } } = ( t _ { s } + m t _ { \mathrm { w } } ) ( 2 \lfloor { \sqrt { \dot { p } } } / 2 \rfloor + 1 )
$$

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0004_pages_0211-0280/auto/images/598f6a49c061c4c94d6696f02d2ffe31b34945cf09e205593fb7f7b007b6917e.jpg)  
图8.19 $4 \times 4$ 环绕网孔上5-移位过程

(a)起始分布和第1通信步;(b)补偿列移位;(c)第3通信步中列移位；(d)最终分布

# 第九章 稠密矩阵运算

矩阵运算是数值计算中最重要的一类运算，特别是在线性代数和数值分析中,它是一种最基本的运算。本章讨论稠密矩阵的运算,包括矩阵转置、矩阵和向量相乘以及矩阵相乘等。在讨论并行矩阵算法时，将结合具体例子以图示的方法着重算法原理的叙述;在分析算法时，除了分析计算时间外,还要利用上一章所学的知识来分析通信时间;在实现算法时，强调矩阵到处理器的映射；同时为了教学的方便，限于讨论方阵，但所介绍的算法也同样适用于矩形阵。

# 9.1矩阵的划分

在科学和工程计算中，矩阵的阶都很高(元素很多),为了并行实现,很自然地要将其进行划分，然后指派给不同的处理器。下面将扼要讨论矩阵的两种常见的划分方法，即行列划分(又称为带状划分)和棋盘划分(又称为块状划分)。

# 9.1.1 带状划分

所谓带状划分（Striped Partitioning)就是将矩阵整行或整列地分成若干个组,每组指派给一个处理器。也可将若干行或若干列指派给一个处理器,而且这些行和列可以是连续的，也可以是等距相间的，前者称为块带状的（ $\mathbf { B l o c k } \mathbf { - }$ Striped),后者称为循环带状的(Cyclic-Striped)。

块带状划分如图9.1(a)所示,它是一种列块带状划分。在此情况下,对于一个 $\mathbf { \Omega } _ { n } \times \mathbf { \Omega } _ { n }$ 的矩阵和 $\pmb { \mathscr { p } }$ 个处理器（编号为 $\mathbf { P _ { 0 } } , \mathbf { P _ { 1 } } , \cdots , \mathbf { P _ { \pmb { \hat { \rho } } - 1 } } )$ 而言,每个处理器将均匀连续地分配有 $\pmb { n } / \pmb { \mathscr { p } }$ 列,其中 $\mathbf { P } _ { i }$ 包含有列 $\left( n / p \right) i , \left( n / p \right) i + 1 , \cdots , \left( n / \right)$ $\pmb { \mathscr { p } } ) ( i + 1 ) - 1 , 0 { \leqslant } i { \leqslant } \pmb { \mathscr { p } } - \pmb { 1 } _ { \pmb { \mathscr { c } } }$

循环带状划分如图9.1(b)所示,它是一种行循环带状划分。在此情况下，对于一个 $\mathbf { \Omega } _ { n } \times \mathbf { \Omega } _ { n }$ 的矩阵和 $\pmb { \hat { p } }$ 个处理器(编号为 $\mathbf { P } _ { 0 } , \mathbf { P } _ { 1 } , \cdots , \mathbf { P } _ { { \pmb { \phi } } - 1 } )$ 而言,每个处理器将均匀相间地分配有n/p行,其中P;包含有行i,i+p,i+2p,,i+（n-1)p,$0 { \leqslant } i { \leqslant } p - 1 ,$

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0004_pages_0211-0280/auto/images/88f778434d422b9b2b570fb7ba6dfc44355ca2f342b1a7934ccc97b8dbeac81c.jpg)  
图9.14个处理器上 $1 6 \times 1 6$ 矩阵带状划分(a)列块带状划分； (b)行循环带状划分

# 9.1.2棋盘划分

所谓棋盘划分(Checker Board Partitioning)就是将方阵划分成若干个子方阵，每个子方阵指派给一个处理器，此时任一处理器均不包含整行或整列。和带状划分类似,棋盘划分也可分为如图9.2(a)所示的块棋盘划分(Block-CheckerBoard

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0004_pages_0211-0280/auto/images/fd2848291ab301fbb8514e29fad56c00696a950bd04dc7422de6d0e4bf2d1a33.jpg)  
图9.216个处理器上 $\mathbf { 8 \times 8 }$ 矩阵棋盘划分(a)块棋盘划分； (b)循环棋盘划分

Partitioning)和如图9.2(b)所示的循环棋盘划分(Cyclic-Checker Board Partition-ing）。

矩阵划分成棋盘状可和处理器连成二维网孔相对应。对于一个 $n \times n$ 的方阵和 ${ \overline { { \pmb { p } } } } \times { \sqrt { \pmb { p } } }$ 的二维处理器阵列,每个处理器均匀地分配有 $( n / \sqrt { \hat { p } } ) \times ( n / \sqrt { \hat { p } } ) =$ $n ^ { 2 } / \phi$ 个矩阵元素。

值得指出的是,和带状划分相比,棋盘划分可开发更高的并行度。例如,对于一个 $\mathbf { \Omega } _ { n } \times \mathbf { \Omega } _ { n }$ 的方阵,棋盘划分最多可使用 $n ^ { 2 } .$ 个处理器进行并行计算,但使用带状划分可用的处理器不能多于 $\pmb { n }$ 个。

# 9.2矩阵转置

对于一个 ${ \pmb n } \times { \pmb n }$ 的方阵 $\pmb { A }$ ,将其元素 $a _ { i j }$ (沿主对角线)与 $a _ { j i }$ 互换,就构成了转置矩阵(Transposing Matrix) $\pmb { A } ^ { \textrm { T } }$ 。如果假定成对元素交换取单位时间，则显然串行矩阵转置算法9.1的运行时间为 $\left( n ^ { 2 } - n \right) / 2 = O ( n ^ { 2 } )$ 。

# 算法9.1单处理机上矩阵转置算法

输入： $\mathbf { A } _ { n } \times \mathbf { \mu } _ { n }$   
输出： $\smash { A _ { n \times n } ^ { \textrm { T } } }$   
Begin for $i = 2$ to $_ n$ do for $j = 1$ to $i - 1$ do $a _ { i j }  a _ { j i }$ endfor endfor   
End

# 9.2.1 棋盘划分的矩阵转置

以下仅讨论网孔和超立方上块棋盘划分的矩阵转置算法，它们对循环棋盘划分也同样适用。

网孔上的矩阵转置如图9.3所示,要是处理器数目p=n²,则网孔上的矩阵转置算法是非常简单的：对角线下的元素,先向上移至对角线,再向右移至目的地；对角线上的元素，先向下移至对角线，再向左移至目的地。

对于p<n²的情况,整个n×n的矩阵先分成p个大小为(n/√p)×（n/√p)的子块,然后算法分两步进行：第一步,将子块视为单个元素进行如图9.4(a)所示的子块转置;第二步,在各处理器内施行如图9.4(b)所示的局部转置。

（0，1） 0,2） 0,3） （0，0） （1.0） （2,0） （3,0）P0 P1 P ？ → P0 P1 P2 P  
（1.3 0，1） （1,1） （2,1） 3,1）P P6 P P4 P P6 P7, 1.....  
（2,0） (2. （2,3） 0,2) $\left( 1 , 2 \right)$ （2,2） （3,2）P8 P10 P P& P9 P10 ${ \bf P } _ { 1 1 }$ i  
（3,0） （3，1 （3,2) 0.3） （1.3） （2,3） （3,3）P12 4 .Pj3 P14 ↑ P12 P13 P14 P1s（a） （b）

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0004_pages_0211-0280/auto/images/39b2cd59f3d897e2c303061035b6d8e0a972ed00573dae057c64299f4ae0bb50.jpg)  
图9.316个处理器上棋盘划分的 $4 \times 4$ 矩阵的转置(a)通信过程； (b)最终结果  
图9.416个处理器上棋盘划分的 ${ \pmb 8 } \times { \pmb 8 }$ 矩阵的转置(a)子块转置； (b)子块内局部转置

整个算法的运行时间可分析如下：第一步的子块转置最长的路径约为$2 \sqrt { \pmb { \mathscr { p } } }$ ，移动单个子块的时间为 $t _ { \mathrm { s } } + t _ { \mathrm { w } } n ^ { 2 } / \phi$ ，所以各子块达到其目的地的时间为 $2 ( t _ { s } + t _ { \mathrm { w } } n ^ { 2 } / p ) \sqrt { \ p }$ ;第二步,假定成对元素局部交换取单位时间,则大小为$( n / \sqrt { \hbar } ) \times ( n / \sqrt { \hbar } )$ 子块约花了 $\scriptstyle { n ^ { 2 } } / ( 2 p )$ 的时间进行局部转置，所以算法总运行时间为：

$$
T _ { \mathrm { p } } = { \frac { n ^ { 2 } } { 2 \phi } } + 2 t _ { \mathrm { s } } \ { \sqrt { \hat { p } } } + 2 t _ { \mathrm { w } } \ { \frac { n ^ { 2 } } { \sqrt { \hat { p } } } }
$$

递归转置算法（Recursive Transposition Algorithm）如图9.5所示，一个$\mathbf { \Omega } _ { n } \times \mathbf { \Omega } _ { n }$ 的方阵先分成4个子方阵,对其施行转置，即右上与左下两个子方阵对调;然后每个子方阵再分成4个更小的子方阵施行转置;依此类推直到整个矩阵转置完毕。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0004_pages_0211-0280/auto/images/1871df9ada8f6d37f6e57c7d2290e9e26662bc2878e883f7a59891769385550a.jpg)  
图9.5 ${ \pmb 8 } \times { \pmb 8 }$ 矩阵的递归转置法

(a)矩阵分成4块进行转置； (b)每块再分成4个子块进行转置；(c)每个子块中4个元素进行转置； (d)最终结果

超立方上的矩阵转置上面所介绍的递归转置算法可以很自然地映射到超立方上。如图9.6（a）所示，先将 $_ n \times n$ 的方阵分成4个 $\frac { n } { 2 } \times \frac { n } { 2 }$ 的子方阵，相应地将p个处理器的超立方考虑成4个p/4个处理器的子超立方;然后将右上子块与左下子块对调(如图9.6(a)所示， $\mathrm { P } _ { 8 }$ 中的子块与 ${ \bf P } _ { 2 }$ 中子块对调， $\mathrm { P } _ { 9 }$ 中子块与${ \bf P } _ { 3 }$ 中子块对调等等)。接着如图9.6(b)所示,再将各个 $\frac { n } { 2 } \times \frac { n } { 2 }$ 的子块分成4个更小的子块,并对它们施行转置。在最后递归步中，子超立方中只有一个处理器,显然总共进行了 $\log _ { 4 } { p } = ( \log { p } ) / 2$ 递归步,这时各子块的大小为 $( n / \sqrt { \ p } ) \times$ $( n / \sqrt { \ p } )$ ,它们要在每个处理器中施行局部转置,花费了约 $n ^ { 2 } / ( 2 \phi )$ 的时间。因为每个待通信的子块大小为 $\dot { n } ^ { 2 } / \phi$ ,所以使用存储转发选路时需 $2 ( t _ { \mathrm { s } } + t _ { \mathrm { w } } n ^ { 2 } / \phi )$ 时间,因此递归 $( \log p ) / 2$ 步的总通信时间为 $( t _ { s } + t _ { \mathrm { w } } \ n ^ { 2 } / p ) \mathrm { l o g } p$ ,这样算法总的运行时间为：

$$
T _ { \mathrm { p } } { = } \frac { n ^ { 2 } } { 2 \hat { p } } + ( t _ { \mathrm { s } } + t _ { \mathrm { w } } \frac { n ^ { 2 } } { \hat { p } } ) \log \hat { p }
$$

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0004_pages_0211-0280/auto/images/ec066e051791df00dd39e65ed51ab318362fc65dbf8aa33cdae3e65ae35202a6.jpg)  
图9.616个处理器的超立方上的矩阵递归转置(a)矩阵分成4块进行转置； (b)每块中4个子块进行转置

# 9.2.2带状划分的矩阵转置

如图9.7所示,假定对于一个 $n \times n$ 的矩阵,使用 $\pmb { n }$ 个处理器按行划分。

开始时,处理器 $\mathrm { P } _ { i }$ 中存有矩阵元素 $[ i , 0 ] , [ i , 1 ] , \cdots , [ i , n - 1 ]$ ,则在转置后，元素 $[ i , 0 ]$ 将属于 ${ \tt P } _ { 0 }$ ，元素 $[ i , 1 ]$ 将属于 $\mathbf { P _ { 1 } }$ ,如此等等。注意在转置过程中，每个处理器将发送不同的值给其它处理器,这实际上就是第八章中所讲的多到多个人通信。

一般而论， $\textstyle { p { \leqslant } n }$ 时每个处理器分配有 $n / \phi$ 行(共 $n ^ { 2 } / \phi$ 个元素),此时转置中所涉及到的多到多个人通信的子块大小为 $( n / p ) \times ( n / p )$ 。通信完毕后，每个处理器尚须对这些子块施行局部转置。假定成对元素交换取单位时间,则每个子块转置时间为 $n ^ { 2 } / ( 2 p ^ { 2 } )$ 。因为每个处理器有 $\pmb { \mathscr { P } }$ 个这样的子块,所以转置它们花费了 $n ^ { 2 } / ( 2 p )$ 时间。当在超立方上使用切通选路法对大小为 $n ^ { 2 } / \phi ^ { 2 }$ 的信包进行多到多个人通信时，其时间约为 $t _ { \mathrm { s } } ( \boldsymbol { \ p } - 1 ) + t _ { \mathrm { w } } \ n ^ { 2 } / \hbar + \left( 1 / 2 \right) t _ { \mathrm { h } } \ \boldsymbol { p } \log \boldsymbol { \phi }$ （参见第八章的表8.1)。所以这时算法总的运行时间为：

$$
T _ { \mathrm { p } } = { \frac { n ^ { 2 } } { 2 \phi } } + t _ { \mathrm { s } } ( \not p - 1 ) + t _ { \mathrm { w } } { \frac { n ^ { 2 } } { \phi } } + { \frac { 1 } { 2 } } t _ { \mathrm { h } } \not p \log \phi
$$

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0004_pages_0211-0280/auto/images/147f35c50f4f32badec6b43b862d4e2d3d8b621221f7cf1d5effe3b2e9737ea6.jpg)  
图9.74个处理器上 $4 \times 4$ 矩阵的转置

# 9.3 矩阵-向量乘法

对于一个n×n的方阵A乘以n×1的向量X就可得n×1的向量Y。如果假定一个乘-加运算取单位时间，则显然串行矩阵-向量乘法(Matrix-VectorMultiplication）算法9.2的运行时间为 $O ( n ^ { 2 } )$

# 算法9.2单处理机上矩阵-向量乘算法

输入： $A _ { n } \times _ { n } , X _ { n \times 1 }$   
输出: $\pmb { Y } _ { n \times 1 }$   
Begin for $i = 0$ to $n \sim 1$ do $y _ { i } = 0$ for $j = 0$ to $\pmb { n } - \pmb { 1 }$ do $y _ { i } = y _ { i } + a _ { i j } x _ { j }$ endfor endfor   
End

# 9.3.1带状划分的矩阵-向量乘法

以下仅讨论行带状划分矩阵-向量乘法,列带状矩阵-向量乘法是类似的。

$p = n$ 的情况,如图9.8(a)所示，开始时处理器 $\mathrm { \bf P } _ { i }$ 存放 $. \boldsymbol { r } _ { j }$ 和 $a _ { i , \ i } , a _ { i , \ i } , \cdots ,$ $a _ { i , n }$ 并负责计算 $y _ { i }$ 。由于矩阵-向量相乘要求每一行与整个向量相乘，所以如图9.8(b)所示每个处理器要将其向量元素向其余的处理器进行多到多播送。播送完毕后就可以如图9.8(c)那样进行 $y _ { i } = \sum _ { j = 0 } ^ { n - 1 } u _ { i j } x _ { j }$ aij的计算了。按此，通信和计算时间均为 $O ( n )$ ,它是成本最佳的。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0004_pages_0211-0280/auto/images/123fd9a3da2e72a9b5bf878d092bf5dc47f076f4f3437e9bcad7a896f23f43d9.jpg)  
图9.8 $\beta = \pi$ 时按行划分的矩阵-向量乘法：

(a)起始分布；（b）向量多到多播送；$\left( \mathfrak { c } \right)$ 施行相乘；（d)结果向量 $\pmb { \gamma }$

$/ / < / \iota$ 的情况是类似的，只是开始时每个处理器存放有矩阵的 $n / /$ 行(共$n ^ { 2 } / 1 )$ 个元素)和向量的 $n / \mu$ 个元素。

超立方上矩阵乘向量参照第八章的表8.1可知、"/p个向量元索多到多播送时间为 $t _ { \mathrm { s } } \mathrm { l o g } \phi + \left( n / p \right) t _ { \mathrm { w } } \left( \mathbf { \Gamma } _ { \mathbf { \hat { P } } } - 1 \right)$ ,当 $\pmb { \phi }$ 充分大时它近似为 $t _ { \mathrm { s } } \mathrm { l o g } \ p + n t _ { \mathrm { w } } ,$ 。考虑到每个处理器要花 $n ^ { 2 } / \phi$ 的时间进行乘-加运算，所以超立方上并行矩阵-向量乘之总时间为：

$$
T _ { \mathrm { p } } = \frac { n ^ { 2 } } { \phi } + t _ { \mathrm { s } } \mathrm { l o g } \phi + n t _ { \mathrm { w } }
$$

当 ${ \boldsymbol { \mathbf { \mathit { p } } } } = { \boldsymbol { \mathbf { \mathit { n } } } }$ 时， $T _ { \mathfrak { p } } = O ( n )$ ,它是成本最佳的。

网孔上矩阵乘向量参照第八章的表8.1可知多到多播送 $n / \phi$ 个元素的时间为 $2 \big ( \sqrt { \ p } - 1 \big ) t _ { \mathrm { s } } + \frac { n } { \ p } t _ { \mathrm { w } } \big ( \ p - 1 \big )$ ,它可近似为 $2 t _ { \mathrm { s } } ( \sqrt { \hat { p } } - 1 ) + n t _ { \mathrm { w } }$ 。所以二维环绕 $\sqrt { \pmb { \mathscr { p } } } \times \sqrt { \pmb { \mathscr { p } } }$ 网孔上并行矩阵-向量乘之总时间为：

$$
T _ { \mathrm { p } } = \frac { n ^ { 2 } } { \phi } + 2 t _ { \mathrm { s } } ( \sqrt { \hat { p } } - 1 ) + n t _ { \mathrm { w } }
$$

# 9.3.2棋盘划分的矩阵-向量乘法

以下仅讨论块棋盘划分矩阵-向量乘法，循环棋盘划分时的矩阵-向量乘法是类似的。

$\pmb { p } = \pmb { n } ^ { 2 }$ 的情况此时每个处理器存放有矩阵的一个元素，而向量 $\pmb { x } _ { i }$ 通常是存放在 $P _ { i i }$ 中的。如果 $\pmb { x _ { i } }$ 是存放在处理器阵列的最后一列中，则进行矩阵-向量乘时，如图9.9(a)所示，先要将向量元素与矩阵主对角线对准;然后如图9.9(b)所示，在列方向上施行向量元素一到多播送；播送完毕后，接着如图9.9(c)和(d)所示,则施行乘-加和单点累积,最后按行收集结果向量 $\yen 0$

在网孔上，图9.9(a)所示的一到一通信、图9.9(b)所示的一到多播送和图9.9(c)所示的单点累积，时间均为 $O ( n )$ ;在超立方上则为 $O ( \log n )$ 。因为每个处理器执行乘-加操作的时间为常数，所以在 $\textbf { \em n } \times \textbf { \em n }$ 的网孔上和 $\pmb { n } ^ { 2 }$ 个处理器的超立方上的并行矩阵-向量乘之总时间分别为 $O ( n )$ 和 $O ( \log n )$ ,它们不是成本最佳的。

$\pmb { p } < \pmb { n } ^ { 2 }$ 的情况假定 $\pmb { \mathscr { p } }$ 个处理器排成 $\sqrt { \pmb { \mathscr { p } } } \times \sqrt { \pmb { \mathscr { p } } }$ 的二维网孔,每个处理器存放有 $( n / \sqrt { \hat { p } } ) \times ( n / \sqrt { \hat { p } } )$ 的子块, $\pmb { \mathscr { n } } / \sqrt { \pmb { \mathscr { p } } }$ 个向量元素存放在处理器阵列的最后一列中,则进行矩阵-向量乘时，首先最右列的每个处理器要发送 $n / { \sqrt { \phi } }$ 个向量元素至主对角线上的处理器;然后按列进行一到多播送 $n / \sqrt { \mathbf { \Lambda } } \mathbf { \Lambda }$ 个元素；接着每个处理器施行n²/p次乘法并积累了n/√p个部分和，它们均须按行累加以得到结果向量。

当在无环绕的网孔上用CT选路法执行矩阵-向量乘时：向量与主对角线对准的时间为 $t _ { \mathrm { s } } + \frac { n } { \sqrt { \hat { p } } } t _ { \mathrm { w } } + t _ { \mathrm { h } } \sqrt { \hat { p } }$ ;按列施行一到多播送时间为 $\big ( \mathrm { \Delta } t _ { s } + \frac { n } { \sqrt { \phi } } \mathrm { \Delta } t _ { \mathrm { w } } \big ) \log { \sqrt { \phi } }$

$+ \ t _ { \mathrm { h } } ( \sqrt { \beta } - 1 )$ ；按行单点累积的时间为 $( \mathbf { \widetilde { \Gamma } } _ { \mathrm { s } } + \frac { n } { \sqrt { \hat { \mathcal { P } } } } \mathbf { \widetilde { \Gamma } } _ { \mathrm { w } } ) \log \sqrt { \hat { \mathcal { P } } } + t _ { \mathrm { h } } ( \sqrt { \hat { \mathcal { P } } } - 1 )$ ;假定乘-加取单位时间,则计算时间为 $n ^ { 2 } / \phi$ 。所以在网孔上并行算法总运行时间约为：

$$
T _ { \mathrm { p } } { \approx } \frac { n ^ { 2 } } { \phi } + t _ { \mathrm { s } } \mathrm { l o g } \phi + t _ { \mathrm { w } } \frac { n } { \sqrt { \phi } } \log \phi + 3 t _ { \mathrm { h } } \sqrt { \phi }
$$

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0004_pages_0211-0280/auto/images/564092c81b1868edde3506a1ccedbb1b1d57552eee351ef3e07a5bd61de602c1.jpg)  
图9.9 $\scriptstyle { p = n ^ { 2 } }$ 时棋盘划分的矩阵-向量乘法(a)起始分布和一到一通信； (b)一到多播送；(c)施行乘-加与单点累积；(d)结果向量 $\pmb { y }$

类似地,当在二维网孔上用SF选路法执行矩阵-向量乘时,并行算法的总运行时间约为：

$$
T _ { \mathrm { p } } { \approx } \frac { n ^ { 2 } } { \dot { p } } + 2 t _ { \mathrm { s } } { \sqrt { \dot { p } } } + 3 n t _ { \mathrm { w } }
$$

带状与棋盘划分时矩阵-向量乘的比较比较(9.5)式与(9.6)式可知,在网孔上用同样多的处理器，棋盘划分的矩阵-向量乘法比带状划分时要快；如果 ${ \pmb { \mathscr { p } } } > { \pmb { \mathscr { n } } }$ ,则无法使用带状划分，而棋盘划分不受此限制；即使 $\pmb { \mathscr { p } } \leqslant \pmb { \mathscr { n } }$ ,棋盘划分也更优;上述结论也适合于超立方(见习题9.3)。同时由章末习题9.5和9.4可知，棋盘划分的矩阵-向量乘的可扩放性也比带状划分时的好。

# 9.4矩阵乘法

一个 $\mathbf { \Omega } _ { n } \times \mathbf { \Omega } _ { n }$ 的方阵 $\pmb { A }$ 乘以 $\mathbf { \Omega } _ { n } \times \mathbf { \Omega } _ { n }$ 的方阵 $\pmb { B }$ 就得一个 $\mathbf { \Omega } _ { n } \times \mathbf { \Omega } _ { n }$ 的方阵 $\pmb { c }$

$$
c _ { i j } = \sum _ { k = 0 } ^ { n - 1 } a _ { i k } b _ { k j } , 0 { \leqslant } i , j { \leqslant } n - 1 _ { _ { - } }
$$

矩阵相乘的关键是相乘的两个元素的下标要满足一定的要求(即对准)。为此常采用旋转矩阵元素的办法(如下面将要介绍的Cannon乘法)使元素下标对准,或采用适当复制矩阵元素的办法(如下面将要介绍的DNS算法)使元素下标对准,或采用流水线的办法(如习题9.10所示的心动阵列上的算法)使元素的下标对准。

如果假定一个乘-加运算取单位时间，则显然串行矩阵乘法算法9.3的运行时间为 $O ( n ^ { 3 } )$

# 算法9.3单处理机上矩阵相乘算法

输入： $A _ { n } \times \ l _ { n } \lor \ l _ { n } \times \ l _ { n }$   
输出： $C _ { n \times n }$   
Begin for ${ \bf { \sigma } } _ { i } = \mathbf { 0 }$ to $\pmb { n } - 1$ do for ${ \bf { \nabla } } j = { \bf { 0 } }$ to $\pmb { n } - 1$ do $c _ { i j } = 0$ for $k = 0$ to $\pmb { n } - 1$ do $c _ { i j } = c _ { i j } + a _ { i k } \cdot b _ { k j }$ endfor endfor endfor   
End

目前所知的串行矩阵乘法的时间复杂度均为O(n"）,其中2<x≤3。例如Strassen乘法的时间阶为 $O \big ( n ^ { 2 . 8 0 7 4 } \big )$ 。

# 9.4.1 简单并行分块乘法

分块矩阵乘法(Block Matrix Multiplication）矩阵运算中分块的概念是非常有用的，可以将对矩阵元素的代数运算推广到对矩阵的块(子矩阵)进行同样的代数运算。例如,一个 $\mathbf { \Omega } _ { n } \times \mathbf { \Omega } _ { n }$ 的矩阵 $\pmb { A }$ 可以视为一个 $q \times q$ 的方块阵 $A _ { i , j } ( 0 \leqslant$ $i , j { \leqslant } q - 1 )$ ,每个方块阵大小为 $( n / q ) \times ( n / q )$ 。这样算法9.3就可改写成算法9.4,相应地,将矩阵元素的乘-加运算代换为子矩阵的乘-加运算。算法9.4共执行了 $q ^ { 3 }$ 次矩阵乘法，每个矩阵乘法需 $( n / q ) ^ { 3 }$ 次乘-加运算，所以总的乘-加次数仍为 $\pmb { n } ^ { 3 }$ 。

使用 $\pmb { \mathscr { p } }$ 个处理器执行分块乘时，可取 $q = \sqrt { \mathfrak { p } }$ ,这样每个处理器计算一个$\mathbf { C } _ { i , j }$ 块。

算法9.4单处理机上分块矩阵相乘算法输入： $A _ { n } \times \smash { _ { n } , B _ { n \times n } }$ ,子块大小为 $( n / q ) \times ( n / q )$ 输出： $\pmb { C _ { n } } \times \pmb { n }$

Begin for ${ \pmb i } = { \bf 0 }$ to $q - 1$ do for ${ j = 0 }$ to $q - 1$ do $\mathbf { C } _ { i , j } = 0$ for $k = 0$ to $q - 1$ do $\mathbf { } C _ { i , j } = \mathbf { } C _ { i , j } + A _ { i , k } \cdot B _ { k , j } $ endfor endfor endfor   
End

并行分块乘法简单的并行分块乘法的过程是： $\textcircled{1}$ 分块：将 $\mathbf { A } _ { n } \times \mathbf { \partial } _ { n }$ 与 $\pmb { { \cal B } } _ { n } \times \mathbf { \nabla } _ { n }$ 分成 $\pmb { \mathscr { p } }$ 块 $\mathbf { A } _ { i , j }$ 和 $B _ { i , j } ( 0 { \leqslant } i , j { \leqslant } \sqrt { \ p } - 1 )$ ,每块大小为 $( n / \sqrt { \hbar } ) \times ( n / \sqrt { \hbar } )$ ,并将它们分配给√p×p个处理器(Po,o,Po,1,,Pp-1,√P-1),开始时P,,存放有块Ai,j与块Bi,,，,然后计算块Ci,;②通信：为了计算块Ci,j,则需要所有块Ai,与Bk,j(0≤k≤√p-1),为此在每行的处理器之间要进行A矩阵块的多到多播送，以得到Ai,k,而在每列的处理器之间要进行B矩阵块的多到多播送,以得到Bk,j;③乘-加计算:一旦Pi,;收到了Ai,o,Ai,1,…,Ai,p-1与Bo,;,B1,j,,B[-1,j之后,就同时进行乘-加运算。

当并行分块乘法执行在 $\pmb { \mathscr { P } }$ 个处理器的超立方上时，参照第八章表8.1可知，通信时间为 $2 \big ( t \llcorner \log \sqrt { \ p } + t _ { \ w } \frac { n ^ { 2 } } { \ p } \big ( \sqrt { \ p } - 1 \big ) \big )$ ;计算时间为 $q \times ( \frac { n } { q } ) ^ { 3 } = \sqrt { p } \times$ $( \frac { n } { \sqrt { \phi } } ) ^ { 3 } = n ^ { 3 } / \phi$ 。所以算法的并行运行时间为：

$$
T _ { \mathrm { p } } = \frac { n ^ { 3 } } { \hbar } + t _ { \mathrm { s } } \mathrm { l o g } \hbar + 2 t _ { \mathrm { w } } \frac { n ^ { 2 } } { \sqrt { \hbar } }
$$

当并行分块乘法执行在 $\sqrt { \pmb { p } } \times \sqrt { \pmb { p } }$ 的二维环绕网孔上时,参照第八章表8.1可知其通信时间为 $2 t _ { \mathrm { s } } \sqrt { \hat { p } } + 2 t _ { \mathrm { w } } \frac { n ^ { 2 } } { \sqrt { \hat { p } } }$ ；计算时间为 $n ^ { 3 } / \phi$ ，所以算法的并行运行时间为：

$$
T _ { \mathrm { p } } = { \frac { n ^ { 3 } } { \phi } } + 2 t _ { \mathrm { s } } { \sqrt { \hat { p } } } + 2 t _ { \mathrm { w } } { \frac { n ^ { 2 } } { \sqrt { \hat { p } } } }
$$

简单并行分块乘法的主要缺点是存储要求过大：通信结束时每个处理器拥有 $2 \sqrt { \ p }$ 个块,每块大小为 $n ^ { 2 } / \phi$ ,所以每个处理器要求 $O ( n ^ { 2 } / { \sqrt { p } } )$ 存储器， $\pmb { \phi }$ 个处理器共要求 $O ( n ^ { 2 } \sqrt { \pmb { \mathscr { p } } } )$ ,它是串行算法存储要求的 $\sqrt { \pmb { \mathscr { p } } }$ 倍。

# 9.4.2 Cannon 乘法

算法原理Cannon算法是一种存储有效的算法。为了使两矩阵的下标满足相乘的要求，它和上一节的并行分块乘法不同，不是阵列的各行和各列施行多到多播送，而是有目的地在各行和各列施行循环移位，从而使处理器的总存储要求可以降下来。照例,将矩阵 $\pmb { A }$ 和 $\pmb { B }$ 分成 $\pmb { \hat { p } }$ 个方块 $\mathbf { A } _ { i } , _ { j }$ 和 $B _ { i , j } ( 0 { \leqslant } i , j { \leqslant } \sqrt { \ p } -$ 1),每块大小为 $( n / \sqrt { \hat { p } } ) \times ( n / \sqrt { \hat { p } } )$ ,并将它们分配给 $\sqrt { \pmb { \mathscr { p } } } \times \sqrt { \pmb { \mathscr { p } } }$ 个处理器 $( \mathtt { P _ { 0 , 0 } }$ ，$\mathrm { P } _ { 0 , 1 } , \cdots , \mathrm { P } _ { \sqrt { \hat { p } } ^ { - 1 } , \sqrt { \hat { p } } ^ { - } 1 } )$ 。开始时处理器 $\mathbf { P } _ { i , j }$ 存放有块 $\mathbf { A } _ { i }$ ,和块 $\mathbf { \delta } _ { B _ { i , j } }$ ,并负责计算块 $\mathbf { C } _ { i , j }$ ,然后算法开始执行：

$\textcircled{1}$ 将块 $A _ { i , j } ( 0 { \leqslant } i , j < \sqrt { \ p } )$ 向左循环移动 $_ i$ 步；将块 $B _ { i , j } ( 0 { \leqslant } i , j < \sqrt { \ p } )$ 向上循环移动 $j$ 步；  
$\textcircled { 2 } \ \mathbb { P } _ { i , j }$ 执行乘-加运算；然后,将块 $A _ { i , j } ( 0 { \leqslant } i , j < \sqrt { \ p } )$ 向左循环移动1步；将块 $B _ { i , j } ( 0 { \leqslant } i , j < \sqrt { \dot { p } } )$ 向上循环移动1步；  
③重复第②步,在Pi,;中共执行p次乘-加运算和p次块Ai,;和Bi,的循环单步移位。

算法举例图9.10示例了在16个处理器上，用Cannon算法执行A4×4×$\mathbf { \delta } \mathbf { B } _ { 4 \times 4 }$ 的过程。其中(a)和(b)对应于上述算法的第 $\textcircled{1}$ 步；(c)、(d)、(e)和(f)对应于上述算法的第 $\textcircled{2}$ 和第 $\textcircled{3}$ 步。注意在算法第 $\textcircled{1}$ 步时， $\pmb { A }$ 矩阵的第0行不移位，第1行循环左移1位，第2行循环左移2位,第3行循环左移3位；类似地， $\pmb { B }$ 矩阵的第0列不移位,第1列循环上移1位,第2列循环上移2位,第3列循环上移3位。

算法描述假定矩阵 $\pmb { A }$ 和 $\pmb { B }$ 分成 $\pmb { \mathscr { P } }$ 块 $\mathbf { A } _ { i , j }$ 与 $B _ { i , j } ( 0 { \leqslant } i , j { \leqslant } \sqrt { \dot { p } } - 1 )$ ,处理器排成 $\sqrt { \pmb { \mathscr { p } } } \times \sqrt { \pmb { \mathscr { p } } }$ 的方阵，符号“ $\Leftarrow$ ”表示移位,则Cannon算法可形式描述如下：

# 算法9.5Cannon分块乘法算法

输入： $A _ { n } \times \ d _ { n } , B _ { n } \times \ d _ { n }$ 输出：Cn×n

Begin

(1)for ${ \pmb k } = { \bf 0 }$ to $\sqrt { \pmb { \mathscr { p } } } - 1$ do for all $\mathrm { P } _ { i , j }$ par-do (i)if $i > k$ then $A _ { i , j } {  } A _ { i , ( j + 1 ) \bmod { \sqrt { \hat { \rho } } } } \mathbf { e }$ ndif (ii)if $j > k$ then $B _ { i , j } {  } B _ { ( i + 1 ) \mathrm { m o d } \sqrt { \hat { p } } , j }$ endif endfor endfor (2)for all $\mathrm { P } _ { i , j } \mathrm { \bf ~ p a r { - } d o } C _ { i , j } = 0$ endfor (3)for ${ \pmb k } = { \bf 0 }$ to $\sqrt { \phi } - 1$ do for all $\mathbf { P } _ { i , j }$ par-do $\begin{array} { r l } & { \mathrm { ( i ) } C _ { i , j } = C _ { i , j } + A _ { i , j } \circ B _ { i , j } } \\ & { \mathrm { ( i i ) } A _ { i , j } { \Leftarrow } A _ { i , ( j + 1 ) \mathrm { m o d } \sqrt { \hslash } } } \\ & { \mathrm { ( i i i ) } B _ { i , j } { \Leftarrow } B _ { ( i + 1 ) \mathrm { m o d } \sqrt { \hslash } , j } } \end{array}$ endfor endfor End

算法分析当算法执行在 $\pmb { \mathscr { p } }$ 个处理器的超立方上时,若使用CT选路法,算法第(1)步的循环移位时间(参照第八章表8.1)为2（ts+tw $2 \big ( t _ { \mathrm { s } } + t _ { \mathrm { w } } \frac { n ^ { 2 } } { \phi } + t _ { \mathrm { h } } \log \sqrt { \phi } \big )$ ,算法第(3)步的单步移位时间为2（ts+tw $2 ( t _ { \mathrm { s } } + t _ { \mathrm { w } } \frac { n ^ { 2 } } { \phi } ) \sqrt { \phi }$ ，当 $\pmb { \mathscr { P } }$ 充分大时后者为主项。算法第(3)步共执行 $\sqrt { \phi }$ 次 $( n / \sqrt { \hat { p } } ) \times ( n / \sqrt { \hat { p } } )$ 子块乘法，其时间为 $\sqrt { \pmb { \mathscr { p } } } \times ( \pmb { n } \sqrt { \pmb { \mathscr { p } } } ) ^ { 3 } =$ $n ^ { 3 } / \phi$ 。所以在超立方上Cannon乘法的并行运行时间为：

$$
T _ { \mathrm { p } } = { \frac { n ^ { 3 } } { \hbar } } + 2 { \sqrt { \hbar } } t _ { \mathrm { s } } + 2 t _ { \mathrm { w } } { \frac { n ^ { 2 } } { \sqrt { \hbar } } }
$$

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0004_pages_0211-0280/auto/images/204600d07040cb0aaeb9fbf9e1777cdb6cdc602ca4814122f693d1891b2bc383.jpg)  
图9.1016处理器上Cannon乘法过程${ \bf \Pi } ( { \bf a } ) { \bf A }$ 阵起始对准； $( \boldsymbol { \mathbf { b } } ) \pmb { \mathbf { \{ \delta \mu } } $ 阵起始对准；(c)起始对准后的 $\pmb { A }$ 和 $\pmb { \cal B }$ ：(d)第一次移位后的子阵位置；(e)第二次移位后的子阵位置； (f)第三次移位后的子阵位置

当算法执行在 $\sqrt { \phi } \times \sqrt { \phi }$ 的二维网孔上时,算法第(1)步的循环移位时$2 (  { t _ { \mathrm { s } } } +  { t _ { \mathrm { w } } } \frac {  { n } ^ { 2 } } {  { p } } ) \sqrt {  { p } }$ 2)p,算法第(3)步的单步移位时间为2（ts+tw $2 ( t _ { \mathrm { s } } + t _ { \mathrm { w } } \frac { n ^ { 2 } } { \hat { P } } ) \sqrt { \hat { p } }$ 。算

法第(3)步的运算时间为 $n ^ { 3 } / \phi$ 。所以在二维网孔上Cannon乘法的并行运行时间为：

$$
T _ { \mathrm { p } } = { \frac { n ^ { 3 } } { \hbar } } + 4 { \sqrt { \hbar } } t _ { \mathrm { s } } + 4 t _ { \mathrm { w } } { \frac { n ^ { 2 } } { \sqrt { \hbar } } }
$$

# 9.4.3 Fox 乘法

算法原理 $\mathbf { F o x }$ 算法是另一种存储有效的算法，它和并行分块乘法及Can-non乘法均不同,执行Fox乘法时，行处理器施行一到多播送，而列处理器施行循环单步上移，从而使处理器的存储要求可以降下来。照例,将矩阵 $\pmb { A }$ 和 $\pmb { B }$ 分成 $\pmb { \hat { p } }$ 个方块 $\mathbf { A } _ { i }$ ,和 $\pmb { \mathscr { B } } _ { i }$ ,j $( 0 { \leqslant } i , j { \leqslant } \sqrt { \pmb { \phi } } - 1 )$ ,每块大小为 $( n / \sqrt { \hat { p } } ) \times ( n / \sqrt { \hat { p } } )$ ,并将它们分配给 $\sqrt { \pmb { \mathscr { p } } } \times \sqrt { \pmb { \mathscr { p } } }$ 个处理器 $( \mathrm { P } _ { \boldsymbol { 0 } , 0 , } \mathrm { P } _ { \boldsymbol { 0 } , 1 } , \cdots , \mathrm { P } _ { \sqrt { p } - 1 , \ \sqrt { p } - 1 } )$ 。开始时处理器 $\mathrm { P } _ { i , j }$ 存放有块 $\pmb { A } _ { i }$ ,;和块 $\mathbf { \delta } _ { B _ { i , j } }$ ,并负责计算块 $\mathbf { C } _ { i , j \circ }$ 假定首先选定对角块 $\mathbf { A } _ { i , i }$ 向同行的$\sqrt { \phi } - 1$ 个处理器进行一到多播送，则 $\mathtt { F o x }$ 算法执行以下各步 $\sqrt { \phi }$ 次迭代即可完成：

$\textcircled{1}$ 所选中的对角块 $\mathbf { A } _ { i }$ ,向所在行的 $\sqrt { \beta } - 1$ 个处理器进行一到多播送；  
$\textcircled{2}$ 各处理器将所收到的 $\pmb { A }$ 阵的块与 $\pmb { B }$ 阵原有的块进行乘-加运算；  
$\textcircled{3} \textbf { \textB { } }$ 阵的块向上循环1步；  
$\textcircled{4}$ 如果 $\mathbf { A } _ { i , j }$ 是本次播送的块,则下一次应选块 $A _ { i } , ( { j + 1 } ) _ { \mathrm { m o d } } \sqrt { { \small { \phi } } }$ 向同行的 $\sqrt { \pmb { \mathscr { p } } } -$ 1个处理器播送，然后转第 $\textcircled{2}$ 步。

算法举例图9.11示例了在16个处理器上，用 $\mathtt { F o x }$ 算法执行 $\mathbf { A _ { 4 } } \times 4 \mathbf { \Omega } \times \mathbf { \Omega }$ $\pmb { { \cal B } } _ { 4 \times 4 }$ 时的块 $\pmb { A }$ 的播送与块 $\pmb { B }$ 的单步循环上移的过程。

算法分析当算法执行在 $\pmb { \mathscr { P } }$ 个处理器的超立方上时,若使用CT选路法,块A的总的一到多播送时间(参照第八章表8.1)为 $\frac { 1 } { 2 } ( t _ { \mathrm { s } } \sqrt { \hbar } + t _ { \mathrm { w } } \frac { n ^ { 2 } } { \sqrt { \hbar } } ) \log { \hbar }$ ，而块$\pmb { \cal B }$ 的总的循环单步上移的时间比起它来不是主要的;照例 $\mathbf { P } _ { i , j }$ 执行运算的时间为 $n ^ { 3 } / \phi$ 。所以在超立方上Fox乘法的并行运行时间为：

$$
T _ { \mathrm { p } } = \frac { n ^ { 3 } } { \hbar } + \frac 1 2 t _ { \mathrm { s } } \sqrt { \hbar } \log { \phi } + \frac 1 2 t _ { \mathrm { w } } \frac { n ^ { 2 } } { \sqrt { \hbar } } \log { \phi }
$$

# 9.4.4 DNS 乘法

算法原理如前所述,使用棋盘划分最多可用 ${ \pmb n } ^ { 2 }$ 个处理器，算法的加速可达 $O ( n ^ { 2 } )$ 。下面介绍一种使用更多的处理器可得到更快的算法，即 DNS算法，从而加速比也更高。

DNS 是三位学者Dekel、Nassimi、Sahni 名字的首字母,他们的算法是运行在超立方连接的SIMD机器上的。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0004_pages_0211-0280/auto/images/f41962f06b27e14c99f9b3c74064cf9d268a7549276552042281381aac26a69f.jpg)  
图9.1116个处理器上 $\mathbf { F o x }$ 乘法通信过程(a)A0,0等一到多播送， $\pmb { B _ { i } }$ ,j循环上移； $( \mathbf { b } ) \mathbf { A } 0 , 1$ 等一到多播送， $\mathbf { \delta } _ { B _ { i , j } }$ 循环上移；$( \mathsf { c } ) \mathbf { { A 0 } } , 2$ 等一到多播送， $\mathbf { \delta } _ { B _ { i , j } }$ 循环上移； $( \mathsf { d } ) \mathbf { A } \mathsf { 0 } , 3$ 等一到多播送

在 $\pmb { A } _ { n } \times _ { n } \times \pmb { B } _ { n } \times _ { n }$ 的运算中, $a _ { i s } \times b _ { s j }$ 的操作共有 $\pmb { n } ^ { 3 }$ 个。如果对矩阵 $\pmb { A }$ 和 $\pmb { B }$ 的元素进行适当的复制,则有可能利用 $\pmb { n } ^ { 3 }$ 个处理器同时执行 $n ^ { 3 }$ 个乘法运算,然后再作 $\log n$ 次求和运算即可得到最终的乘积元素 $c _ { i j }$ 。为此将处理器数目$\scriptstyle { p = n ^ { 3 } }$ 表示成 $\pmb { n } \times \pmb { n } \times \pmb { n }$ 的三维数组,其中 $\pmb { n } = 2 ^ { q }$ 。这样超立方中的处理器 $\mathbf { P } _ { r }$ 将处于位置 $( i , j , k )$ ,其中 $r = i n ^ { 2 } + j n + k$ ，且 $0 { \leqslant } i , j , k { \leqslant } n - 1$ 。令 $r$ 的二进制表示为 $r _ { 3 q - 1 } , \cdots , r _ { 2 q } r _ { 2 q - 1 } , \cdots , r _ { q } r _ { q - 1 } , \cdots , r _ { 0 }$ ，其中 $r _ { b }$ 表示从 $r _ { 0 }$ 数起的 $r$ 的第b位。显然下标i,j,k分别对应着r3q-1,,r2q,r2q-1,…,rq,rq-1,,r0o

假定每个处理器 $\mathrm { \bf P } _ { r }$ 有三个寄存器 $A _ { r } \setminus B _ { r } \setminus C _ { r }$ 。开始时处于位置 $( \mathbf { 0 } , j , k )$ 的处理器 $\mathbf { P } _ { s }$ 其 $\pmb { A } _ { s }$ 和 $\pmb { { \cal B } } _ { s }$ 中的内容为 $a _ { j k }$ 和 $b _ { j k }$ ,所有其它处理器的寄存器内容均置为0,算法结束时， $c _ { j k } = \sum _ { i = 0 } ^ { n - 1 } a _ { j i } \times b _ { j k } \circ$ aj×bjk。算法可分为三步：

$\textcircled{1}$ 数据复制： $\mathbf { A } _ { n } \times \mathbf { \nabla } _ { n }$ 与 $\pmb { { \cal B } } _ { n } \times \mathbf { \nabla } _ { n }$ 的元素加载到 $\mathbf { P } _ { 0 , j , k }$ 中的A和B寄存器中；通过A、B同时在 $\textbf { \em i }$ 维复制， $\pmb { A }$ 在 $\pmb { k }$ 维复制和 $\mathbf { B }$ 在 $j$ 维复制后，矩阵 $\pmb { A }$ 和 $\pmb { B }$ 元素就被分配到 $n ^ { 3 }$ 个处理器中了；

$\textcircled{2}$ 施行相乘：各处理器将A寄存器之内容与B寄存器之内容两两相乘；

$\textcircled{3}$ 求和运算：执行 $\sum _ { i = 0 } ^ { n - 1 } C _ { i , j , k \circ }$ (a)初始加载； $( \ b )  { \mathbf { A } } \setminus \pmb { B }$ 沿 $\pmb { i }$ 维复制； $( { \mathfrak { c } } ) \mathbf { { A } }$ 沿 $k$ 维复制； $( d ) B$ 沿 $\pmb { j }$ 维复制；(e)施行点积；(f)相加得最终结果

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0004_pages_0211-0280/auto/images/ac0a1e004bea125d8270bce1fe67151813965dc86c9219baf72d77103d39e112.jpg)  
图9.12 DNS乘法的执行过程

算法举例假定 $\pmb { A } = \left( \begin{array} { r r } { 1 } & { 2 } \\ { 3 } & { 4 } \end{array} \right) , \pmb { B } = \left( \begin{array} { r r } { - 5 } & { - 6 } \\ { 7 } & { 8 } \end{array} \right)$ ,图9.12示例了DNS乘法的过程：图9.12(a)是初始加载;图9.12(b)为A和B寄存器同时按 $_ i$ 维进行复制，即 $r _ { 2 } = 0$ 的那些处理器中 $A , B$ 寄存器之内容复制到 $r _ { 2 } = 1$ 的那些处理器的相应寄存器中；图 $9 . 1 2 ( \mathbf { c } )$ 为 $\pmb { A }$ 寄存器按 $k$ 维进行复制，即凡是 $\mathbf { \nabla } r _ { 0 } = r _ { 2 }$ 的那些处理器中 $\pmb { A }$ 寄存器之内容复制到 $r ^ { ( 0 ) }$ 的那些处理器的 $\pmb { A }$ 寄存器中,其中 $r ^ { ( 0 ) }$ 表示 $_ r$ 的第0位取反；图9.12(d)为 $B$ 寄存器按 $j$ 维进行复制，即凡是 $r _ { 1 } = r _ { 2 }$ 的那些处理器中 $B$ 寄存器之内容复制到 $r ^ { ( 1 ) }$ 的那些处理器的 $B$ 寄存器中,其中r(1)表示r的第1位取反;图9.12(e)为A和B寄存器中的元素之乘积;图9.12

（f)为最终之结果。

算法描述令 $r ^ { ( m ) }$ 表示 $r$ 的第 $\mathbf { \nabla } m$ 位取反； $\mid { \pmb { \mathscr { P } } } , r _ { m } = d \mid$ 表示整数 $r ( 0 { \leqslant } r { \leqslant }$ ${ \pmb { \rho } } - { \bf 1 } )$ 的集合， $r$ 的二进制表示为 $r _ { 3 q - 1 } \cdots r _ { m + 1 } \mathrm { d } r _ { m - 1 } \cdots r _ { 0 0 }$

算法9.6 DNS乘法算法输入： $A _ { n \times n } , B _ { n \times n } , n = 2 ^ { q }$ 输出： $C _ { n \times n }$

Begin

(1）for $m = 3 q \textrm { -- } 1$ to $2 q$ do $\big / \star$ 按 $i$ 维复制 $\mathbf { A } , \mathbf { B } \ast \mathbf { \ell } /$ for all $_ r$ in $\{ \pmb { \mathscr { p } } , r _ { m } = 0 \} \mathbf { p a r } - \mathbf { d o }$ $\begin{array} { l } { { ( 1 . 1 ) A _ { r } { } ^ { ( m ) } {  } A _ { r } } } \\ { { ( 1 . 2 ) B _ { r } { } ^ { ( m ) } {  } B _ { r } } } \end{array}$ endfor endfor

(2）for $m = q - 1$ to $0 ~ \mathrm { d } \mathbf { 0 } ~ / \star$ 按 $k$ 维复制 $\mathbf { A } \ast { \mathbf { \zeta } } ^ { \prime }$ for all $r$ in $\left\{ \ p , r _ { m } = r _ { 2 q + m } \right\}$ par-do ${ \pmb { A } } _ { r } { \bf \Sigma } ^ { ( m ) } {  } { \pmb { A } } _ { r }$ endfor endfor

(3）for $m = 2 q - 1$ to $\pmb q$ do $\big / \ast$ 按 $j$ 维复制 $\pmb { \mathcal { B } } \ast \boldsymbol { \mathit { \iota } }$ for all $r$ in $\left\{ \mathbf { \nabla } _ { \mathbf { \mathcal { P } } } , r _ { m } = r _ { q + m } \right\}$ par-do $\mathbf { B } _ { r } ^ { { ( m ) } } { \gets } \mathbf { B } _ { r }$ endfor endfor

(4） for $\boldsymbol r = 0$ to ${ \pmb { \mathscr { p } } } - 1 \ \mathbf { p a r } - \mathbf { d o } \ / \ { \pmb { \mathscr { x } } }$ 相乘 $\yen 7$ $\pmb { C } _ { r } = \pmb { A } _ { r } \times \pmb { B } _ { r }$ endfor

(5) for $m = 2 q$ to $3 q - 1$ do $\gamma *$ 求和 $\yen 7$ for $\mathbf { \nabla } _ { r } = \mathbf { 0 }$ to $\pmb { \mathscr { p } } - 1 \ \pmb { \mathrm { p a r } } - \ \pmb { \mathrm { d o } }$ $C _ { r } { = } C _ { r } { + } C _ { r } { ^ { ( m ) } }$ endfor endfor

End

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0004_pages_0211-0280/auto/images/a61572003f89b2136a8f363c4d78e5d3ab8562f4e6df6adc7bf6f89384cd23f6.jpg)  
图9.13 $4 \times 4$ 的矩阵在64个处理器上的DNS乘法(a)A、B起始分布；（b)Ai,,从P,j,o传到P.,;(c）所有 $\pmb { A } _ { i , j }$ 沿 $j$ 维播送；（d)所有 $\pmb { B } _ { i }$ 沿 $_ i$ 维播送

算法分析由算法9.6可知,使用 $n ^ { 3 }$ 个处理器的DNS 乘法,其并行运行时间为 $O ( \log n )$ ,它不是成本最佳的。

算法讨论在图9.12中,是以 $\pmb { A } _ { 2 \times 2 } \times 2 \pmb { B } _ { 2 \times 2 }$ 为例的，如果矩阵的阶超过2（例如为4),则这种表示就不方便了，但可以采用图9.13所示的方法进行DNS相乘。图9.13(a)是 $\pmb { A }$ 和 $\pmb { B }$ 的起始加载，此时 $\pmb { A }$ 矩阵的行按 $j$ 维分布； $\pmb { B }$ 矩阵的列按 $_ i$ 维分布。复制时，首先 $\pmb { A }$ 和 $\pmb { B }$ 同时沿 $\pmb { k }$ 维进行一到一播送,其中如图9.13(b), $\mathbf { A } _ { i , j }$ 从 $\mathrm { P } _ { i , j , 0 }$ 传到 $\mathbf { P } _ { i , j , j }$ (类似地 $\pmb { { \cal B } } _ { i }$ ,j从 $\mathbf { P } _ { i , j , 0 }$ 传到 $\mathbf { P } _ { i , j , i } )$ ；然后 $\pmb { A }$ 在不同的 $\pmb { k }$ 平面内将其列沿 $j$ 维同时进行一到多播送，其结果如图 $9 . 1 3 ( \mathfrak { c } )$ 所示。类似地, $\pmb { B }$ 在不同的 $k$ 平面内将其行沿 $_ i$ 维同时进行一到多播送,其结果如图9.13(d)所示。复制完毕后， $\mathbf { A } _ { i , k }$ 与 $\mathbf { B } _ { k }$ ,,就可以在 $\mathbf { P } _ { i , j , k }$ 中相乘了；然后每个乘积元素$\mathbf { { C } } _ { i } ,$ 再沿 $k$ 维进行单点累积。在此过程中,处理器 $\mathbf { P } _ { i , j , 0 }$ 就收集了来自处理器$\mathbf { P } _ { i , j , 1 } , \cdots , \mathbf { P } _ { i , j , n - 1 }$ 的乘积。为了清楚起见，图9.13(c)和 $(  { \mathbf d } )$ 只示出了 $\pmb { C } _ { 0 , 0 }$ 的计算。

当处理器的数目 $\ p < n ^ { 3 }$ 时,为了执行 DNS乘法,可以假定 $\pmb { \mathscr { p } } = q ^ { 3 }$ ,而 $q <$ $\pmb { n }$ 。此时原 ${ \pmb n } \times { \pmb n }$ 的矩阵可以划分成大小为 $( n / q ) \times ( n / q )$ 的一些块,每个矩阵可以视为 ${ \pmb q } \times { \pmb q }$ 的分块矩阵。这样在 $q ^ { 3 }$ 个处理器上执行DNS算法与在 $\mathbf { \dot { \boldsymbol { n } } } ^ { 3 }$ 个处理器上执行DNS算法类似，只是前者是块运算后者是单独元素运算。

当分块的DNS算法执行在 $\scriptstyle { p < n ^ { 3 } }$ 个处理器的超立方上时，若使用CT选路法,算法执行一到一传送的时间为 $t _ { \mathrm { s } } + t _ { \mathrm { w } } ( n / q ) ^ { 2 } + t _ { \mathrm { h } } \mathrm { l o g } q$ （见第八章8.2节）；算法执行一到多播送的时间为 $( t _ { \mathrm { s } } + t _ { \mathrm { w } } ( n / q ) ^ { 2 } ) \mathrm { l o g } q$ (见第八章表8.1);算法执行单点收集的时间为 $t \sqrt { \smash [ b ] { 3 } q + t  { \mathbf { w } } ( \ b { n } / q ) ^ { 2 }  { \log { q } } }$ 。假定乘-加操作取单位时间，则 $\left( n \right/$ $\mathbf { \boldsymbol { q } } ) \times ( \mathbf { \boldsymbol { n } } / q )$ 块阵乘法的时间为 $( n / q ) ^ { 3 }$ 。略去一到一传送时间和收集过程中的加法时间,则在超立方上使用CT选路法的DNS乘法之并行运行时间为：

$$
T _ { \mathrm { p } } { \approx } ( \frac { n ^ { 3 } } { q } ) + 3 t _ { \mathrm { s } } { \log } q + 3 t _ { \mathrm { w } } \bigl ( \frac { n } { q } \bigr ) ^ { 2 } { \log } q
$$

因为 $q = \pmb { \mathscr { p } } ^ { 1 / 3 }$ ，所以

$$
T _ { \mathrm { p } } = { \frac { n ^ { 3 } } { \hbar } } + t _ { \mathrm { s } } \mathrm { l o g } \hbar + t _ { \mathrm { w } } { \frac { n ^ { 2 } } { { \hbar } ^ { 2 / 3 } } } \mathrm { l o g } \hbar
$$

# 9.5小结和导读

小结本章所研究的矩阵都是稠密阵，又称为满阵(FullMatrices),与其相对是稀疏阵(SparseMatrices)。稠密阵几乎没有零元素，而稀疏阵其绝大多数元素均为零。之所以要区分出稀疏阵，是因为可以利用非零元素的号码与位置来减少运算时间。本章着重讨论了稠密阵的最基本的运算,包括矩阵转置、矩阵乘向量和矩阵乘法等运算。这些算法在执行过程中几乎用到了第八章所讲的所有基本通信操作，所以在分析算法的通信时间时，读者要不断参照第八章的有关

内容。

从处理器的利用能力等来看，棋盘划分比带状划分要好，这一点从第9.3节“矩阵-向量乘法”的讨论可以得到证实;简单的并行分块乘法虽然运行时间较快,但对存储要求过大;从存储要求来看，Cannon乘法和Fox乘法优于简单并行分块乘法，特别是Cannon乘法综合性能较优，所以使用得较普遍；从加速能力来看,DNS乘法的加速比较大，特别是它经常被别的算法作为基本算法加以调用,所以使用较广。

除了本章所讨论的矩阵运算外，矩阵的分解、矩阵的求逆和矩阵求特征值等也是很常见的矩阵运算，但限于篇幅，就不再讨论了。

导读关于并行与分布式数值算法，[31]是一本很好的参考书。有关矩阵运算,[78]是一本很经典的教本(此书的第一版有中译本：廉庆荣等译.矩阵计算.大连：大连理工大学出版社,1988)。本章所讨论的Cannon乘法、Fox乘法和DNS乘法，原始论文分别来源于[40]、[68]和[58]。这些算法的改进版本可参考[30]和[94]。有关并行矩阵算法的可扩放性分析，读者可阅读[84]。在[113,114]书中的第五章的参考文献注释中还列举了大量有关稠密矩阵的算法，读者可追踪进一步阅读。

# 习 题

9.1根据9.2.1节所讨论的矩阵转置算法：

$\textcircled{1}$ 试写出二维网孔上递归矩阵转置算法的形式描述；  
$\textcircled{2}$ 试写出超立方上递归矩阵转置算法的形式描述。

9.2根据9.3.2节所讨论的矩阵-向量乘法，试证明：在 $\pmb { \hat { p } }$ 个处理器的超立方上，用SF选路方法进行矩阵-向量乘法,其并行运行时间约为n²/p+tlogp+(3/2)tw(n/√p)logp。

）.3试分析在超立方上执行矩阵-向量乘法时，使用棋盘划分比带状划分为优。

9.4试证明:在使用带状划分的超立方上执行矩阵-向量乘时，其等效率函数$f _ { \mathtt { E } } ( \mathbf { \Psi } _ { \pmb { \mathscr { P } } } ) = O ( \mathbf { \Psi } _ { \pmb { \mathscr { P } } } ^ { 2 } ) _ { \mathtt { c } }$

[提示：将(9.4)式代人 $\pmb { \phi } ^ { \star } \mathbb { T } _ { \mathbb { P } } = \pmb { T } _ { 0 } + \pmb { W }$ 从而求出 $T _ { 0 }$ ，再由 $\pmb { W } = \pmb { K } \pmb { T } _ { 0 }$ 和 $\scriptstyle { \overrightarrow { W } } = n ^ { 2 }$ 求出 $\pmb { n }$ 与 $\pmb { \hat { p } }$ 的关系，最后求出等效率函数 $f _ { \Xi } ( \pmb { \mathscr { p } } ) = f ( \pmb { \mathscr { p } } ) ]$ 。

9.5试证明：在使用棋盘划分的网孔上执行矩阵-向量乘时，其等效率函数

$$
f _ { \mathrm { E } } ( \boldsymbol { \phi } ) = O ( \operatorname* { m a x } \{ \boldsymbol { \phi } ^ { 3 / 2 } , \boldsymbol { \phi } \log \boldsymbol { \phi } \} ) \mathrm { , }
$$

[提示：参见习题9.4的提示。]

9.6试证明：在超立方上，并行分块矩阵乘法和Cannon乘法的等效率函数均为fe（p）=$O ( p ^ { 3 / 2 } )$ ；而 $\mathtt { F o x }$ 乘法的等效率函数为 $f _ { \mathtt { E } } ( \mathtt { \Delta } _ { \mathtt { p } } ) = O ( \mathtt { \Delta } _ { \mathtt { p } } ^ { 3 / 2 } \mathrm { l o g } \mathtt { p } )$ 。

9.7根据9.4.3节所讨论的Fox乘法：

$\textcircled{1}$ 试写出 $\mathbf { F o x }$ 乘法的形式描述；

$\textcircled{2}$ 试分析 $\mathtt { F o x }$ 乘法的主要优点是什么。

9.8试推导：在 $\boldsymbol { p } ^ { 1 / 3 } \times \boldsymbol { p } ^ { 1 / 3 } \times \boldsymbol { p } ^ { 1 / 3 }$ 三维网孔上，使用CT选路方法时DNS乘法的并行运行时间。

9.9算法9.7给出了 $n ^ { 2 }$ 个处理器的并行系统上用PRAM-CREW模型施行两个 $\mathbf { \Omega } _ { n } \times \mathbf { \Omega } _ { n }$ 矩阵相乘的算法。假定存储器的读写时间为 $\pmb { t _ { a } }$ ，两个元素的乘－加时间为 $t _ { \mathrm { c } }$ 。试分析该算法的并行运行时间。

算法9.7 PRAM-CREW上矩阵相乘算法  
输入: Anxn,Bn×n  
输出： $C _ { n \times n }$   
Begin(1)将 ${ \pmb n } ^ { 2 }$ 个处理器组织成 ${ \pmb n } \times { \pmb n }$ 的网孔(2)for each $\mathrm { P } _ { i , j }$ do(2.1) $\pmb { c _ { i , j } = 0 }$ (2.2)for $k = 0$ to $\pmb { n } - \pmb { 1 }$ do$c _ { i , j } = c _ { i , j } + a _ { i , k } \times b _ { k , j }$ endforendfor  
End

9.10参照图9.14,算法9.8描述了m×k二维Systolic阵列上实现Am×n×Bxk=Cm×k的矩阵乘法,它是采用流水线原理,通过在时间上延迟矩阵元素的办法来达到一对下标合宜的矩阵元素适时相乘的目的。

算法9.8 $\mathbf { S I M D } ^ { - } \mathbf { M C } ^ { 2 }$ 上 Systolic矩阵相乘算法  
输入： $\mathbf { A } _ { m \times n } , \mathbf { B } _ { n \times k }$   
输出：在 $\mathrm { P } _ { i , j }$ 中存有乘积矩阵元素 $c _ { i , j }$   
Beginfor ${ \bf \nabla } _ { i } = 1$ to m par - dofor $j = 1$ to $k \ p a r - \mathrm { d } \mathbf { 0 }$ (1) $c _ { i , j } = 0$ (2） while $\ P _ { i , j }$ 收到 $^ { a }$ 和 $^ b$ 时 ${ \bf d o }$ $( 2 . 1 ) c _ { i , j } = c _ { i , j } + a \times b$ (2.2)if $i < m$ then 发送 $^ { b }$ 给 $\mathrm { P } _ { i + 1 , j }$ endif(2.3)if $j < k$ then 发送 $^ { a }$ 给 $\mathrm { P } _ { i , j + 1 }$ endifendwhileendforendfor  
End

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0004_pages_0211-0280/auto/images/e3745e7ca92cf04127b4413b56c656e1699b43531e430d3c85fb6ab84e7bb66d.jpg)  
图9.14矩阵 $\pmb { A }$ 和 $\pmb { \cal B }$ 的输入加载方式

试问： $\textcircled{1}$ 为了确保 ${ \pmb { a } } _ { i }$ 与 $\delta _ { s , j }$ 适时在 $\mathbf { P } _ { i , j }$ 相遇， $\pmb { A }$ 矩阵的第i行要比第i-1行 $( 2 \leqslant i \leqslant m )$ 滞后多少时间单位？同样， $\mathbf { B }$ 矩阵的第 $\pmb { j }$ 列要比第 $j - 1$ 列 $( 2 { \leqslant } j { \leqslant } k )$ 滞后多少时间单位？

$\textcircled{2}$ 当 $j = k$ 时， $\pmb { \alpha }$ 传送给 $\pmb { \mathrm { P } } _ { i , j + 1 }$ 吗？当 $i = m$ 时， $b$ 传送给 $\bar { \mathbf { P } } _ { i + 1 , j }$ 吗?

# 第十章 线性方程组的求解

很多科学与工程计算问题大都可以化为线性代数方程组的形式，所以有效的求解线性方程组在科学和工程计算中是非常重要的。虽然线性代数方程的求解方法和数值计算软件包(如Linpack等)均很成熟，但随着并行计算机的发展，问题的求解速度和解题规模都大大提高，因而使数值计算方法和相应的数学软件包都产生了变化,相应地线性方程组的有效并行求解也引起了人们的普遍关注。本章主要讨论基本线性方程组的求解,包括三角形方程组的求解、三对角方程组的求解、稠密线性方程组的求解和稀疏线性方程组的求解。对于每一种求解问题,我们首先讨论它的数值求解数学原理;接着给出其串行算法;然后分析串行算法中的并行性及并行化方法并给出相应的并行算法(有时我们只作简单的并行化分析）。

# 10.1三角形方程组的求解

# 10.1.1基本术语

本小节是预备性知识。为了读者阅读下文方便,先给出几个有关定义：

定义10.1一个 $\pmb { n }$ 个变量 $x _ { 1 } , x _ { 2 } , \cdots , x _ { n }$ 的线性方程(Linear Equation)可表示为：

$$
a _ { 1 } x _ { 1 } + a _ { 2 } x _ { 2 } + \cdots + a _ { n } x _ { n } = b
$$

其中， $a _ { 1 } , a _ { 2 } , \cdots , a _ { n }$ 和 $^ { b }$ 均为常数。

定义10.2变量 $x _ { 1 } , x _ { 2 } , \cdots , x _ { n }$ 的一组线性方程称为 $\pmb { n }$ 元线性方程组(Sys-tem of Linear Equations),也详称为 $\pmb { n }$ 个变量 $\pmb { n }$ 个方程线性联立方程组，简称为线性系(Linear System),可表示为：

$$
\begin{array} { c } { \alpha _ { 1 1 } x _ { 1 } + a _ { 1 2 } x _ { 2 } + \cdots + a _ { 1 n } x _ { n } = b _ { 1 } } \\ { \qquad \quad } \\ { a _ { 2 1 } x _ { 1 } + a _ { 2 2 } x _ { 2 } + \cdots + a _ { 2 n } x _ { n } = b _ { 2 } } \\ { \qquad \quad } \\ { \qquad \vdots \qquad \quad } \\ { \qquad \quad } \\ { a _ { \mathrm { \scriptsize ~ - ~ 1 ~ } } x _ { 1 } + a _ { \mathrm { \scriptsize ~ - ~ 2 ~ } } x _ { 2 } + \cdots + a _ { \mathrm { \scriptsize ~ ~ - ~ } } r = b } \end{array}
$$$$
\alpha _ { n 1 } x _ { 1 } + \alpha _ { n 2 } x _ { 2 } + \cdots + \alpha _ { n n } x _ { n } = b _ { n }
$$

它通常也可写成矩阵-向量形式：

$$
\begin{array} { r } { \left( \begin{array} { c c c c c } { a _ { 1 1 } } & { a _ { 1 2 } } & { \cdots } & { a _ { 1 n } } \\ { a _ { 2 1 } } & { a _ { 2 2 } } & { \cdots } & { a _ { 2 n } } \\ & { \vdots } & & & \\ { a _ { n 1 } } & { a _ { n 2 } } & { \cdots } & { a _ { n n } } \end{array} \right) \left( \begin{array} { c } { x _ { 1 } } \\ { x _ { 2 } } \\ { \vdots } \\ { x _ { n } } \end{array} \right) = \left( \begin{array} { c } { b _ { 1 } } \\ { b _ { 1 } } \\ { \vdots } \\ { b _ { n } } \end{array} \right) } \end{array}
$$

简记之为 $\mathbf { A } { \boldsymbol { \mathbf { \mathit { x } } } } = \mathbf { \mathit { \mathbf { b } } }$ 。其中矩阵 $\pmb { A }$ 中非零元素的位置和值决定了求解 $_ { x }$ 的困难复杂程度。通常一个顺序求解 $\mathbf { \nabla } \mathbf { \pmb { A } } \mathbf { \nabla } \pmb { x } = \mathbf { \nabla } \mathbf { \delta }$ 的算法的时间复杂度为 $O ( n ^ { 3 } )$

定义 10.3一个 $\textbf { \em n } \times \textbf { \em n }$ 的矩阵是上三角(Upper Triangular）的,如果 $i > j$ 时， $a _ { i j } = 0$ 。

定义 10.4一个 $\textbf { \em n } \times \textbf { \em n }$ 的矩阵是下三角(Lower Triangular)的,如果 $i < j$ 时， $\alpha _ { i j } = 0$ 。

定义10.5一个 $\pmb { n } \times \pmb { n }$ 的矩阵是三对角(Tridiagonal)的,当且仅当 $| i - j |$ $> 1$ 时， $a _ { i j } = 0 _ { \circ }$

相应地，在 $\mathbf { A } \mathbf { x } = \mathbf { b }$ 中,若系数矩阵 $\pmb { A }$ 是上(下)三角的,则称其为上(下)三角线性方程组；若系数矩阵 $\pmb { A }$ 是三对角的，则称其为三对角线性方程组。

零元素出现在适当位置的线性方程组比任意形式的方程组的求解要快得多。例如上三角线性方程组和下三角线性方程组，在串行机上可在 $O ( n ^ { 2 } )$ 时间界内求解;而三对角线性方程组则可在 $O ( n )$ 时间界内求解。

定义 10.6一个 $\pmb { n } \times \pmb { n }$ 的矩阵是对角占优(Diagonal Dominant）的,如果 $\mid a _ { i i } \mid$ $> \sum _ { j \neq i } ^ { } \mid a _ { i j } \mid , 1 { \leqslant i , j { \leqslant n _ { \circ } } }$

定义10.7一个n×n的矩阵是对称(Symmetric)的,如果aj=ai,1≤i,j$\leqslant n$ 。

定义10.8一个 ${ \pmb n } \times { \pmb n }$ 的矩阵称为正定(Positive Definite)的,如果对于非零向量 $\pmb { X }$ 及其转置 $\pmb { X } ^ { \mathsf { T } }$ ，则乘积 $\pmb { X } ^ { \updownarrow } \pmb { A } \pmb { X } > 0$ 。

例如所有对称的、对角占优的且 $a _ { j i } > 0$ 的矩阵都是正定的。

# 10.1.2上三角方程组的求解

SISD上回代解法先看一个例子。假定欲求解以下上三角方程组：

$$
\begin{array} { r } { { 1 } x _ { 1 } + { 1 } x _ { 2 } - { 1 } x _ { 3 } + { 4 } x _ { 4 } = 8 } \\ { - 2 x _ { 2 } - 3 x _ { 3 } + { 1 } x _ { 4 } = 5 } \\ { 2 x _ { 3 } - 3 x _ { 4 } = 0 } \\ { 2 x _ { 4 } = 4 } \end{array}
$$

先求解最后一个方程,得x4=2,将其值代入其它方程,清去x4这一项,从而有

$$
\begin{array} { r l } { { 1 } x _ { 1 } + 1 x _ { 2 } - 1 x _ { 3 } \quad } & { { } = 0 } \\ { - 2 x _ { 2 } - 3 x _ { 3 } \quad } & { { } = 3 } \end{array}
$$

$$
\begin{array} { r l r l } { { 2 } x _ { 3 } } & { { } } & { } & { { } = 6 } \\ { 2 x _ { 4 } } & { { } } & { } & { { } = 4 } \end{array}
$$

再求解第3个方程,得 $_ { x _ { 3 } } = 3$ ,将其代人第1和2个方程,消去 $x _ { 3 }$ 这一项,从而有

$$
\begin{array} { r l r l } { { 1 } x _ { 1 } + 1 x _ { 2 } } & { { } } & { } & { { } = 3 } \\ { - 2 x _ { 2 } } & { { } } & { } & { { } = 1 2 } \\ { 2 x _ { 3 } } & { { } } & { } & { { } = 6 } \\ { 2 x _ { 4 } } & { { } } & { } & { { } = 4 } \end{array} ,
$$

同样,消去 $x _ { 2 }$ ,最后将欲求解的上三角方程化成了如下形式的对角方程：

$$
\begin{array} { r l r l } { { 1 } x _ { 1 } } & { { } } & { } & { { } = 9 } \\ { - 2 x _ { 2 } } & { { } } & { } & { { } = 1 2 } \\ { 2 x _ { 3 } } & { { } } & { } & { { } = 6 } \\ { 2 x _ { 4 } } & { { } } & { = 4 } \end{array}
$$

易知 $x _ { 1 } = 9$

一个回代法(Back Substituting)求解上三角方程组的顺序算法如算法10.1。

算法10.1 SISD上回代求解上三角方程组算法

输入： $\mathbf { A } _ { n \times n } , \mathbf { \boldsymbol { b } } = [ b _ { 1 } , \cdots , b _ { n } ] ^ { \mathrm { T } }$ 输出： $\pmb { x } = [ \pmb { x } _ { 1 } , \cdots , \pmb { x } _ { n } ] ^ { \top }$

Begin

$$
x _ { i } = b _ { i } / a _ { i i }
$$

$$
\begin{array} { l } { b _ { j } = b _ { j } - a _ { j i } x _ { i } } \\ { a _ { j i } = 0 . } \end{array}
$$

# end for

end for

End

显然,算法10.1的复杂度为 $O ( n ^ { 2 } )$ 。

如果分析一下算法10.1,则知算法的(1.2)步,即j循环是可以并行化的，于是有如下UMA上回代求解上三角方程组的并行算法10.2。

UMA上回代解法 UMA是一种共享存储的 MIMD多处理机计算模型,其中所有处理器通过互连机制均匀一致地访问共享存储器。

算法10.2UMA上回代求解上三角方程组算法   
输入： $\mathbf { A } _ { n \times n } , \pmb { b } = \smash { \left[ b _ { 1 } , \cdots , b _ { n } \right] ^ { \mathrm { T } } }$   
输出： $\mathbf { X } = [ \mathbf { \Psi } _ { X _ { 1 } } , \cdots , \mathbf { \Psi } _ { X _ { n } } ] ^ { \mathrm { { T } } }$   
Begin for ${ \bf { \ell } } _ { i } = n$ to 1 do $x _ { i } = b _ { i } / a _ { i i }$ for all $\mathbf { P } _ { j }$ ,where $1 { \leqslant } j { \leqslant } p$ do $\times ~ { \pmb { p } }$ 为处理器数 $\yen 7$ for $k = j$ to ${ \bf \chi } _ { i } - 1$ step $\pmb { \hat { p } }$ do $\begin{array} { l } { b _ { k } = b _ { k } - a _ { k i } x _ { i } } \\ { a _ { k i } = 0 } \end{array}$ endfor endfor all endfor   
End

显然,算法10.2之复杂度为 $\boldsymbol { \hat { p } } \left( \boldsymbol { n } \right) = \boldsymbol { \hat { p } } , t \left( \boldsymbol { n } \right) = \boldsymbol { O } \left( \boldsymbol { n } \right)$ 。

# 10.2三对角方程组的求解

本节打算介绍两种求解三对角方程组的方法：直接求解法，适合于在串行机上执行,但不适合并行化;奇偶归约求解法,虽有较高的比例常数,但易于并行化。

# 10.2.1 三对角方程组直接求解法

例示直接求解方法三对角方程组中的系数矩阵，除了三条对角线上的元素为非零外，其余元素均为零,但通常没有只含一个变量的方程，因此不能用上节解上三角方程组的办法对它进行求解，为此需进行一些变换。先看一个具体例子。假定欲求解以下三对角方程组：

$$
\begin{array} { r c l } { { } } & { { } } & { { 1 6 x _ { 1 } + ~ 4 x _ { 2 } } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { 4 x _ { 1 } + 1 1 x _ { 2 } - ~ 5 x _ { 3 } } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { 2 x _ { 2 } + 1 4 x _ { 3 } - ~ 6 x _ { 4 } } } \\ { { } } & { { } } & { { ~ 5 x _ { 3 } + 1 8 x _ { 4 } } } \end{array}
$$

$$
\begin{array} { r l } { { \mathbf { \Omega } } } & { { } = 8 \qquad { \mathbb { O } } } \\ { { \mathbf { \Omega } } } & { { } = 7 \qquad { \mathbb { O } } } \\ { { \mathbf { \Omega } } } & { { } = 1 3 \qquad { \mathbb { O } } } \\ { { \mathbf { \Omega } } } & { { } = 2 4 \qquad { \mathbb { O } } } \end{array}
$$

首先， $\textcircled { 2 } - \frac { 1 } { 4 } \textcircled { 1 }$ ，消去第 $\textcircled{2}$ 个方程中的 $\pmb { x _ { 1 } }$

$$
\begin{array} { c } { 1 6 x _ { 1 } + 4 x _ { 2 } } \\ { 1 0 x _ { 2 } - 5 x _ { 3 } } \end{array}
$$

然后， $\textcircled { 3 } - \frac { 1 } { 5 } \textcircled { 2 }$ ，消去第 $\textcircled{3}$ 个方程中的 $x _ { 2 }$ ：

$$
\begin{array} { c } { { \ S x _ { 1 } + 4 x _ { 2 } } } \\ { { \ O } } \\ { { 1 0 x _ { 2 } - 5 x _ { 3 } } } \\ { { \ O } } \\ { { 1 5 x _ { 3 } - \ O 6 x _ { 4 } } } \\ { { \ O } } \\ { { \ S x _ { 3 } + 1 8 x _ { 4 } } } \end{array}
$$

$$
\begin{array} { r l } { { \mathbf { \Omega } } } & { { } \quad \mathbb { 0 } } \\ { { \mathbf { \Omega } } } & { { } = { \mathbf { 5 } } } \\ { { \mathbf { \Omega } } } & { { } \quad \mathbb { 2 } } \\ { { \mathbf { \Omega } } } & { { } \quad \mathbb { 3 } } \\ { { \mathbf { \Omega } } } & { { } \quad \mathbb { 4 } } \end{array} \qquad { \begin{array} { r l } { { \mathbb { D } } } & { { } } & { { \mathbb { 1 } } } \\ { { \mathbb { 2 } } } & { { } } \\ { { \mathbb { 3 } } } & { { } } \\ { { \mathbb { 2 } } } & { { } } \end{array} }
$$

最后， $\textcircled { 4 } - \frac { 1 } { 3 } \textcircled { 3 }$ ，消去第 $\textcircled{4}$ 个方程中的 $\pmb { x } _ { 3 }$ ：

$$
\begin{array} { c } { 1 6 x _ { 1 } + 4 x _ { 2 } } \\ { 1 0 x _ { 2 } - 5 x _ { 3 } } \\ { 1 5 x _ { 3 } - 6 x _ { 4 } } \\ { 2 0 x _ { 4 } } \end{array}
$$

$$
\begin{array} { l } { { \mathbf { \eta } } } \\ { { \mathbf { \eta } } } \\ { { \mathbf { \eta } } } \\ { { \mathbf { \eta } } } \\ { { \mathbf { \eta } } } \\ { { \mathbf { \eta } } } \end{array} \Vdash \mathbf { 1 } 2
$$

此时三对角方程组的最后一个方程只含一个变量,这样就可以用回代法直接求解了。

三对角方程组的一般形式在正式给出 SISD上求解三对角方程组的算法之前，先考虑三对角方程组的一般形式。注意，在三对角方程组中，第一个和最后一个方程中只含有两个变量，其余均有三个变量，于是可以将三对角方程组一般化表示如下：

$$
\begin{array} { r l r } { g _ { 1 } x _ { 1 } + h _ { 1 } x _ { 2 } } & { = b _ { 1 } } \\ { f _ { i } x _ { i - 1 } + g _ { i } x _ { i } + h _ { i } x _ { i + 1 } } & { = b _ { i } } & { , 2 \leqslant i \leqslant n - 1 } \\ { f _ { n } x _ { n - 1 } + g _ { n } x _ { n } } & { = b _ { n } } \end{array}
$$

SISD上直接求解法一个直接求解三对角方程组的顺序算法如算法10.3。

算法10.3 SISD上直接求解三对角方程组算法

输入： $\mathbf { \delta } _ { { \pmb { A } } _ { n } \times { \pmb { n } } } , { \pmb { b } } = [ b _ { 1 } , \cdots , b _ { n } ] ^ { \mathbb { T } }$ 输出： $\mathbf { \pmb { x } } = [ \mathbf { \mathscr { x } } _ { 1 } , \cdots , \mathbf { \mathscr { x } } _ { n } ] ^ { \mathsf { T } }$

Begin

(1） for ${ \dot { \pmb { \imath } } } = { \boldsymbol { 1 } }$ to $\pmb { n } - 1$ do$\begin{array} { r } { { g _ { i + 1 } } = { g _ { i + 1 } } - ( { f _ { i + 1 } } / { g _ { i } } ) { h _ { i } } } \\ { \smash { { b _ { i + 1 } } = { b _ { i + 1 } } - ( { f _ { i + 1 } } / { g _ { i } } ) { b _ { i } } } } \end{array}$

end for

(2） for $i = n$ to 2 do

$$
x _ { i } = b _ { i } / g _ { i }
$$

$$
b _ { i - 1 } = b _ { i - 1 } - x _ { i } h _ { i - 1 }
$$

# end for

End

显然,算法10.3的复杂度为 $O ( n )$

并行化分析仔细分析算法10.3,并参照上述具体例子可知,算法第(1)步,每次循环计算 $\pmb { g }$ 与 $^ { b }$ 时会用到前次循环计算的结果，所以此循环不能并行执行。同样,算法第(2)步,由于回代计算的顺序性,所以该循环也不能并行执行。因此,为了并行化必须另寻途径。

# 10.2.2三对角方程组奇偶归约求解法

奇偶归约法原理首先将(10.2)式所示的三对角方程组改写成如下的一个通式：

$$
f _ { i } x _ { i - 1 } + g _ { i } x _ { i } + h _ { i } x _ { i + 1 } = b _ { i } \quad , \quad 1 \leqslant i \leqslant n
$$

$$
f _ { 1 } = h _ { n } = 0
$$

然后奇偶归约法求解三对角方程组分成两步：第一步消去偶序号方程组中具有奇下标的 $\pmb { x _ { i } }$ 变量;第二步回代求解。消去 $\pmb { x } _ { 2 i - 1 }$ 和 $\pmb { x } _ { 2 i + 1 }$ 的方法可描述如下：

$$
\begin{array} { r l r } { \phantom { \frac { 1 } { 2 } } f _ { 2 i - 1 } x _ { 2 i - 2 } + g _ { 2 i - 1 } x _ { 2 i - 1 } + h _ { 2 i - 1 } x _ { 2 i } } & { = b _ { 2 i - 1 } } \\ { f _ { 2 i } x _ { 2 i - 1 } + g _ { 2 i } x _ { 2 i } + h _ { 2 i } x _ { 2 i + 1 } } & { = b _ { 2 i } } \\ { f _ { 2 i + 1 } x _ { 2 i } + g _ { 2 i + 1 } x _ { 2 i + 1 } + h _ { 2 i + 1 } x _ { 2 i + 2 } = b _ { 2 i + 1 } } \end{array}
$$

第一式乘以 $- f _ { 2 i } g _ { 2 i } ^ { - 1 } -$ 1后加到中间一式；第三式乘以 $- h _ { 2 i } g _ { 2 i } ^ { - 1 } +$ 后亦加到中间-式,这样中间一式就变为：

$$
\begin{array} { r l } & { - f _ { 2 i } g _ { 2 i - 1 } ^ { - 1 } f _ { 2 i - 1 } x _ { 2 i - 2 } + ( g _ { 2 i } - f _ { 2 i } g _ { 2 i - 1 } ^ { - 1 } h _ { 2 i - 1 } - h _ { 2 i } g _ { 2 i + 1 } ^ { - 1 } f _ { 2 i + 1 } ) x _ { 2 i } } \\ & { \qquad - h _ { 2 i } g _ { 2 i + 1 } ^ { - 1 } h _ { 2 i + 1 } x _ { 2 i + 2 } = b _ { 2 i } - f _ { 2 i } g _ { 2 i - 1 } ^ { - 1 } b _ { 2 i - 1 } - h _ { 2 i } g _ { 2 i + 1 } ^ { - 1 } b _ { 2 i + 1 } } \\ & { \qquad i = 1 , 2 , \cdots , \lfloor { n / 2 } \rfloor } \end{array}
$$

方程组(10.5)中只含偶下标的 $_ { \pmb { x } }$ 变量,它消去了原方程组(10.3)式中含奇下标的x变量,该方程仍然是一个三对角方程组，但变量少了一半。重复上述过程可使方程组的变量越来越少，最后只剩下二个或三个方程：

$$
\begin{array} { r } { g _ { 1 } x _ { 1 } + h _ { 1 } x _ { 2 } = b _ { 1 } } \\ { f _ { 2 } x _ { 1 } + g _ { 2 } x _ { 2 } = b _ { 2 } } \end{array}
$$

或

$$
\begin{array} { r l r } & { } & { \quad g _ { 1 } x _ { 1 } + h _ { 1 } x _ { 2 } \qquad = b _ { 1 } } \\ & { } & { f _ { 2 } x _ { 1 } + g _ { 2 } x _ { 2 } + h _ { 2 } x _ { 3 } = b _ { 2 } } \\ & { } & { f _ { 3 } x _ { 2 } + g _ { 3 } x _ { 3 } = b _ { 3 } } \end{array}
$$

从最后的方程组就可解得x1、x2或x1、x2、x30

一旦求出了上述 $_ { x }$ 的值,就可以开始回代,即将 $\boldsymbol { x } _ { 2 i - 2 } \ 、 \boldsymbol { x } _ { 2 i } \ 、 \boldsymbol { x } _ { 2 i + 2 }$ 代人(10.4)式即可解得 $x _ { 2 i - 1 }$ 和 $x _ { 2 i + 1 }$ 。此过程一直进行到解出了原方程组的所有变量为止。

SISD上奇偶归约法求解法习题10.1给出了一种 SISD上用奇偶归约法(Odd-Even Reduction)求解三对角方程组的算法形式描述。建议读者认真分析此算法，最好在计算机上编程实现它。

并行化分析根据上述求解原理可知,在第一步消元时可同时消去具有奇下标的 $_ { x }$ 变量，所以该步可直接并行化;同样，在回代时奇下标的变量亦可同时求解,所以也可直接并行化。

最后,如果对于所有的 $\dot { \pmb { \imath } }$ ，满足 $\mid _ { g _ { i } } \mid \geqslant \mid _ { f _ { i } } \mid + \mid h _ { i } \mid$ (即对角占优),则消去奇下标变量后的方程组仍具有对角占优的性质。所以只要三对角方程组是对角占优的,奇偶归约法就可使用(见习题10.2)。

# 10.3稠密线性方程组的求解

求解稠密线性方程组的经典数值方法有直接三角分解法(即LU分解法),正交三角分解法(即QR分解法)和蝶形分解法(即WZ分解法)。本节介绍最基本的求解稠密线性方程组的高斯消去法(Gaussian Elimination)。

# 10.3.1 有回代的高斯消去法

基本原理高斯消去法求解 $\mathbf { A } \mathbf { \boldsymbol { x } } = \mathbf { \boldsymbol { b } }$ 的基本思想是,将稠密系数矩阵 $\pmb { A }$ 化为上三角阵 $\pmb { T }$ ，然后对 $\pmb { T x } = \pmb { c }$ 施行回代求解。参照图10.1,在消元的过程中,在第i步时为了消去第i列的第i+1行到第n行中的元素(即化非零元素为零)，可以用行 $_ i$ 的倍数与其余行(第 $i + 1$ 行到第 $\pmb { n }$ 行)相减而达到目的。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0004_pages_0211-0280/auto/images/688251f14221f4b666352468554c5c7eb1ffe4685a29b7589085b8b90e68f08c.jpg)  
图10.1高斯消去法过程

选主元的高斯消去法为了确保数值解的稳定性，在第 $\textbf { \em i }$ 步时,应先找第 $_ i$ 列中第 $\pmb { i }$ 行到第 $\pmb { n }$ 行中绝对值最大的元素，此元素称之为主元(Pivot)；再将此元素所在的行(称为主元行)与第 $_ i$ 行施行交换。由于交换系数矩阵的两行只相当于交换两方程的位置,所以不影响求解结果。在实际执行中，每次迭代时并不真正交换主元行与第 $\pmb { i }$ 行,而是引人一些参量，指明迭代时是否某一特定行已被选作主元行等就可以了。

SISD上高斯主元消去法一个有回代的、采用选主元的求解稠密线性方程组的高斯消去顺序算法如算法10.4。其中,marked $\pmb { 1 } : \pmb { n }$ ，指明哪些行已选作主元行;pivot $\mathbf { 1 } : \pmb { n } ^ { \prime }$ 指明行 $\textbf { \em i }$ 被用作主元行的迭代步数;picked指明选作主元行的行。

# 算法10.4SISD上求解稠密线性方程组高斯主元消去算法

输入： $\mathbf { A } _ { n } \times _ { n } , \mathbf { \boldsymbol { b } } = \{ b _ { 1 } , \cdots , b _ { n } \} ^ { \mathbf { T } }$ 输出： $\mathbf { \Psi } \mathbf { x } = [ \mathbf { \Psi } _ { x _ { 1 } } , \cdots , \mathbf { \Psi } _ { x _ { n } } ] ^ { \mathrm { T } }$

# Begin

(1) for ${ \bf \nabla } _ { i } = 1$ to $\pmb { n }$ do $\mathbf { m a r k e d } _ { i } = 0$ end for

(2) for ${ i } = 1$ to $\pmb { n } - \pmb { 1 }$ do (2.1) $\mathbf { \ t e m p { = } 0 }$ (2.2) for $j = 1$ to $\pmb { n }$ do i $\mathbf { i f } \ \mathbf { m a r k e d } _ { j } = 0$ and $| a _ { j i } | >$ temp then $\mathrm { t e m p } = \left| \boldsymbol { a } _ { j i } \right|$ $\operatorname { p i c k e d } = j$ endif endfor (2.4) (2.3) $\begin{array} { l } { \mathrm { m a r k e d } _ { \mathrm { \ p i c k e d } } = 1 } \\ { \mathrm { p i v o t } _ { \mathrm { \ p i c k e d } } = i } \end{array}$ (2.5) for $j = 1$ to $\pmb { n }$ do $\mathbf { i f } \ m a r \mathbf { k e d } _ { j } = 0$ then (i)temp= aji /a picked,i (ii)for $k = i + 1$ to $\pmb { n }$ do $a _ { j k } = a _ { j k } - a _ { \mathrm { p i c k e d } , k } \star \mathrm { t e m p }$ endfor $( \mathrm { i i i } ) b _ { j } = b _ { j } - b _ { k } \star \mathrm { t e m p } \ .$

# endif

# endfor

end for (3) for $i = 1$ to $\pmb { n }$ do if marked $\mathbf { \epsilon } _ { i } = 0$ then $\mathrm { p i v o t } _ { i } = n$ break end if end for

End

显然,算法10.4的复杂度为 $O ( n ^ { 3 } )$ 。

并行化分析根据算法10.4可知，一旦主元行选定,所有非主元行的修改可同时进行,也就是说算法(2.5)步和(ii)步的中层的 $j$ 循环和最内层的 $k$ 循环可并行化。下面将讨论超立方连接的多计算机上如何执行高斯主元消去法。为此必须研究每次迭代时的数据相关性以便选择适当的处理器分配。如图10.2所示,在第 $\mathbf { \chi } _ { i }$ 次迭代确定主元行时,要求比较 $_ i$ 列中的各数据;而一旦主元行确定，未被选中的行 $\pmb { j }$ 中的每个元素 $a _ { j k }$ 在更新时要用到 $a _ { j i } \setminus a _ { \mathrm { p i c k e d } , }$ i和 $\alpha _ { \mathrm { p i c k e d } , k ^ { \circ } }$ 显然， $\pmb { \alpha }$ 和 $^ b$ 的分配直接影响着通信要求。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0004_pages_0211-0280/auto/images/a298a5419005094bbabbff8882e74ac0cd03bd9de09b1c0b3b67dd8ddb54d601.jpg)  
图10.2高斯消去法单步迭代时的数据相关性

超立方多计算机上高斯主元消去法假定采用按行划分法分配处理器，具体实现方法如算法10.5。其中,marked1:n/p指明哪些行已是主元行,pivot1:n/p指明迭代步数;value表示主元值;winner 是控制主元行的处理器。

算法10.5超立方多计算机上求解稠密线性方程组高斯主元消去算法

输入： $\mathbf { A } _ { n \times n } , \pmb { b } = [ b _ { 1 } , \cdots , b _ { n } ] ^ { \mathrm { T } }$ 输出： $\pmb { x } = [ \pmb { x } _ { 1 } , \cdots , \pmb { x } _ { n } ] ^ { \mathrm { T } }$

Begin

forall $\mathrm { \bf P } _ { i d }$ ，where $1 \leqslant i d \leqslant p$ do

(1）for ${ \bf \nabla } _ { i } = 1$ to $\scriptstyle { n / p }$ do $\nearrow$ 初始化；开始时所有行均非主元行 $\bigstar$ / $\mathbf { m a r k e d } _ { i } = 0$ end for

(2）for $i = 1$ to $\pmb { n } - 1$ do $\big / \big \varkappa$ 各处理器找主元候选者 $\yen 7$ (2.1) value ${ \bf \delta } = { \bf 0 }$ (2.2) for $j = 1$ to $n / \phi$ do $\begin{array} { r l } & { \mathrm { i f ~ } \operatorname* { m a r k e d } _ { j } = 0 \ \& \mid a _ { j i } \mid > \mathrm { v a l u e ~ t h e n } } \\ & { \mathrm { v a l u e } = \mid a _ { j i } \mid } \\ & { \mathrm { p i c k e d } = j } \end{array}$ end if end for

(2.3）winner $\mathbf { \mu } =$ id $\big / \big \varkappa$ 标记控制主元行的处理器 $\yen 7$ (2.4）MAX.TOURNAMENT (id,value,winner） $\big / . *$ 调用MAX

# 选全局最大主元 $\yen 7$

(2.5) if $i d \equiv$ winner then

(i) $\mathbf { m a r k e d } _ { \mathrm { p i c k e d } } = 1$   
(ii) $\mathbf { p i v o t } _ { \mathrm { p i c k e d } } = i$   
(iii） for $j = i$ to $\pmb { n }$ do temp.vector; = a picked,j end for   
${ \big ( } \mathrm { i } \mathbf { v } { \big ) } \ \mathrm { t e m p . } \mathbf { v e c t o r } _ { n + 1 } = b _ { \mathrm { p i c k e d } }$   
endif

(2.6） HC. BROADCAST( $\Dot { \pmb { \imath } } d$ , winner,temp. vector; $\tan + 1$ ） $\nearrow$ 主元处理器播送主元给其它处理器 $\yen 7$ (2.7) for $j = 1$ to $\pmb { n } / \pmb { \mathscr { p } }$ do $\big / \big \varkappa$ 未选中的行中消去列 $_ i$ 之元素 $\yen 7$

if marked; $\mathbf { \mu } = \mathbf { 0 }$ then  
(i) $\scriptstyle { \mathrm { t e m p } } = a _ { j i } / { \mathrm { t e m p } } . { \mathrm { v e c t o r } } _ { i }$   
(ii） for $k = i + 1$ to $\pmb { n }$ do$a _ { j k } = a _ { j k } - \mathrm { t e m p . } \mathrm { v e c t o r } _ { k } \times \mathrm { t e m p }$ end for

(iii) b;= b; - temp.vectorn+1 × temp

#

enai end for endfor (3）for $i = 1$ to $\pmb { n } / \pmb { \mathscr { p } }$ do $\big / \ast$ 定位从未被用作主元行的行 $\pmb { \mathscr { k } }$ / if marked ${ \bf \nabla } _ { i } = { \bf 0 }$ then $\mathsf { p i v o t } _ { i } = n$ break end if end for end for End MAX.TOURNAMENT( id ,value',winner) $\curvearrowright$ 被主程序所调用的过程 $\pmb { \mathscr { R } }$ / Reference:id,value',winner 局部变量:temp.value',temp.winner begin for $\mathbf { \nabla } _ { i } = \mathbf { 0 }$ to log ${ \pmb { \hat { p } } } - 1$ do （1）partner $= i d \oplus 2 ^ { i }$ (2）[partner]temp.value $\twoheadleftarrow$ value' (3）[partner]temp.winner $\twoheadleftarrow$ winner (4) if temp.value' $>$ value' then value' $\eqcirc$ temp. value' winner $\asymp$ temp. winner endif end for end

# 10.3.2无回代的高斯-约旦法

基本原理无回代的高斯－约旦法与有回代的高斯消去法基本思想一样，区别是，后者通过一系列的消元,最终使系数矩阵变成一个上三角阵，然后由第$\pmb { n }$ 个方程先解出 $x _ { n }$ ,令其代人第 $\dot { n } - 1$ 个方程解出 ${ \pmb x _ { n } } - { \pmb 1 }$ ,如此一直回代下去,最后由第一个方程解出 $x _ { 1 }$ ；而前者通过一系列消元,最终使系数矩阵变成一个对角阵,然后直接由第 $\textbf { \em i }$ 个方程解出 $x _ { i } ( i = 1 , 2 , \cdots , n )$ 。

下面以 $ \pmb { n = 4 }$ 为例来说明无回代的主元消去法的具体消元过程(为方便计算,令 $b _ { i }$ 改写成 $a _ { i } , _ { n + 1 } )$ ：

$\textcircled{1}$ 在系数矩阵中找绝对值最大者(主元),假定为 $\pmb { a } _ { 1 1 }$ ;将第一个方程乘以$- \ a _ { i 1 } / a _ { 1 1 }$ ,分别与第 $\textbf { \em i }$ 个方程相加 $( \mathbf { \it _ i } = 2 , 3 , 4 )$ ,于是有：

$$
\left( \begin{array} { c c c c } { { a _ { 1 1 } } } & { { a _ { 1 2 } } } & { { a _ { 1 3 } } } & { { a _ { 1 4 } } } \\ { { 0 } } & { { b _ { 2 2 } } } & { { b _ { 2 3 } } } & { { b _ { 2 4 } } } \\ { { 0 } } & { { b _ { 3 2 } } } & { { b _ { 3 3 } } } & { { b _ { 3 4 } } } \\ { { 0 } } & { { b _ { 4 2 } } } & { { b _ { 4 3 } } } & { { b _ { 4 4 } } } \end{array} \right) \left[ \begin{array} { c } { { x _ { 1 } } } \\ { { x _ { 2 } } } \\ { { x _ { 3 } } } \\ { { x _ { 4 } } } \end{array} \right] = \left[ \begin{array} { c } { { \alpha _ { 1 5 } } } \\ { { b _ { 2 5 } } } \\ { { b _ { 3 5 } } } \\ { { b _ { 4 5 } } } \end{array} \right]
$$

$\textcircled{2}$ 除去第一行,在剩下的系数矩阵中再找主元,假定为 $\pmb { b } _ { 2 2 }$ ;将第二个方程乘以 $- \ b _ { i 2 } / b _ { 2 2 }$ ,分别与第 $\textbf { \em i }$ 个方程相加 $( \mathbf { \zeta } _ { i } = 1 , 3 , 4 )$ ,于是有：

$$
\begin{array} { r } { \left\{ \begin{array} { c c c c } { \boxed { a _ { 1 1 } } } & { 0 } & { c _ { 1 3 } } & { c _ { 1 4 } } \\ { 0 } & { \boxed { b _ { 2 2 } } } & { b _ { 2 3 } } & { b _ { 2 4 } } \\ { 0 } & { 0 } & { c _ { 3 3 } } & { c _ { 3 4 } } \\ { 0 } & { 0 } & { c _ { 4 3 } } & { c _ { 4 4 } } \end{array} \right\} \left\{ \begin{array} { c } { x _ { 1 } } \\ { x _ { 2 } } \\ { x _ { 3 } } \\ { x _ { 4 } } \end{array} \right\} = \left\{ \begin{array} { c } { c _ { 1 5 } } \\ { b _ { 2 5 } } \\ { c _ { 3 5 } } \\ { c _ { 4 5 } } \end{array} \right\} } \end{array}
$$

$\textcircled{3}$ 重复之，最后得到的线性方程组为：

$$
\left\{ \begin{array} { c c c c } { { \boxed { \alpha _ { 1 1 } } } } & { { 0 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { \boxed { \hat { b } _ { 2 2 } } } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { \boxed { c _ { 3 3 } } } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { \boxed { d _ { 4 4 } } } } \end{array} \right\} \left\{ \begin{array} { c } { { x _ { 1 } } } \\ { { x _ { 2 } } } \\ { { x _ { 3 } } } \\ { { x _ { 4 } } } \end{array} \right\} = \left\{ \begin{array} { c } { { e _ { 1 5 } } } \\ { { e _ { 2 5 } } } \\ { { e _ { 3 5 } } } \\ { { d _ { 4 5 } } } \end{array} \right\}
$$

由此可直接解出 $x _ { 1 } = e _ { 1 5 } / \alpha _ { 1 1 } , x _ { 2 } = e _ { 2 5 } / b _ { 2 2 } , x _ { 3 } = e _ { 3 5 } / c _ { 3 3 }$ 和 $x _ { 4 } = d _ { 4 5 } / d _ { 4 4 }$ SISD上高斯-约旦主元消去法根据上述无回代求解稠密线性方程组的方法,参照算法10.4,读者不难写出 SISD上求解稠密线性方程组的高斯－约旦主元消去法的算法的形式描述,这作为习题留给读者去完成(习题10.6)。

PRAM上高斯-约旦消去法根据以上的讨论可知，一旦主元行选定后，消元的操作则可同时进行。选主元的方法和10.3.1节一样,所以下面算法10.6中，为了突出主题,选主元行部分并未示出，但读者可以参照算法10.5将它们补上。下面算法中假定使用 ${ n ^ { 2 } + n }$ 个处理器,并排成 $\pmb { n } \times \left( \pmb { n } + 1 \right)$ 的阵列。

算法10.6 PRAM上求解稠密线性方程组高斯-约旦消去算法输入： $\mathbf { A } _ { n } \times \mathbf { \mathit { \Pi } } _ { n } , \mathbf { \mathit { b } } = [ \mathbf { \mathit { b } } _ { 1 } , \cdots , \mathbf { \mathit { b } } _ { n } ] ^ { \mathrm { T } }$ 输出： ${ \pmb x } = [ { \pmb x } _ { 1 } , \cdots , { \pmb x } _ { n } ] ^ { \hat { \operatorname { T } } }$

Begin

(1）for $j = 1$ to $\pmb { n }$ do for $_ { i } = 1$ to $\pmb { n }$ par -do

for $k = j$ to n + 1 par - do if $i { \neq } j$ then $\alpha _ { i k } = \alpha _ { i k } - ( \alpha _ { i j } / \alpha _ { j j } ) \alpha _ { j k }$ end if end for end for end for (2） for $i = 1$ to $\pmb { n }$ par-do $x _ { i } = a _ { i , n + 1 } / a _ { i i }$ end for

End

注意此算法有可能多于一个处理器同时读取 $\alpha _ { i j } \setminus \alpha _ { j j }$ 和 $\alpha _ { j k }$ ,所以此PRAM应是 CREW的。

显然,算法的时间为 $O ( n )$ ，用了 $O ( n ^ { 2 } )$ 个处理器。

# 10.3.3 迭代求解的高斯-赛德尔法

基本原理 高斯-赛德尔求解线性方程组的方法,实际上是迭代(近似求解)法,不仅稠密线性系适用,而且稀疏线性系也适用。

在求解 $\mathbf { A } \mathbf { x } = \mathbf { b }$ 时,可以将系数矩阵 $\pmb { A }$ 分解为 $\pmb { A } = \pmb { E } + \pmb { D } + \pmb { F }$ ,其中 $\pmb { D } \cdot \pmb { E } \cdot \pmb { F }$ 均为 $\mathbf { \Omega } _ { n } \times \mathbf { \Omega } _ { n }$ 的矩阵,具体定义如下：

$$
d _ { i j } = { \left\{ \begin{array} { l l } { a _ { i j } ~ , ~ i = j } \\ { 0 ~ , ~ \operatorname { \circledast } { \mathbb { H } } } \end{array} \right. } e _ { i j } = { \left\{ \begin{array} { l l } { a _ { i j } ~ , ~ i > j } \\ { 0 ~ , ~ \operatorname { \circledast } { \mathbb { H } } } \end{array} \right. } f _ { i j } = { \left\{ \begin{array} { l l } { a _ { i j } ~ , ~ i < j } \\ { 0 ~ , ~ \operatorname { \circledast } { \mathbb { H } } } \end{array} \right. }
$$

这样， $A x = \left( D + E + F \right) x = b$ 可变换成 $\pmb { D x } = \pmb { b } - \pmb { E x } - \pmb { F x }$ 。如果给定初始解 ${ \pmb x } ( { \bf 0 } )$ ，则第 $k$ 次迭代可计算如下：

$$
\pmb { D } \pmb { x } \left( \pmb { k } \right) = \pmb { b } - \pmb { E } \pmb { x } \left( \pmb { k } \right) - \pmb { F } \pmb { x } \left( \pmb { k } - \pmb { 1 } \right)
$$

例如， $^ { n = 4 , k = 1 }$ 时，

$$
\alpha _ { 1 1 } x _ { 1 } ( 1 ) = b _ { 1 } - 0 - \big ( \alpha _ { 1 2 } x _ { 2 } ( 0 ) + \alpha _ { 1 3 } x _ { 3 } ( 0 ) + \alpha _ { 1 4 } x _ { 4 } ( 0 ) \big )
$$

$$
\alpha _ { 2 2 } x _ { 2 } ( 1 ) = b _ { 2 } - \left( \alpha _ { 2 1 } x _ { 1 } ( 1 ) - \left( \alpha _ { 2 3 } x _ { 3 } ( 0 ) + \alpha _ { 2 4 } x _ { 4 } ( 0 ) \right) \right.
$$

$$
\alpha _ { 3 3 } x _ { 3 } \big ( 1 \big ) = b _ { 3 } - \big ( \alpha _ { 3 1 } x _ { 1 } \big ( 1 \big ) + \alpha _ { 3 2 } x _ { 2 } \big ( 1 \big ) \big ) - \alpha _ { 3 4 } x _ { 4 } \big ( 0 \big )
$$

$$
\alpha _ { 4 4 } x _ { 4 } ( 1 ) = b _ { 4 } - \left( \alpha _ { 4 1 } x _ { 1 } ( 1 ) + \alpha _ { 4 2 } x _ { 2 } ( 1 ) + \alpha _ { 4 3 } x _ { 3 } ( 1 ) \right) - 0
$$

对于某一k和给定的误差允许值,如果下式成立，则认为迭代是收敛的：

$$
\operatorname* { m a x } _ { i = 1 } ^ { n } |  x _ { i } ( k + 1 ) - { x _ { i } } ( k ) | < \varepsilon
$$

(10.6）式能够加快顺序计算速度,因为当依次计算 ${ \pmb x } _ { 1 } , { \pmb x } _ { 2 }$ ,…时,第 $k$ 次迭代的

$x _ { i } ( k )$ 值,一部分可用上次迭代的值(相应于上三角部分),而一部分可用本次迭代的值(相应于下三角部分）。

SISD上高斯-赛德尔迭代法注意(10.6)式可以展开为如下形式：

$$
x _ { i } ( k ) = ( b _ { i } - \sum _ { j = 1 } ^ { i - 1 } a _ { i j } x _ { j } ( k ) - \sum _ { j = i + 1 } ^ { n } a _ { i j } x _ { j } ( k - 1 ) ) / a _ { i i } \quad , \quad i = 1 , \cdots , n
$$

按照(10.7)式可直接导出如下顺序算法 $1 0 . 7 _ { \circ }$

算法10.7 SISD上求解线性方程组高斯-赛德尔迭代算法

输入： $\mathbf { A } _ { n \times n } , \pmb { b } = [ b _ { 1 } , \cdots , b _ { n } ] ^ { \mathrm { T } }$ ，精度 $\varepsilon$

输出： ${ \pmb x } = [ { \pmb x } _ { 1 } , \cdots , { \pmb x } _ { n } ] ^ { \mathrm { T } }$

Begin

(1) for $i = 1$ to $\pmb { n }$ do

$$
x _ { i } = 0
$$

(2） ${ p / } = \varepsilon + 1$

(3）while $\pmb { \hat { p } } \mathbf { \mathcal { \gtrsim } } \varepsilon$ do (3.1) ${ \pmb \beta } = { \pmb 0 }$ (3.2) for $i = 1$ to $\pmb { n }$ do $\begin{array} { c } { { \left( \mathrm { i } \right) t = x _ { i } } } \\ { { \left( \mathrm { i i } \right) s = 0 } } \end{array}$ (ii)for $j = 1$ to $\pmb { n }$ do if $j \neq i$ then s=s+aixj end if $x _ { i } = ( b _ { i } - s ) / a _ { i i }$ if $| x _ { i } - t | > _ { \hat { P } }$ then $\mathbf { \nabla } _ { \pmb { \phi } } = | \mathbf { \nabla } _ { \mathbf { \mathcal { X } } _ { i } } - \mathbf { \nabla } _ { t } |$ endif end for end for

# end while

End

注意上述算法只有系数矩阵是对角占优的才适用。

并行化分析上述算法无法直接并行化,因为在第k次迭代时,对于j<i

（下三角部分）的 $x _ { i } ( k )$ 的计算必须等待 $x _ { i } ( k )$ 计算好,因而无法并行。有关它的并行化方法，在10.4节讨论稀疏线性方程组的求解时还要进一步讨论。

# 10.4稀疏线性方程组的求解

稀疏线性方程组系指系数矩阵中绝大多数元素均为零的方程组。之所以专门研究它，不仅仅是因为在科学和工程计算问题中会经常遇到它们,而且它们所涉及到的算法和数据结构也比稠密系统要复杂。

绝大多数科学和工程计算问题均代表了由数学模型所表示的一个物理系统。为了适合于计算机求解,连续物理系统的定义域必须离散化，其常用的方法就是将定义域网格化，这样在离散域上求解数学模型，就可在各格点上获得某些所要求的物理量。

通常离散物理域上每个格点的模拟计算，都是基于域上邻近格点的相互作用与影响。典型地,单格点的模拟就会产生一组线性方程。由于每一格点仅与其近邻有关，所以只有邻近格点的变量的系数是非零,而线性方程组的其余系数均为零，因而线性方程组就变成稀疏的了。

注意我们所考虑的稀疏矩阵，是指那些能够利用非零元素的位置与数量有效减少计算时间的稀疏矩阵。

# 10.4.1 稀疏矩阵的存储方式

通常我们用n×n的数组来存放n×n的稠密矩阵,但对稀疏矩阵而言，这种存储方式效率不高。研究有效的稀疏矩阵存储方式,不仅可节省存储单元，而且也可节省计算时间。但存储稀疏矩阵尚无一种通用的最佳的数据结构，不同的数据结构适合于不同的操作变换和不同的并行实现。以下我们仅研究几种最基本常用的稀疏矩阵存储方式。

坐标存储法(Coordinate Storage Scheme） 对于具有q个非零元素的稀疏矩阵,使用坐标存储法存储非零元素时，使用了三个q×1维的数组：值数组VAL和行列下标数组I和J。图10.3示出了6×6稀疏矩阵及其坐标存储法(行列下标编号从1开始，下同)。

缩行存储法(Compressed Row Storage Scheme） 对于具有q 个非零元素的稀疏矩阵，使用压缩稀疏行的办法存储非零元素时，也使用了三个数 组：一 个q×1维的值数组VAL,它按行序分成了n个段；一个q×1维的列下标数组J；一个n×1维的数组I,该数组中的元素指向各段中首元素在稀疏矩阵中的顺序号（只计算非零元素）。图10.4示出了图10.3中的稀疏矩阵使用缩行存储法时的 VAL、J和 $\mathrm { I } _ { \circ }$

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0004_pages_0211-0280/auto/images/9d82fa3c0de69ca157f68008e641f59092254053a53abd57f8d76192e1974fcb.jpg)  
图10.3 $6 \times 6$ 稀疏矩阵及其坐标存储法

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0004_pages_0211-0280/auto/images/a53ab289ab4c508b838649c6bdf64209353f8a6e70aef607b4e884bc1257f5cd.jpg)  
图10.4图10.3中稀疏矩阵的缩行存储法

对角存储法(Diagonal Storage Scheme） 对于具有 $\pmb { d }$ 条对角线的 $\mathbf { \mu } _ { n } \times \mathbf { \mu } _ { n }$ 的稀疏矩阵,使用对角存储法时,使用了两个数组：一个 ${ \pmb n } \times { \pmb d }$ 维的值数组VAL,它每一列存储了一条对角线;一个 $d \times 1$ 维的偏移数组(OFFSET),存储各对角线相对于主对角线偏移量。图10.5示出了一个稀疏矩阵及其对角存储方法。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0004_pages_0211-0280/auto/images/26d5047180d87e0f5026987a7d9bf1d3fa12e8d7edafe225ce3e614e90dc60c4.jpg)  
图10.5稀疏矩阵的对角存储法

按行存储法(Elpack-Itpack Storage Scheme）对于一个 $\textbf { \em n } \times \textbf { \em n }$ 的稀疏矩阵,假定任意行中最多非零元素数为m，则使用这种存储法时使用了两个数组：一个𝑛×m维的值数组VAL,它每一行包含了稀疏矩阵中相应行中的非零元素;一个𝑛×m 维的数组J,它存储了VAL中相应元素的列号,其中行末的-1是行结束符。图10.6示出了一个稀疏矩阵及其按行存储法。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0004_pages_0211-0280/auto/images/bc2b653a5b03a9ffc2999a57e9f102a59d9c94b7da103623ebd225e5cee005c9.jpg)  
图10.6稀疏矩阵的按行存储法

齿对角存储法(Jagged-Diagonal Storage Scheme） 对于具有 $\pmb q$ 个非零元素的稀疏矩阵，使用齿状对角线的形式存储非零元素时,首先将原矩阵按每行中非零元素之数目的降序重新排列之，然后辅之以三个数组：一个 $q \times 1$ 维的值数组VAL,它包含有若干段,每段存储一条齿状对角线；一个 $q \times 1$ 维的数组J,它存储VAL中相应元素的列号;一个 $m \times 1$ 维的数组I( $\mathbf { \nabla } m$ 是任意行中最多非零元素数),该数组之元素是指向各条齿状对角线中首元素依次在所有齿状对角线中的顺序号。图10.7示出了一个稀疏矩阵及其重新调整行序的稀疏矩阵以及它的齿对角存储法。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0004_pages_0211-0280/auto/images/f0759fa56ed51d934269673d5ccd5340ccac1af68ea5a33326912f3a0f464d71.jpg)  
图10.7稀疏矩阵的齿对角存储法：(a)原始稀疏矩阵； (b)行重排稀疏矩阵;(c)数组VAL、J和I

# 10.4.2雅可比迭代法

前面10.3.3节已经介绍了线性方程组的迭代求解法。对于求解大型、稀疏线性方程组,迭代法(Iterative Method)是一种最常使用的方法,与直接法相比，它具有方法简单,存储空间小(迭代法通常只对系数矩阵中的非零元素进行运

算)等优点，特别是在有限步内无法得到问题的解时，迭代法就可在有限的迭代步数后，停止运算而得到足够好的近似解。本节先介绍雅可比迭代法，它是一种最简单的线性方程组的迭代解法。

SISD上雅可比迭代法对于求解线性方程组 $\mathbf { A } { \boldsymbol { \mathbf { \mathit { x } } } } = \mathbf { \mathit { b } }$ ,未知向量 $_ { x }$ 的分量可写成如下形式：

$$
x _ { i } = \frac { 1 } { a _ { i i } } \bigg [ b _ { i } - \sum _ { j \neq i } a _ { i j } x _ { j } \bigg ]
$$

雅可比迭代原理是,使用第 $k - 1$ 步所计算的变量 $x _ { i } ( k - 1 )$ ,来计算第 $k$ 步的 $\vert x _ { i } \langle k \rangle$ 之值：

$$
x _ { i } ( k ) = \frac { 1 } { a _ { i i } } \Big ( b _ { i } - \sum _ { j \neq i } a _ { i j } x _ { j } \big ( k - 1 \big ) \Big )
$$

算法10.8给出了串行雅可比迭代算法,注意为了确保该算法总能收敛,要求系数矩阵 $\pmb { A }$ 是对角占优的,即 $\vert a _ { i i } \vert > \sum _ { j \neq i } \mid a _ { i j } \vert$ ， $1 { \leqslant } i { \leqslant } n _ { \leqslant }$

# 算法10.8SISD上求解线性方程组雅可比迭代算法

输入： $\mathbf { A } _ { n } \times \mathbf { \ b _ { n } } , \pmb { b } = [ b _ { 1 } , \cdots , b _ { n } ] ^ { \mathrm { T } } , \varepsilon$ 输出： $\pmb { x } = \{ x _ { 1 } , \cdots , x _ { n } \} ^ { \mathbb { T } }$

# Begin

(1） for $i = 1$ to $_ n$ do $\mathbf { \nabla } \times \mathbf { \nabla } x _ { i }$ 赋初值 $\yen 7$ $x _ { i } = b _ { i } / a _ { i i }$ end for   
(2) $\operatorname { d i f f } = \varepsilon$   
(3）while diff≥ε do (3.1) $\operatorname { d i f f } = 0$ (3.2) for $i = 1$ to $\pmb { n }$ do (i) $\mathrm { n e w } x _ { i } = b _ { i }$ (ii）for $j = 1$ to $\mathbf { n }$ do if $ { j } \neq  { i }$ then $\mathrm { n e w } x _ { i } = \mathrm { n e w } x _ { i } - \alpha _ { i j } x _ { j }$ end if endfor (ii) $\mathrm { n e w } x _ { i } = \mathrm { n e w } x _ { i } / a _ { i i }$ end for (3.3) for $i = 1$ to $_ n$ do

$$
{ \mathrm { d i f f } } = \operatorname* { m a x } \left\{ { \mathrm { d i f f } } , \mid x _ { i } - { \mathrm { n e w } } x _ { i } \mid \right\}
$$

# end for

# end while

End

算法10.8并行化分析雅可比算法很适合于并行化，因为每次迭代均使用上次迭代的值。假定处理器按行分配，即每个处理器负责矩阵的若干行和相应的 $^ b$ 分量，则在while循环时产生两次通信要求：在(3.2)步,每个处理器 $\mathbf { P } _ { i }$ 在计算自己的 $x _ { i } ( k )$ 时,必须用到上次计算出的 $x _ { j } ( k - 1 ) , j \neq i _ { \mathfrak { c } }$ ，为此每个处理器计算出所负责的变量后,必须将其播送给所有其它的处理器;在(3.3)步,每个处理器计算出局部差值diff后,必须从中选取最大者作为下一次迭代的判据,这种求最大值操作是在所有处理器之间的全局操作。

偏微分方程的差分解法试考虑拉普拉斯方程的第一边值问题：

$$
\begin{array} { l } { { \displaystyle { \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } } + { \frac { \partial ^ { 2 } u } { \partial y ^ { 2 } } } = 0 } } \\ { { \displaystyle u \mid _ { s } = \mu ( x , y ) } } \end{array}
$$

其中， $\mu ( x , y )$ 为有界区域 $D$ 的边界 $S$ 上的已知函数。为了求解此偏微分方程，我们可以用差商代替偏导数,得到相应的差分方程,通过解差分方程就可得到偏微分方程的近似解。

试考虑在平面 $( x , y )$ 上一个以S为边界的有界区域 $D$ 上定解问题。为了用差分法求解,可以分别作平行x轴和y轴的直线簇x;=id,y=jd（i,j=0,$1 , \cdots , n ; d$ 为步距),从而构成一个等间距正方网格,而直线的诸交点 $( x _ { i } , y _ { j } )$ 称为格点，记之为 $( i , j )$ 。当 $i , j = 1 , 2 , \cdots , n - 1$ 时的格点称为内格点,在 $S$ 上的格点称为边界格点。所有内格点上，函数 ${ \mathbf { } } u \left( x , y \right)$ 的偏导数可用差商代替：

$$
\frac { \partial u \left( x , y \right) } { \partial x } { \approx } \frac { 1 } { d } \left[ u \left( x _ { i } + d , y _ { j } \right) - u \left( x _ { i } , y _ { j } \right) \right]
$$

$$
\frac { \partial u \left( x , y \right) } { \partial y } { \approx } \frac { 1 } { d } \left[ u \left( x _ { i } , y _ { j } + d \right) - u \left( x _ { i } , y _ { j } \right) \right]
$$

$$
\frac { \partial ^ { 2 } u \left( \boldsymbol { x } , \boldsymbol { y } \right) } { \partial x ^ { 2 } } \approx \frac { 1 } { d ^ { 2 } } \big [ u \left( \boldsymbol { x } _ { i } + d , \boldsymbol { y } _ { j } \right) - 2 u \left( \boldsymbol { x } _ { i } , \boldsymbol { y } _ { j } \right) + u \left( \boldsymbol { x } _ { i } - d , \boldsymbol { y } _ { j } \right) \big ]
$$

$$
\frac { \partial ^ { 2 } u \left( \boldsymbol { x } , \boldsymbol { y } \right) } { \partial \boldsymbol { y } ^ { 2 } } \approx \frac { 1 } { d ^ { 2 } } \big [ u \left( x _ { i } , \boldsymbol { y } _ { j } + d \right) - 2 u \left( x _ { i } , \boldsymbol { y } _ { j } \right) + u \left( x _ { i } , \boldsymbol { y } _ { j } - d \right) \big ]
$$

(10.11)式代人(10.10)式则有：

$$
u \left( x _ { i } , y _ { j } \right) = \frac { 1 } { 4 } \big [ u \left( x _ { i } + d , y _ { j } \right) + u \left( x _ { i } - d , y _ { j } \right) + u \left( x _ { i } , y _ { j } + d \right) + \big ]
$$

$$
u ( x _ { i } , y _ { j } - d ) ]
$$

若格点 $( i , j )$ 处的函数值 $u \left( x _ { i } , y _ { j } \right)$ 记之为 $\boldsymbol { u } _ { i j }$ ,且取 $d = 1$ ,则(10.12)式可简化为：

$$
u _ { i j } = \frac { 1 } { 4 } \left[ u _ { i + 1 , j } + u _ { i - 1 , j } + u _ { i , j + 1 } + u _ { i , j - 1 } \right]
$$

它就是有名的五点格式,即任一格点 $( \mathbf { \omega } _ { i } , \mathbf { \omega } _ { j } )$ 上 $\boldsymbol { u } _ { i j }$ 的值等于周围相邻四格点上解·的值的算术平均。

雅可比算法用于求解稀疏线性方程组当用算法10.8来求解(10.13)式所示的方程组时,效率很低,因为它相应的系数矩阵是稀疏的,每行只有五个非零元素,为此我们设计如下算法10.9来求解它。照例,使用第 $k - 1$ 步所计算的变量来计算第 $\pmb { k }$ 步的变量。

# 算法10.9 SISD上求解拉普拉斯方程雅可比迭代算法

输入：格点数 $\pmb { n }$ ,精度 $\varepsilon$ 输出： ：xi,j

Begin

(1）for $i = 1$ to $\pmb { n }$ do $\big / \ast$ 边界条件 $\bigstar$ / $\begin{array} { r l } & { x _ { 0 , i } = \mathrm { n o r t h } _ { i } } \\ & { x _ { n + 1 } , i = \mathrm { s o u t h } _ { i } } \\ & { x _ { i , 0 } = \mathrm { w e s t } _ { i } } \\ & { x _ { i , n + 1 } = \mathrm { e a s t } _ { i } } \end{array}$ end for

(2) for $i = 1$ to $\pmb { n }$ do $\big / \ast$ 赋初值 $\yen 7$ for $j = 1$ to $\pmb { n }$ do $x _ { i j } = c$ end for end for   
(3） $\operatorname { d i f f } = \varepsilon$   
（4）while diff≥ε do (4.1) $\operatorname { d i f f } = 0$ (4.2) for $i = 1$ to $\pmb { n }$ do for $j = 1$ to $_ { \pmb { n } }$ do $\mathrm { n e w } x _ { i j } = \frac { 1 } { 4 } ( x _ { i - 1 , j } + x _ { i + 1 , j } + x _ { i , j - 1 } + x _ { i , j + 1 } )$ end for

# end for

$$
\begin{array} { r l } & { \mathrm { d i f f } = \operatorname* { m a x } \{ \mathrm { d i f f } , \vert \operatorname { n e w } x _ { i j } - x _ { i j } \vert \} } \\ & { x _ { i j } = \mathrm { n e w } x _ { i j } } \end{array}
$$

# end for

# 'end for

end while

End

算法10.9并行化分析该算法是基于雅可比迭代原理,所有格点之值可同时更新。但在并行更新过程中会产生通信要求：在处理器按行分配时，如图10.8(a)所示，每个处理器负责 $\frac { n } { \pmb { \mathscr { p } } } \times \pmb { \mathscr { n } }$ 个元素，算法(4.2)步每次迭代计算 $\mathtt { n e w } x _ { i j }$ 时，处理器中的阴影区要分别传送 $\pmb { n }$ 个元素给对方的处理器和同时接收来自对方的 $\pmb { n }$ 个元素，令 $\lambda$ 为延迟时间， $\beta$ 为传送每个单值的时间，则每次迭代的通信时间为 $4 ( \lambda + n \beta )$ ;在处理器按块分配时,如图10.8(b)所示,每个处理器负责×个元素，算法执行(4.2)步计算 newxij时,处理器中的阴影区的通信时间为 $8 \left( \lambda + \frac { n } { \sqrt { \lambda } } \beta \right)$ 。同样,不管哪种处理器分配,算法(4.3)步计算全局diff时也会产生通信要求,为了减少此通信时间，可每迭代 $\pmb { k }$ 次才计算一次 diff 的全局值，其中 $k$ 值的大小与计算机的结构和求解问题类型有关。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0004_pages_0211-0280/auto/images/2373f7e9a2e80b48443609116d5e29bae21acb2d4024daf8f27d5d11702f2d5a.jpg)  
图10.8处理器的两种划分(a)按行划分 $( \pmb { \phi } = 4 )$ ；(b)按块划分（ $\bf \Pi \cdot \langle \delta 1 6 \rangle$

# 10.4.3 高斯-赛德尔迭代法

基本原理曾在第10.3.3节介绍了求解稠密线性方程组的高斯-赛德尔迭

代法。本节着重介绍此法用于求解稀疏线性方程组。两者的计算原理是一样的,即在迭代时用最新算出的部分 $x _ { i }$ 值代替旧的 $x _ { i }$ 值参于迭代。不妨将(10.7)式改写成如下等效形式：

$$
x _ { i } ( k ) = \frac { 1 } { a _ { i i } } [ b _ { i } - \ \sum _ { j < i } a _ { i j } x _ { j } ( k ) - \ \sum _ { j > i } a _ { i j } x _ { j } ( k - 1 ) ]
$$

按此,在第 $k$ 次迭代时,只有当 $x _ { i - 1 } ( k )$ 计算完成后才能开始计算 $x _ { i } ( k )$ ,这意味着计算的顺序性。

并行化讨论诚然,按照(10.14)式迭代计算时会加快收敛速度,但已如上述，第 $k$ 次迭代时，对于系数矩阵的下三角部分， $x _ { j } ( k )$ 的计算必须等待所有 $x _ { i } ( k )$ 计算完毕时才能进行。这种计算的顺序性限制了并行化的实现,当系数矩阵为稠密阵时的确如此。然而,对于稀疏矩阵,x;(k)的计算不一定要等到x(k),…，$x _ { i - 1 } ( k )$ 都计算完毕才行。因为稀疏矩阵大多数元素均为零，如果 $a _ { i j } = 0$ ,那么(10.14)左边 $x _ { i } ( k )$ 不依赖于 $x _ { j } ( k )$ ,所以只要计算出 $j < i$ 且 $a _ { i j } \neq 0$ 的 $x _ { j } ( k )$ ，$x _ { i } ( k )$ 便可计算。由此可见,高斯-赛德尔迭代法的并行化程度与系数矩阵 $\pmb { A }$ 下三角部分中非零元素的分布状况有关。试考虑(10.13)式所示的五点差分格式的迭代计算问题,此时所有格点值的更新可按下述公式计算之：

$$
x _ { i , j } ( k ) = \frac { 1 } { 4 } \{ x _ { i - 1 , j } ( k ) + x _ { i , j - 1 } ( k ) + x _ { i + 1 , j } ( k - 1 ) + x _ { i , j + 1 } ( k - 1 ) \}
$$

对上式迭代计算进行数据相关分析。图10.9(a)示出了 $4 \times 4$ 格点迭代计算的数据相关性。由图可知， $x _ { 1 , 1 }$ 之新值必须先计算;一旦算出 $x _ { 1 , 1 }$ ，就可并行计算x1,2与x2,1;使用新计算的x1,2和x2,1,就可同时计算x1,3,x2,2和x3,1,与此同时也可计算𝑥1,i下一次迭代之值;同样,下一步就并行计算x1,4,x2,3,x3,2，$x _ { 4 , 1 } , x _ { 1 , 2 }$ 和 $x _ { 2 , 1 }$ 。按此,可以将变量分为两组,每一组中的变量可以同时更新。一种方法就是有名的红-黑着色法(Red-Black Coloring)。如图10.9(b)所示，在每一行和每一列,将格点交替地着成红色,其余的着成黑色,相同颜色的格点可同时更新。而格点的更新是以波前(Wavefront)形式从左上角向右下角逐步推进，并行化程度是不高的。事实上，使用红-黑法对格点进行着色后，所有红点的邻节点仅为黑色，同样所有黑点的邻节点仅为红色。这样，高斯-赛德尔迭代法第$k$ 次迭代时可分为两步：

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0004_pages_0211-0280/auto/images/046c7941dde0320af782cdc39b7ea4d016f57a328f0764a7a4049f2607d1e59b.jpg)  
图10.9高斯-赛德尔法并行化分析(a)数据相关分析；(b)红-黑着色法

$\textcircled{1}$ 第1步,同时计算所有的红点：

$$
x _ { i , j } ( k ) = \frac { 1 } { 4 } \{ x _ { i - 1 , j } ( k - 1 ) + x _ { i , j - 1 } ( k - 1 ) + x _ { i + 1 , j } ( k - 1 ) + x _ { i , j + 1 } ( k - 1 ) \}
$$

$\textcircled{2}$ 第2步，同时计算所有的黑点：

$$
x _ { i , j } ( k ) = \frac { 1 } { 4 } \{ _ { x _ { i - 1 , j } } ( k ) + x _ { i , j - 1 } ( k ) + x _ { i + 1 , j } ( k ) + x _ { i , j + 1 } ( k ) \}
$$

而第2步计算黑点时所用到的红点值均已在第1步计算出。

# 10.4.4超松弛迭代法

雅可比超松弛法(JacobiOverRelaxation）雅可比超松弛法是雅可比迭代法的变体,它组合旧 $\pmb { x _ { i } }$ 之值与用雅可比标准算法所算出的新 $\pmb { x _ { i } }$ 之值,来计算新的$\pmb { x _ { i } }$ 之值,其更新计算遵循如下方程：

$$
x _ { i } \left( k \right) = \left( 1 - \gamma \right) x _ { i } \left( k - 1 \right) + \frac { \gamma } { \alpha _ { i i } } { \left[ b _ { i } - \mathrm { ~ \sum _ { j \ne i } ~ } a _ { i j } x _ { j } \left( k - 1 \right) \right] }
$$

其中 $\gamma ( 0 { \leqslant } \gamma { \leqslant } 1 )$ 为松弛因子,当 $\gamma = 1$ 时上式就是标准的雅可比迭代公式(10.9)。  
适当选择 $\gamma$ 之值可加快收敛。

逐次超松弛法 SOR(Successive Over Relaxation） 逐次超松弛法是高斯-赛德尔迭代法的变体,它组合旧 $\pmb { x _ { i } }$ 之值与用高斯-赛德尔法所算出的新 $\dot { \boldsymbol { x } } _ { i }$ 之值，来计算新的 $\pmb { x _ { i } }$ 之值,其更新计算遵循如下方程：

$$
x _ { i } ( k ) = ( 1 - \gamma ) x _ { i } ( k - 1 ) + \frac { \gamma } { \alpha _ { i i } } [ b _ { i } - \ \sum _ { j < i } \alpha _ { i j } x _ { j } ( k ) - \ \sum _ { j > i } \alpha _ { i j } x _ { j } ( k - 1 ) ]
$$

其中， $\gamma ( 0 \leqslant \gamma \leqslant 1 )$ 为松弛因子。当 $\gamma = 1$ 时上式就是高斯-赛德尔迭代公式(10.14)。适当选择 $\gamma$ 之值可加快收敛。

# 10.4.5多重网格法

基本原理 多重网格(Multigrid)法是一类求解偏微分方程数值解的迭代方法,产生于两个事实：其一，迭代方法在粗网格上比细网格上收敛更快;其二，如果变量初始估计值合适，则迭代算法收敛也快。所以多重网格法就是基于上述事实,用前一组网格格点上的值去计算后一组网格格点上的值。其中,在细网格上的迭代可得到较准确的解，在粗网格上的迭代能加快收敛速度。适当地组合粗、细网格上的迭代就可得到多重网格迭代算法。

算法描述为了简化讨论,仅考虑二维网孔上的多重网格法。约定： $G ^ { 0 }$ 是$\mathbf { \Omega } _ { n } \times \mathbf { \Omega } _ { n }$ 维（ $\pmb { n }$ 是2的方幂)的最细网格, $G ^ { i }$ 表示较粗的网格 $( 1 { \leqslant } i < \log n )$ ， $G ^ { k }$ 中的格点 $( i , j )$ 对应着变元 $x _ { i j } ^ { k }$ 。例如,对于 $n = 1 6$ ，则 $G ^ { 0 }$ 为 $1 6 \times 1 6$ 的网格(最细网格）, $G ^ { 1 }$ 为 ${ \bf 8 } \times { \bf 8 }$ 的网格, $G ^ { 2 }$ 为 $4 \times 4$ 的网格, $G ^ { 3 }$ 为 $2 \times 2$ 的网格（最粗的网格）。

在多重网格算法中,有三类运算：

$\textcircled{1}$ 松弛(Relaxation):计算 $G ^ { k }$ 中所有 $x _ { i j } ^ { k }$ 之值,这可用雅可比迭代法、高斯-赛德尔迭代法、雅可比超松弛法、逐次超松弛法或其它迭代方法。

$\textcircled{2}$ 内插(Interpolation):用较粗网格 $G ^ { k }$ 中变量 $x _ { i , j } ^ { k }$ 之值,去计算较细网格$G ^ { k - 1 }$ 中变量 $x _ { i , j } ^ { k - 1 }$ 之值。一种简单内插法是以与 $x _ { i , j } ^ { k - 1 }$ 最近的 $G ^ { k }$ 中变量之值取平均值作为 $x _ { i , j } ^ { k - 1 }$ 之值。例如， $x _ { 3 , 5 } ^ { 0 } = \frac { 1 } { 4 } \big ( x _ { 2 , 4 } ^ { 1 } + x _ { 2 , 6 } ^ { 1 } + x _ { 4 , 4 } ^ { 1 } + x _ { 4 , 6 } ^ { 1 } \big ) _ { \circ }$

$\textcircled{3}$ 投射(Projection):用较细网格 $G ^ { k - 1 }$ 中变量 $x _ { i , j } ^ { k - 1 }$ 之值,去计算较粗网格$G ^ { k }$ 中变量 $x _ { i } ^ { k }$ j之值。一种投射法是内射法,它取与细网格点相重合的粗网格点之值作为粗网格点之值,即 $x _ { i , j } ^ { k } = x _ { i , j } ^ { k - 1 }$ 。例如， $x _ { 4 , 4 } ^ { 2 } = x _ { 4 , 4 } ^ { 1 }$ 。

使用多重网格法时,由于在粗网格上未知量少,从而问题计算规模比细网格上小,因此粗网格上问题的求解比细网格上容易。如果首先近似地求出粗网格上的解,然后将其插值到细网格上作为细网格迭代的初值,则细网格上的松弛收敛将会加快。这种将粗、细网格优点相互结合的方法,使多重网格法的应用非常广泛。

并行化通信分析多重网格算法中，松弛、内插和投射均会产生通信要求。其中,松弛计算的通信要求已在10.4.2节讨论过;而内射法(Injection)不产生通信要求;在简单内插时,细网格点之值由其近邻的诸粗网格点之值决定之。在此情况下,假定将最细网格 $G ^ { 0 }$ 指派给 $\mathbf { \Omega } _ { n } \times \mathbf { \Omega } _ { n }$ 的二维处理器阵列上,那么在较粗网格 $G ^ { 1 } , G ^ { 2 } , \cdots , G ^ { \log n - 1 }$ 上需要相互通信的处理器是不相邻的,其距离在 $G ^ { 1 }$ 上为2,在 $G ^ { 2 }$ 上为4,如此等等。

当把网格 $G ^ { 0 } , G ^ { 1 } , \cdots , G ^ { \log n - 1 }$ 映射到超立方上时,情况比映射到二维网孔上复杂。这时可以使用葛莱码把二维网孔映射到超立方上,但这只能确保 $G ^ { 0 }$ 中相邻的格点映射到超立方的相邻顶点上,而对较粗网格不能都这样。在最坏情况下， $\mathbf { \Omega } _ { n } \times \mathbf { \Omega } _ { n }$ 的网格中的某一点会有 $4 \log n - 2$ 个邻居,而点数为 $n ^ { 2 }$ 的超立方仅有 $2 \log { n }$ 个邻居。例如图10.10所示的 ${ \bf 8 \times 8 }$ 的网格中,点18有10个邻居，但64个顶点的超立方任一点都只有6个邻居。所以网格不能直接嵌入超立方中。但可以使G1,,Glg"中的邻点在超立方上相离为2。为此可将处理器编号分为两部分，一部分相应于行，另一部分相应于列;然后使用葛莱码将相邻的行和列元素映射到超立方相邻的顶点上。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0004_pages_0211-0280/auto/images/df0018ccaea7bbe63116e30d761de68c97ed7fef08f346453e32a100d528f647.jpg)  
图10.10二维多重网格映射到超立方上

# 10.4.6共轭梯度法

共轭梯度(Conjugate Gradient)法,也叫共轭斜量法。从理论上讲它是属于直接法,但在实际计算过程中,由于不可避免地会出现舍人误差,所以常作为迭代法使用。该方法的最大特点是，当方程组的阶数很高时，往往只要经过比阶数小得多的迭代次数，就能得到满足精度要求的近似解。

基本思想共轭梯度法是属于最小化类的迭代方法。为了求解 $\mathbf { A } \pmb { x } = \pmb { b }$ 这样的一次函数,可以先构造一个二次函数 $q ( x )$ ,然后利用最小化原理对其求导$\partial q ( x ) / \partial x$ ,再令其为零。如果 $\partial q ( x ) / \partial x = A x - b = 0$ ,那么就可达到求解 $\mathbf { A } \mathbf { x }$ $- \ b = 0$ 的目的。所以关键的问题是如何构造一个所要求的二次函数。

构造二次函数 ${ \pmb q } ( { \pmb x } )$ 先定义一个二次齐次函数 $f ( x )$ ,再定义一个一次线性函数 $g ( x )$ ,将两者合成为 $q ( x )$ 。

$\textcircled{1}$ 定义二次齐次函数：

$$
\begin{array} { r } { f ( x _ { 1 } , x _ { 2 } , \cdots , x _ { n } ) = a _ { 1 1 } x _ { 1 } ^ { 2 } + a _ { 2 2 } x _ { 2 } ^ { 2 } + \cdots + a _ { n n } x _ { n } ^ { 2 } + \qquad } \\ { 2 a _ { 1 2 } x _ { 1 } x _ { 2 } + 2 a _ { 1 3 } x _ { 1 } x _ { 3 } + \cdots + 2 a _ { n - 1 , n } x _ { n - 1 } x _ { n } } \end{array}
$$

如果 $a _ { i j } = a _ { j i }$ ,则上式可写成如下形式：

$$
\begin{array} { r } { f ( x _ { 1 } , x _ { 2 } , \cdots , x _ { n } ) = \alpha _ { 1 1 } x _ { 1 } ^ { 2 } + a _ { 1 2 } x _ { 1 } x _ { 2 } + \cdots + a _ { 1 n } x _ { 1 } x _ { n } \ + } \\ { \qquad \quad \alpha _ { 2 1 } x _ { 2 } x _ { 1 } + \alpha _ { 2 2 } x _ { 2 } ^ { 2 } + \cdots + a _ { 2 n } x _ { 2 } x _ { n } \ + } \end{array}
$$

$$
\alpha _ { n 1 } x _ { n } x _ { 1 } + \alpha _ { n 2 } x _ { n } x _ { 2 } + \cdots + \alpha _ { n n } x _ { n } ^ { 2 }
$$

$$
x _ { n } ( a _ { n 1 } x _ { 1 } + a _ { n 2 } x _ { 2 } + \cdots + a _ { n n } x _ { n }
$$

$$
\mathbf { \Sigma } = ( \mathbf { \Sigma } _ { X _ { 1 } , X _ { 2 } } , \cdots , \mathbf { \Sigma } _ { X _ { n } } ) \left( \begin{array} { l l l l } { a _ { 1 1 } } & { a _ { 1 2 } } & { \cdots } & { a _ { 1 n } } \\ { a _ { 2 1 } } & { a _ { 2 2 } } & { \cdots } & { a _ { 2 n } } \\ { a _ { \mathbf { \Sigma } } } & { \vdots } & & \\ { a _ { n 1 } } & { a _ { n 2 } } & { \cdots } & { a _ { n n } } \end{array} \right) \left( \begin{array} { l } { x _ { 1 } } \\ { x _ { 2 } } \\ { \vdots } \\ { x _ { n } } \end{array} \right) = \mathbf { x } ^ { \mathrm { T } } A \mathbf { x }
$$

$\textcircled{2}$ 定义一次线性函数：

$$
\begin{array} { c } { g ( x _ { 1 } , x _ { 2 } , \cdots , x _ { n } ) = x _ { 1 } b _ { 1 } + x _ { 2 } b _ { 2 } + \cdots + x _ { n } b _ { n } } \\ { \qquad } \\ { = ( x _ { 1 } , x _ { 2 } , \cdots , x _ { n } ) \left( \begin{array} { l } { b _ { 1 } } \\ { b _ { 2 } } \\ { \vdots } \\ { b _ { n } } \end{array} \right) = { \pmb x } ^ { \mathrm { T } } { \pmb b } } \end{array}
$$

$\textcircled{3}$ 合成 $f ( x )$ 与 ${ \pmb g } ( { \pmb x } )$ ：

$$
q ( x ) = \frac { 1 } { 2 } \pmb { x } ^ { \mathrm { T } } \pmb { A } \pmb { x } - \pmb { x } ^ { \mathrm { T } } \pmb { b }
$$

求二次函数 ${ \pmb q } ( { \pmb x } )$ 的最小值为此要对 $q ( x )$ 求偏导数，即 $\partial q ( x ) / \partial x = \partial q$ $\left( x \right) / \partial x _ { 1 } + \partial q \left( x \right) / \partial x _ { 2 } + \cdots + \partial q \left( x \right) / \partial x _ { n }$ ,其中，

$$
{ \begin{array} { c } { { \frac { \partial q \left( x \right) } { \partial x _ { 1 } } } = { \frac { 1 } { 2 } } \left( 2 a _ { 1 1 } x _ { 1 } + 2 a _ { 1 2 } x _ { 2 } + 2 a _ { 1 3 } x _ { 3 } + \cdots + 2 a _ { 1 \pi } x _ { n } \right) - b _ { 1 } } \\ { { \frac { \partial q \left( x \right) } { \partial x _ { 2 } } } = { \frac { 1 } { 2 } } \left( 2 a _ { 2 1 } x _ { 1 } + 2 a _ { 2 2 } x _ { 2 } + 2 a _ { 2 3 } x _ { 3 } + \cdots + 2 a _ { 2 n } x _ { n } \right) - b _ { 2 } } \\ { \vdots } \\ { { \frac { \partial q \left( x \right) } { \partial x _ { n } } } = { \frac { 1 } { 2 } } \left( 2 a _ { n 1 } x _ { 1 } + 2 a _ { n 2 } x _ { 2 } + 2 a _ { n 3 } x _ { 3 } + \cdots + 2 a _ { n n } x _ { n } \right) - b _ { n } } \end{array} }
$$

所以，

$$
{ \frac { \partial q \left( { \boldsymbol { x } } \right) } { \partial { \boldsymbol { x } } } } = { \left( \begin{array} { l l l l l } { a _ { 1 1 } } & { a _ { 1 2 } } & { a _ { 1 3 } } & { \cdots } & { a _ { 1 n } } \\ { a _ { 2 1 } } & { a _ { 2 2 } } & { a _ { 2 3 } } & { \cdots } & { a _ { 2 n } } \\ & & & & { \vdots } \\ { a _ { n 1 } } & { a _ { n 2 } } & { a _ { n 3 } } & { \cdots } & { a _ { n n } } \end{array} \right) } { \left( \begin{array} { l } { x _ { 1 } } \\ { x _ { 2 } } \\ { \vdots } \\ { x _ { n } } \end{array} \right) } - { \left( \begin{array} { l } { b _ { 1 } } \\ { b _ { 2 } } \\ { \vdots } \\ { b _ { n } } \end{array} \right) } = \mathbf { A } \mathbf { x } - \mathbf { b }
$$

因此,所构造的二次函数 $q \left( x \right)$ ,求导后令其为零,正是要求解的线性方程组 $\mathbf { A } { \boldsymbol { x } } - \mathbf { b } = 0$ 。

共轭梯度法 ${ \pmb { \alpha } } ( { \pmb { k } } )$ 与 $\alpha ( k )$ 的求取用共轭梯度法求解 $\mathbf { A } { \boldsymbol { \mathbf { \mathit { x } } } } - \mathbf { \boldsymbol { \mathbf { b } } } = \mathbf { 0 }$ 的迭代公式如下：

$$
{ \pmb x } \left( \ b k \right) = { \pmb x } \left( \ b k - 1 \right) + { \pmb \alpha } \left( \ b k \right) { \pmb d } \left( \ b k \right)
$$

新向量 ${ \pmb x } ( k )$ 的值由老向量 $x \left( k - 1 \right)$ 、迭代步长 ${ \pmb { \alpha } } ( { \pmb { k } } )$ 和方向向量 $\pmb { d } ( k )$ 决定之，此时 $x ( k )$ 至多迭代 $_ n$ 次就可收敛。

$\textcircled{1}$ 求 ${ \pmb { \alpha } } ( { \pmb { k } } )$ ：对于给定的 ${ \pmb x } \left( { \pmb k } - 1 \right)$ 和 ${ \pmb d } \left( \pmb { k } \right) , { \pmb \alpha } \left( \pmb { k } \right)$ 的选取应使所构造的二次函数 $q ( x )$ 取最小值。由 $\frac { \partial q \left( \boldsymbol { x } \right) } { \partial \boldsymbol { x } } = \boldsymbol { A } \boldsymbol { x } \left( \boldsymbol { k } \right) - \boldsymbol { b } = \boldsymbol { 0 }$ 和 $\begin{array} { r } { \pmb { A } \pmb { x } \left( \pmb { k } \right) - \pmb { b } = \pmb { A } \left[ \pmb { x } \left( \pmb { k } - 1 \right) + \right. } \end{array}$ ${ \pmb { a } } \left( \beta \right) { \pmb { d } } \left( \beta \right) \} - { \pmb { b } } = 0$ ，可求出 ${ \pmb { \alpha } } ( k )$ 为：

$$
\pmb { \alpha } ( k ) = \frac { \pmb { b } - \pmb { A } \pmb { x } ( \pmb { k } - 1 ) } { \pmb { A } \pmb { d } ( \pmb { k } ) }
$$

令 ${ \pmb r } ( k )$ 为第 $k$ 次迭代的残向量：

$$
r ( k ) = A x ( k - 1 ) - b
$$

(10.22)代入(10.21）,则有

$$
\pmb { \alpha } ( k ) = - \frac { \pmb { r } ( k ) } { \pmb { A } \pmb { d } ( k ) } = - \frac { \pmb { d } ^ { \operatorname { T } } ( k ) \pmb { r } ( k ) } { \pmb { d } ^ { \operatorname { T } } ( k ) \pmb { A } \pmb { d } ( k ) }
$$

可见,每次迭代时唯一的矩阵－向量乘就是 $\pmb { A } \pmb { d } ( \pmb { k } )$ 。

$\textcircled{2}$ 求 $\pmb { d } ( \pmb { k } )$ ：求 $\pmb { d } ( \pmb { k } )$ 时,应使函数 $q ( x )$ 在 $\pmb { x _ { i } }$ 点最快地下降到 $x _ { i + 1 }$ ,而函数$q ( x )$ 在 $\boldsymbol { x } = \boldsymbol { x } _ { i }$ 点的变化率最快的方向就是 $q ( x )$ 在 $\pmb { x _ { i } }$ 处的梯度，即

$$
{ \mathrm { g r a d } } \ q \ { \Biggl | } _ { { \boldsymbol { x } } _ { i } } \ = \left( { \frac { \partial q } { \partial x _ { 1 } } } , { \frac { \partial q } { \partial x _ { 2 } } } , \cdots , { \frac { \partial q } { \partial x _ { n } } } \right) ^ { \mathrm { T } } { \Biggl | } _ { { \boldsymbol { x } } _ { i } }
$$

所以迭代时取梯度方向作为 $\pmb { d } _ { i }$ 。

可以证明,如果 $\pmb { A }$ 是对称正定的,且 $d _ { 1 } , d _ { 2 } , \cdots , d _ { n }$ 是相对于 $\pmb { A }$ 共轭的（即${ { d _ { i } } ^ { \mathrm { T } } } A { { d _ { j } } } = 0 , 1 { \leqslant } i , j { \leqslant } n , i { \neq } j )$ ，则 ${ \pmb x } \left( \ b k \right) = { \pmb x } \left( \ b k - 1 \right) + { \pmb \alpha } \left( \ b k \right) { \pmb d } \left( \ b k \right)$ 最多迭代 $_ n$ 次就可收敛到 $\mathbf { A } \mathbf { x } = \mathbf { \nabla } \delta$ 的解。

因此,从一组共轭矩阵 $\pmb { A }$ 的方向向量,作为迭代方向求解 $\mathbf { A } \mathbf { x } = \mathbf { b }$ 的方法称之为共轭梯度法。在此法中，一组共轭A的方向向量d(k)可选取如下：

$$
d \left( k \right) = - r \left( k \right) + \frac { r ^ { \operatorname { T } } ( k ) r \left( k \right) } { r ^ { \operatorname { T } } ( k - 1 ) r \left( k - 1 \right) } d \left( k - 1 \right)
$$

其中 $r ^ { \mathrm { T } } ( k ) r ( k )$ 表示残向量转置与残向量之内积。

共轭梯度算法步骤用共轭梯度法求解 $\mathbf { A } { \boldsymbol { \mathbf { \mathit { x } } } } - \mathbf { \boldsymbol { \mathit { b } } } = \mathbf { 0 }$ 的步骤如下：

$\textcircled{1}$ 初始化： ${ \pmb x } \left( 0 \right) = 0 , { \pmb d } \left( 0 \right) = 0 , { \pmb r } \left( 0 \right) = { \bf - \kappa \pmb \nu } _ { 0 }$ $\textcircled{2}$ 在第 $k$ 次迭代时,计算 ${ \pmb x } ( k )$ 分为四步：第1步：计算残向量(按照(10.22)式)：

$$
r ( k ) = A x ( k - 1 ) - b
$$

第2步：计算方向向量(按照(10.24)式)：

$$
\pmb { d } \left( k \right) = - r \left( k \right) + \frac { \pmb { r } ^ { \operatorname { T } } ( k ) \pmb { r } ( k ) } { \pmb { r } ^ { \operatorname { T } } ( k - 1 ) \pmb { r } ( k - 1 ) } \pmb { d } \left( k - 1 \right)
$$

第3步：计算步长(按照(10.23)式)：

$$
\pmb { \alpha } ( k ) = - \frac { \pmb { d } ^ { \operatorname { T } } ( k ) \pmb { r } ( k ) } { \pmb { d } ^ { \operatorname { T } } ( k ) \pmb { A } \pmb { d } ( k ) }
$$

第4步：计算新的近似变量(按照(10.20)式)：

$$
{ \pmb x } \big ( \pmb { k } \big ) = { \pmb x } \big ( \pmb { k } - 1 \big ) + { \pmb \alpha } \big ( \pmb { k } \big ) { \pmb d } \big ( \pmb { k } \big )
$$

SISD上共轭梯度算法用共轭梯度法求解 $\mathbf { A } \mathbf { x } = \mathbf { b }$ 的串行算法如算法10.10。其中,denom1,denom2,num1,num2,tempvect $\left[ 1 \colon n \right]$ 为临时变量,主算法调用两个过程 INNER.PRODUCT()和 MATRIX-VECTOR.PRODUCT（）。

算法10.10 SISD上求解 $\mathbf { A } \mathbf { \boldsymbol { x } } = \mathbf { \boldsymbol { b } }$ 共轭梯度算法

输入： $\mathbf { A } _ { n \times n } , \pmb { b } = [ b _ { 1 } , \cdots , b _ { n } ] ^ { \mathrm { T } } , \varepsilon$ 输出： $\pmb { x } = \big [ \pmb { x } _ { 1 } , \cdots , \pmb { x } _ { n } \big ] ^ { \mathrm { T } }$

Begin

(1） for $i = 1$ to $\pmb { n }$ do $\big / \ast$ 初始化 $\yen 7$

$$
\begin{array} { l } { { d _ { i } = 0 } } \\ { { \ } } \\ { { x _ { i } = 0 } } \\ { { r _ { i } = { \ - \ b _ { i } } } } \end{array}
$$

end for

$$
r _ { 1 : n } = M A T R I X { \cdot } V E C T O R . P R O D U C T ( a _ { 1 : n , 1 : n , x _ { 1 : n } } )
$$

$$
r _ { i } = r _ { i } - b _ { i }
$$

# end for

$$
\mathrm { n u m 1 } { = } \mathrm { I N N E R . P R O D U C T } ( r _ { 1 : n } , r _ { 1 : n } )
$$

$$
d _ { i } = - r _ { i } + \frac { \mathrm { n u m l } } { \mathrm { d e n o m l } } d _ { i }
$$

# end for

$$
{ \mathrm { n u m } } 2 = { \mathrm { I N N E R . P R O D U C T } } ( d _ { 1 : n } , r _ { 1 : n } ) \quad / *
$$

$$
d _ { 1 : n } )
$$

$$
\mathtt { d e n o m 2 } = \mathtt { I N N E R . P R O D U C T } ( d _ { 1 : n } , \mathrm { t e m p v e c t } _ { 1 , n } )
$$

(2.11） for $i = 1$ to $\pmb { n }$ do $\big / \ast$ 修正 $x _ { i } \ast { \mathrm { ~ } } /$

$$
x _ { i } = x _ { i } + \alpha d _ { i }
$$

# end for end for

End   
INNER.PRODUCT ${ \bf \Phi } ( a _ { 1 : n } , b _ { 1 : n } )$ begin result $\mathbf { \tau } = \mathbf { 0 }$ for $i = 1$ to $\pmb { n }$ do ${ \mathrm { r e s u l t } } = { \mathrm { r e s u l t } } + \alpha _ { i } b _ { i }$ end for return result end   
MATRIX-VECTOR.PRODUCT(a1:n,1:n , 61:n) begin for $i = 1$ to $\pmb { n }$ do $\mathbf { r e s u l t } _ { i } = 0$ for $j = 1$ to $\pmb { n }$ do ${ \mathrm { r e s u l t } } _ { i } = { \mathrm { r e s u l t } } _ { i } + a _ { i j } b _ { j }$ end for end for return result 1: n end

并行化通信分析假定算法10.10在分布存储的并行机上实现，且每个处理器在其局存中存有 $A$ 的若干行以及相应的向量 $\pmb { b } \sqrt { \pmb { d } } \setminus \pmb { r }$ 的分量。则由于并行化所造成的通信要求主要来源于向量内积(INNER.PRODUCT)和矩阵与向量乘积(MATRIX-VECTOR.PRODUCT)。在计算向量内积时，每个处理器计算它的局部积之和，为了计算总的积之和(即内积)要花费对数时间，所以向量内积的通信时间为 $O \left( { \frac { n } { \hbar } } + \log \hbar \right)$ 。在计算矩阵～向量之积时，每个处理器均需与其它处理器通信,以取得别的处理器中的向量 $\pmb { b }$ 之分量，为此可先把各个处理器中 $\pmb { b }$ 之分量集中在一个处理器中,然后由此处理器以树状形式播送给各处理器,这种通信策略的总耗费时间为 $O ( n \log { p } )$ 。

# 10.5 小结和导读

小结线性代数方程组的求解在科学和工程计算中应用非常广泛,这是因为很多科学与工程问题的计算，最终大都可以化为线性代数方程组的求解。本章主要讨论最基本的线性方程组的求解,包括三角形方程组、三对角方程组、稠密和稀疏线性方程组等的经典解法。

线性代数方程组的数值解法通常有两种：直接法和迭代法。直接法，又称消元法,是利用矩阵变换技巧,将一般的系数矩阵化为特殊形式(如上三角和对角形式)的矩阵以对方程组消解。其优点是可以预先估计运算量，并可得到问题的准确解，但由于实际计算过程中总存在着舍入误差,因此直接法得到的结果并非绝对精确，并且还存在着计算过程的稳定性问题。迭代法是一种逐步求精的近似求解过程,此法一般总是假定方程组中的系数 $a _ { i i } { \neq } 0 ( i = 1 , \cdots , n )$ 。其优点是简单,易于计算机编程，但它存在着迭代是否收敛和收敛快慢的问题。迭代求解的过程是，先给定初始解,然后逐次迭代下去，且理论上讲，每次迭代的结果都应改善前一次的计算结果。迭代过程由预先给定的精度要求来控制，但由于方程组的准确解一般是不知道的,因此判断某次迭代是否满足精度要求是困难的，通常我们总是认为当相邻两次迭代值 $x _ { i } \left( k \right)$ 与 $x _ { i } \left( k - 1 \right)$ 也很接近时, $x _ { i }$ 与 $x _ { i } \left( \boldsymbol { k } \right)$ 也很接近,因此就可直接用条件 $\operatorname* { m a x } _ { 1 \leqslant i \leqslant n } \big | x _ { i } ( k ) - x _ { i } ( k - 1 ) \big | < \varepsilon$ 来判定迭代是否终止。迭代法在求解稀疏线性方程组时经常使用，而很多的偏微分方程经差分化后也可化为稀疏线性方程组,所以在偏微分方程数值求解中,迭代法使用得尤其广泛。

导读[136]是一本很好的综述性专著,它全面地讨论了向量机和并行机上线性方程组的直接法和迭代法的并行求解方法;[91]是一篇有关并行数值算法的很好的综述文章;[149]展示了三角形方程组求解器可在多计算机上有效地实现;[96]首先引人奇－偶归约算法;[73]讨论了共享存储和分布存储结构的并行机上稠密线性方程组的并行算法;[90]综述了稀疏线性方程组的并行求解算法；[135]综述了在向量机和并行机上偏微分方程的求解方法；[44]讨论了超立方多处理机上的多重网格算法;[50]讨论了并行共轭梯度算法。在国内[202]全面地介绍了工程上常用的、行之有效的串行算法(主要偏重于数值问题的常用算法)；[201]较深人、系统地介绍了SIMD并行机上并行数值计算方法,对MIMD并行机上的数值算法也作了简要介绍;[195]深人而全面地论述了SIMD和MIMD模型上的数值代数、离散变换和卷积、微分方程、计算数论和最优化计算的并行算法,对并行排序算法也作了介绍。此外，在[143]书中第九章的参考文献注释中还列举了大量有关参考文献，读者可追踪进一步阅读。

# 习 题

10.1如果在(10.2)式中,引入虚变量 $\pmb { x _ { 0 } }$ 与 ${ \pmb x } _ { \pmb { \mathscr { n } } + 1 }$ 以及 ${ \pmb x } _ { - 1 }$ 与 $x _ { n + 2 }$ 且令它们为零：

$\textcircled{1}$ 试推导下式：

$$
f _ { i } \left( \frac { b _ { i - 1 } - f _ { i - 1 } x _ { i - 2 } - h _ { i - 1 } x _ { i } } { g _ { i - 1 } } \right) + g _ { i } x _ { i } + h _ { i } \left( \frac { b _ { i + 1 } - f _ { i + 1 } x _ { i } - h _ { i + 1 } x _ { i + 2 } } { g _ { i + 1 } } \right) = b _ { i }
$$

为了简化，记 $r _ { i } = f _ { \mathrm { i } } / g _ { \mathrm { i } - 1 } , \delta _ { \mathrm { i } } = h _ { \mathrm { i } } / g _ { \mathrm { i } + 1 } , 1 { \leqslant i } \leqslant n$ ,则(10.25)式可写成：$\begin{array} { r l } & { - \ r _ { i } \ f _ { i - 1 } x _ { i - 2 } + \big ( g _ { i } - r _ { i } h _ { i - 1 } - \delta _ { i } f _ { i + 1 } \big ) x _ { i } - \delta _ { i } h _ { i + 1 } x _ { i + 2 } = b _ { i } + r _ { i } b _ { i - 1 } - \delta _ { i } b _ { i + 1 } } \\ & { \qquad \quad 1 \leqslant i \leqslant n } \end{array}$ 根据(10.26)式,可设计如下 SISD上奇偶归约法求解三对角线性方程组算法10.11：

算法10.11 SISD上三对角方程组奇偶归约求解算法   
输入 $\mathbf { \partial } : A _ { n } \times \mathbf { \partial } _ { n } , b = \left[ b _ { 1 } , \cdots , b _ { n } \right] ^ { \mathbf { T } }$   
输出： $\mathbf { \pmb { x } } = \{ \pmb { x } _ { 1 } , \cdots , \pmb { x } _ { n } \} ^ { \bar { \mathbf { T } } }$   
Begin

(1) for ${ \bf { \sigma } } _ { i } = { \bf { 0 } }$ to $\log n - 1$ do (1.1) $\pmb { d } = 2 ^ { i }$ (1.2) for $\scriptstyle j = 2 i + 1$ to $\pmb { n } - 1$ step $\pmb { 2 } \pmb { d }$ do $\begin{array} { r l } & { r _ { j } = f _ { j } / g _ { j - d } , \ S _ { j } = h _ { j } / g _ { j + d } , f _ { j } ^ { \prime } = - r _ { j } f _ { j - d } , } \\ & { \boldsymbol { g } ^ { \prime } { } _ { j } = - \delta _ { j } f _ { i + d } - r _ { j } h _ { j - d } , \boldsymbol { h } ^ { \prime } { } _ { j } = \delta _ { j } h _ { j + d } } \\ & { \boldsymbol { b } ^ { \prime } { } _ { j } = b _ { j } + r _ { j } b _ { j - d } - \delta _ { j } b _ { j + d } } \end{array}$ end for (1.4) $\begin{array} { r l } & { r _ { n } = f _ { n } / g _ { n - d } } \\ & { f _ { n } = - \ r _ { n } f _ { n - d } } \\ & { g _ { n } = g _ { n } - \ r _ { n } h _ { n } - d } \\ & { b _ { n } = b _ { n } + \ r _ { n } b _ { n } - d } \end{array}$ (1.6) (1.7) for $\begin{array} { r } { j = 2 i + 1 } \end{array}$ to $\pmb { n } - 1$ step $2 d$ do $f _ { j } = f ^ { \prime } { } _ { j } , g _ { j } = g ^ { \prime } { } _ { j } , h _ { j } = h ^ { \prime } { } _ { j } , b _ { j } = b ^ { \prime } { } _ { j }$ end for end for

(2) ${ x _ { n } = b _ { n } / g _ { n } }$   
(3) for $\pmb { i } = \log \pmb { n } - 1$ to O step - 1 do (3.1) $d = 2 ^ { i }$ (3.2) $x _ { d } = ( b _ { d } - h _ { d } x _ { 2 d } ) / g _ { d }$ (3.3) for ${ j = 3 d }$ to $\pmb { n }$ step $^ { 2 d }$ do

$$
x _ { j } = ( b _ { j } - f _ { j } x _ { j - d } - h _ { j } x _ { j + d } ) / g _ { j }
$$

# end for

end for

End

$\textcircled{2}$ 假定：

$$
\begin{array} { r } { A = \left( \begin{array} { c c c c c c c c c } { 4 } & { 1 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 4 } & { 1 1 } & { - 5 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 2 } & { 1 4 } & { - 6 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 5 } & { 1 8 } & { - 4 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 1 } & { 2 } & { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 2 } & { 3 } & { 6 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 2 } & { 1 } & { 1 2 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 5 } & { 8 } \end{array} \right) , B = \left( \begin{array} { c } { 2 } \\ { 7 } \\ { 1 3 } \\ { 1 8 } \\ { 6 } \\ { 3 } \\ { 9 } \\ { 9 } \\ { - 1 } \end{array} \right) , } \end{array}
$$

10.2试证明：在奇偶归约算法中,如果对于所有 $_ i$ ，满足 $\mid _ { g _ { i } } \mid \geqslant \mid _ { f _ { i } } \mid + \mid _ { h _ { i } } \mid$ (即对角占优),则消去奇下标变量后的方程组仍具有对角占优的性质。

[提示：考查(10.5)式,对于所有 $\textbf { \em i }$ ,如果 $\mid _ { g _ { i } } \mid \geqslant \mid f _ { i } \mid + \mid h _ { i } \mid$ 其系数关系。]

10.3试分析高斯主元消去法算法10.4的复杂度为：

$$
( 2 n ^ { 3 } + 3 n ^ { 2 } - 2 n - 3 ) / 3
$$

10.4试用高斯主元消去法算法10.4,逐步求解下述线性方程组：

$$
\left( { \begin{array} { r r r r r } { - 1 } & { 2 } & { 1 } & { - 2 } \\ { 2 } & { 2 } & { 0 } & { 1 } \\ { 1 } & { - 1 } & { 3 } & { - 5 } \\ { - 2 } & { 3 } & { - 4 } & { 4 } \end{array} } \right) { \left( \begin{array} { l } { x _ { 1 } } \\ { x _ { 2 } } \\ { x _ { 3 } } \\ { x _ { 4 } } \end{array} \right) } = \left( { \begin{array} { l } { 4 } \\ { 3 } \\ { 2 } \\ { 1 } \end{array} } \right)
$$

10.5试分析算法10.5的复杂度。如果处理器按列分配,情况有何变化?

10.6根据10.3.2节所述原理,参照算法10.4,试写出 SISD上求解稠密线性方程组的高斯-约旦主元消去法的算法。

10.7试用高斯-赛德尔算法10.7,逐步求解下述线性方程组 ${ \bf \Pi } _ { \varepsilon } ^ { \prime } = 1 0 ^ { - 6 }$ ）

$$
\left( \begin{array} { c c c c } { { 1 } } & { { 3 } } & { { 2 } } & { { 1 3 } } \\ { { 7 } } & { { 2 } } & { { 1 } } & { { - 2 } } \\ { { 9 } } & { { 1 5 } } & { { 3 } } & { { - 2 } } \\ { { - 2 } } & { { - 2 } } & { { 1 1 } } & { { 5 } } \end{array} \right) \left( \begin{array} { c } { { x _ { 1 } } } \\ { { x _ { 2 } } } \\ { { x _ { 3 } } } \\ { { x _ { 4 } } } \end{array} \right) = \left( \begin{array} { c } { { 0 } } \\ { { 4 } } \\ { { 7 } } \\ { { - 1 } } \end{array} \right)
$$

# 10.8对于如下的泊松方程

$$
- \left( \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } + \frac { \partial ^ { 2 } u } { \partial y ^ { 2 } } \right) = f
$$

其中f=f(x,y)不为零,主要问题就是定出未知函数u=u(x,y)在某区域Ω内满足(10.27),且在边界 $\partial \varOmega$ 上满足给定的条件。

$\textcircled{1}$ 试推导其差分方程为：

$$
4 u _ { i , j } - ( u _ { i - 1 , j } + u _ { i + 1 , j } + u _ { i , j - 1 } + u _ { i , j + 1 } ) = h ^ { 2 } f _ { i , j } , 1 \leqslant i , j \leqslant n - 1
$$

其中， $\pmb { h }$ 为网格间距， $h = 1 / n \mathrm { ~ , ~ } u _ { i , j }$ 为格点 $( i , j )$ 的函数值 $u ( x _ { i } , y _ { j } )$

$\textcircled{2}$ 如何变换(10.28)式使其成为如下线性方程组：

$$
\pmb { A } \pmb { U } = \pmb { F }
$$

其中，系数矩阵 $\pmb { A }$ 为块三对角矩阵：

$$
\left( \begin{array} { l l l l } { s } & { \boldsymbol { \vartheta } } & & \\ { \boldsymbol { \vartheta } } & { s } & { \boldsymbol { \vartheta } } & \\ & { \cdot _ { \cdot } } & & \\ & { \boldsymbol { \vartheta } } & { s } & { \boldsymbol { \vartheta } } \\ & & & { \boldsymbol { \varrho } } & \end{array} \right)
$$

$\pmb { S }$ 和 $\pmb { Q }$ 都是 $\left( n - 1 \right) \times \left( n - 1 \right)$ 的矩阵，且 $\pmb { s }$ 本身又是三对角矩阵：

$$
\left( \begin{array} { c c c c c c } { { 1 } } & { { - \frac { 1 } { 4 } } } & { { } } & { { } } & { { } } & { { } } \\ { { - \frac { 1 } { 4 } } } & { { 1 } } & { { \frac { 1 } { 4 } } } & { { } } & { { } } & { { } } \\ { { } } & { { } } & { { \ddots } } & { { } } & { { } } & { { } } \\ { { } } & { { } } & { { - \frac { 1 } { 4 } } } & { { 1 } } & { { - \frac { 1 } { 4 } } } \\ { { } } & { { } } & { { } } & { { } } & { { - \frac { 1 } { 4 } } } & { { 1 } } \end{array} \right)
$$

而 $Q = - \frac { 1 } { 4 } I , I$ 为单位矩阵,向量 $\pmb { U }$ 未知：

$$
\begin{array} { r l } & { \pmb { U } ^ { \mathrm { T } } = ( u _ { 1 , 1 } , u _ { 1 , 2 } , \cdots , u _ { 1 , n - 1 } , u _ { 2 , 1 } , u _ { 2 , 2 } , \cdots , u _ { 2 , n - 1 } , \cdots , } \\ & { \qquad \quad u _ { n - 1 , 1 } , u _ { n - 1 , 2 } , \cdots , u _ { n - 1 , n - 1 } ) } \end{array}
$$

向量F已知,F(i-1)(n-1)+j= fi,jo

10.9试证明共轭梯度法求解 $\pmb { n }$ 阶线性方程组，最多迭代 $\pmb { n }$ 次即可收敛。

10.10试用共轭梯度法,求解下述方程组。假定

$$
{ \pmb x } ( 0 ) = [ 0 , 0 , 1 ] ^ { \mathrm { T } } \mathrm { : }
$$

$$
{ \left( \begin{array} { l l l } { 2 } & { 1 } & { 0 } \\ { 1 } & { 2 } & { 1 } \\ { 0 } & { 1 } & { 1 } \end{array} \right) } \left( { \begin{array} { l } { x _ { 1 } } \\ { x _ { 2 } } \\ { x _ { 3 } } \end{array} } \right) = { \left( \begin{array} { l } { 1 } \\ { 0 } \\ { 1 } \end{array} \right) }
$$

# 第十一章 快速傅里叶变换

20 世纪60年代是计算复杂性研究的主要里程碑。在此十年中发现了三个非常惊人的有效算法，即两整数乘法、离散的傅里叶变换和两矩阵相乘。其中1965年Cooley和Tukey所研究出的计算离散傅氏变换(DFT)的快速傅氏变换(FFT),将计算量从 $O ( n ^ { 2 } )$ 下降到 $O \left( n \log n \right)$ ，从而使得FFT在数字信号处理、石油勘探、地震预报、医学断层诊断、编码理论、量子物理及概率论等领域中都得到了广泛的应用。长期以来,各种快速FFT的算法不断出现，成为数值代数方面最活跃的一个研究领域，而其意义远远超过了算法研究的范围，进而为诸多科技领域的研究打开了一个崭新的局面。本章先从离散傅氏变换DFT讲起，引出Cooley-Tukey著名FFT蝶式计算图;然后讨论串行FFT迭代算法和串行FFT递归算法；最后研究并行FFT算法，包括网孔连接、蝶式连接、立方连接的SIMD机器上的并行FFT算法以及超立方多计算机上的并行FFT算法。因为傅氏变换会涉及到一些复数运算，所以把其作为预备知识给出，熟悉的读者可以不必读它。

# 11.1 离散傅氏变换

# $^ { \star }$ 11.1.1预备知识

复数及其表示复数 $Z$ 一般表示为 $z = a + \mathrm { i } b$ ,其中 $\mathbf { i } = { \sqrt { - 1 } }$ 称为虚数单位， $^ { a }$ 和 $\pmb { b }$ 分别为 $\pmb { z }$ 的实部和虚部。上述 $z = a + \mathrm { i } b$ 为复数的坐标表示法；它还有三角表示法 $z = r ( \cos \theta + \mathrm { i } \ \sin \theta )$ 。因为根据台劳级数，

$$
{ \begin{array} { r l } & { \sin \theta = \theta - \theta ^ { 3 } / 3 ! + \theta ^ { 5 } / 5 ! - \theta ^ { 7 } / 7 ! + \cdots } \\ & { \cos \theta = 1 - \theta ^ { 2 } / 2 ! + \theta ^ { 4 } / 4 ! - \theta ^ { 6 } / 6 ! + \cdots } \\ & { e ^ { \mathrm { i } \theta } = 1 + \mathrm { i } \theta - \theta ^ { 2 } / 2 ! - \mathrm { i } \theta ^ { 3 } / 3 ! + \theta ^ { 4 } / 4 ! + \mathrm { i } \theta ^ { 5 } / 5 ! + \cdots } \\ & { = ( 1 - \theta ^ { 2 } / 2 ! + \theta ^ { 4 } / 4 ! + \cdots ) + \mathrm { i } ( \theta - \theta ^ { 3 } / 3 ! + \theta ^ { 5 } / 5 ! + \cdots ) } \\ & { = \cos \theta + \mathrm { i } \sin \theta } \end{array} }
$$

所以复数还可以表示为指数形式 $z = r e ^ { \mathrm { i } \theta }$ 。如果 $r = 1 , \theta = 2 \pi / n$ ,则 $z = \mathrm { e } ^ { 2 \pi \mathrm { i } / n }$

单位根与单位元根方程 $x ^ { n } - 1 = 0$ 有 $\pmb { n }$ 个根,称为 $\pmb { n }$ 次单位根。如果复数 $\pmb { \omega }$ 是 $\pmb { n }$ 次单位根， $( \omega ^ { n } - 1 = 0 )$ ，则 $\omega ^ { k } ( k$ 为整数)也一定是 $\pmb { n }$ 次单位根,因为$( \omega ^ { k } ) ^ { n } = ( \omega ^ { n } ) ^ { k } = 1 ^ { k } = 1$ 。显然 $\omega ^ { n } - 1 = 0$ 有 $\pmb { n }$ 个根,如果这 $\pmb { n }$ 个根 $1 , \omega ^ { 1 } , \omega ^ { 2 } , \cdots ,$ $\omega ^ { n - 1 }$ 都不同,则称 $\omega ^ { 1 }$ 为 $\pmb { n }$ 次单位元根(Princ ipal nth Root of Unity）。显然$\omega = e ^ { 2 \pi \mathrm { i } / n }$ 是一个 $\pmb { n }$ 次单位元根。注意,不是所有的 $\pmb { n }$ 次单位根都可以称为 $\pmb { n }$ 次单位元根。例如,1是 $\pmb { n }$ 次单位根,但不是 $\pmb { n }$ 次单位元根。

在离散的傅氏变换中所定义的 $\pmb { \omega }$ 正好是一个 $\pmb { n }$ 次单位元根。

例11.1 如图11.1, $\pmb { n = 8 }$ 则有8个不同的8次单位根,其中 $\omega ^ { 1 }$ 为8次单位元根：

$$
\omega ^ { 1 } = \mathrm { e } ^ { 2 \pi \mathrm { i } / 8 } = \mathrm { e } ^ { \mathrm { i } \pi / 4 } = \cos { \frac { \pi } { 4 } } + \mathrm { i } \sin { \frac { \pi } { 4 } } = { \frac { \sqrt { 2 } } { 2 } } + \mathrm { i } { \frac { \sqrt { 2 } } { 2 } }
$$

$$
\begin{array} { r l } & { \quad _ { \pm } ^ { \pm } = ( e ^ { 2 \pi i \Phi } ) ^ { 2 } = \mathrm { e } ^ { i \pi / 2 } = \cos { \frac { \pi } { 2 } } + \mathrm { i } \sin { \frac { \pi } { 2 } } = 0 + \mathrm { i } } \\ & { \quad _ { \pm } ^ { 3 } = \omega ^ { 2 } \cdot \omega ^ { 1 } = \cos { \frac { 3 } { 4 } } \pi ^ { 4 } + \mathrm { i } \sin { \frac { 3 } { 4 } } \pi = - \frac { \sqrt { 2 } } { 2 } + \mathrm { i } \frac { \sqrt { 2 } } { 2 } } \\ & { \quad _ { \pm } ^ { 4 } = \omega ^ { 2 } \cdot \omega ^ { 2 } = \cos \pi + \mathrm { i } \sin \pi = - 1 + 0 } \\ & { \quad _ { \pm } ^ { 5 } = \omega ^ { 1 } \cdot _ { \omega ^ { 4 } } = \cos { \frac { 5 } { 4 } } \pi + \mathrm { i } \sin { \frac { 5 } { 4 } } \pi = - \frac { \sqrt { 2 } } { 2 } - \mathrm { i } \frac { \sqrt { 2 } } { 2 } } \\ & { \quad _ { \omega ^ { 6 } } = \omega ^ { 2 } \cdot _ { \omega ^ { 4 } } = 0 - \mathrm { i } } \\ & { \quad _ { \omega ^ { 7 } } = \omega ^ { 4 } \cdot _ { \omega ^ { 3 } } = \frac { \sqrt { 2 } } { 2 } - \mathrm { i } \frac { \sqrt { 2 } } { 2 } } \\ & { \quad _ { \omega ^ { 8 } } = \omega ^ { 4 } \cdot _ { \omega ^ { 8 } } = 1 + 0 \quad \Omega } \end{array}
$$

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0004_pages_0211-0280/auto/images/2f21e0d11990ac74515298431527839e03c31ae28c52cad3b9818088d48c1a97.jpg)  
图11.18次单位元根及其它的8次单位根

单位根的性质 $\textcircled{1}$ 对于 $n \geqslant 2 , \sum _ { k = 0 } ^ { n - 1 } \omega ^ { k } = 0 ; \textcircled { 2 } \omega ^ { n } = 1 , \omega ^ { n / 2 } = - 1 ; \textcircled { 3 } \omega ^ { s n + p } =$ $\omega ^ { p } { \big ( } s \circ \cdot n \cdot p$ 为正整数)。

# 11.1.2离散傅里叶变换

一个n 点离散傅里叶变换(Discrete Fourier Transform）,简记之为DFT,可定义


<!-- chunk 0005: pages 281-350 -->
为：给定序列 $( a _ { 0 } , a _ { 1 } , \cdots , a _ { n - 1 } )$ ，按如下规则变换成序列 $( b _ { 0 } , b _ { 1 } , \cdots , b _ { n - 1 } )$

$$
b _ { j } = \ \sum _ { k = 0 } ^ { n - 1 } \ \omega ^ { j k } a _ { k } , 0 { \leqslant } j { \leqslant } n - 1
$$

其中， $\pmb { \omega }$ 是单位 $\pmb { n }$ 次元根,即 $\omega = \mathrm { e } ^ { 2 \pi \mathrm { i } / n }$ ， $\mathbf { i } = { \sqrt { - 1 } }$ 。

上述公式也可写成矩阵 $\pmb { \omega }$ （其元素 $\omega ( j , k )$ 记之为 $\omega ^ { j k }$ )和向量 $\pmb { a }$ 之乘积：

$$
\left\{ \begin{array} { c } { { b _ { 0 } } } \\ { { b _ { 1 } } } \\ { { \cdot } } \\ { { \cdot } } \\ { { \cdot } } \\ { { \cdot } } \\ { { b _ { n - 1 } } } \end{array} \right\} = \left( \begin{array} { c c c c c c } { { \omega ^ { 0 } } } & { { \omega ^ { 0 } } } & { { \omega ^ { 0 } } } & { { \cdots } } & { { \omega ^ { 0 } } } \\ { { \omega ^ { 0 } } } & { { \omega ^ { 1 } } } & { { \omega ^ { 2 } } } & { { \cdots } } & { { \omega ^ { n - 1 } } } \\ { { \cdot } } & { { } } & { { } } & { { } } & { { } } \\ { { \cdot } } & { { } } & { { } } & { { } } & { { } } \\ { { \cdot } } & { { \cdot } } & { { } } & { { } } & { { } } \\ { { \cdot } } & { { } } & { { } } & { { } } & { { } } \\ { { \omega ^ { 0 } } } & { { \omega ^ { n - 1 } } } & { { \omega ^ { 2 ( n - 1 ) } } } & { { \cdots } } & { { \omega ^ { ( n - 1 ) ( n - 1 ) } } } \end{array} \right) \left( \begin{array} { c } { { a _ { 0 } } } \\ { { a _ { 1 } } } \\ { { \cdot } } \\ { { \cdot } } \\ { { \cdot } } \\ { { \cdot } } \\ { { a _ { n - 1 } } } \end{array} \right) .
$$

例11.2给定 $\pmb { a } = ( 1 , 2 , 4 , 3 )$ ,欲计算其DFT。先计算4个不同的单位4次根：

$$
\begin{array} { l } { { \omega ^ { 1 } = \mathrm { e } ^ { 2 \pi \mathrm { i } / 4 } = \mathrm { e } ^ { \mathrm { i } \pi / 2 } = \cos { \frac { \pi } { 2 } } + \mathrm { i } \sin { \frac { \pi } { 2 } } = \mathrm { i } } } \\ { { \displaystyle { \omega ^ { 2 } = - 1 } } } \\ { { \displaystyle { \omega ^ { 3 } = \omega ^ { 1 } \cdot \omega ^ { 2 } = - \mathrm { i } } } } \\ { { \displaystyle { \omega ^ { 4 } = \omega ^ { 2 } \cdot \omega ^ { 2 } = 1 } } } \end{array}
$$

其系数矩阵 $\pmb { \omega }$ 为：

$$
{ \left( \begin{array} { l l l l } { \omega ^ { 0 } } & { \omega ^ { 0 } } & { \omega ^ { 0 } } & { \omega ^ { 0 } } \\ { \omega ^ { 0 } } & { \omega ^ { 1 } } & { \omega ^ { 2 } } & { \omega ^ { 3 } } \\ { \omega ^ { 0 } } & { \omega ^ { 2 } } & { \omega ^ { 4 } } & { \omega ^ { 6 } } \\ { \omega ^ { 0 } } & { \omega ^ { 3 } } & { \omega ^ { 6 } } & { \omega ^ { 9 } } \end{array} \right) } = { \left( \begin{array} { l l l l } { \omega ^ { 0 } } & { \omega ^ { 0 } } & { \omega ^ { 0 } } & { \omega ^ { 0 } } \\ { \omega ^ { 0 } } & { \omega ^ { 1 } } & { \omega ^ { 2 } } & { \omega ^ { 3 } } \\ { \omega ^ { 0 } } & { \omega ^ { 2 } } & { \omega ^ { 4 } } & { \omega ^ { 2 } } \\ { \omega ^ { 0 } } & { \omega ^ { 3 } } & { \omega ^ { 2 } } & { \omega ^ { 1 } } \end{array} \right) } = { \left( \begin{array} { l l l l } { 1 } & { 1 } & { 1 } & { 1 } \\ { 1 } & { \mathrm { i } } & { - 1 } & { - \mathrm { i } } \\ { 1 } & { - 1 } & { 1 } & { - 1 } \\ { 1 } & { - \mathrm { i } } & { - 1 } & { \mathrm { i } } \end{array} \right) }
$$

所以序列 $\pmb { b }$ 为：

$$
\left( \begin{array} { c c c c } { { 1 } } & { { 1 } } & { { 1 } } & { { 1 } } \\ { { 1 } } & { { \mathrm { ~ i ~ } } } & { { - 1 } } & { { - \mathrm { i } } } \\ { { 1 } } & { { - 1 } } & { { 1 } } & { { - 1 } } \\ { { 1 } } & { { - \mathrm { i } } } & { { - 1 } } & { { \mathrm { i } } } \end{array} \right) \left( \begin{array} { c } { { 1 } } \\ { { 2 } } \\ { { 2 } } \\ { { 3 } } \end{array} \right) = \left( \begin{array} { c } { { 1 0 } } \\ { { - 3 - \mathrm { i } } } \\ { { 0 } } \\ { { - 3 + \mathrm { i } } } \end{array} \right)
$$

即 $b = \left( 1 0 , - 3 - \mathrm { i } , 0 , - 3 + \mathrm { i } \right)$ 。□

按照上述矩阵－向量相乘的方式来计算离散的傅氏变换，显然计算量为$O ( n ^ { 2 } )$ 。

# 11.1.3离散傅里叶逆变换

一个 $\boldsymbol { n }$ 点的离散傅里叶逆变换(Inverse Discrete Fourier Transform),简记之为 IDFT,可类似定义为：

$$
a _ { k } = \frac { 1 } { n } \sum _ { j = 0 } ^ { n - 1 } \omega ^ { - k j } b _ { j } , 0 { \leqslant } k { \leqslant } n - 1
$$

例11.3例如序列 $b = ( 1 0 , - 3 - \mathrm { i } , 0 , - 3 + \mathrm { i } )$ 之逆变换为：

$$
\frac { 1 } { 4 } \left( \begin{array} { c c c c c } { \omega ^ { 0 } } & { \omega ^ { 0 } } & { \omega ^ { 0 } } & { \omega ^ { 0 } } \\ { \omega ^ { 0 } } & { \omega ^ { - 1 } } & { \omega ^ { - 2 } } & { \omega ^ { - 3 } } \\ { \omega ^ { 0 } } & { \omega ^ { - 2 } } & { \omega ^ { - 4 } } & { \omega ^ { - 2 } } \\ { \omega ^ { 0 } } & { \omega ^ { - 3 } } & { \omega ^ { - 2 } } & { \omega ^ { - 1 } } \end{array} \right) \left( \begin{array} { c } { b _ { 0 } } \\ { b _ { 1 } } \\ { b _ { 2 } } \\ { b _ { 3 } } \end{array} \right) = \frac { 1 } { 4 } \left( \begin{array} { c c c c c } { 1 } & { 1 } & { 1 } & { 1 } \\ { 1 } & { - \mathrm { i } } & { - 1 } & { \mathrm { i } } \\ { 1 } & { - 1 } & { 1 } & { - 1 } \\ { 1 } & { \mathrm { i } } & { - 1 } & { - \mathrm { i } } \end{array} \right) \left( \begin{array} { c } { 1 0 } \\ { - 3 - \mathrm { i } } \\ { 0 } \\ { - 3 + \mathrm { i } } \end{array} \right)
$$

$$
= \frac { 1 } { 4 } \left( \begin{array} { c } { 4 } \\ { 8 } \\ { 1 6 } \\ { 1 2 } \end{array} \right) = \left( \begin{array} { c } { 1 } \\ { 8 } \\ { 2 } \\ { 4 } \\ { 3 } \end{array} \right)
$$

即 $a = ( 1 , 2 , 4 , 3 )$ 。□

# 11.1.4离散傅氏变换的蝶式计算

本节根据离散傅氏变换(11.1)式来推演 DFT蝶式计算流图。

当 $\scriptstyle n = 2$ 时， ${ \pmb { \omega } } = \mathrm { e } ^ { \pi } = \cos \pi + \mathrm { i } \ \mathrm { s i n } \pi = - 1$ ：

$$
\left( \begin{array} { c } { { b _ { 0 } } } \\ { { b _ { 1 } } } \end{array} \right) = \left( \begin{array} { c c } { { 1 } } & { { 1 } } \\ { { 1 } } & { { \omega } } \end{array} \right) \left( \begin{array} { c } { { a _ { 0 } } } \\ { { a _ { 1 } } } \end{array} \right) = \left( \begin{array} { c c } { { 1 } } & { { 1 } } \\ { { 1 } } & { { - 1 } } \end{array} \right) \left( \begin{array} { c } { { a _ { 0 } } } \\ { { a _ { 1 } } } \end{array} \right)
$$

所以,bo=ao+a1

$$
\pmb { b } _ { 1 } = \pmb { a } _ { 0 } - \pmb { a } _ { 1 }
$$

其蝶式计算图如图11.2(a)所示。

当n=4时,可以将其变成两个2点的DFT,兹推导如下,注意,ω²=-1,${ \omega } ^ { 3 } = { \bf { - } } { \omega } , { \omega } ^ { 4 } = 1 , { \omega } ^ { 6 } = { \bf { - } } 1 , { \omega } ^ { 9 } = { \omega } :$

$$
[ { \begin{array} { r } { b _ { 0 } } \\ { b _ { 1 } } \\ { b _ { 2 } } \\ { b _ { 3 } } \end{array} } ] = [ { \begin{array} { r r r r r r } { 1 } & { 1 } & { 1 } & { 1 } \\ { 1 } & { \omega } & { \omega ^ { 2 } } & { \omega ^ { 3 } } \\ { 1 } & { \omega ^ { 2 } } & { \omega ^ { 4 } } & { \omega ^ { 6 } } \\ { 1 } & { \omega ^ { 3 } } & { \omega ^ { 6 } } & { \omega ^ { 9 } } \end{array} } ] ( { \begin{array} { r } { \alpha _ { 0 } } \\ { \alpha _ { 1 } } \\ { \alpha _ { 2 } } \\ { \alpha _ { 3 } } \end{array} } ) = [ { \begin{array} { r r r r r r } { 1 } & { 1 } & { 1 } & { 1 } \\ { 1 } & { \omega } & { - 1 } & { - \omega } \\ { 1 } & { - 1 } & { 1 } & { - 1 } \\ { 1 } & { - 1 } & { - 1 } & { \omega } \end{array} } ] ( { \alpha _ { 0 } } \atop { \alpha _ { 1 } } \atop { \alpha _ { 2 } } \atop { \alpha _ { 3 } }  ) ( { \alpha _ { 1 } } \atop { \alpha _ { 3 } } \omega ^ { 5 }  ) ( { \alpha _ { 1 } } - { \omega _ { 1 } } - { \omega _ { 1 } } - 1 ) ( { \alpha _ { 1 } } \atop { \alpha _ { 1 } }  ) ( { \alpha _ { 2 } } \atop { \alpha _ { 2 } } ) ( { \alpha _ { 1 } } \atop { \alpha _ { 3 } }  ) ( { \alpha _ { 1 } } - { \omega _ { 1 } } - 1 ) ( { \alpha _ { 1 } } \atop { \alpha _ { 3 } }  ) ( { \alpha _ { 2 } } \atop { \alpha _ { 1 } } ) ( { \alpha _ { 1 } } \atop { \alpha _ { 2 } } \atop { \alpha _ { 3 } }  ) ( { \alpha _ { 1 } } - { \omega _ { 1 } } - 1 ) ( { \alpha _ { 1 } } \atop { \alpha _ { 1 } } ) ( { \alpha _ { 2 } } \atop { \alpha _ { 2 } } ) ( { \alpha _ { 1 } } \atop { \alpha _ { 3 } } ) ( { \alpha _ { 1 } } \atop { \alpha _ { 1 } } ) ( { \alpha _ { 1 } } -  \omega _  1
$$

对调 $b _ { 1 }$ 和 $b _ { 2 }$ ,系数矩阵1行和2行亦同时对调：

$$
\left| \begin{array} { r } { b _ { 0 } } \\ { b _ { 2 } } \\ { b _ { 1 } } \\ { b _ { 3 } } \end{array} \right| = \left( \begin{array} { r r r r r } { 1 } & { 1 } & { 1 } & { 1 } \\ { 1 } & { - 1 } & { 1 } & { - 1 } \\ { 1 } & { \omega } & { - 1 } & { - \omega } \\ { 1 } & { - \omega } & { - 1 } & { \omega } \end{array} \right) \left( \begin{array} { r } { a _ { 0 } } \\ { a _ { 1 } } \\ { a _ { 2 } } \\ { a _ { 3 } } \end{array} \right)
$$

$$
= { \left[ \begin{array} { l l l l l l l } { 1 } & { } & { 1 } & { 0 } & { } & { 0 } \\ { 1 } & { - 1 } & { 0 } & { } & { 0 } \\ { 0 } & { } & { 0 } & { 1 } & { } & { 1 } \\ { 0 } & { } & { 0 } & { 1 } & { - 1 } \end{array} \right] } { \left[ \begin{array} { l l l l l } { 1 } & { 0 } & { } & { 1 } & { } & { 0 } \\ { 0 } & { 1 } & { } & { 0 } & { } & { 1 } \\ { 1 } & { 0 } & { - 1 } & { } & { 0 } \\ { 0 } & { \omega } & { } & { 0 } & { - \omega } \end{array} \right] } { \left[ \begin{array} { l } { a _ { 0 } } \\ { a _ { 1 } } \\ { a _ { 2 } } \\ { a _ { 3 } } \end{array} \right] }
$$

$$
\begin{array}{c} \begin{array}{c} = \left( \begin{array} { c c c c } { { 1 } } & { { 1 } } & { { 0 } } & { { 0 } } \\ { { 1 } } & { { - 1 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 1 } } & { { 1 } } \\ { { 0 } } & { { 0 } } & { { 1 } } & { { - 1 } } \end{array} \right) \left( \begin{array} { c } { { \alpha _ { 0 } + \alpha _ { 2 } } } \\ { { \alpha _ { 1 } + \alpha _ { 3 } } } \\ { { \alpha _ { 0 } - \alpha _ { 2 } } } \\ { { \left( \alpha _ { 1 } - \alpha _ { 3 } \right) \omega } } \end{array} \right) = \left( \begin{array} { c c c } { { \left( 1 \right)} } & { { 1 } } \\ { { 1 } } & { { - 1 } } \end{array}   & { { \left( \alpha _ { 0 } + \alpha _ { 2 } \right) } } \\ { { \left( 1 \right)} } & { { 1 } } \\ { { 1 } } & { { - 1 } } \end{array}   & { { \left( \alpha _ { 1 } - \alpha _ { 3 } \right) \omega } } \end{array} \right)
$$

$$
{ \bf \theta } = \left\{ \begin{array} { l } { { \left( a _ { 0 } + a _ { 2 } \right) + \left( a _ { 1 } + a _ { 3 } \right) } } \\ { { \left( a _ { 0 } + a _ { 2 } \right) - \left( a _ { 1 } + a _ { 3 } \right) } } \\ { { \left( a _ { 0 } - a _ { 2 } \right) + \left( a _ { 1 } - a _ { 3 } \right) \omega } } \\ { { \left( a _ { 0 } - a _ { 2 } \right) - \left( a _ { 1 } - a _ { 3 } \right) \omega } } \end{array} \right.
$$

所以原4点的DFT就化成了两个2点的DFT:

$$
\begin{array} { r l } & { b _ { 0 } = \left( \alpha _ { 0 } + \alpha _ { 2 } \right) + \left( \alpha _ { 1 } + \alpha _ { 3 } \right) } \\ & { b _ { 2 } = \left( \alpha _ { 0 } + \alpha _ { 2 } \right) - \left( \alpha _ { 1 } + \alpha _ { 3 } \right) } \\ & { b _ { 1 } = \left( \alpha _ { 0 } - \alpha _ { 2 } \right) + \left( \alpha _ { 1 } - \alpha _ { 3 } \right) \omega } \\ & { b _ { 3 } = \left( \alpha _ { 0 } - \alpha _ { 2 } \right) - \left( \alpha _ { 1 } - \alpha _ { 3 } \right) \omega } \end{array}
$$

其蝶式计算图如图11.2(b)所示。

当 $\pmb { n = 8 }$ 时,8个不同的单位8次根为 $\omega , \omega ^ { 2 } , \omega ^ { 3 } , \omega ^ { 4 } = - 1 , \omega ^ { 5 } \ = \ - \ \omega , \ \omega ^ { 6 }$ $= - \omega ^ { 2 } , \omega ^ { 7 } = - \omega ^ { 3 } , \omega ^ { 8 } = 1 ;$

$$
\{ \begin{array} { c } { { b _ { 0 } } } \\ { { b _ { 1 } } } \\ { { b _ { 2 } } } \\ { { b _ { 3 } } } \\ { { b _ { 4 } } } \\ { { b _ { 5 } } } \\ { { b _ { 6 } } } \\ { { b _ { 7 } } } \end{array}  [ \begin{array} { c c c c c c c c } { { 1 } } & { { 1 } } & { { 1 } } & { { 1 } } & { { 1 } } & { { 1 } } & { { 1 } } & { { 1 } } \\ { { 1 } } & { { \omega ^ { 1 } } } & { { \omega ^ { 2 } } } & { { \omega ^ { 3 } } } & { { \omega ^ { 4 } } } & { { \omega ^ { 5 } } } & { { \omega ^ { 6 } } } & { { \omega ^ { 7 } } } \\ { { 1 } } & { { \omega ^ { 2 } } } & { { \omega ^ { 4 } } } & { { \omega ^ { 6 } } } & { { 1 } } & { { \omega ^ { 2 } } } & { { \omega ^ { 4 } } } & { { \omega ^ { 6 } } } \\ { { 1 } } & { { \omega ^ { 3 } } } & { { \omega ^ { 6 } } } & { { \omega } } & { { \omega ^ { 4 } } } & { { \omega ^ { 7 } } } & { { \omega ^ { 2 } } } & { { \omega ^ { 5 } } } \\ { { 1 } } & { { \omega ^ { 4 } } } & { { 1 } } & { { \omega ^ { 4 } } } & { { 1 } } & { { \omega ^ { 4 } } } & { { 1 } } & { { \omega ^ { 4 } } } \\ { { 1 } } & { { \omega ^ { 5 } } } & { { \omega ^ { 2 } } } & { { \omega ^ { 7 } } } & { { \omega ^ { 4 } } } & { { \omega } } & { { \omega ^ { 6 } } } & { { \omega ^ { 3 } } } \\ { { 1 } } & { { \omega ^ { 6 } } } & { { \omega ^ { 4 } } } & { { \omega ^ { 2 } } } & { { 1 } } & { { \omega ^ { 6 } } } & { { \omega ^ { 4 } } } & { { \omega ^ { 2 } } } \\ { { 1 } } & { { \omega ^ { 7 } } } & { { \omega ^ { 6 } } } & { { \omega ^ { 5 } } } & { { \omega ^ { 4 } } } & { { \omega ^ { 3 } } } & { { \omega ^ { 2 } } } \end{array} ] ( \begin{array} \end{array}
$$

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0005_pages_0281-0350/auto/images/de9c3259fb05e6534f0d4d695979dc870496839f210285035aaf9bb8da6b16a5.jpg)  
图11.2离散傅氏变换蝶式计算流图

同样,我们可以将其化为两个4点的DFT,每个再化成两个2点的DFT,最后得：

$$
\begin{array} { r l } & { b _ { 0 } = [ ( a _ { 0 } + \alpha _ { 4 } ) + ( a _ { 2 } + \alpha _ { 6 } ) ] + [ ( a _ { 1 } + a _ { 5 } ) + ( a _ { 3 } + \alpha _ { 7 } ) ] \omega ^ { 0 } } \\ & { b _ { 4 } = [ ( a _ { 0 } + a _ { 4 } ) + ( a _ { 2 } + a _ { 6 } ) ] - [ ( a _ { 1 } + a _ { 5 } ) + ( a _ { 3 } + \alpha _ { 7 } ) ] \omega ^ { 0 } } \\ & { b _ { 2 } = [ ( a _ { 0 } + a _ { 4 } ) - ( a _ { 2 } + a _ { 6 } ) ] + [ ( a _ { 1 } + a _ { 5 } ) - ( a _ { 3 } - a _ { 7 } ) ] \omega ^ { 2 } } \\ & { b _ { 6 } = [ ( a _ { 0 } + a _ { 4 } ) - ( a _ { 2 } - a _ { 6 } ) ] - [ ( a _ { 1 } + a _ { 5 } ) - ( a _ { 3 } - a _ { 7 } ) ] \omega ^ { 2 } } \\ & { b _ { 1 } = [ ( a _ { 0 } - a _ { 4 } ) + ( a _ { 2 } - a _ { 6 } ) \omega ^ { 2 } ] + [ ( a _ { 1 } - a _ { 5 } ) + ( a _ { 3 } - a _ { 7 } ) \omega ^ { 2 } ] \omega } \\ & { b _ { 5 } = [ ( a _ { 0 } - a _ { 4 } ) + ( a _ { 2 } - a _ { 6 } ) \omega ^ { 2 } ] - [ ( a _ { 1 } - a _ { 5 } ) + ( a _ { 3 } - a _ { 7 } ) \omega ^ { 2 } ] \omega } \\ & { b _ { 3 } = [ ( a _ { 0 } - a _ { 4 } ) - ( a _ { 2 } - a _ { 6 } ) \omega ^ { 2 } ] + [ ( a _ { 1 } - a _ { 5 } ) - ( a _ { 3 } - a _ { 7 } ) \omega ^ { 2 } ] \omega } \\ &  b _ { 7 } = [ ( a _ { 0 } - a _ { 4 } ) - ( a _ { 2 } - a _ { 6 } ) \omega ^ { 2 } ] - [ ( a _ { 1 } - a _ { 5 } ) - ( a  \end{array}
$$

其蝶式计算图如图 $1 1 . 2 ( \mathrm { c } )$ 所示。

# $\yen 12$ 快速傅氏变换串行算法

# 11.2.1 串行FFT迭代算法

FFT算法版本很多，但大体上可分为两类：迭代法和递归法。本节先讨论

迭代法，下节再讨论递归法。

算法11.1 SISD上FFT迭代算法

输入： ${ \pmb a } = ( a _ { 0 } , \cdots , a _ { n - 1 } )$ 输出： $\pmb { b } = ( b _ { 0 } , \cdots , b _ { n - 1 } )$

# Begin

(1）for ${ \pmb k } = { \bf 0 }$ to $\pmb { n } - 1$ do $\big / \ast$ 初始化 $\yen 7$

$$
c _ { k } = a _ { k }
$$

(2） for $\pmb { h } = \log \pmb { n } - 1$ to 0 do (2.1) $\begin{array} { l } { { \pmb { \mathscr { p } } } = 2 ^ { { \pmb { \mathscr { h } } } } } \\ { { \pmb q } = { \pmb { \mathscr { n } } } / { \pmb { \mathscr { p } } } } \\ { { \pmb z } = { \pmb { \mathscr { \omega } } } ^ { q } / 2 } \end{array}$ (2.2) (2.3) (2.4) for ${ \pmb k } = { \bf 0 }$ to $\pmb { n } - 1$ do if $( k \ \mathrm { m o d } \ \not p = k \ \mathrm { m o d } ( 2 \not p ) )$ then $\diagup \ast \left( \mathrm { i } \right)$ 和(ii)同时执行 $\yen 7$ (i)ck = Ck + Ck+p （ $\mathrm { i i } ) c _ { k + p } = \left( c _ { k } - c _ { k + p } \right) Z ^ { k \mathrm { m o d } p } / \ast c _ { k }$ 不用(i)计算的值 $\yen 7$

# endif

# endfor

# endfor

(3) for $k = 1$ to $\pmb { n } - 1$ do $\big / \big \varkappa$ 调整位序 $\yen 7$ $b _ { r ( k ) } = c _ { k } \quad / * r ( k )$ 为 $\pmb { k }$ 的位反 $\yen 7$ endfor

End

显然,算法的复杂度为 $O \left( n \log n \right)$ 。

例11.4给定 $\pmb { a } = \left( a _ { 0 } , a _ { 1 } , a _ { 2 } , a _ { 3 } \right)$ ,试计算 $\pmb { b } = \left( b _ { 0 } , b _ { 1 } , b _ { 2 } , b _ { 3 } \right)$ 。算法执行第(1)步，计算出 $c _ { 0 } = \alpha _ { 0 } , c _ { 1 } = \alpha _ { 1 } , c _ { 2 } = \alpha _ { 2 }$ ，和 $\mathbf { \Delta } _ { C 3 } = \mathbf { \Delta } _ { a _ { 3 } } .$ 算法执行第(2）步， $\pmb { h } = 1$ 时， $\scriptstyle { p = 2 , q = 2 , z = \omega }$ ，只有 $k = 0$ 和1满足条件：当 $k = 0$ 时计算出 $c _ { 0 } = a _ { 0 } +$ $\boldsymbol { a } _ { 2 } , \boldsymbol { c } _ { 2 } = \boldsymbol { a } _ { 0 } - \boldsymbol { a } _ { 2 }$ ；当 $k = 1$ 计算出 $c _ { 1 } = \alpha _ { 1 } + \alpha _ { 3 } , c _ { 3 } = { \left( a _ { 1 } - a _ { 3 } \right) } \omega _ { o } h = 0$ 时， $\pmb { \hat { p } = 1 }$ ，q=4，x=ω²,只有k=0和2满足条件:当k=0时计算出co=(ao+a2)+(a1+a3),c1=(ao+a2)-(a1+a3);当k=2时计算出 c2=(ao-a2)+i(a1-a3),c3=(ao-a2)-i（a1-a3)。算法执行第(3)步,结果为bo=co,b1=c2,b=c1

和 $b _ { 3 } = c _ { 3 }$ 。□

# 11.2.2 串行FFT递归算法

本节使用分而治之思想来推导递归的FFT计算算法。注意在下面推导中，反复使用 $\omega ^ { n } = 1 , \omega ^ { n / 2 } = - 1 , \omega ^ { l n } = 1$ 和 $\omega ^ { s n } { } ^ { + } \mathbf { \nabla } ^ { } = \omega ^ { p }$ 这几个等式。

对于 $b _ { \mathrm { j } } = \sum _ { k = 0 } ^ { n - 1 } \omega ^ { j k } a _ { k } , 0 \leqslant j \leqslant n - 1 \leqslant$ 首先，令 $j$ 为偶下标，即 $j = 2 l$ $\left( 0 { \leqslant } l { \leqslant } \frac { n } { 2 } - 1 \right)$ ，注意 $\omega ^ { l n } = \left( \omega ^ { n } \right) ^ { l } = 1$ ，于是

$$
\begin{array} { c } { { \displaystyle b _ { 1 } = b _ { 2 \ell } = \displaystyle \sum _ { k = 0 } ^ { \infty 1 } \omega ^ { 2 k } \alpha _ { k } } } \\ { { \displaystyle = a _ { 0 } + \omega ^ { 2 } \alpha _ { 1 } + \omega ^ { 4 } \alpha _ { 2 } + \cdots + \omega ^ { 2 l } \Big ( \frac { n } { 2 } - 1 \Big ) \alpha _ { \frac { n } { 2 } - 1 } ^ { n } + } } \\ { { \displaystyle a _ { \frac { 1 } { 2 } } ^ { n } + \omega ^ { 2 } \alpha _ { \frac { n } { 2 } + 1 } + \omega ^ { 4 } \alpha _ { \frac { n } { 2 } + 2 } ^ { n } + \cdots + \omega ^ { 2 l } \Big ( \frac { n } { 2 } - 1 \Big ) \alpha _ { n - 1 } } } \\ { { \displaystyle = \big ( a _ { 0 } + a _ { \frac { 1 } { 2 } } \big ) + \omega ^ { 2 l } \big ( \alpha _ { 1 } + a _ { \frac { 1 } { 2 } + 1 } ^ { n } \big ) + \omega ^ { 4 l } \big ( \alpha _ { 2 } + a _ { \frac { 1 } { 2 } + 2 } ^ { n } \big ) + } } \\ { { \displaystyle \quad \quad \cdots + \omega ^ { 2 l } \Big ( \frac { n } { 2 } - 1 \big ) \big ( a _ { \frac { 1 } { 2 } - 1 } ^ { n } + a _ { n - 1 } \big ) } } \\ { { \displaystyle = \big ( \alpha _ { 0 } + \alpha _ { \frac { 1 } { 2 } } ^ { n } \big ) + \omega ^ { 0 } \big ( a _ { 1 } + \alpha _ { \frac { 1 } { 2 } + 1 } ^ { n } \big ) + \omega ^ { 0 } \big ( \alpha _ { 2 } + a _ { \frac { 1 } { 2 } + 2 } ^ { n } \big ) + } } \\ { { \displaystyle \quad \cdots + \omega ^ { 0 } \big ( \alpha _ { \frac { n } { 2 } - 1 } + \alpha _ { n - 1 } \big ) } } \end{array}
$$

同样,令 $j$ 为奇下标，即 $_ { j } = 2 l + 1$ ,注意 $\omega ^ { n / 2 } = - 1$ ，于是

$$
\begin{array} { r l } { \gamma _ { 5 } = b _ { 2 + 1 } - } & { \displaystyle \sum _ { k = 0 } ^ { \infty + 1 } \frac { \omega ^ { 2 } + 1 } { \omega ^ { 2 } } \mathrm { t a n h } _ { \Omega _ { k } } } \\ { = } & { a _ { 0 + 1 } + \omega ^ { 2 , 1 - 1 } a _ { 1 } + \omega ^ { 2 , 1 - 1 } a _ { 2 } + \cdots + \omega \left( \frac { \lambda _ { - } - 1 } { 2 } \right) ( 2 - 1 ) a _ { 2 } ^ { 2 } - 1 } \\ & { \displaystyle \sum _ { k = 0 } ^ { \infty + 1 } a _ { 2 } + 1 \omega _ { \Omega _ { k } } \left( \omega ^ { 2 } + 1 \right) a _ { 2 + 1 } ^ { 2 } + \cdots + \omega ^ { 2 , 1 - 1 } \omega ^ { 2 , 1 - 1 } a _ { 2 } ^ { 2 } - 1 } \\ & { \displaystyle \sum _ { a _ { 0 } \neq 0 } ^ { \infty + 2 } a _ { 3 } + a _ { 3 } ^ { 2 } \omega _ { a _ { 2 } + 1 } ^ { 2 } - \cdots + \omega ^ { 2 , 1 } \omega _ { a _ { 1 } } ^ { 2 } - 1 \omega _ { a _ { 2 } + 1 } ^ { 2 } } \\ & { \displaystyle a _ { 2 } ^ { 2 } - \omega ^ { 2 } a _ { 0 } a _ { 1 } ^ { 2 } - \cdots - \omega ^ { 2 } \left( \frac { \lambda _ { - } - 1 } { 2 } \right) a _ { 2 } ^ { 2 } \cdots \omega _ { a _ { 1 } - 1 } } \\ & { \displaystyle ( a _ { 0 } - a _ { 2 } ) + \omega ^ { 2 } a _ { 0 } ^ { 2 } ( a _ { 1 } - a _ { 2 } + 1 ) + \omega ^ { 2 } a _ { 0 } ^ { 2 } ( a _ { 2 } - a _ { 2 } ^ { 2 } \tau _ { 2 } ) + } \\ & { \displaystyle - \imath + \omega ^ { 2 } a _ { 1 } ^ { 2 } - 1 \omega _ { a _ { 2 } - 1 } ^ { 2 } \omega _ { a _ { 1 } - 1 } } \\ & { \displaystyle ( \omega - a _ { 0 } \omega _ { 0 } ) ^ { 2 } + \omega ( a _ { 1 } - a _ { 2 } \omega _ { 1 } ^ { 2 } - a _ { 2 } \omega _ { 2 } ^ { 2 } \omega _ { 2 } - a _ { 2 } ^ { 2 } \tau _ { 2 } ) + } \\ &  \displaystyle - \imath + \omega ^ { 2 } a _ { 0 } ^ { 2 } \cdots + \omega ^ { 2 } a _  0 \end{array}
$$

根据(11.4)式和(11.5)式,就可画出如图11.3所示的离散傅里叶变换递归计算流图。图11.4就是一个按此递归方法计算的n=8的FFT蝶式计算图。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0005_pages_0281-0350/auto/images/44e00cac93a1158aa00d3ea1ba680d495291307c8d86e5953dd43994a4d65c44.jpg)  
图11.3FFT递归计算流图

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0005_pages_0281-0350/auto/images/73668b14f0eed0b124e0e62317a16117a678c34e431f19216a785a28236ccf72.jpg)  
图11.4 $\pmb { n = 8 }$ 的FFT蝶式计算图

下面给出串行的FFT递归算法。

算法11.2 SISD上FFT递归算法 输入： $\pmb { a } = ( a _ { 0 } , \cdots , a _ { n - 1 } )$ 输出： $\pmb { b } = ( b _ { 0 } , \cdots , b _ { n - 1 } )$ Procedure RFFT $( a , b )$ Begin

if $\pmb { n = 1 }$ then ${ \boldsymbol { b } } _ { 0 } = { \boldsymbol { a } } _ { 0 }$ else $\begin{array} { r l } & { \left( a _ { 0 } , a _ { 2 } , \cdots , a _ { n - 2 } , u _ { 0 } , u _ { 1 } , \cdots , u _ { 2 } ^ { n } - 1 \right) } \\ & { \left( a _ { 1 } , a _ { 3 } , \cdots , a _ { n - 1 } , v _ { 0 } , v _ { 1 } , \cdots , v _ { \frac { n } { 2 } - 1 ) } ^ { } \right. } \end{array}$

(3) $z = 1$   
(4） for $j = 0$ to $\pmb { n } - 1$ do(4.1) (4.2） $\begin{array} { l } { b _ { \mathrm { j } } = u _ { j \mathrm { ~ m o d } } \frac { n } { 2 } + z \ v _ { j \mathrm { m o d } } \frac { n } { 2 } } \\ { z = z \ \omega } \end{array}$

# endfor

# endif

End

显然,上述算法的复杂度表示为 $t \left( n \right) = 2 t \left( \frac { n } { 2 } \right) + O \left( n \right)$ ，解之得 ${ \pmb t } ( { \pmb n } ) =$ $O ( n \log n ) ,$

# 11.3 并行FFT算法

# 11.3.1 SIMD-MC²上FFT算法

算法描述本节所要描述的算法,实际上是算法11.1在网孔结构上的具体实现。假定 $\pmb { n }$ 个处理器 $\mathbb { P } _ { 0 } , \ \mathbb { P } _ { 1 } , \cdots , \mathbb { P } _ { n - 1 }$ 排成 $\sqrt { n } \times \sqrt { n }$ 的方阵 $\mathbf { \nabla } ( n = 2 ^ { s } \times 2 ^ { s } =$ $2 ^ { 2 s }$ ),处理器按图11.5所示的行主编号。 $\pmb { n }$ 的二进制数表示为： $2 ^ { \log n - 1 } 2 ^ { \log n - 2 \ldots }$ $2 ^ { 1 } 2 ^ { 0 }$ 。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0005_pages_0281-0350/auto/images/88839c082993709a2c13c169759ecf4a55f40186e4e99298618e7924f0153b47.jpg)  
图11.5并行计算FFT的网孔结构

令 $k$ 是 $\log n$ 位长的二进制整数，其位反为 $r ( k )$ （例如， ${ \pmb k } = { \bf 0 } { \bf 1 0 1 1 }$ ,则 $r ( k )$ $= 1 1 0 1 0 )$ 。假定输人序列 $( a _ { 0 } , a _ { 1 } , \cdots , a _ { n - 1 } )$ 开始时已处于阵列的各处理器中,即Pk保存ak（k=0,,n-1)。算法结束时,Pk保存bk。网孔上FFT算法的形式描述如下：

算法11.3 SIMD $\mathbf { M C } ^ { 2 }$ 上FFT算法输入： $a _ { k }$ 处于 $\mathrm { \bf P } _ { k }$ 中， $k = 0 , \cdots , n - 1$ 输出： $b _ { k }$ 处于 $\mathbf { P } _ { k }$ 中

# Begin

(1） for $k = 0$ to $\pmb { n } - 1$ par-do$c _ { k } = a _ { k }$ endfor

(2）for $\pmb { h } = \log \pmb { n } - 1$ to O do for ${ \boldsymbol { k } } \ = \mathbf { 0 }$ to ${ \pmb n } - 1$ par-do (2.1) $\pmb { \mathscr { p } } = 2 ^ { \frac { \hbar } { L } }$ (2.2) ${ \pmb q } = { \pmb n } / { \pmb \ p }$ (2.3) $\scriptstyle { \pmb z } = { \pmb \omega } ^ { \pmb \mathcal { P } }$ (2.4) if $\left( k \mathrm { m o d } \ p = k \mathrm { m o d } \ 2 p \right)$ then par-do (i） $c _ { k } = c _ { k } + c _ { k + p } z ^ { r \left( k \right) \mathrm { m o d } q } / \ast \mathrm { ( i ) }$ 和(ii)同 时执行 $\yen 7$ $\left( \operatorname { i i } \right) c _ { k + \mathtt { p } } = c _ { k } - c _ { k + \mathtt { p } } z ^ { r ( k ) \bmod q }$

# endif

endfor endfor (3) for ${ \bf k } = { \bf 0 }$ to $\pmb { n } - 1$ par-do $b _ { k } = c _ { r ( k ) } \qquad / * \ r ( k )$ 为 $\pmb { k }$ 的位反 $\yen 7$ endfor

End

其中,(2.4)步的条件 $k { \bmod { \hat { \varepsilon } } } = k { \bmod { \hat { \varepsilon } } } 2 { \hat { \varepsilon } }$ 是确保参与运算的处理器处于同一行或同一列中；(2.3)步是乘幂运算，是为了计算系函数矩阵元素。如果也用$\pmb { n }$ 个排成 ${ \sqrt { n } } \times { \sqrt { n } }$ 的处理器来计算的话,可令 $\mathbb { P } \{ j , k \}$ 负责计算 $\omega ^ { ( j - 1 ) ( k - 1 ) }$ ， $1 \leqslant$ $j , k \leqslant \sqrt { n }$ 。注意 $\omega ^ { ( j - 1 ) ( k - 1 ) }$ 的计算可重复执行平方和乘法（例如， $\omega ^ { 1 3 } = \big [ ( \omega ^ { 2 } ) ^ { 2 }$ $\times \omega ] \times [ ( ( \omega ^ { 2 } ) ^ { 2 } ) ^ { 2 } ] )$ ，所以可设计如下算法来计算傅氏变换的系函数矩阵元素w。假定每个处理器有三个寄存器：Mj存放ω的幂,X和Y存放中间结果，而计算结果返回在 $\Upsilon _ { k j } = \pmb { \omega } ^ { ( k - 1 ) ( j - 1 ) }$ 。

Procedure COMPUTE $\omega ^ { j k }$ Begin

$$
\mathbf { M } _ { k j } = { \left( { k - 1 } \right) } { \left( { j - 1 } \right) }
$$

(2) (3） $\begin{array} { r } { { \mathrm { X } } _ { k j } = \omega } \\ { { \mathrm { Y } } _ { k j } = 1 } \end{array}$   
（4）while $\mathbf { M } _ { k j } \neq 0$ do (4.1)if $\mathbf { M } _ { k j }$ 是奇数 then $\mathrm { Y } _ { k j } = \mathrm { X } _ { k j } \cdot \mathrm { Y } _ { k j }$ endif (4.2) $\begin{array} { l } { { \bf { M } } _ { k j } = \lfloor { \bf { M } } _ { k j } / 2 \rfloor } \\ { { \bf { X } } _ { k j } = { \bf { X } } _ { k j } ^ { 2 } } \end{array}$ (4.3) end while

End

显然，上述算法的复杂度为 $O ( \log n )$ 。

例11.5令 $\pmb { n } = 4$ ,排成 $2 \times 2$ 的处理器 $\mathbf { P _ { 0 } } \setminus \mathbf { P _ { 1 } } \setminus \mathbf { P _ { 2 } }$ 和 $\mathbf { P _ { 3 } }$ 按行主编号。算法11.3执行第(2)步， $\pmb { h } = 1$ 时， $\scriptstyle { p = 2 , q = 2 , z = \omega ^ { 2 } }$ ，满足 $k \mathrm { m o d } \ 2 = k \mathrm { m o d } \ 4$ 的处理器为 $\mathbf { P _ { 0 } }$ 和 $\mathbf { P } _ { 1 } { : } \mathbf { P } _ { 0 }$ 计算 $\begin{array} { r } { \dot { \mathbf { \sigma } } , c _ { 0 } = c _ { 0 } + c _ { 2 } \big ( \omega ^ { 2 } \big ) ^ { 0 } = \alpha _ { 0 } + \alpha _ { 2 } , c _ { 2 } = c _ { 0 } - \big ( \omega ^ { 2 } \big ) ^ { 0 } c _ { 2 } = \alpha _ { 0 } - \alpha _ { 2 } ; } \end{array}$ $\mathbf { P } _ { 1 }$ 计算 $c _ { 1 } = c _ { 1 } + ( \omega ^ { 2 } ) ^ { 0 } c _ { 3 } = \alpha _ { 1 } + \alpha _ { 3 } , c _ { 3 } = c _ { 1 } - \big ( \omega ^ { 2 } \big ) ^ { 0 } c _ { 3 } = \alpha _ { 1 } - \alpha _ { 3 } , \mathrm { I }$ 此时同列中的处理器要进行通信。 $\pmb { h } = \pmb { 0 }$ 时， $\ p = 1 , q = 4 , z = \omega$ ，满足 $k \mathrm { m o d } 1 = k \mathrm { m o d } 2$ 的处理器为 ${ \tt P } _ { 0 }$ 和 $\mathbf { P } _ { 2 } : \mathbf { P } _ { 0 }$ 计算 ${ \mathrm { \Delta } c } _ { 0 } = c _ { 0 } + \omega ^ { 0 } c _ { 1 } = \left( a _ { 0 } + a _ { 2 } \right) + \left( a _ { 1 } + a _ { 3 } \right) , c _ { 1 } = c _ { 0 } - \omega ^ { 0 } c _ { 1 } =$ $( a _ { 0 } + a _ { 2 } ) - \left( a _ { 1 } + a _ { 3 } \right) ; \mathbf { P } _ { 2 }$ 计算 $c _ { 2 } = c _ { 2 } + \omega c _ { 3 } = \left( a _ { 0 } - a _ { 2 } \right) + \left( a _ { 1 } - a _ { 3 } \right) \omega , c _ { 3 } = c _ { 2 } -$ $\omega c _ { 3 } = \left( \alpha _ { 0 } - a _ { 2 } \right) - \left( a _ { 1 } - a _ { 3 } \right) \omega _ { \circ }$ ，第(3)步执行结果为 $b _ { 0 } = c _ { 0 } , b _ { 3 } = c _ { 3 } , b _ { 1 } = c _ { 2 } , b _ { 2 }$ $\mathbf { \lambda } = \mathbf { \lambda } _ { C 1 }$ ,其中计算 $b _ { 1 } = c _ { 2 }$ 和 $\boldsymbol { b } _ { 2 } = \boldsymbol { c } _ { 1 }$ 时处于对角的处理器要进行通信。□

算法分析算法11.3的第(1)步是局部复制，只需取常数时间，且无须选路；算法的第(2)步既需要复数计算又需要选路;算法的第(3)步是位序调整只需选路。下面分析这两类操作的时间：

$\textcircled{1}$ 计算时间 $t _ { \mathfrak { c } }$ ：算法的第(2)步中包含了 ${ } + { } , { } - { } , { } \times { } ,$ ÷和指数运算，其中最费时间的是指数操作，根据Procedure COMPUTE的分析，可知其时间复杂度为 $O ( \log n )$

$\textcircled{2}$ 选路时间 ${ \pmb t } _ { \mathbf { r } }$ :通信主要发生在第(2.4)步和第(3)步。在第(2.4)步时，如果 $k \mathrm { m o d } \ p = k \mathrm { m o d } 2 \ p$ ，则 $\mathbf { P } _ { k }$ 需要接收来自 $\mathrm { P } _ { k + p }$ 中的 $c _ { k + \ p }$ ,然后再将 $c _ { k + \ p }$ 返回给 $\boldsymbol { \mathrm { P } } _ { k + \ p }$ 。此选路所需的时间与 $\pmb { h }$ 的值有关：当 $\pmb { h } = 0 , \pmb { \phi } = 1$ 时,通信只发生在同行中那些下标差1的处理器间,所以选路步距为1;当 $h = 1 , \phi = 2$ 时,通信只发生在同行中那些下标差2的处理器间,所以选路步距为2;按此类推，当 $h = \log n ^ { \mathrm { ~ - ~ } }$ $1 , \beta ^ { = } n / 2$ 时,通信只发生在同列中那些下标差 $\sqrt { n } / 2$ 的处理器间，所以选路步距为 $\sqrt { n } / 2$ 。一般而言,对于 $\pmb { \hat { p } } = 2 ^ { h }$ ，当 $h = 2 s - 1 , 2 s - 2 , \cdots , 0$ 时,其选路步距为 $2 ^ { h \ m o d s }$ 。所以算法第(2)步的总的选路步距为 $2 { \big ( } 1 + 2 + 4 + \cdots + 2 ^ { s - 1 } { \big ) } = 2 { \big ( } 2 ^ { s }$ $- 1 ) = O ( { \sqrt { n } } )$ 。在第(3)步时，通信发生在 $\mathrm { \bf P } _ { k }$ 和 $\mathbf { P } _ { r ( k ) }$ 之间,其最远者为两个对角处的处理器 $\mathbf { P } _ { 2 } { \boldsymbol { \mathsf { \Pi } } } ^ { \bullet - 1 }$ 和 $P _ { 2 ^ { ' } ( 2 ^ { ' } - 1 ) }$ 之间，所以选路步距为 $2 ( 2 ^ { s } - 1 ) = O ( { \sqrt { n } } )$ 。所以算法11.3总选路时间为 $O ( { \sqrt { n } } )$ 。当 $\pmb { n }$ 充分大时,显然选路时间占主导地位。

# 11.3.2 SIMD-BF上FFT算法

蝶形网络上FFT系数矩阵的计算一个 $n = 2 ^ { k }$ 的蝶形网络(简记为BF)有$( k + 1 ) 2 ^ { k }$ 个节点,布局成 $( k + 1 )$ 行，每行有 $\pmb { n }$ 节点。令 $( r , i )$ 表示第 $_ r$ 行和第 $_ i$ 列的坐标， $\scriptstyle 0 \leqslant i \leqslant n - 1 , 0 \leqslant r \leqslant k { \mathrm { ~ } } ; \exp ( r , i )$ 表示在BF中坐标点 $( r , i )$ 处的 $\pmb { \omega }$ 之指数，它等于字长为 $\pmb { k }$ 的整数 $j$ ，即 $\mathbf { e x p } ( r , i ) = j$ ，使得如果 $\dot { \pmb { \imath } }$ 的二进制表示为$a _ { 1 } a _ { 2 } \cdots a _ { r - 1 } a _ { r } \cdots a _ { k }$ ，则 $j$ 的二进制为 $\mathbf { \alpha } _ { a , a _ { r - 1 } } \cdots \mathbf { \alpha } _ { a _ { 1 } } \mathbf { \alpha } _ { 0 0 } \cdots \mathbf { \alpha } _ { 0 } \mathbf { \alpha } _ { \mathrm { ~ < ~ } }$ ，也就是说，将 $\pmb { i }$ 的前 $\pmb { r }$ 位取位反(即倒序),后面其余位补零就可以得到 $j$ 。例如， $\mathbf { e x p } ( r , i ) = \mathbf { e x p } ($ 3,3)$= j = 6 , \exp ( 2 , 7 ) = j = 6$ 等。所以在BF中作 FFT计算时,可将 $\omega ^ { \mathrm { e x p } ( r , i ) }$ 想像为$\mathbb { P } _ { ( } r , i )$ 中保留的系数。图11.6为 $\pmb { n } = \pmb { 8 }$ 的蝶形网络与相应的FFT系数矩阵元素的分布图。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0005_pages_0281-0350/auto/images/0e454dc3bd5ed88a980d4014baf798c5271587345570f04b65bbc0c7509a213a.jpg)  
图11.6 $\pmb { n = 8 }$ 的蝶形网络及其8点FFT系数分布

算法描述假定系数 $\omega ^ { \mathrm { e x p } \left( r , i \right) }$ 已按图11.6方式分布在网络的各处理器$\mathbf { P } _ { \{ \} } r , i )$ 中;开始时,序列 $( a _ { 0 } , \cdots , a _ { n - 1 } )$ 并行地向第0行加载到各处理器中使得doi=ai;然后在网络中逐行计算dr之值;最终dki就是b;,其中j=exp(k,i),i和 $\pmb { j }$ 的二进制位互为位反。蝶形网上FFT算法的形式描述如下：

算法11.4 SIMD-BF上FFT算法 输入: ao,a1,…,an-1

输出： $b _ { 0 } , b _ { 1 } , \cdots , b _ { n - 1 }$

# Begin

(1）for $\mathbf { \nabla } _ { i } = \mathbf { 0 }$ to $\pmb { n } - 1$ par-do $\big / \ast$ 初始加载 $\yen 7$ $d _ { 0 i } = a _ { i }$ endfor

(2）for $r = 1$ to $\log n$ do $\nearrow$ 计算 $d _ { r , i } \ast /$ for所有仅第 $\pmb { r }$ 位不同且 $\pmb { i }$ 在第 $\boldsymbol { r }$ 位 ${ \bf \Pi } = \bf { 0 }$ 的每对 $( i , j ) \mathbf { P a r - d o }$ $\begin{array} { r } { ( 2 . 1 ) d _ { r , i } = d _ { r - 1 , i } + \omega ^ { \exp ( r , i ) } d _ { r - 1 , j } } \\ { ( 2 . 2 ) d _ { r , j } = d _ { r - 1 , i } + \omega ^ { \exp ( r , j ) } d _ { r - 1 , j } } \end{array}$

# end for

(3）for ${ \bf { \sigma } } _ { i } = { \bf { 0 } }$ to $\pmb { n } - 1$ par-do $\big / \ast$ 调整位序 $\yen 7$ (3.1)计算 $\exp ( k , i ) = j$ (3 $\begin{array} { l } { { \dots 2 ) c _ { j } = d _ { k i } } } \\ { { \dots 3 ) b _ { i } = c _ { r ( j ) } } } \end{array}$ end for

End

算法分析因为蝶形网络第 $\boldsymbol { r } - 1$ 行和第 $r$ 行之间的连接,正好能满足直接将 $d _ { r - 1 }$ ,i和 $d _ { r - 1 , j }$ 传到 $\mathbf { \delta P } _ { ( } r , j )$ 和 $\mathbf { P } ( r , j )$ ,所以无需考虑选路时间。至于计算时间，除了计算 $\omega ^ { \tt e x p ( \boldsymbol { r } , i ) }$ 的时间外,主要是算法第(2)步进行复数运算的时间,它等于 $O ( \log n )$ ,显然优于 SIMD - $\mathbf { M C } ^ { 2 }$ 上的 FFT算法,这也说明算法和体系结构的密切关系。

# 11.3.3 SIMD-CC上FFT算法

对于立方连接的SIMD机器，我们可用n/2个处理器来计算n点FFT。例如对于图11.7所示的16点FFT,可用8个处理器并行计算之，图11.8给出了这种计算过程：开始时P存在a与ak+n/2(0≤k<n/2)，然后逐级展开计算。整个计算需要logn步，每一步中，各处理器实现图11.7(b)所示的蝶式计算。在图11.8中,逐级使用立方连接函数C2、C和Co来传递各次蝶式计算结果中的一个数据。在整个计算过程中,有log(n/2)次并行数据传输。由于立方连接正好满足并行传输数据的要求，所以无需额外的选路时间。

如果用n/4个处理器来计算n点FFT,可将原两个处理器中并行执行的一对蝶式计算，合并成由一个处理器串行地执行两个蝶式计算。这样执行时间延长为2logn,而数据传输次数为2log(n/4)。一般而言,若用n/2个处理器来计算n点FFT(2≤k≤logn），则每个处理器最初应存人2个输人元素，要执行

$2 ^ { k - 1 } \log { n }$ 个并行蝶式计算步,而立方连接函数 $C _ { i }$ 要重复 $2 ^ { k - 1 }$ 次 $( 0 { \leqslant } k { \leqslant } \log n ^ { - }$ $k - 1 )$ ,总的并行数据传输次数为 $2 ^ { k - 1 } ( \log n - k )$ 次。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0005_pages_0281-0350/auto/images/77e1854a560505676b239fa5b9c1ab4b028c7c0222fe1960aef69be2edd9928e.jpg)  
16点FFT

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0005_pages_0281-0350/auto/images/7debfeaef29b352947fc3bc97e0f11250c10dec75dc60c80a3eaa4e9971c93e3.jpg)  
图11.7（a)16点FFT计算流图;(b)蝶式计算  
图11.88个立方连接的处理器上16点FFT的计算

# 11.3.4 MIMD-DM上FFT算法

Cormen迭代串行FFT算法Cormen算法是另一种形式的迭代算法，和算法11.1主要差别是,先将输入序列进行位反置换,从而输出序列就不需要进行位序调整了。

算法11.5 SISD上Cormen迭代计算 FFT算法

输入： ao,a1,.,an -1  
输出：bo,b1,.,bn -1

Begin

（1）REVERSE $( a , a ^ { \prime } ) \ / * a ^ { \prime }$ 为 $_ { a }$ 的位反序列 $\yen 7$   
(2） for $\pmb { s } = \pmb { 1 }$ to $\log n$ do(2.1) $m = 2 ^ { s }$ (2.2) $\omega = \mathrm { e } ^ { 2 \pi \mathrm { i } / m }$ (2.3) $z = 1$ (2.4) for ${ \bf { j } } = { \bf { 0 } }$ to $m / 2 - 1$ do(i) for $k = j$ to $\pmb { n } - 1$ step $\pmb { m }$ do$\begin{array} { l } { v = z a ^ { ' } _ { k } + m / 2 } \\ { u = a ^ { ' } _ { k } } \\ { b _ { k } = u + v } \\ { b _ { k + m / 2 } = u - v } \end{array}$ endfor（ii） $\mathfrak { z } = \mathfrak { z } \cdot \mathfrak { \omega }$ endfor

endfor

End

一个 $\pmb { n = 8 }$ 的 Cormen FFT 计算流图如图11.9所示。

超立方多计算机上Cormen算法假定要在 $\pmb { \phi }$ 个处理器的超立方上计算 $\pmb { n }$ 点FFT。参照图11.10,算法可分为三步：第一步,将输入序列进行位反置换操作,每个处理器都必须计算输入元素的目的处理器号和它在输出序列中的位序号；第二步,各处理器执行log(n/p）次各自相应的FFT蝶式计算,此时处理器间不需通信；第三步，各处理器执行logp次各自的蝶式计算，此时处理器间需要进行通信。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0005_pages_0281-0350/auto/images/29ac50c47d01ff3de497685a7c474c37e0e833624c736f32abcb8928c135ae15.jpg)  
图11.9Cormen8点FFT计算流图

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0005_pages_0281-0350/auto/images/c351052132e11b4bfbe44db115e1538356f251f2281d7e1d658483df75e964c2.jpg)  
图11.10 ${ \mathfrak { n } } = 1 6 , { \mathfrak { p } } = 4$ 的FFT计算流图

# 算法11.6 超立方上FFT算法

输入： ao,a1an-1

输出：bo,b1.bn-1

#

(1） for all $\mathrm { \bf P } _ { i }$ , where $0 \leqslant i < \phi$ do $\nearrow$ 计算输人元素位反 $\star$ /for $k = 0$ to $n / \phi - 1$ do

$\mathbf { i d } = i ( n / p ) + k$ dest. processor $=$ REVERSE(id)/(n /p) dest. offset $\mathbf { \simeq }$ REVERSE( id)mod(n /p) $[ \mathrm { d e s t . p r o c e s s o r } ] b _ { \mathrm { d e s t . o f f s e t } } { \Leftarrow } a _ { k }$ end for end for

(2) for $s = 1$ to $\log ( n / \beta )$ do $\big / \big \varkappa$ 无通信要求的迭代计算 (2.1) $m = 2 ^ { s }$ (2.2)ω=e2ri/m (2.3) for all $\mathrm { \bf P } _ { i }$ , where $0 \leqslant i < \pmb { \mathscr { p } }$ do (i) $z = 1$ (ii） for $j = 0$ to $m / 2 - 1$ do for $k = j$ to $n / p - 1$ step $\pmb { m }$ do $\begin{array} { l } { q = z b _ { k } + _ { m } / 2 } \\ { r = b _ { k } } \\ { b _ { k } = r + q } \\ { b _ { k + m / 2 } = r - q } \end{array}$ endfor $z = z \cdot \omega _ { \mathrm { \Delta } }$ endfor endfor endfor

#

(3）for $s = 1$ to $\log \phi$ do $\big / \ast$ 有通信要求的迭代计算 $\star$ / (3.1) $m = 2 ^ { s + \log ( n / p ) }$ (3.2) $\omega = \mathrm { e } ^ { 2 \pi \mathrm { i } / m }$ (3.3) for all $\mathbf { P } _ { i }$ ，where $0 \leqslant i < \phi$ do (i) if $i / 2 ^ { s - 1 }$ 是奇数 then $\begin{array} { l } { { \mathrm { p o s } = \left( i \times { \frac { n } { \hbar } } \right) { \bmod { \mathit { m } } } / 2 } } \\ { { z = { \mathrm { e } } ^ { 2 \left( \mathrm { p o s } \right) \pi { \mathrm { i } } / m } } } \end{array}$ for $\mathbf { j } = \mathbf { 0 }$ to $n / p - 1$ do $\begin{array} { l } { { t _ { j } = z \cdot b _ { j } } } \\ { { \ z = z \cdot \omega } } \end{array}$ endfor endif

（ii） $\mathrm { s h i f t } = 2 ^ { s - 1 }$ (i） partner= kshift(iv） if $i / 2 ^ { s - 1 }$ 是奇数then$\left[ \mathrm { p a r t n e r } \right] u \Leftarrow { t }$ else$[ \mathrm { p a r t n e r } ] u \Leftarrow b$ endifendfor(3.4） for all $\mathbf { P } _ { i }$ , where $\mathbf { 0 } { \leqslant } i < \mathbf { \mathit { p } }$ doif $i / 2 ^ { s - 1 }$ 是奇数thenfor $j = 0$ to $n / \phi - 1$ do$\pmb { b } _ { j } = \pmb { u } _ { j } - \pmb { t } _ { j }$ endforelsefor $j = 0$ to $n / p - 1$ do$\begin{array} { r } { \pmb { b } _ { j } = \pmb { b } _ { j } + \pmb { u } _ { j } } \end{array}$ endforendifendforendford

# 11.4 小结和导读

小结本章所讨论的快速傅里叶变换是一类最重要的快速离散变换，此类变换还有数论变换、多项式变换、卷积和滤波等。其中，数论变换物理意义欠弱，所以应用尚不甚广泛；而卷积与滤波计算在数字信号处理中应用得十分广泛，因为许多数字信号处理问题都要求高速滤波能力（所谓滤波实际上是指将某些输人序列进行变换，使其具有某些预定的性质)。但本书限于篇幅就不再讨论它们了。

此外,本章所讨论的FFT算法是基－2FFT算法，即将输人序列分为奇数下标和偶数下标两个n/2点的序列进行递归计算。工程实用中，还常用到基一4FFT算法，即将输入序列分成四个n/4点的序列进行递归计算，其计算量（乘法和加法)比基-2算法有所减少。如果n不是单一基的幂，则可以试用混合基算法,要是算法设计得当，则可望达到最佳效果。同样限于篇幅,本章也不予以

讨论。

最后,本章所讨论的FFT算法是一维 FFT算法,如果输人元素是 $a _ { n _ { 1 } , n _ { 2 } }$ 形式的二维复序列，则可相应地定义二维FFT变换,它在光学、地震以及图像信号处理等方面起着重要的作用。也是限于篇幅,不再予以讨论。

导读快速离散傅氏变换FFT最原始的文章是[53]。在计算机科学的教科书中，介绍串行FFT算法者很多,较早的有[7]、[20]和[54]等。专门介绍快速傅氏变换和卷积算法的著作可参见[132]。在国内科技著作中，介绍傅氏变换并行算法的,主要可参考[191]、[201]和[195],[190]中还专门讨论了VLSI阵列中的卷积、滤波和傅氏变换等并行算法。至于FFT算法在超立方多计算机和向量多处理器上的并行实现,读者可参阅[172]、在商用MIMD机器上的并行算法可参阅[19]和在Transputer网络上的并行算法可参阅[99]等。

# 习 题

11.1试计算下述序列的 DFT:

(a)(13,17,19,23) (b)(2,1,3,7,5,4,0,6)

11.2试计算下述序列的逆 DFT:

(a）（ $1 6 , \cdot 0 . 7 6 + 8 . 6 6 \mathrm { i } , - 6 + 6 \mathrm { i } , - 9 . 2 5 + 2 . 6 6 \mathrm { i } , 0 , - 9 . 2 5 - 2 . 6 6 \mathrm { i } , - 6 - 6 \mathrm { i } , - 0 . 7 6$ -8.66i)  
（b） $( 4 - \mathrm { i } , 2 + \mathrm { i } , 2 + \mathrm { i } , - \mathrm { i } , 4 - \mathrm { i } , 2 + \mathrm { i } , 2 + \mathrm { i } , - \mathrm { i } )$

11.3给定两个 $\pmb { n } - 1$ 阶多项式 $f ( x ) = \sum _ { j = 0 } ^ { n - 1 } a _ { j } x ^ { j }$ 和 $g ( x ) = \sum _ { k = 0 } ^ { n - 1 } c _ { k } x ^ { k }$ ,可以利用FFT变换及其逆变换来计算两个两项式的乘积 $h = f \cdot g$ ,其步骤如下：

$\textcircled{1}$ 令 $N$ 是大于等于 $2 n - 1$ 的2的方幂的最小整数,在序列 $( a _ { 0 } , \cdots , a _ { n - 1 } )$ 和 $( c _ { 0 } , \cdots ,$ $c _ { n - 1 } )$ 之后各补上 $N - n$ 个零；  
$\textcircled{2}$ 计算 $( a _ { 0 } , \cdots , a _ { n - 1 } , 0 , \cdots , 0 )$ 的FFT,得到多项式 $f$ 在单位 $N$ 次根之值；  
$\textcircled{3}$ 计算 $( c _ { 0 } , \cdots , c _ { n - 1 } , 0 , \cdots , 0 )$ 的FFT,得到多项式 $\pmb { g }$ 在单位 $N$ 次根之值；  
$\textcircled{4}$ 计算 $f ( \omega ^ { j } ) \times g ( \omega ^ { j } )$ 之积 $( j = 0 , 1 , \cdots , N - 1 )$ ,其中 $\scriptstyle \omega = e ^ { 2 \pi i / N }$ 所得之结果就是多项式$\pmb { h }$ 在单位 $N$ 次根之值；  
$\textcircled{5}$ 计算序列 $( f ( \omega ^ { 0 } ) g ( \omega ^ { 0 } ) , f ( \omega ^ { 1 } ) g ( \omega ^ { 1 } ) , \cdots , f ( \omega ^ { N - 1 } ) g ( \omega ^ { N - 1 } ) )$ 的逆FFT,所得之序列就是多项式 $\pmb { h }$ 的系数。按此方法，给定下述多项式对,试计算其乘积 $h ( x )$ ：(a) $f ( \mathbf { \Psi } _ { x } ) = 3 x - 2 , g ( \mathbf { \Psi } _ { x } ) = 4 x + 1$ (b) $f ( x ) = 2 x ^ { 3 } - 4 x ^ { 2 } + 5 x - 1 , g ( x ) = x ^ { 3 } + 2 x ^ { 2 } + 3 x + 2$

11.4根据离散傅氏变换蝶式计算规则,参照图11.2画出 $n = 1 6$ 的离散傅氏变换蝶式计算流图。

11.5参照算法11.1,设计一个单处理机上时间为 $O ( n \log n )$ 的离散傅氏逆变换算法；并以$\pmb { n = 8 }$ 为例，画出其逆变换蝶式计算流图。

11.6参照图11.8,画出4个处理器立方网络上16点FFT的计算流图。

11.7Cormen 曾给了另一种形式的FFT递归算法11.7:

(a)试分析此算法的执行过程；  
(b)它和算法11.2有何区别？  
(c)按此算法画出 $\pmb { n = 8 }$ 的FFT蝶式计算流图。

算法11.7 SISD上 Cormen 计算 FFT算法输入： $a _ { 0 } , a _ { 1 } , \cdots , a _ { n - 1 }$ 输出： $b _ { 0 } , b _ { 1 } , \cdots , b _ { n - 1 }$

Begin

if $\pmb { n } = 1$ then return a   
else   
(1） ω= 2i/n   
(2) x=1   
(3） ${ \pmb a } ^ { [ 0 ] } = ( a _ { 0 } , a _ { 2 } , \cdots , a _ { n - 2 } )$   
(4) ${ \pmb a } ^ { [ 1 ] } = ( a _ { 1 } , a _ { 3 } , \cdots , a _ { n - 1 } )$   
（5） $\pmb { b } ^ { [ 0 ] } = \mathrm { R E C U R S I V E F F T } ( \pmb { a } ^ { [ 0 ] } )$   
（6） $\pmb { b } ^ { [ 1 ] } = \mathrm { R E C U R S I V E F F T } ( \pmb { a } ^ { [ 1 ] } )$   
（7） $\operatorname { f o r } \ k = 0 \ \tan { \frac { n } { 2 } } - 1 \ \mathrm { d o }$ (i) $b _ { k } = b _ { k } ^ { \{ 0 \} } + z b _ { k } ^ { \{ 1 \} }$ (i) $b _ { k } + { \frac { n } { 2 } } = b _ { k } ^ { [ 0 ] } - z b _ { k } ^ { [ 1 ] }$ (ii） $\ z = z \cdot \omega$ endfor

(8）return $\pmb { b }$

# endif

End

11.8以 $\scriptstyle n = 1 6 , p = 4$ 为例,逐步写出算法11.6的执行过程。

11.9根据算法11.2,逐步计算 $\pmb { n = 8 }$ 的 FFT,并画出其蝶式计算流图。

11.10令 $\pmb { n } = \pmb { 8 } = 2 ^ { k }$ ，在蝶式网络上,按照 $\exp ( r , i ) = j \left( 0 { \leqslant } i { \leqslant } n - 1 , 0 { \leqslant } r { \leqslant } k \right)$ 的计算方法，试计算分布在蝶形网络中的8点FFT的系数矩阵元素 $\omega ^ { j }$ 。

# 第四篇 并行程序设计

第十二章 并行程序设计基础  
第十三章 并行程序设计模型和共享存储系统编程  
第十四章 分布存储系统并行编程  
第十五章 并行程序设计环境与工具

这一篇主要研究并行程序设计,包括并行程序设计基础(第十二章),并行程序设计模型和共享存储系统编程(第十三章),分布存储系统并行编程(第十四章)和并行程序设计环境与工具(第十五章)。这一篇内容足以构成单独的一门课程,但是作为并行计算的一大部分内容之一，只能从实用的角度出发，围绕着如何进行并行编程来开展讨论。特别是本篇介绍并行程序设计语言时只是着重原理和方法而不能作为手册使用。

本篇第十二章主要讨论并行程序中的进程和线程等基本概念以及相关的同步机制和通信操作。第十三章主要介绍隐式并行、数据并行、消息传递和共享变量四种并行程序设计模型;同时讨论了X3H5、POSIX和OpenMP三种共享存储的编程标准。第十四章着重讨论了分布存储系统的消息传递和数据并行编程，介绍了MPI、PVM和HPF三种主要语言标准及其一些编程实例。第十五章先从一般的软件工具环境讲起,然后重点介绍并行程序设计语言并行编译器以及并行程序的调试工具、性能分析工具和可视化设计工具。

# 第十二章 并行程序设计基础

一个有实际应用的并行算法，最终总要在并行机上实现,为此首先就要将并行算法转化为并行程序,此过程就是所谓的并行程序设计（Paralel Program-ming)。它要求算法设计者、系统结构师和软件工作者广泛频繁的交互。因为设计并行程序涉及到的知识面较广，所以必须首先学习一下有关并行程序设计的若干基础知识,主要包括操作系统中的有关知识和优化编译方面的知识。本章先讨论前者,后者放在第十五章中讨论。操作系统内容非常丰富，在此只讨论并行程序中最基本的计算要素如任务、进程、线程等基本概念、同步机制和通信操作等。

# 12.1 并行程序设计概述

目前并行程序设计的状况是： $\textcircled{1}$ 并行软件的发展落后于并行硬件； $\textcircled{2}$ 和串行系统与应用软件相比,现今的并行系统与应用软件甚少且不成熟； $\textcircled{3}$ 并行软件的缺乏是发展并行计算的主要障碍； $\textcircled{4}$ 不幸的是，这种状态似乎仍在继续着。究其原因是并行程序设计远比串行程序设计复杂： $\textcircled{1}$ 并行程序设计不但包含了串行程序设计,而且还包含了更多的富有挑战性的问题； $\textcircled{2}$ 串行程序设计仅有一个普遍被接受的冯·诺依曼计算模型,而并行计算模型虽有好多,但没有一个可被共同认可的像冯·诺依曼那样的优秀模型； $\textcircled{3}$ 并行程序设计对环境工具(如编译、查错等)的要求远比串行程序设计先进得多;④串行程序设计比较适合于自然习惯,且人们在过去积累了大量的编程知识、经验和宝贵的软件财富。下面我们从应用的观点,来比较一下串行程序设计和并行程序设计。

# 12.1.1串行程序设计与并行程序设计

串行程序设计(Sequential Programming）对于所希望的应用,很多串行源代码均是有的,用户只需要在目标机上重新编译运行一下即可;即使对于待开发的应用,用户也能很容易找到适合其目的的现有算法，纵然找不到现有的算法，用户也可借助于某些程序设计工具来解决。

串行程序设计的优点是：①长期以来，已建立了很多算法范例，它们可以指导用户设计算法;②程序设计是建立在唯一的、普遍使用的、适用于各种程序设计语言的冯·诺依曼编程模型之上的； $\textcircled{3}$ 虽然已有很多串行语言，但形成标准的只有适合科学计算的Fortran语言，商用的Cobol语言和通用的C语言等为数不多的几种； $\textcircled{4}$ 串行程序设计工具是通用的和稳定的：例如C语言能支持所有的算法范例和运行在任何串行计算机上，而且屡经数代这些工具依然不变。C语言发明已经20多年至今变化甚微;冯·诺依曼模型已经历时40多年并无本质变化。特别是这些工具都已多年经不同的应用、在不同的计算机平台上屡经测试而变得成熟,人们已经学会在使用中如何将其扬长避短。

并行程序设计(Parallel Programming） 对于所希望的应用,很多并行代码似乎是不存在的;即使有,也常不能用于用户的并行机上,因为并行代码原来都是为不同的并行结构(如 SMP、MPP等)而写的。

并行程序设计的问题是： $\textcircled{1}$ 并行算法范例至今尚不能被很好地理解和广泛地接受； $\textcircled{2}$ 并行程序的设计是建立在不同的计算模型上的，而它们没有谁能像冯·诺依曼模型那样被普遍的接受和认可； $\textcircled{3}$ 绝大部分被使用的并行程序设计语言都是Fortran和C的推广，它们都不能充分地表达不同并行结构的特点，既不成熟也不通用; $\textcircled{4}$ 并行程序设计工具依赖于具体的并行结构和计算机代的更迭，既不通用也不稳定,在某个并行平台上开发的并行程序,很难移植到别的或将来的并行机上。

有关串行程序设计和并行程序设计的比较可概括于表12.1中。

表12.1串行程序设计和并行程序设计比较一览表  

<table><tr><td rowspan=2 colspan=1>应用领域</td><td rowspan=1 colspan=2>科学和工程计算,数据处理，商务应用等</td></tr><tr><td rowspan=1 colspan=1>串行程序设计</td><td rowspan=1 colspan=1>并行程序设计</td></tr><tr><td rowspan=1 colspan=1>算法范例</td><td rowspan=1 colspan=1>分而治之，分枝限界，动态规划,回溯，贪心</td><td rowspan=1 colspan=1>计算交互、工作池、异步迭代、流水线、主-从,细胞自动机</td></tr><tr><td rowspan=1 colspan=1>编程模型</td><td rowspan=1 colspan=1>冯·诺依曼模型</td><td rowspan=1 colspan=1>隐式并行、数据并行、共享变量、消息传递</td></tr><tr><td rowspan=1 colspan=1>编 程语言</td><td rowspan=1 colspan=1>Fortran,C,Cobol,4GL</td><td rowspan=1 colspan=1>KAP、Fortran90、HPF、X3H5、PVM、MPI</td></tr><tr><td rowspan=1 colspan=1>体系结构</td><td rowspan=1 colspan=1>不同类型的单处理机</td><td rowspan=1 colspan=1>共享内存(PVP、SMP、DSM)数据并行(SIMD)消息传递(MPP、Clusters)</td></tr></table>

尽管并行程序设计问题很多,但也有不少进展： $\textcircled{1}$ 已经开发了很多并行算法，虽然它们大多基于理想的PRAM模型，但有些已被实际采用；②少量的并行算法范例已出现,并且正逐渐被接受;③编程类型渐趋汇聚于两类：用于PVP、SMP和DSM的共享变量的单地址空间模型和用于MPP和机群的消息传递的多地址空间模型,SIMD模型已退出主流，但对专用领域(如信号、图像处理，多媒体处理等）仍是有用的； $\textcircled{4}$ 并行编程模型渐趋汇聚于三类标准模型：数据并行（如HPF),消息传递(如 PVM和 MPI)和共享变量(如 ANSI和 X3H5）。

现在人们希望高性能的并行机应是具有单一系统映像的巨大的工作站，使得很多用户都能利用增强的处理能力和存储容量来运行多个串行作业，这就是所谓的串行程序并行系统 SPPS(Serial Program Parallel System）。

# 12.1.2并行程序设计环境

从用户的观点，一个典型的并行处理过程可简述如下：首先开发求解一个应用问题的具体算法；用户或程序员在并行计算模型上用高级语言(串行或并行）编程实现算法;然后编译器将源代码转换成可在并行平台上执行的目标代码；最后借助于OS和硬件平台运行程序。其中，从用户编程到编译源代码和链接（包括源到源转换预处理器)的这一过程统称之为并行程序设计，其间任何程序设计语言都有一个运行支持系统,它就是一组子例程(包括用户代码开始执行的初始化,结束清场,数据对象的分布与再分布等);部分运行支持也可由库函数(Li-braryFunction)提供,它就是一组按照某些规则经过编译后的经常使用的子例程。库可以与语言相关(如C语言的"stdio"库),也可与OS相关(如线程库),也可与语言和平台无关(如MPI库),库函数在程序运行前或在运行时动态地链向用户代码。

编程环境与工具编程工具(Programming Tools)泛指用于帮助用户开发应用问题的任何硬件和一组软件实用程序。工具通常不涉及到OS和程序设计语言，主要包括作业管理工具(如网络排队系统NQS:Network Queueing System和负载共用设施LSF:Load Sharing Facility),查错工具和性能工具等。编程环境,简称为环境(Environment),系由硬件平台、支撑语言、操作系统、软件工具和应用软件包等组成。所谓集成工具(Integrated Tool),在通常意义下系指编辑器、查错器、性能监视器、程序可视化工具等。

# 12.1.3并行程序设计方法

如上所述，现今并行程序设计模型主要有隐式并行、数据并行、消息传递和共享变量等四种。当在实际的并行机上根据它们设计并行程序时，绝大部分均是采用扩展Fortran和C语言的办法。目前有三种扩展的办法：①库函数法：除了串行语言所包含的库函数外，一组新的支持并行性和交互操作的库函数（如MPI消息传递库和POSIXPthreads多线程库)引人到并行程序设计中；②新语言结构法：采用某些新的语言结构来帮助并行程序设计以支持并行性和交互操作（如Fortran 90 中的聚集数组操作）;③编译制导法(CompilerDirectives)：程序设计语言保持不变,但是加进称之为编译制导(Pragmas)的格式注释。

上述三种编程方法的风范示于图12.1中。对于图12.1(a)所示的一个简单代码段,图(b)使用库函数的方法实现之,其中两个循环由 $\pmb { \hat { p } }$ 个进程并行执行,两个库函数 my-process-id()和 number-of-processes()开拓并行性,barrier(）函数确保第一个循环执行后所有进程被同步,这样第二个循环能使用第一个循环更新后的数组 $\pmb { A }$ 的正确值;图 $( \mathbf { c } )$ 展示了使用新语言结构执行并行操作,Fortran90数组赋值结构语句执行 $N$ 个元素相乘,然后以一个赋值语句进行赋值,两个数组赋值之间无需显式同步，因为Fortran90语句是松散同步的,即在下一语句开始执行之前,一条赋值语句的所有操作均已完成；图 $(  { \mathbf d } )$ 例示了编译制导法实现并行操作,并行 pragmas 指示下面语句均要并行执行,SGI的 $\mathfrak { p f o r }$ 指使系统并行执行下一循环，同步 pragma产生路障同步。

$$
\begin{array} { r } { \mathbf { f o r ( i = 0 ; i < N ; i + \Delta + \Delta ) ~ A [ i ] = b [ i ] * b [ i + 1 ] ; } } \\ { \mathbf { f o r ( i = 0 ; i < N ; i + \Delta + \Delta ) ~ C [ i ] = A [ i ] + A [ i + 1 ] ; } } \end{array}
$$

# (a）顺序化码段

id= my- process_id();   
$\mathbf { p } { = }$ number-of - processes();   
${ \bf { f o r } ( \bar { \ t } = i d ; i < N ; i = i + p ) \Delta A [ \bar { \ t } ] = b [ \bar { \ t } ] * b [ \bar { \ t } + 1 ] , }$ barrier()   
${ \bf \ f o r ( i = i d ; i < N ; i = i + p ) \ C [ i ] = A [ i ] + A [ i + 1 ] ; }$

# (b）使用库函数的等效并行代码

my- process-id,number-of--processes(),and barrier() $\mathbf { A } ( \mathbf { 0 } ; \mathbf { N } - \mathbf { 1 } ) = \mathbf { b } ( \mathbf { 0 } ; \mathbf { N } - \mathbf { 1 } ) * \mathbf { b } ( \mathbf { 1 } ; \mathbf { N } )$ $\mathbf { c } { = } \mathbf { A } ( \mathbf { 0 } { : } \mathbf { N } { - } \mathbf { 1 } ) { + } \mathbf { A } ( \mathbf { 1 } { : } \mathbf { N } )$

# (c）使用数组操作 Fortran90等效代码

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0005_pages_0281-0350/auto/images/af69784431d4d0b71c57e0bad848b6334cdd2294295d38e55b5527cb6fa37247.jpg)  
图12.1示例三种并行化方法

三种并行编程方法的优缺点可概括于表12.2中。

表12.2 三种并行编程方法比较一览表  

<table><tr><td rowspan=1 colspan=1>方法</td><td rowspan=1 colspan=1>优点</td><td rowspan=1 colspan=1>缺点</td><td rowspan=1 colspan=1>例子</td></tr><tr><td rowspan=1 colspan=1>库函数</td><td rowspan=1 colspan=1>易于实现,不需要新的编译器</td><td rowspan=1 colspan=1>没有编译检查、分析和优化</td><td rowspan=1 colspan=1>MPI、PVM、Cray Craft</td></tr><tr><td rowspan=1 colspan=1>新结构</td><td rowspan=1 colspan=1>允许编译检查、分析和优化</td><td rowspan=1 colspan=1>难以实现，需要一个新的编译器</td><td rowspan=1 colspan=1>Fortran90、Cray Craft</td></tr><tr><td rowspan=1 colspan=1>制导</td><td rowspan=1 colspan=2>是库函数和新结构两者优缺点的折衷,其显著优点是“普通申行程序+格式注释”,可在任何串行平台上编译</td><td rowspan=1 colspan=1>HPF、Cray Craft</td></tr></table>

# \*12.2进 程

进程 $( \mathrm { P m o c e s s } )$ 是并行程序中的基本计算单位,它对应于由相应代码段所执行的操作。程序就是一些进程的集合。而并行程序设计的基本问题就是围绕着进程的说明、生成、中止、激活、迁移、结束和同步等。在一台并行机上,用户应用程序都是作为进程(任务、线程)被执行的，所以有必要先复习一下进程的有关问题。

# 12.2.1 进程的基本概念

基本定义进程 $\mathbf { P } { = } \left( \mathbf { P } , \mathbf { C } , \mathbf { D } , \mathbf { S } \right)$ 是一个4元组,其中P是程序(即代码)、C是控制状态 $\mathbf { D }$ 是数据状态、S是进程 $\mathbf { P }$ 之状态。任何进程总和程序连系在一起。程序使用两组变量：数据变量保持数值,由程序员说明之;控制变量保持控制流信息，不需显式说明。在任何时刻t,程序的状态由所有成对的(程序变量，值)之集合所定义。进程是动态变化的,在任何时候它会处于某一状态。如图12.2所示，开始时进程处于非存在(Nonexistent)状态;它可由其父进程生成就绪(Ready)状态,然后被调度进人运行(Rumning)状态;当无法继续执行时，它就转人中止(Suspended)状态,以后待机被唤醒可再次进入就绪状态;进程运行中也可被别人抢先或因超时而停止运行,或者就正常结束,或者因异常退出而被废弃。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0005_pages_0281-0350/auto/images/a6e28f65978c98e4400b717c4ac6e599f6597f62a02d5a1f1dd71d2a843b2a21.jpg)  
图12.2进程状态转换图

上述给出的进程概念对只是使用并行语言的用户是合适的,如要具体实现它，尚须涉及到进程执行模式、进程的现场活动、进程描述符和进程控制等诸多方面。

执行模式众所周知,操作系统通常包含核(Kermel)、壳(Shell)和一组实用程序(Utilities)。其中,核直接管理系统资源,处理例外和控制进程;壳称之为命令解释器,是用户和OS的界面;实用程序是附加的OS软件,提供经常使用的诸如编译器、编辑器和调试器等功能。一台计算机执行程序时提供两种执行模式：核模式和用户模式。OS中核执行在核模式(Kermel Mode),核进程在核模式下执行,这些进程由核生成以帮助管理系统资源;OS中的其它程序作为进程执行在用户模式（Us-er Mode),这样的进程称为用户进程。进程的执行模式可以在核与用户模式之间来回转换。机器开始在核模式,初始化系统和生成一些核进程后,核最终将控制传给壳(它是用户进程),它能生成一些附加的用户进程。用户进程执行中也可将执行模式切换到核模式,核完成了所请求的服务后,又能将执行模式返回到用户模式。

活动现场一个进程的活动现场，或称前后关系(Context)是程序状态的一部分,系保留在处理器的寄存器中。现场切换(Context Switch)就是保留现行进程现场,加载新的进程现场的活动过程。当进程执行模式变化时就需要施行现场切换。在切换前,用户进程的现场必须被保存在主存中,当中断处理完毕后,核就恢复用户进程现场，并将控制返回给用户进程而继续执行之。 ；

进程描述符进程的附加信息以某些数据结构保存在核空间中,其最重要者是进程描述符(Prooess Descriptor),它包含了核管理进程的如下信息： $\textcircled{1}$ 进程凭证：如进程标识符、父进程标识符、用户标识符和组标识符等； $\textcircled{2}$ 进程状态：如就绪、运行和中止等； $\textcircled{3}$ 进程现场：保持执行模式切换时的进程现场； $\textcircled{4}$ 存储映射：如各存储段的大小与访问权限、段指针与页表等； $\textcircled{5}$ 各进程信息：如打开文件、接收信号等；$\textcircled{6}$ 全局数据结构：由核管理的所有进程的队列指针和表； $\textcircled{7}$ 进程的控制与管理信息(见下）。

OS将进程描述符分为两部分:其一是各进程(Per-Process)部分,它可从进程用户空间中交换出去;其二是在所有时间均必须驻留在主存中的其它部分。在有的实现中,各进程部分被分配在用户空间,但只能由核访问。

进程控制(Process Control）进程控制是指由核对诸进程进行管理,其主要功能有： $\textcircled{1}$ 进程管理(Process Management):由核使用进程描述符去生成、中止、唤起和结束进程,管理全局数据结构和所有的各个进程的数据结构；②进程保护(Pro-cess Protection)：由核执行全面检查以确保进程只能访问规定的资源。在进程描述符中含有各种进程的权限信息。通常用户进程只能访问其用户空间,而不能访问核空间或别的进程用户空间；③进程调度(Process Scheduling)：由称之为调度器的核程序将处理器、存储器和I/O等资源指派给进程。调度器应是公平、有效的，它可根据进程描述符中所提供的进程优先信息进行调度。所谓有效的调度是指调度开销低的调度。如图12.3所示，调度有单道程序和多道程序之分。如果资源为单一用户所专用,这样的系统称为单用户单任务(Single-User Single-Tasking）系统，即单道程序设计(Uniprogramming)系统(如MicrosoftDOS),其变体方案是允许单用户的多进程同时使用资源，此即所谓的单用户多任务系统(如MicrosoftWin-dows)；如果允许很多用户同时分享系统资源，则这样的系统称为多用户多任务（Multi-UserMulti-Tasking）系统,即多道程序设计(Multiprogramming)系统(如Unix和Windows NT)。资源的共享形式,可取独占(Dedicated)方式(资源不共享）、批处理(Batching)方式(一旦调度运行就执行到完成）、分时(Time-Sharing)方式(轮流交替使用资源)和抢先(Preemptive)方式(高优先权的进程可以抢走低优先度的处理器）。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0005_pages_0281-0350/auto/images/a985fe2de56984ae7ad95d3e4c7ae6b9b8dc978b8c2347368a8d5fb9da12994a.jpg)  
图12.3调度类型

在并行机上有所谓空间共享与时间共享之分：前者是指一个进程指派给一个处理器，或不同的应用指派给不同的处理器集合；后者是指不同应用的多个进程可指派给同一个处理器。同时在并行机上的调度必须考虑到并行进程的交互作用。

进程与线程传统的OS进程具有分开的地址空间,它使得进程的管理非常费时。例如,当Unix进程执行 fork（）系统调用生成一个子进程时,就必须为该子进程生成一个新的地址空间。这就意味着必须分配存储器、数据段和父进程描述符必须复制,必须为该子进程设置运行栈等。这种费时的Unix进程被称为重量级进程(Heavy-Weighted Process)。进程生成与切换的高开销严重影响并行系统的性能，所以重量级进程是不适合于并行机的。为了开拓细粒度的并行性，必须使用轻量级进程(Light-Weighted Process),它的流行名称叫线程(Threads),其与OS进程的主要差别是,在一个重量级OS进程内，可存在多个线程，它们共享相同的进程地址空间。任何线程执行线程生成操作就可生成附加的线程,生成线程比生成重量级进程的开销小得多。用户级线程的生成不涉及到核，但线程的管理(生成、结束和调度等)必须由核或用户级线程库完成。为了统一起见,约定：

任务 $\equiv$ 进程 $\asymp$ 重量级进程 ${ \boldsymbol { \mathbf { \mathit { \sigma } } } } = \boldsymbol { \mathbf { \mathit { \Omega } } } \infty$ 进程。

轻量级进程 $=$ 线程。

# 12.2.2 进程的并行执行

执行方式并行程序中的各个进程如果是同质的(Homogeneous),则诸进程可以单程序多数据 SPMD(Single-Program-Multiple-Data)方式执行,即各个进程作用在不同的数据上但执行相同的代码;如果并行程序中的各个进程是异质的(Heteroge-neous),则它们可以多程序多数据MPMD(Multiple-Program-Multiple-Data)方式执行,即各个进程在不同的数据上执行不同的代码。SPMD程序是单一代码(SingleCode)方式的并行循环(Parallel Loop)结构，即数据并行(Data-Parallel)结构;MPMD程序是多代码(Multiple-Code)方式的并行块(Parallel Block)结构。在文献中,SPMD程序也称为数据并行程序,强调开发数据域中的并行性;MPMD程序常是功能并行(Functional-Parallel)、又称之为任务并行(Task-Parallel)或控制并行(Control-Paral-lel)程序。

并行进程表达对于MPMD程序,可使用并行块表达方式,其形式描述如下：

其中 $\mathbf { s } _ { 1 } \mathbf { s } _ { 2 } \cdots \mathbf { s } _ { n }$ 是组件进程(Component Processes),它们可同时并行执行,但步伐各异彼此独立,当 $\pmb { n }$ 个组件进程都结束时则并行块结束,为了协调各进程须执行特殊的互操作。

对于 SPMD程序,可使用并行循环表达方式,其形式描述如下：

当使用单一代码方法表达parfor $( i = 0 ; i < n ; i + + ) \left\{ \mathbf { f o o } ( i ) \right\}$ 时,用户只须书写如下的一个程序：

$$
\mathrm { \ p i d { = } m y \mathrm { \_ p r o c e s s \mathrm { \_ i d ( \Omega ) } ; } }
$$

numproc $\asymp$ number_ of_ process();

$$
{ \mathrm { f o r } } ( i = { \mathrm { p i d } } ; i < n ; i = i + { \mathrm { n u m p r o c } } ) { \mathrm { f o o } } ( i ) ;
$$

它可被编译成一个可执行程序,然后使用执行命令将其加载到 $\pmb { n }$ 个节点运行之。

对于具有静态并行性(程序的结构和进程数目可在运行前,即在编译、链接、加载时确定)的程序,可以使用上述并行块和并行循环的方式表达;而对于具有动态并行性(进程可在运行时生成和结束)的程序,则可通过分支/汇合(fork/join)之类的操作表达之。例如,下述程序有三个进程,其中A进程为主进程,它在程序开始执行时自动生成：

进程A 进程B 进程C begin begin begin ${ \bf { { Z } } } \colon = { \bf { { 1 } } } \colon$ $\mathrm { \bf f o r k } ( \mathrm { \bf C } )$ ； $\mathrm { Y } _ { \mathrm { : } } = \mathrm { f o o } ( Z ) \mathrm { ; }$ $\mathbf { f o r k } ( \mathbf { B } )$ ； $\mathbf { X } _ { : } = \mathbf { f } _ { \infty } ( Z )$ ； end

$\mathrm { T } _ { \mathbf { \lambda } } = \mathbf { f o o } ( 3 ) \mathrm { : }$ join(C); end output(X + Y) end

进程A执行fork(B)操作生成新进程B,它与A并行执行;进程B依次又生成另一进程C,因为进程B中的输出语句需要进程C计算的Y值,所以在输出语句之前插入一个 $\bf { j o i n } ( C )$ 语句,它强使B等待C结束才能执行输出语句。

进程分配任何并行程序总要在某些数据上执行某些计算（又叫负载，Work-load)。所谓分配(Allcation)就是将数据和负载划分(Partitioning)给诸进程,然后将这些进程映射(Mapping)给处理器(节点)。划分的重要任务就是去选择合适的并行度DOP(Degree Of Parallelism)和粒度(Granularity)。DOP可定义为能同时并行执行的组件进程数;粒度可定义为进程的尺寸，即一个组件进程内总的运算数。并行度和粒度常是互易的：增加粒度尺寸趋向减少并行度;而减少粒度尺寸则趋向增加并行度。此外,在实际并行机中,并行度、通信开销和同步之间通常具有一定的比例关系：增加并行度常导致增加开销;而减少并行度则趋向减少开销。

分配有隐式和显式之分：显式分配,用户必须明确指定如何分配数据和负载；隐式分配，此任务由编译和运行系统完成。在SMP中，共同的方法是将数据驻留在中央共享存储器中,使得所有进程均可访问,负载被静态或动态地分发给诸进程,当一进程分得一批负载时，它就从共享存储器中取得所需数据。在分布存储系统中,流行的方法是属主-计算(Owner-Compute)规则：即数据首先分配给进程，当变量 $_ { x }$ 分配给进程P时,P就称之为 $_ { x }$ 的属主，由 $\mathbf { P }$ 执行与 $_ { \pmb { x } }$ 相关的计算。

# 12.2.3进程的相互作用

进程间的相互操作表现为三种形式：通信、同步和聚集(Aggregation)。

通信进程之间传递数据称之为通信。在共享存储的程序中,它可通过读/写共享变量的方法实现之；在fork操作中，子进程和父进程可通过参数传递方法实现通信;在分布存储的程序中,它可使用消息传递的办法进行交换数据。

同步同步使进程之间相互等待。同步操作一般有三种：①原子性(Atomici-ty),是指一系列不可分割的操作，例如

$$
\begin{array} { r l } & { \mathrm { p a r f o r } \ ( \ i = 1 ; i < n ; i + + ) \big \{ \qquad } \\ & { \qquad \mathrm { a t o m i c } \big \} x = x + 1 ; y = y - 1 ; \big \} } \\ & { \qquad \mathrm { i } } \end{array}
$$

其中atomic确保每个进程都必须将两个赋值语句作为不可分离的原子操作来执行；②控制同步，使进程的所有操作均必须等待到达某一控制状态。路障(Barrier)同步就属控制同步，例如

$$
\mathrm { p a r f o r } \ ( \it { i } = 1 ; \it { i } < \it { n } ; \it { i } + \it { + } \ ) \left\{ \begin{array} { r l } \end{array} \right.
$$

Pbarrier$\mathbf { Q } _ { i }$ 一

其中 barrier 确保 $\mathrm { P } _ { i }$ 执行完毕达到barrier后,它必须等待所有其它进程也到达barrier时才能继续。另一种控制同步是临界区(Critical),例如

$\mathrm { p a r f o r } \ ( \it { i } = 1 ; \it { i } < \it { n } ; \it { i } + \it { + } \ ) \left\{ \begin{array} { r l } \end{array} \right.$ ${ \mathrm { c r i t i c a l } } \{ x = x + 1 ; y = y - 1 ; \}$

临界区操作实际上是一种互斥操作,critical只允许一次仅一个进程执行两条赋值语句； $\textcircled{3}$ 数据同步，使程序执行必须等待到达某一数据状态。锁 $\mathbf { ( ~ L o c k s ) }$ 、条件临界区(Conditional Critical Regions)、监视器(Monitors)和事件(Events)等均属数据同步,例如

$\operatorname { p a r f o r } ( i = 1 ; i < n ; i + + ) \left\{ \operatorname { l o c k } ( s ) ; x = x + 1 ; y = y - 1 ; \operatorname { m l o c k } ( s ) ; \right\}$ 其中 $\mathbf { l o c k }$ 同步依赖于信号量s之数据状态。

聚集聚集将并行程序中的各进程所计算之局部结果汇总起来以产生一个完整的结果,它实际上也是进程相互通信的一种形式。求全和、前缀和（ $( \mathrm { P r e f i x } )$ 和归约(Reduction)等均属聚集操作,例如

parfor $\scriptstyle \cdot ( i = 0 ; i < { \dot { n } } ; i + + ) \left\{ \begin{array} { r l } \end{array} \right.$ $\mathbf { X } [ i ] = \mathbf { A } [ i ] * \mathbf { B } [ i ] ;$ inner_ product: $=$ aggregate _sum(X[ i]);  
一

其中 aggregate_sum归并部分结果 X[0],X[1],…,X[n-1]以产生最终内积 X[0]$+ \mathbf { X } [ 1 ] + \cdots + \mathbf { X } [ n - 1 ] _ { \circ }$

通信的模式有多种：包括点到点、播送、散播(Scatter)、收集(Gather)、全交换、归约和前缀和(即 Scan)等。有时把除了点到点以外的其它通信统称之为集合(Collective)通信。

# 12.3线 程

在近代OS研究中的一个关键发明就是线程(Threads)。线程就是能单独执行的计算实体(Entity),它们是些具有某些必要最小状态的轻量级进程,而最小状态包括进程状态和相关寄存器的内容。本节将要简要讨论一下线程的概念、管理与同步。

# 12.3.1线程的基本概念

线程(Threads)是控制流线(Threadof Control)的简称,就是被执行的一个指令序列,其基本概念可图示在图12.4中。Solaris的线程分为两级：运行于用户空间的用户线程和运行于核空间的核线程。工作在核模式下的线程也称之为轻量级进程LWP(Light-WeightProcess)。轻量级线程由核施行管理,在用户级,动态链接的线程库(ThreadLibrary)执行线程应用编程和管理用户线程。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0005_pages_0281-0350/auto/images/cace6c700489cca9bff834214505c52ec15d80504a928a3aed2331b122af48e0.jpg)  
图12.4Solaris操作系统中的多线程

每个进程可有一个或多个线程,进程可以被分配给一个或多个LWP,分配给进程的LWP数目称为进程的并发度。线程库调度进程线运行于LWP池上,就像核调度LWP运行于物理处理器池上一样。线程从进程外是看不到的,进程中线程的号和身份，核是不知道的,核不能管理用户级线程,只能管理LWP。

线程就像进程一样，能执行任何应用代码和系统调用。一个进程的诸线程可共享进程的地址空间,包括它的代码、它的大多数数据和大多数进程描述符信息。各个线程可彼此独立、异步地执行，当一个线程被阻塞时，其它线程可照旧执行，一个进程的多个线程可在多个处理器上同时执行。

因为线程在用户空间中由线程库执行，且进程中的线程勿须分开的地址空间,所以线程操作执行代价比进程的低。又由于线程操作(如生成、结束、同步等)均是在同一用户空间中完成,勿须进人核状态,所以因复制、现场切换、边界交叉保护等进程操作而引起的开销亦将大大降低。

# 12.3.2线程的管理

线程生成（Thread Creation）生成线程比生成进程要简单得多，因为无需生成新的地址空间,只需保存该线程所需的一些状态信息：如线程ID、处理器状态(程序计数器、堆栈指针）、线程专用栈、线程优先度、线程局部存储区等。这些信息由线程库以称之为线程结构的数据结构形式来生成和维护。

进程中的变量由进程的所有线程共享。因此，如果某一线程修改了一变量，其后果对进程的所有线程均可见。每个线程也有一局部线程存储区，用以保存该特定线程的私有变量，这不能由其它线程直接访问。

线程调度（ThreadScheduling）线程库提供一个线程调度器去调度LWP池中线程的执行。如图12.5所示，每一线程在任何时刻均处于某一状态。一个新生成的线程开始在可运行状态，它等待一个空闲的LWP到来，然后库调度它运行在LWP上，从而进入了活动状态；一个活动的线程，可被阻塞而进入睡眠状态；当阻塞条件消除时，它又被唤醒而进入可运行状态；当线程支持抢先时，一个优先级高的线程可从活动状态中抢走它的LWP；程序员可以中止一个线程使其进入停止状态；最后，当一个线程结束时，它就进人了“僵尸"(Zombie)状态。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0005_pages_0281-0350/auto/images/bfd5635e9050dfd6d8e2ccceb0a22801db307809a8c3e245ecb3391dc4c4c01b.jpg)  
图12.5线程库控制的线程状态转换图

已如上述，核不能管理用户级线程，只能管理LWP。图12.6示出了由核调度LWP的状态转换图：一个运行的LWP,当被抢先或超时时就转人可运行状态；当执行阻塞系统调用时，运行的LWP被阻塞，强使LWP等待某一条件满足；当执行LWP库函数调用时,LWP被中止而进人中止状态，而执行继续库函数调用时，它又能返回至先前状态；当一个线程结束，或不再有可运行的线程时，LWP就进入空闲状态，它也可被再次唤醒而进人可运行状态。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0005_pages_0281-0350/auto/images/35026fc8cfa748b233609c314aacf4d5721d52abff9c8dfe03171a0cfaf5b6da.jpg)  
图12.6核控制的LWP状态转换图

# 12.3.3线程的同步

Solaris线程库执行两种类型的同步对象：局部进程(Process-Local)和共享进程(Process-Shared)。一个局部进程同步对象,可由同一进程中的线程所访问，它用来同步相同进程中的诸线程;一个共享进程同步对象,可由多个进程所访问,它用来同步不同进程中的诸线程。

在分布式计算环境中,也提供两种类型的线程同步：互斥和条件变量。互斥用来防止多个线程在同一时间访问相同的资源;条件变量常与互斥联合使用。典型的情况是,当一线程需要某一资源时,它就使用互斥排斥其它线程的访问；如果资源无效，线程就根据条件变量等待之，稍后条件满足时就可再启动。

# \*12.4同 步

同步这一术语,在计算机的很多课程(例如系统结构、操作系统、数据库、并行处理和程序设计语言等)中经常出现,其意义和用法也不尽相同,且其实现方法亦颇多，所以有必要专辟一节深人学习之。

一般而言，同步操作,如图12.7所示,可分为三类：原子操作,数据同步和控制同步。所有在共享存储的机器(PVP、SMP、DSM等)上的同步通常使用锁原语实现;在分布存储的机器(MPP和机群等)上的同步使用消息传递原语实现。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0005_pages_0281-0350/auto/images/9d50b5e47136a333c89ec7139d1221fdab7a3f000927cc8c6bd538627ad1e7e4.jpg)  
图12.7同步的不同类型

# 12.4.1原子与互斥

在同步操作中,原子(Atomicity)和互斥(Mutual Exclustion)是两个相关但不同的概念。互斥是指在同一时间、同一地方不能有两件事情存在;原子性是指一个操作序列不能分开执行。临界区(Critical Section)就是按原子操作的一段代码。在临界区内必须使用某种机构确保代码执行的原子性（即操作的相互排斥）。一个互斥问题应满足如下性质：①独占,即一次只允许一个进程在临界区中执行；②前进，即程序必须无死锁或活锁(Livelock);③“得食”,即一个试图执行在临界区中的进程最终必将成功而不会被饿死。一个原子性问题应满足如下性质： $\textcircled{1}$ 有限的，即原子操作从开始到结束的时间应是有限的； $\textcircled{2}$ 不可分的，即原子操作必须作为一个单一的不可分开的执行步，只有原子操作的最终结果是可见的，而任何中间结果均是不可见的； $\textcircled{3}$ 可串行化的，即一些并行执行的原子操作之结果，尤如以任意顺序串行执行的结果。原子操作和互斥操作的主要不同是： $\textcircled{1}$ 原子操作是有限的，但有限性并不是互斥操作的固有性质，例如临界区中可能包含一个由编译或运行支持系统无法检测出的无限循环; $\textcircled{2}$ 互斥强使操作串行执行,但原子性允许并行执行； $\textcircled{3}$ 互斥操作可确保不可分割性,但不可分割性也可由别的、非互斥方法实现。原子性传统上用互斥方法实现,而锁是支持互斥的主流技术，所以锁也就是原子操作。

在并行计算中,虽然仍使用互斥结构(如锁和临界区)作为原子操作的主要支持,但是互斥不是唯一的或最好的达到并行计算应用原子性的方法。有效的、安全的实现并行计算中原子性的方法正在研究中。然而我们必须打破这种观念,即原子性只能够被模拟作一个临界区问题,而临界区要求互斥，因此也要求锁。

# 12.4.2 高级同步结构

现今共享存储的多处理器系统的并行程序设计环境，提供了四种类型的同步原语：事件、路障、锁/信号灯和临界区。事件(Event)操作用于实现产-销(Producer-Consumer)同步;路障(Barrier)用在Barrier同步中;锁和临界区主要用于实现互斥形式的原子性。

信号灯和锁信号灯S是一个非负整数变量,对其能进行两个原子操作 $\mathbf { P }$ (S)和V(S):①P(S)操作用于延迟一个进程直至S变成大于零,然后 S减一;②V(S)操作将 S增一。二元信号灯(Binary Semaphore),S取值为真或假,也称之为锁。相应地,对于锁S其P(S)和V(S)常写作 $\mathbf { l o c k } ( \mathbf { S } )$ 和unlock(S)。锁的普通用法就是通过互斥将临界区转换成原子操作。

锁的副作用锁的主要优点是它已由大多数多处理器支持之,并且已研究得相当深人。锁是一种非常灵活的机制，几乎能实现任何同步。然而互斥锁技术用于实现原子时具有某些严重的缺点，从而导致如下一些问题：①非结构性：锁不是一种结构化的结构，容易用错它，如果lock/unlock语句漏掉或冗余，则编译器不能查出它;②重叠说明(Overspecification)：锁不是用户所真正想要的，它只是达到原子性的一种方法。锁损害了程序的可移植性，且使代码难于理解；③状态相关：锁引人了信号灯S及使用条件原子操作lock(S)，一个进程能否穿过lock(S)依赖于信号灯变量S之值,一般而言，像这样的与状态有关的数据是难于理解的；④顺序执行：对于有些事务处理操作，即使可并行访问,但由于使用锁互斥，它们只能一次执行一个，同样这种顺序执行也不是用户想要的； $\textcircled{5}$ 锁开销：顺序执行 lock(S)和unlock(S)也存在着附加的开销,而且当 $\pmb { n }$ 个进程每个都执行lock(S)操作时,它们中至多一个能成功,其余者均必须重复访问S而再试; $\textcircled{6}$ 优先倒置(Priority Inversion)：当一个保持了高优先进程所需的锁的低优先进程被抢先时，高优先进程并不能前进,因为它被锁锁住了；?护送阻塞(ConvoyingBlocking)：当一个保持锁的进程因缺页或超时被中断时,其它的进程因等待锁不能前进； $\textcircled{8}$ 死锁(Deadlock)：假定两进程P与Q,欲进行X与Y操作：当进程P已为X保持了一把锁并想为Y申请一把锁;而进程Q已为Y保持了一把锁并想为 $\mathbf { X }$ 申请一把锁时,此时没有任何进程在其得到锁之前释放一把锁,结果谁也得不到所要求的锁。

临界区OS所使用的临界区,其语法结构如下：

critical _ region resource$\big / \ast$ 进入点 $\yen 7$ S1 ;S2; ;Sn; $\big / \ast$ 临界区 $\yen 7$ 一 $\nearrow$ 退出点 $\yen 7$

其中,resource代表一组共享变量。所有共享相同资源的临界区必须互斥执行。并行程序设计所使用的临界区作了两点修改：①resource部分不是真正有用的，所以被略去。使用在真正多处理机中的临界区,其语法结构及其等效锁代码表示如下：

$$
\mathsf { S } _ { 1 } ; \mathsf { S } _ { 2 } ; \cdots ; \mathsf { S } _ { n } ;
$$

②多处理机中的临界区变成了锁结构方式,系统自动说明和初始化一个隐含的信号灯S并产生正确的lock/unlock语句。

临界区比锁有很多优点，它是结构化的、与状态无关的，因而易于使用。临界区只是一段被互斥执行的代码，并非必须使用锁。

# 12.4.3低级同步原语

很多多处理机的硬件都能确保单独读/写初等变量的操作的原子性；绝大多数多处理机硬件都提供了某些原子性指令，它们可对初等变量执行单一的读-修改-写操作。本节讨论三种低级同步结构:Test& Set、Compare& Swap、Fetch& Add。

测试并设置(Test& Set） Test & Set(S,temp)是一个原子操作指令，它将共享变量S读入局部变量 temp,然后将S置为1,其主要用途是执行锁功能。兹示例如下：

while(S); $\big / \ast$ 这三行执行 lock(S)操作 $\yen 7$   
Test & Set(S,temp);  
while(temp)Test & Set(S,temp);： $\big / \big \varkappa$ 临界区 $\yen 7$   
$\mathbf { S } = \mathbf { F a l s e } ;$ $/ \star \mathrm { u n l o c k } ( \mathsf { S } ) \star /$

上例中,使用了 Test-and-Set操作执行 $\mathrm { l o c k } ( \mathrm { s } )$ ,其中第一个while循环检查锁 S是否已由别的进程释放。由于每次执行 Test& Set都要写共享变量S,所以可能导至频繁的存储器访问。

比较并交换(Compare & Swap） Compare & Swap(S,old,new,flag)也是一条原子操作指令,它将共享变量 S与局部变量old 进行比较;若S与old一致,则$\mathtt { S } = \mathtt { n e w }$ ，且 $\mathbf { f l a g } = \mathbf { T r u e }$ 以指明 S被修改;若S与old不一致,则 $\mathbf { o l d } = \mathbf { S }$ ，且 $\mathbf { f l a g } =$ False,其主要用途也是执行锁功能，兹示例对照如下：

old= balance[x]; /\*读共享变量 $\clubsuit$ /   
do new= old - 100; $\nearrow$ 修改 $\yen 7$ Compare & Swap(balancel $_ { x }$ ],old,new,flag); /\*写 \* / $\{ \mathbf { w h i l e } ( \mathbf { \mathrm { f l a g } } = \mathbf { \mathrm { F } } a \mathbf { l s e } )$ ;

上述操作可以用锁实现如下：

lock(S); $\mathbf { b a l a n c e } [ \mathbf { \textit { x } } ] = \mathbf { b a l a n c e } [ \mathbf { \textit { x } } ] - 1 0 0 ; / \star$ 读-修改-写 $\bigstar$ /   
unlock(S) ;

上述锁功能使读、修改、写这一整个过程是互斥的。使用Compare& Swap的优点是临界区的长度减至只一条指令。

取并加(Fetch& Add）Fetch& Add(S,V)也是一条原子指令,它返回共享变量S给局部变量Result,然后将局部值V加向S,其语法结构如下：

Fetch & Add(S,V)Result = S;$\begin{array} { r } { \pmb { \mathrm { S } } = \pmb { \mathrm { S } } + \pmb { \mathrm { V } } ; } \end{array}$ Return Result;！

该指令不仅简单而且快速，例如上节示例的代码段只用一条Fetch& Add指令即可实现：

Fetch & Add(balance[ $_ { \pmb { x } }$ ],100);

# 12.5通 信

进程之间的协同工作必然会产生通信。通信可以通过共享变量和消息传递的办法来达到。通信协议的不同结构如图12.8所示,通信库(如PVM和 MPI)可以实现在套接字(Socket)之上。在发送端，消息下传至套接字层、TCP/IP(或UDP/IP)层直到驱动器和网络硬件层;在接收端,以相反次序重复上述过程。套接字可以直接在低级基本通信层 BCL(Base Communication Layer)上实现而旁路掉 TCP/IP;PVM/MPI也可执行在 BCL之上而旁路掉 TCP/IP 层。BCL的主要目的是尽可能多地展示原始硬件性能，而为了评价通信系统的性能，PVM、MPI和套接字的性能比BCL之性能更为重要。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0005_pages_0281-0350/auto/images/2db295085f3c30b7027f1e7b86ad1abb4c0f6f1c3593e7d72c7966036fc3904a.jpg)  
图12.8通信协议不同结构

通信对并行计算的性能影响很大，而影响通信性能的主要因素有通信硬件（包括节点存储器 $\cdot \mathbf { I } / 0$ 结构、网络界面和通信网络本身等),通信软件(包括通信协议结构和算法等),所提供的通信服务(包括消息传送、流控、失效处理和保护等）等。

# 12.5.1影响通信系统性能的因素

通信硬件典型的通信硬件结构示于图12.9。在松散耦合的系统中，网络接口电路 NIC(Network Interface Circuitry)搭接在I/O 总线(例如 PCI)上。一条发送的消息,从发送节点的存储器出发,经过存储总线、I/O总线、NIC,最后送至网上,其间可达到的通信带宽受限于该路径上最慢的部件,而实际上的通信瓶颈常在存储带宽而不是网络带宽，因为很多通信方案均涉及到DMA访问，待发送的数据在发出去之前首先要复制到DMA缓冲器，而这种存储复制的带宽远远小于存储总线的峰值带宽。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0005_pages_0281-0350/auto/images/fb30ef903a546eff3e2dfe570c89470068379c48c5d69eeaf59e6d642f289d16.jpg)  
图12.9典型的通信硬件结构

通信硬件中NIC是个很关键的电路,它应具有DMA功能;有自己的通信处理器(协处理器),主要用于初始化DMA、打包/拆包、保护检查等;应有存放 NIC代码和临时缓冲消息的存储器；也还应有缓冲信包的一些FIFO等。

通信软件在现代的机群和 MPP系统中，软件开销占通信时间的主导地位。如果没有良好的通信软件，即使有非常有效的网络和NIC,其通信时间也难以明显下降。软件开销主要来源于：①穿越多层协议所需的软件开销；②由于消息通信所涉及的一些存储复制操作所引起的开销；③传输消息时多次跨越保护边界所造成的通信开销(一般至少穿越四次：在发方和收方分别从用户空间进入和离开核空间)。对付第一个问题可以使用简化的通信协议;对付第二个问题可以使用零复制协议(Zero-Copy Protocol),即消息直接从源节点的发送缓冲器到目的节点的接收缓冲器而不缓冲在存储区中；对付第三个问题可以使用用户级技术,即所有的通信均完全执行在用户空间。

通信服务所提供的通信服务会大大影响通信系统的性能，所期望的服务包括：①可靠传输，一旦消息发出就应确保它能正确无误地去向目的地且信包不会丢失； $\textcircled{2}$ 流控，消息不应死锁、拥挤和使缓存溢出； $\textcircled{3}$ 失效处理，包括错误检测、重发、校正等； $\textcircled{4}$ 有序传输，在任何情况下应保障接收消息顺序的正确性。

# 12.5.2低级通信支持

在改进通信性能方面，BCL起着关键的作用。本节简要讨论三种有代表性的 BCL，即双复制(用户空间协议）、单复制(快速消息)和零复制。

双复制(2-Copy） 最好以IBMSP的通信过程(图12.10)说明之。SP通信协议要求发送节点处理器首先将数据从发送缓冲器复制到管道缓冲器；然后再从管道缓冲器复制到虚拟开关界面中的输出队列。接收节点处理器以相反的次序执行相同的动作。参照图12.11,消息层和管道层形成了基本通信库(层)BCL。其中消息层系由一些简单的、非阻塞的、点到点的通信库组成,MPI和PVM等中所有高级消息传递功能均由这些原语实现；管道层维持成对发/收进程之间可靠的、具有流控的、有序的字节流。当源节点处理器执行一条消息层发送操作时，它就将数据从发送缓冲器复制到管道缓冲器；然后消息层再调用管道层代码将数据从管道缓冲器复制到输出队列；源适配器用DMA将数据再从输出队列移到适配器，最终将数据经网络传至目的适配器；目的适配器用DMA将进来的数据传至目的节点的输入队列；目的节点处理器执行一条管道层接收操作，它就将数据从输人队列复制到管道缓冲器；管道层调用消息层代码将数据从管道缓冲器复制到最终的接收缓冲器。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0005_pages_0281-0350/auto/images/b74e57d7ad6adb51a221e55c3cb6c3201a40f0b46ced721236236e1832a486a9.jpg)  
图12.10 IBM SP通信中的数据移动

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0005_pages_0281-0350/auto/images/129653b527dded990a3c8c3f99c70656512f5d982b3ca1509afd462cedb5a1d5.jpg)  
图12.11 IBM SP通信软件

单复制(1-Copy） 单复制又称快速消息FM(Fast Message),主要支持机群和 MPP上低延迟、高带宽通信,其目的是在消息层提供足够的功能使得较高级原语(如PVM、MPI套接字等)所实现的通信性能接近于硬件极限。

FM数据结构和功能非常类似于主动消息，但它简单，只包含很少的几个通信原语,例如,FM_initialize(）,用于初始化;FM_send(dest,h,buf,size),用于发送存储器中长消息； $\mathbf { F M } _ { - } \ s e n d \_ { 4 } ( \operatorname { d e s t } , h , i _ { 0 } , i _ { 1 } , i _ { 3 } )$ ,用于发送寄存器中4字消息；FM_extract（）,用于抽取接收的消息和调用处理程序。

FM是一个用户级通信层，一旦初始化后，适配存储器和节点接收队列都暴露在用户级,随后的FM_send和FM_extract均不必有跨边界保护。当发送节点处理器从缓冲中取出数据并组装成信包后，就直接将其存人适配器的发送队列中,然后信包在DMA控制下注人到网络;当信包到达接收节点时，仍由DMA控制将其放人适配器接收队列，稍后移人节点接收队列，最后调用处理程序将消息数据移进用户存储空间。

零复制（Zero-Copy） 这种通信机制由Princeton的 SHRIMP项目实现，又叫作虚拟存储映射通信,它能提供真正的零复制通信协议。当节点间进行发送/接收时，节点中的守护程序可以通过网络在发送节点和接收节点之间建立人-出关系；然后发送节点的进程就能将其源缓冲器(用户空间)中的消息，直接发送给另一节点中的目的缓冲器，而不须要穿越核空间中的DMS缓冲器。

# 12.5.3 TCP/IP通信协议组简介

网络上的通信通常由一组协议实现，协议就是一组控制数据格式和数据如何传输的规则。本节主要讨论TCP/IP协议组的性质;经常使用的UDP、TCP和IP协议的基本概念与特点;最后讨论应用编程界面API(Application Pro-gramming Interface),即俗称的套接字(Sockets)。

TCP/IP协议组性质目前两种广泛使用的通信协议是由ISO(Interna-tional Standard Organization）制定的 OSI(Open System Interconnect）和由 IAB(Internet Activities Board)制定的 TCP/IP,其对应关系示于图12.12中。TCP/IP(Transmisson Control Protocol/Internet Protocol)协议组涉及到三层：应用层（包括FTP、TELNET、SMTP、SNMP、HTTP）、传输层(包括 TCP 和 UDP)和网络层(包括IP)。TCP层附有TCP头形成称之为TCP段的传输层消息；IP层附有IP头形成称之为IP数据报的网络层消息：NAP层附有以太网头形成称之为以太网帧的NAP层消息。应用层协议必须告诉下层协议目的进程的地址，这通常以(IP地址，端口)数偶形式给出，其中IP地址唯一地指定了目的主机，而端口号指明目的进程。

用户数据报协议 UDP(User Datagram Protocol）TCP/IP 协议组包括两个传输层协议：TCP和UDP,两者均操作在IP协议之上。其中UDP是个非常简单的传输层协议，消息以数据报的格式组装。UDP是一种非连接协议，它就像邮局发信一样，发送者发出数据并不建立连接，而是将大量数据分割并封装成单独的数据报(信件),然后分开发出去(这和下面将要讨论的TCP不一样,它先要建立连接,然后以连续的数据流而不是单独的数据报形式发送)。UDP协议努力将邮件传送好，但并不保证无误传输。一个UDP数据报可能遭到损害或丢失,但在接收端可通过检查和查出错误,并甩掉受损的数据报。UDP对不严格要求确保无误的传输是合适的，否则要使用TCP协议。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0005_pages_0281-0350/auto/images/9fc779e993c1daad6ad97e1a0c70cf5461708e213df43af47282f63463a2af1f.jpg)  
图12.12 OSI和 TCP/IP(a)OSI;(b)TCP/IP

传输控制协议 TCP(Transmission Control Protocol） TCP 协议的功能比UDP强,它是面向连接的协议,就像打电话一样,通话的双方必须先建立连接，然后才能传输消息。在TCP协议中，使用误差检测、应答和重发机制可确保消息的正确顺序和可靠的传输。TCP中消息传输以段的格式，段头中包括源端□、目的端口、顺序号、应答号、标志、窗口尺寸、应急指针与校验和等。TCP传输连续消息流,一旦建立起连接,一个接一个的消息就不间断的传输。TCP 在发送端负责将消息流分成 TCP段,在接收端再负责将段组合成消息。TCP还负责处理乱序段、重复段以及流控：其中乱序段和重复段是由段头中的顺序号来处理;窗口尺寸的值用于流控。在TCP中,采用超时重发的办法可保证可靠传输,但也易造成缓冲饱和与网络拥挤，为此TCP使用了滑动窗口(SlidingWin-dow)流控机制来解决此问题。

互联网协议IP(Internet Protocol）IP的主要功能就是在Internet 网内（可由多个LAN 组成)将消息从一个主机选路至另一个主机。在Internet 网上，任何主机均有唯一的IP地址,而路由器不同于一般主机,它可有多个IP地址,其主要功能是在Internet网内选路IP数据报。IP类似于UDP,它也是非连接的协议,所以传输中也可能出现乱序的或丢失数据板，但此问题留给上一层协议来解决。

当一个主机中的IP软件模块收到发送请求时,它就查找本地表以确定目的主机是否在同一LAN中;如果不是,数据报就必须发给路由器，由其确定进一步的路由路径,并转发数据报给指定的路由器;然后由其将数据报发往最终的目的主机。除了选路以外,IP层协议还提供数据报分段和重装配功能以及误差的通告。

套接字(Socket)界面套接字就是为了使用TCP/IP协议组的一组数据类型和功能,即API。它最初由BerkeleyUnix实现,但现在已经变成了几乎在所有Unix系统上和MicrosoftWindows平台上的标准。一个套接字就是一个通信端口。当两个进程使用套接字通信时，它们各自首先生成一个套接字并指明使用哪种传输协议(UDP或TCP);然后采用读/写它们相应的套接字来进行通信，而套接字软件负责执行真正的通信。下面以简化的域名服务器为例，说明如何使用UDP套接字和TCP套接字来实现客户发送任意主机名给服务器，服务器查找主机的IP地址;然后将其返回给客户。

UDP实现上述域名服务器程序框架如下：

$/ / \ast$ 用UDP实现域名服务器代码段 $\yen 7/$   
$\mathbf { m a i n ( \theta ) } / \ast$ 服务器代码段 $\yen 7$   
mysocket socket(AF_ INET,SOCK _DGRAM,…); bind(my socket,·\*);   
recvfrom(mysocket , hostname) ;   
host_ $\mathbb { P } =$ Name To IP(hostname);   
send to (mysocket,host _IP,…);   
main(int argc,char $\clubsuit$ argv[]) $\big / \ast$ 客户代码段 $\yen 7$   
mysocket $\asymp$ socket(AF_ INET,SOCK _DGRAM,); send to (mysocket,argv[1],\*\*);   
recvfrom(mysocket,host_ IP,…);   
一

其中，服务器和客户均首先调用socket函数，目的就是生成变量为mysocket的套接字;常量AF_INET指明互连网域地址(IP地址)将用作套接字寻址格式，而 SOCK_DGRAM指明使用UDP;服务器使用bind函数调用将套接字连接至端口号上;当套接字建立后，客户用 send to 函数将hostname发给服务器；服务器使用recvfrom 函数接收消息,并用执行局部函数Name TOIP将其翻译成相应的 IP 地址,并用 send to将 IP地址返回给客户;客户使用 recvfrom 接收此 IP地址。

TCP实现上述域名服务器程序框架如下：

$/ / \ast$ 用TCP实现域名服务器代码段 $\clubsuit$ /1   
$\mathtt { m a i n ( \mu ) } / *$ 服务器代码段 $\clubsuit$ /   
！   
mysocket $=$ socket(AF_ INET,SOCK _ STREAM,); bind(mysocket,\*);   
listen(mysocket,…\*);   
fp accept(mysocket,.\*);   
read(fp,hostname,.);   
host _ $\mathbf { I P } =$ Name To IP(hostname);   
write(fp,host_ IP,…\*);   
close(fp) ;   
一   
main(int argc,char $\bigstar$ argr[]）/\*客户代码段 $\yen 7$   
mysocket $\simeq$ Socket(AF_ INET,SOCK _ STREAM,…); connect(mysocket,…\*);   
write(mysocket,argv[1],…\*);   
read(mysocket,host_ IP,.\*);   
！

其中，socket 生成和binding（连接）类似于UDP 实现的程序,只是 SOCK_DGRAM用 SOCK_STREAM代替。与UDP不一样,TCP是面向连接的，服务器要告诉核它准备接收连接，这通过执行listen函数实现;然后通过执行accept函数，服务器等待接收来自客户的连接请求，此函数一直到客户执行connect函数才返回;连接双方的建立尤如普通文件一样，使用了文件指针fp。到此，就像访问一个文件一样，服务器和客户就可利用读/写连接而相互通信，当通信完毕，服务器执行close(fp)关闭连接。

# 12.6 小结和导读

小结本章首先对并行程序设计作了一般性介绍，包括并行程序设计和申行程序设计的差别、并行程序设计的困难所在,并行程序设计的环境与工具以及并行程序设计的一般方法;然后对并行程序中最基本的计算要素一一进程和线程的基本概念以及支持进程和线程的管理、同步和通信的各种软/硬件机制进行了讨论。这些机制可被用在不同的多处理机和多计算机平台上。目前随着VL-SI工艺的进展,有些机制甚至被加人到单处理机系统中。

有关进程和线程的一些问题，已在操作系统课程中和计算机体系结构课程中详细讨论过,所以熟悉这些内容的读者，可以跳过这些章节;而不熟悉这些内容的读者，在阅读本章时恐怕要随时参照有关教材内容。但不管如何，由于本章所介绍内容,对学习并行计算针对性较强,所以复习或学习本章内容也是必要的。

导读关于并行程序设计问题读者可参阅[127]；对并行程序设计的困难性,[137]中进行了讨论;提倡 SPPP(Seqential-Program,Paralel-Processing)编程风格的是[140]。从OS角度讨论进程和线程的概念,读者可参阅[166];IEEEPthreads标准发表在[141]。关于同步的讨论,读者可参阅[126]。有关双复制通信过程最好参阅IBMSP2通信子系统[163];有关FM的讨论,读者可参阅[118];零复制使用在Princeton大学 SHRIMP项目中[35];TCP/IP 协议组的讨论读者可参阅Comer的著作[52]。

# 习 题

12.1假定要录制一部数字电影。电影的一帧有 $\textbf { 1 0 2 4 } \times \textbf { 1 0 2 4 }$ 个像素，每个像素需4B(4个字节),即每帧需要 ${ \textbf { 4 } } \mathbf { M B }$ 。如果电影每秒钟有30帧，不经压缩，问一部两小时的电影需要多少字节？

12.2当CrayResearch欲研制一台能扩展至2048个处理器，每个处理器有 ${ \ 6 4 } \ \mathbf { M B }$ 的局存的T3D MPP时,他们使用了DEC Alpha 21064微处理器芯片，该芯片为34位。试问其物理地址空间够用吗？应要多少位的物理地址才行？

12.3在一个计算机系统中，如果10个进程使用一个处理器。假定处理器的一个交互进程须5s,而其余的各进程须 ${ \bf 1 0 0 0 5 } ,$

试间： $\textcircled{1}$ 在批处理时，用户必须等待多久？$\textcircled{2}$ 在分时处理时，用户必须等待多久？

12.5假定有 $\pmb { n }$ 个进程 $\mathrm { P } ( 0 ) , \mathrm { P } ( 1 ) , \cdots , \mathrm { P } ( n - 1 )$ ，数组元素 $\pmb { a } \{ \pmb { i } \}$ 开始时被分配给进程 $\operatorname { P } ( i )$ 0 试写出求归约和 $a [ 0 ] + a \left[ 1 \right] + \cdots + a \left[ n - 1 \right]$ 的代码段，并以 $\pmb { n = 8 }$ 示例之。

12.6图12.13示出了点到点和各种集合通信操作。试根据该图解释点到点、播送、散播、搜集、全交换、移位、归约与前缀和等通信操作的含义。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0005_pages_0281-0350/auto/images/803891719e121704502e99e9c20c3716308868f5fdc09403bb71536cd4082ae0.jpg)  
图12.13点到点和集合通信操作

12.7某一机群系统,节点使用800MB/s的存储总线,133MB/s的I/O总线和200 MB/s的NIC DMA 总线。

试问：①如通信网络的峰速为1Gb/s,那么通信带宽的硬件限制是什么？$\textcircled{2}$ 如果网络升级为 $4 0 0 ~ \mathrm { M B / s }$ 应如何办？

12.8假定某公司在银行中有三个帐户X、Y和Z,它们可以由公司的任何雇员随意访问。雇员们对银行的存、取和转帐等事务处理的代码段可描述如下：

$\big / \ast$ 从帐户X支取 $\yen 100$ 元 $\pmb { \star }$ / atomic! 一 ${ \bf i f ( b a l a c e [ X ] > 1 0 0 ) ~ b a l a n c e [ X ] = b a l a n c e [ X ] - 1 0 0 ; }$   
$\big / \big \varkappa$ 从帐户 $\mathbf { Y }$ 存人 $\yen 100$ 元 $^ { \star }$ / ${ \mathrm { a t o m i c } } \{ { \mathrm { b a l a n c e } } [ { \mathrm { Y } } ] = { \mathrm { b a l a n c e } } [ { \mathrm { Y } } ] + 1 0 0 ; \}$   
$\nearrow$ 向帐户 $\mathbf { x }$ 中转 $\yen 100$ 元到帐号 $Z \star ~ \nearrow$ atomic!

$\mathbf { i } \pmb { f } ( \mathbf { b a l a n c e [ X ] } > 1 0 0 !$ balance[ X] $1 = b a$ lance[X]-100; $\mathbf { b a l a n c e [ Z ] } = \mathbf { b a l a n c e [ Z ] } + \mathbf { 1 0 0 } ;$

其中,atomic！|为子原子操作。试解释为什么雇员们在任何时候(同时)支、取、转帐时,这些事务操作总是安全有效的。

12.9考虑如下使用 $\mathbf { i o c k }$ 和unlock的并行代码：

$\mathrm { p a r f o r } \left( \mathrm { i } = 0 ; \mathrm { i } < \mathrm { n } ; \mathrm { i } + \right) \left\{ \begin{array} { r l } \end{array} \right.$ noncritical section lock(S); critical section unlock(S); 一

假定非临界区操作取 $T _ { \mathrm { r e s } }$ 时间,临界区操作取 $T _ { \infty }$ 时间,加锁取 ${ \pmb t } _ { \mathbf { b d } }$ 时间,而去锁时间可忽略。则相应的串行程序需 $n ( T _ { \mathrm { n s } } + T _ { \mathrm { s } } )$ 时间。试问：

$\textcircled{1}$ 总的并行执行时间是多少？$\textcircled{2}$ 使用 $\pmb { n }$ 个处理器时加速多大？$\textcircled{3}$ 你能够忽略开销吗？

12.10试回答如下问题：

$\textcircled{1}$ 什么是面向连接的协议和非连接协议？$\textcircled{2} \textcircled { 1 } \textcircled { 2 }$ 协议和UDP协议有何异同？$\textcircled{3}$ IP在功能上与TCP和UDP差别何在？$\textcircled{4}$ 何谓套接字界面？

# 第十三章 并行程序设计模型和共享存储系统编程

本章首先简要介绍五种并行编程风范：相并行、分治并行、流水线并行、主-从并行和工作池并行，并给出了一个计算 $\pmb { \pi }$ 的样本程序，以便以其示例各种编程风格；然后讨论了四种并行程序设计模型：隐式并行模型、数据并行模型、消息传递模型和共享变量模型,并将它们的主要特性进行了综合比较;最后讨论了共享存储的三种与平台无关的编程模型：ANSIX3H5A共享存储模型、POSIX线程模型和OpenMP标准。至于基于数据并行的高性能Fortran(HPF)编程和基于消息传递的 MPI编程将在第十四章中予以讨论。

# 13.1 并行编程风范和样本程序

# 13.1.1 五种并行编程风范

所谓并行编程风范(Parallel Programming Paradigms)是指构造运行在并行机上的并行算法的方法。目前已有好几种方法,它们既可单独使用,也可组合使用。参照图13.1,现分述如下

相并行(Phase Parallel） 如图13.1(a)所示,一个并行程序系由一些超级步(也称为相)组成：每个超级步内，各个进程执行独自的计算,然后继之以交互作用(包括通信同步等)。可见相并行和第四章中所讲的 BSP模型是十分相似的，这种相并行也称之为松散同步并行，其优点是方便查错和性能分析，其缺点是计算和交互作用不能重叠且维持负载平衡是较困难的。

分治并行(Divide and Conquer Parallel） 如图13.1(b)所示,一个父进程将其工作负载分成一些小的负载并将它们指派给一些子进程,这些子进程并行地完成各自的计算，其计算结果由父进程归并之。这种分开和合并的过程很自然地导致递归,其缺点是难以达到负载平衡。

流水线并行(Pipeline Parallel）如图13.1(c)所示,一些进程形成流水线作业法，诸进程在流水线的不同地段同时重叠地执行操作以达到整体并行的效果。

主-从并行(Master-Slave Parallel） 如图13.1(d)所示,这种并行也称之为放牧式并行。一个主进程执行并行程序的串行部分并生成一些可同时并行执行计算的子进程；当某一子进程完成计算后就报告给主进程，主进程再分配新的任务给它。整个的协调工作由主进程完成，其缺点是主进程易成为系统瓶颈。

工作池并行(Work Pool Parallel） 如图13.1(e)所示,开始时池中只有一件工作，任何空间的进程均可以从池中取出它并执行之，执行中可能产生一个或多个新工作并把它们放回池中，以供别的空间进程受领之，当池中变空时则并行程序结束。一个工作池实际上就是一个全局数据结构,可以是无序集合、队列、或优先队列等。这种并行的优点是易于达到负载平衡，因为工作负载是动态地分配给空间进程的；然而实现工作池能被多个进程有效访问并非易事，特别是消息传递模式中,也正是因为如此,工作池并行常使用在共享变量的模式中。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0005_pages_0281-0350/auto/images/8aea6c0d66914f30a6fa363c5ffac57af6af3b314dbcdd49b250af6e31d6daac.jpg)  
图13.1五种并行编程风范(a)相并行；(b)分治并行;(c)流水线并行;(d)主-从并行;(e)工作池并行

# 13.1.2计算 $\pmb { \pi }$ 样本程序

为了以下各节讨论方便和具体,先选择一个样本程序,以其为例进行讨论和相互对照。在此所讲的样本程序，并非普通意义下的“标准样板"程序，它只不过是一个简单、易于实现、且便于理解的一个计算程序罢了。习惯上,作为教材，选择了这样一个大家都不生疏的用数值积分法求π近似值的样本程序。

参照图13.2,用数值积分法计算 $\pmb { \pi }$ 时，就是要求出在压间[0,1]内函数曲线$4 / ( 1 + x ^ { 2 } )$ 下的面积，此面积就是 $\pmb { \pi }$ 的近似值，为此先将区间[0,1]划分成N个等间隔的子区间，每个子区间的宽度为 $1 / N$ ;然后计算出各子区间中点处的函数值；再将各个子区间面积相加就可得出 $\pmb { \pi }$ 的近似值。其计算公式如下：

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0005_pages_0281-0350/auto/images/abb73a3ab832b2f8e1466fda62a26b66e8976df237c7c40ac752e1ad6467c202.jpg)  
图13.2用数值积分法求 $\pmb { \pi }$ 值

$$
\pi = \int _ { 0 } ^ { 1 } \frac { 4 } { 1 + x ^ { 2 } } \mathrm { d } x \approx \sum _ { 0 \leqslant { 1 < N } } \frac { 4 } { 1 + \left( \frac { i + 0 . 5 } { N } \right) ^ { 2 } } \cdot \frac { 1 } { N }
$$

计算此公式的串行C代码如下：

# $/ / *$ 计算 ${ \pmb { \pi } } \mathbf { C }$ 语言编程代码段 $\yen 7/$

#define N 1000000   
main(） double local, $\mathbf { \vec { p i } } = \mathbf { 0 } . 0 , \mathbf { w } ;$ long i; $\mathbf { w } = 1 . 0 \mathbf { \langle N ; }$ $\begin{array} { r l } & { \mathrm { ~ f o r ( i = 0 , i < N , j + 1 + \Delta ) ~ } ; } \\ & { \qquad \mathrm { l o c a l = ( i + 0 . 5 ) * w , } } \\ & { \qquad \mathrm { { p i = p i + 4 . 0 / ( 1 . 0 + l o c a l * l o c a l ) } } ; } \\ &  \qquad \quad \} \end{array}$ $\begin{array} { l } { \mathrm { p r i n t f } ( \mathrm { ' p i ~ i s ~ } \% \mathrm { ~ f ~ } \backslash \mathrm { ~ n ~ " ~ } , \mathrm { p i ~ } \ast \mathrm { ~ w ~ } ) ; } \\  \mathrm { ~ } \} \end{array}$

其中， $N$ 是等分间隔数,其值越大越精确，但计算时间越长。

# 13.2并行程序设计模型

并行程序设计模型(Parallel Program Model)是一种程序抽象的集合，它给程序员提供了一幅计算机硬件/软件系统透明的简图,程序员利用这些模型就可以为多处理机、多计算机和工作站机群等设计并行程序。

# 13.2.1隐式并行模型

隐式并行（Implicit Parallelism)是相对显式并行(Explicit Parallelism）而言的,后者是指程序的并行性由程序员利用专门的语言结构,编译制导或库函数调用等在源代码中给予明显的指定;前者,程序员未作明确地指定并行性，而让编译器和运行(时)支持系统自动地开拓它,本节先讨论隐式并行程序设计模型;而显式并行程序设计模型,包括数据并行、共享变量和消息传递等将在下几小节分别讨论之。

隐式并行模型中最著名的方法是串行程序的自动并行化（Automatic Paral-lellzation)。编译器执行串行源代码程序的相关分析，然后使用一组转换技术将顺序代码转换成本原并行Fortran代码。将串行代码并行化的关键是相关分析,主要包括数据相关和控制相关。如果操作A依赖于B,则A必须在B之后执行;两个操作可以并行执行只有它们俩是不相关的才行。如果相关的确存在，则必须使用转换技术(也称为重构或优化)将其删除之。目前绝大多数分析和重构技术都集中在 loop 级上,也就是集中开拓 Fortran 的"do loops"和C的“forloops"的并行性。常用的三种最重要的转换方法有：专用化(Privatization）、并行归约(Parallel Reduction)和归纳变量(Induction Variables),尽管它们均在个例中有所奏效，但总的讲自动并行化方法效率是非常不高的。

一种有效的方法就是使用用户定向(User Direction)的办法,即用户帮助编译器为并行化提供更多的信息，例如交互并行化(InteractiveParallelization)方法允许编译器(或运行系统)提问题,然后程序员可提供附加信息以指导并行化的进程。更流行的方法是允许程序员在源代码中插人编译制导(Compiler Direc-tives),它在C语言中叫 Pragmas。这些格式化的注释语句,携带着有助于编译器能更好地进行重构的附加信息。例如下述代码段：

# Pragmas_ CNX loop- Parallel $\mathbf { f o r } ( \mathrm { i } = 0 ; \mathrm { i } < 1 0 0 0 ; \mathrm { i } + \mathit { \Omega } + ) \left. \begin{array} { r l } \end{array} \right.$ $\mathsf { A } [ \mathrm { i } ] = \mathsf { f o o } ( \mathsf { B } [ \mathrm { i } ] , \mathsf { C } [ \mathrm { i } ] ) ;$

其中 Loop-Parallel Pragmas 强使编译器并行化随后的 $\mathbf { l o o p }$ ，而不管 $\mathsf { l o o p }$ 体是什么。编译器不必分析loop体中的相关性，是用户确保并行化后代码的正确性。

即使编译制导能帮助并行化，但并非所有的并行性均能在编译时识别，有些并行性只能在运行时才能被揭示出来。相应地这种技术称为运行时并行化(Run-TimeParallelization）。例如 Stanford大学开发的Jade语言,既能开拓编译时的并行性又能开拓运行时的并行性，程序员从现行的串行程序开始,附加的语言结构用来将顺序程序分解成多个任务和指明每个任务如何访问数据;编译器和运行(时)系统将自动识别和开拓并行性。Jade不仅能识别出更多的并行性，而且允许自动开拓非规整和动态并行性。

# 13.2.2数据并行模型

数据并行(Data-Parallel)模型既可以在 SIMD 计算机上实现,也可以在 SP-MD 计算机上实现,这取决于粒度大小。SIMD程序着重开发指令级细粒度的并行性。SPMD程序着重开发子程序级中粒度的并行性。数据并行程序设计强调的是局部计算和数据选路操作,它比较适合于使用规则网络,模板和多维信号/图像数据集来求解细粒度的应用问题。数据并行操作的同步是在编译时而不是在运行时完成的。硬件同步则是通过控制器执行SIMD程序的锁步操作完成的。在同步的SIMD程序中，所有PE间的通信则直接由硬件控制，除所有PE间操作需锁步外,PE间的数据通信也是以锁步方式进行的。这些同步指令的执行和数据选路操作使得SIMD计算机在开发大型数组，大型网格或网状数据的空间并行性时相当有效。

值得注意的是,一个SIMD程序可以重新编译用于MIMD结构,其思想是开发一个源到源的预编译器来实现程序之间的转换。就此意义而言，数据并行程序设计模型既适用于同步的SIMD计算机，也适用于紧耦合的MIMD计算机。

总之，数据并行模型具有以下特点：①单线程(Single-Threading)：从程序员的观点，一个数据并行程序只由一个进程执行，具有单一控制线；就控制流而论，一个数据并行程序就像一个顺序程序一样。②并行操作于聚合数据结构上：数据并行程序的一个单步(语句),可指定同时作用在不同数组元素或其它聚合数据结构上的多个操作。③松散同步(Loosely Synchronous)：在数据并行程序的每条语句之后，均有一个隐含的同步，这种语句级的同步是松散的（相对于SIMD机器每条指令之后的紧同步而言）。④全局命名空间（GlobalNamingSpace):数据并行程序中的所有变量均驻留在单一地址空间内，所有语句可访问任何变量而只要满足通常的变量作用域规则。③隐式相互作用(Implicit Inter-action)：因为数据并行程序的每条语句之末存在着一个隐含的路障，所以不需要一个显式同步;通信可由变量指派而隐含地完成。 $\textcircled{6}$ 隐式数据分配（Implicit Da-ta Allocation)：程序员不必要明确地指定如何分配数据,可将改进数据局部性和减少通信的数据分配方法揭示给编译器。

下面举一个计算 $\pmb { \pi }$ 值的数据并行程序的例子，以期体会数据并行的基本特点。参照13.1.2节用C语言书写的计算 $\pmb { \pi }$ 的串行代码,不难写出如下数据并行程序：

$/ / \ast$ 计算 $\pmb { \pi }$ 数据并行编程代码段 $\yen 7/$   
main（）！ double local[N],temp[N],pi,w; long i,j,t $\mathbf { , N } = 1 0 0 0 0 0 0$ ；   
A: $\mathbf { w } = 1 . 0 \Lambda$   
B: $\mathrm { f o r a l l } ( \mathrm { i } = 0 ; \mathrm { i } < \mathrm { N } ; \mathrm { i } + { } + { } ) \left. \begin{array} { r l } \end{array} \right.$ $\mathrm { P } { : } \mathrm { l o c a l } \mathrm { [ i ] } = \left( \mathrm { i } + 0 . 5 \right) \mathrm { \# ~ w ~ }$ $\mathbf { Q } { \mathrm { : } } { \mathrm { t e m p } } [ \mathbf { i } ] = 4 . 0 / ( 1 . 0 + \mathrm { l o c a l [ i ] } * \mathrm { l o c a l [ i ] } ) ;$ ！   
C: $\mathrm { \bf p i = s u m ( t e m p ) }$ ；   
D:printf("pi is %f\n",pi \* w);   
$\mid / \ast _ { \mathrm { \bf ~ m a i n } } ( ) \ast /$

上述程序中包含了四个语句A、B(B又包含两个子语句 $\mathbf { P }$ 和 $\mathbf { Q }$ ）、C和D,这四个语句可由单一进程一个接一个地执行,但每个均同时对多个数据执行相同的操作，其中语句A和D就是普通的顺序语句;而语句C执行N个 temp数组元素的归约求和,并将结果赋值给变量pi;语句P并行执行表达式求值并更新所有N个local数据组元素，但所有这N个元素均必须由语句P更新完后语句Q才能被执行;类似地，在语句C执行归约求和之前，所有temp元素均必须由语句Q进行赋值。

# 13.2.3消息传递模型

在消息传递(Message Passing)模型中,驻留在不同处理器节点上的进程可以通过网络传递消息相互通信。消息可以是指令、数据、同步信号或中断信号等。在消息传递并行程序中，用户必须明确地为进程分配数据和负载，它比较适合于开发大粒度的并行性，这些程序是多线程的和异步的，要求显式同步（如路障等)以确保正确地执行顺序。然而这些进程均有其分开的地址空间。消息传递模型比数据并行模型灵活，两种广泛使用的标准库PVM和MPI使消息传递程序大大地增强了可移植性。消息传递程序不仅可执行在共享变量的多处理机上，而且可执行在分布存储的多计算机上。

总之，消息传递模型具有以下特点： $\textcircled{1}$ 多线程（Multithreading)：消息传递程序系由多个进程组成，每个进程都有其自己的控制线且可执行不同的代码；控制并行（MPMD)和数据并行(SPMD)均可支持。 $\textcircled{2}$ 异步并行性（AsynchronousParallelism)：消息传递程序的诸线程彼此异步地执行，使用诸如路障和阻塞通信的方法来同步各个进程。 $\textcircled{3}$ 分开的地址空间(Separate Address Space):并行程序的进程驻留在不同地址空间内。一个进程中的数据变量在其它进程是不可见的,因此一个进程不能读/写另一进程中的变量，进程的相互作用通过执行特殊的消息传递操作实现之。 $\textcircled{4}$ 显式相互作用(Explicit Interaction):程序员必须解决包括数据映射、通信、同步和聚合等相互作用问题;负载分配通常通过属主-计算(Owner-Compute)规则来完成,即进程只在其所拥有的数据上执行计算。 $\textcircled{5}$ 显式分配(ExplicitAllocation)：负载和数据均由用户显式地分配给进程,为了减少设计和编码的复杂性，用户常使用单一代码方法编写SPMD应用程序。

下面用MPI以C语言表示方式来示例上一节所举的计算 $\pmb { \pi }$ 的消息传递程序，不期望读者完全理解它，但求读者能领会消息传递程序的基本特点。

$/ / \ast$ 计算 $\pmb { \pi } .$ 消息传递编程代码段 $\pmb { \mathscr { k } }$ //   
# define $\mathbf { N }$ 100000 main(){ donuble local, pi, w ; long i ,taskid,numtask; A: $\mathbf { w } = 1 . 0 \ N$ ; MPI- Init(&argc,&argv); MPI- Comm-rank(MPI-COMM_WORLD,&taskid); MPI - Comm- Size(MPI- COMM. WORLD,& numtask);   
B: for $\mathrm { ( i = t a s k i d ; i < N ; i = i + n u m t a s k ) } \left\{ \begin{array} { r l } \end{array} \right.$ P $\mathbf { : } \mathrm { l o c a l } = ( \mathrm { i } + \mathbf { 0 } . 5 ) \star \mathbf { w } ;$ $\mathbf { Q } : { \mathrm { l o c a l } } = 4 . 0 / ( 1 . 0 + { \mathrm { l o c a l } } * { \mathrm { l o c a l } } )$ ： 一   
C: MPI-Reduce(&local,&pi,1,MPI_ Double,MPI_ MAX,0,MPI-COMM- WORLD) ;   
D: if( taskid ${ \bf \mu } = { \bf \sigma } = { \bf 0 }$ ) printf("pi is %f\ n",pi \* w); MPI_Finalize();

有关消息传递操作的细节将在第十四章中讨论。

# 13.2.4共享变量模型

在共享变量(Shared-Variable)模型中,驻留在各处理器上的进程可以通过读/写公共存储器中的共享变量相互通信。它与数据并行模型的相似之处在于它有一个单一的全局名字空间；它与消息传递模型的相似之处在于它是多线程的和异步的。然而数据是驻留在单一共享地址空间中，因此不需要显式分配数据,而工作负载既可显式也可隐式分配。通信通过共享的读/写变量隐式完成，而同步必须是显式的，以保持进程执行的正确顺序。

共享变量模型尚无一个可广泛接受的标准。例如一个为 SGI Power Chal-lenge编写的程序不能直接运行在 Convex Exemplar上;一个为 SMP或DSM开发的共享变量程序不能运行在诸如 MPP和机群的多计算机上。

关于共享变量模型尚须说明以下几点： $\textcircled{1}$ 一个广为流传的错误概念是共享变量模型运行细粒度(FineGranularity)的并行性比消息传递模型好：要注意共享变量模型是一种并行编程模型,它可以实现在PVP、SMP、DSM、MPP或甚至机群的任意并行平台上。支持细粒度并行性的平台应具有有效的通信/同步机制，一个共享变量的程序可能遭致高的相互作用开销从而远比运行在机群、MPP甚至SMP上的消息传递程序慢得多。 $\textcircled{2}$ 一个普遍的说法是共享变量编程比消息传递编程容易：此说法虽不错，但科学试验的事实尚未完全建立。为了开发一个新的、有效的、松散同步的、通信模式规则的并行程序,共享变量的方法未必比消息传递方法容易。当然对于非规则的并行程序，使用消息传递原语很难指明所需要的相互作用；同时共享变量模型允许全局指针操作，而消息传递模型是无此能力的；此外共享变量编程虽不必明显地划分和分配数据，但这也可能伤害性能。③就查错而论，共享变量程序可能比消息传递程序更困难：共享变量程序中的所有进程都驻留在单地址空间中，而且访问共享数据必须由同步结构(如锁和临界区)加以保护。同步错误易于出现,而且一旦出现就难以查找；但在消息传递程序中，此类错误出现的频度大大减少，因为诸进程不共享单一地址空间。

最后，为了比照起见,下面也给出用类-C语言方式书写的计算π的共享变量程序。读者可能暂不能完全理解，但至少可以理解其编程概貌。

# $/ / *$ 计算 $\pmb { \pi }$ 共享变量编程代码段 $\yen 74$

# define N 1000000   
main（）{ double local , $\mathfrak { p i } = 0 . 0$ ,w; long i;   
A: $\mathbf { w } { = } 1 . 0 \Lambda$ ；   
B: # Pragma Parallel # Pragma Shared(pi,w) # Pragma Local(i, local) # Pragma pfor iterate $\mathbf { ( i = 0 ; N ; 1 ) }$ $\mathbf { f o r } ( \mathrm { i } = 0 ; \mathrm { i } < \mathrm { N } , \mathrm { i } + { \mathbf { \rho } } + ) \left\{ \begin{array} { r l } \end{array} \right.$ P $\mathbf { : } \mathrm { l o c a l } = ( \mathrm { i } + \mathbf { 0 } . 5 ) \not \times \mathbf { w } \mathbf { ; }$ $\mathsf { Q } { : } \mathrm { l o c a l } { = 4 . 0 / ( 1 . 0 + \mathrm { l o c a l } * \mathrm { l o c a l } ) } ;$   
C: # Pragma Critical   
D: $\begin{array} { r l } & { \mathrm { p i } { = } \mathrm { p i } + \mathrm { l o c a l } ; } \\ & { \nmid } \\ & { \mathrm { p r i n t f } ( \mathrm { \ ' p i } \mathrm { \ i s \ } \mathrm { \ } \mathrm { \ } \mathrm { \% } \mathrm { \ } \mathrm { \Omega } ) ; } \\ & { \mathrm { \mid } / \mathrm { \ne p a i n } ( { \bf \Omega } ) \mathrm { \ne \ } / } \end{array}$

其中,Pragma 即编译制导,意义同前(见第13.2.1节)。

# 13.2.5并行程序设计模型比较

三种显式并行程序设计模型(数据并行、消息传递、共享变量)的主要特性可综合于表13.1中。

表13.1三种显式并行程序设计模型主要特性一览表  

<table><tr><td rowspan=1 colspan=1>特性</td><td rowspan=1 colspan=1>数据并行</td><td rowspan=1 colspan=1>消息传递</td><td rowspan=1 colspan=1>共享变量</td></tr><tr><td rowspan=1 colspan=1>控制流(线）</td><td rowspan=1 colspan=1>单线程</td><td rowspan=1 colspan=1>多线程</td><td rowspan=1 colspan=1>多线程</td></tr><tr><td rowspan=1 colspan=1>进程间操作</td><td rowspan=1 colspan=1>松散同步</td><td rowspan=1 colspan=1>异步</td><td rowspan=1 colspan=1>异步</td></tr><tr><td rowspan=1 colspan=1>地址空间</td><td rowspan=1 colspan=1>单一地址</td><td rowspan=1 colspan=1>多地址空间</td><td rowspan=1 colspan=1>单地址空间</td></tr><tr><td rowspan=1 colspan=1>相互作用</td><td rowspan=1 colspan=1>隐式</td><td rowspan=1 colspan=1>显式</td><td rowspan=1 colspan=1>显式</td></tr><tr><td rowspan=1 colspan=1>数据分配</td><td rowspan=1 colspan=1>隐式或半隐式</td><td rowspan=1 colspan=1>显式</td><td rowspan=1 colspan=1>隐式或半隐式</td></tr></table>

四种并行程序设计模型(隐式并行、数据并行、消息传递并行、共享变量并行),从用户的观点也可作一比较。使用星号(★)的多少来表征它们性能优劣程度，其中四星(★★★★)表示性能最好，一个星(★)表示性能较差。表13.2中的结果,只是现状的写照,将来也许会变化。

表13.2 四种并行程序设计模型比较一览表  

<table><tr><td rowspan=1 colspan=1>比较项目</td><td rowspan=1 colspan=1>隐式并行</td><td rowspan=1 colspan=1>数据并行</td><td rowspan=1 colspan=1>消息传递</td><td rowspan=1 colspan=1>共享变量</td></tr><tr><td rowspan=1 colspan=1>并行性</td><td rowspan=1 colspan=1>★★★★</td><td rowspan=1 colspan=1>★★★</td><td rowspan=1 colspan=1>★</td><td rowspan=1 colspan=1>★★</td></tr><tr><td rowspan=1 colspan=1>数据分配</td><td rowspan=1 colspan=1>★★★★</td><td rowspan=1 colspan=1>★★</td><td rowspan=1 colspan=1>★</td><td rowspan=1 colspan=1>★★★</td></tr><tr><td rowspan=1 colspan=1>通信</td><td rowspan=1 colspan=1>★★★★</td><td rowspan=1 colspan=1>★★★</td><td rowspan=1 colspan=1>★</td><td rowspan=1 colspan=1>★★★</td></tr><tr><td rowspan=1 colspan=1>同步</td><td rowspan=1 colspan=1>★★★★</td><td rowspan=1 colspan=1>★★★★</td><td rowspan=1 colspan=1>★★</td><td rowspan=1 colspan=1>★</td></tr><tr><td rowspan=1 colspan=1>正确性</td><td rowspan=1 colspan=1>★★★★</td><td rowspan=1 colspan=1>★★★</td><td rowspan=1 colspan=1>★</td><td rowspan=1 colspan=1>★</td></tr><tr><td rowspan=1 colspan=1>可移植性</td><td rowspan=1 colspan=1>★★★★</td><td rowspan=1 colspan=1>★★★</td><td rowspan=1 colspan=1>★★★</td><td rowspan=1 colspan=1>★</td></tr><tr><td rowspan=1 colspan=1>通用性</td><td rowspan=1 colspan=1>★</td><td rowspan=1 colspan=1>★★</td><td rowspan=1 colspan=1>★★★</td><td rowspan=1 colspan=1>★★★</td></tr><tr><td rowspan=1 colspan=1>结构性</td><td rowspan=1 colspan=1>★★★★</td><td rowspan=1 colspan=1>★★★</td><td rowspan=1 colspan=1>★</td><td rowspan=1 colspan=1>★</td></tr><tr><td rowspan=1 colspan=1>与平台无关的标准</td><td rowspan=1 colspan=1>Kap,Forge </td><td rowspan=1 colspan=1>Fortran90,HPF</td><td rowspan=1 colspan=1>PVM,MPI</td><td rowspan=1 colspan=1>X3H5,Pthreads,OpenMP</td></tr><tr><td rowspan=1 colspan=1>与平台有关的标准</td><td rowspan=1 colspan=1>ConvexExemplar</td><td rowspan=1 colspan=1>CMC*</td><td rowspan=1 colspan=1>SP2MPL,ParagonNX</td><td rowspan=1 colspan=1>Cray Craft,SGI Power C</td></tr></table>

# 13.3共享存储并行编程

在20 世纪80年代,高性能的科学和工程计算中共享存储的编程模式曾是一统天下。进人20世纪90年代后,尽管分布存储的大规模并行处理系统已夺走了峰值计算速度的桂冠,但共享存储的并行处理仍以其可编程性和系统的可用性的优势，在科学和工程计算中与分布存储系统共领风骚。

在共享存储的编程模式中,各个处理器可以对共享存储器中的数据进行存取,数据对每个处理器而言都是可访问到的，不需要在处理器之间进行传送，即数据通信是通过读/写共享存储单元来完成的。

共享存储的并行程序设计的基本问题包括：①任务划分：任务划分就是把一个程序划分成若干个可以分配给不同的处理器去并行执行的一组任务，划分的方法与并行程序设计风格有关：单程序多数据流(SPMD)编程风格采用按数据流划分任务的方法，即域分解法，它将要计算的问题的区域分解成多个子域,每个任务计算一个子域,这样实现的并行也称为数据并行；多程序多数据流（MP-MD)编程风格则采用按控制流划分任务的方法，即功能分解法，它将要计算的问题分解成多个子问题,每个任务计算一个子问题,这样实现的并行也称为控制并行。 $\textcircled{2}$ 任务调度：调度就是把一个任务集合分配给一组处理器，传统的调度是操作系统管理的事,但因为由操作系统施行调度开销较大，且操作系统难于从程序中获得优化调度信息，所以现代并行机上一个程序内的调度多由用户、编译器和运行库来完成。任务调度有静态调度和动态调度之分：静态调度（StaticScheduling)由程序员在编程时、或者编译器在编译时将任务分配给处理器。静态调度有确定的和非确定的两种模式：确定模式(Deterministic.Model)任务之间的优先关系和任务所需的执行时间在调度之前是固定和已知的，常可使用Gantt图(Gantt Chart)来说明调度过程;非确定模式(Nondeterminstic Model)任务的执行时间可表示为一随机变量，这就使得调度问题更为困难。动态调度(Dynamic Scheduling)在运行时将任务分配给处理器，分配的策略是在编程或编译时确定的，但具体的分配是在运行时才能确定的。③任务同步：同步对并行程序设计是非常重要的,同步常用来确定任务间正确的执行次序,或用于确保各任务对共享变量的正确的读写次序。简单高速的同步机制一般由硬件支持，复杂多功能的同步机制常由软件实现。已如第十二章所述,同步方式有锁、路障、事件、信号灯和管程等。注意错误的同步会导致死锁。④任务通信：在共享存储系统中，任务间的通信借助于读写共享变量来完成，不需要专门的机制，但应注意读写的时机,即要在发送者将正确的信息送出后，接收者才可去读取，为此常要使用路障同步操作，其实同步也可视为一种特殊的通信，只不过所交换的是控制信息,而不是一般通信操作中所交换的数据信息。

基于共享存储模型的并行编程目前进展不大，主要是在该模型中没有像MPI或PVM那样被广泛接受的统一的语言标准(尽管PCFFortran也是一种很有特色的共享存储的程序设计语言)。目前共享存储的并行程序设计的现状是，为共享存储的某一多处理机系统编写的程序，都不能在其它的多处理机系统中相互移植，更不用说在分布存储的多计算机系统(如MPP和COW)之间运行了。所以,在研究和开发共享存储的并行编程中首要任务是建立实用的标准。下面我们将简要讨论三种与平台无关的共享存储编程模型，即 X3H5、Pthreads和OpenMP。其中X3H5标准虽尚未被广泛接受,但它对一些商用共享存储语言的设计产生了影响，且已渐进到OpenMP标准;而Pthreads在Unix操作系统级的多线程方面是一个颇有影响的标准。

# 13.3.1 ANSI X3H5 共享存储模型

X3H5共享存储模型是1993年建立的ANSI标准，它定义了一个概念标准编程模型,已与C、Fortran77和Fortran90三种语言相结合。下面我们只简介其主要思想,而细节可参阅[16]。

在图13.3中示出了X3H5中所使用的指明并行性的一些结构。并行结构(Parallel Construct)也称为并行区域(Parallel Region),是些成对的(Parallel...endParallel)。程序以单线程(也叫基线程(Base Thread)或主线程(Master Thread)）串行模式开始执行,当其遇到parallel时就开启到并行模式生成多个子线程;基线程及其子线程并行执行其后的代码直到遇到end paralel,然后又返回到串行模式，由基线程继续执行之。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0005_pages_0281-0350/auto/images/033232ec1c74619dd710746900ff900673ea94d7aee47703283f7107bdc6ded9.jpg)  
图13.3 ANSI X3H5标准中并行结构

在并行结构内可有一些并行块(psections...end psections）、并行循环(pdo...endpdo)或单一进程(psingle..endpsingle)等结构,其中并行块用以指明 MPMD并行性,并行循环用于指明 SPMD并行性,而单一进程结构指明代码仅由一个线程顺序执行。

图13.3中的代码执行顺序可以更清楚地示于图13.4中。假定有三个线程P、Q和R：开始基线程P执行代码A;当遇到parallel时就生成两个子线程Q和R,所以代码B被复制成三份;在并行块(psections)中两段代码C和D被并行执行；单进程代码E仅由Q执行；并行循环(pdo)有6次迭代，由三个线程分摊执行；接着 $\mathrm { P } \setminus \mathrm { Q } , \mathrm { R }$ 并行执行代码G；最后由基线程 $\mathbf { P }$ 执行代码 $\mathbf { H } _ { \circ }$ 在此执行过程中,在 parallel、endpsections、end psingle、end pdo 和 end parallel 处设有隐路障(Implicit Barrier),它们也称为栅栏操作(Fence Operation),强使所有存储访问统一于一点以保持一致;如果勿需等待,亦可使用勿需等待隐路障,简称为无隐路障(No Implicit Barrier)。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0005_pages_0281-0350/auto/images/3bdccb346590e4bb05bd5265d190763caee6ffbae1aaf2e3b137ec05edc3fe86.jpg)  
图13.4图13.3的执行过程

在X3H5模型中，线程间的相互作用具有很多很有兴趣的性质：①并行结构中的变量具有共享/私有属性，其中一个线程的私有变量对别的线程是不可见的；②X3H5非常重视存储器的一致性问题，隐路障、栅栏操作和显路障都可用于此目的;③X3H5模型引入四种形式的同步变量，即门锁(Latch)、锁、事件和顺序(Ordinal)。每种类型的变量都伴有初始化操作和释放(Destroy)操作,任何变量在使用前均必须初始化，而采用赋值非初始化状态的办法变可使其释放。锁和事件同步类似于第12.4.2节所讨论的内容；而顺序变量用于按照线程的次第(Rank)进行线程同步,例如可以使用顺序变量指定线程T只有在Ti-1,,Ti在临界区均执行完毕后才能使其进入临界区;门锁变量使用在临界区中,其语法结构如下：

# Critical region[(latch- Variable)]

Critical- section-code

# end Critical region

此结构类似于普通意义的临界区结构，只是可以包含任选的门锁变量而已。使用门锁能减少竞争和增加并行度。

使用X3H5模型,如何编写计算 $\pmb { \pi }$ 的并行程序,留给读者(习题13.5)。

# 13.3.2 POSIX线程模型

POSIX(Portable Operating System Interface)Threads,即 Pthreads,代表官方IEEE POSIX1003.IC-1995线程标准,系由IEEE标准委员会所建立,其功能和界面类似于 Solaris线程的功能与界面。下面我们只简介其公共性质。

线程管理(Thread Management） 线程库用于管理线程,pthreads中基本线程管理原语如表13.3所示。其中 pthread-create()在进程内生成新线程，新线程执行带有变元arg的myroutine,如果pthread_create()生成,则返回0并将新线程之ID置人thread-id,否则返回指明错误类型的错误代码;pthread-exit()结束调用线程并执行清场处理;pthread_self()返回调用线程的 ID;pthread-join()等待其它线程结束。

表13.3Pthreads中基本线程管理原语一览表  

<table><tr><td rowspan=1 colspan=1>功能</td><td rowspan=1 colspan=1>含义</td></tr><tr><td rowspan=1 colspan=1>int pthread_ create (pthread- t * thread- idpthread_ attr- t * attr,void * ( * myroutine)lvoid * ）,void * arg)</td><td rowspan=1 colspan=1>生成线程</td></tr><tr><td rowspan=1 colspan=1>void pthread - exit ( void * status)</td><td rowspan=1 colspan=1>退出线程</td></tr><tr><td rowspan=1 colspan=1>int pthread - join(pthread- t thread,void * * status)</td><td rowspan=1 colspan=1>联合线程</td></tr><tr><td rowspan=1 colspan=1>pthread- t pthread_ self(void)</td><td rowspan=1 colspan=1>返回调用线程ID</td></tr></table>

线程调度pthread-yield()的功能是使调用者将处理机让位于其它线程；pthread-cancel()的功能是终止指定的线程。

Pthread同步Pthread 同步原语列于表13.4中。重点讨论互斥mutex(mutual-Exclusion)变量和条件 Cond(Conditional)变量。前者类似于信号灯结构;后者类似于事件结构。注意,使用同步变量之前需被初始化(生成),用后应

# 释放清除之。

表13.4Pthreads中线程相互作用原语一览表  

<table><tr><td rowspan=1 colspan=1>功能</td><td rowspan=1 colspan=1>含义</td></tr><tr><td rowspan=1 colspan=1>pthread- mutex- init(*…*)</td><td rowspan=1 colspan=1>生成新的互斥变量</td></tr><tr><td rowspan=1 colspan=1>pthread- mutex- destroy(*·*)</td><td rowspan=1 colspan=1>释放互斥变量</td></tr><tr><td rowspan=1 colspan=1>pthread- mutex-lock(*)</td><td rowspan=1 colspan=1>锁住互斥变量</td></tr><tr><td rowspan=1 colspan=1>pthread- mutex- trylock(*·)</td><td rowspan=1 colspan=1>试探锁住互斥变量</td></tr><tr><td rowspan=1 colspan=1>pthread- mutex- unlock(·)</td><td rowspan=1 colspan=1>开锁互斥变量</td></tr><tr><td rowspan=1 colspan=1>pthread- cond.- init(.)</td><td rowspan=1 colspan=1>生成新的条件变量</td></tr><tr><td rowspan=1 colspan=1>pthread- cond- destroy(··*)</td><td rowspan=1 colspan=1>释放条件变量</td></tr><tr><td rowspan=1 colspan=1>pthread- cond- wait(.)</td><td rowspan=1 colspan=1>等待(阻塞)条件变量</td></tr><tr><td rowspan=1 colspan=1>pthread- cond- timedwait(·)</td><td rowspan=1 colspan=1>等待条件变量直至到达时限</td></tr><tr><td rowspan=1 colspan=1>pthread- cond- sinnal()</td><td rowspan=1 colspan=1>投寄一个事件,开锁一个等待进程</td></tr><tr><td rowspan=1 colspan=1>pthread- cond- broadcast(*.)</td><td rowspan=1 colspan=1>投寄一个事件,开锁所有等待进程</td></tr></table>

pthread-mutex-lock()锁住互斥(mutex)变量,如果它未被加锁;如果mutex已被加锁,调用线程一直被阻塞到mutex变成有效。pthread-mutex-trylock()类似于 test-and-set,它一旦锁住 mutex 即立刻返回。pthread-mutex-unlock()释放先前所获得的mutex,当mutex被释,它就能由别的线程获取。

pthread-cond-wait()自动阻塞等待条件满足的现行线程,并开锁mutex变量。pthread-cond-timedwait()与 pthread-cond-wait()类似,除了当等待时间达到时限它将解除阻塞外。pthread-cond-signal()解除等待条件满足的已被阻塞的一个线程的阻塞。pthread-cond-broadcast()将所有等待条件满足的已被阻塞的线程解除阻塞。

使用pthreads编写计算π的程序比较复杂,读者可参见习题13.6。

# 13.3.3Open MP标准

OpenMP是由一组硬件和软件商(如DEC、Intel、IBM、SGI、DOEASCI等)支持的共享存储标准,它是编译制导、库例程和为Unix与Windows NT平台提供环境变量等的集合，于1997年10月公布了用Fortran语言的第一本标准规范，支持C和C++的标准已在计划中,有关OpenMP(OMP)与现存的并行编程标准的比较可综合于表13.5中。其中,Pthreads与OpenMP 相比,Pthreads是不可扩放的,因为它的目标是在低端UnixSMP,而不是变性能计算;Pthreads是低级的，因为它使用库方法，而不是编译制导法，库方法妨碍编译优化;Pthreads仅仅支持线程并行性，它不是细粒度数据并行性;Pthreads只在Unix SMP平台(包括单处理器工作站)中可移植;Pthreads不支持增量并行化,给定一个串行计算程序，用户很难使用Pthreads将其并行化，用户必须虑及很多低级细节，因而Pthreads不能很自然地支持循环 $\left( \log \right)$ 级并行，用户须将串行代码大量修改；而OpenMP能灵活地支持粗粒度并行性，很多串行代码能够简单地并行化。所以OpenMP是一种很有前途的标准,它继承了X3H5很多概念,对PCF和C3H5作了很多改进,然而它尚未被广泛地接受,对于OpenMP而言,关键的问题是开发一个好的编译器和运行环境。

表13.5 五种并行编程标准比较一览表  

<table><tr><td rowspan=1 colspan=1>属性</td><td rowspan=1 colspan=1>X3H5</td><td rowspan=1 colspan=1>MPI</td><td rowspan=1 colspan=1> Pthreads</td><td rowspan=1 colspan=1>HPF</td><td rowspan=1 colspan=1>OpenMP</td></tr><tr><td rowspan=1 colspan=1>可扩放性</td><td rowspan=1 colspan=1>否</td><td rowspan=1 colspan=1>是</td><td rowspan=1 colspan=1>有时是</td><td rowspan=1 colspan=1>是</td><td rowspan=1 colspan=1>是</td></tr><tr><td rowspan=1 colspan=1>Fortran 联编</td><td rowspan=1 colspan=1>是</td><td rowspan=1 colspan=1>是</td><td rowspan=1 colspan=1>香</td><td rowspan=1 colspan=1>是</td><td rowspan=1 colspan=1>是</td></tr><tr><td rowspan=1 colspan=1>C联编（Binding)</td><td rowspan=1 colspan=1>是</td><td rowspan=1 colspan=1>是</td><td rowspan=1 colspan=1>是</td><td rowspan=1 colspan=1>否</td><td rowspan=1 colspan=1>计划中</td></tr><tr><td rowspan=1 colspan=1>高级</td><td rowspan=1 colspan=1>是</td><td rowspan=1 colspan=1>否</td><td rowspan=1 colspan=1>否</td><td rowspan=1 colspan=1>是</td><td rowspan=1 colspan=1>是</td></tr><tr><td rowspan=1 colspan=1>面向性能</td><td rowspan=1 colspan=1>否</td><td rowspan=1 colspan=1>是</td><td rowspan=1 colspan=1>否</td><td rowspan=1 colspan=1>是</td><td rowspan=1 colspan=1>是</td></tr><tr><td rowspan=1 colspan=1>支持数据并行</td><td rowspan=1 colspan=1>是</td><td rowspan=1 colspan=1>香</td><td rowspan=1 colspan=1>香</td><td rowspan=1 colspan=1>是</td><td rowspan=1 colspan=1>是</td></tr><tr><td rowspan=1 colspan=1>可移植性</td><td rowspan=1 colspan=1>是</td><td rowspan=1 colspan=1>是</td><td rowspan=1 colspan=1>是</td><td rowspan=1 colspan=1>是</td><td rowspan=1 colspan=1>是</td></tr><tr><td rowspan=1 colspan=1>销售商支持</td><td rowspan=1 colspan=1>否</td><td rowspan=1 colspan=1>广泛</td><td rowspan=1 colspan=1>UnixSMP</td><td rowspan=1 colspan=1>广泛</td><td rowspan=1 colspan=1>开始</td></tr><tr><td rowspan=1 colspan=1>增量并行化</td><td rowspan=1 colspan=1>是</td><td rowspan=1 colspan=1>香</td><td rowspan=1 colspan=1>否</td><td rowspan=1 colspan=1>否</td><td rowspan=1 colspan=1>是</td></tr></table>

有关OpenMP与X3H5的主要性能比较可综合于表13.6中。OpenMP中加进了孤幼制导(Orphan Directives),它不出现在并行结构的词法范围，而是位于动态执行范围内;OpenMP提供了带有环境变量的一组运行时库例程,它们可用于控制和询问并行执行环境,提供能用锁功能，设置执行模式（例如OpenMP允许吞吐率模式)等;这样系统动态设置用于执行并行区的线程数目,从而能最大化系统的吞吐率;OpenMP比X3H5提供更灵活的控制数据环境的功能，例如可使用REDUCTION(+,sum)子句支持归约操作;OpenMP引人ATOMIC 制导,它允许编译器利用最有效的方式执行变量原子更新,它比互斥结构(例如临界区和锁)更优越。

最后,为了给读者一个直观理解,给出以OpenMP 计算 $\pmb { \pi }$ 的代码段如下,不期望读者完全理解它，但求读者能体会用OpenMP编程的风格。

表13.6 X3H5与OpenMP主要性能比较一览表  

<table><tr><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1>X3H5</td><td rowspan=1 colspan=1>OpenMP</td></tr><tr><td rowspan=3 colspan=1>概观</td><td rowspan=1 colspan=1>孤幼制导(orphan Direcfives)</td><td rowspan=1 colspan=1>无</td><td rowspan=1 colspan=1>OpenMP</td></tr><tr><td rowspan=1 colspan=1>库函数和环境变量</td><td rowspan=1 colspan=1>无</td><td rowspan=1 colspan=1>标准</td></tr><tr><td rowspan=1 colspan=1>吞吐率模式</td><td rowspan=1 colspan=1>未定义</td><td rowspan=1 colspan=1>有</td></tr><tr><td rowspan=4 colspan=1>并行结构</td><td rowspan=1 colspan=1>并行区(region)</td><td rowspan=1 colspan=1> PARALLEL</td><td rowspan=1 colspan=1> PARALLEL</td></tr><tr><td rowspan=1 colspan=1>迭代</td><td rowspan=1 colspan=1>PDO</td><td rowspan=1 colspan=1>DO</td></tr><tr><td rowspan=1 colspan=1>非迭代</td><td rowspan=1 colspan=1>PSECTION</td><td rowspan=1 colspan=1>SECTION</td></tr><tr><td rowspan=1 colspan=1>单线程</td><td rowspan=1 colspan=1>PSINGLE</td><td rowspan=1 colspan=1>SINGLE,MASTER</td></tr><tr><td rowspan=4 colspan=1>数据环境</td><td rowspan=1 colspan=1>自动作用域</td><td rowspan=1 colspan=1>无</td><td rowspan=1 colspan=1>DEFAULT</td></tr><tr><td rowspan=1 colspan=1>归约</td><td rowspan=1 colspan=1>无</td><td rowspan=1 colspan=1>REDUCTION</td></tr><tr><td rowspan=1 colspan=1>私有初始化</td><td rowspan=1 colspan=1>无</td><td rowspan=1 colspan=1>FIRSTPRIVATE,COPYIN</td></tr><tr><td rowspan=1 colspan=1>私有存留</td><td rowspan=1 colspan=1>无</td><td rowspan=1 colspan=1>LASTPRIVATE</td></tr><tr><td rowspan=5 colspan=1>同步结构</td><td rowspan=1 colspan=1>路障</td><td rowspan=1 colspan=1>BARRIER</td><td rowspan=1 colspan=1>BARRIER</td></tr><tr><td rowspan=1 colspan=1>栅栏</td><td rowspan=1 colspan=1>SYNCHRONIZE</td><td rowspan=1 colspan=1>FLUSH</td></tr><tr><td rowspan=1 colspan=1>临界区</td><td rowspan=1 colspan=1>CRITICAL SECTION</td><td rowspan=1 colspan=1>CRITICA</td></tr><tr><td rowspan=1 colspan=1>自动区域</td><td rowspan=1 colspan=1>无</td><td rowspan=1 colspan=1>ATOMIC</td></tr><tr><td rowspan=1 colspan=1>锁</td><td rowspan=1 colspan=1>无</td><td rowspan=1 colspan=1>全功能</td></tr></table>

# $/ / *$ 计算 $\pmb { \pi }$ OpenMP编程代码段 $\star$ //

Program Compute-pi integer n,i $\mathbf { r e a l \ w } , \mathbf { x } , \mathbf { s u m } , \mathbf { p i } , \mathbf { f } , \mathbf { a }$

C function to integrate

$$
\begin{array} { r l } & { \mathrm { f ( a ) } = 4 . \mathrm { d } 0 / ( 1 . \mathrm { d } 0 + \mathrm { a } \ast \mathrm { a } ) } \\ & { \mathrm { p r i n t } \ast \mathrm { , } ^ { \prime } \mathrm { E n t e r ~ n u m b e r ~ o f ~ i n t e r v a l s } \ast } \\ & { \mathrm { r e a d } \ast \mathrm { , n } } \end{array}
$$

C calculate the interval size

$$
\begin{array} { l } { \mathbf { w } { = } 1 . \mathbf { d } 0 / \mathbf { n } } \\ { \mathbf { s u m } { = } 0 . 0 \mathbf { d } \mathbf { o } } \end{array}
$$

！\$ OMP PARALLEL DO PRIVATE(x),SHARED(w),REDUCTION（ + : sum)

$\mathbf { d o } \ \mathbf { i } = \mathbf { 1 } , \mathbf { n }$ $\begin{array} { r l } & { \mathbf { \lambda } ^ { = 1 } , \mathbf { n } } \\ & { \mathbf { \lambda } \mathbf { x } = \mathbf { w } \ast \left( \mathrm { i } + 0 . 5 \mathrm { d } 0 \right) } \\ & { \mathbf { \lambda } \mathbf { s u m } = \mathbf { s u m } + \mathbf { f } \left( \mathbf { x } \right) } \end{array}$ enddo ！ $\$ 9$ OMP END PARALLEL DO ${ \mathrm { \bf p i } } = { \bf w } * { \mathrm { \bf s u m } }$ print $\star$ ,'compute $\mathrm { \ p i = ' }$ ,pi stop end

# 13.4 小结和导读

小结本章首先简要介绍的五种常用的构造运行在并行机上的并行算法（并行编程)的方法，在实际的并行程序中经常可以不同的方式组合使用。这些方法都是从以往大量使用的方法中归纳出来的,实践证明它们都是行之有效的。本章仅讨论了四种并行程序设计模型,其中最为流行的是数据并行、消息传递和共享变量三种模型。另外,还有一些其它的并行程序设计模型,包括函数式程序设计模型（也称之为数据流风格）、逻辑程序设计模型(它以谓词逻辑为基础,描述输人和输出之间的逻辑关系,适用于涉及大型数据库的知识处理等）、面向对象的程序设计模型(按此风格,程序由一些对象组成,每个对象都是一个抽象的数据类型,即一组数据结构及其该数据结构上的一组操作,并行程序设计模型将低级对象,如进程和信号灯等,组合起来形成高级对象,如程序模块等)等。至于共享存储的编程方法，本章只简单讨论了X3H5、Pthreads和OpenMP三个标准,另外还有像 SGIPower C和新型并行C语言C//等,前者是串行C语言的推广,具有编译制导和库函数;后者是基于标准C语言，具有少量的为并行和进程相互作用的一组扩展结构。

导读讨论并行程序(并行算法)设计风范目前已有好几本书,最新近的一本是[88]。有关并行化编译技术，[25][109][184]都是很好的人门读物,Illinois对并行化编译的研究读者可参阅[32][33][34]。X3H5标准在[16]中给于了描述，POSIX在[141]中进行了讨论,有关OpenMP标准描述在[133][134]中,SGIPowerC编程模型读者可参阅[159],新型并行语言C//读者可参阅[186],函数式程序设计语言讨论在[9]中,面向对象方法讨论在[6]中,应用C++进行并行编程读者可参阅[182],分布计算系统程序设计语言读者可参阅[23]。

# 习 题

13.1试分析下列循环嵌套中各语句间的相关关系：

$$
\begin{array} { r l } & { \mathrm { ~ D O ~ I = 1 , N ~ } } \\ & { ~ \mathrm { ~ \bf ~ D O ~ J = 2 , N ~ } } \\ & { ~ \mathrm { S _ { 1 } : \quad \quad ~ A ( I , J ) = A ( I , J - 1 ) + B ( I , J ) ~ } } \\ & { ~ \mathrm { S _ { 2 } : \quad \quad ~ C ( I , J ) = A ( I , J ) + D ( I + 1 , J ) ~ } } \\ & { ~ \mathrm { S _ { 3 } : \quad \quad ~ D ( I , J ) = 0 . 1 ~ } } \end{array}
$$

# Enddo

# Enddo

$$
\begin{array} { r l r l } { \textcircled { 2 } } & { \mathbf { D O \ I = 1 , N } } \\ & { \mathbf { S _ { 1 } : } } & { \mathbf { A ( I ) = B ( I ) } } \\ & { \mathbf { S _ { 2 } : } } & { \mathbf { C ( I ) = A ( I ) + B ( I ) } } \\ & { \mathbf { S _ { 3 } : } } & { \mathbf { D ( I ) = C ( I + 1 ) } } \end{array}
$$

# Enddo

$\textcircled{3}$ DO I= $\begin{array} { l } { { 1 , \mathrm { N } } } \\ { { \displaystyle { \bf \beta } } } \\ { { \displaystyle { \bf \beta } } } \\ { { \displaystyle { \bf \cal A } ( { \bf I } , { \bf J } ) = { \bf B } ( { \bf I } , { \bf J } ) + \mathrm { C } ( { \bf I } , { \bf J } ) } } \\ { { \displaystyle { \bf C } ( { \bf I } , { \bf J } ) = \mathrm { D } ( { \bf I } , { \bf J } ) / 2 } } \\ { { \displaystyle { \bf E } ( { \bf I } , { \bf J } ) = { \bf A } ( { \bf I } , { \bf J } - 1 ) * * 2 + \mathrm { E } ( { \bf I } , { \bf J } - 1 ) } } \end{array}$   
$\mathsf { S } _ { 1 }$ ：   
$S _ { 2 }$ ：   
$S _ { 3 }$ ：   
Enddo   
Enddo

13.2计算两整数数组之内积的串行代码段如下：

$$
\begin{array} { c } { \begin{array} { r l } & { \mathrm { S u m = 0 ; } } \\ & { \mathrm { f o r ( i = 0 ; i < N ; i + \Delta + \Delta ) } } \\ & { \qquad \mathrm { S u m = S u m + A [ i ] * B [ i ] ; } } \end{array} } \end{array}
$$

试用 $\textcircled{1}$ 相并行； $\textcircled{2}$ 分治并行； $\textcircled{3}$ 流水线并行； $\textcircled{4}$ 主-从行并行； $\textcircled{5}$ 工作池并行等五种并行编程范例，写出如上计算内积的并行代码段。

13.3试解释：隐并行模型在并行性、数据分配、相互作用，可编程性,可移植性和程序正确性等方面，为什么均优于显式模型。

13.4令 $\mathbf { N } = 1 0 ^ { 5 }$ 和 $\mathbf { N } = 1 0 ^ { 8 }$ ，试编写计算 $\pmb { \pi }$ 的 SPMD并行程序,并在您现有的共享存储的平台上调试之;同时应执行在1,2,3,4,5,6,7和8个处理器上。

13.5试用X3H5模型,写出计算 $\pmb { \pi }$ 的并行程序。

13.6下面是使用Pthreads方法计算 $\pmb { \pi }$ 的一种并行代码段：

# $/ / *$ 计算 $\pmb { \pi }$ Pthreads编程代码段＊//

# include $<$ pthread.h> $\big / \ast$ 线程控制所需的头文件 $\pmb { \mathscr { k } }$ / # include <synch.h> ／＊同步操作所需的头文件 $\star$ /   
extern unsigned $\star$ micro-timer; $\curvearrowright$ 系统计时变量 $\star$ /   
unsigned int fin,start;   
semaphore- t semaphore;   
barrier-spin- t barrier; $\nearrow$ 同步信号量说明 $\yen 7$   
double delta, pi;   
typedef struct| $\big / \big \varkappa$ 定义参数结构\*／ int low; int high;   
Arg;   
$\nearrow$ 定义线程执行的函数 $\star$ /   
void child(arg)   
Arg \* arg   
！ int $\mathrm { l o w } = \mathrm { a r g } \mathrm { \to l o w }$ int $\mathbf { h i g h } = \mathbf { a r g } \mathbf { \to } \mathbf { h i g h }$ ： int i； double $\pmb { \ x }$ $\mathbf { \nabla } , \mathsf { p a r t } = \mathbf { 0 } . \mathbf { 0 }$ ； $\mathbf { \acute { f o r } } ( \mathrm { i } = \mathrm { l o w } ; \mathrm { i } < = \mathrm { h i g h } ; \mathrm { i } + \mathbf { \acute { \alpha } } + \mathbf { \acute { \beta } } \mathbf { \acute { \alpha } } ) \left\{ \begin{array} { r l r } \end{array} \right.$ $\mathbf { x } = ( \mathop { \mathrm { i } } + 0 . 5 ) \not \times \mathrm { d e l t a } ;$ ${ \bf p a r t + \delta } = 1 . 0 / \big ( 1 . 0 + { \bf x * x } \big ) ;$ psema( &semaphore); $\curvearrowright$ 利用信号量进行互斥累加\*／ $\mathrm { p i } + = 4 . 0 \star \mathrm { d e l t a } \star \mathrm { p a r t } ;$ vsema( &semaphore); -barrier- spin(&barrier); $\nearrow$ 线程在完成计算后需barrier 同步 $\star$ / pthread-exit(); $\swarrow \ast$ 线程终止 $^ { \star }$ /   
一   
main(argc,argv)   
int argc;   
char $\clubsuit$ argv[]; int no-of-_ threads,segments,i; pthread-t thread; Arg $\bigstar$ arg;   
if $( \tt a r g c ! = 3 )$ printf("usage:pi<no-of-threads><no-of-strips>\n"); exit(1);   
！   
no-of-threads $=$ atoi(argv[1]）;   
segments atoi(argv[2];   
delta ${ \bf \varepsilon } = 1 . 0$ /segments;   
$\bf { \dot { p } } i = 0 . 0$ ；   
sema- init(&semaphore,1)； $\nearrow$ 初始化同步变量 $\pmb { \mathscr { k } }$ /   
-barrier-spin-init(&barrier,no-of-threads $\mathbf { \nabla } + \mathbf { 1 }$ ）；   
start $\qquad = \quad \star$ micro- timer; $\big / \ast$ 线程开始计时 $\yen 7$   
$\mathbf { f o r } ( \mathrm { i } = 0 ; \mathrm { i } < \mathrm { n o \_ o f \_ t h r e a d s } ; \mathrm { i } + \mathit { \Theta } + \mathit { \Theta } ) \left\{ \begin{array} { l l } { \begin{array} { r l r } \end{array} } \end{array} \right.$ /\*启动线程 $\bigstar$ / ${ \bf a r g } = ( { \bf A r g } * { \bf \theta } ) { \bf m a l l o c } ( \mathrm { s i z e ~ o f ~ ( A r g ) } )$ $\mathbf { a r g } \to \mathrm { l o w } = \mathrm { i } \star$ segments/no- of- threads; $\mathbf { a r g } \mathbf {  } \mathbf { h i g h } = ( \mathrm { i } + 1 ) \mathrm { * \ s e g m e n t s / n o \_ o f } \mathbf { - } \mathbf { t h r e a d s } \cdot \mathbf { 1 } ;$ pthread- create( &thread,pthread- attr_default,child,arg);   
一   
-barrier- spin(&barrier)； $\prime *$ 主进程等待所有子线程结束\*／   
$\mathbf { f i n } = \mathbf { \nabla } \ast$ micro- timer; $\big / \big \langle \big \varkappa$ 线程结束记时 $\bigstar$ /   
printf $( ^ { \prime \prime } { \bf \tilde { \tau } } { \bf \tilde { \tau } } { \bf u } \setminus { \bf \tilde { \tau } } { \bf \tilde { \tau } } ^ { \prime \prime }$ ,fin - start);   
printf("\npit\t%15.14f\n",pi);   
$\textcircled{1}$ 试解释上述代码段的工作流程。   
$\textcircled{2}$ 通过三种模型X3H5、Pthreads和 OpenMP上计算 $\pmb { \pi }$ 的代码段，比较它们的编程风格 的异同和优缺点。

13.7消息传递模型可支持MPMD和 SPMD两种编程方式。下面给出 SPMD方式的计算 $\pmb { \pi }$ 的并行Fortran代码段[NX]：

$\ d s / \ d t \nearrow \ d s$ 计算 $\pmb { \pi }$ Fortran 语言 SPMD 编程代码段 $^ { \star }$ / Program pi node include 'fnx.h' double precision h,sum,x,pi,f,a,temp integer n integer nodes,iam,intsize data intsize /4/ C Define the function $\mathbf { f } ( \mathbf { a } ) = 4 . \mathbf { d 0 } / ( 1 . \mathbf { d 0 } + \mathbf { a } * \mathbf { a } )$

C DO some bookkeeping iam $\eqslantless$ mynode() $\big / \big \langle \big \varkappa$ 获得调用进程的节点号 $\bigstar$ / nodes $=$ numnodes() $\big / \big \varkappa$ 获得分配给应用程序的节

点数 $\bigstar$ / 1 if(iam· eq 0) then print $\star$ ,'enter number of intervals:' $\mathrm { r e a d } ( 5 , \ast , { \mathrm e n d } = 1 0 0 ) \mathrm { ~ r ~ }$ call csend(300,n,intsize,-1,0) /\*同步发送 $\star$ / else call crecv(300,n,intsize） $\big / \big \varkappa$ 同步接收\*/ endif C Calulate the scaling factor $\mathbf { h } { } { } = 1 . { } \mathbf { d } \mathbf { 0 } / \mathbf { n }$ C Integrate the value of $\pmb { \kappa }$ used to calculate the slice is the C value of the midpoint of the integration slice $\begin{array} { c } { \begin{array} { r l } & { \operatorname { s u m } = 0 . \operatorname { d } 0 } \\ & { \operatorname { d } \mathbf { 0 } 1 0 \ \operatorname { i } = \operatorname { i } = \operatorname { i } 0 . 1 , \operatorname { n } , \operatorname { n o d e s } } \\ & { \qquad \operatorname { x } = \operatorname { h } * ( \operatorname { d o u b l e } ( \operatorname { i } ) - 0 . 5 ) } \\ & { \qquad \operatorname { s u m } = \operatorname { s u m } + \operatorname { f } ( \mathbf { x } ) } \end{array} } \end{array}$ 10 continue $\mathsf { p i } { = } \mathsf { h } \star \mathsf { s u m }$ call gdsum(pi,1,temp) $\big / \ast$ 计算双精度全和 $\divideontimes$ / $\mathbf { i f } ( \mathrm { i a m } \cdot \mathbf { e q } \cdot \mathbf { 0 } ) \ \mathbf { t h e n }$ C Output the answer print $\pmb { \mathscr { k } }$ ,'the value of pi for', $\pmb { \mathrm { n } }$ ,'interval is',pi endif go to 1 C Terminate all nodes 100 $\mathbf { i } = \mathbb { K i l l } ( \mathbf { 0 } . \mathbf { 9 } )$ end 试解释上述代码段的计算过程。

13.8下面是使用经理员工(Manager-Worker)模型(即主-从模型)求解N-皇后问题的并行代码段：

$/ / \ *$ 求解 $\mathbb { N } \cdot$ 皇后经理-员工编程代码段 $\pmb { \mathscr { k } }$ /1$\nearrow$ Manager程序段 $\star$ /if (!iam) $\{ \nearrow$ 如果我是节点 $\mathbf { 0 } \ast { \mathbf { \zeta } } { \mathit { \prime } }$

printf("\n STARTING… \n"); while(get-board(board) $\bumpeq$ !DONE){ crecv(READY,NULL,0) ; nodenbr $=$ infonode() ; msgcount++;/\*计数多少节点准备好＊/ csend(TASK,board,sizeof(two ,two D),nodenbr,0); msgcount- - ; ！ /\*等待所有员工空闲 $^ \star$ / $\begin{array} { r l } & { \mathrm { ~ \forall ~ \eta ~ h i l e ( m s g c o u n t ! = n o d e s - 1 )  \{ \begin{array} { l l } { \eta } \\ { \eta \mathrm { e c v ( R E A D Y , N U L L , 0 )  \{ \begin{array} { l l } { \eta } \\ { \eta } \end{array}  } } \\ { m s g c o u n t + \mathrm {   ~ \{ ~ \} ~ } } \end{array}  } }  \end{array}$ $\big / \ast$ 发送FINISHED消息给所有节点，并退出 $\yen 7$ board[0][0] $\underline { { \underline { { \mathbf { \delta \pi } } } } }$ FINISHED; csend(TASK,board,sizeof(two D),-1,0); goodbye(); 一 else|/ $\clubsuit$ 员工程序段 $\yen 7$ $\mathbf { f o r ( \lambda _ { i } ; \lambda ) } \left\{ \begin{array} { l l } \end{array} \right.$ csend(READY,0,0,0,0); crecv(TASK,board,sizeof(board)) ; if(board[0][0] $= =$ FINISHED goodbye(); if(chk-board(board)) move- to-right(board,0,MCOLS); ！

# 试解释上述代码段的计算过程。


<!-- chunk 0006: pages 351-420 -->
# 第十四章 分布存储系统并行编程

从并行程序设计的角度来看，分布存储系统的主要特点是：系统通过互连网络将多个处理器连接起来，每个处理器均有自己的局部存储器，所有的局部存储器就构成了整个地址空间;整个地址空间有局部和全局两种编址方式，全局编址方式是指系统的所有局部存储器统一编址，用户程序空间是一个统一的全局地址空间，其中远程存储器的访问与局部存储器的访问一样用指令来完成，其指令地址由处理器号和局部存储器地址所组成。局部编址方式是系统中各局部存储器单独编址，用户程序空间是多地址空间,远程存储器的访问要通过调用消息传递库程序来实现的。

上述的特点，导致了分布存储系统的两种并行编程模型：消息传递模型和数据并行模型。实现消息传递有 SPMD(单程序多数据流)和MPMD(多程序多数据流)两种模式;实现数据并行有 SIMD(单指令多数据流)和 SPMD 两种模式。在分布存储的SIMD体系结构上可以实现 SPMD模式的数据并行;在分布存储的 MIMD体系结构上可以实现 SPMD模式的数据并行,也可以实现MPMD模式的消息传递。

本章首先讨论消息传递的并行编程,着重讨论MPI而顺便介绍一下PVM 并行编程环境;然后讨论数据并行编程,着重讨论HPF 而穿插提及一下Fortran 90。

# 14.1 基于消息传递的并行编程

所谓基于消息传递的并行编程,是指用户必须显式地通过发送和接收消息来实现处理器之间的数据交换。这种编程方式是大规模并行处理机MPP 和工作站机群COW采用的主要编程方式。在这种并行编程中，每个进程均有自己独立的地址空间,一个进程不能直接访问其它进程中的数据,这种远程访问必须通过消息传递来实现。因为消息传递的开销比较大，所以它主要用来开发大粒度和粗粒度的并行性。

根据问题分解的两种形式，消息传递并行性的开发也有两种形式：域分解形式,即将一个大的问题区域分解成若干个较小的问题区域,然后对其并行求解;函数分解(也有人称为功能分解)形式,即将一个大的问题分解成若干个子问题，然后对其并行求解。相应于这两种形式，就有所谓SPMD编程和MPMD编程两种模式。

# 14.1.1 SPMD并行程序

基于域分解的思想开发出的并行程序，通常组织成SPMD形式。SPMD就是同一程序复制到各个处理器上，而不同的数据分布在不同的处理器上。这样在系统中各处理器均运行相同的程序，但对不同的数据执行操作。在大量的处理器上运行用户软件,为了减少管理指令流的复杂性,加大并行粒度,用 SPMD程序代替SIMD程序是很自然的。

设计SPMD形式的消息传递程序的主要步骤是： $\textcircled{1}$ 数据划分：尽量考虑负载平衡、存储空间的均衡使用以及减少处理器之间的通信； $\textcircled{2}$ 优化通信：尽量提高计算/通信比,数据就地使用和合并短消息成一个长消息进行传输； $\textcircled{3}$ 全局操作：将各处理器之局部结果组合起来形成整个问题的解,像这样的操作包括全局同步、广播、归约、前缀运算、聚集/散射等。

编写 SPMD形式的程序有两种方式：主机/节点(Host/Node)式和无主机(Hostless)式,兹分述如下：

主机/节点结构在此结构中，一个应用程序由两部分组成：一是主机程序，二是节点程序。主机程序运行在控制节点上,节点程序运行在所有的计算节点上。这种形式的程序，实际上是一个主机程序控制一组以SPMD方式执行的节点程序。主机程序的功能是： $\textcircled{1}$ 申请和释放处理器,加载节点程序； $\textcircled{2}$ 执行I/O和处理用户界面； $\textcircled{3}$ 发送数据给各节点处理器,并收集各处理器的计算结果。节点程序的功能是： $\textcircled{1}$ 接收来自主机的输入信息； $\textcircled{2}$ 完成各自的局部计算,施行计算节点间的通信； $\textcircled{3}$ 回送计算结果给主机。主机/节点结构的主要优点是： $\textcircled{1}$ 易于并行编程：欲将一个已有的串行程序修改成主机/节点形式的并行程序时，原有程序中的I/O与用户界面部分(代码量大但运行时间短)可以完全不变，而只需并行化计算部分(代码量小但运行时间长),这样开发并行程序代价较低； $\textcircled{2}$ 充分利用主机的特殊能力：在很多MPP系统中,计算节点通常只提供最基本的操作系统功能，而图形功能、I/O功能和数据库接口功能等通常远不如控制节点强,对于需要图形功能或数据库接口功能的应用软件来说,主机/节点结构可以充分利用主机功能强的优势。但主机/节点结构也有些不足,主要是： $\textcircled{1}$ 调试困难：采用主机/节点结构，一般不允许节点程序直接进行自己的I/O,这样当用户试图用打印信息来定位错误时,用户必须同时修改主机和节点程序,以便两者协调输出所需之信息；②维护困难：因为主机/节点结构涉及到两类节点，当两类节点结构上(字节次序、最高有效位之位置、数据类型长度不一致等)有差异时，两个程序之间交换数据产生困难,给维护增加了难度；③可移植性差：因为主机/节点程序不能直接在串行机上执行，所以用户常常需要为一个应用软件保持一个并行版本和一个串行版本，用户负担过大，给程序移植带来困难。

无主机结构在此结构中，一个应用程序整个地运行在计算节点上，而控制节点不起上节所说的主机节点的作用，所运行的实际上是一个系统提供的通用$\mathbf { I } / \mathbf { O }$ 服务程序，它为计算节点提供I/O服务和计算节点所不具备的操作系统请求服务。在这种结构中，程序控制也是在计算节点上完成的。无主机结构的主要优点是： $\textcircled{1}$ 易于程序开发、维护和移植：因为只涉及一类节点，用户只需写一种应用程序； $\textcircled{2}$ 程序较易调试：因为程序可以在计算节点上，直接使用标准的I/O功能进行调试； $\textcircled{3}$ 程序的正确性易于保证：因为在无主机结构上书写的并行程序,可以不加修改或少量修改即可在串行机上运行。

由于上述优点,无主机结构已成为编写 SPMD程序的主要方式。

# 14.1.2 MPMD并行程序

基于函数分解思想开发出的并行程序,通常组织成MPMD形式。MPMD就是每个处理器执行不同的代码副本、各自对数据完成不同的运算。在诸如事务处理的应用中,由于各子功能本身固有的异构性;以及在异构网络环境下，由于各计算机资源差异性，用MPMD结构的程序是很合适的。

设计MPMD形式的消息传递程序的主要步骤是： $\textcircled{1}$ 子问题划分：尽量考虑各处理器负载均衡和充分利用各处理器的独特能力,在全系统范围内合理分配各子问题于不同处理器上； $\textcircled{2}$ 确定子问题之间的相互作用方式。

实现子问题之间相互作用方式有两种：数据流方式和客户/服务器方式，兹分述如下：

数据流方式在此方式的 MPMD程序中，用户将问题分解为各不相同的子问题；根据子问题的相关性来组织并行，按数据驱动(Data-Driven)的方式决定并行执行的先后次序。这种方式主要应用于异构型计算环境中的应用软件的开发。

客户/服务器方式在此方式的 MPMD程序中，用户将一些典型的不同的子问题求解作为相应的服务进程分布于各个计算节点上；整个问题的求解就归结为客户对各个服务器的一系列服务请求。这种方式主要应用于某类特殊的应用领域。在这些应用领域中，将一些普遍性的子功能(例如数据库应用中的插入、删除和查询等)作为服务进程,可以大大减轻用户重复开发具体应用软件的负担。

客户/服务器方式是一种需求驱动(Demand-Driven）（数据流方式是一种数据驱动）。用户所请求的服务可以是信息服务、计算服务或资源服务。客户/服务器方式的显著特点是非对等性，即客户与服务器地位不对等，服务器拥有客户所不具有的硬件资源和运算能力，服务器提供服务，客户请求服务。这种方式特别适合于子功能比较通用的应用领域。一个客户/服务器方式的MPMD程序示意图如图14.1所示。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0006_pages_0351-0420/auto/images/f1659d525ca3694f6dd51f31c0d504ec94210760121ecb02b8c131d15f8b8fc4.jpg)  
图14.1客户/服务器方式的MPMD程序

# 14.2 MPI并行编程

在消息传递库方法的并行编程中，一组进程所执行的程序是用标准串行语言书写的代码加上用于消息接收和发送的库函数调用。其中,MPI(MessagePassing Interface)就是1994年5月发布的一种消息传递接口。它实际上是一个消息传递函数库的标准说明，吸取了众多消息传递系统的优点，是目前国际上最流行的并行编程环境之一（其它的系统包括P4、PVM、Express和PARMACS等）。MPI具有许多优点：具有可移植性和易用性；有完备的异步通信功能；有正式和详细的精确定义，因而为并行软件产业的增长提供了必要的条件。

在基于MPI编程模型中，计算是由一个或多个彼此通过调用库函数进行消息收、发通信的进程所组成。在绝大部分MPI实现中，一组固定的进程在程序初始化时生成，一个处理器生成一个进程。这些进程可以执行相同或不同的程序（相应地称为SPMD或MPMD模式）。进程间的通信可以是点到点的，也可以是群体的（Collective)。或许MPI最重要的特性就是使用了称之为通信体(Communicator)的机构,允许程序员定义一种封装内部通信结构的模块。所谓通信体就是一个进程组(Process Group)加上进程活动环境(Context),其中进程组就是一组有限和有序进程集合。所谓有限意即组内包含有限数目的n个进程;所谓有序意即n个进程依次按0,1,,n-1整数定序(Ranked)。MPI中的进程活动环境(Contexts),也称为上下文,是系统指定的超级标记(Supertag)，它能安全地将彼此相互冲突的通信区分开来。每个通信体都有一个不同的、系统指定的进程活动环境，一条在一个进程活动环境中发送的消息不能在另一个进程活动环境中被接收。通信体的作用，请参阅习题14.1。

# 14.2.1最基本的 MPI

MPI是个复杂的系统，它包含了129个函数(根据1994年发布的MPI标准)。事实上,1997年修订的标准,称之为MPI-2,已超过200,目前最常用的也有约30个。然而我们可以只使用其中的6个最基本的函数就能编写一个完整的 MPI程序去求解很多问题。这6个基本函数,包括启动和结束计算,识别进程以及发送与接收消息：

MPI_INIT: 启动MPI计算MPI_FINALIZE: 结束MPI计算MPI_COMM_SIZE: 确定进程数MPI_COMM_RANK: 确定自己的进程标识符MPI _SEND: 发送一条消息MPI_RECV: 接收一条消息

函数的功能及其参数描述在图14.2中,其中标号IN、OUT和 INOUT分别指明函数使用但不能修改参数、函数不使用但可修改参数以及函数既可使用也可修改参数。

MPI_INIT(int \*argc,char \* \* \* argv)   
Initiate a computation . argc,argv are required only in the C language binding, where they are the main program's arguments.

MPI_FINALIZE() Shut down a computation .

MPI_COMM_SIZE(comm,size) Determine the number of proceses in a computation .

IN comm communicator(handle) OUT size number of processes in the group of comm(integer)

MPI_COMM_RANK(comm,pid).

Determine the identifier of the current process.

IN comm communicator(handle) OUT pid process id in the group of comm(integer)

MPI_ SEND(buf,count,datatype,dest,tag,comm).   
Send a message.

IN buf address of send buffer(choice) IN count number of elements to send (integer≥0) IN datatype datatype of send buffer elerments(handle) IN dest process id of destination process(integer) IN tag message tag(integer) IN comm communicator(handle)

MPI_RECV(buf,count,datatype,source,tag,comm,status)   
Receive a message . OUT buf address of receive buffer(choice) IN count size of receive buffer,in elements(integer $\mathtt { > 0 }$ ） IN datatype datatype of receive buffer,elements(handle) IN source process id of source process,or MPI_ANY_SOURCE(integer) IN tag message tag,or MPI_ANY_TAG(integer) IN comm communicator( handle) OUT status status object(status)

只使用6个基本函数中的4个即可写出如下一段MPI程序：

program main   
begin MPI_INIT() $\big / \ast$ 启动计算 $\yen 7$ MPI_COMM_SIZE(MPI_COMM_WORLD,count) $\big / \big \langle \big \varkappa$ 找进程数 $\yen 7$ MPI_COMM_RANK(MPI_COMM_WORLD,myid) $\big / \ast$ 找自己的 $\yen 12$ print("I am",myid,"of",count) $\big / \big | \big | \big |$ 打印消息 $\yen 7$ MPI_FINALIZE（） $\big / \ast$ 结束计算 $\yen 7$   
end

其中,MPI_COMM_WORLD是一个缺省的进程组,它指明所有的进程都参与计算。

MPI不是一个独立的、自包含的软件系统,MPI进程是重量级、单线程的进程,MPI标准并不指明如何启动并行计算，它可通过命令行参数指明应被生成的进程数目，然后按SPMD方式或MPMD方式执行程序。MPI函数库本身是与语言无关的，也就是说,库函数的描述可以使用C语言、Fortran语言或其它的语言。目前 MPI库函数提供了C语言和 Fortran 语言描述(称为LanguageBinding)。在C语言描述中,函数名均冠以MPI前缀,且其首字母需大写。返回的状态值是整数；成功完成的返回代码是MPI_SUCCESS；失败时也会定义一组错误代码。编译时的常数均须大写且被定义在文件mpi.h中,mpi.h在任何需调用MPI的程序中必须被包含进来。句柄(Handles)由定义在mpi.h中的特殊类型所表示。具有类型IN的函数参数由值传送；具有类型OUT和 IN-OUT的函数参数由引用传送(例如指针）。MPI的数据类型定义成C和Fortran语言的数据类型，如表14.1所示。

在Fortran语言描述中,函数名均冠以MPI前缀，且均须大写。函数返回代码由一个附加的整数变量表示之;成功完成的返回代码是MPI_SUCCESS；失败时也会定义一组错误代码。编译时的常数均须大写且被定义在文件mpif.h中,它在任何需调用MPI的程序中必须被包含进来。所有句柄均具有类型 IN-TEGER。MPI的数据类型如表14.1所示。

表14.1 MPI中的数据类型一览表  

<table><tr><td rowspan=1 colspan=1>MPI(C Binding)</td><td rowspan=1 colspan=1>C</td><td rowspan=1 colspan=1>MPI(Fortran Binding)</td><td rowspan=1 colspan=1>Fortran</td></tr><tr><td rowspan=1 colspan=1>MPI_BYTE</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>MPI_BYTE</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>MPI_CHAR</td><td rowspan=1 colspan=1> signed char</td><td rowspan=1 colspan=1>MPI_CHARACTER</td><td rowspan=1 colspan=1>CHARACTER(1)</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>MPI_COMPLEX</td><td rowspan=1 colspan=1>COMPLEX</td></tr><tr><td rowspan=1 colspan=1>MPI_DOULBE</td><td rowspan=1 colspan=1>double</td><td rowspan=1 colspan=1>MPI_DOUBLE._PRECISION</td><td rowspan=1 colspan=1>DOUBLE1PRECISION</td></tr><tr><td rowspan=1 colspan=1>MPI_FLOAT</td><td rowspan=1 colspan=1>float</td><td rowspan=1 colspan=1>MPI_REAL</td><td rowspan=1 colspan=1>REAL</td></tr><tr><td rowspan=1 colspan=1>MPI_ INT</td><td rowspan=1 colspan=1>int</td><td rowspan=1 colspan=1>MPI_INTEGER</td><td rowspan=1 colspan=1>INTEGER</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>MPI _LOGICAL</td><td rowspan=1 colspan=1>LOGICAL</td></tr><tr><td rowspan=1 colspan=1>MPI_LONG</td><td rowspan=1 colspan=1>long</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>MPI_LONG_DOUBLE  ：</td><td rowspan=1 colspan=1>long double</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>MPI_PACKED</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>MPI_PACKED</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>MPI_SHORT</td><td rowspan=1 colspan=1>short</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>MPI_UNSIGNED_CHAR</td><td rowspan=1 colspan=1>unsigned char</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>MPI一UNSIGNED</td><td rowspan=1 colspan=1>unsigned int</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>MPI_UNSIGNED_LONG</td><td rowspan=1 colspan=1> unsigned long</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>MPI _UNSIGNED_SHORT</td><td rowspan=1 colspan=1> unsigned short</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

# 14.2.2群体通信

MPI并行程序中经常需要一些进程组间的群体通信(CollectiveCommunica-tion),包括：①路障(Barrier)：同步所有进程;②播送(Broadcast）：从一个进程发送一条数据给所有进程；③收集(Gather)：从所有进程收集数据到一个进程；④散射(Scatter)：从一个进程散发多条数据给所有进程；③归约(Reduction）：包括求和、求积等。这些函数的功能及其参数描述在图14.3中，播送、收集和散射的几何意义示于图14.4中。

MPI_REDUCE和 MPI_ALLREDUCE 均执行归约操作,它们组合每个进程中输入缓冲器中的值,返回组合后的值于单一根进程的输出缓冲器中（MPI_REDUCE)或者于所有进程的输出缓冲器中（MPI_ALLREDUCE)。组合所使用的操作包括最大和最小（MPI_MAX和MPI_MIN);求和与求积（MPI_SUM和 MPI_PROD);逻辑与、逻辑或以及异或(MPI_LAND、MPI_LOR 和MPI_LXOR);按位与、按位或以及按位异或(MPI_BAND、MPI_BOR 和 MPI_BXOR)。

MPI_BARRIER(comm)   
Global synchronization . IN comm communicator( handle)   
MPI_BCAST(inbuf,incnt,intype,root,comm）.   
Broadcast data from root to all processes . INOUT IN incnt number of elements in input buffer(integer) IN intype datatype of input buffer elements(handle) IN root process id of root process(integer) IN comm communicator( handle)   
MPI_ GATHER(inbuf,incnt,intype,outbuf,outcnt,outtype,root,comm)   
MPI_ SCATTER(inbuf,incnt,intype,outbuf,outcnt,outtype,root,comm)   
Collective data movement functions . IN inbuf address of input buffer(choice) IN incnt number of elements sent to each(integer) IN intype datatype of input buffer elements(handle) OUT outbuf address of output buffer (choice) IN outcnt number of elements received from each(integer) IN outtype datatype of output buffer elements(handle) IN root process id of root process(integer) IN comm communicator( handle)   
MPI_REDUCE(inbuf,outbuf,count,type,op,root,comm)   
MPI_ALLREDUCE(inbuf,outbuf,count,type,op,comm)   
Collectiue reduction functions . IN inbuf address of input buffer(choice) OUT outbuf address of output buffer(choice) IN count number of elements in input buffer(integer) IN type datatype of input buffer elements(handle) IN op operation;see text for list(handle) IN root process id of root process(integer) IN comm communicator(handle)

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0006_pages_0351-0420/auto/images/e2f90925660e69455d982317d0b5fecff71ac33f7231923115e5daa41adf36db.jpg)  
图14.4MPI播送、收集和散射的几何意义

# 14.2.3通信体

通信体(Communicator)提供了MPI中独立的安全的消息传递。不同的通信库使用独立的通信体,它隔离了内部和外部通信，避免了在通信库被调用和退出时的同步,也保证了在同一通信体的通信操作互不干扰。

MPI提供的通信体函数概括在图14.5中:①MPI_COMM_DUP:它生成一个新的通信体,具有相同的进程组但新的上下文,这可确保不同目的通信不会混淆； $\textcircled{2}$ MPI_COMM_SPLIT:它生成一个新的通信体,但只是给定进程组的子集，这些进程可相互通信而不必害怕与其它并发计算相冲突;③MPI_INTERCOMM_CREATE:它构造一个进程组之间的通信体,该通信体链接两组内的进程;④MPI_COMM_FREE:它用来释放上述三个函数所生成的通信体。

MPI_COMM_DUP(comm,newcomm) Create new communicator : same group , new context . IN comm communicator(handle) OUTnewcommcommunicator(handle) MPI_ COMM_ SPLIT(comm,color,key,newcomm) Partion group into disjoint subgroups. IN comm communicator(handle)

IN color subgroup control( integer) IN key process id control(integer) OUT newcomm communicator(handle)

MPI_INTERCOMM_CREATE(comm,leader,peer,rleader,tag,inter) Create an intercommunicator.

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0006_pages_0351-0420/auto/images/f60465d6da1512ea83bd5c275b0b8b59f7d482f7e4ae1422d4423b13195a25ad.jpg)  
图14.5MPI通信体函数

图14.6示出使用MPI_COMM_SPLIT生成新的通信体方法,其中第一个通信体是个8进程组，使用myid%3着色法并调用MPI_COMM_SPLIT(comm,color,myid,newcomm)就把原通信体劈成3个不相交的进程组。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0006_pages_0351-0420/auto/images/ea8afc0dade7b2e0ce148ea9e21c70903a5af59b67cb81ea284883be7e4a96dc.jpg)  
图14.6使用MPI_COMM_SPLIT生成新通信体

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0006_pages_0351-0420/auto/images/549ad3be716f7d90f68261690c4e663503d18d205400df2a88f588d9e8d21640.jpg)  
图14.7在两进程组之间建立组间通信体

图14.7示出了在两进程组之间建立了一个组间通信体，其中顶上是原8进程组,这是一个MPI_COMM_WORLD;调用MPI_COMM_SPLIT生成两个进程组,每个包含4个进程;最后调用MPI_INTERCOMM_CREATE生成两组之间的组间通信体。

# 14.2.4导出数据类型

MPI中的导出数据类型(DerivedDatatype)允许将不连续的数据元素组合在一起,这种导出数据类型可以使用构造函数(ConstructorFunction)构造之。MPI提供的导出数据类型函数概括在图14.8中： $\textcircled { 1 } \mathbf { M P I }$ _TYPE_CONTIGU-OUS:它用来定义由一个或多个连续数据元素组成的类型; $\textcircled { 2 } \mathbf { M P I }$ _ TYPE _VECTOR:它用来定义由一个或多个成块数据元素组成的类型，这些成块的数据元素是由数组中的恒间距所分开； $\textcircled{3}$ MPI_TYPE_INDEXED:它用来定义由一个或多个基本的或先前已定义数据类型的数据块组成的类型,其中块的长度和块间位移量由数组指定； $\textcircled{4}$ MPI_TYPE_COMMIT:它用来提交数据类型,必须在使用导出数据类型之前使用; $\textcircled{5}$ MPI_TYPE_FREE:它用来释放导出数据类型,必须在使用导出数据类型之后使用。这些函数的作用,读者可参照习题14.2和14.3进一步理解之。

MPI_TYPE_CONTIGUOUS(count,oldtype,newtype)   
Construct datatype from contiguous elements . IN count number of elements(integer≥0) IN OUT newtype output datatype(handle)   
MPI_TYPE_VECTOR(count,blocklen,stride,oldtype,newtype)   
Construct datatype from blocks separated by stride. IN count number of elements(integer≥0) IN blocklen elements in a block( integer≥0) IN stride elements between start of each block(integer) IN oldtype input datatype(handle) OUT newtype output datatype(handle)   
MPI_TYPE_INDEXED(count,blocklens,indices,oldtype,newtype)   
Construct datatype with variable indices and sizes . IN count number of blocks(integer≥0) IN blocklens elements in eack block(array of integer ${ \geqslant } 0$ ） IN indices displacements for each block(array of integer) IN oldtype input datatype(handle) OUT newtype output datatype(handle)   
MPI_TYPE_COMMIT(type)   
Construct datatype so that it can be used in communication . INOUTtype datatype to be committed(handle)   
MPI_TYPE_FREE(type)   
Free a derived datatype. INOUTtype datatype to be freed(handle)

# 14.2.5点到点通信

点到点通信(Point-to-Point Communication)是MPI中比较复杂的一部分，其数据传送有阻塞和非阻塞两种机制：对于阻塞方式,它必须等到消息从本地送出之后才可以执行后续的语句，保证了缓冲区等资源的可再用性;对于非阻塞方式,它不须等到消息从本地送出就可执行后续的语句，从而允许通信和计算的重叠,但非阻塞调用的返回并不保证资源的可再用性。

如图14.9所示，阻塞和非阻塞有四种通信模式： $\textcircled{1}$ 标准模式,包括阻塞（标准)发送MPI_SEND、阻塞(标准)接收MPI_RECV、非阻塞(标准)发送MPI_ISEND 和非阻塞(标准)接收MPI_IRECV; $\textcircled{2}$ 缓冲模式，包括阻塞缓冲发送MPI_BSEND 和非阻塞缓冲发送MPI_IBSEND; $\textcircled{3}$ 同步模式,包括阻塞同步发送MPI_SSEND和非阻塞同步发送MPI_ISSEND; $\textcircled{4}$ 就绪模式，包括阻塞就绪发送MPI_RSEND和非阻塞就绪发送 MPI_IRSEND。在标准通信模式中，MPI根据当前的状况选取其它三种模式或用户定义的其它模式;缓冲模式在相匹配的接收未开始的情况下，总是将送出的消息放在缓冲区内，这样发送者可以很快地继续计算,然后由系统处理放在缓冲区中的消息，但这不仅占用内存，而且多用了一次内存拷贝;在同步模式中,MPI必须保证接收者执行到某一点,这样接收者是必须有确认信息的;在就绪模式下,系统默认与其相匹配的接收已经调用。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0006_pages_0351-0420/auto/images/3b4d4f30e4370d9314f2eefb0937340194265c98e26bd690d63f62980e785f61.jpg)  
图14.9点到点消息通信四种模式

在点到点通信中,发送和接收语句必须是匹配的。为了区分不同进程或同一进程发送来的不同消息，在这些语句中采用了通信体Comm和标志位 tag来实现成对语句的匹配。

对于阻塞的标准通信 MPI_SEND 和 MPI_RECV 函数的格式及其说明,请参见前图14.2。其中发送的含义是将包含count个datatype类型的首地址为buf的消息发送至dest进程,该消息是与标志位tag和通信体comm封装在一块的;接收的含义是从 source进程接收标志为 tag 和通信体为 comm 的消息,将该消息写入首地址为buf的缓冲区,其返回值status中包含消息的大小、标志和来源等信息。

对于非阻塞的标准通信MPI_ISEND和MPI_IRECV 函数格式及其说明如下：

MPI_ISEND(buf,count,datatype,dest,tag,comm,request)

IN buf  
IN countIN datatype  
IN dest 参照图14.2中MPI-SEND函数说明  
IN tag  
IN comm  
OUT request

MPI_IRECV(buf,count,datatype,source,tag,comm,status,request)

OUT buf  
IN count  
IN datatype  
IN dest参照图14.2中MPI-REW函数说明  
IN tag  
IN count  
OUT status  
OUT request

它们的含义与MPI_SEND和MPI_RECV 函数基本上一致,因为它们是非阻塞的通信模式,语句结束后真正的消息发送或接收并没有完成，它仅将消息挂入消息队列中,所以用request指明返回队列指针。也正是因为非阻塞通信在语句结束后,真正的消息发送或接收并没有完成,所以必须用MPI_WAIT和MPI_TEST等语句来结束非阻塞通信,它们的格式及其说明如下：

MPI_WAIT(request,status) IN request OUTstatus   
MPI_TEST(request,flag,status) IN request

OUT flag OUT status

其中,MPI_TEST用来检测非阻塞操作是否真正结束, $\mathrm { f l a g } = 1$ 表示该请求re-quest指向的非阻塞通信已完成;MPI_WAIT则一直要等到非阻塞操作真正完成之后才返回。我们可以认为阻塞通信等于非阻塞通信加上MPI_WAIT。

在点到点通信中，除了上述的函数外还须提供系统询问(Inquiry)和探测(Probe)两个函数,它们的操作概括在图14.10中： $\textcircled { 1 } \mathbf { M P I }$ _IPROBE函数检查未决(Pending)消息的存在而不必接收这些消息，从而允许我们将局部计算与处理将要到来的消息交织在一起编写程序,该调用将设置一个布尔变量flag,以指明与指定的源、tag和通信体相匹配的信息是否有效；②MPI_PROBE函数与MPI_IPROBE相关,它阻塞一直到指定的源、tag和通信体有效,然后返回并设置其status变量; $\textcircled{3}$ MPI_GET_COUNT询问函数得到刚刚收到的消息的长度，其前两个参数分别是由上一个探测或MPI_RECV调用设置的状态目标和被接收的元素的数据类型，而第三个参数是一个用以返回所接收的元素数目的整数。

MPI_ IPROBE(source,tag,comm,flag,status)

Poll for a pending message.

IN source id of source process,or MPI_ANY_SOURCE(integer)   
IN tag message tag,or MPI_ANY_TAG(integer)   
IN comm communicator(handle)   
OUT flag (logical/Boolean)   
OUT status status object(status)

MPI_PROBE(source,tag,comm,status)

Return uhen message is pending.

IN source id of source process,or MPI_ANY_SOURCE(integer)   
IN tag message tag,or MPI_ANY_TAG(integer)   
IN comm communicator(handle)   
OUT status status object(status)

MPI_GET_COUNT(status,datatype,count)

Determine size of a message.

IN status status variable from receive( status) IN datatype datatype of receive buffer elements(handle) OUT count number of data elements in message(integer)

这些函数的用法可通过如下代码段理解之：

int count, $\star$ buf , source;   
MPI_Probe(MPI_ ANY_ SOURCE,0,comm,&status);   
Source $=$ status. MPI_SOURCE;   
MPI_ Get_count(status,MPI_ INT,&count);

buf $=$ malloc(count \* size of (int));

MPI_Recv(buf,count,MPI _ INT,source,0,comm,&status);

该段代码接收来自未知源和包含未知整数数目的消息：它首先用MPI_PROBE检测消息的到来;然后决定消息源，并用MPI_GET_COUNT决定消息的大小;最后分配一个合适大小的缓冲，并接收此消息。

到现在为止，已讨论了约30个MPI函数，它们的C语言说明和Fortran语言说明,综合在本章最后的附录一和附录二中。其中allgather(全收集)和all-toall(多到多)的含义和功能的解释，作为习题14.3留给读者完成。

最后,给出一个用C语言描述的MPI计算 $\pmb { \pi }$ 的示范程序（它是Hostless程序)如下,以供读者学习理解之用。

$/ / \star$ 计算 $\pmb { \pi } \pmb { \mathbb { C } }$ 语言MPI编程代码段 $\yen 74$   
# include "mpi.h"   
# include $<$ stdio.h>   
# include<math.h>   
double f(a)   
double a; return(4.0/(1.0+a \*a));   
一

int main(argc,argv) int argc; char $\bigstar$ argv[];

int done ${ \bf \mu } = { \bf 0 }$ ， $\mathbf { n }$ ,myid,numprocs,i;   
double PI25DT ${ \ o } = 3$ .141592653589793238462643;   
double mypi,pi,h,sum,x,a;   
double startwtime,endwtime; MPI _ Init(&argc,&argv);   
MPI_Comm_ size(MPI_COMM_WORLD,&numprocs);   
MPI_Comm_rank(MPI_COMM_WORLD,&myid);

$\mathbf { \hat { n } } = \mathbf { 0 }$

while(!done) i $\mathbf { f } ( \mathbf { m } \mathbf { y } \mathrm { i d } = \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \alpha } } } } } \mathbf { = } \mathbf { 0 } )$ printf("Enter the number of intervals:(O quits)"); $\mathbf { s c a n f } ( ^ { \prime \prime } \mathfrak { H } \mathrm { d } ^ { \prime \prime } , \& \mathrm { n } )$ ； $\mathbf { i f } ( \mathbf { n } = \mathbf { \Gamma } = \mathbf { 0 } ) \mathbf { n } = 1 0 0 \mathbf { ; }$ else $\mathbf { \hat { n } = 0 }$ ； startwtime $\asymp$ MPI _ Wtime(); ！ MPI_Bcast(&n,1,MPI_INT,0,MPI_COMM_WORLD); if $\mathbf { \hat { n } } = \mathbf { \hat { \mu } } = \mathbf { 0 } .$ ） done= 1; else ！ $\begin{array} { r l } & { \mathbf { h } { = } 1 . 0 / ( \mathbf { d o u b l e } ) \mathbf { n } ; } \\ & { { \mathrm { s u m } } { = } 0 . 0 } \\ & { \mathbf { f o r } ( \mathrm { i } { = } \mathrm { m y i d } + 1 ; \mathrm { i } { < } { = } \mathrm { n } ; \mathrm { i } + \mathrm { \ n u m p r o c s } ) } \\ & { \big ~ ; } \end{array}$ $\begin{array} { l } { \mathbf { x } = \mathbf { h } \ast \left( \left( \mathbf { d o u b l e } \right) \mathrm { i } - \mathbf { 0 } . 5 \right) ; } \\ { \mathbf { s u m } + = \mathbf { f } \left( \mathbf { x } \right) ; } \end{array}$ 一 1 $\mathtt { m y p i } { = } \mathtt { h } * \mathtt { s u m }$ MPI_Reduce(&mypi,&pi,1,MPI_DOUBLE,MPI_ SUM,0, MPI_COMM_WORLD); $ \begin{array} { l } { \mathbf { i f } \left( { \mathrm { m y i d } } = = 0 \right) } \\ { \qquad { \Big \} } \end{array} }$ printf ("pi is approximately $\%$ .16f,Error is %.16f\ n", pi,fabs(pi-PI25DT)); endwtime $\asymp$ MPI _Wtime(); printf("wall clock tin $\vert \mathbf { e } = \boldsymbol { \mathfrak { g } } _ { 0 } \mathbf { f } \setminus \mathbf { n } ^ { \prime \prime }$ ,endwtime - startwtime); 8 MPI_Finalize(); eturn(0);

# \*14.3 PVM并行编程

并行虚拟机PVM(ParallelVirtualMachine)是由美国橡树岭国家实验室ORNL(Oak Ridge National Laboratory)于1989 年开发的一种支持网络并行计算的支撑软件。后来,由 Tennessee 大学、Emory 大学、CMU等大学共同研制,并得到美国能源部、国家科学基金会、Convex公司的资助，于1995年发布3.3版本。它是一个自包含的自由软件,源代码公开,从网上可以得到,因而颇受大学、研究机构的欢迎并得到广泛应用。它已成为很流行的大型科学计算的并行软件,可在同构/异构型网络环境下模拟实现一个通用的基于分布存储的并行计算机系统,提供基于消息传递的并行程序设计接口,使网上的用户能够集中地使用众多的机器资源来求解大规模计算问题。

PVM虽然没有MPI功能那么强大,但由于其出现较早,且是一个自包含系统(MPI不是自包含的),同时PVM不是一个标准(MPI是个标准),这就意味它较易修改,所以在大型计算应用领域中得到广泛使用。目前PVM和MPI正在彼此靠拢,例如,MPI-2(相对而言,以前所讨论的MPI可称为MPI-1)已加进了进程管理的功能;而PVM也有较多的群体通信功能。如果PVM和MPI最终能归并成一个单一的和标准的库,则无疑对并行处理是非常有益的。

# 14.3.1 PVM概貌

PVM组成 它由两部分组成：监控进程(Daemon Process)和PVM例程库。监控进程(称之为 pvmd)驻留在虚拟机的每一台节点机上(PVM称节点为主机),提供类似于系统调用的接口,实现进程(PVM称进程为任务)控制、通信和错误检测;PVM可调用库(称之为libpvm3.a)提供并行程序设计所需的函数和过程,主要包括进程(任务)的创建与控制、进程(任务)间的通信、系统配置以及错误处理和动态进程组管理等。

PVM控制台(PVMConsole）在PVM安装[74]之后,用户从任何主机上键入下述命令就可生成PVM控制台：

pvm host _file

成功地执行此条命令,就可在调用的主机(称为master)上启动pvmd,而在其它各主机上列出一个任选host_file并在master主机上显示如下提示：

# pvm>

它指明该主机处于PVM控制台模式。PVM控制台是一个独立的交互的PVM进程,尤如 shell,用户键人一些命令就可管理虚拟机、调用PVM应用作业、监视作业的执行等。这些命令包括加人、删除主机和列出虚拟机配置,在虚拟机上启动运行多个任务和列出运行的作业以及PVM关机杀掉所有进程。

编译和运行PVM应用程序可用C语言或Fortran语言编写，它通过PVM提供的消息传递机制实现并行计算。因为PVM定义了许多常量和数据结构,为了使用PVM库函数,在C语言中要引入语句include $<$ pvm3.h>;在Fortran语言中要引人语句include‘ $\$ 1$ PVM_ROOT/include/fpvm3.h'。编好的程序可分别使用编译器cc或f77进行编译和链接。编译完后，如PVM是同构的则可将该目标代码拷贝到所有其它机器上;如PVM是异构的，则须将源代码拷贝到各个机器上重新编译。当所有工作完成后，在master主机上启动pvmd，该 pvmd进程将按用户的配置启动网络上其它节点上的pvmd进程,这样用户的应用程序就可在PVM上运行了。

# 14.3.2 PVM消息传递库

PVM库(libpvm3.a)提供并行程序设计所需的函数和过程，主要包括以下几类：

进程(任务)的创建与控制 $\textcircled{1}$ PVM进程通过调用pvm_mytid（）来进人PVM,同时获得自己的 TID; $\textcircled{2}$ 通过调用函数 pvm_exit（)退出 PVM; $\textcircled{3}$ 函数pvm_spawn(）用于生成 pvm 的子进程;④pvm_parent（）用于返回任务的父进程的 TID。它们的格式如下：

int pvm_mytid()   
int pvm _exit()   
int pvm_parent(）   
int pvm _ spawn(char $\pmb { \mathscr { k } }$ task ,char $\yen 123,456$ argv,int flag,char $\clubsuit$ where, int ntask,int $\pmb { \mathrm { \star } }$ tids)

进程(任务)间的通信①PVM通过调用pvm_initsend()函数来创建一个新的发送缓冲区，并将其置为活动缓冲区，参数encoding是数据打包时所使用的数据编码类型，包括pvmDataDefault(若PVM是同构的，则不进行数据格式转换；否则要按外部数据表示XDR进行数据格式转换）、PvmDataRaw(不对数据进行任何编码)和PvmDataInPlace(打包时数据仍放在原处）；②发送缓冲区中可以同时包含各种不同类型、不同长度的数据，所以在数据发送之前必须对其打包，所使用的函数包括pvm_pkint（）、pvm__pkbyte（）、pvm_pklong（）、pvm_pkshort(）、pvm_pkdouble(）、pvm_pkfloat(）和 pvm_pkstr(）等;③函数pvm_send（）用来将打好包的数据发送给其它的进程;④函数pvm_recv（）用来接收数据，参数tid给出目标进程的TID,msgtag给出消息的标志;③接收时必须对所收到的数据进行与发送时打包相对应的拆包，所使用的函数包括pvm_upkint（）、pvm_upkbyte（）、pvm_upklong（）、pvm_upkshort（）、pvm_upkdouble(）、pvm_upkfloat（）和 pvm_upkstr（）等。它们的格式如下：

int pvm _initsend(int encoding) int pvm _pkint(int \* np,int nitem,int stride) int pvm_send(int tid,int msgtag) int pvm _recv(int tid,int msgtag) int pvm _mcast(int tids,int nitem,int msgtag) int pvm_upkint(int \* np,int nitem,int stride)

动态进程(任务)组PVM支持进程(任务)组(Group)的概念。一个任务组中可包含多个任务;一个任务也可同时属于多个任务组。任务组可动态生成，任何任务可在任何时刻加入或离开一个任务组。任务组的创建有助于对组中任务进行广播、设置路障以及施行全局运算。任务组的引入，使得一个PVM任务既可以用 tid来标识,也可以用(组名，成员号)二元组来标识。任务组操作中最基本的函数是加人和离开任务组：

int pvm _joingroup(char \* group) int pvm _ lvgroup(char $\star$ group)

下面的函数可以从成员号inum获得tid,或从tid获得成员号以及获得一个任务组中的成员数：

int pvm_gettid(char \* group,int inum) int pvm_getinst(char \* group;int tid) int pvm _gsize(char \* group)

与任务组相关的其它操作,包括同步 pvm_barier（）:调用任务等待组中共有count个任务调用了pvm_barrier(）;广播pvm_bcast（）:对任务组中的所有成员进行播送;归约 pvm_reduce（):类似于 MPI中的归约,用于在指定的任务组的全体成员进行全局性运算,如在同组的所有任务中求最大/最小、求和等。这些函数的格式如下：

int pvm_barrier(char \* group,int count)   
int pvm _bcast(char $\clubsuit$ group,int msgtag)   
int pvm_reduce (void( \* func)(),void $\ast$ data,int nitem,int datatype, int msgtag,char $\clubsuit$ group,int root)

动态配置PVM可由用户调用PVM库函数进行动态配置。函数pvm_addhosts(）和pvm_delhosts(）用来加人和删除一个或多个主机：

int pvm_addhosts(char $^ { \star }$ $\clubsuit$ hosts,int nhost,int $^ { \ast }$ infos) int pvm_delhosts(char $\pmb { \mathscr { k } }$ $\pmb { \mathscr { k } }$ hosts ,int nhost ,int $\pmb { \mathscr { k } }$ infos) 它们将hosts指定的机器名加人到当前虚拟机中，或从当前虚拟机中删去这些 机器。

最后,给出一个用C语言描述的PVM计算 $\pmb { \pi }$ 的示范程序（它是一个 SPMD程序)如下，以供读者学习理解之用。

$/ / \ast$ 计算 $\pmb { \pi } \pmb { \mathbb { C } }$ 语言PVM编程代码段 $\yen 74$   
# define n $1 6 ~ / \ast$ number of tasks $\pmb { \mathscr { k } }$ /   
# include $\prime \prime \mathrm { p v m } 3 . \mathrm { h } ^ { \prime \prime }$   
main(int argc,char $\# \quad \#$ argv) int mytid,tids[n],me,i,N,rc,parent; double mypi, $\mathbf { h } , \mathbf { s u m } = \mathbf { 0 } . \mathbf { 0 } , \mathbf { x } ;$ $\mathtt { m e } = \mathtt { p v m }$ _joingroup("pi"); parent $=$ pvm _ parent(); if $\mathbf { \dot { m } e } = 0 .$ pvm_ spawn("pi",(char \* \* )0,0," ",n-1,tids); printf("Enter the number of regions:"); scanf("%d",&N); pvm_initsend(PvmDataRaw); pvm_pkint(&N,1,1); pvm _mcast(tids,n-1,5); else pvm __recv(parent,5); pvm_upkint(&N,1,1); $\mathrm { p v m \_ b a r r i e r { ( } ^ { \prime \prime } P I ^ { \prime \prime } , n ) } ; / * \mathrm { o p t i o n a l } * /$ ${ \bf h } = 1 . 0$ /(double)N; ${ \bf f o r ( i = m e + 1 ; i < = N ; i + \omega = n ) } \left\{ \right.$ $\mathbf { x } = \mathbf { h } \nmid ( ( \mathbf { d o u b l e } ) \mathbf { i } - \mathbf { 0 } . 5 ) ;$ $\mathbf { s u m } + = 4 . 0 / ( 1 . 0 + \mathbf { x } * \mathbf { x } ) ;$ $\mathrm { { m y p i } = h \ast \ s u m _ { \mathrm { { i } } } }$ pvm_reduce(PvmSum,&mypi,1,PVM_DOUBLE,6,"1 if( $\mathbf { m e } = { \mathbf { \eta } } = { \mathbf { 0 } }$ )printf("pi is approximately %.16f\n",mypi pvm_lvgroup("PI"); pvm_exit();

# 14.4 基于数据并行的并行编程

# 14.4.1数据并行模型的特点

关于数据并行模型已在第十三章的第13.2.2节进行了讨论，读者不妨先复习一下那里所讲的内容。

对于有些问题,常常要对大量的数据进行相同的、彼此独立的操作,这些量大且互不影响的操作是可以并行进行的,此即数据并行名称的由来。例如,矩阵相乘就呈现出数据并行的特点：当两个 ${ \pmb n } \times { \pmb n }$ 的矩阵 $\pmb { A }$ 和 $B$ 相乘而得到矩阵C时,其乘积元素 $C _ { i j }$ 就是 $\pmb { A }$ 的第 $i$ 行与 $B$ 的第 $j$ 列执行点积运算而求得。所以求每个 $C _ { i j }$ 元素可以并行地对不同的数据元素 $a _ { i k }$ 与 $b _ { k j }$ 执行相同的点积运算。如果我们用某种数据并行语言(下一节将要讨论)来编程实现这种计算,就可得到一个数据并行程序。一个数据并行程序包含一个单一的指令序列,每条指令作用于不同的数据项且以锁步方式同步执行,所以这种程序很自然地适合于在SIMD 机器上实现。当然这样的数据并行程序也可在MIMD机器上实现，只不过是在每条指令之后施行全局同步导致执行效率很低。实用的办法是在MIMD机器上使用 SPMD编程模式,在此模式下并行粒度要大一些。事实上，SPMD是 SIMD的特例,SPMD是一种中粒度的并行,是语句块和循环一级的同步,而不是像SIMD那样是指令级的同步。在SPMD模式下,每个处理器异步地执行相同的程序,只有当处理器间需要交换数据时才施行同步。由于减少了同步,SPMD模式在许多情况下比 SIMD模式更有效。在大规模并行处理MPP系统中，使用 SPMD模式进行编程时，用户程序把整个分布存储系统视为一个统一的全局空间,由编译实现程序的逻辑地址到物理地址的映射。

总之,数据并行程序是一个单一控制线程的、并行操作于不同数据项的、语句循环级同步的、单一地址空间的、通信可由变量指派而隐含地完成的一种并行程序。

# 14.4.2数据并行编程的基本问题

进行数据并行程序设计时常常需要考虑以下几个基本问题：

数据分布(DataDistribution）分布就是要建立数据集合到处理器集合之间的映射关系，数据分布就是把数据按一定规则分配到各个处理器的存储单元中去。数据分布规则实际上也就是数据地址计算规则。分布的目的是为了提高程序执行的并行性，增强数据局部性，减少通信，从而提高程序的执行效率。数据并行程序设计语言及其编译系统所扩充的最主要功能之一就是支持数据分布。

数据分布规则是将共享分布的数组按维分配到各个处理器上。常用分布方法有按块分布、循环分布、对准分布和静态/动态分布等。这些方法在下节介绍HPF时会看到。

任务分配(TaskAllocation）任务分配就是把计算任务分配给各个处理器上,使得程序可以在并行系统上高效执行。任务分配的原则是尽可能将计算和其所需数据对准，也就是数据分配到哪个处理器，就将用到这些数据的计算操作也分配到哪个处理器，此即所谓的属主-计算(Owner-Computes)的原则。在进行数据并行编程时，一般是先定义数据分布，再将并行循环中的迭代计算按数据分布模式分配到各个处理器上去执行，这样就实现了计算和数据的对准。

同步通信对于 SPMD模式数据并行编程,在共享变量模型下,同步机制--般包含临界区、锁、路障和事件等;对于 SPMD模式数据并行编程,编译系统给通信提供了较强的支持：对于点到点通信,程序员可以写成赋值语句，对于全局通信，程序员可以调用系统库程序。

处理器拓扑结构在数据并行语言中，处理器的拓扑结构是逐个数组确定的,是受数据分布影响的。处理器拓扑的形成就是把参加并行执行的处理器分配给分布数组的各维,即决定每维分几个处理器。处理器拓扑结构可由编译系统确定,所依据的规则是数据分布大致均匀、地址计算尽量简单和通信尽可能少。

# 14.5HPF并行编程

高性能Fortran(High Performance Fortran)简称 HPF,是一个支持数据并行的并行语言标准。它提供了一个全局名字空间和单线程控制，用户可以用分布(Distribution)和对准(Alignment)说明定义所希望的数据布局,用显式的并行结构表达并行机制。HPF中由于没有显式的任务划分和通信语句,代码的定义是在高层进行的,因此具有良好的移植性,通过具体机器上的编译器可以生成各种系统平台上的高效代码。

HPF 的产生可以追溯到DEC的 Lovman 和Rice大学的Kennedy在 Super-computing'91大会上发起的“Birdsof afeather"小组会。在这个会上主要讨论了关于分布存储机器上的高层编程方法。DEC首先抛砖引玉，提供了他们的HPF;紧接着于1992年1月在Rice大学召开了第一次HPF会议,会议决定组织HPF论坛;1992年3月论坛正式成立;1993年5月发布了HPF1.0版;1994年11月发布了HPF1.1版,到1997年1月发布了HPF2.0版。所有文档可从网上站点 http://www.crpc.rice.edu/HPF/home.html获得。

# 14.5.1 HPF的语言特点

以下的讨论立足于HPF2.0版本。HPF2.0语言包括三个部分： $\textcircled{1}$ 语言的基本部分,包括任何HPF编译器必须支持的特性; $\textcircled{2}$ 已经核准的扩展部分，包括满足某些特殊需要的高级结构(早期的编译器可能不支持这一部分); $\textcircled{3}$ 已被认可的外部接口,这是HPF论坛批准的一组接口。

当前的HPF2.0 版是基本 Fortran95,并吸取了HPF1.1版的一些特性；而HPF1.1版是基于Fortran90的,Fortran 90的数组语句为数据并行提供了一种自然的机制,HPF1.1扩展了Fortran90的这些特性,提供了实现数据并行操作的FORALL结构和几个内部与外部库。

HPF2.0的一些基本特性是： $\textcircled{1}$ 数据并行制导（Data Parallel·Directives）：HPF2.0提供的数据并行机制扩展了Fortran 95的数组语句和FORALL结构，其中 INDEPENDENT用于声明无依赖循环迭代,可以并行执行；REDUCTION用于标识被不同迭代修改的变量;②数据映射制导(Data MappingDirectives）：HPF提供了一组扩展的说明,用于指定数据的分布和对准，可将数据显式地定义到抽象的处理器上，所提供的ALIGN和DISTRIBUTION说明，能够让用户告诉编译器如何在各处理器间分配数据，以使通信开销最小和负载划分最均匀；$\textcircled{3}$ 新内部函数和库函数(New Intrinsic and Library Functions):HPF 提供了一组新的内部函数和库,包括请求底层硬件的系统函数、请求数据结构分布的映射请求函数以及一些计算的内部函数;HPF定义了一组新的库,为并行操作定义了一个标准的接口，包括归约（Reduction）、组合-散射（Combining-Scatter）、前缀(Prefix)及后缀(Suffix)分类(Sorting)和位操作(Bit-Manipulation）函数等; $\textcircled{4}$ 外部过程(Extrinsic Procedures):除了数据并行编程外,HPF为了匹配其它编程方法,HPF定义了一个显式接口，允许用不同语言(如C)或不同方法(如显式消息传递)所编制的程序能够被一个HPF程序调用。

# 14.5.2 HPF的数据并行机制

FORALL结构HPF 中新增的 FORALL 语句和 FORALL 结构类似于Fortran 90的数0组赋值语句，只是比Fortran90的数组赋值语句更灵活,并且FORALL语句能以指定的逻辑表达式对赋值语句进行限定。例如下述FORALL 语句：

$$
\mathrm { L } ( i = 2 \colon 5 , \mathrm { X } ( i ) > 0 ) \quad \mathrm { X } ( i ) = \mathrm { X } ( i - 1 ) + \mathrm { X } ( i + 1 )
$$

其中,i是索引变量；i=2:5称为 for-三元组,等价于i=2:5:1,表示i取值上界为5、下界为2而步长缺省时为1。在上述FORALL语句中,假定初始X={1,-1,2，-2,3,-3},在i的有效值范围内,满足X(i)>0的索引i的活动集合为

{3,5,同时计算如下赋值语句：

$$
\mathrm { X } ( 3 ) = \mathrm { X } ( 2 ) + \mathrm { X } ( 4 ) = - 3
$$

$$
{ \bf X } ( 5 ) = { \bf X } ( 4 ) + { \bf X } ( 6 ) = - 5
$$

FORALL语句结束后， $\dot { \mathbf { X } } = \left\{ 1 , - 1 , - 3 , - 2 , - 5 , - 3 \right\} ,$ 在 FORALL语句中,可能有不止一个for-三元组,则用的是组合索引,例如：

$\mathrm { F O R A L L } ( \textit { i } = 1 : 2 , \textit { j } = 1 : 3 , \mathrm { Y } ( \textit { i } , \boldsymbol { j } ) > 0 ) \quad \mathrm { Z } ( \textit { i } , \boldsymbol { j } ) = 1 / \mathrm { Y } ( \textit { i } , \boldsymbol { j } )$ 该语句等价于Fortran 90如下语句：

wher $\mathsf { \Lambda } _ { \mathsf { P } } ( \Upsilon ( 1 : 2 , 1 : 3 ) > 0 ) \cdot \mathsf { Z } ( 1 : 2 , 1 : 3 ) = 1 \Upsilon ( 1 : 2 , 1 : 3 )$ 则组合索引的有效值集合为{(1,1),(1,2),(1,3),(2,1),(2,2),(2,3)|,而组合索引的活动值取上述集合中使 $\Upsilon ( i , j ) > 0$ 的子集。

有时用户希望在一个FORALL 语句中包含几个赋值,这可使用 FORALL结构来实现。FORALL结构是对 FORALL语句的进一步扩充,即在FORALL和ENDFORALL之间可以写多条语句，但限制FORALL结构中只能使用赋值语句、FORALL语句、FORALL结构、WHERE语句以及WHILE结构。例如：

$$
\begin{array} { l } { \mathsf { A } ( \mathrm { I } ) = \mathsf { A } ( \mathrm { I } - \mathrm { 1 } ) + \mathsf { A } ( \mathrm { I } + \mathrm { 1 } ) } \\ { \mathsf { B } ( \mathrm { I } ) = \mathsf { A } ( \mathrm { I } ) } \end{array}
$$

上述代码，首先对从2到9的各个I求 $\mathbf { A } { \left( \ \mathrm { I } - 1 \right) } + \mathbf { A } { \left( \ \mathrm { I } + 1 \right) }$ 之值,并将结果送人A(2)到A(9)中;然后将求得的A(2)到A(9)之值送人B(2)到B(9)中。

！HPF $\$ 1$ PROCESSORS proc_name(dim1,,dimN)   
Declare and abstract processor array. proc_ name name of abstract processor array dim1,.,dimN size and shape of array

！ HPF $\$ 1$ ALIGN array WITH target

Align array with a target array.

array array to be aligned target array to be aligned to ！ HPF \$ DISTRIBUTE list_of_arrays[ONTO proc_ name] Distribute array(s)onto processor array.

list_ of _arrays arrays to be distributed proc_ name abstract processor array

数据分布 数据分布指的是将数据(主要是数组)分布到处理器上。HPF引入了如图14.11所示的一些指导数据分布的伪指令，指示编译器如何最佳地分布数据于计算节点上。图14.12是HPF数据分布模型。数据映射(分布)要达到的目的是：使处理器间的通信开销最小以及使负载在处理器上分布均匀。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0006_pages_0351-0420/auto/images/96824a8f0005904c1a51fb10e06efbb1bae6d8d582656fd27f9c1bc3427bae85.jpg)  
图14.12 HPF数据分布模型

$\textcircled{1}$ PROCESSORS:伪指令 PROCESSORS说明抽象的处理器排列结构。例如：

它通知编译器,应用程序希望使用4个处理器排成线性阵列的抽象结构。同样，

！HPF $\$ 9$ PROCESSORS P(4,5)！HPF $\$ 1$ PROCESSORS Q(4,5,6)

分别指明20个处理器排成 $4 \times 5$ 的二维网孔和120个处理器排成 $4 \times 5 \times 6$ 的三维网孔。

$\textcircled{2}$ ALIGN:伪指令ALIGN用于描述数组间元素的对准。例如：

！HPF $\$ 9$ ALIGN A(I) WITH B(I)

表示把A的第Ⅰ个元素与B的第I个元素分配到同一个处理器上。同样，！HPF $\$ 8$ ALIGN A(I) WITH $\mathbb { B } ( \mathbb { I } + 2 )$

表示把A的第I个元素与B的第I+2个元素分配到同一个处理器上。图14.13示出了HPF对准语句的6个例子。

$\textcircled{3}$ DISTRIBUTE:伪指令DISTRIBUTE用于指明数组如何在计算机存储器间进行划分。数组每一维可按下述方式之一进行分布：

无分布BLOCK(n) 块状分布CYCLIC(n) 循环分布对于程序员可使用下述两种DISTRIBUTE伪指令：

！HPF $\$ 1$ DISTRIBUTE A(BLOCK) ONTO N！HPF $\$ 9$ DISTRIBUTE C(CYCLIC) ONTO N

图14.14示出了一个8×8的二维数组,使用分块和循环方式分布到4个处理器上的情况。图中带阴影的数据分布给第一个处理器。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0006_pages_0351-0420/auto/images/9b1b2c587c95b08d5dec912fcf6aaecf37eae222475344ecb80e6cf8900a4bf4.jpg)  
图14.13HPF对准方式示例

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0006_pages_0351-0420/auto/images/1928f8bfd172c82886952bdaf03a8a16028c07123b46f21adb22b2f0ff30979c.jpg)  
图14.14 $\mathbf { 8 \times 8 }$ 的二维数组分布给4个处理器

下面给出 HPF 数据映射的一个综合例子。试考虑如下HPF代码段：integer A(100),B(100),C(101),i

！ HPF \$ ALIGN A(i) WITH B(i-1)  
！ HPF \$ PROCESSOR N(4)  
！ HPF \$ DISTRIBUTE A(BLOCK) ONTO N  
！HPF \$ DISTRIBUTE C(CYCLIC) ONTO NFORALL ( $i = 2 { : } 1 0 0 \rangle$ ）$\mathbf { A } ( \mathbf { \zeta } _ { i } ) = \mathbf { A } ( \mathbf { \zeta } _ { i } ) + \mathbf { B } ( \mathbf { \zeta } _ { i } - 1 )$ $\mathbf { C } ( \mathsf { \Delta } i ) = \mathbf { C } ( \mathsf { \Delta } i - 1 ) + \mathbf { C } ( \mathsf { \Delta } i ) + \mathbf { C } ( \mathsf { \Delta } i + 1 )$ ENDFORALL

图14.15描述了上述代码段实现的数据映射过程。HPF 中数据映射的实现分为两个阶段：逻辑映射和物理映射。前者由用户通过编译制导(CompilerDirectives)定义,将数据映射到抽象处理器节点上;后者由系统将上述抽象处理器节点映射到实际计算机物理节点上,这对用户是透明的。其中逻辑映射分为对准和分布两步。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0006_pages_0351-0420/auto/images/264a362f98477fcd1c979061c0e0eaad4e87481f7caad17755ace72b5e0214da.jpg)  
图14.15HPF数据映射过程

外部过程HPF中增加了具有如下功能的库程序：①系统查询功能：它可给出有关处理器的信息,包括可用处理器数的NUMBER_OF_PROCESSOR库程序以及处理器构成信息的PROCESSOR_SHAPE库程序； $\textcircled{2}$ 变换查询功能：它可给出有关数据的分布、定位方面的信息,包括数据定位信息的HPF_ALIGNMENT_库程序,template信息的HPF_TEMPLATE库程序和数据分布状态信息的HPF_DISTRIBUTION库程序； $\textcircled{3}$ 计算库功能：它提供求数组中的最大值和前缀运算等。这些运算使用具有网络特性的库函数比起使用以For-tran描述的循环效果更好。在HPF中提供的库函数有归约函数、前缀及后缀函数、组合-散射函数、分类函数和位变换函数等。

# 14.5.3 HPF使用中的若干问题

语言的限制问题在Fortran中,数组元素按一定的顺序被分配在一维连续的存储区内,并可通过等价语句EQUIVALENCE和子程序调用中的虚实变量结合发生连接。因此会发生部分一维数组被二维数组覆盖以及某变量的一部分和另一变量的一部分拥有同一存储区的情况。在HPF程序中也会发生类似情况(参见习题14.6)。另外,关于子程序调用时的虚实变量结合也受到限制。例如在Fortran90中，能作到用数组元素的实变量代换虚变量，用二维数组代换一维数组。但在HPF中这样作就需要使用 SEQUENCE伪指令写出程序,例如：

REAL A(100,100),B(200)  
！ HPF \$ SEQUENCE A,BCALL S(A,B(51))ENDSUBROUTINE S(X,Y)REAL X(10000),Y(100)  
！ HPF \$ SEQUENCE X,Y：END

并行性问题因为HPF是单线程的，所以一个数据并行的程序逻辑上只有一个进程,尽管多个节点能够对不同的数据子域执行相同的程序。绝大部分并行性问题由系统管理,用户不用担心进程的生成、结束和有多少进程正在运行程序。因为HPF是语句级的数据并行,它允许在同一时间不同的节点执行不同的指令，因此可同时支持SIMD和 SPMD并行计算,但不支持MPMD计算。程序中的并行度是随所用的不同的数组指派或执行不同的FORALL语句而动态变化。

相互作用问题因为是松散同步，所以在数据并行编程中绝大多数相互作用问题都躲开了，除了归约操作外，Fortran90或HPF中不存在相互作用问题。

在Fortran 90中提供了9种内部函数以支持归约,但不支持前缀、递降、分类,它也不支持用户定义的归约操作。HPF通过一组库例程扩展了Fortran 90的能力，包括辅助的归约函数、scan函数和分类等。

数据并行程序只有一种相互作用模式，即语句级的松散同步。一条语句的所有操作均必须在下一语句的任一操作开始之前完成。通信经由数组赋值而呈隐式状。HPF提供一组数组分布伪指令，使用开拓数据局部性而可最小化通信开销。HPF除了提供 PROCESSORS、ALIGN和DISTRIBUTE 伪指令外,还提供REALIGN 和REDISTRIBUTE语句以调节通信模式的变化。

语义问题由于单线程和松散同步,所以数据并行程序具有清晰的语义,它不可能出现死锁或活锁,仅有的可能是由于无限循环而会造成非确定性。For-tran 90 和HPF在结构性、合成性和正确性方面类似于串行的Fortran90程序,并未因引人并行性而增加复杂性。

数据并行程序只要满足单赋值规则它就是确定的。

可编程性问题 因为Fortran和HPF均是高级语言标准,所以具有好的可移植性。又因为大多数并行性、相互作用和语义问题均由系统负责，所以For-tran 90 和HPF易于使用。但现在的Fortran90和HPF语言说明对通用性和效率尚有严格的限制,所以不少人仍在使用别的编程方法。Fortran90和HPF不支持开拓控制并行,它们也不适合于支持异步迭代、流水线计算等算法范例,数据库方面的应用也比较困难。HPF 的数据映射似乎也仅支持正规通信模式的数组,它是否有效地支持一般数据结构和非正规通信模式的并行算法，还值得怀疑。

最后,给出一个高斯消去法的 HPF 程序如下,以供读者学习理解之用(其Fortran 90程序见习题14.7)。

$/ / \ast$ 高斯消去法的HPF编程代码段\*//  
parameter $\mathtt { n } = 3 2$   
real $\mathbf { A ( n , n + 1 ) , x ( n ) }$   
integer $\vdots$ ,pivot_location(1)  
！HPF $\$ 9$ PROCESSOR Nodes(4)  
！HPF $\$ 9$ ALIGN $\mathbf { x } ( \mathrm { i } )$ WITH A(i,j)  
！HPF $\$ 1$ DISTRIBUTE A(BLOCK, $\star$ ） ONTO Nodes  
d $\mathbf { \delta } _ { \mathbf { \{ j } }  = \mathbf { 1 } , \mathbf { n } - \mathbf { 1 }$ ！pivotingpivot_ $\scriptstyle \mathrm { l o c a t i o n } = \mathbf { M A X L O C } ( \mathbf { A B S } ( \mathbf { A } ( \mathbf { i } \cdot \mathbf { n } , \mathbf { i } ) ) )$ swap $\mathfrak { o } \big ( \mathbf { A } ( \mathrm { i } , \mathrm { i } { : } \mathrm { n } + 1 ) , \mathbf { A } ( \mathrm { i } - 1 + \mathrm { p i v o t \_ l o c a t i o n } ( 1 ) , \mathrm { i } { : } \mathrm { n } + 1 ) \big )$ ！triangularization$\mathbf { A } ( \mathrm { i } , \mathrm { i } ; \mathbf { n } + 1 ) = \mathbf { A } ( \mathrm { i } , \mathrm { i } ; \mathbf { n } + 1 ) / \mathbf { A } ( \mathrm { i } , \mathrm { i } )$ FORALL $( { \bf j } = { \bf i } + 1 \cdot { \bf n } , { \bf k } = { \bf i } + 1 \cdot { \bf n } + 1 ) { \bf A } ( { \bf j } , { \bf k } ) = { \bf A } ( { \bf j } , { \bf k } ) - { \bf A } ( { \bf j } , { \bf i } ) * { \bf A } ( { \bf i } , { \bf k } )$   
end do  
！back substitution$\begin{array} { r l } & { \mathfrak { p i } = \mathfrak { n } , \mathbf { 1 } , - 1 } \\ & { \mathbf { x } ( \mathrm { i } ) = \mathrm { A } ( \mathrm { i } , \mathfrak { n } + \mathbf { 1 } ) } \\ & { \mathrm { A } ( 1 { : } \mathrm { i } - 1 , \mathfrak { n } + 1 ) = \mathrm { A } ( 1 { : } \mathrm { i } - 1 , \mathfrak { n } + 1 ) - \mathrm { A } ( 1 { : } \mathrm { i } - 1 , \mathrm { i } ) * \mathbf { x } ( \mathrm { i } ) } \end{array}$

end do

# 14.6 小结和导读

小结分布存储系统包括 SIMD-DM、MIMD-DM和COW-DM等并行计算机系统。在SIMD-DM并行系统上,使用数据并行程序设计模型,以SPMD编程方式编写并行程序,常用的编程语言有Fortran90 和HPF等;在MIMD-DM和COW-DM并行系统上,使用消息传递程序设计模型,以 SPMD和MPMD编程方式编写并行程序,常用的语言标准有MPI和PVM等。

数据并行语言标准除了本章所介绍的HPF和Fortran90外，目前还有For-tran 95、Fortran 2001 和 Fortran D、Vienna Fortran。其中 Fortran 95 和 Fortran2001是Fortran 90 的推广;Fortran D和 Vienna Fortran是MPI的推广。Fortran95发布于1997年,主要新特性是FORALL 语言和 FORALL结构,PURE 和ELEMENTAL过程以及结构和指针缺省初始化。Fortran 2001预计2001年发布,正被考虑中的新特性包括例外处理,与C语言的连接性，增强导出数据类型,附加支持高性能数值计算,新的I/O性质,面向对象等。Fortran D(后称为Fortran 90D)和ViennaFortran提供更通用的数据映射函数,包括支持动态和非正规数据分布等。

消息传递标准除了本章所介绍的1994 年发布的 MPI(称之为MPI-1外),1997年MPI论坛又发布了修订标准MPI-2。MPI-2相对于 MPI-1增加了很多功能,主要包括动态进程(MPI-1并行程序中的进程是静态的),点到点单边通信(MPI-1点到点通信是双边的),可扩放I/O支持(MPI-1完全不考虑I/O问题),Fortran 90 和 $\mathrm { C } + +$ 语言描述(MPI-1的语言描述是 Fortran 77和 C),增加实时处理,推广MPI-1的外部接口和环境工具,允许非阻塞群体通信、通信体间的群体通信、通信体间的拓扑结构(MPI-1只支持阻塞和通信体内的群体通信)等。

导读有关MPI的最初描述见[128],一本好的 PVM人门见[74]。关于网络并行计算与分布式编程环境，读者可参阅[197]。数据并行方法见[92]，HPF描述在[111]、[125],推广的HPF见[45],Fortran 90描述在[1],Fortran95 描述在[2],FortranD描述见[70],Vienna Fortran描述在[188]。关于并行程序设计的一本简明教材是[195]。关于消息传递程序设计和数据并行程序设计,读者可阅读[103]书的第13章和第14章。

# 习 题

14.1试考虑下述代码段中通信体的使用：

process 0:  
MPI_Send(msgl,countl,MPI_INT,tagl,comml);parallel_fft(…);  
process 1:  
MPI _Recv(msgl,countl,MPI _ INT,tagl,comml) ;parallel_fft(…);  
(1)试分析上述代码段的计算功能。  
(2)如果在parallel_fft $( \cdots )$ 中又包含了另一个发送程序：if(my-rank ${ \bf \Psi } = { \bf 0 }$ )MPI_Send(msg2,count1,MPI_INT,1,tag2,comm2);如果没有通信体则会发生什么情况？

14.2填上空白处,使下述两代码段完全等效：

(1)Call MPI_TYPE_CONTIGUOUS(10,MPI_REAL,tenrealtype,ier) Call MPI_TYPE_COMMIT(tenrealtype,ierr) Call MPI_ SEND(data,1,tenrealtype,dest,tag,MPI _ COMM_WORLD,ierr) Call MPI _TYPE_FREE(tenrealtype,ierr)   
(2)Call MPI_SEND(data., ， ,dest,tag, ,ierr)

14.3填上空白处,使下述两代码段完全等效：

(1)float data[1024];MPI _Datatype floattype;MPI_Type_vector(10,1,32,MPI_FLOAT,&floattype);MPI_Type_commit(& floattype);MPI _ Send(data,1,floattype,dest,tag,MPI_COMM_WORLD);MPI_Type_free(&floattype);  
(2)float data[1024],buff[10];for(_ ； _;i++）buff[i] $\mathbf { \Phi } = \mathbf { \Phi }$ data[. ：MPI__Send(buff, _,MPI_FLOAT, ）；

14.4在MPI群体通信中,还有allgather和altoall两个函数,它们可图示于图14.16中,试

解释两者的功能及意义。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0006_pages_0351-0420/auto/images/ad801e61592d0b59bdc58e664218573cb0112b9418db4591a29c2cdbaecf55cf.jpg)  
图14.16allgather和 alltoall群体操作

14.5下面是PVM环境下的 hello程序,它是一个 host/node程序,试分析其工作过程。

//\*PVM主机/节点编程的hello代码段 $\bigstar$ // $\big / \ast \mathrm { \bf { h o s t } }$ 程序 hello. $\pmb { c } \star$ / # include <stdio.h> # include “pvm3.h" main() int cc,tid; char buf[100]; $\begin{array} { r l } & { \mathrm { p r i n t f } ( \mathrm { \ ' { ' } ^ { \prime } i } ^ { \prime } \mathrm { \ ` m ~ t } \% \times \mathrm { \ ` ~ n ' ~ } , \mathrm { p v m \_ m y t i d ( \cdot ) } ) ; } \\ & { \mathrm { c c = \mathrm { p v m \_ \mathrm { p n } - \mathrm { s p a w n } } ( \mathrm { \ ' { ' h e l l o } _ { \mathrm { - } } \ o t h e r \ " , ( \mathrm { c h a r } \times \mathrm {  ~ \times ~ } ) 0 , 0 , \mathrm { \cdots ~ } ^ { \prime \prime } , \mathrm { \bf { 1 } } , \& \mathrm { \ " { \mathrm { t i d } } } ) ; } } } \\ & { \mathrm { i f } ( \mathrm { c c = \bf { 1 } } ) \smash { \downarrow } } \\ & { \qquad \mathrm { c c = \mathrm { p v m \_ \mathrm { r e c v } ( \mathrm { - } 1 , \mathrm { - } 1 ) } ; } } \\ & { \qquad \mathrm { p v m \_ { \mathrm { b u f i n f o } } ( \mathrm { c c , \mathrm { ( i n t \ast ) } 0 , ( i n t \ast \mathrm { \Lambda ) } 0 , \& \mathrm { \vec { \mathrm { ~ } } t i d } ) ; } } } \\ & { \mathrm { p v m \_ \mathrm { \nu \mathrm { \nu \mathrm { \to } \nu t r i c } } ( \mathrm { b u f } ) ; } } \\ & { \mathrm { p r i n t f } ( \mathrm { \ ' f r o m \_ t y \mathrm { \nu } , \mathrm { \Lambda } } ; \mathrm { \Lambda } _ { \mathrm { \Lambda } } ^ { \prime } ) { _ \mathrm { \mathrm { 6 l } } } , \mathrm { \ n i d } , \mathrm {  { b u f } } ) ; } \end{array}$ else

printf("can't start hello _other\n"); pvm_exit(); /\* node 程序 heuo__ other.c \*/ # include "pvm3.h" # include"string.h" main() ！ int ptid; char buf[100]; ptid $\lneq$ pvm _ parent(); strcpy(buf,"heul,world from"); gethostname(buf $^ +$ strlen(buf),64); pvm _initsend(PvmDataDefault); pvm_pkstr(buf); pvm__send(ptid,1); pvm_exit(）; exit(0); ！

14.6试分析下述HPF代码段中数组元素的覆盖情况;如何用EQUIVALENCE语句使其变成正确的HPF程序？

REAL A(100),B(100) EQUIVALENCE(A(51),B(1))   
$! \ H P F \ S$ PROCESSORS P(4)   
$! \ H P F \ S$ DISTRIBUTE A(Block) ONTOP

14.7高斯消去法的Fortran90程序如下：试分析其计算过程并与高斯消去法的 HPF程序(课文中）加以比较。

$/ \varkappa$ 高斯消去法的Fortran90编程代码段 $\pmb { \mathscr { k } }$ /   
real $\mathbf { A ( n , n + 1 ) , x ( n ) }$   
integer i,pivot_loctation(1)   
do $\mathbf { \omega } _ { \mathbf { i } } = \mathbf { 1 } , \mathbf { n } - \mathbf { 1 }$ ！pivoting pivot_ location $\lneq$ MAXLOC(ABS(A(i: n,i))) swaj $\mathsf { p } \big ( \mathsf { A } \big ( \mathrm { i } , \mathrm { i } ; \mathsf { n } + 1 \big ) , \mathsf { A } \big ( \mathrm { i } - 1 + \mathsf { p i v o t \_ l o c a t i o n } \big ( 1 \big ) , \mathrm { i } ; \mathsf { n } + 1 \big ) \big )$ ！ triangularization $\begin{array} { r l } & { \mathbf { A } ( \mathrm { i } , \mathrm { i } ; \mathbf { n } + 1 ) = \mathbf { A } ( \mathrm { i } , \mathrm { i } ; \mathbf { n } + 1 ) / \mathbf { A } ( \mathrm { i } , \mathrm { i } ) } \\ & { \mathbf { A } ( \mathrm { i } + 1 ; \mathbf { n } , \mathrm { i } + 1 ; \mathbf { n } + 1 ) = \mathbf { A } ( \mathrm { i } + 1 ; \mathbf { n } , \mathrm { i } + 1 ; \mathbf { n } + 1 ) - \& } \end{array}$

SPREAD(A(i,i + 1:n + 1),1,n-i) \* SPREAD(A(i+ 1:n,i),2,n-i+1)

# end do

！back substitution ${ \begin{array} { r l } & { = \mathbf { n } , 1 , - 1 } \\ & { ~ \mathbf { x } ( \mathrm { i } ) = \mathbf { A } ( \mathrm { i } , \mathbf { n } + 1 ) } \\ & { ~ \mathbf { A } ( 1 { : } \mathrm { i } - 1 , \mathrm { n } + 1 ) = \mathbf { A } ( 1 { : } \mathrm { i } - 1 , \mathrm { n } + 1 ) - \mathbf { A } ( 1 { : } \mathrm { i } - 1 , \mathrm { i } ) * \mathbf { x } ( \mathrm { i } ) } \end{array} }$   
end do

14.8雅可比松弛法 Fortran90程序如下：参照它试写出雅可比松弛法的HPF程序;并将两者加以比较。

$^ { \prime \prime * }$ 雅可比松弛法的Fortran90编程代码段 $^ { \star }$ //   
parameter ${ \bf n } = { \bf 1 0 2 4 }$   
real $\mathrm { A ( n , n ) , x ( n ) , b ( n ) , e r r o r , T e m p ( n ) , D i a g A ( n ) }$   
integer i   
error $=$ SomeLargeValue   
初始化 $\mathbf { A } , \mathbf { x }$ 和 $\boldsymbol { \mathbf { b } }$   
do i=1,n $\mathrm { D i a g A ( i ) } = \mathbf { A } ( \mathrm { i , i } )$   
end do   
do while(error >ErrorBound)   
S1: $\begin{array} { r l } & { \mathrm { T e m p } { = } \left( \mathbf { b } - \mathbf { M A T M U L } ( \mathbf { A } , \mathbf { x } ) \right) \ \mathrm { \mathcal { N i a g A } } } \\ & { \mathbf { x } { = } \mathrm { T e m p } + \mathbf { x } } \\ & { \mathrm { e r r o r } { = } \mathbf { S U M } ( \mathrm { T e m p } \star \mathrm { T e m p } ) } \end{array}$   
S2:   
S3:   
end do

14.9雅可比松弛法MPI程序如下：参照它试写出雅可比松弛法PVM程序;并将两者加以比较。

$/ / \ast$ 雅可比松弛法的MPI编程代码段 $^ { * }$ //float Arow[N],X[N],NewX,B,error,Temp;MPI _Comm comm;  
error $\eqcirc$ SomeLargeValue;  
初始化 $\mathbf { A } , \mathbf { x }$ 和B  
MPI_Init(&argc,&argv);  
comm = MPI_COMM_WORLD;  
MPI_ Comm_rank(comm,&my_ rank);while(error>SomeErrorBound）{$\mathtt { T e m p } = \mathtt { B } ;$   
$\mathbf { f o r ( \vec { i } = 0 ; i < N ; i + \Delta + \Delta ) T e m p - = A r o w [ i ] * X [ i ] } ,$   
Temp/= A[my_rank];  
$\mathrm { \cal N e w } { \bf X } = { \sf T e m p } + { \bf X } \left[ \mathrm { \bf \ m y } \_ { \mathrm { \bf \ m a n k } } \right] ;$   
MPI_Allgather (&NewX,1,MPI_FLOAT,&X,1,MPI _FLOAT,comm);Temp $=$ Temp $\bigstar$ Temp;  
MPI _Allreduce (&Temp,&error,1,MPI _FLOAT,MPI_SUM,comm);

# 14.10Fortran 90 计算 $\pmb { \pi }$ 的程序如下：参照它试写出计算 $\pmb { \pi }$ 的 HPF程序;并将两者加以比较。

$/ / \ast$ 计算 $\pmb { \pi }$ Fortran 90编程代码段 $\star$ /

1. INTEGER,PARAMETER: : $\mathbf { N } { } = 1 3 1 0 7 2$   
2. INTEGER,PARAMETER: : LONG $=$ SELECTED_REAL_KIND(13,99)   
3. REAL( $\mathbf { \bar { \rho } } _ { \mathbf { K I N D } = \mathbf { L O N G } } ^ { \prime }$ PI,WIDTH   
4. INTEGER,DIMENSION(N) : : ID   
5. REAL $\mathbf { \tilde { \rho } } _ { \mathbf { K I N D } = \mathbf { L O N G } } )$ ,DIMENSION(N)::X,Y   
6. $\mathbf { W I D T H } = 1 . 0$ _LONG/N   
7. $\mathrm { I D } { = } \left( / ( \mathrm { I } , \mathrm { I } { = } 1 , \mathrm { N } ) / \right)$   
8. $\mathbf { X } = \left( \mathbf { I D } - \mathbf { 0 } . 5 \right) * \mathbf { W } \mathbf { I D T H }$   
9. $\mathbf { Y } { = } 4 . 0 / ( 1 . 0 + \mathbf { X } * \mathbf { X } )$   
10. $\mathbf { P I } = \mathbf { S U M } ( \mathbf { \nabla \mathbf { Y } } ) \ast \mathbf { W I D T H }$   
11. FORMAT('ESTIMATION OF PI WITH',I6,&   
12. 'INTERVALS IS',F14.12)   
13. PRINT10,N,PI   
14. END

# 附录一 MPI的函数的C语言说明

double MPI_Wtime(void)   
int MPI_Init(int $\clubsuit$ argc,char\* \* \* argv)   
int MPI_Finalize(void)

int MPI_Send(void \* buf,int count,MPI_Datatype datatype,int dest,int tag,MPI__Comm comm) int MPI_Recv (void \* buf,int count,MPI_Datatype datatype,int source,int tag,MPI_Comm comm,MPI Status \* status) int MPI_Isend (void \*buf,int count,MPI_Datatype datatype,int dest,int tag,MPI_Comm comm,MPI_

Request \* request)

int MPI_ Isend (void \* buf,int count,MPI_Datatype datatype,int dest,int tag,MPI_ Comm comm,MPI_ Request \* request)

int MPI_Wait(MPI_Request \* request,MPI_Status \* status) int MPI _Test(MPI_Request \* request,int $^ { \star }$ flag,MPI_Status \* status) int MPI_Iprobe(int source,int tag,MPI__Comm comm,int \* flag,MPI_Status \* status) int MPI_Probe(int source,int tag,MPI_Comm comm,MPI_Status \* status) int MPI _ Get __count(MPI __Status \* status,MPI _Datatype datatype,int \* count)

int MPI_ Type_contiguous(int count,MPI_Datatype oldtype,MPI_Datatype \* newtype) int MPI_ Type_vector (int count,int blocklength,int stride,MPI_Datatype oldtype,MPI_Datatype \* newtype)

int MPI_Type_indexed (int count,int \* array_of_blocklengths,int $\clubsuit$ array_of_displacements,MPI_Datatype oldtype,MPI_ Datatype \* newtype)  
int MPI_Type_commit(MPl_Datatype \* datatype)  
int MPI_ Type_free(MPI _ Datatype \* datatype)

int MPI_ Barier(MPI_Comm comm)

int MPI_Bcast(void \*bufer,intcount,MPIDatatypedatatpeintroot,MPICommcomm)

int MPI_ Gather (void \* sendbuf,int sendcount,MPI_Datatype sendtype,void \* recvbuf,int recvoount,MPI _Datatype recvtype,int root, MPI_ Comm comrm)

int MPI_ Scater (void \* sendbuf,int sendcount,MPI_Datatype sendtype,void \* recvbuf,int recvcount,MPI _Datatype recvtype,int root,MPI _Comm comm)

int MPI _ Algather (void $\nmid$ sendbuf,int sendount,MPIDatatype sendtype,void \* recvbuf,intrecvcount, MPI _Datatype recvtype,MPI _Comm comm)

int MPI_ Altoall(void \* sendbuf,int sendcount,MPI_Datatype sendtype,void \* recvbuf,int recvcount,MPI_Datatype recvtype,MPI__Comm comm)

int MPI_Reduce (void \* sendbuf,void \* recvbuf,int count,MPI_Datatype datatype,MPI_Op op ,int root, MPI _ Comm comm)

int MPI_ Alreduce (void \* sendbuf, Void \* recvbuf,int count,MPI__Datatype datatype,MPI_Op op,MPI _ Comm comm)

int MPI_Comm_ size(MPI _Comm comm,int \* size)   
int MPI_Comm_rank(MPI_Comm comm,int \* rank)   
int MPI_Comm_dup(MPI__Comm comm,MPI_Comm \* newcomm)   
int MPI __ Comm __ split(MPI _Comm comm,int color,int key,MPI __ Comm \* newcomm)   
int MPI__Comm_free(MPI__Comm \*comm)   
int MPI_Intercomm_create (MPI_Comm local_comm,int local_leader,MPI_Comm peer_comm,int remote_ leader,int tag,MPI _Comm \* newintercomm)

# 附录二 MPI的函数的Fortran语言说明

DOUBLE PRECISION MPI_WTIME() MPI_INIT(IERROR)

INTEGER IERROR MPI_FINALIZE(IERROR)

INTEGER IERROR

MPI_ SEND(BUF,COUNT,DATATYPE,DEST,TAG,COMM,IERROR)

<type>BUF( \*)

INTEGER COUNT,DATATYPE,DEST,TAG,COMM, IERROR

MPI_RECV(BUF,COUNT,DATATYPE,SOURCE,TAG,COMM,STATUS,IERROR)

<type>BUF（ \*）

INTEGER COUNT,DATATYPE,SOURCE,TAG,COMM,STATUS(MPI_ STATUS_ SIZE), IER-ROR

MPI_ ISEND(BUF,COUNT,DATATYPE,DEST,TAG,COMM,REQUEST,IERROR)

<type>BUF( \*)

INTEGER COUNT,DATATYPE,DEST,TAG,COMM,REQUEST,IERRORMPI_ IRECV(BUF,COUNT,DATATYPE,SOURCE,TAG,COMM,REQUEST,IERROR)

<type>BUF(\*)

INTEGER COUNT,DATATYPE,SOURCE,TAG,COMM,REQUEST,IERRORMPI_WAIT(REQUEST,STATUS,IERROR)

INTEGER REQUEST,STATUS(MPI_STATUS_SIZE),IERRORMPI_TEST(REQUEST,FLAG,STATUS,IERROR)

LOGICAL FLAG

INTEGER REQUEST,STATUS(MPI_ STATUS__SIZE), IERRORMPI_ IPROBE(SOURCE,TAG,COMM,FLAG,STATUS,IERROR)

LOGICAL FLAG

INTEGER SOURCE,TAG,COMM,STATUS(MPI_STATUS_SIZE),IERRORMPI_ PROBE(SOURCE,TAG,COMM,STATUS,IERROR)

INTEGER SOURCE,TAG,COMM,STATUS(MPI_STATUS_SIZE),IERRORMPI_GET_COUNT(STATUS,DATATYPE,COUNT,IERROR)

INTEGER STATUS(MPI_ STATUS_ SIZE),DATATYPE,_ COUNT,IERROR

MPI_TYPE_CONTIGUOUS(COUNT,OLDTYPE,NEWTYPE,IERROR)

INTEGER COUNT,OLDTYPE,NEWTYPE, IERROR MPI_TYPE_VECTOR(COUNT,BLOCKLENGTH,STRIDE,OLDTYPE,NEWTYPE,IERROR)

INTEGER COUNT,BLOCKLENGTH,STRIDE,OLDTYPE,NEWTYPE, IERRORMPI_TYPE__INDEXED(COUNT, ARRAY_OF_BLOCKLENGTHS,

ARRAY_OF__DISPLACEMENTS,OLDTYPE,NEWTYPE, IERROR)

INTEGER COUNT,ARRAY_OF_BLOCKLENGTHS( $\pmb { \mathscr { k } }$ ),ARRAY__ OF_DISPLACEMENTS（\*），

OLDTYPE,NEWTYPE,IERRORMPI_TYPE_COMMIT(DATATYPE,IERROR)

INTEGER DATATYPE,IERRORMPI_TYPE_FREE(DATATYPE,IERROR)

INTEGER DATATYPE,IERROR

MPI_BARRIER(COMM,IERROR)

INTEGER COMM,IERRORMPI_BCAST(BUFFER,COUNT,DATATYPE,ROOT,COMM,IERROR)

<type>BUFFER( $\pmb { \ k }$ ）

INTEGER COUNT,DATATYPE,ROOT,COMM,IERROR

ROOT,COMM,IERROR)

< type>SENDBUF( $\star$ ),RECVBUF( $\pmb { \mathscr { \star } }$ ）

INTEGER SENDCOUNT,SENDTYPE,RECVCOUNT,RECVTYPE,ROOT,COMM,IERROR MPI_ SCATTER(SENDBUF,SENDCOUNT,SENDTYPE,RECVBUF,RECVCOUNT,RECVTYPE,

ROOT,COMM,IERROR)

< type> SENDBUF( $\star$ ),RECVBUF( $\star$ ）

INTEGER SENDCOUNT,SENDTYPE,RECVCOUNT,RECVTYPE,ROOT,COMM,IERROR MPI_ ALLGATHER(SENDBUF,SENDCOUNT,SENDTYPE,RECVBUF,RECVCOUNT,

RECVTYPE,COMM,IERROR)

< type> SENDBUF( $\bigstar$ ),RECVBUF( \* )

INTEGER SENDCOUNT,SENDTYPE,RECVCOUNT,RECVTYPE,COMM,IERRORMPI_ ALLTOALL(SENDBUF,SENDCOUNT,SENDTYPE,RECVBUF,RECVCOUNT,RECVT

COMM,IERROR)

<type>SENDBUF( \*),RECVBUF（ \*)

INTEGER SENDCOUNT,SENDTYPE,RECVCOUNT,RECVTYPE,COMM,IERRORMPI_REDUCE(SENDBUF,RECVBUF,COUNT,DATATYPE,OF,ROOT,COMM,IERROR)

< type> SENDBUF( $\bigstar$ ),RECVBUF( $\pmb { \mathscr { k } }$ ）

INTEGER COUNT,DATATYPE,OP,ROOT,COMM, IERROR

MPI_ALLREDUCE(SENDBUF,RECVBUF,COUNT,DATATYPE,OP,COMM,IERROR)

< type>SENDBUF( $\star$ ),RECVBUF( $\divideontimes$ ） INTEGER COUNT,DATATYPE,OP,COMM,IERROR

MPI__COMM_SIZE(COMM,SIZE,IERROR)

INTEGER COMM,SIZE,IERRORMPI_COMM_RANK(COMM,RANK,IERROR)

INTEGER COMM,RANK,IERROR MPI_COMM_DUP(COMM,NEWCOMM,IERROR)

INTEGER COMM,NEWCOMM, IERROR

MPI_COMM_SPLIT(COMM,COLOR,KEY,NEWCOMM,IERROR)

INTEGER COMM,COLOR,KEY,NEWCOMM,IERROR MPI_COMM_FREE(COMM,IERROR)

INTEGER COMM,IERROR

API_ INTERCOMM_CREATE(LOCAL_COMM,LOCAL_LEADER,REER_COMM,

REMOTE_LEADER,TAG,NEWINTERCOMM,IERROR)

INTEGER LOCAL_ COMM,LOCAL_LEADER,PEER _ COMM; REMOTE_LEADER,TAG, NEWINTERCOMM,IERROR

# 第十五章 并行程序设计环境与工具

广义上讲,并行程序设计环境系由硬件平台、支撑语言、系统软件、应用软件包和软件工具等组成;狭义上讲,并行程序设计环境就是由一组并行程序设计工具所组成。所谓软件工具系指任何能帮助软件开发过程的辅助工具；而程序设计工具系指任何有助于程序员编程的辅助工具。显然软件工具含意较广,进行程序设计总要利用某些软件工具。所以本章先从一般的软件工具环境讲起，然后重点介绍并行程序设计语言的并行编译器以及并行程序的调试工具、性能分析工具和可视化设计工具。

# \*15.1 软件工具与环境

# 15.1.1 编码工具

编辑器(Editor） 它是一种具有编辑功能的程序设计工具,其功能从简单的文本编辑器到语法制导(Syntax-Directed)或语言敏感(Language-Sensitive)的编辑器。目前最普通的程序编辑器是知识语言(Language-Knowledgeable)编辑器,它借助语言知识来增强编辑能力,例如可自动缩进(Indentation)、括号检查，甚至简单交叉引用等。Emacs 就是这样的编辑器[79]。

编译器(Compiler）它将源代码转换成机器可执行的代码（或实际机器代码或能被解释的中间代码)形式。各种编译器的差别在于执行优化的程度不同以及它们是不是渐增的(Incremental,即只当变化时才编译)或成批的。并行编译的技术难点是对一个源程序如何识别出可并行执行的部分而将其并行化，同时保证整个程序的正确运行。本章第15.2节会专门对此进行讨论。

连接器和加载器(Linker andLoader）它们将编译好的文件与库连接在一起以产生一个可执行的文件。因为库的内容一直在增加,因此连接时间占了编辑-编译-查错总时间的相当部分。使用渐增连接器可缓解此问题，渐增连接器只修改那些已改变的可执行部分。

预处理程序(Preprocessor）它提供超过基本源语言范围的某些能力,这些能力可内置在源语言中(如C预处理器),也可以由它们自己的语言提供(如 Lex和Yacc)。

交叉引用程序(CrossReferencer）它提供将名字和其定义相关联的方法。交叉引用信息可有效地由编译器产生，它可以用在编辑器中,也可用在文本或者图形显示的独立系统中。普通图形交叉引用工具，可提供调用图和面向对象程序的类层次图的显示。

源级查错器(Source-LevelDebugger）它允许用户用设置断点等方法控制程序的执行。更先进的查错工具能够处理优化的代码和库以及同一系统中的多种语言。现今这些工具已配用程序的可视显示手段，允许程序员观察应用的数据结构。

查错辅助程序(Debugging Aids）它们提供超过程序设计语言范围的在编译或运行时的检查工具,还包括那些甚至编译器发现是合法结构的潜在问题的系统和库。

# 15.1.2 软件工程工具

这些工具牵涉到整个系统的维护而不是代码本身,现今这类工具包括：

系统构造程序(System Builder）该工具允许用户定义系统应如何建造系统模型，模型包括相关性、编译选项和应该执行什么命令等信息;然后工具应能够构筑原型系统或者基于一组源文件变化渐增的更新系统。

版本管理程序（Version Manager）该工具允许一个源文件的多种版本同时共存。这样就允许多个程序员共同开发系统,允许在新版本开发的同时维护已发布的系统的老版本,或者允许单一系统不同定制版本的共存。

设计编辑器(Design Editor）该工具使用户采用各种图形设计符号设计一个系统。CASE(Computer-Aided Software Engineering)就是这样的工具,它使用Petri网、SADT[150]、状态图和面向对象的设计OMT[151]等表示来开发软件。很多这样的工具至少能基于设计产生代码框架。如果提供足够的设计信息，有些工具能够模拟系统的若干方面,同时允许开发者在较高级测试设计。

代码产生器(Code Generator）该工具也称为第四代语言,它实际上是让程序员交互地指定系统的大部分而不必进行编码的专用高级语言。它们普遍地用于定义用户界面和程序与数据库系统的相互作用。

测试辅助程序（Testing Aids）该工具试图将测试软件系统的过程自动化。其范围从测试事例产生器(用于分析源代码或说明以产生一组测试实例)到回归测试系统(程序员产生测试事例,系统施行内务操作,包括运行每个测试实例、确定它是否成功或失败以及报告结果)。

# 15.1.3集成工具

软件工具可以使用不同的集成技术进行组合。早期,或采用不同工具的松散联合，或将所有相关的工具组合成单一系统。单一系统的优点是,紧密地将一些工具耦合在一起使得程序员对环境有所了解;其缺点是，此单一系统是个封闭系统,很难加入新的工具,或很难使用多种语言或者现存代码，而且系统相当庞大。紧密的联合可以解决不少问题,它是个开放系统,易于开发和利用新工具，且系统可以使用多种语言和库构筑之。然而，它把正确使用工具的义务转给程序员且不提供公共框架。目前已提出三种将工具集成为环境的方法：

数据集成(Data Integration）该方法使诸工具共享信息,为此要开发一个能保存各个工具必须共享的信息数据库。例如,编译器产生的中间表示可存人数据库中并且能被别的工具直接使用,以避免重新进行源程序语法分析。此法的缺点是，所要求的数据库很大，而且为了确保环境正常工作,数据库系统必须是先进的；同样这样的环境趋于封闭而不是开放。

公共前端(Common Front End）在软件开发中最流行的工具是用于生成程序、文本、系统模型等的文本编辑器。它相对容易地可嵌入编辑器的命令中，这些命令可调用其它工具并使用那些工具的输出。这种集成方法为各种工具提供一个公共的界面,而且如果它们有一个文本界面就可使新的工具很简单地被集成。因为这些工具实际不共享信息，所以程序员仍旧知道不同的工具及其使用方法。

控制集成(Control Integration）它涉及到工具之间的消息传递。在此，每当诸工具需共享信息时和调用命令时就彼此发送消息。通常不使用点到点消息传送,而是使用中央消息服务器作为中介物,每个工具都要告诉消息服务器它们对什么消息感兴趣。此法集成度较高，允许多种工具尤如是一个那样进行操作。

实际的环境可以是上述不同集成方法的组合。例如,PCTE标准[37]就使用了控制集成，以及在数据集成之上的公共前端实用程序。

# 15.1.4将来的工具与环境

因为软件的开发是个困难和费时的过程,所以人们不断地发展和推广现有的工具和环境。可以预计将来的工具一定比现在的好：较快的编译器、渐增的加载器、较好和更多的查错辅助程序和完善的编辑器等等。相应地,这些先进工具的集成会形成一个开放的环境。现在的研究旨在推广软件工具以支持一些新的领域：

过程工具(Process Tools）这些工具帮助管理软件开发过程,它们允许使用规则和步骤定义过程;然后提供过程内务操作和管理的帮助。

群件工具(Groupware Tools）这些工具允许多个程序员以受控方式联合工作。版本管理为多个程序员提供一个基础,而新的工具将会促进分布在不同场点的开发者之间的合作和交互能力的增强。

可视化工具（Visualization Tools）现行的可视化主要集中在类层次显示、调用图或模块的显示以及受限的数据结构可视化上，提供大量程序数据的高质量显示有待增强。这些将会变成软件环境的标准部分。

程序分析工具(Program Analysis Tools） 这些工具承担系统的详细语义分析并向用户提供反馈。反馈可能与潜在的问题、代码和说明之间的失配、帮助归并不同版本或重定工程代码(Reengineering Code)有关。

# 15.2 并行编译器

一旦一个程序以某种高级语言书写完成后,在正式运行前,必须将此程序转换成实际机器能够理解的机器语言(指令集)。此过程就是编译(Compile),而编译器实际上就是实现此转换的一种语言处理程序。编译过程可分为： $\textcircled{1}$ 词法分析； $\textcircled{2}$ 语法分析； $\textcircled{3}$ 中间代码产生； $\textcircled{4}$ 代码优化； $\textcircled{5}$ 代码生成等几个阶段。上述几个阶段或多或少都是顺序执行的。而并行化编译面临的任务是：给定一个在单处理机上运行较长的串行程序和一台具有多个处理器可同时工作的并行计算机,目的是将申行程序分解成若干个能并行执行或至少能重叠执行的代码段，使其在并行机上能较快地运行。所以并行编译器主要工作就是寻找代码的并行性,然后将其调度在并行机上高速正确地执行。

如图15.1所示，一个并行编译器大致可由三部分组成：流分析、程序优化和代码生成。其中，流分析是确定源代码中数据和控制的相关性;优化常常是将代码变换成与之等效但具有"更好"的形式,以利于尽量挖掘硬件潜力,最终达到全局优化的目的;代码生成通常涉及到从一种描述转换成另一种中间形式的描述，不同类型的计算机其并行代码的生成也各不相同。在正式讨论并行编译器之前,先对编译及其并行化作一概括介绍,以期读者对此有个感性的认识。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0006_pages_0351-0420/auto/images/f81c689f779e56ba3980b5ca4c0cfdd850ed3181b7f3ec532fa17eee054ca550.jpg)  
图15.1并行编译过程

# 15.2.1 编译及其并行化

图15.2示出了编译器将一个高级语言的代码段翻译成汇编语言形式的机器目标代码的过程。最右边还给出了经过简单优化后使用较少指令的目标代码。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0006_pages_0351-0420/auto/images/8f75f745b6bfa1f3bb85dbd7f6011262fdf83c1262f3a2f032e4369e573ec71a.jpg)  
图15.2例示编译过程

事实上,最左边的源代码经过词法分析器首先被分解成一些原子目标（即tokens),再把它们分类为操作符、常数、分隔符、标志符等;然后经过语法分析器,分析程序的文法结构、检查错误,最后转换成类似于图15.3的语法分析树；产生中间代码是为了便于移植和优化，中间代码和汇编语言的主要区别是,前者不必为每种操作之输人和输出指定实际的寄存器和存储器位置;优化的目的是使程序运行得较快和使用较少的存储器,其主要方法重排编译后的代码(即所谓代码移动),它是建立在流分析的基础上的,是程序向量化和并行化的关键。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0006_pages_0351-0420/auto/images/ae5378ee1a8fdd375b0e4a1e954d135aeece98aae593ec4446b66b63b26e21c0.jpg)  
图15.3表达式 $\mathbf { A } \mathcal { B } \ast \mathbf { C }$ 与 $\mathsf { A } \div$ $\bf \Pi \cdot B \times C )$ 的分析树

一般而言，有两种并行化代码段的方法：SIMDizing(即向量化,Vectorizing)和MIMDizing(即并行化Parallelizing)。如图15.4所示，代码段的程序流图被分成几个不同的计算调度单元。此时，DO循环可被分布成三个不同的相互独立的循环,它们分别标志为"向量”、“向量"和“递归"：其中前两个循环执行简单的、相同的和独立的算术运算,因此每个循环都可用一条向量指令代替之，从而达到向量化;后一个循环涉及到递归,是彼此相关的,所以无法向量化,但可将代码分成可供MIMD多处理机执行的几个任务，每个处理器负责循环的若干次迭代,各处理器之间再施行必要的同步就可达到并行化。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0006_pages_0351-0420/auto/images/516ff42a932c71f019b87379febe04ef042f43c9b7c0d2a16d252910a30c0cdc.jpg)  
图15.4两种并行化的方法

下面结合一段具体的程序代码，分别给出相应的向量化和并行化的结果，以期读者对两种并行化方法有个感性认识。

<table><tr><td rowspan=1 colspan=1>顺序代码</td><td rowspan=1 colspan=1>向量化代码</td><td rowspan=1 colspan=1>并行化代码</td></tr><tr><td rowspan=1 colspan=1>(1)A=B+C(2）DO 5 I=1,N(3)D(I)=A*E(I)(4) S=E(I) *5(5) T=T+S(6)A=D(N)-7</td><td rowspan=1 colspan=1>(1)A=B+C(3) D(1:N)=A*E(1:N)(3.1) Allocate S&#x27;(1:N)(4) S&#x27;(1:N)=E(1:N) * 5(5.1) S=S(N)(5.2) Free S&#x27;(N)(5.3) I=N+1(6) A=D(N)-7</td><td rowspan=1 colspan=1>A=B+CWith N ProcessorsLocal S&#x27;D(#)=A*E(#)S=E(#)*5T=T+S&#x27;   ■   SynchIF(# ·EQ·N)THENS=S&#x27;A=D(N)-7I=N+1ENDIF</td></tr></table>

# 15.2.2相关分析

要并行执行几个程序段，必须使每段与其它各段无关。研究计算程序中所有语句间的相关性称为相关分析(Dependency Analysis)。准确有效的相关测试对发挥并行化编译器的功效十分重要。先定义如下四种形式的相关。假定语句$\mathsf { S } _ { j }$ 继语句 $\mathsf { S } _ { i }$ 之后执行，其定义及符号约定如下：

$\textcircled{1}$ 流相关：如果从 $\mathsf { S } _ { i }$ 到 $\mathbf { S } _ { j }$ 存在执行通路,而且如果 $\mathbf { S } _ { i }$ 至少有一个输出可供$\mathsf { S } _ { j }$ 用作输人,则语句 $\mathbf { S } _ { j }$ 与语句 $\mathsf { S } _ { i }$ 流相关(Flow-Dependent),记之为 $\mathsf { S } _ { i } \delta \mathsf { S } _ { j }$ 。

$\textcircled{2}$ 反相关：如果S紧接 $\mathsf { S } _ { i }$ ，而且如果 $\mathbf { S } _ { j }$ 的输出与 $\mathsf { S } _ { i }$ 的输人重叠,则语句 $\mathsf { S } _ { j }$ 与语句 $\mathsf { S } _ { i }$ 反相关(Antidependent）,记之为 $\mathbf { S } _ { i } \overline { { \ 8 } } \mathbf { S } _ { j }$ 。

$\textcircled{3}$ 输出相关:如果两语句能产生(写)同一输出变量,则两者是输出相关(Out-put-Dependent）,记之为 $\mathsf { S } _ { i } \mathfrak { F S } _ { j }$ 。

$\textcircled{4}$ 控制相关：如果语句 $\mathsf { S } _ { j }$ 的执行依赖于语句 $\mathsf { S } _ { i } ( \mathsf { S } _ { i }$ 必须在 $\mathsf { S } _ { j }$ 之前执行),则语句 $\mathbf { S } _ { j }$ 与语句 $\mathsf { S } _ { i }$ 控制相关(Control-Dependent),记之为 $\mathrm { S } _ { i } \delta ^ { \mathrm { c S } _ { j } }$ 。

图15.5分析了上一节中所列举的顺序代码的各种相关(不包括控制相关)。

向量数组的相关分析比标量数据的相关分析要复杂得多，本节只概略讨论数据数组相关分析的基本概念,有兴趣的读者可参阅[100]。

相关距离向量和相关方向向量令 ${ \pmb { \alpha } } = ( { \pmb { \alpha } } _ { 1 } , { \pmb { \alpha } } _ { 2 } , \cdots , { \pmb { \alpha } } _ { n } )$ 和 $\pmb { \beta } = ( \beta _ { 1 } , \beta _ { 2 } , \cdots , \beta _ { n } )$ 是在 $\pmb { n }$ 层循环上界和下界范围内的 $\pmb { n }$ 个整数指标向量，假定 $\pmb { \alpha }$ 和 $\pmb { \beta }$ 存在数据相关性;则相关距离向量(Dependent Distance Vector $) \mathbf { D } { = } \left( D _ { 1 } , D _ { 2 } , \cdots , D _ { n } \right)$ 定义为$\beta - \alpha$ ,相关方向向量(Dependent Direction Vector) $\pmb { d } = ( d _ { 1 } , d _ { 2 } , \cdots , d _ { n } )$ 定义为：

$$
d _ { i } = \left\{ \begin{array} { l l } { < \ddagger { \alpha _ { i } } < \beta _ { i } } \\ { = \ddagger { \alpha _ { i } } < \beta _ { i } } \\ { > \ddagger { \alpha _ { i } } < \beta _ { i } } \end{array} \right.
$$

例如,假定有如下循环嵌套：

$$
\mathbf { D O } \mathbf { i } { = } \mathbf { L } _ { 1 } , \mathbf { U } _ { 1 }
$$

$$
\mathrm { { \bf D 0 } } \mathrm { { \bf j } } = \mathrm { L } _ { 2 } , \mathrm { { \bf U } } _ { 2 }
$$

$$
\mathbf { D O } \mathbf { \ k } = \mathrm { L } _ { 3 } , \mathrm { U } _ { 3 }
$$

$$
\mathbf { A } ( \mathrm { i } + 1 , \mathrm { j } , \mathrm { k } - 1 ) = \mathbf { A } ( \mathrm { i } , \mathrm { j } , \mathrm { k } ) + \mathbf { C }
$$

# Enddo

则数组A的三维迭代之间的相关距离向量和相关方向向量分别为(1,0，－1)和$( < , = , > )$ 。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0006_pages_0351-0420/auto/images/963e07c78f77ea3f9724c31aab8ae9d76df0f2c7f0f0f53cd55afa13226e3201.jpg)

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0006_pages_0351-0420/auto/images/aef4826bfb9221e8247d2439f0768a776819de2817c04f486e5cc8aa5a356170.jpg)  
图15.5相关分析示例

相关类型：

<table><tr><td rowspan=1 colspan=1>（A=A</td><td rowspan=1 colspan=1>8（流），</td></tr><tr><td rowspan=1 colspan=1>1=AA=</td><td rowspan=1 colspan=1>（反）</td></tr><tr><td rowspan=1 colspan=1>A=A=</td><td rowspan=1 colspan=1>8（输出）</td></tr></table>

相关性：

381 683 68°l   
683   
584 48°4 48 5   
585 585585

相关方向向量对计算循环体间相关性十分有用。这里,相关性是通过相关方向向量中方向不是 $^ { \mathfrak { a } } = { } ^ { \mathfrak { a } }$ ”号的外层循环传递的。所以上述相关方向向量 $( < ,$ 、$\mathbf { \epsilon } = \mathbf { \epsilon } , > )$ 所表示的相关性就是在循环 $i$ 传递的。相关距离向量指明在对同一存储单元的两次访问之间循环迭代的实际距离。它们对开发并行性或优化存储器层次结构将起到指引作用。

相关方程(Dependent Equation）设 $\pmb { \alpha }$ 和 $\pmb { \beta }$ 是在 $\pmb { n }$ 层循环上界和下界范围内的n个整数指标向量。当且仅当存在α和β,并且α按字典序小于或等于β以及满足下述相关方程时，则从 $\mathbf { S } _ { i }$ 到 $\mathrm { \bf S } _ { j }$ 存在相关性：

$$
{ \int _ { i } ^ { } ( } \alpha { \ ) = } _ { E i } ( \beta )
$$

否则两次引用都是不相关的。

(15.2)式中的相关方程是循环指标变量的线性表达式。所以测试相关性相当于求解线性 Diophantine方程,它是NP-完全问题。

数据相关性测试(Dependency Testing）进行相关性测试目的有二：一是试图证明同一数组变量的下标引用对(即引用两个数组某维中的一对下标)之间的相关性是不存在的；二是若相关性存在，则应以某种方式（例如使用相关方向向量的最小全集)将它们表示出来。相关测试采用比较保守的策略，若不能证明任何相关性是不存在的话，则就认为它们是存在的。

进行相关性测试所追求的目标，就是构造相关距离向量或相关方向向量的全集。此全集可以表达对同一数组变量任意下标引用对之间可能存在的相关性。这实际上是求方程组(15.2)的通解，已如上述这是个NP-完全难解问题。精确测试是当且仅当相关性存在时,检查这些相关性,它所花费的开销太大，因而精确解无法实现,只好采用近似测试法。最常用的两个近似测试法是最大公约数测试,即GCD测试[183]和Banerjee不等式测试[24]。本书限于篇幅就不再讨论了。

# 15.2.3代码优化

代码优化(CodeOptimization)的目的是使代码执行速度达到最高,这就要求代码长度最短、存储器访问次数最少以及程序的并行性得到较好的开发。优化技术包括用流水线硬件完成向量化和同时用多台处理器实现并行化。向量化是把标量循环操作转换成等效的向量指令执行的过程；并行化的目的是把顺序代码转换成并行形式，使多台处理机能同时并行执行。向量硬件用来加速向量操作,多处理机或多计算机用来执行并行代码。本节简要讨论代码向量化方法和代码并行化方法。

代码向量化(CodeVectorization)方法向量是一维的,所以直观上讲,向量程序设计就是把标量程序中的由一种可向量化循环完成的操作改成向量操作。常用的代码向量化的基本方法包括：

①直接向量化法：它是把申行程序中的循环直接用数组运算语句来描述。

例15.1 DO $\mathbf { I } = 8 , 1 2 0 , 2$ $\mathbf { A } ( \mathbf { I } ) = \mathbf { B } { \bigl ( } \mathbf { I } + 3 { \bigr ) } + \mathbf { C } { \bigl ( } \mathbf { I } + 1 { \bigr ) }$ ENDDO

此标量循环可直接转换成一条由下列数组赋值语句定义的向量化指令：

$$
{ \bf A } ( 8 : 1 2 0 : 2 ) = { \bf B } ( 1 1 : 1 2 3 : 2 ) + { \bf C } ( 9 : 1 2 1 : 2 )
$$

②含条件语句的循环向量化：循环中的条件语句可以用WHERE语句向量化。

例15.2 DO $\mathbf { I } = 1 , \mathbf { N }$ $\mathrm { I F } \left( \mathrm { L } ( \mathrm { I } ) \cdot \mathrm { N E } \cdot 0 \right) \quad \mathrm { A } ( \mathrm { I } ) = \mathrm { A } ( \mathrm { I } ) - 1$ ENDDO

它可向量化为：

$$
\mathbf { W H E R E } ( \operatorname { L } ( \mathbf { \lambda } ) \cdot \mathbf { N E } \cdot \mathbf { 0 } ) \quad \mathbf { A } ( 1 : \mathbf { N } ) = \mathbf { A } ( 1 : \mathbf { N } ) - 1
$$

③语序重排向量化法：有时按照循环中原有的语序会因数据相关而妨碍向量化,此时交换一下语句顺序即可向量化。

例15.3 DO ${ \mathbf { I } } = { \mathbf { 1 } } \mathbf { \Gamma } , { \mathbf { N } }$ $\mathbf { A } ( \mathbf { \pi } _ { \mathrm { I } } ) = \mathbf { B } ( \mathbf { \pi } _ { \mathrm { I } } - \mathbf { 1 } )$ $\mathsf { B } ( \mathrm { I } ) = 2 * \mathsf { B } ( \mathrm { I } )$ ENDDO

上例中对B的引用导致一个妨碍向量化的流相关，但把两语句执行顺序交

换一下即可得到如下形式的向量化：

$\mathtt { B } ( 1 : \mathbb { N } ) = 2 * \mathtt { B } ( 1 : \mathbb { N } )$ $\mathrm { A } ( 1 { : } \mathrm { N } ) { = } \mathrm { B } ( 0 { : } \mathrm { N } - 1 )$

$\textcircled{4}$ 引入临时数组向量化法：通过引入中间数组，有时可消除妨碍向量化的数据相关，从而达到向量化之目的。

例15.4 D0 $\mathbf { I } = \mathbf { 1 } , \mathbf { N }$

$$
\mathbf { A } ( \mathbf { I } ) = \mathbf { B } ( \mathbf { I } ) + \mathbf { C } ( \mathbf { I } )
$$

$$
\mathrm { B } ( \mathrm { I } ) { = } 2 * \mathrm { A } ( \mathrm { I } + 1 )
$$

ENDDO

上例中关于数组A存在一个反相关,兹引临时数组TEMP 先把 $\mathbf { A } ( 2 : \mathbb { N } +$ 1)暂存起来,就可得到如下形式的向量化：

$\mathrm { T E M P } ( 1 { : } \mathrm { N } ) = \mathrm { A } ( 2 : \mathrm { N } + 1 )$ $\mathrm { A } ( \mathbf { 1 } { : } \mathbf { N } ) { = } \mathbf { B } ( \mathbf { 1 } { : } \mathbf { N } ) + \mathbf { C } ( \mathbf { 1 } { : } \mathbf { N } )$ $\mathrm { B } ( \mathrm { 1 { : } N } ) { = } 2 * \mathrm { T E M P } ( \mathrm { 1 { : } N } )$

$\textcircled{5}$ 交换循环向量化法：向量化通常在内循环而不是在外循环进行。当内循环不能向量化而外循环可以向量时，则交换一下内外循环即可实现向量化。

例15.5D0 ${ \bf I } = 2 , { \bf N }$

$$
\mathbf { D O } \quad \mathbf { J } = 2 , \mathrm { N }
$$

$$
\mathrm { A } ( \mathrm { I } , \mathrm { J } ) = ( \mathrm { A } ( \mathrm { I } , \mathrm { J } - 1 ) + \mathrm { A } ( \mathrm { I } , \mathrm { J } + 1 ) ) / 2
$$

ENDDO

ENDDO

上例中数组A在J维存在着数据相关,故在J维不能向量化,兹将两层循环交换如下：

$$
\begin{array} { r l } & { \mathrm { J } = 2 , \mathrm { N } } \\ & { \mathrm { { \bf D O } } \quad \mathrm { I } = 2 , \mathrm { N } } \\ & { \quad \quad \quad \mathrm { A } ( \mathrm { I , J } ) = ( \mathrm { A } ( \mathrm { I , J } - 1 ) + \mathrm { A } ( \mathrm { I , J } + 1 ) ) / 2 } \end{array}
$$

现在I维(内层循环)无相关性了,所以向量化的代码为：

DO ${ \mathbf { J } } = 2 , { \mathbf { N } }$ $\begin{array} { r } { \mathbf { A } ( 2 { : } \mathbf { N } , \mathbf { J } ) = \left( \mathbf { A } ( 2 { : } \mathbf { N } , \mathbf { J } - \mathbf { 1 } ) + \mathbf { A } ( 2 { : } \mathbf { N } , \mathbf { J } + \mathbf { 1 } ) \right) / 2 } \end{array}$   
ENDDO

③ 循环分离向量化法：有时一个循环中只有部分语句可向量化,此时可将整个循环分离成两个：一个含可向量化的语句；另一个含不可向量化的语句，然后将能向量化的循环向量化之。

例15.6 DO ${ \bf \Lambda } [ = 1 , 1 0 0$ $\operatorname { A } ( \operatorname { I } ) = \operatorname { B } ( \operatorname { I } ) + \operatorname { C } ( \operatorname { I } )$ $\mathrm { D } ( \mathrm { I } ) = \mathrm { D } ( \mathrm { I } - 1 ) * \mathrm { E } ( \mathrm { I } )$ ENDDO

上例中第一个语句可向量化,第二个则不能，可把它分离成如下两个循环：

DO ${ \bf { I } } = 1 , 1 0 0$ $\mathrm { A ( I ) = B ( I ) + C ( I ) }$   
ENDDO   
DO ${ \bf I } = { \bf 1 } , { \bf 1 0 0 }$ $\mathrm { D } ( \mathrm { I } ) = \mathrm { D } ( \mathrm { I } - 1 ) * \mathrm { E } ( \mathrm { I } )$   
ENDDO

这样第一个循环可向量化为：

DO ${ \bf I } = { \bf 1 } , { \bf 1 0 0 }$ $\mathrm { A } ( 1 { : } 1 0 0 ) = \mathrm { B } ( 1 { : } 1 0 0 ) + \mathrm { C } ( 1 { : } 1 0 0 )$

ENDDO

$\textcircled{7}$ 迭代区间分段向量化法：例如当循环迭代区间从正到负变化时，整个迭代区间可能要分成几段才能向量化。

例15.7 DIMENSION A(-200,200) D0 $\boldsymbol { \mathrm { I } } = - 1 0 0$ ,100 $\mathbf { A } ( \mathbf { \sigma } _ { \mathrm { I } } ) = \mathbf { 0 }$ $\mathbf { A } ( 2 \times \mathbf { I } ) = \mathbf { 1 }$ ENDDO

此程序运行结果是：

$\mathrm { A } ( - 2 0 0 ) , \mathrm { A } ( - 1 9 8 ) , \cdots , \mathrm { A } ( 0 )$ 等于1；  
$\mathbf { A } ( - 9 9 ) , \mathbf { A } ( - 9 7 ) , \cdots , \mathbf { A } ( - 1 )$ 等于0；  
A(1) $, \mathsf { A } ( 2 ) , \cdots , \mathsf { A } ( 1 0 0 )$ 等于0；  
A(102),A(104),…,A(200)等于1。

显然本例不能直接向量化为A(-100:100)=0和A(－200:200:2)=1,也不能向量化为A(-200:200:2)=1和A(－100:100)=0,但若从0为分界点，I≤0时可按该循环的语句顺序进行向量化;当I>0时则必须按语句反序进行向量化,此时可得到如下的向量代码：

$\mathbf { A } ( - 1 0 0 : 0 ) = 0$ $\mathrm { A } ( - 2 0 0 { : } 0 { : } 2 ) = 1$ $\mathrm { A } ( 2 : 2 0 0 : 2 ) = 1$ $\mathrm { A } ( 1 { : } 1 0 0 ) { = } 0$

向量化的方法还有很多,在此就不再进一步讨论了。

代码并行化(Code Parallelization)方法并行代码的优化是将一个程序展开成许多线程以供多台处理机并行执行，其目的是要减少总的执行时间。在此线程就是在一台处理机上执行的指令序列。能否将一个程序分成多个线程并行执行,依赖于程序的数据和控制相关性。理想的情况是任何两个线程之间无相关性,所以可以并行执行;当线程之间有强相关性时,若加上适当的同步操作,则含有任何相关性的两个线程也可并行执行,极端的情况是同步多得使两个线程事实上还是串行执行的。

循环一般占程序的大部分运行时间,而循环的并行化分析和改写又相对较容易,所以十多年来有关代码并行化的研究主要集中在循环的并行化方面。因为组织循环并行执行的开销一般比组织循环向量化执行的开销大得多，所以对嵌套循环作并行化时总是选择外层循环进行并行化。这样使存储器能对数组中的连续元素进行访问，并将带有长向量的循环放到最内层进行向量化,从而缩短了总的执行时间。

返回去再看一下例15.5中的两层循环嵌套。因为I循环中的所有相关关系都有相关方向 $^ { \bullet } = { } ^ { \bullet }$ ,所以这个外层循环是可以并行化的,其并行化后的代码如下：

$$
\begin{array} { r l } { \mathbf { D } \mathbf { 0 } } & { { } \mathbf { J } = 2 , \mathbf { N } } \end{array}
$$

$$
\mathrm { A } ( \mathrm { I } , \mathrm { J } ) = \left( \mathrm { A } ( \mathrm { I } , \mathrm { J } - 1 ) + \mathrm { A } ( \mathrm { I } , \mathrm { J } + 1 ) \right) / 2
$$

ENDALL

此时外层循环中的 $\Nu - 1$ 次迭代都可以调度给不同的处理机执行。每个新创建的线程都由一个带I常数下标的完整的」循环组成。

下面给出一个例子综合说明一个程序循环的串行执行、并行化、向量化执行的各种组合情况。

例15.8 在Allant FX/80 处理机上一个FX/Fortran循环的五种执行方式[10]示例在图15.6中。

FX/Fortran可以用标量、向量、并发标量、并发向量及并发外层/向量内层(COVI)等五种方式来生成代码以执行简单的DO循环。例中所涉及的计算可以对一维数据数组A(1:2048)进行;也可以对二维数据数组B(1:256:1:8)进行,其中,A(K)=B(I,J),而K=8(I-1)+J。

图15.6(a)示出了用一台处理机顺序执行标量的情况。若利用数组A,则所涉及的计算可用一个纯标量循环表示如下：

DO $\mathtt { K } = 1$ ,2048

$$
\mathbf { A } ( \mathbf { K } ) = \mathbf { A } ( \mathbf { K } ) + \mathbf { S }
$$

ENDDO

其中S是标量常数。

图15.6(d)示出了用一台配有向量硬件的处理机执行8条向量指令的情况。每条向量指令处理下列256次迭代：

$$
{ \mathrm { A } } ( 1 { : } 2 0 4 8 { : } 2 5 6 ) = { \mathrm { A } } ( 1 { : } 2 0 4 8 { : } 2 5 6 ) + { \mathrm { S } } _ { \circ }
$$

图15.6(c)示出了用8台处理机并行执行如下的标量计算(标量并发方式)：

DOALL ${ \tt I } = 1 , 8$ DO ${ \bf J } = { \bf 1 } , 2 5 6$ $\mathbf { B } ( \mathbf { I } , \mathbf { J } ) = \mathbf { B } ( \mathbf { I } , \mathbf { J } ) + \mathbf { S }$ ENDDO  
ENDALL

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0006_pages_0351-0420/auto/images/c8ba85c71ab45d4f20bb6a588cb28ac297f493d2d971a1dc8a980c53fd81aa14.jpg)  
图15.6Alliant 多处理机上FX/Fortran 循环五种执行方式

图15.6(d)示出了用8台全部配有向量硬件的处理机上以向量并发方式执行如下代码的情况：

DOALL $J { = } 1 , 8$ $\mathbf { A } ( \mathrm { K } { : } 2 0 4 0 + \mathrm { K } { : } 8 ) = \mathbf { A } ( \mathrm { K } { : } 2 0 4 0 + \mathrm { K } { : } 8 ) + \mathbf { S }$

ENDALL

图15.6(e)示出了8台处理机以COVI方式执行，内层向量化执行，外层并行化执行，以Fortran 90 表示符则有：

$$
\mathrm { B } ( 1 { : } 8 , 1 { : } 2 5 6 ) = \mathrm { B } ( 1 { : } 8 , 1 { : } 2 5 6 ) + \mathrm { S }
$$

在代码并行化时，下列的情况往往会阻止或妨碍并行化： $\textcircled{1}$ 多个人口或出□； $\textcircled{2}$ 函数调用或子例程调用; $\textcircled{3}$ 输入/输出语句； $\textcircled{4}$ 并行执行的非确定性； $\textcircled{5}$ 循环体间的相关性。

总之，对向量化只是向后相关性有影响，而对并行化则向前和向后相关性都有影响；同步代码的开销可能会超过并行化所带来的好处；大多数代码的并行化都集中在循环级;并行化循环应尽量在最外层进行；在考虑并行化的粒度时，必须在计算和通信之间折衷考虑等。

# 15.2.4代码生成

并行代码生成(CodeGeneration)涉及到将优化后的中间形式的代码转换成可执行的具体的机器目标代码。因为目标机包含有不同的并行结构，所以并行机的代码生成仍还限制在每台处理机的范围内进行。不同类型的计算机的并行代码的生成也很不一样。例如，超标量处理机可能用软件调度也可能用硬件调度来实现。在RISC或超标量处理机上如何优化寄存器分配，在多处理机上如何降低同步开销,在多计算机上分布的代码/数据如何实现消息传递等,这些问题都给并行代码的生成增添了不少困难。当代码自动生成不易实现时，还可以使用编译命令来帮助并行代码的生成。

代码生成所涉及的问题很多,包括执行次序、指令选择、寄存器分配、负载平衡、并行粒度、代码调度以及后优化(Postoptimization)等。先进的代码生成技术应以开发并行性为目标，要为并行机开发真正的“智能”编译器，目前还相差甚远。

# 15.3 并行程序调试和性能分析

并行程序的设计不仅编程难，而且调试和分析更难。调试的目的是为了获得一个正确的并行程序；而性能分析是为了获得一个高效的并行程序。本节就并行程序调试的难点、技术和方法，并行程序的静态性能、动态性能的分析方法和可视化设计环境与工具作一简单介绍。

# 15.3.1并行程序的调试

串行程序的调试,有比较成熟的技术和工具(如Unix的dbx)。通过这些工具，程序员(用户)可在其程序中设置断点、采用步进和施行跟踪等手段来控制程序的执行和观察程序的运行状态，从而能发现错误所在。由于串行程序中语句执行次序是确定的，所以只要输人数据不变，程序的走向和产生的结果是不变的，因而用户可以重复运行同一程序来逐步定位错误所在。

并行程序调试(Parallel Program Debugging)技术和手段尚不成熟，难以借鉴串行程序的调试方法。向量化的引人并未给程序调试带来太大的困难，因为向量化的程序仍是单指令流的程序，其仍具有运行确定的特点；并行化的引入给程序调试带来相当大的难度，因为并行化的程序语句执行的次序是不确定的。这种不确定性意味着特殊的机器指令执行序列是不可重现的，因而难以跟踪观察；同时不确定性使得并行程序对相同的输人多次运行会产生不同的结果，因而无法相互比较验证。并行程序的这一特点，使得无法使用通过运行测试来保证程序的正确性,给并行调试工具的开发带来相当困难。特别是并行调试工具还会带来所谓探针效应(ProbeEffect)，即调试工具本身的引入，可能掩盖了被调试程序中的时序错误。例如，当人们想通过输出某些运行轨迹来定位错误而加人了这些用来输出轨迹信息的测试指令时，可能改变了原指令的执行次序,从而使错误被屏蔽而不再出现。

导致并行程序产生不确定性的主要原因是：①共享变量竞争：在共享存储的多处理机系统中,通过读和写共享变量实现通信。当缺少必要的同步操作时，可能造成数据的不正确读出或写人；②发收消息竞争：在分布存储的多计算机上，通过发送和接收消息实现通信。但由于消息在行进中的遭遇不同，使得一个处理机所收到的消息次序，可能在每次程序执行中都不一样；③动态进程调度：在并行机上为了负载平衡常使用动态调度，当同步使用不当时，可能使程序在某种调度次序下正确，而在另一种调度次序下出错；④不确定的系统调用：当程序与其执行环境交互时可能引起不确定的行为；③交错的消息发送：当多个源进程向一个目的进程发送消息时，一个目的进程意外接收的消息可能妨碍了它接收真正需要的消息。

一般而言，分布式系统比共享系统中出现并行程序的不确定性更大，也更难测试。下面我们简要介绍三种常用的调试技术：断点调试、事件分析和静态分析。

断点调试(Break-PointDebugging）并行断点调试是串行断点调试方法在并行系统中的扩展。它是将多个串行断点组合在一起，每个并行任务使用一个串行断点进行调试，配合使用多窗口技术,使各个任务对应在各自的窗口中。目前已有不少商品化的调试器,其代表者有 Sequent的pdbx和Cray的mtdbx等；其断点的种类也很多：它可以是基于控制流的断点，即在源程序语句处中止程序的执行；也可以是基于事件的断点(俗称的自陷),即当例外或用户自定义的事件或访问某个变量时中止程序的执行；也可以是基于谓词的断点，即当某个条件表达式满足时中止程序的执行。

在并行环境中，断点尚有局部和全局之分：前者只中止碰到断点的任务；后者则中止并行程序中的所有任务，如果不能中止所有的任务，则有可能造成某个任务修改了它的状态，此时全局断点后所观察到的状态就不是断点发生时的状态。一般而言，全局断点的实现应有硬件直接支持。

断点调试方法的最大缺陷是探针效应，它使得无法处理时序性错误。但是，因为探针效应不会掩盖并行程序中的非时序性错误，以及当断点引人的延迟足够小时，诱发探针效应的机会也很少，所以尽管存在探针效应，它仍能在一定程度上支持并行调试。

事件分析(EventAnalysis）事件分析方法就是记录程序运行中的事件发生的有关信息,事后加以分析以帮助发现错误,系由两部分组成：一是程序运行时的事件信息记录部分；二是程序终止后的事件信息分析部分。所要记录的信息是事件分析所需要的。目前也有些商品化的此类调试器,其代表者有Cray 的GMAT和 BBN Butterfly 的 Instant。

此类调试方法所记录的事件轨迹信息主要用于阅览和重放：前者是通过对事件信息的整理,帮助用户查看有助于发现错误的有兴趣的信息,通常多窗口图形显示技术是不可少的，GMAT就属此类;后者是利用事件轨迹信息来控制程序的再执行，以重现程序的运行结果,Instant就属此类。

重放(Replay）在分布式多机系统上实现较多,其原因是重放要求记录下任务间所有同步通信的信息。而在分布式多机系统中，一般是采用消息传递同步通信的办法。同步通信和计算是分开的，所有的同步通信都必须使用通信原语指定消息收发的双方。这样在消息传递系统中，何时产生通信以及谁参与通信都很清楚，因而有关同步通信的信息就比较少，只要记录下这些少量的信息，在重放时控制程序再现这些同步通信的次序就可重放程序的运行结果。但在共享存储的多处理机系统中，同步通信和计算是分不开的，赋值和变量引用可以视为消息的发送和接收。这样每个共享存储单元的访问就可能是一次处理器间的同步通信。为了重放程序的执行，就必须记录下所有共享存储单元的访问次序，因而信息量极大。所以目前的程序重放在共享存储的多处理机系统中实现较少。

值得注意的是：即使在消息传递机制下，记录所有同步通信信息仍然是调试时的主要开销;事件分析方法尚需要硬件的支持；同样也存在着探针效应，不管其对性能影响大小如何。

静态分析(StaticAnalysis）静态分析技术目前还处于研究阶段，是在相关分析的基础上发展起来的，用来识别那些未由同步保证的任务间语句的相关性，可有效解决并行程序不确定性所引起的困难。使用静态分析工具自动检测并行程序中导致结果不确定的数据竞争，分析其产生的原因,针对性地修改程序,消除竞争,从而排除程序中的时序性错误;在此基础上,就可使用断点调试法来排除程序中的非时序性错误。但现阶段静态分析方法的计算时空量极大，限制了它能处理的程序规模;同时该方法对数据竞争的识别是保守的,可能会误判一些实际上不存在的数据竞争。所以它处理实际的并行程序的能力还有待于进一步完善。

并行程序的调试步骤并行程序的调试是复杂困难的，一般的方法和步骤为：①如果一个并行程序系由串行程序改写的，则首先应确保原串行程序运行是正确的；②如果并行机制支持单机运行并行程序，则首先应在较简单的运行环境下,尝试用单机执行并行程序,以确信并行程序的基本正确性；③如果并行程序允许处理器数目的变化,那么在单机运行正确的基础上可以逐步增加执行并行程序的处理器数以充分证实并行程序的正确性；④逐步增加并行程序中的并行成分以进一步对并行程序进行性能调试。当调试中出错时：①首先检查程序数据特性(共享或局部)定义是否正确；②在分布存储的系统上数据是分布在局存中的,当出错时应检查数据的分布是否正确;③检查数据相关或控制相关所造成的程序执行流向的可能错误；④检查同步机制是否错用或漏用同步信号使得某些相关不能满足而引起结果的不确定性，经验证明同步通信错误是较多的和难查的；③当出现固定错误时应多检查数据定义特性、依赖关系等方面；当出现不固定的错误时则应多检查同步通信等操作。

# 15.3.2并行程序的性能分析

并行程序的性能分析工具主要用来分析并行程序的性能，指导程序的优化；提供性能参数，改进系统的设计。性能分析工具一般分为静态和动态两种：前者采用模拟或分析方法获取源程序中的有关性能数据报告给用户；后者采用测量的方法收集程序运行中的各种性能数据，即时或事后报告给用户。动态性能分析所提供的数据比较准确,但灵活性较差,常随算法、问题规模、处理器数、输人数据集合以及具体的并行系统等而变化;静态性能分析能够针对不同的程序和运行环境给出性能预测，但预测的准确性却有待提高。

静态性能分析(Static Performance Analysis）静态性能分析也称为性能预测,是在源程序一级进行的。它可以是一个由用户调用的工具,也可能是一个由编译器调用的工具,编译器调用一般是为了某种优化作出决策。因为静态性能分析的方法是用模拟分析的方法实现的，而不真正地运行程序，所以只能对占用时间较多的重要的程序结构(例如循环和子程序调用等)进行分析。静态确定程序的运行轨迹一般是困难的，所以就此意义而言静态分析是一种试探性的方法。

静态性能分析所采用的体系结构模型一般是比较抽象的，忽略的一些细节常会对真实的性能有较大的影响，正是因为如此，静态性能分析的准确性是不理想的,但从现有的静态工具使用的情况来看，在大多数情况下还是能有效地指导程序优化的。静态性能预测的最大好处是可以用较小的时间代价，针对重要的程序结构，作出多种可能的性能选择。

动态性能分析(Dynamic Performance Analysis） 动态性能分析所获取的数据可由支持硬件提供,也可完全由软件的办法得到，当然硬件性能监测器也能同时收集软件所提供的信息。但硬件性能监测器可以提供很多对性能分析有很大帮助的有关机器CPU性能的参数，诸如功能部件的忙闲情况、各处理器间的通信模式、访存冲突率、Cache命中率、指令流出受阻率、同步通信频度、各类指令数等。不过这些性能参数几乎全是基于CPU的,对系统级或任务级的性能参数提供较少,所以硬件监测器在此方面的功能尚需进一步加强,同时分布存储系统除少数(如 Intel的Paragon)外一般都没有硬件监测器,这可能是因为在此类系统上,系统互连网络的性能更为关键,而CPU的性能主要由微处理器芯片所决定。

用软件的办法提供动态性能信息系由操作系统和并行运行支持系统完成，它们大都在完成其正常的功能外,还提供事件信息记录的功能。通过这些信息用户可以了解并行程序的有关性能，诸如并行度、负载平衡、等待时间等,进而可以帮助用户改进任务划分、同步互斥的组织等。但这些信息的记录都存在所谓“侵人性”,即信息记录的引人,或多或少会干扰程序的正常执行，加长程序的执行时间，甚至可能使所记录的信息不能正确反映程序的运行状态。此外，记录下来的信息太多，使得用户难以发现所感兴趣的有意义的信息。缓解此问题的办法有二：一是选择性地记录有关事件的轨迹信息;二是提供强有力的事件浏览手段。

动态性能分析工具又可分为联机的和脱机的：前者的信息记录部分和分析显示部分是同时工作的，记录的信息立即送给分析显示部分去分析，并将结果报告给用户；后者在程序运行时记录下有关信息，然后在运行中止后再进行分析并报告给用户。联机方式的优点是可及时反映程序的运行状态；缺点是信息量较小和分析程序较弱。脱机方式的优点是可提供较大的信息量和分析较准确；缺点是程序死锁时就得不到数据,不能及时反映运行状态。

并行程序的性能分析方法如何分析并行程序的性能虽无定规可循，但下述方法可供参考：①统计程序各部分执行时间,将性能分析的重点放在占时间较多的那些部分上;②分析计算量大的程序段中是计算部分、还是通信部分、还是I/O部分，从而找出并行程序的性能瓶颈;③对照理论计算的加速比和实际测量的加速比之差异,仔细分析所设计的并行程序的并行粒度是否合适、负载是否平衡、通信开销是否过大、存储访问冲突是否严重、Cache命中率是否不佳或cache颠簸现象过于明显等； $\textcircled{4}$ 从分析程序的效率和可扩放性出发，分析体系结构和算法的组合、问题尺寸和系统规模之间的比例关系等。

# 15.3.3并行程序的可视化设计环境与工具

20多年来，串行程序的设计经过结构化、过程化、面向对象技术、CASE技术、组件技术和可视化编程技术等的应用，大大提高了串行软件的开发效率。面对并行程序开发困难的局面，长期来，从事并行程序设计的人员也作了大量工作,试图将串行程序的这些有效技术引入到并行程序设计中来,并且也已开发出了一些试验性的可视并行程序设计语言和环境,包括HENCE、CODE、PSEE、Paralex、TRAPPER和GRADE等。它们的思路基本相同,都是用节点表示计算,用弧表示节点间的交互,通过一个可视的集成开发环境,采用统一的图形用户界面,将并行程序的设计、编辑、编译连接、调试和性能分析等工具集成起来，力图实现并行程序开发各个阶段的可视化。当前可视化的并行软件设计工具的趋势是,在一个图形的集成环境里,支持并行软件开发的全过程。一个典型的这样的工具集至少应包括三个主要的工具：一个可视化的程序设计工具,一个可视化的模拟系统和一个可视的程序正确性调试和行为分析工具。可视的程序设计工具和行为分析工具应该并存在同一个环境中，允许有关程序行为的信息与其设计联系起来。而目前许多现有的工具集只包含这些工具的一个子集,可视化性能分析工具通常作为一个单独的工具。

作为例子,下面给出一个使用图形应用开发环境GRADE(GRaphical Appli-cationDevelopmentEnvironment）开发并行程序的过程。它目前的组成为： $\textcircled{1}$ GRED:一个图形的并行程序编辑器，它支持图形编程语言GRAPNEL; $\textcircled{2}$ GRP2C:一个预编译器，它将图形语言程序转换成C语言和PVM函数调用的程序； $\textcircled{3} \mathrm {{ D D B G } }$ ：一个分布式调试工具； $\textcircled{4}$ Tape/PVM:一个监视工具,它在PVM程序执行期间生成跟踪文件(Trace File); $\textcircled{5}$ PROVE:一个可视化的工具,用于分析和解释Tape/PVM跟踪文件信息,并用图形方式表示出来。GRADE开发并行程序的流程如图15.7所示(其中矩形框代表不同的工具，椭圆框内是系统使用的数据文件,圆角方框表示对象库)： $\textcircled{1}$ 用户使用GRED图形语言编辑器设计和构造用图形编程语言GRAPNEL书写的并行程序; $\textcircled{2}$ 用GRP2C预编译器产生一个C/PVM源程序、一个MakeFile工程文件和一个支持图形化调试和程序行为动画显示的交叉引用文件; $\textcircled{3}$ 由生成器分别连接三个不同的库(GRAPNEL库：在GRAPNEL语言层隐藏PVM细节;PVM库:实现进程间和处理器间的通信;Tape/PVM库：为运行时监视和事件跟踪收集有关PVM调用的信息)生成可执行文件; $\textcircled{4}$ 可执行代码以调试(查错)模式或跟踪模式加载到处理器上执行：

在调试模式下,DDBG通过生成断点、单步执行和动画等指令控制程序的执行；在跟踪模式下，产生包含所有用户定义的跟踪信息的跟踪文件，这些事件通过PROVE可视化工具,为用户指出在GRAPNEL程序中的性能瓶颈。

GRADE打算作成一个复杂的程序设计环境，在此环境下用户可以用高层工具和抽象机制来开发并行程序,无需关心消息传递原语的低层细节。所有的通信原语可以用图形的方式定义,程序员在同一个图形用户界面下即可完成程序的设计，调试和性能调整。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0006_pages_0351-0420/auto/images/00394bd73df6754f443d851147cc6669b558cdd473262d7d2ec5e3d0d1f75866.jpg)  
图15.7GRADE开发并行程序的流程

# 15.4 小结和导读

小结并行程序的编制、调试和性能分析是比较复杂和困难的，人们需要不同的工具来帮助程序员或用户减轻这些困难和提高程序生产率;需要一个较完善的和良好的程序设计环境来帮助调试程序、监视程序的运行和分析程序的性能。将来的工具环境应该是一个集成化的开放式的人机交互方式更为自然和谐

的环境。

本章除了概括性地介绍了一下软件工具（它包含了并行程序设计工具中的编辑、编译、连接、预处理、查错等编码工具,系统维护工具以及先进的集成工具)外，重点讨论了语言编译器。并行编译系统的技术难点是如何自动识别用户源程序中的可并行执行部分并将其并行化,其工作流程是：根据相关理论,把顺序程序转换为程序流图;将此进程流程图划分成若干并行模块;用分布式并行语言描述并行执行模块,并与系统结构相匹配；重新编译，生成可执行的目标代码。本章还对并行程序的调试和性能分析作了简要讨论。从本质上讲，调试是从并行程序执行错误的现象出发,通过某种手段找出错误代码的位置,就地改正，以获得一个正确的并行程序;性能分析以改善并行程序的性能为出发点，帮助用户发现和消除性能瓶颈，以获得一个高效的优化程序。本章最后对并行程序设计的可视化环境与工具作了简单介绍,并以GRADE为例,描述了如何用图形应用开发环境开发一个并行程序。

导读关于软件工具与环境的概述,读者可阅读[145]。Emacs编辑器描述在[79]中,SADT描述在[150]中,OMT描述在[151]中,PCTE标准描述在[37]中。关于编译原理、技术和工具,读者可阅读[8];并行编译的论述,读者可阅读[184];有关相关性分析,读者可阅读[195]和[100];关于相关测试中GCD测试读者可参阅[184],Banerjee不等式测试读者可参阅[24];有关AlliantFX/80多处理机介绍,读者可参考[10]。关于并行程序的测试和性能分析,读者可阅读[195]、[39]、[146]、[48]。关于并行程序设计语言与工具,读者可阅读[47]。关于可视化的并行程序设计环境与工具,读者可参阅[27]、[130]、[122]、[21][153]和[107]。

# 习 题

15.1分析下列代码段中三条语句间的相关关系;给出相应的相关方向向量和相关距离向量：

D0 $\mathbf { I } { = } 1 , \mathbf { N }$ DO $J { = } 2 , \Nu$ $\mathbf { S } _ { 1 }$ ： $\mathrm { \bf A } ( \mathrm { \bf I } , \mathrm { \bf J } ) = \mathrm { \bf A } ( \mathrm { \bf I } , \mathrm { \bf J } - \mathrm { \bf 1 } ) + \mathrm { \bf B } ( \mathrm { \bf I } , \mathrm { \bf J } )$ $\mathsf { S } _ { 2 }$ ： $\mathrm { C } ( \mathrm { I } , \mathrm { J } ) { = } \mathrm { A } ( \mathrm { I } , \mathrm { J } ) + \mathrm { D } ( \mathrm { I } + 1 , \mathrm { J } )$ S: $\mathbf { D ( \boldsymbol { I } , \boldsymbol { J } ) = 0 . 1 }$ ENDDOENDDO

15.2判定下列的循环,哪些是可向量化的：

$\textcircled{1}$ D0 $\mathbf { I } = 1 , \mathsf { N }$

S: A(I)=B(I)S: $\mathrm { C ( I ) } = \mathrm { A ( I ) } + \mathrm { B ( I ) }$ S: $\operatorname { E } ( \operatorname { I } ) = \operatorname { C } ( \operatorname { I } + 1 )$ ENDDO  
② DO I=1,N$\mathsf { S } _ { 1 }$ ： $\mathrm { A } ( \mathrm { I } ) = \mathrm { B } ( \mathrm { I } ) + \mathrm { C } ( \mathrm { I } + 1 )$ ${ \bf S } _ { 2 }$ ： $\mathrm { C } ( \mathrm { I } ) = \mathrm { A } ( \mathrm { I } ) \star \mathrm { D } ( \mathrm { I } )$ ENDDO  
$\textcircled{3}$ DO ${ \bf { I } } = { \bf { 1 } } , { \bf { N } }$ S: $\mathbf { A ( I ) } = \mathbf { A ( I - 1 ) } + \mathbf { 1 }$ ENDDO  
$\textcircled{4}$ DO $\mathbf { I } { = } 1 , \mathbf { N }$ S: $\mathbf { A ( I ) } = \mathbf { A ( I + 1 ) } + \mathbf { 1 }$ ENDDO  
$\textcircled{5}$ DO ${ \bf I } = 2 , { \bf N }$ D0 $\mathbf { J } { = } 2 , \mathbf { M }$ $\mathbf { A ( I , J ) } = \mathbf { A ( I , J - 1 ) } + 1$ ENDDOENDDO

15.3试述向量化下列代码段：

$\textcircled{1}$ DIMENSION A(200,200),B(200,200),C(200,200) DO $_ { 1 } = 1 , 2 0 0$ DO ${ \bf J } = 1 , 2 0 0$ $\mathrm { A ( I , J ) = B ( I , J ) * C ( I , J ) }$ ENDDO ENDDO

$\textcircled{2}$ DO ${ \bf I } = { \bf 1 } , { \bf 1 0 0 }$ $\mathbf { C ( \mathbf { I } ) = 0 . 0 }$ DO J= 1,100 $\mathrm { C } ( \mathrm { I } ) = \mathrm { C } ( \mathrm { I } ) + \mathrm { A } ( \mathrm { I } , \mathrm { J } ) * \mathrm { B } ( \mathrm { J } )$ ENDDO ENDDO

$\textcircled{3}$ D0 $\mathbf { I } { = } 1 , \mathbf { N }$ $\mathrm { B } ( \mathrm { I } , 1 ) = 0$ D0 $J { = } 1 , M$ $\mathrm { A ( I ) = A ( I ) + B ( I , J ) * C ( I , J ) }$ ENDDO $\mathrm { D } ( \mathbf { I } ) = \mathbf { E } ( \mathbf { I } ) + \mathbf { A } ( \mathbf { I } )$

# ENDDO

④ DO $\mathbf { I } = 2 , \mathbf { N }$ $\mathsf { S } _ { 1 }$ ： $\mathrm { T } ( \mathbf { I } ) = \mathbf { A } ( \mathrm { I } - \mathbf { 1 } ) + \mathbf { A } ( \mathrm { I } + \mathbf { 1 } )$ S: $\mathrm { A ( I ) } = \mathrm { B ( I ) } + \mathrm { C ( I ) }$ END

15.4分析下列循环，哪些是可并行化的：

$\textcircled{1}$ DO ${ \bf I } = 2 , { \bf N }$ $\mathrm { A } ( \mathrm { I } ) = \mathrm { B } ( \mathrm { I } ) - \mathrm { A } ( \mathrm { I } - 1 )$ ENDDO   
$\textcircled{2}$ DO $\mathtt { I } = 2 , \mathtt { N } , 2$ $\mathrm { A } ( \mathrm { I } ) = \mathrm { B } ( \mathrm { I } ) - \mathrm { A } ( \mathrm { I } - 1 )$ ENDDO   
$\textcircled{3}$ DO $\mathbf { I } { = } 1 , \mathbf { N }$ $\mathbf { X } { = } \mathbf { S Q R T } ( \mathbf { A ( I ) } )$ $\mathrm { B } ( \mathrm { I } ) = \mathbf { X } * \mathbf { C } ( \mathrm { I } ) + \mathbf { X } * \mathbf { D } ( \mathrm { I } )$ ENDDO   
$\textcircled{4}$ $\mathbf { I N D X } { = } \mathbf { 0 }$ DO $\mathbf { I } = \mathbf { A } , \mathbf { N }$ $\mathrm { I N D X } { = } \mathrm { I N D X } + 1$ $\mathrm { A } ( \mathrm { I } ) = \mathrm { B } ( \mathrm { I } ) + \mathrm { C } ( \mathrm { I N D X } )$ ENDDO   
$\textcircled{5}$ DO $\mathbf { I } { = } 1 , \mathbf { N }$ IF(A(I ) ·LT·EPSILON)GOTO 320 $\mathbf { A ( I ) } = \mathbf { A ( I ) } * \mathbf { B ( I ) }$ ENDDO 320 CONTINUE

15.5分析下列循环的语句数据相关性;如何进行循环调度并行化：

D0 $\mathbf { I } { = } 1 , \mathbf { N }$ DO $J { = } 2 , \Nu$   
$\mathsf { S } _ { \mathsf { I } }$ ： $\begin{array} { r l } & { \mathrm { \cal { A } ( I , J ) = \mathrm { \cal { B } ( I , J ) + C ( I , J ) } } } \\ & { \mathrm { \cal { C } ( I , J ) = \mathrm { \cal { D } ( I , J ) } } / 2 } \\ & { \mathrm { \cal { E } ( I , J ) = \mathrm { \cal { A } ( I , J - 1 ) } * \ x \ 2 + \mathrm { \cal { E } ( I , J - 1 ) } } } \end{array}$   
$\mathsf { S } _ { 2 }$ ：   
$\mathsf { S } _ { 3 }$ ： ENDDO ENDDO

# 算法索引

算法4.1 共享存储多处理器上求和算法 110  
算法4.2 分布存储多计算机上矩阵向量乘算法 111  
算法4.3 PRAM-EREW上累加求和算法 125  
算法4.4 APRAM上求和算法 125  
算法4.5 BSP上求和算法 126  
算法5.1 SISD上快排序算法 130  
算法5.2 PRAM-CRCW上为快排序构造二叉树算法 131  
算法5.3 失效函数的计算算法 134  
算法5.4 KMP串匹配算法 135  
算法5.5 SIMD-CC上求所有点对间最短路径算法 139  
算法5.6 超立方上快排序算法 142  
算法5.7 计算串匹配的 $\operatorname { d } { \mathrm { u e l } } ( \phi , q )$ 的算法 142  
算法6.1 MIMD机器上PSRS排序算法 144  
算法6.2 SIMD-EREW上Valiant归并算法 146  
算法6.3 PRAM上对数划分算法 147  
算法6.4 $( m , n )$ -选择网络算法 148  
算法6.5 Batcher双调归并算法 150  
算法6.6 PRAM上求上凸壳算法 152  
算法6.7 PRAM上求凸壳算法 152  
算法6.8 SIMD-TC上求最大值算法 153  
算法6.9 SIMD-TC上非递归求前缀和算法 154  
算法6.10 SIMD-EREW上求元素表序算法 155  
算法6.11 SIMD-CREW上求森林根的算法 157  
算法6.12 PRAM-CREW上Hirschberg求连通分量算法 163  
算法7.1 SISD上组合搜索算法 179  
算法7.2 SISD上分治(D&C)算法 179  
算法8.1 二维网孔上的X-Y选路算法 185  
算法8.2 超立方网络上的E-立方选路算法 186  
算法8.3 $^ { d }$ 维超立方上前缀和算法 199  
算法9.1 单处理机上矩阵转置算法 205  
算法9.2 单处理机上矩阵-向量乘算法 209  
算法9.3 单处理机上矩阵相乘算法 213  
算法9.4 单处理机上分块矩阵相乘算法 214  
算法9.5 Cannon分块乘法算法 216  
算法9.6 DNS乘法算法 221  
算法9.7 PRAM-CREW上矩阵相乘算法 225  
算法9.8 SIMD-MC²上Systolic矩阵相乘算法 225  
算法10.1 SISD上回代求解上三角方程组算法 229  
算法10.2 UMA上回代求解上三角方程组算法 230  
算法10.3 SISD上直接求解三对角方程组算法 231  
算法10.4 .SISD上求解稠密线性方程组高斯主元消去算法 234  
算法10.5 超立方多计算机上求解稠密线性方程组高斯主元消去算法 236  
算法10.6 PRAM上求解稠密线性方程组高斯-约旦消去算法 238  
算法10.7 SISD上求解线性方程组高斯－赛德尔迭代算法 240  
算法10.8 SISD上求解线性方程组雅可比迭代算法 244  
算法10.9 SISD上求解拉普拉斯方程雅可比迭代算法 246  
算法10.10 SISD上求解 $\mathbf { A } \mathbf { x } = \mathbf { b }$ 共轭梯度算法 254  
算法10.11 SISD上三对角方程组奇偶归约求解算法 257  
算法11.1 SISD上FFT迭代算法 266  
算法11.2 SISD上FFT递归算法 268  
算法11.3 SIMD-MC上FFT算法 270  
算法11.4 SIMD-BF上FFT算法 272  
算法11.5 SISD上Cormen 迭代计算FFT算法 275  
算法11.6 超立方上FFT算法 276  
算法11.7 SISD上Cormen 计算FFT算法 280

# 表格索引

表1.1 美国HPCC计划公布的重大挑战性应用课题一览表 5  
表1.2 美国ASCI计划中的并行机一览表 7  
表1.3 OptionRed系统硬件参数一览表 8  
表1.4 静态互连网络特性一览表 13  
表1.5 动态互连网络特性一览表 16  
表1.6 三代以太网特性一览表 18  
表1.7 ATM与OSI标准对应关系一览表 20  
表1.8 5种结构特性一览表 24  
表1.9 计算机科学中常用千进制单位量词一览表 33  
表2.1 5种商用SMP系统特性比较一览表 40  
表2.2 Origin2000结构配置属性一览表 41  
表2.3 Origin 2000不同层次存储器读延迟一览表 46  
表2.4 Origin 2000 带宽(GB/s)和延迟(ns)一览表 46  
表2.5 4种CC-NUMA结构比较一览表 47  
表2.6 典型MPP系统特性比较一览表 49  
表2.7 MPP所用的高性能CPU特性参数一览表 50  
表2.8 ASCI计划的3个高端MPP系统特性一览表 51  
表2.9 典型的机群系统特点一览表 61  
表2.10 20 世纪90年代我国自行研制的几种并行机一览表 68  
表2.11 曙光-1000与某些著名MPP系统性能比较一览表 75  
表2.12 SMP、MPP、COW性能比较一览表 81  
表3.1 处理器数及其相应执行时间一览表 94  
表3.2 $\Psi \big ( \pmb { \phi } , \pmb { \phi } ^ { \prime } \big )$ 一览表 94  
表3.3 $\Psi \big ( \pmb { \phi } , \pmb { \phi } ^ { \prime } \big )$ 上三角阵 95  
表3.4 $\Phi ( 0 , 2 5 , \phi , \phi ^ { \prime } )$ 上三角阵 97  
表4.1 机器的平均距离和对剖宽度一览表 119  
表4.2 $\mathbf { P } _ { i }$ 发送 $L _ { i , j }$ 个字节给 $\mathbf { P } _ { j }$ 时发送和接收时间一览表 120  
表4.3 一个超级步中的处理器发送和接收时间一览表 120  
表4.4 非阻塞发送和接收虫蚀式选路的通信单位数一览表 121  
表4.5 并行计算模型综合比较一览表 124  
表8.1 通信时间汇总一览表(使用CT方式) 196  
表12.1 串行程序设计和并行程序设计比较一览表 284  
表12.2 三种并行编程方法比较一览表 287  
表13.1 三种显式并行程序设计模型主要特性一览表 317  
表13.2 四种并行程序设计模型比较一览表 318  
表13.3 Pthreads中基本线程管理原语一览表 322  
表13.4 Pthreads中线程相互作用原语一览表 323  
表13.5 五种并行编程标准比较一览表 324  
表13.6 X3H5与OpenMP主要性能比较一览表 325  
表14.1 MPI中的数据类型一览表 338

# 示范程序索引

$/ / \star$ 用BSPLib求前缀和 $\yen 7/$ 128  
$/ / \varkappa$ 用UDP实现域名服务器代码段 $\pmb { \mathscr { k } }$ // 304  
$/ / \ast$ 用TCP实现域名服务器代码段 $\divideontimes$ // 305  
$/ / \ast$ 计算 $\pmb { \pi } \mathbf { C }$ 语言编程代码段 $\divideontimes$ // 311  
$\nearrow \nearrow$ 计算 $\pmb { \pi }$ 数据并行编程代码段 $\pmb { \mathscr { k } }$ // 314  
$/ \nearrow$ 计算 $\pmb { \pi }$ 消息传递编程代码段 $\pmb { \mathscr { k } }$ // 315  
$/ / \ast$ 计算 $\pmb { \pi }$ 共享变量编程代码段 $\star$ /1 317  
$\nearrow$ 计算 $\pmb { \pi }$ OpenMP编程代码段 $\star$ // 325  
$/ / \ast$ 计算 $\pmb { \pi }$ Pthreads编程代码段 $\star$ // 328  
$/ / \ast$ 计算 $\pmb { \pi }$ Fortran语言SPMD编程代码段 $\yen 7/$ 329  
$/ \nearrow \ *$ 求解N-皇后经理-员工编程代码段 $\pmb { \mathscr { k } }$ // 330  
$/ / \ast$ 计算 $\pmb { \pi } \mathbf { C }$ 语言MPI编程代码段 $\bigstar$ // 346  
$/ / \ast$ 计算 $\pmb { \pi } \mathbf { C }$ 语言PVM编程代码段 $\yen 74$ 351  
$\nearrow$ 高斯消去法的HPF编程代码段 $\star$ // 360  
$/ / * \mathsf { P V M }$ 主机/节点编程的hello代码段 $\yen 74$ 363  
$/ / \ast$ 高斯消去法的Fortran90编程代码段 $\yen 74$ 364  
$/ / \ast$ 雅可比松弛法的Fortran90编程代码段 $\star$ / 365  
$/ / \ast$ 雅可比松弛法的MPI编程代码段 $\star$ // 365  
$/ \nearrow \ *$ 计算 $\pmb { \pi }$ Fortran90编程代码段 $\bigstar$ // 366

# 参考文献

1Adams J et al.The Fortran 90 Handbook.McGraw-Hill,1992   
2Adams J et al.The Fortran 95 Handbook.MIT Press,1997   
3Adve S V,Hill M D,Vernon M.Comparison of Hardware and Software Cache and Cohercnce Schemes.Proc.18th Annu.Int.Symp.Computer Arch.,1991,298～308   
4 Agerwala T,Martin J L,Mirza J H,et al. SP2 System Architecture. IBM Systems Jourmal, 1995,34(2):152\~184   
5 Aggarwal A et al. Communication Complexity of PRAMs. Theoretical Computer Science,1990, 3:3\~28   
6 Agha G,Concurrent Object-Oriented Programming. Comm.of the ACM,1990,33(9):125\~ 141   
7Aho A,Hopcroft J,Ullman J. The Design and Analysis of Computer Algorithms. Addison-Wesley,1974   
8 Aho A V,Sethi R,Ulman J D.Compilers:Principles,Techniques,and Tools. Adison-Wesley, 1986   
9 Allan S J,Oldehoeft R,HEP SISAL: Paralel Functional Programming. Kowalik(Ed). Paralel MIMD Computation: HEP Supercomputers and Applications.MIT Press,1985   
10 Alliant. Alliant Product Summary. Alliant Computer Systems Corporation,1989   
11 Alpern B et al.The Uniform Memory Hierarchy Model of Computation.Algorithmic,1993   
12 Amdahl G M. Validity of Single-Processor Approach to Achieving Large-Scale Computing Capability. Proc.AFIPS Conf.，1967,483～ 485   
13Amza C et al. Treadmarks: Shared Memory Computing on Networks of Workstations. IEEE Computer,1996,29(2):18～28   
14 Anderson E et al. LAPACK User's Guide.SIAM,1992   
15 Anderson T E et al. A Case for NOW(Networks of Workstations). IEEE,Micro,1995,2:54～64   
16 ANSI Technical Committee X3H5. Parallel Processing Model for High-level Programming Languages,1993   
17 Accelerated Strategic Computing Initiative( ASCI) Program. A Report by US Department of Energy,Lawrence Livermore National Lab.，Los Alamos National Lab.，Sandia National Lab.,1996   
18 3ATM Forum.ATM User Network Interface: Version UNI3.1 Specification,1994   
19 Averbuch A,Gabber E,Gordissky B et al.A Parallel FFT on an MIMD Machine. Parallel Computing,1991,15:61～74   
20Baase S,Computer Algorithms: Introduction to Design and Analysis. Addison-Wesley,1978 21 Babaoglu Oet al. Paralex: An Environment for Paralel Programming in Distributed Systems. Proc.of ACM Int'1 Conf .on Supercomputing,1992   
22 Bailey D H et al. The NAS Paralel Benchmarks 2.0. NASA Ames Research Center Report, 1995,12: NAS-95-020   
23 Bal HE,Steiner JG,Tanenbaum A S.Programming Languages for Distributed Computing Systems. ACM Computing Surveys,1989,21(3):261～322   
24 Banerjee U.Dependence Analysis for Supercomputing.Boston: Kluwer Academic Press,1988   
25 Banerjee U. Dependence Analysis.Boston: Kluwer Academic Publishers,1996   
26 Batcher K E.Sorting Networks and Their Applications. AFIPS Proc.1968,307～314   
27 Beguelin A et al. Visualization and Debugging in a Heterogeneous Environment. IEEE Computers,1993,26(6)   
28 Berger M,Bokhair S.A Partitioning Strategy for Nonuniform Problems on Multiprocessors, IEEEXTran. Computs.,1987,C-36(5):570～580   
29 Berman F,Snyder L.On Mapping Parallel Algorithms into Parallel Architectures. Parallel J& Distributed Computing,1987,4(5):439～458   
30 Bermtsen J. Communication Effcient Matrix Multiplication on Hypercubes.Parallel Computing,1989,12:335～342   
31 Bertsekas D P and Tsitsilklis JN.Paralel and Distributed Computation: Numerical Methods. Prentice-Hall,1989   
32 Blume W,Eigenmann R.Performance Analysis of Paralelizing Compilers on the Perfect Benchmarks Programs. IEEE Trans.on Paralel and Distributed Systems,1992,3(6):643\~ 656   
33 Blume W et al. Automatic Detection of Parallelism: A Grand Chalenge for High-Performance Computing. IEEE Parallel and Distributed Technology,1994,2(3):37～47   
34 Blume W et al. Paralel Programming with Polaris. IEEE computer,1996,29(12):78～82   
35 Blumrich M A,Dubnicki C,Felten E W et al.Protected User-Level DMA for the SHRIMP Network Interface,Proc.2"dInt'1 Symp.on High-Performance Computer Architecture,1996   
36 Boden N J et al. Myrinet: A Gigabit-Per-Second Local Area Network. IEEE Micro.1995,2: 29\~36   
37 Boudier G et al. An Overview of PCTE $^ +$ .SIGPLAN,1982,2(24):248\~257   
38 Boyer R S,Moore J S.A Fast String Searching Algorithm. Comm.of the ACM,1997,20:762 \~772   
39 Brown J S. Debuggers for High Performance Computers,Proc.of the Superoomputing'93, 1993   
40Cannon L E.A Celular Computer to Implement the Kalman Filter Algorithm: Ph.D.thesis. Montana State Univ.,1969   
41Carriero N,Gelernter D.How to Write Parallel Programs. MIT Press,1990   
42Catlett C,Smarr.L. Metacomputing.Comm. of ACM,1992,35(6):44～52   
43Chaiken D,Fields C,Kwibara K et al. Director-Based Cache Coherence in Large-Scale Multiprocessor.IEEE Computer,1990,23(6):49～59   
44 Chan TF,Saad Y.Multigrid Algorithms on the Hypercube Multiprocessr. IEEE-TC,1986, C-35(11) :969\~977   
45 Chapman B et al.. Extending HPF for Advanced Data-Paralel Aplications. IEEE Paralel & Distributed Technology,1994,2(3):15～27   
46 Cheatham T,Fahmy A,Stefanescu D C et al.Bulk Synchronous Parallel ComputingA Paradigm for Transportable Software. Proc. of $2 8 ^ { \mathrm { { t h } } }$ Hawaii Int. Conf.on System Science,1995   
47 Cheng Y. A Survey of Parallel Programming Languages and Tols. Technical Report RND-93- 005,NASA Ames Research Center,1993   
48 Cheng D,Hood R.A Portable Debugger for Paralel and Distributed Programs,Proc.of the Superoomputing'94.1994   
49 Chlebus B,Vrto I.,Parallel Quick Sort.Journal of Paralel and Distributed Computing,1991, 11:332\~337   
50 Chronopoulos A T,Gear C W. On the Efficient Implementation of Pre-condition S-step Con-jugate Gradient Methods on Multiprocessors with Memory Hierarchy. Parallel Computing, 1989,11:37\~53   
51 Cole R, Vishkin U. Approximate Coin Tossing with Application's to List, Tree,and Graph Problems,Proc. 27hannu. IEEE Symposium on FOCS(Foundations of Computer Science), IEEE press1986,478～491   
52 Comer D E. Intermetworking with TCP/IP. $3 ^ { \alpha }$ Ed. Prentice-Hall,995   
53 Cooley JW,Tukey T W.An Algorithm for the Machine Calculation of Complex Fourier Series. Mathenatics of computation,1965,19(90):297～301   
54 Cormen T H,Leiserson C E,Rivest R L. Introduction to Algorithms.MIT Press,1990   
55 Culler D,Karp R,Patterson D,et al.LogP:Towards a Realistic Model of Paralel Computation.Proc.of 4th Symp. on Principles & Practice of Paralll Programming,ACM SIGPLAN, 1993,1\~12   
56 Cybenko G.Dynamic Load Balancing for Distributed Memory Multiprocessors.Parallel J& Distributed Computing,1989,7:279～301   
57 DeFanti T et al. Overview of the I-WAY: Wide Area Visual Supercomputing. Int'1 J.of Supercomputer Applications,1996,10(2)   
58 Dekel E,Nassimi D,Sahni S. Paralel Matrix and Graph Algorithms.SIAM J.on Computing, 1981,10:657\~673   
59 Dijkstra E D,Seijen W H,Gasteren A J M V. Derivation of a Termination Detection Algorithm for a Distributed Computation.Info.Proc.Lett.,1983,16(5):217～219   
501 Dincer K,FoxG C.Building a World-Wide Virtual Machine Based on Web and HPCC Technologies. Supercomputing'96 Conference Proceedings,1996


<!-- chunk 0007: pages 421-451 -->
61 Dongarra J J et al.LINPACK User's Guide.SIAM.1979   
62Duato J,Yalamanchili S,Ni L,Interconnection Networks: An Engineering Approach. IEEE Computer Society Press,1997   
63 Felten E W et al.Early Experience with Message- Passing on the SHRIMP Multicomputer. Proc.of the $2 3 ^ { n d }$ Int'1 Symp.on Computer Architecture,1996   
64 Feng T Y.A Survey of Interconnection Networks.IEEE Computer,1981,14(12):12～27   
65 SFortue ,J Wylle. Paralelism in Random Access Machines.Proc.of $1 0 ^ { \mathrm { { d h } } }$ Symp. on Theory of Computing,1978,114～118   
66 Fosdick L D,Schauble C JC.Computer Performance.A Tutorial High Performance Scientific Computing.Boulder:Univ.of Colorado,1994   
67 Foster IT,Designing and Building Paralel Programs:Concepts & Tos for Parallel Software Engineering. Addison-Wesley Pub. Company,1995   
68 Fox G C,Ot S W,Hey A JG. Matrix Algorithms on Hypercube I: Matrix Multiplication. Parallel Computing,1987,4:17\~31   
69 Fox G et al.Solving Problems on Concurrent Processrs.Prentice-Hall,988   
70 Fox G et al.FORTRAN D Language Specification.Rice Univ.,1992.   
71 Williams G Fox R,Messna P.Parale Computing Works! Morgan Kaufman,1994   
72 Galil Z.Optimal Parallel Algorithms for String Matching.Info.and Control,1985,67(1～3): 144～157   
73 Galivan K A,Plemmons R J,Sameh A H. Parallel Algorithms for Dense Linear Algebra Computations. SIAM Rev.,1990,32(1):54～135   
74 Geist A et al.PVM:Paralel Virtual Machine--A User's Guide and Tutorial for Networked Parallel Computing.MIT Press,1994   
75 Gigabit Ethermet Aliance.White Paper of Gigabit Ethernet,March,1997(http://www.gigabit-ethermet. org/)   
76 Gibbons P B.A More Practical PRAM Model.Proc.of the ACM Symp. on Paralel Algorithms and Architectures, ACM,1989,158～168   
77 Goldberg A,Plotkin S,Shannon G. Paralel Symmetry-Breaking in Sparse Graphs.Proc. of $1 9 ^ { \circ { \circ } }$ Annu. ACM Symp.on Theory of Computing,1989,351～324   
78 Golub G H, Loan C V.Matrix Computations.(2rdEd). The Johns Hopkins Univ.Press,1989   
79 Gosling J. Unix Emacs. Carmegie-Mellon Computer Science Dept.,1982   
80 Goudreau M W et al.The Green BSP Library.CS-TR-95-11,Univ.of Central Florida,1995   
81 Goudreau M W et al. A Proposal for a BSP Worldwide Standard Library. http://www. bspworldwide.org/,1996   
82 Goudreau M W et al. Towards Efficiency and Portability: Programming with the BSP Model. SPAA'96,1996,1\~12   
83 Grimshaw A et al. Legion: The Next Logical Step Towards a Nationwide Virtual Computer. Tech.Report CS-94-21,Dept.of CS,Univ.of Virginia,1994 WCB/McGraw-Hill Companies,1998   
104JaJa J.An Introduction to Paralel Algorithms.Addison-Wesley Pub.Company,1992   
105Jones M,Plassmann P.Paralel Algorithms for the Adaptive Refinernent and Partitioning ol Unstructured Meshes. Proc.1994 Scalable High-Performance Computing Conf., IEEE Computer Society,1994,478～485   
106 Juurlink B H H,Wijshoff H A G.A Quantitative Comparison of Parallel Computation Mdels.SPAA'96,ACM,1996,13～24   
107 Kacsuk P et al. A Graphical Development and Debugging Environment for Paralel Programs.Parallel Computing,1997,22:1747～1770   
108 Karp R M et al.Effcient PRAM Simulation on a Distributed Memory Machine.Proc.of $2 4 ^ { \# }$ Annual ACM Symp.of the Theory of Computing,1992,318～326   
109 Kennedy K.Compiler Technology for Machine-Independent Parallel Programming. Int'1 J. of Parallel Programming,1994,22(1):79～98   
110 Knuth DE,Moris JH,PrattV B.Fast Patern Matching in String.SAM J. Computing, 1997,6(2):189\~195   
111 Koelbel C et al.The High Performance Fortran Handbook.MIT Press,1994   
112 Kumar V,Rao V N,Paralel Depth-First Search,Part II : Analysis. Int’1 J.of Paralel Programming,1987,16(6):501\~519   
113 Kumar V,Gupta A,Rao V. Scalable Load Balancing Techniques for Paralel Computers. J. Paralel & Distributed Computing,1994,22(1):60～79   
114 Kumar V,Gupta A,Gupta A et al. Introduction to Paralel Computing:Design and Analysis of Algorithms. Benjamin/Cummings Publishing Company,Inc.,1994   
115 Kung H T.Why Systolic Architectures? Computer,1982,15(1):37\~46   
116 Ladner R E,Fisher MJ. Prefix Computation.JACM,1980,27(4):831～838   
117 Laudon J,Lenoski D. The SGI Origin: A CC-NUMA Highly Scalable Server. Proc.of the $2 4 ^ { \dag \mathrm { h } }$ Int'1 Symp.Computer Architecture,1997,241～251   
118 Lauria M,Chien A.MPI-FM:High Performance MPI on Workstation Clusters.J.of Parallel and Distributed Computing,1997,40(1):4\~18   
119 Leiserson C L.Fat tree: Universal Networks for Hardware-Efficient Supercomputing. IEEE Trans. on computers,1985,C-34(10):892～901   
120 Lin F C H,Keller R M. The Graph Model Load Balancing Method. IEEE Trans. software Eng.,1987,SE-13(1):32\~38   
121 Lo V.Heuristic Algorithms for Task Assignment in Distributed Systems. IEEE Trans. Computs.,1988,C-37(11):1348\~1397   
122 Luque E et al. Overview and New Trend on PSEE.IEEE software,1992   
123 Mattson T G,Scott D,Wheat S.A Teraflops Supercomputer in 1996:The ASCI Tflops Sys-tem. Proc.of the $6 ^ { \mathrm { t h } }$ Int'1 Parallel Processing Syp.,199,8493   
124McBryan O. An Overview of Messge Passing Environments. Parallel Computing,1994,20 (4):41/\~444   
125 Mehrotra P et al. High Performanc Fortran: History,Status and Future.Paralel Computing, 1998,24:325～354   
126 Mellor-Crummey J M,Soott ML. Algorithms for Scalable Synchronization on Shared Memory Multiprocessors.ACM Trans.Computer Systems,1991,9(1):21～65   
127 Messina P,Sterling T (Eds).System Software and Tools for High Performance Computing Environment. SIAM,1993   
128 MPI Forum, MPI: A Messge Passing Interface, Proceedings of Supercomputing' 93. IEEE Computer Society,1993,878～883   
129 National Research Center for Inteligent Computing Systes.Introduction tothe Dawing-1000 Massively Parallel Processing System,1996   
130 Newton P,Browne J C.The CODE 2.0 Graphical Parallel Programming Language.Proc.of ACM Int'1 Conf on Supercomputing,1992   
131 Nicol D M,Saltz J H.An Analysis of Scater Decomposition.IEEE Trans. Computs.,1990, C-39(11):1337\~1345   
132 Nussbaumer H J.Fast Fourier Transform and Convolution Algorithms. $2 ^ { \mathbf { n d } }$ ed. Springer-Verlag,1982   
133 OpenMP Standards Board. OpenMP:A Proposed Industry Standard API for Shared Memory Programming,Oct.1997   
134 OpenMP Standards Board. OpenMP Fortran Application Program Interface Version 1. 0, Oct. 1997.   
135 Ortega JM,Voigt R G. Solution of Partial Diferential Equationson Vector and Paralel Computers.SIAM Review,1985,27(2):149～240   
136 Ortega J M. Introduction to Paralel and Vector Solution of Linear Systems.Plenum,1988   
137 Pancake C.M.Software Support for Paralel Computing: Where are We Headed? Comm.of the ACM,1991,34(11):53\~64   
138 Papadimitriou CH,Yannakakis M. Towards an Architecture-Independent Analysis of Parallel Algorithms. Proc. of $2 0 ^ { \mathrm { { d h } } }$ Annual ACM Symp.of the Theory of Computing,1998,510～ 513   
139 Parmas D,Clements P.A Rational Design Process: How and Why to Fake It. IEEE Trans. Software Eng.,1986,SE-12(2):251～257   
140 Pfister G F. In Search of Clusters.Prentice-Hall PTR,1995   
141 IEEE,POSIX P1003.4a: Threads Extension for Portable Operating Systems,IEEE,1994   
142 Pothen A,Simon H,Liou K.Partitioning Sparse Matrices with Eigenvectors of Graph.SIAM J. Math.Anal.Appl.,1990,11(3):430～452   
143Quinn M J. Parallel Computing-Inc. Theory and Practice (second edition) McGraw-Hill, 1994   
144Reinhardt’ S K,Pfile R W,Wood D A.Decoupled Hardware Support for Distributed Shared Memory. Proc.of the $2 3 ^ { \mathrm { { r d } } }$ Int'l Symp.on Computer Architecture,1996   
145 Reiss S P.Software Tools and Environments. ACM Computing Surveys,1996,28(1):281\~ 284   
146 Ries B.The Paragon Performance Monitoring Environment. Proc.of the Supercomputing' 93,1993   
147 Rinard MC,Scales DJ,Lam MS. Jade:A High-level,Machine-independent Language for Parallel Programming. IEEE Computer,1993,26(6) :28～38   
148Rokusawa K,Ichiyoshi N,Chikayama T et al.An Effcient Termination Detection and Abortion Algorithm for Distributed Processing Systems. Proc.1998 Int'1 Conf.on Parallel Processing,1988,I:18～22   
149 Romine C H,Ortega JM.Paralel Solution of Triangular Systems of Equations.Parallel Computing,1988,6:109～114   
150 Ross D T. Applications and Extensions of SADT. IEEE Computer,1985,18(4):25～35   
151 Rumbaugh Jet al.Object-Oriented Modeling and Design.Prentice-Hall,1991   
152 Sadayappan P,Ercal F.Nearest-Neighbor Mapping of Finite Element Graphs onto Processor Meshes. IEEE Trans. Computs.,1987,C-36(12):1408\~1424   
153 Scheidler C,Schafers L. TRAPPER: A Graphical Paralel Programming Environment for Industrial High Performance Applications. Proc.of PARLE’93: Parallel Architectures and Languages,1993   
154 Sedgewick R. Implementing Quicksort Programs. Communication of the ACM,1978,21 (10):847\~857   
155 Silicon Graphics:Origin 20and Origin 2000 Technical Report:Silicon Graphics Computer Systems,1997   
156 Shamos M I. Computational Geometry. PhD thesis,1978   
157 Shi HM,Schaeffer J.Parallel Sorting by Regular Sampling.J.of Paraleland Distributed Computing,1992,14(4):316～372   
158 Shiloach Y,Vishkin U.Finding the Maximum. Merging and Sorting in a Paralel Computational Model,1981,2(1):88～102   
159 Silicon Graphics. IRIS Power C User's Guide.Silicon Graphics Computer Systems,1989   
160 Simon H.Partitioning Unstructured Problems for Paralel Processing. Computing Systems in Eng.,1991,2(2/3):135\~148   
161 Singh V, Kumar V,Agha G et al.Efcient Algorithms for Paralel Sorting on Mesh Multicomputers.Intermational Jounal of Parallel Programming,1991,20(2):95～131   
162 Skillicorm D B,Hill J M D,McColl W F. Questions and Answers about BSP. TR-15-96. Oxford Univ. Computing Laboratory,1996   
163 Snir M et al. The Communication Software and Parallel Environment of the IBM SP2.IBM Systems Jourmal,1995,34(2):205～221   
164Stalings W (Ed).Advances in ISDN and Broadband ISDN. IEEE Computer Society Press, 1992   
165Stalings W (Ed).Advances in Local and Metropolitan Networks. IEEE Computer Society Press,1994 Stallings W.Operating Systems $( 2 ^ { \mathrm { n d } } \mathrm { E d } )$ .Prentice-Hall,1995 Stamper D A.FDDI Handbook: High-Speed Networking Using Fiber and Other Media. Addison-Wesley,1994 Stenstrom P,Joe T,Gupta A. Comparative Performace Evaluation of Cache-Coherent NUMA and COMA Architectures. $\mathbf { P r o c . 1 9 ^ { t h } }$ Annu. Int. Symp.Computer Arch.,1992,86～91 Stunkel C B et al. The SP2 High-Performance Switch. IBM Systems Journal,1995,34(2): 185～204 Sun X H,Ni L M. Another View of Parallel Speed.Proc. Superomputing'90,1990,324\~ 333 Sun X H,Rover D T.Scalability of Paralel Algorithm-Machine Combinations. IEEE Trans. on Parallel and Distributed Systems,1994,5(6):599～613 Swarztrauber P N.Multiprocessr FFTs.Parallel Computing,1987,5:197～210 Tolmie D,Flanagan D. HiPPI: It's Not Just for Supercomputers Anymore.Data Communication( http: //www. data. com/) Trew A,Wilson G (Eds). Past,Present Paralel: A Survey of Available Parallel Computer Systems.Springer-Verlag,1991 Valiant L G.Paralelism in Comparison Problems.J.of SIAM,Computing,1995,4(3):348 \~355 Valiant L G A Bridging ModelforParalel Computation.Comm.of ACM,199,3(8):103 \~111 Vishkin U.Optimal Paralel Matching in Strings.Info.and Control,1985,67(1-3):913 Wagar B A. Hyperquicksort: A Fast Sorting Algorithm for Hypercubes.Proc.of the Second Conference on Hypercube Multiprocessors,1987,292～299 Wah B W,Li G J,Yu C F.Multiprocessing of Combinatorial Search Problems. Computers, 1985,18(6):93\~108 Warschko T M,Blum J M,Tichy W F. The Parastatim Project: Using Workstations as Building Blocks for Paralel Computing.Proc.of Int’1 Conf.on Paralel and Distributed Processing,Techniques and Applications (PDPTA'96),1996,1:375～386 Whitney S et al. The SGI Origin Software Environment and Application Performance. Proc. of COMPCON Spring 97,IEEE Computer Society,Feb.1997,165～170 Wilson G V,Lu P (Eds). Parallel Programming Using C+ + .MIT Press,1996 Wolfe M JAutomatic Vectorization,Data Dependence,and Optimizations for Paralel Com-puters，in Hwang and DeGroot(Eds) : Paralel Processing for Supercomputing and Artificial Intelligence,cGraw-Hill,1989   
184Wolfe M. High-Performance Compilers for Paralel Computing. Addison-Wesley,Pub. Com-

pany,1996185Wylie JC.The Complexity of Parallel Computations.[PhD thesis].Cormell Univ.,1979186Xu Z,Hwang K.Coherent Parallel Programming in C//.Proc.of Int'1 Conf.on Advances inParallel and Distributed Computing,IEEE Computer Society Press,Mar.1997,116～122187Zhang X D,Yan Y,He K Q.Latency Metric: An Experimental Method for Measuring andEvaluating Parallel Program and Architecture Scalability.J.of Paralldl and Distributed Com-puting,1994,22:392～410188 Zima H et al. Vienna FORTRAN-A Language Specification.ICASE,1992.Version 1.1189 陈国良.平衡分组选择网络：计算机研究与发展,1984,21(11)：9～21190 陈国良编著.VLSI计算理论与并行算法.合肥：中国科学技术大学出版社,1991191 陈国良编著.并行算法的设计与分析.北京：高等教育出版社,1994192 陈国良.并行算法的可扩放性分析.小型微型计算机系统1995,16(2)： $1 0 \sim 1 6$ 193 国家智能计算机研究开发中心.曙光1号智能化共享存储多处理机系统.技术报告：1993194 曙光信息产业有限公司.曙光天潮系列曙光2000超级并行计算机.技术白皮书.1998195 李晓梅,蒋增荣等编著.并行算法(第五章).湖南科技出版社，1992196 沈志宇等编著.并行程序设计.长沙：国防科学技术大学出版社,1997197 孙家昶等编著.网络并行计算与分布式编程环境.北京：科学出版社,1996198 唐策善，梁维发编著.并行图论算法.合肥：中国科学技术大学出版社，1991199 王鼎兴,陈国良编著.互联网络结构分析.北京：科学出版社，1990200 王鼎兴,庄伟强编著.一种实现并行计算的新主流技术—NOW.小型微型计算机系统,1995,16(2):29～34201 王嘉谟,沈毅主编.并行计算方法(上册).北京：国防工业出版社,1987202徐士良编著.计算机常用算法(第二版),北京:清华大学出版社,1996

# 并行与分布计算Web网址

# Parallel and Distributed Computing Bibliography on WWW

Distributed Algorithms and/or Distributed Systems (http://www.cwi. nl/cwi/departments/AAl/distcom/distcom. html)   
The CSP archive at Oxford(http://www.comlab.ox.ac.uk/archive/csp. html)   
Digital Technical Reports(http://www.research.digital.com/wrl/techre   
ports/)   
Bibliographies on Parallel Processing (http://linwww.ira.uka.de/bibliography/Paralel/index. html)   
Transputer,Occam and Parallel Computing Archive (http://unix. hensa.ac. uk/parallel/index. html)   
Parallel and Heterogeneous Publications (http://www-cse. ucsd.edu/users/jenny/parpubs. html)   
IEEE/CS ParaScope(http://computer.org/parascope/), world-wide paralel computing sites   
High Performance Computing Lists   
(http://www.cs. colorado.edu/homes/mcbryan/public- html/bb/2/ summary. html)   
The Language List(htp://cuiwww.unige.ch/langlist)enumerate   
programming languages   
TOP 500(http://www.netlib.org/benchmark/top500. html)   
World's TOP 500 most powerful computing sites(at Netlib,University of Tennessee)

# News Groups about Paralel and Distributed Computing

Architecture(news://comp. arch) Benchmarks(news://comp.benchmarks) MPI(news: //comp. parallel. mpi) OS Research(news: //comp.os.research) + Parallel(news://comp.parallel) PVM(news: //comp. parallel. pvm) Supercomputer(news: //comp.sys. super)

# Parallel Computer Models

:Bulk Synchronous Paralel(BSP)(http://www.comlab.ox.ac.uk/oucl/

oxpara/bsplib.html)   
The Concurrent Systems site(http://www.comlab.ox.ac. uk/archive/ concurrent. html) at Oxford Univ.links to theoretical and formal models for paralel and distributed systems Parallel Monte Carlo simulation at Berkeley (http://dnclab.berkeley.edu/codef/may/prj. html)   
·Numerical recipes(http: //cfata2. harvard.edu/nr/nrhome. html)has on-line book and code   
·PLAPACK,InterCom(iCC),SUMMA(htp://www. cs. utexas. edu/users/rvdg)at Austin

# Benchmarks and Performance

Netlib Repository (http://www. netlib.org/liblist. html), has performance data on many benchmarks: LINPACK，LAPACK，BLAS，BLACS，Livermore loops，Dhrystone，Whet-stone,NAS,SPEC,Sim,etc. It contains sources for some benchmarks.   
PARKBENCH (PARallel Kermels and BENCHmarks) (http://netlib2.cs.utk.edu/parkbench/)

# Microprocessors

:DEC Alpha home page(http: //www.digital. com/semiconductor/alpha/alpha. htm)   
SGI MIPS Group site(http://www.sgi. com/MIPS/)   
· IBM's PowerPC microprocessors site( http://www.chips. ibm.com/products/ppc/) Sun SPARC page(http://www. sun. com/sparc/) Fujitsu TurboSPARC Microprocessors (http://www.fujistumicro.com/sparcupgrade/sparcmicro.html)

# Systems Interconnects

Myrinet(htp://www.myri.com)   
PCI SIG Home Page(htp://www. teleport.com/～pc2/pcisigindex. html)   
The ATM Forum(http: //atmforum. com/)   
SCI News(http://www.dolphinics. no/SCI_News/SCI- News.html)at Dolphin   
Interonnect Solutions(http: //www.dolphinics. no/Dolphin. html)

# Distributed Memory Technology

DSM bibliography(http://www.cs. ualberta.ca/\~rasit/dsmbiblio. html)   
DICE(htp://www-mount. ee.umn.edu/\~dice/)   
FLASH(http://www-flash.stanford. edu/)   
NUMAchine at the Univ.of Toronto   
(http: //www. eecg. toronto. edu/EECG/RESEARCH/ParallelSys/   
numachine.html)

:Simple COMA(htp://playground.Sun.COM:80/pub/S3. mp/simple-coma/)

# Threads

:Bibliography on multithreading(http://linwww.ira.uka.de/bibliography/Os/threads. html) :Pthread at MIT (http://www. mit. edu:8001/people/proven/pthreads. html).

# Synchronization and Communication

:High-performance synchronization papers and codes. (http: //www. cs. rochester. edu/users/faculty/scott/synchronization. html).   
:Berkeley Active Messge page( http: //now. cs.berkeley. edu/AM/active_ messages. html)   
:Active Messages for SP- 2(htt://www. cs. cormell edu/Info/Projects/CAM/sp2. html)at Cornell

# File Systems

:IBM SPs GPFS(http://www. rs6000.ibm. com/sofware/sp_ producst/gpfs. html)and PIO (http://www.rs600. ibm. com/software/sp_products/piofs. html) The HA-NFS project (http: //www. cs.cmu. edu/afs/cs.cmu. edu/user/mootaz/ftp/html/hanfs. html)   
The Berkeley xFS(http://now. cs. berkeley. edu/Xfs/xfs. html)   
CIFS(Common Internet File System)(http://www. microsoft. com/intdev/cifs/)   
:WebNFS(http://www. sun. com/webnfs/index. html)

# Workload Management (Load sharing,load balancing, batching, scheduling)

:IBM LoadLeveler(http: //www. rs6000. ibm.com/software/sp _ products/ loadlev. html)   
Scheduling, batch processing,load balancing(http://www. epm: orml. gov/\~ zhou/lds/lds. html)at Oak Ridge National Laboratory

# Symmetric Multiprocessor(SMP)

:SGI Power Challenge white paper (ftp://ftp.sgi.com/sgi/whitepaper/ challenge- paper. ps. Z) Intels Multiprocessor Specification( http: //www. intel. com/IAL/processr/ mpovr.html） Digital AlphaServer Family (http://www.digital. com/alphaserver/) HP Enterprise Server page (http://www. hp.com/gsy/products. html) IBM Server page(http: //www. rs6000.ibm. com/hardware/# eservers)

·Sun SMP Architectures (http: //www. sun. com/smi/ssoftpress/books/Catanzaro/Catanzaro. html) :The Cray Research system page(http: //www.cray.com/products/systems)

# CC-NUMA and NCC-NUMA System

:Sequent NUMA-Q(http://www.sequent.com/numaq/technology/) ·SGI/Gray Origin 2000(http: //www.sgi. com/Products/hardware/servers/ index. html) :Cray T3E(http://www.cray.com/products/systems/crayt3e/)

# Massively Parallel Processors (MPPs and HPC)

:DEC HPC site(http://www.digital. com/info/hpc/welome. html)

:HPC Modernization Program (http: //www.aero. hq. nasa. gov/hpcc/ petaflops/) PetaFLOPS web site(http://www.aero. hq. nasa. gov/hpcc/) NASA HPCC Program(htp: //www. aero. hq. nasa. gov/hpcc/) Cray T3E( htp: //www.cray. com/products/systems/crayt3e/)   
. IBM SP(http: //www. rs6000. ibm.com/hardwaere/argescale/) Intel Paragon( http: //www.sdsc. edu/Services/Consult/Paragon/paragon. html)

# Clustering Technology and Systems

Kai Li(http://www.cs. princeton. edu/\~li/)   
Overview of Checkpoint (http: //warp.dcs.st-and.ac.uk/warp/systems/ checkpoint/) Single System Image and Metacomputing Berkeley WebOS(http://now.CS.Berkeley.EDU/WebOS/) Solaris MC (http://www.sun.com/960201/cover/solaris-mc.html) National Scalable Cluster Project(NSCP)(http://www_ lac.eecs. uic.edu/NSCP2. html) SP2 at MHPOC(http://www.mhpcc.edu/doc/SP2.general/SP2.general. html)   
Sequent Symmetry 5000 Cluster (ttp://www.sequent.com/public/solution/server/s5000cl. html)   
Sun Microsystems Ultra HPC Cluster (http: //www. sun. com/products-n-solutions/hw/servers/product/PDB/)

# Parallel Programming : models , languages and tools

:X3H5-Paralel Processing Constructs for High Level Programming Languages

(http://www.x3.org/tc_home/x3h5.html),at ANSI(inactive) ANL Shared-Variable Macros on Solaris (ftp://dit.lth.se/pub/sun_thread_ANL_macros) $\mathbf { u } \mathbf { C } + \mathbf { \epsilon } + \mathbf { \epsilon }$ (http://plg.uwaterloo.ca/\~pabuhr/uC + + html) Cray MPP Fortran Model (ftp://ftp.cray.com/product-info/program _env/program _ model. html) Linda Group(http://www. cs. yale.edu/HTML/YALE/CS/Linda/linda. html) The Fortran M Programming Language (http://www. mcs.anl. gov/fortran-m/index. html) Introduction to PVM (htp://www. mhpcc. edu/training/workshop/html/pvm/PvmIntro. html)from Maui workshop MPI Standard site (http://www. mcs. anl.gov/mpi/index. html) :Parallel Tools Consortium(http: //www.IInl. gov/ptools/) :Vienna Fortran Compilation System(http://www. par.univie.ac.at/project/vfcs. html)

# Parallel Object Oriented Programming

： $\mathbb { C } \mathbb { C } + \mathbb { + }$ (http://www.compbio.caltech.edu)at Caltech   
:CHARM $+ ~ +$ (http://charm. cs.uiuc.edu)at UIUC LPARX ftp site(ftp://cs. ucsd. edu/pub/skohn/lparx/)at UCSD Object Oriented Parallel Programming(http://www.arc.unm.edu/workshop/oop/oop. html)a suruey at U.of New Mexico.   
pC+ + ,Sage+ + (http://www.cica.indiana.edu/sage)at Indiana University

# Parallel Programming Issues

AIMS(http://www. nas. nasa.gov/NAS/Tools/Projects/AIMS/)(NASA Ames) The Lost Cycles Toolkit for Performance Prediction (http://www.cs.rochester.edu/u/leblanc/prediction. html),at Univ.of Rochester

# Sites List of the Important Agencies,Laboratories ,Consortiums and Organizations

:MIT Parallel and Distributed Operating Systems Group (http://www.pdos.lcs. mit.edu/). National Center for Supercomputer Applications at UIUC(NCSA) (http://www. ncsa. uiuc.edu/) NCSA Virtual Reality Faclities (http://www. ncsa. uiuc.edu/Viz/VR/)and CAVE.(http: // evlweb.eecs. uic. edu/EVL/VR/systems. html # CAVE) Conell Theory Center (CTC)(http://www. tc.cornel.edu/ctc. html) Argonne Natl Laboratory,Mathematics & Computer Science Div. (http://www. mcs. anl. gov/) Army Research Lab(http://www.arl.army. mil/)   
:Lawrence Livermore National Laboratory (http://www.llnl. gov/comp/comp.html)   
:Los Alamos Natl Laboratory(LANL)Advanced Computing Laboratory

(http: //www.acl.lanl.gov/). Maui High Performance Computing Center （MHPCC)（http://www. mhpcc. edu/mhpcc. html) NASA Ames Research Center, Numerical Aerodynamic Simulation Systems Division,Applied Research Branch(http://www. nas. nasa.gov/RNR/rnr. htrml) NASA Jet Propulsion Laboratory (JPL)(http: //www.jpl. nasa. gov/) National Center for Supercomputer Applications(NCSA)(http: //www. ncsa. uiuc. edu/) National Energy Research Supercomputer Center(NERSC)(htp://www. nersc. gov/) Oak Ridge National Laboratory: Center for Computing(http: //www.cs.orml. gov/) San Diego Supercomputer Center (http: //www.sdsc.edu/SDSCHome. html) Sandia National Laboratories(http://www. cs. sandia. gov/) Massively Paralel Comp. Res. Lab. :Parallel Processng in Japan (http://fuji.stanford.edu/papers/ppij. html)

# Commercial and Industrial Companies

Cray Research(http://www.cray. com/) Fujitsu(http://www. fujitsu. co.jp/) IBM High-Performance Computing( htp://ibm. tc.cornell. edu/) · ParaSoft Corporation(http: //www. parasoft.com/) :Silicon Graphics(http://www.sgi.com/) Sun Microsystems(http://www.sun.com/) :Thinking Machines Corp.(http://www. think.com/)

# 术语中-英对照及索引

3-立方环  
3点格式  
5点格式  
9点格式  
Amdahl定律  
ATM适配层（AAL）  
Batcher定理  
BM算法  
Brent定理  
BSP库  
$C ^ { 3 }$ 模型  
Cannon 算法  
CCOTS  
Cormen FFT算法  
Cougar操作系统  
Dhrystone基准测试程序  
DNS算法  
EisPACK特征值软件包  
E-立方选路  
FORALL结构  
Fox算法  
Gantt图  
Gustafson 定律  
h-关系  
Horner规则  
KMP算法  
LAPACK基准测试程序  
LinPACK基准测试程序  
logP模型  
$( m , n )$ -选择  
Moore定律

3-CCC(Cube Connected Cycle) 12   
Three-Point Stencil 180   
Five-Point Stencil 168   
Nine-Point Stencil 180   
Amdahl's Law 83   
ATM Adaptation Layer 20   
Batcher's Theorem 149   
Boyer and Moore's Algorithm 133   
Brent's Theorem 110   
BSP Library 123   
Computation,Communication,   
Congestion Model 118   
Cannon's Algorithm 215   
Commercial Commodity Off The Shelf 7   
Cormen's FFT Algorithm 269   
Cougar OS 8   
Dhrystone Benchmark 99   
Dekel,Nassimi and Sahni's Algorithm 218   
E-Cube Routing 186   
FORALL Construct 354   
Fox's Algorithm 218   
Gantt Chart 319   
Gustafson's Law 85   
h-relation 115   
Hormer's Rule 158   
Kunth,Morris and Partt's Algorithm 133   
LAPACK Benchmark 100   
LinPACK Benchmark 100   
logP Model 116   
$( m , n )$ -selection 148   
Moore's Law 48

Myrinet开关网 N-概率转发法 $\pmb { n }$ 次单位元根 NPB

OpenMP标准Origin2000系统PARKBENCHPCAM

POSIX 线程(Pthreads)POWER-2微处理器

PVM监控进程(pvmd)  
PVM可调用库(libpvm3.a)  
PVM控制台  
RAS  
ScaLAPACK基准测试程序  
Shell 结构  
SP系统  
SPEC浮点程序  
SPEC整数程序  
Sun 和 Ni 定律  
TPC基准测试程序  
Valiant归并算法  
Whetstone基准测试程序  
X-树  
X3H5共享存储模型  
X-Y选路  
$\pmb { \Omega }$ 网络

Myrieat Switch Network 17   
N-Chance Forwarding 66   
Principal $\pmb { n }$ th Root of Unity 261   
NAS(Numerical Aerodynamic Simulation)   
Parallel Benchmark 101   
OpenMP Standard 323   
Origin System 40   
PARallel Kernels and BENCHmark 101   
Partitioning,Communication,   
Agglomeration,Mapping 164   
Portable Operating System Interface Threads 322   
Performance Optimized With Enhanced   
RISC-2Microprocessor 53   
PVM Daemon Process 348   
PVM User-Callable Library 348   
PVM Console 348   
Reliability Availability Serviceability 7   
ScaLAPACK Benchmark 100   
Shell Architecture 24   
SP System 53   
SPECfp 100   
SPECint 100   
Sun and Ni's Law 85   
Transaction Processing   
Council Benchmark 102   
Valiant's Merging Algorithm 146   
Whetstone Benchmark 99   
X-Tree 12   
X3H5 Shared-Memory Model 320   
X-Y Routing 185   
Ω Network 15

# Ellpack-Itpack Storage Scheme

242

# B

版本管理程序 Version Manager 373  
倍增技术 Doubling Technique 155

本地总线  
比较并交换  
比较器  
比较器网络  
编程工具  
编程环境  
编辑器  
编译器  
编译制(指)导  
标准性能评价公司(SPEC)  
表面-容积效应  
表序问题  
并行FFT算法  
并行I/O文件系统(PIOFS)  
并行编程风范  
并行操作环境(POE)  
并行查错(pdbx)  
并行程序调试  
并行程序设计  
并行程序设计模型  
并行程序性能分析  
并行度(DOP)  
并行归约  
并行化  
并行计算  
并行宽松度  
并行算法  
并行随机存取机(PRAM)  
并行向量处理机(PVP)  
并行虚拟机(PVM)  
并行正则采样排序(PSRS)  
波前  
播送  
不允许同时读写(EREW)

# C

# 测试并设置

Local Bus 13   
Compare & Swap 298   
Comparator 150   
Comparator Network 150   
Programming Tools 285   
Programming Environment 285   
Editor 372   
Compiler 372   
Compiler Directives(Pragmas) 285   
Standard Performance Evaluation   
Corporation 49   
Surface-to-Volume Effect 171   
List Ranking Problem 155   
Parallel FFT Algorithm 269   
Parallel I/O File System 60   
Parallel Programming Paradigms 309   
Parallel Operating Environment 56   
Parallel Debugger 56   
Parallel Program Debugging 386   
Parallel Programming 283   
Parale Programming Model 312   
Parallel Program Performance Analysis 388   
Degree Of Parallel 291   
Parallel Reduction 312   
Parallelizing(MIMDizing) 377   
Parallel Computing 3   
Parallel Slackness 115   
Parallel Algorithm 107   
Parallel Random Access Machine 112   
Parallel Vector Processor 21   
Parallel Virtual Machine 348   
Parallel Sorting by Regular Sampling 144   
Wavefront 167   
Broadcast 338   
Exclusive-Read and Exclusive-Write 112

测试辅助程序  
查错辅助程序  
长宽比  
超(级)步  
超级计算  
超立方  
超立方上FFT算法  
超线性加速  
成本  
成本最优  
程序分析工具  
齿对角存储法  
虫蚀路由芯片（WRC)  
虫蚀选路  
稠密阵  
传递闭包  
传输汇聚子层(TC)  
传输控制协议(TPC)  
串  
串匹配  
串行FFT递归算法  
串行FFT迭代算法  
串行程序并行系统(SPPS)  
申行程序设计  
粗粒度  
存储转发选路  
存储器总线

Testing Aids 373   
Debugging Aids 373   
Aspects Ratios 175   
Superstep 115   
Supercomputing 3   
Hypercube 190   
FFT Algorithm on Hypercube 273   
Super-linear Speedup 87   
Cost 110   
Cost Optimal 110   
Program Analysis Tools 375   
Jagged-Diagonal Storage Scheme 243   
Wormhole Routing Chip 72   
Wormhole Routing 119   
Dense Matrix 223   
Transitive Closure 137   
Transmission Convergence Sublayer 20   
Transmission Control Protocol 303   
String 132   
String Matching 132   
Recursive Sequential FFT Algorithm 267   
Iterative Sequential FFT Algorithm 265   
Serial Program Parallel System 285   
Sequential Programming 283   
Coarse Granularity 118   
Store and Forward Routing 119   
Memory Bus 13

# D

大规模并行处理机(MPP) Massively Parallel Processor 21   
大气模型 Atmosphere Model 180   
大同步并行(BSP) Bulk Synchronous Parallel 113   
代码并行化 Code Parallelization 383   
代码产生器 Code Generator 373   
代码生成 Code Generation 385   
代码向量化 Code Vectorization 380   
代码优化 Code Optimization 380   
带状划分 Striped Partitioning 203

单程序多数据(SPML  
单道程序设计  
单点累积  
单点散射  
单点收集  
单复制  
单线程  
单一系统映像(SSI)  
单源最短路径  
单指令多数据(SIMD  
导出数据类型  
登录段  
登录片  
登录条  
等速度标准  
等效率函数  
递归  
递归对剖  
递归转置矩阵  
点到点通信  
迭代法  
蝶形网上FFT算法  
定制  
动态调度  
动态规划  
动态网络  
动态性能分析  
都域网(MAN)  
独占方式  
断点调试  
对称Unix(SNIX)  
对称的  
对称多处理机(SMP)  
对角存储法  
对角占优  
对剖宽度  
对数划分  
对准

Single-Program Multiple-Data 290   
Uniprogramming 289   
Single-Node Accumulation 190   
Single-Node Scatter 200   
Single-Node Gather 197   
1-Copy 302   
Single-Threading 313   
Single-System Image 48   
Single-Source Shortest Path 138   
Single Instruction Multiple Data 21   
Derived Datatype 342   
log segment 65   
log fragment 65   
log-based striping 65   
ISO-speed Metrics 91   
ISO-efficiency Function 90   
Recursion 149   
Recursive Bisection 175   
Recursive Transposing Matrix 205   
Point-to-Point Communication 343   
Iterative Method 243   
FFT Algorithm on Butterfly 272   
Custom-Made 22   
Dynamic Scheduling 319   
Dynamic Programming 161   
Dynamic Network 10   
Dynamic Performance Analysis 15   
Metropolitan Area Network 9   
Dedicated Mode 289   
Break-Point Debuggin 386   
Symmetric Unix 68   
Symmetric 228   
Symmetric Multi-Processor 21   
Diagonal Storage Scheme 242   
Diagonal Dominant 228   
Bisection Width 10   
Logarithmic Partition 146   
Aligmment 353

多程序多数据(MPMD)  
多到多播送  
多到多个人通信  
多道程序设计  
多点播送  
多点累积  
多级互连网络（MIN）  
多线程  
多指令多数据(MIMD)  
多重网格法

Multiple-Program Multiple-Data 332   
All- to-All Broadcast 193   
All-to-All Personalized Communication 196   
Multiprogramming 289   
Multinode Broadcast 193   
Multinode Accumulation 193   
Multistage Interconnection Network 15   
Multithreading 315   
Multiple Instruction Multiple Data 21   
Multigrid 249

# E

二维FFT二维环绕二维网孔二元信号灯

Two-Dimensional FFT 279   
2-D Torus 11   
2-D Mesh 11   
Binary Semaphore 296

# F

反相关  
非存在  
非高速缓存一致性NUMA(NCC-NUMA)  
非集中模式  
非均匀存储访问(NUMA)  
非确定模式  
非数值算法  
非远程存储访问(NORMA)  
非周期串  
非阻塞发送  
非阻塞接收  
分布  
分布共享存储(DSM)  
分布计算  
分布算法  
分段与组装子层(SAR)  
分开的地址空间  
分块矩阵乘法  
分时方式

Antidependent 378   
Nonexistent 287   
Non-Cache   
Coherence NUMA 47   
Decentralized Schemes 177   
Non-Uniform Memory Access 26   
Non-Deterministic Model 319   
Non-Numerical Algorithm 107   
No-Remote Memory Access 27   
Aperiodic String 136   
Non-Blocking Send 121   
Non-Blocking Receive 343   
Distribution 352   
Distributed Shared Memory 21,23   
Distributed Computing 108   
Distributed Algorithm 108   
Segmentation and Reassembly Sublayer 20   
Separate Address Space 315   
Block Matrix Multiplication 214   
Time-Sharing Mode 289   
分相PRAM Phase PRAM (APRAM) 113   
分支汇合 Fork/Join 290   
分支界限 Branch and Bound 161   
分治 Divide-and-Conquer 149   
分治并行 Divide and Conquer Parallel 309   
G   
高端并行机 High-End Parallel Computer 7,   
高斯-赛德尔法 Gauss-Seidel Method 239   
高斯消去法 Gaussian Elimination   
高斯-约旦消去法 Gauss-Jordan Elimination 233   
高斯-约旦主元消去法 Gaussian-Jordan Elimination With Partial Pivoting 238   
高速缓存行 Cache Line 29   
高速缓存一致性非均匀存储 (CC-NUMA) Coherent-Cache   
访问 Non-Uniform Memory Access 27   
高速网络(HSN) High Speed Network 47   
高性能 Fortran(HPF) High Performance Fortran 353   
高性能并行接口(HiPPI) High Performance Parallel Interface 18   
高性能计算 High Performance Computing 3   
高性能计算和通信(HPCC) High Performance Computing &   
Communication / 5   
高性能开关(HPS) High Performance Switch 53   
更实际的计算模型 More Realistic Computation Model 123   
工作池并行 Work Pool Parallel 310   
工作站机群(COW) Cluster Of Workstation 8,21,23   
工作站网络(NOW) Network Of Workstation 61   
公共 PRAM-CRCW Common PRAM-CRCW 112   
公共前端 Common Front End 374   
功能并行 Functional Parallel 290   
功能分解 Functional Decomposition 166   
功能划分 Functional Partitioning 148   
共轭梯度法 Conjugate Gradient 251   
共享变量 Shared-Variable 285   
孤幼制导 Orphan Directives 324   
光纤分布数据接口(FDDI) Fiber Distributed Data Interface 17   
广度优先搜索 Breadth-First Seaching 161   
广域网(WAN) Wide Area Network 9   
归纳变量 Induction Variables 312   
归约 Reduction 338   
过程工具 Process Tools 374

# H

# 带状划分矩阵-向量乘法

核  
核模式  
红-黑着色法  
互斥  
互联网协议(IP)  
划分  
环  
环绕(正方)网孔  
回代法  
回溯  
汇聚子层(CS)

M-V Multiplication Using   
Row- wise Striping 210   
Kermel 288   
Kernel Mode 288   
Red-Black Coloring 248   
Mutual Exclusion 292   
Intermet Protocol 303   
Partitioning 144,164   
Ring 191   
Wraparound( Square)Mesh 194   
Back Substituting 228   
Backtracking 161   
Convergence Sublayer 20

# J

基-2FFT算法  
基-4FFT算法  
基本代数子程序(BLAS)  
基本通信层(BCL)  
奇偶归约法  
基线程  
基于目录的协议  
基准测试程序  
集成工具  
计算科学与工程  
计算密集  
加速级联  
加速战略计算创新（ASCI)  
监听协议  
见证函数  
交叉开关  
交叉引用程序  
交互并行化

Radix-2 FFT Algorithm 278   
Radix-4 FFT Algorithm 278   
Basic Algebra Subprogram 99   
Base Communication Layer 299   
Odd-Even Reduction 257   
Base Thread 320   
Directory Based Protocol 31   
Benchmark 99   
Integrated Tool 285   
Computational Science & Engineering 3   
Compute- Intensive 4   
Accelerated Cascading 161   
Accelerated Strategic Computing   
Initiative 6   
Snoopy Protocol 31   
Witness Function ： 136   
Crossbar Switcher 14   
Cross Referencer 373   
Interactive Parallelism 312

节点度  
紧致界  
进程  
进程描述符  
进程保护  
进程调度  
进程管理  
进程活动环境  
进程控制  
进程组  
经理/雇员模式  
竞争函数  
静态调度  
静态分析  
静态网络  
静态性能分析  
就绪  
局部通信  
局域网络(LAN)  
矩阵-向量乘法  
句柄  
卷积  
绝对加速  
均匀存储访间(UMA)  
均匀划分

# K

Node Degree 10   
Tightly Bound 109   
Process 287   
Process Descriptor 288   
Prccess Protection 288   
Process Scheduling 288   
Process Management 288   
Context 328   
Process Control 288   
Process Group 335   
Manager/Worker Schemes 177   
Duel Function 136   
Static Scheduling 319   
Static Analysis 379   
Static Network 10   
Static Performance Analysis 380   
Ready 287   
Local Communication 168   
Local Area Network 9   
Matrix-Vector Multiplication 209   
Handles 337   
Convolution 159   
Absolute Speedup .88   
Uniform Memory Access 25   
Uniform Partitioning 144

开放系统连接(OSI)  
开销  
壳  
可扩放共享存储多处理机  
(S2MP)  
可扩放性  
可扩放一致性接口(SCI)  
可视化工具(VT)  
客户/服务器  
控制并行  
控制集成

Open System Interconnection 20   
Overhead 117   
Shell 288   
Scalable Shared Memory   
Multi Processor 41   
Scalability 88   
Scalable Coherence Interface 46   
Visualization Tool 56   
Client/Server 334   
Control-Parallel 290   
Control Integration 374   
控制相关 Control-Dependent 378   
库函数 Library Function 285   
跨步 Hops 117   
块带状划分 Block-Striped Partitioning 203   
块棋盘划分 Block-Checkboard Partitioning 204   
块棋盘划分矩阵-向量乘法 M-V Multiplication Using   
Block-Checkboard 211   
块循环分配 Block Cyclic Distribution 176   
快排序 Quicksort 130   
快速傅里叶变换(FFT) Fast Fourier Transform 265   
快速消息(FM) Fast Message 302   
快速以太网 Fast Ethernet 17

# L

离散傅里叶变换(DFT)  
离散傅里叶逆变换(IDFT)  
粒度  
连接器和加载器  
廉价冗余磁盘阵列(RAID)  
链路级协议（LLP)  
临界区  
零复制协议  
流水线  
流水线并行  
流相关  
路障  
逻辑盘组管理器(LVM)

Discrete Fourier Transform 260.   
Inverse Discrete Fourier Transform 262   
Granularity 291   
Linker and Loader 372   
Redundant Array of Inexpensive Disk 7   
Link-Level Protocol 42   
Critical Region 297   
Zero-Copy Protocol 302   
Pipelining 158   
Pipeline Parallel 309   
Flow-Dependent 378   
Barrier 296   
Logical Volume Manager 57

M

模式串 Pattern String 133

N

内插 Interpolation 250  
内射法 Injection 250

# P

胖超立方 Fat Hypercube 43   
胖树 Fat Tree 12   
批处理方式 Batching Mode 289   
平方根划分 Square Root Partitioning 146   
平衡树 Balanced Tree 153   
平均延迟标准 Average Latency Metrics 95   
破对称 Symmetry Breaking 161

# Q

期望复杂度  
棋盘划分  
前缀和  
抢先方式  
切通选路  
轻量级核(LWK)  
轻量级进程  
求解拉普拉斯方程的雅可比  
算法  
求解三对角方程组  
求解上三角方程组  
取并加  
全高速缓存存储访问(COMA)  
全交换  
全局层Unix(GLUnix）  
全局命名空间  
全局通信  
全晴空(TCS)  
确定模式  
确定算法  
确定选路  
群件工具  
群体通信

Expected Complexity 109   
Checkboard Partitioning 204   
Prefix-Sums 198   
Preemptive Mode 289   
Cut-Through Routing 189   
Light-Weight Kernel 8   
Light-Weighted Process 289   
Solving Laplace Equation   
Using Jacobi Algorithm 246   
Solving a System of Triagonal Equations 231   
Solving Upper Triangular System 229   
Fetch& Add 298   
Cache-Only Memory Access 26   
Total Exchange 200   
Global Layer Unix 63   
Global Naming Space 313   
Global Communication 169   
Total Clear Sky 181   
Deterministic Model 319   
Deterministic Algorithm 108   
Deterministic Routing 185   
Groupware Tools 374   
Collective Communication 338

# R

任务并行 Task-Parallel 290  
任务调度 Task Scheduling 319  
任务调度算法 Task Scheduling Algorithm 177  
任务分配 Task Allocation 353  
任意PRAM-CRCW Arbitrary PRAM-CRCW 112  
日志 Journaling 45

# S

三对角  
散射  
上公切线  
上界  
上三角  
上凸壳  
设计编辑器  
深度优先搜索  
失效函数  
实用程序  
事件  
事件分析  
收集  
输出相关  
属籍服务  
属主-计算  
数据并行  
数据并行制导  
数据分布  
数据集成  
数据密集  
数据驱动  
数据映射制导  
数据总线  
数值算法  
门锁  
双调序列  
双复制  
死锁  
松弛  
松散同步  
算法  
随机算法  
缩行存储法  
所有点对间的最  
锁

Tridianogal 228   
Scatter 338   
Upper Common Tangent 151   
Upper Bound 109   
Upper Triangular 228   
Upper Convex Hull 151   
Design Editor 373   
Depth-First Searching 161   
Failure Function 133   
Utilities 288   
Events 292   
Event Analysis 387   
Gather 338   
Output-Dependent 378   
Membership Service 57   
Owner-Compute 291   
Data-Parallel 290   
Data Parallel Directives 354   
Data Distribution 374   
Data Integration 374   
Data-Intensive 4   
Data-Driven 334   
Data Mapping Directives 354   
Data Bus 13   
Numerical Algorithm 107   
Latch 321   
Bitonic Sequence 149   
2-Copy 301   
Deadlock 297   
Relaxation 250   
Loosely Synchronous 313   
Algorithm 107   
Randomized Algorithm 108   
Compressed Row Storage Scheme 241   
All Pairs Shortest Paths 138   
Lock 292

# T

贪心法 Greedy Method 161   
贪心转发法 Greedy Forwarding 66   
探针效应 Probe Effect 386   
套接字 Socket 299   
通告服务 Notification Service 57   
通信 Communication 111   
通信体 Communicator .335   
网络密集 Network-Intensive 4   
同步 Synchronization 110   
同步路障 Synchronization Barrier 113   
同步算法 Synchronous Algorithm 107   
同步通信 Synchronous Communication 353   
投射 Projection 250   
凸多边形 Convex Polygon 151   
凸壳 Convex Hull 151   
图形应用开发环境(GRADE) Graphical Application Development   
Environment 390

W

外部过程 Extrinsic Procedures 354  
网孔上FFT算法 FFT Algorithm on Mesh 269  
网络到网络接口(NNI) Network-Network Interface 20  
网络计算 Network Computing 108  
网络接口电路(NIC) Network Interface Circuitry 47  
网络文件系统(NFS) Network File System 57  
网络直径 Network Diameter 10  
维序选路 Dimension-Ordered Routing 185  
位序 Rank 147  
无服务器网络文件系统(xFS) Serverless Network File System 64  
无主机 Hostless 333  
物理介质相关子层(PMD) Physical Medium Dependant Sublayer 20

# X

稀疏阵 Sparse Matrix 223   
系统构造程序 System Builder 373   
系统数据储存库(SDR) System Data Repository 57   
系统域网络(SAN) System Area Network 9   
系统总线 System Bus 13   
细胞IRIX Cellular IRIX 44   
细粒度 Fine Granularity 316   
下界 Lower Bound 109   
下三角 Lower Triangular 228   
下凸壳 Lower Convex Hull 151   
显式并行 Explicit Parallelism 312   
显式分配 Explicit Allocation 315   
显式相互作用 Explicit Interaction 315   
现场切换 Context Switch 288   
线程 Threads 289   
线程调度 Thread Scheduling 322   
线程管理 Thread Management 322   
线程库 Thread Library 293   
线程生成 Thread Creation 293   
线程同步 Thread Synchronization 295   
线性方程 Linear Equation 227   
线性方程组 System of Linear Equations 227   
线性系 Linear System 227   
相并行 Phase Parallel 309   
相对加速 Relative Speedup 88   
相关方程 Dependent Equation 379   
相关方向向量 Dependent Direction Vector 378   
相关分析 Dependency Analysis 378   
相关距离向量 Dependent Distance Vector 378   
相关性测试 Dependency Testing 379   
向量化 Vectorilizing(SIMDizing) 377   
消息传递 Message Passing 285   
消息传递界面(MPI) Message Passing Interface 332   
消息传递库(MPL) Message Passing Library 56   
小-写问题 Small- Write Problem 65   
小型机系统接口(SCS) Small Computer System Interface 9   
协同文件缓存 Cooperative File Cache 65   
写更新 Write-Update 31   
写回(WB) Write-Back 30   
写通过(WT) Write-Through 30   
写无效 Write-Invalidate 31

心动阵列  
心跳守护程序  
新内部函数和库函数  
信元  
虚拟共享磁盘(VSD)  
需求驱动  
选路  
循环 $\mathbf { q } -$ 移位  
循环带状划分  
循环棋盘划分  
循环映射

Systolic Array 158   
Heartbeat Daemon 57   
New Intrinsic and Library Functions 354   
Cell 19   
Virtual Shared Disk 57   
Demand-Driven 334   
Routing 185   
Circular q-Shift 201   
Cyclic-Striped Partitioning 203   
Cyclic-Check Board Partitioning 204   
Cyclic Mapping 176

# Y

雅可比超松弛法雅可比迭代法延迟一到多播送一到多个人通信一维FFT一维线性阵列一致性异步并行性异上传输模式(ATM)异步算法异步通信隐式并行隐式数据分配隐式相互作用应用编程界面(API)映射拥挤用户模式用户数据报协议(UDP)用户网络接口(UNI)优先PRAM-CRCW有限差分法预处理程序域分解

Jacobi Overrelaxation 249   
Jacobi Iterative Algorithm 243   
Latency 117   
One-to-All Broadcast 189   
One-to-All Personalized Communication 196   
One-Dimensional FFT 279   
1-D Linear Array 10   
Coherence 29   
Asynchronous Paralelism 315   
Asynchronous Transfer Model 19   
Asynchronous Algorithm 108   
Asynchronous Communication 170   
Implicit Parallelism 285   
Implicit Data Allocation 314   
Implicit Interaction 313   
Application Programming Interface 304   
Mapping 175   
Congestion 118   
User Mode 288   
User Datagram Protocol 302   
User-Network Interface 20   
Priority PRAM-CRCW 112   
Finite Difference Method 168   
Preprocessor 372   
Domain Decomposition 166

元计算  
元路由器  
原子性  
源级查错器  
允许同时读不允许同时写  
(CREW)  
允许同时读写(CRCW)  
运行  
运行时并行化

Metacomputing 108   
Metarouter 43   
Atomicity 291   
Source-Level Debugger 373   
Concurrent-Read and   
Exclusive-Write 112   
Concurrent-Read and Concurrent-Write 112   
Running 287   
Run-Time Parallelization 313

# Z

栅栏操作  
找森林的根  
正定的  
正文串  
(整体)大同步  
帧调度  
直接存储访问(DMA)  
指针跳跃  
中止  
重放  
重复计算  
重量级进程  
周期串  
逐次超松弛法(SOR)  
主-从并行  
主动消息  
主机/节点  
主线程  
主元  
专用化  
转置矩阵  
子集同步  
自动并行化  
自适应选路  
总线  
阻塞发送  
阻塞接收

Fence Operation 321   
Finding Roots of a Forest 156   
Positive Definite 228   
Text String 133   
Bullk-Synchronization 122   
Frame Scheduling 45   
Direct Memory Access 300   
Pointer Jumping 155   
Suspended 287   
Relay 387   
Replicating Computation 172   
Heavy-Weighted Process 289   
Periodic String 133   
Succesive Overrelaxation 249   
Master-Slave Parallel 309   
Active Message 60   
Host/Node 333   
Master Thread 320   
Pivot 130   
Privatization 312   
Transposing Matrix 205   
Subset Synchronization 122   
Automatic Parallelism 312   
Adaptive Routing 185   
Bus 13   
Blocking Send 343   
Blocking Receive 343   
组调度 Gang Scheduling 45   
组合 Agglomeration 171   
组合最优原理 Combinatorial Optimization Principle 138   
最大公约数(GCD)测试 Greatest Common Divisor Testing 380   
最坏情况下的复杂度 Worst-Case Complexity 109   
坐标存储法 Coordinate Storage Scheme 241

Document generated by Anna's Archive around 2023-2024 as part of the DuXiu collection (https://annas-blog.org/duxiu-exclusive.html).

Imageshavebeenlossessyembedded.Informationabout theoriginalfilecanbefoundinPDFatachments.Some stats(more inthe PDF attachments):

"filename": "MTA5MDA0NjMuemlw",   
"filename_decoded": "10900463.zip",   
"filesize": 34580177,   
"md5": "23743fe1894cee9603b395275fbc0034",   
"header_md5": "e8c3a03a5d7c3c29ef1606723c99b0bd",   
"sha1": "c43f2f386aaed8e09930c4510da20caac92ba671",   
"sha256": "6a42828d03a84c1f02131e34a8b34539993f5612fc62b2cdb87876e4cd64bf7b",   
"crc32": 3910169147,   
"zip_password":"",   
"uncompressed_size": 36588852,   
"pdg_dir_name": "10900463",   
"pdg_main_pages_found": 431,   
"pdg_main_pages_max": 431,   
"total_pages": 450,   
"total_pixels": 2400007680,   
"pdf_generation_missing_pages": false
