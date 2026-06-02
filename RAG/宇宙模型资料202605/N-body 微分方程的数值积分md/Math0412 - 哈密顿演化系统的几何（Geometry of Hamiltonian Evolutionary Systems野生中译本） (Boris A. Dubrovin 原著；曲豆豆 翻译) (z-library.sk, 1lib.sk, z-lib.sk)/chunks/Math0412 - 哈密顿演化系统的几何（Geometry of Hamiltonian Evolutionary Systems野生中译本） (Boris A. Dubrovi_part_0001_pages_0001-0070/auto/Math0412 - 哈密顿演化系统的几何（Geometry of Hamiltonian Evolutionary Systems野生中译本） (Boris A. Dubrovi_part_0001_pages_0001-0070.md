# 哈密顿演化系统的几何

Math4012 第 1.28 稿

曲豆豆 翻译 原著: Boris A. Dubrovin

2020 年 12 月 22 日

![](images/9899135dd942c6cc4c8e60882909103b72bb647a3b8dc96f4c1704a7f931f083.jpg)

![](images/b4b62a5a5edaee9c74f9d0bea51e46749446f6de9b61148932eca4eaf7673001.jpg)  
图: Boris Dubrovin, 个人主页: https://people.sissa.it/\~dubrovin/

本书为 Boris Dubrovin

Geometry of Hamiltonian Evolutionary Systems的非官方 (野生) 中译本, 以此纪念 Dubrovin!

# 目录

# 引言

#

# 第一章 泊松括号的几何 1

1.1 有限维泊松括号的主要例子 1

补充内容: 哈密顿-李群与量子群 8

1.2 完全可积系统及其摄动. 平均化方法 13

1.3 局部场论泊松括号: 主要例子 16

1.4 微分几何泊松括号. 流体力学型泊松括号与黎曼几何 27

# 第二章 可积系统理论基础 41

# 2.1 流体力学型系统的可积性理论 41

附录 1. 流体力学型系统的黎曼不变量 49  
附录 2. 正交曲线坐标系与可积系统 51

2.2 演化系统的不变环 55

2.3 交换表示, 守恒律与演化系统的哈密顿理论 64

附录: 引理 2.9 的证明 72

2.4 构造演化系统的不变环并寻找相应作用量-角参数的代数几何方法 (“有

限空缺积分方法”) 73

# 第三章 场论哈密顿系统的慢摄动与平均化方法 87

3.1 演化系统在不变环上的泊松括号的平均化 . . 873.2 应用: KdV 理论中某步骤的分解; 色散版本的冲击波. Gurevich-Pitaevskii问题的解析解 1003.3 有限空缺势的平均化方法与半经典量子化. Painlevé-I 方程的渐近积分 . . 105

# 参考文献

# 引言

这本书基于本人 1990 年在那不勒斯大学 (University of Naples) 理论物理系的讲稿编写而成, 目的是介绍偏微分方程的演化系统的哈密顿理论的基本几何想法, 并介绍该想法的一些应用. 我们暂不考虑量子哈密顿系统中的问题, 只局限于经典的情况 (尤其是 $1 + 1$ 维).

第一章的前两节介绍有限维哈密顿理论, 该理论基于泊松括号的观点. 泊松括号的几何在局部上是平凡的, 毕竟 Darboux 定理断言在适当的局部坐标下泊松括号可以写成标准形式. 但是在整体上, 泊松括号不再平凡; 例如我们讨论了磁场, 二次泊松括号及其与量子群的关系等等非平凡的例子. 有限维可积哈密顿系统的几何非常简单: 在Liouville 定理的情况下, 相空间被 不变环 (invariant tori) 所充满; 在如此的不变环上的一点出的小邻域内, 泊松结构是典范的, 因为可以在该邻域内构造 作用量-角参数(action-angle variable) . 摄动后的可积系统的相曲线的行为可以通过 Poincaré 平均化方法来研究; 这里仅仅介绍该平均方法的启发性的想法 (这对无限维情形也十分有益),而不会去严谨地考虑 KAM 理论.

在无限维哈密顿系统的几何中, 我们也能证明一些将泊松括号化为常值的 Darboux型定理. 但在我们的情形下, 容许的“变量代换”类被局部性原理所限制: 在此变换下局部演化偏微分方程系统应为保守的. 这就引出了关于演化系统的泊松括号的几何的一系列非平凡的问题; 这之中的一些会在第一章讨论.

在演化系统的可积性理论中, 我们在第二章重点关注寻找有限维不变流形的问题.$1 + 1$ 维演化系统的任何一个局部守恒律的驻点集都构成该系统的一个有限维不变流形.若哈密顿演化系统具有充分多的两两交换的守恒律, 则有限维驻点集被不变环所充满.最简单的情形 [一维, 或者二维环面] 可用初等方法求解. 但对于高维的不变环面, 目前只有来自孤子理论 [例如 KdV] 的可积系统可以显式构造. 我们以 Korteweg-de Vires(KdV) 方程为例子, 介绍求解高维不变环面及其相应作用量-角参数的代数几何方法 [“有限空缺积分”] 的一些基本想法. 关于未知函数的导数的一阶线性系统 [所谓的“流体力学型系统”] 的可积性理论的介绍分布于不同章节. 相比一般情形, 此理论更加基本, 并且在此理论中哈密顿理论与古典微分几何格外重要. 第三章揭示了这种流体力学系统在哈密顿演化系统的有限维不变流形的小邻域研究中的普适性.

第三章讨论了哈密顿演化系统的“相曲线”在不变环面的有限维族的小邻域中的行为 [无限维版本的 Poincaré 平均化方法, 也是非线性版本的 WKB 方法] . 可以证明, 该小邻域可以表示为一类 [带内部自由度的] 理想流体系统的相空间, 并且原来的哈密顿系统在此小邻域中的演化可以用流体力学型哈密顿系统来描述 [所谓的“平均化系统”] .并且, 这个平均化过程不仅保持哈密顿性质, 还保持可积性. 此章还讨论了该理论在色散流体力学的应用. 它甚至在有限维动力系统的研究中也有用. 本章最后一节给出了这种应用的一个例子——非摄动弦理论中新近出现的一个系统的渐近积分.

致谢. 感谢那不勒斯大学 (University of Naples) 物理系以及 INFN 的热情好客和对编写本讲义的支持. 这个讲座是在与系里的同事讨论互动中形成的; 感谢他们, 尤其感谢G.Marmo 教授有益探讨与建议. 我也感谢我在莫斯科, 列宁格勒的同事们, 包括 A.R.Its, I.M. Krichever, S.P. Novikov, S.P. Tsarev 的有益探讨. 也感谢 Guido Celentano 为本讲义准备 TEX 文档.

# 第 1 章 泊松括号的几何

# 1.1 有限维泊松括号的主要例子

在本章, 我试图说清楚在几何的观点下哈密顿理论是什么, 以及现代数学物理的一些想法如何在其中自然地出现. 本节介绍有限维的哈密顿理论, 这之中几乎所有的想法与内容都是大家或多或少熟知的.

我想先回顾基于 泊松括号 (Poisson bracket) 的标准的 (有限维) 哈密顿理论(Hamiltonian formalism) . 对于 相空间 (phase space) $P$ 上的两个函数 $f ( x )$ 与 $g ( x )$ ,其泊松括号是一个新的函数 $\{ f , g \}$ . 我们希望该操作是双线性, 反对称的, 并且服从 莱布尼茨法则 (Leibnitz rule) 以及 雅可比恒等式 (Jacobi identity) :

$$
\{ \lambda f + \mu g , h \} = \lambda \{ f , h \} + \mu \{ g , h \} ,
$$

$$
\{ g , f \} = - \{ f , g \} ,
$$

$$
\{ f g , h \} = f \{ g , h \} + g \{ f , h \} ,
$$

$$
\{ \{ f , g \} , h \} + \{ \{ g , h \} , f \} + \{ \{ h , f \} , g \} = 0 .
$$

在局部坐标 $( x ^ { 1 } , x ^ { 2 } , . . . , x ^ { N } )$ 下, 定义如下的反对称矩阵

$$
h ^ { i j } ( x ) = \{ x ^ { i } , x ^ { j } \} , \quad h ^ { j i } = - h ^ { i j } .
$$

由莱布尼茨法则可知, 在坐标变换 $x ^ { i }  y ^ { i } = y ^ { i } ( x )$ 下该矩阵满足 $( 2 , 0 )$ -张量的变化规律1

$$
h ^ { k l } ( y ) = { \frac { \partial y ^ { k } } { \partial x ^ { i } } } { \frac { \partial y ^ { l } } { \partial x ^ { j } } } h ^ { i j } ( x )
$$

反之, 张量 $h ^ { i j } ( x )$ 可通过公式

$$
\{ f , g \} = h ^ { i j } ( x ) \frac { \partial f } { \partial x ^ { i } } \frac { \partial g } { \partial x ^ { j } }
$$

来完全决定泊松括号 (双线性与莱布尼茨法则的推论).

而雅可比恒等式给张量 $h ^ { i j } ( x )$ 更多限制:

$$
\{ \{ x ^ { i } , x ^ { j } \} , x ^ { k } \} + \{ \{ x ^ { j } , x ^ { k } \} , x ^ { i } \} + \{ \{ x ^ { k } , x ^ { i } \} , x ^ { j } \} \equiv { \frac { \partial h ^ { i j } } { \partial x ^ { s } } } h ^ { s k } + { \frac { \partial h ^ { j k } } { \partial x ^ { s } } } h ^ { s i } + { \frac { \partial h ^ { k i } } { \partial x ^ { s } } } h ^ { s j } = 0
$$

(上式左边在微分几何中称为 Schouten 括号 (Schouten bracket) $[ h , h ] ^ { i j k } )$ . 该式显然是雅可比恒等式的必要条件; 其逆命题的证明也是直接的. 在非退化, 即 $\operatorname* { d e t } ( h ^ { i j } ) \neq 0$ 的情形, 逆矩阵 $( h _ { i j } ) = ( h ^ { i j } ) ^ { - 1 }$ 定义了相空间 $P$ 上的 辛结构 (symplectic structure)$\omega = h _ { i j } \mathrm { d } x ^ { i } \wedge \mathrm { d } x ^ { j }$ , (即 2-形式 $\omega$ 是非退化的闭形式, $\mathrm { d } \omega = 0 \mathrm { . }$ ). 此时相空间 $P$ 为 辛流形(symplectic manifold) . 反之也成立: 对于任何配以辛形式 $\omega = h _ { i j } \mathrm { d } x ^ { i } \wedge \mathrm { d } x ^ { j }$ 的辛流形,逆矩阵 $( h ^ { i j } ) = ( h _ { i j } ) ^ { - 1 }$ 确定了泊松括号 $\{ f , g \} = h ^ { i j } \frac { \partial f } { \partial x ^ { i } } \frac { \partial g } { \partial x ^ { j } }$ 由 Darboux 定理可知, 在适当的局部坐标下 $( h ^ { i j } )$ 为常值矩阵. 而若 $( h ^ { i j } )$ 是退化但常秩的, 则相空间 $P$ 在整体上是由 辛叶 (symplectic leaf) 构成的 叶状结构 (foliation) , 局部坐标下辛叶有如下表示:

$$
\begin{array} { l } { P = \displaystyle \bigcup _ { a _ { 0 } } P _ { a _ { 0 } } , } \\ { P _ { a _ { 0 } } = \{ a ( x ) = a _ { 0 } \} , } \\ { a = ( a ^ { 1 } , . . . , a ^ { k } ) , \quad \textstyle \sharp \sharp \ d } \\ { \{ a ^ { i } , f \} \equiv 0 \quad \forall f . } \end{array}
$$

使得泊松括号 $\{ , \}$ 在每一片辛叶 $P _ { a _ { 0 } }$ 当中非退化. (函数 $a ^ { 1 } , . . . , a ^ { n }$ 为泊松括号 $\{ , \}$ 的零化子 (annihilator) 的一组生成元. )

上述内容都是经典的.

泊松括号诱导了相空间上的 哈密顿系统 (Hamiltonian system) . 每一个函数 $H ( x )$ 都可通过下述公式

$$
\frac { \mathrm { d } x ^ { i } } { \mathrm { d } t } = \{ H ( x ) , x ^ { i } \} , \quad i = 1 , . . . , N
$$

来定义一个哈密顿系统. 此时函数 $H$ 称为该系统的 哈密顿量 (Hamiltonian) . 向量场

$h ^ { i } ( x ) = \{ H ( x ) , x ^ { i } \}$ 称为哈密顿量 $H$ 的 斜梯度 (skew gradient) 2 在哈密顿理论中, 对称性和守恒律的关系密切. 对任意函数 $F ( x )$ , 成立 $\frac { \mathrm { d } } { \mathrm { d } t } F ( x ) = \{ H ( x ) , F ( x ) \}$ . 该哈密顿系统的 守恒律 (consetvation law) 定义为如下方程

$$
\{ H , F \} = 0 , \quad F = F ( x ) .
$$

对于给定的哈密顿系统, 其所有的守恒律构成一个李代数.

若 $F ( x )$ 为该哈密顿系统的一个守恒律, 则以 $F$ 为哈密顿量的另一个哈密顿系统

$$
\frac { \mathrm { d } x ^ { i } } { \mathrm { d } s } = \{ F ( x ) , x ^ { i } \}
$$

是之前那个哈密顿系统的一个 对称 (symmetry) , 也就是说它与前者交换:

$$
{ \frac { \mathrm { d } } { \mathrm { d } s } } { \frac { \mathrm { d } } { \mathrm { d } t } } x ^ { i } = { \frac { \mathrm { d } } { \mathrm { d } t } } { \frac { \mathrm { d } } { \mathrm { d } s } } x ^ { i } .
$$

若两个函数 $F _ { 1 } , F _ { 2 }$ 的泊松括号 $\{ F _ { 1 } , F _ { 2 } \}$ 为零, 则相应的对称也是交换的.

哈密顿量诱导 泊松对称 (Poisson symmetry) , 即保持泊松括号. 具体地讲, 张量$h ^ { i j } ( x )$ 关于向量场 $f ^ { i } ( x ) = \{ F ( x ) , x ^ { i } \}$ 的李导数为零:

$$
{ \mathcal { L } } _ { f } h ^ { i j } ( x ) \equiv f ^ { k } { \frac { \partial h ^ { i j } } { \partial x ^ { k } } } - { \frac { \partial f ^ { i } } { \partial x ^ { k } } } h ^ { k j } - h ^ { i k } { \frac { \partial f ^ { j } } { \partial x ^ { k } } } = 0 .
$$

反之, 对于非退化泊松括号 (即 $\operatorname* { d e t } ( h ^ { i j } ) \neq 0 )$ , 则任何泊松对称在局部上都对应关于某个哈密顿量 $F ( x )$ 的哈密顿系统. 函数 $F ( x )$ 称为该泊松对称的生成元. 若该泊松对称也是以 $H ( x )$ 为哈密顿量的另一个哈密顿系统的对称, 则 $A ( x ) : = \{ H , F \}$ 为泊松括号的零化子. 非退化泊松括号的情况下, $A ( x )$ 恒为常值.

这些性质是对原系统进行哈密顿约化以及在完全可积性理论的要点.

例子 1. 常值泊松括号. 此时 $h ^ { i j }$ 为任意的常值反对称矩阵, 雅可比恒等式显然成立.若 $N = 2 n$ 且 $\operatorname* { d e t } ( h ^ { i j } ) \neq 0$ , 则可取局部坐标 $( x ^ { 1 } , . . . , x ^ { n } ) = ( q ^ { 1 } , . . . , q ^ { n } ; p _ { 1 } , . . . , p _ { n } )$ 使得

$$
\{ p _ { i } , q ^ { j } \} = \delta _ { i } ^ { j } , \quad \{ q ^ { i } , q ^ { j } \} = \{ p _ { i } , p _ { j } \} = 0 ,
$$

(典范坐标).

相应的哈密顿系统具有如下的典范形式:

$$
{ \dot { q } } ^ { i } = { \frac { \partial H } { \partial p _ { i } } } , \quad { \dot { p } } { \boldsymbol { i } } = - { \frac { \partial H } { \partial q ^ { i } } } , \quad { \boldsymbol { i } } = 1 , . . . , n .
$$

众所周知, 欧拉-拉格朗日方程

$$
\delta \int L ( q , \dot { q } , \ddot { q } , . . . , q ^ { ( n ) } ) \mathrm { d } t = 0
$$

可通过 Legendre 变换来写成哈密顿的形式 (对非退化的拉格朗日量 $L$ ). 在最简单的$L = L ( q , \dot { q } )$ 情形, 相应的泊松括号正是某个流形 $Q$ (经典力学的位形空间) 的余切丛$P = T ^ { * } Q$ 上的常值泊松括号. (此情形下, 泊松括号在整体上是常值的). 相空间 $P$ 配以典范泊松括号下的任何哈密顿系统都能写为如下的拉格朗日形式:

$$
\delta \int ( p _ { i } \dot { q } ^ { i } - H ( p , q ) ) \mathrm { d } t = 0 ,
$$

其中我们要将 ${ \dot { q } } ^ { i } = { \frac { \partial H } { \partial p _ { i } } } \quad$ 代入 $p _ { i } = p _ { i } ( q , \dot { q } )$ . 这种形式在定性研究哈密顿系统时有时很有用.

例子 2. 磁场. 对于位形空间 $Q$ 上的闭 2-形式 $\Omega = \frac { 1 } { 2 } \Omega _ { i j } ( q ) \mathrm { d } q ^ { i } \wedge \mathrm { d } q ^ { j }$ , $\mathrm { d } \Omega = 0$ , 定义如下的泊松括号 $\{ , \} _ { \Omega }$ :

$$
{ } \{ p _ { i } , q ^ { j } \} _ { \Omega } = \delta _ { i } ^ { j } , \quad \{ q ^ { i } , q ^ { j } \} _ { \Omega } = 0 , \quad { } \{ p _ { i } , p _ { j } \} _ { \Omega } = \Omega _ { i j } ( q ) .
$$

局部上, 我们可以引入“矢势”(1-形式) $\textstyle | A = A _ { i } \mathrm { d } q ^ { i }$ 使得 $\Omega = \mathrm { d } A$ . 则 (局部上) 通过以下变换公式

$$
\tilde { q } ^ { i } = q ^ { i } , \quad \tilde { p } _ { i } = p _ { i } - A _ { i } ( q )
$$

可构造出典范坐标 $( \tilde { q } ^ { i } , \tilde { p } _ { i } )$ . 在整体上将泊松括号化为常值的障碍, 是微分形式 $\Omega$ 所在的流形 $Q$ 的上同调类. 该运动方程可写成欧拉-拉格朗日形式

$$
\frac { \delta S [ q ] } { \delta q ( t ) } = 0 , \quad S [ q ] = \int L ( q , \dot { q } ) \mathrm { d } t - \int A _ { i } ( q ) \mathrm { d } q ^ { i } ,
$$

其中 $L ( q , \dot { q } ) = p _ { i } \dot { q } ^ { i } - H ( p , q )$ , ${ \dot { q } } ^ { i } = { \frac { \partial H } { \partial p _ { i } } } \quad$ 而整体地 (对于非恰当的 $\Omega$ ), 我们得到多值作用泛函 $S$ . 此时我们无法确切定义泛函 $S$ (因为 1-形式 $A _ { i } ( q )$ 无法整体定义), 但其变分$\delta S$ 是良好定义的, 并且是由全体路径 $q ( t )$ 构成的空间上的闭 1-形式. 这是 Dirac 单极点类型的一种情形. 经典力学中的一些系统 (例如轴对称场中的陀螺, 浸入流体之中的刚体... 等等) 在去掉“循环变量”之后也能表示为如此形式. 无限维 (也就是场论) 版本的这种多值泛函由 Novikov 在 80 年代初所引入, 并被 Witten 等人使用. 多值泛函的Morse 理论的基本想法可参见 [10].

# 例子 3. 线性泊松括号.

$$
h ^ { i j } ( x ) = c _ { k } ^ { i j } x ^ { k } , \quad c _ { k } ^ { i j } \equiv { \stackrel { \mathrm { \tiny ~ * ~ } } { \Pi } } { } ^ { * } { \stackrel { \mathrm { \tiny ~ * ~ } } { \ast } } { \mit \Psi } .
$$

此时, 相空间 $P$ 上的线性泛函之全体构成李代数:

$$
a = a _ { i } x ^ { i } , \quad b = b _ { i } x ^ { i } \implies \{ a , b \} = c = c _ { i } x ^ { i } , \quad c _ { k } = a _ { k } b _ { j } c _ { k } ^ { i j } .
$$

因此对偶空间 $P ^ { * }$ 为李代数, $P ^ { * } = L$ , 并且其结构常数为 $c _ { k } ^ { i j }$ , $P = L ^ { * }$ (相空间是李代数的对偶). 李代数的对偶空间上的如此的泊松括号也称为 李-泊松括号 (Lie-Poissonbracket) , 其通常是退化的. 相应的辛叶为以 $L$ 为李代数的李群 $G$ 的在 $L ^ { * }$ 上的余伴随表示 $\operatorname { a d } ^ { * }$ 的轨道. 在这些轨道上的相应的辛结构正是众所周知的 Kirillov-Konstant 辛结构.

例如, $\mathbb { R } ^ { 3 }$ 的刚体运动群 $E ( 3 )$ 的李代数的李-泊松括号为如下:

$$
\{ M _ { i } , M _ { j } \} = \varepsilon _ { i j k } M _ { k } , ~ \{ M _ { i } , p _ { j } \} = \varepsilon _ { i j k } p _ { k } , ~ \{ p _ { i } , p _ { j } \} = 0 ,
$$

$i , j , k = 1 , . . . , 3$ . 其秩为 4, 相应的辛叶由方程

$$
p ^ { 2 } \equiv \sum _ { i } p _ { i } ^ { 2 } = \frac { \cdot \mathrm { s } \cdot p } { \mathrm { H } ^ { 2 } } \frac { \cdot \mathrm { s } \cdot p } { \bar { \bar { \xi } } \bar { \bar { \xi } } } \chi > 0 , \quad M p \equiv \sum _ { i } M _ { i } p _ { i } = \frac { \cdot \mathrm { s } \cdot p } { \mathrm { H } }
$$

所给定. 变量代换

$$
( M _ { i } , p _ { j } ) \mapsto ( \tilde { M } _ { i } = M _ { i } - \lambda p _ { i } , \tilde { p } _ { j } = p _ { j } ) , \lambda = \frac { M p } { p ^ { 2 } }
$$

给出了此辛叶与二维球面的余切丛

$$
\sum _ { i } \tilde { p } _ { i } ^ { 2 } = \stackrel {  } { \ P } \stackrel {  } { \ast } \acute { \chi } , \quad \sum _ { i } \tilde { M } _ { i } \tilde { p } _ { i } = 0
$$

的同构.

习题: 证明该辛叶上的泊松括号与例子 2 中的磁场是等价的. 并且当 $M P \ne 0$ 时,相应的磁场的上同调类非零.

对任意哈密顿量 $H = H ( M , p )$ , 运动方程可写为如下形式:

$$
\left\{ \begin{array} { l l } { \dot { \pmb { p } } = [ \pmb { p } , \omega ] , } & { \left( \omega = \frac { \partial H } { \partial M } \right) } \\ { \dot { \pmb { M } } = [ \pmb { M } , \omega ] + [ \pmb { p } , \pmb { u } ] , } & { \left( \pmb { u } = \frac { \partial H } { \partial \pmb { p } } \right) . } \end{array} \right.
$$

而对二次哈密顿量 $H ( M , p )$ , 此方程恰为刚体在理想流体中运动的 Kirchhoff 方程.

至于线性非齐次情形

$$
\begin{array} { r }  h ^ { i j } ( x ) = c _ { k } ^ { i j } x ^ { k } + c _ { 0 } ^ { i j } , \quad c _ { k } ^ { i j } , c _ { 0 } ^ { i j } = \overset { \underset { \mathrm { r e f } } { \mathrm { a r } } } { \underset { \mathrm { r e f } } { \mathrm { a r } } } \overset { \ast \} { \underset { \mathrm { b l } } { \mathrm { b r } } } , } \end{array}
$$

矩阵元 $c _ { 0 } ^ { i j } = - c _ { 0 } ^ { j i }$ 构成以 $c _ { k } ^ { i j }$ 为结构常数的李代数 $L$ 上的二维上链 (cocycle). 也就是说,

$$
c _ { s } ^ { i j } c _ { 0 } ^ { s k } + c _ { s } ^ { j k } c _ { 0 } ^ { s i } + c _ { s } ^ { k i } c _ { 0 } ^ { s j } = 0 .
$$

此时, 所有的形如 $a ( x ) = a _ { i } x ^ { i } + a _ { 0 }$ 的函数在此泊松括号下通过上链 $c _ { 0 } ^ { i j }$ 构成李代数 $L$ 的一个中心扩张:

$$
a ( x ) = a _ { i } x ^ { i } + a _ { 0 } , \quad b ( x ) = b _ { i } x ^ { i } + b _ { 0 } , \quad \{ a , b \} = c ( x ) = c _ { i } x ^ { i } + c _ { 0 } ,
$$

$$
c _ { k } = c _ { k } ^ { i j } a _ { i } b _ { j } , \quad c _ { 0 } = c _ { 0 } ^ { i j } a _ { i } b _ { j } .
$$

上链 $c _ { 0 } ^ { i j }$ 上同调于零当且仅当存在向量 $( x _ { 0 } ^ { 1 } , . . . , x _ { 0 } ^ { N } )$ 使得

$$
c _ { 0 } ^ { i j } = c _ { k } ^ { i j } x _ { 0 } ^ { k } .
$$

此时通过变量代换 $x ^ { i } \mapsto x ^ { i } + x _ { 0 } ^ { i }$ 可将泊松括号化为齐次的.

例子 4. 线性化 Yang-Baxter 方程与二次泊松括号. (Sklyanin-Drinfel’d, 见 [3,24]).设 $r = ( r _ { k l } ^ { i j } )$ 为所谓的经典 $r .$ -矩阵, 即满足如下的线性化 Yang-Baxter 方程:

$$
[ r _ { 1 2 } , r _ { 1 3 } ] + [ r _ { 1 2 } , r _ { 2 3 } ] + [ r _ { 1 3 } , r _ { 2 3 } ] = 0
$$

以及“酉条件”

$$
r _ { l k } ^ { j i } = - r _ { k l } ^ { i j } .
$$

这里

$$
\begin{array} { r } { ( r _ { 1 2 } ) _ { j _ { 1 } j _ { 2 } j _ { 3 } } ^ { i _ { 1 } i _ { 2 } i _ { 3 } } = r _ { j _ { 1 } j _ { 2 } } ^ { i _ { 1 } i _ { 2 } } \delta _ { j _ { 3 } } ^ { i _ { 3 } } , } \\ { ( r _ { 1 3 } ) _ { j _ { 1 } j _ { 2 } j _ { 3 } } ^ { i _ { 1 } i _ { 2 } i _ { 3 } } = r _ { j _ { 1 } j _ { 3 } } ^ { i _ { 1 } i _ { 3 } } \delta _ { j _ { 2 } } ^ { i _ { 2 } } , } \\ { ( r _ { 2 3 } ) _ { j _ { 1 } j _ { 2 } j _ { 3 } } ^ { i _ { 1 } i _ { 2 } i _ { 3 } } = r _ { j _ { 2 } j _ { 3 } } ^ { i _ { 2 } i _ { 3 } } \delta _ { j _ { 1 } } ^ { i _ { 1 } } . } \end{array}
$$

如此的 $r .$ -矩阵定义了矩阵 $( t _ { j } ^ { i } )$ 空间上的一个二次泊松括号:

$$
\{ t _ { k } ^ { i } , t _ { l } ^ { j } \} = r _ { a b } ^ { i j } t _ { k } ^ { a } t _ { l } ^ { b } - t _ { a } ^ { i } t _ { b } ^ { j } r _ { k l } ^ { a b } ,
$$

或者写成紧凑形式,

$$
\{ T \stackrel { \otimes } { , } T \} = [ r , T \otimes T ] , \quad T = ( t _ { j } ^ { i } ) .
$$

此泊松括号是量子群中如下交换关系的半经典极限:

$$
R T _ { 1 } T _ { 2 } = T _ { 2 } T _ { 1 } R , \quad T = ( t _ { j } ^ { i } ) , \quad T _ { 1 } = T \otimes 1 , \quad T _ { 2 } = 1 \otimes T .
$$

这里的变量 $t _ { j } ^ { i }$ 可被看作量子群中非交换的坐标.

矩阵 $R = ( R _ { k l } ^ { i j } ) _ { \sf K }$ 指标 $k , l$ 固定 满足经典 Yang-Baxter 方程

$$
R ^ { 1 2 } R ^ { 1 3 } R ^ { 2 3 } = R ^ { 2 3 } R ^ { 1 3 } R ^ { 1 2 } .
$$

取半经典极限, 有

$$
R _ { k l } ^ { i j } = \delta _ { k l } ^ { i j } + \hbar r _ { k l } ^ { i j } , \hbar  0 , \quad [ t _ { k } ^ { i } , t _ { l } ^ { j } ] = - \hbar \{ t _ { k } ^ { i } , t _ { l } ^ { j } \} + o ( \hbar ) .
$$

以下公式也给出了二次泊松括号的其它例子:

$$
\{ T \stackrel { \otimes } { , } T \} _ { \cal R } = r \cdot T \otimes T , \quad \{ T \stackrel { \otimes } { , } T \} _ { \cal L } = T \otimes T \cdot r .
$$

上述任何一个泊松括号反对称性与雅可比恒等式都等价于 Yang-Baxter 方程与酉条件.这些泊松括号是相容的, 这是指它们的任何线性组合依然是泊松括号. $\{ , \} _ { R }$ 与 $\{ , \} _ { L }$ 分别为线性群上的右, 左不变泊松括号.

若 $r = { \mathfrak { g } } \otimes { \mathfrak { g } }$ (其中 $\mathfrak { g }$ 为矩阵李代数) 3, 则二次泊松括号 $\{ , \} , \{ , \} _ { R }$ 与 $\{ , \} _ { L }$ 可定义在相空间 $P = G$ 上, 其中 $G$ 为相应的李群. $G$ 配以泊松括号 $\{ , \}$ 构成了一个 哈密顿-李群 (Hamiltonian-Lie group) , 即群乘法 $G \times G \to G$ 为泊松流形之间的映射, 其中$G \times G$ 配以泊松括号的“直积”.

# 补充内容: 哈密顿-李群与量子群

根据 Drinfel’d[4] 的观点, 哈密顿-李群是量子群的半经典极限.

有两种方式来理解此观点. (在某种意义下其中一种是另一种的对偶). 第一种观点代表了量子化的思想. 我们考虑哈密顿-李群 $G$ 上的函数构成的线性空间 $\mathcal { A } _ { 0 }$ . (这里的“函数”为某些恰当的类型, 例如对于矩阵群 $G$ , 我们应考虑关于其矩阵元的多项式函数). 则该空间具有如下的结构:

1. 关于通常的函数乘法构成交换代数: $f _ { 1 } ( x ) \cdot f _ { 2 } ( x ) , ( x \in G )$ ;

2. $G$ 上的乘法定义了对角映射

$$
\triangle : { \cal A } _ { 0 }  { \cal A } _ { 0 } \otimes { \cal A } _ { 0 } , \quad ( \triangle f ) ( x , y ) = f ( x \cdot y ) .
$$

在上述两种运算下, $\mathcal { A } _ { 0 }$ 构成交换结合 Hopf 代数, 也就是说满足如下: (i) 对角映射为代数同态, (ii) 对角映射是 余结合 (co-associative) 的 (此性质与群 $G$ 乘法

$$
c _ { \mu \nu } ^ { \alpha } r ^ { \mu \beta } r ^ { \nu \gamma } + r ^ { \alpha \mu } c _ { \mu \nu } ^ { \beta } r ^ { \nu \gamma } + r ^ { \alpha \mu } r ^ { \beta \nu } c _ { \mu \nu } ^ { \gamma } = 0
$$

的结合性可得), (iii) $\mathcal { A } _ { 0 }$ 具有单位元 $C  A _ { 0 } ( C$ 指常函数), 以及 (iv) 余单位元${ \mathcal { A } } _ { 0 } \mapsto C$ , $f \mapsto f ( e )$ , 其中 $e \in G$ 为群 $G$ 的乘法单位元. 这些映射所满足的公理是我们熟知的. (此外, $\mathcal { A } _ { 0 }$ 还满足: (v) $\mathcal { A } _ { 0 }$ 具有对极同态 $f ( x ) \mapsto f ( x ^ { - 1 } )$ , 但我们在此不去探讨它).

3. 泊松括号 $\{ , \}$ 给出了 $\mathcal { A } _ { 0 }$ 的另一个反对称双线性算子 $\mathcal { A } _ { 0 } \otimes \mathcal { A } _ { 0 }  \mathcal { A } _ { 0 }$ , $f _ { 1 } , f _ { 2 } \mapsto$ $\{ f _ { 1 } , f _ { 2 } \}$ .

上述这些结构在后文将介绍的某种意义下是相容的. 这由泊松括号, 李群, 哈密顿-李群的定义可知. 为将上述内容量子化, 我们要构造一个 (与小参数 $\hbar$ 有关的) 非交换的代数 $\mathcal { A }$ , 使得对任意 $f _ { 1 } , f _ { 2 }$ 都成立

$$
f _ { 1 } f _ { 2 } - f _ { 2 } f _ { 1 } = \hbar \{ f _ { 1 } , f _ { 2 } \} + o ( \hbar ) .
$$

自然地, 我们也假设对角映射 $\triangle$ 也定义在“量子化”代数 $\mathcal { A }$ 上. 更确切地讲, 下述断言成立: [4]

引理. 设 $\mathcal { A }$ 为与小参数 $\hbar$ 有关的 Hopf 代数, 并且 $\mathcal { A } / \hbar \mathcal { A }$ 同构于由某个李群 $G$ 上的函数构成的 Hopf 代数 $\mathcal { A } _ { 0 }$ . 则算子

$$
\{ f _ { 1 } , f _ { 2 } \} = \frac { f _ { 1 } f _ { 2 } - f _ { 2 } f _ { 1 } } { \hbar } \mod \hbar \cal { A }
$$

定义了 $G$ 的哈密顿-李群结构.

该 Hopf 代数 $\mathcal { A }$ 可视为“量子化的李群 $G ^ { \dprime }$ 上的函数代数 (但某些点集构成的群不能被如此“量子化”) 或者“ $G$ 上的函数代数的 $\hbar .$ -形变”. 例如在之前的例子中, 含幺结合代数 $\mathcal { A }$ 具有生成元 $t _ { j } ^ { i }$ , 满足二次关系

$$
R T _ { 1 } T _ { 2 } = T _ { 2 } T _ { 1 } R
$$

对角映射

$$
\triangle ( t _ { j } ^ { i } ) = t _ { k } ^ { i } \otimes t _ { j } ^ { k }
$$

以及余单位元 $\varepsilon ( t _ { j } ^ { i } ) = \delta _ { j } ^ { i }$ . 上述性质的验证都是直接的.

于是, 量子群 (quantum group) 的定义非常简单: 它是非交换的 Hopf 代数 $\mathcal { A }$ (它也是非余交换的, 即对偶代数 $\mathcal { A } ^ { \prime }$ 也非交换), 但它是某个交换 Hopf 代数的形变.

当然, 若按上述解释, 我们难以看出 Yang-Baxter 方程在一般的“量子群的理论”中起到的作用. 我打算稍后再探讨此问题.

另一种观点 (前一种的对偶) 是考虑“泛包络代数 $\mathcal { U } { \mathfrak { g } }$ 的量子化”. 我们回顾, 李代数 $\mathfrak { g }$ 的泛包络代数 $\mathcal { U } { \mathfrak { g } }$ 是由 $\mathfrak { g }$ 中的元素构成的非交换的多项式所构成. 它在对角映射

$$
\triangle _ { 0 } a = a \otimes 1 + 1 \otimes a
$$

(此对角映射是余交换的) 的意义下构成 Hopf 代数. $\mathcal { U } { \mathfrak { g } }$ 的量子化是指 (与小参数 $\hbar$ 有关) 的 Hopf 代数 $\mathcal { A }$ , 并且满足

$$
\mathcal { A } / \hbar \mathcal { A } \cong \mathcal { U } \mathfrak { g }
$$

(Hopf 代数的同构). 这里的 Hopf 代数 $\mathcal { A }$ 通常记作 $\mathcal { U } _ { \hbar } \mathfrak { g }$ (或者 $\mathcal { U } _ { q } { \mathfrak { g } }$ , $q = \exp \hbar$ ), 称为泛包络代数 $\mathcal { U } { \mathfrak { g } }$ 的 $\hbar \cdot$ -形变 (或者 $q \mathrm { . }$ -形变). 他也可以被认为是“量子群 (或者其李代数) 的泛包络代数”.

上述的量子化方法与哈密顿-李群之间的关系并不是太明显. 为说明它, 我需要说明(李群) $G$ 的哈密顿-李群的结构 (假定 $G$ 是连通且单连通的) 由其李代数 $\mathfrak { g }$ 的对偶空间${ \mathfrak { g } } ^ { * }$ 上的给定的李代数结构所唯一决定. 其中 $\mathfrak { g }$ 与 ${ \mathfrak { g } } ^ { * }$ 的李代数结构在某种意义下要相容.设 $I _ { * } ^ { \alpha }$ 为 ${ \mathfrak { g } } ^ { * }$ 的一组基, $I _ { \alpha }$ 为 $\mathfrak { g }$ 的相应的对偶基. 记 $f _ { \gamma } ^ { \alpha \beta }$ 为 ${ \mathfrak { g } } ^ { * }$ 的结构常数:

$$
[ I _ { * } ^ { \alpha } , I _ { * } ^ { \beta } ] = f _ { \gamma } ^ { \alpha \beta } I _ { * } ^ { \gamma } .
$$

则系数 $f _ { \gamma } ^ { \alpha \beta }$ 定义了 $H ^ { 1 } ( { \mathfrak { g } } , { \mathfrak { g } } \otimes { \mathfrak { g } } )$ 中的一个 1-上链 (cocycle), (也就是线性映射 ${ \mathfrak { g } } \to$ ${ \mathfrak { g } } \otimes { \mathfrak { g } }$ , $I _ { \gamma } \mapsto f _ { \gamma } ^ { \alpha \beta } I _ { \alpha } \otimes I _ { \beta } )$ , 并且需要满足下述关系

$$
c _ { \rho \lambda } ^ { \varepsilon } f _ { \varepsilon } ^ { \mu \nu } = c _ { \varepsilon \lambda } ^ { \mu } f _ { \rho } ^ { \varepsilon \nu } + c _ { \varepsilon \lambda } ^ { \nu } f _ { \rho } ^ { \mu \varepsilon } - c _ { \varepsilon \rho } ^ { \mu } f _ { \lambda } ^ { \varepsilon \nu } - c _ { \varepsilon \rho } ^ { \nu } f _ { \lambda } ^ { \mu \varepsilon } .
$$

(Drinfel’d 将这样的 $\mathfrak { g }$ 称为 李双代数 (Lie bi-algebra) .)

对于哈密顿-李群, 系数 $f _ { \gamma } ^ { \alpha \beta }$ 的具体构造如下. 设 $\partial _ { \alpha }$ 为 $G$ 的左不变向量场构成的一组基, 设在该基下泊松括号 $\{ , \}$ 的系数矩阵为 $\eta ^ { \alpha \beta } = \eta ^ { \alpha \beta } ( x )$ , 即

$$
\{ f , g \} = \eta ^ { \alpha \beta } ( x ) \partial _ { \alpha } f ( x ) \partial _ { \beta } g ( x ) .
$$

则我们定义

$$
f _ { \gamma } ^ { \alpha \beta } = \partial _ { \gamma } \eta ^ { \alpha \beta } ( x ) | _ { x = e } .
$$

反过来, 也可从结构常数 $f _ { \gamma } ^ { \alpha \beta }$ 来将泊松括号 $\{ , \}$ 恢复出来, 这只需要求解以解线性微分方程的初值问题

$$
\left\{ \begin{array} { l l } { { \partial _ { \lambda } \eta ^ { \mu \nu } = c _ { \varepsilon \lambda } ^ { \mu } \eta ^ { \varepsilon \nu } + c _ { \varepsilon \lambda } ^ { \nu } \eta ^ { \mu \varepsilon } + f _ { \lambda } ^ { \mu \nu } } } \\ { { \eta ^ { \alpha \beta } ( x ) | _ { x = e } = 0 . } } \end{array} \right.
$$

上述超定的微分方程组的相容性条件由 $f _ { \gamma } ^ { \alpha \beta }$ 所满足的前面给出的那个方程所保证.

在我们的二次泊松括号的例子中, $f _ { \gamma } ^ { \alpha \beta }$ 为 上边缘 (coboundary) :

$$
f _ { \gamma } ^ { \alpha \beta } = c _ { \varepsilon \gamma } ^ { \alpha } r ^ { \varepsilon \beta } + c _ { \varepsilon \gamma } ^ { \beta } r ^ { \alpha \varepsilon } , \quad r ^ { \alpha \beta } = - r ^ { \beta \alpha } .
$$

此结构常数 $f _ { \gamma } ^ { \alpha \beta }$ 的雅可比恒等式由 $r ^ { \alpha \beta }$ 所满足的线性 Yang-Baxter 方程所保证. $G$ 上的泊松括号具有如下的显式表达式:

$$
\{ f , g \} = r ^ { \alpha \beta } ( \partial _ { \alpha } f \partial _ { \beta } g - \partial _ { \alpha } ^ { \prime } f \partial _ { \beta } ^ { \prime } g )
$$

其中 $\partial _ { \alpha } ^ { \prime }$ 为 $G$ 的关于 $\mathfrak { g }$ 的基向量 $I _ { \alpha }$ 的右不变向量场.

现在回到泛包络代数的量子化. 以下引理成立 [4]:

引理. 设 $\mathcal { A }$ 为与小参数 $\hbar$ 有关的 Hopf 代数, 并且 $\mathcal { A } / \hbar \mathcal { A }$ 同构于 Hopf 代数 $\mathcal { U } { \mathfrak { g } }$ .则映射 $f ( a ) = { \frac { \triangle ( a ) - \triangle ^ { \prime } ( a ) } { \hbar } }$ mod $\hbar$ , $a \in { \mathfrak { g } } \in \mathcal { U } { \mathfrak { g } }$ 定义了 $\mathfrak { g }$ 的李双代数结构. (这里的 $\triangle ^ { \prime }$ 与 $\triangle$ 相差一个对换: 若 $\triangle ( a ) = \sum a _ { i } \otimes b _ { i }$ , 则 $\triangle ^ { \prime } ( a ) = \sum b _ { i } \otimes a _ { i } )$ .

上述表述将 Hopf 代数 $\mathcal { U } _ { \hbar } \mathfrak { g }$ 看作量子化的泛包络代数, 其半经典极限与给定的哈密顿-李群是一致的.

其最简单 (也可能是最重要) 的例子 (Jimbo, Drinfel’d) 是 ${ \mathfrak { g } } = { \mathfrak { s l } } ( 2 )$ 的泛包络代数的量子形变. 代数 $\mathcal { U } _ { \hbar } \mathfrak { s l } ( 2 )$ 由 $H , X ^ { + } , X ^ { - }$ 所生成, 其生成关系为

$$
[ H , X ^ { + } ] = \pm 2 X ^ { \pm } , \quad [ X ^ { + } , X ^ { - } ] = 2 \hbar ^ { - 1 } \sinh ( \hbar H / 2 ) .
$$

对角映射 $\triangle$ 定义为

$$
\triangle ( H ) = H \otimes 1 + 1 \otimes H , \quad \triangle ( X ^ { \pm } ) = X ^ { \pm } \otimes \exp ( \hbar H / 4 ) + \exp ( - \hbar H / 4 ) \otimes X ^ { \pm } .
$$

现在我们来谈谈与量子 Yang-Baxter 方程的关系. 有一类称为 拟三角 Hopf 代数(quasi-triangular Hopf algebra) 的特殊的 Hopf 代数 (此概念也是由 Drinfel’d 引入的).其主要想法来自于 Hopf 代数的表示论.

设 $V , W$ 为结合代数 $\mathcal { A }$ 的两个表示, 则有 $A \otimes A$ 自然地作用于 $V \otimes W$ . 而若 $\mathcal { A }$ 为 Hopf 代数, 则我们可通过对角映射 $\triangle : { \mathcal { A } }  { \mathcal { A } } \otimes { \mathcal { A } }$ 来定义 $\mathcal { A }$ 在 $V \otimes W$ 上的作用. 如此定义的表示的张量积显然是结合的, 但当 $\triangle ^ { \prime } \ne \triangle$ 时此张量积非交换 (回顾: 若$\triangle ( a ) = \sum a _ { i } \otimes b _ { i }$ , 则 $\triangle ^ { \prime } ( a ) = \sum b _ { i } \otimes a _ { i } )$ . Hopf 代数 $\mathcal { A }$ 称为拟三角的, 若存在可逆元$R \in { \cal { A } } \otimes { \cal { A } }$ 使得

$$
\triangle ^ { \prime } ( a ) = R \triangle ( a ) R ^ { - 1 } , \quad \forall a \in \mathcal { A } .
$$

此时表示 $V \otimes W$ 与 $W \otimes V$ 在下述“交换同构”映射下是同构的:

$$
C : V \otimes W \to W \otimes V , \quad C = C _ { 0 } R _ { V , W } ,
$$

其中 $C _ { 0 }$ 为线性空间之间的显然的同构 $V \otimes W \ { \stackrel { \approx } { \to } } \ W \otimes V$ , $R _ { V , W }$ 为关于 $R$ 的算子$V \otimes W \to V \otimes W$ . 交换性与结合性的同构的一些相容性条件应当满足 (细节详见Drinfel’d 的 Berkeley ICM-86 talk). 它们可以写成如下形式:

$$
( \triangle \otimes \mathrm { i d } ) ( R ) = R ^ { 1 3 } R ^ { 2 3 } , \quad ( \mathrm { i d } \otimes \triangle ) ( R ) = R ^ { 1 3 } R ^ { 1 2 } .
$$

这里的 $R ^ { 1 2 } , R ^ { 1 3 } , R ^ { 2 3 }$ 为 $\mathcal { A } \otimes \mathcal { A } \otimes \mathcal { A }$ 中的元素, 且

$$
R ^ { 1 2 } = \sum r _ { i } ^ { \prime } \otimes r _ { i } ^ { \prime \prime } \otimes 1 , \quad R ^ { 1 3 } = \sum r _ { i } ^ { \prime } \otimes 1 \otimes r _ { i } ^ { \prime \prime } , \quad R ^ { 2 3 } = \sum 1 \otimes r _ { i } ^ { \prime } \otimes r _ { i } ^ { \prime \prime } ,
$$

其中 $R = \sum r _ { i } ^ { \prime } \otimes r _ { i } ^ { \prime \prime }$ . 从这三个等式立刻得到 ( $\mathcal { A } \otimes \mathcal { A } \otimes \mathcal { A }$ 中的) Yang-Baxter 方程为

$$
R ^ { 1 2 } R ^ { 1 3 } R ^ { 2 3 } = R ^ { 2 3 } R ^ { 1 3 } R ^ { 1 2 } .
$$

正因为此, $R$ 常被称为“万有 $R$ -矩阵”. 对于 $\mathcal { A }$ 的任何表示, 都能得到矩阵元为数字的$R \mathrm { . }$ -矩阵.

在量子化李代数 ${ \mathfrak { s l } } ( 2 )$ 的例子中, $( \mathcal { U } _ { \hbar } \mathfrak { s l } ( 2 ) \otimes \mathcal { U } _ { \hbar } \mathfrak { s l } ( 2 )$ 中的) 万有 $R \mathrm { . }$ -矩阵为如下:

$$
R = \sum _ { k = 0 } ^ { \infty } p _ { k } ( \hbar ) \left\{ \exp { \frac { \hbar } { 4 } } [ H \otimes H + k ( H \otimes 1 - 1 \otimes H ) ] \right\} ( X ^ { + } ) ^ { k } \otimes ( X ^ { - } ) ^ { k } ,
$$

其中

$$
p _ { k } ( \hbar ) = \hbar ^ { k } e ^ { - \frac { k \hbar } { 2 } } \prod _ { r = 1 } ^ { k } \frac { e ^ { \hbar } - 1 } { e ^ { r \hbar } - 1 } .
$$

# 1.2 完全可积系统及其摄动. 平均化方法

来说一下 完全可积性 (complete integrability) . 此概念是 Liouville 基于对可分离的系统的分析而提出的. 完全可积系统首先是哈密顿系统, 配以 $2 n$ 维相空间中的哈密顿量 $H$ , 非退化的泊松括号, 以及 $n$ 个两两独立且交换的守恒律 $I _ { 1 } , . . . , I _ { n }$ ,

$$
\left\{ I _ { i } , I _ { j } \right\} = 0 .
$$

由于 $I _ { 1 } , . . . , I _ { n }$ 的独立性, 其 等值面 (level surface) 的切空间由 $I _ { 1 } , . . . , I _ { n }$ 的斜梯度所张成. 且这些斜梯度两两交换. 于是群 $\mathbb { R } ^ { n }$ 在等值面的任何一个连通分支上的作用都可迁. 于是这些等值面的任何紧致光滑连通分支

$$
I _ { 1 } = c _ { 1 } , . . . , I _ { n } = c _ { n }
$$

是 $n$ 维环面 $T ^ { n } = { \cal T } ^ { n } ( c _ { 1 } , . . . , c _ { n } )$ . 在环面 $T ^ { n } = { \cal T } ^ { n } ( c _ { 1 } , . . . , c _ { n } )$ 附近存在典范坐标$J _ { 1 } , . . . , J _ { n } , \varphi _ { 1 } , . . . , \varphi _ { n }$ 使得 $\{ J _ { i } , \varphi _ { j } \} = \delta _ { i j }$ 并且其余泊松括号为零. 这是所谓的“作用量-角参数”— $\varphi _ { 1 } , . . . , \varphi _ { n }$ 是该 $T ^ { n }$ 附近的任何一个环面 $T ^ { n } ( c _ { 1 } , . . . , c _ { n } )$ 上的坐标, 而$J _ { 1 } , . . . , J _ { n }$ (在这些环面上) 为 (与 $c _ { 1 } , . . . , c _ { n }$ 有关的) 常数. 该完全可积系统的哈密顿量$H$ 形如 $H = H ( J _ { 1 } , . . . , J _ { n } )$ , 从而该系统的演化方程形如

$$
\left. \begin{array} { l } { \dot { J } _ { i } = 0 } \\ { \dot { \varphi } _ { i } = \omega _ { i } ( J _ { 1 } , . . . , J _ { n } ) } \end{array} \right\} i = { 1 , . . . , n } ,
$$

其中 ωi = $\omega _ { i } = \frac { \partial H } { \partial J _ { i } }$ 该系统在 Liouville 环面上的运动是周期的或者近似周期的, 角参数为时

间 $t$ 的线性函数, 即 $\omega = ( \omega _ { 1 } , . . . , \omega _ { n } )$ 为相应的频率向量. 哈密顿系统 $\frac { \mathrm { d } x ^ { a } } { \mathrm { d } t } = \{ H ( x ) , x ^ { a } \}$ 相应的解为关于时间 $t$ 的周期函数或近似周期函数, 且形如

$$
x ^ { a } ( t ) = X ^ { a } ( \omega t + \varphi ^ { 0 } ; c ) , \quad a = 1 , . . . , 2 n .
$$

这里的函数 $X ^ { a } = X ^ { a } ( \varphi ; c )$ 关于每个 $\varphi _ { i }$ 都是 $2 \pi \cdot$ -周期的; $\varphi = ( \varphi _ { 1 } , . . . , \varphi _ { n } )$ , 与参数$\pmb { c } = ( c _ { 1 } , . . . , c _ { n } )$ 有关; 相位 $\varphi ^ { 0 } = ( \varphi _ { 1 } ^ { 0 } , . . . , \varphi _ { n } ^ { 0 } )$ 为任意向量.

作用量 $J _ { i }$ 可如下构造. 对于标准的相空间 $\mathbb { R } ^ { 2 n }$ , 典范坐标 $( p _ { 1 } , . . . , p _ { n } , q ^ { 1 } , . . . , q ^ { n } )$ , 作用量形如

$$
J _ { i } = { \frac { 1 } { 2 \pi } } \oint _ { \gamma _ { i } } p _ { k } \mathrm { d } q ^ { k } , \quad i = 1 , . . . , n .
$$

这里的 $\gamma _ { i }$ 为环面 $T ^ { n }$ 的第 $i$ 个基本闭路:

在具有辛形式 $\Omega = { \frac { 1 } { 2 } } h _ { i j } \operatorname { d } x ^ { i } \wedge \operatorname { d } x ^ { j }$ 的任意辛相空间中, $\Omega$ 在环面的某个邻域里是恰当的,$\Omega = \mathrm { d } \eta$ . 此时作用量的表达式为

$$
J _ { i } = \frac { 1 } { 2 \pi } \oint _ { \gamma _ { i } } \eta , i = 1 , . . . , n .
$$

而角变量 $\varphi _ { i }$ 可通过生成函数的标准的理论来构造.

对于单自由度哈密顿系统 (若哈密顿量 $H ( p , q )$ 不显含时间, 则该系统必完全可积),作用量-角参数可显式构造. 若哈密顿量的等值线 $H ( p , q ) = E$ 为光滑闭曲线, 则作用量可通过下述公式计算:

$$
J = J ( E ) = { \frac { 1 } { 2 \pi } } \oint _ { H = E } p \mathrm { d } q .
$$

由于

$$
{ \frac { \mathrm { d } J } { \mathrm { d } E } } = \int _ { H = E } { \frac { \mathrm { d } s } { | \mathrm { g r a d } H | } } , \quad \mathrm { d } s = \sqrt { \mathrm { d } p ^ { 2 } + \mathrm { d } q ^ { 2 } } ,
$$

从而 $\mathrm { d } J / \mathrm { d } E \ne 0$ . 取 $J , q$ 为曲线 $H \ = \ E$ 上的某点的某邻域上的局部坐标, 假设$\frac { \partial H } { \partial q } \neq 0$ , 则引入生成函数

$$
S _ { ( q ) } ( J , q ) = \int _ { q _ { 0 } } ^ { q } p ( J , q ^ { \prime } ) \mathrm { d } q ^ { \prime } ,
$$

$$
H ( p ( J , q ) , q ) \equiv E ( J ) .
$$

之后令

$$
\varphi _ { ( q ) } = \frac { \partial S _ { ( q ) } } { \partial J } ,
$$

$\{ J , \varphi _ { ( q ) } \} = 1$ . 而对于 $\frac { \partial H } { \partial p } \neq 0$ 的情况, 我们令

$$
\begin{array} { l l l } & { \displaystyle \varphi _ { ( p ) } = \frac { \partial S _ { ( p ) } } { \partial J } } \\ & { S _ { ( p ) } ( J , p ) = - \int _ { p _ { 0 } } ^ { p } q ( J , p ^ { \prime } ) \mathrm { d } p ^ { \prime } } \\ & { H ( p , q ( J , p ) ) \equiv E ( J ) . } \end{array}
$$

在这些小邻域的公共部分, 由 $\{ J , \varphi _ { ( p ) } - \varphi _ { ( q ) } \} = 0$ 可知 $\varphi _ { ( p ) } - \varphi _ { ( q ) } \equiv$ 常数. 因此我们能够沿着等值线构造角参数 $\varphi$ . 注意此角参数是在模 $2 \pi$ 意义下定义的, 因为

$$
\oint _ { H = E } p \mathrm { d } q = 2 \pi J .
$$

我想强调一点, 当 $n \geq 2$ 时, 不可分离的完全可积系统的作用量-角参数不存在显式表达式 (例如 Novikov 等人近期的工作表明 Kovalevskaja 陀螺的作用量-角参数不存在显示表达).

不幸的是, 一般的动力系统并不是可积的. 若系统 (在某种意义下) 近似是可积的,则我们可以用 摄动理论 (perturbation theory) 来研究它.

假设可以用小参数 $\varepsilon$ 来描述摄动. 摄动理论的最简单的问题是计算摄动后的相曲线 $x _ { \varepsilon } ( t )$ 与未摄动的相曲线 $x ( t )$ 之间的误差 $| x _ { \varepsilon } ( t ) - x ( t ) |$ 的一阶部分. 该误差可以通过求解解 $x ( t )$ 附近的线性化系统来得到. 但这种方法不能提供 $x _ { \varepsilon } ( t )$ 的长时间行为的任何信息, 具体地说, 时间区间在 $\varepsilon ^ { - 1 }$ 量级. 有多种解决此问题的有用的渐近方法, 而Poincaré-Bogolyubov 等人的 平均化方法 (averaging method) 是非线性振动理论中最有效的渐近方法之一.

这种平均化方法用于未摄动的系统为一族闭路, 恰当的周期解 (“单相情形”) 的情形, 或者一组 $m$ 维不变环面, 关于参数 $J = \left( J _ { 1 } , . . . , J _ { k } \right)$ 的拟周期解 (“ $m \cdot$ -相情形”)

$$
x ^ { a } ( t ) = X ^ { a } ( \omega t + \varphi ^ { 0 } ; J )
$$

的情形. 这里的函数 $X ^ { a } ( \varphi , J )$ 关于每个 $\varphi _ { 1 } , . . . , \varphi _ { m }$ 都是 $2 \pi \cdot$ -周期的, $\varphi = ( \varphi _ { 1 } , . . . , \varphi _ { m } )$ 与参数 $J$ 有关. 相空间中这个解族附近的点将沿着该族的环面迅速振荡, 并沿参数族 $J$ 缓慢滑动. 为描述参数 $J$ 的这种“缓慢滑动”, 平均化系统出现了.

我们在此介绍平均化方法的最简单的情形. 此时 $m + k$ 等于相空间的维数. 换句话说相空间的某个区域被不变环面充满. 变量 $J _ { 1 } , . . . , J _ { k } , \varphi _ { 1 } , . . . , \varphi _ { m }$ (其中 $\varphi _ { i }$ 是在模 $2 \pi$ 意义下) 作为该区域的坐标. 频率向量 $\omega = ( \omega _ { 1 } , . . . , \omega _ { m } )$ 与 $J$ 有关, $\omega = \omega ( J )$ . 未摄动的系统在该坐标下形如

$$
\begin{array} { l } { \varphi _ { t } = \omega ( J ) } \\ { J _ { t } = 0 . } \end{array}
$$

假设摄动后的系统形如

$$
\begin{array} { l } { \varphi _ { t } = \omega ( J ) + \varepsilon f ( J , \varphi , \varepsilon ) } \\ { J _ { t } = \varepsilon g ( J , \varphi , \varepsilon ) . } \end{array}
$$

则其平均化系统定义为如下:

$$
\begin{array} { l } { { J _ { t } = G ( J ) , \quad T = \varepsilon t , } } \\ { { G ( J ) = \displaystyle \frac { 1 } { ( 2 \pi ) ^ { m } } \int _ { T ^ { m } } g ( J , \varphi , 0 ) \mathrm { d } ^ { m } \varphi . } } \end{array}
$$

(这里的 $T ^ { m }$ 为 $m$ 维环面 $0 \leq \varphi _ { i } \leq 2 \pi$ , $i = 1 , . . . , m$ .) 则 $J = J _ { \overline { { \mathcal { F } } } \dot { \bf z } \dot { \bf z } } ( \varepsilon t )$ 给出了参数 $J$ 关于时间的“缓慢滑动”. 在单相情形, 函数 $J _ { \overline { { \Psi } } \dot { \Sigma } \dot { \Sigma } } ( \varepsilon t )$ 是摄动后的系统的精确解 $J = J _ { \varepsilon } ( t )$ 的非常好的近似: 当时间 $t \overset \sim { < } \varepsilon ^ { - 1 }$ 时, 无穷小量 $| J _ { \mathcal { \vec { F } \vec { \pmb { \mathscr { H } } } } } ( \varepsilon t ) - J _ { \varepsilon } ( t ) |$ 与 $\varepsilon$ 同阶. 而在多相情形, 情况就更复杂了 (比如, 见 [26]).

我们将在本书第三章考虑平均化方法的一例应用.

在哈密顿系统的情形, 我们假定未摄动的系统时完全可积的, 其哈密顿量为 $H _ { 0 }$ .$J _ { 1 } , . . . , J _ { n } , \varphi _ { 1 } , . . . , \varphi _ { n }$ 为此系统的作用量-角参数, $H _ { 0 } = H _ { 0 } ( J )$ , $\omega _ { i } ( J ) = \frac { \partial H _ { 0 } } { \partial J _ { i } }$ $i = 1 , . . . , n$ .我们假定摄动后的系统也是哈密顿系统, 且哈密顿量 $H _ { \varepsilon } = H _ { 0 } ( J ) + \varepsilon H _ { 1 } ( J , \varphi , \varepsilon )$ . 上述基本观察对于完全可积哈密顿系统的摄动理论 (KAM 理论, 见 [26]) 大有所益.

# 1.3 局部场论泊松括号: 主要例子

我们来考虑无限维的泊松括号. 我们将只考虑场论型的泊松括号. 在场论中, 我们

考虑由场

$$
u ( \boldsymbol { x } ) = ( u ^ { 1 } ( \boldsymbol { x } ) , . . . , u ^ { N } ( \boldsymbol { x } ) ) , \quad \boldsymbol { x } = ( x ^ { 1 } , . . . , x ^ { d } )
$$

构成的无限维相空间, 其中 $u ( x )$ 取值于某空间 $Y$ (靶空间). 这里的 $x$ 视为公式中的一个(类似于 $i = 1 , 2 , \dots$ 的) 指标. 我不打算详细说明 $u ( x )$ 到底属于哪个函数类, 只给出泊松括号的形式的理论. 在此形式的理论中, 我们只需要让导函数的积分为零:

$$
\int ( . . . ) ^ { \prime } \mathrm { d } ^ { d } x = 0 .
$$

例如, 可以考虑紧致 $x \cdot$ -流形 $M$ , $x \in M$ , 或者某些有限向量值函数 $u ( x ) , x \in \mathbb { R } ^ { d }$ .

泊松括号应定义在场 $u ( x )$ 的适当的泛函类上. 在我们的理论中, 泊松括号定义在“逐点的”泛函上. 我们要求这种泛函形如

$$
f ( u ( x ) , u ^ { \prime } ( x ) , . . . , u ^ { ( k ) } ( x ) ) ,
$$

其中 $x$ 为给定某点, $f ( u , u ^ { \prime } , . . . , u ^ { ( k ) } )$ 为解析函数 $( u ^ { \prime } , . . . , u ^ { ( k ) }$ 为 $u ( x )$ 的各阶导数). 泊松括号由如下公式定义:

$$
\{ u ^ { i } ( x ) , u ^ { j } ( y ) \} = h ^ { i j } ( x , y ) .
$$

这里的 $h ^ { i j } ( x , y ) \ = \ h ^ { i j } ( x , y ) [ u ]$ 也是与场 $u$ 有关的泛函, 它是关于 $x , y$ 的 广义函数(distribution) . 泊松括号可以通过双线性与莱布尼茨法则推广到“多点泛函”上:

$$
\begin{array} { l l } { { } } & { { \{ f ( u ( x ) , . . . ) g ( u ( y ) , . . . ) , h ( u ( z ) , . . . ) \} } } \\ { { = } } & { { f ( u ( x ) , . . . ) \{ g ( u ( y ) , . . . ) , h ( u ( z ) , . . . ) \} } } \\ { { + } } & { { g ( u ( y ) , . . . ) \{ f ( u ( x ) , . . . ) , h ( u ( z ) , . . . ) \} . } } \end{array}
$$

下述性质也非常有用:

$$
\left\{ { \frac { \partial f ( u ( x ) , \ldots ) } { \partial x ^ { \alpha } } } , g ( u ( y ) , \ldots ) \right\} = { \frac { \partial } { x ^ { \alpha } } } \{ f ( u ( x ) , \ldots ) , g ( u ( y ) , \ldots ) \}
$$

(这是双线性的显然推论). 关于积分的类似性质

$$
\left\{ \int f ( u ( x ) , \ldots ) \mathrm { d } ^ { d } x , g ( u ( y ) , \ldots ) \right\} = \int \{ f ( u ( x ) , \ldots ) , g ( u ( y ) , \ldots ) \} \mathrm { d } ^ { d } x
$$

使得我们能将泊松括号推广到形如下述的 局部场论泛函 (local field-theoretic func-tional)

$$
F [ u ] = \int f ( x , u ( x ) , u ^ { \prime } ( x ) , . . . , u ^ { ( k ) } ( x ) ) \mathrm { d } ^ { d } x ,
$$

简称局部泛函 ( $f$ 称为 $F$ 的密度, 假定它是关于 $u , u ^ { \prime } , . . . , u ^ { ( k ) }$ 的多项式或者解析函数).

引理. 对于局部泛函 $F [ u ] , G [ u ]$ , 其泊松括号的表达式如下:

$$
\{ F , G \} = \iint \frac { \delta F } { \delta u ^ { i } ( x ) } \frac { \delta G } { \delta u ^ { j } ( y ) } h ^ { i j } ( x , y ) \mathrm { d } ^ { d } x \mathrm { d } ^ { d } y .
$$

[上述公式中出现的变分导数由以下展开式所确定

$$
F [ u + \delta u ] - F [ u ] = \int \frac { \delta F } { \delta u ^ { i } ( x ) } \delta u ^ { i } ( x ) \mathrm { d } ^ { d } x + o ( \delta u ) .
$$

对于局部泛函, 变分导数为如下的欧拉-拉格朗日算子:

$$
\frac { \delta F } { \delta u ^ { i } ( x ) } = \frac { \partial f } { \partial u ^ { i } } - \frac { \partial } { \partial x ^ { \alpha } } \frac { \partial f } { \partial u _ { \alpha } ^ { i } } + \frac { \partial ^ { 2 } } { \partial x ^ { \alpha } \partial x ^ { \beta } } \frac { \partial f } { \partial u _ { \alpha \beta } ^ { i } } - \cdot \cdot \cdot
$$

这里 $u _ { \alpha } ^ { i } \equiv \frac { \partial u ^ { i } } { \partial x ^ { \alpha } }$ ≡ ∂ u ∂ x α , u iαβ = $u _ { \alpha \beta } ^ { i } = \frac { \partial ^ { 2 } u ^ { i } } { \partial x ^ { \alpha } \partial x ^ { \beta } } , \dots ~ ]$

证明. (不妨只证明 $d = 1$ 的情况). 我们有

$$
\begin{array} { r c l } { { \{ F , u ^ { j } ( y ) \} } } & { { = } } & { { \displaystyle \int \mathrm { d } ^ { d } x \{ f ( x , u ( x ) , u ^ { \prime } ( x ) , \ldots ) , u ^ { j } ( y ) \} } } \\ { { } } & { { = } } & { { \displaystyle \int \mathrm { d } ^ { d } x \left[ \frac { \partial f } { \partial u ^ { i } } ( x ) \{ u ^ { i } ( x ) , u ^ { j } ( y ) \} + \frac { \partial f } { \partial u _ { x } ^ { i } } ( x ) \{ u _ { x } ^ { i } ( x ) , u ^ { j } ( y ) \} + \cdots \right] } } \\ { { } } & { { = } } & { { \displaystyle \int \mathrm { d } ^ { d } x \left[ \frac { \partial f } { \partial u ^ { i } } ( x ) h ^ { i j } ( x , y ) + \frac { \partial f } { \partial u _ { x } ^ { i } } ( x ) \partial _ { x } h ^ { i j } ( x , y ) + \cdots \right] } } \\ { { } } & { { = } } & { { \displaystyle \int \mathrm { d } ^ { d } x \left[ \frac { \partial f } { \partial u ^ { i } } ( x ) - \partial _ { x } \frac { \partial f } { \partial u _ { x } ^ { i } } ( x ) + \cdots \right] h ^ { i j } ( x , y ) } } \\ { { } } & { { = } } & { { \displaystyle \int \frac { \delta f } { \delta u ^ { i } ( x ) } h ^ { i j } ( x , y ) \mathrm { d } ^ { d } x . } } \end{array}
$$

再记泛函 $G$ 的密度为 $g$ , 因此有

$$
\begin{array} { r c l } { { \{ F , G \} } } & { { = } } & { { \displaystyle \int \mathrm { d } ^ { d } y \{ F , g ( y , u ( y ) , u ^ { \prime } ( y ) , \ldots ) \} } } \\ { { } } & { { = } } & { { \displaystyle \int \mathrm { d } ^ { d } y \left[ \{ F , u ^ { j } ( y ) \} \frac { \partial g } { \partial u ^ { j } } ( y ) + \partial _ { y } \{ F , u ^ { j } ( y ) \} \frac { \partial g } { \partial u _ { y } ^ { j } } ( y ) + \cdots \right] } } \\ { { } } & { { = } } & { { \displaystyle \int \mathrm { d } ^ { d } y \{ F , u ^ { j } ( y ) \} \frac { \delta G } { \delta u ^ { j } ( y ) } } } \\ { { } } & { { = } } & { { \displaystyle \iint \frac { \delta F } { \delta u ^ { i } ( x ) } \{ u ^ { i } ( x ) , u ^ { j } ( y ) \} \frac { \delta G } { \delta u ^ { j } ( y ) } \mathrm { d } ^ { d } x \mathrm { d } ^ { d } y . } } \end{array}
$$

现在我们再对泊松括号的类型加以限制.

定义. 局部场论泊松括号 (local field-theoretic Poisson bracket) 是指形如以下的泊松括号:

$$
\{ u ^ { i } ( x ) , u ^ { j } ( y ) \} = \sum _ { | k | \leq K } A _ { k } ^ { i j } ( x , u ( x ) , u ^ { \prime } ( x ) , . . . , u ^ { n _ { k } } ( x ) ) \partial _ { x } ^ { k } \delta ( x - y ) .
$$

上式中的 $\delta$ 为 Dirac $\delta$ -函数, $\boldsymbol { k } = ( k _ { 1 } , . . . , k _ { d } )$ 为多重指标, $| k | = k _ { 1 } + \ldots + k _ { d }$ , $\partial _ { x } ^ { k } = $ ${ \bigg ( } { \frac { \partial } { \partial x ^ { 1 } } } { \bigg ) } ^ { k _ { 1 } } \dots { \bigg ( } { \frac { \partial } { \partial x ^ { d } } } { \bigg ) } ^ { k _ { d } }$ , $\kappa$ 称为该泊松括号的阶数, 系数 $A _ { k } ^ { i j }$ 为关于 $x , u , u ^ { \prime } , \ldots$ 的解析函数. 此外, 该泊松括号称为平移不变的, 若 $\boldsymbol { x } \in \mathbb { R } ^ { d }$ (或 $x \in T ^ { d } ,$ ) 并且系数 $A _ { k } ^ { i j }$ 与 $x$ 无关.

此外, 该泊松括号称为常值的, 若系数 $A _ { k } ^ { i j }$ 也与 $u ( x ) , u ^ { \prime } ( x ) , \ldots$ 无关.

我们引入算子

$$
A ^ { i j } = \sum _ { | k | \leq \mathcal { K } } A _ { k } ^ { i j } ( u ( x ) , u ^ { \prime } ( x ) , \ldots ) \partial _ { x } ^ { k } .
$$

则局部泛函在此泊松括号下的表达式为

$$
\{ F , G \} = \int { \frac { \delta F } { \delta u ^ { i } ( x ) } } A ^ { i j } { \frac { \delta G } { \delta u ^ { j } ( x ) } } \mathrm { d } ^ { d } x .
$$

很显然, 局部泛函关于局部场论泊松括号构成李代数.

泊松括号的反对称性要求算子 $A ^ { i j }$ 满足

$$
( A ^ { i j } ) ^ { * } = - A ^ { j i } ,
$$

这里的 $( A ^ { i j } ) ^ { * }$ 为其伴随算子, 定义为

$$
( A ^ { i j } ) ^ { * } = \sum _ { | k | \leq \mathcal { K } } ( - \partial _ { x } ) ^ { k } A _ { k } ^ { i j } .
$$

至于雅可比恒等式, 那等价于一个关于系数 $A _ { k } ^ { i j }$ 及其导数的非常复杂的二次方程组, 形如

$$
\begin{array} { l } { { \{ \{ u ^ { i } ( x ) , u ^ { j } ( y ) \} , u ^ { k } ( z ) \} + \cdots } } \\ { { \equiv } } \\ { { \displaystyle \partial u ^ { i j } ( x ) } } \end{array}
$$

关于局部泊松括号与局部哈密顿量

$$
H = \int h ( \boldsymbol { u } , \boldsymbol { u } ^ { \prime } , \ldots ) \mathrm { d } ^ { d } \boldsymbol { x }
$$

的哈密顿系统形如

$$
\frac { \partial u ^ { i } ( x ) } { \partial t } = \{ H , u ^ { i } ( x ) \} = - A ^ { i j } \frac { \delta H } { \delta u ^ { j } ( x ) } .
$$

重要的是, 如此的哈密顿系统是演化型的偏微分方程组. 这也是我们考虑局部泊松括号的一个原因.

例子 1. 常值泊松括号的典型例子. 记 $N \ : = \ : 2 n$ , 相空间由场 $( u ^ { 1 } ( x ) , . . . , u ^ { N } ( x ) ) \ =$ $( q ^ { 1 } ( x ) , . . . , q ^ { n } ( x ) , p _ { 1 } ( x ) , . . . , p _ { n } ( x ) )$ 构成:

$$
\{ p _ { i } ( x ) , q ^ { j } ( y ) \} = \delta _ { i } ^ { j } \delta ( x - y ) , \quad \{ p _ { i } ( x ) , p _ { j } ( y ) \} = \{ q ^ { i } ( x ) , q ^ { j } ( y ) \} = 0 .
$$

此泊松括号出现于形如

$$
\delta \int \int \mathrm { d } t \mathrm { d } ^ { d } x { \cal L } ( q , q _ { t } , q _ { x } ) = 0
$$

的多维变分问题的欧拉-拉格朗日理论 (这里 pi = $p _ { i } = { \frac { \partial L } { \partial q _ { t } ^ { i } } }$ $= \frac { \partial L } { \partial q _ { t } ^ { i } } , H = \int \mathrm { d } ^ { d } x ( p _ { i } q _ { t } ^ { i } - L ) = \int \mathrm { d } ^ { d } x h ( q , p , q _ { x } ) ) .$

例子 2. 超局部泊松括号. 5 更一般地, 设 $P$ 为有限维泊松流形, 其泊松括号 $\{ u ^ { i } , u ^ { j } \} =$ $h ^ { i j } ( u )$ $( u ^ { 1 } , . . . , u ^ { N }$ 为 $P$ 的局部坐标), 则在场 $u ^ { i } ( x ) , x \in X$ 上可定义如下的 超局部泊松括号 (ultralocal Poisson bracket) :

$$
\{ u ^ { i } ( x ) , u ^ { j } ( y ) \} = h ^ { i j } ( u ) \delta ( x - y ) .
$$

若 $h ^ { i j }$ 为常值, 则此例退化为例子 1.

例子 3. Gardner-Zakharov-Faddeev 泊松括号. 取 $N = d = 1$ , 令 $\{ u ( x ) , u ( y ) \} =$ $\delta ^ { \prime } ( x - y )$ . 该运算的反对称性与雅可比恒等式显然成立 (这是常值泊松括号). 相应的哈密顿系统形如

$$
u _ { t } ( x ) = \{ H , u ( x ) \} = - \partial _ { x } \frac { \delta H } { \delta u ( x ) } .
$$

例如取

$$
H = \int \left( \frac { { { u ^ { \prime } } ^ { 2 } } } { 2 } + u ^ { 3 } \right) \mathrm { { d } } x
$$

时, 我们得到 KdV 方程

$$
u _ { t } + 6 u u _ { x } - u _ { x x x } = 0 .
$$

此泊松括号是退化的. 其零化子形如

$$
I _ { 0 } [ u ] = \int u \mathrm { d } x .
$$

这种常值泊松括号的更一般的例子是

$$
\{ u ^ { i } ( x ) , u ^ { j } ( y ) \} = g ^ { i j } \delta ^ { \prime } ( x - y ) , \quad i , j = 1 , . . . , N ,
$$

其中 $( g ^ { i j } )$ 为常值对称矩阵. 对于 $N = 2 n$ , 且 $( g ^ { i j } )$ 的正负惯性指数为 $( n , n )$ 时, 可以适当选取线性坐标使得

$$
\begin{array} { l } { { \{ u ^ { i } ( x ) , u ^ { n + j } ( y ) \} = \delta ^ { i j } \delta ^ { \prime } ( x - y ) , \quad \{ u ^ { i } ( x ) , u ^ { j } ( y ) \} = \{ u ^ { n + i } ( x ) , u ^ { n + j } ( y ) \} = 0 } } \\ { { \ } } \\ { { i , j = 1 , . . . , n . } } \end{array}
$$

此泊松括号可通过下述变量代换化为例子 1 中的标准形式:

$$
u ^ { i } ( x ) = p _ { i } ( x ) , \quad u ^ { n + i } ( x ) = q ^ { i } ( x ) ^ { \prime } , \quad i = 1 , . . . , n .
$$

着用引入典范坐标的技巧 19 世纪以来就在流体力学中众所周知了. 该技巧被称为“引入 Clebsch 变量”, 可用于将偏微分方程化为拉格朗日形式. 当 $N$ 为奇数或者正负惯性指数不是 $( n , n )$ 时无法引入 Clebsch 变量.

例子 4. (Novikov). 对于任何两个流形 $M ^ { d }$ , $Y ^ { n }$ (其中 $M ^ { d }$ 紧致),定义在由映射 $M ^ { d } $ $Y ^ { n }$ 构成的空间上的可定义 手性场 (chiral field) 型拉格朗日量. 为构造最简单的例子,我们需要 $M ^ { d }$ 上的度量 $\gamma _ { \alpha \beta }$ 以及 $Y ^ { n }$ 上的度量 $g _ { i j }$ . 手性场作用泛函形如以下:

$$
\begin{array} { l } { { S _ { 0 } = \displaystyle \frac { 1 } { 2 } \int \mathrm { d } t \int _ { M ^ { d } } \sqrt { \gamma } \mathrm { d } ^ { d } x g _ { i j } ( y ( x ) ) ( y _ { t } ^ { i } y _ { t } ^ { j } - \gamma ^ { \alpha \beta } ( x ) \partial _ { \alpha } y ^ { i } \partial _ { \beta } y ^ { j } ) , } } \\ { { y ^ { i } = y ^ { i } ( t , x ) , \quad x \in M ^ { d } , \quad y \in Y ^ { n } , } } \\ { { ( \gamma ^ { \alpha \beta } ) = ( \gamma _ { \alpha \beta } ) ^ { - 1 } , \quad \gamma = | \mathrm { d e t } ( \gamma _ { \alpha \beta } ) | . } } \end{array}
$$

可通过标准的 Legendre 变换将其化为哈密顿形式. 这里的“位形空间” $Q$ 为由映射$M ^ { d } \to Y ^ { n }$ 构成的空间. $Y ^ { n }$ 上的任何闭 $( d + 2 )$ -形式 $\Omega = { \frac { 1 } { ( d + 2 ) ! } } \Omega _ { i _ { 1 } , \dots , i _ { d + 2 } } ( y ) \mathrm { d } y ^ { i _ { 1 } } \wedge$ $\cdots \wedge \mathrm { ~ d } y ^ { i _ { d + 2 } }$ , $\mathrm { d } \Omega = 0$ 通过下式决定了 $Q$ 上闭 2-形式 $\hat { \Omega }$ :

$$
\hat { \Omega } ( \xi , \eta ) = \frac 1 { d ! } \int _ { M ^ { d } } \xi ^ { i } ( x ) \eta ^ { j } ( x ) \Omega _ { i j i _ { i } \cdots i _ { d } } ( y ( x ) ) \mathop { } \mathrm { d } y ^ { i _ { 1 } } ( x ) \wedge \cdots \wedge \mathop { } \mathrm { d } y ^ { i _ { d } } ( x ) .
$$

这里的 $\xi = ( \xi ^ { i } ( x ) )$ , $\eta = ( \eta ^ { i } ( x ) )$ 为空间 $Q$ 在点 $y ( x )$ 处的两个“切向量”(即 $\xi ( x ) , \eta ( x )$ 为 $Y ^ { n }$ 的在点 $y ( x )$ 的切向量. 此 2-形式 $\hat { \Omega }$ 定义了第 1 节例子 2“磁场中的泊松括号”的无限维版本):

$$
\{ p _ { i } ( x ) , p _ { j } ( x ^ { \prime } ) \} _ { \Omega } = \frac { 1 } { d ! } \frac { \Omega _ { i j i _ { 1 } \cdots i _ { d } } ( y ( x ) ) \mathrm { d } y ^ { i _ { 1 } } ( x ) \wedge \cdots \wedge \mathrm { d } y ^ { i _ { d } } ( x ) } { \mathrm { d } x ^ { 1 } \wedge \cdots \wedge \mathrm { d } x ^ { d } } \cdot \delta ( x - x ^ { \prime } ) ,
$$

其余泊松括号都是标准的.

这里的 $\delta$ 为流形 $M ^ { d }$ 上的 Dirac 函数:

$$
\int _ { M ^ { d } } f ( x ^ { \prime } ) \delta ( x - x ^ { \prime } ) \mathrm { d } ^ { d } x ^ { \prime } = f ( x ) ;
$$

动量 $p _ { i } ( x )$ 为 $M ^ { d }$ 的余切向量密度. 与有限维情形一样, 该系统的哈密顿方程也能表示为多值泛函 (若 $\Omega$ 整体上不是恰当形式) 的欧拉-拉格朗日系统, 相应的作用泛函形如

$$
S = S _ { 0 } - \iint _ { M ^ { d } \times \mathbb { R } } A _ { i _ { 0 } i _ { 1 } \cdots i _ { d } } ( y ( x ) ) \mathrm { d } y ^ { i _ { 0 } } ( t , x ) \wedge \cdots \wedge \mathrm { d } y ^ { i _ { d } } ( t , x ) ,
$$

其中 $A$ 为 $( d + 1 )$ -形式, 使得局部成立 $\mathrm { d } A = \Omega$ , $A = { \frac { 1 } { ( d + 1 ) ! } } A _ { i _ { 0 } i _ { 1 } \cdots i _ { d } } \mathrm { d } y ^ { i _ { 0 } } \wedge \cdot \cdot \cdot \mathrm { d } y ^ { i _ { d } }$ , 而$\mathbb { R }$ 为 $t { \cdot }$ -轴.

在 $d = 1 , \gamma _ { \alpha \beta } = 1$ , $Y ^ { n } = G$ (紧群) 配以双不变度量 $g _ { i j }$ 的重要特殊情形, $S _ { 0 }$ 为主手性场作用泛函. 此时的运动方程在 反散射方法 (inverse scattering method) (简称ISM) 的意义下是可积的 (Palmayer, Zakharov, Mikhailov, 见 [27]). 这里的磁场 ( $G$ 上的闭 3-形式 $\Omega$ ) 可自然地引入, 因为任何紧群都满足 $H ^ { 3 } ( G ) \neq 0$ . 对于最简单的例子$G = { \mathrm { S U } } ( 2 )$ , 可取 $\Omega$ 为其体积形式, 可以证明此时的运动方程在反散射方法的意义下可积 (Takhtadjan, Veselov [28]).

例子 5. 圈代数与泊松括号. 线性的场论泊松括号的最简单的例子与 圈代数 (loopalgebra) 有关. 设场 $u ^ { 1 } ( x ) , . . . , u ^ { N } ( x )$ 为 $x \in X$ 上的 $d .$ -形式, $d = \dim X$ , 且取值于某个李代数 $L$ 的对偶空间 $L ^ { * }$ , 其中 $L$ 的的结构常数为 $( c _ { k } ^ { i j } )$ . 因此相空间 $L ^ { * }$ 形式地成为圈群 (loop group) $G ^ { X }$ 的无限维李代数, 其中 $G$ 是以 $L$ 为李代数的李群, $X$ 为变量$x ^ { 1 } , . . . , x ^ { d }$ 所在的空间, $G ^ { X }$ 为由光滑映射 $X  G$ 构成的群. $( L ^ { X } ) ^ { * }$ 上的泊松括号是超局部, 线性的:

$$
\{ u ^ { i } ( x ) , u ^ { j } ( y ) \} = c _ { k } ^ { i j } u ^ { k } ( x ) \delta ( x - y ) .
$$

我们假设李代数 $L$ 配有不变双线性型 $g ^ { i j } = g ^ { j i }$ , 即满足

$$
c _ { s } ^ { i j } g ^ { s k } = - c _ { s } ^ { i k } g ^ { s j } .
$$

例如对于半单李代数 $L$ , $g ^ { i j }$ 可取其 Killing 型, $g ^ { i j } = - c _ { l } ^ { i k } c _ { k } ^ { j l }$ . 则在一维空间情形 (即$d = 1 \mathrm { \Omega }$ ), 我们得到圈代数 $L ^ { X }$ 的一个中心扩张 (Kac-Moody 代数), 且相应的泊松括号为如下非齐次的:

$$
\{ u ^ { i } ( x ) , u ^ { j } ( y ) \} _ { g } = g ^ { i j } \delta ^ { \prime } ( x - y ) + c _ { k } ^ { i j } u ^ { k } ( x ) \delta ( x - y ) .
$$

圈代数的中心扩张在共形场论中扮演重要角色.

例子 6. 李代数 $L ( d )$ . 考虑 $d$ 为空间的切向量场构成的李代数 $L ( d )$ , 其中的向量场$a , b \in L ( d )$ 的交换子为形如下式的向量场 $c = [ a , b ]$ :

$$
c = c ^ { i } \partial _ { i } , \quad a = a ^ { i } \partial _ { i } , \quad b = b ^ { i } \partial _ { i } , \quad c ^ { i } = a ^ { k } \partial _ { k } b ^ { i } - b ^ { k } \partial _ { k } a ^ { i } .
$$

我们来验证对偶空间 $L ( d ) ^ { * }$ 上的李-泊松括号形如

$$
\{ p _ { i } ( x ) , p _ { j } ( y ) \} = p _ { j } ( x ) \partial _ { i } \delta ( x - y ) + p _ { i } ( y ) \partial _ { j } \delta ( x - y ) , \quad i , j = 1 , . . . , d .
$$

这里的变量 $p _ { i } ( x )$ 为余切向量密度 (即 1-形式与体积元相乘), 使得对任意向量场 $a =$ $a ^ { i } \partial _ { i }$ , 数量积

$$
a [ p ] \equiv ( a , p ) = \int p _ { i } a ^ { i } \mathrm { d } ^ { d } x
$$

是良好定义的. 事实上, 两个线性泛函

$$
a = a [ p ] = \int a ^ { i } p _ { i } \mathrm { d } ^ { d } x , \quad b = b [ p ] = \int b ^ { i } p _ { i } \mathrm { d } ^ { d } x
$$

的泊松括号也是线性泛函

$$
\{ a , b \} = c = \int c ^ { i } p _ { i } \mathrm { d } ^ { d } x ,
$$

其中向量场 $c = c ^ { i } \partial _ { i }$ 为 $a , b$ 的交换子.

设 $L _ { 0 } ( d ) \subseteq L ( d )$ 为无散向量场 $a = a ^ { i } \partial _ { i }$ , $\partial _ { i } a ^ { i } = 0$ 构成的李子代数. 对偶空间 $L _ { 0 } ( d ) ^ { * }$ 可由模掉梯度向量 $p _ { i } = \partial _ { i } \phi$ 的商空间来实现:

$$
{ \cal L } _ { 0 } ( d ) ^ { * } = { \cal L } ( d ) ^ { * } / ( \partial _ { i } \phi ) .
$$

事实上, $p$ 满足对任何使得 $\partial _ { i } a ^ { i } = 0$ 的 $a ^ { i }$ 都有 $\int { p _ { i } } { a ^ { i } } { { \mathrm { d } } ^ { d } } x = 0$ , 当且仅当 $p _ { i } = \partial _ { i } \phi$ .$L _ { 0 } ( d ) ^ { * }$ 的哈密顿系统可以在 $L ( d ) ^ { * }$ 上写为下式:

$$
\partial _ { t } p _ { i } ( x ) = \{ H , p _ { i } ( x ) \} + \partial _ { i } \phi , \quad i = 1 , . . . , d .
$$

理想不可压缩流体的哈密顿理论可以用 $L _ { 0 } ( d ) ^ { * }$ 上的此泊松括号来描述 (这首先由 Arnol’d用辛流形的语言发现, 见 [26]). 对于理想不可压缩流, $X = \mathbb { R } ^ { d }$ 为欧氏空间, 配以欧氏度量 $g _ { i j } = \rho \delta _ { i j }$ , 其中常数 $\rho$ 为流体的密度. 余切向量 $p _ { i }$ 与切向量 $v _ { i }$ 通过公式 $p _ { i } = \rho v _ { i }$ 相

联系. 对于哈密顿量

$$
H = \int { \frac { p ^ { 2 } } { 2 \rho } } \mathrm { d } ^ { d } x = \int { \frac { \rho v ^ { 2 } } { 2 } } \mathrm { d } ^ { d } x
$$

$\langle \equiv \int \frac { 1 } { 2 } \langle \boldsymbol { v } , \boldsymbol { v } \rangle \mathrm { d } ^ { d } x$ , 数量积 $\langle , \rangle$ 为度量 $g _ { i j }$ ), 则我们得到理想不可压缩流体的欧拉方程

$$
\partial _ { t } p _ { i } ( \boldsymbol { x } ) = \{ H , p _ { i } ( \boldsymbol { x } ) \} + \partial _ { i } \phi \iff \partial _ { t } \boldsymbol { v } + ( \boldsymbol { v } \nabla ) \boldsymbol { v } = - \frac { 1 } { \rho } \operatorname { g r a d } \mathcal { P } .
$$

这里的 $( v \nabla ) = v _ { i } \partial _ { i }$ ; 函数 $\mathcal { P } = \mathcal { P } ( \boldsymbol { x } )$ 为压强 (形如 $\mathcal { P } = \rho \frac { v ^ { 2 } } { 2 } - \phi )$ .

$d$ 维空间向量场李代数 $L ( d )$ 由自然的中心扩张, 其可以用来描述带有“冻结的”(frozen-in) 张量场的可压缩流体. 为描述这种扩张, 我们在 $p _ { i } ( x )$ (切向量场的对偶) 当中添加一定数量的 $( m _ { s } , n _ { s } )$ 型张量 $T _ { ( } s ) ( x )$ . 这些张量 $T _ { ( } s )$ 之间的泊松括号恒为 0

$$
\{ T _ { ( s _ { 1 } ) } ( x ) , T _ { ( s _ { 2 } ) } ( y ) \} = 0 .
$$

而泊松括号 $\{ p _ { i } ( x ) , T _ { ( s ) } ( y ) \}$ 由以下条件唯一确定: 对于形如

$$
H _ { v } = \int v ^ { i } p _ { i } \mathrm { d } ^ { d } x
$$

的哈密顿量 (由向量场 $v ^ { i } ( x )$ 所确定的单参数群的生成元), 应满足

$$
\{ T _ { ( s ) } ( x ) , H _ { v } \} = \mathcal { L } _ { v } T _ { ( s ) } ( x )
$$

(这里的 $\mathcal { L } _ { v }$ 为李导数).

对于可压缩流的情况, 我们应添加 $\rho ( \boldsymbol { x } ) \mathrm { d } ^ { d } \boldsymbol { x }$ (质量密度) 与 $\sigma ( x ) \mathrm { d } ^ { d } x$ (熵密度), 它们都是 $d .$ -形式. 从而有

$$
\begin{array} { l } { { \{ p _ { i } ( x ) , \rho ( y ) \} = \rho ( x ) \partial _ { i } \delta ( x - y ) , } } \\ { { \{ p _ { i } ( x ) , \sigma ( y ) \} = \sigma ( x ) \partial _ { i } \delta ( x - y ) , } } \\ { { \{ \rho ( x ) , \rho ( y ) \} = \{ \sigma ( x ) , \sigma ( y ) \} = \{ \rho ( x ) , \sigma ( y ) \} = 0 . } } \end{array}
$$

理想可压缩流体的哈密顿量形如

$$
H = \int \left[ { \frac { p ^ { 2 } } { 2 \rho } } + { \mathcal { E } } ( \rho , \sigma ) \right] { \mathrm { d } } ^ { d } x ,
$$

其中 $\mathcal { E } ( \rho , \sigma ) \mathrm { d } ^ { d } x$ 为内能密度. 相应的哈密顿系统

$$
\begin{array} { l } { \rho _ { t } ( x ) = \{ H , \rho ( x ) \} } \\ { \sigma _ { t } ( x ) = \{ H , \sigma ( x ) \} } \\ { p _ { i _ { t } } ( x ) = \{ H , p _ { i } ( x ) \} } \end{array}
$$

恰为理想不可压缩流体的运动方程:

$$
\begin{array} { r l } & { \rho _ { t } + \mathrm { { d i v } } ( \rho { \boldsymbol { v } } ) = 0 } \\ & { \sigma _ { t } + { \mathrm { d i v } } ( \rho \sigma ) = 0 } \\ & { v _ { t } + ( v \nabla ) v = - \displaystyle \frac { 1 } { \rho } \mathrm { { g r a d } } \mathcal { P } . } \end{array}
$$

这里 $p _ { i } = \rho v _ { i }$ . 压强 $\mathcal { P } = \mathcal { P } ( \rho , \sigma )$ 为函数 $\mathcal { E }$ 的 Legendre 变换:

$$
\mathcal { P } = \rho \mathcal { E } _ { \rho } + \sigma \mathcal { E } _ { \sigma } - \mathcal { E } .
$$

也常引入单位质量的熵密度 $s = \sigma / \rho$ , 此函数为标量. 也引入单位质量的内能 $\varepsilon$ :

$$
\mathcal { E } ( \rho , \sigma ) = \rho \varepsilon ( \rho , s ) .
$$

则我们得到标准的热力学方程

$$
\mathcal { P } = \rho ^ { 2 } \frac { \partial \varepsilon ( \rho , s ) } { \partial \rho } .
$$

作为本例结尾, 我们要注意场 $p _ { i } ( x ) , \rho ( x ) , \sigma ( x )$ 的线性泛函的李代数 (相空间的对偶空间) 是 $L ( d )$ 与 $C ^ { \infty } ( \mathbb { R } ^ { d } ) \times C ^ { \infty } ( \mathbb { R } ^ { d } )$ 的半直积, 其中李代数 $L ( d )$ 中的向量场在每个函数空间 $C ^ { \infty } ( \mathbb { R } ^ { d } )$ 上的作用都是通常的. 换句话说, 在此半直积中, 向量场 $a = a ^ { i } \partial _ { i }$ 与函数$f$ 的交换子形如

$$
[ a , f ] = a ^ { i } \partial _ { i } f .
$$

磁流体力学方程的哈密顿理论也可类似描述, 不过要用到 $L ( d )$ 的别的中心扩张, 添加别的张量. 磁场张量需要添加. 我们不再探讨其细节.

例子 7. Magri 括号与 Virasoro 代数. 一维向量场的李代数 $L ( 1 )$ 的泊松括号形如

$$
\{ p ( x ) , p ( y ) \} = [ p ( x ) + p ( y ) ] \delta ^ { \prime } ( x - y ) = 2 p ( x ) \delta ^ { \prime } ( x - y ) + p ^ { \prime } ( x ) \delta ( x - y ) .
$$

有趣的是, 可通过变量代换

$$
p ( x ) = { \frac { u ^ { 2 } ( x ) } { 2 } }
$$

将其化为 Gardner-Zakharov-Faddeev 泊松括号 (见前面的例子 3). 事实上, 若 $\{ u ( x ) , u ( y ) \} =$ $\delta ^ { \prime } ( x - y )$ , 则

$$
\begin{array} { r c l } { { \{ p ( x ) , p ( y ) \} } } & { { = } } & { { u ( x ) u ( y ) \{ u ( x ) , u ( y ) \} = u ^ { 2 } ( x ) \delta ^ { \prime } ( x - y ) + u ( x ) u ^ { \prime } ( x ) \delta ( x - y ) } } \\ { { } } & { { = } } & { { 2 p ( x ) \delta ^ { \prime } ( x - y ) + p ^ { \prime } ( x ) \delta ( x - y ) . } } \end{array}
$$

李代数 $L ( 1 )$ 通过 Gel’fand-Fuks 上链的的众所周知的一维中心扩张 ( $\ b { x } \in \ b { S } ^ { 1 }$ 的 Virasoro代数) 诱导了线性非齐次泊松括号

$$
\{ p ( x ) , p ( y ) \} _ { c } = c \delta ^ { \prime \prime \prime } ( x - y ) + [ p ( x ) + p ( y ) ] \delta ^ { \prime } ( x - y )
$$

(见第 1 节例子 3). 这里的 $c$ 为常数. 此括号在可积系统理论中称为 Magri 括号 [29].KdV 方程 $p _ { t } + 6 p p _ { x } - p _ { x x x } = 0$ 也是关于 Magri 括号的哈密顿系统, 且 $c = - { \frac { 1 } { 2 } }$ 时相应的哈密顿量为

$$
H = \int p ^ { 2 } \mathrm { d } x .
$$

# 1.4 微分几何泊松括号. 流体力学型泊松括号与黎曼几何

我们考虑流形 $M ^ { d } , Y ^ { N }$ 之间的映射 $X ^ { d }  Y ^ { N }$ 构成的空间. 为定义空间 $\{ M ^ { d } $ ${ { Y } ^ { N } } \}$ 上的局部泊松括号, 应该在流形 $Y ^ { N }$ 上引入什么样的结构呢? 是否可能在此空间里定义常值的局部泊松括号? 若靶空间 $Y ^ { N }$ 不是线性空间, 则上述问题是不平凡的. 其原因是莱布尼茨法则: 若泊松括号在 $Y ^ { N }$ 的局部坐标 $\boldsymbol { u } ^ { 1 } , . . . , \boldsymbol { u } ^ { N }$ 下为常值的,

$$
\{ u ^ { i } ( x ) , u ^ { j } ( y ) \} = \sum _ { k \le | K | } A _ { k } ^ { i j } \delta ^ { ( k ) } ( x - y ) , \quad A _ { k } ^ { i j } \nearrow | \stackrel { \mathrm { \scriptsize { \sim } } \Psi } { \overbrace { \mathrm { \large { \cdot } } \mathrm { \large { \cdot } } \mathrm { \large { \cdot } } \mathrm { \large { \cdot } } \mathrm { \large { \cdot } } \mathrm { \large { \cdot } } \mathrm { \large { \cdot } } \mathrm { \large { \cdot } } \mathrm { \large { \cdot } } \mathrm { \large { \cdot } } } } .
$$

则在新坐标

$$
u ^ { i ^ { \prime } } ( x ) = u ^ { i ^ { \prime } } ( u ( x ) )
$$

下, 该泊松括号未必是常值的:

$$
\begin{array} { r c l } { { \{ u ^ { i ^ { \prime } } ( u ( x ) ) , u ^ { j ^ { \prime } } ( u ( y ) ) \} } } & { { = } } & { { \displaystyle \frac { \partial u ^ { i ^ { \prime } } ( u ( x ) ) } { \partial u ^ { i } } \frac { \partial u ^ { j ^ { \prime } } ( u ( y ) ) } { \partial u ^ { j } } \{ u ^ { i } ( x ) , u ^ { j } ( y ) \} } } \\ { { } } & { { = } } & { { \displaystyle \sum A _ { k } ^ { i ^ { \prime } j ^ { \prime } } ( u ( x ) , u ^ { \prime } ( x ) , . . . , u ^ { ( K - k ) } ( x ) ) \delta ^ { ( k ) } ( x - y ) . } } \end{array}
$$

[上式是由如下公式导出的:

$$
f ( y ) \delta ^ { ( n ) } ( x - y ) = \sum _ { k = 0 } ^ { n } { \binom { n } { k } } f ^ { ( n - k ) } ( x ) \delta ^ { ( k ) } ( x - y ) .
$$

] 在靶空间的坐标变换下保持“不变”的 $\kappa$ 阶局部泊松括号的极小类称为局部微分几何泊松括号 (local differential geometric Poisson bracket, 简称 D.G.P.B, 见 Novikov,Dubrovin [7]). 为给出上述概念的严格定义, 我们接下来只考虑空间一维情形 $( d = 1 )$ ),$\boldsymbol { M } ^ { d } = \mathbb { R }$ 或 $S ^ { 1 }$ .

定义. $( 1 )$ . 在靶空间局部坐标 $u ^ { 1 } , . . . , u ^ { N }$ 下, $\kappa$ 次齐次微分几何泊松括号是指形如下述的泊松括号:

$$
\{ u ^ { i } ( x ) , u ^ { j } ( y ) \} = \sum _ { k = 0 } ^ { \kappa } A _ { k } ^ { i j } ( u ( x ) , u ^ { \prime } ( x ) , . . . , u ^ { ( K - k ) } ( x ) ) \delta ^ { ( k ) } ( x - y ) ,
$$

其中系数 $A _ { k } ^ { i j }$ 是关于变元 $u ^ { \prime } , u ^ { \prime \prime } , \ldots$ 的 $( { \boldsymbol { \kappa } } - { \boldsymbol { k } } )$ 次齐次多项式 [这里的次数定义为:$\deg u ^ { ( s ) } = s , s = 1 , 2 , \ldots \rfloor$ :

$$
A _ { \mathcal K } ^ { i j } = g ^ { i j } ( u ) , \quad A _ { \mathcal K - 1 } ^ { i j } = b _ { k } ^ { i j } ( u ) u _ { x } ^ { k } , \quad A _ { \mathcal K - 2 } ^ { i j } = c _ { k } ^ { i j } ( u ) u _ { x x } ^ { k } + d _ { k l } ^ { i j } ( u ) u _ { x } ^ { k } u _ { x } ^ { l } , . . .
$$

(2). 非齐次局部微分几何泊松括号是不同 $\kappa$ 次齐次微分几何泊松括号的有限线性组合.

我们来看例子.

例子 1. 0 次微分几何泊松括号. 这正是上一节例子 2 当中的“超局部”泊松括号:

$$
\{ u ^ { i } ( x ) , u ^ { j } ( y ) \} = h ^ { i j } ( u ( x ) ) \delta ( x - y ) , \quad h ^ { j i } = - h ^ { i j } .
$$

例子 2. 1 次齐次微分几何泊松括号. 它具有如下形式:

$$
\{ u ^ { i } ( x ) , u ^ { j } ( y ) \} = g ^ { i j } ( u ( x ) ) \delta ^ { \prime } ( x - y ) + b _ { k } ^ { i j } ( u ( x ) ) u _ { x } ^ { k } \delta ( x - y ) .
$$

该泊松括号出现于流体力学型哈密顿系统的描述 (Novikov, Dubrovin[6]). 确切地说, 一维 (齐次) 流体力学型系统 (system of hydrodynamic type, 简称 SHT) 是指形如下述的偏微分方程组:

$$
u _ { t } ^ { i } = v _ { j } ^ { i } ( u ) u _ { x } ^ { j } , \quad i = 1 , . . . , N .
$$

所有的理想流体运动方程 (可能有内在的自由度) 都形如此 (比如可见上一节). 我们还将 (第三章) 介绍, 流体力学型系统也可用于描述任何场论哈密顿系统的孤子格的弱形变. 我们称形如

$$
H [ u ] = \int h ( u ) \mathrm { d } x
$$

的泛函为流体力学型泛函 (注意密度 $h$ 不显含 $u ^ { \prime } , u ^ { \prime \prime } , \ldots )$ . 某些理想流体的运动方程的全部守恒量都形如此 (比如, 可见第 3 节).

容易验证在一次齐次微分几何泊松括号以及流体力学型哈密顿量的情况下, 相应的哈密顿系统是流体力学型的:

$$
\begin{array} { r c l } { { u _ { t } ^ { i } ( x ) } } & { { = } } & { { \{ H , u ^ { i } ( x ) \} = v _ { j } ^ { i } ( u ) u _ { x } ^ { j } } } \\ { { } } & { { \equiv } } & { { - ( g ^ { i k } ( u ) \partial _ { x } + b _ { j } ^ { i k } ( u ) u _ { x } ^ { j } ) { \frac { \partial h } { \partial u ^ { k } } } } } \\ { { } } & { { = } } & { { - \left[ g ^ { i k } ( u ) { \frac { \partial ^ { 2 } h } { \partial u ^ { k } \partial u ^ { j } } } + b _ { j } ^ { i k } ( u ) { \frac { \partial h } { \partial u ^ { k } } } \right] u _ { x } ^ { j } . } } \end{array}
$$

正由于此原因, 我们也把这种泊松括号称为流体力学型泊松括号 (Poisson bracket ofhydrodynamic type, 简称 P.B.H.T.). 易知流体力学型泊松括号是与流体力学型哈密顿量生成流体力学型系统的最一般的一类局部泊松括号.

这些演化系统与泛函的类型在靶空间坐标变换下不变. 在坐标变换下, 系数矩阵$( v _ { j } ^ { i } ( x ) )$ 的变化规律同 $( 1 , 1 )$ 型张量.

流体力学型泊松括号经过靶空间坐标变换之后还是流体力学型的. 下述断言对流体力学型泊松括号十分重要:

引理. $( a )$ . 在靶空间坐标变换下, 系数矩阵 $g ^ { i j } ( u )$ 的变化规律同 $( 2 , 0 )$ 型张量.

$( b )$ . 假设 $\operatorname* { d e t } ( g ^ { i j } ( u ) ) \neq 0$ , 则可由下式唯一确定系数 $\Gamma _ { j k } ^ { i } = \Gamma _ { j k } ^ { i } ( u )$ :

$$
b _ { k } ^ { i j } = - g ^ { i s } \Gamma _ { s k } ^ { j } ,
$$

并且系数 $\Gamma _ { j k } ^ { i }$ 在坐标变换下的变化规律同仿射联络系数 (Christoffel 符号).

由下式可证此引理:

$$
\begin{array} { r c l } { { \{ u ^ { i ^ { \prime } } ( x ) , u ^ { j ^ { \prime } } ( y ) \} } } & { { = } } & { { \displaystyle \frac { \partial u ^ { i ^ { \prime } } ( u ( x ) ) } { \partial u ^ { i } } \frac { \partial u ^ { j ^ { \prime } } ( u ( y ) ) } { \partial u ^ { j } } \{ u ^ { i } ( x ) , u ^ { j } ( y ) \} } } \\ { { } } & { { = } } & { { \displaystyle \frac { \partial u ^ { i ^ { \prime } } ( u ( x ) ) } { \partial u ^ { i } } \frac { \partial u ^ { j ^ { \prime } } ( u ( y ) ) } { \partial u ^ { j } } g ^ { i j } ( u ( x ) ) \delta ^ { \prime } ( x - y ) } } \\ { { } } & { { } } & { { \displaystyle + \frac { \partial u ^ { i ^ { \prime } } } { \partial u ^ { i } } \left[ \frac { \partial u ^ { j ^ { \prime } } } { \partial u ^ { j } } \frac { \partial u ^ { k } } { \partial u ^ { k ^ { \prime } } } b _ { k } ^ { i j } u _ { x } ^ { k ^ { \prime } } + \partial _ { x } \left( \frac { \partial u ^ { j ^ { \prime } } } { \partial u ^ { j } } \right) g ^ { i j } \right] \cdot \delta ( x - y ) . } } \end{array}
$$

下面我们只考虑满足非退化条件 $\operatorname* { d e t } ( g ^ { i j } ) \neq 0$ 的流体力学型泊松括号. 这种泊松括号的微分几何十分简单.

定理. (a). 流体力学型泊松括号的反对称性 $\Longleftrightarrow$ 张量 $g ^ { i j }$ 是对称的 (即它定义了靶空间上的一个度量 a), 并且联络 $b _ { k } ^ { i j }$ (或者 $\Gamma _ { j k , } ^ { i }$ ) 与此度量相容 (即 $\nabla _ { k } g ^ { i j } \equiv 0 ,$ ).

$( b )$ . 流体力学型泊松括号的雅可比恒等式 $\Longleftrightarrow$ 联络的对称性 $\Gamma _ { j k } ^ { i } = \Gamma _ { k j } ^ { i }$ (即此联络是度量 $g ^ { i j }$ 的 Levi-Civita 联络), 并且度量 $g ^ { i j }$ 的曲率 $R _ { j k l } ^ { i }$ 为零.

a本书中的“度量”不要求具有正定性, 只需要非退化, 对称即可--译者注.

若此定理成立, 则可选取局部平坦坐标 $\boldsymbol { v } ^ { 1 } , . . . , \boldsymbol { v } ^ { N }$ 使得在此坐标下的泊松括号为常值的:

$$
\{ v ^ { i } ( x ) , v ^ { j } ( y ) \} = \hat { g } ^ { i j } \delta ^ { \prime } ( x - y ) , \quad \hat { g } ^ { i j } = \hat { g } ^ { j i } = { } ^ { \cdot }
$$

(见上一节例子 3). 流体力学型泊松括号的全系局部不变量为度量 $g ^ { i j }$ 的正负惯性指数.

证明. 反对称条件为

$$
\begin{array} { r c l } { { \{ u ^ { j } ( y ) , u ^ { i } ( x ) \} } } & { { = } } & { { g ^ { j i } ( u ( y ) ) \delta ^ { \prime } ( y - x ) + b _ { k } ^ { j i } ( u ( y ) ) \delta ( y - x ) } } \\ { { } } & { { = } } & { { - g ^ { j i } ( u ( x ) ) \delta ^ { \prime } ( x - y ) + [ - g ^ { j i } ( u ( x ) ) + b _ { k } ^ { j i } ( u ( x ) ) ] \delta ( x - y ) } } \\ { { } } & { { = } } & { { - [ g ^ { i j } ( u ( x ) ) \delta ^ { \prime } ( x - y ) + b _ { k } ^ { i j } ( u ( x ) ) \delta ( x - y ) ] } } \\ { { } } & { { = } } & { { - \{ u ^ { i } ( x ) , u ^ { j } ( y ) \} . } } \end{array}
$$

注意在上式中我们用到了 $f ( y ) \delta ^ { \prime } ( x - y ) = f ( x ) \delta ^ { \prime } ( x - y ) + f ^ { \prime } ( x ) \delta ( x - y )$ , 以及 $\delta ( y - x ) =$ $( x - y ) , \delta ^ { \prime } ( y - x ) = - \delta ^ { \prime } ( x - y )$ . 从而有

$$
g ^ { i j } ( u ) = g ^ { j i } ( u ) ,
$$

$$
b _ { k } ^ { i j } ( u ) + b _ { k } ^ { j i } ( u ) = \frac { \partial g ^ { i j } ( u ) } { \partial u ^ { k } } .
$$

上面第二个方程正是联络 $b _ { k } ^ { i j } = - g ^ { i s } \Gamma _ { s k } ^ { j }$ 与度量 $g ^ { i j }$ 的相容性:

$$
\begin{array} { r c l } { { \nabla _ { k } g ^ { i j } } } & { { = } } & { { \displaystyle \frac { \partial g ^ { i j } } { \partial u ^ { k } } + \Gamma _ { s k } ^ { i } g ^ { s j } + \Gamma _ { s k } ^ { j } g ^ { i s } } } \\ { { } } & { { = } } & { { \displaystyle \frac { \partial g ^ { i j } } { \partial u ^ { k } } - b _ { k } ^ { i j } - b _ { k } ^ { j i } = 0 . } } \end{array}
$$

为证明度量的平坦性与联络的对称性, 我们用雅可比恒等式. 令

$$
\begin{array} { r c l } { { J ^ { i j k } ( x , y , z ) } } & { { = } } & { { \{ \{ u ^ { i } ( x ) , u ^ { j } ( y ) \} , u ^ { k } ( z ) \} + \{ \{ u ^ { j } ( y ) , u ^ { k } ( z ) \} , u ^ { i } ( x ) \} } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { + \{ \{ u ^ { k } ( z ) , u ^ { i } ( x ) \} , u ^ { j } ( y ) \} } } \end{array}
$$

为雅可比恒等式的一端. 关于 $x , y , z$ 的广义函数 $J ^ { i j k } ( x , y , z )$ 对任意 $i , j , k$ 都为零, 当且仅当对任意“好的”向量值函数 $p , q , r$ 都有

$$
\iiint \mathrm { d } x \mathrm { d } y \mathrm { d } z p _ { i } ( x ) q _ { j } ( y ) r _ { k } ( z ) J ^ { i j k } ( x , y , z ) = 0 .
$$

上述积分可化为如下的单重积分

$$
\int \mathrm { d } x \sum _ { \sigma , \tau = 0 } ^ { 2 } A _ { \sigma \tau } ^ { i j k } p _ { i } q _ { j } ^ { ( \sigma ) } r _ { k } ^ { ( \tau ) } = 0 ,
$$

其中系数 $A _ { \sigma \tau } ^ { i j k }$ 与 $p , q , r$ 无关. 从而得到下述与雅可比恒等式等价的方程组:

$$
A _ { \sigma \tau } ^ { i j k } = 0 , \quad 1 \leq i , j , k \leq N , \quad 0 \leq \sigma , \tau \leq 2 .
$$

我们来写出这些关系的具体表达式. 首先有

$$
A _ { 0 2 } ^ { i j k } \equiv b _ { s } ^ { i j } g ^ { s k } - b _ { s } ^ { k j } g ^ { s i } = 0 ,
$$

这恰好是联络 $b _ { k } ^ { i j } = - g ^ { i s } \Gamma _ { s k } ^ { j }$ 的对称性条件. 此外,

$$
A _ { 0 0 } ^ { i j k } = B _ { s } ^ { i j k } ( u ) u _ { x x } ^ { s } + C _ { s t } ^ { i j k } ( u ) u _ { x } ^ { s } u _ { x } ^ { t } = 0 ,
$$

其中

$$
\begin{array} { r c l } { { { \cal B } _ { s } ^ { i j k } } } & { { = } } & { { ( b _ { t , s } ^ { j k } - b _ { s , t } ^ { j k } ) g ^ { t i } + b _ { t } ^ { i j } b _ { s } ^ { t k } - b _ { t } ^ { i k } b _ { s } ^ { t j } } } \\ { { } } & { { = } } & { { - g ^ { i t } g ^ { j r } R _ { r s t } ^ { k } . } } \end{array}
$$

[这里的 $b _ { t , s } ^ { j k } = \partial _ { s } b _ { t } ^ { j k }$ , 其余类似] . 从而曲率为零. 此定理的必要性条件得证.

至于充分性, 我们不必用到其余的那几个 $A _ { \sigma \tau } ^ { i j k } = 0$ 的关系. 事实上, 适当选取坐标变换 $u ^ { i } \mapsto v ^ { i } = v ^ { i } ( u )$ 可将泊松括号化为常值, 此时雅可比恒等式是显然的. 这就完成了证明. □

在讲具体例子前我想说, 这种平坦坐标是“非物理的”. 还有另外一种重要的坐标选取. 若局部坐标 $u ^ { 1 } , . . . , u ^ { N }$ 使得其度量与联络形如

$$
g ^ { i j } = \gamma ^ { i j } + \gamma ^ { j i } , \quad b _ { k } ^ { i j } = \frac { \partial \gamma ^ { i j } } { \partial u ^ { k } }
$$

其中 $\gamma ^ { i j } = \gamma ^ { i j } ( u )$ 为矩阵函数, 则称此坐标为 Liouville 坐标. 在此坐标下的流体力学型泊松括号形如

$$
\{ u ^ { i } ( x ) , u ^ { j } ( y ) \} = [ \gamma ^ { i j } ( u ( y ) ) + \gamma ^ { j i } ( u ( x ) ) ] \delta ^ { \prime } ( x - y ) .
$$

这种局部坐标的代表性质是下述泛函两两交换:

$$
U ^ { i } = \int u ^ { i } ( x ) \mathrm { d } x , \quad \{ U ^ { i } , U ^ { j } \} \equiv 0 .
$$

第一个例子是一维可压缩流体 (也可见第 3 节的例子 6) 的运动方程. 这里 $N = 3$ ,靶空间的自然的坐标选取为

$$
\begin{array}{c} \begin{array} { r l } { u ^ { 1 } = p } & { \left( \vec { z } \right) \varTheta \varXi \varTheta ^ { * } \varTheta } \\ { u ^ { 2 } = \rho } & { \left( \vec { \jmath } \varTheta \varXi \varXi \varTheta ^ { * } \varTheta \varTheta \right)} \\ { u ^ { 3 } = \sigma } & { \left( \imath \rlap / \hbar \partial \not \Xi \varTheta ^ { * } \varTheta \varTheta \right) \varXi } \end{array}   \end{array}
$$

泊松括号形如

$$
\begin{array} { l } { { \{ p ( x ) , p ( y ) \} = [ p ( x ) + p ( y ) ] \delta ^ { \prime } ( x - y ) , } } \\ { { \{ p ( x ) , \rho ( y ) \} = \rho ( x ) \delta ^ { \prime } ( x - y ) , } } \\ { { \{ p ( x ) , \sigma ( y ) \} = \sigma ( x ) \delta ^ { \prime } ( x - y ) , } } \\ { { \{ \rho ( x ) , \rho ( y ) \} = \{ \sigma ( x ) , \sigma ( y ) \} = \{ \rho ( x ) , \sigma ( y ) \} = 0 . } } \end{array}
$$

其 Liouville 矩阵为

$$
( \gamma ^ { i j } ) = { \binom { p } { \rho } } \ 0 0 \rangle \ .
$$

该系统的哈密顿量形如

$$
H = \int \left[ { \frac { p ^ { 2 } } { 2 \rho } } + { \mathcal { E } } ( \rho , \sigma ) \right] { \mathrm { d } } x .
$$

相应的度量 $g ^ { i j } = \gamma ^ { i j } + \gamma ^ { j i }$ 恒退化. 但在正压 (barotropic) 情形 $\sigma / \rho =$ 常数时 (此时$N = 2$ ), 相应的二维度量非退化:

$$
( g ^ { i j } ) = { \binom { 2 p } { \rho } } \ \rho \sp { } \ \rho \nonumber ) ,
$$

其正负惯性指数为 $( 1 , 1 )$ .

第二个例子时一维相对论流体. 其运动方程形如

$$
\frac { \partial T ^ { i j } } { \partial x ^ { j } } = 0 , \quad i = 0 , 1 , \quad x ^ { 0 } = t , \quad x ^ { 1 } = x .
$$

能-动量张量 $T ^ { i j } = T j i$ 的三个分量并不是独立的, 它们要满足一个约束条件, 此约束为相对论流体的状态方程. 根据相对论的不变性条件, 此状态方程仅仅是对张量 $( T ^ { i j } )$ 的不变量的限制:

$$
f ( { \mathcal { E } } , { \mathcal { P } } ) = 0 .
$$

这里的 $\mathcal { E } , \mathcal { P }$ 为此流体在余活动标架 [使得成立

$$
T ^ { i ^ { \prime } j ^ { \prime } } = { \binom { \varepsilon } { 0 } } \mathcal { P } \Biggr )
$$

的洛伦兹标架] 下的能量密度与压强.

记靶空间坐标 $u ^ { 0 } = T ^ { 0 0 } = \varepsilon$ (能量密度) 与 $u ^ { 1 } = T ^ { 0 1 } = p$ (动量密度). 在此局部坐标下的运动方程为

$$
\varepsilon _ { t } + p _ { x } = 0 , \quad p _ { t } + ( \varepsilon - 2 q ) _ { x } = 0 .
$$

其中 $2 q = T _ { i } ^ { i } = \mathcal { E } - \mathcal { P }$ 为能-动量张量的洛伦兹迹 (Lorentz-trace). 此 $\varepsilon , p$ 是关于其泊松括号的 Liouville 坐标, 且相应的

$$
( \gamma ^ { i j } ) = - \left( { p \atop \varepsilon } \ : \ : \ : ^ { \varepsilon - 2 q } \right) .
$$

哈密顿量为 $H = \int \varepsilon \mathrm { d } x$ . 度量 $g ^ { i j } = \gamma ^ { i j } + \gamma ^ { j i }$ 的正负惯性指数为 $( 1 , 1 )$

我们回到一般的一维流体力学型系统. 下述断言给出了如下系统

$$
u _ { t } ^ { i } = v _ { j } ^ { i } ( u ) u _ { x } ^ { j }
$$

为哈密顿系统的一个判据 (Tsarev [17]).

引理. 上述系统是流体力学型哈密顿系统 $\Longleftrightarrow$ 存在靶空间上的 (非退化的) 平坦度量 $g ^ { i j } ( u )$ 满足

$$
\begin{array} { l } { g _ { i k } v _ { j } ^ { k } = g _ { j k } v _ { i } ^ { k } } \\ { \nabla _ { i } v _ { j } ^ { k } = \nabla _ { j } v _ { i } ^ { k } . } \end{array}
$$

证明. 若上述系统具有哈密顿量

$$
H = \int h ( \boldsymbol { u } ) \mathrm { d } \boldsymbol { x } ,
$$

则相应哈密顿系统 $u _ { t } ^ { i } ( x ) = \{ u ^ { i } ( x ) , H \}$ 系数矩阵满足6

$$
v _ { j } ^ { i } ( u ) = \nabla ^ { i } \nabla _ { j } h ( u )
$$

这里的 $\nabla _ { i }$ 为度量 $\left( g _ { i j } \right)$ 的 Levi-Civita 联络的协变导数, $\nabla ^ { i } = g ^ { i k } \nabla _ { k }$ . 因此有

$$
g _ { i k } v _ { j } ^ { k } = \nabla _ { i } \nabla _ { j } h .
$$

从而由 Levi-Civita 联络的对称性立刻得到 (a). 再由度量的平坦性以及联络与度量相容性可证明 (b):

$$
\nabla _ { i } v _ { j } ^ { k } = - \nabla _ { i } \nabla ^ { k } \nabla _ { j } h = - \nabla _ { i } \nabla _ { j } \nabla ^ { k } h = \nabla _ { j } v _ { i } ^ { k } .
$$

反之, 从 (b) 可知存在向量场 $h ^ { i }$ 使得系数矩阵 $v _ { j } ^ { i }$ 形如

$$
v _ { j } ^ { i } = - \nabla _ { j } h ^ { i } .
$$

再由 (a) 可知相应的 1-形式 $h _ { i } = g _ { i k } h ^ { k }$ 是闭的, 从而形如

$$
h _ { i } = \partial _ { i } h \equiv \nabla _ { i } h .
$$

引理证毕.

例子 3. 非齐次的一次泊松括号. 这种泊松括号形如

$$
\{ u ^ { i } ( x ) , u ^ { j } ( y ) \} = g ^ { i j } ( u ( x ) ) \delta ^ { \prime } ( x - y ) + [ b _ { k } ^ { i j } ( u ) u _ { x } ^ { k } + h ^ { i j } ( u ) ] \delta ( x - y ) .
$$

$g ^ { i j } ( u )$ , $h _ { k } ^ { i j } ( u )$ 的微分几何意义与之前一样. 反对称矩阵 $h ^ { i j }$ 定义了靶空间上的一个有限维泊松括号. 在度量 $( g ^ { i j } )$ 非退化的假设下, 下述断言成立 (见 [7]).

定理. 在关于度量 $( g ^ { i j } )$ 的平坦坐标 $\boldsymbol { u } ^ { 1 } , . . . , \boldsymbol { u } ^ { N }$ 下, 上述非齐次的一次泊松括号恰为关于某李代数 $\mathfrak { g }$ 的 (非齐次)Kac-Moody 括号 (见第 3 节例 $5 _ { , }$ ):

$$
\{ u ^ { i } ( x ) , u ^ { j } ( y ) \} = \hat { g } ^ { i j } \delta ^ { \prime } ( x - y ) + [ c _ { k } ^ { i j } v ^ { k } + c _ { 0 } ^ { i j } ] \delta ( x - y ) ,
$$

其中 $c _ { k } ^ { i j }$ 为 $\mathfrak { g }$ 的结构常数, $\hat { g } ^ { i j }$ 与 $c _ { 0 } ^ { i j }$ 分别为 $\mathfrak { g }$ 的不变双线性型与 2-上链.

例子 4. 格上的泊松括号与 Yang-Baxter 方程. 我们来看离散版本的微分几何泊松括号. 场 $u ^ { i }$ , $i = 1 . . . , N$ 定义在一维 格 (lattice) 上: $u ^ { i } = ( u _ { n } ^ { i } ) , n \in \mathbb { Z }$ (我们只考虑空间一维情形). $n _ { 0 }$ 次的微分几何泊松括号形如

$$
\begin{array} { l } { { \{ u _ { n } ^ { i } , u _ { m } ^ { j } \} = h _ { m - n } ^ { i j } ( u _ { n } , u _ { m } ) , } } \\ { { h _ { k } ^ { i j } = 0 , \quad \forall | k | > n _ { 0 } . } } \end{array}
$$

该括号的反对称性等价于 $h _ { - k } ^ { i j } ( u , v ) = - h _ { k } ^ { j i } ( v , u )$ . 在局部坐标变换

$$
u _ { n } ^ { i } \to u _ { n } ^ { i ^ { \prime } } = f ^ { i } ( u _ { n } ^ { 1 } , . . . , u _ { n } ^ { N } ) , \quad i = 1 , . . . , N , n \in \mathbb { Z }
$$

下, 矩阵 $h _ { k } ^ { i j } ( u , v )$ 满足变换关系

$$
h _ { k } ^ { i j } ( u , v )  h _ { k } ^ { i ^ { \prime } j ^ { \prime } } ( u ^ { \prime } , v ^ { \prime } ) = \frac { \partial f ^ { i } ( u ) } { \partial u ^ { p } } \frac { \partial f ^ { j } ( v ) } { \partial v ^ { q } } h _ { k } ^ { p q } ( u , v ) .
$$

若 $n _ { 0 } = 0$ , 则称该括号是超局部的 (也就是说, 它由靶空间上的有限维泊松括号$h _ { 0 } ^ { i j } ( u )$ 所确定). 否则, 我们仅考虑 $n _ { 0 } = 1$ 的情形. [这是因为, 若 $n _ { 0 } > 1$ , 则引入新的场变量 $v _ { n } ^ { \alpha }$ , $\alpha = 1 , . . . , n _ { 0 } N$ 使得

$$
v _ { n } ^ { i + p N } = u _ { n n _ { 0 } + p } ^ { i } , \quad i = 1 , . . . , N , \quad p = 0 , 1 , . . . , n _ { 0 } - 1 .
$$

在此变换下, 我们得到关于 $v _ { n } ^ { \alpha }$ 的一次微分几何括号. ]

因此, 我们只考虑如下的一次泊松括号:

$$
\begin{array} { l } { { \{ u _ { n } ^ { i } , u _ { n } ^ { j } \} = h _ { 0 } ^ { i j } ( u _ { n } ) , \quad \{ u _ { n } ^ { i } , u _ { n + 1 } ^ { j } \} = h _ { 1 } ^ { i j } ( u _ { n } , u _ { n + 1 } ) , } } \\ { { \{ u _ { n } ^ { i } , u _ { m } ^ { j } \} = 0 \quad \# | n - m | > 1 . } } \end{array}
$$

如果张量 $h _ { 1 } ^ { i j } ( u , v )$ 非退化, 则 [5] 断言此泊松括号来自于某个哈密顿-李群 (见第 1 节).我们回忆: (连通且单连通的) 哈密顿-李群 $G$ 被其李双代数 $( L , c _ { \alpha \beta } ^ { \gamma } ; L ^ { * } , f _ { \gamma } ^ { \alpha \beta } )$ 所决定. 这里的 $L$ 为 $G$ 的李代数, 且 $c _ { \alpha \beta } ^ { \gamma }$ 为其结构常数; $L ^ { * }$ 为 $L$ 的对偶空间, 且具有与 $L$ 相容的李代数结构 $f _ { \gamma } ^ { \alpha \beta }$ .

设反对称矩阵 $h ^ { \alpha \beta }$ 使得上链

$$
\overline { { { f } } } _ { \gamma } ^ { \alpha \beta } = f _ { \gamma } ^ { \alpha \beta } + c _ { \varepsilon \gamma } ^ { \alpha } h ^ { \varepsilon \beta } + c _ { \varepsilon \gamma } ^ { \beta } h ^ { \alpha \varepsilon }
$$

也使得 $L ^ { * }$ 为李代数 (该李代数结构自动地与 $L$ 相容). 我们要求下述关系成立:

$$
\begin{array} { r l } & { c _ { \alpha \beta } ^ { \mu } h ^ { \alpha \nu } h ^ { \beta \lambda } + h ^ { \mu \alpha } c _ { \alpha \beta } ^ { \nu } h ^ { \beta \lambda } + h ^ { \mu \alpha } h ^ { \nu \beta } c _ { \alpha \beta } ^ { \lambda } } \\ { = } & { f _ { \varepsilon } ^ { \mu \nu } h ^ { \varepsilon \lambda } + f _ { \varepsilon } ^ { \lambda \mu } h ^ { \varepsilon \nu } + f _ { \varepsilon } ^ { \nu \lambda } h ^ { \varepsilon \mu } . } \end{array}
$$

[回顾: 上式等号左边恰为李代数 $L$ 的关于“ $\cdot _ { r } .$ -矩阵” ${ \ " } h ^ { \alpha \beta }$ 的经典 Yang-Baxter 方程, 见第1 节.] 最后, 必存在下述李代数同态

$$
r : ( L ^ { * } , f _ { \gamma } ^ { \alpha \beta } )  ( L , c _ { \alpha \beta } ^ { \gamma } ) , \quad r = ( r ^ { \alpha \beta } ) ;
$$

共轭映射 $r _ { * } ^ { \alpha \beta } = r ^ { \beta \alpha }$ 必为李代数同态:

$$
r _ { * } : ( L ^ { * } , \overline { { { f } } } _ { \gamma } ^ { \alpha \beta } )  ( L , c _ { \alpha \beta } ^ { \gamma } ) .
$$

对于哈密顿-李群 $G$ , 如果存在满足上述性质的同态 $r$ 与 $( h = h ^ { \alpha \beta }$ ), 则称 $G$ 是容许的.

定理. 容许的哈密顿-李群 $( G , r , h )$ 通过如下关系决定了一个格上的泊松括号: $u _ { n } \in$ $G , n \in \mathbb { Z }$ ,

$$
\begin{array} { r c l } { { \{ \varphi ( u _ { n } ) , \psi ( u _ { m } ) \} } } & { { = } } & { { 0 } } & { { \sharp \bigr | n - m | > 1 } } \\ { { \{ \varphi ( u _ { n } ) , \psi ( u _ { n + 1 } ) \} } } & { { = } } & { { r ^ { \alpha \beta } \partial _ { \alpha } \varphi ( u _ { n } ) \partial _ { \beta } ^ { \prime } \psi ( u _ { n + 1 } ) } } \end{array}
$$

其中 $\partial _ { \alpha } , \partial _ { \beta } ^ { \prime }$ 分别为 $G$ 的左, 右不变向量场,

$$
\{ \varphi ( u _ { n } ) , \psi ( u _ { n } ) \} = \eta ^ { \alpha \beta } ( u _ { n } ) \partial _ { \alpha } \varphi ( u _ { n } ) \partial _ { \beta } \psi ( u _ { n } ) ,
$$

其中

$$
\eta ^ { \alpha \beta } ( u ) = \eta _ { 0 } ^ { \alpha \beta } ( u ) + \mathrm { a d } _ { u ^ { - 1 } } h ^ { \alpha \beta }
$$

其中 $\eta _ { 0 } ^ { \alpha \beta }$ 由 $G$ 的哈密顿-李群结构确定 (见第 $\mathit { 1 }$ 节). 这里的 $\varphi , \psi$ 为 $G$ 上的任意光滑函数. 另一方面, 格上的所有的满足非退化条件 $\operatorname* { d e t } ( h _ { 1 } ^ { i j } ( u ) ) \neq 0$ 的一次微分几何泊松括号都可由此方法得到.

[注记: 上述非退化条件等价于 $r = ( r ^ { \alpha \beta } )$ 的非退化性. 换句话说, $r$ 为李代数同构$L ^ { * } \to L$ . 此时所有的容许条件都可化为李代数 $L$ 与矩阵 $r = ( r ^ { \alpha \beta } )$ 的条件. ]

三角哈密顿-李群 (见第 1 节) 的微分几何泊松括号是重要例子. 此时, 反对称矩阵$r ^ { \alpha \beta }$ 满足其李代数 $L$ 的经典 Yang-Baxter 方程. 于是上述定理给出的泊松括号为

$$
\{ \varphi ( u _ { n } ) , \psi ( u _ { n + 1 } ) \} = r ^ { \alpha \beta } \partial _ { \alpha } \varphi ( u _ { n } ) \partial _ { \beta } ^ { \prime } \psi ( u _ { n + 1 } ) ,
$$

$$
\{ \varphi ( u _ { n } ) , \psi ( u _ { n } ) \} = - r ^ { \alpha \beta } [ \partial _ { \alpha } \varphi ( u _ { n } ) \partial _ { \beta } \psi ( u _ { n } ) + \partial _ { \alpha } ^ { \prime } \varphi ( u _ { n } ) \partial _ { \beta } ^ { \prime } \psi ( u _ { n } ) ] .
$$

该泊松括号非退化当且仅当矩阵 $r ^ { \alpha \beta }$ 非退化. 此时李代数 $L$ 是拟-Frobnious 的.

例子. 对于最简单的二维非交换群 $G$ , 任取非退化矩阵作为 $r$ , 则有如下括号:

$$
h _ { 1 } ^ { i j } ( u , v ) = { \binom { \sigma y ^ { 2 } } { 0 } } ~ \frac { 0 } { 2 } \bigg ) ~ { \binom { a } { c } } ~ b \bigg ( \frac { 1 } { x ^ { \prime } } ~ \frac { 0 } { 2 } \bigg ) ~ ,
$$

$$
\begin{array} { l } { { u = ( x , y ) , \quad v = ( x ^ { \prime } , y ^ { \prime } ) , \quad \sigma = \pm 1 , } } \\ { { \nonumber h _ { 0 } ^ { i j } ( u ) = - h _ { 1 } ^ { i j } ( u , u ) + h _ { 1 } ^ { j i } ( u , u ) . } } \end{array}
$$

若取 ${ \left( \begin{array} { l l } { a } & { b } \\ { c } & { d } \end{array} \right) } = { \left( \begin{array} { l l } { \sigma } & { 0 } \\ { 0 } & { 2 } \end{array} \right) }$ 则得到 Toda 格方程 [18,16] 的第二个哈密顿结构.

[注记. 对于任意 $n _ { 0 }$ 次的微分几何泊松括号 $\{ u _ { n } ^ { i } , u _ { m } ^ { j } \} = h _ { m - n } ^ { i j } ( u _ { n } , u _ { m } )$ , 我们可以定义其关于参数 $\varepsilon$ 的 连续延伸 (continuous prolongation) :

$$
\{ u ^ { i } ( x ) , u ^ { j } ( y ) \} _ { \varepsilon } = \sum _ { k = - n _ { 0 } } ^ { n _ { 0 } } h _ { k } ^ { i j } ( u ( x ) , u ( y ) ) \delta ( x - y + k \varepsilon ) .
$$

] 为定义格上的泊松括号的连续极限, 考虑如下形式展开

$$
\{ u ^ { i } ( x ) , u ^ { j } ( y ) \} _ { \varepsilon } = \sum _ { s = 0 } ^ { \infty } \varepsilon ^ { s } \{ u ^ { i } ( x ) , u ^ { j } ( y ) \} _ { s } .
$$

则 $\{ u ^ { i } ( x ) , u ^ { j } ( y ) \} _ { 0 }$ 是超局部泊松括号 (由靶空间上某有限维泊松括号所确定). 若 $\{ u ^ { i } ( x ) , u ^ { j } ( y ) \} _ { 0 } =$ 0, 则 $\{ u ^ { i } ( x ) , u ^ { j } ( y ) \} _ { 1 }$ 为流体力学型泊松括号. 对于 (格上的) 一次泊松括号, 我们有

$$
\begin{array} { l } { { \{ u ^ { i } ( x ) , u ^ { j } ( y ) \} _ { 0 } = h ^ { i j } ( u ( x ) ) \delta ( x - y ) , } } \\ { { h ^ { i j } ( u ) = h _ { 0 } ^ { i j } ( u ) + h _ { 1 } ^ { i j } ( u , u ) - h _ { 1 } ^ { j i } ( u , u ) ; } } \\ { { \{ u ^ { i } ( x ) , u ^ { j } ( y ) \} _ { 1 } = g ^ { i j } ( u ( x ) ) \delta ^ { \prime } ( x - y ) + b _ { k } ^ { i j } ( u ( x ) ) u _ { x } ^ { k } \delta ( x - y ) , } } \\ { { g ^ { i j } ( u ) = h _ { 1 } ^ { i j } ( u , u ) + h _ { 1 } ^ { j i } ( u , u ) , } } \\ { { b _ { k } ^ { i j } ( u ) = \displaystyle \frac \partial { \partial v ^ { k } } ( h _ { 1 } ^ { i j } ( u , v ) + h _ { 1 } ^ { j i } ( v , u ) ) _ { v = u } . } } \end{array}
$$

在上例的二分量泊松括号中, $\{ , \} _ { 0 } \equiv 0$ , 从而其连续极限为流体力学型的.

对于由经典 Yang-Baxter 方程的解 $r ^ { \alpha \beta }$ 定义的格上的泊松括号 (见前文), 我们得到相应李群上的一个新的泊松括号:

$$
\{ \varphi ( u ) , \psi ( u ) \} = r ^ { \alpha \beta } [ \partial _ { \alpha } \varphi \partial _ { \beta } ^ { \prime } \psi - \partial _ { \beta } \varphi \partial _ { \alpha } ^ { \prime } \psi - \partial _ { \alpha } \varphi \partial _ { \beta } \psi + \partial _ { \alpha } ^ { \prime } \varphi \partial _ { \beta } ^ { \prime } \psi ] ( u )
$$

另一个 (更简单的) 例子是差分版本的 KdV 方程

$$
{ \dot { c } } _ { n } = c _ { n } ( c _ { n + 1 } - c _ { n - 1 } )
$$

[所谓的 Volterra 格方程] . 相应的哈密顿结构为

$$
\{ c _ { n } , c _ { m } \} = c _ { n } c _ { m } ( \delta _ { m , n + 1 } - \delta _ { n , m + 1 } )
$$

[这里的 $\delta$ 为 Kronecker $\delta$ 记号] , 哈密顿量为 $H = \sum c _ { n }$ . 我们有 $h _ { 0 } ( u ) \equiv 0$ , $h _ { 1 } ( u , v ) =$ uv, 其连续极限为

$$
\{ c ( x ) , c ( y ) \} _ { \varepsilon } = c ( x ) c ( y ) \left[ 2 \varepsilon \delta ^ { \prime } ( x - y ) + { \frac { \varepsilon ^ { 3 } } { 3 } } \delta ^ { \prime \prime \prime } ( x - y ) + \cdot \cdot \cdot \right] .
$$

若变量代换 $c ( x ) = 1 - \frac { \varepsilon ^ { 2 } } { 3 } u ( x )$ , 则得到

$$
\frac { \varepsilon ^ { 3 } } { 9 } \{ u ( x ) , u ( y ) \} = 2 \delta ^ { \prime } ( x - y ) - \frac { \varepsilon ^ { 2 } } { 6 } \left[ - \frac { 1 } { 2 } \delta ^ { \prime \prime } ( x - y ) + ( u ( x ) + u ( y ) ) \delta ^ { \prime } ( x - y ) \right] + O ( \varepsilon ^ { 4 } ) .
$$

我们注意到在离散 KdV 方程的泊松括号中 (某种意义下) 隐藏着 Gardner-Zakharov-Faddeev 括号与 Magri 括号.

# 第 2 章 可积系统理论基础

# 2.1 流体力学型系统的可积性理论

我们来探讨如何构造演化型 $( 1 + 1 )$ -哈密顿系统 $u _ { t } ^ { i } = \{ H , u ^ { i } ( x ) \}$ 的有限维不变流形. 这种不变流形有两种最简单的构造方式.

1. 对任何交换流

$$
u _ { s } ^ { i } = K ^ { i } ( x , t , u , u ^ { \prime } , \ldots ) , \quad u _ { t s } ^ { i } = u _ { s t } ^ { i } ,
$$

$s \cdot$ -流的满足

$$
K ^ { i } ( x , t , u , u ^ { \prime } , . . . ) = 0 , \quad i = 1 , 2 , . . . , N
$$

的稳定点集 $M = M _ { K }$ 关于 $t { \cdot }$ -演化不变 [此系统甚至不必为哈密顿系统] .

2. 对任意守恒律 $F = \int f ( u , u ^ { \prime } , \ldots ) \mathrm { d } x$ , 考虑此泛函的极值 (extrema) 点集

$$
N _ { F } : = \Big \{ u ( x ) \Big | \frac { \delta F } { \delta u ^ { i } ( x ) } = 0 \Big \} .
$$

第一种构造的主要例子是流体力学型系统的可积性理论. 若此交换流为关于哈密顿量 $F$ 的哈密顿系统, 则 $N _ { F } \subseteq M _ { k }$ . 而当泊松括号退化时, 此命题的逆命题不成立. 若泊松括号的零因子 (annihilator) 由局部泛函 $A _ { 1 } , . . . , A _ { s }$ 生成, 则任何哈密顿流$u _ { s } ^ { i } ( x ) = K ^ { i } ( u , u ^ { \prime } , \ldots ) = \{ F , u ^ { i } ( x ) \}$ 的稳定点集 $M _ { K }$ 可表示为 $M _ { K } = \bigcup _ { c } N _ { \hat { F } _ { c } }$ , $\hat { F } _ { c } =$ $F + c _ { 1 } A _ { 1 } + \cdot \cdot \cdot + c _ { s } A _ { s }$ , 其中 $\boldsymbol { c } = ( c _ { 1 } , . . . , c _ { s } )$ 为常值向量.

从而, 即使对于哈密顿系统, 考虑与之交换的非哈密顿流有时也有用.

下面考虑流体力学型哈密顿系统:

$$
\begin{array} { r l } & { u _ { t } ^ { i } = v _ { j } ^ { i } ( u ) u _ { x } ^ { j } = \{ H , u ^ { i } ( x ) \} , \quad H = \displaystyle \int h ( u ) \mathrm { d } x , } \\ & { \{ u ^ { i } ( x ) , u ^ { j } ( y ) \} = g ^ { i j } ( u ( x ) ) \delta ^ { \prime } ( x - y ) + b _ { k } ^ { i j } ( u ) u _ { x } ^ { k } \delta ( x - y ) . } \end{array}
$$

在考虑与此交换的另一个流体力学型系统:

$$
u _ { s } ^ { i } = w _ { j } ^ { i } ( u ) u _ { x } ^ { j } , \quad ( u _ { t } ^ { i } ) _ { s } = ( u _ { s } ^ { i } ) _ { t } .
$$

[可以证明, 对角的流体力学型哈密顿系统存在这样的交换流 (见 Novikov, Tsarev[26-28])] . 第二个流的稳定点集是平凡的 [只有常函数] . 但我们可考虑将此流与另一个与尺度变换 $( x , t ) \mapsto ( k x , k t )$ 有关的第三个流

$$
u _ { r } ^ { i } = x u _ { x } ^ { i } + t u _ { t } ^ { i } = ( x \delta _ { j } ^ { i } + t v _ { j } ^ { i } ( u ) ) u _ { x } ^ { j }
$$

的组合. 因此下述断言成立:

引理 2.1. 由下式

$$
w _ { j } ^ { i } ( u ) = x \delta _ { j } ^ { i } + t v _ { j } ^ { i } ( u ) , \quad i , j = 1 , . . . , N
$$

确定的隐函数 $u ^ { i } = u ^ { i } ( x , t )$ 满足方程 (2.1).

证明. 这是流 $u _ { s } ^ { i } - u _ { r } ^ { i }$ 的稳定点集.

此系统的相容性是因为该系统的如下等价表示:

$$
w ^ { i } ( u ) = x + v ^ { i } ( u ) t , \quad i = 1 , . . . , N .
$$

其中 $w ^ { 1 } ( u ) , . . . , w ^ { N } ( u )$ 与 $v ^ { 1 } ( u ) , . . . , v ^ { N } ( u )$ 分别为矩阵 $( w _ { j } ^ { i } ( u ) )$ 与 $( v _ { j } ^ { i } ( u ) )$ 的特征值.

现在, 我要将某些特定的流体力学型哈密顿系统定义为“可积的”(integrable). 这种系统应该存在形如 (2.1’) 的交换流. 此外, (2.1) 的任何解在局部上都应该能够通过(2.1’)(2.2) 求得. 还应当要求, 在 Liouville 定理的某种无穷维推广下此系统是完全可积的.

这类特殊的流体力学型哈密顿系统正是可对角化的流体力学型哈密顿系统. 这是指, 在适当的局部坐标下, (2.1) 的系数矩阵 $( v _ { j } ^ { i } ( u ) )$ 为对角阵. 换句话说此系统的黎曼不变量 [见本节的附录 1] 存在. Novikov 认为如此的流体力学型系统是可积的; 他的学生Tsarev 在其博士论文当中给出了这种系统的可积性的证明.

现在假定哈密顿系统 (2.1) 在局部坐标 $u ^ { 1 } , . . . , u ^ { N }$ 下是对角的:

$$
u _ { t } ^ { i } = v ^ { i } ( u ) u _ { x } ^ { i } , \quad i = 1 , . . . , N
$$

[本节不假定对重复指标自动求和] , 并且当 $i \neq j$ 时 $v ^ { i } \neq v ^ { j }$ .

引理 2.2. 在此 $u ^ { i }$ -局部坐标下, 此流体力学型哈密顿系统的相应度量 $g ^ { i j } ( u )$ 也 是对角的:

$$
g ^ { i j } ( u ) = g ^ { i } ( u ) \delta ^ { i j } .
$$

证明. 由对称性条件 $g _ { i k } v ^ { k j } = g _ { j k } v _ { i } ^ { k }$ [见 1.4 节的某引理] 可知当 $i \neq j$ 时有

$$
g _ { i j } v ^ { j } = g _ { j i } v ^ { i } \Longrightarrow g _ { i j } = 0 .
$$

在微分几何的观点下, 零曲率的对角度量可被平坦空间 (配以欧氏度量或者不定度量) 中的 $N .$ -正交曲线坐标系所确定. [根据 E.Cartan [29] 的结果, 此坐标系局部上可由N(N − 1) 个二元函数所确定] . 反之, 任何正交曲线坐标系都定义了一族交换的对角的流体力学型哈密顿系统, 它们可由下述定理确定:

定理 2.3. 设 $\Gamma _ { j k } ^ { i }$ 为平坦对角度量 (2.4) 的 Levi-Civita 联络的 Christoffel 符号, 则在此局部坐标下, 流体力学型哈密顿系统

$$
u _ { s } ^ { i } = w ^ { i } ( u ) u _ { x } ^ { i }
$$

的系数满足如下方程组:

$$
\partial _ { i } w ^ { k } = \Gamma _ { k i } ^ { k } ( w ^ { i } - w ^ { k } ) , \quad \left( \partial _ { i } = \frac { \partial } { \partial u ^ { i } } \right) , \quad i \neq k .
$$

反之, 方程组 (2.6) 的每一个解都确定了一个流体力学型哈密顿系统; 任意 $N$ 个单变量函数均确定了方程组 (2.6) 的一个解.

这些哈密顿系统两两交换.

证明. 对角系统 (2.5) 在由对角的平坦度量 (2.4) 所确定的泊松括号意义下是哈密顿系统, 当且仅当 [1.4 节介绍过的] 的下述对称性条件 (a)(b) 成立:

$$
\sum _ { k } g _ { i k } w _ { j } ^ { k } = \sum _ { k } g _ { j k } w _ { i } ^ { k }
$$

$$
\nabla _ { i } w _ { j } ^ { k } = \nabla _ { j } w _ { i } ^ { k }
$$

其中 $g _ { i j } = g _ { i } \delta _ { i j }$ , $g _ { i } = \frac { 1 } { g ^ { i } } , w _ { j } ^ { i } = w ^ { i } \delta _ { j } ^ { i }$ . 对称性条件 (a) 是平凡成立的, 而条件 (b) 等价于(2.6). 系统 (2.5) 的哈密顿量 $F = \int f ( u ) \mathrm { d } x$ 可由下述方程确定:

$$
\nabla _ { i } ^ { 2 } f ( u ) + g _ { i } ( u ) w ^ { i } ( u ) = 0 , \quad i = 1 , . . . , N .
$$

下面证明超定的线性系统 (b) 是相容的. 此相容性条件为 $\partial _ { j } ( \partial _ { i } w ^ { k } ) = \partial _ { i } ( \partial _ { j } w ^ { k } )$ 对任意互不相同的指标 $i , j , k$ 成立; 显式地,

$$
\begin{array} { r c l } { { 0 } } & { { = } } & { { ( \Gamma _ { k i , j } ^ { k } - \Gamma _ { k i } ^ { k } \Gamma _ { i j } ^ { i } - \Gamma _ { k j } ^ { k } \Gamma _ { j i } ^ { j } + \Gamma _ { k j } ^ { k } \Gamma _ { k i } ^ { k } ) w ^ { i } } } \\ { { } } & { { } } & { { + ( \Gamma _ { k i } ^ { k } \Gamma _ { i j } ^ { i } - \Gamma _ { k i } ^ { k } \Gamma _ { k j } ^ { k } - \Gamma _ { k j , i } ^ { k } + \Gamma _ { k j } ^ { k } \Gamma _ { j i } ^ { j } ) w ^ { j } } } \\ { { } } & { { } } & { { + ( \Gamma _ { k j , i } ^ { k } - \Gamma _ { k i , j } ^ { k } ) w ^ { k } . } } \end{array}
$$

[这里的 $\Gamma _ { k i , j } ^ { k } \equiv \partial _ { j } \Gamma _ { k i } ^ { k }$ , 其余类似] . 由众所周知的公式

$$
\Gamma _ { k i } ^ { k } = \partial _ { i } \log \sqrt { g _ { k } } , \quad i \neq k
$$

可知上式右端 $w ^ { k }$ 的系数为零. 而 $w ^ { i }$ 与 $w ^ { j }$ 的系数分别等于曲率 $R _ { i j k } ^ { k }$ 与 $- R _ { j i k } ^ { k }$ . 因为此度量的曲率为零, 从而方程组 (2.6) 相容. 从而其解在局部上可被 $N$ 个一元函数所确定.

最后, 我们证明所有的形如 (2.5) 的哈密顿流两两交换. 只需证明任意两个对角哈密顿流

$$
u _ { t } ^ { i } = v ^ { i } ( u ) u _ { x } ^ { i } , \quad u _ { s } ^ { i } = w ^ { i } ( u ) u _ { x } ^ { i }
$$

交换. 其交换性条件 $( u _ { t } ^ { i } ) _ { s } = ( u _ { s } ^ { i } ) _ { t }$ 等价于

$$
{ \frac { \partial _ { k } v ^ { i } } { v ^ { k } - v ^ { i } } } = { \frac { \partial _ { k } w ^ { i } } { w ^ { k } - w ^ { i } } } , \quad i \neq k .
$$

而系数 $v ^ { i }$ 与 $w ^ { i }$ 都满足 (2.6), 从而上式两端都等于 $\Gamma _ { i k } ^ { i }$ , 得证.

注记. 容易证明任何与对角哈密顿系统 (2.3) 交换的流体力学型系统

$$
u _ { s } ^ { i } = \sum _ { j } w _ { j } ^ { i } ( u ) u _ { x } ^ { j }
$$

必为对角哈密顿系统. [其中 $\boldsymbol { v } ^ { 1 } , . . . , \boldsymbol { v } ^ { N }$ 两两互异] .

因此对于对角的流体力学型系统 (2.3), 有如下 积分算法 (algorithm of integration)

1. 求解满足线性系统

$$
\partial _ { k } w ^ { i } = { \frac { \partial _ { k } v ^ { i } } { v ^ { k } - v ^ { i } } } ( w ^ { k } - w ^ { i } ) , \quad i \neq k
$$

的函数 $w ^ { 1 } ( u ) , . . . , w ^ { N } ( u )$

2. 对该系统的任何解 $w ^ { 1 } ( u ) , . . . , w ^ { N } ( u )$ , 隐函数方程组

$$
w ^ { i } ( u ) = v ^ { i } ( u ) t + x , \quad i = 1 , . . . , N
$$

确定了解 $u ( x , t )$ .

可以证明 [28], 在满足 $u _ { x } ^ { i } ( x _ { 0 } , t _ { 0 } ) \neq 0$ , $i = 1 , . . . , N$ 的点 $( x _ { 0 } , t _ { 0 } )$ 附近, 方程组 (2.3)的任何解都可由上述算法得到.

注记. 上述“积分算法”已被证明不止适用于对角的流体力学型哈密顿系统, 而且还适用于更广的一类对角的流体力学型系统. 这种更一般的对角的流体力学型系统由 Tsarev引入 [27,28], 他称此为流体力学型 半哈密顿系统 (semi-Hamiltonian system) . 其定义为: 对任意两两互异的指标 $i , j , k$ 成立

$$
\partial _ { i } \left( \frac { \partial _ { j } v ^ { k } } { v ^ { j } - v ^ { k } } \right) = \partial _ { j } \left( \frac { \partial _ { i } v ^ { k } } { v ^ { i } - v ^ { k } } \right)
$$

的对角的流体力学型系统. 对角的流体力学型哈密顿系统显然是半哈密顿的, 这是因为(2.6) 与 (2.7). 其逆命题一般不正确. 例如, 任何 2-分量的对角的流体力学型系统是半哈密顿的 [单分量的显然也是] . [顺便一提, 任何 2-分量的流体力学型系统都是可对

角化的, 至少通过复数域上的坐标变换. 1] 对于半哈密顿系统, 也可以引入对角度量$g _ { i j } = g _ { i } ( u ) \delta _ { i j }$ . 在相差变换 $g _ { i } ( u )  g _ { i } ( u ) \varphi _ { i } ( u ^ { i } )$ 的意义下, 此对角度量可由方程组

$$
\partial _ { i } \log \sqrt { g _ { k } } = \frac { \partial _ { i } v ^ { k } } { v ^ { i } - v ^ { k } } , \quad i \neq k
$$

所确定. (2.10) 保证了此方程组的相容性. 该对角度量的曲率不一定为零, 但由 (2.10)可知该度量的曲率张量是对角的: 曲率张量的非零分量必形如 $R _ { i j i j }$ . 对这样的对角矩阵, 此定理的陈述依然正确.

例子 1. 对于单分量情形

$$
u _ { t } = v ( u ) u _ { x } ,
$$

任何函数 $w ( u )$ 都确定了一个交换流

$$
u _ { s } = w ( u ) u _ { x } .
$$

因此对任意函数 $w ( u )$ , 由方程

$$
w ( u ) = x + v ( u ) t
$$

确定的隐函数 $u = u ( x , t )$ 都是 (2.12) 的解. 此公式是众所周知的.

例子 2. 考虑 2-分量的对角的流体力学型系统

$$
\left\{ \begin{array} { l } { u _ { t } ^ { 1 } = v ^ { 1 } ( u ) u _ { x } ^ { 1 } } \\ { u _ { t } ^ { 2 } = v ^ { 2 } ( u ) u _ { x } ^ { 2 } } \end{array} \right. ~ .
$$

此时, 之前所述“积分算法”其实刚好是众所周知的“速端曲线法 (hodograph method)”. 经过 速端曲线变换 (hodograph transform) $( x , t )  ( u ^ { 1 } , u ^ { 2 } )$ 之后, 此方程变为

$$
\left. \begin{array} { l } { \partial _ { 2 } x + v ^ { 1 } ( u ) \partial _ { 2 } t = 0 } \\ { \partial _ { 1 } x + v ^ { 2 } ( u ) \partial _ { 1 } t = 0 } \end{array} \right\} , \quad x = x ( u ) , t = t ( u ) , \partial _ { 1 } = \frac { \partial } { \partial u ^ { 1 } } , \partial _ { 2 } = \frac { \partial } { \partial u ^ { 2 } } .
$$

1译者注: 我们总假定流体力学型系统 $u _ { t } ^ { i } = \sum _ { j } v _ { j } ^ { i } ( u ) u _ { x } ^ { j }$ 的系数矩阵 $( v _ { j } ^ { i } )$ 的 (复) 特征值两两互异.

或者等价地,

$$
\begin{array} { l c l } { { \partial _ { 2 } \underbrace { \left( v ^ { 1 } t + x \right) } _ { w ^ { 1 } } } } & { { = } } & { { t \partial _ { 2 } v ^ { 1 } } } \\ { { } } & { { } } & { { } } \\ { { \partial _ { 1 } \underbrace { \left( v ^ { 2 } t + x \right) } _ { w ^ { 2 } } } } & { { = } } & { { t \partial _ { 1 } v ^ { 2 } . } } \end{array}
$$

由于 w − w v2 − v1 , 我们得到形如 (2.8) 的方程

$$
\frac { \partial _ { 2 } w ^ { 1 } } { w ^ { 2 } - w ^ { 1 } } = \frac { \partial _ { 2 } v ^ { 1 } } { v ^ { 2 } - v ^ { 1 } } \quad , \quad \frac { \partial _ { 1 } w ^ { 2 } } { w ^ { 1 } - w ^ { 2 } } = \frac { \partial _ { 1 } v ^ { 2 } } { v ^ { 1 } - v ^ { 2 } } .
$$

此过程的逆是平凡的.

正由此例, 我们将流体力学型哈密顿 (或半哈密顿) 系统的“积分算法”(2.8)(2.9)称为 广义速端曲线变换 (generalized hodograph transform)

例子 3. 理想层析 (chromatography) 方程. 它描述了 $N .$ -组分化合物在吸附剂中的渗流. 此方程形如

$$
\begin{array} { l } { { c u _ { x } ^ { i } + ( a ^ { i } ( u ) + u ^ { i } ) _ { t } = 0 , \quad i = 1 , . . . , N , } } \\ { { \displaystyle a ^ { i } ( u ) = \alpha _ { i } k _ { i } u ^ { i } / V , \quad V = 1 + \sum _ { s = 1 } ^ { N } k _ { s } u ^ { s } . } } \end{array}
$$

其中 $\alpha _ { i } , k _ { i } , c$ 为常数, $u ^ { i } , a ^ { i }$ 分别为第 $i$ 个未被吸收与被吸收组分的浓度. 方程组 (2.14)可通过变换

$$
u ^ { 1 } , . . . , u ^ { N } \mapsto r ^ { 1 } , . . . , r ^ { N }
$$

对角化 [31], 其中 $r ^ { i } = r ^ { i } ( u )$ 为方程

$$
\sum _ { i = 1 } ^ { N } { \frac { \alpha _ { j } k _ { j } ^ { 2 } u ^ { j } } { \alpha _ { j } k _ { j } - r } } = V
$$

的根. 在坐标 $r ^ { 1 } , . . . , r ^ { N }$ 下方程组 (2.14) 化为对角型 [32]:

$$
r _ { t } ^ { i } = v ^ { i } ( r ) r _ { x } ^ { i } , \quad v ^ { i } = r ^ { i } \prod _ { k = 1 } ^ { N } r ^ { k } , \quad i = 1 , . . . , N .
$$

此系统是半哈密顿的, 并且当 $N \geq 4$ 是不是哈密顿的. 方程组 (2.15) 的通解可见 [32],其形如 (2.9), 其中

$$
\begin{array} { r } { w ^ { i } ( r ) = v ^ { i } ( r ) \partial _ { i } \displaystyle \sum _ { k = 1 } ^ { N } \frac { A _ { k } ( r _ { k } ) } { \prod _ { m \neq k } ( r _ { m } - r _ { k } ) } , } \end{array}
$$

其中 $A _ { 1 } ( r _ { 1 } ) , . . . , A _ { N } ( r _ { N } )$ 为任意函数.

我打算建立一些关于对角流体力学型哈密顿系统的守恒律的定理, 来结束对可积性理论的讨论. 回顾流体力学型泛函形如

$$
I = \int P ( u ) \mathrm { d } x .
$$

定理 2.4. (1) 对角的流体力学型哈密顿系统 (2.3) 具有无穷多族形如 (2.16) 的流体力学型守恒律; 且该守恒律的密度函数可由下述系统确定:

$$
\begin{array} { r } { \partial _ { i } \partial _ { j } P - \Gamma _ { i j } ^ { i } \partial _ { i } P - \Gamma _ { j i } ^ { j } \partial _ { j } P = 0 , \quad i \ne j } \\ { \left( \Gamma _ { p q } ^ { p } = \frac { \partial _ { q } v ^ { p } } { v ^ { q } - v ^ { p } } \right) . } \end{array}
$$

局部上它们被 $N$ 个任意的一元函数所决定.

(2) 这些泛函是所有的与之交换的对角哈密顿系统 $( 2 . 5 ) ( 2 . 6 )$ 的公共的守恒律.

(3) 这些守恒律的泊松括号两两为零.

(4) 对于每个守恒律 (2.16), 相应的哈密顿系统 $u _ { s } ^ { i } ( x ) = \{ I , u ^ { i } ( x ) \}$ 是对角的.

证明. 与定理 2.3 的证明类似.

此定理的 (1)(2) 也适用于半哈密顿系统.

这些两两交换 (即泊松括号为零) 的守恒律构成一个完备族, 这是指, 它们的斜梯

度张成了其公共等值面的切空间. 更形式地讲 [28], 我们称这一族两两交换的守恒律$\{ I = \int P ( u ) \mathrm { d } x \}$ 在相空间中的点 $u _ { 0 } ( x ) = ( u _ { 0 } ^ { 1 } ( x ) , . . . , u _ { 0 } ^ { N } ( x ) )$ 处完备, 如果对任何变分$\delta u ^ { i } ( x )$ , 若对这一族守恒律之中的任何一个 $I$ 都有

$$
\delta I \equiv \int \partial _ { i } P ( u _ { 0 } ) \delta u ^ { i } ( x ) = 0 ,
$$

则在这一族守恒律中存在某个 $I _ { 1 } = \int P _ { 1 } ( u ) \mathrm { d } x$ 使得 $\delta u ^ { i }$ 是在点 $u _ { 0 } ( x )$ 处的相应的哈密顿向量场:

$$
\delta u ^ { i } ( x ) = \{ I _ { 1 } , u ^ { i } ( x ) \} | _ { u = u _ { 0 } } .
$$

对于 $| x | \to \infty$ 速降函数 $u ^ { i } ( x )$ 的相空间或者周期函数相空间的情形, [27] 证明了如此意义下的完备性. 其中我们假定函数 $u _ { 0 } ( x )$ 满足下述附加条件: (a) 函数 $u _ { 0 } ^ { i } ( x )$ 的任何值都不会被超过两个点取到 [对于周期函数的情形, 限制在一个周期内谈论] . (b) 函数 $u _ { 0 } ^ { i } ( x )$ 的任何临界点都非退化. 此完备性定理的证明见 [28].

# 附录 1. 流体力学型系统的黎曼不变量

考虑任意给定的流体力学型系统

$$
u _ { t } ^ { i } = v _ { j } ^ { i } ( u ) u _ { x } ^ { j } , \quad i = 1 , . . . , N
$$

[这里又重新假定对重复指标求和] . 假设此系统是严格双曲的 (strictly hyperbolic), 即矩阵 $( v _ { j } ^ { i } ( u ) )$ 的特征值 $v ^ { 1 } , . . . , v ^ { n }$ 是两两互异的实数. 那么是否可能找到新的局部坐标$r ^ { 1 } , . . . , r ^ { N }$ , $r ^ { i } = r ^ { i } ( u )$ 使得 (2.18) 在此坐标下是形如

$$
r ^ { i } ( t ) = v ^ { i } r _ { x } ^ { i } , \quad v ^ { i } = v ^ { i } ( r ) , i = 1 , . . . , N
$$

的对角系统? 如果可以, 那么函数 $r ^ { 1 } , . . . , r ^ { N }$ 称为 (2.18) 的 黎曼不变量 (Riemanninvariant) , 并称该方程组可对角化. 对于系数矩阵 $( v _ { j } ^ { i } ( u ) )$ 的特征值为互异复数的流体力学型系统, 我们也可在复坐标变换下谈论对角化.

若 $N = 2$ , 则 (2.18) 必可对角化. 事实上, 取 余向量 (co-vector) $\boldsymbol { \omega } _ { i } ^ { ( 1 ) } , \boldsymbol { \omega } _ { i } ^ { ( 2 ) }$ 使得

$$
\omega _ { i } ^ { ( k ) } v _ { j } ^ { i } = v ^ { k } \omega _ { j } ^ { ( k ) } , \quad k = 1 , 2
$$

[即矩阵 $( v _ { j } ^ { i } )$ 的“左特征向量”] . 则可通过适当乘以函数系数, 使得 1-形式 $\omega _ { i } ^ { ( k ) } \mathrm { d } u ^ { i }$ 是闭形式. 从而局部地有

$$
\begin{array} { r } { \omega _ { i } ^ { ( k ) } \mathrm { d } u ^ { i } = \mathrm { d } r ^ { k } , \quad k = 1 , 2 . } \end{array}
$$

函数 $r ^ { i } ( u ) , r ^ { 2 } ( u )$ 即为我们所求的黎曼不变量.

当 $N \geq 3$ 时, 流体力学型系统一般不可对角化. 为刻画将其对角化的障碍, 我们引入 Nijenhuis 张量 [33]. 回顾: 对任意 $( 1 , 1 )$ -型张量 $V = ( v _ { j } ^ { i } )$ , 相应的 Nijenhuis 张量 $N _ { i j } ^ { k }$ 为如下 $( 1 , 2 )$ -型张量:

$$
N _ { i j } ^ { k } = v _ { i } ^ { p } v _ { j , p } ^ { k } - v _ { j } ^ { p } v _ { i , p } ^ { k } + v _ { p } ^ { k } ( v _ { i , j } ^ { p } - v _ { j , i } ^ { p } ) .
$$

等价地, 对任意向量场 $a = ( a ^ { i } )$ , $b = ( b ^ { i } )$ , 向量场 $N ( a , b ) = ( N _ { i j } ^ { k } a ^ { i } b ^ { j } )$ 形如

$$
N ( a , b ) = [ V a , V b ] + V ^ { 2 } [ a , b ] - V [ a , V b ] - V [ V a , b ] .
$$

考虑另一个 $( 1 , 2 )$ -型张量

$$
\begin{array} { r } { K _ { i j } ^ { k } = v _ { s } ^ { k } ( v _ { p } ^ { s } N _ { i j } ^ { p } - N _ { i p } ^ { s } v _ { j } ^ { p } ) - ( v _ { p } ^ { k } N _ { s j } ^ { p } - N _ { s p } ^ { k } v _ { j } ^ { p } ) v _ { i } ^ { s } . } \end{array}
$$

相应的向量场 $K ( a , b ) = ( K _ { i j } ^ { k } a ^ { i } b ^ { j } )$ 形如

$$
K ( a , b ) = V ^ { 2 } N ( a , b ) - V N ( a , V b ) - V N ( V a , b ) + N ( V a , V b ) .
$$

性质. [34]. 方程组 (2.18) 可对角化当且仅当 (2.19) 中的张量 $( K _ { i j } ^ { k } ) \equiv 0$

证明. 若 (2.18) 可对角化, 则 $K = 0$ . 由于 $K$ 为张量, 从而 $K = 0$ 为可对角化的必要条件. 2 我们来证明充分性. 设 $\lambda \neq \mu$ 为矩阵 $V$ 的两个特征值, 相应的特征向量分别为$a , b$ :

$$
V a = \lambda a , \quad V b = \mu b ,
$$

则有如下等式:

$$
N ( a , b ) \ = \ ( V - \lambda ) ( V - \mu ) [ a , b ] + ( \lambda - \mu ) ( \partial _ { b } \lambda \cdot a + \partial _ { a } \mu \cdot b ) ,
$$

$$
{ \begin{array} { l l l } { K ( a , b ) } & { = } & { ( V - \lambda ) ( V - \mu ) N ( a , b ) = ( V - \lambda ) ^ { 2 } ( V - \mu ) ^ { 2 } [ a , b ] . } \end{array} }
$$

若 $K = 0$ , 则由 $K ( a , b ) = 0$ 可知存在函数 $\alpha , \beta$ 使得

$$
[ a , b ] = \alpha a + \beta b .
$$

设 $a _ { 1 } , . . . , a _ { N }$ 分别是 $V$ 的属于特征值 $\boldsymbol { v } ^ { 1 } , . . . , \boldsymbol { v } ^ { N }$ 的特征向量. 由 (2.20) 不妨设

$$
\left[ a _ { i } , a _ { j } \right] = { \alpha } _ { i j } a _ { i } - { \alpha } _ { j i } a _ { j } ,
$$

其中 $\alpha _ { i j } = \alpha _ { i j } ( u )$ 为函数. 我们企图将这些特征向量适当数乘使得新得到的 $e _ { i } : = c _ { i } a _ { i }$ 两两交换, $[ e _ { i } , e _ { j } ] = 0$ . 这样的系数函数 $c _ { i }$ 应满足方程组

$$
\partial _ { a _ { i } } c _ { j } + \alpha _ { i j } c _ { j } = 0 , \quad i \neq j .
$$

此方程组应当相容, 可以验证其相容性条件等价于李括号 (2.21) 的雅可比恒等式. 因此可取坐标系 $r _ { 1 } , . . . , r _ { N }$ 使得 $e _ { 1 } , . . . , e _ { N }$ 为该坐标系的坐标曲线的切向量. 此坐标 $r _ { 1 } , . . . , r _ { N }$ 正是我们所求黎曼不变量. □

# 附录 2. 正交曲线坐标系与可积系统

前文已说, 正交曲线坐标系确定了可积的流体力学型哈密顿系统. 为寻找这种坐标系, 我们需要求解非常复杂的非线性偏微分方程组

$$
R _ { i j k l } = 0 .
$$

这里的 $R _ { i j k l } = R _ { i j k l } ( h , { \frac { \partial h } { \partial u _ { i } } } , { \frac { \partial ^ { 2 } h } { \partial u _ { i } \partial u _ { j } } } )$ , $h = ( h _ { 1 } , . . . , h _ { N } ) = h ( u )$ , 是对角度量

$$
\mathrm { d } s ^ { 2 } = \sum _ { i = 1 } ^ { N } \varepsilon _ { i } h _ { i } ^ { 2 } ( u ) \mathrm { d } u _ { i } ^ { 2 } , \quad \varepsilon _ { i } = \pm 1
$$

的黎曼曲率张量. 系统(2.22),(2.23) 的解的自由度被 E.Cartan[29] 所求得 [正如我们之前所说, 上述系统的解可被任意 $N ( N + 1 ) / 2$ 个二元函数所确定] . 一般来说, 当 $N \geq 3$ 时方程组 (2.22),(2.23)不一定可积. 但存在一类特殊的对角度量使得该系统可积 [42].这一类特殊的对角度量由 Darboux[43] 提出, 被 Egoroff 所研究 [44]. Darboux 将这种正交曲线坐标系称为 Egoroff 坐标系. 对于度量(2.23), 如果它的 旋转系数 (rotationcoefficient)

$$
\gamma _ { i j } = \partial _ { j } h _ { i } / h _ { j } , \quad i \neq j
$$

[其中 $\partial _ { j } \equiv \frac { \partial } { \partial u _ { j } } ]$ 满足对称性条件

$$
\gamma _ { j i } = \varepsilon _ { i } \varepsilon _ { j } \gamma _ { i j } ,
$$

则称该度量为 Egoroff 度量 (Egoroff metric) . 它还有另一个等价定义: 存在势函数$V = V ( u )$ 使得该度量的对角元 $g _ { i i } : = \varepsilon _ { i } h _ { i } ^ { 2 }$ 满足

$$
g _ { i i } = \partial _ { i } V .
$$

性质. (见 [43]). Egroff 度量(2.23)平坦, 当且仅当旋转系数(2.24)满足下述偏微分 方程:

$$
\partial \gamma _ { i j } = 0 , \quad i \neq j , \quad \partial : = \sum _ { k = 1 } ^ { N } \partial _ { k } .
$$

其证明是直接的.

性质. (见 [42], 也可见 $[ 4 5 ] )$ . 方程组(2.27),(2.28)是可积系统. 它可以表示为下述谱问题的相容性条件 [见后文 2.3 节] , 其中 $\lambda$ 为谱参数:

$$
\partial _ { j } \psi _ { i } = \gamma _ { i j } \psi _ { j } , \quad j \ne i
$$

$$
\partial \psi _ { i } = \lambda \psi _ { i } , \quad i = 1 , . . . , N .
$$

为进一步诠释系统(2.27),(2.28)的结构, 我们将函数 $\gamma _ { i j } ( u )$ 限制在任一给定的平面$u _ { i } = a _ { i } x + b _ { i } t + u _ { i 0 } , i = 1 , . . . , N .$

性质. 矩阵 $\Gamma = ( \gamma _ { i j } ( u ) )$ 在平面 $u _ { i } = a _ { i } x + b _ { i } t + u _ { i 0 }$ 上的限制满足下述非线性$( 1 + 1 )$ -系统:

$$
[ A , \Gamma _ { t } ] - [ B , \Gamma _ { x } ] = [ [ A , \Gamma ] , [ B , \Gamma ] ] ,
$$

其中 $A = \mathrm { d i a g } ( a _ { 1 } , . . . , a _ { N } )$ , $B = \mathrm { d i a g } ( b _ { 1 } , . . . , b _ { N } ) .$ .

系统(2.30)恰为所谓“ $N .$ -波系统”( $N .$ -wave system) 的纯虚约化 (purely imaginaryreduction) [见 [17]] . 我们应注意矩阵 $\Gamma = ( \gamma _ { i j } )$ 具有对称:

$$
\Gamma ^ { T } = J \Gamma J , \quad J = \mathrm { d i a g } ( \varepsilon _ { 1 } , . . . , \varepsilon _ { N } ) .
$$

$\Gamma = ( \gamma _ { i j } )$ 关于变量 $u _ { 1 } , . . . , u _ { N }$ 的独立性由一族与(2.30)交换的流所确定 [这串流可见[46]] .

注意此对角度量的 Lamé 系数 $h _ { 1 } ( u ) , . . . , h _ { N } ( u )$ 可由旋转系数 $\gamma _ { i j }$ 通过(2.29)所恢复:

$$
\partial _ { j } h _ { i } = \gamma _ { i j } h _ { j } , \quad j \neq i .
$$

此系统的解由任意 $N$ 个一元函数所确定. 对于某些合适的 $\gamma _ { i j } ( u )$ [例如, 当 $| u |  \infty$ 时速降] , 方程(2.31)的“好的”解可表示为谱问题 (2.29),(2.29’) 的本征函数的线性组合.

注记 1. 也可对半哈密顿系统谈论上述. 相应对角度量的曲率张量满足如下对角性:

$$
( 1 - \delta _ { i k } \delta _ { j l } ) R _ { i j k l } = 0 , \quad i < j , \quad k < l .
$$

性质. 以下成立:

(1). 若对角度量(2.23)的曲率满足对角性(2.32), 则其旋转系数 $\gamma _ { i j }$ 满足(2.27).

(2). 此系统是可积的; 它可表示为线性问题(2.29)的相容性条件, 或者等价地,可表示为共轭系统

$$
\partial _ { j } \varphi _ { i } = \gamma _ { j i } \varphi _ { j } , \quad i \neq j
$$

的相容性条件.

性质. (续).

(3). 此度量的 Lamé 系数 $h _ { i } ( u )$ 可由旋转系数 $\gamma _ { i j } ( u )$ 通过方程(2.29) (或者(2.31)) 所恢复.

(4). 交换的半哈密顿流 (2.3),(2.10) 的系数 $v ^ { i } ( u )$ 满足方程(2.29), 其中 $\psi _ { i } = $ $h _ { i } v ^ { i }$ , $i = 1 , . . . , N$ . 此系统的守恒律 (2.16) 的密度 $P ( u )$ 满足共轭系统(2.33), 其中$\partial _ { i } P = h _ { i } \varphi _ { i }$ .

其证明是直接的. 若对角度量平坦, 则 (3)(4) 对哈密顿系统也成立.

注记 2. 平坦 Egoroff 度量的平坦坐标 $x _ { 1 } , . . . , x _ { N }$ 可通过求解线性问题(2.33)得到. 确切地说, 设 $\varphi _ { i } ^ { 1 } , . . . , \varphi _ { i } ^ { N }$ 为方程组

$$
\begin{array} { r } { \partial _ { j } \varphi _ { i } = \gamma _ { j i } \varphi _ { i } , \quad i \neq j . } \\ { \partial \varphi _ { i } = 0 } \end{array}
$$

的一组基解, 再设函数 $x _ { 1 } ( u ) , . . . , x _ { N } ( u )$ 满足

$$
\begin{array} { r } { \partial _ { i } x _ { k } = h _ { i } \varphi _ { i } ^ { k } , \quad i , k = 1 , . . . , N . } \end{array}
$$

则度量(2.23)在坐标 $x _ { 1 } , . . . , x _ { N }$ 下为常值.

我们看到, Egoroff 度量的几何问题都能“嵌入”到可积系统理论中. 它们可以通过适当的反散射变换来求解. 如此求解 [用到黎曼-希尔伯特问题的方法] 的例子可见 [42].

例子. 我们具体求解一例 $N = 3$ , 符号 $( \varepsilon _ { 1 } , \varepsilon _ { 2 } , \varepsilon _ { 3 } ) = ( + , - , + )$ 的 Egoroff 度量. 首先我们断言方程(2.27),(2.28)的满足自相似性

$$
\gamma _ { i j } ( k u ) = k ^ { - 1 } \gamma _ { i j } ( u )
$$

的解可由下述常微分方程得到:

$$
\left. \begin{array} { r } { { ( z p _ { 1 } ) ^ { \prime } = - p _ { 2 } p _ { 3 } } } \\ { { p _ { 2 } ^ { \prime } = - p _ { 3 } p _ { 1 } } } \\ { { ( ( z - 1 ) p _ { 3 } ) ^ { \prime } = p _ { 1 } p _ { 2 } } } \end{array} \right\}
$$

其中 $z = ( u _ { 2 } - u _ { 3 } ) / ( u _ { 1 } - u _ { 3 } )$ ,

$$
\begin{array} { r l } & { \gamma _ { 2 3 } = p _ { 1 } ( z ) / ( u _ { 3 } - u _ { 1 } ) , \quad \gamma _ { 3 1 } = - p _ { 2 } ( z ) / ( u _ { 3 } - u _ { 1 } ) } \\ & { \gamma _ { 1 2 } = p _ { 3 } ( z ) / ( u _ { 3 } - u _ { 1 } ) . } \end{array}
$$

利用首次积分

$$
( z p _ { 1 } ) ^ { 2 } - p _ { 2 } ^ { 2 } + [ ( z - 1 ) p _ { 3 } ] ^ { 2 } = R ^ { 2 }
$$

可将(2.36)化为二阶常微分方程; 此二阶常微分方程可以化为 [与参数 $R$ 有关的] Painlevé-VI 方程 [47]. 方程(2.36)的一个非常特殊的显式解可见 [42]. 该解形如

$$
p _ { 1 } = h _ { 1 } / z \sqrt { 2 } , \quad p _ { 2 } = - h _ { 2 } \sqrt { 2 } , \quad p _ { 3 } = - h _ { 3 } / ( z - 1 ) \sqrt { 2 } ,
$$

且相应度量的 Lamé 系数满足

$$
\begin{array} { r l } & { h _ { 1 } = f ( z ) / \sqrt { 2 ( 1 - a z ) } , \quad h _ { 2 } = ( f ( z ) + z - 1 ) / \sqrt { 2 z ( 1 - z ) } , } \\ & { h _ { 3 } = ( f ( z ) - 1 ) / \sqrt { 2 z } , \quad f ( z ) = E ( \sqrt { z } ) / K ( \sqrt { z } ) , } \end{array}
$$

其中 $E , K$ 为完全椭圆积分. (2.38)中的常数 $R = \frac 1 2$ . 其对角度量的哈密顿系统为 KdV方程的椭圆余弦波的慢形变 (slow deformation) 的 Whitham 方程 [见本章后文] , 并且$u _ { 1 } , u _ { 2 } , u _ { 3 }$ 为该方程的黎曼不变量.

$N > 3$ 的 Egoroff 度量的例子可见 [42].

# 2.2 演化系统的不变环

本节我们继续讨论空间一维, 平移不变的演化型偏微分方程组

$$
u _ { t } ^ { i } ( x ) = \{ H , u _ { x } ^ { i } \} , \quad i = 1 , . . . , N ,
$$

假定该方程有足够多的守恒律. 我们设这些守恒律形如

$$
F = \int f ( u , u ^ { \prime } , . . . , u ^ { ( n ) } ) \mathrm { d } x ,
$$

其中 [这些守恒律中至少有一个满足] $n > 0$ . 此外我们还假定(2.41)式右边的守恒律密度

$f$ 是 $u , u ^ { \prime } , \ldots$ 的多项式 [或解析函数] . 上一节提到的泛函 $F$ 的驻点构成的有限维流形$N _ { F }$ 是 $t { \cdot }$ -演化不变的. $N _ { F }$ 当中的函数 $u ( x )$ 满足如下拉格朗日系统:

$$
{ \frac { \delta F } { \delta u ^ { i } ( x ) } } = 0 \Longleftrightarrow { \frac { \partial f } { \partial u ^ { i } } } - \left( { \frac { \partial f } { \partial u ^ { i ^ { \prime } } } } \right) ^ { \prime } + \cdot \cdot \cdot + ( - 1 ) ^ { n } \left( { \frac { \partial f } { \partial u ^ { i ( n ) } } } \right) ^ { ( n ) } = 0 .
$$

在拉格朗日量 $f ( u , u ^ { \prime } , . . . , u ^ { ( n ) } )$ 非退化的假设下, 流形 $N _ { F }$ 的维数是 $2 N n$

有限维流形 $N _ { F }$ 在典范坐标

$$
q _ { j } ^ { i } = u ^ { i ( j - 1 ) } , \quad p _ { i } ^ { j } = \sum _ { k = 0 } ^ { n - j } ( - 1 ) ^ { k } \left( \frac { \partial f } { \partial u ^ { i ( j + k ) } } \right) ^ { ( k ) } ,
$$

$$
i = 1 , . . . , N , \quad j = 1 , . . . , n , \quad u ^ { i ( j ) } \equiv \frac { \mathrm { d } ^ { j } u ^ { i } } { \mathrm { d } x ^ { j } }
$$

下有自然的辛结构:

$$
\{ p _ { i } ^ { j } , q _ { l } ^ { k } \} _ { \cal F } = \delta _ { i } ^ { k } \delta _ { l } ^ { j } , \quad \{ p , p \} _ { \cal F } = \{ q , q \} _ { \cal F } = 0 .
$$

[拉格朗日量 $f ( u , u ^ { \prime } , . . . , u ^ { ( n ) } )$ 称为非退化的, 如果(2.42)所确定的变换

$$
\left\{ u ^ { i ( j ) } \Big | 1 \leq i \leq N , 0 \leq j \leq 2 n - 1 \right\} \mapsto \left\{ q _ { j } ^ { i } , p _ { i } ^ { j } \Big | 1 \leq i \leq N , 1 \leq j \leq n \right\}
$$

可逆. ]

$N _ { F }$ 上的空间平移变换 $u ^ { i } ( x )  u ^ { i } ( x + x _ { 0 } )$ 是哈密顿流, 相应的哈密顿量为

$$
P _ { F } = \sum p _ { i } ^ { j } u ^ { i ( j ) } - f = P _ { F } ( q , p )
$$

[注意我们假定拉格朗日量 $f$ 非退化] .

这表明 $N _ { F }$ 的关于(2.41)的 $t { \cdot }$ -流也是哈密顿流 (Novikov, Bogoyavlensky [35]). 3

引理. 若多项式 [或解析函数] $H _ { F }$ 由下式所确定:

$$
{ \frac { \delta F } { \delta u ^ { i } ( x ) } } u _ { t } ^ { i } \equiv { \frac { \delta F } { \delta u ^ { i } ( x ) } } \{ H , u ^ { i } ( x ) \} = - \partial _ { x } H _ { F }
$$

[这样的 $H _ { F }$ 存在, 因为 $\partial _ { t } F = \int \frac { \delta F } { \delta u ^ { i } ( x ) } u _ { t } ^ { i } ( y ) \mathrm { d } x \equiv 0 \jmath$ . 则 $H _ { F }$ 是 $N _ { F }$ 上的上述$t$ -流关于 $N _ { F }$ 的辛结构(2.42) 的哈密顿量.

设 $G = \int g ( u , u ^ { \prime } , . . . ) \mathrm { d } x$ 为系统(2.41)的另一个局部守恒律, 并且 $\{ G , F \} = 0$ . 则流形 $N _ { F }$ 也关于下述哈密顿系统不变:

$$
u _ { r } ^ { i } ( x ) = \{ G , u ^ { i } ( x ) \} .
$$

根据上述引理, 此流在 $N _ { F }$ 上的限制是 $N _ { F }$ 上的关于哈密顿量 $G _ { F }$ 的哈密顿流, 其中 $G _ { F }$ 可通过类似(2.44)的方式定义:

$$
{ \frac { \delta F } { \delta u ^ { i } ( x ) } } u _ { r } ^ { i } = - \partial _ { x } P _ { F } .
$$

注意 $P _ { F }$ [见公式(2.43)] 可类似定义:

$$
{ \frac { \delta F } { \delta u ^ { i } ( x ) } } u _ { x } ^ { i } = - \partial _ { x } P _ { F } .
$$

引理. 若哈密顿量 $H , G$ 的泊松括号为 0, 则相应的 $H _ { F } , G _ { F }$ 在流形 $N _ { F }$ 上满足

$$
\{ G _ { F } , H _ { F } \} _ { F } = 0 .
$$

推论: $\{ H _ { F } , P _ { F } \} _ { F } = 0$ .

上述两引理描述了在构造 $( 1 + 1 )$ -哈密顿系统的有限维不变流形中的无限维与有限维哈密顿理论之间的关系.

现在假设系统(2.41)有足够多个两两交换的守恒律 $F _ { 0 } , F _ { 1 } , . . . , F _ { M }$ [不妨 $F _ { 0 } = H ]$ .

对任意常数 $c _ { 0 } , c _ { 1 } , . . . , c _ { M }$ , 则有如下有限维不变流形

$$
N _ { c _ { 0 } , \dots , c _ { M } } = \bigg \{ u ( x ) \bigg | \frac { \delta } { \delta u ^ { i } ( x ) } \left[ \sum _ { \alpha = 0 } ^ { M } c _ { \alpha } F _ { \alpha } \right] \bigg \} .
$$

[常数 $c _ { 0 } , . . . , c _ { M }$ 可以适当地单位化, 比如不妨 $c _ { M } = 1 ]$ . 记 $N$ 为所有这些不变流形之并:

$$
N = \bigcup _ { c _ { 0 } , . . . , c _ { M } } N _ { c _ { 0 } , . . . , c _ { M } } .
$$

此流形也关于(2.41)的 $t { \cdot }$ -演化不变. 此时 $N$ 不一定是辛流形, 但依然可以保证是泊松流形: $N$ 上的泊松括号的零化子由常数 $c _ { 0 } , . . . , c _ { M }$ 生成. (2.46)将 $N$ 表示为辛叶的叶状结构.

哈密顿流(2.41)在每个辛叶上的限制仍是哈密顿流, 相应的哈密顿量为

$$
H _ { c } = \sum _ { \alpha = 0 } ^ { M } c _ { \alpha } H _ { \alpha } , \quad \frac { \delta F _ { \alpha } } { \delta u ^ { i } ( x ) } u _ { t } ^ { i } = - \partial _ { x } H _ { \alpha } , \quad c = ( c _ { 0 } , c _ { 1 } , . . . , c _ { M } ) .
$$

此流的积分 (守恒律) 形如

$$
F _ { \alpha , c } = \sum _ { \beta = 0 } ^ { M } c _ { \beta } F _ { \alpha \beta } , \quad \frac { \delta F _ { \alpha } } { \delta u ^ { i } ( x ) } \{ F _ { \beta } , u ^ { i } ( x ) \} = - \partial _ { x } F _ { \alpha \beta } .
$$

$N$ 上的这些函数关于 $N$ 的泊松括号两两交换.

记辛叶 $N _ { c _ { 0 } , \dots , c _ { M } }$ 的维数为 $2 m$ . 若系统(2.41)的守恒律充分多, 则其 $x \cdot$ -流在不变流形 $N$ 上的限制构成一组完备可积系统: 更具体地说, 我们需要让系统(2.41)具有至少 $m - 1$ 个两两交换的守恒律 $F _ { \alpha _ { 2 } } ~ = ~ H$ , $F _ { \alpha _ { 3 } } , . . . , F _ { \alpha _ { m } }$ 使得(2.43)(2.45)中的函数$P _ { c } ( q , p ) , F _ { \alpha _ { i } , c } ( q , p ) , i \ = \ 2 , . . . , m$ 在 $\boldsymbol { c } = ( c _ { 0 } , . . . , c _ { M } )$ 处无关. 若对给定的 $c$ , 它们公共的等值面

$$
P _ { c } ( q , p ) = f _ { 1 } , \quad F _ { \alpha _ { i } } ( q , p ) = f _ { i } , \quad i = 2 , . . . , m
$$

是紧致 [且连通] 的, 则它是环面. 因此演化系统(2.41)的相应的解是关于 $x , t$ 的周期或近似周期函数, 且形如

$$
u ( x , t ) = U ( k x + \omega t + \varphi ^ { 0 } ; c , f ) .
$$

这里的 $U = U ( \varphi ; c , f )$ , $\varphi = ( \varphi _ { 1 } , . . . , \varphi _ { m } )$ 关于每个分量 $\varphi _ { 1 } , . . . , \varphi _ { m }$ 都是 $2 \pi \cdot$ -周期的, 其中

$\varphi _ { 1 } , . . . , \varphi _ { m }$ 是 $c = ( c _ { 0 } , . . . , c _ { M } )$ , $f = ( f _ { 1 } , . . . , f _ { m } )$ 的函数; $\varphi ^ { 0 } = ( \varphi _ { 1 } ^ { 0 } , . . . , \varphi _ { m } ^ { 0 } )$ 为任意常值向量. 波数向量 $k = ( k _ { 1 } , . . . , k _ { m } )$ 与频率向量 $\omega = ( \omega _ { 1 } , . . . , \omega _ { m } )$ 都是 $c , f$ 的函数:

$$
k = k ( c , f ) , \quad \omega = \omega ( c , f ) .
$$

可在环面(2.48)的某邻域定义作用量-角参数 $J _ { a } , \varphi _ { a } , a = 1 , . . . , m$ , 使得

$$
\begin{array} { l } { { P _ { c } = P _ { c } ( J _ { 1 } , . . . , J _ { m } ) , \quad F _ { \alpha _ { i } , c } = F _ { \alpha _ { i } , c } ( J _ { 1 } , . . . , J _ { M } ) , } } \\ { { \displaystyle k _ { a } = \frac { \partial P _ { c } } { \partial J _ { a } } , \quad \omega _ { a } = \frac { \partial H _ { c } } { \partial J _ { a } } , \quad a = 1 , . . . , m . } } \end{array}
$$

例子 1. 非线性 Klein-Gordon 方程. 考虑方程

$$
u _ { t t } - u _ { x x } + V ^ { \prime } ( u ) = 0 .
$$

这是关于 $u , \pi = u _ { t }$ 的哈密顿系统, 其泊松括号为

$$
\{ \pi ( x ) , u ( y ) \} = \delta ( x - y ) ,
$$

哈密顿量为

$$
H = \int \left[ \frac { 1 } { 2 } ( \pi ^ { 2 } + u _ { x } ^ { 2 } ) + V ( u ) \right] \mathrm { d } x .
$$

此系统有两个局部守恒律:

$$
\begin{array} { r c l } { F _ { 1 } } & { = } & { \displaystyle H ( \frac { \sf G E } { \sf E \underline { { { \boxplus } } } } ) , } \\ { F _ { 2 } } & { = } & { \displaystyle \int \pi u _ { x } { \mathrm d } x ( \vec { z } \mathcal { J } ) \frac { \sf E q } { \sf E } ) . } \end{array}
$$

考虑泛函 $F _ { 1 } + c F _ { 2 }$ 的驻点构成的二维流形 $N _ { c } ^ { 2 }$ :

$$
\delta ( F _ { 1 } + c F _ { 2 } ) = 0 \iff \pi + c u _ { x } = 0 , \quad - u _ { x x } + V ^ { \prime } ( u ) - c \pi _ { x } = 0 .
$$

该流形由单行波 $u = u ( x - c t )$ 构成. Legendre 变换(2.42)退化.

尽管如此, 当 $c \neq \pm 1$ 时我们仍能够引入 $N _ { c } ^ { 2 }$ 上的典范坐标

$$
\begin{array} { r } { q = u , \quad p = u _ { x } + c \pi . } \end{array}
$$

系统(2.53)的哈密顿量形如

$$
P _ { c } = { \frac { p ^ { 2 } } { 2 ( 1 - c ^ { 2 } ) } } - V ( q ) .
$$

若势函数 $V ( q )$ 形如下图所述

![](images/6b4292952f0d97bf828ffe5ca82b3ff85b29d4e23e73c2e3895b9b922f587be0.jpg)  
图 2.1

则适当选取 $E$ 可使得等值面

$$
P _ { c } + E = 0
$$

是紧致的 [闭曲线] . 此时相应的周期解

$$
q ( x , t ) = Q ( k x + \omega t + \varphi ^ { 0 } ) ,
$$

$$
Q ( \varphi + 2 \pi ) = Q ( \varphi )
$$

形如

$$
\varphi = \sqrt { \omega ^ { 2 } - k ^ { 2 } } \int \frac { \mathrm { d } Q } { \sqrt { 2 ( E - V ( Q ) ) } } .
$$

其中频率 $\omega$ 与波数 $k$ 是关于 $c , E$ 的函数, 满足如下关系:

$$
\begin{array} { l } { { \omega = \kappa c , } } \\ { { 2 \pi = \sqrt { \omega ^ { 2 } - k ^ { 2 } } \oint \displaystyle \frac { \mathrm { d } Q } { \sqrt { 2 ( E - V ( Q ) ) } } \equiv 2 \sqrt { \omega ^ { 2 } - k ^ { 2 } } \displaystyle \int _ { q _ { \mathrm { m i n } } } ^ { q _ { \mathrm { m a x } } } \displaystyle \frac { \mathrm { d } Q } { \sqrt { 2 ( E - V ( Q ) ) } } , } } \end{array}
$$

上式中, 若 $| c | < 1$ , 则 $q _ { \mathrm { m i n } } = q _ { 1 }$ , $q _ { \mathrm { m a x } } = q _ { 2 }$ ; 当 $| c | > 1$ 时 $q _ { \mathrm { m i n } } = q _ { 2 }$ , $q _ { \mathrm { m a x } } = q _ { 3 }$ [见图2.1] .

方便起见, 引入函数

$$
g ( E ) = { \frac { 1 } { 2 \pi } } \oint \sqrt { 2 ( E - V ( Q ) ) } \mathrm { d } Q .
$$

则有

$$
k = { \frac { 1 } { \sqrt { c ^ { 1 } - 1 } g _ { E } } } , \quad \omega = - k c .
$$

[与(2.55)的 $\varphi$ 相对应的] 作用量 $J$ 形如

$$
J = { \frac { 1 } { 2 \pi } } \oint p \mathrm { d } q = - { \sqrt { c ^ { 2 } - 1 } } g ( E ) .
$$

这些公式给出了系统(2.50)的由周期解构成的三维不变流形.

例子 2. 广义 $K d V$ 方程. 考虑方程

$$
u _ { t } + V ^ { \prime \prime } ( u ) u _ { x } - u _ { x x x } = 0 ,
$$

其泊松括号为

$$
\{ u ( x ) , u ( y ) \} = \delta ^ { \prime } ( x - y ) ,
$$

相应的哈密顿量为

$$
H = \int \left[ { \frac { 1 } { 2 } } u _ { x } ^ { 2 } + V ( u ) \right] { \mathrm { d } } x .
$$

此系统具有以下三个守恒律:

$$
\begin{array} { r c l } { F _ { 2 } } & { = } & { \displaystyle H \left( \frac { \varkappa \Xi \Xi } { \sharp \Xi \Xi } \right) } \\ { F _ { 1 } } & { = } & { \displaystyle \int \frac { u ^ { 2 } } { 2 } \mathrm { d } x \left( \vec { \mathfrak { x } } { \mathfrak { J } } _ { \Xi } ^ { \boxplus } \right) } \\ { F _ { 0 } } & { = } & { \displaystyle \int u \mathrm { d } x \left( \breve { \mathfrak { x } } { \mathfrak { J } } _ { \Xi } ^ { \boxplus } \not \Sigma _ { \textsc { h } } ^ { \boxplus } \right) } \end{array}
$$

泛函

$$
F _ { c , d } = F _ { 2 } + c F _ { 1 } + d F _ { 0 }
$$

的驻点构成的二维流形形如

$$
- u _ { x x } + V ^ { \prime } ( u ) + c u + d = 0 .
$$

其中的函数只有单行波. (2.64)的解形如

$$
u ( x , t ) = U ( k x + \omega t + \varphi ^ { 0 } ) , \quad U ( \varphi + 2 \pi ) = U ( \varphi ) ,
$$

$$
\begin{array} { l } { { \varphi } } \end{array} = \begin{array} { l } { { \displaystyle k \int \frac { \mathrm { d } U } { \sqrt { 2 ( V ( U ) + \frac { c } { 2 } U ^ { 2 } + d U + E ) } } , } } \\ { { \displaystyle k } } \end{array}
$$

其中

$$
g = g ( c , d , E ) = \frac { 1 } { 2 \pi } \oint \sqrt { 2 ( V ( U ) + \frac { c } { 2 } U ^ { 2 } + d U + E ) } \mathrm { d } U .
$$

其作用量-角参数为 $J , \varphi$ , 其中

$$
J = g / g _ { E } .
$$

在本例, 我们得到由周期解构成的四维不变流形 [一维不变环的三维族] .

例子 3. 广义非线性薛定谔方程. 考虑方程

$$
i \psi _ { t } = - \psi _ { x x } + V ^ { \prime } ( | \psi | ^ { 2 } ) \psi .
$$

这是哈密顿系统, 其泊松括号为

$$
\{ \psi ( x ) , \psi ^ { * } ( y ) \} = i \delta ( x - y ) ,
$$

相应的哈密顿量为

$$
H = \int [ \psi _ { x } \psi _ { x } ^ { * } + V ( \psi \psi ^ { * } ) ] \mathrm { d } x .
$$

这里的 $\psi , \psi ^ { * }$ 应该被视为两个独立分量. [对于任意的“势函数 ${ } ^ { \mathfrak { N } } ]$ , 方程(2.67)还有另外两个守恒律

$$
F _ { 1 } = \int \psi \psi ^ { * } \mathrm { d } x , \quad F _ { 2 } = \int \frac { \psi ^ { * } \psi _ { x } - \psi \psi _ { x } ^ { * } } { 2 i } \mathrm { d } x .
$$

由泛函 $H + c _ { 1 } F _ { 1 } + c _ { 2 } F _ { 2 }$ 的驻点构成的四维流形 $N _ { c }$ 中的函数满足

$$
- \psi _ { x x } + V ^ { \prime } ( | \psi | ^ { 2 } ) \psi + c _ { 1 } \psi + \frac { c _ { 2 } } { i } \psi _ { x } = 0 .
$$

$N _ { c }$ 上的典范坐标为

$$
\psi , \quad p _ { \psi } = \psi _ { x } ^ { * } + \frac { c _ { 2 } } { 2 i } \psi ^ { * } , \quad \psi ^ { * } , \quad p _ { \psi ^ { * } } = \psi _ { x } - \frac { c _ { 2 } } { 2 i } \psi .
$$

方程(2.70)是流形 $N _ { c }$ 上的哈密顿系统, 其哈密顿量为

$$
P _ { c } = p _ { \psi } p _ { \psi } ^ { * } - V ( \psi \psi ^ { * } ) + \psi \psi ^ { * } \left( { \frac { c _ { 2 } ^ { 2 } } { 4 } } - c _ { 1 } \right) + { \frac { c _ { 2 } } { 2 i } } ( \psi p _ { \psi } - \psi ^ { * } p _ { \psi ^ { * } } ) .
$$

该系统具有额外的首次积分

$$
F _ { 1 c } = \frac { 1 } { i } ( \psi p _ { \psi } - \psi ^ { * } p _ { \psi ^ { * } } ) .
$$

于是我们得到自由度为 2 的可积系统. 为显式写出等值面

$$
P _ { c } = E , \quad F _ { 1 c } = - 2 f ,
$$

我们引入极坐标系

$$
\psi = r e ^ { i \varphi } , \quad \psi ^ { * } = r e ^ { - i \varphi } .
$$

则有

$$
\varphi _ { x } = \frac { f } { r ^ { 2 } } , \quad r _ { x } ^ { 2 } = E + V ( r ^ { 2 } ) + ( c _ { 1 } - c _ { 2 } ^ { 2 } ) r ^ { 2 } - \frac { f ^ { 2 } } { r ^ { 2 } } + 2 f c _ { 2 } .
$$

假设集合 $\Big \{ r \Big | \overline { { E } } + V ( r ^ { 2 } ) + c r ^ { 2 } - \frac { f ^ { 2 } } { r ^ { 2 } } \geq 0 \Big \}$ 具有紧连通分支 [其中 $c = c _ { 1 } - c _ { 2 } ^ { 2 }$ ,${ \overline { { E } } } = E + 2 f c _ { 2 } ]$ . 则相应的近似周期解

$$
\psi ( x , t ) = \Psi ( k _ { 1 } x + \omega _ { 1 } t + \tau _ { 1 } ^ { 0 } , k _ { 2 } x + \omega _ { 2 } t + \tau _ { 2 } ^ { 0 } ; c , \overline { { { E } } } , f )
$$

形如

$$
r = | \psi | = R ( k _ { 1 } x + \varphi _ { 1 } ^ { 0 } ) , \quad R ( \varphi _ { 1 } + 2 \pi ) = R ( \varphi _ { 1 } )
$$

$$
\varphi _ { 1 } = k _ { 1 } \int \frac { \mathrm { d } R } { \sqrt { \overline { { E } } + V ( R ^ { 2 } ) + c R ^ { 2 } - \frac { f ^ { 2 } } { R ^ { 2 } } } } ,
$$

$$
\begin{array} { r c l } { \varphi } & { = } & { \arg \psi = \displaystyle \frac { f } { k _ { 1 } } \Phi ( k _ { 1 } x + \varphi _ { 1 } ^ { 0 } ) + k _ { 2 } x + \omega _ { 2 } t , } \\ { \Phi ( \tau ) } & { = } & { \displaystyle \int \left[ \frac { 1 } { R ^ { 2 } ( \tau ) } - \frac { k _ { 2 } } { f } \right] \mathrm { d } \tau , } \\ { k _ { 1 } } & { = } & { \displaystyle 1 / g _ { E } , \quad \omega _ { 1 } = 0 , \quad k _ { 2 } = - g _ { f } - c _ { 2 } , \quad \omega _ { 2 } = c _ { 1 } , } \\ { g } & { = } & { \displaystyle g ( E , c , f ) = \frac { 1 } { 2 \pi } \oint \sqrt { E + V ( R ^ { 2 } ) + c R ^ { 2 } - \frac { f ^ { 2 } } { R ^ { 2 } } } \mathrm { d } R . } \end{array}
$$

在本例, 我们得到系统(2.67)的一个六维不变流形, 它被表示成二维不变环面的四维族. 作为基础练习, 请读者自行求解关于角参数 $\varphi _ { 1 } , \varphi _ { 2 }$ 的作用量 $J _ { 1 } , J _ { 2 }$ [这里的 $\varphi _ { 1 }$ 见(2.74), $\varphi _ { 2 } = \arg \psi - \frac { f } { k _ { 1 } } \Phi ( \varphi _ { 1 } )$

# 2.3 交换表示, 守恒律与演化系统的哈密顿理论

之前几节的例子都非常基本. 我们只考虑了这些演化系统的“显然的”守恒律 [例如能量, 动量...] . 确定相应的有限维不变流形的常微分方程是单自由度哈密顿系统 [或者可分离变量的二自由度系统] .

于是, 关于演化方程的“可积性理论”的两个自然的问题如下:

1. 寻找具有充分多“非平凡”守恒律的演化系统;2. 定义演化系统的有限维不变流形的完全可积常微分方程是否具有某些奇特的性质? 如何积分这种常微分方程, 并高效地寻找相应的作用量-角参数?

众所周知, 孤子 (soliton) 理论中的演化系统 [比如 Korteweg-de Vires 方程] 具有无穷多守恒律. 对这个现象的最自然解释可见 Lax[37]. 他发现了 KdV 方程

$$
u _ { t } + 6 u u _ { x } - u _ { x x x } = 0
$$

的形如

$$
L _ { t } = [ A , L ]
$$

的 交换表示 (commutative representation) , 其中

$$
L = - \partial _ { x } ^ { 2 } + u , \quad A = 4 \partial _ { x } ^ { 3 } - 6 u \partial _ { x } - 3 u _ { x } , \quad \left[ A , L \right] = A L - L A .
$$

算子方程 $L _ { t } = [ A , L ]$ 等价于 KdV 方程. 于是 $L$ 的谱特征给出了 KdV 方程的守恒律.Shabat, Ibragimov, Mikhailov, Sokolov 等人 [38-40] 在可积偏微分方程的分类的研究中证明了, 在一些附加的假设下相反的陈述似乎也成立: 如果 $( 1 + 1 )$ -系统具有充分多的高阶守恒律, 则其存在一些特定类型的交换表示 [也就是说, 它是孤子理论中的可积系统]. 至少我们对某些演化系统证明了此结果 [作为分类定理的推论] . 于是, 对第一个问题的靠谱回答是: 具有充分多 [高阶] 守恒律的演化系统具有交换表示.

因此从这一点出发, 我们只考虑具有交换表示的演化系统 [要把 KdV 方程作为主要例子牢记于心] . 我们也将看到, 交换表示也是回答第二个问题的关键. 在下一节我将解释为什么对于孤子理论中的可积系统, 求解不变环以及相应的作用量-角参数的代数几何方法为何非常有用. 而在本节, 我将回顾 KdV 方程的 [适当形式的] 守恒律的构造,以及 KdV 方程簇 (hierarchy) 及其哈密顿理论的构造.

将交换表示(2.76)写成下述 [15] 形式会更方便:

$$
[ \partial _ { x } - U ( \lambda ) , \partial _ { t } - V ( \lambda ) ] = 0 \iff U _ { t } ( \lambda ) - V _ { x } ( \lambda ) + [ U ( \lambda ) , V ( \lambda ) ] = 0
$$

(“零曲率表示 (zero-curvature representation) ”). 这里的 ${ \mathcal { L } } = \partial _ { x } - U ( \lambda )$ 为薛定谔算子 $L - \lambda$ 的矩阵形式 [其中 $\lambda$ 为 谱参数 (spectral parameter) ] :

$$
\mathcal { L } = \partial _ { x } - U ( \lambda ) = \partial _ { x } - \left( \begin{array} { c c } { 0 } & { 1 } \\ { u - \lambda } & { 0 } \end{array} \right) ,
$$

$$
[ \partial _ { x } - U ( \lambda ) ] \binom { \psi _ { 1 } } { \psi _ { 2 } } = 0 \Longleftrightarrow \psi _ { 1 } = \psi , \psi _ { 2 } = \psi ^ { \prime } , L \psi = \lambda \psi .
$$

并且矩阵 $V ( \lambda )$ 为方程(2.78a)的解空间上的 $A \cdot$ -算子的矩阵形式:

$$
V ( \lambda ) ( \begin{array} { c } { { \psi } } \\ { { \psi ^ { \prime } } } \end{array} ) = ( \begin{array} { c } { { A \psi } } \\ { { ( A \psi ) ^ { \prime } } } \end{array} ) \quad ( \begin{array} { c }  { \mathrm { m o d } [ \partial _ { x } - U ( \lambda ) ] ( \begin{array} { c } { { \psi } } \\ { { \psi ^ { \prime } } } \end{array} ) = 0 . ) } \end{array}
$$