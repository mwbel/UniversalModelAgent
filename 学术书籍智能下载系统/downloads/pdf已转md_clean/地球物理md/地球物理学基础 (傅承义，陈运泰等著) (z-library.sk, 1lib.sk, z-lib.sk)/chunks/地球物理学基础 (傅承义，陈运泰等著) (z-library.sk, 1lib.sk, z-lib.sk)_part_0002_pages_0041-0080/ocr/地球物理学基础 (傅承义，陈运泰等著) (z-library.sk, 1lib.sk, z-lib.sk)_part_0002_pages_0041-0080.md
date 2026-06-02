函数 $\phi _ { \pmb { n } }$ 在 $\pmb { r }  \infty$ 时是有限的。因

$$
r ^ { 2 } = x ^ { 2 } + y ^ { 2 } + z ^ { 2 } ,
$$

$\lambda > 0$ ，则 $c ^ { 2 } + \lambda \leqslant r ^ { 2 } \leqslant a ^ { 2 } + \lambda , \ : \ : \operatorname* { l i m } _ { r \to \infty } \frac { r } { \sqrt { \lambda } } = 1 ,$

$$
\operatorname* { l i m } _ { r \to \infty } r \phi _ { n } = \operatorname* { l i m } _ { r \to \infty } r \int _ { r ^ { 2 } } ^ { \infty } \left( { \frac { r ^ { 2 } } { \lambda } } - 1 \right) ^ { n } { \frac { d \lambda } { \lambda ^ { 3 / 2 } } } = ( - 1 ) ^ { n } { \frac { n ! 2 ^ { n + 1 } } { 1 \cdot 3 \cdot 5 \cdot \cdot \cdot ( 2 n + 1 ) } } \circ
$$

对以后讨论最有关系的函数是 $\phi _ { 0 }$ 和 $\phi _ { 1 0 }$ 此处只讨论旋转椭球面,即 ${ \pmb a } = { \pmb b }$ 的情况。

$$
\phi _ { 0 } = \int _ { \imath } ^ { \infty } { \frac { d \lambda } { ( a ^ { 2 } + \lambda ) ( c ^ { 2 } + \lambda ) ^ { 1 / 2 } } } = { \frac { \imath } { ( a ^ { 2 } - c ^ { 2 } ) ^ { 1 / 2 } } } \tan ^ { - 1 } E ( \lambda ) { \mathsf { o } }
$$

$$
E ( \lambda ) = \Big ( \frac { a ^ { 2 } } { c ^ { 2 } } \frac { - c ^ { 2 } } { + \lambda } \Big ) ^ { 1 / 2 } \circ
$$

在 $\scriptstyle { E _ { 0 } }$ 上， $\lambda = 0$ ，

$$
E ( 0 ) = \varepsilon = { \frac { ( a ^ { 2 } - c ^ { 2 } ) ^ { 1 / 2 } } { c } } _ { 0 }
$$

ε是纵截面的偏心率。故在 $\scriptstyle { E _ { 0 } }$ 上， $\phi _ { 0 }$ 是个常数。

$$
\begin{array} { l } { \phi _ { 1 } = \displaystyle \int _ { \imath } ^ { \infty } \left( \frac { x ^ { 2 } + y ^ { 2 } } { a ^ { 2 } + \lambda } + \frac { z ^ { 2 } } { c ^ { 2 } + \lambda } - 1 \right) \frac { d \lambda } { ( a ^ { 2 } + \lambda ) ( c ^ { 2 } + \lambda ) ^ { 1 / 2 } } } \\ { = ( x ^ { 2 } + y ^ { 2 } ) A _ { 1 } + z ^ { 2 } A _ { 3 } - \phi _ { 0 } , } \end{array}
$$

式中

$$
A _ { 1 } = \int _ { \lambda } ^ { \infty } \frac { d \lambda ~ \cdot ~ \cdot } { ( a ^ { 2 } + \lambda ) ( c ^ { 2 } + \lambda ) ^ { 1 / 2 } } - \frac { 1 } { \varepsilon ^ { 3 } c ^ { 3 } } \Big ( \tan ^ { - 1 } E - \frac { E } { 1 + E ^ { 2 } } \Big ) ,
$$

$$
{ \cal A } _ { 3 } = \int _ { \lambda } ^ { \infty } { \frac { d \lambda } { ( a ^ { 2 } + \lambda ) ( c ^ { 2 } + \lambda ) ^ { 3 / 2 } } } = { \frac { 2 } { \varepsilon ^ { 3 } c ^ { 3 } } } ( E - \tan ^ { - 1 } E ) _ { 0 }
$$

令 $x ^ { 2 } + y ^ { 3 } = s ^ { 2 }$ ，则 $\scriptstyle { E _ { 0 } }$ 的方程可以写成 $z ^ { 2 } = c ^ { 2 } ( 1 - s ^ { 2 } / a ^ { 2 } ) ,$ 。

$$
\phi _ { 1 } = s ^ { 2 } { \cal A } _ { 1 } + c ^ { 2 } ( 1 - s ^ { 2 } / a ^ { 2 } ) { \cal A } _ { 3 } - \phi _ { 0 0 }
$$

故 $\phi _ { 1 }$ 只与 $s ^ { 2 }$ 成线性关系。

# （四）重力公式的精确解

现在要解决的问题是要确定一个重力场使它满足以下的条件：

$\textcircled{1}$ 它必须等于引力场与离心力场之和。  
$\textcircled{2}$ 它的一个等位面必须是一个旋转椭球面 $\scriptstyle { E _ { 0 } }$ ，其对称轴与旋转轴重合。$\textcircled{3}$ 产生引力位的所有质量都在椭球面 $\scriptstyle { E _ { 0 } }$ 之内。  
$\textcircled{4}$ 引力位必须满足 $\operatorname* { l i m } _ { r \to \infty } r V = G M$

根据这些条件，首先可以将重力位写为

$$
W = V + \frac { 1 } { 2 } \ \omega ^ { 2 } ( x ^ { 2 } + y ^ { 2 } ) = V + \frac { 1 } { 2 } \ \omega ^ { 2 } s ^ { 2 } { _ 0 }
$$

因在 $\pmb { { \cal E } } _ { 0 }$ 上 $\pmb { W }$ 是一常数,故可将 $\pmb { V }$ 写成 $\phi _ { 0 }$ 及 $\phi _ { 1 }$ 的线性组合

将(2.91)及(2.94)代人并比较两端 $s ^ { 2 }$ 的系数,得

$$
\begin{array} { r } { K _ { 2 } = \frac { a \omega ^ { 2 } } { 2 \left( c ^ { 2 } A _ { 3 } - a ^ { 2 } A _ { 1 } \right) } = - \frac { \varepsilon ^ { 3 } c ^ { 3 } \omega ^ { 2 } \left( 1 \mathrm { ~ + ~ } \varepsilon ^ { 2 } \right) } { 2 [ \left( 3 \mathrm { + } \varepsilon ^ { 2 } \right) \tan ^ { - 1 } \varepsilon \mathrm { - } 3 \varepsilon ] } \circ } \end{array}
$$

由

$$
\operatorname * { l i m } _ { r  \infty } r V = \operatorname * { l i m } _ { r  \infty } r ( K _ { \imath } \phi _ { \flat } + K _ { \imath } \phi _ { \imath } ) = G M ,
$$

得

$$
K _ { \mathfrak { s } } = \frac { 1 } { 2 } G M + \frac { 2 } { 3 } K _ { 2 0 }
$$

故

$$
W = K _ { 1 } \phi _ { 0 } + K _ { 2 } \phi _ { 1 } + \frac { 1 } { 2 } \omega ^ { 2 } s ^ { 2 } = \frac { 1 } { 2 } \Big ( G M + \frac { 2 } { 3 } K _ { 2 } \Big ) \phi _ { 0 } + K _ { 2 } \phi _ { 1 } + \frac { 1 } { 2 } \omega ^ { 2 } s ^ { 2 } ,
$$

式中的 $\phi _ { \Phi } , \phi _ { 1 }$ 及 $\pmb { K } _ { 2 }$ 可用式(2.91),(294)及(2.96)代人。

重力 $\pmb { g }$ 的分量 ${ \pmb g } ,$ 和 $g _ { z }$ 可由下式计算：

$$
g _ { \ast } = - \frac { \partial W } { \partial s } = - K _ { 1 } \frac { \partial \phi _ { 0 } } { \partial s } - K _ { 2 } \frac { \partial \phi _ { 1 } } { \partial s } - \omega ^ { 2 } s ,
$$

$$
g _ { z } = - \frac { \partial W } { \partial z } = - K _ { 1 } \frac { \partial \phi _ { 0 } } { \partial z } - K _ { 2 } \frac { \partial \phi _ { 1 } } { \partial z } \circ
$$

由 $\phi _ { 0 }$ 及 $\phi _ { 1 }$ 的定义，得

$$
\begin{array} { r l } & { \frac { \partial \phi _ { 0 } } { \partial s } = \frac { - 2 s } { ( a ^ { 2 } + \lambda ) ^ { 2 } ( c ^ { 2 } + \lambda ) ^ { 1 / 2 } } \frac { 1 } { P ( \lambda ) } , \ \frac { \partial \phi _ { 1 } } { \partial s } = 2 s A _ { 1 } , } \\ & { \frac { \partial \phi _ { 0 } } { \partial z } - \frac { - 2 z } { ( a ^ { 2 } + \lambda ) ( c ^ { 2 } + \lambda ) ^ { 3 / 2 } } \frac { 1 } { P ( \lambda ) } , \ \frac { \partial \phi _ { 1 } } { \partial z } = 2 s A _ { 3 } , } \end{array}
$$

故

$$
g _ { s } = \frac { 2 s \Big ( \frac { 1 } { 2 } ~ G M + \frac { 2 } { 3 } ~ K _ { 2 } \Big ) } { ( a ^ { 2 } + \lambda ) ^ { 2 } ( c ^ { 2 } + \lambda ) ^ { 1 / 2 } } \frac { 1 } { P ( \lambda ) } - \frac { 2 s K _ { 2 } } { ( a ^ { 2 } - c ^ { 2 } ) ^ { 3 / 2 } } \Big ( \mathfrak { t a } ^ { - 1 } E - \frac { E } { 1 + E ^ { 2 } } \Big ) - \omega ^ { 2 } s ,
$$

$$
g _ { z } = \frac { 2 z \left( \frac { 1 } { 2 } \ G M + \frac { 2 } { 3 } \ K _ { 2 } \right) } { ( a ^ { 2 } + \lambda ) ( c ^ { 2 } + \lambda ) ^ { 3 / 2 } } \frac { 1 } { P ( \lambda ) } - \frac { 4 z K _ { 2 } } { ( a ^ { 2 } - c ^ { 2 } ) ^ { 3 / 2 } } \left( E - \tan ^ { - 1 } E \right) _ { 0 }
$$

右令 $s = ( a ^ { 2 } + \lambda ) ^ { 1 / 2 }$ ， $z = ( c ^ { 2 } + \lambda ) ^ { 1 / 2 }$ ，则得到 $\pmb { g }$ 在 ${ \pmb E } _ { \pmb { \lambda } }$ 的赤道及两极的 $\pmb { g }$ 值 ${ \pmb g } _ { \pmb { a } \pmb { \mathscr { s } } }$ 及 ${ \pmb g } _ { e } { \pmb x }$ 并由此得出

$$
{ \frac { 2 g _ { a , 1 } } { ( a ^ { 2 } + \lambda ) ^ { 1 / 2 } } } + { \frac { g _ { c , 1 } } { ( c ^ { 2 } + \lambda ) ^ { 1 / 2 } } } = { \frac { 3 G M } { ( a ^ { 2 } + \lambda ) ( c ^ { 2 } + \lambda ) ^ { 1 / 2 } } } - 2 \omega _ { \circ } ^ { 2 }
$$

此式称为庇猜梯（Pizzetti）定理。当 $\lambda = 0$ 时，

$$
\frac { 2 g _ { e } } { a } + \frac { g _ { p } } { c } - \frac { 3 G M } { a ^ { 2 } c } - 2 \omega ^ { 2 } = 4 \pi G \rho _ { m } - 2 \omega ^ { 2 } \circ
$$

g.和g,是地球赤道和两极的重力值,pm是地球的平均密度。

由式(2.99)还可得到

$$
\frac { g _ { c s 1 } } { ( c ^ { 2 } + \lambda ) ^ { 1 / 2 } } - \frac { g _ { a s 1 } } { ( a ^ { 2 } + \lambda ) ^ { 1 / 2 } } = \frac { 2 K _ { 2 } } { ( a ^ { 2 } - c ^ { 2 } ) ^ { 3 / 2 } } \left[ 3 \tan ^ { - 1 } E - \frac { 3 + 2 E ^ { 2 } } { 1 + E ^ { 2 } } E \right] + \omega ^ { 3 } ,
$$

当 $\lambda = 0$ 时,此式可写成

$$
\frac { g _ { \widehat { r } } } { g _ { e } } - \frac { c } { a } = \frac { g _ { \widehat { r } } - g _ { e } } { g _ { , } } + \frac { a - c } { a } = \beta + \epsilon = 2 q ( \varepsilon ) \frac { \omega ^ { 2 } c } { g _ { e } } ,
$$

式中

$$
q ( \varepsilon ) = \frac { \varepsilon ^ { 2 } ( \varepsilon - \tan ^ { - 1 } \varepsilon ) } { ( 3 + \varepsilon ^ { 2 } ) \tan ^ { - 1 } \varepsilon - 3 \varepsilon } , \varepsilon = E ( 0 ) = \frac { ( a ^ { 2 } - c ^ { 2 } ) ^ { 1 / 2 } } { c } \circ
$$

与克雷若定理相比,此式可以改写成

$$
\begin{array} { r } { \beta + { \it e } = \frac { 5 } { 2 } { m } \left[ \frac { 4 } { 5 } \left( 1 - e \right) q ( { \tt e } ) \right] , { m } = \frac { \omega ^ { 2 } a } { g _ { e } } , } \end{array}
$$

而因子 $\frac { 4 } { 5 } \left( { \bf l } - { \epsilon } \right) q ( \varepsilon ) \approx 1 \mathrm { ~ }$ 。克雷若定理是近似的,上式是它的修正。

$\scriptstyle { E _ { 0 } }$ 是相当于 $\lambda = 0$ 的旋转椭球面。若它是一个等位面，就可以计算面上的重力值。索米扬那（C.Somigliana）首先证明在 $\scriptstyle { \mathbf { } } _ { E _ { 0 } }$ 上的任何三个重力值有一定的关系。这个关系叫做索米扬那公式。

设所有的质量都包含在 $E _ { \mathfrak { d } }$ 之内。取两个函数 $V _ { \mathfrak { d } }$ 和 $V$ 。它们在 $\scriptstyle { E _ { 0 } }$ 之外是谐函数,但在 $E _ { 0 }$ 之上，取值

$$
V _ { \circ } = 1 , \quad V _ { \circ } = s ^ { 2 } ,
$$

在远处，

$$
\operatorname* { l i m } _ { r  \infty } r V _ { \circ } = m _ { 0 } , \ : \ : \ : \ : \operatorname* { l i m } _ { r  \infty } r V _ { 1 } = m _ { 1 0 }
$$

$m _ { 0 } , \ m _ { 1 }$ 是两个任意常数。按照狄利克雷定理， $ { \boldsymbol { V } } _ { 0 }$ 和 $V _ { \parallel }$ 是完全确定的。所以重力位可以写为

$$
W = V + \frac { 1 } { 2 } \omega ^ { 2 } s ^ { 2 } = K V _ { \circ } - \frac { 1 } { 2 } \omega ^ { 2 } V _ { \circ } + \frac { 1 } { 2 } \omega ^ { 2 } s ^ { 2 } { _ { \circ } }
$$

此式在 $\scriptstyle { E _ { 0 } }$ 上等于常数 $K$ 。因

$$
\operatorname * { l i m } _ { r  \infty } r V = G M ,
$$

故

$$
\{ \begin{array} { l }  { K = { \begin{array} { c } { { G { \frac { M } { m } } } \end{array} } + { \frac { \omega ^ { 2 } m } { 2 m _ { 0 } } } , } } \\  { | \begin{array} { l } { { \begin{array} { l } { { } \\ { { W = ( { \begin{array} { c } { { G M } } \end{array} } + { \begin{array} { c } { { \omega ^ { 2 } m _ { 1 } } } } \\ { { m _ { 0 } } } \end{array} } ) V , - { \frac { 1 } { 2 } } } \omega ^ { 2 } V _ { 1 } + { \frac { 1 } { 2 } } \omega ^ { 2 } s ^ { 2 } , } } \\ { { g = - \begin{array} { c } { { \partial { } { \underline { { { W } } } } } } \end{array} } = - { ( \begin{array} { l } { { G { \underline { { { M } } } } } } \\ { { m _ { 0 } } } \end{array} + \begin{array} { c } { { \omega ^ { 2 } m _ { 1 } } } \\ { { 2 m _ { 0 } } } \end{array} ) } { \frac { \partial V _ { 0 } } { \partial n } } + { \frac { 1 } { 2 } } \omega ^ { 2 } { - } { \frac { \partial } { \partial \tau } } ( V _ { 1 } - s ^ { 2 } ) _ { 0 } } \end{array} } } \end{array}  \end{array}
$$

在 $E _ { \mathfrak { d } }$ 上取任意三点 $\boldsymbol { \mathrm { ~ \mathcal { P } ~ } } _ { \iota } \left( \iota = 1 , 2 , 3 \right)$ ，则

$$
g _ { \iota } = - \left( \frac { G M } { m _ { 0 } } \ + \ \frac { \omega ^ { 2 } m _ { 1 } } { 2 m _ { 0 } } \right) \left( \frac { \partial V _ { 0 } } { \partial n } \right) _ { \iota } + \ \frac { \omega ^ { 2 } } { 2 } \ \frac { \partial } { \partial n } \ ( V _ { 1 } - s ^ { 2 } ) , \ ( \iota = 1 , 2 , 3 ) _ { 0 }
$$

若以上三式不矛盾，必须有

$$
\begin{array} { r } { \left| g _ { 1 } \left( \begin{array} { c } { \partial V _ { 0 } } \\ { \partial n } \end{array} \right) _ { 1 } \left[ \begin{array} { c } { \underline { { \partial } } } \\ { \partial n } \end{array} \left( V _ { 1 } - s ^ { 2 } \right) \right] _ { 1 } \right| } \\ { \left| g _ { \cdot } \left( \begin{array} { c } { \underline { { \partial } } V _ { 0 } } \\ { \partial n } \end{array} \right) _ { 2 } \left[ \begin{array} { c } { \underline { { \partial } } } \\ { \partial n } \end{array} \left( V _ { 1 } - s ^ { 2 } \right) \right] _ { 2 } \right| = 0 _ { 0 } } \\ { \left| g _ { \cdot } \left( \begin{array} { c } { \underline { { \partial } } V _ { \underline { { \circ } } } } \\ { \partial n } \end{array} \right) _ { 3 } \left[ \begin{array} { c } { \underline { { \partial } } } \\ { \partial n } \end{array} \left( V _ { 1 } - s ^ { 2 } \right) \right] _ { 3 } \right| } \end{array}
$$

比较式(2.102)与式（2.98)，可以选择适当的m。与m以使两式中Φ与V。的系数儿全相等。于是得

$$
V _ { \scriptsize 0 } = \phi _ { \scriptsize 0 } , ~ V _ { \scriptsize 1 } = - \frac { 2 K _ { \scriptsize 2 } } { \omega ^ { \scriptsize 2 } } \phi _ { \scriptsize 1 } ,
$$

故

$$
\begin{array} { r l r } {  { \frac { \partial V _ { \circ } } { \partial n } = \frac { \partial \phi _ { 0 } } { \partial n } = [ ( \frac { \partial \phi _ { 0 } } { \partial \varepsilon } ) ^ { 2 } + ( \frac { \partial \phi _ { 0 } } { \partial \varepsilon } ) ^ { 2 } ] ^ { 1 / 2 } } } \\ & { } & { = \frac { \partial \phi _ { 0 } } { \partial \lambda } [ ( \frac { \partial \lambda } { \partial s } ) ^ { 2 } + ( \frac { \partial \lambda } { \partial z } ) ^ { 2 } ] ^ { 1 / 2 } = \frac { 1 } { \sqrt { P ( \lambda ) } } \frac { 2 } { ( a ^ { 2 } + \lambda ) ( c ^ { 2 } + \lambda ) ^ { 1 / 2 } } \circ } \end{array}
$$

变换坐标,使

$$
\begin{array} { l } { { s = ( a ^ { 2 } + \lambda ) \cos \phi \sqrt { P ( \lambda ) } \mathrm { , } } } \\ { { z = ( c ^ { 2 } + \lambda ) \sin \phi \sqrt { P ( \lambda ) } \mathrm { o } \mathrm { } } } \end{array}
$$

$\pmb { \phi }$ 是通过 $\pmb { P }$ 点 $\scriptstyle { E _ { 0 } }$ 的法线与 $\pmb { x y }$ 面所夹的角(即纬度),

$$
P ( \lambda _ { \iota } ) = \frac { s _ { \iota } ^ { 2 } } { ( a ^ { 2 } + \lambda _ { \iota } ) ^ { 2 } } + \frac { z _ { \iota } ^ { 2 } } { ( c ^ { 2 } + \lambda _ { \iota } ) ^ { 2 } } \circ
$$

由(2.104),并令 $\lambda = 0$ ，立得

$$
{ \frac { 1 } { P ( 0 ) } } = a ^ { 2 } \cos ^ { 2 } \phi + c ^ { 2 } \sin ^ { 2 } \phi ,
$$

故

$$
\left( \frac { \partial V _ { \ L \ L _ { 0 } } } { \partial n } \right) _ { \ L _ { \ L { 1 } = \ L \ L _ { 0 } } } = \frac { 2 ( 1 + \varepsilon ^ { \varepsilon } \cos ^ { 2 } \phi ) ^ { 1 / 2 } } { a ^ { 2 } } ,
$$

可以证明

$$
\begin{array} { l } { { \displaystyle \frac { \partial } { \partial n } ~ ( V _ { 1 } - s ^ { 2 } ) _ { \lambda = 0 } = \frac { 4 c } { ( 1 + \varepsilon ^ { 2 } \cos ^ { 2 } \psi ) ^ { 1 / 2 } } , } } \\ { { \displaystyle \ } } \\ { { \displaystyle \varepsilon = ( a ^ { 2 } - c ^ { 2 } ) ^ { 1 / 2 } / c _ { 0 } } } \end{array}
$$

代人(2103),化简后,得

$$
\begin{array} { r l r } {  { g _ { 1 } ( \cos ^ { 2 } \phi _ { 2 } - \cos ^ { 2 } \phi _ { 3 } ) ( 1 + \varepsilon ^ { 2 } \cos ^ { 2 } \phi _ { 1 } ) ^ { 1 / 2 } + g _ { 2 } ( \cos ^ { 2 } \phi _ { 3 } - \cos ^ { 2 } \phi _ { 1 } ) ( 1 + \varepsilon ^ { 2 } \cos ^ { 2 } \phi _ { 2 } ) } } \\ & { } & { + g _ { 3 } ( \cos ^ { 2 } \phi _ { 1 } - \cos ^ { 2 } \phi _ { 2 } ) ( 1 + \varepsilon ^ { 2 } \cos ^ { 2 } \phi _ { 3 } ) = 0 , \qquad ( 2 . 1 0 3 . } \end{array}
$$

$\phi _ { i } = 0 , \phi _ { i } = { \frac { \pi } { 2 } } , \phi _ { i } = \phi ;$

$$
\begin{array} { r l } & { g = \frac { g _ { r } \sin ^ { 2 } \phi + g _ { e } ( 1 + \varepsilon ^ { 2 } ) ^ { 1 / 2 } \cos ^ { 2 } \phi } { ( 1 + \varepsilon ^ { 2 } \cos ^ { 2 } \phi ) ^ { 1 / 2 } } } \\ & { ~ - \frac { a g _ { e } \cos ^ { 2 } \phi + c g _ { \phi } \sin ^ { 2 } \phi } { ( a ^ { 2 } \cos ^ { 2 } \phi + c ^ { 2 } \sin ^ { 2 } \phi ) ^ { 1 / 2 } } } \\ & { ~ - g _ { e } \frac { 1 + ( \beta - e - \varepsilon \beta ) \sin ^ { 2 } \phi } { ( 1 - e ( 2 - \varepsilon ) \sin ^ { 2 } \phi ) ^ { 1 / 2 } } , } \end{array}
$$

$$
\epsilon = \frac { a - c } { a } , \beta = \frac { g _ { p } - g _ { c } } { g _ { e } } \circ
$$

上式称为索米扬那公式。这是一个精确的公式而不是一个几近公式。可以证明，若将上式展开至二级小数,所得结果与式(2.84)是完全一样的。为了数值计算的方便,式(2.84)更为有用。

以上所讨论的重力公式都是相对于一个与大地水准面最逼近的旋转椭球面；这个面是一个重力等位面并包含所有的质量;它叫做参考椭球面。这个面的形状和大小完全可以由赤道半径 $\pmb { \alpha }$ 和扁率 $^ { e }$ 来确定。与它相应的重力公式则可以由 $\pmb { \omega }$ ，GM, $\pmb { a }$ ， $^ e$ 或 $\omega$ ， ${ { g } _ { e } } ,$ $a , \sigma$ 完全确定。

现在通用的参考系有两个：

$\textcircled{1}$ 国际参考椭球1930

$a = 6 3 7 8 , 3 8 8$ 米，  
$\begin{array} { r } { \begin{array} { r } { e = 1 / 2 9 7 . 0 = 0 . 0 0 3 3 6 7 , } \end{array} } \end{array}$   
$g _ { \epsilon } = 9 . 7 8 0 4 9 0$ 米/秒,  
$\omega = 7 . 2 9 2 1 1 5 \times 1 0 ^ { - 5 }$ 弧度/秒，  
$g = 9 . 7 8 0 4 9 0 ( 1 + 0 . 0 0 5 2 8 8 3 \sin ^ { 2 } \varphi - 0 . 0 0 0 0 5 9 \sin ^ { 2 } 2 \varphi )$ 米/秒,${ \mathfrak { P } } =$ 地理纬度。

$\textcircled{2}$ 国际参考椭球1967

$a = 6 3 7 8 1 6 0$ 米，  
$J _ { 2 } = 1 0 8 2 . 7 \times 1 0 ^ { - 6 } ,$   
$G M = 3 . 9 8 6 0 3 \times 1 0 ^ { 1 4 }$ 米/秒²。

由此导出 $e = 1 / 2 9 8 . 2 5$ ， $g _ { e } = 9 . 7 8 0 3 1 8$ 米/秒。故

$$
g = 9 . 7 8 0 3 1 8 ( 1 + 0 . 0 0 5 3 0 2 4 \sin ^ { 2 } \varphi - 0 . 0 0 0 0 5 8 \sin ^ { 2 } 2 \varphi )
$$

若将式(2.105)写成

$$
g = { \frac { g _ { e } ( 1 + K \sin ^ { 2 } \varphi ) } { \sqrt { 1 - { \frac { a ^ { 2 } - c ^ { 2 } } { a ^ { 2 } } } \sin ^ { 2 } \varphi } } } ,
$$

则

$$
\begin{array} { r l } & { g _ { c } = 9 . 7 8 0 3 1 8 5 ~ \ast / \ddagger { \mathbb { F } \mathbb { J } \mathbb { S } ^ { 2 } } , } \\ & { K = 0 . 0 0 1 9 3 1 6 6 3 , } \\ & { \frac { a ^ { 2 } - c ^ { 2 } } { a ^ { 2 } } = 0 . 0 0 6 6 9 4 6 0 5 _ { o } } \end{array}
$$

# 四、重力异常和大地水准面的高度

前节推导了在一个参考椭球面上的重力加速度g。大地水准面与参考椭球面是有差别的,但如能计算大地水准面上各点与参考面的距离N，则大地水准面的形状也就确定。N叫做大地水准面的高度。斯托克斯首先证明N可以由重力的分布计算出来。

# （一）布容斯（H.Bruns）公式和球面几近

实际的重力位W与参考椭球面上的重力位U有一个微小的差别T,叫做干扰重力位，即

$$
\begin{array} { r } { W ( x , y , z ) = U ( x , y , z ) + T ( x , y , z ) _ { 0 } } \end{array}
$$

现将大地水准面，

$$
\begin{array} { r } { W = U ( x , y , z ) + T ( x , y , z ) = W _ { 0 } } \end{array}
$$

与参考面， $U ( x , y , z ) = W _ { 0 }$ 做比较。将大地水准面上的任一点 $\pmb { P }$ 投影到参考面上的 $\varrho$ 点并令 $P Q = N , N$ 叫做大地水准面的高度。令$\mathbf { \Delta } \mathbf { g } = - \mathbf { \nabla } \nabla W$ ， $\pmb { \gamma } = - \pmb { \nabla } U$ 。两个向量的方向不同,叫做垂线偏差。现只讨论它们的数值之差。定义

![](images/7c26b0c933a182734d01487286d3c8317b02377d8784a7bdf445d604f55ecb12.jpg)  
图2.12

$$
\Delta g = g _ { P } - \gamma _ { Q }
$$

叫做重力异常。

$$
\delta g = g _ { P } - \gamma _ { P }
$$

叫做重力干扰。

$$
U _ { P } = U _ { \vartheta } + \left( \frac { \partial U } { \partial n } \right) _ { \vartheta } N = U _ { \vartheta } - \gamma N ,
$$

$$
\ b { W _ { P } } = \ b { U _ { P } } + \ b { T _ { P } } = \ b { U _ { Q } } - \ b { r N } + \ b { T _ { P 0 } }
$$

但

$$
\begin{array} { r } { W _ { P } = W _ { 0 } = U _ { Q } , } \end{array}
$$

故

$$
\pmb { T } = \pmb { \gamma } \pmb { N } _ { \circ }
$$

此式称为布容斯公式， $\pmb { \gamma }$ 是参考面上的重力。

$$
\begin{array} { r } { \delta g = - \left( \frac { \partial W } { \partial n } - \frac { \partial U } { \partial n ^ { \prime } } \right) \approx - \frac { \partial } { \partial n } \left( W - U \right) = - \frac { \partial T } { \partial n } } \end{array}
$$

但又有

$$
\delta g = g _ { P } - \ d _ { Y P } = g _ { P } - \ d _ { Y Q } - \frac { \partial \gamma } { \partial n } \ d _ { N } = \Delta g - \frac { \partial \gamma } { \partial n } \ d _ { N } ,
$$

故

$$
\begin{array} { c } { { g = - \frac { \partial T } { \partial n } + \frac { \partial \gamma } { \partial n } \ N , } } \\ { { \mathrm { ~ } } } \\ { { \mathrm { ~ } = - \frac { \partial T } { \partial n } + \frac { 1 } { \gamma } \frac { \partial \gamma } { \partial n } \ T _ { \circ } } } \end{array}
$$

在式(2.106)中,W和U都不是谐函数,因为它们都包含离心力位，但T是质量的重新分布引起的,所以V²T一0。若△g在大地水准面上为已知，则式(2.110)是T与 $\frac { \partial T } { \partial \eta }$ 面上的线性组合。所以求 $\pmb { T }$ 就是求解第三边界值问题。

参考面的扁率是e≈3×10-。若将它看成球面，则N，T，△g等量的相对误差不过3×10"。N的值不超过百米，所以它的误差不超过一米。如果这个误差是在允许的范围之内，则

$$
\begin{array} { r } { \gamma \approx \frac { G M } { r ^ { 2 } } , \ \frac { \partial \gamma } { \partial n } \approx \frac { \partial \gamma } { \partial r } \approx - \frac { 2 G M } { r ^ { 3 } } , \ \frac { 1 } { r } \frac { \partial \gamma } { \partial n } \approx - \frac { 2 } { r } } \end{array}
$$

在地面上,球面半径R可用椭球面的平均半径来替代,即R一ab,Y值可用椭球面上的平均值 $\gamma _ { m }$ 来替代，于是得

$$
\triangle \varrho = - \ : \frac { \partial T } { \partial r } - \frac { 2 \gamma _ { m } } { R } N = - \ : \frac { \partial T } { \partial r } - \frac { 2 } { R } T ,
$$

$$
\delta g = \Delta g + \frac { 2 \gamma _ { m } } { R } N = \Delta g + \frac { 2 } { R } T _ { \circ }
$$

上二式是式(2.110)和式(2.111)的球面几近。

# （二）地球以外一点的重力异常

若一谐函数在地面上的值为已知,则按球面几近,它在地球以外一点 $\pmb { P }$ 的值可用泊松

积分来计算。若这个函数不含零次项和一次项，则泊松积分可以写成另一形式，用时比较方便。根据公式(2.60),任一连续函数 $f ( \theta , \lambda )$ 可以写成

$$
f ( \theta , \lambda ) = \int f ( \theta ^ { \prime } , \lambda ^ { \prime } ) \sum _ { n = 0 } ^ { \infty } \frac { 2 n + 1 } { 4 \pi } P _ { n } \big ( \cos \phi \big ) d \omega ^ { \prime }
$$

$d \omega ^ { \prime } = \sin \theta ^ { \prime } d \theta ^ { \prime } d \lambda ^ { \prime } , \phi$ 是定点 $( \theta , \lambda )$ 与变点 $( \theta ^ { \prime } , \iota ^ { \prime } )$ 的夹角。若将 $f ( \theta , \lambda )$ 展成面谐函数的级数，

$$
\not \in ( \theta , \ \lambda ) = \sum _ { n = 0 } ^ { \infty } Y _ { n } ( \theta , \lambda ) ,
$$

则立见

$$
Y _ { n } ( \theta , \lambda ) = { \frac { 2 n + 1 } { 4 \pi } } \int f ( \theta , \lambda ^ { \prime } ) P _ { n } { \bigl ( } \cos \phi { \bigr ) } d \omega
$$

![](images/4608e9f02933a839317d1073319d578ffb6796a43305381c44010e4ed43eb2d5.jpg)  
图2.13

而

$$
\cos \phi = \cos \theta \cos \theta ^ { \prime } + \sin \theta \sin \theta ^ { \prime } \cos ( \lambda ^ { \prime } - \lambda ) { \circ }
$$

若一谐函数 $\pmb { H }$ 可以展成如下形式：

$$
H _ { \nu } = \frac { R } { r } H _ { \circ } + \Big ( \frac { R } { r } \Big ) ^ { \circ } H _ { \ I } + \sum _ { n = 2 } ^ { \infty } \Big ( \frac { R } { r } \Big ) ^ { n + 1 } H _ { n } ,
$$

$H _ { n }$ 为 $\pmb { n }$ 次的面谐函数。移项，得

$$
H _ { p } ^ { \prime } = H _ { p } - { \frac { R } { r } } H _ { 0 } - \left( { \frac { R } { r } } \right) ^ { 2 } H _ { 1 } = \sum _ { n = 2 } ^ { \infty } \left( { \frac { R } { r } } \right) ^ { n + 1 } H _ { n 0 }
$$

$H ^ { \prime }$ 不含零次或一次项。由式(2.115),

$$
\begin{array} { l } { { H _ { \mathrm { 0 } } = \frac { 1 } { 4 \pi } \bigg \{ H d \omega , } }  \\ { { { } } } \\ { { H _ { \mathrm { 1 } } = \frac { 3 } { 4 \pi } \bigg \{ H \cos \phi d \omega , } }  \end{array}
$$

$\pmb { \omega }$ 为立体角(见图2.13）, $\pmb { H }$ 为球面上之值。由泊松积分，

$$
H _ { \mathscr { s } } = \frac { R } { 4 \pi } \int \frac { r ^ { 2 } - R ^ { 2 } } { \rho ^ { 3 } } H d \omega ,
$$

$$
\rho = ( R ^ { 2 } + r ^ { 2 } - 2 r R \cos \phi ) ^ { 1 / 2 } ,
$$

故

$$
H _ { p } ^ { \prime } = \frac { R } { 4 \pi } \bigg \{ \bigg ( \frac { r ^ { 2 } - R ^ { 2 } } { \rho ^ { 3 } } - \frac { 1 } { r } - \frac { 3 R } { r ^ { 2 } } \cos \phi \bigg ) H d \omega _ { 0 }
$$

由式(2.113),

$$
\Delta g = - \ { \frac { \partial T } { \partial r } } - { \frac { 2 } { r } } \ T _ { \circ }
$$

$\pmb { \tau }$ 为一谐函数,且力位发生干扰后,质量无增减。故 $\operatorname* { l i m } _ { r \to \infty } r T = 0 ,$ 。这就意味着，当 $_ { \pmb { T } }$ 展成为球谐函数时,零次项不存在,即 $\pmb { n } \neq 0$ 。故

$$
T ( r , \theta , \lambda ) = \sum _ { n = 1 } ^ { \infty } \bigg ( \frac { R } { r } \bigg ) ^ { n + 1 } T _ { n } ( \theta , \lambda ) _ { \circ }
$$

代人上式，

$$
\Delta g = \frac { 1 } { r } \sum _ { n = 1 } ^ { \infty } \left( n - 1 \right) \left( \frac { R } { r } \right) ^ { n + 1 } T _ { n } ( \theta , \ \lambda ) _ { \circ }
$$

由此可见， $\pmb { \triangle } g$ 中并不含 $T _ { \perp }$ 项。

$$
r \Delta g = \sum _ { n = 2 } ^ { \infty } ( n - 1 ) \left( \frac { R } { r } \right) ^ { n + 1 } T _ { n } ( \theta , \lambda ) ,
$$

是一谐函数,但不含零次及一次项。将其代人式(2.116),得

$$
\Delta g _ { \dot { p } } = \frac { R ^ { 2 } } { 4 \pi r } \int _ { \omega } \Bigl ( \frac { r ^ { 2 } - R ^ { 2 } } { \rho ^ { 3 } } - \frac { 1 } { r } - \frac { 3 R } { r ^ { 2 } } \cos \phi \Bigr ) \Delta g d \omega _ { 0 }
$$

积分号下的 $\pmb { \triangle } g$ 是地面上的观测值。此式将地面值拓展到地外空间。

# （三）斯托克斯公式

若能由 $\pmb { \triangle } g$ 的地面观测值求得干扰力位 $_ { T }$ ，便可以计算大地水准面的高度 $\pmb { N } _ { 0 }$ 式(2113)给出了一个边界条件,但由式(2.117)， $\pmb { \triangle } g$ 可以向地外空间延拓，所以问题也可以看做是解微分方程(2.117)。将其两端乘以一 $r ^ { 2 }$ ，得

$$
- \ r ^ { 2 } \Delta g = r ^ { 2 } { \frac { \partial T } { \partial r } } + 2 r T = { \frac { \partial } { \partial r } } \left( r ^ { 2 } T \right) ,
$$

故

$$
r ^ { \ i } T \Bigm | _ { \infty } ^ { \prime } = - \int _ { \infty } ^ { \prime } r ^ { \ i } \Delta g d r _ { 0 }
$$

但式(2.117)的左端不含零次及一次的谐函数，故由 $\pmb { \triangle g }$ 计算的 $\pmb { T }$ 也不含 $\pmb { T _ { 0 } }$ 及 $\pmb { T } _ { \pmb { \imath } } ,$

$$
T = \sum _ { n = 2 } ^ { \infty } \left( { \frac { R } { r } } \right) ^ { n + 1 } T _ { n } ,
$$

$$
\operatorname * { l i m } _ { r  \infty } ( r ^ { 2 } T ) = 0 , r ^ { 2 } T \bigg | _ { \infty } ^ { r } = r ^ { 2 } T ,
$$

故

$$
r ^ { 2 } T = - \int _ { \circ } ^ { r } r ^ { 2 } \Delta g d r = \frac { R ^ { 2 } } { 4 \pi } \int _ { \circ } \left[ \int _ { \circ } ^ { r } \left( - \ \frac { r ^ { 3 } - r R ^ { 2 } } { \rho ^ { 3 } } + 1 + \frac { 3 R } { r } \cos \phi \right) d r \right] \Delta g d \omega _ { 0 }
$$

可以证明：

$$
\begin{array} { l } { { \displaystyle \left. \left( - \frac { r ^ { 3 } - r R ^ { 2 } } { \rho ^ { 3 } } + 1 + \frac { 3 R } { r } \cos \phi \right) d r \right. } } \\ { { \displaystyle = \frac { 2 r ^ { 2 } } { \rho } - 3 \rho - 3 R \cos \phi \ln ( r - R \cos \phi + \rho ) + r + 3 R \cos \phi \ln r } , } \end{array}
$$

$$
\begin{array} { l } { { { \displaystyle \int _ { \circ } ^ { \prime } \left( - { r ^ { 3 } } - { \frac { r R ^ { 2 } } { { \rho } ^ { 3 } } } + 1 + { \frac { 3 R } { r } } \cos \phi \right) d r } \qquad } } \\ { { = { \displaystyle 2 r ^ { \prime } } + r - 3 \rho - R \cos \phi \left( 5 + 3 \ln { \frac { r - R \cos \phi + \rho } { 2 r } } \right) } { } _ { 0 } } \end{array}
$$

故

$$
\begin{array} { c } { { T ( r , \theta , \lambda ) = \displaystyle { \frac { R } { 4 \pi } \int _ { \alpha } S ( r , \psi ) \Delta g d \omega } , } } \\ { { S ( r , \psi ) = \displaystyle { \frac { 2 R } { \rho } + \frac { R } { r } - 3 \frac { R \rho } { r ^ { 2 } } - \frac { R ^ { 2 } } { r ^ { 2 } } \cos \phi \left( 5 + 3 \ln \frac { r - R \cos \phi + \rho } { 2 r } \right) } \mathrm { d } r } } \end{array}
$$

在大地水准面上(球面几近)， $r = R$ ， $\rho = 2 R \sin { \frac { \phi } { 2 } }$ ，

$$
\begin{array} { r } { T ( R , \theta , \lambda ) = \frac { R } { 4 \pi } \int _ { \omega } \Delta g S ( \phi ) d \omega , } \end{array}
$$

$$
S ( \phi ) = \mathit { c s c } \phi / 2 - 6 \sin \phi / 2 + 1 - 5 \cos \phi - 3 \cos \phi \ln \left( \sin \phi / 2 + \sin ^ { 2 } \phi / 2 \right) _ { \mathrm { { o } } }
$$

$S ( \phi )$ 称为斯托克斯函数。根据布容斯公式，

$$
 { N } = \frac { R } { 4 \pi g _ { m } } \int _ { \omega }  { \Delta g }  { S } ( \phi ) d \omega _ { 0 }
$$

$g _ { m }$ 是地面上 $\pmb { g }$ 的平均值， $_ N$ 是大地水准面的高度。

斯托克斯公式假定大地水准面之外并无质量存在,其实不然,因为一部分水准面穿到地下。这部分质量的影响必须加以校正。这就引起理论上的一些细致问题，此处从略。在应用这个公式时，必须有充分的观测数据。在卫星时代之前，全球重力观测资料是很不均匀的,所以斯氏的方法只有理论上的意义。另一方面,这个公式只是球面几近。以后的发展已将这个理论推广到其他形状的参考面。这些都是大地测量学的专门问题，已超出本书的范围，本章不再讨论。

# 五、重力值的校正

重力异常的定义是大地水准面与参考面上的重力值之差，但实际观测是在地面上,而不是在水准面上,因此观测值必须校正。重力校正在以下几类问题中都是需要的： $\textcircled{1}$ 确定大地水准面； $\textcircled{2}$ 将不同地点的重力观测值进行对比； $\textcircled{3}$ 研究地壳的结构。

在应用斯托克斯公式来求大地水准面的高度时， $\pmb { \triangle } g$ 是水准面上的边界值，而且假定面外无质量存在。但其实面外是有质量的。所以校正时，必须将观测点由地面移到水准面上,并且将水准面以上质量的影响消去。

# （一）自由空气及布格校正

设地面一点 $\pmb { P }$ 的海拔高度为 $\pmb { h }$ ，它在海面上的投影为 $P _ { \vartheta }$ （图2.14）。 $\pmb { g }$ 值随高度的递减率 $\frac { \partial r } { \partial h }$ 可以由重力公式计算。若用 1930 年的公式，递减率为每升高一米， $\pmb { g }$ 值减少0.3086毫伽（1毫伽 $\ l = 1 0 ^ { - 3 }$ 厘米/秒2)；若用1967年的公式，递减率为0.3083毫伽/米。

![](images/c5e9885e8d670e95cd5b42fa9cd9ced4159cfa20214603af0d603c2e0c7d9b59.jpg)  
图2.14

若将 $\pmb { P }$ 点降到 $\pmb { P } _ { 0 }$ ，实测的 $\pmb { g }$ 值应增加03086h或0.3083h毫伽，h以米计。这个校正并未考虑 $\pmb { P }$ 与 $P _ { 0 }$ 之间那部分物质的引力，因此叫做自由空气校正，可以 $\pmb { F }$ 表示。

海面以上的物质可以分成两部分来讨论。一部分是通过 $\pmb { P }$ 点厚度为 $\pmb { h }$ 的一块无限平板；另一部分是选加在平板之上、在 $\pmb { P }$ 点四周的地形起伏。前一部分对 $\pmb { P }$ 点的引力极易证明为

$$
B = 2 \pi G \rho h ,
$$

$\pmb { \rho }$ 是地面附近岩石的密度。若取 $\bullet = 2 . 6 7$ 克/厘米，则 $B = 0 . 1 1 1 9 h$ 毫伽， $\pmb { \mathscr { h } }$ 以米计。这部分引力应从观测值中减去，

$$
\begin{array} { l } { { g _ { b } ^ { \prime } = g + F - B = g + 0 . 1 9 6 4 h , } } \\ { { \Delta g _ { b } ^ { \prime } = g _ { b } ^ { \prime } - \gamma } } \end{array}
$$

叫做布格重力异常， $\boldsymbol { \mathscr { r } }$ 是参考面上的重力值。

![](images/dbd7be01f628de6579ebac5a6bd542ce0d7ad2ec2e4721d416d7d7c071461b11.jpg)  
图2.15

进一步的校正就需要考虑地形的影响。图2.14表示 $P$ 点附近的地形起伏， $\pmb { A }$ 是凸起部分，$\pmb { B }$ 是凹下部分；须注意的是，无论是削去 $\pmb { A }$ 或是填平 $\pmb { { \cal B } }$ ,其结果都是使 $P$ 点的重力值加大，所以地形校正只与高差的绝对值有关。令地形校正为 $\pmb { T }$ ，则更完全的布格重力应包括这一项，即gb=g+F-B+T=g+F-(B-T)。

计算 $_ { T }$ 时，一般是将 $\boldsymbol { P }$ 点附近的地形划成扇形小块(如左图),求各小块所产生的重力值，然后选加。所用公式如下：

$$
\begin{array} { c } { { \triangle T = \alpha G \rho [ \sqrt { \overline { { { a _ { 2 } ^ { 2 } + ( h - b ) ^ { 2 } } } } } } } \\ { { - \sqrt { \overline { { { a _ { 1 } ^ { 2 } + ( h - b ) ^ { 2 } } } } - \sqrt { \overline { { { a _ { 2 } ^ { 2 } + h ^ { 2 } } } } } } } } \\ { { + \sqrt { \overline { { { a _ { 1 } ^ { 2 } + h ^ { 2 } } } } } ] , } } \end{array}
$$

式中 $\alpha = { \frac { 2 \pi } { \pi } }$ 是扇形在 $\pmb { P }$ 点所张的角, $\pmb { n }$ 是一周所割的块数, $a _ { 1 } , ~ a _ { 2 }$ 是扇形的内外半径，b是扇形的厚度(由海面算起),h是P点的海拔高度。总的地形校正为T=Σ△T。校正应伸展到多远,视观测的精确度而定。若远处地形的影响已降到所要求的精确度之下,就可以不计了。地形校正是有表可查的,只须测定式(2.122)中的参数就行了。完全的布格异常 $\Delta g _ { b }$ 是

$$
\begin{array} { c } { \triangle g _ { b } = g _ { b } - \gamma = g + F - ( B - T ) - \gamma } \\ { = g + 0 . 1 9 6 4 \hbar + T - \gamma _ { \circ } } \end{array}
$$

# （二）地壳均衡及均衡校正

如果地形起伏仅仅是多余（或短缺)的物质附加在一个大致均匀的地球之上，则经过布格校正之后，重力异常应当不大，并且无系统偏离，但事实并非如此。山区的重力异常经过布格校正之后,往往是负的，并且每升高一千米，异常约增加上百毫伽。这表明在高山之下,地下物质发生某种短缺,因而对地形的重力影响产生一种补偿作用。如果不考虑这个因素，校正便过头了，因而造成负异常。相似的现象也在垂线偏差的观测中看到。在高山的旁边，重力场的方向应当几近地等于地球重力与高山引力的合力的方向，这也就是垂线的方向。在1854年,英国人普拉特（J.H.Pratt）在喜马拉雅山附近一点,根据地形的计算，估计垂线应有 $2 8 ^ { \prime \prime }$ 的偏差，但实测结果只有5"。这也表明地下物质的变化起了某种补偿作用，部分地抵销了高山的影响。

为了解释这个现象，普拉特在1855年提出一个假设。他认为地下从某一深度算起（叫做补偿深度),以下物质的密度是均匀的，但以上的物质，则相同截面的柱体保持相同的总质量，因此地形越高，密度越小。计算一座高山的重力影响时，可以设想这座山是从补偿深度起，在垂直方向均匀膨胀而成的。

在同一年,另外一个英国人艾里（G．B.Airy）提出另一种假设。他认为地球上层物质的密度比下层小，山脉是较轻的岩石浮在较重的介质之上，仿佛冰浮在水上一样,但是它的底部也伸入水下;山越高,它的底部伸人介质也越深,山是有根的。按同样的道理,在海洋下面，由于海水的密度比岩石的小，下面的介质反而向上凸出,形成一个反山根。

以上两种模式都引出这样一个概念：从地下某一深度起，相同截面（面积要足够大）所承载的质量趋于相等。这个概念叫做地壳均衡。根据这个概念，地面上大面积的地形起伏，必然在地下有所补偿。普拉特的模式是将地形所增减的质量均匀地取偿于海面与补偿深度之间。因为地形高低不同，它在横的方向上密度也不同。艾里的模式则将地形所增减的质量取偿于山根或反山根。喜马拉雅山所产生的垂线偏差比按地形计算的小得多就是补偿的结果。无论根据哪种模式，只要测量了地形高度，并适当地估计下层岩石的密度和地壳厚度，就可计算由于补偿作用所减少的地面重力值l。这叫做均衡校正。将这个校正加在式(2.123)上，就叫做均衡异常。

![](images/7e67bb45dbc9c07d45f4f2b8f2227cb858176a147e1df2384a190c24c7b785f8.jpg)  
图2.16

图2.16是普拉特模式示意图。各柱状体因高程不同，其密度也有差异，但在补偿深度以上，各柱体的总质量是相等的。设补偿深度为 $D$ ，任一柱体的海拔高度为h，则有

$$
( D + h ) \rho = D \rho _ { \circ } ,
$$

$\pmb { \rho } _ { 0 }$ 及 $\pmb { \rho }$ 为海拔为零和为 $\pmb { \mathscr { h } }$ 时的密度。由此得到密度差 $\Delta \rho$ 为

$$
\Delta \rho = \rho _ { 0 } - \rho = \frac { h } { h + D } \rho _ { 0 0 }
$$

在海洋中,设海水的深度为 $\pmb { h } ^ { \prime }$ ，海水的密度为 $\scriptstyle \pmb { \rho } _ { \pmb { \omega } }$ ，则有

$$
( D - h ^ { \prime } ) \rho + h ^ { \prime } \rho _ { \omega } = D \rho _ { 0 } ,
$$

$$
\Delta \rho = \rho _ { 0 } - \rho = \frac { h ^ { \prime } } { D - h ^ { \prime } } \left( \rho _ { 0 } - \rho _ { \omega } \right) _ { 0 }
$$

补偿深度 $D$ 一般假定约为一百公里。 $h , \ h _ { 1 } , \ \rho _ { \omega } , \ \rho _ { 0 }$ 都是可以测定的。这样就可以计算$\Delta \rho$ 。知道 $\Delta \rho$ ，便可计算由于地壳均衡作用,各柱体对于 $P$ 点的重力曾经减少了多少。这是作布格校正时未曾考虑的,叫做均衡校正。计算公式与式(2.122)相似，不过其中的 $\pmb { \rho }$ 应以 $\Delta \rho$ 替代。

![](images/2d6f23bc28371cab40d77aa8e77292480ce22bcc84e7037d1d2db996b3b1e829.jpg)  
图2.17

图2.17是艾里模式的示意图。假定密度为2.67克/厘米的岩石浮在密度为3.27克/厘米的介质之上，地壳的正常厚度为 $_ T$ 。按照阿基米德原理，若地形的高度为 $\pmb { h }$ ，其下部深入介质中的深度为 $\pmb { \mathscr { t } }$ （即山根）,则有

$$
t \Delta \rho = h \rho _ { 0 } ,
$$

故

$$
\iota = h \frac { \rho _ { 0 } } { \Delta \rho } = \frac { 2 . 6 7 } { 0 . 6 } h = 4 . 4 5 h _ { 0 }
$$

在海洋下面，若海水的深度为 $h ^ { \prime }$ ，则反山根

的厚度 $\pmb { \mathscr { t } } ^ { \prime }$ 将符合

$$
\iota ^ { \prime } \Delta \rho = h ^ { \prime } ( \rho _ { 0 } - \rho _ { \omega } ) ,
$$

故

$$
\begin{array} { r } { t ^ { \prime } = \frac { \rho _ { 0 } - \rho _ { \omega } } { \Delta \rho } h ^ { \prime } = 2 . 7 3 h ^ { \prime } \circ } \end{array}
$$

设地壳的正常厚度为 $_ { T }$ ，则在高山之下,柱体的总厚度为

$$
T + h + t _ { \circ }
$$

在海洋之下，厚度为 $T - h ^ { \prime } - t _ { \mathrm { ~ o ~ } } ^ { \prime } \rho _ { 0 } , \rho _ { \omega }$ 为已知， $h , \ h ^ { \prime }$ 可以测量， $\rho _ { 1 } , T$ 可以由其他的地球物理观测来推导,于是各柱体的总厚度就可以得到，由此便可以计算均衡校正。

从物理意义上来看，普拉特模式不如艾里模式，因为均匀膨胀的设想并无观测的依据,而地壳以下的物质在载荷的长期作用下是可以发生流动的。不过实际计算补偿时，两种模式所得的结果相差无几。布格异常再经过均衡校正后便得到均匀异常。实测结果表明，大面积的均衡异常要比布格异常小得多，但在地球上的个别地区(如海沟或某些高山地区,包括喜马拉雅山地区),仍有相当大的均衡异常存在,说明这些地区的地壳是不均衡的。如何解释这些不均衡,学者的意见还是有分歧的。本世纪以来,地壳均衡的概念对地学的研究起了很大的影响。然而地球介质即使在极长时期的载荷作用下，和真正的流体还是有区别的。地壳本身是有弹性强度的，因而局部不均衡完全是可能的，即是说，补偿未必是完全的。这就仿佛船在水里,虽然全船的重量等于船所排开水的重量，但由于船身有一定的强度，船内的负载还可以随意安排。解释重力异常时，也应考虑这种情况。

另外一点也须指出。用斯托克斯的方法,由重力异常来确定大地水准面的高度时,曾假定水准面之外无质量存在,但实际上，大地水准面部分地穿过地下。在以上所讨论的各种校正中,不是将外部质量削去,便是将内部质量重新分布。这样做了之后,重力值变了，但所得到的大地水准面也不与原来的完全一样。这是一种规格化的大地水准面，叫做同水准面（co-geoid)。关于如何将大地水准面规格化，讨论很多。还有人主张根本不必用大地水准面这个概念。这是大地测量学的专门课题，本章不再讨论。

# 六、固体潮

地球的重力场基本上是恒定的，但也有微小的时间变化。这是由于地球在其他天体（特别是日、月)的引力场中做相对运动所引起的。月球虽小，但离地球很近，它的影响比太阳的约大一倍。

# (一)引潮力位

日、月的引力产生潮汐，这是众所熟知的。因为地球不是刚体，非但海洋有潮汐，地球的固体部分在日、月引力下也发生变形。这种变形随时间而变化,叫做固体潮。伴随着地面变形，重力场也有变化。总的变化是日、月引力影响之和。以下以月球为例来推导引起潮汐的力位。

![](images/9e5cd4195a8c79a302bbc33532730a9425683b1c8075625cd5b463c776c5700d.jpg)  
图2.18

设O,C各为地心及月心，其距离为R，地球半径为α，月球质量为m,P是地面上任一点。月球不但在P点产生引力,而且使全地球产生加速Gm/R,其方向是沿着OC。与此相应的力位是－Gm $\mathfrak { - } \frac { G m } { R ^ { 2 } } \ \pmb { a } \cos \phi \circ$ ，所以月球对于 $\pmb { P }$ 点的总力位等于

$$
{ \cal W } = \frac { G m } { ( R ^ { 2 } + a ^ { 2 } - 2 a R \cos \psi ) ^ { 1 / 2 } } - \frac { G m } { R ^ { 2 } } a \cos \psi ,
$$

将右端第一项展开至 $P _ { 2 } ( \cos \phi )$ ，得

$$
{ \cal { W } } _ { 2 } = { \frac { 3 } { 2 } } { \frac { G m a ^ { 2 } } { R ^ { 3 } } } \Big ( \cos ^ { 2 } \phi - { \frac { 1 } { 3 } } \Big ) = { \frac { G m a ^ { 2 } } { R ^ { 3 } } } P _ { 2 } ( \cos \phi ) ,
$$

$W _ { 2 }$ 叫做引潮力位，它是一个二次谐函数。

假设地球是个刚体,其质量为 $M$ ，则因引潮力所产生的重力变化 $\pmb { \triangle } g$ 为

$$
\triangle g _ { a } = - \frac { \partial W _ { \mathrm { 2 } } } { \partial a } = - \frac { G m a } { R ^ { 3 } } \big ( 3 \cos ^ { 2 } \phi - 1 \big ) ,
$$

$$
\begin{array} { r } { \Delta g _ { \phi } = - \frac { 1 } { a } \frac { \partial W _ { 2 } } { \partial \phi } = - \frac { 3 } { 2 } \frac { G m a } { R ^ { 3 } } \sin 2 \phi , } \end{array}
$$

$$
\triangle g _ { a } / g \approx \triangle g _ { a } \bigg / \frac { G m } { a ^ { 2 } } = - \frac { m } { M } \left( \frac { a } { R } \right) ^ { 3 } ( 3 \cos ^ { 2 } \phi - 1 ) ,
$$

$$
\triangle g _ { \psi } / g \approx \tan \alpha \approx \frac { 3 } { 2 } \frac { m } { M } \left( \frac { a } { R } \right) ^ { 3 } \sin 2 \phi _ { 0 }
$$

$\pmb { \alpha }$ 足在子午面上的垂线偏差。对于月球来说， $\frac { m } { M } \left( \frac { a } { R } \right) ^ { 3 } = 5 . 6 \times 1 0 ^ { - 8 } \mathrm { ~ ; ~ }$ ；对于太阳来说,这个数值要小045倍。

假设地球是个刚体，还可以估计月球引潮力对地球等位面的高度所产生的变化。地球自由振动的周期，最大不过约一小时,这比引潮力的周期小多了。所以固体潮可以看做是平衡潮,即是说,变形和引潮力几乎是同步的。在平衡潮中，W,=△ag，△a 是潮高的变化。

故

$$
\Delta a = W _ { 2 } / g = \frac { m } { M } \left( \frac { a } { R } \right) ^ { 3 } a \cdot \frac { 1 } { 2 } ( 3 c o s ^ { 2 } \phi - 1 ) _ { \circ }
$$

由此算出最大的高度差为0.535米。

# （二）勒夫数和志田数

地球并非刚体。在日、月引力的作用下，海洋和地球的固体部分都要发生变形，这就使引潮力位也发生变化。这些变化可以用三个无量纲的参数h,k,l来表示。h,k叫做勒夫数，l叫做志田数,纪念最初引用这些数的学者勒夫（A.E.H.Love）和志田顺。它们的定义如下：h是固体潮的潮高与海洋平衡潮的潮高之比；k是由于质量的重新分布而引起的力位变化与引潮力位W，之比；是地壳的水平位移与平衡海潮的水平位移之比。

观测到的海洋潮高是由三部分组成的。一部分是由于W,第二部分是由于kW。所以潮高应当等于（W+kW)/g。但海底本身由于W而上升h $h \frac { W _ { z } } { z } c$ ， 所以实际观测到的潮高为

$$
\displaystyle \Delta z = ( 1 + k - h ) W _ { 2 } / g _ { \circ }
$$

因为W是已知的，所以由观测潮高就可以确定1十k一h，这个数值常用γ表示．即$\gamma = 1 + k - k _ { \circ }$

在可变形的地面上，力位 $W$ 可以写成

$$
W = W _ { \circ } + W _ { \circ } + k W _ { \circ } - g u _ { r } ,
$$

$W _ { 0 }$ 是重力位， $W _ { 2 }$ 是引潮力位， $\pmb { k W }$ ，是由于质量的重新分布而引起的力位变化， $\pmb { u } _ { r }$ 是垂直位移。上式的后三项是可变的。由于引潮力的影响,在地面上所观测到的重力变化 $\triangle g$ 为

$$
- \ \triangle g = \frac { \partial W _ { \scriptscriptstyle 2 } } { \partial r } + k \frac { \partial W _ { \scriptscriptstyle 2 } } { \partial r } + u _ { r } \frac { \partial ^ { 2 } W _ { \scriptscriptstyle 0 } } { \partial r ^ { 2 } } \circ
$$

由式(2124),在地球内， $W _ { \it z } = \frac { G m r ^ { \it 2 } } { R ^ { \it 3 } } P _ { \it 2 } ;$ 在地球外， $\boldsymbol { W } _ { z } = \frac { G m } { R ^ { 3 } } \ : \frac { \boldsymbol { a } ^ { 5 } } { r ^ { 3 } } \boldsymbol { P } _ { z 0 }$ 故

$$
\frac { \partial W _ { 2 } } { \partial r } = 2 \ \frac { W _ { 2 } } { r } , k \ \frac { \partial W _ { 2 } } { \partial r } = - 3 k \ \stackrel { \{ V _ { 2 } }  { _ { r } } \circ
$$

根据球面几近，

$$
\frac { \partial ^ { 2 } W _ { 0 } } { \partial r ^ { 2 } } = \frac { 2 g } { r } , ~ u _ { r } \frac { \partial ^ { 2 } W _ { 0 } } { \partial r ^ { 2 } } = h \underset { g } { W _ { - } } \ : { \cdot } \ : { \ : } ^ { 2 g } = 2 h \underset { g } { W _ { - } } \circ
$$

所以

$$
\begin{array} { r l } & { - \bigtriangleup g = ( 2 - 3 k + 2 h ) \frac { W _ { 2 } } { g } } \\ & { \qquad = \left( 1 + h - \frac { 3 } { 2 } k \right) \frac { \partial W _ { 2 } } { \partial r } = \left( 1 + h - \frac { 3 } { 2 } k \right) \Delta g _ { r } , } \end{array}
$$

$\triangle g ,$ 表示一个刚体地球（ $\not { k } = \not { k } = 0$ ）所相应的 $\Delta g$ 。由上式,便可根据重力的变化求得

$$
\delta = 1 + h - { \frac { 3 } { 2 } } k _ { \circ }
$$

由 $\gamma$ 及 $\pmb { \delta }$ 便可计算 $h , k _ { \circ }$

引潮力位 $W _ { 2 }$ 及变形力位 $k W _ { z }$ 产生重力的两个水平分量 $\triangle g _ { \phi }$ 及 $\pmb { \triangle } \pmb { g _ { \lambda } }$ ，从而导致垂线偏差的两个分量：

但 $W _ { 3 }$ 也使地面产生水平位移 $\pmb { u } _ { \phi }$ 及 ${ \pmb u } _ { { \pmb \lambda } \circ }$ 定义

$$
u _ { \psi } = \frac { l } { g } \frac { \partial { \cal W } } { \partial \phi } , u _ { \lambda } = \frac { l } { g \cos \phi } \frac { \partial { \cal W } _ { 2 } } { \partial \lambda } ,
$$

1称为去田数。若用天文仪器在地面上观测,则相对于地轴所测定的垂线偏差将由

$$
\iota = ( 1 + k - l ) \ \frac { 1 } { a } \ \frac { \partial { W _ { 2 } } } { \partial { \phi } } ,
$$

$$
\jmath = ( 1 + k - l ) ~ \frac { 1 } { a g } ~ \frac { 1 } { \cos \phi } ~ \frac { \partial { W _ { 2 } } } { \partial { \lambda } } \circ
$$

表示。由此可确定L=(1+k一l)。结合式(2.126)及(2.127)，便求得h,k,l。一组典型的数据是

$$
h = 0 . 5 9 , ~ k = 0 . 2 7 , ~ l = 0 . 0 4 _ { o }
$$

但各家所得的结果颇有分歧。这一部分是由于干扰固体潮测定的因素太多，特别是海洋潮汐的影响不易消除,另一部分是地球内部情况复杂,由三个常数来概括各种形式的形变

也许是过于简化了。

# 参考书目

[1] 傅承义，1976。《地球十讲>科学出版社。  
[2] 方俊，1965，1975。《重力测量与地球形状学,上、下册,科学出版社。  
[3] Jeffreys,H,1964 The Earth,4th ed., Cambridge Univ.Press,London.  
[4] Heiskanen，W A，and H.Moritz,1967.Phystcal Geodesy,Freeman， San Francisco,1967.  
[5] Caputo,M., 1967. The Gravtty Fteld of the Earth，Acad. Press， New York.

# 第三章 地球的转动

在宇宙空间中,地球不仅绕着一条轴线自西向东自转,同时也沿着近于圆的轨道绕着太阳转动。地球自转平均角速度为 $7 . 2 9 2 1 \times 1 0 ^ { - 5 }$ 弧度/秒，在地球赤道上自转线速度为465米/秒。地球的自转轴和地面的两个交点叫做转动极或地极，和天球的两个交点叫做天极。在地球上看，天极就是天空中没有周日运动的两个点。平常说的北极星就是一颗靠近北天极的恒星。

作用在地球上的力种类很多。日、月对地球赤道凸出部分的吸引力随日月位置而变化。在它们的作用下，地球转动轴在空间的取向发生变化。地球作为一个整体也相对于其转动轴而摆动。由于日、月的吸引和地球惯量矩的季节性变化以及其他目前还不甚清楚的原因。地球的转动速率也不恒定。概而言之，地球的转动是不均匀的。从这个意义上讲，研究地球的转动就是研究地球转动的不均匀性。在天文学中,研究地球转动的不均匀性对于天体演化的研究以及天体方位的测定有着重要意义。在地球物理学中，研究地球转动有助于了解地球内部构造和运动，地球内部的密度、弹性和非完全弹性以及地壳、地核、海洋和大气的运动。

# 一、岁差和章动

在太阳和月球对地球赤道凸出部份的吸引作用下，地球的转动轴在空间的位置发生变化。如果地球是一个球体，而且赤道面与太阳轨道平面(黄道面)及月球轨道平面(白道面)都重合的话，就不会发生这种变化。实际上，赤道面和黄道面的倾角（黄赤交角）是$2 3 ^ { \circ } 2 7 ^ { \prime } 0 8 ^ { \prime \prime }$ ，而白道面和黄道面的倾角（黄白交角）是 $5 ^ { \circ } 8 ^ { \prime } 4 3 ^ { \prime \prime }$ 。如果地球不转动，日、月的引力对地球产生的力矩将使这些平面趋于一致。但地球是转动着的。由于转动的迴转效应,黄赤交角仍保持不变，而天极则以25,700年为周期绕着黄道面的极(黄极)转动，也就是赤道和黄道的交点（春分点和秋分点)沿着黄道每年向西移动 $5 0 ^ { \prime \prime } . 2 5 6 4 7 .$ 。当地球两次经过春分点时，它实际上并未绕完一周。这种运动叫作分点的岁差,简称岁差。迴转效应还使得天极相对于黄极作一种点头式的运动,叫做章动。现在北天极在北极星附近,可是在5,000年前，它在天龙座 $\pmb { \alpha }$ 星附近；5,000年后，它将在仙王座 $\pmb { \alpha }$ 星附近。

# (一)欧拉方程

我们来分析岁差和章动。为简单起见，把地球当作刚体，并且先只考虑太阳的影响。假定地球是一个旋转椭球体，它的三个主惯量分别是 $A , B , C$ ，其中 $A = B < C$ ，即相对于短轴的转动惯量 $^ c$ 最大。我们称这条轴为地球的形状轴或对称轴或惯性轴。取一个固定在地球上的运动坐标系 $\pmb { x } ,$ $( \iota = 1 , 2 , 3 )$ ，把它的原点放在地球的质心上，并使$\pmb { x } _ { 3 }$ 轴与形状轴重合(图3.1)。 $\pmb { x } _ { 1 }$ 轴可以放在过原点并与 $\pmb { x } _ { 3 }$ 轴垂直的平面里的任意方向上，$\pmb { x } _ { 2 }$ 轴也在这个平面上，与 $x _ { 1 } , x _ { 3 }$ 轴构成右旋坐标系。因为按照前面的假设，相对于另两个主轴的转动惯量是相等的。设地球以角速度 $\omega = \omega , e _ { \imath }$ 相对于“静止"坐标系 $X ,$ 转动，这里， $\pmb { e } _ { t }$ 表示转动坐标系 $\pmb { x } ,$ 的基矢量。将“静止”坐标系的 $X _ { 1 }$ 轴和 $X _ { 3 }$ 轴置于黄道面上，使

![](images/ac4080c314e7e278710bd5e9803ac255e46fa2916f358a0ea97cf48f9e191513.jpg)  
图3.1岁差和章动示意图

$X _ { 1 }$ 轴指向白羊宫 $( r ) \pmb { \alpha }$ 星。 $\pmb { X _ { 3 } }$ 轴和天球的交点 $\pmb { { \cal E } }$ 就是黄道的极。实际上， ${ \pmb \omega } _ { 3 }$ 比 $\pmb { \omega _ { 1 } } , \pmb { \omega _ { 2 } }$ 大得多，所以转动轴很靠近 $\pmb { x _ { 3 } }$ 轴，也就是说 $\pmb { x } _ { 3 }$ 轴和天球的交点 $P$ 是近似的天极， $\pmb { x } _ { 3 }$ 轴和 $X _ { 3 }$ 轴的夹角 $\pmb { \theta }$ 近似地等于黄赤交角，${ \pmb x } _ { 1 } { \pmb x } _ { 2 }$ 平面接近于赤道面。我们把 ${ \pmb x } _ { 1 } { \pmb x } _ { 2 }$ 平面和黄道面的交线NN'叫做节线，由于 ${ \pmb x } _ { 1 } { \pmb x } _ { 2 }$ 平面接近于赤道面，所以 $N ^ { \prime } , N$ 点近似于春、秋分点。 $N N ^ { \prime }$ 和 $X _ { 1 }$ 轴的夹角以$\pmb { \mathscr { Q } }$ 表示， $\pmb { x _ { 1 } }$ 轴和NN'的夹角以 $\phi$ 表示。太阳位于黄道上的 $s$ 点， $\overleftarrow { O S }$ 和 $X _ { \mathfrak { i } }$ 轴的夹角以 $\gimel$ 表示。

设 $\pmb { r } = \pmb { x } _ { t } \pmb { e } _ { t }$ ，则角动量 $\pmb { H }$ 为

$$
H = \int \limits _ { \tau } \int \int \rho \boldsymbol { r } \times ( \boldsymbol { \omega } \times \boldsymbol { r } ) d \tau ,
$$

式中， $\pmb { \rho }$ 是密度。式中的 $\pmb { r } \times ( \pmb { \omega } \times \pmb { r } )$ 可化为

$$
\boldsymbol { r } \times ( \boldsymbol { \omega } \times \boldsymbol { r } ) = ( r ^ { 2 } \mathbf { I } - r \boldsymbol { r } ) \cdot \boldsymbol { \omega } ,
$$

【是单位张量：

$$
\mathbf { I } = \delta _ { t } , e , e _ { I } ,
$$

其中， $\delta _ { \prime \prime }$ 是克朗内克（Kronecker）符号，当 $\bullet \ : = \ : \pmb { \mathscr { I } }$ 时， $\delta _ { i j } = 1 ;$ 当 $i \neq j$ 时， $\delta _ { t \prime } = 0$ 。这样一来， $\pmb { H }$ 可表示为：

$$
\pmb { H } = \pmb { \mathrm { C } } \cdot \pmb { \omega } ,
$$

其中，

$$
\mathbf { C } = \iint _ { \pmb { r } } \int \int \rho ( r ^ { 2 } \mathbf { l } - \pmb { r } \pmb { r } ) d \tau _ { 0 }
$$

C叫做惯量张量，其分量是：

$$
\{ \begin{array} { l } { C _ { 1 } = - \displaystyle { \int } \{ \int _ { 0 } ^ { \cdot } \rho ( x _ { i } ^ { \varepsilon } + x _ { i } ^ { \varepsilon } ) d \tau  } \\ { C _ { - } = \displaystyle { \int } \{ \int _ { 0 } ^ { \cdot } \rho ( x _ { i } ^ { \varepsilon } + x _ { i } ^ { \varepsilon } ) d \tau  } \\ { C _ { \mathrm { a s } } = \displaystyle { \int } \{ \int _ { 0 } ^ { \cdot } \rho ( x _ { i } ^ { \varepsilon } + x _ { i } ^ { \varepsilon } ) d \tau  } \\  C _ { \mathrm { a s } } = C _ { \mathrm { s } } = - \displaystyle { \int } \{ \begin{array} { l l } { 1 } \\ { \rho ( x _ { i } ^ { \varepsilon } , x _ { i } , d \tau ) } \\ { [ \int _ { 0 } ^ { \cdot } \rho ( x _ { i } ^ { \varepsilon } , d \tau ) ] } \\ { [ \int _ { 0 } ^ { \cdot } \rho ( x _ { i } ^ { \varepsilon } , d \tau ) ] } \\ { C _ { \mathrm { a s } } = C _ { \mathrm { a s } } = - \displaystyle { \int } \{ \begin{array} { l l } { 1 } \\ { \int _ { 0 } ^ { \cdot } \rho ( x _ { i } , d \tau ) } \\ { [ \int _ { 0 } ^ { \cdot } \rho ( x _ { i } ^ { \varepsilon } , d \tau ) ] } \end{array}  } \end{array}  \end{array}
$$

以 $\pmb { L }$ 表示外加力矩。则在坐标系 $X ,$ 中，

$$
\frac { d H } { d t } = L _ { \circ }
$$

在以 $\pmb { \omega }$ 转动的坐标系 $\pmb { x } ,$ 中,对于任一向量 $\pmb { v }$ 都有：

$$
\begin{array} { r } { \frac { d \pmb { v } } { d t } = \frac { \tilde { d } \pmb { v } } { d t } + \pmb { \omega } \times \pmb { v } , } \end{array}
$$

其中 $\tilde { d } v / \ d t$ 表示 $\pmb { v }$ 相对于转动坐标系的改变速度。对于角动量 $\pmb { H }$ 来说,类似地有：

$$
\frac { d \pmb { H } } { d t } \ = \frac { \tilde { d } \pmb { H } } { d t } + \pmb { \omega } \times \pmb { H } _ { \circ }
$$

将(3.7)式代人(3.5)式,即得表示刚体运动的欧拉方程：

$$
\frac { \tilde { d } \pmb { H } } { \tilde { d t } } + \pmb { \omega } \times \pmb { H } = \pmb { L } _ { 0 }
$$

式中， $\tilde { d } H / d t$ 是 $\pmb { H }$ 相对于转动坐标系的变化速度。

在转动坐标系 $\pmb { x } ,$ 中，

$$
\left\{ \begin{array} { l l } { C _ { 1 1 } = C _ { 2 2 } = A , } \\ { C _ { 3 3 } = C , } \\ { C _ { 1 2 } = C _ { 2 1 } = C _ { 1 } = C _ { 4 1 } = C _ { 2 2 } = C _ { 3 2 } = 0 , } \end{array} \right.
$$

从而欧拉方程可以表示为：

$$
\left\{ \begin{array} { l l } { { \mathit { 1 } } ^ { d } { \mathit { \Pi } } _ { { \overline { { d t } } } } ^ { d } + ( C - { \mathit { 1 } } ) { \mathit { \omega } } _ { 2 } { \omega } _ { 3 } = { \mathit { L } } _ { 1 } , } \\ { \ } \\ { { \mathit { 1 } } ^ { d } { \mathit { \Pi } } _ { { \overline { { d t } } } } ^ { d \omega _ { 2 } } + ( A - C ) { \omega } _ { 3 } { \omega } _ { 1 } = { \mathit { L } } _ { 2 } , } \\ { \ } \\ { { \mathit { C } } ^ { d \omega _ { 3 } } = { \mathit { L } } _ { 3 0 } } \end{array} \right.
$$

# (二）欧拉角

用前面引进的三个角 $\theta , \alpha , \phi$ 可以表示 $\pmb { x } ,$ 的转动，通常称它们为欧拉角。角速度 $\pmb { \omega }$ 在 $\pmb { x } ,$ 方向的分量，可以用欧拉角及其微商表示。角速度 $\dot { \pmb \theta } = \theta \mathbf e _ { \theta }$ 沿着节线 $o N$ 的方向,因而它在 $\pmb { x } _ { \pmb { \imath } }$ 轴上的分量为：

$$
\theta = \{ \theta \cos { \phi } , - \dot { \theta } \sin { \phi } , 0 \} ;
$$

角速度 $\dot { \pmb { \Omega } } = { \pmb { \mathcal { Q } } } \pmb { e } _ { \pmb { \mathcal { Q } } }$ 沿着 $\mathbf { { \boldsymbol { X } } _ { 3 } }$ 轴方向,所以它在 $\pmb { x } ,$ 轴上的分量是：

$$
\dot { \mathcal { Q } } = \{ \dot { \mathcal { Q } } \sin \theta \sin \phi , \dot { \mathcal { Q } } \sin \theta \cos \phi , \dot { \mathcal { Q } } \cos \theta \} ;
$$

角速度 $\dot { \phi } = \phi e _ { \phi }$ 沿着 $\pmb { x _ { 3 } }$ 轴方向，所以它在 $\pmb { x } ,$ 轴上的分量简单地就是：

$$
\dot { \phi } = \{ 0 , 0 , \dot { \phi } \} _ { \circ }
$$

如果以 $\theta , \textstyle \pmb { \mathcal { Q } } , \dot { \phi }$ 表示 $\pmb { \omega }$ ，即：

$$
\omega = \theta + \dot { \pmb { \Omega } } + \dot { \phi } ,
$$

则由(3.11)-(3.13)诸式可得：

$$
\begin{array} { r } { \left\{ \begin{array} { l l } { \omega = \dot { \mathcal { Q } } \sin \theta \sin \phi + \theta \cos \phi , } \\ { \omega = \mathcal { Q } \sin \theta \cos \phi - \theta \sin \phi , } \\ { \omega _ { \mathrm { s } } = \dot { \mathcal { Q } } \cos \theta + \phi _ { \mathrm { o } } } \end{array} \right. } \end{array}
$$

既然 $\pmb { x } _ { 1 }$ 轴可以放在赤道面的任意方向上,不失一般性,我们可以让它与ON重合，即取 $\phi = 0$ 。这样一来 $\pmb { \omega }$ 和 $d \omega / d t$ 的分量可以简单地表示成：

$$
\left\{ \begin{array} { l l } { \omega _ { 1 } = \dot { \theta } , } \\ { \omega _ { 2 } = \dot { \mathcal { Q } } \sin \theta , } \\ { \omega _ { 3 } = \dot { \mathcal { Q } } \cos \theta + \dot { \phi } , } \end{array} \right.
$$

$$
\left\{ \begin{array} { l } { \displaystyle \frac { d \omega _ { 1 } } { d t } = \dot { \mathcal { Q } } \dot { \phi } \sin \theta + \theta , } \\ { \displaystyle \frac { d \omega _ { 2 } } { d t } = \frac { d } { d t } \left( \dot { \mathcal { Q } } \sin \theta \right) - \theta \dot { \phi } , } \\ { \displaystyle \frac { d \omega _ { 3 } } { d t } = \frac { d } { d t } \left( \dot { \mathcal { Q } } \cos \theta \right) + \phi _ { \circ } } \end{array} \right.
$$

将以上两式代到(3.10)式中,我们便得到：

$$
\left\{ \begin{array} { l l } { { A ( \dot { \mathcal { Q } } \dot { \phi } \sin \theta + \theta ) + ( C - \mathcal { A } ) \dot { \mathcal { Q } } \sin \theta ( \dot { \mathcal { Q } } \cos \theta + \dot { \phi } ) = L _ { 1 } , } } \\ { { A \left[ \frac { d } { d t } \left( \dot { \mathcal { Q } } \sin \theta \right) - \dot { \theta } \dot { \phi } \right] + ( \mathcal { A } - C ) \dot { \theta } ( \dot { \mathcal { Q } } \cos \theta + \dot { \phi } ) - L _ { 2 } , } } \\ { { } } \\ { { C \frac { d } { d t } \left( \dot { \mathcal { Q } } \cos \theta + \dot { \phi } \right) = L _ { 3 0 } } } \end{array} \right.
$$

要解这个方程,需要知道因为太阳的吸引而作用在地球上的力矩 $\scriptstyle { \pmb { L } } _ { \pmb { \circ } }$

# （三）麦柯拉夫(MacCullagh)公式

如果以 $\pmb { \sigma }$ 表示地球在太阳的引力场中的位能，以 $\pmb { \mathscr { f } }$ 表示作用于地球上某一质量元的力，那么位能的变化 ${ \pmb \delta U }$ 应当等于反抗引力所作的功，即

$$
\delta U = - \ : \Sigma \boldsymbol { f } \cdot \delta \boldsymbol { r } _ { \circ }
$$

若地球绕某一轴线转动了一个无穷小角 $\delta \pmb { \theta }$ ，则

$$
\delta r = \delta \theta \times { r } ,
$$

从而

$$
\delta U = - \Sigma { \boldsymbol { \mathsf { f } } } \cdot ( \delta { \boldsymbol { \theta } } \times { \boldsymbol { \mathsf { r } } } ) = - { \boldsymbol { L } } \cdot \delta { \boldsymbol { \theta } } ,
$$

其中 $\pmb { L }$ 是作用在地球上的力矩：

$$
\pmb { L } = \Sigma \pmb { r } \times \pmb { f } _ { \circ }
$$

另一方面，如果地球绕某一轴线转动了 $\delta \pmb { \theta }$ ，则其位能的变化为：

$$
\delta U = \frac { \partial U } { \partial \pmb { \theta } } \cdot \delta \pmb { \theta } _ { o }
$$

由(3.21),(3.23)两式立刻可得

$$
\pmb { L } = - \frac { \partial U } { \partial \pmb { \theta } } \circ
$$

由麦柯拉夫（MacCullagh）公式[(2.66)式],可以求得位能

$$
\begin{array} { r l } & { U = - \ G \left[ \frac { M _ { s } M } { R _ { s } } + \frac { M \left( A _ { s } + B _ { r } + C _ { s } - 3 I _ { s } \right) } { 2 R _ { s } ^ { 3 } } + \frac { M _ { s } \left( A + B + C - 3 I \right) } { 2 R _ { s } ^ { 3 } } \right] } \\ & { \phantom { \frac { M _ { s } M } { R _ { s } } } } \\ & { \phantom { \frac { M _ { s } M } { R _ { s } } } + O \left( \frac { 1 } { R _ { s } ^ { 4 } } \right) , } \end{array}
$$

式中， $_ { G }$ 是引力常数， $M$ 是地球的质量， $A \circ B , C$ 是其主惯量, $\pmb { I }$ 是它对太阳、地球质心联线(图3.1中的 $\overline { { O S } }$ ）的转动惯量， $M _ { s } , A _ { s } , B _ { s } , C _ { s } , I _ { s }$ 是太阳的相应的量， $R _ { s }$ 是太阳质心至地球质心的距离。

假定太阳具有球对称性,并忽略地球绕太阳公转的轨道的偏心率，那么在上式中对 $\pmb { L }$ 有意义的项只是含有一31的项，所以

$$
\begin{array} { r } { \pmb { L } = - \frac { 3 G M _ { s } } { 2 R _ { s } ^ { 3 } } \frac { \partial I } { \partial \pmb \theta } , } \end{array}
$$

式中

$$
\begin{array} { r } { I = A l ^ { 2 } + B m ^ { 2 } + C { n ^ { 2 } } _ { \circ } } \end{array}
$$

$\{ l , m , n \}$ 是 $\overrightarrow { O S }$ 在转动坐标系 $\pmb { x } _ { t }$ 中的方向余弦。

在 $x _ { \ast }$ 中， $\pmb { e } _ { \pmb { \imath } }$ 可表示为：

$$
\left\{ \begin{array} { l } { e _ { 1 } = \{ \cos Q , \ \sin Q , \ 0 \} , } \\ { e _ { 2 } = \{ - \ \cos \theta \sin Q , \ \cos \theta \cos Q , \ \sin \theta \} , } \\ { e _ { 3 } = \{ \sin \theta \sin Q , \ - \ \sin \theta \cos Q , \ \cos \theta \} _ { 0 } } \end{array} \right.
$$

而 $\overline { { O S } }$ 可表示为：

$$
\overline { { O S } } = \{ \cos { \lambda } , \ \sin { \lambda } , \ 0 \} ,
$$

所以

$$
\left\{ \begin{array} { l } { { l = \overrightarrow { O S } \cdot e _ { 1 } = \cos { ( \lambda - \mathcal { Q } ) } , } } \\ { { m = \overrightarrow { O S } \cdot e _ { 2 } = \sin { ( \lambda - \mathcal { Q } ) } \cos { \theta } , } } \\ { { n = \overrightarrow { O S } \cdot e _ { 3 } = - \sin { ( \lambda - \mathcal { Q } ) } \sin { \theta } , } } \end{array} \right.
$$

从而

或

$$
I = d \cos ^ { 2 } { ( \lambda - \mathcal { Q } ) } + \left( B \cos ^ { 2 } { \theta } + C \sin ^ { 2 } { \theta } \right) \sin ^ { 2 } { ( \lambda - \mathcal { Q } ) } ,
$$

$$
l = \mathit { A l } ^ { 2 } + ( B \cos ^ { 2 } \theta + C \sin ^ { 2 } \theta ) ( 1 - \mathit { l } ^ { 2 } ) _ { 0 }
$$

在(3.26)式中， $\pmb { \theta } = \theta _ { \imath } \pmb { e } _ { \imath } , \theta _ { \imath }$ 就是欧拉角 $\pmb \theta$ ，所以，

$$
{ \cal L } _ { \mathrm { t } } = - \frac { 3 G M _ { \mathscr { s } } } { 2 R _ { \mathscr { s } } ^ { 3 } } \frac { \partial I } { \partial \theta } \circ
$$

由上式可求得 $L _ { \mathbf { \lambda } }$ 的表示式。然后通过对有关量的循环代换，又可得 $\pmb { L _ { 3 } }$ 和 $\pmb { L } _ { 3 0 }$ 结果是：

$$
\left\{ \begin{array} { l } { { L _ { 1 } = \displaystyle \frac { 3 G M _ { \varepsilon } } { R _ { \varepsilon } ^ { 3 } } ( C - B ) m n , } } \\ { { } } \\ { { L _ { 2 } = \displaystyle \frac { 3 G M _ { \varepsilon } } { R _ { \varepsilon } ^ { 3 } } ( A - C ) n l , } } \\ { { } } \\ { { L _ { 3 } = \displaystyle \frac { 3 G M _ { \varepsilon } } { R _ { \varepsilon } ^ { 3 } } ( B - A ) l m _ { 0 } } } \end{array} \right.
$$

# (四)岁差和章动

将上式代人(3.18)式的最后一式,并用到 $A = B$ ，立即可得：

$$
\omega _ { 3 } = \dot { \mathcal { Q } } \cos \theta + \dot { \phi } = \tilde { \omega } ,
$$

其中 $\pmb { \tilde { \omega } }$ 是一个常数。考虑到 $\dot { \phi } \gg \dot { \mathcal { Q } } , \dot { \theta } ,$ 故

$$
{ \dot { \phi } } \doteq { \tilde { \pmb { \omega } } } ,
$$

于是(3.18)式的前两式可化为：

$$
\left\{ \begin{array} { l l } { \displaystyle { \dot { \mathcal { Q } } = - \frac { 3 G M _ { \prime } } { \tilde { \omega } R _ { s } ^ { 3 } } \frac { C } { C } \overline { { - \mathrm { \ i } } } \sin ^ { 2 } ( \lambda - \mathcal { Q } ) \cos \theta , } } \\ { \displaystyle { \theta = - \frac { 3 G M _ { \prime } } { \tilde { \omega } R _ { s } ^ { 3 } } \frac { C - A } { C } \frac { 1 } { 2 } \sin \left[ 2 ( \lambda - \mathcal { Q } ) \right] \sin \theta _ { \circ } } } \end{array} \right.
$$

$$
k _ { s } = \frac { G M _ { s } } { \tilde { \omega } R _ { s } ^ { 3 } } \ \frac { c - \lrcorner \lrcorner } { c } ,
$$

则

$$
\left\{ \begin{array} { l } { { \displaystyle \dot { \mathcal { Q } } = - \frac { 3 } { 2 } k _ { s } \{ 1 - \cos { [ 2 ( \lambda - \mathcal { Q } ) ] } \} \cos { \theta } , } } \\ { { \displaystyle } } \\ { { \theta = - \frac { 3 } { 2 } k _ { s } \sin { [ 2 ( \lambda - \mathcal { Q } ) ] } \sin { \theta _ { \mathrm { o } } } } } \end{array} \right.
$$

实际上， $\theta , \alpha$ 变化很小，所以上式右边的 $\theta , \ Q$ 可以用其平均值 $\theta _ { s } , \ : Q _ { s }$ 代替。此外，上式中的 $\lambda = n , t , n ,$ 是太阳轨道角速度。于是得

$$
\left\{ \begin{array} { l l } { { \displaystyle Q = Q _ { 0 } - \frac { 3 } { 2 } k _ { s } \cos \theta _ { , } t + \frac { 3 k _ { s } } { 4 n _ { s } } \cos \theta _ { , } \sin \left[ 2 \left( n _ { s } t - Q _ { s } \right) \right] , } } \\ { { \displaystyle \theta = \theta _ { 0 } + \frac { 3 k _ { s } } { 4 n _ { s } } \sin \theta _ { , } \cos \left[ 2 \left( n _ { s } t - Q _ { s } \right) \right] , } } \end{array} \right.
$$

式中， $\pmb { \mathscr { Q } } _ { 0 }$ 和 $\theta _ { \mathfrak { o } }$ 是常数。这个结果表明， $\pmb { \mathscr { Q } }$ 以恒定的平均速率 $- \frac { 3 } { 2 } k _ { s } \cos \theta _ { s }$ 变化;或者说，节线NN'以恒定的速率绕黄道轴旋转。前面已经提到， $\pmb { N }$ 和 ${ \pmb { N } } ^ { \prime }$ 点分别是秋分点和春分点的近似位置,所以这种运动叫做二分点的岁差，简称岁差。在岁差上又迭加了一个振荡式的运动,其幅角为 $2 ( n _ { s } t - \mathcal { Q } _ { s } )$ ，振幅为 $\frac { 3 k _ { s } } { 4 n _ { s } } \cos \theta _ { s 0 }$ 类似地， $\pmb \theta$ 以比上述振荡式运动超前 $\pmb { \pi } / 2$ 的幅角振荡,但振幅为 3k sin0，这两种振荡式的运动合起来，称作章动。

从天球上看，天极以速率 $- \frac { 3 } { 2 } k , \cos \theta ,$ 绕着黄道轴顺时针(此处以及后面提到顺、逆时针时,都是参照图3.1而言)旋转，同时以图3.1中的 $\pmb { P }$ 点为中心绕着一个椭圆逆时针旋转。椭圆的长轴在天球的子午圈上,其长度为 3ksin0,；其短轴在天球的纬度圈上，长4ns为 $\frac { 3 k } { 4 n _ { s } } \sin \theta _ { s } \cos \theta _ { s 0 }$

# （五）月球的影响

以上只考虑了太阳的影响。实际上，月球对地球的岁差也有影响。它的影响与太阳的类似,就是使得以恒定的速率一 $- \frac { 3 } { 2 } k _ { L } \cos \theta _ { L }$ 变化。这里 $k _ { L }$ 和 $\theta _ { L }$ 是与 $k _ { s }$ 和 $\theta _ { \varepsilon }$ 相应的量,但是指月球而言的。

按照开普勒定律：

$$
n _ { \ell } ^ { 2 } R _ { \ell } ^ { 3 } = G M _ { \ell } ,
$$

可将 $k _ { s }$ 表示成

$$
{ / k } _ { { s } } = \tilde { \omega } \left( \frac { n _ { s } } { \tilde { \omega } } \right) ^ { 2 } H ,
$$

其中 $\pmb { H }$ 称为地球的动力学扁率或岁差常数：

$$
\mathit { \Pi } _ { M } = { \mathit { \Pi } _ { { \overline { { C } } } } } ^ { - \frac { d } { d } } \circ
$$

对于月球来说,与(3.41)式相应的关系式是：

$$
n _ { \iota } ^ { 2 } R _ { L } ^ { 3 } = G M _ { o }
$$

式中， $\pmb { n } _ { \pmb { L } }$ 是月球轨道角速度， $\scriptstyle { R _ { L } }$ 是月球质心至地球质心的距离， $\pmb { M }$ 是地球的质量。所以和(3.42)式相应的关系式是：

$$
k _ { L } = \tilde { \omega } \left( \frac { n _ { L } } { \tilde { \omega } } \right) ^ { 2 } \frac { M _ { L } } { M } H _ { o }
$$

现在我们知道，n,/@=1 $n _ { L } / \tilde { \omega } = \frac { 1 } { 2 8 } , H { = } 3 . 2 7 3 2 \times 1 0 ^ { - 3 }$ ， $M _ { L } / M = \frac { 1 } { 8 1 . 3 0 3 }$ ， 所以$h , \doteq 9 \times 1 0 ^ { - 6 }$ （恒星年）\~， $k _ { L } \doteq 1 . 9 \times 1 0 ^ { - 5 }$ （恒星年)-。如果暂且忽略不计黄白交角，即取 $\theta _ { L } \doteq \theta _ { s } = 2 3 ^ { \circ } 2 7 ^ { \prime }$ ，则太阳和月球引起的岁差就是 $\frac { 3 } { 2 } ( k _ { 1 } + k _ { 2 } ) \cos \theta _ { s }$ ，其数值是$3 . 8 5 \times 1 0 ^ { - 5 }$ （恒星年） $- 1$ 或 $5 0 ^ { \prime \prime }$ （恒星年）-。考虑其他行星的影响，并考虑月球轨道与黄道并不重合，可以求得总岁差是50".25647（恒星年）-,即周期为25,700年。

太阳引起的章动周期是 $2 \pi / 2 n _ { s }$ ，即半年。其振幅约为 $\mathfrak { 0 } ^ { \prime \prime } . 0 1$ 。月球引起的章动则要复杂些。在太阳的吸引作用下，白道面和黄道面的交线以角速度 $\pmb { \mathscr { p } }$ 西移， $\pmb { \mathscr { p } } { = } 2 \pi / 1 8 . 6$ 年。这种运动引起了周期为18.6年的章动，振幅大约为9".206，是章动的主要成份。月球绕地球转动引起的章动的周期是 ${ 2 \pi } / { 2 n _ { L } }$ ，也就是只有两星期，振幅只有 $\mathfrak { d } ^ { \prime \prime } . 0 0 1$ 左右。

# （六）地球的动力学扁率

由(3.42)和(3.45)式得,日、月吸引产生的岁差 $k$ 为：

$$
\dot { k } = \tilde { \omega } \left[ \left( \frac { n _ { s } } { \tilde { \omega } } \right) ^ { 2 } + \left( \frac { n _ { L } } { \tilde { \omega } } \right) ^ { 2 } \frac { M _ { L } } { M } \right] H _ { \circ }
$$

k,@,n/ω,nz/@和M/M都是已知量,因此便可计算出H。在推导上式时,作了许多简化的假定，特别是忽略了日、月轨道的偏心率和倾角。并且，也忽略了其他行星的影响。把这些因素都考虑在内，便可求得 H= 3.2732× 10- $H = 3 . 2 7 3 2 \times 1 0 ^ { - 3 } = { \frac { 1 } { 3 0 5 . 5 1 } } c$ ) 这是我们在上面刚用过的数值。

# 二、转动轴的变化

# (一)欧拉章动

前面只讨论了欧拉方程的特解。当然这个方程的全解应当包括相应的各次方程的通解，即自由运动。在(3.37)式中令 $\pmb { L } = 0$ ，我们便得到：

$$
\frac { \tilde { d } \boldsymbol { H } } { \tilde { d } t } + \boldsymbol { \omega } \times \boldsymbol { H } = \boldsymbol { 0 }
$$

写成分量形式,即：

$$
\{ \begin{array} { l l } { { d } \frac { d \omega _ { 1 } } { d t } + ( C - A ) \omega _ { 2 } \omega _ { 3 } = 0 , } \\ {  } \\ { { d } \frac { d \omega _ { 2 } } { d t } + ( A - C ) \omega _ { 3 } \omega _ { 1 } = 0 , } \\ { { c } \frac { d \omega _ { 3 } } { d t } = 0 _ { 0 } } \end{array} 
$$

由上式的最后一式可知 $\pmb { \omega } _ { 3 }$ 保持不变,我们以常数 $\pmb { \tilde { \omega } }$ 表示之：

$$
\omega _ { 3 } = \tilde { \omega } ,
$$

将它代人(3.48)式的头两式,我们就得到：

$$
\begin{array} { r } { \left\{ \begin{array} { l l } { \frac { d \omega _ { 1 } } { d t } + \sigma _ { 0 } \omega _ { 2 } = 0 , } \\ { \frac { d \omega _ { 1 } } { d t } - \sigma _ { 0 } \omega _ { 1 } = 0 , } \end{array} \right. } \end{array}
$$

其中，

$$
\sigma _ { 0 } = \ { \frac { c - { \mathcal { A } } } { { \mathcal { A } } } } \ { \tilde { \sigma } } _ { \circ } \quad
$$

将（3.50)的第二式乘以i，然后与第一式相加,则得：

$$
\frac { d } { d t } \left( \omega _ { 1 } + \imath \omega _ { 2 } \right) = \imath \sigma _ { 0 } ( \omega _ { 1 } + \imath \omega _ { 2 } ) ,
$$

因此

$$
\omega _ { 1 } + \imath \omega _ { 2 } = K e ^ { \imath ( \sigma _ { 0 } t + \alpha ) } ,
$$

式中， $K , \pmb { \alpha }$ 是实常数。可以将上式改写成：

$$
\begin{array} { r } { \{ \omega _ { 1 } = K \cos ( \sigma _ { 0 } t + \alpha ) , } \\ { \{ \omega _ { 2 } = K \sin ( \sigma _ { 0 } t + \alpha ) _ { 0 }  } \end{array}
$$

这一结果表明,角速度在赤道面上的投影的数值是不变的（√+ω=K)，并以角速度 $\pmb { \sigma _ { 0 } }$ 在赤道面上旋转。既然 $\pmb { \omega _ { 3 } }$ 也保持不变，所以我们可以得出下列结论，即：向量@的数值不发生变化,但以角速度σ绕x轴等速转动。2（恒星日），

$$
\textstyle { \frac { c - A } { A } } = { \frac { 1 } { 3 0 5 } } ,
$$

所以转动轴绕着形状轴以 $\frac { 2 \pi } { \tilde { \omega } } \frac { A } { C - A } = 3 0 5$ 恒星日,即大约10个月的周期旋转。这个结果是欧拉(Euler）在1765年得到的，所以刚体地球的这种运动叫做欧拉(自由)章动。相应的周期叫做欧拉(自由)周期。

由(3.2）式可得：

$$
H = \left\{ \mathit { A } \omega _ { 1 } , \mathit { A } \omega _ { 2 } , \mathit { C } \omega _ { 3 } \right\}
$$

这一结果说明，H位于x轴和@构成的平面内，并且在它们中间；在转动坐标系X，中，H的数值不发生变化,并且以角速度α绕x轴等速转动。在“静止”坐标系X,中，H是守恒的，所以实际上是形状轴和角速度向量绕着 $\pmb { H }$ 等速转动。

图3.2表示上述各种轴的几何关系。OZ是垂直于黄道面的轴线，0C是地球的形状轴，O1是转动轴，OH是角动量轴,实际上,地球的转动轴与角动量轴的夹角很小，只有千分之几秒,形状轴与转动轴的夹角要大300倍左右，图3.2仅是示意图。在作岁差运动时,地球坐标的锥面以 $- \frac { 3 } { 2 } k _ { s } \cos \theta _ { s }$ 的速率绕OZ顺时针转动(如果从上往下看的话)，即向西移动。与此同时，形状轴 $_ { o c }$ 和角速度向量01绕角动量向量OH逆时针转动。

# (二）钱德勒晃动

以上分析中一直把地球当作刚体。真实地球在受到力矩作用和转动时都要发生形变。可以预料转动的实际变化不会与上述理论结果完全一致。事实正是这样。自欧拉1765年的工作以后，人们一直在寻找周期为305恒星日的转动轴的变化，但没有成功。直到1891年钱德勒（S.C.Chandler）发现了周期为425一440恒星日、即大约14个月的变化后人们才认识到这个周期约14个月的运动就是真实地球的自由章动。地球自由章动的周期不是10个月而是14个月，是由于它并非刚体。当地球转动轴在地球中的位置改变时，离心力对地球各部分的作用也随着改变,从而引起地球变形,使形状轴略向转动轴靠近。这也就等效于使转动惯量变大，从而使周期加大。为了区别于刚体地球的欧拉自由章动并纪念它的发现者，现在称真实地球的自由章动为钱德勒晃动。

![](images/7608d6c94ffbc8573fef5f864ab1e59512a055efe9b5730be179d4f44570c832.jpg)  
图3.2形状轴、角动量向量和角速度向量的几何关系示意图

我们来分析变形的旋转椭球体的运动。仍取质心为坐标原点。取一个以 $\pmb { \omega }$ 转动的坐标系。若地球是刚性的，则这个转动坐标系在地球中是固定的，此时地球里某一质点相对于“静止”坐标系的运动速度应为 ${ \pmb { \omega } } \times { \pmb { r } } _ { \circ }$ 但是地球是变形体，所以若以 $\pmb { U }$ 表示质点相对于"静止"坐标系的运动速度，则该质点相对于转动坐标系的速度为 $\pmb { U } - \pmb { \omega } \times \pmb { r } _ { \circ }$ 今令

$$
E _ { \kappa } = \frac { 1 } { 2 } \int \int _ { \tau } \rho ( U - \omega \times \boldsymbol { r } ) ^ { 2 } d \tau ,
$$

我们可以选取某个 $\pmb { \ 6 0 }$ ，使得：

$$
\mathop { E _ { K } } | _ { \mathop { \bf { \substack { \left. \kern - delimiterspace \right.} } } \omega  \kern - delimiterspace } \omega  =
$$

由上式得：

$$
\int _ { \tau } \Bigl \{ \intop _ { \tau } \rho [ \boldsymbol { r } \times \boldsymbol { U } - ( \boldsymbol { r } ^ { 2 } \boldsymbol { I } - \boldsymbol { r } \boldsymbol { r } ) \cdot \vec { \omega } ] d \tau = 0
$$

也就是：

$$
c \cdot \omega = H
$$

其中 $\pmb { H }$ 是

$$
H = \int \limits _ { \tau } \int \int \rho \boldsymbol { r } \times \boldsymbol { U } d \tau ,
$$

满足上述条件的坐标系叫平均本体轴坐标系。对于这样选取的坐标系，运动方程和描述刚体运动的欧拉方程的形式是一样的：

$$
\frac { \tilde { d } \boldsymbol { H } } { \tilde { d t } } + \boldsymbol { \varpi } \times \boldsymbol { H } = \boldsymbol { L } ,
$$

只是式中的角速度是平均本体轴坐标系转动的角速度 $\clubsuit _ { 9 }$ 为简便计，以下分析中都省去$\pmb { \hat { \omega } }$ 上的一横。

仍让 $\pmb { x } ,$ 轴分别和变形前的惯量主轴重合。变形后，惯量主轴发生变化，在原坐标系中，惯量积不再等于零。设变形不大，以至惯量矩与原先的主惯量差别很小，故仍以 $\pmb { A }$ ，$B , c$ 表示;因变形不大，所以变形后的惯量积 $c _ { \scriptscriptstyle { 2 3 } } , c _ { \scriptscriptstyle { 3 1 } } , c _ { \scriptscriptstyle { 1 2 } }$ 都是一级小量。今以 $D , \ E , \ F$ 分别表示 $- \ C _ { 2 3 } , - \ C _ { 3 1 } , - \ C _ { 1 2 0 }$ 考虑到 $\cos _ { 3 } , \cos _ { 3 }$ 也都是一级小量，所以在略去高级小量之后，我们有：

$$
H = \{ A \omega _ { 1 } - E \omega _ { 3 } , B \omega _ { 2 } - D \omega _ { 3 } , C \omega _ { 3 } \} ,
$$

$$
\frac { \tilde { d } H } { \dot { d t } } = \{ A \dot { \omega } _ { \mathrm { s } } - \dot { E } \omega _ { \mathrm { 3 } } , B \dot { \omega } _ { \mathrm { 2 } } - \dot { D } \omega _ { \mathrm { 3 } } , C \dot { \omega } _ { \mathrm { 3 } } \} ,
$$

$$
\omega \times H = \{ ( C - B ) \omega _ { 2 } \omega _ { 3 } + D \omega _ { 3 } ^ { 2 } , ( A - C ) \omega _ { 3 } \omega _ { 1 } - E \omega _ { 3 } ^ { 2 } , 0 \} _ { \partial }
$$

所以(3.61）式的分量形式是：

$$
\begin{array} { r } { \left\{ \begin{array} { l l } { d \dot { \omega } _ { 1 } + ( c - B ) \omega _ { 2 } \omega _ { 3 } - \dot { E } \omega _ { 3 } + D \omega _ { 3 } ^ { 2 } = 0 , } \\ { B \dot { \omega } _ { 2 } + ( A - C ) \omega _ { 3 } \omega _ { 1 } - \dot { D } \omega _ { 3 } - E \omega _ { 3 } ^ { 2 } = 0 , } \\ { C \dot { \omega } _ { 3 } = 0 _ { \circ } } \end{array} \right. } \end{array}
$$

由上式的最后一式得：

若引进转动轴的方向余弦 $\left\{ l , \ m , \ n \right\}$ ，则:

$$
\begin{array} { r l } & { \left\{ \begin{array} { l l } { { \mathit { l } } = \omega _ { 1 } / \omega \doteq \omega _ { 1 } / \tilde { \omega } , } \\ { m = \omega _ { 2 } / \omega \doteq \omega _ { 2 } / \tilde { \omega } , } \\ { n = \omega _ { 3 } / \omega \doteq 1 , } \end{array} \right. } \end{array}
$$

所以(3.65）的前两式式化为：

$$
\begin{array} { r } { \left\{ \begin{array} { l l } { \Dot { A } \Dot { l } + ( C - B ) \tilde { \omega } m - \Dot { E } + D \tilde { \omega } = 0 , } \\ { B \Dot { m } + ( A - C ) \tilde { \omega } l - \Dot { D } - E \tilde { \omega } = 0 _ { \circ } } \end{array} \right. } \end{array}
$$

转动在点 $( x _ { 1 } , x _ { 2 } , x _ { 3 } )$ 引起的位移和力位 $- \frac { 1 } { 2 } \pi ^ { 2 } s ^ { 2 }$ 引起的位移一样， $\pmb { \mathscr { s } }$ 是该点到转动轴的距离。这个力位称为离心力位。当转动轴和形状轴不重合时，离心力位比这两个轴重合时的离心力位增加了 $\triangle U _ { \infty }$ ：

$$
\begin{array} { r l r } {  { \Delta U _ { \omega } = - \frac { 1 } { 2 } \widetilde { \omega } ^ { 2 } \{ [ ( x _ { 1 } ^ { \prime } + x _ { 2 } ^ { \prime } + x _ { 3 } ^ { 2 } ) - ( x _ { 1 } l + x _ { 2 } m + x _ { 3 } n ) ^ { 2 } ] - ( x _ { 1 } ^ { 2 } + x _ { 2 } ^ { 2 } ) \} , } } \\ & { } & \\ & { } & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { } & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { } & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { } & { = \widetilde { \omega } ^ { 2 } r ^ { 2 } \cos { \theta } \sin { \theta } ( l \cos { \varphi } + m \sin { \varphi } ) , } \\ & { } & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { } & { = - \frac { 1 } { 3 } \widetilde { \omega } ^ { 2 } a ^ { 2 } ( \frac { r } { a } ) ^ { 2 } P _ { 2 1 } ( \cos { \theta } ) ( l \cos { \varphi } + m \sin { \varphi } ) , } \end{array}
$$

式中的（r,θ,φ）是（x，x,x）点的球极坐标,a是地球的平均半径，P是连带勒让德函数。上式说明，△U。是一个球谐函数。这个力位使地球发生弹性变形。变形后的地球在其外部产生了一个附加力位△Ur。△Ur满足拉普拉斯方程，所以可以将它表示为：

$$
\Delta U _ { T } = \sum _ { n = 0 } ^ { \infty } \sum _ { m = 0 } ^ { n } \frac { 1 } { r ^ { n + 1 } } P _ { n m } ( \cos \theta ) ( a _ { n m } \cos m \varphi + b _ { n m } \sin m \varphi ) _ { 0 }
$$

通常把附加力位与引起它的力位之比叫做勒夫数。若以 $k$ 表示地球表面处的勒夫数，则由以上两式可得：

由此确定出：

$$
\begin{array} { r l r } {  { \sum _ { n = 0 } ^ { \infty } \sum _ { m = 0 } ^ { n } \frac { 1 } { a ^ { n + 1 } } P _ { n m } ( \cos \theta ) ( a _ { n m } \cos m \varphi + b _ { n m } \sin m \varphi ) } } \\ & { = - \frac { k } { 3 } \tilde { \omega } ^ { 2 } a ^ { 2 } P _ { 2 1 } ( \cos \theta ) ( l \cos \varphi + m \sin \varphi ) , } \end{array}
$$

$$
\left\{ \begin{array} { l l } { \displaystyle a _ { 2 1 } = - \frac { k } { 3 } \tilde { \omega } ^ { 2 } a ^ { 5 } l , } \\ { \displaystyle a _ { n m } = - \frac { k } { 3 } \tilde { \omega } ^ { 2 } a ^ { 5 } m , } \\ { \displaystyle a _ { n m } = b _ { n m } = 0 , n \ne 2 , m \ne 1 , } \end{array} \right.
$$

从而

$$
\triangle U , \ l = - \ \frac { k } { 3 } \ \tilde { \omega } ^ { 2 } a ^ { 2 } \left( \frac { a } { r } \right) ^ { 3 } P _ { 2 1 } ( \cos \theta ) ( \ l \cos \varphi + m \sin \varphi ) ,
$$

$$
= k \tilde { \omega } ^ { 2 } x _ { 3 } ( l x _ { 1 } + m x _ { 2 } ) \Big ( \frac { a } { r } \Big ) _ { 0 } ^ { 5 }
$$

从另一个角度看，按照麦柯拉夫公式[(2.66)式]，变形前、后地球的引力位 $U , U ^ { \prime }$ 分别为：

$$
\boldsymbol { U } = - \ G \left[ \frac { M } { r } + \frac { \left( \boldsymbol { \mathcal { A } } + \boldsymbol { B } + \boldsymbol { C } - 3 \boldsymbol { l } \right) } { 2 r ^ { 3 } } \right] ,
$$

$$
\begin{array} { r } { U = - \ G \left[ \frac { M } { r } + \frac { \left( \mathit { 1 } + \mathit { B } + \mathit { C } - 3 \mathit { l } \right) } { 2 r ^ { 3 } } \right] , } \end{array}
$$

其中，

$$
I = ( A x _ { 1 } ^ { 2 } + B x _ { 2 } ^ { 2 } + C x _ { 3 } ^ { 2 } ) \frac { 1 } { r ^ { 2 } } ,
$$

$$
I ^ { \prime } = ( { \cal { A } } x _ { 1 } ^ { 2 } + { \cal { B } } x _ { 2 } ^ { 2 } + { \cal { C } } x _ { 3 } ^ { 2 } - 2 { \cal { D } } x _ { 2 } x _ { 3 } - 2 { \cal { E } } x _ { 3 } x _ { 1 } - 2 { \cal { F } } x _ { 1 } x _ { 2 } ) ~ \frac { 1 } { r ^ { 2 } } ,
$$

所以

$$
\triangle U _ { T } = U ^ { \prime } - U = - \ \frac { 3 G } { r ^ { 5 } } \left( D x _ { 2 } x _ { 3 } + E x _ { 3 } x _ { 1 } + \ F x _ { 1 } x _ { 2 } \right) _ { 0 }
$$

对比(3.72)式和上式,即得：

$$
\left\{ \begin{array} { l l } { { D = - \frac { k \tilde { \omega } ^ { 2 } a ^ { * } m } { 3 G } , } } \\ { { } } \\ { { E = - \frac { k \tilde { \omega } ^ { 2 } a ^ { * } l } { 3 G } , } } \\ { { } } \\ { { F = 0 _ { \circ } } } \end{array} \right.
$$

将上式代人(3.68)式,即得：

$$
\left\{ \begin{array} { l } { \displaystyle { \left( A + \frac { k \tilde { \omega } ^ { 2 } a ^ { 5 } } { 3 G } \right) l + \left( C - B - \frac { k \tilde { \omega } ^ { 2 } a ^ { 5 } } { 3 G } \right) \tilde { \omega } m = 0 , } } \\ { \displaystyle { \left( B + \frac { k \tilde { \omega } ^ { 2 } a ^ { 5 } } { 3 G } \right) \dot { m } + \left( A - C + \frac { k \tilde { \omega } ^ { 2 } a ^ { 5 } } { 3 G } \right) \tilde { \omega } l = 0 _ { 0 } } } \end{array} \right.
$$

注意到 $A = B$ ，并令

$$
\sigma _ { \epsilon } = \frac { C - A - \frac { k \tilde { \omega } ^ { 2 } a ^ { 3 } } { 3 G } } { A + \frac { k \tilde { \omega } ^ { 2 } a ^ { 5 } } { 3 G } } \cdot \tilde { \omega } ,
$$

则(3.79）化为

$$
\begin{array} { r } { { \mathopen { } \mathclose \bgroup \left\{ { } _ { { \dot { m } } } ^ { \dot { l } + \sigma _ { c } m = 0 , } \right.}  }  \\ { { \dot { m } - \sigma _ { c } l = 0 _ { \circ } } } \end{array}
$$

这意味着

$$
\left\{ \begin{array} { l } { { \displaystyle l = \frac { K } { \tilde { \omega } } \cos \left( \sigma _ { c } t + \alpha \right) , } } \\ { { } } \\ { { \displaystyle m ^ { \cdot } = \frac { K } { \tilde { \omega } } \sin \left( \sigma _ { c } t + \alpha \right) _ { 0 } } } \end{array} \right.
$$

相应的周期 $\pmb { \tau _ { c } }$ 为:

$$
\tau _ { c } = \frac { 2 \pi } { \sigma _ { c } } = \frac { A + \frac { k \tilde { \omega } ^ { 2 } a ^ { 3 } } { 3 G } } { C - A - \frac { k \tilde { \omega } ^ { 2 } a ^ { 3 } } { 3 G } } \frac { 2 \pi } { \tilde { \omega } } ( { \tt i g E \perp H } ) _ { \circ }
$$

由上式可见，弹性变形使自由章动的周期变长。代入 $G = 6 . 6 7 0 \times 1 0 ^ { - 8 }$ 达因·厘米2/克， $a = 6 . 3 7 1 \times 1 0 ^ { 8 }$ 厘米，并设 $k - 0 . 3 0$ ，可得 $\tau _ { c } = 4 4 8$ 恒星日。仔细的理论计算表明,地慢的弹性可使自由章动的周期延长约120天。由于地球外核是液体,致使这个周期略为缩短。潮汐摩擦作用又使之增长。所以实测的钱德勒晃动的周期在425一440恒星日之间。

地球的转动轴相对于形状轴的运动可以从纬度变化中反映出来。通过纬度变化资料的功率谱分析可以得到两个峰，一个在437日，一个在365日。前者即钱德勒周期,相当于 $k = 0 . 2 8 4$ ，在目前用固体潮确定k值的精度范围内，这个数值和上面取的0.30是一致的。后者是一种周年变化，振幅约为0".09，是季节性变化引进的。此外,还包含有半年变化的成份,其振幅只约为0".01。

# (三)周年变化

地球上的质量迁移,如大气的流动、降雪量的变化、地下水、海水的流动等季节性变化都会影响地球的惯量张量，使得转动轴的方向发生变化。现在我们来分析因为质量迁移引起的转动轴的运动。

仍采用上节用的转动坐标系。我们先来求质量移动后的惯量主轴的方向。设惯量主轴变化不大，所以质量移动后的惯量张量 $\pmb { \mathrm { c } } _ { \imath }$ 为：

$$
\mathbf { C } _ { 1 } = \left[ \begin{array} { l l l } { A } & { - F _ { 1 } } & { - E _ { 1 } } \\ { - F _ { 1 } } & { B } & { - D _ { 1 } } \\ { - E _ { 1 } } & { - D _ { 1 } } & { C } \end{array} \right] ,
$$

其中， $D _ { 1 } , E _ { 1 } , F _ { 1 }$ 是一级小量。惯量主轴的方向 $\pmb { \xi }$ 可以由本征方程

$$
C _ { 1 } \cdot \xi = \lambda \xi
$$

求得。式中，是本征值,这就是：

$$
\left\{ \begin{array} { l l } { ( \mathcal { A } - \lambda ) \xi _ { 1 } - F _ { 1 } \xi _ { 2 } - E _ { 1 } \xi _ { 3 } = 0 , } \\ { - F _ { 1 } \xi _ { 1 } + ( B - \lambda ) \xi _ { 2 } - D _ { 1 } \xi _ { 3 } = 0 , } \\ { - E _ { 1 } \xi _ { 1 } - D _ { 1 } \xi _ { 2 } + ( C - \lambda ) \xi _ { 3 } = 0 _ { \circ } } \end{array} \right.
$$

质量移动后的形状轴和原来的形状轴差别不大，也就是 $\xi _ { 1 } , \xi _ { 2 }$ 是小量， $\xi _ { 3 } \doteq 1 _ { \circ }$ 在略去高级小量后，上式化为：

$$
\left\{ \begin{array} { l l } { ( A - \lambda ) \xi _ { 1 } - E _ { 1 } = 0 , } \\ { ( B - \lambda ) \xi _ { 2 } - D _ { 1 } = 0 , } \\ { C - \lambda = 0 , } \end{array} \right.
$$

从而

$$
\left\{ { \begin{array} { l } { \displaystyle \lambda = C , } \\ { \displaystyle \xi _ { 1 } = { \frac { E _ { 1 } } { A - C } } , } \\ { \displaystyle \xi _ { 2 } = { \frac { D _ { 1 } } { B - C } } } \end{array} } \right.
$$

和上一节的情况类似,因为转动轴和质量移动后的形状轴不一致,地球变形引起了附加力位：

$$
\triangle U _ { T } = k \tilde { \omega } ^ { 2 } x _ { 3 } [ ( l - \xi _ { 1 } ) x _ { 1 } + ( m ~ - ~ \xi _ { 2 } ) x _ { 2 } ] \left( \frac { a } { r } \right) ^ { 5 } ,
$$

上式是把(3.72）式的 $\iota$ 换成 $l - \xi _ { 1 } , m$ 换成 $m - \xi _ { 2 }$ 后得到的。

从另一角度看,若地球绕质量移动后的形状轴转动，则其引力位

$$
\begin{array} { r } { U _ { 1 } = - \ G \left[ \frac { M } { r } + \frac { \left( \underline { { \boldsymbol { A } } } + \boldsymbol { B } + C - 3 I _ { 1 } \right) } { 2 r ^ { 3 } } \right] , } \end{array}
$$

其中

$$
I _ { 1 } = { \frac { 1 } { r ^ { 2 } } } \left( d x _ { 1 } ^ { 2 } + B x _ { 2 } ^ { 2 } + C x _ { 3 } ^ { 2 } - 2 D _ { 1 } x _ { 2 } x _ { 3 } - 2 E _ { 1 } x _ { 3 } x _ { 1 } - 2 F _ { 1 } x _ { 1 } x _ { 2 } \right) _ { 0 }
$$

当它绕转动轴转动时，其引力位

$$
\begin{array} { r } { U ^ { \prime } = - \ G \left[ \frac { M } { r } + \frac { \left( \mathcal { A } + B + C - 3 I ^ { \prime } \right) } { 2 r ^ { 3 } } \right] , } \end{array}
$$

其中

$$
I ^ { \prime } = \frac { 1 } { r ^ { 2 } } \left( \mathcal { A } x _ { 1 } ^ { 2 } + \mathcal { B } x _ { 2 } ^ { 2 } + C x _ { 3 } ^ { 2 } - 2 D x _ { 2 } x _ { 3 } - 2 E x _ { 3 } x _ { 1 } - 2 F x _ { 1 } x _ { 2 } \right) _ { 0 }
$$

所以引力位的变化为

$$
\triangle U _ { T } = - { \frac { 3 G } { r ^ { 5 } } } [ ( D - D _ { 1 } ) x _ { 1 } x _ { 3 } + ( E - E _ { 1 } ) x _ { 3 } x _ { 1 } + ( F - F _ { 1 } ) x _ { 1 } x _ { 2 } ] _ { 0 }
$$

对比(3.89)式和上式，就可以得到：

$$
\left\{ \begin{array} { l l } { { D = D _ { i } - \frac { K \tilde { \omega } ^ { 2 } a ^ { 5 } } { 3 G } \left( m - \xi _ { 2 } \right) , } } \\ { { } } \\ { { E = E _ { 1 } - \frac { K \tilde { \omega } ^ { 2 } a ^ { 5 } } { 3 G } \left( l - \xi _ { 1 } \right) , } } \\ { { } } \\ { { F = F _ { 1 } , } } \end{array} \right.
$$

从而

$$
\begin{array} { r l } & { H = \big \{ \mathcal { A } \omega _ { 1 } - E _ { 1 } \omega _ { 3 } + \frac { \mathcal { k } \tilde { \omega } ^ { 3 } \alpha ^ { 5 } } { 3 G } \left( \mathit { l } - \xi _ { 1 } \right) , B \omega _ { 2 } - D _ { 1 } \omega _ { 3 } } \\ & { \phantom { \mathcal { A } = } + \frac { \mathcal { k } \tilde { \omega } ^ { 3 } \alpha ^ { 5 } } { 3 G } \left( m - \xi _ { 2 } \right) , C \omega _ { 3 } \big \} , } \end{array}
$$

$$
\omega \times H = \Big \{ C \omega _ { 2 } \omega _ { 3 } - \omega _ { 3 } \Big [ B \omega _ { 2 } - D _ { 1 } \omega _ { 3 } + { \frac { k _ { \mathrm { A } } \tilde { \omega } ^ { 3 } a ^ { 5 } } { 3 G } } ~ ( m - \xi _ { 2 } ) \Big ] ,
$$

$$
\omega _ { 3 } [ d \omega _ { 1 } - E _ { 1 } \omega _ { 3 } + \ \underbrace { \bar { k } \tilde { \omega } ^ { 3 } \underline { { a } } ^ { 5 } } _ { 3 \bar { G } } \ ( \mathrm { / - ~ } \xi _ { 1 } ) ] - C \omega _ { 1 } \omega _ { 3 } , \ 0 \} \mathrm { _ { 0 } }
$$

将这些表示式代人运动方程(3.68)式中，即得：

$$
\left\{ \begin{array} { l l } { { \mathit { l } + \sigma _ { c } m = - \frac { n _ { c } } { \tilde { \omega } } \xi , + \sigma _ { c } \xi _ { 2 } , } } \\ { { { } } } \\ { { { \dot { m } - \sigma _ { c } l = \frac { n _ { c } } { \tilde { \omega } } \dot { \xi } _ { 2 } - \sigma _ { c } \xi _ { 1 } , } } } \end{array} \right.
$$

因为 $\dot { \xi } _ { 1 } / \tilde { \omega }$ 和 $\dot { \xi } _ { 2 } / \widetilde { \omega } \ll \xi _ { 1 }$ 和 $\pmb { \xi _ { 2 } }$ ，所以上式可化为：

$$
\left\{ \begin{array} { l l } { { l ^ { l } + \sigma _ { c } m = \sigma _ { c } \xi _ { 2 } , } } \\ { { \dot { m } - \sigma _ { c } l = - \sigma _ { c } \xi _ { 1 } , } } \end{array} \right.
$$

或

$$
\frac { d } { d t } \ ( l + \ i m ) - i \sigma _ { c } ( l + \ i m ) = - \ i \sigma _ { c } ( \xi , + \ : i \xi _ { 2 } ) _ { \circ }
$$

与上列方程相应的齐次方程就是(3.81)式，它的解如(3.82)所示。上列方程的特解相当于强迫运动。

不失一般性，设 $\xi _ { 1 } , \xi _ { 2 }$ 作椭圆运动：

$$
\xi _ { 1 } + \iota \xi _ { 2 } = \overline { { { n } } } e ^ { \iota ^ { \alpha _ { \ell } } } + \overline { { { n } } } ^ { \prime } e ^ { - \iota ^ { \alpha _ { \ell } } } ,
$$

则可求得：

$$
\iota + \iota m = \frac { \overline { { n } } } { 1 - \frac { \alpha } { \sigma _ { c } } } e ^ { \iota ^ { \alpha _ { i } } } + \frac { \overline { { n } } ^ { \prime } } { 1 + \frac { \alpha } { \sigma _ { c } } } e ^ { \iota ^ { \alpha _ { i } } }
$$

倘若 $\xi _ { 1 } , \xi _ { 2 }$ 系由周年变化引起的，即 $2 \pi / \alpha = 1$ 年，则因 $\sigma _ { c } = 2 \pi / \tau _ { c }$ ，所以

$$
\ l + \ { \ i } m = { \frac { \bar { n } } { 1 - \tau _ { c } } } e ^ { \imath 2 \pi t } + \ { \frac { \bar { n } ^ { \prime } } { 1 + \tau _ { c } } } e ^ { - \imath 2 \pi t } \circ
$$

当 $\pmb { \mathscr { t } } = \pmb { 0 }$ 时， $\ l - \ \frac { \overline { { n } } ^ { \prime } } { 1 } - \frac { \overline { { n } } } { \tau _ { c } } - \frac { \overline { { n } } } { \tau _ { c } - 1 } = b$ ， $m = 0$ ；当 $ \ t = 1 / 4$ 时， $l = 0$ ，

$$
m = - \ \frac { \overline { { n } } ^ { \prime } } { 1 + \tau _ { c } } - \frac { \overline { { n } } } { \tau _ { c } - 1 } = - \ a _ { 0 }
$$

这里 $a , b$ 分别表示半长轴和半短轴。这说明转动轴所作的椭圆运动和形状轴作的椭圆运动不同：两个椭圆位相差 $\pmb { \pi } / 2$ ，而且转动方向相反。

# (四)纬度变化

# 1.地心纬度、天文纬度和地理纬度

前面我们讨论了岁差和章动。发生岁差和章动时，地球转动轴和形状轴的相对位置不变，但它们的方向在空间中发生变化。我们也讨论了自由章动,它们是转动轴相对于形

状轴的摆动。这两种运动在地球上都可以测量出来。通过测量恒星的赤纬，可以观测到岁差和受迫章动;通过测量纬度，可以观测到转动轴相对于形状轴的摆动。

纬度有好几种不同的定义。所谓地心纬度 $\pmb { \phi }$ 指的是地面上任一点与地心的联线和赤道面的夹角（图3.3)。天文纬度指的是地面上任一点的铅垂线（大地水准面的法线）与赤道面的夹角 $\phi ^ { \prime }$ 。地理纬度 $\phi$ 则是参考椭球体上某点的法线与赤道面的夹角。因为大地水准面接近于参考椭球面，所以天文纬度和地理纬度相差不大，我们这里不加区别。

![](images/0d02fc6b5f2d6e4b4e7ba59c37a75542aad8306fe776efe949399fc592e4da40.jpg)  
图3.3地心纬度、天文纬度和地理纬度

地心纬度与地理纬度之间有一个简单的关系。设参考椭球面的截面的方程为：

$$
\begin{array} { r } { \frac { x ^ { 2 } } { { a } ^ { 2 } } + \frac { y ^ { 2 } } { { b } ^ { 2 } } = 1 , } \end{array}
$$

其中 $a , b$ 分别是参考椭球的长、短轴。所以

$$
\begin{array} { r } { \frac { d y } { d x } = - \left( \frac { b } { a } \right) ^ { 2 } \frac { x } { y } \circ } \end{array}
$$

因为 tanΦ=y/x，tanΦ=-(dy/dx)-¹，而偏心率ε-√i-(b/a)²，所以Φ和Φ的关系可表示为：

$$
\tan \phi = ( 1 - \mathtt { s } ^ { 2 } ) \tan \phi _ { \circ }
$$

![](images/7a62d1aa99553332f236f153b38f4f9806f0e8d60b931d5f6296d29c26498f06.jpg)  
图3.4岁差(左)和晃动(右),中图为未受扰动的情形

转动轴和形状轴相对位置的变化在测量上是可以和岁差或受迫章动区分开的。图3.4表示如何区分它们。图3.4的中图表示受扰动的地球的位置。OP代表转动轴，北极星在它附近。A是地面上某一指定地点，Z是其天顶，S是空间中的某一恒星，R是OP和地面的交点,即地极。M是形状轴和地面的交点，即参考极。在图3.4的中图里,M和$\pmb R$ 是重合的。

在发生岁差或受迫章动时(图3.4的左图),形状轴(连同转动轴)的位置发生了变化。在这幅图中,M和R也是重合的。这时恒星S的余赤纬（∠SOP）发生变化，而A点的余

纬（ $\angle Z O P )$ 不发生变化。

在发生晃动时(图3.4的右图)，形状轴(因而参考极 $M$ )离开了转动轴，此时，恒星的余赤纬不变而 $\pmb { A }$ 点的余纬发生变化。

这就是说,岁差和受迫章动可以由恒星的赤纬测定，而晃动可以由纬度测定。当然，发生晃动时,经度也有变化，只是因为经度的变化不易测量，所以一般都是通过纬度变化的观测来研究转动轴的运动。

# 2.观测纬度的方法

测量纬度和赤纬的基本方法是用子午环（一架可以绕东西向水平轴转动的折射望远镜)观测恒星上中天和下中天时的天顶距。在恒星上中天时，其天顶距(图3.5左图)

$$
z = \theta - \delta ,
$$

式中， $\theta$ 是余纬， $\pmb { \delta }$ 是该恒星的余赤纬。下中天时，天顶距

$$
z ^ { \prime } = \theta + \delta _ { \circ }
$$

所以

$$
\left\{ \begin{array} { l } { { \theta = \frac { 1 } { 2 } \left( Z ^ { \prime } + Z \right) , } } \\ { { } } \\ { { \delta = \frac { 1 } { 2 } \left( Z ^ { \prime } - Z \right) _ { \circ } } } \end{array} \right.
$$

用这种方法可以同时确定纬度和赤纬，是测定纬度和赤纬的基本方法。

![](images/3bfc300f2215a1a189c307aa3bd40b9409aa8d07c05f835da73966e57b85a3ce.jpg)  
图3.5观测纬度的方法左图为基本方法,右图为塔尔柯特法。

另一种方法称为塔尔柯特（Tallcott）法。这种方法是选取中天时天顶距近似相等，分别位于天顶南北并在几分钟内相继通过子午面的两颗恒星，用天顶仪测量其天顶距之差。当这两颗恒星中天时(图3.5右图)，

$$
\begin{array} { l } { { \displaystyle { \left\{ \theta = \delta - z , \right. } } } \\ { { \displaystyle { \left\{ \theta = \delta ^ { \prime } + z ^ { \prime } , \right. } } }  \end{array}
$$

式中， $\pmb { \delta }$ 是位于天顶南面的恒星的余赤纬， $z$ 是其天顶距， ${ \pmb { \delta } } ^ { \prime }$ 和 $z ^ { \prime }$ 是天顶北面的恒星的相应的量。将上式的一、二两式相加即得：

$$
\theta = \frac { 1 } { 2 } \left( \delta + \delta ^ { \prime } \right) + \frac { 1 } { 2 } ( Z ^ { \prime } - Z ) _ { \circ }
$$

&和δ可以由天文年历的星表中查到，Z'一Z 是这两颗恒星的天顶距之差。塔尔权特法不是基本方法，因为用它来测量纬度时需要予先知道平均极距 $\frac { 1 } { 2 } \left( \delta + \delta ^ { \prime } \right) _ { \mathcal { C } }$ ，但在纬度观测中经常使用这个方法,因为它有两个优点：用两颗星的天顶距相减可以消除蒙气差，并且用测微器测量小角度Z'一Z 比在一个度盘上测量Z和 Z'精确。

为了精确地测定纬度，除了必须考虑大气折射影响外，还必须考虑其他因素的影响，如固体潮引起的垂线偏差。现在纬度测量已是一件常规工作。国际纬度局（InternationalLatitude Service，缩写为 ILS，1962年起改名为国际极移局，International Polar MotionService，缩写为IPMS)在北半球有39个同纬度的、经度等间距的纬度站。每个站的观测精度是0.1弧秒，所以这些纬度站观测结果的平均值的精度约为0.01秒。

# 3.地极移动

地轴相对于形状轴位置的变化表现为地极位置的移动，简称极移。地极移动是相对于形状轴而言的，可是形状轴在地球上也不是固定的。为了测定地极的位置，1967年国际天文学联合会（IAU）和国际大地测量和地球物理联合会（IUGG）决定采用1900年至1905年地球转动极的平均位置作为参考点，叫国际习用原点（Conventional International Origin,缩写为 CIO)。这样，极移便可以用转动极相对于CIO的位移来表示。

图36中的 $^ o$ 卢表示 CIO，过CIO 作两条切线 $O x$ 和 $O y _ { \circ } \textbf { \em x }$ 轴通过格林尼治子午面，以指向格林尼治的方向为正， $\pmb { y }$ 轴通过西经 $9 0 ^ { \circ } \circ \quad x , y$ 组成左旋坐标系。在此坐标系内，地极 $P$ 的坐标可用直角坐标 $( x , \ y )$ 表示，也可用极坐标 $( \rho , \theta )$ 表示， $\theta$ 从 $\pmb { x }$ 轴顺时针算起。由图36可知，

![](images/e5248c6e0bf6ccfaf1b03d77c4435f28dae6c5d6464833835c764ad9910d4744.jpg)  
图3.6纬度变化

$$
\left\{ { \begin{array} { l } { x = \rho \cos \theta , } \\ { y = \rho \sin \theta \circ } \end{array} } \right.
$$

设 $s$ 是纬度观测站，它对 $o$ 的地理坐标为 $( \varphi _ { s } , \lambda _ { s } )$ ，对地极 $\pmb { P }$ 的地理坐标为 $( \varphi , \lambda )$ ，于是,在 $s$ 点测得的纬度变化 $\Delta \varphi _ { s } = \varphi - \varphi _ { s 0 }$

从地极引一条球面垂线 $\widehat { P R }$ 至子午线 $\widehat { o s }$ 。因 $\widehat { o P }$ 很小，故 $\widehat { o _ { R } } , \widehat { P _ { R } }$ 也很小,于是球面三角形可视为直角三角形。 ${ \widehat { P S } } = 9 0 ^ { \circ } - \varphi , { \widehat { O S } } = 9 0 ^ { \circ } - \varphi , { \widehat { R S } } \doteq { \widehat { P S } } ,$

$$
\widehat { O R } = \widehat { O S } - \widehat { R S } \doteq \Delta \varphi _ { s 0 }
$$

又因为

$$
\widehat { O R } = \rho \cos { ( \theta - \lambda _ { s } ) } ,
$$

所以，

$$
\Delta \varphi _ { s } = \rho \cos \theta \cos \lambda _ { s } + \rho \sin \theta \sin \lambda , ,
$$

$$
\Delta \varphi _ { s } = x \cos \lambda _ { s } + y \sin \lambda _ { s 0 }
$$

考虑到观测误差、星表误差、天文常数的误差、地方性的误差(如大气折射、垂线变化等)，应当在上式中再加上一项 ${ \pmb z } _ { \pmb { \varpi } }$ ：

$$
\Delta \varphi _ { s } - z _ { \varphi } = \tau \cos \lambda _ { s } + \gamma \sin \lambda _ { s } ,
$$

$z _ { \varphi }$ 项称为木村项。

由上式可知，若两纬度站的经度相差 $1 8 0 ^ { \circ }$ ，则一处的纬度增加时，另一处的纬度应当相应地减小。图3.7是一个例子。1891年，为了和柏林同时观测纬度，一支德国探险队被派遣到和柏林经度相差 $1 7 1 ^ { \circ }$ （接近 $1 8 0 ^ { \circ }$ ）的檀香山。这幅图是这两个地方的纬度在1891一1893年间的变化。从图上可见,当檀香山的纬度减少时,柏林的增加；反之亦然。

图3.8是1962年至1968年的极移轨迹。地极的移动在xy切面内是螺旋形的曲线，它交错地时而向内、时而向外移动,有时有驻点或者掉转方向旋转。在这幅图中，迴线的最大直径约为 $0 ^ { \prime \prime } . 5 ;$ 自1900年以来，这种迴线的最大直径曾达到 $0 . ^ { \prime \prime } \eta _ { \circ }$ 转动轴相对于参考轴的角位移与地极相对于参考极的线位移的换算关系是： $0 . { } ^ { \prime \prime } 0 1 0 0 = 0 . 3 0 8$ 米，所以幅度为0."7的转动轴的角位移相当于地极在地面上移动了21米。

![](images/6789fcd8163f1f4a2a26e0224d0551a9f127856d34d735f6a9140e5e3d78f99f.jpg)  
图3.7柏林和檀香山两地的纬度变化

![](images/1ed27adb665ccf3a0e56bf49e20a7757ca8d8dfbad14c7cbaff59e939dbac639.jpg)  
图3.81962年至1968年的极移轨迹

极移的轨迹看起来很不规则，但是用频谱分析法可以从中分析出不同周期的分量。通过对大约80年来极移数据的分析，可以得到一个14个月的分量和一个一年的分量。前者就是钱德勒晃动，后者是周年变化。

地球的外核是液体，它除了对钱德勒周期有影响外，还由于与地幔耦合，对地球的转动产生微小的干扰,这个成份叫做马柯维茨（Markowitz）章动，其周期略小于一日，振幅约为 $0 \ ^ { \prime \prime } 0 2$ ，地球的固体内核通过外核也与地幔耦合，产生相同数量级的干扰，周期约为24—40年。

极移轨迹的幅度大约每6一7年达到一次最小值，因此一个地点的平均纬度就取它在6一7年间的纬度的平均值，而地球的平均形状极则由许多纬度站的平均纬度计算出。这个极已从七十年前的位置朝芬兰方向移动了大约0."2。这种运动称为平均极的长期变化。长期变化很不规则，很难将它与大陆漂移引起的纬度变化分开。它可能是海平面变化和地球内部构造运动引起的转动惯量变化的结果。

# （五）钱德勒晃动的衰减和激发

钱德勒周期并不是单值的,而是在相当宽的范围内（由425天到440天)内变化。这表明它是一个有阻尼的运动。这种阻尼运动的衰减时间常数有人估计是27年左右。不过，也有人估计它为225年。钱德晃动的振幅在几十年的观测中一直保持在 $\mathfrak { 0 . 7 1 }$ 至0."2间而不消失，这意味着它不断地受到新的激发。设钱德勒晃动是自由周期为 $\pmb { \tau _ { \epsilon } }$ 的衰减运动，以品质因质 $Q$ 表示贮存在这个振荡系统中的能量 $\pmb { \cal E }$ 和在一个周期内耗散的能量 $\pmb { \triangle E }$ 之比:

$$
\begin{array} { r } { Q ^ { - 1 } = \frac { 1 } { 2 \pi } \frac { \Delta E } { E } , } \end{array}
$$

则可以证明， $\varrho$ 可以用钱德勒晃动的共振曲线的宽度 $2 \pmb { \triangle } \pmb { \sigma }$ 与峰值频率 $\pmb { \sigma _ { \epsilon } }$ 的比值来表示：

$$
Q ^ { - 1 } = \frac { 2 \Delta \sigma } { \sigma _ { c } } \circ
$$

由钱德勒晃动的频谱，可以计算共振曲线的宽度，从而求得 $\pmb { Q }$ 值。有人求得 $\pmb { Q }$ 大约是$7 2 \pm 2 0$ ，相当于衰减的时间常数为27年；但也有人求得 $Q = 6 0 0$ ，相当于衰减的时间常数为225年。

钱德勒晃动衰减很快。是什么原因使它衰减？这个问题尚未解决。地幔的非弹性所产生的衰减很小。潮汐摩擦和地幔与地核的滞性耦合或电磁耦合所消耗的能量，也不能造成数量级这样大的衰减。有人曾试图从地幔物质的流变性质找出衰减的原因，但未能得到令人满意的结果。近年来有人认为钱德勒晃动可能是由两个自由周期相近(约相差十天)的振动组成的,它们迭加在一起，产生“拍”。照此观点,钱德勒晃动振幅的变化和频谱的加宽只是一种干涉现象，而不是由于衰减。不过,要从不到八十年的极移记录中分析出相差十天左右的两个周期成份，从统计分析的角度看,是很不可靠的。这种解释有待进一步研究。

钱德勒晃动的激发，同样是一个悬而未决的问题。有人认为，外界的影响不大，主要是地球内部角动量的再分布引起钱德勒晃动，同时也引起转速的变化。

布拉德（E.C.Bullard）认为,可以用地幔和地核间的电磁耦合同时解释钱德勒晃动和转速的变化。这是因为硅酸盐在温度升高时具有半导体的特性，所以地幔的下部能导电。当地幔和产生磁场的地核之间出现运动上的差异时，它们之间就要出现电磁耦合作用，结果导致钱德勒晃动衰减，并导致地球转速发生变化。

为简单计，假定地核是一个整体,但以不同于地幔的角速度转动。我们先来分析地幔和地核在转动速度上的差异是如何通过电磁耦合恢复平衡的。以 $\imath _ { \bullet }$ 和 $\pmb { I _ { m } }$ 分别表示地核和地幔的惯量矩,以 $\omega + \bigtriangleup { \omega _ { c } }$ 和 $\omega + \triangle \omega _ { m }$ 分别表示它们转动的角速度。其中， $\pmb { \omega }$ 是它们平衡时的角速度。由于角动量守恒,所以

$$
\begin{array} { r } { I _ { m } \Delta \omega _ { m } + I _ { c } \Delta \omega _ { c } = 0 , } \end{array}
$$

从而地幔和地核的角速度之差

$$
\triangle \omega = \Delta \omega _ { m } - \Delta \omega _ { c } = \triangle \omega _ { m } \Big ( 1 + \frac { I _ { m } } { I _ { c } } \Big ) = 8 . 7 4 \Delta \omega _ { m }
$$

地幔(导体)以角速度 $\vartriangle C$ 切割磁力线，感应电流应正比于 $\vartriangleleft$ 。设地幔与地核之间的耦合是线性的，也就是说使地幔与地核的角速度趋于一致的力矩正比于 $\vartriangle$ ：

$$
L = K _ { R } \Delta \omega ,
$$

其中， $K _ { R }$ 是耦合系数，它与地幔的导电率和磁力线穿透它的具体情况有关。将(3.118)式和(3.119)式代人下式：

$$
L = - \ I _ { m } \frac { d } { d t } \ \Delta \omega _ { m } ,
$$

就可得出：

$$
\begin{array} { r } { \frac { d \left( \Delta \omega _ { m } \right) } { \Delta \omega _ { m } } = - \kappa _ { R } \Big ( \frac { 1 } { I _ { m } } + \frac { 1 } { I _ { c } } \Big ) d t , } \end{array}
$$

从而

$$
\Delta \omega _ { m } = ( \Delta \omega _ { m } ) _ { 0 } e ^ { - \pmb { \varepsilon } / \tau } R
$$

其中，

$$
\tau _ { R } = \biggl [ K _ { R } \left( \frac { 1 } { I _ { m } } + \frac { 1 } { I _ { c } } \right) \biggr ] ^ { - 1 }
$$

这就是说， $\pmb { \triangle } \pmb { \omega } _ { m }$ 以时间常数 $\pmb { \tau _ { R } }$ 指数地衰减。若取 $\tau _ { R } \doteq 1 0$ 年，那么可得

在弱耦合(即地核几乎跟不上地幔的晃动)情形下，钱德勒晃动的能量 $\pmb { E } _ { \pmb { \ W } }$ 等于：

$$
E _ { w } = { \frac { 1 } { 2 } } l _ { m } H \omega ^ { 2 } \alpha ^ { 2 } ,
$$

式中，α是钱德勒晃动的角振幅。在现在讨论的情形下,地幔和地核的相对角速度

$$
\Delta \omega ^ { \prime } = \sigma _ { c } \alpha ,
$$

式中， $\pmb { \sigma } _ { \pmb { \mathscr { s } } }$ 是钱德勒晃动的角频率。如果其衰减是由于地幔和地核之间的电磁耦合,那么：

$$
\begin{array} { r } { \frac { d E _ { w } } { d t } = - \kappa _ { w } ( \Delta \omega ^ { \prime } ) ^ { 2 } = - K _ { w } \sigma _ { c } ^ { 2 } \alpha ^ { 2 } , } \end{array}
$$

式中， $K _ { \pmb { \mathscr { W } } }$ 是钱德勒晃动的耦合系数。将(3.124)式代人上式，即得：

$$
\begin{array} { r } { \frac { d E _ { w } } { d t } = - \frac { 2 K _ { w } \sigma _ { c } ^ { 2 } } { I _ { m } H \omega ^ { 2 } } E _ { w } , } \end{array}
$$

所以

$$
E _ { w } = ( E _ { w } ) _ { 0 } e ^ { - t / \tau _ { w } } ,
$$

式中，

$$
\tau _ { w } = \frac { I _ { m } H } { 2 K _ { w } } \left( \frac { \omega } { \sigma _ { c } } \right) ^ { 2 } \circ
$$

上式说明， $\pmb { E } _ { \pmb { \ W } }$ 以时间常数 $\pmb { \tau } _ { \pmb { \mathscr { W } } }$ 指数地衰减。

Kw应当和KR相当,即Kw=K=2.6×102焦耳·秒,所以由上式可得

这个数值比从实际资料得到的最大的衰减时间（225年)大两个数量级，由此看来，电磁耦合很难解释钱德勒晃动和转速变化。

有人认为，钱德勒晃动可能是由大地震激发的。这种见解在六十年代前已有人提出过,但不太受重视。1967年,曼新哈（Mansinha）和斯迈里（Smylie）又提出这个问题。他们认为大地震造成大规模的质量迁移，使地球的转动惯量发生变化，从而激发地震。

曼新哈和斯迈里的理论的要点是：在地球内部，震前和震后，应力都是动态平衡的。这就使得地球的质心不因地震而移动,即：

$$
\int _ { ( M ) } \int \displaylimits _ { } ^ { } \Delta \bmod { m } = 0 ,
$$

其中, $\vartriangleleft$ 是坐标原点至质量 $d m$ 的矢径在地震前后的变化，即 $\scriptstyle { d m }$ 的位移矢量，积分遍及整个震源区和整个地球。这个式子说明，虽然地震时可能出现显著的地壳升降和错动，但从大范围看，位移必定是平衡的。

地震是岩层的错动。设想地震时，两块质量为 ${ \pmb m } _ { 1 }$ 和 ${ \pmb m } _ { 2 }$ 的岩石相对移动。设地震前它们到转动轴的距离分别为 ${ \pmb r } _ { 1 }$ 和 $\boldsymbol { r } _ { 2 }$ ，地震时各自移动了 $\pmb { \triangle r _ { 1 } }$ 和 $\triangle \ r _ { 2 }$ .由上式可得：

$$
m _ { 1 } \Delta r _ { 1 } + m _ { 2 } \Delta r _ { 2 } = 0 _ { o }
$$

相对于转动轴,地球的惯量矩因为地震发生了 $\triangle I$ 的变化:

$$
\Delta I = m _ { 1 } [ ( r _ { 1 } + \Delta r _ { 1 } ) ^ { 2 } - r _ { 1 } ^ { 2 } ] + m _ { 2 } [ ( r _ { 2 } + \Delta r _ { 2 } ) ^ { 2 } - r _ { 2 } ^ { 2 } ] _ { 0 }
$$

设 $\triangle r _ { 1 }$ 和 $\triangle r _ { 2 }$ 是小量,运用(3.123)式并略去二级小量,我们便得到：

$$
\Delta I = 2 m _ { 1 } \Delta r _ { 1 } ( r _ { 1 } - r _ { 2 } ) _ { \circ }
$$

由上式不难估计一个大地震引起的惯量矩的变化。以1964年阿拉斯加8.3级大地震为例。取 $\Delta r _ { 1 } = 2 2$ 米， $r _ { 1 } - r _ { 2 } = 2 0 0$ 公里（相当于断层面宽度)，假定断层长度为800公里，则发生位移的质量所占体积为800公里 $\times ~ 2 0 0$ 公里 $\times ~ 2 0 0$ 公里。设密度为3克/厘米,则 $m _ { 1 } \doteq 1 0 ^ { 3 3 }$ 克，从而

惯量积的变化与惯量矩的变化是同一数量级的量。在岩层错动方向最有利的情况下，数量级为 $\triangle l$ 的惯量积的变化可以引起钱德勒晃动的角振幅发生

$$
\Delta \alpha = \frac { \Delta I } { C - \mathcal { A } } = 3 . 5 \times 1 0 ^ { - 9 }
$$

的变化[参阅(3.88)式]。在计算上式时，取C一A=2.6×10克·厘米。这个幅度是太小了;因为现在观测到的钱德勒晃动的平均幅度是 $0 . { } ^ { \prime \prime } 1 5 = 7 . 5 \times 1 0 ^ { - 7 }$ 弧度。

地震能量主要是由为数不多的较大地震释放的。由位错理论可知，惯量矩的变化近似与能量的平方成正比。这样一来，只有特别大的地震才能引起惯量矩的显著变化。但是计算值和观测值差别太大，即便是同步地发生一系列特别大的地震也不足以激发钱德勒晃动。

人们对曼新哈和斯迈里发表的极移和地震的相关性的实际资料也产生了怀疑。曼新哈和斯迈里从几十年来的极移资料中发现，大地震时平均地极的轨迹由一个圆弧换到另一个圆弧上,轨迹出现了间断。然而,有人指出,如果用不同的统计分析方法处理数据,则轨迹的突然性转折和大地震的相关性其实不大。

即使极移和大地震确有关系，也必须分辨它究竟是大地震的成因，还是大地震的结果。如果是前者，那么这种联系对地震预报有重要意义。第三种可能是,极移和地震都来源于地球内部的某种过程，它们在表面上相关，但未必有直接的因果关系。

激发钱德勒晃动的另一种可能机制是大气的运动。大气运动的质量不大，但运行的距离却不小，可与地球的半径相比拟。设想质量为 $\vartriangle A m$ 的大气移动了像地球半径那么远的距离，则惯量矩的变化 $\triangle I$ 为：

$$
\Delta I = \triangle m { a ^ { 2 } } _ { \circ }
$$

如果 $\triangle l = 1 0 ^ { 3 6 }$ 克·厘米,则

$$
\triangle m = \triangle l / a ^ { 2 } = 2 . 5 \times 1 0 ^ { 1 8 }
$$

即 $2 . 5 \times 1 0 ^ { 1 8 }$ 克的大气就足以引起 $1 0 ^ { 3 6 }$ 克·厘米的惯量矩的变化。这个数值仅是全部大气质量的 $5 \times 1 0 ^ { - 4 }$ 。根据1873年至1950年期间的气压资料，芒克（Munk）和哈森(Hassan）分析了大气惯量矩和惯量积的月均值。他们得出结论说，大气的运动不足以激发钱德勒晃动(差一至两个数量级),但极移中的周年变化则是由大气激发的。

激发钱德勒晃动的又一种可能的机制是太阳风(太阳幅射的粒子流)。但计算表明太阳风的扰动和不规则性引起的、作用在磁层上的力矩太小，不足以解释钱德勒晃动。

有人认为,地核的湍流对地慢的电磁效应产生一种短期的冲量,使地球的自转轴突然改变方向，但形状轴不变。这同时会使极移轨迹发生转折，使地球内部应力重新分布，从而也可能触发地震。

还有人认为，地核和地幔的扁率不同，它们在旋进时产生运动上的差异，造成较大的电磁效应，激发极移。

# 三、转速的变化

# （一）地球的转动和时间

时间标准原先是根据地球的转动确定的。地球自转一周的时间叫做一日。由于观测周期所采用的参考点不同，“一日"的定义也略有不同。若取春分点为标准，则它连续两次通过同一子午面的时间,叫做一恒星日;若取太阳为标准,就叫做太阳日。地球不但自转，而且绕太阳公转,公转的轨道是椭圆的,所以太阳日在一年中不是等长的。取其一年的平均值,就得到一平均太阳日，这就是日常生活中所用的日,每日有86.400平均太阳秒。但在天文观测中仍用恒星时。一个平均太阳日比一个恒星日长3'55".909平均太阳时。

地球绕太阳一周的时间叫做一年。若以恒星为标准，这段时间叫做一恒星年，它有365.25636个平均太阳日，每百年约增长0.01秒，这是地球公转的真正周期。若以春分点为标准，就得到回归年。因为分点的岁差效应，回归年比恒星年约短20分钟，它有365.2422个平均太阳日，每百年约减短0.53秒。因为季节变化取决于太阳相对于春分点的位置,所以民用和纪年一般都采用回归年。

根据地球的自转确定的时间叫世界时（UT，Universal Time的缩写)，它以英国格林尼治的地方时间为起点，按照各地的经度向后推移，所用的单位是平均太阳时。这是一切民用时间的标准。显然，若要以地球的自转确定时间，自转速度就必须很均匀。其实不然,近年来通过天文测量和原子钟发现，地球的转速并不是真正均匀的，而是有微小的变化。所以,从1955年起,在精密的天文测量中引用了原子时（AT,Atomic Time 的缩写）。原子时是由原子的振动频率确定的,与地球的转动无关。氢、铷、铯等元素的原子振动频率稳定性很高，相对变化只有 $1 0 ^ { - 1 3 } - 1 0 ^ { - 1 4 }$ ，是极均匀的时间标准。现在用的另一种计时方法是历书时（ET，Ephemeris Time 的缩写)。历书时是由日、月和行星的运动确定的、与地球自转没有关系,只取决于牛顿定律。一历书秒等于1900 年开始的那个回归年除以该年的秒数，即31,556,925.9747。铯原子的振动频率是 $9 , 1 9 2 , 6 3 1 , 7 7 0 \pm 2 0$ 周/历书秒，所以现在国际上规定的时间标准是：1历书秒等于铯原子 $1 3 3 \mathrm { ( C } _ { \varepsilon } ^ { 1 3 3 } )$ 振动9,192.63177兆周的时间。

# （二）地球转速的变化

地球的自转速度的变化可以用日长表示。所谓日长（lengthofday，缩写为1.o.d.）就是一日之长，即地球自转一周的时间。日长的变化反映了转速的变化。设日长为l，其变化为 $\mathbf { \Delta } d l$ ，那么转速的相对变化

$$
\sigma = - \ d l / l _ { \circ }
$$

例如,若 $d l = 1$ 毫秒，则 $\sigma = - 1 1 6 \times 1 0 ^ { - 1 0 } ,$

加速度 $\pmb { \alpha }$ 定义为：

$$
\alpha = d \sigma / d t _ { \circ }
$$

若日长每百年增长1毫秒，则 $\alpha = - 1 . 1 6 \times 1 0 ^ { - 1 0 } /$ 年。

地球自转速度的变化其实很小。三十年代以前，最好的天文钟也不过准到百分之一秒。这样的精确度对于测定地球自转速度的变化是不够的。直到石英钟和原子钟问世以后，再配合高精度的现代测量仪器，如照像天顶仪、莱塞测距仪，超长基线干涉仪等，人们才能对地球转速在较短时间内的变化进行系统的研究。到目前为止，人们发现地球的转速有三种变化：长期变化、不规则变化和季节变化。它们的数量级如表3.1所示。

表3.1  

<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>长期变化</td><td rowspan=1 colspan=1>不规则变化（最大值）</td><td rowspan=1 colspan=1>季节变化（最大值）</td></tr><tr><td rowspan=1 colspan=1>α（加速度）σ（地球自转速度）</td><td rowspan=1 colspan=1>-1.6×10-1/年13×10-1*</td><td rowspan=1 colspan=1>±80×10-10/年±500×10--0</td><td rowspan=1 colspan=1>±650×10-10/年士70×10-10</td></tr></table>

\*这是2,000年的累积变化

根据多年积累的日食观测资料，天文工作者很早就发现月球的平均运动每百年约有10”的加速。这个加速的一部分可能是由于地、月的引力，另一部分5”多只能归因于地球转速变慢的结果。这相当于日长每百年约增长1一2毫秒。现在不但可以由天文观测算出在历史时期地球自转的长期变化，而且还可以利用化石“时钟”追溯地质时期地球自转的长期变化。例如,有一种珊瑚化石上面有年轮、月轮和日轮，根据这种化石可以知道，在三亿七千多万年以前,即在泥盆纪中期，每年约有400天。由此推知，从那时到现在平均每百年日长增加2.4毫秒，和历史年代的数值很接近。现在的测量结果也是同样的数量级，约每百年增加1.4毫秒。引起地球自转长期减速的原因主要是潮汐摩擦。潮汐摩擦引起地球自转角动量减小,同时使月球离地球越来越远，进而使月球绕地球公转的周期变长。这种潮汐摩擦作用主要发生在浅海地区。另外，大气的振荡、冰川的消长，地幔和地核的角动量交换也会引起地球转速的长期变化。这些问题目前尚在研究中。

地球自转速度除了上述的长期变化外，还存在着时快时慢的不规则变化。这种变化同样可以在月球、太阳和行星的观测资料以及天文测时资料中得到反映。它大致可以分为三种： $\textcircled{1}$ 在几十年或更长的一段时间内约有不到 $\pm \ 5 \times 1 0 ^ { - 1 0 } /$ 年的相对变化； $\textcircled{2}$ 在几年到十年的时间内约有不到 $\pm 8 \times 1 0 ^ { - 9 } /$ 年的相对变化； $\textcircled{3}$ 在几个星期到几个月的时间内约有不到$\pm \ 5 \times 1 0 ^ { - 8 } /$ 年的相对变化。前两种变化相对说来比较平缓，而最后一种变化相当急骤。产生这些不规则变化的机制，目前尚无定论。平缓的变化可能是由于地幔和地核的角动量交换或海平面变化引起的；而急骤的变化可能是由于风的作用引起的。图3.9是1820一1969年地球自转速度 $\pmb { \sigma }$ 与加速度 $\pmb { \alpha }$ 的变化，图3.9a中的斜线相当于 $^ { - 1 . 6 } \times 1 0 ^ { ^ { - 1 0 } } /$ 年的长期减速。

![](images/10bbce8a44277e9792e2cc8019232fa484661edc85f7016df392d71f10c60bb7.jpg)  
图3.91820年—1969年地球自转速度 $\pmb { \sigma }$ 与加速度 $\pmb { \alpha }$ 的变化

以前有人认为,地球的转速在某些时间曾经发生过间断性的突然变化,相当于日长突然变化1一3毫秒。但自从采用原子钟后，未再发现这个现象。图3.10是1955年至1970年地球自转速度的变化情况，由图可见，如果按季节平均的话,这个变化可以用一条折线表示，其转折点在1957.79，1961.93和1965.61年处，这意味着从1955年起，加速度约每四年就有一次突变，但速度是连续的。这个现象的物理意义，现在还不清楚。

地球自转速度的季节性变化是五十年代发现的。图3.10表明,这种变化的最主要特点是春天变慢、秋天变快的年变化和周期为半年的变化。年变化的幅度约为20-25毫秒，半年变化的幅度约为9毫秒。 年变化是由风和洋流(主要是风)引起的。 在南半球夏季时，角动量比北半球夏季时的角动量大。风也可以引起周期为半年的变化，但不是半年变化的主要原因。半年变化的主要原因可能是地球潮汐屈服引起的惯量矩的变化。太阳的

表3.2地球的转动  

<table><tr><td rowspan=1 colspan=1>地球自转轴在空间的运动</td><td rowspan=1 colspan=1>地球自转轴在地球上的运动</td><td rowspan=1 colspan=1>地球自转速度的变化</td></tr><tr><td rowspan=1 colspan=1>1.地轴的旋进，黄赤交角23°.5,周期～25,700年。2.主要章动,振幅9.&quot;206,周期18.6年。3.黄赤交角长期减小，~47&quot;/百年</td><td rowspan=1 colspan=1>1.地极的长期迁移：70年迁移约0.&quot;2。2.马柯维茨章动，振幅0.&quot;02(?)，周期24-40年(？)3.钱德勒章动,振幅二0.&quot;15，周期425—440天，衰减时间14—73年(?)4.季节章动：年变化振幅二0.&quot;09,半年变化振幅二0.&quot;01。5.日章动,振幅≤0.&quot;02(?）周期比一恒星日少三分。6.月章动，双周章动:振幅≈0.&quot;001(理论值）</td><td rowspan=1 colspan=1>1.长期减速≤5×10-1°/年。2.无规则变化：（1）几百年期间，α≤±5×10-10/年；（2)1--10年期间，α≤±80×10-1/年；（3）几月或几周(急剧变化),α≤±500×10-10/年。3.短周期变化：（1）二年变化，振幅≈9毫秒；（2）年变化,振幅20-25毫秒；（3）半年变化,振幅≈9毫秒；（4）月变化,双周变化,振幅二1毫秒</td></tr></table>