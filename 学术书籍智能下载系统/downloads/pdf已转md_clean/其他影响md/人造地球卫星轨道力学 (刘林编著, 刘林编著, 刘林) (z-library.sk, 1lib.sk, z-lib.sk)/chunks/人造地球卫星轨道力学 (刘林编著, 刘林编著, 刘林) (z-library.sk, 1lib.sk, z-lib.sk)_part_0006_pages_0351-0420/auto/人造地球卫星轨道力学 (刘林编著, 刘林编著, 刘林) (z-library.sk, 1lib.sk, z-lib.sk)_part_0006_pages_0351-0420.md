$$
\hat { P } ^ { * } \mathrm { = } \left( \begin{array} { c } { \mathrm { c o s } \widetilde { \Omega } } \\ { \mathrm { s i n } \widetilde { \Omega } } \\ { 0 } \end{array} \right) , \ \hat { Q } ^ { * } \mathrm { = } \left( \begin{array} { c } { - \mathrm { s i n } \widetilde { \Omega } \mathrm { c o s } \widetilde { J } } \\ { \mathrm { c o s } \widetilde { \Omega } \mathrm { c o s } \widetilde { J } } \\ { \mathrm { s i n } \widetilde { J } } \end{array} \right) .
$$

# 3．适用于分析方法的日、月轨道有关量的计算公式

在用分析方法讨论日月摄动时，在摄动函数中将出现下列形式的三个量：

$$
\left( { \frac { 1 } { r ^ { \prime } } } \right) ^ { 3 } , \left( { \frac { 1 } { r ^ { \prime } } } \right) ^ { 3 } \cos 2 u ^ { \prime } , \left( { \frac { 1 } { r ^ { \prime } } } \right) ^ { 3 } \sin 2 u ^ { \prime }
$$

其中 $\pmb { u } ^ { \prime }$ 是日、月对赤道的纬度角，见图8.2．对于分析方法，相应的摄动函数表达式不宜过于复杂，在精度要求不太高的情况下，这一点是可以满足的．例如定位精度为米级，对于近地卫星，摄动外推在 $1 0 ^ { 3 }$ 弧段以内，相应的月球位置矢量 $r ^ { \prime } ( t )$ 的精度要求不高于$1 0 ^ { - 3 }$ ，在此前提下，根据月球瞬时轨道根数的计算公式(8.7)式可以导出上述三个量的近似表达式，即

$$
\begin{array} { l } { { \displaystyle ( \frac { 1 } { r ^ { \prime } } ) ^ { 3 } = ( \frac { 1 } { r _ { 0 } ^ { \prime } } ) ^ { 3 } \{ ( 1 + \frac { 3 } { 2 } e ^ { \prime 2 } ) + 3 e ^ { \prime } \cos { \mathcal { M } ^ { \prime } } + \frac { 9 } { 2 } e ^ { \prime 2 } \cos { 2 \mathcal { M } ^ { \prime } }  } } \\ { { \displaystyle \qquad + 2 \sum _ { j } P _ { j } \cos { \alpha _ { j } } \} } } \\ { { \displaystyle ( \frac { 1 } { r ^ { \prime } } ) ^ { 3 } \cos { 2 u ^ { \prime } } = ( \frac { 1 } { r _ { 0 } ^ { \prime } } ) ^ { 3 } \{ ( 1 - \frac { 5 } { 2 } e ^ { \prime 2 } ) \cos { 2 L ^ { * } } - 2 e ^ { \prime }  } }  \\ { { \displaystyle \qquad \times [ \frac { 1 } { 4 } \cos { ( 2 L ^ { * } - \mathcal { M } ^ { \prime } ) } - \frac { 7 } { 4 } \cos { ( 2 L ^ { * } + \mathcal { M } ^ { \prime } ) } ]  } } \end{array} \qquad 
$$

$$
\begin{array} { c } { { \mathrm {  ~ \gamma ~ } \times \displaystyle _ { 0 } ^ { 0 } \mathrm {  ~ \gamma ~ } \times \left( 2 { \cal L } ^ { * } - { \cal M } ^ { \prime } \right) - \displaystyle \frac { 7 } { 4 } \cos \left( 2 { \cal L } ^ { * } + { \cal M } ^ { \prime } \right) \displaystyle \Bigg ] } } \\ { { \mathrm {  ~ \times ~ } \displaystyle _ { \left\{ \frac { 1 } { 4 } \leq 0 \right\} } ^ { 1 } \mathrm {  ~ \exp ~ } ( 2 { \cal L } ^ { * } + 2 { \cal M } ^ { \prime } ) - \displaystyle \sum _ { j } ^ { 1 } \left( { \cal K } _ { j } - P _ { j } \right) \mathrm {  ~ \cos ~ } ( 2 { \cal L } ^ { * } - \alpha _ { j } ) } } \\ { { + \displaystyle \frac { 1 7 } { 2 } e ^ { i \alpha _ { j } } \mathrm {  ~ \cos ~ } ( 2 { \cal L } ^ { * } + 2 { \cal M } ^ { \prime } ) - \displaystyle \sum _ { j } ^ { 1 } \left( { \cal K } _ { j } - P _ { j } \right) \mathrm {  ~ \cos ~ } ( 2 { \cal L } ^ { * } - \alpha _ { j } ) } } \\ { { + \displaystyle \sum _ { j } ^ { 1 } \left( { \cal K } _ { j } \cdot \mathrm {  ~ F ~ } p \right) \mathrm {  ~ \cos ~ } ( 2 { \cal L } ^ { * } + \alpha _ { j } ) \displaystyle \Bigg \} , } } \\ { { \mathrm {  ~ a ~ } 2 \alpha ^ { \prime } = \left( \displaystyle \frac { 1 } { r _ { 0 } } \right) ^ { 2 } \displaystyle \left\{ \left( 1 - \frac { 5 } { 2 } e ^ { i \mathrm {  ~ \alpha ~ } _ { j } } \right) \sin 2 { \cal L } ^ { * } - 2 { \cal E } e ^ { i \left[ \displaystyle \frac { 1 } { 4 } \sin \left( 2 { \cal L } ^ { * } - { \cal M } ^ { \prime } \right) \right] } \mathrm {  ~ \sin ~ } ( 2 { \cal L } ^ { * } - \alpha _ { j } ) \mathrm {  ~ \Omega ~ } \right. } } \\ { { \displaystyle \left. \mathrm {  ~ \alpha ~ } - \displaystyle \frac { 7 } { 4 } \sin \left( 2 { \cal L } ^ { * } + { \cal M } ^ { \prime } \right) \right\} + \displaystyle \frac { 1 7 } { 2 } e ^ { i 2 } \sin \left( 2 { \cal L } ^ { * } + 2 { \cal M } ^ { \prime } \right) } } \end{array}
$$

$$
- \sum _ { j } \left( K _ { j } - P _ { j } \right) \sin \left( 2 L ^ { * } - \alpha _ { j } \right) + \ \sum _ { j } \left( K _ { j } + P _ { j } \right) \sin \left( 2 L ^ { * } + \alpha _ { j } \right) \Big \{
$$

其中

$$
e ^ { \prime } { = } 0 . 0 5 4 6 ,
$$

$$
\displaystyle { P _ { j } = \frac { 3 } { 2 } Q _ { j } } ,
$$

$$
\scriptstyle { L ^ { * } = L ^ { \prime } - ( \varOmega _ { \mathfrak { d } } - \theta ) }
$$

各式中出现的 $e ^ { \prime }$ 不同于(8.6)式中给出的月球平均根数 ${ \pmb e } ^ { \prime }$ ，原出现在各式中的 $\pmb { e } ^ { \prime }$ 是不同的，但在准到 $1 0 ^ { - 3 }$ 的前提下,可取同一值，即(8.15)式给出的0.0546．而(8.17)式中的 $( \Omega _ { \mathfrak { c } } \sim \theta )$ ，可利用图8.3导出，即

$$
\mathrm {  ~ \xi ~ } _ { 1 } \left( \Omega _ { \mathfrak { q } } - \theta \right) = \frac { \cos \varepsilon \sin \mathcal { Q } _ { \mathfrak { q } } } { \sin i ^ { \prime } } \ \sin J - \frac { \sin \varepsilon \sin 2 \mathcal { Q } _ { \mathfrak { q } } } { \sin i ^ { \prime } } \sin ^ { 2 } \frac { J } { 2 } .
$$

对于太阳, $\pmb { r _ { 0 } ^ { \prime } }$ 即平均距离， $\pmb { e } ^ { \prime }$ 和 $M ^ { \prime }$ 相应地换成太阳平均轨道根数 $\pmb { e }$ 和 $\mathcal { M }$ ， $L ^ { * }$ 即平均根数 $\pmb { L }$ ，而所有 $\kappa _ { j }$ 和 $P _ { j }$ 项消失．除此之外,所有 $e ^ { 2 }$ 项亦可删去.

# 8.2 日月摄动函数的根数形式

根据(8.1)式不难写出地心赤道直角坐标系 $( x , y , z )$ 中的日月摄动函数 $R _ { ☉ }$ ，即

$$
R { = } G m ^ { \prime } \biggl ( \frac { 1 } { \Delta } { - } \frac { r ^ { \prime } } { r ^ { \prime 3 } } { \cdot } r \biggr ) { = } G m ^ { \prime } \biggl ( \frac { 1 } { \Delta } { - } \frac { r } { r ^ { \prime 2 } } \cos \psi \biggr ) ,
$$

$$
\cos \psi = \frac { r ^ { \prime } } { r ^ { \prime } } \cdot \frac { r } { r } .
$$

这里 $\psi$ 是日、月和卫星在地心处的张角，见图8.2，显然有如下关系：

$$
\Delta ^ { 2 } = r ^ { 2 } + r ^ { \prime 2 } - 2 r r ^ { \prime } \cos \psi ,
$$

![](images/b151dcb58276fa61c602f9c009c2293c883f674fc6dd3e55a012cf8be8e84c5c.jpg)  
图8.2赤道、卫星 $( \pmb { S } _ { \ast } )$ 轨道和日、月 $( \pmb { \mathcal { S } } ^ { \prime } )$ 轨道在天球上的投影

根据勒让德多项式的性质(5.25)式,有

$$
\begin{array} { l } { { \displaystyle \frac { 1 } { \Delta } { = } \frac { 1 } { r ^ { \prime } } \biggl [ 1 { - } 2 \biggl ( \frac { r } { r ^ { \prime } } \biggr ) \cos \psi + \Bigl ( \frac { r } { r ^ { \prime } } \biggr ) ^ { 2 } \biggr ] ^ { - 1 / 2 } } } \\ { { \mathrm { = } \displaystyle \frac { 1 } { r ^ { \prime } } \sum _ { n = 0 } ^ { \infty } P _ { n } \bigl ( \cos \psi \bigr ) \left( \frac { r } { r ^ { \prime } } \right) ^ { n } , } } \end{array}
$$

将该式代人(8.19)式,舍去与卫星根数无关的 $\frac { 1 } { r ^ { \prime } } ,$ 则得

$$
\begin{array} { r l } & { R { = } \displaystyle \frac { G m ^ { \prime } } { r ^ { \prime } } \sum _ { n > 2 } \biggl ( \frac { r } { r ^ { \prime } } \biggr ) ^ { n } P _ { n } ( \cos \psi ) } \\ & { ~ { = } G m ^ { \prime } \left[ \frac { r ^ { 2 } } { r ^ { \prime 3 } } \biggl ( \frac { 3 } { 2 } \cos ^ { 2 } \psi { - \frac { 1 } { 2 } } \biggr ) \right. } \\ & { ~ \left. + \frac { r ^ { 3 } } { r ^ { \prime 4 } } \biggl ( \frac { 5 } { 2 } \cos ^ { 3 } \psi { - \frac { 3 } { 2 } } \cos \psi \biggr ) { + } \cdots \right] . } \end{array}
$$

要将摄动函数表示成轨道根数的形式，其关键在于 $\cos \psi$ 、因$\frac { \hat { \mathbf { r } } ^ { \prime } } { \hat { r } ^ { \prime } } { = } \hat { r } ^ { \prime }$ 是日、月方向的单位向量， $\frac { r } { r } { = } \stackrel { \wedge } { r }$ 即卫星的径向单位向量，根据第四章给出的 $\hat { \pmb { r } }$ 的三个分量 $l _ { 1 } , m _ { 1 } , n _ { 1 }$ 的表达式(4.70)，不难给出相应的 $\hat { \pmb { r } }$ 的三个分量的表达式，只要将卫星的根数 $\Omega , u , i$

应的改为日、月根数 $\Omega ^ { \prime } , u ^ { \prime } , i$ 即行，这几个量的意义见图8.2．于是可得

$$
 \begin{array} { c } { { \cos \psi = A \cos u + B \sin u , } } \\ { { { } } } \\ { { A = \cos ( \varOmega - \varOmega ^ { \prime } ) \cos u ^ { \prime } - | - \sin ( \varOmega - \varOmega ^ { \prime } ) \cos i ^ { \prime } \sin u ^ { \prime } , } } \\ { { \bar { B } = - \sin ( \varOmega - \varOmega ^ { \prime } ) \cos i \cos u ^ { \prime } + ( \cos ( \varOmega - \varOmega ^ { \prime } )  } } \\ { {  \cos i \cos i ^ { \prime } + \sin i \sin i ^ { \prime } ) \sin u ^ { \prime } , } } \end{array} \}
$$

或者将 $A , B$ 写成另一种形式：

$$
\left. \begin{array} { c } { { A { = } A _ { 1 } \cos u ^ { \prime } { + } A _ { 2 } \sin u ^ { \prime } , \quad B { = } B _ { 1 } \cos u ^ { \prime } { + } B _ { 2 } \sin u ^ { \prime } } } \\ { { A _ { 1 } { = } \cos \left( \Omega { - } \Omega ^ { \prime } \right) , \qquad A _ { 2 } { = } \sin \left( \Omega { - } \Omega ^ { \prime } \right) \cos i ^ { \prime } , } } \\ { { B _ { 1 } { = } - \sin \left( \Omega { - } \Omega ^ { \prime } \right) \cos i , B _ { 2 } { = } \cos \left( \Omega { - } \Omega ^ { \prime } \right) } } \\ { { c o s i \ : c o s i ^ { \prime } { + } \sin i \sin i ^ { \prime } . } } \end{array} \right\}
$$

对于太阳有

$$
\dot { \pmb { i } } ^ { \prime } { = } \pmb { \varepsilon } , ~ \pmb { \varOmega } ^ { \prime } { = } 0 .
$$

将 $\cos \psi$ 的表达式代入(8.23)式,并采用标准单位,得

$$
\begin{array} { l } { { \displaystyle = \frac { 3 } { 2 } \beta a ^ { 2 } \bigg ( \frac { r } { a } \bigg ) ^ { 2 } \bigg [ - \frac { 1 } { 3 } + \frac { 1 } { 2 } ( A ^ { 2 } + B ^ { 2 } ) } } \\ { { + \frac { 1 } { 2 } ( A ^ { 2 } - B _ { - } ^ { 2 } ) \cos 2 u + A B \sin 2 u \bigg ] + \frac { 3 } { 2 } \beta a ^ { 2 } \bigg ( \frac { a } { r _ { 0 } ^ { \prime } } \bigg ) \bigg ( \frac { r } { a } \bigg ) ^ { 3 } } } \\ { { \times \bigg \{ \bigg [ \frac { 5 } { 4 } ( A ^ { 2 } + B ^ { 2 } ) - 1 \bigg ] A \cos u + \bigg [ \frac { 5 } { 4 } ( A ^ { 2 } + B ^ { 2 } ) - 1 \bigg ] B \sin u } } \\ { { + \frac { 5 } { 1 2 } ( A ^ { 2 } - 3 B ^ { 2 } ) A \cos 3 u + \frac { 5 } { 1 2 } ( 3 A ^ { 2 } - B ^ { 2 } ) B \sin 3 u \bigg \} , ( 8 . 2 9 } } \end{array}
$$

其中

$$
\beta { = } \frac { m ^ { \prime } } { r ^ { \prime 3 } } .
$$

对于月球摄动,上述各式中出现的 $i ^ { \prime }$ 和 $\Omega ^ { \prime }$ ，可根据图8.3导出相应的计算公式，即

$$
\cos \theta ^ { l } = \cos \mathcal { E } \cos \theta J - \sin \mathcal { E } \sin \mathcal { J } \cos \mathcal { Q } _ { \nu } , \ \sin i ^ { \prime } = \sqrt { 1 - \cos ^ { 2 } i ^ { \prime } } \ ,
$$

![](images/246189fa88e4ade8214fd340a7aac3f93ace7421c8c74d8e444420909ba75ac2.jpg)  
图8.3赤道、黄道和白道在天球上的投影

$$
\sin \varOmega ^ { \prime } = \frac { \sin J \sin \varOmega _ { \mathrm { ~ p ~ } } } { \sin i ^ { \prime } } , \cos \varOmega ^ { \prime } = \frac { \cos J - \cos \varepsilon \cos i ^ { \prime } } { \sin \varepsilon \sin i ^ { \prime } } ,
$$

其中计算 $\sin \varOmega ^ { \prime }$ 时,按前面提出的对月球位置精度的要求，右端的sin $\varOmega _ { \mathfrak { d } }$ 应为 $\sin \widetilde { \Omega } , \widetilde { \Omega }$ 的变化中有一最大的周期项 $\Omega _ { 1 2 } \sin \alpha _ { 1 2 }$ 要考虑（见表 $8 . 1 , \varOmega _ { 1 2 } { = } - 0 . 0 2 7 4 7 )$ ，如果精度要求稍低些，则 $\widetilde { \Omega }$ 可由$\varOmega$ ,代替，即(8.32)式.

利用第二章求平均值的方法,给出

$$
\overline { { \left( \frac { r } { a } \right) ^ { 2 } } } = 1 + \frac { 3 } { 2 } e ^ { 2 } , \overline { { \left( \frac { r } { a } \right) ^ { 2 } \cos 2 f } } = \frac { 5 } { 2 } e ^ { 2 } , \overline { { \left( \frac { r } { a } \right) ^ { 2 } \sin 2 f } } = 0 ,
$$

$$
\begin{array} { r l r } & { \overline { { ( \frac { r } { a } ) ^ { 3 } \cos f } } = - \Big ( \frac { 5 } { 2 } e + \frac { 1 5 } { 8 } e ^ { 3 } \Big ) , \overline { { ( \frac { r } { a } ) ^ { 3 } \cos 3 f } } = - \frac { 3 5 } { 8 } e ^ { 3 } , } & { \underline { { | } } } \\ & { \overline { { ( \frac { r } { a } ) ^ { 3 } \sin f } } = \overline { { ( \frac { r } { a } ) ^ { 3 } \sin 3 f } } = 0 . } & { \} ^ { 0 } } \end{array}
$$

于是摄动函数 $\pmb { R }$ 可分成两个部分，即

$$
\begin{array} { c } { { R = \overline { { { R } } } + R _ { s } , } } \\ { { \displaystyle \frac { 3 } { 8 } \beta a ^ { 2 } \Big \{ \Big ( 1 + \frac { 3 } { 2 } e ^ { 2 } \Big ) D _ { 1 } + \frac { 5 } { 2 } e ^ { 2 } ( D _ { 3 } \cos 2 \omega + D _ { 5 } \sin 2 \omega ) } } \\ { { \displaystyle + \bigg [ \Big ( 1 + \frac { 3 } { 2 } e ^ { 2 } \Big ) D _ { 2 } + \frac { 5 } { 2 } e ^ { 2 } ( D _ { 4 } \cos 2 \omega + D _ { 6 } \sin 2 \omega ) \Big ] \log 2 a ^ { \prime } \ } } \end{array}
$$

$$
+ \bigg [ \bigg ( 1 + \frac { 3 } { 2 } e ^ { 2 } \bigg ) D _ { \tau } + \frac { 5 } { 2 } e ^ { 2 } ( D _ { 8 } \cos 2 \omega + D _ { 8 } \sin 2 \omega ) \bigg ] \sin 2 u ^ { \prime } \bigg \}
$$

$$
\begin{array} { r l } & { \mathbb { E } \beta a ^ { 5 } \biggl ( \frac { a } { T _ { 0 } } \biggr ) ^ { \zeta } 1 - \frac { 5 } { 4 } ( A ^ { * } + B ^ { * } ) \Biggr ] e ( \langle A \mathrm { e o s ~ } \Omega + B \mathrm { s i n o l ~ } ) , \qquad \mathrm { ( } \beta , \bar { s } \mathrm { i n h o l ~ } ) } \\ & { + \frac { 3 } { 8 } \beta a ^ { * } \biggl \{ \biggl ( \frac { T } { a } \biggr ) ^ { \zeta } \biggl ( - \biggl ( 1 + \frac { 3 } { 2 } e ^ { \xi } \biggr ) \biggr ) \biggl ( \langle D _ { 1 } - D _ { \bar { s } } \mathrm { e v e } 2 L ^ { * } + D _ { \bar { s } } \mathrm { e i n } 2 L ^ { * } } \\ & { + \biggl [ \biggl ( \frac { T } { a } \biggr ) ^ { \zeta } \biggr ) ^ { \zeta } \biggr . \biggr . } \\ & {   + ( \langle D _ { \bar { s } } \mathrm { e v e } 2 \ell - \frac { 5 } { 2 } e ^ { z } \biggr ] \frac { 1 } { L } \langle D _ { \bar { s } } \mathrm { e s } 2 \mathrm { e } 2 \beta \mathrm { e } 3 \rangle \biggr .   } \\ & {    + ( \langle D _ { \bar { s } } \mathrm { e v e } 2 \mathrm { e } 1 \beta \mathrm { e } 2 \rangle ) \mathrm { s i n } 2 \langle D _ { \bar { s } } \mathrm { e } 1 \beta \mathrm { e } 2 \phi ) \biggr \}   } \\ & {  \mathrm { s i n } 2 L ^ { * } \geq \{ \biggl ( \frac { T } { a } \biggr ) ^ { \zeta } \sin 2 \bar { f } \} \bigl [ \langle - D _ { \bar { s } } \mathrm { s i n } 2 \omega + D _ { \bar { s } } \mathrm { e o s } 2 \omega \rangle } \\ & { +  \langle - D _ { \bar { s } } \mathrm { e i n } 2 \omega + D _ { \bar { s } } \mathrm { e s } 2 \omega \rangle \mathrm { c o s } 2 L ^ { * } \} } \\ & {  \quad - \langle D _ { \bar { s } } \mathrm { e n } 2 \omega - D _ { \bar { s } } \mathrm { e s } 2 \omega \rangle \mathrm { s i n } 2 L ^ { * } \} . } \end{array}
$$

其中

$$
\begin{array} { r l } &  \begin{array} { r l } & { \mathcal { P } _ { 2 } \ldots \mathcal { A } _ { 1 } + \mathcal { A } _ { 1 } ^ { - 1 } + \mathcal { B } _ { 1 } ^ { - 1 } - \mathcal { R } _ { 1 } ^ { 1 } - \frac { 1 } { 3 } } \\ & { - \frac { 2 } { 3 } \left( 1 - \frac { \lambda } { 2 } \sin ^ { 2 } \psi _ { 1 } + \mathcal { R } _ { 1 } ^ { - 1 } \right) \left( \lambda - \frac { 2 } { 3 } \sin ^ { 2 } \psi _ { 1 } + \rangle + \right) + \frac { 1 } { 2 } \sin ^ { 2 } \psi _ { 1 } \sin 2 \psi _ { 1 } ^ { 2 } } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ &  \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \ \end{array} \end{array}
$$

$$
D _ { 4 } { = } A _ { 1 } ^ { 2 } { - } A _ { 2 } ^ { 2 } { - } B _ { 1 } ^ { 2 } { + } B _ { 2 } ^ { 2 }
$$

$$
 \begin{array} { l } { { \begin{array} { r l } { \omega - \frac { 3 } { 2 } \sin ^ { 2 } \mathrm { i } \sin ^ { 3 } \mathrm { i } \sin ^ { 4 } \mathrm { i } + \frac { 1 } { 2 } \sin 2 \mathrm { i } \sin 2 \mathrm { i } ^ { 3 } \cos ( \Omega - Q ^ { 2 } ) } \\ { \quad + \frac { 1 } { 2 } ( 1 + \cos ^ { 2 } \mathrm { i } ) ( 1 + \cos ^ { 2 } \mathrm { i } ^ { 2 } ) \cos 2 \mathrm { i } ( Q - Q ^ { 2 } ) , } \end{array} } } \\ { { \begin{array} { r l } { \partial _ { 1 } - ( 2 ( A _ { 1 } B _ { 1 } - A _ { 1 } B _ { 1 } ) } \\ { - \cos \mathrm { i } \sin \mathrm { i } \Omega ^ { 2 } \mathrm { i } \sin ( Q - Q ^ { 2 } ) - \cos \mathrm { i } \sin \mathrm { i } \mathrm { i } ^ { 3 } \mathrm { i } ^ { 2 } } \\ { \sin ^ { 2 } \mathrm { i } \sin \mathrm { i } \Omega ^ { 2 } \mathrm { i } \sin ( Q - Q ^ { 2 } ) - \cos \mathrm { i } \sin \mathrm { i } \mathrm { i } ^ { 3 } \mathrm { i } ^ { 2 } } \end{array} } } \\ { { \begin{array} { r l } { \sin \mathrm { i } \sin \mathrm { i } ( Q - Q ^ { 2 } ) , } \\ { { B _ { 6 } - ( A _ { 1 } B _ { 1 } - A _ { 2 } B _ { 2 } ) } } \\ { - \cos \mathrm { i } \sin \mathrm { i } \sin \mathrm { i } \mathrm { i } \sin ( Q - Q ^ { 2 } ) - \cos \mathrm { i } ( 1 + \cos ^ { 2 } \mathrm { i } ^ { 3 } ) } \\ { \sin ^ { 2 } \mathrm { i } \sin \mathrm { i } \mathrm { i } \sin \mathrm { i } \mathrm { i } \partial _ { 2 } \mathrm { i } \mathrm { i } \cos 2 \mathrm { i } \mathrm { i } ^ { 3 } } \end{array} } } \\   \begin{array} { r l } { \cos \mathrm { i } \sin \mathrm { i } \mathrm { i } \sin \mathrm { i } Q \mathrm { i } \cos ( Q - Q ^ { 2 } ) , } \\  { B _ { 6 } - ( A _ { 1 } A _ { 2 } + B _ { 1 } B _ { 2 } ) } \\ { - \cos \mathrm { i } \sin ^ { 2 } \mathrm { i } \sin \mathrm { i } \mathrm { i } ^ { 3 } \mathrm { i } ^ { 2 } } \\  - \sin ^ { 2 } \mathrm { i } \sin ^ { 2 } \mathrm { i } ^ { 3 } \mathrm { i } ^ { 4 }  \end{array} \end{array}
$$$$
\left. \begin{array} { l } { { - \sin i \sin \alpha \tan \beta \tan ( \beta - \alpha ) - \cos \alpha \sin ^ { 2 } \alpha ^ { \prime } } } \\ { { } } \\ { { } } \\ { { D _ { t } - 2 \sin \alpha \left( 2 \sin \beta - \alpha \right) , } } \\ { { } } \\ { { D _ { t } - 2 \left( \Delta _ { t } \beta - \Delta _ { t } \beta \right) , } } \\ { { } } \\ { { } } \\ { { \phantom { - } \sin \alpha \tan \beta \tan \left( \beta - \alpha \right) , } } \\ { { } } \\ { { } } \\ { { \phantom { - } \cos \alpha \sin \alpha \sin \alpha \sin \beta \sin \left( \alpha \right) , } } \\ { { { } \phantom { - } \sin \alpha \cos \alpha \sin \beta \sin \alpha \sin ^ { \prime } \alpha \sin ^ { \prime } } } \\ { { } } \\ { { } } \\ { { \phantom { - } \sin \alpha \cos \beta \sin \alpha \sin \beta \sin \beta } } \\ { { } } \\ { { } } \\ { { \phantom { - } \sin \alpha \sin \beta \sin \alpha \sin \left( \beta - \alpha \right) + \left( 1 + \cos \alpha ^ { \prime } \right) \sin \alpha \sin ^ { \prime } \alpha \sin ^ { \prime } } } \\ { { } } \\ { { } } \\ { { } } \\ { { \phantom { - } \sin \alpha \cos \alpha \sin \beta \cos \alpha \cos \beta \sin \beta \sin \alpha \sin ^ { \prime } \alpha \cos \alpha ^ { \prime } } } \\ { { } } \\ { { } } \\ { { } } \\ { { } } \\ { { \phantom { - } \cos 2 \left( \Delta _ { t } \beta - \Delta _ { t } \right) , } } \\ { { } } \\ { { } } \\ { { \phantom { - } \cos 2 \left( \Delta _ { t } \beta - \alpha \right) , } } \\ { { } } \\ { { \phantom { - } \cos 2 \left( \Delta _ { t } \beta - \alpha \right) , } } \\ { { } } \\ { { } } \\ { { \phantom { - } \cos 2 \left( \Delta _ { t } \beta - \alpha \right) , } } \\ { { } } \\ { { } } \\ { { \phantom { - } \cos 2 \left( \Delta _ { t } \beta - \alpha \right) , } } \\ { { } } \\ { { } } \\ { { \phantom { - } \cos 2 \left( \Delta _ { t } \gamma \right) \cos \alpha \left( \Delta ^ { \prime } - \alpha \right) + \cos \alpha ^ { \prime } \cos \alpha ^ { \prime } \alpha } } \\ { { } } \\ { { } } \\ { { } } \end{array} \right\} .
$$

若以地球引力场位函数展开式中的 ${ \pmb J } _ { 2 }$ 项作为小量的标准，那么对近地卫星，上述 $\overline { R }$ 右端的第一大部分为二阶小量，第二大部分则为三阶小量， $\pmb { R _ { s } }$ 即二阶短周期部分．为了证实前面的量级估计和有助于实际工作中对摄动函数作各种进一步的简化，有必要作一些定量计算、选取两种卫星：近地卫星（周期为 $2 ^ { \tt h }$ ）和 $2 4 ^ { \tt h }$ 地球同步卫星，初始值分别为

$$
T = 2 ^ { \mathrm { h } } , a = 8 0 5 9 . 0 0 3 0 9 3 \mathrm { k m } , e = 0 . 0 1 , i = 5 0 ^ { \circ } , \varOmega = 5 0 ^ { \circ } ,
$$

$$
\begin{array} { r } { I ^ { \circ } = 2 3 ^ { \mathrm { h } } 5 6 ^ { \mathrm { m } } 4 5 ^ { \mathrm { s } } , a = 4 2 1 7 7 . 5 4 4 8 0 0 \mathrm { k m } , e = 0 . 0 2 , i = 1 ^ { \circ } . 0 , } \end{array}
$$

$$
\Omega = 3 0 ^ { \circ } , \omega = 3 0 ^ { \circ } , M = 3 0 ^ { \circ } .
$$

<table><tr><td>2卫星</td><td>a(km)</td><td>e</td><td>（度）</td><td>λ=M+ω（度）</td><td>△(弧度）</td><td>注</td></tr><tr><td>无抵运动</td><td>8059.003093</td><td>0.01000000</td><td>50.000000</td><td>99.999996</td><td></td><td></td></tr><tr><td>S1</td><td>8059.003121</td><td>0.00999998</td><td>49.999903</td><td>99.999759</td><td>4×10--</td><td>相对无摄运动</td></tr><tr><td>S2</td><td>8059.003124</td><td>0.00999997</td><td>49.999898</td><td>99.999744</td><td>3×10-7</td><td>相对S1</td></tr><tr><td>L1</td><td>8059.002955</td><td>0.01000074</td><td>50.000195</td><td>99.997653</td><td>4×10-</td><td>相对无摄运动</td></tr><tr><td>L2</td><td>8059.003109</td><td>0.01000064</td><td>50.000127</td><td>99.997835</td><td>3×10-8</td><td>相对L1</td></tr><tr><td>L3</td><td>8059.003100</td><td>0.01000064</td><td>50.000128</td><td>99.997836</td><td>10-:</td><td>相对L2</td></tr><tr><td>同步卫星</td><td>a(km)</td><td>e</td><td>（度）</td><td>-M+e+Ω（度）</td><td>△(弧度）</td><td>注</td></tr><tr><td></td><td></td><td>0.02000000</td><td>1.000000</td><td>106.286760</td><td></td><td></td></tr><tr><td>无摄运动</td><td>42177.544800</td><td>0.01993612</td><td>1.004181</td><td>106.347128</td><td>10-8</td><td>相对无摄运动</td></tr><tr><td>S1</td><td>42177.538883</td><td></td><td>1.004286</td><td>106.350332</td><td>6×10-5</td><td>相对S1</td></tr><tr><td>S2</td><td>42177.533447</td><td>0.01993270</td><td>1. 015587</td><td>106.130660</td><td></td><td></td></tr><tr><td>L1</td><td>42178.666249</td><td>0.01993851</td><td>1.014978</td><td>106.176551</td><td>3×10-s</td><td>相对无摄运动</td></tr><tr><td>L2</td><td>42178.589828</td><td>0.01992945</td><td></td><td></td><td>0.8×10-s</td><td>相对L1</td></tr><tr><td>L3</td><td>42178.600847</td><td>0.01992995</td><td>1.014943</td><td>106.175225</td><td>2X10-</td><td>相对L2</td></tr></table>

外推20圈 $( t _ { 0 } = 0 , t$ 分别为 $4 0 ^ { \mathtt { h } }$ 和20天，相应的弧段约为 $1 0 ^ { 2 }$ ，计算结果列于表8.2.

表8.2中, $\pmb { S 1 }$ 和 $\pmb { S 2 }$ 是太阳摄动，分别对应太阳轨道为不变圆和不变椭圆； $L 1 , L 2 , L 3$ 是月球摄动，分别对应月球轨道为不变圆，包含主要变化项(长期项，椭圆项和表8.1中 $\mathbf { } K _ { j } , Q _ { j }$ 的前两项以及${ \mathcal { Q } } _ { j } , J _ { j }$ 中的第12项)的椭圆和包含表8.1中列出的全部周期项的椭圆．从表中列出的数据可以看出，不仅完全符合前面的量级估计而且为确定各种项的取舍提供了定量依据．对于近地卫星，如果只要求达到一阶解精度(定轨精度为 $\mathbf { 1 0 ^ { - 5 } - 1 0 ^ { - 6 } }$ ，相应的地面定位精度为 $\mathbf { 1 0 m { - } 1 0 0 m } )$ ，太阳轨道和月球轨道都可以取为不变圆；对于远地卫星，太阳轨道应取为不变椭圆，而月球轨道情况则要复杂些,在上述精度要求下，显然要考虑其各种周期变化和长期变化（对应L3),如果计算弧段稍短些(如同步卫星，10天以内的弧段)，则周期变化部分只要考虑主要几项(对应 $I 2 )$ 即可

# 8.3 日月摄动解

关于日月引力摄动的分析研究，古在由秀等人曾有过较完善的工作[4-6]。这里为了清楚地表明日月摄动的规律，不妨针对近地卫星给出一般精度要求下的一阶摄动解，这同时也可满足一些人卫工作的需要．在这一前提下，只要取摄动函数 $\overrightarrow { R }$ 中的第一大部分即可，而且相应的(8.12)一(8.14)式可简化成下列形式：

$$
\left. \begin{array} { l } { \displaystyle \left( \frac { 1 } { r ^ { \prime } } \right) ^ { 3 } = \left( \frac { 1 } { r _ { 0 } ^ { \prime } } \right) ^ { 3 } , } \\ { \displaystyle \left( \frac { 1 } { r ^ { \prime } } \right) ^ { 3 } \cos 2 u ^ { \prime } = \left( \frac { 1 } { r _ { 0 } ^ { \prime } } \right) ^ { 3 } \cos 2 L ^ { * } , } \\ { \displaystyle \left( \frac { 1 } { r ^ { \prime } } \right) ^ { 3 } \sin 2 u ^ { \prime } = \left( \frac { 1 } { r _ { 0 } ^ { \prime } } \right) ^ { 3 } \sin 2 L ^ { * } . } \end{array} \right\}
$$

对于一阶解,无论是按第五章的平均根数法，或是按第七章的

一般变换方法，都很容易给出具体结果，事实上，由(8.35)式不难看出，摄动函数 $\overrightarrow { R }$ 的右端， $\biggl ( 1 + \frac { 3 } { 2 } e ^ { 2 } \biggr ) D _ { 1 }$ 这一部分有不含慢变量$\Omega , \omega , u ^ { \prime }$ （即 $\pmb { L } ^ { * } ) , \cdots$ 的项,即

$$
\frac { 3 } { 8 } \frac { m ^ { \prime } } { r _ { 0 } ^ { ' 3 } } a ^ { 2 } \biggl [ \frac { 2 } { 3 } \biggl ( 1 + \frac { 3 } { 2 } e ^ { 2 } \biggr ) \biggl ( 1 - \frac { 3 } { 2 } \sin ^ { 2 } i \biggr ) \biggr ( 1 - \frac { 3 } { 2 } \sin ^ { 2 } i ^ { \prime } \biggr ) \biggr ] .
$$

因此，在日月摄动下，只有 $\Omega , \omega , M$ 这三个根数有真正的长期变化.摄动函数 $\bar { R }$ 的其它部分都将引起卫星轨道根数发生长周期变化，其中与月球运动有关的项变化稍为快些．如果要严格按平均根数法或变换方法，将长期项和长周期项分开，则必须重新整理(8.35)式右端的第一大部分，这并不困难，根据 $\mathscr { D } _ { j } ( j = 1 , \cdots , 9 )$ 的定义(8.37)式，不难给出 $\pmb { \bar { R } }$ 分离后的两个部分，即

$$
{ \cal { R } } _ { 2 c } = \frac { 3 } { 8 } \beta a ^ { 2 } \bigg \{ \frac { 2 } { 3 } \bigg ( 1 + \frac { 3 } { 2 } e ^ { 2 } \bigg ) \bigg ( 1 - \frac { 3 } { 2 } \sin ^ { 2 } i \bigg ) \bigg ( 1 - \frac { 3 } { 2 } \sin ^ { 2 } i ^ { \prime } \bigg ) \bigg \} ,
$$

$$
\begin{array} { r l } { \mathbb { E } _ { \geq 2 } = \frac { 3 } { 8 } \beta \beta \delta ^ { 4 } \Big [ \Big ( 1 + \frac { 3 } { 2 } \alpha ^ { 4 } \varepsilon ^ { \prime } \Big ) \bigg ] \Big ( ( 1 - \frac { 3 } { 2 } \sin ^ { 4 } \alpha ) ^ { 4 } \Big ) \sin ^ { 3 } \alpha ^ { 3 } \exp 2 L ^ { \phi } } & { } \\ & { \quad \times + \frac { 1 } { 2 } \sin 2 4 \sin 2 \beta \cos ( \Omega - \beta ^ { \prime } ) } \\ & { \quad \quad + \frac { 1 } { 2 } \sin ^ { 4 } \alpha \sin ^ { 4 } \alpha ^ { 4 } \cos ( 2 \beta - \alpha ^ { \prime } ) } \\ & { \quad \quad - \frac { 1 } { 2 } \sin ^ { 4 } \alpha ^ { 3 } \sin ^ { 4 } \beta \cos 2 ( \Omega - \beta ^ { \prime } ) } \\ & { \quad \quad - \frac { 1 } { 2 } \sin ^ { 2 } \alpha \sin \beta \sin ^ { 4 } \gamma ( ( 1 + \cos \beta ^ { \prime } ) \cos ( \Omega - \beta ^ { \prime } - 2 L ^ { \prime } ) ) } \\ & { \quad \quad \times ( 1 - \cos \beta ^ { \prime } ) \cos ( \Omega - \beta ^ { \prime } + \beta L ^ { \prime } ) ) \quad \quad \quad } \\ & { \quad + \frac { 1 } { 4 } \sin ^ { 4 } \alpha ^ { 3 } \sin ^ { 4 } \big ( ( 1 - \cos \beta ^ { \prime } ) ^ { 2 } \cos 2 ( \Omega - \beta ^ { \prime } - L ^ { \prime } ) \big ) } \\ & { \quad \quad + ( 1 - \cos \alpha ^ { \prime } ) ^ { 4 } \cos 2 ( \Omega - \beta ^ { \prime } + L ^ { \prime } ) ) \quad } \\ & { \quad \quad + ( 1 - \cos \beta ^ { \prime } ) \cos 2 ( \Omega - \beta ^ { \prime } + L ^ { \prime } ) ) \quad ] } \end{array}
$$

$$
\begin{array} { r l } & { \quad + \frac { 3 } { 4 } \sin ^ { 2 } \sin ^ { 2 } \psi ( \cos 2 ( \theta - L ^ { * } ) + \cos 2 ( \omega + L ^ { * } ) ) } \\ & { \quad + \frac { 1 } { 2 } \sin i \sin 2 \psi ( ( 2 - \cos \theta ) \cos ( \mathcal { Q } - \mathcal { Q } ^ { \prime } - 2 \omega ) } \\ & { \quad - ( 1 + \cos \theta ) \cos ( \mathcal { Q } - \mathcal { Q } ^ { \prime } - 2 \omega ) } \\ & { \quad - ( ( \lambda ^ { 2 } - \epsilon \epsilon \delta ) \cos ( \mathcal { Q } - \mathcal { Q } ^ { \prime } - 1 / 2 \omega ) ) + \frac { 1 } { 4 } \sin ^ { 4 } \theta \sin ^ { 2 } ( ( 1 - \cos \theta ) ) ^ { 2 } } \\ & { \quad \cos \theta ( 2 - \mathcal { Q } ^ { \prime } - \omega ) + ( 1 + \cos \theta ) ^ { 2 } \cos 2 ( \mathcal { Q } - \mathcal { Q } ^ { \prime } \{ \omega \} ) } \\ & { \quad - \frac { 2 } { 2 } \sin i \sin ^ { 4 } \theta \sin ^ { 2 } ( 1 - \cos \theta ) ( ( 1 + \cos \theta ) ^ { 4 } ) } \\ & { \quad \cos ( \mathcal { Q } - \mathcal { Q } ^ { \prime } - 2 \omega - 2 L ^ { * } ) } \\ & { \quad - ( ( \lambda ^ { 2 } - \cos ^ { 2 } \theta ) \cos ( \mathcal { Q } - \mathcal { Q } ^ { \prime } - 2 \omega ) + 2 L ^ { * } ) } \\ & { \quad + \frac { 2 } { 2 } \sin i \sin i ^ { 4 } ( 1 + \cos \theta ) ( ( 1 + \cos \theta ^ { \prime } ) ) } \end{array}
$$$$
\begin{array} { r l } & { \quad , \quad \zeta = { \bf O } ( { \bf O } ^ { - 1 } ) , \quad \psi = { \bf O } ( { \bf O } ^ { - 1 } ) } \\ & { \quad \le \sigma \le ( 2 ( { \bf O } - \delta ^ { 2 } - \sigma ) + ( 1 + \epsilon \sigma ) ) ^ { \epsilon } \eta + 2 ( { \bf O } - \sigma ^ { 2 } ) \cdot ( { \bf O } + { \bf O } ^ { - 1 } ) } \\ & { \quad - \frac { 1 } { 2 } \epsilon \eta \sin \delta \eta + ( 1 + \epsilon \sigma ) ( \zeta _ { 1 } + \epsilon \sigma ) \cdot ( { \bf O } + { \bf O } ^ { - 1 } ) } \\ & { \quad = \epsilon \left( \zeta - \sigma \right) \cdot ( - \zeta = 2 ( { \bf O } ^ { - 1 } ) ) } \\ & { \quad - ( 1 - \epsilon \sigma ) \cdot ( \zeta ) - \sigma \left( \zeta - \sigma ^ { 2 } - \zeta _ { 0 } \right) \cdot ( { \bf O } ^ { - 1 } ) \cdot ( { \bf O } ^ { - 1 } ) } \\ & { \quad + \frac { 1 } { 2 } \frac { \eta } { 2 } \sin \delta \sin \left( \zeta + \sin \theta \right) \cdot ( \zeta ( { \bf O } + \cos \theta ) ) } \\ & { \quad - \epsilon \eta \le ( \zeta - \sigma ^ { 2 } ) \cdot ( 1 - \epsilon \sigma ) \cdot \cos ( \zeta - \sigma ) \cdot ( 3 \sigma + 1 \cdot \psi ) } \\ & { \quad \quad \quad \times \frac { 1 } { 3 } \left( { \bf I } - \cos \theta \right) \cdot ( \zeta ( 1 + \epsilon \sigma ) \cdot \eta ) \cdot \cos ( 2 \cdot \psi - 2 \cdot \zeta _ { 1 } ) } \\ & { \quad \quad - ( 1 - \epsilon \sin \zeta ) \cdot \cos ( \zeta ( { \bf O } - \delta ^ { 2 } - \sigma - \zeta _ { 1 } \cdot \psi ) ) } \\ & { \quad \quad + \frac { \eta } { 3 } \left( { \bf I } + \sin \theta \right) \cdot ( \zeta ( 1 + \epsilon \sigma ) \cdot \zeta ) \cos ( 2 \cdot \psi - \sigma ^ { 2 } \cdot \psi ) } \\ & { \quad \quad + ( 1 - \epsilon \sigma ) \cdot \sigma \left( \zeta - \sigma ^ { 2 } \cdot \zeta _ { 1 } \right) \cdot ( { \bf O } ^ { - 1 } ) \cdot ( { \bf O } ^ { - 1 } ) \cdot ( { \bf O } ^ { - 1 } ) \cdot ( { \bf O } ^ { - 1 } ) \cdot ( { \bf O } ^ { - 1 } ) } \\ &  \quad + ( 1 - \epsilon \sigma ) \cdot ( \zeta - \sigma  \end{array}
$$

其中 $\pmb { \beta } { = } m ^ { \prime } / r _ { 0 } ^ { \prime } { } ^ { 3 }$ 对于太阳， $\Omega ^ { \prime } { = } 0 .$ ，对于月球，根据(8.32)式可知，$\Omega ^ { \prime }$ 的变化取决于 $\pmb { \Omega }$ ，的变化,其变率很小，量级为 $1 0 ^ { - 5 }$ 因此，从$\pmb { R } _ { 2 l }$ 的形式不难看出，长周期项的变化情况由 $\Omega , \omega , L ^ { * }$ （实为日、月平黄经 $L$ 和 $L ^ { \prime }$ )三个量确定．在一定条件下会出现通约情况，例如太阳同步卫星(即轨道面跟着太阳“跑"的卫星)，轨道升交点总经度 $\boldsymbol { \Omega }$ 的变率与太阳平黄经的变率相等．这一问题在第六章中已仔细讨论过，并无困难，而在实际计算中，把相应的通约项按长期项积分即可.

然而,对于近地卫星,按照前面的估计,日、月摄动力的量级只有 $1 0 ^ { - 7 }$ ，比二阶小量还小．因此，在一阶解前提下计算日月摄动时，没有必要严格区分上述两种项，但为了考虑到月球运动较快，并能将日、月摄动两种表达式写成统一形式，仅需区分(8.35)式中的非日、月运动项和日，月运动项即可.前者给出二阶长期项 $\sigma _ { 2 } ( t$ $- t _ { 0 } )$ ，而后者则给出一阶长周期项 $\sigma _ { \imath } ^ { ( 1 ) } ( t )$ ，相应的公式如下：

$$
{ a _ { 2 } } = 0 ,
$$

$$
e _ { 2 } = - \bigg ( \frac { 1 5 } { 8 } \beta \bigg ) a ^ { 3 / 2 } \sqrt { 1 - e ^ { 2 } } e ( D _ { 5 } \cos 2 \omega - D _ { 3 } \sin 2 \omega ) ,
$$

$$
\begin{array} { r l r } {  { \hat { \mathbf { \Sigma } } } } \\ & { } & { \dot { i } _ { 2 } { = } ( \frac { 3 } { 8 } \beta ) \frac { \mathfrak { c } \sec i } { \sqrt { 1 - e ^ { 2 } } } a ^ { 3 / 2 } \Big \vert { - } 2 \Big ( 1 { + } \frac { 3 } { 2 } e ^ { 2 } \Big ) D _ { 1 0 } { - } 5 e ^ { 2 } ( D _ { 1 1 } \cos 2 \omega  } \\ & { } & {  + D _ { 1 6 } \sin 2 \omega ) { + } 5 e ^ { 2 } \cos i ( D _ { 5 } \cos 2 \omega { - } D _ { 3 } \sin 2 \omega ) \Big \vert , ( 8 { + } \frac { 4 } { 3 }  } \end{array}
$$

$$
\mathcal { Q } _ { 2 } = \biggr ( \frac { 3 } { 8 } \beta \biggr ) \frac { c s c i } { \sqrt { 1 - e ^ { 2 } } } a ^ { 3 / 2 } \biggr [ 2 \biggr ( 1 + \frac { 3 } { 2 } e ^ { 2 } \biggr ) D _ { 1 9 } - 5 e ^ { 2 } ( D _ { 1 9 } \cos 2 \omega
$$

$$
 - D _ { 2 1 } \sin 2 \omega ] \} ,
$$

$$
\omega _ { 2 } { = } \left( \omega _ { 2 } \right) _ { 1 } { + } \left( \omega _ { 2 } \right) _ { 2 }
$$

$$
\left. \omega _ { 2 } \right. _ { 1 } = - \cos i \Omega _ { 2 } ,
$$

$$
\begin{array} { r l } & { M _ { 1 } = - \sqrt { 1 - e ^ { 2 } } ( \omega _ { 2 } ) _ { 2 } } \\ & { \qquad - \frac { 3 } { 4 } \beta a ^ { 3 / 2 } \biggl [ 2 \biggl ( 1 + \frac { 3 } { 2 } e ^ { 2 } \biggr ) D _ { 1 } + 5 e ^ { 2 } ( D _ { 3 } \cos 2 \omega + D _ { 5 } \sin 2 \omega ) \biggr ] . } \end{array}
$$

$$
\begin{array} { r l r } & { a _ { l } ^ { ( 1 ) } ( t ) = 0 , } & { \mathrm { ( } } \\ & { \cdot e _ { \mathrm { \ell } } ^ { ( 1 ) } ( t ) = - \Big ( \frac { 1 5 } { 8 } \beta \Big ) a ^ { 3 / 2 } \sqrt { 1 - e ^ { 2 } } e \bigg [ ( D _ { 6 } \cos 2 \omega - D _ { 4 } \sin 2 \omega ) } \\ & { \times \frac { \sin 2 u ^ { \prime } } { 2 n ^ { \prime } } - ( D _ { 8 } \cos 2 \omega - D _ { 8 } \sin 2 \omega ) \frac { \cos 2 u ^ { \prime } } { 2 n ^ { \prime } } \bigg ] , } & { \mathrm { ( } } \end{array}
$$

$$
\begin{array} { l } { \displaystyle \hat { u } ^ { ( 1 ) } ( t ) = \biggl ( \frac { 3 } { 8 } \beta \biggr ) \frac { \csc i } { \sqrt { 1 - { e ^ { 2 } } } } a ^ { s / 2 } \biggl \{ - \biggl [ 2 \biggl ( 1 + \frac { 3 } { 2 } e ^ { 2 } \biggr ) D _ { 1 2 } } \\ { \displaystyle \qquad + 5 e ^ { 2 } ( D _ { 1 3 } \cos 2 \omega + D _ { 1 7 } \sin 2 \omega ) } \\ { \displaystyle \qquad - 5 e ^ { 2 } \cos i \left( D _ { 6 } \cos 2 \omega - D _ { 4 } \sin 2 \omega \right) \biggr ] \frac { \sin 2 \hat { u } ^ { \prime } } { 2 \pi ^ { \prime } } } \\ { \displaystyle \qquad + \biggl [ 2 \biggl ( 1 + \frac { 3 } { 2 } e ^ { 2 } \biggr ) D _ { 1 4 } + 5 e ^ { 2 } ( D _ { 1 5 } \cos 2 \omega + D _ { 1 8 } \sin 2 \omega ) } \\ { \displaystyle \qquad - 5 e ^ { 2 } \cos i \left( D _ { 0 } \cos 2 \omega - D _ { 8 } \sin 2 \omega \right) \biggr ] \frac { \cos 2 \hat { u } ^ { \prime } } { 2 \pi ^ { ' } } \biggr \} , ~ \mathrm { } \mathrm { } ( 8 . } .  \end{array}
$$

$$
\begin{array} { r l } & { \qquad \cdot \Bigl ( - \frac { 1 } { 8 } \Bigr ) \cos { 2 \omega } - D _ { 0 } \sin { 2 \omega } \Bigr ) \Biggr ] \stackrel { \cos { 2 \omega t } { \cos { 2 \omega } } } { \longrightarrow } \Biggr \} , } \\ & { \qquad - 5 e ^ { 2 \cos { \theta } } + ( D _ { 0 } \cos { 2 \omega } - D _ { 0 } \sin { 2 \omega } ) \Biggr ] \stackrel { \cos { 2 \omega t } { \sin ^ { \prime } { 2 \theta } } } { \longrightarrow } \Biggr \} , } \\ & { \qquad \quad \Omega _ { 0 } ^ { ( 1 ) } ( t ) = \left( \frac { 3 } { 8 } \beta \right) \underbrace { \frac { \cos { \alpha t } } { \sqrt { 1 - e ^ { 2 \alpha } } } } _ { \longrightarrow } a ^ { 1 / 2 } \left( \left[ 2 \right] \left( 1 + \frac { 3 } { 2 } e ^ { 2 } \right) D _ { 2 0 } \right. } \\ & { \qquad \left. - 5 e ^ { 2 } ( D _ { 2 \theta } \cos { 2 \omega } - D _ { 2 2 } \sin { 2 \omega } ) \right) \Biggr ] \stackrel { \sin { \theta } { \sin { 2 \theta } } } { \longrightarrow } \Biggr \} , } \\ & { \qquad - \biggl [ 2 \biggl ( 1 + \frac { 3 } { 2 } e ^ { 2 } \biggr ) D _ { 2 3 } - 5 e ^ { 2 } ( D _ { 2 \theta } \cos { 2 \omega } } \\ & { \qquad - D _ { 2 4 } \sin { 2 \omega } ) \int \frac { \cos { 2 \theta } { \sin ^ { \prime } { 2 \theta } } } { 2 \pi ^ { 2 } } \biggr \} , } \end{array}
$$

$$
\begin{array} { r l } & { \quad \frac { \partial \hat { \mathcal { A } } ( t ) } { \partial t } ( t ) = \mathrm { [ s i n ' ~ } ( \partial \phi ( t ) ) ] _ { \pm } [ - \mathrm { [ o r ~ } ( \partial \phi ( t ) ) \hat { z } + \mathrm { [ o r ~ } ( \partial \phi ( t ) ) \hat { z } ) \quad  } \\ & {  \mathrm { [ s i n ' ~ } ( \partial \phi ( t ) ) _ { \pm } - \mathrm { [ - s i n ' ~ } \partial \phi ( t ) ) , \quad  } \\ &  \quad  \mathrm { [ s i n ' ~ } ( \partial \phi ( t ) ) _ { \pm } \mathrm { ] ] ^ { T } } \sqrt  \frac { \partial } { \partial t } \hat { z } ^ { 2 } \hat { z } ^ { 2 } \hat { z } ^ { 2 } \hat { z } ^ { 2 } \hat { z } ^ { 2 } \hat { z } ^ { 2 } \hat { z } ^ { 2 } \hat { z } ^ { 2 } \hat { z } ^ { 2 } \hat { z } ^ { 2 } \hat { z } ^ { 2 } \hat { z } ^ { 4 } \hat { z } ^ { 2 } \hat { z } \hat { z } ^ { 2 } \hat { z } ^ { 4 } \hat { z } ^ { 2 } \hat { z } \hat { z } ^ { 2 } \hat { z } ^ { 2 } \hat { z } ^ { 4 } \hat { z } \hat { z } ^ { 2 } \hat { z } ^ { 2 } \hat { z } ^ { 2 } \hat { z } ^ { 2 } \hat { z } ^ { 4 } \hat { z } \hat { z } ^ { 2 } \hat { z } ^ { 2 } \hat { z } ^ { 2 } \hat { z } ^ { 2 } \hat { z } ^ { 2 } \hat { z } ^ { 2 } \hat { z } ^ { 2 } \hat { z } ^ { 2 } \hat { z } ^ { 2 } \hat { z } ^ { 2 } \hat { z } ^ { 2 } \hat { z } ^ { 2 } \hat { z } ^ { 2 } \hat { z } ^ { 2 } \hat { z } ^ { 2 } \hat { z } ^ { 2 } \hat { z } ^ { 2 } \hat { z } ^ { 2 } \hat { z } ^ { 2 } \hat { z } ^ { 2 } \hat { z } ^ { 2 } \hat { z } ^ { 2 } \hat { z } ^ { 2 } \hat { z } ^ { 2 } \hat { z } ^ { 2 } \hat { z } ^ { 2 } \hat { z } ^ { 2 } \hat { z } ^ { 2 } \hat { z } ^ { 2 } \hat { z } ^ { 2 } \hat { z } ^ { 2 } \hat { z } ^ { 2 } \hat { z } ^ { 2 } \hat { z } ^  2  \end{array}
$$

这里 $\beta = m ^ { \prime } / r _ { 0 } ^ { \prime } , u ^ { \prime } { = } L ^ { * } , n ^ { \prime }$ 是日、月平黄经的变化率，见(8.5)式和（8.6）式， $D _ { 1 9 } \cdots D _ { 9 }$ 见（8.37）式，而 $\pmb { { \cal D } } _ { 1 0 } , \cdots , \pmb { { \cal D } } _ { 2 4 }$ 由下列各式表达：

$$
\begin{array} { r l } & { B _ { x , z } = A _ { 4 } A _ { 1 } ^ { \prime } \mid A _ { 4 } A _ { 4 } ^ { \prime } \mid B _ { 4 } B _ { 5 } ^ { \prime } \mid B _ { 4 } B _ { 5 } ^ { \prime } , } \\ & { D _ { y , z } = A _ { 4 } A _ { 4 } ^ { \prime } + A _ { 4 } A _ { 4 } ^ { \prime } - B _ { 4 } B _ { 4 } ^ { \prime } - B _ { 4 } B _ { 5 } ^ { \prime } , } \\ & { D _ { z , z } = A _ { 4 } A _ { 4 } ^ { \prime } - A _ { 4 } A _ { 4 } ^ { \prime } + B _ { 4 } B _ { 5 } ^ { \prime } - B _ { 4 } B _ { 6 } ^ { \prime } , } \\ & { D _ { z , z } = A _ { 4 } A _ { 4 } ^ { \prime } - A _ { 4 } A _ { 5 } ^ { \prime } - B _ { 4 } B _ { 5 } ^ { \prime } - B _ { 4 } B _ { 6 } ^ { \prime } , } \\ & { D _ { y , z } = A _ { 4 } A _ { 4 } ^ { \prime } - A _ { 4 } A _ { 4 } ^ { \prime } + B _ { 5 } B _ { 4 } ^ { \prime } - B _ { 4 } B _ { 5 } ^ { \prime } , } \\ & { D _ { z , z } = A _ { 4 } A _ { 4 } ^ { \prime } + A _ { 4 } A _ { 4 } ^ { \prime } - B _ { 4 } B _ { 5 } ^ { \prime } - B _ { 4 } B _ { 6 } ^ { \prime } , } \\ & { D _ { y , z } = A _ { 4 } A _ { 4 } ^ { \prime } + A _ { 4 } A _ { 4 } ^ { \prime } - B _ { 4 } B _ { 5 } ^ { \prime } - B _ { 4 } B _ { 6 } ^ { \prime } , } \\ & { D _ { z , z } = A _ { 4 } B _ { 4 } ^ { \prime } - A _ { 4 } A _ { 4 } ^ { \prime } - B _ { 4 } B _ { 5 } ^ { \prime } - A _ { 4 } B _ { 6 } ^ { \prime } , } \\ & { D _ { y , z } = A _ { 4 } B _ { 4 } ^ { \prime } + A _ { 4 } B _ { 4 } ^ { \prime } - A _ { 4 } B _ { 4 } ^ { \prime } - A _ { 4 } B _ { 5 } ^ { \prime } , } \\ &  D _ { y , z } = A _ { 4 } B _ { 4 } ^ { \prime } + B _ { 4 } ^ { \prime } - B _ { 4 } B _ { 4 } ^ { \prime } - A \end{array}
$$

上述各式中的 $A _ { 1 } ^ { \prime } , A _ { 2 } ^ { \prime } , B _ { 1 } ^ { \prime } , B _ { 2 } ^ { \prime }$ 是 $A _ { 1 } , A _ { 2 } , B _ { 1 } , B _ { 2 }$ 对 $\pmb { \Omega }$ 的偏导数， $\mathcal { B } _ { \mathbf { i } } ^ { \dagger }$ ，$B _ { 2 } ^ { \prime \prime }$ 则是 $\mathcal { B } _ { 1 } , \mathcal { B } _ { 2 }$ 对 $\textbf { \textit { i } }$ 的偏导数，由(6.27)式求出，即

$$
\left. \begin{array} { r l } { A _ { 1 } ^ { \prime } = - \sin \left( \Omega - \Omega ^ { \prime } \right) , } & { \quad A _ { 2 } ^ { \prime } = \cos i ^ { \prime } \cos \left( \bar { \varOmega } - \bar { \varOmega } ^ { \prime } \right) , } \\ { B _ { 1 } ^ { \prime } = - \cos i \cos \left( \Omega - \bar { \varOmega } ^ { \prime } \right) , } & { \quad B _ { 2 } ^ { \prime } = - \cos i \cos i ^ { \prime } \sin \left( \bar { \varOmega } - \bar { \varOmega } ^ { \prime } \right) , } \\ { B _ { 1 } ^ { \prime } = \sin i \sin \left( \Omega - \bar { \varOmega } ^ { \prime } \right) , } & { \quad B _ { 2 } ^ { \prime \prime } = \cos i \sin i ^ { \prime } - \sin i \cos i ^ { \prime } . } \\ & { \quad \quad \times \cos \left( \bar { \varOmega } - \bar { \varOmega } ^ { \prime } \right) . } \end{array} \right\}
$$

$\sigma _ { z }$ 和 $\sigma _ { i } ^ { ( i ) } ( t )$ 的各表达式右端出现的根数均为平均根数，如果计算弧段较长， $\varOmega$ 和 $\pmb { \omega }$ 可按下式取值：

$$
\left. \begin{array} { r } { \Omega = \overline { { \Omega } } _ { 0 } + \frac { 1 } { 2 } \Omega _ { 1 } ( t - t _ { 0 } ) , } \\ { \quad } \\ { \omega = \varpi _ { 0 } + \frac { 1 } { 2 } \omega _ { 1 } ( t - t _ { 0 } ) . } \end{array} \right\}
$$

$\Omega _ { 1 }$ 和 ${ \pmb { \omega } } _ { 1 }$ 即由 $\pmb { \mathscr { J } _ { 2 } }$ 项摄动给出的一阶长期项系数，见第五章相应的(5.87)式．在同时考虑 ${ \pmb J } _ { 2 }$ 项摄动时， $\pmb { \sigma } _ { \textbf { i } } ^ { ( \pm ) } ( t )$ 除上述直接部分外，还有间接部分(联合项),即

$$
\int ^ { 1 } \biggl [ \sum _ { j } \frac { \partial f _ { l o } } { \partial \sigma _ { j } } ( \sigma _ { i } ^ { ( i ) } ) _ { j } \biggr ] d t = \int ^ { t } \biggl [ \frac { \partial f _ { l o } } { \partial e } e _ { l } ^ { ( 1 ) } + \frac { \partial f _ { l o } } { \partial i } i _ { l } ^ { ( 1 ) } \biggr ] d t .
$$

其中 $f _ { 1 6 }$ 是 $\pmb { J _ { 2 } }$ 对应的量，其意义和具体形式见第五章(5.83)式, $\pmb { e } _ { t } ^ { ( 1 ) }$ 和 $\pmb { i } _ { \lambda } ^ { ( 1 ) }$ 见(8.48)和(8.49)式，这里不再写出.

# $\ S 8 . 4$ 适用于任意偏心率的日月摄动计算公式

尽管上一节给出的日月摄动计算公式中并无小偏心率问题和临界角问题，但为了和地球形状摄动计算公式统一，使其适应各种情况，仍采用第六章 $\ S \ B . \ 4$ 中给出的消除奇点的摄动计算方法，取下述变量：

$$
a , i , \Omega , \xi = e \cos \omega , \eta = - e \sin \omega , \lambda = M + \omega ,
$$

并引进拟平均根数，具体方法不再重复，相应的计算公式由上一节的结果化为新变量的形式如下：

$$
a _ { 2 } ( t - t _ { 0 } ) + [ a _ { l } ^ { ( 1 ) } ( t ) - a _ { l } ^ { ( 1 ) } ( t _ { 0 } ) ] = 0 ,
$$

$$
\begin{array} { r l } & { \quad _ { i \in \{ i - \frac { 3 } { 2 } \} } , \quad _ { i \in \{ i \} } , } \\ & { = ( \frac { 3 } { 8 } \beta ) \sqrt { \frac { \pi ^ { 2 } } { \sqrt { 1 - e ^ { \frac { 3 } { 2 } } } } [ \sum _ { j = 1 } ^ { i } ( \frac { 3 } { 2 } + \frac { 3 } { 2 } e ^ { \frac { \pi ^ { 2 } } { 4 } } ) W _ { z } + \bar { \Phi } ( \xi ^ { 2 } - \eta ^ { 2 } ) W _ { x }  } } \\ &  \quad - \frac { 1 0 5 } { 8 } \beta ) \sqrt { \frac { \pi ^ { 2 } } { \sqrt { 1 - e ^ { \frac { 3 } { 2 } } } } [ \sum _ { j = 1 } ^ { i } ( \frac { 3 } { 2 } + \frac { 3 } { 2 } e ^ { \frac { \pi ^ { 2 } } { 4 } } ) W _ { z } + \bar { \Phi } ( \xi ^ { 2 } - \eta ^ { 2 } ) W _ { x }  } \\ & { \quad  - 1 0 5 \beta \eta W _ { x } ] ( \ell - t _ { 0 } ) } \\ & { \quad + [ \sum _ { j = 1 } ^ { i } ( 1 + \frac { 3 } { 2 } e ^ { \frac { \pi ^ { 2 } } { 4 } } ) W _ { i \cdot i } + \bar { \Phi } ( \xi ^ { 2 } - \eta ^ { 2 } ) W _ { i \cdot i - 1 0 } \xi \eta W _ { x } ] \frac { \sin 2 \pi ^ { 2 } - \sin 2 \pi ^ { 2 } } { 2 \pi ^ { 2 } } } \\ & { \quad + [ - 2 ( 1 + \frac { 3 } { 2 } \frac { \pi ^ { 2 } } { 2 } e ^ { \frac { \pi ^ { 2 } } { 4 } } ) W _ { \nu } - 5 ( \xi ^ { 2 } - \eta ^ { 2 } ) W _ { \nu } } \\ & { \quad - 1 0 5 \eta W _ { \nu } [ \frac { \log 2 \pi ^ { 2 } - \log 2 \pi _ { \nu } ^ { 2 } } { 2 \pi ^ { 2 } } ] , } \\ & { \quad { \mathfrak { A } } _ { 0 } ( i - t _ { 0 } ) \dots ( \mathrm { A r } ( i ) - \mathrm { A r } ( i ) ) . } \end{array}
$$

$$
\begin{array} { r l } & { \quad - s _ { 1 } , } \\ & { \quad - s _ { 2 } , } \\ & { \quad - s _ { 1 } ( s _ { 2 } - s _ { 2 } ) \nabla F _ { 1 } \cdot \frac { 2 s _ { 1 } \delta } { 2 s _ { 1 } } \nabla F _ { 1 } \cdot ( \delta - q _ { 1 } ) } \\ & { \quad + [ \frac { 3 } { 4 } ] ^ { s _ { 1 } } ( 1 - \frac { 3 } { 2 } q _ { 2 } ^ { s _ { 2 } } ) \nabla F _ { 1 } - S ( \delta ^ { 2 } - q _ { 2 } ^ { s _ { 3 } } ) \nabla F _ { 1 } } \\ & { \quad - 1 0 \delta \mathcal { F } _ { 1 } \cdot [ \frac { 1 } { 2 } \frac { \partial \delta \partial \delta ^ { 2 } } { \partial x } - q _ { 1 } \partial \delta \delta ] } \\ & { \quad + \frac { 1 } { 2 } \nabla ^ { 2 } ( 1 - \frac { 3 } { 2 } q _ { 2 } ^ { s _ { 1 } } ) \nabla F _ { 1 } \cdot \delta ( \delta ^ { 2 } - q _ { 2 } ^ { s _ { 2 } } ) \nabla F _ { 2 } } \\ & { \quad + 1 2 \delta \mathcal { F } _ { 1 } \cdot \nabla \delta \frac { 1 } { 2 } \frac { \partial \delta \partial \delta ^ { 2 } } { \partial x } - q _ { 1 } \partial \delta \delta ] } \\ & { \dot { \mathcal { L } } ( \delta ^ { 2 } - \delta _ { 1 } ) + \dot { \mathcal { L } } \partial \mathcal { F } ( \delta ^ { 2 } - \delta _ { 1 } \omega ) } \\ & { \quad - ( \frac { 3 } { 8 } \delta ) \dot { \mathcal { F } } _ { 1 } \cdot \frac { 2 \delta \partial \delta ^ { 2 } } { \partial x } \nabla \delta ^ { 2 } \Gamma _ { 1 } - \delta \mathcal { F } _ { 1 } \nabla F _ { 1 } - \delta \mathcal { F } _ { 1 } \nabla F _ { 1 } } \\ & { \quad - 1 0 \delta \mathcal { F } _ { 1 } \times \mathrm { H } ( \delta ^ { 2 } - \delta _ { 2 } ) } \\ & { \quad - 1 2 \delta \mathcal { F } _ { 1 } \times \mathrm { H } ( \delta - q _ { 1 } ^ { s _ { 2 } } ) } \end{array}
$$

$$
\begin{array} { r l } { \quad } & { \quad , \quad \quad \times \quad , \quad : \quad \times , \quad 1 0 ^ { 9 } I ^ { 9 } \times \frac { 1 - 1 8 8 9 } { 1 0 ^ { 8 } } \mathrm { W } _ { 3 } \dots \dots \dots \dots \dots } \\ { \quad } & { \quad \times \quad + 1 2 0 1 9 \pi \mathrm { W } _ { 4 } \dots 4 8 9 1 \mathrm { W } _ { 5 } \dots \underline { { \mathrm { t r } } } \underline { { \mathrm { s u p } } } \underline { { \mathrm { f o r } } } \dots \underline { { \mathrm { s u p } } } \underline { { \mathrm { f o r } } } \quad } \\ & { \quad \quad - \eta \in \mathrm { O } \pi \mathrm { i } \{ 2 Q _ { 2 } ( t - t _ { 2 } ) + 1 0 \hat { \mathcal { H } } _ { 3 } ^ { \top } ( t ) - \frac { \mathrm { t r } \hat { \mathcal { H } } _ { 4 } ^ { \top } ( t ) - \mathrm { t r } \hat { \mathcal { H } } _ { 4 } ^ { \top } ( t ) } { 2 0 } \} } \\ & { \quad \quad \quad \eta \mathrm { a s t } \quad \dots \quad + 1 2 0 ^ { 9 } I ^ { 9 } ( \xi ) \dots \eta \mathrm { t r } ( \xi ) \underline { { \mathrm { d } } } \xi \qquad \biggr ( \xi ) \dots \quad \mathrm { ( B \cdot l ) } , } \\ { \quad } & { \quad \quad \quad - ( \frac { 3 } { 8 } \beta ) \sqrt { 1 0 ^ { 8 } } \mathrm { W } _ { 3 } \dots \underline { { \mathrm { t r } } } \underline { { \mathrm { s u p } } } ^ { \mathrm { a } \cdot \mathrm { p } } \{ \Gamma - 4 \xi - \mathrm { t r } ( \theta \xi ) \underline { { W } } _ { 4 } \} + 2 6 4 \beta \mathcal { H } _ { 5 } \quad , } \\ & { \quad \quad \quad + 1 \partial \eta \mathrm { W } _ { 6 } \gamma ( \underline { { \mathrm { a } } } \dots \underline { { \mathrm { t r } } } ) } \\ &  \quad \quad \quad + \{ - 8 \xi \Psi _ { 8 } + 1 2 \xi \Psi _ { 8 } + 1 0 \} \frac { \Gamma } { \mathrm { W } _ { 3 } \alpha ^ { 2 } } \underline { { \mathrm { t r } } } \underline { { \mathrm { s u p } } } \frac { \partial } { \partial \tau } \underline { { \mathrm { s u p } } } \frac { \partial } { \partial \tau } \underline { { \mathrm { s u p } } } \frac { \partial } { \partial \tau } \ \end{array}
$$

$$
\begin{array} { r l } & { \mathbb { E } \{ \mathbf { J } _ { 1 } \} \cdot \sum _ { i = 1 } ^ { N } \mathcal { J } _ { 1 } ^ { \mu } \Big \{ ( \mathbf { J } _ { 2 } ^ { \nu } \cdot \mathbf { A } _ { i } ^ { \nu } ) ^ { \mu } \Big ( \mathbf { J } _ { 3 } ^ { \nu } \cdot \mathbf { A } _ { i } ^ { \nu } \Big ) } \\ & { = ( \frac { 3 } { N } ) \tilde { \mathbf { J } } _ { 3 } ^ { \mu } ) ^ { \mu + 2 } \Big ( \frac { 1 } { N } \Big ( \mathbf { J } _ { 1 } ^ { \mu } \cdot \mathbf { A } _ { i } ^ { \nu } \cdot \mathbf { a } _ { 2 } ^ { \nu } \Big ) - \boldsymbol { a } _ { 3 } ^ { \nu } \cdot \mathbf { J } _ { 1 } ^ { \mu } \cdot \frac { \lambda } { 2 } \frac { \lambda } { N } \tilde { \mathbf { J } } _ { 2 } ^ { \nu } \Big ) \tilde { \Psi } _ { 1 } } \\ & { \quad - \mathbb { E } \{ \mathbf { J } } _ { 3 } ^ { \mu } \cdot \mathbf { a } _ { 2 } ^ { \nu } \cdot \mathbf { J } _ { 3 } ^ { \mu } \cdot \mathbf { J } _ { 1 } ^ { \mu } \cdot \mathbf { J } _ { 1 } ^ { \mu } \cdot \mathbf { J } _ { 2 } ^ { \nu } \cdot \mathbf { J } _ { 2 } ^ { \nu } \cdot \mathbf { J } _ { 1 } ^ { \mu } \cdot \mathbf { J } _ { 2 } ^ { \nu } \cdot \mathbf { J } _ { 1 } ^ { \mu } \cdot \mathbf { J } _ { 2 } ^ { \nu } \cdot \mathbf { J } _ { 1 } ^ { \mu }  \\ &  \quad + \frac { 1 } { N } \cdot \sum _ { i = 1 } ^ { N } \frac { \mu _ { 0 } } { N } \Big ( \mathbf { J } _ { 1 } ^ { \mu } \cdot \mathbf { a } _ { 2 } ^ { \nu } \cdot \mathbf { a } _ { 3 } ^ { \nu } \cdot \mathbf { J } _ { 1 } ^ { \mu } \cdot \mathbf { J } _ { 1 } ^ { \mu } \cdot \mathbf { J } _ { 2 } ^ { \nu } \cdot \mathbf { J } _ { 2 } ^ { \nu } \cdot \mathbf { J } _ { 3 } ^ { \mu } \cdot \mathbf { J } _ { 1 } ^ { \mu } \cdot \mathbf { J } _ { 2 } ^ { \nu } \cdot \mathbf { J } _ { 3 } ^ { \mu } \cdot \mathbf { J } _ { 2 } ^ { \nu } \phantom  \Bigg )  \end{array}
$$

其中β,u的意义同前,而W,,W2o由下列各式定义：

$$
\left. \begin{array} { r l } & { \Psi _ { 1 } = - \displaystyle \frac { 1 } { 2 } \sin 2 i \cos 2 i ^ { \prime } + \frac { 1 } { 2 } \cos 2 i \sin 2 i ^ { \prime } \cos \left( \varOmega - \varOmega ^ { \prime } \right) } \\ & { \qquad + \displaystyle \frac { 1 } { 2 } \sin 2 i \sin ^ { 2 } i ^ { \prime } \cos ^ { 2 } \left( \varOmega - \varOmega ^ { \prime } \right) , } \\ & { \Psi _ { 2 } = \displaystyle \frac { 1 } { 2 } \cos i \sin 2 i ^ { \prime } \sin \left( \varOmega - \varOmega ^ { \prime } \right) } \\ & { \qquad + \displaystyle \frac { 1 } { 2 } \sin i \sin ^ { 2 } i ^ { \prime } \sin 2 ( \varOmega - \varOmega ^ { \prime } ) , } \\ & { \Psi _ { s } = - \Psi _ { 1 } - \sin 2 i \sin ^ { 2 } ( \varOmega - \varOmega ^ { \prime } ) , } \\ & { \Psi _ { 4 } = - \Psi _ { 2 } + \sin i \sin 2 ( \varOmega - \varOmega ^ { \prime } ) , } \end{array} \right\}
$$

$$
\begin{array} { r l } & { \Psi _ { \star } = - \exp 2 i \sin i ^ { \xi } \sin ( \Omega - \theta ^ { \prime } ) } \\ & { \qquad \quad + \frac { 1 } { 2 } \sin 2 i \cos i ^ { \xi } \sin ( 2 \Omega - \Omega ^ { \prime } ) , } \\ & { \qquad \quad - \cos i \sin ^ { \xi } \cos ( \Omega - \theta ^ { \prime } ) - \sin i \sin ^ { \xi } \cos ^ { 2 } ( \Omega - \theta ^ { \prime } ) , } \\ & { \Psi _ { \star } = \sin i ^ { \xi } \sin ^ { \xi } \sin ^ { \xi } \sin ( \Omega - \theta ^ { \prime } ) } \\ & { \qquad \quad + \cos i ^ { \xi } \sin ^ { \xi } i \sin ( \Omega - \theta ^ { \prime } ) } \\ & { \qquad \quad + \cos i ^ { \xi } \cos ^ { 2 } i ^ { \xi } \sin ^ { \xi } i \sin ^ { 2 } ( \Omega - \theta ^ { \prime } ) , } \\ & { \Psi _ { \star } = \cos ^ { \xi } i ^ { \xi } \cos ^ { 2 } i ^ { \xi } + \sin ^ { 2 } i ^ { \xi } \sin ^ { \xi } i ^ { \xi } \cos ^ { 2 } ( \Omega - \theta ^ { \prime } ) } \\ & { \qquad \quad + \frac { 1 } { 2 } \sin ^ { 2 } i \sin 2 i ^ { \xi } \cos ( 2 \Omega - \theta ^ { \prime } ) , } \\ & { \qquad \quad + - \mathcal { B } _ { \star } = - \mathcal { B } _ { \star } + [ \sin ^ { \xi } i ^ { \xi } \sin ^ { \xi } ( \Omega - \Omega ^ { \prime } ) ] , } \\ & { \Psi _ { \star } = - \frac { 1 } { 2 } \sin i ^ { \xi } i ^ { \xi } \sin ^ { \xi } ( 2 i - \Omega ^ { \prime } ) } \\ & { \qquad \quad - 1 - \cos i ^ { \xi } \cos ( \Omega - \theta ^ { \prime } ) , } \\ & { \qquad \quad 1 - \cos i ^ { \xi } \cos \theta . } \end{array}
$$

$$
\begin{array} { r l } & { \quad - \frac { 1 } { 2 } \operatorname { m i n } \{ \phi \} ^ { 2 } \operatorname* { i n } \{ \phi \} ^ { 2 } \operatorname* { i n } \{ \phi \} ^ { 2 } \partial ^ { 2 } \gamma , } \\ & { \quad \times _ { 1 } ^ { \mathrm { F r } } - 1 \dag , \ \mathrm { ~ 1 2 - 1 } \dag , \ \mathrm { ~ 2 1 - 1 } \dag , \ \mathrm { ~ 2 1 - 1 } \dag , \ \mathrm { ~ 2 1 - 2 } \dag , \ \mathrm { ~ 1 } } \\ &  \quad \times _ { 1 } \dag , \ \mathrm { ~ 1 } - 1 \dag , \ \ \mathrm { ~ 2 ( \phi - \phi ^ { \prime } ) } \dag , \ \mathrm { ~ 1 } \dag , \ \mathrm { ~ 1 } \dag , \ \mathrm { ~ 1 } \dag , \ \mathrm { ~ 2 } \dag , \qquad \phi \} \\ & { \quad - \left( \phi - \phi \right) \dag , \ \ \mathrm { ~ 1 } \dag , \ \ \mathrm { ~ 1 } \dag , \ \ \mathrm { ~ 2 } \dag , \ \qquad \phi \in \mathcal { O } ^ { \prime } \dag \} , } \\ & { \quad \Psi _ { i \mathrm { t } } = - \frac { 1 } { 2 } \dag , \ \ \mathrm { ~ 1 } \dag , \ \mathrm { ~ 2 } \dag , \ \qquad \mathrm { ~ ( \phi - \phi ^ { \prime } ) } , } \\ & { \quad \quad \mp \frac { 1 } { 2 } \dag , \ \mathrm { ~ 1 } \dag , \ \mathrm { ~ 2 } \dag , \ \qquad \mathrm { ~ ( \phi - \phi ^ { \prime } ) } \dag , \ \ \mathrm { ~ 1 } \dag , \ \ \mathrm { ~ 1 } \dag , \ \mathrm { ~ 2 } \dag , \ \qquad \mathrm { ~ 1 } \dag , \ \ } \\ & { \quad \times _ { 1 } \dag , \ \ \mathrm { ~ 1 } - 1 \dag , \ \ \mathrm { ~ 1 } \dag , \ \ \mathrm { ~ 2 } \dag , \ \qquad \mathrm { ~ 1 } \dag , \ \ \mathrm { ~ 2 } \dag , \ \qquad \mathrm { ~ 1 } \dag , \ \ } \\ &  \quad \times _ { 1 } \dag , \ \mathrm { ~ 1 } \dag , \ \mathrm { ~ 2 } \dag , \ \mathrm { ~ 1 } \dag , \ \mathrm { ~ 2 } \dag , \ \qquad \mathrm { ~ 1 } \dag , \ \mathrm { ~ 2 } \dag , \ \qquad \mathrm { ~ 1 } \dag , \ \mathrm { ~ 2 } \dag , \qquad \mathrm { ~ 1 } \dag , \ \mathrm { ~ 3 } \dag , \ \mathrm { ~ 3 } \dag , \qquad \mathrm  \end{array}
$$$$
\begin{array} { l } { { W _ { 1 \vartheta } = - W _ { 1 \vartheta } + 2 \cos ^ { 2 } i \sin ^ { 2 } ( \varOmega - \varOmega ^ { \prime } ) , } } \\ { { W _ { 2 0 } = \displaystyle \frac { 1 } { 2 } \cos i ^ { \prime } \sin 2 ( \varOmega - \varOmega ^ { \prime } ) . } } \end{array}
$$

上述各式中出现的根数均为平均根数,而Ω,，n可按下式取值：

$$
\begin{array} { l } { \displaystyle \Omega = \overline { { \Omega } } _ { 0 } + \frac { 1 } { 2 } \Omega _ { 1 } ( t - t _ { 0 } ) , } \\ { \displaystyle \xi = \xi _ { 0 } \cos \bigg [ \frac { 1 } { 2 } \omega _ { 1 } ( t - t _ { 0 } ) \bigg ] + \eta _ { 0 } \sin \bigg [ \frac { 1 } { 2 } \omega _ { 1 } ( t - t _ { 0 } ) \bigg ] , } \\ { \displaystyle \eta = \eta _ { 0 } \cos \bigg [ \frac { 1 } { 2 } \omega _ { 1 } ( t - t _ { 0 } ) \bigg ] - \xi _ { 0 } \sin \bigg [ \frac { 1 } { 2 } \omega _ { 1 } ( t - t _ { 0 } ) \bigg ] , } \end{array}
$$

该表达式的意义同(8.55)式.

# $\ S 8 . 5$ 地球扁率的间接摄动

由(8.4)式可知，地球扁率间接摄动力相对地球中心引力的大小(即摄动量级),近地卫星(如2卫星)为4×10-，远地卫星(如地球同步卫星)为2×10-10．因此，对于高精度问题，有时是要考虑该摄动的．首先讨论这一摄动的基本规律，为此，可利用(8.3)式写出地球扁率间接摄动对应的摄动函数，即

$$
{ \cal R } = J _ { 2 } m ^ { \prime } \biggl [ \frac { \partial } { \partial r ^ { \prime } } \biggl ( \frac { 1 } { r ^ { \prime 3 } } P _ { 2 } ( \sin \varphi ^ { \prime } ) \biggr ) \biggr ] ^ { \frac { \pi } { 2 } } \cdot r ,
$$

这里已采用标准计算单位，G=1，m是以地球质量为单位的月球质量。(8.64)式可进一步写成下列形式：

$$
R = \frac { 3 } { 2 } J _ { 2 } m ^ { \prime } \Big ( \frac { r } { r ^ { \prime 4 } } \Big ) [ ( 5 \sin ^ { 2 } \varphi ^ { \prime } - 1 ) \cos \psi - 2 \sin \varphi ^ { \prime } \sin \varphi ] ,
$$

其中sin𝜑',sinφ和cosψ可用月球和卫星的根数来表达，即

$$
\sin \varphi ^ { \prime } = \sin i ^ { \prime } \sin u ^ { \prime } , \sin \varphi = \sin i \sin u ,
$$

$$
\cos \psi = \frac { r ^ { \prime } } { r ^ { \prime } } \cdot \frac { r } { r } = \frac { 1 } { 2 } ( A _ { 1 } + B _ { 2 } ) \cos \left( u - u ^ { \prime } \right)
$$

$$
\begin{array} { c } { { \displaystyle + \frac { 1 } { 2 } ( A _ { \mathrm { t } } - B _ { 2 } ) \cos { ( u + u ^ { \prime } ) } } } \\ { { \displaystyle + \frac { 1 } { 2 } ( B _ { \mathrm { t } } - A _ { 2 } ) \sin { ( u - u ^ { \prime } ) } } } \end{array}
$$

$$
+ \frac { 1 } { 2 } ( B _ { 1 } + A _ { 2 } ) \sin { ( u + u ^ { \prime } ) } .
$$

',u'和A,A,B,B在S8.3中已出现过，不再说明。利用上述表达式,可将摄动函数 $\pmb { R }$ 写成根数形式：

$$
\begin{array} { r l } & { { \mathcal { R } } - ( \frac { \partial } { \partial x } \cdot L \rho ) \sqrt { \frac { \partial \theta } { \partial x } }  \frac { \partial \theta } { \partial x }  [ \frac { \partial \theta } { \partial x }  ( \frac { \partial \theta } { \partial x } )  \frac { \partial \theta } { \partial x } \cdot \Phi ( - \theta - \theta ^ { \prime } )  [ ( \frac { \partial \theta } { \partial x } \cdot \Phi ( \theta ^ { \prime } - \frac { \theta ^ { \prime } } { 2 } ) ) \cdot ( A _ { 1 } \cdot B _ { 2 } )  } \\ & {  \quad - \frac { \partial \theta } { \partial x } \cdot \Phi ( \theta ^ { \prime } ) \cdot ( A _ { 1 } - B _ { 2 } ) \cdot \exp \mathrm { i } \theta ^ { \prime } : \sin \theta ] } \\ & { \quad + \exp ( \alpha \cdot \pi ^ { 2 } ) [ ( \frac { \partial \theta } { \partial x } ) \mathrm { i } \theta ^ { \prime }  } \\ & { \quad - \frac { \theta } { 8 } \cdot \sin \theta ^ { \prime } \langle \mathcal { A } _ { 4 } \rangle + L \rho ] \cdot \exp \mathrm { i } \theta \cdot \frac { \partial \theta } { \partial x } \mathrm { i } } \\ & { \quad + \exp ( \alpha \cdot \theta \cdot \theta ^ { \prime } ) [ - \frac { \theta } { 8 } \sin ^ { 4 } \theta ^ { \prime } \langle \mathcal { A } _ { 4 } \cdot B _ { 2 } \rangle ] } \\ & { \quad + \cos ( \alpha \cdot \theta \cdot \theta ^ { \prime } ) [ - \frac { \theta } { 8 } \sin ^ { 4 } \theta ^ { \prime } \langle \mathcal { A } _ { 4 } \cdot B _ { 2 } \rangle ] } \\ & { \quad + \sin ( \alpha \cdot \theta ) \theta [ - ( \frac { \sqrt { 6 } } { 8 } \sin ^ { 4 } \theta ^ { \prime } \cdot \Phi ( - \theta _ { 2 } ) ) ] } \\ & { \quad - \sin ( \alpha \cdot \theta ^ { \prime } ) [ - ( \frac { \sqrt { 6 } } { 8 } \sin ^ { 2 } \theta ^ { \prime } - \frac { 1 } { 2 } ) \cdot ( \mathcal { A } _ { 4 } \cdot B _ { 2 } )  } \\ &  \quad  \frac { \sqrt { 6 } } { 8 } \sin ^ { 2 } \theta ] \cdot \exp \mathrm { i } \theta \cdot \frac { \sqrt { 6 } } { 8 } \sin ^ { 2 } \ \end{array}
$$$$
\begin{array} { r l } & { \quad \sum _ { j = 1 } ^ { S } \hat { u } ( \hat { x } , t ) } \\ & { = - \frac { \hat { \sigma } } { \beta } \sinh ^ { \prime } ( \hat { \gamma } ( \Delta + \hat { u } ^ { \dagger } ) + \sinh ^ { \prime } \hat { \gamma } ) , } \\ & { \quad + \operatorname* { c e t } ( \hat { \mathbf { x } } - \Delta \hat { \mathbf { y } } ) \Bigg [ - \frac { \hat { \mathbf { y } } } { \beta } \sinh ^ { \prime } ( \hat { \mathbf { z } } + \hat { \mathbf { z } } ^ { \dagger } ( \hat { \mathbf { z } } _ { 1 } - \hat { \mathbf { z } } _ { 2 } ) ) } \\ & { \quad + \cosh ( \alpha + \Delta \hat { \mathbf { z } } ) \Bigg [ - \frac { \sqrt { 3 } } { \beta } \sinh ^ { \prime } ^ { \prime } ( \Delta + \hat { \mathbf { z } } ^ { \dagger } ( \hat { \mathbf { z } } _ { 1 } - \hat { \mathbf { z } } _ { 2 } ) ) } \\ & { \quad + \sin ( \alpha - \kappa ) \kappa \Big [ - ( \frac { \sqrt { 3 } } { \beta } \sinh ^ { \prime } ^ { \prime } ( \Delta + \hat { \mathbf { z } } ^ { \dagger } ( \hat { \mathbf { z } } - \hat { \mathbf { z } } ^ { \dagger } ) ) \Big ] ( \Delta - \hat { u } ^ { \dagger } ) } \\ & { \quad - \frac { \sqrt { 3 } } { \beta } \sin ^ { \prime } ( \hat { \mathbf { z } } ( \hat { \mathbf { z } } - \hat { \mathbf { z } } ^ { \dagger } ( \hat { \mathbf { z } } ) \Delta ) \Bigg ] } \\ & { \quad + \sin ^ { \prime } ( \hat { \mathbf { z } } - \hat { \mathbf { z } } ^ { \dagger } ( \hat { \mathbf { z } } + \hat { \mathbf { z } } ^ { \dagger } ( \hat { \mathbf { z } } ) \Delta ^ { \prime } ) } \\ & { \quad - \sin ^ { \prime } ( \hat { \mathbf { z } } ) ( \hat { \gamma } \frac { \sqrt { 3 } } { \sqrt { 3 } } \sinh ^ { \prime } ( \hat { \mathbf { z } } + \hat { \mathbf { z } } ^ { \dagger } ( \hat { \mathbf { z } } ) \Delta ^ { \prime } ) \Bigg ] ( \Delta + \hat { \mathbf { z } } ) } \\ &  \quad \times \frac  \sqrt { 3 } \end{array}
$$

其中 ${ \pmb \beta } = m ^ { \prime } / r ^ { \prime 3 }$

$$
\begin{array} { r l } & { A _ { 1 } + B _ { 2 } = ( 1 + \cos \dot { i } ^ { \prime } \cos \dot { i } ) \cos \left( \mathcal { Q } - \mathcal { Q } ^ { \prime } \right) + \sin \dot { i } ^ { \prime } \sin \dot { i } , } \\ & { A _ { 1 } - B _ { 2 } = ( 1 - \cos \dot { i } ^ { \prime } \cos \dot { i } ) \cos \left( \mathcal { Q } - \mathcal { Q } ^ { \prime } \right) - \sin \dot { i } ^ { \prime } \sin \dot { i } , } \\ & { A _ { 2 } + B _ { 1 } = ( \cos \dot { i } ^ { \prime } - \cos \dot { i } ) \sin \left( \mathcal { Q } - \mathcal { Q } ^ { \prime } \right) , } \\ & { A _ { 2 } - B _ { 1 } = ( \cos \dot { i } ^ { \prime } + \cos \dot { a } ) \sin \left( \mathcal { Q } - \mathcal { Q } ^ { \prime } \right) . } \end{array}
$$

显然,由于

$$
\overline { { { \Big ( \frac { r } { a } \Big ) \mathrm { c o s } f } } } = - \frac { 3 } { 2 } e \mp 0 ,
$$

在地球扁率间接摄动下，卫星根数(除a外)将有长周期变化．在非通约情况下,对于近地卫星,轨道根数的变化不大，量级为 $1 0 ^ { - 8 }$ ，而对远地卫星，根数的变化较大(因月球摄动本身就比较大),可达10-7．当然，若考虑的弧段不长，无论是近地卫星还是远地卫星，根数的变化都不大．下面给出近地卫星的几个算例，初始条件为

$$
\begin{array} { c } { { a = 8 0 5 9 . 0 0 3 0 9 3 \mathrm { ~ k m } , i = 5 0 ^ { \circ } . 0 , \Omega = 5 0 ^ { \circ } . 0 , \omega = 5 0 ^ { \circ } . 0 , } } \\ { { { \cal M } = 5 0 ^ { \circ } . 0 , } } \end{array}
$$

$\pmb { e }$ 分别取0.01,0.1,0.2,外推20圈,结果列于表8.3.

表8.3  

<table><tr><td rowspan=1 colspan=1>eo</td><td rowspan=1 colspan=1>摄动类型</td><td rowspan=1 colspan=1>a(km)</td><td rowspan=1 colspan=1>e</td><td rowspan=1 colspan=1>i（度）</td><td rowspan=1 colspan=1>λ=M+ω（度）</td><td rowspan=1 colspan=1>△i（弧度）</td><td rowspan=1 colspan=1>注</td></tr><tr><td rowspan=1 colspan=1>0.01</td><td rowspan=1 colspan=1>L1L2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.010</td><td rowspan=1 colspan=1>相对L1</td></tr><tr><td rowspan=1 colspan=1>0.1</td><td rowspan=1 colspan=1>LiL2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>相对L1</td></tr><tr><td rowspan=1 colspan=1>0.2</td><td rowspan=1 colspan=1>L</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>80.00</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>相对L1</td></tr></table>

表8.3中， $\pmb { L 1 }$ 的意义同表8.2中的 $\pmb { L 1 }$ ， $\pmb { L 2 }$ 是考虑地球扁率 $( J$ 项)的月球摄动。 $\pmb { L 2 }$ 与 ${ \pmb L } { \pmb 1 }$ 之间的差别(如 $\Delta \lambda$ )就是地球扁率间接摄动所引起的，即该摄动效应在20 圈内的体现，完全符合前面的量级估计，外推200圈(即 $1 0 ^ { 3 }$ 的弧段)的结果，可完全体现长周期变化的幅度,计算结果不再列出，其中 $L 2$ 相对 $\pmb { L 1 }$ 的差别 $\Delta \lambda$ 达$1 0 ^ { - 9 }$ 但 $\pmb { a }$ 只有短周期变化，外推20圈和200圈，相应的差别$\Delta a / a$ 均在 $1 0 ^ { - 1 2 } { - } 1 0 ^ { - 1 1 }$ 的范围内.

# \$8.6潮汐摄动

在日、月引力影响下,地球的弹性形变表现为固体潮、海潮和-大气潮，当然，大气潮的起因更主要的是热源．有些研究曾表明[7,8],海潮对卫星运动的影响比固体潮的影响要小5—10倍，而大气潮对卫星运动的影响比海潮影响还要小100倍。因此，在一般情况下，主要是考虑固体潮和海潮，但这两种潮汐对卫星轨道影响的规律很类似，往往难以分开，下面就固体潮对卫星轨道的影响-作一分析.

关于固体潮,古在由秀曾提出一种模型[9],相应的摄动函数为

$$
R = \frac { G M } { r } \Bigl ( \frac { m ^ { \prime } } { M } \Bigr ) \sum _ { n  2 } k _ { n } \Bigl ( \frac { a _ { e } } { r } \Bigr ) ^ { n } \Bigl ( \frac { a _ { e } } { r ^ { \prime } } \Bigr ) ^ { n + 1 } P _ { n } ( \cos \psi ^ { * } ) ,
$$

其中k,k,称为Love 数,常取k2=0.3,k=0.1，…，ψ\*是卫星方向与潮峰方向之间的地心张角。由于地球不是理想弹性体，故：潮汐形变有滞后现象，潮峰方向不是当时的日、月方向，而向东偏离了一个v角(即赤经变为α+,或经度变为+,α'和λ是日、月赤经和经度)．早期用测地卫星GEOS-1和GEOS-2测定地球模型时,未将几种潮汐分开,测得k2的有效值接近0.3[10],[11]．。因此,在精度要求不太高的情况下,只要对Love数kn和滞后角v作适当的修正，即可用上述模型同时研究固体潮和海潮对卫星轨道的影响．随着卫星测量精度愈来愈高，要求潮汐模型进一步精化，目前大多以Wahr模型为基础[121．该模型是用地球引力场位函数展开式系数的变化来表达的，例如固体潮中系数改正的主要部分为

$$
\begin{array} { l } { { \displaystyle \Delta C _ { \xi , 0 } = k _ { 2 } \sum _ { i = 1 } ^ { \frac { 5 } { 2 } } \biggl ( \frac { m _ { i } ^ { \prime } } { M ^ { \prime } } \biggr ) \biggl ( \frac { \hat { a } _ { \phi } } { m _ { j } ^ { \prime } } \biggr ) ^ { 3 } P _ { z } ( { \sin \varphi _ { j } ^ { \prime } } ) - \langle \Delta C _ { 3 2 } \rangle , } } \\ { { \displaystyle \Delta C _ { z , 0 } = \frac { 1 } { 3 } b _ { z } \sum _ { i = 1 } ^ { \frac { 5 } { 2 } } \biggl ( \frac { m _ { i } ^ { \prime } } { M } \biggr ) \biggl ( \frac { \hat { a } _ { \phi } } { m _ { j } ^ { \prime } } \biggr ) ^ { 3 } P _ { z } ^ { 1 } ( { \sin \varphi _ { j } ^ { \prime } } ) \cos ( \hat { x } _ { j } ^ { \prime } + \nu ) , } } \\ { { \displaystyle \Delta S _ { 3 3 } = \frac { 1 } { 3 } b _ { z } \sum _ { i = 1 } ^ { \frac { 5 } { 2 } } \biggl ( \frac { m _ { i } ^ { \prime } } { M ^ { \prime } } \biggr ) \biggl ( \frac { \hat { a } _ { \phi } } { m _ { j } ^ { \prime } } \biggr ) ^ { 3 } P _ { z } ^ { 1 } ( { \sin \varphi _ { i } ^ { \prime } } ) \sin ( \hat { x } _ { j } ^ { \prime } + \nu ) , } } \\ { { \displaystyle \Delta C _ { \nu ; 0 } = \frac { 1 } { 1 2 } b _ { z } \sum _ { i = 1 } ^ { \frac { 5 } { 2 } } \biggl ( \frac { m _ { i } ^ { \prime } } { M ^ { \prime } } \biggr ) \biggl ( \frac { \hat { a } _ { \phi } } { \nu _ { j } ^ { \prime } } \biggr ) ^ { 3 } P _ { z } ^ { 2 } ( { \sin \varphi _ { i } ^ { \prime } } ) \cos ( \hat { x } _ { j } ^ { \prime } + \nu ) , } } \\   \displaystyle \Delta S _ { 3 3 } = \frac { 1 } { 1 2 } b _ { z } \sum _ { i = 1 } ^ { \frac { 5 } { 2 } } \biggl ( \frac { m _ { i } ^ { \prime } } { M ^ { \prime } } \biggr ) \biggl ( \frac { m _ { i } } { \nu _ { j } ^ { \prime } } \biggr ) ^ { 3 } P _ { z } ^ { 3 } ( { \sin \varphi _ { i } ^ { \prime } } ) \sin (  \end{array}
$$

其中 $\pmb { C } _ { 2 , 0 } , \pmb { C } _ { 2 , 1 } , \pmb { S } _ { 2 , 1 } , \pmb { C } _ { 2 , 2 }$ 和 $\pmb { S _ { 2 , 2 } }$ 即第五章中所引用的符号 $C _ { 2 3 } A _ { \mathrm { 2 } 9 1 9 }$ $B _ { 2 9 1 9 } \ A _ { 2 9 2 }$ 和 $B _ { 2 } , { \bf { 2 } } , { \bf { \mathcal { M } } }$ 和 $a _ { e }$ 是地球质量和赤道平均半径，求和 $( j = 1 ,$ 2)表示日、月两个部分，下面仍改用一项(去掉求和号)表示日、月两个部分。 $\langle \Delta \mathcal { C } _ { 2 } , _ { 0 } \rangle$ 是 $C _ { 2 }$ 的零频率项(即永久潮汐项),其值为

$$
\langle \Delta C _ { 2 , 0 } \rangle = 3 . 1 1 0 \times 1 0 ^ { - 8 } \cdot k _ { 2 } .
$$

该项是常数，显然要反映在 $C _ { 2 }$ 中，因此，应从 $\Delta C _ { 2 9 0 }$ 中消除掉，即(8.72)式．其实，除 $\langle \Delta C _ { 2 , 0 } \rangle$ 外，这些系数改正对应的潮汐附加摄动位就是模型(8.71)式的 ${ \pmb k } _ { 2 }$ 部分．（8.72)式对应的附加位是

$$
\Delta V = { \frac { G M } { r } } \left( { \frac { a _ { e } } { r } } \right) ^ { 2 } \left\{ k _ { 2 } \left( { \frac { m ^ { \prime } } { M } } \right) \left( { \frac { a _ { e } } { r ^ { i } } } \right) ^ { 3 } \right\} P _ { 2 } \left( \sin \varphi ^ { \prime } \right) P _ { 2 } \left( \sin \varphi \right)
$$

$$
\begin{array} { l } { { \displaystyle \left. + \frac { 1 } { 3 } P _ { 2 } ^ { 1 } ( \sin \varphi ^ { \prime } ) \cos \lambda ^ { * } P _ { 1 } ^ { 2 } ( \sin \varphi ) \cos \lambda \right. } } \\ { { \displaystyle + \frac { 1 } { 3 } P _ { 2 } ^ { 1 } ( \sin \varphi ^ { \prime } ) \sin \lambda ^ { * } P _ { 2 } ^ { 1 } ( \sin \varphi ) \sin \lambda } } \\ { { \displaystyle + \frac { 1 } { 1 2 } P _ { 2 } ^ { 2 } ( \sin \varphi ^ { \prime } ) \cos 2 \lambda ^ { * } P _ { 2 } ^ { 2 } ( \sin \varphi ) \cos 2 \lambda } } \\ { { \displaystyle \left. + \frac { 1 } { 1 2 } P _ { 2 } ^ { 2 } ( \sin \varphi ^ { \prime } ) \sin 2 \lambda ^ { * } P _ { 2 } ^ { 2 } ( \sin \varphi ) \sin 2 \lambda \right] \Bigg \} , } } \end{array}
$$

其中λ\*=λ+v.若将(8.71)式中的k部分改写成下列形式：

$$
R = \frac { G M } { r } \bigg ( \frac { a _ { e } } { r } \bigg ) ^ { 2 } \bigg [ k _ { 2 } \bigg ( \frac { m ^ { \prime } } { M } \bigg ) \bigg ( \frac { a _ { e } } { r ^ { \prime } } \bigg ) ^ { 3 } P _ { 2 } \left( \cos \psi ^ { * } \right) \bigg ] ,
$$

很容易证明该表达式就是(8.74)式．为此，需改变P(cos\*)的表达形式,有

$$
\begin{array} { c } { { \cos \psi ^ { * } = \sin \varphi ^ { \prime } \sin \varphi + \cos \varphi ^ { \prime } \cos \varphi \cos \left( \lambda ^ { * } - \lambda \right) , } } \\ { { { } } } \\ { { { \displaystyle P _ { 2 } ( \cos \psi ^ { * } ) = \frac { 3 } { 2 } \cos ^ { 2 } \psi ^ { * } - \frac { 1 } { 2 } } } } \\ { { { } } } \\ { { = \frac { 3 } { 4 } \sin ^ { 2 } \varphi ^ { \prime } \sin ^ { 2 } \varphi - \frac { 3 } { 4 } \sin ^ { 2 } \varphi ^ { \prime } - \frac { 3 } { 4 } \sin ^ { 2 } \varphi + \frac { 1 } { 4 } } } \\ { { { } } } \\ { { { } \ + 3 \sin \varphi ^ { \prime } \cos \varphi ^ { \prime } \sin \varphi \cos \varphi \cos \left( \lambda ^ { * } - \lambda \right) } } \\ { { { } } } \\ { { { } + \frac { 3 } { 4 } \cos ^ { 2 } \varphi ^ { \prime } \cos ^ { 2 } \varphi \cos 2 ( \lambda ^ { * } - \lambda ) , } } \end{array}
$$

而

$$
\begin{array} { r l } & { P _ { 2 } \big ( \sin \varphi \big ) = \displaystyle \frac { 3 } { 2 } \sin ^ { 2 } \varphi - \frac { 1 } { 2 } , P _ { 2 } ^ { 1 } \big ( \sin \varphi \big ) = 3 \sin \varphi \cos \varphi , } \\ & { P _ { 2 } ^ { 2 } \big ( \sin \varphi \big ) = 3 \cos ^ { 2 } \varphi , } \end{array}
$$

因此，

$$
\begin{array} { l } { { P _ { 2 } ( \cos \psi ^ { * } ) = P _ { 2 } ( \sin \varphi ^ { \prime } ) P _ { 2 } ( \sin \varphi ) } } \\ { { \ \qquad + \frac { 1 } { 3 } P _ { 2 } ^ { 1 } ( \sin \varphi ^ { \prime } ) P _ { 2 } ^ { 1 } ( \sin \varphi ) \ ( \cos \lambda ^ { * } \cos \lambda } } \\ { { \ \qquad + \sin \lambda ^ { * } \sin \lambda ) \qquad } } \\ { { \ \qquad + \frac { 1 } { 1 2 } P _ { 2 } ^ { 2 } ( \sin \varphi ^ { \prime } ) P _ { 2 } ^ { 2 } ( \sin \varphi ) \ ( \cos 2 \lambda ^ { * } \cos 2 \lambda } } \\ { { \ \qquad + \sin 2 \lambda ^ { * } \sin 2 \lambda ) . } } \end{array}
$$

将该式代人(8.75)式即得(8.74)式.

(8.71)式表明，潮汐摄动与日月引力摄动大小之比为kz/r，由此不难看出,对近地卫星，两种摄动效应相差不大,约为一个量级,而对远地卫星(如24地球同步卫星)，则前者与后者之比却为

$1 0 ^ { - 5 }$ ，这种差别是不难理解的，由于(8.74)式中的田谐项改正部分仅涉及 $\lambda ^ { * }$ 与 $\lambda$ 之差，故 $\lambda ^ { \prime }$ 和 $\lambda$ 的起量点就可以取历元平春分点方向．因此，这些改正部分与地球形状摄动中的田谐项不同，不会出现地球自转项，对卫星轨道的影响将有依赖于 $\pmb { \omega }$ 和 $\varOmega$ 的长周期项，这说明 $\Delta C _ { 2 3 1 9 } \Delta  { S _ { 2 3 1 9 } }$ …等项与 $\Delta C _ { 2 9 0 }$ 项同等重要，下面仅讨论$\Delta C _ { 2 5 0 }$ 项的摄动效应，为了方便，仍采用标准计算单位 $( \vec { G } M \simeq 1$ ，$\pmb { a } _ { e } = \pmb { 1 } , \pmb { m } ^ { \prime }$ 表示 $m ^ { \prime } / M )$ ，有

$$
\Delta R { = } \beta k _ { 2 } \Big ( \frac { 1 } { r } \Big ) ^ { 3 } P _ { \circ } ( \sin \varphi ^ { \prime } ) P _ { \circ } ( \sin \varphi ) ,
$$

$$
\sin \varphi ^ { \prime } = \sin i ^ { \prime } \sin u ^ { \prime } , \sin \varphi = \sin i \sin u ,
$$

其中 $\beta = m ^ { \prime } / r ^ { \prime } { } ^ { 3 } , i ^ { \prime }$ 和 ${ \boldsymbol { u } } ^ { \prime }$ 在 $\ S 8 . 2$ 中出现过，将(8.78)式代入 $\Delta R _ { \star }$ 经整理后得

$$
\begin{array} { r l } & { \Delta R { * } \simeq \frac { \beta R _ { 2 } } { 4 a ^ { 3 } } \bigg ( \frac { a } { r } \bigg ) ^ { 3 } \bigg \{ \bigg ( 1 - \frac { 3 } { 2 } \sin ^ { 2 } i ^ { \prime } \bigg ) \bigg \rangle \bigg ( 1 - \frac { 3 } { 2 } \sin ^ { 2 } i \bigg ) } \\ & { \qquad + \frac { 3 } { 2 } \bigg ( 1 - \frac { 3 } { 2 } \sin ^ { 2 } i \bigg ) \sin ^ { 2 } i ^ { \prime } \cos 2 { \mathcal U } ^ { \prime } } \\ & { \qquad + \frac { 3 } { 2 } \bigg ( 1 - \frac { 3 } { 2 } \sin ^ { 2 } i ^ { \prime } \bigg ) \sin ^ { 2 } i \cos 2 { \mathcal U } } \\ & { \qquad - \frac { 9 } { 8 } \sin ^ { 2 } i ^ { \prime } \sin ^ { 2 } i \big [ \cos ( 2 u - 2 u ^ { \prime } ) + \cos ( 2 u + 2 u ^ { \prime } ) \big ] \bigg \} . } \end{array}
$$

消除快变量(即分离出短周期项)后得

$$
\begin{array} { r l r }   { \Delta \bar { R } = \frac { \beta k _ { 2 } } { 4 a ^ { 3 } } \Bigl ( 1 - \frac { 3 } { 2 } \sin ^ { 2 } i \Bigr ) ( 1 - e ^ { 2 } ) ^ { - 3 / 2 } \biggl [ \biggl ( 1 - \frac { 3 } { 2 } \sin ^ { 2 } i ^ { \prime } \biggr ) } \\ & { } & { \mathrm + \frac { 3 } { 2 } \sin ^ { 2 } i ^ { \prime } \cos 2 { \it u } ^ { \prime } \biggr ] . } \end{array}
$$

若取

$$
\beta { = } m ^ { \prime } / r _ { 0 } ^ { \prime 3 } , ~ u ^ { \prime } { = } \ L _ { l , l ^ { \prime } + ( \Omega _ { \partial } { - } \theta ) , } ^ { ( L , }
$$

则相应的潮汐摄动引起的卫星轨道根数变化的长期项(记为三阶 项 $\sigma _ { 3 } ( t - t _ { 0 } ) )$ 和长周期项(记为二阶项 $\pmb { \sigma } _ { \uparrow } ^ { ( 2 ) } ,$ 为

$$
\Omega _ { 3 } ( t - t _ { 0 } ) + [ \Omega _ { \iota } ^ { \scriptscriptstyle ( 2 ) } ( t ) - \Omega _ { \iota } ^ { \scriptscriptstyle ( 2 ) } ( t _ { 0 } ) ] = - \frac { 3 } { 4 p ^ { 2 } } \beta k _ { 2 } n \cos i W ( t ) ,
$$

$$
{ \omega } _ { 3 } ( t - t _ { 0 } ) + [ { \omega } _ { l } ^ { ( 2 ) } ( t ) - { \omega } _ { l } ^ { ( 2 ) } ( t _ { 0 } ) ] = \frac { 3 } { 4 p ^ { 2 } } \beta { k } _ { 2 } n \bigg ( 2 - \frac { 5 } { 2 } \sin ^ { 2 } i \bigg ) { W } ( t )
$$

$$
\boldsymbol { M } _ { 3 } ( t - t _ { 0 } ) + [ M _ { \iota } ^ { \scriptscriptstyle ( 2 ) } ( t ) - M _ { \iota } ^ { \scriptscriptstyle ( 2 ) } ( t _ { 0 } ) ]
$$

$$
= \frac { 3 } { 4 p ^ { 2 } } \beta k _ { 2 } n \biggl ( 1 - \frac { 3 } { 2 } \sin ^ { 2 } i \biggr ) \sqrt { 1 - e ^ { 2 } } W ( t ) , .
$$

$$
W ( t ) = \biggl ( 1 - \frac { 3 } { 2 } \sin ^ { 2 } i ^ { \prime } \biggr ) ( t - t _ { 0 } ) + \biggl ( \frac { 3 } { 2 } \sin ^ { 2 } i ^ { \prime } \biggr ) \frac { \sin 2 u ^ { \prime } - \sin 2 u _ { 0 } ^ { \prime } } { 2 n ^ { \prime } } ,
$$

其中 $\pmb { p } = \pmb { a } ( 1 - e ^ { 2 } )$ ，关于日、月的各种量 $L , L ^ { \prime } , \mathcal { Q } _ { \mathrm {  p } } { - } \theta _ { \mathrm { ; } }$ ，在 $\ S 8 . 1$ 和$\ S 8 . 2$ 中均出现过， $\pmb { n } ^ { \prime }$ 即 $L$ 和 $L ^ { \prime }$ 的变率．另三个根数 $a , e , \ i$ 只有短周期变化.

关于模型(8.71)式中的 ${ \pmb k } _ { 3 }$ 部分，亦可化成地球引力场系数的变化形式,其中

$$
\begin{array} { c } { { P _ { 3 } ( \cos \psi ) ^ { * } ) } } \\ { { = \displaystyle P _ { 3 } ( \sin \varphi ^ { \prime } ) P _ { 3 } ( \sin \varphi ) } } \\ { { = \displaystyle \int _ { - \frac { 1 } { 6 0 } P _ { 3 } ^ { 1 } ( \sin \varphi ^ { \prime } ) P _ { 3 } ^ { 1 } ( \sin \varphi ) \left[ \cos { \lambda ^ { * } } \cos { \lambda } + \sin { \lambda ^ { * } } \sin { \lambda } \right] } } } \\ { { + \displaystyle \frac { 1 } { 6 0 } P _ { 3 } ^ { 1 } ( \sin \varphi ^ { \prime } ) P _ { 3 } ^ { 2 } ( \sin \varphi ) \left[ \cos { 2 \lambda ^ { * } } \cos { 2 \lambda } + \sin { 2 \lambda ^ { * } } \sin { 2 \lambda } \right] } } \\ { { + \displaystyle \frac { 1 } { 6 0 } P _ { 3 } ^ { 2 } ( \sin \varphi ^ { \prime } ) P _ { 3 } ^ { 3 } ( \sin \varphi ) \left[ \cos { 3 \lambda ^ { * } } \cos { 3 \lambda } + \sin { 3 \lambda ^ { * } } \sin { 3 \lambda } \right] } } \\ { { + \displaystyle \frac { 1 } { 3 6 0 } P _ { 3 } ^ { 9 } ( \sin \varphi ^ { \prime } ) P _ { 3 } ^ { 8 } ( \sin \varphi ) \left[ \cos { 3 \lambda ^ { * } } \cos { 3 \lambda } + \sin { 3 \lambda ^ { * } } \sin { 3 \lambda } \right] . } } \end{array}
$$

相应的潮汐形变附加位就类似于(8.74)式.

上述模型是固体潮引起地球引力场系数变化的主要部分，这一部分取了与潮汐变化频率无关的Love数 ${ \pmb { k } } _ { n }$ ，Wahr模型对此作了进一步的修正[12],即系数 $\pmb { C } _ { 2 \bullet 1 } , \pmb { C } _ { 2 \bullet 2 } ,$ …变化的第二部分.

如果将海潮与固体潮严格分开，单独考虑它对卫星轨道的影响，同样可通过地球引力场系数的变化来讨论[12]，但涉及的数学模型比较复杂.至于大气潮，更是如此，这些都有待进一步探讨，如需了解其基本情况,可参阅文献[12]和[13].

# 参考文献

[1]狄晓华，天文学报,21(1980),287—292.  
[2] Meeus,J.,Tables of Moon and Sun (1962).  
[3]刘林，南京大学学报(自然科学版),1981,No.1,150-152.  
[4] Kozai,Y.,SAO Spec. Rep.,349(1973).  
[5]Estes,R.H.,Celest. Mech.,10(1974),253-276.  
[6]刘林,赵德滋，南京大学学报(自然科学版),1979,No.1,55-66.  
[7] Lambeck,K.,et al. Rev. of Geophys. and Space Phys.,12(1974)，421—434.  
[8]Gaposchkin,E.M.，SAO Spec. Rep.，313(1973)，89-191.  
[9]Kozai，Y.,Publ. Astron. Soc.Japan，17(1965)，395-402.  
[10]Douglas,B.C.,et al.，Celest. Mech.，10(1974)，165-178.  
[11] Lambeck,K.,Celest. Mecl.，10(1974)，179-182.  
[12] Melbourne，W.,et al.，MERIT STANDARDS,Third Draft,1983.  
[13] Lambeck,K.,et al.，Proceedings of International Sympo-sium on the Use of Artificial Satellite for Geodesy andGeo-dynamics, 1973,Athens,Greecc,353-393.

# 第九章 太阳光压摄动

当卫星离地面较近时，除地球形状摄动外，大气阻力的影响不可忽视，它是耗散力，将使卫星运动的能量减小(即半长径 $\pmb { a }$ 随时间单调地变小)，这将在下一章中讨论．而当卫星离地面不太近时，太阳辐射压(简称光压)的影响将会超过大气阻力，特别是对那些面质比较大的远地卫星，光压摄动很显著.1960年，人们发现卫星先锋1号（Vanguard-1)和回声1号(Echo-1）的运动规律出现异常现象：周期 $\pi$ 并不是随时间 $\pmb { \ell }$ 单调地减小（从半长径 $\pmb { a }$ 的变化规律得知)，偏心率 $e$ 的变化又出现周期长、变幅大的情况．由此，引起了人们对光压(包括对卫星的直接照射和地球的反照)摄动的研究 $[ 1 - - 1 1 ]$ ，近年来由于航天技术的高速发展，已有条件促使有关专家们考虑进一步利用光压作为星际航行的动力．为纪念克里斯托夫·哥伦布(C.Columbus）发现美洲大陆500周年，在美国成立的纪念委员会，于1988年12月10日一致批准“哥伦布500周年太空帆船杯赛”，就是规定利用太阳光压作为动力，将飞船（太空帆)从地球附近推向月球和火星.这从轨道力学的角度来看是完全可行的，一个 $( 2 5 0 \times 2 5 0 ) \mathrm { m } ^ { 2 }$ 的太空帆（总重量为 $5 0 0 ~ \ k g )$ ，以光压作为推力,从地球同步轨道上起航,在地球(非球形)和日，月引力以及光压作用下，约50天即可到达月球．若改用 $( 1 0 0 \times 1 0 0 ) \mathrm { m } ^ { 2 }$ 的太空帆，航行时间较长些，约300天.

这一章将仔细讨论光压对人造地球卫星轨道的摄动影响.

# $\ S \ 9 . 1$ 光压摄动的数学模型

如果是球形卫星，那么，作用在该卫星上的太阳直接照射的光压力(指合力，是一矢量) $\pmb { F } _ { \odot }$ 可由下式表达：

$$
F _ { \odot } { = } F _ { \odot } \Big ( \frac { \Delta } { \Delta } \Big ) ,
$$

$$
\begin{array} { r } { F _ { \odot } = \kappa S \bigg ( \rho _ { \odot } \frac { \Delta _ { 0 } ^ { 2 } } { \Delta ^ { 2 } } \bigg ) . } \end{array}
$$

其中 $\pmb { \triangle }$ 的意义见图 ${ \mathfrak { s } } . { \mathfrak { l } } { \mathfrak { s } } ~ { \mathfrak { s } }$ 是有效截面积，对于球形卫星，即垂直于太阳光线的卫星截面积; $\rho _ { \odot }$ 是距离 $\Delta _ { y }$ 处的光压强度(常称为光压常数)，地球表面附近的值为 $4 . 5 6 0 5 \times 1 0 ^ { - 6 } \mathrm { N } { \cdot } \mathrm { m } ^ { - 2 }$ ；系数 $\kappa = 1 +$ $\pmb { k } , 0 { \leqslant } k { \leqslant } 1 , k$ 值与卫星表面材料的反射性能有关， $\pmb { k } = 0$ 对应于全吸收， $\pmb { k } = \pmb { 1 }$ 对应于镜反射.

在上述假定下，光压力为一有心力，力心即太阳，但方向是朝向受力体(卫星)而不是力心，这与引力相反，既然是有心力，当然存在势，若记

![](images/0e1d91e38cb3b56c7a6a03f179ea1d3a89061416e6eff58ff0ee61414a5799f4.jpg)  
图9.1 $o$ 是地心， $S ^ { \prime }$ 是太阳， $\pmb { S } _ { \star }$ 是卫星

$$
C = \kappa S ( \rho _ { \odot } \Delta _ { 0 } ^ { 2 } ) ,
$$

则力 $\pmb { F }$ 又可写成

$$
\pmb { F } _ { \odot } = \frac { C } { \Delta ^ { 2 } } \big ( \frac { \Delta } { \Delta } \big ) .
$$

这与引力表达式类似，相应地有

$$
\left. \begin{array} { c l c r } { { F _ { \odot } = m { \bf g } \mathrm { r a d } R , } } \\ { { R = - \displaystyle \frac { C / m } { \Delta } = - \displaystyle \frac { C / m } { | r - r ^ { \prime } | } , } } \end{array} \right\}
$$

$\pmb { R }$ 即光压摄动函数.

实际上，大多数卫星并非球形，所以,作用在卫星上的光压力方向并不是 $( \Delta / \Delta )$ ,它将与卫星的形状、姿态以及 $\pmb { k }$ 值有关．根据卫星接受光照时的入射光和反射光的方向（包括卫星形状和姿态两个因素)以及反映该卫星表面吸收和反射性能的系数 $\pmb { k }$ 值，就可算出光压力的大小和方向，(9.1)和(9.2)式中的 $\kappa \mathcal { S } ( \Delta / \Delta )$ 将以 $\pmb { k }$ 和上述有关因素的某一函数所代替．因此，对于需要精确计算光压摄动的问题，必须严格考虑上述光压力的数学模型.

光压摄动还有一个特点，即地影问题，对卫星而言，常发生“日蚀”现象，阳光被地球挡住．因此光压力 ${ \pmb F } _ { \odot }$ 还得加上一个地影因子 $_ { \pmb { \nu } }$ (或称蚀因子),其定义为

$$
\small { \gamma = 1 - \frac { \Delta S _ { \odot } } { S _ { \odot } } } ,
$$

其中 $\pmb { S } _ { \odot }$ 是太阳视面积， $\Delta \pmb { S } _ { \odot }$ 是太阳被蚀的视面积，有 $0 \leqslant \nu \leqslant 1 .$

通常就将太阳直接照射的这一辐射压摄动称为光压摄动，除此之外，还有地球反照辐射压摄动．它包含两部分，一部分是光学辐射，即地球反照率辐射，另一部分是地球吸收阳光后转化为热辐射(即红外辐射)，又称发射率辐射。

因卫星在地球附近运动， $\Delta \approx \Delta _ { 0 }$ ，于是光压摄动的大小可用下式估计，即

$$
\frac { F _ { \odot } } { F _ { 0 } } { = } \Big ( \frac { \kappa S } { m } \Big ) \rho _ { \odot } r ^ { 2 } ,
$$

$\pmb { F } _ { 0 }$ 即地球中心引力，对于一-般面质比为 $\frac { \delta } { m } = 1 0 ^ { \circ } .$ 的卫星(相当于直径为 $3 \ m _ { i }$ 重 $1 \uparrow$ 的球形卫星),若在近地飞行， ${ r } { \approx } 1 . 1 .$ 有

$$
\frac { { \pmb { F } } _ { \odot } } { { \pmb { F } } _ { 0 } } { \approx } 0 . 5 \times 1 0 ^ { - 8 } ,
$$

若是 $2 4 ^ { \tt h }$ 地球同步卫星，则 $r \approx 6 . 6$ ，有

$$
\frac { F _ { \odot } } { F _ { 0 } } { \approx } 2 . 0 \times 1 0 ^ { - 7 } .
$$

因此，,相对地球形状 $\pmb { J _ { 2 } }$ 项摄动而言，光压可看成二阶小量．考虑到卫星和太阳到地心的距离比 $r / \Delta \approx 1 0 ^ { - 4 }$ ，光压力 $\pmb { F } _ { \odot }$ 即可简化成下列形式：

$$
\left. \begin{array} { l } { F _ { \odot } = - \kappa S \rho _ { \odot } \hat { \mathcal { r } } _ { \odot } , } \\ { \hat { r } _ { \odot } = r ^ { \prime } / r ^ { \prime } , } \end{array} \right\}
$$

这就是人卫工作中常采用的一种简化的光压摄动力数学模型。至于精密定轨中所需要的数学模型，主要应进一步考虑前面提到的卫星形状、姿态、表面材料性能（即 $\pmb { k }$ 值)以及地影因子 $\pmb { \nu }$ ．下面几节将首先利用模型(9.10)式来讨论光压摄动的具体计算方法和这种摄动对卫星轨道影响的规律，

# $\ S \ 9 . 2$ 光压摄动的基本方程

仍以 $\hat { \boldsymbol r } , \hat { \boldsymbol \theta } , \hat { \mathbf { R } }$ 分别表示卫星轨道径向、横向和轨道面法向的三个单位矢量，则相应的光压加速度的三个分量为

$$
\boldsymbol { \mathcal { S } } = \frac { 1 } { m } ( \boldsymbol { F } _ { \odot } { \boldsymbol { \hat { r } } } ) , \boldsymbol { \mathcal { T } } = \frac { 1 } { m } ( \boldsymbol { F } _ { \odot } { \boldsymbol { \hat { \theta } } } ) , \boldsymbol { W } = \frac { 1 } { m } ( \boldsymbol { F } _ { \odot } { \boldsymbol { \hat { R } } } ) .
$$

以(9.10)式中的 $\pmb { F } _ { \odot }$ 代入，并记

$$
k _ { 0 } = \frac { F _ { \odot } } { m } = \Big ( \frac { \kappa S } { m } \Big ) \rho _ { \odot } ,
$$

上式即可写成

$$
\begin{array} { r } { \dot { S } = - k _ { 0 } \left( \hat { r } _ { \odot } \cdot \hat { r } \right) , T = - k _ { 0 } \left( \hat { r } _ { \odot } \cdot \hat { \pmb { \theta } } \right) , W = - k _ { 0 } \left( \hat { r } _ { \odot } \cdot \hat { \pmb { R } } \right) , } \end{array}
$$

其中 $( \pmb { \hat { r } } _ { \odot } \pmb { \cdot } \pmb { \hat { r } } )$ 正是上一章(8.20)式所表达的cos $\pmb { \psi }$ ，这里，太阳方向单位矢量 $\hat { r } _ { \odot }$ 在地心赤道坐标系中的三个分量可写成

$$
\cos L , \sin L \cos \varepsilon \ , \sin L \sin \varepsilon \ ,
$$

$\pmb { L }$ 和 $\pmb { \varepsilon }$ 即太阳平黄经和黄赤交角．引用第四章的(4.69)一(4.72)式,即可算出光压加速度的三个分量 $\pmb { \mathcal { S } } _ { \pmb { \mathscr { S } } } \pmb { \mathcal { T } } _ { \pmb { \mathscr { S } } } \pmb { W }$ ，其形式如下：

$$
\left. \begin{array} { r l } & { S = - k _ { 0 } ( A \cos f + B \sin f ) , } \\ & { T = - k _ { 0 } ( - A \sin f + B \cos f ) , } \\ & { W = - k _ { 0 } C , } \end{array} \right\}
$$

其中

$$
\begin{array} { r l } { A - \frac { 1 } { 4 } \{ ( \Omega - \cos \theta ) ( \Gamma ( 1 - \cos \theta ) \cos ( \theta + \mathcal { G } + \mathcal { L } ) ) } \\ { + ( \Gamma - \cos \theta ) \cos ( \phi ) - ( \Gamma - \mathcal { L } ) \} } \\ { + ( \Gamma - \cos \theta ) \cos ( \phi - \mathcal { L } ) } \\ { + ( 1 - \cos \theta ) \cos ( \phi - \mathcal { L } ) } \\ { + ( \Gamma + \cos \theta ) \cos ( \phi - \mathcal { L } ) \cos ( \theta - \mathcal { L } - \mathcal { L } ) } \\ { - \frac { 1 } { 4 } \mathrm { d i s i n } \mathrm { d i s n o t } \mathrm { L i m } \epsilon \mathrm { d i m } \epsilon \mathrm { d i m } \epsilon \mathrm { d } \epsilon \mathrm { d } \epsilon } \\  B = - \frac { 1 } { 4 } \{ ( \Omega + \cos \theta ) \mathrm { d i s n o t } \mathrm { L } ( 1 - \cos \theta ) \sin ( \phi - \mathcal { L } ) \mathrm { d } \epsilon \mathrm { d } \epsilon \mathrm { d } \epsilon \} \\ { + ( \Omega - \cos \theta ) \sin ( \phi + \mathcal { L } - \mathcal { L } ) \} } \\ { \times \{ ( 1 - \cos \phi ) \mathrm { d i s n o t } \mathrm { L e m } \epsilon \mathrm { d i m } \epsilon \mathrm { ~ } \Omega - \mathcal { L } - \mathcal { L } \} } \\ { - ( 1 + \cos \theta ) \cos ( \phi - \mathcal { D } - \mathcal { L } ) \mathrm { d } \epsilon } \\ { - \frac { 1 } { 4 } \mathrm { d i s i n } \{ \cos \theta \mathrm { d i s n o t } \mathrm { L i m } \epsilon \mathrm { d i m } \epsilon \} } \\ { \epsilon = \mathrm { i s t ~ } \{ \cos \theta \mathrm { d i s n o t } \mathrm { L e m } \epsilon \mathrm { d i n } \epsilon \mathrm { d i m } \epsilon \mathrm { d } \epsilon \mathrm { d } \epsilon \mathrm { d } \epsilon \mathrm { d } \epsilon \mathrm { d } \epsilon \mathrm { ~ } } \\ { \epsilon \mathrm { d i s n o t } \mathrm { L e m } \epsilon \mathrm { d i m } \epsilon \mathrm { ~ } } \end{array}
$$

将 $s , \tau , w$ 三个分量代入第四章导出的摄动运动方程(4.80)即可得计算光压摄动的基本方程。但考虑到仍用平均根数法（或一般变换方法)来构造光压摄动解，在消除短周期部分时，需要对右函数求平均值，由于地影的存在(后面要详细讨论)，,方程还是化成对偏近点角 $\pmb { \mathcal { B } }$ 的形式比较简单，这一转化主要是为了求平均值，在

$$
\frac { d \sigma } { d t } = \frac { d \sigma } { d E } \ \frac { d E } { d t }
$$

的变换中， $d E / d t$ 可引用二体问题的表达式(2.37)．由此给出：

$$
\frac { d a } { d E } = 2 k _ { 0 } a ^ { 3 } ( A \sin E - B \sqrt { 1 - e ^ { 2 } } \cos E ) ,
$$

$$
\frac { \bar { d } e } { d E } = \frac { 1 } { 2 } k _ { 0 } a ^ { 2 } \sqrt { 1 - e ^ { 2 } } [ A \sqrt { 1 - e ^ { 2 } } \sin 2 E
$$

$$
- B ( 3 - 4 e \cos E + \cos 2 E ) ] ,
$$

$$
\frac { d i } { d E } = \frac { 1 } { 4 } k _ { 0 } a ^ { 2 } \frac { C } { \sqrt { 1 - e ^ { 2 } } } \{ [ 6 e - 4 ( 1 + e ^ { 2 } ) \cos { E }
$$

$$
\begin{array} { r l } & { \frac { d \mathcal { D } } { d \mathcal { E } } = \frac { 1 } { 4 } \frac { k _ { \mathrm { B } } a ^ { 2 } } { k _ { \mathrm { B } } ^ { 2 } } \frac { C } { \sqrt { 1 - \varepsilon ^ { 2 } } \sin \delta } \langle \sqrt { 1 - e ^ { 2 } } [ - 4 \sin B \cdot } \\ & { \quad + 2 e \sin 2 B ] \cos \theta + \mathcal { O } \theta - 4 ( 1 + e ^ { 3 } ) \cos B \cdot } \\ & { \quad + 2 e \cos 2 B \gamma \sin \partial \rangle , } \\ & { \frac { d \mathcal { D } } { d \mathcal { E } } = - \cos \phi \frac { d \mathcal { D } } { d \mathcal { E } } + \frac { 1 } { 2 } \varepsilon _ { B } a ^ { 3 } \frac { 1 } { k _ { \mathrm { B } } ^ { 2 } } \langle \sqrt { 1 - e ^ { 2 } } A ( 3 - 2 \cos \delta B \cos \mathcal { F } } \\ & { \quad - \cos 2 B ) \cdot \mathbb { E } \theta ( 2 \sin B \cos B - \sin 2 B ) \rangle , } \\ & { \frac { d \mathcal { M } } { d \mathcal { E } } = - \frac { 1 } { 4 } \frac { 1 } { 2 } k _ { \mathrm { B } } a ^ { 4 } \frac { 1 } { k _ { \mathrm { B } } ^ { 2 } } \frac { C } { \sin ( \lambda - 3 ( 1 + e ^ { 4 } ) ) - 2 e ( 3 + e ^ { 2 } ) \cos ( \mathcal { F } + \mathcal { S } ) \cos \mathcal { F } } } \\ & { \quad \quad + ( 1 - 3 e ^ { 3 } ) \cos 2 B \zeta \cos ( \mathcal { T } + ( 1 - 2 e ^ { 2 } ) \sin 2 B ) \sin 2 \mathcal { F } ] \cdot } \\ & { \quad + \sqrt { 1 - e ^ { 2 } } \mathcal { B } [ 2 \varepsilon \sin B \cos ( 1 + 2 e ^ { 2 } ) \sin 2 B ] \cdot } \end{array}
$$

# \$9.3 光压摄动解

因光压可看成二阶小量，上述摄动运动方程的原形式可写成

$$
\frac { d \sigma } { d t } { \doteq f _ { 2 } \left( \sigma , k _ { 0 } \right) } .
$$

对于一阶解，只需要 $\pmb { \hat { f } _ { 2 } }$ ，有

$$
\bar { f } _ { 2 } = \frac { 1 } { T } \int _ { 0 } ^ { \pi } \Bigl ( \frac { d \sigma } { d t } \Bigr ) d t = \frac { 1 } { T } \int _ { 0 } ^ { 2 \pi } \Bigl ( \frac { d \sigma } { d E } \Bigr ) d E
$$

$$
= = \frac { n } { 2 \pi } \int _ { . } ^ { 2 \pi } { \biggl ( } \frac { d \sigma } { d E } { \biggr ) } d E ,
$$

其中被积函数 $( d \sigma / d E )$ 由(9.17)式给出，由于地影的存在， $\hat { f } _ { 2 }$ 的计算公式将变为

$$
\vec { f } _ { 2 } = \frac { n } { 2 \pi } \int _ { \varepsilon _ { 0 } } ^ { \varepsilon _ { 1 } } \biggl ( \frac { d \sigma } { d E } \biggr ) d E .
$$

这里的积分上下限 $\scriptstyle { E _ { 0 } }$ 和 $\pmb { { \cal E } } _ { 1 }$ 分别为卫星出地影和进地影时对应的偏近点角．不过，地影又有本影与半影之分，在本影中地影因子${ \pmb \nu } = 0$ ，而在半影中却有 $0 { < } { \nu } { < } 1$ ，对于这一部分，光压仍起作用，积分(9.20)中应包含这一部分.关于此问题将要专门讨论(见9.5)，这里对 ${ \mathit { { E } } } _ { 0 }$ 和 $\mathbf { { \mathcal { E } } } _ { 1 }$ 暂作简单的理解。

将(9.17)式给出的右函数代人积分(9.20)得

$$
\begin{array} { r l r } {  { ( \vec { f } _ { 2 } ) _ { a } = - \Big ( \frac { k _ { 0 } } { 2 \pi } \Big ) 2 a ^ { 3 / 2 } \{ A ( \cos { E _ { 1 } } - \cos { E _ { 0 } } ) } } \\ & { } & \\ & { } & { + B \sqrt { 1 - e ^ { 2 } } ( \sin { E _ { 1 } } - \sin { E _ { 0 } } ) \} , } \end{array}
$$

$$
\begin{array} { r l r } { \langle \bar { f } _ { 2 } \rangle _ { \alpha } = - \left( \frac { k _ { \mathrm { e } } } { 2 \pi } \right) \frac { 1 } { 4 } \sqrt { a ( 1 - e ^ { 2 } ) } \left. \boldsymbol { 4 } \sqrt { 1 - e ^ { \bar { \iota } } } \left( \cos { 2 E _ { 1 } } - \cos { 2 E _ { 0 } } \right) \right. } & \\ & { } & { \left. + B [ \sin { E _ { 1 } } - \bar { E } _ { 0 } ] - 3 \theta \left( \sin { B _ { 1 } } - \sin { B _ { 0 } } \right) \right. } \\ & { } & { \left. + \left( \sin { 2 E _ { 1 } } - \sin { 2 E _ { 0 } } \right) ] \right. , } \\ { \langle \bar { f } _ { 2 } \rangle _ { \alpha } = \left( \frac { k _ { \mathrm { B } } } { 2 \pi } \right) \frac { \sqrt { a } } { 4 \sqrt { 1 - e ^ { 2 } } } G \left. \left[ \left\{ 6 e \left( E _ { 1 } - \bar { E } _ { 0 } \right) - \right. \right. \right. } \\ & { } & { \left. \left. \left. 4 \left( 1 + e ^ { 2 } \right) \left( \sin { E _ { 1 } } - \sin { E _ { 0 } } \right) + e \left( \sin { 2 E _ { 1 } } \right. \right. \right. \right. } \\ & { } & { \left. \left. \left. - \sin { 2 E _ { 0 } } \right) \right] \cos \theta \right. } \\ & { } & { \left. + \sqrt { 1 - e ^ { 2 } } \left[ - 4 \left( \cos { E _ { 1 } } - \cos { E _ { 0 } } \right) \right. \right. } \end{array}
$$

$$
( \bar { f } _ { 2 } ) _ { a } = \biggl ( \frac { k _ { 0 } } { 2 \pi } \biggr ) \frac { \sqrt { a } } { 4 \sqrt { 1 - e ^ { - 2 } \sin i } } C \sqrt { 1 - e ^ { 2 } } \sqrt { 4 ( \cos E _ { 1 } }
$$

$$
- \cos E _ { 0 } ) - e ( \cos 2 E _ { 1 } - \cos 2 E _ { 0 } ) ] \cos \omega
$$

$$
\begin{array} { r l r } & { } & { - [ { \bf B } ^ { c } ( \{ { { \bf A } _ { 1 } ^ { c } , { \bf B } _ { 2 } } \} ) - 4 ( 1 + e ^ { \mathrm { i } \theta _ { 1 } } ) ( \sin { \bf B } _ { 1 } \cos \psi _ { 1 } ) } \\ & { } & { + ( \sin ^ { 2 } \alpha ( { \bf B } _ { 2 } \cos 2 \psi _ { 2 } ) + \sin ^ { 2 } \alpha ) , \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad }  \\ & { } & { ( \vec { { \bf B } } _ { 2 } ) - \cos ( \alpha \sin \beta _ { 2 } ) \chi _ { 1 } ( \frac { \sin \theta } { \sin \theta } ) \chi _ { 2 } ^ { - \theta } ( \sin ^ { 2 } \alpha ( \theta - E _ { 2 } \sin ( E _ { 1 } - E _ { 2 } )     } \\ & { } & { -    \sin ( e ( \sin \theta E _ { 1 } ) E _ { 1 } ) - \sin ( \sin 2 E _ { 1 } \cos \psi _ { 1 } ) ) ) } \\ & { } & { (    \sin ^ { 2 } \alpha ( \alpha ( \sin 2 E _ { 2 } \cos 2 \psi _ { 2 } ) ) ) ] } \\ & { } &  (  \sin ^ { 2 } \alpha ( \alpha ( \sin 2 E _ { 2 } \cos 2 \psi _ { 2 } ) ) ) , \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \end{array}
$$

由于 $E _ { 0 } , E _ { 1 }$ 和系数 $A , B , C$ 的变化均取决于日、地、卫三者的相对位置，该变化显然是长周期的，故 $\pmb { \bar { f } _ { 2 } }$ 实为长周期项．如果要严格按长周期项积分，则相当麻烦，进行一些合理的简化并不影响我们了解光压摄动的规律，为此，仍按上一章对日月摄动的处理方法，作为二阶长期项，即

$$
\sigma _ { 2 } ( t - t _ { 0 } ) = ( \vec { f } _ { 2 } ) ( t - t _ { 0 } ) .
$$

上述(9.21)一(9.26)式给出的 $( 7 _ { 2 } ) _ { \sigma }$ 即系数 $a _ { 2 } , { \acute { e } } _ { 2 } , i _ { 2 } , \Omega _ { 2 } , \omega _ { 2 } , M _ { 2 } ,$ 而 $M _ { 2 }$ 右端的第二大项可写成下列形式：

$$
- \frac { 1 } { 2 } \Big ( \frac { 3 \pi } { 2 a } \Big ) \Delta { \ a } = - \frac { 1 } { 2 } \Big ( \frac { 3 \pi } { 2 a } \Big ) a _ { 2 } \big ( t - t _ { 0 } \big ) .
$$

$\left( \vec { f } _ { 2 } \right) _ { \sigma }$ 右端出现的根数均用 $( t - t _ { 0 } )$ 中间时刻对应的平均根数，类似于上一章的(8.55)式.

如果不存在地影，则 ${ \pmb { { \cal E } } } _ { 1 } = { \pmb { { \cal E } } } _ { 0 } + 2 \pi$ ，相应地有

$$
\left. \begin{array} { l } { a _ { z } = 0 , } \\ { \varepsilon _ { z } = - \frac { 3 } { 2 } k _ { 0 } \sqrt { \alpha } ( 1 - \overline { { e ^ { \varepsilon } } } ) B , } \\ { i _ { z } = \frac { 3 } { 2 } k _ { 0 } \sqrt { \frac { \alpha } { \sqrt { 1 - e ^ { \varepsilon _ { z } } } } } C , } \\ { \mathcal { D } _ { z } = \frac { 3 } { 2 } k _ { 0 } \sqrt { \frac { \alpha } { \sqrt { 1 - e ^ { \varepsilon _ { z } } } \sin \alpha } } C , } \\ { \omega _ { \ell } = - \cos i \mathcal { D } _ { 2 } + \frac { 3 } { 2 } k _ { 0 } \sqrt { \frac { \alpha ( 1 - e ^ { \varepsilon _ { z } } ) } { e } } A , } \\ { i _ { z } = - \frac { 3 } { 2 } k _ { 0 } \sqrt { \frac { \alpha } { \sqrt { 1 - e ^ { \varepsilon _ { z } } } } } A . } \end{array} \right\}
$$

由此可知，这一章开始提出的现象，不仅仅是简单的光压作用，而更重要的原因是由于地影的存在，它使得 $a$ 出现长周期变化，从而导致周期 $\pmb { T }$ 的非单调减小现象.另外， $e$ 出现周期长变幅大的原因可直接由上述摄动解得知.

# 9.4适用于任意偏心率的光压摄动计算公式

从上节结果可以看出小 $\pmb { e }$ 问题依然存在，与前面几章的处理方法一致，采用第六章\$6.4中给出的方法，相应的变量为

$$
a , i , \Omega , \xi = e \cos \omega , \eta = - e \sin \omega , \lambda = M + \omega .
$$

由原结果(9.21)一(9.26)式按变量的定义，经一定的组合即可给出相应的光压摄动计算公式，即

$$
a _ { 2 } = - \bigg ( \frac { k _ { 0 } } { 2 \pi } \bigg ) 2 a ^ { 3 / 2 } \left\{ A _ { 0 } \right[ ( \cos \tilde { u } _ { 1 } - \cos \tilde { u } _ { 0 } )
$$

$$
- \frac { \eta } { 1 + \sqrt { 1 - e ^ { 2 } } } ( \xi ( \sin \tilde { u } _ { 1 } - \sin \tilde { u } _ { 0 } ) + \eta ( \cos \tilde { u } _ { 1 } - \cos \tilde { u } _ { 0 } ) ) \ ]
$$

$$
\begin{array} { r l } & { + B _ { 0 } \tilde { \mathcal { L } } \left( \sin \tilde { u } _ { 1 } - \sin \tilde { u } _ { 0 } \right) } \\ & { - \frac { \xi } { 1 + \sqrt { 1 - e ^ { 2 } } } ( \xi ( \sin \tilde { u } _ { 1 } - \sin \tilde { u } _ { 0 } ) + \eta ( \cos \tilde { u } _ { 1 } - \cos \tilde { u } _ { 0 } ) ) ] \} , } \end{array}
$$

$$
\begin{array} { r l } & { \dot { u } _ { 2 } = \left( \frac { k _ { 0 } } { 2 \pi } \right) \underset { 4 \sqrt { 1 - e ^ { 2 } } } { \overset { \sqrt { a } } { \sum } } Q _ { 0 } \{ 6 \xi ( \tilde { u } _ { 1 } - \tilde { u } _ { 0 } ) } \\ & { \quad - 4 ( 1 + \xi ^ { 2 } ) \left( \sin \tilde { u } _ { 1 } - \sin \tilde { u } _ { 0 } \right) - 4 \xi \eta \left( \cos \tilde { u } _ { 1 } - \cos \tilde { u } _ { 0 } \right) } \\ & { \quad + \xi ( \sin 2 \tilde { u } _ { 1 } - \sin 2 \tilde { u } _ { 0 } ) + \eta \left( \cos 2 \tilde { u } _ { 1 } - \cos 2 \tilde { u } _ { 0 } \right) } \\ & { \quad + \frac { \eta } { 1 + \sqrt { 1 - e ^ { 2 } } } [ 4 \eta \left( \sin \tilde { u } _ { 1 } - \sin \tilde { u } _ { 0 } \right) } \\ & { \quad - 4 \xi \left( \cos \tilde { u } _ { 1 } - \cos \tilde { u } _ { 0 } \right) - 2 \xi \eta \left( \sin 2 \tilde { u } _ { 1 } - \sin 2 \tilde { u } _ { 0 } \right) } \\ & { \quad + \left( \xi ^ { 2 } - \eta ^ { 2 } \right) \left( \cos 2 \tilde { u } _ { 1 } - \cos 2 \tilde { u } _ { 0 } \right) ] \} , } \end{array}
$$

$$
\begin{array} { r l r }   { \mathcal { Q } _ { 2 } \simeq \biggl ( \frac { k _ { 0 } } { 2 \pi } \biggr ) \frac { \sqrt { a } } { 4 \sqrt { 1 - e ^ { 2 } } \sin i } C _ { 0 } \{ - 6 \eta ( \tilde { u } _ { 1 } - \tilde { u } _ { 0 } ) } \\ & { } & { + 4 ( 1 + \eta ^ { 2 } ) ( \cos \tilde { u } _ { 1 } - \cos \tilde { u } _ { 0 } ) + 4 \xi \eta \langle \sin \tilde { u } _ { 1 } - \sin \tilde { u } _ { 0 } \rangle } \\ & { } & { - \xi \bigl ( \cos 2 \tilde { u } _ { 1 } - \cos 2 \tilde { u } _ { 0 } \bigr ) + \eta \bigl ( \sin 2 \tilde { u } _ { 1 } - \sin 2 \tilde { u } _ { 0 } \bigr ) } \\ & { } & { + \frac { \xi } { 1 + \sqrt { 1 - e ^ { 2 } } } \bigl [ 4 \eta \bigl ( \sin \tilde { u } _ { 1 } - \sin \tilde { u } _ { 0 } \bigr ) } \\ & { } & { - 4 \xi \bigl ( \cos \tilde { u } _ { 1 } - \cos \tilde { u } _ { 0 } \bigr ) - 2 \xi \eta \bigl ( \sin 2 \tilde { u } _ { 1 } - \sin 2 \tilde { u } _ { 0 } \bigr ) } \\ & { } & { \pm ( \xi ^ { 2 } - \eta ^ { 2 } ) ( \cos 2 \tilde { u } _ { 1 } - \cos 2 \tilde { u } _ { 0 } \bigr ) \bigr ] \} , \qquad ( \xi \bigr ) } \end{array}
$$

$$
\begin{array} { r l } & { \quad : 1 _ { 1 } \gamma _ { - 1 } \sqrt { 1 - \phi ^ { 2 } } \mathrm { s i n } \mathrm { s u b } _ { 1 } \gamma - \mathrm { a r } \tilde { g } _ { 1 } ( \mathrm { s i n } \Omega _ { 1 } - \mathrm { s i n } \Omega _ { 0 } ) } \\ & { \qquad - 4 \mathcal { D } \tilde { \phi } ( \mathrm { s i n } \Omega _ { 1 } - \mathrm { o a d } \Omega _ { 1 } ) - 2 \mathcal { D } \tilde { \phi } \eta ( \mathrm { s i n } \Omega _ { 1 } - \mathrm { s i n } \Omega _ { 0 } ) } \\ & { \qquad + ( \hat { \phi } ^ { 2 } - n ) ^ { 4 } ( \mathrm { o a d } \Omega _ { 1 } \tilde { n } - \mathrm { o a d } \tilde { \Omega } _ { 1 } ^ { \ast } ) \tilde { \Omega } \eta , } \\ & { \hat { \phi } _ { z } = - ( \int _ { 2 \pi } ^ { \bar { \theta } } \sqrt { \frac { \gamma } { 4 } } \ 4 \mathcal { A } _ { z } \tilde { \phi } ( \hat { \mathrm { d } } - \tilde { b } ^ { 2 } ) \{ \epsilon \mathrm { o a d } \Omega _ { 1 } - \mathrm { e a d } \tilde { \Omega } _ { 0 }  } \\ & { \qquad - 4 \eta ( \mathrm { s i n } \tilde { n } _ { 2 } - \mathrm { o i d } \Omega _ { 0 } ) + \mathcal { D } \tilde { \Omega } \mathrm { t o } \mathrm { s i n } 2 \tilde { \Omega } _ { 1 } - \mathrm { s i n } 2 \tilde { \Omega } _ { 0 } ) } \\ & { \qquad + \frac { 4 \eta } { 1 + \sqrt { 1 - \phi ^ { 2 } } } \mathrm { s i n } \tilde { \Phi } ( \mathcal { G } ( \mathrm { s i n } \Delta _ { 1 } - \mathrm { s i n } \Omega _ { 1 } ) + \mathcal { D } ( \mathrm { c o s d } \tilde { \Omega } _ { 1 } - \mathrm { c o s d } \tilde { \Omega } _ { 0 } ) ) } \\ & { \qquad - \frac { \tilde { \phi } \tilde { \eta } } { \sqrt { 1 - \phi ^ { 2 } } } \mathrm { s i n } \frac { \tilde { \phi } } { \sqrt { 1 - \phi ^ { 2 } } } ( 2 \tilde { \xi } \eta ( \mathrm { s a d } \tilde { \Omega } _ { 1 } - \mathrm { c o s d } \tilde { \Omega } _ { 0 } ) } \\ &  \qquad - ( \tilde { \xi } - \eta ^ { 2 } ) \{ 2 \xi \eta ( \mathrm { s i n } 2 \tilde { \Omega } _ { 1 } - \mathrm \end{array}
$$

$$
\begin{array} { r l } & { \quad + \frac { \lambda } { 2 } ( \int _ { 1 } ^ { \infty } \frac { d z } { \sqrt { 2 } } - z \frac { z } { \sqrt { 2 } } ) + \mathcal { E } ( 4 \sin z \sin z - 4 \sin z ) } \\ & { \quad + \frac { \lambda } { 2 } ( \frac { \lambda } { 2 } - \sqrt { 2 } - 1 ) \mathcal { E } ( \cos z - 2 \sin z ) } \\ & { \quad - \frac { \lambda } { 2 } ( \frac { \lambda } { 2 } - \sqrt { 2 } ) ^ { 2 } ( 2 \sin ( \cos z - 2 \sin z ) ) } \\ & { \quad - \frac { \lambda } { 2 } ( \frac { \lambda } { 2 } - \sqrt { 2 } ) ^ { 2 } ( 2 \sin ( \cos z - 3 \cos z ) ) \sum _ { k = 0 } ^ { \infty } d z , \quad \Theta ( \theta ) } \\ & { \quad + \frac { \lambda } { 2 } ( \theta \sin z - 4 \sin z ) ( \sin z - 4 \sin z ) } \\ & { \quad \frac { \lambda } { 2 } ( \frac { \lambda } { 2 } - \sqrt { 2 } ) ^ { 2 } ( 4 \sin ( \sin z - 1 \sin z ) ) - \frac { \lambda } { 2 } \eta _ { k } ( \sin z - 4 \cos z ) } \\ & { \quad - ( \frac { \lambda } { 2 } - \frac { \lambda } { 2 } ) ( \sin ^ { 2 } z ) ( 2 \sin z - 4 \sin z ) - \bar { \lambda } \eta ( \cos z - 3 \cos z ) } \\ & { \quad - \frac { \lambda } { 2 } ( \frac { \lambda } { 2 } - \frac { \lambda } { 2 } ) ( 2 \sin z ) ( 2 \sin z - 4 \sin z ) } \\ & { \quad - \frac { \lambda } { 2 } ( \frac { \lambda } { 2 } - \frac { \lambda } { 2 } ) ^ { 2 } ( 2 \sin z \sin z - \sin z ) } \\ & { \quad + \frac { \lambda } { 2 } ( \frac { \lambda } { 2 } - \sqrt { 2 } - 1 ) ( 2 \sin z \sin z - 4 \sin z ) } \\ & { \quad + \frac { \lambda } { 2 } ( \sin z - 2 \sin z ) \sum _ { k = 0 } ^ { \infty } \frac { \lambda } { 2 } ( 2 \sin z \cos z - \sin z ) } \\ & { \quad + \frac { \lambda } { 2 } ( 2 \sin z - 3 \cos z ) } \\ &  \quad + \frac { \lambda } { 2 } ( 2 \sin z \ \end{array}
$$$$
\begin{array} { r l } & { = - \underbrace { \mathcal { U } _ { \mathrm { { J } } } ^ { \mathrm { { S } } } \left\{ \mathcal { A } ^ { \mathrm { { S } } } \left( \mathrm { e } ^ { \mathcal { R } } \right) - \mathrm { e } ^ { \mathcal { R } } \right\} } _ { \mathrm { { J } } } \times \mathrm { e } ^ { \mathcal { R } } \bigg \{ \mathcal { A } \bigg [ \mathrm { e } ^ { \mathcal { R } } \bigg ] - \mathrm { e } ^ { - \mathcal { R } } \bigg \{ \mathcal { A } \bigg [ \mathrm { e } ^ { \mathcal { R } } \bigg ] - \mathrm { e } ^ { - \mathcal { R } } \bigg \{ \mathcal { A } \bigg [ \mathrm { e } ^ { \mathcal { R } } \bigg ] - \mathrm { e } ^ { - \mathcal { R } } \bigg \{ \mathcal { A } \bigg \} [ \mathrm { e } ^ { \mathcal { R } } \bigg ] - \mathrm { e } ^ { - \mathcal { R } } \bigg \{ \mathcal { A } \bigg \} [ \mathrm { e } ^ { - \mathcal { R } } \bigg ] } { \mathcal { A } \bigg [ \mathrm { e } ^ { - \mathcal { R } } \bigg ] - \mathrm { e } ^ { - \mathcal { R } } \bigg \{ \mathcal { A } \bigg \} [ \mathrm { e } ^ { - \mathcal { R } } \bigg ] }  \\ &  - \bigg \{ \mathrm { e } ^ { - \mathcal { R } } \bigg \{ \frac { \mathcal { A } \bigg [ \mathrm { e } ^ { \mathcal { R } } } { \mathrm { { I } } - \mathrm { e } ^ { - \mathcal { R } } \bigg ] - \mathrm { e } ^ { - \mathcal { R } } \bigg \} - \bigg \} [ \mathrm { E } \bigg \{ \bigg \langle \mathrm { e } ^ { \mathcal { R } } \bigg \{ e ^ { - \mathcal { R } } - \mathrm { e } ^ { - \mathcal { R } } \bigg \} \lvert \mathrm { e } ^ { \mathcal { R } } \bigg \rvert - \mathrm { e } ^ { - \mathcal { R } } \bigg \{ \mathcal { A } \bigg \} [ \mathrm { e } ^ { - \mathcal { R } } \bigg ] } \\ &  - \eta \bigg \{ \mathrm { e } ^  - \Phi _ { \mathrm { { A } } } - \mathrm { e } ^  - \Phi _ { \mathrm { { A } } } - \mathrm { e } ^ { - \Phi _ { \mathrm { { A } } } - \mathrm { e } ^ { - \Phi _ { \mathrm { { A } } } - \mathrm { e } ^ { - \Phi _ { \mathrm { { A } } } - \mathrm { e } ^ { - \Phi _ { \mathrm { { A } } } } } } \bigg \} } \\ &  + \underbrace  \mathcal { F } \bigg \{ - \mathrm { e } ^  \end{array}
$$

$$
\begin{array} { r l } & { \quad + ( 2 \alpha ^ { 4 } - 2 \beta ^ { 2 } ) \zeta ( \omega + 2 \beta \beta ) , } \\ & { \quad + \frac { \zeta } { 1 + \sqrt { 3 } } \frac { \zeta } { \sqrt { 3 } } \zeta ( - \omega + 2 \beta ^ { 2 } ) \left( \delta - 4 \eta ^ { 2 } \right) ( \delta - 4 \eta ^ { 2 } ) } \\ & { \quad + \left( \zeta ^ { 4 } + 2 \eta ^ { 2 } \right) \left( \delta + 2 \eta ^ { 2 } \right) \zeta ( \omega + \kappa ( 2 \beta \omega ) ) ] } \\ & { \quad + \frac { \zeta } { 1 + \sqrt { 3 } } \frac { \beta \zeta } { \sqrt { 3 } } \eta \left( \eta ( 2 ) + \sqrt { 3 } - \varepsilon ^ { 2 } \right) \left( \delta - \frac { \zeta } { 1 + \sqrt { 3 } } \right) } \\ & { \quad - \zeta ( 2 \beta \omega ) + \sqrt { 3 } - \varepsilon ^ { 2 } \zeta ( \omega + \kappa ( 2 \beta \omega ) , \ \sin \alpha \beta ) } \\ & { \quad - 4 \zeta ( ( \beta + \kappa ( 1 - \beta \omega ^ { 2 } ) ) ( 2 1 \eta ^ { 3 } ) - \langle ( \zeta ^ { 2 } - \eta ^ { 2 } ) \rangle ) ( \delta \sin _ { \xi } - \varepsilon \omega \sin _ { \xi } \beta ) } \\ & { \quad + \frac { \zeta } { 1 + \sqrt { 3 } } \frac { \beta \zeta } { \sqrt { 3 } } \zeta ( - ( 1 + \sqrt { 3 } - \varepsilon ^ { 2 } ) ) \left( \delta - 4 \eta ^ { 2 } \right) } \\ & { \quad + \frac { \zeta } { 1 + \sqrt { 3 } } \frac { \zeta } { \sqrt { 3 } } \frac { \zeta } { \sqrt { 3 } } \left( - \frac { \zeta } { 1 + \sqrt { 3 } } - \varepsilon ^ { 2 } \right) ( \delta - 3 \eta ^ { 2 } ) } \\ & { \quad + \left( \delta ^ { 2 } - 2 \eta ^ { 2 } \right) \zeta ( \sin _ { \xi } \alpha + 3 \eta \cos _ { \xi } \beta ) } \\ & { \quad \gamma _ { 1 } \frac { \zeta } { \sqrt { 3 } } \frac { \zeta } { \sqrt { 3 } } \frac { \zeta } { \sqrt { 3 } } \exp ( ( - \beta \gamma - \varepsilon ^ { 2 } ) \zeta ( \eta \beta \omega ) ) } \\ & { \quad - ( 2 \beta \gamma ^ { 2 } ) \left( \delta + 2 \eta ^ { 2 } \right) ( \delta + 2 \eta ^ { 2 } \sin _ { \xi } \alpha + \beta \eta ^ { 2 } ) }  \end{array}
$$

其中 $\widetilde { \pmb { u } } = \pmb { E } _ { 1 } ^ { 1 } - \pmb { \omega } _ { }$ ，相应的 $\widetilde { \pmb { u } } _ { 0 }$ 和 $\widetilde { \pmb { u } } _ { 1 }$ 分别为 ${ \pmb { { \cal E } } } _ { 0 } + \omega$ 和 $\pmb { { \cal E } } _ { 1 } + \omega , A _ { 0 } , B _ { 0 }$ 与$A , B$ 的关系为

$$
A = \cos \omega A _ { 0 } + \sin \omega B _ { 0 } , B = - \sin \omega A _ { 0 } + \cos \omega B _ { 0 } ,
$$

$A _ { 0 } , B _ { 0 }$ 和 $C _ { 0 }$ 由下式表达：

$$
\left. \begin{array} { l } { { A _ { 0 } { = } A ( \omega { = } 0 ) } } \\ { { \quad { = } \cos { \mathcal { Q } } \cos { L } + \sin { \mathcal { Q } } \sin { L } \cos { \varepsilon } , } } \\ { { \quad B _ { \theta } { = } B ( \omega { = } 0 ) } } \\ { { \quad { = } - \cos { i } \left( \sin { \mathcal { Q } } \cos { L } - \cos { \mathcal { Q } } \sin { L } \cos { \varepsilon } \right) } } \\ { { \quad { \quad } + \sin { i } \left( \sin { L } \sin { \varepsilon } \right) , } } \\ { { \quad C _ { \theta } { = } C . } } \end{array} \right\}
$$

上述各式右端出现的(包括 $A _ { 0 } , B _ { 0 }$ 和计算 $\widetilde { \pmb { u } } _ { 0 } , ~ \widetilde { \pmb { u } } _ { 1 }$ 时要用到的）

根数均为平均根数，特别是 $\Omega , \xi , \eta$ 等量，应按上一章(8.63)式取值．剩下的问题是上一节的 $E _ { 0 }$ 和 $E _ { 1 }$ 以及这一节的 $\tilde { \boldsymbol { u } } _ { 0 }$ 和 $\widetilde { \pmb { u } } _ { 1 }$ 如何给出,这将涉及到下一节要讨论的地影模型.

# 9.5地影问题

太阳的角半径约为 $1 6 ^ { \prime }$ ，相应的视半径为 $1 0 9 a _ { e } ( a _ { e }$ 是地球赤道平均半径),地影显然呈锥形，且有本影与半影之分[11]．但是，由于太阳离地球很远，平均距离为 $\mathbf { 2 . 3 4 \times 1 0 ^ { 4 } } a _ { e }$ ，若把太阳光处理成从无穷远射来(即平行光)，形成“柱形”地影，在地球处两种地影的差别也只有 $0 ^ { \circ } . 2 7$ ，而且锥形地影的锥顶在地球背后(即背着太阳的方向)约 $\mathbf { 2 1 7 } a _ { e }$ 处,卫星却在地球附近飞行,因此，在计算光压摄动时，对于一阶解的精度要求，处理成柱形地影不成问题，即使在很多高精度问题中，亦同样可采用这一简单的地影模型。当然，对于具体问题要作具体分析，必须考虑卫星面质比的大小，距地球的远近以及计算弧段的长短等，从而确定是否需要采用锥形地影模型．除上述因素外，还有地球形状和大气衰减效应问题，考虑地球扁率后，地影不再是圆柱形，其差别约为 $\mathfrak { s } \times \mathfrak { 1 0 } ^ { - 3 }$ ，而大气衰减效应可以等效于地球半径增大 $2 0  { \mathrm { k m } } ^ { [ 1 1 1 }$ ，这与原地球半径之差别亦为 $3 \times 1 0 ^ { - 3 }$

如果采用圆柱形地影模型(就简称柱形地影)，则无本影与半影之分，相应的地影因子 $\pmb { \nu }$ 就取0 (地影内)和1(地影外)，在计算光压摄动时，无论是分析方法或是数值方法，都很简单．事实上，前 $\ S \ 9 . \ 3$ 和 $\ S \ 9 . \ 4$ 中就是在此地影模型下给出的解，这一节将用此模型给出卫星出、进地影对应的 ${ \pmb E } _ { 0 }$ 和 $\mathbf { { \mathcal { E } } } _ { 1 }$ 值（或 $\widetilde { \pmb { u } } _ { 0 }$ 和 $\widetilde { \pmb { u } } _ { 1 }$ 值)，此问题实为一求解地影方程问题.

根据上述假定，卫星出、进地影时应满足下列条件（见图 9. 2):

![](images/fd731e9bb55e676d7913a47debc5d39af6537fb3201eebfac4f02af9548fcac8.jpg)  
图9.2卫星的出、进地影平面图

$$
\left. \begin{array} { l } { \cos \psi = \hat { \pmb { r } } _ { \odot } \cdot \hat { \pmb { r } } , } \\ { \sin \psi = \displaystyle \frac { R } { r } , } \end{array} \right\}
$$

其中 $\pmb { R }$ 就用地球赤道平均半径 ${ \pmb { a } } _ { e }$ ，在人卫工作的常用计算单位中，$\pmb { R } = \pmb { a _ { e } = 1 } ,$ ，又根据(9.15)式，上述条件可改写成

$$
\left. \begin{array} { l } { \cos \psi = A \cos f + B \sin f , } \\ { \qquad \sin \psi \ { = } \frac { 1 } { r } , } \end{array} \right\}
$$

这就是地影方程，确切地说是柱形地影方程．由该方程可解出卫星出、进地影时的位置 $f _ { 0 }$ 和 $f _ { 1 }$ ，因方程中包含 $A , B$ 和 $\pmb { r }$ ，其解显然依赖于卫星轨道和太阳的位置，如果直接解方程(9.39)，那么必然涉及到sinf或cos $f$ 的四次代数方程，尽管可以解出，但比较麻烦，下面介绍一种比较简单的解法.

# 1.以 $\pmb { f }$ 或 $\pmb { \cal E }$ 表达的解

令

$$
K \sin \theta { = } A , K \cos \theta { = } B , K { > } 0 ,
$$

则方程(9.39)式变为

$$
\left. \begin{array} { l } { \cos \psi = K \sin { ( \theta + f ) } , \quad } \\ { \sin \psi = \displaystyle \frac { 1 } { p } ( 1 + e \cos f ) , } \end{array} \right\}
$$

其中 $\pmb { p = a ( 1 - e ^ { 2 } ) }$ ,于是有

$$
K ^ { 2 } \sin ^ { 2 } ( \theta + f ) = 1 - \frac { 1 } { p ^ { 2 } } ( 1 + e \cos f ) ^ { 2 } .
$$

这就是地影方程的另一种表达形式,其中 $\kappa$ 和 $\theta$ 由定义(9.40）式确定，即

$$
K ^ { 2 } = A ^ { 2 } + B ^ { 2 } , \theta = \operatorname { t g } ^ { - 1 } \left( A / B \right) .
$$

方程(9.42)可用迭代法求解，共迭代过程是：首先令 $e = 0$ ，由

$$
\sin \left( \theta + f \right) ^ { \left( 0 \right) } = - \frac { 1 } { K } \sqrt { 1 - \frac { 1 } { p ^ { 2 } } }
$$

解出 $f _ { 0 }$ 和 $f _ { 1 }$ 的初值 $f _ { 0 } ^ { ( 0 ) }$ 和 $f _ { \textbf { i } } ^ { ( 0 ) }$ ，然后再分别代入方程(9.42）的右端进行迭代，直到满足一定精度为止，即给出卫星出、进地影的位置 $f _ { 0 }$ 和 $f _ { 1 }$ .迭代过程中有三个问题：

(1）（9.44)式右端为什么取负号?这是由于 $K { > } 0$ ，而在地影中， $\psi { > } 1 8 0 ^ { \circ } , \thinspace \thinspace \thinspace \thinspace \mathrm { c o s } \psi { = } K \sin { ( \theta + f ) } < 0 ,$ 因此有 $\sin { ( \theta + f ) } < 0 ,$ 故取负号．正号是对应卫星轨道与地影圆柱的另两个交点，在太阳与地球之间．、

(2） $f _ { 0 } ^ { ( 0 ) }$ 和 $f _ { 1 } ^ { ( 0 ) }$ 以及整个迭代过程中 $f _ { 0 }$ 和 $f _ { 1 }$ 如何区分？sin $( \theta$ $+ \ldots 0$ 有两个解,一个在第三象限，另一个在第四象限，而根据地影的特点，要求 $\widehat { f _ { \vartheta } f _ { 1 } } > 1 8 0 ^ { \circ }$ ，因此 $( \theta + f _ { 0 } )$ 应在第四象限， $( \theta + f _ { 1 } )$ 应在第三象限， $f _ { 0 }$ 和 $f _ { 1 }$ 就这样确定.

（3）如果 $\mathfrak { s i n } \left( \theta + f \right) ^ { \left( 0 \right) } \geqslant 1$ 怎么办？这表示接近无地影或就是无地影 (无地影是指卫星不进入阴影区)的情况，此时可令 $( \theta +$ $f ) ^ { ( 0 ) } = 2 7 0 ^ { \circ }$ 代人方程(9.42）右端开始迭代．如果再出现 $\sin \left( \theta + \right.$ $f ) \geq 1$ 或迭代过程中出现这种情况，就认为不存在地影，相应地令$f _ { 0 } = 0 , f _ { 1 } = 2 \pi$ 即可．由于这种状态可能发生在卫星刚好穿过柱形地影的边缘,无地影解存在误差，但其量级较小，仅为 $O ( e ^ { 2 } )$ ，对光压摄动计算而言影响甚小，而且不易发生。

由解出的 $f _ { 0 }$ 和 $f _ { 1 }$ ，根据 $\pmb { \cal E }$ 和 $f$ 之间的关系：

$$
r \cos f = a ( \cos E - e ) , r \sin f - a { \sqrt { 1 - e ^ { 2 } } } \sin E , r = { \frac { a ( 1 - e ^ { 2 } ) } { 1 + e \cos f } }  f \quad
$$

就可给出计算 ${ \pmb E } _ { 0 }$ 和 $\pmb { { \cal E } } _ { 1 }$ 的公式，即

$$
\sin E = { \frac { \sqrt { 1 - e ^ { 2 } } } { 1 + e \cos f } } \sin f , \cos E = { \frac { 1 - e ^ { 2 } } { 1 + e \cos f } } \cos f + e .
$$

类似上面的做法，亦可直接给出解 $\pmb { { \cal E } } _ { 0 }$ 和 $\pmb { { \cal E } } _ { 1 }$ 的方程，但不如求解 $f _ { 0 }$ 和 $f _ { 1 }$ 方便.

# 2.以 $\pmb { \mathcal { U } }$ 或 $\widetilde { \pmb { u } }$ 表达的解

根据上节的结果,有

$$
\left. \begin{array} { r l } & { A = A _ { 0 } \cos \omega + B _ { 0 } \sin \omega , } \\ & { B = - A _ { 0 } \sin \omega + B _ { 0 } \cos \omega . } \end{array} \right\}
$$

$$
K \sin \theta = { A _ { 0 } , K \cos \theta } = { B _ { 0 } , K > 0 , }
$$

则方程(9.39)变为

$$
\left. \begin{array} { l } { \displaystyle \cos \psi = K \sin \left( \theta + u \right) , } \\ { \displaystyle \sin \psi = \frac { 1 } { p } ( 1 + \xi \cos u - \eta \sin u ) , } \end{array} \right\}
$$

其中 $\pmb { u } = \pmb { f } + \pmb { \omega } .$ 于是有

$$
K ^ { 2 } \sin ^ { 2 } ( \theta \div u ) = 1 - \frac { 1 } { p ^ { 2 } } ( 1 + \xi \cos u - \eta \sin u ) ^ { 2 } ,
$$

这又是地影方程的一种形式，其中 $\pmb { K }$ 和 $\pmb \theta$ 由定义（9.48）式确定，即

$$
K ^ { 2 } = A _ { 0 } ^ { 2 } + B _ { 0 } ^ { 2 } , \theta = { \tt t g } ^ { - 1 } ( A _ { 0 } / B _ { 0 } ) .
$$

解方程(9.50),给出卫星出进地影的位置 ${ \mathfrak { u } } _ { 0 }$ 和 ${ \pmb u } _ { 1 }$ 的步骤与前面给出 $\pmb { f _ { 0 } }$ 和 $f _ { 1 }$ 类似．首先令 ${ \pmb \xi } = { \pmb \eta } = 0$ （相当于 $e = 0 ,$ ，由

$$
\sin { ( \theta + u ) ^ { \left( 0 \right) } } = - \frac { 1 } { K } \sqrt { 1 - \frac { 1 } { p ^ { 2 } } }
$$

解出 ${ \pmb u } _ { 0 }$ 和 ${ \pmb u } _ { 1 }$ 的初值 ${ \pmb u } _ { 0 } ^ { ( 0 ) }$ 和 ${ \pmb u } _ { 1 } ^ { ( 0 ) }$ ，然后再分别代入方程(9.50)的右端进行迭代，最后给出所需要的 ${ \pmb u } _ { \pmb 0 }$ 和 ${ \pmb u } _ { 1 }$ ，而迭代过程中出现的各种情况及其处理方法与前面亦类似，不再重复。

根据(9.44)式，可得 $\tilde { { \pmb u } }$ 与 $\pmb { \mathscr { u } }$ 之间的关系如下：

$$
\left. \begin{array} { c } { { \cos \tilde { u } = \displaystyle \frac { \sqrt { 1 - e ^ { 2 } } } { 1 + \xi \cos u - \eta \sin u } \biggl [ \biggl ( 1 - \frac { \xi ^ { 2 } } { 1 + \sqrt { 1 - e ^ { 2 } } } \biggr ) } } \\ { { \cos u \div \frac { \xi \eta } { 1 + \sqrt { 1 - e ^ { 2 } } } \sin u \biggr ] \div \xi , } } \\ { { \sin \tilde { u } = \displaystyle \frac { \sqrt { 1 - e ^ { 2 } } } { 1 + \xi \cos u - \eta \sin u } \biggl [ \biggl ( 1 - \frac { \eta ^ { 2 } } { 1 + \sqrt { 1 - e ^ { 2 } } } \biggr ) } } \\ { { \cdot \ } } \\ { { \sin \tilde { u } = \displaystyle \frac { \xi \eta } { 1 + \frac { \xi \eta } { 1 + \sqrt { 1 - e ^ { 2 } } } \cos u } \biggl ] - \eta \sin \eta \biggr ] - \eta , } } \\ { { \sin \tilde { u } = \displaystyle \frac { \xi \eta } { 1 + \frac { \xi \eta } { 1 + \sqrt { 1 - e ^ { 2 } } } \cos u } \biggl ] - \eta , } } \end{array} \right\}
$$

由此，在给出 ${ \pmb u } _ { 0 }$ 和 ${ \pmb u } _ { 1 }$ 后即可算出前面所需要的 $\widetilde { \pmb { u } } _ { 0 }$ 和 $\widetilde { \pmb u } _ { 1 }$ ，同样可直接给出计算 ${ \widetilde { \pmb u } } _ { 0 }$ 和 $\widetilde { \pmb { u } } _ { 1 }$ 的地影方程，但也是不如求解 ${ \boldsymbol { \mathit { u } } } _ { 0 }$ 和 ${ \pmb u } _ { 1 }$ 方便.

# 3．卫星是否在地影中的判别方法

这是卫星位置预报中或用数值方法计算光压摄动时要考虑的问题．如果已经给出了地影方程的解 $( f _ { 0 }$ 和 $\scriptstyle f _ { 1 }$ 或 ${ \mathfrak { u } } _ { 0 }$ 和 ${ \pmb u } _ { 1 }$ )，那么只要根据卫星的位置 $f$ 或 $\pmb { u }$ ，判断条件

$$
f - f _ { 0 } > f _ { 1 } - f _ { 0 } \ 是 8 - u _ { 0 } > u _ { 1 } - u _ { 0 }
$$

是否满足．若满足，则卫星在地影内，否则在地影外．条件(9.54)式中的 $f { - } f _ { 0 } , f _ { 1 } { - } f _ { 0 } , u { - } u _ { 0 } , u _ { 1 } { - } u _ { 0 }$ 都要取正值，如果是负值，应加上 $\pmb { 2 \pi }$

在没有给出地影方程解的情况下，由图9.2可知，卫星在地影内所满足的条件是：

$$
\cos \psi = \hat { r } _ { \odot } \cdot \hat { r } < 0 , \mathrm { ~ } \sin \psi < \frac { 1 } { r } ,
$$

因 $\psi$ 总是在 $\left( { \frac { \pi } { 2 } } , \pi \right)$ 内，故si $\scriptstyle \mathtt { n } \psi = { \sqrt { 1 - \cos ^ { 2 } \psi } } .$

除地影问题外，还有月影问题，但人造卫星进入月影的“机会”要比进入地影的机会小得多．如果要考虑这一问题也不困难，和考虑地影方法类似，这里不再讨论.

# 9.6 地球反照辐射压摄动问题

$\ S 9 . 1$ 中已提到，地球反照辐射压摄动包括两个部分，即光学辐射(反照率辐射)和红外辐射(发射率辐射)，前者的辐射强度依赖于太阳的位置，而后者仅与发射点的状态有关．如果卫星是球形，则光学辐射对该卫星将产生径向和“横”向摄动加速度，当卫星处在光亮地球中心上空时，径向加速度达到最大，当卫星处在昼夜交界处时，横向加速度达到最大，而当卫星处于黑夜地球一面时，则光学辐射压摄动加速度为零．红外辐射对球形卫星主要产生径向摄动加速度．早期的研究工作主要局限于简单的模型[9，近年来由于对人卫定轨精度的要求提高，促使人们进一步讨论反照辐压的机制，并使其数学模型精化.

精化的主要问题是如何给出更合理的反照率(系数) $\scriptstyle { I _ { a } }$ 和发射率(系数) $I _ { e }$ ，由于受到地面、海面和空间云层等各种复杂物理因素的影响，无法给出 $\pmb { I _ { a } }$ 和 $I _ { e }$ 的精确分析表达式，只能根据大量的测量数据进行拟合，例如，根据Sehnal的工作 $[ \pmb { \vartheta } ] \cdot [ \mathbf { ! } \pmb { 0 } ]$ ，给出拟合式为

$$
I _ { a } = 0 . 3 4 + 0 . 1 \cos \left[ { \frac { 2 \pi } { 3 6 5 . 2 5 } } ( t - t _ { 0 } ) \right] \sin \varphi + 0 . 2 9 \left( { \frac { 3 } { 2 } } \sin ^ { 2 } \varphi - { \frac { 1 } { 2 } } \right)
$$

$$
I _ { e } = 0 . 6 8 \mathrm { - } 0 . 0 7 \mathrm { c o s } \left[ \frac { 2 \pi } { 3 6 5 . 2 5 } ( t - t _ { 0 } ) \right] \mathrm { s i n } \varphi \mathrm { - } 0 . 1 8 \bigg ( \frac { 3 } { 2 } \mathrm { s i n } ^ { 2 } \varphi \mathrm { - } \frac { 1 } { 2 } \bigg )
$$

其中 $\pmb { \varphi }$ 是地球表面辐射面积元的地心纬度， $( t - t _ { 0 } )$ 的单位是平太阳日， $\pmb { t _ { 0 } }$ 是历元.上述近似表达式反映了地球表面的区域性和季节变化.

有了反照率 $I _ { a }$ 和发射率 $I _ { e }$ 的分析表达式，即可按下面两个积分求出反照率辐射压和发射率辐射压的摄动加速度,分别用 $A _ { a }$ 和 $A _ { e }$ 表示，有

$$
\begin{array} { r l } & { \boldsymbol { A } _ { a } = \displaystyle \int _ { \omega } \int \Big ( \frac { \boldsymbol { s } } { m } \Big ) \Big ( \rho _ { \odot } \frac { \Delta _ { 0 } ^ { 2 } } { r _ { s } ^ { 2 } } \Big ) \Big ( \frac { 1 + k } { \cdot \pi } \Big ) \frac { I _ { a } y _ { s } \cos \theta _ { s } \cos \alpha } { \rho ^ { 2 } } \Big ( \frac { \rho } { \rho } \Big ) d \sigma \ , } \\ & { \boldsymbol { A } _ { e } = \displaystyle \int _ { \omega } \Big [ \Big ( \frac { \boldsymbol { s } } { m } \Big ) \Big ( \rho _ { \odot } \frac { \Delta _ { 0 } ^ { 2 } } { r _ { s } ^ { 2 } } \Big ) \Big ( \frac { 1 + k } { 4 \pi } \Big ) \frac { I _ { e } \cos \alpha } { \rho ^ { 2 } } \Big ( \frac { \rho } { \rho } \Big ) d \sigma , } \end{array}
$$

$$
 \begin{array} { r }  \ _ { y _ { s } } = \{ \begin{array} { l l } { 1 , \ \cos { \theta _ { s } } > 0 , } \\ { 0 , \ \cos { \theta _ { s } } \leqslant 0 . } \end{array}  \end{array}
$$

其中 $\pmb { r _ { s } }$ 是日心的地心距， $\theta _ { s }$ 是面积元 ${ \pmb d \sigma }$ 的法向与太阳的地心位置矢量方向的夹角， $\pmb { \alpha }$ 是面积元 $d \sigma$ 的法向与卫星的地心位置矢量方向的夹角， $\rho$ 是面积元 ${ \pmb d } \sigma$ 到卫星的矢量，其它各量在 $\ S 9 . 1$ 中都出现过。 $\pmb { \sigma }$ 是卫星上所见到的地球表面部分 (实为一球“帽")，卫星离地球越近，这一部分就越小．这里同样对卫星形状作了简化假定，否则 $A _ { a }$ 和 $\mathbf { A } _ { e }$ 的表达式更复杂.

求出摄动加速度 $A _ { a }$ 和 $\mathbf { A } _ { e }$ 后即可讨论对卫星轨道的影响，除上述特点外，与太阳直接照射的辐射压摄动效应类似。在一般情况下，反照辐射压摄动效应比直接辐射压摄动效应小近两个量级，因此，在一阶解精度要求下显然不必考虑，而在高精度要求下，考虑上述影响时还必须针对具体问题进行适当的简化，有时又必须进一步精化相应的数学模型.

# 参考文献

[1] Musen,P.,J. Geophs. Res.,65(1960),1391-1396.  
[2] Koskela,P.E.,J. Astronaut. Sci.,9(1962),71-82.  
[3]Kozai,Y.， Smithsonian Contr. Astrophys.，6(1963)，109-112.  
[4] Lala,P. and Sehnai,L.,Bull.Astron.Inst. Czech.,20(1969),327-330.  
[5] Lala,P.，Bull. Astron. Inst. Czech.,22(1971),63-72.  
[6] Mello,S.F.,Celest. Mech.,5(1972),80-101.  
[7] Smith,D.E.，Donamics of Satellite (1969)，284-294,Ed.B.Morando,Springer-Verlag， Berlin， Heidelberg,New York(1970).  
[8]Lautman,D.A.,Celest, Mech.,15(1977),387-420,16(1977),3-25.  
[9] Sehnal,L.,Bull. Astron. Inst. Czech.,30(1979)，199-204.  
[10] Sehnal,L.,Celest. Mech.,25(1981)，169-179.  
[11] Haley,D.,EG&G Report,8-73(1973).

# 第十章 大气阻力摄动

由于人造地球卫星是在近地空间飞行，特别是一些低轨道卫星，离地面只有几百千米，甚至低于200km，大气阻力的影响比较显著，使得卫星椭圆轨道不断变小变圆，对卫星的寿命往往起决定性作用.因此大气阻力摄动也是影响卫星运动的一种主要因素，特别对那些面质比较大的低轨卫星.

# 10.1 气动力及其有关问题

人造地球卫星在大气层中飞行的受力状况相当复杂，它是气体动力学领域中的一个极其重要的研究课题．卫星受力问题将涉及到低层的连续介质流和高层的自由分子流，以及介于其间的过渡流，还涉及到中性气体、电离气体和多成分的混合气体等复杂因素，在气体动力学中，对中性大气状态的基本假定是按鲁森数 $K _ { n }$ (Knudsen number)来划分的， ${ \pmb { K } } _ { n }$ 的定义为

$$
K _ { n } = \frac { \lambda } { L }
$$

这里 $\lambda$ 是气体分子平均自由程， $\pmb { L }$ 是飞行器的特征尺度，相应的划分如下：

$$
\left. \begin{array} { l } { K _ { n } < 0 . 0 1 , \qquad \mathrm { i } \hbar \llangle \frac { \dot { \omega } _ { 1 } } { 2 } \hbar \ll \dot { \mathcal { W } } , } \\ { K _ { n } = 0 . 0 1 - 0 . 1 , \frac { \dot { \omega } _ { 1 } } { \mathrm { i } \mathrm { R } } \dot { \omega } _ { 1 } \vert \underset { \mathrm { i } } { \times } , } \\ { K _ { n } = 0 . 1 - 1 0 , \quad \frac { \dot { \omega } _ { 1 } } { \mathrm { i } \times } \dot { \mathcal { W } } \underset { \mathrm { i } } { \times } \dot { \mathcal { W } } , } \\ { K _ { n } > 1 0 , \qquad \dot { \Theta } \underset { \mathrm { i } } { \oplus } \dot { \mathcal { W } } \dot { \mathcal { T } } \dot { \mathcal { W } } . } \end{array} \right\}
$$

在地面以上 $1 0 0 ~ \mathrm { k m }$ 处，气体分子平均自由程 $\lambda$ 约为 $\mathbf { 1 0 c m } _ { \mathrm { { a } } }$ ，在120km高度上约为 $\mathbf { l m } _ { i }$ 而在 $1 8 0 \mathbf { k m }$ 高度上则增大到100m．通常，人造地球卫星是在180km以上的高空飞行，而其特征尺度往往只有几米．因此,相应的大气状态属自由分子流．但有些特殊卫星(包括准备回收的卫星）和将要陨落的卫星总是要在180km以下的空间飞行,那么，相应的大气状态将是过渡流，甚至是连续介质流。

在大气层中飞行的卫星所受的气动力(包括阻力和升力)也随着相应的大气状态不同而异,但在自由分子流中，可以认为卫星所受的气动力就是大气阻力，阻力加速度由下式表达：

$$
D { = } { - } \frac { 1 } { 2 } \bigg ( \frac { C _ { D } S } { m } \bigg ) \rho V V .
$$

其中 $C _ { p }$ 是阻力系数， $\delta / m$ 是卫星的面质比（ $\boldsymbol { \mathfrak { S } }$ 是对阻力而言的有效截面积), $\pmb { \rho }$ 是卫星所在空间处的大气密度。 $\pmb { V } = \pmb { v } - \pmb { v _ { a } }$ 是卫星相对于大气的运动速度， $\pmb { v }$ 和 ${ \pmb v } _ { \pmb { a } }$ 分别为卫星和大气相对于地心的运动速度.

关于阻力系数 $C _ { p } ,$ ，在自由分子流中可视其为常数，通常取 $C _ { p }$ $= 2 . 2$ ，但是，对于那些尺度较大而飞行高度低于 $1 8 0 \mathbf { k m }$ 的卫星，将要处于大气的过渡流区．在此区域中，阻力系数 $C _ { D }$ 不再是常数，它与 $K _ { n }$ 等量有关,到目前为止，还没有得到较好的分析表达式,有些近似公式也是极其复杂的,不便于用来讨论或直接计算卫星的轨道变化,关于这个问题可参阅文献[1—2].不过，对于 $K _ { n } >$ 3的近自由分子流和自由分子流这两种状态，可将 $C _ { D }$ 统一表示成下列近似公式[81：

$$
\left. \begin{array} { l } { { C _ { D } = C _ { 0 } + C _ { 1 } K _ { n } ^ { - 1 } = C _ { 0 } + C ^ { \prime } { } _ { 1 } \rho , } } \\ { { } } \\ { { C _ { 0 } = 2 . 2 . } } \end{array} \right\}
$$

对于阻力公式(10.3)，除 $C _ { D }$ 的复杂性外，卫星的面质比 $\delta / m$ 将依赖卫星的姿态,一般会随时间而变化，而大气密度 $\rho$ 的问题就更复杂,它的分布不仅依赖空间,随时间的变化也相当显著．大气阻力又是一种耗散力，它将消耗卫星运动的动能，从而导致轨道半长径 ${ \pmb a }$ 不断减小，因此，讨论大气阻力摄动对卫星轨道的影响时，引用前几章给出的方法将会遇到两大问题：

1．由于是耗散力,引用摄动方法时受到一定的限制，而且轨道半长径 $\pmb { \sigma }$ 存在长期变化，这又将导致小参数幂级数解的结构发生变化，以致引起一些难以克服的困难(对分析方法固然如此，对数值方法也有影响).

2．阻力表达式本身有三种不确定因素，即 $\log \delta / m$ 和 $\pmb { \rho }$ （确切地说是密度分布中涉及到的一些参数，下一节再介绍)，特别是 $\rho$ 的分布规律至今还不十分清楚，是一个有待进一步研究的问题。

由于这些原因，大气阻力摄动己成为人卫（特别是低轨卫星）精密定轨中的一大障碍．故有些需要高精度定轨的卫星，往往都是对称体(或姿态容易掌握的)、小面质比和高轨道，如测地卫星、导航卫星等.

# 10.2大气模式与大气密度分布的近似表达式

# 1．高层大气及其研究状况

上节已指出，研究卫星运动在大气阻力影响下的变化规律，阻力加速度表达式中的密度分布是一个很关键的物理量，它涉及高层大气的有关参数及其变化,所谓大气模式，就是给出这些大气参数及其变化的一种数学模型（包括离散型的各类数据和一些逼近式)．自从人造卫星上天以来，各国已从不同资料来源（包括卫星阻力资料和卫星携带仪器在空间获得的直接测量资料),进行了长期的积累和研究，并取得了一些重大发现和结果,从而改变了人们对高层大气结构的认识．在此基础上曾先后给出过多种大气模式,应用较广的有CIRA-72（这是国际标准大气模式CIRA-61，65,72,86 系列中的一种),Jacchia-77,MSIS，DTM等模式．我国科学院人卫系统也曾开展过一些大气研究工作，并获得了有益的成果[\*],[5]。有关上述大气模式的特性、应用和研究动向，在文献[6]和[7]中有较全面的介绍，值得提出的是，在实际工作中，针对具体卫星和要求，对上述模式进行分析比较,从而给出某种简单的逼近模式还是有意义的。

所有上述高层大气模式，尽管彼此之间有差别（包括所采用的资料、考虑的因素和描述的参数等差别)，或适用不同的高度，但在大气密度分布方面几乎都反映了下述基本特征：

.（1）大气密度随高度增加而减小，减小的速度随高度增加而变慢,等密度面接近于地球形状，大致为扁球面.

(2）大气密度分布受太阳辐射(紫外和粒子辐射)的影响相当显著，愈高变化愈大.有周日变化、季节变化、半年变化和长周期变化(与太阳活动11年周期有关)等，大气成分也相应地有明显变化.从统计表现来看，太阳辐射影响可以用10.7cm流量和地磁指数来描述.

# 2．大气密度分布的一些近似表达式

如果只考虑大气的重力平衡，在一定的近似下，根据流体静力学可知，基密度分布是指数函数形式,即

$$
\rho { = } \rho _ { 0 } \mathbf { e x p } \mathbb { Z } { - } \left( r { - } r _ { 0 } \right) / H \mathbb { ] } .
$$

此为球形大气， $\rho _ { 0 }$ 是参考球面 $r = r _ { 0 }$ 上的大气密度， $\pmb { H }$ 称为密度标高，假定为常数，这符合密度随高度增加而减小的规律，但根据上述各大气模式已知，密度随高度的变化愈到高层愈慢，因此密度标高 $H$ 应随高度缓慢地增大，一个较好的近似是假定 $\pmb { H }$ 随高度 $\hbar$ 线性变化[8],在 $h { = } 2 0 0 { - } 6 0 0 ~ \mathrm { k m }$ 之间，可取

$$
H { = } H ( r ) { = } H _ { 0 } { + } \frac { \mu } { 2 } ( r { - } r _ { 0 } ) ,
$$

$\mu \approx 0 . 1$ ，一般 $\mu < 0 . 2$ ，相应的密度公式(10.5)变为

$$
\begin{array} { l } { { \pmb \rho = \rho _ { 0 } \mathbf { e x p } \big [ - \left( \pmb { r } - \pmb { r } _ { 0 } \right) / H \left( \pmb { r } \right) \big ] } } \\ { = \rho _ { 0 } \bigg [ 1 + \frac { \mu } { 2 } \bigg ( \frac { \pmb { r } - \pmb { r } _ { 0 } } { H _ { 0 } } \bigg ) ^ { 2 } \bigg ] \mathbf { e x p } \bigg [ - \left( \pmb { r } - \pmb { r } _ { 0 } \right) / H _ { 0 } \bigg ] } \end{array}
$$

对于CIRA-61模式, $h = 2 0 0 { \bf k m }$ 处，有

$$
\rho _ { 0 } = 3 . 6 \times 1 0 ^ { - 1 0 } \mathrm { k g } \cdot \mathrm { m } ^ { - 3 } , H _ { 0 } = 3 7 . 4 \mathrm { k m } , \mu = 0 . 1 .
$$

由于地球是扁球体，在重力平衡条件下,大气的等密度面亦可认为是相似的扁球面[8],[91,那么(10.7)式可修正为下列形式：

$$
\begin{array} { l } { \rho { = \rho _ { 0 } \exp [ - \left( r - \sigma \right) / H \left( r \right) ] } } \\ { { \ } } \\ { { = \rho _ { 0 } \bigg [ 1 + \displaystyle \frac { \mu } { 2 } \bigg ( \displaystyle \frac { r - \sigma } { H _ { 0 } } \bigg ) ^ { 2 } \bigg ] \exp [ - \left( r - \sigma \right) / H _ { 0 } ] . } } \end{array}
$$

这就是扁球大气，其中 $\pmb { \sigma }$ 是地心和通过参考点（对应密度为 $\rho _ { 0 }$ ，密度标高为 $H _ { 0 } )$ 的椭球面之间的距离，见后面的图10.3．（10.8)式基本上反映了大气在地球重力影响下的一种空间分布规律，与已有的大气模式所给出的平均密度分布规律比较符合．在King-Hele等人早期有关大气及大气阻力对卫星轨道影响的研究工作中，就是采用这种近似密度表达式的 $[ 8 - 1 1 ]$ ，相应的参考点是取卫星轨道的初始近地点 ${ \pmb p _ { 0 } }$ （在该点附近，大气阻力对卫星轨道的影响最显著), $\rho _ { 0 }$ 和 $\scriptstyle { H _ { 0 } }$ 即 $\rho _ { p _ { 0 } }$ 和 $H _ { v _ { 0 } }$ ·

前面己指出,大气密度分布受太阳辐射的影响相当显著，呈现各种周期变化，其中与地球自转有关的周日效应尤为明显,在同一高度和纬度上，白天的密度要比夜间的密度大得多，地方恒星时14时密度达到极大,在其“附近”,密度变化快，而密度极小值附近变化平缓,出现在地方恒星时2--5时，但正如Cook和King-Hele曾提出的,作为第一近似,可以假设地心和周日效应的极大、极小是共线的，且等密度面相对该轴线是对称的[12]。在此假定下，同时考虑密度随高度和时间的变化，有

$$
\rho { = } \rho _ { 0 } ( 1 { + } F ^ { \ast } \cos \psi ) \exp \mathcal { - } \left( r { - } \sigma \right) / H ( r ) \mathcal { I } .
$$

其中 $\psi$ 是所考虑密度那一点(即卫星所在处)的地心向径 $\pmb { r }$ 与密度周日峰 (对应密度极大值)方向 $\pmb { r _ { m } }$ 之间的夹角．在上述对称周日效应的假定下，周日峰方向与太阳方向之间的关系为

$$
\left. \begin{array} { c } { { \alpha _ { m } = \alpha + \lambda _ { m } , } } \\ { { \delta _ { m } = \delta , } } \end{array} \right\}
$$

其中 $\alpha , \delta$ 是太阳的赤经赤纬， $\lambda _ { m }$ 可取 $3 0 ^ { \circ } . \quad F ^ { * }$ 称为周日变化因子,它与昼夜密度比 $f ^ { * }$ 之间的关系为

$$
\left. \begin{array} { l } { { f ^ { * } = \displaystyle \frac { \rho _ { \mathrm { m a x } } } { \rho _ { \mathrm { m i n } } } { = } \displaystyle \frac { 1 + F ^ { * } } { 1 - F ^ { * } } } , } \\ { { F ^ { * } = \displaystyle \frac { f ^ { * } - 1 } { f ^ { * } + 1 } . } } \end{array} \right\}
$$

按此定义， $\rho _ { 0 }$ 就是参考椭球面 $\pmb { r } = \pmb { \sigma }$ 上的周日平均密度，对应$\psi = 9 0 ^ { \circ } .$

显然，密度分布的数学模型还可进一步修正，如周日效应随高度的变化，非对称周日效应，季节变化等，相应的 $\rho = \rho _ { 0 } ( t )$ 就更加复杂化，但这并未改变密度表达式的基本形式，在讨论大气阻力对卫星轨道影响的规律时，不会增加任何新的实质性的信息，而在精密定轨中，却可在大气模式的基础上（或某种局部的逼近式）采用离散点密度的直接计算，不必在密度分布的分析表达式上做更多的修正．因此，下面将根据应用较广也较简单的密度公式(10.9)，来讨论大气阻力对卫星轨道的影响，从而得出一些大气阻力摄动的基本规律，相应的结果在一般人卫工作中也可引用：当然，针对不同高度、不同卫星，还出现过一些有别于上述形式的密度公式，这里不再一一列举.

密度表达式中的一些参数和大气阻力加速度中的另两个参数$C _ { D }$ 和 $\mathbb { S } / m$ ，都可以在卫星定轨（指多资料定轨，即轨道改进）的同时进行相应的修正.

# 10.3 大气阻力摄动的基本方程

# 1．静止大气和旋转大气中的阻力加速度

由(10.3)式可知，静止大气和旋转大气两种情况下的大气阻力加速度是有明显差别的，对于静止大气， $\pmb { \tau } _ { a } = 0 , V = \pmb { \sigma }$ ，于是(10.3)式变为

$$
\left. \begin{array} { l } { { \pmb { { \cal D } } = - \frac { 1 } { 2 } \bigg ( \frac { C _ { D } S } { m } \bigg ) \rho v ^ { 2 } ( \pmb { v } / v ) , } } \\ { { \pmb { v } } ^ { 2 } = \frac { 2 } { \pi } - \frac { 1 } { a } = \frac { 1 + e \cos f } { a ( 1 - e ^ { 2 } ) } . } \end{array} \right\}
$$

显然,在这种情况下,阻力加速度只有切向分量,即

$$
\left. \begin{array} { l l } { { U = - { \displaystyle \frac { 1 } { 2 } } \bigg ( { \displaystyle \frac { C _ { D } S } { m } } \bigg ) \rho v ^ { 2 } = - { \displaystyle \frac { A } { 2 } } \rho { \displaystyle \frac { 1 + 2 \dot { e } \cos f + e ^ { 2 } } { a ( 1 - e ^ { 2 } ) } } , } } \\ { { N = 0 , } } \\ { { W = 0 , } } \end{array} \right\}
$$

其中A=CDS

事实上，大气并非处于静止状况,大气有旋转，但情况比较复杂，早期,人们作了一些简单处理，认为大气由地球“带动”,随地球自转而旋转，其旋转角速度 $\omega _ { u }$ 就是地球自转角速度 $n _ { e } ^ { \ [ 8 ] }$ .根据近年来利用卫星倾角的变化测定大气旋转速率的结果[12],发现这一旋转速率不仅随高度变化而不同 $( h = 1 2 5 { \mathrm { k m } }$ ， ${ \omega _ { a } = n _ { e } }$ ， $h = 3 2 5$ km, $\omega _ { \omega } = 1 . 2 2 n _ { e } , h$ 再增大， $\omega _ { a }$ 又下降， $h = 4 0 0 \mathrm { k m }$ ， $\omega _ { a } = n _ { e } , \ h = 6 0 0$ km, $\omega _ { a } = 0 . 8 2 n _ { e } , \cdots )$ ,还有周日变化(6时一12时， $\omega _ { a }$ 较小,18时一24时， $\omega _ { a }$ 较大)和季节变化(夏季的 $\omega _ { a }$ 比冬季的 $\omega _ { a }$ 小， $\varpi _ { \alpha }$ 为 $\omega _ { a }$ 的平均值)．不过，这里仍采用 $\omega _ { a } = n _ { e }$ 来研究大气旋转效应的摄动效果．在此假定下，有

$$
v _ { a } = r \cos \varphi \dot { n } _ { e } ,
$$

其中是卫星所在处的地心纬度。卫星运动速度v在切向、主法向和次法向(既轨道面法向)的三个分量为

$$
\begin{array} { r } { v _ { U } = v , v _ { N } = 0 , v _ { \mathrm { w } } = 0 . } \end{array}
$$

由图10.1可知，大气旋转速度va在径向、横向和轨道面法向的三个分量为

$$
 \begin{array} { l } { ( v _ { a } ) _ { S } = 0 , } \\ { ( v _ { a } ) _ { T } = r \cos \varphi n _ { e } \cos i ^ { \prime } \} } \\ { ( v _ { a } ) _ { W } = - r \cos \varphi n _ { e } \sin i ^ { \prime } . } \end{array} \}
$$

![](images/c6cdc5302ee4ebaac9defd2019aea140f430601678edbd798e65b2201080b970.jpg)  
图10.1过卫星 $s _ { * }$ 的辅助球面  
图10.2轨道平面内几个方向的几何关系

![](images/72b53273e251684ef0b3d319339ce2617003b80ff4187fea71fdd8b91e9e11b9.jpg)

于是根据图10.2可得到\~。在上述切向，主法向和轨道面法向的三个分量为

$$
\left. \begin{array} { l } { { \left( v _ { a } \right) _ { U } = \left( v _ { a } \right) _ { T } \sin \theta , } } \\ { { \left( v _ { a } \right) _ { N } = \left( v _ { a } \right) _ { T } \cos \theta , } } \\ { { \left( v _ { a } \right) _ { W } = - r \cos \varphi n _ { e } \sin \dot { \iota } ^ { \prime } . } } \end{array} \right\}
$$

根据第四章给出的几何关系(4.63)一(4.64)式，有

$$
 \begin{array} { l } { { \displaystyle { \tan \theta } = r / \frac { d r } { d f } { = } \frac { 1 + e \cos f } { e \sin f } , } } \\ { { \displaystyle { \sin \theta } = \frac { 1 + e \cos f } { \sqrt { 1 + 2 e \cos f - e ^ { 2 } } } { = } 1 - \frac { e ^ { 2 } } { 2 } \sin ^ { 2 } f + O ( e ^ { 3 } ) , } } \\ { { \displaystyle { \cos \theta } { = } \frac { e \sin f } { \sqrt { 1 + 2 e \cos f + e ^ { 2 } } } { = } e \sin f - \frac { e ^ { 2 } } { 2 } \sin 2 f {  } O ( e ^ { 3 } ) . } } \end{array} \}
$$

将(10.18)式和(10.16)式代人(10.17)式，再和(10.15)式一起代人(10.3)式，即得旋转大气阻力摄动加速度的三个分量：

$$
\left. \begin{array} { l } { { U = - \displaystyle \frac { 1 } { 2 } \left( \frac { C _ { D } \delta } { m } \right) \rho V v \left\{ 1 - \left( \frac { r \pi _ { e } } { v } \right) \cos \varphi \cos \theta ^ { * } \right. ^ \qquad } } \\ { { \left. \qquad \left[ 1 - \frac { e ^ { 2 } } { 2 } \sin ^ { 2 } f + O ( e ^ { 3 } ) \right] \right\} , } } \\ { { N = - 1 / 2 \Bigg ( \frac { C _ { D } \delta } { m } \Bigg ) \rho V v \Bigg \{ - \left( \frac { r \pi _ { e } } { v } \right) \cos \varphi \cos \theta ^ { * } \left[ e \sin f \right. } } \\ { { \left. \qquad \quad - \frac { e ^ { 2 } } { 2 } \sin 2 f + O ( e ^ { 3 } ) \right] \Bigg \} , } } \\ { { W = - \displaystyle \frac { 1 } { 2 } \left( \frac { C _ { D } \delta } { m } \right) \rho V v \left\{ \left( \frac { r \pi _ { e } } { v } \right) \cos \varphi \sin \dot { \theta } ^ { * } \right\} \qquad } } \end{array} \right\}
$$

其中

$$
\begin{array} { c c } { { } } & { { V = \left| \ v - \mathcal { D } _ { a } \right| } } \\ { { } } & { { } } \\ { { \displaystyle = v \left[ 1 - \left( \frac { r n _ { e } } { v } \right) \cos \varphi \cos \theta ^ { \prime } + \frac { 1 } { 2 } \left( \frac { r n _ { e } } { v } \right) ^ { 2 } \cos ^ { 2 } \varphi \sin ^ { 2 } \theta ^ { \prime } \right. } } \\ { { } } & { { } } \\ { { \displaystyle \left. + O \left( \left( \begin{array} { c } { { \frac { r n _ { e } } { v } } } \end{array} \right) ^ { 2 } e ^ { 2 } \right) \right] } . }  & { { ( 1 } } \end{array}
$$

对近地卫星(如 $2 ^ { \mathbf { h } }$ 卫星)，有

$$
\frac { r n _ { e } } { v } { = } \frac { 1 } { 1 2 } { \approx } 0 . 8 \times 1 0 ^ { - 1 } ,
$$

而需要考虑大气阻力摄动的卫星，其轨道偏心率不会太大，例如 $^ e$ $\prec 0 . 2$ （若近地高度 $h _ { p } = 2 5 0 { \mathrm { k m } }$ ，当 $e = 0 , 2$ 时，则远地高度 $h _ { p ^ { \prime } } =$ 3564km),因此有

$$
\biggl ( \frac { r n _ { e } } { v } \biggr ) ^ { 2 } e = 1 0 ^ { - 3 } , \biggl ( \frac { r n _ { e } } { v } \biggr ) e ^ { 2 } = 3 \times 1 0 ^ { - 3 } .
$$

邂去这些小项,并利用球面三角公式(见图10.1):

$$
\left. \begin{array} { l } { { \cos \varphi \cos i ^ { \prime } = \cos i , } } \\ { { } } \\ { { \cos \varphi \sin i ^ { \prime } = \cos u \sin i , } } \end{array} \right\}
$$

(10.19)式可简化成下列形式：

$$
\begin{array} { l } { { \displaystyle U = - \frac { 1 } { 2 } \biggl ( \frac { C _ { p } S } { m } \biggr ) \rho v ^ { 2 } \biggl [ 1 - 2 \langle \frac { r n _ { e } } { v } \rangle \cos \delta + \biggl ( \frac { r n _ { e } } { v } \biggr ) ^ { 2 } \cos ^ { 2 } \delta } } \\ { { \displaystyle \qquad + \frac { 1 } { 2 } \biggl ( \frac { r n _ { e } } { v } \biggr ) ^ { 2 } \cos ^ { 2 } u \sin ^ { 2 } \delta \biggr ] } , } \\ { { \displaystyle N = - \frac { 1 } { 2 } \biggl ( \frac { C _ { p } S } { m } \biggr ) \rho v ^ { 2 } \biggl [ - \biggl ( \frac { r n _ { e } } { v } \biggr ) e \cos \delta \sin f \biggr ] , } } \\ { { \displaystyle - \frac { 1 } { 2 } \biggl ( \frac { C _ { p } S } { m } \biggr ) \rho v ^ { 2 } \biggl [ \biggl ( \frac { r n _ { e } } { v } \biggr ) \cos u \sin i - \biggl ( \frac { r n _ { e } } { v } \biggr ) ^ { 2 } \cos u \sin i \cos \delta \biggr ] } . }  \end{array}
$$

在上述假定下,如果再略去该式中的

$$
\bigg ( \frac { r n _ { e } } { v } \bigg ) ^ { 2 } ; = 7 \times 1 0 ^ { - 3 } , \bigg ( \frac { r n _ { e } } { v } \bigg ) e = 1 . 7 \times 1 0 ^ { - 2 } ,
$$

并引进 $v ^ { 2 }$ 的根数形式，则三个阻力摄动加速度分量最后可写成

$$
\left. \begin{array} { c } { { U = - \displaystyle \frac 1 2 A _ { 1 } \frac { 1 + 2 e \cos f + e ^ { 2 } } { a ( 1 - e ^ { 2 } ) } \rho , } } \\ { { N = 0 , } } \\ { { W = - \displaystyle \frac 1 2 A _ { 2 } r \cos u \sin i ~ \left[ \frac { 1 + 2 e \cos f + e ^ { 2 } } { a ( 1 - e ^ { 2 } ) } \right] ^ { 1 / 2 } \rho . } } \end{array} \right\}
$$

其中

$$
\left. \begin{array} { r l } {  } & { { } A _ { 1 } = \bigg ( \frac { C _ { D } S } { m } \bigg ) F ^ { 2 } , ~ A _ { 2 } = \bigg ( \frac { C _ { D } S } { m } \bigg ) n _ { e } F , } \\ { F = \bigg ( 1 { - } \frac { r n _ { e } } { v } \cos i \bigg ) { - } \bigg ( 1 { - } \frac { r _ { p _ { 0 } } n _ { e } } { v _ { p _ { 0 } } } \cos i \bigg ) . } \end{array} \right.
$$

如果大气静止，即 $n _ { e } = 0 .$ ，则(10.23)式退化成(10.13)式， $\pmb { W }$ 分量显然是直接反映大气旋转的．(10.23)式的简化，主要是略去了加速度分量 $N$ ,这不仅因为其量级较小，而且根据摄动运动方程的特点，略去该小项不会改变大气阻力摄动的性质·

# 2．摄动运动方程

对于静止大气情况，将(10.13)式中的 $U$ 代入第四章给出的摄动运动方程(4.81)得

$$
\left. \begin{array} { l } { \displaystyle \frac { d \alpha } { d \xi } = - \frac { A n \alpha ^ { 2 } } { ( 1 - \epsilon ^ { 2 } ) ^ { 2 / 2 } } \left( 1 + 2 \varepsilon \cos { f } + \varepsilon ^ { 2 } \right) ^ { 3 / 2 } \rho , } \\ { \displaystyle \frac { d \alpha } { d \xi } = - \frac { A n \alpha } { ( 1 - \epsilon ^ { 2 } ) ^ { 1 / 2 } } \left( \cos { f } + \varepsilon \right) \left( 1 + 2 \varepsilon \cos { f } + \varepsilon ^ { 2 } \right) ^ { 1 / 2 } \rho , } \\ { \displaystyle \frac { d \vec { x } } { d \xi } = 0 , } \\ { \displaystyle \frac { d \vec { Q } } { d \xi } = 0 , } \\ { \displaystyle \frac { d \vec { Q } } { d \xi } = - 0 , } \\ { \displaystyle \frac { d \omega } { d \xi } - \frac { A n \alpha } { e ( 1 - \epsilon ^ { 2 } ) ^ { 1 / 2 } } \sin { f } \left( 1 + 2 \varepsilon \cos { f } + \varepsilon ^ { 2 } \right) ^ { 1 / 2 } \rho , } \end{array} \right\} \left( 1 + 2 \varepsilon \cos { f } \right) ,
$$

$$
+ e ^ { 2 } ) ^ { 1 / 2 } \rho ,
$$

由此还可给出近地距 $\scriptstyle \gamma _ { p } = a ( 1 - e )$ 的变化率，即

$$
\begin{array} { r } { \frac { d r _ { p } } { d t } = - \frac { A n a ^ { 2 } } { ( 1 - e ^ { 2 } ) ^ { 3 / 2 } } ( 1 + 2 e \cos f + e ^ { 2 } ) ^ { 1 / 2 } ( 1 - \cos f ) ( 1 - e ) ^ { 2 } \rho } \\ { \leqslant 0 , \quad \qquad \quad ( 1 0 . 2 e ^ { 2 } ) ^ { 1 / 2 } \rho } \end{array}
$$

上述各式中的 $\pmb { n } = \pmb { a } ^ { - 3 / 2 }$ ，方程表明，在静止大气阻力摄动下,卫星轨道面不变，而轨道半长径 $\pmb { a }$ 和近地距 $r _ { p }$ 在不断减小．事实上，仅根据上述方程还不能立即得出偏心率 $\pmb { \theta }$ 也是不断减小的结论，因 $( \cos f \div e )$ 并不恒大于零，后面将会从平均效应得知这一：结果.

对于旋转大气，暂以(10.23)式的 $\boldsymbol { U }$ 和 $\pmb { W }$ 代人方程(4.81)，得

$$
\left. \begin{array} { l } { { \displaystyle \frac { d a } { d t } = - \frac { A _ { 1 } n a ^ { 2 } } { ( 1 - e ^ { 2 } ) ^ { 3 / 2 } } ( 1 + 2 e \cos f + e ^ { 2 } ) ^ { 3 / 2 } \rho , } } \\ { { \displaystyle \frac { d e } { d t } = - \frac { A _ { 1 } n \dot { a } } { ( 1 - e ^ { 2 } ) ^ { 1 / 2 } } ( \cos f + e ) ( 1 + 2 e \cos f + e ^ { 2 } ) ^ { 1 / 2 } \rho , } } \\ { { \displaystyle \frac { d \dot { a } } { d t } = - \frac { A _ { 2 } a \sin { i } } { 4 ( 1 - e ^ { 2 } ) } \left( \frac { r } { a } \right) ^ { 2 } ( 1 + \cos 2 u ) ( 1 + 2 e \cos f + e ^ { 2 } ) ^ { 1 / 2 } \rho , } } \\ { { \displaystyle \frac { d Q } { d t } = - \frac { A _ { 2 } a } { 4 ( 1 - e ^ { 2 } ) } \left( \frac { r } { a } \right) ^ { 2 } \sin { 2 u } ( 1 + 2 e \cos f + e ^ { 2 } ) ^ { 1 / 2 } \rho , } } \end{array} \right\}
$$

$$
\begin{array} { l } { \displaystyle \frac { d \omega } { d t } = - \frac { A _ { 1 } n a } { e ( 1 - e ^ { 2 } ) ^ { 1 / 2 } } \sin f ( 1 + 2 e \cos f + e ^ { 2 } ) ^ { 1 / 2 } \rho - \cos i \frac { d \Omega } { d t } , } \\ { \displaystyle \frac { d M } { d t } = n + \frac { A _ { 1 } n a } { e ( 1 - e ^ { 2 } ) } \Big ( \frac { r } { a } \Big ) \sin f ( 1 + e \cos f + e ^ { 2 } ) \left( 1 + 2 e \cos f \right. } \\ { \displaystyle \left. + e ^ { 2 } \right) ^ { 1 / 2 } \rho . } \end{array}
$$

这组方程与(10.25）式的主要差别在于轨道面 $( i , \Omega )$ 有变化，此即大气旋转效应的特点。倾角 $\pmb { i }$ 将有长期变化，因此人们用倾角的变化来测定大气旋转参数[13．除此之外，其它四个根数对应的摄动方程与静止大气情况类似,仅“参数” $\pmb { A }$ 变为 $\pmb { A } _ { 1 }$ ·

关于 $\pmb { i }$ 的变化，由方程(10.27)不难看出,它也是不断减小的.用圆轨道可给出粗略的估计式，即

$$
0 { \geq } \frac { d i } { d n } { \geq } - \frac { n _ { e } } { 3 n } \frac { / } { ( n - \varkappa _ { e } ) } ,
$$

其中 $\pmb { n } = \pmb { a } ^ { - 3 / 2 }$ 从高度 $h$ （相应地有 $\pmb { n } _ { 1 } )$ 降低到 $\pmb { h } _ { \mathbb { J } }$ （对应 ${ \bf \sigma } _ { { \pmb { \mathscr { R } } } _ { 0 } } )$ ，积分上式得

$$
\Delta i \ge \frac { 1 } { 3 } \mathrm { i n } \frac { n _ { 0 } \left( n _ { 1 } - n _ { e } \right) } { n _ { \mathrm { i } } \left( n _ { 0 } - n _ { e } \right) } .
$$

其中 $\pmb { n _ { e } = 0 . 0 5 8 8 }$ ，若分别取 $\pmb { h } _ { 1 }$ 为 $\mathbf { 1 0 0 0 k m , 1 2 0 0 k m , 1 4 0 0 k m }$ 而 $h _ { 0 }$ 取为 $\mathbf { 1 0 0 k m }$ （卫星下降到该高度后很快就要陨落)，则有下列结果：

$$
\Delta i \geq \{ \begin{array} { l l } { - 0 ^ { \circ } . 2 7 , } & { \ h _ { 1 } = 1 0 0 0 \mathrm { k m } , } \\ { - 0 ^ { \circ } . 3 3 , } & { \ h _ { 1 } = 1 2 0 0 \mathrm { k m } , } \\ { - 0 ^ { \circ } . 3 9 , } & { \ h _ { 1 } = 1 4 0 0 \mathrm { k m } . } \end{array}  \quad \}
$$

这表明，在卫星整个寿命期间，由于大气旋转效应引起的倾角变化(减小)大约在 $0 ^ { \circ } . 3 { - } 0 ^ { \circ } . 4$ 左右.

# 3.大气密度 $p$ 的根数表达式

若要研究卫星轨道在大气阻力摄动影响下的变化规律，就必须将方程（10.25）或（10.27）各式右端出现的大气密度 $\rho$ 表示成卫星轨道根数的形式.

（1）球形大气取参考点为初始近地点 ${ \pmb p _ { 0 } }$ ，相应的密度为$\rho _ { { \tiny ? } { \tiny \cap } }$ ，将

$$
r = a ( 1 - e \cos E ) , r _ { p _ { 0 } } = \mathfrak { z } _ { 0 } ( 1 - e _ { 0 } )
$$

代人（10.5）式得

$$
\rho = \rho _ { p _ { 0 } } \in \mathbf { x p } \bigg [ { - \frac { 1 } { H } ( a - a _ { 0 } + a _ { 0 } e _ { 0 } ) \bigg ] \exp \bigg ( \frac { a e } { H } \cos E } \bigg ) .
$$

这里引用偏近点角 $\pmb { \cal E }$ 作为卫星轨道的第六个根数是为了后面求摄动解的需要，

(2）扁球大气对(10.8)式，暂不考虑密度标高 $\pmb { H }$ 的变化， $\sigma$ 就取为过初始近地点 ${ \pmb p _ { 0 } }$ 的旋转椭球面，见图10.3,该椭球面上任·点的向径 $\pmb { \sigma }$ 由下式计算：

$$
\sigma = \sigma _ { 0 } [ 1 - \epsilon \sin ^ { 2 } \varphi + O ( \epsilon ^ { 2 } ) ] .
$$

![](images/c7b31312f685dcb4eb1c422ca8da4a7515cf628efff5a9146e71f2f0a5a637b6.jpg)  
图10.3等密度面为扁球面的示意图

其中 $\sigma _ { 0 }$ 是相应的“赤道”半径(即椭圆的半长径)， $\varphi$ 是地心纬度， $\pmb { \epsilon }$ 是扁率，取地球的值，即

$$
\epsilon = \frac { 1 } { 2 9 8 . 2 5 7 } { = 0 . 0 0 3 3 5 2 8 } .
$$

因参考椭球面过初始近地点 ${ \pmb \mathcal { P } } _ { \pmb { 0 } } ,$ 有

$$
\sigma _ { p _ { 0 } } = \sigma _ { 0 } ( 1 - \epsilon \sin ^ { 2 } \varphi _ { p _ { 0 } } ) = r _ { p _ { 0 } } .
$$

代入(10.32)式得

$$
\sigma = r _ { p _ { 0 } } { \frac { 1 - \epsilon \sin ^ { 2 } \varphi } { 1 - \epsilon \sin ^ { 2 } \varphi _ { p } } }
$$

根据

$$
\sin \varphi = \sin i \sin ( f \div \omega ) , \sin \varphi _ { p } = \sin i \sin \omega _ { 0 } ,
$$

于是得

$$
\begin{array} { c } { { r - \sigma = \displaystyle r - r _ { p _ { 0 } } \big [ 1 - \epsilon \sin ^ { 2 } \varphi + \epsilon \sin ^ { 2 } \varphi { } _ { p _ { 0 } } + O ( \epsilon ^ { 2 } ) \big ] } } \\ { { \mathrm { } } } \\ { { = \displaystyle ( r - r _ { p _ { 0 } } ) + \frac { 1 } { 2 } \epsilon r _ { p _ { 0 } } \sin ^ { 2 } \dot { \epsilon } \big [ - \cos 2 ( f + \omega ) + \cos 2 \omega _ { 0 } \big ] } } \\ { { \mathrm { } } } \\ { { \therefore O ( \epsilon ^ { 2 } ) , \qquad ( 1 0 . } } \end{array}
$$

将此结果代入(10.8)式得

$$
\rho = \rho _ { p _ { 0 } } \mathrm { e x p } \biggl [ - \frac { r - r _ { p _ { 0 } } } { H } + C \cos 2 \left( f + \omega \right) - C \cos 2 \omega _ { 0 } + O \left( C \epsilon \right) \biggr ] .
$$

其中 $c$ 称为扁率参数，即

$$
C = \frac { 1 } { 2 } \frac { \epsilon } { H } r _ { p _ { 0 } } \sin ^ { 2 } \hat { t } ,
$$

一般有 $\mathcal { C } { \simeq } 0 . 1$ ，与处理球形大气一样，(10.35)式可表示为

$$
\rho = \rho _ { p _ { 0 } } \exp \Biggl [ - \frac { 1 } { H } ( a - a _ { 0 } + a _ { 0 } e _ { 0 } ) - C \cos 2 \omega _ { 0 } \Biggr ] \exp \Biggr [ \frac { a e } { H } \mathrm { c o s } E
$$

$$
+ C \cos 2 \left( f + \omega \right) + O ( C \epsilon ) ] .
$$

为了后面求摄动解的需要，利用

$$
r \cos f = a ( \cos E - e ) , r \sin f = a { \sqrt { 1 - e ^ { 2 } } } \sin E , r = a ( 1 - e \cos E )
$$

将 $\exp [ C \cos 2 ( f + \omega ) ]$ 表示成下列形式：

$$
\begin{array} { r } { \exp [ \mathcal { C } ( \cos 2 ( f + \omega ) ] = 1 + C \cos 2 ( f + \omega ) - 2 C e \sin E \sin 2 ( E + \omega ) } \end{array}
$$

$$
+ \frac { 1 } { 4 } C ^ { 2 } [ 1 + \cos 4 ( E + \omega ) ] - \frac { 1 } { 2 } \ : C e ^ { 2 } \ : [ \cos 2 \omega \div 2 \cos 2 ( E + \omega )
$$

$$
\begin{array} { r } { - 3 \cos 2 E \cos 2 ( E + \omega ) ] - C ^ { 2 } e \sin E \sin 4 ( E + \omega ) + \cdots } \end{array}
$$

代入（10.37）式得

$$
\begin{array} { c c } { { \rho = k \Bigg \{ \Bigg ( 1 + \frac { C ^ { 2 } } { 4 } \Bigg ) + C \cos 2 \omega \big ( - e \cos \theta + \cos 2 E + e \cos 3 E \big ) } } \\ { { + C \sin 2 \omega \big ( e \sin B - \sin 2 E - e \sin 3 B \big ) } } \\ { { + C ^ { 2 } \cos 4 \omega \Bigg ( \displaystyle \frac { 1 } { 4 } \cos 4 E \Bigg ) + C ^ { 2 } \sin 4 \omega \Bigg ( - \displaystyle \frac { 1 } { 4 } \sin 4 E \Bigg ) } } \\ { { + O ( C \epsilon ) + O ( C e ^ { 2 } ) + O ( C ^ { 2 } e ) } } \\ { { + O ( C ^ { 2 } ) \Bigg \} \exp \Bigg ( \displaystyle \frac { \alpha e } { H } \cos E \Bigg ) , } } \end{array}
$$

其中

$$
\boldsymbol k = \rho _ { p _ { 0 } } \mathrm { e x p } \bigg [ { - \frac { 1 } { H } ( a - a _ { 0 } + a _ { 0 } e _ { 0 } ) - C \cos { 2 \omega _ { 0 } } } \bigg ] .
$$

当 $e < 0 . 2$ 时，（10.38)式中略去的项为

$$
O \left( C \epsilon \right) = 3 \times 1 0 ^ { - 4 } , O \left( C e ^ { 2 } \right) = O \left( C ^ { 2 } e \right) = O \left( C ^ { 3 } \right) = 1 0 ^ { - 3 } .
$$

(3）考虑周日变化的扁球大气这里仍先假定(10.9)式中的$H ( r )$ 为常数．若记 $\hat { r }$ 和 $\hat { \pmb { r } } _ { m }$ 分别为卫星向径和密度周日峰方向的单位向量，则

$$
\cos \psi { = } \hat { \pmb { r } } { \cdot } \hat { \pmb { r } } _ { m } .
$$

在地心赤道坐标系中有

$$
\hat { \pmb { r } } = \cos f \hat { \pmb { P } } + \sin f \hat { \pmb { Q } }
$$

其中 $\hat { p }$ 和 $\hat { \boldsymbol { Q } }$ 都是 $i , \Omega , \omega$ 的函数，具体形式见第二章(2.45)和(2.46)式．根据(10.10)式， $\widehat { r } _ { m }$ 的三个分量为

$$
\cos \delta \cos ( \alpha + \lambda _ { m } ) , \cos \delta \sin ( \alpha + \lambda _ { m } ) , \sin \delta ,
$$

利用球面三角公式(见图10.4)

$$
\cos \delta \cos \alpha = \cos L ,
$$

$$
\begin{array} { r } { \cos \delta \sin \alpha = \sin L \cos \varepsilon , } \end{array}
$$

$$
\sin \delta = \sin L \sin \varepsilon ,
$$

可将 $\hat { r } _ { m }$ 表为

![](images/65e8952e61d8ae3a746691b3facaa48a79750423a619cfd28e8572a696db5304.jpg)  
图10.4赤道坐标与黄道坐标关系

$$
\hat { \pmb { r } } _ { m } = \left( \begin{array} { c } { \cos L \cos \lambda _ { m } - \sin L \sin \lambda _ { m } \cos \varepsilon } \\ { \cos L \sin \lambda _ { m } + \sin L \cos \lambda _ { m } \cos \varepsilon } \\ { \sin L \sin \varepsilon } \end{array} \right) ,
$$

其中 $\pmb { L }$ 是太阳的平黄经， $\pmb { \varepsilon }$ 是黄赤交角.将 $\hat { \pmb r }$ 和 $\hat { r } _ { m }$ 的表达式代人（10.40)式，进行适当的整理即得

$$
\cos \psi = A ^ { * } \cos f + B ^ { * } \sin f ,
$$

其中

$$
\begin{array} { r l } & { \begin{array} { r l } & { A ^ { * } = \frac { 1 } { 4 }  ( 1 + \cosh \bar { t } ) \bar { \zeta } ( ( 1 - \exp \xi ) \cos ( \omega + \mathcal { Q } + L - \lambda _ { \mathrm { s h } } )  } \\ & {  \qquad + ( 1 + \cos \bar { t } ) \cos ( \omega + \mathcal { Q } - L - \lambda _ { \mathrm { s h } } )  } \\ & {  \qquad + ( 1 - \cos \bar { t } ) [ ( 1 - \cos \bar { t } ) \cos ( \omega - \mathcal { Q } - L + \lambda _ { \mathrm { s h } } )  } \\ & {  \qquad + ( 1 - \cos \bar { t } ) \cos ( \omega - \mathcal { Q } + L + \lambda _ { \mathrm { s h } } ) ] \sin [ \sqrt { \pi } \sin ( \omega ) ] } \\ & {  \qquad \mathrm { s i n ~ } L \sin [ \sin ^ { 2 } ] , } \end{array} } \\ & { B ^ { * } = - \frac { 1 } { 4 }  ( 1 + \cosh \bar { t } ) [ ( 1 - \cos \bar { t } ) \sin ( \omega + \mathcal { Q } + L - \lambda _ { \mathrm { s h } } )   } \\ & {  \qquad + ( 1 + \cos \bar { t } ) \sin ( \omega ) ( - \mathcal { Q } - L - \lambda _ { \mathrm { s h } } ) \}  } \\ & {  \qquad \vdots ( 1 - \cos \bar { t } ) [ ( 1 - \cos \bar { t } ) \sin ( \omega - \mathcal { Q } - L + \lambda _ { \mathrm { s h } } )   } \\ & {   \qquad + ( 1 + \cos \bar { t } ) \sin ( \omega - \mathcal { Q } + L + \lambda _ { \mathrm { s h } } ) ]  } \\ & {  \qquad - 4 \sin [ \bar { t } ] \cos ( \omega + \mathcal { Q } ) \sin L \sin [ \bar { t } ] \} . } \end{array}
$$

事实上,若 $\lambda _ { m } = 0 , A ^ { \ast }$ 和 $B ^ { \ast }$ 就是第九章中(9.16)式表达的 $\pmb { A }$ 和 $B$ ·

将cosy代人(10.9）式得

$$
\rho { = } \rho _ { \geqslant _ { 0 } } ( 1 + F ^ { * } A ^ { * } \cos f \cdot F ^ { * } B ^ { * } \sin f ) \exp \biggl [ { - \frac { 1 } { H } ( r { - } \sigma ) } \biggr ] .
$$

类似对扁球大气的处理，上式即可化为

$$
\begin{array} { r l r } {  { \rho = k \bigg \{ \bigg ( 1 + \frac { C ^ { 2 } } { 4 } \bigg ) + C \cos 2 \omega \big ( - e \cos E + \cos 2 E + e \cos 3 E \big ) } } \\ & { } & { + \mathrm { C } \sin 2 \omega ( e \sin E - \sin 2 E - e \sin 3 E ) } \\ & { } & { + \mathrm { \nabla } C ^ { 2 } \cos 4 \omega \bigg ( \frac { 1 } { 4 } \mathrm { \cos } 4 E \bigg ) \div \mathrm { \nabla } C ^ { 2 } \sin 4 \omega \bigg ( - \frac { 1 } { 4 } \mathrm { \sin } 4 E \bigg ) } \\ & { } & { + \Delta ( F ^ { * } ) \mathrm { \nabla } _ { \big \{ } } ^ { \dagger } \exp \bigg ( \frac { \mathcal { U } \mathcal { C } } { H } \cos 8 \bigg ) . \quad \qquad ( 1  \end{array}
$$

其中 $k$ 仍旧是前面(10.39)式给出的量， $\Delta ( F ^ { \ast } )$ 是周日变化项，由下式表达：

$$
\begin{array} { r l } & { \quad + C \cos 2 \cos 1 - \frac { 1 } { 3 } + \frac { 1 } { 2 } - \frac { \cos 2 \cos 2 - 1 } { 2 } \cos 2 \mathrm { s } + \frac { 2 } { 3 } - \frac { \sin 2 \mathrm { s } } { 2 } + \frac { \cos 2 \mathrm { s } } { 2 } + } \\ & { \quad \frac { 2 } { 4 } \mathrm { e } ^ { \mathrm { i } \omega \mathrm { s } + 4 \Delta } \Big \{ + C \sin 2 \mathrm { e } \Big [ - \frac { 1 } { 2 } \frac { \sin \mathrm { i } B } { \sin { B } \cdot 1 } \cdot \frac { \epsilon } { 2 } \frac { \sin 2 B - 1 } { 2 } - \frac { 1 } { 2 } \sin 3 B \Big ] } \\ & { \quad - \frac { 3 } { 4 } \mathrm { e } ^ { \mathrm { i } \omega \mathrm { s } + \sin 4 \mathrm { f } } \Big \} + C ^ { \mathrm { t o } } \mathrm { e s } \mathrm { s } + \omega \Big \{ \frac { 1 } { 8 } \cdot \big ( \sin ^ { \mathrm { s } + 2 B + \cos 3 B \big ) } \Big ] } \\ & { \quad + C ^ { \mathrm { s } } \mathrm { s } \mathrm { i n } 4 \omega \Big \{ - \frac { 1 } { 8 } ( \sin 3 B + \sin 5 B \sin ) \Big \} } \\ &  \quad + P ^ { \mathrm { s } } \mathrm { i n } 4 \omega \Big \{ - \frac { 1 } { 8 } \frac { 1 } { 9 } + \frac { \sin ^ { \mathrm { s } } } { 2 } \Big \} \mathrm { s } \mathrm { i n } 2 \mathrm { E } + \frac { \mathrm { e } ^ { \mathrm { i } \omega ^ { 2 } } \mathrm { s } \mathrm { i n } 3 B \mathrm { f } } \\ &  \quad + C \sin 2 \mathrm { e } ^ { \mathrm { i } \omega \mathrm { s } } - \frac { 1 } { 2 } \sin B \cdot \mathrm { e s i n } 2 B + \frac { 1 } { 2 } \sin 2 B + \frac { \mathrm { e } ^ { \mathrm { i } \omega ^ { 2 } } \mathrm { s i n } 3 B \Big \} } \\ &  \quad + C \cos 2 \mathrm { e } ^ { \mathrm { i } \omega \mathrm { s } } - \frac { 1 } { 2 } \sin B \cdot \mathrm { e s i n } 2 B + \frac { 1 } { 2 } \sin 3 B + \frac { 3 } { 4 } \mathrm { e s i n } 4 B \Big \} \\ &  \quad + C \sin 2 \mathrm { e } ^ { \mathrm { i } \omega \mathrm { s } } \frac { 1 } { 4 } - \frac { 1 } { 2 } \cos B - \mathrm { e x i n } 2 B - \frac { 1 } { 2 } \end{array}
$$

$$
\begin{array} { l } { { \displaystyle + C ^ { 2 } \cos \ell \omega \Big [ - \frac { 1 } { 8 } \Big ( \sin 3 E - \sin 5 E \Big ) \Big ] } } \\ { { \displaystyle + C ^ { 2 } \sin 4 \omega \Big [ - \frac { 1 } { 8 } ( \cos 3 E - \cos 5 E ) \Big ] \Big \} . } } \end{array}
$$

以上密度公式中略去的项与扁球大气(10.38)式一致，不再写出.

(4）同时考虑密度标高变化和周日变化的扁球大气根据(10.6)式对 $H ( r )$ 的假定，考虑到(10.7)式，密度公式(10.9）式可进一步写成

$$
\begin{array} { r } { \rho = \rho _ { p _ { 0 } } ( 1 + F ^ { * } A ^ { * } \cos f + F ^ { * } B ^ { * } \sin f ) \left[ 1 + \frac { \mu } { 2 } \Big ( \frac { r - \sigma } { H _ { p _ { 0 } } } \Big ) ^ { 2 } \right] } \\ { \exp \biggl ( - \frac { r - \sigma } { H _ { p _ { 0 } } } \biggr ) \qquad ( \frac { r } { H _ { p _ { 0 } } } \biggr ) } \end{array}
$$

由于大气密度随高度按指数规律减小，当偏心率不太小时，阻力摄动效应主要表现在近地点附近．因此,尽管 $( r - \sigma )$ 较大时， $( r -$ $\sigma ) / H _ { p _ { 0 } }$ 并非小量，但此时相应的大气密度很小，阻力效应变弱.故从大气阻力摄动的效果来看，这一表达式的近似处理仍是合理的·下面将进一步化成根数形式，由(10.34)式可知

$$
\frac { r - \sigma } { H _ { p _ { 0 } } } { = } \frac { r - r _ { p _ { 0 } } } { H _ { p _ { 0 } } } { - } C \cos 2 ( f + \omega ) + C \cos 2 \omega _ { 0 } ,
$$

这里 $C$ 与(10.36)式给出的 $\pmb { C }$ 基本一致,只是相应的 $\pmb { H }$ 改为 $H _ { p _ { 0 } \cdot }$ 于是

$$
\begin{array} { c l c r } { \displaystyle \frac { \mu } { 2 } \bigg ( \frac { r - \sigma } { H _ { p _ { 0 } } } \bigg ) ^ { 2 } = \frac { \mu } { 2 } \bigg ( \frac { r - r _ { p _ { 0 } } } { H _ { p _ { 0 } } } \bigg ) ^ { 2 } - \mu C \bigg ( \frac { r - r _ { p _ { 0 } } } { H _ { p _ { 0 } } } \bigg ) [ \cos 2 ( E + \omega ) } \\ { \displaystyle - \cos 2 \omega _ { 0 } ] + O ( \mu C ^ { 2 } , \mu C e ) , } \end{array}
$$

同样可利用 $r { = } a ( 1 { - } e \cos E )$ 将该式化为

$$
\begin{array} { r l r } & { } & { \dot { \overline { { r _ { p _ { 0 } } } } } \bigg ) ^ { 2 } = \dot { \mu } \left[ \left( \frac { z _ { 0 } ^ { 2 } } { 2 } + \frac { z ^ { 2 } } { 4 } + C z _ { 0 } \cos 2 \omega _ { 0 } \right) - ( z _ { 0 } z + C z \cos 2 \omega _ { 0 } ) \cdot \right. } \\ & { } & { \left. \cos { E } + \frac { z ^ { 2 } } { 4 } \cos 2 E \right] + \mu C \left[ \cos 2 \omega \left( \frac { z } { 2 } \cos E - z _ { 0 } \cos 2 E \right. \right. } \end{array}
$$

$$
\begin{array} { r l } & { \frac { 1 } { 2 } \cdots + \frac { z } { 2 } \cos 3 E \ \biggr ) + \sin 2 \omega \biggl ( - \frac { z } { 2 } \sin E + z _ { 0 } \sin 2 E \ } \\ & { - \frac { z } { 2 } \sin 3 E \ \biggr ) \biggr ] } \end{array}
$$

$$
z = \frac { a e } { H _ { p _ { 0 } } } , \qquad z _ { 0 } = \frac { a _ { 0 } e _ { 0 } } { H _ { p _ { 0 } } } , \qquad \left\{ \begin{array} { l l } { \begin{array} { r l r l r l } \end{array} } \end{array} \right.
$$

将此式代入(10.48)式，并利用(10.46)和(10.47)式两结果，就可以给出同时考虑密度标高变化和周日变化的扁球大气密度表达式,即

$$
\begin{array} { r l r } {  { \rho = k \Big \{ \bigg ( 1 + \frac { C ^ { 2 } } { 4 } \bigg ) + C \cos 2 \omega \big ( - e \cos \bar { E } + \cos 2 \bar { E } - \rho \cos 3 \bar { E } \big ) } } \\ & { } & { + C \sin 2 \omega \big ( e \sin \bar { E } - \sin 2 \bar { E } + e \sin 3 \bar { E } \big ) } \\ & { } & { + C ^ { 2 } \cos 4 \omega ( \frac { 1 } { 4 } \mathrm { c o s } 4 \bar { E } { \it \Delta \phi } ) + C ^ { 2 } \sin 4 \omega ( - \frac { 1 } { 4 } \sin 4 \bar { E } { \it \Delta \phi } ) } \\ & { } & \\ & { } & { + \Delta ( F ^ { * } ) + \Delta ( \mu ) \bigg \} \exp \big ( z \cos \bar { E } ) , } & { ( 1 6 \pi ^ { 2 } ) } \end{array}
$$

这里△(F\*)仍为周日变化项,而△(μ)为密度标高变化项，由于大气的一些参数难以定准，而C=0.1,μ二0.1,e<0.2,因此，在一般情况下,密度表达式中只要取到O(e,C,μ)项就够了.在此情况下，对于200km以上的高空,Hp。≥10-²，a和e的变化也不太大，可取z=zo,其差别与μ相当.于是密度公式(10.51)最后可以简化成下列形式：

$$
\begin{array} { r l r } { \rho } & { { } } & { \rho = k \big \{ 1 + C \cos 2 \omega \cos 2 E - C \sin 2 \omega \sin 2 E } \\ { \quad } & { { } } & { + \Delta ( F ^ { * } ) + \Delta ( \mu ) \big \} \exp ( z \cos { E } ) , } \end{array}
$$

其中

$$
\begin{array} { r l } & { k = \rho _ { p _ { 0 } } \exp \Biggl [ - \frac { 1 } { H _ { p _ { 0 } } } ( a - a _ { 0 } + a _ { 0 } e _ { 0 } ) - C \cos 2 \omega _ { 0 } \Biggr ] , } \\ & { \cdot \ C = \frac { 1 } { 2 \ H _ { p _ { 0 } } } r _ { p _ { 0 } } \sin ^ { 2 } i \ , } \end{array}
$$

$$
\begin{array} { r l } &  \begin{array} { r l } & { \Lambda ( ( B ^ { * } ) + \Delta ( B ( p ) - p )  \frac { \hat { \sigma } } { 2 } \frac { \hat { \sigma } ^ { 2 } } { \hat { \sigma } ^ { 4 } } - \partial _ { 0 } ^ { 2 } \hat { \sigma }  { s } = K + \frac { 1 } { 4 } \frac { \hat { \sigma } } { 2 } \frac { \hat { \sigma } } { 4 } \frac { \hat { \sigma } \hat { \sigma } \cdot \cos 2 B } { \hat { \sigma } ^ { 2 } } \Biggr \} } \\ & { \qquad + F ^ { N } \cdot [ - ( \frac { \hat { \sigma } } { 2 } \frac { \hat { \sigma } } { 2 } \frac { \hat { \sigma } ^ { 2 } } { \hat { \sigma } ^ { 4 } } ) - ( 1 + \frac { \hat { \sigma } } { 2 } \frac { \hat { \sigma } \cos 2 B } { \hat { \sigma } ^ { 4 } } ) ] \cos { \mathbb B } } \\ & { \qquad \quad  } \\ & { \qquad \quad  } \\ & { \qquad \quad  } \\ & { \qquad \frac { \hat { \sigma } } { 2 } \frac { \hat { \sigma } } { 2 } \frac { \hat { \sigma } ^ { 4 } } { \hat { \sigma } ^ { 2 } } \big ( \cos 2 \hat { \sigma } \big ( \cos 2 B ^ { * } \big ) \cos 2 B ^ { * } \big ) ( \frac { 1 } { \hat { \sigma } } \sin \hat { \sigma } \big ) \cos { \mathbb B } } \\ & { \qquad \quad  } \\ & { \qquad \quad  } \\ & { \qquad \quad \textstyle } \\ &  + \frac { \hat { \sigma } } { 2 } \frac { \hat { \sigma } \cdot \cos 2 \hat { \sigma } \cos \hat { \sigma } \big ( \cos 2 B ^ { * } \cos 2 B ^ { * } \big ) \big ) \cdot \ \hat { \sigma } ^ { 2 } \frac { \hat { \sigma } } { 4 } \sin 2 \hat { \sigma } \big ( - \sin \hat { \sigma } - \sin \hat { \sigma } \cos 3 B ^ { * } \big ) ] } \\ & { \qquad \quad  } \\ & { \quad  } \\ &  \quad \quad + \hat { \sigma } ^ { 2 } \frac { \hat { \sigma } \cdot \sin \hat { \sigma } \cdot \cos 2 B ^ { * } \sin 2 B } { \hat { \sigma } ^ { 4 } } \big ( \frac { \hat { \sigma } } { 2 } - \frac { \hat { \sigma } } { 2 } \frac { \hat { \sigma } } { \hat { \sigma } ^ { 4 } } \big ) \ \end{array} \end{array}
$$

大气密度表达式（10.52)式反映了大气的主要变化，球形大气、扁球大气等是该式的特例.但必须指出，根数形式的密度公式（10.52)是原(10.9）式的一个简化，其目的是为了便于讨论大气阻力摄动的性质和各种参数的作用，如果要在(10.9)式基础上求精确解，那么可在数值方法中直接采用(10.9)式．下面就用（10.52)式来求大气阻力摄动解，从而给出各种因素对应的摄动效应，以及大气阻力摄动的基本特征.

# 10.4 大气阻力摄动解

在具体构造大气阻力摄动解时，必须了解相应的阻力加速度的量级.根据(10.3)式，有

$$
\frac { D } { F _ { 0 } } { = } \frac { \displaystyle \frac { 1 } { 2 } \biggl ( \frac { C _ { D } S } { m } \biggr ) \rho v ^ { 2 } } { \displaystyle 1 / r ^ { 2 } } { = } \biggl ( \frac { C _ { D } S } { m } \rho \biggr ) \biggl ( \frac { r ^ { 2 } v ^ { 2 } } { 2 } \biggr ) ,
$$

其中 $v ^ { 2 } { = } \frac { 2 } { r } { - } \frac { 1 } { a } ,$ 则

$$
\frac { D } { F _ { 0 } } { \simeq } \Big ( \frac { C _ { D } S } { m } \rho \Big ) \frac { r } { 2 } .
$$

根据实际情况，一般卫星和气球卫星的面质比 $s / m$ 分别在下述范围内：

$$
\begin{array} { l } { { \displaystyle \frac { \delta } { m } = 2 - 2 0 ~ \mathrm { m ^ { 2 } / T } , } } \\ { { \displaystyle \frac { \delta } { m } = 3 0 0 0 - 1 0 0 0 0 \mathrm { m ^ { 2 } / T } . } } \end{array}
$$

前者相当于一个直径为 $\mathbf { 1 . 5 - 5 \ m } .$ 重 ${ \bf 1 ^ { \alpha } T }$ 的球，后者相当于一个直径为60—110m、重 $\mathbf { 1 \ T }$ 的球.若采用第一章给出计算单位，上述比分别为

$$
\begin{array} { l } { \displaystyle \frac { \delta } { m } = \left( 3 - 3 0 \right) \times 1 0 ^ { 8 } \approx 1 0 ^ { 9 } , } \\ { \displaystyle \frac { \delta } { m } = \left( 4 . 5 - 1 . 5 \right) \times 1 0 ^ { 1 1 } \simeq 1 0 ^ { 1 2 } . } \end{array}
$$

在 $2 0 0 ~ \mathrm { k m }$ 高度处，大气密度 $\rho { \approx } 3 \times 1 0 ^ { - 1 0 } \mathrm { k g / m ^ { 3 } } { = } 1 0 ^ { - 1 4 }$ ，对于一般卫星，若在这一高度飞行，相应地有

$$
\frac { D } { { \cal F } _ { \circ } } { = } 1 0 ^ { - 6 } { - } 1 0 ^ { - 5 } .
$$

通常飞行高度在 $2 0 0 ~ \mathrm { k m }$ 以上,上述比不大于 $1 0 ^ { - 8 }$ ，因此，在一般情况下，总是把大气阻力摄动当作二阶小量来处理。

这里必须说明一点，估计大气阻力摄动量级时,对偏心率e较小的情况，只要用近地点处的数据就可以了，但对 $\pmb { e }$ 较大的情况,要看平均效应，这是因为大气密度 $\pmb { \rho }$ 随高度按指数规律下降，只有近地点附近阻力才起作用，而远地点处的大气密度比近地点处的小得多，因此在大 $^ { e }$ 情况下,应取卫星运动一圈所对应的平均大气密度来估计摄动量级.

根据上述量级估计的结果，以及有关大气和大气阻力的一些参数不够准确,对于一阶解,前面的各种简化显然是合理的，用简-化后的基本方程（包括密度 $\rho$ 的表达式)来讨论大气阻力摄动，不仅可以给出大气和大气阻力的有关参数与卫星轨道变化之间的关系，而且在上述近似下构造出的摄动解，也能满足一定的精度要求.

# 1．右函数的转换

为了引用平均法或一般变换方法,需将基本方程(10.27)的右函数分解成长期项和周期项.为此,仿照第九章的处理方法，将基本方程 $d \sigma / d t$ 的形式(注意，这里的 $\pmb { \sigma }$ 是指卫星的六个轨道根数)变为dg/aE的形式，即根据dg/dE=/ 给出 $d \sigma / d E$ .这仅仅是为了便于求平均值,因此 $d E / d t$ 可引用无摄运动的表达式。根据这一考虑,再利用

$$
\begin{array} { r } { r \cos f = a \left( \cos E - e \right) , \quad r \sin f = a \sqrt { 1 - e ^ { 2 } } \sin E , } \\ { r = a \left( 1 - e \cos E \right) , \qquad } \end{array}
$$

就可将方程(10.27)化成 ${ d \sigma } / { d E }$ 的形式,取到 $O ( e )$ 项为

$$
\left. \begin{array} { l } { { \displaystyle \frac { d { \cal { a } } } { d E } = - A _ { 1 } a ^ { 2 } ( 1 + 2 e \cos E ) \rho , } } \\ { { \displaystyle \frac { d e } { d E } = - A _ { 1 } a \left( \frac { e } { 2 } + \cos E + \frac { e } { 2 } \cos 2 E \right) \rho , } } \\ { { \displaystyle \frac { d { \cal { i } } } { d E } = - \frac { A _ { 2 } a } { 4 n } \sin \mathrm { i } \left[ ( 1 - 2 e \cos E ) + \cos 2 \omega ( - 2 e \cos E ) \right] } } \\ { { ~ + \cos 2 E ) + \sin 2 \omega ( 2 e \sin E - \sin 2 E ) ] \rho , } } \end{array} \right\}
$$

$$
\frac { d \mathcal { Q } } { d E } { = } { - } \frac { A _ { 2 } a } { 4 n } \big [ \cos 2 \omega ( - 2 e \sin E + \sin 2 E ) \big . \qquad \quad
$$

$$
\frac { d \mathcal { M } } { d E } { = } A _ { 1 } a [ \frac { 1 } { e } \bigg ( 1 + \frac { 1 } { 8 } e ^ { 2 } \bigg ) \sin E + \frac { 1 } { 2 } \sin 2 E + \frac { 1 } { 8 } e \sin 3 E ^ { 2 } ] \rho .
$$

原方程 $d . M / d t$ 右端的零阶项 $\pmb { \mathscr { n } }$ 在 $d M / d E$ 中未写出，因讨论过程中暂不涉及到该项.以密度模式(10.52)式代入上述方程得

$$
\frac { d a } { d E } = \dot { - B _ { 1 } } a ^ { 2 } \bigg \{ ( 1 + 2 e \cos \mathcal { B } ) + C \cos 2 \omega \cos 2 \mathcal { B } +
$$

$$
\begin{array} { r l } & { \quad + \mu \left( \frac { 3 } { 4 } z _ { 0 } ^ { 2 } - z _ { 0 } ^ { 2 } \cos { g } \cdot \frac { 1 } { 4 } z _ { 0 } ^ { 2 } \cos { 2 E } \right) } \\ & { \quad + F ^ { \ast } A ^ { \ast } \Bigg [ \left( \frac { e } { 2 } - \frac { \mu } { 2 } z _ { 0 } ^ { 2 } \right) + \left( 1 + \frac { 7 } { 8 } \mu z _ { 0 } ^ { 2 } \right) \cos { E } } \\ & { \quad + \left( \frac { 3 } { 2 } e - \frac { 1 } { 2 } \mu z _ { 0 } ^ { 2 } \right) \cos { 2 E } + \frac { \mu } { 8 } z _ { 0 } ^ { 2 } \cos { 3 E } } \\ & { \quad + \frac { C } { 2 } \cos { 2 \omega } ( \cos { E } + \cos { 3 E } ) \Bigg ] } \\ & { \quad + F ^ { \ast } B ^ { \ast } \Bigg [ \frac { C } { 2 } \sin { 2 \omega } ( - \cos { E } + \cos { 3 E } ) \Bigg ) \Bigg ] \exp ( z \cos { E } ) , } \end{array}
$$

$$
\begin{array} { r l } & { \langle \Psi , \xi | , } \\ { t = - B _ { 0 } \bigg \{ \bigg \} \Big \{ \frac { \xi } { 2 } , ~ 1  \theta , ~ \Big \} } \\ & { + \frac { \xi } { 2 } \cos { 2 \xi } ( \cos \theta - \cos \theta ) , ~ \frac { \theta } { 2 } \bigg ( - \mathrm { e } \frac { \xi } { 3 } \big ) - \frac { \xi } { 4 } \bigg \{ \frac { \xi } { 2 } , ~ \xi  \theta , }  \\ & { - \frac { \xi } { 3 } \mathrm { e } \mathrm { i } \alpha { 2 } \mathrm { e x t ~ } ^ { 2 } , } \\ { \quad } & { + \bigg \{ \frac { \xi } { 2 } , ~ \xi  \theta , ~ \Big \} \frac { 1 } { 4 } \mathrm { e } ^ { \frac { \xi } { 3 } } \mathrm { e x t } \bigg \{ - 1 + \xi \mathrm { e } ^ { \frac { \xi } { 3 } } \bigg \} \mathrm { e x t } \bigg \{ \bigg ( \frac { 1 } { 2 } - \frac { \xi } { 1 6 } \big ) \mathrm { e } \xi \bigg \} } \\ { \quad } &  + \bigg ( \frac { \xi } { 2 } - \frac { \xi } { 4 } \mu  \Big \} \\ & { + ( \frac { \xi } { 2 } - \frac { \xi } { 3 } ) \mathrm { e x t } \bigg \{ \cos \theta \mathrm { e } ^ { \prime } + ( \frac { 1 } { 2 } + \frac { \xi } { 2 } \mu  \frac { 1 } { 2 } ) \mathrm { e x t } \bigg \} } \\ { \quad } & { + ( \frac { \xi } { 2 } - \frac { \xi } { 3 } \mathrm { e x t } \alpha ) \mathrm { e x t } \bigg \{ \mathrm { e x t } ^ { 2 } + \mathrm { e x t } \beta \mathrm { e x t } \mathrm { e } \xi } \\ { \quad } & { + \frac { \xi } { 6 } \mathrm { e x t } \alpha \big ( \mathrm { e } - 2 \mathrm { e x t } 2 \mathrm { e x t } \mathrm { e x t } \big \{ \} } \\ { \quad } &  + \mathrm { e } ^ { \mathrm { i } \alpha } \mathrm { e x t } \big \{ \frac { \xi } { 6 } , ~ \xi  \mathrm { e } \xi \big \} \bigg \} \\ { \quad } & { + \mathrm { e } ^ { \mathrm { i } \alpha } \mathrm { e x t } \big \{ \frac { \xi } { 6 } , ~ \xi  \mathrm { i } \xi \big \} , } \end{array}
$$