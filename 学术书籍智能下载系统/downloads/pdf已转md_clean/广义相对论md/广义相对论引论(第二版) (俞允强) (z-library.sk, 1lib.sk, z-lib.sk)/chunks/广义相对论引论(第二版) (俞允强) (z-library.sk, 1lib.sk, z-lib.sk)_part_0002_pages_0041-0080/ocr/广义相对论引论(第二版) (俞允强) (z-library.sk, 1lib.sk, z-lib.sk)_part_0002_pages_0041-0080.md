改变.选取适当的曲线参量 $\lambda$ ，可以使新坐标下的类时凯林矢量场有形式

$$
\xi ^ { \mu } = ( 1 , 0 , 0 , 0 ) .
$$

把新坐标下的度规张量记作 $\tilde { g } _ { \mu \nu }$ ，就有

$$
\begin{array} { c } { { \mathfrak { L } _ { \xi } \tilde { g } _ { \mu } = \tilde { g } _ { \mu \nu , \rho } \tilde { \xi } ^ { \rho } + \tilde { g } _ { \rho s } \tilde { \xi } _ { , \mu } ^ { \rho } + \tilde { g } _ { \mu \rho } \tilde { \xi } _ { , \nu } ^ { \rho } } } \\ { { { } } } \\ { { = \tilde { g } _ { \mu \nu , 0 } = 0 , } } \end{array}
$$

即 $\tilde { g } _ { \mu \nu }$ 与 $\mathbf { \widetilde { x } } ^ { 0 }$ 无关.于是证明了这度规场的稳定性.注意上述结论反过来也成立，即如果度规场是稳定的，它必具有类似的凯林矢量场，而且一定能找到适当的坐标使凯林矢量有(2.8.12)的简单形式.这种讨论时间平移不变性的方法，事实上对讨论任何类型的时空对称性都是适用的.我们在后面讨论物理问题时还将会遇到这种方法.

# 第三章 相对论性的引力理论

爱因斯坦所建立的广义相对论是一个协变的引力理论.它包含两部分.一一部分是等效原理，它说明有引力场存在的时空构成弯曲的黎曼空间，空间度规起着引力势的作用.另一部分是爱因斯坦引力场方程，它指明空间度规即引力势对物质分布的依赖关系.本章讨论的就是这两部分内容.

# \$3.1 引力质量与惯性质量的等同性

牛顿在力学中引入过两个质量的概念.一个从动力学方程

$$
\mathbf { \nabla } \mathbf { F } = m \mathbf { a }
$$

引入，它反映物体的惯性，可叫作惯性质量.另一个从引力定律

$$
F = { \frac { G M m } { r ^ { 2 } } }
$$

引入，它反映物体产生和接受引力的能力，可叫做引力质量.从概念上讲，这两种质量是本质上不同的物理量.但如果两者量值之比对一切物体相同，那么实用上就可以把它们当同一个量来对待.这就叫惯性质量和引力质量的等同性.

由于从概念上没有说明它们会相等的理由，我们先退一步问：它们量值上的相等是不是一个确切的物理事实？

反映它们相等的第…-个事实是伽利略的落体实验.把重力作用下的落体方程写作

$$
m _ { \# \mathbb { R } } a = m _ { \# } , g ,
$$

则有落体加速度

$$
\begin{array} { r } { a = \frac { m _ { 4 \parallel } } { m _ { \parallel } } g . } \end{array}
$$

从比萨斜塔上自由下落的大球和小球，铜球和铁球都同时到地，证明了引力质量和惯性质量之比与球的大小、材料都无关.当然伽利略并没有这样想过.

第一个明确地想检验这等同性的是牛顿.他做了两个等长的同形状的单摆，一个摆锤是金的，另一个摆锤选用等重的银、铅、玻璃、沙等不同的材料制成.单摆的周期为

$$
\begin{array} { r } { T = 2 \pi \sqrt { \frac { m _ { \perp \perp } l } { m _ { \perp \perp } g } } . } \end{array}
$$

从这里看出，仅当引力质量与惯性质量之比与材料无关，两摆的周期才会相同.牛顿做了许多实验都没能观测到周期的差异.按照实验的精确度，牛顿的结论是

$$
\frac { m _ { \vec { 5 } | } } { m _ { \hbar \Re } } = 1 + { \cal O } ( 1 0 ^ { - 3 } ) .
$$

此后检验这等同性的最著名的实验是厄阜(Eotvos)做的.他用一个很精巧的扭摆装置，去测量上述比值对1的可能的偏离.从1890 年起他持续做了25年的实验，实验中他用铂为基准比较了八种不同材料，都没有发现这可能的偏离.按照实验的精确度，厄阜的结论是

$$
\frac { m _ { \vec { \mathfrak { g } } \vert } } { m _ { \mathfrak { H } } } = 1 + O ( 1 0 ^ { - 8 } ) .
$$

在60 年代,迪克(Dicke)等人改进了厄阜实验，但实验原理并没有改变.他们仍观测到零结果，然而把精确度又提高为

$$
\frac { m _ { \mathfrak { s l } } } { m _ { \mathfrak { s l } } } = 1 + O ( 1 0 ^ { - 1 1 } ) .
$$

此外人们还用实验测定了原子和原子核的结合能所对应的惯性质量与相应引力质量之比.虽然精确度还没有那么高，但也都没有发现对1的偏离.

总之，这些实验说明，在量值上

$$
m _ { i , | } = m _ { \dagger }
$$

是一个观测事实.而它们相等的原因，则有待理论去解释。

# 3.2等效原理

下面我们来讨论惯性质量与引力质量的等同性给人们的启示

模仿爱因斯坦，考虑…个没有窗户的密封舱中的观察者.他不可能用直接的观察知道他的舱相对外部世界的运动.他通过舱内的实验发现了一条规律：舱内一切物体都会自由下落，下落的加速度与物体的固有属性无关.试想，他应该怎么解释这规律呢？

在牛顿力学的基础上，他发现有两种可能的解释.

首先，他会想到比萨斜塔上的伽利略实验，从而推断出他的舱是一个惯性系，舱内物体的自由下落是舱下面的恒星的重力场造成的.

其次，他也可以认为舱下面并没有恒星也没有引力场，舱内物体的加速自由下落反映他的舱在太空中加速地向上飞行，即下落是惯性力造成的.

注意重力正比于引力质量，而惯性力却正比于惯性质量.如果这两种质量是严格相等的，那么他在舱内再进一步做任何力学实验也不可能区分他的舱属于两种可能性中的哪一种.也就是说，他的任何力学实验都无法区分是重力的效果或惯性力的效果.这种引力和惯性力(即参考系的加速运动)的等效性被称作弱等效原理.其中“弱"指限于力学现象.弱等效原理只是惯性质量与引力质量严格相等的一个推论.

如果进一步假定任何物理实验一-力学的、电磁的和其他的实验都不可能判断他的舱是引力场中的惯性系或不受引力的加速系，即不能区分引力或惯性力的效果，这就是强等效原理.强等效原理是-个更强的假设，也是更深刻的假设.它的要点是认为引力和惯性力在物理效果上完全没有区别.或者从另一角度讲：一个局域参考系的加速度仅有相对的意义.这正是广义相对论的基本观点

如果参考系的加速度失去了绝对意义，那么惯性系的概念必须重新审查.为此我们考察一个恒星表面附近正在自由下落的爱因斯坦密封舱.

以此密封舱为参考系，内部空间的引力与惯性力正好抵消.舱内的观察者会发现，不需要引入任何看不到来源的力，牛顿第二定律对他的参考系完全适用.任何力学实验都不能使他获得一点证据，来表明他的参考系在加速地相对恒星表面下落.这一切正是弱等效原理的表现.那么是否可能用其他的，例如电磁的实验来发现他的舱的加速运动呢?按强等效原理的思想，他的电磁实验将证实惯性系中才适用的麦克斯韦方程对他的舱完全有效，因而也没有理由断言他的舱在做加速运动.

按照这样的分析，近年来人们更准确地把强等效原理表述如下：在任何引力场中任一时空点，人们总能建立一个自由下落的局域参考系，在这一参考系中狭义相对论所确立的物理规律全部有效.如果进步把狭义相对论所确立的物理规律全部有效的参考系定义为惯性系，那么上述自由下落的密封舱正构成一个局域惯性系的样本.值得注意，从恒星表面上的静止观察者看来，实际上，它是一个加速的参考系.

我们对这新的惯性系概念再作一些补充说明.首先关于惯性系的本质.原来认为惯性系是自身没有加速度的参考系.这概念是无法确切定义的，因为在自然界中找不到第一个最基本的无加速系.现在按推广了的引力概念，认为惯性系是没有引力存在的参考系.或者用旧概念讲，它是引力与惯性力相抵消的参考系.这样惯性系就成了至少局域地能实现的参考系，即在引力场中做自由运动的参考系.按这新概念，--个静止在恒星表面的参考系反而不是惯性系了.其次关于实际惯性系的局域性.事实表明全空间的引力场是不均匀的，因此无法找到一个参考系使它的惯性力处处与引力相消.这就说明现实的惯性系只能是局域的.严格讲来，在不均匀引力场中自由下落的参考系中，只有一点上的惯性力与引力完全相消.因此自由下落的局域惯性系也只是一个近似的惯性系.

# \$3.3引力几何化

强等效原理是一个强有力的原理，它包含了许多重要的推论.上节讨论的惯性系概念的修正是它的推论之一.现在我们继续考察它的后果.

等效原理显然要求引力和惯性力可用同样方法描述.容易看清惯性力是怎么描述的.当一个质点相对闵柯夫斯基空间中的惯性系作自由运动时，它的动力学方程为

$$
{ \frac { \mathrm { d } ^ { 2 } X ^ { \mu } } { \mathrm { d } s ^ { 2 } } } = 0 ,
$$

其中 $X ^ { \mu } { \equiv } ( T , X , Y , Z )$ 是惯性系的闵柯夫斯基坐标，从这里开始，我们将一直采用光速 $c = 1$ 的自然单位制.方程(3.3.1)就是测地线方程.因为闵柯夫斯基度规下克里斯朵夫联络为零，测地线方程才简化成(3.3.1)的形式.我们可以用广义坐标变换来引入非惯性系，它的四维时空坐标记为 $x ^ { \mu }$ ，

$$
x ^ { \mu } = x ^ { \mu } ( X ) .
$$

相应的反变换为

$$
X ^ { \mu } = X ^ { \mu } ( x ) .
$$

上述自由运动的动力学方程(3.3.1)可通过变换化成

$$
\frac { \mathrm { d } ^ { 2 } x ^ { \prime } } { \mathrm { d } s ^ { 2 } } + \Gamma _ { \alpha \beta } ^ { \ast } \frac { \mathrm { d } x ^ { \alpha } } { \mathrm { d } s } \frac { \mathrm { d } x ^ { \beta } } { \mathrm { d } s } = 0 ,
$$

其中

$$
\displaystyle { \cal T } _ { \alpha _ { i } 3 } ^ { \mu } = \frac { \ni ^ { 2 } X ^ { \nu } } { \mathsf { \partial } x ^ { \alpha } \partial x ^ { \beta } } \frac { \ni x ^ { \mu } } { \mathsf { \partial } X ^ { \nu } } .
$$

(3.3.2)式就是非惯性系中的自由粒子的动力学方程.式中第一项是粒子的加速度，第二项是单位质量粒子所受的引力.从这里看出，惯性力场的场强是由黎曼空间的联络描述的.按照等效原理的思想，引力场与惯性力场在物理规律中的地位应是相同的，因此引力场强一般地应由空间的联络描述.我们从上一章知道，联络描述空间的几何结构，现在又看到引力场强也通过联络反映.这种用空间几何来表示引力的想法叫引力的几何化.

我们知道联络是由度规张量的微商构成的.因此，如果讲联络描述了引力场强，那么度规张量就相当于引力势.在牛顿理论中，引力势是一个标量场.按现在的理论，引力势是一个二阶对称张量场，它有10个独立的分量.

当肯定了引力场应由联络描述，它还将引伸出一个重要的推论.

如果时空是平坦的，那么总能找到一组闵柯夫斯基坐标使联络恒为零，即使引力场的效果完全消失.这意味着存在全局性的惯性系.然而经验却表明这种惯性系是不存在的.它推论，现实的物理时空一定是弯曲的黎曼空间.曲率张量必不为零，从而消除全部引力效果是不可能的.

黎曼几何又告诉我们，在弯曲空间中消除任一点的联络是永远可以的.这意味着在任--时空点的无穷邻域中引力效果是近似地可消除的，即近似的局域惯性系是永远可以找到的.这正是等效原理的物理基础.等效原理进一步作出了两个判断：(1)自由下落的局域参考系正是这种参考系；(2)在这种参考系中狭义相对论所肯定的物理规律都成立.这两点判断正是等效原理所蕴含的假设.

# 3.4弱引力场中的自由粒子

已经指出，任意引力场中自由粒子的动力学方程是测地线方程

$$
\frac { \mathrm { d } ^ { 2 } x ^ { \mu } } { \mathrm { d } s ^ { 2 } } = - \Gamma _ { \alpha \beta } ^ { \mu } \frac { \mathrm { d } x ^ { \alpha } } { \mathrm { d } s } \frac { \mathrm { d } x ^ { \beta } } { \mathrm { d } s } .
$$

现在我们论证，当满足条件：

(a）引力场是弱场，即令

$$
g _ { \mu \nu } = \eta _ { \mu \nu } + h _ { \mu \nu } ,
$$

则有

$$
| h _ { \mu \nu } | \ll 1 ,
$$

其中 $\eta _ { \mu \nu }$ 是闵柯夫斯基度规(2.1.8)；

(b）引力场是静态的，即

$$
\{ \ L _ { \mu \nu , \ L _ { 0 } } = h _ { \mu \ L \bullet , \ L _ { 0 } } = 0 ;
$$

(c）引力场是空间缓变的，即

$$
\begin{array} { r } { \{ \xi _ { \mu \nu , i } = h _ { \mu \nu , i } \ll 1 , } \end{array}
$$

此处及此后拉丁指标均为1至3；

（d）粒子的运动是低速的，即

$$
{ \frac { \mathrm { d } x ^ { i } } { \mathrm { d } x ^ { 0 } } } \ll 1 ;
$$

那么测地线方程(3.4.1)将还原到牛顿方程

$$
{ \frac { \mathrm { d } ^ { 2 } x ^ { i } } { \mathrm { d } t ^ { 2 } } } = - { \frac { \mathsf { \partial } \mathsf { \partial } \mathsf { \varphi } } { \mathsf { \partial } { \boldsymbol { x } } ^ { i } } } ,
$$

其中 $\pmb { t } \equiv \pmb { x } ^ { 0 } \cdot \pmb { \varphi }$ 是牛顿引力势.

证明如下.按上述条件1至3,联络 $\Gamma _ { \alpha \beta } ^ { \mu }$ 是小量.保留至一级小量，有

$$
{ \cal { T } } _ { \alpha \beta } ^ { \mu } = \frac { 1 } { 2 } \eta ^ { \prime \prime } { } ^ { \alpha } ( h _ { \rho \alpha , \beta } + h _ { \rho \beta , \alpha } - h _ { \alpha \beta , \rho } ) .
$$

再利用条件4，在(3.4.1)式右边也只保留一级小量，测地线方程简化为：

$$
\frac { \mathrm { d } ^ { 2 } x ^ { 0 } } { \mathrm { d } s ^ { 2 } } = 0 ,
$$

$$
\frac { \mathrm { d } ^ { 2 } x ^ { \prime } } { \mathrm { d } s ^ { 2 } } = - \ F _ { \ 0 0 } ^ { i } \bigg ( \frac { \mathrm { d } x ^ { 0 } } { \mathrm { d } s } \bigg ) ^ { 2 } .
$$

由(3.4.9)式解出

$$
x ^ { 0 } = { \bf i } s + \mathrm { c o n s t . } \ ,
$$

于是(3.4.10)式变成

$$
\frac { \mathrm { d } ^ { \cdot } x ^ { i } } { \mathrm { d } t ^ { 2 } } = \frac { 1 } { 2 } h _ { 0 0 , i } .
$$

这正是牛顿方程(3.4.7)的形式.对比看出牛顿引力势 $\varphi$ 与度规分量 $h _ { 0 0 }$ 的关系为

$$
\varphi = - \mathrm {  ~ \nabla ~ } \frac { 1 } { 2 } h _ { \scriptscriptstyle 0 0 } + \mathrm { c o n s t } \mathrm {  ~ . ~ } .
$$

考虑到无穷远处引力场消失，度规还原到闵柯夫斯基形式，即 $\varphi { = }$ 0处有 $h _ { \scriptscriptstyle ( ) 0 } = 0$ ，则有

$$
\varphi = - \ \frac { 1 } { 2 } h _ { \scriptscriptstyle 0 0 } ,
$$

或写成

$$
g _ { \scriptscriptstyle { 0 0 } } = - 1 + h _ { \scriptscriptstyle { 0 0 } } = - 1 - 2 \varphi .
$$

这证明告诉我们，引力场中的牛顿方程(3.4.7)仅对在静态的、缓变的弱引力场中的自由粒子才适用.而我们又知道，这方程在天体力学中早已在很高的精度上被证实.为看清这两方面没有矛盾，我们具体讨论-个质量为 $M$ 的球状源的引力场.

按牛顿引力理论，球状源的外引力势为

$$
\varphi = - \ { \frac { G M } { r } } ,
$$

其中 $G$ 是牛顿引力常数.当它是弱场时，上述证明说

$$
{ \bf g } _ { \scriptscriptstyle 0 0 } \ { \bf \Psi } = - \ 1 + \frac { 2 G M } { r } .
$$

而弱场条件则表现为

$$
\frac { 2 G M } { r } \ll 1 .
$$

定义 $R _ { g } \equiv 2 G M$ ，叫球状源的引力半径 $\textcircled{1}$ 弱场条件就是

$$
r \gg R _ { { \varepsilon } } ,
$$

即粒子在比引力半径大得多的地方运动.我们来估算一下太阳的引力半径.太阳质量 $M = 2 \times 1 0 ^ { 3 3 } \mathrm { g } .$ 从而算出它的引力半径

$$
R _ { g } = 3 ~ \mathrm { { k m } } .
$$

注意到太阳物理半径是 $7 \times 1 0 ^ { 5 } ~ \mathrm { k m }$ ,看出即使对太阳表面附近运动的粒子，弱场条件(3.4.17)也是足够好地成立的.反之，我们将看到要破坏弱场条件(3.4.17)则是很困难的.

由于牛顿外引力势公式(3.4.14)并不适用于引力源内部区域，所以要实现一个强场，源的几何半径至多略大于它的引力半径 $\textcircled{2}$ ，设源的质量是一个太阳质量的量级，则这时源的物质密度须高达 $2 \times 1 0 ^ { 1 9 } \ \mathbf { k g } \cdot \mathbf { m } ^ { - 3 }$ .实际上，太阳的平均密度是 $1 0 ^ { 3 } \ \mathrm { k g } \cdot \mathrm { m } ^ { - 3 }$ 的量级.白矮星作为演化晚期的致密星，密度也只有 $1 0 ^ { 9 } \mathrm { \sim } 1 0 ^ { 1 2 } \mathrm { k g }$ $\bullet \textrm { m } ^ { - 3 }$ .在观测到的所有星体中，仅有中子星的密度达到了 $1 0 ^ { 1 8 } \mathrm { k g }$ · $\mathbf { m } ^ { - 3 }$ .因此中子星表面(其实也包括内部)的引力场是强场，它不宜用牛顿理论研究.

# 3.5爱因斯坦(Einstein)引力场方程

等效原理推广了引力的概念，并暗示了有引力场的时空是弯曲的黎曼空间，引力场的物理效果可通过黎曼空间的度规张量来体现.为了完成这新的引力理论，需要找到度规场分布的物理规律，即度规场(或叫推广的引力势)所满足的微分方程.可是这方面没有直接可依据的观测知识，所以能采取的途径是作猜测性的推理.

参照牛顿引力理论，我们可以得到这些设想.首先，牛顿引力势的分布取决于静态物质的密度分布，所以度规场应取决于物质的动量能量张量，因为在张量性的物理理论中物质密度是动量能量张量的一个分量.这样我们把度规场方程的数学形式确立为

$$
F _ { \mu \nu } = T _ { \mu \nu } ,
$$

其中 $T _ { \mu \nu }$ 是物质的动量能量张量， $F _ { \mu \nu }$ 是由度规 $g _ { \mu \nu }$ 及其微商构成的张量.其次，牛顿引力方程

$$
\nabla ^ { 2 } \varphi = { 4 \pi G \rho }
$$

是一个引力势的二阶线性偏微分方程，因此我们要求 $F _ { \mu \nu }$ 最高只含$g _ { \mu \nu }$ 的二阶微商，且对二阶微商是线性的.有趣的是黎曼几何中有一条定理 $\textcircled{1}$ ：由度规张量 $g _ { \mu \nu }$ 及其一和二阶微商构成的，对二阶微商为线性的张量只有黎曼张量 $R _ { \mu \nu \lambda } ^ { \rho }$ 及其缩并，此外就是 $g _ { \mu \nu }$ 自身.这一数学定理几乎把上述 $F _ { \mu \nu }$ 完全确定了.

按上述推测和数学定理， $F _ { \mu \nu }$ 最一般只能是

$$
F _ { \mu \nu } = \alpha R _ { \mu \nu } + \beta g _ { \mu \nu } R + \gamma _ { g _ { \mu \nu } } ,
$$

其中 $\alpha , \beta$ 和 $\pmb { \gamma }$ 是任意常参量.注意到能量动量的守恒，它现在表现为 $T _ { \nu } ^ { \mu }$ 的四维协变散度等于零，即

$$
T _ { \nu _ { 3 } \mu } ^ { \mu } = 0 ,
$$

因此 $F _ { \mu \nu }$ 应满足

$$
F _ { \nu _ { \imath } \mu } ^ { \mu } = 0 .
$$

参照公式(2.6.4)以及(2.3.8)，我们看出应取 $\beta = - \alpha / 2$ ,即把 $R _ { \mu \nu }$ 和 $R$ 组合成爱因斯坦张量 $G _ { \mu \nu }$ .这样度规场方程(3.5.1)就取得了具体形式

$$
G _ { \mu } + \lambda g _ { \mu \nu } = - \kappa T _ { \mu \nu } ,
$$

其中 $\pmb { \kappa }$ 叫相对论引力常数，下-节将导出它与牛顿引力常数 $G$ 的关系； $\lambda$ 是唯--剩下的任意参量.最简单的可能是令 $\lambda { = } 0$ ,相应的方程

$$
G _ { \mu \nu } = R _ { \mu \nu } - \frac { 1 } { 2 } g _ { \mu \nu } R = - \ \kappa T _ { , \mu \nu }
$$

叫爱因斯坦引力场方程.

将方程(3.5.6)的指标上升再缩并，得到

$$
R = \kappa T ,
$$

其中 $T { \equiv } T _ { \mu } ^ { \mu }$ 是动量能量张量的迹.把它代入式(3.5.6)再移项，爱因斯坦场方程获得另一等价的表述

$$
R _ { \mu \nu } = \cdots \kappa \Big ( T _ { \mu \nu } - { \frac { 1 } { 2 } } g _ { \mu \nu } T \Big ) .
$$

当 $T _ { \mu \nu } = 0$ ，即处理物质分布区之外的引力场，我们有

$$
R _ { \mu \nu } \ : \approx \ : 0 .
$$

这是真空区的场方程.

# 3.6场方程的牛顿近似

现在我们讨论什么条件下爱因斯坦引力场方程将还原到牛顿引力场方程.为与前节的分析相协调，自然期望相应的条件正是前节的条件1至3.我们来导出这些条件下的爱因斯坦场方程的简化形式.

考虑一片非相对论性理想流体构成的介质 $\textcircled{1}$ ,它在某参考系中为静止介质.由狭义相对论知，非相对论理想流体的动量能量张量为

$$
T ^ { \mu \nu } = \rho u ^ { \mu } u ^ { \nu } ,
$$

其中 $\rho$ 是物质密度， $\pmb { u } ^ { \mu }$ 为介质的四维速度，它定义为

$$
u ^ { \mu } \equiv { \frac { \mathrm { d } x ^ { \mu } } { \mathrm { d } \tau } } ,
$$

而 $\mathbf { d } \tau$ 是固有时，

$$
\mathrm { d } \tau ^ { 2 } = - \mathrm { \ d } s ^ { 2 } = - \mathrm { \ g } _ { \mu \nu } \mathrm { d } x ^ { \mu } \mathrm { d } x ^ { \nu } .
$$

这样 $u ^ { \mu }$ 归一为

$$
g _ { \mu } u ^ { \mu } u ^ { \nu } = - \ 1 .
$$

采用相对介质静止的坐标系， $\pmb { u } ^ { \mu }$ 有形式

$$
{ \pmb u } ^ { \mu } = \frac { 1 } { \sqrt { - { \bf \alpha g } _ { 0 0 } } } ( 1 , 0 , 0 , 0 ) ,
$$

于是看出,动量能量张量的唯一非零分量是

$$
T ^ { \scriptscriptstyle ( ) \scriptscriptstyle ( ) } = - \mathrm { \Lambda } \rho / g _ { \scriptscriptstyle ( 0 0 } .
$$

相应张量的迹为

$$
T ^ { \mathrm { ~ } } = - \mathrm { ~ } T _ { \mu } ^ { \mu } = - \mathrm { ~ } \rho .
$$

然后计算静态、缓变弱场近似下的里契张量 $R _ { \mu \nu }$ .写出

$$
R _ { \mu \nu } = R _ { \nu a } ^ { \dot { \imath } } = { \cal P } _ { \mu \lambda , \dot { \imath } } ^ { \lambda } - { \cal P } _ { \mu \nu , \lambda } ^ { \lambda } + { \cal P } _ { \mu \lambda } ^ { \rho } { \cal T } _ { \nu \rho } ^ { \lambda } - { \cal T } _ { \mu } ^ { \lambda } { \cal T } _ { \lambda \rho } ^ { \rho } .
$$

保留至一级小量，联络 $\Gamma _ { \mu \nu } ^ { \lambda }$ 为

$$
I _ { \mu \nu } ^ { \lambda } = \frac { 1 } { 2 } \eta ^ { \lambda , \rho } ( h _ { \rho \mu , \nu } + h _ { \rho \nu , \mu } - h _ { \mu \nu , \rho } ) .
$$

它的分量可明显地写成

$$
I _ { \mathrm { ~ 0 \ell } } ^ { \mathrm { { \scriptsize ~ 0 } } } = 0 ,
$$

$$
{ \cal { T } } _ { _ { ( ) \prime } } ^ { \prime ) } = - \ { \frac { 1 } { 2 } } h _ { \scriptscriptstyle { ( ) 0 , i } } ,
$$

$$
\Gamma _ { i j } ^ { \mathrm { o } } = \cdots \ : \ : \frac { 1 } { 2 } ( h _ { \mathrm { o } i , j } + h _ { \mathrm { o } j , i } ) ,
$$

$$
{ \cal I } _ { _ { \{ \ \ \ n \} } } ^ { \ast } \ = - \ { \frac { 1 } { 2 } } h _ { _ { 0 0 , i } } ,
$$

$$
I _ { \tiny ( \cdot ) , } ^ { \prime } = \frac { 1 } { 2 } ( h _ { 0 i , . j } - h _ { 0 j , . i } ) ,
$$

$$
I _ { { \bf \Phi } _ { j k } } ^ { \prime } = { \frac { 1 } { 2 } } \{ h _ { \prime , k } + h _ { i k , j } - h _ { j k , i } ) .
$$

因联络分量是一级小量，里契张量(3.6.8)式右边对联络为二次的项可以忽略，即

$$
R _ { \mu \nu } = { \Gamma } _ { \mu \lambda , \nu } ^ { \lambda } - { \Gamma } _ { \mu \nu , \lambda \bullet } ^ { \lambda }
$$

于是得出所述条件下里契张量分量的简化形式

$$
R _ { \mathrm { \scriptsize ( \approx ) } } = \frac { 1 } { 2 } h _ { 0 0 , i , i } ,
$$

$$
R _ { \mathfrak { o } _ { t } } = \frac { 1 } { 2 } ( h _ { \mathtt { k } \mathfrak { o } , i , k } - h _ { \mathfrak { o } i , k , k } ) ,
$$

$$
R _ { i j } = \frac { 1 } { 2 } ( h _ { k k , i , j } - h _ { k i , j , k } - h _ { k j , i , k } + h _ { i j , k , k } ) .
$$

虽然这是非协变形式，我们仍保持重复指标自动求和的约定.

用定义把里契张量换成逆变形式，

$$
R ^ { \mu \nu } \equiv g ^ { \mu \alpha } g ^ { \nu \beta } R _ { \alpha \beta } = \eta ^ { \mu a } \eta ^ { \nu \beta } R _ { \alpha \beta } .
$$

于是看出，在一级近似下有

$$
R ^ { 0 0 } = R _ { \scriptscriptstyle 0 0 } , \quad R ^ { \scriptscriptstyle 0 i } = - R _ { \scriptscriptstyle 0 i } , \quad R ^ { i j } = R _ { i j } .
$$

为导出牛顿近似下的场方程,现在一切都准备好了.我们写出00分量的方程

$$
R ^ { \tiny { 0 0 } } = \dots \star \biggr ( T ^ { \tiny { 0 0 } } - \frac { 1 } { 2 } g ^ { \tiny { 0 0 } } T \biggr ) .
$$

把有关的量代入，得到

$$
h _ { \iota _ { ( 1 ) , i , i } } = - \ \kappa \rho .
$$

利用前节得出的关系，牛顿引力势

$$
\varphi = - \ \frac { 1 } { 2 } h _ { \scriptscriptstyle { 0 0 } } .
$$

这样(3.6.12)可改写成牛顿势 $\varphi$ 的微分方程，

$$
\bigtriangledown ^ { 2 } \varphi = { \frac { 1 } { 2 } } \kappa \rho .
$$

它完全就是牛顿引力理论中的场方程(3.5.2).对比之下定出 $\textcircled{1}$

$$
\kappa = 8 \pi { \cal G } .
$$

至此我们既论证了在适当条件下爱因斯坦场方程以牛顿场方程为近似，而且把场方程(3.5.6)中唯一的参量用实验值确定了.

最后对方程(3.5.5)作一些说明.前已指出，引力场方程中可以添一个 $\lambda _ { g , \mu \nu }$ 形式的项.在牛顿近似下，它将给(3.6.13)式右方加上常数 $\lambda$ ，因此参量 $\lambda$ 必须充分小才能保证牛顿引力理论是足够好的近似.爱因斯坦曾设想，这一项应很小，以至对通常天文尺度上的引力场不起重要作用；而只在宇宙学问题上才有重要作用.这-一项因此得名为宇宙项.爱因斯坦最初利用宇宙项建立了一个稳态的宇宙模型.现在观测表明，宇宙并不是稳态的，因此宇宙学是否必须要这样的项也是一个争论中的问题.

# 3.7 谐和坐标条件

度规张量作为对称张量，它有10个独立分量.爱因斯坦引力场方程

$$
G _ { _ { \tiny { \mathscr { n } } } } = - \ 8 \pi G T _ { _ { \tiny { \mu \nu } } }
$$

初看也是10 个方程，其实不是.由于毕安基恒等式 $G _ { \nu ; \mu } ^ { \mu } { \equiv } 0$ ，场方程只有6个是独立的.这样场方程并不能完全确定 ${ \pmb { g } } _ { \pmb { \mu } \pmb { \nu } }$ 的10个分量. $g _ { \mu \nu }$ 有4个不能为场方程确定的自由度反映一个事实，若 $g _ { \mu \nu }$ 是场方程的解，那么作任意变换 $x {  } x ^ { \prime }$ 后的 $\smash { \boldsymbol { g } ^ { \prime } { \mathbf { \Pi } } _ { \mu \nu } }$ 也是场方程的解，它们所代表的物理情况是一样的.因此，这种不确定性使我们可以对坐标的选择加上4个限制条件.

有---种常被采用的限制条件叫谐和坐标条件，它要求坐标的选择满足

$$
{ \cal { T } } ^ { \ast } \equiv g ^ { \mu \nu } { \cal { T } } _ { \mu \nu } ^ { \lambda } = 0 ,
$$

或利用联络的定义，把上述条件写作

$$
g ^ { \mu \nu } g ^ { \lambda \rho } ( g _ { \rho , \nu } + g _ { \rho , \mu } - g _ { \mu , \rho } ) = 0 .
$$

满足(3.7.1)或(3.7.2)的坐标叫谐和坐标.注意这条件既然是对坐标选择的限制，它当然不是协变的.

谐和的含意是什么？若 $\phi$ 是谐和量意指它满足谐和方程

$$
\begin{array} { r } { \boxed { + } \pmb { \phi } \equiv ( g ^ { \lambda \varphi } \pmb { \phi } _ { ; \lambda } ) _ { ; \rho } = 0 . } \end{array}
$$

可以证明 $\textcircled { 1 }$

$$
\begin{array} { r } { \square \pmb { \phi } = g ^ { \lambda \rho } \frac { \ni ^ { 2 } \phi } { \partial x ^ { \lambda } \partial x ^ { \rho } } - \Gamma ^ { \lambda } \frac { \partial \pmb { \phi } } { \partial x ^ { \lambda } } . } \end{array}
$$

取 $\phi$ 为坐标 $x ^ { \mu }$ ，因为

$$
\frac { \ni ^ { 2 } { x ^ { \prime } } } { \ni x ^ { \lambda } \ni x ^ { \rho } } = 0 ,
$$

便有

$$
\boxed { \begin{array} { r } { \boxed { . } x ^ { \ast } : = - \ r ^ { \ast } \frac { \mathfrak { d } x ^ { \mu } } { \mathfrak { d } x ^ { \lambda } } = - \ r ^ { \mu } . } \end{array} }
$$

这样，若坐标的选取满足 $\Gamma ^ { \mu } = 0$ ,我们有

$$
\square x ^ { \mu } = 0 .
$$

这就是谐和坐标名称的来源.

在没有引力场的情况下采用笛卡儿坐标，使度规具有闵柯夫斯基的形式

$$
g _ { \mu \nu } = \eta _ { \mu \nu } ,
$$

易从(3.7.2)验证它满足谐和坐标条件.因此，谐和坐标可以看作闵柯夫斯基空间中的笛卡儿坐标在有引力场情况下的推广.

在讨论弱引力场下的线性近似理论时用谐和坐标尤为方便.在弱引力场下，我们把度规表示成

$$
{ \it g } _ { \mu \nu } = \eta _ { \mu \nu } + h _ { \mu \nu } ,
$$

并有 $| h _ { \mu \nu } | \ll 1$ .线性近似理论中只保留 $h _ { \mu \nu }$ 的线性项，于是有

$$
\begin{array} { l } { { { \displaystyle { \cal T } _ { \alpha \beta } ^ { \prime \prime } } = \frac { 1 } { 2 } \eta ^ { \mu \nu } ( h _ { \alpha , \beta } + h _ { \beta \nu , \alpha } - h _ { \alpha \beta , \nu } ) } } \\ { { { } } } \\ { { \equiv \frac { 1 } { 2 } ( h _ { \alpha , \beta } ^ { \mu } + h _ { \beta , \alpha } ^ { \prime } - h _ { \alpha \beta } ^ { , \mu } ) . } } \end{array}
$$

注意线性理论中张量指标的升降是借助 $\eta ^ { \mu \nu }$ 和 $\eta _ { \mu \nu }$ 进行的.线性化后的里契张量也很简单.

$$
R _ { , u \nu } = { \Gamma } _ { \mu { \lambda } , \nu } ^ { \lambda } - { \Gamma } _ { \mu \nu , \lambda } ^ { \lambda }
$$

$$
\begin{array} { r l } { \mathrm { ~  ~ \cdot ~ } } & { { } \equiv \displaystyle \frac { 1 } { 2 } ( h _ { \mu , \alpha } ^ { \mathrm { ~ \alpha ~ } } + h _ { , \mu , \nu } \mathrm { ~ \longrightarrow ~ } h _ { \mu , \nu , \alpha } ^ { \mathrm { ~ \alpha ~ } } - h _ { \nu , \mu , \alpha } ^ { \mathrm { ~ \alpha ~ } } ) , } \end{array}
$$

其中

$$
h \equiv h _ { \alpha } ^ { \alpha } = \eta ^ { \alpha \beta } h _ { \alpha \beta } .
$$

为表达引力场方程的方便，我们定义

$$
\overline { { { h } } } _ { \mu \nu } \equiv h _ { \mu \nu } - \frac { 1 } { 2 } \eta _ { \mu } h .
$$

容易证明，它的逆变换是

$$
\overline { { { h } } } _ { \prime \alpha } \equiv \bar { h } _ { \mu } - \frac { 1 } { 2 } \eta _ { \mu \nu } \ : \overline { { { h } } } = h _ { \mu \nu } .
$$

利用 $\widehat { h } _ { \mu \nu }$ ,线性化的场方程

$$
\overline { { { R } } } _ { \mu } \equiv R _ { \mu } \mathrm { ~ -- ~ } \frac { 1 } { 2 } \eta _ { \mu } R = - \mathrm { ~ } 8 \pi G T _ { \mu } ,
$$

具体化为

$$
\overline { { h } } _ { \mu \nu , \alpha } ^ { , \alpha } + \eta _ { \mu \nu } \overline { { h } } _ { \alpha \beta } ^ { , \alpha , \beta } \ - \ \overline { { h } } _ { \mu \alpha , \nu } ^ { , \alpha } \ - \ \overline { { h } } _ { \nu \alpha , \mu } ^ { , \alpha } = - \ 1 6 \pi G T _ { \mu \alpha } .
$$

如果对坐标加上谐和条件的限制，线性化场方程(3.7.13)将简化.谐和条件(3.7.2)线性化后有形式

$$
\overline { { h } } _ { \mu \alpha } ^ { , \alpha } = 0 .
$$

这样(3.7.13)式左边后三项全为零.于是场方程化简为

$$
\bar { h } _ { \mu \nu , \alpha } ^ { , \alpha } = 1 6 \pi G T _ { \mu \nu } .
$$

(3.7.14)和(3.7.15)就是谐和坐标下的线性化引力场方程，它非常类似于电磁学中电磁势的场方程和洛伦兹规范条件.因此（3.7.14)也叫引力势的洛伦兹规范条件.

如同电磁势的洛伦兹规范并没有完全确定电磁势一样，现在引力势的洛伦兹规范也没有完全确定坐标.如果再作坐标变换

$$
x ^ { \prime } \to . { x ^ { \prime } } ^ { . } + \xi ^ { \mu } ,
$$

其中 $\xi ^ { \mu }$ 是 $h _ { \mu \alpha }$ 的同级小量，那么

$$
h _ { \mu \nu } \to h _ { \mu \nu } - \xi _ { \mu , \nu } - \xi _ { \nu , \mu } .
$$

容易验证，只要 $\xi ^ { \mu }$ 满足

$$
\xi _ { \mu , \alpha } ^ { , \alpha } = 0 ,
$$

则变换(3.7.16)将不破坏 $h _ { \mu \nu }$ 的洛伦兹规范性.

最后应注意，在一组确定的坐标下解出 $\overline { { h } } _ { \mu \nu }$ 后，度规场是

$$
g _ { \mu \nu } = \eta _ { \mu \nu } + h _ { \mu \nu } = \eta _ { \mu \nu } + \widetilde { h } _ { \mu \nu } - \frac { 1 } { 2 } \eta _ { \mu \nu } \widetilde { h } .
$$

# \$3.8引力波

在形式上， $\overline { { h } } _ { \mu \nu }$ 所满足的场方程(3.7.15)就是闵柯夫斯基空间中的波动方程.这表明引力场和电磁场一样可以用波的方式辐射和传播，而且引力波的波速就是光速 $c$

我们只讨论引力波的传播.当波在真空中传播时，有 $T _ { \mu \nu } = 0$ ，因而可用 $R _ { \mu \nu } = 0$ 代替(3.7.12)式.波方程(3.7.15)相应改作

$$
h _ { \mu \nu , \sigma } ^ { \cdot \alpha } = 0 ,
$$

洛伦兹规范条件写作

$$
h _ { ; \varkappa } ^ { \ast a } \sim \frac { 1 } { 2 } \eta _ { \mu \alpha } h ^ { ; \alpha } = 0 .
$$

看沿 $_ { x }$ 方向传播的单色平面波

$$
h _ { \mu \nu } = A _ { \mu \nu } \mathrm { e } ^ { \mathrm { i } ( k x \cdot \omega t ) } ,
$$

波方程(3.8.1)决定 $\pmb { k } = = \omega$ 洛伦兹规范条件要求振幅满足

$$
\overline { { { A } } } _ { \mu } ^ { \ i } = \overline { { { A } } } _ { \mu } ^ { \ 0 } ,
$$

其中

$$
\ddot { A } _ { \mu } ^ { \nu } \equiv A _ { \mu } ^ { \nu } - \frac { 1 } { 2 } \delta _ { \mu } ^ { \nu } A _ { \alpha } ^ { \alpha } .
$$

此外,我们用显然满足式(3.7.18)的函数

$$
\xi _ { \mu } = \xi _ { \mu } ^ { ( 0 ) } \mathrm { e } ^ { \mathrm { i } ( k x \cdots \omega t ) }
$$

按(3.7.16)和(3.7.17)式作规范变换.适当选取 $\pmb { \xi } _ { \mu } ^ { ( 0 ) }$ 可以使

$$
\bar { A } _ { 1 } ^ { \prime ) } = \overline { { { A } } } _ { 2 } ^ { 0 } \ = \ \overline { { { A } } } _ { 3 } ^ { 0 } = 0 ,
$$

$$
{ \overline { { { A } } } } _ { 2 } ^ { 2 } + { \overline { { { A } } } } _ { 3 } ^ { 3 } = 0 .
$$

条件(3.8.4)和(3.8.6)使 $\mu { = } 0 , 1$ 或 $\nu { = } 0 , 1$ 的振幅 $\overline { { A } } _ { \mu \nu }$ 都等于零

即振幅只有2,3分量不为零.注意这波是沿 $x ^ { 1 } = = x$ 的方向传播的，因此所用的规范叫横波规范.余下不为零的振幅是

$$
\left\{ \begin{array} { l l } { \bar { A } _ { 2 } ^ { 2 } } & { \overline { { A } } _ { 2 } ^ { 3 } } \\ { \quad \quad } \\ { \bar { A } _ { 3 } ^ { 2 } } & { \overline { { A } } _ { 3 } ^ { 3 } } \end{array} \right\} .
$$

它是对称的，又是无迹的（由于式(3.8.7)），因此只有两个独立的分量.由于 $\stackrel { \scriptscriptstyle - } { A } { } _ { \alpha } ^ { \alpha } = = 0$ ，所以

$$
{ \operatorname { \lrcorner } } 1 _ { \mu \nu } = \overline { { A } } _ { \mu \nu } .
$$

由此得出结论，沿 $x$ 方向传播的平面引力波(3.8.3)的振幅$A _ { \mu \nu }$ 在横向无迹的洛伦兹规范下只有两个独立分量，它可取为 $A _ { 2 3 }$ 和 $A _ { 2 \bar { z } } - A _ { 3 3 }$ ·

# 第四章 观测量的理论

在广义相对论中，我们需要一个理论，用它来说明某一观测者在他的局域参考系中所测到的物理量与张量性物理理论中所得出的物理量之间的关系，这就是观测量的理论·这理论一般是很复杂的，但对于局域的观测，它的含义却是简单明确的，本章要讨论的将限于局域的观测量理论·

# 4.1观测量作为标量

按广义相对论，四维物理时空是一个弯曲的黎曼空间．因此-一般讲，全局性的空间刚架和全局性的统一时间都是不存在的·选定时空坐标系的作用仅是对事件的时空位置提供一种确定的表述，它完全不具有--个全局性参考系的含意，后面我们将看到，即使在局域的意义上，坐标系也不一定能代表一个物理上有意义的参考系．可是从另一方面讲，物理量必须具有可观测性，而任何测量总是与一个确定的观测者的局域参考系相联系的·脱离参考系来谈论测量结果是没有意义的·广义相对论对物理问题的理论研究需要坐标系，任何测量结果都依赖于参考系，但坐标系与参考系--般又并不一致，这三个情况结合在一起就导致了一个问题：在某一坐标系中所得出的张量性的物理量与某一观测者观察同一现象时所测到的物理量之间是什么关系？

在讨论这问题之前，我们先对坐标系和参考系的概念作一澄清．什么是时空坐标系？时空坐标系就是在物理事件的时空位置和四个数构成的数组之间建立一种确定的一一对应关系．有了时空坐标系，这数组的任-确定取值就代表了一个确定的时空点，什么是参考系？由于全局性参考系一般没有意义，我们限于用局域参考系的概念．简单说，一个局域参考系就是指一个按确定方式在时空中运动的观测者所携带的局域刚架和时钟，

在测量问题中我们面对着四个因素：第一是确定的观察对象·这里指的是某物理现象中的某个物理量，第二是事件发生点的时空几何性质．第三是确定的参考系·主要是指按某种已知方式运动的观测者．第四是一个为表述该物理量和该观测者运动情况的坐标系，任一观测结果会依赖于前三个因素，即依赖于观测对象、观测者和观测点的时空几何，这是显然的·需要强调的是观测结果不应依赖于第四个因素，即它应与坐标系无关，例如看两个事件的时间间隔的测量，当前三个因素都已确定时，该观测者就可测得一个确定的数·坐标系的选取虽具有人为的任意性，但当客观情况一经确定，换-种坐标取法将不再改变这个数的大小．这一结论用张量的术语讲，那就是观测量必定是一个标量．后面的实例将帮助我们理解这一点·

# 4.2时空间隔的测量和投影算符

我们讨论在具有确定的几何结构(即度规张量)的时空中的两个事件 $P$ 和 $\boldsymbol { Q }$ ，任意选定坐标系后，事件 $P$ 的时空坐标为 $x ^ { \mu } , Q$ 的时空坐标为 $x ^ { \prime \prime } + \mathbf { d } x ^ { \prime \prime }$ ．我们想知道这两个事件间的时间间隔和空间距离的大小：

从狭义相对论知道，这问题的提法不完整，因为两事件间的时间间隔及空间距离与观测者的运动情况有关，为此我们先给出观测者的运动情况的描述·

在上述同-一坐标系中，观测者的运动由他的四维世界线

$$
x _ { \uparrow \downarrow } ^ { \prime \prime } = x _ { \uparrow \downarrow } ^ { \mu } ( \tau )
$$

来刻画．世界线的切矢量即他的四维速度

$$
u ^ { \mu } = { \frac { \mathrm { d } x _ { \bar { \mathrm { x t } } } ^ { \mu } } { \mathrm { d } \tau } } .
$$

这四维速度 ${ \pmb u } ^ { \mu }$ 是类时矢量，它归一为

$$
g _ { \mu \nu } u ^ { \mu } u ^ { \nu } = - \ 1 .
$$

现在我们才可以问：对这一观测者讲，他测到 $P$ 和 $\mathbf { \delta } _ { \mathbf { Q } }$ 的时间间隔$\Delta T$ 和空间距离 $\Delta L ,$ 有多大？

任一观测者都有权认为自己是静止的，因此他可以把他的世界线的切向当作他的时间轴方向：与时间轴正交的三维子空间就是他的普通空间·被观测事件 $P$ 与 $\mathbf { Q }$ 的时空坐标差 ${ \mathrm { \bf d } } x ^ { \mu }$ 是一个四维矢量·若把这四维矢量往观测者的时间轴上投影，所得到的就是他应测得的 $P$ 与 $\mathbf { Q }$ 的时间间隔，同样，若把这四维矢量往观测者的空间部分投影，所得的矢量的长度就是他应测得的 $P$ 与 $\mathbf { Q }$ 的空间距离，这就是我们关于时空测量的基本观念，问题在于如何引入时间方向和空间部分的投影运算：

我们把时间投影算符定义为

$$
\pi ^ { \mu \nu } \equiv - \ u ^ { \mu } u ^ { \nu } ,
$$

其中 $u ^ { \mu }$ 是观测者的四维速度，相应显然可以有混合的和协变的算符 $\pi _ { \nu } ^ { \mu }$ 及 $\pi _ { \mu \nu }$ ．任一逆变矢量 $A ^ { \mu }$ 在时间轴上的投影定义为

$$
A _ { / / } ^ { \mu } \equiv \pi _ { \nu } ^ { \mu } A ^ { \nu } .
$$

注意，按这样的定义，投影后的 $A _ { \mathrm { { / / } } } ^ { \mu }$ 仍是原空间的四维逆变矢量·

这样定义的 $\pi ^ { \mu \nu }$ 叫作时间投影算符，因为它具有如下两点性质：

(a)对任 $\cdots \ A ^ { \prime \prime }$ ，投影后的 $A _ { / / } ^ { \mu }$ 必平行于时间轴方向 $u ^ { \mu }$ ·

证明：由于

$$
A _ { / \prime } ^ { \mu } = \pi _ { \nu } ^ { \mu } A ^ { \ast } = - \ u ^ { \mu } u , A ^ { \nu } = - \ ( u , A ^ { \nu } ) u ^ { \mu } ,
$$

因此它与 $\boldsymbol { \imath } \iota ^ { \prime }$ 是平行的·

(b)若 $A ^ { \mu }$ 平行于 $u ^ { \prime }$ .则 $A _ { / / } ^ { \mu }$ 就是 $A ^ { \mu }$ 自身·

证明：当 $A ^ { \mu }$ 与 $u ^ { \mu }$ 平行，可令 $A ^ { \mu } { = } C u ^ { \mu }$ 这样

$$
A _ { \mathcal { M } } ^ { \prime } = - ~ ( u , A ^ { \nu } ) u ^ { \mu } = - ~ C ( u , u ^ { \nu } ) u ^ { \mu } = C u ^ { \mu } = A ^ { \mu } .
$$

由这两个性质导出一自然的结果

$$
\pi _ { \nu } ^ { \mu } \pi _ { \lambda } ^ { \nu } = \pi _ { \lambda } ^ { \mu } ,
$$

即投影后再投影等于一次投影。

有了时间投影算符，我们只要把两事件的时空间隔矢量 $\operatorname { d } { x ^ { \mu } }$ 往时间轴上投影，就可以得出该观测者应测得的 $\Delta T$ 了·投影后有

$$
\mathrm { d } \mathscr { x } ^ { \mu } . = \pi _ { \nu } ^ { \mu } \mathrm { d } \mathscr { x } ^ { \nu } .
$$

因它仍是矢量，求它的长度 $\int I$ .即得 $\Delta T$

$$
\begin{array} { r l } & { \Delta T = \sqrt { - { \ g _ { \mu } \mathrm { d } x _ { / / } ^ { \mu } } \ \mathrm { { d } } x _ { / / } ^ { \nu } } \ = \ \sqrt { - { \ g _ { \mu } } { \pi _ { \alpha } ^ { \mu } } { \pi _ { \beta } ^ { \nu } } { \mathrm { d } } x ^ { \alpha } \mathrm { { d } } x ^ { \beta } } } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad = \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad }  \end{array}
$$

从这结果看出 $\Delta T$ 确实是一个标量，亦即与坐标系的选择无关，在不同坐标系下，描述时空几何的 $g _ { \alpha \beta }$ 、描述观测者运动的 $\varkappa ^ { \alpha }$ 及描述事件间隔的 $\mathbf { d } \boldsymbol { x } ^ { \beta }$ 都将不同，但 $\Delta T$ 是一样的，而这正是观测量的客观性所要求的·

下面看两个例子：

例1平坦时空中的静观测者的测量·当用闵柯夫斯基坐标，有

$$
g _ { \mu \nu } \mathrel { \mathop : } = \eta _ { \mu \nu } , \quad u ^ { \mu } = ( 1 , 0 , 0 , 0 ) .
$$

由(4.2.10)立即得出

$$
\Delta T = \mathbf { d } x ^ { 0 } .
$$

这正是--个最平常的结果.

例2平坦时空中沿 $_ { x }$ 方向运动的观测者的测量·这时有

$$
g _ { \mu \nu } = \eta _ { \mu } , \quad u ^ { \mu } = ( u ^ { 0 } , u ^ { 1 } , 0 , 0 ) .
$$

由 $\pmb { u } ^ { \mu }$ 的归一化条件(4.2.3)得出

$$
u ^ { " } = { \frac { 1 } { \sqrt { 1 - v ^ { 2 } } } } , \quad u ^ { 1 } { \frac { v } { \sqrt { 1 - v ^ { 2 } } } } ,
$$

其中 $\upsilon { \equiv } \frac { \mathrm { d } \mathscr { x } _ { \mathfrak { R } } ^ { 1 } } { \mathrm { d } \mathscr { x } _ { \mathfrak { R } } ^ { 0 } }$ 是观测者的速度．代入(4.2.10)式即得

$$
\Delta T = { \frac { \mathrm { d } x ^ { 0 } - v \mathrm { d } x ^ { 1 } } { \sqrt { 1 - { \mathrm {  ~ } } v ^ { 2 } } } } .
$$

这正是洛伦兹变换公式之一．

然后我们转入空间距离的测量问题，为此引入空间投影算符

$$
h ^ { \mu \nu } \equiv g ^ { \mu \nu } + u ^ { \mu } u ^ { \nu } .
$$

任一逆变矢量 $A ^ { \mu }$ 在普通空间部分的投影定义为

$$
A _ { \perp } ^ { \mu } = h _ { \nu } ^ { \mu } A ^ { \nu } .
$$

这投影运算具有如下性质：

（a）对任意 $A ^ { \mu }$ ，投影后的 $A _ { \perp } ^ { \mu }$ 必与时间轴方向 $u ^ { \mu }$ 垂直，即$A _ { \perp } ^ { \mu } u _ { \mu } { = } 0 ;$

(b)若 $A ^ { \mu }$ 与 $\pmb { u } ^ { \prime }$ 垂直，则投影后的 $A _ { \perp } ^ { \mu }$ 等于自身；

(c）若 $A ^ { \mu }$ 与 $u ^ { \mu }$ 平行，则投影后为零；

$( \mathbf { d } )$ 时间投影部分和空间投影部分之和为自身，即

$$
A _ { / / } ^ { \mu } + A _ { \scriptscriptstyle \perp } ^ { \mu } = A ^ { \mu } ;
$$

$( \mathrm { e } ) h _ { \nu } ^ { \prime \prime } h _ { \lambda } ^ { \nu } = h _ { \lambda } ^ { \mu } ;$

$$
( \mathrm { f } ) h _ { \nu } ^ { \prime \prime } \pi _ { \lambda } ^ { \nu } = \pi _ { \nu } ^ { \mu } h _ { \lambda } ^ { \nu } = = 0 .
$$

所有这些性质都很容易从定义直接验证：

计算时空坐标差为 ${ \mathrm { d } } x ^ { \mu }$ 的两事件的空间距离就是把它向空间方向投影，然后求 ${ \mathrm { \bf d } } \boldsymbol { x } _ { \perp } ^ { \mu }$ 的长度．

$$
\begin{array} { r l } & { \Delta L = \sqrt { g _ { \mu \nu } \mathrm { d } x _ { \perp } ^ { \mu } \ \mathrm { d } x _ { \perp } ^ { \nu } } = \sqrt { g _ { \mu \nu } h _ { a } ^ { \mu } h _ { \beta } ^ { \nu } \mathrm { d } x ^ { \alpha } \mathrm { d } x ^ { \beta } } } \\ & { \quad \quad = \sqrt { h _ { a \beta } \mathrm { d } x ^ { a } \mathrm { d } x ^ { \beta } } . } \end{array}
$$

从这结果又一次看出， $\Delta L ,$ 取决于事件的坐标差 $\operatorname { d } { x ^ { \mu } }$ 、观测者的四维速度 $\pmb { u } ^ { \mu }$ 和该点的度规 $g _ { \mu \nu } \Im L$ 是一个标量，它与坐标系无关．从公式(4.2.16)还看到，在三维普通空间中起度规作用的是 $h _ { \mu \nu }$ 而

不是 $g _ { \mu \nu }$ 的空-空分量·

下面看两个空间测量的例子：

例1平坦时空中的静观测者的测量·当用闵柯夫斯基坐标，有

$$
g _ { \mu \nu } = \eta _ { \mu } , \quad u ^ { \mu } = ( 1 , 0 , 0 , 0 ) .
$$

由 $h _ { \mu \nu }$ 的定义(4.2.11)算出

$$
h _ { i j } = \eta _ { i j } , \quad h _ { 0 0 } = h _ { 0 i } = h _ { i 0 } = 0 .
$$

然后(4.2.16)式给出

$$
\Delta L = \sqrt { \eta _ { i j } \mathrm { d } x ^ { i } \mathrm { d } x ^ { j } } ,
$$

这正是欧氏几何中最熟知的结果．

例2平坦时空中沿 $_ { x }$ 方向运动的观测者的测量·这情况下可有

$$
\begin{array} { c c l } { { } } & { { g _ { \mu \nu } = \eta _ { \mu \nu } , } } & { { } } \\ { { u ^ { 0 } = \displaystyle \frac { 1 } { \sqrt { 1 - v ^ { 2 } } } } } & { { \exists \Sigma } } & { { u _ { 0 } = \displaystyle \frac { - 1 } { \sqrt { 1 - v ^ { 2 } } } , } } \\ { { u ^ { 1 } = \displaystyle \frac { v } { \sqrt { 1 - v ^ { 2 } } } } } & { { \exists \Sigma } } & { { u _ { 1 } = \displaystyle \frac { v } { \sqrt { 1 - v ^ { 2 } } } . } } \end{array}
$$

由 $h _ { \mu \nu }$ 的定义算出

$$
h _ { \rho } = \left[ \begin{array} { c c c c } { \displaystyle \frac { v ^ { \prime } } { 1 - v ^ { \prime } } } & { \displaystyle \frac { - v } { 1 - v ^ { 2 } } } & { 0 } & { 0 } \\ { \displaystyle \frac { - v } { 1 - v ^ { \prime } } } & { \displaystyle \frac { 1 } { 1 - v ^ { 2 } } } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 1 } \end{array} \right] .
$$

代入(4.2.16)式,我们即有

$$
\varDelta L ^ { 2 } = \frac { ( \mathrm { d } x ^ { 1 } - v \mathrm { d } x ^ { 0 } ) ^ { 2 } } { 1 - \overline { { { \tau } } } ^ { 2 } } + ( \mathrm { d } x ^ { 2 } ) ^ { 2 } + ( \mathrm { d } x ^ { 3 } ) ^ { 2 } .
$$

这正是洛伦兹变换给出的结果。

最后指出，由(4.2.10)式和(4.2.16)式可得出一个值得注意

的结果：

$$
\begin{array} { r l } & { - \Delta T ^ { 2 } + \Delta L ^ { 2 } = - \ u _ { \alpha } u _ { \beta } \mathrm { d } x ^ { \alpha } \mathrm { d } x ^ { \beta } + ( g _ { \alpha \beta } + u _ { \alpha } u _ { \beta } ) \mathrm { d } x ^ { \alpha } \mathrm { d } x ^ { \beta } } \\ & { \qquad = g _ { \alpha \beta } \mathrm { d } x ^ { \alpha } \mathrm { d } x ^ { \beta } = \Delta s ^ { 2 } . } \end{array}
$$

这结果与平坦时空下的结果一样，可是它却对任意引力场中的任意观测者都适用：

# 4.3物理的坐标系

在任意的物理时空中取定了坐标系 $x ^ { \mu }$ 之后，我们来考虑一种特殊的观测者，它的四维速度是

$$
u ^ { \scriptscriptstyle ( 1 ) } \ne 0 ; \quad u ^ { \scriptscriptstyle ( i ) } = 0 .
$$

这种观测者相对于坐标系是局域静止的，也可以说它相对于坐标系是局域地随动的．由 $u ^ { \mu }$ 的归一条件(4.2.3)定出

$$
{ \pmb u } ^ { 0 } = \frac { 1 } { \sqrt { - \mathrm { \pmb { g } } _ { 0 0 } } } { \bf \cdot }
$$

先以这观测者所携带的时钟的走时为观测对象，这时有 $\mathbf { d } \boldsymbol { x } ^ { i }$ $= 0$ 和 $\mathsf { d } x ^ { \mathsf { C } } \neq 0$ ，结合他自身的四维速度表达式（4.3.1）和（4.3.2），他测得的时间间隔立即由(4.2.10)给出

$$
\Delta T = { \bf \cdots } ~ g _ { 0 0 } u ^ { 0 } { \bf d } x ^ { 0 } = \sqrt { - { \bf \Psi } g _ { 0 0 } } { \bf d } x ^ { 0 } .
$$

这结果其实就是(4.3.2)式．从这结果看到，如果要求观测者相对坐标系局域静止,则该处的 $g _ { 0 0 }$ 必须小于零;这时 $\sqrt { - g _ { 0 0 } }$ 是时钟指示的时间差与时间坐标差之间的比例因子，

再看这观测者在自身邻域的空间距离测量·算出他所适用的普通空间度规为

$$
\begin{array} { r l } & { h _ { \alpha \beta } = g _ { \alpha \beta } + u _ { \alpha } u _ { \beta } = g _ { \alpha \beta } + g _ { \alpha \mu } g _ { \beta \nu } u ^ { \mu } u ^ { \nu } } \\ & { \quad = g _ { \alpha \beta } - ( g _ { \alpha 0 } g _ { \beta 0 } ) / g _ { 0 0 } . } \end{array}
$$

它表明 $\pmb { h } _ { 0 0 } = h _ { 0 i } = h _ { i 0 } = 0$ ,其空-空分量

$$
h _ { i \prime } = g _ { i j } - ( g _ { i 0 } g _ { j 0 } ) / g _ { 0 0 } .
$$

如果时空度规有性质 $g _ { i 0 } = 0$ ，则 $h _ { i j } = g _ { i j }$ ，一般说，从这种局域静止观测者看来，相邻点的距离公式为

$$
\Delta L = \sqrt { h _ { \alpha \beta } \mathrm { d } x ^ { \alpha } \mathrm { d } x ^ { \beta } } = \sqrt { h _ { i j } \mathrm { d } x ^ { i } \mathrm { d } x ^ { j } } .
$$

距离公式(4.3.6)也可以用一个物理上更直观的方法来导出·为测量邻点 $P$ 与 $\boldsymbol { \mathsf { Q } }$ 的空间距离， $P$ 点的静观测者送出一光信号，信号从 $P$ 传至 $\alpha$ 再返回 $P$ 所化的时间的一半乘上光速应该就是 $P$ 与 $\boldsymbol { Q }$ 的空间距离，我们按这样的理解来导出距离公式·

先算信号从 $P$ 至 $\boldsymbol { Q }$ 的传播·设 $P$ 与 $\boldsymbol { Q }$ 的空间坐标差为 $\mathbf { d } \boldsymbol { x } ^ { i }$ ， 传播的时间坐标差为 $\mathrm { d } x _ { \pounds } ^ { 0 }$ ．因光的传播满足 $\mathbf { d } s ^ { 2 } = 0$ ，所以有

$$
g _ { \mathfrak { d o } } ( d x _ { \mathfrak { d } } ^ { \circ } ) ^ { 2 } + 2 g _ { \mathfrak { d i } } \mathrm { d } x _ { \mathfrak { L } } ^ { \circ } \mathrm { d } x ^ { i } + g _ { i j } \mathrm { d } x ^ { i } \mathrm { d } x ^ { j } = 0 .
$$

解出

$$
\mathbf { d } x _ { \pm } ^ { 0 } = \frac { 1 } { - g _ { 0 0 } } ( g _ { 0 i } \mathbf { d } x ^ { \prime } + \sqrt { ( g _ { 0 i } g _ { 0 j } - g _ { 0 0 } g _ { i j } ) \mathbf { d } x ^ { i } \mathbf { d } x ^ { j } } ) .
$$

再同样算信号从 $\mathbf { \boldsymbol { Q } }$ 至 $P$ 的返回．这时空间坐标差应为一 $\mathrm { d } \boldsymbol { x } ^ { i }$ ，传播的时间坐标差为 $\mathrm { d } \mathscr { x } _ { [ \bar { \mathtt { g } } ] } ^ { 0 }$ ，相应解出的结果是

$$
\mathsf { d } x _ { \mathsf { f i } } ^ { \flat } = \frac { 1 } { - g _ { 0 \ell } } ( - g _ { 0 i } \mathsf { d } x ^ { \prime } + \sqrt { ( g _ { 0 i } g _ { 0 j } - g _ { 0 0 } g _ { i j } ) \mathsf { d } x ^ { i } \mathsf { d } x ^ { j } } ) .
$$

信号从 $P$ 传出再返回 $p$ 所化的时间是

$$
\begin{array} { r } { \Delta T = \sqrt { { { \cdots } _ { g _ { 0 } } } } ( \mathbf { d } x _ { \pm } ^ { 0 } + \mathbf { d } x _ { \{ \mp \} } ^ { 0 } ) . } \end{array}
$$

注意在我们的单位制中光速 ${ \dot { c } } = 1$ ，所以 $\Delta L ,$ 就是 $\Delta T / 2$ ，最后得到的距离公式是

$$
\begin{array} { r } { \Delta L = \sqrt { \left( \left. g _ { * j } - \frac { g _ { 0 i } g _ { 0 j } } { g _ { 0 0 } } \right| \right) \mathbf { d } x ^ { i } \mathbf { d } x ^ { j } } . } \end{array}
$$

它与用投影运算得出的(4.3.6)式是完全一样的·

我们强调指出，距离公式(4.3.6)的得出是以存在局域静止观测者为前提的，如果这前提在物理上能实现，那么他测得的 $\Delta L$ 应总是实数．这也就是要求 $h _ { i j } \mathbf { d } x ^ { i } \mathbf { d } x ^ { j }$ 是一个正定的二次型，把对

$h _ { i j }$ 的要求转化为对时空度规 $g _ { \mu \nu }$ 的要求，它可表述为

$$
g _ { \mathrm { 0 c } } < 0 ,
$$

$$
\left| \begin{array} { l l } { { g _ { \boldsymbol { \imath } \boldsymbol { \imath } } } } & { { { \bf g } _ { \boldsymbol { \imath } \boldsymbol { \imath } } } } \\ { { g _ { \boldsymbol { \imath } \boldsymbol { \imath } } } } & { { g _ { \boldsymbol { \imath } \boldsymbol { \imath } } } } \end{array} \right| < 0 ,
$$

$$
\left| { \begin{array} { l l l } { g _ { 0 0 } } & { g _ { 0 1 } } & { g _ { 0 2 } } \\ { g _ { 1 0 } } & { g _ { 1 : } } & { g _ { 1 2 } } \\ { g _ { 2 0 } } & { g _ { 2 : } } & { g _ { 2 2 } } \end{array} } \right| < 0 ,
$$

$$
\left| { \begin{array} { l l l l } { g _ { \ast \ast } } & { g _ { 0 1 } } & { g _ { 0 2 } } & { g _ { 0 3 } } \\ { g _ { \ast \ast } } & { g _ { 1 1 } } & { g _ { 1 2 } } & { g _ { 1 3 } } \\ { g _ { \ast \ast } } & { g _ { 2 1 } } & { g _ { 2 2 } } & { g _ { 2 3 } } \\ { g _ { 3 \ast } } & { g _ { 3 1 } } & { g _ { 3 2 } } & { g _ { 3 3 } } \end{array} } \right| < 0 .
$$

这些条件叫物理的坐标系条件，反之，若这些条件之一不成立，则所用的坐标系是非物理的，意指一个物理的观测者不可能相对这坐标系局域静止．这正是在 $\$ 4.1$ 中指出的，即使局域地看，坐标系也不一定能代表一个物理上有意义的参考系．可是注意，这样的坐标系在广义相对论中是允许采用的·

最后说明两点弯曲时空与平坦时空的差别·

(a)时间对准问题，两相邻点 $P$ 与 $\boldsymbol { \mathsf { Q } }$ 的时间对准可通过光信号的传播来做到：上面算出 $\mathrm { d } \boldsymbol { x } _ { \mathtt { E } } ^ { 0 } \neq \mathrm { d } \boldsymbol { x } _ { \mathtt { E } } ^ { 0 }$ 说明 $P$ 与 $\boldsymbol { \mathrm { \Delta } } \boldsymbol { \mathrm { \Delta } } \boldsymbol { \mathrm { \Delta } } \boldsymbol { \mathrm { \Omega } }$ 的时间一般没有对准．以 $P$ 为基准， $\boldsymbol { Q }$ 点所需的修正量是

$$
\Delta x ^ { \circ } = \mathrm { ~ \stackrel { d } { \iota } ~ } \frac { x _ { \ast } ^ { \circ } } { 2 } - \mathrm { d } x _ { \ast } ^ { \circ } = - \mathrm { ~ \frac { \displaystyle g _ { \theta i } d { \cal } x ^ { i } } { \displaystyle g _ { \circ \flat } } . }
$$

如果想用逐点调准的方法来对准有限远处的时间，那必须要求（4.3.11)式的积分与空间路径无关，对于弯曲时空，这一般是不成立的，因此在广义相对论中通常不能建立全局性的统一时间·从(4.3.11)式又看出，如果度规有性质 $g _ { 0 i } { \equiv } 0$ ，那么坐标时不仅可以对准而且已经对准了：

(b)有限距离问题，静止观测者测得的相邻点间的空间距离$\Delta I ,$ 也叫两点间的固有距离·如果要对有限间隔的两点间的三维曲线定义固有距离，那就要涉及对 $\Delta L$ 的表达式(4.3.6)的积分，可是由于度规 ${ \pmb { \xi } } _ { \pmb { \mu } } ( { \pmb { \xi } } )$ 一般依赖于 $x ^ { \prime }$ ，为积分就失去了确切的意义．因此在广义相对论中，空间距离的概念对相邻点有确切的定义，对有限间距点通常没有确切的定义．有一类重要特例，即 $g _ { \mu \nu }$ 与 $x ^ { 0 }$ 无关，这时有限曲线的长度可由积分得到确定值·

# 4.4 四轴系和局域测量的一般概念

前面我们以观测者的世界线的切向为基准来建立他的参考系，这样自然地把他的四维时空分隔成了相互正交的两部分，平行于世界线切向的一维叫他的时间，垂直于这方向的三维叫他的空间．现在我们再在他的三维空间中引入三个两个正交的类空轴，它与时间轴合在一起就叫观测者的四轴系，这四轴系构成了观测者的一个完整的局域参考系·任何局域的张量性物理量都可以通过向四轴系的投影，使每一分量获得确切的测量意义·

设观测者的世界线的切矢量为 $u ^ { \mu }$ ．我们把它叫四轴系的第零轴，记为

$$
\omega _ { 0 } ^ { \prime } \equiv u ^ { \prime } ,
$$

这里把轴指标0加上符号“ $\Lambda ^ { \textit { \textbf { * } } }$ ,以表明它不是张量指标．第零轴是类时轴，即它归为

$$
g _ { \mu } \omega _ { 0 } ^ { \alpha } \omega _ { 0 } ^ { \nu } = - 1 .
$$

现在我们再引入三个两两正交的类空轴 $\omega _ { z } ^ { \prime } , a = 1 , 2 , 3$ 并让它们归一为

$$
g _ { \prime ^ { a } } \omega _ { a } ^ { \prime } \ \omega _ { \prime } ^ { \prime } : = \ \left\{ \begin{array} { l l } { 1 , } & { \exists \ : a = b ; } \\ { 0 , } & { \exists \ : a \neq b . } \end{array} \right.
$$

这些轴都与时间轴正交，即

$$
\ Z n \omega _ { \alpha } ^ { \prime } \ \omega _ { 0 } ^ { \prime } = 0 .
$$

这样我们就有了一个四轴系 $\omega _ { \alpha } ^ { \ast } , \alpha = 0 , 1 , 2 , 3 .$ ，四轴系的正交归一

性(4.4.2)至(4.4.4)可合并表示成

$$
g _ { \mu } \omega _ { \alpha } ^ { \mu } \ \omega _ { \beta } ^ { \nu } = \eta _ { \alpha \beta } ,
$$

其中 $\eta _ { \alpha \beta }$ 是闵柯夫斯基度规·注意，四轴系的第零轴是由观测者的运动情况决定的，而第-、二和三轴的选取有一定的任意性·

为运算方便，我们用闵柯夫斯基度规来定义轴指标 $\overset { \wedge } { \alpha }$ 的上升和下降，即

$$
\omega ^ { { \stackrel { \wedge } { \alpha } } { \mu } } \equiv \eta ^ { \alpha \beta } \omega _ { \beta } ^ { \mu } \ .
$$

这样，例如正交归一条件(4.4.5)就可等价地写成

$$
\omega _ { \mu } ^ { \hat { \alpha } } \omega _ { \beta } ^ { \mu } = \delta _ { \beta } ^ { \alpha } .
$$

四轴系在四维时空中显然具有完备性，即任一矢量(逆变的或协变的)都可用这组基矢的线性组合来构成，例如

$$
A ^ { \prime } = A ^ { \stackrel { \wedge } { \alpha } } \omega _ { \alpha } ^ { \mu } \ .
$$

这里的系数 $A ^ { \stackrel { \wedge } { \alpha } }$ 是矢量 $A ^ { \prime \prime }$ 在第 $\pmb { \alpha }$ 轴上投影的大小．利用正交归一条件(4.4.7)，得出

$$
A ^ { \stackrel { \wedge } { \alpha } } = A ^ { \prime \prime } \omega _ { \mu } ^ { \hat { \alpha } } .
$$

(4.4.9)式显示出 $\boldsymbol { A } ^ { \stackrel { \wedge } { \alpha } }$ 在坐标变换下是标量，即它的值与坐标选取无关，因此具有可观测性：把(4.4.9)代回(4.4.8)式，得到

$$
\therefore \mathbb { \ H } ^ { \mu } = ( \omega _ { \alpha } ^ { \mu } \omega _ { \nu } ^ { \Lambda } ) A ^ { \nu } .
$$

因为它对任何 $A ^ { \mu }$ 都成立，所以有

$$
\omega _ { \alpha } ^ { \prime } \omega _ { \nu } ^ { \alpha } = \delta _ { \nu } ^ { \prime \prime } ,
$$

它叫四轴系的完备性条件．正交归一条件和完备性条件是四轴系的最基本的性质·

有了四轴系就可以讨论对任一张量性物理量的测量·问题仅在于对任意阶张量来确立一种投影运算．从(4.4.9)式看出，求矢量的投影大小就是把它与某轴基矢作内乘，对任意阶张量，我们可以对它的每一张量指标按类似的方法来投影，例如看动量能量张量 $T ^ { \mu \nu }$ ，它通过两个指标的两次投影得到

$$
T ^ { \prime } { } ^ { \stackrel { \prime } { \epsilon } } { } ^ { \stackrel { \wedge } { \beta } } = T ^ { \mu \nu } \omega _ { \mu } ^ { \stackrel { \wedge } { \alpha } } \omega _ { \nu } ^ { \stackrel { \wedge } { \beta } } .
$$

这 $T ^ { \frac { \Lambda } { \alpha } \sharp }$ 包含 $4 ^ { 2 }$ 个数，或叫 $4 ^ { 2 }$ 个四轴系分量·从坐标系的角度看，它们都是与坐标变换无关的标量·这些标量构成了这观测者对张量性物理量 $T ^ { \mu \nu }$ 的独立可观测量，当 $T ^ { \mu \nu }$ 是对称张量时， $T ^ { \frac { 1 } { \alpha } \frac { \lambda } { \beta } }$ 也是对称的，因此独立可观测量的个数与张量独立分量的个数是一致的，可观测量的大小取决于观测对象 $T ^ { \mu \nu }$ ,也取决于观测者的四轴系，可是与坐标系的选取却无关．这正是 $\ S \ 4 . 1$ 中叙述过的道理·

举几个应用的例子·

例1平坦时空中的静观测者的测量，即有

$$
g _ { \mu \nu } = \eta _ { \mu } , \quad \omega _ { 0 } ^ { \prime \prime } = u ^ { \mu } = ( 1 , 0 , 0 , 0 ) .
$$

我们把三个类空轴取作

$$
\omega _ { 1 } ^ { \mu } = \left( 0 , 1 , 0 , 0 \right) , \quad \omega _ { 2 } ^ { \mu } = \left( 0 , 0 , 1 , 0 \right) , \quad \omega _ { 3 } ^ { \mu } = \left( 0 , 0 , 0 , 1 \right) .
$$

这四轴系显然满足正交归…条件和完备性条件．对于张量性物理量 $T ^ { \mu \nu }$ ,它的可观测量是

$$
T ^ { \because \dag } = T ^ { \ast \nu } \omega _ { \mu } ^ { \wedge } \omega _ { \nu } ^ { \wedge } .
$$

利用

$$
\omega _ { \mu } ^ { \stackrel { \wedge } { \alpha } } { } ^ { ~ \dotsc } ~ g _ { \mu \nu } \eta ^ { \alpha \beta } \omega _ { \beta } ^ { \stackrel { \nu } { \alpha } } = \delta _ { \mu } ^ { \alpha } ,
$$

得到

$$
T ^ { \wedge \alpha \beta } \ { } ^ { * } \ { } ^ { * } \ { } ^ { * } \ { } ^ { * } \ { } ^ { * } \delta _ { \mu } ^ { \alpha } \delta _ { \nu } ^ { \beta } \ = \ T ^ { * } { } ^ { \alpha \beta } .
$$

可见张量 $T ^ { \mu \nu }$ 的分量本身就是可观测量．这就是狭义相对论中的观测量理论．或者说，它表明狭义相对论不需要一个观测量理论，因为用狭义相对论处理时所用的坐标系与观测者所用的参考系是自然地统一的·

例2弯曲时空中的静观测者所测得的能量密度·

某观测者所测到的能量密度应是动量能量张量在他的时间轴上的两次投影 $\pmb { T } ^ { \dag \mathparagraph 0 }$ ，观测者的时间轴基矢是

$$
\omega _ { \scriptscriptstyle 0 } ^ { \mu } = { \frac { 1 } { \sqrt { - \mathrm { \small ~ \displaystyle ~ } g _ { 0 0 } } } } ( 1 , 0 , 0 , 0 ) ,
$$

相应有

$$
\omega _ { \mu } ^ { \hat { 0 } } = \eta ^ { 0 \beta } g _ { \mu \alpha } \omega _ { \beta } ^ { \hat { 0 } } = - \ g _ { \mu \nu } \omega _ { 0 } ^ { \hat { \wedge } } = - \ \frac { g _ { \mu 0 } } { \sqrt { - \ g _ { 0 0 } } } .
$$

于是

$$
T ^ { ^ { \wedge } _ { 0 } ^ { \wedge } , } = T ^ { \wedge \prime \prime } \omega _ { \mu } ^ { \wedge } \omega _ { \nu } ^ { \wedge } = \frac { - \ g _ { \mu 0 } g _ { \nu 0 } } { g _ { 0 0 } } T ^ { \mu \nu } .
$$

可见在弯曲时空中，即使对相对坐标系静止的观察者， $T ^ { \ d _ { 0 0 } }$ 也不具有能量密度的含义．这正是广义相对论中需要观测量理论的原因：

例3任意度规场中任意观测者的时空间隔测量·

设观测者的四轴系为 $\omega _ { \lambda } ^ { \mu }$ ，被观测事件的时空坐标间隔为 ${ \mathrm { d } } x ^ { \mu }$ 易写出这观测者所测得的时空间隔为

$$
\begin{array} { r l } & { \Delta T \equiv { \mathrm { d } } x ^ { \hat { \ddot { \jmath } } } = { \mathrm { d } } x ^ { \mu } \omega _ { \mu } ^ { \hat { \hat { \imath } } } , \quad \Delta X \equiv { \mathrm { d } } x ^ { \hat { \imath } } = { \mathrm { d } } x ^ { \mu } \omega _ { \mu } ^ { \hat { \hat { \imath } } } , } \\ & { \Delta Y \equiv { \mathrm { d } } x ^ { \hat { \ddot { \jmath } } } = { \mathrm { d } } x ^ { \mu } \omega _ { \mu } ^ { \hat { \hat { \imath } } } , \quad \Delta Z \equiv { \mathrm { d } } x ^ { \hat { \ddot { \imath } } } = { \mathrm { d } } x ^ { \mu } \omega _ { \mu } ^ { \hat { \hat { \ast } } } . } \end{array}
$$

对比用(4.2.16)算出的 $\varDelta I .$ ，易证明

$$
\Delta L ^ { 2 } : = \Delta X ^ { 2 } + \Delta Y ^ { 2 } + \Delta Z ^ { 2 } .
$$

值得注意，这结果好像说空间是平坦的，但实际上我们处理的空间是弯曲的·原因在于第二章 $\ S \ 2 . 1$ 中叙述过的数学定理，当限于讨论弯曲空间中的-点·总可以适当取坐标，使不变距离由一般的二次型化简为平方和．这完全不表明空间是平坦的，平坦性的特征在于能够同时把…个区域内的度规场化为欧氏型或闵柯夫斯基型·我们所讨论的局域测量理论始终只涉及弯曲时空中的一个点，此外又适当地选用了两两正交的四轴系，因此它会表观地显现出某些类似平坦空间的特征，

# 4.5两个观测者的测量的比较

我们来比较两个不同的观测者 $u , k$ （分别以他们的四维速度$u ^ { \mu } , k ^ { \mu }$ 来标志)观测同一个事件间隔 $\mathrm { ~ d } x ^ { \mu }$ 所得的结果．

观测者 $\pmb { u }$ 的四轴系记为 $\omega _ { \alpha } ^ { \mu }$ ，按上节的例3,他测得的时空间隔为

$$
\mathbf { \Sigma } _ { u } \mathrm { d } x \hat { \pmb { \alpha } } = \mathrm { d } x ^ { \mu } \omega _ { \mu } ^ { \hat { \alpha } } .
$$

类似地把观测者 $\pmb { k }$ 的四轴系记为 $\lambda _ { \alpha } ^ { \mu }$ ，他测得的时空间隔为

$$
\mathbf { \Sigma } _ { k } \mathrm { d } x ^ { \hat { \alpha } } = \mathrm { d } x ^ { \mu } \lambda _ { \mu } ^ { \hat { \alpha } } .
$$

由(4.5.1)式解出

$$
\begin{array} { r } { \mathrm { d } \boldsymbol { x } ^ { , \mu } = \mathbf { \nabla } _ { u } \mathrm { d } \boldsymbol { x } _ { \alpha } ^ { \wedge } \omega _ { \alpha } ^ { \mu } , } \end{array}
$$

代入(4.5.2)式得到

$$
\mathbf { \Sigma } _ { k } \mathbf { d } \boldsymbol { x } ^ { \hat { \alpha } } = \mathbf { \Sigma } _ { u } \mathbf { d } \boldsymbol { x } ^ { \hat { \beta } } \mathbf { \Sigma } ( \omega _ { \beta } ^ { \mu } \mathbf { \Sigma } \lambda _ { \mu } ^ { \hat { \alpha } } ) .
$$

从而看到两组观测结果是由线性变换相联系的，变换矩阵为

$$
A _ { \underset { \beta } { \uparrow } } ^ { \underset { \alpha } { \uparrow } } = \omega _ { \underset { \beta } { \uparrow } } ^ { \mu } \lambda _ { \mu } ^ { \underset { \alpha } { \uparrow } } ,
$$

它仅取决于两个四轴系，而不依赖于坐标系．

下面我们分析两者测得的时间间隔的关系，

$$
_ { \boldsymbol { \mathsf { A } } } \mathrm { d } \boldsymbol { x } ^ { \hat { \boldsymbol { \imath } } } = \boldsymbol { A } _ { \boldsymbol { \imath } } ^ { \hat { \boldsymbol { \imath } } } _ { \boldsymbol { \imath } } \mathrm { d } \boldsymbol { x } ^ { \hat { \boldsymbol { \imath } } } + \boldsymbol { A } _ { \boldsymbol { \alpha } \boldsymbol { u } } ^ { \hat { \boldsymbol { \imath } } } \mathrm { d } \boldsymbol { x } ^ { \hat { \boldsymbol { \alpha } } } .
$$

按(4.5.4),

$$
A _ { \lambda } ^ { ^ { \wedge } } = \omega _ { \partial } ^ { \mu } \ \lambda _ { \mu } ^ { ^ { \wedge } } = - \omega _ { \beta } ^ { \mu } \ k _ { \mu } = - \ k _ { \tilde { \beta } } ^ { \wedge } ,
$$

其中 $k$ 是 $k _ { \mu }$ 在四轴系 $\omega _ { \beta } ^ { \mu }$ 上的投影，即 ${ \pmb u }$ 所测到的 $k$ 的四维速度的四轴系分量．利用

$$
\eta _ { a , 3 } k ^ { \stackrel { \wedge } { \alpha } } k ^ { \stackrel { \wedge } { \beta } } = - 1 ,
$$

以及

$$
k ^ { \stackrel { \wedge } { \alpha } } = k ^ { \stackrel { \wedge } { 0 } } v ^ { \stackrel { \wedge } { \alpha } } ,
$$

其中 $\boldsymbol { v } ^ { \wedge }$ 是从 $\pmb { u }$ 看 $\pmb { k }$ 的三维普通速度的 $\overset { \wedge } { \alpha }$ 轴分量·我们有

$$
k ^ { \stackrel { \wedge } { 0 } } = { \frac { 1 } { \sqrt { 1 - v ^ { 2 } } } } ,
$$

其中 $_ { \pmb { v } }$ 是从 $\pmb { u }$ 看 $k$ 的三维速率，回到(4.5.6)式,就可以写出变换系数

$$
A _ { \circ } ^ { \wedge } = \textrm { -- } k _ { \circ } = k ^ { \wedge } = \frac { 1 } { \sqrt { 1 - { v ^ { 2 } } } } ,
$$

$$
A _ { \alpha } ^ { \stackrel { \wedge } { 0 } } = - \ k _ { \alpha } ^ { \wedge } = - \ k ^ { \wedge } = \frac { - \ v ^ { \wedge } } { \sqrt { 1 - \ v ^ { 2 } } } .
$$

把这结果代入(4.5.5)式，得到

$$
\mathsf { \Pi } _ { \mathsf { A } } \overset { \wedge } { \boldsymbol { x } ^ { \hat { 0 } } } = \frac { \mathsf { \Pi } _ { \mathsf { a } } \mathsf { d } \boldsymbol { x } ^ { \hat { 0 } } - \boldsymbol { v } ^ { \hat { \mathsf { \Pi } } } \mathsf { \Pi } _ { \mathsf { a } } \mathsf { d } \boldsymbol { x } ^ { \hat { \mathsf { \Pi } } } } { \sqrt { 1 - \boldsymbol { v } ^ { 2 } } } .
$$

这是以瞬时相对速度 $\boldsymbol { v } ^ { \stackrel { \wedge } { a } }$ 所作的洛伦兹变换．其他三个四轴系分量的变换公式也是瞬时洛伦兹变换公式，这里不再重复了，

注意两个观测者的四轴系一般是非惯性系．可是测量结果只依赖观测者的瞬时速度和类空轴的瞬时取向，观测者的加速度及空间轴的转动在这种测量中得不到反映·这使它显示出某种与惯性系类似的行为·

# 4.6 局域惯性系条件

作为本章最后一节，我们简单涉及一下四轴系的运动,以说明在什么条件下四轴系才是一个局域的惯性系．

考虑某时空区域内有一类时的曲线族,即区域内每一时空点都属于一条曲线,该曲线的切向量 $u ^ { \mu }$ 是类时的归一化矢量

$$
g _ { \mu \nu } u ^ { \mu } u ^ { \nu } = - \ 1 .
$$

这样每一曲线代表一个运动着的观测者．一般说这种观测者的运动是加速的，它的四维加速度矢量定义为

$$
\dot { u } ^ { \prime \prime } \equiv u ^ { \prime \prime } , u ^ { \prime } .
$$

对每一个观测者规定-个随动的四轴系,因此四轴系基矢是时空点的函数

$$
\omega _ { \alpha } ^ { \prime \prime } = \omega _ { \alpha } ^ { \prime } \ ( \boldsymbol { x } ) .
$$

每一点上的基矢都满足正交归一条件

$$
g _ { \prime \prime } \omega _ { \alpha } ^ { \prime } \ \omega _ { \beta } ^ { \nu } = \eta _ { \alpha \beta } ,
$$

以及完备性条件：

现在我们讨论四轴系基矢在观测者运动过程中的变率．四轴系作为观测者的局域参考系，它的基矢的变率是否为零正是这局域参考系是否为惯性系的标志，

把轴基矢的变率按自身的轴基矢展开，

$$
\begin{array} { r } { \tilde { \omega } _ { \alpha } ^ { \prime \prime } \equiv \omega _ { \alpha _ { 3 } \nu } ^ { \prime } u ^ { \nu } = \Omega _ { \alpha _ { 3 } } ^ { \wedge } \omega ^ { \wedge } { } ^ { \prime } \omega ^ { \prime } { } ^ { \prime } , } \end{array}
$$

其中 $\Omega _ { \alpha \beta } ^ { \wedge }$ 是标量，我们将用它作为判断某局域参考是否为惯性系的可观测的依据：

首先来证明，由于四轴系在运动过程中保持正交归一性，所以$\Omega _ { a , \hat { \beta } } ^ { \wedge }$ 必是反称的，把(4.4.5)式对参量 $\tau$ 求微，得

$$
\begin{array} { r l } & { g _ { \mu \nu } \dot { \omega } _ { \alpha } ^ { \mu } \omega _ { \gamma } ^ { \nu } + g _ { \mu \nu } \omega _ { \alpha } ^ { \prime \prime } \dot { \omega } _ { \beta } ^ { \nu } } \\ & { \quad = g _ { \mu \nu } \Omega _ { \alpha } ^ { \wedge } \hat { \omega } ^ { \prime \prime } \omega _ { \beta } ^ { \nu } + g _ { \mu \nu } \omega _ { \alpha } ^ { \prime \prime } \Omega _ { \beta } \hat { \omega } ^ { \hat { \gamma } _ { \nu } } } \\ & { \quad = \Omega _ { \alpha } ^ { \wedge } \hat { \gamma } \partial _ { \beta } ^ { \gamma } - \Omega _ { \beta } \hat { \gamma } \partial _ { \alpha } ^ { \gamma } = \Omega _ { \alpha } ^ { \wedge } \hat { \beta } + \Omega _ { \beta } ^ { \wedge } \hat { \alpha } = 0 . } \end{array}
$$

这就是 $\varOmega _ { \textit { \Phi } _ { \textit { \Phi } } ^ { \backslash } \mathscr { \hat { s } } }$ 的反称性，因此它只包含6个独立的标量·

为看清这6个标量的物理意义，把(4.6.4)式写开，当 $\alpha = 0$ ，

$$
\begin{array} { r } { \dot { \pmb { \omega } } _ { \uparrow \uparrow } ^ { \prime \prime } = \dot { \pmb { u } } ^ { \prime \prime } \circ \cdot \pmb { \Omega } _ { 0 } ^ { \wedge } \hat { \pmb { \beta } } \pmb { \omega } ^ { \hat { \beta } \prime \prime } = \Omega _ { 0 } ^ { \wedge } \hat { \pmb { \alpha } } ^ { \wedge } \pmb { \omega } ^ { \hat { \alpha } \mu } , } \end{array}
$$

这里利用了 $\varOmega _ { \mathrm { ~ 0 ~ } \mathrm { { ( i ) } ~ = 0 } } ^ { \wedge \wedge \varOmega }$ ·由此得出

$$
\Omega _ { \scriptscriptstyle  { \tiny + } } ^ { \scriptscriptstyle  { \tiny + } } = \dot { \bar { u } } ^ { \mu } \omega _ { \alpha \mu } ^ { \wedge } \equiv \dot { u } _ { \alpha } ^ { \wedge } .
$$

它说明三个标量 $\Omega _ { \Uparrow \alpha } ^ { \wedge \wedge } ( a = 1 , 2 , 3 )$ 是观测者的四维加速度在自身的类空轴上的三个投影：然后在(4.6.4)式中取 $\alpha = 1 , 2 , 3$ ，利用结果(4.6.7)，有

$$
\begin{array} { r c l } { { } } & { { } } & { { \dot { \omega } _ { a } ^ { \mu } = 2 \lambda _ { a } ^ { \wedge } \stackrel { \wedge } { \omega } { } ^ { 0 } { } ^ { \mu } + \Omega _ { a } ^ { \wedge } \stackrel { \wedge } { \omega } { } ^ { \hat { b } \mu } } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { = \dot { \bar { u } } _ { a } ^ { \wedge } u ^ { \mu } + \Omega _ { a } ^ { \wedge } \stackrel { \wedge } { \omega } { } ^ { \hat { b } \mu } . } } \end{array}
$$

这正是一个有平动又有转动的普通矢量的变率公式.（4.6.8)右边第一项是类空轴随观测者平动所造成的变率，第二项是类空轴在随观测者运动时轴向的转动带来的变率，类空的三个轴基矢$\omega ^ { \overset { \wedge } { \alpha } \beta }$ 的三维转动角速度为

$$
\Omega ^ { \stackrel { \wedge } { \iota } } = { \frac { 1 } { 2 } } \varepsilon ^ { a b c } \Omega _ { b } ^ { \wedge } \stackrel { \wedge } { \cdot } ,
$$

其中

$$
\begin{array} { r } { \varepsilon ^ { a b c } = \left\{ \begin{array} { l l } { \mathrm { ~ l ~ } , } & { a , b , c \textnormal {  { \ -- } } 1 , 2 , 3 \mathrm { ~ } \forall \Sigma \backslash \mathbb { H } \xrightarrow { \mathrm { m a } } \Sigma \backslash \mathcal { H } \mathrm { ~ t ~ } , } \\ { \mathrm { ~ } 0 , } & { a , b , c \mathrm { ~ } \mathcal { D } \gg \mathrm { l y } \mathcal { H } \uparrow \uparrow \mathrm { ~ } \uparrow \mathrm { - } \lambda \mathrm { H } \xrightarrow { \mathrm { m a } } \xi , } \\ { \mathrm { ~ - ~ } 1 , } & { a , b , c \mathrm { ~ } \Xi \mathrm { ~ l } , 2 , 3 \mathrm { ~ } \dot { \mathrm { H } } \mathrm { ~ } \Sigma \backslash \Xi \mathrm { ~ t ~ } . } \end{array} \right. } \end{array}
$$

当观测者沿测地线运动，即在引力场中自由运动，我们有 $\dot { u } ^ { \ \mu }$ $= 0$ ,即

$$
\Omega _ { \textsc { \tiny 0 } _ { \textsc { \tiny a } } } ^ { \mathrm { ~ \tiny ~ \backslash ~ } } = \ 0 .
$$

上面分析表明，这观测者的参考系还不一定是局域惯性系，因为它的三个空间轴可能有转动．如果

$$
\Omega _ { a } ^ { \wedge } \dot { \bf \omega } _ { b } ^ { \ast } = 0 ,
$$

即三个空间轴都不转动，这参考系叫费米平动参考系，现在的结论是：自由下落的费米平动参考系才构成一个局域的惯性系·

# 第五章 球对称的引力场

球对称物体的引力场是引力理论中最有用的一类情形，著名的牛顿引力定律直接刻画的正是这种引力场·现在我们以广义相对论的引力理论为基础来求解球对称的引力场·

# $\$ 5.1$ 球对称度规场的一般结构

度规场是由 $g _ { \mu \nu }$ 的10个独立分量描述的，每一分量都是时空坐标 $x ^ { \mu }$ 的四元函数．考虑到 $g _ { \mu \nu }$ 所满足的爱因斯坦场方程是一组非线性的偏微分方程组，因此度规场的求解一般说在数学上是一个很复杂的问题，如果所研究的对象具有某种几何对称性，度规场的结构就可以得到简化．现在我们要讨论的是球对称引力源的度规场，在用场方程求解之前，我们先分析一下场的球对称性能使它的结构化简到什么程度，

度规场的空间球对称性意味着能找到三个两两正交的对称轴，绕其中任一轴的无穷小转动都保持度规场不变．用等度规映射和凯林矢量场的概念讲，绕这些轴转动的映射构成等度规映射，转动映射的生成元是凯林矢量场·我们取以这些轴向为基准的类笛卡儿坐标， $( \boldsymbol { x } ^ { \flat } \cdot \boldsymbol { x } ^ { \flat } , \boldsymbol { x } ^ { \flat } , \boldsymbol { x } ^ { \flat } )$ ·度规写成

$$
\mathrm { d } s ^ { 2 } = g _ { 0 0 } ( \mathrm { d } x ^ { 0 } ) ^ { \cdot } + 2 g _ { 0 i } \mathrm { d } x ^ { 0 } \mathrm { d } x ^ { \prime } + g _ { i j } \mathrm { d } x ^ { i } \mathrm { d } x ^ { j } .
$$

回忆无穷小映射的形式是

$$
\tilde { z } ^ { \prime \prime } = x ^ { \prime \prime } + \varepsilon \xi ^ { \mu } ,
$$

其中 $\sum ^ { \mu , \nu }$ 叫生成元，ε是无穷小参量，写出绕 $x ^ { 1 }$ 轴转动的生成元为

$$
{ \sf \sf \sf { \sf \sf { \sf { \sf { \sf { \sf { \sf { \sf { \sf { \Lambda } } } } } } } } } } = { \sf { \sf { \sf { \sf { \sf { \sf { \sf { \sf { \Lambda } } } } } } } } } ^ { 1 } = 0 , \quad { \sf { \sf { \sf { \sf { \sf { \sf { \sf { \sf { \Lambda } } } } } } } } ^ { 2 } } = x ^ { 3 } , \quad { \sf { \sf { \sf { \sf { \sf { \sf { \sf { \sf { \Lambda } } } } } } } } ^ { 3 } } = - x ^ { 2 } ,
$$

无穷小参量 $\varepsilon$ 代表转过的角度，这生成元可统一地表述为

$$
\xi _ { ( 1 ) } ^ { \mu } = \delta _ { 2 } ^ { \mu } x ^ { 3 } - \delta _ { 3 } ^ { \mu } x ^ { 2 } .
$$

同样绕 $x ^ { 2 }$ 和 $x ^ { 3 }$ 轴转动映射的生成元可类似地写作

$$
\begin{array} { l } { { \hat { \xi } _ { ( 2 ) } ^ { \mu } = \delta _ { 3 } ^ { \mu } x ^ { 1 } - \delta _ { 1 } ^ { \mu } x ^ { 3 } , } } \\ { { { } } } \\ { { \hat { \xi } _ { ( 3 ) } ^ { \mu } { = } \delta _ { 1 } ^ { \mu } x ^ { 2 } - \hat { \sigma } _ { 2 } ^ { \mu } x ^ { 1 } . } } \end{array}
$$

度规场的球对称性说明这三个转动映射的生成元都是凯林矢量，它们都应当满足凯林方程

$$
g _ { \mu \nu , \rho } \xi ^ { \rho } + g _ { \mu \rho } \xi _ { , \nu } ^ { \rho } + g _ { \nu \rho } \xi _ { , \mu } ^ { \rho } = 0 .
$$

注意，现在凯林矢量 $\hat { \xi } _ { ( \mathrm { ~ l ~ } ) } ^ { \mu } , \hat { \xi } _ { ( \mathrm { ~ 2 ~ } ) } ^ { \mu }$ 和 $\xi _ { ( 3 ) } ^ { \mu }$ 已经确定，因此凯林方程限制了度规场 $g _ { \mathbf { \alpha } ^ { \mathbf { \alpha } } }$ 的结构，而我们的目的正是要找出满足这些限制条件的度规场的一般结构：

这些限制条件中有三个方程只涉及度规分量 $g _ { \boldsymbol { \Theta } 0 0 }$ ，它们是

由 $\xi _ { ( \mathrm { ~ l ~ } ) } ^ { \mu }$ 得 由 $\xi _ { ( 2 ) } ^ { \prime \prime }$ 得 由 $\xi _ { ( 3 ) } ^ { \prime }$ 得

$$
\begin{array} { r l } & { \mathcal { L } _ { 0 0 , 2 } x ^ { 3 } - g _ { 0 0 , 3 } x ^ { 2 } = 0 , } \\ & { \mathcal { L } _ { 0 0 , 3 } x ^ { 1 } - g _ { 0 0 , 1 } x ^ { 3 } = 0 , } \\ & { \mathcal { L } _ { 0 0 , 1 } x ^ { 2 } - \mathcal { E } _ { 0 0 , 2 } x ^ { 1 } = 0 . } \end{array}
$$

形式上引用三维矢量记号 $\pmb { r } = ( \mathcal { x } ^ { 1 } , \mathcal { x } ^ { 2 } , \mathcal { x } ^ { 3 } )$ 及 $\nabla = \left( { \frac { \ \mathsf { \partial } \mathsf { \partial } } { \mathsf { \partial } x ^ { \mathrm { 1 } } } } , { \frac { \mathsf { \partial } \mathsf { \partial } \mathsf { \partial } } { \mathsf { \partial } x ^ { \mathrm { 2 } } } } , { \frac { \mathsf { \partial } \mathsf { \partial } \mathsf { \partial } } { \mathsf { \partial } x ^ { \mathrm { 3 } } } } \right)$ 上述方程写作

$$
\begin{array} { r } { \nabla g _ { \mathfrak { o o } } \times r = 0 . } \end{array}
$$

不难看出， $g _ { 0 0 }$ 作为 $x ^ { \mu }$ 的四元函数的最一般形式只能是

$$
g _ { \scriptscriptstyle { \mathrm { ( ) 0 } } } = F ( r , x ^ { \scriptscriptstyle \mathrm { ( ) } } ) ,
$$

其中 $r = { \sqrt { ( { x } ^ { 1 } ) ^ { 2 } + ( { x } ^ { 2 } ) ^ { 2 } + ( { x } ^ { 3 } ) ^ { 2 } } } , F$ 是任意函数．这就是球对称性对 $g _ { \scriptscriptstyle ( ) 0 }$ 提出的限制·

凯林方程组中有九个方程只涉及度规分量 ${ \pmb { g } } _ { 0 } ;$ ,写出三个如下

$$
\begin{array} { r l } & { ( \nabla g _ { \mathfrak u _ { 1 } } \times \pmb { r } ) _ { \mathfrak u } = 0 , ( \nabla g _ { 0 1 } \times \pmb { r } ) _ { 2 } = - \ \pmb { g } _ { 0 3 } , } \\ & { ( \nabla g _ { \mathfrak u _ { 1 } } \times \pmb { r } ) _ { \mathfrak u } = \pmb { g } _ { 0 2 } . } \end{array}
$$

其他六个方程可用指标的循环替换得到，这组方程的一般解具有形式

$$
\begin{array} { r } { g _ { 0 i } = G ( r , x ^ { \flat } ) x ^ { i } , } \end{array}
$$

其中 $G$ 是任意函数．这就是球对称性对 $g _ { 0 i }$ 的限制，此外还有18

个方程对度规场的空-空分量提出了限制，它要求 $g _ { i j }$ 必须具有如下的形式

$$
g _ { i j } = A ( r , x ^ { 0 } ) { \hat { \partial } } ^ { \prime } + B ( r , x ^ { 0 } ) x ^ { i } x ^ { j } ,
$$

其中 $A$ 和 $B$ 是任意函数·

把上面的结果代回（5.1.1)，我们得到球对称度规的一般结构为

$$
\begin{array} { r l } & { \mathrm { d } s ^ { 2 } = F ( r , x ^ { 0 } ) ( \mathrm { d } x ^ { 0 } ) ^ { 2 } + 2 G ( r , x ^ { 0 } ) x ^ { i } \mathrm { d } x ^ { i } \mathrm { d } x ^ { 0 } } \\ & { ~ + ~ A ( r , x ^ { 0 } ) \mathrm { d } x ^ { \prime } \mathrm { d } x ^ { i } + B ( r , x ^ { 0 } ) ( x ^ { i } \mathrm { d } x ^ { i } ) ^ { 2 } } \end{array}
$$

其中只包含有四个任意的二元函数，从(5.1.8)式的形状看出，如采用普通的空间球坐标 $( r , \theta , \varphi )$ 代替 $( x ^ { 1 } , x ^ { 2 } , x ^ { 3 } )$ 将更为方便．这变换给出

$$
x ^ { i } \mathbf { d } _ { x ^ { \prime } } = r \mathbf { d } r ,
$$

$$
\mathrm { d } x ^ { \prime } \mathrm { d } x ^ { \prime } = \mathrm { d } r ^ { 2 } + r ^ { 2 } ( \mathrm { d } \theta ^ { 2 } + \sin ^ { 2 } \theta \mathrm { d } \varphi ^ { 2 } ) .
$$

于是(5.1.8)式可重新整理成

$$
\begin{array} { r l } & { \mathrm { d } s ^ { \scriptscriptstyle - 4 } = F ( r , t ) \mathrm { d } t ^ { \scriptscriptstyle 2 } + I . ( r , t ) ( \mathrm { d } \theta ^ { \scriptscriptstyle 2 } + \sin ^ { 2 } \theta \mathrm { d } \varphi ^ { \scriptscriptstyle 2 } ) } \\ & { ~ + ~ M ( r , t ) \mathrm { d } r ^ { \scriptscriptstyle - } + N ( r , t ) \mathrm { d } r \mathrm { d } t , } \end{array}
$$

其中 $t \equiv x ^ { \dagger }$ ．它仍包含四个任意的二元函数，

利用坐标的任意性，(5.1.11)式还能化简：作一坐标变换，让$t , \theta$ 和 $\varphi$ 不变而用 $\widetilde r$ 代替 $\gamma$ ：

$$
\begin{array} { r } { \hat { \boldsymbol r } ^ { 2 } ~ = ~ : ~ L ( \boldsymbol r , t ) . } \end{array}
$$

为简单起见，变换后的 $r$ 仍写作 $_ r$ ，度规的结构简化成

$$
\begin{array} { r l } & { \mathrm { d } s ^ { z } = f ( r , t ) \mathrm { d } t ^ { \acute { z } } + r ^ { 2 } ( \mathrm { d } \theta ^ { 2 } + \sin ^ { 2 } \theta \mathrm { d } \varphi ^ { 2 } ) } \\ & { ~ . + ~ m ( r , t ) \mathrm { d } r ^ { 2 } + n ( r , t ) \mathrm { d } r \mathrm { d } t . } \end{array}
$$

若再做一坐标变换，让 $r , \theta$ 和 $\varphi$ 不变而用 $\widetilde { t }$ 代替 $t$ ，以使 $\mathrm { d } \mathscr { r } \mathrm { d } \widetilde { t }$ 的系数为零，则度规的结构中就只包含两个任意的未知函数了．这样化简后的度规通常被写成

$$
\mathbf { d } s ^ { 2 } = - \mathbf { \nabla } \mathrm { e } ^ { \nu ( r , u ) } \mathrm { d } t ^ { 2 } + \mathrm { e } ^ { \mu ( r , u ) } \mathrm { d } r ^ { 2 } + r ^ { 2 } ( \mathrm { d } \theta ^ { 2 } + \sin ^ { 2 } \theta \mathrm { d } \varphi ^ { 2 } ) .
$$

它就是充分化简后的球对称度规的一般形式·

至此我们只考虑了度规场的几何对称性和坐标选取的任意性，所以不可能把度规完全确定下来．其中的任意函数 $\mu ( r , t )$ 和$\nu ( r , t )$ 须由度规场的动力学规律，即由爱因斯坦引力场方程来确定：

# 5.2席瓦西尔(Schwarzschild)外部解

爱因斯坦引力场方程确立后，席瓦西尔首先求出了真空场方程

$$
R _ { \mu \nu } = 0
$$

的一个稳定的球对称解，它描述的是静止球对称引力源外部的引力场，因此正是牛顿引力定律的相对论对应·

采用球坐标 $( x ^ { 0 } , x ^ { . 1 } , x ^ { 2 } , x ^ { 3 } ) = ( t , r , \theta , \varphi )$ ，由上节的(5.1.13)式知，度规分量有形式

$$
\begin{array} { r l } & { { g } _ { 0 0 } = - \mathrm { \bf ~ e } ^ { \nu } , } \\ & { { g } _ { 1 1 } = \mathrm { \bf ~ e } ^ { \mu } , } \\ & { { g } _ { 2 2 } = r ^ { 2 } , } \\ & { { g } _ { 3 3 } = r ^ { 2 } \mathrm { s i n } ^ { 2 } \theta , } \end{array}
$$

所有非对角分量为零．由 $g ^ { \mu }$ 的定义(2.2.3)解出

$$
\begin{array} { r l } & { { g } ^ { \mathrm { 0 0 } } = - \mathrm { \nabla } \mathrm { e } ^ { - \nu } , } \\ & { { g } ^ { \mathrm { 1 1 } } = \mathrm { e } ^ { - \mu } , } \\ & { { g } ^ { \mathrm { 2 2 } } = \frac { 1 } { r ^ { 2 } } , } \\ & { { g } ^ { \mathrm { 3 3 } } = \frac { 1 } { r ^ { 2 } \mathrm { s i n } ^ { 2 } \theta } , } \end{array}
$$

所有非对角分量也为零，现在引力源是静止的，因此它的引力场也应当与 $t$ 无关．这里待求的 $\dot { \mu }$ 和 $\nu$ 都只是 $r$ 的函数，下面我们用场方程(3.5.9)来求解这两个函数，