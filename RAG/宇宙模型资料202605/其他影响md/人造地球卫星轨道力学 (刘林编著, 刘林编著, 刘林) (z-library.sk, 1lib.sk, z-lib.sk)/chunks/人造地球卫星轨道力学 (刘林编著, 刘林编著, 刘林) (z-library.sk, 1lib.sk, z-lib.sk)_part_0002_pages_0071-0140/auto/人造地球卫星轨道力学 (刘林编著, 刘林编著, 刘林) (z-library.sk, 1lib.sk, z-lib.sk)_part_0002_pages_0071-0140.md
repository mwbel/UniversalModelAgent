要由方位观测直接得到地心向径 $\pmb { r } _ { 1 }$ ，就必须同时知道卫星到测站的距离 $\rho$ ，如果已知轨道平面的空间定向，即可达到此目的。利用轨道平面法向单位向量 $\hat { \pmb R }$ 的三个分量(见第二章(2.4)式),可写出轨道平面方程，即

$$
A x + B y + c z = 0 ,
$$

或

$$
\pmb { g x } + \pmb { h } \pmb { y } + \pmb { z } = \pmb { 0 } .
$$

其中

$$
g = \frac { A } { C } { = } \mathfrak { t g i } \sin \Omega , \quad h { = } \frac { B } { C } { = } { - } \mathfrak { t g i } \cos \Omega .
$$

将(3.53)式的 $\pmb { r }$ 代人方程(3.55)得

$$
\rho = - \frac { g x + l _ { i } y + z } { g \lambda + h \mu + y } ,
$$

油 $\rho$ 即可算出 $\pmb { r }$ ，下面的问题是如何转换成轨道根数，这在前面$\mathfrak { f 3 . 1 }$ 中已介绍过，但定向根数 $i , \Omega$ 未知，即仅考虑到几何关系是不够的．与拉普拉斯方法类似,可以假定知道 $i , \Omega$ 的初值，然后由力学条件来检验，反复进行迭代，从而确定轨道平面，并同时算出卫星向径 $\pmb { r } _ { + }$

所谓力学条件,这里指的是卫星从 $r _ { 1 }$ 到 $\pmb { r _ { 2 } }$ 并非任意，它应满足椭圆运动性质，有

$$
n \tau = ( E _ { 2 } { - } E _ { 1 } ) \longrightarrow e ( \sin E _ { 2 } { - } \sin E _ { 1 } ) .
$$

其中 $\tau { = } t _ { 2 } { - } t _ { 1 }$ ．这一条件不便于直接引用，下面采用相应的朗伯方程(它可叫做条件方程,其推导将在后面给出)：

$$
n \tau _ { i } = ( e _ { i } - \delta _ { i } ) - ( \sin \varepsilon _ { i } - \sin \delta _ { i } ) .
$$

其中

$$
\begin{array} { c } { { \tau _ { i } = t _ { k } - t _ { j } , } } \\ { { \sin \varepsilon _ { i } / 2 = \pm \left( \displaystyle \frac { r _ { j } + r _ { k } + \sigma _ { i } } { 4 a } \right) ^ { 1 / 2 } , } } \\ { { \sin \delta _ { i } / 2 = \pm \left( \displaystyle \frac { r _ { j } + r _ { k } - \sigma _ { i } } { 4 a } \right) ^ { 1 / 2 } , } } \\ { { \cos ( x _ { k } - x _ { j } ) ^ { 2 } + ( y _ { k } - y _ { j } ) ^ { 2 } + ( z _ { k } - z _ { j } ) ^ { 2 } ] ^ { 1 / 2 } } } \end{array}
$$

下标 $i , j , k , = 1 , 2 , 3 ,$ 且 $k { \Rightarrow } j { \neq } i ,$ 两次观测组成一个方程，容易看出，三次观测对应的条件方程(3.59)只有两个是独立的，它与方程(3.57)一共有五个，包含了五个未知量： $g , h$ 和三个 $\rho _ { j } ( j { = } 1 , ~ 2 ,$ 3)，原则上可解，但这组超越方程无法直接求解，下面采用迭代法.至于si $a e _ { i } / 2$ 和 $\sin \theta _ { i }$ /2右端正、负号的取法，请见后面推导朗伯方程时的说明.

首先选取适当的初值 $g ^ { ( 0 ) }$ 和 $\pmb { \hbar } ^ { ( 0 ) }$ （即 $\pmb { i } ^ { ( 0 ) }$ 和 $\Omega ^ { ( 0 ) }$ ），由(3.57）式算出 $\rho _ { j \pmb { \mathscr { s } } }$ 再由(3.53)式算出 $r _ { i } ( x _ { j } , y _ { j } , z _ { j } )$ ，代入朗伯方程(3.59）算出残差 $\Delta _ { i } \gimel$

$$
\Delta _ { i } = n \tau _ { i } - [ ( e _ { i } - \delta _ { i } ) - ( \sin \varepsilon _ { i } - \sin \delta _ { i } ) ] .
$$

再用微分改正法改正 ${ \pmb g } ^ { ( 0 ) }$ 和 ${ h ^ { ( 0 ) } }$ ，改正公式为

$$
\Delta _ { \imath } = - \frac { \partial F _ { i } } { \partial g } \Delta g - \frac { \partial F _ { i } } { \partial h } \Delta h ,
$$

$$
\begin{array} { r l } & { \displaystyle \frac { \partial F _ { i } } { \partial g } = \frac { x _ { j } } { a m _ { j } } \bigg ( \frac { 1 } { r _ { j } } M _ { j } U _ { i } + \frac { 1 } { \sigma _ { i } } N _ { j } V _ { i } \bigg ) + \frac { x _ { k } } { a m _ { k } } \bigg ( \frac { 1 } { r _ { k } } M _ { k } U _ { i } - \frac { 1 } { \sigma _ { i } } N _ { k } V _ { i } \bigg ) , } \\ & { \displaystyle \frac { \partial F _ { i } } { \partial h } = \frac { y _ { j } } { a m _ { j } } \bigg ( \frac { 1 } { r _ { j } } M _ { j } U _ { i } + \frac { 1 } { \sigma _ { i } } N _ { j } V _ { i } \bigg ) + \frac { y _ { k } } { a m _ { k } } \bigg ( \frac { 1 } { r _ { k } } M _ { k } U _ { i } - \frac { 1 } { \sigma _ { i } } N _ { k } V _ { i } \bigg ) . } \end{array}
$$

其中

$$
\left. \begin{array} { l } { m _ { j } = \lambda _ { j } g + \mu _ { j } h + \nu , ~ m _ { k } = \lambda _ { k } g + \mu _ { k } h + \nu _ { k j } , } \\ { M _ { j } = \lambda _ { j } x _ { j } + \mu _ { j } y _ { j } + \nu _ { j } z _ { j } , ~ M _ { k } = \lambda _ { k } x _ { k } + \mu _ { k } y _ { k } + \nu _ { k } z _ { k } , } \\ { N _ { j } = \lambda _ { j } ( x _ { k } - x _ { j } ) + \mu _ { j } ( y _ { k } - y _ { j } ) + \nu _ { j } ( z _ { k } - z _ { j } ) , } \\ { N _ { k } = \lambda _ { k } ( x _ { k } - x _ { j } ) + \mu _ { k } ( y _ { k } - y _ { j } ) + \nu _ { k } ( z _ { k } - z _ { j } ) , } \\ { U _ { i } = \frac { \sin ^ { 2 } \frac { \partial _ { i } } { 2 } } { \sin \delta _ { i } } - \frac { \sin ^ { 2 } \frac { \delta _ { i } } { 2 } } { \sin \delta _ { i } } , ~ V _ { i } = \frac { \sin ^ { 2 } \frac { \partial _ { i } } { 2 } } { \sin \delta _ { i } } + \frac { \sin ^ { 2 } \frac { \delta _ { i } } { 2 } } { \sin \alpha _ { i } } . } \end{array} \right\}
$$

解出 $\Delta g$ 和 $\Delta \hbar$ 后改正 ${ \pmb g } ^ { ( 0 ) }$ 和 $\pmb { \lambda } ^ { ( 0 ) }$ 得

$$
g ^ { ( 1 ) } { = } g ^ { ( 0 ) } { + } \Delta g , ~ \hbar ^ { ( 1 ) } { = } \hbar ^ { ( 0 ) } { + } \Delta h .
$$

由此重复上述步骤，直至残差 $\Delta _ { i }$ 达到要求的精度为止，从而算出$z \theta , h$ 和 $r _ { j } ( j = 1 , 2 , 3 )$ ，这里说明一下改正公式(3.62)的由来，记

$$
F _ { i } = F _ { i } ( g , h , a ) = n \tau _ { i } - [ ( \varepsilon _ { i } - \delta _ { i } ) - ( \sin \varepsilon _ { i } - \sin \delta _ { i } ) ]
$$

函数 $\pmb { F _ { i } }$ 的真值是零,近似值是 $\Delta _ { i j }$ 从而有

$$
\begin{array} { r } { 0 = \Delta _ { i } + \displaystyle \frac { \partial { \cal F } _ { i } } { \partial g } \Delta g + \displaystyle \frac { \partial { \cal F } _ { i } } { \partial h } \Delta h , } \end{array}
$$

此即改正公式(3.62)．关于偏导数 $\partial F _ { i } / \partial g , \partial F _ { i } / \partial h ,$ ，读者如有兴趣可自己推导.

# 2．计算五个根数

首先由 $g , h$ 算出 $i , \Omega$ 。根据(3.56)式可得

$$
\displaystyle \mathrm { t g } i = \pm { \sqrt { g ^ { - } + h ^ { 2 } } } .
$$

等式右端取正号还是负号，这就涉及到 $\textbf { \em i }$ 的象限问题．一般 $i$ 变化不大，我们事先可以知道它的象限，但若 $i \approx 9 0 ^ { \circ }$ 而难以确定其象限时,可用轨道面法向单位向量在 $\pmb { z }$ 轴上的分量来确定，即

$$
\cos i = ( \boldsymbol { r } _ { 1 } \times \boldsymbol { r } _ { 2 } ) _ { z } / \left| \boldsymbol { r } _ { 1 } \times \boldsymbol { r } _ { 2 } \right| .
$$

$\textbf { \textit { i } }$ 的象限确定后，就可以计算 $2$ 若 $\tan i > 0$ 有

$$
\mathrm { { t g } } \Omega = { \pmb g } / ( - h ) ,
$$

否则

$$
\mathbf { t g } { \boldsymbol { \varOmega } } = \left( - { \pmb g } \right) / h .
$$

上两式右端的分子和分母的符号分别表示 sin $\pmb { \Omega }$ 和 $\cos \Omega$ 的符号，这样， $\pmb { \Omega }$ 的象限就能唯一确定。

由 $\pmb { a }$ 和 $\boldsymbol { r } _ { j }$ 中的任何两个（例如取 $\pmb { r _ { 1 } }$ 和 $r _ { 2 }$ 可算出另三个根数$\mathbf { \mathcal { L } } , \mathcal { M } _ { \mathrm { ~ l ~ } }$ 和 $\pmb { \omega }$ ，引用下式

$$
\left. \begin{array} { l } { e \cos { E _ { 1 } } = 1 - \frac { r _ { 1 } } { a } , \quad e \cos { E _ { 2 } } = 1 - \frac { r _ { 2 } } { a } , } \\ { e \sin { E _ { 1 } } = \frac { e \cos { E _ { 1 } } \cos { 2 q _ { 3 } } - e \cos { E _ { 2 } } } { \sin { 2 q _ { 3 } } } . } \end{array} \right\}
$$

计算 $\pmb { e }$ 和 $E _ { 1 \rangle }$ 再由开普勒方程:

$$
\boldsymbol { \mathcal { M } } _ { 1 } { = } \boldsymbol { \mathcal { E } } _ { 1 } { - } e \sin \boldsymbol { \mathcal { E } } _ { 1 }
$$

即可算出 $M _ { 1 }$ （3.69）式中的 $\cos i \ n \mathbf { \mathcal { B } } _ { 1 }$ 是由

$$
\begin{array} { r l } & { e \cos { E _ { 2 } } = e \cos { [ E _ { 1 } + ( E _ { 2 } - E _ { 1 } ) ] } } \\ & { \qquad = e \cos { E _ { 1 } } \cos { ( E _ { 2 } - E _ { 1 } ) } - e \sin { E _ { 1 } } \sin { ( E _ { 2 } - E _ { 1 } ) } } \end{array}
$$

推出,其中 $\begin{array} { r } { \pmb { { \cal E } } _ { 2 } - \pmb { { \cal E } } _ { 1 } = \pmb { \mathscr { e } } _ { 8 } - \delta _ { 3 } , } \end{array}$ 记作 $2 \textmu _ { 3 } ,$ 这在下一段推导朗伯方程时会给出，最后由下面一组公式算出 $\omega _ { \ast }$

$$
\left. \begin{array} { l } { \displaystyle \mathrm { t g } u _ { 1 } = \frac { z _ { 1 } / \sin i } { x _ { 1 } \cos \varOmega + y _ { 1 } \sin \varOmega } ; } \\ { \displaystyle \mathrm { t g } \frac { f _ { 1 } } { 2 } = \sqrt { \frac { 1 + e } { 1 - e } } \mathrm { t g } \frac { E _ { 1 } } { 2 } , } \\ { \displaystyle \omega = u _ { 1 } - f . } \end{array} \right\}
$$

其中 $\mathbf { t } \mathbf { g } \pmb { u } _ { 1 }$ 是由 $\sin { u } _ { 1 }$ 和 $\mathbf { c o s } \pmb { u } _ { 1 }$ 导出，而

$$
\sin u _ { 1 } = \frac { \sin \varphi _ { 1 } } { \sin i } = \frac { ( z _ { 1 } / r _ { 1 } ) } { \sin i } .
$$

$$
\scriptstyle \cos u _ { 1 } = { \hat { r } } _ { \uparrow } \cdot { \hat { N } } = \left( { \frac { x _ { 1 } } { r _ { 1 } } } \right) \cos \varOmega + \left( { \frac { y _ { 1 } } { r _ { 1 } } } \right) \sin \varOmega ,
$$

$\hat { \pmb { r } } _ { 1 }$ 和 $\hat { \mathbf { N } }$ 分别为卫星方向和升交点方向的单位向量。到此，五个根数全部给出.

# 3.几点说明

（1）从原理上看，只需三次观测．用力学条件一一朗伯方程来“控制"计算，实际上就是调整轨道平面 $( i , \Omega )$ 使其满足椭圆运动所应遵循的条件，这相当于拉普拉斯方法中“自然”调节半长径${ \pmb a }$ 的效果．但这一方法中半长径 $\pmb { a }$ 是固定的，因此三次观测不一定同在一个椭圆上，例如改用第一和第三次观测（即 $r _ { 1 }$ 和 $r _ { 3 }$ ，那么给出的 $e , M _ { \mathrm { i } } , \omega$ 三个根数就可能与前面给出的不同，若要改进短弧定轨的效果，也可采用多资料，相应的条件方程(3.59)及其改正公式(3.62)均多于两个,可用简单的最小二乘法求改正量 $\Delta g$ 和$\Delta h$ 的最佳解，对多个残差 $\Delta _ { i }$ （包括对坏资料的剔除）的处理亦类似于拉普拉斯方法中对 $\Delta F _ { j }$ 和 $\Delta G _ { j }$ 的处理，这样一来，既保证半长径 $\pmb { a }$ 直接引用已知的较准确的值，又可在一定精度条件下(指观测资料)获得另五个较理想的根数。

（2）关于已知 $\pmb { a }$ 值的问题，从上述迭代过程来看， $\pmb { \alpha }$ 无需事先知道，这正是原巴日诺夫方法[81．但需要四次观测才能构成三个独立的条件方程(3.59)，这不仅影响上述迭代过程的收敛速度，而且它又将遇到短弧定轨的难题： $\pmb { a }$ 同样定不准，通常还是固定 $\pmb { a }$ 值为好，这已为大量的计算所证实.

（3）这一方法将卫星运动的几何条件和轨道平面联系起来是一特点．因卫星离地面较近(斜距 $\rho$ 较小)， $g , h$ 的一个微小改变将会引起 $\rho$ 的较大变化，这样用朗伯方程来控制收敛定出的 $g , h$ 就较准．当然，若观测站位于或接近卫星轨道面时，(3.57)式右端分子分母都接近零，相应的 $\pmb { \rho }$ 无法计算．不过这样的情况很难得，如发生，可将相应的资料舍去，或采取相应的改进措施。

# 4．朗伯方程的推导和 $\varepsilon _ { i } , \delta _ { j }$ 的象限问题定义

$$
\left. \begin{array} { c } { { 2 Q _ { i } = E _ { k } + E _ { j } , ~ 2 q _ { i } = E _ { k } - E _ { j } , } } \\ { { } } \\ { { \cos p _ { i } = e \cos Q _ { i } , } } \\ { { } } \\ { { e _ { i } = p _ { i } + q _ { i } , ~ \delta _ { i } = p _ { i } - q _ { i } . } } \end{array} \right\}
$$

由定义可知

$$
\left. \begin{array} { l } { { \varepsilon _ { i } - \delta _ { i } = 2 q _ { i } = E _ { k } - E _ { j } } } \\ { { } } \\ { { e _ { i } + \delta _ { i } = 2 p _ { i } . } } \end{array} \right\}
$$

根据开普勒方程，并利用三角函数的和差化积公式

$$
\begin{array} { r l } & { \sin { E _ { k } } - \sin { E _ { j } } = 2 \cos { \frac { 1 } { 2 } } \ ( E _ { k } + E _ { j } ) \ \sin { \frac { 1 } { 2 } } ( E _ { k } - E _ { j } ) , } \\ & { \cos { E _ { k } } - \cos { E _ { j } } = - 2 \sin { \frac { 1 } { 2 } } \ ( E _ { k } + E _ { j } ) \ \sin { \frac { 1 } { 2 } } ( E _ { k } - E _ { j } ) , } \end{array}
$$

$$
\mathrm { \mathrm { \small ~ \mathfrak ~ { \circ \ o s } } } E _ { b } + \mathrm { \small ~ { \ c o s } } E _ { j } = 2 \mathrm { \textnormal { \small o s } } \frac { 1 } { 2 } \mathrm { \small ~ ( } E _ { k } + E _ { j } ) \mathrm { \small ~ \cos ~ } \frac { 1 } { 2 } ( E _ { k } - E _ { j } ) ,
$$

立即可得

$$
\begin{array} { r l } {  { n ( { \boldsymbol { \varepsilon } } _ { k } - { \boldsymbol { t } } _ { j } ) = n { \boldsymbol { \tau } } _ { i } = ( E _ { k } - E _ { j } ) - e ( \sin E _ { k } - \sin E _ { j } ) } } \\ & { = ( { \boldsymbol { \varepsilon } } _ { i } - \delta _ { i } ) - 2 e \cos Q _ { i } \sin { \boldsymbol { q } } _ { i } } \\ & { = ( { \boldsymbol { \varepsilon } } _ { i } - \delta _ { i } ) - 2 \cos { \boldsymbol { p } } _ { i } \sin { \boldsymbol { q } } _ { i } } \\ & { = ( { \boldsymbol { \varepsilon } } _ { i } - \delta _ { i } ) - 2 \cos \frac { 1 } { 2 } ( { \boldsymbol { \varepsilon } } _ { i } + \delta _ { i } ) \sin \frac { 1 } { 2 } ( { \boldsymbol { \varepsilon } } _ { i } - \delta _ { i } ) } \\ & { = ( { \boldsymbol { \varepsilon } } _ { i } - \delta _ { i } ) - ( \sin { \boldsymbol { \varepsilon } } _ { i } - \sin \delta _ { i } ) . } \end{array}
$$

这就是朗伯方程，剩下的问题是 $\ell _ { 1 }$ 和 $\delta _ { i }$ 如何计算，根据弦长 ${ \pmb { \sigma } } _ { \pmb { \imath } }$ 的定义有

$$
\begin{array} { r l } & { \sigma _ { \mathfrak { s } } ^ { 2 } = ( x _ { k } - x _ { j } ) ^ { 2 } + ( y _ { k } - y _ { j } ) ^ { 2 } + ( z _ { k } - z _ { j } ) ^ { 2 } } \\ & { \quad = ( r _ { k } \cos f _ { k } - r _ { j } \cos f _ { j } ) ^ { 2 } + ( r _ { k } \sin f _ { k } - r _ { j } \sin f _ { j } ) ^ { 2 } } \\ & { \quad = a ^ { 2 } \big ( \cos  { E _ { k } } - \cos  { E _ { j } } ) ^ { 2 } + a ^ { 2 } ( 1 - e ^ { 2 } ) \big ( \sin  { E _ { \mathfrak { s } } } - \sin  { E _ { j } } \big ) ^ { 2 } } \\ & { \quad = 4 a ^ { 2 } \sin ^ { 2 } Q _ { i } \sin ^ { 2 } q _ { i } + 4 a ^ { 2 } ( 1 - e ^ { 2 } ) \cos ^ { 2 } Q _ { i } \sin ^ { 2 } q _ { i } } \\ & { \quad = 4 a ^ { 2 } \sin ^ { 2 } q _ { i } - 4 a ^ { 2 } e ^ { 2 } \cos ^ { 2 } Q _ { i } \sin ^ { 2 } q _ { i } } \\ & { \quad = 4 a ^ { 2 } \sin ^ { 2 } q _ { i } \sin ^ { 2 } p _ { i } , } \end{array}
$$

即

$$
\sigma _ { i } = 2 \mathfrak { a s i n } q _ { i } \mathfrak { s i n } p _ { i } ,
$$

式中 $\pmb { \mathcal { P } _ { 3 } }$ 的象限应根据 $\sigma _ { i } > 0$ 来确定．由上式得

$$
\begin{array} { c } { { r _ { k } + r _ { j } + \sigma _ { i } = a \left( 1 - e \cos { \cal E } _ { k } + 1 - e \cos { \cal E } _ { j } \right) + 2 a \sin { q _ { i } } \sin { p _ { i } } } } \\ { { { } } } \\ { { = 2 a [ 1 - \cos { ( p _ { i } + q _ { i } ) } ] = 4 a \sin ^ { 2 } \displaystyle \frac { e _ { i } } { 2 } , } } \end{array}
$$

$$
r _ { i } + r _ { j } - \sigma _ { i } = 2 a [ 1 - \cos \left( p _ { i } - q _ { i } \right) ] = 4 a \sin ^ { 2 } \frac { \delta _ { i } } { 2 } ,
$$

由此即可给出(3.60)式中 $\pmb { \varepsilon _ { i } }$ 和 $\delta _ { i }$ 的算法．它们的象限可用下述法则确定[2]：若第 $j$ 个和第 $\pmb { k }$ 个观测在同一圈或相隔偶数圈，则$\mathrm { i n } \frac { \varepsilon _ { i } } { 2 } { > } 0 ,$ 否则 $\sin \frac { \frac { \pi } { 3 } } { 2 } < 0 ;$ 若两个观测的向径之间的弧和弦组成

的弓形包含第一个焦点 $\pmb { 0 } _ { 1 }$ （即地心)，则 $\sin { \frac { \delta _ { i } } { 2 } } < 0 ,$ 反之， $\mathrm { s i n } { \frac { \delta _ { i } } { 2 } } \mathrm { > } 0 ;$ 若该弓形包含第二个焦点 $O _ { 2 }$ ，则 $\cos { \frac { \varepsilon _ { i } } { 2 } } < 0 .$ ，否则 $\cos { \frac { \varepsilon _ { i } } { 2 } } { > } 0 ;$ 而恒有 $\cos \frac { \delta _ { i } } { 2 } > 0$ 下面证明有关 $\sin \frac { \frac { \theta _ { i } } { 2 } } { 2 }$ 和 $\cos \frac { \delta _ { i } } { 2 }$ 的结论.

若两个观测在同一圈(相隔偶数圈类似),则

$$
0 { < } E _ { k } { - } E _ { j } { < } 2 \pi ,
$$

即

$$
0 { < } q _ { i } { = } \frac { 1 } { 2 } ( E _ { k } { - } E _ { j } ) { < } \pi ,
$$

因此有

$$
\sin q _ { i } > 0 .
$$

由于

$$
\sigma _ { i } { = } 2 a \sin { q _ { i } } \sin { p _ { i } } { > } 0 ,
$$

要求 $\sin \pmb { p _ { i } } > 0 _ { i }$ 即

$$
0 { < } p _ { i } { < } { \pi } .
$$

根据 $\pmb { \varepsilon }$ 和 $\pmb { \delta }$ 的定义有

$$
0 { < } \frac { 1 } { 2 } { \varepsilon } _ { i } { = } \frac { 1 } { 2 } \ ( p _ { i } + q _ { i } ) { < } \pi ,
$$

$$
- \frac { \pi } { 2 } { < } \frac { 1 } { 2 } \delta _ { i } { = } \frac { 1 } { 2 } ( p _ { i } { - } q _ { i } ) < \frac { \pi } { 2 } ,
$$

故

$$
\sin \frac { \varepsilon _ { i } } { 2 } { > } 0 , \quad \cos \frac { \delta _ { i } } { 2 } { > } 0 .
$$

若两个观测相隔奇数圈(例如一圈)，则

$$
2 \pi { < } E _ { k } { - } E _ { j } { < } { \mathit { 1 } } \pi ,
$$

$$
\pi < q _ { i } = \frac { 1 } { 2 } ( E _ { k } - E _ { j } ) < 2 \pi ,
$$

即

$$
\sin q _ { 1 } < 0 ,
$$

则 $\sin \pmb { p _ { i } } < 0 _ { i }$ 即

$$
\pi < p _ { i } < 2 \pi .
$$

于是有·

$$
\pi < \frac { c _ { i } } { 2 } < 2 \pi , - \frac { \pi } { 2 } < \frac { \delta _ { i } } { 2 } < \frac { \pi } { 2 } ,
$$

故

$$
\sin \frac { \varepsilon _ { i } } { 2 } < 0 , \qquad \cos \frac { \delta _ { i } } { 2 } > 0 .
$$

这就是上述结论.

关于 $\sin \frac { \delta _ { i } } { 2 }$ 和 $\cos \frac { \theta _ { i } } { 2 }$ 的结论，证明过程中要用到 $\sin \frac { \varepsilon _ { i } } { 2 }$ 和$\cos \frac { \delta _ { i } } { 2 }$ 的结论,这里不再讨论下去。但有一点要说明，前面证明过程中， $\pmb { p _ { i } }$ 事实上是作了规定，即在 $( 0 , 2 \pi )$ 内，如果不加这个条件，则 $\sin \frac { \varepsilon _ { i } } { 2 } , \sin \frac { \delta _ { i } } { 2 } , \cos \frac { \varepsilon _ { i } } { 2 } , \cos \frac { \delta _ { i } } { 2 }$ 可以完全反号(注意，是四个一起反号),这对上述结论无影响，因为这四个量无论是在朗伯方程中，还是在迭代过程的改正公式中，都是以两两乘积形式出现的，故无影响.

最后必须指出，上述判别 $\varepsilon _ { i }$ 和 $\delta _ { i }$ 象限的法则，虽然看上去很直观,但在计算机上很难用．不过，既然是用二体问题定轨，弧段就不宜长，那么，我们可以找出一个临界弧段,其对应的时间间隔称为“临界间隔”．所谓临界间隔，即只要两次观测的间隔不超过它， $\sin { \frac { \theta _ { i } } { 2 } } , \quad \sin { \frac { \delta _ { i } } { 2 } } ,$ $\cos \frac { \mathcal { E } _ { i } } { 2 } , \cos \frac { \delta _ { i } } { 2 }$ 全部取正值，否则就可能有象限判别问题.根据上面的判别法则和面积速度公式很容易知道，这个临界间隔与卫星从 $f = - 9 0 ^ { \circ }$ 到 $f = 9 0 ^ { \circ }$ 所飞行的时间 $\Delta t ^ { * }$ 相等.

1   

<table><tr><td rowspan=1 colspan=1>a(km)</td><td rowspan=1 colspan=1>6600</td><td rowspan=1 colspan=1>6700</td><td rowspan=1 colspan=1>6800</td><td rowspan=1 colspan=1>6900</td><td rowspan=1 colspan=1>7000</td><td rowspan=1 colspan=1>7200</td><td rowspan=1 colspan=2>7400</td><td rowspan=1 colspan=1>7600</td><td rowspan=1 colspan=2>7800</td><td rowspan=1 colspan=1>8000</td><td rowspan=1 colspan=1>8200</td><td rowspan=1 colspan=1>8400</td><td rowspan=1 colspan=1>8600</td><td rowspan=1 colspan=1>8800</td><td rowspan=1 colspan=1>9000</td></tr><tr><td rowspan=1 colspan=1>T(min)△t（min）e</td><td rowspan=1 colspan=1>88.94</td><td rowspan=1 colspan=1>90.96</td><td rowspan=1 colspan=1>93.01</td><td rowspan=1 colspan=1>95.07</td><td rowspan=1 colspan=1>97.14</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2>广</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>123.16127.70</td><td rowspan=1 colspan=1>123.16127.70</td><td rowspan=1 colspan=1>132.28</td><td rowspan=1 colspan=1>136.92</td><td rowspan=1 colspan=1>141.62</td></tr><tr><td rowspan=1 colspan=1>0.01</td><td rowspan=1 colspan=1>43.9</td><td rowspan=1 colspan=1>44.9</td><td rowspan=1 colspan=1>45.9</td><td rowspan=1 colspan=1>46.9</td><td rowspan=1 colspan=1>48.0</td><td rowspan=1 colspan=1>50.0</td><td rowspan=1 colspan=2>52.1</td><td rowspan=1 colspan=1>54.2</td><td rowspan=1 colspan=2>56.4</td><td rowspan=1 colspan=1>58.6</td><td rowspan=1 colspan=1>60.8</td><td rowspan=1 colspan=1>63.0</td><td rowspan=1 colspan=1>65.3</td><td rowspan=1 colspan=1>67.6</td><td rowspan=1 colspan=1>69.9</td></tr><tr><td rowspan=1 colspan=1>0.02</td><td rowspan=1 colspan=1>43.3</td><td rowspan=1 colspan=1>44.3</td><td rowspan=1 colspan=1>45.3</td><td rowspan=1 colspan=1>46.3</td><td rowspan=1 colspan=1>47.3</td><td rowspan=1 colspan=1>49.4</td><td></td><td rowspan=1 colspan=1>51.4</td><td rowspan=1 colspan=1>53.5</td><td></td><td rowspan=1 colspan=1>55.7</td><td rowspan=1 colspan=1>57.8</td><td rowspan=1 colspan=1>60.0</td><td rowspan=1 colspan=1>62.2</td><td rowspan=1 colspan=1>64.5</td><td rowspan=1 colspan=1>66.7</td><td rowspan=1 colspan=1>69.0</td></tr><tr><td rowspan=1 colspan=1>0.03</td><td rowspan=1 colspan=1>42.8</td><td rowspan=1 colspan=1>43.7</td><td rowspan=1 colspan=1>44.7</td><td rowspan=1 colspan=1>45.7</td><td rowspan=1 colspan=1>46.7</td><td rowspan=1 colspan=1>48.7</td><td></td><td rowspan=1 colspan=1>50.8</td><td rowspan=1 colspan=1>52.8</td><td></td><td rowspan=1 colspan=1>54.9</td><td rowspan=1 colspan=1>57.1</td><td rowspan=1 colspan=1>59.2</td><td rowspan=1 colspan=1>61.4</td><td rowspan=1 colspan=1>63.6</td><td rowspan=1 colspan=1>65.8</td><td rowspan=1 colspan=1>68.1</td></tr><tr><td rowspan=1 colspan=1>0.04</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>43.2</td><td rowspan=1 colspan=1>44.1</td><td rowspan=1 colspan=1>45.1</td><td rowspan=1 colspan=1>46.1</td><td rowspan=1 colspan=1>48.1</td><td></td><td rowspan=1 colspan=1>50.1</td><td rowspan=1 colspan=1>52.1</td><td></td><td rowspan=1 colspan=1>54.2</td><td rowspan=1 colspan=1>56.3</td><td rowspan=1 colspan=1>58.4</td><td rowspan=1 colspan=1>60.6</td><td rowspan=1 colspan=1>628</td><td rowspan=1 colspan=1>65.0</td><td rowspan=1 colspan=1>67.2</td></tr></table>

<table><tr><td rowspan=1 colspan=1>0.05</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>43.5</td><td rowspan=1 colspan=1>44.5</td><td rowspan=1 colspan=1>45.5</td><td rowspan=1 colspan=1>47.4</td><td rowspan=1 colspan=1>49.4</td><td rowspan=1 colspan=1>51.5</td><td rowspan=1 colspan=1>53.5</td><td rowspan=1 colspan=1>55.6</td><td rowspan=1 colspan=1>57.7</td><td rowspan=1 colspan=1>59.8</td><td rowspan=1 colspan=1>61.9</td><td rowspan=1 colspan=1>64.1</td><td rowspan=1 colspan=1>66.3</td></tr><tr><td rowspan=1 colspan=1>0.06</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>43.0</td><td rowspan=1 colspan=1>43.9</td><td rowspan=1 colspan=1>44.9</td><td rowspan=1 colspan=1>46.8</td><td rowspan=1 colspan=1>48.8</td><td rowspan=1 colspan=1>50.8</td><td rowspan=1 colspan=1>52.8</td><td rowspan=1 colspan=1>54.8</td><td rowspan=1 colspan=1>56.9</td><td rowspan=1 colspan=1>59.0</td><td rowspan=1 colspan=1>61.1</td><td rowspan=1 colspan=1>63.2</td><td rowspan=1 colspan=1>65.4</td></tr><tr><td rowspan=1 colspan=1>0.07</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>43.3</td><td rowspan=1 colspan=1>44.2</td><td rowspan=1 colspan=1>46.2</td><td rowspan=1 colspan=1>48.1</td><td rowspan=1 colspan=1>50.1</td><td rowspan=1 colspan=1>52.0</td><td rowspan=1 colspan=1>54.1</td><td rowspan=1 colspan=1>56.1</td><td rowspan=1 colspan=1>58.2</td><td rowspan=1 colspan=1>60.3</td><td rowspan=1 colspan=1>62.4</td><td rowspan=1 colspan=1>64.5</td></tr><tr><td rowspan=1 colspan=1>0.08</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>43.6</td><td rowspan=1 colspan=1>45.5</td><td rowspan=1 colspan=1>47.4</td><td rowspan=1 colspan=1>49.4</td><td rowspan=1 colspan=1>51.3</td><td rowspan=1 colspan=1>53.3</td><td rowspan=1 colspan=1>55.3</td><td rowspan=1 colspan=1>57.4</td><td rowspan=1 colspan=1>59.4</td><td rowspan=1 colspan=1>61.5</td><td rowspan=1 colspan=1>60.6</td></tr><tr><td rowspan=1 colspan=1>0.09</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>43.0</td><td rowspan=1 colspan=1>44.9</td><td rowspan=1 colspan=1>46.8</td><td rowspan=1 colspan=1>48.7</td><td rowspan=1 colspan=1>50.6</td><td rowspan=1 colspan=1>52.6</td><td rowspan=1 colspan=1>54.5</td><td rowspan=1 colspan=1>56.5</td><td rowspan=1 colspan=1>58.6</td><td rowspan=1 colspan=1>60.6</td><td rowspan=1 colspan=1>62.7</td></tr><tr><td rowspan=1 colspan=1>0.10</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>44.2</td><td rowspan=1 colspan=1>46.1</td><td rowspan=1 colspan=1>48.0</td><td rowspan=1 colspan=1>49.9</td><td rowspan=1 colspan=1>51.8</td><td rowspan=1 colspan=1>53.8</td><td rowspan=1 colspan=1>55.7</td><td rowspan=1 colspan=1>57.7</td><td rowspan=1 colspan=1>59.8</td><td rowspan=1 colspan=1>61.8</td></tr><tr><td rowspan=1 colspan=1>0.12</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>42.9</td><td rowspan=1 colspan=1>44.7</td><td rowspan=1 colspan=1>46.6</td><td rowspan=1 colspan=1>48.4</td><td rowspan=1 colspan=1>50.3</td><td rowspan=1 colspan=1>52.2</td><td rowspan=1 colspan=1>54.1</td><td rowspan=1 colspan=1>56.1</td><td rowspan=1 colspan=1>58.0</td><td rowspan=1 colspan=1>60.0</td></tr><tr><td rowspan=1 colspan=1>0.14</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>43.4</td><td rowspan=1 colspan=1>45.2</td><td rowspan=1 colspan=1>47.0</td><td rowspan=1 colspan=1>48.8</td><td rowspan=1 colspan=1>50.6</td><td rowspan=1 colspan=1>52.5</td><td rowspan=1 colspan=1>54.4</td><td rowspan=1 colspan=1>56.3</td><td rowspan=1 colspan=1>58.2</td></tr><tr><td rowspan=1 colspan=1>0.16</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>43.8</td><td rowspan=1 colspan=1>45.5</td><td rowspan=1 colspan=1>47.3</td><td rowspan=1 colspan=1>49.1</td><td rowspan=1 colspan=1>50.9</td><td rowspan=1 colspan=1>52.7</td><td rowspan=1 colspan=1>54.6</td><td rowspan=1 colspan=1>56.4</td></tr><tr><td rowspan=1 colspan=1>0.18</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>42.4</td><td rowspan=1 colspan=1>44.1</td><td rowspan=1 colspan=1>45.8</td><td rowspan=1 colspan=1>47.5</td><td rowspan=1 colspan=1>49.3</td><td rowspan=1 colspan=1>51.1</td><td rowspan=1 colspan=1>52.9</td><td rowspan=1 colspan=1>54.7</td></tr><tr><td rowspan=1 colspan=1>0.20</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>42.7</td><td rowspan=1 colspan=1>44.3</td><td rowspan=1 colspan=1>46.0</td><td rowspan=1 colspan=1>47.7</td><td rowspan=1 colspan=1>49.4</td><td rowspan=1 colspan=1>51.1</td><td rowspan=1 colspan=1>52.9</td></tr></table>

由开普勒方程可得

$$
\Delta t ^ { * } = \frac { 2 } { n } ( E ^ { * } - e \sin E ^ { * } ) ,
$$

其中 ${ \pmb { { \cal E } } } ^ { * }$ 由下式确定：

$$
\cos E ^ { * } = e , \qquad \sin E ^ { * } = \sqrt { 1 - e ^ { 2 } } .
$$

临界间隔 $\Delta t ^ { * }$ 是 $e$ 的函数,当 $e = 0$ 时有

$$
\Delta t ^ { * } = \frac { \pi } { n } { = } \frac { T } { 2 } ,
$$

$\pmb { T }$ 是卫星运动周期．通常 $\pmb { e }$ 不太大，因此，对于我国人卫观测站的分布来说，同一圈的资料，最大间隔也不会超过临界间隔，这就无需判别 $e _ { 1 }$ 和 $\delta _ { i }$ 的象限.

为了便于读者在实际工作中加以判断，我们对 $\Delta t ^ { * }$ 作了一些计算,现将结果列于表3.1,以供参考.

# \$3.6其它定轨方法

# 1.由观测直接给出向径 $\pmb { r }$ 和速度 $\dot { \pmb { r } }$ 的定轨方法

根据现代观测条件，有可能直接给出 $\pmb { r }$ 或 $\dot { \pmb { r } } .$ 给出 $\pmb { r }$ 的方法大致有下列几种：

(1）雷达或激光测距同时定向,即给出 $\scriptstyle \pmb { \rho } = \pmb { \rho } \hat { \mathbf { L } }$ ，从而得到 $\mathbf { r } _ { \mathbf { \nu } _ { \mathbf { y } } }$

（2）用雷达或激光进行三站同步测距，即由

$$
\rho ^ { ( j ) } = \{ [ x - X ^ { ( j ) } ] ^ { 2 } + [ y - Y ^ { ( j ) } ] ^ { 2 } + [ z - Z ^ { ( j ) } ] ^ { 2 } \} ^ { 1 / 2 } , ( j = 1 , 2 , 3 , 3 )
$$

解出 $\pmb { x } , \pmb { y } , \pmb { z } _ { 3 } ^ { \bullet }$

（3）两站进行同步光学测量,即由

$$
\rho ^ { ( 1 ) } \mathbf { L } ^ { ( 1 ) } + \mathbf { R } ^ { ( 1 ) } = \rho ^ { ( 2 ) } \mathbf { L } ^ { ( 2 ) } + \mathbf { R } ^ { ( 2 ) }
$$

解出 $\rho$ ，从而给出 $\pmb { r }$

至于如何得到 $\dot { \pmb { r } } _ { i }$ 一般需要进行多普勒三站同步测速 $( \beta )$ ，观

测量满足下列方程组：

$$
\left. \begin{array} { l } { { \lambda ^ { ( 1 ) } \dot { x } + \mu ^ { ( 1 ) } \dot { y } + \nu ^ { ( 1 ) } \dot { z } = \pmb { \rho } ^ { ( 1 ) } + { \cal C } ^ { ( 1 ) } , } } \\ { { \lambda ^ { ( 2 ) } \dot { x } + \mu ^ { ( 2 ) } \dot { y } + \nu ^ { ( 2 ) } \dot { z } = \pmb { \rho } ^ { ( 2 ) } + { \cal C } ^ { ( 2 ) } , } } \\ { { \lambda ^ { ( 3 ) } \dot { x } + \mu ^ { ( 3 ) } \dot { y } + \nu ^ { ( 3 ) } \dot { z } = \pmb { \rho } ^ { ( 3 ) } + { \cal C } ^ { ( 3 ) } , } } \end{array} \right\}
$$

其中

$$
c ^ { ( j ) } = \mu ^ { ( j ) } X ^ { ( j ) } - \lambda ^ { ( j ) } Y ^ { ( j ) } .
$$

由线性方程组(3.79)式可解出 $\dot { \pmb x } , \dot { \pmb y } , \dot { \ z } ,$ 即得 $\dot { \pmb { r } } .$

根据上述介绍，直接测出卫星向径 $\pmb { r }$ 比较简单，特别是定初轨要求精度不高，更容易实现．只要得到两次观测时刻 $t _ { 1 }$ 和 $\pmb { \ell _ { 2 } }$ 对应的 $\pmb { r } _ { 1 }$ 和 $\mathbf { r } _ { 2 }$ ，即可定轨．若用一些经典方法，则显得太繁，可直接根据前面3.2中介绍的方法,将 $r _ { \mathrm { 1 } }$ 和 $\pmb { r _ { 2 } }$ 转化成 $\mathbf { r } _ { 1 }$ 和 $\dot { \pmb { r } } _ { 1 }$ ，此时，令$\pmb { t _ { 0 } } = \pmb { t _ { \mathrm { ~ i ~ } } }$ 相应的 $\pmb { \tau _ { 2 } } = \pmb { t _ { 2 } } - \pmb { t _ { 1 } }$ ,由(3.30)式可得

$$
\left. \begin{array} { l } { { r _ { 1 } = r _ { 1 } , } } \\ { { { \displaystyle { \dot { r } } _ { 1 } = { \frac { 1 } { G _ { 2 } } } ( r _ { 2 } - F _ { 2 } r _ { 1 } ) . } } } \end{array} \right\}
$$

有了 $\pmb { r }$ 和 ${ \dot { \pmb { r } } } ,$ 就可立即转换成六个轨道根数（见 $\ S$ 3. 1).

# 2.单站六次测距或测速定轨问题

四种类型的观测值都与轨道根数之间存在函数关系，那么，对于测距和测速资料，能否象光学资料那样，直接定轨，这是人们所关心的问题，为此，这里作一些必要的讨论。

通常把观测值称为观测量，记作 ${ \pmb y }$ (它是 $\pmb { m }$ 维向量， $\pmb { m } = \mathbb { 1 } , 2 ,$ $\cdots )$ ,而待确定的卫星轨道根数被称为状态量，记作 $\pmb { x }$ （在这里，它是六维向量)．这两种量有如下函数关系：

$$
{ \pmb y } = { \pmb H } ( { \pmb x } , t ) ,
$$

$H$ 是 $\pmb { m }$ 维向量函数.如果要由观测量 $\pmb { y }$ 反解状态量 ${ \pmb x } _ { 1 }$ ，就涉及到方程(3.82)是否可解的问题．显然，观测量 $\pmb { y }$ 的维数应满足 $m \geq 6$ ，对于前面所提到的光学观测，至少需要三次，而测距或测速，则至

少需要六次，尽管(3.82)式相当于一超越方程组,无直接解法，但这并不影响我们讨论它的可解性。为了叙述方便，假定 $\pmb { m } = \pmb { 6 }$ ，并将(3.82)式写成下列形式：

$$
\begin{array} { r } { \Phi \left( y , x , t \right) = H ( x , t ) - y = 0 , } \end{array}
$$

$\phi$ 是六维向量函数。相应的雅可比(Jacobi)矩阵为

$$
\mathbf { \delta } B { = } \frac { \partial \phi } { \partial x } { = } \frac { \partial H } { \partial x } .
$$

根据隐函数存在定理,要由(3.83)式解出

$$
{ \pmb x } = { \pmb x } ( { \pmb y } , t ) ,
$$

其充要条件是

$$
| B | \neq 0 ,
$$

$\left| B \right|$ 为矩阵行列式.

对于两种光学资料(方位观测)，即使单站三次观测也能满足条件(3.86)式,实际上已给出上述解,即前面两种定轨方法给出的结果．然而,对于单站(假定地球不转)测距或测速资料,却有

$$
| B | = 0 .
$$

要严格证明结论(3.87)式是相当困难的，但可在计算机上用一不太严格的方法证实这一结论.

首先写出 $\pmb { B }$ 矩阵的形式.为了方便，状态量 $\pmb { x }$ (即轨道根数 $\pmb { \sigma }$ ）的六个分量取为 ${ \mathbf { } } n , e , i , 0 , \omega , M _ { \mathrm { { i } } }$ ，待确定的六个根数对应历元时刻 $\pmb { t _ { 0 } } ,$ 相应的 $\pmb { \sigma }$ 记作 ${ \pmb { \sigma _ { 0 } } }$ 其中 $M ( t _ { 0 } )$ 记作 $M _ { 0 . }$ 除

$$
M ( t ) = M _ { 0 } + n ( t - t _ { 0 } )
$$

外， $\sigma ( t ) = \sigma ( t _ { 0 } ) = \sigma _ { 0 } ,$ 即

$$
\begin{array} { r } { n = n _ { 0 } , e = e _ { 0 } , i = i _ { 0 } , \Omega = \Omega _ { 0 } , \omega = \omega _ { 0 } . } \end{array}
$$

那么,对于六次测距资料,有

$$
\rho { = } H ( \sigma ( \sigma _ { 0 } , t _ { 0 } , t ) , t ) ,
$$

$$
B { = } \frac { { \partial } H } { { \partial } { \sigma } _ { 0 } } { = } \frac { { \partial } \rho } { { \partial } r } \frac { { \partial } r } { { \partial } \sigma } \frac { { \partial } \sigma } { { \partial } { \sigma } _ { 0 } } ,
$$

其中

$$
\begin{array} { r l } & { \frac { \partial \rho } { \partial r } = \left( \frac { \rho } { \rho } \right) ^ { 2 } , } \\ & { \frac { \partial r } { \partial \sigma } = \left( \frac { \partial r } { \partial n } \ \frac { \partial r } { \partial \tilde { \sigma } } \ \frac { \partial r } { \partial \tilde { \sigma } } \ \frac { \partial r } { \partial \tilde { \sigma } } \frac { \partial r } { \partial \tilde { \sigma } } \ \frac { \partial r } { \partial \tilde { \sigma } } \frac { \partial r } { \partial \tilde { \mathcal { M } } } \right) , } \\ & { \frac { \partial \sigma } { \partial \tilde { \sigma } _ { \sigma } } = \left( \begin{array} { l l l l } { 1 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 1 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \end{array} \right) } \\ & { \ell - \ell _ { 0 } \ \mathrm { ~ , ~ } \ 0 , \ 0 \ 0 \ 0 \ 1 , } \end{array}
$$

对于六次测速资料，有

$$
\begin{array} { l } { \displaystyle { \dot { \rho } = H ( \sigma ( \sigma _ { 0 } , t _ { 0 } , t ) , t ) , } } \\ { \displaystyle { B = \frac { \partial H } { \partial \sigma _ { 0 } } = \Bigl ( \frac { \partial \dot { \rho } } { \partial r } \frac { \partial r } { \partial \sigma } + \frac { \partial \dot { \rho } } { \partial \dot { r } } \frac { \partial \dot { r } } { \partial \sigma } \Bigr ) \frac { \partial \sigma } { \partial \sigma _ { 0 } } } , } \end{array}
$$

其中

$$
\left. \begin{array} { l } { \displaystyle \frac { \partial \beta } { \partial \boldsymbol { r } } = \left( \frac { 1 } { \rho } \dot { \boldsymbol { r } } - \frac { \partial } { \rho ^ { 2 } } \boldsymbol { \rho } \right) ^ { \boldsymbol { r } } , } \\ { \displaystyle \frac { \partial \beta } { \partial \dot { \boldsymbol { r } } } = \left( \frac { \rho } { \rho } \right) ^ { \boldsymbol { r } } , } \\ { \displaystyle \frac { \partial \dot { \boldsymbol { r } } } { \partial \sigma } = \left( \frac { \partial \dot { \boldsymbol { r } } } { \partial \boldsymbol { n } } \frac { \partial \dot { \boldsymbol { r } } } { \partial \varrho } \frac { \partial \dot { \boldsymbol { r } } } { \partial i } \frac { \partial \dot { \boldsymbol { r } } } { \partial \varOmega } \frac { \partial \dot { \boldsymbol { r } } } { \partial \omega } \frac { \partial \dot { \boldsymbol { r } } } { \partial \mathcal { M } } \right) . } \end{array} \right\}
$$

关于 $\partial r / \partial \sigma$ 和 $\partial \ r _ { r } / \partial \sigma$ 的六个元素不再列出，其具体形式可见最后一章的有关内容。

$| B |$ 的各元素所涉及的量均满足椭圆运动关系．具体计算时，我们可以给定一组根数，并算出相应的坐标和速度，代入上述各式,只要所给根数及其有关量不具有任何几何上的特殊性即可.文[4]曾对单站六次测距和测速资料作过计算,结果证实确有

$$
| B | = 0 .
$$

这说明:单站六次(或更多次)测距和测速资料是不能定轨的..

上面的结论是在假定地球不转，观测站为一固定点时得到的，但在观测弧段不长的情况下，地球自转的反映不明显，单站测距和测速资料会有 $| B | \approx 0$ 的结果，这样还是难以定轨．因此，对于这两种资料，只有长弧段或多站才行．然而，定初轨无需这么复杂，尽可能采用简单方法为宜.

# 3.牛顿-拉夫森(Newton-Raphson)方法

一种将常微初值问题化为边值问题，由边值条件(观测值)来确定初值(待定根数)的方法，叫做牛顿-拉夫森方法．但它与最后一章介绍的微分轨道改进方法不一样，所涉及的偏导数并不复杂.详见文[5一7],这里简单介绍一下迭代中用到的基本方程.

卫星运动方程为

$$
\pmb { \dot { x } } = \pmb { F } ( \pmb { x } , \pmb { t } ) ,
$$

这里六维状态向量 $\pmb { x }$ 的形式为

$$
\pmb { x } = ( x y z \pmb { \dot { x } } \pmb { \dot { y } } \pmb { \dot { z } } ) ^ { T } ,
$$

右函数下亦是六维向量函数，但它可以包含摄动力部分，解此方程是用迭代法，迭代第 $j$ 次 $( j = 1 , 2 , \cdots )$ 时有

$$
\dot { x } ^ { ( j ) } = F ( x ^ { ( j - 1 ) } , t ) + B [ x ^ { ( j ) } - x ^ { ( j - 1 ) } ] ,
$$

$$
B { = } \bigg ( \frac { \partial F } { \partial x } \bigg ) _ { x = x } ( \ j { - } 1 ) ,
$$

方程(3.98)可写成下列一阶线性常微方程组：

$$
\left. \begin{array} { l } { \dot { x } ^ { ( j ) } = B x ^ { ( j ) } + D } \\ { D = F ( x ^ { ( j - 1 ) } , t ) - B x ^ { ( j - 1 ) } } \end{array} \right\}
$$

方程(3.96)和(3.100)就是牛顿-拉夫森方法的基本方程．这里的$\pmb { { \cal B } }$ 矩阵仅仅涉及运动方程的右函数对状态量的偏导数，如果是二体问题，确实比较简单，但是，迭代过程中不象轨道改进那样求线性代数方程的解，而是求线性常微分方程的解，从这一角度来看比较复杂.因此,牛顿-拉夫森方法在定轨工作中并未得到广泛应用.

# 4.一些近似处理

如果观测资料少(例如一圈只有两个光学资料)，而精度要求又不高,那么可以简化轨道计算,这里提供几种途径。

(1）固定 $\pmb { a }$ 和 $\textbf { \textit { i } }$ 的巴日诺夫方法 $\pmb { a }$ 和 $\textbf { \textit { i } }$ 一般是可以知道其近似值的，作为两个已知根数，用两次观测首先确定 $\varOmega$ ，基本上与已知 $\pmb { a }$ 值的巴日诺夫方法相同，相应的改正公式(3.62)式变为

$$
\Delta = \biggl [ - \frac { \partial F } { \partial g } ( - \hbar ) - \frac { \partial F } { \partial h } ( g ) \biggr ] \Delta \varOmega
$$

整个计算过程不再重复。

（2）圆轨道近似 若轨道偏心率 $e$ 较小，则可用圆轨道作近似，此时只要在几何条件和力学条件中考虑圆运动的特征即可，问题很简单，读者可自己写出相应的公式.

（3）带有轨道改进性质的近似定轨法 在知道某些根数(较好的近似值)后,可以固定下来，用类似于轨道改进的方法（见最后一章)去求另几个根数.

关于初轨的确定,还有一些针对具体情况的处理方法，除前面引出的文献外，还可参看文[8]和[9],以及国内有关部门的类似工作．但作为一本教材，仍以介绍基本原理为主，因此就不再一一列举.

# 参考文献

[1] Escobal, P.R.,Methods of Orbit Determination,New York, 1965.

[2] Plummer,H.C.,An Introductory Treatise on Dynamical

Astronomy, Cambridge at the University Press, 1918.

[3]BaxKeH0B,r.M.,E1OJJI. NTA,7(1960),757-765.

[4]刘林,飞行器测控技术,1985,No.3,6-12.

[5]Long,R.S.,AIAA Journal,3(1965)，1937-1940.  
[6] Pitkin,E. T. and Carpenter,G.C.,Celest. Mech. 1(1969),72-90.  
[7]刘林，人造地球卫星运动理论,科学出版社，1974.  
[8]Taff,L.G.,Astr0n. J.,89(1984),1426-1428.  
[9] Morton,B.G.and Taff,L.G.,Celest. Mech.39(l986)，181--190.

# 第四章 摄动运动方程及其解法轮廓

前面两章所讨论的二体问题只是人造卫星绕地球运动的一种近似，从这一章开始将要仔细研究人造卫星在各种力学因素作用下的运动规律．为了便于讨论，暂取历元地心惯性系作为讨论问题的参考系．在此参考系中，人造卫星绕地球运动的微分方程可写成下列形式：

$$
\therefore \tilde { \boldsymbol { r } } = \boldsymbol { F } ( \boldsymbol { r } , \dot { \boldsymbol { r } } , t ) .
$$

这里，右函数 $\pmb { F }$ （尽管少一个质量因子，我们还是经常习惯地称它为作用力)极其复杂，若要获得运动方程(4.1)式的解，就必须对 $\pmb { F }$ 作一些必要的分析和简化，给出合理的动力模型，每种力学因素的数学模型将要在后面各章中逐一介绍，这一章先引用某些结论，以说明人造卫星绕地球运行过程中的受力情况，从而让读者了解方程(4.1)的基本类型，以及求解这类方程的基本知识.

# 4.1 人造地球卫星运动的受力分析

# 1.地球引力与形状摄动

如果地球作为一个刚体，而且赤道面与历元地心惯性系的基本平面重合，那么其引力位函数展开式在地心球坐标系 $( r , \lambda , \varphi )$ 中可写成下列形式(详细推导见第五章S5.1):

$$
V = V _ { 0 } + \Delta V ,
$$

$$
V _ { \ L _ { 0 } } = \frac { \ L _ { 1 } } { r } ,
$$

$$
\Delta V = - \sum _ { n \geqslant 2 } \frac { J _ { n } } { r ^ { n + 1 } } P _ { n } ( \sin \varphi ) - \sum _ { n \geqslant 2 } \sum _ { m = 1 } ^ { n } \frac { J _ { n \geqslant m } } { r ^ { n + 1 } } P _ { n } ^ { m } ( \sin \varphi ) \cos { m \bar { \lambda } } ,
$$

$$
\stackrel {  } { \lambda } = \lambda - \lambda _ { n } , \stackrel { \cdot } { m } , \lambda _ { n } , _ { m } = \mathrm { c o n s t . }
$$

其中λ,φ为地心经、纬度，Pn(sin)和P(sinφ)分别为勒让德(Legendre)和缔合勒让德多项式．V。是地球引力位的主要部分，相当于均匀密度球体的引力位，或质量全部集中在地心的质点引力位．△V是真实地球引力位对均匀球体的修正部分，包括带谐(Zonal harmonic)和田谐(Tesseral harmonic)两大项,它们反映了地球的不均匀性(包括形状不规则和密度分布的不均匀)．相应的 $\pmb { J _ { n } }$ 和 $J _ { n \sin }$ 即带谐项系数和田谐项系数，它们的大小则反映出上述不均匀性的程度。其中 $J _ { 2 } { = } O ( 1 0 ^ { - 3 } )$ ，相应的项又称为扁率项，其它 $J _ { \mathscr { n } }$ 和 $J _ { n \cdot m }$ 的量级几乎都不大于 $1 0 ^ { - 8 }$ ，因此，人造卫星在地球引力场中的运动方程又可写成下列形式：

$$
\ddot { r } { = } F _ { 0 } { + } F _ { \varepsilon } ,
$$

其中

$$
\begin{array} { l } { { { \cal F } _ { \mathrm { 0 } } = \mathrm { g r a d } V _ { \mathrm { 0 } } = - { \frac { 1 } { r ^ { 2 } } } \Bigl ( { \frac { r } { r } } \Bigr ) , } } \\ { { { \cal F } _ { \varepsilon } = \mathrm { g r a d } \left( \Lambda V \right) , } } \end{array}
$$

且有

$$
\mid F _ { \varepsilon } \mid / \mid F _ { 0 } \mid = O ( \varepsilon ) , \varepsilon = O ( J _ { 2 } ) .
$$

方程(4.6)的主要部分对应二体问题,即

$$
\ddot { r } = F _ { 0 } .
$$

它是可积的(请看第二章)，而 $\pmb { F }$ 相对 $\pmb { F } _ { 0 }$ 是一小扰动，称为摄动部分，按照(4.6)式的写法，即把一个复杂的实际运动分解为简单可积的二体问题加上摄动“改正”两个部分，通常称这类问题为有摄(或受摄)二体问题．这里由地球不均匀性引起的摄动，常被简

称为地球形状摄动。

除地球引力外，人造卫星在运动过程中所涉及到的其它各种力学因素，相对而言，都是比较小的，甚至比 $\pmb { J _ { 2 } }$ 项的影响小得多，因此，都是摄动项，即仅仅给上述 $\pmb { F }$ ，部分增加一些新内容.

# 2.地球形变摄动

由于日、月引力作用以及地球自转的不均匀性(包括自转轴在休内的移动一一极移)，将导致地球的弹性形变，前者就是潮现象，有固体潮、海潮和大气潮，这相当于原摄动项 $\pmb { J } _ { n }$ 和 $J _ { n : m }$ 有一种附加变化，从而对人造卫星运动产生一种附加摄动，或称潮汐摄动和地球自转形变摄动.

# 3．大气阻力与类阻力摄动

人造卫星(特别是近地卫星)在大气层中飞行，将受大气阻力的影响，阻力加速度可写成下列形式：

$$
D = - \frac { 1 } { 2 } \bigg ( \frac { C _ { D } S } { m } \bigg ) \rho v ^ { 2 } \bigg ( \frac { v } { v } \bigg ) .
$$

其中 $\mathfrak { C }$ 是卫星相对大气的飞行速度， $\pmb { v }$ 是其大小， $\pmb { \rho }$ 是大气密度，$\delta / m$ 是卫星对阻力而言的有效面积质量比(以后简称面质比）， $C _ { D }$ 是阻力系数．另外，还有电离气体的磁阻力等不太清楚的力学因素，我们统称它们为“类阻力”，且可并人上述阻力项中，只要将阻力系数 $C _ { D }$ 作适当的处理即可．对于绝大多数卫星而言，它们的有效截面积 $\pmb { \mathcal { S } }$ 不是太大，而飞行高度又不太低(通常是离地面200km以上), $\pmb { D }$ 相对前面的主项 $\pmb { F } _ { 0 }$ 是很小的，即 $\pmb { { \cal D } } \ b { = } \pmb { { \cal F } } .$ ，是一种阻力摄动.

# 4.日、月引力摄动

人造卫星在地球附近运动时，日、月(作为质点)引力是一种典型的第三体摄动力，相应的摄动加速度为

$$
\left. \begin{array} { l } { { \displaystyle F _ { \varepsilon } = \sum _ { j = 1 } ^ { 2 } ( - m _ { j } ) \left( \frac { R _ { j } } { | R _ { j } | ^ { 3 } } + \frac { \Delta _ { j } } { | \Delta _ { j } | ^ { 3 } } \right) } , } \\ { { \displaystyle \vphantom { \sum _ { j = 1 } ^ { 2 } ( - m _ { j } ) ( - m _ { j } ) } \sum _ { j = 1 } ^ { 2 } ( - 1 , 2 ) . } } \end{array} \right\}
$$

其中 $\pmb { r }$ 和 $\mathbf { R } _ { j }$ 各为人造卫星和日、月的地心向径， $\mathbf { R } _ { s }$ 是时间 $\pmb { \mathscr { t } }$ 的已知函数,由日、地、月三体系统确定，与人造卫星运动无关.

# 5.地球扁率的间接摄动

事实上，前面已说过，地球并非质点，如果看成扁球体，它与日、月之间的相互作用要增加两项：一是力矩作用引起的赤道面摆动，此即岁差章动现象，这是在前面选取的惯性参考系中计算地球引力位时要考虑的影响；另一项就是日、月与地球扁率部分的相互作用引起的平动加速度,对原参考系而言应增加一惯性力，此即地球扁率的间接摄动，其表达形式与地球形状摄动中的扁率项很类似.

# 6．月球扁率摄动

月球也并非质点,它的扁率还是较大的，量级为 $1 0 ^ { - 4 }$ ，这部分对地球(作为质点)和人造卫星的运动都有影响．当然，它比月球引力作用小得多，是一种摄动，即月球扁率摄动，或称月球形状摄动．

# 7．太阳辐射压摄动

直接作用在人造卫星表面的太阳辐射压(或简称光压)，虽然并不大，但同样要影响卫星的运动，也是一种摄动源，相应的摄动加速度为

$$
F _ { e } = \gamma \Big ( \frac { C _ { r } S } { m } \Big ) \rho _ { \odot } \frac { a _ { \psi } ^ { 2 } } { \Delta ^ { 2 } } \Big ( \frac { \Delta } { \Delta } \Big ) .
$$

其中 $p _ { \odot }$ 是作用在离太阳一个天文单位 ${ \pmb { a } } _ { \pmb { u } }$ 处的太阳辐射压强， $C _ { r }$ 是卫星表面的反射系数 ${ \mathcal { S } } / m$ 是卫星对辐射压而言的有效面质比，$\pmb { \Delta }$ 是太阳到卫星的矢径。 $\gamma$ 是地影因子，由下式定义：

$$
\gamma { = } 1 { \ - } \Delta \mathcal { S } / \mathcal { S } _ { \odot } .
$$

这里 $\pmb { S } _ { \odot }$ 是太阳视面积， $\Delta \theta$ 是被“蚀”部分,这涉及到地影问题.当$\Delta \pmb { S } = \pmb { S } _ { \odot }$ 时， $\gamma = 0 _ { \mathrm { i } }$ ，此时对应卫星进入真正的地影.

# 8．地球反照辐射压摄动

地球受太阳直接辐射后，其本身会产生次辐射，这有两类：一类是光学辐射,亦称反照率辐射，另一类是红外辐射，又称发射率辐射，尽管这两类性质不同的次辐射能量要比直接辐射小，但它们对卫星运动也同样构成一种摄动作用，其数学模型与上述光压摄动类似，称为地球反照辐射压摄动。

# 9．小推力摄动

有些卫星入轨后，需要不断调节姿态和修正轨道，常在某一段时间内点火喷气，产生一种小推力，对卫星运动的影响即小推力摄动.

# 10．广义相对论效应

考虑广义相对论效应，地心惯性系只是一个局部惯性参考系。在此参考系中，卫星运动方程不同于牛顿引力场中的形式，其差别就相当于人造卫星运动受到一个附加摄动，此即后牛顿效应，它来源于地球引力场。相应的摄动加速度为

$$
F _ { \varepsilon } = \frac { 1 } { r ^ { 2 } } \biggl [ \biggl ( \frac { 4 } { c ^ { 2 } r } - \frac { \dot { r } ^ { 2 } } { c ^ { 2 } } \biggr ) \frac { r } { r } + \frac { 4 } { c ^ { 2 } } ( r \cdot \dot { r } ) \ \frac { \dot { r } } { r } \biggr ]
$$

其中 $\pmb { \mathscr { c } }$ 为光速.

综上所述，人造卫星运动的基本方程(1)可以写成(4.6)式的形式：

$$
\ddot { r } { = } F _ { 0 } { + } F _ { \cdots }
$$

而 $\pmb { F } .$ 的形式为

$$
F _ { \varepsilon } = \sum _ { k = 1 } ^ { n } F _ { k } ( r , \dot { r } , t ; e ^ { k } ) ,
$$

$$
\mid F _ { k } \mid / \mid F _ { 0 } \mid = \dot { O } ( g ^ { k } ) , \dot { \varepsilon } = O ( J _ { 2 } ) .
$$

这是一个有摄二体问题的数学模型．根据上述分析， $\pmb { F _ { \ell } }$ 不仅包含各阶 $( \varepsilon ^ { k } , k { = } 1 , 2 , \cdots , n )$ 摄动力，面且摄动力的形式是多样的，有保守力与耗散力，有仅与 $\pmb { r }$ 有关的或同时与 $\pmb { r }$ 和 $\dot { \pmb { r } }$ 有关的，也有显含 $\pmb { \mathrm { \acute { \varepsilon } } }$ 的，甚至还有不连续的，形式极其复杂，除单独考虑后牛顿效应时，相应的方程(4.15)可积(见第十二章)外，考虑其他摄动效应时，目前还无法给出严格解，因此，对于有摄二体问题(4.15)式，通常是先给出二体问题的解一一椭圆运动，并以此作为基本解，考虑摄动影响后研究它的变化(称为摄动变化)．当然，在具体工作中，也可直接求方程(4.15)的数值解.

卫星在发射段和回收段中，所受到的火箭推力和大气阻力与地球引力 $\pmb { F _ { 0 } }$ 之比并不是小量，不能处理成有摄二体问题,其数学模型与上面讨论的卫星进入轨道后的运动截然不同，必须处理成一般飞行力学问题.

# 4.2 常数变易法一—摄动运动方程的建立

# 1.基本原理

首先考虑无摄运动问题(即二体问题),这时 $F _ { \bullet } = 0$ ，相应的方程(4.15)变为

$$
{ \ddot { r } } = F _ { 0 } = - { \frac { 1 } { r ^ { 2 } } } { \left( { \frac { r } { r } } \right) } .
$$

第二章已给出该问题的解：

$$
\left. \begin{array} { l } { r = f ( C _ { 1 } , C _ { 2 } , \cdots , C _ { 6 } , t ) , } \\ { \dot { r } = g ( C _ { 1 } , C _ { 2 } , \cdots , C _ { 6 } , t ) . } \end{array} \right\}
$$

其中 $\scriptstyle { \dot { \pmb { r } } } = \partial { \pmb { f } } / \partial t$ 。对于人造地球卫星而言，此解描述一椭圆运动.六个积分常数 $c _ { 1 } , c _ { 2 } , \ldots , c _ { 6 }$ 即轨道根数，依次排列为 $a , e , i , \Omega ,$ $\omega _ { s } \tau _ { s }$ ，回到原方程(4.15)， $\pmb { F } _ { \bullet } \pmb { \div } 0 _$ ，解(4.19)式当然不能满足它.所谓常数变易法，即要使无摄运动的解一—椭圆运动公式(4.19)满足方程(4.15)．显然， $\sigma _ { 1 } , \sigma _ { 2 } , \cdots , \sigma _ { 6 }$ 不再是常数，应变成时间 $\pmb { \ell }$ 的函数，那么接下去就要导出这些积分常数(或轨道根数)的变化所满足的微分方程一一摄动运动方程。

(4.19)式第一式对 $\pmb { t }$ 求导得

$$
\frac { d r } { d t } { = } \frac { \partial f } { \partial t } { + } \sum _ { j { = 1 } } ^ { 8 } \frac { \partial f } { \partial C _ { j } } \frac { d C _ { j } } { d t } .
$$

由于要求(4.19)式第二式亦满足受摄运动方程,所以应有

$$
\frac { d r } { d t } { = } \frac { { \partial } f } { { \partial } t } { = } g ( C _ { 1 } , C _ { 2 } , \cdots , C _ { . 6 } , t ) .
$$

此式再对 $\pmb { t }$ 求一次导数，并让其满足受摄运动方程(4.15),即

$$
\frac { d ^ { 2 } r } { d t ^ { 2 } } { = } \frac { \partial g } { \partial t } { + } \sum _ { j = 1 } ^ { 6 } \frac { \partial g } { \partial C _ { j } } \frac { d C _ { j } } { d t } { = } F _ { 0 } { + } F _ { s } ,
$$

而在该式中有

$$
\frac { \partial g } { \partial t } { = } F _ { 0 } .
$$

由此可知，常数变易的两个条件应为

$$
\left. \begin{array} { l } { { \displaystyle { \sum _ { j = 1 } ^ { 6 } } \frac { \partial f } { \partial { \cal C } _ { j } } \frac { d { \cal C } _ { j } } { d t } } { = 0 } , } \\ { { \displaystyle { \sum _ { j = 1 } ^ { 6 } } \frac { \partial g } { \partial { \cal C } _ { j } } \frac { d { \cal C } _ { j } } { d t } { = { \cal F } _ { \ast } } } } \end{array} \right\} .
$$

其中 $\Pi _ { \overline { { \partial C _ { j } } } } ^ { \frac { \partial f } { \hbar } } \hat { \mathcal { F } } \Pi _ { \overline { { \partial C _ { j } } } } ^ { \frac { \partial g } { \partial g } ; }$ 都是 $c _ { s }$ 和 $\pmb { \ell }$ 的已知函数，因此共有六个“未知量”$d C _ { j } / d t$ ，与方程个数相同。对于具体应用，需要由该方程组给出$d C _ { j } / d t$ 的显形式。至于如何给出,暂放一下,先来看看上述常数变易法的实际意义．显然,经上述处理，就是把受摄运动看成一个变化的椭圆运动，无摄运动中的椭圆关系式(4.19)仍然成立,只是相应的六个不变根数 $c _ { j }$ 变为 $\smash { C _ { j } ( t ) }$ ，即瞬时根数，亦称吻切根数。

关于由线性方程组(4.24)给出 $d C _ { j } / d t$ 的显形式问题，不再重复许多天体力学书中常用的推导方法，这里将介绍另一种比较简单的以轨道根数作为基本变量的直接推导方法[1],[2],它无需假定摄动力是保守力,可普遍适用.

# 2.摄动运动方程的直接推导

原理未变，但不是直接引用椭圆关系式(4.19),而是引用它们的原始形式，即二体问题的六个积分：

$$
\begin{array} { r } { \mathsf { s i n } i \sin \varOmega } \\ { \pmb { r } \times \dot { \pmb { r } } = h \hat { R } \sqrt { \mu a ( 1 - e ^ { 2 } ) } \left( - \mathsf { s i n } i \cos \varOmega \right) , } \\ { \mathsf { c o s } i \qquad } \end{array}
$$

$$
v ^ { 2 } = \dot { r } ^ { 2 } = \mu \Bigl ( \frac { 2 } { r } - \frac { 1 } { a } \Bigr ) ,
$$

$$
r { = } \frac { a \left( 1 - e ^ { 2 } \right) } { 1 + e \cos f } \mathop { = } \frac { a \left( 1 - e \cos E \right) } { 1 + e \cos E } ,
$$

$$
\scriptstyle { M = E - e \sin E . }
$$

这里同时引用轨道积分(4.27)和活力公式(4.26)，仍算作两个独立积分．因此，(4.25)—(4.28)式一共是六个关系式，可用来导出六个积分常数(可变根数)变化的微分方程．同样，让它们满足受摄运动方程(4.15)，而原不变根数变为时间 $\pmb { t }$ 的函数．公式中暂时保留了地球引力常数 $\mu$ ，推出摄动运动方程后再回到标准计算单位系统,即 $\mu = 1$ .

为了下面推导的需要，现将 $\pmb { r }$ 和 $\dot { \pmb { r } }$ 在空间极坐标系 $( r , \theta , z )$ 和地心赤道直角坐标系 $( x , y , z )$ 中的形式分别列出，即

$$
\begin{array} { l } { r { = } r { \hat { r } } } \\ { { } } \\ { { = } x { \hat { i } } { + } y { \hat { j } } { + } z { \hat { k } } , } \\ { { } } \\ { { \dot { r } } { = } { \dot { r } } { \hat { r } } { + } r { \dot { \theta } } { \hat { \theta } } } \end{array}
$$

$$
= \dot { x } \hat { i } + \dot { y } \hat { j } + \dot { z } \hat { k } ,
$$

$$
\mathbf { \boldsymbol { r } } \times { \dot { \mathbf { r } } } = r ^ { 2 } { \dot { \theta } } \mathbf { \hat { R } }
$$

$$
= ( y { \dot { z } } - z { \dot { y } } ) { \hat { i } } + ( z { \dot { x } } - x { \dot { z } } ) { \hat { j } } + ( x { \dot { y } } - y { \dot { x } } ) { \hat { k } } .
$$

其中 ${ \hat { r } } , { \hat { \theta } } , { \hat { R } }$ 为径向,横向和轨道面法向单位向量， $i , j , k$ 为直角坐标三方向的单位向量，摄动力 (加速度) ${ \pmb F } _ { 1 }$ ，在上述两坐标系中的三个分量分别记作

$$
S , T , W \mathrm { \# H } F _ { x } , F _ { y } , F _ { z } .
$$

将常数变易的原理用于上述六个积分(4.25)一(4.28)．设

$$
\varphi ( C _ { 1 } , C _ { 2 } , \cdots , C _ { 6 } , t ) = \psi \left( r , { \dot { r } } \right)
$$

为无摄运动(4.18)式的任一积分，对于无摄运动有

$$
{ \frac { d \varphi } { d t } } = { \frac { \partial \varphi } { \partial t } } = { \frac { \partial \psi } { \partial r } } { \dot { r } } + { \frac { \partial \psi } { \partial r } } { \ddot { r } }
$$

即

$$
\frac { \partial \varphi } { \partial t } = \frac { \partial \psi } { \partial r } \dot { r } + \frac { \partial \psi } { \partial \dot { r } } F _ { 0 } .
$$

而对受摄运动却变为

$$
\begin{array} { r l r } { \frac { d \varphi } { d t } { = } \frac { \partial \varphi } { \partial t } { + } \displaystyle \sum _ { j } \frac { \partial \varphi } { \partial { \dot { C } } _ { j } } { \dot { C } } _ { j } { = } \frac { \partial \psi } { \partial r } { \dot { r } } { + } \frac { \partial \psi } { \partial { \dot { r } } } { \ddot { r } } } & { } & \\ { { = } \frac { \partial \psi } { \partial r } { \dot { r } } { + } \frac { \partial \psi } { \partial { \dot { r } } } ( F _ { 0 } { \cdot } F _ { \iota } ) , } & { } & \end{array}
$$

按常数变易的要求，其中 $\pmb { r }$ 和 $\dot { \pmb { r } }$ 仍满足椭圆运动关系，那么根据(4.33)式立即可得

$$
\sum _ { j } { \frac { \partial \varphi } { \partial C _ { j } } } \dot { C } _ { j } = { \frac { \partial \psi } { \partial { \dot { r } } } } F _ { \varepsilon } .
$$

实际上，这就是条件(4.24)式的一般情况，当 $\psi = x , y , z$ 和$\psi = { \dot { x } } , { \dot { y } } , { \dot { z } }$ 时,条件(4.34)式即退化为(4.24)式.

为了避免“混乱”，我们引用 $a , e , i , \Omega , \omega , M$ 六个根数作为独立变量．事实上，无论是理论研究还是具体应用问题，都没有必要引用过近地点时刻 $\pmb { \tau }$ 或常用的 $M _ { 0 } = - n \pmb { \tau } _ { \ast }$ ，真正有用的是时间根数$M = n \left( \ell - \tau \right)$ ，或另两个近点角 $f$ 和 $\pmb { { \cal E } }$ ，而采用平近点角 $\pmb { M }$ 比较方便．引用 $M$ 代替 $\pmb { \tau }$ 作为独立变量后，在求某些函数对 $\pmb { a }$ 的偏导数时，不再有显含 $\pmb { a }$ 和隐含 $\pmb { a }$ 的问题．上述六个积分中的前四个，即(4.25)一(4.26)式，可以写成形如(4.32)式的简单形式：

$$
\varphi ( a , e , i , \varOmega ) = \psi ( r , \dot { r } ) .
$$

相应的条件(4.34)式为

$$
{ \begin{array} { r l } & { { \frac { \partial \varphi } { \partial a } } { \frac { d a } { d t } } + { \frac { \partial \varphi } { \partial { \boldsymbol { \dot { e } } } } } { \frac { d { \boldsymbol { e } } } { d t } } + { \frac { \partial \varphi } { \partial { \dot { i } } } } { \frac { d { \dot { i } } } { d t } } + { \frac { \partial \varphi } { \partial \Omega } } { \frac { d \Omega } { d t } } } \\ & { \qquad = { \frac { \partial \psi } { \partial { \dot { r } } } } S + { \frac { 1 } { r } } { \frac { \partial \psi } { \partial { \dot { \theta } } } } T } \\ & { \qquad = { \frac { \partial \psi } { \partial { \dot { x } } } } F _ { x } + { \frac { \partial \psi } { \partial { \dot { y } } } } F _ { y } + { \frac { \partial \psi } { \partial { \dot { z } } } } F _ { \dot { z } } . } \end{array} }
$$

这可用来推导 $d a / d t , d e / d t , d i / d t$ 和 $d \Omega / d t$ ，此即文献[1],[2]中介绍的方法，关于另两个方程，虽然 $\pmb { M }$ 或 $f , \mathbf { \nabla } \overline { { \mathbf { g } } }$ 可以代替 $\pmb { \tau }$ 作为独立变量，但它们都不能看成积分常数，因此对后两个积分（4.27）式和(4.28)式不便引用条件(4.34)式，但仍可用来直接推导 $d \omega /$ $d t$ 和 $d M / d t$ ．推导中将要用到 $f$ ，这可由面积积分将它与 $\dot { \omega } , \dot { \Omega }$ 联系起来．对于无摄运动有

$$
\left. \begin{array} { l } { { \dot { \theta } = \dot { f } , } } \\ { { r ^ { 2 } \dot { \theta } = r ^ { 2 } \dot { f } = h , } } \\ { { h = \sqrt { \mu p } = \sqrt { \mu a ( 1 - e ^ { 2 } ) . } } } \end{array} \right\} ~ .
$$

而对于受摄运动却有

$$
\Dot { \theta } = \Dot { f } + \Dot { \omega } + \Dot { \Omega } \cos \Dot { \imath } ,
$$

$$
r ^ { 2 } \dot { \theta } = r ^ { 2 } ( \dot { f } + \dot { \omega } + \dot { Q } \cos \dot { t } ) = h ( t ) ,
$$

即

$$
r ^ { 2 } \dot { f } = h ( t ) - r ^ { 2 } ( \dot { \omega } + \dot { \Omega } \cos i ) .
$$

现在根据上述原理具体推导摄动运动方程．首先将积分（4.26)式写成(4.35)式的形式：

$$
\frac { \mu } { a } { = } \frac { 2 \mu } { r } { - } ( \dot { r } ^ { 2 } + r ^ { 2 } \dot { \theta } ^ { 2 } ) ,
$$

根据(4.36)式得

$$
- \frac { \mu } { a ^ { 2 } } \frac { d a } { d t } { = } - 2 \dot { r } S - 2 r \dot { \theta } T ,
$$

其中

$$
\left. \begin{array} { c } { { \dot { r } = \dot { r } \cdot \hat { r } = \sqrt { \frac { \mu } { p } } e \sin f , } } \\ { { } } \\ { { r \dot { \theta } = \frac { 1 } { r } \sqrt { \mu p } . } } \end{array} \right\}
$$

代人上式整理后得

$$
 \frac { d a } { d t } { = } \frac { 2 } { \pi \sqrt { 1 - e ^ { 2 } } } [ S e \sin f { + } T ( 1 + e \cos f ) ] .
$$

接着利用积分(4.25)式在轨道面法向和 $x , y$ 方向上的分量来推导 $\mathrm { d } e / \mathrm { d } t , d i / d t$ 和 $d \Omega / d t$ ，相应的形式为

$$
h = r ^ { 2 } \theta ,
$$

$$
\hbar \sin i \sin \Omega = y \dot { z } - z \dot { y } ,
$$

$$
- h \sin i \cos \varOmega = z \dot { x } - x \dot { z } .
$$

由(4.35)式得

$$
\frac { d h } { d t } { = } r T ,
$$

$$
r T \sin i \sin \Omega + h \cos i \sin \Omega { \frac { d i } { d t } } + h \sin i \cos \Omega { \frac { d \Omega } { d t } } -
$$

$$
\begin{array} { r l } { \cdot } & { { } = y { \cal F } _ { z } { - z { \cal F } _ { y } } { = ( \pmb { r } \times { \cal F } _ { z } ) _ { z } } , } \end{array}
$$

$$
\begin{array} { c } { { - r T \sin i \cos \varOmega - h \cos i \cos \varOmega \displaystyle \frac { d i } { d t } + h \sin i \sin \varOmega \displaystyle \frac { d \varOmega } { d t } } } \\ { { = z F _ { x } - x F _ { z } = ( { \pmb r } \times { \cal F } _ { * } ) _ { y } , } } \end{array}
$$

由 $h { = } \sqrt { \mu p } = \sqrt { \mu a ( 1 { - } e ^ { 2 } ) }$ ，(4.44)式可以写成

$$
 \frac { d h } { d t } { = } \frac { \mu } { 2 \sqrt { \mu p } } \bigg [ \left( 1 - e ^ { 2 } \right) \frac { d a } { d t } { - 2 a e \frac { d e } { d t } } \bigg ] { = } r T
$$

将方程(4.40)代人上式并消去 $d a / d t$ ，即得

$$
\frac { d e } { d t } = \frac { \sqrt { 1 - e ^ { 2 } } } { n a } [ S \sin f + \mathrm { { T } } ( \cos f + \cos \it { E } ) ] .
$$

为了由(4.45)式和(4.46)式推出 $\alpha i / d t$ 和 $d \Omega / d t$ ，需要计算$( r \times F _ { \varepsilon } ) _ { \varepsilon }$ 和 $( r \times F _ { e } ) _ { y }$ ．在空间极坐标系中有

$$
( \boldsymbol { r } \times \boldsymbol { F } _ { \epsilon } ) ^ { * } = \left( \begin{array} { c } { 0 } \\ { - r W } \\ { r T } \end{array} \right) .
$$

：经三次旋转可得 $\pmb { r } \times \pmb { F } .$ ，在地心赤道直角坐标系中的表达式，即

$$
\boldsymbol { r } \times \boldsymbol { F } _ { \varepsilon } = R _ { z } \left( - \varOmega \right) R _ { x } ( - i ) R _ { z } ( - u ) ( \boldsymbol { r } \times \boldsymbol { F } _ { \varepsilon } ) ^ { * }
$$

$$
= \left( \begin{array} { l } { r T \sin i \sin \varOmega + r W \left( \cos \varOmega \sin u + \sin \varOmega \cos u \cos i \right) } \\ { - r T \sin i \cos \varOmega + r W \left( \sin \varOmega \sin u - \cos \varOmega \cos u \cos i \right) } \\ { r T \cos i - r W \cos u \sin i } \end{array} \right) , (
$$

其中 ${ \pmb u } = { \pmb f } + { \pmb \omega }$ 将 $( r \times \pmb { F } , ) _ { x }$ 和 $( r \times { \pmb F } _ { \bullet } ) _ { \pmb { y } }$ 两个分量代人(4.45)式，作简单运算即得

$$
\begin{array} { l } { \displaystyle \frac { d i } { d t } = \frac { r c o s u } { n a ^ { 2 } \sqrt { 1 - e ^ { 2 } } } W , } \\ { \displaystyle \frac { d \varOmega } { d t } = \frac { r \sin u } { n a ^ { 2 } \sqrt { 1 - e ^ { 2 } \sin i } } W . } \end{array}
$$

利用轨道积分(4.27)式分别得出

$$
\begin{array} { r l } & { \frac { d r } { d t } { = } \frac { 1 - e ^ { 2 } } { 1 + e \cos f } \ \frac { d a } { d t } { - } \bigg [ \frac { p \cos f } { ( 1 + e \cos f ) ^ { 2 } } { - } \frac { 2 a e } { 1 + e \cos f } \bigg ] \frac { d e } { d t } } \\ & { \quad \quad + \frac { p e \sin f } { ( 1 + e \cos f ) ^ { 2 } } \frac { d f } { d t } , } \end{array}
$$

$$
\frac { d r } { d t } = \left( 1 - e \cos E \right) \frac { d a } { d t } - a \cos E \frac { d e } { d t } + a e \sin E \frac { d E } { d t } .
$$

而根据常数变易原理,按椭圆运动关系有

$$
\frac { d r } { d t } { = } \frac { \partial r } { \partial t } { = } \sqrt { \frac { \mu } { p } } e \sin f ,
$$

通过(4.38)式和开普勒积分给出的导数关系

$$
\frac { d M } { d t } { = } \left( 1 { - } e \cos E \right) \ \frac { d E } { d t } { - } \sin E \ \frac { d e } { d t }
$$

即可将(4.53)和(4.54)式中的 $d f / d t$ 和 $d E / d t$ 与 $d \omega / d t$ 和 $d M / d t$ 联系起来，从而导出最后两个方程

$$
\frac { d \omega } { d t } = \frac { \sqrt { 1 - e ^ { 2 } } } { n a e } \bigg [ - S \cos f + T \bigg ( 1 + \frac { r } { p } \bigg ) \sin f \bigg ] - \cos i \frac { d \varOmega } { d t } ,
$$

$$
\frac { d M } { d t } = n - \frac { 1 - e ^ { 2 } } { n a e } \bigg [ - S \bigg ( \cos f - 2 e \frac { r } { p } \bigg ) + T \left( 1 + \frac { r } { p } \right) \sin f \bigg ] .
$$

从上述六个方程的形式来看，地球引力常数 $\mu$ 仅出现在平运动速度 $\pmb { \mathscr { n } }$ 中，即

$$
n { = } \sqrt { \mu } a ^ { - 3 / 2 } .
$$

因此,在实际工作中,引用第一章给出的计算单位时， $\mu = 1$ 即对应

$$
\pmb { n } = \pmb { a } ^ { - 3 / 2 } ,
$$

所有方程的形式不变。

# 4.3摄动运动方程的各种形式

# 1．以六个椭圆轨道根数为基本变量的摄动运动方程

基本变量记作 $\pmb { \sigma } _ { . }$ ，它们是 $a , e , i , \Omega , \omega , M$ 六个随时间变化的吻切根数，根据不同问题的需要，摄动力(加速度)将以三种形式表达．其一是

径向分量 $\pmb { \mathscr { S } } _ { : }$ ，横向分量 $\pmb { T } _ { : }$ 轨道面法向分量 $\pmb { W }$ ，另一种形式是将 $s , \tau$ 改为

切向分量 $\pmb { U }$ ，法向分量 $N$

这里切向是指天体运动方向， $N$ 是轨道面内的法向分量，也称主法

线分量,而W又称次法线分量.U,N,W与S,T,W一样,组成右手螺旋系统，有些摄动力是保守力,存在势 $R _ { ☉ }$ ，即

$$
F _ { \varepsilon } { \equiv } \ g { \mathrm { r a d } } R
$$

其中 $\pmb { R }$ 又称为摄动函数.

为了由 $\pmb { \mathcal { S } } , \pmb { T } , \pmb { W }$ 型的摄动运动方程推出另两种形式，就必须找出 $\pmb { U } , \pmb { N } , \pmb { W }$ 三分量以及摄动函数的偏导数 $\partial R / \partial \sigma$ 与 $\delta , T _ { i }$ W的关系．首先考虑 $\pmb { U } , \pmb { N } .$ ，设径向与切向之间的夹角为 $\alpha ,$ 由坐标旋转，立即可得

$$
\left. \begin{array} { r } { S = U \cos \alpha - N \sin \alpha , \phantom { } } \\ { T = U \sin \alpha + N \cos \alpha . } \end{array} \right\}
$$

根据微分几何知识可知,对于曲线(即轨道） $r = r ( \theta )$ 或 $r = r ( f )$ ，有

$$
\mathrm { t g } \alpha = \mathcal { r } / \frac { d r } { d f } { = } \frac { 1 + e \cos f } { e \sin f } .
$$

由此可得

$$
\cos \alpha = \frac { e \sin f } { \sqrt { 1 + 2 e \cos f + e ^ { 2 } } } , \sin \alpha = \frac { 1 + e \cos f } { \sqrt { 1 + 2 e \cos f + e ^ { 2 } } } .
$$

将此结果代人(4.62)式得

$$
\left. \begin{array} { l } { { S = \frac { e \sin f } { \sqrt { 1 + 2 e \cos f + e ^ { 2 } } } U - \frac { 1 + e \cos f } { \sqrt { 1 + 2 e \cos f + e ^ { 2 } } } N , } } \\ { { \pi = \frac { 1 + e \cos f } { \sqrt { 1 + 2 e \cos f + e ^ { 2 } } } U + \frac { e \sin f } { \sqrt { 1 + 2 e \cos f + e ^ { 2 } } } N . } } \end{array} \right\}
$$

对于保守力情况有

$$
{ \mathcal { S } } { = } \frac { { \partial } R } { { \partial } r } , ~ { \mathcal { T } } { = } \frac { 1 } { r } ~ \frac { { \partial } R } { { \partial } { \dot { \theta } } } { = } \frac { 1 } { r } ~ \frac { { \partial } R } { { \partial } u } , ~ W { = } \frac { { \partial } R } { { \partial } z } { = } \frac { 1 } { r \sin u } ~ \frac { { \partial } R } { { \partial } { \dot { \iota } } } .
$$

有了这 关系，当然可以写出用摄动函数描述吻切根数变化的摄动运动方程，但方程右端还包含 $r , u , f , E$ 等量，若要使给出的方程 $d \sigma / d t$ ，其右端仅出现 $a , e , i$ 三个量和 $| \partial R / \partial \sigma ,$ 就必须求出 $\partial R / \partial \sigma$ 与 $s , \tau , \pi$ 之间的关系.

因 $\scriptstyle { \mathcal { R } } = R ( r )$ ,故有

$$
\frac { \partial R } { \partial \sigma } { = } \frac { \partial R } { \partial r } \cdot \frac { \partial r } { \partial \sigma } { = } \ F _ { \varepsilon } \cdot \frac { \partial r } { \partial \sigma }
$$

而其中

$$
F _ { \varepsilon } = R _ { z } ( - \varOmega ) R _ { x } ( - i ) R _ { z } ( - u ) \left( \begin{array} { c } { \mathscr S } \\ { T } \\ { W } \end{array} \right)
$$

$$
= { \left( \begin{array} { l l l } { \ell _ { 1 } } & { l _ { 2 } } & { l _ { 3 } } \\ { m _ { 1 } } & { m _ { 2 } } & { m _ { 3 } } \\ { n _ { 1 } } & { n _ { 2 } } & { n _ { 3 } } \end{array} \right) } { \left( \begin{array} { l } { S } \\ { T } \\ { W } \end{array} \right) } .
$$

这里 $l _ { j } , m _ { i } , \ n _ { j } ( j = 1 , 2 , 3 )$ 是径向、横向和轨道面法向单位向量的三个分量，即

$$
\begin{array} { r } { \hat { \pmb r } = \left( { \begin{array} { l } { l _ { 1 } } \\ { m _ { 1 } } \\ { n _ { 1 } } \end{array} } \right) , \hat { \pmb \theta } = \left( { \begin{array} { l } { l _ { 2 } } \\ { m _ { 2 } } \\ { n _ { 2 } } \end{array} } \right) , \hat { \pmb R } = \left( { \begin{array} { l } { l _ { 3 } } \\ { m _ { 3 } } \\ { n _ { 3 } } \end{array} } \right) . } \end{array}
$$

具体形式在第二章中已给出,它们是：

$$
\begin{array} { r l } & { l _ { 1 } = \cos { 2 \cos { \theta } } - \sin { 2 \sin { \theta } } \cos { i } , } \\ & { m _ { 1 } = \sin { 2 \cos { \theta } } - \cos { 2 \sin { \theta } } \cos { i } , } \\ & { n _ { 1 } = \sin { n \sin { i } } , } \\ & { l _ { 2 } = - \cos { 2 \sin { a } } - \sin { 2 \cos { \theta } } \cos { i } , } \\ & { m _ { 2 } = - \sin { 2 \sin { i } } \cos { i } \cos { \theta } \cos { i } , } \\ & { n _ { 3 } = \cos { n \sin { i } } , } \\ & { l _ { 3 } = \sin { 2 \sin { i } } , } \\ & { m _ { 3 } = - \cos { 2 \sin { i } } , } \\ & { n _ { 3 } = \cos { i } . } \end{array}
$$

$\hat { \pmb r } , \hat { \pmb \theta }$ ， $\hat { \mathbf { R } }$ 满足下列关系：

$$
\left. \begin{array} { l } { { \hat { r } ^ { 2 } = \hat { \theta } ^ { 2 } = \hat { R } ^ { 2 } = 1 , } } \\ { { \hat { r } \cdot \hat { \theta } = \hat { \theta } \cdot \hat { R } = \hat { R } \cdot \hat { r } = 0 . } } \end{array} \right\}
$$

剩下的问题是求 $\frac { \partial r } { \partial \sigma }$

$$
r = r \hat { r }
$$

可知

$$
\frac { \partial r } { \partial \sigma } { = } \frac { \partial r } { \partial \sigma } \hat { r } + r \frac { \partial \hat { r } } { \partial \sigma } ,
$$

其中

$$
\frac { \partial \hat { r } } { \partial \sigma } = ( { l _ { 3 } \sin u \frac { \partial i } { \partial \sigma } - m _ { 1 } \frac { \partial \varOmega } { \partial \sigma } + l _ { 2 } \frac { \partial u } { \partial \sigma } } )  { m _ { 3 } \sin u \frac { \partial i } { \partial \sigma } + l _ { 1 } \frac { \partial \varOmega } { \partial \sigma } + m _ { 2 } \frac { \partial u } { \partial \sigma } }  \\ { \displaystyle { n _ { 3 } \sin u \frac { \partial i } { \partial \sigma } - m _ { 3 } \frac { \partial u } { \partial \sigma } } + { n _ { 2 } \frac { \partial u } { \partial \sigma } } } ) .
$$

将(4.68)式和(4.75)式连同(4.69)—(4.72)式以及(4.76)式一并代人(4.67)式,经整理后得

$$
\begin{array} { c } { { \displaystyle { \frac { \partial R } { \partial \sigma } } = { \mathcal { S } } { \displaystyle { \frac { \partial r } { \partial \sigma } } } + r T \bigg ( \cos i { \frac { \partial \varOmega } { \partial \sigma } } + { \frac { \partial \dot { u } } { \partial \sigma } } \bigg ) + { r } W \bigg ( \sin u { \frac { \partial \dot { u } } { \partial \sigma } } } } \\ { { \displaystyle - \sin i \cos u { \frac { \partial \varOmega } { \partial \sigma } } \bigg ) . } } \end{array}
$$

利用第二章\$2.2中的结果

$$
\left. \begin{array} { l } { { \displaystyle { \frac { \partial r } { \partial t } } = { \frac { r } { a } } , { \frac { \partial r } { \partial e } } = - a \cos f , { \frac { \partial r } { \partial M } } = { \frac { a e } { \sqrt { 1 - e ^ { 2 } } } } \sin f , \qquad } } \\ { { \displaystyle { \frac { \partial u } { \partial \omega } } = 1 , { \frac { \partial u } { \partial e } } = { \frac { 1 } { 1 - e ^ { 2 } } } \Big ( 1 + { \frac { p } { r } } \Big ) _ { \cdot } \sin f , { \frac { \partial u } { \partial M } } = \Big ( { \frac { a } { r } } \Big ) ^ { 2 } \sqrt { 1 - e ^ { 2 } } , \Big \{ 1 - e ^ { 2 } \Big \} , } }  \end{array} \right.
$$

就可给出(4.77)式的具体形式,即

$$
\begin{array} { r } {  \begin{array} { l } { \frac { \partial R } { \partial a } = \frac { r } { a } \mathcal { S } , } \\ {  \frac { \partial R } { \partial \theta } - - a \cos \hat { s } \hat { l } \mathcal { S } \cdot \boldsymbol { \nu } ( \frac { 1 } { L - e ^ { \xi } } + \frac { a } { T } ) \sin f \mathcal { T } , } \\ {  \frac { \partial R } { \partial \hat { l } } - r \sin u \mathcal { W } ,  } \\ {  \frac { \partial R } { \partial \theta } - r \cos i \mathcal { T } - r \cos u \sin i W ,  } \\ {  \frac { \partial R } { \partial \theta } - r \mathcal { T } ,  } \\ {  \frac { \partial R } { \partial \theta } - r \mathcal { T } ,  } \\ {  \frac { \partial R } { \partial \theta } - \frac { a e } { \sqrt { 1 - e ^ { 2 } } } \sin f \mathcal { S } + \frac { a ^ { 2 } \sqrt { 1 - e ^ { 2 } } } { r } \mathcal { T } . } \end{array} \} } \end{array}
$$

根据前面的推导，我们将三种形式的摄动运动方程整理于下：

(1) $s , T , W$ 型

$$
\left. \begin{array} { l } { \displaystyle \frac { d a } { d t } = \frac { 2 } { \pi \sqrt { 1 - e ^ { 2 } } } \Big [ \delta e \sin f + T ( 1 + e \cos f ) \Big ] , } \\ { \displaystyle \frac { d e } { d t } = \frac { \sqrt { 1 - e ^ { 2 } } } { \pi a } \Big [ , \boldsymbol { S } \sin f + T ( \cos f + \cos E ) \Big ] , } \\ { \displaystyle \frac { d i } { d t } = \frac { \pi \cos t } { \pi a ^ { 2 } \sqrt { 1 - e ^ { 2 } } } \cdot \boldsymbol { F } , } \\ { \displaystyle \frac { d g } { d t } = \frac { \pi \sin t } { \pi a ^ { 2 } \sqrt { 1 - e ^ { 2 } } \sin ^ { 2 } t } , } \\ { \displaystyle \frac { d g } { d t } = \frac { \pi \sin t } { \pi a ^ { 2 } \sqrt { 1 - e ^ { 2 } } \sin ^ { 2 } t } , } \\ { \displaystyle \frac { d c } { d t } = \frac { \sqrt { 1 - e ^ { 2 } } } { \pi a ^ { 2 } } \Big [ - \delta \cos f + T \Big ( 1 + \frac { T } { \frac { T } { \frac { T } { \rho } } } \Big ) \sin f \Big ] - \cos i \frac { d \Omega } { d t } , } \\ { \displaystyle \frac { d \lambda t } { d t } = n - \frac { 1 - e ^ { 2 } } { \pi a ^ { 2 } } \Big [ - \delta \Big ( \cos f - 2 e \frac { T } { \frac { T } { \rho } } \Big ) + T \Big ( 1 + \frac { T } { \frac { T } { \rho } } \Big ) \sin f \Big ] . } \end{array} \right\}
$$

(2) $U , N , W$ 型

$$
\begin{array} { r l } & { \frac { \lambda \alpha } { 4 L } - \underbrace { 2 } ^ { 2 } } \\ & { \frac { \lambda \alpha } { 4 L } - \underbrace { 2 } ^ { 2 } } \\ & { \frac { \delta \alpha } { 4 R } - \underbrace { \sqrt { 1 - \alpha } ^ { 2 } } _ { \mathrm { \normalfont { n } \neq 0 } } ( 1 + 2 \alpha \cos { f } \mathrm { \normalfont ~ e } ^ { 2 } ) ^ { - \alpha } \nabla L ( \cos { f } \mathrm { \normalfont ~ - } \mathrm { e } ) U - \sqrt { 1 - \alpha ^ { 2 } } } \\ & { \frac { \varepsilon } { 4 R } - \mathrm { \normalfont ~ a n } L \nabla L ) , } \\ & { \frac { \lambda \alpha } { 4 R } - \frac { \sqrt { 1 - \alpha } ^ { 2 } } { 4 R } ( 1 + 2 \alpha \cos { f } \mathrm { \normalfont ~ e } ^ { 2 } ) ^ { - \alpha + \frac { 2 } { 4 R ^ { 2 } } } \left[ 2 \sin { 2 } \mathrm { \normalfont ~ f } U - \ ( \cos {  { \underline { { F } } } } + \mathrm { e } ) \right] , } \\ & { \frac { \lambda \alpha } { 4 R } - \frac { \varepsilon } { 3 R } - \mathrm { \normalfont ~ a n } L \mathrm { \normalfont ~ , } } \\ & { \frac { \lambda \alpha } { 4 R } - \frac { 1 - \alpha } { 8 R \omega } \left( 1 + 2 \alpha \cos { f } \mathrm { \normalfont ~ e } ^ { 2 } \right) ^ { - \alpha } \nabla L \left( 2 \sin {  { \underline { { f } } } } + \frac { 2 \alpha ^ { 2 } } { \sqrt { 1 - \alpha ^ { 2 } } } \right. } \\ & { \left. \phantom { \frac { \varepsilon } { 4 R } - \frac { 1 - \alpha } { 4 R } } \right) , } \end{array}
$$

$\frac { d i } { d t } \neqq \frac { d \Omega } { d t }$ 与上相同，上述两种类型称为高斯(Gauss)型.

(3） $\partial R / \partial \sigma$ 型

$$
\begin{array} { r l } & { \frac { d \overline { { u } } } { d t } = \frac { 2 } { n \alpha \overline { { a } } } \frac { \partial R } { \partial M } } \\ & { \frac { d \overline { { v } } } { d t } = \frac { 1 - e ^ { - 2 } \overline { { \alpha } } ^ { 2 } R } { n \alpha ^ { 2 } e ^ { 3 } \overline { { \mathcal { M } } } } - \frac { \sqrt { 1 - e ^ { 2 } } } { n \alpha ^ { 2 } e } \frac { \partial R } { \partial \omega } , } \\ & { \frac { d \overline { { i } } } { d t } = \frac { 1 } { n \alpha ^ { 2 } \sqrt { 1 - e ^ { 2 } } \sin \overline { { i } } } \langle \mathrm { e s } i \frac { \partial R } { \partial \omega } - \frac { \partial R } { \partial \mathcal { D } } \rangle , } \\ & { \frac { d \overline { { \Omega } } } { d t } = \frac { 1 } { n \alpha ^ { 2 } \sqrt { 1 - e ^ { 2 } } \sin \overline { { i } } } \frac { z R } { \partial t } , } \\ & { \frac { d \omega } { d t } = \frac { \sqrt { 1 - e ^ { 2 } } \overline { { \alpha } } ^ { 2 } R } { n \alpha ^ { 2 } e ^ { - 2 } \widetilde { \alpha } \overline { { e } } ^ { - } \cos \overline { { i } } \frac { d \overline { { \Omega } } } { \widetilde { \mathcal { U } } } } , } \\ &  \frac { d \overline { { \mathcal { M } } } } { d t } = - \frac { 1 - e ^ { 2 } } { n \alpha ^ { 2 } e ^ { \frac { \partial R } { \partial e } } - \frac { 2 } { n \alpha ^ { 2 } e ^ { \frac { \partial R } { \partial e } } } \frac { \partial R } { \partial z } . } \end{array}
$$

这种类型称为拉格朗日(Lagrange)型.

2．适合于任意偏心率 $( 0 { \leqslant } e { < } 1 )$ 问题的摄动运动方程

前面推出的方程，右端含有 $\frac { 1 } { e }$ 因子，不能用于 $\pmb { e } = 0$ 的情况.为此引进新变量，它们是

$$
a , i , \Omega , \xi = e \cos \omega , \eta = - e \sin \omega , \lambda = M + \omega .
$$

为什么要取这六个根数或根数的组合作为基本变量，将在后面第六章中讨论。根据变量的定义和前面已推出的方程，经简单运算即可给出以新变量表达的摄动运动方程，其形式如下：

$( \mathrm { ~ 1 ~ } ) \ S , T , W$ 型

$$
\begin{array} { r l } & { \quad \frac { d } { d t } = - \frac { 2 } { 3 \pi \sqrt { 1 - e ^ { 2 } } }  \phantom { \frac { b } { b } } \int \phantom { \frac { b } { b } } ( \xi \sin \theta + \eta \cos \theta ) + \mathcal { F } ( \frac { \sqrt { b } } { e ^ { 2 } } )  } \\ & { \quad \frac { d } { d t } = - \frac { \sqrt { 1 - e ^ { 2 } } } { 3 \pi \sqrt { 1 - e ^ { 2 } } }  \phantom { \frac { b } { b } } \int \phantom { \frac { b } { b } } ( \xi \sin \theta + \frac { T } { \sqrt { 1 - e ^ { 2 } } } e ^ { \theta } ) ( 1 + \sqrt { 1 - e ^ { 2 } } ) \cos \theta \sin \theta  } \\ & { \quad  \frac { d } { d t } = - \frac { \sqrt { 1 - e ^ { 2 } } } { 1 + \sqrt { 1 - e ^ { 2 } } } ( \xi \cos \theta + \frac { T } { \sqrt { 1 - e ^ { 2 } } } ) \sin \theta  - \eta \cos \theta \frac { \sqrt { 1 - e ^ { 2 } } } { \sqrt { 1 - e ^ { 2 } } } \cos \theta \sin \theta } \\ & { \quad  - \frac { \sqrt { 1 - e ^ { 2 } } } { 1 + \sqrt { 1 - e ^ { 2 } } } ( \theta \cos \theta + \frac { T } { \sqrt { 1 - e ^ { 2 } } } e ^ { \theta } - ( 1 + \sqrt { 1 - e ^ { 2 } } e ^ { \theta } ) \sin \theta    } \\ & { \quad   \frac { d } { d t } = - \frac { \sqrt { 1 - e ^ { 2 } } } { 1 + \sqrt { 1 - e ^ { 2 } } } ( \xi \cos \theta + \frac { T } { \sqrt { 1 - e ^ { 2 } } } e ^ { \theta } - ( 1 + \sqrt { 1 - e ^ { 2 } } e ^ { \theta } ) \sin \theta    } \\ & { \quad    - \frac { \sqrt { 1 - e ^ { 2 } } } { 1 + \sqrt { 1 - e ^ { 2 } } } \xi \cos \theta )  + \xi \cos \theta \frac { \sqrt { 1 - e ^ { 2 } } } { \sqrt { 1 - e ^ { 2 } } } \xi \cos \theta  } \\ &  \quad  \mathcal { H } _ { a } ^ { 1 } \times \dots \frac { \sqrt { 1 - e ^ { 2 } } } { \sqrt { 1 - e ^ { 2 } } }   \end{array}
$$

其中 $\widetilde { u } = \dot { \theta } + \omega , d i / d t , d \Omega / d t$ 与前面(4.80)式中的形式相同，不再重复.

(2) $\partial R / \partial \sigma$ 型

$$
 \begin{array} { l }  \displaystyle  \begin{array} { l } { \displaystyle \frac { \partial \vec { x } } { \partial \xi } - \frac { 1 } { 8 4 \alpha ^ { 2 } \sqrt { 3 } \alpha ^ { 2 } } \frac { 1 } { \sin { \alpha } ^ { 3 } } [ \cos \vec { x } ( \frac { 1 } { 9 \hat { x } } - \hat { \mathrm { s } } \frac { 2 \Re B } { \hat { x } ^ { 3 } } + \frac { 2 B R } { \partial \lambda } ) - \frac { \partial \vec { x } } { \partial \mathcal { A } } ] \} } \\ { \displaystyle \frac { \partial \vec { x } } { \partial \xi } - \frac { 1 } { \sin { \alpha } ^ { 3 } \sqrt { 3 } \alpha ^ { 2 } \sqrt { 3 } \alpha ^ { 3 } } \frac { 2 R } { \sin { \alpha } ^ { 3 } \hat { x } ^ { 3 } } , } \\ { \displaystyle \frac { \partial \vec { x } } { \partial \xi } - \frac { \sqrt { 1 - e ^ { - \frac { \beta } { 2 } } \beta \mathcal { B } } } { 3 4 \alpha ^ { 3 } } - \frac { \frac { \partial \vec { x } } { \partial \xi } } { \sin { \alpha } ^ { 3 } \hat { x } ^ { 3 } } \frac { 1 } { \sin { \alpha } ^ { 5 } } \frac { 2 } { ( 1 + \sqrt { 1 - e ^ { \frac { \beta } { 2 } } } ) ^ { 3 } \hat { \partial } \lambda _ { \lambda } ^ { 3 } } - \eta \cos { \alpha } \frac { \delta \vec { \xi } \vec { \xi } \vec { \xi } } { \partial \mathcal { A } } , } \\ { \displaystyle \frac { \partial \vec { x } } { \partial \xi } - \frac { \sqrt { 1 - e ^ { - \frac { \beta } { 2 } } \alpha \beta } \mathcal { R } } { \partial \alpha ^ { 2 } } \frac { \sqrt { 1 - \cos ^ { 2 } \delta \xi } } { \partial \alpha ^ { 2 } } \frac { \sqrt { 1 - e ^ { \frac { \beta } { 2 } } \alpha \beta } } { ( 1 + \sqrt { 1 - e ^ { \frac { \beta } { 2 } } } ) ^ { 3 / 2 } } \partial \vec { x } } \\  \displaystyle \frac { \partial \vec { x } } { \partial \xi } - \frac { \sqrt { 1 - e ^ { \frac { \beta } { 2 } } \alpha \beta } } { \partial \alpha ^ { 2 } } \frac { 2 R } { \partial \alpha ^ { 2 } } - \frac { \sqrt { 1 - e ^ { \frac { \beta } { 2 } } \alpha ^ { 2 } } }  ( 1 + \sqrt   \end{array} \end{array}
$$$$
- \cos i { \frac { d \Omega } { d t } } .
$$

这两组方程的右端不再出现 $1 / e$ 因子.

3．适用于任意偏心率 $( 0 { \leqslant } e { < } 1 )$ 和倾角 $( 0 { \leqslant } i { \ < } 1 8 0 ^ { \circ } )$ 问题的摄动运动方程

上述方程右端还有1/sin $\pmb { i }$ 因子,不适用于 $i = 0$ 或 $1 8 0 ^ { \circ }$ 情况.但对于人造地球卫星，一般不会出现 $i = 1 8 0 ^ { \circ }$ 的情况，只需考虑$\pmb { i } = 0$ 的问题，为此，引进另一组新变量，它们是：

$$
\alpha , h = \sin i \cos \varOmega , k = - \sin i \sin \varOmega ,
$$

$$
\boldsymbol { \xi } = e \cos { ( \omega + \Omega ) } , \eta = - e \sin { ( \omega + \Omega ) } , \lambda { = } M + \omega + \Omega .
$$

同样,在第六章中将要讨论这一问题，这里先写出相应的摄动运动方程．通常,对于同时出现 $\pmb { e = 0 }$ 和 $i = 0$ 的问题，摄动力往往是保守力,故下面只写出 $\partial R / \partial \sigma$ 型的方程.至于 $s , \tau , W$ 型的方程，读者如有需要，按上述过程推出它也并不困难。 $2 R / 2 \sigma$ 型方程如下

$$
\begin{array} { r l } & { \frac { \mathrm { d } } { \mathrm { d } t } - \frac { \mathrm { d } } { \mathrm { d } t ^ { 2 } } \frac { \mathrm { d } \omega } { \partial t } - \frac { \mathrm { d } } { \mathrm { d } t } \frac { \partial } { \partial t } + \frac { \mathrm { d } } { \partial t } \frac { \partial } { \partial t } + \frac { \mathrm { d } } { \mathrm { d } t } \frac { \partial } { \partial t } - \eta ^ { 2 } \frac { \partial L } { \partial t } + \frac { \mathrm { d } L ^ { 2 } \eta } { \partial t } - \frac { \partial L ^ { 2 } } { \partial t ^ { 2 } } \frac { \partial L ^ { 2 } } { \partial \eta ^ { 2 } } - \frac { \partial L ^ { 2 } } { \partial t ^ { 2 } } \bigg | } \\ & { + \frac { \mathrm { d } } { \mathrm { d } t } \frac { \partial } { \partial t } - \frac { \partial L ^ { 2 } } { \partial t } - \overline { { \eta } } \bigg [ - \frac { \partial L ^ { 2 } } { \partial t } + \frac { \mathrm { d } } { \mathrm { d } t } \frac { \partial } { \partial t } - \bigg ( - \eta \frac { \partial L ^ { 2 } } { \partial t } + \xi \frac { \partial L ^ { 2 } } { \partial t } - \frac { \partial L ^ { 2 } } { \partial t } \bigg ) \bigg ] } \\ & { + \frac { \mathrm { d } } { \mathrm { d } t } \frac { \partial } { \partial t } - \frac { \mathrm { d } } { \partial t } \frac { \partial } { \partial t } - \frac { \mathrm { d } } { \partial t } \frac { \partial } { \partial t } + \frac { \mathrm { d } } { \partial t } \frac { \partial } { \partial t } \bigg ( \frac { \partial \partial \mathbf { k } } { \partial t } + \frac { \partial L ^ { 2 } } { \partial t } + \frac { \partial L ^ { 2 } } { \partial t } - \frac { \partial L ^ { 2 } } { \partial t } \bigg ) , } \\ &  + \frac { \mathrm { d } } { \mathrm { d } t } \frac { \partial } { \partial t } - \frac { \mathrm { d } } { \partial t } \frac { \partial } { \partial t } - \frac { \mathrm { d } } { \partial t } \frac { \partial } { \partial t } \frac { \partial \partial \mathbf { k } } { \partial t } + \frac { \mathrm { d } } { \partial t } \frac { \partial } { \partial t } \frac { \partial \mathbf { k } } { \partial t } + \frac { \partial L ^ { 2 } } { \partial t } \\ &  + \frac { \mathrm { d } } { \partial t } \frac   \end{array}
$$

这种形式的方程不再有 $1 / e$ 和1/sin $\pmb { i }$ 因子.

# 4.4 摄动运动方程的级数解

经常数变易法处理，原受摄运动方程

$$
\ddot { r } = F _ { 0 } + \dot { F } _ { e }
$$

的求解问题就转化为相应的摄动运动方程

$$
\frac { d \sigma } { d t } { = } f _ { \ast } ( \sigma , t , \varepsilon )
$$

的求解问题．这里 $\pmb { \sigma }$ 表示一六维向量，六个分量即吻切根数或前面引进的那两组“无奇点”变量，相应的右函数 $f$ ，则是六维向量函

数，原运动问题的解由两部分组成，即

$$
\left. \begin{array} { l } { r = r ( \sigma , t ) , \bar { r } = \bar { r } ( \sigma , t ) , } \\ { \sigma ( t ) = \sigma ( \sigma _ { 0 } , t _ { 0 } ; t , e ) . } \end{array} \right\} .
$$

其中 $\pmb { r }$ 和 $\scriptstyle { \dot { \pmb { r } } }$ 的表达式已知，它们对应于一瞬时椭圆．剩下的问题是如何求解小参数方程(4.86),以给出解 $\sigma ( t )$ ·

尽管方程(4.86)是复杂的非线性方程组，但其右端含小参数$\varepsilon _ { i }$ ，给出相应的小参数幂级数解并不困难，已有成熟的方法，即摄动法．在未介绍这一方法之前，对于小参数方程(4.86)有一说明，如果 $\pmb { \sigma }$ 的第六个分量用过近地点时刻 $\pmb { \tau }$ 或 $M _ { 0 } = - n \tau _ { \mathrm { { 0 } } }$ ，则右函数 $f .$ 的六个元素的量级都是 $O ( \varepsilon )$ ，然而，这里是用时间根数 $M$ ，相应的 $f _ { \bullet }$ 的第六个分量含有一项 $\pmb { n } = \pmb { O } ( \pmb { \varepsilon } ^ { 0 } )$ ，故方程(4.86)应改写成下列形式：

$$
\frac { d \sigma } { d t } { = } f _ { 0 } ( a ) + f _ { 1 } ( \sigma , t , \varepsilon ) ,
$$

其中

$$
\begin{array} { r } { f _ { 0 } ( a ) = \delta n , \delta = ( 0 , 0 , 0 , 0 , 0 , 1 ) ^ { \tau } . } \end{array}
$$

$f _ { 1 }$ 的各分量的量级均为 $O ( \varepsilon )$ ·

方程(4.88)的小参数幂级数解的形式为

$$
\begin{array} { c } { { \sigma ( t ) = \sigma ^ { ( 0 ) } ( t ) + \Delta \sigma ^ { ( 1 ) } ( t , \varepsilon ) + \Delta \sigma ^ { ( 2 ) } ( t , e ^ { 2 } ) + \cdots } } \\ { { { } } } \\ { { + \Delta \sigma ^ { ( t ) } ( t , \varepsilon ^ { l } ) + \cdots . } } \end{array}
$$

其中 $\sigma ^ { ( 0 ) } \left( t \right)$ 是对应 $\varepsilon = 0$ 的无摄运动解,即

$$
\begin{array} { r l } & { { \pmb a } ^ { ( 0 ) } \left( \mathit { t } \right) = { a } _ { 0 } , { \boldsymbol e } ^ { ( 0 ) } \left( \mathit { t } \right) = { e } _ { 0 } , \mathit { i } ^ { ( 0 ) } \left( \mathit { t } \right) = \dot { \iota } _ { 0 } , } \\ & { { \pmb Q } ^ { ( 0 ) } \left( \mathit { t } \right) = \mathcal { Q } _ { 0 } , { \omega } ^ { ( 0 ) } \left( \mathit { t } \right) = \omega _ { 0 } , } \\ & { \mathcal { M } ^ { ( 0 ) } \left( \mathit { t } \right) = \mathcal { M } _ { 0 } + { \pmb n } _ { 0 } \left( \mathit { t } - \mathit { t } _ { 0 } \right) . } \end{array}
$$

其中 $\sigma _ { \Updownarrow }$ 是历元 $\scriptstyle t _ { 0 }$ 时的根数，亦称初始根数．不难看出，对 $e = 0$ 展开的小参数幂级数解，实际上就是解 $\sigma ( t )$ 在无摄运动解 ${ \pmb { \sigma } } ^ { ( 0 ) } \{ t \}$ “处”展开。 $\Delta \sigma ^ { ( 1 ) } , \Delta \sigma ^ { ( 2 ) }$ ，…各称为一阶摄动，二阶摄动，…，将形

式解(4.90)代人方程(4.88)的两端，得

$$
\begin{array} { l } { { \displaystyle \left. \begin{array} { c } { { \displaystyle \frac { d } { d t } \biggl [ \sigma ^ { ( 0 ) } + \Delta \sigma ^ { ( 1 ) } + \Delta \sigma ^ { ( 2 ) } + \cdots + \Delta \sigma ^ { ( l ) } + \cdots \biggr ] } } \\ { { \vdots } } \\ { { = f _ { 0 } \bigl ( a ^ { ( 0 ) } \bigr ) + \displaystyle \frac { \partial f _ { 0 } } { \partial a } \biggl [ \Delta a ^ { ( 1 ) } + \Delta a ^ { ( 2 ) } + \cdots \biggr ] + \frac { 1 } { 2 \partial a ^ { 2 } } f _ { 0 } \biggl [ \Delta a ^ { ( 1 ) } + \cdots \biggr ] ^ { 2 } } } \end{array} \right. } } \\ { { \displaystyle = f _ { 0 } \bigl ( a ^ { ( 0 ) } \bigr ) + \frac { \partial f _ { 0 } } { \partial a } \biggl [ \Delta a ^ { ( 1 ) } + \Delta a ^ { ( 2 ) } + \cdots \biggr ] + \frac { 1 } { 2 \partial a ^ { 2 } } f _ { 0 } \biggl [ \Delta a ^ { ( 1 ) } + \cdots \biggr ] ^ { 2 } } } \end{array}
$$

$$
+ \cdots + f _ { 1 } ( \sigma ^ { ( 0 ) } , t , e ) \cdot \mathrm { i } \cdot \mathrm { \sum _ { j = 1 } ^ { 8 } } \frac { \partial f _ { 1 } } { \partial \sigma _ { j } } [ \Delta { \sigma _ { j } } ^ { ( 1 ) } \cdot + \Delta \sigma _ { j } ^ { ( 2 ) } + \cdots ]
$$

$$
+ \frac { 1 } { 2 } \sum _ { j } \sum _ { k } \frac { \partial ^ { 2 } f _ { 1 } } { \partial \sigma _ { j } \partial \sigma _ { k } } [ \Delta { \sigma _ { j } } ^ { ( 1 ) } + \cdots ] [ \Delta { \sigma _ { k } } ^ { ( 1 ) } + \cdots ] + \cdots .
$$

该式右端各项中出现的根数 $\pmb { \sigma }$ 均应取为 $\sigma ^ { ( 0 ) } \left( t \right)$ ，若级数（4.90） 式收敛，则比较展开式(4.92)两端同次幂 $( \pmb \varepsilon ^ { l } )$ 的系数即得

$$
 \begin{array} { l } { { \displaystyle \sigma ^ { ( 0 ) } ( t ) = \sigma _ { 0 } + \int _ { t _ { 0 } } ^ { t } \delta _ { \hat { n } _ { 0 } } d t = \sigma _ { 0 } + \delta _ { \hat { n } _ { 0 } } ( t - t _ { 0 } ) , } } \\ { { \displaystyle \Delta \sigma ^ { ( 1 ) } ( t ) = \int _ { t _ { 0 } } ^ { t } [ \delta \frac { \partial \pi } { \partial \hat { a } } \Delta a ^ { ( 1 ) } + f _ { 1 } ( \sigma , t , \varepsilon ) ] _ { \sigma ( 0 ) } d t } } \\ { { \displaystyle \Delta \sigma ^ { ( 2 ) } ( t ) =  \int _ { t _ { 0 } } ^ { t } [ \delta ( \frac { \partial \pi } { \partial \hat { a } } \Delta a ^ { ( 2 ) } + \frac { 1 } { 2 } \frac { \partial ^ { 2 } \pi } { \partial \hat { a } ^ { 2 } } ( \Delta a ^ { ( 1 ) } ) ^ { 2 } )  } } \\ { { \displaystyle  \qquad + \sum _ { j } \frac { \partial f _ { 1 } } { \partial \sigma _ { j } } \Delta \sigma _ { j } ^ { ( 1 ) } \sigma _ { j } ^ { ( 1 ) } ] _ { \sigma ( 0 ) } d t } } \\ { { \displaystyle \qquad \quad . } } \end{array} \}
$$

显然，这是一个有效的递推过程，由低阶摄动求高阶摄动．将 $f _ { t }$ $( \sigma , t , \varepsilon )$ 的具体形式代入后，即可给出(4.90)式中的各阶摄动表达式.

在一定条件下，上述级数解(4.90）的收敛范围是 $n ( t - t _ { 0 } )$ $= O { \Big ( } { \frac { 1 } { \varepsilon } } { \Big ) } ^ { [ 3 ] }$ 这一提动法已在天体力学和非线性力学等领域里得到广泛应用，但在计算人造地球卫星的轨道变化时不甚理想，有必要作某些改进，这将在以后几章中逐一介绍。

通常,如果摄动力是保守力,在有限时间间隔内，对于低阶摄动， $a , e , i$ 仅有周期变化， $\Omega , \omega$ 有随时间的长期变化，但比 $M$ （或$E , f )$ 的变化缓慢得多，因后者是直接反映人造卫星绕地球运动的根数，而 $\pmb { \Omega }$ 和 $\pmb { \omega }$ 的变化仅仅由摄动引起。故有时称 $a , e , i$ 为“不变量”， $\Omega$ 和 $\pmb { \omega }$ 为慢变量， $M$ 或 $\smash { \mathbf { \mathcal { E } } _ { 3 } f } )$ 为快变量，在上述情况下，摄动变化 $\Delta \sigma ^ { ( 1 ) }$ ， $\Delta \sigma ^ { ( 2 ) }$ ，…中-般包含三种性质不同的项：长期项，长周期项和短周期项．它们的形式基本上有如下特征：长期项是时间间隔 $( t - t _ { 0 } )$ 的线性函数或多项式，其系数仅是 $a , e , i$ 的函数；长周期项是 $\pmb { \Omega }$ 或 $\pmb { \omega }$ 的函数，而短周期项则是 $M$ 的周期函数．除此之外,还有其它形式的长周期项，以及形如 $( t - t _ { 0 } ) \sin { ( A t + B ) }$ 和 $( t - t _ { 0 } ) \cos { ( A t + B ) }$ 等形式的泊松(Poisson)项,亦称混合项.如果摄动力是耗散力， $a _ { s } e$ 将有长期变化，各种摄动项的形式要复杂一些.

# 84.5摄动力的取舍问题

在 $\ S \ 4 . 1$ 中列举了人造地球卫星在运动过程中的受力状况，但对于一个具体问题．不必考虑所有的力学因素.当精度要求（记作 $\varepsilon ^ { * }$ )给定后，哪些摄动因素必须考虑是可以进行估计的。

假定某--摄动力 $\boldsymbol { F } _ { \cdot } = | \boldsymbol { F } _ { \cdot } |$ 相对于中心引力 $F _ { 0 } = \frac { 1 } { r ^ { 2 } }$ 的大小为

$$
\mathbb { F } _ { \varepsilon } / F _ { 0 } = \varepsilon .
$$

若 $\pmb { F }$ ，为保守力，可以认为轨道半长径 $\pmb { a }$ 无长期变化．根据前面给出的摄动运动方程进行估计,不难得知，在 $\Delta t = t - t _ { 0 }$ 间隔内，根数摄动变化 $( \Delta a / a , \Delta e , \Delta i , \Delta \mathcal { Q } , \Delta \omega , \Delta \mathcal { M } )$ 的范围是：

$$
\frac { 2 } { n a } F _ { \ast } \Delta t \approx \frac { 2 \varepsilon } { n a } F _ { \ast } \Delta t \approx \frac { 2 \varepsilon } { n ^ { 2 } a ^ { 3 } } ( n \Delta t )
$$

$$
= 2 e ( n \Delta t ) .
$$

如果 $\pmb { F } .$ 只引起短周期摄动，则上述范围将变成 $\mathbf { \Delta } \mathfrak { L } \mathfrak { e }$ 若 $\pmb { F _ { e } }$ 为耗散力， $\pmb { a }$ 将有长期变化，而 $d M / d t$ 右端有一零阶项 $\pmb { n }$ ，那么上述变化范围扩大为

$$
\frac { 3 } { 2 } e ( n \Delta t ) ^ { 2 } .
$$

根据上述估计可知：若摄动力为保守力，且满足

$$
2 \varepsilon ( n \Delta t ) \geqslant { e ^ { * } } ,
$$

则该摄动因素必须考虑．对于只引起短周期变化的情况，条件(4.96)式变为

$$
2 \varepsilon \geqslant \varepsilon ^ { * } .
$$

而当 $\pmb { F }$ ，为耗散力时，则条件(4.96)式变为

$$
: \frac { 3 } { 2 } \varepsilon \left( n \Delta t \right) ^ { 2 } \geqslant \varepsilon ^ { * } :
$$

以上 $\pmb { n } \Delta t$ 是卫星运动所经历的弧长．这里给出的条件表明，在精度要求给定后，根据计算间隔的长短，即可知道哪些摄动因素该考虑，在实际工作中可用来对摄动因素进行初选.

# 参考文献

[1] Iy6aro,A.Ⅱ.，onpeπeπeHne op6nT，MOCKBA，JEHNH-PPAП,1949.

[2] Brouwer,D.,Clemence,G.M.,Methods of Celestial Mechanics,Acεdemic Press,New York and London，1961.

[3］易照华，孙义燧，摄动理论，第三章，科学出版社，1981.

# 第五章 地球形状摄动与平均根数法

根据上一章对人造卫星绕地球运动过程中的受力分析，已经知道：不仅地心引力占主导地位，而且除面质比较大的低轨道(离地面高度在 $2 0 0 ~ \mathrm { k m }$ 以下)卫星外，地球形状摄动(包括形状不规则和密度分布不均匀两个方面)是一个主要摄动因素，因此，首先研究这一问题是很自然的．另外，尽管相应的摄动力是一保守力，有它的特殊性，但它的表达形式，从某种意义上讲，仍带有一种普遍性，通过讨论这种摄动对卫星轨道的影响，引进人卫运动理论研究和实际应用中的一个重要方法一平均根数法，显然是合适的.关于这种方法，同样可用来研究其它类型的摄动，而且它的基本思想也可作为另外一些重要方法的基础.

# 5.1地球引力场的位函数

对于质点引力场，空间任何一点的引力位由下式表达

$$
V _ { 0 } { = } \frac { G M } { r } ,
$$

其中 $G$ 是引力常数， $\pmb { M }$ 是质点的质量， $\pmb { \mathscr { r } }$ 是空间测量点到该质点的距离．显然， $V _ { 0 } { = } V _ { 0 } ( r )$ 是空间点的函数，亦称位函数．相应的引力加速度为

$$
\bar { F } _ { 0 } = \mathrm { g r a d } V _ { 0 } = - \frac { G M } { r ^ { 2 } } \biggl ( \frac { r } { r } \biggr ) .
$$

关于地球，通常不能把它看成质点，地球引力场的位函数$\pmb { V } ( \pmb { x } , \pmb { y } , z )$ 与质点引力位函数 $V _ { 0 } ( r )$ 是有差别的．但是，可将地球·104·

：分解成若干个小体元（相应的质量记作 $d \pmb { M } _ { \bot }$ ，每个小体元可以看·成质点，于是地球引力场位函数可以用一个积分来表达，即

$$
V ( x , y , z ) = \int \int \int { \frac { G d M } { r ^ { \prime } } } .
$$

其中 $\pmb { r } ^ { \prime }$ 是空间测量点到小体元 $\pmb { d M }$ 的距离.显然，要给出 $V ( x , y , z )$ 的具体表达式，就必须知道地球的质量分布规律（ $( d M$ 的表达式)和地球形状(积分限)．这个问题如何解决，正是本节讨论的内容，它将涉及球函数，下面先作一简单介绍.

# 1．球函数简介

球函数是从求解拉普拉斯方程

$$
\Delta u = \frac { { \partial } ^ { 2 } u } { { \partial } x ^ { 2 } } + \frac { { \partial } ^ { 2 } u } { { \partial } y ^ { 2 } } + \frac { { \partial } ^ { 2 } u } { { \partial } z ^ { 2 } } = 0
$$

中引出的，这里的 $\Delta$ 称为拉普拉斯算子， $\pmb { \mathscr { u } }$ 是 $( x , y , z )$ 的函数．为了给出方程(5.4)的解，改用一般正交曲线坐标系，由相应的三个曲线坐标 $q _ { 1 } , q _ { 2 } , q _ { 3 }$ 来代替直角坐标 $x , y , z ;$

$$
x = \varphi ( q _ { 1 } , q _ { 2 } , q _ { 3 } ) , y = \psi ( q _ { 1 } , q _ { 2 } , q _ { 3 } ) , z = \omega ( q _ { 1 } , q _ { 2 } , q _ { 3 } ) .
$$

若记

$$
\left. \begin{array} { c } { { H _ { 1 } ^ { 2 } { = } \displaystyle { \left( \frac { \partial \varphi } { \partial q _ { 1 } } \right) ^ { 2 } } { + } { \left( \frac { \partial \psi } { \partial q _ { 1 } } \right) ^ { 2 } } { + } { \left( \frac { \partial \omega } { \partial q _ { 1 } } \right) ^ { 2 } } , } } \\ { { H _ { ~ 2 } ^ { 2 } { = } { \left( \frac { \partial \varphi } { \partial q _ { 2 } } \right) ^ { 2 } } { + } { \left( \frac { \partial \psi } { \partial q _ { 2 } } \right) ^ { 2 } } { + } { \left( \frac { \partial \omega } { \partial q _ { 2 } } \right) ^ { 2 } } , } } \\ { { H _ { ~ 3 } ^ { 2 } { = } { \left( \frac { \partial \varphi } { \partial q _ { 3 } } \right) ^ { 2 } } { + } { \left( \frac { \partial \psi } { \partial q _ { 3 } } \right) ^ { 2 } } { + } { \left( \frac { \partial \omega } { \partial q _ { 3 } } \right) ^ { 2 } } , } } \end{array} \right\}
$$

则 $\Delta \pmb { u }$ 的表达式变为

$$
\begin{array} { r l } & { \Delta u { = } \cfrac { 1 } { H _ { 1 } H _ { 2 } H _ { 3 } } \bigg [ \cfrac { \partial } { \partial q _ { 1 } } \bigg ( \cfrac { H _ { 2 } H _ { 3 } } { H _ { 1 } } \cfrac { \partial u } { \partial q _ { 1 } } \bigg ) { + } \cfrac { \partial } { \partial q _ { 2 } } \bigg ( \cfrac { H _ { 3 } H _ { 1 } } { H _ { 2 } } \cfrac { \partial u } { \partial q _ { 2 } } \bigg ) } \\ & { \qquad + \cfrac { \partial } { \partial q _ { 3 } } \bigg ( \cfrac { H _ { 1 } H _ { 2 } } { H _ { 3 } } \cfrac { \partial u } { \partial q _ { 3 } } \bigg ) \bigg ] , } \end{array}
$$

于是曲线坐标系中的拉普拉斯方程为

$$
\frac { 3 } { \partial q _ { 1 } } \bigg ( \frac { H _ { 2 } H _ { 3 } } { H _ { 1 } } \frac { \partial u } { \partial q _ { 1 } } \bigg ) \dot { + } \frac { \partial } { \partial q _ { 2 } } \bigg ( \frac { H _ { 3 } H _ { 1 } } { H _ { 2 } } \frac { \partial u } { \partial q _ { 2 } } \bigg ) + \frac { \partial } { \partial q _ { 3 } } \bigg ( \frac { H _ { 1 } H _ { 2 } } { H _ { 3 } } \frac { \partial u } { \partial q _ { 3 } } \bigg ) = 0 .
$$

若用球坐标 $( r , \lambda , \varphi )$ ,有

$$
x = r \cos \varphi \cos \lambda , y = r \cos \varphi \sin \lambda , z = r \sin \varphi .
$$

代入(5.6)式可算出

$$
\begin{array} { r } { H _ { 1 } { = } 1 , H _ { 2 } { = } r \cos \varphi , H _ { 3 } { = } r , } \end{array}
$$

因此球坐标系中的拉普拉斯方程为

$$
\frac { \partial } { \partial r } \Bigl ( r ^ { 2 } \frac { \partial u } { \partial r } \Bigr ) + \frac { 1 } { \cos ^ { 2 } \varphi } \frac { \partial ^ { 2 } u } { \partial \lambda ^ { 2 } } + \frac { 1 } { \cos \varphi } \frac { \partial } { \partial \varphi } \Bigl ( \cos \varphi \frac { \partial u } { \partial \varphi } \Bigr ) = 0 .
$$

下面就来讨论这个方程的解。

方程(5.11)可用分离变量法来解，相应的解写成下列形式

$$
u \left( r , \lambda , \varphi \right) = R \left( r \right) \theta \left( \lambda \right) \varPhi \left( \varphi \right) .
$$

代入(5.11)式，即可分离为三个常微分方程：

$$
r ^ { 2 } \frac { d ^ { 2 } R } { d r ^ { 2 } } + 2 r \frac { d R } { d r } - n \left( n + 1 \right) R = 0 ,
$$

$$
\frac { d ^ { 2 } \theta } { d \lambda ^ { 2 } } + m ^ { 2 } \theta = 0 ,
$$

$$
( 1 - \mu ^ { : } ) \frac { d ^ { 2 } P } { d \mu ^ { 2 } } . . . 2 \mu \frac { d P } { d \mu } + \biggl [ n ( n + 1 ) - \frac { m ^ { 2 } } { 1 - \mu ^ { 2 } } \biggr ] P = 0 ,
$$

其中 $\mu = \sin \varphi , P ( \mu ) = \Phi \left( \varphi \right)$ ；而 $n , m = 0 , 1 , 2 , \cdots$ 是正整数（一般${ \pmb n } , { \pmb m }$ 可以是任意实数或复数，这里不予讨论)．于是拉普拉斯方程（5.11）的求解问题化为上述三个二阶线性常数分方程的求解问题，它们的解分别是

$$
r ^ { n } , r ^ { - ( n + 1 ) } ; \cos m \lambda , \sin m \lambda ; P _ { n } ^ { m } ( \mu )
$$

的线性组合．因此原拉普拉斯方程(5.11)的解就是上述函数族的线性组合，若记某一解为 ${ \bf \bar { \theta } } u _ { n } ( r , \lambda , \mu )$ ，则有

$$
u _ { n } ( r , \lambda , \mu ) = r ^ { n } y _ { n } ( \lambda , \mu ) ,
$$

$$
y _ { n } ( \lambda , \mu ) = \sum _ { m = 0 } ^ { n } P _ { m } ^ { m } ( \mu ) ( A _ { n , m } \cos m \lambda . | \cdot B _ { n , m } \sin m \lambda ) .
$$

其中 $P _ { n } ^ { n } ( \mu )$ 就是方程(5.15)的解，由下式表达

$$
P _ { n } ^ { m } ( \mu ) = ( 1 - \mu ^ { 2 } ) ^ { m / 2 } \frac { d ^ { m } P _ { n } ( \mu ) } { d \mu ^ { m } } ,
$$

$$
P _ { n } ( \mu ) = \frac { 1 } { 2 ^ { n } n ! } \frac { d ^ { n } } { d \mu ^ { n } } [ ( \mu ^ { 2 } - 1 ) ^ { n } ] .
$$

$u _ { n } ( r , \lambda , \mu )$ 称为球体函数， $y _ { n } ( \lambda , \mu )$ 称为球面函数，或简称球函数，$P _ { n } ^ { m } ( \mu )$ 称为缔合勒让德多项式， $P _ { n } ( \mu )$ 称为勒让德多项式.

$P _ { n } ^ { m } ( \mu )$ 有如下一些性质：

$$
P _ { n } ^ { m } ( \mu ) = ( - 1 ) ^ { m } \frac { \left( n + m \right) ! } { \left( n - m \right) ! } P _ { n } ^ { - m } ( \mu ) ,
$$

其模 $N _ { n } ^ { m }$ 为

$$
[ N _ { n } ^ { m } ] ^ { 2 } = \int _ { - 1 } ^ { + 1 } [ P _ { n } ^ { m } ( \mu ) ] ^ { 2 } d \mu = \frac { 2 } { 2 n + 1 } \frac { ( n + m ) ! } { ( n - m ) ! } .
$$

还有递推关系，即

$$
( n + 1 \_ m ) P _ { n + 1 } ^ { m } ( \mu ) - ( 2 n + 1 ) \mu P _ { n } ^ { m } ( \mu ) + ( n + m ) P _ { n - 1 } ^ { m } ( \mu )
$$

对于 $P _ { n } ( \mu )$ ，有类似的性质，令 $m = 0$ 即得，有

$$
[ N _ { n } ] ^ { 2 } = \frac { 2 } { 2 n + 1 } ,
$$

$\stackrel { \displaystyle } { ( n + 1 ) } P _ { n + 1 } ( \mu ) - \stackrel { \displaystyle ( 2 n + 1 ) } { ( 2 n + 1 ) } \mu P _ { n } ( \mu ) + n P _ { n - 1 } ( \mu ) = 0 .$ (5.另外,它又是函数 $( 1 - 2 \mu t + t ^ { 2 } ) ^ { - 1 / 2 }$ 对 $t ( t < 1 )$ 展开的系数，即

$$
( 1 - 2 \mu t + t ^ { 2 } ) ^ { - 1 / 2 } { = } \sum _ { n = 0 } ^ { \infty } P _ { n } ( \mu ) t ^ { n } .
$$

# 2．地球引力场位函数的一般表达式

由于地球在自转，又并非旋转对称体，故空间任一固定点的地球引力位都要随时间变化。为此，必须在地固坐标系中讨论这一问题．用球坐标 $( r , \lambda , \varphi ) , r$ 是地心向径, $\lambda , \phi$ 是地心经纬度，则地球引力场位函数(对地球外任一点)由(5.3)式表达:

$$
V ( r , \lambda , \varphi ) = \int \int \limits _ { 0 } ^ { \infty } \frac { d \cal { d } \cal { M } } { r ^ { \prime } }
$$

小体元dM的直角坐标记为(,n,s)，到地心(坐标原点)的距离为p,则小体元到空间点(r,,φ)的距离r为

$$
\begin{array} { c } { { r ^ { \prime 2 } = ( x - \xi ) ^ { 2 } + ( y - \eta ) ^ { 2 } + ( z - \xi ) ^ { 2 } } } \\ { { { } } } \\ { { = r ^ { 2 } + \rho ^ { 2 } - 2 r \rho C . } } \end{array}
$$

其中

$$
C = \frac { r \cdot \rho } { r \rho } { = } \frac { x \xi + y \eta + z \xi } { r \rho } .
$$

由C的这一定义可知，除小体元的坐标外，它是空间点λ，的函数.

现在来处理引力位V(r,,𝜑)的积分，因p<r，根据(5.25)式， $1 / r ^ { \prime }$ 可展为

$$
{ \frac { 1 } { r ^ { \prime } } } { = } ( r ^ { 2 } { + } \rho ^ { 2 } { - } 2 r \rho C ) ^ { - 1 / 2 } { = } { \frac { 1 } { r } } { \sum _ { n = 0 } ^ { \infty } } \biggl ( { \frac { \rho } { r } } \biggr ) ^ { n } P _ { n } ( C ) .
$$

${ \pmb { P } } _ { \pmb { n } } ( C )$ 即 $a$ 的 $\pmb { \mathscr { n } }$ 阶勒让德多项式，有

$$
\begin{array} { r } { P _ { 0 } ( C ) = 1 , P _ { 1 } ( C ) = C . } \end{array}
$$

将这些结果一并代人V(r,,)的积分表达式，得

$$
V ( r , \lambda , \varphi ) = \{ \{ \{ \begin{array} { l l } { { \displaystyle { \frac { G } { r } } \bigg [ 1 + ( \frac { \rho } { r } ) C + \sum _ { n = 2 } ^ { \infty } ( \frac { \rho } { r } ) ^ { n } P _ { n } ( C ) \bigg ] } \ d M . }  \end{array}  
$$

由于坐标原点是地心(即质心),因此有

$$
\frac { G } { r ^ { 2 } } \bigg [ \int \int \rho C d M = \frac { G } { r ^ { 3 } } \bigg \{ \int \bigg [ ( x \xi + y \eta + z \xi ) d M = 0 .
$$

于是

$$
V ( r , \lambda , \varphi ) = \frac { G } { r } \biggl \{ \biggr \} \biggr \} d M + \sum _ { n = 2 } ^ { \infty } \frac { G } { r ^ { n + 1 } } \biggl \{ \biggr \} \biggr \{ \rho ^ { n } P _ { n } ( C ) d M .
$$

其中第一个积分 $\int \int d M = M$ ，这是地球的总质量。下面讨论第二个积分.

容易证明 ${ \pmb { P } } _ { n } \{ { \pmb { C } } \}$ 是球函数，即 $r ^ { \mathfrak { n } } P _ { \mathfrak { n } } ( C )$ 满足拉普拉斯方程

$$
( \frac { \partial ^ { 2 } } { \partial x ^ { 2 } } + \frac { \partial ^ { 2 } } { \partial y ^ { 2 } } + \frac { \partial ^ { 2 } } { \partial z ^ { 2 } } ) r ^ { n } P _ { n } ( C ) = 0 .
$$

因

$$
\begin{array} { r l r } & { } & { \frac { \sigma } { \partial x } r ^ { n } P _ { n } ( C ) = n r ^ { n - 2 } x P _ { n } ( C ) + r ^ { n } \frac { \sigma } { \partial x } P _ { n } ( C ) , } \\ & { } & \\ & { } & { \frac { \partial ^ { 2 } } { \partial x ^ { 2 } } r ^ { n } P _ { n } \left( C \right) = n r ^ { n - 2 } P _ { n } ( C ) + n ( n - 2 ) r ^ { n - 4 } x ^ { 2 } P _ { n } ( C ) } \\ & { } & \\ & { } & { \qquad + 2 n r ^ { n - 2 } x \frac { \partial } { \partial x } P _ { n } ( C ) + r ^ { n } \frac { \partial ^ { 2 } } { \partial x ^ { 2 } } P _ { n } ( C ) , } \end{array}
$$

且根据 $c$ 的表达式(5.28)有

$$
\frac { \partial } { \partial x } = \frac { \partial C } { \partial x } \frac { d } { d C } , \frac { \partial ^ { 2 } } { \partial x ^ { 2 } } = \frac { \partial ^ { 2 } C } { \partial x ^ { 2 } } \frac { d } { d C } + \left( \frac { \partial C } { \partial x } \right) ^ { 2 } \frac { d ^ { 2 } } { d C ^ { 2 } }
$$

对 $y$ 和 $\pmb { z }$ 亦有类似情况，故

$$
\displaystyle { \left. \frac { \partial ^ { 2 } } { \partial x ^ { 2 } } + \frac { \partial ^ { 2 } } { \partial y ^ { 2 } } + \frac { \partial ^ { 2 } } { \partial z ^ { 2 } } \right. } \boldsymbol { r } ^ { n } \boldsymbol { P } _ { n } ( C ) = n ( n + 1 ) r ^ { n - 2 } \boldsymbol { P } _ { n } \left( C \right)
$$

$$
\begin{array} { r l } & { + n r ^ { n - 2 } \bigg ( x \frac { \partial C } { \partial x } + y \frac { \partial C } { \partial y } + z \frac { \partial C } { \partial z } \bigg ) \frac { d P _ { n } ( C ) } { d C } } \\ & { + { r ^ { n } } \bigg ( \frac { \partial ^ { 2 } C } { \partial x ^ { 2 } } + \frac { \partial ^ { 2 } C } { \partial y ^ { 2 } } + \frac { \partial ^ { 2 } C } { \partial z ^ { 2 } } \bigg ) \frac { d P _ { n } ( C ) } { d C } } \\ & { + { r ^ { n } } \bigg [ \bigg ( \frac { \partial C } { \partial x } \bigg ) ^ { 2 } + \bigg ( \frac { \partial C } { \partial y } \bigg ) ^ { 2 } + \bigg ( \frac { \partial C } { \partial z } \bigg ) ^ { 2 } \bigg ] \frac { d ^ { 2 } P _ { n } ( C ) } { d C ^ { 2 } } } \end{array}
$$

但根据 $\pmb { c }$ 有

$$
\begin{array} { l } { \displaystyle \frac { \partial C } { \partial x } = - \frac { x } { r ^ { 2 } } C + \frac { \xi } { r \rho } , } \\ { \displaystyle \frac { \partial C } { \partial y } = - \frac { y } { r ^ { 2 } } C + \frac { \eta } { r \rho } , } \end{array}
$$

$$
\begin{array} { c } { { \displaystyle \frac { \partial C } { \partial z } = - \frac { z } { r ^ { 2 } } C + \frac { \xi } { r \rho } , } } \\ { { \displaystyle \frac { \partial ^ { 2 } C } { \partial x ^ { 2 } } = 2 \frac { x ^ { 2 } } { r ^ { 4 } } C - \frac { 1 } { r ^ { 2 } } C - \frac { x } { r ^ { 2 } } \frac { \partial C } { \partial x } - \frac { x \xi } { r ^ { 3 } \rho } , } } \\ { { \displaystyle \frac { \partial ^ { 2 } C } { \partial y ^ { 2 } } = 2 \frac { y ^ { 2 } } { r ^ { 4 } } C - \frac { 1 } { r ^ { 2 } } C - \frac { y } { r ^ { 2 } } \frac { \partial C } { \partial y } - \frac { y \eta } { r ^ { 3 } \rho } , } } \end{array}
$$

$$
\frac { \partial ^ { 2 } C } { \partial z ^ { 2 } } = 2 \frac { z ^ { 2 } } { r ^ { 4 } } C - \frac { 1 } { r ^ { 2 } } C - \frac { z } { r ^ { 2 } } \frac { \partial C } { \partial z } - \frac { z \xi } { r ^ { 3 } \rho } .
$$

于是可得

$$
x \frac { \partial C } { \partial x } + y \frac { \partial C } { \partial y } + z \frac { \partial C } { \partial z } { = } 0 ,
$$

$$
\frac { \partial ^ { 2 } C } { \partial x ^ { 2 } } + \frac { \partial ^ { 2 } C } { \partial y ^ { 2 } } + \frac { \partial ^ { 2 } C } { \partial z ^ { 2 } } = - \frac { 2 C } { r ^ { 2 } } ,
$$

$$
\left( \frac { \partial C } { \partial x } \right) ^ { 2 } + \left( \frac { \partial C } { \partial y } \right) ^ { 2 } + \left( \frac { \partial C } { \partial z } \right) ^ { 2 } = \frac { 1 } { r ^ { 2 } } ( 1 - C ^ { 2 } ) .
$$

因此有

$$
\begin{array} { l } { { { \displaystyle { \left( \frac { \partial ^ { 2 } } { \partial x ^ { 2 } } + \frac { \partial ^ { 2 } } { \partial y ^ { 2 } } + \frac { \partial ^ { 2 } } { \partial z ^ { 2 } } \right) } r ^ { n } P _ { n } ( C ) } } } \\ { { { \mathrm { } } } } \\ { { { \displaystyle { = r ^ { n - 2 } \left[ n ( n + 1 ) P _ { n } \left( C \right) - 2 C \frac { d P _ { n } ( C ) } { d C } + ( 1 - C ^ { 2 } ) \frac { d ^ { 2 } P _ { n } ( C ) } { d C ^ { 2 } } \right] } . } } } \end{array}
$$

右端括号内正是勒让德多项式Pn(C)应满足的线性方程(5.15)的左端（对应m=0)，这就证得了所需的结论：r"Pn(C）满足方程(5.30).

根据上一段的讨论可知,在球坐标系中,按C的定义应有

$$
P _ { n } \left( C \right) = y _ { n } \left( \lambda , \mu \right) ,
$$

μ=sin𝜑,yn(λ,μ)由(5.17)式表达．于是(5.29)式变为

$$
\begin{array} { l } { { V = \displaystyle \frac { G M } { r } + \sum _ { n = 2 } ^ { \infty } \displaystyle \frac { G } { r ^ { n + 1 } } \int \left. \int \rho ^ { n } \sum _ { m = 0 } ^ { \infty } P _ { n } ^ { m } ( \mu ) \left( A _ { n , m } ^ { \prime } \cos m \lambda \right. \right. } } \\ { { \left. \left. + B _ { n , m } ^ { \prime } \sin m \lambda \right) d M . \right.}  } \end{array}
$$

这里 $A _ { n } ^ { \prime } , _ { m }$ 和 $B _ { n } ^ { \prime } , _ { m }$ 仅与小体元的坐标 $( \xi , \eta , \xi )$ 有关。显然，由于地球形状和密度分布规律不知，这一积分无法积出，但可写成下列形式

$$
\begin{array} { c } { { \displaystyle { V = \frac { G M } { r } \bigg [ 1 + \sum _ { n = 2 } ^ { \infty } \sum _ { m = 0 } ^ { n } \bigg ( \frac { a _ { e } } { r } \bigg ) ^ { n } P _ { \pi } ^ { m } ( \mu ) \left( A _ { n , m } \cos m \lambda \right. } } } \\ { { \left. + B _ { n , m } \sin m \lambda \right) \big ] _ { - } } } \end{array}
$$

其中 ${ \pmb { a } } _ { e }$ 取为地球赤道半径(具体地说是参考椭球体的赤道半径)，系数 $A _ { n } , _ { m }$ 和 $B _ { n \leq m }$ 是与地球形状和密度分布有关的常数．(5.31)式就是地球引力场位函数的一般形式，导出过程中对形状和密度分布未作任何假定，因此，亦适用于其它与地球类似的天体.

由(5.31)式可知，地球引力场位函数的一般形式 $V$ 与质点引力位函数 $V _ { 0 }$ 之差就是该式右端括号中的第二项，此即摄动函数$R$ ，有

$$
\begin{array} { r l } & { \ R { = } V { - } V _ { 0 } } \\ & { \ { = } \frac { G M } { r } \displaystyle \sum _ { n = 2 } ^ { \infty } \displaystyle \sum _ { m = 0 } ^ { n } \biggl ( \frac { a _ { e } } { r } \biggr ) ^ { n } P _ { n } ^ { m } ( \mu ) \left( A _ { n , m } \cos m \lambda \right. } \\ & { \qquad \quad \left. + B _ { n , m } \sin m \lambda \right) . } \end{array}
$$

因此，地球是否能看成质点，将取决于两个因素：一是地球形状不规则和密度不均匀的程度，这由两个参数 $A _ { n , m }$ 和 $B _ { n , m }$ 的大小来体现；另一个因素即引力场中测量点(亦即人造卫星)到地心的距离 $r _ { \perp }$ ，离地球愈远，上述影响愈不明显。参数 $A _ { n , m }$ 和 $B _ { n , m }$ 是确定的，因此，地球能否看成质点就取决于卫星离地球的远近以及问题要求的精度.

# 3．位函数的常用形式及有关参数

（1）带谐项和田谐项由 $\mathbf { \nabla } \cdot \mathbf { \vec { V } }$ 的表达式(5.31)可以看出，地球非均匀部分包含两种性质完全不同的项：一种对应于 $\pmb { m } = 0$ ，此时$\cdot \ s i n m \lambda = 0 ,$ $\cos m \lambda = 1$ ，这种项显然与经度 $\lambda$ 无关;而另一种则对应

于 $m = 1 , 2 , \cdots , n ,$ 依赖经度 $\lambda$ ，既然性质不同，就把它们分开，于是可写成

$$
V = { \frac { G M } { r } } { \left[ 1 + \sum _ { n = 2 } ^ { \infty } C _ { n } \left( { \frac { a _ { e } } { r } } \right) ^ { n } P _ { n } \left( \sin \varphi \right) \right. }
$$

$$
+ \sum _ { n = 2 } ^ { \infty } \sum _ { m = 1 } ^ { n } \bigg ( \frac { a _ { e } } { r } \bigg ) ^ { n } P _ { n } ^ { m } ( \sin \varphi ) \left( A _ { n , m } \cos \varphi \frac { \ l } { 4 } + B _ { n , m } \sin m \lambda \right) ,
$$

$$
\vec { C } _ { n } = A _ { n } , _ { 0 } .
$$

为了方便,与 $\lambda$ 有关的项常以另一种形式表达,即

$A _ { n , m } \cos m \lambda + B _ { n , m } \sin m \lambda = C _ { n , m } \cos m ( \lambda - \lambda _ { n , m } ) = C _ { n \mathrm { ~ } m } \cos m \bar { \lambda } ,$ 其中

$$
\left. \begin{array} { l } { { C _ { n , m } = ( A _ { n } ^ { 2 } , _ { m } + B _ { n , m } ^ { 2 } ) ^ { \cdot 1 / 2 } , } } \\ { { \phantom { m } } } \\ { { m \lambda _ { n , m } = \mathrm { t g } ^ { - 1 } \Big ( \frac { B _ { n , m } } { A _ { n , m } } \Big ) , } } \\ { { \phantom { m } } } \\ { { \bar { \lambda } = \lambda - \lambda _ { n , m } . } } \end{array} \right\}
$$

于是(5.33)式又可写成下列形式

$$
V = { \frac { G M } { r } } \biggl [ 1 + \sum _ { n = 2 } ^ { \infty } C _ { n } \biggl ( { \frac { a _ { e } } { r } } \biggr ) ^ { n } P _ { n } \left( \sin \varphi \right)
$$

$$
+ \sum _ { n = 2 } ^ { \infty } \sum _ { m = 1 } ^ { n } C _ { n } , _ { m } \Big \langle \frac { a _ { e } } { r } \Big \rangle ^ { n } P _ { n } ^ { m } ( \sin \varphi ) \cos { m } \overline { { { \lambda } } } \Big ] ,
$$

或

$$
V = { \frac { G M } { r } } { \left[ 1 - \sum _ { n = 2 } ^ { \infty } J _ { n } \left( { \frac { a _ { e } } { r } } \right) ^ { n } P _ { n } \left( \sin \varphi \right) \right. }
$$

$$
- \sum _ { n = 2 } ^ { \infty } \sum _ { m = 1 } ^ { n } J _ { n } , _ { m } \biggl ( \frac { a _ { e } } { r } \biggr ) ^ { n } P _ { n } ^ { m } ( \sin \varphi ) \cos { m } \mathcal { \bar { \Lambda } } \rvert ,
$$

其中

$$
{ \pmb J } _ { n } = - { \pmb C } _ { n } , \quad { \pmb J } _ { n , m } = - { \pmb C } _ { n , m } .
$$

若引用第一章中提出的标准计算单位,则(5.37)式变为

$$
V = \frac { 1 } { r } \biggl [ 1 - \sum _ { n = 2 } ^ { \infty } \frac { J _ { n } } { r ^ { n } } P _ { n } \left( \sin \varphi \right)
$$

$$
- \sum _ { n = 2 } ^ { \infty } \sum _ { m = 1 } ^ { n } \frac { J _ { n } , _ { m } } { r ^ { n } } P _ { n } ^ { m } ( \sin \varphi ) \cos { m \bar { \lambda } } ] .
$$

上述两种项分别称为带谐项和田谐项，相应的 $A _ { n , 0 }$ （即 $C _ { n }$ 或$\pmb { J } _ { \pmb { n } . }$ 称为带谐系数，而 $A _ { n \cdot m }$ 和 $B _ { n 3 m } ( m { \neq } 0 )$ ，或 $C _ { n \geq m }$ 或 $J _ { n \sin }$ 称为田谐系数。也有人把 $A _ { n ; m }$ 和 $B _ { n , m }$ 中 ${ \pmb { m } } = { \pmb { n } }$ 对应的 $A _ { n } , { \mathfrak { n } }$ 和 $B _ { n } , _ { n }$ 称为扇谐系数，相应的项称为扇谐项.

讨论人造卫星运动时，是采用历元地心赤道坐标系，而不是采用地固坐标系.那么，由于地球自转,位函数(5.39)式中的 $\bar { \lambda }$ 将引进时间 $\pmb { t }$ ，因此，与地球自转有关的田谐项将显含 $\pmb { \ell }$ ，该项随 $\pmb { \mathscr { t } }$ 的变化是一周期变化,周期即地球自转周期,每一田谐项就相当于一个“第三体”.

仅考虑带谐项修正时，地球就相当于一个旋转对称体，其引力场位函数不显含 $\pmb { t }$ ，即

$$
V = \frac { G M } { r } \biggl [ 1 + \sum _ { n = 2 } ^ { \infty } C _ { n } \left( \frac { a _ { e } } { r } \right) ^ { n } P _ { n } \left( \sin \varphi \right) \biggr ] ,
$$

或

$$
V = \frac { G M } { r } \biggl [ 1 - \sum _ { n = 2 } ^ { \infty } J _ { n } \left( \frac { a _ { e } } { r } \right) ^ { n } P _ { n } \left( \sin \varphi \right) \biggr ] .
$$

# (2）地球引力场参数

地球引力场参数包括 $G M , a _ { e } ,$ $\pmb { \ 6 }$ (参考椭球体的扁率)以及带谐系数 $\scriptstyle { J _ { \pi } }$ 和田谐系数 $\int \limits _ { . } ^ { } n \geq m \geq$ 这些都需要测定．短短20多年来利用人造卫星测地(主要是利用卫星轨道根数的变化)给出了20多

个地球引力场模式，较著名的有史密森标准地球 SAO-SEI，II,III,79,哥达德的标准地球GEM1—10， $\mathbf { G E M L _ { 2 } }$ ，法、德合作建立的GRIM地球模型等[11-[31．例如 SA0-SEIII,给出如下参数

$$
{ \bf G M } = 3 9 8 6 0 1 . 3 { \bf k m } ^ { 3 } / { \bf s } ^ { 2 } , a _ { e } = 6 3 7 8 . 1 4 0 { \bf k m } , \epsilon = 1 / 2 9 8 . 2 5 6 ,
$$

$$
\begin{array} { l l } { { \begin{array} { l l } { { r _ { 2 } = 1 0 8 2 . 6 3 6 \times 1 0 ^ { - 6 } , } } \\ { { r _ { 4 } = - 1 . 6 1 9 \times 1 0 ^ { - 6 } , } } \end{array} } } & { { \begin{array} { l l } { { J _ { 3 } = - 2 . 5 4 0 \times 1 0 ^ { - 6 } , } } \\ { { J _ { 5 } = - 0 . 2 3 0 \times 1 0 ^ { - 6 } , } } \end{array} } } \\ { { \begin{array} { l l } { 4 _ { 2 } , _ { 2 } = 1 . 5 3 6 2 \times 1 0 ^ { - 6 } , } } \end{array} } & { { \begin{array} { l l } { { B _ { 2 } , } } \\ { { B _ { 2 } , } } \end{array} } } & { { = - 0 . 8 8 1 4 9 \times 1 0 ^ { - 6 } . } } \end{array}
$$

如果按照(5.31)式表达位函数 ${ \dot { \bar { \rho } } } { } _ { n } ^ { m } ( \sin \varphi )$ 的值对不同的 $\pmb { \mathscr { n } }$ 和$\pmb { \mathcal { M } }$ 相差可以很大，如 $P _ { 2 } ^ { \prime } { = } O ( 2 \sqrt { 2 \pi } )$ ： $P _ { 8 } ^ { \prime } { = } O ( 1 5 0 0 0 { \sqrt { 2 \pi } } )$ 、相应的系数也因此而起伏较大．为了避免这种情况，常采用正规化(或称归一化）的 $P _ { n } ^ { m }$ 来代替 $P _ { n } ^ { m } .$ ，定义如下：

$$
\begin{array} { r l r } {  { \widetilde { P _ { n } ^ { m } } ( \mu ) = P _ { n } ^ { m } ( \mu ) / N _ { n } ^ { m } } } \\ & { } & { = \sqrt { \langle 2 n + 1 \rangle \frac { ( n - m ) ! } { ( n + m ) ! } \delta } \ P _ { n } ^ { m } ( \mu ) , } \end{array}
$$

$$
\dot { \delta } = \dddot [ 2 , m \neq 0 ] { } ,
$$

注意这里引用的模 ${ \cal N } _ { n } ^ { m }$ 和前面(5.21)式给出的相差一个常数．在此定义下，位函数可写成

$$
V = \frac { G M } { r } \Bigg [ 1 + \sum _ { n = 2 } ^ { \infty } \sum _ { m = 0 } ^ { n } \bigg ( \frac { a _ { e } } { r } \bigg ) ^ { n } \overline { { P _ { n } ^ { m } } } \left( \sin \varphi \right)
$$

其中

$$
\left. \begin{array} { c } { { \widetilde { A } _ { n , m } = A _ { n , m } N _ { n } ^ { m } = A _ { n } , \displaystyle { m \bigg / \sqrt { ( 2 n + 1 ) \frac { ( n - m ) ! } { ( n + m ) ! } \delta } } , \bigg \} } } \\ { { \widetilde { B } _ { n , m } = B _ { n } , \displaystyle { m \bigg / \sqrt { ( 2 n + 1 ) \frac { ( n - m ) ! } { ( n + m ) ! } \delta } } . } } \end{array} \right\}
$$

这样一来,根据测定，除 $\stackrel { . } { \bar { A } } _ { 2 3 0 } = \overline { { C } } _ { 2 } = - \bar { J } _ { 2 }$ 的量级为 $1 0 ^ { - 3 }$ 外,其余各参数 $\overline { { A } } _ { n , m }$ 和 $\overline { { B } } _ { n , m }$ 的量级一般为 $1 0 ^ { - 8 } \mathrm { - } 1 0 ^ { - 7 }$

# 4.地球形状摄动的量级

由位函数的一般表达式可知，卫星所受到的地球作用力已不再是中心引力，它与 $r , h , \varphi$ 有关，如果地球是旋转对称体，而且卫星又在赤道面上运动，对于这种特殊情况，作用力仅与 $\pmb { \mathscr { r } }$ 有关；根据第二章的讨论,相应的动力系统是可积的．除这一特例外，至今无法给出严格解．因此只能用摄动问题来处理.

摄动函数 $\pmb { R }$ (见(5.32)式)对应的摄动力 $\pmb { F }$ 。可分成两个部分，即

$$
\pmb { F _ { z } } = \pmb { F _ { \mathrm { 1 } } } + \pmb { F _ { \mathrm { 2 } } }
$$

其中 $\pmb { F } _ { 1 }$ 仅与 $\pmb { J _ { 2 } }$ 有关，而 ${ \pmb F } _ { 2 }$ 即表示其余所有带谐项和田谐项产生的摄动力，显然有

$$
\{ F _ { 1 } \} / \{ F _ { 0 } \} = O ( J _ { 2 } )
$$

若记 $\begin{array} { r } { \varepsilon = J _ { 2 } , } \\ { \quad \varepsilon = J _ { 2 } , } \end{array}$ 作为小量的“标准”，则 $\pmb { F _ { 1 } }$ 和 $\pmb { F _ { z } }$ 分别为一阶小量和二阶小量，与之对应的摄动运动方程可写成

$$
\frac { d \sigma } { d t } = f _ { 0 } ( a ) + f _ { 1 } ( \sigma , J _ { 2 } ) + f _ { 2 } ( \sigma , t , J _ { 2 } ^ { 2 } ) ,
$$

其中 $\pmb { \mathcal { J } } _ { 2 } ^ { 2 }$ 表示 $J _ { 3 } , J _ { 4 } , \cdots , J _ { 2 , 2 , 3 } , \cdots$

# 5.2 平均根数法

根据地球引力场位函数的形式和有关参数可知，考虑地球形状摄动时,相应的摄动运动方程可以写成下列形式

$$
\frac { d \sigma } { d t } = f _ { 0 } ( a ) + f _ { 1 } ( \sigma , \varepsilon ) + f _ { 2 } ( \sigma , t , \varepsilon ^ { 2 } ) .
$$

其中

$$
\boldsymbol { \sigma } = ( a , e , i , \varOmega , \omega , M ) ^ { \tau } ,
$$

$$
f _ { 0 } ( a ) = \delta n , n = a ^ { - 8 / 2 } , \delta = ( 0 , 0 , 0 , 0 , 0 , 1 ) ^ { \tau } .
$$

而 $f _ { 1 }$ 和 $f _ { 2 }$ 均是六维向量函数，并有

$$
\left. \begin{array} { c c c } { { ( f _ { 1 } ) _ { j } = { \cal O } ( \varepsilon ) , ( f _ { 2 } ) _ { j } = { \cal O } ( \varepsilon ^ { 2 } ) , j = 1 , 2 , \cdots , 6 . } } \\ { { } } & { { } } & { { } } \\ { { \varepsilon = { \cal J } _ { 2 } } } \end{array} \right\}
$$

这里 $f _ { 1 }$ 是 $\pmb { J _ { 2 } }$ 项的贡献， $f _ { 2 }$ 则表示除 $\pmb { J _ { 2 } }$ 项外所有带谐项和田谐项对应的摄动加速度，若只考虑带谐项 ${ \pmb J } _ { \pmb { \mathscr { n } } }$ ,则相应的 $f _ { 2 }$ 不显含 $\pmb { t }$ ·

如果按上一章用摄动法求解小参数方程(5.50)，从各阶摄动$\Delta \sigma ^ { ( 1 ) } ( t ) , \Delta \sigma ^ { ( 2 ) } ( t )$ ，…的计算公式(4.93)可以看出，不仅与 $\pmb { \Omega }$ 和$\pmb { \omega }$ 有关的长周期项将变成形如 $\varepsilon ^ { 2 } n ( t - t _ { 0 } ) , e ^ { 3 } [ n ( t - t _ { 0 } ) ] ^ { 2 } .$ …的长期项，而且还会出现泊松项．将周期项变成时间间隔的幂级数这样一种解的结构是不理想的．为此，古在由秀(Kozai)于1959 年根据非线性力学中平均法的思想，针对地球形状摄动(主要带谐项$J _ { 2 } , J _ { 3 } , J _ { 4 } )$ 提出了平均根数法[41．尽管当时并没有得到完整的结果，但是作为一种方法，在以后的人卫工作中被广泛地引用．本节将以古在由秀的原始提法作为基础，对该方法作一完整的阐述.

平均根数法与摄动法的第一个不同之处在于前者是将摄动变化 $\Delta \sigma ^ { ( 1 ) } ( t ) , \Delta \sigma ^ { ( 2 ) } ( t ) , \cdots$ 中不同性质的项区分开，相应的幂级数解的形式由摄动法中的(4.90)式改为

$$
\left. \begin{array} { l } { { \sigma \left( t \right) = \sigma \left( t \right) + \left[ \sigma _ { t } ^ { \left( 1 \right) } \left( t \right) + \sigma _ { t } ^ { \left( 2 \right) } \left( t \right) + \cdots \right] + \left[ \sigma _ { s } ^ { \left( 1 \right) } \left( t \right) + \sigma _ { s } ^ { \left( 2 \right) } \left( t \right) \right] } } \\ { { \qquad \quad + \cdots \mathrm { . } } } \\ { { \sigma \left( t \right) = \overline { { { \sigma ^ { \left( 0 \right) } } } } \left( t \right) + \sigma _ { s } \left( t \right) , } } \\ { { \sigma _ { e } \left( t \right) = \sigma _ { 1 } \left( t - t _ { 0 } \right) + \sigma _ { 2 } \left( t - t _ { 0 } \right) + \cdots , } } \\ { { \overline { { { \sigma ^ { \left( 0 \right) } } } } \left( t \right) = \sigma _ { 0 } + \delta \bar { \pi } _ { 0 } \left( t - t _ { 0 } \right) , } } \\ { { \sigma _ { 0 } = \sigma _ { 0 } - \left[ \sigma _ { t } ^ { \left( 1 \right) } \left( t _ { 0 } \right) + \cdots + \sigma _ { s } ^ { \left( 0 \right) } \left( t _ { 0 } \right) + \cdots \right] . } } \end{array} \right\}
$$

其中 $\pmb { \sigma _ { c } } ( t )$ 是长期项， ${ \pmb { \sigma } } _ { 1 } = { \pmb { O } } ( { \pmb { \varepsilon } } )$ ， $\sigma _ { 2 } { = } O ( \varepsilon ^ { 2 } ) ,$ …各为一阶,二阶，…长期项系数（不要与向量 $\pmb { \sigma }$ 的分量 $\sigma _ { j }$ 相混淆)，它们是 $\bar { a } , \bar { e } , \bar { i }$ 的函数． $\sigma _ { \iota } ^ { \scriptscriptstyle ( 1 ) } ( t ) , \sigma _ { \iota } ^ { \scriptscriptstyle ( 2 ) } ( t ) , \cdot$ …各为一阶,二阶,…长周期项,其周期取决于慢变量 $\varOmega$ 和 $\omega$ (或具有慢变化的某种组合变量)的变化。而 $\pmb { \sigma } _ { \bullet } ^ { ( 1 ) }$ $( t ) , \sigma _ { s } ^ { ( 2 ) } ( t ) , \cdots$ 则为各阶短周期项，它们的周期取决于快变量 $M$ 的变化周期(亦即卫星运动周期)．仅含长期变化的 $\theta ( t )$ 就称为平均根数，相应的 $\overline { { \sigma ^ { ( 0 ) } } } ( t )$ 称为无摄平均根数， ${ \pmb { \sigma } } _ { 0 }$ 是初始（对应 $\pmb { t _ { 0 } } .$ ）平均根数，若无摄动，则有

$$
\begin{array} { l } { { \overline { { { \sigma } } } _ { 0 } = \sigma _ { 0 } , } } \\ { { \overline { { { \sigma ^ { ( 0 ) } } } } ( t ) = \sigma ^ { ( 0 ) } ( t ) = \sigma _ { 0 } + \delta n _ { 0 } ( t - t _ { 0 } ) , } } \end{array}
$$

针对上述区分不同项的处理，方程(5.50)的右函数也相应地分成三个部分：

$$
f _ { k } = f _ { k \circ } + f _ { k l } + f _ { k \circ } , \quad ( k = 1 , 2 ) .
$$

其中 $f _ { k c }$ 只与 $a , e , i$ 有关， $f _ { k \downarrow }$ 是 $\Omega$ 或 $\pmb { \omega }$ （或具有慢变化的组合变量)的周期函数， $f _ { k , g }$ 是 $M$ 的周期函数，若要使平均根数法有效地构成小参数幂级数解，则应有

$$
f _ { 1 1 } \approx 0 .
$$

对于地球形状摄动，确实满足这一条件.

方程(5.50）的幂级数解是对 $\sigma ( t )$ 展开，它代替了摄动法中对无摄运动解 ${ \pmb { \sigma } } ^ { ( 0 ) } ( t )$ 的展开，这又是一个重要差别.将形式解(5.54)代入方程(5.50）两端得

$$
\begin{array} { l } { { \displaystyle \frac { d } { d t } [ \bar { \sigma } ( t ) + \sigma _ { t } ^ { \left( 1 \right) } \left( t \right) + \sigma _ { t } ^ { \left( 2 \right) } \left( t \right) + \cdots + \sigma _ { s } ^ { \left( 1 \right) } \left( t \right) + \sigma _ { s } ^ { \left( 2 \right) } \left( t \right) + \cdots ] } } \\ { { \displaystyle } } \\ { { \displaystyle = f _ { 0 } \langle \bar { a } \rangle + \frac { \partial f _ { 0 } } { \partial a } [ a _ { s } ^ { \left( 1 \right) } + a _ { s } ^ { \left( 2 \right) } + \cdots + a _ { t } ^ { \left( 1 \right) } + a _ { t } ^ { \left( 2 \right) } + \cdots ] } } \\ { { \displaystyle \qquad + \frac { 1 } { 2 } \frac { \partial ^ { 2 } f _ { 0 } } { \partial a ^ { 2 } } [ a _ { s } ^ { \left( 1 \right) } + a _ { t } ^ { \left( 1 \right) } + \cdots ] ^ { 2 } + \cdots + f _ { 1 } \left( \sigma , \varepsilon \right) } } \\ { { \displaystyle \qquad + \sum _ { j } \frac { \partial f _ { j } } { \partial \sigma _ { j } } [ \sigma _ { s } ^ { \left( 1 \right) } + \sigma _ { t } ^ { \left( 1 \right) } + \cdots ] _ { j } } } \end{array} .
$$

$$
+ \frac { 1 } { 2 } \sum _ { j } \sum _ { \pm } \frac { \partial ^ { 2 } f _ { 1 } } { \partial \sigma _ { j } \partial \sigma _ { \pm } } [ \sigma _ { \pm } ^ { ( 1 ) } + \sigma _ { l } ^ { ( 1 ) } + \cdots ] _ { j } [ \sigma _ { \pm } ^ { ( 1 ) } \div \sigma _ { l } ^ { ( 1 ) } + \cdots ] _ { k }
$$

$$
+ ^ { . . . . } + f _ { 2 } ( \sigma , t , \varepsilon ^ { 2 } ) + \sum _ { j } \frac { \partial f _ { 2 } } { \partial \sigma _ { i } } \lbrack \sigma _ { s } ^ { ( 1 ) } + \sigma _ { i } ^ { ( 1 ) } + \cdots \rbrack + \cdots ,
$$

该式右端各项中出现的根数均应取 $\pmb { \mathcal { O } } ( t )$ ．比较展开式两端同次 幂 $( \varepsilon ^ { l } )$ 的系数得

$$
\widehat { \pmb { \sigma } ^ { ( 0 ) } } ( t ) = \pmb { \sigma } _ { 0 } + \int _ { t _ { 0 } } ^ { t } \delta \bar { n } d t = \pmb { \sigma } _ { 0 } + \delta \bar { n } _ { 0 } ( t - t _ { 0 } ) ,
$$

$$
\sigma _ { 1 } ( t - t _ { 0 } ) = \int _ { t _ { 0 } } ^ { t } [ f _ { 1 e } ] _ { \sigma } d t ,
$$

$$
\sigma _ { s } ^ { \scriptscriptstyle ( 1 ) } \left( t \right) = \int ^ { t } \biggl [ \delta \frac { \partial n } { \partial a } a _ { s } ^ { \scriptscriptstyle ( 1 ) } + f _ { 1 s } \biggr ] _ { \sigma } d t ,
$$

$$
\sigma _ { 2 } ( t - t _ { 0 } ) = \int _ { t _ { 0 } } ^ { t } \left[ \delta \frac { 1 } { 2 } \frac { \partial ^ { 2 } n } { \partial a ^ { 2 } } ( a _ { s } ^ { \scriptscriptstyle ( 1 ) } ) _ { \sigma } ^ { 2 } + \left( \sum _ { j } \frac { \partial f _ { 1 } } { \partial \sigma _ { j } } ( \sigma _ { s } ^ { \scriptscriptstyle ( 1 ) } ) _ { j } \right) _ { o } + f _ { 2 e } \right] _ { \overline { { \sigma } } } d t
$$

$$
\sigma _ { \iota } ^ { ( 1 ) } \left( \iota \right) = \int ^ { \iota } \left[ \delta \frac { \partial \iota } { \partial \boldsymbol { a } } a _ { \iota } ^ { ( 2 ) } + \delta \frac { 1 } { 2 } \frac { \partial ^ { 2 } \boldsymbol { n } } { \partial \boldsymbol { a } ^ { 2 } } \left( a _ { s } ^ { ( 1 ) } \right) _ { \iota } ^ { 2 } \right.
$$

$$
+ \bigg ( \sum _ { j } \frac { \partial f _ { 1 } } { \partial \sigma _ { j } } ( \sigma _ { s } ^ { ( 1 ) } + \sigma _ { l } ^ { ( 1 ) } ) _ { j } \bigg ) _ { l } + f _ { 2 l } \int _ { \overline { { \sigma } } } d t ,
$$

$$
\sigma _ { s } ^ { \left( 2 \right) } \left( t \right) = \int ^ { t } \left[ \delta \frac { \partial n } { \partial a } a _ { s } ^ { \left( 2 \right) } + \delta \frac { 1 } { 2 } \frac { \partial ^ { 2 } n } { \partial a ^ { 2 } } { \left( a _ { s } ^ { \left( 1 \right) } \right) } _ { s } ^ { 2 } \right.
$$

$$
+ \Bigl ( \sum _ { j } \frac { \mathcal { I } f _ { 1 } } { \tilde { \sigma } \sigma _ { j } } ( \sigma _ { s } ^ { ( 1 ) } + \sigma _ { l } ^ { ( 1 ) } ) _ { j } \Bigr ) _ { s } + f _ { 2 s } \biggl ] _ { \overline { { { \sigma } } } } d t ,
$$

关于上述计算各阶摄动的方法需要说明几点：

(1）对于保守力情况,a,e,i无长期项，故(5.58)式中的n=.$\overline { { \pmb { { \mathscr { R } } } } } _ { 0 }$ ，否则(例如大气阻力摄动)有

$$
\bar { n } = \bar { n } _ { 0 } + n _ { c } ( t ) ,
$$

(5.58)式将增加一项，即

$$
\int _ { t _ { 0 } } ^ { t } \delta n _ { c } ( t ) d t .
$$

不仅如此，(5.59)-(5.63)式中都有类似问题，解的结构将复杂化．尽管这不影响级数解的构造，但解的形式不再象(5.54)式那么简单. +

(2）对于长周期项，其变化取决于慢变量，例如 $\omega$ ，有 ${ \mathfrak { D } } = { \mathfrak { D } } _ { \mathfrak { d } }$ $+ \omega _ { 1 } ( t - t _ { 0 } ) , \omega _ { 1 } = { \cal O } ( \varepsilon )$ 是一阶小量，不象 $\mathcal { M }$ 的变化速度 $\pmb { n } = \pmb { O } ( \pmb { \varepsilon } ^ { 0 } )$ ·因此,若 $f _ { 1 2 } = \varepsilon \cos \omega _ { 3 }$ 将有

$$
\int ^ { t } f _ { 1 l } d t = \int ^ { t } \varepsilon \cos \varpi d t = \frac { \varepsilon \sin \varpi } { \omega _ { 1 } } = A \sin \varpi ,
$$

这里 $A { = } O ( \varepsilon ^ { 0 } )$ ，故上述积分给出的不是一阶长周期项，而是零阶长周期项．与此类似， $\pmb { f _ { 2 l } }$ 给出的将是一阶长周期项，…，积分一次降一阶．故要使级数解能构成，一方面要求条件(5.56)式成立，而且 $f _ { \kappa l } \left( \sigma , t , \varepsilon ^ { k } \right)$ 产生的长周期项是 $( k - 1 )$ 阶，即

$$
\sigma _ { l } ^ { ( k - 1 ) } ( t ) = \int ^ { t } f _ { k l } \left( \sigma , t , \varepsilon ^ { k } \right) d t .
$$

这就是(5.62)式 $\pmb { \sigma } _ { \ell } ^ { ( 1 ) } ( t )$ 的写法．另外， $a _ { i } ^ { ( 1 ) } \left( t \right) = 0 i$ （这在后面将会给出证明),否则其效果与 $f _ { 1 l } { \neq } 0$ 相当.

（3）展开“点”（即参考解） $\sigma ( t )$ 与摄动法中的无摄根数${ \pmb \sigma } ^ { ( 0 ) } ( t )$ 不同， $\pmb { \sigma } ( t )$ 是在求解过程中同时形成的，但它不影响上述级数解的构造。例如

$$
\int \cos { \varpi } d t = \frac { \sin { \varpi } } { ( \omega _ { 1 } + \omega _ { 2 } + \cdots ) } ,
$$

其中 $\omega _ { 1 3 } \omega _ { 2 3 } \cdots$ 是各阶长期项系数，积分时不必知道它的具体形式只是在推出后引用该公式计算时才可能用到.

根据上述讨论，在一定条件下，平均根数法可以有效地构成摄动运动方程(5.50)的小参数幂级数解(5.54)式，它将保持各类摄动项的性质，而不会象摄动法中那样将周期项构造成一个时间间隔的幂级数，特别对于保守力情况，还避免了泊松项的出现．这些都是平均根数法的优点，当然，平均根数法也有它自身的缺陷，这将在下一节中结合具体问题加以说明.

对于一个具体问题,在一定精度要求下,相应的小参数幂级数解,只要取到足够多项即行。为此,引进各阶摄动解的概念,即

一阶摄动解(简称一阶解)：取到所有的一阶摄动项(包括长期、长周期和短周期)和二阶长期项.

二阶摄动解(简称二阶解)：取到所有的二阶摄动项和三阶长期项.

以下类推．这与讨论自然天体轨道变化时的提法稍有差别，对长期项的要求高一阶．其原因在于对人造地球卫星而言，运动较快，近地卫星一天就绕地球转10多圈，10天左右即有

$$
\begin{array} { r } { n ( t - t _ { 0 } ) = O ( 1 / \varepsilon ) . } \end{array}
$$

因此,二阶长期项的量级将与一阶周期项差不多，这才引起上述提法.至于在具体问题中，到底取到哪一项，这要看精度要求和相应的时间间隔有多长.对于一阶解如果计算弧段n(t一to)=10，则可满足10-5的精度(相当于地面定位精度在100m以内）.

# $\ S 5 . 3$ 主要带谐项 $( J _ { 2 } , J _ { 3 }$ 和 $J _ { \frac { 1 } { 4 } } )$ 的摄动解

J,J,J三项是地球引力场位函数展开式中的低阶带谐项(或长波项)．对于精度要求不高的问题，地球不均匀性的修正只需考虑这三项就够了，常把它们称为主要带谐项．特别是J2项，它表明地球为一扁球体(扁旋转椭球体)，这是一个很好的近似.$\pmb { J _ { 2 } }$ 与地球几何扁率 $\pmb { \epsilon }$ 有如下近似关系：

$$
J _ { 2 } { = } \frac { 2 } { 3 } \bigg ( \epsilon { - } \frac { 1 } { 2 } n _ { e } ^ { 2 } \bigg ) { + } O ( \epsilon ^ { 2 } ) .
$$

其中n。是地球自转角速度,这里用了标准计算单位。

通过对上述三项摄动解的讨论，可以全面地了解平均根数法的具体用法,下面将在一阶意义下构造相应的幂级数解。

# 1．摄动函数及其分解

由(5.39)式给出 $J _ { 2 } , J _ { 8 }$ 和 ${ \pmb J } _ { 4 }$ 三项的摄动函数为

$$
\begin{array} { r l r } {  { R = - \frac { J _ { 2 } } { r ^ { 3 } } P _ { 2 } ( \sin \varphi ) \cdots \frac { J _ { 3 } } { r ^ { 4 } } P _ { 3 } ( \sin \varphi ) \cdots \frac { J _ { 4 } } { r ^ { 5 } } P _ { 4 } ( \sin \varphi ) } } \\ & { } & { = - \frac { J _ { 2 } } { r ^ { 3 } } \Big ( \frac { 3 } { 2 } \sin ^ { 2 } \varphi - \frac { 1 } { 2 } \Big ) - \frac { J _ { 3 } } { r ^ { 4 } } \Big ( \frac { 5 } { 2 } \sin ^ { 3 } \varphi - \frac { 3 } { 2 } \sin \varphi \Big ) } \\ & { } & { \quad - \frac { J _ { 4 } } { r ^ { 5 } } \Big ( \frac { 3 5 } { 8 } \sin ^ { 4 } \varphi - \frac { 1 5 } { 4 } \sin ^ { 2 } \varphi + \frac { 3 } { 8 } \Big ) . \qquad ( 5 } \end{array}
$$

引人

$$
A _ { 2 } { = } \frac { 3 } { 2 } J _ { 2 } , A _ { 3 } { = } { - } J _ { 3 } , A _ { 4 } { = } { - } \frac { 3 5 } { 8 } J _ { 4 } ,
$$

并以

$$
\sin \varphi = \sin i \sin ( f + \omega )
$$

代人(5.66)式得

$$
\begin{array} { r l } & { R = \frac { A _ { 0 } / a } { c ^ { 3 } } \bigg [ \bigg ( \frac { 1 } { \sqrt { 3 } } - \frac { 1 } { 2 } \sin ^ { 2 } \iota \bigg ) + \frac { 1 } { 2 } \sin ^ { 2 } \iota \cos 2 ( f + \omega ) \bigg ] } \\ & { \qquad + \frac { A _ { 0 } / } { a ^ { 4 } } \bigg ( \frac { a } { \gamma } \bigg ) ^ { 4 } \sin i \left[ \left( \frac { 1 5 } { 8 } \sin ^ { 2 } \iota - \frac { 3 } { 2 } \right) \sin \left( f + \omega \right) \right. } \\ & { \qquad \left. - \frac { 5 } { 8 } \sin ^ { 6 } i \sin 3 ( f + \omega ) \right] } \\ & { \qquad + \frac { A _ { 4 } / } { a ^ { 4 } } \bigg ( \frac { a } { \gamma } \bigg ) ^ { 4 } \bigg [ \bigg ( \frac { 3 } { 3 5 } - \frac { 3 } { 7 } \sin ^ { 2 } i + \frac { 3 } { 8 } \sin ^ { 4 } i \bigg ) } \\ & { \qquad \quad - \frac { 1 } { 2 } \sin ^ { 2 } i \bigg ) \sin ^ { 2 } i \cos 2 ( f + \omega ) + \frac { 1 } { 8 } \sin ^ { 4 } i \cos 4 ( f + \omega ) \bigg ] , } \end{array}
$$

从(5.69)式可知，摄动函数 $\pmb { R }$ 不显含 $\pmb { t }$ 也不含 $\Omega$ ，这也是所有带谐项的特征.

对于上述三项，方程(5.50)变为

$$
\frac { d \sigma } { d t } { = } f _ { 0 } ( a ) + f _ { 1 } ( \sigma , J _ { 2 } ) + f _ { 2 } ( \sigma , J _ { 3 } , J _ { 4 } ) ,
$$

这里取 $\varepsilon = J _ { 2 } , J _ { 3 } , J _ { 4 } { = } O ( \varepsilon ^ { 2 } )$ ，将摄动函数 $\pmb { R }$ 代入摄动运动方程(4.82)即可给出(5.70)式的具体形式。但为了用平均根数法构造级数解，还需要将 $f _ { 1 } , f _ { 2 }$ 分解成 $f _ { k \sigma } , f _ { k l }$ 和 $f _ { k \mathscr { s } } ( k { = } 1 , 2 )$ ，既然如此，先对 $\pmb { R }$ 进行分解似乎更简单些．引用第二章求平均值的方法，即可分解 $\pmb { R }$ ，首先对卫星运动(即时间 $\pmb { \mathscr { t } }$ 或平近点角 $M$ )求平均值，可将短周期项分离出，剩下的项中关于 $\pmb { \omega }$ 的周期函数部分即长周期项，这样便将 $\pmb { R }$ 分解成五个部分

$$
\begin{array} { c } { { R = R _ { c } + R _ { l } + R _ { s } } } \\ { { { } } } \\ { { = R _ { 1 e } + R _ { 2 c } + R _ { 2 l } + R _ { 1 s } + R _ { 2 s } } } \end{array}
$$

其中一、二阶长期部分 $R _ { c } = R _ { 1 o } ( J _ { 2 } ) + R _ { 2 c } ( J _ { 4 } )$ 是 $a , \enspace \pmb { \mathscr { e } } , \enspace i$ 的函数，$R _ { 1 l } = 0 , R _ { 2 l } \left( J _ { 3 } , J _ { 4 } \right)$ 是长周期部分，而 $R _ { s } = R _ { 1 s } ( J _ { 2 } ) + R _ { 2 s } ( J _ { 3 } , J _ { 4 } )$ 是一、二阶短周期部分．从 $\pmb { R }$ 的表达式(5.69)可以看出，分解过程中仅涉及形如

$$
\left( { \frac { a } { r } } \right) ^ { p } \cos q f , \ \left( { \frac { a } { r } } \right) ^ { p } \sin q f
$$

，这类函数的求平均值问题．利用第二章给出的方法或直接引用附录中的结果：

$$
\left. \begin{array} { l } { { \left( \displaystyle \frac { a } { r } \right) ^ { 3 } = ( 1 - e ) ^ { - 3 / 2 } , \left( \displaystyle \frac { a } { r } \right) ^ { 3 } \cos 2 f = 0 , } } \\ { { \left( \displaystyle \frac { a } { r } \right) ^ { 4 } \cos f = e ( 1 - e ^ { \frac { i } { 2 } } ) ^ { - 5 / 2 } , \left( \displaystyle \frac { a } { r } \right) ^ { 4 } \cos 3 f = 0 , } } \\ { { \left( \displaystyle \frac { a } { r } \right) ^ { 5 } = \left( 1 + \displaystyle \frac { 3 } { 2 } e ^ { 2 } \right) ( 1 - e ^ { 2 } ) ^ { - 7 / 2 } , } } \\ { { \left( \displaystyle \frac { a } { r } \right) ^ { 5 } \cos 2 f = - \displaystyle \frac { 3 } { 4 } e ^ { 2 } ( 1 - e ^ { 2 } ) ^ { - 7 / 2 } , \left( \displaystyle \frac { a } { r } \right) ^ { 5 } \cos 3 f = 0 , } } \\ { { \left( \displaystyle \frac { a } { r } \right) ^ { 9 } \sin 4 f = 0 , } } \end{array} \right\}
$$

便可得到(5.71)式中五个部分的具体形式

$$
\begin{array} { r l r } & { R _ { 1 c } = \displaystyle \frac { A _ { 2 } } { a ^ { 3 } } \Big ( \frac { 1 } { 3 } - \frac { 1 } { 2 } \sin ^ { 2 } i \Big ) ( 1 - e ^ { 2 } ) ^ { - 3 / 2 } , } & { ( 5 . } \\ & { R _ { 2 c } = \displaystyle \frac { A _ { 4 } } { a ^ { 6 } } \Big ( \frac { 3 } { 3 5 } - \frac { 3 } { 7 } \sin ^ { 2 } i + \frac { 3 } { 8 } \sin ^ { 4 } i \Big ) \Big ( 1 + \frac { 3 } { 2 } e ^ { 2 } \Big ) ( 1 - e ^ { 2 } ) ^ { - 7 / 2 } , } & \end{array}
$$

$$
\begin{array} { r l } {  { R _ { 2 l } = - \frac { 3 } { 4 } \frac { A _ { 3 } } { a ^ { 4 } } \sin i \bigg ( 2 - \frac { 5 } { 2 } \sin ^ { 2 } i \bigg ) ( 1 - e ^ { 2 } ) ^ { - 5 / 2 } e \sin \omega } } \\ & { + \frac { 3 } { 4 } \frac { A _ { 4 } } { a ^ { 6 } } \sin ^ { 2 } i \bigg ( \frac { 3 } { 7 } - \frac { 1 } { 2 } \sin ^ { 2 } i \bigg ) ( 1 - e ^ { 2 } ) ^ { - 7 / 2 } e ^ { 2 } \cos 2 \omega , } \end{array}
$$

$$
\begin{array} { r l } & { \qquad \cdot \ \sum ^ { i = 1 } \cdots \cdots \cdots \cdots \gamma } \\ & { \qquad \ R _ { s } \dot { \sigma } : = \ \frac { \dot { A } _ { 2 } \dot { \sigma } } { \alpha ^ { 4 } } \left\{ \frac { \partial } { \partial \mathbf { \sigma } } \sin \dot { \alpha } \dot { u } \right\} \left( 2 - \frac { \dot { \sigma } } { 2 } \sin \dot { \alpha } \dot { u } ^ { 4 } \right) \left( \left( \frac { \alpha } { \tau } \right) ^ { 4 } \sin \left( f + \omega \right) \ } \\ & { \qquad - ( 1 - \epsilon ) ^ { s } \gamma ^ { s } \epsilon \sin \omega \dot { \alpha } \right) \left| + \frac { \dot { \sigma } } { s } \sin ^ { 3 } \dot { u } ^ { 3 } \left( \frac { \alpha } { \tau } \right) ^ { s } \sin ^ { 3 } \left( f + \omega \right) \right\} } \\ & { \qquad + \frac { \dot { A } _ { 4 } \dot { \sigma } } { \alpha ^ { 4 } } \left\{ \left( \frac { \partial } { \partial \mathbf { \sigma } } - \frac { \dot { \sigma } } { 7 } \sin ^ { 2 } \dot { u } + \frac { \dot { \sigma } } { 8 } \sin ^ { 4 } \right) \int _ { \frac { \cos \alpha } { \gamma } } ^ { \infty } \left( - \left( 1 + \frac { \partial } { 2 } \epsilon ^ { s } \right) ( 1 - \epsilon ^ { s } ) ^ { - \alpha \beta } \right\} \ } \\ & { \qquad + \sin ^ { 4 } \left( \frac { \partial } { \partial \tau } - \frac { \dot { \sigma } } { 2 } \sin ^ { 2 } \dot { u } \sin ^ { 2 } \right) \left( \frac { \alpha } { \sqrt { \tau } } \right) ^ { s } \cos 2 ( f + \omega ) } \\ & { \qquad - \frac { \dot { \sigma } } { 4 } \left( 1 - \epsilon \right) ^ { - \gamma + \alpha } \epsilon ^ { s } \cos ^ { 2 } \omega \right\} } \\ & { \qquad + \frac { 1 } { 8 } \sin ^ { 4 } \left( \frac { \alpha } { \gamma } \right) ^ { s } \exp 4 ( f + \omega ) \Big \} . \qquad ( 5 \cdot 7 7 } \end{array}
$$

对于一阶解，二阶短周期部分 $R _ { 2 s }$ 是不需要的.

将 $\pmb { R }$ 的各个部分代人摄动运动方程(4.82)，就可分别给出方程(5.70)右函数的具体形式，即

$$
\begin{array} { r l } & { f _ { 0 } = \left( 0 , 0 , 0 , 0 , 0 , n \right) ^ { T } , } \\ & { f _ { 1 e } = \left( 0 , 0 , 0 , \left( f _ { 1 e } \right) _ { a } , \left( f _ { 1 e } \right) _ { o } , \left( f _ { 1 e } \right) _ { M } \right) ^ { T } , } \end{array}
$$

$$
f _ { 1 s } = ( ( c f _ { 1 s } ) _ { a , \textbf { ( } f _ { 1 s } ) _ { e } , \textbf { ( } f _ { 1 s } ) _ { i , \textbf { ( } f _ { 1 s } ) _ { a , \textbf { ( } f _ { 1 s } ) _ { o , \textbf { ( } f _ { 1 s } ) _ { M } } ) ^ { T } , } } }
$$

其中

$$
\begin{array} { r l } & { f _ { 2 c } = \left( 0 , \ : 0 , \ : 0 , \ : ( f _ { 2 c } ) _ { \ : \alpha } , \ : ( f _ { 2 c } ) _ { \ : \alpha } , \ : ( f _ { 2 c } ) _ { \ : \alpha } \right) ^ { \tau } , } \\ & { f _ { 2 l } = \left( 0 , \ : ( f _ { 2 l } ) _ { \ : e } , \ : ( f _ { 2 l } ) _ { \ : i } , \ : ( f _ { 2 l } ) _ { \ : \alpha } , \ : ( f _ { 2 l } ) _ { \ : \alpha } , \ : ( f _ { 2 l } ) _ { \ : \mathcal { M } } \right) ^ { \tau } . } \end{array}
$$

$$
\left. \begin{array} { l } { { ( f _ { 1 c } ) _ { a } = \displaystyle - \frac { { \cal A } _ { 2 } } { p ^ { 2 } } n \cos i , } } \\ { { { } } } \\ { { ( f _ { 1 c } ) _ { \it \circ } = \displaystyle \frac { { \cal A } _ { 2 } } { p ^ { 2 } } n \biggl ( 2 - \frac { 5 } { 2 } \sin ^ { 2 } i \biggr ) , } } \\ { { { } } } \\ { { ( f _ { 1 c } ) _ { \it { M } } = \displaystyle \frac { { \cal A } _ { 2 } } { p ^ { 2 } } n \biggl ( 1 - \frac { 3 } { 2 } \sin ^ { 2 } i \biggr ) \sqrt { 1 - e ^ { 2 } } . } } \end{array} \right\}
$$

$$
\begin{array} { r l } { + } & { \frac { 1 } { 2 } \sin ^ { 2 } \left( \cos 2 ( f - \omega ) \right) - \sin ^ { 2 } \left( \frac { \omega f } { f } \right) \sin 2 ( f + \omega ) \Bigr \} , } \\ & { \qquad \left( f _ { 1 } \right) \cos ^ { 2 } \left( \frac { \omega f } { \omega ^ { 2 } } \right) - \frac { \sin ^ { 2 } \left( f ^ { 2 } \right) } { 2 } \sin ^ { 2 } \left( \frac { \omega f } { f } \right) \Bigr \{ - \sin \left( f \left( \frac { \omega f } { \omega } \right) \sin ^ { 2 } \left( f \right) \right) } \\ & { \qquad \quad + \frac { 3 } { 2 } \sin ^ { 2 } \left( \omega + 2 ( f - \omega ) \right) - ( 1 - e ^ { \omega t } ) \sin ^ { 2 } \left( \frac { \omega f } { \omega } \right) \sin 2 ( f - \omega ) } \\ & { \qquad \quad \sin ^ { 2 } \left( \frac { \omega f } { f } \right) \sin 2 ( f + \omega ) \Bigr \} , } \\ & { \qquad \quad \left( f _ { 2 } \right) _ { 1 } \cos - \frac { \sin ^ { 2 } \left( f ^ { 2 } \right) } { 2 \omega ^ { 2 } \sqrt { 1 - e ^ { - \omega t } } } \sin 2 \left( \frac { \omega f } { \omega } \right) ^ { 3 } \sin 2 ( f + \omega ) , } \\ & { \qquad \quad \left( f _ { 3 } \right) _ { 2 } \cdots - \frac { \cos ^ { 2 } \left( f ^ { 2 } \right) } { 4 } \sin ^ { 2 } \left( f \right) \Bigr \{ \frac { \omega } { f } \sin ^ { 2 } \left( f + \omega \right) , } \\ & { \qquad \quad - \frac { \cos ^ { 2 } \left( f ^ { 2 } \right) } { 4 } \cos ^ { 2 } \left( f + \omega \right) \Bigr \} \textstyle , } \\ & { \qquad \quad \sin ^ { 2 } \left( f + \omega \right) \Bigr \} , } \end{array}
$$

$$
\begin{array} { r l } & { \quad + \frac { 6 4 \lambda _ { \mathrm { d } } } { \mu ^ { 2 } } e ^ { - \lambda } \ \Gamma - \lambda e ^ { - \lambda } \ \biggl \{ \Lambda ^ { 1 - \frac { \delta } { 2 } } \sin ^ { \lambda } \phi \biggr \} \biggl ( \frac { \lambda } { \tau ^ { 2 } } \biggr \} ^ { 4 } } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad }  \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad }  \\ & & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad }  \\ & & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad ( 1 - e ^ { \lambda } ) \biggr \ \biggr \{ \left( \frac { \lambda } { \tau ^ { 2 } } \biggr \right) ^ { 4 } \sin ^ { 2 } 4 e ^ { \lambda } \phi ( t + \omega ) \biggr \} \biggr \} , } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ &  \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \end{array}
$$

$$
\begin{array} { c } { { ( f _ { 2 e } ) _ { a } = - \displaystyle \frac { A _ { 4 } } { p ^ { 4 } } n \cos \bar { s } \left[ \left( \frac { 6 } { \bar { \gamma } } + \frac { 9 } { 7 } e ^ { 2 } \right) - \sin ^ { 2 } i \left( \frac { 3 } { 2 } + \frac { 9 } { 4 } e ^ { 2 } \right) \right] , } } \\ { { ( f _ { 2 e } ) _ { a } = \displaystyle \frac { A _ { 4 } } { p ^ { 4 } } n \Bigg [ \left( \frac { 1 2 } { 7 } + \frac { 2 7 } { 1 4 } e ^ { 2 } \right) - \sin ^ { 2 } i \left( \frac { 9 3 } { 1 4 } + \frac { 2 7 } { 4 } e ^ { 2 } \right) } } \\ { { + \sin ^ { 4 } i \left( \frac { 2 1 } { 4 } + \frac { 8 1 } { 1 6 } e ^ { 2 } \right) \Bigg ] , } } \\ { { ( f _ { 2 e } ) _ { M } = \displaystyle \frac { A _ { 4 } } { p ^ { 4 } } n \sqrt { 1 - e ^ { 2 } } \left[ e ^ { 2 } \left( \frac { 9 } { 1 4 } - \frac { 4 5 } { 1 4 } \sin ^ { 2 } i + \frac { 4 5 } { 1 6 } \sin ^ { 4 } i \right) \right] . } } \end{array}
$$

$$
\begin{array} { r l } { ( \widetilde { \mathcal { A } } _ { 1 1 } ) _ { 1 2 } - \hbar ^ { 2 } \frac { \theta } { 8 } \frac { \theta } { 8 } \frac { \theta } { \theta } \langle \dot { z } ( \widetilde { z } ) _ { 1 1 } \rangle = } & { } \\ { ( \dot { f } _ { 3 1 } ) _ { 2 } - \frac { \theta } { 8 } \frac { \theta } { 8 } \frac { \theta } { \theta } \left[ \frac { 3 } { 4 } \frac { \theta } { 8 } \alpha \sin ( 2 \left( \frac { \theta } { 2 } - \frac { \theta } { 2 } \sin ^ { 2 } \frac { \theta } { \theta } \right) \right] \cos ( \theta ) } & { } \\ { - \frac { \theta } { 8 } \frac { \theta } { 8 } \frac { \theta } { \theta } \left[ 1 + \alpha \sin ( 2 \sqrt { \theta } ) - \frac { 3 } { 8 } \sin ^ { 2 } \theta \right] \cos ( \theta ) } & { } \\ { ( \dot { f } _ { 1 1 } ) _ { 3 2 } - \frac { \theta } { 8 } \frac { \theta } { 8 } \frac { \theta } { 8 } \frac { \theta } { \theta } \left[ \sin ( 2 \pi \Delta \theta ) - \theta \sin ^ { 2 } \theta \right] \cos ( \theta ) } & { } \\ { ( \dot { f } _ { 2 2 } ) _ { 4 3 } - \frac { 3 } { 8 } \frac { \theta } { 8 } \frac { \theta } { \theta } \left[ \sin ( 2 \pi \Delta \theta ) - \sin ^ { 2 } \theta \right] \cos ( \theta ) } & { } \\ { ( \dot { f } _ { 3 2 } ) _ { 5 } - \frac { 3 } { 8 } \frac { \theta } { 8 } \frac { \theta } { \theta } \left[ \sin ^ { 2 } \frac { 3 } { 8 } \frac { \theta } { \theta } \right] \left( \sin ( 2 \pi \Delta \theta ) - \sin ^ { 2 } \theta \right) } & { } \\ { ( \dot { f } _ { 4 3 } ) _ { 5 } - \frac { 3 } { 8 } \frac { \theta } { 8 } \frac { \theta } { \theta } \left[ \sin ^ { 2 } \theta \right] \left( \frac { 3 } { 8 } \sin ^ { 2 } \theta \right) ( 1 - \sin ^ { 2 } \theta ) } & { } \\ { - \frac { 3 } { 8 } \cos ( 2 \pi \Delta \theta ) + \sin ^ { 2 } \theta \cos ( 2 \pi \Delta \theta ) } & { } \\  ( \sin \theta ) - \cos ( 2 \pi \Delta \theta ) + \sin ^ { 2 } \theta \cos ( 2 \pi \Delta \theta ) - \ \end{array}
$$$$
\begin{array} { r l } { ( f _ { 3 } ) { \mathbf { g } } = - \frac { \nu } { \nu } \sum _ { k = 1 } ^ { N } \frac { 1 } { \nu } \{ { \mathbf { g } } ^ { ( 1 ) } + ( - 2 \nu ) \sum _ { k = 1 } ^ { N } m _ { k } ^ { ( 1 ) } \hat { \mathbf { g } } ^ { ( 1 ) } \} \exp \alpha } & { { \mathbf { f } } _ { k } } \\ & { \quad + \frac { \lambda _ { 1 } } { \nu } \{ { \mathbf { g } } ^ { ( 2 ) } + ( - 3 \nu ) \sum _ { k = 1 } ^ { N } m _ { k } ^ { ( 1 ) } \hat { \mathbf { g } } ^ { ( 2 ) } \} \{ { \mathbf { g } } ^ { ( 3 ) } - { \mathbf { g } } ^ { ( 3 ) } \} \{ 2 { \mathbf { g } } ^ { ( 4 ) } + { \mathbf { g } } ^ { ( 2 ) } \} , } \\ { ( f _ { 3 } ) \leq - \frac { \nu } { \nu } \sum _ { k = 1 } ^ { N } \alpha f _ { 3 } \{ { \mathbf { g } } ^ { ( 1 ) } + ( - 3 \nu ) \sum _ { k = 1 } ^ { N } m _ { k } ^ { ( 1 ) } \hat { \mathbf { g } } ^ { ( 3 ) } - { \mathbf { g } } ^ { ( 3 ) } \} \exp \alpha ^ { ( 2 ) } \alpha } \\ & { \quad - \frac { \nu } { \nu } \sum _ { k = 1 } ^ { N } m _ { k } ^ { ( 1 ) } f _ { 3 } \{ { \mathbf { g } } ^ { ( 1 ) } + ( - 3 \nu ) \sum _ { k = 1 } ^ { N } m _ { k } ^ { ( 1 ) } \hat { \mathbf { g } } ^ { ( 2 ) } \} \exp \alpha + \frac { \lambda _ { 1 } ^ { ( 2 ) } } { \nu } \exp \alpha } \\ & { \quad - 5 \nu \sum _ { k = 1 } ^ { N } m _ { k } ^ { ( 1 ) } \hat { \mathbf { g } } ^ { ( 1 ) } \exp \alpha + \frac { \lambda _ { 1 } ^ { ( 2 ) } } { \nu } \exp \alpha + \frac { \lambda _ { 2 } ^ { ( 2 ) } } { \nu } \exp \alpha } \\ &  \quad \times \{ \frac { 3 } { \nu } \sum _ { k = 1 } ^ { N } m _ { k } ^ { ( 1 ) } \hat { \mathbf { f } } _ { k } ^ { ( 2 ) } - \frac { 3 } { \nu } \sum _ { k = 1 } ^ { N } m _ { k } ^  \end{array}
$$

以上各式中的n和p分别为a-3/2和a(1-e2),不要与某些公式中的整数取值相混淆.推导中涉及的af/ag和a()/a，已在第二章 $\ S 2 . 2$ 中给出.

# 2. ${ { J } _ { 2 } } , { { J } _ { 3 } } , { { J } _ { 4 } }$ 三项摄动的一阶解

将上述右函数fic，fis，fc和ft分别代入(5.59)-(5.(2)式,即可给出一阶解所需要的各摄动项，下面分别列出.

（1）一阶长期项 $\sigma _ { \mathrm { i } } ( t - \pmb { \mathrm { i } } _ { 0 } )$

$$
\begin{array}{c} \left. \begin{array} { l } { { \varepsilon _ { 1 } ( t - t _ { 0 } ) = 0 , e _ { 1 } ( t - t _ { 0 } ) = 0 , i _ { 1 } ( t - t _ { 0 } ) = 0 , } } \\ { { \mathcal { Q } _ { 1 } ( t - t _ { 0 } ) = - \frac { A _ { 2 } } { \overline { { p } } ^ { 2 } } \bar { n } \cos { i } \left( t - t _ { 0 } \right) , } } \\ { { \quad \quad \omega _ { 1 } ( t - t _ { 0 } ) = \frac { A _ { 2 } } { \overline { { p } } ^ { 2 } } \bar { n } \bigg ( 2 - \frac { 5 } { 2 } \sin ^ { 2 } { \tilde { \imath } } \bigg ) \left( t - t _ { 0 } \right) , } } \\ { { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } } \\ { { M _ { 1 } ( t - t _ { 0 } ) = \frac { A _ { 2 } } { \overline { { p } } ^ { 2 } } \bar { n } \left( 1 - \frac { 3 } { 2 } \sin ^ { 2 } { \tilde { \imath } } \right) \sqrt { 1 - \overline { { e } } ^ { 2 } } \left( t - t _ { 0 } \right) . } } \end{array} \right\} \qquad \left\{ \left( \begin{array} { l } { { \varepsilon _ { 1 } } } \\ { { \varepsilon _ { 2 } } } \\ { { \varepsilon _ { 3 } } } \\ { { \varepsilon _ { 3 } } } \end{array} \right) = 0 ,   \\ { { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } } \\ { { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } } \\ { { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } } \end{array} \right.
$$

其中

$$
\bar { n } = \vec { a } ^ { - 3 / 2 } , \vec { p } ^ { : } = \bar { a } ( 1 - \vec { e } ^ { 2 } ) .
$$

（2）一阶短周期项 $\sigma _ { s } ^ { ( 1 ) } \left( t \right)$

根据 $f _ { 1 s }$ 的表达式可以看出，由于积分时 $\pmb { \sigma }$ 应以 $\overline { { \sigma } } ( t )$ 代入，被积函数中会同时出现 $f$ 和 $\pmb { t }$ 两种变量，对 $\pmb { t }$ 无法严格积分．但由于 $f _ { \textrm { I s } }$ 的变化具有短周期特征,又是求一阶项，故可按无摄运动引用变换关系,而且积分时 $\pi ( t )$ 可当作常数.

$$
\begin{array} { c } { { a _ { s } ^ { ( 1 ) } ( t ) = \displaystyle { \int } ^ { t } \frac { 2 } { a n } \frac { \partial R _ { 1 s } } { \partial M } d t = \displaystyle { \int } ^ { u } \frac { 2 } { n a } \frac { \partial R _ { 1 s } } { \partial M } \frac { d M } { n } = \frac { 2 } { n ^ { 2 } a } R _ { 1 s } } } \\ { { = \displaystyle { \frac { A _ { 2 } } { a } \biggl \{ \frac { 2 } { 3 } \biggl ( 1 - \frac { 3 } { 2 } \sin ^ { 2 } i \biggr ) \biggl [ \biggl ( \frac { a } { \uparrow } \biggr ) ^ { 3 } - ( \mathbf { { \bar { 1 } } } - e ^ { 2 } ) ^ { - 3 / 2 } \biggr ] } } } \\ { { + \sin ^ { 2 } i \biggl ( \frac { a } { r } \biggr ) ^ { 3 } \cos 2 ( f + \omega ) \biggr \} . } } \end{array}
$$

$$
\begin{array} { c } { { \dot { \hat { u } } _ { \mathrm { s } } ^ { ( i ) } ( t ) = \displaystyle \int ^ { t } \left( f _ { 1 s } \right) _ { i } d t } } \\ { { \cdot \qquad = - \displaystyle \frac { A _ { 2 } } { 2 a ^ { 2 } } \left( 1 - e ^ { 2 } \right) ^ { s _ { \mathrm { i n } } } 2 i \displaystyle \int ^ { t } \left( \frac { a } { r } \right) ^ { s _ { \mathrm { i n } } } 2 ( f + \omega ) d f } } \\ { { \cdot \qquad = - \displaystyle \frac { A _ { 2 } } { 2 p ^ { 2 } } \sin 2 i \displaystyle \int ^ { t } \left( 1 + e \cos f \right) \sin 2 ( f + \omega ) d f } } \\ { { \cdot \qquad \cdot \qquad \qquad \cdot } } \\ { { \cdot \qquad = \displaystyle \frac { A _ { 2 } } { 4 p ^ { 2 } } \sin 2 i \displaystyle \int \cos 2 ( f + \omega ) + e \cos \left( f + 2 \omega \right) } } \end{array}
$$

$$
+ \frac { e } { 3 } \cos ( 3 f + 2 \omega ) .
$$

关于 $e _ { s } ^ { ( 1 ) } ( t )$ ,不必求积分 $\int ^ { t } { \dot { ( f } } _ { 1 s } ) _ { e } d t$ 根据 ${ \pmb \sigma } _ { \mathfrak { s } } ^ { ( 1 ) } ( t )$ 的积分方法，可由摄动运动方程(4.82)直接给出

$$
\begin{array} { c } { { e _ { s } ^ { ( 1 ) } ( t ) = \displaystyle \frac { 1 - e ^ { 2 } } { e } \biggl [ \frac { 1 } { 2 a } { a } ^ { ( 1 ) } ( t ) - 1 \mathrm { g } i \cdot i _ { s } ^ { ( 1 ) } ( t ) \biggr ] } } \\ { { = \displaystyle \frac { A _ { 2 } } { a ^ { 2 } } \biggl ( \frac { 1 - e ^ { 2 } } { e } \biggr ) \biggl \{ \frac { 1 } { 3 } \biggl ( 1 - \frac { 3 } { 2 } \sin ^ { 2 } i \biggr ) \biggl [ \biggl ( \frac { a } { T } \biggr ) ^ { 3 } - ( 1 - e ^ { 2 } ) ^ { - 3 / 2 } \biggr ] } } \\ { { + \displaystyle \frac { 1 } { 2 } \sin ^ { 2 } i \biggl ( \frac { a } { T } \biggr ) ^ { 3 } \cos 2 \mathrm { ~ } ( f + \omega ) - \frac { \sin ^ { 2 } i } { 2 ( 1 - e ^ { 2 } ) ^ { 2 } } \biggl [ \mathrm { c o s } 2 ( f } } \\ { { } } \\ { { + \omega ) + e \cos \left( f + 2 \omega \right) + \frac { e } { 3 } \cos \mathrm { ~ } ( 3 f + 2 \omega ) \biggr ] \biggr \} . } } \end{array}
$$

$$
\mathcal { Q } _ { \varepsilon } ^ { \scriptscriptstyle ( 1 ) } ( t ) = \int ^ { t } \left( f _ { 1 s } \right) _ { \partial } d t = - \frac { n A _ { 2 } } { a ^ { 2 } \sqrt { 1 - e ^ { 2 } } } \cos { i } \left\{ \frac { 1 } { \pi \sqrt { 1 - e ^ { 2 } } } \right.
$$

$$
\begin{array} { r l } & { \quad \int ^ { 1 } \Big ( \frac { d } { \tau _ { r } ^ { 2 } } \Big ) | \omega \omega | ^ { 2 } \Big ( d \tau \Big ) | \partial _ { t } ^ { 3 } \Big ) - \frac { d _ { 2 } } { \tau _ { r } ^ { 3 } } \omega \varepsilon \varepsilon | \Big ( \int ^ { 1 } \int \mathrm { d } \tau } \\ & { \quad - \mathrm { e } ^ { \mathrm { i } \omega \mathrm { d } \tau _ { r } } \partial _ { - 1 } ^ { 3 } \frac { 1 } { 2 } \sin ( 2 \tau _ { r } ^ { 3 } \cdot \phi ) \cdot \exp ( \tau _ { r } ^ { 3 } \cdot \log ( \tau _ { r } ^ { 3 } ) ) } \\ & { \quad - \frac { 1 } { 8 } \sin ( 3 \tau _ { r } ^ { 3 } ) \cdot \log ( \tau _ { r } ^ { 3 } ) \Big ) \cdot \ } \\ & { \quad \omega _ { \omega } ^ { * } ( \tau _ { r } ^ { 3 } ) - \int ^ { 1 } ( \int _ { 0 } ^ { 1 } \int _ { 0 } ^ { 1 } \int _ { 0 } ^ { 1 } \int _ { 0 } ^ { 1 } \int _ { 0 } ^ { 1 } \int _ { 0 } ^ { 1 } \int _ { 0 } ^ { 1 } \int _ { 0 } ^ { 1 } \int _ { 0 } ^ { 1 } \int _ { 0 } ^ { 1 } \int _ { 0 } ^ { 1 } \int _ { 0 } ^ { 1 } \int _ { 0 } ^ { 1 } } \\ & { \quad - \frac { d _ { 3 } } { \tau _ { r } ^ { 3 } } \Big ( \int _ { 0 } ^ { 1 } - \frac { \delta } { 2 } \sin ^ { 3 } ( \tau _ { r } ^ { 3 } ) \Big ) \cdot \Big ( 1 - \frac { \delta } { 2 } \sin ^ { 3 } ( \tau _ { r } ^ { 3 } ) \Big ) } \\ & { \quad \quad \times \Big [ \Big ( \frac { 1 } { \epsilon } \frac { \delta } { \epsilon } \frac { \delta } { \epsilon } \Big ) \sin ( 1 + \frac { 1 } { 2 } \sin ^ { 2 } ( \tau _ { r } ^ { 4 } ) \frac { \delta } { 1 2 } \sin ^ { 3 } \beta \Big ) \Big ] \ \sin \beta \Big [ \int _ { 0 } ^ { 1 } \int _ { 0 } ^ { 1 } \log ( \tau _ { r } ^ { 3 } ) \Big ] } \\ &  \quad - \Big [ \frac { 1 } { 4 } \sin ^ { 2 } ( \tau _ { r } ^ { 3 } ) \Big \langle \frac { 1 } { 2 }  \end{array}
$$

$$
\begin{array} { l } { { \displaystyle - \Big ( \frac { 1 } { 2 } - \frac { 5 } { 4 } \sin ^ { 2 } i \Big ) \sin 2 ( f + \omega ) + \Big [ \frac { 7 } { 1 2 e } \sin ^ { 2 } i \Big . } } \\ { { \displaystyle - \Big ( \frac { 1 } { 6 } - \frac { 1 9 } { 4 8 } \sin ^ { 2 } i \Big ) e \Big ] \sin \big ( 3 f + 2 \omega \big ) + \frac { 3 } { 8 } \sin ^ { 2 } i \sin \big ( 4 f + \frac { 1 7 } { 2 \cos ( f + \omega ) } \Big ) } } \\ { { \displaystyle + 2 \omega \big ) + \frac { e } { 1 6 } \sin ^ { 2 } i \Bigg [ \sin \big ( 5 f + 2 \omega \big ) + \sin \big ( f - 2 \omega \big ) \Bigg ] \Big \} . } } \end{array}
$$

$$
\begin{array} { r l } { \mathcal { M } _ { a } ^ { ( 1 ) } ( t ) = \displaystyle \int ^ { 1 } [ \frac { \partial \eta } { \partial a } a _ { \star } ^ { ( 1 ) } ( t ) + ( f _ { \star \star } ) _ { \mathcal { H } } ] d t } \\ { \displaystyle } & { ~ = \frac { \overline { { A } } _ { 2 } } { \bar { p } ^ { 2 } } \sqrt { 1 - \bar { e } ^ { 2 } } \{ - ( 1 - \frac { 3 } { 2 } \sin ^ { 2 } \bar { \psi } ) [ ( \frac { 1 } { e } - \frac { e } { 4 } ) \sin f   } \\ { \displaystyle } & { ~  + \frac { 1 } { 2 } \sin 2 f + \frac { e } { 1 2 } \sin 3 \bar { f } ] + \sin ^ { 2 } i [ ( \frac { 1 } { 4 e } + \frac { 5 } { 1 6 } e )   } \\ { \displaystyle } & { ~   \sin ( f + 2 \omega )  } \\ { \displaystyle } & { ~ - ( \frac { 7 } { 1 2 e } - \frac { e } { 4 8 } ) \sin ( 3 f + 2 \omega ) - \frac { 3 } { 8 } \sin ( 3 f + 2 \omega )  } \\ { \displaystyle } & { ~ \displaystyle - \frac { e } { 1 6 } \sin ( 5 f + 2 \omega ) - \frac { e } { 1 6 } \sin ( f - 2 \omega ) ] \} . } \end{array}
$$

上述 ${ \pmb { \sigma } } _ { \bullet } ^ { ( 1 ) } \big ( \pmb { t } \big )$ 表达式右端出现的根数均为 $\overline { { \sigma } } ( t )$ ，当然,在一阶解意义下， $\overline { { a } } , \overline { { e } } , \overline { { i } }$ 就是 $\overline { { { a _ { 0 } } } } , \overline { { { e _ { 0 } } } } , \overline { { { i _ { 0 } } } } ,$ 也可用 $a _ { 0 } , \mathrm { ~ } e _ { 0 } , \mathrm { ~ } i _ { 0 }$ 代替，但$\begin{array} { r } { \cdot \varpi \left( t \right) = \overline { { \omega _ { 0 } } } + \omega _ { 1 } ( t - t _ { 0 } ) , \overline { { M } } ( t ) = \overline { { M _ { 0 } } } + \left( \bar { n } + M _ { 1 } \right) ( t - t _ { 0 } ) . } \end{array}$

将 ${ \sigma _ { s } ^ { ( 1 ) } ( t ) }$ 对卫星运动求平均值,得

$$
\widehat { \pmb { a } _ { s } ^ { ( 1 ) } ( t ) } = 0 ,
$$

$$
\widetilde { e _ { s } ^ { ( 1 ) } ( t ) } = \frac { A _ { 2 } } { p ^ { 2 } } \sin ^ { 2 } i \Big ( \frac { 1 - e ^ { 2 } } { 6 e } \Big ) \widetilde { \cos { 2 f } } \cos 2 \omega ,
$$

$$
\widehat { i _ { s } ^ { ( 1 ) } ( t ) } = - \frac { 1 } { 1 2 } \frac { A _ { 2 } } { p ^ { 2 } } \sin 2 i \widehat { \cos 2 f } \cos 2 \omega ,
$$

$$
\overline { { \mathcal { Q } _ { s } ^ { ( 1 ) } ( t ) } } = - \frac { 1 } { 6 } \frac { A _ { 2 } } { p ^ { 2 } } \cos i \overline { { \cos 2 f } } \sin 2 \omega ,
$$

$$
\widetilde { \omega _ { s } ^ { ( 1 ) } ( t ) } = \frac { A _ { 2 } } { p ^ { 2 } } \bigg [ \sin ^ { 2 } i \bigg ( \frac { 1 } { 8 } + \frac { 1 - e ^ { 2 } } { 6 e ^ { 2 } } \overline { { \cos { 2 f } } } \bigg )
$$

$$
+ \frac { 1 } { 6 } \cos ^ { 2 } i \frac { \phantom { | } } { \cos 2 f } \Biggr ] \sin 2 \omega ,
$$

$$
\overline { { \mathcal { M } _ { s } ^ { ( 1 ) } ( t ) } } = - \frac { A _ { : } } { p ^ { : } } \sqrt { \mathbf { 1 } - e ^ { 2 } } \sin ^ { 2 } i
$$

$$
\times \bigg ( \frac { 1 } { 8 } + \frac { 1 + e ^ { 2 } / 2 } { 6 e ^ { 2 } } \overrightarrow { \mathrm { c o s } 2 f } \bigg ) \sin 2 \omega .
$$

在求平均值过程中已经将 $\overrightarrow { \cos q f }$ 表示成 $\widehat { \tt c o s 2 f }$ 的形式，而 $\widehat { \tt c o s 2 f }$ 由下式计算

$$
\overline { { \cos 2 f } } = \frac { 1 + 2 \sqrt { 1 - e ^ { 2 } } } { ( 1 + \sqrt { 1 - e ^ { 2 } } ) ^ { 2 } } e ^ { 2 } .
$$

上述结果表明， $\sigma _ { s } ^ { \scriptscriptstyle ( 1 ) } ( t ) - \overline { { \sigma _ { s } ^ { \scriptscriptstyle ( 1 ) } ( t ) } }$ 才是真正的短周期项．事实上,求$\pmb { \sigma } _ { s } ^ { ( 1 ) } ( t )$ 时是按无摄运动变换关系积分的，而 $\widehat { \pmb { \sigma } _ { \pmb { \mathscr { s } } } ^ { ( 1 ) } ( t ) }$ 只是 $a , e , i , \omega$ 的函数，因此，该项实为这种积分方法所导致的一个“积分常数”.如果积分 $\int ^ { t } f _ { 1 s } d t$ 时，将 $f _ { i s }$ 展成平近点角 $\pmb { M }$ 的三角级数,从而表示成时间 $\pmb { t }$ 的显函数后直接对 $\pmb { t }$ 积分，则必有 $\overline { { \sigma _ { s } ^ { ( 1 ) } ( \mathfrak { t } ) } } = 0$ 但在计算时， $\widehat { \pmb { \sigma } _ { s } ^ { ( 1 ) } ( t ) }$ 中的 $\omega$ 应为 $\textstyle { \widehat { \omega } } ( t )$ ，而不能当作“常数”，故一阶短周期项应该是

$$
\sigma _ { s } ^ { \scriptscriptstyle ( 1 ) } \big ( t \big ) - \overline { { \sigma _ { s } ^ { \scriptscriptstyle ( 1 ) } \big ( t \big ) } } .
$$

(3）二阶长期项 $\sigma _ { 2 } ( t - t _ { 0 } )$

推导 $\sigma _ { 2 } ( t - t _ { 0 } )$ 和 $\sigma _ { \iota } ^ { ( 1 ) } ( t )$ 时,均涉及到

$$
\sum _ { j } \frac { \partial f _ { 1 } } { \partial \sigma _ { j } } ( \sigma _ { s } ^ { ( 1 ) } ) _ { j } .
$$

这类表达式求平均值时分解成 $c , l , s$ 三种项的问题，为了书写方便，这里引用符号 $c , \ l , s$ 分别表示前面提出的仅与 $a , \ e , \ i$ 有关的部分，性质取决于 $\omega$ 变化的长周期部分和变化由 $\pmb { M }$ 决定的短周期部分．在分离上述各项时要注意以下两点：

1） $c , l , s$ 三种项相乘的结果，一般为

$$
\begin{array} { r l } { c \cdot c  c , } & { c \cdot l  l , ~ c \cdot s  s , } \\ & { l \cdot l  c , l , ~ l \cdot s  s , } \\ & { s \cdot s  c , l , s . } \end{array}
$$

例如

$$
\sin f \cdot \sin f = \left( { \frac { 1 } { 2 } } - { \frac { 1 } { 2 } } { \overline { { \cos 2 f } } } \right) - \left( { \frac { 1 } { 2 } } \cos 2 f - { \frac { 1 } { 2 } } { \overline { { \cos 2 f } } } \right)
$$

2）求平均值时，有

$$
\overline { { A \pm B } } = \overline { { A } } \pm \overline { { B } } .
$$

而在一般情况下，

$$
A \cdot B { \stackrel { \triangledown } { = } } \overline { { A } } \cdot \overline { { B } } , \ \overline { { \left( \frac { A } { B } \right) } } { \triangleq } \overline { { A } } / \overline { { B } } .
$$

对于 $a , e , i _ { : }$ 很容易得到

$$
a _ { 2 } = 0 , e _ { 2 } = 0 , i _ { 2 } = 0 .
$$

由(5.81)式可知,相应的 $f _ { 2 c }$ 的三个分量皆为零，即

$$
( f _ { 2 c } ) _ { a , e ; i } = 0 .
$$

而另一大项

$$
\displaystyle \left( \sum _ { j } \frac { \partial f _ { 1 } } { \partial \sigma _ { j } } ( \sigma _ { s } ^ { ( 1 ) } ) _ { j } \right) _ { c } ~ ;
$$

的计算也不复杂。对 $a , i$ 很容易算出它们为零,因此有

$$
a _ { 2 } = 0 , ~ i _ { 2 } = 0 .
$$

至于 $e _ { i }$ ，由摄动运动方程(4.82)可知，

$$
\frac { d e } { d t } = \frac { 1 - e ^ { 2 } } { e } \bigg ( \frac { 1 } { 2 a } \frac { d a } { d t } - \mathrm { t g } i \frac { d i } { d t } \bigg )
$$

于是有

$$
\sum _ { j } \frac { \partial ( f _ { 1 } ) _ { e } } { \partial \sigma _ { j } } \left( \sigma _ { s } ^ { ( 1 ) } \right) _ { j } = \frac { 1 - e ^ { 2 } } { e } \bigg [ \frac { 1 } { 2 a } \sum _ { j } \frac { \partial ( f _ { 1 } ) _ { a } } { \partial \sigma _ { j } } \left( \sigma _ { s } ^ { ( 1 ) } \right) _ { j }
$$

$$
\begin{array} { r l } & { \quad _ { j } ^ { j } } \\ & { - \arg i \sum _ { j } \frac { \partial ( f _ { 1 } ) _ { i } } { \partial \sigma _ { j } } ( \sigma _ { s } ^ { ( 1 ) } ) _ { j } \bigg ] + \frac { 1 + e ^ { 2 } } { e ^ { 2 } } \times \bigg [ - \frac { 1 } { 2 a } ( f _ { 1 } ) _ { a } e _ { s } ^ { ( 1 ) } + \mathrm { t g } i \big ( f _ { 1 } \big ) _ { i } e _ { s } ^ { ( 1 ) } } \\ & { + \frac { 1 - e ^ { 2 } } { e } \bigg [ - \frac { 1 } { 2 a ^ { 2 } } \left( f _ { 1 } \right) _ { a } a _ { s } ^ { ( 1 ) } - \sec ^ { 2 } i \left( f _ { 1 } \right) _ { i } i _ { s } ^ { ( 1 ) } \bigg ] . } \end{array}
$$

经计算得