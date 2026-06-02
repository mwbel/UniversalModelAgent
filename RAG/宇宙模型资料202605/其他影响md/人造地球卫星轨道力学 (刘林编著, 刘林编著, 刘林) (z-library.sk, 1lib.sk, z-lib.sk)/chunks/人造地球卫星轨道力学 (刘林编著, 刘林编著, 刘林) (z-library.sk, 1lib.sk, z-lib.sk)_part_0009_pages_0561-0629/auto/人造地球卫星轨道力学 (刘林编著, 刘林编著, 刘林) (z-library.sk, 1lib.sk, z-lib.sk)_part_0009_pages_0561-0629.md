<table><tr><td rowspan=6 colspan=2>8131133  E8</td><td rowspan=2 colspan=1>3</td><td></td></tr><tr><td rowspan=1 colspan=1>一840003√5955959918+8                                                                                41</td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0 271-91-6 5-21-25-61-62-31-3１01</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>心</td><td rowspan=1 colspan=1>１２３４5６７８90１２</td></tr></table>

RKF7(8）方法：

$$
\left. \begin{array} { c } { { \displaystyle x _ { n + 1 } = x _ { n } + \sum _ { \kappa = 0 } ^ { 1 0 } c _ { k } f _ { k } + { \cal O } ( h ^ { 8 } ) \ : , } } \\ { { \displaystyle \vphantom { \frac { 1 0 } { c _ { n + 1 } } } } } \\ { { \displaystyle \hat { x } _ { n + 1 } = x _ { n } + h \sum _ { k = 0 } ^ { 1 2 } \hat { c } _ { k } f _ { k } + { \cal O } ( h ^ { 8 } ) \ : , } } \end{array} \right\}
$$

$$
\left. \begin{array} { l } { { f _ { 0 } = f \left( t _ { n } , x _ { n } \right) , } } \\ { { { } } } \\ { { f _ { k } = f \bigg ( t _ { n } + \alpha _ { k } h , ~ x _ { n } + h \displaystyle \sum _ { \lambda = 0 } ^ { k - 1 } \beta _ { k \lambda } f _ { \lambda } \bigg ) , k = 1 , 2 , \cdots 1 2 \Bigg \{ } }  \end{array} \right\}
$$

截断误差为

$$
T _ { n + 1 } = { \frac { 4 1 } { 8 4 0 } } ( f _ { 0 } + f _ { 1 0 } - f _ { 1 1 } - f _ { 1 2 } ) h .
$$

各系数列于表3中.

# 3.常用的线性多步法—Adams方法和Adams-Cowell方法

对于初值问题(1),线性多步法的一般计算公式为

$$
\begin{array} { r l } { } & { \alpha _ { k } x _ { n + k } + \alpha _ { k - 1 } x _ { n + k - 1 } + \cdots + \alpha _ { 0 } x _ { n } } \\ { } & { } \\ { } & { = h ( \beta _ { k } f _ { n + k } + \beta _ { k - 1 } f _ { n + k - 1 } + \cdots + \beta _ { 0 } f _ { n } ) . } \end{array}
$$

其中 ${ a _ { i } } , { \beta _ { i } } \left( i = 0 , 1 , \cdots , k \right)$ 是与 $\pmb { \mathscr { n } }$ 无关的常数， $f _ { i } = f ( t _ { i } , x _ { i } )$ ，一般设 $\alpha _ { k } = 1$ ， $| \alpha _ { 0 } | + | \beta _ { 0 } | . > 0$ （即 $\pmb { \alpha _ { 0 } }$ 与 $\beta _ { 0 }$ 不同时为零)．上述公式表明：计算 $t _ { n + k }$ 步点上的 ${ \pmb x } _ { { \pmb n } + k }$ 值时,需要知道它前面的 $t _ { n + k - 1 } , t _ { n + k - 2 } ,$ $\cdots \ell _ { n }$ 各步点上的 $\pmb { x _ { i } }$ 值．因此，称(32)式所确定的方法为 $\pmb { k }$ 步法，当 $k = 1$ 时就是单步法，而 $k { > } 1$ 时则称多步法．又由于公式中出现的 $x _ { i } , f _ { i }$ 都是线性的，故称线性多步法．当 $\beta _ { k } = 0$ 时，公式是显式，否则为隐式.

（1）Adams显式公式和Adams隐式公式Adams显式公.式又称为Adams-Bashforth公式，隐式公式又称为Adams-Mo-:ulton 公式.

对所给的微分方程(1)两端求积分，从 $\smash { t _ { n } }$ 积分到 $t _ { n + 1 }$ 就得到等价的积分方程：

$$
x ( t _ { n + 1 } ) = x ( t _ { n } ) + \int _ { t _ { n } } ^ { t _ { n + 1 } } f ( t , x ( t ) ) d t .
$$

可用插值多项式来代替上式右端的被积函数，从而使其离散化以.得到数值公式。这里将采用牛顿后差公式，记

$$
\nabla ^ { m } f _ { n } = \sum _ { \rho \ = \ 0 } ^ { m } ( - 1 ) ^ { \rho } { \binom { m } { \rho } } f _ { n - \rho } ,
$$

$\nabla$ 即向后差分算子：

$$
\left. \begin{array} { c } { { \nabla f _ { n } = \nabla f \left( x _ { n } \right) = f \left( x _ { n } \right) - f \left( x _ { n } - h \right) , } } \\ { { \nabla ^ { 2 } f _ { n } = \nabla f \left( x _ { n } \right) - \nabla f \left( x _ { n } - h \right) } } \\ { { = f \left( x _ { n } \right) - 2 f \left( x _ { n } - h \right) + f \left( x _ { n } - 2 h \right) , } } \\ { { \ldots \ldots \ldots } } \\ { { . } } \end{array} \right\}
$$

相应的函数 $f$ 的向后插值多项式为

$$
\pmb { p } ( t ) = \sum _ { m = 0 } ^ { k } ( - 1 ) ^ { m } \binom { - s } { m } \nabla ^ { m } \pmb { f } _ { n } ,
$$

其中系数 $\binom { - s } { m }$ 又可表示为

$$
{ \binom { - s } { m } } = ( - 1 ) ^ { m } { \binom { s + m - 1 } { m } } ,
$$

于是

$$
\mathfrak { p } ( t ) = \sum _ { m = 0 } ^ { k } \binom { s + m - 1 } { m } \nabla ^ { m } \mathfrak { f } _ { n } .
$$

这里辅助变量 $\pmb { \mathscr { s } }$ 由下式定义：

$$
\mathscr { s } = \frac { t - t _ { n } } { h } ,
$$

相应地有

$$
s + 1 = \frac { t - t _ { n } } { n } + 1 = \frac { t - t _ { n - 1 } } { h } , \cdots , \ s + m - 1 = \frac { t - t _ { n - m + 1 } } { h } .
$$

将插值多项式 ${ \pmb p } ( t )$ 代入(33)式，略去中间推导过程[1]，直接给出用函数表示 (适用于电子计算机)的 $\pmb { k }$ 阶Adams-Bashforth公式：如下：

$$
\pmb { x } _ { n + 1 } = \pmb { x } _ { n } + \hbar \sum _ { i = 0 } ^ { k - 1 } \pmb { \beta } _ { k i } \pmb { f } _ { n - i } , k = 1 , 2 , \cdots ,
$$

$$
\pmb { \beta } _ { k i } = ( - 1 ) ^ { i } \sum _ { m = 1 } ^ { k - 1 } \binom { m } { i } \gamma _ { m } .
$$

其中 $\gamma _ { m }$ 满足下列递推关系：

$$
\gamma _ { m } + \frac { 1 } { 2 } \gamma _ { m - 1 } + \frac { 1 } { 3 } \gamma _ { m - 2 } + \cdots + \frac { 1 } { m + 1 } \gamma _ { 0 } = 1 .
$$

由(38)式计算 $x _ { n + 1 }$ 时,只用到前 $\pmb { k }$ 个步点 $t _ { n - k + 1 } , t _ { n - k + 2 } , \cdots , t _ { n }$ 上的 $x _ { n - k + 1 } , x _ { n - k + 2 } , \cdots , x _ { n }$ 值，故它是显式.

与上类似,可导出用函数表达的 $\pmb { k }$ 阶 Adams-Moulton 公式:

$$
x _ { n + 1 } = x _ { n } + h \sum _ { i = 0 } ^ { k - 1 } \beta _ { k i } ^ { * } f _ { n + 1 - i } , k = 1 , 2 , \cdots ,
$$

$$
\beta _ { k i } ^ { * } { = } ( - 1 ) ^ { i } \sum _ { m = i } ^ { k - 1 } \binom { m } { i } \gamma _ { m } ^ { * } .
$$

其中 $\gamma _ { m } ^ { * }$ 满足下列递推关系：

$$
\gamma _ { m } ^ { * } + \frac { 1 } { 2 } \gamma _ { m - 1 } ^ { * } + \frac { 1 } { 3 } \gamma _ { m - 2 } ^ { * } + \cdots + \frac { 1 } { m + 1 } \gamma _ { 0 } ^ { * } = \left\{ \begin{array} { l l } { { \ l } , m = 0 , } \\ { { \ l } _ { 0 , m \ne 0 } . } \end{array} \right.
$$

$\cdot \gamma _ { 0 } ^ { \ast } , \gamma _ { 1 } ^ { \ast } , \cdots , \gamma _ { m } ^ { \ast }$ 与 $\gamma _ { m }$ 之间有如下关系：

$$
\sum _ { i = 0 } ^ { m } \gamma _ { i } ^ { * } = \gamma _ { m } , m { = } 0 , 1 , 2 , \cdots .
$$

(41)式右端包含 $f _ { n + 1 } ,$ 这显然是隐式。

按(40)和(43)式，(39)和(42)式算出的 $\gamma _ { m }$ 和 $\gamma _ { m } ^ { * } , \ \beta _ { \varepsilon i }$ 和 $\beta _ { k } ^ { * }$

# 的部分数值列于表4和表5.

表5 $\gamma _ { m }$ 和值  

<table><tr><td>m</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>Ym</td><td>1</td><td>1/2</td><td>5/12</td><td>3/8</td><td>251/720</td><td>95/288</td><td>19087/60480</td></tr><tr><td></td><td>1</td><td></td><td>1</td><td>1</td><td>19</td><td>3</td><td>863</td></tr><tr><td>2</td><td></td><td>2</td><td>12</td><td>24</td><td>720</td><td>160</td><td>60480</td></tr></table>

表6 $\beta _ { k j }$ 和 $\beta _ { k i } ^ { * }$ 值  

<table><tr><td>i</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>βu</td><td>1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2β</td><td>3</td><td>11</td><td></td><td></td><td></td><td></td></tr><tr><td>12β</td><td>23</td><td>-16</td><td>5</td><td></td><td></td><td></td></tr><tr><td>244</td><td>55</td><td>159</td><td>37</td><td>19</td><td></td><td></td></tr><tr><td>720βs</td><td>1901</td><td>-2774</td><td>2616</td><td>-1274</td><td>251</td><td></td></tr><tr><td>1440βai</td><td>4277-7923</td><td></td><td>9482</td><td>-6798</td><td>2627</td><td>-475</td></tr><tr><td>：</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>B</td><td>1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2</td><td>1</td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>12*</td><td>5</td><td>8</td><td>-1</td><td></td><td></td><td></td></tr><tr><td>24β*</td><td>9</td><td>19</td><td>15</td><td>1</td><td></td><td></td></tr><tr><td>720β*</td><td>251</td><td>646</td><td>-264</td><td>106</td><td>-19</td><td></td></tr><tr><td>1440B</td><td>475</td><td>1427</td><td>-798</td><td>482</td><td>--173</td><td>27</td></tr><tr><td>：</td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Adams隐式公式常与显式公式联合使用，即由Adams显式公式提供一个零次近似值 ${ x _ { n + 1 } ^ { ( 0 ) } }$ ,再用隐式公式进行迭代来校正它，从而得到所需要的 $x _ { \Re + 1 }$ 值，这一联合使用的方法就是预估-校正法，简称PECE算法．对于天体力学和人造卫星运动问题，针对运动方程的特点，可将右函数分解为主要(即中心引力加速度)和次要(即摄动加速度)两个部分，前者是校正的主要“内容”，这种方法又称为部分预估-校正法，简称PECE\*算法.

(2）Adams-Cowell方法 Cowell方法是1910年由Co-well和Crommelin在预报哈雷彗星回归的工作中提出的{4],它是求解下列二阶方程初值问题

$$
\left. \begin{array} { l } { { \pmb { \xdot { x } } = f ( \pmb { x } , t ) , } } \\ { { \pmb { x } ( t _ { 0 } ) = x _ { 0 } , { \dot { x } ( t _ { 0 } ) = \dot { x } _ { 0 } } } } \end{array} \right\}
$$

的线性多步法。该二阶方程的特点是右函数不含 $\pmb { \dot { x } }$ ，而仅需考虑引力作用的天体力学问题正是如此。所以,Cowell方法曾是天体力学有关问题常采用的一种数值方法．在每一步计算中，只需直接给出 ${ \pmb x } _ { \pmb { \pi } }$ 而不必去算 $\dot { x } _ { n }$ ，这比将二阶方程(45)式化为一阶方程组后用Adams方法求数值解简单(费时少).

适用于初值问题(45)式的线性多步法计算公式与（32）式不同,其一般形式为

$$
\begin{array} { r l } {  { \alpha _ { k } x _ { n + k } + \alpha _ { k - 1 } x _ { n + k - 1 } + \cdots + \alpha _ { 0 } x _ { n } } } \\ & { = h ^ { 2 } ( \beta _ { k } f _ { n + k } + \beta _ { k - 1 } f _ { n + k - 1 } + \cdots + \beta _ { 0 } f _ { n } ) , } \end{array}
$$

或写成

$$
\sum _ { i \mathop { = } 0 } ^ { k } \alpha _ { i } x _ { n + i } = h ^ { 2 } \sum _ { i \mathop { = } 0 } ^ { k } \beta _ { i } f _ { n + i } .
$$

通常设 $\alpha _ { k } = 1 , | \alpha _ { 0 } | + | \beta _ { 0 } | > 0 .$

对问题(45)式的微分方程求积分，得

$$
\dot { x } ( t ) = \dot { x } ( t _ { n } ) \div \int _ { t _ { n } } ^ { t } f ( t , x ( t ) ) d t .
$$

再积分该式两端,分别从 $\pmb { t } _ { \pmb { \mathscr { n } } }$ 积到 $t _ { n + 1 }$ 和 $t _ { n }$ 积到 $t _ { n - 1 }$ 有

$$
x \left( t _ { n + 1 } \right) = x \left( t _ { n } \right) + h \dot { x } \left( t _ { n } \right) + \int _ { t _ { n } } ^ { t _ { n + 1 } } \int _ { t _ { n } } ^ { t } f \left( t , x \left( t \right) \right) d t ^ { 2 } ,
$$

$$
x ( t _ { n - 1 } ) = x ( t _ { n } ) + h \dot { x } ( t _ { n } ) - \int _ { t _ { n } } ^ { t _ { n - 1 } } \int _ { t _ { n } } ^ { t } \dot { f } ( t , x ( t ) ) d t ^ { 2 } ,
$$

由这两式即可消去 $\dot { x } ( t _ { n } )$ ,最后得一等价的积分方程,即

$$
x ( t _ { n + \mathfrak { r } } ) - 2 x ( t _ { n } ) + x ( t _ { n - 1 } )
$$

$$
= \int _ { \ell _ { n } } ^ { \ell _ { n } \circ \ell _ { 1 } } \int _ { \ell _ { n } } ^ { \ell } f ( t , x ( t ) ) d t ^ { 2 } + \int _ { \ell _ { n } } ^ { \ell _ { n } \circ \ell _ { 1 } } \int _ { \ell _ { n } } ^ { t } f ( t , x ( t ) ) d t ^ { 2 } .
$$

用插值多项式代替被积函数，即可给出离散化后的数值公式。略去推导过程，直接写出用函数表示的 $\pmb { k }$ 阶Cowell公式如下[21：

$$
\displaystyle { \alpha _ { n + 1 } - 2 x _ { n } + x _ { n - 1 } = h ^ { 2 } \sum _ { j  ~ = 0 } ^ { k - 1 } \beta _ { j } ^ { * } f _ { n + 1 - j } } ,
$$

$$
\beta _ { j } ^ { * } { = } ( - 1 ) ^ { j } \sum _ { i \ : = j } ^ { k - 1 } \binom { i } { j } c _ { i } .
$$

其中

$$
\left. \begin{array} { l } { { c _ { 0 } = 1 , } } \\ { { \displaystyle c _ { i } = - \sum _ { m = 0 } ^ { i - 1 } c _ { \scriptscriptstyle \lambda } B _ { i - m } , i = 1 , 2 , \cdots , } } \\ { { \displaystyle B _ { m } = \frac { 2 } { m + 2 } \sum _ { \scriptscriptstyle \lambda = 1 } ^ { m + 1 } \frac { 1 } { \lambda } , m = 0 , 1 , \cdots . } } \end{array} \right\}
$$

相应的Stomer公式为[21

$$
\displaystyle { \alpha _ { n + 1 } } - 2 { x _ { n } } + { x _ { n - 1 } } = h ^ { 2 } \sum _ { j ~ = 0 } ^ { k - 1 } { \beta _ { j } } { f _ { n - j } } ,
$$

$$
\beta _ { j } = ( - 1 ) ! \sum _ { i \ = j } ^ { k \ - 1 } { \binom { i } { j } } s _ { i } .
$$

其中

$$
\left. \begin{array} { l l } { { s _ { 0 } = 1 , } } \\ { { \bar { s } _ { i } = s _ { i - 1 } + c _ { i } , } } \end{array} \right\}
$$

Cowell方法即由上述Stomer公式和Cowell公式组成，前者是：显式公式，而后者是隐式公式，因此，实际引用时，先由Stomer公·式给出 ${ \pmb x } _ { { \pmb n } + 1 }$ 的零次近似，以此作为Cowell公式的迭代初值，从而求出 ${ \pmb x } _ { \pmb n + 1 }$

上述方法是通过二次差分 ${ \pmb x } _ { n + 1 } - { \pmb 2 } { \pmb x } _ { n } + { \pmb x } _ { n - 1 }$ 求出坐标的方法，.

又称为第一Cowell方法．Cowell和Crommelin还推荐了用二次和分的方法,也称为第二Cowell方法．但与第一Cowell方法相比,并无特点，反而增加计算量[5]，这里不再列出相应的计算公式. $\pmb { \chi }$ 阶Cowell公式的局部截断误差是 $O ( h ^ { k + 2 } )$ ，而Adams公式是 $O ( h ^ { k + 1 } )$ ，因此Cowell公式比同阶的Adams公式精确．但是,由于天体力学的发展,考虑的因素增多，右函数中出现 $\dot { \pmb { x } }$ ，而且即使纯引力问题，有时也要知道 $\dot { x } _ { n }$ ．人造卫星有摄星历表的计算，是两种情况兼而有之，这就有必要将Adams公式与Cowell公式联合使用.

考虑初值问题

$$
\left. \begin{array} { l } { \ddot { x } = f ( x , \dot { x } , t ) , } \\ { x ( t _ { 0 } ) = x _ { 0 } , \dot { x } ( t _ { 0 } ) = \dot { x } _ { 0 } . } \end{array} \right\}
$$

可将方程(55)看成 $\pmb { \dot { x } }$ 的一阶方程，用Adams公式计算 $\pmb { \dot { x } } _ { : }$ ，同时用Cowell公式计算 $\pmb { \mathscr { x } }$ ，这比单纯用Adams方法有效，因为Cowell公式比同阶Adams 公式精确。这种联合使用的方法，即Adams-Cowell方法，在人造卫星精密星历表计算中常被采用.

从上述介绍中可以看出,对于 $\pmb { k }$ 步法，必须知道 $\pmb { k }$ 个步点上的近似解才能向后积分，给出各步点上的数值解,因此有一个起步问题．通常采用单步法来完成，如前面介绍的RK方法或RKF方法．另一点也是显而易见的,即多步法变步长不方便,这一点后面再谈.

# 4．各种方法的比较

如何评价各种数值方法的优缺点，或者说到底选用哪一种方法好？这将涉及到具体问题和计算工具的状况等多种因素，而且不同的专家(数学家,计算机软件专家以及各个不同领域的科技工作者等)从不同的角度来看待同一问题,会有不同的结论．就动力天文以及与人造卫星定轨工作有关的各种需要而言，对数值方法的

要求,通常有下面四个方面：

（1）精度高低,即方法的局部截断误差;（2）数值稳定性，即误差累积状况，但这要排除具体问题对应的运动不稳定性；（3）方法的复杂性，包括数值计算公式和在计算机上具体实现时的繁易程度；（4）普适性，包括能否适用上述领域内的各种情况，如运动方程的不同类型，不同偏心率的轨道(大偏心率情况要求能灵活变步长）等.当然，上面四个条件也不是绝对的或孤立的，例如局部截断误差小的高阶方法数值稳定性差，因此低精度要求就不必选择高阶方法；在高精度要求下，阶不高步长就要小，这样计算步数增多，又会增大全局误差的累积等等，总之，对于一个具体问题，在选择方法时要对上述四个方面进行综合考虑，至于前面介绍的几种常用方法，从某一角度来讲，它们的优缺点是清楚的，例如隐式公式比显式公式稳定性好；在同精度条件下，多步法的步长往往比单步法长，计算右函数次数少,省机时；而单步法(如RK方法)却比多步法稳定性好，变步长灵活，起步不用借助其它方法等.

在实际工作中，可以结合具体问题的要求做一些试验性的比.较，以便选择恰当的方法，对现有方法的某些方面做些有益的改进无疑是可取的，例如文[6]和[7]对Cowell方法所做的改进，在人造卫星精密定轨和行星轨道数值积分中都取得了良好的效果。

# 5.人造卫星运动方程及其解的特点

人造卫星绕地球运动所对应的方程可写成

$$
\left. \begin{array} { c } { { \ddot { r } = F _ { 0 } + F _ { \varepsilon } , } } \\ { { F _ { i } : = \displaystyle - \frac { 1 } { r ^ { 2 } } \biggl ( \frac { r } { r } \biggr ) _ { r } F _ { \varepsilon } = F _ { \varepsilon } ( r , \dot { r } , t , \varepsilon ) , } } \end{array} \right\}
$$

其中

$$
\vert F _ { \varepsilon } \vert / \vert F _ { 0 } \vert = O ( \varepsilon ) , \varepsilon = O ( 1 0 ^ { - 3 } ) .
$$

该方程有如下几个特点：

（1）方程右函数的主要部分比摄动部分大三个量级，在采用预估-校正算法时可充分利用这一特点。

（2）仅考虑右函数的主要部分时，相应的轨道是一椭圆，读者已很清楚，它是运动不稳定的，微小的初值误差将会随时间 $\pmb { t }$ 增长，累积和扩大不可避免，它主要表现为沿迹(即运动方向)误差增长迅速，若用轨道根数来看,就是平近点角 $M$ 的误差增长显著．这是数值方法不能解决的一个运动问题.

(3）方程(56)的解是一变化椭圆，由于人造地球卫星有各种用途，相应的轨道偏心率往往较大，例如发射地球同步卫星时，其“过渡段”就是一个偏心率超过0.7的大椭圆，因此对变步长的要求很显著.

（4）由于人造卫星运动中受力情况特殊，若用轨道根数作为基本变量，相应运动方程的右函数比用坐标、速度作为基本量时复杂得多．尽管用根数时，右函数是小量，但由于存在短周期变化，右函数的各阶导数并不小，因此，积分步长增大不十分明显，从步长大小和右函数的复杂性两个方面综合起来看，还是选择坐标、速度作为基本变量优点多，运动方程的右函数简单，计算程序容易实现,计算费时少.

# 6．正规化与稳定化

关于上述第(3)个问题，尽管不必考虑卫星与地球碰撞的情况,但在轨道偏心率较大的情况下,变步长不可避免．因此，引用多步法时遇到麻烦．为此可采用正规化方法中的自变量变换

$$
d s = d t / r ^ { p } , ( 1 \leqslant p \leqslant 2 )
$$

将步长均匀化,对于人造卫星运动情况，式中的 $\pmb { p }$ 可取 $\mathbf { 3 / 2 }$ ，此时

新自变量是S．在此情况下，原运动方程（用一阶方程组来说明问题)

$$
\left. \begin{array} { l } { \displaystyle \frac { d r } { d t } { = \dot { r } } , } \\ { \displaystyle \frac { d \dot { r } } { d t } { = f ( r , \dot { r } , t ; \varepsilon ) } \Bigg ) } \end{array} \right\} .
$$

变为

$$
\left. \begin{array} { l } { \displaystyle \frac { d r } { d s } = r ^ { p } \dot { r } , } \\ { \displaystyle \frac { d \dot { r } } { d s } = r ^ { p } f ( r , \dot { r } , t ; \varepsilon ) . } \end{array} \right\}
$$

另外增加一辅助方程：

$$
\frac { d t } { d s } = r ^ { p } .
$$

在此变换下,未知函数仍然是所需要的x,,仅方程(60）右端多了一个因子r和一个计算时间t的辅助方程(61)，但带来的方便却十分明显,即步长h=h/r可以是均匀的，而无需变步长[。对于单步法，引用此变换当然毫无问题，而且可直接按原方程积分，仅步长按变换(58)自动调节，即h=rPh,h=const，此值根据具体问题选定[8]．对于多步法，采用上述变换后，仅结尾时，要借助于内插或单步法，因为不可能最后一步的s值正好对应t的终点值.不过，不作自变量变换也有这一问题，即t的终点值不在整步点上.

关于上述第(2)个问题，即稳定化问题．根据第五章\$5.4中介绍的能量积分的特点，在数值方法中也可以引用它，通过每一步提高轨道半长径a的计算精度来控制沿迹误差的增长，在一定条件下是有效的，文[9]和[10]作了详细的讨论，并附有计算结果的比较.

# 参考文献

[1］南京大学数学系计算数学专业编，常微分方程数值解法，科学出版社(1979).  
[2］P．亨利西著，包雪松等译，常微分方程离散变量方法，科学出版社(1985).  
[3] Fehlberg,E.,NASA TR R-287 (1968).  
[4] Cowell, P.H，Crommelin,A.C.D.，Appendix to GreenwichObservations for 1909,Edinburgh(1910),84.  
[5]丁华,黄天衣,天文学报,21(1980),58.  
[6] Lundberg,J.B.，IASOM 81-1 (1981)，Univ.of Texas Dept.of Aerospace Enginering.  
[7］张家祥，紫金山天文台台刊,8(1989),159.  
[8]刘林，廖新浩,人造卫星观测与研究,1988,No.1,1.  
[9]黄天衣，丁华,天文学报,22(1981),328.  
[10]刘林，廖新浩,天文学报,28(1987),215.

# 附录I 常用公式和一些基本数据

# 1．球面三角公式

正弦公式：

$$
{ \frac { \sin A } { \sin a } } { \frac { \sin B } { \sin b } } { = } { \frac { \sin C } { \sin c } } .
$$

余弦公式：

$$
\begin{array} { r l } & { \cos a = \cos b \cos c + \sin b \sin c \cos A , } \\ & { \cos A = - \cos B \cos C + \sin B \sin C \cos a . } \end{array}
$$

五元素公式：

$$
\sin a \cos B = \cos b \sin c - \sin b \cos c \cos A ,
$$

$$
\begin{array} { r } { \imath A \cos b = \cos B \sin C + \sin B \cos C \cos a , } \end{array}
$$

$$
\sin A \cos B = \cos b \sin C - \sin B \cos c \cos A .
$$

公式中的 $A , \ B , \ C$ 是球面三角形的三个角， $a , \ b , \ c$ 是相应的三个边.

# 2．贝塞耳函数 ${ \bf J } _ { n } ( n e )$

$$
\begin{array} { r l } & { \quad J _ { 1 } ( e ) = \frac { 1 } { 2 } e \bigg ( 1 - \frac { 1 } { 8 } e ^ { 2 } + \frac { 1 } { 1 9 2 } e ^ { 4 } - \frac { 1 } { 9 2 1 6 } e ^ { 6 } + \cdots \bigg ) , } \\ & { \quad J _ { 2 } ( 2 e ) = \frac { 1 } { 2 } e ^ { 2 } \bigg ( 1 - \frac { 1 } { 3 } e ^ { 2 } + \frac { 1 } { 2 4 } e ^ { 4 } - \frac { 1 } { 3 6 0 } e ^ { 6 } + \cdots \bigg ) , } \\ & { \quad J _ { 3 } ( 3 e ) = \frac { 9 } { 1 6 } e ^ { 3 } \bigg ( 1 - \frac { 9 } { 1 6 } e ^ { 2 } + \frac { 8 1 } { 6 4 0 } e ^ { 4 } - \cdots \bigg ) , } \\ & { \quad J _ { 4 } ( 4 e ) = \frac { 2 } { 3 } e ^ { 4 } \bigg ( 1 - \frac { 4 } { 5 } e ^ { 2 } + \frac { 4 } { 1 5 } e ^ { 4 } - \cdots \bigg ) , } \\ & { \quad J _ { 5 } ( 5 e ) = \frac { 6 2 5 } { 7 6 8 } e ^ { 8 } \bigg ( 1 - \frac { 2 5 } { 2 4 } e ^ { 2 } + \cdots \bigg ) , } \end{array}
$$

$$
\stackrel { * } { J } _ { 6 } ( 6 e ) = \frac { 8 1 } { 8 0 } e ^ { 6 } \biggl ( 1 - \frac { 9 } { 7 } e ^ { 2 } + \cdots \biggr ) .
$$

3.勒让德多项式 $P _ { n } ( \mu )$

$$
P _ { 2 } ( \mu ) = \frac { 3 } { 2 } \mu ^ { 2 } - \frac { 1 } { 2 } ,
$$

$$
\begin{array} { r l } & { P _ { \mathrm { C } } ( \omega ) = \frac { 3 5 } { 2 4 } a ^ { 2 } e ^ { - \frac { 1 5 } { 2 4 } \omega _ { \mathrm { L } } ^ { 2 } t } \frac { \frac { 3 } { 4 } } { 8 } , } \\ & { P _ { \mathrm { S } } ( \omega ) = \frac { 8 5 } { 8 4 } a ^ { 2 } e ^ { - \frac { 1 5 } { 2 4 } \omega _ { \mathrm { L } } ^ { 2 } t } - \frac { 1 5 } { 2 4 4 } a ^ { 2 } e ^ { - \frac { 1 5 } { 2 4 } \omega _ { \mathrm { L } } } } \\ & { P _ { \mathrm { S } } ( \omega ) = \frac { 8 5 } { 1 6 } a ^ { 2 } e ^ { - \frac { 1 5 } { 2 4 } \omega _ { \mathrm { L } } ^ { 2 } t } - \frac { 1 5 5 } { 1 6 4 } a ^ { 2 } e ^ { - \frac { 1 5 } { 2 4 } \omega _ { \mathrm { L } } } } \\ & { P _ { \mathrm { C } } ( \omega ) = \frac { \sqrt { 1 5 } } { 1 6 } a ^ { 2 } e ^ { - \frac { 1 5 } { 2 4 } \omega _ { \mathrm { L } } ^ { 2 } t } - \frac { 1 5 5 } { 1 6 4 } a ^ { 2 } e ^ { - \frac { 1 5 } { 2 4 } \omega _ { \mathrm { L } } ^ { 2 } t } - \frac { 1 5 } { 1 6 4 } a ^ { 2 } e ^ { - \frac { 1 5 } { 2 4 } \omega _ { \mathrm { L } } } } \\ & { P _ { \mathrm { C } } ( \omega ) = \frac { 4 5 } { 1 6 } a ^ { 2 } e ^ { - \frac { 1 5 } { 2 4 } \omega _ { \mathrm { L } } ^ { 2 } t } - \frac { 3 5 5 } { 1 6 4 } a ^ { 2 } e ^ { - \frac { 1 5 } { 2 4 } \omega _ { \mathrm { L } } ^ { 2 } t } - \frac { 3 5 } { 1 6 4 } a ^ { 2 } e ^ { - \frac { 1 5 } { 2 4 } \omega _ { \mathrm { L } } } } \\ &  P _ { \mathrm { C } } ( \omega ) = \frac { 4 5 } { 1 6 } a ^ { 2 } e ^ { - \frac { 1 5 } { 2 4 } \omega _ { \mathrm { L } } ^ { 2 } t } - \frac { 3 5 } { 1 6 4 } a ^ { 2 } e ^ { - \frac { 1 5 } { 2 4 } \omega _ { \mathrm { L } } ^ { 2 } t } \\ &  P _ { \mathrm { S } } ( \omega ) = \frac  1 2 1 5 \end{array}
$$

4.缔合勒让德多项式 $P _ { n } ^ { m } ( \mu )$

$$
\begin{array} { r c l } { { } } & { { } } & { { P _ { 1 } ^ { 1 } ( \mu ) = ( 1 - \mu ) ^ { 1 / 2 } , } } \\ { { } } & { { } } & { { P _ { 2 } ^ { 1 } ( \mu ) = 3 \mu ( 1 - \mu ^ { 2 } ) ^ { 1 / 2 } , } } \\ { { } } & { { } } & { { P _ { 2 } ^ { 2 } ( \mu ) = 3 ( 1 - \mu ^ { 2 } ) , } } \\ { { } } & { { } } & { { P _ { 3 } ^ { 1 } ( \mu ) = \displaystyle \biggr ( \frac { 1 5 } { 2 } \mu ^ { 2 } - \frac { 3 } { 2 } \biggr ) ( 1 - \mu ^ { 2 } ) ^ { 1 / 2 } , } } \end{array}
$$

$$
\begin{array} { l } { { { \cal P } _ { 3 } ^ { 2 } ( \mu ) = 1 5 \mu ( 1 - \mu ^ { 2 } ) , } } \\ { { { \cal P } _ { 3 } ^ { 3 } ( \mu ) = 1 5 ( 1 - \mu ^ { 2 } ) ^ { 3 / 2 } , } } \\ { { { \cal P } _ { 4 } ^ { 1 } ( \mu ) = \left( \displaystyle \frac { 3 5 } { 2 } \mu ^ { 3 } - \displaystyle \frac { 1 5 } { 2 } \mu \right) ( 1 - \mu ^ { 2 } ) ^ { 1 / 2 } , } } \\ { { { \cal P } _ { 4 } ^ { 2 } ( \mu ) = \left( \displaystyle \frac { 1 0 5 } { 2 } \mu ^ { 2 } - \displaystyle \frac { 1 5 } { 2 } \right) ( 1 - \mu ^ { 2 } ) , } } \\ { { { \cal P } _ { 3 } ^ { 3 } ( \mu ) = 1 0 5 \mu ( 1 - \mu ^ { 2 } ) ^ { 3 / 2 } , } } \\ { { { \cal P } _ { 4 } ^ { 4 } ( \mu ) = 1 0 5 ( 1 - \mu ^ { 2 } ) ^ { 2 } . } } \end{array}
$$

5.一些函数的平均值

(1) $\scriptstyle { \overline { { \left( { \frac { a } { r } } \right) } } } = 1 .$   
(2) ${ \overline { { \left( { \frac { a } { r } } \right) ^ { p } \sin q f } } } = 0 . \qquad \quad ( p , q = 0 , 1 , 2 , \cdots )$   
(3） $\stackrel { \_ } { \left( \frac { a } { r } \right) ^ { p } } { \cos q } f { = 0 } . \qquad ( p { \geq } 2 , q { \geq } p - 1 )$ $\overline { { \left( \frac { a } { r } \right) ^ { p } \cos q f } } = ( 1 - e ^ { 2 } ) ^ { - \left( p - \frac { 3 } { 2 } \right) } \sum _ { n ( 2 ) = q } ^ { ( p - 2 ) ^ { - 3 } } { \binom { p - 2 } { n } } \binom { n } { \frac { 1 } { 2 } ( p - q ) }$ $\mathbf { \nabla } \times \left( { \frac { e } { 2 } } \right) ^ { n } ,$ $\delta \mathrm { = } \frac { 1 - ( - 1 ) ^ { p - q } } { 2 } , ( p \geqslant 2 , q < p - 1 )$ $\begin{array} { l } { { { \displaystyle \left( { \frac { a } { r } } \right) ^ { 2 } = ( 1 - e ^ { 2 } ) ^ { - 1 / 2 } , } } } \\ { { { \displaystyle \left( { \frac { a } { r } } \right) ^ { 2 } \cos q f = 0 , ~ ( q \geqslant 1 ) } } } \\ { { { \displaystyle \left( { \frac { a } { r } } \right) ^ { 3 } = ( 1 - e ^ { 2 } ) ^ { - 3 / 2 } , } } } \\ { { { \displaystyle \left( { \frac { a } { r } } \right) ^ { 3 } \cos f = \frac { 1 } { 2 } e ( 1 - e ^ { 2 } ) ^ { - 3 / 2 } } } } \end{array}$

$\begin{array} { r l } & { \frac { \sqrt { \pi } } { \sqrt { \frac { d } { \tau } } } \frac { \sqrt { 3 } } { \sigma \sin { q } f } = 0 , \quad ( q \widetilde { \gamma } \widetilde { \le } 2 ) } \\ & { \frac { \sqrt { \pi } } { \sqrt { \frac { d } { \tau } } } \mathrm { e } ^ { \sigma } \Big ( 1 + \frac { 1 } { 2 } \theta ^ { 2 } \Big ) ( 1 - e ^ { \sigma } ) ^ { - \sigma _ { 0 } } , } \\ & { \frac { \sqrt { \pi } } { \sqrt { \frac { d } { \tau } } } \frac { \sqrt { 3 } } { \sigma \sin { q } } = \epsilon ( 1 - e ^ { 2 } ) ^ { - \sigma _ { 0 } } , } \\ & { \frac { \sqrt { \pi } } { \sqrt { \frac { d } { \tau } } } \widetilde { < } \frac { 1 } { \sigma \sin ^ { 2 } { q } } = \frac { 1 } { 4 } a ^ { 3 } ( 1 - e ^ { 2 } ) ^ { - \sigma _ { 0 } } , } \\ & { \frac { \sqrt { \pi } } { \sqrt { \frac { d } { \tau } } } \widetilde { < } \omega \sigma q \widetilde { f } - 0 , \quad ( q \widetilde { \gamma } \widetilde { \le } 3 ) } \\ & { \frac { \sqrt { \pi } } { \sqrt { \frac { d } { \tau } } } \widetilde { < } \Big ( 1 + \frac { 3 } { 2 } \theta ^ { 4 } \Big ) ( 1 - e ^ { 2 } ) ^ { - \sigma _ { 0 } } . } \end{array}$ $\begin{array} { r l } & { \quad \times \ : \ : \mathcal { F } _ { \ell } ^ { \ell } \ : \ : \ : \mathcal { C } ^ { n } } \\ & { \quad \times \ : \left( \frac { \overline { { \alpha } } ( \theta ) } { \tau } \right) ^ { \ell } - \left( 1 + \frac { 3 } { 2 } \theta ^ { \ell } \right) ^ { n } ( 1 - \epsilon ^ { n } ) ^ { n } , } \\ & { \quad \times \ : \left( \frac { \overline { { \alpha } } ( \theta ) } { \tau } \right) ^ { \ell } \epsilon \epsilon \epsilon \epsilon - \frac { 3 } { 2 } \epsilon \int _ { \tau _ { 0 } } ^ { \tau } \left( 1 + \frac { \epsilon } { 4 } \theta ^ { \ell } \right) ^ { n } ( 1 - \epsilon ^ { n } ) ^ { n - 1 } \ : \ : \mathcal { P } ^ { n } } \\ & { \quad \times \ : \left( \frac { \overline { { \alpha } } ( \theta ) } { \tau } \right) ^ { \ell } \epsilon \epsilon \epsilon 2 \epsilon ^ { n } d ^ { \ell } - \frac { 3 } { 4 } \epsilon ^ { n } ( 1 - \epsilon ^ { n } ) ^ { n - 1 } \ : \ : \mathcal { P } ^ { n } , } \\ & { \quad \times \ : \left( \frac { \overline { { \alpha } } ( \theta ) } { \tau } \right) ^ { \ell } \epsilon \epsilon \epsilon 3 d ^ { \ell } - \frac { 1 } { 4 } \theta ^ { \ell } \epsilon ( 1 - \epsilon ^ { n } ) ^ { n - 1 } \ : \ : \mathcal { P } ^ { n } , } \\ & { \quad \times \ : \left( \frac { \overline { { \alpha } } ( \theta ) } { \tau } \right) ^ { \ell } \epsilon \epsilon \epsilon 3 d ^ { \ell } - \frac { 1 } { 8 } \theta ^ { \ell } ( 1 - \epsilon ^ { n } ) ^ { n - 1 } \ : \ : \ : \mathcal { P } ^ { n } } \\ & { \quad \times \ : \left( \frac { \overline { { \alpha } } ( \theta ) } { \tau } \right) ^ { \ell } \epsilon \omega \epsilon \epsilon ^ { n } d ^ { \ell } - 0 , \ : \ : \ : \ : \ : \ : \ : \ : \ : \ : \ : } \\ & { \quad \times \ : \left( \frac { \overline { { \alpha } } ( \theta ) } { \tau } \right) ^ { \ell } \epsilon \left( 1 + 3 \epsilon ^ { n } + \frac { \epsilon } { 8 } \epsilon ^ { n } \right) ^ { n - 1 } \ : \ : \ : \ : \times ^ { \ell } , } \\ &  \quad \times \ : \ : \alpha ^ { \ell + 1 } - \ : \ : \alpha , \ : \ : \ : \ : \times ^  \ell  \end{array}$ $\overline { { { \biggl ( \frac { a } { r } \biggr ) } ^ { 6 } \cos f } } = 2 e \biggl ( 1 + \frac { 3 } { 4 } e ^ { 2 } \biggr ) ( 1 - e ^ { 2 } ) ^ { - 9 / 2 } ,$ $\overline { { \cdot \left( \frac { a } { r } \right) ^ { 6 } \cos 2 f } } = \frac { 3 } { 2 } e ^ { 2 } \Big ( 1 + \frac { 1 } { 6 } e ^ { 2 } \Big ) ( 1 - e ^ { 2 } ) ^ { - 9 / 2 } ,$ $\stackrel { a } { \left( \frac { a } { r } \right) ^ { 6 } } \stackrel { \cos 3 f } { \cos 3 f } = \frac { 1 } { 2 } e ^ { 3 } ( 1 - e ^ { 2 } ) \stackrel { - \theta / 2 } { \cos 3 f } ,$ $\overline { { \left( \frac { a } { r } \right) ^ { 6 } \cos { 4 f } } } = \frac { 1 } { 1 6 } e ^ { 4 } ( 1 - e ^ { 2 } ) ^ { - 9 / 2 } ,$

$\left( { \frac { a } { r } } \right) ^ { 6 } \cos q f = 0 , \quad ( q \geq 5 )$ $\begin{array} { r l } & { \quad \times \ : \tau ^ { ( a ) } , } \\ & { \quad \sqrt { \frac { \alpha } { \tau ^ { 2 } } } \ : \ : \mathrm { - } \ : \left( 1 - 5 \alpha ^ { 5 } + \frac { 1 } { 4 } \frac { 1 } { 8 } \epsilon ^ { 5 } \right) ( 1 - \epsilon ^ { 4 } ) ^ { - 1 / 2 } , } \\ & { \quad \times \ : \left( \frac { \alpha } { \tau ^ { 3 } } \right) ^ { - 1 } \ : \mathrm { - } \left( 1 - 5 \alpha ^ { 5 } + \frac { 1 } { 8 } \epsilon ^ { 5 } \right) ( 1 - \epsilon ^ { 4 } ) ^ { - 1 / 2 } , } \\ & { \quad \times \ : \left( \frac { \alpha } { \tau ^ { 4 } } \right) ^ { - 1 / 2 } \ : \mathrm { e x c } _ { 2 } \ : - \frac { 5 } { 2 } \epsilon _ { 1 } ^ { 5 } ( 1 + \frac { 3 } { 2 } \epsilon ^ { 5 } + \frac { 1 } { 8 } \epsilon ^ { 5 } ) ( 1 - \epsilon ^ { 4 } ) ^ { - 1 / 3 } , } \\ & { \quad \times \ : \left( \frac { \alpha \sqrt { 3 } } { \tau ^ { 5 } } \right) ^ { - 1 / 2 } \ : \mathrm { e x c } _ { 2 } \ : - \frac { 3 } { 2 } \epsilon _ { 1 } ^ { 5 } ( 1 + \frac { 1 } { 2 } \epsilon ^ { 5 } ) \ : [ 1 - \epsilon ^ { 4 } ) ^ { - 3 / 3 } \tau ^ { ( 2 ) } , } \\ & { \quad \times \ : \left( \frac { \alpha } { \tau ^ { 5 } } \right) ^ { - 1 / 2 } \ : \mathrm { e x c } _ { 3 } \ : - \ : \frac { 5 } { 4 } \epsilon ^ { 5 } \left( 1 + \frac { 1 } { 8 } \epsilon ^ { 5 } \right) ( 1 - \epsilon ^ { 4 } ) ^ { - 1 / 2 } \cdots \ : \mathrm { e x c } _ { 2 } , } \\ & { \quad \times \ : \left( \frac { \alpha } { \tau ^ { 7 } } \right) ^ { - 1 / 2 } \ : \mathrm { e x c } _ { 4 } \ : - \ : \frac { 5 } { 1 6 } \epsilon ^ { 5 } ( 1 - \epsilon ^ { 6 } ) ^ { - 1 / 3 } \tau ^ { ( 2 ) } , } \\ &  \quad \times \ : \left( \frac { \alpha } { \tau ^ { 7 } } \right) ^ { - 1 / 2 } \ : \mathrm { e x c } _ { 2 } \ : - \ : \frac { 5 } { 1 6 } \epsilon ^ { 5 } ( 1 - \epsilon ^ { 5 } ) ^  - 1 /  \end{array}$ $\begin{array} { r l } & { \sqrt { \pi } \int ^ { 1 } \ d \mathbf { r } \cdot \hat { \mathbf { \xi } } ( \mathbf { \theta } ) , \quad \mathbf { \xi } ( \mathbf { \theta } ^ { \sharp } \times \sqrt { \pi } ) ^ { \vee } = \frac { \pi ^ { \vee } } { 1 } \left. \mathbf { \xi } \cdot \hat { \mathbf { \xi } } ( \mathbf { \theta } ) ^ { \vee } ( \mathbf { \theta } ) \cdot \mathbf { \xi } ( \mathbf { \theta } ^ { \vee } ) \cdot \mathbf { \xi } ( \mathbf { \theta } ^ { \vee } ) \cdot \mathbf { \xi } ( \mathbf { \theta } ^ { \vee } ) \cdot \mathbf { \xi } ( \mathbf { \theta } ^ { \vee } ) \cdot \mathbf { \xi } ( \mathbf { \theta } ^ { \vee } ) \cdot \mathbf { \xi } ( \mathbf { \theta } ^ { \vee } ) \right. , } \\ & { \sqrt { \frac { \pi ^ { \vee } } { \gamma } } \left. \frac { \pi ^ { \vee } } { 1 } \right. ^ { \vee } \cos \xi \left( \frac { 1 } { 3 2 } \right) e ^ { s } ( 1 - e ^ { s } ) ^ { s } \left. 1 - e ^ { s } \right. ^ { - 1 / 3 / 2 } , } \\ & { \sqrt { \frac { \pi ^ { \vee } } { \gamma } } \left. \frac { \pi ^ { \vee } } { 1 } \right. ^ { \vee } = \sin \left( \eta \left( \frac { 1 } { 3 2 } \right) e ^ { s } ( 1 - e ^ { s } ) \right. } \\ & { \left( \frac { \pi ^ { \vee } } { \gamma } \right) ^ { \vee } = \left. 1 - \frac { 1 5 } { 2 } e ^ { 2 } - \frac { 4 5 } { 8 } e ^ { s } + \frac { 5 } { 1 6 } e ^ { s } \right. ( 1 - e ^ { s } ) ^ { - 1 / 3 / 2 } , } \\ & { \sqrt { \frac { \pi ^ { \vee } } { \gamma } } ^ { \vee } \cos \gamma - 3 e \left( 1 + \frac { 5 } { 2 } e ^ { 2 } + \frac { 5 } { 8 } e ^ { s } \right) ( 1 - e ^ { s } ) ^ { - 1 / 3 / 2 } , } \end{array}$ $\overline { { { \biggl ( \frac { a } { r } \biggr ) } ^ { 8 } \cos 2 f } } = \frac { 1 5 } { 4 } e ^ { 2 } \biggl ( 1 + e ^ { 2 } + \frac { 1 } { 1 6 } e ^ { 4 } \biggr ) ( 1 - e ^ { 2 } ) ^ { - 1 3 / 2 } ,$ ${ \begin{array} { r l } & { \left( { \frac { u } { r } } \right) \cos 3 f = { \frac { \sin } { 2 } } e ^ { 3 } \left( 1 + { \frac { \cdot { \frac { \cdot } { 8 } } } { 8 } } e ^ { 2 } \right) ( 1 - e ^ { 2 } ) ^ { 1 3 / 2 } , } \\ & { { \frac { \cdot } { \left( { \frac { a } { r } } \right) ^ { 8 } \cos 4 f } } { \frac { 1 5 } { 1 6 } } e ^ { 4 } { \Big ( } 1 + { \frac { \cdot } { 1 6 } } e ^ { 2 } { \Big ) } ( 1 - e ^ { 2 } ) ^ { - 1 3 / 2 } , } \\ & { { \frac { \cdot } { \left( { \frac { a } { r } } \right) ^ { 8 } \cos 5 f } } { \frac { 3 } { 1 6 } } e ^ { 5 } ( 1 - e ^ { 2 } ) ^ { - 1 3 / 2 } , } \\ & { { \frac { \cdot } { \left( { \frac { a } { r } } \right) ^ { 8 } \cos 6 f } } { \frac { 1 } { 6 4 } } e ^ { 6 } ( 1 - e ^ { 2 } ) ^ { - 1 3 / 2 } , } \end{array} }$ $\begin{array} { l } { { { \displaystyle \overline { { { \left( \frac { a } { r } \right) } ^ { 8 } \cos q \mathrm { { \bar { f } } } } } = 0 , \quad ( q \geqslant 7 ) } } } \\ { { { \displaystyle \overline { { { \left( \frac { a } { r } \right) } ^ { \oplus } } } = \left( 1 + \frac { 2 1 } { 2 } e ^ { 2 } + \frac { 1 0 5 } { 8 } e ^ { 4 } + \frac { 3 5 } { 1 6 } e ^ { 6 } \right) ( 1 - e ^ { 2 } ) ^ { - 1 5 / 2 } , } } } \\ { { { \displaystyle \overline { { { \left( \frac { a } { r } \right) } ^ { \oplus } \cos f } } = \frac { 7 } { 2 } e \Big ( 1 + \frac { 1 5 } { 4 } e ^ { 2 } + \frac { 1 5 } { 8 } e ^ { 4 } + \frac { 5 } { 6 4 } e ^ { 6 } \Big ) ( 1 - e ^ { 2 } ) ^ { - 1 5 / 2 } , } } } \\ { { { \displaystyle \overline { { { \left( \frac { a } { r } \right) } ^ { \oplus } \cos { 2 } f } } = \frac { 2 1 } { 4 } e ^ { 2 } \Big ( 1 + \frac { 5 } { 3 } e ^ { 2 } + \frac { 5 } { 1 6 } e ^ { 4 } \Big ) ( 1 - e ^ { 2 } ) ^ { - 1 5 / 2 } , } } } \end{array}$ $\begin{array} { r l } & { \frac { \sqrt { \pi } } { r } ~ \sqrt { \operatorname { e x g s } \eta } - \frac { 1 } { 3 2 } \mathrm { e } ^ { s } ( \lambda ^ { - \epsilon } ) ^ { - 1 } \lambda ^ { \epsilon } ~ 1 2 ^ { - s } ~ / ~ , } \\ & { \frac { \sqrt { \pi } } { r } ~ \sqrt { \operatorname { e x g s } f } - \frac { \pi } { 5 4 } \epsilon ^ { s } ( 1 - e ^ { s } ) ^ { - 1 . 5 / 2 } , } \\ & { \frac { \sqrt { \pi } } { r } ~ \sqrt { \operatorname { e x g s } f } - \frac { 1 } { 1 2 8 } \epsilon ^ { s } ( 1 - e ^ { s } ) ^ { - 1 . 5 / 2 } , } \\ & { \frac { \sqrt { \pi } } { r } ~ \sqrt { \operatorname { e x g s } \eta } ~ \sqrt { \operatorname { e x g s } \eta } ~ } \\ & { \frac { \sqrt { \pi } } { r } ~ \sqrt { \operatorname { e x g s } \eta } ~ \sqrt { q } = 0 , \quad ~ ( q \ge 8 ) } \\ & { \frac { \sqrt { \pi } } { r } ~ \sqrt { \operatorname { e x g s } \eta ^ { - 1 } } - \biggl ( 1 \cdot 1 4 e ^ { - 2 } + \frac { 1 0 5 } { 4 } e ^ { 4 } + \frac { 3 5 } { 4 } e ^ { 6 } + \frac { 3 5 } { 1 2 8 } e ^ { \kappa } \biggr ) ( 1 - e ^ { 2 } ) ^ { - 1 . 7 / 2 } , } \\ & { \frac { \sqrt { \pi } } { \epsilon } ~ \sqrt { \operatorname { e x g s } f } - 4 \epsilon \biggl ( 1 + \frac { 2 1 } { 4 } e ^ { - 4 } - \frac { 3 5 } { 8 } e ^ { 4 } + \frac { 3 5 } { 6 4 } e ^ { 6 } \biggr ) ( 1 - e ^ { 2 } ) ^ { - 1 . 7 / 2 } , } \end{array}$ $\begin{array} { r l } & { \left( \frac { a } { \tau } \right) ^ { \lambda } \cos { 3 \xi } - \frac { 3 5 } { 8 } \sigma ^ { \lambda } \Big ( 1 + \frac { 3 } { 4 } \sigma ^ { 5 } + \frac { \lambda } { 8 0 } \sigma ^ { \lambda } \Big ) ( 1 - e ^ { \lambda } ) } \\ & { \left( \frac { a } { \tau } \right) ^ { \lambda } \cos { 4 \xi } - \frac { 3 5 } { 1 6 } \sigma ^ { \lambda } \Big ( 1 + \frac { 3 } { 1 6 } \sigma ^ { \lambda } \Big ) ( 1 - e ^ { 2 } ) ^ { - 1 / \lambda / \lambda } , } \\ & { \left( \frac { a } { \tau } \right) ^ { \lambda } \cos { 5 \xi } - \frac { 2 1 } { 3 2 } \sigma ^ { \lambda } \Big ( 1 - \frac { 1 } { 1 2 } \sigma ^ { \lambda } \Big ) ^ { \lambda \alpha } , } \\ & { \left( \frac { a } { \tau } \right) ^ { \lambda } \cos { 6 \xi } - \frac { 7 } { 8 4 } e ^ { \lambda } ( 1 - e ^ { \lambda } ) ^ { - 1 / \lambda / \tau } , } \\ & { \left( \frac { a } { \tau } \right) ^ { \lambda } \cos { 7 \xi } - \frac { 1 } { 1 2 8 } e ^ { \lambda } ( 1 - e ^ { \lambda } ) ^ { - \lambda / \tau } , } \\ & { \left( \frac { a } { \tau } \right) ^ { \lambda } \cos { 9 \xi } - 0 , \quad ( 7 \xi ) ^ { \lambda } \cos { 9 \xi } } \\ & { \left( \frac { a } { \tau } \right) ^ { \lambda } \cos { 9 \xi } - 0 , } \end{array}$ $\overline { { { \left( \frac { a } { r } \right) ^ { 1 0 } \ \cos 2 f } } } = 7 e ^ { 2 } \bigg ( 1 + \frac { 5 } { 2 } e ^ { 2 } + \frac { 1 5 } { 1 6 } e ^ { 4 } + \frac { 1 } { 3 2 } e ^ { 6 } \bigg ) ( 1 - e ^ { 2 } ) ^ { - 1 7 / 2 } ,$ $\left( \frac { a } { r } \right) ^ { 1 0 } \cos 3 f = 7 e ^ { 3 } \bigg ( 1 + \frac { 5 } { 4 } e ^ { 2 } + \frac { 3 } { 1 6 } e ^ { 4 } \bigg ) ( 1 - e ^ { 2 } ) ^ { - 1 7 / 2 } ,$ $\overline { { \left( \frac { a } { r } \right) ^ { 1 0 } \cos { 4 f } } } = \frac { 3 5 } { 8 } e ^ { 4 } \bigg ( 1 + \frac { 3 } { 5 } e ^ { 2 } + \frac { 1 } { 4 0 } e ^ { 4 } \bigg ) ( 1 - e ^ { 2 } ) ^ { - 1 7 / 2 } ,$

$$
{ \begin{array} { r l } & { \left( { \frac { a } { \gamma } } \right) ^ { 1 0 } \cos { 5 f } = { \frac { 7 } { 4 } } e ^ { 8 } { \Big ( } 1 + { \frac { 1 } { 4 } } e ^ { 2 } { \Big ) } ( 1 - e ^ { 2 } ) ^ { - 1 1 / 2 } , } \\ & { \left( { \frac { a } { \gamma } } \right) ^ { 1 0 } \cos { 6 f } = { \frac { 7 } { 1 6 } } e ^ { 8 } { \Big ( } 1 + { \frac { 1 } { 1 4 } } e ^ { 2 } { \Big ) } ( 1 - e ^ { 2 } ) ^ { - 1 1 / 2 } , } \\ & { \left( { \frac { a } { \gamma } } \right) ^ { 1 0 } \cos { 7 f } = { \frac { 1 } { 1 6 } } e ^ { 7 } \left( 1 - e ^ { 2 } \right) ^ { - 1 1 / 2 } , } \\ & { \left( { \frac { a } { \gamma } } \right) ^ { 1 1 } \cos { 8 f } - { \frac { 1 } { 2 5 6 } } e ^ { 8 } { \Big ( } 1 - e ^ { 2 } { \Big ) } ^ { - 1 1 / 2 } , } \\ & { \left( { \frac { a } { \gamma } } \right) ^ { 1 0 } \cos { 9 f } = 0 . \qquad ( { g } \cos { 9 } ) } \end{array} }
$$

$$
{ \biggl ( } { \frac { a } { r } } { \biggr ) } \cos q f = \biggl ( { \frac { - e } { 1 + { \sqrt { 1 - c ^ { 2 } } } } } \biggr ) ^ { q } . \qquad ( q = 0 , 1 , 2 , \cdots )
$$

${ \overline { { \cos q f } } } = \left( { \frac { - e } { 1 + { \sqrt { 1 - e ^ { 2 } } } } } \right) ^ { q } ( 1 + { \sqrt { 1 - e ^ { 2 } } } ) \quad ( q = 0 , 1 , 2 , \cdots )$   
$\overline { { \cos f } } = - e ,$   
${ \overline { { \cos 2 f } } } = { \frac { 1 + 2 { \sqrt { 1 - e ^ { 2 } } } } { ( 1 + { \sqrt { 1 - e ^ { 2 } } } ) ^ { 2 } } } e ^ { 2 } = { \frac { 1 } { e ^ { 2 } } } { \bigg [ } 2 ( 1 - e ^ { 2 } ) ^ { 3 / 2 } \quad$ $- 2 \Bigl ( 1 - \frac { 3 } { 2 } e ^ { 2 } \Bigr ) \Biggr ] ,$   
$\overline { { \cos 3 f } } = - \frac { 4 } { e } \overline { { \cos 2 f } } + 3 e ,$   
$\overline { { \cos 4 f } } { = } \frac { 2 } { e ^ { 2 } } ( 6 - e ^ { 2 } ) \overline { { \cos 2 f } } { - } 9 ,$   
$\cos 5 f = - { \frac { 4 } { e ^ { 3 } } } ( 8 - 3 e ^ { 2 } ) { \overline { { \cos 2 f } } } + { \frac { 1 } { e } } ( 2 4 - 5 e ^ { 2 } ) ,$   
${ \overline { { \cos 6 f } } } = { \frac { 1 } { e ^ { 4 } } } ( 8 0 - 4 8 e ^ { 2 } + 3 e ^ { 4 } ) { \overline { { \cos 2 f } } } - { \frac { 2 } { e ^ { 2 } } } ( 3 0 - 1 3 e ^ { 2 } ) .$

$$
\overline { { \left( \frac { a } { r } \right) ^ { p } \left( f - M \right) \cos q f } } = 0 , \qquad \left( p , q = 0 , 1 , 2 , \cdots \right)
$$

$$
\overbrace { ( \frac { a } { r } ) ^ { 2 } ( f - M ) \sin q f } ^ { ( \frac { a } { r } ) ^ { 2 } ( f - M ) } = - \frac { 1 } { q } \overbrace { ( \frac { \cos q f } { \sqrt { 1 - e ^ { 2 } } } ) } ^ {  q f } . ( q \geqslant 1 )
$$

$\left( { \frac { a } { r } } \right) ^ { p } { \overline { { ( f - M ) \sin q f } } } = ( 1 - e ^ { 2 } ) \cdot { ( p - 3 / 2 ) } \sum _ { n = 0 } ^ { p - 2 } \sum _ { m = 0 } ^ { n } { \binom { p - 2 } { n } } { \binom { n } { m } }$ $\begin{array} { l } { { \displaystyle \times \left( \frac { e } { 2 } \right) ^ { n } \left\{ - \frac { \cos { ( q + n - 2 m ) f } } { q + n - 2 m } \right\} _ { 2 m \neq q + n } , \quad ( p \geqslant 3 , ~ q \geqslant 1 ) } } \\ { { \displaystyle \frac { \left( \frac { a } { r } \right) ^ { 3 } ( f - M ) \sin { f } } { \left( \frac { a } { r } \right) ^ { 3 } ( f - M ) \sin { f } } } { \displaystyle - \left( 1 - \frac { 1 } { 4 } \frac { \cos { 2 f } } { \cos { 2 f } } \right) } e ( 1 - e ^ { 2 } ) ^ { - 3 / 2 } , }  \\ { { \displaystyle \frac { \left( \frac { a } { r } \right) ^ { 3 } ( f - M ) \sin { 2 f } } { \left( \frac { a } { r } \right) ^ { 3 } ( f - M ) \sin { 2 f } } = \frac { 1 } { 6 } \overline { { { \cos { 2 f } } } } ( 1 - e ^ { 2 } ) ^ { - 3 / 2 } , } } \\ { { \displaystyle \overline { { { ( a \mathbf { \Psi } ) } } } ^ { \prime } \mathbb { + } _ { \ell - m + n + \infty , e } } _ { \ell } \quad , \ 1 \quad 1 \quad . . . . \int _ { c } \setminus { _ { c } \mathbf { \Psi } } _ { - 3 } , \quad . . . . }  \end{array}$ $\begin{array} { r l } & { \bigg ( \frac { a } { r } \bigg ) ^ { 8 } ( f - M ) \sin 2 f = \frac { 1 } { 6 } \cos 2 f ( 1 - e ^ { 2 } ) ^ { - 9 / 2 } , } \\ & { \bigg ( \frac { a } { r } \bigg ) ^ { 8 } ( f - M ) \sin 3 f = \bigg ( \frac { 1 } { 8 } - \frac { 1 } { 6 e ^ { 2 } } \cos 2 f \bigg ) e ( 1 - e ^ { 2 } ) ^ { - 3 / 2 } , } \\ & { \bigg ( \frac { a } { r } \bigg ) ^ { 8 } ( f - M ) \sin 4 f = \frac { 1 } { 5 } \bigg [ \bigg ( \frac { 1 } { e ^ { 2 } } - \frac { 1 } { 6 } \bigg ) \cos 2 f - \frac { 3 } { 4 } \bigg ] } \\ & { \qquad \times ( 1 - e ^ { 2 } ) ^ { - 3 / 2 } , } \\ & { \bigg ( \frac { a } { r } \bigg ) ^ { 4 } ( f - M ) \sin f = \bigg ( 1 - \frac { 1 } { 6 } \cos 2 f \bigg ) e ( 1 - e ^ { 2 } ) ^ { - 6 / 2 } , } \end{array}$ $\begin{array} { r l } & { \frac { \overline { { \binom { a } { \tau } } } ^ { 4 } ( f - \mathcal { M } ) \sin f _ { - } \left( 1 - \frac { 1 } { 6 } \cos 2 f \right) e ( 1 - e ^ { \theta } ) ^ { 2 } + ^ { \tau _ { 2 } } } { \sqrt { \frac { \binom { a } { \tau } } { \varepsilon } ( f - \mathcal { M } ) \sin 2 f } + \frac { 1 } { 1 2 } \sqrt { \frac { \binom { a } { \tau } } { \varepsilon } ( \frac { 1 } { e ^ { \theta } } - \frac { 3 } { 2 } ) \sqrt { \cos 2 f } + \frac { 2 7 } { 4 } } } } \\ & { \frac { \overline { { \binom { a } { \tau } } } ^ { 4 } ( f - \mathcal { M } ) \sin 2 f _ { - } \frac { 1 } { 1 2 } \Big [ \Big ( \frac { 1 } { e ^ { \theta } } ^ { 2 } - \frac { 3 } { 2 } \Big ) \overline { { \cos 2 f } } + \frac { 2 7 } { 4 } \Big ] } { \sin 2 \theta } } \\ & { \frac { \overline { { \binom { a } { \tau } } } ^ { 4 } ( f - \mathcal { M } ) \sin 3 f _ { - } \frac { 1 } { 1 2 } \Big [ \Big ( 1 - \frac { 1 } { e ^ { \theta } } \Big ) ^ { 2 } \cos 2 f _ { + } + \frac { 3 } { 4 } \Big ] } { \sin 2 \theta } } \\ & { \frac { \overline { { \binom { a } { \tau } } } ^ { 8 } ( f - \mathcal { M } ) \cos 2 f _ { - } } { \cos 2 \theta } . } \end{array}$

$$
\begin{array} { r l } & { \frac { \sqrt { \alpha } } { \sqrt { \alpha } } \left( \mathcal { f } - \mathcal { M } \right) \sin 2 \phi - \frac { 1 } { 2 } \Bigg [ \sqrt { \alpha } \left( 1 - \frac { \sigma ^ { 2 } } { e ^ { 2 } } \right) ^ { - \alpha } \frac { 3 } { 4 } \Bigg ] } \\ & { \qquad \quad \times \exp \left( 1 - e ^ { 2 } \right) ^ { - \alpha } \mathcal { R } , } \\ & { \frac { \sqrt { \alpha } } { \sqrt { \alpha } } \Bigg [ \frac { \mathcal { F } } { \alpha } \Bigg ] ^ { - \alpha } \cos 2 \phi , } \\ & { \frac { \sqrt { \alpha } } { \Bigg ( \frac { \mathcal { F } } { \alpha } \Bigg ) } = 1 - \frac { 1 } { 2 } e ^ { 2 } , } \\ & { \frac { \Bigg ( \frac { \mathcal { F } } { \alpha } \Bigg ) \cos 2 \phi - 2 } { \alpha } = - \frac { 3 } { 2 } e , } \\ & { \frac { \Bigg ( \mathcal { F } } { \alpha } \Bigg ) \cos 2 \phi - \frac { 3 } { 2 } e ^ { 3 } , } \end{array}
$$

（10)

${ \hat { \left( { \frac { r } { a } } \right) } } ^ { 2 } = 1 + { \frac { 3 } { 2 } } e ^ { 2 } ,$   
${ \overline { { \left( { \frac { r } { a } } \right) ^ { 2 } \cos f } } } = - 2 e { \left( 1 + { \frac { 1 } { 4 } } e ^ { 2 } \right) } .$   
$\overline { { { \left( \frac { r } { a } \right) ^ { 2 } \cos 2 f } } } = \frac { \bar { \bf 5 } } { 2 } e ^ { 2 } ,$   
$( \frac { r } { a } ) ^ { 2 } \cos 3 f = - \frac { 5 } { 2 } e ^ { 3 } ,$   
） =1+3e²+ 8 e 4   
（=1+5e2+ 15 e   
$\displaystyle { \overline { { { \left( \frac { r } { a } \right) } ^ { 5 } } } = 1 + \frac { 1 5 } { 2 } e ^ { 2 } + \frac { 4 5 } { 8 } e ^ { 4 } + \frac { 5 } { 1 6 } e ^ { 6 } } ,$   
$\overline { { { \left( \frac { r } { a } \right) ^ { 6 } } } } = 1 + \frac { 2 1 } { 2 } e ^ { 2 } + \frac { 1 0 5 } { 8 } e ^ { 4 } + \frac { 3 5 } { 1 6 } e ^ { 6 } .$

6.汉森系数 Xpm(e) (n=0,±1,±2,…;m=0,1,2,…)$\begin{array} { r c l } { { } } & { { } } & { { X _ { 2 } ^ { n , 0 } = \displaystyle { \frac { 1 } { 8 } } n ( n - 3 ) e ^ { 2 } + \displaystyle { \frac { 1 } { 9 6 } } n ( n ^ { n } - 6 n ^ { 2 } - n + 2 2 ) e ^ { 4 } + \cdots , } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { X _ { 3 } ^ { n , 0 } = - \displaystyle { \frac { 1 } { 4 8 } } n ( n ^ { 2 } - 9 n + 1 7 ) e ^ { 3 } - \cdots , } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { X _ { 4 } ^ { n , 0 } = \displaystyle { \frac { 1 } { 3 8 4 } } n ( n ^ { 3 } - 1 8 n ^ { 2 } + 9 5 n - 1 4 2 ) e ^ { 4 } + \cdots , } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { X _ { - 3 } ^ { n , 1 } = \displaystyle { \frac { 1 } { 3 8 4 } } ( n ^ { 4 } - 1 0 n ^ { 3 } + 1 7 n ^ { 2 } + 2 8 n - 2 7 ) e ^ { 4 } + \cdots , } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { X _ { - 2 } ^ { n , 1 } = - \displaystyle { \frac { 1 } { 4 8 } } ( n ^ { 3 } - 3 n ^ { 2 } - 4 n + 4 ) e ^ { 3 } - \cdots , } } \end{array}$ $\begin{array} { r c l } { { } } & { { } } & { { \displaystyle X _ { 0 } ^ { * , 0 } = 1 + \frac { 1 } { 4 } n ( n + 1 ) e ^ { 2 } + \frac { 1 } { 6 4 } n ( n - 2 ) ( n ^ { 2 } - 1 ) e ^ { 4 } + \cdots , } } \\ { { } } & { { } } & { { } } \\ { { } } & { { \displaystyle X _ { 1 } ^ { * , 0 } = - \frac { 1 } { 2 } n e - \frac { 1 } { 1 6 } n ( \pi ^ { 2 } - n - 3 ) e ^ { 3 } ~ \cdots , } } \\ { { } } & { { } } & { { } } \\ { { } } & { { \displaystyle X _ { 2 } ^ { n , 0 } = \frac { 1 } { 8 } ~ n ( n - 3 ) e ^ { 2 } + \frac { 1 } { 9 6 } n ( n ^ { 3 } - 6 n ^ { 2 } - n + 2 2 ) e ^ { 4 } + \cdots , } } \\ { { } } & { { } } & { { } } \\ { { } } & { { \displaystyle X _ { 3 } ^ { * , 0 } = - \frac { 1 } { 4 8 } n ( n ^ { 2 } - 9 n + 1 7 ) e ^ { 3 } - \cdots , } } \\ { { } } & { { } } & { { } } \\ { { } } & { { \displaystyle X _ { 4 } ^ { n , 0 } = \frac { 1 } { 3 8 4 } n ( n ^ { 3 } - 1 8 n ^ { 2 } + 9 5 n - 1 4 2 ) e ^ { 4 } + \cdots , } } \end{array}$

$$
\begin{array} { l } { { { \displaystyle X _ { - 1 } ^ { n , 1 } = \frac { 1 } { 8 } \left( n ^ { 2 } + n - 1 \right) e ^ { 2 } + \frac { 1 } { 9 6 } \left( n ^ { 4 } - 2 n ^ { 3 } - 4 n ^ { 2 } + 7 n + 2 \right) e ^ { 4 } + \cdots , } } } \\ { { \ } } \\ { { { \displaystyle X _ { 0 } ^ { n , 1 } = - \frac { 1 } { 2 } \left( n + 2 \right) e - \frac { 1 } { 1 6 } n ( n - 1 ) \left( n + 2 \right) e ^ { 3 } - \cdots , } } } \\ { { { \displaystyle X _ { 1 } ^ { n , 1 } = 1 + \frac { 1 } { 4 } \left( n ^ { 2 } + n - 4 \right) e ^ { 2 } + \frac { 1 } { 6 4 } \left( n ^ { 4 } - 2 n ^ { 3 } - 9 n ^ { 2 } + 2 n + 3 \right) e ^ { 4 } } } } \\ { { \ ~ + \cdots , } } \\ { { { \displaystyle X _ { 2 } ^ { n , 1 } = - \frac { 1 } { 2 } \left( n - 2 \right) e - \frac { 1 } { 1 6 } \left( n ^ { 3 } - 3 n ^ { 2 } - 1 2 n + 2 0 \right) e ^ { 3 } - \cdots , } } } \end{array}
$$

$$
\begin{array} { c } { { \displaystyle x _ { 2 } ^ { n , 1 } = - \frac 1 2 ( n - 2 ) e - \frac 1 { 1 6 } ( n ^ { 3 } - 3 n ^ { 2 } - 1 2 n + 2 0 ) e ^ { 3 } - \cdots , } } \\ { { \displaystyle X _ { 3 } ^ { n , 1 } = \frac 1 8 ( n ^ { 2 } - 7 n + 9 ) e ^ { 2 } + \frac 1 { 9 6 } ( n ^ { 4 } - 1 0 n ^ { 3 } + 2 n ^ { 2 } + 1 3 3 n - 1 6 2 ) e ^ { 4 } } } \\ { { \displaystyle + \cdots , } } \end{array}
$$

$$
X _ { 4 } ^ { n , 1 } = - { \frac { 1 } { 4 8 } } ( n ^ { 3 } - 1 5 n ^ { 2 } + 6 2 n - 6 4 ) e ^ { 3 } - \cdots ,
$$

$$
X _ { 5 } ^ { n , 1 } = \frac { 1 } { 3 8 4 } ( n ^ { 4 } - 2 6 n ^ { 3 } + 2 2 1 n ^ { 2 } - 6 9 6 n + 6 2 5 ) e ^ { 4 } + \cdots ,
$$

$$
\begin{array} { l } { { \displaystyle \vphantom { \displaystyle \frac { \partial } { \partial } } \overline { { { \displaystyle \lambda } } } ^ { n - } = \overline { { { \displaystyle \frac { 1 } { 3 } } } } ( n ^ { s } - 2 6 n ^ { s } + 2 2 1 n ^ { s } - 6 9 6 n + 6 2 5 ) e ^ { s } + \cdots , } } \\ { ~ } \\ { { \displaystyle \vphantom { \displaystyle \frac { 1 } { 3 } } X _ { - 2 } ^ { n , 2 } = \overline { { { \displaystyle \frac { 1 } { 3 8 4 } } } } ( n ^ { s } - 2 n ^ { s } - 1 3 n ^ { 2 } + 6 n + 1 6 ) e ^ { 4 } + \cdots , } } \\ { { \displaystyle \vphantom { \displaystyle \frac { 1 } { 3 } } } } \\ { { \displaystyle \vphantom { \displaystyle \frac { 1 } { 3 } } X _ { - 1 } ^ { n , 2 } = - \overline { { { \displaystyle \frac { 1 } { 4 8 } } } } ( n ^ { s } + 3 n ^ { 2 } - n - 4 ) e ^ { 3 } , } } \\ { { \displaystyle \vphantom { \displaystyle \frac { 1 } { 3 } } } } \\ { { \displaystyle \vphantom { \displaystyle \frac { 1 } { 3 } } X _ { 0 } ^ { n , 2 } = \overline { { { \displaystyle \frac { 1 } { 8 } } } } ( n + 2 ) ( n + 3 ) e ^ { 2 } + \frac { 1 } { 9 6 } ( n - 1 ) \left( n - 2 \right) ( n + 2 ) ( n + 3 ) e ^ { 6 } } } \end{array}
$$

$$
X _ { 1 } ^ { n , 2 } = - { \frac { 1 } { 2 } } ( n + 4 ) e - { \frac { 1 } { 1 6 } } ( n ^ { 3 } + 3 n ^ { 2 } - 9 n - 2 8 ) e ^ { 3 } - \cdots ,
$$

$$
\begin{array} { c } { { \displaystyle - \frac { 1 } { \imath } \qquad 2 \cdots \qquad 1 6 ^ { \imath \times \quad 1 } } } \\ { { \displaystyle } } \\ { { \displaystyle } X _ { 2 } ^ { n , 2 } = 1 + \frac { 1 } { 4 } \left( n ^ { 2 } + n - 1 6 \right) e ^ { 2 } + \frac { 1 } { 6 4 } ( n ^ { 4 } - 2 n ^ { 3 } - 3 3 n ^ { 2 } + 2 n + 2 2 0 ) }  \\ { { \displaystyle \qquad \times e ^ { 4 } + \cdots , } } \\ { { \displaystyle } X _ { 3 } ^ { n , 2 } = - \frac { 1 } { 2 } ( n - 4 ) e - \frac { 1 } { 1 6 } ( n ^ { 3 } - 5 n ^ { 2 } - 2 9 n + 1 0 8 ) e ^ { 3 } - \cdots , }  \end{array}
$$

$$
X _ { 4 } ^ { n , 2 } = \frac { 1 } { 8 } \left( n ^ { 2 } - 1 1 n + 2 6 \right) e ^ { 2 } + \frac { 1 } { 9 6 } ( n ^ { 4 } - 1 4 n ^ { 3 } + 5 n ^ { 2 } + 4 3 6 n
$$

$$
\begin{array} { r l } & { \quad , } \\ & { \quad \quad \quad \lambda ^ { * } = - { \frac { 1 } { 3 8 } } ( \mathbf { x } ^ { 8 } - \mathbf { y } \mathbf { x } ^ { 8 } ) \mathbf { e } ^ { \lambda } - 1 8 2 8 8 \mathbf { i } + 2 7 6 8 \mathbf { i } + 2 7 6 5 ) \mathbf { e } ^ { \lambda } + \cdots , } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ &  \end{array}
$$$$
X _ { 3 } ^ { n , 3 } = 1 + { \frac { 1 } { 4 } } \left( n ^ { 2 } + n - 3 6 \right) e ^ { 2 } + { \frac { 1 } { 6 4 } } ( n ^ { 4 } - 2 n ^ { 3 } - 7 3 n ^ { 2 } + 2 n + 1 2 1 5 )
$$

$$
X _ { 4 } ^ { n , 3 } = - { \frac { 1 } { 2 } } \left( n - 6 \right) e - { \frac { 1 } { 1 6 } } \left( n ^ { 3 } - 7 n ^ { 2 } - 5 4 n + 3 1 2 \right) e ^ { 3 } - \cdots ,
$$

$$
X _ { 5 } ^ { n , 3 } = { \frac { 1 } { 8 } } \left( n ^ { 2 } - 1 5 n + 5 1 \right) e ^ { 2 } + { \frac { 1 } { 9 6 } } ( n ^ { 4 } - 1 \dot { 8 } n ^ { 3 } + 8 n ^ { 2 } + 1 0 2 7 n
$$

$$
- 3 5 5 8 ) e ^ { 4 } + \cdots ,
$$

$$
\begin{array} { l } { { \displaystyle X _ { 6 } ^ { n , 3 } = - \frac { 1 } { 4 8 } ( n ^ { 3 } - 2 7 n ^ { 2 } + 2 2 4 n - 5 6 4 ) e ^ { 3 } - \cdots , } } \\ { { \mathrm { } } } \\ { { \displaystyle X _ { 7 } ^ { n , 3 } = \frac { 1 } { 3 8 4 } ( n ^ { 4 } - 4 2 n ^ { 3 } + 6 1 7 n ^ { 2 } - 3 7 2 4 n + 7 7 0 1 ) e ^ { 4 } + \cdots , } } \\ { { \mathrm { } } } \\ { { \displaystyle X _ { 0 } ^ { n , 4 } = \frac { 1 } { 3 8 4 } ( n + 2 ) \left( n + 3 \right) \left( n + 4 \right) \left( n + 5 \right) e ^ { 4 } + \cdots , } } \end{array}
$$

$$
X _ { 1 } ^ { n , 4 } = - { \frac { 1 } { 4 8 } } ( n ^ { 3 } + 1 5 n ^ { 2 } + 7 7 n + 1 3 6 ) e ^ { 3 } - \cdots ,
$$

$$
X _ { 2 } ^ { n , 4 } = \frac { 1 } { 8 } \ \left( n ^ { 2 } + 1 3 n + 4 4 \right) e ^ { 2 } + \frac { 1 } { 9 6 } \left( n ^ { 4 } + 1 0 n ^ { 8 } - 1 3 n ^ { 2 } - 4 2 2 n \right.
$$

$$
- 1 1 9 2 ) e ^ { 4 } + \cdots ,
$$

$$
X _ { 3 } ^ { n , 4 } = - { \frac { 1 } { 2 } } ( n + 8 ) e - { \frac { 1 } { 1 6 } } ( n ^ { 3 } + 7 n ^ { 2 } - 4 7 n - 3 6 0 ) e ^ { 3 } - \cdots ,
$$

$$
\begin{array} { c } { { X _ { 4 } ^ { n , 4 } = 1 + \displaystyle \frac { 1 } { 4 } ( n ^ { 2 } + n - 6 4 ) + \displaystyle \frac { 1 } { 6 4 } ( n ^ { 4 } - 2 n ^ { 8 } - 1 2 9 n ^ { 2 } + 2 n + 3 9 5 2 ) } } \\ { { \times e ^ { 4 } + \cdots , } } \end{array}
$$

$$
\begin{array} { l } { { { \cal X } _ { 8 } ^ { n , 4 } = - \displaystyle \frac { 1 } { 2 } ( n - 8 ) e - \displaystyle \frac { 1 } { 1 6 } ( n ^ { 8 } - 9 n ^ { 2 } - 8 7 n + 6 8 0 ) e ^ { 3 } - \cdots , } } \\ { { } } \\ { { { \cal X } _ { 8 } ^ { n , 4 } = \displaystyle \frac { 1 } { 8 } ( n ^ { 2 } - 1 9 n + 8 4 ) e ^ { 2 } + \displaystyle \frac { 1 } { 9 6 } ( n ^ { 4 } - 2 2 n ^ { 3 } + 1 1 n ^ { 2 } + 2 0 0 2 n  } } \\ { { } } \\ { { \displaystyle \qquad - 9 0 4 8 ) e ^ { 4 } + \cdots , } } \\ { { { \cal X } _ { 7 } ^ { n , 4 } = - \displaystyle \frac { 1 } { 4 8 } ( n ^ { 8 } - 3 3 n ^ { 2 } + 3 4 1 n - 1 0 9 6 ) e ^ { 3 } - \cdots , } } \\ { { { \cal X } _ { 8 } ^ { n , 4 } = \displaystyle \frac { 1 } { 3 8 4 } ( n ^ { 4 } - 5 0 n ^ { 3 } + 8 8 7 n ^ { 2 } - 6 5 8 2 n + 1 7 1 2 8 ) e ^ { 4 } + \cdots . } } \end{array}
$$

# 7．地球引力场模型

$$
V = \frac { G M } { r } \Bigg [ 1 + \sum _ { n > 2 } \sum _ { m = 0 } ^ { n } \Bigg ( \frac { a _ { e } } { r } \Bigg ) ^ { n } \bar { P } _ { n } ^ { m } . ( \sin \varphi ) ( C _ { n , m } \cos m \lambda + \delta _ { n , m }
$$

sinm)],

$$
\begin{array} { l } { \displaystyle \overline { { P } } _ { n } ^ { m } ( \sin \varphi ) = P _ { n } ^ { m } ( \sin \varphi ) / N _ { n } ^ { m } , } \\ { \displaystyle F _ { n } ^ { m } ( \sin \varphi ) = ( 1 - \sin ^ { 2 } \varphi ) ^ { m / 2 } \frac { d ^ { m } P _ { n } ( \sin \varphi ) } { d \sin \varphi ^ { m } } , } \\ { \displaystyle P _ { n } ( \sin \varphi ) = \frac { 1 } { 2 ^ { n } n ! } \frac { d ^ { n } } { d \sin \varphi ^ { n } } [ ( \sin ^ { 2 } \varphi - 1 ) ^ { n } ] , } \end{array}
$$

$$
C _ { n } , _ { m } { = } A _ { n } , _ { m } N _ { n } ^ { m } , ~ S _ { n } , _ { m } { = } B _ { n } , _ { m } N _ { n } ^ { m } ,
$$

$$
N _ { n } ^ { m } { = } \biggl [ \frac { \left( n + m \right) \varsigma } { \left( 2 n + 1 \right) \left( n - m \right) \varsigma } \delta \biggr ] ^ { 1 / 2 } ,
$$

$$
\delta = \left\{ { \displaystyle { 1 , ~ m = 0 } } , \right.
$$

(1) SAO-III(1973)   
$G M = 3 . 9 8 6 0 1 3 \times 1 0 ^ { 5 } \mathrm { k m } ^ { 3 } \cdot \mathrm { s } ^ { - 2 } , ~ a _ { e } = 6 3 7 8 . 1 4 0 \mathrm { k m } .$ (2）GEM-L2(1982)   
$G M = 3 . 9 8 6 0 0 4 4 \times 1 0 ^ { 5 } \ \mathrm { k m ^ { 3 } \cdot s ^ { - 2 } } , a _ { e } = 6 3 7 8 . 1 4 5 \ \mathrm { k m } .$ (3)GEM-T1(1987)   
$G M = 3 . 9 8 6 0 0 4 4 \times 1 0 ^ { 5 } ~ \mathrm { k m ^ { 3 } \cdot { s ^ { - 2 } } } , ~ a _ { e } = 6 3 7 8 . 1 4 5 ~ \mathrm { k m } .$

三种模型的引力场系数 $C _ { n } , \ldots$ 和 $\delta _ { n , m }$ 分别列于下面三个表中，

SAO-III

n m $\mathbf { C _ { n m } }$   
2 0 -4.84170E-04   
3 0 9.60408E -07   
4 0 5.39333E-07   
5 0 6.87446E-08   
6 0 -1.53097E --07   
7 0 9.08860E-08   
8 0 4.97198E-08   
9 0 3.53300E-08   
10 0 5.17176E-08   
11 0 -6.50565E-08   
12 0 3.84000E-08   
13 0 6.52406E-08   
14 0 -1.94980 E -08   
15 0 -1.88586E-08   
16 0 -5.91864E-09   
17 0 3.71868E-08   
18 0 1.67687E-08   
19 0 -1.58527E-08   
20 0 1.85847E -- 08   
21 0 1.26574E -08   
22 0 -1.37146E-08   
n m Cnm   
35 0 1.59029E-08   
36 0 -2.32912E-08   
2 2 2.37990E -06   
3 1 1.99770E -- 06   
3 2 7.78300E-07   
.3 3 4.90110E-07   
4 1 -5.17480E-07   
4 2 3.42960E-07   
4 3 1.03900E-06   
4 4 -1.05120E-07   
.5 1 -5.36670E-08   
.5 2 5.98690E-- 07   
5 3 -5.84290E-07   
5 4 -1.15830E-07   
5 5 1.39560E-07   
6 1 -7.21660E-08   
6 2 2.46700E-08   
6 3 4.41390E-09   
\`6 4 -1.00030E-08   
6 5 －1.35040E-07   
6 6 --2.91360E-07   
7 1 2.35320E-07   
7 2 2.04250E-07   
7 3 2.19940E-07   
7 4 -2.86170E-07   
7 5 3.47270E-08   
7 6 -2.74960E-07   
7 7 -2.48560E-08   
8 1 1.09460E--08   
.8 2 1.10840E-07   
8 3 -8.85780E-08   
8 4 -2.23150E-07   
8 5 .1.53180E-07

# Snm

-1.36560E-06   
2.23370E-07   
-7.55190E-07   
1.52830E-06   
-4.81400E-07   
6.71740E-07   
-1.19230E-07   
3.56610E-07   
7.99730E-08   
-3.99100E-07   
-1.63380E-07   
-4.53930E-08   
-8.68410E-07   
1.77560E-08   
-4.06540E-07   
2.90550E-08   
-3.02970E-07   
-6.09640E-07   
-2.63270E-07   
5.56340E-08   
1.73210E-07   
-3.46440E-07   
-2.77380E-07   
8.70140E--08   
8.58650E-08   
-8.89680E-09   
4.84290E-08   
1.03590E-07   
--5.07150E-08   
2.65110E-07   
8.11580E-08   
1 m Cnm Snm   
8 6 -9.75420E-08 2.80820E-07   
8 7 2.04980E-07 2.45920E-07   
8 8 1.69670E-07 9.32610E-08   
9 1 1.80990 E-07 4.10910E-08   
9 2 -2.20130E-08 2.42150E-08   
9 3 -9.92520E-08 -2.30850E- 08   
9 4 -4.08670E-03 -3.85250E-08   
9 5 -5.89570E-08 3.68340E-09   
9 6 4.88120E-08 1.11150 E-07   
9 7 1.98800E -07 -1.49780E-07   
9 8 2.35230E-07 9.63550E-- 09   
9 9 -3.45330E-08 5.95020E-08   
10 1 8.90080E-08 -6.01570E-08   
10 2 -3.72560E-08 -6.36760E-08   
10 3 11.33070E-07 -7.27280E-08   
10 4 -2.18870E-08 -7.84080E-08   
10 5 -6.15090E-09 -1.19040E-07   
10 6 -9.41420E-08 -1.17280E-08   
10 7 1.85250E-07 2.16560E-08   
10 8 1.08870E-09 7.07810E-09   
10 9 7.84730E-08 5.63810E-09   
10 10 1.33210E-07 9.88390E-08   
11 1 --1.21940E-08 7.54630 E-08   
11 2 -2.02550E-08 -6.29980E-08   
11 3 -1.09880E-09 -3.80980E-08   
11 4 1.56760E-08 -1.95510E-07   
11 5 -1.85910E-09 6.11130E-08   
11 6 6.36010E-08 -2.64570E-08   
11 7 -3.37610E-08 -1.28250E-07   
11 8 -1.36340E-08 4.52290E-08   
11 9 2.12560E-08 6.67210E-08   
11 10 5.25550E-08 -7.74010E-08   
11 11 8.69960E-08 -2.56910E-08   
Cnm   
-5.69350E-08   
-9.74240E-08   
1.15550E-07   
-5.03790E-08   
8.18340E-08   
-2.11770E - 08   
2.97510E-08   
4.01900E-08   
-1.15030E-07   
-4.59210E-08   
-7.84430E-09   
-2.76170E-08   
8.61360E-09   
-1.06790E-08   
-3.23610E-08   
3.98520E-08.   
4.00470E-08   
-2.19060E-08   
-7.69330E-08   
-2.74480E-09   
-1.15880E-08   
4.19790E-09   
-5.43810E-08   
-4.66330E-08   
-6.89440E-08   
-1.43590E-08   
-1.59080E-08   
9.69150E-08   
-2.98640E-08   
-1.38280E-09   
-1.38720E-08   
7.10560E-08   
-1.87790E-08   
Unm   
-6.61590E-08   
4.63410E-08   
-4.86660E-08   
5.35680E -- 08   
2.79320E-08   
3.50340E-08   
3.17830E-08   
5.68770E-08   
1.45080E-08   
-4.32640E-08   
-4.78580E-08   
-1.68080E-08   
-3.24010E-08   
-9.06700E-08   
4.92860E-08   
-1.06080E-07   
3.81140E-08   
-1.13210E-08   
1.11400E-08   
1.43090E-08   
7.29890E-08   
7.67690E-09   
1.34500E-08   
7.99630E--08   
7.18910E-08   
5.23900E-08   
2.73740E-08   
-2.56310E-08   
-3.81890E-09   
-5.86800E-08   
-2.79760E-08   
2.40430E-09   
-5.87500E-08   
n I   
14 9   
14 410   
14 11   
14 1   
14 1   
14 14   
15 1   
15 2   
15 3   
15 4   
15 5   
15 6   
15 7   
15 8   
15 9   
15 10   
15 11   
15 12   
15 13   
15 14   
15 15   
16 1   
16 2   
16 3   
16 4   
16 5   
16 6   
16 7   
16 8   
16 9   
1610   
16 11   
16 12   
<nm   
-2.43220E--08   
2.89850E-- 08   
8.26110E--08   
1.17510E -- 09   
3.07930E-08   
-6.59690E-08   
2.93580E-08   
-1.22910E-08   
-5.89210E-08   
1.48760E- 08   
3.68060E--08   
1.00810E-08   
3.04390E-08   
--6.88840E-08   
-4.51690E-08   
6.21260E-08   
-4.47240E-08   
-4.20250E-08   
-4.16540E-08   
9.56540E-09   
-5.63540E-08   
-9.95883E-09   
5.50860E-09   
5.41890E-08   
4.61760E-08   
-2.44320E-08   
-3.72030E-09   
-2.27940E -.09   
-1.04590E-07   
2.48450E-08   
-3.99280E- 08   
-2.08480E-08   
1.59300E-08   
Dnm   
6.04610E-08   
-3.42240E-08   
-1.96270E-09   
-3.09670E-08   
4.76200E-08   
.3.30300E-09   
-1.66910E-08   
-6.89630E-08   
4.47720E-- 08   
7.03560E--09   
-8.40510E-09   
-3.04730E-08   
1.57750E-08   
6.08080E-08   
5.55560E-08   
-7.17990E-09   
-3.43910E-09   
5.90720E-09   
-5.58920E-09   
- 2.71450E-08   
3.48950E-08   
5.41600E-08   
4.94550E-08   
5.48870E-09   
3.62700E-08   
2.96710E-08   
-2.07860E-08   
3.06090E-09   
-4.47310E-08   
-8.62620E-08   
-4.50580E-09   
2.97380E-08   
-1.27030E-08

#

# Cm

n m   
16 13   
16 14   
16 15   
16 16   
17 1   
17 2   
17 3   
17 4   
17 5   
17 6   
17 7   
17 8   
17 9   
17 10   
17 11   
17 12   
17 13   
17 14   
17 15   
17 16   
17 17   
18 1   
18 2   
18 3   
18 4   
18 5   
18 6   
18 7   
18 8   
18 9   
18 10   
18 11   
1312   
2.52800F08   
-1.48520E-08   
-7.74250E -- 08   
-1.85380E-08   
8.65930E--09   
-9.07690E-09   
-7.78640E-09   
-4.32310E- 08   
4.15130E-08   
-4.54530E -08   
1.69380E-08   
4.12310E-08   
-4.31190E-08   
-1.08440E--08   
-4.41360E -- 03   
3.16610E-08   
2.51470E-08   
-5.59450E-09   
4.91130E-08   
-2.35400E-08   
-9.01910E-08   
-2.35570E-08   
-9.42490E-09   
-3.50030E-08   
2.94330E-08   
1.75110E-09   
2.39310E-08   
-7:80400E-10   
5.38190E-C8   
-3.61200E-10   
4.21460E-08   
2.49810E-08   
-6.22420E-09   
Pnm   
6 62400E-09   
-8.17130E-09   
-2.64910E-08   
--2.23100E-08   
-4.10930E-08   
-2.72050E-08   
-1.79130E-- 08   
6.82030E-08   
-2.54530E- 08   
-1.72730E\~08   
-3.37520E - 08   
5.87920E-09   
-1.59740E-08   
5.56280E-08   
--4.31230E--09   
6.29820E-09   
9.77280E-09   
7.26040E--09   
3.19580E-08   
-1.58820E--08   
-9.47750E-09   
-7.45360E-08   
3.03530E-08   
-2.04640E-08   
-4.46720E-08   
-6.03670E--08   
-4.49660E-09   
--8.20100E--09   
-2.21060E-08   
-5.05620E-09   
7.89240E-09   
2.31830E-08   
6.60250E--09

n m Cnm Sm 1813 -2.66850E-08 --4.25000E-08 1814 9.11910E-09 -3.31290E-08 1815 -4.15210E-08 -1.76100E-03 1815 2.48500E-C8 -4.81820E-09 1817 3.53570E-08 -4.71660E-08 1818 -3.47010E-10 5.05540E-08 19 12 3.60580E-08 -3.44210E-09 1913 9.68760E-09 -6.60950E-08 1914 7.63890E-08 -2.76490E-08 20 13 2.76300E-08 3.23890E-08 2014 3.36870E-08 -6.57410E-08 2113 -1.97990E -- 08 -3.07110E-08 21 14 1.66230E-C8 8.72150E-09 2213 -7.94350E-09 4.14520E-09 2214 2.85160E-09 -4.21480E-08 2313. --1. 32360 E-08 -4.88920E-09 2314 -2.11480E-08 2.20100E-08 2414 3.46680E-09 2.29330E-08 GEM-- L2 n m Cnm Sm 2 0 -0.48416499E--03 3 0 0.95772324E-06 4 0 0.54127369E-06 5 0 0.69236593E-07 6 0 -0.15062766E-06 7 0 0.92372778E-07 8 0 0.50884647E-07 9 0 0.27692087E-07 10 0 0.53335420E-07 11 0 -0.48494249E-07 12 0 0.38518846E-07 13 0 0.42878621E-07 14 0 -0.20448167E-07

n m Cnm Sm   
15 0 0.28646209E-08   
16 0 -0.72319799E-08   
17 0 0.14859141E-07   
18 0 0.11623765E-07   
19 0 0.72981966E-09   
20 0 0.26889193E-07   
21 0 -0.17392269E-10   
22 0 -0.23942600E-08   
23 0 -0.20474702E-07   
24 0 -0.28244623E-08   
25 0 0.15136233E--08   
26 0 0.81294365E-08   
27 0 0.10966424E-07   
28 0 -0.22632916E-07   
29 0 -0.11237761E-07   
2 1 -0.10565891E-08 -0.30681926E-08   
3 1 0.20288151E-05 0.24969314E-06   
4 1 -0.53520200E-06 -0.46628996E-06   
5 1 -0.54001637E-07 -0.95101141E-07   
6 1 -0.74893262E--07 0.17733433E-07   
7 1 0.26914914E-06 0.93736114E-07   
8 1 0.23209605E-07 0.61280752E-07   
9 1 0.15542835E-06 0.17034888E-07   
10 1 0.82611211E-07 -0.13441567E-06   
11 1 0.68328346E-09 -0.13442197E-07   
12 1 -0.64614401E-07 -0.54345414E--07   
13 1 -0.35908499E-07 0.36228573E--07   
14 1 -0.17628534E-07 0.51711929E-07   
15 1 -0.17911975E-07 0.30002480E-09   
16 1 0.28985186E-07 -0.99145644E-08   
17 1 -0.87125032E-08 -0.24205535E--07   
18 1 0.26507175E-08 -0.21420443E-08   
19 1 -0.36519929E-07 -0.35115409E-08   
n m Cm Snm   
:20 1 0.56994328E-08 -0,21894988E-07   
.21 1 -0.12007749E-07 0.74136611E-08   
.22 1 0.28086387E-08 0.52357935E-08   
23 1 0.28528035E- 08 0.92717879E-- 08   
24 1 -0.68384589E-08 -0.28532732E-- 08   
25 1 0.12457864E-07 -0.52946106E-- 08   
2 2 0.24379113E-05 -0.13991847E-05   
3 2 0.90403154E-06 -0.61593532E-06   
4 2 0.35465063E-06 0.66033145E-06   
5 2 0.65096276E-06 -0.33062602E-06   
6 2 0.50277935E-07 -0.35499376E-0C   
7 2 0.33473458E-06 0.10700980E-06   
8 2 0.74218431E-07 0.48090826E-07   
9 2 0.25838855E-07 -0.31323843E-- 07   
10 2 -0.80407151E-07 -0.11701996E-- 07   
11 2 0.46158884E-07 -0.93731816E-07   
12 2 0.71497346E-08 -0.10335614E-07   
13 2 0.23181723E-07 -0.38618273E-07   
14 2 -0.31988861E -- 07 0.40649339E-07   
15 2 0.14228470E-- 07 -0.25799311E -- 07   
16 2 -0.27472114E-08 0.84067174E-08   
17 2 -0.77535724E-- 08 0.10307438E-- 07   
18 2 0.74878450E-08 0.22498685E-07   
19 2 0.11446254E-07 -0.57597861E-08   
20 2 -0.90238966E--09 0.14280905E--08   
21 2 0.16939294E-07 0.74414286E---08   
22 2 -0.77031167E-09 -0.12646391E-07   
3 3 0.72315232E-06 0.14152047E-05   
4 3 0.99324898E--06 10.20270397E-06   
5 3 -0.45002008E-06 -0.21278950E-06   
6 3 0.60303193E-07 0.17767317E-08   
7 3 0.24608728E--06 -0.21509167E·-06   
8 3 -0.55962219E-08 -0.88627793E --07   
n 1   
9 3   
10 3   
11 3   
12 3   
13 3   
14 3   
15 3   
16 3   
17 3   
18 3   
19 3   
.20 3   
21 3   
22 3   
4 4   
5 4   
6 4   
7 4   
8 4   
9 4   
10 4   
11 4   
12 4   
13 4   
14 4   
15 4   
i6 4   
17 4   
18 4   
19 4   
20 4   
21 4   
22 4   
Cnm   
- 0.15614892E--06   
-- 0.16102631E-07   
-- 0.21913063E-07   
0.66972413E-07   
--0.28251274E-07   
0.16645860E-07   
0.29496329E-07   
-0.70098249E-08   
-0.11484820E--07   
-0.42187726E-08   
0.44748290E-09   
-- 0.15513821E-07   
0.46017387E-08   
0.58099252E-09   
-0.19210158E-06   
--.0.29163106E-06   
-0.10190439E-06   
-0.28677468E-06   
--0.24414096E-06   
-0.99674125E-08   
-0.97336274E-07   
-0.44910084E--07   
-0.71821878E-07   
-0.25242520E-07   
-0.13794715E-07   
-0.44296809E-07   
0.41037879 E -- 07   
0.45013098E--08   
0.28332572E-07   
-0.32314360E-08   
-0.16644343E-08   
0.25581173E-08   
-0.78038494E-08   
Unm   
-0.99360035E-07   
-0.16890771E-06   
-0.13229365E--06   
0.30044149E-07   
0.79158862E-07   
-0.11019607E-07   
0.10467127E-07   
-0.24055485E-07   
0.96230752E-08   
-0.17317500E- 08   
0.22755622E-09   
0.92834439E-08   
0.31767916E-08   
0.10828784E-07   
0.30701141E-06   
0.49588273E-07   
--0.46823126E-06   
:- 0.12730253E-- 06   
0.74425146E-07   
0.94562515E--08   
-0.67442835E-07   
-0.59605822E-07   
-0.84051490E-08   
0.96843744E-- 08   
0.92993518E--08   
-0.68733254E-08   
0.13582423E-07   
-0.44837729E--08   
0.16890111E-07   
-0.98675494E-08   
-0.46833688E-08   
-0.29647169E-08   
0.73870996F-08   
n m Cnm Sum   
5 5 0.17799113E-06 -0.66068205E-06   
6.5 -0.26579745E-06 -0.53659438E-06   
7 .5 0.12079659E-07 0.41687479E·- 07   
8 5 -0.14702225E-07 0.80079315E-07   
9 .5 0.31383825E-08 -0.68855293E-07   
10 5 -0.62394663E-07 -0.39860491E-07   
11 5 0.47974319E-07 0.84568299E-07   
125 0.45663760E-07 0.14265395E-07   
13 5 0.75603596E--07 0.49190993E-07   
14 5 0.17611174E-07 --0.19897999E-07   
15 5 -0.10524533E-07 -0.68376411E-08   
16 5 -0.14384921E-07 0.10256253E-03   
17 5 -0.23601956E--07 0.92743247E-08   
18 5 0.12347485E-07 0.14675030E-07   
19 5 -0.89511505E-09 -0.17642279E-08   
20 5 -0.23004801E-08 0.68920126E-- 08   
6 6 0.86955820E-08 -0.23800855E-06   
7 6 -0.36045816E-06 0.15172312E-- 06   
8 6 -0.68132539E-07 0.31229768E-06   
9 6 0.47247885E-07 0.22226072E-06   
10 6 -0.33881619E-07 -0.89413762E-07   
11 6 0.43536878E-08 0.42427966E-07   
12 6 0.73521318E- 08 0.33374103E--07   
13 6 -0.36171637E--07 0.70596300E-08   
14 6 -0.21124988E-08 -0.76621331E-08   
15 6 0.27154749E-07 -0.32428131E-07   
16 6 0.31145116E-08 -0.33437527E-07   
17 6 0.26107279E-10 -0.97645602E-08   
18 6 0.16014496E-07 -0.13670500E-07   
19 6 0.43073248E-09 -0.78777246E-09   
20 6 -0.56319551E-08 0.18683889E-08   
7 7 0.91941422E-08 0.27990330E-- 07   
8 7 0.67088694E-07 0.74134522E- 07   
n m Cpm   
9 7 -0.10256007E-G6   
10 7 0.50838817E-C8   
11 7 0.14394839E-C7   
12 7 -0.99930517E-08   
13 7 -0.20162518E-08   
14 7 0.18132994E-07   
15 7 0.68653811E-07   
16 7 0.77794860E-08   
17 7 0.18370112E-07   
18 7 -0.38366910E-08   
19 7 -0.62182996E-08   
20 7 -0.97819177 E-08   
8 8 -0.12223741E-06   
9 8 0.18657978E-06   
10 8 0.40085257E--07   
11 8 0.26921099E-08   
12 8 -0.24996605E-07   
13 8 -0.25689913E-07   
14 8 -0.44939258E-07   
15 8 -0.18333334E-07   
16 8 -0.74635376E-08   
17 8 0.14226623E-07   
18 8 0.99324099E-08   
19 8 0.68591631E-08   
20 8 -0.21359961E-08   
9 9 -0.55687161E-07   
10 9 0.12350575E-06   
11 9 -0.30153596E-07   
12 9 0.43784512E-07   
13 9 0.26019565E-07   
14 9 0.42506002E-07   
15 9 0.14016229 E-07   
16 9 -0.16455937E-07   
Dnm   
-0.88682079E-07   
0.39341576E-08   
-0.83834403E--07   
0.45085896E-07   
0.20848924E-09   
-0.31495998E-07   
0.12947087E-07   
-0.25660859E-08   
0.10824189E-07   
-0.27510592E-09   
0.77566286E-08   
-0.32238800E-08   
0.12976349E-06   
-0.13139392E-07   
-0.81235671E-07   
0.22249182E-07   
0.24691798E-07   
-0.39834442E-08   
0.49416509E-08   
0.24956692E-07   
0.81057949E-08   
-0.82223187E-09   
-0.13555598E-07   
－0.18242000E-- 07   
-0.32440024E-08   
0.93967079E-07   
-0.49765398E-07   
0.34308380E-07   
0.14040972E-07   
0.42953614E-07   
0.14530220E-07   
0.42823183E-07   
-0 35206443E-07   
n m Cnm Snm   
17 9 -0.87636250E-08 -0.19846374E-07   
18 9 -0.23289774E-07 0.25315889E-07   
19 9 0.25886014E-08 0.18259766E-07   
20 9 0.55064414E-08 0.20691185E-07   
21 9 0.30424360E-08 -0.33916278E-08   
22 9 0.42224225E-08 -0.30699002E-C8   
1010 0.10890599E-06 -0.25218792E-07   
11 10 -0.60750135E-07 -0.63224712E-08   
12 10 0.69255496E-08 0.47385077E- 07   
13 10 0.31167774E-07 -0.34188735E-07   
1410 0.59215244E-07 0.10204922E-07   
15 10 0.29705625E-07 0.61080644E-08   
16 10 0.16741413E-07 0.77601092E-08   
17 10 0.12040172E-07 0.99661212E--08   
18 10 -0.31365421E--08 -0.89005661E-C8   
19 10 -0.14055606E-07 -0.84286463E-08   
2010 -0.14681371E-07 -0.95705596E-08   
21 10 -0.38852867E--09 0.20808154E-C8   
2210 0.14086401E-08 -0.21203264E-C9   
11 11 0.40035394E-07 -0.80951110E-07   
12 11 0.15927625E-07 -0.67999120E-08   
13 11 -0.43701055E-07 -0.18565207E-07   
14 11 0.17769345E-07 -0.34190132E-07   
1511 -0.10356574E-08 -0.41802835E-08   
1611 0.20365486E-07 0.11170177E-07   
1711 -0.38944618E-07 -0.19879351E-08   
18 11 -0.28750080E-08 0.17639327E-07   
1911 -0.18832417E-08 0.27206508E-07   
2011 0.10919143E-07 -0.10217501E-07   
21 11 -0.56775629E-08 -0.99381314E-08   
2211 -0.57354150E-08 -0.24021939E-07   
1212 -0.77624625E-08 -0.12435246E--07   
1312 -0.32186364E-07 0.90355728E-07   
Ⅱ m   
14 12   
15 12   
16 12   
17 12   
18 12   
.19 12   
:20 12   
21 12   
22 12   
.23 12   
.24 12   
.25 12   
131 13   
14:13   
15 13   
16.13   
17 13   
18 13   
19 13   
.20 13   
.21 13   
.22 13   
.23 13   
.24 13   
.25 13   
.26 13   
.27 13   
.28 13   
29 13   
14 14   
15 514   
1614   
1714   
nm Pnm   
0.81458245E- 08 -0.31305527E-07   
-0.33254884E-07 0.16561859E-07   
0.17429680E-07 0.94420531E-08   
0.31410965E-07 0.21548090E-07   
-0.40136097E-07 -0.24307234E-07   
－0.10205013E-07 0.57553151E-08   
-0.11171068E-07 0.26461023E-07   
0.15335122E-08 0.22380214E-07   
-0.16136555E -07 -0.18051161E-07   
0.17379348E-07 0.10039208E--07   
-0.85285347E-08 -0.15247934E--07   
-0.12414596E-07 0.10096277E-08   
--0.60364810E-07 0.70505261E-07   
0.28509586E-07 0.42514780E-07   
-0.22974405E-07 -0.71983121E--08   
0.12425916E-07 -0.17422930E-08   
0.14355422E-07 0.19853228E -07   
-0.11422798E-07 0.37141793E-07   
-0.12853957E-- 07 0.29927530E-07   
0.24233424E-07 0.44425633E-08   
-0.16662157E-07 0.14293556 E-07   
--0.29363130E--07 0.84812977E-08   
-0.22872575E-08 -0.14577381E-0   
0.61641164E-08 0.68607753E-08   
0.15092964E-07 0.83316940E-08   
-0.33240056E--08 -0.81370184E-08   
-0.82349658E-08 -0.10324445E-07   
0.20590622E-07 0.3605882E-08   
-0.11108516E-07 -0.87090975E-08   
-0.51009757E-07 0.57807109E-08   
0.39972189E-08 -0.24577210E-07   
-0.19465729E-- 07 -0.37879609E-07   
-0.15835961E-07 0.10851357E-07   
n m Cnm   
1814 -0.86648091E-08   
1914 -0.55947842E-08   
20 14 0.12279215E-07   
21 14 0.19369491E-07   
2214 0.95769993E-07   
2314 0.86305161E-08   
24 14 -0.16837749E-07   
2514 -0.24209441E-07   
2614 0.74549429E-08   
27 14 0.23450546E-07   
2814 -0.53526975E-08   
29 14 -0.10980240E-07   
15 15 -0.21839434E-07   
1615 -0.13117388E-07   
17 15 0.97352476E-09   
18 15 -0.54464037E-07   
1915 -0.22266692E-07   
20 15 -0.23792562E-07   
21 15 0.10428100E-07   
22 15 0.24083606E-07   
2315 0.13462651E-07   
24 15 0.58586362E-08   
2515 -0.24729545E-08   
1616 --0.29205699E-07   
17 16 -0.23913577E-07   
18 16 0.11108303E-07   
1916 -0.35402384E-07   
20 16 -0.13930518E-07   
21 16 -0.84435744E-10   
2216 -0.40760661E-08   
1717 -0.11900867E-07   
18 17 0.21146024E-07   
19 17 0.30424729E-07   
Unm   
-0.92065896E-08   
-0.12589401E-07   
-0.10038272E-07   
0.10222863E-07   
0.65217836E-08   
-0.53407649E-08   
0.36020836E-08   
0.16924962E-07   
0.11779540E-08   
0.58917610E-08   
-0.10565846E-08   
0.99757442E-08   
-0.56963495E-08   
-0.25958721E-07   
0.48072218E-08   
-0.16115436E-07   
-0.15318470E-07   
0.87442615E-08   
0.11487724E-07   
0.81938181E-10   
0.34413456E--08   
-0.21743642E-08   
-0.17155684E-08   
0.12253366E-07   
0.13264217E-07   
0.19449968E-07   
-0.13067001E-07   
0.97025452E-09   
-0.59787307E-08   
-0.47087781E-08   
-0.33685315E-10   
0.10658114E-07   
-0.57810357E-08.

n m Cnm Sm 20 17 -0.13064496E-07 -0.72825745E-08 .21 17 -0.26664251E-08 --0.29289956E-08 22 17 -0.53096792E-08 -0.37690008E-08 18 18 0.19929495E-08 -0.12744534E-07 19 18 0.33852797E-07 -0.21033670E-07 20 18 -0.31768957E-08 0.29542439E-07 21 18 0.12498797E-07 --0.13863115E-07 22 18 0.90862145E-08 -0.95018435E-08 19 19 0.97083611F --C8 -0.21049736E-08 20 19 0.17211495E--07 0.87109227E-08 .21 19 0:11918393E-07 --0.89025929E--08 22 19 -0.18006127E-07 -0.22831162E-07 20 20 -0.61814011E-08 -0.55310403E-08 0 0 0.0 0.9 0 0 0.0 0.0 0 0 0.0 0.0 0 0 0.0 0.0 0 0 0.0 0.0 27 26 -0.11168448E-07 -0.61017990E-08 28 26 0.74233346E-08 -0.23132861E-08 29 26 -0.10320632E-07 -0.16901060E-07 27 27 0.95990507E-- 10 -0.30028277E-08 28 27 -0.83079094E-08 0.25735176E-08 2828 0.42471146E-08 0.58630268E-08 3028 －0.18353777E-07 -0.34857327E-07 GEM-T1 n m Cnm Sm 2 0 -0.48416499E-03 3 0 0.95723751E-06 4 0 0.53873219E-06 5 0 0.68780161E-07 6 0 -0.14810038E-06 .7 0 0.90533705E-07

n m Cnm   
8 0 0.45902321E-07   
9 0.28376362E-07   
10 0 0.57221060E-07   
11 -0.51261854E-07   
12 0 0.32080560E-07   
13 1 0.42231883E-07   
14 0 -0.19732657E-07   
15 0 0.18730994E-08   
16 0 -0.93772439E-08   
17 0 0.20396768E-07   
18 0.11291237E-07   
19 0 -0.46083952E-08   
20 0 0.15314998E-07   
21 0 0.97754500E-08   
22 0 -0.48440169E-08   
23 0.24126042E-07   
24 0.95558088E-09   
25 -0.68866692E-08   
26 ） -0.18390658E- 08   
27 0.41233832E- 08   
28 0 --0.58541428E-08   
29 0 -0.39091111E-08   
30 0 -0.27488096E-09   
31 0 0.51153935E-08   
32 0 0.81872659E-10   
33 0 0.2286365E-08   
34 0 -0.24803074E-08   
35 0.12730888E-08   
36 0 0.73959303E-09   
1 1 0.0   
2 1 0.0   
3 1 0.20297737E-05   
4 1 -0.53342722E-06

# Snm

0.0 0.0 0.24959463E-06:   
-0.47511891E- 06:

-nⅢ \~nm   
-0.58950310E-07 -0.95543463E-07   
-0.81375094E --07 0.23890050E-07   
0.27709714E-06 0.97817738E-07   
0.28856051E-07 0.54722278E-07   
0.14804470E-06 0.24525140E-07   
0.76965520E--07 --0.13811096E-06   
0.95018541E-08 -0.27811143E-07   
-0.49261048E-07 -0.49651962E-07   
-0.54061688E-07 0.43455461E-- 07   
-0.18746223E-07 0.23224364E-06   
0.82867603E-08 0.14212435E-07   
0.31709949E-07 0.17349282E-07   
-0.30938101E-07 -0.26845911E-07   
-0.22530245E-09 -0.45605469E-07   
-0.11594207E-07 0.53764346E- 08   
0.14511924E-07 -0.21271095E-07   
-0.15394159E-07 0.41745854E-07   
0.83945638E-08 -0.14724999 E-07   
0.86571068E--09 0.14597012E-07   
0.81178418E-08 -0.29198651E-07   
0.37144518E--08 0.43498107E-08   
0.49740599E--08 -0.17251808E-07   
0.52298861E-09 0.66113211E-08   
0.65293723E-08 －0.10025069E-07   
0.34698888E-08 0.24175564E-08   
-0.16170787E-08 -0.90886001E-08   
0.51781892E-08 0.23829429E-08   
-0.91529228E-08 -0.92450896E-08   
0.12672493E-08 0.21258063E-08   
-0.15608227E-08 -0.91011313E-08   
-0.19068960E-08 0.20110394E-08   
0.28774429E-08 -0.58408490E-08   
0.24389280E-05 --0.13998397E-05   
n m Cmm Snm   
3 2 0.90354910E-06 -0.62041982E-06   
4 2 0.34700208E-06 0.66403042E-06   
5 2 0.65579025E-06 -0.32340559E-06   
6 2 0.51609578E-07 -0.37499560E-06   
7 2 0.31771079E-06 0.91608267E--07   
8 2 0.70380074E-07 0.68449357E-07   
9 2 0.31136534E-07 -0.32388207E-07   
10 2 -0.80521206E-07 -0.51335560E-07   
11 2 0.90541469E-08 -0.99241417E-07   
12 2 0.76400257E-08 0.34918307E-07   
13 2 0.53436060E-07 -0.57584426E-07   
14 2 -0.34812151E-07 -0.60681388E-08   
15 2 -0.21625825E-07 -0.36442471E-07   
16 2 -0.15643689E-07 0.24543138E-- 07   
17 2 -0.57799960E-08 0.17124749E-07   
18 2 0.84082647E-08 0.16842781E-07   
19 2 0.84369162E-08 -0.10474406E-07   
20 2 0.19877209E-07 0.32259479E-08   
21 2 0.98738727E-09 -0.26067452E--08   
22 2 -0.14292465E-07 0.20957550E--08   
23 2 -0.53132926E-09 -0.17780401E-08   
24 2 -0.58515141E-08 0.52022322E--08   
25 2 0.37220008E-08 0.52067808E-08   
26 2 -0.52886997E-08 0.25220078E-09   
27 2 0.10217402E-07 -0.28223192E--08   
28 2 -0.84275601E-08 -0.11552428E-07   
29 2 0.94631996E-08 -0.43310841E-08   
30 2 -0.40515249E--08 -0.53644918E-08   
31 2 0.66008381E-08 0.83617817E-09   
32 2 -0.18648975E-08 0.43748673E-08   
33 2 0.10231050E-08 0.95479524E-09   
34 2 -0.35817186E-08 0.51783191E-08   
35 2 0.25528604E-08 0.10276933E-08   
n m Cnm Snm   
36 2 0.17895825E-09 0.12922184E-08   
3 3 0.72098662E-06 0.14131694E-05   
4 3 0.99097790E-06 -0.20062149E-06   
5 3 -0.44820358E-06 -0.21512633E-06   
6 3 0.61970909E-07 0.46429830E-08   
7 3 0.25074289E-06 -0.20916391E-06   
8 3 -0.19966400E-07 -0.86936688E-07   
9 3 -0.15537419E-06 -0.84015759E-07   
10 0.13119206E-08 -0.16148241E-06   
11 3 -0.28889528E-07 -0.13249631E--06   
12 3 0.32419822E-07 0.17943766E-07   
13 3 -0.14025872E-07 0.83661466E-07   
14 3 0.36931119E-07 0.22422233E-07   
15 3 0.44627091E-07 0.26544709E-07   
16 3 -0.32084146E-07 -0.45027214E-07   
17 3 0.10121364E-07 0.98938954E-08   
18 3 -0.10019902E-08 -0.70482902E-08   
19 3 0.14390659E-08 0.14195541E-07   
20 3 0.82691340E-08 0.13715069E-07   
21 3 0.19940731E-08 0.22692348E-07   
22 3 0.67253396E-08 -0.80912522E-08   
23 3 -0.45641514E-08 -0.11945837E-07   
24 3 0.69147885E-08 -0.10592550E-07   
25 3 -0.32642356E--08 -0.31087039E-08   
26 3 -0.26206333E-08 -0.37215303E-08   
27 3 -0.51035161E-08 -0.18585398E-08   
28 3 -0.26464087E-09 0.11661870E-08   
29 3 -0.43864241E-08 --0.17609256E-08   
30 3 -0.16075275E-08 0.14769842E-08   
31 3 -0.18668416E-08 -0.40768640E-08   
32 3 -0.66627992E-09 0.29992183E-08   
33 3 -0.17027147E-08 -0.28776290E-08   
34 3 -0.51451343E-09 0.22064928E--08   
n m Cnm Snm   
35 3 0.67326256E- 09 0.68607957E-09   
36 3 -0.81294713E-09 0.13851648E-08   
4 4 -0.19003480E-06 -0.30845955E-06   
5 4 -0.29482361E-06 0.52408737E-07   
6 4 -0.92797469E-07 0.47330695E-06   
7 4 -0.27374044E-06 -0.12200273E-06   
8 4 --0.24606388E-06 0.67745274E \~- 07   
9 4 -0.12830303E-- 07 0.23263712E-07   
.10 4 -0.97312281E-07 -0.69382470E-07   
11 4 -0.33210825E-07 -0.70003586E-07   
12 4 -0.65301966E-07 -0.30124749E-08   
13 4 -0.88182430E-08 -0.37315985E-09   
14 4 -0.88329178E-08 0.18783233E--08   
15 4 -0.44375984E-07 0.12641626E-07   
16 4 0.36512284E-07 0.43855936E-07   
17 4 0.12587762E-07 0.31224178E-07   
18 4 0.43416654E-07 0.60924096E-08   
19 4 0.25698533E-08 0.76746622E-08   
20 4 -0.17950684E-08 0.82814012E-09   
.21 4 -:0.25498323E-09 0.69894096E-08   
22 4 -0.94461540E-08 0.16709984E-07   
23 4 -0.10033607E-07 -0.16695799E-08   
24 4 0.60579731E-08 0.18114515E-07   
25 4 0.63502786E-08 -0.15335295E-08   
26 4 0.53222010E-08 0.48968094E-08   
27 4 0.29163700E-08 -0.64011363E-09   
28 4 0.28786394E-08 -0.24854683E--08   
29 4 -0.63640995E-08 0.72890842E-09   
30 4 -0.21102268E-08 -0.39249671E-08   
31 4 -0.49509276E-08 －0.16391510E-08   
32 4 0.20178990E-08 -0.33824636E-08   
33 4 -0.23622194E-09 0.39381070E-09   
34 0.28502139E--08 -0.18773298E-08   
n m Cnm Snm   
35 4 0.27441905E-08 0.14863525E--08:   
36 4 0.13156923E-08 -0.11812307E-09.   
5 5 0.17775628E--06 -0.66602811E-06   
6 5 -0.26576497E-06 -0.53774724E-06   
7 5 0.34749784E-08 0.19651896E-07   
8 5 -0.24933453E-07 0.85300324E-07   
9 5 -0.14112484E-07 -0.60062687E-07   
10 5 -0.50440072E-07 -0.43826930E-07   
11 5 0.45908630E-07 0.55284846E-07   
12 5 0.30604018E-07 -0.14745023E-08   
13 5 0.59617645E-07 0.57445970E-07   
14 5 0.22795185E-07 -0.11607786E-07   
15 5 0.16074165E-07 0.10886373E-07   
16 5 -0.77241776E-08 -0.16772527E--08   
17 5 -0.11147188E-07 -0.56030506E-08   
18 5 0.17425976E-08 0.21127630E-07   
19 5 -0.24456877E-08 0.17378879E-07   
20 5 -0.10418225E-07 0.30340910E-09   
21 5 0.17759319E-07 -0.15891088E-07   
22 5 -0.46334771E-08 -0.12572490E-09   
23 5 0.19940734E-08 -0.79407063E-08   
24 5 -0.14083816E-07 -0.79804972E-08   
25 5 -0.24584695E-08 -0.23514377E-08   
26 5 0.43006874E-08 0.10647174E-07   
27 5 -0.15884485E-08 0.37102860E-08   
28 5 0.29221835E-08 -0.23605821E-09   
29 5 0.34464500E-08 0.35422017E-08   
30 5 0.33915905E-08 0.69830051E-09   
31 5 0.90957175E-09 0.14649106E-08   
32 5 -0.48016094E--10 -0.27949055E-08   
33 5 -0.51318216E-09 0.32352716E-08   
34 5 -0.12951735E -- 08 0.40120636E-10   
35 5 -0.23508223E-09 -0.73737355E-09   
n m Cnm Snm   
36.5 -0.11797710E-08 0.34027125E-09   
6 6 0.90593110E-06 -0.23633442E-06   
7 6 :-0.35785266E-06 0.15091751E-06   
8 6 -0.66417800E-07 0.31283228E-06   
9 6 0.70526278E-07 0.21662848E-06   
10 6 -0.34736639E-07 -0.77718879E-07   
11 6 0.84723183E-08 0.24290955E-07   
12 6 0.13880827E-08 0.45832155E-07   
13 6 -0.22386919E-07 -0.11835958E-07   
14 6 -0.31868397E-08 0.65118719E-08   
15 6 0.27231763E-07 -0.51707671E-07   
16 6 0.17994870E-07 -0.26783523E-07   
17 6 0.29202865E-09 -0.30416593E-07   
18 6 0.31199089E-07 -0.85569089E-08   
19 6 -0.62544678E-08 0.39168584E-08   
20 6 0.12760653E-07 0.96620759E-09   
.21 6 0.42146274E-08 -0.83500531E-08   
.22 6 0.14626140E-07 0.24348355E-08   
.23 6 0.99987799E-08 0.49568433E-08   
.24 6 -0.30547150E-09 -0.66405117E-09   
.25 6 0.59358163E-08 -0.67430051E-08   
26 6 0.85388115E-08 0.31967552E-08   
27 6 0.17746059E-08 -0.21341571E-08   
28 6 -0.83296107E-08 0.20029352E-08   
29.6 -0.29604759E-09 -0.24663349E-08   
30 6 -0.32177147E-08 0.41679122E-08   
31.6 --0.56215143E-09 0.76666984E-09   
32 6 -0.38310209E-08 0.21903594E-09   
33:6 0.13823756E-08 -0.12541577E-08   
34 6 0.58081313E-09 －0.32202302E-09   
35 6 0.83041406E-09 -0.14751754E-08   
36 6 -0.57574770E-09 -0.89878853E-09   
7 7 0.15976040E-08 0.22001281E-07   
1 Cnm   
8 7 0.70424829E-07   
9 7 -0.11862334E-06   
10 7 0.97467817E-08   
11 7 0.96092625E-08   
12 7 -0.12697545E-07   
13 7 0.35735887E-08   
14 7 0.37484340E-07   
15 7 0.66713009E-07   
16 7 0.30510613E--08   
17 7 0.22952022E-07   
18 7 -0.79568117E-09   
19 7 0.51443421E-08   
20 7 -0.77912749E-08   
21 7 -0.12227926E-07   
22 7 0.12753844E-07   
23 7 -0.23282304E-08   
24 7 -0.25113287E-08   
25 7 0.26315859E-09   
26 7 0.54523616E-08   
27 7 0.69279448E-08   
28 7 -0.46458954E-08   
29 7 0.11829611E-08   
30 7 -0.17199722E-09   
31 7 0.14817170E-08   
32 7 10.30832015E-08   
33 7 -0.40520201E-10   
34 7 -0.23148182E-08   
35 7 0.74827537E-10   
36 7 0.16620509E-09   
8 8 -0.11888272E-06   
9 8 -0.18449536E-06   
10 8 0.43746826E-07   
11 8 -0.63529583E-08   
Pnm   
0.74862572E-07   
-0.10055100E-06   
－0.42901064E-08   
-0.91889110E-07   
0.34829092E-07   
-0.66171063E-08   
0.43588271E--08   
-0.11454541E-07   
0.90736837E-08   
-0.11980959E-07   
0.67158701E-08   
-0.16620217E-08   
0.48958423E-08   
-0.14057562E-08   
0.13041803E-08   
0.26451762E-08   
0.50661763E-08   
0.34596220E-08   
0.25831011E--08   
-0.28217028E-08   
-0.15444277E-08   
-0.72940317E-08   
-0.12910545E-09   
-0.17479204E-08   
0.18611086E-08   
0.17755761E-08   
0.10284346E-09   
0.15282139E-08   
-0.41993948E-09   
0.12233200E-06   
-0.18494446E--08   
-0.92480766E-07   
0.22582708E-07   
n m Cnm   
12 8 -0.21217724E-07   
13.8 -0.12296415E-07   
14 8 -- 0.32941574E-07   
15 8 -0.40666014E-07   
16 8 -0.13437589E-07   
17 8 0.31156353E-07   
18 8 0.45719109E-07   
19 8 0.14862645E-07   
:20 8 -0.20109280E-07   
:21 8 -0.18100827E-08   
22 8 -0.98173394E-08   
23 8 0.42209432E-08   
.24 8 -0.24330168E-08   
25 8 0.14256293E-08   
26 8 0.30889398E-08   
27 8 -0.41793993E -- 08   
.28 8 -0.56548364E-08   
29 8 -0.64244512E-08   
30 8 0.29535874E-08   
.31 8 0.87245942E-10   
32 8 0.88180698E-09   
33 8 -0.82271696E-10   
34 8 0.70831611E-09   
35 8 0.26785018E-09   
36 8 -0.10487426E-08   
9 9 -0.55545705E-07   
10 9 0.12817966E-06   
11 9 -0.38777353E-07   
12.9 0.46937991E-07   
13 9 0.20382660E-07   
14 9 0.37160897E-07   
15 9 0.13444146E--07   
16 9 -0.16575038E-07   
0.16904595E-07   
-0.11092454E-07   
-0.13181398E-07   
0.24732519E-07   
0.22803667E-08   
0.87749530E-08   
-0.43052581E-09   
-0.11327286E-07   
0.12912453E-08   
-0.25207967E-08   
-0.68267229E-08   
0.67954115E-08   
-0.75573889E-08   
-0.41241093E-08   
-0.21406622E-08   
-0.44058873E-08   
0.31778226E-08   
0.25406137E-08   
0.57203317E-09   
0.11844897E-08   
0.33225532E-08   
0.15750144E -- 08   
-0.78595875E-09   
0.17721535E-09   
-0.53775389E-09   
0.97588872E-07   
-0.48185995E-07   
0.40284908E-07   
0.13222327E--07   
0.45782026E-07   
0.17933219E-07   
0.41018706E-07   
-0.50982455E-07   
m m Cnm Dnm   
17 9 -0.32014696E-08 -0.34324567E-07   
18 9 -0.13521645E-07 0.19244620E-07   
19 9 0.17565609E-08 0.86593015E-08   
20 9 0.22812092E-07 0.72350387E-08   
21 9 0.17320532E-07 -0.93912901E-08   
22 9 0.12510638E-07 -0.94816097E-08   
.23 9 -0.40274233E-08 -0.10391555E-07   
.24 .9 -0.38939765E-08 -0.14301925E-08   
:25 9 -0.60297356E-08 0.98442109E-08   
26 9 0.25190886E-08 -0.65916451E-09   
:27 9 0.39904591E-09 0.21552798E-08   
28 9 0.29414014E-08 -0.30550496E-08   
.29 9 -0.16393562E-08 0.24790390E-08   
30 9 0.16647631E-09 -0.39351135E-08   
31 9 -0.38940793E-08 -0.17016136E-08   
32 9 0.19461106E-08 0.76813568E-09   
33 9 -0.29391935E--G9 0.18691477E-08   
:34 9 0.12659539E-08 0.15092713E-08   
35 9 0.10826201E-08 -0.20731238E-08   
36 9 -0.31699159E--09 0.54838552E-09   
1010 0.94559588E-07 -0.20104057E-07   
11 10 -0.52058168E-07 -0.17612584E-07   
12 10 -0.91273230E-08 0.31678246E-07   
13 10 0.43302795E-07 -0.38038293E-07   
14 10 0.36995260E-07 一0.27966224E-08   
15 10 0.95927798E-08 0.16081179E-07   
16 10 -0.10417125E-07 0.66055970E-08   
17 10 0.21049915E-08 0.20119348E-07   
18 10 0.90063434E-08 -0.10861864E-07   
1910 -0.35353833E-07 -0.26556393E-08   
:2010 -0.22420129E-07 -0.80926195E-08   
21 10 0.36543010E-08 0.18355898E-08   
.22 10 0.50022072E-08 0.20382965E-07   
n m Cnm Snm   
23 10 0.19975759E-07 -0.37584670E-08   
24 10 0.17353495E-07 0.92954402E-08   
25 10 0.56907222E-08 -0.44669453E-08   
2610 -0.48369701E-08 0.16644731E-08   
27 1 -0.88099557E-08 0.60111969E-08   
28 10 -0.72825822E-08 0.12045527E-08   
29 10 0.60200073E-10 0.60143513E-08   
30 10 0.12264617E-08 -0.10401712E-08   
31 10 0.25178065E-08 -0.37447264E-08   
32 10 0.83079647E-09 -0.19507298E-08   
33 10 0.23412401E-09 -0.94493111E-09   
3410 -0.14878521E-08 -0.92535974E-11   
3510 -0.14313425E-08 -0.83536624E-09-   
36 10 -0.35704088E-09 0.46712720E-09.   
11 11 0.54332237E-07 -0.54728755E-07   
12 11 0.54142822E-08 -0.95227576E-08.   
13 11 -0.40190616E-07 0.55014711E- 08   
14 11 0.80835463E-08 -0.41361426E-07   
15 11 0.17171129E-08 0.28932194E-07   
16 11 0.14015621E-07 -0.64368248E-08   
17 11 -0.17110766E-07 0.17501888E-07   
18 11 \~0.12798854E-07 -0.59706494E-09·   
19 0.16480439E-07 0.13474805E-07   
20 11 0.11378710E-07 -0.23930498E-07   
21 11 0.92806093E-08 -0.36783378E-07   
22 11 -0.93740004E-08 -0.18377493E-07   
23 11 0.38490112E-08 0.13679365E-07   
24 11 0.12739592E-07 0.12118036E-07   
25 11 0.55793278E--08 -0.12765636E-08   
26 11 0.32045208E-08 0.50467355E-08   
27 11 -0.11882699E-08 -0.30951190E-08   
28 11 -0.62138108E-09 -0.82897789E-09   
2911 -0.93225622E-08 0.45476219E-09.   
Ⅱ m Cnm Sm   
30 11 -0.16206668E-08 0.50752246E-08   
31 11 －0.16630653E-08 0.58520843E-08   
32 11 -0,24010320E-08 -0.64625180E-09   
33.11 0.55568436E-08 -0.48032147E-09   
.34.11 0.12405502E-08 -0.38324768E-08   
3511 0.67850949E-09 -0.36582555E-08   
3611 0.58804905E-09 -0.73084032E-09   
12 12 -0.35280275E-08 -0.11796361E-07   
13 12 -0.28005922E-07 0.86410159E-07   
14 12 0.89681035E-08 -0.32066790E-07   
15 12 -0.28331733E-07 0.12487194E-07   
1612 0.20880258E-07 0.57370415E-08   
17 12 0.24272433E -- 07 0.17256973E-07   
18 12 -0.26181930E-07 -0.16526234E-07   
19 12 0.32037207E-08 0.43291853E-08   
20 12 -0.40581260E-08 0.17297999E-07   
21 12 0.28236369E-08 0.12706611E --07   
22 12 0.74377420E-08 -- 0.78426316E-08   
23 12 0.21577716E-07 -0.16681196E-07   
24.12 0.12340608E-07 -0.95151695E-08   
25 12 -0.55424850E-08 0.11010009E-07   
26 .12 -0.19645685E-07 0.54337947E-08   
27 .12 -0.42280551E-09 -0.17181839E-08   
2812 0.40239692E-09 0.24268971E-08   
.2912 -0.83392613E-09 - 0.49254326E-08   
30 12 0.37914893E-08 -0.34239656E-08   
31 12 0.14908170E-09 0.46158516E-08   
32 12 -0.17117612E-08 0.41939723E-08   
33 12 0.52207678E-08 0.41268005E－08   
34 12 0.45499257E-09 0.24876009E-08   
35 12 0.14840867E-08 -0.20618921E-08   
3612 -0.21819353E-09 -0.16067792E-- 08   
13 13 -0.61548330E-07 0.68266144E-07   
m Cnm Snm   
14 -0.18643629E-07 0.14570360E-08   
4 -0.21941813E-07 0:13205763E-07   
.4 0.39290295E-08 0.56349630E-08   
.4 0.11970223E-07 0.66379307E-08   
4 -0.21064347E-08 -0.65024742E-08   
4 -0.51524666E-08 0.19468687E-08   
4 -0.32739042E-10 -0.25522211E-08   
4 -0.72827994E-08 0.12481398E--08   
4 0.46569292E-08 0.69215582E-08   
4 0.92319340E-08 0.25098564E-08   
4 -0.10430646E-08 -0.28782175E-09   
4 -0.48360432E-09 -0.12377339E-09   
4 -0.48384403E-08 -0.40884548E-08   
5 -0.18094792E-07 -0.80853614E-08   
5 -0.12532065E-07 -0.32295812E-07   
5 0.49435184E-08 0.57492871E-08   
5 -0.37761928E-07 -0.19824678E--07   
5 -0.18316396E-07 -0.12767.524E-07   
5 -0.22730633E-07 -0.41347684E-09   
5 0.16620498E-07 0.14983722E-07   
5 0.27937349E-07 0.31033478E-08   
5 0.17731839E-08 -0.22812883E-08   
5 0.98097195E-08 -0.13528561E-07   
5 -0.19898648E-08 -0.22709952E-08   
5 -0.11379665E-07 0.47010451E-08   
5 -0.43373196E-08 0.10017932E-09   
5 -0.82106410E-08 .0.53750943E-08   
5 -0.12718069E-08 -0.24917824E-08   
5 0.28146176E-08 -0.92780211E-08   
5 0.45405152E-09 -0.43732181E-08   
5 0.39106700E-08 -0.49374981E- 08   
-0.30054530E-08 0.21726351E-08   
； 0.76434690E-09 0.30005129E-08   
Cnm Dnm   
35·15 0.26088249E-09 0.28303581E-08   
3615 -0.18223411E-08 0.18633535E-08   
16 -16 -0.32411413E-07 -0.43685900E-08   
17 :16 10.29068322E-07 0.18847933E-08   
18 -16 0.97879569E-08 0.50024382E-08   
19 16 -0.19904738E-07 -0.11932552E-07   
20 16 －0.10668481E-07 0.16918906E-08   
2116 0.87330779E-08 -0.51553482E-08   
22 16 0.89245267E-10 -0.49264787E-08   
2316 0.49029078E-08 0.11767122E-07   
2416 -0.49084124E-09 0.62766318E-08   
25 16 0.30418521E-08 -0.12797205E-07   
26 16 0.58241019E-08 -0.41510185E-08   
27 16 0.65849014E-08 -0.41071626E-08   
28 16 -0.83072931E-08 -0.76859638E-08   
29 -16 -0.21980212E-08 -0.55327287E-08   
30 16 0.61893248E-09 0.56596820E-08   
31 16 -0.45140939E-08 0.48013368E-08   
32 16 0.29187335E-08 0.41009838E-08   
33 16 -0.38789253E-09 0.19723651E-08   
34 16 0.11336508E-08 -0.26577938E-08   
35 16 0.13138056E-09 -0.13369327E-08   
36 16 0.13405118E-08 -0.20055241E-08   
17 17 -0.38310904E-07 -0.20623445E-07   
18 17 0.61141636E-08 0.87663478E-08   
19 17 0.27945883E-07 -0.10883665E-07   
20 17 0.42934494E-08 -0.89775714E-- 08   
21 17 -0.67459362E-08 0.83960260E-09   
22 17 0.13807922E-07 -0.11125838E-07   
23 17 -0.72124847E-08 -0.66030834E-08   
24 17 -0.84625438E-08 0.18817093E-08   
25 17 -0.83082653E-08 0.54995111E-09   
26 17 -0.48890087E-08 0.82819679E-08   
n m Cnm Snm   
27 17 0.55505166E-08 0.15914118E-08   
28 17 0.45200818E-08 -0.42606002E-08   
29 17 0.45707564E-08 -0.27848874E-08   
30 17 0.10056617E-08 -0.15437767E-08   
31 17 -0.59334851E-08 0.25686424E-08   
32 17 -0.36602060E-08 0.18909065E-08   
33 17 -0.21426255E-08 0.30431594E-08   
34 17 0.36257703E-09 0.25763510E-08   
35 17 0.33862758E-08 -0.24391254E-08   
36 17 0.21678685E-08 -0.84901523E-09   
18 18 -0.44492488E-08 -0.50646586E-08   
19 18 0.21646651E-07 -0.31130968E-08   
20 18 0.10577121E-07 0.13023524E-08   
21 18 0.16830431E-07 -0.65691029E--08   
22 18 0.70310805E-08 -0.10295487E-07   
23 18 -0.19055704E-08 -0.63022635E-08   
24 18 0.43072442E-08 -0.50725097E-08   
25 18 -0.13004410E-08 -0.10669721E--07   
26 18 -0.90148288E-08 0.75516338E-08   
27 18 -0.51897501E-08 0.59394146E-08   
28 18 0.36452556E-09 -0.82952500E-09   
29 18 -0.20095225E-08 -0.13783483E-09   
30 18 0.30346336E-09 0.85303494E-09   
31 18 0.25645102E-08 0.84908875E-09   
32 18 0.22104681E-08 -0.14794813E-08   
33 18 0.87020026E-09 -0.12393076E-08   
34 18 -0.27232498E-08 -0.86909901E-10   
35 18 0.15003020E-08 -0.59374283E-09   
36 18 0.69338426E-10 0.53062021E-09   
1919 0.64638489E-08 0.10424368E-07   
20 19 -0.70980370E-08 0.84585572E-08   
21 19 -0.20951496E-07 0.15878998E-07   
22 19 0.66210335E-08 -0.46952003E-08   
n m Cnm Sm   
:23 21 0.10819548E-07 0.76428354E-08   
24 21 0.10574395E-07 0.11196894E-08   
25 21 0.53968150E-08 0.31404063E-08   
26 21 -0.39072329E-09 -0.24147308E-08   
27 21 0.20712300E-08 -0.45431539E-08   
28 21 0.24900117E-08 0.26969931E-09   
29 21 -0.93986375E-08 -0.59494212E-08   
30 21 -0.74517662E-08 -0.30982061E-08   
31 21 0.23358473E-08 0.35766685E-08   
32 21 0.11689742E-08 0.58848002E-08   
33 21 0.73187559E-09 -0.83937102E-09   
34 21 0.13743386E-08 -0.65898518E-09   
35 21 0.13843491E-08 0.27357410E-08   
36 21 0.74113804E-09 -0.21175286E-- 08   
22 22 -0.14623026E-08 0.47182374E-08   
.23 22 -0.90335577E-09 -0.21444698E-08   
.24 22 -0.17321568E-08 -0.13033160E-.08   
.25 22 -0.18741354E-08 -0.17577620E-08   
26 22 0.10911869E-07 0.91610004E-08   
27 22 -0.14295524E-09 0.29341120E-08   
28 22 -0.48465048E-08 0.51180449E-09   
29 22 0.96561861E-08 0.44395297E-08   
30 22 0.32458117E-08 --0.55410417E-08   
31 22 -0.62664026E-08 -0.57324686E-08   
32 22 --0.46595098E-08 0.74549050E-09   
33 22 -0.40991751E-08 -0.10974261E-08   
34 22 0.82939028E-09 0.42210856E-09   
35 22 0.15947247E-10 0.33003309E-08   
36 22 0.57316584E-09 0.68641138E-09   
23 23 0.84457439E-09 0.20297596E-09   
:24 23 -0.21435378E-08 -0.90055328E-08   
.25 23 0.45743254E-08 -0.24632970E-08   
26 23 0.23537011E-08 0.89515942E-- 08   
Cnm Onm   
27 23 -0.53880829E-08 -0.27371510E-08:   
28 23 -0.26403499E--08 ·0.63890659E--08   
29 23 -0.50118310E-08 0.77968506E-10   
30 23 -0.15832858E-08 -0.53377076E-08.   
31 23 0.95046673E-08 0.56544150E-08   
32 23 0.38573353E-08 0.47586351E-09   
33 23 -0.62774040E-09 -0.43975457E-08   
34 23 －0.92997917E-09 -0.21403493E-08   
35 23 -0.23783158E-08 -0.15551059E-08   
36 23 -0.12168408E-08 -0.55176169E-09   
24 24 0.23437675E-08 -0.12129382E--08   
25 24 0.36064793E-08 -0.38584111E-08.   
26 24 -0.13736048E-08 0.12183732E-07   
27 24 -0.19361389E-08 0.26238009E-08   
28 24 0.68762168E-08 -0.15084055E-07   
29 24 -0.25341909E-08 0.37023542E--08   
30 24 -0.25119795E-08 -0.37742482E-10   
31 24 -0.38298402E-08 -0.19100845E-08   
32 24 -0.65905154E-08 0.53250974E-08   
33 24 0.39902712E--08 －0.48209270E-09   
34 24 0.67266646E-08 0.85111872E-09   
35 24 0.25277456E-08 0.21953442E-08   
36 24 0.65885664E-09 -0.14200715E--08   
25 25 0.49455303E-08 0.40141176E-08   
26 25 -0.39875836E-08 0.82487628E-08   
27 25 0.11801361E-07 0.31453301E-08   
28 25 0.11295137E--08 0.48095819E-08   
29 25 0.83056743E-08 0.36286261E-08   
30 25 0.88475174E-08 -0.56061849E-08   
31 25 -0.77448508E-08 -0.27571258E-:.09   
32 25 -0.13172992E-07 0.77043262E-08   
33 25 -0.12627718E-08 -0.48224338E-08   
34 25 0.62515907E-08 -0.82080489E-08   
:n m Cnm Snm   
35 25 -0.33892373E-08 0.15231360E-08   
36 25 0.27006468E-10 0.86476698E-08   
26.26 0.34281419E-08 -0.42689820E-08   
27 26 -0.50080153E-08 0.40035297E-08   
2826 0.34420699E-08 0.16810610E-08   
2926 0.62583993E-08 -0.36877549E-08   
30 .26 -0.32087448E-08 0.81398691E-08   
31 26 -0.46923433E-08 0.36394477E-09   
3226 -0.10511391E-08 -0.15337420E-08   
3326 0.81343124E-08 0.55386200E-08   
3426 0.10815530E-08 -0.90061186E-08   
3526 -0.14343837E-07 -0.14114753E-09   
36 26 0.84469112E-08 0.11084908E-07   
27 27 0.68945212E-08 0.34537943E-08   
28 27 ！ -0.99247008E-08 0.13336342E-08   
29 27 -0.74724537E-08 -0.21506514E-08   
30 27 -0.19205691E-08 0.78152361E-08   
31 27 0.69959714E-08 0.12252489E-07   
32 27 -0.30949343E-08 -0.30220777E-08   
33 27 －0.10332266E-07 -0.21296776E-08   
34 27 0.68974284E-08 -0.54417794E-09   
3527 0.27786837E-08 -0.19129023E-07   
36 27 -0.10191244E-07 0.42304724E-08   
28 28 0.67688663E-08 0.19492585E-08   
2928 0.10322564E-07 -0.19625430E-08   
30 28 -0.89658109E-08 -0.51588533E-08   
31 28 0.34279387E-09 0.17261218E-08   
3228 0.15717493E-08 0.23530321E-08   
3328 -0.10885070E-07 0.18951682E-08   
3428 0.45501888E-08 -0.81979365E-08   
3528 -0.10893598E-07 -0.23354243E-07   
3628 0.69479884E-08 0.56619051E-08   
‘2929 0.86365940E-08 0.31600534E-08

<table><tr><td>nm</td><td></td><td>Cnm</td><td>Snm</td><td></td></tr><tr><td>14</td><td>13</td><td>0.31533302E-07</td><td>0.44623425E-07</td><td></td></tr><tr><td>15</td><td>13</td><td>-0.28105077E-07</td><td>-0.49829339E-08</td><td></td></tr><tr><td>16</td><td>13</td><td>0.13075426E-07</td><td>0.61337462E-09</td><td></td></tr><tr><td>17</td><td>13</td><td>0.11907491E-07</td><td>0.20112232E-07</td><td></td></tr><tr><td>18</td><td>13</td><td>-0.65814505E-08</td><td>-0.35155095E-07</td><td></td></tr><tr><td>19</td><td>13</td><td>-0.60894302E--08</td><td>-0.29170910E-07</td><td></td></tr><tr><td>20</td><td>13</td><td>0.26649108E-07</td><td>0.48913292E-08.</td><td></td></tr><tr><td>21</td><td>13</td><td>-0.18169409E-07</td><td>0.11596871E-07</td><td></td></tr><tr><td>22</td><td>13</td><td>-0.16945480E-07</td><td>0.17845306E-07</td><td></td></tr><tr><td>23</td><td>13</td><td>-0.10457758E-07</td><td>-0.75111962E-08</td><td></td></tr><tr><td>24</td><td>13</td><td>-0.36234682E-08</td><td>-0.38241900E-09-</td><td></td></tr><tr><td>25</td><td>13</td><td>0.73794797E-- 08</td><td>-0.15188289E-07</td><td></td></tr><tr><td>26</td><td>13</td><td>0.27230055E-- 08</td><td>0.14150526E-08</td><td></td></tr><tr><td>27</td><td>13</td><td>-0.59813217E-- 08</td><td>-0.41286544E-08.</td><td></td></tr><tr><td>28</td><td>13</td><td>0.98295394E-10</td><td>0.35308387E--08</td><td></td></tr><tr><td>29</td><td>13</td><td>-0.11458264E-08</td><td>-0.19753431E-08</td><td></td></tr><tr><td>30</td><td>13</td><td>0.14674204E-07</td><td>-0.19169178E-10</td><td></td></tr><tr><td>31</td><td>13</td><td>0.56871226E-08</td><td>0.13249823E-08.</td><td></td></tr><tr><td>32</td><td>13</td><td>0.72555685E-08</td><td>0.22293521E-09·</td><td></td></tr><tr><td>33</td><td>13</td><td>0.36683817E-08</td><td>0.67767413E--08:</td><td></td></tr><tr><td>34</td><td>13</td><td>-0.80803395E-08</td><td>0.12767749E-08</td><td></td></tr><tr><td>35</td><td>13</td><td>-0.11848621E-08</td><td>0.44811860E-08</td><td></td></tr><tr><td>36</td><td>13</td><td>0.76845304E-09</td><td>.0.37947987E-08</td><td></td></tr><tr><td>14</td><td>14</td><td>-0.50565721E-07</td><td>-0.63741139E-08</td><td></td></tr><tr><td>15</td><td>14</td><td>0.61707282E-08</td><td>-0.25613175E-07</td><td></td></tr><tr><td>16</td><td>14</td><td>-0.19122599E-07</td><td>-0.38289549E-07</td><td></td></tr><tr><td>17</td><td>14</td><td>-0.13337011E-07</td><td>0.11761315E-07</td><td></td></tr><tr><td>18</td><td>14</td><td>-0.92828105E-08</td><td>-0.10940046E-07</td><td></td></tr><tr><td>19</td><td>14</td><td>-0.51227063E-08</td><td>-0.12644761E-07</td><td></td></tr><tr><td>20</td><td>14</td><td>0.10322807E-07</td><td>-0.11761956E-07</td><td></td></tr><tr><td>21</td><td>14</td><td>0.18776045E-07</td><td>0.86993835E--08:</td><td></td></tr><tr><td>22</td><td>14</td><td>0.87280204E-08</td><td>0.10240679E-07</td><td></td></tr><tr><td>23</td><td>14</td><td>0.46108312E-08</td><td>-0.32726701E-08.</td><td></td></tr></table>

<table><tr><td>nm</td><td></td><td>Cnm</td><td>Snm</td></tr><tr><td>23</td><td>19</td><td>-0.86826880E-08</td><td>0.74915564E-08</td></tr><tr><td>24</td><td>19</td><td>0.52739365E-09</td><td>-0.15017926E-07</td></tr><tr><td>25</td><td>19</td><td>0.91802375E-08</td><td>0.21317033E-08</td></tr><tr><td>26</td><td>19</td><td>0.16259713E --08</td><td>0.71987541E-09</td></tr><tr><td>27</td><td>19</td><td>0.92542220E-09</td><td>-0.62305405E-08</td></tr><tr><td>28</td><td>19</td><td>0.44182432E-08</td><td>0.13800256E-07</td></tr><tr><td>29</td><td>19</td><td>-0.21920404E-08</td><td>0.15058591E-08</td></tr><tr><td>30</td><td>19</td><td>-0.56265679E-08</td><td>-0.26383561E-08</td></tr><tr><td>31</td><td>19</td><td>0.20171801E-08</td><td>0.28161808E-08</td></tr><tr><td>32</td><td>19</td><td>0.30881481E-08</td><td>-0.15146100E-08</td></tr><tr><td>33</td><td>19</td><td>0.16796386E-08</td><td>0.23687007E-09</td></tr><tr><td>34</td><td>19</td><td>0.59532903E-09</td><td>-0.10032120E-08</td></tr><tr><td>35</td><td>19</td><td>-0.29031008E-08</td><td>0.59317344E-09</td></tr><tr><td>36</td><td>19</td><td>-0.25620332E一09</td><td>-0.69478862E-10</td></tr><tr><td>20</td><td>20</td><td>0.17084949E-08</td><td>-0.13505093E-07</td></tr><tr><td>21</td><td>20</td><td>-0.19041126E-07</td><td>0.18536067E--07</td></tr><tr><td>22</td><td>20</td><td>-0.13315209E-07</td><td>0.14778930 E -- 07</td></tr><tr><td>23</td><td>20</td><td>0.17224835E-07</td><td>--0.90475206E-08</td></tr><tr><td>24</td><td>20</td><td>-0.60618534E-08</td><td>-0.32981772E--09</td></tr><tr><td>25</td><td>20</td><td>-0.37314973E-08</td><td>-0.66216761E-08</td></tr><tr><td>26</td><td>20</td><td>0.94829741E-08</td><td>-0.10948813E-07</td></tr><tr><td>27</td><td>20</td><td>0.29524854E-08</td><td>0.30105691E-08</td></tr><tr><td>28</td><td>20</td><td>-0.98045321E-09</td><td>0.11270809E---08</td></tr><tr><td>29</td><td>20</td><td>-0.47995833E-08</td><td>0.31624766E-08</td></tr><tr><td>30</td><td>20</td><td>-0.27634896E--10</td><td>0.35665893E-08</td></tr><tr><td>31</td><td>20</td><td>0.18946771E-08</td><td>0.55950510E-09</td></tr><tr><td>32</td><td>20</td><td>-0.15880547E-08</td><td>0.14199035E-08</td></tr><tr><td>33</td><td>20</td><td>0.20821542E-08</td><td>-0.75254292E-09</td></tr><tr><td>34</td><td>20</td><td>0.89172446E-09</td><td>-0.39746606E-09</td></tr><tr><td>35</td><td>20</td><td>-0.77451961E-09</td><td>-0.87627222E-09</td></tr><tr><td>36</td><td>20</td><td>-0.91279363E-09</td><td>－0.86613100E-09</td></tr><tr><td>21</td><td>21</td><td>0.24774805E--08</td><td>-0.68510209E-08</td></tr><tr><td>2221</td><td></td><td>-0.13224425E-07</td><td>0.75983161E-08</td></tr></table>

<table><tr><td>m</td><td>Cnm</td><td>Snm</td></tr><tr><td>29</td><td>0.48228870E-08</td><td>0.12395741E-09</td></tr><tr><td>29</td><td>-0.54214572E-08</td><td>-0.59501612E-08</td></tr><tr><td>29</td><td>-0.33427694E-08</td><td>0.25024398E-08</td></tr><tr><td>29</td><td>-0.21320909E-07</td><td>0.19323372E-09</td></tr><tr><td>29</td><td>-0.38112634E-08</td><td>-0.44842110E-08</td></tr><tr><td>29</td><td>0.81878098E-08</td><td>-0.31532255E-08</td></tr><tr><td>29</td><td>--0.13415318E-08</td><td>-0.24474463E-08</td></tr><tr><td>30</td><td>-0.15075257E-08</td><td>-0.42214438E-09</td></tr><tr><td>30</td><td>-0.24527121E --08</td><td>0.84230269E-08</td></tr><tr><td>30</td><td>0.82893385E-08</td><td>0.16312875E-08</td></tr><tr><td>30</td><td>0.25216704E-08</td><td>-0.13493470E-07</td></tr><tr><td>30</td><td>--0.61160808E-08</td><td>0.26790326E-10</td></tr><tr><td>30</td><td>0.37128453E-08</td><td>-0.28852407E-08</td></tr><tr><td>30</td><td>--0.15550663E-08</td><td>-0.20260591E-08</td></tr><tr><td>31</td><td>-0.23188856E-09</td><td>-0.73696032E-10</td></tr><tr><td>31</td><td>-0.76161301E-09</td><td>-0.27125189E-08</td></tr><tr><td>31</td><td>0.17452897E-09</td><td>0.11565784E-08</td></tr><tr><td>31</td><td>0.23533706E-08</td><td>0.22983257E-08</td></tr><tr><td>31</td><td>0.13305218E-08</td><td>0.10338604E-08</td></tr><tr><td>31</td><td>-0.35516319E-08</td><td>0.13604423E-08</td></tr><tr><td>32</td><td>0.72773234E-09</td><td>0.50677161E-09</td></tr><tr><td>32</td><td>0.24100159E-08</td><td>-0.21924817E-10</td></tr><tr><td>32</td><td>-0.81664394E-09</td><td>-0.11610481E-08</td></tr><tr><td>32</td><td>-0.39790599E-09</td><td>0.56640787E-09</td></tr><tr><td>32</td><td>-0.88037162E-08</td><td>-0.30002961E-09</td></tr><tr><td>33</td><td>-0.26755523E-09</td><td>-0.36033958E-09</td></tr><tr><td>33</td><td>0.10234263E-08</td><td>0.13813304E-08</td></tr><tr><td>33</td><td>-0.28805891E-09</td><td>0.16655421E-08</td></tr><tr><td>33</td><td>-0.23972037E-08</td><td>-0.26170123E-08</td></tr><tr><td>34</td><td>-0.20926754E-09</td><td>-0.60385543E-09</td></tr><tr><td>34</td><td>-0.51678490E-09</td><td>0.12373228E-09</td></tr><tr><td>34</td><td>0.83238402E-09</td><td>0.17560494E-08</td></tr><tr><td>35</td><td>0.93798198E-10</td><td>-0.14498513E-09</td></tr><tr><td>35</td><td>0.21523885E-09</td><td>-0.73474771E-09</td></tr><tr><td>36</td><td>0.14836846E-09</td><td>0.41966690E-09</td></tr></table>

# 附录IV 习 题

# 第一章

1．对于远地卫星,若时间单位改为平太阳日·质量和长度单位仍采用书中所给定的，试导出相应的引力常数 $\pmb { G }$ 的大小.

2．对于月球卫星，若采用月球质量为质量单位，长度单位采用月球半径。要使引力常数 $\pmb { G } = 1$ ，试求相应的时间单位．月球质量为 $\mathbf { 1 . 2 3 \times 1 0 ^ { - 2 } M }$ ，$M$ 是地球质量，月球半径为 $1 7 0 0 \mathbf { k m }$ ·

3．若两颗球形卫星分别重1T和 $5 0 0 ~ \mathbf { k } \mathbf { g }$ ，它们的直径则分别为 $2 \textrm { m }$ 和$\bf { 1 0 0 m }$ ，试用书中给出的计算单位算出这两颗卫星的面积质量比 $\pmb { S } / m$

4．如果可以丢掉 $1 0 ^ { - 5 }$ 的量(指不大于 $5 \times 1 0 ^ { - 5 }$ 的量)，那么轨道坐标系与历元地心惯性系之间的转换矩阵 $U$ （见书中(1.53)式)简化成何种形式？表湖何意？

# 第二章

1．对于二体问题,若将相互作用力中的 $1 / r ^ { 2 }$ 改为 $1 / r ^ { n } , n { = } 0 , { \pm } 1 , { \pm } 2 ,$ …，试证明相应的问题仍是可积的.

2．二体间题中,存在面积积分： $r ^ { 2 } \theta = h$ ，试问 $\theta$ 角是从哪里起量的？为什么可以简化成 $r ^ { 2 } \dot { f } = h _ { f }$ 对于有摄情况,能否写成 $r ^ { 2 } ( \dot { f } + \pmb { \varpi } ) = \hbar ( t ) \ ?$ 为什么？

3．试求 $\pmb { \partial } \pmb { r } / \pmb { \partial } \sigma$ ，其中 $\pmb { \sigma }$ 分别取：(1) ${ a , e , i , \varOmega , \omega , M } ;$ (2) $a , i , \Omega$ ， $\pmb { \xi } = \pmb { \varrho }$ $\cdot \sin { \omega } , \eta = e \cos { \omega } , \lambda = M + \omega .$

4．对于小 $\pmb { \mathscr { e } }$ 情况，取基本变量 $\pmb { \sigma }$ 为 $a , i , \mathcal { Q } , \ \xi = e \cos \omega , \eta = - e \sin \omega , \lambda$ $\bf { x } ( M - \lvert - G )$ 试求 ${ \partial u } / { \partial \sigma } , { \partial \left( \frac { a } { r } \right) } / { \partial \sigma } ,$ 其中 $u = f + \omega ,$

5．对于小 $\pmb { \varrho }$ 和小 $\pmb { e }$ 小 $\pmb { \dot { z } }$ 两种情况，基本变量分别取

$$
a , i , \Omega , \xi = e \cos \omega , \eta = - e \sin \omega , \lambda = M + \omega ,
$$

$$
a , \boldsymbol { h } = \sin i \cos \Omega , \boldsymbol { k } = - \sin i \sin \Omega , \boldsymbol { \xi } = e \cos \left( \omega + \Omega \right) ,
$$

$$
\eta = - e \sin \left( \omega + \Omega \right) , \lambda = M + \omega + \Omega ,
$$

若将向径 $\pmb { r }$ 分别写成下列形式：

$$
\begin{array} { r l } & { \pmb { r } = r \cos u \widehat { \pmb { P } } ^ { * } + r \sin u \widehat { \pmb { Q } } ^ { * } , \quad u = f + \omega , } \\ & { \pmb { r } = r \cos u \widehat { \pmb { P } } ^ { * * } + , \sin u \widehat { \pmb { Q } } ^ { * * } , u = f + \omega + \Omega , } \end{array}
$$

试给出 $\hat { P } ^ { * }$ 和 $\hat { Q } ^ { * } , \hat { P } ^ { * * }$ 和 $\hat { Q } ^ { * * }$ 的表达式，并说明其几何意义.

6.将 $\left( { \frac { a } { r } } \right) ^ { 3 } \cos 2 f$ 和 $\left( \frac { a } { r } \right) ^ { 3 } \sin 2 f$ 分别展成 $M$ 的三角级数，取到 $O ( \theta ^ { 2 } )$ 项，并由此说明展开式的特点。

7.已知 $\overrightarrow { \mathrm { c o s } f } { = } - e , \overrightarrow { \mathrm { s i n } f } { = } 0 ,$ ，若改为对真近点角 $\pmb { f }$ 求平均值， $\cos f$ 和sin $f$ 的平均值都为零,说明上述两种平均值有不同结果的原因。

8.将函数 $\cdot \left( \frac { a } { r } \right) ^ { 3 } \cos 2 f , \left( \frac { r } { a } \right) ^ { 3 } \cos \left( f + \omega \right) , \left( \frac { a } { r } \right) ^ { 2 } ( 1 + \cos f + \cos 2 f ) + ( f$ 一M)分别分解成不同性质的项.

# 第三章

1．如何解释短弧定轨中资料误差对轨道半长径a以及偏心率e的影响较大？

2.试由轨道根数a,e,i,ω和观测数据A,h确定卫星星下点纬度,写出具体计算公式.

3．在EaxeHOB定轨方法中，若a不固定，试导出相应的əF;/a，并用三次观测和四次观测分别定轨，从中了解固定a值的原因.

4．试证明由书中(3.74)式定出的间隔△t\*为临界间隔，即两次观测的：间隔△t小于△t\*时，ε,δ无象限判别问题.

# 第四章

1．用书中给出的计算单位，计算地球所受到的光压加速度的大小.

2．如果摄动加速度只有 $W$ 分量，试验证 $\Sigma _ { \bar { \partial } { c _ { j } } } ^ { \partial { r } } \dot { { \bar { c } _ { j } } } = 0 .$

3．若第六个时间根数 $M$ 改为

(1) $M _ { 0 } = - n \tau ,$

$$
M _ { 0 } ^ { \prime } { = } M { - } \int _ { 0 } n d t ,
$$

试导出M。和M。的表达式，并由此说明第六个根数还是采用M为好.

4.试根据摄动运动方程(4.82)找出,@,M三个方程之间的某种关系 （或特征）.

5．试用摄动法构造小参数方程

$$
\ddot { x } + \omega ^ { 2 } x = - \varepsilon x ^ { 3 } , \varepsilon \ll 1 ,
$$

的二阶摄动解.

6．若人造卫星绕地球运行时，相应的摄动函数为R=εcosf,ε>1,试用摄动法构造二阶摄动解.

# 第五章

1．假定地球密度分布均匀，试给出分别考虑J,J,J4项对应的地球引力场等位面的几何形状.

2．地球对绕其运行的人造卫星的引力是否为有心力？为什么？

3．试比较摄动法与平均根数法构造级数解的差别.

4．对于平均根数法，如果(5.56)式不满足,即fi0，那么用该方法构造级数解时，将出现什么情况？

5．试用平均根数法，构造小参数方程

$$
\ddot { x } \dot { + } \omega ^ { 2 } x = - \varepsilon x ^ { 3 }
$$

的二阶解。

6．试写出地球形状摄动(考虑J,J,J三项)二阶解中各种摄动项的计算公式(指形式解）.

7.若将J项的摄动函数展成M的三角级数，取到O(e²)项，试验证$\overline { { \sigma _ { s } ^ { \ ( 1 ) } ( t ) } } = 0 .$

8．对于太阳同步卫星(即Ω的变化与太阳运动“同步”,每天东进约1°)，若每天绕地球转13圈,e0.01,只考虑J2项摄动，试求出该卫星的轨道倾角 $\dot { \mathfrak { z } }$ ：

9.若 $R { = } \frac { { \mathcal { J } } _ { 2 } } { r ^ { 3 } } \cos i$ ，试求 $\varOmega _ { 1 }$ 和 ${ \pmb { a } } _ { \pmb { \mathscr { s } } } ^ { ( 1 ) } ( t )$

10.人造卫星绕地球运行时，若摄动函数改为R=Jcosf，试用平均根数法构造二阶解.

11.如果将基本变量α,e,i,Ω,ω，M中的a换成变量L=a,那么L的二阶长周期项 $L _ { l } ^ { ( 2 ) } { \left( t \right) } .$ 是否为零？

12．在平均根数法构造的地球形状摄动一阶解中，根数M的解对a有哪

些特殊要求？为什么？

13．考虑田谐项摄动时，为什么相应的摄动函数必须展成 $M$ 的三角级数？

14．在地球形状摄动下，卫星轨道变化的主要特征是什么？

15．试具体导出交点周期 $\pmb { T } _ { \pmb { \varphi } }$ 与恒量周期 $\pmb { \mathcal { T } }$ 之间的关系，准到 $\pmb { \theta } ( e ^ { \circ } )$ 项

# 第六章

1．例举人造卫星运动中出现的各种通约情况.

2．对拟平均根数法和平均根数法作详细的比较.

3．具休推出在拟平均根数法构造的 $\pmb { J _ { 2 } }$ 项一阶解(对不同根数）中，(6.37)式右端的第二个积分项.

4.仅就 $J _ { 2 }$ 项的一阶长期摄动项形式 $\sigma _ { i } ( t - t _ { 0 } )$ ，验证振动解(6.55)的合理性.

5．消除奇点方法中给出的 $\Omega _ { \bullet } ^ { ( 1 ) } ( t )$ 含有 $( u - \lambda )$ 项，它与平均根数法给出的 $\Omega _ { \bullet } ^ { ( 1 ) } ( t )$ 含有的 $( f - M )$ 项有何差别，在计算中会出现什么不同的情况！

# 第七章

1、利用泊松括号的性质验证(7.67）式.

2．对于正则方程 ，=，=1,2,3，

(1） $H$ 不含 ${ \pmb q } _ { 1 } , { \pmb p } _ { 3 } .$ ，

(2） $\pmb { H }$ 不含 ${ \mathfrak { q } } _ { 1 } , { \mathfrak { p } } _ { 1 }$ ，

(3） $\pmb { H }$ 不含 ${ \pmb p } _ { 1 }$ 又不显含 $t ,$ 那么原方程可以降低几阶？为什么！

3．求向径 $\pmb { r }$ 对德洛纳变量 $L , G , H , l , g , h$ 的偏导数.

4．试由德洛纳变量所满足的正则运动方程(7.148)推出椭圆轨道根数所满足的摄动运动方程（4.82).

5．用Zeipel方法构造摄动解时，为什么要作二次变换？作一次变换是否可以？试就 ${ { J } _ { 2 } }$ 项的一阶解作具体讨论.

6．若在Zeipel方法中，给第一次消除 $\pmb { \ell }$ 变换的生成函数 $\pmb { \mathcal { S } } _ { 1 }$ 增加一个任意函数 $\varphi _ { 1 } ( L ^ { \prime } , G ^ { \prime } , H ^ { \prime } , g )$ 或 $\varphi _ { 1 } ( L ^ { \prime } , G ^ { \prime } , H ^ { \prime } )$ ，对解有无影响 $q$ 就 $\pmb { J _ { 2 } }$ 项摄动的

一阶解具体讨论。

${ \cal F } = { \cal F } _ { 0 } ( L ) + { \cal F } _ { 1 } ( L , G , H , l , g ) + { \cal F } _ { \ : \circ / \ : 2 } ( L , G , H , g ) + { \cal F } _ { 2 } ( L , G , H , H , g ) $ l,g),试用Zeipel方法构造相应问题的一阶解，其中Fb=O(ε),ε是小参数.

8．用Zeipel方法求小参数方程

$$
\pmb { \chi } + \omega ^ { 2 } \pmb { x } = - \pmb { \varepsilon } \pmb { x } ^ { 3 }
$$

的二阶解.

9．如果R=Jcosf,试用Zeipel方法求相应问题的一阶解，并与用摄动法、平均根数法给出的结果作比较.

10．为什么在第五章第11题中求出L（t)0,而用Zeipel方法却求.出L2（t）=O试具体分析其原因.

11．试用Lie变换求解第8题.

12．试用Lie变换求解第9题，并与Zeipel方法给出同一问题解的过！程相比较.

13．全面比较Zeipel变换与Lie变换之间的差别，并由此说明各自的：优缺点.

14．就地球形状摄动，对正则变换方法与平均根数法进行比较，并由此说明各自的优缺点.

15．用一般变换方法求解第8题和第9题.

# 第八章

1．具体分析日、月摄动对人造地球卫星轨道影响的特征.

2．对于太阳同步卫星,具体导出相应的主要通约项.

3．对于近地卫星,考虑太阳摄动时，试估计地球扁率间接摄动的量级.

4．对于潮汐摄动，书中已针对k2部分证明了潮汐摄动位的两种表达形式的一致性，试对k部分作类似的证明.

# 第九章

1．在光压力为有心力的假定下，试用(9.5)式给出的光压摄动函数R推出摄动力 $\pmb { F } _ { \odot }$

2．对有、无地影两种情况，卫星轨道在光压摄动影响下，其变化有什么.

重大差别？

3．具体分析光压摄动对人造卫星轨道的影响特征。

4．直接推导用偏近点角E作基本变量的地影方程。

5．对于24地球同步卫星，一年内何时有地影存在，哪几天卫星在地影内的时间最长，并具体给出该值，假定e=0.0,i=0.0.

# 第十章

1．针对球形静止大气，假定密度标高H不变，试计算大气密度对卫星运动而言的平均值，从而了解该平均值与卫星轨道偏心率e之间的关系.

2．对静止大气情况导出远地距𝑟p的变化率rp'并与近地距r的变化率 ${ \dot { \pmb { r } } } _ { \pmb { p } }$ 进行比较.

3．如何定性地解释在大气阻力摄动下，卫星轨道偏心率e随时间t减小？

4.对于球形静止大气,给出大气阻力摄动解的短周期项，取到O(z)项.

5．若卫星轨道偏心率较小，对于局部问题，假定大气密度是高度的代数函数：

$$
\rho { = } \rho _ { 0 } { + } \rho _ { 1 } ( r { - } r _ { 0 } ) , \rho _ { 1 } { = } { \tt c o n s t . }
$$

试给出大气阻力摄动对卫星轨道影响的基本规律，并与指数形式的大气密度情况进行比较。

# 第十一章

1．如果J项摄动函数改为R=J/2r，试求历元地心惯性系中的附加摄动.

2．在轨道坐标系中，根据常数变量法导出的方程(11.79)，其中dr/d的右端为什么增加了(ər/əl)这一项，而不是dr/dt=r？如有计算条件，不妨用具体计算结果来验证上述情况.

# 第十二章

1．具体计算近地卫星(周期为2h)在后牛顿效应影响下，近地点参数@的长期变化率，采用广义相对论模型.

2．如果将人造卫星改为水星，地球改为太阳,试计算水星近日点参数@的长期变化率．另一方面考虑太阳的扁率摄动，试问太阳扁率J为何值时，它所引起的@的长期变化与广义相对论效应的结果相当？

# 第十三章

1．为什么说AKCeHOB型中间轨道解的后三个积分N,N,N存在积分常数问题？并给出相应的积分常数的量级.

2．若以包含J2项摄动一阶长期项的变化椭圆作为中间轨道，在此基础上如何求剩余摄动？就J,J,J4三项进行讨论.

3．根据书中介绍的内容，仔细分析一下，中间轨道达到实用程度的主要障碍在何处？

# 第十四章

1．试证最优加权的最小二乘估计是无偏的.

2．对于非线性系统，写出相应的最小二乘估计的分批递推公式和具有初始估计的最小二乘估计公式.

# 3．试直接根据表达式

$$
r = r \cos f { \widehat { \mathbf { P } } } + r \sin f { \widehat { \mathbf { Q } } }
$$

推导ar/i,r/Ω,ar/x,并整理成书中的形式,即(14.8)式.

4.若取基本变量a,i,Ω,=esinω,n=ecosω,λ=M+ω,试导出矩阵$\ r _ { \pmb { \mathscr { o r } } } / \ r _ { \pmb { \mathscr { o } } }$ 的元素 ${ \pmb \partial } { \pmb r } / { \pmb \partial } { \pmb \xi }$ 和 ${ \pmb { \partial } } { \pmb { r } } / { \pmb { \partial } } { \pmb { \eta } }$

Document generated by Anna's Archive around 2023-2024 as part of the DuXiu collection (https://annas-blog.org/duxiu-exclusive.html).

Imageshavebeen losseslyembedded.InformationabouttheoriginalfilecanbefoundinPDFattachments.Somestats (moreinthe PDF attachments):

"filename": "MTAyNDczMDhf5Lq66YCg5Zyw55CD5Y2r5pif6L2o6YGT5Yqb5a2mLnppcA $z { = } "$ ，   
"filename_dec0ded": "10247308_\u4eba\u9020\u5730\u7403\u536b\u661f\u8f68\u9053\u529b\u5b66.zip",   
"filesize": 27165496,   
"md5": "79ab9daac355fa59b5ff996bb26b9bb9",   
"header_md5": "8a483011ff335e8ebedf6b6f48eba76c",   
"sha1": "c76ebf2e4315b62f47af7070cbd1ae6d940c0725",   
"sha256": "ba0c8ecd301cb978b2a382c55c8c1655dca4b955c36b55689941ae8bed624f51",   
"crc32": 4079964980,   
"zip_password": "",   
"uncompressed_size": 27452432,   
"pdg_dir_name": ",   
"pdg_main_pages_found": 619,   
"pdg_main_pages_max": 619,   
"total_pages": 628,   
"total_pixels": 2106833088,   
"pdf_generation_missing_pages": false