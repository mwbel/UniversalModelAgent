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

![](images/de9c3259fb05e6534f0d4d695979dc870496839f210285035aaf9bb8da6b16a5.jpg)  
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

![](images/44e00cac93a1158aa00d3ea1ba680d495291307c8d86e5953dd43994a4d65c44.jpg)  
图11.3FFT递归计算流图

![](images/73668b14f0eed0b124e0e62317a16117a678c34e431f19216a785a28236ccf72.jpg)  
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

![](images/88839c082993709a2c13c169759ecf4a55f40186e4e99298618e7924f0153b47.jpg)  
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

![](images/0e454dc3bd5ed88a980d4014baf798c5271587345570f04b65bbc0c7509a213a.jpg)  
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

![](images/77e1854a560505676b239fa5b9c1ab4b028c7c0222fe1960aef69be2edd9928e.jpg)  
16点FFT

![](images/7debfeaef29b352947fc3bc97e0f11250c10dec75dc60c80a3eaa4e9971c93e3.jpg)  
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

![](images/29ac50c47d01ff3de497685a7c474c37e0e833624c736f32abcb8928c135ae15.jpg)  
图11.9Cormen8点FFT计算流图

![](images/c351052132e11b4bfbe44db115e1538356f251f2281d7e1d658483df75e964c2.jpg)  
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

![](images/af69784431d4d0b71c57e0bad848b6334cdd2294295d38e55b5527cb6fa37247.jpg)  
图12.1示例三种并行化方法

三种并行编程方法的优缺点可概括于表12.2中。

表12.2 三种并行编程方法比较一览表  

<table><tr><td rowspan=1 colspan=1>方法</td><td rowspan=1 colspan=1>优点</td><td rowspan=1 colspan=1>缺点</td><td rowspan=1 colspan=1>例子</td></tr><tr><td rowspan=1 colspan=1>库函数</td><td rowspan=1 colspan=1>易于实现,不需要新的编译器</td><td rowspan=1 colspan=1>没有编译检查、分析和优化</td><td rowspan=1 colspan=1>MPI、PVM、Cray Craft</td></tr><tr><td rowspan=1 colspan=1>新结构</td><td rowspan=1 colspan=1>允许编译检查、分析和优化</td><td rowspan=1 colspan=1>难以实现，需要一个新的编译器</td><td rowspan=1 colspan=1>Fortran90、Cray Craft</td></tr><tr><td rowspan=1 colspan=1>制导</td><td rowspan=1 colspan=2>是库函数和新结构两者优缺点的折衷,其显著优点是“普通申行程序+格式注释”,可在任何串行平台上编译</td><td rowspan=1 colspan=1>HPF、Cray Craft</td></tr></table>

# \*12.2进 程

进程 $( \mathrm { P m o c e s s } )$ 是并行程序中的基本计算单位,它对应于由相应代码段所执行的操作。程序就是一些进程的集合。而并行程序设计的基本问题就是围绕着进程的说明、生成、中止、激活、迁移、结束和同步等。在一台并行机上,用户应用程序都是作为进程(任务、线程)被执行的，所以有必要先复习一下进程的有关问题。

# 12.2.1 进程的基本概念

基本定义进程 $\mathbf { P } { = } \left( \mathbf { P } , \mathbf { C } , \mathbf { D } , \mathbf { S } \right)$ 是一个4元组,其中P是程序(即代码)、C是控制状态 $\mathbf { D }$ 是数据状态、S是进程 $\mathbf { P }$ 之状态。任何进程总和程序连系在一起。程序使用两组变量：数据变量保持数值,由程序员说明之;控制变量保持控制流信息，不需显式说明。在任何时刻t,程序的状态由所有成对的(程序变量，值)之集合所定义。进程是动态变化的,在任何时候它会处于某一状态。如图12.2所示，开始时进程处于非存在(Nonexistent)状态;它可由其父进程生成就绪(Ready)状态,然后被调度进人运行(Rumning)状态;当无法继续执行时，它就转人中止(Suspended)状态,以后待机被唤醒可再次进入就绪状态;进程运行中也可被别人抢先或因超时而停止运行,或者就正常结束,或者因异常退出而被废弃。

![](images/a6e28f65978c98e4400b717c4ac6e599f6597f62a02d5a1f1dd71d2a843b2a21.jpg)  
图12.2进程状态转换图

上述给出的进程概念对只是使用并行语言的用户是合适的,如要具体实现它，尚须涉及到进程执行模式、进程的现场活动、进程描述符和进程控制等诸多方面。

执行模式众所周知,操作系统通常包含核(Kermel)、壳(Shell)和一组实用程序(Utilities)。其中,核直接管理系统资源,处理例外和控制进程;壳称之为命令解释器,是用户和OS的界面;实用程序是附加的OS软件,提供经常使用的诸如编译器、编辑器和调试器等功能。一台计算机执行程序时提供两种执行模式：核模式和用户模式。OS中核执行在核模式(Kermel Mode),核进程在核模式下执行,这些进程由核生成以帮助管理系统资源;OS中的其它程序作为进程执行在用户模式（Us-er Mode),这样的进程称为用户进程。进程的执行模式可以在核与用户模式之间来回转换。机器开始在核模式,初始化系统和生成一些核进程后,核最终将控制传给壳(它是用户进程),它能生成一些附加的用户进程。用户进程执行中也可将执行模式切换到核模式,核完成了所请求的服务后,又能将执行模式返回到用户模式。

活动现场一个进程的活动现场，或称前后关系(Context)是程序状态的一部分,系保留在处理器的寄存器中。现场切换(Context Switch)就是保留现行进程现场,加载新的进程现场的活动过程。当进程执行模式变化时就需要施行现场切换。在切换前,用户进程的现场必须被保存在主存中,当中断处理完毕后,核就恢复用户进程现场，并将控制返回给用户进程而继续执行之。 ；

进程描述符进程的附加信息以某些数据结构保存在核空间中,其最重要者是进程描述符(Prooess Descriptor),它包含了核管理进程的如下信息： $\textcircled{1}$ 进程凭证：如进程标识符、父进程标识符、用户标识符和组标识符等； $\textcircled{2}$ 进程状态：如就绪、运行和中止等； $\textcircled{3}$ 进程现场：保持执行模式切换时的进程现场； $\textcircled{4}$ 存储映射：如各存储段的大小与访问权限、段指针与页表等； $\textcircled{5}$ 各进程信息：如打开文件、接收信号等；$\textcircled{6}$ 全局数据结构：由核管理的所有进程的队列指针和表； $\textcircled{7}$ 进程的控制与管理信息(见下）。

OS将进程描述符分为两部分:其一是各进程(Per-Process)部分,它可从进程用户空间中交换出去;其二是在所有时间均必须驻留在主存中的其它部分。在有的实现中,各进程部分被分配在用户空间,但只能由核访问。

进程控制(Process Control）进程控制是指由核对诸进程进行管理,其主要功能有： $\textcircled{1}$ 进程管理(Process Management):由核使用进程描述符去生成、中止、唤起和结束进程,管理全局数据结构和所有的各个进程的数据结构；②进程保护(Pro-cess Protection)：由核执行全面检查以确保进程只能访问规定的资源。在进程描述符中含有各种进程的权限信息。通常用户进程只能访问其用户空间,而不能访问核空间或别的进程用户空间；③进程调度(Process Scheduling)：由称之为调度器的核程序将处理器、存储器和I/O等资源指派给进程。调度器应是公平、有效的，它可根据进程描述符中所提供的进程优先信息进行调度。所谓有效的调度是指调度开销低的调度。如图12.3所示，调度有单道程序和多道程序之分。如果资源为单一用户所专用,这样的系统称为单用户单任务(Single-User Single-Tasking）系统，即单道程序设计(Uniprogramming)系统(如MicrosoftDOS),其变体方案是允许单用户的多进程同时使用资源，此即所谓的单用户多任务系统(如MicrosoftWin-dows)；如果允许很多用户同时分享系统资源，则这样的系统称为多用户多任务（Multi-UserMulti-Tasking）系统,即多道程序设计(Multiprogramming)系统(如Unix和Windows NT)。资源的共享形式,可取独占(Dedicated)方式(资源不共享）、批处理(Batching)方式(一旦调度运行就执行到完成）、分时(Time-Sharing)方式(轮流交替使用资源)和抢先(Preemptive)方式(高优先权的进程可以抢走低优先度的处理器）。

![](images/a985fe2de56984ae7ad95d3e4c7ae6b9b8dc978b8c2347368a8d5fb9da12994a.jpg)  
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

![](images/cace6c700489cca9bff834214505c52ec15d80504a928a3aed2331b122af48e0.jpg)  
图12.4Solaris操作系统中的多线程

每个进程可有一个或多个线程,进程可以被分配给一个或多个LWP,分配给进程的LWP数目称为进程的并发度。线程库调度进程线运行于LWP池上,就像核调度LWP运行于物理处理器池上一样。线程从进程外是看不到的,进程中线程的号和身份，核是不知道的,核不能管理用户级线程,只能管理LWP。

线程就像进程一样，能执行任何应用代码和系统调用。一个进程的诸线程可共享进程的地址空间,包括它的代码、它的大多数数据和大多数进程描述符信息。各个线程可彼此独立、异步地执行，当一个线程被阻塞时，其它线程可照旧执行，一个进程的多个线程可在多个处理器上同时执行。

因为线程在用户空间中由线程库执行，且进程中的线程勿须分开的地址空间,所以线程操作执行代价比进程的低。又由于线程操作(如生成、结束、同步等)均是在同一用户空间中完成,勿须进人核状态,所以因复制、现场切换、边界交叉保护等进程操作而引起的开销亦将大大降低。

# 12.3.2线程的管理

线程生成（Thread Creation）生成线程比生成进程要简单得多，因为无需生成新的地址空间,只需保存该线程所需的一些状态信息：如线程ID、处理器状态(程序计数器、堆栈指针）、线程专用栈、线程优先度、线程局部存储区等。这些信息由线程库以称之为线程结构的数据结构形式来生成和维护。

进程中的变量由进程的所有线程共享。因此，如果某一线程修改了一变量，其后果对进程的所有线程均可见。每个线程也有一局部线程存储区，用以保存该特定线程的私有变量，这不能由其它线程直接访问。

线程调度（ThreadScheduling）线程库提供一个线程调度器去调度LWP池中线程的执行。如图12.5所示，每一线程在任何时刻均处于某一状态。一个新生成的线程开始在可运行状态，它等待一个空闲的LWP到来，然后库调度它运行在LWP上，从而进入了活动状态；一个活动的线程，可被阻塞而进入睡眠状态；当阻塞条件消除时，它又被唤醒而进入可运行状态；当线程支持抢先时，一个优先级高的线程可从活动状态中抢走它的LWP；程序员可以中止一个线程使其进入停止状态；最后，当一个线程结束时，它就进人了“僵尸"(Zombie)状态。

![](images/bfd5635e9050dfd6d8e2ccceb0a22801db307809a8c3e245ecb3391dc4c4c01b.jpg)  
图12.5线程库控制的线程状态转换图

已如上述，核不能管理用户级线程，只能管理LWP。图12.6示出了由核调度LWP的状态转换图：一个运行的LWP,当被抢先或超时时就转人可运行状态；当执行阻塞系统调用时，运行的LWP被阻塞，强使LWP等待某一条件满足；当执行LWP库函数调用时,LWP被中止而进人中止状态，而执行继续库函数调用时，它又能返回至先前状态；当一个线程结束，或不再有可运行的线程时，LWP就进入空闲状态，它也可被再次唤醒而进人可运行状态。

![](images/35026fc8cfa748b233609c314aacf4d5721d52abff9c8dfe03171a0cfaf5b6da.jpg)  
图12.6核控制的LWP状态转换图

# 12.3.3线程的同步

Solaris线程库执行两种类型的同步对象：局部进程(Process-Local)和共享进程(Process-Shared)。一个局部进程同步对象,可由同一进程中的线程所访问，它用来同步相同进程中的诸线程;一个共享进程同步对象,可由多个进程所访问,它用来同步不同进程中的诸线程。

在分布式计算环境中,也提供两种类型的线程同步：互斥和条件变量。互斥用来防止多个线程在同一时间访问相同的资源;条件变量常与互斥联合使用。典型的情况是,当一线程需要某一资源时,它就使用互斥排斥其它线程的访问；如果资源无效，线程就根据条件变量等待之，稍后条件满足时就可再启动。

# \*12.4同 步

同步这一术语,在计算机的很多课程(例如系统结构、操作系统、数据库、并行处理和程序设计语言等)中经常出现,其意义和用法也不尽相同,且其实现方法亦颇多，所以有必要专辟一节深人学习之。

一般而言，同步操作,如图12.7所示,可分为三类：原子操作,数据同步和控制同步。所有在共享存储的机器(PVP、SMP、DSM等)上的同步通常使用锁原语实现;在分布存储的机器(MPP和机群等)上的同步使用消息传递原语实现。

![](images/9d50b5e47136a333c89ec7139d1221fdab7a3f000927cc8c6bd538627ad1e7e4.jpg)  
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

![](images/2db295085f3c30b7027f1e7b86ad1abb4c0f6f1c3593e7d72c7966036fc3904a.jpg)  
图12.8通信协议不同结构

通信对并行计算的性能影响很大，而影响通信性能的主要因素有通信硬件（包括节点存储器 $\cdot \mathbf { I } / 0$ 结构、网络界面和通信网络本身等),通信软件(包括通信协议结构和算法等),所提供的通信服务(包括消息传送、流控、失效处理和保护等）等。

# 12.5.1影响通信系统性能的因素

通信硬件典型的通信硬件结构示于图12.9。在松散耦合的系统中，网络接口电路 NIC(Network Interface Circuitry)搭接在I/O 总线(例如 PCI)上。一条发送的消息,从发送节点的存储器出发,经过存储总线、I/O总线、NIC,最后送至网上,其间可达到的通信带宽受限于该路径上最慢的部件,而实际上的通信瓶颈常在存储带宽而不是网络带宽，因为很多通信方案均涉及到DMA访问，待发送的数据在发出去之前首先要复制到DMA缓冲器，而这种存储复制的带宽远远小于存储总线的峰值带宽。

![](images/fb30ef903a546eff3e2dfe570c89470068379c48c5d69eeaf59e6d642f289d16.jpg)  
图12.9典型的通信硬件结构

通信硬件中NIC是个很关键的电路,它应具有DMA功能;有自己的通信处理器(协处理器),主要用于初始化DMA、打包/拆包、保护检查等;应有存放 NIC代码和临时缓冲消息的存储器；也还应有缓冲信包的一些FIFO等。

通信软件在现代的机群和 MPP系统中，软件开销占通信时间的主导地位。如果没有良好的通信软件，即使有非常有效的网络和NIC,其通信时间也难以明显下降。软件开销主要来源于：①穿越多层协议所需的软件开销；②由于消息通信所涉及的一些存储复制操作所引起的开销；③传输消息时多次跨越保护边界所造成的通信开销(一般至少穿越四次：在发方和收方分别从用户空间进入和离开核空间)。对付第一个问题可以使用简化的通信协议;对付第二个问题可以使用零复制协议(Zero-Copy Protocol),即消息直接从源节点的发送缓冲器到目的节点的接收缓冲器而不缓冲在存储区中；对付第三个问题可以使用用户级技术,即所有的通信均完全执行在用户空间。

通信服务所提供的通信服务会大大影响通信系统的性能，所期望的服务包括：①可靠传输，一旦消息发出就应确保它能正确无误地去向目的地且信包不会丢失； $\textcircled{2}$ 流控，消息不应死锁、拥挤和使缓存溢出； $\textcircled{3}$ 失效处理，包括错误检测、重发、校正等； $\textcircled{4}$ 有序传输，在任何情况下应保障接收消息顺序的正确性。

# 12.5.2低级通信支持

在改进通信性能方面，BCL起着关键的作用。本节简要讨论三种有代表性的 BCL，即双复制(用户空间协议）、单复制(快速消息)和零复制。

双复制(2-Copy） 最好以IBMSP的通信过程(图12.10)说明之。SP通信协议要求发送节点处理器首先将数据从发送缓冲器复制到管道缓冲器；然后再从管道缓冲器复制到虚拟开关界面中的输出队列。接收节点处理器以相反的次序执行相同的动作。参照图12.11,消息层和管道层形成了基本通信库(层)BCL。其中消息层系由一些简单的、非阻塞的、点到点的通信库组成,MPI和PVM等中所有高级消息传递功能均由这些原语实现；管道层维持成对发/收进程之间可靠的、具有流控的、有序的字节流。当源节点处理器执行一条消息层发送操作时，它就将数据从发送缓冲器复制到管道缓冲器；然后消息层再调用管道层代码将数据从管道缓冲器复制到输出队列；源适配器用DMA将数据再从输出队列移到适配器，最终将数据经网络传至目的适配器；目的适配器用DMA将进来的数据传至目的节点的输入队列；目的节点处理器执行一条管道层接收操作，它就将数据从输人队列复制到管道缓冲器；管道层调用消息层代码将数据从管道缓冲器复制到最终的接收缓冲器。

![](images/b74e57d7ad6adb51a221e55c3cb6c3201a40f0b46ced721236236e1832a486a9.jpg)  
图12.10 IBM SP通信中的数据移动

![](images/129653b527dded990a3c8c3f99c70656512f5d982b3ca1509afd462cedb5a1d5.jpg)  
图12.11 IBM SP通信软件

单复制(1-Copy） 单复制又称快速消息FM(Fast Message),主要支持机群和 MPP上低延迟、高带宽通信,其目的是在消息层提供足够的功能使得较高级原语(如PVM、MPI套接字等)所实现的通信性能接近于硬件极限。

FM数据结构和功能非常类似于主动消息，但它简单，只包含很少的几个通信原语,例如,FM_initialize(）,用于初始化;FM_send(dest,h,buf,size),用于发送存储器中长消息； $\mathbf { F M } _ { - } \ s e n d \_ { 4 } ( \operatorname { d e s t } , h , i _ { 0 } , i _ { 1 } , i _ { 3 } )$ ,用于发送寄存器中4字消息；FM_extract（）,用于抽取接收的消息和调用处理程序。

FM是一个用户级通信层，一旦初始化后，适配存储器和节点接收队列都暴露在用户级,随后的FM_send和FM_extract均不必有跨边界保护。当发送节点处理器从缓冲中取出数据并组装成信包后，就直接将其存人适配器的发送队列中,然后信包在DMA控制下注人到网络;当信包到达接收节点时，仍由DMA控制将其放人适配器接收队列，稍后移人节点接收队列，最后调用处理程序将消息数据移进用户存储空间。

零复制（Zero-Copy） 这种通信机制由Princeton的 SHRIMP项目实现，又叫作虚拟存储映射通信,它能提供真正的零复制通信协议。当节点间进行发送/接收时，节点中的守护程序可以通过网络在发送节点和接收节点之间建立人-出关系；然后发送节点的进程就能将其源缓冲器(用户空间)中的消息，直接发送给另一节点中的目的缓冲器，而不须要穿越核空间中的DMS缓冲器。

# 12.5.3 TCP/IP通信协议组简介

网络上的通信通常由一组协议实现，协议就是一组控制数据格式和数据如何传输的规则。本节主要讨论TCP/IP协议组的性质;经常使用的UDP、TCP和IP协议的基本概念与特点;最后讨论应用编程界面API(Application Pro-gramming Interface),即俗称的套接字(Sockets)。

TCP/IP协议组性质目前两种广泛使用的通信协议是由ISO(Interna-tional Standard Organization）制定的 OSI(Open System Interconnect）和由 IAB(Internet Activities Board)制定的 TCP/IP,其对应关系示于图12.12中。TCP/IP(Transmisson Control Protocol/Internet Protocol)协议组涉及到三层：应用层（包括FTP、TELNET、SMTP、SNMP、HTTP）、传输层(包括 TCP 和 UDP)和网络层(包括IP)。TCP层附有TCP头形成称之为TCP段的传输层消息；IP层附有IP头形成称之为IP数据报的网络层消息：NAP层附有以太网头形成称之为以太网帧的NAP层消息。应用层协议必须告诉下层协议目的进程的地址，这通常以(IP地址，端口)数偶形式给出，其中IP地址唯一地指定了目的主机，而端口号指明目的进程。

用户数据报协议 UDP(User Datagram Protocol）TCP/IP 协议组包括两个传输层协议：TCP和UDP,两者均操作在IP协议之上。其中UDP是个非常简单的传输层协议，消息以数据报的格式组装。UDP是一种非连接协议，它就像邮局发信一样，发送者发出数据并不建立连接，而是将大量数据分割并封装成单独的数据报(信件),然后分开发出去(这和下面将要讨论的TCP不一样,它先要建立连接,然后以连续的数据流而不是单独的数据报形式发送)。UDP协议努力将邮件传送好，但并不保证无误传输。一个UDP数据报可能遭到损害或丢失,但在接收端可通过检查和查出错误,并甩掉受损的数据报。UDP对不严格要求确保无误的传输是合适的，否则要使用TCP协议。

![](images/9fc779e993c1daad6ad97e1a0c70cf5461708e213df43af47282f63463a2af1f.jpg)  
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

![](images/803891719e121704502e99e9c20c3716308868f5fdc09403bb71536cd4082ae0.jpg)  
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

![](images/8aea6c0d66914f30a6fa363c5ffac57af6af3b314dbcdd49b250af6e31d6daac.jpg)  
图13.1五种并行编程风范(a)相并行；(b)分治并行;(c)流水线并行;(d)主-从并行;(e)工作池并行

# 13.1.2计算 $\pmb { \pi }$ 样本程序

为了以下各节讨论方便和具体,先选择一个样本程序,以其为例进行讨论和相互对照。在此所讲的样本程序，并非普通意义下的“标准样板"程序，它只不过是一个简单、易于实现、且便于理解的一个计算程序罢了。习惯上,作为教材，选择了这样一个大家都不生疏的用数值积分法求π近似值的样本程序。

参照图13.2,用数值积分法计算 $\pmb { \pi }$ 时，就是要求出在压间[0,1]内函数曲线$4 / ( 1 + x ^ { 2 } )$ 下的面积，此面积就是 $\pmb { \pi }$ 的近似值，为此先将区间[0,1]划分成N个等间隔的子区间，每个子区间的宽度为 $1 / N$ ;然后计算出各子区间中点处的函数值；再将各个子区间面积相加就可得出 $\pmb { \pi }$ 的近似值。其计算公式如下：

![](images/abb73a3ab832b2f8e1466fda62a26b66e8976df237c7c40ac752e1ad6467c202.jpg)  
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

![](images/033232ec1c74619dd710746900ff900673ea94d7aee47703283f7107bdc6ded9.jpg)  
图13.3 ANSI X3H5标准中并行结构

在并行结构内可有一些并行块(psections...end psections）、并行循环(pdo...endpdo)或单一进程(psingle..endpsingle)等结构,其中并行块用以指明 MPMD并行性,并行循环用于指明 SPMD并行性,而单一进程结构指明代码仅由一个线程顺序执行。

图13.3中的代码执行顺序可以更清楚地示于图13.4中。假定有三个线程P、Q和R：开始基线程P执行代码A;当遇到parallel时就生成两个子线程Q和R,所以代码B被复制成三份;在并行块(psections)中两段代码C和D被并行执行；单进程代码E仅由Q执行；并行循环(pdo)有6次迭代，由三个线程分摊执行；接着 $\mathrm { P } \setminus \mathrm { Q } , \mathrm { R }$ 并行执行代码G；最后由基线程 $\mathbf { P }$ 执行代码 $\mathbf { H } _ { \circ }$ 在此执行过程中,在 parallel、endpsections、end psingle、end pdo 和 end parallel 处设有隐路障(Implicit Barrier),它们也称为栅栏操作(Fence Operation),强使所有存储访问统一于一点以保持一致;如果勿需等待,亦可使用勿需等待隐路障,简称为无隐路障(No Implicit Barrier)。

![](images/3bdccb346590e4bb05bd5265d190763caee6ffbae1aaf2e3b137ec05edc3fe86.jpg)  
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