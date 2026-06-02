# 第13章 Kerr-Newman(克尔-纽曼)黑洞

本章介绍相对论天体物理学中异常重要的 Kerr-Newman(KN)度规.这是一个3参数度规族,参数 $M , J$ 及 $Q$ 可分别解释为星体的质量、角动量及电荷,当 $J = 0$ 时退化为Reissner-Nordstrom(RN)度规.由于RN度规同KN度规有不少共性,又比后者简单得多,我们在第一节先介绍RN 黑洞.

# \$ 13.1 Reissner-Nordstrom(RN)黑洞

$\ S 8 . 4$ 曾导出RN度规

$$
\mathtt { d } s ^ { 2 } = - \left( 1 - { \frac { 2 M } { r } } + { \frac { Q ^ { 2 } } { r ^ { 2 } } } \right) \mathtt { d } t ^ { 2 } + \left( 1 - { \frac { 2 M } { r } } + { \frac { Q ^ { 2 } } { r ^ { 2 } } } \right) ^ { - 1 } \mathtt { d } r ^ { 2 } + r ^ { 2 } ( \mathtt { d } \theta ^ { 2 } + \sin ^ { 2 } \theta \mathtt { d } \varphi ^ { 2 } ) ,
$$

它描述静态球对称带电星体的外部几何.由于星体内部并非电磁真空,RN 解对星体内部不适用.然而，同施瓦西解的讨论类似,我们仍对下述问题感兴趣：若RN 解对所有 $r > 0$ 值都成立，时空的情况如何？首先，因为 $r$ 出现于分母中， $r = 0$ 是线元(13-1-1)的奇点.计算表明RN度规是类时测地完备而类光测地不完备的,那些不完备类光测地线(只能是径向的)都伸向 $r = 0$ (而且趋近 $r = 0$ 时存在 s.p.曲率奇性),因此 $r = 0$ 按定义是时空奇性.其次，若函数 $f ( r ) \equiv 1 - 2 M / r + Q ^ { 2 } / r ^ { 2 }$ 有零点，则线元(13-1-1)还有其他奇性.能使 $f ( r )$ 为零的 $r$ 值满足

$$
r _ { \pm } = M \pm \sqrt { M ^ { 2 } - Q ^ { 2 } } \ ,
$$

所以应分三种情况讨论. $\textcircled{1}$ 若 $M ^ { 2 } { < } Q ^ { 2 }$ ，则 $f ( r )$ 无(实)零点,这种 RN 时空只有一个奇性,即时空奇性 $r = 0$ . $\textcircled{2}$ 若 $M ^ { 2 } { > } Q ^ { 2 }$ ，则除 $r = 0$ 外还有 $r = r _ { + }$ 和 $r = r _ { - }$ 两个奇性.同施瓦西解类似,它们也是坐标奇性(证明见选读13-1-2). $\textcircled{3}$ 若 $M ^ { 2 } = Q ^ { 2 }$ ，上述两个奇性合而为一.

实际星体常有 $M ^ { 2 } \gg Q ^ { 2 }$ ，因此我们只讨论 $M ^ { 2 } { > } Q ^ { 2 }$ 的情况.函数 $f ( r )$ 有两个零点使Reissner-Nordstrom时空的延拓比施瓦西时空更为复杂.图13-1是由计算和讨论(详见选读13-1-2)所得到的Reissner-Nordstrom最大延拓时空的Penrose图,[只适用于 $M ^ { 2 } { > } Q ^ { 2 }$ ,其他两种情况的Penrose 图见Hawking and Ellis(1973)图26.]它可看作由一个单元出发沿竖直方向无限重复的结果.无限重复是为保证除到达时空奇点 $r = 0$ 的测地线外所有测地线的完备性．看图时应充分利用Penrose图的优越性——(球对称的)类光超曲面和径向类光测地线表现为 $4 5 ^ { \circ }$ 斜直线.我们从图中标出的那个单元开始介绍.该单元含有三种不同类型的时空区,称为I,II,III型区.I型区满足 $r > r _ { + }$ ， $\mathbf { I I }$ 型区满足 $r _ { - } < r < r _ { + }$ ,III型区满足 $0 < r < r _ { - } . \mathrm { ~ I ~ }$ 型区和III型区都有$g _ { a b } ( \partial / \partial t ) ^ { a } ( \partial / \partial t ) ^ { b } \equiv g _ { 0 0 } < 0$ ,即 Killing矢量场 $( \partial / \partial t ) ^ { a }$ 类时，故为稳态区.反之,Ⅱ型区有 $g _ { 0 0 } > 0$ ,即 Killing矢量场类空.由于不存在类时 Killing矢量场,II型区不是稳态区.每个III型区都有时空奇性 $r = 0$ .与施瓦西奇性不同,RN 奇性是类时的.(在Penrose 图中为一竖直线,与超曲面类比可知为类时.然而奇点不属于时空流形,时空度规 ${ g } _ { a b }$ 在奇性处无定义,严格说对奇性的类时性应另给定义.可参见 $\ S \mathrm { E } . 3$ 之末.）I型区与施瓦西最大延拓时空(图12-9)的A和 $\mathbf { A ^ { \prime } }$ 区十分类似(也是渐近平直区),也有自己的共形无限远 $\mathcal { I } ^ { \pm } , i ^ { \pm } , i ^ { 0 }$ ,并在代表 $r = r _ { + }$ 的斜直线(类光超曲面)处与 ⅡI 型区相毗邻.I型区中的任一观者(指向未来类时线)一旦穿过 $r = r _ { + }$ 面进入ⅡI型区就再也不能回到原来的I型区，因此这个面类似于施瓦西时空的 $r = 2 M$ 面,称为I型区的事件视界(于是 $M ^ { 2 } > Q ^ { 2 }$ 的 RN 时空含有黑洞).由于RN奇性的类时性,观者进入ⅡI 型区后有丰富得多的选择性.对于施瓦西时空中开着飞船进入黑洞区B 的观者,无论他让飞船熄火(因而走测地线)还是开足马力，总躲不过掉入奇点$r = 0$ 的结局.反之,计算表明,RN 时空中到达奇性 $r = 0$ 的类时线必定不是测地线[但存在到达 $r = 0$ 的类光测地线,例如图中的 $\eta ( \lambda ) . ]$ 因此从I型区进入ⅡI型区的观者如果让飞船熄火就一定不会触及奇性,在穿越II型区并进入III型区后[图中的$\gamma ( \tau )$ ]将安全进入下个ⅡI型区(并将穿过 $r = r _ { + }$ 而从下个I型区冒出来).或者,从I型区进入ⅡI型区的观者也可开动发动机从而沿类时非测地线[图中的 $G ( \tau ) ]$ 穿越ⅡI型区进入II型区,并在不触及奇性的情况下进入下个II型区和I型区.读者自然要问：如果愿意,他是否也可借助发动机选择类时非测地线到达奇性并终结其在时空中的存在?答案是出乎意料地否定的.并非不存在到达奇性的类时非测地线，而是原则上不存在任何观者，他能沿这种线到达 $r = 0$ .这是由 Chakrabarti,Geroch,andLiang(1983)指出的,该文要点如下：类时测地线和类时非测地线的表现很不相同,例如,闵氏时空存在着起于 $\mathcal { I } ^ { - }$ 或止于 ${ \mathcal { I } } ^ { + }$ 的类时非测地线,却不存在起于 $\mathcal { I } ^ { - }$ 或止于 ${ \mathcal { I } } ^ { + }$ 的类时测地线(见命题12-2-1);RN 时空存在着到达奇性的类时非测地线,却不存在到达奇性的类时测地线,等等.由于类时测地线代表自由下落质点而类时非测地线代表非自由下落质点,RN 时空存在到达奇点的类时非测地线一事似乎表明至少有些观者可以借助飞船到达奇点,然而问题并非如此简单.任一飞船的燃料总是有限的,它不能经历任意的类时非测地线.在这个意义上说,类时非测地线又可分为两个子类：物理上可经历的和物理上不可经历的.该文证明物理上可经历的类时非测地线的充要条件是该线的4 加速的长度 $a \equiv ( g _ { a b } A ^ { a } A ^ { b } ) ^ { 1 / 2 }$ 沿线的积分$\int a \mathbf { d } \tau$ 为有限值( $\tau$ 为固有时),并进一步证明： $\textcircled{1}$ 所有到达 RN 奇点的类时非测地线的 $\int a \mathbf { d } \tau$ 都无限； $\textcircled{2}$ 所有到达闵氏时空(以及任意渐近平直时空)的 ${ \mathcal { I } } ^ { + }$ 的类时非测地线的 $\int a \mathbf { d } \tau$ 都无限.由此可得结论:RN时空的奇点和渐近平直时空的未来类光无限远都是物理上不可到达的.

![](images/061d860a5b4b77cddf22005759edccfd8cde4d9c8a44d411eb2e191fb0f00661.jpg)  
图13-1 $M ^ { 2 } > Q ^ { 2 }$ 的 RN 最大延拓时空的 Penrose 图(上下可无限延伸).左、下方 $\mathbf { I } , \mathbf { I I }$ 型区内的实、虚线分别代表等 $r$ 线和等 $t$ 线

RN 奇性的类时性表明 RN 最大延拓时空不是整体双曲的：它没有柯西面（见 $\ S 1 1 . 5 )$ .从一定意义上说,最有可能成为柯西面的要算是图13-1中的水平面 $S$ ，然而由图可见它只是由它所在的两个I型区和两个相邻II型区组成的子时空(斜置正方形)的柯西面.斜置正方形与 III 型区的边界 $r = r _ { - }$ 就是 $S$ 的柯西视界(\$11.5),某些文献称之为内视界(inner horizon).这一柯西视界的存在给物理学家带来严重问题：物理可预言性在柯西视界以外的时空区域(暂且简称界外区)将被破坏殆尽， $S$ 面上的全部初始条件不足以预言界外区将会发生什么，从类时奇性所在处可能发出的信号(例如定时炸弹)使界外区随时随地可能发生无从预料的任何物理事件.此外,这一柯西视界的特点还导致它的严重不稳定性,在微扰下 RN 黑洞内的几何情况将与图13-1非常不同,详见选读13-1-1.

![](images/321cca6f7b814202451a4e63d5a94317c153e1468eed288844d666af1935a2aa.jpg)  
图13-2观者 $G$ 在跨越柯西视界 $r = r _ { - }$ 前无论多么短的时间内都能看到K区的全部“未来历史”

[选读13-1-1]

与最大延拓的施瓦西时空(图9-13)类似,最大延拓的RN 时空(图13-1)也不大可能是物理上真实的时空.然而,图13-1的一部分在讨论球对称带电星体晚期坍缩成 RN 黑洞时有重要意义:坍缩星的外部几何仍由RN 度规描述.(图13-2,其中K区代表坍缩星外及事件视界 $r = r _ { + }$ 以外的时空区.）注意到尺度在 ${ \mathcal { I } } ^ { + }$ 处作过无限大的压缩，便会发现柯西视界( ${ \bf \nabla } ( r = r _ { - }$ )十分异乎寻常.设观者 $G$ 的世界线与柯西视界交于 $p$ ，线的一小段 $q p$ 的固有时间为 $\Delta \tau .$ 过 $q$ 作与 ${ \mathcal { I } } ^ { + }$ 平行的直线,便可定出 K区的一个子集 $\mathbf { K } _ { \mathrm { F } }$ (图中的暗灰细长方形). $\Delta \tau$ 越小则 $\mathtt { K } _ { \mathtt { F } }$ 越“窄”，但其内部各事件都在 ${ \mathcal { I } } ^ { + }$ 附近,所以 $\mathbf { K }$ 区中任一观者 $\widetilde { G }$ 的世界线与 $\mathbf { K } _ { \mathrm { F } }$ 的相交段都包含着 $\widetilde { G }$ 的全部“未来历史”(对应于无限长固有时间),可见 $G$ 在到达柯西视界前无论多么短的一段时间内总能看到 $\mathbf { K }$ 区的全部未来历史.柯西视界的一个更为特别的问题则是由“无限蓝移”所导致的不稳定性.人们更关 $\aleph ^ { \bullet }$ 的是旋转星体(非球对称)的晚期坍缩,其最终形成的稳态黑洞不是RN黑洞而是Kerr-Newman黑洞(见 $\ S 1 3 . 6 )$ .与这种坍缩相伴随的引力波在柯西视界将出现无限蓝移并使之变得不稳定.由于非球对称坍缩非常复杂,又由于人们相信Kerr-Newman 黑洞与RN 黑洞在因果结构和视界结构上非常类似,所以,作为研究非球对称坍缩的第一步(突破口),人们曾研究过如下的理想化模型：星外时空由经受微扰的“RN度规”描写,这微扰来自交叉流动的入射和出射光子流(或静质量为零的其他粒子流).为了帮助读者理解光子流的无限蓝移,我们以球对称坍缩星(外部为RN度规)为例作一粗略说明(图13-2).设 $\mathbf { K }$ 区中的观者 $\widetilde { G }$ 向 $G$ 发光，由于尺度在 ${ \mathcal { I } } ^ { + }$ 处的无限压缩， $\widetilde { G }$ 世界线限于 $\mathbf { K } _ { \mathbf { F } }$ 内的一段对应于无限大的固有时间.这段时间内所发的无限多个波峰只能挤在 $G$ 线的有限长度 $q p$ 段内，可见 $G$ 收到的光的周期在趋于 $p$ 时趋于零,相应于无限蓝移.这一异常表现导致柯西视界的高度不稳定性：微弱的入射波(向左)在柯西视界附近的频率(因而能量)无限增大[称为质量暴涨(mass inflation)],使柯西视界很可能成为新的曲率奇性所在处.可见原本类时的RN奇性是不稳定的，它在微扰下很可能变得类光(甚至类空).观者 $G$ 在与柯西视界相交前的一瞬间，在看到他曾经生活于其中的“宇宙”(指K区)的全部未来历史在眼前闪过之后落入这一新奇点.Poisson andIsrael(1990)写道：“柯西视界是一堵终极性的砖墙，时空演化至此被迫终止.”RN黑洞的事件视界以内的时空几何因而变得面目全非，然而K区(即坍缩星外和事件视界外)的观者则对此毫无察觉,在他们看来，时空几何仍由静态RN度规描述. [选读13-1-1完]

[选读13-1-2]

本选读介绍 $M ^ { 2 } > Q ^ { 2 }$ 的 RN 时空最大延拓(图13-1)的获得.RN线元(13-1-1)的前2维可表为

$$
\begin{array} { r c l } { { } } & { { } } & { { \mathrm { d } \hat { s } ^ { 2 } = - f ( r ) \mathrm { d } t ^ { 2 } + f ( r ) ^ { - 1 } \mathrm { d } r ^ { 2 } = f ( r ) [ - \mathrm { d } t ^ { 2 } + f ( r ) ^ { - 2 } \mathrm { d } r ^ { 2 } ] } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { = f ( r ) ( - \mathrm { d } t ^ { 2 } + \mathrm { d } r _ { * } ^ { \ 2 } ) ~ , } } \end{array}
$$

其中乌龟坐标 $r _ { * }$ 由下式定义：·

$$
\frac { \mathrm { d } r _ { * } } { \mathrm { d } r } = f ( r ) ^ { - 1 } = \left( 1 - \frac { 2 M } { r } + \frac { Q ^ { 2 } } { r ^ { 2 } } \right) ^ { - 1 } .
$$

积分上式得

$$
r _ { * } ( r ) = r + C + \frac { 1 } { 2 \beta } \mathrm { l n } \frac { \vert r - r _ { + } \vert } { 2 M } - \frac { \alpha } { 2 \beta } \mathrm { l n } \frac { \vert r - r _ { - } \vert } { 2 M } ,
$$

其中 $C$ 为积分常数， $\beta \equiv ( r _ { + } - r _ { - } ) / 2 { r _ { + } } ^ { 2 }$ ， $\alpha \equiv ( r _ { - } / r _ { + } ) ^ { 2 }$ .易见 $\beta > 0$ 和 $1 > \alpha > 0$ .由式(13-1-5)可知函数 $r _ { * } ( r )$ 在 $r$ 从0增至 $\infty$ 时有以下表现：在 $r \in [ 0 , r _ { - } )$ 段内从某值$r _ { * } ( 0 )$ 单调增至 $+ \infty$ ；在 $r \in \left( r _ { - } , r _ { + } \right)$ 段内从 $+ \infty$ 单调减至 $- \infty$ ；在 $r \in \left( r _ { + } , \infty \right)$ 段内从 $- \infty$ 单调增至 $+ \infty$ .选积分常数 $C$ 使 $r _ { * } ( 0 ) = 0$ .把 $f ( r ) = r ^ { - 2 } ( r - r _ { + } ) ( r - r _ { - } )$ 代入式(13-1-3)得

$$
\begin{array} { r } { \mathtt { d } \hat { s } ^ { 2 } = r ^ { - 2 } ( r - r _ { + } ) ( r - r _ { - } ) ( - \mathtt { d } t ^ { 2 } + \mathtt { d } r _ { * } ^ { \ 2 } ) , } \end{array}
$$

可见 $\mathrm { d } \hat { s } ^ { 2 }$ 在 $r = r _ { + }$ 及 $r = r _ { - }$ 处奇异(退化),因而暂时把三种类型的区域作为互不连通的流形讨论.取定一个I型区作为延拓的出发区,并称之为A区.仿照施瓦西时空的做法,在A区定义新坐标 $V , U$ ：

$$
V = { \bf e } ^ { \beta ( r _ { * } + t ) } , U = - { \bf e } ^ { \beta ( r _ { * } - t ) } , ( \ddagger { \bf A } \boxtimes \overrightarrow { \mathcal { A } } \infty > V > 0 , 0 > U > - \infty )
$$

则线元(13-1-6)改写为

$$
\begin{array} { r } { \begin{array} { r } { \mathbf { d } \hat { s } ^ { 2 } = - \beta ^ { - 2 } ( 2 M ) ^ { 1 - \alpha } r ^ { - 2 } ( r - r _ { - } ) ^ { 1 + \alpha } \mathbf { e } ^ { - 2 \beta ( r + C ) } \mathbf { d } V \mathbf { d } U , } \end{array} } \end{array}
$$

上式在 $r = r _ { + }$ 处不再奇异,可见式(13-1-6)的奇性 $r = r _ { + }$ 只是坐标奇性.为便于画图,仿照 $\ S 1 2 . 3$ 用正切函数把施瓦西无限远 $( r = \infty$ )“拉近”的做法，即定义 $V ^ { \prime }$ 和 $U ^ { \prime }$ 使

A区在 $\{ V ^ { \prime } , U ^ { \prime } \}$ 系的形状及各坐标在四条边界线上的数值可提前参见图13-3.既然$r = r _ { + }$ 不再奇异,就可把线元(13-1-8)越过 $b c$ 段和 $c d$ 段延拓出去.暂时只看 $b c$ 段，因其 $U = \mathbf { 0 }$ ，越过它作延拓就是允许 $U$ 的取值范围从 $0 > U > - \infty$ 拓宽至$\infty > U > - \infty$ .在延拓部分仍用式(13-1-9)定义 $V ^ { \prime }$ 和 $U ^ { \prime }$ ，则也可说这延拓是允许 $U ^ { \prime }$ 从 $0 > U ^ { \prime } > - \pi / 2$ 拓宽至 $\pi / 2 > U ^ { \prime } > - \pi / 2$ .于是式(13-1-8)的定义域从A区拓展为

![](images/20251927f2ca830ae5c2beb428222002418aeadd6bb6391ee8a55bda76b4c8f4.jpg)  
图13-3从A区出发越过 $U = 0$ 延拓得AB区

AB区,其定义是

AB区 $\equiv \mathbf { A }$ 区 $\bigcup b c$ 段UB区.(其中 $\mathbf { B }$ 区由图13-3界定)

在B区从 $V , U$ 出发按下式定义 $t , r$ ：

$$
V = { \mathrm e } ^ { \beta ( r _ { * } + t ) } , ~ U = { \mathrm e } ^ { \beta ( r _ { * } - t ) } ,
$$

则B区在 $\{ t , r \}$ 系的线元仍为式(13-1-6),而且从B区边界的 $r$ 值可知 $\mathbf { B }$ 区是个Ⅱ型区.为进一步消除式(13-1-8)中的奇性 $r = r _ { - }$ ，可在 $\mathbf { B }$ 区借 $t , r$ 定义新坐标 $\widetilde { V } , \widetilde { U }$ ：

$\widetilde { V } = - { \bf e } ^ { - \alpha ^ { - 1 } \beta ( r _ { * } + t ) } , \widetilde { U } = - { \bf e } ^ { - \alpha ^ { - 1 } \beta ( r _ { * } - t ) } , ( \ddagger { \bf B } \boxtimes \widetilde { \pmb { \mathbb { H } } } \boldsymbol { 0 } > \widetilde { V } > - \infty , 0 > \widetilde { U } > - \infty )$ (13-1-10a)B区的线元在 $\{ \tilde { V } , \tilde { U } \}$ 系中取如下形式：

$$
\begin{array} { r } { \mathtt { d } \hat { s } ^ { 2 } = - \beta ^ { - 2 } \alpha ^ { 2 } ( 2 M ) ^ { 1 - \alpha ^ { - 1 } } r ^ { - 2 } ( r _ { + } - r ) ^ { 1 + \alpha ^ { - 1 } } \mathtt { e } ^ { 2 \alpha ^ { - 1 } \beta ( r + C ) } \mathtt { d } \widetilde { V } \mathtt { d } \widetilde { U } , } \end{array}
$$

它在 $r = r _ { - }$ 处不再奇异(但却在 $r = r _ { + }$ 奇异.不存在同时消除奇性 $r = r _ { + }$ 和 $r = r _ { - }$ 的坐标系),因而可越过ef段和 $b e$ 段延拓.暂时只看ef段，因其 $\widetilde { U } = 0$ ，越过它作延拓就是允许 $\widetilde { U }$ 的取值范围从 $0 > \widetilde { U } > - \infty$ 拓宽至 $\infty > \widetilde { U } > - \infty$ ,于是式(13-1-11)的定义域从B区拓展为BC区,其定义是

BC区 $\equiv \mathbf { B }$ 区 $\mathsf { U }$ ef段UC区.(其中C区由图 13-4界定)

![](images/2ae617666fd8eb38e1a2af288f795f843d18d8ba022d611b54378eb1d90aa34b.jpg)  
图13-4从B区出发越过 $\widetilde { U } = 0$ 延拓得BC区

在C区从 $\widetilde { V } , \widetilde { U }$ 出发按下式定义 $t , r$ ：

$$
\widetilde V = - { \mathrm e } ^ { - \alpha ^ { - 1 } \beta ( r _ { \ast } + t ) } , \widetilde U = { \mathrm e } ^ { - \alpha ^ { - 1 } \beta ( r _ { \ast } - t ) } ,
$$

则C区在 $\{ t , r \}$ 系的线元仍为式(13-1-6),而且从 $\mathbf { C }$ 区边界的 $r$ 值可知 $\mathbf { C }$ 区是个III

型区.以上为消除坐标奇性 $r = r _ { + }$ 和 $r = r _ { - }$ 而分别引入了坐标系 $\{ V ^ { \prime } , U ^ { \prime } \}$ 和 $\{ \tilde { V } , \tilde { U } \}$ ，两坐标域的交域为B.不难验证两套坐标在B区有如下良好关系：

$$
\cot V ^ { \prime } = \mid \tilde { V } \mid ^ { \alpha } , \cot U ^ { \prime } = \mid \tilde { U } \mid ^ { \alpha } .
$$

既然图13-3,4都含B区,就可把两图粘合而得大区ABC,如图13-5.这还不是最大延拓,因为,例如,任一到达边界fcd的测地线必然不完备,但又没有曲率发散性，暗示着时空还可经 $_ { f c d }$ 向左下方延拓,由此得到大区 $\mathbf { A } ^ { \prime } \mathbf { B } ^ { \prime } \mathbf { C } ^ { \prime }$ ，它也可看作是大区ABC 关于原点做反演的结果(图13-6).这两个大区可粘合为一个单元,再以 $\sqrt { 2 } \pi$ 为步长沿上下方向做无限次平移便得最大延拓,此即图13-1. [选读13-1-2完]

![](images/46aa88de7a6455e598bf00346b4972ae2e7ad91fc92d0a0a14c141e8405892ab.jpg)  
图 13-5图13-3,4粘合成大区ABC,仍可延拓

![](images/d841311e29acbb58824108603015f5cd19897b801e50c4102e167703522264a6.jpg)  
图13-6 大区ABC与 $\mathbf { A B ^ { \prime } C ^ { \prime } }$ 粘成一个单元．再以 $\sqrt { 2 } \pi$ 为步长上下无限平移便得RN最大延拓

# \$13.2 Kerr-Newman(KN)度规

星体或多或少都有转动,其外部时空只有轴对称性而无球对称性,严格说来不能用施瓦西(或 RN)度规描述.Kerr(克尔)在1963 年找到真空爱因斯坦方程的一个稳态轴对称解(后称 Kerr 解),它在物理上描述某种旋转的不带电星球的外部时空几何(把施瓦西解作为角动量为零的特例包括在内).由于几乎所有星球都有自转(其中有些转得飞快),Kerr 度规在黑洞物理中有异乎寻常的重要性(见\$13.6).Newman(纽曼)与合作者于1965 年用复坐标变换的手法有点像变魔术似地从施瓦西度规生出一个解,竟与 Kerr 解一样[生成过程见d'Invermo(1992)19.2].虽然未得新解,但却受到启发.同年稍后,Newman又与多人合作以类似手法从RN解生出一个电磁真空新解,其度规比Kerr度规多一个参数Q(后来发现在物理上可解释为电荷),当 $Q = 0$ 时与Kerr度规无异，后人称之为带电Kerr度规或Kerr-Newman度规(KN 度规),在坐标系 $\{ t , r , \theta , \varphi \}$ (称为 Boyer-Lindquist 系)中的线元为

$$
\begin{array} { r l } & { \mathrel { \phantom { = } } \mathrel { \phantom { = } } \mathstrut \cdot - [ \begin{array} { l } { 1 - \rho ^ { - 2 } ( 2 M r - Q ^ { 2 } ) ] } \ \mathrm { d } t ^ { 2 } + \rho ^ { 2 } A ^ { - 1 } \mathrm { d } r ^ { 2 } + \rho ^ { 2 } \mathrm { d } } \\ {  } \\ { \mathrm { ~ } \mathstrut } \\ { \quad } \end{array} \end{array}
$$

式中

$$
\rho ^ { 2 } ( r , \theta ) \equiv r ^ { 2 } + a ^ { 2 } \cos ^ { 2 } \theta ,
$$

$$
\varDelta ( r ) \equiv r ^ { 2 } - 2 M r + a ^ { 2 } + Q ^ { 2 } ,
$$

其中 $M , a , Q$ 为常实数.式(13-2-1)在 $a = 0$ 时回到 RN 度规；在 $a = Q = 0$ 时回到施瓦西度规.这暗示参数 $M$ 及 $Q$ 可分别解释为星体的质量及电荷(详见选读13-2-1). $Q = 0$ 时的式(13-2-1)就是 $\mathbf { K e r r }$ 度规(见图 13-7).讨论表明(见选读 13-2-1),式(13-2-1)中的 $^ { a }$ 可解释为星体单位质量的角动量.(即 $a = J / M , J$ 为角动量.）因为总可选择 $\varphi$ 坐标的正向使 $a$ 为正,今后将默认 $a > 0$ ·

与Kerr-Newman度规配套的电磁场可用电磁4势表为

$$
A _ { a } = - \rho ^ { - 2 } Q r \left[ \left( \mathrm { d } t \right) _ { a } - a \sin ^ { 2 } \theta ( \mathrm { d } \varphi ) _ { a } \right] .
$$

为便于使用,下面列出 Kerr-Newman 度规及其逆在 Boyer-Lindquist 坐标系的非零分量表达式(其中 $t , r , \theta , \varphi$ 对应于 $x ^ { 0 } , x ^ { 1 } , x ^ { 2 } , x ^ { 3 } )$ ：

![](images/e064c2f7c2172e31bfe8d8ba5e0faf6d803c90367740e3590dc3e46cc914ff96.jpg)  
图13-7几个度规的关系(括号内是所含参量)

$$
\begin{array} { r l } & { g _ { 1 1 } ^ { ( 2 ) } = \rho ^ { 2 } A ^ { 1 } , } \\ & { g _ { 2 2 } ^ { ( 3 ) } , } \\ & { g _ { 3 3 } = \rho ^ { 2 } \frac { 1 } { 2 } , } \\ & { g _ { 2 3 } = \rho ^ { - 2 } [ ( r ^ { 2 } + a ^ { 2 } ) ^ { 2 } - A a ^ { 2 } \sin ^ { 2 } \theta ] \sin ^ { 2 } \theta = [ r ^ { 2 } + a ^ { 2 } + \rho ^ { 2 } a ^ { 2 } ( 2 M r - Q ^ { 2 } ) \sin ^ { 2 } \theta ] \sin ^ { 2 } } \\ & { } \\ & { g _ { 4 0 } = g _ { 4 0 } = - \rho ^ { - 2 } a ( 2 M r - Q ^ { 2 } ) \sin ^ { 2 } \theta \ ; \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad ( 1 3 2 - \rho ^ { 2 } ) } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ &  \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \ \end{array}
$$

由式(13-2-5)求得 $g _ { \mu \nu }$ 的行列式为

$$
g = - \rho ^ { 4 } \sin ^ { 2 } \theta .
$$

证明上式的关键是证明(留作习题)如下的有用公式:

$$
{ g _ { 0 3 } } ^ { 2 } - g _ { 0 0 } g _ { 3 3 } = \varDelta \sin ^ { 2 } \theta .
$$

由式(13-2-5)显见 $\xi ^ { a } \equiv ( \widehat { \partial } / \widehat { \partial } t ) ^ { a }$ 和 $\psi ^ { a } \equiv ( \hat { \partial } / \hat { \partial } \varphi ) ^ { a }$ 是Killing场.此外没有其他独立Killing 矢量场.因星体半径远大于使 $g _ { 0 0 }$ 为零的 $r$ 值,星外有 $g _ { a b } \xi ^ { a } \xi ^ { b } \equiv g _ { 0 0 } < 0$ 和$g _ { a b } \psi ^ { a } \psi ^ { b } \equiv g _ { 3 3 } > 0$ ，表明 $\xi ^ { a }$ 和 $\psi ^ { a }$ 分别是类时和类空Killing场,而且两者对易.可见星外的 KN 时空是稳态轴对称的(见 $\ S 8 . 5 )$ .然而,式(13-2-1)中交叉项 $\mathbf { d } t \mathbf { d } \varphi$ 的系数非零表明 $\xi ^ { a }$ 与等 $t$ 面并不正交. $[ \varphi$ 坐标线躺在等 $t$ 面上， $( \partial / \partial \varphi ) ^ { a }$ 应切于等 $t$ 面，而 $g _ { a b } ( \hat { \partial } / \partial t ) ^ { a } ( \hat { \partial } / \partial \varphi ) ^ { b } = g _ { 0 3 } \neq 0$ 说明 $( \partial / \partial t ) ^ { a }$ 不垂直于 $( \partial / \partial \varphi ) ^ { a }$ ,故不正交于等 $t$ 面.]事实上,可以证明(习题2)类时Killing场 $\xi ^ { a } \equiv ( \widehat { \partial } / \widehat { \partial } t ) ^ { a }$ 为非超曲面正交矢量场,因此$\xi ^ { a }$ 所代表的稳态性并不蕴含静态性.从物理上看,这是因为旋转使时间反演对称性不复存在.(把描写旋转的影片倒放,会因旋转方向相反而被认出.)

如果想消除时空交叉项，可按下式定义新坐标系 $\{ t ^ { \prime } , r ^ { \prime } , \theta ^ { \prime } , \varphi ^ { \prime } \}$ ：

$$
t ^ { \prime } \equiv t , ~ r ^ { \prime } \equiv r , ~ \theta ^ { \prime } \equiv \theta , ~ \varphi ^ { \prime } \equiv \varphi - \varOmega t ,
$$

其中

$$
\varOmega \equiv - \frac { g _ { 0 3 } } { g _ { 3 3 } } .
$$

KN 度规在新系的线元为

$$
\mathrm { d } s ^ { 2 } = \left( g _ { 0 0 } - { \frac { { g _ { 0 3 } } ^ { 2 } } { g _ { 3 3 } } } \right) \mathrm { d } t ^ { \prime } { } ^ { 2 } + g _ { 1 1 } \mathrm { d } { r ^ { \prime } } ^ { 2 } + g _ { 2 2 } \mathrm { d } { \theta ^ { \prime } } ^ { 2 } + g _ { 3 3 } ( \mathrm { d } { \varphi ^ { \prime } } + t ^ { \prime } \mathrm { d } { \varOmega } ) ^ { 2 } ,
$$

其中 $g _ { 0 0 } , g _ { 1 1 } , g _ { 2 2 } , g _ { 3 3 } , g _ { 0 3 }$ 是度规在原坐标系的分量,但现在(连同 $\varOmega$ )应看作新坐标的函数.式(13-2-11)右边最后一项包含交叉项,但因gμv不含t和φ，由式(13-2-9)和(13-2-10)可知 $\pmb { \mathcal { S } }$ 只是 $r ^ { \prime }$ 和 $\theta ^ { \prime }$ 的函数,故式(13-2-11)不含“时空交叉项”,这是一个优点.然而度规的新分量 $g _ { \mu \nu } ^ { \prime }$ 不再与 $t ^ { \prime }$ 无关，从而隐藏了度规的稳态性,这是一大缺点,是稳态时空不选类时Killing场的积分曲线为时间坐标曲线的必然结果.不要由 $t ^ { \prime } = t$ 误以为 $( \hat { \partial } / \hat { \partial } t ^ { \prime } ) ^ { a } = ( \hat { \partial } / \hat { \partial } t ) ^ { a }$ ，因为两者都取决于各自坐标系中其他坐标的定义（ $t$ 坐标线是除 $t$ 外的坐标为常数的曲线).两者关系为

$$
\left( \frac { \partial } { \partial t } \right) ^ { a } = \left( \frac { \partial } { \partial t ^ { \prime } } \right) ^ { a } - \varOmega \left( \frac { \partial } { \partial \varphi } \right) ^ { a } .
$$

请注意(@/at')ä不是Killing场.从几何角度看，KN度规在{t',r',0',φ}系的线元之所以无时空交叉项,是因为(@/at')a与等t'面正交(图13-8).还应注意(@/aφ)[及$( \hat { \partial } / \hat { \partial } \theta ^ { \prime } ) ^ { a } , ( \hat { \partial } / \hat { \partial } r ^ { \prime } ) ^ { a } ]$ 切于等 $t ^ { \prime }$ 面,因为对 $\varphi ^ { \prime }$ 坐标线有 $t ^ { \prime } =$ 常数.

![](images/60f9f8dd6e4f4d4e872b87cc51a33dd7947ad4afd4b914b2dc530898280168c6.jpg)  
图13-8 $( \hat { \boldsymbol { o } } / \hat { \boldsymbol { o } } t ^ { \prime } ) ^ { a }$ 与等 $t ^ { \prime }$ 面正交是带撇系中线元无时空交叉项的几何原因

[选读13-2-1]

KN度规的参数M,a,Q的物理意义可借第12章的概念解释.由式(12-6-11)可知,对KN 度规,

其中 $F _ { c d } = 2 \nabla _ { [ c } A _ { d ] }$ 可由4势 $A _ { a }$ 表达式(13-2-4)求得， $\varepsilon _ { a b c d }$ 是与 KN度规适配的体元， $\boldsymbol { S }$ 是任一类空超曲面上把星体包围在内的任一拓扑 2球面.借用线元(13-2-1)可求得(习题)

$$
\frac { 1 } { 8 \pi } \int \varepsilon _ { a b c d } F ^ { c d } = \mathrm { K N } \ 种 \bar { \pi } ( 1 3 \ – 2 \ – 1 ) \sharp \rlap / \hbar \frac { * } { \hbar } \ast \rlap / { \hbar } \mathcal { Q } ,
$$

可见参数 $\mathcal { Q }$ 的确是时空的总电荷.对 $Q = 0$ 的情况，(事实上任何星体都有 $Q < < M$ ，对大多数情况都可近似认为 $Q = 0$ .）星外Kerr时空是渐近平直稳态时空[Ashtekarand Hansen (1978)附录 $\mathbf { C }$ 有详细讨论],时空的总质量可由 Komar 质量公式[式(12-7-2)]

$$
M _ { \mathrm { K } } = - { \frac { 1 } { 8 \pi } } { \int } \varepsilon _ { a b c d } \nabla ^ { c } { \xi ^ { d } }
$$

计算,其中类时 Killing 矢量场 $\xi ^ { d }$ 就是Boyer-Lindquist系的坐标基矢场 $( \partial / \partial t ) ^ { d }$ .由计算可得(习题)

$$
{ \cal M } _ { \mathrm { K } } = - { \frac { 1 } { 8 \pi } } { \int } \varepsilon _ { a b c d } \nabla ^ { c } { \xi } ^ { d } = \mathrm { K e r r } \ { \not \equiv \hat { \pi } } \hat { \pi } ( 1 3 - 2 \mathrm { - } 1 ) \not \equiv \not \exists \not \equiv \not \exists \not \equiv \not { \ k } { \cal M } ,
$$

可见参数 $M$ 的确是星体(时空)的总质量.类似地,渐近平直的轴对称真空时空的总角动量可由下式定义[参见Wald(1984)第11章习题6]

$$
\sharp \ddagger { \underbrace { \ddot { \Sigma } } _ { \Sigma } } ^ { * } \lessgtr ^ { * } \boxed { \dot { \bar { \Sigma } } } \bar { \mathcal { D } } \bar { \mathcal { D } } : = \frac { 1 } { 1 6 \pi } \int \varepsilon _ { a b c d } \nabla ^ { c } \psi ^ { d } \ ,
$$

其中 $\psi ^ { d }$ 是反映轴对称性的类空 Killing 矢量场.[对 Kerr-时空， $\psi ^ { d }$ 就是Boyer-Lindquist系的坐标基矢场 $\left( \widehat { o } / \widehat { o } \varphi \right) ^ { a } . ]$ 由计算可得(习题)

$$
\frac { 1 } { 1 6 \pi } \int _ { S } ^ { } \varepsilon _ { a b c d } \nabla ^ { c } \psi ^ { d } = M a ,
$$

可见 $a$ 的确是星体(时空)的单位质量的角动量.

对 $Q \neq 0$ 的 KN 时空,能动张量 $T _ { a b }$ 在星外不为零,但在趋于无限远时足够快地趋于零,用式(13-2-15)和(13-2-17)计算总质量和总角动量时应取两式右边的积分在 $S ^ { \mathrm { ~ ~ } \bullet }$ 趋于无限远”时的极限(见小节12.7.1末),结果仍分别为 $M$ 和 $M a$ .

# S 13.3 KN 时空的最大延拓

线元(13-2-1)在 $\rho ^ { 2 } = 0$ 即 $r = 0$ 且 $\theta = \pi / 2 )$ 处奇异 $( g _ { 0 0 } , g _ { 3 3 }$ 和 $g _ { 0 3 }$ 无意义).计算表明这一奇性对应于不完备类光(在 $Q = 0$ 时还有类时)测地线,而且 $R _ { a b c d } R ^ { a b c d }$ 在趋于 $\rho ^ { 2 } = 0$ 时发散,可见 $\rho ^ { 2 } = 0$ 是时空奇性,而且是 s.p.曲率奇性(见小节9.4.1末).除这一奇性外,线元(13-2-1)在 $\pmb { \mathcal { A } } = \mathbf { 0 }$ 处也有奇性.由式(13-2-3)可知能使 $\varDelta = 0$ 的 $r$ 为

$$
r _ { \pm } = M \pm \sqrt { M ^ { 2 } - ( a ^ { 2 } + Q ^ { 2 } ) } .
$$

对下列三种情况应分别讨论： $\textcircled { 1 } M ^ { 2 } < a ^ { 2 } + Q ^ { 2 } , \textcircled { 2 } M ^ { 2 } > a ^ { 2 } + Q ^ { 2 } , \textcircled { 3 } M ^ { 2 } = a ^ { 2 } + Q ^ { 2 }$ ·

# 13.3.1 $M ^ { 2 } < a ^ { 2 } + Q ^ { 2 }$ 的情况

这时 $\varDelta ( r ) = 0$ 没有实根,线元(13-2-1)只在 $\rho ^ { 2 } = 0$ 处奇异.要想弄清奇点所在区的“形状”,先要对Boyer-Lindquist坐标给出合理的解释.鉴于施瓦西坐标 $t , r , \theta , \varphi$ 可解释为准球坐标，(当 $M = 0$ 时退化为闵氏时空的球坐标．“准”字也常略去.）最天真的想法是把 Boyer-Lindquist 坐标 $t , r , \theta , \varphi$ 也解释为准球坐标.然而 $\rho ^ { 2 } = 0$ 对应于 $r = 0$ 且 $\theta = \pi / 2$ ，而球坐标 $\theta$ 在 $r = 0$ 处无意义，因此条件 $r = 0 , \theta = \pi / 2$ 显得非常奇怪.例如,奇点应从时空流形中挖去,而球坐标 $r = 0$ 代表一个点(不问 $\theta$ 是否为$\pi / 2 )$ ，到底该挖不该挖？这说明在求解爱因斯坦方程得到 $g _ { \mu \nu }$ 后,在讨论它代表的度规场 $g _ { a b }$ 应该定义在什么流形上这一问题时,对所用坐标系的天真解释是易出问题的.为了给 Boyer-Lindquist 坐标 $t , r , \theta , \varphi$ 一个合理的解释,先考虑 $M = Q = 0$ 而 $a \neq 0$ 的特例.这时式(13-2-1)成为

$$
\begin{array} { r l } & { \mathrm { d } s ^ { 2 } = - \mathrm { d } t ^ { 2 } + ( r ^ { 2 } + a ^ { 2 } ) ^ { - 1 } ( r ^ { 2 } + a ^ { 2 } \cos ^ { 2 } \theta ) \mathrm { d } r ^ { 2 } + ( r ^ { 2 } + a ^ { 2 } \cos ^ { 2 } \theta ) \mathrm { d } \theta ^ { 2 } } \\ & { \quad + ( r ^ { 2 } + a ^ { 2 } ) \sin ^ { 2 } \theta \mathrm { d } \varphi ^ { 2 } , } \end{array}
$$

它在 $r = 0 , \theta = \pi / 2$ 处仍奇异(行列式 $g = 0$ ).然而,从物理角度考虑， $M = Q = 0$ 恐怕就应为平直度规,故式(13-3-2)应能通过坐标变换变为闵氏线元的最简形式.事实的确如此.令

$$
x = { \sqrt { r ^ { 2 } + a ^ { 2 } } } \sin \theta \cos \varphi , y = { \sqrt { r ^ { 2 } + a ^ { 2 } } } \sin \theta \sin \varphi , z = r \cos \theta ,
$$

则式(13-3-2)变为 $\mathrm { d } s ^ { 2 } = - \mathrm { d } t ^ { 2 } + \mathrm { d } x ^ { 2 } + \mathrm { d } y ^ { 2 } + \mathrm { d } z ^ { 2 }$ .可见式(13-3-2)在 $r = 0 , \theta = \pi / 2$ 处的奇性只是坐标奇性,而且式中的 $^ { a }$ 也只是坐标变换的一个参数,毫无物理意义.

式(13-3-3)其实就是3维欧氏空间中笛卡儿坐标与椭球坐标之间的变换关系.由该式可知等φ面是过z轴的平面,这与球坐标系相同.然而椭球坐标系中等r面和等θ面的表现却与球坐标系不同.由式(13-3-3)可看出各等r面和等θ面关于z轴对称,因此只须讨论任一φ=φ的等φ面.又由于在x～y面内作坐标转动

$$
x \mapsto x ^ { \prime } = x \cos \varphi _ { 0 } + y \sin \varphi _ { 0 } , \quad y \mapsto y ^ { \prime } = - x \sin \varphi _ { 0 } + y \cos \varphi _ { 0 } ,
$$

便可使此面的 $\varphi$ 值变为 $\varphi ^ { \prime } = \varphi - \varphi _ { 0 } = 0$ ，所以只须讨论 $\varphi = 0$ 的等 $\varphi$ 面.但它只代表半个平面(x～z面的一半),索性讨论由φ=0和φ=π合起来的整个x～z面.在此截面上有

$$
x = \pm { \sqrt { r ^ { 2 } + a ^ { 2 } } } \sin \theta , \gamma = 0 , z = r \cos \theta .
$$

当 $r \neq 0$ 时上式给出

$$
{ \frac { x ^ { 2 } } { r ^ { 2 } + a ^ { 2 } } } + { \frac { z ^ { 2 } } { r ^ { 2 } } } = 1 ,
$$

可见 $x \sim z$ 面内的等 $r$ 线是单参共焦椭圆族,焦点与原点的距离为

$$
{ \sqrt { ( r ^ { 2 } + a ^ { 2 } ) - r ^ { 2 } } } = a .
$$

当 $r = 0$ 时式(13-3-4)给出 $x = \pm a \sin \theta , z = 0$ ，所以 $r = 0$ 的等 $r$ 线是两焦点之间的直线段，不妨看作短轴为零的“椭圆”(图13-9).另一方面，若sinθ≠0,cosθ≠0,则式(13-3-4)给出

$$
\frac { x ^ { 2 } } { a ^ { 2 } \sin ^ { 2 } \theta } - \frac { z ^ { 2 } } { a ^ { 2 } \cos ^ { 2 } \theta } = 1 ,
$$

可见 $x \sim z$ 面内的等 $\theta$ 线是单参共焦双曲线族， $\textcircled{1}$ 焦点与原点的距离为

$$
{ \sqrt { a ^ { 2 } \sin ^ { 2 } \theta + a ^ { 2 } \cos ^ { 2 } \theta } } = a ,
$$

说明这对焦点与刚才那对焦点重合.当sinθ=0(或cosθ=0)时双曲线退化为z(或x)轴的两段(图13-9).椭球坐标系与球坐标系的一个重要区别是:对球坐标系,r=0是原点；对椭球坐标系,r=0是半径为a的圆盘,而θ和φ则是用以区分盘上不同点的坐标.r=0,θ=π/2代表圆盘的边线,即半径为a的圆环,也可用笛卡儿坐标表为x²+y²=α²,z=0.上述讨论表明闵氏度规在椭球坐标系的线元(13-3-2)在圆环(r=0,θ=π/2)上有奇性,这当然只是坐标奇性.受此启发,人们认识到KN时空的Boyer-Lindquist 坐标 $t , r , \theta$ ， $\varphi$ 不应天真地解释为准球坐标,而应看作准椭球坐标(在M=Q=0时退化为椭球坐标),并希望找到闵氏时空的洛伦兹坐标t,x,y,z在 KN 时空的某种推广(准洛伦兹坐标),它与准椭球坐标的关系在$M = Q = 0$ 时能回到式(13-3-3).这种准洛伦兹坐标的确存在,称为Kerr-Schild 坐标,与准椭球坐标的关系为

![](images/095a63806efc24a9a5f0ced70d81a46e4d2afed655caa2ad12cd3d6bfb85b547.jpg)  
图13-9 椭球坐标系(关于 $z$ 轴对称)

$$
\overline { t } = t - r + \int ( r ^ { 2 } + a ^ { 2 } ) \varDelta ^ { - 1 } \mathrm { d } r ,
$$

$$
x = \sqrt { r ^ { 2 } + a ^ { 2 } } \sin \theta \cos \left[ \varphi + \arctan \frac { a } { r } + a \int _ { \infty } ^ { r } \varDelta ^ { - 1 } ( \hat { r } ) \mathrm { d } \hat { r } \right] ,
$$

$$
\gamma = \sqrt { r ^ { 2 } + a ^ { 2 } } \sin \theta \sin \left[ \varphi + \arctan \frac { a } { r } + a \int _ { \infty } ^ { r } \varDelta ^ { - 1 } ( \hat { r } ) \mathrm { d } \hat { r } \right] \ : ,
$$

$$
z = r \cos \theta \ .
$$

KN度规在Kerr-Schild 坐标系{t,x,y,z}的线元式为(Kerr最初求得的线元正是下 $\stackrel { \cdot } { Q } = 0$ 时的特例) m

$$
\begin{array} { l } { { \displaystyle { \mathrm { d } } s ^ { 2 } = - { \mathrm { d } } \vec { t } ^ { 2 } + { \mathrm { d } } x ^ { 2 } + { \mathrm { d } } y ^ { 2 } + { \mathrm { d } } z ^ { 2 } + \frac { r ^ { 2 } ( 2 M r - Q ^ { 2 } ) } { r ^ { 4 } + a ^ { 2 } z ^ { 2 } } } } \\ { { \displaystyle \qquad \times \left[ \frac { r ( x { \mathrm { d } } x + \mathrm { p a b } { \mathrm { b } } ) - a ( x { \mathrm { d } } y { \mathrm { H } } ^ { \dag } y { \mathrm { d } } x ) } { r ^ { 2 } + a ^ { 2 } } + \frac { z { \mathrm { d } } z } { r } + { \mathrm { d } } \overline { { t } } \right] ^ { 2 } } } \end{array} .
$$

当 $M = Q = 0$ 时上式退化为闵氏度规在洛伦兹系的线元.请读者验证式(13-3-3)是(13-3-5)的后3式在 $M = Q = 0$ 时的特例.由式(13-3-5)可知 $r = 0 , \theta = \pi / 2$ (即 $\rho ^ { 2 } = 0$ ）也对应于 $x ^ { 2 } + y ^ { 2 } = a ^ { 2 }$ ， $z = 0$ ,即代表半径为 $a$ 的圆环,所以 KN 时空的奇性称为环状奇性(ring singularity)或奇环(singular ring),应从时空中开除出去[在4维语言中应开除的是这个环与 $\mathbb { R }$ （“时间”)的卡氏积].

既然式(13-3-6)是KN 度规在 Kerr-Schild 坐标系(准洛伦兹坐标系)的线元,式中的 $r$ 就应看作坐标 $x , y , z$ 的函数.由式(13-3-5)可知函数 $r ( x , y , z )$ 以如下方式被隐给出(但只能把 $r$ 确定到差一负号的程度):

$$
r ^ { 4 } - r ^ { 2 } ( x ^ { 2 } + y ^ { 2 } + z ^ { 2 } - a ^ { 2 } ) - a ^ { 2 } z ^ { 2 } = 0 .
$$

上式首先表明 $z \neq 0$ 时 $r \neq 0$ .令 $K \equiv x ^ { 2 } + y ^ { 2 } - a ^ { 2 }$ ，则由上式还可解得

$$
r ^ { 2 } = \frac { 1 } { 2 } \bigg [ K + z ^ { 2 } + \sqrt { ( K + z ^ { 2 } ) ^ { 2 } + 4 a ^ { 2 } z ^ { 2 } } \bigg ] ,
$$

故 $z = 0$ 时 $r ^ { 2 } = ( K + | K | ) / 2$ ，表明

$$
\left\{ r = 0 , \frac { \ast \hdots } { \hslash } x ^ { 2 } + y ^ { 2 } - a ^ { 2 } \leqslant 0 , \right. \mathrm { ~ }
$$

上述结论也可从图13-9 看出(图中横轴相当于 $z = 0$ ).不过现在出现一个微妙问题.在 $M ^ { 2 } < a ^ { 2 } + Q ^ { 2 }$ 的情况下线元(13-2-1)只在 $\rho ^ { 2 } = 0$ (即奇环)处奇异,因此原则上 $r$ 既可为正又可为负(在 $\theta \neq \pi / 2$ 时还可为零).然而图 13-9 只显示出 $r \geqslant 0$ 的一面,因为所有椭球面的 $r$ 都为正.你也可令所有椭球面的 $r$ 都为负,那时的图13-9就只显示出 $r \leqslant 0$ 的一面.可见,即使把图13-9中的圆环 $( r = 0 , \theta = \pi / 2 )$ 挖去，它与KN时空的等 $\bar { t }$ 面(记作 $\textstyle { \sum _ { \bar { t } } }$ )也不会有相同的拓扑结构.事实上,如果用挖去圆环的图13-9描述 $\Sigma _ { \bar { t } }$ (即暂时规定 $\Sigma _ { \bar { t } }$ 上的 $r \geqslant 0$ )，则到达圆盘 $( x ^ { 2 } + y ^ { 2 } < a ^ { 2 } , z = 0 )$ 的所有测地线都不完备，但计算表明在沿线趋近 $r = 0$ 时又都没有曲率奇性,这就强烈暗示着时空应“穿过圆盘内部”向 $r < 0$ 处延拓.这一想法也可从另一角度印证.要使线元(13-3-6)能描写 KN 度规,函数 $r ( x , y , z )$ 至少应为 $C ^ { 2 }$ （以使时空曲率有意义）然而(下面将证明) $z$ 在经过圆盘时变号而 $r$ 不变号导致 $\partial r / \partial z$ 在圆盘上不存在，所以$r ( x , y , z )$ 连 $\mathrm { C } ^ { 1 }$ 也不够.具体说,在 $x ^ { 2 } + y ^ { 2 } < a ^ { 2 }$ 的情况下有 $x _ { i } = \sum \limits _ { i = 1 } ^ { n } i _ { i }$

$$
 \frac { \partial r } { \partial z } | _ { z = 0 } \frac { \mp \operatorname * { l i m } _ { z  0 } ^ { r - 0 } = ( \frac { r } { \mathrm { d i f f o r } } + \infty , 0 \cdot r ) } { z  \theta _ { z } = 0 \cdot \infty \cdot \infty \cdot \infty } ] \ : \times
$$

再令 $\pmb { { \cal A } } \equiv \pmb { { \cal K } } + \tau ^ { 2 }$ ， $B \equiv ( A ^ { 2 } + 4 a ^ { 2 } z ^ { 2 } ) ^ { 1 / 2 }$ ，则式(13-3-8)成为 $2 r ^ { 2 } = A + B$ ，故

$$
 ( { \frac { \partial r } { \partial z } } ) ^ { 2 } | _ { z = 0 } = \operatorname * { l i m } _ { z  0 } { \frac { r ^ { 2 } } { z ^ { 2 } } } = \operatorname * { l i m } _ { z  0 } { \frac { { \cal A } + { \cal B } } { 2 z ^ { 2 } } } = \operatorname * { l i m } _ { z  0 } { \frac { ( { \cal A } + { \cal B } ) ( { \cal A } - { \cal B } ) } { 2 z ^ { 2 } ( { \cal A } - { \cal B } ) } }
$$

$$
= \operatorname* { l i m } _ { z  0 } { \cfrac { - 2 a ^ { 2 } } { K + z ^ { 2 } - { \sqrt { ( K + z ^ { 2 } ) ^ { 2 } + 4 a ^ { 2 } z ^ { 2 } } } } } = - { \frac { a ^ { 2 } } { K } } = { \frac { a ^ { 2 } } { a ^ { 2 } - x ^ { 2 } - y ^ { 2 } } } \neq 0 .
$$

就是说,只要 $\partial r / \partial z | _ { z = 0 }$ 存在,则必非零.另一方面,由式(13-3-7)可知在 $x , y$ 给定后$r ( - z ) = \pm r ( z )$ ，若坚持在穿过圆盘时 $r$ 不变号，则只能有$r ( - z ) = r ( z )$ ，故 $r ( z ) / z$ 与 $r ( - z ) / ( - z )$ 异号，由式(13-3-10)便得$\partial r / \partial z \mid _ { z = 0 } = \operatorname* { l i m } _ { z  0 } ( r / z ) = 0$ ，与“只要 $\partial r / \partial z | _ { z = 0 }$ 存在,则必非零”的结论矛盾.可见 $r ( - z ) = - r ( z )$ ，即 $r$ 在自上而下经过圆盘时也像 $z$ 那样由正变负.这再次表明 $r$ 应向负值延拓.①为便于理解即将介绍的延拓,先打一个比方.设在闵氏时空中挖去两区$A$ 和 $B$ 再把两者的边界按某种方式认同(图13-10),度规通常便不连续.治理此“病”的方法很简单：先解除认同,再补上所挖部分便可.线元(13-3-6)中的函数 $r ( x , y , z )$ 在 $r = 0$ 处的病态表现也可认为是从原本有光滑度规的流形中挖去某个区域并把所余部分随意认同的结果.治理方法也是先解除认同再补上所挖部分.具体做法如下.取 $\mathbb { R } ^ { 3 }$ 的两个版本，其自然坐标分别记作 $x , y , z$ 和$x ^ { \prime } , y ^ { \prime } , z ^ { \prime }$ .挖去圆环 $z = 0 , x ^ { 2 } + y ^ { 2 } = a ^ { 2 }$ 和 $z ^ { \prime } { = } 0 , x ^ { \prime } { } ^ { 2 } + y ^ { \prime } { } ^ { 2 } { = } a ^ { 2 }$ ，产物分别记作W和$W ^ { \prime }$ ，其中的圆盘 $z = 0 , x ^ { 2 } + y ^ { 2 } < a ^ { 2 }$ 和 $z ^ { \prime } = 0 , x ^ { \prime } { } ^ { 2 } + y ^ { \prime } { } ^ { 2 } < a ^ { 2 }$ 分别记作 $D$ 和 $D ^ { \prime }$ .令$M \equiv W \times \mathbb { R }$ ， $M ^ { \prime } \equiv W ^ { \prime } \times \mathbb { R }$ ，以 $\bar { t }$ 代表 $\mathbb { R }$ 的自然坐标，则 $\{ \overline { { t } } , x , y , z \}$ 和 $\{ \overline { { t } } , x ^ { \prime } , y ^ { \prime } , z ^ { \prime } \}$ 分别是 $M$ 和 $M ^ { \prime }$ 的坐标系．以 $\bar { t } , x , y , z$ 为老坐标借式(13-3-5)在 $M$ 上定义新坐标$t , r , \theta , \varphi$ ，并规定各点的 $r > 0$ .（在 $D \times \mathbb { R }$ 上除外，那里 $r = 0$ ·）把式(13-3-5)的$x , y , z$ 改为 $x ^ { \prime } , y ^ { \prime } , z ^ { \prime }$ 后又可用来在 $M ^ { \prime }$ 上定义新坐标 $t , r , \theta , \varphi$ ，但规定$r < 0$ .（ $D ^ { \prime } \times \mathbb { R }$ 除外，那里 $r = 0$ ·）再用式(13-3-6)在 $M$ 上定义KN 度规,则 $\bar { t } , x , y , z$ 和 $t , r , \theta , \varphi$ 分别成为准洛伦兹(Kerr-Schild)坐标和准椭球坐标.在 $M ^ { \prime }$ 上也可类似地定义KN 度规,只须把式(13-3-6)中的 $x , y , z$ 改为 $x ^ { \prime } , y ^ { \prime } , z ^ { \prime }$ .设 $\Sigma _ { \bar { t } }$ 和 $\Sigma _ { \bar { t } } ^ { \prime }$ 分别是 $M$ 和 $M ^ { \prime }$ 中 $\bar { t }$ 值相等的等 $\bar { t }$ 面,则点 $( x , y , z ) \in \textstyle \sum _ { t }$ 对应的 $r$ 值是式(13-3-8)右边的正平方根；点 $( x ^ { \prime } , y ^ { \prime } , z ^ { \prime } ) \in \textstyle \mathcal { Z } _ { t } ^ { \prime }$ 的 $r$ 值是式(13-3-8)右边的负平方根.因 $\sum _ { t } ^ { \prime } - D _ { \tau } ^ { \prime }$ 上有 $r < 0$ ，故由式(13-3-5)可知图 13-11 右图的 $z ^ { \prime }$ 轴的负半轴有 $\pmb { \theta = 0 }$ ，但 $\varphi$ 与 $z ^ { \prime }$ 轴仍保持右手关系. $D$ 盘虽然并无厚度,但可看作由两个圆盘粘合而成,分别称为 $D$ 顶和 $D$ 底.(类似地, $D ^ { \prime }$ 也由 $D ^ { \prime }$ 顶和 $D ^ { \prime }$ 底粘成.） $M$ 上的KN度规在从 $D$ 顶到 $D$ 底的过渡中的不良表现可看作 $D$ 顶和 $D$ 底被错误粘合所致,因此“治病”方法是解除这一认同,再补上“曾被不适当地挖去的”ΣCM'.补法是:先把D底与D'顶认同,再把 $D$ 顶与 $D ^ { \prime }$ 底认同(图 13-11,详见选读 13-3-1). $M$ 和 $M ^ { \prime }$ 从此合成一个“是 $M$ 的两倍大"的流形 $\widetilde { M }$ ,其中任一到达 $D$ 或 $D ^ { \prime }$ )顶的曲线必从 $D ^ { \prime }$ 或 $D$ )底出来,其 $r$ 在经过零值时变号.这样便可消除由于z值在盘上符号改变而给函数r(x,y,z)造成的不可微性.由式(13-3-6)在 $M$ 上定义的 KN 度规的定义域现在可自然延拓为 $\widetilde { M }$ ，而且在整个 $\widetilde { M }$ 上表现良好.以 $M ^ { \prime } \subset \widetilde { M }$ 上的 Boyer-Lindquist 坐标重表这一线元则仍得式(13-2-1),不过其中的 $r < 0$ $\widetilde { M }$ 仍是连通流形(满足时空背景流形的必要条件),因为其中任意两点 $p , q$ 可被连续曲线所连结(图 13-11 示出 $p \in M$ ， $q \in M ^ { \prime }$ 的情形).但它不是单连通流形,图13-12示出从 $p \in M$ 经曲线 $C _ { p 1 }$ 到点1,再经曲线$C _ { 1 2 }$ 到点2,最后经曲线 $C _ { 2 p }$ 回到 $p$ 的闭合曲线,它不能通过连续变形缩为一点(这当然是挖去奇环的结果——该闭合曲线链绕了奇环).至此我们在 $M ^ { 2 } < a ^ { 2 } + Q ^ { 2 }$ 的情况下完成了从 $r \in ( 0 , \infty )$ 到 $r \in ( - \infty , \infty )$ 的延拓,KN 度规 $g _ { a b }$ 在“大”流形 $\widetilde { M }$ 上表现良好.由于不存在其他坐标奇性, $( \tilde { M } , g _ { a b } )$ 就是 $M ^ { 2 } < a ^ { 2 } + Q ^ { 2 }$ 的 KN 时空的最大延拓.请注意这种时空不存在事件视界,环状奇性裸露在外.这种不藏在事件视界之内的奇性称为裸奇性(naked singularity).裸奇性比非裸奇性使物理学家的日子更不好过,因此Penrose于1969 年提出一个假设:任何真实的物理时空都不存在裸奇性.这称为宇宙监督假设,详见 $\ S \mathrm { E } . 2$

![](images/9b4910d1a597c763b88a5c642ae8067c3edd284146765f89bbc791f5382166e0.jpg)  
图13-10挖去A, $B$ 再把边界按某种方式认同

![](images/cd0feb6f1551e6d340047180f9962ca458b7ede5c9cfbc21eb815194a5c4955e.jpg)  
图13-11 $M$ 和 $M ^ { \prime }$ 中的等 $\bar { t }$ 面 $\Sigma _ { \overline { { t } } }$ 和 $\Sigma _ { t } ^ { \prime }$ .把 $D$ 顶与 $D '$ 底认同,$D$ 底与 $D '$ 顶认同,所得“大”流形 $\tilde { M }$ 上的KN度规表现良好

![](images/217ead54537c88c7d772bad87c82ff7b609332f5adb7e533033ea24ef281e7da.jpg)  
图13-12 $\widetilde { M }$ 是连通流形 $( \forall p , q \in \widetilde { M }$ 存在从 $p$ 到 $\pmb q$ 的连续曲线 $C _ { p 1 } \cup C _ { 1 q } .$ ，但不是单连通流形(存在不能连续缩为一点的连续闭曲线 $C _ { p 1 } \bigcup C _ { 1 2 } \bigcup C _ { 2 p } )$

[选读13-3-1]

读者可能会问：圆盘 $D$ （及 $D '$ )既然没有厚度,所谓“把 $D$ 底与 $D '$ 顶认同”和“把 $D$ 顶与 $D ^ { \prime }$ 底认同”究竟是什么意思?其实,真正的认同无非是把 $D$ 和 $D ^ { \prime }$ 的对应点视为同一点，因而就是把 $D$ 与 $D '$ 做了认同.采用“把 $D$ 底与 $D ^ { \prime }$ 顶认同”说法的目的是指明曲线的走向,即：任一条从 $D ^ { \mathrm { ~ } ^ { 6 6 } }$ 上方” $( \theta < \pi / 2 )$ 出发的曲线到达 $D$ （因而到达 $D ^ { \prime }$ )后应向 $D ^ { \prime } ^ { 6 6 }$ 下方” $( \theta < \pi / 2 )$ 继续前行.为了更加清晰和避免误解，也可用如下方式重新表述前面的做法.

以 $x , y , z$ 代表 $\mathbb { R } ^ { 3 }$ 的笛卡儿坐标.从 $\mathbb { R } ^ { 3 }$ 中挖去 $z = 0 , \ x ^ { 2 } + y ^ { 2 } \leqslant a ^ { 2 }$ 的所有点，其产物(再与 $\mathbb { R }$ 作卡氏积,下同)记作 $N$ .在 $N$ 上按式(13-3-8)定义 $r$ ，并要求 $r > 0$ .再从 $\mathbb { R } ^ { 3 }$ 中挖去 $z = 0$ ， $x ^ { 2 } + y ^ { 2 } \geqslant a ^ { 2 }$ 的所有点，其产物记作 $\hat { N }$ .在 $\hat { N }$ 上按式(13-3-8)定义 $r$ ，并要求 $r > 0$ （对 $z > 0 \ .$ ）， $r = 0$ （对 $z = 0$ ），, $r < 0$ （对 $z < 0$ ).类似地还可定义 $N ^ { \prime }$ 和 $\hat { N } ^ { \prime }$ ，只是在 $N ^ { \prime }$ 上要求 $r < 0$ ；在 $\hat { N } ^ { \prime }$ 上要求 $r < 0$ （对 $z > 0$ ）， $r = 0$ （对$z = 0$ ）， $r > 0$ （对 $z < 0$ ).再用式(13-3-5)在 $N , \hat { N } , N ^ { \prime } , \hat { N } ^ { \prime }$ 上定义 $\theta$ 和 $\varphi$ 值.现在把$N , \hat { N } , N ^ { \prime } , \hat { N } ^ { \prime } \bot r , \theta , \varphi$ 相等的点认同,它们便可看作一个大流形 $\widetilde { M }$ 的4个坐标邻域，四者之间的相交状况如下：

$$
\begin{array} { r } { N \bigcap N ^ { \prime } = \emptyset , \quad \hat { N } \bigcap \hat { N } ^ { \prime } = \emptyset , } \end{array}
$$

$$
N \cap { \hat { N } } = O _ { 1 } , N \cap { \hat { N } } ^ { \prime } = O _ { 2 } , N ^ { \prime } \cap { \hat { N } } = O _ { 3 } , N ^ { \prime } \cap { \hat { N } } ^ { \prime } = O _ { 4 } ,
$$

其中 $O _ { 1 } , O _ { 2 } , O _ { 3 } , O _ { 4 }$ 是如图13-13所示的开集,例如(其他仿此), $O _ { 1 }$ 定义为

$$
O _ { 1 } \equiv \{ ( \overline { { { t } } } , x , y , z ) | z > 0 , r > 0 \} ,
$$

而 $N$ 和 $\hat { N }$ 各自可表为3个子集的并集：

$$
N = O _ { 1 } \bigcup O _ { 2 } \bigcup \{ ( \overline { { t } } , x , y , z ) | z = 0 , x ^ { 2 } + y ^ { 2 } > a ^ { 2 } , r > 0 \} ,
$$

$$
\begin{array} { r } { \hat { N } = O _ { 1 } \bigcup O _ { 3 } \bigcup \{ ( \overline { { t } } , x , y , z ) | z = 0 , x ^ { 2 } + y ^ { 2 } < a ^ { 2 } , \theta < \pi / 2 \} . } \end{array}
$$

这样得到的大流形 $\widetilde { M }$ 是4个流形 $N , \hat { N } , N ^ { \prime } , \hat { N } ^ { \prime }$ 先求并集再作认同的结果,但现在的认同是开集与开集(例如 $N$ 中的 $O _ { 1 }$ 与 $\hat { N }$ 中的 $O _ { 1 }$ )的认同,比正文中的认同更为清晰明确.请注意现在的 $N$ 及 $N ^ { \prime }$ 分别是原来(正文)的 $M$ 及 $M ^ { \prime }$ 挖去圆盘$z = 0 , \ x ^ { 2 } + y ^ { 2 } < a ^ { 2 }$ 的结果. [选读13-3-1完]

![](images/d20912af44414432a0808a1120de1aec6fd2f4acf216c51a95a8824202a08aac.jpg)  
图13-13 $N , \hat { N } , N ^ { \prime } , \hat { N } ^ { \prime }$ 可看作大流形 $\widetilde { M }$ 的4个坐标邻域

# 13.3.2 $M ^ { 2 } > a ^ { 2 } + Q ^ { 2 }$ 和 $M ^ { 2 } = { { a } ^ { 2 } } + Q ^ { 2 }$ 的情况

与 $M ^ { 2 } < a ^ { 2 } + Q ^ { 2 }$ 的情况相较， $M ^ { 2 } > a ^ { 2 } + Q ^ { 2 }$ 的延拓更为复杂．首先，$r = 0$ ， $\theta = \pi / 2$ 仍是奇环,时空仍可通过圆盘 $r = 0 , \theta < \pi / 2$ 按图13-10 向 $r < 0$ 延拓.问题的复杂性源于方程 $\varDelta ( r ) = 0$ 现在有两个实根

$$
r _ { \pm } = M \pm [ M ^ { 2 } - ( a ^ { 2 } + Q ^ { 2 } ) ] ^ { 1 / 2 } .
$$

虽然通常星体半径远大于 $r _ { + }$ ,我们仍想讨论KN度规适用于全时空的情况.由于线元(13-2-1)在 $r _ { \pm }$ 上奇异,KN时空也像RN时空那样分成3种区域:I型区(渐近平直区)满足 $r _ { + } < r < \infty$ ；ⅡI型区满足 $r _ { \mathrm { - } } < r < r _ { \mathrm { + } }$ ；III 型区满足 $- \infty < r < r _ { - }$ (已向 $r < 0$ 作了延拓).当 $M ^ { 2 } = a ^ { 2 } + Q ^ { 2 }$ 时 $r _ { + } = r _ { - }$ ， $\mathrm { I I }$ 型区消失.与 RN 线元的奇性 $r = r _ { \pm }$ 类似,KN线元的上述奇性也只是坐标奇性，引入类似于Kruskal坐标的坐标可消除并实现最大延拓.图13-14(a),(b)分别是 $M ^ { 2 } > a ^ { 2 } + Q ^ { 2 }$ 和 $M ^ { 2 } = a ^ { 2 } + Q ^ { 2 }$ 的 KN 最大延拓时空的Penrose 图[详见Chandrasekhar(1983)].由于KN度规只是轴对称而非球对称,不同 $\theta$ 的情况不同,图13-14只表现出 $\pmb { \theta = 0 }$ ， $\pmb { \pi }$ (即对称轴 $z$ 上)的情况.与 RN 时空最大延拓图类似,图13-14也应向上、下方无限延伸,类光超曲面 $r = r _ { + }$ 也是I型区的事件视界(越过此视界就是KN 黑洞区),II型区与两个II型区之间的两个[互相正交的(按纸面欧氏度规)]类光超曲面 $r = r _ { - }$ 也可看作柯西视界(许多文献也称之为内视界).与RN 时空不同,III型区除包含 $0 < r < r _ { - }$ 的点外还包含 $- \infty < r = 0$ 的所有点$\rvert r = 0$ 且 $\theta = \pi / 2$ 的点除外).作为2 维时空图,图13-14 表现的只是1维空间.而$\rho ^ { 2 } = 0$ 对应于 $r = 0$ ， $\theta = \pi / 2$ ,故图13-14中的 $r = 0$ 并不代表奇环.为了表现含 $z$ 轴的2维截面的情况,可以改画空间图,即图13-15[见Carter(1966)].读过选读13-3-1的读者可以看出此图就是图13-13 的 $\hat { N }$ .与施瓦西和 RN 的最大延拓时空[图9-13(或12-9)和图13-1]类似,图13-14所描写的KN最大延拓时空很可能也不是物理真实的时空,见 $\ S 1 3 . 6$ .

![](images/d0a2bb2918d0808770170c54c6ba2891f66fcf2f9ac5f629569de9b35c956bd0.jpg)  
图13-14最大延拓 KN 时空的 Penrose 图(只表现对称轴 $z$ 的情况),曲线代表等 $r$ 线

![](images/4edca6a0ca154a9570b15e84c797109d6f4083597542387bed88eb3c1a88f1c2.jpg)  
图13-15M²>a²+Q²的KN时空的空间图(Carter图).粗椭圆线代表事件视界r=r+和内视界r=r_.图中上、下部分只在r=0,0≠π/2的圆盘连通,波状线表示上、下部分是割断的(两部分都有 $\theta < \pi / 2 \mathit { \Theta } .$ ).在 $Q = \mathbf { 0 }$ 的情况下,视界 $r = r _ { + }$ 和 $r = r _ { - }$ 随 $a ^ { 2 }$ 增大而相互趋近,当 $\pmb { a } ^ { 2 } = \pmb { M } ^ { 2 }$ 时重合(这时

Carter(1968)曾对最大延拓 KN 时空的测地线作过深入研究并得出如下结论：①不到达奇环的测地线都完备；②Q=0时,确有类时和类光测地线到达奇环(因而Q=0的KN时空是类时、类光测地不完备的),但它们必须躺在赤道面上(θ=π/2);$\textcircled { 3 } Q \neq 0$ 时,所有测地线中只有赤道面上且满足很具体条件的类光测地线才能到达奇环,因而 $Q \neq 0$ 的 KN 时空是类时测地完备而类光测地不完备的.读者试与施瓦西和 RN 时空作一比较.

最后对参数 $M , a , Q$ 的正负问题作一讨论. $M$ 的物理意义是星体(或黑洞)质量，我们一直默认M>0.Q值可正可负,反映星体(或黑洞)带电的正负.a(=J/M)在$M > 0$ 的前提下与 $J$ 同号，本来可正可负,但总可选择 $\varphi$ 坐标的正向使 $\pmb { a }$ 为正.如果把M仅看作 KN 解的一个参数而不问物理意义,则M<0当然也是解.有趣的是， $M > 0$ 的 KN 时空中 $r < 0$ 区域的度规与 $M < 0$ 的 KN 时空中 $r > 0$ 区域的度规完全相同,(因而在 $| r |$ 很大时也渐近平直,只是质量参数 $M$ 为负.）理由是线元(13-2-1)中的 $r$ 以 $r ^ { 2 }$ 或 $M r$ 形式出现.

# S13.4 静界、能层和其他

# 13.4.1 静界和能层

本节讨论 $M ^ { 2 } > a ^ { 2 } + Q ^ { 2 }$ 的情况.这时除 $r = r _ { \pm }$ 外， $g _ { 0 0 } = 0$ 的点也有重要意义.与施瓦西解不同， $a \neq 0$ 时的线元(13-2-1)在 $g _ { 0 0 } = 0$ 处并无奇性(线元的非对角性使行列式 $g$ 在 $g _ { 0 0 } = 0$ 处非零).由式(13-2-5)可知 $g _ { 0 0 }$ 的零点有两个,分别记作 $r _ { 0 + }$ 和_，即

$$
r _ { 0 \pm } = M \pm \sqrt { M ^ { 2 } - ( a ^ { 2 } \cos ^ { 2 } \theta + Q ^ { 2 } ) } ,
$$

将上式与 $r _ { \pm }$ 的表达式对比易见在对称轴上( $\pmb { \theta = 0 }$ )有 $r _ { 0 \pm } = r _ { \pm }$ ，在轴外有$r _ { 0 + } > r _ { + } , r _ { 0 - } < r _ { - }$ ，见图13-16和图13-17.曲面 $r = r _ { 0 + }$ 称为静界(理由见命题13-4-1后的注 1), $r _ { + }$ 和 $r _ { 0 + }$ 之间的区域称为能层(理由见 $\ S 1 3 . 5 )$ .因为 $r = r _ { + }$ 才是事件视界,所以能层不含于黑洞区：飞船中的观者穿越 $r = r _ { 0 + }$ 进入能层后，只要尚未到达事件视界,仍可掉转船头、开足马力回到 $r$ 为任意大的地方.4个关键点 $r _ { \pm }$ 和 $r _ { 0 \pm }$ 把 $r$ 轴分成若干区域,各区的性质与Kerr-Newman 度规在Boyer-Lindquist系的分量 $g _ { \mu \nu }$ 的正负有关.由式(13-2-5)可知 $g _ { 2 2 }$ 恒为正； $g _ { 0 0 }$ 和 $g _ { 1 1 }$ 的正负分别以 $r _ { 0 \pm }$ 和 $r _ { \pm }$ 为分界点； $g _ { 3 3 }$ 则与 $r ^ { 2 } + a ^ { 2 } + \rho ^ { - 2 } a ^ { 2 } ( 2 M r - Q ^ { 2 } ) \sin ^ { 2 } \theta$ 同号(当 $\sin ^ { 2 } \theta = 0$ 时 $g _ { 3 3 } = 0$ ).若$Q = 0$ ， $g _ { 3 3 }$ 只在 $\rho ^ { 2 } = 0$ 附近一个 $r < 0$ 的小区域内为负.若 $Q \neq 0$ ， $g _ { 3 3 }$ 可在一较大区域(包含 $r > 0$ 的点)内为负.但域内 $r > 0$ 的点的 $r ^ { 2 }$ 值不大于 $Q ^ { 2 }$ ，而 $r < 0$ 的点的r²值不大于4M²[见Carter(1968)].①图13-17 示意性地表出goo，811，822和g33在全 $r$ 轴上的正负情况.对 $r > r _ { 0 + }$ 和 $r < r _ { 0 - }$ 有 $g _ { 0 0 } < 0$ ,Killing 矢量场 $\xi ^ { a } \equiv ( \widehat { \partial } / \widehat { \partial } t ) ^ { a }$ 类时,所以这两个区域是稳态区.反之,在 $r _ { 0 - } < r < r _ { 0 + }$ 中有 $g _ { 0 0 } > 0$ ，表明 $\xi ^ { a }$ 类空,由图13-17可知 $g _ { 3 3 } > 0$ ，即 Killing场 $\psi ^ { a } \equiv ( \partial / \partial \varphi ) ^ { a }$ 也类空,所以该区为非稳态区.在能层外 $( r > r _ { 0 + } )$ 有 $g _ { 0 0 } < 0 , g _ { 1 1 } > 0 , g _ { 2 2 } > 0 , g _ { 3 3 } > 0$ ,坐标基矢 $( \partial / \partial t ) ^ { a }$ 类时而 $( \partial / \partial r ) ^ { a }$ ，$( \partial / \partial \theta ) ^ { a }$ ， $( \partial / \partial \varphi ) ^ { a }$ 类空,人们自然把 $t$ 看作时间坐标,把 $r , \theta , \varphi$ 看作空间坐标.然而在能层内 $g _ { 0 0 } , g _ { 1 1 } , g _ { 2 2 } , g _ { 3 3 }$ 皆为正,所有坐标基矢皆类空,初学者往往觉得不好理解.其实,任一时空点 $p$ 的切空间 $V _ { p }$ 的任意4个线性独立的元素都构成 $V _ { p }$ 的一个基底，它们可以全部类空.例如,设 $T , X$ 是2维闵氏时空的洛伦兹坐标,则线元可表为$\mathrm { d } s ^ { 2 } = - \mathrm { d } T ^ { 2 } + \mathrm { d } X ^ { 2 }$ .借用下式定义新坐标 $t$ 和 $x : \ T = t + x , \ X = 2 ( t - x )$ ，则线元改写为

![](images/2cd58a770270363b8835f880b581eb4306a2ae0e87dc65dcbc694e0864063a4d.jpg)  
图13-16 Kerr-Newman 黑洞、能层和静界(空间图)

$$
\mathrm { d } s ^ { 2 } = 3 \mathrm { d } t ^ { 2 } + 3 \mathrm { d } x ^ { 2 } - 1 0 \mathrm { d } t \mathrm { d } x \ : ,
$$

其中 $g _ { t t } = g _ { x x } = 3 > 0$ 表明坐标基矢 $\left( \partial / \partial t \right) ^ { a }$ 和 $( { \partial } / { \partial x } ) ^ { a }$ 都类空.事实上,不难证明

$$
\left( \frac { \partial } { \partial t } \right) ^ { a } = \left( \frac { \partial } { \partial T } \right) ^ { a } + 2 \left( \frac { \partial } { \partial X } \right) ^ { a } , \left( \frac { \partial } { \partial x } \right) ^ { a } = \left( \frac { \partial } { \partial T } \right) ^ { a } - 2 \left( \frac { \partial } { \partial X } \right) ^ { a } ,
$$

![](images/3d957e42d419484d4c6d28b1974489f9679ded892b24d761c4232b8fdd48306b.jpg)  
图13-17 $g _ { 0 0 } , g _ { 1 1 } , g _ { 2 2 } , g _ { 3 3 }$ 的正负示意图(其中 $\varepsilon _ { \pm }$ 与 $\theta$ 有关,${ \varepsilon _ { + } } ^ { 2 }$ 不超过 $Q ^ { 2 }$ ； ${ \varepsilon _ { - } } ^ { 2 }$ 不超过 $a ^ { 2 }$ ， $Q ^ { 2 }$ 和 $4 M ^ { 2 }$ 中之最大者)

从而印证 $\left( \partial / \partial t \right) ^ { a }$ 和 $( { \partial } / { \partial x } ) ^ { a }$ 的类空性.回到能层问题来,初学者可能仍觉得在物理上不好理解：怎么可以没有时间坐标？事实上,正如 $\ S 2 . 1$ 讲流形时所指出的,坐标本身是数学概念.至于时间概念,则须对时空作 $3 + 1$ 分解(详见 $\ S 1 4 . 4 )$ 后才有明确意义，而为此先要选定参考系.选定参考系后就有共动坐标系，其 $x ^ { 0 }$ 坐标线与观者世界线重合，于是第零坐标基矢 $( \partial / \partial x ^ { 0 } ) ^ { a }$ 类时,其他三个类空,坐标 $x ^ { 0 }$ 便可解释为观者的坐标时间.[是指观者手中任一走时率特定的钟(称为坐标钟)所指示的时间，与固有时很可以不同.]KN时空的Boyer-Lindquist坐标系在 $r > r _ { 0 + }$ 的时空区就是稳态参考系的一个共动坐标系，但在能层内却失去这一特点[坐标基矢 $( \partial / \partial t ) ^ { a }$ 的类空性排除了 $t$ 坐标线与任何观者世界线重合的可能].然而它在能层内仍是数学上合法的坐标系.如果愿意，你也可以另选坐标系使它满足“一个类时、三个类空”的要求.虽然能层内的 $t$ (指Boyer-Lindquist系的 $t$ )不是类时坐标,能层内外(指 $r > r _ { + }$ )绕黑洞匀速公转(指 $\mathbf { d } \varphi / \mathbf { d } t =$ 常数 $\neq 0$ ）而且 $r , \theta$ 为常数的质点(记作 $A$ ）的 $\mathbf { d } \varphi / \mathbf { d } t$ （记作 $\omega$ )却仍可解释为质点相对于远方静态观者的转动(公转)角速度.(足够远处时空近似平直,静态观者有意义.)理由如下.以 $p _ { 1 }$ 和 $p _ { 2 }$ 代表 $A$ 旋转一周的始末两个事件(图

![](images/292203e7ffeda4aabaece04670f010c2de7773a0f798185e2c9c82639a0c629f.jpg)  
图13-18 $\mathbf { d } \varphi / \mathbf { d } t$ 是质点 $\pmb { A }$ 相对于远方静态观者 $G$ 的角速度(示意图)

13-18),设 $A$ 在 $p _ { 1 }$ 时所发的外向光子的世界线(类光测地线) $\eta _ { 1 }$ 与远方静态观者 $G$ 交于 $p _ { 1 } ^ { \prime }$ .以 $\Delta t$ 代表 $p _ { 2 }$ 和 $p _ { 1 }$ 的 $t$ 坐标之差， $\phi _ { \Delta t }$ 代表由 $( { \partial } / { \partial t } ) ^ { a }$ 产生的等度规映射，则 $\eta _ { 2 } \equiv \phi _ { \Delta t } [ \eta _ { 1 } ]$ 必为过 $p _ { 2 }$ 的类光测地线，而且也必与 $G$ 相交,设交点为 ${ \pmb p } _ { 2 } ^ { \prime }$ .以 $\Delta t ^ { \prime }$ 代表 ${ \pmb p } _ { 2 } ^ { \prime }$ 和 $p _ { 1 } ^ { \prime }$ 的 $t$ 坐标之差，则必有 $\Delta t ^ { \prime } = \Delta t$ .利用同一世界线上固有时与坐标时的关系 $\mathrm { d } \tau / \mathrm { d } t = \left( - g _ { 0 0 } \right) ^ { 1 / 2 }$ 以及 $- \ g _ { 0 0 }$ 在 $r$ 很大处接近于1的事实可知 $G$ 世界线上 $p _ { 2 } ^ { \prime }$ 和的固有时间差 $\Delta \tau _ { G } \cong \Delta t ^ { \prime }$ ，因而 $\Delta \tau _ { G } \cong \Delta t$ .从 $G$ 看来(根据他的眼睛和他的标准钟), $\Delta \tau _ { G }$ 正是质点转一周所需时间，故 $G$ 测得的、质点 $A$ 的

这一结论对能层内外（指 $r > r _ { + }$ )的质点都成立.下面对能层内外质点的角速度 $\omega$ 所受到的限制作进一步的讨论.因 $\varphi$ 在对称轴上无定义，我们只讨论 $\theta \neq 0 , \pm \pi$ 的稳态观者.

命题13-4-1能层内(指 $r _ { \mathrm { + } } < r < r _ { \mathrm { 0 + } }$ )和静界上的任何观者(质点)的 $\varphi$ 坐标都不能不变即 $\pmb { \wp }$ $\mathbf { \{ } , \{ \} , \}$ $g ( \pmb { \mathscr { x } } ) > 0$ .(其实是 $\pmb { \omega }$ 与 $\pmb { a }$ 同号,但前已约定 $a > 0$ .）

证明设 $( \mathsf { \partial } / \partial \tau ) ^ { a }$ 为所论观者(质点)的4速，把类时性条件 界reaibgwsH文 $g _ { a b } ( \hat { \partial } / \hat { \partial } \tau ) ^ { a } ( \hat { \partial } / \hat { \partial } \tau ) ^ { \upsilon } < 0$ 在Boyer-Lindquist系展开并乘以 $( \mathbf { d } \tau / \mathbf { d } t ) ^ { 2 }$ 得

$$
g _ { 0 0 } + g _ { 1 1 } \left( { \frac { \mathrm { d } r } { \mathrm { d } t } } \right) ^ { 2 } + g _ { 2 2 } \left( { \frac { \mathrm { d } \theta } { \mathrm { d } t } } \right) ^ { 2 } + g _ { 3 3 } \omega ^ { 2 } + 2 g _ { 0 3 } \omega < 0 .
$$

由图 13-17 可知在能层内和静界上有g00≥0,g11,g22,833>0,故g03@<0,可见$\omega \neq 0$ .与式(13-2-5)结合得

$$
a \omega ( 2 M r - Q ^ { 2 } ) > 0 .
$$

在 $[ r _ { 0 - } , r _ { 0 + } ]$ 内 $g _ { 0 0 } \geqslant 0$ ，由式(13-2-5)可知在能层内和静界上有 $( 2 M r - Q ^ { 2 } ) > 0$ ，加上早已约定a>0,故式(13-4-3)表明ω>0. □

注1根据 \$8.1,一个观者称为稳态观者,若他是某一稳态参考系的观者，而稳态参考系则定义为与类时Killing矢量场对应的参考系.对KN时空，r,0,φ为常数的观者自然是稳态观者,因为Killing矢量场§类时.然而r,θ及@=dφ/dt为常数的观者也是稳态观者，因为不难证明(习题)其世界线与矢量场°=°+ωya的一条积分曲线重合，而ä作为Killing场a和ya的线性组合也是Killing场.前后两种稳态观者的区别在于前者的@=0，①因而相对于无限远静态观者静止,所以Misner et al.(1973)在893 页把ω=0的稳态(stationary)观者专称为 static observer,译成汉语既可以是静止观者又可以是静态观者.考虑到“静态观者”在本书\$8.1中有不同含义(只在静态时空中才有),本书把@=0的稳态观者专称为静止观者.于是命题13-4-1表明能层内不存在静止观者，而且指出能层内任何观者(质点)之所以不能静止的关键在于其φ坐标不能为常数,即必须围绕黑洞公转.由于a代表黑洞单位质量的角动量，@与a同号表明能层内的观者的旋转方向与“黑洞的旋转方向”相同,可以解释为“被黑洞拖电着转动”.由于ro+是能层的外边界,是静止观者可否存在的两个区域的交界面，因此称为静界(static limit surface). ②

能层内虽不存在静止观者，却存在稳态观者.下述命题给出能层内外稳态观者相对于无限远的角速率 ${ \pmb { \omega } } \equiv \mathbf { d } \varphi / \mathbf { d } t$ 的取值范围.$( 1 ) 5 L$

命题 13-4-2 能层内外(指r>r+)任一时空点的稳态观者(质点)的角速率${ \pmb { \omega } } \equiv \mathbf { d } \varphi / \mathbf { d } t$ 可以(且仅可以)在 $( \omega _ { - } , \omega _ { + } )$ 的范围内取值,即

$$
\omega _ { - } < \omega < \omega _ { + } ,
$$

其中

山原汉344.普欧态

内恩 1-1命

$$
\omega _ { \pm } \equiv \varOmega \pm A , \qquad \varOmega \equiv - \frac { g _ { 0 3 } } { g _ { 3 3 } } , \qquad A \equiv \sqrt { \varOmega ^ { 2 } - \frac { g _ { 0 0 } } { g _ { 3 3 } } } ,
$$

或者，借助于式(13-2-8)，注意到在 $r > r _ { + }$ 时 $\varDelta > 0$ ，有

$$
\omega _ { \pm } = \Omega \pm \frac { \sqrt { \varDelta } \sin \theta } { g _ { 3 3 } } .
$$

证明 把式(13-4-2)用于 $r$ 和 $\theta$ 为常数的观者得

$$
g _ { 0 0 } + 2 g _ { 0 3 } \omega + g _ { 3 3 } \omega ^ { 2 } < 0 .
$$

式(13-4-5)的 $\omega _ { \pm }$ 正是关于 $\omega$ 的代数方程 $g _ { 0 0 } + 2 g _ { 0 3 } \omega + g _ { 3 3 } \omega ^ { 2 } = 0$ 的解,注意到能层内外(指 $r > r _ { + }$ ）有 $g _ { 3 3 } > 0$ ,便知式(13-4-6)的充要条件为式(13-4-4). □

注2式(13-4-5)定义的 $\omega _ { \pm }$ 是 $r$ 的函数，我们讨论该式与式(13-4-4)结合后在$r \geqslant r _ { + }$ 的一些关键段(点)上对 $\omega$ 所给出的限制.由式(13-2-5)可知 $r \geqslant r _ { + }$ 时 $\pmb { \mathcal { S } }$ 与 $^ { a }$ 同号,而我们早已约定选 $\varphi$ 的正向使 $a > 0$ ，所以讨论中默认 $\pmb { \mathcal { Q } } > 0$

$( 1 ) r$ 很大的情况.这时 $g _ { 0 3 } \cong 0 , g _ { 0 0 } \cong - 1 , g _ { 3 3 } \cong r ^ { 2 } \sin ^ { 2 } \theta$ ，故 $\varOmega \cong 0$ ，由式(13-4-5)可知 $\omega _ { + } \cong ( r \sin \theta ) ^ { - 1 } , \omega _ { - } \cong - ( r \sin \theta ) ^ { - 1 }$ ，所以式(13-4-4)对 $\omega$ 给出的限制就是$- 1 < \omega r \sin \theta < 1$ .注意到 $\omega r \sin \theta$ 是线速率,(直观上不难理解,证明见本小节末.)可见命题13-4-2对远方稳态观者(质点)的限制无非是必须亚光速.

(2)能层外 $\left( \ r > r _ { 0 + } \ \right)$ 的情况，这时有 $- g _ { 0 0 } / g _ { 3 3 } > 0$ 及 $\pmb { \mathcal { Q } } > 0$ .（后者是因为$M ^ { 2 } > a ^ { 2 } + Q ^ { 2 }$ 及 $r > r _ { 0 + }$ 保证 $2 M r - Q ^ { 2 } > 0$ ，从而有 $- g _ { 0 3 } > 0 . )$ 于是由式(13-4-5)可知 $\omega _ { - } < 0$ ， $\omega _ { + } > 0$ ，因而式(13-4-4)允许 $\omega$ 取零值,说明在 $r > r _ { 0 + }$ 段内允许存在静止观者.

(3)静界上 $\left( r = r _ { 0 + } \right)$ 和能层内 $\left( r _ { + } < r < r _ { 0 + } \right)$ 的情况.由式(13-4-5)可知 $\omega _ { - } \geqslant 0$ （等号仅适用于 $r = r _ { 0 + }$ ),故式(13-4-4)要求 $\omega > 0$ ,因而不存在静止观者,与命题 13-4-1的结论一致.

(4)事件视界上( $( r = r _ { + }$ )的情况.由式(13-4-5)得

$$
\omega _ { + } - \omega _ { - } = 2 \frac { \sqrt { \varDelta } \sin \theta } { g _ { 3 3 } } .
$$

由 $\varDelta _ { r _ { + } } = 0$ 易见在 $r = r _ { + }$ 上有 $\omega _ { + } - \omega _ { - } = 0$ ，说明在事件视界上连稳态观者也不允许存在.这是事件视界的类光性及单向膜性的体现：任何观者的 $r$ 值一旦等于 $r _ { + }$ 就只能向小于 $r _ { + }$ 演化(被吸入黑洞),不存在 $r = r _ { + }$ 的类时线.

要点小结静界外 $( r > r _ { 0 + } )$ 存在静止观者；能层内 $\left( r _ { + } < r < r _ { 0 + } \right)$ 及静界上$( r = r _ { 0 + }$ )不存在静止观者,但存在稳态观者；事件视界上( $( r = r _ { + }$ )不存在稳态观者，


<!-- chunk 0016: pages 601-640 -->
甚至不存在 $r$ 为常数的观者.

现在补证“在 $r$ 很大时ωrsin $\theta$ 是稳态观者的线速率”.稳态观者的4速为

$$
\left( \frac { \partial } { \partial \tau } \right) ^ { a } = \frac { \mathrm { d } t } { \mathrm { d } \tau } \left( \frac { \partial } { \partial t } \right) ^ { a } + \frac { \mathrm { d } \varphi } { \mathrm { d } \tau } \left( \frac { \partial } { \partial \varphi } \right) ^ { a } .
$$

在 $r \to \infty$ 时 $( \partial / \partial t ) ^ { a }$ 等于静止观者的4速 $Z ^ { a }$ ，故上式可看作 $( \partial / \partial \tau ) ^ { a }$ 用 $Z ^ { a }$ 的 $3 + 1$ 分解式 $( \hat { \partial } / \hat { \partial } \tau ) ^ { a } = \gamma Z ^ { a } + \gamma u ^ { a }$ [见式(6-3-30)]，由此可得稳态观者相对于静止观者的3速度 $\pmb { u } ^ { a } = \omega ( \hat { \partial } / \hat { \partial } \varphi ) ^ { a }$ ，于是3速率 $u = \sqrt { g _ { a b } u ^ { a } u ^ { b } } = \sqrt { \omega ^ { 2 } g _ { 3 3 } } = \omega r \sin \theta .$

# 13.4.2无限红移面

设静界以外的静止观者 $G$ 和 $G ^ { \prime }$ 的径向坐标各为 $r$ 和 $r ^ { \prime } ( > r )$ ， $G$ 向 $G ^ { \prime }$ 发光,则由式(9-2-2)得

$$
\frac { \lambda ^ { \prime } } { \lambda } = \sqrt { \frac { g _ { 0 0 } ( r ^ { \prime } ) } { g _ { 0 0 } ( r ) } } ,
$$

其中 $g _ { 0 0 } = \xi ^ { a } \xi _ { a }$ 是 KN 度规在 Boyer-Lindquist 系的00分量.①由于 $g _ { 0 0 } ( r _ { 0 + } ) = 0$ ，仿照小节9.4.4的讨论可知 $r _ { 0 + }$ 是 KN 时空的无限红移面.确切地说,这只是时空中选择类时Killing场 $\xi ^ { a }$ 的积分曲线为稳态观者(我们已称为静止观者)世界线时的无限红移面.由于 KN 时空有无数个类时 Killing 矢量场,对其他类时 Killing 场将有其他无限红移面.与施瓦西时空(以及闵氏时空)类似,无限红移面是类时Killing场依赖的.由于以 $\xi ^ { a }$ 的积分曲线为世界线的稳态观者的特殊性(他们是静止观者),在谈到无限红移面而不加说明时都是指此类观者对应的无限红移面,它们与静界重合，却不同于事件视界 $( r _ { 0 + } \neq r _ { + } )$ ）.

# 13.4.3 闭合类时线

图13-17表明 $r = 0$ 附近有一由 $\pmb { \mathcal { E } } _ { - } { < } r < \pmb { \mathcal { E } } _ { \pmb { \mathrm { + } } }$ 定义的区域,其中 $g _ { 3 3 } < 0$ .为方便起见,将此区称为 $\pmb { \varepsilon }$ 区. $g _ { 3 3 } < 0$ 意味着 $\psi ^ { a } \equiv ( \partial / \partial \varphi ) ^ { a }$ 为类时矢量场.因为 $\varphi$ 坐标线是闭合曲线,所以 $\pmb { \varepsilon }$ 区内任一 $\varphi$ 坐标线都是闭合类时线.更有甚者,利用 $\pmb { \varepsilon }$ 区的特殊性质,Carter(1968)证明，对 $M ^ { 2 } > a ^ { 2 } + Q ^ { 2 }$ 的 KN 时空中 II 型区的任一点(若讨论

$M ^ { 2 } < a ^ { 2 } + Q ^ { 2 }$ 的 KN 时空,则应说对时空中任一点) $p$ 都存在过 $p$ 的闭合类时线.(为了闭合,类时线必须有一段位于 $\pmb { \varepsilon }$ 区内.）闭合类时线所导致的因果性问题见 $\ S 1 1 . 3$

$( \mathsf { a } ) r , \theta$ 为常数的圆环形镜面的光源发出正、逆行光

![](images/2addb14a50bc4636005219d83696f94bc26de88498c8c827b1a9703befe4ac29.jpg)  
图13-19(空间图）角动量 $J \neq 0$ 导致正、逆行光在 Boyer-Lindquist 系的坐标角速不等

![](images/ea050cd3b2f2bdbacaffd2601bcbf322fef58e4e8dc4353323b608d5b8caf2de.jpg)  
（b）含 $z$ 轴的截面图

# 13.4.4 局域非转动观者

在 KN 黑洞外置一 $r , \theta$ 为常数的圆环形镜子(内侧为镜面).一个以角速度$\omega _ { G }$ (相对于无限远)贴着镜面运动的观者 $G$ (因而其 $r , \theta$ 为常数)在某一时刻持一光源发光.由于镜面的吸收和再发射(反射),部分光子将贴着镜面分别沿 $\varphi$ 的正向和逆向运动并返回观者(图 13-19).以 $\omega _ { \pm }$ 代表正、逆行光子相对于无限远的角速率，把光子看作命题13-4-2中的质点的世界线趋于类光曲线的极限情况,便知这 $\omega _ { \pm }$ 可由式(13-4-5)表示.如果观者的角速率 $\omega _ { G } = 0$ ,(即是静止观者,在静界外允许存在.)他将先回收到正行光子后回收到逆行光子.因为光子的运动由时空几何决定,他可把这种双向发射并回收光子的实验看作对局域时空几何的测量手段，于是回收的不同时性表明他测得的局域时空几何在 $+ \varphi$ 和 $- \varphi$ 方向上不等价，可以解释为“他相对于局域时空几何有转动"(他相对于无限远观者无角速度恰恰相应于他相对于局域时空几何有转动).如果他想同时回收到正、逆行光子,则他应以某一匀角速(相对于无限远) $\omega _ { G }$ 贴着镜面沿正向(迎着逆行光)行进.下面将证明同时回收的充要条件是 $\omega _ { G } = \varOmega \equiv - g _ { 0 3 } / g _ { 3 3 }$ (一个完全由时空几何决定的量).这一证明对 $r > r _ { + }$ 的任一点都成立，但能层外和能层内的物理图象有所不同.[刚才介绍的物理图象（正、逆行光分别沿 $+ \varphi$ 和 $- \varphi$ 方向行进)只对能层外 $\left( r > r _ { 0 + } \right)$ 成立,在能层内$( r _ { + } < r < r _ { 0 + }$ 有 $g _ { 0 0 } > 0 , 1 < \varOmega$ （已约定 $a > 0$ )，故 $\omega _ { + } > \omega _ { - } > 0$ ，因此正、“逆”行光都沿 $+ \varphi$ 方向行进.]以 $t = 0$ 和 $t = T$ 分别代表三者(正、逆行光子及观者 $G$ )开始运动和三者相遇(同时回收)的时刻,以 $\Delta \varphi _ { { _ + } } , \Delta \varphi _ { _ - }$ 和 $\Delta \varphi _ { G }$ 依次代表三者在 $T$ 时间内走过的 $\varphi$ 角，则

$$
\Delta \varphi _ { + } = \Delta \varphi _ { G } + 2 \pi , ~ \Delta \varphi _ { G } = \Delta \varphi _ { - } + 2 \pi ,
$$

故 $\Delta \varphi _ { G } = ( \Delta \varphi _ { + } + \Delta \varphi _ { - } ) / 2$ ，除以 $T$ 便得 $\omega _ { G } = ( \omega _ { + } + \omega _ { - } ) / 2 = \varOmega$ .这一证明对能层内外和静界上[即对开区间 $( r _ { + } , \infty )$ 中的任一 $r$ 值]都成立.既然以 $\omega _ { G } = \mathcal { Q }$ 为角速率的观者能同时回收到正、逆行光子，他测得的时空几何便在 $+ \varphi$ 和 $- \varphi$ 方向上等价，因而“他相对于局域时空几何没有转动”，所以可把任一 $r , \theta$ 为常数、$\omega _ { G } \equiv \mathrm { d } \varphi _ { G } / \mathrm { d } t = \varOmega ( r , \theta )$ 的观者称为局域非转动观者(locally nonrotating observer).也可说局域非转动观者是“被黑洞拖电着”、与黑洞同步转动的观者.

以上讨论使我们想到图13-8,图中以 $t$ 坐标线为世界线的观者是静止观者，看来以 $t ^ { \prime }$ 坐标线为世界线的观者才是局域非转动观者.答案的确如此.以 $\beta$ 代表上述光子世界线的参数,用坐标系 $\{ t ^ { \prime } , r ^ { \prime } , \theta ^ { \prime } , \varphi ^ { \prime } \}$ [由式(13-2-9)定义]表述 $( \partial / \partial \beta ) ^ { a }$ 的类光性$g _ { a b } ( \hat { \partial } / \hat { \partial } \beta ) ^ { a } ( \hat { \partial } / \hat { \partial } \beta ) ^ { b } \overset { . } { = } 0$ ，注意到此系的线元不含时空交叉项以及$\mathrm { d } t ^ { \prime } / \mathrm { d } \beta = \mathrm { d } \varphi ^ { \prime } / \mathrm { d } \beta = 0$ ，得

$$
g _ { 0 0 } ^ { \prime } \left( \frac { \mathrm { d } t ^ { \prime } } { \mathrm { d } \beta } \right) ^ { 2 } + g _ { 3 3 } ^ { \prime } \left( \frac { \mathrm { d } \varphi ^ { \prime } } { \mathrm { d } \beta } \right) ^ { 2 } = 0 .
$$

以 $\omega ^ { \prime } \equiv \mathrm { d } \varphi ^ { \prime } / \mathrm { d } t ^ { \prime }$ 代表光子在这个坐标系中相对于无限远的角速率，便得$\omega _ { \pm } ^ { \prime } = \pm \left( - g _ { 0 0 } ^ { \prime } / g _ { 3 3 } ^ { \prime } \right) ^ { 1 / 2 }$ ，即 $\omega _ { + } ^ { \prime }$ 和 $\omega _ { - } ^ { \prime }$ 等值异号.这表明正、逆行光在坐标系$\{ t ^ { \prime } , r ^ { \prime } , \theta ^ { \prime } , \varphi ^ { \prime } \}$ 中的角速度等值反向,平均值为零,因此同时回收两光的观者(即局域非转动观者) $G$ 在此系的角速度应为零，即 $G$ 的世界线上不但 $r , \theta$ 为常数,而且 $\varphi ^ { \prime }$ 也为常数.而这正是 $\{ t ^ { \prime } , r ^ { \prime } , \theta ^ { \prime } , \varphi ^ { \prime } \}$ 系的 $t ^ { \prime }$ 坐标线！可见以 $t ^ { \prime }$ 坐标线为世界线的观者正是局域非转动观者.这也可通过计算他在 $\{ t , r , \theta , \varphi \}$ 系的角速度 $\omega _ { G }$ 得到印证：设$\varphi _ { G }$ 和 $\varphi _ { G } ^ { \prime }$ 是他在两系的 $\varphi$ 坐标,则由 $\varphi _ { G } ^ { \prime } = \varphi _ { G } - \varOmega t \vert$ 见式(13-2-9)]得

$$
\boldsymbol { \omega } _ { G } \equiv { \bf d } \boldsymbol { \varphi } _ { G } / { \bf d } t = { \bf d } \boldsymbol { \varphi } _ { G } ^ { \prime } / { \bf d } t + \boldsymbol { \varOmega } = \boldsymbol { \varOmega } .
$$

以 $P ^ { a }$ 代表局域非转动观者 $G$ 的4动量，则他的角动量为$L \equiv g _ { a b } P ^ { a } ( \widehat { \partial } / \partial \varphi ) ^ { b }$ [参见式(9-1-5)及该节末对角动量的讨论].注意到 $G$ 的世界线与等 $t$ 面正交以及 ${ ( \partial / \partial \varphi ) } ^ { b }$ 切于等 $t$ 面,便知 $L = 0$ .可见局域非转动观者的角动量为零，因此也被称为零角动量观者(zero-angular-momentumobserver)，详见Thorne,Price,and Macdonald(1986)及其所引文献.[选读13-4-1]

Bardeen and Press(1972)指出,研究旋转黑洞附近的物理过程时，用物理量在

Boyer-Lindquist坐标系的分量会使问题复杂化，原因是： $\textcircled{1} ( \hat { \partial } / \hat { \partial } t ) ^ { a }$ 在能层内类空而不类时； $\textcircled{2}$ 线元的非对角性给指标升降带来代数运算的麻烦.他们以局域非转动观者组成的参考系为基础建立正交归一标架场,使许多问题得以简化,而且物理意义更加明晰.这一做法还可推广到任意稳态轴对称渐近平直时空(真空或非真空),其度规在 $\{ t , r , \theta , \varphi \}$ 坐标系中的线元为

$$
\begin{array} { r } { \begin{array} { r } { \mathrm { d } s ^ { 2 } = - \mathrm { e } ^ { 2 \nu } \mathrm { d } t ^ { 2 } + \mathrm { e } ^ { 2 \nu } \left( \mathrm { d } \varphi - \mathcal { Q } \mathrm { d } t \right) ^ { 2 } + \mathrm { e } ^ { 2 \mu _ { 1 } } \mathrm { d } r ^ { 2 } + \mathrm { e } ^ { 2 \mu _ { 2 } } \mathrm { d } \theta ^ { 2 } , } \end{array} } \end{array}
$$

其中 $\nu , \psi , \mu _ { 1 } , \mu _ { 2 } , \varOmega$ 是 $r$ 和 $\theta$ 的函数.对Kerr度规有

$$
\displaystyle { \mathrm { e } } ^ { 2 \nu } = { \frac { \rho ^ { 2 } A } { A } } , \displaystyle { \mathrm { e } } ^ { 2 \psi } = { \frac { A \sin ^ { 2 } \theta } { \rho ^ { 2 } } } , \quad { \mathrm { e } } ^ { 2 \mu _ { 1 } } = { \frac { \rho ^ { 2 } } { A } } , \quad { \mathrm { e } } ^ { 2 \mu _ { 2 } } = \rho ^ { 2 } , \quad \varOmega = \frac { 2 M a r } { A } ,
$$

其中

$$
\begin{array} { r } { A \equiv ( r ^ { 2 } + a ^ { 2 } ) ^ { 2 } - 4 a ^ { 2 } \sin ^ { 2 } \theta . } \end{array}
$$

在对Kerr时空的若干计算中,先用式(13-4-9)求得结果再用式(13-4-10)代入比直接用式(13-2-1)计算要省事得多.度规(13-4-9)的局域非转动观者是这样的观者,其世界线的 $r , \theta$ 为常数， $\varphi , t$ 满足 $\mathrm { d } \varphi / \mathrm { d } t = \varOmega$ .不难证明,与 Kerr 度规一样,他们的世界线也正交于等 $t$ 面.定义正交归一4标架场[注意 $( e _ { 0 } ) ^ { a }$ 正是局域非转动观者的4速]

$$
( e _ { 0 } ) ^ { a } = { \bf e } ^ { - \nu } \left[ \left( \frac { \partial } { \partial t } \right) ^ { a } + \varOmega \left( \frac { \partial } { \partial \varphi } \right) ^ { a } \right] ,
$$

$$
( e _ { 1 } ) ^ { a } = { \bf e } ^ { - \mu _ { 1 } } \left( \frac { \partial } { \partial r } \right) ^ { a } ,
$$

$$
( e _ { 2 } ) ^ { a } = \mathrm { e } ^ { - \mu _ { 2 } } \left( \frac { \partial } { \partial \theta } \right) ^ { a } , \qquad ( e _ { 3 } ) ^ { a } = \mathrm { e } ^ { - \psi } \left( \frac { \partial } { \partial \varphi } \right) ^ { a } ,
$$

不难验证其对偶标架场为

$$
( e ^ { 0 } ) _ { a } = \mathrm { e } ^ { \nu } ( \mathrm { d } t ) _ { a } , ( e ^ { 1 } ) _ { a } = \mathrm { e } ^ { \mu _ { 1 } } ( \mathrm { d } r ) _ { a } , ( e ^ { 2 } ) _ { a } = \mathrm { e } ^ { \mu _ { 2 } } ( \mathrm { d } \theta ) _ { a } , ( e ^ { 3 } ) _ { a } = \mathrm { e } ^ { \psi } [ - \varOmega \left( \mathrm { d } t \right) _ { a } + \left( \mathrm { d } \varphi \right) _ { a } ] ,
$$

由于 $\{ ( e _ { i } ) ^ { a } , i = 1 , 2 , 3 \}$ 就是局域非转动观者的空间3标架,所以任一空间张量的 $i$ 分量就是他测得的分量,有清晰的物理意义.为避免误解，我们指出两点： $\textcircled{1}$ 由全体局域非转动观者组成的参考系并非稳态参考系，因为它不对应于任一Killing矢量场$[ \mathcal { S } 2 ( r , \theta )$ 的非常数性导致式(13-2-12)的 $( \partial / \partial t ^ { \prime } ) ^ { a }$ 的非Killing性].局域非转动观者 $G$ 之所以是稳态观者，是因为存在以他的角速度 $\varOmega$ 为组合常数组成的Killing 场$\widetilde { \xi } ^ { a } \equiv \xi ^ { a } + \varOmega \psi ^ { a }$ .设局域非转动观者 $G ^ { \prime }$ 与 $G$ 有不同的 $r , \theta$ 值,则其角速度 $\Omega ^ { \prime }$ 不等于 $^ { \varOmega }$ ，但 $G ^ { \prime }$ 由于属于另一稳态参考系(对应于Killing 场 $\widetilde { \xi } ^ { \prime a } \equiv \xi ^ { a } + \varOmega ^ { \prime } \psi ^ { a } )$ 而同样有资格作为稳态观者.简言之， $G$ 和 $G ^ { \prime }$ 是属于不同稳态参考系的两个稳态观者. $\textcircled{2}$ 局域非转动观者的世界线并非测地线,其正交归一4标架场(13-4-12)沿世界线也非费移(“非转动”不同于无自转).

# S13.5 从旋转黑洞提取能量(Penrose 过程)

设 $C ( \tau )$ 是Kerr 时空的指向未来类时线， $\tau$ 为固有时, $P ^ { a } = m ( \partial / \partial \tau ) ^ { a }$ 是它所代 表的质点的4动量，则

$$
{ \cal E } \equiv - g _ { a b } \xi ^ { a } P ^ { b } = - \xi ^ { a } P _ { a } = - \left( \frac { \partial } { \partial t } \right) ^ { a } P _ { a } , .
$$

$$
{ \cal L } \equiv g _ { a b } \psi ^ { a } { \cal P } ^ { b } = \psi ^ { a } P _ { a } = \left( { \frac { \partial } { \partial \varphi } } \right) ^ { a } P _ { a }
$$

可分别解释为质点(相对于无限远稳态观者)的能量和角动量(见 $\ S 9 . 1 )$ .由于$\xi ^ { a } \equiv ( \widehat { \partial } / \widehat { \partial } t ) ^ { a }$ 和 $\psi ^ { a } \equiv ( \partial / \partial \varphi ) ^ { a }$ 是 Killing矢量场,由定理4-3-3可知当 $C ( \tau )$ 为测地线时 $E$ 和 $L$ 在线上为常量,可分别解释为质点的能量和角动量守恒.因为 $\xi ^ { a }$ 在能层外是指向未来类时的,由命题 11-1-1(1)及式(13-5-1)可知 $E > 0$ .然而, $\xi ^ { a }$ 在能层内类空,于是 $\dot { \boldsymbol { { \cal E } } }$ 可正可负,视所论类时线 $C ( \tau )$ 而定. $E$ 恒为负的类时(及类光)曲线称为负能轨道. $\textcircled{1}$ 请注意 $E$ 与 $E _ { \ Y }$ 的区别,后者是观者(其4速 $Z ^ { a }$ 恒为类时单位矢)作当时当地观测所得的能量,不包含引力势能，恒为正( $\cdot E _ { \underline { { { \underline { { { \bf { u } } } } } } } \cdot } = - Z ^ { a } P _ { a } > 0 )$

![](images/2ea38505fa71b5d36ef99bf9e2b017e4bcf0d744d4c31fda8476d074b0b43525.jpg)  
图13-20 Penrose过程示意

Penrose 于1969 年根据能层内存在负能轨道的特点提出从旋转黑洞提取能量的有趣想法,后称 Penrose 过程(Penrose process).设能量为 $E ( > 0 )$ 的质点从“无限远”实验室向 Kerr 黑洞自由下落,则其 $E$ 为常数.质点备有定时装置,以使其在能层内某时空点自动爆裂为两块，以 $P ^ { a } , P _ { 1 } ^ { a }$ 和 $P _ { 2 } ^ { a }$ 分别代表原质点及两个碎块的 4动量.由等效原理可知狭义相对论的4动量守恒式 $P ^ { a } = { P _ { 1 } ^ { a } + P _ { 2 } ^ { a } }$ 对弯曲时空的爆裂事件也成立,与 $\xi _ { a }$ 缩并便得(局域)能量守恒 $E = E _ { 1 } + E _ { 2 }$ .可以证明，原则上总可这样安排爆裂事件,使碎块1以负能轨道为世界线(即 $E _ { 1 } < 0 \big )$ 而碎块2（其能量 $E _ { 2 } > E )$ 沿外向测地线返回远方实验室.还可证明碎块1最终必然落入黑洞(图13-20).整个过程的净结果为： $\textcircled{1}$ 远方实验室得到能量 $\Delta E = E _ { 2 } - E = - E _ { 1 } > 0$ ； $\textcircled{2}$ 由于“吃进”负能碎块1,黑洞能量由 $M$ 减为 $M - | E _ { 1 } |$ .这就是“从黑洞提取能量”的实质，能层(ergosphere)也由此得名.设想图13-20 中的远方实验室是一座城市,卡车满载垃圾向能层自由下落，到 $x$ 点把垃圾抛出并使其沿负能轨道进入黑洞，能量变大了的卡车沿外向测地线返回城市,把获得的动能转给一个巨大的飞轮并使其推动发电机,然后卡车再次满载垃圾进入能层，.这似乎为一箭双雕地解决能源和垃圾处理问题提供了一种原则上的可能性,然而付诸实践却远非如此简单.纵使有朝一日能在足够近处发现一个可供利用的旋转黑洞，上述过程所要求的非常高的爆后速率(为使能量为负,碎块1的3速率须大于c/2.）以及极端精确的定时技术,特别是对两个碎块的精确去向的控制都是远非目前人类技术所能达到的.不过,无论如何,这至少是一个很有兴趣的理论设想.

旋转黑洞(至少在理论上)可以成为取之不尽的能源吗?当然不.关键在于负能粒子的角动量 $L$ 必与黑洞的角动量 $J$ 反号.证明如下.把 $\varOmega \equiv - g _ { 0 3 } / g _ { 3 3 }$ 在事件视界$r = r _ { + }$ 的值记作 $\varOmega _ { \mathrm { H } }$ (H代表事件视界)，由式(13-2-5)和(13-2-3)易得

$$
\varOmega _ { \mathrm { H } } = \frac { a } { \displaystyle r _ { + } ^ { 2 } + a ^ { 2 } } .
$$

上式再次表明 $\varOmega _ { \mathrm { H } }$ 与 $\pmb { a }$ 同号.定义矢量场

$$
K ^ { a } \equiv \xi ^ { a } + \varOmega _ { \mathrm { H } } \psi ^ { a } ,
$$

由 $\xi ^ { a }$ 和 $\psi ^ { a }$ 的Killing性以及 $\varOmega _ { \mathrm { H } }$ 的常数性可知 $K ^ { a }$ 也是Killing场.在 $\mathbf { H }$ 外定义矢量场 $\eta ^ { a } \equiv \xi ^ { a } + \omega _ { + } \psi ^ { a }$ ，因 $\omega _ { + }$ 是方程 $g _ { 0 0 } + 2 g _ { 0 3 } \omega + g _ { 3 3 } \omega ^ { 2 } = 0$ 的解,故

$$
g _ { a b } \eta ^ { a } \eta ^ { b } = g _ { 0 0 } + 2 g _ { 0 3 } \omega _ { + } + g _ { 3 3 } { \omega _ { + } } ^ { 2 } = 0 ,
$$

即 $\eta ^ { a }$ 类光.由于在 $r > r _ { 0 + }$ 处 $\xi ^ { a }$ 为指向未来类时,而且

$$
\begin{array} { c } { { g _ { a b } \xi ^ { a } \eta ^ { b } = g _ { 0 0 } + g _ { 0 3 } \omega _ { + } = ( g _ { 0 0 } + 2 g _ { 0 3 } \omega _ { + } + g _ { 3 3 } { \omega _ { + } } ^ { 2 } ) - ( g _ { 0 3 } \omega _ { + } + g _ { 3 3 } { \omega _ { + } } ^ { 2 } ) } } \\ { { { } } } \\ { { g _ { a b } \xi ^ { a } \eta ^ { b } = g _ { + } [ g _ { 0 3 } + g _ { 3 3 } ( \varOmega + \varOmega ) ] = - \omega _ { + } g _ { 3 3 } \varLambda < 0 , } } \end{array}
$$

所以由命题 11-1-1(1)可知 $\eta ^ { a }$ 指向未来.而 $K ^ { a } \models _ { \mathrm { H } } = \eta ^ { a } \models _ { \mathrm { H } }$ ，可见 $K ^ { a }$ 在 $\mathbf { H }$ 上是指向未来的类光矢量.而质点的 4 动量 $P ^ { a }$ 是指向未来类时矢量,再次利用定理 11-1-1(1)便得

$$
0 > g _ { a b } P ^ { a } \chi ^ { b } = - E + \varOmega _ { \mathrm { H } } L .
$$

( $E$ 和 $L$ 对自由下落质点为常数).不失一般性,选 $\varphi$ 坐标的正向使 $J > 0$ ，则 $\varOmega _ { \mathrm { H } } > 0$ ，故上式在 $E < 0$ 的情况下给出

$$
L < E / \varOmega _ { \mathrm { H } } < 0 ,
$$

可见Kerr黑洞在“吃进”负能粒子后其 $J$ 将减小.等它稳定为一个 $M$ 和 $J$ 都小于原值的新Kerr黑洞后,还可再用Penrose过程提取能量.如此反复进行，当 $J$ 减至零时能层(因而提取能量的可能性)消失.下面讨论从 Kerr 黑洞可以提取的能量的极限.

黑洞在“吃进”能量为 $E$ 、角动量为 $L$ 的粒子后,质量 $M$ 和角动量 $J$ 的改变量分别为 $\delta M = E$ ， $\delta J = L$ .故式(13-5-6)可改写为 $\delta J < \varOmega _ { \mathrm { H } } { } ^ { - 1 } \delta M$ .利用式(13-5-5)又可改写为

因而

$$
\begin{array} { c } { { ( { r _ { + } } ^ { 2 } + a ^ { 2 } ) \delta M > a \delta J = a \delta ( a M ) = a ^ { 2 } \delta M + M a \delta a , } } \\ { { { } } } \\ { { { \ l { r _ { + } } } ^ { 2 } \delta M > M a \delta a . } } \end{array}
$$

用下式定义一个称为不可减质量(irreducible mass)的正量 $\hat { M }$ ：

$$
2 \hat { \cal M } ^ { 2 } \equiv { \cal M } [ { \cal M } + \sqrt { { \cal M } ^ { 2 } - a ^ { 2 } } ] ,
$$

则

$$
2 \delta ( \hat { M } ^ { 2 } ) = \frac { 1 } { \sqrt { M ^ { 2 } - a ^ { 2 } } } ( { r _ { + } } ^ { 2 } \delta M - M a \delta a ) ,
$$

于是由式(13-5-7)得

$$
\delta ( \hat { M } ^ { 2 } ) > 0 .
$$

可见,虽然黑洞在“吃进”负能粒子后 $M$ 要减小,但不可减质量却只增不减(故此得名).由式(13-5-8)可反解出 $M$ ：

$$
M ^ { 2 } = \hat { M } ^ { 2 } + \frac { J ^ { 2 } } { 4 \hat { M } ^ { 2 } } \stackrel { > } { } \hat { M } ^ { 2 } \nonumber ,
$$

设黑洞的初始数据为 $M , { \hat { M } }$ 和 $^ { a }$ ，反复经历Penrose过程后的数据为 $M ^ { \prime } , \hat { M } ^ { \prime }$ 和 $\acute { a }$ ，则由式(13-5-11)和(13-5-10)可知

$$
M ^ { \prime } \geqslant \hat { M } ^ { \prime } > \hat { M } > 0 ,
$$

可见“吃进”负能粒子后的黑洞质量不但不会为零,而且总比初始不可减质量 $\hat { M }$ 大. $\hat { M }$ 为反复经历 Penrose 过程的Kerr 黑洞提供了一个正的质量下限.能量提取的极限相应于终结质量 $M$ 等于初始不可减质量 $\hat { M } _ { 0 }$ 的情形.理由如下.首先,适当选择碎块1的轨道可使式(13-5-5)[因而(13-5-10)]的不等号任意地接近等号,于是式(13-5-12)中的 $\hat { M } ^ { \prime } > \hat { M }$ 在极限情况下可改写为 $\hat { M } ^ { \prime } = \hat { M }$ ；其次，原则上可通过多次Penrose 过程使黑洞的 $^ { a }$ 值任意地小,在极限情况下可取为零,再注意到式(13-5-11),便知式(13-5-12)中的 $\geqslant$ 可改写为等号.所以在极限情况(可趋近而不可达到)下可把式(13-5-12)改写为 $M ^ { \prime } = \hat { M } ^ { \prime } = \hat { M } > 0$ .于是

可提取的最大能量 $= M - \hat { M }$

因为上式对应的终结情况为 ${ a = 0 }$ ，相应于黑洞经多次提取能量后最终不转，所以可把 $M - { \hat { M } }$ 解释为Kerr黑洞的转动能.Penrose过程所提取的正是这种转动能．当全部转动能都被提取殆尽时Kerr黑洞退化为不转动的施瓦西黑洞．为了最大限度地提取能量，黑洞的初始不可减质量 $\hat { M }$ 应在初始质量 $M$ 给定的前提下取最小值,由式(13-5-8)知这相当于 $a = M$ 的情况[称为极端(extreme)Kerr 黑洞]，其转动能$M - { \hat { M } }$ 与能量 $M$ 之比(称为比转动能)显然为 $\frac { M - \hat { M } } { M } = 1 - \frac { 1 } { \sqrt { 2 } } \cong 2 9 \%$ ．可见反复运用Penrose过程所能提取的极限能量是黑洞总能量的 $29 \%$ ．在把质量转化为其他能量形式的各种机制中，这是一个异常巨大的转化百分数．烧氢变氦的核聚变是实验室中可实现的转化率最高的过程，其转化百分数也不到 $1 \%$

# \$13.6 黑洞“无毛”猜想

同爱因斯坦和某些物理学家原来的期望相反，广义相对论自1915年诞生后曾一直进展缓慢,经历了大约半个世纪的“冬眠”期.情况从20世纪60年代开始出现转机，当时天体物理学的新发现使广义相对论天体物理学一跃而成蓬勃发展的研究前沿.天体演化中的灾难性过程,诸如引力坍缩和星系中心的爆炸,会导致甚强而且迅变的引力场,广义相对论正好在这些领域中找到自己的用武之地.由于引力的普适性和长程性，质量足够大的天体在演化生涯晚期的自引力足以超过所有其他力而占主导地位,连平常认为最有排斥倾向的核力都不足以遏止天体坍缩成黑洞.广义相对论在对这些天体的研究中不但非用不可,而且完全不像在水星近日点进动等现象中那样只扮演对牛顿理论作微小修正的角色.然而,宇宙中是否真有黑洞?美国和意大利联合发射的、探测X射线的人造卫星Uhuru于1972年得到的信息表明某密近双星系中的不可见子星(天鹅座 X-1)是一个很有希望的黑洞候选者.虽然对它是否真是黑洞的争论至今尚未完全了断,但已有越来越多的证据表明它十分可能是黑洞.后来又发现了越来越多的黑洞候选者[见Menou etal.(1999)].无论如何,关于黑洞的研究早已并正在成为广义相对论和天体物理学的重要课题，而且它同热力学、粒子物理学、量子物理学以及数学的密切而深刻的联系也已引起多方面学者们的关注和兴趣,新的研究成果层出不穷，而且不断带来惊奇和惊喜

我们已介绍过施瓦西、RN 和 KN 黑洞,前两者只是后者的特例.由于星体或多或少都有转动,大质量恒星晚期在经历了短暂的不稳定坍缩期(那时要发射引力波和电磁波)后如果形成稳态黑洞也不可能是施瓦西或 RN 黑洞.(对稳态黑洞一词应加说明.如果要求全时空为稳态时空,则连施瓦西黑洞也不是稳态黑洞,因为黑洞内部没有类时Killing场.文献中的稳态黑洞是指这样的黑洞,它所在的时空存在这样的单参等度规群,生成该群的Killing矢量场在无限远附近为类时.）一个自然的问题是：它们一定是KN 黑洞吗?换句话说,除此还有其他稳态黑洞吗?经过许多学者多年的努力(一个漫长的研究过程),人们从20世纪70年代初开始相信如下结论:所有(电磁真空的)稳态黑洞都是 KN 黑洞,因而只需三个参量——质量 M、电荷 $Q$ 和角动量 $J = a M$ 来刻画.这是一个非常惊人的结论,它表明千差万别的恒星最终成为稳态黑洞后只需3个参量便可描述其时空几何，而且其度规又是爱因斯坦方程的一个非常好(并且相对简单)的精确解.应该指出,Kerr 度规决非旋转星体外部时空的唯一可能度规,一般来说,外部度规与星体形状及诸多因素有关,即使在 $r$ 很大之处的度规也要取决于由星体的质量分布决定的引力多极矩.Kerr 度规只描写具有某种特定质量多极矩组合的旋转星体的外部几何,具有其他多极矩组合的星体的外部几何由其他度规描写.然而,晚期坍缩的大质量星体带着自己的全部信息穿越事件视界进入黑洞内部，它们对视界外部的影响只体现为三个参量$M , J , Q$ 的影响.由于坍缩过程所发射的引力波和电磁波会带走能量和角动量(但不会带走电荷),星体的 $M$ 和 $J$ 在坍缩过程中也会改变，不过很快就会达到最终的稳态，这时的 $M , J$ 将与原来不同,因而终态黑洞及其外部度规由这终态 $M , J$ 和$Q$ 唯一决定.Wheeler在1971年把稳态黑洞只有3个参量的结论形象地说成“黑洞没有毛发”（“black holes have no hair”),这一结论后来被广泛地称作黑洞的“无毛定理”（“no hair theorem”).黑洞有3个参量而仍被说成无毛,也许缘于hair为不可数名词之故.(为描述坍缩前恒星的各个细节需要数不清的、如毛发般浓密的各种参量,而一旦坍缩成黑洞则只剩3个，故曰无毛.然而，考虑到已故著名漫画家张乐平先生笔下的三毛形象，对国人而言改称“三毛定理”或许更为合适.

以上讨论说明KN时空最大延拓图[图13-14(a)]与大质量恒星坍缩而成黑洞的物理过程没有任何关系.这不但是因为坍缩星内部并非电磁真空(因而 KN 度规不适用),而且(更重要的)是因为在坍缩为黑洞之前,如果星体有球对称性,则星外度规为施瓦西(或RN)度规(由Birkhoff定理及其对电磁真空球对称解的推广保证);如果星体无球对称性,则星体可能具有的“千姿百态”(例如隆起和湍流)将使星外偏离KN 度规.只有到坍缩完结并达到稳态后在事件视界及其外部的时空几何才由 KN 度规描述.至于事件视界以内(黑洞)的情况,人们相信 \$13.1关于RN 黑洞内部柯西视界不稳定性的讨论对KN黑洞也有重要借鉴意义，(事实上，鉴于星体都有转动，包括20世纪90年代的文章在内的关于柯西视界不稳定性的研究都是针对KN 黑洞的,只是为了简单而以 RN 黑洞为突破口.）因此,图13-14(a)中位于事件视界 $r = r _ { + }$ 以内的部分也不再适用.

黑洞无毛说是在若干唯一性定理的基础上提出的.Israel于1967年证明了其中的第一个，大意是：真空爱因斯坦方程的静态黑洞解(指事件视界以外为静态)必为施瓦西度规.稍后(1968年),他又证明了上述定理的推广：爱因斯坦-麦克斯韦方程的静态黑洞解(静态含义同上)必为RN度规.接着,Carter于1971年进一步证明如下的唯一性定理(大意):爱因斯坦-麦克斯韦方程的稳态轴对称黑洞解必为KN度规.这些唯一性定理促使Wheeler于1971年提出黑洞无毛说.后来又有许多学者(如Hawking和Robinson)在黑洞唯一性定理方面做出了进一步的成果.然而，“黑洞无毛”真是定理吗?换句话说,稳态黑洞除了质量、电荷和角动量外果真不能有其他参量吗?自从无毛说提出以来,对黑洞是否有毛的问题的探讨就一直没有停止过.既然把只有 $M , J , Q$ 三个参量的黑洞称为无毛黑洞，黑洞“毛”就应定义为存在于黑洞之外而又不是电磁场的任何场.若干文章指出，在稳态黑洞外部除电磁场外还可存在其他场,例如非阿贝尔规范场(电磁场是阿贝尔规范场)[第一个被找到的有毛黑洞所涉及的就是Einstein-Yang-Mills理论(即Yang-Mills理论与Einstein广义相对论的耦合)].特别是,20世纪80年代末和90年代初关于有毛黑洞的文章的激增更加促使许多人认为应把黑洞无毛说搁置一旁.然而，鉴于黑洞无毛说在黑洞物理中的重要性(例如它对黑洞热力学的创立有过重要的激励作用),人们还是希望能在一定的限制范围内、在某种适当的意义上证明“黑洞无毛”猜想.这一研究还在继续进行中[参阅Frolov and Novikov(1998)及其所引文献].另一方面,对有毛黑洞的研究至今仍是数学物理研究中的一个活跃分支,见Volkov and Gal'tsov(1999).

# 习 题

\~1.试证 Ker-Newman 度规在 Boyer-Lindquist 坐标系的分量满足：

(a) $- g _ { 0 3 } / g _ { 3 3 } = g ^ { 0 3 } / g ^ { 0 0 }$

$$
{ g _ { 0 3 } } ^ { 2 } - g _ { 0 0 } g _ { 3 3 } = \varDelta \sin ^ { 2 } \theta
$$

(c)行列式 $g = - \rho ^ { 4 } \sin ^ { 2 } \theta$

2．根据 Frobenius 定理(见附录F)，矢量场 $\xi ^ { a }$ 为超曲面正交的充要条件是 $\xi _ { [ a } \nabla _ { b } \xi _ { c ] } = 0$ ，其中$\xi _ { a } \equiv g _ { a b } \xi ^ { b }$ ．试证 Kerr和 KN度规中的类时 Killing 矢量场 $\xi ^ { a } \equiv ( \partial / \partial t ) ^ { a }$ 为非超曲面正交.

$^ { * 3 }$ ．试证 KN 时空的总电荷[由式(13-2-13)定义]等于其电荷参数 $Q$ .

\*4.试证参数为M,a的 Kerr 时空的总质量和总角动量[由式(13-2-15)和(13-2-17)定义]分别等于 $M$ 和 $M a$ .

\~5.试证在图 13-18中随质点 $\pmb { A }$ 一同运动的观者用标准钟测量 $\pmb { A }$ 转动一周所用的时间为

$$
\Delta \tau = 2 \pi \omega ^ { - 1 } \sqrt { - g _ { 0 0 } - 2 g _ { 0 3 } \omega - g _ { 3 3 } \omega ^ { 2 } } \ ,
$$

其中 ${ \boldsymbol { \omega } } \equiv \mathrm { d } \varphi / \mathrm { d } t$ 是远方静态观者测得的 $\pmb { A }$ 的角速度.

\~6.试证KN时空中r,θ及@=dφ/dt为常数的观者的世界线(经适当重参数化后)是Killing 矢量场 $\widetilde { \xi } ^ { a } = \xi ^ { a } + \omega \psi ^ { a }$ 的积分曲线,因而可称为稳态观者.

7.验证式(13-4-12)给出正交归一4标架场,式(13-4-13)是其对偶标架场.
