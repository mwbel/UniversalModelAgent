因此，由 $( 4 \cdot 5 1 )$ 式可得

$$
\operatorname* { l i m } _ { \boldsymbol { \rho } \to \infty } | \boldsymbol { \rho } ^ { 2 } \frac { \partial \mathbf { V } } { \partial \boldsymbol { \rho } } | = \mathbf { f } \mathbf { M }
$$

fM是质体的总质量与引力常数的乘积，它是一个有限的数值。因此，综合(4·47）、（4·49)和 $( 4 \cdot 5 2 )$ 式可知，质体引力位是在无穷远处的正则函数。

# 4.质体对外部点的引力位满足拉普拉斯方程

所谓满足拉普拉斯方程就是存在如下的关系：

$$
\frac { \partial ^ { 2 } \mathrm { V } } { \partial \mathbf { x } ^ { 2 } } + \frac { \partial ^ { 2 } \mathrm { V } } { \partial \mathbf { y } ^ { 2 } } + \frac { \partial ^ { 2 } \mathrm { V } } { \partial \mathbf { z } ^ { 2 } } = 0
$$

这说明，质体引力位对直角坐标系的三个坐标轴的二阶偏导数之和等于零。 $( 4 \div 5 3 )$ 式左端通常用符号 $\Delta \mathbf { V }$ 表示之，因此拉普拉斯方程又可写为

$$
\Delta \mathsf { V } = 0
$$

其中 $\pmb { \triangle }$ 称为拉普拉斯算子。只需对质体引力位进行求导就可证明这一性质的存在。

设 $\mathbf { d m }$ 的坐标为 $( \xi , \eta , \zeta )$ ，则有

$$
\mathbf { r } = { \sqrt { ( \mathbf { x } - { \dot { \bar { \xi } } } ) ^ { 2 } + ( \mathbf { y } - \pmb { \eta } ) ^ { 2 } + ( \mathbf { z } - \pmb { \zeta } ) ^ { 2 } } }
$$

由此可得

$$
\frac { \cdot } { \partial \mathbf { x } } ( \frac { \cdot } { \mathrm { ~ \mathbf ~ { r } ~ } } ) = - \frac { \mathbf { x } - \xi } { \mathrm { ~ \mathbf ~ { r } ~ } } \qquad \frac { \partial } { \partial \mathrm { y } } ( \frac { 1 } { \mathrm { ~ \mathbf ~ { r } ~ } } ) = - \frac { \mathbf { y } - \eta } { \mathrm { ~ \mathbf ~ { r } ~ } } \qquad \frac { \partial } { \partial \mathrm { z } } ( \frac { 1 } { \mathrm { ~ \mathbf ~ { r } ~ } } ) = - \frac { z - \zeta } { \mathrm { ~ \mathbf ~ { r } ~ } }
$$

再求一次导数，得到

$$
\begin{array} { r } { \frac { \partial } { \partial \mathbf { x } ^ { 2 } } ( \frac { 1 } { \textbf { r } } ) = - [ \frac { 1 } { \mathbf { r } ^ { 3 } } - \frac { 3 ( \mathbf { x } - \hat { \mathbf { \varepsilon } } ) ^ { 2 } } { \mathbf { r } ^ { 5 } } ] } \\ { \frac { \partial ^ { 2 } } { \partial \mathbf { y } ^ { 2 } } ( \frac { 1 } { \textbf { r } } ) = - [ \frac { 1 } { \mathbf { r } ^ { 3 } } - \frac { 3 ( \mathbf { y } - \boldsymbol { \eta } ) ^ { 2 } } { \mathbf { r } ^ { 5 } } ] } \\ { \frac { \partial ^ { 2 } } { \partial z ^ { 2 } } ( \frac { 1 } { \textbf { r } } ) = - [ \frac { 1 } { \mathbf { r } ^ { 3 } } - \frac { 3 ( z - \boldsymbol { \xi } ) ^ { 2 } } { \mathbf { r } ^ { 5 } } ] } \end{array}
$$

因而有

$$
\begin{array} { r l } & { \Delta \mathbf { V } = \mathbf { f } \underset { ( \mathbf { M } ) } { \int } [ \frac { \partial } { \partial { \mathbf { x } } ^ { 2 } } ( \frac { 1 } { \tau } ) + \frac { \partial } { \partial { \mathbf { y } } ^ { 2 } } ( \frac { 1 } { \tau } ) + \frac { \partial } { \partial { z } ^ { 2 } } ( \frac { 1 } { \tau } ) ] \mathrm { d } { \mathbf { m } } } \\ & { \quad \quad = - \mathbf { f } \underset { ( \mathbf { M } ) } { \int } \{ \frac { 3 } { { \mathbf { r } } ^ { 3 } } - \frac { 3 } { { \mathbf { r } } ^ { 5 } } \big [ ( { \mathbf { x } } - { \hat { \mathbf { \xi } } } ) ^ { 2 } + ( { \mathbf { y } } - \eta ) ^ { 2 } + ( z - \zeta ) ^ { 2 } \big ] \} \mathrm { d } { \mathbf { m } } } \end{array}
$$

依据 $( 4 \cdot 5 5 )$ 式， $( 4 \cdot 5 6 )$ 式中方括号内的值为 $\scriptstyle \mathbf { r } ^ { 2 }$ ，因为对外部点 $\pmb { r }$ 不可能为零，故被积函数为零,所以 $\Delta \mathbf { V } = 0$ 。

# 5.质体对内部点的引力位满足布桑方程

当被吸引点在质体内时，由于r可能为零,就不能从(4·56)式求出△V的结果了，需要用别的方法求之。

先在质体内作一半径R很小的球，它小到球内的物质密度可视为一个常数D,并将被吸引点P(x,y,z)包含在其中,见图4.10,它与球心相距一个微小的距离p,且p<R。设球心O的坐标为 $( \mathbf { x } ^ { \prime } , \mathbf { y } ^ { \prime } , \mathbf { z } ^ { \prime } )$ ，则

$$
\rho { } = { } \sqrt { ( \mathbf { x } - \mathbf { x } ^ { \prime } ) ^ { 2 } + ( \mathbf { y } - \mathbf { y } ^ { \prime } ) ^ { 2 } + ( \mathbf { z } - \mathbf { z } ^ { \prime } ) ^ { 2 } }
$$

这样，质体对 $\mathbf { P }$ 点的引力位 $\mathbf { v }$ 是两部份质体引力位之和，即

$$
\mathbf { V } { = } \mathbf { V } _ { 1 } { + } \mathbf { V } _ { 2 }
$$

![](images/67e0eb1080dbc565931b9f9f92fd7dcee7633daf06ce72e436764c017921b1f4.jpg)  
图4.10

$\mathbf { v _ { i } }$ 是均质小球的引力位，因为 $\mathbf { P }$ 在球内，故 $\mathbf { V } _ { 1 }$ 的计算式为$( 4 \cdot 4 2 )$ 式，即

$$
\mathrm { V _ { 1 } } { = } \frac { 2 } { 3 } \pi \mathrm { f D } ( 3 \mathrm { R } ^ { 2 } { - } \rho ^ { 2 } )
$$

$\mathtt { V } _ { 2 }$ 为质体其余部份的引力位，此时 $\mathbf { P }$ 是外部点，满足拉普拉斯方程 $\Delta \mathrm { V } _ { 2 } { = } 0$ 。因此有

$$
\Delta \mathsf { V } = \Delta \mathsf { V } _ { 1 }
$$

由 $( 4 \cdot 5 8 )$ 式可得

$$
\frac { \partial \mathrm { V } _ { 1 } } { \partial \mathbf { x } } = \frac { \mathrm { d } \mathrm { V } _ { 1 } } { \mathrm { d } \rho } \frac { \partial \rho } { \partial \mathrm { X } } = - \mathrm { \frac { 4 } { 3 } } \pi \mathrm { f D } \rho \mathrm { \frac { \partial \rho } { \partial \mathbf { x } } }
$$

从 $( 4 \cdot 5 7 )$ 式可以求得·

$$
\frac { \partial \rho } { \partial \alpha } { = } \frac { \alpha - \alpha ! } { \rho }
$$

因而有

$$
\frac { \partial \nabla _ { 1 } } { \partial \mathbf { x } } { = } - \frac { 4 } { 3 } \pi \mathbf { f } \mathrm { D } ( \mathbf { x } - \mathbf { x } ^ { \prime } ) .
$$

则二次偏导数为

$$
\frac { \mathcal { F } \mathrm { V } _ { 1 } } { \partial \mathbf { x } ^ { 2 } } { = } { \mathrm { - } } \frac { 4 } { 3 } \pi \mathrm { f D }
$$

同样可以求得

$$
\frac { \partial ^ { 2 } \mathsf { V } _ { 1 } } { \partial \mathbf { y } ^ { 2 } } { = } \frac { \partial ^ { 2 } \mathsf { V } _ { 1 } } { \partial \mathbf { z } ^ { 2 } } { = } { - } \frac { 4 } { 3 } \pi \mathbf { f } \mathbf { D }
$$

所以有

$$
\Delta \mathbf { V } _ { 1 } = { \frac { \partial ^ { 2 } \mathbf { V } _ { 1 } } { \partial \mathbf { x } ^ { 2 } } } + { \frac { \partial ^ { 2 } \mathbf { V } _ { 1 } } { \partial \mathbf { y } ^ { 2 } } } + { \frac { \partial ^ { 2 } \mathbf { V } _ { 1 } } { \partial { \boldsymbol { z } } ^ { 2 } } } = - 4 \pi \mathbf { f } \mathbf { D }
$$

代入 $( 4 \cdot 5 9 )$ 式，得到

$$
\Delta \mathbf { V } = - 4 \pi \mathbf { f } \mathbf { D }
$$

$( 4 \cdot 6 0 )$ 式称为布桑方程，式中的 $\mathbf { D }$ 是质体在研究点处的物质体密度。

实际上，拉普拉斯方程 $( 4 \cdot 5 4 )$ 可以看作是布桑方程用于 $\mathbf { D } { = } 0$ 处的一个特例。因为当研究点位于质体外时，那里没有质量，也就是密度为零，因而 $\boldsymbol { \triangle } \mathbf { V }$ 也为零。

从上面的论证中看到，质体引力位的二阶导数与研究点处的密度有关。因此，如果密度不连续变化，必将导致质体引力位的二阶导数产生不连续。

# 84.5单层引力位的性质

单层引力位及其一阶导数在层面以外的空间是有限和连续的，单层引力位在无穷远处是正则的，并且满足拉普拉斯方程。这些性质的证明可以运用类似于质体引力位所采取的方法来实现，这里不再重覆。但当被吸引点在层面上时，由于r出现等于零的情况，需要另作讨论。

先讨论均质圆平面层的引力位和引力。如图4.11所示，有一半径为a、面密度为8的圆平面层o,以其圆心O为坐标原点设置直角坐标系，XOY面与圆平面层重合,Z轴与圆平面层正交。今欲求该平面层对点P(0,0,z)和P'(0,0,-z)的引力位和引力。若在XOY平面内采用平面极坐标(l,0),则有do=ldldθ和r=√²+z,因此平面层对P点的引力位为

$$
{ \bf V } _ { \mathrm { p } } = { \bf f } \hat { \otimes } \int _ { 0 } ^ { 1 2 \pi } \frac { l \mathrm { d } l \mathrm { d } \theta } { \sqrt { l ^ { 2 } + z ^ { 2 } } }
$$

完成积分运算后得到

$$
\therefore V _ { P } = 2 \pi \mathbf { f } \& \sqrt { \mathbf { a } ^ { 2 } + \mathbf { z } ^ { 2 } } - \mathbf { z } \mp 
$$

显然,对于P'点有Vp'=Vp。当P点和P'点沿Z轴移动时,引力位值也随之变化。而当.z=0时，都可求得V=2xf8a，这说明均质圆平面层的引力位在通过层面时是连续的。

![](images/2bededb5beb9ec47d5fa197a6c617842d64059e16578302a3dace5709d7c58ab.jpg)  
图4.11

由 $( 4 \bullet 6 1 )$ 式可以求得圆平面层对 $\mathbf { P }$ 点的引力为

$$
F _ { \mathrm { P } } = \frac { \mathrm { d } \mathrm { V } _ { \mathrm { p } } } { \mathrm { d } z } { = } 2 \pi \mathrm { f } \delta [ \frac { z } { \sqrt { a ^ { 2 } + z ^ { 2 } } } { - } 1 ] ( 4 \cdot 6 2 )
$$

该式右端方括号中的第一项总是小于1的，这说明P点所受的引力实际上是与Z轴的正方向相反的。而圆平面层对P'的引力为

$$
\mathrm { F _ { P } } ^ { \prime } = - \frac { \mathrm { d } \mathrm { V _ { p } } ^ { \prime } } { \mathrm { d } z } { = } - \frac { \mathrm { d } \mathrm { V _ { p } } } { \mathrm { d } z }
$$

故由 $( 4 \cdot 6 1 )$ 式可得

$$
\mathbf { F } _ { \mathrm { P } } ^ { \prime } = - 2 \pi \mathbf { f } \& [ \frac { \mathbf { z } } { \sqrt { \mathbf { a } ^ { 2 } + \mathbf { z } ^ { 2 } } } - 1 ]
$$

${ \pmb { \mathrm { F } } } _ { \pmb { \mathrm { p } } ^ { \prime } }$ 总是大于零，说明 $\bar { \mathbf { P ^ { \prime } } }$ 点所受引力与乙轴同向。

当 $\mathbf { P }$ 点沿 $z$ 轴往下移至无限接近于层面上的 $\mathbf { o }$ 点时， $\pmb { z }$ 值变得很小很小，由 $( 4 \cdot 6 2 )$ 式可得

$$
F _ { \mathrm { p } } = - 2 \pi \hbar 
$$

而当 $\mathbf { P ^ { \prime } }$ 点沿Z轴往上移至无限接近于层面上的 $\boldsymbol { 0 }$ 点时，由于 $\pmb { z }$ 值很小很小，由 $( 4 \cdot 6 3 )$ 式可得

$$
{ \bar { \mathbf { F } } } _ { \mathbf { P } } ^ { \prime } { = } 2 \pi { \mathbf { \ell } } \delta
$$

而当被吸引点位于层面的O点时，层面对它的引力等于零。这个现象说明，均质圆平面层的引力在通过层面时是不连续的。

现在对任意形状和密度分布的层面进行讨论。如图4.12所示，设研究点将从P点通过层面，则以P为中心作一半径很小的圆,它将层面(o)分为两部份：一部份是这个圆所围的部份，

它的面积极小，以致可视为均质圆平面层 $( \sigma _ { 0 } )$ ；另一部份就是 $\sigma - \sigma _ { 0 }$ 。若以 $\mathbf { v } _ { z }$ 表示 $( \pmb { \sigma } _ { 0 } )$ 的引力位， $\mathbf { V _ { 1 } }$ 表示 $\sigma - \sigma _ { 0 }$ 的引力位，则整个单层的引力位 $\mathbf { v }$ 为

$$
\small \mathbf { V } { = } \mathbf { V } _ { 1 } { + } \mathbf { V } _ { 2 }
$$

对于 $\mathbf { v _ { \imath } }$ ，当研究点从 $\pmb { P }$ 通过层面时，它仍属层 $\pmb { \sigma } - \pmb { \sigma _ { 0 } }$ 之外的点，因此仍然保持连续和有限。对于$\mathbf { V _ { 2 } }$ ，在前面讲了，当研究点通过均质圆平面层的中心时引力位保持连续和有限。综合起来，说明任意单层引力位 $\mathbf { v }$ 在通过层面时都是连续和有限的。

对于单层引力位对任意方向S的一阶导数也可分为两部份，即

![](images/88088fb9a3f2a12aa8a5a518f9be458cb1500be42d03bdbb19039c532b1935d1.jpg)  
围4.12

$$
\frac { \partial \mathbf { V } } { \partial \mathbf { s } } { = } \frac { \partial \mathbf { V } _ { 1 } } { \partial \mathbf { s } } { + } \frac { \partial \mathbf { V } _ { 2 } } { \partial \mathbf { s } } .
$$

显然，在研究点通过层面时， $\frac { \partial \mathbb { V } _ { 1 } } { \partial \mathbf { s } }$ 仍然是连续和有限的；而$\frac { \partial \mathbf { V } _ { 2 } } { \partial \mathbf { s } }$ 是均质圆平面层的引力在s方向上的分力，根据前面的讨论，它在通过层面时是不连续的。因此，单层引力位的一阶导数在通过层面时是不连续的。当研究点正位于层面时，单层位的一阶导数为

$$
( \frac { \partial V } { \partial \mathbf { s } } ) _ { \sigma } = - \textbf { f } \int _ { ( \mathbf { o } ) } \frac { \delta } { \mathbf { r } ^ { 2 } } \mathrm { c o s } \left( \mathbf { r } , \mathbf { s } \right) \mathrm { d } \sigma
$$

当由层外无限接近于层面时，单层位的一阶导数为

$$
( { \frac { \partial { \bf V } } { \partial { \bf s } } } ) _ { { \bf w }  { \bf s } } = - \mathrm { ~ f ~ } \int _ { { \bf \sigma } } { \frac { \hat { \bf s } } { { \bf r } ^ { 2 } } } \mathrm { c o s } ( { \bf r } , { \bf s } ) \mathrm { d } { \boldsymbol { \sigma } } - 2 \pi \mathrm { f } \hat { \delta } _ { 0 } \mathrm { c o s } ( { \bf n } , { \bf s } )
$$

而当由层内无限接近于层面时，单层位的一阶导数为

$$
( \frac { \partial \Psi } { \partial \mathbf { s } } ) _ { \mathsf { N } \to \mathsf { e } } = - \mathrm { ~ f ~ } \int _ { ( \mathsf { e } ) } \frac { \hat { \delta } } { \mathsf { r } ^ { 2 } } \cos { ( \mathsf { r } , \mathsf { s } ) } \mathrm { d } \sigma + 2 \pi \mathrm { f } \hat { \delta } _ { \boldsymbol { 0 } } \cos { ( \mathsf { n } , \mathsf { s } ) }
$$

$( 4 \cdot 6 7 )$ 和 $( 4 \cdot \cdot 6 8 )$ 式中的 $\delta _ { 0 }$ 为要通过的层面点的单层密度， $\mathbf { n }$ 为在该处层面的外法线方向。由于本课程研究的是外部位， $( 4 \cdot 6 7 )$ 式将会被用到。

# 84.6重力位

如果质体自身在绕轴旋转，则在质体上的点还受到离心力的作用，离心力的大小为

$$
\scriptstyle \mathbf { P } = \omega ^ { 2 } \rho
$$

式中 $\pmb { \omega }$ 为自转角速度， $\pmb { \vartheta }$ 为研究点到旋转轴的垂直距离；它的方向重合于 $P$ 方向，背向旋转轴，见图4.13。设旋转轴重合于直角坐标系的Z轴，则对于坐标为 $( \mathbf { x } , \mathbf { y } , \mathbf { z } )$ 的研究点有

$$
\pmb { \rho } { = } ( \mathbf { x } ^ { 2 } + \mathbf { y } ^ { 2 } ) ^ { 1 / 2 }
$$

代入 $( 4 \cdot 6 9 )$ 式，则得

$$
p = \omega ^ { 2 } ( \mathbf { x } ^ { 2 } + \mathbf { y } ^ { 2 } ) ^ { 1 / 2 }
$$

它在三个坐标轴方向的分量为

$$
\left. \begin{array} { c } { { \mathrm { P } _ { \bf { x } } { = } \omega ^ { 2 } { \bf { x } } } } \\ { { \mathrm { P } _ { \bf { y } } { = } \omega ^ { 2 } { \bf { y } } } } \\ { { \mathrm { P } _ { \bf { z } } { = } 0 } } \end{array} \right\}
$$

设有如下的一个数量函数

![](images/2d4f19ba7fff7d99cdd46e9367613c71d2d2e7ba3f19345183527853897e0459.jpg)  
图4.13

$$
\mathbf { Q } { = } \frac { \omega ^ { 2 } } { 2 } ( \mathbf { x } ^ { 2 } { + } \mathbf { y } ^ { 2 } )
$$

它对各坐标轴的偏导数为

$$
\scriptstyle { \begin{array} { l } { { \frac { \partial \mathbf { Q } } { \partial \mathbf { x } } } = { \boldsymbol { \omega } } ^ { 2 } \mathbf { x } } \\ { { \frac { \partial \mathbf { Q } } { \partial { \boldsymbol { y } } } } = { \boldsymbol { \omega } } ^ { 2 } \mathbf { y } } \\ { { \frac { \partial \mathbf { Q } } { \partial { \boldsymbol { z } } } } = 0 } \end{array} } { \mathrm { . } }
$$

对照（4·71)和(4·73)式，它符合力的位函数的定义，故 $( 4 . 7 2 )$ 式就是离心力位的表达式。

重力是引力和离心力的合力，可以证明重力位就是引力位和离心力位之和。

就等于重力 $\pmb { \ 8 }$ 在三个方向上的分量，即

以W表示重力位，它对三个坐标轴的偏导数

$$
\scriptstyle { \begin{array} { l } { { \frac { \partial \mathsf { W } } { \partial \mathbf { x } } } = g _ { \mathbf { x } } } \\ { \displaystyle { \frac { \partial \mathsf { W } } { \partial { \mathbf { y } } } } = g _ { \mathbf { y } } } \\ { \displaystyle { \frac { \partial \mathsf { W } } { \partial { \mathbf { z } } } } = g _ { \mathbf { z } } } \end{array} } .
$$

因为重力是引力F和离心力 $\mathbf { P }$ 的合力，因此有

$$
\begin{array} { l } { \mathbf { g _ { x } } = \mathbf { F _ { x } } + \mathbf { P _ { x } } } \\ { \mathbf { g _ { y } } = \mathbf { F _ { y } } + \mathbf { P _ { y } } } \\ { \mathbf { g _ { z } } = \mathbf { F _ { z } } + \mathbf { P _ { z } } } \end{array}
$$

将引力和离心力的分量分别用引力位V和离心力位Q的偏导数表示，然后代入（4·74)式的右端，得到

$$
\left. \begin{array} { c } { { \displaystyle { \frac { \partial \mathbf { W } } { \partial \mathbf { x } } } = { \frac { \partial } { \partial \mathbf { x } } } ( \mathbf { V } + \mathbf { Q } ) } } \\ { { \displaystyle { \frac { \partial \mathbf { W } } { \partial \mathbf { y } } } = { \frac { \partial } { \partial \mathbf { y } } } ( \mathbf { V } + \mathbf { Q } ) } } \\ { { \displaystyle { \frac { \partial \mathbf { W } } { \partial \mathbf { z } } } = { \frac { \partial } { \partial \mathbf { z } } } ( \mathbf { V } + \mathbf { Q } ) } } \end{array} \right\}
$$

这完全表明

$$
{ \bf W } = { \bf V } + { \bf Q }
$$

即重力位等于引力位和离心力位之和。将质体引力位的(4·20)式和离心力位的(4·72)式代入，得重力位的一般表达式为

$$
\mathbf { W } { = } \mathbf { f } \ \int _ { ( \mathbf { M } ) } \frac { \mathrm { d } \mathbf { m } } { \mathrm { ~ \overline { { \mathbf { r } } } ~ } } { + } \frac { \omega ^ { 2 } } { 2 \cdot } ( \mathbf { x } ^ { 2 } { + } \mathbf { y } ^ { 2 } )
$$

由位函数的性质,重力位对任意方向S的导数等于重力在该方向的分力g.,即

$$
\frac { \mathrm { d } \mathrm { W } } { \mathrm { d s } } { = } _ { \bf { g } \mathrm { s } } { = } _ { \bf { g c o s } } ( \bf { g } , \bf { s } )
$$

若S方向与重力方向相垂直，此时 $\cos ( \mathbf { g } , \mathbf { S } ) = 0$ ，则有

$$
\frac { \mathrm { d } \mathrm { w } } { \mathrm { d s } } { = } 0
$$

积分后可得

$$
\mathbf { W } _ { ( \mathbf { x } , \mathbf { y } , \tau ) } { = } \mathbf { C o n s t } .
$$

当给右端的常数一个定值，就得一个曲面方程。因为在这个面上重力位值处处都相等，故称等位面。另一方面，在这个曲面的任一点，所受重力的方向都与曲面正交，这样的曲面是处于均衡状态的液体表面，在大地测量中称之为水准面。水准面是一切大地测量实践的基准面，而与之正交的重力方向又是测量的基准线—一铅垂线。因此，重力位函数对于大地测量的实践和理论都是一个非常重要的物理量。

# 84.7水准面和力线

在 $( 4 \cdot 7 7 )$ 式中，若S方向为重力 $\pmb { \ 8 }$ 的反方向 $\mathbf { h }$ ,由于 $\cos { ( \mathbf { h } , \mathbf { g } ) } = - 1$ ，得到

$$
\frac { \mathrm { d } \mathrm { w } } { \mathrm { d } \mathbf { h } } { = } { - \mathbf { g } }
$$

亦可写为

$$
\mathrm { d } \mathbf { h } { = } { - } \frac { \mathrm { d } \mathbf { W } } { \mathbf { g } }
$$

式中dW可视为两个无限接近的水准面之间的位差,dh是这两个水准面之间的垂直距离。（4·79)式说明，水准面之间的距离与重力值成反比，这是水准面的不平行性。另一方面 $\pmb { \mathrm { \varepsilon } }$ 的数值是有限的值，dh不可能为零，这是水准面的不相交性。但在较小的范围内（如几百米间隔），重力值变化很小很小，这时就可把两个水准面视为平行。例如，在水准测量中，就认为每一站的前后标尺所在的两个水准面是互相平行的，从而将测出的水准面之间的距离作为两点的高差。

如图4.14所示，以水准面上任意一点O为原点设置坐标系，其Z轴重合于它的重力方向,XOY面重合于在该点的水准面的切平面,X轴指向北,Y轴指向东。通过O点的重力方向在任意方位θ(与X轴的夹角)作一法截面，它与水准面相交得一法截线(s)。现研究法截线(s)在O点处的曲率半径 $\scriptstyle \mathbf { R } _ { \theta }$ 。

根据数学知识，曲线的曲率等于切线的微小转角与曲线相应的微小弧长之比。如果用矢量表示，那就是：曲线在某点的曲率矢量 $\bar { \bf v }$ 等于曲线微分弧长趋于零时，切线单位矢量t的增量与ds之比值，即

$$
\scriptstyle { \vec { \mathbf { v } } } = { \frac { \mathbf { d } { \vec { \mathbf { \tau } } } } { \mathbf { d s } } }
$$

设 $\vec { \textbf { v } }$ 为单位曲率矢量,则可写为

$$
\frac { \overline { { \mathbf { v } } } } { \mathbf { R _ { \theta } } } { = } \frac { \mathrm { d } \overline { { \mathbf { \Omega } } } } { \mathrm { d } \mathbf { s } }
$$

将该式两端同取与重力矢量 $\pmb { \overline { { g } } }$ 的数量积。考虑到 $\vec { \pmb { v } }$ 和同向， ${ \vec { \mathbf { v } } } \cdot { \vec { \mathbf { g } } } = _ { \mathbf { g } }$ ，由 $( 4 \cdot 8 0 )$ 式得到

![](images/8d73e57cd725951b1c52782a54977107c8b208ddca7f58cfe193f4a00e671892.jpg)  
图4.14

$$
\frac { 1 } { \mathsf { R } _ { \theta } } { = } \frac { \overline { { \mathbf { g } } } } { \mathbf { g } } \cdot \frac { \mathrm { ~ d ~ } \overline { { \mathbf { t } } } } { \mathrm { ~ d } \mathbf { s } }
$$

因单位切线矢量 $\vec { \pmb { \tau } }$ 与 $\vec { \pmb { \mathsf { g } } }$ 正交，有

$$
\stackrel {  } { \mathbf { g } } \cdot \stackrel {  } { \mathbf { t } } = 0
$$

取关于 $\boldsymbol { \mathsf { s } }$ 的导数，得到

$$
\overline { { \underline { { \bf g } } } } \cdot \frac { \mathrm { ~ d ~ } \overline { { \bf t } } } { \mathrm { ~ d } s } + \overline { { \bf t } } \cdot \frac { \mathrm { ~ d ~ } \overline { { \bf g } } } { \mathrm { ~ d } s } = 0
$$

将它代入 $( 4 \cdot 8 1 )$ 式，则得

$$
\frac { 1 } { \mathbb { R } _ { 9 } } = - \frac { 1 } { g } ( \overline { { \sf t } } \cdot \frac { { \sf d } \vec { \sf g } } { { \sf d } s } )
$$

因为

$$
\vec { \bf g } = { \bf W } _ { \bf x } \vec { \bf i } + { \bf W } _ { \bf y } \vec { \bf j } + { \bf W } _ { \bf x } \vec { \bf k }
$$

式中 $\mathbf { w }$ 右下方的角标表示对该方向求偏导数。故有

$$
\frac { \mathrm { d } \overrightarrow { \mathbf { g } } } { \mathrm { d } \mathbf { s } } { = } \frac { \mathrm { d } } { \mathrm { d } \mathbf { s } } ( \boldsymbol { \Psi } _ { \mathbf { x } } \mathbf { \overrightarrow { i } } + \boldsymbol { \Psi } _ { \mathbf { y } } \mathbf { \overrightarrow { j } } + \boldsymbol { \Psi } _ { \mathbf { z } } \mathbf { \overrightarrow { k } } )
$$

而

$$
\scriptstyle { \overline { { \mathbf { t } } } } = \cos \theta { \mathrm { ~ } } { \overrightarrow { \mathbf { i } } } + \sin \theta { \mathrm { ~ } } { \overrightarrow { \mathbf { j } } }
$$

由这两个式子可得

$$
\overline { { { \mathrm {  ~ t ~ } } } } \cdot \frac { \mathrm { ~ d ~ } \overline { { { \mathrm {  ~ g ~ } } } } } { \mathrm { ~ d } \mathrm { s } } = \cos \theta \frac { \mathrm { ~ d } { \bf W } _ { \mathrm { x } } } { \mathrm { ~ d } \mathrm { s } } + \sin \theta \frac { \mathrm { ~ d } { \bf W } _ { \mathrm { Y } } } { \mathrm { ~ d } \mathrm { s ~ } }
$$

代人 $( 4 \cdot 8 2 )$ 式，得到

$$
\mathrm { ~  ~ \cdot ~ } \mathrm { ~  ~ \frac ~ { ~ 1 ~ } { ~ R _ { \theta } ~ } = - \frac ~ { 1 } ~ } ( \cos \theta \mathrm { ~ \frac { d W _ { x } } { d s } + } \sin \theta \mathrm { ~ \frac { d W _ { y } } { d s } ~ } )
$$

右端的两个导数可以写为

$$
\begin{array} { r } { \frac { \mathrm { d } \mathbf { W } _ { \mathbf { x } } } { \mathrm { d } \mathbf { s } } { = } \frac { \partial \mathbf { W } _ { \mathbf { x } } } { \partial \mathbf { x } } \frac { \mathrm { d } \mathbf { x } } { \mathrm { d } \mathbf { s } } { + } \frac { \partial \mathbf { W } _ { \mathbf { y } } } { \partial \mathbf { y } } \frac { \mathrm { d } \mathbf { y } } { \mathrm { d } \mathbf { s } } { + } \frac { \partial \mathbf { W } _ { \mathbf { x } } } { \partial \boldsymbol { z } } \frac { \mathrm { d } \mathbf { z } } { \mathrm { d } \mathbf { s } } } \\ { \frac { \mathrm { d } \mathbf { W } _ { \mathbf { y } } } { \mathrm { d } \mathbf { s } } { = } \frac { \partial \mathbf { W } _ { \mathbf { y } } } { \partial \mathbf { x } } \frac { \mathrm { d } \mathbf { x } } { \mathrm { d } \mathbf { s } } { + } \frac { \partial \mathbf { W } _ { \mathbf { y } } } { \partial \mathbf { y } } \frac { \mathrm { d } \mathbf { y } } { \mathrm { d } \mathbf { s } } { + } \frac { \partial \mathbf { W } _ { \mathbf { y } } } { \partial \boldsymbol { z } } \frac { \mathrm { d } \mathbf { z } } { \mathrm { d } \mathbf { s } } } \end{array}
$$

还有

$$
\scriptstyle { \frac { \mathrm { d } \mathbf { x } } { \mathrm { d s } } } = \cos \theta \qquad { \frac { \mathrm { d } \mathbf { y } } { \mathrm { d s } } } = \sin \theta \qquad { \frac { \mathrm { d } { z } } { \mathrm { d s } } } = 0
$$

因此有

$$
\begin{array} { r l } & { \frac { \mathrm { d } \mathbb { W } _ { \mathbf { x } } } { \mathrm { d s } } { = } \mathbb { W } _ { \mathbf { x } \times \mathbf { \cos } \theta + \mathbb { W } _ { \mathbf { x } \times \mathbf { \sin } \theta } } } \\ & { \frac { \mathrm { d } \mathbb { W } _ { \mathbf { \eta } \times \mathbf { \cos } \theta + \mathbb { W } _ { \mathbf { y } \times \mathbf { \sin } \theta } , } } { \mathrm { d } \mathbf { s } } { = } \mathbb { W } _ { \mathbf { y } \times \mathbf { \cos } \theta + \mathbb { W } _ { \mathbf { y } \times \mathbf { \sin } \theta } . } } \end{array}
$$

将它们代入 $( 4 \cdot 8 4 )$ 式，最后得到

$$
\frac { 1 } { \mathrm { R } _ { \theta } } { = } - \frac { 1 } { g } \left( \mathrm { W } _ { \mathrm { x x } } { \cos } ^ { 2 } \theta { + } \mathrm { W } _ { \mathrm { x y } } { \sin } 2 \theta { + } \mathrm { W } _ { \mathrm { y y } } { \sin } ^ { 2 } \theta \right)
$$

这就是水准面曲率(或曲率半径)的计算式，它要求知道研究点处的重力和重力位的三个二阶导数值；另一方面还与法截线的方位 $\pmb \theta$ 有关，即水准面曲率在不同的方位上是不同的。在 $( 4 \cdot$ 85）式中，分别取 $\pmb \theta$ 为 $0 ^ { \circ }$ 和 $9 0 ^ { \circ }$ ，则可得水准面的子午方向和卯酉方向的曲率，即子午方向的曲率为

$$
\frac { 1 } { \mathsf { R } _ { \mathrm { x } } } { = } - \frac { \mathsf { W } _ { \mathrm { x x } } } { \mathsf { g } }
$$

卯酉方向的曲率为

$$
\frac { 1 } { \mathsf { R } _ { \mathsf { y } } } { = } { - } \frac { \mathsf { W } _ { \mathsf { y } \mathsf { y } } } { \mathsf { g } } .
$$

重力位的拉普拉斯算子为

$$
\Delta \mathbb { W } { = } \mathbb { W } _ { { \mathbf { x } } { \mathbf { x } } } { + } \mathbb { W } _ { y y } { + } \mathbb { W } _ { z z }
$$

由 $( 4 \cdot 7 5 )$ 式有

$$
\Delta \overrightarrow { w } = \Delta \overrightarrow { v } + \Delta \alpha
$$

在 $\ S \ 4 . 4$ 中讲到 $\Delta \mathbf { V } = - 4 \pi \mathbf { f } \mathbf { D }$ ，由 $( 4 \cdot 7 2 )$ 式可得 $\Delta \mathsf { Q } = \mathsf { 2 } \omega ^ { 2 }$ 。故有

$$
\Delta \Psi = - 4 \pi \mathrm { f D } + 2 \omega ^ { 2 }
$$

因而可以写出如下的关系式

$$
\mathrm { W } _ { u z } = - 4 \pi \mathrm { f D } + 2 \omega ^ { 2 } - \mathrm { W } _ { x x } - \mathrm { W } _ { y y }
$$

将由 $( 4 \cdot 8 6 )$ 和 $( 4 \cdot 8 7 )$ 分别导出的 $\pmb { W } _ { \pmb { x } \pmb { x } }$ 和 $\yen 1$ 代入，则得

$$
\mathrm { W } _ { \mathrm { s s } } = - 4 \pi \mathrm { f D } + 2 \omega ^ { 2 } + \mathrm { g } ( \frac { 1 } { \mathrm { R } _ { \mathrm { s } } } + \frac { 1 } { \mathrm { R } _ { \mathrm { y } } } )
$$

因为Z轴与重力方向一致， $\pmb { \mathbb { W } } _ { \pmb { z } }$ 是重力， $\Psi _ { \pmb { z } }$ 是重力在 $z$ 方向的变化率，一般称为重力的垂直梯度。因此， $( 4 \cdot 8 9 )$ 式给出了重力垂直梯度与水准面曲率之间的关系。

水准面之间的互不平行，使得处处与水准面正交的线必然是一条曲线，见图4.15。由于在这条曲线上的每一点的切线都与该点的重力方向相重合，故称它为重力线，简称为力线。下面研究力线的曲率。

以 ${ \vec { \mathbf { v } } } ^ { \prime }$ 表示力线 ${ \bf ( s ^ { \prime } ) }$ 的单位曲率矢量p为力线的曲率半径，为力线 ${ { \bf \zeta } _ { \bf 8 } } ^ { \prime }$ )的切线单位矢量，类似于 $( 4 \cdot 8 0 )$ 式可以写出

![](images/455a590900edc6f011210423343358a46c94b10ecb27a3e4ae7e6592bc053e8e.jpg)  
图4.15

$$
\frac { \vec { \bf v } ^ { \prime } } { \pmb { \rho } } { = } \frac { \bf d \vec { \bf \tau } ^ { \prime } } { \bf d s ^ { \prime } }
$$

因为力线上每点的切线与重力方向一致，故有

$$
\mathbf { g } \cdot \overline { { \mathbf { t } } } ^ { \prime } = \overline { { \mathbf { g } } }
$$

取关于 $\mathbf { s } ^ { \prime }$ 的导数，得到

$$
\mathbf { g } \ { \frac { \mathrm { d } \ { \overline { { \mathbf { t } } } } ^ { \prime } } { \mathrm { d } \mathbf { s } ^ { \prime } } } { + \mathrm { r } } { \frac { \mathrm { d } \mathbf { g } } { \mathrm { d } \mathbf { s } ^ { \prime } } } { = } { \frac { \mathrm { d } \ { \overline { { \mathbf { g } } } } } { \mathrm { d } \mathbf { s } ^ { \prime } } }
$$

即

$$
\frac { \mathrm { d } \vec { \textbf { t } } ^ { \prime } } { \mathrm { d } s ^ { \prime } } { = } \frac { 1 } { \mathbf { g } } ( \frac { \mathrm { d } \vec { \textbf { g } } } { \mathrm { d } s ^ { \prime } } { - } \vec { \textbf { t } } ^ { \mathrm { d } } \frac { \mathrm { d } \mathbf { g } } { \mathrm { d } s ^ { \prime } } )
$$

将它代人 $( 4 \cdot 9 0 )$ 式，则得

![](images/62b3bc1f0d6c0584cf81d877b6963830c0530c7e2b725d0b065c33e8d2c1036e.jpg)  
图4.16

$$
\frac { \overline { { \bf v } } ^ { \prime } } { \rho } { = } \frac { 1 } { \bf g } ( \frac { \mathrm { d } \mathrm { ~ } \overline { { \bf g } } } { \mathrm { d } { \bf s } ^ { \prime } } { - } \overline { { \bf t } } ^ { \prime } \frac { \mathrm { d } { \bf g } } { \mathrm { d } { \bf s } ^ { \prime } } )
$$

设研究力线上 $^ { \mathrm { o } }$ 点的曲率，见图4.16,以 $\mathrm { \bf O }$ 为原点设置坐标系，使其Z轴重合于该点的重力方向,XOY平面与其正交,X轴指北,Y轴指东。因为ds'=dz,故有

$$
\frac { \partial \mathbf { \vec { g } } } { \partial \mathbf { s } ^ { \prime } } = \frac { \mathbf { d } \mathbf { \vec { \tau g } } } { \mathbf { d z } } = \mathbf { W _ { x z } } \mathbf { \vec { i } } + \mathbf { W _ { y z } } \mathbf { \vec { j } } + \mathbf { W _ { z z } } \mathbf { \vec { k } }
$$

$$
\frac { \mathrm { d } \mathbf { g } } { \mathrm { d } \mathbf { s } ^ { \prime } } { = } \frac { \mathrm { d } \mathbf { g } } { \mathrm { d } \mathbf { z } } { = } \mathbf { W } _ { z z } ,
$$

$$
\overline { { \mathfrak { r } } } ^ { \prime } = \overline { { \mathfrak { k } } }
$$

将这些代入 $( 4 \cdot 9 1 )$ 式，得到

$$
\frac { \widehat { \mathbf { v } } ^ { \prime } } { \rho } { = } \frac { 1 } { \mathbf { g } } ( \mathbb { W } _ { \mathbf { x } } \widehat { \mathbf { i } } + \mathbb { W } _ { \mathbf { y } \mathbf { z } } \widehat { \mathbf { j } } ^ { \ ) }
$$

因此可以求得,力线曲率的大小为

$$
\frac { 1 } { \rho } = \frac { 1 } { \mathbf { g } } \sqrt { \mathbf { W } _ { \mathbf { x } \mathbf { z } } ^ { 2 } + \mathbf { W } _ { \mathbf { y } \mathbf { z } } ^ { 2 } } = \frac { 1 } { \mathbf { g } } \sqrt { ( \frac { \partial \mathbf { g } } { \partial \mathbf { x } } ) ^ { 2 } + ( \frac { \partial \mathbf { g } } { \partial \mathbf { y } } ) ^ { 2 } } \ ( 4 \ \cdot \ 9 2 )
$$

设 $\mathbf { x }$ 为力线曲率矢量与 $\mathbf { x }$ 轴的夹角，则有

$$
\scriptstyle { \mathrm { t g } } \alpha = { \frac { \mathbb { W } _ { \gamma _ { s } } } { \mathbb { W } _ { \gamma _ { s } } } } = { \frac { \frac { \partial \mathbf { g } } { \partial { \boldsymbol { y } } } } { \frac { \partial { \boldsymbol { g } } } { \partial { \boldsymbol { \mathbf { x } } } } } }
$$

$( 4 \cdot 9 2 )$ 和(4·.93)式说明，力线的曲率与重力的水平梯度 $\frac { \partial g } { \partial \mathbf { x } } \neq \boldsymbol { \mathbb { I } } \frac { \partial \mathbf { g } } { \partial \mathbf { y } }$ 有关。由于&值的变化，使重力线变成一条空间曲线。

# 第五章 调和函数及其边值问题

# 85.1高斯和格林的积分式

高斯和格林的积分公式可用于研究位函数，它们是研究地球重力场理论的最基本公式。

# -、高斯公式

若有三个函数 $\mathbf { P } ( \mathbf { x } , \mathbf { y } , \mathbf { z } ) , \mathbf { Q } ( \mathbf { x } , \mathbf { y } , \mathbf { z } )$ 和 $\mathbf { R } ( \mathbf { x } , \mathbf { y } , \mathbf { z } )$ ，它们在 $\mathbf { \Pi } ( \pmb { \sigma } )$ 面所围的区域 $( \pmb { \tau } )$ 内连同一阶偏导数都是连续和有限的，则有如下的关系式：

$$
\int ( \frac { \partial \mathbf { P } } { \partial \mathbf { x } } + \frac { \partial \mathbf { Q } } { \partial y } + \frac { \partial \mathbf { R } } { \partial z } ) \mathrm { d } \tau = \int _ { \circ } ( \mathbf { P } \mathrm { c o s } ( \mathbf { n } , \mathbf { X } ) + \mathbf { Q } \mathrm { c o s } ( \mathbf { n } , \mathbf { Y } ) + \mathbf { R } \mathrm { c o s } ( \mathbf { n } , \mathbf { Z } ) ) \mathrm { d } \sigma
$$

式中 $\bar { \mathbf { u } }$ 为曲面 $\mathbf { \Pi } ( \pmb { \sigma } )$ 的关于 $\pmb { \tau }$ 的外法线方向,X、Y、Z为坐标轴方向。

为了证明 $( 5 \cdot 1 )$ 式，先考察积分 {dr。因为体积元素dt=dxdydz，代入并完成对乙的积分，则得

$$
\int \frac { \partial \mathbb { R } } { \partial z } \mathrm { d } \tau = \iint _ { \pmb { \zeta } } [ \mathbb { R } ( \mathbf { x } , \mathbf { y } , \mathbf { z } _ { \mathrm { A } } ) - \mathbb { R } ( \mathbf { x } , \mathbf { y } , \mathbf { z } _ { \mathrm { B } } ) ] \mathrm { d } \mathbf { x } \mathrm { d } \mathbf { y }
$$

式中 $\pmb { z _ { \mathrm { A } } }$ 是 $\pmb { z }$ 的积分上限，即 $\pmb { \sigma }$ 面的上半部份 ${ \pmb { \sigma } } _ { \pmb { \Lambda } }$ 的 $\pmb { z }$ 值； $\pmb { z } _ { \mathbf { B } }$ 是 $\mathbf { z }$ 的积分下限，即 $\pmb { \sigma }$ 面的下半部份$\sigma _ { \mathrm { B } }$ 上的 ${ \pmb z }$ 值；(C）是 $( \pmb { \sigma } )$ 面在坐标面XOY上的投影，参见图5.1。因此，dxdy可以看作是曲面 $\pmb { \sigma }$ 上的单元面积 $\pmb { \mathrm { d } } \pmb { \sigma _ { \mathsf { A } } }$ 和 $\mathsf { d } \pmb { \sigma _ { \mathtt { B } } }$ 在XOY面上的投影，显然有

$$
\mathrm { d } \sigma _ { \mathrm { A } } \mathrm { c o s } \left( \mathbf { n } _ { \mathrm { A } } , Z \right) { = } \mathrm { d } { \mathbf { x } } \mathrm { d } { \mathbf { y } } { = } { - } \mathrm { d } \sigma _ { \mathrm { B } } \mathrm { c o s } \left( \mathbf { n } _ { \mathrm { B } } , Z \right)
$$

其中 $\pmb { \mathrm { n } } _ { \pmb { \mathrm { A } } }$ 和 $\mathtt { n } _ { \mathtt { B } }$ 分别为 $\mathtt { d } \pmb { \sigma } _ { A }$ 和 $\mathbf { d } \pmb { \sigma } _ { \vec { \imath } }$ 的外法线方向。这样·一来， $( 5 \cdot 2 )$ 式就可以写为

$$
\int \frac { \partial { \mathbf { R } } } { \partial z } \mathrm { d } \tau = \iint \mathrm { R } \left( \mathbf { x } , \mathbf { y } , \mathbf { z } _ { \mathrm { A } } \right) \mathrm { c o s } \left( \mathrm { n } _ { \mathrm { A } } , Z \right) \mathrm { d } \sigma _ { \mathrm { A } } + \iint \mathbf { R } \left( \mathbf { x } , \mathbf { y } , \mathbf { z } _ { \mathrm { B } } \right) \mathrm { c o s } \left( \mathrm { n } _ { \mathrm { B } } , Z \right) \mathrm { d } \sigma _ { \mathrm { B } }
$$

右端两项可以合并为对整个曲面 $\mathbf { \Pi } ( \pmb { \sigma } )$ 的曲面积分，即

$$
\int \frac { \partial \mathbb { R } } { \partial z } \mathrm { d } \tau = \int _ { \boldsymbol { \sigma } } \mathrm { R c o s } ( \mathtt { n } , Z ) \mathrm { d } \sigma
$$

同理可以得到

$$
\left. \begin{array} { c } { { \displaystyle \int \frac { \partial { \bf P } } { \partial { \bf x } } { \bf d } \tau = \displaystyle \int _ { o } { \bf P } \mathrm { c o s } \left( { \bf n } , { \bf X } \right) { \bf d } \sigma } } \\ { { \displaystyle \int \left. \frac { \partial { \bf Q } } { \partial { \bf y } } { \bf d } \tau = \displaystyle \int _ { o } { \bf Q } \mathrm { c o s } \left( { \bf n } , { \bf Y } \right) { \bf d } \sigma \right)}  }  \end{array} \right\}
$$

综合 $( 5 \cdot 3 )$ 和 $( 5 \cdot 4 )$ 式，即得 $( 5 \cdot 1 )$ 式。 $( 5 \circ 1 )$ 式就是高斯公式。

![](images/cdea637327f5d01499b71d9af7d90e07c65df44b7e4adc697463ffa22e616edb.jpg)  
图5.1

# 二、格林公式

在 $( 5 \cdot 1 )$ 式中，令

$$
\mathrm { P = U } { \frac { \partial V } { \partial \mathbf { x } } } \qquad \mathbf { Q } = \mathrm { U } { \frac { \partial V } { \partial y } } \qquad \mathrm { R = U } { \frac { \partial V } { \partial z } }
$$

其中 $\mathbf { U }$ 和 $\mathbf { v }$ 都是 $\mathbf { x } , \mathbf { y } , \mathbf { z }$ 的函数，且在 $\pmb { \tau }$ 内有连续和有限的一阶偏导数。由此可得

$$
\scriptstyle { \begin{array} { c } { { \frac { \partial \mathbf { P } } { \partial \mathbf { x } } } = { \frac { \partial \mathbf { U } } { \partial \mathbf { x } } } { \frac { \partial \mathbf { V } } { \partial \mathbf { x } } } + \mathbf { U } { \frac { \partial ^ { 2 } \mathbf { V } } { \partial \mathbf { x } ^ { 2 } } } } \\ { { \frac { \partial \mathbf { Q } } { \partial \mathbf { y } } } = { \frac { \partial \mathbf { U } } { \partial \mathbf { y } } } { \frac { \partial \mathbf { V } } { \partial \mathbf { y } } } + \mathbf { U } \ { \frac { \partial ^ { 2 } \mathbf { V } } { \partial { \mathbf { y } } ^ { 2 } } } } \\ { { \frac { \partial \mathbf { R } } { \partial { \mathbf { z } } } } = { \frac { \partial \mathbf { U } } { \partial { \mathbf { z } } } } { \frac { \partial \mathbf { V } } { \partial { \mathbf { z } } } } + \mathbf { U } \ { \frac { \partial ^ { 2 } \mathbf { V } } { \partial { \mathbf { z } } ^ { 2 } } } } \end{array} } .
$$

和

$$
{ \bf \mathrm { ~  ~ \psi ~ } } ^ { 3 } \cos \left( { \bf n } , { \bf X } \right) + \mathrm { Q c o s } \left( { \bf n } , { \bf Y } \right) + \mathrm { R c o s } \left( { \bf n } , Z \right) = \mathrm { U } \frac { \partial \nabla } { \partial { \bf x } } \mathrm { c o s } \left( { \bf n } , { \bf X } \right) + \mathrm { U } \frac { \partial \hat { W } } { \partial { \bf y } } \mathrm { c o s } \left( { \bf n } , { \bf Y } \right) + \mathrm { U } \frac { \partial \hat { W } } { \partial { \bf z } } \mathrm { c o s } \left( { \bf n } , { \bf X } \right) .
$$

将 $( 5 \cdot 5 )$ 和 $( 5 \cdot 6 )$ 式代入 $( 5 \cdot 1 )$ 式，并顾及到

$$
\frac { \partial \mathbf { V } } { \partial \mathbf { x } ^ { 2 } } + \frac { \partial ^ { 2 } \mathbf { V } } { \partial \mathbf { y } ^ { 2 } } + \frac { \partial ^ { 2 } \mathbf { V } } { \partial \mathbf { z } ^ { 2 } } = \Delta \mathbf { V }
$$

和

$$
\frac { \partial { \cal { N } } } { \partial { \bf x } } \mathrm { c o s } \left( { \bf n , X } \right) + \frac { \partial { \cal { N } } } { \partial { \bf y } } \mathrm { c o s } \left( { \bf n , Y } \right) + \frac { \partial { \cal { V } } } { \partial { \bf z } } \mathrm { c o s } \left( { \bf n , Z } \right) = \frac { \partial { \bf V } } { \partial { \bf n } }
$$

则得

$$
\int ( \frac { \partial \mathrm { U } } { \partial \mathrm { x } } \frac { \partial \mathrm { V } } { \partial \mathrm { x } } + \frac { \partial \mathrm { U } } { \partial \mathrm { y } } \frac { \partial \mathrm { V } } { \partial \mathrm { y } } + \frac { \partial \mathrm { U } } { \partial \mathrm { z } } \frac { \partial \mathrm { V } } { \partial \mathrm { z } } ) \mathrm { d } \tau + \int \mathrm { U } \Delta \mathrm { V } \mathrm { d } \tau = \int \mathrm { U } \frac { \partial \mathrm { V } } { \partial \mathrm { n } } \mathrm { d } \sigma
$$

式中 $\frac { \partial \mathbf { V } } { \partial \mathbf { n } }$ 为 $\mathbf { v }$ 的外法线方向的偏导数。 $( 5 \cdot 7 )$ 式通常被称为格林第一恒等式。显然，将 $( 5 \cdot 7 )$ 式中的两个函数U和 $\mathbf { v }$ 互换，等式仍然成立，得到.

$$
\int ( \frac { \partial \mathrm { U } } { \partial \mathbf { x } } \frac { \partial \mathrm { V } } { \partial \mathbf { x } } + \frac { \partial \mathrm { U } } { \partial \mathbf { y } } \frac { \partial \mathrm { V } } { \partial \mathbf { y } } + \frac { \partial \mathrm { U } } { \partial \mathbf { z } } \frac { \partial \mathrm { V } } { \partial \mathbf { z } } ) \mathrm { d } \mathbf { z } + \int \mathrm { V } \Delta \mathrm { U } \mathbf { d } \tau = \int \mathrm { V } \frac { \partial \mathrm { U } } { \partial \mathbf { \mathrm { n } } } \mathrm { d } \boldsymbol { \sigma }
$$

以 $( 5 \cdot 7 )$ 式减 $( 5 \cdot 8 )$ 式，则得

$$
\int _ { \tau } ( \mathrm { U } \Delta \mathsf { V } - \mathrm { V } \Delta \mathrm { U } ) \mathrm { d } \tau = \int _ { \sigma } ( \mathrm { U } \frac { \partial \mathsf { V } } { \partial \mathrm { n } } - \mathrm { V } \frac { \partial \mathrm { U } } { \partial \mathrm { n } } ) \mathrm { d } \sigma
$$

该式称为格林第二恒等式。

$( 5 \cdot 9 )$ 式也可用于由两个或多个界面组成的 $\pmb { \tau }$ 区域。如图5.2所示，区域 $\pmb { \tau }$ 是(S)面及半径为 $P$ 的球面 $( \pmb { \Sigma } )$ 之间的区域。此时，格林第二恒等式应写为

$$
\int _ { \Omega } ( \mathrm { U } \Delta \mathrm { V } - \mathrm { V } \Delta \mathrm { U } ) \mathrm { d } \tau = \int _ { \Omega } ( \mathrm { U } \frac { \partial \mathrm { V } } { \partial \mathrm { n } } - \mathrm { V } \frac { \partial \mathrm { U } } { \partial \mathrm { n } } ) \mathrm { d } \mathrm { S } + \int _ { \Omega } ( \mathrm { U } \frac { \partial \mathrm { V } } { \partial \mathrm { n } } - \mathrm { V } \frac { \partial \mathrm { U } } { \partial \mathrm { n } } ) \mathrm { d } \Sigma
$$

其中的 $\pmb { \Omega }$ 都必须是界面(S)和 $\textcircled{2}$ 的关于 $\pmb { \tau }$ 的外法线方向。

如果区域 $\pmb { \tau }$ 是指闭曲面(S)以外的整个外空间，则函数U和 $\mathbf { v }$ 不仅要满足前述的要求，而且还必须是在无穷远处满足正则的条件。适用于该种情况的格林第二恒等式可以由$( 5 \cdot 1 0 )$ 式导出，但要取第二项积分中的球面 $( \pmb { \Sigma } )$ 的半径变为无穷大。根据正则函数的性质可知，此项积分为零。因此，适用于 $\mathbf { \Pi } ( \pmb { \sigma } )$ 面以外的无限空域的格林第二恒等式有与 $( 5 \cdot 9 )$ 式完全相同的形式，只是 $\pmb { \nmid }$ 的方向应该是向里的。这点非常重要，在应用时如不注意，就会导致错误的结果。

![](images/72fe2a323f131d9d1539e9c23e5907196ca91ac7fddde891edd8dd140cbd2019.jpg)  
图5.2

在(5·9)式中，函数U取为区域 $( \pmb { \tau } )$ 内的流动点至某一固定点 $\mathbf { P }$ 的距离 $\pmb { \tau }$ 的倒数，即 $\mathbf { U } { = } \frac { 1 } { \mathbf { r } }$ ，看看有怎样的结果。按$\mathbf { P }$ 点位置的不同，可分为三种情况讨论。

1.P点在区域 $\pmb { \tau }$ 的外面。此时 $\frac { 1 } { \ I }$ 满足拉普拉斯方程，即 $\Delta \mathrm { U } = \Delta ( \frac { 1 } { \mathrm { \Delta r } } ) = 0$ ，这在 $\ S \ 4 . 4$ 中证明质体对外部点的引力位满足拉普拉斯方程时已经证明。这样一来，由 $( 5 \cdot 9 )$ 式得到

$$
\int \limits _ { \tau } \frac { 1 } { \mathbf { r } } \Delta \mathbf { V } \mathrm { d } \tau = \int \lbrack \frac { 1 } { \mathbf { r } } \frac { \partial \mathbf { V } } { \partial \mathbf { n } } - \mathbf { V } \frac { \partial } { \partial \mathbf { n } } ( \frac { 1 } { \mathbf { r } } ) ) \mathrm { d } \sigma
$$

2.P点在区域 $\pmb { \tau }$ 内。此时 $\pmb { \tau }$ 有为零的情况， $\mathbf { U } = \frac { 1 } { \mathbf { \sigma _ { r } } }$ 就不是有限的，故不能运用 $( 5 \cdot 9 )$ 式。为避免此种情况，如图5.3所示，以 $\mathbf { P }$ 为球心作一半径为 $P$ 的小球，这个球要小到保证球面(S)都在区域 $\pmb { \tau }$ 内。这样一来，区域 $\pmb { \tau }$ 被分成两部分，球内部份和球外的其余部份 $\pmb { \tau _ { 1 } _ { 0 } }$ 对于区域 $\pmb { \tau } _ { 1 }$ ，可以应用 $( 5 \cdot 1 0 )$ 式。由于在此区域内 $\Delta ( \frac { 1 } { \tau } ) = 0$ ，故可写为

$$
\int \frac { 1 } { \tau } \Delta \mathbf { V } \mathrm { d } \tau = \int \sb { \textnormal { \mathfrak { c } } } ( \frac { 1 } { \tau } \frac { \partial \mathbf { V } } { \partial \boldsymbol { \mathrm { n } } } - \textnormal { V } \frac { \partial } { \partial \boldsymbol { \mathrm { n } } } ( \frac { 1 } { \textup { \bf r } } ) ) \mathrm { d } \boldsymbol { \sigma } + \int \sb { \mathrm { ~ \mathfrak { c } ~ } } ( \frac { 1 } { \textup { \bf r } } \frac { \partial \mathbf { V } } { \partial \boldsymbol { \mathrm { n } } } - \textnormal { V } \frac { \partial } { \partial \boldsymbol { \mathrm { n } } } ( \frac { 1 } { \textup { \bf r } } ) ) \mathrm { d } \mathbf { S }
$$

当小球的半径趋于零时，区域 $\tau _ { 1 }$ 就变成区域 $\pmb { \tau }$ ，所以要讨论 $( 5 ^ { \cdot } \cdot 1 2 )$ 式在 $\pmb { \rho }  0$ 时的极限情况。显然有

![](images/621b3ada70d3b9a14f5b5359f2ee86890e0882d146c1553d3668a0140f2054ec.jpg)  
图5.3

$$
\operatorname* { l i m } _ { \mathfrak { e } \to 0 } \int \frac { \cdot 1 } { \mathfrak { r } } \Delta \mathbf { V } \mathrm { d } \tau = \int \frac { 1 } { \mathfrak { r } } \Delta \mathbf { V } \mathrm { d } \tau \quad ( 5 \bullet 1 3 )
$$

现研究 $( 5 \cdot 1 2 )$ 式右端第二项。先考察$\operatorname* { l i m } _ { \boldsymbol { \rho } \to 0 } \int _ { \mathbb { S } ) } \frac { 1 } { \boldsymbol { r } } \frac { \partial \mathbf { V } } { \partial \boldsymbol { \mathrm { n } } } \mathrm { d } \mathbf { S }$ 。因为(S)面为球面，由球面上的点至球心P的距离r都等于球的半径p,故有

$$
\operatorname* { l i m } _ { \boldsymbol { \Theta } \to \boldsymbol { 0 } } \int \frac { 1 } { \boldsymbol { \Upsilon } } \frac { \partial \mathsf { V } } { \partial \boldsymbol { \mathsf { n } } } \mathrm { d } \mathsf { S } = \operatorname* { l i m } _ { \boldsymbol { \theta } \to \boldsymbol { 0 } } \frac { 1 } { \boldsymbol { \mathsf { \rho } } } \int \frac { \partial \mathsf { V } } { \partial \boldsymbol { \mathsf { n } } } \mathrm { d } \mathsf { S }
$$

由于 $\mathbf { v }$ 的一阶偏导数是有限、连续的，可以利用积分中值定理写出

$$
\int _ { \left( \mathbb { S } \right) } \frac { \partial V } { \partial \boldsymbol { \mathrm { n } } } \mathrm { d } \mathbf { S } = \mathbf { A } \int _ { \left( \mathbb { S } \right) } \mathrm { d } \mathbf { S } = \mathrm { A } \cdot 4 \pi \boldsymbol { \rho } ^ { 2 }
$$

其中的A是 $\cdot \frac { \partial \mathbf { V } } { \partial \mathbf { n } }$ 在球面上的积分中数。将该式代入 $( 5 \cdot 1 \dot { 4 } )$ 式，则得

$$
\operatorname* { l i m } _ { \boldsymbol { \mapsto } \boldsymbol { \boldsymbol { \vartheta } } } \int _ { \boldsymbol { \mathsf { S } } } \frac { 1 } { \boldsymbol { \mathsf { r } } } \frac { \partial \boldsymbol { \mathsf { V } } } { \partial \boldsymbol { \mathsf { n } } } d \boldsymbol { \mathsf { S } } = \operatorname* { l i m } _ { \boldsymbol { \mathsf { \rho } } \boldsymbol { \mapsto } \boldsymbol { \boldsymbol { \imath } } } ( \boldsymbol { \mathsf { A } } \boldsymbol { \cdot } \boldsymbol { \mathsf { 4 } } \pi \boldsymbol { \rho } ) = 0
$$

再考察 $\operatorname* { l i m } _ { \boldsymbol { \theta } \to 0 } \int _ { \mathbb { S } } \mathbf { V } \frac { \partial } { \partial \mathbf { n } } ( \frac { 1 } { \mathbf { r } } ) d \mathbf { S } .$ )ds。因为(S)是球面,n是(S)面的关于τ的外法线，故n是指向球心P的，它与 $\pmb { \mathfrak { F } }$ 同方向，但在求导时变点是 $\pmb { \tau }$ 的起始点，故有

$$
\frac { \partial } { \partial \mathbf { n } } ( \frac { 1 } { \mathbf { r } } ) \vert _ { s } = - \frac { \partial } { \partial \mathbf { r } } ( \frac { 1 } { \mathbf { r } } ) \vert _ { s } = \frac { 1 } { \mathbf { r } ^ { 2 } } \vert _ { s } = \frac { 1 } { \rho ^ { 2 } }
$$

因而得到

$$
\operatorname* { l i m } _ { \boldsymbol { \Theta } \to \boldsymbol { 0 } } \int _ { \mathcal { ( S ) } } \nabla \frac { \partial } { \partial \boldsymbol { \mathrm { n } } } ( \frac { 1 } { \boldsymbol { \mathrm { r } } } ) \mathrm { d } \boldsymbol { \mathrm { S } } = \operatorname* { l i m } _ { \boldsymbol { \Theta } \to \boldsymbol { 0 } } \frac { 1 } { \rho ^ { 2 } } \int _ { \mathcal { ( S ) } } \nabla \mathrm { d } \boldsymbol { \mathrm { S } }
$$

应用积分中值定理， $\mathbf { v }$ 在球面上的积分中数 $\mathbf { v _ { m } }$ 为

$$
\mathbf { V } _ { \mathbf { m } } = \frac { 1 } { 4 \pi \rho ^ { 2 } } \int \mathbf { V } \mathbf { d } \mathbf { S }
$$

故有

$$
\frac { 1 } { p ^ { 2 } } \int \limits _ { ( \odot ) } ^ { \infty } \nabla \mathrm { d } \mathsf { S } = 4 \pi \mathsf { V } _ { \mathrm { m } }
$$

当 $\rho {  } 0$ 时， $\mathtt { v _ { m } }$ 就是 $\mathbf { P }$ 点的函数值 ${ \bf v _ { P } }$ ，因此由 $( 5 \cdot 1 6 )$ 式可得

$$
\operatorname* { l i m } _ { p  0 } \int _ { ( \mathbb { S } ) } \nabla \frac { \partial } { \partial \mathbf { n } } ( \frac { 1 } { \mathbf { r } } ) \mathrm { d } \mathbb { S } = 4 \pi \mathbf { V } _ { \mathbb { P } }
$$

考虑到(5·13)、(5·15)和(5·17)式,由(5·12)式可得

$$
\int \displaylimits _ { \overline { { \mathbf { \Pi } } } } \frac { 1 } { r } \Delta \mathbf { V } d \tau = \int \displaylimits _ { \mathcal { ( 0 ) } } [ \frac { 1 } { r } \frac { \partial \mathbf { V } } { \partial \mathbf { \Pi } } - \mathbf { V } \frac { \partial } { \partial \mathbf { n } } ( \frac { 1 } { r } ) ] \mathbf { d } \sigma - 4 \pi \mathbf { V _ { P } }
$$

3.P点正在(o)面上。此时也不能直接应用格林第二恒等式,也要类似于内部点那样处理。但不是作一小球，而是以(σ)面上的P点作一个很小的半球。通过相同的推导，最后得到如下的结果：

$$
\int \displaylimits _ { \tau } \frac { 1 } { \mathbf { r } } \Delta \mathbf { V } \mathbf { d } \tau = \int \lbrack \frac { 1 } { \mathbf { r } } \frac { \partial \mathbf { V } } { \partial \mathbf { n } } - \mathbf { V } \frac { \partial } { \partial \mathbf { n } } ( \frac { 1 } { \mathbf { r } } ) ] \mathbf { d } \sigma - 2 \pi \mathbf { V _ { p } }
$$

现将 $( 5 \cdot 1 1 )$ 、 $( 5 \cdot 1 8 )$ 和 $( 5 \cdot 1 9 )$ 式综合在一起，可写为

$$
\int \frac { 1 } { \tau } \Delta \mathbf { V } \mathbf { d } \tau - \intop _ { ( \sigma ) } \lbrack \frac { 1 } { \tau } \frac { \partial \mathbf { V } } { \partial \mathbf { n } } - \mathbf { V } \frac { \partial } { \partial \mathbf { n } } ( \frac { 1 } { \tau } ) ) \mathbf { d } \sigma = \left\{ \begin{array} { c c } { 0 } & { ( \mathbf { P } \mathrm { \# } \tau \leq \tau \nmid \mathbf { \hat { H } } ) } \\ { - 2 \pi \mathbf { V } _ { \mathrm { P } } } & { ( \mathbf { P } \mathrm { \# } \sigma \mathrm { \# } \bot \mathbf { E } ) } \\ { - \mathbf { \Pi } \mathbf { \pi } \mathbf { V } _ { \mathrm { P } } } & { ( \mathbf { P } \mathrm { \# } \tau \nmid \mathbf { \hat { H } } ) } \end{array} \right.
$$

$( 5 \cdot 2 0 )$ 式通常称为格林第三公式。它也可应用于 $( { \pmb \sigma } )$ 面外的无限空间 $\pmb { \tau }$ ，此时 $\mathbf { n }$ 仍是 $( { \pmb \sigma } )$ 面的关于τ的外法线方向，而函数V应满足在无穷远处正则的条件。

若在 $( 5 \cdot 2 0 )$ 式中，取函数 $\mathbf { v } { \equiv } 1$ 。此时有 $\Delta \mathbf { V } = 0 , { \frac { \partial \mathbf { V } } { \partial \mathbf { n } } } = 0$ 和 $\mathrm { v _ { p } } { = } 1$ ，故可得到

$$
\int \limits _ { ( \sigma ) } \frac { \partial } { \partial \mathbf { n } } ( \frac { 1 } { \mathbf { r } } ) \mathrm { d } \sigma = \left\{ \begin{array} { l l } { 0 } & { ( \mathrm { P } \mathrm { \mathop { / / } } \sigma \overline { { \mathrm { B i } } } \mathrm { P } \mathrm { \mathop { / } } \mathrm { P } ) } \\ { - \mathrm { \mathop { / } } \pi } & { ( \mathrm { P } \mathrm { \mathop { / / } } \sigma \overline { { \mathrm { B i } } } \mathrm { P } \mathrm { E } ) } \\ { - \mathrm { \mathop { / } } \pi } & { ( \mathrm { P } \mathrm { \mathop { / / } } \sigma \overline { { \mathrm { B i } } } \mathrm { P } \mathrm { P } \mathrm { M } ) } \end{array} \right.
$$

$( 5 \cdot 2 1 )$ 式给出了 $\mathbf { \Pi } ( \pmb { \sigma } )$ 面上的点至任一固定点 $\mathbf { P }$ 的距离倒数的对 ${ \bf ( \pmb { \sigma } ) }$ 面内法线的导数值的积分和，它随 $\mathbf { P }$ 点相关于 $\left( { \pmb \sigma } \right)$ 面的位置不同而异。

# $\$ 5.2$ 调和函数

如果一个函数 $\mathbf { U } ( \mathbf { x } , \mathbf { y } , \mathbf { z } )$ 在某一区域 $\pmb { \tau }$ 内直到二阶偏导都是有限和连续的，并且满足拉普拉斯方程，即

$$
\Delta \mathbf { U } { = } \frac { \partial ^ { 2 } \mathbf { U } } { \partial \mathbf { x } ^ { 2 } } { + } \frac { \partial ^ { 2 } \mathbf { U } } { \partial { y } ^ { 2 } } { + } \frac { \partial ^ { 2 } \mathbf { U } } { \partial { z } ^ { 2 } } { = } 0
$$

则此函数称为 $\pmb { \tau }$ 区域内的调和函数，亦称谐函数。若区域 $\pmb { \tau }$ 是某一界面 $\pmb { \sigma }$ 以外的无限空间，那么该函数U还应满足在无穷远处正则的条件。

这样的函数是很多的。例如：

$$
\mathrm { U } \left( \mathbf { x } , \mathbf { y } , \mathbf { z } \right) = 2 ( \mathbf { x } ^ { 2 } - \mathbf { z } ^ { 2 } ) + 3 \mathbf { x } \mathbf { y } + 4 \mathbf { z }
$$

它们都是一个封闭曲面 $\pmb { \sigma }$ 所包围的有限区域内的调和函数。因为它们在无穷远处不满足正则条件，故在无限空间内，它们就不是调和函数了。又如：函数 $\mathbf { U } ( \mathbf { x } , \mathbf { y } , \mathbf { z } )$ 是空间任一点 $( \mathbf { x } , \mathbf { y } , \mathbf { z } )$ 至某一固定点 $( \sum \eta , \zeta )$ 之间的距离 $\pmb { \tau }$ 的倒数，即

$$
\operatorname { U } ( \mathbf { x } , \mathbf { y } , z ) = { \frac { 1 } { \mathbf { r } } } = { \frac { 1 } { \sqrt { ( \mathbf { x } - \mathbf { \xi } ) ^ { 2 } + ( \mathbf { y } - \mathbf { \eta } \mathbf { \xi } \mathbf { \eta } ) ^ { 2 } + ( z - \zeta ) ^ { 2 } } } }
$$

此函数不仅满足拉普拉斯方程，而且在无穷远处是正则的，因而它是在点 $( \varepsilon , \eta , \zeta )$ 以外的无限空间内的调和函数。

调和函数用球坐标 $( \pmb \rho , \pmb \theta , \pmb \lambda )$ 表示在使用上更为方便，其中 $P$ 是向径， $\pmb \theta$ 是极距， $\pmb { \lambda }$ 是经度。由图5.4可很容易地看出，球坐标与直角坐标有如下的关系：

$$
\scriptstyle \left. { \begin{array} { l } { \mathbf { x } = \rho { \mathrm { s i n } } \theta { \mathrm { c o s } } \lambda } \\ { \mathbf { y } = \rho { \mathrm { s i n } } \theta { \mathrm { s i n } } \lambda } \\ { \mathbf { z } = \rho { \mathrm { c o s } } \theta } \end{array} } \right\}
$$

![](images/29be84fbf98b172c830d23877cd2d961400639d1398cf8c989a47adda529fc5b.jpg)  
图5.4

调和函数实质上是拉普拉斯方程的解。为此，首先要得出以球坐标表达的拉普拉斯方程。在高等数学中给出了在任意正交曲线坐标系 $( \mathbf { u } _ { 1 } , \mathbf { u } _ { 2 } , \mathbf { u } _ { 3 } )$ 中的拉普拉斯算子32]为

$$
\Delta \mathrm { U } = \frac { 1 } { \mathbf { h } _ { 1 } \mathbf { h } _ { 2 } \mathbf { h } _ { 3 } } \lbrack \frac { \partial } { \partial \mathbf { u } _ { 1 } } ( \frac { \mathbf { h } _ { 2 } \ddot { \mathbf { h } } _ { 3 } } { \mathbf { h } _ { 1 } } \frac { \partial \mathrm { U } } { \partial \mathbf { u } _ { 1 } } ) + \frac { \partial } { \partial \mathbf { u } _ { 2 } } ( \frac { \mathbf { h } _ { 3 } \mathbf { h } _ { 1 } } { \mathbf { h } _ { 2 } } \frac { \partial \mathrm { U } } { \partial \mathbf { u } _ { 2 } } ) + \frac { \partial } { \partial \mathbf { u } _ { 3 } } ( \frac { \mathbf { h } _ { 1 } \mathbf { h } _ { 2 } } { \mathbf { h } _ { 3 } } \frac { \partial \mathrm { U } } { \partial \mathbf { u } _ { 3 } } ) \rbrack
$$

式中 $\mathbf { h } _ { 1 } , \mathbf { h } _ { 2 }$ 和 $h _ { 3 }$ 称为尺度因子，可通过直角坐标由下列公式求定：

$$
\left. \begin{array} { r } { \mathrm { h } _ { 1 } ^ { 2 } = ( \frac { \partial \mathbf { x } } { \partial \mathbf { u } _ { 1 } } ) ^ { 2 } + ( \frac { \partial \mathbf { y } } { \partial \mathbf { u } _ { 1 } } ) ^ { 2 } + ( \frac { \partial \mathbf { z } } { \partial \mathbf { u } _ { 1 } } ) ^ { 2 } } \\ { \mathrm { h } _ { 2 } ^ { 2 } = ( \frac { \partial \mathbf { x } } { \partial \mathbf { u } _ { 2 } } ) ^ { 2 } + ( \frac { \partial \mathbf { y } } { \partial \mathbf { u } _ { 2 } } ) ^ { 2 } + ( \frac { \partial \mathbf { z } } { \partial \mathbf { u } _ { 2 } } ) ^ { 2 } } \\ { \mathrm { h } _ { 3 } ^ { 2 } = ( \frac { \partial \mathbf { x } } { \partial \mathbf { u } _ { 3 } } ) ^ { 2 } + ( \frac { \partial \mathbf { y } } { \partial \mathbf { u } _ { 3 } } ) ^ { 2 } + ( \frac { \partial \mathbf { z } } { \partial \mathbf { u } _ { 3 } } ) ^ { 2 } } \end{array} \right\}
$$

对于上述的球坐标,有

$$
u _ { 1 } = \rho \qquad u _ { 2 } = \theta \qquad v _ { 3 } = \lambda
$$

由 $( 5 \cdot 2 4 )$ 式求出 $\mathbf { x } , \mathbf { y } , \pmb { z }$ 对 $\rho , \theta , \lambda$ 的各个偏导数，并代人 $( 5 \cdot 2 6 )$ 式，经运算后可得

$$
\begin{array} { r } { \mathbf { h } _ { 1 } = 1 \qquad \quad \mathbf { h } _ { 2 } = \boldsymbol { \rho } \qquad \quad \mathbf { h } _ { 3 } = \boldsymbol { \rho } \sin \theta } \end{array}
$$

将它们代入 $( 5 \cdot 2 5 )$ 式，得到

$$
\Delta { \bf U } = \frac { 1 } { \rho ^ { 2 } } \frac { \partial } { \partial \boldsymbol { \mathbf { \rho } } } ( \rho ^ { 2 } \mathrm { ~ \frac { \partial U } { \partial \boldsymbol { \mathbf { \rho } } } ~ } ) + \frac { 1 } { \rho ^ { 2 } \mathrm { s i n } \theta } \frac { \partial } { \partial \boldsymbol { \mathbf { \theta } } } ( \mathrm { s i n } \theta \mathrm { ~ \frac { \partial U } { \partial \boldsymbol { \mathbf { \theta } } } ) + \frac { 1 } { \rho ^ { 2 } \mathrm { s i n } ^ { 2 } \theta } \frac { \partial { \bf U } } { \partial \boldsymbol { \mathbf { \alpha } } ^ { 2 } } }
$$

完成求导后就可得到拉普拉斯方程的球坐标表达式：

$$
\frac { \partial \mathcal { A } } { \partial \boldsymbol { \rho } ^ { 2 } } + \frac { 2 } { \rho } \frac { \partial \mathcal { U } } { \partial \boldsymbol { \rho } } + \frac { 1 } { \rho ^ { 2 } } \frac { \partial ^ { 2 } \mathrm { U } } { \partial \boldsymbol { \theta } ^ { 2 } } + \frac { \mathrm { c t g } \theta \partial \mathcal { U } } { \rho ^ { 2 } } + \frac { 1 } { \rho ^ { 2 } \sin ^ { 2 } \theta } \frac { \partial ^ { 2 } \mathrm { U } . } { \partial \boldsymbol { \rho } ^ { 2 } } = 0
$$

两端乘以 $p ^ { 2 }$ ，得到另一种形式：

$$
\rho ^ { 2 } \ \frac { \partial \sp { 2 } \mathrm { U } } { \partial \rho ^ { 2 } } + 2 \rho \ \frac { \partial \mathrm { U } } { \partial \rho } + \frac { \partial \sp { 2 } \mathrm { U } } { \partial \theta ^ { 2 } } + \cot \theta \ \frac { \partial \mathrm { U } } { \partial \theta } + \frac { 1 } { \sin ^ { 2 } \theta } \frac { \partial \mathrm { U } } { \partial \Lambda ^ { 2 } } = 0
$$

解拉普拉斯方程(5·28)可以用分离变量法，即假定：

$$
\mathbf { U } _ { \mathbf { \Phi } ( \rho , \theta , \mathbf { \lambda } \mathbf { \lambda } ) } { = } \mathbf { f } \left( \rho \right) \mathbf { Y } \left( \theta , \lambda \right)
$$

其中f(p)为只含变量p的函数,而Y(0,λ)只是变量θ和入的函数。将(5·29)式代入(5·28)式，得到

$$
[ \rho ^ { 2 } \mathbf { f } ^ { n } ( \rho ) + 2 \mathbf { f } ^ { \prime } ( \rho ) ] \mathbf { Y } ( \theta , \lambda ) = - [ \frac { \partial ^ { 2 } \mathbf { Y } ( \theta , \lambda ) } { \partial \theta ^ { 2 } } + \mathrm { c t g } \theta \frac { \partial \mathbf { Y } ( \theta , \lambda ) } { \partial \theta } + \frac { 1 } { \sin ^ { 2 } \theta } \frac { \partial \mathbf { Y } ( \theta , \lambda ) } { \partial \theta ^ { 2 } } ] \mathbf { f } ( \rho )
$$

式中符号“'"表示对 $P$ 的导数。将上式以 $\mathbf { f } ( \pmb { \rho } ) \mathbf { Y } ( \pmb { \theta } , \pmb { \lambda } )$ 除之，则得

$$
\frac { 1 } { \mathbf { f } \left( \rho \right) } \big [ \varrho ^ { 2 } \mathbf { f } ^ { \prime \prime } ( \rho ) + 2 \rho \mathbf { f } ^ { \prime } \left( \rho \right) \big ] = - \frac { 1 } { \mathbf { Y } ( \theta , \lambda ) } \big [ \frac { \partial ^ { \prime } \mathbf { Y } \left( \theta , \lambda \right) } { \partial \theta ^ { 2 } } + \mathrm { c t g } \theta \frac { \partial \mathbf { Y } \left( \theta , \lambda \right) } { \partial \theta } + \frac { 1 } { \mathrm { s i n } ^ { 2 } \theta } \frac { \partial ^ { \prime } \mathbf { Y } \left( \theta , \lambda \right) } { \partial \theta ^ { 2 } } \big ]
$$

该等式的左边只与变量p有关，右边只与变量θ和入有关，两端要相等，只能是等于一个常数。今以 $\mathfrak { n } ( \mathfrak { n } + 1 )$ 表示这个常数，则得两个微分方程：

$$
\rho ^ { 2 } \mathbf { f } ^ { \prime \prime } ( \mathsf { p } ) + 2 \mathsf { \rho } \mathbf { f } ^ { \prime } \left( \mathsf { p } \right) - \mathbf { n } ( \mathsf { n } + 1 ) \mathbf { f } \left( \mathsf { p } \right) = 0
$$

$$
\frac { \partial ^ { 2 } \Upsilon ( \theta , \lambda ) } { \partial \theta ^ { 2 } } + \mathrm { c t } \mathbf { g } \theta \frac { \partial \mathbf { Y } ( \theta , \lambda ) } { \partial \theta } + \frac { 1 } { \sin ^ { 2 } \theta } \frac { \partial ^ { 2 } \mathbf { Y } ( \theta , \lambda ) } { \partial \lambda ^ { 2 } } + _ { \mathbf { n } } ( \mathbf { n } + 1 ) \mathbf { Y } ( \theta , \lambda ) = 0
$$

依据微分方程知识，方程 $( 5 \cdot 3 0 )$ 的解为

$$
{ \mathfrak { f } } ( { \mathfrak { p } } ) = { \mathfrak { p } } ^ { \mathrm { { s } } } { \mathfrak { k } } \parallel { \mathfrak { f } } ( { \mathfrak { p } } ) = { \frac { 1 } { { \mathfrak { p } } ^ { { \mathrm { n } } + 1 } } }
$$

将 $( 5 \cdot 3 1 )$ 式的解以未知函数 $\Upsilon _ { \mathfrak { n } } ( \theta , \lambda )$ 表示，则 $( 5 \cdot 2 8 )$ 式的解应为

$$
\mathrm { U } _ { ( \rho , \theta , \lambda ) } { = } \rho ^ { n } \mathrm { Y } _ { \mathfrak { n } } ( \theta , \lambda ) \sharp \sharp \mathrm { U } _ { ( \rho , \theta , \lambda ) } { = } \frac { \mathrm { Y } _ { \mathfrak { n } } ( \theta , \lambda ) } { \rho ^ { n + 1 } }
$$

以后将看到，其中的n不是任意的常数，而必须是正整数。而对于一个线性微分方程，知道它的几个特解，那末，这些解的线性组合就是它的通解。因此，得到拉普拉斯方程的通解为

$$
\begin{array} { r } { \textrm { U } _ { ( \rho , \theta , \lambda ) } = \overset { \infty } { \underset { \mathbf { n } = 0 } { \sum } } \rho ^ { \mathrm { n } } \Upsilon _ { \mathbf { n } } ( \theta , \lambda ) \not \equiv \mathfrak { A } \equiv \mathbf { U } _ { ( \rho , \theta , \lambda ) } = \overset { \infty } { \underset { \mathbf { n } = 0 } { \sum } } \frac { \mathbf { Y } _ { \mathbf { n } } ( \theta , \lambda ) } { \displaystyle \rho ^ { \mathsf { n } + 1 } } } \end{array}
$$

下面解方程 $( 5 \cdot 3 1 )$ ，以确定 $\Upsilon _ { \mathfrak { n } } ( \theta , \lambda )$ 的表达式。仍采用分离变量法，令

$$
\Upsilon _ { \mathbf { n } } \langle ( \theta , \lambda ) { = } \mathbf { g } ( \theta ) \mathbf { h } \left( \lambda \right)
$$

将它代入 $( 5 \cdot 3 1 )$ 式，得到

$$
\ln ( \lambda ) \left( { \bf g } ^ { \prime \prime } ( \theta ) + \mathrm { c t g } \theta { \bf g } ^ { \prime } \left( \theta \right) \right) + \frac { 1 } { \sin ^ { 2 } \theta } { \bf h } ^ { \prime \prime } ( \lambda ) { \bf g } \left( \theta \right) + { \bf n } ( { \bf n } + 1 ) { \bf g } \left( \theta \right) { \bf h } \left( \lambda \right) = 0
$$

两端乘以 $\frac { \sin ^ { 2 } \theta } { \pmb { g } ( \theta ) \mathbf { h } ( \lambda ) }$ ，则得

$$
\sum _ { g ( \theta ) } ^ { \prime } ( \sin \theta _ { \mathrm { g } } ^ { \prime \prime } ( \theta ) + \cos \theta _ { \mathrm { g ^ { \prime } } } ( \theta ) + \mathcal { \Lambda } ( \mathsf { n } + 1 ) \sin \theta _ { \mathrm { g } } ( \theta ) ] = - \frac { \mathbf { \dot { h } } ^ { \prime } ( \dot { \mathsf { \mathcal { X } } } ) } { \mathbf { \dot { h } } ( \lambda ) } .
$$

该等式的左端只与变量θ有关，而右端只与变量入有关，等式两端要相等，只能等于一个常数。现令此常数为 $\mathbf { m } ^ { 2 }$ ，则可得到两个微分方程：

$$
\mathrm { s i n } \theta \mathbf { g } ^ { \prime \prime } ( \theta ) + \mathrm { c o s } \theta \mathbf { g } ^ { \prime } \left( \theta \right) + \mathrm { \mathcal { \mathrm { \Lambda } } } ( { \mathbf { n } } ( { \mathbf { n } } + 1 ) \mathrm { s i n } \theta - \frac { \mathbf { m } ^ { 2 } } { \mathrm { s i n } \theta } \dot { \mathbf { \tilde { g } } } \left( \theta \right) = 0
$$

和

$$
\mathbf { h } ^ { \prime \prime } ( \lambda ) + \mathbf { m } ^ { 2 } \mathbf { h } \left( \lambda \right) = 0
$$

依据微分方程知识， $( 5 \cdot 3 8 )$ 式的解为

而方程(5·37)就是勒戎德微分方程,它的解是勒戎德函数 $\pmb { \mathrm { P } } _ { \pmb { \mathrm { n m } } } ( \pmb { \mathrm { c o s } } \theta )$ 。因此有

$$
\mathtt { g } ( \theta ) { = } \mathtt { P } _ { \mathtt { n m } } ( \cos \theta )
$$

将 $( 5 \cdot 3 9 )$ 和 $( 5 \cdot 4 0 )$ 式代入 $( 5 \cdot 3 5 )$ 式，则得 $( 5 \cdot 3 1 )$ 式的解为

$$
\mathbf { Y _ { n } } \left( \theta , \lambda \right) { = } \mathbf { P } _ { \mathrm { { n m } } } \left( \cos \theta \right) \cos { \mathbf { m } } \lambda \ \sharp \mathbf { l } \ \mathbf { Y } _ { \mathrm { { n } } } \left( \theta , \lambda \right) { = } \mathbf { P } _ { \mathrm { { n m } } } \left( \cos \theta \right) \sin \lambda
$$

四为 $( 5 \cdot 3 1 )$ 式是线性微分方程，故 $( 5 \cdot 4 1 )$ 的线性组合是它的通解。其一般形式为

$$
\Upsilon _ { \mathfrak { n } } ( \theta , \mathfrak { \lambda } ) = \sum _ { \mathfrak { n } : = 0 } ^ { \mathfrak { n } } ( \mathtt { A } _ { \mathfrak { n } \mathfrak { m } } \mathtt { c o s m a } \mathtt { \lambda } + \mathtt { B } _ { \mathfrak { n } \mathfrak { m } } \mathtt { s i n m } \mathtt { \lambda } ) \mathrm { P } _ { \mathfrak { n } \mathfrak { m } } ( \mathtt { c o s } \theta )
$$

式中 $\mathsf { A } _ { \mathsf { n m } }$ 和 $\mathtt { B } _ { \mathtt { n m } }$ 为任意的常数。

将 $( 5 \cdot 4 2 )$ 式代入 $( 5 \cdot 3 4 )$ 式,得到拉普拉斯方程 $( 5 \cdot 2 8 )$ 的解,也是以球坐标表示的调和函数的一般表达式。若以半径为 $\mathbf { R }$ 的球面作为界面，则球外调和函数的一般形式为：

$$
\mathbf { U } _ { \mathrm { e } } ( \boldsymbol { \rho } , \boldsymbol { \theta } , \lambda ) = \sum _ { \mathfrak { n } = \mathfrak { c } } ^ { \infty } \frac { \mathrm { R } ^ { \mathfrak { n } } } { \boldsymbol { \rho } ^ { \mathfrak { n } + 1 } } \sum _ { \mathfrak { m } = 0 } ^ { \mathfrak { n } } ( \mathbf { C } _ { \mathfrak { n } \mathfrak { m } } \mathrm { c o s } \mathrm { m } \lambda + \mathbf { S } _ { \mathfrak { n } \mathfrak { m } } \mathrm { s i n } \mathrm { m } \lambda ) \mathbf { P } _ { \mathfrak { n } \mathfrak { m } } ( \mathrm { c o s } \boldsymbol { \theta } )
$$

球内调和函数的一般形式为：

$$
\mathrm { U _ { i } } ( \rho , \theta , \lambda ) = \sum _ { n = 0 } ^ { \infty } { \frac { \rho ^ { n } } { \mathrm { R } ^ { n + 1 } } } \sum _ { \mathrm { { n } = 0 } } ^ { \infty } ( \mathrm { C } _ { \mathrm { { n m } } } \mathrm { { c o s m } \lambda + \mathrm { S } _ { \mathrm { { n m } } } \mathrm { { s i n m } \lambda ) \mathrm { P } _ { \mathrm { { n m } } } ( \mathrm { { c o s } \theta ) } } }
$$

式中 $\mathbf { C _ { n m } }$ 和 $\mathsf { \pmb { S } } _ { \mathsf { n m } }$ 为常系数，它们的具体数值与函数 $\mathbf { U }$ 有关。例如：对于球内的调和函数 ${ \bf U } = { \bf C }$ ，当用 $( 5 \cdot 4 4 )$ 式表示时，式中的 $\mathrm { C } _ { \mathsf { G } \mathsf { \bar { y } } } { = } \mathbf { R } \mathrm { C }$ ，而其他的 $\mathbf { C } _ { \mathbf { n } \mathbf { m } }$ 和 $\mathsf { S } _ { \mathsf { n m } }$ 都为零;对于球内的调和函数 $\mathbf { U } =$ $2 ( \mathbf { x } ^ { 2 } - \mathbf { z } ^ { 2 } ) + 3 \mathbf { x } \mathbf { y } + 4 \mathbf { z }$ ，用球谐函数的级数式可表示为

$$
\mathrm { U } \left( \rho ; \theta ; \lambda \right) = 4 \rho \mathrm { P } _ { 1 0 } \left( \cos \theta \right) - 2 \rho ^ { 2 } \mathrm { P } _ { 2 0 } \left( \cos \theta \right) + \rho ^ { 2 } ( \frac { 1 } { 3 } \cos 2 \lambda + \frac { 1 } { 2 } \sin 2 \lambda ) \mathrm { P } _ { 2 2 } \left( \cos \theta \right)
$$

相当于 $( 5 \cdot 4 4 )$ 式中的 ${ \bf C } _ { 1 0 } = { 4 { \bf R } ^ { 2 } } , { \boldsymbol { \Sigma } } _ { 2 0 } = - 2 { \bf R } ^ { 3 } , { \bf C } _ { 2 2 } = \frac { 1 } { 3 } { \bf R } ^ { 3 } , { \bf S } _ { 2 2 } = \frac { 1 } { 2 } { \bf R } ^ { 3 }$ ，而其他的 $C _ { n m }$ 和 $\mathsf { \pmb { S } } _ { \mathbf { n m } }$ 都为

对于调和函数 $\mathbf { U } = \frac { 1 } { \mathbf { \rho } _ { \mathbf { r } } }$ ，设距离 $\mathbf { r }$ 两端点 $\mathtt { P } _ { 0 }$ 和 $\mathbf { P }$ 的坐标分别为 $( \mathbf { R } , \theta _ { 0 } , \lambda _ { 0 } )$ 和 $( \rho , \theta , \lambda )$ ，见图5.5,则

$$
\frac { 1 } { \mathrm { r } } { = } \frac { 1 } { \sqrt { \rho ^ { 2 } + \mathrm { R } ^ { 2 } - 2 \rho \mathrm { R } \mathrm { c o s } \emptyset } }
$$

式中 $\psi$ 为向径 $P$ 和 $\mathbf { R }$ 之间的夹角。设 $\rho { \mathrm { > R } } , \alpha { = } \frac { \mathbb { R } } { \rho }$ 和 $\scriptstyle { \mathfrak { u } } = { \mathfrak { c o s } } \psi$ ，则得

$$
\frac { 1 } { \tau } = \frac { 1 } { \rho \ \sqrt { 1 - 2 \alpha \mathbf { u } + \mathbf { u } ^ { 2 } } }
$$

等式右端可以展开为 $\pmb { \alpha }$ 的幂级数，且 $\pmb { \alpha } ^ { \tt n }$ 的系数为勒戎德多项式 $\mathrm { P _ { n } } ( \mathbf { u } ) { = } \mathrm { P _ { n } } ( \cos \psi )$ 。因此，得到

$$
\frac { \ d S } { \ d t } = \sum _ { \mathfrak { n } = 0 } ^ { \infty } \frac { \ d \mathbb { R } ^ { \mathfrak { n } } } { \ d \mathfrak { p } ^ { \mathfrak { n } + 1 } } \mathbb { P } _ { \mathfrak { n } } ( \mathrm { c o s } \psi )
$$

由球函数的加法定理[4,有

$$
{ \begin{array} { r l } & { \mathsf { P } _ { n } ( \cos \psi ) = \mathsf { P } _ { \mathsf { n o } } ( \cos \theta _ { 0 } ) \mathsf { P } _ { \mathsf { n o } } ( \cos \theta ) } \\ & { \qquad + \underbrace { { \bar { \mathsf { \Pi } } } ^ { \sharp } } _ { \mathsf { n } = 1 } \underbrace { 2 \left( \mathsf { n } - \mathsf { m } \right) ! } _ { ( \mathsf { n } + \mathsf { r } \mathtt { n } ) ! } \mathsf { P } _ { \mathsf { n } \mathsf { n } } ( \cos \theta _ { 0 } ) ( \cos \mathsf { m } \lambda _ { 0 } \cos \mathsf { m } \lambda + \mathsf { s i n } \mathsf { m } \lambda _ { 0 } \mathsf { s i n } \mathsf { m } \lambda ) \mathsf { P } _ { \mathsf { n } \mathsf { n } } ( \cos \theta ) } \end{array} }
$$

![](images/ba7f9596447cbf51c44ee0463a4a7e4f30f9f3cd5eb554a6e491cdfbd118850b.jpg)  
图5.5

将它代入 $( 5 \cdot 4 5 )$ 式，就将 $\frac { 1 } { \tt { r } }$ 表示为(5·44)的形式,其中

$$
\begin{array} { r l } & { \mathbf { C } _ { \mathfrak { n } 0 } = \mathbf { P } _ { \mathfrak { n } 0 } ( \cos \theta _ { 0 } ) } \\ & { \mathbf { C } _ { \mathfrak { n } \mathfrak { n } } { = } 2 \ \frac { ( \mathbf { n } - \mathbf { m } ) ! } { ( \mathbf { n } + \mathbf { m } ) ! } \mathbf { P } _ { \mathfrak { n } \mathfrak { m } } ( \cos \theta _ { 0 } ) \cos \mathbf { m } \lambda _ { 0 } \Bigg \} _ { ( \mathbf { m } > 0 ) } } \\ & { \mathbf { S } _ { \mathfrak { n } \mathfrak { m } } { = } 2 \ \frac { ( \mathbf { n } - \mathbf { m } ) ! } { ( \mathbf { n } + \mathbf { m } ) ! } \mathbf { P } _ { \mathfrak { n } \mathfrak { m } } ( \cos \theta _ { 0 } ) \sin \lambda _ { 0 } \Bigg \} ^ { ( \mathbf { m } > 0 ) } } \end{array}
$$

# $\ S 5 . 3$ 调和函数的性质

归纳一下 $\ S \ 4 . 4$ 中得出的质体对外部点引力位的性质，可以明确地看出，质体对外部点的引力位是一个调和函数。因此，对调和函数的性质作深入的探讨是非常必要的。

1.若 $\mathbf { V _ { 1 } }$ 和 $\mathbf { V } _ { 2 }$ 都是区域 $\pmb { \tau }$ 内的调和函数，那末，由这两个函数的线性组合而成的新函数

$$
{ \bf U } = { \bf C } _ { 1 } { \bf V } _ { 1 } + { \bf C } _ { 2 } { \bf V } _ { 2 }
$$

也是区域 $\pmb { \tau }$ 内的调和函数，其中的 $\mathrm { C _ { 1 } }$ 和 $\mathrm { C } _ { 2 }$ 是任意的常数。

2.区域 $\pmb { \tau }$ 内的调和函数 $\mathbf { v }$ 的对坐标轴的任意阶偏导数，即

$$
\mathbf { U } = \frac { \partial ^ { \mathbf { z } + \beta + \gamma } \mathbf { V } } { \partial \mathbf { x } ^ { \alpha } \partial \mathbf { y } ^ { \beta } \partial \mathbf { z } ^ { \gamma } }
$$

也是该区域内的调和函数，其中的 $\alpha \lrcorner \beta \lrcorner \gamma$ 是零或任意的正整数。

在证明时可从 $\mathbf { U } = { \frac { \partial \mathbf { V } } { \partial \mathbf { x } } }$ 开始。显然有

$$
{ \frac { \partial \mathbf { U } } { \partial \mathbf { x } } } = { \frac { \partial ^ { 2 } \mathbf { V } } { \partial \mathbf { x } ^ { 2 } } } { \frac { \partial \mathbf { U } } { \partial \mathbf { y } } } = { \frac { \partial \mathbf { U } } { \partial \mathbf { y } } } = { \frac { \partial ^ { 2 } \mathbf { V } } { \partial \mathbf { x } \partial \mathbf { y } } } { \frac { \partial \mathbf { U } } { \partial \mathbf { z } } } = { \frac { \partial ^ { 2 } \mathbf { V } } { \partial \mathbf { x } \partial \mathbf { z } } }
$$

再分别对 $\mathbf { x } , \mathbf { y } , \mathbf { z }$ 求一次偏导数,则得

$$
{ \frac { \partial ^ { 2 } \mathbf { U } } { \partial \mathbf { x } ^ { 2 } } } = { \frac { \partial ^ { 3 } \mathbf { V } } { \partial \mathbf { x } ^ { 3 } } } \quad \quad \quad { \frac { \partial ^ { 2 } \mathbf { U } } { \partial \mathbf { y } ^ { 2 } } } { = } { \frac { \partial ^ { 3 } \mathbf { V } } { \partial \mathbf { x } \partial \mathbf { y } ^ { 2 } } } \quad \quad \quad { \frac { \partial ^ { 2 } \mathbf { U } } { \partial { \boldsymbol { z } } ^ { 2 } } } { = } { \frac { \partial ^ { 3 } \mathbf { V } } { \partial \mathbf { x } \partial { \boldsymbol { z } } ^ { 2 } } }
$$

将这三个二阶偏导数相加，则得拉普拉斯算子 $\pmb { \triangle } \pmb { \mathrm { U } }$ 为

$$
\Delta \mathbf { U } = \frac { \partial } { \partial \pmb { \kappa } } ( \frac { \partial ^ { 2 } \mathbf { V } } { \partial \pmb { \kappa } ^ { 2 } } ) + \frac { \partial } { \partial \pmb { \kappa } } ( \frac { \partial ^ { 2 } \mathbf { V } } { \partial \mathbf { y } ^ { 2 } } ) + \frac { \partial } { \partial \pmb { \kappa } } ( \frac { \partial ^ { 2 } \mathbf { V } } { \partial \pmb { z } ^ { 2 } } ) = \frac { \partial } { \partial \pmb { \kappa } } ( \Delta \mathbf { V } )
$$

因为 $\mathbf { v }$ 是调和函数，有 $\Delta { \bf V } { = } 0$ 故必然有 $\Delta \mathbf { U } { = } 0$ 。这说明 $\frac { \partial V } { \partial x }$ 是调和函数。

同理可得 $\frac { \partial \mathbf { V } } { \partial \mathbf { y } } \neq \parallel \frac { \partial \mathbf { V } } { \partial \mathbf { z } }$ 也是调和函数。这就证明了调和函数的任意一阶偏导数仍为调和函数。

对这新的调和函数再应用上述的结论，就可得出任意二阶偏导数也是调和函数。依次类推下去，即可得出调和函数对坐标轴的任意阶偏导数都是调和函数的结论。

3.若 $\mathbf { v }$ 是区域 $\pmb { \tau }$ 内的调和函数，则函数

$$
\mathrm { U } = \rho \ : \frac { \partial \mathrm { V } } { \partial \rho }
$$

也是该区域内的调和函数。其中 $P$ 是至坐标原点的向径,即 $\pmb { \rho } = \sqrt { \mathbf { x } ^ { 2 } + \mathbf { y } ^ { 2 } + \mathbf { z } ^ { 2 } }$ 。因为

$$
\frac { \partial \mathbf { V } } { \partial \mathbf { \nabla } } = \frac { \partial \mathbf { V } } { \partial \mathbf { x } } \frac { \partial \mathbf { x } } { \partial \mathbf { \nabla } } + \frac { \partial \mathbf { V } } { \partial \mathbf { y } } \frac { \partial \mathbf { y } } { \partial \mathbf { \nabla } } + \frac { \partial \mathbf { V } } { \partial \mathbf { z } } \frac { \partial \mathbf { z } } { \partial \mathbf { \nabla } }
$$

而

$$
\frac { \partial \mathbf { x } } { \partial \boldsymbol { \mathsf { p } } } = \frac { \mathbf { x } } { \boldsymbol { \mathsf { \rho } } } \qquad \frac { \partial \mathbf { y } } { \partial \boldsymbol { \mathsf { p } } } = \frac { \mathbf { y } } { \boldsymbol { \mathsf { \rho } } } \qquad \frac { \partial \boldsymbol { z } } { \partial \boldsymbol { \mathsf { p } } } = \frac { \mathbf { z } } { \boldsymbol { \mathsf { \rho } } }
$$

故有

$$
\frac { \partial \mathrm { \bf V } } { \partial \mathrm { \bf p } } = \frac { \partial \mathrm { \bf V } } { \partial \mathrm { \bf x } } \frac { \mathrm { \bf x } } { \mathrm { \bf \nabla \rho } } + \frac { \partial \mathrm { \bf V } } { \partial \mathrm { \bf y } } \frac { \mathrm { \bf y } } { \mathrm { \bf \rho } } + \frac { \partial \mathrm { \bf V } } { \partial \mathrm { \bf z } } \frac { \mathrm { \bf z } } { \mathrm { \bf \rho } }
$$

将它代入 $( 5 \cdot 4 7 )$ 式，得到

$$
{ \boldsymbol { \mathrm { U } } } = \mathbf { x } { \frac { \partial \mathbf { V } } { \partial \mathbf { x } } } + \mathbf { y } { \frac { \partial \mathbf { V } } { \partial { \boldsymbol { \mathbf { y } } } } } + z { \frac { \partial \mathbf { V } } { \partial z } }
$$

·先将右边第一项对 $\pmb { \mathrm { x } }$ 求偏导数，可得.

$$
\frac { \partial } { \partial \mathbf { x } } ( \mathbf { x } \ \frac { \partial \mathbf { V } } { \partial \mathbf { x } } ) = \mathbf { x } \ \frac { \partial ^ { 2 } \mathbf { V } } { \partial \mathbf { x } ^ { 2 } } + \frac { \partial \mathbf { V } } { \partial \mathbf { x } }
$$

再对 $\pmb { x }$ 求一次偏导数，则得

$$
\frac { \partial \mathcal { F } } { \partial \mathbf { x } ^ { 2 } } ( \mathbf { x } \ \frac { \partial \mathbf { V } } { \partial \mathbf { x } } ) = \mathbf { x } \ \frac { \partial } { \partial \mathbf { x } } ( \frac { \partial ^ { 2 } \mathbf { V } } { \partial \mathbf { x } ^ { 2 } } ) + 2 \ \frac { \partial \mathbf { V } } { \partial \mathbf { x } ^ { 2 } }
$$

而 $\mathbf { x } \ : \frac { \partial \mathbf { V } } { \partial \mathbf { x } }$ 对 $\mathbf { y }$ 和 $\pmb { z }$ 的二阶偏导数为

$$
\frac { \partial } { \partial y ^ { 2 } } ( \textbf x \frac { \partial \textbf V } { \partial \textbf x } ) = \textbf x \frac { \partial } { \partial \textbf x } ( \frac { \partial \textbf V } { \partial y ^ { 2 } } )
$$

$$
\frac { \partial } { \partial z ^ { 2 } } ( \mathbf { x } \ \frac { \partial \mathbf { V } } { \partial \mathbf { x } } ) { = } \mathbf { x } \ \frac { \partial } { \partial \mathbf { x } } ( \frac { \partial \mathbf { \nabla } \mathbf { V } } { \partial z ^ { 2 } } )
$$

这样就得到

$$
\Delta ( \mathbf { x } \ { \frac { \partial V } { \partial \mathbf { x } } } ) { = } \mathbf { x } \ { \frac { \partial } { \partial \mathbf { x } } } ( \Delta \mathbf { V } ) + 2 \ { \frac { \partial { \mathbf { V } } } { \partial \mathbf { x } ^ { 2 } } }
$$

因为 $\Delta \mathbf { V } = 0$ ，故

$$
\Delta ( \mathbf { x } \ { \frac { \partial \mathbf { V } } { \partial \mathbf { x } } } ) { = } 2 \ { \frac { \partial ^ { 2 } \mathbf { V } } { \partial \mathbf { x } ^ { 2 } } }
$$

类似地可以求得

$$
\begin{array} { c } { \displaystyle \Delta ( \mathbf { y } \frac { \partial N } { \partial \mathbf { y } } ) = 2 \frac { \partial ^ { 2 } \mathbf { V } } { \partial \mathbf { y } ^ { 2 } } } \\ { \displaystyle \Delta ( \mathbf { z } \frac { \partial \mathbf { V } } { \partial \mathbf { z } } ) = 2 \frac { \partial ^ { 2 } \mathbf { V } } { \partial \mathbf { z } ^ { 2 } } } \end{array}
$$

将这三个式子相加，则得

$$
\mathbf { \partial } \cdot \Delta \mathbf { U } = \Delta ( \mathbf { x } \ { \frac { \partial \mathbf { V } } { \partial \mathbf { x } } } ) + \Delta ( \mathbf { y } \ { \frac { \partial \mathbf { V } } { \partial \mathbf { y } } } ) + \Delta ( \mathbf { z } \ { \frac { \partial \mathbf { V } } { \partial \mathbf { z } } } ) = 2 ( \Delta \mathbf { V } ) = 0
$$

因此， $\rho \ : \frac { \partial \mathbf { V } } { \partial \rho }$ 满足拉普拉斯方程，至于连续、有限和无穷远处正则等是必然存在的，无需单独证明。故函数 $\mathbf { U } { = } \rho \frac { \partial \mathbf { V } } { \partial \boldsymbol { p } }$ 也是调和函数。

4.有限区域 $\pmb { \tau }$ 内的调和函数 $\mathbf { v }$ 的法线导数沿区域 $\pmb { \tau }$ 的界面 $\mathbf { \Pi } ( \pmb { \sigma } )$ 的积分等于零，即

$$
\int \limits _ { ( 0 ) } ^ { \partial V } \frac { \partial V } { \partial \mathrm { n } } \mathrm { d } \sigma = 0
$$

为了求证，应用格林第二恒等式 $( 5 \cdot 9 )$ ,其中的两个函数U和 $\mathbf { v }$ 分别假设为 $\mathbf { U } = \mathbf { 1 }$ 和 $\mathbf { v }$ 是调和函数。因为 $\Delta \mathbf { U } = 0 , { \frac { \partial \mathbf { V } } { \partial \mathbf { n } } } = 0$ 和 $\Delta \mathbf { V } { = } 0$ ，由 $( 5 \cdot 9 )$ 式很容易地就得到 $( 5 \cdot 4 8 )$ 式。

5.调和函数 $\mathbf { v }$ 及其法线导数 $\frac { \partial \mathbf { V } } { \partial \mathbf { n } }$ 的乘积在界面 $( { \pmb \sigma } )$ 上的积分值大于或等于零，即

$$
\int \limits _ { ( \sigma ) } ^ { } \nabla \frac { \partial { \mathbf { V } } } { \partial \mathbf { n } } \mathrm { d } \sigma \geqslant 0 .
$$

为了求证，在格林第一恒等式 $( 5 \cdot 7 )$ 中取 $\mathbf { U } = \mathbf { v }$ 且为调和函数，则得

$$
\int _ { \tau } \mathrm { \bf D } ( \mathrm { \bf V } , \mathrm { \bf V } ) \mathrm { d } \tau = \int _ { \mathrm { 0 } } \mathrm { \bf V } \frac { \partial \mathrm { \bf V } } { \partial \mathrm { \bf h } } \mathrm { d } \sigma
$$

其中

$$
\mathrm { D } ( \mathbf { V } , \mathbf { V } ) = ( \frac { \partial \mathbf { V } } { \partial \mathbf { x } } ) ^ { 2 } + ( \frac { \partial \mathbf { V } } { \partial \mathbf { y } } ) ^ { 2 } + ( \frac { \partial \mathbf { V } } { \partial \mathbf { z } } ) ^ { 2 }
$$

等式的右端为平方和，它的数值永远是正的，最小为零，所以

$$
\int \limits _ { \tau } \mathbf { D } ( \mathbf { V } , \mathbf { V } ) d \tau \geq 0
$$

因而等式 $( 5 \cdot 4 9 )$ 也成立。

对于怎样的调和函数 $\mathbf { V } ( 5 \cdot 4 9 )$ 和 $( 5 \cdot 5 1 )$ 式取等号呢？从 $( 5 \cdot 5 0 )$ 式看出，只有 $\mathbf { v } =$ 常数时，D(V，V)才可能为零，它在 $\mathbf { \Pi } ( \pmb { \sigma } )$ 面所围的有限区域 $\pmb { \tau }$ 内才是调和函数；而在无限空间，由于不满足无穷远正则的条件，它不是调和函数。因此，只有在应用于有限区域 $\pmb { \tau }$ 内的调和函数V$=$ 常数时， $( 5 \cdot 4 9 )$ 和 $( 5 \cdot 5 1 )$ 式才取等号。

6.区域 $\pmb { \tau }$ 内的调和函数 $\mathbf { v }$ 在任意点 $\mathbf { P }$ 处的值 $\mathbf { v _ { p } }$ 可以用在界面上的函数值和法线导数值来表示。下面推导其具体表达式。

在格林第三公式 $( 5 \cdot 2 0 )$ 中，取 $\mathbf { v }$ 是 $\pmb { \tau }$ 内的调和函数。由于 $\Delta \mathbf { V } { = } 0$ ，就可得到

$$
\mathbf { V } _ { \mathrm { r } } = { \frac { 1 } { \mathsf { q } } } \int _ { ( \circ ) } \subset \frac { 1 } { \mathsf { r } } { \frac { \partial \mathbf { V } } { \partial \mathrm { n } } } - \mathbf { V } { \frac { \partial } { \partial \mathrm { n } } } ( { \frac { 1 } { \mathsf { r } } } ) \mathsf { \hat { \Pi } } \mathrm { d } \sigma ^ { * }
$$

其中

$$
{ \bf q } = \left\{ \begin{array} { c c } { { 4 \pi } } & { { ( { \bf P } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \bar { \sf t } \mathrm { ~ } \tau \mathrm { ~ } \vec { \sf H } ) } } \\ { { \sf 2 } \bar { \bf \tau } } & { { ( { \bf P } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \bar { \sf t } \mathrm { ~ } \sigma \mathrm { ~ } \overline { { \sf H } } \mathrm { ~ } \mathrm { ~  ~ \cal ~ \cal ~ \cdot ~ } ) } } \end{array} \right.
$$

（5·52)式就是由界面上的函数值和外法线导数值推求区域内和界面上的调和函数值的公式，对于两种情况式中的q取不同的数值。（5·52)式不但适用于(o)面所围的有限区域，也适用于 $( \pmb { \sigma } )$ 面以外的无限空间，但要注意，两种情况下外法线 $\mathbf { n }$ 的指向是相反的。

对于界面(o)以外的无限空间内的调和函数(5·52)式可以改写为

$$
\mathrm { V _ { P } = \frac { 1 } { 4 \pi } \int _ { ( \sigma ) } [ \frac { i } { \tau } \frac { \partial V } { \partial n } - ( V - V _ { \circ } ) \frac { \partial } { \partial n } ( \frac { 1 } { r } ) ] d \sigma } _ { . }
$$

它不但可以应用于(σ)面外，而且也适用于(σ)面上.式中V为P点的向径与(σ)面相交处P。的函数值。将 $( 5 \cdot 5 4 )$ 式与 $( 5 \cdot 5 2 )$ 式相比较，多了一项 $\frac { 1 } { 4 \pi } \int _ { ( \sigma ) } \nabla _ { \mathfrak { o } } \frac { \partial } { \partial \mathfrak { n } } ( \frac { 1 } { \mathfrak { r } } ) \mathrm { d } \sigma _ { \mathfrak { o } }$ 依据 $( 5 \cdot 2 1 )$ 式可得：当P点在(σ)面外时，它为零;当P在(σ)面上时,它为 $\frac { \mathrm { { V } _ { P _ { 0 } } } } { 2 }$ 中 因此; $( 5 \cdot 5 4 )$ 式的结果与 $( 5 \cdot 5 2 )$ 式完全一样。 ：

7.设V为区域τ内的调和函数，在区域τ内有一半径为R的球，则调和函数V在球心O点的值 $\mathtt { V _ { \mathrm { 0 } } }$ 等于 $\mathbf { v }$ 在球面(S)上的值的积分中数，即

$$
\begin{array} { r } { \mathbf { V } _ { \circ } = \frac { 1 } { 4 \pi \mathbf { R } ^ { 2 } } \displaystyle \int _ { \mathbf { S } ) } \mathbf { V } \mathbf { d S } } \end{array}
$$

由 $( 5 \cdot 5 2 )$ 式有

$$
\mathrm { V } _ { \circ } = \frac { 1 } { 4 \pi } \underset { ( \mathrm { \Phi } ) } { \int } [ \frac { 1 } { \tau } \frac { \partial \mathrm { V } } { \partial \mathrm { n } } - \mathrm { V } \frac { \partial } { \partial \mathrm { n } } ( \frac { 1 } { \tau } ) ] \mathrm { d } \mathrm { S }
$$

因为 $\frac { 1 } { \tt r } | _ { { \tt s } } = \frac { 1 } { \tt R }$ ，再应用 $( 5 \cdot 4 8 )$ 式，则得

$$
\int _ { \langle { \bf S } \rangle } \frac { 1 } { \mathrm {  ~ r ~ } } \frac { \partial { \cal V } } { \partial \mathrm {  ~ \scriptstyle \Lambda ~ } } \mathrm { d } { \bf S } = \frac { 1 } { \mathrm {  ~ R ~ } } \int _ { \langle { \bf S } \rangle } \frac { \partial { \bf V } } { \partial \mathrm {  ~ \scriptstyle \Lambda ~ } } \mathrm { d } { \bf S } = 0
$$

又因外法线方向 $\pmb { \mathrm { n } }$ 重合于 $\pmb { \tau }$ 方向，故有

$$
\frac { \partial } { \partial \mathbf { n } } ( \frac { 1 } { \mathbf { \nabla } } ) \vert _ { \mathsf { s } } = \frac { \partial } { \partial \mathbf { r } } ( \frac { 1 } { \mathbf { \nabla } } ) \vert _ { \mathsf { s } } = - \frac { 1 } { \mathbf { r } ^ { 2 } } \vert _ { \mathsf { s } } = - \frac { 1 } { \mathsf { R } ^ { 2 } }
$$

因此

$$
\mathrm { - \int _ { \Omega } V \frac { \partial } { \partial \mathbf { n } } ( \frac { \partial } { \partial \mathbf { r } } ) d S = \frac { 1 } { R ^ { 2 } } \int _ { \Omega } V d S }
$$

将这两个结果代入 $( 5 \cdot 5 6 )$ 式，就得到 $( 5 \cdot 5 5 )$ 式。

8.区域内的调和函数在任意点上都不会有极大值或极小值。

证明这个性质应用反证法。假定在区域τ内某一点P处调和函数有极大值(或极小值),那末,它周围点上的函数值就一定比它小(或大)。再以P为中心作一个很小的球，则球面上调和函数值的积分中数就一定比P点的值小(或大),这就违背了前面讲的第七个性质。这说明有极值的假定不成立，应该是在区域内没有极值，而其最大或最小值位于界面的某处。

在区域内，调和函数值相等的点可以连接成一个连续的曲面，它将整个区域划分成为两部分：其中一部份区域中的函数值都大于曲面上的函数值;而在另一部份区域内的函数值都小于曲面上的函数值。如图5.6所示，在调和函数V=Vp的曲面上取一点P。如果在两侧的函数值都比Vp大(或小),则V就成为极小值(或极大值),这就违背了本条所讲的性质。因此，必然是一侧的函数值大于 $\mathbf { V _ { P } }$ ,而另一侧的函数值小于 ${ \bf { V } } _ { \ P }$ 。

由此还可得出，在 $\mathbf { v } =$ 常数的曲面上，函数 $\mathbf { v }$ 的法线导数应有相同的符号。

9.用界面 $( { \pmb \sigma } )$ 上的调和函数值可以唯一地确定区域内的调和函数。

![](images/cdccc6730065d3ba68f16dcd063589efcfd9ef79cc5f6e7ddbc43d1b71cf7b66.jpg)  
图5.6

假定能在区域内得出两个调和函数 $\mathbf { U _ { 1 } }$ 和 $\mathbf { { U } } _ { 2 }$ ，则它们在界面上的值应该是相同的，必然有 $( \mathbf { U } _ { 1 } - \mathbf { U } _ { 2 } ) _ { \circ } { \equiv } 0$ 。按照前面讲的第一个性质， $\mathbf { U } _ { 1 } - \mathbf { U } _ { 2 }$ 也是个调和函数。根据第八个性质，在区域内调和函数无极值。这样一来，调和函数 $\bf { U } _ { 1 } - \bf { U } _ { 2 }$ 在整个区域内只能是处处为零。这就明在整个区域内 $\mathbf { U } _ { 1 }$ 和$\mathbf { U _ { 2 } }$ 都是相等的，也就是说 $\bf { U } _ { 1 }$ 和 $\mathbf { U } _ { 2 }$ 是无区别的同一个函数。

# 5.4球外调和函数的径向导数

讨论从 $( 5 \cdot 5 4 )$ 式开始。当界面 $\mathbf { \sigma } ( \pmb { \sigma } )$ 为半径等于 $\pmb { \mathrm { R } }$ 的球面(∑）时， $( 5 \cdot 5 4 )$ 式还可写成如下的形式：

$$
\mathbf { V _ { P } } = \frac { 1 } { 4 \pi } \int \{ \frac { 1 } { \tau } ( \frac { \partial \mathbf { V } } { \partial \mathbf { n } } - ( \frac { \partial \mathbf { V } } { \partial \mathbf { n } } ) _ { 0 } \mathbf  \} - ( \mathbf { V } - \mathbf { V _ { 0 } } ) \frac { \partial } { \partial \mathbf { n } } ( \frac { 1 } { \mathbf { \mu _ { r } } } ) \} \mathrm { d } \Sigma + \frac { \mathbf { R } ^ { 2 } } { \rho } ( \frac { \partial \mathbf { V } } { \partial \mathbf { n } } ) _ { 0 }
$$

式中 $j$ 为 $\mathbf { P }$ 点的球心向径OP,见图 $5 . 7 { \ : } 5 _ { \circ }$ 和 $( \frac { \partial \mathbf { V } } { \partial \mathbf { n } } ) _ { 0 }$ 分别为向径 $P$ 与球面 $( \pmb { \Sigma } )$ 相交处 $\mathbf { P } _ { 0 }$ 的 $\mathbf { v }$ 和 $\frac { \partial \mathbf { V } } { \partial \mathbf { n } }$ 的数值。

将 $( 5 \cdot 5 7 )$ 式与 $( 5 \cdot 5 4 )$ 式相对照，除了后面多了一项以外，在积分号内也增加了一项。下面将证明，这两项会互相抵消的。因为

$$
\frac { 1 } { 4 \pi } \int _ { ( \Sigma ) } \frac { 1 } { \bf r } ( \frac { \partial V } { \partial \bf \Phi } ) _ { \circ } { \sf d } \Sigma = ( \frac { \partial V } { \partial \bf \Phi } ) _ { \circ } \frac { 1 } { 4 \pi } \int _ { \Sigma } \frac { { \sf d } \Sigma } { \bf r }
$$

考虑到

$$
\scriptstyle \mathbf { r } = { \sqrt { \theta ^ { 2 } + R ^ { 2 } - 2 \rho \mathbf { R } \cos \psi } } .
$$

$$
\mathrm { d } \Sigma = \mathrm { R } ^ { 2 } \mathrm { s i n } \psi \mathrm { d } \psi \mathrm { d } \alpha
$$

可以求得

![](images/29d1d877bc7a93bab6816165e42477837f1931fa61ffffb988f2eb323eb70165.jpg)  
图5.7

$$
\int _ { \bar { \mathbf { \Gamma } } } { \frac { \mathrm { d } \Sigma } { \mathbf { r } } } = { \frac { 4 \pi \mathbf { R } ^ { 2 } } { \rho } }
$$

因此可得

$$
- \frac { 1 } { 4 \pi } { \int _ { ( \bar { \bf z } ) } { \frac { 1 } { \bar { \bf \Gamma } } ( \frac { \partial V } { \partial \bar { \bf n } } ) _ { \dot { 0 } } } } \mathrm { d } \bar { \bf \Sigma } + \frac { { \bf R } ^ { 2 } } { \rho } ( \frac { \partial V } { \partial \bar { \bf n } } ) _ { 0 } = 0 \mathrm { ~ }
$$

这说明 $( 5 \cdot 5 7 )$ 式是成立的。

下面由 $( 5 \cdot 5 7 )$ 式推求球外的调和函数 $\mathbf { v }$ 的径向导数 $\cdot \frac { \partial \mathbb { V } } { \partial \mathbb { P } }$ 。显然有

$$
\frac { \partial \mathbf { V } } { \partial \mathbf { p } } = \frac { 1 } { 4 \pi } \int \{ [ \frac { \partial \mathbf { V } } { \partial \mathbf { n } } - ( \frac { \partial \mathbf { V } } { \partial \mathbf { n } } ) _ { 0 } ] \frac { \partial } { \partial \mathbf { p } } ( \frac { 1 } { \mathbf { r } } ) - ( \mathbf { V } - \mathbf { V } _ { 0 } ) \frac { \partial ^ { \beta } } { 2 \rho \partial \mathbf { n } } ( \frac { 1 } { \mathbf { r } } ) \} \mathrm { d } \Sigma - \frac { \mathbf { R } ^ { 2 } } { \rho ^ { 2 } } ( \frac { \partial \mathbf { V } } { \partial \mathbf { n } } ) _ { 0 }
$$

因为

$$
\frac { \partial } { \partial \boldsymbol { 0 } } ( \frac { 1 } { \mathbf { r } } ) \mid _ { \mathbf { z } } = - \frac { 1 } { 2 \mathbf { r } _ { 0 } \mathbf { R } }
$$

而

$$
\frac { \partial ^ { \aa } } { \partial \mathsf { p } \partial \mathrm { n } } ( \frac { 1 } { \tt \frac { r } } ) { \partial - } - \frac { 1 } { \tt r } \mathrm { \frac { 3 } { \tt b } } - \frac { 1 } { 4 \tt r _ { 0 } \mathrm { R } ^ { 2 } } \mathrm { = } - \tt c \frac { 1 } { \tt r ^ { 3 } } + \frac { 1 } { 2 \tt R } \frac { \partial } { \partial \mathrm { n } } ( \frac { 1 } { \tt \frac { r } } ) \left| \tt { z } \right\}
$$

因此可得

$$
\frac { \mathcal { N } } { \mathfrak { p } } = \frac { 1 } { 4 \pi } { \int _ { \Omega } } \frac { \mathbf { V } - \mathbf { \bar { V } } _ { 0 } } { \mathbf { r } _ { 0 } ^ { 3 } } \mathrm { d } \Sigma - \frac { 1 } { 8 \pi \mathrm { R } } { \int _ { \Omega } } \{ \frac { 1 } { \mathbf { r } _ { 0 } } [ \frac { \partial \mathbf { V } } { \partial \mathrm { \bar { n } } } - ( \frac { \partial \mathbf { V } } { \partial \mathrm { \bar { n } } } ) _ { 0 } ] \overset { * } { - } ( \nabla - \mathbf { V } _ { 0 } ) \frac { \partial } { \partial \mathrm { \bar { n } } } ( \frac { 1 } { \mathbf { r } } ) \} \mathrm { d } \Sigma - \frac { \mathbf { R } ^ { 2 } } { \rho ^ { 2 } }
$$

若用 $( 5 \cdot 5 7 )$ 式推求 $\mathbf { P } _ { 0 }$ 点的调和函数值 $\mathtt { v _ { \mathfrak { o } } }$ ，则有

$$
\mathrm  V _ { \mathrm { 0 } } = \frac { 1 } { 4 \pi } \int \{ \frac { 1 } { r _ { \mathrm { 0 } } } \subset \frac { \partial V } { \partial \hbar } - ( \frac { \partial V } { \partial \hbar } ) _ { \mathrm { 0 } } \} - ( \nabla - V _ { \mathrm { 0 } } ) \frac { \partial } { \partial \hbar } ( \frac { 1 } { r } ) \} d \Sigma + \mathrm { R } ( \frac { \partial V } { \partial \hbar } ) _ { \mathrm { 0 } }
$$

将该式右端的积分项与 $( 5 \cdot 5 8 )$ 式右端第二项相对照，看到它们基本上相同。因此，用它可将$( 5 \cdot 5 8 )$ 式改写为：

$$
\frac { \partial \bar { \bf V } } { \partial \bar { \bf p } } = \frac { . 1 } { 4 \pi } \int \frac { \nabla - { \bf V } _ { 0 } } { { \bf r } _ { 0 } ^ { 3 } } \mathrm { d } \Sigma - \lbrack \frac { { \bf V } _ { 0 } } { 2 \bar { \bf R } } - \frac { 1 } { 2 } ( \frac { \partial \bar { \bf V } } { \partial \bar { \bf n } } ) _ { 0 } ] - \frac { { \bf R } ^ { 2 } } { \rho ^ { 2 } } ( \frac { \partial \bar { \bf V } } { \partial \bar { \bf n } } ) _ { 0 } \mathrm { ~ . ~ }
$$

用 $( 5 \cdot 5 9 )$ 式求球面上 $\mathbf { p _ { 0 } }$ 点的径向导数值，则有

$$
( \frac { \partial \mathbf { \bar { N } } } { \partial \mathbf { p } } ) _ { \circ } = \frac { 1 } { 4 \pi } \int \frac { \mathrm { ~ \mathbf { V } ~ - \mathbf { \bar { V } } _ { \circ } ~ } } { \mathrm { ~ \mathbf { r } _ { 0 } ~ } ^ { 3 } } \mathrm { d } \Sigma - \frac { \mathbf { \bar { V } } _ { \circ } } { 2 \mathrm { \mathbf { \bar { R } } } } - \frac { 1 } { 2 } ( \frac { \partial \mathbf { \bar { V } } } { \partial \mathrm { n } } ) _ { \circ }
$$

因为 $\pmb { \mathrm { n } }$ 为球面(∑)的内法线，与向径 $p$ 方向相反，故有

$$
( \frac { \partial \mathbf { V } } { \partial \mathbf { p } } ) _ { \circ } = - ( \frac { \partial \mathbf { V } } { \partial \mathbf { n } } ) _ { \circ }
$$

最后得到

$$
( \frac { \partial \mathbf { V } } { \partial \mathbf { \rho } } ) _ { \circ } = \frac { 1 } { 2 \pi } \int _ { ( \Sigma ) } \frac { \mathbf { V } - \mathbf { V } _ { \circ } } { { \tau _ { 0 } } ^ { 3 } } \mathrm { d } \Sigma - \frac { \mathbf { V } _ { \circ } } { \mathrm { R } }
$$

$( 5 \cdot 6 0 )$ 式可用于由球面上的调和函数值推求球面上的调和函数一阶径向导数值。

由 $( 5 ^ { \cdot } { \mathfrak { s } } 9 )$ 式可得

$$
\frac { \partial \mathbb { V } } { \partial \boldsymbol { \mathfrak { p } } } = \frac { 1 } { 4 \pi } \int \frac { \mathrm { \bf ~ V } - \mathrm { \bf ~ V } _ { 0 } } { \mathrm { \bf ~ r } _ { 0 } ^ { ~ 3 } } \mathrm { d } \boldsymbol { \Sigma } - \frac { \mathrm { \bf ~ V } _ { 0 } } { 2 \mathrm { \bf R } } - \frac { 1 } { 2 } ( \frac { \partial \mathbb { V } } { \partial \boldsymbol { \Phi } } ) _ { 0 } + \frac { \mathrm { \bf ~ R } ^ { 2 } } { \rho ^ { 2 } } ( \frac { \partial \mathbb { V } } { \partial \boldsymbol { \mathrm { p } } } ) _ { 0 }
$$

考虑到 $( 5 \cdot 6 0 )$ 式，则得

$$
\frac { \partial \mathbf { V } } { \partial \boldsymbol { \rho } } { = } \frac { \mathbf { R } ^ { 2 } } { \boldsymbol { \rho } ^ { 2 } } ( \frac { \partial \mathbf { V } } { \partial \boldsymbol { \rho } } ) _ { \circ }
$$

从 $( 5 \cdot 6 1 )$ 式看到，只要按 $( 5 \cdot 6 0 )$ 式求得了球面上的调和函数一阶径向导数值，球外点的一阶径向导数值就很容易求了。

现用球谐函数来讨论。球外调和函数的一般表达式是 $( 5 \cdot 4 3 )$ 式，亦可写为

$$
\mathbb { V } ( \rho , \theta , \lambda ) = \sum _ { \mathfrak { n } = 0 } ^ { \infty } ( \frac { \mathbf { R } } { \rho } ) ^ { \mathfrak { n } + 1 } \mathbb { Y } _ { \mathfrak { n } } ( \theta , \lambda )
$$

式中

$$
\Upsilon _ { \mathrm { { s } } } ( \theta , \lambda ) = \sum _ { \mathrm { { m = 0 } } } ^ { \mathrm { { s } } } ( \mathbb { C } _ { \mathrm { { n m } } } \mathrm { { c o s } } \operatorname* { m a x } + \mathbb { S } _ { \mathrm { { s m } } } { \mathrm { { s i n m } } \lambda } ) \mathrm { { P } } _ { \mathrm { { i m } } } ( \mathrm { { c o s } } \theta )
$$

由 $( 5 \cdot 6 2 )$ 式可得一阶径向导数为

$$
\frac { \partial \mathbf { V } } { \partial \boldsymbol { p } } = - \underset { \mathbf { n } = 0 } { \overset { \infty } { \sum } } ( \mathbf { n } + 1 ) \underset { \boldsymbol { \rho } ^ { \mathbf { n } + 2 } } { \frac { \mathrm { R } ^ { \mathbf { n } + 1 } } { \boldsymbol { \rho } ^ { \mathbf { n } + 2 } } } \mathbf { Y } _ { \mathbf { n } } ( \boldsymbol { \theta } , \lambda )
$$

因此，调和函数的一阶径向导数在球面上的值为

$$
( \frac { \partial \mathbb { V } } { \partial \boldsymbol { \mathsf { p } } } ) _ { 0 } = - \mathrm { \small ~ \frac { 1 } { R } \sum _ { n = 0 } ^ { \Sigma } ( n + 1 ) \mathbb { Y } _ { a } } ( \boldsymbol { \theta } , \lambda )
$$

由 $( 5 \cdot 6 4 )$ 和 $( 5 \cdot 6 5 )$ 式很容易导出 $( 5 \cdot 6 1 )$ 式。 $( 5 \cdot 6 5 )$ 式与 $( 5 \cdot 6 0 )$ 式相当，只不过是用球谐函数级数式表达而已。

由 $( 5 \cdot 6 2 )$ 式可得，调和函数 $\mathbf { v }$ 在球面上可表为

$$
{ \bf V } _ { 0 } = \sum _ { n = 0 } ^ { \infty } { \bf Y } _ { n } ( \theta , \lambda )
$$

用它可将 $( 5 \cdot 6 5 )$ 式写为

$$
\begin{array} { r } { ( \frac { \partial \mathbb { V } } { \partial \mathfrak { p } } ) _ { \mathfrak { o } } = - \frac { 1 } { \mathrm { R } } \overset { \infty } { \underset { \mathfrak { n } = 0 } { \Sigma } } \mathfrak { n } \Upsilon _ { \mathfrak { n } } ( \theta , \lambda ) - \frac { \mathbb { V } _ { \mathfrak { o } } } { \mathrm { R } } } \end{array}
$$

将此式与 $( 5 \cdot 6 0 )$ 式对照，可以得到

$$
\frac { 1 } { 2 \pi } \int _ { ( \Sigma ) } \frac { \mathrm { ~ V ~ } - \mathrm { ~ V } _ { \theta } } { \mathrm { ~ r } _ { \theta } ^ { 3 } } \mathrm { d } \Sigma = - \mathrm { ~ \frac { 1 } { R } \sum _ { n = 0 } ^ \infty ~ n Y _ { n } } ( \theta , \lambda )
$$

.再讨论调和函数的二阶径向导数。

在 $\ S \ 5 . 3$ 中讲到调和函数的一个性质：若 $\mathbf { v }$ 是调和函数，则 $\rho \ : \frac { \partial \mathbb { V } } { \partial \rho }$ 也是调和函数。将$( 5 \cdot 6 0 )$ 式应用于它，可得

$$
\begin{array} { r } { \lbrack \frac { \partial } { \partial \boldsymbol { \wp } } ( \boldsymbol { \wp } \frac { \partial \mathbb { V } } { \partial \boldsymbol { \wp } } ) \rbrack _ { 0 } = \frac { 1 } { 2 \pi } \displaystyle \int _ { \mathbb { ( } \mathbb { 2 } ) } ^ { \mathbb { R } \frac { \partial \mathbb { V } } { \partial \boldsymbol { \wp } } - \mathbb { R } ( \frac { \partial \mathbb { V } } { \partial \boldsymbol { \wp } } ) _ { \circ } } \mathrm { d } \Sigma - ( \frac { \partial \mathbb { V } } { \partial \boldsymbol { \wp } } ) _ { \circ } } \end{array}
$$

因为

$$
C \frac { \partial } { \partial \boldsymbol { \rho } } ( \boldsymbol { \rho } \frac { \partial \mathsf { V } } { \partial \boldsymbol { \rho } } ) \boldsymbol { \mathrm { \lambda } } _ { 0 } = ( \frac { \partial \mathsf { V } } { \partial \boldsymbol { \rho } } ) _ { \boldsymbol { \circ } } + \mathrm { R } ( \frac { \partial \mathsf { V } } { \partial \boldsymbol { \rho } ^ { 2 } } ) _ { \boldsymbol { \circ } }
$$

因而得到

$$
( \frac { \partial ^ { \mathbf { V } } } { \partial \boldsymbol { \mathfrak { p } } ^ { 2 } } ) _ { , 0 } = \frac { 1 } { 2 \pi } \int \frac { \frac { \partial \mathbb { V } } { \partial \boldsymbol { \mathfrak { p } } } - ( \frac { \partial \mathbb { V } } { \partial \boldsymbol { \mathfrak { p } } } ) _ { 0 } } { \boldsymbol { \mathfrak { r } } _ { 0 } ^ { 3 } } \mathrm { d } \Sigma - \frac { 2 } { \mathbf { R } } ( \frac { \partial \mathbb { V } } { \partial \boldsymbol { \mathfrak { p } } } ) _ { 0 }
$$

$( 5 \cdot 6 7 )$ 式就是推求球面上调和函数二阶径向导数值的公式，其已知数据是球面上调和函数的一阶径向导数值。

# \$5.5边值问题

在只考虑点 $\mathbf { P }$ 在 $\pmb { \tau }$ 内的情况，由(5·52)式有

$$
\mathbf { V _ { p } } = \frac { 1 } { 4 \pi } \int _ { ( \sigma ) } \subset \frac { 1 } { \mathbf { r } } \ \frac { \partial \mathbf { V } } { \partial \mathbf { n } } , - \nabla \ \frac { \partial } { \partial \mathbf { n } } ( \frac { 1 } { \mathbf { r } } ) \ ] d \sigma
$$

因为区域τ可以是界面(α)内的区域，也可以是(σ)面以外的无限空间，而n方向总是(o)面的关于τ区域的外法线方向。现改为以界面(α)为准,当P点在(o)面以外时,n由(α)面向内指；当P点位于(o)面内时,n由(σ)面向外指。(5·68)式说明：若已知调和函数V及其外法线导数$\frac { \partial \mathbb { V } } { \partial \mathbf { n } }$ 在界面上的值，即已知

$$
\nabla \ ! _ { o } = \Phi _ { 1 } ( \mathbf { x } , \mathbf { y } , z )
$$

$$
\frac { \partial \mathbf { V } } { \partial \mathbf { n } } | _ { \sigma } { = } \Phi _ { z } ( \mathbf { x } , \mathbf { y } , z )
$$

则(o)面内或面外任一点P的调和函数就可求得。(5·69)和(5·70)式是在界面上应满足的条件，故称为边值条件。根据边值条件推求界面外的调和函数称为外部边值问题，求界面内的调和函数称为内部边值问题。

实际上，只需一个边值条件就可求出调和函数，另一个边值条件用别的来代替。

在格林第二恒等式(5·9)中,取U和V都是区域τ内的调和函数。因为△U=△V=0,故有

$$
0 = \int _ {  { \left( a \right) } } ( \mathbf { U } \frac { \partial \mathbf { V } } { \partial \mathbf { \hat { n } } } - \nabla \frac { \partial \mathbf { V } } { \partial \mathbf { \hat { n } } } ) \mathrm { d }  { \boldsymbol { \sigma } }
$$

将该式除以 $4 \pi$ ，以 $( 5 \cdot 6 8 )$ 式减之，则得

$$
\mathbf { V _ { P } } = - \ \frac { 1 } { 4 \pi } \int _ { ( 0 ) } ^ { } [ ( \mathbf { U } - \frac { 1 } { \mathbf { r } } ) \ \frac { \partial \mathbf { V } } { \partial \mathbf { n } } - \nabla \frac { \partial } { \partial \mathbf { n } } ( \mathbf { U } - \frac { 1 } { \mathbf { r } } ) ] \mathrm { d } \mathbf { e }
$$

从 $( 5 \cdot 7 1 )$ 式看出，如果能找到一个调和函数U，它在 $\mathbf { \Pi } ( \pmb { \sigma } )$ 面上总是等于 $\cdot \frac { 1 } { \mathbf { r } }$ ，即

$$
( \mathbf { U } - \frac { 1 } { \mathbf { r } } ) _ { \circ } = 0
$$

则有

$$
\mathrm { V } _ { \mathrm { P } } = \frac { 1 } { 4 \pi } \underset { ( \circ ) } { \int } \mathrm { V } \frac { \partial } { \partial \mathrm { n } } ( \mathbf { U } - \frac { 1 } { \mathrm { \tau } } ) \mathrm { d } \sigma
$$

(5·73)式表明，此时只要有边值条件(5·69)式，就可求得P点的调和函数Vp。这种根据调和函数在界面上的值推求界面内或外的调和函数的问题称为第一边值问题，亦称狄义赫利(Dirichlet)问题。关键是要找到区域内的另一个满足(5·72)式的调和函数U。

如果找到的调和函数U,它的法线导数在界面 $( { \pmb \sigma } )$ 上总是与 (）。相等，即

$$
\frac { \partial } { \partial \mathbf { n } } ( \mathbf { U } - \frac { 1 } { \mathbf { r } } ) \mid _ { \mathbf { \theta } _ { 0 } = 0 }
$$

代入 $( 5 \cdot 7 1 )$ 式，则得

$$
\mathbf { \boldsymbol { \nabla } } _ { \mathbf { \boldsymbol { P } } } = - \mathbf { \nabla } \frac { 1 } { 4 \pi } \int _ { \mathbf { \boldsymbol { ( \sigma ) } } } ( \mathbf { \boldsymbol { U } } - \frac { 1 } { \mathbf { \nabla } \mathbf { \vec { r } } } ) \ \frac { \partial \nabla } { \partial \mathbf { \hat { n } } } \mathrm { d } \sigma \ .
$$

这样一来，只要有边值条件(5·70)式，就可求得P点的调和函数Vp。这种根据调和函数在界面上的法线导数值推求界面内或外的调和函数的问题称为第二边值问题,亦称诺依曼(Neu-mann)问题。关键要找到满足(5·74)式的另一个调和函数U。

还有第三边值问题,它要求找到的另一个调和函数 $\mathtt { U }$ 满足下列方程：

$$
[ \alpha ( \mathbf { U } - \frac { 1 } { \mathbf { r } } ) + \beta \frac { \partial } { \partial \mathbf { n } } ( \mathbf { U } - \frac { 1 } { \mathbf { r } } ) ] _ { \circ } = 0
$$

其中 $\pmb { \alpha }$ 和 $\beta$ 为任意的常数。将 $( 5 \cdot 7 6 )$ 式代入 $( 5 \cdot 7 1 )$ 式，则得

$$
\mathrm { \bf V _ { P } } = - \mathrm { \bf \Gamma } \frac { 1 } { 4 \pi \beta } \int _ { \mathrm { \bf \Gamma } ( \circ ) } ^ { } ( \mathrm { \bf U } - \mathrm { \bf \frac { 1 } { \hbar } } ) ( \alpha \mathrm { \bf V } + \beta \mathrm { \bf \frac { \partial \mathrm { \bf V } } { \partial \hbar } } ) \mathrm { d } \sigma
$$

如果有了边值条件

$$
( \alpha \mathbf { V } + \beta { \frac { \partial \mathbf { V } } { \partial \mathbf { n } } } ) _ { \circ } = \Phi ( \mathbf { x } , \mathbf { y } , z )
$$

则由 $( 5 \cdot 7 7 )$ 式可求得 $\mathbf { P }$ 点的调和函数 ${ \tt V } _ { \tt P }$ 。因为边值条件是调和函数及其法线导数的线性组合，故亦称混合边值问题。

由此可见，界面内或外的调和函数都可以通过解边值问题求得。但无论解那一类边值问题,都需要找到区域内另一个满足一定条件的调和函数 $\mathbf { U }$ 。通常将 $\mathrm { U } - \frac { 1 } { \tt r } = \tt G$ 称为格林函数。这个函数与界面的形状密切相关，目前只对个别规则的界面找到了相应的格林函数。这也就是说，绝大部分边值问题还不能严格求解。

# 5.6格林公式的应用

在 $\ S 5 . 3$ 中，已将格林公式应用于调和函数，得出了调和函数的一些性质。在这一节中，将把格林公式应用于物体对内部点的引力位和重力位。因为它们都不是调和函数，所得的结论与$\ S \ 5 . 3$ 中的不一致。虽然有些式子看起来似乎很类同，但其实质却不同，望读者注意。

# 一、将格林第二恒等式应用于质体对内部点的引力位

在格林第二恒等式 $( 5 \cdot 9 )$ 中，取 $( \tau )$ 为质体所占的空间， $( \pmb { \sigma } )$ 面是质体的表面，其中的两个函数分别为 $\mathrm { U } = 1$ 和质体对内部点的引力位 $\mathbf { v }$ 。因为 $\Delta \mathbf { U } = 0$ 和 $\frac { \partial \mathbf { U } } { \partial \mathbf { n } } { = } 0$ ，而 $\Delta \mathrm { V } = - 4 \pi \mathrm { f } \mathrm { D } ( \mathrm { D }$ 是质体的质量密度)，将这些代人 $( 5 \cdot 9 )$ 式，得到

$$
- \mathbf { \Gamma } _ { 4 \pi \mathbf { f } } \underbrace { \mathbf { \hat { I } } } _ { ( \tau ) } \mathbf { D } \mathbf { d } \tau = \int _ { ( \sigma ) } \mathbf { \frac { \partial V } { \partial \mathbf { n } } } \mathbf { d } \sigma
$$

显然， $\int \limits _ { ( \tau ) } ^ { } \dot { \mathbf { D } } \mathbf { d } \tau$ 就是质体的质量 $\mathbf { M }$ ,因此有·

$$
\mathbf { M } = - \mathbf { \Gamma } \frac { 1 } { 4 \pi \mathrm { f } } \int \displaylimits _ { ( \sigma ) } ^ { \partial \mathbf { V } } \mathbf { d } \sigma
$$

$( 5 \cdot 7 9 )$ 式表明，只要知道质体的表面 $( \pmb { \sigma } )$ 及引力位在这个面上的法线导数值(也就是引力在外法线方向上的分量)就可求出物体的总质量，而不需知道质体内部的质量分布情况。

# 二、将格林第二恒等式应用于重力位

有一质体，它绕质体内一个固定轴以角速度 $\pmb { \omega }$ 均速旋转,产生重力位W。在格林第二恒等式 $( 5 \cdot 9 )$ 中，取 $\left( \pmb { \tau } \right)$ 为质体所占的空间， $( \pmb { \sigma } )$ 面是将质体包含在内的曲面，其中的两个函数 ${ \bf U } =$

常数和 $\mathbf { v } = \mathbf { w }$ 。因为 $\Delta \mathbf { U } = 0$ 和 $\scriptstyle { \frac { \partial \mathbf { U } } { \partial \mathbf { n } } } = 0$ ，得到

$$
\int _ { \bar { ( } \tau ) } \Delta \mathbf { W } \mathrm { d } \tau = \int _ { \bar { ( } \tau ) } \frac { \partial \mathbb { W } } { \partial \mathbf { n } } \mathrm { d } \sigma
$$

如果 $\mathbf { \Pi } ( \pmb { \sigma } )$ 面上的重力位值处处相等，也就是 $\mathbf { \sigma } ( \pmb { \sigma } )$ 面是一个水准面，则其法线导线就是重力，即

$$
- \frac { \partial \mathbf { W } } { \partial \mathbf { n } } { = } \mathbf { g }
$$

代入 $( 5 \cdot 8 0 )$ 式，则得

$$
\int \limits _ { ( \epsilon ) } \Delta \Psi d \tau = - \int \limits _ { 0 } \mathbf { g } \mathrm { d } \sigma
$$

依据 $( 4 \cdot 8 8 )$ 式,对内部点的拉普拉斯算子等于一 $\cdot 4 \pi \mathrm { f D } + 2 \omega ^ { 2 }$ 。因而由 $( 5 \cdot 8 1 )$ 式可得：

$$
\int \limits _ { ( 0 ) } ^ { \infty } g d \sigma = 4 \pi f M - 2 \omega ^ { 2 } \frac { \cdot } { \tau }
$$

式中 $\mathbf { M }$ 和 $\pmb { \tau }$ 分别为质体的质量和体积。 $( 5 \cdot 8 2 )$ 式表明，匀速旋转的质体的外水准面上的重力值的总和只与质体的总质量、旋转角速度和该水准面所包的体积有关，而与其内部质量的分布无关。

# 三、将格林第三公式应用于重力位

在格林第三公式 $( 5 \cdot 2 0 )$ 中,取 $\mathbf { V }$ 为质体的重力位W,则得

$$
\int \limits _ { ( \tau ) } \frac { \Delta \mathbf { W } } { \mathbf { r } } \mathrm { d } \tau - \int \mathopen { } \mathclose \bgroup \left. \frac { 1 } { \tau } \cdot \frac { \partial \mathbf { W } } { \partial \mathbf { n } } - \mathbf { W } \frac { \partial } { \partial \mathbf { n } } ( \frac { 1 } { \mathbf { r } } ) \aftergroup \egroup \right. \mathrm { d } \sigma = \mathopen { } \mathclose \bgroup \left. \begin{array} { c } { - 2 \pi \mathbf { W } _ { \mathrm { P } } } \\ { 0 } \end{array} \aftergroup \egroup \right.
$$

利用 $( 4 \cdot 8 8 )$ 式，可将 $( 5 \cdot 8 3 )$ 式左端第一项可改写为

$$
\int _ { ( \tau ) } \frac { \Delta \mathbb { W } } { \tau } \mathrm { d } \tau = - \mathrm { \sf 4 } \pi \mathrm { f } \int _ { ( \tau ) } \cdot \frac { \mathrm { D } } { \tau } \mathrm { d } \tau + 2 \omega ^ { 2 } \int _ { ( \tau ) } \frac { \mathrm { d } \tau } { \tau }
$$

该式右端第一项包含了质体对 $\mathbf { P }$ 点的引力位，它可以表示为重力位减离心力位，即

$$
\mathbf { f } \int _ { ( \tau ) } \frac { \mathrm { D } } { \mathbf { r } } \mathrm { d } \tau = \mathrm { W } _ { \mathrm { P } } - \frac { \omega ^ { 2 } } { 2 } ( { \mathbf { x } } ^ { 2 } + { \mathbf { y } } ^ { 2 } ) .
$$

其中 $( \mathbf { x } , \mathbf { y } )$ 为 $\mathrm { \bf P }$ 点的两个坐标值，而坐标系的乙轴重合于质体的旋转轴。因而得到

$$
\int \limits _ { ( \tau ) } \frac { \Delta \mathbf { W } } { \tau } \mathrm { d } \tau = - \mathbf { \nabla } 4 \pi \mathbf { W } _ { \mathrm { P } } + 2 \pi \omega ^ { 2 } ( \mathbf { x } ^ { 2 } + \mathbf { y } ^ { 2 } ) + 2 \omega ^ { 2 } \intop _ { ( \tau ) } \frac { \mathrm { d } \tau } { \tau }
$$

将它代入 $( 5 \cdot 8 3 )$ 式，则得

$$
2 \pi \omega ^ { 2 } ( \mathbf { x } ^ { 2 } + \mathbf { y } ^ { 2 } ) + 2 \omega ^ { 2 } \int _ { \left( \tau \right) } ^ { } \frac { \mathrm { d } \tau } { \tau } - \int _ { \left( \epsilon \right) } ^ { } [ \frac { 1 } { \tau } \frac { \partial \mathbb { W } } { \partial \hbar } - \mathbb { W } \frac { \partial } { \partial \mathbf { n } } ( \frac { 1 } { \mathbf { r } } ) ] \mathrm { d } \sigma = \left\{ \begin{array} { l l } { 2 \pi \mathbb { W } _ { \mathbf { p } } \left( \frac { \mathrm { d } \tau } { \tau } \right) = 0 } & { \mathrm { ~ f ~ o ~ r ~ } \tau \leq 0 } \\ { 4 \pi \mathbb { W } _ { \mathbf { p } } } & { } \end{array} \right. ,
$$

如果 $\pmb { \sigma }$ 面上的重力位处处相等，它的数值为 $\mathbf { W _ { 0 } }$ 。考虑到 g和（5·21）式，由（5·84）式可得

$$
2 \pi \omega ^ { 2 } ( \mathbf { x } ^ { 2 } + \mathbf { y } ^ { 2 } ) + 2 \omega ^ { 2 } \int _ { \mathbf { \overline { { \Gamma } } } } \frac { \mathrm { d } \tau } { \mathbf { r } } + \int \underset { ( \sigma ) } { \underbrace { \mathbf { g } } } \mathrm { d } \sigma = 4 \pi \mathbf { W } _ { \mathrm { p } }
$$

这个式子不仅适用于 $\mathrm { \bf P }$ 在 $\mathbf { \Pi } ( \pmb { \sigma } )$ 面外而且也适合于 $\mathbf { P }$ 在 $\mathbf { \Pi } ( \pmb { \sigma } )$ 面上(此时 ${ \bf W _ { P } } { = } { \bf W _ { \varphi } } _ { 0 } \mathrm { ~ . ~ }$ 。由该式可得

$$
\mathbf { W _ { P } } = \frac { \omega ^ { 2 } } { 2 } ( { \bf x } ^ { 2 } + { \bf y } ^ { 2 } ) + \frac { \omega ^ { 2 } } { 2 \pi } \mathrm {  ~ \downarrow ~ } \frac { \mathrm { d } \tau } { \mathrm {  ~ r ~ } } + \frac { 1 } { 4 \pi } \mathrm {  ~ \downarrow ~ } \frac { { \bf g } } { \mathrm {  ~ r ~ } } \mathrm { d } \sigma \cdot
$$

$( 5 \cdot 8 5 )$ 式表明，依据质体外水准面 $\left( \sigma \right)$ 的形状，质体绕轴旋转的角速度 $\omega$ 和水准面上的重力值就可求定 $( \pmb { \sigma } )$ 面上和面外任一点的重力位，而无需知道质体内部质量分布的情况。

# $8 5 . 7$ 质体引力位的等值层

前面已经讲过，质体对外部点的引力位是个调和函数。因此，可以利用 $( 5 \cdot 5 \dot { 2 } )$ 式推求质体对 $\mathbf { \Pi } ( \pmb { \sigma } )$ 面以外空间任一点 $\mathbf { P }$ 的引力位 $\mathbf { v _ { r } }$ ，即

$$
\begin{array} { r } { \mathrm { V } _ { \mathrm { p } } = - \frac { 1 } { 4 \pi } \underset { \left( \sigma \right) } { \int } [ \frac { 1 } { \mathbf { r } ^ { \prime } } \frac { \partial \mathrm { V } } { \partial \mathrm { n } } - \mathrm { V } \frac { \partial } { \partial \mathrm { n } } ( \frac { 1 } { \mathbf { r } ^ { \prime } } ) ] \mathrm { d } \sigma } \end{array}
$$

如图5.8所示， $( \sigma )$ 面是将质体包围在其中的任意封闭曲面。 $( 5 \cdot 8 6 )$ 式中的 $\pmb { n }$ 是指向 $\mathbf { \Pi } ( \pmb { \sigma } )$ 面外的法线方向，这与 $( 5 ^ { \cdot } 5 2 )$ 式中所规定的方向相反 $\mathbf { r } ^ { \prime }$ 是单元面积do至 $\bar { \bf P }$ 点的距离。

![](images/61b4bf8f8d1968da8050107bce2d1fc694127c213da1c6eb68520b50f2ae7ae7.jpg)  
图5.8

若 $\mathbf { \Pi } ( \pmb { \sigma } )$ 面是质体引力位的一个等位面，即在$\scriptstyle ( \sigma )$ 面上引力位值为一常数 $\mathrm { v } _ { \sigma }$ ，则 $( 5 \cdot 8 6 )$ 式中右边的第二项为

$$
\int _ { \mathfrak { o } } \nabla \frac { \partial } { \partial \mathfrak { n } } ( \frac { 1 } { \mathbf { r } ^ { \prime } } ) \mathrm { d } \sigma = \mathrm { V } _ { \circ } \int _ { \mathfrak { o } } \frac { \partial } { \partial \mathfrak { n } } ( \frac { 1 } { \mathbf { r } ^ { \prime } } ) \mathrm { d } \sigma
$$

而根据 $( 5 \cdot 2 1 )$ 式，当 $\mathbf { P }$ 点在 $( \pmb { \sigma } )$ 面外时，积分值为零。因而，由 $( 5 \cdot 8 6 )$ 式得到

$$
\mathbf { V } _ { \mathrm { p } } = - \frac { 1 } { 4 \pi } \int \limits _ { ( \sigma ) } ^ { } \frac { 1 } { \mathrm { r ^ { \prime } } } \frac { \partial \mathbf { V } } { \partial \mathbf { \eta } } \mathrm { d } \sigma = \mathbf { f } \int \displaylimits _ { ( \sigma ) } ^ { } \frac { - \frac { \partial \mathbf { V } } { \partial \mathbf { n } } } { \mathbf { r ^ { \prime } } } \mathrm { d } \sigma
$$

将该式与单层引力位的表达式 $( 4 \cdot 2 5 )$ 相对照，可

以看出，质体对外部点引力位Vp可以用等位面(o)上的一个单层所产生的引力位来代替，这个物质层的密度为

$$
\displaystyle \delta = \frac { - \frac { \partial \mathsf { V } } { \partial \mathsf { n } } | _ { \mathsf { \sigma } } } { \mathsf { \sigma } _ { \cdot } \mathsf { \sigma } _ { \cdot } \mathsf { \sigma } _ { \cdot } \mathsf { f } }
$$

这个物质层被称为质体位的等值层，亦称格林等值层。要按(5·87)式求得单层密度，就必须知道在 $\mathbf { \Pi } ( \pmb { \sigma } )$ 面上的引力 $( - \frac { \partial \mathrm { V } } { \partial \mathrm { n } } )$ 因为引力与等位面 $( \pmb { \sigma } )$ 垂直，方向与 $\pmb { \mathrm { n } }$ 的方向相反。

实际上，等值层并不一定要在等位面上，也可以在包围质体的任意封闭曲面上。最常用的是质体表面(∑)上的单层，见图5.8。这就是说，质体对外部点的引力位可以用在质体表面(∑)上的一个单层所产生的引力位来代替，即

$$
\begin{array} { r } { \mathbf { V } _ { \mathrm { P } } = \mathbf { f } \displaystyle \int _ { ( \Sigma ) } \frac { \delta } { \mathbf { r } } \mathbf { d } \Sigma } \end{array}
$$

式中r为单元面积d∑至P点的距离，而单层密度δ的计算式可由(5·86)式推得，即

$$
\hat { \mathbf { \delta } } = \frac { - \mathbf { \overset { . } { [ } \frac { \partial \mathbf { V } } { \partial \mathbf { \hat { n } } } - \mathbf { r } \mathbf { V } \frac { \partial } { \partial \mathbf { n } } ( \frac { 1 } { \mathbf { r } } ) \mathbf { \hat { \Sigma } } _ { \mathbf { \Sigma } } } } { 4 \pi \mathbf { f } }
$$

式中n为(∑)面的外法线。显然，要按(5·89)式推求单层密度是不现实的,因为(∑)面上的 $\frac { \partial \mathsf { V } } { \partial \mathbf { n } }$ 和V值要同时已知是困难的。以后将是应用这种等值层的原理，将质体位转换为单层位，以便于进一步的研究问题。

# $\ S 5 . 8$ 用球谐函数解球的外部边值问题

85.5讨论了调和函数的三类边值问题，其中提到，必需找到相应的格林函数才能求得它们的解。然而，如果界面(o)是球面的话，则可运用球谐函数来求解边值问题，而无需寻找格林函数。依据本书的需要，本节只讨论外部边值问题。

# 一、第一边值问题的解

所谓第一外部边值问题就是已知调和函数在界面上值，求界面外的调和函数。当界面为球面时，边值条件可以写为已知的面球谐函数的级数，即

$$
\begin{array} { r } { { \bf V } ( { \bf R } , \theta , \lambda ) = \sum _ { \bf n = 0 } ^ { \infty } { \bf Y } _ { \bf n } ( \theta , \lambda ) _ { \mathrm { . } } } \end{array}
$$

而依据 $( 5 \cdot 4 3 )$ 式,可以假定所要求的球外调和函数有如下的形式：

$$
\begin{array} { r } { \mathbf { V } ( \rho , \theta , \lambda ) = \underset { \mathfrak { n } = 0 } { \overset { \mathtt { c o } } { \sum } } \frac { \mathbf { R } ^ { \mathfrak { n } } } { \rho ^ { \mathfrak { n } + 1 } } \mathbf { X } _ { \mathfrak { n } } ( \theta , \lambda ) } \end{array}
$$

式中R为球的半径,X(0,λ)为面球谐函数,但其中的常系数待定。在(5·91)式中令ρ=R,就得球面上的调和函数V(R,0,λ),它应与(5·90)式相等,故有X(0,λ)=RY(0,λ)。将它代人$( 5 \cdot 9 1 )$ 式，则得

$$
\mathbb { V } ( \rho , \theta , \lambda ) = \sum _ { { \mathfrak { n } } = 0 } ^ { \infty } ( \frac { \mathbf { R } } { \rho } ) ^ { { \mathfrak { n } } + 1 } \mathbf { Y } _ { \mathfrak { n } } ( \theta , \lambda )
$$

由于 $\mathbf { Y } _ { \mathfrak { n } } ( \pmb \theta , \lambda )$ 是已知的，因此解可以求得。

根据球函数展开理论4有

$$
{ \bf Y _ { n } } ( \theta , \lambda ) = \frac { 2 { \bar { \bf n } } + 1 } { 4 \pi { \mathrm R } ^ { 2 } } \int _ { { \bf \sigma } ^ { \left( \theta \right) } } { \bf V } ( { \bf R } , \theta ^ { \prime } , \lambda ^ { \prime } ) { \bf P _ { n } } ( \cos \psi ) \mathrm d \sigma
$$

式中 $( \theta ^ { \prime } , \lambda ^ { \prime } )$ 表示球面元素 ${ \bf d } \pmb { \sigma }$ 的球面坐标， $\phi$ 为 ${ \bf d } \pmb { \sigma }$ 与求值点 $( \pmb { \rho } , \pmb { \theta } , \lambda )$ 的球心角距。将 $( 5 \cdot 9 3 )$ 式代入 $( 5 ^ { \cdot } 9 2 )$ 式，并调换求和与积分的顺序，得到

$$
\mathrm { ~ V ~ } ( \rho , \theta , \lambda ) = \frac { 1 } { 4 \pi \mathsf { R } } \int _ { \mathsf { \Omega } ( o ) } \mathrm { V } ( \mathrm { R } , \theta ^ { \prime } , \lambda ^ { \prime } ) \underset { \mathsf { \Omega } = \mathsf { 0 } } { \overset { \infty } { \sum } } ( 2 \mathsf { n } \overset { * } { \overbar { \mathrm { \Omega } } } + 1 ) \frac { \mathrm { R } ^ { \mathsf { n } } } { \mathsf { \Omega } ^ { \mathsf { n } + 1 } } \mathrm { P } _ { \mathfrak { n } } ( \cos \psi ) \mathrm { ] } \mathrm { d } o
$$

为了将 $( 5 ^ { . } \cdot \mathfrak { s } 4 )$ 式积分号中的无穷级数改化成封闭形式，以 $\mathbf { r }$ 表示 ${ \bf d } \pmb { \sigma }$ 至求值点的距离，则有

$$
\begin{array}{c} \mathbf { r } = \sqrt { \rho ^ { 2 } + \mathbf { R } ^ { 2 } - 2 \rho \mathbf { R } \mathbf { c o s } \psi }  \end{array} .
$$

由 $\frac { 1 } { \tt { r } }$ 的球谐函数表示式 $( 5 \cdot 4 5 )$ 可以求得

$$
\frac { \partial } { \partial \boldsymbol { \mathsf { p } } } ( \frac { 1 } { \boldsymbol { \mathsf { r } } } ) = - \sum _ { \boldsymbol { \mathsf { n } } = 0 } ^ { \infty } \frac { \boldsymbol { \mathsf { R } } ^ { \mathrm { n } } } { \boldsymbol { \mathsf { p } } ^ { \mathrm { n } + 2 } } \boldsymbol { \mathsf { P } } _ { \boldsymbol { \mathsf { n } } } ( \boldsymbol { \mathsf { c o s } } \boldsymbol { \psi } )
$$

进而可得

$$
- 2 p \frac { \partial } { \partial \boldsymbol { \wp } } ( \frac { 1 } { \mathbf { r } } ) - \frac { 1 } { \mathbf { r } } = \overset { \infty } { \underset { \mathbf { r } } { \sum } } ( 2 \mathbf { n } + 1 ) \frac { \mathbf { R } ^ { \mathrm { n } } } { \boldsymbol { \wp } ^ { \mathrm { n + 1 } } } \mathbf { P } _ { \mathbf { n } } ( \cos \psi )
$$

再由 $( 5 \cdot 9 5 )$ 式可以求得

$$
\frac { \partial } { \partial \boldsymbol { \mathsf { p } } } ( \frac { 1 } { \mathbf { r } } ) = - \frac { \boldsymbol { \mathsf { p } } - \mathsf { R c o s } \boldsymbol { \Psi } } { \mathbf { r } ^ { 3 } } \quad .
$$

因而有

$$
- 2 \rho \frac { \partial } { \partial \boldsymbol { \mathbf { p } } } ( \frac { 1 } { \mathbf { r } } ) - \frac { 1 } { \mathbf { r } } = \frac { \rho ^ { 2 } - \mathbf { R } ^ { 2 } } { \mathbf { r } ^ { 3 } }
$$

由 $( 5 \cdot 9 7 )$ 和 $( 5 \cdot 9 8 )$ 式可得

$$
\underset { { \mathfrak { n } } = { \mathfrak { n } } } { \overset { \infty } { \Sigma } } ( 2 { \mathfrak { n } } + 1 ) \frac { { \mathrm { R } } ^ { { \mathfrak { n } } } } { \rho ^ { { \mathfrak { n } } + 1 } } { \mathrm { P } } _ { \mathfrak { n } } ( { \cos } \psi ) = \frac { \rho ^ { 2 } - { \mathrm { R } } ^ { { \mathfrak { 2 } } } } { { \mathrm { r } } ^ { 3 } }
$$

将它代入 $( 5 \cdot 9 4 )$ 式，则得

$$
\mathrm { V } ( \rho , \theta , \lambda ) = \frac { \rho ^ { 2 } - \mathrm { R } ^ { 2 } } { 4 \pi \mathrm { r } } \int \displaylimits _ { \langle \sigma \rangle } ^ { } \frac { \mathrm { V } ( \mathrm { R } , \theta ^ { \prime } , \lambda ^ { \prime } ) } { \mathrm { r } ^ { 3 } } \mathrm { d } \sigma
$$

$( 5 \cdot 9 9 )$ 式称为布桑积分，用它可以由调和函数在球面上的值 $\mathbf { V } ( \vec { \mathbf { R } } , \theta ^ { \prime } , \lambda ^ { \prime } )$ 求得球外任意点(p,${ \theta } _ { { \em \lambda } }$ 的调和函数值 $\nabla ( \rho , \theta , \lambda )$ ,即球的第一外部边值问题的解

# 二、第二边值问题的解

所谓第二外部边值问题，就是已知界面上调和函数的法线导数值，求界面外的调和函数。当界面 $\mathbf { \Pi } ( \pmb { \sigma } )$ 为球面时,法线方向与球心向径方向一致,可认为已知径向导数 $( \frac { \partial \mathbf { V } } { \partial \mathbf { p } } ) _ { \pmb { \jmath } }$ 。这个已知的边值条件也可以用面球谐函数的级数式表示，即

$$
( \frac { \partial \mathbf { V } } { \partial \boldsymbol { \mathbf { \rho } } } ) _ { \boldsymbol { \circ } } = \sum _ { \mathfrak { n } = 0 } ^ { \infty } \mathbf { Y } _ { \mathfrak { n } } ( \boldsymbol { \theta } , \lambda )
$$

球的第二外部边值问题的解为

$$
\mathbb { V } ( \rho , \theta , \lambda ) = - \textrm { R } _ { \textrm { n } = 0 } ^ { \infty } \frac { 1 } { \textrm { n } + 1 } ( \frac { \textrm { R } } { \rho } ) ^ { \textrm { n } + 1 } \Upsilon _ { \textrm { n } } ( \theta , \lambda )
$$

只要将 $( 5 \cdot 1 0 1 )$ 式对 ${ \pmb \rho }$ 求导，再令其中的 $\scriptstyle { \pmb { \rho } } = { \pmb { R } }$ ，就得 $( 5 \cdot 1 0 0 )$ 式,因而解成立。

因为 $( 5 \cdot 1 0 1 )$ 中的 $\yen 123$ 要按下式求得：

$$
{ \bf Y } _ { \bf n } ( \theta , \lambda ) = \frac { 2 { \bf n } + 1 } { 4 \pi { \bf R } ^ { 2 } } \int _ { ( \sigma ) } ( \frac { \partial { \bf V } } { \partial \bf { p } } ) _ { \bf { \sigma } } { \bf P } _ { \bf { n } } ( \cos \psi ) \mathrm { d } \psi
$$

将它代入 $( 5 \cdot 1 0 1 )$ 式,并调换积分与求和的顺序，得到

$$
\mathsf { V } ( \rho , \theta , \lambda ) = - \frac { 1 } { 4 \pi } \int _ { ( \sigma ) } ( \frac { \partial \mathsf { V } } { \partial \mathsf { p } } ) _ { s } \subset \sum _ { \mathsf { a } = 0 } ^ { \infty } \frac { 2 \mathsf { n } + 1 } { \mathsf { n } + 1 } \frac { \mathsf { R } ^ { \mathsf { n } } } { \rho ^ { \mathsf { n } + 1 } } \mathsf { P } _ { \mathsf { n } } ( \mathsf { c o s } \psi ) \ d ) \mathsf { d } \sigma
$$

下面要将积分号中的无穷级数改化掉。因

$$
\frac { 2 n + 1 } { n + 1 } = 2 - \frac { 1 } { n + 1 }
$$

并顾及 $( 5 \cdot 4 5 )$ 式，则有

$$
\begin{array} { l } { \displaystyle { \sum _ { n = 0 } ^ { \infty } \frac { 2 \mathrm { n } + 1 } { \mathrm { n } + 1 } \frac { \mathrm { R } ^ { \mathrm { n } } } { \rho ^ { \mathrm { n } + 1 } } \mathbf { P } _ { \mathrm { n } } ( \cos \phi ) = \frac { 2 } { \mathrm { r } } - \sum _ { \mathrm { n } = 0 } ^ { \infty } \frac { 1 } { \mathrm { n } + 1 } \frac { \mathrm { R } ^ { \mathrm { n } } } { \rho ^ { \mathrm { n } + 1 } } \mathbf { P } _ { \mathrm { n } } ( \cos \phi ) } } \end{array}
$$

$$
\alpha { = } \frac { \mathbb { R } } { \rho }
$$

则得

$$
\underset { { \mathfrak { n } } = { \mathfrak { o } } } { \overset { \infty } { \sum } } \frac { 1 } { { \mathfrak { n } } + 1 } \frac { { \mathrm { R } } ^ { \bullet } } { \rho ^ { { \mathfrak { n } } + 1 } } { \mathrm { P } } _ { \mathfrak { n } } ( \cos \psi ) = \frac { 1 } { \mathrm { R } } \underset { { \mathrm { n } } = { \mathfrak { o } } } { \overset { \infty } { \sum } } \frac { \alpha ^ { \mathfrak { n } + 1 } } { \mathfrak { n } + 1 } { \mathrm { P } } _ { \mathfrak { n } } ( \cos \psi )
$$

因为

$$
\frac { \alpha ^ { n + 1 } } { n + 1 } = \int \limits _ { 0 } ^ { \alpha } a ^ { n } \mathrm { d } a
$$

故有

$$
\underset { { \mathfrak { n } } = { \mathfrak { n } } } { \overset { \infty } { \sum } } \frac { 1 } { { \mathfrak { n } } + 1 } \frac { { \mathfrak { R } } ^ { \mathfrak { n } } } { \rho ^ { { \mathfrak { n } } + 1 } } { \mathrm { P } } _ { \mathfrak { n } } ( \mathsf { c o s } \psi ) = \frac { 1 } { \mathsf { R } } \int _ { \mathfrak { n } = 0 } ^ { \mathsf { a } } \alpha ^ { \mathsf { n } } { \mathrm { P } } _ { \mathfrak { n } } ( \mathsf { c o s } \psi ) \mathrm { d } \alpha
$$

考虑到 $( 5 \cdot 1 0 4 )$ 式 $\frac { 1 } { \mathfrak { r } }$ 可表为

$$
\frac { 1 } { \tau } = \frac { 1 } { \rho } \sum _ { n = 0 } ^ { \infty } \alpha ^ { n } \mathrm { P } _ { \mathrm { n } } ( \cos \psi )
$$

而

$$
\underset { \mathfrak { n } = 0 } { \overset { \infty } { \sum } } \alpha ^ { \mathfrak { n } } \mathrm { P } _ { \mathfrak { n } } ( \mathsf { c o s } \psi ) = \frac { \ell } { \mathfrak { r } } = \frac { 1 } { \sqrt { 1 + \alpha ^ { 2 } - 2 a \mathrm { c o s } \psi } }
$$

因而可得

$$
\int _ { \stackrel { \mathrm { R } } { 0 } } ^ { \infty } \alpha ^ { \mathrm { s } } \mathrm { P } _ { \mathrm { n } } ( \cos \psi ) \mathrm { d } \alpha = \int _ { \stackrel { \mathrm { 0 } } { 0 } } ^ { \infty } { \frac { \mathrm { d } \alpha } { \sqrt { 1 + \alpha ^ { 2 } - 2 \alpha \mathrm { c o s } \psi } } } = \ln { \frac { \mathrm { r } + \mathrm { R } - \mathrm { \rho } \mathrm { c o s } \psi } { \rho ( 1 - \mathrm { \cot } \psi ) } }
$$

将该式代人 $( 5 \cdot 1 0 5 )$ 式后，再代入 $( 5 \cdot 1 0 3 )$ 式，得到

$$
\sum _ { \mathfrak { n } = \mathfrak { n } } ^ { \infty } \frac { 2 \mathfrak { n } + 1 } { \mathfrak { n } + 1 } \frac { \mathbb { R } ^ { \mathfrak { n } } } { \rho ^ { \mathfrak { n } + 1 } } \mathrm { P } _ { \mathfrak { n } } ( \cos \phi ) = \frac { 2 } { \mathfrak { r } } - \frac { 1 } { \mathsf { R } } \mathrm { l } \mathsf { n } \frac { \mathfrak { r } + \mathsf { R } - \mathsf { \rho } \cos \phi } { \rho ( 1 - \cos \phi ) }
$$

再将它代入 $( 5 \cdot 1 0 2 )$ 式，则得

$$
\mathsf { V } ( \rho , \theta , \lambda ) = \frac { 1 } { 4 \pi } \int \underset { ( \sigma ) } { \langle \frac { \partial \mathbb { V } } { \partial \rho } \rangle } { \circ } \mathbb { C } \frac { 1 } { \mathsf { R } } \mathrm { l n } \frac { \mathsf { r } + \mathsf { R } - \mathsf { p c o s } \psi } { \rho ( 1 - \mathsf { c o s } \psi ) } - \frac { 2 } { \mathsf { r } } \mathrm { \mathsf { ] } d } \sigma
$$

这个式子称为贝尔聂克公式，用它可由调和函数在球面上的径向导数值 $( \frac { \partial { \bf V } } { \partial \boldsymbol { p } } ) _ { \sigma }$ 求得球外任意点的调和函数 $\mathbf { V } ( \pmb { \rho } , \pmb { \theta } , \pmb { \lambda } )$ ，即球的第二外部边值问题的解

在 $( 5 \cdot 1 0 7 )$ 式中，取 ${ \pmb \rho } { = } { \bf R }$ ，则得球面上的调和函数值

$$
\mathsf V ( \rho , \theta , \lambda ) = \frac { 1 } { 4 \pi \mathsf R } \int \displaylimits _ { ( \rho ) } ^ { \infty } ( \frac { \partial \pmb V } { \partial \rho } ) _ { \circ } \mathsf { d n } ( 1 + \frac { 1 } { \sin \frac { \psi } { 2 } } ) - \frac { 1 } { \sin \frac { \psi } { 2 } } ) \mathsf { d } \sigma
$$

# 三、第三边值问题的解

所谓第三外部边值问题，就是已知调和函数及其法线导数的线性组合在界面上的值，求界面外的调和函数。当界面为球面时，边值条件可写为

$$
( \alpha \mathbf { V } + \beta { \frac { \partial { \mathbf { V } } } { \partial { \boldsymbol { p } } } } ) _ { \circ } = \sum _ { n = 0 } ^ { \infty } \mathbf { Y } _ { \mathfrak { n } } ( { \boldsymbol { \theta } } , { \boldsymbol { \lambda } } )
$$

其中

$$
\Upsilon _ { \mathrm { n } } ( \theta , \lambda ) = \frac { 2 \mathrm { n } + 1 } { 4 \pi \mathrm { R } ^ { 2 } } \int _ { ( \sigma ) } ^ { } ( \alpha \mathrm { V } + \beta \frac { \partial \mathrm { V } } { \partial \boldsymbol { \mathrm { p } } } ) _ { \alpha } \mathrm { P } _ { \mathrm { n } } ( \mathrm { c o s } \psi ) \mathrm { d } \sigma
$$

式中α和β为常系数。设解为

$$
\begin{array} { r l } { \small } & { { } \mathbf { V } ( \boldsymbol { \rho } , \boldsymbol { \theta } , \widetilde { \lambda } ) = \sum _ { n = 0 } ^ { \infty } \frac { \mathbf { R } ^ { n } } { \boldsymbol { \rho } ^ { n + 1 } } \mathbf { X } _ { n } ( \boldsymbol { \theta } , \lambda ) } \end{array}
$$

将它代入 $( 5 \cdot 1 0 9 )$ 式的左端，得到

$$
\frac { \alpha } { \mathrm { R } } \underset { { \bf n } = 0 } { \overset { \infty } { \sum } } { \bf X } _ { \bf n } ( \theta , \lambda ) - \frac { \beta } { \mathrm { R } ^ { 2 } } \underset { { \bf n } = 0 } { \overset { \infty } { \sum } } ( { \bf n } + 1 ) { \bf X } _ { \bf n } ( \theta , \lambda ) = \underset { { \bf n } = 0 } { \overset { \infty } { \sum } } { \bf Y } _ { \bf n } ( \theta , \lambda )
$$

由此有

$$
X _ { n } ( \theta , \lambda ) = \frac { R ^ { 2 } Y _ { n } ( \theta , \lambda ) } { \alpha R - \beta ( n + 1 ) }
$$

将它代入 $( 5 \cdot 1 1 1 )$ 式右端，则得

$$
\operatorname { V } ( \rho , \theta , \lambda ) = \ R \sum _ { s = 0 } ^ { \infty } ( \frac { \mathbf R } { \rho } ) ^ { \mathsf { n + 1 } } \frac { \Upsilon _ { \mathrm { n } } ( \theta , \lambda ) } { \alpha \mathbf R - \beta ( \mathbf n + 1 ) }
$$

这就是球的第三部边值问题的解。

在研究地球外部重力场时会遇到此类边值问题，边值条件(5·109)中的系数为

$$
\alpha { = } \frac { 2 } { R } \qquad \beta { = } 1
$$

代入 $( 5 \cdot 1 1 2 )$ 式，得到

$$
\stackrel { . } { X } _ { \mathrm { s } } ( \theta , \lambda ) = \frac { R ^ { 2 } } { 1 - n } \ o Y _ { \mathrm { s } } \left( \theta , \lambda \right)
$$

当n=1时，右端分母为零。因此,不能由Y(θ,λ)求得X(0,).，故解应为

$$
\mathsf { V } ( \rho , \theta , \lambda ) = \frac { \mathrm { R } ^ { 2 } \mathrm { Y } _ { 0 } ( \theta , \lambda ) } { \rho } + \frac { \mathrm { R } \mathrm { X } _ { 1 } ( \theta _ { 1 } , \lambda ) } { \rho ^ { 2 } } + \mathrm { R } \underset { \mathfrak { n } = 2 } { \overset { \infty } { \Sigma } } ( \frac { \mathrm { R } } { \rho } ) ^ { \mathfrak { n } + 1 } \frac { \mathrm { Y } _ { \mathfrak { n } } ( \theta , \lambda ) } { 1 - \mathrm { ~ \mathfrak { n } ~ } }
$$

其中的X(0,λ)将根据问题的具体情况另行求定。以(5·110)式代入(5.·115)式右端的最后一项，得到

$$
( \rho , \theta , \lambda ) = \frac { \mathrm { R } ^ { 2 } \mathrm { Y } _ { 0 } ( \theta , \lambda ) } { \mathsf { p } } ) + \frac { \mathrm { R } \mathrm { X } _ { 1 } ( \theta _ { 1 } , \lambda ) } { \mathsf { p } ^ { 2 } } - \frac { 1 } { 4 \pi } \int ( \frac { \mathcal { W } } { \partial \mathsf { p } } + \frac { 2 } { \mathsf { R } } \mathrm { V } ) _ { \alpha } \underset { \mathrm { n } = 2 } { \overset { \smile \simeq } { \subset } } \frac { 2 \mathsf { n } + 1 } { \mathsf { n } - 1 } \frac { \mathrm { R } ^ { \mathrm { n } } } { \mathsf { p } ^ { \mathrm { n } + 1 } } \mathrm { P } _ { \mathrm { n } } ( \mathsf { c o s } , \mathsf { d } _ { \mathrm { n } + 1 } , \mathsf { d } _ { \mathrm { n } + 1 } , \mathsf { d } _ { \mathrm { n } + 1 } , \mathsf { d } _ { \mathrm { n } + 1 } ) \mathrm { d } _ { \mathrm { n } + 1 } .
$$

，这就是所研究的特定边值问题的解。

# 第六章 水准椭球的重力场

# \$6.1外部点的重力位

所谓水准椭球，就是表面为水准面(面上重力位值为常数)的旋转椭球。因此，它具有如下几个特性：①它绕自已的短轴匀速旋转；②它的质量中心与它的几何中心重合；③它的水准面(等位面)都是旋转椭球面，它的表面是其中的一个。由于地球近似于旋转椭球，故水准椭球的重力场可以作为地球重力场的近似，因而有研究它的必要。

水准椭球对外部点的重力位U,取决于水准椭球的四个基本参数：表示椭球大小和形状的长半径a和扁率α;椭球的总质量M以及绕短轴旋转的角速度w。下面就来导出关系式。

![](images/f638cc8c8d31ab17ca78a7906ad869b29a32d5c0bf9172311114da6d16d3c9ac.jpg)  
图6.1

将坐标原点放在椭球的中心O，坐标面XOY与椭球的赤道面重合，Z轴与椭球的短轴重合。为了讨论方便，引入正交椭球坐标系(u，0,λ)。如图6.1所示，u是通过椭球外任--点P的与水准椭球表面共焦的椭球面的短半轴；0是P点的归化纬度β的余角，即θ=90°一β;入为P点的经度，由X轴所在的子午面起算，向东为正。此椭球坐标与直角坐标之间的关系为

$$
\left. \begin{array} { l } { \mathbf { x } = \sqrt { \mathbf { u } ^ { 2 } + \mathbf { E } ^ { 2 } } \sin \theta \cos \lambda } \\ { \mathbf { y } = \sqrt { \mathbf { u } ^ { 2 } + \mathbf { E } ^ { 2 } } \sin \theta \sin \lambda } \\ { z = \mathbf { u } \cos \theta } \end{array} \right\}
$$

式中

$$
\mathsf { E } { = } \mathsf { \bar { a } } \sqrt { 2 \alpha { - } \alpha ^ { 2 } }
$$

它是椭球两个焦点间的距离的一半。坐标面u=常数是旋转椭球面·它的方程为

$$
\frac { \mathbf { x } ^ { 2 } + \mathbf { y } ^ { 2 } } { \mathbf { u } ^ { 2 } + \mathbf { E } ^ { 2 } } + \frac { \mathbf { z } ^ { 2 } } { \mathbf { u } ^ { 2 } } = 1
$$

当u=b=a(1--a)时，就是水准椭球的表面。坐标面0=常数是旋转双曲面，它的方程为

$$
\frac { { \bf x } ^ { 2 } + { \bf y } ^ { 2 } } { { \bf E } ^ { 2 } \sin ^ { 2 } \theta } - \frac { { \bf z } ^ { 2 } } { { \bf E } ^ { 2 } \cos ^ { 2 } \theta } = 1
$$

坐标面入=常数是平面，它的方程是

$$
\mathbf { y } = \mathbf { x } \mathbf { t } \mathbf { g } \lambda
$$

重力位等于引力位加离心力位，先讨论引力位。由于质体对外部点的引力位V是调和函

数，可以从解拉普拉斯方程求得。为此，要导出在正交椭球坐标系中的拉普拉斯方程。

由(6·1)式求出×、y、z对u、0、入的偏导数，再代入(5·26)式,经运算后可得三个尺度因子

$$
\scriptstyle \left. { \begin{array} { l } { \scriptstyle \mathbf { h } _ { 1 } = { \sqrt { \frac { \mathbf { u } ^ { 2 } + \mathbf { E } ^ { 2 } \cos ^ { 2 } \theta } { \mathbf { u } ^ { 2 } + \mathbf { E } ^ { 2 } } } } } \\ { \scriptstyle \mathbf { h } _ { 2 } = { \sqrt { \mathbf { u } ^ { 2 } + \mathbf { E } ^ { 2 } \cos ^ { 2 } \theta } } } \\ { \scriptstyle \mathbf { h } _ { 3 } = { \sqrt { \mathbf { u } ^ { 2 } + \mathbf { E } ^ { 2 } } } \sin \theta } \end{array} } \right\}
$$

将 $( 6 \cdot 3 )$ 式代入 $( 5 \cdot 2 5 )$ 式，完成运算后得到拉普拉斯算子的表示式：

$$
\begin{array} { r l } & { \Delta { \bf V } = \frac { 1 } { ( { \bf u } ^ { 2 } + { \bf E } ^ { 2 } \cos ^ { 2 } \theta ) \sin \theta } \zeta ( { \bf u } ^ { 2 } + { \bf E } ^ { 2 } ) \sin \theta \frac { \mathcal { J } { \bf V } } { \partial { \bf u } ^ { 2 } } + 2 { \bf u } \sin \theta \frac { \partial { \bf V } } { \partial { \bf u } } ) + \sin \theta \frac { \mathcal { J } { \bf V } } { \partial { \bf \theta } ^ { 2 } } } \\ & { \qquad + \cos \theta \frac { \partial { \bf V } } { \partial \theta } + \frac { { \bf u } ^ { 2 } + { \bf E } ^ { 2 } \cos ^ { 2 } \theta } { ( { \bf u } ^ { 2 } + { \bf E } ^ { 2 } ) \sin \theta } \frac { \mathcal { J } { \bf V } } { \partial { \bf \theta } ^ { 2 } } } \end{array}
$$

因而拉普拉斯方程可以写为

$$
( \mathbf { u } ^ { 2 } + \mathrm { E } ^ { 2 } ) { \frac { \partial { \big / } \mathbf { V } } { \partial \mathbf { u } ^ { 2 } } } + 2 \mathbf { u } { \frac { \partial { \big / } \mathbf { V } } { \partial \mathbf { u } } } + { \frac { \partial { \big / } \mathbf { V } } { \partial { \big / } ^ { 2 } } } + \mathrm { c t g } \theta { \frac { \partial { \big / } \mathbf { V } } { \partial \mathbf { \bar { \theta } } } } + { \frac { \mathbf { u } ^ { 2 } + \mathrm { E } ^ { 2 } \mathrm { c o s } ^ { 2 } \theta } { ( \mathbf { u } ^ { 2 } + \mathbf { E } ^ { 2 } ) \sin ^ { 2 } \theta } } { \frac { \partial { \big / } \mathbf { V } } { \partial { \big / } ^ { 2 } } } = 0
$$

如上一章那样，解拉普拉斯方程时采用分离变量法。由于水准椭球的引力位有绕短轴旋转对称的特性，它不随经度 $\gimel$ 而变。因此，可以假定水准椭球对外部点 $( \mathbf { \bar { u } } , \mathbf { \bar { \theta } } , \lambda )$ 的引力位为：

$$
\nabla _ { \{ v , \forall \} } = \mathsf { f } \left( \mathsf { u } \right) \mathsf { h } \left( \theta \right)
$$

其中 $\dot { \bf f } ( { \bf u } )$ 为只含变量 $\dot { \bf u }$ 的函数， $\operatorname { h } ( \pmb \theta )$ 为只含变量 $\cdot \overleftarrow { \theta }$ 的函数。将 $( 6 \cdot 5 )$ 式代入 $( 6 \cdot 4 )$ 式，则得

$$
( \mathbf { u } ^ { 2 } + \mathbf { E } ^ { 2 } ) \mathbf { f } ^ { \prime \prime } ( \mathbf { u } ) \mathbf { h } ( \theta ) + 2 \mathbf { u } \mathbf { f } ^ { \prime } ( \mathbf { u } ) \mathbf { h } ( \theta ) + \mathbf { h } ^ { \prime \prime } ( \theta ) \mathbf { f } \left( \mathbf { u } \right) + \mathrm { c t } \mathbf { g } \mathbf { h } ^ { \prime } ( \theta ) \mathbf { f } \left( \mathbf { u } \right) = 0
$$

除以 $\mathbf { f } ( \mathbf { u } ) \mathbf { h } ( \pmb \theta )$ ，并移项，得到

$$
( \dot { \mathbf { u } } ^ { 2 } + \mathbf { E } ^ { 2 } ) \frac { \mathbf { f } ^ { \prime \prime } ( \mathbf { u } ) } { \mathbf { f } \left( \mathbf { u } \right) } + 2 \mathbf { u } \frac { \mathbf { f } ^ { \prime } ( \mathbf { u } ) } { \mathbf { f } ( \mathbf { u } ) } = - \frac { 1 } { \mathbf { h } ( \theta ) } \mathbb { C } \mathbf { h } ^ { \prime \prime } ( \theta ) + \mathrm { c t g } \mathbf { \theta } \mathbf { h } ^ { \prime } ( \theta ) \mathbb { ) } ,
$$

很明显，方程的左端只是变量 $\pmb { \mathrm { u } }$ 的函数，而有只是变量 $\pmb \theta$ 的函数，两边要相等，只能是等于一个常数。今以 $\mathfrak { n } ( \mathfrak { n } + 1 )$ 表示这个常数，得到的两个微分方程：

$$
( { \bf u } ^ { 2 } + { \bf E } ^ { 2 } ) { \bf f } ^ { n } ( { \bf u } ) + 2 { \bf u } { \bf f } ^ { \prime } ( { \bf u } ) - { \bf n } ( { \bf n } + 1 ) { \bf f } \left( { \bf u } \right) = 0
$$

$$
\mathtt { h } ^ { \prime \prime } ( \theta ) + \mathtt { c } \mathtt { t } \mathtt { g } \mathtt { \theta } \mathtt { h } ^ { \prime } ( \theta ) + \mathtt { n } ( \mathtt { n } + 1 ) \mathtt { h } ( \theta ) = 0
$$

解这两个微分方程，就可求得 $\mathbf { f } \left( \mathbf { u } \right)$ 和 $\mathbf { h } \left( \theta \right)$ 的具体表达式。

为求解方程 $( 6 \cdot 6 )$ 式，引入新变量 $\pmb { \tau }$ ，它与原来的变量 $\mathbf { \ddot { u } }$ 有如下的关系：

$$
\dot { \boldsymbol { \tau } } { = } \dot { \mathbf { i } } \ \frac { \mathbf { u } } { \mathbf { E } }
$$

其中 $\mathbf { i } { = } \sqrt { - 1 }$ 。经变量代换后有

$$
\mathtt { f } ( \mathtt { u } ) { = } \overline { { \mathbf { f } } } ( \tau )
$$

$$
\mathrm { f ^ { \prime } } ( \mathrm { u } ) { = } \frac { \mathrm { d } \overline { { \mathrm { f } } } ( \tau ) } { \mathrm { d } \tau } \cdot \frac { \mathrm { d } \tau } { \mathrm { d } \mathrm { u } } { = } \overline { { \mathrm { f ^ { \prime } } } } ( \tau ) \frac { \mathrm { i } } { \mathrm { E } }
$$

$$
{ \bf f } ^ { \prime \prime } ( { \bf u } ) = { \frac { \bf d } { { \bf d } \tau } } ( { \bar { \bf f } } ^ { \prime } \ ( \tau ) { \frac { \bf i } { \mathrm { E } } } ) { \frac { \bf d \tau } { { \bf d u } } } = { \bar { \bf f } } ^ { \prime \prime } ( \tau ) { \frac { \mathrm { i } ^ { 2 } } { { \mathrm { E } } ^ { 2 } } } = - { \frac { { \bar { \bf f } } ^ { \prime \prime } ( \tau ) } { { \mathrm { E } } ^ { 2 } } }
$$

而

$$
\frac { \mathbf { u } ^ { 2 } + \mathbf { E } ^ { 2 } } { \mathbf { E } ^ { 2 } } { = } 1 { - } \tau ^ { 2 }
$$

考虑到这些， $( 6 \cdot 6 )$ 式就改化为：

$$
( 1 - \tau ^ { 2 } ) \bar { \mathbf { f } } ^ { \prime \prime } ( \tau ) - 2 \tau \mathbf { \Delta } \tilde { \mathbf { f } } ^ { \prime } ( \tau ) + \mathbf { n } \left( \mathbf { n } + 1 \right) \bar { \mathbf { f } } ( \tau ) = 0
$$

$( 6 \cdot 9 )$ 式与勒戎德多项式所满足的微分方程有完全相同的形式。因为是对于外部，恒有 $\mathbf { u } >$ E，由 $( 6 \cdot 8 )$ 式可得，此时 $\pmb { \tau }$ 的绝对值大于1。因此， $( 6 \cdot 9 )$ 式的解为第二类勒戎德多项式$Q _ { \mathfrak { n } } ( \tau )$ 。考虑到 $( 6 \cdot 8 )$ 式，解可写为 ${ \cal Q } _ { \mathfrak { n } } ( { \mathfrak { i } } \frac { \mathfrak { u } } { \overline { { \mathfrak { E } } } } ) ^ { \cdot }$ 。

为了解微分方程 $( 6 \cdot 7 )$ 式,引入新变量t,它与 $\boldsymbol { \theta }$ 有如下的关系：

$$
\scriptstyle \mathbf { t } = \mathbf { c o s } \theta
$$

经变量变换后得到

$$
\scriptstyle \left. { \begin{array} { l } { \displaystyle \mathtt { h } ( \theta ) = \overline { { \mathtt { h } } } ( \theta ) } \\ { \displaystyle \mathtt { h } ^ { \prime } ( \theta ) = \overline { { \mathtt { h } } } ^ { \prime } ( { \mathrm { t } } ) \frac { \mathtt { d } { \mathtt { t } } } { \mathtt { d } \theta } = - \sin \theta \overline { { \mathtt { h } } } ^ { \prime } ( { \mathrm { t } } ) } \\ { \displaystyle \mathtt { h } ^ { \prime \prime } ( \theta ) = ( 1 - { \mathrm { t } } ^ { \prime } ) \overline { { \mathtt { h } } } ^ { \prime \prime } ( { \mathrm { t } } ) - { \mathrm { t } } \overline { { \mathtt { h } } } ^ { \prime } ( { \mathrm { t } } ) } \end{array} } \right\}
$$

以 $( 6 \cdot 1 1 )$ 式代入 $( 6 \cdot 7 )$ 式，则得

$$
( 1 - \mathfrak { t } ^ { 2 } ) \overline { { \mathrm { h } } } ^ { \prime \prime } ( \mathfrak { t } ) - 2 \mathfrak { t } \overline { { \mathrm { h } } } ^ { \prime } ( \mathfrak { t } ) + \mathbf { n } ( \mathfrak { n } + 1 ) \overline { { \mathrm { h } } } ( \mathfrak { t } ) = 0
$$

$( 6 \cdot 1 2 )$ 式也是勒戎德多项式满足的微分方程。当 $\boldsymbol { \theta }$ 在0到 $\pmb { \pi }$ 之间变化时， $\mathbf { \nabla } \cdot \mathbf { t }$ 在 $+ 1$ 到-1的区间内变化。因此,微分方程 $( 6 \cdot 1 2 )$ 式的解为第一类勒戎德多项式 $\mathbf { P _ { n } } ( \mathbf { t } )$ 。考虑到 $( 6 \cdot 1 0 )$ 式，解可写为 $\mathrm { P _ { n } } ( \cos \theta )$ 。

这样一来，水准椭球对外部点的引力位就是微分方程 $( 6 \cdot 6 )$ 和 $( 6 \cdot 7 )$ 式的解的线性组合，即

$$
\mathrm { V } _ { ( \mathbf { u } , \boldsymbol { \vartheta } ) } = \sum _ { \mathfrak { n } = 0 } ^ { \infty } \mathrm { A } _ { \mathfrak { n } } \mathrm { Q } _ { \mathfrak { n } } ( \mathrm { i } \frac { \mathbf { u } } { \mathbf { E } } ) \mathrm { P } _ { \mathfrak { n } } ( \cos \theta )
$$

式中 $\mathsf { A } _ { \mathfrak { n } }$ 为常系数。实际上， $( 6 \cdot 1 3 )$ 式是用椭球谐函数表示的在椭球面外的与 $\gimel$ 无关的调和函数的一般形式。下面将针对引力位这一特定调和函数来确定其中的常系数 $\mathbf { A } _ { \mathfrak { n } }$ 。

为此，将 $( 6 \cdot 1 3 )$ 式加上离心力位组成重力位。因离心力位为

$$
\mathsf { Q } _ { ( \mathsf { u } , \mathsf { \theta } ) } = \frac { 1 } { 3 } \omega ^ { 2 } ( \mathsf { u } ^ { 2 } + \mathsf { E } ^ { 2 } ) - \frac { 1 } { 3 } \omega ^ { 2 } ( \mathsf { u } ^ { 2 } + \mathsf { E } ^ { 2 } ) \mathsf { P } _ { 2 } ( \mathsf { c o s } \theta )
$$

由 $( 6 \cdot 1 3 )$ 和 $( 6 \cdot 1 4 )$ 式相加得到重力位

$$
\mathrm { U _ { ( u , \theta ) } = \sum _ { n = 0 } ^ { \infty } A _ { n } Q _ { n } ( i \frac { u } { E } ) P _ { n } ( c o s \theta ) + \frac { 1 } { 3 } \omega ^ { 2 } ( u ^ { 2 } + E ^ { 2 } ) - \frac { 1 } { 3 } \omega ^ { 2 } ( u ^ { 2 } + E ^ { 2 } ) P _ { 2 } ( c o s \theta ) \left( 6 \theta ^ { 2 } + E ^ { 2 } \right) } ,
$$

水准椭球的表面 $a = b .$ 是一个等位面，设其位值为 $\mathrm { { U } } _ { 0 }$ ，则由 $( 6 \cdot 1 5 )$ 式可得：

$$
\sum _ { n = 0 } ^ { \infty } \mathrm { A _ { n } \mathrm { Q _ { n } ( i \frac { \partial } { \partial E } ) \mathrm { P _ { n } ( \cos \theta ) + \frac { 1 } { 3 } \mathrm { \omega ^ { 2 } a ^ { 2 } - \frac { 1 } { 3 } \mathrm { \omega ^ { 2 } a ^ { 2 } \mathrm { P _ { 2 } ( \cos \theta ) - \mathrm { U _ { \mathrm { 0 } } = 0 } } } } } } }
$$

这个等式中只有一个变量0，而且都是cos0的勒戎德多项式（常数项可看成是零阶勒戎德多项式乘一常数)。因此等式成立的条件是各阶勒戎德多项式的系数为零，因而有

$$
\left. \begin{array} { l } { { \displaystyle { \bf A } _ { \circ } { \bf Q } _ { o } ( \mathrm { i } \mathrm { \frac { \partial b } { E } } ) + \frac { 1 } { 3 } \omega ^ { 2 } { \bf a } ^ { 2 } - { \bf U } _ { \circ } = 0 } } \\ { { } } \\ { { \displaystyle { \bf A } _ { 2 } { \bf Q } _ { 2 } ( \mathrm { i } \mathrm { \frac { \partial b } { E } } ) - \frac { 1 } { 3 } \omega ^ { 2 } { \bf a } ^ { 2 } = 0 } } \\ { { } } \\ { { \displaystyle { \bf A } _ { 1 } = { \bf A } _ { 3 } = { \bf A } _ { 4 } = \cdots \cdots = 0 } } \end{array} \right\}
$$

从 $( 6 \cdot 1 6 )$ 式的前两个方程可以解得

$$
\mathbf { A } _ { 0 } { = } \frac { 1 } { \mathbf { Q } _ { 0 } ( \mathbf { i } } \frac { \mathbf { b } } { \mathbf { E } } )  ( \mathbf { U } _ { 0 } { - } \frac { 1 } { 3 } \omega ^ { 2 } a ^ { 2 } )
$$

$$
\mathbf { A } _ { 2 } { = } \frac { 1 } { \mathbf { Q } _ { 2 } ( \mathbf { i } \ \frac { \mathbf { b } } { \mathbf { E } } ) } \frac { 1 } { 3 } \mathbf { \omega } ^ { 2 } \mathbf { a } ^ { 2 }
$$

将这些结果代入 $( 6 \cdot 1 4 )$ 式，则得水准椭球对外部点的引力位为

$$
\mathsf { V } _ { ( \mathbf { u } , \boldsymbol { \mathfrak { e } } ) } = ( \mathsf { U } _ { 0 } - \frac { 1 } { 3 } \omega ^ { 2 } \mathsf { a } ^ { 2 } ) \frac { \mathbf { Q } _ { 0 } ( \mathrm { i } \frac { \mathbf { u } } { \mathbf { E } } ) } { \mathbf { Q } _ { 0 } ( \mathrm { i } \frac { \mathbf { b } } { \mathbf { E } } ) } + \frac { 1 } { 3 } \omega ^ { 2 } \mathsf { a } ^ { 2 } \frac { \mathbf { Q } _ { 2 } ( \mathrm { i } \frac { \mathbf { u } } { \mathbf { E } } ) } { \mathbf { Q } _ { 2 } ( \mathrm { i } \frac { \mathbf { b } } { \mathbf { E } } ) } \mathbf { P } _ { 2 } ( \cos \theta )
$$

为了应用方便，还需将(6·17)式中的第二类勒戎德多项式改化掉。依据定义有

$$
\mathbf { \bar { Q } } _ { 0 } ( \mathbf { i } \frac { \mathbf { u } } { \mathbf { E } } ) = \mathbf { c } \mathbf { t } \mathbf { h } ^ { - 1 } \mathbf { i } \frac { \mathbf { u } } { \mathbf { E } }
$$

$$
{ \bf Q } _ { 2 } ( \mathrm { \bf ~ i } \frac { \mathrm { \bf ~ u } } { \mathrm { \bf ~ E } } ) = ( \frac { 3 } { 2 } \mathrm { i } ^ { 2 } \frac { \mathrm { \bf ~ u } ^ { 2 } } { \mathrm { \bf ~ E } ^ { 2 } } - \frac { 1 } { 2 } ) \tt c t h ^ { - 1 } \mathrm { \bf ~ i } \frac { \mathrm { \bf ~ u } } { \mathrm { \bf ~ E } } - \frac { 3 } { 2 } \mathrm { i } \frac { \mathrm { \bf ~ u } } { \mathrm { \bf ~ E } }
$$

利用三角函数与双曲线函数之间的关系式

通过运算可以得到

$$
{ \sf Q } _ { 0 } ( \mathrm { i } \frac { { \sf u } } { { \sf E } } ) = - \mathrm { i } { \sf t g } ^ { - 1 } \frac { { \sf E } } { { \sf u } }
$$

$$
\mathbf { Q } _ { 2 } ( \mathbf { i } \frac { \mathbf { u } } { \mathbf { E } } ) { = } \mathbf { i } \mathbf { q }
$$

其中

$$
\mathbf { q } { = } \frac { 1 } { 2 } \mathbb { ( } ( 1 { + } 3 \frac { \mathbf { u } ^ { 2 } } { \mathbf { E } ^ { 2 } } ) \mathbf { t g } ^ { - 1 } \frac { \mathbf { E } } { \mathbf { u } } { - } 3 \frac { \mathbf { u } } { \mathbf { E } } \mathbb { ) } .
$$

同理，还可得出

$$
\mathbf { Q } _ { 0 } ( \mathrm { i } \frac { \mathbf { b } } { \mathbf { E } } ) = - \mathrm { i } \mathbf { t g } ^ { - 1 } \frac { \mathbf { E } } { \mathbf { b } }
$$

$$
\mathbf { Q } _ { 2 } ( \mathbf { i } ~ \frac { \mathbf { b } } { \mathbf { E } } ) = \mathrm { i } \mathbf { q } _ { 0 }
$$

其中

$$
{ \bf q } _ { 0 } { = } \frac { 1 } { 2 } ( ( 1 { + } 3 \frac { { \bf b } ^ { 2 } } { { \bf E } ^ { 2 } } ) \mathbf { t g } ^ { - 1 } \frac { \mathbf { E } } { { \bf b } } { - } 3 \frac { { \bf b } } { { \bf E } } )
$$

考虑到以上这些关系式，由 $( 6 \cdot 1 7 )$ 式可得

$$
{ \bf V } _ { ( \mathfrak { n } , \theta ) } = ( \mathbf { U } _ { 0 } - \frac { 1 } { 3 } \omega ^ { 2 } \mathfrak { a } ^ { 2 } ) \frac { \mathfrak { t g } ^ { - 1 } \frac { \mathbf { E } } { \mathfrak { u } } } { \mathfrak { t g } ^ { - 1 } \frac { \mathbf { E } } { \mathfrak { b } } } + \frac { 1 } { 3 } \omega ^ { 2 } \mathfrak { a } ^ { 2 } \frac { \mathbf { q } } { \mathbf { q } _ { 0 } } \mathbb { P } _ { 2 } \left( \cos \theta \right)
$$

$( 6 \cdot 2 0 )$ 式给出了水准椭球对外部点的引力位与 $\mathrm { U } _ { \circ , \ast } \underset { \ast , \ast } { \omega } \underset { \ast } { \circ } \alpha$ 四个参数的关系。但通常给出的是水准椭球的质量M，而不给出 $\mathrm { { U } } _ { \mathfrak { n } }$ 值，故尚需导出推求 $\mathbf { U } _ { 0 }$ 的公式。

椭球坐标为 $( \mathbf { u } , \boldsymbol { \theta } )$ 的点至坐标原点(椭球中心)的距离 $P$ 可按下式求得：

$$
\overset { \cdot } { \underset { \rho = \cdot } { \rho = \cdot } } \sqrt { \mathrm { \mathbf { u } } ^ { 2 } + \mathrm { \mathbf { E } } ^ { 2 } \mathrm { \mathbf { s i n } } ^ { 2 } \mathrm { \hat { \boldsymbol { \theta } } } }
$$

对于椭球面外的点，有 $\rho { \geqslant } { \tt u } { > } { \tt E }$ ，故可写出如下的关系式：

$$
\frac { 1 } { \mathsf { u } } = \frac { 1 } { \mathsf { \rho } } ( 1 - \frac { \mathsf { E } ^ { 2 } } { \mathsf { \rho } ^ { 2 } } \mathrm { s i n } ^ { 2 } \theta ) ^ { - \frac { 1 } { 2 } } = \frac { 1 } { \mathsf { \rho } } + \mathsf { O } ( \frac { 1 } { \mathsf { \rho } ^ { 3 } } )
$$

其中 $0 ( \frac { 1 } { \rho ^ { 3 } } .$ 表示分母为 $p$ 的三次幂及更高次幂的各项。;同时有

$$
\mathrm { t g } ^ { - 1 } \frac { \mathrm { \bf G } } { \mathrm { \bf u } } { = } \frac { \mathrm { \bf G } } { \mathrm { \bf u } } { . } + 0 ( \frac { 1 } { \mathrm { \bf u } ^ { 3 } } ) { = } \frac { \mathrm { \bf G } } { \rho } { + } 0 ( \frac { 1 } { \rho ^ { 3 } } )
$$

代入 $( 6 \cdot 2 0 )$ 式，则得

$$
V _ { ( { \bf u } , { \boldsymbol \theta } ) } = ( \mathrm { U } _ { 0 } - { \frac { 1 } { 3 } } \omega ^ { 2 } { \bf a } ^ { 2 } ) { \frac { \displaystyle { \frac { \mathrm { E } } { \rho } } } { \displaystyle { \bf t g ^ { - 1 } } { \frac { \mathrm { E } } { \mathrm { b } } } } } + 0 \dot { ( } { \frac { 1 } { \rho ^ { 3 } } } )
$$

另一方面,水准椭球对外部点的引力位在用球谐函数级数式表示时，只有偶阶带谐项，因而可写为

$$
v = \frac { f ( M } { \rho } + \theta ( \frac { 1 } { \rho ^ { 3 } } )
$$

式中 $\frac { \mathbf { f } \mathbf { M } } { \rho }$ 是零阶项， $0 ( \frac { 1 } { \rho ^ { 3 } } )$ 是二阶以上各项。对照上两个式子，可得

$$
\mathbf { f } \dot { \mathbf { M } } { = } ( \mathbf { U } _ { 0 } { - } \frac { 1 } { 3 } \omega ^ { 2 } \mathbf { a } ^ { 2 } ) \frac { \dot { \mathbf { E } } } { 1 \mathbf { g } ^ { - 1 } \frac { \mathbf { E } } { \dot { \mathbf { b } } } }
$$

移项后得到

$$
{ \bf U } _ { 0 } { = } \frac { { \bf f } { \bf M } } { { \bf E } } { \bf t } { \bf g } ^ { - 1 } \frac { { \bf E } } { { \bf b } } { + } \frac { 1 } { 3 } \omega ^ { 2 } { \bf a } ^ { 2 }
$$

$( 6 \cdot 2 3 )$ 式给出了水准椭球表面上的重力位值 $\mathbf { U } _ { \mathfrak { o } }$ 与四个基本参数 $M , \omega , a , \alpha$ 之间的关系。将$( 6 \cdot 2 3 )$ 式代入 $( 6 \cdot 2 0 )$ 式，则得

$$
V _ { ( { \mathrm { u } } , { \mathrm { \scriptsize 6 } } ) } = \frac { \mathrm { f } \mathrm { M } } { \mathrm { E } } { \mathrm { t g } } ^ { - 1 } \frac { \mathrm { E } } { \mathrm { u } } + \frac { 1 } { 3 } { \omega } ^ { 2 } { \mathrm { a } } ^ { 2 } \frac { { \mathrm { q } } } { { \mathrm { q } } _ { 0 } } { \mathrm { P } } _ { 2 } ( \cos { \theta } )
$$

$( 6 \cdot 2 4 )$ 式就是根据水准椭球的四个基本参数推求外部点引力位的公式。加上离心力位（6·14)式，则得水准椭球对外部点的重力位

$$
\mathrm { U } _ { ( \mathrm { u } , \theta ) } = \frac { \mathrm { f } \mathrm { M } } { \mathrm { E } } \mathrm { t } \mathrm { g } ^ { - 1 } \frac { \mathrm { E } } { \mathrm { u } } + \frac { 1 } { 2 } \omega ^ { 2 } \mathrm { a } ^ { 2 } \frac { \mathrm { q } } { \mathrm { q } _ { 0 } } ( \cos ^ { 2 } \theta - \frac { 1 } { 3 } ) + \frac { 1 } { 2 } \omega ^ { 2 } ( \mathrm { u } ^ { 2 } + \mathrm { E } ^ { 2 } ) \sin ^ { 2 } \theta
$$

# 6.2椭球面上的重力

依据位和力的关系，重力可以通过对重力位求导而得到。设 $\mathsf { \pmb { S } } _ { \mathbf { u } }$ 为坐标面 ${ \mathfrak { u } } = { \mathfrak { c } }$ 的法线方向， $\gamma _ { \ast }$ 表示重力在 $\mathfrak { s } _ { \mathfrak { u } }$ 方向上的分量，则有

$$
- \gamma _ { \dot { \mathfrak { i } } } = \frac { \partial \mathbf { U } _ { ( \mathfrak { u } , \theta ) } } { \partial \mathbf { S } _ { \mathfrak { u } } }
$$

因为 $\mathbf { S } _ { \mathbf { u } }$ 线段上其他两个坐标 $\pmb \theta$ 和 $\gimel$ 为常数，因此有

$$
- Y _ { \mathrm { { u } } } = \frac { \partial \mathbf { U } _ { \mathrm { { \left( u , \theta \right) } } } } { \partial \mathbf { u } } \frac { \mathrm { d } \mathbf { u } } { \mathrm { d } \mathbf { S } _ { \mathrm { { u } } } }
$$

而

$$
\frac { \mathrm { { d } } \mathbf { u } } { \mathrm { { d } } \mathbf { S _ { u } } } { = } \frac { 1 } { \mathbf { h _ { 1 } } }
$$

将 $( 6 \cdot 3 )$ 式的第一式代入，则得

$$
\frac { \mathrm { d u } } { \mathrm { d } \mathbb { S } _ { \mathrm { u } } } { = } \sqrt { \frac { { \mathrm { \bf ~ u } } ^ { 2 } + \mathbb { E } ^ { 2 } } { { \mathrm { \bf ~ u } } ^ { 2 } + \mathbb { E } ^ { 2 } \cos ^ { 2 } \theta } } \mathrm { ~ . ~ }
$$

把它代人 $( 6 \cdot 2 6 )$ 式，得到

$$
- \gamma _ { \mathrm { u } } { = } \sqrt { \frac { \mathrm { u } ^ { 2 } + \mathrm { E } ^ { 2 } } { \mathrm { u } ^ { 2 } + \mathrm { E } ^ { 2 } \cos ^ { 2 } \theta } } \frac { \partial \mathrm { U } _ { ( \mathrm { u } , \theta ) } } { \partial \mathrm { u } }
$$

因为

$$
\frac { \partial } { \partial { \bf u } } ( \ d _ { \bf t } { \bf g } ^ { - 1 } \frac { \ d _ { \bf E } } { \ d { \bf u } } ) = \frac { - \bf E } { \ d { \bf u } ^ { 2 } + \ d { \bf E } ^ { 2 } }
$$

由 $( 6 \cdot 1 8 )$ 式可得

$$
\frac { \partial { \bf q } } { \partial { \bf u } } = \frac { \mathrm { d } { \bf q } } { \mathrm { d } { \bf u } } = - \frac { 1 } { 2 } ( 1 + 3 \frac { { \bf u } ^ { 2 } } { \mathrm { E } ^ { 2 } } ) \frac { \mathrm { E } } { { \bf u } ^ { 2 } + \mathrm { E } ^ { 2 } } + \frac { 3 { \bf u } } { \mathrm { E } ^ { 2 } } \mathrm { t g } ^ { - 1 } \frac { \mathrm { E } } { \mathrm { \bf u } } - \frac { 3 } { 2 \mathrm { E } }
$$

考虑到这两个等式，由 $( 6 \cdot 2 5 )$ 式可以求得

$$
\frac { \partial \mathrm { U } _ { ( \mathrm { u } , \theta ) } } { \partial \mathrm { u } } = - \lbrack \frac { \mathrm { f } \mathrm { M } } { \mathrm { u } ^ { 2 } + \mathrm { E } ^ { 2 } } - \frac { \omega ^ { 2 } a ^ { 2 } } { \mathrm { q } _ { 0 } } \frac { \mathrm { d } \mathrm { q } } { \mathrm { d } \mathrm { u } } ( \frac { 1 } { 2 } \mathrm { c o s } ^ { 2 } \theta - \frac { 1 } { 6 } ) - \omega ^ { 2 } \mathrm { u } \mathrm { s i n } \theta )
$$

将 $( 6 \cdot 2 9 )$ 式代入 $( 6 \cdot 2 7 )$ 式，得到

$$
\gamma _ { \mathrm { { s } } } = { \sqrt { \frac { \mathrm { { u } } ^ { 2 } + \mathrm { { E } } ^ { 2 } } { \mathrm { { u } } ^ { 2 } + \mathrm { { E } } ^ { 2 } \cos ^ { 2 } \theta } } } { \boldsymbol { \zeta } } { \frac { \mathrm { { f } } \mathrm { { M } } } { \mathrm { { u } } ^ { 2 } + \mathrm { { E } } ^ { 2 } } } - { \frac { \omega ^ { 2 } \mathrm { { a } } ^ { 2 } } { \mathrm { { q } } _ { 0 } } } { \frac { \mathrm { { d } } \mathrm { { q } } } { \mathrm { { d } } \mathrm { { u } } } } ( { \frac { 1 } { 2 } } \cos ^ { 2 } \theta - { \frac { 1 } { 6 } } ) - \omega ^ { 2 } \mathrm { { u } } \sin \theta ) ~ ,
$$

对于水准椭球的表面，它是坐标面 $\ y = 6$ ，也是个等位面，所以它的法线方向就是重力方向，即 $( Y _ { \parallel } ) _ { \parallel = \ b }$ 就是水准椭球面上的重力值 $\Upsilon _ { 0 }$ 。这样，由 $( 6 \cdot 3 0 )$ 式可得

$$
\gamma _ { \mathrm { { o } } } = { \sqrt { { \frac { z ^ { 2 } \cdot z ^ { 2 } } { { \bf { b } } ^ { 2 } + { \bf { E } } ^ { 2 } { \cos ^ { 2 } } \theta } } } } { \Big \{ } { \frac { { \bf { f } } { \bf { M } } } { { \bf { a } } ^ { 2 } } } +  \frac { { \bf { \omega } } ^ { 2 } { \bf { a } } ^ { 2 } { \bf { E } } } { \frac { { \bf { q } } _ { 0 } } { 2 } } { \bf { \omega } } ( { \frac { 1 } { 2 } } { \cos ^ { 2 } } \theta - { \frac { 1 } { 6 } } ) - { \bf { \omega } } ^ { 2 } { \bf { b } } { \sin ^ { 2 } } \theta { \Big \} }
$$

其中

$$
q _ { 0 } ^ { ' } = ( - \frac { \mathbf { u } ^ { 2 } + \mathbf { E } ^ { 2 } } { \mathbf { E } } \frac { \mathrm { d } \mathbf { q } } { \mathrm { d } \mathbf { u } } ) _ { \mathfrak { u } = \mathfrak { b } } = 3 ( 1 + \frac { \mathbf { b } ^ { 2 } } { \mathbf { E } ^ { 2 } } ) ( 1 - \frac { \mathbf { b } } { \mathbf { E } } \mathbf { t g } _ { \cdot } ^ { - 1 } \frac { \mathbf { E } } { \mathbf { b } } ) - 1
$$

(6·31)式就是由水准椭球的基本参数计算椭球面上重力值的公式，它随极距 $\pmb \theta$ 而变。下面再对它作些改化。

因为

$$
E ^ { 2 } = { \bf a } ^ { 2 } - { \bf b } ^ { 2 } \qquad \& = 9 0 ^ { \circ } - \theta
$$

再令

$$
{ \frac { \omega ^ { 2 } \mathbf { a } ^ { 2 } \mathbf { b } } { \mathbf { f } \mathbf { M } } } = \mathbf { m }
$$

和

$$
\frac { \mathbf { E } } { \mathbf { b } } { = } \mathbf { e } ^ { \prime }
$$

则 $( 6 \cdot 3 1 )$ 式可写为

$$
\gamma _ { \circ } = \frac { \mathrm { f } \mathrm { \bf { M } } } { \mathrm { a \sqrt { a ^ { 2 } \sin ^ { 2 } \beta + b ^ { 2 } \cos ^ { 2 } \beta } } } \mathrm { [ } ( 1 + \frac { 1 } { 3 } \mathrm { m e ^ { \prime } ~ } \frac { \mathrm { q } _ { \circ } ^ { \prime } } { \mathrm { q } _ { \mathrm { 0 } } } ) \mathrm { s i n } ^ { 2 } \mathrm { \beta + } ( 1 - \mathrm { m } - \frac { 1 } { 6 } \mathrm { m e ^ { \prime } ~ } \frac { \mathrm { q } _ { \circ } ^ { \prime } } { \mathrm { q } _ { \mathrm { 0 } } } ) \mathrm { c o s } ^ { 2 } \mathrm { \beta ] }
$$

在这个式子中，令 ${ \beta = 0 }$ ，则得椭球面上赤道处的正常重力值 $\pmb { \gamma _ { \mathrm { a } } }$ ,即

$$
\gamma _ { \mathrm { { s } = \frac { f M } { a b } ( 1 - m - \frac { 1 } { 6 } m \frac { e ^ { \prime } q _ { 0 } ^ { \prime } } { \bf { q } } ) } }
$$

若令 $\beta = 9 0 ^ { \circ }$ ，则得椭球面上极点处的重力值 $\boldsymbol { \Upsilon } _ { \mathfrak { p } }$ ,即

$$
\gamma _ { \mathrm { p } } = \frac { \mathbf { f } \mathbf { M } } { \mathbf { a } ^ { 2 } } ( 1 + \frac { 1 } { 3 } \mathbf { m } \ \frac { \mathrm { e } ^ { \prime } \mathbf { \Delta q } _ { 0 } } { \mathbf { q } _ { 0 } } )
$$

这样一来， $\gamma _ { \mathfrak { o } }$ 的公式可写为

$$
\gamma _ { \scriptscriptstyle 0 , } = \frac { \mathrm { a } \gamma _ { \scriptscriptstyle \mathrm { p } } \mathrm { s i n } ^ { 2 } \beta + \mathrm { b } \gamma _ { \scriptscriptstyle \mathrm { s } } \mathrm { c o s } ^ { 2 } \beta } { \sqrt { \mathrm { a } ^ { 2 } \mathrm { s i n } ^ { 2 } \beta + \mathrm { b } ^ { 2 } \mathrm { c o s } ^ { 2 } \beta } }
$$

这就是所谓的索米里安(Somigliano.C.)公式，它表示了水准椭球面上重力值的变化规律。但公式中的变量是归化纬度 $\beta$ ，不便于使用。现将其转化为大地纬度表示。今以B表示大地纬度，它是椭球面法线与赤道面的夹角。因为

$$
\mathbf { \Delta t g                 beta { = } \frac { b } { a } { \dot { \mathbf { t } } } g B }
$$

进而有

$$
\begin{array} { c } { { \cos ^ { 2 } \beta { = } \frac { a ^ { 2 } { \cos ^ { 2 } \mathrm { B } } } { a ^ { 2 } { \cos ^ { 2 } \mathrm { B } } + { \mathrm { b } } ^ { 2 } { \sin ^ { 2 } \mathrm { B } } } } } \\ { { \sin ^ { 2 } \beta { = } \frac { { \mathrm { b } } ^ { 2 } { \sin ^ { 2 } \mathrm { B } } } { a ^ { 2 } { \cos ^ { 2 } \mathrm { B } } + { \mathrm { b } } ^ { 2 } { \sin ^ { 2 } \mathrm { B } } } } } \end{array}
$$

将它们代入 $( 6 \cdot 3 7 )$ 式，经运算后得到

$$
\gamma _ { \mathrm { 0 } } = \frac { \mathrm { b } \gamma _ { \mathrm { p } } \mathrm { s i n } ^ { 2 } \mathrm { B } + \mathrm { a } \gamma _ { \mathrm { a } \mathrm { c o s } } \mathrm { } ^ { 2 } \mathrm { B } } { \sqrt { \mathrm { a } ^ { 2 } \mathrm { c o s } ^ { 2 } \mathrm { B } + \mathrm { b } ^ { 2 } \mathrm { s i n } ^ { 2 } \mathrm { B } } }
$$

$( 6 \cdot 3 8 )$ 式中， $\Upsilon _ { \mathfrak { p } }$ 和 $\pmb { \gamma _ { \mathrm { a } } }$ 可由椭球的基本参数分别按 $( 6 \cdot 3 6 )$ 和 $( 6 \div 3 5 )$ 式算出，因此 $\boldsymbol { \Upsilon } _ { \mathfrak { o } }$ 只随B而变。利用 $( 6 \cdot 3 8 )$ 式，可以根据大地纬度算得水准椭球面上任一点的重力值。

# $\ S 6 . 3$ 椭球面上重力位和重力的级数式

上两节导出的重力位和重力的表达式都是严密公式，在实用时不甚方便。尚需用级数展开的方法导出级数形式的实用公式，这样就可根据不同的精度要求进行运用。从目前的实际情况看·需要取至扁率三级小，约为 $1 0 ^ { - \gamma }$ 的精度。由 $( 6 \cdot 3 3 )$ 和 $( 6 \cdot 3 4 )$ 式算出的 $\mathbf { m }$ 和 $\mathsf { e } ^ { \prime \mathsf { 2 } }$ 有与 $\pmb { \alpha }$ 相同的量级。在下面的推导过程中，所有展开式的取项都是以保证达到这一精度为目标的。

先改化计算椭球面上重力值的公式 $( 6 \cdot 3 8 )$ 。为此，要把推求 $\pmb { \gamma } _ { \ast }$ 和 $\boldsymbol { \Upsilon } _ { \mathfrak { p } }$ 的公式 $( 6 \cdot 3 5 )$ 和$( 6 \cdot 3 6 )$ 式变为级数形式。利用级数展开的公式，由 $( 6 \cdot 3 4 )$ 式可得

$$
\mathbf { t } g ^ { - 1 } \frac { \mathbf { E } } { \mathbf { b } } { = } \mathbf { t } g ^ { - 1 } \mathbf { e } ^ { \prime } = \mathbf { e } ^ { \prime } - \frac { 1 } { 3 } \mathbf { e } ^ { \prime } { } ^ { 3 } + \frac { 1 } { 5 } \mathbf { e } ^ { \prime } { } ^ { 5 } - \frac { 1 } { 7 } \mathbf { e } ^ { \prime } { } ^ { 7 } + \frac { 1 } { 9 } \mathbf { e } ^ { \prime } { } ^ { 9 } - \frac { 1 } { 1 1 } \mathbf { e } ^ { \prime } { } ^ { 1 1 }
$$

将它代入 $( 6 \cdot 3 2 )$ 和 $( 6 \cdot 1 9 )$ 式，得到

$$
\begin{array} { l } { { \displaystyle { \mathfrak { q } } _ { \mathfrak { i } } { \mathrm { = } } { \frac { 2 } { 5 } } { \mathrm { e } } ^ { \prime } { \mathrm { \mathrm { \mathrm { \mathrm { \ell } } } } ^ { 2 } } ( 1 { \mathrm { - } } { \frac { 3 } { 7 } } { \mathrm { e } } ^ { \prime } { \mathrm { \mathrm { \ell } } ^ { 2 } } { \mathrm { + } } { \frac { 5 } { 2 1 } } { \mathrm { e } } ^ { \prime } { \mathrm { \ell } } ^ { 4 } { \mathrm { - } } { \frac { 5 } { 3 3 } } { \mathrm { e } } ^ { \prime } { \mathrm { \ell } } ^ { 6 } ) } }  \\ { { \displaystyle { \mathfrak { q } } _ { \mathfrak { i } } { \mathrm { = } } { \frac { 2 } { 1 5 } } { \mathrm { e } } ^ { \prime } { \mathrm { \mathrm { \ell } } } ^ { 3 } ( 1 { \mathrm { - } } { \frac { 6 } { 7 } } { \mathrm { e } } ^ { \prime } { \mathrm { \mathrm { \ell } } } ^ { 2 } { \mathrm { + } } { \frac { 5 } { 7 } } { \mathrm { e } } ^ { \prime } { \mathrm { \ell } } ^ { 4 } { \mathrm { - } } { \frac { 2 0 } { 3 3 } } { \mathrm { e } } ^ { \prime } { \mathrm { \ell } } ^ { 6 } ) } }  \end{array}
$$

因而可以算得

$$
\frac { \mathrm { e } ^ { \prime } \ : \mathrm { q } _ { \mathrm { e } } } { \mathrm { q } } { = } 3 ( 1 + \frac { 3 } { 7 } \mathrm { e } ^ { \prime \ : 2 } { - } \frac { 1 6 } { 1 4 7 } \mathrm { e } ^ { \prime \ : 4 } { + } \frac { 2 1 8 } { 3 7 7 3 } \mathrm { e } ^ { \prime \ : 6 } )
$$

因为

$$
\mathfrak { b } { = } \mathfrak { a } \left( 1 { - } \mathfrak { a } \right)
$$

与 $( 6 \cdot 2 )$ 式一起可得

$$
\operatorname { e } ^ { \prime } = { \frac { \mathbf { E } } { \mathbf { b } } } { = } { \frac { \sqrt { 2 \alpha - \alpha ^ { 2 } } } { 1 - \alpha } }
$$

因而可以求得

$$
\left. \begin{array} { l } { { { \mathrm { e } ^ { \prime } } { } ^ { 2 } = 2 \alpha + 3 \alpha ^ { 2 } + 4 { \alpha } ^ { 3 } } } \\ { { } } \\ { { { \mathrm { e } ^ { \prime } } { } ^ { 4 } = 4 { \alpha } ^ { 2 } + 1 2 { \alpha } ^ { 3 } } } \\ { { } } \\ { { { \mathrm { e } ^ { \prime } } { } ^ { \delta } = 8 { \alpha } ^ { \mathrm { 5 } } } } \end{array} \right\}
$$

将 $( 6 \cdot 4 1 )$ 式代入 $( 6 \cdot 4 0 )$ 式，得到

$$
\frac { \mathrm { e } ^ { \prime } \mathrm { g } _ { \scriptscriptstyle 0 } } { \mathrm { 4 } } = 3 ( 1 \div \frac { 6 } { 7 } \alpha + \frac { 1 2 5 } { 1 4 7 } \alpha ^ { 2 } + \frac { 3 2 0 4 } { 3 7 7 3 } \alpha ^ { 3 } )
$$

利用 $( 6 \cdot 4 2 )$ 式，可将 $( 6 \cdot 3 5 )$ 和 $( 6 ~ \cdot ~ 3 6 )$ 式分别改化为

$$
Y _ { a } = { \frac { \mathbf { f } _ { i } ^ { \mathsf { r } } { \mathsf { M } } } { \mathsf { a } { \mathsf { b } } } } ( 1 - { \frac { ? } { 2 } } \mathsf { m } - { \frac { ? } { 7 } } \mathsf { m } \alpha - { \frac { 1 2 5 } { 2 9 4 } } \mathsf { m } \alpha ^ { \colon } )
$$

$$
Y _ { ; } = { \frac { \mathbf { f } \mathbf { M } } { a ^ { 2 } } } ( 1 + \mathbf { m } + { \frac { 6 } { 7 } } \mathbf { m } \alpha + { \frac { 1 2 5 } { 1 4 7 } } \mathbf { m } \alpha ^ { 2 } )
$$

将 $( 6 \cdot 4 3 )$ 和 $( 6 \cdot 4 4 )$ 式代入 $( 6 \cdot 3 8 )$ 式，完成繁琐的运算后得到

$$
\gamma _ { \mathrm { { s } } } = \gamma _ { \mathrm { { s } } } ( 1 + \mathrm { { \frac { 1 } { s } } \mathrm { { s } } \mathrm { { i n } } ^ { \div } \mathrm { { 3 } } \mathrm { { \frac { 1 } { s } } \mathrm { { i n } } ^ { \ast } \mathrm { { B } } + \mathrm { { f } } _ { \mathrm { { s } } } \mathrm { { s } } \mathrm { { i n } } ^ { \ast } \mathrm { { B } } ) } }
$$

式中

$$
\left. \begin{array} { l } { { \displaystyle \mathrm { f } _ { \mathrm { 2 } } = - \alpha + \frac { 5 } { 2 } \mathrm { m } + \frac { 1 } { 2 } \alpha ^ { 2 } - \frac { 2 6 } { 7 } \mathrm { m } \alpha + \frac { 1 5 } { 4 } \mathrm { m } ^ { 2 } + \frac { 5 9 } { 1 4 9 } \mathrm { m } \alpha ^ { 2 } - \frac { 9 } { 7 } \mathrm { m } ^ { 2 } \alpha + \frac { 4 5 } { 8 } \mathrm { m } ^ { 3 } } } \\ { { \displaystyle \mathrm { f } _ { \mathrm { 4 } } = - \frac { 1 } { 2 } \alpha ^ { 2 } + \frac { 5 } { 2 } \mathrm { m } \alpha + \frac { 1 } { 2 } \alpha ^ { 3 } - \frac { 1 3 9 } { 2 8 } \mathrm { m } \alpha ^ { 2 } + \frac { 1 5 } { 4 } \mathrm { m } ^ { 2 } \alpha } } \\ { { \displaystyle \mathrm { f } _ { \mathrm { 6 } } = - \frac { 1 } { 2 } \alpha ^ { 3 } + \frac { 7 5 } { 4 } \mathrm { m } \alpha ^ { 2 } } } \end{array} \right\}
$$

目前习惯于使用保留至 $\pmb { \alpha }$ 二级小的公式。因为

$$
\sin ^ { 4 } \mathrm { B } = \sin ^ { 2 } \mathrm { B } - { \frac { 1 } { 4 } } \sin ^ { 2 } 2 \mathrm { B }
$$

由 $( 6 \cdot 4 5 )$ 式可以得到

$$
\gamma _ { \scriptscriptstyle 0 } = \gamma _ { \scriptscriptstyle \mathrm { a } } ( 1 + \beta \sin ^ { 2 } \mathrm { B } - \beta _ { \scriptscriptstyle 1 } \sin ^ { 2 } 2 \mathrm { B } )
$$

式中

$$
\begin{array} { l } { { \displaystyle \beta = \hat { \mathrm { t } } _ { 2 } + \mathrm { f } _ { 4 } = - \alpha + \frac 5 2 \mathrm { m } - \frac { \mathrm { l } 7 } { \mathrm { 1 4 } } \mathrm { m } \alpha + \frac { 1 5 } { 4 } \mathrm { m } ^ { 2 } \Bigg \} } } \\ { { \displaystyle \beta _ { 1 } = \frac 1 4 \mathrm { f } _ { 4 } = - \frac 1 8 \alpha ^ { 2 } + \frac 5 8 \mathrm { m } \alpha } } \end{array}
$$

$( 6 \cdot 4 7 )$ 式就是推求水准椭球面上重力值的实用公式，其中的常数 $\Upsilon _ { \mathrm { a } \setminus \beta }$ 和 $\beta _ { \mathrm { { l } } }$ 可由椭球的四个基本参数求得。

下面改化计算椭球面上重力位值 $\mathrm { { U } } _ { \mathfrak { I } }$ 的公式 $( \zeta \cdot 2 3 )$ 式。由 $( 6 \cdot 3 3 )$ 式可得