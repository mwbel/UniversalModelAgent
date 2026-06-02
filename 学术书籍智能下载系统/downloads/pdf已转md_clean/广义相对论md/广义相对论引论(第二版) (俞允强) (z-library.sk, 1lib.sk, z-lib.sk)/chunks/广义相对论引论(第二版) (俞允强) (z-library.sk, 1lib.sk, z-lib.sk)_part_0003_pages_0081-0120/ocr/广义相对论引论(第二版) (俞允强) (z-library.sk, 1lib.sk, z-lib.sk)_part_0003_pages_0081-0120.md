先按公式

$$
T _ { \mu \lambda } ^ { a } = \frac { 1 } { 2 } g ^ { \alpha \nu } ( g _ { \mu , \lambda } + g _ { \nu \lambda , \mu } - g _ { \lambda \mu , \nu } )
$$

算出克里斯朵夫联络的非零分量为

$$
\begin{array} { r c l } { { } } & { { } } & { { \displaystyle r _ { 1 0 } ^ { 0 } = \frac { 1 } { 2 } \nu ^ { \prime } , \quad r _ { 1 1 } ^ { 1 } = \frac { 1 } { 2 } \mu ^ { \prime } , \quad r _ { \scriptscriptstyle 0 0 } ^ { 1 } = \frac { 1 } { 2 } \mathrm { e } ^ { \nu - \mu _ { \chi ^ { \prime } } } , } } \\ { { } } & { { } } & { { } } \\ { { } } & { { \displaystyle r _ { 2 2 } ^ { 1 } = \cdots r \mathrm { e } ^ { - \mu } , \quad r _ { \scriptscriptstyle 3 3 } ^ { 1 } = - r \mathrm { e } ^ { - \mu } \mathrm { s i n } ^ { 2 } \theta , \quad { \cal T } _ { \scriptscriptstyle 1 2 } ^ { 2 } = \frac { 1 } { r } . } } \\ { { } } & { { } } & { { } } \\ { { } } & { { \displaystyle r _ { 3 3 } ^ { 2 } = - \mathrm { s i n } \theta \mathrm { c o s } \theta , \quad r _ { \scriptscriptstyle 1 3 } ^ { 3 } = \frac { 1 } { r } , \quad r _ { \scriptscriptstyle 2 3 } ^ { 3 } = \frac { \mathrm { c o s } \theta } { \mathrm { s i n } \theta } , } } \end{array}
$$

其中 $\mu ^ { \prime }$ 和 $\nu ^ { \prime }$ 分别是 $\mu$ 和 $v$ 对 $r$ 的微商：然后按定义式(1.6.6)和(1.6.3)得出的关系

$$
R _ { \mu \nu } = R _ { \mu \nu \lambda } ^ { \lambda } = { \Gamma } _ { \mu \lambda , \nu } ^ { \lambda } - { \Gamma } _ { \mu \nu , \lambda } ^ { \lambda } + { \Gamma } _ { \mu \lambda } ^ { \rho } { \Gamma } _ { \nu \rho } ^ { \lambda } - { \Gamma } _ { \mu } ^ { \lambda } { \Gamma } _ { \lambda \rho } ^ { \rho }
$$

计算里契张量·得到的非零分量是

$$
\begin{array} { r l } & { R _ { \mathrm { o t } } = \mathrm { e } ^ { \nu - \mu } \bigg \{ - \frac { y ^ { \prime \prime } } { 2 } - \frac { y ^ { \prime } } { r } + \frac { y ^ { \prime } } { 4 } ( \mu ^ { \prime } - \nu ^ { \prime } ) \bigg \} , } \\ & { R _ { \mathrm { l i } } = \frac { y ^ { \prime \prime } } { 2 } - \frac { \mu ^ { \prime } } { r } + \frac { y ^ { \prime } } { 4 } ( \nu ^ { \prime } - \mu ^ { \prime } ) , } \\ & { R _ { z z } = \mathrm { e } ^ { - \mu } \bigg \{ 1 - \mathrm { e } ^ { \alpha } + \frac { r } { 2 } ( \nu ^ { \prime } - \mu ^ { \prime } ) \bigg \} , } \\ & { R _ { 3 z } = R _ { z z } \mathrm { s i n } ^ { 2 } \theta . } \end{array}
$$

这样真空场方程具体化为

$$
\begin{array} { l } { { \frac { \nu ^ { \prime \prime } } { 2 } + \frac { \nu ^ { \prime } } r - \frac { \nu ^ { \prime } } { 4 } ( \mu ^ { \prime } - \nu ^ { \prime } ) = 0 , } } \\ { { \frac { \nu ^ { \prime \prime } } { 2 } - \frac { \mu ^ { \prime } } r - \frac { \nu ^ { \prime } } { 4 } ( \mu ^ { \prime } - \nu ^ { \prime } ) = 0 , } } \end{array}
$$

$$
1 - \mathrm { e } ^ { \mu } + \frac { r } { 2 } ( \nu ^ { \prime } - \mu ^ { \prime } ) = 0 .
$$

它是 $\mu$ 和 $\pmb { \nu }$ 的联立微分方程组．这三个方程只有两个是独立的，那是因为爱因斯坦张量必满足毕安基恒等式(2.6.4)的后果.

这组方程很容易求解：将(5.2.9)式减去(5.2.10)式得出

$$
\mu ^ { \prime } + \nu ^ { \prime } = 0 ,
$$

由此解出

$$
\mu + \nu = \lambda , \quad \lambda = { \mathrm { c o n s t . } } .
$$

将(5.2.12)式代入(5.2.11)式消去 $\nu$ ，得

$$
1 - \mathrm { e } ^ { \mu } - r \mu ^ { \prime } = 0 ,
$$

即 $( r e ^ { - \mu } ) ^ { \prime } = 1$ ．它的解可写成

$$
\mathrm { e } ^ { - \mu } = 1 \displaystyle - \frac { 2 k } { r } , ~ k = \mathrm { c o n s t . } ~ .
$$

再利用(5.2.13)式得

$$
\mathbf { e } ^ { \nu } = \mathrm { e } ^ { \lambda - \mu . } = \mathrm { e } ^ { \lambda } \Big ( 1 - { \frac { 2 k } { r } } \Big ) .
$$

注意 ${ \pmb g } _ { 0 0 } = - { \pmb e } ^ { \nu }$ ，令 $\lambda = 0$ 相当于改变时间尺度，于是最后得解

$$
\begin{array} { l } { { \displaystyle g _ { 0 } \ d e = - \frac { } { } \mathrm { \bf e } ^ { \nu } = - \left( 1 - \frac { } { r } \frac { } { r } \right) , } } \\ { { \displaystyle g _ { 1 } \ d e = - \frac { } { } \mathrm { \bf e } ^ { \mu } = \Bigl ( 1 - \frac { } { r } \Bigr ) ^ { - 1 } . } } \end{array}
$$

回忆第三章 $\ S \ 3 . 4$ 中论证过的牛顿近似下

$$
g _ { \scriptscriptstyle 0 0 } = - \ 1 + \frac { 2 G M } { r } ,
$$

对比看出 $k { = } G M$ ，相应把不变距离公式写成

$$
\mathrm { d } s ^ { 2 } = - \mathrm { ~  ~ \left( ~ 1 ~ \right)} - \mathrm { ~ \frac { ~ 2 G M } { ~ r ~ } ~ }  \mathrm { d } t ^ { 2 } + \Bigl ( 1 - \frac { 2 G M } { r } \Bigr ) ^ { - 1 } \mathrm { d } r ^ { 2 }
$$

$$
+ \ r ^ { 2 } ( \mathrm { d } \theta ^ { 2 } + \sin ^ { 2 } \theta \mathrm { d } \varphi ^ { 2 } ) .
$$

它就是球对称外引力场的席瓦西尔解·

这引力场与牛顿引力场有一个很重要的共同点·球外引力场只取决于引力源的总质量，而与引力源的大小和物质密度随 $r$ 的分布无关，因此若只观测这种引力场，我们只能推知源的总质量，而不能获得关于源的其他信息·

# 5.3伯克霍夫(Birkhoff)定理

如果球对称的引力源不是静止而是在作径向运动，且在运动中保持球对称性，例如在收缩，膨胀或径向振荡，伯克霍夫定理说，它的外引力场仍可用席瓦西尔解描述：

按 $\$ 5.1$ 的分析，这情况下的度规场总可化成(5.1.13)的形式：其中两个未知函数

$$
\nu = \nu ( r , t ) , \quad \mu = \mu ( r , t )
$$

应由真空场方程 $R _ { \mu \nu } = 0$ 解出：

这情况与上节的区别在于现在 dv $\frac { \mathrm { d } { \nu } } { \mathrm { d } t }$ 和 $\frac { \mathrm { d } \mu } { \mathrm { d } t }$ 不为零：因此克里斯朵夫联络多出三个不为零的分量

$$
{ \cal I } _ { \scriptscriptstyle 0 \scriptscriptstyle 0 } ^ { \scriptscriptstyle 0 } = \frac { 1 } { 2 } \dot { r } , \quad { \cal T } _ { \scriptscriptstyle 1 \scriptscriptstyle 0 } ^ { \scriptscriptstyle 1 } = \frac { 1 } { 2 } \dot { \mu } , \quad { \cal T } _ { \scriptscriptstyle 1 \scriptscriptstyle 1 } ^ { \scriptscriptstyle 0 } = \frac { 1 } { 2 } \mathrm { e } ^ { \mu - \nu } \dot { \mu } ,
$$

其中 $\dot { \mu }$ 和 $\dot { r }$ 代表 $\mu$ 和 $r$ 对 $t$ 的微商．相应算出里契张量的分量$R _ { 2 2 }$ 和 $R _ { 3 3 }$ 不变，但 $R _ { \odot \odot }$ 和 $R _ { 1 1 }$ 添了附加的项：

$$
\begin{array} { r l } & { \displaystyle R _ { \mathfrak { o o } } = = \cdots + \frac { 1 } { 2 } \Big \vert \ddot { \mu } - \frac { 1 } { 2 } \dot { \mu } ^ { 2 } - \frac { 1 } { 2 } \dot { \mu } \dot { r } \Big \vert , } \\ & { \displaystyle R _ { 1 . } = \cdots - \frac { 1 } { 2 } \mathrm { e } ^ { \mu } \ddot { \textbf { \ i } } \ddot { \mu } + \frac { 1 } { 2 } \dot { \mu } ^ { 2 } - \frac { 1 } { 2 } \dot { \mu } \dot { r } \Big \vert , } \end{array}
$$

其中 $^ { \bullet \bullet } \bullet \bullet ^ { \bullet \bullet }$ 代表原有的项．此外，里契张量多了一个非零分量

$$
R _ { _ { ( ) , } } \mathrel { \mathop : } = - \mathrm { \small ~ \frac { 1 } { \gamma } ~ } \dot { \mu } .
$$

从场方程 $R _ { \odot } = 0$ 导出

$$
i = 0 ,
$$

它说明 $\mu$ 仍只是 $r$ 的函数：（5.3.5)式代回(5.3.2)和(5.3.3)式，$R _ { \mathfrak { d } }$ 和 $R _ { \mathrm { ~ l ~ l ~ } }$ 中的附加项全部消失，从而其余场方程回复到(5.2.9)至(5.2.11)式.

当同样由场方程解出(5.2.13)时，现在 $\lambda$ 可以是 $t$ 的任意函

数，

$$
\mu + \nu = \lambda ( t ) .
$$

再同样算下去，得到的解是

$$
\mathrm { e } ^ { - \hbar } = 1 - \frac { 2 k } { r } ,
$$

$$
\mathrm { e } ^ { \nu } = \mathrm { e } ^ { \lambda ( t ) } \Big ( 1 - { \frac { 2 k } { r } } \Big ) .
$$

这样不变距离公式写成

$$
\mathrm { d } s ^ { 2 } = \cdots \mathrm { e } ^ { \lambda \boldsymbol { ( t ) } } \bigl ( 1 - \frac { 2 k } { r } \bigr ) \mathrm { d } t ^ { 2 } + \Bigl ( 1 - \frac { 2 k } { r } \Bigr ) ^ { - 1 } \mathrm { d } r ^ { 2 }
$$

$$
+ r ^ { 2 } ( \mathrm { d } \theta ^ { 2 } + \sin ^ { 2 } \theta \mathrm { d } \varphi ^ { 2 } ) .
$$

这公式与席瓦西尔解的差别仅在第一项多了一个因子 $\mathbf { e } ^ { \lambda ( t ) }$ ．当对时间变量作--变换

$$
t  \widetilde { t } = \int \mathrm { e } ^ { \lambda ( t ) / 2 } \mathrm { d } t , \ -
$$

(5.3.9)式即回复到席瓦西尔解，这样就证明了伯克霍夫定理，

伯克霍夫定理的意义在于指明，席瓦西尔解描述的是球对称源的外引力场，但这源不必须是静止的·因此当观测到一个席瓦西尔引力场，我们无法判明它的源是一个稳定的恒星，还是-一个膨胀、收缩、振荡的恒星·

# 5.4 席瓦西尔坐标的物理意义

在广义相对论中，时空坐标只不过是事件点的数值对应，因此坐标值的大小一般并不具有更直接的几何意义或物理意义·但是对具体问题中按物理情况而适当选取的坐标系，却常常能对事件点的坐标值作出几何的或物理的解释，本节中我们讨论席瓦西尔解中所用的坐标 $( t \cdot r \cdot \theta \cdot \varphi )$ 的意义·

先看空间坐标与空间测量的关系．这里有两点值得注意．-是席瓦西尔度规中 $g _ { \cdot ) } = 0$ ，按(4.3.5)，有 $h _ { i j } = g _ { i j }$ ,因而相邻点的固

有距离 $\Delta L ,$ 是

$$
\Delta L ^ { 2 } = \Big ( 1 - \frac { 2 G M } { r } \Big | \mathrm {  ~ \nabla ~ } { \mathrm {  ~ d } } r ^ { 2 } + r ^ { 2 } { \mathrm {  { d } } } \theta ^ { 2 } + r ^ { 2 } { \sin } ^ { 2 } \theta { \mathrm { d } } \varphi ^ { 2 } .
$$

二是席瓦西尔度规与 $t$ 无关，所以积分性的有限测量是有意义的·

从(5.4.1)式首先看出，等 $_ r$ 面上的几何与三维欧氏空间中的球面几何是一样的·因此席瓦西尔角坐标 $\theta$ 与 $\varphi$ 仍具有通常的球面角坐标的意义，测量等 $_ r$ 面上任一大圆的周长 $s$ 将有

$$
s = 2 \pi r .
$$

测量等 $r$ 面的总面积 $A$ ，将得

$$
\ A = 4 \pi r ^ { 2 } .
$$

由此可把径向坐标 $r$ 的几何意义解释成等 $\boldsymbol { r }$ 面的面积除以 $4 \pi$ 再开根（或等 $_ r$ 面上大圆的周长除以 $2 \pi )$ ．从这意义上说， $r$ 可叫作等 $r$ 球面的有效半径，但是注意， $_ r$ 的大小完全不反映等 $_ r$ 面上任一点至坐标中心 $( r = 0 )$ 的固有距离，这有两方面原因．一方面从(5.4.1)式看到，径向相邻点的固有距离并不与径向坐标差成比例；或者说，比例系数与 $r$ 有关，另一方面，当 $r { < } 2 G M$ 时 $g _ { r r } < 0$ ，这时席瓦西尔坐标是非物理的，固有距离的概念失却了意义（参看第四章 $\ S \ 4 . \ 3 )$ ．因此如果把等 $_ r$ 面上任一点至坐标中心的固有距离理解成真实半径，在席瓦西尔场中这真实半径是没有意义的，回到上面的结论：坐标 $_ r$ 只代表有效半径·

然后讨论时间坐标与时间测量的关系．度规分量 $g _ { 0 i } = 0$ 表明席瓦西尔坐标时是全空间对准了的，意思是不同地点的同时事件是用同样的时间坐标标志的，在 $r { > } 2 G M$ 的区域内这坐标系是物理的，即可以有静观测者，静观测者用他携带的钟所测到的时间差 $\Delta T$ 与坐标时差 $\Delta t$ 的关系是（参看第四章 $\ S$ 4.3)

$$
\Delta T = \sqrt { 1 - \frac { 2 G M } { r } } \Delta t .
$$

因为坐标时 $t$ 对不同地点是对准了的，故(5.4.4)式说明不同地点时钟的快慢是不一样的，在 $r$ 小(须比 $2 G M$ 大)的地方引力越强，

时钟走得越慢，在无穷远处引力消失 $( g _ { \infty }$ 回到一1)，这情况下 $\Delta T$ $= \Delta t$ ，因此人们也说坐标时是无穷远处观测者的时钟所记录的时间：

# 5.5引力源中的内引力场

现在我们讨论球对称引力源内部引力场的分布问题，

设引力源是静止的理想流体．理想流体的能量动量张量有形式

$$
T ^ { \prime \prime } = ( \rlap { / } p + \rho ) U ^ { \prime \prime } U ^ { \prime } + \rlap { / } p g ^ { \prime \prime } ,
$$

其中 $\boldsymbol { \mathscr { P } }$ 是压强， $p$ 是能量密度， $U ^ { \mu }$ 是流体元的四维速度．对静止流体，四维速度是

$$
U ^ { \mu } = \frac { 1 } { \sqrt { - \ g _ { 0 0 } } } ( 1 , 0 , 0 , 0 ) ,
$$

因此相应混合形式的能量动量张量是

$$
T _ { \nu } ^ { \mu } : = \cdot \left( \begin{array} { c c c c } { { - \rho } } & { { 0 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { \rlap / { P } } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { \rlap / { P } } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { \rlap / { P } } } \end{array} \right) .
$$

内部引力场的场方程写作

$$
R _ { \nu } ^ { \mu } \ \cdot - \ \frac { 1 } { 2 } \delta _ { \nu } ^ { \mu } R = - \ 8 \pi G T _ { \nu } ^ { \mu } .
$$

利用 $\$ 5.2$ 中对里契张量的计算，我们得出场方程的分量式

$$
\mathrm { ~ e ~ } ^ { - \mu } \Big ( \frac { 1 } { r ^ { 2 } } \mathrm { ~ \ -- ~ } \frac { \mu ^ { \prime } } { r } \Big ) - \frac { 1 } { r ^ { 2 } } = - \mathrm { ~ 8 \pi } G \rho ,
$$

$$
\mathrm { e } \mathrm {  ~ \cdot ~ } \mu \left( \begin{array} { l } { { 1 } } \\ { { r ^ { 2 } } } \end{array} + \frac { \nu ^ { \prime } } { r } \right) - \frac { 1 } { r ^ { 2 } } = 8 \pi G \phi ,
$$

$$
\mathrm { ~ e ~ } ^ { \mu } \Big ( \frac { y ^ { \prime \prime } } { 2 } - \frac { \mu ^ { \prime } \nu ^ { \prime } } { 4 } + \frac { y ^ { \prime 2 } } { 4 } + \frac { \nu ^ { \prime } } { 2 r } - \frac { \mu ^ { \prime } } { 2 r } \Big ) = 8 \pi G \phi .
$$

能量动量张量的守恒律 $T _ { \nu ; \mu } ^ { \mu } { = } 0$ 给出

$$
\frac { \mathrm { d } \phi } { \mathrm { d } r } = - \ \frac { ( \phi + \rho ) } { 2 } \nu .
$$

毕安基恒等式决定了(5.5.5)至(5.5.8)式中只有三个独立的方程式：在这方程组中·决定引力场分布的 $\mu ( r )$ 和 $\nu ( r )$ 与决定引力源内物理参量分布的 $\rho ( r )$ 和 $p ( r )$ 是联立的，因此这组方程也就是恒星结构的方程．尤其是(5.5.8)式，它实质上是介质的静力平衡方程，至此这组方程并不完备·如果介质的物态方程有形式

$$
\rho = \rho ( \phi ) ,
$$

那么方程组就完备了·在恒星表面 $r = - R$ 处的边条件是 ${ \big . } _ { P } ( R ) =$ $0 , \mu ( R )$ 与 $\nu ( R )$ 与席瓦西尔外部解相衔接，即

$$
\mathrm { e } ^ { \mathrm { ~ \cdot ~ } \mu ( R ) } \mathrm { e } ^ { \mathrm { * } ( R ) } = 1 - \frac { 2 G M } { R } .
$$

现在我们讨论这方程组的求解问题．令

$$
m ( r ) = \frac { r } { 2 G } ( 1 - \epsilon ^ { - \mu } ) ,
$$

方程(5.5.5）可写成

$$
\operatorname* { l } _ { r \cdot } { \frac { \mathrm { d } m } { \mathrm { d } r } } = 4 \pi \rho .
$$

或

$$
m \left( r \right) = \int _ { 0 } ^ { r } 4 \pi r ^ { 2 } \theta \mathrm { d } r .
$$

$m \left( \tau \right)$ 的意义可解释为坐标为 $r$ 的球面内的质量：把(5.5.11)代入（5.5.6）式，得到

$$
\gamma ^ { \prime } = = \frac { 8 \pi G \rho r ^ { 3 } + 2 G m } { r ( r - 2 G m ) } .
$$

再代入(5.5.8)式，我们得出 ${ \boldsymbol { \mathit { p } } } ( { \boldsymbol { r } } )$ 的微分方程

$$
\frac { \mathrm { d } \phi } { \mathrm { d } r } = - \ \frac { ( \rho \ + \ p ) ( 4 \pi G \rho r ^ { 3 } \ + G m ) } { r ( r \ - \ 2 G m ) } .
$$

结合物态方程(5.5.9)，(5.5.15)就可用来求解恒星内部的结构，它是奥本海默(Oppenheimer)求解中子星结构时首次导出的，因此叫奥本海默方程．解出 $p ( r )$ 和 $\rho ( r )$ 后，通过积分(5.5.13)和

(5.5.14)式，就可得到引力场的分布：

对于较实际的物态方程，奥本海默方程都无法解析地积出·下面我们讨论一种能解析积出的理想模型：均匀密度介质构成的恒星，物态方程写作

$$
\rho = \rho _ { \mathrm { { \ell } } } = \mathrm { c o n s t . } .
$$

由(5.5.13)式积出

$$
m ( r ) = \frac { 4 \pi } { 3 } \rho _ { 0 } r ^ { 3 } , \ Y \not \equiv r \leqslant R .
$$

代入(5.5.15)式，奥本海默方程具有可分离变数的形式

$$
\frac { \mathrm { d } \phi } { \mathrm { d } r } = - \ \frac { 4 \pi ( \dot { r } r ^ { 3 } ( \rho _ { \vartheta } + \phi ) ( \rho _ { \vartheta } / 3 + \phi ) } { r ( r - 8 \pi G \rho _ { \vartheta } r ^ { 3 } / 3 ) } .
$$

这样就可以积出恒星内压力场的分布

$$
\begin{array} { r } { \phi ( r ) = \rho _ { \mathrm { 3 } } \bigg \{ \frac { \Big ( 1 - \frac { 2 G M r ^ { 2 } } { R ^ { 3 } } \Big | ^ { 1 / 2 } - \Big ( 1 - \frac { 2 G M } { R } \Big ) ^ { 1 / 2 } } { 3 \Big ( 1 - \frac { 2 G M } { R } \Big ) ^ { 1 / 2 } - \Big ( 1 - \frac { 2 G M r ^ { 2 } } { R ^ { 3 } } \Big ) ^ { 1 / 2 } } \bigg \} , } \end{array}
$$

其中 $M = 4 \pi \rho _ { \mathrm { 0 } } R ^ { 3 } / 3$ 是恒星总质量．把这结果代回(5.5.14)式，积出

$$
{ \mathrm { e } } ^ { r / 2 } { = } ~ \frac { 3 } { 2 } \Bigl ( 1 - \frac { 2 ( \dot { \iota } M } { \bar { R } } \Bigr ) ^ { 1 / 2 } - \frac { 1 } { 2 } \Bigl ( 1 - \frac { 2 G M r ^ { 2 } } { R ^ { 3 } } \Bigr ) ^ { 1 / 2 } ,
$$

把(5.5.17）代入(5.5.11）式，得到

$$
\mathrm { ~ e ~ } ^ { \cdot \mu } = \mathrm { ~ 1 ~ } - \frac { 2 G m } { r } \cdot = 1 - \frac { 2 G M r ^ { 2 } } { R ^ { 3 } } ,
$$

这样的内引力场也被称作席瓦西尔内部解·

有一些特征值得指出．恒星的内压力是向中心递增的，中心压强为

$$
\dot { p } _ { c } = \rho _ { 0 } \bigg \{ \frac { 1 - \Big ( 1 - \frac { 2 G M } { R } \Big ) ^ { 1 / 2 } } { 3 \Big ( 1 - \frac { 2 G M } { R } \Big ) ^ { 1 / 2 } - 1 } \bigg \} .
$$

由（5.5.22)式看出， $2 G M / R$ 随 $\pmb { \mathscr { P } } _ { c }$ 增大而增大．当 $\pmb { \phi } _ { c }$ 增至无穷，$2 G M / R$ 将增至 $8 / 9$ ．这极限情形下恒星的半径和总质量是

$$
R = ( 3 \pi G \rho _ { 0 } ) ~ ^ { - 1 / 2 } , ~ M = \frac { 4 } { 9 } ( 3 \pi G ^ { 3 } \rho _ { 0 } ) ^ { - 1 / 2 } .
$$

重要的是可以证明，其他物态方程下 $2 G M / R$ 的极限值都将小于8/9．回忆恒星表面时空偏离平坦的程度是由 $2 G M / R$ 标志的，因此这极限值代表了稳定恒星表面引力场强度的极限．这极限的存在纯粹是一种广义相对论效应，在牛顿理论中是没有这种极限的.

# 第六章 粒子在球对称场中的运动

因为有恒星这样现实的球对称引力场存在，所以粒子在这种场中的运动问题是有实际意义的问题.本章将在广义相对论基础上讨论质点在席瓦西尔场中的运动.它与牛顿理论的相应结果之间的差别是特别令人感兴趣的，因为它可用来检验广义相对论的正确性.

# 6.1时空对称性与守恒量

对称性与守恒量的关系的理论在物理学中有广泛的用途.这里我们将在广义相对论的框架下就质点动力学问题来讨论时空对称性与动力学守恒量的关系.它对求解质点的运动是很有帮助的.

在相对论动力学中，质点的逆变四维动量 ${ \phi } ^ { \mu }$ 定义为

$$
{ p ^ { \mu } } = m { \frac { \mathrm { d } { x ^ { \mu } } } { \mathrm { d } { \tau } } } ,
$$

其中 $_ { m }$ 是标量性的静质量.由逆变动量可派生地引入协变动量

$$
\ p _ { \mu } = g _ { \mu \nu } p ^ { \nu } .
$$

下面将看到这个量在动力学中更为重要.当质点在引力场中运动，它的动力学守恒量是由度规场的时空对称性决定的.我们首先可以证明，如果 $\xi ^ { \mu }$ 所生成的映射是等度规映射，则质点在这度规场中运动时 ${ p / } _ { \mu } \xi ^ { \mu }$ 是一个守恒量.

这证明是直截了当的.利用标量的普通微商与协变微商的一致性，以及乘积微商的分配律，我们有

$$
\frac { \mathrm { d } } { \mathrm { d } \tau } ( \phi _ { \mu } \hat { \pmb { \xi } } ^ { \mu } ) = \frac { \mathrm { d } } { \mathrm { d } \tau } ( \pounds \bar { \pmb { \xi } } _ { \mu } ) = ( \pounds ^ { \mu } \hat { \pmb { \xi } } _ { \mu } ) \lrcorner \pmb { \upsilon } ^ { \nu } = ( \pounds ^ { \mu } \hat { \pmb { \xi } } _ { \mu } ) \lrcorner \pmb { \upsilon } ^ { \nu }
$$

$$
\begin{array} { r } { = \ m ( u _ { : \nu } ^ { \prime \prime } u ^ { \prime } \xi _ { { \mu } } + \dot { \xi } _ { { \mu } ; \nu } u ^ { \prime \prime } u ^ { \nu } ) . } \end{array}
$$

由粒子在度规场中运动所满足的测地线方程知，上式右边第一项为零，

$$
u _ { \ast \nu } ^ { \mu } u ^ { \nu } = u _ { \ast \nu } ^ { \mu } u ^ { \nu } + { \cal { T } } _ { \alpha \nu } ^ { \mu } u ^ { \alpha } u ^ { \nu } = \frac { \mathrm { d } u ^ { \mu } } { \mathrm { d } \tau } + { \cal { T } } _ { \alpha } ^ { \mu } u ^ { \alpha } u ^ { \nu } = 0 .
$$

由 $\xi ^ { \mu }$ 所满足的凯林方程知，右边第二项也为零，

$$
\hat { \xi } _ { \mu , \nu } u ^ { \mu } u ^ { \nu } = \frac { 1 } { 2 } ( \xi _ { , \mu , \nu } + \xi _ { \nu , \mu } ) u ^ { \mu } u ^ { \nu } = 0 .
$$

于是证得 $\frac { \mathrm { d } } { \mathrm { d } \tau } ( \boldsymbol { p } _ { \mu } \boldsymbol { \hat { \varsigma } } ^ { \mu } ) = 0$ ，即 $\phi , \xi ^ { \mu }$ 是一个守恒量.

下面我们讨论一种常见形式的凯林矢量

$$
\xi ^ { \prime \prime } = \delta _ { \dot { \varepsilon } } ^ { \mu } ,
$$

其中 $k$ 取确定值.这凯林矢量所生成的无穷小映射是

$$
\tilde { x } ^ { \mu } = \left\{ \begin{array} { l l } { { x ^ { \mu } , } } & { { \mu \neq k ; } } \\ { { x ^ { \mu } + \varepsilon , } } & { { \mu = k . } } \end{array} \right.
$$

即映射对应点的坐标仅有 $x ^ { k }$ 改变了一个小量.这映射是等度规映射，说明度规场 $g _ { \mu \nu }$ 与 $x ^ { k }$ 无关.这情况下我们叫 $x ^ { k }$ 是度规场的循环坐标.当 $x ^ { \star }$ 是循环坐标，相应的运动质点的守恒量是

$$
{ p } _ { \varkappa } \xi ^ { \mu } \ \dots \ { p } _ { \varkappa } \delta _ { \ast } ^ { \mu } = \ { p } _ { k } .
$$

值得强调，守恒的是协变动量而不是逆变动量的对应分量.这结论在讨论质点动力学问题时很有用.

作为应用的例，看质点在席瓦西尔场中的运动.由于 $t$ 和 $\varphi$ 是席瓦西尔度规的循环坐标，所以运动质点的守恒量是 $\phi _ { \mu }$ 的 $t$ 和 $\varphi$ 分量，即

$$
\rho _ { 0 } = g _ { \circ } \rho ^ { \ast } = g _ { \circ 0 } \rho ^ { 0 } = { \textrm { \cdot } } \ m \Big ( 1 - \frac { 2 G M } { r } \Big | \frac { \mathrm { d } t } { \mathrm { d } \tau } = \mathrm { c o n s t . } \ .
$$

$$
\ p _ { 3 } = g _ { 3 \nu } \rlap         { / } p ^ { \prime } = g _ { 3 3 } \rlap { / } p ^ { \lambda } = m r ^ { 2 } \sin ^ { 2 } \theta \frac { \mathrm { d } \varphi } { \mathrm { d } \tau } = { \mathrm { c o n s t . } } ~ .
$$

# 6.2席瓦西尔场中的运动方程

现在我们要导出在席瓦西尔场中运动的质点所遵循的动力学微分方程.同牛顿力学中的有心运动一样，由于左右对称的缘故，质点必在初速度矢量(三维)与力心所构成的对称面上运动.我们取垂直轨道平面的方向为极轴，则质点的运动满足

$$
\ddot { \theta } = \frac { \pi } { 2 } , \qquad \frac { \mathrm { d } \theta } { \mathrm { d } \tau } = 0 .
$$

按上节的分析， $\pmb { \mathscr { P } } _ { 0 }$ 和 $p$ 是守恒量，它写成

$$
\mathrm { ~  ~ l ~ } - \mathrm { ~ \frac { 2 G M } { \mit ~ r ~ } ~ } \bigg | \frac { \mathrm { d } t } { \mathrm { d } \tau } = E ,
$$

$$
r ^ { 2 } \ : \frac { \mathrm { d } \varphi } { \mathrm { d } \tau } = L ,
$$

其中 $E$ 和 $L$ 是积分常量.此外，四维速度的归一条件 $g _ { \mu \nu } u ^ { \mu } u ^ { \nu } = - 1$ 也提供--个方程

$$
- \left( 1 - \frac { 2 G M } { r } \right) \left( \frac { \mathrm { d } t } { \mathrm { d } \tau } \right) ^ { 2 } + \left( 1 - \frac { 2 G M } { r } \right) ^ { - 1 } \left( \frac { \mathrm { d } r } { \mathrm { d } \tau } \right) ^ { 2 } + r ^ { 2 } \Big ( \frac { \mathrm { d } \varphi } { \mathrm { d } \tau } \Big ) ^ { 2 } = - 
$$

方程(6.2.1)至(6.2.4）是测地线方程的四个初积分，它们构成质点动力学的--组完备的微分方程组.

整理--下，这方程组可化成更简洁的形式：

$$
\frac { \mathrm { d } \varphi } { \mathrm { d } \tau } = \frac { L } { r ^ { 2 } } ,
$$

$$
\frac { \mathrm { d } t } { \mathrm { d } \tau } = - \ \underbrace { E } _ { 1 \ - \ \frac { 2 G M } { r } } ,
$$

$$
\left( { \frac { \mathrm { d } r } { \mathrm { d } \tau } } \right) ^ { 2 } = E ^ { ? } - \left( 1 - { \frac { 2 ( j M } { r } } \right) \left( 1 + { \frac { L ^ { 2 } } { r ^ { 2 } } } \right) .
$$

它将是后面各节中讨论的出发点.

在应用之前，我们先看一下积分常数 $E$ 和 $L$ 的物理意义.为

此计算观测者所测到的质点的能量和角动量.在坐标的赤道面 $( \theta$ $= \pi / 2 )$ 上静止的观测者的四维速度是

$$
u ^ { \mu } = \left( \frac { 1 } { \left( 1 - \frac { 2 G M } { r } \right) ^ { 1 / 2 } } , 0 , 0 , 0 \right) .
$$

他的四轴系类空基矢取作

$$
\omega _ { \hat { a } } ^ { \prime } = \frac { 1 } { \sqrt { g _ { u u } } } \delta _ { a } ^ { \mu } , \quad \vec { \mathrm { { A f } } } \circ \vec { \mathrm { { A } } } \vec { \mathrm { { A } } } \vec { \mathrm { { A } } } \vec { \mathrm { { F H } } } .
$$

这些观测者测得的质点的能量是 $\boldsymbol { \phi } ^ { \stackrel { \wedge } { \alpha } }$ 的0分量，

$$
{ \hat { \boldsymbol { p } } } ^ { \hat { \mathcal { 0 } } } = \phi _ { \mu } \omega ^ { \hat { \boldsymbol { \theta } } _ { \mu } } = - \mathbf { \nabla } \phi _ { \mu } \boldsymbol { u } ^ { \mu } = - \mathbf { \nabla } \phi _ { 0 } \boldsymbol { u } ^ { \intercal } = { \frac { m E } { \left( 1 - { \frac { 2 G M } { r } } \right) ^ { 1 / 2 } } } .
$$

(6.2.10)式表明实测的质点能量 $\phi ^ { \overset { \land } { \partial } }$ 并不守恒，它与质点所在地的$\sqrt { - g _ { 0 0 } }$ 成反比.这叫质点能量的引力红移(可对比本章 $\ S \ 6 . 6$ 中对光子频率红移的讨论).在无穷远处 $\sqrt { - g _ { \theta 0 } } = 1$ ，于是可以说 $E$ 是无穷远处测到的单位质量质点的能量.这种说法对束缚态质点（见下节)不具有明确的含义，因为那种情况下质点不会达到无穷远处.一般说， $E$ 所反映的是单位质量质点的能量与 $\sqrt { - g _ { \mathfrak { o o } } }$ 的乘积.

这些观测者测得的质点的横向 $( \varphi$ 方向)动量是 $p ^ { \frac { \lambda } { \alpha } }$ 的3分量，

$$
\begin{array} { r } { \boldsymbol { \dot { \ p } } ^ { \hat { 3 } } = \boldsymbol { \dot { p } } _ { \ast } \omega ^ { \hat { 3 } \mu } = \boldsymbol { \dot { p } } _ { \ast } \omega _ { \hat { 3 } } ^ { \mu } = \boldsymbol { \dot { p } } _ { 3 } \omega _ { \hat { 3 } } ^ { 3 } = m L / r . } \end{array}
$$

$r { \phi } ^ { \uparrow }$ 可叫作质点的等效角动量.冠以“等效”二字，因为 $\boldsymbol { r }$ 不是质点与力心的真实距离而只是有效距离.在这意义上， $L$ 是单位质量质点的等效角动量.

# 6.3运动的分类

这一节我们讨论质点在席瓦西尔场中的运动情况的分类.在讨论相对论之前，先简单回顾一下牛顿力学中与它相对应的分类.

对同一问题，采用同样的坐标，牛顿动力学方程的初积分是

$$
{ \frac { \mathrm { d } \varphi } { \mathrm { d } t } } = { \frac { L } { r ^ { 2 } } } ,
$$

$$
\frac { 1 } { 2 } \bigg \{ \frac { \mathrm { d } r } { \mathrm { d } t } \bigg \} ^ { 2 } = E + \frac { G M } { r } - \frac { L ^ { 2 } } { 2 r ^ { 2 } } ,
$$

其中 $L$ 和 $E$ 是积分常量，分别代表单位质量的角动量和能量.满足这方程组的运动可分为两大类.一类是按椭圆形轨道运动的束缚态，它对应于 $E < 0$ 的情形.另一类是按双曲线或抛物线轨道运动的散射态，它对应于 $E = 0$ 的情形.特例是 $L = 0$ 的情形.这时质点既不是束缚态也不是散射态，它将向力心吸收.我们把这情形叫吸收态.

这种分类定性地可以从(6.3.2)式直观地看出.为此引入径向运动的等效势

$$
V = - \ \frac { G M } { r } + \frac { L ^ { 2 } } { 2 r ^ { 2 } } ,
$$

它是牛顿引力势和离心势的叠加.这等效势的函数图象如图6.1所示.利用等效势，径向动力学方程可重新写成

$$
\frac { 1 } { 2 } \Big \{ \frac { \mathrm { d } r } { \mathrm { d } t } \Big \} ^ { 2 } = E - V ( r ) .
$$

因等式左边不能为负数，可能的运动只发生在 $E { \geqslant } V \left( r \right)$ 的范围内.看 $I { \mathcal { A } } 0$ .当 $E < 0$ ，由 $V ( r )$ 曲线形状看出，可能的 $_ { r }$ 有最大值和最小值，它可由 $E = = V \left( r \right)$ 解出.这表明它的运动是束缚态.当 $E {  }$ 0，曲线形状表明 $_ r$ 可延伸至无穷远，但它必有最小值.这就是散射态.在 $\cal { L } = 0$ 时由于没有离心势，中心排斥力消失了.等效势的形状有了根本的不同.从图6.1看出，不管 $E$ 多大，只要向力心运

![](images/c1401340e75b6c9953d2c952f29f7a6ee95c17be43219af752e302ead23741be.jpg)  
图6.1牛顿的等效势

动，它必定坠落到 $r = = 0$

现在我们转入讨论相对论性的运动的分类，它完全可按对应的径向方程(6.2.7)类似地作出.为此我们引入相对论性的等效势

$$
U ^ { \prime 2 } = \Big ( 1 - \frac { 2 G M } { r } \Big ) \Big ( 1 + \frac { L ^ { 2 } } { r ^ { 2 } } \Big ) .
$$

这样径向方程可重写作

$$
\left( \frac { \mathrm { d } r } { \mathrm { d } \tau } \right) ^ { 2 } = E ^ { 2 } - U ^ { 2 } .
$$

同样，可能的运动只发生在 $E ^ { 2 } { \geqslant } U ^ { \gamma 2 }$ 的范围内.

把等效势展开

$$
U ^ { \prime 2 } = 1 \ - \ \frac { 2 G M } { r } + \frac { L ^ { 2 } } { r ^ { 2 } } - \frac { 2 G M L ^ { 2 } } { r ^ { 3 } } ,
$$

看出它比牛顿等效势多了两项.多出的常数1不是实质性的.因相对论性的能量包括静止能，所以无穷远处静止质点的 $E$ 是1，而不像非相对论情况下它是零.实质的差别在于增加了一项

$- 2 G M L ^ { 2 } / r ^ { 3 }$ .它的负幂次最高，所以在 $_ r$ 较大时它不起显著作用，牛顿力学构成好的近似；在 $_ r$ 很小时它起决定作用，等效势由于这个新的吸引心而根本改变了形状.

为分析的方便，我们以 $G M$ 为 $_ r$ 的单位，把等效势用无量纲量表述

$$
U ^ { : } = 1 - \frac { 2 } { r } + \frac { \tilde { { \cal { L } } } ^ { 2 } } { r ^ { 2 } } - \frac { 2 \tilde { { \cal { L } } } ^ { 2 } } { r ^ { 3 } } ,
$$

其中 $\stackrel { \sim } { L } = I _ { \iota } / G M$ ，即以 $\cal G M$ 为单位时的 ${ \cal L } . { \cal U } ^ { 2 } ( r )$ 的形状只依赖单一参量 $\tilde { L }$ 参量取各种值时的等效势如图6.2所示.

从图线看出，当 $\tilde { L } > 4$ ，在 $_ r$ 很小的地方有一个峰值大于1的势垒，此外在 $r$ 较大的地方仍有一势阱.这就把可能的运动分成了三类：

$$
\begin{array} { r l r l } & { E ^ { 2 } < 1 , } & & { \mathrm { ~ \gamma ~ } ^ { * } \overset { \cdot \in } { \mathbb { R } } ^ { 2 } \overset { \cdot \llcorner } { \mathbb { R } } ; } \\ & { 1 \leqslant E ^ { 2 } < { \cal U } _ { \mathrm { m a x } } ^ { 2 } , } & & { \frac { \pm \mu } { \Theta } \overset { \cdot \oplus } { \mathbb { H } } \overset { \ll } { \underset { \mathrm { i c } } { \mathbb { H } } } ; } \\ & { E ^ { 2 } \geqslant { \cal U } _ { \mathrm { m a x } } ^ { 2 } , } & & { \mathfrak { U Z } _ { \mathrm { m a x } } ^ { 2 } . } \end{array}
$$

随 $\smash { \widetilde { L } }$ 的减小,中心势垒降低它的高度.在 $2 \sqrt { 3 } \leqslant \tilde { L } \leqslant 4$ 的范围内${ U _ { \mathrm { m a x } } ^ { 2 } } { \leqslant } 1$ (参看图6.2).这情况下出现散射态的可能消失了，只有束缚态和吸收态.若 $\check { L } { < } 2 \checkmark 3$ ,等效势的峰与谷都消失,这时唯一的可能是被力心吸收.这就是相对论性球对称场中运动的分类.注意，上述分析基于一个假定，即引力源的几何半径充分小，以至席瓦西尔外部界对很小的 $_ r$ 仍能适用.

相对论性的结果与牛顿结果的重要不同之一是场中运动质点被引力源吸收的可能增加了.按牛顿理论，运动质点的角动量必须充分小，即运动方向几乎是准确地指向引力源，它才可能落到引力源上去.否则它在越过双曲线的近心点后将重新向远处飞去而构成散射态.按相对论性的分析我们看到，即使 $L$ 很大，只要 $E$ 充分大，质点就会绕力心回旋多次后坠落.这一点对讨论致密天体对空

![](images/12b41742c7850f4c3f7df186081c12947461e4f2a103611107a36de467f0c966.jpg)  
图6.2相对论性等效势

间粒子的吸积问题是一个重要的观念.

还有一个重要的不同点.按牛顿理论，可以实现半径任意小的圆轨道，即结合能任意大的束缚态.从相对论的等效势看出，最小的圆轨道半径是6GM,它是由

$$
\frac { \mathrm { d } ( U ^ { 2 } ) } { \mathrm { d } r } = 0 \hbar \frac { \mathrm { d } ^ { 2 } ( U ^ { 2 } ) } { \mathrm { d } r ^ { 2 } } = 0
$$

算出的.束缚态中单位静质量质点的结合能定义为 $1 - E .$ 容易算出最小圆轨道中这结合能的大小是0.057.这意味着原来在远处静止的质点在逐步丢失能量而过渡到这束缚态的过程中，它的静止能的 $5 . 7 \%$ 将被释放出来.回忆核反应的能量释放率仅为$0 . 7 \%$ ，这是一个极强有力的能量释放机制.人们猜想类星体的巨大的辐射功率很可能与这种能量释放机制有关.

# 6.4行星的轨道

为了便于对比,同样先回顾一下牛顿的行星轨道理论.

利用(6.3.1)式,把(6.3.2)式化为 $_ r$ 对 $\varphi$ 的微分方程，它是

$$
\frac { 1 } { 2 } \Bigl [ \frac { \mathrm { d } } { \mathrm { d } \varphi } \Bigl ( \frac { 1 } { r } \Bigr ) \Bigr ] ^ { 2 } = \frac { E } { L ^ { 2 } } + \frac { G M } { r L ^ { 2 } } - \frac { 1 } { 2 r ^ { 2 } } .
$$

为下面讨论方便,把它化为二阶微分方程.把(6.4.1)两边对 $\varphi$ 求微商，得到

$$
\frac { { \mathrm { d } } ^ { 2 } } { { \mathrm { d } } \varphi ^ { 2 } } \Big ( \frac { 1 } { r } \Big ) + \frac { 1 } { r } = \frac { G M } { L ^ { 2 } } ,
$$

这是轨道的微分方程，在牛顿力学中叫比内(Binet)公式.为了使量值大小有清楚的意义，我们把变量和参量无量纲化，定义

$$
{ \mathrm { } } u = { \frac { G M } { r } } .
$$

比内公式重写成

$$
\frac { \mathrm { d } ^ { 2 } u } { \mathrm { d } \varphi ^ { 2 } } + u = \bigg ( \frac { G M } { L } \bigg ) ^ { 2 } ,
$$

这里每一-项都是无量纲的.这方程的解是

$$
u = \bigg ( \frac { G M } { L } \bigg ) ^ { 2 } ( 1 + e \mathrm { c o s } \varphi ) .
$$

对行星讲，偏心率 $e$ 是小于1的,相应的轨道是一个椭圆.

相对论性的动力学方程可作类似的处理.利用(6.2.5)把（6.2.7)式化为 $_ r$ 对 $\varphi$ 的微分方程，

$$
\frac { 1 } { 2 } \Bigl [ \frac { \mathrm { d } } { \mathrm { d } \varphi } \Bigl ( \frac { 1 } { r } \Bigr ) \Bigr ] ^ { 2 } = \frac { E ^ { 2 } - 1 } { 2 L ^ { 2 } } + \frac { G M } { r L ^ { 2 } } - \frac { 1 } { 2 r ^ { 2 } } + \frac { G M } { r ^ { 3 } } .
$$

同样两边对 $\varphi$ 求微商，得出比内公式的相对论推广

$$
\frac { \mathrm { d } ^ { 2 } } { \mathrm { d } \varphi ^ { 2 } } \Big ( \frac { 1 } { r } \Big ) + \frac { 1 } { r } = \frac { G M } { L ^ { 2 } } + \frac { 3 G M } { r ^ { 2 } } .
$$

再同样按(6.4.3)式引用无量纲变量 $\pmb { u }$ ，方程化为

$$
\frac { \mathrm { d } ^ { 2 } u } { \mathrm { d } \varphi ^ { 2 } } + u = \bigg ( \frac { G M } { L } \bigg ) ^ { 2 } + 3 u ^ { 2 } .
$$

把它与非相对论公式(6.4.4)比较，(6.4.8)中仅多了一项 $3 u ^ { 2 }$

我们用实际的行星估算一下各项的量级.对太阳，有

$$
\mathit { G M } = 1 . 5 \times 1 0 ^ { 3 } \mathrm { \ m } .
$$

太阳系中水星的轨道半径最小(即 ${ \pmb u }$ 最大),它的值为

$$
r = 5 \times 1 0 ^ { 1 0 } \ \mathrm { m } .
$$

相应看出无量纲变量 $u$ 是量级为 $1 0 ^ { - 7 }$ 的小量.由（6.4.5）知，$( G M / L ) ^ { 2 }$ 也具有同样的量级.然后看相对论的轨道微分方程(6.4.8).其中 $\pmb { u }$ 与 $( G M / L ) ^ { 2 }$ 的量级对水星已估出为 $1 0 ^ { - 7 }$ ,相对论修正项 $3 \boldsymbol { u } ^ { 2 }$ 具有 $1 0 ^ { - 1 4 }$ 的量级，它是一个很小的修正.因为对其他行星，这个修正项将更小，所以我们先来计算相对论效应对水星轨道的影响.

考虑到牛顿解(6.4.5)可以作为相对论性方程(6.4.8)的零级近似，我们把它代入修正项，以使非线性微分方程变为线性非齐次方程，

$$
\begin{array} { c } { { { \displaystyle { \frac { \mathrm { d } ^ { 2 } u } { \mathrm { d } \varphi ^ { 2 } } } + u = ( { \frac { G M { \mathrm { \Omega } } ^ { \prime } } { L } } ^ { 2 } + 3 \Big ( { \frac { G M } { L } } \Big ) ^ { 4 } ( 1 + e { \cos } \varphi ) ^ { 2 } \qquad } } } \\ { { { \approx \Big ( { \frac { G M { \mathrm { \Omega } } _ { \ast } } { L } } ^ { 2 } + 3 { \frac { G M } { L } } \Big ) ^ { 4 } + 6 \Big ( { \frac { G M } { L } } \Big ) ^ { 4 } e { \cos } \varphi . ~ ( \mathrm { d } } } } \end{array}
$$

这里利用了水星轨道的 $e \ll 1$ 的事实，即它很接近于圆形.式中常数 $3 ( G M / L ) ^ { \dagger }$ 是对 $( G M / L ) ^ { 2 }$ 的小修正，它将微小地改变椭圆长轴的长度.我们对这个改变不感兴趣，因为它不可能被测得非常准确.略去这项后方程变成

$$
\frac { \mathrm { d } ^ { 2 } u } { \mathrm { d } \varphi ^ { 2 } } + u \ \cdot = \ \bigg ( \frac { G M } { L } \bigg ) ^ { 2 } + 6 \bigg ( \frac { G M } { L } \bigg ) ^ { 4 } e \mathrm { c o s } \varphi .
$$

作为线性方程，我们把它分两部分来解.令

$$
u = u _ { 1 } + u _ { 2 } .
$$

其中 $\pmb { u } _ { 1 }$ 满足

$$
\frac { \mathrm { d } ^ { 2 } u _ { 1 } } { \mathrm { d } \varphi ^ { 2 } } + u _ { 1 } = \Bigl ( \frac { G M } { L } \Bigr ) ^ { 2 } ,
$$

${ \pmb u } _ { 2 }$ 满足

$$
\frac { \mathrm { d } ^ { 2 } u _ { 2 } } { \mathrm { d } \varphi ^ { 2 } } + u _ { 2 } = 6 \bigg ( \frac { G M } { L } \bigg ) ^ { 4 } e \mathrm { c o s } \varphi ,
$$

(6.4.11)式有通解

$$
u _ { 1 } = \bigg ( \frac { G M } { L } \bigg ) ^ { 2 } ( 1 + { e } { \cos } \varphi ) ,
$$

(6.4.12)式有特解

$$
u _ { 2 } = 3 \bigg \{ \frac { G M } { L } \bigg \} ^ { 4 } e \varphi \mathrm { s i n } \varphi .
$$

于是得出方程(6.4.10)的通解为

$$
u = u _ { 1 } + u _ { 2 } = \bigg ( \frac { G M } { L } \bigg | ^ { 2 } \bigg ( 1 + e \mathrm { c o s } \varphi + 3 \Big ( \frac { G M } { L } \Big ) ^ { 2 } e \varphi \mathrm { s i n } \varphi \bigg )
$$

$$
\approx \Bigl ( \frac { G M } { L } \Bigr ) ^ { 2 } \Bigl \{ 1 + e \cos \Bigl \{ 1 - 3 \Bigl ( \frac { G M } { L } \Bigr ) ^ { 2 } \Bigr ] \varphi \Bigr \} .
$$

这里最后的等式须忽略 $( G M / L ) ^ { 6 }$ 以上的小量、

相对论修正后的水星轨道(6.4.13)与牛顿轨道(6.4.5)的差别在于轨道近日点与远日点有进动发生.近日点的标志是

$$
\Big [ 1 - 3 \Big ( \frac { G M } { L } \Big ) ^ { 2 } \Big ] \varphi = 2 n \pi , \quad n = 0 , 1 , 2 , \cdots ,
$$

即

$$
\varphi = { \cfrac { 2 n \pi } { 1 - 3 { \Big ( } { \cfrac { G M } { L } } { \Big ) } ^ { 2 } } } \approx 2 n \pi { \Big [ } 1 + 3 { \Big ( } { \frac { G M } { L } } { \Big ) } ^ { 2 } { \Big ] } .
$$

两个相邻的近日点方位角之差是

$$
\Delta \varphi = 6 \pi \Big ( \frac { G M } { L } \Big ) ^ { 2 } .
$$

代入水星的观测数据，得到 $\Delta \varphi { = } 0 . 1 { ^ \prime } ^ { \prime } .$ ，这是一个很小的数字，但它是会长期积累的.水星公转周期是0.24a(a 为年的符号)，因此每一世纪积累的近日点偏转角是 $4 3 "$

观测表明水星近日点的偏转角为每世纪 $5 6 0 0 . 7 3 \pm 0 . 4 1 ^ { \prime \prime }$ 由牛顿理论算出其他行星的摄动导致的偏转角为 $5 5 5 7 . 6 2 { \pm } 0 . 2 0 { ^ { \prime \prime } } $ 其差值 $4 3 . 1 1 \pm 0 . 4 5 ^ { \prime \prime }$ 与广义相对论预言值的符合是惊人的.但对于是否还有其他重要因素在引起附加进动的问题，至今仍有争议.讨论得很多的是太阳扁率的影响.本世纪初观测使人们相信太阳扁率不致在这里产生显著影响.60年代迪克(Dicke)等人定出扁率为 $( 5 . ~ 0 { \pm } 0 . ~ 7 ) \times 1 0 ^ { - 5 }$ .它就可能引起每世纪3.4"的附加进动.由于这种争议夹杂了许多不确定因素，因此很难有明确的结论.无论如何，水星近日点进动问题是对广义相对论的巨大支持，这是可以肯定的.

# $\ S 6 . 5$ 光子轨线的引力偏折

在讨论等效原理时我们已指出，在牛顿理论中质点的加速度$a = F / m$ ，而引力 $F$ 正比于 $_ { \pmb { \mathscr { M } } }$ ，所以质点的加速度与它的固有属性无关，仅取决于引力场.这样会引出一个有趣的问题.光子作为零静质量粒子，它在引力场中是否也会有同样的加速度，从而引起轨道的偏折？在实践上，光子速度很大，这一点偏折很难测到，因而没有明确的回答.在理论上，肯定与否定的回答都不至于与牛顿理论的框架相冲突，从而也没有结论.在广义相对论中情况却不同.由等效原理可以论证，光子的轨线必然有引力偏折.

先看一个理论上的原因.牛顿力学中认为质量是质点的固有属性(即与它的运动无关）.它反映惯性（即不易被加速的程度）.在狭义相对论中质量的概念变复杂了.从相对论动力学看，动质量$m = E ,$ 反映质点不易被加速的程度，即惯性；但它与速度有关，即不是质点的固有属性.静质量是标量，它是质点的固有属性；但不代表惯性.弱等效原理认为引力质量与惯性质量相等，这惯性质量应指质点的动质量.光子是以静质量等于零为特征的，但它的动质量不为零.按普朗克公式， $m = E = h \nu , \nu$ 是光子的频率.于是等效原理对光子作出了推论：光子应具有引力质量，即光子能产生引力场，也必会受其他物体的引力场的作用.

此外还可有一个很直观的论证.设想一“静止"升降机中的观测者看到外面射进来的光线是直线行进的（图6.3）.当此升降机加速向上运动，他将发现光线沿向下弯曲的曲线行进.按广义相对论前的物理学，这光线的弯曲归之于参考系的加速性，即惯性力.如接受了等效原理，它就只能被认为是引力的效果.

现在我们讨论光子在引力场中的运动.它与前面讨论质点的运动有些不同.光子的运动是由 $\mathtt { d } s \equiv 0$ 刻画的，因此 $s$ 不能用作光子世界线上的仿射参量.与此有关的是光子静质量为零，于是四维动量的定义式(6.1.1)对它不适用.我们可以任选一标量性的仿射参量 $\lambda$ ，把光子四维动量定义为

![](images/8b998fa99f877aad65851a332363bbbcf18db64552381972237420fd6a6ef9bd.jpg)  
图6.3加速升降机中的光线

$$
{ \boldsymbol { \rho } } ^ { \prime } { } ^ { \prime } = { \frac { \operatorname { d } { \boldsymbol { x } } ^ { \prime } } { \operatorname { d } \lambda } } ,
$$

当光子在席瓦西尔场中沿测地线运动，仍有 $\phi _ { \mathrm { 0 } }$ 和 $\pmb { \mathscr { P } } 3$ 守恒，写作

$$
r ^ { 2 } \ { \frac { \mathrm { d } \varphi } { \mathrm { d } \lambda } } = L .
$$

$$
\left\{ \begin{array} { l l } { \mathbf { 1 } } &  - \displaystyle \frac { 2 G M } { r } \right\} \frac { \mathrm { d } t } { \mathrm { d } \lambda } = E . \end{array}
$$

现在由 $g _ { \mu \nu } \not p ^ { \mu } \not p ^ { \nu } = = 0$ 给出第三个初积分，它可化成

$$
\Big | \frac { \mathrm { d } r } { \mathrm { d } \lambda } \Big | ^ { 2 } = : E ^ { 2 } - \frac { L ^ { 2 } } { r ^ { 2 } } \Big ( 1 - \frac { 2 G M } { r } \Big ) .
$$

(6.5.2)至（6.5.4）式是光子的动力学方程组.由（6:5.2）和(6.5.4)式消去参量 $\lambda$ ，得到光子的轨道方程

$$
\Big ( { \frac { 1 } { r ^ { 2 } } } { \frac { \mathrm { d } r } { \mathrm { d } \varphi } } \Big ) ^ { 2 } = \Big ( { \frac { E } { L } } \Big ) ^ { 2 } - { \frac { 1 } { r ^ { 2 } } } \Big ( 1 - { \frac { 2 G M } { r } } \Big ) ,
$$

它依赖于一个参量 $E / I$ 令

$$
 / = \frac { L } { E } ,
$$

在远处 $E$ 是线动量大小, $L$ 是角动量大小；所以 $^ { b }$ 代表等效的瞄准距离·或叫碰撞参量.

为讨论光子运动的分类·我们定义光子的等效势 $B ^ { 2 } ( r )$ ，

$$
B ^ { 2 } ( r ) = \frac { r ^ { 2 } } { 1 - 2 G M / r } .
$$

这样光子轨道方程(6.5.5)改写成

$$
\left( \begin{array} { l } { { { \underline { { { 1 } } } } } } \\ { { r ^ { 2 } } } \end{array} \right) { \underline { { { \mathrm { d } } } } } \underline { { { r } } } . \quad = \displaystyle \frac { 1 } { b ^ { 2 } } - \frac { 1 } { B ^ { 2 } ( r ) } .
$$

$B ^ { \cdot } \ ^ { 2 } ( r )$ 的函数图象由图6.4所示. $B ^ { \cdot \cdot } \mathcal { Y } _ { r } )$ 在 $r = 3 G M$ 处有-峰，峰高为 $\mathrm { ~ ( ~ 2 7 } M ^ { 2 } \mathrm { ~ ) ~ } \mathrm { ~ } \mathrm { ~ } ;$ .光子的可能运动必须满足条件

$$
6 i \backslash \leqslant B ^ { 2 } ( r ) .
$$

由图线可看出，当光子以 $b { \overset {  } { \to } } { \overset { \cdot } { \to } } { \overset { \prime } { \sqrt { 3 } } } G M$ 入射，它最终必将被散射回无穷远处.当以 $\smash { I _ { 2 } < - 3 \sqrt { 3 } G _ { 2 } 1 1 }$ 入射，它将回旋地落入力心.

![](images/20d2d0e0b26393aeed8da485a0bc1424afdf0674fb0fba4afdad99634000a0f7.jpg)  
图6.：光子的等效势

要使光线被引力场强烈地偏转，引力源的几何半径必须是3GM 的量级.我们知道，除中子星外，其他类型的已知恒星的半径

都比它大很多量级.在这种情况下，光线只会受引力的影响而发生微小的偏折.作为可观测的例子，我们讨论太阳引力对擦过它表面的星光的偏折(图6.5).

同样引入无量纲变量 $\pmb { u } = G M / r$ 代替 $r$ ，我们把光子轨道方程(6.5.5）化成

$$
\frac { \mathrm { d } ^ { 2 } u } { \mathrm { d } \varphi ^ { 2 } } + u = 3 u ^ { 2 } .
$$

因为太阳半径远大于 $G M , u$ 永远是小量，所以又可以采用逐次逼近的方法求解.先略去二级小量 $3 \boldsymbol { u } ^ { 2 }$ ，解出零级近似

$$
u = u _ { 0 } { \cos } \varphi .
$$

它是--条垂直极轴的直线.然后把零级近似代入(6.5.8)式的右边，来计算二级小项引起光线的偏折.代入后的方程变为

$$
\begin{array} { l } { \mathrm { d } ^ { \div } u } \\ { \mathrm { d } \varphi ^ { \mathrm { i } } } \end{array} - u = 3 u ^ { \mathrm { 2 } } \mathrm { c o s } ^ { \mathrm { 2 } } \varphi .
$$

这方程有一特解

$$
u = u _ { \scriptscriptstyle ( ) } ^ { \scriptscriptstyle 2 } ( 1 + \sin ^ { 2 } \varphi ) .
$$

由此易得知偏折光线的·级近似解为

$$
\begin{array} { r } { u = u \cos \varphi + u \sp 2 _ { 0 } ( 1 + \sin \varphi ) . } \end{array}
$$

零级解(6.5.9)在远处 $( \imath ( = 0 )$ 的方位角是 $\pm \pi / 2$ 一级解（6.5.12）在远处的方位角是士 $( \pi / 2 + \alpha )$ ,其中 $\alpha$ 是小量，它满足

$$
- \ u _ { 0 } s \mathfrak { m } \alpha + u _ { 0 } ^ { 2 } ( 1 \ + \cos ^ { 2 } \alpha ) = 0 .
$$

对 $\sin \alpha$ 和 $\cos \alpha$ 作泰勒展开后保留主项，则可解出

$$
\ d { \ L } _ { \alpha } = \ 2 \ d { u } _ { \ L } = \frac { 2 G M } { R } ,
$$

其中 $R$ 是太阳半径.于是最终得出光线的偏折角

$$
\Delta \theta = 2 \alpha = { \frac { 4 G M } { R } } ,
$$

代入太阳的数据，算出 $\Delta \theta = 1 . 7 5 ^ { \prime \prime }$

我们也计算-一下牛顿理论下的结果.把牛顿动力学用于光子，轨道方程仍为(6.4.2).注意光子在远处不受引力时速度 $\tau = 1$ ，所

![](images/56c2448db991190cafc5b7b231fe6de8657c6825cb8c151d199a674b7aa4b3ad.jpg)  
图6.5星光的偏折

以有 $L = R v { = } R$ 方程(6.4.2)用变量 $\pmb { u }$ 写成

$$
1
$$

$$
\frac { \mathrm { d } ^ { 2 } u } { \mathrm { d } \varphi ^ { 2 } } + u = u _ { 0 } ^ { 2 } .
$$

忽略 $u _ { 0 } ^ { 2 }$ 后的解仍是直线(6.5.9).考虑 $\pmb { u } _ { \mathrm { 0 } } ^ { 2 }$ 引起的修正后的解是

$$
\begin{array} { r } { \pmb { \mathscr { u } } = \pmb { \mathscr { u } } _ { 0 } \mathrm { c o s } \varphi + \pmb { \mathscr { u } } _ { 0 } ^ { 2 } . } \end{array}
$$

仍令入射和出射光线的方位角为 $= ( \frac { \pi } { 2 } + \alpha )$ ，则有

$$
\sin \alpha = \alpha = u _ { 0 } = { \frac { G M } { R } } .
$$

即偏折角 $\Delta \theta$ 是相对论预言值的一半，即 $0 . 8 7 5 ^ { \prime \prime }$ ·

在1919年5月发生的日全蚀时，两个观测队第一次实测了通过太阳表面的星光的偏折.所得结果是 $\Delta \theta = ( 1 . 9 8 \pm 0 . 1 2 ) ^ { n }$ 和$( 1 . 6 1 \pm 0 . 3 0 ) ^ { \prime \prime } .$ ，它与相对论的结果相符.在各次日蚀中，至今已对四百多颗恒星作了这种测量.观测数据的范围是从1.57"至$2 . 3 7 ^ { \prime \prime }$ ,平均值是 $1 . 8 9 ^ { \prime \prime }$ .它与相对论符合得很好.

# 6.6光频的引力红移

当光子在稳定的引力场中传播，不同地点的静观测者将测得不同的频率.这叫光频的引力红移.它是等效原理的又一推论.

对稳定的引力场，适当地选取坐标可使度规 $g _ { \mu \nu }$ 与 $\mathcal { X } _ { \Uparrow }$ 无关.静 观测者测到的光子能量为

$$
E = - \ \not p _ { \mu } U ^ { \mu } ,
$$

其中 $\hbar _ { \mu }$ 为光子的四维动量， $U ^ { \mu }$ 为观测者的四维速度，它有形式（参看第四章 $\ S \ 4 . \ 3 )$

$$
U ^ { \mu } = = \frac { 1 } { \sqrt { - \mathrm { \small ~ \displaystyle ~ \xi ~ } } g _ { 0 0 } } ( 1 , 0 , 0 , 0 ) .
$$

把(6.6.2)用于(6.6.1)式，得

$$
E = \frac  - \frac { \mathbf { \nabla } \phi _ { 0 } } { \sqrt { \mathbf { \nabla } - \mathbf { \nabla } g _ { 0 0 } } } .
$$

按普朗克公式 $E = h \nu$ ，(6.6.3)式重写作

$$
\sqrt { \phantom { b } _ { \theta ^ { 0 } } } \nu \phantom { + } _ { 0 } \psi = - \phantom { } _ { \phi _ { 0 } } / h .
$$

这等式右边是常数，因为粒子在稳定场中运动时 $\pmb { \hat { p } } _ { 0 }$ 是守恒量.于是，(6.6.4)式说明,光频 $\nu$ 与所在地的 $\sqrt { - g _ { 0 0 } }$ 成反比.

具体看席瓦西尔引力场.它有

$$
\cdots \ g _ { 0 0 } = 1 - { \frac { 2 G M } { r } } .
$$

代入(6.6.4)得到

$$
\nu \sqrt { 1 - { \frac { 2 G M } { r } } } = - { \frac { \phi _ { 0 } } { \dot { h } } } .
$$

在离引力中心越远的地方测到的频率越小，因此叫引力红移.这是一种与多普勒(Doppler)红移完全不同的红移机制.

在弱引力场中，这红移量很小.在太阳表面测起来频率应为 $\nu _ { 0 }$ 的光在传播至远处时频率变为 $\nu , \nu$ 与 $\nu _ { \mathrm { 0 } }$ 之比是

$$
{ \frac { \nu } { \nu _ { 0 } } } = { \sqrt { 1 - { \frac { 2 G M } { R } } } } \approx 1 - { \frac { G M } { R } } .
$$

通常定义红移量 $z \equiv \nu _ { \mathrm { 0 } } / \nu - 1$ 于是，

$$
\begin{array} { r } { s \approx \frac { G M } { R } . } \end{array}
$$

我们又一次看到，弱中心引力场中的效应具有 $G M / R$ 的量级.对于太阳，它的值约为 $1 0 ^ { - \cdot 6 }$ .这红移量容易被其他效应所模糊或掩盖.例如太阳表面的大气湍流所产生的多普勒红移就可能大于它.所以很难用测量来检验.60年代，庞德(Pound)等人利用穆斯堡尔（Mossbauer)效应的原理在地球上测量从二十多米高射向地面的光线的蓝移（这是从位能高的地方射向位能低的地方，因而是蓝移).蓝移量的大小是 $1 0 ^ { \cdots 1 \ s }$ 的量级.实验结果与理论预言符合得很好.它被认为是支持广义相对论的重要实测证据之一.

最后讨论一下光源的固有频率的概念.与广义相对论前的物理学一样，光源的固有频率，是指相对光源静止的观测者测到的源所放的光子的频率.为具体起见，考虑原子的能级跃迁为光源.原子的固有频率取决于原子的能级结构，因此是它的固有属性.这里要指出的是作为等效原理的后果，光源的固有频率与引力场也无关，因为按等效原理，局域的引力场总可通过引入局域惯性系而使之消失.于是，太阳上的氢原子，地球上的氢原子及遥远的引力场已消失处的氢原子具有相同的固有频率.太阳上运动的氢原子跃迁所放的光的频率在相对该原子静止的观测者看来是固有频率；如果原子是在运动的，相对太阳静止的观测者会看到频率的多普勒红移；而远处的静观测者接收到远光子时则将看到多普勒红移和引力红移的联合效果.

# 第七章 黑 洞

拉普拉斯(Laplace)曾在牛顿力学的基础上指出，若恒星的半径 $R$ 小于 $2 G M / c ^ { 2 } \left( c \right.$ 是光速)，恒星表面所放的光将不能传播到无穷远处，从而远处的观测者不能看到这恒星.现在人们常把它作为黑洞观念的开端.可是，广义相对论的黑洞概念与它还是有本质区别的.按广义相对论，这种恒星的外部会有一个特殊的时空区，在那里光和其他粒子都只能单向地向引力源下落，而不可能静止或向外运动.恒星物质本身也只能不断收缩而变成密度为无穷的奇点.这种特殊的时空区就叫作黑洞.尽管人们至今尚未直接找到黑洞，但有许多理论上的原因和观测上的迹象使天体物理学家们相信黑洞在自然界中应该是存在的.本章将主要讨论席瓦西尔型黑洞的有关概念.最后还将介绍60年代末以来黑洞理论的发展.

# 7.1 $r { = } 2 ( \vec { \mathrm { , } } M$ 球面上时空的非奇异性

设想有一质量为 $M$ 而等效半径 $r$ 几乎为零的致密恒星.席瓦西尔外部解

$$
\mathrm { d } s ^ { 2 } = - \Big ( 1 - \frac { 2 G M } { r } \Big ) \mathrm { d } t ^ { 2 } + \Big ( 1 - \frac { 2 G M } { r } \Big ) ^ { - 1 } \mathrm { d } r ^ { 2 }
$$

$$
+ r ^ { 2 } \mathrm { d } \theta ^ { 2 } \div r ^ { 2 } \mathrm { s i n } ^ { 2 } \theta \mathrm { d } \varphi ^ { 2 } ,
$$

作为它的外引力场，几乎在全空间适用.在 $r { > } 2 G M$ 的区域内，坐标系是物理的.相应的物理性质已在前两章讨论过了.注意 $r =$ $2 G M$ 的球面.这等效半径 $\gamma ^ { \bullet }$ 被称为席瓦西尔半径或引力半径.

引力半径处首先的特征是

$$
g _ { \scriptscriptstyle { 0 0 } } = 0 , \quad g ^ { \scriptscriptstyle { 0 0 } } = \infty ,
$$

$$
g _ { 1 1 } \stackrel { \ldots } { - } \infty , \quad g ^ { 1 1 } \stackrel { \ldots } { = } 0 .
$$

度规的发散可能说明这是时空的奇异点，那里物理规律失去了意义.但也有可能它仅是坐标系的选择不当而带来的.我们将从物理的讨论来说明这里遇到的是后一情况.

考虑物体在引力作用下从 $r { > } 2 G M$ 处向中心的径向下落.按第六章 $\$ 6.2$ ，动力学方程是

$$
( \frac { \mathrm { d } r } { \mathrm { d } \tau } ) ^ { 2 } = E ^ { 2 } - \mathrm { ~ \scriptsize ~ \frac { 1 } { ~ 1 } ~ } - \frac { 2 G M } { r } ) ,
$$

$$
\frac { \mathrm { d } t } { \mathrm { d } \tau } = \left. E \right/ \left( 1 - \frac { 2 G M } { r } \right| .
$$

当 $r$ 逼近引力半径 $2 ( \gamma M , \mathrm { d } r / \mathrm { d } \tau$ 是有限值，而 $\mathrm { d } t / \mathrm { d } \tau$ 却趋于无穷.因而有三维速度

$$
\frac { \mathrm { d } r } { \mathrm { d } t } = \frac { \mathrm { d } r } { \mathrm { d } \tau } \bigg / \frac { \mathrm { d } t } { \mathrm { d } \tau }  0 .
$$

这结果与初速度无关，它似乎表明物体永远也不会穿过引力半径.注意到 $t$ 代表远处观测者的时间（参看第五章 $\ S \ 5 . 4 )$ ，所以结论只能是远处观测者永远不能看到自由下落物体穿过引力半径.但是，如果我们不是作为旁观者从远处观测，而是作为探险者随物体下落，这时固有时 $\pmb { \tau }$ 才代表我们的时间.（7.1.3)表明我们的下落速度 $\frac { \mathrm { d } \boldsymbol { r } } { \mathrm { d } \boldsymbol { \bar { \tau } } }$ 一直是有限的，所以引力半径是可以穿过的.我们现在来求解这运动.

设开始从静止下落时的有效半径 $r = r _ { 0 }$ ，方程(7.1.3)化为

$$
\frac { \mathrm { ; } } { \mathrm { ; } } \frac { \mathrm { ; } } { \mathrm { ; } } \bigg { } = 2 G M \bigg ( \frac { \mathrm { ~ l ~ } } { r } - \frac { 1 } { r _ { \circ } } \bigg ) .
$$

这方程容易求得一参数式的解

$$
r : = \mathrm { \small ~ \displaystyle \frac { } { 2 } ( 1 + \cos \eta ) ~ } ,
$$

$$
\tau = \frac { r _ { \circ } } { 2 } ^ { \prime } \cdot \frac { r _ { \circ } } { 2 G M } \Big \rangle ^ { 1 / 2 } ( \eta + \sin \eta ) .
$$

开始时 $\pmb { \eta } = 0$ .以后 $\tau$ 随 $\eta$ 增加， $r$ 随 $\eta$ 增大而减小.当达到 $r =$

$2 G M , \eta$ 满足

$$
\cos \eta = \frac { 4 G M } { r _ { \mathrm { 0 } } } - 1 ,
$$

因而时间 $\tau$ 是有限的.穿过引力半径后它仍将继续下落.当 $\eta = \pi$ ，即 $r = 0$ ，相应的时间是

$$
\tau = \frac { \pi r _ { 0 } } { 2 } \Big ( \frac { r _ { 0 } } { 2 G M } \Big ) ^ { 1 / 2 } .
$$

可见我们将在有限时间内一直落到引力中心，而没有遇到任何物理上不可逾越的时空奇点.这分析说明 $r = 2 G M$ 处引力强度是有限的，时空结构也是正常的.问题仅在于把与无穷远处的时钟相对准的时间坐标用在引力半径处是不合适的.

$r = 2  { \mathrm { ( } } j M$ 处时空的非奇异性也可从别的角度看出.计算 ${ \boldsymbol { r } } =$ $2 G M$ 球面与其他球面的固有距离，我们得到

$$
\int _ { 2 \ell M } ^ { r } | g _ { 1 1 } | ^ { 1 / 2 } \mathrm d r =  \begin{array} { l r } { [ r ( r - 2 G M ) ] ^ { 1 / 2 } } \\ { +  2 ( \xi M \mathrm { l n } \bigg [ \bigg ( \frac { r } { 2 G M } - 1 \bigg ) ^ { 1 / 2 } + \bigg ( \frac { r } { 2 G M } \bigg ) ^ { 1 / 2 } ] , } \\ { { r > 2 G M , } } \\ { -  2 ( \xi M \mathrm { c o t } ^ { - 1 } [ r ^ { 1 / 2 } / ( 2 G M - r ) ^ { 1 / 2 } ]   } \\ {   - [ r ( 2 G M - r ) ] ^ { 1 / 2 } ,   } & { { r < 2 G M } . } \end{array} 
$$

对 $0 < r < \zeta ( \times )$ ，它都是有限的.另外若计算曲率张量 $R _ { \mu \nu \rho \lambda }$ ，我们得到非零分量为

$$
\begin{array} { r l r } & { } & { R _ { \scriptscriptstyle { 0 1 0 1 } } = - \frac { 2 G M } { r ^ { 3 } } , \quad R _ { \scriptscriptstyle { 0 2 0 2 } } = R _ { \scriptscriptstyle { 0 3 0 3 } } = \frac { G M } { r ^ { 3 } } , } \\ & { } & \\ & { } & { R _ { \scriptscriptstyle { 2 3 2 3 } } = \frac { 2 G M } { r ^ { 3 } } , \quad R _ { \scriptscriptstyle { 1 2 1 2 } } = R _ { \scriptscriptstyle { 1 3 1 3 } } = - \frac { G M } { r ^ { 3 } } . } \end{array}
$$

它们在引力半径处也都是有限的，曲率张量的奇点只在 $r = 0$ 处.

# 7.2引力半径内的时空结构

$r = 2 G M$ 的球面虽不是奇点构成的，但它确是一个特殊的面，

以它为界，内部区域与外部区域的时空结构有着重要的区别.

为阐明这区别，我们先回忆一下闵柯夫斯基时空中光锥的概念.采用球坐标，闵柯夫斯基时空中的不变距离是

$$
\begin{array} { r } { \begin{array} { r } { \mathbf { d } s ^ { 2 } = - \mathbf { \nabla } \mathbf { d } t ^ { 2 } + \mathbf { d } r ^ { 2 } + r ^ { 2 } ( \mathbf { d } \theta ^ { 2 } + \sin ^ { 2 } \theta \mathbf { d } \varphi ^ { 2 } ) . } \end{array} } \end{array}
$$

光的运动满足 $\mathrm { d } s ^ { 2 } : = 0$ ,因此对径向传播的光有

$$
\begin{array} { r } { \frac { \mathrm { d } \boldsymbol { r } } { \mathrm { d } t } = \pm \mathrm { ~ 1 ~ } , } \end{array}
$$

$$
r = \pm \ t + C .
$$

这直线叫 $r - t$ 图上的光锥(图7.1).任何静质量不为零的质点的运动必满足 $\mathrm { d } s ^ { 2 } < 0$ ，即

$$
\left| \begin{array} { l } { \displaystyle \mathrm { d } r } \\ { \displaystyle \overline { { \mathrm { d } t } } } \end{array} \right| < 1 .
$$

这部分叫光锥的内部.从任--时空点看，物理上能实现的运动总限于该点的光锥内方向.零质量的粒子则沿光锥线运动.从该点向光锥外方向的运动意味着超光速，因而是物理上不可能的.光锥向着两个相反的方向展开，其中 $\mathrm { d } t > 0$ 的部分叫将来光锥， $\mathrm { d } t < 0$ 的部分则叫过去光锥.物理的运动是从过去光锥走向该点，然后从该点走向将来光锥.

现在用光锥的概念来讨论光在席瓦西尔场中的径向运动.由$\mathrm { d } s ^ { 2 } = 0$ ，得出席瓦西尔场中的光锥方程

$$
\frac { \mathrm { d } t } { \mathrm { d } r } \mathrel { \mathop : } = \pm \frac { 1 } { 1 - \frac { 2 G M } { r } \mathbin { \mathop : } }
$$

容易解出光锥线是

$$
\cdot \pm \ t = r + 2 G M { \bf l } _ { - } \left| \ 1 - \frac { r } { 2 G M } \right| + \mathrm { c o n s t . } .
$$

这些光锥线示于图7.2中．为方便起见，引入

$$
r ^ { * } \equiv r \ \cdots \ 2 G M \mathrm { l } \mathrm { l } \ \mathrm { l } \ - \ \frac { r } { 2 G M } \Big | \ ,
$$

光锥线可写作

![](images/e9e0c2b8c8eb581f7d87ce79251e17f742888f6238c6e813960b48f9b9409e1e.jpg)  
终7.1闵柯夫斯基空间的光锥

![](images/b3d84bdc112ea2f2851fdcb048606f091b7f1073813f601fb904ef94a82216dd.jpg)  
图7.2席瓦西尔坐标下的光锥

$$
\begin{array} { r c l } { { t + r ^ { * } = V , } } \\ { { } } & { { } } \\ { { t - r ^ { * } = U , } } \end{array}
$$

其中 $V$ 和 $\boldsymbol { U }$ 是积分常数.当 $r { > } 2 G M$ ，(7.2.7)式描述光的径向向内的运动，（7.2.8)式描述光的径向向外的运动.其它非零质量粒子也同样可以径向向内或径向向外运动. $r { > } 2 G M$ 区域内的光锥线有个引人注意的特征，即没有一条光锥线能穿过引力半径球面.所有光锥线都渐近地逼近它，说明--切粒子都要花费无穷长的时间 $t$ 去靠近引力半径.因此即使穿过引力半径面的运动实际上能发生，这样的时间坐标 $t$ 已无法描述了.

我们暂时放下如何穿过引力半径的问题，而来讨论引力半径内的时空结构.这区域内的光锥线仍示于图7.2.光锥线本身并没有显著特征，可是光锥内外的取向却不一样了，注意物理的运动满足 $\mathrm { d } s ^ { 2 } \leqslant _ { \ast } ^ { - } 0$ ,现在由于 $\underset { \gamma ^ { - } } { \underbrace { \overset { \cdot \mathrm { ? } } { } } } \overset { \cdot \mathrm { ? } } { \underbrace { \mathrm { ? } } } \underset { \mathrm { ? } } { \underbrace { M } } < \underset { \mathrm { ? } } { \underbrace { \mathrm { ? } } } 0$ ，所以光锥内方向应满足

$$
\Bigg \{ \frac { \mathrm { d } r } { \mathrm { d } t } ; \geq \stackrel { i } { _ { \perp } } 1 - \frac { 2 G M } { r } \Bigg \} ^ { 2 } .
$$

这方程所决定的两个方向不是 $\pmb { t }$ 的增加和减少方向，而是 $r$ 的增加和减少方向.这--差别显示了引力半径内部区域的一些非常不寻常的特征．首先， $\frac { \mathrm { d } \boldsymbol { r } } { \mathrm { d } t } = 0$ 是非物理的；即任何粒子都不可能静止于内部区.这正是黑洞概念的要点之一.其次，物理的运动可导致$t$ 的增加，也可导致 $t$ 的减小.注意在这种时间坐标下，内部与外部无法沟通，所以这一点除了进一步说明席瓦西尔时间坐标 $t$ 在 $r { \leqslant }$ 2GM区域内的不适宜，此外并不会给外部区域带来因果的混乱.再则，物理的运动只能导致 $_ r$ 的单调增加，或者单调减小，它取决于如何在内部区定义“将来"和"过去”.如果把 $\pmb { r }$ 增加的方向定义为将来光锥，那么内部区的物质只能向外运动而穿出引力半径球面.这种情形叫作白洞.如果把 $_ r$ 减小的方向定义为将来光锥，那么外部区的物质一旦穿入内部，它只能落向引力中心.停止或返回都是不可能的.这种情形叫作黑洞.

现在我们已看到，引力半径球面虽不是奇异面，但它是两个物理性质很不同的时空区的界面.按现在的术语，它们分别叫作白洞或黑洞的视界.

# 7.3爱丁顿(Eddington）坐标

上面已说明，视界面上度规的奇异性是席瓦西尔时间坐标选用不当而带来的弊病.因此，人们曾致力于寻找更适当的坐标以消除弊病.爱丁顿坐标就是一种能部分地消除这弊病的坐标，它是爱丁顿在20年代引入的，而芬克尔斯坦(Finkelstein)在50年代末对它进行了深入的研究.

当光子向内落时，席瓦西尔时间坐标的弊病表现在 $r {  } 2 G M$ 时，

$$
t = - r - 2 G ; M \ln \Bigl ( \frac { r } { 2 G M } - 1 \Bigr ) \to \infty ,
$$

作一坐标变换把 $t$ 换成 $\tilde { t } , r$ 不变：

$$
\begin{array} { r l } & { \tilde { t } = t + 2 G M \ln \left| \cfrac { r } { 2 G M } - 1 \right| , } \\ & { \tilde { r } = r . } \end{array}
$$

这样下落穿过视界时的坐标弊病就会消除，因现在 $\widetilde { r } = r = 2 G M$ 时， $\tilde { \pmb { t } }$ 必定是有限的(参看(7.2.5)至(7.2.8)式).为看清新坐标下度规与光锥线的结构，我们写出相应的不变距离公式，为书写方便，仍用 $t$ 和 $r$ 表示新坐标，省略了上面的波纹号，

$$
\begin{array} { l } { { \displaystyle \mathrm { d } s ^ { 2 } = - \mathrm { ~  ~ \left( ~ 1 ~ - ~ \right)} \frac { 2 G M } { r }  \mathrm { d } t ^ { 2 } + \left( ~ 1 + \frac { 2 G M } { r } \right) \mathrm { d } r ^ { 2 } } } \\ { { \mathrm { ~  ~ \left. ~ \right. ~ } + \frac { 4 G M } { r } \mathrm { d } r \mathrm { d } t + r ^ { 2 } \mathrm { d } \Omega ^ { 2 } , } } \end{array}
$$

其中 $\mathbf { d } \varOmega ^ { 2 }$ 是立体角元，不细写出.由 $\mathbf { d } s ^ { 2 } { \ : = } 0$ 和 $\mathrm { d } \Omega ^ { 2 } = 0$ 得出径向运动的光锥线方程：

$$
\frac { \mathrm { d } \boldsymbol { r } } { \mathrm { d } t } = - \mathrm {  ~ 1 ~ } ,
$$

$$
\frac { \mathrm { d } r } { \mathrm { d } t } = \left. \left( 1 \cdots \frac { 2 G M } { r } \right) \bigg / \left( 1 + \frac { 2 G M } { r } \right) \cdot\right.
$$

由（7.3.4)解出--组光锥线

$$
t + r \simeq V .
$$

由(7.3.5)式解出另一组光锥线

$$
t - r - 4 ( \dot { r } M \ln \left| 1 - \frac { r } { 2 G M } \right| = U .
$$

这两组光锥线示于图7.3.从图线看出，用新坐标讨论外部粒子下落穿过视界面的运动已没有任何弊病出现，即在坐标时 $t$ 为有限值时粒子穿过了视界.然后再看内部区的光锥结构.现在光锥内的两种取向仍与坐标时 $\pmb { t }$ 的正负向一致，因而将来与过去的概念自然地获得了明确的定义.从向上的将来光锥看， $t$ 的增加必定伴随$r$ 的减小，即新坐标在内部区正确地描述了黑洞的行为.对于 $_ r$ 增加的运动，新坐标仍具有弊病.如果我们用它描述白洞，那么内部区的将来方向就是 $t$ 减少的方向，而且内部物质必须在 $t {  } - \infty$ 时才能逼近视界而不能描述穿出视界的过程.因此这组新坐标被称为爱丁顿内行坐标.人们常用它讨论物体下落而进入视界的运动，这一点用席瓦西尔坐标是不成的.但是这组坐标仍不能描述白洞的物质发射过程.

若需要讨论物体从内部区向外穿过视界的运动，可以类似地引入爱丁顿外行坐标

$$
\check { t } = { t } - 2 G M \ln \left| \frac { r } { 2 G M } - 1 \right| ,
$$

![](images/d7286246e162ad9f23722bc74534d98bc5219a6f367ae2891ddc59aa33c0052d.jpg)  
图7.3爱丁顿内行坐标下的光锥图7.4爱丁顿外行坐标下的光锥

外行坐标下的不变距离公式为

$$
\begin{array} { l }  \displaystyle \mathrm { d } s ^ { 2 } = \ldots \left( \begin{array} { l } { \displaystyle 1 - \frac { 2 G M } { r } \right) \mathrm { d } t ^ { 2 } + \left( \mathrm { 1 } + \frac { 2 G M } { r } \right) \mathrm { d } r ^ { 2 } } \\ { \displaystyle \ldots \left( \frac { 4 G M } { r } \mathrm { d } r \mathrm { d } t + r ^ { 2 } \mathrm { d } \Omega ^ { 2 } . \right. } \end{array} \end{array}
$$

由此导出径向的光锥线方程，

$$
\begin{array} { l } { \displaystyle \frac { \mathrm { d } \boldsymbol { r } } { \mathrm { d } t } = 1 , } \\ { \displaystyle \frac { \mathrm { d } \boldsymbol { r } } { \mathrm { d } t } = - \left. \left( 1 - \frac { 2 G M } { r } \right) \right/ \left( 1 + \frac { 2 G M } { r } \right) . } \end{array}
$$

得出相应的光锥线解是

$$
\begin{array} { l } { t - r = U , } \\ { t + r + 4 ( r M \ln \left| 1 - \frac { r } { 2 G M } \right| = V . } \end{array}
$$

外行坐标下的光锥结构画于图7.4.作完全类似的讨论看出，这坐标对处理内部粒子向外穿过视界的运动已没有弊病.但却不能处理外部粒子向内穿过视界的运动.

总之，采用爱丁顿内行或外行坐标，坐标系在视界面上的弊病将部分地被消除.值得强调，视界面内外时空性质的不同，即外部是可能运动的双向区而内部是可能运动的单向区，这并没有因坐标的改变而改变.也就是说，视界内部的特殊性是时空所固有的，而不是选用某--种坐标系的后果.

# $\ S 7 . 4$ 克鲁斯卡(Kruskal）坐标

60年代初，克鲁斯卡和采克莱斯(Szekeres)独立地建立了-组能完全消除视界面的弊病的坐标系，我们叫它克鲁斯卡坐标.

克鲁斯卡坐标记为 $( \zeta ^ { \prime } \cdot u , \theta , \varphi )$ ,即角坐标 $\theta$ 和 $\varphi$ 与席瓦西尔角坐标一致，而用 $\pmb { \tau }$ 和 $\pmb { u }$ 代替席瓦西尔的时间坐标 $t$ 和径向坐标 $r$ $u \cdot v$ 与 $r , t$ 的关系定义为

当 $r { > } 2 G M$ 时，

$$
\begin{array} { l } { { \displaystyle { \boldsymbol { u } } = \pm \left( \frac { r } { 2 \bar { G } M } - 1 \right) ^ { 1 / 2 } \mathrm { e } ^ { r / 4 G M } \mathrm { c o s h } \frac { t } { 4 G M } } , } \\ { { \displaystyle { \boldsymbol { v } } = \pm \left( \frac { r } { 2 \bar { G } \bar { M } } - 1 \right) ^ { 1 / 2 } \cdot \mathrm { e } ^ { r / 4 G M } \mathrm { s i n h } \frac { t } { 4 G M } } , } \end{array}
$$

当 $r { < } , 2 G M$ 时，

$$
\begin{array} { l } { { u = \pm \left( \mathrm { 1 } - \mathrm { \frac { \partial } { 2 G M } } \right) ^ { \mathrm { 1 / 2 } } \mathrm { e } ^ { r / \mathrm { 4 } G M } \mathrm { s i n h } \mathrm { \frac { \partial } { 4 G M } } , } } \\ { { { \upsilon = \pm \left( \mathrm { 1 } - \mathrm { \frac { \partial } { 2 G M } } \right) ^ { \mathrm { 1 / 2 } } \mathrm { e } ^ { r / \mathrm { 4 } G M } \mathrm { c o s h } \mathrm { \frac { \partial } { 4 } } G M } . } } \end{array}
$$

经这坐标变换后，时空不变距离公式变成

$$
\mathrm { d } s ^ { 2 } = \frac { 3 2 G ^ { 3 } M ^ { 3 } } { r } \mathrm { e } ^ { - r / 2 G M } ( - \mathrm { \bf ~ d } v ^ { 2 } + \mathrm { d } u ^ { 2 } ) + r ^ { 2 } ( \mathrm { d } \theta ^ { 2 } + \mathrm { s i n } ^ { 2 } \theta \mathrm { d } \varphi ^ { 2 } ) ,
$$

其中 $_ r$ 作为 $_ z$ 和 ${ \pmb u }$ 的函数由下式隐示

$$
\Big ( \frac { r } { 2 G M } - ~ 1 \Big ) \mathrm { e } ^ { r / 2 G M } = u ^ { 2 } - v ^ { 2 } .
$$

由(7.4.5)式看出，克鲁斯卡坐标中的度规张量在视界面上没有奇异性.它正是设计这组坐标时期望的目标.这组坐标还有一些特征也是值得注意的：

（a）满足 $\mathbf { d } s ^ { 2 } = 0$ 的光锥线的方程是

$$
\operatorname { \dag } _ { \operatorname { \dot { d } } \operatorname { \overline { { \upsilon } } } } ^ { \mathrm { d } u } = \pm 1 .
$$

它是与 $u \cdot v$ 轴成 $4 5 ^ { \circ }$ 角的两个直线族.

(b)由（7.4.6)式看到， $r =$ 常数被表示成一对双曲线

特别是视界面 $r { = } { \div } 2 G M$ ，它变成了一对直线

$$
u = \pm \ v .
$$

这对直线把 $u , v$ 平面分成四片(图7.5).第I和 $\mathbb { I }$ 片上 $\pmb { u } ^ { 2 } > \tau ^ { 2 }$ ，即$r { > } 2 G M$ ，它是视界外部区，第 $\mathbb { I }$ 和 $\mathbb { N }$ 片上 ${ \pmb u } ^ { 2 } < { \pmb v } ^ { 2 }$ ，即 $r { < } 2 G M$ ，它是视界内部区.引力中心 $r = \circledast = 0$ 表现为

$$
{ \vec { \imath } } ^ { \because } - u ^ { 2 } = 1 ,
$$

是一对上下的双曲线.这对双曲线之外的区域对应 $r < 0$ ，因而是非物理的.

(c)由克鲁斯卡坐标变换的定义式导出，

$$
\operatorname { t a n h } { \frac { t } { 4 G M } } = { \frac { u } { v } } , \quad { \frac { * * } { \exists } } r < 2 G M .
$$

等 $t$ 面是一族由原点出发具有任意斜率的直线族.当 $\pmb { u } \equiv \pmb { v }$ ，有$t = \infty$ ； $\scriptstyle u = \cdots y$ ，有 $t = - \zeta >$ .注意这对直线恰好与视界重合.它反映了 $\$ 7.1$ 中的结果：当达到视界，席瓦西尔时间坐标 $t$ 将是无穷大. $u = 0$ 的直线在 $\mathbb { I }$ 和 $\mathbb { N }$ 区，因而代表 $\pmb { t = } 0 \ ; v = 0$ 的直线在！和Ⅲ区，因而也代表 $t = 0$

![](images/d26237bf120c7b04d2ed4406a3d52b13e7a0279f736537f6191338d94a8649f3.jpg)  
图7.5克鲁斯卡坐标

因为在采用克鲁斯卡坐标后，弊病的奇异性消失了，所以我们可以用它讨论球对称时空的全局结构.我们把这一讨论推到下一节，而在这里补充说明一下这组坐标的设计思想.注意克鲁斯卡坐标变换式作为定义，它并不需要有推导.

爱丁顿内行坐标变换(7.3.2)的动机是把内行光锥线(7.2.7)展成直线，即

$$
\tilde { t } + \tilde { r } = V ,
$$

从而克服了质点内行过视界时的弊病.同样，他的外行坐标变换

(7.3.8)是要把外行光锥线(7.2.8)展成直线，即

$$
\dot { t } - \acute { r } = U ,
$$

从而克服质点外行过视界时的弊病.那么是否有可能同时利用这两组变换，以使内行和外行光锥线都展成直线呢?我们试着把两组光锥线的编号参量 $V$ 和 $U$ 当新坐标，利用(7.2.7)和(7.2.8)式把变换定义为

$$
\begin{array} { r } { V ^ { \prime } = t + r ^ { * } , } \\ { \imath ^ { \prime } = t - r ^ { * } , } \end{array}
$$

其中 $r ^ { \star }$ 仍由（7.2.6)定义.这样，

$$
\mathrm { d } V ^ { \prime } \mathrm { d } l ^ { \prime } = \mathrm { d } t ^ { 2 } \mathrm { ~ -- ~ } \mathrm { d } r ^ { \mathrm { ~ - ~ } \cdot \cdot } = \mathrm { d } t ^ { 2 } - \mathrm { d } r ^ { 2 } \Big / \Big ( 1 - \frac { 2 G M } { r } \Big ) ^ { 2 } .
$$

于是席瓦西尔不变距离公式变为

$$
\mathrm { d } s ^ { 2 } = - \mathrm { ~ \left( ~ 1 ~ -- ~ \right)} \frac { 2 G M } { r }  \mathrm { d } V \mathrm { d } U + r ^ { 2 } ( \mathrm { d } \theta ^ { 2 } + \sin ^ { 2 } \theta \mathrm { d } \varphi ^ { 2 } ) ,
$$

其中 $_ r$ 是 $U$ 和 $V$ 的函数，由（7.2.7)和（7.2.8)式的逆变换决定，由（7.4.14）立即看出，视界面上的奇异性没有消除，即预想的目的没有达到.可是(7.4.14)式也暗示了消除这种奇异性的途径.若对光锥线重新编号，即引入 $\tilde { \cal U } ,$ 和 $\tilde { V }$ 代替 $U$ 和 $V$ ，让

$$
\begin{array} { r } { \tilde { V } = \tilde { V } ( V ) , \tilde { U } = \tilde { U } ( U ) , } \end{array}
$$

不变距离公式（7.4.14)中 $\therefore j$ 角度无关的部分将跟着变为

$$
\mathrm { d } s ^ { z } = \cdots \left( \mathrm {  ~ l ~ } \cdots \frac { 2 G M } { r } \right) \frac { \mathrm { d } V } { \mathrm { d } \tilde { V } } \frac { \mathrm { d } U } { \mathrm { d } \tilde { U } } \mathrm { d } \tilde { V } \mathrm { d } \tilde { U } .
$$

函数 $\tilde { V }$ 和 $\tilde { U }$ 的形状是任意的.适当选取它，以使

$$
\left\{ \begin{array} { l l l } { 1 } & { \mathrm { ~ \_ ~ } } & { \displaystyle \frac { 2 G M } { r } } \end{array} \right\} \frac { \mathrm { d } V } { \mathrm { d } \tilde { V } } \frac { \mathrm { d } U } { \mathrm { d } \tilde { U } }
$$

不出现病态的奇异性，我们的目的就达到了.例如选取

$$
\tilde { V } = \mathrm { e } ^ { V / 4 ( \ne M } = \Big ( \frac { r } { 2 G M } - 1 \Big ) ^ { 1 / 2 } \mathrm { e } ^ { r / 4 G M } \mathrm { e } ^ { \imath / 4 G M } ,
$$

$$
\tilde { U } = - \mathrm { ~ e } ^ { \cdots \prime 4 G M } = - \left( \frac { r } { 2 G M } - 1 \right) ^ { 1 / 2 } \mathrm { e } ^ { r / 4 G M } \mathrm { e } ^ { - \imath / 4 G M } .
$$

(7.4.16)相应变成

$$
\mathrm { d } s ^ { 2 } = - \mathrm { ~ \frac { 3 2 G ^ { 3 } { \cal M } ^ { 3 } } { r } e ^ { - r / 2 G M } d } \tilde { V } \mathrm { d } \tilde { U } ,
$$

视界面 $r { = } 2 G M$ 上的奇异性不再存在.注意 $\tilde { V }$ 和 $\tilde { U }$ 为常数的坐标线是光锥线，即光子的世界线.为了更符合习惯，我们引入新的时间坐标 $_ { v }$ 和新的径向坐标 ${ \pmb u }$ ，趁机要求光锥线为与坐标线成 $4 5 ^ { \circ }$ 角的直线，为此定义

$$
v \equiv \frac { 1 } { 2 } ( \tilde { v } + \tilde { U } ) = \left( \frac { r } { 2 G M } - 1 \right) ^ { 1 / 2 } { \bf e } ^ { r / 4 G M } { \bf c o s h } \frac { t } { 4 G M } ,
$$

$$
u \equiv \frac { 1 } { 2 } ( \tilde { V } - \tilde { U } ) = \Big \langle \frac { r } { 2 G M } - 1 \Big \rangle ^ { 1 / 2 } \mathrm { e } ^ { r / 4 ( \dot { \varsigma } M } \mathrm { s i n h } \frac { t } { 4 G M } .
$$

(7.4.18)又改为

$$
\mathrm { d } s ^ { 2 } = \frac { 3 2 ^ { ( \frac { \ d ^ { 3 } } { \ d r } ) } } { r } \frac { M ^ { 3 } } { \ d r } \mathrm { e } ^ { - r / 2 G M } ( - \mathrm { d } v ^ { 2 } + \mathrm { d } u ^ { 2 } ) .
$$

这正与(7.4.5)式相符合.可是(7.4.17)和(7.4.19)必竟还有缺点，当 $r < 2 G M$ ，坐标成了虚数.经反复尝试，人们已发现在 $r <$ $2 G M$ 的区域内把定义(7.4.19)修改为

$$
\begin{array} { r } { \boldsymbol { u } = \left( \mathrm { 1 ~ -- ~ } \frac { r } { 2 G M } \right) ^ { \mathrm { 1 / 2 } } \mathrm { e } ^ { r / 4 G M } \mathrm { s i n h } \frac { t } { 4 G M } , } \\ { \boldsymbol { v } = \left( \mathrm { 1 ~ -- ~ } \frac { r } { 2 G M } \right) ^ { \mathrm { 1 / 2 } } \mathrm { e } ^ { r / 4 ( \dot { v } M } \mathrm { c o s h } \frac { t } { 4 G M } , } \end{array}
$$

则兼顾了各方面的合理性.而这就是本节开始引入的克鲁斯卡坐标变换.

# $\$ 7.5$ 球对称时空的全局结构

有了不含弊病的克鲁斯卡坐标，我们就有可能在球对称时空