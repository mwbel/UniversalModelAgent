# 7.6Zeipel方法

紫倍耳(Zeipel)方法[是针对保守系统(哈密顿系统）建立在用隐函数定义的正则变换基础上的一种变换方法，其特点是寻找一个特殊的生成函数 $\pmb { S } _ { i }$ 由其构造出一正则变换，使新哈密顿函数出现足够的循环坐标,从而获得该系统的解．具体地说，对于人造卫星的运动，若引用德洛纳变量作为基本变量，就是通过正则变换使相应的哈密顿函数分别消除 $l , \ q , \ h$ 这三个角坐标，消除 $l$ （这是快变量)，实质上就是分离出短周期项，而消除 $g , h$ （这两个是慢变量)就是分离出长周期项．消除这三个变量后，新系统中的轨道根数或由它们组成的德洛纳变量只具有长期变化，这相当于平均根数对应的一种哈密顿系统．尽管Zeipe1方法早在1916年就已提出，但对于大多数自然天体所构成的摄动系统，引用此方法并不方便，而人造卫星在地球形状等因素摄动下，引用此方法却十分简单.

下面结合地球引力位函数主要带谐项 $( J _ { 2 } )$ 的摄动来介绍Zei-pel.方法及其具体应用的完整过程，这样又可以和第五章的平均根数法作一比较。由于仅考虑带谐项时，相应的哈密顿函数不显含 $t$ ，为此，还要引用主要田谐项 $\pmb { J _ { 2 , 2 } }$ 来说明显含 $\pmb { t }$ 的问题如何处理.

采用德洛纳变量，在人卫工作的常用计算单位系统中 $\mu = 1 ,$ 有

$$
\left. \begin{array} { l l } { L = \sqrt { a } , } & { l = M , } \\ { G = \sqrt { a \left( 1 - e ^ { 2 } \right) } } & { g = \omega , } \\ { H = \sqrt { a \left( 1 - e ^ { 2 } \right) } \cos i , } & { h = \Omega . } \end{array} \right\}
$$

对上述带谐项摄动问题，相应的哈密顿函数为

$$
{ \cal F } = \frac { 1 } { 2 L ^ { 2 } } + R ,
$$

其中 $\pmb { R }$ 即 $\pmb { J } _ { 2 }$ 对应的摄动函数：

$$
\begin{array} { r l } & { R = \cfrac { J _ { 2 } } { 2 L ^ { 6 } } \left[ \Big ( - \frac { 1 } { 2 } + \frac { 3 } { 2 } \frac { H ^ { 2 } } { G ^ { 2 } } \Big ) \Big ( \frac { a } { r } \Big ) ^ { 3 } \right. } \\ & { \qquad \left. + \frac { 3 } { 2 } \Big ( 1 - \frac { H ^ { 2 } } { G ^ { 2 } } \Big ) \Big ( \frac { a } { r } \Big ) ^ { 3 } \cos 2 ( f + g ) \right] . } \end{array}
$$

前面已指出，由于哈密顿函数 $\pmb { F }$ 变了一个符号，相应的正则运动方程也变了一个符号，即(7.148)式：

$$
\left. \begin{array} { c } { { \displaystyle \frac { d L } { d t } { = } \frac { \partial F } { \partial l } , \frac { d l } { d t } { = } { - } \frac { \partial F } { \partial L } , } } \\ { { \displaystyle \frac { d G } { d t } { = } \frac { \partial F } { \partial g } , \frac { d g } { d t } { = } { - } \frac { \partial F } { \partial G } , } } \\ { { \displaystyle \frac { d H } { d t } { = } \frac { \partial F } { \partial h } , \frac { d h } { d t } { = } { - } \frac { \partial F } { \partial H } . } } \end{array} \right\}
$$

显然，该问题的哈密顿函数 $\pmb { F }$ 不仅不显含 $\pmb { \mathscr { t } }$ ，还有一个循环坐标 $h _ { i }$ ，对于这一问题，Zeipel变换的任务就是消除 $l$ 和 $\pmb { g }$ 为此，将哈密顿函数按小参数 $\pmb { \varepsilon }$ （即 $\pmb { J _ { 2 } } )$ 的幂以及不同的性质写成

$$
\pmb { F } { = } \pmb { F } _ { 0 } { + } \pmb { F } _ { 1 } ,
$$

$$
{ \cal F } _ { 0 } = \frac { 1 } { 2 L ^ { 2 } } ,
$$

$$
{ \cal F } _ { 1 } = { \cal F } _ { 1 o } ( L , G , H ) + { \cal F } _ { 1 s } ( L , G , H , l , g ) .
$$

其中 $\smash { \mathbf { F } _ { 1 } } _ { 0 }$ 和 ${ \pmb { F } } _ { 1 }$ 。分别表示一阶长期部分（不含任何角坐标）和一阶短周期部分（性质取决于 $\wr$ 的部分，即对时间 $\pmb { \mathrm { \acute { t } } }$ 或 $\pmb { l }$ 的平均值为零),而性质取决于角坐标 $g$ 和 $\pmb { h }$ 的项则称为长周期部分，将以下标 $^ { \ast } k l ^ { \ast } ( k { = } 1 , 2 , \cdots )$ 来表示，如 $F _ { 2 \ \downarrow ; } \ F _ { 3 \ l ; } \cdots , \ F _ { 1 \ 0 }$ 和 $\pmb { F } _ { 1 }$ 的具体形式为

$$
\overline { { { F } } } _ { 1 \circ } = \frac { J _ { 2 } } { 2 L ^ { 6 } } A ( L / G ) ^ { 3 } ,
$$

$$
F _ { 1 s } = \frac { J _ { 2 } } { 2 L ^ { 6 } } \Big \{ { \cal A } \bigg [ \bigg ( \frac { a } { r } \bigg ) ^ { 3 } - ( L / G ) ^ { 3 } \bigg ]
$$

$$
+ \ B \left( { \frac { a } { r } } \right) ^ { \ S } \cos 2 \left( f + g \right) \Big \} ,
$$

其中

$$
A = - { \frac { 1 } { 2 } } + { \frac { 3 } { 2 } } { \frac { H ^ { 2 } } { G ^ { 2 } } } , B = { \frac { 3 } { 2 } } \Bigl ( 1 { - } { \frac { H ^ { 2 } } { G ^ { 2 } } } \Bigr ) .
$$

下面分两步来消除 $\imath$ 和 $\pmb { \mathscr { g } }$ ：

# 1．第一次消除 $\downharpoonright$ 的变换—分离短周期项

为了消除l,Zeipel方法就是寻找这样的生成函数 $\pmb { S } = \pmb { S } ( \pmb { L } ^ { \prime } )$ $G ^ { \prime } , H ^ { \prime } , l , g , h , t )$ ，即7.5给出的生成函数的第四种形式： $\mathbb { S } ( q ,$ $u , t )$ ，由此构造的正则变换为

$$
\pmb { \imath } = \frac { \partial S } { \hat { c } q } , \pmb { \imath } = \frac { \partial S } { \partial u } ,
$$

其中

$$
\begin{array} { r } { p = \left( \begin{array} { l } { L } \\ { G } \\ { H } \end{array} \right) , q = \left( \begin{array} { l } { l } \\ { g } \\ { h } \end{array} \right) , \boldsymbol { u } = \left( \begin{array} { l } { L ^ { \prime } } \\ { G ^ { \prime } } \\ { H ^ { \prime } } \end{array} \right) , \boldsymbol { v } = \left( \begin{array} { l } { l ^ { \prime } } \\ { g ^ { \prime } } \\ { h ^ { \prime } } \end{array} \right) } \end{array}
$$

变换的余函数是 $S _ { i }$ ，但由于哈密顿函数的符号和正则运动方程已变了一个符号，故新哈密顿函数为

$$
\pmb { F } ^ { * } { = } \pmb { F } { - } \pmb { S } _ { t } .
$$

讨论 $\pmb { J _ { 2 } }$ 项摄动时， $\pmb { F }$ 不显含 $\mathbf { \boldsymbol { t } } , \mathbf { \boldsymbol { S } } _ { t } = 0 ;$ 问题将归结为寻找

$$
\begin{array} { r l } & { S \mathrm { = } S \left( L ^ { \prime } , G ^ { \prime } , H ^ { \prime } , l , g , h \right) \mathrm { = } S _ { 0 } \mathrm { + } S _ { 1 } \mathrm { + } \cdots + S _ { j } \mathrm { + } \cdots , } \\ & { S _ { j } \mathrm { = } O \left( \varepsilon ^ { j } \right) , } \end{array}
$$

使新哈密顿函数 $\pmb { F } ^ { \star }$ 满足

$$
\left. \begin{array} { c } { { F ^ { * } { = } \displaystyle { \sum _ { j = 0 } ^ { k } } F _ { j } ^ { * } \left( L ^ { \prime } , G ^ { \prime } , H ^ { \prime } , g ^ { \prime } \right) } } \\ { { { } } } \\ { { { + } \displaystyle { \sum _ { j > i \neq 1 } ^ { } } F _ { j } ^ { * } \left( L ^ { \prime } , G ^ { \prime } , H ^ { \prime } , l ^ { \prime } , g ^ { \prime } \right) , } } \\ { { F _ { j } ^ { * } { = } O ( \varepsilon ^ { j } ) . } } \end{array} \right\}
$$

$\pmb { k }$ 是正整数，其值视问题的需要而定。对于一阶解， $k = 2 .$

显然， $\pmb { \ S _ { 0 } }$ 对应无摄部分，应为恒等变换,即

$$
\begin{array} { r } { S _ { 0 } { = } L ^ { \prime } l + G ^ { \prime } g + { H ^ { \prime } } h . } \end{array}
$$

而 $\pmb { F }$ 又不含 ${ \pmb h } _ { \pmb { \nu } }$ 故可以假定

$$
\mathcal { S } _ { j } = \mathcal { S } _ { j } ( L ^ { \prime } , G ^ { \prime } , H ^ { \prime } , l , g ) , j = 1 , 2 , \cdots .
$$

相应的正则变换为

$$
\left. \begin{array} { c } { { L = L ^ { \prime } + \displaystyle \frac { \partial S _ { 1 } } { \partial l } + \displaystyle \frac { \partial S _ { 2 } } { \partial l } + \cdots , ~ l ^ { \prime } = l + \displaystyle \frac { \partial S _ { 1 } } { \partial L ^ { \prime } } + \displaystyle \frac { \partial S _ { 2 } } { \partial L ^ { \prime } } + \cdots , } } \\ { { { } } } \\ { { G = G ^ { \prime } + \displaystyle \frac { \partial S _ { 1 } } { \partial g } + \displaystyle \frac { \partial S _ { 2 } } { \partial g } + \cdots , ~ g ^ { \prime } = g + \displaystyle \frac { \partial S _ { 1 } } { \partial G ^ { \prime } } + \displaystyle \frac { \partial S _ { 2 } } { \partial G ^ { \prime } } + \cdots , } } \\ { { { } } } \\ { { H = H ^ { \prime } , } } \end{array} \right\}
$$

如何寻找满足上述条件的 $\delta ( L ^ { \prime } , G ^ { \prime } , H ^ { \prime } , l , g , h )$ ，即 $S _ { 1 } , S _ { 2 } , \cdots _ { n }$ 显然，应从下列关系中来确定以混合变量表达的 $\pmb { \mathscr { S } } _ { i }$ 即

$$
\begin{array} { l } { { { \displaystyle F ^ { * } = F ( L ( L ^ { \prime } , G ^ { \prime } , H ^ { \prime } , l , g ) , G ( L ^ { \prime } , G ^ { \prime } , H ^ { \prime } , l , g ) , H = H ^ { \prime } , l , g ) } } } \\  { { \displaystyle \quad = \sum _ { j = 0 } ^ { k } F _ { j } ^ { * } ( L ^ { \prime } , G ^ { \prime } , H ^ { \prime } , g ) + \sum _ { j > k + 1 } F _ { j } ^ { * } ( L ^ { \prime } , G ^ { \prime } , H ^ { \prime } , l , g ) . } } \end{array}
$$

按 $\pmb { \varepsilon } = \pmb { J } _ { 2 }$ 的幂对 $L ^ { \prime } , G ^ { \prime } , H ^ { \prime }$ 展开得

$$
 \begin{array} { r l } & { \gamma \cdot n : n : \sigma , \ \sigma , \ \cdots \ \gamma \cdot n : \sigma } \\ &  \qquad \ F _ { 4 } ^ { ( 1 ) } - F _ { 4 } ^ { ( 2 ) } \ \cdot \mathbf { - } \mathbf { + } \mathbf { - } \mathbf { + } \mathbf { - } \mathbf { - } \mathbf { + } \mathbf { - } \mathbf { - } \mathbf { + } \mathbf { - } \mathbf { - } \mathbf { } \mathbf { - } \mathbf { + } \mathbf { - } \mathbf { } \mathbf { - } \mathbf { } \mathbf { - } \mathbf { } \mathbf { - } \mathbf { } \mathbf { + } \mathbf { - } \mathbf { } \mathbf { - } \mathbf { } \mathbf { - } \mathbf { } \mathbf { - } \mathbf { } \mathbf { - } \mathbf { } \mathbf { - } \mathbf { } \mathbf { - } \mathbf { } \mathbf { - } \mathbf { } \mathbf { - } \mathbf { } \mathbf { - } \mathbf { } \mathbf { - } \mathbf { } \mathbf { - } \mathbf { } \mathbf { - } \mathbf { } \mathbf { - } \mathbf { } \mathbf { - } \mathbf { } \mathbf { - } \mathbf { } \mathbf { - } \mathbf { } \mathbf { - } \mathbf { } \mathbf { - } \mathbf { } \mathbf { - } \mathbf { } \mathbf { - } \mathbf { } \mathbf { - } \mathbf { } \mathbf { - } \mathbf { } \mathbf { - } \mathbf { } \mathbf { - } \mathbf { } \mathbf { - } \mathbf { } \mathbf { - } \mathbf { } \mathbf { - } \mathbf { } \mathbf { - } \mathbf { } \mathbf { - } \mathbf { } \mathbf { - } \mathbf { } \mathbf { - } \mathbf { } \mathbf { - } \mathbf { } \mathbf { - } \mathbf { } \mathbf { - } \mathbf { } \mathbf { - } \mathbf { } \mathbf { - } \mathbf { } \mathbf { - } \mathbf { } \mathbf { - } \mathbf { } \mathbf { - } \mathbf { } \mathbf { - } \mathbf { } \mathbf { - } \mathbf { } \mathbf { - } \mathbf { } \mathbf { - } \mathbf { } \mathbf { - } \mathbf { } \mathbf { - } \mathbf { } \mathbf { - } \mathbf { } \mathbf { - } \mathbf { } \mathbf { - } \mathbf { } \mathbf { - } \mathbf { } \mathbf { - } \mathbf { } \mathbf { - } \mathbf { } \mathbf { - } \mathbf { } \mathbf { - } \mathbf { } \mathbf { - } \mathbf { } \mathbf { - } \mathbf { } \mathbf { - } \mathbf { } \mathbf { - } \mathbf { } \mathbf { - } \mathbf { } \mathbf { - } \mathbf { } \mathbf { - } \mathbf { } \mathbf { - } \mathbf { } \mathbf { - } \mathbf { } \mathbf  -  \end{array}
$$

其中 $\frac { \partial } { \partial L ^ { \prime } }$ 表示对L求偏导数后取L=L',其它表达形式类似，不再一一说明，该式各部分均已表达成L'，G',H',l,g的函数，因而由此确定的S当然是混合变量的函数，对于一阶解，只要F,F\*,F达到消除l的要求即行，比较（7.173）式两端J的同次幂，即得

$$
\begin{array} { r l } & { \boldsymbol { F } _ { 0 } ^ { * } = F _ { 0 } ( L ^ { \prime } ) , } \\ & { \boldsymbol { F } _ { 1 } ^ { * } = F _ { 1 } ( L ^ { \prime } , G ^ { \prime } , H ^ { \prime } , l , g ) + \frac { \partial F _ { 0 } \left( \frac { \partial S } { \partial L ^ { \prime } } \right) } { \partial L ^ { \prime } } , } \\ & { \boldsymbol { F } _ { 2 } ^ { * } = \frac { \partial F _ { 0 } \left( \frac { \partial S _ { 2 } } { \partial l } \right) } { \partial L ^ { \prime } } + \frac { 1 } { 2 } \frac { \frac { \partial ^ { 2 } } { \partial L ^ { \prime 2 } } \left( \frac { \mathcal { C } \cdot S _ { 1 } } { \partial l } \right) ^ { 2 } } { \partial L ^ { \prime 2 } } } \\ & { \qquad + \frac { \partial F _ { 1 } } { \partial L ^ { \prime } } \Big ( \frac { \partial S _ { 1 } } { \partial l } \Big ) + \frac { \partial F _ { 1 } } { \partial G ^ { \prime } } \Big ( \frac { \partial S _ { 1 } } { \partial g } \Big ) , } \end{array}
$$

于是由(7.160)式表达的 $\pmb { F _ { 0 } }$ 得

$$
{ { \cal F } } _ { 0 } = \frac { 1 } { 2 L ^ { \prime } { } ^ { 2 } } .
$$

关于一阶部分,由于S是待定的,故(7.175)式可分成两个部分：

$$
{ \cal F } _ { 1 } ^ { * } { = } { \cal F } _ { 1 \ \circ } ( L ^ { \prime } , G ^ { \prime } , H ^ { \prime } ) { = } \frac { J _ { 2 } } { { 2 } L ^ { ' 3 } G ^ { \prime } { : } ^ { 3 } } { \cal A } ^ { \prime } ,
$$

$$
0 { = } F _ { \mathrm { ~ 1 ~ } s } { + } \frac { { \partial } F _ { 0 } } { { \partial } L ^ { \prime } } \Big ( \frac { { \partial } S _ { 1 } } { { \partial } l } \Big ) .
$$

由(7.179)式即可确定 $\beta _ { 1 s }$ 即

$$
\begin{array} { r l r } {  { \frac { \partial \mathcal { S } _ { 1 } } { \partial l } \mathrm { = } - F _ { 1 \mathcal { S } } \Big / \frac { \partial F _ { 0 } } { \partial L ^ { \prime } } } } \\ & { } & { \mathrm { = } \frac { J _ { 2 } } { 2 L ^ { \prime 3 } } \Big \{ A ^ { \prime } \Big [ \Big ( \frac { a } { r } \Big ) ^ { \ast } - \Big ( \frac { L ^ { \prime } } { G ^ { \prime } } \Big ) ^ { \ast } \Big ] } \\ & { } & { \mathrm { ~ } + B ^ { \prime } \Big ( \frac { a } { r } \Big ) ^ { 3 } \cos 2 ( f ^ { \prime } + g ) \Big \} . } \end{array}
$$

上面各式中出现的A'，B'表示(7.164)式中的G，H均换为G',

$\pmb { H ^ { \prime } }$ ，而 $\left( { \frac { a } { r } } \right)$ 和 $f ^ { \prime }$ 通过 $e$ 包含的 $L , G$ 亦是如此，即

$$
e ^ { \prime } = \biggl [ 1 - \biggl ( \frac { G ^ { \prime } } { \tilde { L ^ { \prime } } } \biggr ) ^ { 2 } \biggr ] ^ { 1 / 2 } .
$$

由于(7.180)式是 $\pmb { \delta } _ { 1 }$ 对 $\pmb { \imath }$ 的偏导数，故积分该式时，各量之间的转换严格地满足二体问题的函数关系。积分得

$$
\begin{array} { l } { { \displaystyle { \mathcal { S } } _ { 1 } { = } \frac { J _ { 2 } } { 2 G ^ { \prime 3 } } \Big \{ A ^ { \prime } \big [ ( f ^ { \prime } - l ) + e ^ { \prime } \sin f ^ { \prime } \big ] } } \\ { { \displaystyle ~ + B ^ { \prime } \Big [ \frac { e ^ { \prime } } { 2 } \sin \big ( f ^ { \prime } + 2 g \big ) + \frac { 1 } { 2 } \sin 2 ( f ^ { \prime } + g ) } } \\ { { \displaystyle ~ + \frac { e ^ { \prime } } { 6 } \sin \big ( 3 f ^ { \prime } + 2 g \big ) \Big ] \Big \} . } } \end{array}
$$

同样可将二阶部分的(7.176)式分成两个部分，即

$$
\begin{array} { r l } & { { \cal F } _ { 2 } ^ { * } = \displaystyle \left\{ \frac { 1 } { 2 } \frac { \partial ^ { 2 } { \cal F } _ { 0 } } { \partial { \cal L } ^ { \prime 2 } } \Big ( \frac { \partial S _ { 1 } } { \partial L } \Big ) ^ { 2 } + \frac { \partial { \cal F } _ { 1 } } { \partial L ^ { \prime } } \Big ( \frac { \partial S _ { 1 } } { \partial \bar { l } } \Big ) + \frac { \partial { \cal F } _ { 1 } } { \partial G ^ { \prime } } \Big ( \frac { \partial S _ { 1 } } { \partial g } \Big ) \right\} _ { c _ { 0 } , 1 } , } \\ & { \displaystyle 0 = \frac { \partial { \cal F } _ { 0 } } { \partial { \cal L } ^ { \prime } } \Big ( \frac { \partial S _ { 2 } } { \partial l } \Big ) + \displaystyle \left\{ \frac { 1 } { 2 } \frac { \partial ^ { 2 } { \cal F } _ { 0 } } { \partial { \cal L } ^ { \prime 2 } } \Big ( \frac { \partial S _ { 1 } } { \partial \bar { l } } \Big ) ^ { 2 } + \frac { \partial { \cal F } _ { 1 } } { \partial { \cal L } ^ { \prime } } \Big ( \frac { \partial S _ { 1 } } { \partial \bar { l } } \Big ) \right. } \\ & { \quad \quad \quad \quad \left. + \frac { \partial { \cal F } _ { 1 } } { \partial G ^ { \prime } } \Big ( \frac { \partial S _ { 1 } } { \partial g } \Big ) \right\} _ { g } . } \end{array}
$$

两个等式右端的括号 $\{ \} _ { \infty }$ 和 $\{ \} _ { \beta }$ 分别表示括号内各项的不含$\mathbf { \Omega } _ { \cdot }$ 的部分和含 $\imath$ 的部分．后一式就用来确定 $\pmb { \ S } _ { 2 }$ ，对于一阶解无需讨论它．要由(7.182)式推出 $\pmb { F _ { 2 } ^ { * } }$ 的具体表达式，即消除该式右端括号{}内含 $\iota$ 的项，这实际上就是分离出短周期项，因此只要引用第二章给出的对卫星运动(平近点角 $\iota$ 从 $l _ { 0 }$ 变到 $l _ { 0 } + 2 \pi )$ 求平均值即可，经计算得

$$
\begin{array} { c } { { { \frac { 1 } { 2 } } { \frac { \partial ^ { 2 } F _ { 0 } } { \partial L ^ { \prime 2 } } } \displaystyle \biggl ( { \frac { \partial S _ { 1 } } { \partial l } } \biggr ) ^ { 2 } = { \frac { 3 J _ { 2 } ^ { 2 } } { 2 L ^ { \prime 1 0 } } } \biggl \{ \biggl [ { \frac { 1 } { 4 } } { \cal A } ^ { \prime 2 } + { \frac { 9 } { 3 2 } } \biggl ( 1 - { \frac { { \cal H } ^ { \prime 2 } } { { \cal G } ^ { \prime 2 } } } \biggr ) ^ { 2 } \biggr ] \cdot } } \\ { { \cdot \biggr . } } \\ { { \times \biggr ( 1 + 3 e ^ { \prime 2 } + { \frac { 3 } { 8 } } e ^ { \prime 4 } \biggr ) ( 1 - e ^ { \prime 2 } ) ^ { - 8 / 2 } } } \\ { { \nonumber } } \\ { { \displaystyle \qquad - { \frac { 1 } { 4 } } { \cal A } ^ { \prime 2 } ( 1 - e ^ { \prime 2 } ) ^ { - 3 } + { \frac { 9 } { 8 } } { \cal A } ^ { \prime } \biggl ( 1 - { \frac { { \cal H } ^ { \prime 2 } } { { \cal G } ^ { \prime 2 } } } \biggr ) ^ { \bullet } } } \end{array}
$$

$$
\begin{array} { r l } & { \left( 1 + \frac { 1 } { 8 } e ^ { - 2 \tau } \right) ^ { 2 \nu \alpha _ { 1 } ( 1 - e ^ { - 2 \tau } ) - 3 \nu \alpha _ { 1 } \alpha _ { 2 } \nu _ { 1 } } } \\ & { \qquad \quad \cdot \ \frac { \lambda _ { 1 } } { 8 } \sum _ { i = 1 } ^ { \infty } \Big ( \frac { 1 } { \lambda _ { 1 } ( 1 - e ^ { - 2 \tau } ) } \Big ) ^ { 2 \nu _ { 1 } ( 1 - e ^ { \alpha _ { 1 } \nu _ { 1 } } ) - 3 \nu _ { 1 } ( 1 - e ^ { \alpha _ { 1 } \nu _ { 1 } } ) } \Big \} , } \\ & { \frac { 1 } { 8 } e ^ { - 2 \tau } \Big ( \frac { 3 \tau } { 2 } \Big ) ^ { 2 \nu _ { 1 } ( 1 - e ^ { - 2 \tau } ) } \frac { \big ( \lambda _ { 1 } e ^ { - 2 \tau } \big ) } { \lambda _ { 1 } ( 1 - e ^ { - 2 \tau } ) } } \\ & { \frac { 1 } { 8 } \Big ( \frac { 1 } { 2 \tau } \Big ) ^ { 2 \nu _ { 1 } ( 1 - e ^ { - 2 \tau } ) } \frac { \big ( \lambda _ { 1 } e ^ { - 2 \tau } \big ) } { \lambda _ { 1 } ( 1 - e ^ { - 2 \tau } ) } \Big ( \frac { 3 } { 8 } e ^ { - 2 \tau } - \frac { 2 7 \nu _ { 1 } e ^ { - \alpha _ { 1 } \nu _ { 1 } } } { 1 6 } \Big ) \cdot } \\ & { \qquad \quad - \frac { 1 } { 4 \tau ^ { 2 \nu _ { 1 } } ( 1 - e ^ { - 2 \tau } ) } \frac { \big ( \lambda _ { 1 } e ^ { - 2 \tau } \big ) } { 1 6 } \Big ( 1 - e ^ { - \alpha _ { 1 } \nu _ { 1 } ( 1 - e ^ { \alpha _ { 1 } \nu _ { 1 } } ) } \Big ) \cdot } \\ & { \qquad \quad \times ( 1 - e ^ { - 2 \tau } ) ^ { 3 \nu _ { 1 } ( 1 - e ^ { - 2 \tau } ) - 3 \tau } \Big ( 1 - e ^ { - \alpha _ { 1 } \nu _ { 1 } ( 1 - e ^ { - 2 \tau } ) } \Big ) \cdot } \\ &  \qquad \quad - p ^ { 2 \nu _ { 1 } } \Big [ \Big ( \frac { 3 } { 8 } - \frac { 2 \nu _ { 1 } e ^ { - \alpha _ { 1 } \nu _ { 1 } } } { 8 } + \frac { 2 }  3 \tau ^  \end{array}
$$$$
\begin{array} { r l } & { \quad = \frac { \bar { g } ^ { 2 } } { 4 \pi ^ { 2 } } \frac { 1 } { \bar { g } ^ { 2 } } \frac { 1 } { \bar { g } ^ { 2 } } \frac { \partial ^ { 2 } } { \partial \tau ^ { 2 } } - \frac { 2 \bar { g } ^ { 2 } } { 3 } \varepsilon ^ { 6 } - \frac { 2 1 } { 3 } \varepsilon ^ { 6 } } \\ & { \quad \quad \times ( 1 - \varepsilon ^ { 2 } ) ^ { 3 / 2 } \frac { \partial ^ { 2 } } { \partial \tau ^ { 2 } } - 3 ( 1 - \varepsilon ^ { 2 } ) ^ { 2 } ) } \\ & { \quad \quad + \beta ^ { 3 / 2 } \bigg [ \bigg ( \frac { 3 } { 4 } - \frac { 3 } { 2 } \varepsilon ^ { 6 } + \frac { 2 } { 3 } \varepsilon ^ { 6 } + \frac { 3 } { 2 } \varepsilon ^ { 6 } \bigg ) ( 1 - \sigma ^ { 4 } ) ^ { 3 / 2 } \sigma ^ { 2 } \bigg ] } \\ & { \quad \quad + \bar { g } \varepsilon \frac { 1 } { \bar { g } ^ { 2 } } \bigg ( \frac { 3 } { 3 } - \frac { 3 } { 2 } \varepsilon ^ { 6 } - \frac { \bar { g } ^ { 2 } } { 3 } \sigma ^ { 2 } \bigg ) \bigg ( 1 - \sigma ^ { 4 } ) ^ { 3 / 2 } \sigma ^ { 2 } } \\ & { \quad \quad \quad \quad + \bar { g } \varepsilon ^ { 2 } \bigg [ \bigg ( \frac { 1 } { 3 } - \frac { 3 } { 2 } \varepsilon ^ { 6 } - \frac { \bar { g } ^ { 2 } } { 3 } \sigma ^ { 2 } \bigg ) ( 1 - \sigma ^ { 4 } ) ^ { 3 / 2 } \sigma ^ { 3 } + 3 \sigma ^ { 2 } \sigma ^ { 2 } } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \frac { \partial ^ { 2 } } { \partial \tau ^ { 2 } } \frac { 1 } { \partial \tau ^ { 3 } } - \frac { 4 \bar { g } ^ { 2 } } { 3 } \varepsilon ^ { 6 } \bigg ( \frac { 1 } { \bar { g } ^ { 2 } } \sigma ^ { 2 } \bigg ) \varepsilon \frac { 1 } { 3 } \bigg ( \frac { 3 } { \bar { g } ^ { 2 } } \sigma ^ { 2 } \bigg ) ^ { 2 } } \\ &  \quad \quad \quad \quad \quad - \varepsilon ^ { 2 } \varepsilon ^ { 3 / 2 } \sigma ^   \end{array}
$$

于是有

$$
\begin{array} { l } { { \bar { \bar { \mu } } _ { 2 } ^ { * } = \displaystyle \frac { J _ { 2 } ^ { 2 } } { 4 L ^ { 2 } } \displaystyle \left\{ \frac { 3 } { 3 2 } \left( \bar { 3 } - 1 8 \cos ^ { 2 } i ^ { \prime } + 5 \cos i ^ { \prime } i ^ { \prime } \right) ( 1 - e ^ { \prime 2 } ) ^ { - 5 / 2 } \right. } } \\ { { \left. \qquad + \frac { 3 } { 8 } ( 1 - 6 \cos ^ { 2 } i ^ { \prime } + 9 \cos ^ { 4 } i ^ { \prime } ) \left( 1 - e ^ { \prime 2 } \right) ^ { - 3 } \right. } } \\ { { \left. \qquad - \frac { 1 5 } { 3 2 } ( 1 - 2 \cos ^ { 2 } i ^ { \prime } - 7 \cos ^ { 4 } i ^ { \prime } ) ( 1 - e ^ { \prime 2 } ) ^ { - 7 / 2 } \right. } } \\ { { \left. \qquad + \frac { 3 } { 1 6 } ( 1 - 1 6 \cos ^ { 2 } i ^ { \prime } + 1 5 \cos ^ { 4 } i ^ { \prime } ) \left( e ^ { \prime 2 } \left( 1 - e ^ { \prime 2 } \right) ^ { - 7 / 2 } \cos 2 g \right\} \right] } . }  \end{array}
$$

其中

$$
\cos i = \frac { H ^ { \prime } } { G ^ { \prime } } , ~ ( 1 - e ^ { \prime 2 } ) = \stackrel { \prime } { ( \frac { G ^ { \prime } } { L ^ { \prime } } ) } ^ { 2 } .
$$

对于一阶解而言，第一次消除 $\it { \Omega } _ { l }$ 的变换已完成，给出了生成函数 $\smash { \boldsymbol { S } ( \boldsymbol { S } _ { 0 } ) }$ 和 $\pmb { \ S } _ { 1 }$ )和变换后的哈密顿函数 ${ \pmb { F } } ^ { \ast }$ ，即

$$
F ^ { * } = F _ { 0 } ^ { * } \left( L ^ { \prime } \right) + F _ { 1 } ^ { * } \left( L ^ { \prime } , G ^ { \prime } , H ^ { \prime } \right) + F _ { 2 } ^ { * } \left( L ^ { \prime } , G ^ { \prime } , H ^ { \prime } , g \right) .
$$

但是，由于变换是由隐函数构成的，除 $\pmb { \ S } _ { 1 }$ 中含有原变量 $\pmb { l }$ 和 ${ \mathfrak { g } }$ 外，$. F ^ { * }$ 仍含有原变量 ${ \pmb g } _ { \pmb { \imath } }$ ，而问题需要 ${ \pmb { F } } ^ { * }$ 甚至 $\pmb { \ S } _ { 1 }$ （为了由新变量解得到相应的原变量解）都表示成新变量的函数，要达到这一要求并不困难，因为新旧变量之间的差别是一阶周期量，对于一阶解而言，将 $\pmb { \ S } _ { 1 }$ 和 ${ \pmb F } _ { 2 } ^ { * }$ 中的 $\pmb { l }$ 和 $\pmb { g }$ 直接换为 ${ \bf \nabla } _ { \pmb { \ l } ^ { \prime } }$ 和 ${ \pmb g } ^ { \prime }$ 即行，这样引起的差别分别为二阶周期量（相当于 $S _ { 2 }$ 中增加一部分)和三阶哈密顿函数项．至于高阶解，同样容易解决这一问题,这将在本节第4段中讨论．于是，新哈密顿函数可写成

$$
\begin{array} { r l } & { F ^ { * } = F _ { 0 } ^ { * } \left( L ^ { \prime } \right) + F _ { 1 } ^ { * } ( L ^ { \prime } , G ^ { \prime } , H ^ { \prime } ) + F _ { 2 , c } ^ { * } \left( L ^ { \prime } , G ^ { \prime } , H ^ { \prime } \right) } \\ & { \qquad + F _ { 2 , t } ^ { * } \left( L ^ { \prime } , G ^ { \prime } , H ^ { \prime } , g ^ { \prime } \right) . } \end{array}
$$

其中 $\pmb { F } _ { 2 \mathrm { ~ } \pmb { c } } ^ { * }$ 和 $\pmb { F _ { 2 } ^ { \star } }$ ，分别为 $\pmb { F } _ { 2 } ^ { * }$ 的不含 $g ^ { \prime }$ 和含 ${ \pmb g } ^ { \prime }$ 的部分，见（7.184）式， $\pmb { F } _ { 0 } ^ { * }$ 和 $\pmb { F } _ { 1 } ^ { \ast }$ 即由(7.177)式和(7.178)式表达．将 $\smash {  { S _ { \mathrm { 1 } } } ( L ^ { \prime } , G ^ { \prime } , H ^ { \prime } ) }$ $\therefore \ell ^ { \prime } , g ^ { \prime } )$ 代入(7.171)式，即可得出用新变量来表达旧变量的变换关系，即

$$
L { = } L ^ { \prime } { + } \frac { J _ { 2 } } { { 4 } L ^ { \prime 3 } } \bigg \{ ( { - 1 + 3 \cos ^ { 2 } i ^ { \prime } } ) \left[ \bigg ( \frac { a ^ { \prime } } { r ^ { \prime } } \bigg ) ^ { 3 } - ( 1 { - } e ^ { \prime 2 } ) ^ { - 3 / 2 } \right]
$$

$$
+ 3 ( 1 - \cos ^ { 2 } i ^ { \prime } ) \left( { \frac { a ^ { \prime } } { r ^ { \prime } } } \right) ^ { 3 } \cos 2 ( f ^ { \prime } + g ^ { \prime } ) \Big \} ,
$$

$$
G = G ^ { \prime } + \frac { J _ { 2 } } { 4 G ^ { \prime 3 } } \biggl \{ 3 \ ( 1 - \cos ^ { 2 } i ^ { \prime } ) \left[ e ^ { \prime } \cos \left( f ^ { \prime } + 2 g ^ { \prime } \right) \right.
$$

$$
\left. + \cos 2 \left( f ^ { \prime } + g ^ { \prime } \right) + \frac { e ^ { \prime } } { 3 } \cos \left( 3 f ^ { \prime } + 2 g ^ { \prime } \right) \right] \Bigr \} ,
$$

$$
H = H ^ { \prime } ,
$$

$$
\begin{array} { r l r } {  { L = L ^ { \prime } - \frac { I _ { \nabla } } { 4 L ^ { 2 } ( \Phi ^ { 2 } ) ^ { 5 } ( \varepsilon ^ { \prime \prime } ) } \Big \{ ( - 1 + 3 \cos 2 \varepsilon ) ^ { \prime } \Big \} \Bigg [ \bigg ( 3 - \frac { 3 } { 4 } \varepsilon ^ { \prime \prime } \bigg ) \sin \big ] f ^ { \prime } } } \\ & { } & { + \frac { 3 } { 2 } e ^ { \varepsilon } \sin 2 f ^ { \prime } - \frac { 1 } { 4 } e ^ { \varepsilon ^ { 2 } \sin \Omega / f ^ { \prime } } \Bigg ] } \\ & { } & { + 3 ( 1 - \cos 2 \varepsilon ^ { \prime \prime } ) \Bigg \{ - \frac { 3 } { 4 } e ^ { \varepsilon } \sin 2 g ^ { \prime } + \frac { 1 } { 8 } e ^ { \varepsilon ^ { \prime \prime } \sin \Omega } ( f ^ { \prime } - 2 g ^ { \prime } ) } \\ & { } & { - \bigg ( \frac { 1 } { 2 } - \frac { 5 } { 8 } e ^ { \varepsilon } \bigg ) \sin ( f ^ { \prime } - 2 g ^ { \prime } ) } \\ & { } & { + \bigg ( \frac { 7 } { 6 } - \frac { 1 } { 2 4 } e ^ { \varepsilon ^ { \prime \prime } } \bigg ) \sin ( 3 \xi ^ { \prime } + 2 g ^ { \prime } ) + \frac { 3 } { 4 } e ^ { \varepsilon } \sin ( 4 f ^ { \prime } + 2 g ^ { \prime } ) } \\ & { } & { - \bigg ( \frac { 1 } { 8 } e ^ { \varepsilon } \bigg ) \sin ( \bar { g } f ^ { \prime } + 2 g ^ { \prime } ) \Bigg \} , } \\ & { } & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad . } \end{array}
$$

$$
\begin{array} { r l } & { \quad + \frac { 1 } { 8 } e ^ { - x } \sin \left(  { \mathcal { Q } } ^ { \dagger } ( \cdot ,  { \mathcal { Q } } ^ { \dagger } ) \right) \Bigr | , } \\ { \ } & { \quad \le \sigma = \sigma ^ { 2 } - \frac { 1 } { 4 \sigma ^ { 2 } \sigma ^ { 4 } } \bigl ( 1 -  { \mathcal { Q } } \circ \Phi ^ { \dagger } \bigr ) \zeta ( \cdot , \sigma - \ell ) \cdot \sigma ^ { 2 } \cdots } \\ & { \quad - ( \sigma -  { \mathcal { Q } } \circ \Phi \circ \sigma ^ { 2 } ) \cdot \frac { 1 } { 2 } \frac { \sigma ^ { 2 } \sigma ^ { 4 } } { 2 } \bigl ( \sigma ^ { 2 } - \ell ^ { 2 } \bigr ) \cdot \frac { \sigma ^ { 2 } \sigma ^ { 2 } } { 2 } \cdots \bigl ( \sigma ^ { 2 } - \ell ^ { 2 } \bigr ) } \\ & { \quad - \frac { 1 } { 8 } e ^ { x } \sin \left( \sigma \mathcal { Q } ^ { \dagger } + \ell ^ { 2 } \sigma \right) \Bigr ] \Bigr | } \\ & { \quad \quad + \frac { 1 } { 8 } e ^ { x } \sin \left( \sigma \mathcal { Q } ^ { \dagger } \right) \Bigr [ \bigl ( - 1 + 2 \cos \Phi ^ { \dagger } \bigr ) \bigr ] \Bigr ( 3 - \frac { \sigma } { 2 } \sigma ^ { 2 } \bigr ) \sin \rho ^ { \prime } } \\ & { \quad \quad + \frac { 3 } { 8 } e ^ { x } \sin 2 \sigma ^ { 2 } \cdot \frac { 1 } { 4 } \frac { \sigma ^ { 2 } \sigma ^ { 2 } } { 2 } \cdots \sin 2 \sigma \Bigr | } \\ & { \quad \quad + \sigma \bigr ( 1 - \mathrm { e x t a r k } ^ { 1 / \prime } \bigr ) - \frac { 3 } { 4 } e ^ { x } \sin 2 \sigma ^ { 2 } + \frac { 1 } { 8 } e ^ { x } \sin ( \sigma \mathcal { Q } ^ { \dagger } - 2 \sigma ^ { 2 } ) } \\ & { \quad \quad - \bigl ( \frac { 3 } { 8 } + \frac { 3 } { 8 } e ^ { x } \bigr ) \sigma \bigr ) \cdot \sigma ^ { 2 } \cdots \sigma ^ { 2 } \circ \sigma ^ { 2 } + \frac { 1 } { 8 } e ^ { x } \sin ( \ell ^ { 2 } - 2 \sigma \mathcal { Q } ^ { \dagger } ) } \\ & { \quad \quad - \bigl ( \frac { 3 } { 8 } + \frac { 3 } { 8 } e ^ { x } \bigr ) \sigma \bigr ( \ell ^ { 2 } + 2 \sigma ^ { 2 } \bigr ) } \endarray \end{array}
$$$$
\begin{array} { r l } & { \quad _ { 1 } \cdot _ { 2 } ^ { \varepsilon } \sin ( { \Omega } ^ { \varepsilon } + { \gamma } ^ { \varepsilon } ) \Bigr | _ { \varepsilon } ^ { \varepsilon } } \\ & { \quad \quad - \frac { \gamma } { 4 } \cdot _ { \varepsilon } ^ { \varepsilon } \sin ( { \Omega } ^ { \varepsilon } ) \Bigr | \bigl ( - 1 + 3 \cos { \Omega } ^ { \varepsilon } \bigr ) ^ { \varepsilon } \Bigr | \Bigl ( \Delta - \frac { 3 } { 4 } \varepsilon ^ { \varepsilon } \bigr ) ^ { \varepsilon } \sin { f } } \\ & { \quad + \frac { 3 } { 2 } \cdot _ { \varepsilon } ^ { \varepsilon } \sin { 2 \phi } ^ { \varepsilon } \Bigr | \bigl ( - 1 + 3 \cos ^ { \varepsilon } \bigr ) ^ { \varepsilon } \Bigr | \int _ { 0 } ^ { \varepsilon } } \\ & { \quad + \frac { 3 } { 2 } \cdot _ { \varepsilon } ^ { \varepsilon } ( 1 - \sin { 2 \phi } ^ { \varepsilon } ) \Bigr | \Bigl ( - \frac { 3 } { 4 } \sin ^ { \varepsilon } \sin { 2 \phi } ^ { \varepsilon } \Bigr ) ^ { \varepsilon } \Bigr | } \\ & { \quad + 3 \langle ( 1 - \cos ^ { \varepsilon } \bigr ) ^ { \varepsilon } \Bigr | ( - \frac { 3 } { 4 } \sin ^ { \varepsilon } \sin { 2 \phi } ^ { \varepsilon } + \frac { 1 } { 8 } \varepsilon ^ { \varepsilon } \sin { ( \phi ^ { \prime } - 2 \phi ^ { \prime } ) }  } \\ & { \quad  - \Bigl ( \frac { 1 } { 2 } + \frac { 5 } { 8 } \varepsilon ^ { \varepsilon } \Bigr ) ^ { \varepsilon } \sin ( { \phi } ^ { \varepsilon } - 2 { \phi ^ { \prime } } ) } \\ & { \quad + \Bigl ( \frac { 7 } { 8 } \cdot \frac { 1 } { 2 4 } \varepsilon ^ { \varepsilon } \Bigr ) ^ { \varepsilon } \sin { ( \phi ) } ^ { \varepsilon } + 2 { \phi ^ { \prime } } } \\ & { \quad - \frac { 3 } { 4 } \cdot _ { \varepsilon } ^ { \varepsilon } \sin { ( 4 \phi ) } ^ { \varepsilon } \bigl | \sin ^ { \varepsilon } \bigr | ^ { \varepsilon } \cos ^ { \varepsilon } \bigr ) \Bigr | \int _ { 0 } ^ { \varepsilon } \langle z \rangle } \\ & { \quad + \frac { 3 } { 2 } \cdot _ { \varepsilon } ^ { \varepsilon } \sin { ( 4 \phi ) } ^ { \varepsilon } \bigl | \sin ^ { \varepsilon } \theta \rangle \Bigr | \varepsilon ^ { \prime } \langle z \rangle } \\ &  \quad + \frac { 3 } { 2 } \cdot _ \end{array}
$$

$$
\left. \left. + \frac { e ^ { \prime } } { 2 } \sin { ( f ^ { \prime } + 2 g ^ { \prime } ) } + \frac { e ^ { \prime } } { 6 } \sin { ( 3 f ^ { \prime } + 2 g ^ { \prime } ) } \right] \right\} .
$$

上列各式新旧变量之间的差别，即一阶短周期项 $\sigma _ { s } ^ { ( 1 ) } ( t )$ ，因此，新变量 $L ^ { \prime } , G ^ { \prime } , H ^ { \prime } , l ^ { \prime } , g ^ { \prime } , h ^ { \prime }$ 就相当于消除短周期项的拟平均根数，可统一记成 $\sigma ^ { \prime } ( t )$ ，同样，除 $\overline { { L _ { s } ^ { ( 1 ) } ( t ) } } = 0$ 外， $\overline { { \sigma _ { \mathscr { s } } ^ { ( 1 ) } ( t ) } } \neq 0$ 包含了含 $g ^ { p }$ 的项，从变换的角度来看，这没有任何问题。

根据上述讨论不难看出，在求 ${ \pmb S _ { 1 } }$ 时，按二体问题关系积分是严格的，由它求出“短周期项”也就无需经过“近似”处理，对高阶项亦如此，这从数学角度来看，比第五章介绍的平均根数法清楚得多，而且，由方程(7.180）求 $\pmb { \ S } _ { 1 }$ 时，可以根据某种需要增加一个与$\pmb { l }$ 无关的任意函数，对最后所需要的原变量 $( L , G , H , l , g , \hbar )$ 的解没有影响，关于这一点，将留给读者作为一个习题去讨论。

# 2．第二次消除 $\sum ^ { \prime }$ 的变换—一分离长周期项

与第一次消除 $\pmb { l }$ 的变换类似，即寻找下列形式的生成函数：

$$
\left. \begin{array} { l } { { \delta ^ { * } = \displaystyle { \cal S } ^ { * } ( L ^ { \eta } , G ^ { \eta } , H ^ { \eta } , l ^ { \prime } , g ^ { \prime } , h ^ { \prime } ) = \displaystyle { \cal S } _ { 0 } ^ { * } + \displaystyle { \cal S } _ { 1 } ^ { * } + \cdots + \delta _ { j } ^ { * } + \cdots , } } \\ { { \displaystyle { \cal S } _ { 0 } ^ { * } = { \cal L } ^ { \eta } l ^ { \prime } + G ^ { \eta } g ^ { \prime } + H ^ { \eta } h ^ { \prime } , } } \\ { { \displaystyle { \cal S } _ { j } ^ { * } = { \cal O } ( \varepsilon ^ { j } ) . } } \end{array} \right\} .
$$

使新哈密顿函数 $\pmb { F } ^ { \ast \ast }$ 满足

$$
{ \cal F } ^ { * * } = \sum _ { j = 0 } ^ { k } { \cal F } _ { j } ^ { * * } ~ ( L ^ { \prime \prime } , G ^ { \prime \prime } , H ^ { \prime \prime } ) ~ + ~ \sum _ { j \geqslant k + 1 } { \cal F } _ { j } ^ { * * } ( L ^ { \prime \prime } , G ^ { \prime \prime } , H ^ { \prime \prime } , g ^ { \prime } ) , ~ \Biggr \} .
$$

$$
{ \cal F } _ { j } ^ { \ast } { } ^ { \ast } = \cal 0 ( \varepsilon ^ { j } ) .
$$

针对(7.186)式给出的 ${ \pmb { F } } ^ { \star }$ ，可以假定

$$
S _ { j } ^ { * } = S _ { j } ^ { * } ( L ^ { n } , G ^ { n } , H ^ { n } , g ^ { \prime } ) , j = 1 , 2 \cdots ,
$$

相应的正则变换为

$$
\left. \begin{array} { l } { { { \cal { L } } ^ { \prime } = { \cal { L } } ^ { \prime \prime } , } } \\ { { { \cal { L } } ^ { \prime } - { \cal { G } } ^ { \prime \prime } + \displaystyle \frac { \partial \mathcal { S } _ { 1 } ^ { * } } { \partial g ^ { \prime } } + \displaystyle \frac { \hat { c } \mathcal { S } _ { 2 } ^ { * } } { \partial g ^ { \prime } } + \cdots , } } \\ { { \cal { L } } ^ { \prime \prime } = { \cal { L } } ^ { \prime } + \displaystyle \frac { \partial \mathcal { S } _ { 1 } ^ { * } } { \partial { \cal { L } } ^ { \prime } } + \displaystyle \frac { \partial \mathcal { S } _ { 2 } ^ { * } } { \partial { \cal { L } } ^ { \prime } } + \cdots , }  \\ { { \displaystyle g ^ { \prime \prime } = g ^ { \prime } + \displaystyle \frac { \partial \mathcal { S } _ { 1 } ^ { * } } { \partial { \cal { L } } ^ { \prime } } + \displaystyle \frac { \partial \mathcal { S } _ { 2 } ^ { * } } { \partial { \cal { G } } ^ { \prime \prime } } + \cdots , } } \\ { { { \cal { H } } ^ { \prime } = { \cal { H } } ^ { \prime \prime } , ~ h ^ { \prime \prime } = h ^ { \prime } + \displaystyle \frac { \partial \mathcal { S } _ { 1 } ^ { * } } { \partial { \cal { H } } ^ { \prime \prime } } + \displaystyle \frac { \partial \mathcal { S } _ { 2 } ^ { * } } { \partial { \cal { H } } ^ { \prime \prime } } + \cdots . } } \end{array} \right\}
$$

与确定 $S ( L ^ { \prime } , G ^ { \prime } , H ^ { \prime } , l , g , h )$ 的方法类似，应从下列关系中来确定$\mathcal { S } ^ { \ast } ( L ^ { \prime \prime } , G ^ { \prime \prime } , H ^ { \prime \prime } , l ^ { \prime } , g ^ { \prime } , h ^ { \prime } )$ ，即

$$
\begin{array} { r l } { { } } & { { \displaystyle F ^ { * * } = F ^ { * } ( \tilde { L } ^ { \prime } { = } \tilde { L } ^ { \prime } ( \tilde { L } ^ { \prime } ( \dot { } \cdot , G ^ { \prime \prime } , H ^ { \prime \prime } , g ^ { \prime } ) , H ^ { \prime } { = } H ^ { \prime \prime } , g ^ { \prime } ) } } \\ { { } } & { { \displaystyle ~ - \sum _ { j = 0 } ^ { k } F _ { j } ^ { * } ( \tilde { L } ^ { \prime \prime } , G ^ { \prime \prime } , H ^ { \prime \prime } ) + \sum _ { j \ge k + 1 } ^ { } F ^ { * * } ( L ^ { \prime \prime } , G ^ { \prime \prime } , H ^ { \prime \prime } , g ^ { \prime } ) . } } \end{array}
$$

按 $\pmb { \varepsilon } = \pmb { J } _ { 2 }$ 的幂对 ${ { L } ^ { \prime \prime } } , { { G } ^ { \prime \prime } } , \dot { { H } ^ { \prime \prime } }$ 展开得

$$
\begin{array} { r l } & { \quad F _ { \vartheta } ^ { \ast } \gets F _ { 1 } ^ { \ast } \gets F _ { 2 } ^ { \ast } \gets F _ { 3 } ^ { \ast } + \ d F _ { 3 } ^ { \ast } + \ d F _ { 3 } ^ { \ast } + \ d H \cdots } \\ & { = F _ { 0 } ^ { \ast } \left( L ^ { \prime \prime } \right) + F _ { 1 } ^ { \ast } \left( L ^ { \prime \prime } , G ^ { \prime \prime } , H ^ { \prime \prime } \right) + \frac { \partial F _ { 1 } ^ { \ast } } { \partial G ^ { \prime \prime } } \Big ( \frac { \partial S _ { 1 } ^ { \ast } } { \partial g ^ { \prime } } + \frac { \partial S _ { 2 } ^ { \ast } } { \partial g ^ { \prime } } + \cdots \Big ) } \\ & { \quad + \frac { 1 } { 2 } \frac { \partial ^ { 2 } F _ { 1 } ^ { \ast } } { \partial G ^ { \prime \prime } } \Big ( \frac { \partial S _ { 1 } ^ { \ast } } { \partial g ^ { 1 } } + \cdots \Big ) ^ { 2 } + \cdots } \\ & { \quad + F _ { 2 } ^ { \ast } \left( L ^ { \prime \prime } , G ^ { \prime \prime } , H ^ { \prime \prime } , g ^ { \prime \prime } \right) + \frac { \partial F _ { 2 } ^ { \ast } } { \partial G ^ { \prime } } \Big ( \frac { \partial S _ { 1 } ^ { \ast } } { \partial g ^ { \prime } } + \cdots \Big ) + \cdots , \quad \left( 7 . \right) } \end{array}
$$

比较该式两端 $\pmb { J _ { 2 } }$ 的同次幂，即得

$$
\begin{array} { r l } & { F _ { 0 } ^ { * * } = F _ { 0 } ^ { * } ( L ^ { \prime \prime } ) , } \\ & { F _ { 1 } ^ { * * } = F _ { 1 } ^ { * } ( L ^ { \prime \prime } , G ^ { \prime \prime } , H ^ { \prime \prime } ) , } \\ & { F _ { 2 } ^ { * * } = \displaystyle \frac { \partial F _ { 1 } ^ { * } } { \partial G ^ { \prime \prime } } \Big ( \frac { \partial S _ { 1 } ^ { * } } { \partial g ^ { \prime } } \Big ) + F _ { 2 } ^ { * } ( L ^ { \prime \prime } , G ^ { \prime \prime } , H ^ { \prime \prime } , g ^ { \prime } ) , } \end{array}
$$

于是由(7.177)和(7.178)两式给出的 $\pmb { F } _ { 0 } ^ { \ast }$ 和 $\pmb { F } _ { 1 } ^ { \ast }$ 得

$$
\bar { F } _ { \mathrm { ~ 0 ~ } } ^ { * * } = \frac { 1 } { 2 L ^ { \prime \prime 2 } } ,
$$

$$
F _ { 1 } ^ { * * } = { \frac { J _ { 2 } } { 2 L ^ { \prime \prime } { } ^ { 3 } G ^ { \prime \prime } { } ^ { 5 } } } A ^ { \prime \prime } = { \frac { J _ { 2 } } { 2 L ^ { \prime \prime } { } ^ { 3 } G ^ { \prime \prime } { } ^ { 3 } } } \biggl ( - { \frac { 1 } { 2 } } + { \frac { 3 } { 2 } } \ H ^ { \prime \prime } { } ^ { 2 } \biggr ) .
$$

同样可将(7.202)式分成两部分·

$$
\begin{array} { r l } & { I _ { 2 } ^ { * * } \simeq F _ { 2 ^ { c } } ^ { * } ( L ^ { \eta } , G ^ { \eta } , H ^ { \eta } ) } \\ & { \qquad = \frac { T _ { 2 } ^ { * } } { 4 L ^ { \eta / 1 0 } } \bigg [ \frac { 3 } { 3 2 } ( 5 - 1 8 \cos ^ { 2 } \eta ^ { * \eta } \cdot 5 \cos ^ { 4 \eta } ) ( 1 - e ^ { \eta \tau 2 } ) ^ { - 5 / 2 } } \\ & { \qquad + \frac { 3 } { 8 } ( 1 - 6 \cos ^ { 2 } \eta ^ { * \eta } + 9 \cos ^ { 4 \eta ^ { * } } ) ( 1 - e ^ { \eta ^ { 2 } } ) ^ { - 3 } } \\ & { \qquad - \frac { 1 5 } { 3 2 } ( 1 - 2 \cos ^ { 2 } \eta ^ { * \eta } - 7 \cos ^ { 4 \eta ^ { * } } ) ( 1 - e ^ { \eta ^ { 2 } } ) ^ { - / 2 } \bigg ] ; \qquad \mathcal { C } } \\ & { \qquad 0 = F _ { 2 ^ { c } } ^ { * } \cdot \frac { - 9 F _ { 1 } ^ { * } } { 2 G ^ { \eta / 1 } } \bigg ( \frac { 3 8 1 } { 9 G ^ { \eta } } \bigg ) . } \end{array}
$$

后一式用来确定 $\pmb { \ S } _ { 1 } ^ { * }$ ，即

$$
\frac { \partial S _ { 1 } ^ { \ast } } { \partial g ^ { \prime } } { = } F _ { 2 } ^ { \ast } \mathrm { ~ , ~ } \biggl / \Bigl ( { - } \frac { \partial F _ { 1 } ^ { \ast } } { \partial G ^ { \prime \prime } } \Bigr ) ,
$$

以 $\boldsymbol { F } _ { 1 } ^ { * }$ 和 $\pmb { F _ { 2 i } ^ { * } }$ 代人积分得

$$
\begin{array} { l } { { \displaystyle \mathcal { S } _ { 1 } ^ { * } = - \frac { J _ { 2 } } { 3 2 G ^ { \prime \prime \prime ^ { 3 } } } e ^ { \prime \prime 2 } ( 1 - 1 6 \cos ^ { 2 } i ^ { \prime \prime } + 1 5 \cos i ^ { \prime \prime } ) } } \\ { { \displaystyle \qquad \times ( 1 - 5 \cos ^ { 2 } i ^ { \prime \prime } ) ^ { - 1 } \sin 2 g ^ { \prime } } . } \end{array}
$$

其中 $( 1 - 5 \cos ^ { 2 } i ^ { \prime \prime } ) ^ { - 1 }$ 的出现是由

$$
- \frac { \partial F _ { 1 } ^ { * } } { \hat { q } \hat { G } ^ { \prime \prime } } { = } - \frac { 3 J _ { 2 } } { 4 L ^ { \prime \prime } ^ { 3 } \hat { G } ^ { \prime \prime } { } ^ { 4 } } ( 1 { - } 5 \cos ^ { 2 } \dot { \iota } ^ { \prime \prime } )
$$

引进的，而 $\frac { \partial F _ { 1 } ^ { * } } { \partial G ^ { \prime \prime } } { = } - \frac { \partial F _ { 1 } ^ { * * } } { z G ^ { \prime \prime } } { - }$ 就是 ${ \pmb g } ^ { \prime \prime }$ 的一阶长期项系数，即第五.  
章中给出的 $\omega _ { 1 }$ ，临界角问题就由此产生。

到此，在一阶解意义下，第二次消除 ${ \pmb g } ^ { \prime }$ 的变换已完成，新哈密顿函数 ${ \pmb { F } } ^ { * * }$ 为

$$
F ^ { * * } = F _ { 0 } ^ { * * } ( L ^ { \prime \prime } ) + F _ { 1 } ^ { * * } ( L ^ { \prime \prime } , G ^ { \prime \prime } , H ^ { \prime \prime } , ) + F _ { 2 } ^ { * * } ( L ^ { \prime \prime } , G ^ { \prime \prime } , H ^ { \prime \prime } ) ,
$$

共中 $F _ { \mathrm { ~ 0 ~ } } ^ { * * } , F _ { 1 } ^ { * * } , F _ { 2 } ^ { * * }$ 分别由(7.202),(7.203),(7.204)三式表达.

与第一次变换类似，在一阶解意义下， $S _ { 1 } ^ { * } ( L ^ { \prime \prime } , G ^ { \prime \prime } , H ^ { \prime \prime } , g ^ { \prime } )$ 中的 ${ \pmb g } ^ { \prime }$ 可直接换成 ${ \pmb g } ^ { \prime \prime }$ ,于是将这样的 $\pmb { \ S _ { 1 } ^ { * } }$ 代入(7.196)式，即得新旧变量之间的简单变换关系：

$$
L ^ { \prime } = L ^ { \prime \prime } ,
$$

$$
\begin{array} { r l } { G ^ { n } = G ^ { n + \frac { 1 } { n } } - \frac { \int _ { 0 } } { 1 \tilde { \Phi } ( d ^ { n + 1 } ) } \frac { \int _ { 0 } } { 1 \tilde { \Phi } ( d ^ { n + 1 } ) } ( 1 - I 6 \cos { \bf u } ^ { s _ { 1 } + n } + 1 5 \cos { \bf u } ^ { s _ { 1 } + n } ) } \\ { \times ( 1 - 5 \cos { \bf u } ^ { 2 } ) ^ { n } ) - \cos { 2 \theta ^ { n } } ^ { s _ { 1 } } , } \\ { I ^ { n } : = I ^ { n } ; } \\ { I ^ { n } = I ^ { n } ; \frac { \int _ { 0 } } { 1 + 1 5 \cos { \bf u } ^ { 3 } ( d ^ { n + 1 } ) } - 1 . 8 \cos { \bf u } ^ { s _ { 1 } + n } \mathrm { ~ i ~ } \Sigma \mathrm { ~ e q ~ } \mathrm { e \ } ^ { i \left( 1 + 1 5 \cos { \bf u } ^ { s _ { 1 } + n } \right) } } \\ { \times ( 1 - 5 \cos { 2 \theta ^ { n } } ) ^ { n } - 1 . 4 \sin { 2 \theta ^ { n } } ^ { s _ { 1 } } , } \\ { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\  \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \end{array}
$$

$$
+ \left. ( 1 - 5 \cos ^ { 2 } i ^ { n } ) ^ { - 2 } [ \left( - 2 0 0 e ^ { n ^ { \prime } 2 } \right) \cos ^ { 6 } i ^ { n \prime \prime } ] \right\} \sin 2 g ^ { n \prime } .
$$

$$
\hbar ^ { \prime } = \hbar ^ { \prime \prime } - \frac { J _ { 2 } } { 1 6 G ^ { \prime \prime 4 } } e ^ { \prime \prime 2 } \cos \mathfrak { s } ^ { \prime \prime } \big [ ( 1 - 5 \cos ^ { 2 } \mathfrak { s } ^ { \prime \prime } ) ^ { - 1 } ( 1 1 + 2 5 \cos ^ { 2 } \mathfrak { s } ^ { \prime \prime } )
$$

$$
+ ( 1 - 5 \cos ^ { 2 } i ^ { \prime \prime } ) ^ { - 2 } ( 2 0 0 \cos ^ { 4 } i ^ { \prime \prime } ) ] \sin 2 g ^ { \prime \prime } .
$$

上列各式新旧变量之间的差别,即一阶长周期项 $\sigma _ { \textit { l } } ^ { ( 1 ) } \big ( t \big )$ ，因此，新变量 $L ^ { \prime \prime } , G ^ { \prime \prime } , H ^ { \prime \prime } , l ^ { \prime \prime } , g ^ { \prime \prime } , h ^ { \prime \prime }$ 就相当于消除全部周期项的平均根数，可统一记成 $\sigma ^ { \prime \prime }$ ·

# 3.摄动解

经过两次变换给出的 $\pmb { F } ^ { \ast \ast }$ 出现了三个循环坐标，于是有三个积分：

$$
\begin{array} { l } { { L ^ { \prime \prime } { = } L _ { 0 } ^ { \prime \prime } , } } \\ { { \ } } \\ { { G ^ { \prime \prime } { = } G _ { \ 0 } ^ { \prime \prime } , } } \\ { { \ } } \\ { { H ^ { \prime \prime } { = } H _ { 0 } ^ { \prime \prime } . } } \end{array}
$$

而另三个变量的解可直接写出，即

$$
\left. \begin{array} { l } { { \displaystyle { \it l } ^ { \prime \prime } = l _ { 0 } ^ { \prime \prime } + \biggl ( - \frac { \partial { \cal F } ^ { * * } } { \partial L ^ { \prime \prime } } \biggr ) ( t - t _ { 0 } ) } , } \\ { { } } \\ { { \displaystyle g ^ { n } = g _ { 0 } ^ { n } + \biggl \{ - \frac { \partial { \cal F } ^ { * * } } { \partial G ^ { \prime \prime } } \biggr ) ( t - t _ { 0 } ) , \left. \right\} } } \\ { { \displaystyle h ^ { n } = h _ { 0 } ^ { n } + \biggl ( - \frac { \partial { \cal F } ^ { * * } } { \partial H ^ { n } } \biggr ) ( t - t _ { 0 } ) . } } \end{array} \right\}
$$

共 $\scriptstyle \left( - { \frac { \partial F ^ { * * } } { \partial L ^ { n } } } \right) , \left( - { \frac { \partial F ^ { * * } } { \partial G ^ { n } } } \right) , \left( - { \frac { \partial F ^ { * * } } { \partial H ^ { n } } } \right)$ 都是 $L ^ { \prime \prime } , G ^ { \prime \prime } , H ^ { \prime \prime }$ 的函数，

$$
\begin{array} { r l } &  \varepsilon ( \mathbf { k } \parallel \mathbf { k } \parallel ^ { 2 } \mathbf { s } \parallel \mathbf { k } \parallel ^ { 3 } \mathbf { H } \perp \phi \mathbf { N } , \mathbf { k } \phi \mathbf { k } \parallel ^ { 2 } \mathbf { H } \phi \mathbf { N } , \mathbf { k } \phi \mathbf { k } \mathbf { H } \phi \mathbf { N } , \mathbf { k } \phi \mathbf { k } \mathbf { H } \phi \mathbf { N } , \mathbf { k } \phi \mathbf { k } \mathbf { H } \phi \mathbf { N } , \mathbf { k } \phi \mathbf { k } \mathbf { H } \phi \mathbf { N } , \mathbf { k } \phi \mathbf { k } \mathbf { H } \phi , \mathbf { k } \mathbf { k } \mathbf { H } \phi , \mathbf { k } \mathbf { k } \mathbf { H } \phi , \mathbf { k } \mathbf { k } \mathbf { H } \phi , \mathbf { k } \mathbf { k } \mathbf { H } \phi , \mathbf { k } \mathbf { k } \mathbf { H } \phi , \mathbf { k } \mathbf { k } \mathbf { H } \phi , \mathbf { k } \mathbf { k } \mathbf { H } \mathbf { k } \mathbf { H } \phi , \mathbf { k } \mathbf { k } \mathbf { H } \mathbf { k } \mathbf { H } \phi , \mathbf { k } \mathbf { k } \mathbf { H } \mathbf { k } \mathbf { H } \mathbf { k } \mathbf { H } \mathbf { k } \mathbf { H } \mathbf { k } \mathbf { k } \mathbf \phi , \mathbf { k } \mathbf { k } \mathbf { H } \mathbf { k } \mathbf \phi , \mathbf { k } \mathbf { k } \mathbf { k } \mathbf \phi \mathbf { k } \mathbf { k } \mathbf \phi , \mathbf { k } \mathbf { k } \mathbf \phi \mathbf { k } \mathbf { k } \mathbf \phi , \mathbf { k } \mathbf { k } \mathbf \phi \mathbf { k } \mathbf { k } \mathbf \phi , \mathbf { k } \mathbf { k } \mathbf \phi \mathbf { k } \mathbf { k } \mathbf \phi , \mathbf { k } \mathbf { k } \mathbf \phi \mathbf { k } \mathbf { k } \mathbf \phi , \mathbf { k } \mathbf { k } \mathbf \phi \mathbf { k } \mathbf { k } \mathbf \phi , \mathbf { k } \mathbf { k } \mathbf \phi \mathbf { k } \mathbf { k } \mathbf \phi , \mathbf { k } \mathbf { k } \mathbf \phi \mathbf { k } \mathbf { k } \mathbf \phi , \mathbf { k } \mathbf { k } \mathbf { H } \mathbf { k } \mathbf { k } \mathbf { H } \mathbf { k } \mathbf { k } \mathbf { H } \mathbf { k } \mathbf { k } \mathbf { H } \mathbf { k } \mathbf { k } \mathbf { H } \mathbf { k } \mathbf { k } \mathbf { H } \mathbf { k } \mathbf { k } \mathbf { H } \mathbf { k } \mathbf { k } \mathbf { H } \mathbf { k } \mathbf { k } \mathbf { H } \mathbf  \end{array}
$$

$$
\begin{array} { l } { { \displaystyle - \frac { \partial F ^ { * * } } { \partial H ^ { n } } = n ^ { n } \left. J _ { 2 } \Biggl ( - \frac { 3 } { 2 G ^ { n + 1 } } \cos i ^ { n } ) \right. } } \\ { { \displaystyle \qquad + J _ { 2 } ^ { 2 } \left( \frac { 3 } { 3 2 G ^ { n / 8 } } \cos i ^ { n } \right) \Biggl [ ( 4 - 4 0 \cos ^ { 2 } i ^ { n } ) + e ^ { n ^ { 2 } } } } \end{array}
$$

$$
( - 9 + 5 \cos ^ { 2 } i ^ { \prime \prime } )
$$

$$
+ \Bigl ( \frac { G ^ { n } } { L ^ { n } } \Bigr ) ( 1 2 - 3 6 \cos ^ { 2 } i ^ { n } ) \Biggr ] \Biggr \} ,
$$

其中 $n ^ { \prime \prime } { = } L ^ { \prime \prime - 3 } .$

上述(7.214)和(7.215)两式即平均根数 $\sigma ^ { \prime \prime } ( t )$ 的解，积分常数 $L _ { 0 } ^ { \prime } , G _ { 0 } ^ { \prime \prime } , H _ { 0 } ^ { \prime \prime } , l _ { 0 } ^ { \prime \prime } , g _ { 0 } ^ { \prime \prime } , h _ { 0 } ^ { \prime \prime }$ 就是初始平均根数 $\sigma _ { 0 } ^ { \prime \prime }$ ，于是原变量 $L$ ，$G , H , l , g , h $ 记成 $\pmb { \sigma }$ )的解可由变换关系来确定，即

$$
\begin{array} { c } { { \sigma ( t ) = \sigma ^ { \prime } ( t ) + \sigma _ { g } ^ { ( 1 ) } ( t ) } } \\ { { = \sigma ^ { \prime \prime } ( t ) + \sigma _ { l } ^ { ( 1 ) } ( t ) + \sigma _ { s } ^ { ( 1 ) } ( t ) . } } \end{array}
$$

其中 $\sigma _ { \mathcal { S } } ^ { ( 1 ) } ( t )$ 和 $\sigma _ { \iota } ^ { ( 1 ) } ( \iota )$ 分别由(7.187)—(7.192)式和(7.208)—(7.213)式中相应的项表达。在计算中有关初始平均根数 $L _ { 0 } ^ { \prime \prime } , G _ { 0 } ^ { \prime \prime }$ ，$H _ { 0 } ^ { \prime \prime } , l _ { 0 } ^ { \prime \prime } , g _ { 0 } ^ { \prime \prime } , h _ { 0 } ^ { \prime \prime }$ 的处理,与第五章中的方法相同,不再重复。

关于 $J _ { 2 }$ 项的摄动解，平均根数法与Zeipel方法都是将摄动变化部分分成长期项,长周期项和短周期项三个部分，因此，结果是应该相同的．但是,在长、短周期项中分别出现一些差别也是有可能的，例如

$$
g _ { \vartheta } ^ { ( 1 ) } = \omega _ { \vartheta } ^ { ( 1 ) } - \Bigl ( \frac { 3 J _ { 2 } } { 2 p ^ { 2 } } \Bigr ) \frac { 3 } { 8 } \sin ^ { 2 } i \sin 2 \omega ,
$$

$$
l _ { s } ^ { ( 1 ) } = M _ { s } ^ { ( 1 ) } + \left( \frac { 3 J _ { 2 } } { 2 p ^ { 2 } } \right) \frac { 3 } { 8 } \sqrt { 1 - e ^ { 2 } } \sin ^ { 2 } i \sin 2 \omega ,
$$

而

$$
g _ { l } ^ { ( 1 ) } { = } \omega _ { l } ^ { ( 1 ) } { + } \bigg ( \frac { 3 J _ { 2 } } { 2 p ^ { 2 } } \bigg ) \frac { 3 } { 8 } \mathrm { s i n } ^ { 2 } i \sin { 2 \omega } ,
$$

$$
l _ { \ i } ^ { \left( 1 \right) } = \mathcal { M } _ { \ \iota } ^ { \left( 1 \right) } - \left( \frac { 3 J _ { 2 } } { 2 p ^ { 2 } } \right) \frac { 3 } { 8 } \sqrt { 1 - e ^ { 2 } } \sin ^ { 2 } i \sin 2 \omega .
$$

显然，对整个解而言是一致的，只是部分长周期项出现的位置不一样，这是由于消除 $l$ 分离短周期项时，包含了部分长周期项的结果．另外，在二阶长期项中， $l _ { 2 }$ 和 $M _ { 2 }$ 在形式上亦有一些差别，这是由于两者计算时分别用到的系数 ${ \pmb n } _ { 0 } ^ { \prime \prime }$ 和 $\overleftarrow { \pmb { n } } _ { 0 }$ 相差一个二阶常数项所造成,具体形式不再写出，读者如有兴趣可查阅1979 年南京大学出版社的铅印讲义 $\mathfrak { K } _ { \cdot }$ 人造地球卫星轨道理论》一书的第八章。

最后说明一点，从前面两次变换的过程来看，消除 $\iota$ 和 $\pmb { g }$ 的变换也可以一次进行，请见文[6],但最后还是要将长短周期项分开，并无实质性差别，也没有带来方便,文[7]曾作过详细的比较.还有，第一次变换后，含 ${ \pmb g } ^ { \prime }$ 的项只涉及到 $\dot { F } _ { \mathrm { ~ \scriptsize ~ 2 ~ } } ^ { * }$ ，因此第二次变换也可以按$\mu = e ^ { 2 }$ 的幂来展开，这可以简化一些过程，称为加速收敛法[8-10].不过，对于人造卫星运动而言，常用分析方法构造级数解时只做到二阶解，加速收敛的优点不显著[7]，本书不再专门介绍.

# 4.高阶解的建立

从前面的变换过程来看，用Zeipel方法建立高阶解（二阶以上），并无原则困难．但由于用了隐函数 $\delta ( L ^ { \prime } , G ^ { \prime } , H ^ { \prime } , l , g , h ) , S ^ { * }$ $\left. L ^ { \prime \prime } , G ^ { \prime \prime } , H ^ { \prime \prime } , l ^ { \prime } , g ^ { \prime } , h ^ { \prime } \right.$ 定义的正则变换，给出的关系是混合变量的形式(或隐函数形式)，涉及到变量的另一种转换，下面针对构造$J _ { z }$ 项摄动的二阶解来说明这一问题.

# （1）第一次消除 $\imath$ 的变换

生成函数 $\pmb { S }$ 和相应的 $\pmb { F }$ 对 $L ^ { \prime } , G ^ { \prime } , H ^ { \prime }$ 的展开式仍然由(7.167)和(7.173)式表达，对于二阶解，需要确定 $\pmb { \mathcal { S } } _ { 1 }$ 和 $S _ { 2 }$ 以及相应的$F _ { 0 } ^ { \ast } , \varPsi _ { 1 } ^ { \ast } , F _ { 2 } ^ { \ast }$ 和 ${ \pmb { F } } _ { 3 } ^ { * }$ ，其中确定 $\pmb { S _ { 1 } } , \pmb { S _ { 2 } }$ 以及 $F _ { 0 } ^ { * } , F _ { 1 } ^ { * } , F _ { 2 } ^ { * }$ 的表达式同前，由（7.173)式给出 $\pmb { J _ { 2 } ^ { 3 } }$ 部分为

$$
\begin{array} { r l } & { { F _ { 3 } ^ { * } } = \frac { { \partial ^ { 2 } } { F _ { 0 } } } { { \partial { L ^ { \prime } } ^ { 2 } } } \Big ( \frac { { \partial { S _ { 1 } } } } { { \partial l } } \Big ) \Big ( \frac { { \partial { S _ { 2 } } } } { { \partial l } } \Big ) + \frac { 1 } { 6 } \frac { { \partial ^ { 3 } } { F _ { 0 } } } { { \partial { L ^ { \prime } } ^ { 3 } } } \Big ( \frac { { \partial { S _ { 1 } } } } { { \partial l } } \Big ) ^ { 3 } } \\ & { \qquad + \frac { { \partial { F _ { 1 } } } } { { \partial { L ^ { \prime } } } } \Big ( \frac { { \partial { S _ { 2 } } } } { { \partial { L ^ { \prime } } } } \Big ) + \frac { { \partial { F _ { 1 } } } } { { \partial { G ^ { \prime } } } } \Big ( \frac { { \partial { S _ { 2 } } } } { { \partial g } } \Big ) } \\ & { \qquad + \frac { 1 } { 2 } \frac { { \partial ^ { 2 } } { F _ { 1 } } } { { \partial { L ^ { \prime } } ^ { 2 } } } \Big ( \frac { { \partial { S _ { 1 } } } } { { \partial l } } \Big ) ^ { 2 } + \frac { 1 } { 2 } \frac { { \partial ^ { 3 } } { F _ { 1 } } } { { \partial { G ^ { \prime } } ^ { 2 } } } \Big ( \frac { { \partial { S _ { 1 } } } } { { \partial g } } \Big ) ^ { 2 } } \\ & { \qquad + \frac { { \partial ^ { 2 } } { F _ { \mathrm { 1 } } } } { { \partial { L ^ { \prime } } ^ { 2 } } \bar { G } ^ { \prime } } \Big ( \frac { { \partial { S _ { 1 } } } } { { \partial l } } \Big ) \Big ( \frac { { \partial { S _ { 1 } } } } { { \partial g } } \Big ) \Big \} _ { \varepsilon , \varepsilon } } \end{array}
$$

确定 $S _ { 3 }$ 的部分从略。用Zeipel方法给出的结果为

$$
\begin{array} { r l r } { F ^ { * } = F _ { 0 } ^ { * } ( L ^ { \prime } ) + F _ { 1 } ^ { * } ( L ^ { \prime } , G ^ { \prime } , H ^ { \prime } ) + F _ { 2 } ^ { * } ( L ^ { \prime } , G ^ { \prime } , H ^ { \prime } , g ) } \\ { + F _ { 8 } ^ { * } ( L ^ { \prime } , G ^ { \prime } , H ^ { \prime } , g ) . } & { { } \quad ( \tau ^ { \prime } \mathrm { ~ e ~ n ~ s ~ t ~ y ~ } } \end{array}
$$

对于二阶解， $\pmb { F } _ { 3 } ^ { \pm }$ 中的 $\pmb { g }$ 可直接换成 $g ^ { \prime }$ ，而 $\pmb { F _ { 2 } ^ { \ast } }$ 中 $\pmb { g }$ 换成 ${ \pmb g } ^ { \prime }$ 时应由下式表达：

$$
F _ { 2 } ^ { \ast } ( L ^ { \prime } , G ^ { \prime } , H ^ { \prime } , g ) = F _ { 2 } ^ { \ast } ( L ^ { \prime } , G ^ { \prime } , H ^ { \prime } , g ^ { \prime } ) + \frac { \partial F _ { 2 } ^ { \ast } } { \partial g ^ { \prime } } \bigg ( - \frac { \partial S _ { 1 } } { \partial G ^ { \prime } } \bigg )
$$

增加的一项可分成两个部分，即

$$
\frac { \partial F _ { 2 } ^ { * } } { \partial g ^ { \prime } } \Big ( - \frac { \partial S _ { 1 } } { \partial G ^ { \prime } } \Big ) = \Big \{ \frac { \partial F _ { 2 } ^ { * } } { \partial g ^ { \prime } } \Big ( - \frac { \partial S _ { 1 } } { \partial G ^ { \prime } } \Big ) \Big \} _ { e , l } + \Big \{ \frac { \partial F _ { 2 } ^ { * } } { \partial g ^ { \prime } } \Big ( - \frac { \partial S _ { 1 } } { \partial G ^ { \prime } } \Big ) \Big \} _ { s , }
$$

第一部分并入 $\pmb { F } _ { 3 } ^ { \ast }$ 中,而第二部分将在确定生成函数的 $\pmb { \ S _ { 3 } }$ 中作出贡献．因此， ${ \pmb { F } } ^ { \star }$ 完全符合要求，用Zeipel方法确实不会出现实质性困难。至于生成函数的问题，在 $\pmb { \mathscr { S } _ { 2 } }$ 部分建立的变换关系中， $\iota$ 和 $\pmb { g }$ 可直接换成 ${ \vec { \ell } } ^ { \prime }$ 和 ${ \pmb g } ^ { \prime }$ ；而在 $\pmb { \ S } _ { 1 }$ 建立的变换关系中， $\imath$ 和 $\pmb { g }$ 不再能直接改为 $l ^ { \prime }$ 和 ${ \pmb g } ^ { \prime }$ ；但也很容易解决这一问题，以 $L$ 和 $\imath$ 为例,类似于对 $\pmb { F _ { 2 } ^ { * } }$ 的处理，有

$$
\left. \begin{array} { r } { { L = L ^ { \prime } + \frac { \partial S _ { 1 } ( L ^ { \prime } , G ^ { \prime } , H ^ { \prime } , \ell ^ { \prime } , \ell ^ { \prime } , \ell ^ { \prime } , \ell } ) } { \partial l ^ { \prime } } + \frac { \partial S _ { 2 } ( L ^ { \prime } , G ^ { \prime } , H ^ { \prime } , \ell ^ { \prime } , \ell ^ { \prime } ) } { \partial l ^ { \prime } } } \\ { + \Bigg [ \frac { \partial ^ { 2 } S _ { 1 } } { \partial l ^ { \prime 2 } } \bigg ( - \frac { \partial S _ { 1 } } { \partial L ^ { \prime } } \bigg ) + \frac { \partial ^ { 2 } S _ { 1 } } { \partial g ^ { \prime } \partial l ^ { \prime } } \bigg ( - \frac { \partial S _ { 1 } } { \partial G ^ { \prime } } \bigg ) \Bigg ] } \\ { l = l ^ { \prime } - \frac { \partial S _ { 1 } ( L ^ { \prime } , G ^ { \prime } , H ^ { \prime } , l ^ { \prime } , g ^ { \prime } ) } { \partial L } - \frac { \partial S _ { 2 } ( L ^ { \prime } , G ^ { \prime } , H ^ { \prime } , l ^ { \prime } , g ^ { \prime } ) } { \partial L ^ { \prime } } } \\ { - \Bigg [ \frac { \partial ^ { 2 } S _ { 1 } } { \partial l ^ { \prime } \partial L ^ { \prime } } \bigg ( - \frac { \partial S _ { 1 } } { \partial L ^ { \prime } } \bigg ) + \frac { \partial ^ { 2 } S _ { 1 } } { \partial g ^ { \prime } \partial L ^ { \prime } } \bigg ( - \frac { \partial S _ { 1 } } { \partial G ^ { \prime } } \bigg ) \Bigg ] } \end{array} \right\}
$$

对于其它四个变量的变换关系有类似的表达式，问题全部解决，

# （2）第二次消除 ${ \pmb g } ^ { \prime }$ 的变换

与前面求一阶解过程相同，只是生成函数 $\pmb { \delta } ^ { * }$ 和相应的哈密顿函数 ${ \pmb { F } } ^ { * }$ 应增加 $\pmb { S _ { 2 } ^ { * } }$ 和 $\pmb { F _ { 3 } ^ { * } }$ 部分，根据展开式(7.198)可得

$$
\begin{array} { r l } & { \displaystyle { F _ { 3 } ^ { * * } = \frac { \partial F _ { 1 } ^ { * } } { \partial G ^ { \prime \prime } } \bigg ( \frac { \partial S _ { 2 } ^ { * } } { \partial g ^ { \prime } } \bigg ) + \frac { 1 } { 2 } \frac { \partial ^ { 2 } F _ { 1 } ^ { * } } { \partial G ^ { \prime \prime } } \bigg ( \frac { \partial S _ { 1 } ^ { * } } { \partial g ^ { \prime } } \bigg ) ^ { 2 } } } \\ & { \displaystyle { + \frac { \partial F _ { 2 } ^ { * } } { \partial G ^ { \prime \prime } } \bigg ( \frac { \partial S _ { 1 } ^ { * } } { \partial g ^ { \prime } } \bigg ) + F _ { 3 } ^ { * } ( L ^ { \prime } , G ^ { \prime \prime } , H ^ { \prime \prime } , g ^ { \prime } ) . } } \end{array}
$$

这同样可分成两个部分，即

$$
F _ { 3 } ^ { * * } = \left\{ \frac { 1 } { 2 } \frac { \partial ^ { 2 } F _ { 1 } ^ { * } } { \partial G ^ { \prime \prime 2 } } \Big ( \frac { \partial S _ { 1 } ^ { * } } { \partial g ^ { \prime } } \Big ) ^ { 2 } + \frac { \partial F _ { 2 } ^ { * } } { \partial G ^ { \prime \prime } } \Big ( \frac { \partial S _ { 1 } ^ { * } } { \partial g ^ { \prime } } \Big ) \right\} _ { \circ }
$$

$$
+ F _ { 3 c } ^ { * } ( L ^ { \prime \prime } , G ^ { \prime \prime } , H ^ { \prime \prime } ) = F _ { 3 } ^ { * * } ( L ^ { \prime \prime } , G ^ { \prime \prime } , H ^ { \prime \prime } ) ,
$$

$$
\begin{array} { l } { { \displaystyle 0 = \frac { \partial F _ { 1 } ^ { * } } { \partial G ^ { \prime \prime } } \Big ( \frac { \partial S _ { 2 } ^ { * } } { \partial g ^ { \prime } } \Big ) + \Big \{ \frac { 1 } { 2 } \frac { \partial ^ { 2 } F _ { 1 } ^ { * } } { \partial G ^ { \prime \prime 2 } } \Big ( \frac { \partial S _ { 1 } ^ { * } } { \partial g ^ { \prime } } \Big ) ^ { 2 } + \frac { \partial F _ { 2 } ^ { * } } { \partial G ^ { \prime \prime } } \Big ( \frac { \partial S _ { 1 } ^ { * } } { \partial g ^ { \prime } } \Big ) \Big \} _ { \textit { \xi } } } } \\ { { \displaystyle ~ + F _ { 3 \iota } ^ { * } ( L ^ { \prime \prime } , G ^ { \prime \prime } , H ^ { \prime \prime } , g ^ { \prime } ) . } } \end{array}
$$

由后一式确定的 $S _ { 2 } ^ { * }$ 与 $\pmb { \ S _ { 1 } ^ { * } }$ 类似,都是混合变量的函数，即

$$
S _ { 1 } ^ { * } = S _ { 1 } ^ { * } ( L ^ { \prime \prime } , G ^ { \prime \prime } , H ^ { \prime \prime } , g ^ { \prime } ) , ~ S _ { 2 } ^ { * } = S _ { 2 } ^ { * } ( L ^ { \prime \prime } , G ^ { \prime \prime } , H ^ { \prime \prime } , g ^ { \prime } ) .
$$

因此,变换后的新哈密顿函数 $F ^ { * * } { = } F ^ { * * } ( L ^ { \prime \prime } , G ^ { \prime \prime } , H ^ { \prime \prime } )$ 就二阶解而言已不存在换变量问题,而问题仅出现在由 $\ S ^ { * }$ 确定的新旧变量之间的关系中．与第一次消除 $\imath$ 的变换类似，也容易处理，举 $G ^ { \prime }$ 和$\cdot \pmb { g } ^ { \prime }$ 为例,有

$$
\left. \begin{array} { l } { { G ^ { \prime } = G ^ { \prime \prime } + \frac { \partial S _ { 1 } ^ { * } ( L ^ { \prime \prime } , G ^ { \prime \prime } , H ^ { \prime \prime } , g ^ { \prime \prime } ) } { \partial g ^ { \prime \prime } } + \frac { \partial S _ { 2 } ^ { * } ( L ^ { \prime \prime } , G ^ { \prime \prime } , H ^ { \prime \prime } , g ^ { \prime \prime } ) } { \partial g ^ { \prime \prime } } } } \\ { { \qquad + \frac { \partial ^ { 2 } S _ { 1 } ^ { * } } { \partial g ^ { \prime \prime 2 } } \Bigl ( - \frac { \partial S _ { 1 } ^ { * } } { \partial G ^ { \prime \prime } } \Bigr ) , } } \\ { { g ^ { \prime } = g ^ { \prime \prime } - \frac { \partial S _ { 1 } ^ { * } ( L ^ { \prime \prime } , G ^ { \prime \prime } , H ^ { \prime \prime } , g ^ { \prime \prime } ) } { \partial G ^ { \prime \prime } } - \frac { \partial S _ { 2 } ^ { * } ( L ^ { \prime \prime } , G ^ { \prime \prime } , H ^ { \prime \prime } , g ^ { \prime \prime } ) } { \partial G ^ { \prime \prime } } } } \\ { { \qquad - \frac { \partial ^ { 2 } S _ { 1 } ^ { * } } { \partial g ^ { \prime \prime } \partial G ^ { \prime \prime } } \Bigl ( - \frac { \partial S _ { 1 } ^ { * } } { \partial G ^ { \prime \prime } } \Bigr ) . } } \end{array} \right\}
$$

对其它变量亦如此.

从两次变换中处理混合变量的过程来看，尽管Zeipel方法是引用隐函数定义的正则变换，但就应用而言，不含给构造小参数幂级数解带来原则性的困难，具体实现混合变量的转换也并不麻烦.整个消除角坐标的变换过程都是由低阶项确定高阶项，形成一个“良性”的递推过程,方法确实可行。不难看出,如果原哈密顿函数$\pmb { F }$ 存在 $F _ { 2 } , F _ { 3 }$ 等高阶项，也不会给变换带来任何困难．至于 $\pmb { F }$ 显含 $\pmb { t }$ 又含 $\pmb { h }$ ，上述方法是否可用，下面通过同时考虑主要田谐项$( J _ { 2 , 2 } )$ 的摄动来说明这一问题.

# 5．同时考虑 $\mathbf { J _ { 2 } }$ 项和 $\mathbf { J _ { 2 , 2 } }$ 项的情况

此时，原哈密顿函数为

$$
\begin{array} { r l } & { F { = } F _ { 0 } ( L ) + F _ { 1 e } ( L , G , H ) + F _ { 1 \mathscr { s } } ( L , G , H , l , g ) } \\ & { \qquad + F _ { 2 \mathscr { s } } ( L , G , H , l , g , h ; t ) . } \end{array}
$$

其中 $\pmb { \mathcal { F } } _ { 2 } s$ 是 $\boldsymbol { J } _ { 2 , 2 }$ 项对应的摄动函数，一般情况下它属于二阶短周期部分，具体形式请看第五章 $\ S 5 . 7 .$ ，由于 $\pmb { F } _ { 2 } s$ 显含 $\pmb { \ell }$ 又同时含角变量 $\hslash$ ，这就使得在第一次消除 $l$ 的变换中，确定 $\pmb { S _ { 2 } }$ 和 $\pmb { F } _ { 3 } ^ { * }$ 的表达式分别变为下列形式：

$$
\left. \begin{array} { c } { { 0 = \displaystyle \frac { \partial F _ { 0 } } { \partial { \cal L } ^ { \prime } } \bigg ( \frac { \partial S _ { 2 } } { \partial l } \bigg ) - \frac { \partial S _ { 2 } } { \partial t } + \left\{ \frac { 1 } { 2 } \frac { \partial ^ { 2 } F _ { 0 } } { \partial { \cal L } ^ { \prime 2 } } \bigg ( \frac { \partial S _ { 1 } } { \partial l } \bigg ) ^ { 2 } + \frac { \partial F _ { 1 } } { \partial { \cal L } ^ { \prime } } \bigg ( \frac { \partial S _ { 1 } } { \partial l } \bigg ) \right. } } \\ { { \displaystyle \left. + \frac { \partial F _ { 1 } } { \partial { \cal G } ^ { \prime } } \bigg ( \frac { \partial S _ { 1 } } { \partial g } \bigg ) \right\} _ { s } + \dot { F } _ { 2 s } ( { \cal L } ^ { \prime } , { \cal G } ^ { \prime } , { \cal H } ^ { \prime } , l , g , h ; t ) , } } \\ { { \displaystyle \mathcal { H } _ { 3 } ^ { * } = \{ { \cal F } _ { 3 } ^ { * } \} + \left\{ \frac { \partial F _ { 2 s } } { \partial { \cal L } ^ { \prime } } \bigg ( \frac { \partial S _ { 1 } } { \partial l } \bigg ) + \frac { \partial F _ { 2 s } } { \partial { \cal G } ^ { \prime } } \bigg ( \frac { \partial S _ { 1 } } { \partial g } \bigg ) + \frac { \partial F _ { 1 } } { \partial { \cal H } ^ { \prime } } \bigg ( \frac { \partial S _ { 2 } } { \partial h } \bigg ) \right\} _ { c , l } } }  \end{array} \right\}
$$

${ \pmb { F } } _ { 3 } ^ { * }$ 右端第一大项 $\{ F _ { 3 } ^ { * } \}$ 为(7.220)式右端部分，这里从略。计算 $\pmb { F } _ { 3 } ^ { * }$ 并无困难，而 $\pmb { \mathcal { S } _ { 2 } }$ 的确定将涉及如何求解一个偏微分方程问题．事实上， $\pmb { S _ { 2 } }$ 可以分解成两个部分： ${ \cal S } _ { 2 } = ( { \cal S } _ { 2 } ) _ { 1 } + ( { \cal S } _ { 2 } ) _ { 2 } , ( { \cal S } _ { 2 } ) _ { 1 }$ 不显含 $t$ ，而 $( { \pmb S } _ { 2 } ) _ { 2 }$ 为显含 $\pmb { t }$ 的部分，前者与 $\pmb { F _ { 2 , \delta } }$ 无关,仅由 $\scriptstyle { \pmb J } _ { 2 } ^ { 2 }$ 项组成，确定方法同前。后者当然与 $\pmb { F _ { 2 , s } }$ 有关，而 $\pmb { F _ { 2 , s } }$ 却是以 $l , g , h$ 和 $\pmb { t }$ 作为幅角的三角函数的线性组合，为了说明问题，不妨就将 $\pmb { F _ { 2 , g } }$ 写成如下形式：

$\begin{array} { r } { F _ { 2 S } = J _ { 2 , 2 } A ( L , G , H ) \cos { ( k _ { 1 } l + k _ { 2 } g + k _ { 3 } h + k _ { 4 } n _ { e } t ) } } \end{array}$ (7.230)其中 $\pmb { n _ { e } }$ 是地球自转角速度， $\check { \pmb { k } } _ { 1 } , \pmb { k } _ { 2 } , \pmb { k } _ { 3 } , \pmb { k } _ { 4 }$ 均为正负整数(包括零).于是, $( S _ { 2 } ) _ { 2 }$ 由下列一阶线性偏微分方程确定

$$
\pi ^ { \prime } \frac { \partial ( S _ { 2 } ) _ { 2 } } { \partial l } + \frac { \partial ( S _ { 2 } ) _ { 2 } } { \partial t } = J _ { 2 , 2 } A ^ { \prime } \cos \left( k _ { 1 } l + k _ { 2 } g + k _ { 3 } h + k _ { 4 } n _ { e } t \right)
$$

其中 $n { = } L ^ { \prime - 3 }$ ， $A ^ { \prime } { = } A ( L ^ { \prime } , G ^ { \prime } , H ^ { \prime } )$ ，此方程很易求解，显然有

$$
( S _ { 2 } ) _ { 2 } = \frac { J _ { 2 , 2 } A ^ { \prime } \sin \left( k _ { 1 } l + k _ { 2 } g \cdot ^ { \cdot } k _ { 3 } h + k _ { 4 } n _ { e } t \right) } { k _ { 1 } n ^ { \prime } + k _ { 4 } n _ { e } } .
$$

如果 $\pmb { F }$ 显含 $t$ ，或同时含有两个角变量 ${ \pmb g } ^ { \prime }$ 和 $\hbar ^ { \prime }$ 的情况在第二次变换中出现，处理方法同上，没有任何困难，因为同样只涉及到最简单的类似(7.231)式的一阶线性偏微分方程.

与第五章用平均根数法求摄动解的情况一样，显含 $\pmb { t }$ 的问题可导致小分母的出现，即(7.232)式右端分母为零：

$$
\vec { k } _ { 1 } n ^ { \prime } + k _ { 4 } n _ { e } = 0 ,
$$

或

$$
\frac { n ^ { \prime } } { n _ { e } } = \frac { - k _ { 4 } } { k _ { 1 } } .
$$

# 6.引用Zeipel方法的条件

从前面几段的讨论过程可以看出，如果原哈密顿系统的 ${ \boldsymbol { { \mathit { T } } } } _ { 1 }$ 包含 $\pmb { F } _ { \mathrm { i } \mathrm { \Delta } } \triangleq \pmb { 0 }$ ，或变换过程中出现- =0(即1-5cos²i'=0),n'/n$= - k _ { 4 } / k _ { 1 }$ 这类通约情况，级数解的构造将出现问题，但是只要 $\pmb { F } _ { 1 l } ,$ $( 1 - 5 \cos ^ { 2 } i ^ { \prime } )$ ， $( k _ { 1 } n ^ { \prime } + k _ { 4 } n _ { e } ) / n ^ { \prime }$ 的量级不超过 $\mu ^ { 1 / 2 } ( \mu$ 是它们的对应项或含有这些因子项的量级)，方法还是可行的。关于这一点，作为一个习题让读者去验证,其原因将在后面第8节中阐明.

对于自然天体的运动情况，其相应的哈密顿函数 $\pmb { F }$ 通常并不象人造地球卫星运动那样,清楚地分成 $F _ { 0 } , F _ { 1 c } , F _ { 1 s } , \cdots ,$ 往往有类似 ${ { \pmb { F } } _ { 1 l } }$ 的部分和通约项出现,因此，当Zeipel方法于1916年提出后，在具体应用方面并未引起太多的重视，而在人造卫星运动中却用得相当成功.

尽管Zeipel方法在具体应用上(符合一定条件)并无困难，但毕竟有个换变量问题，这是一缺陷;而若采用堀源一郎和德普里先后给出的Lie变换，就可避免这一点，不妨称此方法为Hori-Deprit方法，下一节将用它来构造人造卫星摄动运动方程的级数解。

# 7.7 Hori-Deprit方法

仍然引用德洛纳变量 $L , G , H , l , g , h$ 作为基本变量，并分别将新旧正则共轭变量记为 $P , Q$ 和 $p , q ,$ 即

$$
\begin{array} { r } { p = \left( \begin{array} { c c c } { L } \\ { G } \\ { H } \end{array} \right) , \qquad q = \left( \begin{array} { c c c } { l ^ { \prime } } \\ { g } \\ { h } \end{array} \right) , } \\ { P = \left( \begin{array} { c c c } { L ^ { \prime } } \\ { G ^ { \prime } } \\ { H ^ { \prime } } \end{array} \right) , \quad Q = \left( \begin{array} { c c c } { l ^ { \prime } } \\ { g ^ { \prime } } \\ { h ^ { \prime } } \end{array} \right) . } \end{array}
$$

根据 $\yen 12$ 变换(7.81)式或显含一 $t$ 的形式(7.93)式，有

$$
\left. \begin{array} { l } { { p { = } E _ { \scriptscriptstyle \mathrm { F } } ( P ) { = } \displaystyle { \sum _ { n = 0 } ^ { \infty } } { \frac { \varepsilon ^ { n } } { n ! } } P ^ { \scriptscriptstyle ( n ) } \left( P , Q , t ; 0 \right) { , } } } \\ { { { } } } \\ { { q { = } E _ { \scriptscriptstyle \mathrm { W } } ( Q ) { = } \displaystyle { \sum _ { n = 0 } ^ { \infty } } { \frac { \varepsilon ^ { n } } { n ! } } Q ^ { \scriptscriptstyle ( n ) } \left( P , Q , t ; 0 \right) { . } } } \end{array} \right\}
$$

下面要讨论的问题所对应的母函数 $W ( P , Q , t ; \varepsilon )$ 和哈密顿函数$\pmb { F } ( p , i j , \ell ; \varepsilon )$ 皆可展为小参数 $\pmb { \varepsilon }$ 的幂级数，即

$$
\left. \begin{array} { l } { { W ( P , Q , t ; \varepsilon ) = { \displaystyle \sum _ { n = 0 } ^ { \infty } } \frac { \varepsilon ^ { n } } { n ! } } W _ { n + 1 } ( P , Q , t ) , }  \\ { { } } \\ { { F ( p , q , t ; \varepsilon ) = { \displaystyle \sum _ { n = 0 } ^ { \infty } } \frac { \varepsilon ^ { n } } { n ! } } F _ { n } ( p , q , t ) . }  \end{array} \right\}
$$

根据(7.92)式，变换关系(7.235)式中的系数P(")和Q(")可具体写出，即

$$
\left. \begin{array} { r l } & { P ^ { ( i ) } = P , } \\ & { P ^ { ( i ) } = L _ { 1 } P } \\ & { \quad = \{ P ; W _ { 1 } \} = \frac { \partial W _ { i } } { \partial Q } , } \\ & { P ^ { ( i ) } = L _ { 2 } P + L _ { 1 } ^ { \dagger } P } \\ & { \quad \approx \frac { \partial W _ { 2 } } { \partial Q } + \left\{ \frac { \partial W _ { 1 } } { \partial Q } ; W _ { 1 } \right\} , } \\ & { \quad \left. \partial ^ { ( i ) } = L _ { 3 } P + L _ { 4 } P + 2 L _ { 1 } L _ { 2 } P + L _ { 1 } ^ { 3 } P \right. } \\ & { \quad \quad \approx \frac { \partial W _ { 3 } } { \partial Q } + \left\{ \frac { \partial W _ { 4 } } { \partial Q } ; W _ { 3 } \right\} + 2 \left\{ \frac { \partial W _ { 1 } } { \partial Q } ; W _ { 1 } \right\} + \left\{ \left\{ \frac { \partial W _ { 1 } } { \partial Q } ; W _ { 1 } \right\} ; W _ { 1 } \right\} . } \end{array} \right\}
$$

$$
 \begin{array} { r l } & { Q ^ { ( k ) } = Q _ { r } , } \\ & { ( \theta ^ { ( k ) } = L _ { s } Q ) } \\ & { = \langle Q ; W _ { s } \rangle = - \frac { \partial W _ { 1 } } { \partial P } , } \\ & { Q ^ { ( 2 ) } = L _ { s } Q + L _ { s } ^ { ( 2 ) } = L _ { s } Q } \\ & { \qquad = - \frac { \partial W _ { 1 } } { \partial P } + \frac { \partial W _ { 1 } } { \partial P } , W _ { 1 } \Bigg \rangle , } \\ & { Q ^ { ( 3 ) } = L _ { s } Q - L _ { s } L _ { s } Q + 2 L _ { s } L _ { s } Q , \langle L _ { s } ^ { ( 2 ) } L _ { s } Q \rangle } \\ & { \qquad = - \frac { \partial W _ { 3 } } { \partial P } + \underbrace { \{ - \frac { \partial W _ { 1 } } { \partial P } , \frac { 1 } { \partial P } \} \cdot \partial ^ { 2 } } _ { = P _ { s } P _ { s } } \langle - \frac { \partial W _ { 2 } } { \partial P } ; W _ { s } \rangle } \\ & { \qquad + \{ \{ - \frac { \partial W _ { 1 } } { \partial P } , \frac { 1 } { \partial P } \} \cdot W _ { 1 } \Bigg \} , W _ { 1 } \Bigg \} , } \end{array} \}
$$

其 $\frac { { \hat { c } } ^ { W } { } _ { \eta } } { { \hat { \sigma } } P } , \frac { { \hat { \sigma } } W _ { \eta } } { \partial Q }$ 是三维列向量，即

$$
\frac { \partial W _ { n } } { \partial P } = \left( \begin{array} { c } { \frac { \partial W _ { n } } { \partial L ^ { ' } } } \\ { \frac { \partial W _ { n } } { \partial G ^ { ' } } } \\ { \frac { \partial W _ { n } } { \partial G ^ { ' } } } \end{array} \right) , \frac { \partial W _ { n } } { \partial Q } = \left( \begin{array} { c } { \frac { \partial W } { \partial l ^ { ' } } } \\ { \frac { \partial W _ { n } } { \partial g ^ { ' } } } \\ { \frac { \partial W _ { n } } { \partial h ^ { ' } } } \end{array} \right) .
$$

按变换关系(7.82)式和正则变换的余函数表达式(7.94)，经变换(7.235)，新哈密顿函数 $F ^ { * } ( P , Q , t ; \varepsilon )$ 为

$$
F ^ { \ast } ( P , Q , t ; \varepsilon ) = F \left( \mathcal { P } ( P , Q , t ; \varepsilon ) , \ q ( P , \ Q , \ t ; \ \varepsilon ) , \ t ; \ \varepsilon \right) \ \ast
$$

$$
R ( P , Q , t ; \varepsilon ) = \sum _ { n = 0 } ^ { \infty } \frac { \varepsilon ^ { n } } { n ! } F ^ { ( n ) } \left( P , Q , t , 0 \right) - \sum _ { n = 1 } ^ { \infty } \frac { \varepsilon ^ { n } } { n ! } R ^ { ( n ) } \left( P , Q , t , 0 \right) .
$$

按递推关系(7.90)，(7.91)和(7.95)式，系数 $\pmb { F } ^ { ( n ) }$ 和 $\pmb { R } ^ { ( n ) }$ 的具体形式为

$$
\left. \begin{array} { r l } & { F ^ { ( 0 ) } { = } F _ { 0 } ( P , Q , t ) , } \\ & { F ^ { ( 1 ) } { = } L _ { 1 } F _ { 0 } { + } F _ { 1 } ( P , Q , t ) , } \\ & { F ^ { ( 2 ) } { = } L _ { 2 } F _ { 0 } { + } L _ { 1 } ^ { 2 } F _ { 0 } { + } 2 L _ { 1 } F _ { 1 } { + } F _ { 2 } ( P , Q , t ) , } \\ & { F ^ { ( 3 ) } { = } L _ { 3 } F _ { 0 } { + } \left( L _ { 1 } ^ { 3 } { + } 2 L _ { 1 } L _ { 2 } { + } L _ { 2 } L _ { 1 } \right) F _ { 0 } { \div } \left( 3 L _ { 1 } ^ { 2 } { + } 3 L _ { 2 } \right) F _ { 1 } , } \\ & { ~ + \left. 3 L _ { 1 } F _ { 2 } { + } F _ { 2 } ( P , Q , t ) , \right. } \\ & { . . . . . . . . . } \\ & { . . . . . . . . } \end{array} \right\}
$$

$$
\begin{array} { r l } & { R ^ { ( 1 ) } = \cfrac { \partial V _ { 1 } } { \partial t } } \\ & { R ^ { ( 2 ) } = \cfrac { \partial W _ { 2 } } { \partial t } + L _ { 1 } \bigg ( \cfrac { \partial W _ { 1 } } { \partial t } \bigg ) , } \\ & { R ^ { ( 3 ) } = \cfrac { \partial W _ { 3 } } { \partial t } + L _ { 2 } \bigg ( \cfrac { \partial W _ { 1 } } { \partial t } \bigg ) + L _ { 1 } ^ { 2 } \bigg ( \cfrac { \partial W _ { 1 } } { \partial t } \bigg ) + 2 L _ { 1 } \bigg ( \cfrac { \partial W _ { 2 } } { \partial t } \bigg ) , } \\ & { \cdots \cdots \cdots . } \end{array} \quad \left( \begin{array} { r } { \medskip } \\ { \medskip } \\ { \medskip } \end{array} \right.
$$

讨论人造地球卫星的轨道变化时，常用 $\pmb { J } _ { 2 }$ 作为小参数 $\pmb { \varepsilon }$ ，因

此,相应的哈密顿函数的写法应为

$$
F ( p , q , t ; \varepsilon ) = F _ { 0 } + J _ { 2 } F _ { 1 } + \frac { J _ { 2 } ^ { 2 } } { 2 } F _ { 2 } + \cdots ,
$$

其中

$$
\scriptstyle \left. { \begin{array} { l } { F _ { 0 } = { \frac { 1 } { 2 L ^ { 2 } } } , } \\ { F _ { 1 } = F _ { \tau \sigma } { \frac { 1 } { r } } F _ { 1 s } } \\ { \scriptstyle = { \frac { 1 } { 2 L ^ { 6 } } } { \bar { A } } ( L / G ) ^ { 3 } + { \frac { 1 } { 2 L ^ { 6 } } } \left\{ A \left[ \left( { \frac { a } { r } } \right) ^ { 3 } - ( L / G ) ^ { 3 } \right] \right\} } \\ { \scriptstyle \cdot \quad + B \left( { \frac { a } { r } } \right) ^ { 3 } \cos 2 ( f + g ) { \Big \} } \\ { \scriptstyle \ldots \ldots \ldots } . } \end{array} } \right.
$$

$\pmb { A }$ 和 $\pmb { B }$ 的表达式仍为(7.164)式．关于 $\pmb { J _ { 3 } } , \pmb { J _ { 4 } }$ 等二阶小量对应的$\pmb { F _ { 2 } }$ 应将原式系数 ${ \pmb J } _ { 3 } , { \pmb J } _ { 4 }$ 等相应地改为 $ { { J } _ { 3 } } \middle / { ( \frac { J _ { 2 } ^ { 2 } } { 2 } ) } , { { J } _ { 4 } } \middle / { ( \frac { J _ { 2 } ^ { 2 } } { 2 } ) } , \cdots ,$ 至于三阶或更高阶部分,亦有类似写法，不再一一列举。

下面仍以 $\pmb { J _ { 2 } }$ 项摄动的一阶解为例，介绍Lie变换的具体用法．此时哈密顿函数不显含 $\pmb { t }$ ，相应的母函数亦如此．（7.243）式简化为

$$
F ( p , q ; \varepsilon ) = F _ { 0 } + J _ { 2 } F _ { 1 } , F _ { n } = 0 ( n { \geqslant } 2 ) .
$$

构造级数解的过程与Zeipel方法类似，分两步逐一消除快变量$\pmb { l }$ 和慢变量 ${ \pmb g } .$

# 1.消除 $\pmb { l }$ 的过程

显然可以假定母函数 $\boldsymbol { W } = \boldsymbol { W } \left( \boldsymbol { L } ^ { \prime } , \boldsymbol { G } ^ { \prime } , \boldsymbol { H } ^ { \prime } , \boldsymbol { l } ^ { \prime } , \boldsymbol { g } ^ { \prime } ; \varepsilon \right)$ ，由（7.237)和(7.238)式给出变换关系为

$$
\left. \begin{array} { l l } { { L = L ^ { \prime } + J _ { 2 } \displaystyle \frac { \partial W _ { 1 } } { \partial l ^ { \prime } } , ~ l = l ^ { \prime } - J _ { 2 } \displaystyle \frac { \partial W _ { 1 } } { \partial L ^ { \prime } } , } } \\ { { } } & { { } } \\ { { G = G ^ { \prime } + J _ { 2 } \displaystyle \frac { \partial W _ { 1 } } { \partial g ^ { \prime } } , ~ g = g ^ { \prime } - J _ { 2 } \displaystyle \frac { \partial W _ { 1 } } { \partial G ^ { \prime } } , } } \\ { { } } & { { } } \\ { { H = H ^ { \prime } } } & { { h = h ^ { \prime } - J _ { 2 } \displaystyle \frac { \partial W _ { 1 } } { \partial H ^ { \prime } } . } } \end{array} \right\}
$$

变换后的新哈密顿函数为

$$
F ^ { * } { = } F ^ { ( 0 ) } + \mathcal { J } _ { 2 } F ^ { ( 1 ) } { + } \frac { \mathcal { J } _ { 2 } ^ { 2 } } { 2 } F ^ { ( 2 ) } { + } \cdots ,
$$

其中

$$
\left. \begin{array} { l } { { F ^ { ( 0 ) } = F _ { 0 } ( L ^ { \prime } ) , \qquad \mathrm { . } } } \\ { { F ^ { ( 1 ) } = \displaystyle \frac { \partial F _ { 0 } } { \partial L ^ { \prime } } \displaystyle \{ \frac { \partial W _ { 1 } } { \partial l ^ { \prime } } \biggr ) + F _ { 1 c } ( L ^ { \prime } , G ^ { \prime } , H ^ { \prime } ) + F _ { 1 s } ( L ^ { \prime } , G ^ { \prime } , H ^ { \prime } , l ^ { \prime } , g ^ { \prime } ) , \left\} \right\} } } \\ { { F ^ { ( 2 ) } = \displaystyle \frac { \partial F _ { 0 } } { \partial L ^ { \prime } } \displaystyle \{ \frac { \partial W _ { 1 } } { \partial l ^ { \prime } } \biggr ) + \left\{ \displaystyle \frac { \partial F _ { 0 } } { \partial L ^ { \prime } } \displaystyle \Bigl ( \frac { \partial W _ { 1 } } { \partial l ^ { \prime } } \biggr ) ; W _ { 1 } \right\} + 2 \langle F _ { 1 } ; W _ { 1 } \} . } } \end{array} \right.
$$

类似Zeipel方法，不难给出满足消除 $\downarrow ^ { \prime }$ 的 $\pmb { F } ^ { \star }$ 和确定 $\pmb { W }$ 的关系式，即

$$
F _ { 0 } ^ { * } = F _ { 0 } ( L ^ { \prime } ) = { \frac { 1 } { 2 L ^ { \prime 2 } } } ,
$$

$$
F _ { 1 } ^ { * } = F _ { 1 \circ } ( L ^ { \prime } , G ^ { \prime } , H ^ { \prime } ) = \frac { A ^ { \prime } } { 2 L ^ { \prime 3 } G ^ { \prime 3 } } ,
$$

$$
\begin{array} { l } { { { \cal F } _ { 2 } ^ { * } = [ \{ - { \cal F } _ { 1 s } ; { \cal W } _ { 1 } \} + 2 \{ { \cal F } _ { 1 } ; { \cal W } _ { 1 } \} ] _ { c \ast \imath } } } \\ { { { } } } \\ { { = [ \{ { \cal F } _ { 1 } + { \cal F } _ { 1 c } ; { \cal W } _ { 1 } \} ] _ { c \ast \imath } } } \end{array}
$$

$$
\frac { \partial W _ { 1 } } { \partial l ^ { \prime } } { = } - F _ { 1 s } \mathord { \left/ { \vphantom { \partial F _ { 1 s } ^ { \prime } } } \right. \kern - delimiterspace } \frac { \partial F _ { 0 } } { \partial L ^ { \prime } } ,
$$

$$
\frac { \partial W _ { 2 } } { \partial l ^ { \prime } } = - [ \left\{ F _ { 1 } + F _ { \mathit { 1 c } } ; W _ { 1 } \right\} ] _ { s } \bigg / \frac { \partial F _ { 0 } } { \partial L ^ { \prime } }
$$

确定 $\mathbf { \varPsi } _ { \mathbf { \lambda } }$ 的(7.252)式与前面确定 $\pmb { S } _ { 1 }$ 的(7.180)式在形式上仅差一个系数 $\boldsymbol { J } _ { 2 }$ ，积分得

$$
\begin{array} { l } { { \displaystyle { W _ { 1 } = \frac { 1 } { 2 G ^ { \prime 3 } } \bigg \{ A ^ { \prime } [ ( f ^ { \prime } - l ^ { \prime } ) + e ^ { \prime } \sin f ^ { \prime } ] } } } \\ { { \displaystyle ~ + B ^ { \prime } \bigg [ \frac { e ^ { \prime } } { 2 } \sin \left( f ^ { \prime } + 2 g ^ { \prime } \right) + \frac { 1 } { 2 } \sin 2 \left( f ^ { \prime } + g ^ { \prime } \right) } } \\ { { \displaystyle ~ + \frac { e ^ { \prime } } { 6 } \sin \left( 3 f ^ { \prime } + 2 g ^ { \prime } \right) \bigg ] \bigg \} } } \end{array}
$$

对于一阶解，剩下的只是计算(7.251)式的右端项，有

$$
\begin{array} { r } { \{ F _ { 1 } + F _ { 1 c } ; W _ { 1 } \} = \frac { \partial ( F _ { 1 } + F _ { 1 c } ) } { \partial L ^ { \prime } } \frac { \partial W _ { 1 } } { \partial l ^ { \prime } } - \frac { \partial ( F _ { 1 } + F _ { 1 c } ) } { \partial l ^ { \prime } } \frac { \partial W _ { 1 } } { \partial L ^ { \prime } } } \\ { + \frac { \partial ( F _ { 1 } + F _ { 1 c } ) } { \partial G ^ { \prime } } \frac { \partial W _ { 1 } } { \partial g ^ { \prime } } - \frac { \partial ( F _ { 1 } + F _ { 1 c } ) } { \partial g ^ { \prime } } \frac { \partial W _ { 1 } } { \partial G ^ { \prime } } , } \end{array}
$$

用求平均值的方法给出

$$
\begin{array} { r l } & { \Big \{ \frac { \tilde { \partial } ( F _ { 1 } + \overline { { F } } _ { \epsilon } ) } { \partial \tilde { L } ^ { \prime } } \frac { \partial \Psi _ { 1 } } { \partial \tilde { L } ^ { \prime } } \Big \} _ { \epsilon = 0 } - \frac { 1 } { 2 } \frac { \tilde { \partial } F _ { 1 } \partial \tilde { W } _ { 1 } } { \partial \tilde { L } ^ { \prime } } \Big \} _ { \epsilon \to \pi ^ { 2 } } } \\ & { \qquad \div \frac { 1 } { 4 L ^ { 2 \epsilon } } \Big \{ \tilde { L } ^ { 4 \epsilon / 2 } \Big [ \Big ( \frac { \tilde { \partial } } { 2 } - \frac { 2 \tilde { \mathcal { L } } ^ { 2 } } { 4 } \epsilon ^ { 2 } - \frac { 2 1 } { 1 6 } \theta ^ { 4 } \Big ) ( 1 - \theta ^ { * } ) ^ { * } \Big \cdot } \\ & { \qquad + 3 ( 1 - \epsilon ^ { * } ) ) ^ { * } \Big ] } \\ & { \qquad + B ^ { * } \Big [ \bigg ( \frac { 3 } { 4 } - \frac { 2 7 } { 8 } \epsilon ^ { 2 } - \frac { 2 1 } { 3 2 } \epsilon ^ { \prime 4 } \Big ) ( 1 - \theta ^ { * 2 } ) ^ { * } \Big \cdot } \\ & { \qquad + A B ^ { * } \Big [ \Big ( \frac { 3 } { 4 } - \frac { 1 3 } { 2 } \delta ^ { * 2 } - \frac { 2 1 } { 4 } \epsilon ^ { \prime 4 } \Big ) ( 1 - \epsilon ^ { \prime 2 } ) ^ { * } \Big \cdot \Big ] _ { \epsilon \in \Omega } } \\ & { \qquad + A B ^ { * } \Big [ \Big ( \frac { 1 } { 3 } \epsilon ^ { 2 } - \frac { 1 3 } { 2 } \epsilon ^ { \prime 2 } - \frac { 7 } { 4 } \epsilon ^ { \prime 4 } \Big ) ( 1 - \epsilon ^ { \prime 2 } ) ^ { * } \Big ] _ { \epsilon \to \pi ^ { 2 } } \Big \{ \epsilon ^ { \prime } } \\ & { \qquad + B ^ { * } \Big [ 2 \bigg ( \frac { 1 } { 1 6 } \epsilon ^ { \prime \prime } - \frac { 7 } { 6 4 } \epsilon ^ { \prime \prime } \Big ) ( 1 - \epsilon ^ { \prime 2 } ) ^ { * } \Big ] _ { \epsilon \to \pi ^ { 4 } } { \epsilon } ^ { \prime } \Big \} ; } \\ &  \qquad + \frac { \tilde { \partial } ^ { 2 } \Big ( \epsilon ^ { \prime } \Big ) } { \epsilon \to \pi ^ { 6 } } , \end{array}
$$

$$
\begin{array} { r l } & { \quad + A ^ { \mathcal { H } } \mathcal { H } \left( \left[ \frac { \partial } { \partial \mathbf { r } } \frac { \partial \mathbf { r } } { \partial \mathbf { \theta } } \right] - \frac { \partial ^ { 2 } \mathbf { r } } { \partial \mathbf { \theta } } \right) ^ { 2 } \left[ \left( \mathbf { a } - \mathbf { r } ^ { \prime } \right) ^ { 2 } - \frac { \partial ^ { 2 } \mathbf { r } } { \partial \mathbf { r } } \right] \sin \mathbf { r } \cdot \mathbf { z } ^ { \prime } \Bigr \} } \\ & { \quad + B ^ { 2 } \left[ \left( \frac { \partial } { \partial \mathbf { r } } \frac { \partial \mathbf { r } } { \partial \mathbf { \theta } } \right) ^ { 2 } - \frac { \partial ^ { 2 } \mathbf { r } } { \partial \mathbf { r } } \right] \left( \mathbf { a } - \mathbf { r } ^ { \prime } \right) ^ { 2 } \Biggr ] \sin \mathbf { r } \cdot \mathbf { z } ^ { \prime } \Biggr \} ; } \\ & { \quad - \left[ \frac { \partial } { \partial \mathbf { r } } \frac { \partial \mathbf { r } } { \partial \mathbf { r } } \frac { \partial \mathbf { r } } { \partial \mathbf { \theta } } \right] \frac { \partial \mathbf { r } } { \partial \mathbf { r } } \Biggr \} _ { \mathbf { \theta } = - \mathbf { r } ^ { \prime } \mathbf { \theta } } - \left. \frac { \partial } { \partial \mathbf { r } } \frac { \partial \mathbf { r } } { \partial \mathbf { \theta } } \right. \frac { \partial \mathbf { r } } { \partial \mathbf { \theta } } \right] } \\ & { \quad - \frac { 1 } { 4 A ^ { 2 } } \gamma ( \mathbf { a } - \mathbf { r } ^ { \prime } ) ^ { 2 } \frac { \partial \mathbf { r } } { \partial \mathbf { \theta } } \left. \mathbf { a } ^ { 2 } \right. } \\ & { \quad \left( \frac { \partial } { \partial \mathbf { r } } \frac { \partial \mathbf { r } } { \partial \mathbf { \theta } } \right) ^ { 2 } \frac { \partial } { \partial \mathbf { r } } \left. \mathbf { a } ^ { 2 } \right. } \\ &  \quad + B ^ { 2 } \gamma \left. \left( \frac { \partial } { \partial \mathbf { r } } \frac { \partial \mathbf { r } } { \partial \mathbf { \theta } } \right) ^ { 2 } \left( \mathbf { a } - \mathbf { r } ^ { \prime } \right) - \frac { \partial } { \partial \mathbf { r } } \frac { \partial } { \partial \mathbf { r } } \frac { \partial \mathbf { r } }  \ \end{array}
$$

$$
\begin{array} { r l } & { \quad [ \frac { \partial ( F _ { + } , \bar { x } ^ { \prime } ) } { \partial G ^ { \prime } } \frac { \partial W _ { 1 } ^ { \prime } } { \partial \phi ^ { \prime } } ] _ { , \omega = \frac { 1 } { 2 } } } \\ & { = - \frac { 1 } { 8 \tilde { L } ^ { 2 ( \Omega ) } } B ^ { \prime } ( 1 - e ^ { \omega ^ { \prime } \epsilon ^ { 2 } ) - s \cdot 2 s ^ { \prime } } [ ( 1 - \tilde { \mathcal { B } } \frac { H ^ { \prime \prime } } { G ^ { \prime } } ) ] \omega s _ { 0 2 } \tilde { \mathcal { A } } ^ { \prime } \textrm { P o s } 2 \tilde { \mathcal { A } } ^ { \prime } ] } \\ & { \quad + \frac { 3 } { 8 \tilde { L } ^ { 2 ( \Omega ) } } B ^ { \prime } ( \frac { H ^ { \prime \prime } } { G ^ { \prime } } ) ( 1 - e ^ { \omega ^ { \prime } \epsilon ^ { 2 } \pi ^ { 2 } } ) [ ( 1 + \frac { 2 } { \tilde { \mathcal { B } } } e ^ { \pi ^ { 2 } } ) - e ^ { \kappa ^ { 3 } \cos 2 \theta \tilde { \mathcal { A } } ^ { \prime } } ] } \\ & { \quad - \frac { 1 } { 4 \tilde { L } ^ { 2 ( \Omega ) } } ( 1 - e ^ { \kappa ^ { 3 } \pi ^ { 2 } } ) \exp [ \pi ^ { 2 } ( \frac { 1 } { 6 } + \frac { 2 } { 8 } e ^ { \kappa ^ { 6 } } )  } \\ & { \quad  + A ^ { \prime } B ^ { \prime } ( 3 + \frac { 4 } { 4 } e ^ { \kappa ^ { 7 } } ) \omega 2 g ^ { \prime } g ^ { \prime } ] \omega 2 g ^ { \prime } \frac { \tilde { \mathcal { A } } ^ { \prime } } { 1 6 } ( \frac { 1 } { 1 6 } e ^ { \sigma ^ { \prime } } ) \omega s _ { 0 4 } \tilde { \mathcal { A } } ^ { \prime } ] , } \\ &  \quad - [ \frac { \partial ( F _ { + } , F _ { + } ) } { \partial g ^ { \prime } } \frac { \partial W _ { 1 } ^ { \prime } } { \partial G ^ { \prime } } ] _ { \omega = \frac { 1 } { 2 } } - \frac { 1 } { 2 \tilde { \mathcal { B } } ^ { \prime } } \frac { \partial W _ { 1 } } { \partial G ^ { \prime } } \frac  \partial W \end{array}
$$

$$
\begin{array} { r l } & { \quad \quad \widehat { \mu } ( \mu ^ { ( 0 ) } ) = \frac { 1 } { \sqrt { 2 } } ( \frac { 1 } { \sqrt { 2 } } ( \frac { \mu } { \mu } ) ^ { - 1 } \frac { \mu } { \mu } ) ^ { - 1 } \int } \\ & { + 4 \widehat { \mu } ( \frac { 1 } { \sqrt { 2 } } ( \frac { \mu } { \mu } - \frac { \mu } { \mu } ) ^ { 2 } ) \sin ( 2 \mu ) \cdot \mu ^ { * } \mu ^ { * } ( \frac { 1 } { \sqrt { 2 } } ) \sin ( \mu ^ { * } ) ] , } \\ & { - [ \frac { 2 ( \mu ) ( \hat { \mathbf { r } } _ { + } \hat { \mathbf { r } } _ { + } ) } { \sqrt { 2 } } ( \frac { \mu } { \sqrt { 2 } } ) \sin ( 2 \mu ) ] , } \\ & { - \frac { 1 } { \sqrt { 2 } } \frac { \mu } { \mu ^ { 2 } } ( \frac { 1 } { \sqrt { 2 } } ( 1 - \epsilon ^ { 2 } ) ^ { 2 } ) \sin ( \frac { \mu } { \sqrt { 2 } } ) \sin ( 2 \mu ) } \\ & { - \frac { 1 } { \sqrt { 2 } } \frac { \mu } { \mu ^ { 2 } } ( \frac { 1 } { \sqrt { 2 } } ( 1 - \epsilon ^ { 2 } ) ^ { 2 } ) \cos ( \frac { 1 } { \sqrt { 2 } } ) \cos ( 2 \mu ) } \\ & { \quad \quad \times \frac { 1 } { \sqrt { 2 } } + \frac { ( 1 - \epsilon ^ { 2 } ) ^ { 2 } } { \sqrt { 2 } } ( \frac { 1 } { \sqrt { 2 } } ( \frac { \mu } { \sqrt { 2 } } + \frac { \mu } { \sqrt { 2 } } ) ^ { 2 } ) } \\ & { \quad \quad \times \frac { 1 } { \sqrt { 2 } } + \frac { ( 1 - \epsilon ^ { 2 } ) ^ { 2 } } { \sqrt { 2 } } ( \frac { 1 } { \sqrt { 2 } } ( \frac { \mu } { \sqrt { 2 } } + \frac { \mu } { \sqrt { 2 } } ) ^ { 2 } ) } \\ &  + \frac { ( \mu ^ { 2 } ) ^ { 2 } } { \sqrt { 2 } } ( \frac { 1 } { \sqrt { 2 } } ( \frac { \mu } { \sqrt { 2 } } \end{array}
$$

于是得

$$
\begin{array} { l } { { { \cal F } _ { 2 } ^ { * } = \displaystyle \frac { 1 } { 2 L ^ { \prime , 1 0 } } \biggl [ \frac { 3 } { 3 2 } ( 5 - 1 8 \cos ^ { 2 } i ^ { \prime } + 5 \cos i ^ { \prime } ) ( 1 - e ^ { \prime 2 } ) ^ { - 5 / 2 } } } \\ { { \phantom { \frac { 1 } { 1 } } \qquad \quad \cdots \qquad \cdots \qquad } } \\ { { \phantom { \frac { 1 } { 1 } } \qquad \quad + \displaystyle \frac { 3 } { 8 } ( 1 - 6 \cos ^ { 2 } i ^ { \prime } + 9 \cos ^ { 4 } i ^ { \prime } ) ( 1 - e ^ { \prime 2 } ) ^ { - 3 } } } \\ { { \phantom { \frac { 1 } { 1 } } \qquad \quad - \displaystyle \frac { 1 5 } { 3 2 } ( 1 - 2 \cos ^ { 2 } i ^ { \prime } - 7 \cos ^ { 4 } i ^ { \prime } ) ( 1 - e ^ { \prime 2 } ) ^ { - 7 / 2 } } } \\ { { \phantom { \frac { 1 } { 1 } } \qquad \quad + \displaystyle \frac { 3 } { 1 6 } ( 1 - 1 6 \cos i ^ { \prime } + 1 5 \cos ^ { 4 } i ^ { \prime } ) e ^ { \prime 2 } ( 1 - e ^ { \prime 2 } ) ^ { - 7 / 2 } \cos 2 g ^ { \prime } \biggr ] . } } \end{array}
$$

这与Zeipei方法给出的结果相同，只是小参数J，，的“位置”有移动，当然,重要的是：变换关系是显函数形式，即 $\mathbf { \Psi } \mathbf { W } _ { 1 } = \mathbf { W } _ { 1 } ( \mathbf { \Psi } \mathbf { Z } ^ { \prime } ,$ $G ^ { \prime } , H ^ { \prime } , l ^ { \prime } , g ^ { \prime } )$ ，相应的消除 $l ^ { \prime }$ 后的 $F ^ { * }$ 亦无换变量问题,其形式为

$$
F ^ { * } = F _ { \ell } ^ { * } ( L ^ { \prime } ) + J _ { 2 } F _ { 1 } ^ { * } ( L ^ { \prime } , G ^ { \prime } , H ^ { \prime } ) + \frac { J _ { 2 } ^ { 2 } } { 2 } F _ { 2 } ^ { * } ( L ^ { \prime } , G ^ { \prime } H ^ { \prime } , g ^ { \prime } ) .
$$

# 2.消除 ${ \pmb { \mathscr { E } } } ^ { \prime }$ 的过程

同样将新变量记作 ${ \cal L } ^ { \prime \prime } , { \cal G } ^ { \prime \prime } , { \cal H } ^ { \prime \prime } , { \cal l } ^ { \prime \prime } , g ^ { \prime \prime } , \hbar ^ { \prime \prime } .$ ，母函数和变换后的新合密顿函数分别记作 $\mathbb { W } ^ { * }$ 和 $F ^ { * * }$ ，显然可以假定 $W ^ { * } { = } W ^ { * } ( L ^ { \prime \prime } { ; }$ $( G ^ { \prime \prime } , H ^ { \prime \prime } , g ^ { \prime \prime } ; \varepsilon )$ ，相应的变换关系为

$$
\begin{array} { r l r l } & { L ^ { \prime } = L ^ { \prime \prime } , } & & { l ^ { \prime } = l ^ { \prime \prime } - J _ { 2 } \frac { \partial W _ { 1 } ^ { * } } { \partial L ^ { \prime \prime } } , } \\ & { G ^ { \prime } = G ^ { \prime \prime } + J _ { 2 } \frac { \partial W _ { 1 } ^ { * } } { \partial g ^ { \prime \prime } } , } & & { g ^ { \prime } = g ^ { \prime \prime } - J _ { 2 } \frac { \partial W _ { 1 } ^ { * } } { \partial G ^ { \prime \prime } } , } \\ & { H ^ { \prime } = H ^ { \prime \prime } , } & & { h ^ { \prime } = h ^ { \prime \prime } - J _ { 2 } \frac { \partial W _ { 1 } ^ { * } } { \partial H ^ { \prime \prime } } . } \end{array}
$$

新哈密顿函数为

$$
{ \cal F } ^ { * * } { = } { \cal F } ^ { ( 0 ) } + { \cal J } _ { 2 } { \cal F } ^ { ( 1 ) } { + } \frac { J _ { 2 } ^ { 2 } } { 2 } { \cal F } ^ { ( 2 ) } { + } \cdots ,
$$

这里的系数 $F ^ { ( 0 ) } , F ^ { ( 1 ) } , F ^ { ( 2 ) } \bullet$ 分别由下列各式表达：

$$
\left. \begin{array} { r l } & { F ^ { ( 0 ) } = F _ { 0 } ^ { * } \left( L ^ { \prime \prime } \right) , } \\ & { F ^ { ( 1 ) } = L _ { 1 } F _ { 0 } ^ { * } \ – \ F _ { 1 } ^ { * } \left( L ^ { \prime \prime } , G ^ { \prime \prime } , H ^ { \prime \prime } \right) , } \\ & { F ^ { ( 2 ) } = L _ { 2 } F _ { 0 } ^ { * } \dash \bot _ { 1 } ^ { 2 } F _ { 0 } ^ { * } \gets 2 L _ { 1 } F _ { 1 } ^ { * } + F _ { 2 } ^ { * } \left( L ^ { \prime \prime } , G ^ { \prime \prime } , H ^ { \prime \prime } , g ^ { \prime \prime } \right) . } \end{array} \right\} ^ { ( 1 ) }
$$

因假定 $\boldsymbol { W } _ { \texttt { n } } ^ { * }$ 不含 ${ \vec { \ell } } ^ { \prime \prime }$ ，于是有

$$
L _ { n } F _ { 0 } ^ { * } { = } 0 , ( n { = } 1 , 2 , \cdots ) ,
$$

油此可得消除 ${ \pmb g } ^ { \prime \prime }$ 后的 $\pmb { F } ^ { * * }$ 和确定 $\mathbf { W } ^ { * }$ 的关系式为

$$
\bar { F } _ { 0 } ^ { * * } = \frac { 1 } { 2 L ^ { \prime \prime 2 } } ,
$$

$$
{ \cal F } _ { 1 } ^ { * * } = { \cal F } _ { 1 } ^ { * } \left( L ^ { n } , G ^ { n } , H ^ { n } \right) = \frac { A ^ { n } } { 2 L ^ { n ^ { 3 } } G ^ { n 3 } } ,
$$

$$
\begin{array} { l } { { { \cal F } _ { 2 } ^ { * * } = { \cal F } _ { 2 \sigma } ^ { * } ( L ^ { \mu } , { \cal G } ^ { \nu } , { \cal H } ^ { \nu } ) ~ , } } \\ { { { \ \mathrm {  ~ \Lambda ~ } } } } \\ { { \displaystyle = \frac { 1 } { 2 L ^ { \mu \nu 1 0 } } \Big [ \frac { 3 } { 3 2 } ( 5 - 1 8 \cos ^ { 2 } i ^ { \mu } ) ~ } } \\ { { \ ~ + 5 \cos ^ { 4 } i ^ { \mu } ) ~ ( 1 - e ^ { \eta 2 } ) ^ { - 5 / 2 } } } \\ { { { \ \mathrm {  ~ \Lambda ~ } } } } \\ { { \displaystyle ~ + \frac { 3 } { 8 } ( 1 - 6 \cos ^ { 2 } i ^ { \mu } + 9 \cos ^ { 4 } i ^ { \nu } ) ~ ( 1 - e ^ { \eta 2 } ) ^ { - 3 } } } \\ { { { \ \mathrm {  ~ \Lambda ~ } } } } \\ { { \displaystyle ~ - \frac { 1 5 } { 3 2 } ( 1 - 2 \cos ^ { 2 } i ^ { \upsilon } - 7 \cos i ^ { \mu } i ^ { \nu } ) ~ ( 1 - e ^ { \eta 2 } ) ^ { - 7 / 2 } \Bigg ] , } } \end{array}
$$

$$
0 = 2 \frac { \partial F _ { 1 } ^ { * } } { \partial G ^ { i \prime } } \bigg ( \frac { \partial W _ { 1 } ^ { * } } { \partial g ^ { \prime \prime } } \bigg ) + F _ { 2 \mathit { i } } ^ { * } \left( \mathit { L } ^ { \prime \prime } , G ^ { \prime \prime } , H ^ { \prime \prime } , g ^ { \prime \prime } \right)
$$

最后一个关系式即用来确定 $W _ { 1 } ^ { * }$ ：

$$
\begin{array} { r } { W _ { 1 } ^ { \ast } = \displaystyle \int ^ { g \prime \prime } \frac { F _ { 2 \iota } ^ { \ast } / 2 } { - \frac { \partial F _ { 1 } ^ { \ast } } { \partial G ^ { \prime \prime } } } d g ^ { \prime \prime } } \end{array}
$$

$$
\begin{array} { l } { { \displaystyle = - \frac { 1 } { 3 2 G ^ { n 3 } } e ^ { \prime \prime 2 } ( 1 - 1 6 \cos ^ { 2 } i ^ { \prime \prime } } } \\ { { \displaystyle \qquad + 1 5 \cos ^ { 4 } i ^ { \prime \prime } ) ( 1 - 5 \cos ^ { 2 } i ^ { \prime \prime } ) ^ { - 1 } \sin 2 g ^ { \prime \prime } } . } \end{array}
$$

到此，两次变换完成，将 $\smash { \boldsymbol { W } _ { 1 } }$ 和 $\mathbf { \boldsymbol { W } } _ { 1 } ^ { * }$ 分别代人变换关系（7.246）和(7.256)式，即得一阶短周期项 $\sigma _ { s } ^ { \left( 1 \right) } \left( t \right)$ 和一阶长周期项 $\sigma _ { i } ^ { ( 1 ) } ( t )$ ·最后，“平均根数” $\sigma ^ { \prime \prime }$ 的解由 ${ \cal { F } } ^ { * * } ( L ^ { \prime \prime } , G ^ { \prime \prime } , H ^ { \prime \prime } )$ 给出，与Zeipel方法得到的结果完全相同，这里不再重复列出，请见（7.214）和(7.215)式.

与Zeipel方法相比，其明显的优点是变换为显函数形式，而级数展开式的各次幂的系数有规则的递推关系亦是一大优点，便于某些问题的讨论和机器运算(如用计算机进行公式推导，建立高阶解[11],不过解的形式是对平近点角 $l$ 的展开形式)．但是，就具体应用而言，对构造一阶解或二阶解，尽管Zeipel方法有新旧变量的转换问题，却仍比Lie变换稍为简单些,即中间推导过程的运算所涉及的项数比Lie变换少，读者仔细比较一下是不难得出这一结论的．当然，亦可分别采用两种变换先后消除 $l$ 和 $g$ 来构造级数解[12].

至于显含 $\pmb { t }$ 或同时含 $\pi$ 的问题(例如同时考虑田谐项)，处理方法与Zeipel方法类似,没有任何困难；要构造高 阶解，亦同样可行.

# $\$ 7.8$ 无奇点形式的变换方法

根据前面两节的讨论和结果，可清楚地看出，小 $e$ 小 $\textbf { \textit { i } }$ 问题和通约问题依然存在，这并不奇怪，因为两种方法所采用的变量$( l = M , g = \omega , h = \varOmega )$ 以及解按不同性质的划分与第五章中平均根数法的处理方法类似,当然要出现同类问题，那么，正则变换方法是否也可以消除这两类奇点呢？引用第六章的思想，同样可以达到此目的.

尽管 $e = 0$ 和 $\dot { \pmb { \imath } } = \dot { \pmb { 0 } }$ 的问题仅涉及到变量的选择，但引进无奇点变量后，快、慢变量 $l$ 和 $\pmb { g }$ 不再直接出现，寻找循环坐标的过程将与前面的做法有所区别。而通约情况的问题是出现在长周期项中,这将要改变消除慢变量的过程，下面分三种情况进行讨论.

# 1.消除 $\pmb { e = 0 }$ 的正则变换

采用前面(7.149)式给出的一组无奇点正则共轭变量，即

$$
\left. \begin{array} { l l } { { \tilde { L } = L , } } & { { \tilde { l } = l + g , } } \\ { { \tilde { G } = \sqrt { 2 \left( L - G \right) } \cos g , } } & { { \tilde { g } = - \sqrt { 2 \left( L - G \right) } \sin g , } } \\ { { \widetilde { H } = H , } } & { { \tilde { h } = h . } } \end{array} \right\}
$$

(7.151)式可知

$$
\scriptstyle { \sqrt { 2 ( L - G ) } } = L \ { \sqrt { 2 / ( L + G ) } } e .
$$

烟此， $\widetilde { G }$ 和 $\tilde { \pmb g }$ 又可写成下列形式：

$$
\widetilde { G } = D e \cos g , \widetilde { g } = - D e \sin g ,
$$

$$
\scriptstyle D = L { \sqrt { 2 / ( L \cdot \ i - G ) } } ,
$$

并有

$$
{ \widetilde { \cal G } } ^ { 2 } \div { \widetilde { g } } ^ { 2 } = D ^ { 2 } e ^ { 2 } .
$$

这与平均根数法中引进的两个变量 $\xi = e \cos \omega , \eta = - e \sin \omega$ 类似..相应的逆变换为

$$
\left. \begin{array} { l l } { { L = \tilde { L } , } } & { { \quad \quad l = \tilde { l } - \mathbf { t g } ^ { - 1 } ( - \tilde { g } / \tilde { G } ) , } } \\ { { { \cal G } = \tilde { L } - \frac { 1 } { 2 } ( \tilde { G } ^ { 2 } + \tilde { g } ^ { 2 } ) , } } & { { \quad \quad g = \mathbf { t g } ^ { - 1 } ( - \tilde { g } / \tilde { G } ) , } } \\ { { { \cal H } = \widetilde { H } , } } & { { \quad \quad h = \tilde { h } . } } \end{array} \right\}
$$

由此可清楚地看出两种变量之间的函数关系．显然， $\tilde { l }$ 仍为快变量，它由 $l$ 的性质所确定，而 $\tilde { G }$ 和 $\tilde { \pmb g }$ 则由 $\pmb { g }$ 的性质所确定，因此它.们是慢变量，但 $\widetilde { G } ^ { 2 } + \widetilde { g } ^ { 2 } = D ^ { 2 } e ^ { 2 }$ 却是 $\pmb { L }$ 和 $G$ 的函数，而非慢变量，在相应的消除慢变量过程中，应保留以 $\widetilde { G } ^ { 2 } \mathbb { - } \widetilde { g } ^ { 2 }$ 形式出现的项.

仍用Lie变换,考虑地球形状带谐项摄动，相应的哈密顿函数不显含 $t ,$ 可写为下列形式：

$$
\begin{array} { r l } & { F = F _ { 0 } ( \widetilde { L } ) + J _ { 2 } F _ { 1 } ( \widetilde { L } , \widetilde { G } , \widetilde { H } , \widetilde { l } , \widetilde { g } ) \ + \frac { J _ { 2 } ^ { 2 } } { 2 } F _ { 2 } ( \widetilde { L } , \widetilde { G } , \widetilde { H } , \widetilde { l } , \widetilde { g } ) , } \\ & { F _ { 1 } = F _ { 1 e } ( \widetilde { L } , \widetilde { H } , \widetilde { G } ^ { 2 } + \widetilde { g } ^ { 2 } ) + F _ { 1 s } ( \widetilde { L } , \widetilde { G } , \widetilde { H } , \widetilde { l } , \widetilde { g } ) , } \\ & { F _ { 2 } = F _ { 2 e } ( \widetilde { L } , \widetilde { H } , \widetilde { G } ^ { 2 } + \widetilde { g } ^ { 2 } ) + F _ { 2 l } ( \widetilde { L } , \widetilde { G } , \widetilde { H } , \widetilde { g } ) \ + F _ { 2 s } ( \widetilde { L } , \widetilde { G } , \widetilde { H } , \widetilde { l } , \widetilde { g } ) . } \end{array} \Bigg \{ \Bigg \} 
$$

下面针对一阶解来看消除快、慢变量的过程

（1）消除 $\tilde { \iota }$ 的过程

新变量记作 $\tilde { L } ^ { \prime } , \tilde { G } ^ { \prime } , \widetilde { H } ^ { \prime } , \tilde { \iota } ^ { \prime } , \tilde { g } ^ { \prime } , \tilde { h } ^ { \prime }$ 变换的母函数为

$$
W = W _ { 1 } ( \tilde { L } ^ { \prime } , \tilde { G } ^ { \prime } , \widetilde { H } ^ { \prime } , \tilde { l } ^ { \prime } , \tilde { g } ^ { \prime } ) + J _ { 2 } W _ { 2 } ( \tilde { L } ^ { \prime } , \tilde { G } ^ { \prime } , \widetilde { H } ^ { \prime } , \tilde { l } ^ { \prime } , \tilde { g } ^ { \prime } ) + \cdots
$$

由此给出变换关系如下：

$$
\begin{array} { r } { \tilde { L } = \tilde { L } ^ { \prime } + J _ { 2 } \frac { \hat { \sigma } W _ { 1 } } { \partial \tilde { l } ^ { \prime } } + \cdots , \tilde { l } = \tilde { l } ^ { \prime } - \frac { \partial W _ { 1 } } { \partial \tilde { L } ^ { \prime } } - \cdots , } \\ { \tilde { G } = \tilde { G } ^ { \prime } + J _ { 2 } \frac { \partial W _ { 1 } } { \partial \tilde { g } ^ { \prime } } + \cdots , \tilde { g } = \tilde { g } ^ { \prime } - \frac { \partial W _ { 1 } } { \partial \tilde { G } ^ { \prime } } - \cdots , } \\ { \widetilde { H } = \widetilde { H } ^ { \prime } + J _ { 2 } \frac { \partial W _ { 1 } } { \partial \tilde { h } ^ { \prime } } + \cdots , \tilde { h } = \tilde { h } ^ { \prime } - \frac { \partial W _ { 1 } } { \partial \widetilde { H } ^ { \prime } } - \cdots . } \end{array}
$$

相应的变换后的哈密顿函数为

$$
{ \cal { F } } ^ { * } = { \cal { F } } ^ { ( 0 ) } + { \cal { J } } _ { 2 } { \cal { F } } ^ { ( 1 ) } + \frac { J _ { 2 } } { 2 } { \cal { F } } ^ { ( 2 ) } + \cdots
$$

$$
\left. \begin{array} { l } { { F ^ { ( 0 ) } = F _ { 0 } , } } \\ { { F ^ { ( 1 ) } = L _ { 1 } F _ { 0 } + F _ { 1 } } } \\ { { F ^ { ( 2 ) } = L _ { 2 } F _ { 0 } - \{ \ L _ { 1 } ^ { 2 } F _ { t } - \} \ 2 L _ { 1 } F _ { i } + F _ { 2 } . } } \end{array} \right\}
$$

于是，消除 $\tilde { \boldsymbol { \imath } }$ 后的 $\pmb { F } ^ { * }$ 和相应的母函数 $\pmb { W } ^ { * }$ 由下列各式确定：

$$
\begin{array} { r } { F _ { 0 } ^ { * } = F _ { 0 } ( \widetilde { L } ^ { \prime } ) , } \end{array}
$$

$$
F _ { 1 } ^ { * } { = } F _ { 1 e } ( \widetilde { L } ^ { \prime } , \widetilde { H } ^ { \prime } , \widetilde { G } ^ { \prime 2 } { + } \widetilde { g } ^ { \prime 2 } ) ,
$$

$$
\begin{array} { r l } & { F _ { 2 } ^ { * } = [ \langle F _ { 1 } + F _ { 1 e } ; W _ { 1 } \rangle ] _ { c o 1 } + F _ { 2 e } ( \tilde { L } ^ { \prime } , \widetilde { H } ^ { \prime } , \tilde { G } ^ { \prime 2 } + \tilde { g } ^ { \prime 2 } ) } \\ & { \qquad + F _ { 2 \iota } ( \tilde { L } ^ { \prime } , \tilde { G } ^ { \prime } , \tilde { H } ^ { \prime } , \tilde { g } ^ { \prime } ) } \\ & { \qquad = F _ { 2 \iota } ^ { * } ( \tilde { L } ^ { \prime } , \tilde { H } ^ { \prime } , \tilde { G } ^ { i 2 } + \tilde { g } ^ { \prime 2 } ) + F _ { 2 \iota } ^ { * } ( \tilde { L } ^ { \prime } , \tilde { G } ^ { \prime } , \tilde { H } ^ { \prime } , \tilde { g } ^ { \prime } ) } \end{array}
$$

$$
\frac { \partial F _ { 0 } } { \partial \tilde { L } ^ { \prime } } \Big ( \frac { \partial W _ { 1 } } { \partial \tilde { l } ^ { \prime } } \Big ) { = } - F _ { 1 s } ( \tilde { L } , \tilde { G } ^ { \prime } , \tilde { H } ^ { \prime } , \tilde { l } ^ { \prime } , \tilde { g } ^ { \prime } ) .
$$

最后一式给出

$$
W _ { 1 } ( \tilde { L } ^ { \prime } , \tilde { G } ^ { \prime } , \widetilde { H } ^ { \prime } , \tilde { l } ^ { \prime } , \tilde { g } ^ { \prime } ) = \tilde { L } ^ { \prime 3 } \int ^ { \tilde { \tau } _ { \prime } } F _ { 1 s } ( \tilde { L } ^ { \prime } , \tilde { G } ^ { \prime } , \widetilde { H } ^ { \prime } , \tilde { l } , \tilde { g } ^ { \prime } ) d \tilde { l } ^ { \prime } .
$$

事实上(7.277)式的原式为

$$
\{ F _ { 0 } \dag , W _ { 1 } \} = - F _ { 1 s } ( \tilde { L } ^ { \prime } , \tilde { G } ^ { \prime } , \tilde { H } ^ { \prime } , \tilde { l } ^ { \prime } , \tilde { g } ^ { \prime } ) .
$$

若将 $\{ \pmb { F } _ { 0 } ; \pmb { W } _ { 1 } \}$ 记为 $\{ \pmb { F } _ { 0 } ; \pmb { W } _ { 1 } \} ^ { \tilde { \pmb { \sigma } } ^ { \prime } }$ ，即对无奇点变量 $\mathcal { Z } ^ { \prime } , \tilde { G } ^ { \prime } , \cdots$ 的泊松括弧， $\{ \pmb { F } _ { 0 } ; \pmb { W } _ { 1 } \} ^ { \alpha }$ 表示经变换(7.264）对德洛纳变量 $L _ { 9 } ^ { \prime } G ^ { \prime } .$ ·的泊

松括弧；而右端项 $F _ { 1 s } ( \widetilde { L } ^ { \prime } , \widetilde { G } ^ { \prime } , \cdots )$ 就是原 $F _ { 1 s } ( L ^ { \prime } , G ^ { \prime } , \cdots )$ 经变换(7.268)式给出的，因此，根据前面（7.43）式给出的泊松括弧的正则绝对不变性 $( \mu = 1 )$ ：

$$
\left\{ F _ { 0 } ; W _ { 1 } \right\} ^ { \widetilde \sigma ^ { \prime } } = \left\{ F _ { 0 } ; W _ { 1 } \right\} ^ { \sigma ^ { \prime } } ,
$$

不难看出,无需具体积分(7.278)式， $W _ { 1 } ( \tilde { L } ^ { \prime } , \tilde { G } ^ { \prime } , \cdots )$ 就可由上一节(7.254)式表达的 $W _ { 1 } ( L ^ { \prime } , G ^ { \prime } , \cdots )$ 经变换(7.268)给出，即

$$
W _ { 1 } ( \tilde { L } ^ { \prime } , \tilde { G } ^ { \prime } , \cdots ) = W _ { 1 } ( L ^ { \prime } ( \tilde { L } ^ { \prime } ) , G ^ { \prime } ( \tilde { L } ^ { \prime } , \tilde { G } ^ { \prime 2 } + \tilde { g } ^ { \prime 2 } ) , H ^ { \prime } ( \widetilde { H } ^ { \prime } ) , \cdots ) .
$$

关于 $\pmb { F } _ { 2 , c } ^ { * }$ 和 $\pmb { F _ { 2 l } ^ { * } }$ 的推导，由于 ${ \pmb F } _ { 1 }$ 和 $W _ { \downarrow }$ 的表达式均由上一节的 $\boldsymbol { F } _ { 1 }$ 和 $W _ { \mathrm { ~ 1 ~ } }$ 经变换(7.268)给出，故与上面给出 $W _ { 1 } ( \tilde { L } ^ { \prime } , \tilde { G } ^ { \prime } , \cdots )$ 的情况类似,根据泊松括弧的正则不变性，可以证得 $\pmb { F } _ { 2 , } ^ { * }$ 和 $\tilde { F } _ { 2 l } ^ { * }$ 亦同样可以由上一节的 $F _ { 2 \ c } ^ { * } ( L ^ { \prime } , G ^ { \prime } , H ^ { \prime } )$ 和 $F _ { 2 } ^ { * } { } _ { l } ( L ^ { \prime } , G ^ { \prime } , H ^ { \prime } , g ^ { \prime } )$ 经变换(7.268)给出，最后得

$$
\begin{array} { r l r } {  { F ^ { * } = F _ { 0 } ^ { * } ( \tilde { L } ^ { \prime } ) + F _ { 1 } ^ { * } ( \tilde { L } ^ { \prime } , \widetilde { H } ^ { \prime } , \tilde { G } ^ { \prime 2 } { \cdot } \tilde { g } ^ { \prime 2 } ) + F _ { 2 , c } ^ { * } ( \tilde { L } ^ { \prime } , \widetilde { H } ^ { \prime } , \tilde { G } ^ { \prime 2 } { + } \tilde { g } ^ { \prime 2 } ) } } \\ & { } & { \quad + F _ { 2 , l } ^ { * } ( \tilde { L } ^ { \prime } , \tilde { G } ^ { \prime } , \tilde { \mathcal { U } } ^ { \prime } , \tilde { g } ^ { \prime } ) . \quad \quad \quad \quad \quad ( 7 . 2 8 0 ) } \end{array}
$$

（2）消除 $\tilde { \pmb g } ^ { \prime }$ 的过程

新变量记作 $\widetilde { L } ^ { \prime \prime } , \hat { G } ^ { \prime \prime } , \widetilde { H } ^ { \prime \prime } , \bar { l } ^ { \prime \prime } , \tilde { g } ^ { \prime \prime } , \tilde { h } ^ { \prime \prime }$ ，变换的母函数为

$$
W ^ { * } { = } W _ { 1 } ^ { * } ( \widetilde L ^ { \prime \prime } , \widetilde G ^ { \prime \prime } , \widetilde H ^ { \prime \prime } , \widetilde g ^ { \prime \prime } ) { + } J _ { 2 } W _ { 2 } ^ { * } ( \widetilde L ^ { \prime \prime } , \widetilde G ^ { \prime \prime } , \widetilde H ^ { \prime \prime } , \widetilde g ^ { \prime \prime } ) { + } { \cdots } ,
$$

变换关系是

$$
\begin{array}{c} \begin{array} { r l r l } & { \tilde { L } ^ { \prime } { = } \tilde { L } ^ { n } , } & & { \tilde { L } ^ { \prime } { = } \tilde { \mathcal { \tilde { \tilde { l } } } } ^ { \prime \prime } { - } J _ { 2 } \frac { { \partial } W _ { 1 } ^ { * } } { { \partial \tilde { L } } } { - } \cdots , } \\ & { \tilde { G } ^ { \prime } { = } \tilde { G } ^ { \prime \prime } { + } J _ { 2 } \frac { { \partial } W _ { 1 } ^ { * } } { { \partial \tilde { g } ^ { \prime \prime } } } { + } \cdots , } & & { \tilde { g } ^ { \prime } { = } \tilde { g } ^ { \prime \prime } { - } J _ { 2 } \frac { { \partial } W _ { 1 } ^ { * } } { { \partial \tilde { G } ^ { \prime \prime } } } { - } \cdots , } \\ & { \widetilde { H } ^ { \prime } { = } \widetilde { H } ^ { \prime \prime } , } & & { \tilde { h } ^ { \prime } { = } \tilde { h } ^ { \prime \prime } { - } J _ { 2 } \frac { { \partial } W _ { 1 } ^ { * } } { { \partial \tilde { H } ^ { \prime \prime } } } { - } \cdots . } \end{array} ) ( 7 . 2 8 2 ) ^ { . }  \end{array}
$$

相应的变换后消除部分含 $\widetilde { \pmb { g } }$ 项的哈密顿函数为

$$
F ^ { * * } ( \widetilde { L } ^ { \prime \prime } , \widetilde { H } ^ { \prime \prime } , \widetilde { G } ^ { \prime \prime 2 } + \widetilde { g } ^ { \prime \prime 2 } )
$$

$$
\begin{array} { r l } & { \le F _ { 0 } ^ { * * } ( \widetilde { L } ^ { \prime \prime } ) \div J _ { 2 } F _ { 1 } ^ { * * } ( \widetilde { L } ^ { \prime \prime } , \widetilde { H } ^ { \prime \prime } , \widetilde { G } ^ { \prime \prime 2 } + \widetilde { g } ^ { \prime \prime 2 } ) } \\ & { ~ + \frac { J _ { 2 } ^ { 2 } } { 2 } F _ { 2 } ^ { * * } ( \widetilde { L } ^ { \prime \prime } , \widetilde { H } ^ { \prime \prime } \widetilde { G } ^ { \prime \prime 2 } + \widetilde { g } ^ { \prime \prime 2 } ) , } \end{array}
$$

$$
- \langle F _ { 1 } ^ { * } ; W _ { 1 } ^ { * } \rangle = \frac { 1 } { 2 } F _ { 2 \mathit { l } } ^ { * } ( \widetilde { L } ^ { \prime \prime } , \widetilde { G } ^ { \prime \prime } , \widetilde { H } ^ { \prime \prime } , \tilde { g } ^ { \prime \prime } ) .
$$

其中

$$
\begin{array} { r l } & { F _ { 1 } ^ { * * } { = } F _ { 1 } ^ { * } ( \widetilde { L } ^ { \prime \prime } , \widetilde { H } ^ { \prime \prime } , \widetilde { G } ^ { \prime \prime 2 } { + } \widetilde { g } ^ { \prime \prime 2 } ) , } \\ & { F _ { 2 } ^ { * * } { = } F _ { 2 c } ^ { * } ( \widetilde { L } ^ { \prime \prime } , \widetilde { H } ^ { \prime \prime } , \widetilde { G } ^ { \prime \prime 2 } { + } \widetilde { g } ^ { \prime \prime 2 } ) . } \end{array}
$$

而确定W与确定W，的情况类似,由于(7.284)式中的F和F\*就是上一节F和F；经变换(7.268)给出的，故由泊松括弧的正则不变性：

$$
\left\{ { \cal F } _ { 1 } ^ { * } ; { \cal W } _ { 1 } ^ { * } \right\} ^ { \widetilde \sigma ^ { \prime } } = \left\{ { \cal F } _ { 1 } ^ { * } ; { \cal W } _ { 1 } ^ { * } \right\} ^ { \sigma ^ { \prime \prime } } ,
$$

可知,W亦可直接由上一节的W\*经变换(7.268)给出,即

$$
\begin{array} { r l } & { \mathcal { W } _ { 1 } ^ { * } ( \widetilde { L } ^ { \prime \prime } , \widetilde { G } ^ { \prime \prime } , \widetilde { H } ^ { \prime \prime } , \widetilde { g } ^ { \prime \prime } ) = W _ { 1 } ^ { * } ( L ^ { \prime \prime } ( \widetilde { L } ^ { \prime \prime } ) , G ^ { \prime \prime } ( \widetilde { L } ^ { \prime \prime } , \widetilde { G } ^ { \prime \prime 2 } } \\ & { + \widetilde { g } ^ { \prime \prime } ) , H ^ { \prime \prime } ( \widetilde { H } ^ { \prime \prime } ) , \widetilde { g } ^ { \prime \prime } ( \widetilde { G } ^ { \prime \prime } , \widetilde { g } ^ { \prime \prime } ) ) , } \end{array}
$$

（3）解

经两次变换给出

$$
\begin{array} { r l } & { F ^ { * * } ( \tilde { L } ^ { \prime \prime } , \tilde { H } ^ { \prime \prime } , \tilde { G } ^ { \prime \prime 2 } + \tilde { g } ^ { \prime \prime 2 } ) = F _ { 0 } ^ { * * } ( \tilde { L } ^ { \prime \prime } ) } \\ & { + J _ { 2 } F _ { 1 } ^ { * * } ( \tilde { L } ^ { \prime \prime } , \tilde { H } ^ { \prime \prime } , \tilde { G } ^ { \prime \prime 2 } + \tilde { g } ^ { \prime \prime 2 } ) + \frac { J _ { 2 } ^ { 2 } } { 2 } F _ { 2 } ^ { * * } ( \tilde { L } ^ { \prime \prime } , \tilde { H } ^ { \prime \prime } , \tilde { G } ^ { \prime \prime 2 } + \tilde { g } ^ { \prime \prime 2 } ) . } \end{array}
$$

根据前面的讨论,F\*，F\*和F\*的具体表达式就是上一节给出的F(L"),F\*\*(L",G",H")和F\*\*(L",G",H")经变换(7.268)而得．但现在只有两个循环坐标”和h",那么存在两个积分：

$$
\widetilde { L } ^ { \prime \prime } = \widetilde { L } _ { 0 } ^ { \prime \prime } , \widetilde { H } ^ { \prime \prime } = \widetilde { H } _ { 0 } ^ { \prime \prime } .
$$

对 $G ^ { \prime \prime }$ 和 $\tilde { \pmb { g } } ^ { \prime \prime }$ ，根据变换(7.268)有

$$
\left. \begin{array} { l } { { \displaystyle { \frac { d \tilde { G } ^ { \prime \prime } } { d t } } { = } { \frac { \partial F ^ { * * } } { \partial \tilde { g } ^ { \prime \prime } } } { = } { \frac { \partial F ^ { * * } } { \partial \tilde { G } ^ { \prime \prime } } } ( - \tilde { g } ^ { \prime \prime } ) , } } \\ { { \displaystyle { \frac { d \tilde { g } ^ { \prime \prime } } { d \tilde { t } } } { = } { - } { \frac { \partial F ^ { * * } } { \tilde { c } \tilde { G } ^ { \prime \prime } } } { = } { - } { \frac { \partial F ^ { * * } } { \partial G ^ { \prime \prime } } } ( - \tilde { G } ^ { \prime \prime } ) . } } \end{array} \right\}
$$

右端- $- \mathop { \overline { { \partial } } } _ { \overline { { \partial { G ^ { \prime \prime } } } } } ^ { \partial \overline { { F ^ { * * } } } }$ 中的 ${ \pmb { F } } ^ { * * }$ 已作为 $L ^ { \prime \prime } , G ^ { \prime \prime } , H ^ { \prime \prime }$ 的函数。若记

$$
C = - \frac { \partial F ^ { * * } } { \partial G ^ { \prime \prime } } ,
$$

可以证明,对于 $\tilde { L } ^ { \prime \prime } , \tilde { H } ^ { \prime \prime } , \tilde { G } ^ { \prime \prime 2 } \mathrel { - } \mathrel { \cdot } \tilde { g } ^ { \prime \prime 2 }$ 的解， $\pmb { c }$ 同样为常数.因

$$
C = C ( L ^ { \prime \prime } , G ^ { \prime \prime } , H ^ { \prime \prime } ) = C ( \tilde { L } ^ { \prime \prime } , \widetilde { H } ^ { \prime \prime } , \tilde { G } ^ { \prime \prime 2 } + \tilde { g } ^ { \prime \prime 2 } ) ,
$$

有

$$
\begin{array} { l } { { \displaystyle { \frac { d C } { d t } } { = } \frac { \partial C } { \partial ( \tilde { G } ^ { \prime \prime 2 } + \tilde { g } ^ { \prime \prime 2 } ) } \bigg ( 2 \tilde { G } ^ { \prime \prime } \frac { d \tilde { G } ^ { \prime \prime } } { d t } { + } 2 \tilde { g } ^ { \prime \prime } \frac { d \tilde { g } ^ { \prime \prime } } { d t } \bigg ) } } \\ { { \displaystyle { = } \frac { \partial C } { \partial ( \tilde { G } ^ { \prime \prime 2 } + \tilde { g } ^ { \prime \prime 2 } ) } ( 2 C \tilde { G } ^ { \prime \prime } \tilde { g } ^ { \prime \prime } { - } 2 C \widetilde { G } ^ { \prime \prime } \tilde { g } ^ { \prime \prime } ) = 0 , } } \end{array}
$$

即

$$
C = C _ { 0 } ( \tilde { L } _ { 0 } ^ { \prime \prime } , \tilde { H } _ { 0 } ^ { \prime \prime } , \tilde { G } _ { 0 } ^ { \prime \prime 2 } + \tilde { g } _ { 0 } ^ { \prime \prime 2 } ) .
$$

于是方程(7.288)式给出振动解:

$$
\begin{array} { r l } & { \widetilde { G } ^ { \prime \prime } \preceq \widetilde { G } _ { 0 } ^ { \prime \prime } \cos \left[ C _ { 0 } ( t - t _ { 0 } ) \right] + \widetilde { g } _ { 0 } \sin \left[ C _ { 0 } ( t - t _ { 0 } ) \right] , \rangle } \\ & { \widetilde { g } ^ { \prime \prime } = \widetilde { g } _ { 0 } ^ { \prime \prime } \cos \left[ C _ { 0 } ( t - t _ { 0 } ) \right] - \widetilde { G } ^ { \prime \prime } \sin \left[ C _ { 0 } ( t - t _ { 0 } ) \right] . \widetilde { \rangle } } \end{array}
$$

由此可得

$$
\widetilde { G } ^ { \prime \prime 2 } + \widetilde { g } ^ { \prime \prime 2 } = \widetilde { G } _ { 0 } ^ { \prime \prime 2 } + \widetilde { g } _ { 0 } ^ { \prime \prime 2 }
$$

与 $c$ 为常数一致．这些结果与第六章的解(6.55)完全类似， $C _ { 0 }$ 对应 $\omega _ { 1 }$ 。但这里的处理从数学角度来看很清楚，也很自然,不必作任何说明.

根据积分(7.287)和关系式(7.292)可知， ${ \partial } { F ^ { * * } } / { \partial \tilde { L } ^ { \prime \prime } }$ 和 $\partial F ^ { * * } 1$ ${ \mathcal { A } } { \widetilde { H } } ^ { \prime \prime }$ 亦是常数，从而给出最后两个积分：

$$
\left. \begin{array} { c } { { \displaystyle \tilde { l } ^ { \prime \prime } = \tilde { l } _ { 0 } ^ { \prime \prime } + \left( - \frac { \partial F ^ { * * } } { \partial \tilde { L } ^ { \prime \prime } } \right) ( t - t _ { 0 } ) , } } \\ { { \displaystyle \tilde { h } ^ { \prime \prime } = \tilde { h } _ { 0 } ^ { \prime \prime } + \left( - \frac { \partial F ^ { * * } } { \partial \widetilde { H } ^ { \prime } } \right) ( t - t _ { 0 } ) . } } \end{array} \right\}
$$

若将 $\pmb { F } _ { 0 } , \pmb { F } _ { 1 }$ 和 ${ \pmb { F } } _ { 2 }$ 的具体形式引入， $W$ 和 $\mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf \mathbf { } \mathbf { } \mathbf { } \mathbf \mathbf { } \mathbf { } \mathbf \mathbf { } \mathbf { } \mathbf \mathbf { } \mathbf { } \mathbf \mathbf { } \mathbf \mathbf { } \mathbf \mathbf { } \mathbf \mathbf { } \mathbf \mathbf { } \mathbf \mathbf { } \mathbf \mathbf { } \mathbf \mathbf \mathbf { } \mathbf \mathbf { } \mathbf \mathbf \mathbf { } \mathbf \mathbf \mathbf { } \mathbf \mathbf \mathbf { } \mathbf \mathbf \mathbf \mathbf { } \mathbf \mathbf \mathbf \mathbf { } \mathbf \mathbf \mathbf \mathbf \mathbf { } \mathbf \mathbf \mathbf \mathbf \mathbf { } \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf { \mathbf \mathbf \Psi \mathbf } \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf$ 即可给出，那么原

变量 $\tilde { L } , \tilde { G } , \tilde { H } , \tilde { l } , \tilde { g } , \tilde { h }$ 的一阶摄动解就可以具体写出来，不再有 $e =$ 0的奇点问题，详见文[13].

2．同时消除 $\pmb { e } = \pmb { 0 }$ 和 $\pmb { i } = \pmb { 0 }$ 的正则变换

采用前面(7.150)式给出的另一组无奇点正则共轭变量，即

$$
\begin{array} { r l } & { \tilde { L } = L } \\ & { \tilde { G } = \sqrt { \textbf { 2 } ( L - G ) } \cos \left( g + h \right) , \tilde { g } = - \sqrt { 2 ( L - G ) } \sin \left( g + h \right) , \left\{ \begin{array} { l l } { \tilde { L } = L + g + h , } \\ { \tilde { L } = - H \left( G - H \right) \cos \left( h \right) } \end{array} \right. } \\ & { \tilde { H } = \sqrt { \textbf { 2 } ( G - H ) } \cos h , \qquad \tilde { h } = - \sqrt { 2 ( G - H ) } \sin h . } \end{array}
$$

同样有

$$
\begin{array} { l } { { \sqrt { 2 \left( L - G \right) } = L \sqrt { 2 / \left( L + G \right) } e , } } \\ { { { } } } \\ { { \sqrt { 2 \left( G - H \right) } = G \sqrt { 2 / \left( G + H \right) } \cdot \sin i , } } \end{array}
$$

若记

$$
D _ { 1 } { = } L \sqrt { 2 / ( L { + } G ) } , D _ { 2 } { = } G \sqrt { 2 / ( G { + } H ) } ,
$$

则

$$
\left. \begin{array} { l l } { { \widetilde { G } = D _ { 1 } e \cos \left( g + h \right) , } } & { { \widetilde { g } = - D _ { 1 } e \sin \left( g + h \right) , } } \\ { { \widetilde { H } = D _ { 2 } \sin i \cos h , } } & { { \widetilde { h } = - D _ { 2 } \sin i \sin h . } } \end{array} \right\}
$$

这就类似于第六章同时消除奇点 $e = 0$ 和 $i = 0$ 所采用的无奇点变量：

$$
\begin{array} { l } { { \xi = e \cos { ( \omega + \Omega ) } , \eta = - e \sin { ( \omega + \Omega ) } , } } \\ { {  \begin{array} { r l } { { \displaystyle } } & { { } } \end{array}  } } \\ { {  \begin{array} { r l } { { \displaystyle } } & { { } } \end{array}  } } \\ { {  \begin{array} { r l } { { \displaystyle } } & { { } } \end{array}  \begin{array} { r l } { { \displaystyle } } & { { } } \\ { { \displaystyle } } & { { } } \end{array}  } } \end{array}
$$

变换(7.294)的逆变换为

$$
\left. \begin{array} { c } { { L = \tilde { L } , } } \\ { { { \cal G } = \tilde { L } - \displaystyle { \frac { 1 } { 2 } } ( \tilde { G } ^ { 2 } + \tilde { g } ^ { 2 } ) , g = \displaystyle { \bf t g } ^ { - 1 } ( - \tilde { g } / \tilde { G } ) - \mathrm { t g } ^ { - 1 } ( - \tilde { h } / \tilde { H } ) , \displaystyle \left\{ \begin{array} { l l } { { } } \\ { { { \cal G } = \tilde { L } - \displaystyle { \frac { 1 } { 2 } } ( \tilde { G } ^ { 2 } + \tilde { g } ^ { 2 } + \tilde { H } ^ { 2 } + \tilde { h } ^ { 2 } ) , h = \mathrm { t g } ^ { - 1 } ( - \tilde { h } / \tilde { H } ) . } } \end{array} \right. } } \\ { { { \cal H } = \tilde { L } - \displaystyle { \frac { 1 } { 2 } } ( \tilde { G } ^ { 2 } + \tilde { g } ^ { 2 } + \tilde { H } ^ { 2 } + \tilde { h } ^ { 2 } ) , h = \mathrm { t g } ^ { - 1 } ( - \tilde { h } / \tilde { H } ) . } } \end{array} \right\}
$$

由此可清楚地了解两种变量之间的函数关系。 $\tilde { \iota }$ 仍为快变量，而

$$
\widetilde { G } ^ { 2 } + \widetilde { g } ^ { 2 } = D _ { 1 } ^ { 2 } e ^ { 2 } , \widetilde { H } ^ { 2 } + \widetilde { h } ^ { 2 } = D _ { 2 } ^ { 2 } \sin ^ { 2 } i \ .
$$

并非慢变量，消除快、慢变量后的哈密顿函数 $\pmb { F } ^ { * * }$ 应为

$$
\bar { F } ^ { * * } = \bar { F } ^ { * * } ( \tilde { L } ^ { \prime \prime } , \tilde { G } ^ { \prime \prime 2 } + \tilde { g } ^ { \prime \prime 2 } , \widetilde { H } ^ { \prime \prime 2 } + \tilde { h } ^ { \prime \prime 2 } ) ,
$$

两次变换的具体过程与前面类似， $\widetilde { G } ^ { \prime \prime } , ~ \widetilde { g } ^ { \prime \prime } , ~ \widetilde { H } ^ { \prime \prime } , ~ \widetilde { h } ^ { \prime \prime }$ 的解有如下形式：

$$
\begin{array} { r l } & { \widetilde { G } ^ { \prime \prime } = \widetilde { G } _ { 0 } ^ { \prime \prime } \cos [ C _ { 1 } ( t - t _ { 0 } ) ] + \widetilde { g } _ { 0 } ^ { \prime \prime } \sin [ C _ { 1 } ( t - t _ { 0 } ) ] , } \\ & { \widetilde { g } ^ { \prime \prime } = \widetilde { g } _ { 0 } ^ { \prime \prime } \cos [ C _ { 1 } ( t - t _ { 0 } ) ] - \widetilde { G } _ { 0 } ^ { \prime \prime } \sin [ C _ { 1 } ( t - t _ { 0 } ) ] , } \\ & { \widetilde { H } ^ { \prime \prime } = \widetilde { H } _ { 0 } ^ { \prime \prime } \cos [ C _ { 2 } ^ { \prime } t - t _ { 0 } ) ] + \widetilde { h } _ { 0 } ^ { \prime \prime } \sin [ C _ { 2 } ( t - t _ { 0 } ) ] , } \\ & { \widetilde { h } ^ { \prime \prime } = \widetilde { h } _ { 0 } ^ { \prime \prime } \cos [ C _ { 2 } ( t - t _ { 0 } ) ] - \widetilde { H } _ { 0 } ^ { \prime \prime } \sin [ C _ { 2 } ( t - t _ { 0 } ) ] . } \end{array}
$$

其中 $C _ { 1 }$ 和 $C _ { 2 }$ 对 $\tilde { L } ^ { \prime \prime } , \tilde { G } ^ { \prime \prime }$ ，…的解均为常数,它们分别为

$$
\left. \begin{array} { l } { { C _ { 1 } { = } { - } \displaystyle \frac { \partial F ^ { * * } } { \partial G ^ { \prime \prime } } { - } \displaystyle \frac { \partial F ^ { * * } } { \partial H ^ { \prime \prime } } , } } \\ { { C _ { 2 } { = } { - } \displaystyle \frac { \partial F ^ { * * } } { \partial H ^ { \prime \prime } } , } } \end{array} \right\}
$$

这里 $\pmb { F } ^ { * * }$ 是通过变换(7.294)作为 $L ^ { \prime \prime } , G ^ { \prime \prime } , H ^ { \prime \prime }$ 的函数．将 $\mathbf { } F _ { 0 } , F _ { \mathrm { ~ i ~ s ~ } }$ $\pmb { F _ { 2 } } \vec { 5 } / \lambda$ ，即可得两次变换的母函数 $W$ 和 $W _ { \textbf { i } } ^ { * }$ ，从而给出原变量 $( L ,$ $G , H , l , g , h )$ 的摄动解,奇点 $\pmb { e } = 0$ 和 $\therefore = 0$ 不复存在.

# 3.通约情况的处理

根据第6节和第7节的讨论,对于 $\pmb { J _ { 2 } }$ 项摄动，消除快变量 $\iota$ 后的哈密顿函数为

$$
F ^ { * } { = } F ^ { * } ( L ^ { \prime } ) + F _ { 1 } ^ { * } ( L ^ { \prime } , G ^ { \prime } , H ^ { \prime } ) + F _ { 2 c } ^ { * } ( L ^ { \prime } , G ^ { \prime } , H ^ { \prime } ) + F _ { 2 ^ { \prime } } ^ { * } ( L ^ { \prime } , G ^ { \prime } ,
$$

$$
\pmb { H } ^ { \prime } ) \cos 2 g ^ { \prime }
$$

为了讨论方便，这里已将原 $\pmb { F } _ { 2 } ^ { * } { } _ { t }$ 中的 $\cos 2 g ^ { \prime }$ 单独提了出来。同时考虑 $\pmb { J _ { 4 } }$ 项时， $F ^ { * }$ 仍保持上述形式．考虑 ${ { J } _ { 2 } }$ 项和 $J _ { \textrm { \pm 2 9 2 } }$ 项摄动时，若在第一次变换消除快变量 $\iota$ 的同时也消除单独出现的慢变量（ $\pmb { g }$ 或 $\pmb { h }$ ),而只保留主要通约项，例如对 $2 4 ^ { \mathtt { h } }$ 地球同步卫星，相应的${ \pmb { F } } ^ { * }$ 有如下形式：

$$
\begin{array} { r l } & { F ^ { * } { = } F _ { 0 } ^ { * } ( L ^ { \prime } ) + F _ { 1 } ^ { * } ( L ^ { \prime } , G ^ { \prime } , H ^ { \prime } ) + F _ { 2 } ^ { * } c ( L ^ { \prime } , G ^ { \prime } , H ^ { \prime } ) + } \\ & { F _ { 2 } ^ { * } { = } F _ { 0 } ^ { * } , G ^ { \prime } , H ^ { \prime } ) \cos 2 ( l ^ { \prime } { + } g ^ { \prime } { + } h _ { i } { - } n _ { e } \ell ) . } \end{array}
$$

该式右端最后一项F\*即通约项，其由来请见第五章（5.204)和(5.215)式．为了方便,这里已取 $\iota _ { 0 } = 0 , S _ { 2 } , \iota = 0$

对于第一种情况,通约现象表现在əF\*/2G'=0,即1-5cos²·i'$= 0$ ，这就是 $\pmb { i } = \pmb { i } _ { o } = 6 3 ^ { \circ } 2 6 ^ { \prime }$ 的临界角问题。而后一种情况的通约现象对应n'一n=0．对于这两种情况,按一般变换方法构造小参数 $\pmb { \varepsilon }$ 的幂级数解时，都会出现小分母．但是，只要对消除 $\iota$ 后的新系统(对应F\*),采用经典摄动法(参考解对应无摄运动)分别把上述两种通约情况的 $\pmb { g } ^ { \prime }$ 和 $( l ^ { \prime } - n _ { o } t )$ 都当作慢变量，则小分母问题即可解除，在第五章中曾讨论过：而这里将仍从变换方法的角度来讨论通约情况下如何构造幂级数解以及通约现象的力学特征。[14],[15]

上述两种通约情况都可以简化为一个自由度系统，而且相应的F\*又可以统一写成一种形式。对于第一种情况,有两个循环坐标 $\imath ^ { \prime }$ 和 $\overrightarrow { \lambda } ^ { \prime }$ ，因此存在两个积分，即

$$
{ \pmb { L } } ^ { \prime } { = } { \pmb { L } } _ { 0 } ^ { \prime } , { \pmb { H } } ^ { \prime } { = } { \pmb { H } } _ { 0 } ^ { \prime } .
$$

于是简化成一个自由度 $( G ^ { \prime } , g ^ { \prime } )$ 系统：

$$
\begin{array} { r l } & { F ^ { * } { = } F ^ { * } ( G ^ { \prime } , g ^ { \prime } ) } \\ & { \quad \cdot = F _ { 1 } ^ { * } ( G ^ { \prime } ) + F _ { 2 o } ^ { * } ( G ^ { \prime } ) + F _ { 2 l } ^ { * } ( G ^ { \prime } ) \cos { 2 g ^ { \prime } } . } \end{array}
$$

原（7.301）式右端的 $\pmb { \cal { F } } _ { 0 } ^ { * } ( L ^ { \prime } )$ 已略去，它对讨论 $( G ^ { \prime } , g ^ { \prime } )$ 问题无用.若令

$$
\pmb { y } = \pmb { G } ^ { \prime } , \pmb { x } = \pmb { g } ^ { \prime } ,
$$

则上述 $\pmb { F } ^ { \star }$ 可写成下列形式：

$$
F \left( y , x \right) = A _ { 0 } \left( y \right) + A _ { 1 } \left( y \right) \cos { 2 x } .
$$

其中

$$
\left. \begin{array} { l } { { A _ { \uparrow } \left( y \right) = F _ { \textrm { i } } ^ { * } \left( y \right) + F _ { \textrm { 2 } c } ^ { * } \left( y \right) , A _ { \textrm { i } } \left( y \right) = F _ { \textrm { 2 } i } ^ { * } \left( y \right) , } } \\ { { \left| A _ { \ l } \right| / \left| A _ { 0 } \right| = O \left( e \right) , } } \end{array} \right\}
$$

这里 $\pmb { \mathcal { E } } = \pmb { J _ { 2 } }$ ·

对于第二种情况，亦可简化成上列形式．首先按（7.152）和(7.154)式引进无奇点变量：

$$
\left. \begin{array} { l } { { \widetilde { L } = L ^ { \prime } / q , \widetilde { l } = \left( q l ^ { \prime } - p l _ { 1 } \right) + p \left[ \left( g ^ { \prime } + h ^ { \prime } \right) - \left( g _ { 1 } + \hbar _ { 1 } \right) \right] } } \\ { { \widetilde { G } = G ^ { \prime } - \widetilde { L } , \widetilde { g } = g ^ { \prime } , } } \\ { { \widetilde { H } = H ^ { \prime } - \widetilde { L } , \widetilde { h } = h ^ { \prime } . } } \end{array} \right\}
$$

其中 $p / q$ 是相应的通约比，对这里要讨论的问题，有

$$
\left. \begin{array} { l } { p = q = 1 , } \\ { l _ { 1 } + g _ { 1 } + h _ { 1 } = n _ { e } t . } \end{array} \right\}
$$

相应的哈密顿函数变为

$$
\begin{array} { l } { { \displaystyle { \cal F } ^ { * } = { \cal F } _ { 0 } ^ { * } ( { \tilde { L } } ) + { \cal F } _ { 1 } ^ { * } ( { \tilde { L } } , { \tilde { G } } , { \widetilde { H } } ) + { \cal F } _ { 2 c } ^ { * } ( { \tilde { L } } , { \tilde { G } } , { \widetilde { H } } ) + { \cal F } _ { 2 r } ^ { * } ( { \tilde { L } } , { \tilde { G } } , { \widetilde { H } } ) \cos 2 } } \\ { { \displaystyle { \cal F } _ { 0 } ^ { * } ( { \tilde { L } } ) = \frac { 1 } { 2 { \cal \widetilde { L } } ^ { 2 } } + n _ { e } { \tilde { L } } } . } \end{array}
$$

通约现象对应的 ${ \pmb n } ^ { \prime } - { \pmb n } _ { e } { = } 0$ 即 ${ \partial F _ { 0 } ^ { * } } / { \partial \tilde { L } } { = } 0$ ，新系统同样有两个循环坐标 $\tilde { \pmb g }$ 和 $\tilde { h }$ ，存在两个积分：

$$
\begin{array} { r } { \widetilde { G } = \widetilde { G } _ { 0 } , \widetilde { H } = \widetilde { H } _ { 0 } . } \end{array}
$$

这也可简化成一个自由度 $( \tilde { L } , \tilde { l } )$ 系统：

$$
\begin{array} { r l } & { F ^ { * } = F ^ { * } \left( \tilde { L } , \tilde { l } \right) } \\ & { \quad = F _ { 0 } ^ { * } \left( \tilde { \mathcal { L } } \right) \cdots F _ { 1 } ^ { * } \left( \tilde { L } \right) + F _ { 2 c } ^ { * } ( \tilde { L } ) + F _ { 2 i } ^ { * } ( \tilde { L } ) \cos 2 \tilde { l } . } \end{array}
$$

$$
y = 1 , x = 1 .
$$

则 ${ \pmb { F } } ^ { \star }$ 就可写成(7.305)式的形式：

$$
F ( y , x ) = A _ { 0 } ( y ) + A _ { 1 } ( y ) \cos 2 x ,
$$

其中

$$
\left. \begin{array} { l } { { A _ { 0 } ( y ) = { \cal F } _ { 0 } ^ { \ast } ( \widetilde { L } ) \div { \cal F } _ { 1 } ^ { \ast } ( \widetilde { L } ) + { \cal F } _ { 2 c } ^ { \ast } ( \widetilde { L } ) , } } \\ { { A _ { 1 } ( y ) = { \cal F } _ { 2 r } ^ { \ast } ( \widetilde { L } ) , } } \\ { { \left. \begin{array} { r l } { { | A _ { 1 } | / \left/ \left/ \left[ A _ { 0 } \right| = { \cal O } ( \varepsilon ) , \right. \right. } } \end{array} \right\} } } \end{array} \right.
$$

这里 $\pmb { \varepsilon } = J _ { 2 } , \mathbf { \varepsilon } _ { 2 } .$

对于第一种情况，只考虑 ${ { J } _ { 2 } }$ 项摄动时，有

$$
A _ { 1 } ( y ) < 0 ,
$$

而同时考虑 $\pmb { J _ { 2 } }$ 和 $\pmb { J _ { 4 } }$ 项时，却有

$$
A _ { 1 } ( y ) { > } 0 ,
$$

对于第二种情况，有

$$
A _ { 1 } ( y ) > 0 ,
$$

为了使下面的讨论同时适用两种情况，令

$$
\left. \begin{array} { l } { { \displaystyle \xi = x + \frac { 1 } { 4 } \pi [ 1 + \mathrm { s g n } ( A _ { \mathrm { i } } ) ] , } } \\ { { } } \\ { { \displaystyle A ( y ) = \left| A _ { 1 } ( y ) \right| , } } \\ { { } } \\ { { \displaystyle B ( y ) = A _ { 0 } ( y ) - \left| A _ { 1 } ( y ) \right| . } } \end{array} \right\}
$$

其中 $\mathfrak { s g n } ( A _ { 1 } )$ 是符号函数：

$$
\mathrm { s g n } ( A _ { 1 } ) = \left\{ \begin{array} { l l } { { - 1 , A _ { 1 } < 0 , } } \\ { { 1 , A _ { 1 } > 0 . } } \end{array} \right.
$$

于是有

$A _ { 1 } \cos 2 x = | A _ { 1 } | \ : \mathrm { s g n } \left( A _ { 1 } \right) \cos 2 x = - \ : | A _ { 1 } | \ : \cos 2 \xi ,$ 在上述变换下,系统F(y,x)变为F(y,),并有

$$
\begin{array} { c } { { F ( y , \xi ) = A _ { 0 } - \left\{ A _ { 1 } \right\} + \left\{ A _ { 1 } \right\} ( 1 - \cos { 2 \xi } ) } } \\ { { { } } } \\ { { = B ( y ) + 2 A ( y ) \sin ^ { 2 } \xi , } } \\ { { { } } } \\ { { A ( y ) / \left. B ( y ) \right. = O ( \varepsilon ) . } } \end{array}
$$

两种情况的小分母均对应

$$
B ^ { \prime } ( y ) = \frac { \partial B } { \partial y } { \approx } 0 .
$$

若用变换方法(例如Zeipel方法)按ε的幂构造级数解,新变

量记作 $y ^ { \prime } , \pmb { \xi } ^ { \prime }$ ，相应的生成函数和变换后的哈密顿函数分别为。

$$
\begin{array} { l } { { \displaystyle \pmb { \cal S } = \pmb { \jmath } ^ { \prime } \pmb { \xi } + \pmb { \cal S } _ { 1 } ( \pmb { y } ^ { \prime } , \pmb { \xi } ) + \cdots , } } \\ { { \displaystyle \pmb { \cal F } ^ { * } = \pmb { \cal F } _ { 0 } ^ { * } ( \pmb { y } ^ { \prime } ) + \pmb { \cal F } _ { 1 } ^ { * } ( \pmb { y } ^ { \prime } ) + \cdots . } } \end{array}
$$

有

$$
\begin{array} { r l } & { F _ { 0 } ^ { * } \left( \boldsymbol { y } ^ { \prime } \right) = B \left( \boldsymbol { y } ^ { \prime } \right) , } \\ & { F _ { 1 } ^ { * } \left( \boldsymbol { y } ^ { \prime } \right) = A \left( \boldsymbol { y } ^ { \prime } \right) , } \\ & { \displaystyle \left( \frac { \partial S _ { 1 } } { \partial \boldsymbol { \xi } } \right) = \frac { A \left( \boldsymbol { y } ^ { \prime } \right) } { B ^ { \prime } \left( \boldsymbol { y } ^ { \prime } \right) } \mathrm { c o s } 2 \boldsymbol { \xi } , } \\ & { \displaystyle \ldots \ldots \ldots . } \end{array}
$$

小分母即出现在生成函数 $\pmb { \ S } _ { 1 }$ 中，从而也就出现在由 $\pmb { \ S _ { 1 } }$ 构成的周期项中，但是,若用同样的 Zeipel方法,改按 $\sqrt { e }$ 的幂构造级数解就不一样了,有

$$
S = y ^ { \prime } \xi + S _ { 1 / 2 } ( y ^ { \prime } , \xi ) + S _ { 1 } ( y ^ { \prime } , \xi ) + \cdots
$$

相应的变换关系为

$$
\left. \begin{array} { c } { { y = y ^ { \prime } + \displaystyle \frac { \partial S _ { 1 / 2 } } { \partial \xi } + \cdots , } } \\ { { \xi = \xi ^ { \prime } - \displaystyle \frac { \partial S _ { 1 / 2 } } { \partial y ^ { \prime } } - \cdots . } } \end{array} \right\}
$$

$\pmb { S } _ { 1 / 2 } , \pmb { S } _ { 1 } , \cdots$ 由下列关系确定(即要求变换后消除 $\xi )$ ：

$$
\begin{array} { r l r } {  { \mathrm {  ~ \tilde { \Sigma } ^ * = } F _ { 0 } ^ { * } + F _ { 1 } ^ { * } + \cdots } } \\ & { } & { = B ( y ^ { t } ) + B ^ { \prime } \biggl ( \frac { \partial S _ { 1 / 2 } } { \partial \xi } + \frac { \partial S _ { 1 } } { \partial \xi } + \cdots \biggr ) + \frac { 1 } { 2 } \ B ^ { \prime \prime } \biggl ( \frac { \partial S _ { 1 / 2 } } { \partial \xi } + \cdots \biggr ) ^ { 2 } + \cdots } \\ & { } & { + 2 A ( y ^ { \prime } ) \sin ^ { 2 } \xi + \cdots . } \end{array}
$$

若 $B ^ { \prime }$ 的量级明显大于 $\pmb { \mathcal { E } } ^ { 1 / 2 }$ ，则属正常情况，无小分母问题，也不必按 $\sqrt { e }$ 构造级数解。因此可假定 $B ^ { \prime } { = } O \left( \varepsilon ^ { 1 / 2 } \right)$ ,若其量级更小亦无妨．比较(7.321)式两端 $\sqrt { \varepsilon }$ 的同次幂,有

0阶： $\overrightarrow { F } _ { 0 } ^ { * } = \overrightarrow { B } ( y ^ { \prime } )$ ，

$$
F _ { 1 } ^ { * } = B ^ { \prime } \bigg ( { \frac { \partial S _ { 1 / 2 } } { \partial \xi } } \bigg ) + \frac { 1 } { 2 } ~ B ^ { \prime \prime } \bigg ( { \frac { \partial S _ { 1 / 2 } } { \partial \xi } } \bigg ) ^ { 2 } + 2 A ( y ^ { \prime } ) \sin ^ { 2 } \xi ,
$$

注意，对于上述两种通约情况，均有 $B ^ { \prime \prime } > 0$ 。（7.323）式可以按下列形式分成两部分，即让

$$
F _ { 1 } ^ { * } { = } A ( y ^ { \prime } ) ,
$$

其余各项用来确定 $\pmb { \ S _ { 1 / 2 } } .$ 但为了讨论清楚起见，也可以分成下列两个部分：

$$
F _ { 1 } ^ { * } ( y ^ { \prime } ) { = } 0 ,
$$

$$
\Big ( \frac { \partial S _ { 1 / 2 } } { \partial \xi } \Big ) ^ { 2 } + \frac { 2 B ^ { \prime } } { B ^ { \prime \prime } } \Big ( \frac { \partial S _ { 1 / 2 } } { \partial \xi } \Big ) + \frac { 4 A } { B ^ { \prime \prime } } \mathrm { s i n } ^ { \mathrm { ~ 2 ~ } } \xi = 0
$$

若令

$$
\left. \begin{array} { c } { { P \mp B ^ { \prime } / B ^ { \prime \prime } , } } \\ { { \frac { 4 A } { B ^ { \prime \prime } } { = } \displaystyle \frac { B ^ { \prime 2 } } { B ^ { \prime \prime } { } ^ { 2 } } { \cdot } \frac { 4 A B ^ { \prime \prime } } { B ^ { \prime 2 } } { = } P ^ { 2 } \alpha ^ { - 2 } , } } \\ { { | \alpha | { = } \displaystyle \frac { | B ^ { \prime } | } { 2 \sqrt { A B ^ { \prime \prime } } } . } } \end{array} \right\}
$$

则(7.324)式变为

$$
\begin{array} { r } { \Big ( \frac { \partial S _ { 1 / 2 } } { \partial \xi } \Big ) + 2 P \Big ( \frac { \partial S _ { 1 / 2 } } { \partial \xi } \Big ) + P ^ { 2 } \alpha ^ { - 2 } \sin ^ { 2 } \xi = 0 , } \end{array}
$$

解为

$$
\scriptstyle \left( { \frac { \partial S _ { 1 / 2 } } { \partial \xi } } \right) = \left[ 1 \pm { \sqrt { 1 - \alpha ^ { - 2 } \sin ^ { 2 } \xi } } \right] P .
$$

若要 $\pmb { S } _ { 1 / 2 }$ 能够确定，则应满足

$$
1 - \alpha ^ { - 2 } \sin ^ { 2 } \xi \ge 0 .
$$

确定 $\pmb { S } _ { 1 / 2 }$ 的(7.326)式表明两点：

(1） $\pmb { B ^ { \prime } }$ 不再出现于分母中，小分母问题解除．关于“高阶”项$\bar { \mathcal { S } } _ { 1 } , \bar { S } _ { 3 / 2 9 } \cdots ,$ 亦是如此，这说明按 $\sqrt { \varepsilon }$ 的幂构造级数解确能消除通约奇点．但是,组成 $\pmb { S } _ { 1 / 2 9 } \pmb { S } _ { 1 } ,$ …的项不再是三角函数，而是椭圆函数，因此,尽管小分母消失,这样构造的级数解不便于具体应用.

(2）条件(7.327)式应与真实运动相符，那么，当 $| \alpha | < 1$ 时，$\pmb { \xi }$ 的变化要受到限制；而当 $| \alpha | > 1$ 时， ${ \pmb \xi }$ 的变化不受限制； $| \alpha | = 1$ 则为临界状况．根据(7.325)式定义的 $| a |$ 可知，上述条件表明，当$B ^ { \prime }$ 的量级明显大于 $\sqrt { \varepsilon }$ 时，运动属正常情况,即前面提到的无通约问题；而当 $B ^ { \prime }$ 的量级小于 $\sqrt { \varepsilon }$ 时(对应 $| \alpha | < 1 )$ ，运动将出现“奇异”现象，即天平动(Libration)．如临界倾角问题中，拱线方向是摆动而不是旋转； $2 4 ^ { \mathtt { h } }$ 地球同步卫星的会合经度 $\tilde { \pmb { l } }$ 的值也是在某一值附近波动，即卫星在地球上空某一平衡位置附近摆动，这一“奇异”现象就是通约问题的力学特征．新旧变量的差别(即轨道变化中共振周期项的大小),通过 $\pmb { S } _ { 1 / 2 }$ 取决于 $B ^ { \prime }$ 的量级，当 $B ^ { \prime }$ 愈接近零值时,相应周期项的振幅就变得愈小，而不是“无限”增大，其最大的量级也就是 $\sqrt { \varepsilon }$ ，这就是通约条件下轨道变化的一个基本特征，它更清楚地阐明了第六章中提出的通约现象的力学本质.

# 7.9一般变换方法

无论是Zeipel方法还是Hori-Deprit方法，从数学角度来看，显然要比第五章介绍的平均根数法清楚得多，而且构造级数解的过程也明显地简单．简单的原因当然是采用了由生成函数构造正则变换的方法，把各根数的变化通过一个生成函数来表达．但是，这付出的代价是放弃了引用既直观又具有明显几何意义的椭圆根数作为基本变量，而必须引用正则共轭变量;尽管两种变量之间的变换关系还是简单的，但总有些不便(如不能从正则共轭变量的变化直接看出相应根数的某些变化特征等)；而且对非保守系统不适用,即便形式上推广到耗散系统，正则变换的优点仍然消失。因此，为了使其适用性更广，又保持这些变换方法的独特构思(寻找特殊的变换，简化动力系统，直至给出摄动解)，曾有过推广Lie变换的方法[7],使其适用于非保守系统．但从应用角度来看，Lie变换本身较烦，局限于其原有的变换形式没有必要．作者仅抓住变换思想的特点作了一般性的推广[18]-[20]，本节就介绍这一内容.

# 1．方法的基本原理

对具有n个自由度的非线性摄动系统，若用坐标和速度(或类似的变量)作为基本变量，则对应的运动方程将构成一个2n阶非：线性常微分方程组．用 $\pmb { x }$ 和 $\pmb { z }$ 分别表示坐标向量和速度向量：

$$
\begin{array} { r } { \boldsymbol { x } = \left( \begin{array} { c } { x _ { 1 } } \\ { x _ { 2 } } \\ { \vdots } \\ { x _ { n } } \end{array} \right) , \boldsymbol { \mathrm { Z } } = \left( \begin{array} { c } { Z _ { 1 } } \\ { Z _ { 2 } } \\ { \vdots } \\ { Z _ { n } } \end{array} \right) . } \end{array}
$$

若记

$$
\sigma = \binom { { \cal Z } } { x } , ~ .
$$

则相应的运动方程可写为：

$$
\frac { d \sigma } { d t } { = } f ( \sigma , t ; \varepsilon ) ,
$$

$\pmb { \varepsilon }$ 是小参数， $f$ 为 ${ \pmb 2 } { \pmb n }$ 维向量函数.

通常 $\pmb { x }$ 选用角坐标(如 $\Omega , \omega , M )$ ， $\mathbf { z }$ 选用角动量或矩(如 ${ \pmb { a } } , { \pmb { e } } _ { \pmb { \mathscr { s } } }$ $i )$ ；而它们不必是正则共轭变量. $\pmb { x }$ 的各分量的变化常有快慢之分相应地被称为快变量（如 $M$ )和慢变量(如 $a$ 和 $\pmb { \omega }$ ）；包含快变量的项(或同时包含慢变量，但该项的性质取决于快变量)即短周期项，只包含慢变量的项则为长周期项．若方程组(7.330）式的解能由这些周期项和随时间 $\pmb { t }$ 线性变化的长期项组成，则可用变换方法直接求解；即便长期项随 $\pmb { \mathscr { t } }$ 的变化不是线性的，也可以通过变换分离出周期项，以达到简化方程组的目的．相应的变换关系可取为

$$
\pmb { \sigma } = \pmb { \sigma } ^ { \prime } + \sum _ { m \geq 1 } \sigma _ { g } ^ { ( m ) } \left( Y , x , t ; \varepsilon ^ { m } \right) ,
$$

或

$$
\sigma = \sigma ^ { \prime } + \sum _ { m \geq 1 } \sigma _ { s } ^ { ( m ) } \left( \sigma ^ { \prime } , t ; \varepsilon ^ { m } \right) ,
$$

其中 $\pmb { \sigma } ^ { \prime }$ 为新变量：

$$
\scriptstyle \sigma ^ { \prime } = { \binom { Y } { y } } ,
$$

$\pmb { Y }$ 和 $\pmb { y }$ 均为 $\pmb { \mathscr { n } }$ 维向量，分别对应 $\pmb { z }$ 和 $\pmb { \mathcal { Z } }$ ， $\pmb { \sigma } _ { \textbf { \textsc { g } } } ^ { \{ m \} }$ 为 $\pmb { m }$ 阶周期项，相应地记为

$$
\begin{array} { r } { \sigma _ { \mathcal { S } } ^ { ( m ) } = \binom { Y _ { \mathcal { B } } ^ { ( m ) } } { y _ { \mathcal { B } } ^ { ( m ) } } , } \end{array}
$$

$\pmb { Y } _ { s } ^ { ( n ) }$ 和 $y _ { \delta } ^ { ( m ) }$ 都是待定的，在构造级数解的过程中确定，具有正则变换中生成函数所起的作用．上面第一种变换关系是由混合变量组成的隐函数形式，类似于Zeipel变换；而后一种变换则为显函数形式,类似于Lie变换.

在上述变换下,新变量所满足的常微分方程可写成下列形式：

$$
\begin{array} { l } { \displaystyle \frac { d \sigma ^ { \prime } } { d t } { = } \frac { \partial \sigma ^ { \prime } } { \partial \sigma } \cdot f ( \sigma , t ; e ) + R } \\ { R = \Big ( \frac { \partial \sigma ^ { \prime } } { \partial t } \Big ) . } \end{array}
$$

这里的 $\pmb { R }$ 称为变换的余函数,若变换不显含 $\pmb { \mathscr { t } }$ ，则 $\pmb { R } = 0 , \frac { 2 \sigma ^ { \prime } } { \partial \sigma }$ 是变换矩阵.

对于隐形式,有

$$
\sigma ^ { \prime } { = } \sigma { - } \sigma _ { s } ( \sigma ^ { \prime } , \sigma , t ) ,
$$

$\sigma _ { \mathcal { S } }$ 中出现的 ${ \pmb \sigma } ^ { \prime }$ 即新变量 $\mathcal { T } , \sigma$ 则为原变量 $\pmb { \mathcal { X } }$ ，引进算符D:

$$
\begin{array} { r } { \mathbf { D } { = } \displaystyle \frac { \partial } { \partial ( \vec { Y } , x ) } , } \end{array}
$$

它表示对 $\pmb { 2 \mathscr { n } }$ 维向量 $\binom { Y } { x }$ 求偏导数，于是有

$$
\begin{array} { l } { { \displaystyle { \frac { \partial \sigma ^ { \prime } } { \partial \sigma } } = E - \frac { \partial } { \partial \sigma } \underset { \bf n } { \sum } \sigma _ { s } ^ { ( m ) } } } \\ { { \displaystyle ~ = E - \frac { \partial } { \partial ( Y , x ) } \sum _ { \bf n } \sigma _ { s } ^ { \langle m \rangle } \Bigg ( \frac { \partial Y } { \partial \sigma } \Bigg ) } } \\ { { \displaystyle ~ = E - \mathrm { D } \sum _ { \bf n } \sigma _ { s } ^ { \langle m \rangle } ~ \left( E _ { 1 } - \mathrm { D } \sum _ { \bf n } Y _ { s } ^ { \langle m \rangle } ~ ( E _ { 1 } - D \Sigma Y ~ _ { s } ^ { \langle m \rangle } ~ ( E _ { 1 } - \cdots ) \right) } } \\ { { \displaystyle ~ = E + \mathrm { D } \sum _ { \bf n } \sigma _ { s } ^ { \langle m \rangle } ~ \sum _ { { \bf k \uparrow } } ( - 1 ) ^ { k } \Bigg ( \mathrm { D } \sum _ { \bf n } Y _ { s } ^ { \langle m \rangle } ~ \sigma _ { s } ^ { k - 1 } ~ ( 7 . 3 ) ~ } } \end{array}
$$

该式右端的 $\pmb { \cal E }$ 为 ${ \mathfrak { 2 } } { \mathfrak { n } }$ 阶单位阵,其余各项亦应为 ${ \pmb 2 } \pmb { n }$ 阶方阵或 ${ \pmb 2 } { \pmb n }$ 阶向量；但 $\pmb { { \cal E } } _ { 1 }$ 实为 $\pmb { \mathscr { n } }$ 阶单位阵, $\pmb { Y } _ { s } ^ { ( m ) }$ 是 $\pmb { \mathscr { n } }$ 阶列向量．为此，就分别用零元素补充到 $2 \pi$ 阶,不过，各元素的排列次序同前，下面也将有类似情况，不再说明， $\left( \begin{array} { c } { \mathbf { D } \sum _ { n } Y _ { \delta } ^ { \langle m \rangle } } \end{array} \right) ^ { k - }$ 表示矩阵乘幂，当 $\pmb { k } = 1$ 时，该项为单位阵。与变换矩阵 $\frac { \partial \sigma ^ { \prime } } { \partial \sigma }$ 的表示方法类似，变换的余函数 $\pmb { \cal R }$ 有如下形式：

$$
\left( \frac { \partial \sigma ^ { \prime } } { \partial t } \right) = - \sum _ { m } \left( \frac { \partial \sigma _ { \vartheta } ^ { ( m ) } } { \partial t } \right)
$$

$$
+ \bigg ( \sum _ { k \geqslant 0 } ( - 1 ) ^ { k } \frac { \partial } { \partial \bar { Y } } \sum _ { m } \sigma _ { \beta } ^ { ( m ) } ~ \left( \frac { \partial } { \partial \bar { Y } } \sum _ { m } Y _ { \vartheta } ^ { ( m ) } ~ \right) ^ { k } \bigg ) \sum _ { \mathfrak { m } } \bigg ( \frac { \partial Y _ { s } ^ { ( m ) } } { \partial \ell } \bigg ) ,
$$

相应的方程(7.335)右端的 $f$ 亦应表示成混合变量形式,即

$$
f ( \sigma , t ; \varepsilon ) = f ( Y , x , t ; \varepsilon ) + \sum _ { k \geqslant 1 } { \frac { 1 \partial ^ { k } f } { k ! \partial Y ^ { k } } } { \left( \sum _ { m } Y _ { \vartheta } ^ { ( m ) } \right) } ^ { k } .
$$

对于显形式,有

$$
\sigma ^ { \prime } = \sigma - \sigma _ { s } ( \sigma ^ { \prime } , t ) .
$$

引进算符 $\mathbf { D ^ { \prime } }$ ：

$$
{ \bf D } ^ { \prime } = \frac { \partial } { \partial \sigma ^ { \prime } } ,
$$

它表示对 ${ \pmb 2 } { \pmb n }$ 维向量 $\binom { Y } { y }$ 求偏导数，相应的 ${ \frac { \partial \sigma ^ { \prime } } { \partial \sigma } } ,$ $f$ 和 $\pmb { R }$ 分别由下列各式表达：

$$
\frac { \partial \sigma ^ { \prime } } { \partial \sigma } = E + \sum _ { k \geq 1 } ( - 1 ) ^ { k } \bigg ( \mathrm { D } ^ { \prime } \sum _ { m } \sigma _ { \mathscr { S } } ^ { ( m ) } \bigg ) ^ { k } ,
$$

$$
{ \bigg ( } \frac { \partial \sigma ^ { \prime } } { \partial t } { \bigg ) } = - { \bigg ( } \sum _ { k \geqslant 0 } ( - 1 ) ^ { k } { \bigg ( } \mathrm { D } ^ { \prime } \sum _ { m } \sigma _ { s } ^ { ( m ) } { \bigg ) } ^ { k } { \bigg ) } \sum _ { m } { \bigg ( } \frac { \partial \sigma _ {  { s } } ^ { ( m ) } } { \partial t } { \bigg ) } ,
$$

$$
f ( \sigma , t ; \varepsilon ) = f ( \sigma ^ { \prime } , \varepsilon , t ) + \sum _ { \varepsilon \geqslant 1 } \frac { 1 } { k ! } \mathrm { D } ^ { \prime } \bigg ( \sum _ { m } \sigma _ { s } ^ { ( m ) } \bigg ) ^ { k } .
$$

原方程（7.330）式的右函数 $f$ 可展为小参数 $\pmb { \varepsilon }$ 的收敛幂级数（通常为有限项）,即

$$
f ( \sigma , t ; \varepsilon ) = f _ { 0 } \left( z \right) + \sum _ { k \geqslant u } f _ { k } \left( z , x , t ; \varepsilon ^ { k } \right) ,
$$

其中 $f _ { k } \left( z , \ x , \ t ; \ \varepsilon ^ { k } \right) = O ( \varepsilon ^ { k } )$ ，将(7.339)—(7.341)式代入方程(7.335),即得第一种变换后新变量 $\sigma ^ { \prime }$ 所满足的运动方程：

$$
\frac { d \sigma ^ { \prime } } { d t } { = } f ^ { * } ( Y , x , t ; \ \varepsilon ) { = } \displaystyle { \sum _ { k \geqslant 0 } } f _ { k } ^ { * } ( Y , x , t ; \varepsilon ^ { k } ) .
$$

其中

$$
\begin{array} { r l } & { f _ { 1 } ^ { \ast } = f _ { 1 } ( Y , x , t ; \varepsilon ) \cdot \frac { \partial f _ { 0 } } { \partial Y } Y _ { \varepsilon } ^ { ( 0 ) } \cdot \mathrm { \partial } \mathrm { \partial } \sigma _ { \varepsilon } ^ { ( 0 ) } \cdot f _ { 0 } - \biggl ( \frac { c \sigma _ { \varepsilon } ^ { ( 0 , \varepsilon ) } } { \partial t } \biggr ) , \qquad \mathrm { ( f ~ } } \\ & { f _ { 2 } ^ { \ast } = f _ { 2 } ( Y , x , t ; \varepsilon ^ { 2 } ) + \frac { \partial f _ { 1 } } { \partial Y } Y _ { \varepsilon } ^ { ( 0 ) } + \frac { 1 } { 2 } \frac { \partial ^ { 2 } f _ { 0 } } { \partial Y ^ { 2 } } Y _ { \varepsilon } ^ { ( 0 ) } + \frac { \partial f _ { 0 } } { \partial Y } Y _ { \varepsilon } ^ { ( 0 ) } } \\ & { \qquad + \left( - \mathrm { D } \sigma _ { \varepsilon } ^ { ( 0 ) } + \mathrm { D } \sigma _ { \varepsilon } ^ { ( 0 ) } \mathrm { D } Y _ { \varepsilon } ^ { ( 0 ) } \right) f _ { 0 } - \mathrm { D } \sigma _ { \varepsilon } ^ { ( 0 ) } \biggl ( f _ { 1 } + \frac { \partial f _ { 0 } } { \partial \tilde { Y } } Y _ { \varepsilon } ^ { ( 0 ) } \biggr ) } \\ & { \qquad - \biggl ( \frac { \partial \sigma _ { \varepsilon } ^ { ( 0 ) } } { \partial t } \biggr ) + \frac { \partial \sigma _ { \varepsilon } ^ { ( 0 ) } } { \partial Y } \biggl ( \frac { \partial Y _ { \varepsilon } ^ { ( 0 ) } } { \partial t } \biggr ) , \qquad \ \mathrm { ( f ~ } } \\ & { f _ { 3 } ^ { \ast } = f _ { 3 } ( Y , x , t ; \varepsilon ^ { 3 } ) + \frac { \partial f _ { 2 } } { \partial Y } Y _ { \varepsilon } ^ { ( 0 ) } + \frac { \partial f _ { 1 } } { \partial Y } Y _ { \varepsilon } ^ { ( 0 ) } + \frac { 1 } { 2 } \frac { \partial ^ { 2 } f _ { 1 } } { \partial Y _ { 2 } } Y _ { \varepsilon } ^ { ( 0 ) } } \end{array}
$$

$$
\begin{array} { r l } & { + \underbrace { 1 } \frac { \partial ^ { 3 } f _ { 0 } } { \partial Y ^ { 3 } } Y _ { s } ^ { ( 1 ) ^ { 3 } } + \frac { \partial ^ { 2 } f _ { 0 } } { \partial Y ^ { 2 } } Y _ { s } ^ { ( 1 ) } Y _ { s } ^ { ( 2 ) } + \frac { \partial f _ { 0 } } { \partial Y } Y _ { s } ^ { ( 0 ) } \cdot } \\ & { + ( -  { \mathbf Ḋ \sigma Ḍ } _ { s } ^ { ( 3 ) } +  { \mathbf Ḋ \sigma Ḍ } _ { s } ^ { ( 1 ) }  { \mathbf Ḋ \sigma Ḍ } _ { s } ^ { ( 3 ) } +  { \mathbf Ḋ \sigma Ḍ } _ { s } ^ { ( 2 ) }  { \mathbf Ḋ \sigma Ḍ } _ { s } ^ { ( 3 ) } -  { \mathbf Ḋ \sigma Ḍ } _ { s } ^ { ( 1 ) }  { \mathbf Ḋ \sigma Ḍ } _ { s } ^ { ( 3 ) }  { \mathbf Ḋ Y  Ḍ } _ { s } ^ { ( 3 ) } ) f _ { s } } \\ & { + ( -  { \mathbf Ḋ \sigma Ḍ } _ { s } ^ { ( 2 ) } +  { \mathbf Ḋ \sigma Ḍ } _ { s } ^ { ( 3 ) }  { \mathbf Ḋ \sigma Ḍ } _ { s } ^ { ( 1 ) } ) \Big ( f _ { 1 } + \frac { \partial f _ { 0 } } { \partial Y } Y _ { s } ^ { ( 0 ) } \Big ) } \\ & { + ( -  { \mathbf Ḋ \sigma Ḍ } _ { s } ^ { ( 1 ) } ) \left( f _ { 2 } + \frac { \partial f _ { 1 } } { \partial Y } Y _ { s } ^ { ( 1 ) } + \frac { \partial f _ { 0 } } { \partial Y } Y _ { s } ^ { ( 0 ) } + \frac { 1 } { 2 } \frac { \partial ^ { 2 } f _ { 0 } } { \partial Y ^ { 2 } } Y _ { s } ^ { ( 1 ) ^ { 2 } } \right) } \\ &  - \Big ( \frac { \partial \sigma _ { s } ^ { ( 3 ) } } { \partial t } \Big ) + \frac { \partial \sigma _ { s } ^ { ( 2 ) } } { \partial Y } \Big ( \frac { \partial Y _ { s } ^ { ( 0 ) } } { \partial t } \Big ) + \frac { \partial \sigma _ { s } ^ { ( 3 ) } } { \partial Y } \Big ( \frac { \partial Y _ { s } ^ { ( 2 ) } } { \partial t } \Big ) - \frac { \partial \sigma _ { s } ^ { ( 1 ) } } { \partial Y } \partial Y _ { s } ^ { ( 0 ) } \Big ( \frac { \partial Y _ { s } ^ { ( 1 ) } }   \end{array}
$$

将(7.344)—(7.346)式代入方程(7.335)，即得显形式变换后新变量 $\sigma ^ { \prime }$ 所满足的运动方程：

其中

$$
\frac { d \sigma ^ { \prime } } { d t } { = } f ^ { * } ( \sigma ^ { \prime } , t ; \varepsilon ) = \sum _ { k \geqslant 0 } f _ { k } ^ { * } ( \sigma ^ { \prime } , t ; \varepsilon ^ { k } ) .
$$

$$
\begin{array} { r l } & { \begin{array} { r l } & { ( \vec { r } , 3 ) } \\ { f _ { 0 } ^ { * } = f _ { 0 } \left( \boldsymbol { y } \right) , } \end{array} } \\ & { \begin{array} { r l } & { f _ { 0 } ^ { * } = f _ { 0 } \left( \boldsymbol { \mathcal { x } } ^ { 0 } \right) , } \\ { f _ { 1 } ^ { * } = f _ { 1 } \left( \boldsymbol { \sigma } ^ { \prime } , t ; \boldsymbol { \varepsilon } \right) + \frac { \partial f _ { 0 } } { \partial Y } Y _ { \boldsymbol { \alpha } } ^ { ( 0 ) } - \mathbf { D } ^ { \prime } \boldsymbol { \sigma } _ { \boldsymbol { \nu } } ^ { ( 0 ) } \cdot f _ { 0 } - \left( \frac { \partial \boldsymbol { \sigma } _ { \boldsymbol { \nu } } ^ { ( 0 ) } } { \partial t } \right) , \qquad ( \boldsymbol { \tau } , 3 ) } \\ { \widehat { \mathcal { H } } ^ { * } _ { 2 } - f _ { 2 } \left( \boldsymbol { \sigma } ^ { \prime } , t ; \boldsymbol { \varepsilon } ^ { 2 } \right) + \mathrm { D } ^ { \prime } f _ { 1 } \cdot \boldsymbol { \sigma } _ { \boldsymbol { \delta } } ^ { ( 0 ) } + \frac { 1 } { 2 } \frac { \partial ^ { 2 } f _ { 0 } } { \partial Y ^ { 2 } } Y _ { \boldsymbol { \alpha } } ^ { ( 0 ) } - \frac { \partial } { \partial Y } Y _ { \boldsymbol { \beta } } ^ { ( 0 ) } , } \end{array} } \\ &  \begin{array} { r l } & { f _ { 0 } ^ { * } = f _ { 0 } ^ { * } + \mathrm { D } ^ { \prime } \boldsymbol { \sigma } _ { \boldsymbol { \nu } } ^ { ( 0 ) } D ^ { \prime } \boldsymbol { \sigma } _ { \boldsymbol { \nu } } ^ { ( 0 ) } ) f _ { 0 } - \mathrm { D } ^ { \prime } \boldsymbol { \sigma } _ { \boldsymbol { \nu } } ^ { ( 0 ) } \biggl ( f _ { 1 } - \frac { \partial ^ { 2 } f _ { 0 } } { \partial Y } Y _ { \boldsymbol { \alpha } } ^ { ( 0 ) } \biggr ) } \\ & { \qquad - \left( \frac { \partial \boldsymbol { \sigma } _ { \boldsymbol { \nu } } ^ { ( 0 ) } } { \partial t } \right) + \mathrm { D } ^ { \prime } \boldsymbol { \sigma } _ { \boldsymbol { \nu } } ^ { ( 0 ) } \biggl ( \frac { \partial \boldsymbol { \sigma } _ { \boldsymbol { \nu } } ^ { ( 0 ) } } { \partial t } \biggr ) , } \\  \mathrm  ~  { \varepsilon } -  \end{array} \end{array}
$$

$$
f _ { 3 } ^ { * } = f _ { 3 } ( \sigma ^ { \prime } , t , \varepsilon ^ { 3 } ) + \mathrm { D } ^ { \prime } f _ { 2 } \cdot \sigma _ { s } ^ { ( 1 ) } + \mathrm { D } ^ { \prime } f _ { 1 } \cdot \sigma _ { s } ^ { ( 2 ) } + \frac { 1 } { 2 } \mathrm { D } ^ { \prime 2 } f _ { 1 } \cdot \sigma _ { s } ^ { ( 1 ) 2 }
$$

$$
\begin{array} { r l } & { + \displaystyle \frac { 1 } { 6 } \frac { \partial ^ { 3 } f _ { 0 } } { \partial Y ^ { 3 } } Y _ { s } ^ { ( \scriptscriptstyle 1 ) 3 } + \frac { \partial ^ { 2 } f _ { 0 } } { \partial Y ^ { 2 } } Y _ { s } ^ { ( \scriptscriptstyle 1 ) } Y _ { s } ^ { ( \scriptscriptstyle 2 ) } + \frac { \partial f _ { 0 } } { \partial Y } Y _ { s } ^ { ( \scriptscriptstyle 3 ) } } \\ & { + \left( - \mathbf { D } ^ { \prime } \boldsymbol { \sigma } _ { s } ^ { ( \scriptscriptstyle 3 ) } + \mathbf { D } ^ { \prime } \boldsymbol { \sigma } _ { s } ^ { ( \scriptscriptstyle 2 ) } \mathbf { D } ^ { \prime } \boldsymbol { \sigma } _ { s } ^ { ( \scriptscriptstyle 1 ) } + \mathbf { D } ^ { \prime } \boldsymbol { \sigma } _ { s } ^ { ( \scriptscriptstyle 1 ) } \mathbf { D } ^ { \prime } \boldsymbol { \sigma } _ { s } ^ { ( \scriptscriptstyle 2 ) } - ( \mathbf { D } ^ { \prime } \boldsymbol { \sigma } _ { s } ^ { ( \scriptscriptstyle 1 ) } ) ^ { 3 } \right) f _ { 0 } } \end{array}
$$

$$
\begin{array} { r l } & { + \left( - \mathbf { D } ^ { \prime } \boldsymbol { \sigma } _ { s } ^ { \mathrm { ( 2 ) } } \cdot ( \mathbf { D } ^ { \prime } \boldsymbol { \sigma } _ { s } ^ { \mathrm { ( 1 ) } } ) ^ { 2 } \right) \left( f _ { 1 } + \frac { \partial f _ { 0 } } { \partial Y } Y _ { s } ^ { \mathrm { ( 1 ) } } \right) } \\ & { + \left( - \mathbf { D } ^ { \prime } \boldsymbol { \sigma } _ { s } ^ { \mathrm { ( 1 ) } } \right) \bigg ( f _ { 2 } + \mathbf { D } ^ { \prime } f _ { 1 } \cdot \boldsymbol { \sigma } _ { s } ^ { \mathrm { ( 1 ) } } + \frac { \partial f _ { 0 } } { \partial Y } Y _ { s } ^ { \mathrm { ( 1 ) } } + \frac { 1 } { 2 } \frac { \partial ^ { 2 } f _ { 0 } } { \partial Y ^ { 2 } } Y _ { s } ^ { \mathrm { ( 1 ) } 2 } \bigg ) } \\ & { - \bigg ( \frac { \partial \boldsymbol { \sigma } _ { s } ^ { \mathrm { ( 2 ) } } } { \partial t } \bigg ) + \mathbf { D } ^ { \prime } \boldsymbol { \sigma } _ { s } ^ { \mathrm { ( 1 ) } } \bigg ( \frac { \partial \boldsymbol { \sigma } _ { s } ^ { \mathrm { ( 2 ) } } } { \partial t } \bigg ) + \mathbf { D } ^ { \prime } \boldsymbol { \sigma } _ { s } ^ { \mathrm { ( 2 ) } } \bigg \langle \frac { \partial \boldsymbol { \sigma } _ { s } ^ { \mathrm { ( 1 ) } } } { \partial t } \bigg \rangle } \\ & { - \left( \mathbf { D } ^ { \prime } \boldsymbol { \sigma } _ { s } ^ { \mathrm { ( 1 ) } } \right) ^ { 2 } \cdot \bigg ( \frac { \partial \boldsymbol { \sigma } _ { s } ^ { \mathrm { ( 1 ) } } } { \partial t } \bigg ) , } \\ & { . . . . . . . . . } \end{array}
$$

两种变换的目的都是为了简化原方程(7.330),即在一定精度前提下，使变换后的右函数 $f ^ { * }$ 分别为

$$
f ^ { * } { = } \sum _ { k = 0 } ^ { 1 } f _ { k } ^ { * } \left( Y ; \ e ^ { k } \right) + \sum _ { k \geqslant l + 1 } f _ { k } ^ { * } \left( Y , x , t ; \varepsilon ^ { k } \right) .
$$

和

$$
f ^ { * } { = } \sum _ { k = 0 } ^ { l } f _ { k } ^ { * } \left( Y ; ~ \varepsilon ^ { k } \right) + \sum _ { k \geqslant l + 1 } f _ { k } ^ { * } \left( \sigma ^ { \prime } , t ; \varepsilon ^ { k } \right) .
$$

其中

$$
\begin{array} { r } { f _ { \textbf { k } } ^ { * } ( Y ; \varepsilon ^ { h } ) = \left( \begin{array} { l } { ( f _ { \textbf { k } } ^ { * } ) _ { Y } } \\ { ( f _ { \textbf { k } } ^ { * } ) _ { y } \rule { 0 ex } { 5 ex } } \end{array} \right) , } \\ { ( f _ { \textbf { k } } ^ { * } ) _ { y } = \left( \begin{array} { l } { ( f _ { \textbf { k } } ^ { * } ) _ { y _ { 1 } } } \\ { ( f _ { \textbf { k } } ^ { * } ) _ { y _ { 2 } } } \\ { \vdots } \\ { ( f _ { \textbf { k } } ^ { * } ) _ { y _ { n } } \rule { 0 ex } { 5 ex } } \end{array} \right) , } \end{array}
$$

这里(f)表示y方程的右函数，角动量(或矩)Y对应的右函数部分 $( f _ { k } ^ { * } ) _ { \pmb { \chi } }$ 有两种情况，对于保守系统，它是零向量，即

$$
( f _ { k } ^ { * } ) _ { Y } = \left( \begin{array} { l } { { 0 } } \\ { { 0 } } \\ { { \vdots } } \\ { { 0 } } \end{array} \right) , ~ ( k = 0 , 1 , \cdots l ) ,
$$

而对于非保守系统， $( f _ { k } ^ { * } ) _ { \pmb { \gamma } }$ 为非零向量,例如人造地球卫星运动中，考虑球形(指密度分布)静止大气摄动时，对

$$
Y = { \binom { a ^ { \prime } } { e ^ { \prime } } } ,
$$

有

$$
( f _ { k } ^ { * } ) _ { \gamma } = \left( { \begin{array} { c } { ( f _ { k } ^ { * } ) _ { a } , } \\ { ( f _ { k } ^ { * } ) e ^ { \prime } } \\ { 0 } \end{array} } \right) .
$$

因此,对于保守系统，在 $O ( e ^ { \imath } )$ 精度意义下，变换后的方程成为可积形式,其解为

$$
\pmb { Y = Y _ { 0 } } ,
$$

$$
y = y _ { 0 } + \left[ \sum _ { k = 0 } ^ { l } f _ { k } ^ { \ast } \left( Y _ { 0 } ; \varepsilon ^ { k } \right) \right] \left( t - t _ { 0 } \right) .
$$

对于非保守系统,尽管不像保守系统这么简单，但变换后的方程仍达到了简化的目的，周期项已全部分离出，问题显然变得比较简单．两种系统对应的新变量 $\pmb { Y }$ 和 ${ \pmb y } .$ ，其解都只包含长期变化项.那么，对人卫运动的摄动解而言，它们就是第五章和前面几节中提到的平均根数.

上述由(7.358)和(7.359)式表达的 $f ^ { * }$ 如何得到？这就是方法的关键,与Zeipel方法,Hori-Deprit方法完全类似,利用 ${ \pmb { \sigma } } _ { \pmb { \mathscr { S } } } ^ { ( m ) }$ 的待定性，与 $f ^ { * }$ 在 $O ( e ^ { i } )$ 意义下满足所要求形式的同时来确定其具体表达式．事实上这要经过多次变换逐步实现，实为一变换序列(有限项)．那么，在何种条件下可以构成这样的变换序列与前面对正则变换方法的要求相同,即·

（1）原方程的右函数 $\pmb { f }$ （见(7.347)式)不含一阶长周期部分，即

$$
f _ { 1 \imath } = 0 _ { \cdot } ^ { \cdot } \ .
$$

（2）变换过程中不出现由于通约原因引起的小分母。如果出现，例如在 $\pmb { m }$ 阶项中，相应的小分母的特征大小记作 $\mu$ ，其量级应满足不等式

$$
\mu { > } \mathrm { m } a \mathrm { x } \left( e ^ { m / 2 } \varepsilon \right) .
$$

与正则变换方法一样,这里的一般变换亦可采用加速收敛法[8].总之，凡是正则变换方法中所具有的用变换来简化动力系统的“功能”,在非正则形式的变换方法中都可引用．因此,这一变换方法的原理极其简单,如果读者看过前几节,那么对此方法的构思是不难理解的.

# 2．形式解的建立

这里将针对一个具体的动力模型，阐明如何通过上述变换方法达到简化的目的，即给出变换后(7.358)和(7.359)式右端的第一大部分，不失一般性，对人造卫星绕地球的运动，仅考虑地球引力场的主要带谐项 $( J _ { 2 } , J _ { 3 } , J _ { 4 } )$ 和田谐项 $( J _ { 2 } , _ { 2 } )$ 摄动，这是一个6维非自治(即显含 $t )$ 保守系统，此时可记

$$
\scriptstyle \sigma = { \binom { z } { x } } , \quad z = { \binom { a } { e } } , \ x = { \binom { \Omega } { m } } .
$$

按变量的性质， $\pmb { x }$ 分量的次序应该是 $M , \omega , \Omega$ ，其中 $M$ 应与 $\pmb { a }$ 对应；但是,这里并不是引用正则共轭变量，无需考虑这种对应，上面的排列次序是照顾常用的习惯和书写方便。相应的摄动运动方程为

$$
\frac { d \delta \sigma } { d t } = f ( \sigma , t ; \varepsilon ) = f _ { 0 } ( z _ { 1 } ) + f _ { 1 } ( \sigma , \varepsilon ) + f _ { 2 } ( \sigma , t ; \varepsilon ^ { 2 } ) \ ,
$$

其中 $\pmb { \varepsilon } = \pmb { J } _ { 2 }$ ．显然，该系统只有一个快变量，即 ${ \pmb x } _ { 3 } = M$ 当 $\pmb { \varepsilon } = 0$ 时， ${ \pmb x } _ { 3 }$ 对应的角速度(或角频率)记作 $\pmb { \theta = a } ^ { - 8 / 2 }$ ，它仅与 $z _ { 1 } = a$ 有关，且有

$$
f _ { 0 } ( z _ { 1 } ) = \stackrel { \cdot } { \delta \theta } , \stackrel { \cdot } { \delta } = \left( \begin{array} { c } { 0 } \\ { 0 } \\ { \vdots } \\ { 1 } \end{array} \right) ,
$$

$\pmb { \delta }$ 是6维向量，而且只有第六个分量。 $f _ { 1 }$ 和 $f _ { 2 }$ 可分解为

$$
\begin{array} { r l } & { f _ { 1 } = f _ { 1 e } ( z , \varepsilon ) + f _ { 1 s } ( \sigma , \varepsilon ) , } \\ & { f _ { 2 } = f _ { 2 c } ( z , \varepsilon ^ { 2 } ) + f _ { 2 l } ( z , x _ { 2 } ; \varepsilon ^ { 2 } ) + f _ { 2 s } ( \sigma , t ; \varepsilon ^ { 2 } ) } \end{array}
$$

其中 $f _ { 1 l } = 0 .$ ，符合方法要求满足的条件． $f _ { 2 , s }$ 显含 $\pmb { t }$ 的部分仅与$\pmb { J _ { 2 , 2 } }$ 有关， $f _ { 2 l }$ 不显含 $\pmb { t }$ 也不含 $\pmb { x } _ { 1 } = \pmb { \mathscr { Q } }$ ,即使含 $\pmb { \Omega }$ ，对问题的讨论亦无任何影响，只是构造解的过程中，增加一些项而已．关于 $f _ { \mathrm { ~ t ~ } }$ 和$\pmb { f _ { 2 } }$ 及其分解形式，请见第五章 $\ S \ 5 . \ 3$ 和 $\ S 5 . 7$ 中的有关公式.

（1）隐形式变换方法第一次消除快变量 $( x _ { 3 } )$ ，新变量记作 $\pmb { \sigma } ^ { \prime }$ ：

$$
\scriptstyle \sigma ^ { \prime } = { \left( \begin{array} { l } { Y } \\ { y } \\ { } \end{array} \right) } , \ Y = { \left( \begin{array} { l } { a ^ { \prime } } \\ { e ^ { \prime } } \\ { i ^ { \prime } } \end{array} \right) } , y = { \left( \begin{array} { l } { \Omega ^ { \prime } } \\ { \omega ^ { \prime } } \\ { M ^ { \prime } } \end{array} \right) } .
$$

相应的变换(7.331)可写成

$$
\sigma = \sigma ^ { \prime } + \sum _ { m \geqslant 1 } \sigma _ { g } ^ { \scriptscriptstyle ( m ) } ( a ^ { \prime } , e ^ { \prime } , i ^ { \prime } , \mathscr { Q } , \omega , \mathscr { M } , t ; \varepsilon ^ { m } ) .
$$

根据(7.349)-(7.352)式，消除快变量后的右函数 $f _ { k } ^ { * }$ 和短周期项${ \pmb { \sigma } } _ { { \pmb { \vartheta } } } ^ { ( { \pmb { m } } ) }$ 将由下列各式计算：

$$
f _ { 0 } ^ { * } = f _ { 0 } ( Y _ { 1 } ) = \delta \theta ^ { \prime } , \theta ^ { \prime } = a ^ { \prime - 3 / 2 } ,
$$

$$
f _ { 1 } ^ { * } = f _ { 1 \boldsymbol { \sigma } } ( \boldsymbol { Y } , \varepsilon ) , \boldsymbol { \theta } ^ { \prime } \frac { \partial \sigma _ { g } ^ { ( 1 ) } } { \partial x _ { 3 } } = f _ { 1 \boldsymbol { s } } ( \boldsymbol { Y } , \boldsymbol { x } ; \varepsilon ) + \delta \biggl [ \frac { \partial \theta ^ { \prime } } { \partial Y _ { 1 } } Y _ { 1 \delta } ^ { ( 1 ) } \biggr ] ,
$$

$$
f _ { 2 } ^ { * } = [ \Phi _ { 2 } ] _ { c , l } , \theta ^ { \prime } \frac { \partial \sigma _ { \vartheta } ^ { ( 2 ) } } { \partial x _ { 3 } } + \frac { \partial \sigma _ { \vartheta } ^ { ( 2 ) } } { \partial t } = [ \Phi _ { 2 } ] _ { \vartheta } + \delta \biggl [ \frac { \partial \theta ^ { \prime } } { \partial Y _ { 1 } } Y _ { 1 \vartheta } ^ { ( 2 ) } \biggr ] ,
$$

$$
f _ { 3 } ^ { * } = \big [ \Phi _ { 3 } \big ] _ { c , l } , \theta ^ { \prime } \frac { \partial \sigma _ { g } ^ { ( 3 ) } } { \partial x _ { 3 } } + \frac { \partial \sigma _ { g } ^ { ( 3 ) } } { \partial t } = \big [ \Phi _ { 3 } \big ] _ { \vartheta } + \delta \bigg [ \frac { \partial \theta ^ { \prime } } { \partial Y _ { 1 } } Y _ { 1 \vartheta } ^ { ( 3 ) } \bigg ] .
$$

其中

$$
\begin{array} { r l } & { \phi _ { 2 } = f _ { 4 } + \left( \frac { \partial f _ { 1 } } { \partial Y } Y ^ { ( 0 ) } - \frac { \partial \sigma _ { \mathrm { o } } ^ { ( 0 ) } } { \partial x } f _ { 1 } \right) - \frac { 1 } { \theta ^ { 2 } } \frac { \partial \theta ^ { \prime } } { \partial Y } Y ^ { ( 0 ) } f _ { 1 } \tau \partial f _ { 2 } + \delta \left[ \frac { 1 } { 2 } \frac { \partial ^ { 2 } \theta ^ { \prime } } { \partial Y _ { 1 } ^ { 2 } } \right. } \\ & { \left. \quad - \frac { 1 } { \theta ^ { \prime } } \Big ( \frac { \partial \theta ^ { \prime } } { \partial Y _ { 1 } ^ { 2 } } \Big ) ^ { 2 } Y _ { 1 } ^ { ( 0 ) } , \right. } \\ & { \phi _ { 3 } = \Big < \frac { \partial f _ { 2 } } { \partial Y } Y ^ { ( 0 ) } - \frac { \partial \sigma _ { \mathrm { o } } ^ { ( 0 ) } } { \partial x } f _ { 2 } \Big > - \frac { \partial \sigma _ { \mathrm { o } } ^ { ( 0 ) } } { \partial Y } f _ { 3 } ^ { ( 1 ) } + \Big ( \frac { \partial f _ { 1 } } { \partial Y } Y ^ { ( 0 ) } - \frac { \partial \sigma _ { \mathrm { o } } ^ { ( 0 ) } } { \partial z } f _ { 1 } \Big ) } \\ & { + \Big ( \frac { \partial ^ { 2 } \theta ^ { \prime } } { 2 } Y ^ { ( 0 ) } - \frac { \partial \sigma ^ { ( 0 ) } } { \partial z } \partial Y ^ { ( 0 ) } \Big ) Y ^ { ( 0 ) } - \Big < \frac { \partial \theta ^ { \prime } } { \partial Y } Y ^ { ( 0 ) } , \Big < \frac { \partial \theta ^ { \prime } } { \partial z } \Big > \frac { \partial \sigma _ { \mathrm { o } } ^ { ( 0 ) } } { \partial x } \Big < \frac { \partial \theta ^ { \prime } } { \partial Y } Y ^ { ( 0 ) } } \\ &  + \frac { 1 } { 2 } \frac { \partial ^ { 2 } \theta ^ { \prime } } { \partial Y ^ { * } } Y ^ { ( 0 ) } \frac { \partial \sigma _ { \mathrm { o } } ^ { ( 0 ) } } { \partial x } + \delta \Big > \frac { \partial ^ { 2 } \theta ^ { \prime } } { \partial Y } Y ^ { ( 0 ) } { * } \delta ^ { 1 } \sigma _ { \mathrm { o } } ^ { ( 0 ) } + \frac { 3 } { 6 } \frac   \end{array}
$$

关于 $\Phi _ { 2 } ,$ 根据原(7.351)式,有

$$
\mathbf { D } \boldsymbol { \sigma } _ { g } ^ { ( 1 ) } \mathbf { D } Y _ { s } ^ { ( 1 ) } f _ { 0 } - \mathbf { D } \boldsymbol { \sigma } _ { g } ^ { ( 1 ) } f _ { 1 } = \mathbf { D } \boldsymbol { \sigma } _ { g } ^ { ( 1 ) } \bigg ( \boldsymbol { \theta } ^ { \prime } \frac { \partial Y _ { g } ^ { ( 1 ) } } { \partial x _ { 6 } } \bigg ) - \mathbf { D } \boldsymbol { \sigma } _ { s } ^ { ( 1 ) } f _ { 1 }
$$

$$
\begin{array} { l } { { \displaystyle = - { \bf D } \sigma _ { s } ^ { \scriptscriptstyle ( 1 ) } [ f _ { 1 } - ( f _ { 1 s } ) _ { \scriptscriptstyle { \cal T } } ] = - { \bf D } \sigma _ { s } ^ { \scriptscriptstyle ( 1 ) } [ f _ { 1 } - ( f _ { 1 } ) _ { \scriptscriptstyle { \cal T } } + ( f _ { 1 e } ) _ { \scriptscriptstyle { \cal T } } ] } , }  \\ { { \displaystyle = - \frac { \partial \sigma _ { s } ^ { \scriptscriptstyle ( 1 ) } } { \partial x } ( f _ { 1 } ) _ { \scriptscriptstyle { \cal x } } - \frac { \partial \sigma _ { s } ^ { \scriptscriptstyle ( 1 ) } } { \partial Y } ( f _ { 1 o } ) _ { \scriptscriptstyle { \cal T } } , } } \end{array}
$$

$$
\begin{array} { r l } & { - \mathbf { D } \sigma _ { s } ^ { \scriptscriptstyle ( 1 ) } \xrightarrow { \partial f _ { 0 } } Y _ { s } ^ { \scriptscriptstyle ( 1 ) } = - \mathbf { D } \sigma _ { s } ^ { \scriptscriptstyle ( 1 ) } \xrightarrow { \partial f _ { 0 } } Y _ { s } ^ { \scriptscriptstyle ( 1 ) } } \\ & { = - \mathbf { D } \sigma _ { s } ^ { \scriptscriptstyle ( 1 ) } \delta \left( \overline { { \frac { \partial \theta ^ { \prime } } { \partial Y _ { 1 } } } } Y _ { 1 s } ^ { \scriptscriptstyle ( 1 ) } \right) = - \overline { { \frac { \partial \sigma _ { s } ^ { \scriptscriptstyle ( 1 ) } } { \partial x _ { 6 } } } } \left( \overline { { \frac { \partial \theta ^ { \prime } } { \partial Y _ { 1 } } } } Y _ { 1 s } ^ { \scriptscriptstyle ( 1 ) } \right) } \\ & { = - \frac { 1 } { \tilde { \theta } ^ { \scriptscriptstyle ( r ) } \tilde { \partial } Y _ { 1 } ^ { \scriptscriptstyle ( 1 ) } } \Big [ f _ { 1 s } - \left( \overline { { \frac { \partial \sigma _ { s } ^ { \scriptscriptstyle ( 1 ) } } { \partial t } } } \right) + \delta \left( \overline { { \frac { \partial \theta ^ { \prime } } { \partial Y _ { 1 } } } } Y _ { 1 s } ^ { \scriptscriptstyle ( 1 ) } \right) \Big ] , } \end{array}
$$

其中 $( f _ { 1 } ) _ { x }$ 写成 $f _ { 1 }$ 无妨，因按前面提出的书写规则， $\frac { \partial \sigma _ { \scriptscriptstyle B } ^ { \scriptscriptstyle ( 1 ) } } { \partial x } f _ { 1 }$ 与 $\frac { \partial \sigma _ { \mathscr { g } } ^ { ( 1 ) } } { \partial \boldsymbol { x } }$ (fi)相同，它们的表达式中 $\frac { \partial \sigma _ { g } ^ { \scriptscriptstyle ( 1 ) } } { \partial Y }$ 是以零元素代替的，另外，针对这里所讨论的动力系统，有

$$
( f _ { 1 \mathscr { c } } ) _ { \mathscr { r } } { = } 0 , \qquad \Big ( \frac { \partial \sigma _ { \mathscr { s } } ^ { ( 1 ) } } { \partial \mathscr { t } } \Big ) { = } 0 .
$$

故 $\varPhi _ { 2 }$ 最后被简化成(7.377)式的形式，在给出 $\Phi _ { 3 }$ 的过程中，亦有类似的简化,不再一一列出。

如果只要取到 $O ( \varepsilon ^ { 3 } )$ 项，则 $f _ { 3 } ^ { * }$ 中的 $\pmb { x }$ 可直接用 $\pmb { y }$ 替换，而 $f _ { 2 } ^ { * }$ 中的 $\pmb { \mathcal { X } }$ 换为 $\pmb { y }$ 时，将引进一项：

$$
\left( \frac { \partial f _ { 2 } ^ { * } } { \partial x } \right) _ { x = y } \cdot y _ { s } ^ { ( 1 ) } = \frac { \partial f _ { 2 } ^ { * } } { \partial y } y _ { s } ^ { ( 1 ) } ,
$$

该项将并人 $\Phi _ { 3 }$ 中，于是,消除快变量 $\pmb { x _ { 8 } }$ （即新变量的 $y _ { 3 }$ 后，新变量方程 $d \sigma ^ { \prime } / d t$ 的右函数 $f ^ { * }$ 变为

$$
\begin{array} { r l } & { f ^ { * } ( \sigma ^ { \prime } , \iota _ { \iota ^ { \prime } } ) = f _ { 0 } ^ { * } \left( Y _ { 1 } \right) + f _ { 1 } ( Y , e ) + f _ { 2 } ^ { * } \left( Y , y _ { 2 } ; \varepsilon ^ { 2 } \right) } \\ & { \qquad + f _ { 3 } ^ { * } \left( Y , y _ { 2 } ; \varepsilon ^ { 3 } \right) + \cdots . } \end{array}
$$

由于原 $f _ { 2 }$ 中显含 $\pmb { \mathrm { \acute { \varepsilon } } }$ 并同时含 $\pmb { \Omega }$ 的部分 $f _ { 2 { \theta } }$ 项 $( { J } _ { 2 , 2 }$ 的贡献),以及由此形成的部分短周期项 ${ \pmb { \sigma } } ^ { ( 2 ) } ,$ 与 ${ { J } _ { 2 } }$ 项的性质不同，它们的联合作用不会使 $f _ { 3 } ^ { * }$ 中出现显含 $\pmb { t }$ 或同时含 $\theta _ { 1 } = \Omega ^ { \prime }$ 的项.

第二次消除慢变量 $( y _ { 2 } )$ ，新变量记作 $\sigma ^ { \prime \prime }$ ：

$$
\scriptstyle \sigma ^ { \prime \prime } = { \binom { Z } { z } } , \quad \mathbf { Z } = { \binom { \alpha ^ { \prime \prime } } { e ^ { \prime \prime } } } , \ : \ z = { \binom { \alpha ^ { \prime \prime } } { \alpha ^ { \prime \prime } } } ,
$$

相应的变换(7.331)可写成

$$
\sigma ^ { \prime } { = } \sigma ^ { \prime \prime } { + } \displaystyle \sum _ { m , \ne 1 } \sigma _ { ~ \iota } ^ { \ast m } ( a ^ { \prime \prime } , e ^ { \prime \prime } , i ^ { \prime \prime } , \omega ^ { \prime } ; \varepsilon ^ { m } ) .
$$

与上类似，消除慢变量后的右函数 $f _ { k } ^ { * * }$ 和长周期项 $\sigma _ { i } ^ { ( \pmb { \mathscr { m } } ) }$ 将由下列各式计算：

$$
f _ { 0 } ^ { * * } = f _ { 0 } ^ { * } ( Z _ { 1 } ) = \delta \theta ^ { \prime \prime } , \theta ^ { \prime \prime } { = } a ^ { \prime \prime - 3 / 2 } ,
$$

$$
f _ { \mathrm { \ell } } ^ { \ast \ast } = f _ { \mathrm { 2 } } ^ { \ast } ( Z , e ^ { 2 } ) , ( f _ { \mathrm { \ell } } ^ { \ast } ) _ { \nu _ { \mathrm { 2 } } } \frac { \partial \sigma _ { \mathrm { \ell } } ^ { ( 1 ) } } { \partial y _ { \mathrm { 2 } } } { = } f _ { \mathrm { 2 } \mathrm { \ell } } ^ { \ast } + \frac { \partial f _ { \mathrm { 1 } } ^ { \ast } } { \partial Z } \mathrm { Z } _ { \mathrm { \ell } } ^ { \mathrm { \scriptscriptstyle ( 1 ) } } + \delta \biggl [ \frac { \partial \theta ^ { \prime \prime } } { \partial Z _ { \mathrm { 1 } } } \mathrm { Z } _ { \mathrm { \ell } \mathrm { \ell } } ^ { \mathrm { \scriptscriptstyle ( 2 ) } } \biggr ] ,
$$

$$
\begin{array} { r l r } { f _ { 3 } ^ { * * } = \displaystyle [ \Phi _ { 3 } ^ { * } ] _ { c } , } & { } & { ( f _ { 1 } ^ { * } ) _ { y _ { 2 } } \frac { \partial \sigma _ { l } ^ { ( 2 ) } } { \partial y _ { 2 } } = \lbrack \Phi _ { 3 } ^ { * } ] _ { l } + \left. \frac { \partial f _ { 1 } ^ { * } } { \partial Z } Z _ { l } ^ { ( 2 ) } \right. } \\ & { } & { \displaystyle + \delta \Bigl [ \frac { \partial \theta ^ { \prime \prime } } { \partial Z _ { 1 } } Z _ { 1 } ^ { ( 3 ) } \Bigr ] } \end{array}
$$

其中

$$
\hat { \psi } _ { 3 } ^ { * } = f _ { 3 } ^ { * } + \bigg ( \frac { \partial f _ { 2 } ^ { * } } { \partial Z } Z _ { l } ^ { ( 1 ) } - \frac { \partial \sigma _ { l } ^ { ( 1 ) } } { \hat { c } \mathcal { Y } } f _ { 2 } ^ { * } \bigg ) + \bigg ( \frac { 1 \ \partial ^ { 2 } f _ { 1 } ^ { * } } { 2 \ \partial Z ^ { 2 } } Z _ { l } ^ { ( 1 ) } - \frac { \partial \sigma _ { l } ^ { ( 1 ) } } { \partial y } \frac { \partial f _ { 1 } ^ { * } } { \partial Z } \bigg ) Z _ { l } ^ { ( 1 ) } .
$$

$( f _ { 1 } ^ { \ast } ) _ { y _ { 2 } }$ 表示变量 ${ \pmb y } _ { \mathbf { 2 } }$ 对应的右函数，而这里 $f _ { 1 } ^ { * } { = } f _ { 1 } ^ { * } ( Z , \varepsilon ) { = } f _ { 1 } ^ { * * }$ ，即$z _ { 2 } = \omega ^ { \prime \prime }$ 对应的右函数，亦即 $\pmb { \omega }$ 的一阶长期项系数.

从上述过程可以看出，即使 $f ^ { * }$ 中含另一慢变量 $y _ { 1 } = \Omega ^ { \prime }$ 或同时显含 $\pmb { \ t }$ ，都无关紧要，仅仅使确定 $\sigma _ { \iota } ^ { ( m ) }$ 时，由（7.384）和（7.385)式的简单形式变成多变元的一阶线性偏微分方程，其右端项皆为$\ y _ { 1 } , \ y _ { 2 }$ 和 $\pmb { \ell }$ 的三角函数，故与前面给出的显含 $\pmb { \mathrm { \acute { \varepsilon } } }$ 的Zeipel变换方法一样，容易确定长周期项 $\sigma _ { \textit { l } } ^ { ( m ) }$ ，

经第二次变换,新变量 $\sigma ^ { \prime \prime }$ 的变化满足下列方程：

$$
\begin{array} { l } { \displaystyle \frac { d \sigma ^ { \prime \prime } } { d t } { = } f ^ { * * } ( \sigma ^ { \prime \prime } , \varepsilon ) } \\ { \displaystyle { = } f _ { 0 } ^ { * * } ( { \bf Z } _ { 1 } ) + f _ { 1 } ^ { * * } ( { \bf Z } , \varepsilon ) + f _ { 2 } ^ { * * } ( { \bf Z } , e ^ { 2 } ) } \\ { \displaystyle { \quad + } f _ { 3 } ^ { * * } ( { \bf Z } , \varepsilon ) + \cdots . } \end{array}
$$

而讨论的问题是保守系统，相应地有

$$
( f _ { k } ^ { * * } ) _ { z } = { \binom { 0 } { 0 } } , k = 0 , 1 , 2 , 3 .
$$

于是在 $O ( \varepsilon ^ { 3 } )$ 意义下,上述系统可积,结果为

$$
\left. \begin{array} { l } { \displaystyle \mathbf { Z } = Z _ { 0 } , } \\ { \displaystyle z = z _ { 0 } + \left[ \sum _ { k = 0 } ^ { 3 } f _ { k } ^ { * * } \left( Z _ { 0 } , \varepsilon ^ { k } \right) \right] ( t - t _ { 0 } ) . } \end{array} \right\}
$$

原变量 $\pmb { \sigma }$ 的解则通过两次变换关系得到，即

$$
\pmb { \sigma } = \pmb { \sigma } ^ { \prime \prime } + \pmb { \sigma } _ { i } ^ { ( 1 ) } + \pmb { \sigma } _ { i } ^ { ( 2 ) } + \cdots + \pmb { \sigma } _ { g } ^ { ( 1 ) } + \pmb { \sigma } _ { g } ^ { ( 2 ) } + \cdots
$$

其中有变量转换问题，即α{m）中的y要转换成z，）中的x${ \pmb x } _ { 2 } , { \pmb x } _ { 3 }$ 要转换成 $y _ { 1 } , y _ { 2 } , y _ { 3 } ,$ 其转换规则与前面Zeipel方法中的处理相同，都是隐形式变换引起的问题。

# （2）显形式变换方法

第一次消除快变量 $( y _ { 3 } )$ ，变换关系为

$$
\pmb { \sigma } = \pmb { \sigma } ^ { \prime } + \sum _ { m \geq 1 } \pmb { \sigma } _ { g } ^ { ( m ) } \left( \sigma ^ { \prime } , t ; \varepsilon ^ { m } \right) .
$$

根据(7.354)—(7.357)式,相应地有

$$
f _ { 0 } ^ { * } = f _ { 0 } ( Y _ { 1 } ) = \delta \theta ^ { \prime } , \theta ^ { \prime } = a ^ { \prime - 3 / 2 }
$$

$$
f _ { 1 } ^ { * } = f _ { 1 } ( Y , e ) , \theta ^ { \prime } . \frac { \partial \sigma _ { \mathcal { S } } ^ { ( 1 ) } } { \partial y _ { 3 } } = f _ { 1 \mathcal { S } } ( \sigma ^ { \prime } e ) + \delta \left[ \frac { \partial \theta ^ { \prime } } { \partial Y _ { 1 } } Y _ { 1 \mathcal { S } } ^ { ( 1 ) } \right] ,
$$

$$
f _ { 2 } ^ { \ast } = [ \psi _ { 2 } ] _ { \circ \ast } \textit { \textbf { \theta } } ^ { \prime } \frac { { \partial } \sigma _ { s } ^ { ( 2 ) } } { { \partial } y _ { 3 } } + \frac { { \partial } \sigma _ { s } ^ { ( 2 ) } } { { \partial } t } = [ \psi _ { 2 } ] _ { \mathscr { S } } + \delta \frac { [ 2 \theta ^ { \prime } } { \partial { \cal Y } _ { 1 } } Y _ { 1 \mathscr { S } } ^ { ( 2 ) } \Bigg ] \mathrm { , }
$$

$$
f _ { 3 } ^ { * } = [ \psi _ { 3 } ] _ { \sigma \nu \ell } \quad \theta ^ { \prime } \frac { \partial \sigma _ { g } ^ { ( 2 ) } } { \partial y _ { 3 } } + \frac { \partial \sigma _ { g } ^ { ( 3 ) } } { \partial \ell } { = } [ \psi _ { 3 } ] _ { \mathcal { S } } + \delta \bigg [ \frac { \partial \theta ^ { \prime } } { \partial Y _ { 1 } } Y _ { 1 \mathcal { S } } ^ { ( 3 ) } \bigg ] ,
$$

其中

$$
\psi _ { 2 } = f _ { 2 } + \bigg ( \frac { \partial f _ { 1 } } { \partial \sigma ^ { \prime } } \sigma _ { \it 8 } ^ { ( 1 ) } - \frac { \partial \sigma _ { \it 8 } ^ { ( 1 ) } } { \partial y } f _ { 1 0 } \bigg ) + \delta \bigg [ \frac { 1 } { 2 } \frac { \partial ^ { 2 } \theta ^ { \prime } } { \partial Y _ { 1 } ^ { 2 } } Y _ { 1 \it 8 } ^ { ( 1 ) 2 } \bigg ] ,
$$

$$
\boldsymbol { \psi } _ { 3 } = \left( \frac { \partial f _ { 2 } } { \partial \sigma ^ { \prime } } \sigma _ { s } ^ { \scriptscriptstyle ( 1 ) } - \frac { \partial \sigma _ { s } ^ { \scriptscriptstyle ( 1 ) } } { \partial \sigma ^ { \prime } } f _ { 2 } ^ { * } \right) + \left( \frac { \partial f _ { 1 } } { \partial \sigma ^ { \prime } } \sigma _ { s } ^ { \scriptscriptstyle ( 2 ) } - \frac { \partial \sigma _ { s } ^ { \scriptscriptstyle ( 2 ) } } { \partial y } f _ { 1 e } \right) + \frac { 1 } { 2 ~ \partial \sigma ^ { \scriptscriptstyle ( 1 ) 2 } } \sigma _ { s } ^ { \scriptscriptstyle ( 1 ) 2 }
$$

$$
+ \delta \biggl [ \frac { \partial ^ { 2 } \theta ^ { \prime } } { \partial Y _ { 1 } ^ { 2 } } Y _ { 1 \vartheta } ^ { ( 1 ) } Y _ { 1 \vartheta } ^ { ( 2 ) } + \frac { 1 \partial ^ { 3 } \theta ^ { \prime } } { 6 \partial Y _ { 1 } ^ { 3 } } Y _ { 1 \vartheta } ^ { ( 3 ) } \biggr ] + \frac { \partial \sigma _ { \vartheta } ^ { ( 1 ) } } { \partial \sigma ^ { \prime } } \biggl ( \frac { \partial \sigma _ { \vartheta } ^ { ( 1 ) } } { \partial t } \biggr ) .
$$

第二次消除慢变量 $( z _ { 2 } )$ ，变换关系为

$$
{ \sigma } ^ { \prime } { = } { \sigma } ^ { \prime \prime } { + } \ \sum _ { m > 1 } { \sigma } _ { l } ^ { ( m ) } \left( a ^ { \prime \prime } , e ^ { \prime \prime } , i ^ { \prime \prime } , { \omega } ^ { \prime \prime } ; e ^ { m } \right) ,
$$

有

$$
\begin{array} { l } { { f _ { 0 } ^ { * } { } ^ { * } = f _ { 0 } ^ { * } ( Z _ { 1 } ) = \delta \theta ^ { \prime \prime } , \theta ^ { \prime \prime } { } = a ^ { \prime \prime - 3 / 2 } } } \\ { { { } } } \\ { { f _ { 1 } ^ { * } { } ^ { * } = f _ { 1 } ^ { * } ( Z , e ) , } } \end{array}
$$

$$
\begin{array} { l } { { f _ { 2 } ^ { * * } = f _ { 2 c } ^ { * } \left( \mathrm { Z } , e ^ { 2 } \right) , \qquad \left( f _ { 1 } ^ { * } \right) _ { z _ { 1 } } \frac { \partial \sigma _ { \iota } ^ { ( 1 ) } } { \partial z _ { 2 } } = f _ { 2 \iota } ^ { * } + \frac { \partial f _ { 1 } ^ { * } } { \partial \mathrm { Z } } \mathrm { Z } _ { \iota } ^ { ( 1 ) } } } \\ { { \qquad + \delta \biggl [ \frac { \partial \theta ^ { \prime \prime } } { \partial \mathrm { Z } _ { 1 } } \mathrm { Z } _ { 1 \iota } ^ { ( 2 ) } \biggr ] , } } \end{array}
$$

$$
\begin{array} { r l r } { f _ { 3 } ^ { * * } = [ \mathcal { V } ^ { * } ] _ { \boldsymbol { \sigma } } , } & { } & { ( f _ { 1 } ^ { * } ) _ { \boldsymbol { z } _ { 2 } } \cfrac { \partial \sigma _ { \iota } ^ { ( 2 ) } } { \partial z _ { 2 } } = [ \mathcal { V } _ { 3 } ^ { * } ] _ { \boldsymbol { l } } + \cfrac { \partial f _ { 1 } ^ { * } } { \partial \boldsymbol { Z } } Z _ { \boldsymbol { l } } ^ { \circledast } } \\ & { } & { \qquad + \delta \Big [ \cfrac { \partial \theta ^ { \prime \prime } } { \partial Z _ { 1 } } Z _ { 1 \boldsymbol { l } } ^ { \ c ( 3 ) } \Big ] , } \end{array}
$$

其中

$$
{ \boldsymbol { \psi } } _ { 3 } = f _ { 3 } ^ { * } + \left( \frac { \partial f _ { 2 } ^ { * } } { \partial \sigma ^ { \prime \prime } } \sigma _ { l } ^ { ( 1 ) } - \frac { \partial \sigma _ { l } ^ { ( 1 ) } } { \partial z } f _ { 2 e } ^ { * } \right) + \frac { 1 } { 2 } \frac { \partial ^ { 2 } f _ { 1 } ^ { * } } { \partial Z ^ { 2 } } Z _ { l } ^ { ( 1 ) ^ { 2 } } .
$$

两次变换后的右函数与隐形式的变换结果类似，在一定精度意义下，仅是 $\mathbf { z }$ 的函数，但整个过程没有换变量问题.

根据上面给出形式解的过程，不难看出，尽管显形式变换清楚，表达也显得简单，但从实用角度来看，与前几节的正则变换方法情况类似，还是隐形式变换方法涉及的运算项数少些，愈到高阶愈明显．因此，在具体应用中，常采用隐形式变换方法，特别是一阶解，无变量转换问题．上述方法,变换的特点是明显的，变换中消除快、慢变量即分离出“短周期"项 $\pmb { \sigma } _ { \textbf { \mathcal { B } } } ^ { ( m ) }$ 和“长周期”项 $\pmb { \sigma } _ { \mathrm { ~ } _ { l } } ^ { ( m ) }$ ，由于确定它们的方法不同于平均根数法，因此， $\sigma _ { \beta } ^ { ( m ) }$ 中包含长周期项（即 $\overline { { \sigma _ { \vartheta } ^ { ( m ) } } } \neq 0 )$ 并不奇怪;而且为了需要,还可以在确定 $\sigma _ { \mathcal { S } } ^ { ( m ) }$ 中增加一些与快变量 ${ \pmb x } _ { 3 } = { \pmb M }$ 无关的项.也正因为确定 ${ \pmb { \sigma } } _ { g } ^ { ( m ) }$ 时，是通过偏导数关系(或线性偏微分方程)获得的，因此，与正则变换方法确定生成函数的情况一样，不存在平均根数法中通过对 $\pmb { \mathrm { \acute { t } } }$ 积分求短周期项遇到的那种麻烦。从数学角度来看，显然比平均根数法清楚，也可以看成是平均根数法进一步“数学化”的结果。

# 3. $\pmb { J _ { 2 } }$ 项一阶摄动解的具体结果

对于 $\pmb { J _ { 2 } }$ 项，原方程为

$$
\left. \begin{array} { l } { \displaystyle \frac { d \sigma } { d t } = f _ { 0 } + f _ { 1 } , } \\ { f _ { 0 } = f _ { 0 } ( a ) = a ^ { - 3 / 2 } , } \\ { f _ { 1 } = f _ { 1 \sigma } ( a , e , i ) + f _ { 1 \delta } ( a , e , i , \omega , M ) } \end{array} \right\}
$$

其中 $f _ { 1 }$ 包含小参数 $\pmb { \varepsilon } = \pmb { J _ { 2 3 } }$ 这里省略.

用隐形式变换,第一次消除 $M$ (分离出短周期项)的变换为

$$
\sigma = \sigma ^ { \prime } + \sigma _ { s } ^ { \scriptscriptstyle ( 1 ) } ( a ^ { \prime } , e ^ { \prime } , i ^ { \prime } , \omega , M ) ,
$$

$$
\frac { d \sigma ^ { \prime } } { d t } { = } f _ { 0 } ^ { * } \left( a ^ { \prime } \right) { + } f _ { 1 } ^ { * } \left( a ^ { \prime } , e ^ { \prime } , i ^ { \prime } \right) { + } f _ { 2 } ^ { * } \left( a ^ { \prime } , e ^ { \prime } , i ^ { \prime } \omega \right) .
$$

由形式解(7.373)—(7.377)可知:

$$
\begin{array} { r l r } { \ } & { } & { I _ { 0 } = \pi : = \alpha ^ { ( 2 ) } \ w , } \\ { \ } & { } & { ( \bar { z } , \cdot , \bar { z } ^ { ( 4 ) } ) } \\ { \ } & { } & { f _ { 1 } ^ { \ast } =  \frac { \partial } { \partial z }  _ { 0 , 1 } = f _ { 2 , 0 } ^ { \ast } ( a ^ { ( 4 ) } , e ^ { t } , i ^ { t } ) + \int _ { \bar { z } _ { 1 } } ^ { \bar { z } _ { 1 } } ( a ^ { \prime } , e ^ { t } , i ^ { t } ) e ^ { ( 2 ) } , \quad ( \bar { z } , \cdot , \bar { z } ^ { ( 4 ) } ) } \\ { \ } & { } & { ( \sigma _ { 0 } ^ { ( 4 ) } - \frac { 1 } { \pi ^ { 2 } } ) ^ { \ast }   1 \kappa ( a ^ { \prime } , e ^ { t } , i ^ { t } \omega , j , M ^ { \prime } ) \ } \\ { \ } & { } & { ( \bar { z } , \cdot , \bar { z } ^ { ( 4 ) } ) } \\ { \ } & { } & {   \phi ( - \frac { 3 } { 2 } \alpha ^ { ( 4 ) } , + \frac { 3 } { 2 \pi ^ { 4 } } , a \frac {   } {  \sqrt { 2 } } )  d ^ { ( 4 ) / 2 } , \quad  } \\ { \ } & { } & {  \phi _ { 2 } = ( \frac { \partial f _ { 1 } } { \partial a ^ { \prime } } + \frac { 3 } { 2 \pi ^ { 4 } } f _ { 1 } \omega ) a _ { 0 } ^ { ( 5 ) } + \frac { 3 } { 2 \pi ^ { 6 } } \alpha _ { 0 } ^ { ( 4 ) } + \frac { 3 f _ { 1 } } { \partial \bar { z } ^ { ( 4 ) } } \frac { ( \bar { z } , \cdot , \bar { z } ) } { \partial \bar { z } ^ { ( 4 ) } } - \frac { \partial \bar { z } _ { 0 } ^ { ( 5 ) } } { \partial \omega ^ { \prime } } ( f _ { 1 } ) , } \\ { - \frac { 3 } { 2 \pi ^ { 6 } } ( f _ { 1 } ) _ { \mathcal { W } ^ { \prime } } + \delta [ - \frac { 3 } { 8 } a ^ { 2 - 7 \pi } * \alpha _ { 0 } ^ { ( 6 ) } ] . } \end{array}
$$

上述各式右端的 $\pmb { \omega }$ 和 $\pmb { M }$ 已直接换为 $\omega ^ { \prime }$ 和 $M ^ { \prime }$ ，对于一阶解这是允许的,下面也有类似情况．第二次消除 $\omega ^ { \prime }$ (分离长周期项）的变换为

$$
\sigma ^ { \prime } = \sigma ^ { \prime \prime } { + } \sigma _ { \iota } ^ { \scriptscriptstyle ( 1 ) } ( a ^ { \scriptscriptstyle { \it i \prime } } , e ^ { \prime \prime } , i ^ { \prime \prime } , \omega ^ { \prime } ) ,
$$

$$
\frac { d \sigma ^ { \prime \prime } } { d t } = \acute { \iota } _ { 0 } ^ { \ast \ast } ( a ^ { \prime \prime } ) + f _ { \mathrm { \iota } } ^ { \ast \ast } ( a ^ { \prime \prime } , e ^ { \prime \prime } , i ^ { \prime \prime } ) + f _ { 2 } ^ { \ast \ast } ( a ^ { \prime \prime } , e ^ { \prime \prime } , i ^ { \prime \prime } ) .
$$

由形式解(7.382)—(7.384)可知:

$$
\begin{array} { r l } & { f _ { 0 } ^ { * * } = n ^ { \prime \prime } { = } a ^ { \prime \prime - 3 / 2 } , } \\ & { f _ { 1 } ^ { * * } { = } f _ { 1 } ^ { * } \left( a ^ { \prime \prime } , e ^ { \prime \prime } , i ^ { \prime \prime } \right) { = } f _ { 1 c } ( a ^ { \prime \prime } , e ^ { \prime \prime } , i ^ { \prime \prime } ) , } \\ & { f _ { 1 } ^ { * * } { = } f _ { 2 c } ^ { * } \left( a ^ { \prime \prime } , e ^ { \prime \prime } , i ^ { \prime \prime } \right) , } \end{array}
$$

$$
\begin{array} { l } { { \displaystyle \sigma _ { \iota } ^ { \scriptscriptstyle ( 1 ) } = \frac { 1 } { \left( f _ { 1 } ^ { * } \right) _ { \varrho ^ { \prime \prime } } } \Biggl \{ ^ { \sigma ^ { \prime \prime } } [ f _ { 2 \iota } ^ { * } \left( a ^ { \prime \prime } , e ^ { \prime \prime } , i ^ { \prime \prime } , \omega ^ { \prime \prime } \right) + \left( \frac { \partial f _ { 1 } ^ { * } } { \partial e ^ { \prime \prime } } e _ { \iota } ^ { \scriptscriptstyle ( 1 ) } + \frac { \partial f _ { 1 } ^ { * } } { \partial i ^ { \prime \prime } } i _ { \iota } ^ { \scriptscriptstyle ( 1 ) } \right) } } \\ { { \displaystyle + \delta \biggl ( - \frac { 3 } { 2 } a ^ { \prime \prime - 5 / 2 } \cdot a _ { \iota } ^ { \scriptscriptstyle ( 2 ) } \biggr ] d \omega ^ { \prime \prime } \qquad } } & { { \left( 7 . 4 1 6 \right) } } \end{array}
$$

两次变换后有

$$
\left. \begin{array} { l } { { \left( f _ { 1 } ^ { * * } + f _ { 2 } ^ { * * } \right) _ { a } , , = 0 , a _ { 1 } ^ { \prime \prime } = a _ { 0 } ^ { \prime \prime } , } } \\ { { \left( f _ { 1 } ^ { * * } + f _ { 2 } ^ { * * } \right) _ { e ^ { \prime \prime } } = 0 , e ^ { \prime \prime } = e _ { 0 } ^ { \prime \prime } , } } \\ { { \left( f _ { 1 } ^ { * * } + f _ { 2 } ^ { * * } \right) _ { i } , = 0 , i ^ { \prime \prime } = i _ { 0 } ^ { \prime \prime } . } } \end{array} \right\}
$$

于是

$$
\left. \begin{array} { l } { { \Omega ^ { \prime \prime } = \Omega _ { 0 } ^ { \prime \prime } \mathrm { ~ . ~ . ~ } ( f _ { 1 } ^ { \ast \ast } ( a _ { 0 } ^ { \prime \prime } \mathrm { ~ , ~ } e _ { 0 } ^ { \prime \prime } \mathrm { ~ , ~ } i _ { 0 } ^ { \prime \prime } ) } } \\ { { + f _ { 2 } ^ { \ast \ast } ( a _ { 0 } ^ { \prime \prime } \mathrm { ~ , ~ } e _ { 0 } ^ { \prime \prime } \mathrm { ~ , ~ } i _ { 0 } ^ { \prime \prime } ) ) _ { a } \mathrm { , ~ . ~ } ( t - t _ { 0 } ) , } } \\ { { \omega ^ { \prime \prime } = \omega _ { 0 } ^ { \prime \prime } \mathrm { ~ . ~ } ( f _ { 1 } ^ { \ast \ast } ( a _ { 0 } ^ { \prime \prime } \mathrm { ~ , ~ } e _ { 0 } ^ { \prime \prime } \mathrm { ~ , ~ } i _ { 0 } ^ { \prime \prime } ) } } \\ { { + f _ { 2 } ^ { \ast \ast } ( a _ { 0 } ^ { \prime \prime } \mathrm { , ~ } e _ { 0 } ^ { \prime \prime } \mathrm { , ~ } i _ { 0 } ^ { \prime \prime } ) ) _ { a ^ { \prime \prime } } ( t - t _ { 0 } ) , } } \\ { { M ^ { \prime \prime } = M _ { 0 } ^ { \prime \prime } + [ n _ { 0 } ^ { \prime \prime } \mathrm { ~ . ~ } ( f _ { 1 } ^ { \ast \ast } ( a _ { 0 } ^ { \prime \prime } \mathrm { , ~ } e _ { 0 } ^ { \prime \prime } \mathrm { , ~ } i _ { 0 } ^ { \prime \prime } ) } } \\ { { + f _ { 2 } ^ { \ast \ast } ( a _ { 0 } ^ { \prime \prime } \mathrm { , ~ } e _ { 0 } ^ { \prime \prime } \mathrm { , ~ } i _ { 0 } ^ { \prime \prime } ) ) _ { M ^ { \prime \prime } } ] ( t - t _ { 0 } ) . } } \end{array} \right\}
$$

$\sigma ^ { \prime \prime }$ 就是平均根数， $a , ~ e$ 和 $\pmb { i }$ 的变化无长期项，而(7.418)式右端$( t - t _ { 0 } )$ 的系数即长期项系数，亦即第五章用平均根数法给出的 $\sigma _ { 1 }$ 和 $\pmb { \sigma _ { 2 } } _ { } \mathrm { . }$ 见(5.117)式和(5.118)式，这里不再重复写出．原变量的解为

$$
\left. \begin{array} { l } { { \pmb { \sigma } = \pmb { \sigma } ^ { \prime } + \pmb { \sigma } _ { s } ^ { ( 1 ) } ( \pmb { \sigma } ^ { \prime } ) } } \\ { { \pmb { \sigma } ^ { \prime } = \pmb { \sigma } ^ { \prime \prime } + \pmb { \sigma } _ { l } ^ { ( 1 ) } ( \pmb { \sigma } ^ { \prime \prime } ) . } } \end{array} \right\}
$$

其中 ${ \pmb { \sigma } } _ { \pmb { \mathscr { s } } } ^ { ( 1 ) }$ 和 $\pmb { \sigma } _ { l } ^ { ( 1 ) }$ 的具体形式与第五章的结果一致，见(5.119)一(5.130)式．但有一项移动了“位置”，即由(7.409)式给出的 ${ \boldsymbol \omega } _ { \mathcal { B } } ^ { ( 1 ) * }$ 和 $M _ { s } ^ { ( 1 ) }$ 中分别“增加”一项：

$$
- \frac { 9 J _ { 2 } } { 1 6 p ^ { 2 } } \sin ^ { 2 } i \sin 2 \omega , \frac { 9 J _ { 2 } } { 1 6 p _ { 2 } } \sqrt { 1 - e ^ { 2 } } \sin ^ { 2 } i \sin 2 \omega ,
$$

$\pmb { p } { = } a \left( \mathbf { 1 } { - } e ^ { \mathbf { 2 } } \right)$ ；而由(7.416)式给出的 $\omega _ { l } ^ { ( 1 ) }$ 中却相应地减少了这一项,具体结果整理在文[21]中.

由于计算 $f _ { 2 } ^ { * } , f _ { 3 } ^ { * }$ …时，采用的是 $\frac { \partial \sigma _ { s } ^ { \scriptscriptstyle ( 1 ) } } { \partial \dot { \omega } } ( f _ { 1 } ) _ { \omega } ,$ ， $\frac { \partial \sigma _ { \mathscr { S } } ^ { ( 1 ) } } { \partial M } ( \boldsymbol { f } _ { 1 } ) _ { M } , \cdots ,$ 而不是 $\frac { \partial f _ { 1 } } { \partial \omega } \omega _ { s } ^ { ( 1 ) } , \frac { \partial f _ { 1 } } { \partial \overline { { { \mathcal { M } } } } } \widetilde { M } _ { s } ^ { ( 1 ) } , \cdots ,$ 就避免了平均根数法和正则变换法在·推导时出现

$$
{ \left( { \frac { a } { r } } \right) } ^ { k } \left( f - M \right) { \binom { \cos m f } { \sin m f } } , \left( k , m = 0 , 1 , \cdots \right)
$$

这类项在积分时遇到的麻烦，使推导过程明显地简化，同时便于在计算机上推导对 $e$ 的封闭型解，这也是一般变换方法(隐形式)的-个优点。当然,与平均根数法一样,如不借助能量积分，就仍然存在推导 $M _ { \ : \ell } ^ { ( 1 ) }$ 要用到 ${ \pmb a } _ { l } ^ { ( 2 ) }$ 的麻烦，只有像正则变换方法那样采用正则共轭变量 $( L , G , H , l , g , \hbar )$ 才可避免这一问题．总之,若采用椭圆根数作为基本变量来构造摄动解，那么，还是引用本节给出的一般变换方法(特别是隐形式)为宜，原理清楚，推导也相应地简单些.

# 4.关于引用隐形式变换方法构造其它摄动解的一点说明

在人卫工作中，采用分析方法构造摄动解，进行轨道分析或给出一定精度的有摄星历表,往往限于一阶解。在此情况下,其它各：摄动因素又可看成二阶小量，即 $O ( J _ { 2 } ^ { 2 } )$ ，那么同时考虑各摄动因素时，仅方程(7.403)的右函数增加一个二阶部分：

$$
f _ { 2 } = f _ { 2 c } + f _ { 2 l } + f _ { 2 S } .
$$

对于一阶摄动解， $f _ { 2 , s }$ 通常可略去，只有 $\mathbf { J _ { 2 , 2 } }$ 中的一些特殊项要保留．于是问题变得很简单，仅使两次变换分别增加相应的一些项而已．第一次变换增加

$$
\begin{array} { r l } & { \Delta f _ { 2 } ^ { * } = f _ { 2 c } ( \alpha ^ { \prime } , e ^ { \prime } , i ^ { \prime } ) + f _ { 2 l } ( \alpha ^ { \prime } , e ^ { \prime } , i ^ { \prime } , \Omega ^ { \prime } , \omega ^ { \prime } , t ) \cdot } \\ & { \qquad = \Delta f _ { 2 c } ^ { * } + \Delta f _ { 2 l } ^ { * } , } \end{array} .
$$

$$
{ n ^ { \prime } } \frac { \partial \sigma _ { \vartheta } ^ { ( 2 ) } } { \partial M ^ { \prime } } + \biggl ( \frac { \partial \sigma _ { \vartheta } ^ { ( 2 ) } } { \partial t } \biggr ) { = } f _ { 2 S } ( a ^ { \prime } , e ^ { \prime } , i ^ { \prime } , \Omega ^ { \prime } , \omega ^ { \prime } , M ^ { \prime } , t ) ,
$$

后一式给出 $\pmb { \sigma } _ { \pmb { \mathcal { S } } } ^ { ( 2 ) }$ 增加的在一阶解中需要保留的一些特殊项，第二次变换增加

$$
\begin{array} { c } { { \Delta f _ { \mathrm { \ell } ^ { \ast \ast } = \Delta f _ { \mathrm { 2 } \mathrm { { c } } } \left( a ^ { \prime \prime } , e ^ { \prime \prime } , \mathrm { i } ^ { \prime \prime } \right) , } } } \\ { { ( f _ { \mathrm { \ell } ^ { \ast } } ^ { \ast } ) _ { \omega ^ { \prime \prime } } \displaystyle \frac { \partial \sigma _ { \mathrm { \ell } ^ { ( 1 ) } } ^ { ( 1 ) } } { \partial \omega } + ( f _ { 1 } ^ { \ast } ) _ { a ^ { \prime \prime } } \displaystyle \frac { \partial \sigma _ { \mathrm { \ell } } ^ { ( 1 ) } } { \partial \mathcal { Q } _ { \mathrm { \ell ^ { \prime } } } } + \left( \displaystyle \frac { \partial \sigma _ { \mathrm { \ell } } ^ { ( 1 ) } } { \partial \mathrm { \ell } } \right) = \Delta f _ { \mathrm { \ell } ^ { \ast } \mathrm { \ell } } ^ { \ast } + \left( \displaystyle \frac { \partial f _ { \mathrm { \ell } } ^ { \ast } } { \partial e ^ { \prime \prime } } e _ { \mathrm { \ell } } ^ { ( 1 ) } \right. } } \\ { { \displaystyle \left. + \displaystyle \frac { \partial f _ { \mathrm { \ell } } ^ { \ast } } { \partial \dot { \sigma } ^ { \prime \prime } } \dot { \mathrm { \ell } } _ { \mathrm { \ell } } ^ { ( 1 ) } \right) } . }  \end{array}
$$

后一式给出 $\pmb { \sigma } _ { i } ^ { ( 1 ) }$ 增加的部分，注意,该式中的 $f _ { 1 } ^ { * }$ 即 $\pmb { J _ { 2 } }$ 部分，且有

$$
\left( f _ { 1 } ^ { \ast } \right) _ { a } = ( f _ { 1 } ^ { \ast } ) _ { e } = ( f _ { 1 } ^ { \ast } ) _ { i } = 0 .
$$

(7.421）式右端涉及求 $M _ { \mathrm { ~ i ~ } } ^ { ( 1 ) }$ 的 $\pmb { a } _ { l } ^ { ( 2 ) }$ 部分未写，因为除 $\pmb { J _ { 2 } }$ 项摄动会引起 $\pmb { a } _ { l } ^ { ( 2 ) }$ 以外，其它摄动往往不产生 ${ \pmb { a } } _ { l } ^ { ( 2 ) }$ 项(见第五章85.4),或处理成长期项.

# 参考文献

[1 ] Winter,A.,The Analytical Foundations of Celestial Mechanics,Princeton University Press,Princeton(1952).   
[2]Hori,G.,Publ. Astron.Soc.Japan,18(1966),287.   
[3]Deprit,A.,Celest. Mech.,1(1969),12.   
[ 4] Grobner,W.,Die Lie-Reihen und Thre Anwendungen,Spring er-Verlag(1960).   
[5] Von Zeipel,H.,Arkiv Mat.Astron.,Fys.,(1961).   
£6]Howland,R.A.,Celest. Mech.,19(1979),139.   
[7]刘林，天文学报,23(1982),255.   
[8] Moser,J.,Proc.Acad.Sci.,USA,47(1961),1824.   
[9] Howl and,R.A.,Celest.Mech.,15(1977),327.   
[10] Howland,R.A.Celest. Mech.,19(1979),95. [11] Kinoshita,H.,SAO Spec Rep.,379(1977).   
[12]刘林，赵德滋，天文学报,20(1979),349.   
[13]刘林,赵德滋,南京大学学报（自然科学版),1978,No.1,1.   
[14] Garfinkel,B.,Astron.,J.,71(1966),657.   
[15] L.Liu and Innanen, K.A.and Zhang, S.P.， Astron.J.，90 (1985),877.   
[16] Brouwer,D.and Hori,G.,Astron.J.,66(1961),193.   
[17] Kamel,A.A.,Celest.Mech.,3(1970),90.   
[18]刘林，天文学报,23(1982),255.   
[19]刘林,章圣泮，南京大学学报(自然科学版),1982,No.2,359.   
[20]刘林,章圣泮，中国科学(A辑),1983,No.5,455.   
[21]刘林，飞行器测控技术,1983,No.3,1.

# 第八章 日月摄动

讨论日、月对人造地球卫星运动的影响，是天体力学中的一种典型的第三体摄动问题，虽然这类摄动力也是一种保守力，但由于日、月和地球、卫星相距都不太远，问题就变得比较复杂。在一定精度要求下，日、月和地球都不能简单地看成质点，而且还要考虑日、月引力引起的地球形变(潮汐形变)对卫星的影响.

如果日、月与地球都看成质点，讨论卫星绕地球运动问题时，根据非惯性坐标系(受日、月引力作用的地心坐标系)中卫星受力分析，不难给出日-月摄动加速度为

$$
- G m ^ { \prime } \Bigl ( \frac { \Delta } { \Delta ^ { 3 } } + \frac { r ^ { \prime } } { r ^ { \prime 3 } } \Bigr ) ,
$$

$m ^ { \prime }$ 是日、月质量，其它各量的意义见图8.1．由于日、月摄动机制完全相同，讨论方法也几乎一致,因此，总是把这两种摄动放在一起考虑，通常叫做日-月摄动(LunesolarPerturbations),以后就简称日月摄动.

![](images/acc7987fefd704a940768dbbc95d9f8fa0c442bc419b8eb73340007707c330a5.jpg)  
图8.1地心 $o$ ，卫星 $\smash { \boldsymbol { s } } _ { \ast }$ 和日、月 $\mathbf { \delta } _ { \mathbf { \alpha } } \mathbf { \delta } _ { \mathbf { \alpha } } \mathbf { \delta } _ { \mathbf { \alpha } } \mathbf { \delta } _ { \mathbf { \alpha } } \mathbf { \delta } _ { \mathbf { \alpha } } \mathbf { \delta } _ { \mathbf { \alpha } } \mathbf { \delta } _ { \mathbf { \alpha } } \mathbf { \delta } _ { \mathbf { \alpha } } \mathbf { \delta } _ { \mathbf { \alpha } } \mathbf { \delta } _ { \mathbf { \alpha } } \mathbf { \delta } _ { \mathbf { \alpha } } \mathbf { \delta } _ { \mathbf { \alpha } } \mathbf { \delta } _ { \mathbf { \alpha } } \mathbf { \delta } _ { \mathbf { \alpha } } \mathbf { \delta } _ { \mathbf { \alpha } } \mathbf { \delta } _ { \mathbf { \alpha } }$ 的相对位置

对于人造地球卫星， $r \ll ( \Delta , r ^ { \prime } )$ ,近似地有 $\Delta ^ { 3 } = r ^ { \prime 3 }$ ，于是日月摄动加速度可写成

$$
- G m ^ { \prime } \frac { r } { \Delta ^ { 3 } } ( \frac { r } { r } )
$$

与地球中心引力加速度之比为

$$
\frac { m ^ { \prime } } { M } \Big ( \frac { r } { \Delta } \Big ) ^ { 3 } .
$$

若引用第一章提出的计算单位,则对日、月分别有

$$
\begin{array} { l } { { m _ { \odot } { \approx } 3 . 3 \times 1 0 ^ { 5 } , ~ \Delta _ { \odot } { = } 2 . 3 \times 1 0 ^ { 4 } , } } \\ { { m _ { \odot } { = } 1 . 2 \times 1 0 ^ { - 2 } , \Delta _ { \odot } { \approx } 6 0 . } } \end{array}
$$

那么，对于近地卫星 $( r { \leqslant } 1 . 3 )$ ,相应地有

$$
\begin{array} { r l } & { m _ { \odot } \Big ( \frac { r } { \Delta _ { \odot } } \Big ) ^ { 3 } \leqslant 0 . 6 \times 1 0 ^ { - 7 } , } \\ & { m _ {  { q } } \Big ( \frac { r } { \Delta _ {  { q } } } \Big ) ^ { 3 } \leqslant 1 . 2 \times 1 0 ^ { - 7 } . } \end{array}
$$

而对于远地卫星(如 $2 4 ^ { \mathfrak { n } }$ 地球同步卫星， $r \approx 6 . 6 )$ ，却有

$$
m _ { \odot } { \left( \frac { r } { \Delta _ { \odot } } \right) } ^ { 3 } \approx 1 0 ^ { - 5 } ,
$$

$$
m _ { ^ { \flat } \flat } \biggl ( { \frac { r } { \Delta _ { \flat } } } \biggr ) ^ { 3 } \{ \approx 2 \times 1 0 ^ { - 5 } \biggl .
$$

根据上述估计，在一般情况下，日月摄动力亦可看成二阶小量．但是，并不像地球引力场位函数展开式中的 $J _ { 3 9 } \ { J } _ { 4 9 } \cdots$ 项那么简单，这里将涉及日、月位置矢量 $\gamma ^ { \prime }$ 的计算问题．除此之外，还要考查日、月和地球形状以及日、月引起的地球形变对卫星运动的影响，日月摄动加速度并不像上面给出的那么简单．因此，在这一章里,将首先介绍相应的动力模型以及日、月位置的近似计算。

# 8.1 动力模型和日、月位置的近似计算

# 1．动力模型

对于日、月、地球和卫星这一力学系统，最简单的模型就是处理成四个质点，这是一个典型的限制性四体系统。讨论小天体（人

造卫星)绕主天体(地球)运动时，相应的摄动加速度即

$$
\begin{array} { l } { { F _ { e } = - G m ^ { \prime } \Bigl ( \frac { \Delta } { \Delta ^ { 3 } } + \frac { r ^ { \prime } } { r ^ { \prime 3 } } \Bigr ) , \nonumber \Bigg \} } } \\ { { \Delta = r - r ^ { \prime } . } } \end{array}
$$

其中日、月的位置矢量 $r ^ { \prime } { = } r ^ { \prime } ( t )$ 虽然作为时间 $\pmb { t }$ 的已知函数，但必须达到一定的精度。

进一步要考虑日、月和地球的形状，前者就是简单的日、月形状摄动,而后者提及的地球形状，是考虑日、月对地心坐标系的影响所涉及的问题．它不同于第五章讨论的地球形状摄动，这是一种间接影响.

关于日、月形状摄动，可对最大的扁率项作一估计．对于月球$J _ { 2 } ^ { \prime } { = } 2 \times 1 0 ^ { - 4 }$ ，太阳更小，考虑日、月扁率后，摄动加速度(8.1)式应变为

$$
F _ { \varepsilon } = - G m ^ { \prime } \Big \{ \frac { \Delta } { \Delta ^ { 3 } } [ 1 + A ( J _ { 2 } ^ { \prime } ) ] + \thinspace \frac { \thinspace r ^ { \prime } } { r ^ { \prime 3 } } [ 1 + B ( J _ { 2 } ^ { \prime } ) ] \Big \} .
$$

因这里是量级估计，可略去纬度项,于是利用 $r \ll ( \Delta , r ^ { \prime } )$ 和 $\Delta \approx r _ { 1 } ^ { \prime }$ 上式简化成

$$
F _ { \varepsilon } = - G m ^ { \prime } \frac { r } { \Delta ^ { 3 } } \biggl ( \frac { r } { r } \biggr ) \biggl [ 1 - 3 J _ { 2 } ^ { \prime } \biggl ( \frac { a _ { e } ^ { * } } { r ^ { \prime } } \biggr ) ^ { 2 } \biggr ] .
$$

对于月球， $a _ { e } ^ { \prime } = 1 7 0 0 { \mathrm { k m } }$ ，因此有

$$
3 J _ { 2 } ^ { \prime } \Big ( \frac { a _ { e } ^ { \prime } } { r ^ { \prime } } \Big ) ^ { 2 } = 1 . 2 \times 1 0 ^ { - 8 } .
$$

对于太阳，此值更小.根据前面已给出的日月摄动加速度主项相对地球中心引力加速度的大小，不难看出，在目前测量精度下，日、月形状摄动不必考虑，即在上述动力模型中，日、月完全可以看成质点．至于地球是否可以看成质点，也可作一估计．此时，(8.1)式将变为

$$
\left. \begin{array} { l } { F _ { \varepsilon } = - G m ^ { \prime } \Big \{ \frac { \Delta } { \Delta ^ { 3 } } { - } \big ( \frac { \partial V ^ { \prime } } { \partial r ^ { \prime } } \big ) ^ { T } \Big \} , } \\ { V ^ { \prime } = \frac { 1 } { r ^ { \prime } } \Big [ 1 { - } J _ { 2 } \Big ( \frac { \alpha _ { e } } { r ^ { \prime } } \Big ) ^ { 2 } P _ { 2 } ( \sin \varphi ^ { \prime } ) \Big ] . } \end{array} \right\}
$$

其中 $\left( { \frac { \partial V ^ { \prime } } { \partial r ^ { \prime } } } \right) ^ { 1 }$ 是列向量， $- G m ^ { \prime } \Bigl ( \frac { \partial V ^ { \prime } } { \partial r ^ { \prime } } \Bigr ) ^ { \tau }$ 是作为质点的月球与作为扁球体的地球相互作用使地球获得的加速度，同样略去纬度项，并利用 $\pmb { r } \ll ( \Delta , \pmb { r } ^ { \prime } ) , \Delta \approx \pmb { r } ^ { \prime } ;$ 可将(8.3)式近似地写成

$$
F _ { \varepsilon } = - G m ^ { \prime } \frac { r } { \Delta ^ { 3 } } \bigg ( \frac { r } { r } \bigg ) ( 1 - 3 J _ { 2 } a _ { e } / r r ^ { \prime } ) .
$$

由此不难看出，在高精度要求下，(8.3)式中的地球扁率不能忽略，此即日月摄动中的地球扁率间接摄动。

考虑地球扁率后，日、月对地球引力作用还存在一种力矩效应，使地球赤道面在空间摆动，此即岁差章动现象，这也要改变地球引力位。关于这一问题，实质上是一个坐标系问题，也可以简单地处理成一个坐标转换问题，将在后面第十一章中讨论.

最后还要考虑地球并非刚体，在日、月引力作用下会发生弹性形变——潮汐现象,这将改变地球引力场的“平衡态”,使得引力位随时间变化，该变化就要影响卫星的轨道，此即潮汐摄动。相应的摄动加速度要复杂些,其影响往往不能忽略，本章最后一节将要详细讨论它.

# 2.日、月位置矢量 $\mathbf { \Omega } _ { \mathbf { \Omega } ^ { \prime } } \mathbf { \Omega } _ { \mathbf { \Omega } }$ 的近似计算

上述各种模型都涉及日、月位置矢量 $\mathbf { \boldsymbol { r } } ^ { \prime } { = } \mathbf { \boldsymbol { r } } ^ { \prime } ( t )$ 的计算问题.对于太阳轨道(即地球轨道,以后不再说明),情况比较简单．因为引起轨道变化的主要摄动源是木星引力，其摄动力的量级只有$1 0 ^ { - 5 }$ ，即使对于目前几个厘米的激光测距精度，根据前面的估计，处理10天的资料(就近地卫星而言，弧段约为 $1 0 ^ { 3 }$ ，而对远地卫星，弧段只有 $\mathsf { 1 0 ^ { 2 } }$ ),亦无需考虑其轨道变化,尤其是周期变化，近年来天文年历给出了最新采用的包含长期变化的太阳平均轨道根数，分别记 $a , e , \varepsilon , L , T , \bar { M } { = } L { - } \bar { C }$ 为太阳轨道半长径，偏心率，黄赤交角，对于当天平春分点的几何平黄径,近地点平黄径和平近点角（皆为平均根数)，有

$$
\left. \begin{array} { l } { { a = 1 . 0 0 0 0 0 1 0 2 , } } \\ { { e = 0 . 0 1 6 7 0 8 6 2 - 0 . 0 0 0 0 4 2 0 4 \mathrm { T } - 0 . 0 0 0 0 0 1 2 4 \mathrm { T } ^ { 2 } , } } \\ { { \varepsilon = 2 3 ^ { \circ } 2 6 ^ { \prime } 2 1 ^ { \prime \prime } 4 4 8 - 4 6 ^ { \prime \prime } . 8 1 5 0 \mathrm { T } - 0 ^ { \prime \prime } . 0 0 0 5 9 \mathrm { T } ^ { 2 } , } } \\ { { L = 2 8 0 ^ { \circ } 2 7 ^ { \prime } 5 9 ^ { \prime \prime } . 2 1 + 1 2 9 6 0 2 7 7 1 ^ { \prime \prime } . 3 6 \mathrm { T } + 1 ^ { \prime \prime } . 0 9 3 \mathrm { T } ^ { 2 } , } } \\ { { T = 2 8 2 ^ { \circ } 5 6 ^ { \prime } 1 4 ^ { \prime \prime } . 4 5 - 6 1 9 0 ^ { \prime \prime } . 3 2 \mathrm { T } + 1 ^ { \prime } . 6 5 5 \mathrm { T } ^ { 2 } , } } \\ { { M = 3 5 7 ^ { \circ } 3 1 ^ { \prime } 4 4 ^ { \prime \prime } . 7 6 + 1 2 9 5 9 6 5 8 1 ^ { \prime \prime } . 0 4 \mathrm { T } - 0 ^ { \prime \prime } . 5 6 2 \mathrm { T } ^ { 2 } . } } \end{array} \right\}
$$

式中 $\mathbf { T }$ 为自标准历元J2000.0（即2000年1月1日 $1 2 ^ { \mathrm { { h } } } \mathrm { { T D T } ) }$ 算起的儒略世纪数，如要知道 $L$ 和 $r$ 对标准历元平春分点的值，只需进行岁差改正即行.

关于月球轨道，问题比较复杂。由于月球在绕地球运行过程中,太阳摄动特别大，其摄动力的量级为 $1 0 ^ { - 2 }$ ，月球轨道变化迅速.因此，在一定精度要求下，计算月球对人造卫星运动的影响时，往往需要同时考虑月球的轨道变化．过去的历书(或有关星表)都是以等间距列表形式给出天体的位置，这显然不便于使用．近年来出现了便于计算机应用的历书，这种计算机历书是采用截断的切比雪夫(Chebychev)级数或幂多项式作为一定时间范围内天体位置的逼近公式，我国从事历书工作的专家们也开展了这项工作，在文献[1]中有较详尽的说明．如果有根据时间变量直接计算月球精确位置的逼近式，那么对于卫星有摄星历表(包含月球摄动）的数值计算来说，确实很方便．但是它不便于用来探讨月球对人造卫星运动影响的规律，因此，有必要了解月球轨道变化的分析形式．过去，各国天文年历都采用了布朗(Brown)的结果[2]，但其表达形式不便于用来讨论人造卫星的轨道变化．这里将有针对性地给出一种近似公式，它是用第五章中的平均根数法导出的[31，计算月球位置的精度可达 $1 0 ^ { - 8 } { - } 1 0 ^ { - 4 }$ ，既可用来进行分析研究，也可用于相应精度要求下的卫星有摄星历表的计算。

首先给出最新采用的月球轨道的平均根数(见天文年历)：

$$
\left. \begin{array} { l } { a ^ { \prime } = 3 8 4 7 4 7 . 9 8 1 \mathrm { k m } , } \\ { e ^ { \prime } = 0 . 0 5 4 8 7 9 9 0 5 , } \\ { \sin \frac { J } { 2 } = 0 . 0 4 4 7 5 1 3 0 5 } \\ { L ^ { \prime } = 2 1 8 ^ { \circ } 1 8 ^ { \circ } 5 9 ^ { \prime } , 5 6 + 4 8 1 2 6 7 ^ { \circ } 5 2 ^ { \prime } 5 2 ^ { \prime } 8 3 3 \mathrm { T } - 4 ^ { \prime \prime } . 7 8 7 7 ^ { \prime } , } \\ { T ^ { \prime } = 8 3 ^ { \circ } 2 1 ^ { \prime } 1 1 ^ { \prime } , 6 7 + 4 0 6 9 ^ { \circ } 0 0 ^ { \prime } 4 9 ^ { \prime \prime } , 3 6 \mathrm { T } - 3 7 ^ { \prime \prime } , 1 6 5 7 ^ { \prime } , } \\ { \mathcal { Q } _ { 4 } = 1 2 5 ^ { \circ } 0 2 ^ { \prime } 4 ^ { \prime } 0 ^ { \prime \prime } , 4 0 - 1 9 3 4 ^ { \circ } 0 3 ^ { \prime } 0 3 ^ { \prime } , 2 6 8 \mathrm { T } + 7 ^ { \prime \prime } , 4 7 6 1 ^ { \prime } , } \\  F = 9 3 ^ { \circ } 1 8 ^ { \prime } 1 9 ^ { \prime } , 5 6 + \frac { 4 8 3 2 0 2 ^ { \circ } 0 1 ^ { \prime } 0 3 ^ { \prime \prime } , 0 9 9 \mathrm { T } - 1 2 ^ { \prime \prime } , 2 5 4 \mathrm { T } ^ { \prime \prime } , } \\ { p = - 2 9 7 ^ { \circ } 5 1 ^ { \prime } 0 ^ { \prime \prime } , 7 4 + 4 4 5 2 6 7 ^ { \circ } 0 ^ { \prime } 4 1 ^ { \prime \prime } , 4 6 9 1 - 5 ^ { \prime \prime } , 8 3 2 1 ^ { \prime } . } \end{array} \right\}
$$

这组数据对应地心黄道坐标系， $\pmb { \tilde { \mathbf { T } } }$ 的起算历元仍为 $\mathbf { J 2 0 0 0 . 0 , } J$ 是黄白交角， $L ^ { \prime } , T ^ { \prime }$ 和 $\Omega _ { \mathfrak { g } }$ 分别为对当天平春分点的月球平黄径，近地点平黄径和升交点平黄径， $\pmb { F } \equiv \pmb { L } ^ { \prime } - \pmb { \Omega } _ { a }$ 是月球升交距角， $\pmb { D } = \pmb { L } ^ { \prime }$ $- L$ 是月球与太阳的平距角．在平均根数已知的条件下，可算出地心黄道坐标系中月球轨道变化周期项的系数，那么由文献[3]给出的月球轨道瞬时根数的近似表达式就可写成下列形式：

$$
\left. \begin{array} { l } { \displaystyle \widetilde { \lambda } = \widetilde { \gamma } + \widetilde { \omega } + \widetilde { \Omega } } \\ { \displaystyle = L ^ { \prime } + C _ { 1 } + \sum _ { j } K _ { j } \sin \alpha _ { j } , } \\ { \displaystyle \frac { 1 } { r ^ { \prime } } = \frac { 1 } { r _ { 0 } ^ { \prime } } \biggl ( 1 + C _ { 2 } + \sum _ { j } ^ { \prime } Q _ { j } \cos \alpha _ { j } \biggr ) } \\ { \displaystyle \widetilde { \Omega } = Q _ { p } + C _ { 3 } + \sum _ { j } ^ { \prime } Q _ { j } \sin \alpha _ { j } , } \\ { \displaystyle \widetilde { J } = J + \sum _ { j } J _ { j } \cos \alpha _ { j } , } \end{array} \right\}
$$

其中

$$
\begin{array} { r l r } & { C _ { 1 } = 0 . 1 0 9 7 6 \sin M ^ { \prime } + 0 . 0 0 3 7 3 \sin 2 M ^ { \prime } + 0 . 0 0 0 1 7 \sin 3 M ^ { \prime } , } & \\ & { C _ { 2 } = 0 . 0 5 4 5 0 \cos 3 M ^ { \prime } + 0 . 0 0 2 9 7 \cos 2 M ^ { \prime } + 0 . 0 0 0 1 8 \cos 3 M ^ { \prime } , } & \\ & { C _ { 8 } = 0 . 0 0 0 4 7 \sin M ^ { \prime } , } & { . } \end{array}
$$

$\frac { 1 } { r _ { 0 } ^ { ' } }$ 是月球地平视差正弦常数，有

$$
\underset { r _ { 0 } ^ { \prime } } { \overset { 1 } { \underset { 0 } { \ldots } } } = \sin \pi _ { \mathrm { ~ } \mathrm { { q } } } = 3 4 2 2 ^ { \prime \prime } . 4 4 8 = \underset { 6 0 . 2 6 8 2 0 7 5 \mathrm { { 1 } } } { \overset { 1 } { \underset { \mathrm { { 1 } } } { \\\ { \mathrm { 6 } } } } } .
$$

$c _ { i }$ 和 $C _ { 2 }$ 也叫中心差，包含了椭圆项和以 $k M ^ { \prime } ( k { = } 1 , 2 , \cdots )$ 为引数的周期项， $M ^ { \prime } { = } L ^ { \prime } { - } T ^ { \prime }$ 是月球的平近点角，它是平均根数．各周期项系数列于表8.1.

表8.1  

<table><tr><td rowspan=1 colspan=1>j</td><td rowspan=1 colspan=1>K,</td><td rowspan=1 colspan=1>Q，</td><td rowspan=1 colspan=1>m</td><td rowspan=1 colspan=1>J</td><td rowspan=1 colspan=1>d</td><td rowspan=1 colspan=1>d的每小时变率</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2.223</td><td rowspan=1 colspan=1>1.002</td><td rowspan=1 colspan=1>0.082</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>2D-M&#x27;</td><td rowspan=1 colspan=1>04715</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>1.161</td><td rowspan=1 colspan=1>0.825</td><td rowspan=1 colspan=1>10.230</td><td rowspan=1 colspan=1>-0.019</td><td rowspan=1 colspan=1>2D</td><td rowspan=1 colspan=1>10159</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>0.324</td><td rowspan=1 colspan=1>0.012</td><td rowspan=1 colspan=1>0.283</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>M±180°</td><td rowspan=1 colspan=1>0:0411</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-0.213</td><td rowspan=1 colspan=1>-0.019</td><td rowspan=1 colspan=1>2F±180</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>0.103</td><td rowspan=1 colspan=1>0.009</td><td rowspan=1 colspan=1>0.045</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>2M&#x27;-2D±180°</td><td rowspan=1 colspan=1>0:0728</td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>0.100</td><td rowspan=1 colspan=1>0.042</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>2D-M&#x27;-M</td><td rowspan=1 colspan=1>0:4304</td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>0.093</td><td rowspan=1 colspan=1>0.090</td><td rowspan=1 colspan=1>10.008</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>2D+M&#x27;</td><td rowspan=1 colspan=1>1:5603</td></tr><tr><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>0.080</td><td rowspan=1 colspan=1>0.056</td><td rowspan=1 colspan=1>-0.012</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>2D-M</td><td rowspan=1 colspan=1>0.9748</td></tr><tr><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>0.072</td><td rowspan=1 colspan=1>0.034</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>M&#x27;-M</td><td rowspan=1 colspan=1>0.5033</td></tr><tr><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>0.061</td><td rowspan=1 colspan=1>0.029</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>D±180°</td><td rowspan=1 colspan=1>0.5080</td></tr><tr><td rowspan=1 colspan=1>11</td><td rowspan=1 colspan=1>0.053</td><td rowspan=1 colspan=1>0.028</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>M&#x27;+M±180°</td><td rowspan=1 colspan=1>0:5854</td></tr><tr><td rowspan=1 colspan=1>12</td><td rowspan=1 colspan=1>0.027</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-2.724</td><td rowspan=1 colspan=1>-0.241</td><td rowspan=1 colspan=1>2F-2D±180°</td><td rowspan=1 colspan=1>0:0866</td></tr><tr><td rowspan=1 colspan=1>13</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>10.008</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>2F+M&#x27;±180°</td><td rowspan=1 colspan=1></td></tr></table>

续表

<table><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>K</td><td rowspan=1 colspan=1>Q</td><td rowspan=1 colspan=1>,</td><td rowspan=1 colspan=1>J</td><td rowspan=1 colspan=1>aaj</td><td rowspan=1 colspan=1>x的每小时变率</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0.041</td><td rowspan=1 colspan=1>0.020</td><td rowspan=1 colspan=1>0.070</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>2F-M&#x27;±180°</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>15</td><td rowspan=1 colspan=1>0.018</td><td rowspan=1 colspan=1>C.018</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>4D-M&#x27;</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>16</td><td rowspan=1 colspan=1>0.015</td><td rowspan=1 colspan=1>0.012</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>4D-2M&#x27;</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>17</td><td rowspan=1 colspan=1>0.014</td><td rowspan=1 colspan=1>0.007</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>2D+M-M&#x27;±180°</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>18</td><td rowspan=1 colspan=1>0.012</td><td rowspan=1 colspan=1>0.009</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>2D+M±180°</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>19</td><td rowspan=1 colspan=1>0.009</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>M&#x27;-D</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>0.009</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>D+M&#x27;</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>21</td><td rowspan=1 colspan=1>0.007</td><td rowspan=1 colspan=1>0.007</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>2D-M+M&#x27;</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>22</td><td rowspan=1 colspan=1>0.007</td><td rowspan=1 colspan=1>0.009</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>2D+2M&#x27;</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>23</td><td rowspan=1 colspan=1>0.007</td><td rowspan=1 colspan=1>0.008</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>4D</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>24</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.019</td><td rowspan=1 colspan=1>0.018</td><td rowspan=1 colspan=1>2F-2M&#x27;</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>25</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.110</td><td rowspan=1 colspan=1>0.010</td><td rowspan=1 colspan=1>2F-2D+M</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>26</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.047</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>2D-2F+M</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>27</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.023</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>2F-2D-M&#x27;</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>28</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.023</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>2D-2F-M&#x27;</td><td rowspan=1 colspan=1></td></tr></table>

表中 $K _ { j } , Q _ { j 3 } \varOmega _ { j }$ 和 ${ \pmb J } _ { j }$ 的数据全部都要乘 ${ \bf 1 0 ^ { - 2 } }$ ，凡是空格，表示不存在该项，或是量级小于 $1 0 ^ { - 4 }$ 对于 $1 0 ^ { - 3 } - 1 0 ^ { - 4 }$ 的位置精度，只要取前12项就够了.

月球轨道瞬时根数表达式(8.7）式不仅便于后面讨论月球摄动，而且也可以用来直接计算月球位置矢量 $r ^ { \prime } ( t )$ ，根据第六章(6.3)式和(6.5)式有

$$
\begin{array} { r } { r ^ { \prime } { = } r ^ { \prime } \cos { ( \widetilde { \lambda } { - } \widetilde { \Omega } ) } \hat { P } ^ { * } { + } r ^ { \prime } \sin { ( \widetilde { \lambda } { - } \widetilde { \Omega } ) } \hat { Q } ^ { * } , } \end{array}
$$