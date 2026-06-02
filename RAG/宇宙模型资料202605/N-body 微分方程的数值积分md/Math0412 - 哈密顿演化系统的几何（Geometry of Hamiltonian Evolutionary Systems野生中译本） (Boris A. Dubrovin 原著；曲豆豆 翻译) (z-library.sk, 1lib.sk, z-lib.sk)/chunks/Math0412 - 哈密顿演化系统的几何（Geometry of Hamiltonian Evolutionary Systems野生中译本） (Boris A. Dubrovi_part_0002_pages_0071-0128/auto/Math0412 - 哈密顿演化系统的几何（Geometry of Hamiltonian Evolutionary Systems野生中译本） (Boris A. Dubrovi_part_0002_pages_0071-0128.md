由(2.76a)可得

$$
V ( \lambda ) = \binom { u ^ { \prime } } { u ^ { \prime \prime } - 2 ( u - \lambda ) ( u + 2 \lambda ) } \quad \begin{array} { c } { { - 2 ( u + 2 \lambda ) \nonumber } } \\ { { - u ^ { \prime } } } \end{array} .
$$

(2.77)中的谱参数 $\lambda$ 是一个新的独立变量 [从而(2.77)是关于 $\lambda$ 的恒等式] .

事实上存在一族方程 [KdV 方程簇] , 使得它们都具有形如(2.77)的关于给定的算子${ \mathcal { L } } = \partial _ { x } - U ( \lambda )$ 的交换表示 [或者等价地, 存在关于给定算子 $L$ 的形如(2.76)的 Lax 形式. ] 我们将(2.76a)中的算子 $A$ 重新记作 $A _ { 1 }$ , 将(2.80)中的矩阵 $V ( \lambda )$ 重新记作 $V _ { 1 } ( \lambda )$ .固定 $U ( \lambda )$ , 假定 $V ( \lambda )$ 为关于 $\lambda$ 的多项式, 我们企图寻找形如(2.77)的全部方程:

$$
U _ { s } ( \lambda ) - V _ { x } ( \lambda ) + [ U ( \lambda ) , V ( \lambda ) ] = 0 .
$$

设

$$
V = \left( { a b \atop c d } \right) ,
$$

[其中 $a = a ( \lambda ) , b = b ( \lambda ) , c = c ( \lambda ) , d = d ( \lambda )$ 为多项式] . 不妨假定 $\mathrm { t r } V \equiv 0$ , 即 $d = - a$ .从而由(2.77a)可得

$$
\begin{array} { r } { \left( \begin{array} { c c } { 0 } & { 0 } \\ { u _ { s } } & { 0 } \end{array} \right) - \left( \begin{array} { c c } { a _ { x } } & { b _ { x } } \\ { c _ { x } } & { d _ { x } } \end{array} \right) + \left( \begin{array} { c c } { c - b ( u - \lambda ) } & { - 2 a } \\ { 2 a ( u - \lambda ) } & { - c + b ( u - \lambda ) } \end{array} \right) = 0 . } \end{array}
$$

因此 $a = - \frac { 1 } { 2 } b _ { x }$ $c = - \frac { 1 } { 2 } b _ { x x } + b ( u - \lambda )$ , 以及

$$
u _ { s } = c _ { x } - 2 a ( u - \lambda ) = - \frac { 1 } { 2 } b _ { x x x } + 2 b _ { x } ( u - \lambda ) + u _ { x } b .
$$

由于 $b = b ( \lambda )$ 为多项式

$$
b \equiv b _ { 0 } \lambda ^ { n } + \cdot \cdot \cdot + b _ { n } ,
$$

由(2.81)可得系数 $b _ { 0 } , b _ { 1 } , . . . , b _ { n }$ 的递推关系: $b _ { 0 }$ 为常数, 并且

$$
2 \partial _ { x } b _ { k + 1 } = M b _ { k } , \quad M = - \frac { 1 } { 2 } \partial _ { x } ^ { 3 } + 2 u \partial _ { x } + u _ { x } , \quad k = 0 , . . . , n - 1
$$

$$
u _ { s } = M b _ { n } .
$$

引入“生成函数”

$$
v _ { \infty } ( \lambda ) = 1 + \frac { v _ { 1 } } { \lambda } + \frac { v _ { 2 } } { \lambda ^ { 2 } } + \cdot \cdot \cdot
$$

$[ v _ { \infty }$ 与 $x , t$ 有关] , 使得满足齐次方程

$$
- \frac { 1 } { 2 } v _ { \infty _ { x x x } } + 2 ( u - \lambda ) v _ { \infty _ { x } } + u _ { x } v _ { \infty } = 0 .
$$

等价地, 矩阵 $V _ { \infty } ( \lambda ) = \left( \begin{array} { c c } { { - \displaystyle \frac { 1 } { 2 } v _ { \infty _ { x } } } } & { { v _ { \infty } } } \\ { { - \displaystyle \frac { 1 } { 2 } v _ { \infty _ { x x } } + v _ { \infty } ( u - \lambda ) } } & { { \displaystyle \frac { 1 } { 2 } v _ { \infty _ { x } } } } \end{array} \right)$ 与算子 ${ \mathcal { L } } = \partial _ { x } - U ( \lambda )$ 交换.

$$
[ \mathcal { L } , V _ { \infty } ( \lambda ) ] = [ \partial _ { x } - U ( \lambda ) , V _ { \infty } ( \lambda ) ] = 0 .
$$

引理 2.5. 上述方程具有形如(2.84)的唯一解, 使得系数 $v _ { k }$ 是 $u , u ^ { \prime } , \ldots$ 的形如

$$
v _ { k } = v _ { k } ( u , u ^ { \prime } , . . . , u ^ { ( 2 k - 2 ) } )
$$

的多项式, 并且满足归一化条件

$$
v _ { k } ( 0 , 0 , . . . , 0 ) = 0 .
$$

例如, v1 = 2 , v $v _ { 2 } = \frac { 1 } { 8 } ( 3 u ^ { 2 } - u ^ { \prime \prime } ) .$ ,...

证明. 行列式 $\operatorname* { d e t } V _ { \infty } ( \lambda )$ 与迹 $\mathrm { t r } V _ { \infty } ( \lambda )$ 是方程(2.85a)的首次积分. 我们考虑方程(2.85a)的满足下述归一化条件

$$
\mathrm { t r } V _ { \infty } ( \lambda ) = 0 , \quad \mathrm { d e t } V _ { \infty } ( \lambda ) = \lambda
$$

的解. 而矩阵 $V _ { \infty } ( \lambda )$ 形如

$$
V _ { \infty } ( \lambda ) = \left( \begin{array} { c c } { { - \displaystyle \frac { 1 } { 2 } v _ { \infty _ { x } } } } & { { v _ { \infty } } } \\ { { - \displaystyle \frac { 1 } { 2 } v _ { \infty _ { x x } } + v _ { \infty } ( u - \lambda ) } } & { { \displaystyle \frac { 1 } { 2 } v _ { \infty _ { x } } } } \end{array} \right)
$$

其中 $v _ { \infty } ( \lambda )$ 形如(2.84), 满足(2.85). 由 $\operatorname* { d e t } V _ { \infty } ( \lambda ) = \lambda$ 可得关于 $v _ { \infty } ( \lambda )$ 的如下非线性方程:

$$
\frac { 1 } { 2 } v _ { \infty } v _ { \infty _ { x x } } - \frac { 1 } { 4 } v _ { \infty _ { x } } ^ { 2 } - ( u - \lambda ) v _ { \infty } ^ { 2 } = \lambda .
$$

由此可得(2.84)中的系数的递推关系: $v _ { 0 } = 1$ , $v _ { 1 } = \frac { u } { 2 }$ 并且对于 $k \geq 1$ 有

$$
v _ { k + 1 } = \sum _ { i + j = k } \left( - \frac { 1 } { 4 } v _ { i } v _ { j } ^ { \prime \prime } + \frac { 1 } { 8 } v _ { i } ^ { \prime } v _ { j } ^ { \prime } + \frac { 1 } { 2 } u v _ { i } v _ { j } \right) - \frac { 1 } { 2 } \sum _ { i = 1 } ^ { k } v _ { i } v _ { k + 1 - i } .
$$

显然该递推关系的解 $v _ { 2 } , v _ { 3 } , \ldots$ 形如 (2.85b),(2.85c), 从而得证.

任何满足(2.77a)并且 $\mathrm { t r } V = 0$ 的关于 $\lambda$ 的多项式矩阵 $V ( \lambda )$ 都形如

$$
V = \left( \begin{array} { c c } { { - \frac { 1 } { 2 } b _ { x } } } & { { b } } \\ { { - \frac { 1 } { 2 } b _ { x x } + b ( u - \lambda ) } } & { { \frac { 1 } { 2 } b _ { x } } } \end{array} \right) , \quad b = \sum _ { i = 1 } ^ { n } c _ { i } { \hat { v } } _ { n - i } ( \lambda ) ,
$$

$$
\hat { v } ( \lambda ) = [ \lambda ^ { k } v _ { \infty } ( \lambda ) ] \quad ( \mod \lambda ^ { - 1 } ) ,
$$

$c _ { 0 } , . . . , c _ { n }$ 为常数. 从而“第 $n$ 阶 KdV 方程”形如

$$
u _ { s } = M \sum _ { i = 0 } ^ { n } c _ { n - i } v _ { i } ( u , u ^ { \prime } , . . . , u ^ { ( 2 i - 2 ) } ) \equiv 2 \partial _ { x } \sum _ { i = 0 } ^ { n } c _ { n - i } v _ { i + 1 } ( u , u ^ { \prime } , . . . , u ^ { ( 2 i ) } ) ,
$$

[算子 $M$ 的定义见(2.82)] .

例如 $n = 0$ 时, $u _ { s } = c _ { 0 } u _ { x }$ ; $n = 1$ 时:

$$
u _ { s } = \frac { 1 } { 4 } c _ { 0 } ( 6 u u _ { x } - u _ { x x x } ) + c _ { 1 } u _ { x } .
$$

以下方程构成方程族(2.89) [KdV 方程簇] 的一组“基”:

$$
u _ { t _ { k } } = - 2 ^ { 2 k } M v _ { k } ( u , u ^ { \prime } , . . . , u ^ { ( 2 k - 2 ) } ) \equiv - 2 ^ { 2 k + 1 } \partial _ { x } v _ { k + 1 } ( u , u ^ { \prime } , . . . , u ^ { ( 2 k ) } ) ,
$$

$k = 0 , 1 , \ldots$ . 对于 $k = 0$ , 有 $u _ { t _ { 0 } } + u _ { x } = 0$ ; $k = 1$ 时得到 KdV 方程(2.75). 我们已经知道对任意 $k$ , 方程(2.90)具有 [形如(2.77a)的] 零曲率表示

$$
U _ { t _ { k } } ( \lambda ) - V _ { k _ { x } } ( \lambda ) + [ U ( \lambda ) , V _ { k } ( \lambda ) ] = 0
$$

或者

$$
\partial _ { t _ { k } } \mathcal { L } = [ V _ { k } ( \lambda ) , \mathcal { L } ] ,
$$

$( { \mathcal { L } } = \partial _ { x } - U ( \lambda ) )$ , 或者等价地, 有 Lax 表示

$$
L _ { t _ { k } } = [ A _ { k } , L ] .
$$

这里

$$
V _ { k } ( \lambda ) = - 2 ^ { 2 k } \left( \begin{array} { c c } { { - \frac { 1 } { 2 } \hat { v } _ { k _ { x } } ( \lambda ) } } & { { \hat { v } _ { k } ( \lambda ) } } \\ { { - \frac { 1 } { 2 } \hat { v } _ { k _ { x x } } ( \lambda ) + \hat { v } _ { k } ( \lambda ) ( u - \lambda ) } } & { { \frac { 1 } { 2 } \hat { v } _ { k _ { x } } ( \lambda ) \right) . } } \end{array}
$$

$2 k + 1$ 阶微分算子 $A _ { k }$ 可由 $V _ { k } ( \lambda )$ 与关系(2.79)唯一确定:

$$
A _ { k } = ( - 2 ) ^ { 2 k } \sum _ { i = 0 } ^ { k } \left( - { \frac { 1 } { 2 } } v _ { k - i } ^ { \prime } L ^ { i } + v _ { k - i } L ^ { i } \partial _ { x } \right) .
$$

我们来证明这些方程两两交换.

引理 2.6.

$$
( u _ { t _ { k } } ) _ { t _ { l } } = ( u _ { t _ { l } } ) _ { t _ { k } } .
$$

证明. 由于 $[ \mathcal { L } , V _ { \infty } ] = 0$ , 从而有

$$
0 = [ \partial _ { t _ { k } } , C , V _ { \infty } ] + [ \mathscr { L } , \partial _ { t _ { k } } V _ { \infty } ] = [ [ V _ { k } , \mathscr { L } ] , V _ { \infty } ] + [ \mathscr { L } , \partial _ { t _ { k } } V _ { \infty } ] = [ \mathscr { L } , \partial _ { t _ { k } } V _ { \infty } - [ V _ { k } , V _ { \infty } ] ] .
$$

因此矩阵 $\tilde { V } _ { \infty } ( \lambda ) = \partial _ { t _ { k } } V _ { \infty } - [ V _ { k } , V _ { \infty } ]$ 满足(2.85). 归一化条件(2.85c)显然满足. 由于$V _ { k } = \lambda ^ { k } V _ { \infty } + { \cal O } ( \lambda ^ { - 1 } )$ , 从而 $[ V _ { k } , V _ { \infty } ] = O ( \lambda ^ { - 1 } )$ 以及 $\partial _ { t _ { k } } V _ { \infty } = O ( \lambda ^ { - 1 } )$ . 再由问题(2.85a)-(2.85c)的解的唯一性, 可得 $\tilde { V } _ { \infty } ( \lambda ) = 0$ , 即

$$
\partial _ { t _ { k } } V _ { \infty } = [ V _ { k } , V _ { \infty } ] , \quad k = 1 , 2 , \ldots
$$

由(2.96)易证交换性条件(2.95). 引理证毕.

KdV 方程簇(2.90) 中的所有交换流都是哈密顿 [甚至是 双哈密顿 (bi-Hamiltonian)] 系统, 且具有公共的无穷守恒律. 为构造这些守恒律, 我们要更加深入理解算子 $L$ 的本征函数的性质.

引理 2.7. 设算子 $L = - \partial _ { x } ^ { 2 } + u$ 的势函数 $u$ 与 $t _ { k }$ 有关, 且满足方程簇(2.90). 则两两交换的算子 $\mathcal { L }$ 与 $\partial _ { t _ { k } } - V _ { k } ( \lambda )$ 存在唯一的公共本征函数 $\vec { \psi } = \left( \begin{array} { l } { \psi } \\ { \psi ^ { \prime } } \end{array} \right) .$

$$
\mathcal { L } \vec { \psi } = 0 , \quad ( \partial _ { t _ { k } } - V _ { k } ( \lambda ) ) \vec { \psi } = 0 ,
$$

使得对数导数 $\partial _ { x } \log \psi$ 与 $\partial _ { t _ { k } } \log \psi$ 是如下的关于 $\sqrt { \lambda }$ 的形式幂级数:

$$
{ \frac { 1 } { i } } ( \log \psi ) _ { x } = { \sqrt { \lambda } } + \sum _ { j = 1 } ^ { \infty } { \frac { \chi _ { j } } { ( 2 { \sqrt { \lambda } } ) ^ { j } } } ,
$$

$$
{ \frac { 1 } { i } } ( \log \psi ) _ { t _ { k } } = - 2 ^ { 2 k } ( \sqrt \lambda ) ^ { 2 k + 1 } + \sum _ { j = 0 } ^ { \infty } { \frac { \xi _ { k , j } } { ( 2 \sqrt \lambda ) ^ { j } } } .
$$

并且所有的系数 $\chi _ { j } , \xi _ { k , j }$ 都是 $u , u ^ { \prime } , \ldots$ 的多项式.

证明. 记 $\chi = \frac { 1 } { i } ( \log \psi ) _ { x }$ , 则有 Riccati 方程 $i \chi ^ { \prime } - \chi ^ { 2 } - u + \lambda = 0$ . 易证该方程存在唯一 的形如(2.98)的解, 使得系数 $\chi _ { j }$ 为 $u , u ^ { \prime } , \ldots$ 的多项式, $\chi _ { j } = \chi _ { j } ( u , u ^ { \prime } , . . . , u ^ { ( j ) } )$ .

对于由(2.97),(2.94)所得的 $\psi$ , 有

$$
\partial _ { t _ { k } } \psi = - 2 ^ { k } \left( - \frac { 1 } { 2 } \hat { v } _ { k } ^ { \prime } ( \lambda ) \psi + \hat { v } _ { k } ( \lambda ) \psi ^ { \prime } \right) .
$$

从而有

$$
\frac { 1 } { i } ( \log \psi ) _ { t _ { k } } = - 2 ^ { 2 k } \left( \frac { i } { 2 } \hat { v } _ { k } ^ { \prime } ( \lambda ) + \hat { v } _ { k } ( \lambda ) \chi ( \lambda ) \right) .
$$

这是形如(2.99)的关于 $\sqrt { \lambda }$ 的形式幂级数. 引理证毕.

# 推论 2.8. 泛函

$$
\int \chi _ { j } ( u , u ^ { \prime } , . . . , u ^ { ( j ) } ) \mathrm { d } x
$$

是(2.90)的所有方程的公共的守恒律, 且相应的 流密度 (flux density) 为 $\xi _ { k , j }$ :

$$
\partial _ { t _ { k } } \chi _ { j } = \partial _ { x } \xi _ { k , j } .
$$

证明. 这由等式

$$
[ ( \log \psi ) _ { x } ] _ { t _ { k } } = [ ( \log \psi ) _ { t _ { k } } ] _ { x }
$$

易得.

若 $\chi _ { R }$ 与 $\chi _ { I }$ 分别为 $\chi$ 的实部与虚部 $( \lambda > 0 )$ ), $\chi = \chi _ { R } + i \chi _ { I }$ , 则由 Riccati 方程可得

$$
\chi _ { I } = { \frac { 1 } { 2 } } { \frac { \chi _ { R } ^ { \prime } } { \chi _ { R } } } , \quad \operatorname { R e } \chi _ { 2 j } = 0 , \quad \operatorname { I m } \chi _ { 2 j + 1 } = 0 .
$$

从而 $j$ 为偶数时相应的守恒律 $\chi _ { j }$ 是平凡的; 而奇数项系数其实是 Kruskal 积分:

$$
I _ { m } = \int \chi _ { 2 m + 1 } ( u , u ^ { \prime } , . . . , u ^ { ( 2 m + 1 ) } ) \mathrm { d } x .
$$

其生成函数形如

$$
\sqrt { \lambda } + \sum \frac { I _ { m } } { ( 2 \sqrt { \lambda } ) ^ { 2 m + 1 } } = \int \chi _ { R } \mathrm { d } x \equiv \int \chi \mathrm { d } x \equiv \frac { 1 } { i } \int ( \log \psi ) _ { x } \mathrm { d } x .
$$

注记. 下述等式对形式幂级数(2.84)与(2.98)成立:

$$
\chi _ { R } ( \lambda ) \equiv \sqrt { \lambda } + \sum _ { m = 0 } ^ { \infty } \frac { \chi _ { 2 m + 1 } } { ( 2 \sqrt { \lambda } ) ^ { 2 m + 1 } } = \frac { \sqrt { \lambda } } { v _ { \infty } ( \lambda ) } .
$$

为证明方程(2.90)为哈密顿系统, 我们需要以下:

引理 2.9. 下述等式成立:

$$
\frac { \delta } { \delta u } \int \chi \mathrm { d } x = - \frac { 1 } { 2 \chi _ { R } ( \lambda ) } = - \frac { 1 } { 2 \sqrt { \lambda } } v _ { \infty } ( \lambda ) .
$$

此式出现于 [3] [也可见 [8]] . 这里给出与之不同的证明. 然而这些证明在本质上都基于算子 $L$ 的谱理论. 此引理的证明留作本节附录.

推论 2.10. 对任意 $k$ , 方程(2.90) 都是关于 Gardner-Zakharov-Faddeev 括号

$$
\{ u ( x ) , u ( y ) \} = \delta ^ { \prime } ( x - y )
$$

的哈密顿系统, 并且相应的哈密顿量为 2Ik+1,

$$
u _ { t _ { k } } = 2 \partial _ { x } \frac { \delta I _ { k + 1 } } { \delta u ( x ) } .
$$

此外, 该方程也是关于 Magri 括号

$$
\{ u ( x ) , u ( y ) \} _ { M } = - { \frac { 1 } { 2 } } \delta ^ { \prime \prime \prime } ( x - y ) + [ u ( x ) + u ( y ) ] \delta ^ { \prime } ( x - y )
$$

的哈密顿系统, 相应的哈密顿量为 $I _ { k }$ ,

$$
u _ { t _ { k } } = M \frac { \delta I _ { k } } { \delta u ( x ) } .
$$

证明. 由(2.106)可知 (2.84),(2.85) 中的系数 $v _ { m }$ 满足

$$
\frac { \delta } { \delta u ( x ) } I _ { m } = - 2 ^ { 2 m } v _ { m } , \quad m = 0 , 1 , \ldots
$$

由此易得方程(2.90)的上述双哈密顿结构.

# 附录: 引理2.9的证明

注意泛函 $I _ { k }$ 的密度是 $u , u ^ { \prime } , \ldots$ 的多项式, 由 $I _ { k }$ 的局部性可知变分导数 $\frac { \delta I _ { k } } { \delta u ( x ) }$ 与$u ( x )$ 具体所在的函数空间无关. 我们来证明光滑周期函数 $u ( x + T ) = u ( x )$ 情形. 我们将满足如下性质的函数 $\psi _ { \pm } = \psi _ { \pm } ( x , \lambda )$

$$
\begin{array} { l l } { { L \psi _ { \pm } ( x , \lambda ) = \lambda \psi _ { \pm } ( x , \lambda ) , } } & { { \psi _ { \pm } ( x + T , \lambda ) = e ^ { \pm i p ( \lambda ) T } \psi _ { \pm } ( x , \lambda ) , } } \\ { { { } } } & { { { } } } \\ { { \psi _ { \pm } ( x _ { 0 } , \lambda ) = 1 } } & { { } } \end{array}
$$

称为 Bloch-Floquet 本征函数 [其中给定常数 $x _ { 0 }$ 称为“泛点”(generic point)] . $p ( \lambda )$ 为[多值] 函数, 在固体物理中称为 拟矩 (quasimomentum) . 可以证明 [3], $\psi _ { \pm } ( x , \lambda )$ 可

关于 $\lambda$ 解析延拓到适当的黎曼面上, 使得 $( \log \psi _ { \pm } ) _ { x }$ 可以展成形如(2.98)的形式幂级数,$\frac { 1 } { i } ( \log \psi _ { \pm } ) _ { x } = \pm ( \chi _ { R } \pm i \chi _ { I } )$ , $\chi = \chi ( x , \lambda )$ . 并且成立

$$
p ( \lambda ) = \frac { 1 } { T } \int _ { 0 } ^ { T } \chi \mathrm { d } x = \frac { 1 } { T } \int _ { 0 } ^ { T } \chi _ { R } \mathrm { d } x .
$$

因此在周期函数情形, Kruskal 积分的生成函数(2.104) 恰为拟矩 $p ( \lambda ) ( 2 . 1 1 1 )$ . 现在来证明公式(2.106). 考虑满足下式的函数 $\tilde { \psi } _ { + } , \psi _ { - }$ :

$$
\begin{array} { l l } { { [ - \partial _ { x } ^ { 2 } + \tilde { u } ] \tilde { \psi } _ { + } = \lambda \tilde { \psi } _ { + } , \ } } & { { \tilde { \psi } _ { + } ( x + T , \lambda ) = e ^ { i \tilde { p } T } \tilde { \psi } _ { + } ( x , \lambda ) , } } \\ { { \nonumber } } \\ { { [ - \partial _ { x } ^ { 2 } + u ] \psi _ { - } = \lambda \psi _ { - } , \ } } & { { \psi _ { - } ( x + T , \lambda ) = e ^ { - i p T } \psi _ { - } ( x , \lambda ) . } } \end{array}
$$

则有如下等式:

$$
\partial _ { x } [ \tilde { \psi } _ { + } ^ { \prime } \psi _ { - } - \tilde { \psi } _ { + } \psi _ { - } ^ { \prime } ] = \delta u \tilde { \psi } _ { + } \psi _ { - } , \quad \delta u = \tilde { u } - u .
$$

在一周期内积分, 可得 $\delta u$ 的线性近似

$$
i \delta p \cdot T \cdot 2 i \chi _ { R } ( x _ { 0 } , \lambda ) = \int _ { x _ { 0 } } ^ { x _ { 0 } + T } \psi _ { + } \psi _ { - } \delta u \mathrm { d } x .
$$

又因为 $( \log \psi _ { + } \psi _ { - } ) _ { x } = - 2 \chi _ { I } = - ( \log \chi _ { R } ) _ { x }$ , 从而

$$
\psi _ { + } \psi _ { - } = { \frac { \chi _ { R } ( x _ { 0 } \lambda ) } { \chi _ { R } ( x , \lambda ) } } .
$$

因此

$$
\delta p = - \frac { 1 } { 2 T } \int _ { x _ { 0 } } ^ { x _ { 0 } + T } \frac { \delta u ( x ) } { \chi _ { R } ( x , \lambda ) } \mathrm { d } x .
$$

完成证明.

2.4 构造演化系统的不变环并寻找相应作用量-角参数的代数几何方法 (“有限空缺积分方法”)

考虑 KdV 方程簇的任一串流的稳定点

$$
\partial _ { x } \sum _ { i = 0 } ^ { n } 2 ^ { 2 ( i + 1 ) } c _ { n - i } v _ { i + 1 } ( u , u ^ { \prime } , . . . , u ^ { ( 2 i ) } ) = 0 ,
$$

其中 $c _ { 0 } , c _ { 1 } , . . . , c _ { n }$ 为归一化的常数, 例如满足归一化条件 $c _ { 0 } = 1$ , 或者等价地, 新增常数$c _ { n + 1 }$ 使得

$$
\sum _ { i = - 1 } ^ { n } 2 ^ { 2 ( i + 1 ) } c _ { n - i } v _ { i + 1 } ( u , u ^ { \prime } , . . . , u ^ { ( 2 i ) } ) = 0 .
$$

记方程(2.114)的解集为 $N _ { c }$ , 其中 $c = ( c _ { 0 } , . . . , c _ { n + 1 } )$ [见 2.2 节] . 此集合恰为以下泛函的驻点集:

$$
I _ { c } = \sum _ { i = - 1 } ^ { n } c _ { n - i } I _ { i + 1 } , \quad N _ { c } = \Bigl \{ u ( x ) \Bigl | \frac { \delta I _ { c } } { \delta u ( x ) } = 0 \Bigr \} 
$$

[见上一节(2.109)式] . 我们可用 2.2 节的想法来证明方程 (2.114)是完备哈密顿系统. 但这里我们要用另一种方法来积分此方程. 其关键之处在于, 方程(2.113)等价于矩阵微分算子 ${ \mathcal { L } } ( \lambda ) = \partial _ { x } - U ( \lambda )$ 与关于 $\lambda$ 的多项式矩阵

$$
W ( \lambda ) = - \sum _ { i = 0 } ^ { n } c _ { n - i } V _ { i } ( \lambda )
$$

[此矩阵的左乘作用视为算子] 交换,

$$
[ { \mathcal { L } } ( \lambda ) , W ( \lambda ) ] = 0 .
$$

其中矩阵 $V _ { i } ( \lambda )$ 形如上一节的(2.94). (2.117)等价于

$$
\partial _ { x } W ( \lambda ) = [ U ( \lambda ) , W ( \lambda ) ] .
$$

另外一种等价写法是常微分算子 $L$ 与 $A$ 的交换性

$$
[ L , A ] = 0 ,
$$

其中

$$
A = \sum _ { i = 0 } ^ { n } c _ { n - i } A _ { i } ,
$$

算子 $A _ { i }$ 的定义见上一节(2.94a)式. 方程(2.117) [或者(2.118),(2.119)] 的解集 $\hat { N } _ { c }$ 形如

$$
\hat { N } _ { c } = \bigcup _ { c _ { n + 1 } } N _ { c } ,
$$

此集合关于 KdV 方程簇的任何流的演化不变 [每个 $N _ { c }$ 也是不变的] .

由上一节(2.96)可知, 矩阵 $W ( \lambda )$ 也满足类似的关于 $t _ { k }$ 的演化方程 [对任意 $k ]$

$$
\partial _ { t _ { k } } W = [ V _ { k } , W ] .
$$

本节我们讲利用交换表示 (2.118),(2.122)来显式求解流形 $N _ { c }$ , 以及这些流形上的时间演化, 不变环. 简单起见, 我们只考虑关于第一个时间 $t = t _ { 1 }$ 的演化 [原始的 KdV 方程] .

考虑下述两两交换的算子的公共本征向量 [矩阵 $V _ { 1 } ( \lambda )$ 形如上一节(2.80)式]

$$
\mathcal { L } = \partial _ { x } - U ( \lambda ) , \quad \mathcal { A } _ { 1 } = \partial _ { t } - V _ { 1 } ( \lambda ) , \quad W ( \lambda ) ,
$$

$$
\mathcal { L } \vec { \psi } = 0 , \quad \mathcal { A } _ { 1 } \vec { \psi } = 0 , \quad W ( \lambda ) \vec { \psi } = i \mu \vec { \psi } .
$$

$\vec { \psi }$ 可被(2.123)式以及如下归一化条件完全确定:

$$
\psi | _ { \stackrel { x = x _ { 0 } } { t = t _ { 0 } } } = 1 , \quad \vec { \psi } = \binom { \psi } { \psi ^ { \prime } } .
$$

引理. 上述公共本征向量 $\vec { \psi }$ 是黎曼曲面

$$
\Gamma : \mathcal { R } ( \lambda , \mu ) \equiv \operatorname* { d e t } [ W ( \lambda ) - i \mu \cdot 1 ] \equiv \operatorname* { d e t } W ( \lambda ) - \mu ^ { 2 } = 0
$$

上的关于 $\lambda$ 的亚纯函数.

证明. 设 $\vec { \psi _ { 1 } } = { \binom { c } { c ^ { \prime } } } , \vec { \psi _ { 2 } } = { \binom { s } { s ^ { \prime } } }$ 为方程 $\mathcal { L } \vec { \psi } = 0$ , $\overset { \vartriangle } { \boldsymbol { A } _ { 1 } \boldsymbol { \vec { \psi } } } = 0$ 的满足下述归一化条件

$$
\left( { \begin{array} { l l } { c } & { s } \\ { c ^ { \prime } } & { s ^ { \prime } } \end{array} } \right) { \bmod { \frac { \textstyle } { } } } = { \binom { 1 } { 0 } } \ 0
$$

的解. 则本征函数 $\vec { \psi }$ 形如

$$
\vec { \psi } = \binom { \psi } { \psi ^ { \prime } } = \xi _ { 1 } \binom { c } { c ^ { \prime } } + \xi _ { 2 } \binom { s } { s ^ { \prime } } ,
$$

其中 $\binom { \xi _ { 1 } } { \xi _ { 2 } }$ 为矩阵 $W = W ( \lambda ) \vert _ { \mathbf { \lambda } _ { t = t _ { 0 } } } ^ { x = x _ { 0 } }$ 的本征向量, $W \left( { \xi _ { 1 } \atop { \xi _ { 2 } } } \right) = i \mu \left( { \xi _ { 1 } \atop { \xi _ { 2 } } } \right)$ 函数 $c , s$ 关于$\lambda \in \mathbb { C }$ 解析, 并且 $\xi _ { 1 } = \xi _ { 1 } ( \lambda ) \equiv 1$ , $\xi _ { 2 } = \xi _ { 2 } ( \lambda )$ 为黎曼曲面(2.125)上的代数函数.

我在 2.2 节提到, $x \cdot$ -演化方程与 $t { \cdot }$ -演化方程在有限维流形(2.115)上交换. 易知 $x \cdot$ -与$t \cdot$ -方程具有 Lax 表示

$$
\frac { \mathrm { d } W ( \lambda ) } { \mathrm { d } x } = [ U ( \lambda ) , W ( \lambda ) ] ,
$$

$$
\frac { \mathrm { d } W ( \lambda ) } { \mathrm { d } t } = [ V _ { 1 } ( \lambda ) , W ( \lambda ) ] .
$$

特征多项式 $\operatorname* { d e t } ( W ( \lambda ) - i \mu \cdot 1 ) = \mathcal { R } ( \lambda , \mu )$ 为关于 $u , u ^ { \prime } , . . . , u ^ { ( n + 1 ) }$ , $c _ { 0 } , . . . , c _ { n + 1 }$ 的多项式.

这给出了交换流(2.126),(2.127)的在 $( 3 n + 1 )$ 维相空间 $N$ 上的公共的运动常数族.黎曼曲面(2.125)将这族运动积分参数化. 它的方程形如

$$
\begin{array} { r } { \mathcal { R } ( \lambda , \mu ) \equiv \mu ^ { 2 } - R _ { 2 n + 1 } ( \lambda ) = 0 , \quad \mathrm { d e g } R _ { 2 n + 1 } = 2 n + 1 } \end{array}
$$

$$
R _ { 2 n + 1 } ( \lambda ) = \overbrace { \frac { \mathrm { H } } { \mathrm { H } } } ^ { 2 k + 1 } \overbrace { \frac { \mathrm { H } } { \mathrm { H } } } ^ { 2 k + 1 } \times \prod _ { \alpha = 0 } ^ { 2 k + 1 } ( \lambda - r _ { \alpha } ) = \operatorname* { d e t } W .
$$

$r _ { 1 } , . . . , r _ { 2 n + 1 }$ 给出了 (2.126),(2.127)的一族守恒律 [从而也是 KdV 方程在 $N _ { c }$ 上的限制的守恒律] .

由于

$$
W = \left( \begin{array} { c c } { { - \frac { 1 } { 2 } w _ { x } } } & { { w } } \\ { { - \frac { 1 } { 2 } w _ { x x } + w ( u - \lambda ) } } & { { \frac { 1 } { 2 } w _ { x } } } \end{array} \right) , \quad w = \sum _ { i = 0 } ^ { n } w _ { i } \lambda ^ { n - i } \equiv w ( x , t , \lambda ) ,
$$

$$
w _ { i } = - \sum _ { j } 2 ^ { 2 j } c _ { n - j } v _ { j + i - n }
$$

[回顾 $v _ { 0 } = 1$ , 且 $k > 0$ 时 $v _ { k } = v _ { k } ( u , u ^ { \prime } , . . . , u ^ { ( 2 k - 2 ) } ) \ ]$ , 从而我们得到公共本征函数

$\vec { \psi } = \binom { \psi } { \psi ^ { \prime } }$ 的显式表达式:

$$
\psi = c + \frac { i \mu + \frac { 1 } { 2 } w _ { x } ( x _ { 0 } , t _ { 0 } , \lambda ) } { w ( x _ { 0 } , t _ { 0 } , \lambda ) } s , \quad W \left( { \begin{array} { l } { \psi } \\ { \psi ^ { \prime } } \end{array} } \right) = i \mu \left( { \begin{array} { l } { \psi } \\ { \psi ^ { \prime } } \end{array} } \right) ,
$$

$$
\mu = \sqrt { \operatorname* { d e t } W }
$$

$[ \psi$ 的归一化条件为(2.124)] .

因此我们有

$$
\frac { \psi ^ { \prime } } { \psi } \bigg | _ { \stackrel { x = x _ { 0 } } { t = t _ { 0 } } } = \frac { i \mu + \frac { 1 } { 2 } w _ { x } ( x _ { 0 } , t _ { 0 } , \lambda ) } { w ( x _ { 0 } , t _ { 0 } , \lambda ) } .
$$

推论 2.11.

$$
\frac { \psi ^ { \prime } } { \psi } \equiv \frac { i \mu + \frac { 1 } { 2 } w _ { x } ( x , t , \lambda ) } { w ( x , t , \lambda ) } ,
$$

$$
\frac { \psi _ { t } } { \psi } = u _ { x } - 2 ( u + 2 \lambda ) \frac { i \mu + \frac { 1 } { 2 } w _ { x } ( x , t , \lambda ) } { w ( x , t , \lambda ) } = \frac { 1 } { 2 } \frac { w _ { t } } { w } - \frac { 2 i \mu ( \mu + 2 \lambda ) } { w } ,
$$

$u = u ( x , t )$

推论 2.12. 设 $\psi _ { \pm } = c + \frac { \pm i \mu + \frac { 1 } { 2 } w _ { x } ( x _ { 0 } , t _ { 0 } , \lambda ) } { w ( x _ { 0 } , t _ { 0 } , \lambda ) } s$ 为 2-值函数 $\psi$ 的两个分支. 则有

$$
\psi _ { + } \psi _ { - } = \frac { w ( x , t , \lambda ) } { w ( x _ { 0 } , t _ { 0 } , \lambda ) } .
$$

证明. 由(2.131),(2.132) 可得 [见上一节(2.112)式] :

$$
( \log \psi _ { + } \psi _ { - } ) ^ { \prime } = \frac { w _ { x } ( x , t , \lambda ) } { w ( x , t , \lambda ) } = [ \log w ( x , t , \lambda ) ] ^ { \prime } ,
$$

$$
( \log \psi _ { + } \psi _ { - } ) _ { t } = 2 u _ { x } - 2 ( u + 2 \lambda ) \frac { w _ { x } } { w } = [ \log w ( x , t , \lambda ) ] _ { t } .
$$

又由于(2.124), 从而积分后可得(2.133).

$2 n { + 1 }$ 定理 2.13. 亏格为 $n$ 的黎曼曲面 $\Gamma : \mu ^ { 2 } = \prod _ { \alpha = 1 } \left( \lambda - r _ { \alpha } \right)$ 上的关于 $\lambda$ 的亚纯函数$\psi = \psi ( x , x _ { 0 } , t _ { 0 } , \lambda )$ 具有以下 $n$ 个极点:

$$
P _ { 1 } = ( \gamma _ { 1 } ( x _ { 0 } , t _ { 0 } ) , \pm ) , . . . , P _ { n } = ( \gamma _ { n } ( x _ { 0 } , t _ { 0 } ) , \pm ) , \quad w ( x , t , \gamma _ { i } ( x , t ) ) \equiv 0 ,
$$

[符号“ $\cdot _ { + } ,$ ,“−”表示 $\Gamma$ 的不同叶 $\jmath$ , 并且在无穷远点 $\lambda = \infty$ 处有如下指数渐近:

$$
\psi ( x , x _ { 0 } , t _ { 0 } , \lambda ) = e ^ { i k ( x - x _ { 0 } ) - 4 i k ^ { 3 } ( t - t _ { 0 } ) } ( 1 + O ( k ^ { - 1 } ) ) , \quad k = \sqrt { \lambda } .
$$

证明. 由(2.130)可知函数 $\psi$ 的极点只能位于多项式 $w ( x _ { 0 } , t _ { 0 } , \lambda )$ 的根. 然而由(2.133)可知在每个这样的根处都是单极点. 因此该函数恰有 $n$ 个极点, 并且形如(2.134).

而由(2.131),(2.132) 可得指数渐近(2.135). 证毕.

亏格为 $n$ 的黎曼曲面上的具有上述解析性质的函数 $\psi$ 称为 Baker-Akhiezer 函数.若算子 $L$ [或者 $\mathcal { L } ( \lambda ) ]$ 的本征函数为 [关于 $\lambda$ 的] Baker-Akhiezer 函数, 则此算子称为有限空缺算子 (finite-gap operator) [下文将解释其背后动机] . 使得本征函数为亚纯函数的黎曼曲面 $\Gamma$ 称为该有限 gap 算子的 谱曲线 (spectral curve) . Baker-Akhiezer函数 $\psi$ 可由其极点 $P _ { 1 } , . . . , P _ { n }$ 唯一确定. 作为推论, 可以证明关于 KdV 方程的相应解的下述公式 [例如, 见 [11]] :

$$
u ( x , t ) = - 2 \partial _ { x } ^ { 2 } \log \theta ( k x + \omega t + \tau \vert B ) + c .
$$

其中 $\theta \ : = \ : \theta ( \tau | B )$ , $\tau = ( \tau _ { 1 } , . . . , \tau _ { n } )$ , $B = B ( r _ { 1 } , . . . , r _ { 2 n + 1 } )$ 为 $n \times n$ 矩阵, 为黎曼曲面$2 n { + 1 }$   
$\Gamma : \mu ^ { 2 } = \prod _ { \alpha = 1 } \left( \lambda - r _ { \alpha } \right)$ 的黎曼 $\theta \cdot$ -函数:

$$
\theta ( \tau | B ) = \sum _ { m _ { 1 } , \ldots , m _ { n } } \exp \left( - \frac { 1 } { 2 } \sum B _ { i j } m _ { i } m _ { j } + i \sum m _ { j } \tau _ { j } \right) ,
$$

$$
i B _ { i j } = \oint _ { \beta _ { j } } \Omega _ { i } , \quad i , j = 1 , . . . , n .
$$

此函数关于 $\tau _ { 1 } , . . . , \tau _ { n }$ 是 $2 \pi$ -周期的. 这里的 $\alpha _ { 1 } , . . . , \alpha _ { n }$ , $\beta _ { 1 } , . . . , \beta _ { n }$ 为黎曼曲面 $\Gamma$ 上适当

选取的闭链 (cycle) 构成的典范基, $\Omega _ { 1 } , . . . , \Omega _ { n }$ 为相应的全纯微分形式构成的基,

$$
\int _ { \alpha _ { i } } \Omega _ { j } = 2 \pi \delta _ { i j } , \quad \Omega _ { j } = \sum _ { q = 1 } ^ { n } c _ { j q } \frac { \lambda ^ { q - 1 } \mathrm { d } \lambda } { \sqrt { R _ { 2 n + 1 } ( \lambda ) } } .
$$

波数向量 $k = ( k _ { 1 } , . . . , k _ { n } )$ 与频率向量 $\omega = ( \omega _ { 1 } , . . . , \omega _ { n } )$ 是一些亚纯 Abel 微分的周期:

$$
\mathrm { d } p ( \lambda ) = \frac { P ( \lambda ) } { 2 \sqrt { R _ { 2 n + 1 } ( \lambda ) } } \mathrm { d } \lambda , \quad P ( \lambda ) = \lambda ^ { n } + a _ { 1 } \lambda ^ { n - 1 } + \cdot \cdot \cdot + a _ { n }
$$

$$
\oint _ { \alpha _ { j } } \mathrm { d } p ( \lambda ) = 0 , \quad j = 1 , . . . , n \Rightarrow a _ { s } = a _ { s } ( r _ { 1 } , . . . , r _ { 2 n + 1 } ) , \quad s = 1 , . . . , n ;
$$

$$
k _ { j } = \oint _ { \beta _ { j } } \mathrm { d } \boldsymbol { p } ( \lambda ) = k _ { j } ( r _ { 1 } , . . . , r _ { 2 n + 1 } ) , \quad j = 1 , . . . , n .
$$

$$
\mathrm { d } q ( \lambda ) = - \frac { 6 \lambda ^ { n + 1 } + Q ( \lambda ) } { \sqrt { R _ { 2 n + 1 } ( \lambda ) } } \mathrm { d } \lambda ,
$$

$$
Q ( \lambda ) = b _ { 0 } \lambda ^ { n } + b _ { 1 } \lambda ^ { n - 1 } + \cdots + b _ { n } , \quad b _ { 0 } = - 3 \sum _ { \alpha = 1 } ^ { 2 k + 1 } r _ { \alpha } ,
$$

$$
\oint _ { \alpha _ { j } } \mathrm { d } q ( \lambda ) = 0 , \quad b _ { j } = b _ { j } ( r _ { 1 } , . . . , r _ { 2 n + 1 } ) ,
$$

$$
\omega _ { j } = \oint _ { \beta _ { j } } \mathrm { d } q ( \lambda ) = \omega _ { j } \big ( r _ { 1 } , . . . , r _ { 2 n + 1 } \big ) , \quad j = 1 , . . . , n .
$$

最后还有,

$$
c = \sum r _ { \alpha } - 2 \sum _ { j = 1 } ^ { n } \oint _ { \alpha _ { j } } ^ { n } \lambda \Omega _ { j } = c ( r _ { 1 } , . . . , r _ { 2 n + 1 } ) .
$$

由形如(2.136)的显式表达式可知, 复化后的不变环 [即, 等值面

$$
\boldsymbol { r } _ { 1 } = \frac { \nu _ { \mathrm { H } ^ { \prime } } } { \hbar } \frac { \mathrm { H } } { 3 \mathcal { K } } , \quad \boldsymbol { r } _ { 2 } = \frac { \nu _ { \mathrm { H } ^ { \prime } } } { \hbar } \frac { \mathrm { H } } { 3 \mathcal { K } } , \cdot \cdot \cdot \boldsymbol { r } _ { 2 n + 1 } = \frac { \nu _ { \mathrm { H } ^ { \prime } } } { \hbar } \frac { \mathrm { H } } { 3 }
$$

] 为 [复化的] 阿贝尔簇 (Abelian variety) . 在此情形, 这个环面恰好是黎曼曲面 $\Gamma$ 的雅可比簇 (Jacobi variety) :

$$
J ( \Gamma ) = \mathbb { C } ^ { n } / { \Bigl \{ } 2 \pi M + i B N { \Bigl | } M , N \in \mathbb { Z } ^ { n } { \Bigr \} } .
$$

因此 KdV 方程的任何形如(2.136)的解可解析延拓为关于复变量 $x , t$ 的亚纯函数. 事实上这是非线性方程的可积性理论的“Kovalevskaja-Painleve-测试”的基本想法.

在 Liouville 环面紧致的情况下, 为描述我们的不变流形上的“光滑”区域, 我们回顾在此区域中的解 $\boldsymbol { u } ( \boldsymbol { x } , t )$ 是关于 $x , t$ 的周期或近似周期函数. 于是对数导数 $\psi _ { x } / \psi$ (2.131)与 $\psi _ { t } / \psi ( 2 . 1 3 2 )$ 也是关于 $x , t$ 的周期或近似周期函数 [且具有相同的周期群] . 因此我们得到

推论 2.14. 对于周期情形 $u ( x + T _ { x } , t ) = u ( x , t )$ , $u ( x , t + T _ { t } ) = u ( x , t )$ , 则公共本征函数 $\psi ( 2 . 1 2 3 )$ 是 Bloch-Floquet 函数 [见上一节附录]

$$
\begin{array} { r c l } { { \psi _ { \pm } ( x + T _ { x } , t , \lambda ) } } & { { = } } & { { e ^ { \pm i p ( \lambda ) T _ { x } } \psi _ { \pm } ( x , t , \lambda ) } } \\ { { } } & { { } } & { { } } \\ { { \psi _ { \pm } ( x , t + T _ { t } , \lambda ) } } & { { = } } & { { e ^ { \pm i q ( \lambda ) T _ { t } } \psi _ { \pm } ( x , t , \lambda ) . } } \end{array}
$$

这里的 $p = p ( \lambda )$ 称为“拟动量”, $q = q ( \lambda )$ 称为“拟能量”.

对于任意光滑周期或近似周期解 $u ( x , t )$ , 函数 $p ( \lambda ) , q ( \lambda )$ 定义为如下的平均值:

$$
p ( \lambda ) = \frac { 1 } { i } \overline { { ( \log \psi ) _ { x } } } , \quad q ( \lambda ) = \frac { 1 } { i } \overline { { ( \log \psi ) _ { t } } } .
$$

这里的

$$
{ \overline { { f ( x ) } } } = \operatorname* { l i m } _ { L \to \infty } { \frac { 1 } { 2 L } } \int _ { - L } ^ { L } f ( x ) \mathrm { d } x , \quad { \overline { { f ( t ) } } } = \operatorname* { l i m } _ { L \to \infty } { \frac { 1 } { 2 L } } \int _ { - L } ^ { L } f ( t ) \mathrm { d } t .
$$

于是函数 $p ( \lambda ) , q ( \lambda )$ 为黎曼曲面 $\Gamma$ 上的阿贝尔积分. 事实上它们关于 $\lambda$ 的微分恰好是关于适当的基 $\alpha _ { i } , \beta _ { i }$ 的之前定义的 [见(2.139),(2.140)] $\mathrm { d } p ( \lambda ) , \mathrm { d } q ( \lambda ) .$

在分支点 $\lambda = r _ { 1 } , . . . , \lambda = r _ { 2 n + 1 }$ 处成立 $\psi _ { + } = \psi _ { - }$ . 因此在 $x \cdot$ -周期情形, 这些点是问题 $L \psi = \lambda \psi$ , $L = - \partial _ { x } ^ { 2 } + u$ 的周期谱. 因此这些 $r _ { 1 } , . . . , r _ { 2 n + 1 }$ 为实数 [且互不相同] . 不妨$r _ { 1 } < r _ { 2 } < \cdot \cdot \cdot < r _ { 2 n + 1 }$ . 于是算子 $L$ 的周期系数的 Bloch 谱形如

$$
[ r _ { 1 } , r _ { 2 } ] , [ r _ { 3 } , r _ { 4 } ] , \ldots , [ r _ { 2 n + 1 } , \infty ] .
$$

于是该有限空缺算子只有有限多个“空缺”[即 $[ r _ { 2 } , r _ { 3 } ] , . . . , [ r _ { 2 n } , r _ { 2 n + 1 } ]$ 这 $n$ 个空缺] . [这也是我们叫它“有限空缺算子”的原因] .

可以证明 [3], 点 $\gamma _ { 1 } , . . . , \gamma _ { n }$ 位于这些空缺:

$$
\gamma _ { i } \in [ r _ { 2 i } , r _ { 2 i + 1 } ] , \quad i = 1 , . . . , n .
$$

取黎曼曲面 $\Gamma$ 上的闭链的一组典范基 $\alpha _ { 1 } , . . . , \alpha _ { n } , \beta _ { 1 } , . . . , \beta _ { n }$ , 使得闭链 $\alpha _ { i }$ 为两份第$i$ 个空缺 $[ r _ { 2 i } , r _ { 2 i + 1 } ]$ 的粘合. 选取 $\alpha _ { 1 } , . . . , \alpha _ { n }$ 的定向, 使得曲面 $\Gamma$ 沿着算子 $L$ 的谱割开后, 闭链 $\alpha _ { 1 } , . . . , \alpha _ { n }$ 在 $\mu < 0$ 的分支的部分取关于 $\lambda$ 增长的定向, 其中实数 $\lambda \gg 1$ . Γ的典范基中的 $\beta _ { 1 } , . . . , \beta _ { n }$ 的选取不唯一, 其不唯一性并不会影响后面的讨论. 取定这组闭链构成的基, 则得到由周期(2.137a)的实矩阵 $( B _ { i j } )$ . 相应的实 Liouville 环面恰为由$\tau = ( \tau _ { 1 } , . . . , \tau _ { n } ) , 0 \leq \tau _ { j } \leq 2 \pi$ 构成的集合; 相应的函数 $u$ 由(2.136)给出. 波数 $k _ { j }$ , 频率 $\omega _ { j }$ 以及平均值 $c$ [见(2.139)-(2.141)] 也是实数.

现在我们可以证明, 对于这组基, 由(2.139),(2.140)所确定的阿贝尔积分 $p ( \lambda ) , q ( \lambda )$ 恰为(2.143)的拟动量, 拟能量.

引理. 有限空缺算子的拟动量 $p ( \lambda )$ 以及拟能量 $q ( \lambda )$ (2.143)恰为黎曼曲面 $\Gamma$ [谱曲线] 的形如 (2.139),(2.140)的关于上述基的归一化条件的阿贝尔积分.

证明. 由上一节引理2.9可知

$$
\frac { \mathrm { d } p } { \mathrm { d } \lambda } \equiv \frac { \mathrm { d } } { \mathrm { d } \lambda } \frac { 1 } { T _ { x } } \int _ { 0 } ^ { T _ { x } } \chi \mathrm { d } x = \frac { 1 } { 2 T _ { x } } \int _ { 0 } ^ { T _ { x } } \frac { \mathrm { d } x } { \chi _ { R } } .
$$

然而 $\chi _ { R } = \mu / w$ . 因此

$$
\frac { \mathrm { d } p } { \mathrm { d } \lambda } = \frac { P ( \lambda ) } { 2 \sqrt { R _ { 2 n + 1 } ( \lambda ) } } .
$$

其中 $\sqrt { R _ { 2 n + 1 } ( \lambda ) } = \mu$

$$
P ( \lambda ) = \sum _ { i } \lambda ^ { n - i } \frac { 1 } { T _ { x } } \int _ { 0 } ^ { T _ { x } } w _ { i } ( x ) \mathrm { d } x .
$$

为得到关于 $\mathrm { d } q / \mathrm { d } \lambda$ 的类似公式, 我们要用等式

$$
\partial _ { t } ( \psi _ { + } ^ { \prime } \psi _ { - } - \psi _ { + } \psi _ { - } ^ { \prime } ) = \Delta c \psi _ { + } \psi _ { - } - \Delta b \psi _ { + } ^ { \prime } \psi _ { - } ^ { \prime } - \Delta a ( \psi _ { + } ^ { \prime } \psi _ { - } + \psi _ { + } \psi _ { - } ^ { \prime } )
$$

其中

$$
\partial _ { t } \left( \begin{array} { l } { { \psi _ { \pm } } } \\ { { \psi _ { \pm } ^ { \prime } } } \end{array} \right) = \left( \begin{array} { l l } { { a _ { \pm } } } & { { b _ { \pm } } } \\ { { c _ { \pm } } } & { { d _ { \pm } } } \end{array} \right) \left( \begin{array} { l } { { \psi _ { \pm } } } \\ { { \psi _ { \pm } ^ { \prime } } } \end{array} \right) ,
$$

$$
\Delta a = a _ { + } - a _ { - } , \quad \Delta b = b _ { + } - b _ { - } , \quad \Delta c = c _ { + } - c _ { - } ,
$$

将此式用于 $\psi _ { - } = \psi _ { - } ( x , t , \lambda )$ 的情形, 有

$$
\begin{array} { l } { { \psi _ { - } ( x , t + T _ { t } , \lambda ) = \exp ( - i q ( \lambda ) T _ { t } ) \psi _ { - } ( x , t , \lambda ) ; \quad \psi _ { + } = \psi _ { + } ( x , t , \lambda + \Delta \lambda ) , } } \\ { { \psi _ { + } ( x , t + T _ { t } , \lambda + \Delta \lambda ) = \exp ( i q ( \lambda + \Delta \lambda ) T _ { t } ) \psi _ { + } ( x , t , \lambda + \Delta \lambda ) , } } \\ { { \quad \left( \begin{array} { c c } { { a _ { - } } } & { { b _ { - } } } \\ { { c _ { - } } } & { { - a _ { - } } } \end{array} \right) = \left( \begin{array} { c c } { { u ^ { \prime } } } & { { - 2 ( u + 2 \lambda ) } } \\ { { u ^ { \prime \prime } - 2 ( u - \lambda ) ( u + 2 \lambda ) } } & { { - u ^ { \prime } } } \end{array} \right) } } \end{array}
$$

[见上一节(2.80)式] , 而矩阵 $\left( \begin{array} { c c } { { a _ { + } } } & { { b _ { + } } } \\ { { c _ { + } } } & { { - a _ { + } } } \end{array} \right)$ 具有与其相同的形式, 只需把 $\lambda$ 换成 $\lambda + \Delta \lambda$

将上述等式作关于 $t$ 的沿一周期 $T _ { t }$ 的积分, 经计算可得

$$
\frac { \mathrm { d } q } { \mathrm { d } \lambda } = - \frac { 6 \lambda ^ { n + 1 } + Q ( \lambda ) } { \sqrt { R _ { 2 n + 1 } ( \lambda ) } } ,
$$

其中

$$
6 \lambda ^ { n + 1 } + Q ( \lambda ) = \frac { 1 } { T _ { t } } \int _ { 0 } ^ { T _ { t } } [ 3 ( 2 \lambda - u ) w + w _ { x x } ] \mathrm { d } t .
$$

[对于拟周期情形, 可在公式(2.147), (2.149)当中使用形如(2.143)的平均化方法. ] 由(2.146),(2.148)可知 $p ( \lambda ) , q ( \lambda )$ 为黎曼曲面 $\Gamma$ 上形如(2.139),(2.140) 的阿贝尔积分. 我们只需证明归一化条件 $\oint _ { \alpha _ { j } } \mathrm { d } p = 0$ , $\oint _ { \alpha _ { j } } \mathrm { d } q = 0$ , $j = 1 , . . . , n$ . 为证明它, 我们注意在周期情形$\exp i p ( \lambda ) T _ { x }$ , $\exp i q ( \lambda ) T _ { t }$ 是关于 $\lambda$ 的单值函数 [因此, 是 $\Gamma$ 上的单值函数] . 因此 $\Gamma$ 上的阿贝尔微分 $\mathrm { d } p , \mathrm { d } q$ 的周期一定分别是 $2 \pi / T _ { x }$ , $2 \pi / T _ { t }$ 的整数倍. 对于拟周期情形, 这些周期仍然是实数. 但是下述微分

$$
\mathrm { d } p = \frac { P ( \lambda ) \mathrm { d } \lambda } { 2 \sqrt { R _ { 2 n + 1 } ( \lambda ) } } , \quad \mathrm { d } q = - \frac { 6 \lambda ^ { n + 1 } + Q ( \lambda ) } { \sqrt { R _ { 2 n + 1 } ( \lambda ) } } \mathrm { d } \lambda
$$

在前文所述的闭链 $\alpha _ { j }$ 上的周期是纯虚数, 这是因为(2.147), (2.149)中的多项式 $P ( \lambda ) , Q ( \lambda )$ 是实系数的. 因此这些 $\alpha _ { j }$ -周期为零. 证毕. □

函数 $k _ { 1 } ( r ) , . . . , k _ { n } ( r )$ 显然是 Gardner-Zakharov-Faddeev 泊松括号的零因子 [因为其倒数 $2 \pi / k _ { i } ( r )$ 为周期] . 因此函数 $c ( r ) = \overline { { u } }$ 也是此泊松括号的零因子. KdV 方程在关于这些零因子的等值面

上的限制是 $n$ 自由度的完备可积哈密顿系统. 变量 $\tau _ { 1 } , . . . , \tau _ { n }$ 为相应的角参数. 而变量$\gamma _ { 1 } , . . . , \gamma _ { n }$ 给出了积分 $r _ { 1 } , . . . , r _ { 2 n + 1 }$ 的等值面上的另一组坐标系. $\tau _ { 1 } , . . . , \tau _ { n }$ 可由 $\gamma _ { 1 } , . . . , \gamma _ { n }$ 通过如下阿贝尔变换得到:

$$
\tau _ { j } = \frac { 1 } { i } \left\{ \sum _ { k = 1 } ^ { n } \int _ { P _ { 0 } } ^ { P _ { k } = ( \gamma _ { k } , \pm ) } \Omega _ { j } + { \mathcal K } _ { j } \right\} , \quad j = 1 , . . . , n ,
$$

其中 $\kappa _ { j }$ 为黎曼常数 [41],

$$
\mathcal { K } _ { j } = \frac { 2 \pi i - B _ { j j } } { 2 } + \frac { 1 } { 2 \pi i } \sum _ { k \neq j } \oint _ { \alpha _ { k } } \left( \Omega _ { k } ( P ) \int _ { P _ { 0 } } ^ { P } \Omega _ { j } \right) ,
$$

$P _ { 0 }$ 为黎曼曲面 $\Gamma$ 上的任意的点.

寻找作用量 $J _ { 1 } , . . . , J _ { n }$ 的关键是如下断言 (Flaschka, McLaughlin[21]):

定理 2.15. 下式成立:

$$
\{ \gamma _ { i } , \gamma _ { j } \} = \{ p ( \gamma _ { i } ) , p ( \gamma _ { j } ) \} = \{ r _ { \alpha } , r _ { \beta } \} = 0 ,
$$

$$
\{ p ( \gamma _ { i } ) , \gamma _ { j } \} = \delta _ { i j } .
$$

其中 $\{ , \}$ 为 Gardner-Zakharov-Feddeev 泊松括号, $p = p ( \lambda )$ 为(2.143)的拟动量.

注意到点 $\gamma _ { k }$ 恰好在闭链 $\alpha _ { k }$ 上, $k = 1 , . . . , n$ . 于是由此定理立刻得到, 作用量$J _ { 1 } , . . . , J _ { n }$ 可通过下述公式来计算:

$$
J _ { k } = \frac { 1 } { 2 \pi } \oint _ { \alpha _ { k } } p ( \gamma ) \mathrm { d } \gamma , \quad k = 1 , . . . , n .
$$

此公式是非常一般的解析泊松括号 (Novikov, Veselov[1]) 的构造的一个特例. 我将给出“KdV 型”[或者“有限空缺型”] 相空间情形下的解析泊松括号的一般概念. 在此情形, 相空间 $P$ 中的一个点可以由参数 $r _ { 1 } , . . . , r _ { 2 n + 1 } , \gamma _ { 1 } , . . . , \gamma _ { n }$ 所唯一确定. 这里的$r _ { 1 } , . . . , r _ { 2 n + 1 }$ 为亏格 $n$ 的黎曼曲面上的参数 [在我们的例子中是分支点] , $\gamma _ { 1 } , . . . , \gamma _ { n }$ 为 $\Gamma$ 上的点. 取定一族函数 $x _ { 0 } ( r ) , . . . , x _ { n } ( r )$ 作为解析泊松括号的零因子的一组生成元. 于是相空间上的解析泊松括号被 $\Gamma$ [或它的某个覆盖空间] 上的取定的亚纯 1-形式 $Q ( \lambda , r ) \mathrm { d } \lambda$ 所确定, 其中 $Q ( \lambda , r ) \mathrm { d } \lambda$ 与黎曼曲面 $\Gamma$ 有关 [即与 $r$ 有关] , 满足

1. 对于关于零因子 $x _ { 0 } ( r ) , . . . , x _ { n } ( r )$ 的等值面上的任何曲线 $r _ { \alpha } = r _ { \alpha } ( s )$ ,

$$
\frac { \partial } { \partial s } [ Q ( \gamma , r ( s ) \mathrm { d } \gamma ) ] _ { x _ { \alpha } ( r ( s ) ) = \sqrt { \sharp ^ { * } } \sharp \zeta } , \quad \alpha = 0 , 1 , . . . , n
$$

为 $\Gamma$ 上的全纯微分.

2. 泊松括号满足以下:

$$
\begin{array} { l } { { \{ \gamma _ { i } , \gamma _ { j } \} = \{ Q ( \gamma _ { i } ) , Q ( \gamma _ { j } ) \} = \{ r _ { \alpha } , r _ { \beta } \} = 0 , } } \\ { { \{ Q ( \gamma _ { i } ) , \gamma _ { j } \} = \delta _ { i j } . } } \end{array}
$$

[某种意义下的“分离变量”] .

于是 [在 $Q$ 取实值且 1-形式 $Q ( \lambda , r ) \mathrm { d } \lambda$ 的导函数(2.155)线性无关的假设下] 可以证明对于 $\gamma$ 上的适当的闭链 $a _ { 1 } , . . . , a _ { n }$ , 作用量可由下式计算:

$$
J _ { k } = \frac { 1 } { 2 \pi } \oint _ { a _ { k } } Q ( \gamma ) \mathrm { d } \gamma , \quad k = 1 , . . . , n .
$$

而角参数 $\tau _ { 1 } , . . . , \tau _ { n }$ 可由阿贝尔变换(2.151)得到. [其证明见 [2]] . 对于 Gardner-Zakharov-Faddeev 泊松括号, 微分形式 $Q \mathrm { d } \lambda$ 为 $p ( \lambda ) \mathrm { d } \lambda$ [见(2.153)] . 对于 Magri 括号[见上一节] , 微分形式 $Q \mathrm { d } \lambda$ 为 $p ( \lambda ) \mathrm { d } \lambda / \lambda$ . 解析泊松括号的其他例子可见 [1],[2],[7],[14].

例子. KdV 方程的 单波 (simple wave) 形如

$$
u = 2 \wp ( x - c t - x _ { 0 } - \omega ^ { \prime } ) + { \frac { c } { 6 } } ,
$$

其中任取相位 $x _ { 0 }$ 与速度 $c$ . 这里的 $\wp = \wp ( z | g _ { 2 } , g _ { 3 } )$ 为 Weierstrass 椭圆函数 [可见 [48]], 它满足方程

$$
\wp ^ { \prime } ^ { 2 } = 4 \wp ^ { 3 } - g _ { 2 } \wp - g _ { 3 } .
$$

其中参数 $g _ { 2 } , g _ { 3 }$ 为实数, 且满足

$$
g _ { 2 } ^ { 3 } - 2 7 g _ { 3 } ^ { 2 } > 0 ,
$$

即多项式 $4 x ^ { 3 } - g _ { 2 } x - g _ { 3 }$ 具有三个互异的实根. 把这三个实根记作 $e _ { 1 } , e _ { 2 } , e _ { 3 }$ ,

$$
4 e _ { \alpha } ^ { 3 } - g _ { 2 } e _ { \alpha } - g _ { 3 } = 0 , \quad \alpha = 1 , 2 , 3 ,
$$

$$
e _ { 3 } < e _ { 2 } < e _ { 1 } .
$$

关于复变量 $z$ 的函数 $\wp ( z )$ 具有两个实线性无关的周期 $2 \omega , 2 \omega ^ { \prime }$ ,

$$
\begin{array} { l } { \omega = \displaystyle \int _ { e _ { 3 } } ^ { e _ { 2 } } \frac { \mathrm { d } z } { \sqrt { 4 z ^ { 3 } - g _ { 2 } z - g _ { 3 } } } , \quad \mathrm { I m } \omega = 0 , \quad \omega > 0 , } \\ { \omega ^ { \prime } = \displaystyle \int _ { e _ { 1 } } ^ { e _ { 2 } } \frac { \mathrm { d } z } { \sqrt { 4 z ^ { 3 } - g _ { 2 } z - g _ { 3 } } } , \quad \mathrm { R e } \omega ^ { \prime } = 0 , \quad \frac { 1 } { i } \omega ^ { \prime } > 0 . } \end{array}
$$

解(2.158)也可用其它类型的椭圆函数 [例如椭圆余弦函数 $\mathrm { c n } ]$ ; 从而它有时也叫做 椭圆余弦波 (cnoidal wave) .

我们有

$$
2 e _ { 3 } + \frac { c } { 6 } \leq u \leq 2 e _ { 2 } + \frac { c } { 6 } .
$$

若 $e _ { 2 } \ \to \ e _ { 3 }$ , 则解(2.158)趋于常值 $\frac { c } { 6 } - e _ { 1 } = \frac { c } { 6 } + 2 e _ { 3 }$ . 若 $e _ { 2 } \ \to \ e _ { 1 }$ , $c = - 1 2 e _ { 1 }$ , 则解(2.158)变为孤子.

需要求解的方程 $- c u ^ { \prime } + 6 u u ^ { \prime } - u ^ { \prime \prime \prime } = 0$ 可表示为 Lax 形式 (2.126), 其中

$$
W ( \lambda ) = \left( \begin{array} { c c } { { u ^ { \prime } } } & { { - 2 ( u + 2 \lambda ) } } \\ { { u ^ { \prime \prime } - 2 ( u - \lambda ) ( u + 2 \lambda ) } } & { { - u ^ { \prime } } } \end{array} \right) + c \left( \begin{array} { c c } { { 0 } } & { { 1 } } \\ { { u - \lambda } } & { { 0 } } \end{array} \right)
$$

[见上一节(2.80)式] . 于是解(2.158)的谱曲线形如

$$
\begin{array} { l } { { \mu ^ { 2 } = \operatorname* { d e t } W ( \lambda ) = 1 6 \lambda ^ { 3 } - 8 c \lambda ^ { 2 } + 4 \lambda \left( u ^ { \prime \prime } - 3 u ^ { 2 } + c u + \frac { c ^ { 2 } } { 4 } \right) } } \\ { { \phantom { \mu ^ { 2 } = \operatorname* { d e t } W ( \lambda ) = 1 6 \lambda ^ { 3 } - 8 c u ^ { 2 } + ( 2 u - c ) ( u ^ { \prime \prime } - 2 u ^ { 2 } + c u ) } } } \\ { { \phantom { \mu ^ { 2 } = \operatorname* { d e t } W ( \lambda ) = 1 6 \lambda ^ { 3 } - 9 c \lambda ^ { 2 } + 4 \lambda \left( u ^ { \prime \prime } - 3 u ^ { 2 } + c u - \frac { c ^ { 2 } } { 4 } \right) } . } } \end{array}
$$

该曲线的分支点 $r _ { 1 } , r _ { 2 } , r _ { 3 }$ 形如

$$
r _ { \alpha } = \frac { c } { 6 } - e _ { \alpha } , \quad \alpha = 1 , 2 , 3 , \quad r _ { 1 } < r _ { 2 } < r _ { 3 } .
$$

考虑此曲线的椭圆单值化

$$
\lambda = \frac { c } { 6 } - \wp ( z ) , \quad \mu = 2 i \wp ^ { \prime } ( z )
$$

是方便的, 其中 $\wp$ 依然是之前的椭圆函数 $\wp ( z | g _ { 2 } , g _ { 3 } )$ . 线段 $[ \omega , \omega ^ { \prime } + \omega ]$ 与 $[ \omega ^ { \prime } , 0 ]$ 为算子$L = - \partial _ { x } ^ { 2 } + u$ 的谱构成的区域, 其中 $u$ 形如(2.158); 而线段 $( \omega + \omega ^ { \prime } , \omega ^ { \prime } )$ 为其谱的空缺.相应的拟动量, 拟能量 (2.139), (2.140)的阿贝尔微分 $\mathrm { d } p , \mathrm { d } q$ 由下式给出:

$$
\begin{array} { r c l } { { \displaystyle \mathrm { d } { \boldsymbol { p } } } } & { { = } } & { { i \left[ \wp ( z ) + \displaystyle \frac { \eta } { \omega } \right] \mathrm { d } z , } } \\ { { \mathrm { d } { \boldsymbol { q } } } } & { { = } } & { { i \left[ 1 2 \wp ^ { 2 } ( z ) - c \wp ( z ) - g _ { 2 } - c \displaystyle \frac { \eta } { \omega } \right] \mathrm { d } z , } } \end{array}
$$

$$
\int _ { \omega ^ { \prime } } ^ { \omega + \omega ^ { \prime } } \mathrm { d } p = \int _ { \omega ^ { \prime } } ^ { \omega + \omega ^ { \prime } } \mathrm { d } q = 0 .
$$

这里的 $\eta = - \int _ { \omega ^ { \prime } } ^ { \omega + \omega ^ { \prime } } \wp ( z ) \mathrm { d } z .$ .

我们将在第三章使用此公式.

# 第 3 章 场论哈密顿系统的慢摄动与平均化方法

# 3.1 演化系统在不变环上的泊松括号的平均化

Poincaré-Bogoliubov 平均化方法是非线性力学里面众所周知的有效方法. 此方法可用于描述非摄动情形下具有一族不变环的动力系统的摄动解的行为. 其中“平均化方程”描述了这族不变环的某邻域中的点沿着这族不变环的参数空间的缓慢移动.

对于场论版本的平均化方法, 我们研究如下演化系统

$$
w _ { t } = K ( w , w ^ { \prime } , . . . , w ^ { ( m ) } ) , \quad w = ( w ^ { a } ( x , t ) )
$$

[我们只考虑空间 1 维情形] , 并假定该系统具有形如

$$
w ( x , t ) = \Phi ( k x + \omega t + \tau ^ { 0 } ; u ^ { 1 } , . . . , u ^ { N } )
$$

的一族关于 $x , t$ 的周期或近似周期解 [“ $\cdot _ { n } .$ -相解”, 或者“孤子格族”] . 这里的 $u \ =$ $( u ^ { 1 } , . . . , u ^ { N } )$ 为这族解的参数, [向量值] 函数 $\Phi ( \tau , u )$ , $\tau = ( \tau _ { 1 } , . . . , \tau _ { n } )$ 关于每个 $\tau _ { j }$ 都是周期 $2 \pi$ 的; 波数向量 $\boldsymbol { k } = ( k _ { 1 } , . . . , k _ { n } )$ 与频率向量 $\omega = ( \omega _ { 1 } , . . . , \omega _ { n } )$ 被参数 $u$ 唯一决定: $k = k ( u )$ , $\omega = \omega ( u )$ ; 相位 $\tau ^ { 0 } = ( \tau _ { 1 } ^ { 0 } , . . . , \tau _ { n } ^ { 0 } )$ 为任意向量.

[这里应该注意, 线性演化系统的 单相解 (one-phase solution)

$$
w ( x , t ) = u e ^ { i ( k x + \omega t ) }
$$

当中的 $k , \omega$ 与振幅 $u$ 无关, 而被某些色散关系 $f ( k , \omega ) = 0$ 所约束. 其 多相解 (mut-liphase solution) 形如单相解的线性组合

$$
w ( x , t ) = \sum _ { j = 1 } ^ { n } u ^ { j } e ^ { i ( k _ { j } x + \omega _ { j } t ) } , \quad f ( k _ { j } , \omega _ { j } ) = 0 .
$$

而在非线性情形中有两个重要的特性. 其一是: 色散关系形如 $k = k ( u )$ , $\omega = \omega ( u )$ (即波数, 频率与某种版本的振幅之间的联系). 其二是: 多相解是单相解的非线性叠加 (事实上这种非线性叠加只出现于可积演化系统) ] .

在最简单版本的摄动理论中, 我们不摄动演化系统, 仅摄动初始条件. 我们要求解系统(3.1)的渐近解, 使得此解关于自然小参数 $\varepsilon$ 的一阶近似的领头项为(3.2), 其中 $\varepsilon$ 为时空尺度的“快”与“慢”之比. 此时, 参数 $\boldsymbol { u } ^ { 1 } , . . . , \boldsymbol { u } ^ { N }$ 不再是常数, 而是关于 $x , t$ 缓慢变化的函数:

$$
u ^ { i } = u ^ { i } ( \varepsilon x , \varepsilon t ) .
$$

于是参数 $u ^ { 1 } ( X , T ) , . . . , u ^ { N } ( X , T )$ , $X = \varepsilon x$ , $T = \varepsilon t$ 满足流体力学型系统

$$
u _ { T } ^ { i } = v _ { j } ^ { i } ( u ) u _ { X } ^ { j } , \quad i = 1 , . . . , N ,
$$

[此系统称为“慢调制方程 (equation of slow modulation) ”, 也叫做“惠特姆平均化方程(Whitham averaged equation) ”, 或者叫做“孤子格的流体力学型方程”] . 其系数矩阵$( v _ { j } ^ { i } ( u ) )$ 与系统(3.1)与解族(3.2)有关. 我们将证明 (Dubrovin, Novikov[10]), 对于哈密顿系统(3.1), 其平均化系统(3.3)也具有哈密顿结构; 并且“平均化泊松括号”是流体力学型的. 从而平均化系统(3.3)也继承了系统(3.1)的可积性.

首先我要说一下“平均化”的一些想法, 即如何由(3.1), (3.2)得到(3.3). 我们来寻找方程(3.1)的形如

$$
w ( x , t ) = w _ { 0 } ( x , t ) + \varepsilon w _ { 1 } ( x , t ) + \cdot \cdot \cdot
$$

的关于 $\varepsilon \to 0$ 的 [形式] 渐近解, 其中

$$
w _ { 0 } ( x , t ) = \Phi ( \varepsilon ^ { - 1 } S ( X , T ) ; u ( X , T ) ) , \quad X = \varepsilon x , \quad T = \varepsilon t ,
$$

$S = ( S _ { 1 } , . . . , S _ { n } )$ ; 以及

$$
w _ { k } ( x , t ) = \Phi _ { k } ( \varepsilon ^ { - 1 } S ( X , T ) ; X , T ) ,
$$

其中函数 $\Phi _ { k } ( \tau ; X , T )$ 关于每个 $\tau _ { j }$ 都是 $2 \pi \cdot$ -周期的, $\tau = ( \tau _ { 1 } , . . . , \tau _ { n } )$ . 将(3.4)代入(3.1), 考虑 $\varepsilon$ 的零阶近似, 得到

$$
S _ { X } = k ( u ( X , T ) ) , \quad S _ { T } = \omega ( u ( X , T ) ) .
$$

[此方程等价于 $\varepsilon \to 0$ 时 (3.5)的领头项在区域 $| x | < \varepsilon ^ { - 1 } , | t | < \varepsilon ^ { - 1 }$ 当中收敛于解(3.2) ] .

考虑下一阶近似, 我们得到如下线性系统:

$$
\mathcal { L } \Phi _ { k } = F _ { k } , \quad k = 1 , 2 , \ldots
$$

[此处 $\Phi _ { k } = \Phi _ { k } ( \tau ; X , T ) ]$ , $\mathcal { L }$ 为系统(3.1)在“点”(3.2)的“线性化”. 确切地说, 在 $\mathcal { L }$ 中我们记 $( k , \partial _ { \tau } ) = k _ { 1 } \partial _ { \tau _ { 1 } } + \cdot \cdot \cdot + k _ { n } \partial _ { \tau _ { n } }$ 而不是 $x \cdot$ -导数; 记 $( \omega , \partial _ { \tau } ) = \omega _ { 1 } \partial _ { \tau _ { 1 } } + \cdot \cdot \cdot + \omega _ { n } \partial _ { \tau _ { n } }$ 而不是 $t \mathrm { - }$ -导数. 从而算子

$$
\mathcal { L } = ( \omega , \partial _ { \tau } ) - \frac { \partial K } { \partial w } - \frac { \partial K } { \partial w _ { x } } ( k , \partial _ { \tau } ) - \cdot \cdot \cdot
$$

作用于 $L _ { 2 } ( T ^ { n } )$ . 它与慢参数 $X = \varepsilon x , T = \varepsilon t$ 有关. 等号右边的 $F _ { k }$ 是关于 $u ^ { 1 } , . . . , u ^ { N }$ ,$w _ { 0 } , . . . , w _ { k - 1 }$ 及其关于 $X , T$ 的导数的函数. 由(3.6)可得相容性关系

$$
k _ { T } = \omega _ { X } .
$$

平均化方程的另一部分则是(3.7)的第一个方程 [即 $k = 1 ]$ 在 $L _ { 2 } ( T ^ { n } )$ 的可解性条件, 它形如

$$
\ker \mathcal { L } ^ { \ast } \bot F _ { 1 }
$$

$[ \mathcal { L } ^ { * }$ 是算子 $\mathcal { L }$ 的伴随] .

易知上述正交性条件以及相容性条件(3.8) 构成的方程组形如(3.3).

得到平均化方程(3.3)的更方便的方法由 Whitham[37] 提出 [但它纯粹是启发性的想法] . 我们假设演化系统(3.1)具有 $N$ 个局部守恒律

$$
I _ { j } = \int P _ { j } ( w , w ^ { \prime } , w ^ { \prime \prime } , . . . ) \mathrm { d } x , \quad j = 1 , . . . , N .
$$

设 $Q _ { j } = Q _ { j } ( w , w ^ { \prime } , \ldots )$ 为相应的流密度:

$$
\frac { \partial P _ { j } } { \partial t } = \frac { \partial Q _ { j } } { \partial x } , \quad j = 1 , . . . , N .
$$

定义平均化函数

$$
\begin{array} { r c l } { \overline { { P } } _ { j } } & { = } & { \overline { { P } } _ { j } ( \boldsymbol { u } ) = ( 2 \pi ) ^ { - n } \displaystyle \int P _ { j } ( \Phi ( \tau ; \boldsymbol { u } ) , \ldots ) \mathrm { d } ^ { n } \tau = I _ { j } , } \end{array}
$$

$$
\overline { { { Q } } } _ { j } = \overline { { { Q } } } _ { j } ( u ) = ( 2 \pi ) ^ { - n } \int Q _ { j } ( \Phi ( \tau ; u ) , \ldots ) \mathrm { d } ^ { n } \tau .
$$

则平均化系统形如

$$
\frac { \partial \overline { { { P } } } _ { j } ( u ) } { \partial T } = \frac { \partial \overline { { { Q } } } _ { j } ( u ) } { \partial X } , \quad j = 1 , . . . , N .
$$

如果 $\operatorname* { d e t } ( \partial \overline { { P } } _ { j } ( u ) / \partial u ^ { i } ) \neq 0$ , 则此系统具有(3.3)的形式.

“证明”. 将守恒律

$$
\partial _ { t } P ( w ( x ) , w _ { x } ( x ) , . . . ) = \partial _ { x } Q ( w ( x ) , w _ { x } ( x ) , . . . )
$$

中的 $w ( x , t )$ 换成 $w _ { 0 } ( x , X , t , T ) + \varepsilon w _ { 1 } ( x , X , t , T ) + \cdot \cdot \cdot$ ; 并且同时把 $\partial _ { x }$ 换成 $\partial _ { x } + \varepsilon \partial _ { X }$ ,把 $\partial _ { t }$ 换成 $\partial _ { t } + \varepsilon \partial _ { T }$ . 这样会得到

$$
\begin{array} { r l } & { \partial _ { t } P ( w _ { 0 } + \varepsilon w _ { 1 } , . . . ) + \varepsilon \partial _ { T } P ( w _ { 0 } , w _ { 0 _ { x } } , . . . ) } \\ { = } & { \partial _ { x } Q ( w _ { 0 } + \varepsilon w _ { 1 } , . . . ) + \varepsilon \partial _ { X } Q ( w _ { 0 } , . . . ) + O ( \varepsilon ^ { 2 } ) . } \end{array}
$$

现在我们对此等式采取平均化的操作. 由于对任意的 [属于我们讨论的函数类的] 函数 $f$ 都有 ${ \overline { { \partial _ { x } f } } } = { \overline { { \partial _ { t } f } } }$ , 从而除以 $\varepsilon$ , 再令 $\varepsilon \to 0$ 得到

$$
\partial _ { T } \overline { { { P } } } = \partial _ { X } \overline { { { Q } } } .
$$

我要继续去定义“平均化哈密顿理论 (averaged Hamiltonian formalism) ”. 假设演化系统(3.1)是哈密顿场论系统, 具有如下的局部泊松括号

$$
\{ w ^ { a } ( x ) , w ^ { b } ( y ) \} = \sum _ { k } A _ { k } ^ { a b } ( w ( x ) , w ^ { \prime } ( x ) , . . . ) \delta ^ { ( k ) } ( x - y ) ,
$$

相应的哈密顿量为

$$
H [ w ] = \int h ( w , w ^ { \prime } , \ldots ) \mathrm { d } x .
$$

我们还假设系统(3.1)的守恒律(3.9)两两交换, 即 $\{ I _ { i } , I _ { j } \} = 0$ .

在不变环面(3.2)的参数空间中的适当选取的特殊坐标 $u ^ { 1 } , . . . , u ^ { N }$ 下, 泊松括号(3.12)关

于解(3.2)的平均化具有最简单的形式. 该特殊坐标正是守恒量 $I _ { 1 } , . . . , I _ { N }$ :

$$
u ^ { j } = I _ { j } [ \Phi ] , \quad j = 1 , . . . , N .
$$

平均化泊松括号 $\{ , \}$ 平均 是场 $u ^ { 1 } ( X ) , . . . , u ^ { N } ( X )$ 的相空间上的流体力学型泊松括号:

$$
\{ u ^ { i } ( X ) , u ^ { j } ( Y ) \} _ { \# \# \mathcal { H } } = g ^ { i j } ( u ( X ) ) \delta ^ { \prime } ( X - Y ) + b _ { k } ^ { i j } ( u ) u _ { X } ^ { k } \delta ( X - Y ) .
$$

为给出显式公式, 考虑泛函 $I _ { 1 } , . . . , I _ { N }$ 的密度之间的泊松括号:

$$
\{ P _ { i } ( w ( x ) , . . . ) , P _ { j } ( w ( y ) , . . . ) \} = \sum { B } _ { k } ^ { i j } ( w ( x ) , w ^ { \prime } ( x ) , . . . ) \delta ^ { ( k ) } ( x - y )
$$

[上述求和是有限求和] . 由交换性 $\{ I _ { i } , I _ { j } \} = 0$ 可得

$$
\int B _ { 0 } ^ { i j } \mathrm { d } x \equiv 0 \Longleftrightarrow B _ { 0 } ^ { i j } = \partial _ { x } Q ^ { i j } ( w ( x ) , \ldots ) .
$$

我们记

$$
g ^ { i j } ( u ) = \overline { { B _ { 1 } ^ { i j } } } ,
$$

$$
b _ { k } ^ { i j } ( u ) = \frac { \partial } { \partial u ^ { k } } \overline { { Q ^ { i j } } }
$$

[即在环面(3.2)的平均值] .

定理 3.1. 上述公式确定了流体力学型泊松括号(3.13). 平均化系统(3.11)是关于泊松括号(3.13)的哈密顿系统, 相应的哈密顿量为

$$
H _ { \Phi \Psi } = \int { \overline { { h ( \Phi , \ldots ) } } } \mathrm { d } X = \int H [ \Phi ] \mathrm { d } X .
$$

证明. 首先断言(3.13)-(3.16a)的确定义了一个泊松括号. 为此我们在场 $w ^ { a } ( x , X )$ 的空间中引入泊松括号, 此泊松括号由(3.12)通过如下替换所得到:

$$
\begin{array} { r c l } { { w ( x ) } } & { { \mapsto } } & { { w ( x , X ) } } \\ { { } } & { { } } & { { } } \\ { { \partial _ { x } } } & { { \mapsto } } & { { \partial _ { x } + \varepsilon \partial _ { X } } } \\ { { } } & { { } } & { { } } \\ { { \delta ( x - y ) } } & { { \mapsto } } & { { \delta ( x - y ) \delta ( X - Y ) . } } \end{array}
$$

换句话说

$$
\begin{array} { r l } { { } } & { { \{ w ^ { a } ( x , X ) , w ^ { b } ( y , Y ) \} _ { \varepsilon } } } \\ { { } } & { { = \displaystyle \sum _ { X } A _ { k } ^ { a b } ( w ( x , X ) , w _ { x } ( x , X ) + \varepsilon w _ { X } ( x , X ) , . . . ) } } \\ { { } } & { { ~ \times \left[ \delta ^ { ( k ) } ( x - y ) \delta ( X - Y ) + \varepsilon k \delta ^ { ( k - 1 ) } ( x - y ) \delta ^ { \prime } ( X - Y ) \right. } } \\ { { } } & { { \quad + \left. \cdot \cdot + \varepsilon ^ { k } \delta ( x - y ) \delta ^ { ( k ) } ( X - Y ) \right] . } } \end{array}
$$

上式定义了泊松括号, 因为它是由下述泊松括号 [泊松括号(3.13)的“无限直和”]

$$
\{ w ^ { a } ( x , X ) , w ^ { b } ( y , Y ) \} _ { 0 } = \sum A _ { k } ^ { a b } ( w ( x , X ) , w _ { x } ( x , X ) , . . . ) \delta ^ { ( k ) } ( x - y ) \delta ( X - Y )
$$

作线性变量替换 $( x , X ) \mapsto ( x , \varepsilon x + X )$ 所得.

考虑守恒律密度的泊松括号, 我们有

$$
\begin{array} { l } { { \{ P _ { i } ( w ( x , X ) , w _ { x } ( x , X ) + \varepsilon w _ { X } ( x , X ) , \ldots ) , P _ { j } ( w ( y , Y ) , w _ { y } ( y , Y ) + \varepsilon w _ { Y } ( y , Y ) , \ldots ) \} _ { \varepsilon } } } \\ { { = \sum B _ { k } ^ { i j } ( w ( x , X ) , w _ { x } ( x , X ) , \ldots ) \delta ^ { ( k ) } ( x - y ) \delta ( X - Y ) } } \\ { { \quad \quad + \varepsilon \left[ \displaystyle \sum _ { k } \tilde { B } _ { k } ^ { i j } ( w , w _ { x } , w _ { X } , \ldots ) \delta ^ { ( k ) } ( x - y ) \delta ( X - Y ) \right. } } \\ { { \quad \quad \left. + \displaystyle \sum _ { k \geq 1 } k B _ { k } ^ { i j } ( w , w _ { x } , \ldots ) \delta ^ { ( k - 1 ) } ( x - y ) \delta ^ { \prime } ( X - Y ) \right] + O ( \varepsilon ^ { 2 } ) } } \end{array}
$$

其中 $\tilde { B } _ { k } ^ { i j } = \frac { \partial B _ { k } ^ { i j } } { \partial w _ { x } } w _ { X } + 2 \frac { \partial B _ { k } ^ { i j } } { \partial w _ { x x } } w _ { X X } + \cdots , k = 0 , 1 , \ldots .$ 关键在于如下观察:

$$
\tilde { B } _ { 0 } ^ { i j } = \partial _ { X } Q ^ { i j } ( w , w _ { x } , w _ { x x } , \ldots ) .
$$

这可由(3.15)得到. 因此, 对(3.19)关于 $x , y$ 作“平均化”之后我们得到

$$
\{ u ^ { i } ( X ) , u ^ { j } ( Y ) \} _ { \varepsilon } = \varepsilon \left[ \partial _ { X } \overline { { Q ^ { i j } } } \delta ( X - Y ) + \overline { { B } } _ { 1 } ^ { i j } ( w , w _ { x } , . . . ) \delta ^ { \prime } ( X - Y ) \right] + O ( \varepsilon ^ { 2 } ) .
$$

我们可以将等式右边除以 $\varepsilon$ , 这不会影响 $\varepsilon$ 的零阶项的雅可比恒等式. 取极限 $\varepsilon \to 0$ , 则得到的正是(3.13). 因此(3.13)为泊松括号.

然后易证系统(3.11)是关于泊松括号(3.13) 与哈密顿量(3.17)的哈密顿系统.

例子 1. 考虑非线性 Klein-Gordon 方程

$$
q _ { t t } - q _ { x x } + V ^ { \prime } ( q ) = 0 .
$$

这是关于 $q , p = q _ { t }$ 的哈密顿系统, 其泊松括号为

$$
\{ p ( x ) , q ( y ) \} = \delta ( x - y ) ,
$$

哈密顿量为

$$
H = \int \frac { 1 } { 2 } ( p ^ { 2 } + q _ { x } ^ { 2 } + V ( q ) ) \mathrm { d } x .
$$

该系统具有如下两个守恒律:

$$
\begin{array} { r c l } { { I _ { 1 } } } & { { = } } & { { \displaystyle H = \int P _ { 1 } \mathrm { d } x \quad \left( \overbrace { \mathbb { H } \mathbb { E } } ^ { \mathrm { \large \sf \boxplus } \mathbb { E } } \right) } } \\ { { } } & { { } } & { { } } \\ { { I _ { 2 } } } & { { = } } & { { \displaystyle \int p q _ { x } \mathrm { d } x = \int P _ { 2 } \mathrm { d } x \quad \left( \overrightarrow { { \sf z } } { \sf J } _ { \mathbb { E } } ^ { \boxagger } , \ \mathbb { H } \large \underline { { { z } } } \underline { { { \sf \bf \ S } } } { \sf \Sigma } | \mathbb { \bar { H } } \large \underline { { { y } } } + \overbrace { { \sf t } } \underline { { { \bf \ S } } } { \bf \Sigma } { \bf \Sigma } | \large \underline { { { \Sigma } } } { \bf \Sigma } { \bf \Sigma } \right) \underline { { { \varSigma } } } { \bf \Sigma } { \bf \Sigma } \mathbb { H } \bar { \Sigma } \mathbb { \Sigma } \large ) . } } \end{array}
$$

(3.20)的单相周期解 [见 2.2 节例 1] 形如

$$
\begin{array} { r l } & { q ( \boldsymbol { x } , t ) = Q ( \boldsymbol { k } \boldsymbol { x } + \omega t + \tau ^ { 0 } ) , \quad Q ( \tau + 2 \pi ) = Q ( \tau ) , } \\ & { ( \omega ^ { 2 } - \boldsymbol { k } ^ { 2 } ) ^ { 1 / 2 } \mathrm { d } Q = [ 2 ( E - V ( Q ) ) ] ^ { 1 / 2 } \mathrm { d } \tau . } \end{array}
$$

非线性色散关系形如

$$
( \omega ^ { 2 } - k ^ { 2 } ) ^ { 1 / 2 } \oint \frac { \mathrm { d } Q } { \sqrt { 2 ( E - V ( Q ) ) } } = 2 \pi .
$$

其中

$$
\begin{array} { r c l } { { \{ P _ { 1 } ( x ) , P _ { 1 } ( y ) \} } } & { { = } } & { { \{ P _ { 2 } ( x ) , P _ { 2 } ( y ) \} = ( q ^ { \prime } p ) ^ { \prime } \delta ( x - y ) + 2 q ^ { \prime } p \delta ^ { \prime } ( x - y ) , } } \\ { { \{ P _ { 1 } ( x ) , P _ { 2 } ( y ) \} } } & { { = } } & { { ( p ^ { 2 } + q ^ { \prime 2 } ) \delta ^ { \prime } ( x - y ) + [ ( p ^ { 2 } + q ^ { \prime 2 } ) / 2 + V ( q ) ] ^ { \prime } \delta ( x - y ) , } } \\ { { \{ P _ { 2 } ( x ) , P _ { 1 } ( y ) \} } } & { { = } } & { { ( p ^ { 2 } + q ^ { \prime 2 } ) \delta ^ { \prime } ( x - y ) + [ ( p ^ { 2 } + q ^ { \prime 2 } ) / 2 - V ( q ) ] ^ { \prime } \delta ( x - y ) . } } \end{array}
$$

[这里的 $p = p ( x )$ , $q = q ( x ) ]$ . 因此平均化泊松括号具有 Liouville 形式

$$
g ^ { i j } = \gamma ^ { i j } + \gamma ^ { j i } , b _ { k } ^ { i j } = \frac { \partial \gamma ^ { i j } } { \partial u ^ { k } } ,
$$

$$
( \gamma ^ { i j } ) = { \binom { u ^ { 2 } } { u ^ { 1 } - 2 \Delta } } \ u ^ { 1 } ) , \quad \Delta = \Delta ( u ^ { 1 } , u ^ { 2 } ) = { \overline { { V ( Q ) } } } .
$$

平均化方程具有相对论流体力学方程的形式

$$
\frac { \partial T ^ { i j } } { \partial X ^ { j } } = 0 .
$$

其能-动量张量 $T ^ { i j }$ 可通过对 Klein-Gordon 场 $q$ 的能-动量张量 $t ^ { i j }$ 作平均化得到:

$$
T ^ { i j } = \overline { { { t ^ { i j } } } } , \quad ( t ^ { i j } ) = \left( \begin{array} { l l } { { P _ { 1 } } } & { { - P _ { 2 } } } \\ { { - P _ { 2 } } } & { { P _ { 1 } - 2 V } } \end{array} \right) = \left( \begin{array} { l l } { { E + k ^ { 2 } F F _ { E } } } & { { - \omega F F _ { E } } } \\ { { - \omega k F F _ { E } } } & { { F F _ { E } ^ { - 1 } - E + k ^ { 2 } F F _ { E } } } \end{array} \right) ,
$$

其中 $F ( E ) = \frac { 1 } { 2 \pi } \oint [ 2 ( E - V ( Q ) ) ] ^ { 1 / 2 } \mathrm { d } Q .$

此张量可通过洛伦兹变换对角化: 当 $\omega ^ { 2 } - k ^ { 2 } > 0$ 时取 $( \omega , \boldsymbol { k } ) \to ( \omega ^ { \prime } , 0 )$ , $\omega ^ { 2 } - k ^ { 2 } = { \omega } ^ { \prime } { } ^ { 2 }$ ;当 $\omega ^ { 2 } - \boldsymbol { k } ^ { 2 } < 0$ 时取 $( \omega , \boldsymbol { k } ) \to ( 0 , \boldsymbol { k } ^ { \prime } )$ , $\omega ^ { 2 } - k ^ { 2 } = - k ^ { \prime } ^ { 2 }$ . 态方程 [当 $\omega ^ { 2 } - \boldsymbol { k } ^ { 2 } > 0$ 时] 可表示为下述参数形式

$$
\begin{array} { r } { \mathcal { E } = E , \quad \mathcal { P } = F ( E ) F _ { E } ^ { - 1 } ( E ) - E . } \end{array}
$$

[利用 Hayes[28] 的早期结果] 可以证明, 将平坦度量(3.22)化为常数的平坦坐标为 $k , J$ ,这里的 $J$ 时三维不变流形(3.21),(3.21a) 上的哈密顿系统(3.20)的角参数:

$$
J = { \frac { 1 } { 2 \pi } } \oint p \mathrm { d } q .
$$

在此坐标下, 泊松括号(3.22)形如

$$
\{ k ( X ) , J ( Y ) \} _ { \# \# \sharp } = \delta ^ { \prime } ( X - Y ) ,
$$

并且其余泊松括号都为零. 该度量的正负惯性指数为 $( 1 , 1 )$ .

例子 2. “摄动 KdV 方程”[见 2.2 节例子 2]

$$
w _ { t } = - \partial _ { x } \frac { \delta H } { \delta w ( x ) } = - \partial _ { x } V ^ { \prime } ( w ) + w _ { x x x } , \quad H = \int \left[ \frac { w _ { x } ^ { 2 } } { 2 } + V ( w ) \right] \mathrm { d } x
$$

关于 Gardner-Zakharov-Feddeev 泊松括号

$$
\{ w ( x ) , w ( y ) \} = \delta ^ { \prime } ( x - y )
$$

构成哈密顿系统. 此系统有如下三个两两交换的守恒律

$$
\begin{array} { r c l } { { I _ { 0 } } } & { { = } } & { { \displaystyle \int w \mathrm { d } x \quad \big ( \dot { \forall } \dot { \mathbb { H } } _ { \Sigma } ^ { \sharp } \dddot { \mathbb { H } } _ { \Sigma } ^ { \sharp } \bigstar \underline { { { \Theta } } } _ { \sharp } ^ { \sharp } \big ) \sharp \ddot { \mathbb { H } } \mp \big < \big < \mathcal { k } \mp \big > } } \\ { { I _ { 1 } } } & { { = } } & { { \displaystyle \int \frac { w ^ { 2 } } { 2 } \mathrm { d } x \quad \big ( \vec { z } \big ) _ { \underline { { { \Xi } } } \underline { { { \Psi } } } } ^ { \underline { { { \Xi } } } } \big ) } } \\ { { I _ { 2 } } } & { { = } } & { { \displaystyle H \quad \big ( \dot { \mathbb { H } } _ { \Sigma } ^ { \underline { { { \Xi } } } \underline { { { \Xi } } } } \big ) . } } \end{array}
$$

方程(3.23)的单相解构成三维族, 形如

$$
\begin{array} { r c l } { { w ( x , t ) } } & { { = } } & { { \Phi ( k x + \omega t ) , \quad \Phi ( \tau + 2 \pi ) = \Phi ( \tau ) , } } \\ { { } } & { { } } & { { k \mathrm { d } \Phi } } \\ { { k \mathrm { d } \Phi } } & { { = } } & { { \sqrt { 2 V ( \Phi ) + \displaystyle \frac { \omega } { k } \Phi ^ { 2 } + a \Phi + b } \mathrm { d } \tau . } } \end{array}
$$

其中参数 $k , \omega , a , b$ 满足约束关系 [色散关系]

$$
k \oint \frac { \mathrm { d } \Phi } { \sqrt { 2 V ( \Phi ) + c \Phi ^ { 2 } + a \Phi + b } } = 2 \pi ,
$$

[这里的 $c = \omega / k ]$ . 在坐标 $u ^ { 0 } = I _ { 0 } , u ^ { 1 } = I _ { 1 } , u ^ { 2 } = I _ { 2 }$ 下, 平均化泊松括号为下述Liouville 形式:

$$
( \gamma ^ { i j } ) = \left( \begin{array} { c c c } { { \displaystyle \frac { 1 } { 2 } } } & { { u ^ { 0 } } } & { { - c u ^ { 0 } - a } } \\ { { 0 } } & { { u ^ { 1 } } } & { { - c u ^ { 1 } - b } } \\ { { 0 } } & { { u ^ { 2 } } } & { { - c u ^ { 2 } - b c + \displaystyle \frac { a ^ { 2 } } { 2 } \right) , } } \end{array}
$$

$a = a ( u ) , b = b ( u ) , c = c ( u ) .$ .

我们应当注意到变量

$$
p _ { + } = \frac { \overline { { { w ^ { 2 } } } } } { 2 } = u ^ { 1 } , \quad p _ { - } = \frac { \overline { { { ( w - \overline { { { w } } } ) ^ { 2 } } } } } { 2 } = u ^ { 1 } - \frac { 1 } { 2 } ( u ^ { 0 } ) ^ { 2 }
$$

是交换的:

$$
\{ p _ { + } ( X ) , p _ { - } ( Y ) \} _ { \mp \pm 5 } \equiv 0 ,
$$

并且这两这当中的每一个都定义了直线上的向量场的一个子代数:

$$
\{ p _ { \pm } ( X ) , p _ { \pm } ( Y ) \} _ { \mp \sharp : \sharp } = [ p _ { \pm } ( X ) + p _ { \pm } ( Y ) ] \delta ^ { \prime } ( X - Y ) .
$$

换句话说, 在平均化 KdV 方程中, 每一个变量都可以看作流体两个分量中的一个的动量.

此时, 平坦坐标为 $k$ (波数), $J$ (角参数) 与 $u ^ { 0 } = \overline { { w } } ($ (零化子). 此坐标下的常值度量矩阵为

$$
( \tilde { g } ^ { i j } ) = \left( \begin{array} { l l l } { { 0 } } & { { 1 } } & { { 0 } } \\ { { 1 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 1 } } \end{array} \right) .
$$

例子 3. 当 $V = w ^ { 3 }$ 时 [此时就是通常的 KdV 方程] , 此方程还具有 Magri 泊松括号

$$
\{ w ( x ) , w ( y ) \} _ { M } = - \frac { 1 } { 2 } \delta ^ { \prime \prime \prime } ( x - y ) + ( w ( x ) + w ( y ) ) \delta ^ { \prime } ( x - y ) .
$$

相应的哈密顿量为

$$
H _ { M } = \int w ^ { 2 } \mathrm { d } x .
$$

这也给出 KdV 方程关于单相解的平均化方程的新的流体力学型泊松括号. 在上例的Liouville 坐标 $u ^ { 0 } , u ^ { 1 } , u ^ { 2 }$ 下 [这里 $u ^ { 0 }$ 为动量, $2 u ^ { 1 } = H _ { M } ]$ , 我们得到平均化泊松括号的下述公式

$$
\gamma _ { M } ^ { i j } ( u ) = \left( \begin{array} { c c c } { { 2 u ^ { 0 } } } & { { - c u ^ { 0 } - \frac { a } { 2 } } } & { { 1 0 u ^ { 2 } } } \\ { { } } & { { - c u ^ { 1 } + 2 b } } & { { \frac { 5 } { 3 } \left( - c u ^ { 2 } - b c + \frac { a ^ { 2 } } { 4 } \right) } } \\ { { } } & { { } } & { { } } \\ { { 2 u ^ { 2 } } } & { { - c u ^ { 2 } - b c + \frac { a ^ { 2 } } { 4 } } } & { { - ( c ^ { 2 } - a ) u ^ { 2 } + 2 b c ^ { 2 } - c \frac { a ^ { 2 } } { 4 } + a b } } \end{array} \right) .
$$

我们也可以对 Magri 泊松括号作关于 $n \cdot$ -相解的平均化.

对于广义非线性薛定谔方程 (简称 NLS 方程) [见 2.2 节例子 3] , 利用 [37] 中的“平均化拉格朗日理论”(averaged Lagrangean formalism) 可得其平均化系统 [16]. 而我们现在的方法不能用于此例: 不变环面的四维族, 但此 NLS 方程不可积, 只有三个守恒律. 由于平均化系统是拉格朗日系统, 它可以转化为哈密顿形式, 而不去研究 NLS 方程原来的哈密顿形式.

KdV 方程关于多相解 $[ n$ -相解] 的平均化可以写成下述优美的形式 (Flaschka, For-est, McLaughlin[24]).

定理 3.2.

$$
\begin{array} { r } { \partial _ { T } \mathrm { d } p = \partial _ { X } \mathrm { d } q . } \end{array}
$$

其中 $\mathrm { d } p$ , dq 为拟动量, 拟能量的微分:

$$
\mathrm { d } p = { \frac { \mathrm { d } p } { \mathrm { d } \lambda } } \mathrm { d } \lambda , \quad \mathrm { d } q = { \frac { \mathrm { d } q } { \mathrm { d } \lambda } } \mathrm { d } \lambda ,
$$

$$
p = \frac { 1 } { i } \overline { { ( \log \psi ) _ { x } } } , \quad q = \frac { 1 } { i } \overline { { ( \log \psi ) _ { t } } }
$$

[见上一节] , 它们是下述黎曼曲面

$$
\mu ^ { 2 } = \prod _ { i = 1 } ^ { 2 n + 1 } ( \lambda - r _ { i } ) \equiv R _ { 2 n + 1 } ( \lambda )
$$

上的阿贝尔微分, 其极点位于无穷远点 $\lambda = \infty$ ,

$$
\begin{array} { r c l } { { \mathrm { d } p } } & { { = } } & { { \displaystyle \frac { P ( \lambda ) \mathrm { d } \lambda } { 2 \sqrt { R _ { 2 n + 1 } ( \lambda ) } } = \frac { \mathrm { d } \lambda } { 2 \sqrt { \lambda } } + O ( 1 ) = \mathrm { d } k + O ( 1 ) , \quad k = \sqrt \lambda } } \\ { { } } & { { } } & { { P = P ( \lambda | r _ { 1 } , . . . , r _ { 2 n + 1 } ) } } \\ { { \mathrm { d } q } } & { { = } } & { { \displaystyle - \frac { 6 \lambda ^ { n + 1 } + Q ( \lambda ) } { \sqrt { R _ { 2 n + 1 } ( \lambda ) } } \mathrm { d } \lambda = - 6 \sqrt \lambda \mathrm { d } \lambda + O ( 1 ) = 4 \mathrm { d } ( k ^ { 3 } ) + O ( 1 ) , } } \\ { { } } & { { } } & { { Q = Q ( \lambda | r _ { 1 } , . . . , r _ { 2 n + 1 } ) , } } \end{array}
$$

且有零 $a \mathrm { . }$ -周期.

(3.24)的证明: 类似于(3.11)那样对守恒律

$$
[ ( \log \psi ) _ { x } ] _ { t } = [ ( \log \psi ) _ { t } ] _ { x }
$$

作平均化, 可得

$$
\partial _ { T } \overline { { ( \log \psi ) _ { x } } } = \partial _ { X } \overline { { ( \log \psi ) _ { t } } } ,
$$

即

$$
\partial _ { T } p ( \lambda ) = \partial _ { X } q ( \lambda ) .
$$

对 $\lambda$ 求导可得(3.24).

推论. 分支点 $r _ { 1 } , . . . , r _ { 2 n + 1 }$ 是平均化 $K d V$ 系统的黎曼不变量. 也就是说该平均化系统在此坐标下是对角的:

$$
\partial _ { T } r _ { i } = v _ { i } ( r _ { 1 } , . . . , r _ { 2 n + 1 } ) \partial _ { X } r _ { i } , \quad i = 1 , . . . , 2 n + 1 .
$$

证明. 将(3.24)两边乘以 $( \lambda - r _ { i } ) ^ { 3 / 2 }$ , 再取极限 $\lambda \to r _ { i }$ 即可得到(3.26), 其中

$$
v _ { i } = \left. { \frac { \operatorname { d } q ( \lambda ) } { \operatorname { d } p ( \lambda ) } } \right| _ { \lambda = r _ { i } } = - 2 { \frac { 6 r _ { i } ^ { n + 1 } + Q ( \lambda = r _ { i } ) } { P ( \lambda = r _ { i } ) } } .
$$

推论. 平均化 $K d V$ 方程是可积的流体力学型系统.

注记. 回顾 [见 2.1 节] 平均化系统(3.26)的哈密顿理论(3.13) 当中的度量 $g _ { i j }$ 在坐标$r _ { 1 } , . . . , r _ { 2 n + 1 }$ 下是对角的. 此度量的可表示为 [38]:

$$
g _ { i i } = \mathrm { R e s } _ { \lambda = r _ { i } } \left[ \frac { \mathrm { d } p } { \mathrm { d } \lambda } \right] ^ { 2 } \mathrm { d } \lambda , \quad i = 1 , . . . , 2 n + 1 .
$$

由此公式容易看出该度量的符号为 $( + , - , + , . . . , - , + )$ . 我们还可以证明 [38] 该平坦对角度量是 Egoroff 度量 [见 2.1 节附录 2] , 相应的势函数为 $u ^ { 0 } = \int w \mathrm { d } x = \dot { u } ^ { 0 } ( { \boldsymbol { r } } _ { 1 } , . . . , { \boldsymbol { r } } _ { 2 n + 1 } )$ ,$g _ { i i } = \partial _ { i } u _ { 0 }$ . $n = 1$ 时, 由(3.28)可直接得到方程(2.36)的解(2.40).

求解方程(3.24)的代数几何方法由 Krichever 所发现. 现在我们给出此方法的概要.

设 $\Gamma = \Gamma ( X , T )$ 是(3.25)中的关于 $X , T$ 的黎曼曲面. 设 $\mathrm { d } s = \mathrm { d } s ( \lambda )$ 为任意取定的$\Gamma$ 上的分片全纯微分, 使得它与 $X , T$ 的奇性无关 [例如在某些固定的点处为极点, 或者在某些曲线上跳跃] 并且具有零 $a \cdot$ -周期.

定理 3.3. (Krichever[11]). 若关于 $X , T$ 的黎曼曲面 $\Gamma$ 满足

$$
[ X \mathrm { d } p ( \lambda ) + T \mathrm { d } q ( \lambda ) - \mathrm { d } s ( \lambda ) ] _ { \lambda = r _ { i } } \equiv 0 , \quad i = 1 , . . . , 2 n + 1 ,
$$

则其分支点 $r _ { 1 } , . . . , r _ { 2 n + 1 }$ 满足平均化 $K d V$ 方程(3.26).

证明. 考虑微分形式

$$
\Omega = X \mathrm { d } p + T \mathrm { d } q - \mathrm { d } s
$$

及其关于时间, 空间的导数

$$
\begin{array} { r c l } { \Omega _ { T } } & { = } & { \mathrm { d } q + ( X \partial _ { T } \mathrm { d } p + T \partial _ { T } \mathrm { d } q - \partial _ { T } \mathrm { d } s ) } \\ { \Omega _ { X } } & { = } & { \mathrm { d } p + ( X \partial _ { X } \mathrm { d } p + T \partial _ { x } \mathrm { d } q - \partial _ { X } \mathrm { d } s ) . } \end{array}
$$

注意微分形式 $\mathrm { d } p$ , dq, ds 的导数的奇性相互抵消, 这是因为它们关于 $X , T$ 为常数.由(3.29)可知在分支点 $r \ = \ \lambda _ { i }$ 处的奇性也被抵消. 因此上述公式的括号内的部分为Γ 上的全纯微分. 它们的 $a \cdot$ -周期恒为零, 因此它们也恒为零 [这是关于黎曼曲面上的全纯微分的著名结果] . 因此我们得到

$$
\Omega _ { T } = \mathrm { d } q , \quad \Omega _ { x } = \mathrm { d } p .
$$

此方程组的相容性条件恰为平均化方程

$$
\begin{array} { r } { \partial _ { T } \mathrm { d } p = \partial _ { X } \mathrm { d } q . } \end{array}
$$

利用此构造可以得到色散版本的冲击波的 Gurevich-Pitayevskii 问题的恰当的解析公式 [17]. 为此我们需要取 $\mathrm { d } s ( \lambda )$ 为以无穷远点为极点的亚纯微分, 且在 $\lambda = \infty$ 附近形

如

$$
\mathrm { d } s ( \lambda ) = \stackrel { \ J \psi } { \nabla \cdot } \frac { \ast \chi } { \mathcal { k } \mathcal { U } } \times \mathrm { d } \lambda ^ { \frac { 7 } { 2 } } + O ( 1 )
$$

下一节我们详细考虑此例.

# 3.2 应用: KdV 理论中某步骤的分解; 色散版本的冲击波. Gurevich-Pitaevskii 问题的解析解

在本节, 我们把 KdV 方程写作

$$
u _ { t } + u u _ { x } + u _ { x x x } = 0 .
$$

这种在物理文献上更标准的写法可由之前版本通过变量替换 $u  - \frac { 1 } { 6 } u$ u, t → −t 得到.

我们来考虑两个色散流体力学的问题, 分别是 Gurevich 和 Pitaevskii [见 [4],[5], 也可见书 [39] 的第 4 章 $\ S 4 ]$ .

问题 1. KdV 方程的带状初值条件的分解. 如果 KdV 方程的解的初值条件形如下图,则解在 $t \gg 1$ 时的渐近行为如何?

![](images/3d5bfd144dad259e1375f27841966661e2aa0c4ee9abf7e85e68c2970aaa47ce.jpg)  
图 3.1

问题 2. 色散版本的冲击波. 求 KdV 方程在初值 $u ( x )$ 满足

$$
x = u t - u ^ { 3 } , \quad | x | \to \infty
$$

的情况下, 解在 $t \gg 1$ 时的渐近行为. 问题 2 的物理背景如下. 我们假设色散项 $u _ { x x x }$ 初始时充分小, 不影响系统演化, 于是该系统可由截断方程

$$
u _ { t } + u u _ { x } = 0
$$

近似描述. 此方程的通解形如 $x = u t + f ( u )$ [可见 2.1 节] , 其中 $f ( u )$ 为在某时刻$t \ : = \ : 0$ “倒塌”(topple over) 的任意函数. 即当 $t  0 ^ { - }$ 时, 在某一点 $x \ = \ x _ { 0 }$ 成立$u _ { x }  \infty$ . 一般情况下, 在“倒塌点” $( t = 0 , x = x _ { 0 } = 0 )$ 附近的解可由方程 (3.31)来近似 $( t < 0 )$ . 在此邻域内, KdV 方程的色散项 $u _ { x x x }$ 不可被无视. 考虑到这一项, 方程的解在点 $( 0 , 0 )$ 的一个小邻域内会发生剧烈变化: KdV 理论里不存在“倒塌”, 会出现震荡区 (oscillatory zone). Gurevich 和 Pitaevskii 在小邻域 $\Delta ( t )$ 中用单相 Whitham 方程[见上一节的(3.26), $n = 1 ]$ 来近似描述它; 在此小邻域之外, 震荡区变成方程(3.31)的一个小的解; 色散项在震荡区之外可以无视. 从而, 问题 2 描述了 $x , t$ 的局部情况. 与 $x , t$ 中整体渐近性良好的尺度 [比如问题 1] 相比, 在这个小区域中 Gurevich-Pitaevskii 区域建立在 $x , t$ 的尺度必须较小. 因此问题 2 描述了一种普遍的局部情况, 称为色散版本的冲击波. 在局部上, 这种近似的应用并不是完全规则的, 因为感兴趣的区域只包含有限数量的振荡, 并且这种近似结构将只在有限时间内可见 (中间时间渐近性). 问题 2 出现的“大的” $t$ 要远小于问题 1 中出现的时间.

我们首先给出 $n = 1$ 时 Whitham 方程的显式表达. 由上一节(3.26),(3.27) 以及更早的(2.164),(2.165), 我们有

$$
r _ { i _ { t } } + v _ { i } ( r ) r _ { i _ { x } } = 0 , \quad i = 1 , 2 , 3 ,
$$

$$
r _ { 1 } \le r _ { 2 } \le r _ { 3 }
$$

$$
v _ { i } ( r ) = \frac { 1 2 r _ { i } ^ { 2 } - 6 \sigma _ { 1 } r _ { i } - \frac { 2 } { 3 } \sigma _ { 1 } ^ { 2 } + 4 \sigma _ { 2 } - 2 \sigma _ { 1 } \frac { \eta } { \omega } } { 6 ( \frac { \eta } { \omega } - r _ { i } ) } , i = 1 , 2 , 3 ,
$$

$\frac { \eta } { \omega } = \frac { \eta } { \omega } ( g _ { 2 } , g _ { 3 } )$ [见 2.4 节最末] ,

$$
g _ { 2 } = \frac { 4 \sigma _ { 1 } ^ { 2 } } { 3 } - 4 \sigma _ { 2 } , \quad g _ { 3 } = - 4 \sigma _ { 3 } - \frac { 8 } { 2 7 } \sigma _ { 1 } ^ { 3 } + \frac { 4 } { 3 } \sigma _ { 1 } \sigma _ { 2 } ,
$$

$$
\sigma _ { 1 } = r _ { 1 } + r _ { 2 } + r _ { 3 } , \quad \sigma _ { 2 } = r _ { 1 } r _ { 2 } + r _ { 1 } r _ { 3 } + r _ { 2 } r _ { 3 } , \quad \sigma _ { 3 } = r _ { 1 } r _ { 2 } r _ { 3 } .
$$

可以证明 $v _ { 1 } < v _ { 2 } < v _ { 3 }$ . 我们也指出, 在一个震荡周期内的平均值 $\overline { { u } }$ 为

$$
\overline { { { u } } } = c + 1 2 \frac { \eta } { \omega } , c = - 2 ( r _ { 1 } + r _ { 2 } + r _ { 3 } ) .
$$

速度 $v _ { i } ( r )$ 为齐次函数,

$$
v _ { i } ( k r ) = k v _ { i } ( r ) .
$$

因此对任意指数 $\gamma$ , 系统(3.33)存在形如

$$
r _ { i } ( x , t ) = t ^ { \gamma } R _ { i } ( x t ^ { - 1 - \gamma } )
$$

的自相似解. [4,5] 的想法是用这些解来描述问题 1,2 中 $t \gg 1$ 时振荡区内的渐近状态,因为它们在震荡区外是 [局部] 自相似的.

问题 1. 在此我们必须取 $\gamma ~ = ~ 0$ . 若初始条件形如图 3.1, 并且 $\operatorname* { l i m } _ { x \to - \infty } u ( x ) \ = \ 1 \qquad $ ,$\operatorname* { l i m } _ { x \to \infty } u ( x ) = 0$ , 则方程 (3.33)有如下解

$$
r _ { 1 } \equiv 0 , \quad r _ { 3 } \equiv 1 , \quad v _ { 2 } ( 0 , r _ { 2 } , 1 ) = \frac { x } { t } .
$$

震荡区间 $\Delta = [ \tau ^ { - } , \tau ^ { + } ]$ 如下图:

![](images/b10fce0a31a39a2c30629f138a982b5f738267f911d354378d243aab76c567ee.jpg)  
图 3.2

平均值函数 $\overline { { u } }$ 的图像类似于通常的冲击波 [见下图] .

![](images/5ffd28ebbf4dd729e42f30f9cddb36d6696a2606dff1e5def04511c6d957b5be.jpg)  
图 3.3

这种渐近行为的严格证明问题被 [40] 用反散射变换研究.

问题 2. 此时情况更加复杂. 为正确匹配边值条件(3.31), 我们要考虑(3.33)的关于指标$\gamma = \frac 1 2$ 的自相似解

$$
r _ { i } ( x , t ) = t ^ { 1 / 2 } R _ { i } ( x t ^ { - 3 / 2 } ) .
$$

在区间 $\Delta = [ x ^ { - } , x ^ { + } ]$ 的边界, 函数 $\boldsymbol { r } ( \boldsymbol { x } , t )$ 连续 [甚至光滑] :

$$
r ( x , t ) = \{ r _ { 1 } ( x , t ) , r _ { 2 } ( x , t ) , r _ { 3 } ( x , t ) \}
$$

[3-值函数] ,

$$
\begin{array} { c c } { { r ^ { - } \equiv r _ { 3 } ( x ^ { - } ) = u ( x ^ { - } ) , } } & { { r _ { 2 } ^ { - } = r _ { 1 } ^ { - } , } } \\ { { \nonumber r ^ { + } \equiv r _ { 3 } ( x ^ { + } ) = u ( x ^ { + } ) , } } & { { r _ { 2 } ^ { + } = r _ { 3 } ^ { + } . } } \end{array}
$$

问题 1,2 的震荡区域都覆盖“零-相”(zero-phase)Whitham 方程的两个特解之间的整个区域: 在左端点 $x ^ { - }$ 必有 $r _ { 2 } = r _ { 1 }$ [即, KdV 方程的单相解变成常值] , 而在右端点 $x ^ { + }$ 必有 $r _ { 2 } = r _ { 3 }$ , 即, KdV 方程的单相解变成孤子 [相差常数意义下] . 震荡区间 $\Delta = [ \tau ^ { - } , \tau ^ { + } ]$ 关于不变量 $\tau$ 为常量 [问题 1 当中 $\tau = x / t$ , 问题 2 当中 $\tau = x t ^ { - 3 / 2 } ]$ . 全体多值图像必定是 $C ^ { 1 }$ -光滑的, 且包含震荡区域的边界. 在 [4,5] 可找到这样的解的近似. 现在我们由[17] 给出这种解的解析表达式.

现在考虑椭圆谱曲线 [见 2.4 节] 上的阿贝尔微分 ds 如下:

$$
\mathrm { d } s = \alpha \frac { \lambda ^ { 4 } + \alpha _ { 1 } \lambda ^ { 3 } + a _ { 2 } \lambda ^ { 2 } + a _ { 3 } \lambda + a _ { 4 } } { \sqrt { R _ { 3 } ( \lambda ) } } \mathrm { d } \lambda ,
$$

$$
R _ { 3 } ( \lambda ) = \prod _ { i = 1 } ^ { 3 } ( \lambda - r _ { i } ) .
$$

系数 $a _ { 1 } , a _ { 2 } , a _ { 3 }$ 由如下渐近关系

$$
\mathrm { d } s = \alpha ( \lambda ^ { 5 / 2 } + O ( \lambda ^ { - 3 / 2 } ) ) \mathrm { d } \lambda , \quad \lambda \to \infty
$$

所确定, 系数 $a _ { 4 }$ 使得成立如下归一化条件:

$$
\int _ { r _ { 2 } } ^ { r _ { 3 } } \mathrm { d } s = 0 .
$$

稍后再去确定系数 $\alpha$ . 于是我们有

$$
a _ { 1 } = - \frac { \sigma _ { 1 } } { 2 } , \quad a _ { 2 } = \frac { \sigma _ { 2 } } { 2 } - \frac { \sigma _ { 1 } ^ { 2 } } { 8 } , \quad a _ { 3 } = - \frac { \sigma _ { 3 } } { 2 } + \frac { \sigma _ { 1 } \sigma _ { 2 } } { 4 } - \frac { \sigma _ { 1 } ^ { 3 } } { 8 } ,
$$

其中 $\sigma _ { 1 } , \sigma _ { 2 } , \sigma _ { 3 }$ 为初等对称多项式(3.35a).

我们考虑 Whitham 方程(3.33)的关于 ds 的形如形如上一节(3.29)的解 $r _ { i } ( x , t )$ :

$$
[ x \mathrm { d } p + t \mathrm { d } q - \alpha \mathrm { d } s ] _ { \lambda = r _ { i } } = 0 , \quad i = 1 , 2 , 3 .
$$

它可以重写为

$$
x + v _ { i } ( r ) t - \alpha w _ { i } ( r ) = 0 , \quad i = 1 , 2 , 3 ,
$$

其中函数 $w _ { i } ( r )$ 满足如下公式 [17]:

$$
w _ { i } ( r ) = \left[ \frac { \mathrm { d } s } { \mathrm { d } p } \right] _ { \lambda = r _ { i } } = ( 3 v _ { i } - \sigma _ { 1 } ) f _ { i } ( r ) + f ( r ) , \quad i = 1 , 2 , 3 ,
$$

$$
f ( r ) = 5 \sigma _ { 1 } ^ { 3 } - 1 2 \sigma _ { 1 } \sigma _ { 2 } + \sigma _ { 3 } , \quad f _ { i } ( r ) = \frac { \partial f } { \partial r _ { i } } .
$$

易知对任意 $\alpha$ , 方程(3.45)的解都是关于指数 $\gamma = \frac 1 2$ 的自相似解.

定理. [17]. 方程组(3.45)在区域 $\tau ^ { - } < \tau < \tau ^ { + }$ 非退化, 其中 $\tau = x t ^ { - 3 / 2 }$ , 并且定义了 Whitham 方程(3.33)的一个光滑 [甚至解析] 解. 若 $\alpha = \frac { 1 } { 3 }$ , 则它关于$\tau ^ { - } = - \sqrt { 2 } , \tau ^ { + } = \sqrt { 1 0 } / 2 7$ 满足边值条件(3.40).

数值模拟 [1] [也可见 [13]] 表明, 在奇异边附近具有上述特殊渐近性质的多值函数的演化是局部良好定义的. 若初始条件 $C ^ { 1 }$ -接近于上述解, 则此演化在无限时间内都有定义, 且相应的解渐近收敛于 Gurevich-Pitaevskii 解. 文献 [2] [也可见 [13]] 研究了非零粘性 (non-zero viscosity) 的情形.

# 3.3 有限空缺势的平均化方法与半经典量子化. Painlevé-I 方程的渐近积分

正如第2.3,2.4节所述, 关于常微分算子的交换性方程

$$
[ L , A ] = 0
$$

在某种意义下是有限空缺积分理论的中心方程. 我们先回到最简单的例子

$$
L = - \partial _ { x } ^ { 2 } + u , \quad A = 4 \partial _ { x } ^ { 3 } - 6 u \partial _ { x } - u _ { x } .
$$

此时方程(3.47)形如

$$
6 u u _ { x } - u _ { x x x } = 0 .
$$

等价地, 方程(3.49)可表示为 Lax 形式

$$
V _ { x } ( \lambda ) = [ U ( \lambda ) , V ( \lambda ) ] ,
$$

其中

$$
U ( \lambda ) = \binom { 0 } { u - \lambda } \ 1 \atop \int \ d u , \lambda \atop 0 \ d u , \lambda \atop \frac { d } { d u - \lambda } \ 1 \atop 0 \ d u , \lambda \atop \frac { d } { d u - \lambda } \ 1 \atop 0 \ d u .
$$

$$
V ( \lambda ) = \left( \begin{array} { c c } { { - \displaystyle \frac { u ^ { \prime } } { 2 } } } & { { 2 \lambda + u } } \\ { { - \displaystyle \frac { u ^ { \prime \prime } } { 2 } + ( u - \lambda ) ( 2 \lambda + u ) } } & { { \displaystyle \frac { u ^ { \prime } } { 2 } \quad } } \end{array} \right) .
$$

由(3.49)可知 [关于 $\lambda$ 的] 多项式

$$
\operatorname* { d e t } V ( \lambda ) = 4 \lambda ^ { 3 } - ( 3 u ^ { 2 } - u ^ { \prime \prime } ) \lambda - \frac { 1 } { 4 } ( { u ^ { \prime } } ^ { 2 } + 4 u ^ { 3 } - 2 u u ^ { \prime \prime } )
$$

系数为常数; 它们定义了谱曲线 $\Gamma$

$$
\begin{array} { l } { { \mu ^ { 2 } = \operatorname * { d e t } V ( \lambda ) \equiv 4 \lambda ^ { 3 } - g _ { 2 } \lambda - g _ { 3 } } } \\ { { g _ { 2 } = 3 u ^ { 2 } - u ^ { \prime \prime } , \quad g _ { 3 } = \displaystyle \frac { 1 } { 4 } ( u ^ { \prime 2 } + 4 u ^ { 3 } - 2 u u ^ { \prime \prime } ) . } } \end{array}
$$

方程(3.49)的解形如

$$
u ( x ) = 2 \wp ( x - x _ { 0 } | g _ { 2 } , g _ { 3 } )
$$

[在黎曼曲面(3.54)中的多项式 $\operatorname* { d e t } V ( \lambda )$ 有实根的情况下, 为得到实的光滑解, 作虚部平移 $x _ { 0 } \mapsto x _ { 0 } + \omega ^ { \prime }$ 是必要的, 见第2.4节] . 对于 KdV 方程簇的更一般的算子 $A$ , 或者等价地, 关于 $\lambda$ 的多项式矩阵 $V ( \lambda )$ [见2.3节] , 交换性方程(3.47) [或者(3.50)] 仍然可积, 谱曲线 $\mu ^ { 2 } = \operatorname* { d e t } V ( \lambda )$ 与 $x$ 无关; 只是公式(3.56)变得更加复杂 [见2.4节] . 我们在此指出,交换算子 $L , A$ 满足代数方程

$$
R ( L , A ) = 0 ,
$$

其中

$$
R ( \lambda , \mu ) \equiv \mu ^ { 2 } - \operatorname * { d e t } V ( \lambda ) = 0
$$

为谱曲线方程 [证明可见 [41]] . 换句话说, $L , A$ 为谱曲线上的坐标.

现在我们开始 量子化 (quantization) . 即, 把交换性条件 $[ L , A ] = 0$ 改为关于同样的算子 $L , A$ 的“量子化”条件

$$
[ L , A ] = \varepsilon \cdot 1
$$

[1 为恒等算子, $\varepsilon$ 为参数] . 在我们的例子中, 我们得到 $6 u u ^ { \prime } - u ^ { \prime \prime \prime } = \varepsilon$ , 或者

$$
3 u ^ { 2 } - u ^ { \prime \prime } = \varepsilon x
$$

[Painlevé-I 方程] . 从而, $L , A$ 为“量子化谱曲线” $\hat { \Gamma }$ 上的非交换坐标. 我们将证明 [43]在半经典逼近下, $\hat { \Gamma }$ 可被描述为经典谱曲线 $\Gamma$ 的某个特殊的可积形变.

在量子化之前, 我要说几句量子化问题的背后动机. 考虑 $n \times n$ 厄密随机矩阵模型

(Hermitean random matrix model) 的 配分函数 (partition function)

$$
Z _ { n } = \int \mathrm { d } \Phi \exp [ - \beta \mathrm { t r } U ( \Phi ) ] .
$$

此积分区域为所有 $n \times n$ 厄密矩阵 $\Phi ^ { * } = \Phi$ 构成的空间 [ $\mathrm { d } \Phi$ 为该空间的体积元] ,

$$
U ( \lambda ) = \sum _ { j } g _ { j } \lambda ^ { 2 j }
$$

为多项式. 最近,[44] 表明此随机矩阵模型在非摄动弦理论 (nonperturbative string the-ory) 与 2D-引力当中极其重要.

事实上, 那个配分函数是某个差分版本的 Painlevé-I 方程的 $\tau { } _ { \cdot }$ -函数. 对于首个非平凡例子 $U ( \lambda ) = \frac { 1 } { 2 } \lambda ^ { 2 } + g \lambda ^ { 4 }$ , 相应的差分方程形如 [45]

$$
\frac { \eta } { \beta } = c _ { n } + 4 g c _ { n } ( c _ { n + 1 } + c _ { n } + c _ { n - 1 } ) , \quad c _ { n } = \frac { Z _ { n + 1 } Z _ { n - 1 } } { Z _ { n } ^ { 2 } } ,
$$

$$
\iff \quad [ L ^ { \mathrm { d i s c r } } , A ^ { \mathrm { d i s c r } } ] = \varepsilon \cdot 1 , \quad \varepsilon = \beta ^ { - 1 } .
$$

这里的 $L ^ { \mathrm { d i s c r } }$ , $A ^ { \mathrm { d i s c r } }$ 为差分算子:

$$
L _ { n m } ^ { \mathrm { d i s c r } } = c _ { n } ^ { 1 / 2 } \delta _ { n + 1 , m } + c _ { m } ^ { 1 / 2 } \delta _ { m + 1 , n }
$$

[正是离散 KdV 方程簇的 $L .$ -算子, 差分版本的薛定谔算子] ; 而 $A ^ { \mathrm { d i s c r } }$ 为离散 KdV 方程簇的算子:

$$
\begin{array} { r c l } { { { \cal A } _ { n m } ^ { \mathrm { d i s c r } } } } & { { = } } & { { 2 g \{ c _ { n } ^ { 1 / 2 } ( c _ { n - 1 } + c _ { n } + c _ { n + 1 } ) \delta _ { n + 1 , m } - c _ { m } ^ { 1 / 2 } ( c _ { m - 1 } + c _ { m } + c _ { m + 1 } ) \delta _ { m + 1 , n } } }  \\ { { } } & { { } } & { { + ( c _ { n } c _ { n + 1 } c _ { n + 2 } ) ^ { 1 / 2 } \delta _ { n + 3 , m } - ( c _ { m } c _ { m + 1 } c _ { m + 2 } ) ^ { 1 / 2 } \delta _ { m + 3 , n } \} } } \\ { { } } & { { } } & { { + { \displaystyle \frac { 1 } { 2 } } ( c _ { n } ^ { 1 / 2 } \delta _ { n + 1 , m } - c _ { m } ^ { 1 / 2 } \delta _ { m + 1 , n } ) . } } \end{array}
$$

可以证明 [44], 对 $u ( \log Z ) _ { x x }$ 取适当的连续极限

$$
Z _ { n } \mapsto Z ( x )
$$

之后, 可得到(3.59). 而在此我们只考虑连续情形.

[46] 研究了 Painlevé-I 方程的实解 [定义在半直线 $x > x _ { 0 } ]$ 的定性性质. 可以证明, 实解可分为两族: 类型 I 与类型 II. 类型 I 当中的解是光滑的: 它们沿着抛物线$u = - \sqrt { \frac { \varepsilon x } { 3 } }$ 震荡, 且振幅衰减. 类型 II 当中的解是奇异的, 某种意义下当 $x \to + \infty$ 时[在奇点外] 渐近于 $\sqrt { \frac { \varepsilon x } { 3 } }$ 此外, 还有临界解 (separatrix solution) [称为“类型 III”] , 渐近于 $\sqrt { \frac { \varepsilon x } { 3 } }$ 这些解的性质的大致描述见下图. 而我们这里只考虑类型 I 的解.

![](images/7f649803919b061c8323ebb724b1035614eeb8ea20d1579c731b09d6b6edb701.jpg)  
图 11.1

我们的想法 [43] 是用平均化方法, 考虑项 $\varepsilon x$ 的小扰动, 得到 Painlevé-I 方程 [简称P-I] 的渐近解. 这个想法至少在 $x \ll \infty$ 时看起来可行. 交换表示(3.58)对实现这个想法十分重要.

首先观察到(3.58)可以写成下述线性问题

$$
L \psi = \lambda \psi , \quad A \psi = \varepsilon \partial _ { \lambda } \psi
$$

的相容性条件. 等价地,

$$
\partial _ { \lambda } \vec { \psi } = U ( \lambda ) \vec { \psi } , \quad \varepsilon \partial _ { \lambda } \vec { \psi } = V ( \lambda ) \vec { \psi } ,
$$

或者

$$
[ \partial _ { x } - U ( \lambda ) , \varepsilon \partial _ { \lambda } - V ( \lambda ) ] = 0 \iff \varepsilon U ( \lambda ) - V _ { x } + [ U , V ] = 0 .
$$

根据以下断言, 关于谱曲线 $\Gamma$ 的 $x$ 的慢摄动的平均化系统是可积的.

引理. (见 [11]). 量子化交换方程 $[ L , A ] = \varepsilon \cdot 1$ 的平均化方程可表示为

$$
{ \frac { \mathrm { d } \mu } { \mathrm { d } X } } = { \frac { 1 } { 2 } } { \frac { \mathrm { d } p } { \mathrm { d } \lambda } }
$$

$[ X = \varepsilon x ]$ . 这里的 $\mu = { \sqrt { \operatorname* { d e t } V ( \lambda ) } }$ , $p = p ( \lambda )$ 为谱曲线 $\mu ^ { 2 } = \operatorname* { d e t } V$ 的拟动量.

点评. 在我们的例子中, 我们要寻找如下 P-I 方程的渐近解:

$$
u ( x ) = u ^ { ( 0 ) } ( x ) + \varepsilon u ^ { ( 1 ) } ( x ) + \cdot \cdot \cdot ,
$$

$$
u ^ { ( 0 ) } = 2 \wp \left( { \frac { \omega } { \pi } } { \frac { S ( X ) } { \varepsilon } } + \omega ^ { \prime } ; g _ { 2 } ( X ) , g _ { 3 } ( X ) \right) ,
$$

$$
{ \frac { \mathrm { d } S } { \mathrm { d } X } } = { \frac { \pi } { \omega } } .
$$

这里 $\mu = \sqrt { 4 \lambda ^ { 3 } - g _ { 2 } \lambda - g _ { 3 } }$ [对于类型 I 的解, 方程 $4 \lambda ^ { 3 } - g _ { 2 } \lambda - g _ { 3 } = 0$ 的根都是实根] , $p = p ( \lambda | g _ { 2 } , g _ { 3 } )$ 为某个椭圆积分 [见第2.4节末尾] . 从而我们由(3.66)得到 $g _ { 2 } , g _ { 3 }$ 关于 $X = \varepsilon x$ 的相关性. 这个形变 $\mu ^ { 2 } = 4 \lambda ^ { 3 } - g _ { 2 } ( X ) \lambda - g _ { 3 } ( X )$ 称为 平均化量子曲线(averaged quantum curve) .

证明. (1). 首先证明以下等式:

引入矩阵 $V ( \lambda )$ 的左, 右特征向量 $\langle \mu | , | \mu \rangle$ :

$$
V | \mu \rangle = \mu | \mu \rangle , \quad \langle \mu | V = \mu \langle \mu |
$$

$| \mu \rangle = { \binom { b } { \mu - a } } , \langle \mu | = ( c , \mu - a ) \operatorname { ] }$

$$
\mu _ { x } = \frac { \langle \mu \vert V _ { x } \vert \mu \rangle } { \langle \mu \vert \mu \rangle }
$$

[摄动理论的标准公式] .

$$
\mu _ { x } = \varepsilon \frac { \langle \mu | U _ { \lambda } | \mu \rangle } { \langle \mu | \mu \rangle } + \underbrace { \langle \mu | [ U , V ] | \mu \rangle } _ { = 0 } = \varepsilon \frac { \langle \mu | \begin{array} { l l } { 0 } & { 0 } \\ { 1 } & { 0 } \end{array} } { \langle \mu | \mu \rangle } = \varepsilon \frac { b } { 2 \mu } .
$$

(2). 将 $\mu _ { x } = \varepsilon { \frac { b } { 2 \mu } }$ 关于震荡作平均化, 有

$$
\frac { \mathrm { d } \mu } { \mathrm { d } X } = \frac { \bar { b } } { 2 \mu } .
$$

但因为2.4的公式(2.145), 有

从而引理得证.

$$
{ \frac { \bar { b } } { \mu } } = { \frac { \mathrm { d } p } { \mathrm { d } \lambda } } .
$$

我们只考虑椭圆情形.

推论 3.4. 平均化系统的动量

$$
c = \oint _ { a } \mu \mathrm { d } \lambda = c ( g _ { 2 } , g _ { 3 } )
$$

为常数.

其中 $a$ 为谱的空缺 $( e _ { 2 } , e _ { 1 } )$ [见2.4节末] 上的闭链. 我们已有 $\oint _ { a } \mathrm { d } p = 0$ .

证明. ${ \frac { { \mathrm { d } } c } { { \mathrm { d } } X } } = { \frac { 1 } { 2 } } { \frac { \mathrm { d } } { { \mathrm { d } } X } } \oint _ { a } { \mathrm { d } } p = 0 .$

推论 3.5.

$$
S = 2 \oint _ { b } \mu \mathrm { d } \lambda + S _ { 0 }
$$

为(3.69)的解. 这里的 $S _ { 0 }$ 为任意常数, 闭链 $b$ 在椭圆曲线上与 $a$ 共轭.

证明. 由公式 $\oint _ { b } \mathrm { d } p = { \frac { \pi } { \omega } }$ 可得. [见2.4节公式(2.139)] .

从(3.70), (3.71)出发, 经计算可得渐近解(3.67)的领头项为

$$
u ^ { 0 } ( x ) = 2 \wp \left( \frac { 4 } { 5 } \frac { g _ { 2 } } { \varepsilon } - \frac { 2 c \omega ^ { \prime } } { i \pi \varepsilon } + \frac { \omega } { \pi \varepsilon } S _ { 0 } + \omega ^ { \prime } \Big | g _ { 2 } , g _ { 3 } \right) ,
$$

$$
g _ { 2 } = \varepsilon x ,
$$

并且函数 $g _ { 3 } = g _ { 3 } ( \varepsilon x , c )$ 由下式决定:

$$
3 g _ { 3 } = 2 g _ { 2 } \frac { \eta } { \omega } - \frac { 5 c } { 2 \omega }
$$

$[ \eta = \eta ( g _ { 2 } , g _ { 3 } ) , \omega = \omega ( g _ { 2 } , g _ { 3 } ) ] \ , c , S _ { 0 } \ \dot { \mathcal { I } }$ 为任意常数.

类型 II 的解也有类似公式.

最让人惊讶的是, 这个渐近公式不仅对于有限的 $x$ , 在 $\varepsilon \to 0$ 时是好的, 而且对 $x$ 在$x \to \infty$ 时也是好的. 为此, 注意到当 $x \to \infty$ 时 $e _ { 3 } - e _ { 2 } \to 0$ . 此时求解方程(3.72b)可得

$$
e _ { 1 } \approx \sqrt { \frac { X } { 3 } } , e _ { 2 , 3 } \approx - \sqrt { \frac { X } { 1 2 } } \pm \sqrt { \frac { c } { \pi } } ( 1 2 X ) ^ { - 1 / 8 } ( X = \varepsilon x ) .
$$

因此,

$$
u ^ { ( } 0 ) \approx - \sqrt { \frac { X } { 3 } } - 2 \sqrt { \frac { c } { \pi } } ( 1 2 X ) ^ { - 1 / 8 } \cos \left[ \frac { 4 \sqrt [ 4 ] { 1 2 } } { 5 \varepsilon } X ^ { 5 / 4 } - \frac { 5 c } { 4 \pi \varepsilon } \log X + \frac { \tilde { S } _ { 0 } } { \varepsilon } \right] ,
$$

其中 $\tilde { S } _ { 0 }$ 为某个新的常数. 此公式恰为 P-I 方程的恰当解的渐近公式 [47].

对于 $L = - \partial _ { x } ^ { 2 } + u$ , $A$ 为 KdV 方程簇中的任一算子, 平均化之后的量子化方程(3.58)是可积的 [利用(3.66)] . 更一般的常微分算子的平均化量子化方程的可积性的证明可见 [48].

# 参考文献

# 泊松括号的几何

1. Balinskij, A.A. and Novikov, S.P.,(1985) Poisson brackets of hydrodynamics type, Frobenius algebras and Lie algebras, Sov. Math. Dokl. 32, 228-231.   
2. Grinberg, N.I., Poisson brackets of the hydrodynamic type with degenerate metric, Russian Math. Surveys 40:4, 231-232.   
3. Drinfel’d, V.G.,(1983) Hamiltonian structures on Lie Groups, Lie algebras and the geometrical meaning of the classical Yang-Baxter equations, Sov. Math. Dokl. 27, 68-71.   
4. Drinfel’d, V.G.,(1986) Quantum groups, J. Sov. Math. 41(1988), 898-915.   
5. Dubrovin, B.A.,(1989) Differential-geometrical Poisson brackets on a lattice, Funct. Anal. Appl. 23, 131-133.   
6. Dubrovin, B.A. and Novikov S.P.,(1983) The Hamiltonian formalism of one-dimensional systems of the hydrodynamic type and the Bogoliubov-Whitham averaging method, Sov. Math. Dokl. 27, 665-669.   
7. Dubrovin, B.A., and Novikov, S.P., (1984) On Poisson brackets of the hydrodynamic type, Sov. Math. Dokl. 30(1984), 651-654.   
8. Dubrovin, B.A., Novikov, S.P., Fomenko, A.T., (1984-1990) Modern Geometry. Parts I-III, Springer-Verlag, N.Y.   
9. Mokhov, O.I., (1988) Poisson brackets of the Dubrovin-Novikov type (DN-brackets), Funct. Anal. Appl. 22, 336-338.   
10. Novikov, S.P., (1982) Hamiltonian formalism and the multivalued analogue of Morse’s theory, Russian Math. Surveys 37:5, 1-56.   
11. Novikov, S.P., (1985) Geometry of conservative systems of the hydrodynamic type. The method of averaging for field-theory systems, Russian Math. Surveys 40:4, 85-98.   
12. Pavlov, M.V., (1987) Hamiltonian formalism of weakly nonlinear equations of hydrodynamics, Theoret. and Math. Phys. 73, 1242-1245.   
13. Polyak, M.V., (1987) One-dimensional Hamiltonian systems of the hydrodynamic type with an explicit dependence on the spatial variable, Russian Math. Surveys 42:3, 229-230.   
14. Potiomin, G.V., (1986) On Poisson brackets of differential-geometric type, Sov. Math. Dokl. 33, 30-33.   
15. Tsarev, S.P., (1989) The Hamilton property of stationary and inverse equation of condensed matter mechanics and mathematical physics, Math. Notes 46:1, 569-573.   
16. Tsarev, S.P., (1989) Liouville Poisson brackets and one-dimensional Hamiltonian systems of the hydrodynamics type which arise in the Bogolubov-Whitham theory of averaging, Russian Math. Surveys 39:6, 227-228.   
17. Tsarev, S.P., (1985) Poisson brackets and one-dimensional Hamiltonian systems of the hydrodynamic type, Sov. Math. Dokl. 34 (1987), 534-537.   
18. Astashov, A.M. and Vinogradov, A.M., (1986) On the structure of Hamiltonian operators in field theory, J. Geom. Phys. 3, 263-287.   
19. Zel’manov, E.I., (1987) On a class of local translationally invariant Lie algebras, Sov. Math. Dokl. 35, 216-218.   
20. Gelfand, I.M. and Dorfman, I.A., (1981) Hamiltonian operators and finite-dimensional Lie algebras, Funct. Anal. Appel. 15, 173-187.   
21. Gelfand, I.M. and Dorfman, I.A., (1979) Hamiltonian operators and related algebraic structures, Funct. Anal. Appl. 13, 246-262.   
22. Voroyev, Yu.M. and Karasev, M.V., (1968) Poisson manifolds and Schouten brackets, Funct. Anal. Appl. 22 (1988), 1-9.   
23. Dzyaloshinskii, I.E. and Volovik, G.E., (1980) Poisson brackets in condensed matter physics, Ann. of Phys. 125, 67-97.   
24. Faddeev, L.D., Takhtajan, L.A., (1986) Hamiltonian Methods in the Theory of Solitons, Springer-Verlag, Berlin, Heidelberg, New York, Tokyo.   
25. Jimbo, M., (1985) A q-difference analogue of $\mathcal { U } ( { \mathfrak { g } } )$ and the Yang-Baxter equations, Lett. Math. Phys. 10, 63-69.   
26. Arnold, V.I., (1974) Mathematical Methods of Classical Mechanics, Graduate Texts in Mathematics 60, Springer, New York-Berlin-Heidelberg.   
27. Novikov, S.P. (Ed.), (1980) The Theory of Soltons: the Inverse Problem Method, Nauka, Moscow. Translation: Plenum Press, N.Y., 1984.   
28. Veselov, P.A. and Takhtadjan, L.A., (1984) The integrability of Novikov’s equations for the principal chiral fields with a multi-valued Lagrangian, Sov. Phys. Dokl. 29, 994-996.   
29. Magri, F., (1978) A simple model of the integrable Hamiltonian system, J. Math. Phys. 19:5, 1156-1162.   
30. Dubrovin, B.A. and Novikov, S.P., (1989) Hydrodynamics of weakly deformed soliton lattices. Differential geometry and Hamiltonian theory, Russian Math. Surveys 44:6, 35-124.

# 可积系统

1. Veselov, A.P. and Novikov, S.P., (1982) On Poisson brackets compatible with algebraic geometry and the KdV dynamics on the set of finite-zone potentials, Sov. Math. Dokl. 26, 357-362.   
2. Veselov, A.P. and Novikov, S.P., (1984) Poisson brackets and complex tori, Proc. Stekolv Inst. Math. 165, 52-65.   
3. Dubrovin, B.A., (1975) Periodic problem for the Korteweg-de Vries equation in the class of finite-zone potentials, Funct. Anal. Appl. 9, 215-223.   
4. Dubrovin, B.A., (1981) Theta functions and nonlinear equations, Russian Math. Surveys 36:2, 11-92.   
5. Dubrovin, B.A., Krichever, I.M. and Novikov, S.P., (1985) Integrable system. I. Encyclopaedia of mathematical Sciences, vol.4, 173-280. Springer-Verlag, Berlin - Heidelberg - New York - London - Paris - Tokyo - Hong Kong.   
6. Dubrovin, B.A., Matveev, V.B. and Novikov, S.P., (1976) Non-linear equations of Kortewegde Vries type, finite-zone linear operators, and Abelian varieties, Russian Math. Surveys 31:1, 55-136.   
7. Dubrovin, B.A. and Novikov, S.P., (1982) Algebraic-geometric Poisson brackets for real finite-zone solutions of the Sine-Grodon and of the nonlinear Schrödinger equations, Sov. Math. Dokl. 26, 760-765.   
8. Dubrovin, B.A. and Novikov, S.P., (1974) Periodic and conditionally periodic analogs of the mani-soliton solutions of the Korteweg-de Vries equation, Sov. Phys. JETP 40, 1058-1063.   
9. Zakharov, V.E., (1980) Berney equations and the quasi-classical approximation in the inverse problem method, Funct. Anal. Appl. 14, 89-98.   
10. Zakharov, V.E. and Faddeev, L.D., (1971) The Korteweg-de Vries equation is a completely integrable Hamiltonian system, Ibid. 5, 280-287.   
11. Its, A.R. and Matveev, V.B., (1975) Hill operators with a finite-band spectrum and multisoliton solutions of the Korteweg-de Vries equations, Theor. and Math. Phys. 23, 343-355.   
12. Krechever, I.M., (1977) Integration of non-linear equations by the methods of algebraic geometry, Funct. Anal. Appl. 11, 12-26.   
13. Kuperschmidt, B.A. and Manin, Yu.I., (1977) Equations of long waves with a free boundary. I. Conservation laws and solutions, Ibid. 11, 188-197.   
14. Kuperschmidt, B.A. and Manin, Yu.I., (1978) Equations of long waves with a free boundary. II. Hamiltonian structures and higher order equations, Ibid. 12, 20-29.   
15. Novikov, S.P., (1974) A periodic problem for the Korteweg-de Vries equation. I. Ibidem 8, 236-240.   
16. Takhtadjan, L.A. and Faddeev, L.D. See ref.24 to Part I.   
17. Novikov, S.P., (Ed.). See ref.27 to Part I.   
18. Adler, M., (1979) On a trace functional for formal pseudodifferential operators and the sympletic structure of the Korteweg-de Vries type equations, Invent. Math. 50, 219-248.   
19. Benney, D.J., (1973) Some properties of long non-linear waves, Stud. Appl. Math. 52, 45-50.   
20. Dubrovin, B.A., Krichever, I.M. and Novikov, S.P., (1982) Topological and algebraic geometry methods in contemporary mathematical physics. II, Sov. Sci. Rev.: Math. Phys. Rev. 3, 1-150.   
21. Flaschka, H. and McLaughlin, D.W., (1976) Canonically conjugate variables for the Korteweg-de Vries equation and the Toda lattice with periodic boundary conditions, Progr. Theor. Phys. 55, 438-456.   
22. Gardner, G.S., (1971) Korteweg-de Vries equation and generalizations. IV, J. Math. Phys. 12, 1548-1551.   
23. Gibbons, J., (1981) Collisionless Boltzmann equations and integrable moment equations, Physica 3D, 503-511.   
24. Lax, P.D., (1974) Periodic solutions of the KdV-equation. Lectures in Appl. Math., vol.15, Amer. Math. Soc., Providence, R.I., 85-86.   
25. Belokolos, E.D., Bobenko, A.I., Matveev, V.B. and Enol’skii., V.Z., (1986) Algebraicgeometric principles of superposition of finite-zone solutions of integrable non-linear equations, Russian Math. Surveys 41:2, 1-49.   
26. Novikov, S.P., (1985) See ref.11 to Part I.   
27. Tsarev, S.P., (1985) See ref.17 to Part I.   
28. Tsarev, S.P., (1990) Geometry of Hamiltonian systems of hydrodynamic type. Generalized hodograph method, Soviet Math. Izvestija 54:5.   
29. Cartan, E., (1945) Les systèmes différentielles extérieures et leurs applications géomètriques, Hermann, Paris.   
30. Dubrovin, B.A. and Novikov, S.P. (1989) See ref.30 to Part I.   
31. Rozhdestvenskii, B.L. and Yanenko, N.N., (1978) Systems of quasilinear equations and their applications in gas dynamics, 2nd ed., Nauka, Moscow. (In Russian)   
32. Pavlov, M.V., (1987) Hamiltonian formalism of electrophoresis equations. Integrable equations of hydrodynamics. London Inst. Preprint 87-17, Moscow.   
33. Nijenhuis, A., (1951) On $X _ { n - 1 }$ forming sets of eigenvectors, Indag Math. 13, 200-212.   
34. Haantjes, J., (1954) On $X _ { m }$ -forming sets of eigenvectors, Indag. Math. 17, 158-162.   
35. Bogoyavlenskii, O.I. and Novikov, S.P., (1976) The relationship between the Hamiltonian formalisms of stationary and nonstationary problems, Funct. Anal. Appl. 10 (1976), 8-11.   
36. Mokhov, O.I., (1987) On the Hamiltonian property of an arbitrary evolution system on the set of stationary points of its integral, Math. USSR Izvestiya 31:3, 657-664.   
37. Lax, P.D., (1974) Periodic solutions of the KdV equations, Non-linear Wave Motion (A.C. Newell editor). Lectures in Appl. Math., vol.15, Amer. Math. Soc., Providence, R.I., 85-96.   
38. Mihkailov, A.V., Shabat, A.B. and Yamilov, R.I., (1987) The symmetry approach to the classification of non-linear equations. Complete lists of integrable systems, Russian Math. Surveys 42:4, 1-63.   
39. Ibragimov, N.K., (1985) Transformation groups applied to mathematical physics. Reidel, Dordrecht.   
40. Sokolov, V.V., (1988) On the symmetries of evolution equations, Russian Math. Surveys 43:5, 165-204.   
41. Fay, J.,(1973) Theta functions on Riemann surfaces. Lecture Notes in Math. 352, Springer-Verlag, N.Y.   
42. Dubrovin, B.A., (1990) The differential geometry of strongly integrable systems of the hydrodynamic type, Funct. Anal. Appl. 24.   
43. Darboux, G., (1910) Leçons sur les systèmes orthogonaux et les coordonnées curvilignes. Paris.   
44. Egoroff, D.F., (1901) Selected papers in differential geometry, Nauka, Moscow, 1970. (In Russian).   
45. Dubrovin, B.A., (1977) Completely integrable Hamiltonian systems associated with matrix operators and Abelian varieties, Funct. Anal. Appl. 11, 265-277.   
46. Dubrovin, B.A., (1983) Matrix finite-gap operators, J. Soviet Math. 28 (1985), 20-50.   
47. Fokas, A.S., Leo, R.A., Martina, L. and Soliani, G. (1986), Phys. Lett. 115A, 329-332.   
48. Bateman, H. and Erdélyi, (1955) Higher transcendental functions, vol.3, McGraw-Hill, New York - Toronto - London.

# 哈密顿系统的慢摄动与平均化方法

1. Avilov, V.V. and Novikov, S.P., (1987) Evolution of the Whitham zone in KdV theory, Sov. Phys. Dokl. 32, 366-368.   
2. Avilov, V.V., Krichever, I.M. and Novikov, S.P., (1987) Evolution of the Whitham zone in the Korteweg-de Vries theory, Sov. Phys. Dokl. 32, 564-566.   
3. Vereshchagin, V.L., (1988) Hamiltonian structure of averaged difference schemes. Math. Notes 44, 798-805.   
4. Gurevich, A.V. and Pitaevskii, L.P., (1973) Non-stationary structure of a collisionless shock wave, Sov. Phys. JETP 38, 291-297.   
5. Gurevich, A.V. and Pitaevskii, L.P., (1987) Averaged description of waves in the Kortewegde Vries-Burgers equation, Ibidem, 93, 871-880.   
6. Gurevich, A.V. and Pitaevskii, L.P., (1973) Decay of initial discontinuity in the Kortewegde Vries equation, JETP Letters 17, 193-195.   
7. Dobrokhotov, S. Yu., (1988) Resonance correction to the adiabatically perturbed finite-zone almost periodic solution of the Korteweg-de Vries equation. Math. Notes 44:3, 656-668.   
8. Dobrokhotov, S. Yu., (1988) Resonances in the asymptotics of solution of the Cauchy problem for the Schrödinger equation with a rapidly oscillating finite-zone potential. Math. Notes 44, 656-668. 9. Dobrokhotov, S. Yu. and Maslov, V.P., (1980) Finite-gap almost periodic solutions in WKB-approximations, J. Sov. Math. 16, 1433-1487.   
10. Dubrovin, B.A. and Novikov, S.P. (1983). See ref.6 to Part I.   
11. Krichever, I.M., (1988) The method of averaging for two-dimensional “integrable" equations, Funct. Anal. Appl. 22, 200-213.   
12. Krichever, I.M., (1989) Spectral theory of two-dimensional periodic operators and its applications, Russian Math. Surveys 44, 145-225.   
13. Dubrovin, B.A. and Novikov, S.P. (1989). See ref.30 to Part I.   
14. Maslov, V.P., (1969) Transition as $h  0$ of the Heisenberg equation to the equation of dynamics of an ideal monoatomic gas and the quantization of relativistic hydrodynamics, Theor. and Math. Phys. 1. 378-384.   
15. Novikov, S.P., (1985). See ref.11 to Part I.   
16. Pavlov, M.V., (1987) The non-linear Schrödinger equation and the Bogolyubov-Whitham averaging method, Theor. and Math. Phys. 71, 584-588.   
17. Potiomin, G.V., (1988) Algebraic-geometric construction of self-similar solutions of the Whitham equations, Russian Math. Surveys 43:5, 252-253.   
18. Whitham, G.B., (1974) Linear and Nonlinear Waves. Wiley Interscience, New York - London - Sydney.   
19. Ablowitz, M.J. and Benney, D.J., (1970) The evolution of multiphase modes for non-linear dispersive waves, Stud. Appl. Math. 49, 225-238.   
20. Bikbaev, R.F. and Novokshenov, V.Yu., (1988) Self-similar solutions of the Whitham equations and the KdV equation with finite-gap boundary conditions. Proc. III Inter. Workshop, vol.I, Kiev 1988, 32-35.   
21. Chierchia, L., Ercolani N. and McLaughlin D.W. (1987), On the weak limit of rapidly oscillating waves, Duke Math. J. 55, 759-764.   
22. Dobrokhotov, S. Yu. and Maslov, V.P., (1982) Multiphase asymptotics of non-linear partial differential equations with a small parameter, Sov. Sci. Rev.: Math. Phy. Rev. 3, 221-311.   
23. Ercolani, N., Forest, M.G., McLaughlin, D.W. and Montgomery, R., (1987) Hamiltonian structure of the modulation equations of a Sine-Gordon wavetrain, Duke Math. J. 55, 949-983.   
24. Flaschka, H., Forest, M.G. and McLaughlin, D.W., (1980) Multiphase averaging and the inverse spectral solution of the Korteweg-de Vries equation, Comm. Pure Appl. Math. 33, 739-784.   
25. Forest, M.G. and McLaughlin, D.W., (1984) Modulations of perturbed KdV wavefronts, SIAM J. Appl. Math. 44, 278-300.   
26. Forest, M.G. and McLaughlin, D.W., (1983) Modulation of Sinh and Sine-Gordon wavetrains, Stud. Appl. Math. 68, 11-59.   
27. Goodman, J. and Lax, P.D., (1988) On dispersive difference schemes, Comm. Pure Appl. Math. 41, 591-613.   
28. Hayes, W.D., (1973) Group velocity and non-linear dispersive wave propagation, Proc. Royal Soc. London A332, 199-221.   
29. Lax. P.D., (1986) On dispersive difference schemes, Physica 18D, 250-254.   
30. Lax, P.D., (1988) Oscillatory solutions of partial differential and difference equations. (In: Mathematics Applied to Since, Acad. Press, N.Y., 155-170).   
31. Lax, P.D., (1983) The small dispersion limit of the Korteweg-de Vries equation. II, III, Comm. Pure Appl. Math. 36, 253-290.   
32. Lax, P.D. and Levermore, C.D., (1983) The small dispersion limit of the Korteweg-de Vries equation. II, III, Comm. Pure Appl. Math. 36, 571-593, 809-830.   
33. Luke, J.L., (1966) A perturbation method for non-linear dispersive wave problems, Proc, Royal Soc. London A 292, 403-412.   
34. Venakides, S., (1987) The zero-dispersion limit of the periodic KdV equation, Trans. Amer. Math. Soc. 301, 189-226.   
35. Venakides, S., (1985) The zero-dispersion limit of the KdV equation with non-trivial reflection coefficient, Comm. Pure Appl. Math. 38, 125-155.   
36. Whitham, G.B., (1965) A general approach to linear and non-linear dispersive waves using a Lagrangian, J. Fluid Mech. 22, 273-283.   
37. Whitham, G.B., (1965) Non-linear dispersive waves, Proc. Royal Soc. London A139, 283-291.   
38. Dubrovin, B.A., (1990) See ref.42 to Part II.   
39. Novikov, S.P., (Ed.). See ref.27 to Part I.   
40. Bikbaev, R.F. and Novokshenov, V. Yu. Math. USSR Izvestija.   
41. Dubrovin, B.A., Krichever, I.M. and Novikov, S.P. (1985). See ref.5 to Part II.   
42. Novikov, S.P. (1990), Progress Theor. Phys. Suppl. 102.   
43. Dubrovin, B.A. and Novikov, S.P., (1990) Ibidem, Appendix to ref.42.   
44. Brezin, E. and Kazakov, V.A., (1990), Phys. Lett. 236B, 144; Douglas, M. and Shenkar, S. (1989), Strings in Less than One Dimension, Rutgers preprint RU-89-34; Gross, D. and Migdal, A.A. (1990), Phys. Rev. Lett. 64, 127.   
45. Fokas, A.S., Its, A.R. and Kitaev, A.V., (1990) Isomonodromic approach in 2D quantum gravity, Russian Math. Surveys 45:6.   
46. Holmes, Ph. and Spence, D. (1984), On a Painlevé-type boundary-value problem, Quart. J. Mech. and Appl. Math. 37:4, 525-538.   
47. Krichever, I.M., (1990), On Heisenberg relation for ordinary differential operators. Preprint. Zürich.

# 名词英汉对照

Abelian variety 阿贝尔簇, 79  
action-angle variable 作用量-角参数, iv  
algorithm of integration 积分算法, 45  
annihilator 零化子, 2  
averaged Hamiltonian formalism 平均化  
哈密顿理论, 90  
averaged quantum curve 平均化量子曲  
线, 109  
averaging method 平均化方法, 15  
bi-Hamiltonian 双哈密顿, 69  
chiral field 手性场, 22  
cnoidal wave 椭圆余弦波, 85  
co-associative 余结合, 8  
co-vector 余向量, 49  
coboundary 上边缘, 11  
commutative representation 交换表示,  
65  
complete integrability 完全可积性, 13  
consetvation law 守恒律, 3  
continuous prolongation 连续延伸, 39  
distribution 广义函数, 17  
Egoroff metric Egoroff 度量, 52  
equation of slow modulation 慢调制方  
程, 88  
finite-gap operator 有限空缺算子, 78  
flux density 流密度, 70  
foliation 叶状结构, 2

generalized hodograph transform 广义 速端曲线变换, 47

Hamiltonian 哈密顿量, 2  
Hamiltonian formalism 哈密顿理论, 1  
Hamiltonian system 哈密顿系统, 2  
Hamiltonian-Lie group 哈密顿-李群, 8  
Hermitean random matrix model 厄密随机矩阵模型, 107  
hierarchy 方程簇, 65  
hodograph method 速端曲线法, 46  
hodograph transform 速端曲线变换, 46  
invariant tori 不变环, iv  
inverse scattering method 反散射方法,23

Jacobi identity 雅可比恒等式, 1   
Jacobi variety 雅可比簇, 79   
lattice 格, 36   
Leibnitz rule 莱布尼茨法则, 1   
level surface 等值面, 13   
Lie bi-algebra 李双代数, 10   
Lie-Poisson bracket 李-泊松括号, 5   
local field-theoretic functional 局部场论   
泛函, 18   
local field-theoretic Poisson bracket 局   
部场论泊松括号, 19   
loop algebra 圈代数, 23   
loop group 圈群, 23   
mutliphase solution 多相解, 87   
one-phase solution 单相解, 87   
partition function 配分函数, 107   
perturbation theory 摄动理论, 15   
phase space 相空间, 1   
Poisson bracket 泊松括号, 1   
Poisson symmetry 泊松对称, 3

zero-curvature representation 零曲率表示, 65

quantization 量子化, 106  
quantum group 量子群, 10  
quasi-triangular Hopf algebra 拟三角  
Hopf 代数, 12  
quasimomentum 拟矩, 72  
Riemann invariant 黎曼不变量, 49  
rotation coefficient 旋转系数, 52  
Schouten bracket Schouten 括号, 2  
semi-Hamiltonian system 半哈密顿系  
统, 45  
simple wave 单波, 84  
skew gradient 斜梯度, 3  
soliton 孤子, 64  
spectral curve 谱曲线, 78  
spectral parameter 谱参数, 65  
symmetry 对称, 3  
symplectic leaf 辛叶, 2  
symplectic manifold 辛流形, 2  
symplectic structure 辛结构, 2  
ultralocal Poisson bracket 超局部泊松  
括号, 21  
Whitham averaged equation 惠特姆平  
均化方程, 88