$$
{ \mathrm { C } } _ { \mathrm { w } } = { \left[ \begin{array} { l l l l } { 1 3 4 1 . 6 3 } & { 8 7 6 . 5 3 } & { 9 7 6 . 7 9 } & { 1 4 2 4 . 8 0 } \\ { 7 0 2 . 2 6 } & { 7 9 7 . 6 8 } & { 1 3 6 8 . 1 2 } & { 1 5 7 2 . 9 8 } \\ { 1 0 2 2 . 7 5 } & { 1 4 6 9 . 5 2 } & { 1 6 4 1 . 9 0 } & { 1 0 2 1 . 1 1 } \\ { 1 4 8 0 . 5 7 } & { 1 4 5 1 . 3 2 } & { 1 1 7 7 . 7 4 } & { 8 9 2 . 1 4 } \end{array} \right] }
$$

最后由(13·154)式可以算得未知点的重力异常

$$
\widetilde { \mathbf { S } } = \left( \begin{array} { l } { \Delta \mathbf { g } _ { 1 } } \\ { \Delta \mathbf { g } _ { 2 } } \\ { \Delta \mathbf { g } _ { 3 } } \\ { \Delta \mathbf { g } _ { 4 } } \end{array} \right) = \left( \begin{array} { l } { 3 5 . 2 2 } \\ { 4 7 . 6 3 } \\ { 3 0 . 1 2 } \\ { 2 3 . 0 3 } \end{array} \right)
$$

同时,由(13·155）式可以算得推估值的中误差,m=√E,m=±9.3.mag=±15.9,mg=士15.2,mg=±16.9,以上这些结果的单位都是毫伽。

# 13.10推求高程异常

由司托克斯公式或莫洛琴斯基公式推求高程异常时，都只用了重力异常数据。当按最小二乘配置方法推求高程异常时，除了重力异常还可同时运用垂线偏差数据。此时·也还只是利用配置方法中的推估。由(13·24)式可得

$$
\mathrm { u } { = } \mathrm { C } _ { \mathrm { u t } } ( \mathrm { C } _ { \mathfrak { u } } { + } \mathrm { C } _ { \mathfrak { n } \mathfrak { n } } ) ^ { - 1 } \mathcal { l }
$$

式中

$$
\mathbf { u } = \boldsymbol { \mathfrak { Y } } ( \mathbb { P } )
$$

就是要求的P点的高程异常；观测向量l包含N个重力异常值和垂线偏差子午分量和卯酉分量 $\eta$ 各 $\mathfrak { q }$ 个，即

$$
l = ( \Delta \mathrm { g } _ { 1 } , \cdots \cdots , \Delta \mathrm { g } _ { \mathrm { N } } , \hat { \mathsf { \Pi } } _ { 1 } , \cdots \cdots , \hat { \mathsf { \Pi } } _ { q } , \eta _ { 1 } , \cdots \cdots , \eta _ { q } )
$$

假定所有的△g有相同的误差mg，所有的和n分别有相同的误差m；和m，,且点之间的误差互不相关。那末，噪声的方差协方差阵Cmm是一个对角阵，即

而已知信号的方差协方差阵为

$$
\{ \begin{array} { c c c c c c c c c } { \Gamma ( \Delta _ { 8 } ; \Delta _ { 9 } , \ldots , \Gamma ( \Delta _ { 2 } ; \Delta _ { 8 } ) , \ \Gamma ( \Delta _ { 8 } ; \hat { \mathbf { t } } _ { 1 } ) , \ \ldots , \Gamma ( \Delta _ { 8 } ; \hat { \mathbf { t } } _ { 3 } ) } & { \mathrm { C ( \Delta _ { 8 } ; \hat { \mathbf { t } } _ { 3 } ) } } & { \mathrm { C ( \Delta _ { 2 } ; \Delta _ { 1 } ) } } & { \mathrm { , } } & { \mathrm { , } } & { \mathrm { } } & { \mathrm { } } & { \mathrm { } } \\ { \vdots } & { \vdots } & { \vdots } & { \vdots } & { \vdots } & { \vdots } & { } \\ { \vdots } & { \vdots } & { \vdots } & { \vdots } & { \vdots } & { \vdots } & { } & { \vdots } \\ { \vdots } & { \vdots } & { \vdots } & { \vdots } & { \ddots } & { \vdots } & { \vdots } & { } \\  \mathrm { C ( \Delta _ { 8 } ; \Delta _ { 8 } ) , \ \ \ldots , \Gamma ( \Delta _ { 9 } ; \Delta _ { 8 } ) , \ \Gamma ( \Delta _ { 1 6 } ; \hat { \mathbf { t } } _ { 3 } ) , \ldots , \Gamma ( \Delta _ { 2 } ; \Delta _ { 1 6 } ) , \ \ldots , \Gamma ( \Delta _ { 9 } ; \hat { \mathbf { t } } _ { 3 } ) } & { \mathrm { C ( \Delta _ { 8 } ; \hat { \mathbf { t } } _ { 8 } ) } } & { \mathrm { , } } & { \mathrm { , } } & { \mathrm { } \mathrm { , } } & { \mathrm { } \mathrm { } \forall ( \Delta _ { 8 } ; \hat { \mathbf { t } } _ { 1 } ) } \\ { \Gamma ( \Delta _ { 1 } ; \Delta _ { 1 5 } ) , \ \ldots , \mathrm { } } & { \mathrm { C ( \Delta _ { 1 } ; \Delta _ { 6 } ) } } & { \mathrm { C ( \hat { \mathbf { t } } _ { 2 } ; \Delta _ { 1 } ) } } & { \mathrm { , } } & { \mathrm { } \mathrm { C ( \hat { \mathbf { t } } _ { 3 } ; \Delta _ { 1 6 } ) } } & { \mathrm { , } } & { \mathrm { } \mathrm { , } } & { \mathrm { } \mathrm { C ( \hat { \mathbf { t } } _ { 7 } ; \Delta _ { 1 6 } ) } } & { \mathrm { , } } &  \mathrm { } \forall \quad \pm \Gamma ( \Delta _ { 1 6 } ; \hat  \mathbf  t \end{array}
$$

待估信号与已知信号之间的协方差阵为

$$
\mathbf { C } _ { \mathrm { u } } { = } \mathbb { C } ( \zeta _ { \mathsf { P } } \Delta \mathsf { g } _ { 1 } ) { \cdots } { \cdots } \mathbb { C } ( \zeta _ { \mathsf { P } } \Delta \mathsf { g } _ { \mathrm { N } } ) \mathbb { C } ( \zeta _ { \mathsf { P } } \hat { \mathsf { g } } _ { 1 } ) { \cdots } { \cdots } \mathbb { C } ( \zeta _ { \mathsf { P } } \hat { \mathsf { g } } _ { \mathsf { q } } ) \mathbb { C } ( \zeta _ { \mathsf { P } } \eta _ { 1 } ) { \cdots } { \cdots } \mathbb { C } ( \zeta _ { \mathsf { P } } \eta _ { \mathsf { q } } ) ]
$$

运用协方差传播公式， $( 1 3 \cdot 1 6 0 )$ 和 $( 1 3 \cdot 1 6 1 )$ 式中的每一个协方差都可以由扰动位的协方差函数 $\kappa (  { \mathbf { P } } , \mathbf { Q } )$ 导出。若取 $( 1 3 \cdot 1 3 2 )$ 式作为局部地区扰动位的协方差函数，则可求得如下一组推求所需信号协方差的公式：

$$
\mathcal { C } ( \Delta \mathbf { g } _ { \mathsf { P } } \Delta \mathbf { g } _ { \mathsf { Q } } ) = \frac { \mathbf { K } _ { 0 } \mathbf { b } } { ( l ^ { 2 } + \mathbf { b } ^ { 2 } ) ^ { 3 / 2 } }
$$

$$
\small \mathbb { C } ( \Delta \mathbf { g } _ { \mathrm { P } } \hat { \mathbf { \xi } } _ { \mathrm { Q } } ) = \frac { \mathbf { K } _ { \circ } ( \mathbf { X } ^ { \prime } - \mathbf { X } ) } { \gamma ( l ^ { 2 } + \mathbf { b } ^ { 2 } ) ^ { 3 / 2 } }
$$

$$
\mathbb { C } ( \mathbb { \Delta } \mathbf { g } _ { \mathbb { P } } \boldsymbol { \eta } _ { \mathbf { Q } } ) = \frac { \mathbb { K } _ { 0 } ( \mathbf { y } ^ { \prime } - \mathbf { y } ) } { \gamma ( l ^ { 2 } + \mathbf { b } ^ { 2 } ) ^ { 3 / 2 } }
$$

$$
\begin{array} { r l } & { \quad T ( \ell ^ { * } \mathfrak { p } ^ { * } ) ^ { - 1 } } \\ & { \subset \{ \mathfrak { F } _ { \sharp } \mathfrak { s h } _ { \oplus } \big ) _ { - } \frac { \mathbf { K } _ { \oplus } } { \gamma ^ { * } } \{ \frac { 1 } { ( \ell ^ { * } + \mathrm { b } ^ { * } ) ^ { 1 / 2 } } \big [ \mathbf { I } + ( ( \ell ^ { * } + \mathrm { b } ^ { * } ) ^ { 1 / 3 } ) \frac { - ( \mathrm { x } ^ { * } - \mathrm { x } ) ^ { 2 } \mathrm { i } \mathfrak { F } _ { \sharp } \mathrm { b } + 2 ( \ell ^ { * } + \mathrm { b } ^ { * } ) ^ { 1 / 2 } } { ( F ^ { * } + \mathrm { b } ^ { * } ) ^ { 2 / 2 } \mathrm { b } + ( \ell ^ { * } + \mathrm { b } ^ { * } ) ^ { 1 / 3 } } \big ]  } \\ & { \qquad \subset ( \eta _ { \uparrow } \mathfrak { s h } _ { \oplus } ) _ { - } \frac { \mathbf { K } _ { \oplus } } { \gamma ^ { * } } \{ \frac { 1 } { ( \ell ^ { * } + \mathrm { b } ^ { * } ) ^ { 1 / 2 } } \} \frac { 1 } { \mathrm { i } \mathfrak { F } _ { \sharp } + ( \ell ^ { * } + \mathrm { b } ^ { * } ) ^ { 1 / 3 } } \} - \frac { ( \mathrm { y } ^ { * } - \mathrm { y } ) ^ { 2 / 5 } \{ \mathbf { I } + 2 ( \ell ^ { * } + \mathrm { b } ^ { * } ) ^ { 1 / 2 } \} } { ( L ^ { * } + \mathrm { b } ^ { * } ) ^ { 5 / 4 } } \} } \\ &  \subset ( \mathfrak { F } _ { \sharp } \mathfrak { s h } ) = \frac { \mathbf { K } _ { \oplus } } { \gamma ^ { * } } \{ \frac { 1 } { ( \ell ^ { * } + \mathrm { b } ^ { * } ) ^ { 1 / 4 } } \} \frac { 1 } { \mathrm { i } \mathfrak { F } _ { \sharp } + ( \ell ^ { * } + \mathrm { b } ^ { * } ) ^ { 1 / 3 } } - \frac  ( \mathrm { x } ^ { * } - \mathrm { x } ) ( \mathrm { y } ^ { * } - \mathrm { y } ) \{ \mathbf { I } + 2 ( \ell ^ { * } + \mathrm { b } ^ { * } ) ^ { 1 / 2 } \} \} \\ &  \qquad \big ( \ell  \end{array}
$$

式中 $\iota$ 为 $\mathbf { P } ( \mathbf { x } , \mathbf { y } )$ 和 $\mathbf { Q } ( \mathbf { x } ^ { \prime } , \mathbf { y } ^ { \prime } )$ 两点之间的水平距离。在实际计算时， $( \mathbf { x } ^ { \prime } - \mathbf { x } )$ 和 $( \boldsymbol { \mathbf { \rho } } _ { \boldsymbol { \mathbf { y } } ^ { \prime } } - \boldsymbol { \mathbf { y } } )$ 都应取绝对值,以保证协方差阵是正定的。

一些实际数据的计算结果表明,运用这种方法求出的 $\mathrm { \bf P }$ 点的高程异常值只是-种相应于

不明系统的相对高程异常，但将P：和P两点的高程异常值相减,构成高程异常差，其数值与其他方法的结果还是比较接近的。

为了直接计算两点的高程异常差，可以将(13·156)式中的信号协方差Cu由（13·161)式改变成如下的形式：

$$
\begin{array} { r } { \overrightarrow { C } _ { a } ^ { \mathrm { T } } = \left( \begin{array} { c c } { C ( \xi _ { \xi _ { \eta } } , \Delta _ { \xi _ { 1 } } ) - C ( \xi _ { \xi _ { \eta } } , \Delta _ { \xi _ { 1 } } ) } \\ { \vdots } \\ { C ( \xi _ { \eta _ { \xi } } , \Delta _ { \xi _ { 1 } } ) } \\ { C ( \xi _ { \xi _ { \eta } } , \xi _ { 1 } ) - C ( \xi _ { \eta _ { \xi } } , \Delta _ { \xi _ { 1 } } ) } \\ { C ( \xi _ { \eta _ { \xi } } , \xi _ { 1 } ) - C ( \xi _ { \eta _ { \xi } } , \xi _ { 1 } ) } \\ { \vdots } \\ { C ( \xi _ { \eta _ { \xi } } , \xi _ { 1 } ) - C ( \xi _ { \eta _ { \xi } } , \xi _ { 1 } ) } \\ { C ( \xi _ { \eta _ { \xi } } , \eta _ { 1 } ) - C ( \xi _ { \eta _ { \xi } } , \eta _ { 1 } ) } \\ { \vdots } \\ { C ( \xi _ { \eta _ { \xi } } , \eta _ { 1 } ) - \frac { 1 } { \xi _ { \xi } } } \\ { \vdots } \\ { C ( \xi _ { \eta _ { \xi } } , \eta _ { 1 } ) - C ( \xi _ { \eta _ { \xi } } , \eta _ { 1 } ) } \end{array} \right) , } \end{array}
$$

# 13.11顾及与高程的相关性推估空间异常

在前面讲述的简单的重力异常最小二乘推估，在山区的重力场中不能取得好的结果。这是因为，在山区空间重力异常与点的高程有较强的相关性。为了对这种关联有所顾及，就要使用最小二乘配置，即在观测方程中引入两个参数a和 $\mathfrak { h }$ .此时有

$$
l = = 2 + \frac { 1 } { 3 } - b _ { 1 } - \frac { 1 } { 2 } + 1 + n
$$

式中H为观测点的高程。若将 $( 1 3 \cdot \mathrm { ~ i ~ } 6 . 1 )$ 式还原成 $( 1 3 \cdot 1 )$ 式，则有

$$
\mathbf  A ^ { \mathrm { T } } =  { \{ \begin{array} { l l l l } { \vec { t } \vec { \} _ { i } } & { \vec { H } _ { : } } & { \cdots \cdots } & { \vec { t } _ { i } } \\ { \vec { t } \vec { \Sigma } _ { i } } & { \vec { H } _ { : } } & { \cdots \cdots } & { \vec { H } _ { : } } \end{array} \} } }
$$

$$
X = \left( \begin{array} { l } { { \bar { a } } } \\ { { \bar { b } } } \end{array} \right)
$$

这样一来，推求未知点 $\mathrm { P }$ 的空间异常值 $\widetilde { \Delta \mathfrak { { E } } ^ { \prime } \mathfrak { { I } ^ { \prime } } }$ 的步骤是：

1.先由(13.20)式求出参数估值 $\tilde { \Sigma }$ ；

2.按(13.21)式求出未知点的信号估值 $\tilde { \mathrm { S } } _ { \mathrm { f } } ,$ ；

3.再按公式

$$
\widetilde { \Delta \{ g _ { \uparrow } = \mathop { = } _ { i } \pm _ { \downarrow } \flat _ { i } ^ { \intercal } \} } + \widetilde { S _ { i } } ,
$$

求得 $\Omega$ 点的空间异常值，式中 $\operatorname { f } _ { \mathbf { \lambda } ^ { \mathbf { p } } }$ 为 $\mathrm { J } ^ { \mathrm { 2 } }$ 点的高程。

下面以813·9中的例子.用这种方法重新推求4个未知点的空间异常。在表13.5中给出了所有已知点和未知点的高程。

表13.5  

<table><tr><td rowspan=1 colspan=1>点名</td><td rowspan=1 colspan=1>F（km）</td><td rowspan=1 colspan=1>点</td><td rowspan=1 colspan=1>H(kr</td><td rowspan=1 colspan=1>点名</td><td rowspan=1 colspan=1>H(km）</td><td rowspan=1 colspan=1>点名</td><td rowspan=1 colspan=1>H（km）</td></tr><tr><td rowspan=1 colspan=1>A</td><td rowspan=1 colspan=1>0.2183</td><td rowspan=1 colspan=1>C</td><td rowspan=1 colspan=1>6.4893</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.6812</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>0.3144</td></tr><tr><td rowspan=1 colspan=1>B</td><td rowspan=1 colspan=1>0.7654     </td><td rowspan=1 colspan=1>D</td><td rowspan=1 colspan=1>1.0142</td><td rowspan=1 colspan=1>i  2</td><td rowspan=1 colspan=1>0.8435</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>0.5633</td></tr></table>

公式 $( 1 3 \cdot 2 0 )$ 和 $( 1 3 \cdot 2 1 )$ 式中的 $\overline { { \mathsf { C } } }$ 为

$$
\scriptstyle \overline { { C } } = \mathbf { C } _ { n } + \mathbf { C } _ { n n }
$$

其中的信号协方差阵中的信号 $\pmb { \tau }$ 不是重力异常，应该是 $\Delta \mathbf { g } - ( \mathbf { a } + \mathbf { b } \mathbf { H } )$ 。开始时a和b两个参数的数值不知， ${ \bf { C } } _ { \mathfrak { w } }$ 也就不得而知。暂时先用 $\$ 13.9$ 中所用的 $\mathbf { C } _ { 1 }$ 代之。同理， $\mathbf { { C } _ { \mathfrak { s t } } }$ 也暂不改变。若认为已知点重力异常值的中误差为1毫伽，且点之间误差不相关，则噪声协方差阵为

$$
\mathrm { C _ { n n } } = \left[ \begin{array} { c c c c } { 1 } & & & { 0 } \\ & { 1 } & & \\ & & { \ddots } \\ & & & { \ddots } \\ & { 0 } & & \end{array} \right] ~ .
$$

由此通过运算得到

$$
\left. \begin{array} { l } { { \bf a } = - 2 5 . 8 5 5 \div 4 0 } \\ { { \bf b } = 9 0 . 8 4 3 \times 1 0 ^ { - 8 } { \bf s } ^ { - 2 } } \end{array} \right\}
$$

和

$$
\begin{array} { r } {  ( \begin{array} { c } { \mathsf { S } _ { 1 } } \\ { \mathsf { S } _ { 2 } } \\ { \mathsf { S } _ { 3 } } \\ { \mathsf { S } _ { 4 } } \end{array} ) = ( \begin{array} { c } { 0 . 9 3 2 } \\ { 1 . 7 1 1 } \\ { - 0 . 4 9 2 } \\ { 1 . 0 8 8 } \end{array} ) } \end{array}
$$

根据 $( 1 3 \cdot 1 7 0 )$ 所给出的信号值，可求出一个如下的信号协方差函数

$$
\mathsf { C } ( \mathsf { t } ( \mathsf { P } ) , \mathsf { t } ( \mathsf { Q } ) ) = \frac { 1 . 2 } { \lbrack 1 + ( 0 . 0 4 3 l ) ^ { 2 } ] ^ { \frac { 3 } { 2 } / 2 } }
$$

利用它可以求得如下的信号协方差阵：

$$
\mathbf { C _ { n } } = \left[ \begin{array} { l l l l } { 1 . 2 } & { 0 . 9 1 7 } & { 0 . 7 8 4 } & { 0 . 8 2 1 } \\ { 0 . 9 1 7 } & { 1 . 2 } & { 1 . 0 5 4 } & { 0 . 7 2 0 } \\ { 0 . 7 8 4 } & { 1 . 0 5 4 } & { 1 . 2 } & { 0 . 8 9 5 } \\ { 0 . 8 2 1 } & { 0 . 7 2 0 } & { 0 . 8 9 5 } & { 1 . 2 } \end{array} \right]
$$

和

$$
{ \mathsf { C } } _ { \mathrm { * } } = { \left\{ \begin{array} { l l l l } { 1 . 0 6 8 } & { 0 . 8 9 6 } & { 0 . 9 4 0 } & { 1 . 0 9 2 } \\ { 0 . 8 0 9 } & { 0 . 8 5 9 } & { 1 . 0 7 6 } & { 1 . 1 3 2 } \\ { 0 . 9 5 8 } & { 1 . 1 0 5 } & { 1 . 1 4 9 } & { 0 . 8 5 8 } \\ { 1 . 1 0 8 } & { 1 . 1 0 0 } & { 1 . 0 1 5 } & { 0 . 9 0 3 } \end{array} \right. }
$$

再将它们代入 $( 1 3 \cdot 2 0 )$ 和 $( \updownarrow 3 \cdot 2 1 )$ 式，完成运算后得到

$$
\left. { \begin{array} { l } { \mathbf { a } = - 2 6 . 8 2 5 \ { \stackrel { \mathbf { y } \mathbf { y } } { = } } \{ \mathbf { \textmu } \mathbf { \updownarrow } \mathbf { \updownarrow } \mathbf { \updownarrow } } } \\ { \mathbf { b } = 9 2 . 1 8 4 \times 1 0 ^ { - 8 } \mathbf { s } ^ { - 2 } } \end{array}  \right\}
$$

和

$$
 \begin{array} { r }  \{ \begin{array} { r } { \mathbf { S } _ { 1 } } \\ { \mathbf { S } _ { 2 } } \\ { \mathbf { S } _ { 3 } } \\ { \mathbf { S } _ { 4 } } \end{array} \} = ( \begin{array} { r } { 0 . 2 9 8 } \\ { 0 . 4 0 4 } \\ { - 0 . 1 9 3 } \\ { - 0 . 2 6 5 } \end{array} ) \end{array}
$$

将 $( 1 3 \cdot 1 7 2 )$ 式和 $( 1 3 \cdot 1 6 9 )$ 式相比较，差别不大。这说明信号协方差对解算结果影响甚微，因而无必要再对信号协方差函数 $( 1 3 \cdot 1 7 1 )$ 作改善，并作一次新的计算。

最后可以按 $( 1 3 \cdot 1 6 7 )$ 式算出4个未知点的空间异常值：

$$
\left| \Delta \mathbf { g } _ { 1 } \right| = \left( { \small \begin{array} { c c } { 1 } & { 6 8 1 . 2 } \\ { 1 } & { 8 4 3 . 5 } \\ { 1 } & { 3 1 4 . 4 } \\ { 1 } & { 5 6 3 . 3 } \end{array} } \right) \left( { \small \begin{array} { c } { - 2 6 . 8 2 5 } \\ { 9 2 . 1 8 4 } \end{array} } \right) + \left( { \small \begin{array} { c } { 0 . 2 9 8 } \\ { 0 . 4 0 4 } \\ { - 0 . 1 9 3 } \\ { - 0 . 2 6 5 } \end{array} } \right) = \left( { \small \begin{array} { c } { 3 6 . 2 7 } \\ { 5 1 . 8 9 } \\ { 1 . 9 7 } \\ { 2 4 . 8 4 } \end{array} } \right)
$$

将这个结果与13.9的相应结果作比较,可以发现△g的互差达到28毫伽。这说明，在山区推估未知点的空间异常值时，应当顾及与高程的关联，才能使结果较符合于实际情况，低处的空间异常值小，高处的空间异常值大。

# $\ S$ 13.12逐步配置

在实际计算时，最小二乘配置可以分两步或多步完成，这就是所谓的逐步配置。采用这种方法，可以使求逆的矩阵缩小，计算起来方便；同时，在利用新增补的观测值改善原来的结果时不需全部重算。

先讨论分两步完成。此时，观测方程分为两组，即

$$
\begin{array} { r } { l _ { 1 } = \mathbf { A } _ { 1 } \mathbf { X } + \mathbf { t } _ { 1 } + \mathbf { n } _ { 1 } } \\ { l _ { 2 } = \mathbf { A } _ { 2 } \mathbf { X } + \mathbf { t } _ { 2 } + \mathbf { n } _ { 2 } } \end{array}
$$

将它与一般的观测方程相对照;相当于

$$
\left. \begin{array} { c c } { \mathbf { A } = \left( \mathbf { A } _ { 1 } \right) } & { l = \left( \displaystyle l _ { 1 } \right) } \\ { \mathbf { A } _ { 2 } } & { } \\ { \mathbf { t } = \left( \mathbf { t } _ { 1 } \right) } & { \mathbf { \bar { n } } = \left( \mathbf { \bar { n } } _ { 1 } \right) } \\ { \mathbf { \bar { t } } _ { 2 } } & { } \end{array} \right\}
$$

显然，解 $( 1 3 \cdot 2 0 )$ 和 $( 1 3 \cdot 2 1 )$ 式也就要分解为与两组观测量有关的两部份。

现将全协方差阵 $\overline { { \mathrm { { C } } } }$ 写为

$$
\begin{array} { r } { \overrightarrow { \mathbf { C } } = \left[ \begin{array} { l l } { \mathbf { C } _ { 1 1 } } & { \mathbf { C } _ { 1 2 } } \\ { \mathbf { C } _ { 2 1 } } & { \mathbf { C } _ { 2 2 } } \end{array} \right] } \end{array}
$$

其中

$$
\left. \begin{array} { l l } { \mathrm C _ { 1 1 } { = } \mathrm C _ { \iota _ { 1 } \iota _ { 1 } } { + } \mathrm C _ { \mathfrak { n } _ { 1 } \mathfrak { n } _ { 1 } } } & { \mathrm C _ { 2 2 } { = } \mathrm C _ { \iota _ { 2 } \iota _ { 2 } } { + } \mathrm C _ { \mathfrak { n } _ { 2 } \mathfrak { n } _ { 2 } } } \\ { \mathrm C _ { 1 2 } { = } \mathrm C _ { 2 1 } ^ { \mathrm T } { = } \mathrm C _ { \mathfrak { n } _ { 1 } \mathfrak { n } _ { 2 } } { + } \mathrm C _ { \mathfrak { n } _ { 1 } \mathfrak { n } _ { 2 } } } & { } \end{array} \right\}
$$

同时， $\mathbf { \mathbf { { C } _ { \mathbf { { s t } } } } }$ 可写为

$$
\begin{array} { r l } { \mathbf { C _ { s t } } = ( \mathbf { C _ { 1 } } } & { { } \mathbf { C _ { 2 } } ) } \end{array}
$$

其中 $\mathrm { C } _ { 1 }$ 是信号 $\boldsymbol { \mathsf { s } }$ 与 $\mathbf { t } _ { 1 }$ 的协方差阵， $\mathbf { { C } } _ { 2 }$ 是信号 $\boldsymbol { \mathsf { s } }$ 与 $\mathbf { t _ { 2 } }$ 的协方差阵。

若将 $\overline { { \mathtt { C } } }$ 的逆矩阵写为

$$
\begin{array} { r } { \overline { { \mathbf { C } } } ^ { - 1 } = \left[ \begin{array} { l l } { \mathbf { B } _ { 1 1 } } & { \mathbf { B } _ { 1 2 } } \\ { \mathbf { B } _ { 2 1 } } & { \mathbf { B } _ { 2 2 } } \end{array} \right] } \end{array}
$$

则依据矩阵求逆的理论有

$$
\begin{array} { r l } & { \mathrm { B } _ { 2 2 } = ( C _ { 2 2 } - C _ { 3 1 } \mathrm { C } _ { 1 1 } ^ { - 1 } \mathrm { C } _ { 1 2 } ) ^ { - 1 } } \\ & { \mathrm { B } _ { 1 2 } = - \mathrm { C } _ { 1 1 } ^ { - 1 } \mathrm { C } _ { 1 2 } \mathrm { B } _ { 2 2 } , \mathrm { B } _ { 2 1 } = - \mathrm { B } _ { 2 2 } \mathrm { C } _ { 2 1 } \mathrm { C } _ { 1 1 } ^ { - 1 } } \\ & { \mathrm { B } _ { 1 1 } = \mathrm { C } _ { 1 1 } ^ { - 1 } - \mathrm { C } _ { 1 1 } ^ { - 1 } \mathrm { C } _ { 1 2 } \mathrm { B } _ { 2 1 } = \mathrm { C } _ { 1 1 } ^ { - 1 } + \mathrm { C } _ { 1 1 } ^ { - 1 } \mathrm { C } _ { 1 2 } \mathrm { B } _ { 2 2 } \mathrm { C } _ { 2 1 } \mathrm { C } _ { 1 1 } ^ { - 1 } . } \end{array}
$$

因此可以求得

$$
\begin{array} { r l } & { \mathbf { A } ^ { \mathrm { T } } \overline { { \mathbf { C } } } ^ { - 1 } \mathbf { A } = ( \mathbf { A } _ { 1 } ^ { \mathrm { T } } \mathbf { A } _ { 2 } ^ { \mathrm { T } } ) \left( \begin{array} { l l } { \mathbf { B } _ { 1 1 } } & { \mathbf { B } _ { 1 2 } } \\ { \mathbf { B } _ { 2 1 } } & { \mathbf { B } _ { 2 2 } } \end{array} \right) \left( \mathbf { A } _ { 1 } \right) } \\ & { \qquad = \mathbf { A } _ { 1 } ^ { \mathrm { T } } \mathbf { B } _ { 1 1 } \mathbf { A } _ { 1 } + \mathbf { A } _ { 2 } ^ { \mathrm { T } } \mathbf { B } _ { 2 1 } \mathbf { A } _ { 1 } + \mathbf { A } _ { 1 } ^ { \mathrm { T } } \mathbf { B } _ { 1 2 } \mathbf { A } _ { 2 } + \mathbf { A } _ { 2 } ^ { \mathrm { T } } \mathbf { B } _ { 2 2 } \mathbf { A } _ { 2 } } \end{array}
$$

将 $( 1 3 \cdot 1 7 9 )$ 式代入，则得

$\mathrm { A ^ { 7 } \mathrm { \overline { { C } } ^ { - 1 } \mathrm { A } = A _ { 1 } ^ { T } C _ { 1 1 } ^ { - 1 } A _ { 1 } + A _ { 1 } ^ { T } C _ { 1 1 } ^ { - 1 } C _ { 1 2 } B _ { 2 2 } C _ { 2 1 } C _ { 1 1 } ^ { - 1 } A _ { 1 } - A _ { 2 } ^ { T } B _ { 2 2 } C _ { - 1 } C _ { 1 1 } ^ { - 1 } A _ { 1 } - A _ { 1 } ^ { T } C _ { 1 1 } ^ { - 1 } C _ { 1 2 } B _ { 2 2 } A _ { 2 } + A _ { 2 } ^ { T } C _ { 2 2 } ^ { - 1 } A _ { 1 } ^ { T } C _ { 1 2 } ^ { - 1 } A _ { 1 } } }$ 将右端后四项合并后得到

令

$$
\begin{array} { r } { \mathbf { A } ^ { \mathrm { T } } \widetilde { \mathbf { C } } ^ { - 1 } \mathbf { A } = \mathbf { A } _ { 1 } ^ { \mathrm { T } } \mathbf { C } _ { 1 1 } ^ { - 1 } \mathbf { A } _ { 1 } + ( \mathbf { A } _ { 2 } ^ { \mathrm { T } } - \mathbf { A } _ { 1 } ^ { \mathrm { T } } \mathbf { C } _ { 1 1 } ^ { - 1 } \mathbf { C } _ { 1 2 } ) \mathbf { B } _ { 2 2 } ( \mathbf { A } _ { 2 } - \mathbf { C } _ { 2 1 } \mathbf { C } _ { 1 1 } ^ { - 1 } \mathbf { A } _ { 1 } ) } \end{array}
$$

$$
\begin{array} { c } { { \overline { { \mathrm { A _ { 2 } } } } { = } \mathrm { A _ { 2 } } - \mathrm { C _ { 2 1 } } \mathrm { C _ { 1 1 } ^ { - 1 } } \mathrm { A _ { 1 } } } } \\ { { \mathrm { P _ { \mathrm { \ell } } = \mathrm { A _ { \mathrm { 1 } } ^ { \mathrm { T } } C _ { 1 1 } ^ { - 1 } } \mathrm { A _ { \mathrm { 1 } } } } } } \end{array}
$$

则得

$$
\mathsf { A } ^ { \mathrm { T } } \overline { { \mathsf { C } } } ^ { - 1 } \mathbf { A } { = } \mathbf { P } _ { 1 } { + } \overline { { \mathsf { A } } } _ { 2 } ^ { \mathrm { T } } \mathbf { B } _ { 2 : } \overline { { \mathsf { A } } } _ { 2 }
$$

其逆矩阵为

$$
( \mathbf { A } ^ { \mathsf { T } } \overline { { \mathbf { C } } } ^ { - 1 } \mathbf { A } ) ^ { - 1 } = \mathbf { P } _ { 1 } ^ { - 1 } \overline { { \mathbf { A } } } _ { z } ^ { \mathsf { T } } ( \mathbf { B } _ { 2 z } ^ { - 1 } + \overline { { \mathbf { A } } } _ { z } \mathbf { P } _ { 1 } ^ { - 1 } \overline { { \mathbf { A } } } _ { z } ^ { \mathsf { T } } ) ^ { - 1 } \overline { { \mathbf { A } } } _ { 2 } \mathbf { P } _ { 1 } ^ { - 1 }
$$

再令

$$
\overline { { \dot { \mathrm { C } } } } _ { 2 2 } = \mathrm { B } _ { z 2 } ^ { - 1 } + \overline { { \mathrm { A } } } _ { 2 } \mathrm { P } _ { 1 } ^ { - 1 } \overline { { \mathrm { A } } } _ { 2 } ^ { - 1 }
$$

则 $( 1 3 \cdot 1 8 3 )$ 式又可写为

另有

$$
( \bar { \mathbf { A } } ^ { \top } \widetilde { \mathbf { C } } ^ { - 1 } \bar { \mathbf { A } } ) ^ { - 1 } { = } \mathbf { P } _ { 1 } ^ { - 1 } { - } \mathbf { P } _ { 1 } ^ { - \top } \overline { { \bar { \mathbf { A } } _ { 2 } ^ { \top } \bar { \mathbf { C } } _ { 2 2 } } } ^ { 1 } \overline { { \bar { \mathbf { A } } _ { 2 } } } \mathbf { P } _ { 1 } ^ { - 1 }
$$

$$
\begin{array} { r l } & { \mathbf { A } ^ { \top } \overline { { \mathbf { C } } } ^ { - 1 } \boldsymbol { l } = ( \mathbf { A } _ { 1 } ^ { \top } \quad \mathbf { A } _ { 2 } ^ { \top } ) \left[ \mathbf { B } _ { 1 1 } \quad \mathbf { B } _ { 1 2 } \right] \left[ \boldsymbol { l } _ { 1 } \right] } \\ & { \qquad = \mathbf { A } _ { 1 } ^ { \top } \mathbf { B } _ { 1 1 } \boldsymbol { l } _ { 1 } + \mathbf { A } _ { 1 } ^ { \top } \mathbf { B } _ { 1 2 } \boldsymbol { l } _ { 2 } + \mathbf { A } _ { 2 } ^ { \top } \mathbf { B } _ { 2 1 } \boldsymbol { l } _ { 1 } + \mathbf { A } _ { 2 } ^ { \top } \mathbf { B } _ { 2 2 } \boldsymbol { l } _ { 2 } } \end{array}
$$

将(13·179)式代入，并顾及(13·180)式,可以求得

$$
\mathrm { A } ^ { \mathrm { r } } \overline { \mathbb { C } } ^ { - 1 } \boldsymbol { l } = \mathrm { A } _ { 1 } ^ { \mathrm { r } } \mathbb { C } _ { 1 1 } ^ { - 1 } \boldsymbol { l } _ { 1 } + \overline { { \mathrm { A } } } _ { 2 } ^ { \mathrm { r } } \mathrm { B } _ { 2 : 2 } ( \boldsymbol { l } _ { 2 } - \mathbb { C } _ { : 1 } \mathbb { C } _ { 1 1 } ^ { - 1 } \boldsymbol { l } _ { 1 } )
$$

将(13·185)式和(13·186)式相乘，就得参数的估值文,即

$$
\begin{array} { r } { \tilde { \mathbf { X } } = \mathrm { P } _ { 1 } ^ { - 1 } \mathbf { A } _ { 1 } ^ { T } \mathbf { C } _ { 1 1 } ^ { - 1 } Z _ { 1 } - \mathrm { P } _ { 1 } ^ { - 1 } \overline { { \mathbf { A } _ { 2 } ^ { T } } } \overline { { \mathbf { C } _ { 2 2 } ^ { - 1 } } } \overline { { \mathbf { A } _ { 2 } } } \mathrm { P } _ { 1 } ^ { - 1 } \mathbf { A } _ { 1 } ^ { \top } \mathbf { C } _ { 1 1 } ^ { - 1 } \boldsymbol { l } _ { 1 } + ( \mathrm { P } _ { 1 } ^ { - 1 } - \mathrm { P } _ { 1 } ^ { - 1 } \overline { { \mathbf { A } _ { 2 } ^ { T } } } \overline { { \mathbf { C } _ { 2 2 } } } \overline { { \mathbf { A } _ { 2 } } } \mathrm { P } _ { 1 } ^ { - 1 } ) \overline { { \mathbf { A } _ { 2 } ^ { T } } } \mathrm { B } _ { 2 2 } ( \boldsymbol { l } _ { 2 } - \mathrm { C } _ { 2 2 } \overline { { \mathbf { A } _ { 2 } ^ { T } } } \boldsymbol { l } _ { 1 } ) . } \end{array}
$$

右边的第一项就是只利用第一组观测向量l求得的参数估值，用X表示之。显然，后两项是由于增加了第二组观测向量l使参数估值产生的改正。因为

$$
\begin{array} { r l } & { ( \mathrm { P } _ { 1 } ^ { - 1 } - \mathrm { P } _ { 1 } ^ { - 1 } \overline { { \mathrm { A } } } _ { 2 } ^ { \top } \overline { { \mathrm { C } } } _ { 2 2 } \overline { { \mathrm { A } } } _ { 2 } \mathrm { P } _ { 1 } ^ { - 1 } ) \overline { { \mathrm { A } } } _ { 2 } ^ { \top } \mathrm { B } _ { 2 2 } = \mathrm { P } _ { 1 } ^ { - 1 } \overline { { \mathrm { A } } } _ { 2 } ^ { \top } ( \mathrm { I } - \overline { { \mathrm { C } } } _ { : 2 } ^ { - 1 } \overline { { \mathrm { A } } } _ { 2 } \mathrm { P } _ { 1 } ^ { - 1 } \overline { { \mathrm { A } } } _ { 2 } ^ { \top } ) \mathrm { B } _ { 2 2 } } \\ & { \qquad = \mathrm { P } _ { 1 } ^ { - 1 } \overline { { \mathrm { A } } } _ { 2 } ^ { \top } \overline { { \mathrm { C } } } _ { 2 2 } ^ { - 1 } ( \overline { { \mathrm { C } } } _ { : 2 } - \overline { { \mathrm { A } } } _ { 2 } \mathrm { P } _ { 1 } ^ { - 1 } \overline { { \mathrm { A } } } _ { 2 } ^ { \top } ) \mathrm { B } _ { \ z _ { 2 } } } \end{array}
$$

而由(13·184)式可得

$$
( \overline { { \mathbf { C } } } _ { 2 2 } - \overline { { \mathbf { A } } } _ { 2 } \mathbf { P } _ { 1 } ^ { - 1 } \overline { { \mathbf { A } } } _ { 2 } ^ { \mathrm { T } } ) \mathbf { B } _ { 2 2 } = = \mathbf { I }
$$

考虑到这些，参数估值公式可由 $( 1 3 \cdot 1 8 7 )$ 式改写为

$$
\widetilde { \mathbf { X } } = \widetilde { \mathbf { X } } _ { 1 } + \mathbf { P } _ { 1 } ^ { - 1 } \overline { { \mathbf { A } } } _ { 2 } ^ { \mathsf { T } } \overline { { \mathbf { C } } } _ { 2 2 } ^ { - 1 } ( \boldsymbol { l } _ { 2 } - \mathbf { C } _ { 2 1 } \mathbf { C } _ { 1 1 } ^ { - 1 } \boldsymbol { l } _ { 1 } + \overline { { \mathbf { A } } } _ { 2 } \widetilde { \mathbf { X } } _ { 1 } )
$$

再改化信号推估公式 $( 1 3 \cdot 2 1 )$ 。设

$$
\widetilde { \boldsymbol { Z } } = \boldsymbol { l } - \mathbf { A } \widetilde { \mathbf { X } }
$$

则

$$
\widetilde { \boldsymbol { \mathrm { Z } } } = \left[ \begin{array} { l } { \widetilde { \boldsymbol { Z } } _ { 1 } } \\ { \widetilde { \boldsymbol { Z } } _ { 2 } } \end{array} \right] = \left[ \begin{array} { l } { \boldsymbol { l } _ { 1 } - \mathbf { A } _ { 1 } \widetilde { \mathbf { X } } } \\ { \boldsymbol { l } _ { 2 } - \mathbf { A } _ { 2 } \widetilde { \mathbf { X } } } \end{array} \right] .
$$

由 $( 1 3 \cdot 2 1 )$ 式可得

$$
\begin{array} { r l } & { \tilde { \mathbf { S } } = ( \mathbf { C } _ { 1 } \quad \mathbf { C } _ { 2 } ) \left( \mathbf { B } _ { 1 1 } \quad \mathbf { B } _ { 1 2 } \right) \left( \begin{array} { l } { \tilde { Z } _ { 1 } } \\ { } \\ { \tilde { B } _ { 2 1 } \quad \mathrm { B } _ { 2 2 } } \end{array} \right) } \\ & { \quad = ( \mathbf { C } _ { 1 } \mathbf { B } _ { 1 1 } + \mathbf { C } _ { 2 } \mathbf { B } _ { 2 1 } ) \tilde { Z } _ { 1 } + ( \mathbf { C } _ { 1 } \mathbf { B } _ { 1 2 } + \mathbf { C } _ { 2 } \mathbf { B } _ { 2 2 } ) \tilde { Z } _ { 2 } } \end{array}
$$

再把 $( 1 3 \cdot 1 7 9 )$ 式代入，则得

$$
\begin{array} { r } { \tilde { \mathrm { S } } = \mathrm { C } _ { 1 } \mathrm { C } _ { 1 1 } ^ { - 1 } \hat { \mathrm { Z } } _ { 1 } + ( \mathrm { C } _ { 2 2 } - \mathrm { C } _ { 1 } \mathrm { C } _ { 1 1 } ^ { - 1 } \mathrm { C } _ { 1 2 } ) \mathrm { B } _ { 2 2 } ( \tilde { \mathrm { Z } } _ { 2 } - \mathrm { C } _ { 2 1 } \mathrm { C } _ { 1 1 } ^ { - 1 } \tilde { \mathrm { Z } } _ { 1 } ) } \end{array}
$$

由 $( 1 3 \cdot 1 9 0 )$ 式可以写出

$$
\widetilde { Z } _ { 1 } = \widetilde { l } _ { 1 } - \mathbf { A } _ { 1 } \widetilde { \mathbf { X } _ { 1 } } - \mathbf { A } _ { 1 } ( \widetilde { \mathbf { X } } - \widetilde { \mathbf { X } _ { 1 } } )
$$

将它代入前式，得到

$$
\tilde { \mathbf { S } } = \mathbf { C } _ { 1 } \mathbf { C } _ { 1 1 } ^ { - 1 } ( l _ { 1 } - \mathbf { A } _ { 1 } \widetilde { \mathbf { X } } _ { 1 } ) - \mathbf { C } _ { 1 } \mathbf { C } _ { 1 1 } ^ { - 1 } \mathbf { A } _ { 1 } ( \widetilde { \mathbf { X } } - \widetilde { \mathbf { X } } _ { 1 } ) + ( \mathbf { C } _ { 2 } - \mathbf { C } _ { 1 } \mathbf { C } _ { 1 1 } ^ { - 1 } \mathbf { C } _ { 1 2 } ) \mathbf { B } _ { \geq 2 } ( \widetilde { Z } _ { 2 } - \mathbf { C } _ { 2 1 } \mathbf { C } _ { 1 1 } ^ { - 1 } \widetilde { Z } _ { 1 } ) \phantom { \textbf { C } _ { 1 } } ,
$$

右端第一项就是只利用第一组观测向量 $l _ { \mathrm { 1 } }$ 时所求得的信号估值 $\tilde { S } _ { \imath }$ ，即

$$
\widetilde { \mathbf { S } } _ { 1 } { = } \mathbf { C } _ { 1 } \mathbf { C } _ { 1 1 } ^ { - 1 } ( \boldsymbol { l } _ { 1 } { - } \mathbf { A } _ { 1 } \widetilde { \mathbf { X } } _ { 1 } )
$$

而后两项是由于增加了第二组观测向量 $l _ { \textrm { 2 } }$ 使信号估值产生的改正。由 $( 1 3 ~ \cdot ~ 1 9 0 )$ 式可得

$$
\tilde { \mathrm { Z } } _ { 2 } - \mathrm { C } _ { 2 1 } \mathrm { C } _ { 1 1 } ^ { - 1 } \tilde { \mathrm { Z } } _ { 1 } = l _ { 2 } - \mathrm { A } _ { 2 } \tilde { \mathrm { X } } - \mathrm { C } _ { 2 1 } \mathrm { C } _ { 1 1 } ^ { - 1 } ( l _ { 1 } - \mathrm { A } _ { 1 } \tilde { \mathrm { X } } )
$$

顾及到 $( 1 3 \cdot 1 8 0 )$ 式，又可写为

$$
\begin{array} { r l } & { \widetilde { Z } _ { 2 } - \mathrm { C } _ { 2 1 } \mathrm { C } _ { 1 1 } ^ { - 1 } \widetilde { Z } _ { 1 } = l _ { 2 } - \mathrm { C } _ { 2 1 } \mathrm { C } _ { 1 1 } ^ { - 1 } l _ { 1 } - \overline { { \mathrm { A } } } _ { 2 } \widetilde { \mathrm { X } } } \\ & { \qquad = l _ { 2 } - \mathrm { C } _ { 2 1 } \mathrm { C } _ { 1 1 } ^ { - 1 } l _ { 1 } - \overline { { \mathrm { A } } } _ { 2 } \widetilde { \mathrm { X } } _ { 1 } - \mathrm { A } _ { 2 } ( \widetilde { \mathrm { X } } - \widetilde { \mathrm { X } } _ { 1 } ) } \end{array}
$$

将它和 $( 1 3 \cdot 1 9 2 )$ 式一起代入 $( 1 3 \cdot 1 9 1 )$ 式，则得

$$
\begin{array} { r l } & { \widetilde { \mathsf { S } } { = } \widetilde { \mathsf { S } } _ { 1 } { - } \mathrm { C } _ { 1 } \mathrm { C } _ { 1 1 } ^ { - 1 } \mathrm { A } _ { 1 } ( \widetilde { \mathbf { X } } { - } \widetilde { \mathbf { X } _ { 1 } } ) { - } ( \mathrm { C } _ { 2 } { - } \mathrm { C } _ { 1 } \mathrm { C } _ { 1 1 } ^ { - 1 } \mathrm { C } _ { 1 2 } ) \mathrm { B } _ { 2 2 } \overline { { \mathrm { A } } } _ { 2 } ( \widetilde { \mathbf { X } } { - } \widetilde { \mathbf { X } _ { 1 } } ) } \\ & { \qquad { + } ( \mathrm { C } _ { 2 } { - } \mathrm { C } _ { 1 } \mathrm { C } _ { 1 1 } ^ { - 1 } \mathrm { C } _ { 1 2 } ) \mathrm { B } _ { 2 2 } ( \boldsymbol { \mathit { l } } _ { 2 } { - } \mathrm { C } _ { 2 1 } \mathrm { C } _ { 1 1 } ^ { - 1 } \boldsymbol { \mathit { l } } _ { 1 } { - } \overline { { \mathrm { A } } } _ { 2 } \widetilde { \mathbf { X } _ { 1 } } ) } \end{array}
$$

将 $( 1 3 \cdot 1 8 8 )$ 式求得的 $\widetilde { \mathbf X } - \widetilde { \mathbf X } _ { 1 }$ 代入，得到

$$
\begin{array} { r l } & { \widetilde { \mathrm { S } } { = } \widetilde { \mathrm { S } } _ { 1 } { + } \widetilde { \mathrm { [ } } ( \mathrm { C } _ { 2 } { - } \mathrm { C } _ { 1 } \mathrm { C } _ { 1 1 } ^ { - 1 } \mathrm { C } _ { 1 2 } ) \mathrm { B } _ { { \geq } 2 } ( \mathrm { I } { - } \overline { { \mathrm { A } } } _ { 2 } \mathrm { P } _ { 1 } ^ { - 1 } \overline { { \mathrm { A } } } _ { 2 } ^ { \top } \widetilde { \mathrm { C } } _ { { 2 } 2 } ^ { - 1 } ) } \\ & { \qquad { \mathrm { - } } \mathrm { C } _ { 1 } \mathrm { C } _ { 1 1 } ^ { - 1 } \mathrm { A } _ { 1 } \mathrm { P } _ { 1 } ^ { - 1 } \overline { { \mathrm { A } } } _ { 2 } ^ { \top } \mathrm { C } _ { { \geq } 2 } ^ { - 1 } \mathrm { ] } ( \boldsymbol { l } _ { { \div } } { - } \mathrm { C } _ { { \div } 1 } \mathrm { C } _ { 1 1 } ^ { - 1 } \boldsymbol { l } _ { { \downarrow } } { - } \overline { { \mathrm { A } } } _ { 2 } \widetilde { \mathrm { X } } _ { 1 } ) } \end{array}
$$

该式右端第二项方括号中的因子可以改化为

$$
( \mathsf C _ { 2 } - \mathsf C _ { 1 } \mathsf C _ { 1 1 } ^ { - 1 } \mathsf C _ { 1 2 } ) \mathbb B _ { 2 2 } ( \overline { { \mathsf C } } _ { 2 2 } - \overline { { \mathsf A } } _ { 2 } \mathsf P _ { 1 } ^ { - 1 } \overline { { \mathsf A } } _ { 2 } ^ { \div } ) \overline { { \mathsf C } } _ { 2 2 } ^ { - 1 } - \mathsf C _ { 1 } \mathsf C _ { 1 1 } ^ { - 1 } \mathsf A _ { 1 } \mathsf P _ { 1 } ^ { - 1 } \overline { { \mathsf A } } _ { 2 } ^ { \top } \overline { { \mathsf C } } _ { 2 2 } ^ { - 1 }
$$

再考虑到

$$
\mathbf { B } _ { 2 : 2 } ( \overline { { \mathbf { C } } } _ { 2 : 2 } - \overline { { \mathbf { A } } } _ { 2 } \mathbf { P } _ { 1 } ^ { - 1 } \overline { { \mathbf { A } } } _ { 2 } ^ { \mathrm { T } } ) = \mathbf { I }
$$

又可变为

$$
( \mathbf { C } _ { 2 } - \mathbf { C } _ { 1 } \mathbf { C } _ { 1 1 } ^ { - 1 } \mathbf { C } _ { 1 2 } - \mathbf { C } _ { 1 } \mathbf { C } _ { 1 1 } ^ { - 1 } \mathbf { A } _ { 1 } \mathbf { P } _ { 1 } ^ { - 1 } \overline { { \mathbf { A } } } _ { 2 } ^ { \top } ) \overline { { \mathbf { C } } } _ { 2 2 } ^ { - 1 }
$$

这样一来， $( 1 3 \cdot 1 9 3 )$ 式可写为

$$
\tilde { \bar { \mathbf { S } } } = \tilde { \bar { \mathbf { S } } } _ { 1 } + ( \mathrm { C } _ { 2 } - \mathrm { C } _ { 1 } \mathrm { C } _ { 1 1 } ^ { - 1 } \mathrm { C } _ { 1 2 } - \mathrm { C } _ { 1 } \mathrm { C } _ { 1 1 } ^ { - 1 } \mathrm { A } _ { 1 } \mathrm { P } _ { 1 } ^ { - 1 } \overline { { \bar { \mathbf { A } } _ { 2 } ^ { \top } } } ) \overline { { \mathrm { C } } } _ { 2 2 } ^ { - 1 } ( \mathit { l } _ { 2 } - \mathrm { C } _ { 2 1 } \mathrm { C } _ { 1 1 } ^ { - 1 } \mathit { l } _ { 1 } - \overline { { \mathbf { A } } } _ { 2 } \widetilde { \mathrm { X } } _ { 1 } )
$$

这就是分两步配置时，信号估值的计算公式。

显然，所有的精度估算公式也要相应的变换。将(13·185)式代入(13·31)式，得到

$$
\mathrm { E } _ { \mathrm { x } \mathrm { x } } { = } \mathrm { P } _ { 1 } ^ { - 1 } { - } \mathrm { P } _ { 1 } ^ { - 1 } \overline { { \mathrm { A } _ { 2 } ^ { \prime } \mathrm { C } _ { 2 2 } ^ { - 1 } \mathrm { A } _ { 2 } \mathrm { P } _ { 1 } ^ { - 1 } } }
$$

从 $( 1 3 \cdot 1 8 1 )$ 式知

$$
{ \bf P } _ { 1 } ^ { - 1 } = ( { \bf A } _ { 1 } ^ { \mathrm { T } } { \bf C } _ { 1 1 } ^ { - 1 } { \bf A } _ { 1 } ) ^ { - 1 }
$$

将它与(13·31)式对照可知，它就是只利用观测向量l时所求得的参数估值X的误差协方差阵,用Exx·,表示之。代入(13·195)式则得,参数估值义的误差协方差阵的计算公式为

$$
\mathbf { E } _ { \mathbf { x } \mathbf { x } } { = } \mathbf { E } _ { \mathbf { x } \mathbf { x } \cdot \mathbf { \mu } _ { 1 } } { - } \mathbf { P } _ { 1 } ^ { - 1 } \overline { { \mathbf { A } } } _ { 2 } ^ { \top } \overline { { \mathbf { C } } } _ { 2 2 } ^ { - 1 } \overline { { \mathbf { A } } } _ { 2 } \mathbf { P } _ { 1 } ^ { - 1 }
$$

因为

$$
\begin{array} { r l } & { \mathbb { A } ^ { \mathrm { T } } \overline { { \mathbb { C } } } ^ { - 1 } \mathbb { C } _ { \mathfrak { u } } = ( \mathbf { A } _ { 1 } ^ { \mathrm { T } } \mathbf { A } _ { 2 } ^ { \mathrm { T } } ) \left[ \begin{array} { l l } { \mathbf { B } _ { 1 1 } } & { \mathbf { B } _ { 1 2 } } \\ { \mathbf { B } _ { 2 1 } } & { \mathbf { B } _ { 2 2 } } \end{array} \right] \left[ \mathbf { C } _ { 1 } ^ { \mathrm { T } } \right] } \\ & { \qquad = \mathbf { A } _ { 1 } ^ { \mathrm { T } } \mathbf { C } _ { 1 1 } ^ { - 1 } \mathbf { C } _ { 1 } ^ { \mathrm { T } } + \overline { { \mathbf { A } } } _ { 2 } ^ { \mathrm { T } } \mathbf { B } _ { 2 2 } ( \mathbf { C } _ { 2 } ^ { \mathrm { T } } - \mathbb { C } _ { 2 1 } \mathbf { C } _ { 1 1 } ^ { - 1 } \mathbf { C } _ { 1 } ^ { \mathrm { T } } ) } \end{array}
$$

依据 $( 1 3 \cdot 4 2 )$ 式，将 $( 1 3 \cdot 1 8 5 )$ 式和 $( 1 3 \cdot 1 9 7 )$ 式相乘可得

$$
\begin{array} { r l } & { \mathrm { E } _ { \mathrm { X s } } = - ( \mathrm { P } _ { 1 } ^ { - 1 } - \mathrm { P } _ { 1 } ^ { - 1 } \overline { { \mathrm { A } } } _ { 2 } ^ { \top } \overline { { \mathrm { C } } } _ { 2 ^ { 2 } } ^ { - 1 } \overline { { \mathrm { A } } } _ { 2 } \mathrm { P } _ { 1 } ^ { - 1 } ) \left[ { \mathrm { A } } _ { 1 } ^ { \top } { \mathrm { C } } _ { 1 1 } ^ { - 1 } { \mathrm { C } } _ { 1 } ^ { \top } + \overline { { \mathrm { A } } } _ { 2 } ^ { \top } { \mathrm { B } } _ { 2 2 } ( { \mathrm { C } } _ { 2 } ^ { \top } - { \mathrm { C } } _ { 2 1 } { \mathrm { C } } _ { 1 1 } ^ { - 1 } { \mathrm { C } } _ { 1 } ^ { \top } ) \right] } \\ & { \quad = - \mathrm { P } _ { 1 } ^ { - 1 } { \mathrm { A } } _ { 1 } ^ { \top } { \mathrm { C } } _ { 1 1 } ^ { - 1 } { \mathrm { C } } _ { 1 } ^ { \top } + \mathrm { P } _ { 1 } ^ { - 1 } \overline { { \mathrm { A } } } _ { 2 } ^ { \top } \overline { { \mathrm { C } } } _ { 2 2 } ^ { - 1 } \overline { { \mathrm { A } } } _ { 2 } \mathrm { P } _ { 1 } ^ { - 1 } { \mathrm { A } } _ { 1 } ^ { \top } { \mathrm { C } } _ { 1 1 } ^ { - 1 } { \mathrm { C } } _ { 1 } ^ { \top } } \\ & { \quad \quad - ( \mathrm { P } _ { 1 } ^ { - 1 } - \mathrm { P } _ { 1 } ^ { - 1 } \overline { { \mathrm { A } } } _ { 2 } ^ { \top } \overline { { \mathrm { C } } } _ { 2 2 } ^ { - 1 } \overline { { \mathrm { A } } } _ { 2 } \mathrm { P } _ { 1 } ^ { - 1 } ) \overline { { \mathrm { A } } } _ { 2 } ^ { \top } { \mathrm { B } } _ { 2 2 } ( { \mathrm { C } } _ { 2 } ^ { \top } - { \mathrm { C } } _ { 2 1 } { \mathrm { C } } _ { 1 1 } ^ { - 1 } { \mathrm { C } } _ { 1 } ^ { \top } ) } \end{array}
$$

因为

$$
( \mathrm { P } _ { 1 } ^ { - 1 } + \mathrm { P } _ { 1 } ^ { - 1 } \overline { { \mathrm { A } } } _ { 2 } ^ { \mathrm { T } } \overline { { \mathrm { C } } } _ { 2 2 } ^ { - 1 } \overline { { \mathrm { A } } } _ { 2 } \mathrm { P } _ { 1 } ^ { - 1 } ) \overline { { \mathrm { A } } } _ { 2 } ^ { \mathrm { T } } \mathrm { B } _ { 2 2 } = \mathrm { P } _ { 1 } ^ { - 1 } \overline { { \mathrm { A } } } _ { 2 } ^ { \mathrm { T } } \overline { { \mathrm { C } } } _ { 2 2 } ^ { - 1 }
$$

用它变换 $( 1 3 \cdot 1 9 8 )$ 式右端的第三项，然后与第二项合并，则得

$$
\mathbf { E } _ { \mathrm { x s } } = - \mathbf { P } _ { 1 } ^ { - 1 } \mathbf { A } _ { 1 } ^ { \top } \mathbf { C } _ { 1 1 } ^ { - 1 } \mathbf { C } _ { 1 } ^ { \top } - \mathbf { P } _ { 1 } ^ { - 1 } \mathbf { \overline { { A } } } _ { 2 } ^ { \top } \mathbf { \overline { { C } } } _ { 2 2 } ^ { - 1 } ( \mathbf { C } _ { 2 } ^ { \top } - \mathbf { C } _ { 2 1 } \mathbf { C } _ { 1 1 } ^ { - 1 } \mathbf { C } _ { 1 } ^ { \top } - \mathbf { \overline { { A } } } _ { 2 } \mathbf { P } _ { 1 } ^ { - 1 } \mathbf { A } _ { 1 } ^ { \top } \mathbf { C } _ { 1 1 } ^ { - 1 } \mathbf { C } _ { 1 } ^ { \top } )
$$

令

$$
\begin{array} { r } { \overline { { \mathbf { C } } } _ { 2 } ^ { \mathrm { T } } = \dot { \mathbf { C } } _ { 2 } ^ { \mathrm { T } } - \mathbf { C } _ { 2 1 } \mathbf { C } _ { 1 1 } ^ { - 1 } \mathbf { C } _ { 1 } ^ { \mathrm { T } } - \overline { { \mathbf { A } } } _ { 2 } \mathbf { P } _ { 1 } ^ { - 1 } \mathbf { A } _ { 1 } ^ { \mathrm { T } } \dot { \mathbf { C } } _ { 1 1 } ^ { - 1 } \mathbf { C } _ { 1 } ^ { \mathrm { T } } } \end{array}
$$

得到

$$
\mathbf { E } _ { \mathbf { x } s } = - \mathbf { P } _ { 1 } ^ { - 1 } \mathbf { A } _ { 1 } ^ { \mathrm { T } } \mathbf { C } _ { 1 1 } ^ { - 1 } \mathbf { C } _ { 1 } ^ { \mathrm { T } } - \mathbf { P } _ { 1 } ^ { - 1 } \mathbf { \overline { { A } } } _ { 2 } ^ { \mathrm { T } } \mathbf { \overline { { C } } } _ { 2 2 } ^ { - 1 } \mathbf { \overline { { C } } } _ { 2 } ^ { \mathrm { T } }
$$

该式右端第一项就是只用观测向量l作配置时参数估值与信号估值的误差互协方差阵的计算公式，若用 $\mathbf { E } _ { \mathbf { x } \mathbf { s } \cdot \iota _ { 1 } }$ 表示之，则有

$$
\mathbf { E } _ { \mathbf { x } \mathbf { s } \cdot \boldsymbol { \iota } _ { 1 } } = - \mathbf { P } _ { 1 } ^ { - 1 } \overline { { \mathbf { A } } } _ { 1 } \mathbf { C } _ { 1 1 } ^ { - 1 } \mathbf { C } _ { 1 } ^ { \mathrm { T } }
$$

而 $( 1 3 \cdot 2 0 0 )$ 式就可写为

$$
\mathbf { E } _ { \mathbf { x } \mathbf { s } } { = } \mathbf { E } _ { \mathbf { x } \mathbf { s } \cdot \boldsymbol { \imath } _ { 1 } } { - } \mathbf { P } _ { 1 } ^ { - 1 } \overline { { \mathbf { A } } } _ { 2 } ^ { \mathrm { T } } \overrightarrow { \mathbf { C } } _ { 2 2 } ^ { - 1 } \overline { { \mathbf { C } } } _ { 2 } ^ { \mathrm { T } }
$$

最后改化信号估值S的误差协方差阵的计算式(13·39)式。因为

$$
\begin{array} { r l } & { \mathbf { C } _ { \mathrm { s i } } \overline { { \mathbf { C } } } ^ { - 1 } \mathbf { C } _ { \mathrm { t s } } = ( \mathbf { C } _ { 1 } \mathbf { \Sigma } _ { \mathrm { C } _ { 2 } } ) \left[ \begin{array} { l l } { \mathbf { B } _ { 1 1 } } & { \mathbf { B } _ { 1 2 } } \\ { \mathbf { B } _ { 2 1 } } & { \mathbf { B } _ { 2 2 } } \end{array} \right] \left[ \begin{array} { l } { \mathbf { C } _ { 1 } ^ { \mathrm { T } } } \\ { \mathbf { C } _ { 2 } ^ { \mathrm { T } } } \end{array} \right] } \\ & { \qquad = \mathbf { C } _ { 1 } \mathbf { C } _ { 1 1 } ^ { - 1 } \mathbf { C } _ { 1 } ^ { \mathrm { T } } + ( \mathbf { C } _ { 2 } - \mathbf { C } _ { 1 } \mathbf { C } _ { 1 1 } ^ { - 1 } \mathbf { C } _ { 1 2 } ) \mathbf { B } _ { 2 2 } ( \mathbf { C } _ { 2 } ^ { \mathrm { T } } - \mathbf { C } _ { 2 1 } \mathbf { C } _ { 1 1 } ^ { - 1 } \mathbf { C } _ { 1 } ^ { \mathrm { T } } ) } \end{array}
$$

而

$$
\mathrm { C } _ { \mathrm { s t } } \overline { { \mathrm { C } } } ^ { - 1 } \mathrm { A } { = } \mathrm { C } _ { 1 } \mathrm { C } _ { 1 1 } ^ { - 1 } \mathrm { A } _ { 1 } { + } ( \mathrm { C } _ { 2 } { - } \mathrm { C } _ { 1 } \mathrm { C } _ { 1 1 } ^ { - 1 } \mathrm { C } _ { 1 2 } ) \mathrm { B } _ { 2 2 } \overline { { \mathrm { A } } } _ { 2 }
$$

还有前面已得到的

$$
( \mathbf { A } ^ { \mathrm { T } } \overline { { \mathbf { C } } } ^ { - 1 } \mathbf { A } ) ^ { - 1 } \dot { \mathbf { A } } ^ { \mathrm { T } } \overline { { \mathbf { C } } } ^ { - 1 } \mathbf { C } _ { \mathrm { u s } } = \mathbf { P } _ { 1 } ^ { - 1 } \mathbf { A } _ { 1 } ^ { \mathrm { T } } \mathbf { C } _ { 1 1 } ^ { - 1 } \mathbf { C } _ { 1 } ^ { \mathrm { T } } + \mathbf { P } _ { 1 } ^ { - 1 } \overline { { \mathbf { A } } } _ { 2 } ^ { \mathrm { T } } \overline { { \mathbf { C } } } _ { 2 2 } ^ { - 1 } \overline { { \mathbf { C } } } _ { 2 } ^ { \mathrm { T } }
$$

将这三个式子代入 $( 1 3 \cdot 3 9 )$ 式，得到

$$
\mathrm { E s s } = \mathrm { C s } \mathrm { s } - \mathrm { C } _ { 1 } \mathrm { C } _ { 1 1 } ^ { - 1 } \mathrm { C } _ { 1 } ^ { \mathrm { T } } - ( \mathrm { C } _ { 2 } \mathrm { - } \mathrm { C } _ { 1 } \mathrm { C } _ { 1 1 } ^ { - 1 } \mathrm { C } _ { 1 2 } ) \mathrm { B } _ { 2 2 } ( \mathrm { C } _ { 2 } ^ { \mathrm { T } } \mathrm { - } \mathrm { C } _ { 2 1 } \mathrm { C } _ { 1 1 } ^ { - 1 } \mathrm { C } _ { 1 } ^ { \mathrm { T } } )
$$

$$
+ \big [ \mathbf { C } _ { 1 } \mathbf { C } _ { 1 1 } ^ { - 1 } \mathbf { A } _ { 1 } + ( \mathbf { C } _ { 2 } - \mathbf { C } _ { 1 } \mathbf { C } _ { 1 1 } ^ { - 1 } \mathbf { C } _ { 1 2 } ) \mathbf { B } _ { 2 2 } \overline { { \mathbf { A } } } _ { 2 } \big ] ( \mathbf { P } _ { 1 } ^ { - 1 } \mathbf { A } _ { 1 } ^ { \mathrm { T } } \mathbf { C } _ { 1 1 } ^ { - 1 } \mathbf { C } _ { 1 } ^ { \mathrm { T } } + \mathbf { P } _ { 1 } ^ { - 1 } \widetilde { \mathbf { A } } _ { 2 } ^ { \mathrm { T } } \overline { { \mathbf { C } } } _ { 2 2 } ^ { - 1 } \mathbf { C } _ { 2 } ^ { \mathrm { T } } )
$$

通过运算，并顾及到 $( 1 3 \cdot 1 9 9 )$ 式，可得

$$
\mathrm { E s s = C s s - C _ { 1 } C _ { 1 1 } ^ { - 1 } C _ { 1 } ^ { T } + C _ { 1 } C _ { 1 1 } ^ { - 1 } A _ { 1 } P _ { 1 } ^ { - 1 } A _ { 1 } ^ { T } C _ { 1 1 } ^ { - 1 } C _ { 1 } ^ { T } - ( C _ { 2 } - C _ { 1 } C _ { 1 1 } ^ { - 1 } C _ { 1 2 } ) B _ { 2 2 } \overline { { C } } _ { 2 } ^ { T } }
$$

$$
+ C _ { 1 } C _ { 1 1 } ^ { - 1 } \mathsf { A } _ { 1 } \mathsf { P } _ { 1 } ^ { - 1 } \overline { { \mathsf { A } } } _ { 2 } ^ { \mathsf { T } } \overline { { \mathsf { C } } } _ { 2 2 } ^ { - 1 } \overline { { \mathsf { C } } } _ { 2 } ^ { \mathsf { T } } + ( \mathsf { C } _ { 2 } - \mathsf { C } _ { 1 } \mathsf { C } _ { 1 1 } ^ { - 1 } \mathsf { C } _ { 1 2 } ) \mathsf { B } _ { 2 2 } \overline { { \mathsf { A } } } _ { 2 } \mathsf { P } _ { 1 } ^ { - 1 } \overline { { \mathsf { A } } } _ { 2 } ^ { \mathsf { T } } \overline { { \mathsf { C } } } _ { 2 2 } ^ { - 1 } \overline { { \mathsf { C } } } _ { 2 } ^ { \mathsf { T } }
$$

该式右端前三项就是只用观测向量 $l _ { 1 }$ 所得的信号估值的误差协方差阵，若用 $\mathrm { E s s } \cdot l _ { 1 }$ 表示，则有

$$
\mathrm { E s s } \ \bullet \ l _ { 1 } = \mathrm { C s s } - \mathrm { C } _ { 1 } \mathrm { C } _ { 1 1 } ^ { - 1 } \mathrm { C } _ { 1 } ^ { \mathrm { T } } + \mathrm { C } _ { 1 } \mathrm { C } _ { 1 1 } ^ { - 1 } \mathrm { A } _ { 1 } \mathrm { P } _ { 1 } ^ { - 1 } \mathrm { A } _ { 1 } ^ { \mathrm { T } } \mathrm { C } _ { 1 1 } ^ { - 1 } \mathrm { C } _ { 1 } ^ { \mathrm { T } }
$$

利用 $( 1 3 \cdot 1 8 4 )$ 式，可以将 $( 1 3 \cdot 2 0 5 )$ 式右端的第四项和第六项合并为一项

$$
- ( \mathrm { C } _ { 2 } { - } \mathrm { C } _ { 1 } \mathrm { C } _ { 1 1 } ^ { - 1 } \mathrm { C } _ { 1 2 } ) \overline { { \mathrm { C } } } _ { 2 2 } ^ { - 1 } \mathrm { C } _ { 2 } ^ { \intercal }
$$

再与第五项合并在一起，并考虑到 $( 1 3 \cdot 1 9 9 )$ 式，可写为

$$
- \overline { { \mathsf { C } } } _ { 2 } \overline { { \mathsf { C } } } _ { 2 2 } ^ { - 1 } \overline { { \mathsf { C } } } _ { 2 } ^ { \mathrm { T } }
$$

这样一来，信号估值的误差协方差阵的计算公式变为

$$
\mathrm { E s s } { = } \mathrm { E s s } \ \cdot \ l _ { 1 } { - } \overline { { \mathrm { C } } } _ { 2 } \overline { { \mathrm { C } } } _ { 2 2 } ^ { - 1 } \overline { { \mathrm { C } } } _ { 2 } ^ { \mathrm { T } }
$$

在实际操作时，逐步配置可以采用每次只增加一个新的观测值，即 $\iota _ { z }$ 中只包含一个观测值。只要连续地反复这个过程，所有的新观测值就可以都用进去了。这被称为序列配置。

举一个例子说明之。若共有50个观测值 $l _ { \mathrm { i } } ( _ { \mathrm { i } } { = } 1 , 2 , \cdots , 5 0 )$ ，参数向量X包含8个参数。第一步，取10个(必需大于8个)观测值作为第一组观测向量 $l _ { 1 }$ ，计算出 $\smash { \widetilde { \mathbf { X } } _ { \perp } }$ 和所需信号S的第一次估值;第二步，把第11个观测值作为一个分向量 $l _ { 2 }$ ,应用前面所讲的公式，对结果进行一次改正；第三步，再把第12个观测值，为 $l _ { 2 }$ ,再对结果进行修正；这样一直做下去，直到第50 个观测值用进去为止。当用这种方法计算时，只在求估值的第一次近似值时要进行矩阵的求逆。由于这个矩阵很小，很容易完成计算。以后的 $\overline { { \mathbf { C } } } _ { 2 2 }$ 只是一个量，它的逆就是这个量的倒数。而$\mathbf { P } ^ { - 1 }$ 可连续地由 $( 1 3 \cdot 1 9 6 )$ 式算出，因为前一步骤的 $\mathbf { E } _ { \mathbf { X } \mathbf { X } \cdot \mathbf { \boldsymbol { \iota } } _ { 1 } }$ 就是下一步骤的 $\mathbf { P } _ { 1 } ^ { - 1 }$ 。显然，虽然不做矩阵求逆，但却增加了很多的矩阵相乘，因此总的计算量并没有减少。事实上，逐步配置可以比作按分块矩阵求逆，而序列配置则相当于加边矩阵求逆。

# 第十四章 地球外部重力场

# $\ S$ 14.1概 述

在地球上空运行的人造地球卫星和各种飞行器，仍然受到地球重力场的作用。如果它们所受的作用力只是指向地球质心的向心力 $\frac { \mathbf { f } \mathbf { M } } { \rho ^ { 2 } }$ ，（其中 $P$ 为地心向径、f为万有引力常数和 $\mathbf { M }$ 为地球质量)则它们的飞行轨道是椭圆,地球质心是该椭圆的一个焦点。但实际上，由于地球形状的不规则和内部质量分布的不均匀，地球对空间飞行器的引力方向不指向球心、大小也与 $\frac { \mathrm { f } \mathrm { \bf { M } } } { \rho ^ { 2 } }$ 有差别，就使得它们的运行轨道偏离椭圆轨道。这种差别被称之为摄动力。根据天体力学8中的摄动运动理论，只要有了摄动力的三个分量K、Kz、K，则可求得它们的轨道变化。如图14.1所示,Ki是沿着向径方向的分量，即背向地心为正,K是在轨道平面内垂直于向径p的方向上的分力,与运动方向一致时为正;K是在轨道面法线方向的分量，向北为正。设地球对飞行器的引力在这三个方向分量为gi、g和g,则在忽略对飞行器的其他作用力的情况下，它所受的摄动力的三分量为 $( 1 4 \cdot 1 )$ 式。

![](images/3bab8f9d1df82bcbd73231c0eabf9f7be8f4e02abdf53694b9ebe0c3a0bdc6be.jpg)  
图14.1

$$
\left. { \begin{array} { l } { \displaystyle \mathbf { K } _ { 1 } = \mathbf { g } _ { 1 } + \frac { \mathbf { f } \mathbf { M } } { \boldsymbol { \rho } ^ { 2 } } } \\ { \displaystyle \mathbf { K } _ { 2 } = \mathbf { g } _ { 2 } } \\ { \displaystyle \mathbf { K } _ { 3 } = \mathbf { g } _ { 3 } } \end{array} } \right\}
$$

因此，要求得飞行器在空间运行的准确轨道，必需知道它实际所受的引力大小和方向。如同前面研究重力场那样，实际引力又可分为正常引力和扰动重力两部份，即

$$
\begin{array} { r } { \vec { \bf g } = \vec { \bf F } + \vec { \boldsymbol { \delta } } } \end{array}
$$

其中 $\vec { \pmb { F } }$ 是正常椭球的引力矢量，δ为扰动重力矢量。如何利用地面重力数据准确地计算出空间点的扰动重力矢量，是本章研究的主要内容。

通常，首先算得的是正常引力和扰动重力沿球坐标 $( \rho , \varphi , \lambda )$ 的三个坐标线方向的分量，即$\mathbb { F } _ { \rho } . \mathbb { F } _ { \varphi } . \mathbb { F } _ { \lambda }$ 和 $\delta _ { p } . \delta _ { \varphi } . \delta _ { \lambda }$ 。此时实际引力沿坐标线的三分量为

$$
\left. \begin{array} { c } { { g _ { \rho } = \mathrm { F } _ { \varphi } + \delta _ { \rho } } } \\ { { } } \\ { { g _ { \bar { \varphi } } = \mathrm { F } _ { \bar { \varphi } } + \delta _ { \bar { \varphi } } } } \\ { { } } \\ { { g _ { \lambda } = \mathrm { F } _ { \lambda } + \delta _ { \lambda } } } \end{array} \right\}
$$

显然有 $\mathbf { g _ { 1 } } = \mathbf { g _ { \rho } }$ ，可直接用于计算掇动力 $\mathbf { K } _ { 1 }$ ；但 $\pmb { \mathrm { g } } _ { \pmb { \varphi } }$ 和 $\pmb { \mathrm { g } } _ { \lambda }$ 还需转化为 ${ \pmb g } _ { 2 }$ 和 ${ \pmb g } _ { 3 }$ ,才能得到掇动力 $\mathbf { K } _ { 2 }$ 和 $\mathbb { K } _ { 3 }$ 。因为 $8 0 \cdot 8 4$ 和 $\pmb { 8 2 } \cdot \pmb { 8 3 }$ 都与向径 ${ \pmb \rho }$ 垂直，故同在垂直于 $P$ 的一个平面内。如图14.1所示，以 $\pmb { \updownarrow }$ 表示 ${ \pmb g } _ { 2 }$ 与 $\pmb { \ 8 4 }$ 的夹角，按照解析几何中的转轴公式有

$$
\left. \begin{array} { r } { \tt { g } _ { 2 } = \tt { g } _ { \varphi } \cos x + \tt { g } _ { \mathrm { { a } } } \sin x \it \Psi } \\ { \tt { g } _ { 2 } = \tt { g } _ { \varphi } \sin x - \tt { g } _ { \mathrm { { a } } } \cos x \it \Psi } \end{array} \right\}
$$

从图14.1看到，这个 $\texttt { \textbf { X } }$ 角就是轨道面与子午面的夹角，在轨道、子午线和赤道组成的直角球面三角形中，很容易得出

$$
\cos \left( \omega + \upsilon \right) { = } \mathbf { c } \mathbf { t } \mathbf { g } \mathbf { i } \mathbf { c } \mathbf { t } \mathbf { g } \mathbf { \Psi }
$$

其中i是轨道面相对于赤道的倾角， $. \pmb { \omega }$ 为近地点与升交点的角距， $\pmb { v }$ 是真近点角。因而有

$$
\scriptstyle \mathbf { c t g } \chi = \cos ( \omega + \upsilon ) \mathbf { t g i }
$$

因为通过对飞行器的跟踪观测，可以算得它的轨道根数 $\omega , \mathrm { i }$ 及真近点们 $_ { \star }$ 的数值，因此用(14.5)式可以求出 $\pmb { \updownarrow }$ 角，再将它代入 $( 1 4 \cdot 4 )$ 式中就可由 $\pmb { \mathrm { g } } _ { \mp }$ 和 ${ \pmb g } _ { \pmb { \lambda } }$ 算出 $\pmb { \mathrm { g } } _ { 2 }$ 和 ${ \pmb g } _ { 3 }$ 。

前面已经讲到，正常重力场总是采用水准椭球的重力场，它对外部点的引力三分量 $( \mathbf { F } _ { \rho }$ ，F,Fx)的计算方法已在&6.5中讲述。因此，本章只研究扰动重力三分量的计算方法。

# $\ S$ 14.2用地球重力场模型计算扰动重力

在第十章中讲到，地球重力场模型就是用一个截断到 $\mathbf { N }$ 阶的引力位球谐函数级数式来表示地球引力场。此时，扰动位的表达式为 $( 1 0 \cdot 2 )$ 式。在用地球平均半径 $\mathbf { R }$ 代替椭球长半径 $\mathtt { a _ { e } }$ 的情况下，可以写为

$$
\mathrm { T } = - \frac { \mathrm { f } \mathbf { M } } { \rho } \sum _ { n = 2 } ^ { \mathrm { N } } ( \frac { \mathrm { R } } { \rho } ) ^ { \mathrm { n } } \sum _ { \mathbf { n } = 0 } ^ { \mathrm { n } } ( \overline { { \mathrm { C } } } _ { \mathrm { n m } } ^ { \ast } \mathrm { c o s m } \lambda + \overline { { \mathrm { S } } } _ { \mathrm { n m } } \mathrm { s i n m } \lambda ) \overline { { \mathrm { P } } } _ { \mathrm { n m } } ( \mathrm { c o s } \theta )
$$

式中(p,0,)是空间点的球坐标： $\pmb { \rho } { = } \pmb { \ R } { + } \pmb { \mathrm { H } }$ 是地心向径， $\mathbf { H }$ 是点在地面上的高度； $\scriptstyle \theta = 9 0 ^ { \circ } - \varphi$ 是地心余纬度； $\gimel$ 是地心经度。将 $( 1 4 \cdot 6 )$ 式对三个坐标分别求偏导数，就可得到扰动重力的三分量，即

$$
 \begin{array} { l } { { \hat { \lambda } _ { \mathrm { * } } = \displaystyle \frac { \partial \Gamma } { \partial \boldsymbol { \rho } } = \displaystyle \frac { \mathrm { f } \mathrm { M } } { \rho ^ { 2 } } \sum _ { \mathrm { = 2 } } ^ { \mathrm { N } } ( \boldsymbol { \mathrm { n } } + 1 ) ( \frac { \mathrm { R } } { \rho } ) ^ { \mathrm { * } } \sum _ { \mathrm { n = 0 } } ^ { \mathrm { n } } ( \overline { { \mathrm { C } } } _ { \mathrm { n n } } ^ { \mathrm { * } } \mathrm { c o s m } \lambda + \overline { { \mathrm { S } } } _ { \mathrm { a m } } \mathrm { s i n } \boldsymbol { \mathrm { m } } \lambda ) \overline { { \mathrm { P } } } _ { \mathrm { n n } } ( \mathrm { s i n } \boldsymbol { \varphi } ) } } \\  { \hat { \lambda } _ { \mathrm { * } } = \displaystyle \frac { 1 } { \rho } \frac { \partial \mathrm { T } } { \partial \boldsymbol { \varphi } } = - \ \ \frac { \mathrm { f } \mathrm { M } } { \rho ^ { 2 } } \sum _ { \mathrm { n = 2 } } ^ { \mathrm { N } } ( \frac { \mathrm { R } } { \rho } ) ^ { \mathrm { * } } \sum _ { \mathrm { n = 0 } } ^ { \mathrm { n } } ( \overline { { \mathrm { C } } } _ { \mathrm { n n } } ^ { \mathrm { * } } \mathrm { c o s } \boldsymbol { \mathrm { m } } \lambda + \overline { { \mathrm { S } } } _ { \mathrm { a m } } \mathrm { s i n } \boldsymbol { \mathrm { m } } \lambda ) \ \frac { \mathrm { d } \overline { { \mathrm { P } } } _ { \mathrm { n n } } ( \mathrm { s i n } \boldsymbol { \varphi } ) } { \mathrm { d } \boldsymbol { \varphi } } } \\   \hat { \lambda } _ { \mathrm { * } } = \displaystyle \frac { 1 } { \rho \mathrm { c o s } \varphi } \displaystyle \frac { \partial \mathrm { T } } { \partial \boldsymbol { \hat { \lambda } } } = \frac { \mathrm { f } \mathrm { M } } { \rho ^ { 2 } \mathrm { c o s } \varphi } \sum _ { \mathrm { n = 2 } } ^ { \mathrm { N } } ( \frac { \mathrm { R } } { \rho } ) ^ { \mathrm { * } } \sum _ { \mathrm { n = 0 } } ^ { \mathrm { n } } \mathrm { m } ( \overline { { \mathrm { C } } } _ { \mathrm { n a } } ^ { \mathrm { * } } \mathrm { s i n } \lambda - \overline { { \mathrm { S } } } _ { \mathrm { n n } } \mathrm { c o s } \boldsymbol { \mathrm { m } }  \end{array}
$$

由于式中的系数 $\overline { { \mathbf { C } } } _ { \mathbf { n m } } ^ { * }$ 和 $\overrightarrow { \mathbf { S } } _ { \mathbf { n m } } ^ { * }$ 是已知的，用它们就可算出扰动重力三分量的数值。

利用位系数模型计算扰动重力，误差来源于两个方面：一是位系数的误差，二是级数式截断到N阶所引起的误差。下面对第二项误差进行讨论，它通常被称为截断误差。

在讨论截断误差时，采用类似于讨论高程异常和垂线偏差的截断误差那样的办法，即以重力异常的阶方差为基础。为此，先要导出用n阶重力异常△g表示的扰动重力分量的计算式。

根据 $\ S 1 0 . 6$ 所讲，球面上的重力异常 $\Delta \pmb { \mathrm { g } }$ 可以用 $\pmb { \mathrm { n } }$ 阶重力异常表示为

$$
\Delta \mathbf { g } { = } \sum _ { n = 2 } ^ { \infty } \Delta \mathbf { g } _ { n }
$$

其中

$$
\Delta \mathrm { g _ { n } } \mathrm { = } \frac { \mathrm { f } \mathrm { M } } { \mathrm { R ^ { 2 } } } ( \mathrm { n } \mathrm { - } 1 ) \sum _ { \mathrm { m = 0 } } ^ { \mathrm { n } } ( \overline { { \mathbb { C } } } _ { \mathrm { n m } } ^ { \ast } \mathrm { c o s m } \lambda \mathrm { + } \overline { { \mathbb { S } } } _ { \mathrm { a m } } \mathrm { s i n m } \lambda ) \overline { { \mathrm { P } } } _ { \mathrm { n m } } ( \mathrm { s i n } \varphi )
$$

由此可得

$$
\left. \begin{array} { l } { \displaystyle \frac { \mathbf { f } \mathbf { M } } { \overline { { \rho } } ^ { 2 } } \overset { \mathtt { s } } { \geq } ( \overline { { \mathbb { C } } } _ { \mathrm { n m } } ^ { * } \mathrm { c o s m } \lambda + \overline { { \mathbb { S } } } _ { \mathrm { n m } } \mathrm { s i n m } \lambda ) \overline { { \mathbb { P } } } _ { \mathrm { n m } } ( \mathrm { s i n } \varphi ) = ( \frac { \mathbf { R } } { \overline { { \rho } } } ) ^ { 2 } \frac { \Delta \mathbf { g } _ { \mathrm { n } } } { \mathbf { n } - 1 } } \\ { \displaystyle \frac { \mathbf { f } \mathbf { M } } { \overline { { \rho } } ^ { 2 } } \overset { \mathtt { s } } { \geq } ( \overline { { \mathbb { C } } } _ { \mathrm { n m } } ^ { * } \mathrm { c o s m } \lambda + \overline { { \mathbb { S } } } _ { \mathrm { n m } } \mathrm { s i n m } \lambda ) \frac { \mathrm { d } \overline { { \mathbb { P } } } _ { \mathrm { n m } } ( \mathrm { s i n } \varphi ) } { \mathrm { d } \overline { { \varphi } } } = ( \frac { \mathbf { R } } { \overline { { \rho } } } ) ^ { 2 } \frac { 1 \cdot \mathbf { \alpha } } { \mathbf { n } - 1 } \frac { \partial \Delta \mathbf { g } _ { \mathrm { n } } } { \partial \overline { { \varphi } } } } \\ { \displaystyle \frac { \mathbf { f } \mathbf { M } } { \overline { { \rho } } ^ { 2 } } \overset { \mathtt { n } } { \geq } \operatorname { m } ( \overline { { \mathbb { C } } } _ { \mathrm { n m } } ^ { * } \mathrm { s i n m } \lambda - \overline { { \mathbb { S } } } _ { \mathrm { n m } } \mathrm { c o s m } \lambda ) \overline { { \mathbb { P } } } _ { \mathrm { n m } } ( \mathrm { s i n } \varphi ) = - ( \frac { \mathbf { R } } { \overline { { \rho } } } ) ^ { 2 } \frac { 1 } { \mathbf { n } - 1 } \frac { \partial \Delta \mathbf { g } _ { \mathrm { n } } } { \partial \lambda } } \end{array} \right\}
$$

将 $( 1 4 \cdot 9 )$ 式代入 $( 1 4 \cdot 7 )$ 式，则得

$$
\left. \begin{array} { l } { { \displaystyle \delta _ { \rho } = \sum _ { n = 2 } ^ { N } ( \frac { \Pi + 1 } { n - 1 } ) ( \frac { \mathbb { R } } { \rho } ) ^ { n + 2 } \Delta g _ { n } } } \\ { { \displaystyle \qquad \delta _ { \varphi } = - \sum _ { n = 2 } ^ { N } \frac { 1 } { n - 1 } ( \frac { \mathbb { R } } { \rho } ) ^ { n + 2 } \frac { \partial \Delta g _ { n } } { \partial \varphi } } } \\ { { \displaystyle \qquad \delta _ { \imath } = - \sum _ { n = 2 } ^ { N } \frac { 1 } { n - 1 } ( \frac { \mathbb { R } } { \rho } ) ^ { n + 2 } \frac { \partial \Delta g _ { n } } { \cos \varphi \partial \mathbb { A } } } } \end{array} \right\} .
$$

显而易见，截断误差为

$$
\left. \begin{array} { l } { { \displaystyle { \hat { \sigma } } ^ { \prime } = \sum _ { n = N + 1 } ^ { \infty } ( \frac { \mathbf { n } + 1 } { \mathbf { n } - 1 } ) ( \frac { \mathbf { R } } { \mathbf { \rho } } ) ^ { n + 2 } \Delta \mathbf { g } _ { \mathrm { n } } } } \\ { { \displaystyle { \hat { \sigma } } ^ { \prime } \circ = - \sum _ { n = N + 1 } ^ { \infty } ( \frac { 1 } { \mathbf { n } - 1 } ) ( \frac { \mathbf { R } } { \mathbf { \rho } } ) ^ { n + 2 } \frac { \partial \Delta \mathbf { g } _ { \mathrm { n } } } { \partial \mathbf { \rho } } } } \\ { { \displaystyle { \hat { \sigma } } ^ { \prime } \mathbf { \rho } _ { \mathrm { { a } } } = - \sum _ { n = N + 1 } ^ { \infty } \frac { 1 } { \mathbf { n } - 1 } ( \frac { \mathbf { R } } { \mathbf { \rho } } ) ^ { n + 2 } \frac { 1 } { \cos \varphi } \frac { \partial \Delta \mathbf { g } _ { \mathrm { n } } } { \partial \mathbf { \rho } } } } \end{array} \right\}
$$

为了估算其数值的大小，取其球面上的均方根值。若以 $\sigma _ { \rho }$ 表示向经方向分量 $\delta _ { \rho }$ 的全球均方根值， $\sigma _ { H }$ 表示水平方向分量 $\sqrt { ( \delta _ { \mathfrak { s } } ) ^ { 2 } + ( \delta _ { \mathfrak { a } } ^ { \prime } ) ^ { 2 } }$ 的全球均方根值，则有

$$
\sigma _ { p } ^ { 2 } = \sum _ { { \bf n } = { \bf N } + 1 } ^ { \infty } ( \frac { { \bf n } + 1 } { { \bf n } - 1 } ) ^ { 2 } ( \frac { { \bf R } } { \rho } ) ^ { 2 { \bf n } + 4 } { \bf C _ { n } }
$$

$$
\sigma _ { \mathrm { H } } ^ { 2 } = \sum _ { { \bf n } = { \bf N } + 1 } ^ { \infty } \frac { { \bf n } ( { \bf n } + 1 ) } { ( { \bf n } - 1 ) ^ { 2 } } ( \frac { { \bf R } } { \rho } ) ^ { 2 { \bf n } + 4 } { \bf C _ { \bf n } }
$$

在导出 $( 1 4 \cdot 1 3 )$ 式时利用了 $( 1 0 ~ \cdot ~ 6 3 )$ 式，上两式中的 $\mathbf { C _ { n } }$ 是重力异常的阶方差。如果利用$( 1 0 \cdot 4 9 )$ 式表示的重力异常阶方差模型和 $( \cdot 1 0 \cdot 5 0 )$ 式给出的常数值，则按 $( 1 4 \cdot 1 2 )$ 式可以算得表14.1所示的结果。

表14.1  

<table><tr><td rowspan=1 colspan=1>op毫伽     NH(km)</td><td rowspan=1 colspan=1>36</td><td rowspan=1 colspan=1>72·</td><td rowspan=1 colspan=1>180</td><td rowspan=1 colspan=1>360</td><td rowspan=1 colspan=1>540</td><td rowspan=1 colspan=1>2200</td></tr><tr><td rowspan=1 colspan=1>0.2.151050100200500</td><td rowspan=1 colspan=1>3937292310520.3</td><td rowspan=1 colspan=1>38352721730.7</td><td rowspan=1 colspan=1>343122162.90.4</td><td rowspan=1 colspan=1>282516100.5</td><td rowspan=1 colspan=1>2321.120.6</td><td rowspan=1 colspan=1>430.6</td></tr></table>

表中的数字表明，截断误差与计算点的高度有着明显的关系。对于大于 $2 0 0 \mathbf { k m }$ 高度的点，用36 阶重力场模型，截断误差就小于2毫伽；而对于二三十公里高度的点，即使用现有的最高阶次的360阶模型，其截断误差还大于2毫伽。这是因为扰动重力场的精细结构的影响而造成的。

# 14.3用司托克斯积分法计算扰动重力

![](images/d0fb4b85f5b2d7f45a77cc91b9581221724df01003d13507e8c59c46feac654d.jpg)  
图14.2

由第八章中讲的司托克斯理论知道，在视地球为球体且忽略零阶项的情况下，地球外部点 $( \pmb \rho , \pmb \varphi , \lambda )$ 的扰动位与地面重力异常有如下的关系式：

$$
\mathrm { T } _ { ( p , \psi , \lambda ) } = \frac { 1 } { 4 \pi } \int _ { \frac { \lambda } { 2 } } ^ { } \Delta \mathbf { g } \mathbf { S } ( \rho , \psi ) \mathrm { d } \Sigma
$$

式中函数 $\mathbf { S } ( \pmb { \rho } , \pmb { \psi } )$ 的表达式为

$$
\mathrm { S } ( \rho , \psi ) = \frac { 2 } { \mathrm { r } } + \frac { 1 } { \rho } - \frac { 3 \mathrm { r } } { \rho ^ { 2 } } - \frac { 5 \mathrm { R } } { \rho ^ { 2 } } \mathrm { c o s } \psi
$$

$$
- \frac { 3 \mathbf { R } } { \rho ^ { 2 } } \mathrm { c o s } \psi \mathrm { l n } \frac { \boldsymbol { \rho } - \mathrm { R c o s } \psi + \mathbf { r } } { 2 \boldsymbol { \rho } }
$$

如图14.2所示， $\phi$ 为球面上的单元面积 ${ \tt d } \Sigma$ 的向径与 $P$ 的夹角， $\pmb { r }$ 为单元面积至求位点的距离，即

$$
\mathbf { r } = \sqrt { \pmb { \rho } ^ { 2 } + \mathbf { R } ^ { 2 } - 2 \pmb { \rho } \mathbf { R } \mathrm { c o s } \Psi }
$$

扰动重力是扰动位的偏导数，因此可以求得

$$
\left. \begin{array} { l } { { \displaystyle \hat { \partial } _ { \boldsymbol { \mathsf { p } } } { = } \frac { 1 } { 4 \pi } \Biggl \iint \Delta \mathbf { g } \frac { \partial \ S ( \boldsymbol { \mathsf { p } } , \boldsymbol { \psi } ) } { \partial \boldsymbol { \mathsf { p } } } \mathrm { d } \Sigma } } \\ { { \displaystyle \hat { \partial } _ { \boldsymbol { \mathsf { q } } } { = } \frac { 1 } { 4 \pi \rho } \Biggl \iint \Delta \mathbf { g } \frac { \partial S ( \boldsymbol { \mathsf { p } } , \boldsymbol { \psi } ) } { \partial \boldsymbol { \mathsf { q } } } \mathrm { d } \Sigma } } \\ { { \displaystyle \hat { \partial } _ { \boldsymbol { \mathsf { a } } } { = } \frac { 1 } { 4 \pi \rho \cos \varphi } \Biggl \iint \Delta \mathbf { g } \frac { \partial S ( \boldsymbol { \mathsf { p } } , \boldsymbol { \psi } ) } { \partial \boldsymbol { \mathsf { A } } } \mathrm { d } \Sigma } } \end{array} \right\}
$$

因为

$$
\frac { \partial \mathbb { S } ( \boldsymbol { \rho } , \boldsymbol { \psi } ) } { \partial \boldsymbol { \varphi } } = \frac { \partial \mathbb { S } ( \boldsymbol { \rho } , \boldsymbol { \psi } ) } { \partial \boldsymbol { \psi } } \frac { \partial \boldsymbol { \psi } } { \partial \boldsymbol { \varphi } }
$$

$$
\frac { \partial \mathrm { S } ( \rho , \phi ) } { \partial \lambda } = \frac { \partial \mathrm { S } ( \rho , \psi ) } { \partial \psi } \frac { \partial \psi } { \partial \lambda }
$$

再利用(8·42)式有

$$
\begin{array} { l } { { \displaystyle { \frac { \partial \psi } { \partial \varphi } } = - \cos \alpha } } \\ { ~ } \\ { { \displaystyle { \frac { \partial \psi } { \partial \Lambda } } = - \cos \psi \sin \alpha } } \end{array}
$$

$\pmb { \alpha }$ 的含意见图14.2。因此，(14.17)式可改写为

$$
\begin{array} { l } { { \displaystyle { \hat { \delta } _ { \mathfrak { p } } = \frac { 1 } { 4 \pi } \int \int \mathrm { \hat { \Delta } g } \frac { \mathrm { \partial \mathbb { S } } ( \rho , \psi ) } { \partial \mathfrak { p } } \mathrm { d } \Sigma } } } \\ { { \displaystyle { \hat { \Delta } _ { \mathfrak { p } } = - \frac { 1 } { 4 \pi \mathfrak { p } } \int \int \mathrm { \hat { \Delta } g } \frac { \mathrm { \partial \mathbb { S } } ( \rho , \psi ) } { \partial \psi } \mathrm { c o s a d } \Sigma } } } \\ { { \displaystyle { \hat { \delta } _ { \mathfrak { k } } = - \frac { 1 } { 4 \pi \mathfrak { p } } \int \int \mathrm { \hat { \Delta } g } \frac { \mathrm { \partial \mathbb { S } } ( \rho , \psi ) } { \partial \psi } \mathrm { s i n o d } \Sigma } } } \end{array}
$$

其中， $\frac { \partial \mathbb { S } ( \rho , \psi ) } { \partial \boldsymbol { \mathsf { p } } } \neq \mathbb { I } \frac { \partial \mathbb { S } ( \rho , \psi ) } { \partial \boldsymbol { \psi } }$ 的表达式可由 $( 1 4 \cdot 1 5 )$ 式求得

$$
\begin{array} { r l } & { \frac { \partial \mathbb { S } ( \rho , \phi ) } { \partial \boldsymbol { \wp } } = \frac { \rho - \operatorname { R c o s } \phi } { \mathbf { r } ^ { 3 } } - \frac { 3 } { \rho \mathbf { r } } - \frac { 1 } { \rho ^ { 2 } } + \frac { 6 \mathbf { r } } { \rho ^ { 3 } } - \frac { 1 3 \mathrm { R } } { \mathbf { r } ^ { 3 } } \mathrm { c o s } \psi + \frac { 6 \mathrm { R } } { \rho ^ { 3 } } \mathrm { c o s } \psi \mathrm { l n } \frac { \rho - \operatorname { R c o s } \psi + \mathbf { r } } { 2 \rho } } \\ & { \frac { \partial \mathbb { S } ( \rho , \psi ) } { \partial \psi } = \sin \psi ( 1 - \frac { 2 \rho \mathrm { R } } { \mathbf { r } ^ { 3 } } - \frac { 3 \mathrm { R } } { \rho \mathbf { r } } + \frac { 5 \mathrm { R } } { \rho ^ { 2 } } - \frac { 3 \mathrm { R } ( \mathbf { r } + \rho ) } { \rho ^ { 2 } \mathbf { r } } \frac { \cos \psi } { \mathbf { r } + \rho - \operatorname { R c o s } \psi } + \frac { 3 \mathrm { R } } { \rho ^ { 2 } } \mathrm { l n } \frac { \rho - \operatorname { R c o s } \psi + \mathbf { r } } { 2 \rho } } \end{array}
$$

利用 $( 1 4 \cdot 1 8 )$ 式就可由地面空间异常计算空间点的扰动重力三分量。

为了应用 $( 1 4 \cdot 1 8 )$ 式计算扰动重力三分量，需要用到全球的重力异常数据。通常用地球重力场模型来帮助解决，即在远区域应用重力异常的位系数级数式，而在近区域则用实测的地面重力异常数据。此时，可将扰动重力分解为两部分合成，即

$$
\begin{array} { r l } & { \delta _ { \rho } = ( \delta _ { \rho } ) _ { \mathsf { S } } + ( \delta _ { \rho } ) _ { \mathsf { 0 } } } \\ & { \delta _ { \varphi } = ( \delta _ { \varphi } ) _ { \mathsf { S } } + ( \delta _ { \varphi } ) _ { \mathsf { 0 } } } \\ & { \delta _ { \lambda } = ( \delta _ { \lambda } ) _ { \mathsf { S } } + ( \delta _ { \lambda } ) _ { \mathsf { 0 } } } \end{array}
$$

其中

$$
\left. \begin{array} { l } { ( \hat { \vartheta } _ { \rho } ) _ { \mathrm { s } } = \displaystyle \frac { 1 } { 4 \pi } \displaystyle \iint \displaystyle \Delta \mathrm { g } _ { \mathrm { s } } \frac { \mathcal { K } ( \rho , \psi ) } { \mathcal { D } } \mathrm { d } \Sigma } \\ { \displaystyle \qquad \Sigma } \\ { ( \hat { \vartheta } _ { \varphi } ) _ { \mathrm { s } } = - \displaystyle \frac { 1 } { 4 \pi \rho } \displaystyle \iint \displaystyle \Delta \mathrm { g } _ { \mathrm { s } } \frac { \mathcal { K } ( \rho , \psi ) } { \mathcal { D } } \mathrm { c o s } \alpha \mathrm { d } \Sigma } \\ { ( \hat { \vartheta } _ { \mathrm { s } } ) _ { \mathrm { s } } = - \displaystyle \frac { 1 } { 4 \pi \rho } \displaystyle \iint \displaystyle \Delta \mathrm { g } _ { \mathrm { s } } \frac { \mathcal { K } ( \rho , \psi ) } { \mathcal { D } \psi } \mathrm { s i n } \alpha \mathrm { d } \Sigma } \end{array} \right\}
$$

而

$$
\begin{array} { l } { { ( \displaystyle \hat { \Theta } _ { p } ) _ { \mathfrak { o } } = \frac { 1 } { 4 \pi } \displaystyle \int _ { \mathfrak { s } _ { \mathfrak { o } } } \mathfrak { C } \displaystyle ( \Delta \mathbf { g } - \Delta \mathbf { g } _ { \mathrm { s } } )  \frac { \partial \mathfrak { S } ( \boldsymbol { p } , \boldsymbol { \Psi } ) } { \partial \mathfrak { p } } \mathrm { d } \Sigma  } } \\ { { \displaystyle  ( \hat { \Theta } _ { \mathfrak { e } } ) _ { \mathfrak { o } } = - \frac { 1 } { 4 \pi \rho } \displaystyle \int _ { \mathfrak { s } _ { \mathfrak { o } } } \mathfrak { C } \displaystyle ( \Delta \mathbf { g } - \Delta \mathbf { g } _ { \mathrm { s } } )  \frac { \partial \mathfrak { S } ( \boldsymbol { p } , \boldsymbol { \Psi } ) } { \partial \boldsymbol { \Psi } } \mathrm { c o s } \alpha \mathrm { d } \Sigma \} } } \\ { { \displaystyle ( \hat { \Theta } _ { \mathfrak { h } } ) _ { \mathfrak { o } } = -  \frac { 1 } { 4 \pi \rho } \displaystyle \int _ { \mathfrak { s } _ { \mathfrak { o } } } \mathfrak { C } ( \Delta \mathbf { g } - \Delta \mathbf { g } _ { \mathrm { s } } )  \frac { \partial \mathfrak { S } ( \boldsymbol { p } , \boldsymbol { \Psi } ) } { \partial \boldsymbol { \Psi } } \mathrm { s i n a d } \Sigma ] } } \end{array}
$$

这些式子中的△gs就是用位系数模型按(10·5)式算得的重力异常.∑是一个局部区域，因为$\Delta \mathbf { g } - \Delta \mathbf { g } \mathbf { s }$ 只含重力异常的高频部份，远区域影响很小而可以忽略。

(δ)s和(8)s和(8)s实际上就是只顾及重力场模型的情况下的扰动重力三分量，因此它们可以不按(14·21)式计算，而可以按前一节中给出的(14·7)式用位系数值直接算出。

而 $( \mathfrak { d } _ { \mathfrak { p } } ) _ { \mathfrak { o } \mathfrak { n } } ( \mathfrak { d } _ { \mathfrak { s } } ) _ { \mathfrak { o } }$ 和 $( \delta _ { \mathfrak { a } } ) _ { \mathfrak { 0 } }$ 的计算·利用有限求和的方法实现，即

$$
\left. \begin{array} { l } { { ( \hat { \Phi } _ { \mathfrak { p } } ) _ { \mathfrak { q } } = \displaystyle \frac { 1 } { 4 \pi } \sum _ { i } ( \overline { { \Delta \mathbf { g } } } - \overline { { \Delta \mathbf { g } } } _ { \mathrm { s } } ) _ { i } \mathbb C \underline { { \frac { \partial \mathbb { S } } { \partial } } } \gamma _ { \mathrm { 2 } i } \Delta \Sigma _ { \mathrm { i } } } } \\ { { ( \hat { \Phi } _ { \mathfrak { p } } ) _ { \mathfrak { q } } = - \displaystyle \frac { 1 } { 4 \pi \rho } \sum _ { \mathrm { i } } ( \overline { { \Delta \mathbf { g } } } - \overline { { \Delta \mathbf { g } } } _ { \mathrm { s } } ) _ { \mathrm { i } } \mathbb C \underline { { \frac { \partial \mathbb { S } } { ( \rho , \psi ) } } } \gamma _ { \mathrm { 4 } i } \mathrm { c o s } a _ { \mathrm { i } } \Delta \Sigma _ { \mathrm { i } } } } \\ { { ( \hat { \delta } _ { \mathrm { s } } ) _ { \mathfrak { q } } = - \displaystyle \frac { 1 } { 4 \pi \rho } \sum _ { \mathrm { i } } ( \overline { { \Delta \mathbf { g } } } - \overline { { \Delta \mathbf { g } } } _ { \mathrm { s } } ) _ { \mathrm { i } } \mathbb C \underline { { \frac { \partial \mathbb { S } } { ( \rho , \psi ) } } } \gamma _ { \mathrm { 4 } i } \mathrm { s i n } a _ { \mathrm { i } } \Delta \Sigma _ { \mathrm { i } } } } \end{array} \right\}
$$

其中 $( \overline { { \Delta { \bf g } } } - \overline { { \Delta { \bf g } } } _ { \mathrm { s } } )$ 是第 $\mathbf { i }$ 个网格的平均残差重力异常， $\psi _ { \mathrm { i } }$ 和 $\pmb { \alpha _ { \mathrm { i } } }$ 以网格中点的坐标按下式算得

$$
\begin{array} { r } { \mathrm { c o s } \psi _ { \mathrm { { i } } } = \mathrm { s i n } \varphi \mathrm { { s i n } } \varphi _ { \mathrm { { i } } } ^ { ' } + \mathrm { c o s } \varphi \mathrm { { c o s } } \varphi _ { \mathrm { { i } } } ^ { ' } \mathrm { c o s } \left( \lambda _ { \mathrm { { i } } } ^ { ' } - \lambda \right) } \\  \mathrm { t g } { a _ { \mathrm { { i } } } } = \frac { \mathrm { c o s } \varphi \mathrm { { s i n } } \left( \lambda _ { \mathrm { { i } } } ^ { ' } - \lambda \right) } { \mathrm { c o s } \varphi \mathrm { { s i n } } \varphi _ { \mathrm { { i } } } ^ { ' } - \mathrm { s i n } \varphi \mathrm { { c o s } } \varphi _ { \mathrm { { i } } } ^ { ' } \mathrm { c o s } \left( \lambda _ { \mathrm { { i } } } ^ { ' } - \lambda \right) } \enspace \left\{ \begin{array} { l l } {  } \\ { \mathrm { { c o s } } \varphi \mathrm { { s i n } } \end{array} \right. } \end{array}
$$

其中的 $( \varphi _ { \mathrm { i } } ^ { \prime } , \lambda _ { \mathrm { i } } ^ { \prime } )$ 是第i个网格中点的球面坐标： $\Delta \Sigma _ { \mathrm { i } }$ 是网格的面积。为了保证精度，在靠近计算点向径的地方网格面积要小，越远则可以越大。下面就来讨论各种大小网格应该有多大的区域。

假设在计算时在 $\psi { < } \psi _ { 1 }$ 的范围内采用 $1 ^ { \prime } \times 1 ^ { \prime }$ 网格的平均异常，在 ${ \dot { \psi } } _ { 1 } \sim { \dot { \psi } } _ { 2 }$ 的范围内用 $5 ^ { \prime } \times$ $5 ^ { \prime }$ 网格的平均异常，在 $\psi _ { ? } \sim \psi _ { ? }$ 的范围内用 $2 0 ^ { \prime } \times 2 0 ^ { \prime }$ 网格的平均异常，在 $\psi _ { 3 } \stackrel { \cdot \sim } { \sim } \psi _ { 4 }$ 的范围内用1°$\times 1 ^ { \circ }$ 网格的平均异常，而在 $\psi _ { 4 } \sim \pi$ 的范围内用完全到36阶次的位系数模型计算。类似于11.2中对垂线偏差计算所作的讨论，扰动重力径向分量的计算公式相应地可写为

$$
\begin{array} { r l } & { \hat { \mathbf { \Lambda } } _ { \theta } = \displaystyle \frac { \mathrm { R } ^ { 2 } } { 4 \pi } \displaystyle [ \int _ { 0 } ^ { 1 } \Big [ \sum _ { n = 2 } ^ { \lfloor \alpha \theta \rfloor } \Delta \mathbf { g } _ { \mathrm { n } } ) \frac { \Delta S ( \boldsymbol { \rho } , \boldsymbol { \phi } ) } { \partial \boldsymbol { \phi } } \mathrm { d } \boldsymbol { \omega } + \displaystyle \int _ { 0 } ^ { 2 \pi ^ { b _ { 2 } } } ( \sum _ { n = 2 } ^ { \lfloor \alpha \theta \rfloor } \Delta \mathbf { g } _ { \mathrm { n } } ) \frac { \Delta S ( \boldsymbol { \rho } , \boldsymbol { \phi } ) } { \partial \boldsymbol { \phi } } \mathrm { d } \boldsymbol { \omega } } \\ & { \quad \quad \quad \quad + \displaystyle \int _ { 0 \neq } ^ { 2 \pi ^ { b _ { 3 } } } \sum _ { n = 2 } ^ { \xi ( 1 ) } \Delta \mathbf { g } _ { \mathrm { n } } ) \frac { \Delta S ( \boldsymbol { \rho } , \boldsymbol { \phi } ) } { \partial \boldsymbol { \phi } } \mathrm { d } \boldsymbol { \omega } + \displaystyle \int _ { 0 } ^ { 2 \pi ^ { b _ { 4 } } } ( \sum _ { n = 2 } ^ { \lfloor \alpha \theta \rfloor } \Delta \mathbf { g } _ { \mathrm { n } } ) \frac { \Delta S ( \boldsymbol { \rho } , \boldsymbol { \phi } ) } { \partial \boldsymbol { \phi } } \mathrm { d } \boldsymbol { \omega } + \displaystyle \int _ { 0 \neq } ^ { 2 \pi ^ { b } } ( \sum _ { n = 2 } ^ { \lfloor \alpha \rfloor } \Delta \mathbf { g } _ { \mathrm { n } } ) \frac { \Delta S ( \boldsymbol { \rho } , \boldsymbol { \phi } ) } { \partial \boldsymbol { \phi } } } \end{array}
$$

很显然，此时由于数据不充分所引起的误差8为

$$
\begin{array} { r l } & { \frac { \mathrm { R } ^ { 2 } } { 4 \pi } \mathrm { C } \displaystyle \int \displaystyle \int _ { 0 } ^ { \infty } \mathrm { C } \displaystyle \sum _ { n = 1 0 8 0 1 } ^ { \infty } \Delta g _ { n } ) \frac { \Delta \mathrm { S } ( \rho , \psi ) } { \partial \mathrm { p } } \mathrm { d } \omega + \displaystyle \int _ { 0 \psi _ { \downarrow } } ^ { 2 \psi _ { \downarrow } ^ { \ast } } \mathrm { C } \displaystyle \sum _ { n = 2 1 6 1 } ^ { \infty } \Delta g _ { n } ) \frac { \mathcal { S } ( \rho , \psi ) } { \partial \mathrm { p } } \mathrm { d } \omega + \displaystyle \int _ { 0 \psi _ { \downarrow } } ^ { 2 \psi _ { \downarrow } ^ { \ast } } \mathrm { C } \displaystyle \sum _ { n = 5 4 1 } ^ { \infty } \Delta g _ { n } ) \frac { \mathcal { S } ( \rho , \psi ) } { \partial \mathrm { p } } \mathrm { d } \omega } \\ & { + \displaystyle \int _ { 0 \psi _ { \downarrow } } ^ { 2 \psi _ { \downarrow } } \mathrm { C } \displaystyle \sum _ { n = 1 8 1 } ^ { \infty } \Delta g _ { n } ) \frac { \mathcal { S } ( \rho , \psi ) } { \partial \mathrm { p } } \mathrm { d } \omega + \displaystyle \int _ { 0 \psi _ { \downarrow } } ^ { 2 \psi _ { \downarrow } } \mathrm { C } \displaystyle \sum _ { n = 3 \tau } ^ { \infty } \Delta g _ { n } ) \frac { \mathcal { S } ( \rho , \psi ) } { \partial \mathrm { p } } \mathrm { d } \omega ) } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \displaystyle \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \end{array}
$$

它又可以改写为如下的形式：

$$
\begin{array} { r l } & { \hat { \delta } _ { \rho } ^ { * } = \displaystyle \frac { \mathrm { R } ^ { 2 } } { 4 \pi } \mathcal { ( } \displaystyle { \int } _ { 0 } ^ { \pi \pi } ( \displaystyle { \sum _ { n = 1 0 8 0 1 } ^ { \infty } \Delta \mathrm { g } _ { \mathrm { n } } ) } \frac { \partial \mathrm { S } ( \rho , \phi ) } { \partial \boldsymbol { \theta } } \mathrm { d } \omega + \displaystyle { \int } _ { 0 } ^ { \pi \pi } ( \displaystyle { \sum _ { n = 2 1 6 1 } ^ { \infty } \Delta \mathrm { g } _ { \mathrm { n } } } ) \frac { \partial \mathrm { S } ( \rho , \phi ) } { \partial \boldsymbol { \theta } } \mathrm { d } \omega + \displaystyle { \int } _ { 0 } ^ { 2 \pi \pi } \Delta \mathrm { g } _ { \mathrm { n } } ) \frac { \partial \mathrm { S } ( \rho , \phi ) } { \partial \boldsymbol { \theta } } } \\ & { \quad \quad \quad + \displaystyle { \int } _ { 0 } ^ { 2 \pi } ( \displaystyle { \sum _ { n = 1 8 1 } ^ { \infty } \Delta \mathrm { g } _ { \mathrm { n } } } ) \frac { \partial \mathrm { S } ( \rho , \phi ) } { \partial \boldsymbol { \theta } } \mathrm { d } \omega + \displaystyle { \int } _ { 0 \psi _ { 4 } } ^ { 2 \pi } ( \displaystyle { \sum _ { n = 3 7 } ^ { \infty } \Delta \mathrm { g } _ { \mathrm { n } } } ) \frac { \partial \mathrm { S } ( \rho , \psi ) } { \partial \boldsymbol { \phi } } \mathrm { d } \omega ) . } \end{array}
$$

依据球函数知识[+有

$$
\int _ { 0 } ^ { 2 \pi } \Delta { \bf g } _ { \mathrm { n } } \mathrm { d } \alpha = 2 \pi ( \Delta { \bf g } _ { \mathrm { n } } ) _ { \mathrm { 0 } } { \bf P } _ { \mathrm { n } } ( \mathrm { c o s } \psi )
$$

式中（△g)。是以计算点的球面坐标(q,)算得的n阶重力异常的数值。因此,由(14·27)式可得

$$
\begin{array} { l } { { \displaystyle \tilde { \mathfrak { d } } _ { \rho } ^ { \prime } = \sum _ { \mathfrak { n } = 1 0 \nu \cup \Omega } ^ { \infty } ( \frac { \mathfrak { n } + 1 } { \mathfrak { n } - 1 } ) ( \frac { \mathbb { R } } { \rho } ) ^ { \mathfrak { n } + 2 } ( \Delta \mathbf { g } _ { \mathfrak { n } } ) _ { \mathfrak { o } } + \frac { \mathbb { R } ^ { 2 } } { 2 } \big [ \sum _ { \mathfrak { n } = 2 1 \mathfrak { o } 1 } ^ { \infty } ( \triangle \mathbf { g } _ { \mathfrak { n } } ) _ { \mathfrak { o } } \mathrm { K } _ { \mathfrak { n } } ( \rho , \phi _ { 1 } ) } \ ~ }  \\ { { \displaystyle \quad ~ + \sum _ { \mathfrak { n } = 5 4 1 } ^ { \infty } ( \Delta \mathbf { g } _ { \mathfrak { n } } ) _ { \mathfrak { o } } \mathrm { K } _ { \mathfrak { n } } ( \rho , \phi _ { 2 } ) + \sum _ { \mathfrak { n } = 1 8 1 } ^ { \infty } ( \triangle \mathbf { g } _ { \mathfrak { n } } ) _ { \mathfrak { o } } \mathrm { K } _ { \mathfrak { n } } ( \rho , \phi _ { 3 } ) + \sum _ { \mathfrak { n } = 3 7 } ^ { \infty } ( \triangle \mathbf { g } _ { \mathfrak { n } } ) _ { \mathfrak { o } } \mathrm { K } _ { \mathfrak { n } } ( \rho , \phi _ { 4 } ) \beth } \ ~ } \end{array}
$$

式中

$$
\mathbf { K } _ { \mathfrak { n } } ( \mathfrak { n } , \psi _ { \mathfrak { i } } ) = \int _ { \psi _ { \mathfrak { i } } } ^ { \mathfrak { x } } \frac { \partial \mathbf { S } ( \rho , \psi ) } { \partial \mathfrak { p } } \mathbf { P } _ { \mathfrak { n } } ( \mathrm { c o s } \psi ) \mathrm { s i n } \psi \mathrm { d } \psi \quad ( \mathrm { i } = 1 , 2 , 3 , 4 )
$$

取球面（半径为 $\pmb { \rho } .$ 上的均方值，以 $\pmb { \sigma } _ { \pmb { \rho } } ^ { 2 }$ 表示之，则得

$$
\begin{array} { l } { { \displaystyle \sigma _ { \rho } ^ { 2 } = \mathbf { M } \{ ( \widetilde { \mathbf { \Gamma } } \widetilde { \mathbf { \otimes } } _ { \rho } ^ { \prime } ) ^ { 2 } \} ~ = ~ \overset { \mathrm { s o } } { \sum } ~ ( \frac { \mathbf { n } + 1 } { \mathbf { n } - 1 } ) ^ { 2 } ( \frac { \mathbf { R } } { \rho } ) ^ { 2 \mathrm { n } + 4 }  { \boldsymbol { \mathrm { C } } } _ { \mathrm { n } } + \frac { \mathbf { R } ^ { 4 } } { 4 }  { \boldsymbol { \mathrm { C } } } _ { \mathrm { n } \approx 2 1 6 1 } ^ { \mathrm { } }  { \boldsymbol { \mathrm { C } } } _ { \mathrm { n } }  { \mathbf { K } } _ { \mathrm { n } } ^ { 2 } ( \rho , \phi _ { 1 } ) } \ ~ } \\ { { \displaystyle ~ + ~ \sum _ { \mathrm { n } = 5 4 1 } ^ { \infty }  { \boldsymbol { \mathrm { C } } } _ { \mathrm { n } }  { \mathbf { K } } _ { \mathrm { n } } ^ { 2 } ( \rho , \phi _ { 2 } ) + \sum _ { \mathrm { n } = 1 8 1 } ^ { \infty }  { \boldsymbol { \mathrm { C } } } _ { \mathrm { n } }  { \mathbf { K } } _ { \mathrm { n } } ^ { 2 } ( \rho , \phi _ { 3 } ) + \sum _ { \mathrm { n } = 3 7 } ^ { \infty }  { \boldsymbol { \mathrm { C } } } _ { \mathrm { n } }  { \mathbf { K } } _ { \mathrm { n } } ^ { 2 } ( \rho , \phi _ { 4 } ) ] } } \end{array}
$$

由此可见，可以用重力异常的阶方差C的模型来估算误差的大小。表14.2中给出了在几个高度上取相应的值所算得的结果。表中最后--栏的数值表明，按表中所示的各种网格的范围进行计算，由于数据不充分所引起的误差是可以忽略的。

表14.2  

<table><tr><td>范 网 格 围 大 半 小</td><td rowspan="3">1&#x27;×1&#x27;</td><td rowspan="3">5&#x27;×5&#x27;</td><td rowspan="3"></td><td rowspan="3">1°×1°</td><td rowspan="3">位系数模型</td><td rowspan="3">op毫伽</td></tr><tr><td>径 计算点</td><td>20&#x27;×20&#x27;</td></tr><tr><td>高 度 1km</td><td>2°</td></tr><tr><td></td><td rowspan="3">3</td><td rowspan="3">50&#x27; 50&#x27;</td><td rowspan="3">2 2</td><td>8</td><td>N=36</td><td>1.0</td></tr><tr><td>5</td><td>8</td><td>N=36</td><td>0.8</td></tr><tr><td>30</td><td>8°</td><td>N=36</td><td>0.6</td></tr><tr><td>100</td><td></td><td></td><td></td><td>8</td><td>N= 36</td><td>0.4</td></tr><tr><td>500</td><td></td><td></td><td></td><td></td><td>N= 36</td><td>0.3</td></tr></table>

# S14.4局部扰动重力场的点质量模型

在第七章中讲到，扰动重力场就是扰动质量的引力场。如果扰动质量的形体和密度分布都很简单，则可利用万有引力定律计算扰动位。但实际上扰动质量的形体很不规则，同时密度分布很复杂，因此根本不可能应用万有引力定律来推求实际的扰动位。然而，理论分析表明，把扰动质量简单地看成一大群离散的、位置和质量都是已知的质点，以这些质点的引力场作为实际局部扰动重力场的近似，在实用上还是很有意义的。

![](images/c320137149359d22e986cdf4d1fb1b35c63397fc0c79387aba0644f04fa499fd.jpg)  
图14.3

现假定扰动质量为m个扰动质点，它们离散地分布于地下，则地面外任一点P的扰动位可以简单地用万有引力定律算出，即

$$
\mathrm { { T } _ { \mathrm { { P } } } = f \sum _ { i = 1 } ^ { m } \frac { M _ { j } } { \partial \mathbf { r } _ { j } } }
$$

式中 $\mathbf { M } _ { \mathrm { j } }$ 为第 $\dot { \bf j }$ 个扰动质点的质量， $\mathbf { r } _ { \mathrm { j } }$ 为第 $\mathbf { j }$ 个点质量至 $\mathrm { \sf P }$ 点的距离。下面将证明：如果由 $\mathbf { m }$ 个点质量算得的地面重力异常值与实际观测值完全一致的话，则由 $( 1 4 \cdot 3 2 )$ 式算得的扰动位与按司托克斯公式 $( 8 \cdot 1 9 )$ 求得的扰动位值完全相等。

如图14:3所示,假定地面Σ是半径为R的球面，点质量M;与地心的距离为R;,则Σ面上任意点i的重力异常 $\Delta _ { \tt B i }$ 可按下式求得：

$$
\Delta \mathbf { g } _ { \mathrm { i } } { = } \mathbf { \vec { f } } \ \sum _ { \mathrm { i = 1 } } ^ { \mathrm { m } } ( \frac { \mathrm { R - } \mathrm { R } _ { \mathrm { j } } \mathrm { c o s } \psi _ { \mathrm { i j } } } { \mathbf { r } _ { \mathrm { i j } } ^ { 3 } } - \frac { 2 } { \mathrm { R } \mathbf { r } _ { \mathrm { i j } } } ) \mathbf { M } _ { \mathrm { j } }
$$

式中 $\mathbf { r _ { i j } }$ 和 $\psi _ { \mathrm { i j } }$ 分别为点质量 $\mathbf { M } _ { \mathrm { j } }$ 和 $\mathbf { i }$ 点之间的距离和球心角距。因为

$$
\frac { 1 } { { \bf r } _ { \mathrm { i j } } } = \sum _ { { \bf n } = 0 } ^ { \infty } \frac { { \bf R } _ { \mathrm { j } } ^ { \mathrm { n } } } { { \bf R } ^ { \mathrm { n + l } } } { \bf P } _ { \mathrm { n } } ( \cos \psi _ { \mathrm { i j } } )
$$

而

$$
\frac { \mathrm { R } - \mathrm { R } _ { \mathrm { j } } \mathrm { c o s } \psi _ { \mathrm { i j } } } { \mathrm { r } _ { \mathrm { i j } } } = \sum _ { \mathrm { n } = 0 } \frac { ( \mathrm { n } + 1 ) \mathrm { R } _ { \mathrm { j } } ^ { \mathrm { n } } } { \mathrm { R } ^ { \mathrm { n } + 2 } } \mathrm { P } _ { \mathrm { n } } ( \mathrm { c o s } \psi _ { \mathrm { i j } } )
$$

因此, $( 1 4 \cdot 3 3 )$ 式又可写为

$$
\Delta \mathbf { g } _ { \mathrm { i } } = \mathbf { f } \sum _ { \mathrm { i = 1 } } ^ { \mathrm { m } } \mathbf { M } _ { \mathrm { i } } \sum _ { \mathbf { n } = 0 } ^ { \infty } \mathbf { \frac { ( \mathbf { n } - \mathbf { \nabla } 1 ) \mathbf { R } _ { \mathrm { j } } ^ { \mathrm { n } } } { \mathbf { R } ^ { \mathrm { n } + 2 } } } \mathbf { P } _ { \mathrm { n } } ( \cos \psi _ { \mathrm { i j } } )
$$

将 $( 1 4 \cdot 3 4 )$ 式代入(8.19)式，得到

$$
\mathrm { T } _ { \mathrm { P } } = \mathrm { f } \sum _ { \mathrm { j = 1 } } ^ { \infty } \mathbf { M } _ { \mathrm { i } } \frac { 1 } { 4 \pi } \iint \sum _ { \mathrm { n } = 0 } ^ { \infty } \frac { ( \mathbf { n } - 1 ) \mathbf { R } _ { \mathrm { j } } ^ { \mathrm { s } } } { \mathbf { R } ^ { \mathrm { n } + 2 } } \mathrm { P } _ { \mathrm { n } } ( \cos \psi _ { \mathrm { i } } ) \sum _ { \mathrm { n } = 2 } ^ { \infty } \frac { 2 \mathbf { n } + 1 } { \mathbf { n } - 1 } \frac { \mathrm { R } ^ { \mathrm { n } } } { \rho ^ { \mathrm { n } + 1 } } \mathrm { P } _ { \mathrm { n } } ( \cos \psi ) \mathrm { d } \boldsymbol { \Sigma }
$$

式中 $\boldsymbol { \psi }$ 为 $\mathbf { i }$ 点与 $\mathbf { P }$ 点的球心角距。依据球函数的加法定理有

$$
\mathrm { P _ { n } } ( \mathrm { c o s } \psi ) = \mathrm { P _ { n } } ( \mathrm { c o s } \psi _ { \mathrm { i } } ) \mathrm { P _ { n } } ( \mathrm { c o s } \psi _ { \mathrm { i } } ) + 2 \sum _ { \mathrm { k = 1 } } ^ { \mathrm { n } } \frac { ( \mathrm { n - k } ) ! } { ( \mathrm { n + k } ) ! } \mathrm { P _ { n k } } ( \mathrm { c o s } \psi _ { \mathrm { i } } ) \mathrm { P _ { n k } } ( \mathrm { c o s } \psi _ { \mathrm { i } } ) \mathrm { c o s } \mathrm { k } a
$$

$\pmb { \alpha }$ 的含意见图14.3。将该式代入 $( 1 4 \cdot 3 5 )$ 式，在积分中 $\psi _ { \mathrm { j } }$ 是不变的，再利用球函数的正交性，最后得到

$$
{ \bf { T } } _ { \mathrm { { P } } } = \mathrm { { f } } \sum _ { \mathrm { { i } = 1 } } ^ { \mathrm { { m } } } { \bf { M } } _ { \mathrm { { i } } } \sum _ { \mathrm { { n } } = 0 } ^ { \infty } { \frac { { \bf { R } } _ { \mathrm { { j } } } ^ { \mathrm { { n } } } } { { { \ p ^ { \mathrm { { n } } + 1 } } } } } { \bf { P } } _ { \mathrm { { n } } } \left( \cos \psi \mathrm { { s j } } \right)
$$

因为后一求和号就是 $1 / \mathfrak { r } _ { \mathrm { j } }$ 。因此， $( 1 4 \cdot 3 6 )$ 式与 $( 1 4 \cdot 3 2 )$ 式是完全一致的。

由此可见，扰动重力场可以用埋藏在地球内部的一群离散的扰动质点所产生的引力场来替代,这就是所谓的扰动重力场的点质量模型。扰动质点的质量可以根据地面上已知的重力异常值来推求。如果在地面上已知 $\mathbf { n }$ 个点的重力异常值,则对于每一个异常值可以组成一个类似于(14·33)式的方程,其中的未知量是Mj,j=1、2、、cm。当方程的个数n大于或等于m时，就可解出所有质点的质量。

扰动重力场的点质量模型,可以用于计算扰动重力场中的其他元素：垂线偏差、高程异常和扰动重力等。例如，由 $( 1 4 \cdot 3 2 )$ 式可以很容易导出计算扰动重力三分量的公式为

$$
\left. \begin{array} { l } { { \displaystyle \hat { \delta } _ { \rho } = - \mathrm {  ~ f ~ } \sum _ { \mathrm { i } = 1 } ^ { m } ( \frac { \rho - \mathrm {  ~ \cal ~ R } _ { \mathrm { j } } \cos \psi _ { \mathrm { j } } } { \tau _ { \mathrm { j } } ^ { 3 } } ) { \bf M } _ { \mathrm { j } } } } \\ { { \displaystyle \hat { \delta } _ { \phi } = \mathrm {  ~ f ~ } \sum _ { \mathrm { i } = 1 } ^ { m } \frac { \sin \psi _ { \mathrm { j } } } { \tau _ { \mathrm { j } } ^ { 3 } } \cos \alpha _ { \mathrm { j } } { \bf M } _ { \mathrm { j } } } } \\ { { \displaystyle \hat { \delta } _ { \mathrm { a } } = \mathrm {  ~ f ~ } \sum _ { \mathrm { i } = 1 } ^ { m } \frac { \sin \psi _ { \mathrm { j } } } { \tau _ { \mathrm { j } } ^ { 3 } } \cos \alpha _ { \mathrm { j } } { \bf M } _ { \mathrm { j } } } } \end{array} \right\}
$$

式中

$$
\mathbf { r } _ { \mathrm { i } } ^ { 2 } = \rho ^ { 2 } + \mathbf { R } _ { \mathrm { j } } ^ { 2 } - 2 \rho \mathbf { R } _ { \mathrm { j } } \cos \psi _ { \mathrm { j } }
$$

${ \pmb { a } } _ { \mathrm { j } }$ 为以计算点的北方向起算的质点 $\mathbf { M } _ { \mathrm { j } }$ 的方位角。 $\psi _ { \mathrm { i } }$ 和 $\alpha _ { \mathrm { j } }$ 可由计算点 $\mathbf { P }$ 和扰动质点 $\mathbb { M } _ { \mathrm { j } }$ 的地心经纬度 $( 4 0 , 2 , )$ 和 $( \varphi _ { \mathrm { j } } , \lambda _ { \mathrm { j } } )$ 按下列公式求得

$$
\begin{array} { l } { { \mathrm { c o s } \emptyset _ { \mathrm { i } } { = } \mathrm { s i n } \varphi _ { \mathrm { { s } } } \mathrm { s i n } \varphi _ { \mathrm { { i } } } { + } \mathrm { c o s } \varphi _ { \mathrm { { \circ } } } \mathrm { c o s } \varphi _ { \mathrm { { j } } } \mathrm { c o s } \left( \lambda _ { \mathrm { { j } } } { - } \lambda _ { \mathrm { { \circ } } } \right) } } \\ { { \mathrm { s i n } \alpha _ { \mathrm { { i } } } { = } \mathrm { c o s } \varphi _ { \mathrm { { j } } } \mathrm { s i n } \left( \lambda _ { \mathrm { { j } } } { - } \lambda _ { \mathrm { { o } } } \right) / \mathrm { s i n } \psi _ { \mathrm { { j } } } } } \end{array}
$$

将 $( 1 4 \cdot 3 7 )$ 与 $( 1 4 \cdot 2 3 )$ 式相比较，可以看出用扰动质点计算，公式简单，因而用的计算时间要少很多。

用点质量模型来逼近实际的扰动重力场，其精确程度主要取决于质点的数量。如果只用稀少的扰动质点，则只能描绘出较为平缓的扰动重力场，不能将复杂重力场的细微变化表征出来。所以，应根据其用途和所要达到的精度来确定相应的点质量数目。但质点数目又不能大于用于解算的已知重力异常的数目，否则就无法答解点质量。因此，一般情况下，总是采用质点数与使用的观测值数目相等，以精确再现观测值，使之不因采用点质量模型而降低精度。

当采用积分方法计算扰动重力场中的各种元素时，总是在计算点周围不同范围内使用大小不等的网格的平均异常值,例如 $1 ^ { \circ } \times 1 ^ { \circ } , 2 0 ^ { \prime } \times 2 0 ^ { \prime }$ 和 $5 ^ { \prime } \times 5 ^ { \prime }$ 网格的平均异常。因此，可以根据这些数据分别建立几层相应的扰动质点，每层点质量分别表征扰动场的不同频率部份，叠加起来构成一个完整的点质量模型，见图14.4。

相应于 $1 ^ { \circ } \times 1 ^ { \circ }$ 平均异常的质点，都埋藏在每个 $1 ^ { \circ } \times 1 ^ { \circ }$ 网格中点的下方；相应于 $2 0 ^ { \prime } \times 2 0 ^ { \prime }$ 平均异常的质点，都埋藏在每个 $2 0 ^ { \prime } \times 2 0 ^ { \prime }$ 网格中点的下方；相应于 $5 ^ { \prime } \times 5 ^ { \prime }$ 平均异常的质点，都埋藏在每个 ${ \mathfrak { s } } ^ { \prime } \times { \mathfrak { s } } ^ { \prime }$ 网格中点的下方。质点的埋藏深度与点质量求解时的系数矩阵密切相关，深度过大将导致解的不稳定。如果深度太浅，会使点质量主要受与点质量相距很近的少数观测值的支配。实际上,深度的变化在效果上相当于求解时对观测值加以不同的权。经验表明，一般采用与质点间距大致相等的深度比较合适。因此， $1 ^ { \circ } \times 1 ^ { \circ }$ 点质量的埋藏深度可以取 $1 0 0 \mathbf { k } \mathbf { m }$ 左右 $\mathbf { \nabla } 2 0 ^ { \prime } \times 2 0 ^ { \prime }$ 点质量的埋藏深度可以取 $4 0  { \mathrm { k m } }$ 左右； $5 ^ { \prime } \times 5 ^ { \prime }$ 点质量的埋藏深度可以取 $1 0 \mathbf { k } \mathbf { m }$ 左右。

从实用的角度考虑，可以先选取一个低阶（如 $N { = } 3 6 $ 重力场模型作为参考场，以其与实际扰动场的残差构成残差点质量模型。构成残差点质量型的过程是：

1.将每个 $1 ^ { \circ } \times 1 ^ { \circ }$ 网格的平均异常减去用重力场模型算得的本 $1 ^ { \circ } \times 1 ^ { \circ }$ 网格中点的 $\Delta \mathbf { g } _ { \mathrm { s } }$ 值，解算出相应于 $1 ^ { \circ } \times 1 ^ { \circ }$ 平均异常的那组点质量 $\mathbf { M } _ { 1 ^ { \circ } \times 1 ^ { \circ } }$ ；

2.将每个 $2 0 ^ { \prime } \times 2 0 ^ { \prime }$ 网格的平均异常减去用重力场模型和 $\mathbf { M } _ { 1 ^ { \circ } \times 1 ^ { \circ } }$ 算得的本 $2 0 ^ { \prime } \times 2 0 ^ { \prime }$ 网格中点的 $\Delta \mathbf { g } .$ 值和 $\Delta _ { \tt B M _ { \mathrm { 1 ^ { * } \times \mathrm { 1 ^ { * } } } } }$ ,以这组残差重力异常解算出相应于 $2 0 ^ { \prime } \times 2 0 ^ { \prime }$ 网格平均异常的那组点质量 $\mathbf { M } _ { 2 0 ^ { \prime } \times 2 0 ^ { \prime } }$ ；

3.将每个 $5 ^ { \prime } \times 5 ^ { \prime }$ 网格的平均异常减去用重力场模型和 $\mathbf { M } _ { 1 ^ { \circ } , 1 ^ { \circ } , 1 } \mathbf { M } _ { 2 ^ { \prime } , 1 ^ { \prime } ; 2 , 0 ^ { \prime } }$ 算得的本 $5 ^ { \prime } \times 5 ^ { \prime }$ 网格中点的 $\Delta \mathbf { g } ,$ 值和 $\Delta \mathbf { g } _ { \mathrm { M } _ { 1 } \bullet _ { \times 1 } \bullet } \Delta \mathbf { g } _ { \mathrm { M } _ { 2 0 ^ { \prime } \times 2 0 ^ { \prime } } }$ ,用这组残差重力异常值解算出相应于 $5 ^ { \prime } \times 5 ^ { \prime }$ 网格平均异常的那组点质量 $\mathbf { M } _ { 5 ^ { \prime } \times 5 ^ { \prime } }$ 。

![](images/56a9d983d20371534c8a622d81e155fd9665ac85d9b0263ab7cad525fa0d0658.jpg)  
图14.4

利用上述这组残差点质量模型连同参考场一起计算外部点扰动重力三分量的公式为：

$$
\begin{array} { l } { \displaystyle \frac { [ \mathbf { M } } { \rho ^ { 2 } } \sum _ { n = 2 } ^ { \infty } ( \mathrm { n } + 1 ) ( \frac { \mathbb { R } } { \rho } ) ^ { n } \sum _ { m = 0 } ^ { n } ( \overline { { C } } _ { \mathrm { s m } } ^ { * } \mathrm { c o s m } \lambda _ { 0 } + \overline { { S } } _ { \mathrm { n m } } \mathrm { s i n m } \lambda _ { 0 } ) \overline { { \mathrm { p } } } _ { \mathrm { n m } } ( \mathrm { s i n } \varphi _ { 0 } ) - \displaystyle \int _ { \mathrm { i } = 1 } ^ { \infty } ( \frac { \rho - \mathrm { R } , \mathrm { c o s } \psi _ { j } } { \mathrm { r } _ { i } ^ { 3 } } ) \mathbf { M } _ { i } } \\ { \displaystyle - \frac { \mathrm { f M } } { \rho ^ { 2 } } \sum _ { n = 2 } ^ { \infty } ( \frac { \mathrm { R } } { \rho } ) ^ { n } \sum _ { m = 0 } ^ { n } ( \overline { { C } } _ { \mathrm { s m } } ^ { * } \mathrm { c o s m } \lambda _ { 0 } + \overline { { S } } _ { \mathrm { n m } } \mathrm { s i n m } \lambda _ { 0 } ) ( \mathrm { \zeta } \frac { \mathrm { d } \overline { { \mathrm { F } } } _ { \mathrm { n m } } ( \mathrm { s i n } \varphi ) } { \mathrm { d } \varphi } ) _ { \mathrm { \zeta } \mathrm { e v } _ { 0 } } + \mathrm { f } \sum _ { \mathrm { i } = 1 } ^ { \infty } \frac { \mathrm { s i n } \psi _ { j } } { \mathrm { r } _ { i } ^ { 3 } } \mathrm { c o s } \alpha _ { i } \mathbf { M } _ { i } } \\  \displaystyle \frac { \mathrm { f M } } { \mathrm { \varepsilon ^ { 2 } } \mathrm { c o s } \varphi _ { 0 } } \sum _ { n = 2 } ^ { \infty } ( \frac { \mathrm { R } } { \rho } ) ^ { n } \sum _ { \mathrm { n = 0 } } ^ { n } ( \overline { { C } } _ { \mathrm { s m } } ^ { * } \mathrm { s i n m } \lambda _ { 0 } - \overline { { S } } _ { \mathrm { n m } } \mathrm { c o s m } \lambda _ { \mathrm { o } } ) \overline { { \mathrm { P } } } _ { \mathrm { n m } } ( \mathrm { s i n } \varphi _ { 0 } ) + \mathrm { f } \sum _ { \mathrm { i } = 1 } ^ { n } \frac { \mathrm { s i n } \bar { \psi } _ { i } }  \mathrm { r } _ { i } ^  \end{array}
$$

式中 $\mathbf { M } _ { \mathrm { j } }$ 为第j个点质量，它包括了三种点质量； $\mathtt { R } _ { \mathrm { j } }$ 可由地球平均半径 $\mathbf { R }$ 减去埋藏深度求得。

由于采用的是分层残差点质量模型，较浅的点质量层代表了扰动重力场的较短波长部分，故可以随着计算点高度的增加逐步舍弃浅层的点质量。从一些试算数据表明，在 $3 0 \mathbf { k m }$ 以上的高度可舍去 $5 ^ { \prime } \times 5 ^ { \prime }$ 的点质量层，至 $\bf { 2 0 0 k m }$ 以上的高度可舍去 $2 0 ^ { \prime } \times 2 0 ^ { \prime }$ 的点质量层，在 $5 0 0 \mathbf { k m }$ 以上的高度还可舍去 $1 ^ { \circ } \times 1 ^ { \circ }$ 的点质量层。由此而造成的影响小于毫伽。

综上所述，应用残差点质量模型和参考场--起计算扰动重力三分量，与单纯用重力场模型相比精度有所提高，而与司托克斯积分法相比计算时间可以缩短,因此很有实用价值。

# 14.5利用单层密度计算扰动重力

应用质体引力位的等值层原理，扰动质量对外部点的引力位也可以用地面上的一个单层所产生的引力位来代替，即

$$
\mathrm { T } _ { ( \rho , \varphi , \lambda ) } = \mathrm { f } \int _ { \Sigma } \frac { \dot { { \boldsymbol { x } } } } { \mathrm { ~ \boldsymbol { r } ~ } } \mathrm { d } \Sigma
$$

式中 $\updownarrow$ 为单层的密度。如果将地球视为球体，则 $\pmb { \Sigma }$ 就是半径为 $\mathbf { R }$ 的球面， $\dot { \pmb { \tau } }$ 为球面上的单元面积 $\mathbf { d } \pmb { \Sigma }$ 至计算点的距离，可参见图14.2。由 $( 1 4 \cdot \mathrm { \dot { 4 } 0 } )$ 式，通过求偏导数就可得到扰动重力的三分量，即

$$
\left. \begin{array} { l } { \displaystyle \hat { \otimes } _ { \rho } = \frac { \partial \Gamma } { \partial \rho } = \mathbf { f } \int \chi \frac { \partial } { \partial \rho } ( \frac { 1 } { \tau } ) \mathrm { d } \Sigma } \\ { \displaystyle \hat { \otimes } _ { \varphi } = \frac { \partial \Gamma } { \rho \partial \varphi } = \frac { \mathbf { f } } { \varrho } \int \chi \frac { \partial } { \partial \varphi } ( \frac { 1 } { \tau } ) \mathrm { d } \Sigma } \\ { \displaystyle \hat { \otimes } _ { \lambda } = \frac { \partial \Gamma } { \rho \mathrm { c o s } \varphi \partial \lambda } = \frac { \mathbf { f } } { \mathrm { p c o s } \varphi } \Bigg [ \mathbb { \mathbb { X } } \frac { \partial } { \partial \lambda } ( \frac { 1 } { \tau } ) \mathrm { d } \Sigma \Bigg ] } \end{array} \right\}
$$

与 $\ S 1 4 . 3$ 中相类似,由 $( 1 4 \cdot 1 6 )$ 式可以求得

$$
\begin{array} { r l } & { \frac { \partial } { \partial \boldsymbol { \rho } } ( \frac { 1 } { \tt { r } } ) = - \frac { \boldsymbol { \rho } - \mathrm { { R c o s } } \boldsymbol { \phi } } { { \tt r } ^ { 3 } } } \\ & { \frac { \check { \partial } } { \partial \boldsymbol { \phi } } ( \frac { 1 } { \tt { r } } ) = \frac { \boldsymbol { \rho } { \mathrm { R s i n } } \boldsymbol { \psi } } { { \tt r } ^ { 3 } } \mathrm { c o s } \alpha } \\ & { \frac { \partial } { \partial \boldsymbol { \lambda } } ( \frac { 1 } { \tt { r } } ) = \frac { \boldsymbol { \rho } { \mathrm { R s i n } } \boldsymbol { \psi } } { \tt r ^ { 3 } } \mathrm { s i n } \alpha \mathrm { c o s } \boldsymbol { \varphi } } \end{array}
$$

将它们代入 $( 1 4 \cdot 4 1 )$ 式，并令

$$
\mu { = } 2 \pi \mathrm { } \mathrm { } \mathrm { } \mathrm { } \chi
$$

得到计算扰动重力三分量的公式为

$$
\left. \begin{array} { l } { { \hat { \vartheta } _ { p } } = - \displaystyle \frac { 1 } { 2 \pi } { \displaystyle \int _ { \Sigma } } \mu \displaystyle \frac { \rho - { \bf R } \cos \psi } { { \bf r } ^ { 3 } } \mathrm { d } \Sigma } \\ { ~ { \hat { \vartheta } _ { \varphi } } = \displaystyle \frac { 1 } { 2 \pi } { \displaystyle \int _ { \Sigma } } \mu \displaystyle \frac { { \bf R } \sin \psi } { { \bf r } ^ { 3 } } \mathrm { c o s } \mathrm { d } \Sigma } \\ { { \hat { \vartheta } _ { \mathrm { s } } } = \displaystyle \frac { 1 } { 2 \pi } { \displaystyle \int _ { \Sigma } } \mu \displaystyle \frac { { \bf R } \sin \psi } { { \bf r } ^ { 3 } } \mathrm { s i n a d } \Sigma } \end{array} \right\}
$$

要利用(14·43)式计算扰动重力三分量，必需具备地面上的μ值。为此，需要导出由重力场观

值推求 $\pmb { \mu }$ 值的公式。

在.5中讲到，单层位的一阶外法线导数在通过层面时是不连续的，当以外部位推求时有

$$
\frac { \partial \boldsymbol { \mathrm { T } } } { \partial \boldsymbol { \mathrm { n } } } \vert = \boldsymbol { \mathrm { f } } \underset { \boldsymbol { \Sigma } } { \underbrace { \mathrm { \nabla } } } \times \frac { \partial } { \partial \boldsymbol { \mathrm { n } } } ( \frac { 1 } { \boldsymbol { \mathrm { \textbf { r } } } } ) \boldsymbol { \mathrm { d } } \boldsymbol { \Sigma } - 2 \pi \boldsymbol { \mathrm { f } } \boldsymbol { \times }
$$

$\pmb { \mathrm { n } }$ 表示外法线方向，因 $\pmb { \Sigma }$ 是球面，故 $\mathfrak { n }$ 方向与向径 $\pmb { \rho }$ 重合，故有

$$
\frac { \partial } { \partial \mathbf { n } } ( \frac { 1 } { \mathbf { r } } ) = \frac { \partial } { \partial \mathbf { p } } ( \frac { 1 } { \mathbf { r } } )
$$

而且在球面 $\pmb { \Sigma }$ 上又有 ${ \boldsymbol { \mathsf { P } } } { = } \mathbf { R }$ ,因此

$$
\frac { \partial } { \partial \mathbf { n } } ( \frac { 1 } { \mathbf { r } } ) \mid _ { \mathrm { z } } = - \frac { 1 } { 2 \mathbf { R } \mathbf { r } _ { \mathrm { 0 } } }
$$

其中 $\pmb { \tau _ { 0 } }$ 为 $\mathtt { d } \mathtt { \Sigma }$ 至求 $\pmb { \mu }$ 值点 $\mathbf { P } _ { 0 }$ 的直线距离。将它代入 $( 1 4 \cdot 4 4 )$ 式，并顾及(14.42)式，则得

$$
\frac { \partial \mathbf { T } } { \partial \mathbf { n } } | _ { \rho \to \mathtt { R } } = - \frac { \mathbf { T } _ { \mathtt { r } } } { 2 \mathbf { R } } - \mu
$$

$\boldsymbol { \Upsilon } _ { \mathfrak { L } }$ 为球面上的扰动位。因为球面上的重力异常 $\Delta \mathbf { g }$ 与扰动位的关系为

$$
( \frac { \partial \boldsymbol { \Gamma } } { \partial \boldsymbol { \mathfrak { p } } } + \frac { 2 } { \rho } \boldsymbol { \mathrm { T } } ) _ { \rho \circ \mathrm { { e } } } = - \Delta \mathbf { g }
$$

因此，由 $( 1 4 \cdot 4 5 )$ 式可得

$$
\mu { = } \Delta \mathbf { g } { + } \frac { 3 \mathrm { T } _ { \mathrm { z } } } { 2 \mathrm { R } } { = } \Delta \mathbf { g } { + } \frac { 3 \Upsilon } { 2 \mathrm { R } } \xi
$$

从 $( 1 4 \cdot 4 6 )$ 式看出，地面点除了有重力异常值，还需有高程异常 $\boldsymbol { \zeta }$ 的数值，才能求得它们的 $\mu$ 值。只要有了 $\mu$ 值，就可用 $( 1 4 \cdot 4 3 )$ 式推求扰动重力的三分量。

具体的计算方法可与 $\ S . 1 4 . 3$ 中只用重力异常计算扰动重力所用的方法相同，即利用全球的 $\pmb { \mu }$ 值球函数级数式和局部地区地面 $\pmb { \mu }$ 值的数据分两项计算，因此有

$$
\left. \begin{array} { l } { { \hat { \delta } _ { \rho } = ( \hat { \delta } _ { \rho } ) _ { \sf S } + ( \hat { \delta } _ { \rho } ) _ { \sf 0 } } } \\ { { \hat { \delta } _ { \varphi } = ( \hat { \delta } _ { \varphi } ) _ { \sf S } + ( \hat { \delta } _ { \varphi } ) _ { \sf 0 } } } \\ { { \hat { \delta } _ { \lambda } = ( \hat { \delta } _ { \lambda } ) _ { \sf S } + ( \hat { \delta } _ { \lambda } ) _ { \sf 0 } } } \end{array} \right\}
$$

其中

$$
\left. \begin{array} { l } { { ( \hat { \vartheta } _ { \rho } ) _ { \mathrm { s } } = - \displaystyle \frac { 1 } { 2 \pi } \Biggl [ \mu _ { \mathrm { s } } \displaystyle \frac { \rho - { \mathrm { R c o s } } \psi } { \mathrm { r } ^ { 3 } } \mathrm { d } \Sigma } } \\ { { \mathrm { } ( \hat { \vartheta } _ { \varphi } ) _ { \mathrm { s } } = \displaystyle \frac { 1 } { 2 \pi } \Biggl \{ \mu _ { \mathrm { s } } \displaystyle \frac { { \mathrm { R s i n } } \psi } { \mathrm { r } ^ { 3 } } \mathrm { c o s } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { } \mathrm { { } } } } \\ { { \mathrm { } ( \hat { \vartheta } \lambda ) _ { \mathrm { s } } = \displaystyle \frac { 1 } { 2 \pi } \Biggl \{ \mu _ { \mathrm { s } } \displaystyle \frac { { \mathrm { R s i n } } \psi } { \mathrm { r } ^ { 3 } } \mathrm { s i n } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } } } \end{array} \right\}
$$

和

$$
\left. \begin{array} { l } { { ( \hat { \vartheta } _ { p } ) _ { \mathfrak { q } } = - \displaystyle \frac { 1 } { 2 \pi } \sum _ { i } ( \overline { { \mu } } - \overline { { \mu } } _ { \mathrm { s } } ) _ { \mathrm { i } } \displaystyle \frac { \mathfrak { p } - \mathrm { R o s } \phi _ { \mathrm { i } } } { { \bf r } _ { \mathrm { i } } ^ { 3 } } \Delta \Sigma _ { \mathrm { i } } } } \\ { { ( \hat { \vartheta } _ { \mathfrak { p } } ) _ { \mathfrak { q } } = \displaystyle \frac { 1 } { 2 \pi } \sum _ { i ^ { \prime } } ( \overline { { \mu } } - \overline { { \mu } } _ { \mathrm { s } } ) _ { \mathrm { i } } \displaystyle \frac { \mathrm { R s i n } \psi _ { \mathrm { i } } } { { \bf r } _ { \mathrm { i } } ^ { 3 } } \mathrm { c o s } \alpha _ { \mathrm { i } } \Delta \Sigma _ { \mathrm { i } } } } \\ { { ( \hat { \vartheta } _ { \mathfrak { h } } ) _ { \mathfrak { q } } = \displaystyle \frac { 1 } { 2 \pi } \sum _ { i ^ { \prime } } ( \overline { { \mu } } - \overline { { \mu } } _ { \mathrm { s } } ) _ { \mathrm { i } } \displaystyle \frac { \mathrm { R s i n } \psi _ { \mathrm { i } } } { { \bf r } _ { \mathrm { i } } ^ { 3 } } \mathrm { s i n } \alpha _ { \mathrm { i } } \Delta \Sigma _ { \mathrm { i } } } } \end{array} \right\}
$$

式中 $\mu _ { S }$ 为用位系数模型算得的 $\mu$ 值。用 $( 1 0 \cdot 3 )$ 和 $( 7 0 \cdot 5 )$ 式代入 $( 1 4 \cdot 4 6 )$ 式，很容易得到这个级数式

$$
{ \mathfrak { s } } = \sum _ { n = 2 } ^ { \cdot ; } \mu _ { n }
$$

其中

$$
\mu _ { \mathrm { n } } = - \ \frac { \mathrm { f } \mathrm { M } } { \mathrm { R } ^ { 2 } } ( \mathrm { n } + \mathrm { \frac { ~ 1 } { ~ 2 ~ } } ) \sum _ { \mathrm { n } = 0 } ^ { \mathrm { n } } ( \overline { { \mathrm { C } } } _ { \mathrm { n } \mathrm { m } } ^ { \ast } \mathrm { c o s m } \lambda + \overline { { \mathrm { S } } } _ { \mathrm { n } \mathrm { m } } \mathrm { s i n } \mathrm { m } \lambda ) \overline { { \mathrm { P } } } _ { \mathrm { n } \mathrm { m } } ( \mathrm { s i n } \varphi )
$$

$( 1 \dot { 4 } \cdot 4 9 )$ 式中的其他符号的含意与在 $\$ 14.3$ 中的相同。

$( \delta _ { \mathfrak { p } } ) _ { \mathrm { s } } \ : . ( \delta _ { \mathfrak { p } } ) _ { \mathrm { s } }$ 和 $( \delta _ { \lambda } ) _ { \mathrm { s } }$ 的计算公式也可变为直接用位系数计算的形式，而不用 $( 1 4 \cdot 4 8 )$ 式。因为

$$
\frac { 1 } { \mathrm { r } } = \sum _ { n = 0 } ^ { \cdot \mathrm { v } } \frac { \mathrm { R } ^ { \mathrm { s } } } { \rho ^ { \mathrm { n } + 1 } } \mathrm { P } _ { \mathrm { u } } ( \mathsf { c o s } \psi )
$$

可以求得

$$
\frac { \partial } { \partial \rho } ( \frac { 1 } { \tau } ) = - \sum _ { \mathfrak { n } = \mathfrak { c } } ^ { \infty } ( : \mathfrak { n } + \mathfrak { i } ) \frac { \mathrm { R } ^ { \mathfrak { n } } } { \rho ^ { \mathfrak { n } \cdot \mathfrak { i } / 2 } } \mathbb { P } _ { \mathfrak { n } } ( \mathsf { c o s } \psi )
$$

$$
\overset { \vartriangle } { \underset { \boldsymbol { \hat { \boldsymbol { \Psi } } } } { \longrightarrow } } ( \frac { 1 } { \mathbf { r } } ) = \sum _ { \mathfrak { n } = \boldsymbol { \mathrm { f } } } ^ { \boldsymbol { \mathfrak { N } } } \frac { \mathbf { R } ^ { \mathfrak { n } } } { \boldsymbol { \rho } ^ { \mathfrak { n } + \frac { 1 } { \mathfrak { n } } } } \frac { \mathrm { d } \mathbf { P } _ { \mathfrak { n } } ( \cos \phi ) } { \mathrm { d } \psi }
$$

因此，由 $( 1 4 \cdot 4 1 )$ 式和 $( 1 4 ~ ^ { \circ } ~ 4 2 )$ 式可以得到

$$
\begin{array}{c} \begin{array} { l } { { ( \hat { \ 8 } _ { \rho } ) _ { \mathrm { s } } = + \displaystyle \frac { \mathrm { R } ^ { 2 } } { 2 \pi } \displaystyle \int \displaystyle \int \displaystyle \sum _ { 0 } ^ { \mathrm { x } } \mu _ { \mathrm { s } = 2 } ^ { \mathrm { s } } ( \mu _ { \mathrm { n } } \displaystyle \sum _ { \mathrm { \ell } = 0 } ^ { \infty } ( \mathrm { n } + 1 ) \displaystyle \frac { \mathrm { R } ^ { n } } { \rho ^ { n + 2 } } \mathrm { P } _ { \mathrm { n } } ( \mathrm { c o s } \phi ) \mathrm { s i n } \phi \mathrm { d } \psi \mathrm { d } \alpha } } \\ { { ( \hat { \ 8 } _ { \varphi } ) _ { \mathrm { s } } = - \displaystyle \frac { \mathrm { R } ^ { 2 } } { 2 \pi \rho } \displaystyle \int \displaystyle \int \displaystyle \sum _ { 0 } ^ { \mathrm { x } } \mu _ { \mathrm { n } = 2 } ^ { \mathrm { x } } \mu _ { \mathrm { n } } \displaystyle \sum _ { \mathrm { \ell } = 0 } ^ { \mathrm { x } } \frac { \mathrm { R } ^ { n } } { \rho ^ { n + 1 } } \displaystyle \frac { \mathrm { d } \mathrm { P } _ { \mathrm { n } } ( \mathrm { c o s } \phi ) } { \mathrm { d } \bar { \psi } } \mathrm { c o s } \alpha \mathrm { s i n } \phi \mathrm { d } \phi \mathrm { d } a } } \\ { { ( \hat { 8 } _ { \mathrm { s } } ) _ { \mathrm { s } } = - \displaystyle \frac { \mathrm { R } ^ { 2 } } { 2 \pi \rho } \displaystyle \int \displaystyle \sum _ { 0 } ^ { \mathrm { x } } \sum _ { \mathrm { \ell } = 1 } ^ { \mathrm { x } } \mu _ { \mathrm { n } = 2 } ^ { \mathrm { x } } \displaystyle \sum _ { \mathrm { \ell } = 0 } ^ { \mathrm { R } ^ { n } } \frac { \mathrm { d } \mathrm { P } _ { \mathrm { n } } ( \mathrm { c o s } \phi ) } { \mathrm { d } \bar { \psi } } \mathrm { s i n } \mathrm { a s i n } \phi \mathrm { d } \psi \mathrm { d } \alpha } } \end{array} \}   \end{array}
$$

因为

$$
\begin{array} { l } { \displaystyle \int _ { \tau } ^ { z } } \\ { \displaystyle \int _ { \tau _ { n } } \mathrm { d } z = 2 \pi ( \mu _ { n } ) _ { 0 } \mathrm { P } _ { n } ( \cos \psi ) } \\ { \displaystyle } \\ { \displaystyle \int _ { \tau } ^ { z } } \\ { \displaystyle \int _ { z } ^ { z } } \\ { \displaystyle \int _ { z } ^ { z } } \end{array}
$$

而

$$
\int \limits _ { 0 } ^ { \pi } [ \mathrm { P } _ { n } ( \cos \psi ) ] ^ { 2 } \sin \psi \mathrm { d } \psi = \frac { 2 } { 2 \mathrm { n } + 1 }
$$

$$
\int \limits _ { 0 } ^ { \pi } P _ { \mathrm { n l } } \left( \cos \phi \right) \frac { \mathrm { d } \mathrm { P } _ { \mathrm { n } } \left( \cos \phi \right) } { \mathrm { d } \phi } \sin \psi \mathrm { d } \dot { \varphi } = - \frac { 2 \mathrm { n } \left( \mathrm { n + 1 } \right) } { 2 \mathrm { n } + 1 }
$$

考虑到这些关系式，由 $( 1 4 \cdot 5 2 )$ 式可得

$$
\left. \begin{array} { l } { \displaystyle ( \delta _ { \mathfrak { p } } ) _ { \mathbb { s } } = \sum _ { \mathfrak { n } = 2 } ^ { \mathtt { N } } \frac { 2 ( \mathfrak { n } + 1 ) } { 2 \mathfrak { n } + 1 } ( \frac { \mathtt { R } } { \overline { { \rho } } } ) ^ { \mathfrak { n } + 2 } ( \mu _ { \mathfrak { n } } ) _ { \mathfrak { 0 } } } \\ { \displaystyle ( \delta _ { \mathfrak { e } } ) _ { \mathbb { s } } = - \sum _ { \mathfrak { n } = 2 } ^ { \mathtt { N } } \frac { 2 } { 2 \mathfrak { n } + 1 } ( \frac { \mathtt { R } } { \overline { { \rho } } } ) ^ { \mathfrak { n } + 2 } ( \frac { \partial \mu _ { \mathfrak { n } } } { \partial \overline { { \varphi } } } ) _ { \mathfrak { o } } } \\ { \displaystyle ( \delta _ { \mathfrak { a } } ) _ { \mathbb { s } } = - \sum _ { \mathfrak { n } = 2 } ^ { \mathtt { N } } \frac { 2 } { 2 \mathfrak { n } + 1 } ( \frac { \mathtt { R } } { \overline { { \rho } } } ) ^ { \mathfrak { n } + 2 } \frac { 1 } { \cos \varphi _ { \mathfrak { o } } } ( \frac { \partial \mu _ { \mathfrak { n } } } { \partial \mathtt { A } } ) _ { \mathfrak { o } } \Bigg \} } \end{array} \right. { , }
$$

$( 1 4 \cdot 5 3 )$ 式就是用 $\mu _ { n }$ 计算 $( \mathfrak { d } _ { \mathfrak { p } } ) _ { \mathbb { S } \mathfrak { d } } ( \mathfrak { d } _ { \mathfrak { p } } ) _ { \mathbb { S } }$ 和 $( \eth _ { \mathfrak { s } } ) _ { \mathfrak { s } }$ 的公式。实际上，它的结果应该与 $( 1 4 \cdot 1 0 )$ 式完全相同的。

# 14.6扰动重力的向上延拓

在第五章中导出了由球面上的调和函数值 $\mathbf { V } _ { ( \mathbf { R } , \Psi ^ { ' } , \lambda ^ { \prime } ) }$ 推求球外点 $\ P _ { ( p , \psi , \lambda ) }$ 的调和函数的公式，即布桑积分 $( 5 \cdot 9 9 )$ 式

$$
\operatorname { V } _ { \{ \boldsymbol { \rho } , \boldsymbol { \Psi } , \boldsymbol { \lambda } \} } = \frac { \rho ^ { 2 } - \operatorname { R } ^ { 2 } } { 4 \pi \operatorname { R } } \iint _ { \boldsymbol { \sigma } } \frac { \operatorname { V } \left( \operatorname { R } , \varphi ^ { \prime } \cdot \lambda ^ { \prime } \right) } { \operatorname { \mathbf { r } } ^ { 3 } } \mathrm { d } \boldsymbol { \sigma }
$$

由于积分核 $\frac { 1 } { { \mathfrak { r } } ^ { 3 } }$ 随与 $\mathbf { P }$ 点的距离的增大而很快衰减，故在点的高程 $\scriptstyle { \mathrm { H } } = \rho - { \mathrm { R } }$ 不甚大的情况下（如 $1 0 0 \mathbf { k m }$ 以下)积分区域只需取很小的范围(10倍 $\mathbf { H }$ )，以致于可以看成平面。考虑到

$$
\rho ^ { 2 } - \mathbb { R } ^ { 2 } = \left( \rho + \mathbb { R } \right) \left( \rho - \mathbb { R } \right) \approx 2 \mathbb { R } \mathbb { H }
$$

由 $( 1 4 \cdot 5 4 )$ 式可得

$$
\mathbf { V } _ { ( \boldsymbol { \mathfrak { n } } , \boldsymbol { \mathfrak { o } } , \mathrm { H } ) } { = } \frac { \mathrm { H } } { 2 \pi } \iint \frac { \mathbf { V } _ { ( \mathbf { x } , \mathbf { y } ) } } { \mathbf { r } ^ { 3 } } \mathrm { d } \mathbf { x } \mathrm { d } \mathbf { y }
$$

式中的符号含意如图14.5所示。 $\mathrm { { P _ { \mathrm { { \Phi } } } } } _ { \mathrm { { \Phi } } }$ 点为 $\mathbf { P }$ 的向径与球面的交点， $\pmb { \Sigma }$ 面为过 $\mathbf { P } _ { 0 }$ 点所作的球的切平面；以 $\mathbf { P } _ { 0 }$ 为原点设置三维直角坐标，Z轴与 $\Sigma$ 面正交，X轴指北，Y轴指东。 $( 1 4 \cdot 5 5 )$ 式就是平面情况下的布桑积分，用它可以由面上的调和函数值推求面外的调和函数，式中

![](images/1fe8077b884c51e627217fafa53659785f25fb09ebac24d46bc2393cd8c9337a.jpg)  
图14.5

$$
\mathbf { r } = \sqrt { \mathbf { x } ^ { 2 } + \mathbf { y } ^ { 2 } + \mathbf { H } ^ { 2 } }
$$

扰动位在外空间是个调和函数。依据调和函数的性质，扰动重力的三分量δ= $\widetilde { \delta } _ { \mathrm { x } } = \frac { \partial \mathrm { T } } { \partial \mathbf { x } } \cdot \widetilde { \partial } _ { \mathrm { y } } = \frac { \partial \mathrm { T } } { \partial \mathbf { y } }$ 和8= 也都是调和函数。因此，由 $( 1 4 ~ \cdot ~ 5 5 )$ 式可得

$$
\left. \begin{array} { l } { \displaystyle \hat { \delta } _ { \mathbf x } = \frac { \mathrm { H } } { 2 \pi } \underline { { \iint } } \frac { \hat { \partial } _ { \mathbf x } ( \mathbf x , \mathbf y ) } { \mathbf r ^ { 3 } } \mathrm { d } \mathbf x \mathrm d \mathbf y } \\ { \displaystyle \hat { \partial } _ { \mathbf y } = \frac { \mathrm { H } } { 2 \pi } \underline { { \iint } } \frac { \hat { \partial } _ { \mathbf y } ( \mathbf x , \mathbf y ) } { \mathbf r ^ { 3 } } \mathrm { d } \mathbf x \mathrm d \mathbf y } \\ { \displaystyle \hat { \partial } _ { \mathbf z } = \frac { \mathrm { H } } { 2 \pi } \underset { \mathbf z } { \underbrace { \iint } } \frac { \hat { \partial } _ { \mathbf z } ( \mathbf x , \mathbf y ) } { \mathbf r ^ { 3 } } \mathrm { d } \mathbf x \mathrm d \mathbf y } \end{array} \right\}
$$

这就是扰动重力向上延拓的计算公式，它需要利用地面上已知的扰动重力三分量的数值。然而,它们并不能从观测得到，而是要通过扰动重力场中的其他元素算出。依据前面各章中的知识可得

$$
\left. \begin{array} { l } { \displaystyle \hat { \partial } _ { \mathbf { x } } = - \gamma \xi } \\ { \displaystyle \hat { \partial } _ { \mathbf { y } } = - \gamma \eta } \\ { \displaystyle \hat { \partial } _ { \mathbf { z } } = - \left( \Delta \mathbf { g } + \frac { 2 \gamma } { \mathrm { R } } \boldsymbol { \zeta } \right) } \end{array} \right\}
$$

这表明，垂直分量可以由重力异常和高程异常值推求，而水平分量则要用垂线偏差分量来推求。由于往往不具备大量的垂线偏差值，这使得很难将此公式用于实践。为此，下面将导出也用地面 $\mathfrak { d } _ { \mathfrak { z } }$ 计算 $\delta _ { * }$ 和 $\delta _ { \mathbf { y } }$ 的公式。

从 $( 1 4 \cdot 5 7 )$ 式中可以看出，在 $z$ 轴上扰动重力的两个水平分量 $\delta _ { \mathrm { s } }$ 和 $\mathfrak { d } _ { \mathfrak { y } }$ 都是所求点的Z坐标的函数，因此可以写出如下的关系式：

$$
\begin{array} { r } { ( \hat { \pmb { \theta } } _ { \mathbf { x } } ) _ { \mathrm { P } } = ( \hat { \pmb { \theta } } _ { \mathbf { x } } ) _ { \mathrm { P } _ { 0 } } + \displaystyle \int _ { 0 } ^ { \mathbb { H } } \frac { \partial \hat { \mathbf { x } } _ { \mathbf { x } } } { \partial z } \mathrm { d } z } \\ { ( \hat { \pmb { \theta } } _ { \mathbf { y } } ) _ { \mathrm { P } } = ( \hat { \pmb { \theta } } _ { \mathbf { y } } ) _ { \mathrm { P } _ { 0 } } + \displaystyle \int _ { 0 } ^ { \mathbb { H } } \frac { \partial \hat { \mathbf { \theta } } _ { \mathbf { y } } } { \partial z } \mathrm { d } { \mathbf { z } } } \end{array}
$$

因为

$$
\begin{array} { r l } & { \frac { \partial \widehat { \mathbf { b } } _ { \mathbf { x } } } { \partial \mathbf { z } } { = } \frac { \partial ^ { 2 } \Pi } { \partial \mathbf { x } \partial \mathbf { z } } { = } \frac { \partial \widehat { \mathbf { b } } _ { \mathbf { z } } } { \partial \mathbf { x } } \ \cdot \ } \\ & { \frac { \partial \widehat { \mathbf { b } } _ { \mathbf { y } } } { \partial \mathbf { z } } { = } \frac { \partial ^ { 2 } \Pi } { \partial \mathbf { y } \partial \mathbf { z } } { = } \frac { \partial \widehat { \mathbf { b } } _ { \mathbf { z } } } { \partial \mathbf { y } } } \end{array}
$$

将它代入 $( 1 4 \cdot 5 9 )$ 式，得到

$$
\begin{array} { r } { ( \hat { \otimes } _ { \mathbf { x } } ) _ { \mathrm { P } } = ( \hat { \otimes } _ { \mathbf { x } } ) _ { \mathrm { P } _ { 0 } } + \displaystyle \int _ { 0 } \frac { \partial \hat { \delta } _ { z } } { \partial \mathbf { x } } \mathrm { d } z \Bigg ] } \\ { ( \hat { \otimes } _ { \mathbf { y } } ) _ { \mathrm { P } } = ( \hat { \otimes } _ { \mathbf { y } } ) _ { \mathrm { P } _ { 0 } } + \displaystyle \int _ { 0 } \frac { \partial \hat { \delta } _ { z } } { \partial \mathbf { y } } \mathrm { d } z \Bigg ] } \end{array}
$$

式中 $\frac { \partial \hat { \mathbf { \theta } } _ { z } } { \partial \mathbf { x } } \mp \sharp \frac { \partial \hat { \mathbf { \theta } } _ { z } } { \partial \mathbf { y } }$ 是扰动重力分量的水平梯度,它们可以利用 $( 1 4 \cdot 5 7 )$ 式的第三式来推求。对于 Z

轴上的任一点有

$$
\ S _ { \nu } = \frac { z } { 2 \pi } \iint \frac { \hat { \partial } _ { \mathbf { r } } ( \mathbf { x } , \mathbf { y } ) } { l ^ { 3 } } \mathrm { d } \mathbf { x } \mathrm { d } \mathbf { y }
$$

式中 $\iota$ 为此点到平面上流动点的距离，见图14.5,故有

$$
l = \sqrt { x ^ { 2 } + y ^ { 2 } + z ^ { 2 } }
$$

将 $( 1 4 \cdot 6 1 )$ 式对 $\pmb { \mathrm { x } }$ 和 $\pmb { y }$ 求导时，是 $\pmb { l }$ 的起始点在变动，因此求导结果要加一负号。因此有

$$
\begin{array} { r } { \frac { \partial } { \partial \mathbf { x } } ( \frac { l } { 1 ^ { 3 } } ) = - \frac { 3 \mathbf { x } } { l ^ { 5 } } } \\ { \frac { \partial } { \partial \mathbf { y } } ( \frac { 1 } { l ^ { 3 } } ) = - \frac { 3 \mathbf { y } } { l ^ { 5 } } } \end{array}
$$

这样一来，由 $( 1 4 \cdot 6 1 )$ 式可得

$$
\begin{array} { r l } & { \frac { \partial \hat { \mathbf { \theta } } _ { s } } { \partial x } = - \displaystyle \frac { 3 z } { 2 \pi } \displaystyle \iint \frac { \partial _ { s } ( \mathbf { x } , \mathbf { y } ) } { l ^ { 5 } } \mathbf { x } \mathrm { d } \mathbf { x } \mathrm { d } \mathbf { y } } \\ & { \frac { \partial \hat { \mathbf { \theta } } _ { s } } { \partial y } = - \displaystyle \frac { 3 z } { 2 \pi } \displaystyle \iint \frac { \partial _ { s } ( \mathbf { x } , \mathbf { y } ) } { l ^ { 5 } } \mathbf { y } \mathrm { d } \mathbf { x } \mathrm { d } \mathbf { y } } \end{array}
$$

将它们代入 $( 1 4 \cdot 6 0 )$ 式，则得

$$
\begin{array} { l } { { \displaystyle ( \hat { \otimes } _ { \mathbf { x } } ) _ { \mathrm { P } } = ( \hat { \otimes } _ { \mathbf { x } } ) _ { \mathrm { P } _ { 0 } } - \frac { 1 } { 2 \pi } \displaystyle \frac { \displaystyle \prod } _ { \mathbf { z } } \hat { \otimes } _ { \mathbf { z } } ( \mathbf { x } , \mathbf { y } ) ( \displaystyle \int _ { 0 } ^ { \mathbf { \hat { \mathbf { y } } } } \frac { \displaystyle 3 z } { \displaystyle { l ^ { 5 } } } \mathrm { d } { \mathbf { z } } ) { \mathbf { x } } \mathrm { d } { \mathbf { x } } \mathrm { d } \mathbf { y } } } \\ { { \displaystyle ( \hat { \otimes } _ { \mathbf { y } } ) _ { \mathrm { P } } = ( \hat { \otimes } _ { \mathbf { y } } ) _ { \mathrm { P } _ { 0 } } - \frac { 1 } { 2 \pi } \displaystyle \iint \hat { \otimes } _ { \mathbf { z } } ( \mathbf { x } , \mathbf { y } ) ( \displaystyle \int _ { 0 } ^ { \mathbf { \hat { \mathbf { y } } } } \frac { \displaystyle 3 z } { \displaystyle { l ^ { 5 } } } \mathrm { d } { \mathbf { z } } ) \mathbf { y } \mathrm { d } { \mathbf { x } } \mathrm { d } \mathbf { y } } } \end{array}
$$

因为

$$
\int \limits _ { 0 } ^ { \mathtt { H } } \frac { 3 z } { l ^ { 5 } } \mathrm { d } z = \frac { 1 } { l ^ { 3 } } | _ { 0 } ^ { \mathtt { H } } = \frac { 1 } { { \mathtt { r } } ^ { 3 } } - \frac { 1 } { { \mathtt { r } } _ { 0 } ^ { 3 } }
$$

式中 $\pmb { \tau } _ { 0 }$ 为 $\pmb { \mathrm { P } } _ { \pmb { \sigma } }$ 点到面元素 $\mathbf { d } \pmb { \Sigma }$ 的距离，见图14.5,故有

$$
\mathbf { r } _ { 0 } = \sqrt { \mathbf { x } ^ { 2 } + \mathbf { y } ^ { 2 } }
$$

代人 $( 1 4 \cdot 6 3 )$ 式，最后得到

$$
\begin{array} { l } { { ( \hat { \vartheta } _ { \mathrm { { s } } } ) _ { \mathrm { { P } } } = ( \hat { \vartheta } _ { \mathrm { { s } } } ) _ { \mathrm { { P } _ { 0 } } } - \displaystyle \frac { 1 } { 2 \pi } \displaystyle \iint \hat { \vartheta } _ { \mathrm { { s } } } ( \mathbf { x } , \mathbf { y } ) ( \displaystyle \frac { 1 } { \mathbf { r } ^ { 3 } } - \frac { 1 } { \mathbf { r } _ { 0 } ^ { 3 } } ) { \mathbf { x } } \mathsf { d } \mathbf { x } \mathsf { d } \mathbf { y } } } \\ { { ( \hat { \vartheta } _ { \mathrm { { y } } } ) _ { \mathrm { { P } } } = ( \hat { \vartheta } _ { \mathrm { { s } } } ) _ { \mathrm { { P } _ { 0 } } } - \displaystyle \frac { 1 } { 2 \pi } \displaystyle \iint \hat { \vartheta } _ { \mathrm { { s } } } ( \mathbf { x } , \mathbf { y } ) ( \displaystyle \frac { 1 } { \mathbf { r } ^ { 3 } } - \frac { 1 } { \mathbf { r } _ { 0 } ^ { 3 } } ) { \mathbf { y } } \mathsf { d } \mathbf { x } \mathsf { d } \mathbf { y } } }  \end{array}
$$

按 $( 1 4 \cdot 6 5 )$ 式计算空间点的 $\pmb { \delta } _ { \mathbf { x } }$ 和 $\pmb { \delta _ { y } }$ 时，只需用到地面上一点 $( \pmb { \mathrm { P } } _ { 0 }$ 点)的垂线偏差值就可以了。  
这给付诸实践提供了方便。

# S14.7重力异常的延拓

在将地球视为球的情况下，在球外任意点都存在着关系式

$$
\Delta \mathbf { g } = - \frac { \partial \mathbf { T } } { \partial \mathbf { p } } - \frac { 2 } { \rho } \mathbf { T }
$$

用点的向径相乘，则得

$$
\rho \Delta g = - \rho { \frac { \partial \mathrm { T } } { \partial \rho } } { - 2 \mathrm { T } }
$$

当 $\boldsymbol { \mathsf { T } }$ 是调和函数时 $p \varphi \frac { \partial \boldsymbol { \Gamma } } { \partial \boldsymbol { \rho } }$ 也是调和函数。由此可知，函数 $\rho \Delta g$ 在地球外空间也是调和函数。将布桑积分 $( 5 \cdot 9 9 )$ 式应用于此函数，可得

$$
\Delta { \bf g } _ { \mathrm { P } } = \frac { \boldsymbol { \rho } ^ { 2 } - \mathrm { R } ^ { 2 } } { 4 \pi \boldsymbol { \rho } } \underset { \Delta } { \iint } \cdot \frac { \Delta { \bf g } } { \bf \tilde { r } ^ { 3 } } \mathrm { d } \sigma
$$

利用这个式子，可以利用地面上的空间异常值推求空间点 $\mathbf { P }$ 的重力异常。这就是重力异常的向上延拓。

如图14.6所示， $\Delta { \bf g } _ { \mathrm { P } }$ 的含意是

$$
\Delta _ { \mathrm { B P } } = _ { \mathrm { B P } } - \gamma _ { \mathrm { Q } }
$$

![](images/b7995f6ad939bcc8e9261645f4bb6996aecce7c3584e762e325466aa3d9a8ee2.jpg)  
图14.6

式中 $\mathtt { g } _ { \mathtt { P } }$ 是 $\mathbf { P }$ 点的重力值， $\mathbf { Q }$ 点是在正常水准面 $\mathbf { U } = \mathbf { W _ { p } }$ 上的相应点， $\mathbf { W _ { P } }$ 是 $\mathbf { P }$ 点的重力位值。只要已知 $\mathbf { P }$ 点在地面上的高度 $\mathbf { H } { = } \mathbf { P } \mathbf { P } _ { 0 }$ 以及地面点 $\mathbf { P } _ { 0 }$ 的高程，则 $\gamma _ { \alpha }$ 是可以算得的。因此有了 ${ \bf \Delta } \cdot \Delta { \bf g _ { P } }$ ，又可求得 $\pmb { \mathrm { g } } \mathbf { \mathrm { p } }$ 。当用飞机在空中测定重力值时，飞机对地面的高度是可以测定的，用重力异常向上延拓的结果可以检验航空重力测量的精度。

在 $\mathbf { P }$ 点的高度不大时，也可以采用平面近似。考虑到

$$
\frac { \rho ^ { 2 } - \mathrm { R } ^ { 2 } } { 4 \pi \rho } = \frac { \left( \rho - \mathrm { R } \right) \left( \rho + \mathrm { R } \right) } { 4 \pi \rho } = \frac { \mathrm { H } } { 2 \pi }
$$

可将 $( 1 4 \cdot 6 6 )$ 式改写为

$$
\Delta { \bf { g } } _ { \mathrm { { p } } } = \frac { \mathrm { ~ H ~ } } { 2 \pi } \int _ { a = 0 \kappa = 0 } ^ { \zeta \tau } \int _ { \tau ^ { 3 } } ^ { \Delta { \bf { g } } } { \bf { \ H } } { \bf { \ H } } ^ { \mathrm { { a s d s d } } \alpha }
$$

这里采用了平面极坐标 $( \mathfrak { s } , \mathfrak { a } )$ ，式中

$$
\bf { r } = \sqrt { s ^ { 2 } + H ^ { 2 } }
$$

若将积分区域分成很多的环，则

$$
\Delta \mathbf { g } _ { \mathrm { p } } = \sum _ { \mathrm { i } } \mathrm { C } _ { \mathrm { i } } \Delta \mathbf { g } _ { \mathrm { i } }
$$

式中 $\widetilde { \Delta \bf g _ { i } }$ 为第 $\mathbf { i }$ 环的平均异常值， $\mathbf { C _ { i } }$ 为相应的系数，它可按下式计算

$$
\mathbf { C } _ { \mathrm { { i } } } = { \frac { \mathrm { H } } { 2 \pi } } \int \int \limits _ { \mathrm { { s i } } - 1 \mathrm { ~ { u } ~ } } ^ { \mathrm { { s } _ { \mathrm { { i } } } } } { \frac { \mathrm { { 2 } } \pi } { ( { \mathrm { s } } ^ { 2 } + \mathrm { H } ^ { 2 } ) ^ { 3 / 2 } } } = \mathrm { H } ( { \frac { 1 } { { \mathbf { r } } _ { \mathrm { { i } } - 1 } } } - { \frac { 1 } { { \mathbf { r } } _ { \mathrm { { i } } } } } )
$$

其中

$$
\scriptstyle \mathbf { r } _ { \mathrm { i } } = { \sqrt { s _ { \mathrm { i } } ^ { 2 } + H ^ { 2 } } }
$$

式中 $\mathbb { s } _ { \mathrm { i } - 1 }$ 和 $\mathsf { \pmb { s } } _ { \mathrm { \pmb { i } } }$ 为第i环的内、外半径。为了计算方便，再将每个环又等分为 $\mathbf { k } _ { \mathrm { i } }$ 个扇形，则得

$$
\Delta _ { \mathbf { g } \mathrm { _ p } } = \sum _ { \mathrm { i } } \sum _ { \mathbf { k } } \mathrm { C _ { \mathrm { i } \mathbf { k } } } \overset { \cdot } { \Delta } \mathbf { g } _ { \mathrm { i } \mathbf { k } }
$$

其中 $\overline { { \Delta \mathbf { g } } } _ { \mathrm { i k } }$ 为第 $\vdots$ 环第 $\mathbf { k }$ 个扇形的平均异常值， $\mathbf { C _ { i k } }$ 为相应扇形的系数，显然有：

$$
\mathrm { C _ { \mathrm { i } \mathrm { k } } = \frac { C _ { \mathrm { i } } } { \tilde { k } _ { \mathrm { i } } } = \frac { H } { \tilde { k } _ { \mathrm { i } } } ( \frac { 1 } { r _ { \mathrm { i } - 1 } } - \frac { 1 } { r _ { \mathrm { i } } } ) }
$$

希尔伏宁(Hirvonen.R.A.)曾设计了一组模板(29，其特点是由各个扇形引起的误差有同样的均方根值。表14.3给出了这组模板的数据：环带的内、外半径 $\mathbf { s _ { i - 1 } }$ 和 $\mathbf { s } _ { \mathrm { i } }$ ，每个环带划分的扇形数 $\bf { k } _ { i }$ 和相应的系数值 $\mathbf { C _ { i k } }$ ，其中 $\mathsf { s } _ { \mathrm { i } - 1 }$ 和 $\mathsf { \pmb { s } } _ { \mathrm { \pmb { i } } }$ 和高程 $\mathbf { H }$ 用同样的单位。

表14.3  

<table><tr><td rowspan="2">内半径 si-</td><td rowspan="2">外半径 s</td><td rowspan="2">扇 形 数 ki</td><td colspan="3">Cik</td></tr><tr><td>H=i</td><td>H=2</td><td>H=0.5</td></tr><tr><td>0</td><td>0.4</td><td>1</td><td>0.07152</td><td>0.01942</td><td>0.21913</td></tr><tr><td>0.4</td><td>1.0</td><td>8</td><td>0.02767</td><td>0.01077</td><td>0.04171</td></tr><tr><td>1.0</td><td>1.8</td><td>12</td><td>0.01846</td><td>0.01259</td><td>0.01496</td></tr><tr><td>1.8</td><td>3.0</td><td>12</td><td>0.01412</td><td>0.01572</td><td>0.00860</td></tr><tr><td>3.0</td><td>4.5</td><td>16</td><td>0.00621</td><td>0.00928</td><td>0.00337</td></tr><tr><td>4.5</td><td>6.7</td><td>16</td><td>0.00433</td><td>0.00751</td><td>0.00225</td></tr><tr><td>6.7</td><td>10.0</td><td>16</td><td>0.00301</td><td>0.00562</td><td>0.00153</td></tr><tr><td>10.0</td><td>15.0</td><td>16</td><td>0.00206</td><td>0.00400</td><td>0.00104</td></tr><tr><td>15.0</td><td>22.0</td><td>16</td><td>0.00132</td><td>0.00260</td><td>0.00066</td></tr><tr><td>22.0</td><td>32.0</td><td>16</td><td>0.00089</td><td>0.00176</td><td>0.00044</td></tr></table>

现以计算点的高度为 $5 \mathrm { k m }$ 作为例子，根据所选择的那一组系数，模板的环带有不同的半径：当采用第一组系数时， $\mathbf { s } _ { \mathrm { i } }$ 都应乘 $5 k m$ ，其最大积分半径为 ${ \tt 1 6 0 } _ { \tt A m } ^ { \tt 1 }$ ；若用第二组系数， ${ \bf { s } } _ { \mathrm { { i } } }$ 乘$\pmb { 2 . 5 k \mathrm { m } }$ ，最大积分半径为 ${ 8 0 } \mathbf { k m }$ ；若用第三组系数； ${ \mathfrak { s } } _ { ; }$ 应乘 $\mathrm { { l } } \mathrm { { 0 k m } }$ ，最大积分半径为 $3 2 0 \mathbf { k } \mathfrak { n } \mathfrak { i }$ 。显然，利用第二组系数时，积分区域小，扇形面积小，积分区域内的影响有好的计算精度，但忽略的区域外的影响要大些;而利用第三组系数时，情况与之相反；用第一-组系数时，效果介于前两者之间。

如果航空重力测量能够具有较好的精度，由此可以获得空中大片的已知重力异常值，用它们可以反解地面上的重力异常值，这就是所谓的重力异常向下延拓。向下延拓的方法已在$\ S 9 . 1 0$ 中讲过，那里是将地面上的重力异常值向下延拓到贝亚哈马球上。在此就没有必要再重复了。

# 参考文献

# 17操华胜等：地球重力场的虚拟单层密度表示理论的数字实现：测绘学报，1985.14(4)

34IUGG. geodetic Reierence System. 1971   
35 H Moritz.'Series solutions of Molodensky's problem. Publ. Deut. Geod. Komm.,A,70,1971 36L P Pelinen. On the identity of various solutions of Molodensky's problem with the help of a small parameter. Int. Symp. on Earth gravity Models and Related Problems, Salant Louis， Missourl,1972 37H.Moritz. On’the use of the terrain correction in solving Molodensky's problem. Rep.108，Dep.of Geod.Sci. OSU.1968   
38R.H. Rapp. Geopotential coeffcient behavior to high degree and geoid information by wavelenth. Rep. 180,Dep. of Geod. Sci. OSU.1973   
39 O M Ostach. On the procedure of astro-gravimetric level. Studia geoph. et geod., vol.10,1970 40D D McCarthy et al: IERS Technical Note 3.Observatoire de Paris,1989   
41 MH IOpkiHa.JurTuecKaA riaeka M.C.MoogeHcKoro n BuHceHHA npeRhteHm KRa3ureoa.Tp LHIHrAuk,BHn.121,1957   
42K Arnold. Ein graphik Hilfsmitteln zur'gravity Verbesserung astronomisches Nivellement. Ver.d.geod. Inst.Potsdam,No.18.1961   
43F R Helmert. Die mathematischen und physikalischen Theorien der hFhren geodasie. Vo1. 2,1884 (reprinted 1962）   
44E Ecker. Uber die Aquivalenz von Losungen des geodatischen Randwertproblems. Osterr.z. Vermess. No59.1971   
45CC Tscherning et al. Closed covariance expressions for gravity anomalies,geoid undulations and deflections of the vertical implied by anomaly degree variance models.Rep.208,Dep. of Geod.Sci. OSU.1974 46OL Colombo.Numerical methods for harmonic analysis on the sphere. Rep.310,Dep.of Geod.Sci. OSU.1981

封面书名版权前言目录绪论

0.1重力   
0.2用途和本书概要

# 第一章绝对重力测量

1.1 历史的回顾1.2 数学摆的理论1.3 物理摆1.4 运用可倒摆测定绝对重力1.5 运用物体的自由运动测定重力1.6 几项改正1.7重力系统第二章相对重力测量2.1 用摆仪进行相对重力测量2.2 进行相对重力测量的静力法2.3 ZSM型重力仪2.4 ZSM型重力仪的检验和调整2.5 重力仪的零点飘移2.6 重力仪格值的测定2.7 运用ZSM型重力仪进行相对重力测量2.8 LCR型重力仪的原理和结构2.9 LCR型重力仪的检验和调整2.10 LCR型重力仪观测数据的处理2.11GS型金属弹簧重力仪2.12超导重力仪

# 第三章海洋重力测量

3.1引言  
3.2垂直扰动加速度的影响  
3.3 水平扰动加速度的影响  
3.4 厄特弗斯改正  
3.5 KSS型海洋重力仪  
3.6 CHZ海洋重力仪  
3.7海洋重力测量及其数据处理

# 第四章位理论

4.1力的位函数  
4.2引力位  
4.3匀质球层、球壳和球体的引力位和引力

4.4质体引力位的性质4.5 单层引力位的性质4.6 重力位4.7 水准面和力线  
第五章 调和函数及其边值问题5.1 高斯和格林的积分式5.2 调和函数5.3 调和函数的性质5.4 球外调和函数的径向导数5.5 边值问题5.6 格林公式的应用5.7 质体引力位的等值层5.8 用球谐函数解球的外部边值问题  
第六章 水准椭球的重力场6.1 外部点的重力位6.2 椭球面上的重力6.3 椭球面上重力位和重力的级数式6.4 外部点引力位的球谐函数级数式6.5 计算外部点引力的实用公式6.6 重力的垂直梯度6.7 水准面和力线6.8 水准椭球的质量分布  
第七章 地球重力场7.1 地球重力位的级数展开式7.2 克莱劳定理7.3 扰动位7.4 基本微分方程7.5 旋转扁球面的正常重力公式7.6 赫尔默特1901—1909正常重力公式  
第八章 司托克斯理论8.1 司托克斯定理8.2 大地水准面8.3 司托克斯公式8.4 威宁·曼尼兹公式8.5 广义司托克斯公式8.6 重力的层间改正和局部地形改正8.7 重力归算和间接影响8.8 地壳均衡假说8.9 重力的均衡改正8.10 地形——均衡垂线偏差8.11 积分式的实际计算方法

8.12顾及地球扁率的司托克斯公式第九章研究地球重力场的现代理论9.1莫洛琴斯基问题9.2近似地形面9.3地面垂线偏差和扰动位的关系9.4 基本积分方程9.5 莫洛琴斯基解9.6 布洛瓦尔解9.7 解析延拓解9.8 空间重力异常9.9一次改正项的等值性9.10贝亚哈马理论9.11利用地形数据改进司托克斯解

第十章地球重力场模型10.1引力位系数模型10.2 推求平均异常10.3 利用地面重力数据建立位系数模型10.4 综合卫星和地面数据建立重力场模型10.5 模型成果概况10.6 重力异常的阶方差模型10.7 用位系数计算高程异常和垂线偏差  
第十一章 垂线偏差11.1 定义和用途11.2 运用重力和地形数据计算垂线偏差11.3 推求三角点天文大地垂线偏差的原理11.4 积分半径的确定11.5 精度估算方法11.6 重力垂线偏差的误差11.7 代表误差11.8 推求重力垂线偏差时重力点的最有利分布11.9 为推求平均空间异常的重力点密度11.10 重力点的重力值、高程和坐标的精度要求  
第十二章 高程异常12.1 大地高12.2 正常高的计算12.3 水准路线上重力点的密度12.4 利用重力和地形数据计算高程异常12.5 天文水准12.6 天文重力水准12.7 重力改正项的积分半径12.8 计算重力改正项的模板12.9 天文重力水准的重力点布设

12.10计算重力改正项的其他方法12.11推求大地点相对高程异常的方法第十三章最小二乘配置的应用13.1 最小二乘配置的原理13.2 精度13.3 扰动位的协方差函数13.4 协方差传播13.5 全球协方差函数模型13.6 引力位球谐系数的求定13.7 局部扰动场的协方差函数13.8 重力异常的局部协方差函数13.9 重力异常的推估13.10 推求高程异常13.11 顾及与高程的相关性推估空间异常13.12 逐步配置第十四章 地球外部重力场14.1 概述14.2 用地球重力场模型计算扰动重力14.3 用司托克斯积分法计算扰动重力14.4 局部扰动重力场的点质量模型14.5 利用单层密度计算扰动重力14.6 扰动重力的向上延拓14.7 重力异常的延拓参考文献