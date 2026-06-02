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

![](images/cb8dabaad36d163e0724cea0f9f395488e8dd6d3eb1084206e3a0aa8b8ed693b.jpg)

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

![](images/25d2e14fa7057f930ec69fdecad152db6da59c000c6b228c303981c36584e00b.jpg)  
图1.1HPCC方面的重大挑战性课题的需求

美国ASCI计划全面禁止核试验条约签订后，核武器的研究代之以实验室数值模拟。因此禁试后数值模拟成了唯一可能进行的全系统(虚拟)试验。这样,1996年6月由美国能源部联合美国三大核武器实验室(LawrenceLivermore国家实验室、Los Alamos国家实验室和Sandia国家实验室)共同提出了“加速战略计算创新"（Accelerated Strategic Computing Initiative,简称为 ASCI)项目计划。提出通过数值模拟,评估核武器的性能、安全性、可靠性、更新等。要求数值模拟达到高分辨率、高逼真度、三维、全物理、全系统的规模和能力。该计划被认为是与当年曼哈顿计划等同的一个巨大的挑战,不仅需要科学界的参与，也需要计算机工业界合作,提供保障ASCI应用所需的计算机平台。为此,三大核武器实验室分别向美国三大公司(Intel、IBM和SGI/CRAY)预定了峰值速度超过1Tflops的并行计算机。美国能源部计划在2003年要使用运算速度为100Tflops、内存容量为50TB的并行机（见表1.2)。目前ASCI计划正把各项应用需求与计算平台推进到万亿级规模的体系中去（即每秒可执行万亿次浮点运算，万亿个字节的RAM,数十万亿个字节的磁盘,千万亿个字节的档案存储器,数百亿个字节的网络带宽)。

表1.2 美国ASCI计划中的并行机一览表  

<table><tr><td rowspan=1 colspan=1>时间（年）</td><td rowspan=1 colspan=1>运算速度(OPS)</td><td rowspan=1 colspan=1>存储容量(TB)</td><td rowspan=1 colspan=1>海存容量(PB)</td><td rowspan=1 colspan=1>I/O传输率(GB/s)</td><td rowspan=1 colspan=1>网络传输率(GB/s)</td></tr><tr><td rowspan=1 colspan=1>1996</td><td rowspan=1 colspan=1>1011</td><td rowspan=1 colspan=1>0.05</td><td rowspan=1 colspan=1>0.13</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>0.13</td></tr><tr><td rowspan=1 colspan=1>1997</td><td rowspan=1 colspan=1>1012</td><td rowspan=1 colspan=1>0.5</td><td rowspan=1 colspan=1>1.3</td><td rowspan=1 colspan=1>50</td><td rowspan=1 colspan=1>1.3</td></tr><tr><td rowspan=1 colspan=1>2000</td><td rowspan=1 colspan=1>1013</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>13</td><td rowspan=1 colspan=1>500</td><td rowspan=1 colspan=1>13</td></tr><tr><td rowspan=1 colspan=1>2003</td><td rowspan=1 colspan=1>1014</td><td rowspan=1 colspan=1>50</td><td rowspan=1 colspan=1>130</td><td rowspan=1 colspan=1>5000</td><td rowspan=1 colspan=1>130</td></tr></table>

# \*1.1.3万亿次高端并行机

ASCIOption Red 是由Intel 公司和 Sandia国家实验室联合研制的一台MPP(Massively Parallel Processors)系统,完成于1997年6月,是世界上第一台万亿次的高端并行机,其I/O、存储器、计算节点与通信等性能都能被扩展到一个很高的水平，标准的并行接口可使用户较容易地把各种并行应用程序移植到该系统上。该系统使用两种操作系统，既配置用户很熟悉的Unix，又具备不是非法装人的适用于可扩展应用程序的Cougar系统。该系统使用CCOTS(Com-mercial Commodity Off The Shelf)技术,以降低系统维护费用。

系统结构 如图1.2所示,Option Red 是一台分布存储的 MPP系统，它由四部分构成：计算节点、服务节点、系统节点和I/O节点。其中,计算节点用于并行应用程序的执行;服务节点用于支持登录、软件开发和其它交互操作；I/O节点用于访问磁盘、磁带、网络(Ethernet、FDDI、ATM等)和其它I/O设备；系统节点用于支持系统的RAS(Reliability、Availability、Serviceability)能力。该系统的硬件参数列于表1.3中,其中 RAID(Redundant Array of Inexpensive Disk)是廉价冗余磁盘阵列。

![](images/57dd16e7ed724552f2baea5873ffcd95aa78519224af94d4254403a46b8c61e4.jpg)  
图1.2ASCI Option Red 系统结构

表1.3Option Red 系统硬件参数一览表  

<table><tr><td rowspan=1 colspan=1>名       称</td><td rowspan=1 colspan=1>参       数</td></tr><tr><td rowspan=1 colspan=1>计算节点</td><td rowspan=1 colspan=1>4 536</td></tr><tr><td rowspan=1 colspan=1>服务节点</td><td rowspan=1 colspan=1>32</td></tr><tr><td rowspan=1 colspan=1>硬盘I/O节点</td><td rowspan=1 colspan=1>24</td></tr><tr><td rowspan=1 colspan=1>系统节点(引导与节点站)</td><td rowspan=1 colspan=1>2</td></tr><tr><td rowspan=1 colspan=1>网络节点(Ethernet,ATM)</td><td rowspan=1 colspan=1>6</td></tr><tr><td rowspan=1 colspan=1>系统基座面积</td><td rowspan=1 colspan=1>1 000in²</td></tr><tr><td rowspan=1 colspan=1>机柜数</td><td rowspan=1 colspan=1>85</td></tr><tr><td rowspan=1 colspan=1>系统RAM</td><td rowspan=1 colspan=1>594 MB</td></tr><tr><td rowspan=1 colspan=1>拓扑结构</td><td rowspan=1 colspan=1>38×32×2</td></tr><tr><td rowspan=1 colspan=1>节点到节点带宽(双向）</td><td rowspan=1 colspan=1>800 MB/s</td></tr><tr><td rowspan=1 colspan=1>交叉段(Section）带宽</td><td rowspan=1 colspan=1>51.6 GB/s</td></tr><tr><td rowspan=1 colspan=1>Pentiumpro处理器数</td><td rowspan=1 colspan=1>9 216</td></tr><tr><td rowspan=1 colspan=1>处理器到存储器带宽</td><td rowspan=1 colspan=1>533 MB/s</td></tr><tr><td rowspan=1 colspan=1>计算节点峰值速度</td><td rowspan=1 colspan=1>400 Mflops</td></tr><tr><td rowspan=1 colspan=1>系统峰值性能</td><td rowspan=1 colspan=1>1.8 Tflops</td></tr><tr><td rowspan=1 colspan=1>RAID存储器(每个子系统)</td><td rowspan=1 colspan=1>1 TB</td></tr><tr><td rowspan=1 colspan=1>RAIDI/O带宽(每个子系统）</td><td rowspan=1 colspan=1>1.0 GB/s</td></tr></table>

系统软件 ASCI Option Red 的系统软件是从 Paragon 环境演变而来的。其中,系统、服务和I/O节点运行Paragon操作系统,它是一个基于OSF 的分布式Unix系统;计算节点运行Cougar操作系统,它是从Intel公司的Puma移植来的,是一个轻量级核 LWK(Light-Weight Kernel)。LWK 由两层组成:PCT(Pro-cess Control Thread)和Q-Kernel(Quintessential Kernel)。如图1.3 所示,每个节点都有一些用户进程、一个 PCT 和一个Q-Kermel。Q-Kernel 是唯一能直接访问地址映射和通信硬件的软件，它提供基本计算、通信和地址空间保护等功能；而PCT提供进程管理、名字服务和组保护(Group Protection)等功能。在Cougar 中的基本程序设计模式是建立在消息传送的基础上的。

![](images/f56c3403212a802fcc9e9132a1b696dca2465697c777aca0680b36620a0b59e8.jpg)  
图1.3LWK(Cougar)层结构

Red系统支持FORTRAN77、FORTRAN90、C与C++,并提供查错程序和性能分析工具等。

# 1.2 并行计算机系统互连

# 1.2.1系统互连

在多处理机、多计算机或分布式系统中，不同组成部分（CPU、存储模块、I/O设备、网络接口等）都要通过互连网络彼此连接起来。图1.4示出了当今不同网络拓扑和互连技术的关系图。其中，水平轴自左至右网络距离逐渐增加，垂直轴代表单位时间网络可传输的最大信息量。参照图1.5，一个系统域网络SAN(SystemAreaNetwork)可以将短距离(3～25m）内的不同节点连接起来形成单一系统；该系统可用于一个建筑物、校园或企业(500m～2km)内的局城网络LAN(LocalAreaNetwork)相连构成一个完整系统。在每个节点内，处理器芯片管脚形成了处理器总线；局部（本地）总线，存储器总线，将处理器与存储模块相连；I/O总线，系统总线，将I/O设备、网卡等连接起来(I/O总线有时也叫作小型机系统接口 SCSI(Small Computer System Interface)总线）。一个都域网MAN(MetropolitanArea Network)可以覆盖整个城市(≥25km)；而一个广域网WAN(WideAreaNetwork)甚至可覆盖全球，但本书不讨论它们,只讨论到LAN这一级,因为在构成网络工作站机群COW(Clusterof Workstations)时会用到LAN技术。下面将着重讨论节点内处理器、存储器和I/O设备之间的互连，包括静态互连网络和动态互连网络;而对构成高端并行计算机所需的宽带 SAN/LAN 网络技术只作简要介绍。

![](images/6cee87c19e09bef1e3f284031117a08fbac0fb645b40cb53572497ca7af7fbc5.jpg)  
图1.4系统互连和网络拓扑

![](images/02abd50d75145143e189057bdf889ca79a63406f833dcedb16d8b007d32fe5f4.jpg)  
图1.5图示局部总线、I/O总线、SAN和 LAN

# 1.2.2静态互连网络

所谓静态网络(StaticNetworks)是指处理单元间有着固定连接的一类网络,在程序执行期间,这种点到点的链接保持不变;相反,动态网络(DynamicNetworks)是用开关单元构成的,可按应用程序的要求动态地改变连接组态。典型的静态网络有一维线性阵列、二维网孔、树连接、超立方网络、立方环、洗牌交换网、蝶形网络等;典型的动态网络包括总线、交叉开关和多级互连网络等。为讨论方便,兹作如下定义：

定义1.1 射人或射出一个节点的边数称为节点度(Node Degree)。在单向网络中,人射和出射边之和称为节点度。

定义1.2网络中任何两个节点之间的最长距离,即最大路径数,称为网络直径(Network Diameter）。

定义1.3对分网络各半所必须移去的最少边数称为对剖宽度（BisectionWidth)。

定义1.4如果从任一节点观看网络都一样,则称网络为对称的(Symmetry)。

一维线性阵列(1-DLinearArray）它是并行机中最简单、最基本的互连方式,其中每个节点只与其左、右近邻相连,故也叫二近邻连接。N个节点用N－1条边串接之,内节点度为2,直径为N-1,对剖宽度为1。当首、尾节点相连时可构成循环移位器,在拓扑结构上等同于环,环可以是单向的或双向的,其节点度恒为2,直径或为LN/2」(双向环)或为N-1(单向环),对剖宽度为2。

二维网孔 $( 2 - \mathrm { D } \mathrm { M e s h } )$ 在一个 $\sqrt { N } \times \sqrt { N }$ 的二维网孔网络中，每个节点只与其上、下、左、右的近邻相连(边界节点除外),故也称四近邻连接,因而节点度为4,网络直径为 $2 ( \sqrt { N } - 1 )$ ,对剖宽度为 $\sqrt { N }$ (见图1.6(a))。如果在垂直方向上带环绕,而水平方向呈蛇状,则2-D网孔就变成 Illiac 网孔了(见图1.6(b)),此时节点度恒为4,网络直径为 $\sqrt { N } - 1$ ，而对剖宽度为 $2 \sqrt { N }$ 。如果2-D网孔的垂直和水平方向均带环绕,则它就变成了2－D环绕(2-D Torus)（见图1.6(c)),其节点度恒为4,而网络直径为 $2 \lfloor \sqrt { N } / 2 \rfloor$ ，对剖宽度为 $2 \sqrt { N }$ 。

![](images/e3e0c2655dce05a53f6ad6ef8554942c77c6ea1123bf20c546715b40006f5fd0.jpg)  
图1.6四近邻连接

(a)2-D网孔；(b)lliac 网孔； $( { \mathsf { c } } ) 2 - { \mathsf { D } }$ 环绕

树二叉树除了根节点和叶节点之外,每个内节点只与其父节点和两个子节点相连,故也称为三近邻连接。如图1.7(a)所示,显然节点度为3，对剖宽度为1,而树的直径为 $2 ( \lceil \log N \rceil - 1 )$ （ $N$ 为树的总节点数)。为了减小直径，可使用X-树,将同级的兄弟节点彼此相连。如果尽量增大节点度为 $N - 1$ ,则直径缩小为2,此时就变成了如图1.7(b)所示的星形网络了，其对剖宽度为 $\lfloor N / 2 \rfloor$

![](images/28a6fcc6219566f9e1217f2a1557486ef110f0d66d30bfcf9530c30c595a8752.jpg)  
图1.7树形连接  
(a)二叉树；(b)星形连接；(c)二叉胖树

传统二叉树的主要问题是根易成为通信瓶颈。1985年Leiserson[119]提出的胖树(Fat Tree)可缓解此问题。如图1.7(c)所示，胖树节点间的通路自叶向根逐渐变宽，它更像真实的树，连向根部的枝叉变得愈来愈粗。

超立方一个 $_ n -$ 立方由 $N { } = 2 ^ { n }$ 个顶点组成。3-立方如图1.8(a)所示；4-立方如图 $1 . 8 ( { \mathfrak { b } } )$ 所示，由两个3一立方的对应项点连接而成。 $_ { n } -$ 立方的节点度为 $\pmb { n }$ ,网络直径也是 $\pmb { n }$ ,而对剖宽度为 $N / 2$ 。由于该网络缺乏可扩放性和不易构成多维超立方，所以它正逐渐被其它的网络所代替。但过去在超立方上开发了很多优秀的算法，而像二叉树、网孔和很多其它低维网络均能嵌入超立方中，所以超立方具有学术研究的意义。如果将3-立方的每个顶点代之以一个环就构成了如图1.8(d)所示的3-立方环,此时每个顶点的度为3,而不像超立方那样节点度为 $\pmb { n } \circ$ 一般而言,可以从一个 $k ^ { - }$ 立方构成一个具有 $n = 2 ^ { k }$ 个带环顶点(每个顶点是 $\pmb { k }$ 个连成环的节点）的 $k -$ 立方环,此时 $\pmb { k } -$ 立方环中总共有 $N = k \cdot 2 ^ { k }$ 个节点 $( k \geqslant 3 )$ ，网络直径为 $2 k - 1 + \lfloor k / 2 \rfloor$ ，而对剖宽度为 $N / ( 2 k )$

![](images/4751382b4ed8eb6f324c3bd2e8a9dd575e9b1ea1cd80bb9c2bd97ac24d848ab2.jpg)  
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

![](images/70df07f7eac6436e4da041218c5302b56bf9e28999264756cc6731c88082c190.jpg)  
图1.9板级、底板级和I/O级总线系统

设计多处理器总线系统的主要问题包括总线仲裁、中断处理、协议转换、快速同步、缓存一致性协议、总线桥接和层次总线的扩展等。通常,监听协议(SnoopyProtocol)均内置在多处理器总线中;硬件路障同步也常使用在多处理器总线中。

交叉开关交叉开关(Crossbar Switcher)是一种高带宽网络。像电话交换机一样,交叉点开关能在(源;目的)对之间建立动态连接。每个交叉点开关为一个(源;目的)对提供一条专用连接通路,其开关状态可根据程序的要求动态地置为"开"或"关”。图1.10是一个 $4 \times 4$ 的交叉开关,其中每个输人口有一接收器和输入缓冲器,以处理到达的请求;每个输出口有一个发送器，以传递输出数据信号至一条通信链上;开关控制仲裁开关的"开/关"状态。

![](images/3e717c35dd99505fc57c61da57a56f84d985b1cf27c47c354a392d8c6eb8027b.jpg)  
图1.10 $4 \times 4$ 的交叉开关

在并行处理中,交叉开关的使用通常有两种方式：一种是用于处理器之间的通信,此时每一行和每一列只能接通一个交叉点开关,所以一个 $\mathbf { \Omega } _ { n } \times \mathbf { \Omega } _ { n }$ 的交叉开关网络一次最多可接通 $_ n$ 个对；另一种是用于处理器和存储模块之间的通信,此时每个存储模块一次只能由一个处理器请求访问,所以每一列中只能接通一个交叉点开关,但为了支持并行(或交叉)存储访问,每一行可同时接通多个交叉点开关。

一般而言,交叉开关的成本为 $n ^ { 2 }$ ,其中 $_ n$ 为端口数,这样就限制了它在大型系统中的应用。

多级互连网络为了构筑大型开关网络，常可将单级交叉开关级联起来形成一个多级互连网络 MIN（Multistage Interconnection Network）,它已被用在MIMD和SIMD并行机中。一种通用多级互连网络如图1.11所示,其中每一级都用了多个a×b开关单元,相邻各级之间有着固定的级联拓扑。为了在输入和输出之间建立所需的连接，可以动态设置开关状态。

![](images/736ccf229adcbe5dc4d869131c9be6ff95fe1b193e4303418941b09c8f17a0ba.jpg)  
图1.11通用多级互连网络结构

目前已经提出了很多MIN,其差别就在于开关单元及其级间连接(ISC)方式不同。最简单的开关单元是2×2的开关单元;常用的ISC模式有均匀洗牌、蝶式、纵横交叉等。图1.12(e)就是著名的Ω网络,其中2×2的开关单元可有如图1.12(a)、(b)、(c)、(d)四种连接方式,而ISC是均匀洗牌连接模式。

对于一个n输人和n输出的Ω网络,共有logn级,每级包括n/2个开关单元,所以共有logn个开关单元。其它的MIN,还有基准网络、二进制立方网络和 Benes 网络等。

动态互连网络小结表1.5汇总了动态互连网络的重要特性。显然，总线造价最低,但易冲突；交叉开关造价最高，但带宽和选路性能最好;多级互连网络是总线与交叉开关的折衷,主要优点采用模块结构，可扩展性好，但延迟随网络尺寸对数增长。

![](images/a05775374743887ef1b4725f16e5f2c6fb1c6cfc3fa9fe745e2cd59fbb039834.jpg)  
图1.12 $\pmb { \Omega }$ 网络

(a)直通；（b)交叉：(c)上播；（d)下播； $( { \bf e } ) 1 6 \times 1 6$ 的 $\pmb { \Omega }$ 网络

表1.5动态互连网络特性一览表  

<table><tr><td rowspan=1 colspan=1>网络特性</td><td rowspan=1 colspan=1>总线系统n台处理器，总线宽度为ε位</td><td rowspan=1 colspan=1>多级互连网络nXnMIN采用k×k开关,线宽为ω位</td><td rowspan=1 colspan=1>交叉开关n×n交叉开关线宽为ω位</td></tr><tr><td rowspan=1 colspan=1>最小时延</td><td rowspan=1 colspan=1>恒定(轻负载)</td><td rowspan=1 colspan=1>O(nlogkn)</td><td rowspan=1 colspan=1>恒定</td></tr><tr><td rowspan=1 colspan=1>每台处理器带宽</td><td rowspan=1 colspan=1>O(w/n)至0(ω)</td><td rowspan=1 colspan=1>O(ω)至0(nw)</td><td rowspan=1 colspan=1>O(w)至0(nw)</td></tr><tr><td rowspan=1 colspan=1>开关复杂性</td><td rowspan=1 colspan=1>0(n)</td><td rowspan=1 colspan=1>O(nlogkn)</td><td rowspan=1 colspan=1>O(n²）</td></tr><tr><td rowspan=1 colspan=1>连线复杂性</td><td rowspan=1 colspan=1>0(ω)</td><td rowspan=1 colspan=1>O(nwlogkn)</td><td rowspan=1 colspan=1>O(n²ω)</td></tr><tr><td rowspan=1 colspan=1>连接特性</td><td rowspan=1 colspan=1>一次只能一对一</td><td rowspan=1 colspan=1>是阻塞型网络</td><td rowspan=1 colspan=1>全置换</td></tr></table>

# 1.2.4宽带互连网络

本节所介绍的高速宽带互连技术,对构筑一个分布式网络计算环境是十分有用的,这些互连技术均有普遍被接受的协议标准。

FDDI光纤分布式数据接口 FDDI(Fiber Distributed Data Interface)采用双向光纤令牌环可提供100～200Mb/s数据传输。彼此相反方向的双向环可提供冗余通路以提高可靠性。它能够连接大量的设备，其距离可达100m（使用铜线）、2km(使用多模式光纤)和60km(使用单模式光纤）,这使得有可能在LAN和 MAN中应用FDDI环。FDDI集中器采用孤立故障的办法可使网络更可靠。

100 Mb/s主干FDDI网络如图1.13所示。其中专门的路由器将 FDDI环连向以太集线器,后者可连接大量的桌面计算机。FDDI环可确保加入、删除、移动主机或设备而不会使网络崩溃。

![](images/bc3e9f377e8dbf6eb6e2c2352f949ffd8e7d63c86756b0a444ba3835387298eb.jpg)  
图1.13双向FDDI环作为主干网

FDDI的缺点是不能支持多媒体信息流，这就减弱了它与ATM技术的竞争力,但使用全双工模式的 FDDI(即FFDT)可以增强 FDDI的竞争力。

快速以太网以太网已历经三代：1982年引入的10 Mb/s网属第一代以太网;1994年宣布的100 Mb/s快速网属第二代以太网；1997年IEEE802.3工作.组宣布的1Gb/s千兆位网可谓第三代以太网，其特性汇总于表1.6中。

图1.14示出了如何由开关快速以太主干网升级到千兆位主干LAN。

MyrinetMyrinet是由Myricom公司生产的千兆位包开关网，其目的是互连商用产品以构筑计算机群,常用来构造机箱内SAN机群或基于LAN的桌面系统。Myrinet定义在数据链路层，包的长度可变,在每条链路上施行流控和差错控制，使用切通选路法和定制的可编程主机接口。图1.15示出了用4个Myrinet开关构造MyrinetLAN(连接工作站、PC)桌面系统、机箱内多机机群和单板多处理器机群。

表1.6三代以太网特性一览表  

<table><tr><td rowspan=1 colspan=2>代别(类型）</td><td rowspan=1 colspan=1>以太网10 BaseT</td><td rowspan=1 colspan=1>快速以太网100 BaseT</td><td rowspan=1 colspan=1>千兆位以太网1 Gb</td></tr><tr><td rowspan=1 colspan=2>引人年代</td><td rowspan=1 colspan=1>1982</td><td rowspan=1 colspan=1>1994</td><td rowspan=1 colspan=1>1997</td></tr><tr><td rowspan=1 colspan=2>速度(带宽)</td><td rowspan=1 colspan=1>10 Mb/s</td><td rowspan=1 colspan=1>100 Mb/s</td><td rowspan=1 colspan=1>1 Gb/s</td></tr><tr><td rowspan=4 colspan=1>最大距离</td><td rowspan=1 colspan=1>非屏蔽双扭对</td><td rowspan=1 colspan=1>100 m</td><td rowspan=1 colspan=1>100 m</td><td rowspan=1 colspan=1>25～100 m</td></tr><tr><td rowspan=1 colspan=1>屏蔽双扭对/同轴电缆</td><td rowspan=1 colspan=1>500 m</td><td rowspan=1 colspan=1>100 m</td><td rowspan=1 colspan=1>25~100 m</td></tr><tr><td rowspan=1 colspan=1>多模式光纤</td><td rowspan=1 colspan=1>2 km</td><td rowspan=1 colspan=1>412m(半双工）2 km(全双工）</td><td rowspan=1 colspan=1>500 m</td></tr><tr><td rowspan=1 colspan=1>单模式光纤</td><td rowspan=1 colspan=1>25 km</td><td rowspan=1 colspan=1>20 km</td><td rowspan=1 colspan=1>2 km</td></tr><tr><td rowspan=1 colspan=2>主要应用领域</td><td rowspan=1 colspan=1>文件共享,打印机共享等</td><td rowspan=1 colspan=1>COW 计算,C/S结构,大型数据库等</td><td rowspan=1 colspan=1>大型图像文件，多媒体,因特网，内部网,数据仓库等</td></tr></table>

![](images/b23d642c549b6e14dad252f8b5be1a113ec4048b14b5ca6c228ae04ba5cd8ca4.jpg)  
图1.14千兆位以太主干网的构造

总之,Myrinet支持机群计算具有很大的潜力。但与总线有关的主机界面仍限制大量不同的主机连向Myrinet,其短于25m的电缆(使用铜线)使Myrinet作为SAN 使用受到了限制。

HiPPI 高性能并行接口HiPPI(High Performance Parallel Interface)已广泛用来构筑异构计算机系统，它是LosAlamos国家实验室1987年提出的一个标准,其目的是试图统一不同厂商的所有大型机和超级计算机的界面。HiPPI曾被大型机和超级计算机工业界作为高速I/O通道用于短距离的系统到系统和系统到外设的连接。1993年,ANSIX3T9.3批准了HiPPI标准，它覆盖了物理和数据链路层,而高层的东西留给了用户。

![](images/7cceb97acaa0a0fe89cf896682d2b1769b4fdd02b3a7516d383c5a1a2869a7c4.jpg)  
机箱内多计算机机群  
图1.154个8端口开关构筑的Myrinet群集

HiPPI是一个单工点到点的数据传输界面，其速度可达 $8 0 0 ~ \mathrm { M b / s }$ 到1.6Gb/s。随着工艺的进展和价格的降低,HiPPI已不再只为超级计算机所用。

图1.16展示出用HiPPI交叉开关连接各种大型机、服务器和超级计算机的LAN主千网。

![](images/baa559b24ff425fb3c03cdc206537d8b53951296191b0432025e09b0390ea3fb.jpg)  
图1.16使用HiPPI通道和开关构筑的LAN主干网

ATM异步传输模式 ATM(Asynchronous Transfer Mode)是在光纤通信基础上建立起来的一种新的宽带综合业务数字网(B-ISDN)的交换技术。根据CCITT1998年发表的蓝皮书1.121建议，它将是建立一个统一通信网络的最终解决方案。ATM是一种与介质无关的信息传输协议，采用53个字节的定长短数据单元(信元,Cell)进行传输。按此,如图1.17所示，一个长的包(Packet）经ATM网络传输之前须破成一些小的信元，在接收端再将它们重装起来。这些小的信元,可以使用逐段 $( { \mathrm { H o p } } - { \mathrm { b y } } - { \mathrm { H o p } } )$ 法进行选路。ATM网可以高速传输诸如声音、图像、视频和数据等所有形式的媒体;它可以加人到现存的LAN、MAN和WAN 中。

![](images/1cab50f7bf867b044de5c00a72d651952a042559e94aaf572d306e01c3718b7e.jpg)  
图1.17ATM网中的信元传输

ATM采用4层体系结构,它与 OSI(Open Systems Interoonnection)标准对应关系示于表1.7中。其中,CS(Convergence Sublayer)是汇聚子层;SAR(Segmentationand Reassembly Sublayer）是分段与组装子层；TC（Transmission ConvergenceSublayer)是传输汇聚子层;PMD(Physical Medium Dependent Sublayer)是物理介质相关子层和 AAL(ATM Adaptation Layer)是 ATM适配层。

表1.7ATM与OSI标准对应关系一览表  

<table><tr><td rowspan=1 colspan=1>OSI层</td><td rowspan=1 colspan=1>ATM层</td><td rowspan=1 colspan=1>·ATM子层</td><td rowspan=1 colspan=1>基本功能</td></tr><tr><td rowspan=2 colspan=1>3/4</td><td rowspan=2 colspan=1>AAL</td><td rowspan=1 colspan=1>CS</td><td rowspan=1 colspan=1>提供汇聚标准界面</td></tr><tr><td rowspan=1 colspan=1>SAR</td><td rowspan=1 colspan=1>分段和装配</td></tr><tr><td rowspan=1 colspan=1>2/3</td><td rowspan=1 colspan=1>ATM</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>流控,信元头的产生/消除，虚电路/路径的管理，信元的多路复用/分配</td></tr><tr><td rowspan=2 colspan=1>21</td><td rowspan=2 colspan=1>物理层</td><td rowspan=1 colspan=1>TC</td><td rowspan=1 colspan=1>信元速率匹配，信元的产生、打包/拆包，头检查和产生/验证</td></tr><tr><td rowspan=1 colspan=1>PMD</td><td rowspan=1 colspan=1>位定时，物理网络访问</td></tr></table>

如图1.18所示,ATM网络的端点设备通过用户网络接口UNI(User-Net-workInterface)连到ATM交换机上。一个网络可以有多个ATM交换设备，这些交换机连接在一起可形成更大的网络。ATM交换设备之间的接口称为网络到网络接口NNI(Network-Network Interface)。利用ATM技术可以构成宽带LAN主干网，其中交换机连接路由器和服务器，提供了可扩放和高带宽的交换能力，而高性能的服务器可直接与ATM交换机相连。也可以用ATM作为桌面网络技术组成高速用户机群局域网，然后通过路由器可以把ATM局域网与传统的主干网相连。ATM作为B-ISDN的交换技术,还可提供基于ATM的MAN/WAN的体系结构。

图1.19所示是一个基于ATM的多计算机机群实例,它由香港大学开发，专门应用于分布式多媒体和元计算（Metacomputing）。其中,HARNET代表Hong Kong Academic Research Net; IMSC 代表 Integrated Multimedia SystemCenter;WS 代表 Workstation;PC 代表 Personal Computer。

![](images/055079752b511d8835aa9cc1613295cc433ba2c8431581211f5b475446fa53de.jpg)  
图1.18 ATM网络中的UNI和 NNI

![](images/436ee088beac495753f0ed05f9abc278b9a2a181c38e9e08961d78c7a58ded41.jpg)  
图1.19香港大学开发的珍珠机群

# 1.3 并行计算机系统结构

# 1.3.1并行计算机结构模型

大型并行机系统一般可分为6类：单指令多数据流机SIMD(Single-Instruc-tion Multiple-Data);并行向量处理机 PVP(Paralel Vector Processor);对称多处理机SMP(Symmetric Multiprocessor);大规模并行处理机 MPP(Massively Paral-lel Processor);工作站机群 COW(Cluster of Workstation)和分布共享存储 DSM(Distributed Shared Memory)多处理机。SIMD计算机多为专用,其余的5种均属于多指令多数据流 MIMD(Multiple-Instruction Multiple-Data)计算机。5种MIMD并行机的结构模型示于图1.20。其中B(Bridge)是存储总线和I/O总线间的接口,DIR(Cache Directory)是高速缓存目录,IOB(I/O Bus)是I/O总线,

LD(Local Disk)是本地磁盘，MB（Memory Bus）是存储器总线,NIC(NetworkInterface Circuitry)是网络接口电路,P/C(Microprocessor and Cache)是微处理器和高速缓存 SM(Shared Menory)是共享存储器。目前绝大多数近代并行机均用商品硬件构成,而PVP计算机的部件很多都是定制(Custom-Made)的。

![](images/7bbbace2671399036b1214faf44b6e9d9be83e08433edae2b79cee2bcf1c81b0.jpg)  
图1.205种并行机结构模型(a)PVP；（b)SMP；(c)MPP；(d)DSM；(e)COW

PVP典型的并行向量处理机的结构示于图1.20（a)。Cray C-90、CrayT-90、NEC SX-4和我国的银河1号等都是PVP。这样的系统中包含了少量的高性能专门设计定制的向量处理器VP,每个至少具有1Gflops的处理能力。系统中使用了专门设计的高带宽的交叉开关网络将VP连向共享存储模块，存储器可以兆字节每秒的速度向处理器提供数据。这样的机器通常不使用高速缓存，而是使用大量的向量寄存器和指令缓冲器。

SMP对称多处理机的结构示于图1.20(b)。IBMR50、SGI Power Chal-lenge、DECAlpha服务器 8400 和我国的曙光1号等都是这种类型的机器。SMP系统使用商品微处理器(具有片上或外置高速缓存),它们经由高速总线(或交叉开关)连向共享存储器。这种机器主要应用于商务，例如数据库、在线事务处理系统和数据仓库等。重要的是系统是对称的，每个处理器可等同的访问共享存储器、I/O设备和操作系统服务。正是对称，才能开拓较高的并行度;也正是共享存储，限制系统中的处理器不能太多(一般少于64个),同时总线和交叉开关互连一旦作成也难于扩展。

MPP大规模并行处理机的结构示于图 $1 . 2 0 ( \mathrm { c } )$ 。Intel Paragon、IBM SP2、IntelTFLOPS和我国的曙光-1000等都是这种类型的机器。MPP一般是指超大型(VeryLarge-Scale)计算机系统,它具有如下特性： $\textcircled{1}$ 处理节点采用商品微处理器； $\textcircled{2}$ 系统中有物理上的分布式存储器； $\textcircled{3}$ 采用高通信带宽和低延迟的互连网络(专门设计和定制的）； $\textcircled{4}$ 能扩放至成百上千个处理器; $\textcircled{5}$ 它是一种异步的MIMD机器,程序系由多个进程组成,每个都有其私有地址空间,进程间采用传递消息相互作用。MPP的主要应用是科学计算、工程模拟和信号处理等以计算为主的领域。

DSM分布式共享存储多处理机的结构示于图1.20(d)。Stanford DASH、Cray T3D和 SGI/Cray Origin2000 等属于此类结构。高速缓存目录DIR用以支持分布高速缓存的一致性。DSM和 SMP的主要差别是,DSM在物理上有分布在各节点中的局存从而形成了一个共享的存储器。对用户而言，系统硬件和软件提供了一个单地址的编程空间。DSM相对于MPP的优越性是编程较容易。

COW工作站机群的结构示于图1.20(e)。Berkeley NOW、Alpha Farm、DigitalTrucluster等都是COW结构。在有些情况下,机群往往是低成本的变形的MPP。COW的重要界线和特征是： $\textcircled{1} \mathrm { C O W }$ 的每个节点都是一个完整的工作站(不包括监视器、键盘、鼠标等),这样的节点有时叫作"无头工作站”,一个节点也可以是一台PC 或 SMP; $\textcircled{2}$ 各节点通过一种低成本的商品网络(如以太网、FDDI和ATM开关等)互连(有的商用机群也使用定做的网络）； $\textcircled{3}$ 各节点内总是有本地磁盘,而MPP节点内却没有； $\textcircled{4}$ 节点内的网络接口是松散耦合到I/O总线上的,而MPP内的网络接口是连到处理节点的存储总线上的,因而可谓是紧耦合式的； $\textcircled{5}$ 一个完整的操作系统驻留在每个节点中，而MPP中通常只是个微核,COW的操作系统是工作站UNIX,加上一个附加的软件层以支持单一系统映像、并行度、通信和负载平衡等。

现今,MPP和COW 之间的界线越来越模糊。例如,IBM SP2它虽视为MPP,但它却有一个机群结构。机群相对于MPP有性能/价格比高的优势，所以在发展可扩放并行计算机方面呼声很高。

公用结构 SMP、MPP、DSM和 COW 等并行结构渐趋一致,DSM是 SMP和MPP的自然结合,MPP和COW的界线逐渐不清,它们最终的结构趋向一致,形成当代并行机的公用结构(图1.21)。在这样的系统结构中,大量的节点可通过高速网络互连起来。节点通常遵循着一个Shell结构（ShellArchitec-ture),其中一个专门设计定制的电路(叫作 Shell)将商品微处理器和其余的节点,包括板级高速缓存、局存、NIC和磁盘连接起来。在一个节点内可有不止一个处理器。这种 Shell结构的优点是，当处理器芯片更新换代时只需改变 Shell。图1.21中示出了三种不同的共享结构,其中将无共享结构图(a)中节点内的磁盘(D)移出来就形成了共享磁盘的结构图(b),再把主存(M)移出来就变成了共享存储结构图(c)。

![](images/cb5816d9367a7889ff95e4133f9b6b2581ea8b9807b949ce0ff744712c07e220.jpg)  
图1.21可扩放并行机公用结构(a)无共享；(b)共享磁盘；(c)共享存储

小结表Ⅰ.8汇总了上述5种结构的特性比较，其中有关访存模型解释见第1.3.2节。

表1.85种结构特性一览表  

<table><tr><td rowspan=1 colspan=1>属性</td><td rowspan=1 colspan=1>PVP</td><td rowspan=1 colspan=1>SMP</td><td rowspan=1 colspan=1>MPP</td><td rowspan=1 colspan=1>DSM</td><td rowspan=1 colspan=1>Cow</td></tr><tr><td rowspan=1 colspan=1>结构类型</td><td rowspan=1 colspan=1>MIMD)</td><td rowspan=1 colspan=1>MIMD</td><td rowspan=1 colspan=1>MIMI)</td><td rowspan=1 colspan=1>MIMD</td><td rowspan=1 colspan=1>MIMD</td></tr><tr><td rowspan=1 colspan=1>处理器类型</td><td rowspan=1 colspan=1>专用定制</td><td rowspan=1 colspan=1>商用</td><td rowspan=1 colspan=1>商用</td><td rowspan=1 colspan=1>商用</td><td rowspan=1 colspan=1>商用</td></tr><tr><td rowspan=1 colspan=1>互连网络</td><td rowspan=1 colspan=1>定制交叉开关总线、交叉开关</td><td rowspan=1 colspan=1>定制交叉开关总线、交叉开关</td><td rowspan=1 colspan=1>定制网络</td><td rowspan=1 colspan=1>定制网络</td><td rowspan=1 colspan=1>商用网络（以太ATM）</td></tr></table>

续表

<table><tr><td rowspan=1 colspan=1>属性</td><td rowspan=1 colspan=1>PVP</td><td rowspan=1 colspan=1>SMP</td><td rowspan=1 colspan=1>MPP</td><td rowspan=1 colspan=1>DSM</td><td rowspan=1 colspan=1>cow</td></tr><tr><td rowspan=1 colspan=1>通信机制</td><td rowspan=1 colspan=1>共享变量</td><td rowspan=1 colspan=1>共享变量</td><td rowspan=1 colspan=1>消息传递</td><td rowspan=1 colspan=1>共享变量</td><td rowspan=1 colspan=1>消息传递</td></tr><tr><td rowspan=1 colspan=1>地址空间</td><td rowspan=1 colspan=1>单地址空间</td><td rowspan=1 colspan=1>单地址空间</td><td rowspan=1 colspan=1>多地址空间</td><td rowspan=1 colspan=1>单地址空间</td><td rowspan=1 colspan=1>多地址空间</td></tr><tr><td rowspan=1 colspan=1>系统存储器</td><td rowspan=1 colspan=1>集中共享</td><td rowspan=1 colspan=1>集中共享</td><td rowspan=1 colspan=1>分布非共享</td><td rowspan=1 colspan=1>分布共享</td><td rowspan=1 colspan=1>分布非共享</td></tr><tr><td rowspan=1 colspan=1>访存模型</td><td rowspan=1 colspan=1>UMA</td><td rowspan=1 colspan=1>UMA</td><td rowspan=1 colspan=1>NORMA</td><td rowspan=1 colspan=1>NUMA</td><td rowspan=1 colspan=1>NORMA</td></tr><tr><td rowspan=1 colspan=1>代表机器</td><td rowspan=1 colspan=1>Cray C-90,Cray T-90,银河1号</td><td rowspan=1 colspan=1>IBM R50,SGI PowerChallenge,曙光1号</td><td rowspan=1 colspan=1>IntelParagon,IBMSP2曙光-1000/2000</td><td rowspan=1 colspan=1>StanfordDASH,Cray T 3D</td><td rowspan=1 colspan=1>Berkeley NOW,Alpha Farm</td></tr></table>

# 1.3.2并行计算机访存模型

下面从系统访问存储器的模式来讨论多处理机和多计算机系统的访存模型,它和上节所讨论的结构模型,是实际并行计算机系统的两个方面。

UMA UMA(Uniform Memory Access)模型是均匀存储访问模型的简称。图1.22示出了UMA多处理机模型，其特点是： $\textcircled{1}$ 物理存储器被所有处理器均匀共享; $\textcircled{2}$ 所有处理器访问任何存储字取相同的时间(此即均匀存储访问名称的由来); $\textcircled{3}$ 每台处理器可带私有高速缓存; $\textcircled{4}$ 外围设备也可以一定形式共享。这种系统由于高度共享资源而称为紧耦合系统(Tightly Coupled System)。当所有的处理器都能等同的访问所有I/O设备、能同样地运行执行程序（如操作系统内核和I/O服务程序等）时称为对称多处理机 SMP(Symmetric Multiprocessor);如果只有一台或一组处理器(称为主处理器),它能执行操作系统并能操纵I/O,而其余的处理器无I/O能力(称为从处理器),只在主处理器的监控之下执行用户代码,这时称为非对称多处理机。一般而言，UMA结构适于通用或分时应用。

![](images/d598be91ef683cd2d77450db22c76625ad88081e821bcfa6112987dd1de66915.jpg)  
图1.22UMA多处理机模型

NUMA NUMA(Nonuniform Memory Access)模型是非均匀存储访问模型的简称。图1.23示出了NUMA多处理机模型，其中(a)为共享本地存储器的NUMA;(b)为层次式机群NUMA,NUMA的特点是： $\textcircled{1}$ 被共享的存储器在物理上是分布在所有的处理器中的,其所有本地存储器的集合就组成了全局地址空间； $\textcircled{2}$ 处理器访问存储器的时间是不一样的：访问本地存储器LM或群内共享存储器CSM较快,而访问外地的存储器或全局共享存储器GSM较慢(此即非均匀存储访问名称的由来); $\textcircled{3}$ 每台处理器照例可带私有高速缓存,且外设也可以某种形式共享。

![](images/b86cd64be92790204f2c1adb344f0df93d41d01b9f5dc1ee3aa7af5fbfb697d1.jpg)  
图1.23NUMA多处理机模型(a)共享本地存储器模型； (b)层次式机群模型

COMA COMA(Cache-Only Memory Access）模型是全高速缓存存储访问的简称。图1.24示出了COMA多处理机模型，它是NUMA的一种特例。其特点是：

![](images/5ac9cf794075f52123484417e08679576c16e59a7862a3ddc54f2766a61b748c.jpg)  
图1.24COMA多处理机模型

$\textcircled{1}$ 各处理器节点中没有存储层次结构,全部高速缓存组成了全局地址空间; $\textcircled{2}$ 利用分布的高速缓存目录D进行远程高速缓存的访问； $\textcircled { 3 } \mathrm { C O M A }$ 中的高速缓存容量一般都大于2级高速缓存容量； $\textcircled{4}$ 使用COMA时，数据开始时可任意分配，因为在运行时它最终会被迁移到要用到它的地方。这种结构的机器实例有瑞典计算机科学研究所的 DDM和 Kendall Square Research 公司的KSR-1等。

CC-NUMA CC-NUMA(Coherent-Cache Nonuniform Memory Access)模型是高速缓存一致性非均匀存储访问模型的简称。图1.25示出了CC-NUMA多处理机模型,它实际上是将一些SMP机器作为一个单节点而彼此连接起来所形成的一个较大的系统。其特点是： $\textcircled{1}$ 绝大多数商用CC-NUMA多处理机系统都使用基于目录的高速缓存一致性协议; $\textcircled{2}$ 它在保留 SMP结构易于编程的优点的同时,也改善了常规SMP的可扩放性问题； $\textcircled { 3 } \mathbf { C C } \mathbf { \cdot N U M A }$ 实际上是一个分布共享存储的DSM多处理机系统； $\textcircled{4}$ 它最显著的优点是程序员无需明确地在节点上分配数据,系统的硬件和软件开始时自动在各节点分配数据,在运行期间，高速缓存一致性硬件会自动地将数据移至要用到它的地方。总之，CC-NUMA所发明的一些技术在开拓数据局部性和增强系统的可扩放性方面很有效。不少商业应用,大多数数据访问都可限制在本地节点内，网络上的主要通信不是传输数据,而是为高速缓存的无效性(Invalidation)所用。

![](images/ab2a649141872b3985172919da79d981bb2e7b63516ebabdcfd461e74be94b25.jpg)  
图1.25 CC-NUMA结构模型(RC:远程高速缓存）

NORMA NORMA( $\Nu _ { 0 }$ Remote Memory Access)模型是非远程存储访问模型的简称。在一个分布存储的多计算机系统中,如果所有的存储器都是私有的、仅能由其处理器所访问时就称为NORMA。图1.26示出了基于消息传递的多计算机一般模型,系统由多个计算节点通过消息传递互连网络连接而成,每个节点都是一台由处理器、本地存储器和/或I/O外设组成的自治计算机。NORMA的特点是： $\textcircled{1}$ 所有存储器均是私有的； $\textcircled{2}$ 绝大多数NUMA都不支持远程存储器的访问; $\textcircled{3}$ 在DSM中,NORMA 就消失了。

小结可以将上节所讲的并行机结构模型和本节所讲的并行机访存模型的相互关系汇总在图1.27中。注意，物理上分布的存储器从编程的观点看可以是共享的或非共享的;共享存储结构(多处理机)可同时支持共享存储和消息传递编程模型；共享存储的编程模型可同时执行于共享存储结构和分布式存储结构(多计算机)上。

![](images/04f330bd85eb477f02928b0d94b0c411f6023854414a481c22de133e2e1024a6.jpg)  
图1.26消息传递多计算机一般模型

![](images/fd4f44165ea844c762272866f3317e4b70740851cfbf77cd3e35cdc1a126562a.jpg)  
图1.27构筑并行机系统的不同存储结构

# $\yen 1.3.3$ 并行计算机存储组织

下面从系统的存储器组织方式来讨论近代计算机中层次存储技术及其一致性管理。

层次存储技术在近代计算机中，存储设备都照例按图1.28所示的那样将按层次组织的寄存器和高速缓存装在处理器芯片或处理器板上的。寄存器的分配由编译器完成;高速缓存对程序员是透明的(它可按速度和应用要求有一级或多级);主存储器是计算机系统的基本存储器,它由存储管理部件和操作系统共同管理;磁盘存储器被看作是最高层的联机存储器,它保存系统程序(OS和编译器）、某些用户程序及其数据集;磁带机是脱机存储器，用作后援存储器,它保存当前或过去的用户程序副本、处理结果和文件等。磁盘驱动器和磁带机是由OS采取有限的用户干预方式进行管理的。

![](images/c2bd0a919872406ea74cdd09e372bea4189ea41808fa41fc9a6070d5fea4194e.jpg)  
图1.28存储器的层次结构

存储器相邻层之间的数据传输，是按图1.29所示的那样以不同的单位进行的:CPU 和高速缓存之间数据按字(4个字节)传输(高速缓存 $( \mathbf { M } _ { 1 }$ )通常分成一些高速缓存块,有的作者称之为高速缓存行(Cache Line),每块典型值是8个字);高速缓存和主存储器 $( \mathbf { M } _ { 2 } )$ )之间数据按块(32个字节)传输；主存储器和磁盘$\begin{array} { r } { ( \mathbf { M } _ { 3 } ) . } \end{array}$ )之间数据按页传输(每页可包含128个块);磁盘和磁带机 $( M _ { 4 } )$ 之间数据按段传输(段的大小由用户按需要而定）。

高速缓存一致性所谓一致性（Coherence）是指同一数据项应与后继存储

![](images/1a88c2126d0247664ed70cfe69d2568e0d5a05686f8e7a17542633b5f26e9c4c.jpg)  
图1.29存储器相邻层之间的数据传输

1.从32字节高速缓存块（如块a） 按字（4个字节）存取。

2.从32块或1KB存储页面按块（32字节）存取，如从页面B按块存取。

3.从很多页面组成的文件按页（1KB）存取，如从段F中的页面A和页面B存取。

4.用不同页面数目的段传送。

器层次上的副本相一致。如果在高速缓存中的一个字被修改过，那么在其所有更高层上的该字的副本也必须立即或随后加以修改。层次结构照例必须这样维护。一致性维护一般有两种策略： $\textcircled{1}$ 写通过WT(Write-Through),即如果在 $\mathbf { M } _ { i }$ ${ \bf \Psi } ( i = 1 , 2 \cdots )$ 中修改了一个字，则在 $\mathbb { M } _ { i + 1 }$ 中需要立即修改； $\textcircled{2}$ 写回WB(Write-Back),即在 $\mathbf { M } _ { i + 1 }$ 中的修改延迟到 $\mathbf { M } _ { i }$ 中正在修改的字被替换或从 $\mathbf { M } _ { i }$ 中消除后才进行。在多处理机系统中，由于多台处理机异步地相互操作;因此多个高速缓存中的同一高速缓存行的副本可能不同。造成高速缓存不一致性的原因来源于： $\textcircled{1}$ 由共享可写数据所造成的不一致； $\textcircled{2}$ 由进程迁移所造成的不一致； $\textcircled{3}$ 由绕过高速缓存的I/O操作所造成的不一致。假定有一个由2台处理器组成的多处理机系统，每台处理器各有一个高速缓存，且它们共享主存。设X是两台处理器已访问过的共享数据，在修改之前，X的三个副本是一致的。如图1.30所示，如果 $\mathbf { P } _ { 1 }$ 使用WT策略将其高速缓存中的副本更改为 $\mathbf { X } ^ { \prime }$ ,则存储器中的副本也立即更改为 $\mathbf { X } ^ { \prime }$ ,此时两个高速缓存中的副本就不一致了；同样,如果使用WB策略时也会造成两个高速缓存的副本不一致。至于由进程迁移所造成的不一致性和由绕过高速缓存的I/O操作所造成的不一致性，读者可参阅本章习题1.8和1.9学习之。

![](images/7f4747bef8d39dc0634d381a4301be882ce5424633f4691d462b1c5f67897351.jpg)  
图1.30共享可写数据所造成的不一致性

监听总线协议在基于总线连接的多处理机系统中，总线是保证高速缓存--致性最方便的装置，因为它能使所有的处理器观察到存储器正在进行的业务活动。如果总线业务破坏了本地高速缓存中数据的一致性状态，那么高速缓存的控制器就应采取相应的动作使本地的副本无效。采用此机制保证高速缓存一致性的协议称为监听协议(Snoopy Prolocol)。

如果接在公共总线上的处理机均有自己的私有高速缓存，那么可使用写无效(Write-Invalidale)和写更新(Write-Update)两种策略来确保高速缓存的-致性，前者是在本地高速缓存的数据块更新时使所有远程的副本均无效;后者是把更新的数据块广播给含该数据块的所有高速缓存。

图1.31表示了采用WT策略的写无效和写更新的一致性协议是如何维护共享存储模块中X与3个本地高速缓存中的副本的一致性的。采用写无效协议时，如图1.31(b)所示，当处理器P将其高速缓存中的X修改为X时，通过总线使所有其它的高速缓存中的内容均无效(用I表示)；采用写更新协议时，如图1.31(c)所示，当处理器 $\mathrm { I ^ { 2 } } _ { \mathrm { : } }$ 将其高速缓存中的X修改为X'时，通过总线X广播给所有其它的高速缓存，因为是采用WT策略，还需要更新主存中的副本。至于采用WB策略的·致性维护过程，读者可参阅本章习题1.10理解之。

基于目录的协议上面介绍的监听协议为总线连接的多处理机系统所使用，对于多级I连网络连接的多处理机系统则使用基于目录的协议(DirectoryBascd Prolocol)，它就是使用一个日录来记录共享数据的所有高速缓存行的位置和状态

图1.32示出了基于目录的高速缓存一致性方案的基本原理，其存储器/高速缓存更新工作如下：高速缓存 $\Gamma _ { 2 }$ 的读缺失(Read-Miss)产生·个请求送给 $\mathrm { I } ) _ { 1 }$ （图中用细线表示）， $l ) _ { l }$ 指示在 ${ \bf \Xi } ( { \bf \Lambda } )$ 中有可用(Clean)副本，存储控制器再将请求传全 $C _ { 1 }$ ，它返回一个可用副本给 $\mathrm { M } _ { \mathrm { l } }$ 和 ${ \bf \Xi } ( { \bf \Lambda } )$ ；在 $\bf ( \dot { \omega } _ { 1 } \cdot \dot { \bf \delta } _ { j }$ 命中时（图中用粗线表示），它就发送·个命令给存储控制器，存储控制器再发·个无效命令给在D中有标记的所有高速缓存（在此为 $( \ Y _ { \frac { 3 } { 7 } } )$ 、

![](images/fcbcacf43bb9a8880553d069ab294d556fc9e4b37b5314dd1a257e4836fe5e6d.jpg)  
图1.31采用WT策略的一致性维护(a)更新前； $( \mathfrak { b } ) \mathfrak { P } _ { 1 } \ ^ { \prime } \mathfrak { s }$ 无效操作后； $( \cos ) _ { \mathrm { } } \mathrm { p } _ { 1 } \mathrm { ~ } ^ { \prime } \mathrm { \pmb { \mathscr { s } } ~ }$ 更新操作后

![](images/048e78cb68cab2819ebcc6b59c2f0480c33dc62282d18f4bded32577191ef152.jpg)  
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

![](images/c461ea35fbf3f4755678af71c51e79f5afecc03a3cf6346765c94102b998f7ba.jpg)  
图1.33二元胖树

1.3四元胖树如图1.34所示，试间：每个内节点有几个子节点和几个父节点？你知道哪个机器使用了此种形式的胖树？

1.4试构造一个N=64的立方环网络，并将其直径和节点度与N=64的超立方比较之，你的结论是什么？

![](images/6acafb233605041b9bbf28e753c0c653e1008b9c7c5d0cbbe03120eb8322fbce.jpg)  
图1.34四元胖树

1.5一个 $\therefore \lor = \underline { { ? } } ^ { k }$ 个节点的de Bruijn 网络如图1.35所示，令 $u _ { k - 1 } u _ { k - 2 } \cdots u _ { 1 } u _ { 1 } )$ 是一个节点的二进制表示，则该节点可达如下两个节点：

$$
\begin{array} { r } { a _ { k \textrm { - } 2 } a _ { k \textrm { - } 3 } \cdots a _ { 1 } a _ { 0 } ( ) } \\ { a _ { k \textrm { - } 2 } a _ { k \textrm { - } 3 } \cdots a _ { 1 } a _ { 0 } \} } \end{array}
$$

试问：该网络的直径和对剖宽度为多少?

![](images/5fa17c30b2ed7142a76adb0263500b2274e23ad1fe6da80ebb5a1d922882957b.jpg)  
图1.35 $\mathbf { \nabla } \cdot \mathbf { V } = 8$ 的dc Bruijn 网络

1.6-个 $. \lor = 2 ^ { n }$ 个节点的洗牌交换网络如图1.36所示．试问：此网节点度 $= ?$ 网络直径$= ?$ 和网络对剂度 $= ?$

![](images/7af23c68894190cf52e6c4967d3092ce524024e8e3e851dd5142564d5b3318c7.jpg)  
图1.36 $\mathbf { \nabla } \cdot \mathbf { V } = \mathbf { 8 }$ 的洗牌交换网络

1.7·个 $. \mathsf { V } = (  { k } + \mathsf { i } ) \underline { { \mathsf { \Omega } } } ^ { \prime }$ 个节点的蝶形网络如图1.37所示

![](images/937ff6072098c4ac5dd1323aa97881438a2833c86a77b8550538814b2399f574.jpg)  
图1.37 $k = 3$ 的蝶形网络

试问：此网节点度 $= ?$ 网络直径 $=$ ？和网络对剖宽度 $= ?$

1.8参照图1.38,试解释为什么当采用WT策略进程从 ${ \sf P } _ { 2 }$ 迁移到 $\mathrm { P } _ { 1 }$ 时，或采用WB策略包含共享变量 $\mathbf { X }$ 的进程从 ${ \bf P } _ { 1 }$ 迁移到 ${ \bf P } _ { 2 }$ 时，会造成高速缓存的不一致。

![](images/3f2f041e9232612e6f31a407b4cae42a72f55ac07cb084879cbf112b4df1773a.jpg)  
图1.38进程迁移所造成的不一致性

1.9参照图1.39.试解释为什么：①当I/O处理器将--个新的数据X'写回主存而绕过采用WT策略的高速缓存时会造成高速缓存和主存间的不一致；②当直接从主存输出数据而绕过高速缓存采用WB策略时也会造成不·-致、

![](images/0b8a62ceddcab5c1703188e438721eb80ffc040c9329d56c80c67abfc7bd7a2b.jpg)  
图1.39绕过高速缓存的I/操作所造成的不致性

1.10参照图1.40,试解释采用WB策略的写更新和写无效协议的一致性维护过程，其中，X为更新前高速缓存中的副本，X为修改后的高速缓存行，1为无效的高速缓存行，

![](images/989235be1518179d2c1e609cad5537617640a692edbf65b53fe0e765301ec4a3.jpg)  
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

![](images/0e43d3930947d3b63c15484ad75d7bcade60fca69f688531767829080e8e701a.jpg)  
图2.1CC-NUMA使用远程高速缓存重新分配数据（a)第一步的数据分配；(b)第二步的数据再分配

表2.15种商用SMP系统特性比较一览表  

<table><tr><td rowspan=1 colspan=1>系统特性</td><td rowspan=1 colspan=1>、DECAlphaserver84005/440</td><td rowspan=1 colspan=1>HP9000/T600</td><td rowspan=1 colspan=1>IBMRS600/R40</td><td rowspan=1 colspan=1>Sum UltraEnterprise6000</td><td rowspan=1 colspan=1>SGI PowerChallenge XL</td></tr><tr><td rowspan=1 colspan=1>处理器数目</td><td rowspan=1 colspan=1>：12福</td><td rowspan=1 colspan=1>：  心</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>厦   加：</td><td rowspan=1 colspan=1>36</td></tr><tr><td rowspan=1 colspan=1>处理器类型i</td><td rowspan=1 colspan=1>437 MHzAlpha21164E</td><td rowspan=1 colspan=1>180MHzPA8000</td><td rowspan=1 colspan=1>112MHzPowerPC604     1</td><td rowspan=1 colspan=1>167MHzUtraSPARC</td><td rowspan=1 colspan=1>195MHz： MIPSLR10000</td></tr><tr><td rowspan=1 colspan=1>处理器片外高速缓存容量</td><td rowspan=1 colspan=1>福4MB心</td><td rowspan=1 colspan=1>8MB</td><td rowspan=1 colspan=1>1 MB！</td><td rowspan=1 colspan=1>512MB</td><td rowspan=1 colspan=1>4MB</td></tr><tr><td rowspan=1 colspan=1>最大主存容量</td><td rowspan=1 colspan=1>28GB</td><td rowspan=1 colspan=1>116GB</td><td rowspan=1 colspan=1>i  .2GB</td><td rowspan=1 colspan=1>30GB</td><td rowspan=1 colspan=1>16GB</td></tr><tr><td rowspan=1 colspan=1>互连网络及带宽               ！</td><td rowspan=1 colspan=1>BUS2.1GB/</td><td rowspan=1 colspan=1>BUS960MB/s</td><td rowspan=1 colspan=1>1BUS+Xbar1.8GB/s</td><td rowspan=1 colspan=1>！BUS+Xbar2.6GB/s</td><td rowspan=1 colspan=1>BUS1:2 GB/s</td></tr><tr><td rowspan=1 colspan=1>外磁盘容量</td><td rowspan=1 colspan=1>192 GB</td><td rowspan=1 colspan=1>168GB</td><td rowspan=1 colspan=1>38 GB</td><td rowspan=1 colspan=1>63.GB</td><td rowspan=1 colspan=1>144GB：：！</td></tr><tr><td rowspan=1 colspan=1>I/O通道</td><td rowspan=1 colspan=1>12 PCI总线，每个133MB/s</td><td rowspan=1 colspan=1>N/A1</td><td rowspan=1 colspan=1>2MCA,每个160 MB/s</td><td rowspan=1 colspan=1>30 Sbus,每个200 MB/s</td><td rowspan=1 colspan=1>6 Power Channel-2HIO,每个320MB/s</td></tr><tr><td rowspan=1 colspan=1>I/O槽</td><td rowspan=1 colspan=1>144PCI精</td><td rowspan=1 colspan=1>112HPPB1</td><td rowspan=1 colspan=1>15MCA</td><td rowspan=1 colspan=1>45 Sbus</td><td rowspan=1 colspan=1>12 HIO槽</td></tr><tr><td rowspan=1 colspan=1>I/O带宽</td><td rowspan=1 colspan=1>1.2 GB/s</td><td rowspan=1 colspan=1>1GB/s！</td><td rowspan=1 colspan=1>320 MB/s</td><td rowspan=1 colspan=1>2.6GB/8</td><td rowspan=1 colspan=1>每个HIO槽320MB/s5</td></tr></table>

# $\times 2 . 1 . 2$ SGI/Cray Origin 2000超级服务器

1996年10月，SGI/Cray公司推出了Origin 2000系统，它采用了CC-NUMA结构，此结构也被称之为可扩放共享存储多处理机S2MP或S2MP(Scalable

Shared Memory Multiprocessor)。设计时吸取了DASH的经验,所设计的系统规模可达到1024个处理器和1TB主存，其中 $1 \sim 6 4$ 个处理器的系统叫SGIOri-gin 2000,而大于等于128个处理器的系统叫（ray Origin 2000。现有的Origin2000的结构配置属性综合于表2.2中。

表2.2Origin2000结构配置属性一览表  

<table><tr><td rowspan=1 colspan=1>属性</td><td rowspan=1 colspan=1>立式（Deskside)配置</td><td rowspan=1 colspan=1>装架式（Rack）配置</td></tr><tr><td rowspan=1 colspan=1>处理器数目</td><td rowspan=1 colspan=1>1~8</td><td rowspan=1 colspan=1>2~128</td></tr><tr><td rowspan=1 colspan=1>峰值速度(Gflops)</td><td rowspan=1 colspan=1>3.12</td><td rowspan=1 colspan=1>49.92</td></tr><tr><td rowspan=1 colspan=1>高速缓存容量（MB)</td><td rowspan=1 colspan=1>1~32</td><td rowspan=1 colspan=1>2~512</td></tr><tr><td rowspan=1 colspan=1>物理存储器容量(GB)</td><td rowspan=1 colspan=1>0.064~16</td><td rowspan=1 colspan=1>0.064~256</td></tr><tr><td rowspan=1 colspan=1>总计峰值存储带宽(GB/s)</td><td rowspan=1 colspan=1>3.12</td><td rowspan=1 colspan=1>49.92</td></tr><tr><td rowspan=1 colspan=1>I/端口数目</td><td rowspan=1 colspan=1>14</td><td rowspan=1 colspan=1>208</td></tr><tr><td rowspan=1 colspan=1>总计峰值I/O带宽(GB/s)</td><td rowspan=1 colspan=1>6.2</td><td rowspan=1 colspan=1>102</td></tr></table>

系统结构Origin2000系统结构如图2.2所示。它的每个节点包括1或2个 MIPSR10000处理器（时钟 $1 9 5 ~ \mathrm { M F z }$ ,峰值速度395Mllops)，-个可高达 $4 \ \mathrm { M B }$ 的高速缓存和-个DSM主存(物理上分散在各节点中，但可被所有节点访问),硬件增强了基于目录的高速缓存一致性。如图2.3所示，一个HUB(ASIC交叉开关)连接系统中的处理器、存储器、互连网络和I/O系统,HUB有4个双向端口，使用 $1 9 5 ~ \mathrm { M H z }$ 的时钟，每个口可提供单向 $7 8 0 ~ \mathrm { M B / s }$ 的峰值带宽和全双工1.56(GB/s的峰值带宽,它用于节点内和节点间通信选路,4个成对的接口电路(ififo,ofifo)负责内部和外部信息格式的转换。

![](images/ec0c5beeb0d9bf90eb65487a6de36c50aba959d8af257051c9357207b6299a33.jpg)  
图2.2Origin 2000系统结构

![](images/67425eb9f31a0c84a8dfb1c4b9ceb06542748905390a81dc513f69236c036ee7.jpg)  
图2.3Origin 2000中交叉开关HUB芯片

①I/O子系统:Origin 2000的I/O子系统示于图2.4中,其中,XBOW是一个8端口的交叉开关(各口均使用XIO协议):2个连向节点,其余6个连向XIO设备或者ASIC小部件，包括图形小部件G(GraphicsWidget）和桥接小部件B(BridgeWidget)。通过 32位或 64位的PCI总线,不同的I/O设备（ATM、HiPPI、FDDI、SCSI等)均可连向Origin 2000。Origin 2000 可提供单- I/O空间，即任何处理器能访间任·[O设备。

![](images/fd01944a045c817e9f7c614aee8aadd5151e343603d587eec2cbd6ec15c52d10.jpg)  
图2.4Orgin 2000的I/0子系统

$\textcircled{2}$ 互连系统:Origin2000的互连系统由CrayLink电缆和图2.5所示的路出器组成。SGI SPIDER路由器提供可靠的虫蚀选路，它是6端口的交叉开关,这些端口连向节点或别的路由器。路由器允许6个端口同时全双工工作。由于外部频率$( 3 9 0 ~ \mathrm { M H z } )$ 和路由器芯片内部频率 $( 9 7 . 5 ~ \mathrm { M H z } )$ 的不同，所以需使用源同步驱动器SSD(Source Synchronous Driver)和源同步接收器 SSR(Source Synchronous Receiver)施行内/外频率 $( 9 7 . 5 ~ \mathrm { M H z } / 3 9 0 ~ \mathrm { M H z } )$ 和字长(64位/16位)的转换。链路级协议LLP(Link-Level Protocol)确保信息可靠传输（使用CRC误差检测和重发校正），施行流控、缓解竞争和拥挤等。

![](images/98c7c65bf763c0b024e46740468ae68f96d45e23f8e44d02a9090825685f7b0f.jpg)  
图2.5Origin 2000的 SPIDER 路由器芯片

$\textcircled{3}$ 胖超立方拓扑:Origin 2000 中采用了胖超立方(Fat Hypercube)拓扑。如图2.6所示，胖超立方是将传统的2元超立方加以修改而得，其优点是保持了超立方线性对剖宽度的优点且避免了节点度的增加。在此拓扑中,每个路由器R芯片有6个端口，其中的2个连向节点，其余的4个用于网络连接。按照一般的超立方，度为4的节点最多也只能构造16个顶点的超立方（即Origin 2000中的32个节点),但使用了胖超立方拓扑,可允许Origin 2000连接多达512个节点(1024个处理器)。图2.6(a)只有-个节点，它有2个处理器，还可连向XBOW交叉开关；图2.6(b)中，-个SPIDER路由器R连向2个节点;图2.6(c)中2个R连向4个节点；以此方式可达32个节点(图2.6(f)),至此，如果把R视为超立方的顶点，则它就是普通的2元超立方连接。注意，未被使用的路由器端可连向快速链路( $\operatorname { E x } -$ pressLink)以降低延迟和增大对剖带宽(如图2.6(d)中的虚线连接)。当超过32个节点时，Origin2000的胖超立方中使用了额外的路由器（称之为元路由器，Metaroutcr),8个元路由器构成·个（ray Rouler，这些元路由器只用作中间选路，不连向任何节点，·个64个节点(32个顶点，即路由器)的胖超立方拓扑如图2.6$( \mathbf { g } )$ 所示，其中4个8顶点的子立方中每个顶点都连向一个元路由器，这种胖超立方可·直扩放到1024个处理器，读者不妨想一想应如何构造？

![](images/b2a48e88c7329597d22fb37518c742c989f421bb7148ffd78af9f6024ea6f591.jpg)  
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

![](images/19b9a9aeeb180a9910ffa9378b96cc18794547c645f075e14e8f0a2cccfba9ad.jpg)  
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

![](images/eb9039be60d1bffdc23cc85e9794fea0c7cf8e63f2d677bb258bb9dc369757d1.jpg)  
图2.8微处理器系列及其代表性CPU芯片

# \*2.2.2 机群型大规模并行机 SP2

1991年秋,IBM决定涉足于 MPP 的研究,开动了 SP(Scalable POWERpar-allel)计划。1992年2月开始组队,1993年4月就公布了第一个产品 SP1,继之于1994年7月就宣布了SP2。IBM的 SP是比较特殊的,它采用了机群的办法来构筑MPP。到1998 年之前,其在世界上的总装机量超过3000,实属MPP系统成功之例。

设计目标和策略IBM设计 SP系统时提出了如下目标： $\textcircled{1}$ 赶市场：遵循着