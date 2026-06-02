# 第4章 李导数、Killing场和超曲面

# \$4.1 流形间的映射

设 $M , ~ N$ 为流形(维数可不同)， $\phi : M \to N$ 为光滑映射．以 $\mathcal { F } _ { M }$ 和 $\mathcal { F } _ { N }$ 分别代表 $M$ 和 $N$ 上光滑函数的集合， $\mathcal { F } _ { M } ( k , l )$ 和 $\mathcal { F } _ { N } ( k , l )$ 分别代表 $M$ 和 $N$ 上光滑 $( k , ~ l )$ 型张量场的集合· $\phi$ 自然诱导出一系列映射如下.

定义1拉回(pull back)映射 ${ \phi } ^ { * } : \mathcal { F } _ { N }  \mathcal { F } _ { M }$ 定义为

$$
( \phi ^ { * } f ) | _ { p } : = f | _ { \phi ( p ) } , \qquad \forall f \in { \mathcal { F } } _ { N } , p \in M ,
$$

即 $\phi ^ { * } f = f \circ \phi$ ，见图4-1.

![](images/51d419233d2a9f986ad46ebf0ace41b940fe9faaf1997e0fc170e20056f70efd.jpg)  
图4-1 $\phi ^ { * } f$ 的定义

由定义1不难证明：

(1) ${ \phi } ^ { * } : \mathcal { F } _ { N }  \mathcal { F } _ { M }$ 是线性映射，即

$$
{ \phi } ^ { \ast } ( \alpha f + \beta g ) = \alpha { \phi } ^ { \ast } ( f ) + \beta { \phi } ^ { \ast } ( g ) \quad \forall f , \ g \in \mathscr { F } _ { N } , \quad \alpha , \ \beta \in \mathbb { R } .
$$

$$
{ \phi } ^ { \ast } ( f g ) = { \phi } ^ { \ast } ( f ) { \phi } ^ { \ast } ( g ) , \qquad \forall f , g \in \mathcal { F } _ { N } .
$$

定义2对 $M$ 中任一点 $p$ 可定义推前(push forward)映射 $\phi _ { * } : V _ { p } \to V _ { \phi ( p ) }$ 如下：$\forall v ^ { a } \in V _ { p }$ ，定义其像 $\phi _ { * } { v ^ { a } } \in V _ { \phi ( p ) }$ 为

$$
\left( \phi _ { * } \upsilon \right) \left( f \right) : = \upsilon \left( \phi ^ { * } f \right) , \quad \quad \forall f \in \mathcal { F } _ { N } .
$$

还应证明(习题)这样定义的 $\phi _ { * } { \nu } ^ { a }$ 满足 $\ S 2 . 2$ 定义2对矢量的两个要求，从而确是 $\phi ( p )$ 点的矢量．许多文献也把 $\phi _ { * }$ 称为 $\phi$ 的切映射.

定理 4-1-1 $\phi _ { * } : V _ { p } \to V _ { \phi ( p ) }$ 是线性映射，即

$$
\phi _ { * } ( \alpha u ^ { a } + \beta v ^ { a } ) = \alpha \phi _ { * } u ^ { a } + \beta \phi _ { * } v ^ { a } , \qquad \forall u ^ { a } , v ^ { a } \in V _ { p } , \alpha , \beta \in \mathbb { R } .
$$

证明 习题.

定理4-1-2设 $C \left( t \right)$ 是 $M$ 中的曲线， $T ^ { a }$ 为曲线在 $C ( t _ { 0 } )$ 点的切矢，则 $\phi _ { * } T ^ { a } \in$

$V _ { \phi ( C ( t _ { 0 } ) ) }$ 是曲线 $\phi ( C ( t ) )$ 在 $\phi ( C ( t _ { 0 } ) )$ 点的切矢(曲线切矢的像是曲线像的切矢).

证明习题．提示：利用曲线切矢定义[式(2-2-6)].

定义3拉回映射可按如下方式延拓至 ${ \phi } ^ { \ast } : \mathcal { F } _ { N } ( 0 , l )  \mathcal { F } _ { M } ( 0 , l )$ ：

$\forall T \in \mathcal { F } _ { N } ( 0 , l )$ ，定义 ${ \phi } ^ { \ast } T \in \mathcal { F } _ { M } ( 0 , l )$ 为

$$
( \phi ^ { * } T ) _ { a _ { 1 } \cdots a _ { l } } \mid _ { p } ( \upsilon _ { 1 } ) ^ { a _ { 1 } } \cdots ( \upsilon _ { l } ) ^ { a _ { l } } : = T _ { a _ { 1 } \cdots a _ { l } } \mid _ { \phi ( p ) } ( \phi _ { * } \upsilon _ { 1 } ) ^ { a _ { 1 } } \cdots ( \phi _ { * } \upsilon _ { l } ) ^ { a _ { l } } ,
$$

$$
\forall p \in M , \ : \upsilon _ { 1 } , \cdots , \upsilon _ { l } \in V _ { p } .
$$

定义4 $\forall p \in M$ ，推前映射 $\phi _ { * }$ 可按如下方式延拓至 $\phi _ { * } : \mathcal { T } _ { V _ { p } } ( k , 0 ) \to$ $\mathcal { T } _ { V _ { \phi ( p ) } } ( k , 0 )$ [即 $\phi _ { * }$ 是把 $p$ 点的 $( k , \ 0 )$ 型张量变为 $\phi ( p )$ 点的同型张量的映射]：$\forall T \in \mathcal { T } _ { V _ { p } } ( k , 0 )$ ，其像 $\phi _ { * } T \in \mathcal { T } _ { V _ { \phi ( p ) } } ( k , 0 )$ 由下式定义：

$$
\begin{array} { c } { { ( \phi _ { * } T ) ^ { a _ { 1 } \cdots a _ { k } } ( \omega ^ { 1 } ) _ { a _ { 1 } } \cdots ( \omega ^ { k } ) _ { a _ { k } } : = T ^ { a _ { 1 } \cdots a _ { k } } ( \phi ^ { * } \omega ^ { 1 } ) _ { a _ { 1 } } \cdots ( \phi ^ { * } \omega ^ { k } ) _ { a _ { k } } , } } \\ { { \forall \omega ^ { 1 } , \cdots , \omega ^ { k } \in V _ { \phi ( p ) } ^ { * } , } } \end{array}
$$

其中 $( \phi ^ { * } \omega ) _ { a }$ 定义为 $( \phi ^ { * } \omega ) _ { a } \upsilon ^ { a } : = \omega _ { a } ( \phi _ { * } \upsilon ) ^ { a } \qquad \forall \upsilon ^ { a } \in V _ { p } .$

注1定义2无非是定义4在 $k = 1$ 时的特例．把标量场称为(0,0)型张量场,则定义1无非是定义3在 $l = 0$ 时的特例．定义3表明拉回映射 $\phi ^ { * }$ 能把 $N _ { _ { - } }$ 上的 $( 0 , l )$ 型张量场变为 $M$ 上的同型张量场，是场变为场的映射；而根据定义4,推前映射 $\phi _ { * }$ 只把 $M$ 中一点 $p$ 的 $( k , ~ 0 )$ 型张量变为其像点 $\phi ( p )$ 的同型张量．可否将 $\phi _ { * }$ 延拓为把$M$ 上的 $( k , 0 )$ 型张量场变为 $N$ 上的同型张量场的映射？在一般情况下不能．以矢量场为例．关键在于，给定 $M$ 上一个矢量场 $\pmb { \nu }$ 后，要定义 $N$ 上的像矢量场 $\phi _ { * } \nu$ 就要对 $N$ 的任一点 $q$ 定义一个矢量，而这势必涉及 $q$ 点的逆像 ${ \phi } ^ { - 1 } ( q )$ [可比照定义3理解．根据定义3， $\phi ^ { * }$ 可把 $N$ 上的场 $T$ 变为 $M$ 上的场 $\phi ^ { * } T$ ，而为了定义 $\phi ^ { * } T$ 在 $M$ 的任一点 $p$ 的值，自然要用到 $T$ 在 $\phi ( p )$ 点的值.]．如果 $\phi$ 不是到上映射，则 $\phi ^ { - 1 } ( q )$ 可能不存在，从而无法用 $\phi ^ { - 1 } ( q )$ 点的 $\pmb { \nu }$ 作为式(4-1-2)右边的 $\pmb { \nu }$ ；如果 $\phi$ 不是一一映射，则逆像 $\phi ^ { - 1 } ( q )$ 可能多于一点，从而无从确定该用哪一逆像点的 $\pmb { \nu }$ 作为式(4-1-2)右边的 $\pmb { \nu }$ ·这暗示，如果 $\phi$ 只是光滑映射，则 $\phi _ { * }$ 未必能把场推前为场．然而，如果$\phi : M \to N$ 是微分同胚映射，则上述困难不复存在，推前映射 $\phi _ { * }$ 可看作把 $M$ 上$( k , 0 )$ 型张量场变为 $N$ 上同型张量场的映射，即 $\phi _ { * } : \mathcal { F } _ { M } ( k , 0 ) \to \mathcal { F } _ { N } ( k , 0 )$ .再者，由于 $\phi ^ { - 1 }$ 存在而且光滑，其拉回映射 $\phi ^ { - 1 * }$ 把 $\mathcal { F } _ { M } ( 0 , l )$ 映到 $\mathcal { F } _ { N } ( 0 , l )$ ，这可看作 $\phi$ 的推前映射 $\phi _ { * }$ ，于是 $\phi _ { * }$ 又可进一步推广为 $\phi _ { * } : \mathcal { F } _ { M } ( k , l )  \mathcal { F } _ { N } ( k , l )$ ·例如，设$T ^ { a } { } _ { b } \in \mathcal { F } _ { M } ( 1 , 1 )$ ，则 $( \phi _ { * } T ) _ { \ b } ^ { a } \in \mathcal { F } _ { N } ( 1 , 1 )$ 定义为

$$
\begin{array} { r } { ( \phi _ { * } T ) _ { \phantom { a } b } ^ { a } \mid _ { q } \omega _ { a } v ^ { b } : = T _ { \phantom { a } b } ^ { a } \mid _ { \phi ^ { - 1 } ( q ) } ( \phi ^ { * } \omega ) _ { a } ( \phi ^ { * } v ) ^ { b } , \phantom { a a a a a } \forall q \in N , \omega _ { a } \in V _ { q } ^ { * } , \nu ^ { b } \in V _ { q } , } \end{array}
$$

其中(Φ\*u)应理解为(-v)ʰ.同理，拉回映射也可推广为\*：S(k,l)→m(k,l).  
推广后的 $\phi _ { * }$ 和 $\phi ^ { * }$ 仍为线性映射，而且互逆.

设 $\phi : M \to N$ 是微分同胚， $p \in M$ ， $\{ x ^ { \mu } \}$ 和 $\{ y ^ { \mu } \}$ 分别是 $M$ 和 $N$ 的局部坐标系，坐标域 $O _ { 1 }$ 和 $O _ { 2 }$ 满足 $p \in O _ { 1 } , \phi ( p ) \in O _ { 2 }$ ．于是 $p \in \phi ^ { - 1 } [ O _ { 2 } ]$ $\phi$ 为微分同胚保证M和N维数相等，故{x"}和{y"}的μ都是从1到n．微分同胚本是点的变换，但也可等价地看作坐标变换，因为可用：M→N在Φ-1[O2]上定义一组新坐标$\{ x ^ { \prime \mu } \}$ 如下： $\forall q \in \phi ^ { - 1 } [ O _ { 2 } ]$ ，定义 $x ^ { \prime \mu } ( q ) : = y ^ { \mu } ( \phi ( q ) )$ .可见微分同胚映射 $\phi$ 在 $p$ 的邻域 $O _ { 1 } \cap \phi ^ { - 1 } [ O _ { 2 } ]$ 上自动诱导出一个坐标变换 $x ^ { \mu } \mapsto x ^ { \prime \mu }$ ．由定理 4-1-2 不难证明$\forall q \in O _ { 1 } \bigcap \phi ^ { - 1 } [ O _ { 2 } ]$ 有

$$
\phi _ { * } [ ( \partial / \partial x ^ { \prime \mu } ) ^ { a } \mid _ { q } ] = ( \partial / \partial y ^ { \mu } ) ^ { a } \mid _ { \phi ( q ) } ,
$$

由此又可证明

$$
\phi _ { * } [ ( \mathrm { d } x ^ { \prime \mu } ) _ { a } \mid _ { q } ] = ( \mathrm { d } y ^ { \mu } ) _ { a } \mid _ { \phi ( q ) } .
$$

于是对微分同胚映射Φ:M→N就存在两种观点：①主动观点(active viewpoint),它如实地认为 $\phi$ 是点的变换[把 $p$ 变为 $\phi ( p )$ ]以及由此导致的张量变换[把 $p$ 点的张量 $T$ 变为 $\phi ( p )$ 点的张量 $\phi _ { * } T$ ]； $\textcircled{2}$ 被动观点(passive viewpoint)，它认为点 $p$ 及其上的所有张量T都没变,Φ:M→N的后果是坐标系有了变换(从{x"}变为{x"}).这两种观点虽然似乎相去甚远，但在实用上是等价的．下面的定理可以看作等价性的某种表现.

定理4-1-3 $( \phi _ { * } T ) ^ { \mu _ { 1 } \cdots \mu _ { k } } \nu _ { 1 } { } ^ { \ldots } \nu _ { l } \mid _ { \phi ( p ) } = T ^ { \prime \mu _ { 1 } \cdots \mu _ { k } } \nu _ { 1 } { } ^ { \ldots } \nu _ { l } \mid _ { p } , \qquad \forall T \in \mathcal { F } _ { M } ( k , l ) ,$ (4-1-6)式中左边是新点(p)的新张量Φ.T在老坐标系{y"}的分量，右边是老点p的老张量 $T$ 在新坐标系 $\{ x ^ { \prime \mu } \}$ 的分量.

证明 习题.

注2式(4-1-6)是实数等式，左边是由主动观点(认为点和张量变了而坐标系没变)所得的数,右边是由被动观点(认为点和张量没变但坐标系变了)所得的数.两边相等就表明两种观点在实用上等价.

例1设定理4-1-3中的Ta是矢量v²，令ua=u∈V(p），则由式(4-1-6)不难证明

$$
u ^ { \mu } = \upsilon ^ { \nu } ( \hat { \partial } x ^ { \prime \mu } / \hat { \partial } x ^ { \nu } ) \vert _ { p } .
$$

[选读 4-1-1]

现在进一步说明主、被动观点的等价性．设 $T _ { a b }$ 是流形 $M$ 上的张量场，则它在坐标系 $\{ x ^ { \sigma } \}$ 的分量 $T _ { \mu \nu } ( x ^ { \sigma } )$ 是坐标 $x ^ { \sigma }$ 的一组函数．设有坐标变换$\{ x ^ { \sigma } \} \to \{ x ^ { \prime \sigma } \}$ ，则 $T _ { a b }$ 在 $\{ x ^ { \prime \sigma } \}$ 系的分量 $T _ { \mu \nu } ^ { \prime } ( x ^ { \prime \sigma } )$ 是坐标 $x ^ { \prime \sigma }$ 的一组函数．两组函数一般不同(指函数关系 $T _ { \mu \nu }$ 和 $T _ { \mu \nu } ^ { \prime }$ 不同，至于自变量用什么符号则无所谓．）．要从函数组 $T _ { \mu \nu }$ 出发获得另一函数组 $T _ { \mu \nu } ^ { \prime }$ ，只须进行坐标变换而不必对流形的点及张量做变换，即无须借助于流形间的映射以及它诱导的对张量的映射．这可称为获得新函数组 $T _ { \mu \nu } ^ { \prime }$ 的“被动途径”．然而，采取如下的“主动途径”也可收到相同效果．设 $N$ 是另一流形且存在微分同胚映射 $\phi : M \to N$ ，则 $\tilde { T } _ { a b } \equiv \phi _ { * } T _ { a b }$ 是 $N$ 上的张量场，且 $\tilde { T } _ { a b }$ 在 $N$ 上坐标系 $\{ y ^ { \sigma } \}$ 的分量 $\tilde { T } _ { \mu \nu } ( y ^ { \sigma } )$ 也是一组函数，其函数关系 $\tilde { T } _ { \mu \nu } -$ 般也与 $T _ { \mu \nu }$ 不同．这途径涉及点的变换 $( \phi : M \to N )$ 及张量场的变换$( \phi _ { * } : T _ { a b } \mapsto \tilde { T } _ { a b } )$ 而不涉及坐标变换，这正是主动观点的特征．为保证殊途同归，即由主、被动途径得到的新函数组 $\tilde { T } _ { \mu \nu }$ 和 $T _ { \mu \nu } ^ { \prime }$ 相同，只须令主动途径中的微分同胚$\phi : M \to N$ 在 $M$ 上诱导的坐标变换恰为被动途径中的坐标变换 $\{ x ^ { \sigma } \} \to \{ x ^ { \prime \sigma } \}$ .事实上，设 $p \in M$ ， $q \equiv \phi ( p ) \in N$ ，则

$$
\tilde { T } _ { \mu \nu } \left( y ^ { \sigma } ( q ) \right) = \tilde { T } _ { \mu \nu } \mid _ { q } = \left( \phi _ { * } T \right) _ { \mu \nu } \mid _ { q } = T _ { \mu \nu } ^ { \prime } \mid _ { p } = T _ { \mu \nu } ^ { \prime } \left( x ^ { \prime \sigma } ( p ) \right) = T _ { \mu \nu } ^ { \prime } \left( y ^ { \sigma } ( q ) \right) ,
$$

其中第三、五步分别用到定理 4-1-3 和 ${ } ^ { 6 6 } \phi : M \to N$ 诱导的坐标变换恰为$\{ x ^ { \sigma } \}  \{ x ^ { \prime \sigma } \} ^ { \prime \prime }$ 的要求.上式表明 $\tilde { T } _ { \mu \nu } ( y ^ { \sigma } ) = T _ { \mu \nu } ^ { \prime } ( y ^ { \sigma } )$ ，即函数关系 $\tilde { T } _ { \mu \nu }$ 和 $T _ { \mu \nu } ^ { \prime }$ 相同.

以上只是说明主、被动观点在实用中的等价性的一例，其中关键一步用到定理 4-1-3.这再次表明此定理是这一等价性的某种体现. [选读4-1-1完]

[选读 4-1-2]

本选读补充几个有用的定理.

定理4-1-4设 $\phi : M \to N$ 为光滑映射，则 $\forall T \in \mathcal { F } _ { N } ( 0 , l )$ ， $T ^ { \prime } \in \mathcal { F } _ { N } ( 0 , l ^ { \prime } )$ 有

$$
\phi ^ { * } ( T T ^ { \prime } ) = \phi ^ { * } ( T ) \phi ^ { * } ( T ^ { \prime } ) .
$$

证明 请读者补上抽象指标后给出证明.

定理4-1-5设 $\phi : M \to N$ 为光滑映射，则 $\forall T \in \mathcal { F } _ { V _ { p } } ( k , 0 )$ ， $T ^ { \prime } \in \mathcal { T } _ { V _ { p } } ( k ^ { \prime } , 0 )$ 有

$$
\phi _ { * } ( T T ^ { \prime } ) = \phi _ { * } ( T ) \phi _ { * } ( T ^ { \prime } ) .
$$

证明 请读者补上抽象指标后给出证明.

定理4-1-6设 $\phi : M \to N$ 是微分同胚，则 $\forall T \in \mathcal { F } _ { M } ( k , l )$ ， $T ^ { \prime } \in \mathcal { F } _ { M } ( k ^ { \prime } , l ^ { \prime } )$ 有

$$
\phi _ { * } ( T T ^ { \prime } ) = \phi _ { * } ( T ) \phi _ { * } ( T ^ { \prime } ) .
$$

注3 $\textcircled{1}$ 上式是 $N$ 上的张量场等式，而式(4-1-9)只是点 $\phi ( { \boldsymbol { p } } ) { \dot { \in } } N$ 的张量等式 $\textcircled{2}$ 上式的 $\phi _ { * }$ 换为 $\phi ^ { * }$ 也成立，但式中的 $T$ 和 $T ^ { \prime }$ 应看成 $N$ 上的张量场，新公式应看作 $M$ 上的张量场等式.

证明 练习.

定理4-1-7设 $\phi : M \to N$ 是微分同胚，则 $\phi _ { * }$ （及 $\phi ^ { * }$ )与缩并可交换顺序.

证明欲证 $\phi _ { * } ( \mathbf { C } T ) = \mathbf { C } ( \phi _ { * } T )$ ．先以 $M$ 上张量场 $\boldsymbol { T } _ { \phantom { a } b } ^ { a }$ 为例，这时$\phi _ { * } ( \mathbf { C } T ) = \mathbf { C } ( \phi _ { * } T )$ 是 $N$ 上的标量场等式，只须证明它对任一 $p \in M$ 的像点 $\phi ( p ) \in N$

成立.设 $\{ ( e _ { \mu } ) ^ { a } \}$ 和 $\{ ( e ^ { \mu } ) _ { a } \}$ 是 $p$ 的一个基底及对偶基底,则 $T _ { b } ^ { a } = T _ { \nu } ^ { \mu } ( e _ { \mu } ) ^ { a } ( e ^ { \nu } ) _ { b }$ .由式(4-1-10)得

故

$$
\begin{array} { c } { { \phi _ { * } T _ { b } ^ { a } = ( \phi _ { * } T _ { \nu } ^ { \mu } ) [ \phi _ { * } ( e _ { \mu } ) ^ { a } ] [ \phi _ { * } ( e ^ { \nu } ) _ { b } ] \ , } } \\ { { { } } } \\ { { { \mathrm C } ( \phi _ { * } T ) = ( \phi _ { * } T _ { \nu } ^ { \mu } ) [ \phi _ { * } ( e _ { \mu } ) ^ { a } ] [ \phi _ { * } ( e ^ { \nu } ) _ { a } ] . } } \end{array}
$$

取 $( e _ { \mu } ) ^ { a }$ 和 $( e ^ { \mu } ) _ { a }$ 分别为式(4-1-4)的 $( \partial / \partial x ^ { \prime \mu } ) ^ { a }$ 和式(4-1-5)的 $( \mathrm { d } x ^ { \prime \mu } ) _ { a }$ ，则

$$
[ \phi _ { * } ( e _ { \mu } ) ^ { a } ] [ \phi _ { * } ( e ^ { \nu } ) _ { b } ] = ( \hat { \partial } / \hat { \partial } y ^ { \mu } ) ^ { a } ( \mathrm { d } x ^ { \nu } ) _ { a } = \delta ^ { \nu } { } _ { \mu } .
$$

(其实可证明对 $p$ 点的任一 $\{ ( e _ { \mu } ) ^ { a } \}$ 和 $\{ ( e ^ { \mu } ) _ { a } \}$ 都有 $[ \phi _ { * } ( e _ { \mu } ) ^ { a } ] [ \phi _ { * } ( e ^ { \nu } ) _ { b } ] = { \delta ^ { \nu } } _ { \mu } . )$ 因而

$$
\operatorname { C } ( \phi _ { * } T ) = ( \phi _ { * } T ^ { \mu } { } _ { \nu } ) \operatorname { \mathcal { S } } ^ { \nu } { } _ { \mu } = \phi _ { * } ( T ^ { \mu } { } _ { \nu } \delta ^ { \nu } { } _ { \mu } ) = \phi _ { * } ( T ^ { \mu } { } _ { \mu } ) = \phi _ { * } ( \operatorname { C } T ) .
$$

请读者把这一证明推广到 $M$ 上任意型号的张量场.

[选读4-1-2完]

# \$4.2 李 导数

$\ S 2 . 2$ 末讲过， $M$ 上的一个光滑矢量场 $\nu ^ { a }$ 给出一个单参微分同胚群 $\phi . ^ { \mathbb { \Phi } }$ 设$\pmb { T }$ .是 $M$ 上的光滑张量场，则 $\phi _ { t } ^ { * } T ^ { \cdot }$ ".也是同型光滑张量场，其中 $\phi _ { t }$ 是单参微分同胚群Φ的一个群元．这两个张量场在点pM的值之差T.…..!-T.…..是p点的张量，它与 $t$ 之商 $( \phi _ { t } ^ { * } T _ { \cdot \cdot \cdot } ^ { \cdot \cdot } | _ { p } - T _ { \cdot \cdot } ^ { \cdot \cdot } | _ { p } ) / t$ 在 $t$ 趋于零时的极限可看作张量场T.... $p$ 点的某种导数，于是有以下定义：

定义1 $\mathcal { L } _ { \boldsymbol { v } } T ^ { a _ { 1 } \cdots a _ { k } } { } _ { b _ { 1 } \cdots b _ { l } } : = \operatorname* { l i m } _ { t  0 } \frac { 1 } { t } ( \phi _ { t } ^ { * } T ^ { a _ { 1 } \cdots a _ { k } } { } _ { b _ { 1 } \cdots b _ { l } } - T ^ { a _ { 1 } \cdots a _ { k } } { } _ { b _ { 1 } \cdots b _ { l } } )$

称为张量场 $T ^ { a _ { 1 } \cdots a _ { k } } { } _ { b _ { 1 } \cdots b _ { l } }$ 沿矢量场 $\nu ^ { a }$ 的李导数(Lie derivaive) $\mathcal { L } _ { \nu }$ 中的 $\pmb { \nu }$ 不写为 $\nu ^ { a }$ ，以免误解.).

注1因 $\phi _ { t } ^ { * }$ 为线性映射，故李导数是由 $\mathcal { F } _ { M } ( k , l )$ 到 $\mathcal { F } _ { M } ( k , l )$ 的线性映射．由式(4-2-1)及定理4-1-7还知 $\mathcal { L } _ { \nu }$ 同缩并可交换顺序.

定理4-2-1 $\mathcal { L } _ { \upsilon } f = \upsilon ( f ) , \quad \cdot \quad \forall f \in \mathcal { F } .$

证明 $\forall p \in M$ ，设 $C ( t )$ 是 $\phi$ 过 $p$ 点的轨道， $p = C ( 0 )$ ，则 $\phi _ { t } ( p ) { = } C ( t )$ 且 $\nu ^ { a } \mid _ { p }$ $\equiv ( \widehat { \partial } / \widehat { \partial } t ) ^ { a } \mid _ { p }$ 是 $C ( t )$ 在 $p$ 点的切矢(图4-2)，故

$$
\begin{array} { l } { \displaystyle \mathcal { L } _ { \upsilon } f \vert _ { p } = \displaystyle \operatorname* { l i m } _ { t  0 } - ( \phi _ { t } ^ { * } f - f ) \vert _ { p } = \displaystyle \operatorname* { l i m } _ { t  0 } - [ f ( \phi _ { t } ( p ) ) - f ( p ) ] } \\ { \displaystyle \quad = \operatorname* { l i m } _ { t  0 } - [ f ( C ( t ) ) - f ( C ( 0 ) ) ] = \frac { \mathbf { d } } { \mathbf { d } t } ( f \circ C ) \vert _ { t = 0 } = \upsilon ( f ) \vert _ { p } . } \end{array}
$$

![](images/5189335cab77b38e29de6c03df275ecce0ee7dde6c1f6bba03996f623fb1a326.jpg)  
图4-2定理4-2-1证明用图

下面以 $n = 2$ 为例介绍一种对计算李导数很有用的坐标系．设 $\{ x ^ { 1 } , x ^ { 2 } \}$ 为坐标系，则 $x ^ { 1 }$ 坐标线和 $x ^ { 2 }$ 坐标线组成坐标“网格”，欲知坐标域中某点的坐标，只须看它位于网格的哪两条坐标线的交点．求李导数时总要给定矢量场 $\nu ^ { a }$ ，可以选定它的积分曲线为 $x ^ { 1 }$ 坐标线 $( t$ 充当 $x ^ { 1 }$ ),再相当任意地选定另一组与这组曲线横截(即交点上两线切矢不平行)的曲线作为 $x ^ { 2 }$ 坐标线，这样得到的坐标系称为矢量场 $\nu ^ { a }$ 的适配坐标系①(adapted coordinate system)．换句话说，矢量场 $\nu ^ { a }$ 就是其适配坐标系的第一坐标基矢场，即 $\boldsymbol { \nu } ^ { a } = ( \partial / \partial x ^ { 1 } ) ^ { a }$ ．以上讨论可推广至任意维流形.

定理4-2-2 张量场 $T ^ { a _ { 1 } \cdots a _ { k } } { } _ { b _ { 1 } \cdots b _ { l } }$ bb沿u"的李导数在v的适配坐标系的分量

$$
( \mathcal { L } _ { v } T ) ^ { \mu _ { 1 } \cdots \mu _ { k } } { } _ { \nu _ { 1 } \cdots \nu _ { l } } = \frac { \widehat { \partial } T ^ { \mu _ { 1 } \cdots \mu _ { k } } { } _ { \nu _ { 1 } \cdots \nu _ { l } } } { \widehat { \partial } x ^ { 1 } } .
$$

注2上式左边在坐标变换时满足张量变换律而右边则否，故不能改写为张 量等式.

证明仅以 $\pmb { n = 2 }$ ， $k = l = 1$ 为例(容易推广至一般情况).因 ${ \phi _ { t } ^ { * } } = ( { \phi _ { t } ^ { - 1 } } ) _ { * } = \phi _ { - t * }$ ，式(4-2-1)在任一坐标系(现在取适配坐标系)的分量式为

$$
( \mathcal { L } _ { v } T ) ^ { \mu } { } _ { \nu } ! _ { p } = \operatorname * { l i m } _ { t  0 } \frac { 1 } { t } [ ( \phi _ { - t } { \mathcal { T } } ) ^ { \mu } { } _ { \nu } ! _ { p } - T ^ { \mu } { } _ { \nu } ! _ { p } ] \qquad \forall p \in M .
$$

令 $q \equiv \phi _ { t } ( p )$ ，因式(4-2-4)只涉及 $p$ 点附近的情况，总可认为 $p , \ q$ 点都在同一适配坐标域内．对 $\phi _ { - t }$ 而言， $q$ 为老点， $p$ 为新点，故由式(4-1-6)得

$$
( \phi _ { - t ^ { * } } T ) ^ { \mu } { } _ { \nu } \Big | _ { p } = T ^ { \prime \mu } { } _ { \nu } \Big | _ { q } = \left[ { \frac { \partial x ^ { \prime \mu } } { \partial x ^ { \rho } } } { \frac { \partial x ^ { \sigma } } { \partial x ^ { \prime \nu } } } T ^ { \rho } { } _ { \sigma } \right] _ { q } ,
$$

式中 $x ^ { \sigma }$ 为适配(老)坐标， $x ^ { \prime \mu }$ 是由 $\phi _ { - t }$ 诱导的新坐标．上式右边涉及新老坐标间的偏导数在 $q$ 点的值,要计算就须找出 $q$ 点的一个小邻域 $N$ 内的坐标变换. $\forall \overline { { q } } \in N$ ，记 $\overline { { { p } } } \equiv \phi _ { - t } ( \overline { { { q } } } )$ ，由适配坐标的定义知 $x ^ { 1 } ( \overline { { q } } ) = x ^ { 1 } ( \overline { { p } } ) + \ t .$ $x ^ { 2 } ( { \overline { { q } } } ) = x ^ { 2 } ( { \overline { { p } } } )$ ，而按定义,$\phi _ { - t }$ 在 $\overline { { \pmb q } }$ 诱导的新坐标则为 ${ x ^ { \prime } } ^ { 1 } ( { \overline { { q } } } ) \equiv { x ^ { 1 } } ( { \overline { { p } } } )$ ， $x ^ { \prime 2 } ( { \overline { { q } } } ) \equiv x ^ { 2 } ( { \overline { { p } } } )$ ，故 $x ^ { \prime 1 } ( \overline { { q } } ) = x ^ { 1 } ( \overline { { q } } ) - t$ ，$x ^ { \prime 2 } ( \overline { { q } } ) = x ^ { 2 } ( \overline { { q } } )$ .因 $\overline { { q } }$ 为 $N$ 内任一点，故对 $N$ 有 ${ \boldsymbol { x } } ^ { \prime 1 } = { \boldsymbol { x } } ^ { 1 } - t$ ， ${ x ^ { \prime } } ^ { 2 } = { x ^ { 2 } }$ ，求导得$( \widehat { \partial } x ^ { \prime \mu } / \widehat { \partial } x ^ { \rho } ) \vert _ { q } = \delta ^ { \mu } { } _ { \rho }$ ， $( \widehat { \partial } x ^ { \sigma } / \widehat { \partial } x ^ { \prime \nu } ) \vert _ { q } = \delta ^ { \sigma } { } _ { \nu }$ ，于是式(4-2-5)成为 $( \phi _ { - t ^ { * } } T ) _ { \nu } ^ { \mu } \mid _ { p } = T _ { \nu } ^ { \mu } \mid _ { q }$ ，代人式(4-2-4)便得 $( \mathcal { L } _ { v } T ) _ { \nu } ^ { \mu } | _ { p } = \partial T _ { \nu } ^ { \mu } / \partial x ^ { 1 } | _ { p }$ □

由定理4-2-2可知 $\mathcal { L } _ { \nu }$ 满足莱布尼茨律.

定理4-2-3 $\mathcal { L } _ { \nu } u ^ { a } = \left[ \nu , u \right] ^ { a } , \qquad \forall u ^ { a } , \nu ^ { a } \in \mathcal { F } ( 1 , 0 ) ,$ 或者，借助于对易子的表达式(3-1-13)，有

$$
\mathcal { L } _ { \nu } u ^ { a } = \nu ^ { b } \nabla _ { b } u ^ { a } - u ^ { b } \nabla _ { b } \nu ^ { a } ,
$$

其中 $\nabla _ { a }$ 为任一无挠导数算符.

证明待证命题是矢量等式，只须证明它在某一坐标系的分量等式$( \mathcal { L } _ { v } u ) ^ { \mu } = [ v , u ] ^ { \mu }$ 成立．最方便的当然是适配坐标系．设 $\nu ^ { a }$ 的适配坐标系 $\{ x ^ { \mu } \}$ 的普通导数算符是 $\widehat { \sf { d } } _ { a }$ ，则

$$
\begin{array} { c } { { { } [ \nu , u ] ^ { \mu } = ( \mathrm { d } x ^ { \mu } ) _ { a } [ \nu , u ] ^ { a } = ( \mathrm { d } x ^ { \mu } ) _ { a } ( \nu ^ { b } \hat { \mathcal { O } } _ { b } u ^ { a } - u ^ { b } \hat { \mathcal { O } } _ { b } \nu ^ { a } ) = \nu ^ { b } \hat { \mathcal { O } } _ { b } u ^ { \mu } } } \\ { { { } } } \\ { { { } [ \nu , u ] ^ { \mu } = \nu ( u ^ { \mu } ) = \hat { \mathcal { O } } u ^ { \mu } / \hat { \mathcal { O } } x ^ { 1 } = ( \mathcal { L } _ { \nu } u ) ^ { \mu } , } } \end{array}
$$

其中第三步是因为 $\boldsymbol { \nu } ^ { a } = ( \widehat { o } / \widehat { o } x ^ { 1 } ) ^ { a }$ 导致 $\widehat { \cal O } _ { b } v ^ { a } = 0$ ，第四步用到导数算符定义的条件(d)，最后一步用到式(4-2-3). □

$$
\mathcal { L } _ { \nu } \omega _ { a } = \nu ^ { b } \nabla _ { b } \omega _ { a } + \omega _ { b } \nabla _ { a } \upsilon ^ { b } , \qquad \forall \upsilon ^ { a } \in \mathcal { F } ( 1 , 0 ) , \omega _ { a } \in \mathcal { F } ( 0 , 1 ) ,
$$

其中 $\nabla _ { a }$ 为任一无挠导数算符.

证明习题．提示：用定理4-2-3及4-2-1，后者给出 $\mathcal { L } _ { \nu } ( \omega _ { a } u ^ { a } ) = \nu ^ { b } \nabla _ { b } ( \omega _ { a } u ^ { a } )$

# 定理4-2-5

$$
\mathcal { L } _ { v } T ^ { a _ { 1 } \cdots a _ { k } } { } _ { b _ { 1 } \cdots b _ { l } } = v ^ { c } \nabla _ { c } T ^ { a _ { 1 } \cdots a _ { k } } { } _ { b _ { 1 } \cdots b _ { l } } - \sum _ { i = 1 } ^ { k } T ^ { a _ { 1 } \cdots c \cdots a _ { k } } { } _ { b _ { 1 } \cdots b _ { l } } \nabla _ { c } v ^ { a _ { i } } + \sum _ { j = 1 } ^ { l } T ^ { a _ { 1 } \cdots a _ { k } } { } _ { b _ { 1 } \cdots c \cdots b _ { l } } \nabla _ { b _ { j } } v ^ { a _ { j } } .
$$

$\forall T \in \mathcal { F } ( k , l ) , ~ \nu \in \mathcal { F } ( 1 , 0 ) , ~ \nabla _ { a }$ 为任一导数算符.

证明 练习.

# \$4.3 Killing矢量场

本章至此未涉及度规及与之适配的导数算符，李导数的定义不要求流形 $M$ 有附加结构．但若 $M$ 上选定了度规场 $g _ { a b }$ ，则对微分同胚映射 $\phi : M \to M$ 还可提出更高的要求，即 $\phi ^ { * } g _ { a b } = g _ { a b }$ .于是有如下定义：

定义1微分同胚 $\phi \colon M \to M$ 称为等度规映射，简称等度规(isometry)，若$\phi ^ { * } g _ { a b } = g _ { a b } .$

注1 $\textcircled{1}$ 等度规映射是特殊的微分同胚映射，其特殊性在于“保度规”性，即 $\phi ^ { * } g _ { a b } = g _ { a b }$ .注意这是张量场的等式，其含义是每点 $p$ 的两个张量 $g _ { a b } \mid _ { p }$ 和$\phi ^ { * } g _ { a b } \mid _ { p }$ 相等. $\textcircled{2}$ 由 $\phi ^ { - 1 * } \circ \phi ^ { * } = ( \phi \circ \phi ^ { - 1 } ) ^ { * } =$ 恒等映射[见习题5(c)]易见 $\phi : M \to M$ 为等度规映射当且仅当 $\phi ^ { - 1 } : M \to M$ 为等度规映射.

流形 $M$ 上众多矢量场中有一类特殊矢量场，即光滑矢量场．每一光滑矢量场给出一个单参微分同胚群① 如果 $M$ 上指定了度规场 $g _ { a b }$ ，则众多光滑矢量场中还可挑出特殊的一个子类,其中每个矢量场给出的单参微分同胚群是单参等度规群，即每个群元 $\phi _ { t } : M \to M$ 是 $M$ 上的一个等度规映射．于是有以下定义：

定义2 $( M , \ g _ { a b } )$ 上的矢量场 $\xi ^ { a }$ 称为Killing矢量场，若它给出的单参微分同胚(局部)群是单参等度规(局部)群．等价地(有余力的读者可自证)，称为Killing矢量场，若 $\mathcal { L } _ { \xi } g _ { a b } = 0$ ·

定理 4-3-1 $\xi ^ { a }$ 为 Killing 矢量场的充要条件是 $\xi ^ { a }$ 满足如下的Killing方程：

$$
\nabla _ { a } \xi _ { b } + \nabla _ { b } \xi _ { a } = 0
$$

(其中 $\nabla _ { a }$ 满足 $\nabla _ { a } g _ { b c } = 0 $ ）

证明 $0 = \mathcal { L } _ { \xi } g _ { a b } = \xi ^ { c } \nabla _ { c } g _ { a b } + g _ { c b } \nabla _ { a } \xi ^ { c } + g _ { a c } \nabla _ { b } \xi ^ { c } = \nabla _ { a } \xi _ { b } + \nabla _ { b } \xi _ { a } ,$ 其中第二步用到式(4-2-8).

定理 4-3-2 若存在坐标系 $\{ x ^ { \mu } \}$ 使 $g _ { a b }$ 的全部分量满足 $\partial g _ { \mu \nu } / \partial x ^ { 1 } = 0$ ，则$( \partial / \partial x ^ { 1 } ) ^ { a }$ 是坐标域上的 Killing 矢量场.

证明{x}是(@/axl)²的适配坐标系，由式(4-2-3)得(a/ax¹g)μ=$\widehat { \partial } g _ { \mu \nu } / \widehat { \partial } x ^ { 1 } = 0$ ，故 $\mathcal { L } _ { \partial / \partial x ^ { 1 } } g _ { a b } = 0$ ，即 $( \partial / \partial x ^ { 1 } ) ^ { a }$ 为 Killing 矢量场. □

定理4-3-3设 $\xi ^ { a }$ 为 Killing 矢量场, $T ^ { a }$ 为测地线的切矢,则 $T ^ { a } \nabla _ { a } ( T ^ { b } \xi _ { b } ) = 0$ ，即 $T ^ { b } \xi _ { b }$ 在测地线上为常数.

证明 $T ^ { a } \nabla _ { a } ( T ^ { b } \xi _ { b } ) = \xi _ { b } T ^ { a } \nabla _ { a } T ^ { b } + T ^ { b } T ^ { a } \nabla _ { a } \xi _ { b } = T ^ { b } T ^ { a } \nabla _ { a } \xi _ { b } = 0$ ，其中第二步用到测地线定义，第三步用到定理4-3-1(即 $\nabla _ { a } \xi _ { b } = \nabla _ { [ a } \xi _ { b ] } ,$ 及定理2-6-2(d). □

设 $\xi ^ { a }$ ， $\eta ^ { a }$ 是 Killing 矢量场， $\pmb { \alpha }$ ， $\beta$ 是常实数，则由 Killing 方程的线性性知$\alpha \xi ^ { a } + \beta \eta ^ { a }$ 也是 Killing 矢量场．不难看出 $M$ 上所有 Killing 矢量场的集合是个矢量空间．还可证明(习题)对易子 $[ \xi , \eta ] ^ { a }$ 也是 Killing 矢量场.

定理 4-3-4 $( M , g _ { a b } )$ 上最多有 $n ( n { + } 1 ) / 2$ 个独立的 Killing 矢量场 $\left( n \equiv \mathbf { d i m } M \right)$ ，即 $M$ 上所有 Killing 矢量场的集合(作为矢量空间)的维数小于等于 $n ( n { + } 1 ) / 2$

证明 见Wald(1984)P.442\~443.

注2 $\textcircled{1}$ 等度规映射可看作一种“保度规”的对称变换，所以一个Killing 矢量场代表 $( M , \ g _ { a b } )$ 的一个对称性，具有 $n \left( n { + } 1 \right) / 2$ 个独立Killing矢量场的广义黎曼空间 $( M , \ g _ { a b } )$ 称为最高对称性空间。 $\textcircled{2}$ 寻找 $( M , \ g _ { a b } )$ 的全体 Killing 矢量场的一般方法是求Killing方程的通解．然而对某些简单的 $( M , g _ { a b } )$ 还存在容易得多的方法．下面仅举数例.

例1找出下列广义黎曼空间的全体独立的 Killing 矢量场.

(1）2维欧氏空间 $( \mathbb { R } ^ { 2 } , \delta _ { a b } )$ .设 $\{ x , ~ y \}$ 为笛卡儿坐标系，则 $ { \mathrm { d } } s ^ { 2 } =  { \mathrm { d } } x ^ { 2 } +  { \mathrm { d } } y ^ { 2 }$ ，即欧氏度规 $\delta _ { a b }$ 在此系中的全部分量为常数，故由定理4-3-2 知 ${ ( \partial / \partial x ) } ^ { a }$ 和 $( { \hat { o } } / { \hat { o } } y ) ^ { a }$ 为Killing 矢量场．我们相信欧氏空间有最高对称性，由定理4-3-4可知 $\pmb { n = 2 }$ 时应有3个独立的 Killing场．果然，若改用极坐标系，便有 $\mathrm { d } s ^ { 2 } = \mathrm { d } r ^ { 2 } + r ^ { 2 } \mathrm { d } \varphi ^ { 2 }$ ，可见欧氏度规 $\delta _ { a b }$ 在此系中的全部分量与 $\varphi$ 无关，所以由定理4-3-2可知 $\left( \partial / \partial \varphi \right) ^ { a }$ 为Killing矢量场，它在笛卡儿系的坐标基底的展开式为 $( \hat { \partial } / \hat { \partial } \varphi ) ^ { a } = - y ( \hat { \partial } / \hat { \partial } x ) ^ { a } + x ( \hat { \partial } / \hat { \partial } y ) ^ { a }$ 展开系数与坐标有关，由此不难证明 $\left( \partial / \partial \varphi \right) ^ { a }$ 独立于前两个Killing 场. ${ ( \partial / \partial x ) } ^ { a }$ 和$( \partial / \partial y ) ^ { a }$ 的 Killing性反映2维欧氏度规沿 $x$ 和 $y$ 轴的平移不变性, $( \partial / \partial \varphi ) ^ { a }$ 的 Killing性表明它有旋转不变性.

(2)3维欧氏空间 $( \mathbb { R } ^ { 3 } , \delta _ { a b } )$ .因为 $n = 3$ ,故有6个独立 Killing场，即 $( { \partial } / { \partial } x ) ^ { a }$ ，$( \widehat { \partial } / \widehat { \partial } y ) ^ { a } \ , ( \widehat { \partial } / \widehat { \partial } z ) ^ { a } \ , - y \ ( \widehat { \partial } / \widehat { \partial } x ) ^ { a } + x \ ( \widehat { \partial } / \widehat { \partial } y ) ^ { a } \ , - z \ ( \widehat { \partial } / \widehat { \partial } y ) ^ { a } \ + y \ ( \widehat { \partial } / \widehat { \partial } z ) ^ { a } \ \geq \ 0$ 和 $- x ( \partial / \partial z ) ^ { a }$ $+ z ( \partial / \partial x ) ^ { a }$ .前3.个反映3维欧氏度规沿 $x \ , \ y \ , \ z$ 轴的平移不变性；后3个反映它绕 $z \ , \ x \ , \ y$ 轴的旋转不变性.

(3)2维闵氏空间 $( \mathbb { R } ^ { 2 } , \eta _ { a b } )$ .在洛伦兹坐标系 $\left\{ t , x \right\}$ 中有 $\mathrm { d } s ^ { 2 } = - \mathrm { d } t ^ { 2 } + \mathrm { d } x ^ { 2 }$ ，故知${ ( \partial / \partial t ) } ^ { a }$ 和 $( { \partial } / { \partial } x ) ^ { a }$ 为 Killing场．为求第3个，用下式定义新坐标 $\psi , \eta$ ：

$$
x = \psi \mathrm { c h } \eta , \qquad t = \psi \mathrm { s h } \eta , \qquad 0 < \psi < \infty , \qquad - \infty < \eta < \infty ,
$$

闵氏线元可用新坐标表为 $ { \mathbf { d } } s ^ { 2 } =  { \mathbf { d } } \psi ^ { 2 } - \psi ^ { 2 }  { \mathbf { d } } \eta ^ { 2 }$ .上式表明 $\eta _ { a b }$ 在新坐标系的全体分量与坐标 $\eta$ 无关，故 ${ ( \partial / \partial \eta ) } ^ { a }$ 也是Killing 矢量场(其积分曲线是双曲线)，它在洛伦兹坐标基底的展开式为

$$
( \hat { \partial } / \hat { \partial } \eta ) ^ { a } = t \left( \hat { \partial } / \hat { \partial } x \right) ^ { a } + x \left( \hat { \partial } / \hat { \partial } t \right) ^ { a } ,
$$

由展开系数与坐标有关可知 $( \partial / \partial \eta ) ^ { a }$ 与前两个 Killing 场独立．式(4-3-2)定义的 $\psi$ ，$\eta$ 的坐标域只是 $\mathbb { R } ^ { 2 }$ 的、由 $x > | t |$ 限定的一个开子集(见图4-3的A区).但式(4-3-3)

却在全 $\mathbb { R } ^ { 2 }$ 有定义，而且不难验证 $( \partial / \partial \eta ) ^ { a }$ 是 $\mathbb { R } ^ { 2 }$ 上的Killing矢量场，它在图 4-3的A,B区类时，在C,D区类空，在两条 $4 5 ^ { \circ }$ 斜直线上类光. $t ~ ( \widehat { { \cal O } } / \widehat { \partial } x ) ^ { a } ~ + x ~ ( \widehat { { \cal O } } / \widehat { \partial } t ) ^ { a }$ 叫做伪转动(boost)Killing矢量场，表明闵氏度规具有伪转动下的不变性，对应于洛伦兹变换(详见定理4-3-5).

![](images/cf24d87ac449cb606ca17fea94224ed536156b3275a93793c2a9c2725b15b390.jpg)  
图4-3伪转动Killing矢量场 $( \partial / \partial \eta ) ^ { a }$ 在 $\mathbf { A }$ ， $\mathbf { B }$ 区类时，在C， $\mathbf { D }$ 区类空，在两条 $4 5 ^ { \circ }$ 直线上类光

(4）4维闵氏空间 $( \mathbb { R } ^ { 4 } , \eta _ { a b } )$ .因 $n = 4$ ，故独立的Killing 场共10个，分三组：

(a)4个平移 $( \widehat { \partial } / \widehat { \partial } t ) ^ { a } \ , ( \widehat { \partial } / \widehat { \partial } x ) ^ { a } \ , ( \widehat { \partial } / \widehat { \partial } y ) ^ { a } \ , ( \widehat { \partial } / \widehat { \partial } z ) ^ { a } \ ;$

(b)3个空间转动

$$
- y ( \partial / \partial x ) ^ { a } + x ( \partial / \partial y ) ^ { a } , ~ - z ( \partial / \partial y ) ^ { a } + y ( \partial / \partial z ) ^ { a } , ~ - x ( \partial / \partial z ) ^ { a } + z ( \partial / \partial x ) ^ { a } \ ;
$$

(c)3个伪转动 $t \left( \widehat { { \sf { O } } } / \widehat { \partial } x \right) ^ { a } + x \left( \widehat { { \sf { O } } } / \widehat { \partial } t \right) ^ { a }$ ，t(@/ay)a+y(a/at)²，t(ə/az)a + $z \left( \partial / \partial t \right) ^ { a }$

组(a)反映闵氏度规沿 $t , \ x , \ y , \ z$ 轴的平移不变性，组(b)反映它绕 $z , \ x , \ y$ 轴的空间旋转不变性，组(c)反映它在 $t { \sim } x , t { \sim } y$ ， $\scriptstyle t \sim z$ 面内的伪转动下的不变性.

定理4-3-5设 $\{ x , t \}$ 是2维闵氏空间 $( \mathbb { R } ^ { 2 } , \eta _ { a b } )$ 的洛伦兹坐标系， $\phi _ { \lambda } : \mathbb { R } ^ { 2 } \to \mathbb { R } ^ { 2 }$ 是伪转动Killing 场 $\xi ^ { a } \equiv t ( \partial / \partial x ) ^ { a } + x ( \partial / \partial t ) ^ { a }$ 对应的单参等度规群的一个群元(即以参数 $\lambda \in \mathbb { R }$ 刻画的那个等度规映射)，则由 $\phi _ { \lambda }$ 诱导的坐标变换 $\{ x , t \} \mapsto \{ x ^ { \prime } , t ^ { \prime } \}$ 是洛伦兹变换.

注3本定理表明伪转动和洛伦兹变换是同一变换的两种(主动与被动)提法．类似地，欧氏空间的转动Killing 场 $- y ( \partial / \partial x ) ^ { a } + x ( \partial / \partial y ) ^ { a }$ 与坐标变换

$$
x ^ { \prime } = x \cos \alpha - y \sin \alpha \ , y ^ { \prime } = x \sin \alpha + y \cos \alpha
$$

也是同一变换的两种提法.

证明矢量场 $\xi ^ { a } \equiv ( \partial / \partial \eta ) ^ { a }$ 的积分曲线的参数方程为 $\mathrm { d } x ^ { \mu } ( \eta ) / \mathrm { d } \eta = \xi ^ { \mu }$ $( \mu = 0 , 1 )$ ．注意到 $\xi ^ { a } \equiv t ( \hat { \left. \partial \right)} / \hat { \partial } x  ^ { a } + x ( \hat { \left. \partial \right)} / \hat { \partial } t  ^ { a }$ ，便得

$$
\frac { \mathrm { d } x ( \eta ) } { \mathrm { d } \eta } { = } t ( \eta ) , \qquad \frac { \mathrm { d } t ( \eta ) } { \mathrm { d } \eta } { = } x ( \eta ) .
$$

∀p∈R²，设C(n)是满足p=C(O)的积分曲线，即x(O)=xp，t(O)=tp，则不难证明 方程(4-3-4)的特解[即该线的参数式]为

$$
x ( \eta ) = x _ { p } \mathrm { c h } \eta + t _ { p } \mathrm { s h } \eta , \qquad t ( \eta ) = x _ { p } \mathrm { s h } \eta + t _ { p } \mathrm { c h } \eta .
$$

设q=𝜙(p)，则q就是C(n)上参数值η=的点，即q=C(λ)，故由𝜙诱导的新坐标 $t ^ { \prime }$ 和 $x ^ { \prime }$ 满足

$$
x _ { p } ^ { \prime } \equiv x _ { q } = x _ { p } \mathrm { c h } \lambda + t _ { p } \mathrm { s h } \lambda \ , \qquad t _ { p } ^ { \prime } \equiv t _ { q } = x _ { p } \mathrm { s h } \lambda + t _ { p } \mathrm { c h } \lambda \ .
$$

因 $p$ 点任意，故可去掉下标 $p$ 而写成

x'= xchλ+tsh𝑙=ch𝜆(x+t thl)，t'=tchλ+xsh𝑙=ch𝜆(t+x thλ).令 $\pmb { V } \equiv$ th $\lambda$ ， $\gamma \equiv ( 1 - \nu ^ { 2 } ) ^ { - 1 / 2 } = \operatorname { c h } \lambda$ ，则

$$
x ^ { \prime } = \gamma ( x + \nu t ) , \qquad t ^ { \prime } = \gamma ( t + \nu x ) .
$$

这便是熟知的洛伦兹变换(注意，我们用几何单位制，其中光速c=1.).

# [选读4-3-1]

上述证明中的C(n)对R²的任一点p都是完备曲线,即η∈(-∞,∞).若p在A或B区，则C(n)类时；若p在C或D区，则C(n)类空；若p在45°斜直线上,则C(n)类光.最特别的情况是p=(0,O)，即p为{t,x}系的原点,这时C(n)=p(独点线)．所以每条45斜直线不是一条积分曲线而是3条积分曲线之并，第一、二条分别是斜直线的上、下半段(不含原点)，第三条则是独点线{p}.这3条线的参数范围都是（-8,00). [选读4-3-1完]

由ds²=-dt²+dx²和式(4-3-7)易得ds²=-dt²+dx²，可见伪转动对应的等度规映射诱导的坐标变换把洛伦兹系{t,x}变为洛伦兹系{t',x'}．此结果可推广为如下定理：

定理4-3-6设{x"}是(R",nab)的洛伦兹坐标系，则{x"}也是洛伦兹坐标系 的充要条件是它由{x"}通过等度规映射：R"→R"诱导而得.

证明把nab记作gab，其在{x"}和{x'"}系的分量分别记作gμv和g'v·

（A)设 $\phi \colon { \mathbb { R } } ^ { n } \to { \mathbb { R } } ^ { n }$ 是等度规映射(即 $\phi ^ { * } g _ { a b } = g _ { a b } )$ ， $\{ x ^ { \prime \mu } \}$ 是由洛伦兹系 $\{ x ^ { \mu } \}$ 通过诱导而得的坐标系，则∀p∈R"有gμvlp=(Φg)μv\(p)=(-1\*g)μv\(p)$= g _ { \mu \nu } \mid _ { \phi ( p ) } = \eta _ { \mu \nu }$ ，其中第一步用到式(4-1-6)，第三步是由于 $\phi$ 为等度规导致 $\phi ^ { - 1 }$ 为等度规,第四步用到{x"}的洛伦兹性.上式说明p点的gab在{x"}系的分量为ημv，故 $\{ x ^ { \prime \mu } \}$ 为洛伦兹系.

(B）设 $\{ x ^ { \mu } \}$ 和 $\{ x ^ { \prime \mu } \}$ 都是洛伦兹系， $\phi \colon { \mathbb { R } } ^ { n } \to { \mathbb { R } } ^ { n }$ 是与坐标变换 $\{ x ^ { \mu } \} \mapsto \{ x ^ { \prime \mu } \}$ 对应的微分同胚映射，则 $\forall p \in \mathbb { R } ^ { n }$ 有 $( \phi ^ { - 1 \ast } g ) _ { \mu \nu } \mid _ { p } = ( \phi _ { \ast } g ) _ { \mu \nu } \mid _ { p } = g _ { \mu \nu } ^ { \prime } \mid _ { _ { \phi ^ { - 1 } ( p ) } } = \eta _ { \mu \nu } = g _ { \mu \nu } \mid _ { p } ,$ 其中第二步用到式(4-1-6)，第三、四步用到 $\{ x ^ { \prime } \}$ 和 $\{ x ^ { \mu } \}$ 的洛伦兹性．上式表明$\phi ^ { - 1 * } g _ { a b } = g _ { a b }$ ，故 $\phi ^ { - 1 }$ （因而 $\phi$ )是等度规映射. □

注4本定理也适用于欧氏空间，只须把洛伦兹系改为笛卡儿系．可以说等度规映射保持坐标系的洛伦兹(笛卡儿)性.

# \$4.4 超 曲 面

定义1设 $M$ ， $s$ 为流形, $\mathrm { d i m } S \leqslant \mathrm { d i m } M \equiv n$ .映射 $\phi : S  M$ 称为嵌入(imbed-ding)，若 $\phi$ 是一一和 $\mathbf { C } ^ { \infty }$ 的，而且 $\forall p \in S$ ，推前映射 $\phi _ { * } : V _ { p } \to V _ { \phi ( p ) }$ 非退化[ $V _ { \phi ( p ) }$ 是指 $\phi ( p )$ 作为 $M$ 的一点的切空间]，即 $\phi _ { * } \nu ^ { a } = 0 \Rightarrow \nu ^ { a } = 0$ .

注1嵌入的上述条件使 $s$ 的拓扑和流形结构可自然地被带到 $\phi [ S ]$ 上去，从而使 $\phi : S  \phi [ S ]$ 成为微分同胚映射.

定义2 嵌入 $\phi : S  M$ 称为 $M$ 的一个嵌入子流形(imbedded submanifold),简称子流形．也常把映射的像 $\phi [ S ]$ 称为嵌入子流形．若 $\dim S = n - 1$ ，则 $\phi [ S ] \subset M$ 称为 $M$ 的一张超曲面(hypersurface).

例1设 $U$ 是 $M$ 的开子集，把 $M$ 的流形结构限制在 $U$ 上， $U$ 便成为与 $M$ 同维的流形．把 $U$ 看作定义1的 $s$ ，令 $\phi : U \to M$ 为恒等映射，则 $U \equiv \phi \left[ U \right]$ 便是 $M$ 的一个嵌入子流形(同维嵌入).

例2设 $s$ 是 ${ \mathbb { R } } ^ { 3 }$ (看作 $M )$ 中的单位球面 ${ \mathsf S } ^ { 2 }$ ,则恒等映射 $\phi : \mathbb { S } ^ { 2 } \to \mathbb { R } ^ { 3 }$ 给出 ${ \mathbb { R } } ^ { 3 }$ 的一个嵌入子流形．注意到 ${ \mathsf S } ^ { 2 } \mathsf { t } \mathsf { t } \mathbb { R } ^ { 3 }$ 低一维，可知 ${ \mathsf S } ^ { 2 }$ 是 ${ \mathbb { R } } ^ { 3 }$ 的一个超曲面.

# [选读4-4-1]

嵌入子流形S]有两个拓扑，其一是由嵌入自然带来的拓扑(见注1)，其二是由 $M$ 的拓扑在 $\phi [ S ]$ （作为 $M$ 的子集)上诱导的拓扑．这两个拓扑不一定相同．如果进一步要求它们相同，就对嵌入 $\phi : S  M$ 提出了更高的要求．满足这一附加要求的嵌入称为正则嵌入[见陈省身，陈维桓(1983).]．Hawking and Ellis(1973)的嵌入指的就是正则嵌入．设 ${ \pmb S } = { \mathbb R }$ ， $M = \mathbb { R } ^ { 2 }$ ，则嵌入 $\phi : S  M$ 是 $\mathbb { R } ^ { 2 }$ 中的光滑曲线．定义中 $\phi$ 的一一性不允许嵌入子流形为自相交曲线(例如图4-4的8字形曲线)．图4-5的“任意接近自相交”而不自相交的曲线是不是嵌入子流形？答案是：它是嵌入子流形但不是正则嵌入子流形．本书今后谈到嵌入子流形时，在许多情况下是指正则嵌入子流形.

![](images/e4e0de17e8e9fe3c3244416b6622a294f230ff16cc674c5c4b323b4a9bded455.jpg)  
图4-4 自相交曲线不是嵌入子流形

![](images/da6739cc95aa8f7b795f1f4b7a1620c0520e3e5f4a713a90d3312da733dd21d7.jpg)  
图4-5 “任意接近自相交”的曲线是嵌入子流形，但不是正则嵌入子流形

设S]是M的超曲面，q∈[S]cM．作为M的一点，q有n维切空间Vq.若w∈Vq是过q且躺在[S]上的某曲线的切矢(“躺在”是指曲线每点都在[S]上)，则说w切于S].V中全体切于[S]的元素构成的子集记作Wq.超曲面的定义保证Wa是Va的n-1维子空间．谈到超曲面时自然想到它的法矢．设[S]是超曲面，q∈S]，则q点的法矢n应定义为与q点所有切于S]的矢量正交的矢量．然而正交性只有在指定度规后才有意义．当M没有度规时，不能定义法矢n"，但可定义“法余矢”na.余矢(covector)是对偶矢量的别名．由于对偶矢量作用于矢量给出实数(无需度规)，可定义法余矢如下：

定义3设[S]是超曲面，q∈[S]．非零对偶矢量nα∈V\*称为[S]在q点 的法余矢(normal covector)，若nqwa =0，∀w² ∈Wa.

定理4-4-1 超曲面S]上任一点q必有法余矢na．法余矢不唯一，但q点的任意两个法余矢之间只能差一实数因子.

证明设{(e)a,…,(en)²}为Wa任一基底,因dimVa=n,V必有与{(e2)°,,(en)²}线性无关的元素，任取其一并记作(e)°，则{(eμ)°Iμ=1,,n}为Va的基底，其对偶基底记作{(e")a}.令na=(e¹)a，则na(ez)α=δ¹,=0(τ=2,,n)，故$n _ { a } w ^ { a } = 0 \forall w ^ { a } \in W _ { q }$ ，可见 $n _ { a }$ 为法余矢.若存在 $m _ { a }$ 满足 $m _ { a } ( e _ { \tau } ) ^ { a } = 0 ~ ( \tau = 2 , \cdots , n )$ ，则其在对偶基底{(e")a}的分量m=ma(ez)α=0(τ=2,…,n)，因而ma=m(e¹)a$= m _ { 1 } n _ { a }$ ，即 $m _ { a }$ 与 $n _ { a }$ 只差一因子 $m _ { 1 }$ □

注2非超曲面的嵌入子流形(如3维流形中的曲线)的法余矢没有这样好的唯一性.

[选读 4-4-2]

设 $x , \ y , \ z$ 是 ${ \mathbb { R } } ^ { 3 }$ 的自然坐标，考虑函数 $f = a x + b y + c z ( a , \ b , \ c$ 为常数)，则${ \mathbb { R } } ^ { 3 }$ 中满足方程 $f = 0$ 的点便组成 ${ \mathbb { R } } ^ { 3 }$ 中的一个超曲面(平面)．若 $f = x ^ { 2 } + y ^ { 2 } + z ^ { 2 }$ $- a ^ { 2 }$ ，则方程 $f = 0$ 代表另一超曲面(球面)．然而，若 $f = x ^ { 2 } + y ^ { 2 } + z ^ { 2 }$ ，则只有坐标原点满足 $f = 0$ ，因此 $f { = } 0$ 不代表超曲面．关键在于这时df $\mid _ { f = 0 } = 0$ .另一个极端的例子是 $f : \mathbb { R } ^ { 3 }  \mathbb { R } ^ { 3 }$ 定义为 $f ( \boldsymbol { p } ) = 0 \forall \boldsymbol { p } \in \mathbb { R } ^ { 3 }$ 的情况.这时满足方程 $f = 0$ 的点的子集是 $\mathbb { R } ^ { 3 }$ 自身，所以也不是超曲面．关键仍然在于df $\mid _ { f = 0 } = 0$ .推广至 $f$ 是任意流形 $M$ 上光滑函数的情况，可以证明，只要d $\boldsymbol { f } \mid _ { f = c } \neq 0$ (即 $\nabla _ { a } f \mid _ { f = c } \neq 0 )$ ，则 $f = c$ （常数)给出 $M$ 中的一个超曲面[详见D.Chillingworth(1976)P.156\~158].

[选读4-4-2完]

定理4-4-2设 $\phi \left[ S \right]$ 是由 $f =$ 常数给出的超曲面,则面上的 $\nabla _ { a } f$ 是超曲面的法余矢.

证明只须对任一 $q \in \phi \left[ S \right]$ 证明 $w ^ { a } \nabla _ { a } f = 0 , \forall w ^ { a } \in W _ { q }$ .因 $w ^ { a }$ 总切于过 $q$ 并躺在 $\phi [ S ]$ 上的某曲线 $C ( t )$ ，故 $w ^ { a } \nabla _ { a } f = \frac { \partial } { \partial t } ( f ) = 0 \quad \forall w ^ { a } \in W _ { q }$ ，最后一步是因 $f$ 在 $C ( t )$ 上为常数.

若 $M$ 上有度规 $g _ { a b }$ ，则 $n ^ { a } \equiv g ^ { a b } n _ { b } \in V _ { q }$ 与 $\phi [ S ]$ 的所有矢量正交(因 $g _ { a b } n ^ { a } w ^ { b }$ $= n _ { b } w ^ { b } = 0 , \forall w ^ { b } \in W _ { q } )$ ，故 $n ^ { a }$ 叫超曲面 $\phi [ S ]$ 在 $q$ 点的法矢(normal vector)．若 $g _ { a b }$ 为正定度规(例如 $\mathbb { R } ^ { 2 }$ 嵌入3维欧氏空间)， $n ^ { a }$ 自然不属于 $W _ { q }$ ，即 $n ^ { a } \in V _ { q } - W _ { q }$ ；然而，若 $g _ { a b }$ 为洛伦兹度规， $n ^ { a }$ 却有可能属于 $W _ { q }$ .以下就 $g _ { a b }$ 为洛伦兹度规的情况进行讨论.

定理4-4-3 ${ n ^ { a } \in W _ { q } }$ 的充要条件为 $n ^ { a } n _ { a } = 0$

证明

(A)设 $n ^ { a } \in W _ { q }$ ，则 $n ^ { a }$ 可看作 ${ n _ { a } w } ^ { a } = 0$ 中的 $w ^ { a }$ ，故 $\displaystyle n _ { a } n ^ { a } = 0$ (B）由定理 4-4-1 的证明知对任一法余矢 $n _ { a }$ 存在基底 $\{ ( e _ { \mu } ) ^ { a } \}$ 使 $( e _ { 2 } ) ^ { a } , \cdots ,$ ${ ( e _ { n } ) } ^ { a } \in W _ { q }$ 且 $n _ { a } = ( e ^ { 1 } ) _ { a }$ ，故 $n ^ { a }$ 在该基底的第一分量 $n ^ { 1 } = n ^ { a } ( e ^ { 1 } ) _ { a } = n ^ { a } n _ { a }$ .因此$n _ { a } n ^ { a } = 0 \Longrightarrow n ^ { 1 } = 0 \Longrightarrow n ^ { a } = \sum _ { \tau = 2 } ^ { n } n ^ { \tau } ( e _ { \tau } ) ^ { a } \in W _ { q } .$

例3设 ${ \pmb S } = { \mathbb R }$ ， $M = \mathbb { R } ^ { 2 }$ ， $M$ 上度规 $g _ { a b } = \eta _ { a b }$ ， $\phi : \mathbb { R } \to \mathbb { R } ^ { 2 }$ 为嵌入，则 $\phi \left[ \mathbb { R } \right]$ 是2维闵氏时空中的超曲面．设 $t , \ x$ 为洛伦兹坐标，讨论以下三种有代表性的情况：

(1) $\phi [ \mathbb { R } ]$ 与 $x$ 轴平行(图 4-6a). $\forall q \in \phi [ \mathbb { R } ]$ ，令 ${ ( e _ { 2 } ) } ^ { a } = { ( \hat { o } / \hat { \partial } x ) } ^ { a }$ ，选

$$
( e _ { 1 } ) ^ { a } = \alpha \left( \widehat { \partial } / \widehat { \partial } t \right) ^ { a } + \beta \left( \widehat { \partial } / \widehat { \partial } x \right) ^ { a } , ( \alpha , \beta
$$

则不难验证 $( e ^ { 1 } ) _ { a } = \alpha ^ { - 1 } ( \mathbf { d } t ) _ { a }$ ，注意到定理4-4-1的证明过程，可知 $( e ^ { 1 } ) _ { a }$ 为法余矢 $n _ { a }$ ，

相应的法矢为 $n ^ { a } = \alpha ^ { - 1 } g ^ { a b } ( \mathrm { d } t ) _ { b } = - \alpha ^ { - 1 } ( \hat { \varrho } / \hat { \varrho } t ) ^ { a }$ ，满足 ${ n ^ { a } \notin W _ { q } }$ 且 ${ n _ { a } n } ^ { a } < 0$ 即 $n ^ { a }$ 为类时).

(2) $\phi [ \mathbb { R } ]$ 与 $t$ 轴平行[见图4-6(b)]. $\forall q \in \phi [ \mathbb { R } ]$ ，令 $( e _ { 2 } ) ^ { a } = ( \partial / \partial t ) ^ { a }$ ，选

$( e _ { 1 } ) ^ { a } = \alpha \left( \widehat { \partial } / \widehat { \partial } t \right) ^ { a } + \beta \left( \widehat { \partial } / \widehat { \partial } x \right) ^ { a }$ ， $( \alpha , \beta$ 可为任意实数，但 $\beta \neq 0$ ）

则 $( e ^ { 1 } ) _ { a } = \beta ^ { - 1 } ( \mathrm { d } x ) _ { a }$ .取 $( e ^ { 1 } ) _ { a }$ 为法余矢 $n _ { a }$ ，相应的法矢为 $n ^ { a } = \beta ^ { - 1 } ( \hat { \partial } / \hat { \partial } x ) ^ { a }$ ，满足 $n ^ { a } \notin W _ { q }$ 且 $n _ { a } n ^ { a } > 0$ (即 $n ^ { a }$ 为类空).

(3) $\phi [ \mathbb { R } ]$ 与 $x$ 轴夹 $4 5 ^ { \circ }$ 角(按欧氏)[见图4-6(c)]. $\forall q \in \phi [ \mathbb { R } ]$ ，令 $( e _ { 2 } ) ^ { a } = ( \partial / \partial t ) ^ { a }$ $+ ( \partial / \partial x ) ^ { a }$ ，选 $( e _ { 1 } ) ^ { a } = \alpha \left( \partial / \partial t \right) ^ { a } + \beta \left( \partial / \partial x \right) ^ { a }$ ， $\alpha \neq \beta$ ，则 $( e ^ { 1 } ) _ { a } = ( \alpha - \beta ) ^ { - 1 } [ ( \mathrm { d } t ) _ { a } -$ $( \operatorname { d } x ) _ { a } ]$ .取 $( e ^ { 1 } ) _ { a }$ 为法余矢 $n _ { a }$ ，相应的法矢为

$n ^ { a } = \left( \alpha - \beta \right) ^ { - 1 } g ^ { a b } [ \left( \mathbf { d } t \right) _ { b } - \left( \mathbf { d } x \right) _ { b } ] = - \left( \alpha - \beta \right) ^ { - 1 } [ \left( \partial / \partial t \right) ^ { a } + \left( \partial / \partial x \right) ^ { a } ] = - \left( \alpha - \beta \right) ^ { - 1 } \left( \partial / \partial t \right) ^ { b } .$ （e2)，满足 ${ n ^ { a } \in W _ { q } }$ 且 ${ n _ { a } n } ^ { a } = 0$ （即 $n ^ { a }$ 为类光)．在这种情况下，超曲面的法矢既与面上所有切矢垂直(法矢定义)，本身又是切矢之一！

![](images/7f489c0eaac1e0cf2e840af68c11b3087e76c3fd3ad4de25dceb0180ed361878.jpg)  
图4-6 $\mathbb { R }$ 嵌人 $\mathbb { R } ^ { 2 }$ 的三种情况 $( t$ 轴竖直向上， $\pmb { x }$ 轴水平向右)

定义4超曲面叫类空的，若其法矢处处类时 $( n ^ { a } n _ { a } < 0 )$ ；超曲面叫类时的，若其法矢处处类空 $( n ^ { a } n _ { a } > 0 )$ ；超曲面叫类光的，若其法矢处处类光( $\displaystyle ( n _ { a } n ^ { a } = 0 )$ ).

若 $n ^ { a } n _ { a } \neq 0$ ，今后谈法矢时都指归一化法矢，即 $n ^ { a } n _ { a } = \pm 1$ ·

定义5设S]是流形 $M$ 中的嵌入子流形(不一定是超曲面)， $q \in \phi [ S ]$ ， $W _ { q }$ 是 $q$ 点切于 $\phi [ S ]$ 的切空间． $W _ { q }$ 的度规 $h _ { a b }$ 叫做由 $V _ { q }$ 的度规 $g _ { a b }$ 生出的诱导度规(induced metric)，若

$$
h _ { a b } w _ { 1 } ^ { \ a } w _ { 2 } ^ { \ b } = g _ { a b } w _ { 1 } ^ { \ a } w _ { 2 } ^ { \ b } , \qquad \forall w _ { 1 } ^ { \ a } , \ w _ { 2 } ^ { \ b } \in W _ { q } .
$$

诱导度规 $h _ { a b }$ 实质上是把 $V _ { q }$ 上度规 $g _ { a b }$ 的作用对象限制于 $W _ { q }$ 的结果．当[S]为类时或类空超曲面时，诱导度规 $h _ { a b }$ 可用其归一化法矢( $( n ^ { a } n _ { a } = \pm 1$ 方便地表为(4-4-1)．然而满足式(4-4-1)的hab很多，为什么只能用式(4-4-2)的那个？理由见选读 4-4-3.

[选读 4-4-3]

为便于陈述，设Vq为4维(因而Wq为3维)．作为诱导度规(Wq上的度规),式(4-4-1)的hab是Wq上的张量(3维张量)，即hab∈(0,2)(它不能作用于Va-Wa的元素)．但为了便于用4维等式演算，我们希望找到一个4维的(0，2)型张量[即$\mathcal { T } _ { V _ { q } } ( 0 , 2 )$ 的元素],它能代表3维张量 $h _ { a b } \cdot h _ { a b } \equiv g _ { a b } \mp n _ { a } n _ { b }$ 中的 $h _ { a b }$ 就是这样的4维张量(注意，右边两项都是 4 维张量)．为与式(4-4-1)的 hab 相区别，暂时把$h _ { a b } \equiv g _ { a b } \mp n _ { a } n _ { b }$ 中的 $h _ { a b }$ 记作 $\overline { { h } } _ { a b }$ .可以证明 $\mathcal { T } _ { V _ { q } } ( 0 , 2 )$ 的子集 $\mathcal { S } _ { V _ { q } } ( 0 , 2 ) \equiv \{ T _ { a b } \in$ $\mathcal { T } _ { V _ { q } } ( 0 , 2 ) | T _ { a b } n ^ { a } { = } 0 , T _ { a b } n ^ { b } = 0 \}$ 与 $\mathcal { T } _ { W _ { q } } ( 0 , 2 )$ 自然同构，因而可以自然认同(详见第 14章)．易见 $g _ { a b } \notin \mathcal { S } _ { V _ { q } } ( 0 , 2 )$ 而 $\overline { { h } } _ { a b } \in \mathcal { S } _ { V _ { q } } ( 0 , 2 )$ ，且 $\overline { { { h } } } _ { a b } w _ { 1 } { } ^ { a } w _ { 2 } { } ^ { b } = g _ { a b } w _ { 1 } { } ^ { a } w _ { 2 } { } ^ { b } \forall w _ { 1 } { } ^ { a }$ ， ${ w _ { 2 } } ^ { b }$ $\in W _ { q }$ ，所以可把 $\overline { { h } } _ { a b }$ 认同为 $h _ { a b }$ .还可证明(读者自证) $\mathcal { S } _ { V _ { q } } ( 0 , 2 )$ 中满足式(4-4-1)(因而可充当 $h _ { a b } )$ 的元素只有 $\overline { { h } } _ { a b }$ ，这就是把4维张量 $\overline { { h } } _ { a b } \equiv g _ { a b } \mp n _ { a } n _ { b }$ 看作诱导度规的理由．以后将不在符号上区分 $\overline { { h } } _ { a b }$ 和 $h _ { a b } .$

以上关于(0,2)型张量的结论还可推广为：(0,l)的子集{Taa,∈(0,I)$\vert T _ { a \cdots a _ { l } }$ 的任一下标与 $n ^ { a }$ 缩并为零}与 $\mathcal { T } _ { W _ { q } } ( 0 , l )$ 有自然同构关系,因而可自然认同.这种认同使我们在讨论和书写公式时可用前者的元素代替后者的元素(写成4维而非3维张量等式)，从而带来许多方便.

注3式(4-4-2)在gab为正定时也成立(把干号改为-号)．作为练习，读者试写出3维欧氏度规gab用球坐标系对偶坐标基底的展开式，并验证球面上诱导度规$h _ { a b } = g _ { a b } - n _ { a } n _ { b }$ 同\$3.3例2所定义的诱导度规 $\hat { g } _ { a b }$ 一致．[提示：球面上的归一化法余矢 $n _ { a } = \left( \mathrm { d } r \right) _ { a } .$ ]

设 $\phi [ S ]$ 为类时或类空超曲面， $q \in \phi \left[ S \right]$ ， $h _ { a b }$ 满足式(4-4-2).令

$$
h _ { b } ^ { a } \equiv g ^ { a c } h _ { c b } = \delta _ { b } ^ { a } \mp n ^ { a } n _ { b } \ ,
$$

则 $\forall v ^ { a } \in V _ { q }$ 有 $h _ { ~ b } ^ { a } \upsilon ^ { b } = \upsilon ^ { a } \mp n ^ { a } ( n _ { b } \upsilon ^ { b } )$ ，或

$$
\boldsymbol { \nu } ^ { a } = h ^ { a } { } _ { b } \boldsymbol { \nu } ^ { b } \pm n ^ { a } ( n _ { b } \boldsymbol { \nu } ^ { b } ) .
$$

上式代表矢量 $\nu ^ { a }$ 的一种分解(图 4-7)，其中$\pm n ^ { a } ( n _ { b } \nu ^ { b } )$ 与法矢 $n ^ { a }$ 平行，称为法向分量， $\boldsymbol { h } _ { \ b } ^ { a } \boldsymbol { \nu } ^ { b }$ 与法矢 $n ^ { a }$ 垂直[因为 $n _ { a } ( h _ { b } ^ { a } \upsilon ^ { b } ) = 0 ]$ ，称为切向分量(切于 $\phi [ S ]$ 的分量). $\boldsymbol { h } _ { \ b } ^ { a }$ 称为从 $V _ { q }$ 到 $W _ { q }$ 的投影映射(projection map).

![](images/700f2c629a1010e5b12b03e3ccf91b85710edd14d433dfd90431211de1de2b65.jpg)  
图4-7矢量 $\upsilon ^ { a } \in V _ { q }$ 分解为法向分量 $\pm n ^ { a } ( n _ { b } \nu ^ { b } )$ 和切向分量 $h ^ { a } b ^ { b } \in W _ { p }$

定理4-4-4类光超曲面上的诱导“度规”是退化的(因而没有诱导度规).

证明以 $h _ { a b }$ 代表诱导“度规”．超曲面的类光性导致 $n ^ { a } \in W _ { q }$ (见定理4-4-3),故 $W _ { q }$ 有非零元素 $n ^ { a }$ 使 $h _ { a b } n ^ { a } w ^ { b } = g _ { a b } n ^ { a } w ^ { b } = 0 , \forall w ^ { a } \in W _ { q }$ .可见 $h _ { a b }$ 是 $W _ { q }$ 上的退化张量. □

例4设 $t , \ x , \ y , \ z$ 是4维闵氏空间 $( \mathbb { R } ^ { 4 } , \eta _ { a b } )$ 的洛伦兹坐标，则 $\eta _ { a b }$ 可用对偶坐标基矢表为

$\eta _ { a b } = \eta _ { \mu \nu } ( \mathrm { d } x ^ { \mu } ) _ { a } ( \mathrm { d } x ^ { \nu } ) _ { b } = - \left( \mathrm { d } t \right) _ { a } ( \mathrm { d } t ) _ { b } + \left( \mathrm { d } z \right) _ { a } ( \mathrm { d } z ) _ { b } + \left( \mathrm { d } x \right) _ { a } ( \mathrm { d } x ) _ { b } + \left( \mathrm { d } y \right) _ { a } ( \mathrm { d } y ) _ { b } .$ (4-4-5)方程 $t - ( x ^ { 2 } + y ^ { 2 } + z ^ { 2 } ) ^ { 1 / 2 } = 0$ 定义了一个类光超曲面 $\mathcal { S }$ ，它是以原点为锥顶的圆锥面(见图4-8). $\forall q \in \mathcal { S } \subset \mathbb { R } ^ { 4 }$ ，有4维切空间 $V _ { q }$ 和3维切空间(切于 $\mathcal { S } ) W _ { q } \subset V _ { q }$ 令则 $\pmb { n } ^ { \pmb { a } }$ 是 $\mathcal { S }$ 在 $q$ 点的类光法矢，故 ${ n ^ { a } \in W _ { q } }$ ，因而 $\left\{ \left( \hat { \partial } / \hat { \partial } x \right) ^ { a } , \left( \hat { \partial } / \hat { \partial } y \right) ^ { a } , n ^ { a } \right\}$ 是 $W _ { q }$ 的基底．现在计算 $\eta _ { a b }$ 在 $W _ { q }$ 上的诱导“度规” $h _ { a b }$ 在此基底的分量 $h _ { \mu \nu }$ ·

$$
h _ { 1 1 } \equiv h _ { a b } ( \widehat { { \cal O } } / \widehat { \partial } x ) ^ { a } ( \widehat { { \cal O } } / \widehat { \partial } x ) ^ { b } = \eta _ { a b } ( \widehat { { \cal O } } / \widehat { \partial } x ) ^ { a } ( \widehat { { \cal O } } / \widehat { \partial } x ) ^ { b } = 1 \ ,
$$

其中第二步用到式(4-4-1)，第三步用到式(4-4-5)．类似地，有 $h _ { 2 2 } \equiv h _ { a b } ( \widehat { \partial } / \widehat { \partial } y ) ^ { a }$ $\left( \partial / \partial y \right) ^ { b } = 1$ .而 $h _ { \mu \nu }$ 的第三个对角元(记作 $h _ { n n } )$ 则为

$$
h _ { n n } \equiv h _ { a b } n ^ { a } n ^ { b } = \eta _ { a b } [ \left( \partial / \partial t \right) ^ { a } + \left( \partial / \partial z \right) ^ { a } ] [ \left( \partial / \partial t \right) ^ { b } + \left( \partial / \partial z \right) ^ { b } ] = 1 - 1 = 0 ,
$$

而且容易验证 $h _ { \mu \nu }$ 的所有非对角元为零，故

$$
( h _ { \mu \nu } ) = \left[ \begin{array} { l l l } { { 1 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 1 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 0 } } \end{array} \right] ,
$$

因而 $h _ { a b }$ 退化[也说其“号差”为 $\left( + , + , 0 \right) ]$ 可见 $\eta _ { a b }$ 在类光超曲面 $\mathcal { S }$ 上无诱导度规．然而，令 $s$ 为 $\mathcal { S }$ 与任一等 $t$ 面 $( t > 0 )$ 之交(是2维球面)，以 $\hat { W } _ { q } \subset W _ { q }$ 代表 $W _ { q }$ 中所有切于 $s$ 的元素组成的子空间(见图4-8),则 $\eta _ { a b }$ 在 $\hat { W } _ { q }$ 却有诱导度规,记作 $\hat { h } _ { a b }$ ，而且不难验证

![](images/1c0b77640f926bb6503bac7ee9aeca70b9e950825dec8f3d21f5f7e1370a9f23.jpg)  
图4-8类光超曲面 $\mathcal { S }$ 的诱导“度规”退化

$$
\hat { h } _ { a b } = \left( \mathrm { d } x \right) _ { a } \left( \mathrm { d } x \right) _ { b } + \left( \mathrm { d } y \right) _ { a } \left( \mathrm { d } y \right) _ { b } .
$$

读者不难对 $( \mathbb { R } ^ { 4 } , \eta _ { a b } )$ 中由 $\scriptstyle t - z = 0$ 定义的类光超曲面做类似讨论.

# 习 题

\~1．试证由式(4-1-1)定义的 $( \phi _ { * } \nu ) ^ { a }$ 满足 $\ S 2 . 2$ 定义2对矢量的两个要求，从而确是 $\phi ( p )$ 点的矢量

$\sim _ { 2 }$ ，试证定理4-1-1、4-1-2和4-1-3.

3.设 $\phi : M \to N$ 为光滑映射， $p \in M$ ， $\{ y ^ { \mu } \}$ 是 $\phi ( p )$ 点某邻域上的坐标，试证

$$
( \phi _ { * } \upsilon ) ^ { a } = \upsilon ( \phi ^ { * } y ^ { \mu } ) ( \partial / \partial y ^ { \mu } ) ^ { a } , \qquad \forall \upsilon ^ { a } \in { \cal V } _ { p } .
$$

4.设 $M , N$ 是流形， $\phi : M \to N$ 是微分同胚， $p \in M$ ， $\pmb q \equiv \phi ( \pmb p )$ ，试证推前映射 $\phi _ { * } : V _ { p } \to V _ { q }$ 是同构映射.

5.设 $M , ~ N , ~ Q$ 是流形， $\phi : M \to N$ 和 $\psi : N \to Q$ 是光滑映射.

(a）试证 $\left( \psi \circ \phi \right) ^ { * } f = \left( \phi ^ { * } \circ \psi ^ { * } \right) f \ , \forall f \in \mathcal { F } _ { Q } \ .$

（b）试证 $( \psi \circ \phi ) _ { \ast } v ^ { a } = \psi _ { \ast } ( \phi _ { \ast } v ^ { a } ) \ , \forall p \in M , \upsilon ^ { a } \in V _ { p } .$

(c）把 $( \psi \circ \phi ) ^ { * }$ 和 $\phi ^ { * } \circ \psi ^ { * }$ 都看作由 $\mathcal { F } _ { Q } ( 0 , l )$ 到 $\mathcal { F } _ { M } ( 0 , l )$ 的映射，试证

$$
\left( \psi \circ \phi \right) ^ { * } = \phi ^ { * } \circ \psi ^ { * } .
$$

6.设 $\phi : M \to N$ 是微分同胚， $\nu ^ { a } , u ^ { a }$ 是 $M$ 上矢量场，试证 $\phi _ { * } ( [ \nu , u ] ^ { a } ) = [ \phi _ { * } \nu , \phi _ { * } u ] ^ { a }$ ，其中$[ v , u ] ^ { a }$ 代表对易子.

$\sim _ { 7 }$ ，试证定理4-2-4.

$\sim \mathbf { 8 } .$ 设 $\boldsymbol { \upsilon } ^ { a } \in \mathcal { F } _ { M } \left( 1 , 0 \right) , \ \boldsymbol { \omega } _ { a } \in \mathcal { F } _ { M } \left( 0 , 1 \right)$ ，试证对任一坐标系 $\{ x ^ { \mu } \}$ 有

$( \mathcal { L } _ { \nu } \omega ) _ { \mu } = v ^ { \nu } \partial \omega _ { \mu } / \partial x ^ { \nu } + \omega _ { \nu } \partial v ^ { \nu } / \partial x ^ { \mu }$ ：提示：用式(4-2-7)并令其 $\nabla _ { a }$ 为 $\widehat { \sf { d } } _ { u }$

${ \bf \tilde { \rho } } _ { 9 . }$ 设 $u ^ { a } , \upsilon ^ { a } \in \mathcal { F } _ { M } ( 1 , 0 )$ ，则下式作用于任意张量场都成立

$$
[ \mathcal { L } _ { \nu } , \mathcal { L } _ { u } ] = \mathcal { L } _ { [ \nu , u ] } \quad ( \# \# [ \mathcal { L } _ { \nu } , \mathcal { L } _ { u } ] \equiv \mathcal { L } _ { \nu } \mathcal { L } _ { u } - \mathcal { L } _ { u } \mathcal { L } _ { \nu } ) .
$$

试就作用对象为 $f \in \mathcal { F } _ { M }$ 和 $w ^ { a } \in \mathcal { F } _ { M } ( 1 , 0 )$ 的情况给出证明．提示：当作用对象为 $w ^ { a }$ 时可用雅可比恒等式(第2章习题8).

10.设 $F _ { a b }$ 是4维闵氏空间上的反对称张量场，其在洛伦兹坐标系 $\{ t , \ x , \ y , \ z \}$ 的分量为$F _ { 0 1 } = - F _ { 1 3 } = x \rho ^ { - 1 }$ ， $F _ { 0 2 } = - F _ { 2 3 } = y \rho ^ { - 1 }$ ， $F _ { 0 3 } = F _ { 1 2 } = 0$ ,其中 $\rho \equiv ( x ^ { 2 } + y ^ { 2 } ) ^ { 1 / 2 }$ ，试证 $F _ { a b }$ 有旋转对称性，即 $\mathcal { L } _ { \nu } F _ { a b } = 0$ ，其中 $v ^ { a } = - y ( \partial / \partial x ) ^ { a } + x ( \partial / \partial y ) ^ { a }$ .

11.设 $\xi ^ { a }$ 是 $( M , g _ { a b } )$ 中的 Killing 矢量场， $\nabla _ { a }$ 与 ${ \pmb g } _ { a b }$ 适配，试证 $\nabla _ { a } \xi ^ { a } = 0$

12.设 $\xi ^ { a }$ 是 $( M , g _ { a b } )$ 中的 Killing 矢量场, $\phi : M \to N$ 是等度规映射,试证 $\phi _ { * } \xi ^ { a }$ 也是 $( M , g _ { a b } )$ 中的 Killing 矢量场．提示：利用习题 5(c)的结论.

13.设 $\xi ^ { a }$ ， $\eta ^ { a }$ 是 $( M , g _ { a b } )$ 的 Killing 矢量场，试证其对易子 $\left[ \xi , \eta \right] ^ { a }$ 也是 Killing 矢量场．注：此结论使得 $M$ 上全体 Killing 矢量场的集合不但是矢量空间，而且是李代数(详见下册附录G).

14.设 $\xi ^ { a }$ 是广义黎曼空间 $( M , g _ { a b } )$ 的 Killing 矢量场， ${ R _ { a b c } } ^ { d }$ 是 $g _ { a b }$ 的黎曼曲率张量.

(a）试证 $\nabla _ { a } \nabla _ { b } \xi _ { c } = - { R _ { b c a } } ^ { d } \xi _ { d }$ ．注：此式对证明定理4-3-4有重要用处．提示：由 ${ R _ { a b c } } ^ { d }$ 的定义以及Killing 方程(4-3-1)可知 $\nabla _ { a } \nabla _ { b } \xi _ { c } + \nabla _ { b } \nabla _ { c } \xi _ { a } = { R _ { a b c } } ^ { d } \xi _ { d }$ ．此式称为第一式．作指标替换$a \mapsto b , b \mapsto c , c \mapsto a$ 得第二式，再替换一次得第三式．以第一、二式之和减第三式并利用式(3-4-7)便得证.

(b）利用(a)的结果证明 $\nabla ^ { a } \nabla _ { a } \xi _ { c } = - R _ { c d } \xi ^ { d }$ ，其中 $R _ { c d }$ 是里奇张量.

\~15．验证式(4-3-3)中的 $( \partial / \partial \eta ) ^ { a }$ 的确满足 Killing 方程(4-3-1).

\~16.找出2维欧氏空间中由 $R ^ { a } = x ( \partial / \partial y ) ^ { a } - y ( \partial / \partial x ) ^ { a }$ 生出的单参等度规群的任一元素 $\phi _ { \alpha }$ 诱 导的坐标变换.

$^ { * 1 7 }$ ，设时空 $( M , g _ { a b } )$ 中的超曲面 $\phi [ S ]$ 上每点都有类光切矢而无类时切矢（“切矢”指切于$\phi [ S ]$ )，试证它必为类光超曲面．提示： $\textcircled{1}$ 证明与类时矢量 $t ^ { a }$ 正交的矢量必类空[选正交归一基底 $\{ ( e _ { \mu } ) ^ { a } \}$ 使 $( e _ { 0 } ) ^ { a } = t ^ { a } ]$ ； $\textcircled{2}$ 证明类时超曲面上每点都有类时切矢； $\textcircled{3}$ 由以上两点证明本命题.


<!-- chunk 0004: pages 121-160 -->
