# 第二章 黎曼（Riemann）几何

在仿射空间中引入度规场和不变距离，就构成了黎曼空间.这章要讨论的是黎曼空间的几何和黎曼空间中的张量分析.

# 2.1黎曼空间和度规张量

我们用二次型

$$
\mathrm { d } s ^ { 2 } = g _ { \mu } \mathrm { d } x ^ { \mu } \mathrm { d } x ^ { \nu }
$$

来定义空间相邻两点（坐标差为 ${ \mathrm { d } } x ^ { \mu } )$ 的距离 ${ \bf d } s$ .规定 ${ \bf d } s$ 与坐标无关，即是标量.这样 $g _ { \mu \nu }$ 就是二阶的协变张量，它叫度规张量.为确定起见，令 $g _ { \mu \nu }$ 是对称张量，

$$
g _ { \mu \nu } = g _ { \nu \mu } .
$$

否则， $g _ { \mu \nu }$ 的反称组合对 ${ \mathrm { d } } s$ 没有贡献，因而是不确定的和没有意义的.在仿射空间中确立了度规场后，空间任意两相邻点的距离有了意义，这样的空间就叫黎曼空间.

我们熟知的三维欧氏空间是黎曼空间的特例.在欧氏空间采用笛卡儿坐标 $x ^ { ! } = x , x ^ { 2 } = y$ 和 $x ^ { 3 } = z$ ，相邻点的距离公式是

$$
\mathrm { d } s ^ { 2 } = \mathrm { d } x ^ { 2 } + \mathrm { d } y ^ { 2 } + \mathrm { d } z ^ { 2 } .
$$

这就是说度规张量是

$$
g _ { \mu \nu } = { \left( \begin{array} { l l l } { 1 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } \\ { 0 } & { \cdot } & { 0 } \end{array} \right) } .
$$

这张量的分量值与空间点无关.当在欧氏空间采用球坐标 $x ^ { \mathrm { { I } } } = r$ ，$x ^ { 2 } = \theta$ 和 $x ^ { 3 } = \varphi$ ，距离公式变为

$$
\mathrm { d } s ^ { 2 } = \mathrm { d } r { \dot { \ } } + r ^ { 2 } \mathrm { d } \theta ^ { 2 } + r ^ { 2 } \mathrm { s i n } ^ { 2 } \theta \mathrm { d } \varphi ^ { 2 } ,
$$

相应的度规张量是

$$
g _ { \mu \nu } = { \left( \begin{array} { l l l } { 1 } & { 0 } & { } & { 0 } \\ { 0 } & { r ^ { 2 } } & { 0 } \\ { 0 } & { 0 } & { r ^ { 2 } \sin ^ { 2 } \theta } \end{array} \right) } .
$$

这张量的分量是与点有关的.在欧氏空间中采用笛卡儿坐标的好处正在这里.

另一熟知的例是四维的闵柯夫斯基(Minkowski)空间,它是黎曼空间的又一特例.取坐标 $x ^ { 9 } = c t , x ^ { 1 } = x , x ^ { 2 } = y$ 和 $x ^ { 3 } = z$ ，不变距离公式是

$$
\mathrm { d } s ^ { 2 } = - \ c ^ { 2 } \mathrm { d } t ^ { 2 } + \mathrm { d } x ^ { 2 } + \mathrm { d } y ^ { 2 } + \mathrm { d } z ^ { 2 } ,
$$

即度规张量是

$$
g _ { \mu \nu } = \left( \begin{array} { c c c c } { { - 1 } } & { { 0 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 1 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 1 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { 1 } } \end{array} \right) \equiv \eta _ { \mu \nu } .
$$

对个黎曼空间，如能适当选取坐标,使它的度规张量具有形式：

$$
g _ { \mu \nu } = \left\{ { \begin{array} { l l } { + 1 \ { \overline { { \mathfrak { s } } } } { \overline { { \mathfrak { x } } } } - 1 , } & { \mu = \nu ; } \\ { 0 , } & { \mu \neq \nu , } \end{array} } \right.
$$

则叫它是平坦的黎曼空间（它与第一章 $\ S \ 1 . \ 6$ 中讲的平坦性的关系将在后面看到).

线性代数中有一条定理与这问题很有关系.下面把它叙述成我们所要的形式.

定理：对常系数的二次型

$$
\mathrm { d } s ^ { 2 } = g _ { \mu \nu } \mathrm { d } x ^ { \mu } \mathrm { d } x ^ { \nu } ,
$$

若det $\mid _ { { \pmb { g } } _ { \mu \nu } } \mid \neq 0$ ,则必能找到坐标变换，把这二次型化为坐标微分的平方和(或差).亦即使变换后的系数 $\smash { \widetilde { g } _ { \mu \nu } }$ 满足(2.1.9).

在黎曼空间中 $g _ { \mu \nu }$ 一般不是常数.这时上述定理告诉我们，总

可以用坐标变换把任- $J ^ { \gamma }$ 点的度规 $g _ { \mu \nu } ( P )$ 化成（2.1.9）的形式这定理还有一推论：如果区域 $V$ 内度规张量场是常数，那么 $V$ 内的空间是平坦的.

关于平坦性，最重要的问题是怎么判断度规场能或不能变成(2.1.9)的形式.这问题将在本章的 $\ S 2 . 5$ 中回答.

# 2.2 张量指标的升降

在黎曼空间中，某点上的逆变矢量 $T ^ { \mu }$ 可借助该点的度规张量来定义相应的协变矢量，

$$
T _ { \ast } \equiv g _ { \mu \nu } T ^ { \nu } .
$$

其他有逆变指标的张量也可做同样的操作，如

$$
T _ { \mu \nu } = g _ { \mu \alpha } T _ { \nu } ^ { \alpha } .
$$

这叫张量指标的下降.

当det $i _ { g , \mu \nu } \mid \neq 0$ ，我们可以定义逆变的度规张量 $g ^ { \mu \nu }$ ，它满足

$$
g ^ { \mu \nu } g _ { \nu \lambda } = \delta _ { \lambda } ^ { \mu } .
$$

利用 $g ^ { \prime \prime \prime }$ ，就可以作张量指标上升的操作，如

$$
T ^ { \prime \prime } \equiv g ^ { \mu \nu } T , .
$$

$$
T ^ { \prime \prime } { } ^ { \prime \prime } \equiv g ^ { \mu \alpha } T _ { \alpha } ^ { \nu } .
$$

总之，利用度规可以把任-个张量形式的物理量或几何量表示成逆变的、协变的或混合的形式.这是黎曼空间中的张量的新性质.下面两个例子是该性质的应用.

例1任一矢量可借助度规而构成一个标量

$$
g _ { \mu \nu } T ^ { \prime \prime } T ^ { \ast } = T , T ^ { \ast } = g ^ { \mu \nu } T , T , \nonumber
$$

这标量叫矢量长度的平方.

例2不变距离可写作

$$
\mathrm { } \mathrm { d } s ^ { 2 } = g _ { \mu \mathrm { } } \mathrm { d } x ^ { \prime \prime } \mathrm { d } x ^ { \nu } = \mathrm { d } x , \mathrm { d } x ^ { \nu } = g ^ { \mu \nu } \mathrm { d } x _ { \mu } \mathrm { d } x _ { \nu } .
$$

中间一式表明度规的混合张量形式是克龙涅克张量，

$$
g _ { \nu } ^ { \mu } = \delta _ { \nu } ^ { \mu } .
$$

这一点也可从(2.2.3)式看出.

# \$2.3 克里斯朵夫(Christoffel)联络

仿射空间中借助联络定义了矢量的平移.黎曼空间中进一步要求平移操作保持矢量的长度不变.这一性质在欧氏空间中是自然具有的.本节将证明，如采用对称联络，那满足这附加要求的联络完全由度规场决定.这种联络叫克里斯朵夫联络.

考虑 $P$ 点的逆变矢量 $A ^ { \mu } ( P )$ .借助联络 $T _ { \nu \lambda } ^ { \mu }$ 把它平移至邻点 $\mathbf { Q }$ 而成为 $A ^ { \mu } ( P {  } Q )$ ，

$$
A ^ { \mu } ( P \to Q ) = A ^ { \mu } ( P ) - { \cal { I } } _ { \nu \lambda } ^ { \mu } ( P ) A ^ { \nu } ( P ) \mathrm { d } x ^ { \lambda } .
$$

若平移不改变矢量长度，则

$$
\begin{array} { c } { { g _ { \mu \nu } ( Q ) A ^ { \mu } ( P \to Q ) A ^ { \nu } ( P \to Q ) } } \\ { { = g _ { \mu \nu } ( P ) A ^ { \mu } ( P ) A ^ { \nu } ( P ) . } } \end{array}
$$

由度规场的微分公式

$$
g _ { \mu } ( Q ) = g _ { \mu \nu } ( P ) + g _ { \mu , \lambda } ( P ) { \mathrm d } x ^ { \lambda } ,
$$

把（1.3.7)和(2.3.2)式代入(2.3.1)，保留一级小量，再注意 $A ^ { \mu }$ 是任意矢量，我们得到

$$
g _ { \mu \nu , \lambda } \ : - \ : g _ { \alpha } I _ { \mu \lambda } ^ { a } \ : - \ : g _ { \mu \alpha } I _ { \nu \lambda } ^ { \alpha } = 0 .
$$

这是能保持长度的联络所必须满足的方程.

(2.3.3)式对 $\pmb { \mu }$ 和 $\pmb { \nu }$ 是对称的，因此它只包含 $\pmb { n } ^ { 2 } ( \pmb { n } + 1 ) / 2$ 个独立的方程.可是联络 $\Gamma _ { \nu \lambda } ^ { \mu }$ 有 $\pmb { n } ^ { 3 }$ 个独立分量.所以(2.3.3)式不足以确定联络.如果我们规定联络是对称的，即限于讨论挠率为零的空间，那联络的独立分量也是 $n ^ { 2 } \left( n + 1 \right) / 2$ 个.这时联络将完全被度规场确定，并可由(2.3.3)式解出.

用指标的循环替换 $\mu \to \nu \to \lambda \to \mu$ ，(2.3.3)式可写成

$$
g _ { \nu \lambda , \mu } - g _ { \alpha \lambda } \Gamma _ { \nu \mu } ^ { \alpha } - g _ { \nu \alpha } \Gamma _ { \lambda \mu } ^ { \alpha } = 0
$$

及

$$
g _ { \lambda \mu , \nu } - g _ { \alpha \mu } \Gamma _ { \lambda \nu } ^ { \alpha } - g _ { \lambda \alpha } \Gamma _ { \mu \nu } ^ { \alpha } = 0 .
$$

把(2.3.3)式与(2.3.4)式相加，再减去(2.3.5)式，注意联络是对称的，我们解出

$$
\qquad r _ { \nu \lambda \mu } \equiv g _ { \alpha } r _ { \lambda \mu } ^ { \alpha } = \frac { 1 } { 2 } ( g _ { \mu \nu , \lambda } + g _ { \nu \lambda , \mu } - g _ { \lambda \mu , \nu } ) { . }
$$

它也可以化成

$$
T _ { \lambda \mu } ^ { \alpha } = \frac { 1 } { 2 } g ^ { \alpha \nu } ( g _ { \mu , \lambda } + g _ { \nu \lambda , \mu } - g _ { \lambda \mu , \nu } ) .
$$

这些公式说明，若在黎曼空间内确定了度规，并采用对称联络，那这联络完全由度规和它的普通微商决定.这样的联络叫克里斯朵夫联络.

顺便指出，(2.3.3)式可利用协变微商的定义而写成(参看（1.4.11)式）

$$
g _ { \mu \nu ; \lambda } = 0 .
$$

再利用(2.2.3)式和(1.4.12)式，可得出

$$
g _ { \scriptscriptstyle 3 , \lambda } ^ { \mu \nu } = 0 .
$$

这说明度规张量在协变微商下的行为和常数张量在普通微商下的行为是一样的.

由于广义相对论所用的是无挠率的黎曼空间，因此以后我们将限于讨论对称联络.这时有一条重要的定理：在坐标 $x ^ { \mu }$ 下 $P$ 点的联络为 $( \Gamma _ { \mu \nu } ^ { \lambda } ) _ { P }$ .我们总可找到坐标变换 $x ^ { \mu } { \to } \tilde { x } ^ { \mu }$ ，使得

$$
( \tilde { \cal I } { } _ { \mu \nu } ^ { \lambda } ) _ { P } = 0 .
$$

证明如下：让坐标变换 $x ^ { \mu } { \to } \tilde { x } ^ { \mu }$ 满足

$$
x ^ { \mu } - x _ { \textsc { p } } ^ { \cdot \mu } = { \tilde { x } } ^ { \mu } + { \frac { 1 } { 2 } } C _ { \alpha \beta } ^ { \mu } { \tilde { x } } ^ { a } { \tilde { x } } ^ { \beta } ,
$$

其中 $C _ { \alpha \beta } ^ { \mu } { \stackrel {  } { = } } C _ { \beta \alpha } ^ { \mu }$ ,且都是常数. $P$ 点的旧坐标是 $\boldsymbol { x } _ { P } ^ { \mu }$ ，新坐标 $\widetilde { x } _ { P } ^ { \mu } = 0$ 由(2.3.11)算出

$$
\left\{ \begin{array} { c } { { \frac { \ni x ^ { \mu } } { \negth } } } \\ { { \neg \tilde { x } ^ { \lambda } } } \end{array} \right\} _ { P } = \delta _ { \lambda } ^ { \mu } , \quad \left\{ \begin{array} { c } { { \frac { \ni \tilde { x } ^ { \mu } } { \partial x ^ { \lambda } } } } \end{array} \right\} _ { P } = \delta _ { \lambda } ^ { \mu } ,
$$

以及

$$
\left\{ \begin{array} { l } { \frac { \ni ^ { 2 } { \mathcal { X } } ^ { \mu } } { \ni { \tilde { \mathcal { X } } } ^ { \dot { \lambda } } \ni { \tilde { \mathcal { X } } } ^ { \nu } } \right\} _ { P } = C _ { \lambda \nu } ^ { \mu } . } \end{array}
$$

把算得的这些结果代入联络变换式(1.3.6)，得到

$$
( \tilde { \cal T } _ { \mu \nu } ^ { \lambda } ) _ { P } = ( { \cal I } _ { \mu \nu } ^ { \lambda } ) _ { P } + C _ { \mu \nu } ^ { \lambda } .
$$

因此只要令 $C _ { \mu \nu } ^ { \lambda } { = } - ( {Gamma _ { \mu \nu } ^ { \lambda } } ) _ { P }$ ,（2.3.10)就得到了满足.

我们来看这定理的含意.若在坐标 $x ^ { \mu }$ 下 $P$ 点的联络为零，由(2.3.3)看出

$$
( g _ { \mu \nu , \lambda } ) _ { P } = 0 ,
$$

即在 $P$ 点附近 ${ \mathrm { d } } x ^ { \mu }$ 的二级小量可忽略的小区域内 $g _ { \mu \nu }$ 近似为常数.回忆本章 $\ S \ 2 . \ 1$ 中讲过， $g _ { \mu \nu }$ 为常数的区域是平坦的.这样导致结论：对采用对称联络的黎曼空间中的任一点 $P$ ，总可找到一组适当的坐标，使得从这组坐标看来 $P$ 点的领域是近似地平坦的.这个结论正是广义相对论的等效原理的数学基础.

# S2.4黎曼空间中的测地线
