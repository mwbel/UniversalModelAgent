在地磁学中把这种用来确定某一观测点地磁场的各独立分量称为地磁要素。如图5.5所示， $o$ 为观测点， $o X Y$ 为地平面， $o x$ 指向地理北极， $o z$ 垂直地面，向下为正， $O F$ 为地磁场向量 ${ \pmb H }$ ，它的模 $O F$ 称为地磁场的总强度，通常用 $\pmb { F }$ 表示； $O F$ 可分解为向北、向东、向下三个分量 $O A , O B , O C$ ，用 $X , Y , z$ 表示；最常用的另一组分量是： $O F$ 在水平面上的投影 $o D$ ，叫做水平分量 $\left( H \right) ; O D$ 与正北方向的夹角 $_ D$ ，叫做地磁偏角。水平分量$\pmb { H }$ ，磁偏角 $D$ ，连同垂直分量 $z$ 一起构成一组描写观测点 $o$ 地磁向量 $O F$ 的独立分量；还有 $O F$ 对于水平面的倾角 $I$ ，叫做地磁倾角。总强度 ${ \pmb F }$ ，偏角 $_ { D }$ 和倾角 $\pmb { I }$ 又可构成另一组独立的分量系统。当然还可以有其他的组合方式。以上七个常用的可供选择的分量$\smash { F , X , Y , z , H , D }$ 和 $\pmb { I }$ 通称作地磁要素。它们之间有如下简单关系：

$$
F ^ { 2 } = X ^ { 2 } + Y ^ { 2 } + Z ^ { 2 } ; \ H ^ { 2 } = X ^ { 2 } + Y ^ { 2 } ;
$$

$$
\begin{array} { r } { \boldsymbol { \Upsilon } = H \sin D , \ Z = H \tan I _ { o } } \end{array}
$$

如果已知其中独立的三个，其他四个要素也可以计算出来。

地磁测量就是应用地磁仪器观测某一测点独立的地磁三要素。完成这种观测任务的测点通常分成两类，一类是能连续记录地磁场随时间变化的测点,叫做地磁台。一般台站都装备两套观测系统，一套叫做磁变仪，用来连续记录地磁场随时间的相对变化,通常选用 $H , D , z$ 三个要素。经典的记录方式是把地磁变化转换为光点的移动，用照相的方法把这种变化记录下来，这种记录叫做磁照图。图5.6为我国某地磁台世界日一天的磁照图，图中三条曲线即为 $H , I , D$ 三要素随时间的变化。现在美、日等国已逐步采用数字化仪器和记录系统;另一套是测定地磁要素绝对值的仪器，叫做磁强计或磁力仪，其中用来测定偏角和倾角的经典仪器又叫作地磁经纬仪。磁强计不做连续记录，而是在特定的时间(一般每周两次)进行观测，目的是用来标定相对记录的磁变仪。两套仪器配合把地磁台站的磁场绝对值及其随时间的变化连续地确定下来。除地磁台站外，另一类是野外磁测点。野外磁测点不能连续测定地磁场随时间的变化,而是间断地(例如3一5年)进行地磁要素的绝对测量。但不同磁测点的观测不可能都在同一时刻进行，为了便于分析,还必须将各测点不同时间的观测值，按照地磁场的时间变化规律，归算到同一指定时刻。野外磁测点和地磁台相互补充，构成全球性或局部地区的地磁测网。此外还有航空测量（一般测 $\pmb { F }$ ）和近代发展起来的卫星测量，美国79年发射了专门的磁测卫星。地磁台站和野外磁测点所取得的特定时刻地磁场各要素的数值和它们随时间的变化，构成了地磁场分析研究的基础资料，是进行高斯分析的边值条件。

# 2.高斯系数的确定和内外源场的区分

地磁七个要素每三个独立分量的组合，虽都能等价地有效地表征地磁向量 $\pmb { H }$ ，但它们各具特点，在使用上又各有便利之处。例如，以角度为主的组合 $\smash {  { D _ { \perp } } H _ { \perp } I }$ 和 $D , F , I$ 能够直观地表征磁场向量的方向，而在分析计算中则多采用 $X , Y , z$ 三个要素的组合。这里高斯系数的确定所要回答的中心问题有两个，一是当内边界（即地球表面 $\gamma = a )$ 那些条件已知时，才能可能唯一确定全部高斯系数 $\pmb { \mathrm { \pmb { g } } } \pmb { \mathrm { \cdot } } \pmb { \mathrm { \pmb { g } } } \pmb { e }$ 和 $\pmb { h } _ { i \setminus } \pmb { h } _ { e }$ ；第二是如何根据实测点的观测结果，计算各级常系数 $g _ { n i } ^ { m } \setminus g _ { n e } ^ { m }$ 和 $h _ { n i } ^ { m } \setminus h _ { n e } ^ { m }$ o

设除已知 $W$ 在内边界 $( \pmb { r } = \pmb { a } )$ 的分布外，还知道 $W$ 在界面上的法向导数，由(5.86)可得

$$
\begin{array} { c } { { Z = \displaystyle \frac { \partial W } { \partial r } = \sum _ { n = 1 } ^ { \infty } \sum _ { m = 0 } ^ { n } \left\{ \left[ \left( \frac { r } { a } \right) ^ { n - 1 } \left( n g _ { n e } ^ { m } \left( t \right) \cos m \lambda + n h _ { n e } ^ { m } \left( t \right) \sin m \lambda \right) \right. \right. } } \\   \left. \left. - \left( \frac { a } { r } \right) ^ { n + 2 } \left( \left( n + 1 \right) g _ { n i } ^ { m } \left( t \right) \cos m \lambda + \left( n + 1 \right) h _ { n i } ^ { m } \left( t \right) \sin m \lambda \right) \right] P _ { n } ^ { m } \left( \cos \theta \right) \right\} \mathrm { o } \end{array}
$$

当 $\pmb { r } = \pmb { a }$ 时,对于特定时刻 $\pmb { t _ { 0 } }$

$$
Z ( a , \ \theta , \ \lambda , \ t _ { 0 } ) = \left( \frac { \partial { \cal W } } { \partial _ { r } } \right) _ { \stackrel { r = a } { t = t _ { 0 } } }
$$

$$
\begin{array} { l } { { \displaystyle = \sum _ { n = 1 } ^ { \infty } \sum _ { m = 0 } ^ { n } \left\{ \left[ \left( n g _ { n e } ^ { m } \left( t _ { 0 } \right) - \left( n + 1 \right) g _ { n i } ^ { m } \left( t _ { 0 } \right) \right) \cos m \lambda + \left( n h _ { n e } ^ { m } \left( t _ { 0 } \right) \right. \right. \right. } } \\ { { \left. \left. \left. - \left( n + 1 \right) h _ { n i } ^ { m } \left( t _ { 0 } \right) \right) \sin m \lambda \right] P _ { n } ^ { m } ( \cos \theta ) \right\} _ { 0 } } } \end{array}
$$

与(5.95)相似，由球面函数正交性(5.91)和地面垂直分量 $z$ 的分布(5.97)可以得到

$$
\left. \begin{array} { l } { { n g _ { n e } ^ { m } \left( t _ { 0 } \right) - ( n + 1 ) g _ { n i } ^ { m } \left( t _ { 0 } \right) = \displaystyle \frac { 2 n + 1 } { 4 \pi } \displaystyle \int _ { 0 } ^ { \pi } \int _ { 0 } ^ { 2 \pi } Z \left( a , \theta , \lambda , t _ { 0 } \right) P _ { n } ^ { m } \left( \cos \theta \right) \cos { m \lambda } } } \\ { { \phantom { n g _ { n e } ^ { m } \left( t _ { 0 } \right) - ( n + 1 ) } \cdot \phantom { \displaystyle } \sin { \theta } d \theta d \lambda , } } \\ { { n h _ { n e } ^ { m } \left( t _ { 0 } \right) - ( n + 1 ) h _ { n i } ^ { m } \left( t _ { 0 } \right) = \displaystyle \frac { 2 n + 1 } { 4 \pi } \displaystyle \int _ { 0 } ^ { \pi } \int _ { 0 } ^ { 2 \pi } Z \left( a , \theta , \lambda , t _ { 0 } \right) P _ { n } ^ { m } \left( \cos \theta \right) } } \end{array} \right\}
$$

$$
\bullet \ \sin m \lambda \sin \theta d \theta d \lambda _ { \circ }
$$

若在内边界，=a，W及其法向导数Z已知，则方程（5.95)和（5.99)右端为已知量。(5.95)和（5.99）构成一组关于g、gi和h、h,四个未知量的四个线性独立的方程组,这个方程组可以唯一确定全部高斯系数ge、gi和h、hi。需要指出，这里给出的定解条件既不同于一般椭圆方程已知全部边界场值的第一边界条件(Dirichlet问题),也不同于已知全部边界场的法向导数的第二边界条件 (Neumann 问题)，当然更不是混合边界条件(已知场和场的法向导数的线性组合)的劳平(Robin)问题,而是仅在其内边界上独立给出第一、第二种边界条件。由以上分析可以看出这种边界条件的定解问题同样是唯一的。这种唯一性连同球面函数的正交性可以保证我们在用（5.95）和(5.99)确定某一阶（或级)常系数g、g和h、h时，与其他阶(或级)常系数是否已经求出无关。因而在(5.86)中，取项数多少只影响解的精确程度，而与级数各项本身无关，这种性质对于解的收敛快慢尚未确定之前，根据已经取得的结果研究场的性质有特别重要的意义。

在实际计算中，由于场位W无法直接观测，还不能直接由(5.95)和(5.99)直接确定高斯系数。设在地球表面(r=α)除已知垂直分量Z外(5.98)，北向分量X和东向分量Y也已给定。由（5.86)

$$
X ( r , \theta , \lambda , \iota ) = \frac { \partial W } { r \partial \theta }
$$

$$
\begin{array} { l } { { \displaystyle = \sum _ { n = 1 } ^ { \infty } \sum _ { m = 0 } ^ { n } \left\{ \left[ \left( \frac { a } { r } \right) ^ { n + 2 } \left( g _ { n i } ^ { m } \left( t \right) \cos m \lambda + h _ { n i } ^ { m } \left( t \right) \sin m \lambda \right) \right. \right. } } \\ { { \displaystyle \left. \left. + \left( \frac { r } { a } \right) ^ { n - 1 } \left( g _ { n e } ^ { m } \left( t \right) \cos m \lambda + h _ { n e } ^ { m } \left( t \right) \sin m \lambda \right) \right] \frac { d P _ { n } ^ { m } \left( \cos \theta \right) } { d \theta } \right\} } , }  \end{array}
$$

$$
Y ( r , \theta , \lambda , t ) = - \frac { \partial W } { r \sin \theta \partial \lambda }
$$

$$
\begin{array} { c } { { \displaystyle = \frac 1 { \sin \theta } \sum _ { n = 1 } ^ { \infty } \sum _ { m = 0 } ^ { n } \left\{ \left[ \left( \frac { \alpha } { r } \right) ^ { n + 2 } \left( m g _ { n i } ^ { m } \left( t \right) \sin m \lambda - m h _ { n i } ^ { m } \left( t \right) \cos m \lambda \right) \right. \right. } } \\ { { \displaystyle \left. \left. + \left( \frac { r } { a } \right) ^ { n - 1 } \left( m g _ { n e } ^ { m } \left( t \right) \sin m \lambda - m h _ { n e } ^ { m } \left( t \right) \cos m \lambda \right) \right\} P _ { n } ^ { m } ( \cos \theta ) \right\} , } } \end{array}
$$

当 $\pmb { r } = \pmb { a }$ 时,对于特定时刻 $\pmb { t _ { 0 } }$

$$
\begin{array} { c } { { X ( a , ~ \theta , ~ \lambda , ~ t _ { 0 } ) = \left( \frac { \partial W } { r \partial \theta } \right) _ { t = t _ { 0 } } } } \\ { { = \displaystyle \sum _ { n = 1 } ^ { s } \sum _ { m = 0 } ^ { n } \Big \{ [ \left( g _ { n i } ^ { m } ~ ( t _ { 0 } ) + g _ { n e } ^ { m } \left( t _ { 0 } \right) \right) \cos m \lambda } } \\ { { + \left( h _ { * i } ^ { , } \left( t _ { 0 } \right) + h _ { n e } ^ { m } \left( t _ { 0 } \right) \right) \sin m \lambda ] \frac { d P _ { n } ^ { m } ( \cos \theta ) } { d \theta } \Big \} , } } \end{array}
$$

$$
Y ( a , \ \theta , \ \lambda , \ \varepsilon _ { 0 } ) = \left( - \frac { \partial { \cal W } } { r \sin \theta \partial \lambda } \right) _ { r = a _ { 0 } }
$$

由(5.102)和(5.103)可以看出，与(5.94)场位 $\pmb { W }$ 一样，北向分量 $\pmb { X }$ 和东向分量 $\pmb { \mathrm { y } }$ 也是与关于高斯系数的内外场之和 $g _ { i } + g _ { e } , \ h _ { i } + h _ { e }$ 相联系。可以证明在界面上已知 $x$ 或 $\mathbf { Y }$ 和已知 $W$ 是完全等效的。由关系

$$
W ( a , \theta , \lambda ) = { } _ { a } \int _ { 0 } ^ { \theta } X ( a , \theta , \lambda ) d \theta ,
$$

$$
W ( a , \theta , \lambda ) = - \left. a \sin \theta \int _ { 0 } ^ { \lambda } Y ( a , \theta , \lambda ) d \lambda + W ( a , \theta , \lambda ) _ { \lambda = 0 } \right.
$$

可直接看出,北向分量 $\pmb { X }$ 与 $\pmb { W }$ 是等效的((5.104)),但(5.105)尚有一依赖于 $\ X ( a , \theta , \lambda ) ( \ldots 0$ 的项 $\begin{array} { r } { W \left( \boldsymbol { a } , \boldsymbol { \theta } , \lambda \right) \vert _ { \lambda = 0 } . } \end{array}$ ，即仅由 $\mathbf { Y }$ 还不能完全确定场位 $W$ （除允许差任意常数外）。将(5.105)代人(5.95），由

$$
\int _ { 0 } ^ { \pi } \int _ { 0 } ^ { 2 \pi } W \left( a , \theta , \lambda \right) _ { \lambda = 0 } P _ { \pi } ^ { m } \left( \cos \theta \right) _ { \sin m \lambda } ^ { \cos m \lambda } \sin \theta d \theta d \lambda = 0
$$

可知，依赖于 $X \mid _ { \imath = 0 }$ 的项 $W \mid _ { \lambda = 0 }$ 的存在与高斯常系数的确定无关。这就证明了 $\pmb { x }$ 或 $\mathbf { Y }$ 与$\pmb { W }$ 的上述等效性。因此在地球表面，与 $W , z$ 一样，已知强度 $\pmb { X }$ （或 $\pmb { Y }$ ）、 $\textbf { z }$ 的分布也能唯一确定全部高斯系数。这种等效性和唯一性也可以由 $\boldsymbol { X } , \boldsymbol { Y }$ 分量的级数表达式（5.102）、(5.103)直接证明。对于 $\pmb { Y }$ 分量，由(5.103)可以得出，

$$
Y ( a , \theta , \ : , \ : \lambda , \ : t _ { 0 } ) \sin \theta = \sum _ { n = 1 } ^ { \infty } \sum _ { m = 0 } ^ { n } \ : [ \ : ( g _ { n i } ^ { m } + \xi _ { n e } ^ { m } ) \sin \lambda - \ : ( h _ { n i } ^ { m } + h _ { n e } ^ { m } ) \cos m \lambda ] m P _ { n } ^ { m } ( \cos \theta ) \ : _ { \ : \mathrm { o } }
$$

由 $\pmb { P _ { n } ^ { m } }$ 的正交性容易得到

$$
\left. \begin{array} { l } { { g _ { n i } ^ { m } + g _ { n e } ^ { m } = { \displaystyle \frac { 2 n + 1 } { 4 m \pi } } \int _ { \theta = 0 } ^ { \pi } \int _ { \imath = 0 } ^ { 2 \pi } Y ( a , \theta , \lambda ) \sin { m \lambda } P _ { n } ^ { m } ( \cos \theta ) \sin ^ { 2 } \theta d \theta d \lambda } } \\ { { \displaystyle h _ { n i } ^ { m } + h _ { n e } ^ { m } = - { \displaystyle \frac { 2 n + 1 } { 4 m \pi } } \int _ { \theta = 0 } ^ { \pi } \int _ { \imath = 0 } ^ { 2 \pi } Y ( a , \theta , \lambda ) \cos { m \lambda } P _ { n } ^ { m } ( \cos \theta ) \sin ^ { 2 } \theta d \theta d \lambda } } \end{array} \right\} ,
$$

(5.107)式与(5.95)等效，即与场位W一样，已知分量Y的面值分布,可唯一确定内外场高斯系数之和。对于 $x$ 分量,这种等效性的证明不像 $\pmb { Y }$ 分量这样直接。利用公式[3]

$$
\frac { 2 n + 1 } { n ( n + 1 ) } \sin \theta \frac { d P _ { n } ^ { m } } { d \theta } = \frac { \{ ( n + 1 ) ^ { 2 } - m ^ { 2 } \} ^ { \frac { 1 } { 2 } } } { n + 1 } P _ { n + 1 } ^ { m } - \frac { ( n ^ { 2 } - m ^ { 2 } ) ^ { \frac { 1 } { 2 } } } { n } P _ { n - 1 } ^ { m }
$$

可得

$$
\begin{array} { r l r } {  { X ( a , \theta , \lambda , t _ { 0 } ) \sin \theta = \sum _ { n = 1 } ^ { \infty } \sum _ { m = 0 } ^ { n } \ [ ( g _ { n i } ^ { m } + g _ { n e } ^ { m } ) \cos m \lambda + ( h _ { n i } ^ { m } + h _ { n e } ^ { m } ) \sin m \lambda ] } } \\ & { } & { \quad \cdot \{ \frac { n ! ( n + 1 ) ^ { 2 } - m ^ { 2 } ] ^ { \frac { 1 } { 2 } } } { 2 n + 1 } \ P _ { n + 1 } ^ { m } - \frac { ( n + 1 ) ( n ^ { 2 } - m ^ { 2 } ) ^ { \frac { 1 } { 2 } } } { 2 n + 1 } \ P _ { n - 1 } ^ { m } \} , \ \quad \quad \quad ( 5 . } \end{array}
$$

将上式并项后,得

$$
\begin{array} { l } { { \displaystyle { \cal X } ( a , ~ \theta , ~ \lambda , ~ t _ { 0 } ) \sin \theta - { \displaystyle \sum _ { l = 0 } ^ { \infty } \sum _ { m = 0 } ^ { l } \left( \delta _ { l } ^ { m , * } \cos m \lambda + \delta _ { l } ^ { m , * } \sin m \lambda \right) P _ { l } ^ { m } } , } } \\ { { \displaystyle \delta _ { l } ^ { m , * } = { \displaystyle \frac { ( l - 1 ) ( l ^ { 2 } - m ^ { 2 } ) ^ { \frac { 1 } { 4 } } } { 2 l - 1 } \left( g _ { ( l - 1 ) i } ^ { m } + g _ { ( l - 1 ) i } ^ { m } \right) } } } \\ { { \displaystyle ~ - { \displaystyle \frac { ( l + 2 ) [ ( l + 1 ) ^ { 2 } - m ^ { 2 } ] ^ { \frac { 1 } { 4 } } } { 2 l + 3 } \left( g _ { ( l + 1 ) i } ^ { m } + g _ { ( l + 1 ) i } ^ { m } \right) } , } } \\ { { \displaystyle b _ { l } ^ { m , * } = { \displaystyle \frac { ( l - 1 ) ( l ^ { 2 } - m ^ { 2 } ) ^ { \frac { 1 } { 4 } } } { 2 l - 1 } \left( h _ { ( l - 1 ) i } ^ { m } + h _ { ( l - 1 ) i } ^ { m } \right) } } } \\ { { \displaystyle ~ - { \displaystyle \frac { ( l + 2 ) [ ( l + 1 ) ^ { 2 } - m ^ { 2 } ] ^ { \frac { 1 } { 4 } } } { 2 l + 3 } \left( h _ { ( l + 1 ) i } ^ { m } + k _ { ( l + 1 ) i } ^ { m } \right) } _ { 0 } } } \end{array}
$$

利用球谐函数的正交性,由(5.109)式立得

$$
b _ { l } ^ { m , c } = \frac { 2 l + 1 } { 4 \pi } \int _ { \theta = 0 } ^ { \infty } \int _ { \imath = 0 } ^ { 2 \pi } X ( a , \theta , \lambda ) P _ { l } ^ { m } \cos { m \lambda } \sin ^ { 2 } { \theta } d \theta d \lambda
$$

$$
b _ { l } ^ { m , s } = \frac { 2 l + 1 } { 4 \pi } \int _ { \theta = 0 } ^ { \pi } \int _ { \lambda = 0 } ^ { 2 \pi } X ( a , \theta , \lambda ) P _ { l } ^ { m } \sin { m \lambda } \sin ^ { 2 } \theta d \theta d \lambda
$$

即当 $\pmb { X }$ 分量的面值已知时，(5.110)，(5.111)式中的 $b _ { l } ^ { m , c } , \ b _ { l } ^ { m , s }$ 为已知量。不难看出，与待定量高斯系数 $g _ { n } ^ { m }$ 和 $\pmb { \lambda } _ { \pmb { \lambda } } ^ { m }$ 有关的方程(5.110)和(5.111)是彼此独立的,其中任何一组奇数和偶数阶高斯系数已知,不难由(5.110)和(5.111)式用递推办法求解全部高斯系数。但由于（5.109)式是一个无穷级数，除 $\mathbf { \nabla } m = 0$ 各阶高斯系数可由递推办法确定外，一般情况高斯系数的定解问题乃是无穷多个未知数的线性方程组(5.110)和(5.116)的求解问题。如果这个方程组的解存在而且是唯一的，则 $g _ { n i } ^ { m } ~ + ~ g _ { n e } ^ { m }$ 可由 $\boldsymbol { x }$ 分量的面值分布唯一确定，即证明了 $x$ 分量与场势 $\pmb { w }$ 等价。关于无穷多个未知数的线性方程组解的存在和唯一性的严格理论读者可参阅斯米尔诺夫著《高等数学教程》三卷一分册第二章第48节和五卷二分册第四章第1节。

到此我们已经从理论上解决了拉普拉斯方程(5.85)的普遍解(5.86)的定解问题,肯定了能够由地面磁场强度的分布唯一确定（5.86)中内外场的全部高斯常系数，并且给出了可供实际应用的方程(5.95)、(5.106)、(5.113)和(5.99),为地磁场的分析奠定了理论基础。但在高斯系数的实际计算中一般不采用(5.95）、（5.106)、（5.113)和(5.99)的形式,而是把地面地磁场强度的观测值 $Z \left( a , \theta , \lambda , t _ { 0 } \right) , \ Y \left( a , \theta , \lambda , t _ { 0 } \right) , \ Z \left( a , \theta , \lambda , t _ { 0 } \right)$ 分别直接代人(5.102)、(5.103)和(5.97)求解 $g _ { s i } ^ { m } , g _ { n e } ^ { m }$ 和 $\pmb { { h } } _ { m i } ^ { m } , \pmb { { h } } _ { m e } ^ { m }$ 的线性代数方程组，来确定高斯系数$g _ { i } , h _ { i } , g _ { e } , h _ { e 0 }$ 当观测点的数目足够多，特别是在同一纬度圈上测点够多时，还可采取如下具体计算步骤：首先对地球表面同一纬度的观测值 $X , \ Y , \ Z$ 进行关于经度 $\gimel$ 的傅里叶分析，即

$$
X ( a , \ \theta , \ \lambda , \ t _ { 0 } ) = \sum _ { m = 0 } ^ { \infty } \ \big ( x _ { m \xi } ^ { ( \theta ) } c o s m \lambda + x _ { m k } ^ { ( \theta ) } \sin m \lambda \big ) ,
$$

$$
\left. \begin{array} { l } { { { \displaystyle x _ { o g } ^ { ( \theta ) } = \frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } X \big ( a , ~ \theta , ~ \lambda , ~ t _ { 0 } \big ) d \lambda } } } \\ { { { \displaystyle x _ { m g } ^ { ( \theta ) } = \frac { 1 } { \pi } \int _ { 0 } ^ { 2 \pi } X \big ( a , ~ \theta , ~ \lambda , ~ t _ { 0 } \big ) \cos m \lambda d \lambda } } } \\ { { { \displaystyle x _ { m h } ^ { ( \theta ) } = \frac { 1 } { \pi } \int _ { 0 } ^ { 2 \pi } X \big ( a , ~ \theta , ~ \lambda , ~ t _ { 0 } \big ) \sin m \lambda d \lambda } } } \end{array} \right\} ,
$$

对于 $\boldsymbol { \Upsilon } , \boldsymbol { z }$ 有相同的公式,相应系数分别记作 $y _ { m g } ^ { ( \pmb { \theta } ) } , ~ y _ { m h } ^ { ( \theta ) }$ 和 $z _ { m g } ^ { ( \theta ) } , ~ z _ { m h } ^ { ( \theta ) }$ ，与此相应 $X , Y , z$ 在地球表面的表示式(5.102）、（5.103)和(5.97)可改写为

$$
\begin{array} { l } { { \displaystyle X ( a , \theta , \lambda , \iota _ { 0 } ) = \sum _ { n = 1 } ^ { \infty } a _ { n } ^ { 0 } X _ { n } ^ { 0 } ( \theta ) + \sum _ { m = 1 } ^ { \infty } \biggl \{ \biggl ( \sum _ { n = m } ^ { \infty } a _ { n } ^ { { m } } X _ { n } ^ { m } ( \theta ) \biggr ) \cos { m \lambda } } } \\ { { \displaystyle \qquad + \left( \sum _ { m = n } ^ { \infty } b _ { n } ^ { m } X _ { n } ^ { m } ( \theta ) \right) \sin { m \lambda } \biggr \} , } } \end{array}
$$

$$
Y ( a , \ \theta , \ \lambda , \ t _ { 0 } ) = \sum _ { n = 1 } ^ { \infty } a _ { n } ^ { 0 } Y _ { n } ^ { 0 } ( \theta ) + \sum _ { m = 1 } ^ { \infty } \bigg \{ \bigg ( \sum _ { n = m } ^ { \infty } a _ { n } ^ { m } Y _ { n } ^ { m } ( \theta ) \bigg ) \cos { m \lambda }
$$

$$
+ \left( \sum _ { n = m } ^ { \infty } b _ { n } ^ { m } Y _ { n } ^ { m } ( \theta ) \right) \sin m \lambda \Biggr \} ,
$$

$$
Z ( a , \ \theta , \ \lambda , \ t _ { 0 } ) = \sum _ { n = 1 } ^ { \infty } \alpha _ { n } ^ { 0 } P _ { n } ( \theta ) + \sum _ { m = 1 } ^ { \infty } \bigg \{ \bigg ( \sum _ { n = m } ^ { \infty } \alpha _ { n } ^ { m } P _ { n } ^ { m } ( \theta ) \bigg ) \cos { m \lambda }
$$

$$
+ \left( \sum _ { n = m } ^ { \infty } \beta _ { n } ^ { m } P _ { n } ^ { m } ( \theta ) \right) \sin m \lambda \Biggr \} ,
$$

其中

$$
X _ { n } ^ { m } ( \theta ) = \frac { 1 } { n } \frac { d P _ { n } ^ { m } ( \cos \theta ) } { d \theta } , Y _ { n } ^ { m } ( \theta ) = \frac { m } { n } P _ { n } ^ { m } \big ( \cos \theta \big ) ,
$$

$$
a _ { n } ^ { m } = n ( g _ { n i } ^ { m } + g _ { n e } ^ { m } ) , \quad b _ { n } ^ { m } = n ( h _ { n i } ^ { m } + h _ { n e } ^ { m } ) ,
$$

$$
\alpha _ { n } ^ { m } = n g _ { n e } ^ { m } - ( n + 1 ) g _ { n i } ^ { m } , \quad \beta _ { n } ^ { m } = h _ { n e } ^ { m } - ( n + 1 ) h _ { n i } ^ { m } ,
$$

X"(θ)、Y"(0)与连带勒让德函数的关系读者可参阅[3,p608-622],为了使用方便，施密特同时给出了X(0)和Y(θ)的函数表。比较（5.114)（包括相应的Y、Z的公式)和(5.116）、（5.117）、（5.118)可以得到

$$
x _ { o \mathscr { S } } ^ { ( \theta ) } = \sum _ { n = 1 } ^ { \infty } a _ { n } ^ { 0 } X _ { n } ^ { 0 } ( \theta ) , \quad x _ { m \mathscr { E } } ^ { ( \theta ) } = \sum _ { n = m } ^ { \infty } a _ { n } ^ { m } X _ { n } ^ { m } ( \theta ) \quad ( m > 0 ) ,
$$

$$
\begin{array} { r l } { \iota _ { o g } ^ { ( \theta ) } = \displaystyle \sum _ { n = 1 } ^ { \infty } a _ { n } ^ { 0 } \Lambda _ { n } ^ { 0 } ( \theta ) , } & { \boldsymbol { y } _ { m g } ^ { ( \theta ) } = \displaystyle \sum _ { n = m } ^ { \infty } a _ { n } ^ { m } \boldsymbol { Y } _ { n } ^ { m } ( \theta ) \quad ( m > 0 ) , } \\ { \boldsymbol { x } _ { m n } ^ { ( \theta ) } = \displaystyle \sum _ { n = 1 } ^ { \infty } b _ { n } ^ { m } \boldsymbol { Y } _ { n } ^ { 0 } ( \theta ) , } & { \boldsymbol { y } _ { m g } ^ { ( \theta ) } = \displaystyle \sum _ { n = m } ^ { \infty } a _ { n } ^ { m } \boldsymbol { Y } _ { n } ^ { m } ( \theta ) \quad ( m > 0 ) , } \end{array}
$$

$$
\begin{array} { l } { { \displaystyle y _ { m n } ^ { ( \theta ) } = \sum _ { n = m } ^ { \infty } b _ { n } ^ { m } Y _ { n } ^ { m } ( \theta ) ~ m > 0 , } } \\ { { \displaystyle z _ { n g } ^ { ( \theta ) } = \sum _ { n = 1 } ^ { \infty } \alpha _ { n } ^ { 0 } P _ { n } \big ( \cos \theta \big ) , ~ z _ { m g } ^ { ( \theta ) } = \sum _ { n = m } ^ { \infty } \alpha _ { n } ^ { m } P _ { n } ^ { m } \big ( \cos \theta \big ) ~ m > 0 , } } \\ { { \displaystyle z _ { n m } ^ { ( \theta ) } = \sum _ { n = m } ^ { \infty } \beta _ { n } ^ { m } P _ { n } ^ { m } \big ( \cos \theta \big ) ~ m > 0 } } \end{array}
$$

由 $X , Y , Z$ 的地面观测值按公式(5.115)求出不同纬度关于经度 $\gimel$ 的傅氏系数 $x _ { m g } ^ { ( \theta ) } , x _ { m h } ^ { ( \theta ) }$ 、$y _ { m g } ^ { ( \theta ) } , { y } _ { m h } ^ { ( \theta ) }$ 和 $z _ { m g } ^ { ( \theta ) } , z _ { m h } ^ { ( \theta ) }$ ，再应用线性方程组(5.122）—(5.127)求解 $a _ { n } ^ { m } \ 、 \ : b _ { n } ^ { m } \ 、 \ : \alpha _ { n } ^ { m } 、 \beta _ { n } ^ { m }$ ，最后利用(5.120）、（5.121)就可将内外场系数区分开,从而得到各级高斯常系数 $g _ { n i } ^ { m } \setminus g _ { n c } ^ { m }$ 和 $\displaystyle h _ { n i } ^ { m } \setminus h _ { n \epsilon \Theta } ^ { m }$ 实际计算中无论是由场强的观测值直接代人方程(5.116)、（5.117）、（5.118），还是先由观测值求出关于经度 $\gimel$ 的傅氏系数，再利用方程组（5.122)—(5.127）来求解高斯常系数，各公式中的 $\pmb { \mathscr { n } }$ 及相应的 $\pmb { m }$ 都不可能是无限的。这相应于用有限项级数代替关于场的无穷级数。显然这种近似的可能性取决于场的级数展开式（5.86)的收敛性。实际分析表明，级数(5.86)收敛是迅速的， $\pmb { n } = 1$ 的级数项约占 $8 0 - 8 5 \%$ 。正是这种迅速的收敛性,保证了理论上完备的高斯分析能够用于地磁场的分析实际。若级数最高阶数取为 $\pmb { n }$ ，则全部高斯系数的个数为 $2 n ( n + 2 )$ ，系数 $a _ { n } ^ { m } \setminus b _ { n } ^ { m }$ 和 $\alpha _ { n } ^ { m } \setminus \beta _ { n } ^ { m }$ 的个数相同，各为 $n ( n + 2 )$ ，每个测点可以提供两个关于 $a _ { n } ^ { m } , b _ { n } ^ { m }$ 的方程 $( X , Y )$ ，一个 $\alpha _ { n } ^ { m } \setminus \beta _ { n } ^ { m }$ 的方程(Z)，因此要确定全部$2 n ( n + 2 )$ 个高斯系数至少必须有 $n ( n + 2 )$ 个三分量的测点。实际计算中，观测点的数目必须远大于上述极限数目,这一方面是因为观测点数够多，可以提供较多的方程，利用最小二乘法解有关方程组，可以保证常系数的精度；容易证明，若每个测点以所代表的面积加权，则利用加权最小二乘法求解有关方程组等效于用求和代替积分(5.95)、（5.99)，因此足够的测点和全球较为合理的分布可以近似满足球谐函数的正交关系，以尽可能保证实际计算中各阶高斯系数的独立性。关于后一点往往被人忽视，他们把高斯分析仅仅理解为解方程组（5.116)、（5.117）或（5.118)，用局部有限的测点去求高斯系数并区分内外场。对此这里有特别强调之必要。设在地球表面某一区域S有n个测点，(5.116)和（5.118）中各包含 $\pmb { n }$ 个待定系数 $a _ { n } ^ { m } , b _ { n } ^ { m }$ 和 ${ \pmb { \alpha } } _ { n } ^ { m } , { \pmb { \beta } } _ { n } ^ { m }$ ，则(5.116)和(5.118)将各提供 $\pmb { n }$ 个独立的方程。为方便将方程组形式改写为

$$
( \alpha _ { i j } ) \left( \begin{array} { l } { x _ { 1 } } \\ { x _ { 2 } } \\ { \vdots } \\ { \vdots } \\ { x _ { n } } \end{array} \right) = \left( \begin{array} { l } { b _ { 1 } } \\ { b _ { 2 } } \\ { \vdots } \\ { \vdots } \\ { b _ { n } } \end{array} \right) ,
$$

其中常数bn为测点磁场值X(a,θ,λ,t）或Z(a,θ,λ,t)，xn为待定系数a、b”或α、β，（αii）为n阶系数矩阵，其元素αii由 $\begin{array} { l } { { \cos m \lambda _ { \atop { \sin m \lambda } } P _ { \it \ / n } ^ { m } ( \cos \theta ) } } \end{array}$ 或 $\begin{array} { l } { \cos m \lambda } \\ { \sin m \lambda } \end{array} \textstyle X _ { n } ^ { m } ( \theta )$ 确定， $\lambda ,$ θ∈S,若测点数多于n,则(5.128)是正则化后的“阶线性方程组。设在区域S，系数矩阵(αii）中第l列和第n列元素近似相等(或线性相关),即

$$
\alpha _ { i l } \approx \alpha _ { i n } , ~ ( i = 1 , 2 , \cdot \cdot \cdot , n ) _ { \circ }
$$

其余列（或行)线性无关。因区域S局限于地表的某一局部区域，(5.129)式成立是可能的，例如像图5.7所示，在区间 $0 \leqslant \theta \leqslant 6 0 ^ { \circ }$ ， $P _ { 2 } ^ { 2 }$ 和 $P _ { 3 } ^ { 2 }$ ， $X _ { 3 } ^ { 0 } ( \theta )$ 和 $X _ { 2 } ^ { 0 } ( \theta )$ 差别不大，因此对同一经度，方程(5.116)中待定常数a²和a的系数以及b和b的系数近似相等；方程(5.118）中 $\alpha _ { 2 } ^ { 0 } , \beta _ { 2 } ^ { 0 }$ 分别与 $\alpha _ { 3 } ^ { 0 } , \beta _ { 3 } ^ { 0 }$ 项的系数近似相等。若(5.129)式成立，则方程组(5.128)系数行列式 $\lvert \alpha _ { i j } \rvert = 0$ ，矩阵 $( \alpha _ { i j } )$ 的秩为 $\mathbf { \Omega } _ { \pmb { n } } - 1$ ，方程组（5.128）有解的充分必要条件是其特征行列式

![](images/d0b901dd9589727945b6bc4cdb5a8d92fbfcd0a99782f368310c47b78753bdc2.jpg)  
图5.7

$$
\left| \begin{array} { l l l l l } { a _ { 1 1 } } & { a _ { 1 2 } } & { \cdots } & { a _ { 1 } , _ { n - 1 } } & { b _ { 1 } } \\ { a _ { 2 1 } } & { a _ { 2 2 } } & { \cdots } & { a _ { 2 } , _ { n - 1 } } & { b _ { 2 } } \\ & & { \cdots \cdots \cdots } & & \\ & & & { \ddots } & \\ { a _ { n - 1 } , } & { a _ { n - 1 } , _ { 2 } } & { \cdots } & { a _ { n - 1 , n - 1 } } & { b _ { n - 1 } } \\ { a _ { n } , _ { 1 } } & { a _ { n } , _ { 2 } } & { \cdots } & { a _ { n } , _ { n - 1 } } & { b _ { n } } \end{array} \right| = 0 ,
$$

不难看出，只有当(5.118)或(5.116)中所取项数“已近似或完全描述了真实磁场时，条件(5.130)才能成立。很显然，若(5.130)式成立，则方程组(5.128)有无穷多组解，只有xi，x,，(x+𝑥n)，xα才是唯一确定的。这表明,当(5.129)式成立时，即使满足条件(5.130),也无法由观测值根据(5.116）、(5.118）确定全部高斯系数。因此可以得出，只有当：第一,在局部区域S内,磁场所包含的全部球谐项已知(在一定的精度范围),以保证线性方程组(5.128)的所有特征行列式的秩与行列式的秩相同,即(5.130)式成立;第二，各球谐函数间在区域S内有明显差异,即没有任何两个不同球谐函数满足(5.129)式，两个条件都具备时在区域S内做球谐分析才是可能的。否则由(5.116)、(5.118)计算所得全部系数,无论与实测值符合多好,磁场表达式(5.116)、(5.118）只能是一种插值表示方法，而不再具有上述高斯分析的意义。换句话说，即这样求得的“高斯系数”只在二维公式(5.116)、(5.118)中才有意义,而在三维公式(5.86)、(5.100）、(5.101)中不再具有任何意义了。但当S扩展到全部球面,且测点分布较为均匀合理时,即使(5.116)、(5.118)中不包括全部球谐项,即条件(5.130)不满足,方程组(5.128)的解仍然是唯一确定的。

如前所述，高斯系数gi、h;和g.、h具有明确的物理意义，分别代表地球内部和外部场源所产生的磁场，地磁场高斯分析的结果表明，在地球表面地磁场的绝大部分来源于地球内部，外源部分仅占万分之几到千分之几偶尔可达百分之几，因此高斯理论的成功，除了给出地磁场严格的数学表述外，还在于它把几百年来人们只能猜测的关于地磁场来源所在地的问题，变成了可以通过分析做出客观判断的现实课题。高斯理论的建立和实际分析的结果,证实了早在1600年吉尔伯特关于地球是一个大磁体的论断。地磁场还随时间不断地变化,因此不同时间的地磁场所确定的高斯系数是不同的,即高斯系数是时间$\pmb { \mathscr { t } }$ 的函数。地磁场随时间的变化有缓慢变化和较快速变化两类。来源于地球内部，基本上稳定,只随时间非常缓慢变化的成分,是地磁场的主要部分,称为地球的“基本磁场”;来源于高空,随时间变化较快的成分,称为地球的"变化磁场”。下面将分述基本磁场和变化磁场时空变化的基本形态。

# 三、地球的基本磁场及其长期变化

# （一）地球的基本磁场

# 1.基本磁场的高斯分析和地磁图

基本磁场是地磁场中的稳定部分，在现有的精度范围内，可以认为地球基本磁场全部来源于地球内部。这样，上述球谐分析各公式中与外源场有关的高斯系数 ${ \pmb g } _ { \pmb { c } }$ 和 $\pmb { \hat { h } _ { e } }$ 全部为零。省略表示内源场的脚标 $\pmb { i }$ ，则公式(5.86)、(5.87)、(5.100）(5.101)简化为

$$
W ( r , \theta , \lambda ) = a \sum _ { n = 1 } ^ { \infty } \sum _ { m = 0 } ^ { n } \bigg [ \bigg ( \frac { a } { r } \bigg ) ^ { n + 1 } \big ( g _ { n } ^ { m } \cos m \lambda + h _ { n } ^ { m } \sin m \lambda \big ) P _ { n } ^ { m } \big ( \sin \theta \big ) \bigg ] ,
$$

$$
\begin{array} { r } { X ( r , \theta , \lambda ) = \displaystyle \sum _ { n = 1 } ^ { \infty } \sum _ { m = 0 } ^ { n } [ ( \frac { a } { r } ) ^ { n + 2 } ( g _ { n } ^ { m } \cos m \lambda   } \\ {   +  h _ { n } ^ { m } \sin m \lambda ) \frac { d P _ { n } ^ { m } ( \cos \theta ) } { d \theta } ] } \end{array}
$$

$$
\begin{array} { r } { Y ( r , \theta , \lambda ) = \underset { n = 1 } { \overset { \infty } { \sum } } \underset { m = 0 } { \overset { n } { \sum } } \left[ \left( \frac { a } { r } \right) ^ { n + 2 } \left( g _ { n } ^ { m } \sin m \lambda \right. \right. } \\ { \left. \left. + h _ { n } ^ { m } \cos m \lambda \right) \frac { m } { \sin \theta } P _ { n } ^ { m } ( \cos \theta ) \right] } \end{array}
$$

$$
+ \left. h _ { n } ^ { m } \sin m \lambda \right) P _ { n } ^ { m } ( \cos \theta ) \Biggr ]
$$

关于高斯系数 $g , h$ 的确定，本章第1，2节所述理论和方法全部适用。只是这里， $W , X$ 、$\mathbf { Y }$ 和 $\mathbf { z }$ 之中任何一个量在地球表面的分布已知,都可唯一确定(5.131)或(5.132)中的全部高斯系数。这相应于拉普拉斯方程第一边值（已知 $\pmb { W }$ 或 $x , y )$ 和第二边值（已知 $z$ ）问题,与第1,2节定解问题的这种差异,是由于这里没有外源场，相应外部边界条件为无穷远点,而这种无穷远点的自然边界条件，解(5.131)已经自然满足。实际计算中，当最高阶数取为 $\pmb { n }$ 时，这里球谐系数的总数为 $\pmb { n } ( \pmb { n } + 2 )$ ，只要有 $\pmb { n } ( \pmb { n } + 2 )$ 个独立的方程，就能确定全部高斯系数。地磁场的球谐分析除采用上述球极坐标外，施密特和阿达姆斯（Adams)等人还曾考虑地球扁率的影响。但计算结果两者差异并不显著[3[。表5.7列出了不同年代低阶高斯系数的结果。

五十年代末和六十年代，随着全球范围，特别是航空、海上和卫星地磁测量的发展,大大丰富了人们对于地磁场空间分布的认识，为全球范围的基本磁场的分析提供了良好的条件。但由于人们占有资料的不同，这种分析结果会有明显的差异。全球性的分析结果是判断区域性和局部地区地磁异常的标准,应能客观地反映全球范围地磁场的基本特征。为此国际地磁和高空物理协会（IAGA）除成立世界地磁测量（WMS）的国际合作机构负责协调各国陆上、海上、航空和卫星测量任务外，还于1968年10月在华盛顿召开的专门会议上提出并通过了1965.0年代的国际地磁参考场(IGRF)，做为全世界通用的正常地磁场的标准]。1965.0年代的国际地磁参考场取 $\pmb { n } = 8$ 共80个高斯系数，表5.2,由公式(5.131）、(5.132)给出。它的有效期是1965.0一1975.0,其他年代的高斯系数

表5.1 $\scriptstyle { \pmb { n } } = { \pmb { 2 } }$ 阶高斯系数（单位 $_ { r }$ ）  

<table><tr><td>作</td><td>年代</td><td>g</td><td>g</td><td>h</td><td>g</td><td>g</td><td>H</td><td>gi</td><td>h</td></tr><tr><td>Er man Petexsen</td><td>1829</td><td>-3201</td><td>-284</td><td>691</td><td></td><td>257</td><td>-4</td><td>-14</td><td>146</td></tr><tr><td>Gauss</td><td>1835</td><td>-3235</td><td>-311</td><td>625</td><td>51</td><td>292</td><td>12</td><td>12</td><td>157</td></tr><tr><td>Adams</td><td>1845</td><td>-3219</td><td>-278</td><td>578</td><td>9</td><td>284</td><td>-10</td><td>4</td><td>135</td></tr><tr><td>Adams</td><td>1880</td><td>-3168</td><td>-243</td><td>603</td><td>-49</td><td>297</td><td>-75</td><td>61</td><td>149</td></tr><tr><td>Schmidt</td><td>1885</td><td>-3168</td><td>- 222</td><td>595</td><td>-50</td><td>278</td><td>-71</td><td>65</td><td>149</td></tr><tr><td>Futsche</td><td>1885</td><td>-3164</td><td>-241</td><td>591</td><td>-35</td><td>286</td><td>-75</td><td>68</td><td>142</td></tr><tr><td>Neumeyer Peterson</td><td>1885</td><td>-3157</td><td>-248</td><td>603</td><td>-53</td><td>288</td><td>-75</td><td>65</td><td>146</td></tr><tr><td>Dyson、Furner</td><td>1922</td><td>-3095</td><td>-226</td><td>592</td><td>-89</td><td>299</td><td>-124</td><td>144</td><td>84</td></tr><tr><td> Jones Melotte</td><td>1942</td><td>-3039</td><td>-218</td><td>555</td><td>-117</td><td>294</td><td>-150</td><td>157</td><td>51</td></tr><tr><td>Afauasieva</td><td>1945</td><td>-3032</td><td>-229</td><td>590</td><td>-125</td><td>288</td><td>-146</td><td>150</td><td>48</td></tr><tr><td>Vestine et al.</td><td>1945</td><td>-3057</td><td>-221</td><td>581</td><td>127</td><td>296</td><td>-166</td><td>164</td><td>54</td></tr><tr><td>Finch, Leaton</td><td>1955</td><td>-3055</td><td>-227</td><td>590</td><td>-152</td><td>303</td><td>-190</td><td>158</td><td>24</td></tr><tr><td>Cain et al.</td><td>1965</td><td>-3040.1</td><td>-216.4</td><td>577.8</td><td>-154.0</td><td>299.8</td><td>-193.2</td><td>159.0</td><td>20.3</td></tr><tr><td>Leaton et al.</td><td>1965</td><td>-3037.5</td><td>-208.7</td><td>576.9</td><td>-164.8</td><td>295.4</td><td>-199.5</td><td>157.9</td><td>11.6</td></tr></table>

表5.21965.0年代国际地磁参考场的高斯系数[]  

<table><tr><td colspan="2"></td><td colspan="2">基本磁场</td><td colspan="2">长期变化</td><td colspan="2"></td><td colspan="2">基本磁场</td><td colspan="2">长期变化</td></tr><tr><td>D</td><td>m</td><td>g（x）</td><td>(）</td><td></td><td>h （x/年）</td><td>0</td><td>m</td><td>g（x）</td><td>h（x）</td><td></td><td>h （2/年）</td></tr><tr><td>1</td><td>0</td><td>-30339</td><td></td><td>15.3</td><td></td><td>6</td><td>2</td><td>4</td><td>106</td><td>1.1</td><td>10.4</td></tr><tr><td>1</td><td>1</td><td>-2123</td><td>5758</td><td>8.7</td><td>12.3</td><td>6</td><td>3</td><td>-229</td><td>68</td><td>1.9</td><td>2.0</td></tr><tr><td>2</td><td>0</td><td>-1645</td><td></td><td>-24.4</td><td></td><td>6</td><td>4</td><td>3</td><td>132</td><td>10.4</td><td>-1.1</td></tr><tr><td>2</td><td>1</td><td>2994</td><td>-2006</td><td>0.3</td><td>-11.8</td><td>6</td><td>5</td><td>14</td><td>-10</td><td>10.4</td><td>0.1</td></tr><tr><td>2</td><td>2</td><td>1567</td><td>130</td><td>-1.6</td><td>-16.7</td><td>6</td><td>6</td><td>-112</td><td>-13</td><td>-0.2</td><td>0.9</td></tr><tr><td>3</td><td>0</td><td>1297</td><td></td><td>0.2</td><td></td><td>7</td><td>0</td><td>71</td><td></td><td>10.5</td><td></td></tr><tr><td>3</td><td>1</td><td>-2036</td><td>-403</td><td>-10.8</td><td>4.2</td><td>7</td><td>1</td><td>-54</td><td>-57</td><td>10.3</td><td>-1.1</td></tr><tr><td>3</td><td>2</td><td>1289</td><td>242</td><td>0.7</td><td>0.7</td><td>7</td><td>2</td><td>0</td><td>-27</td><td>10.7</td><td>0.3</td></tr><tr><td>3</td><td>3</td><td>843</td><td>-176</td><td>13.8</td><td>-7.7</td><td>7</td><td>3</td><td>12</td><td>18</td><td>10.5</td><td>0.4</td></tr><tr><td>4</td><td>0</td><td>958</td><td></td><td>10.7</td><td></td><td>7</td><td>4</td><td>125</td><td>9</td><td>0.3</td><td>0.2</td></tr><tr><td>4</td><td>1</td><td>805</td><td>149</td><td>0.2</td><td>10.1</td><td>7</td><td>5</td><td>19</td><td>23</td><td>0.0</td><td>0.4</td></tr><tr><td>4</td><td>2</td><td>492</td><td>-208</td><td>13.0</td><td>1.6</td><td>7</td><td>6</td><td>13</td><td>-19</td><td>10.2</td><td>0.2</td></tr><tr><td>4</td><td>3</td><td>-392</td><td>8</td><td>10.1</td><td>2.9</td><td>7</td><td>7</td><td>12</td><td>-17</td><td>10.6</td><td>0.3</td></tr><tr><td>4</td><td>4</td><td>256</td><td>-265</td><td>12.1</td><td>14.2</td><td>8</td><td>0</td><td>10</td><td></td><td>0.1</td><td></td></tr><tr><td>5</td><td>0</td><td>-223</td><td></td><td>1.9</td><td></td><td>8</td><td>1</td><td>9</td><td>3</td><td>0.4</td><td>0.1</td></tr><tr><td>5</td><td>1</td><td>357</td><td>16</td><td>1.1</td><td>2.3</td><td>8</td><td>2</td><td>13</td><td>-13</td><td>0.6</td><td>10.2</td></tr><tr><td>5</td><td>2</td><td>246</td><td>125</td><td>2.9</td><td>1.7</td><td>8</td><td>3</td><td>-12</td><td>5</td><td>0.0</td><td>10.3</td></tr><tr><td>5</td><td>3</td><td>126</td><td>-123</td><td>0.6</td><td>12.4</td><td>8</td><td>4</td><td>14</td><td>-17</td><td>0.0</td><td>10.2</td></tr><tr><td>5</td><td>4</td><td>-161</td><td>-107</td><td>0.0</td><td>0.8</td><td>8</td><td>5</td><td>7</td><td>4</td><td>10.1</td><td>10.3</td></tr><tr><td>5</td><td>5</td><td>151</td><td>77</td><td>1.3</td><td>10.3</td><td>8</td><td>6</td><td>15</td><td>22</td><td>0.3</td><td>10.4</td></tr><tr><td>6</td><td>0</td><td>47</td><td></td><td>10.1</td><td></td><td>8</td><td>7</td><td>12</td><td>13</td><td>10.3</td><td>10.3</td></tr><tr><td>6</td><td>1</td><td>60</td><td>-14</td><td>10.3</td><td>10.9</td><td>8</td><td>8</td><td>6</td><td>-16</td><td>10.5</td><td>10.3</td></tr></table>

![](images/cb96fbd8bd1b17e684e0e3ac671975ece83b09551b9b99f02d43c17f731f1ecc.jpg)

![](images/c1770ec93b5add95b0259a112c007e4e7a8bcbbee67a8686a8c35736e8ad243e.jpg)  
图5.8

$$
G _ { n } ^ { m } ( t ) = G _ { n } ^ { m } ( t _ { 0 } ) + \dot { G } _ { n } ^ { m } ( t - t _ { 0 } )
$$

其中 $\iota _ { 0 } = 1 9 6 5 . 0$ ， $\dot { G } _ { n } ^ { m }$ 是高斯系数的年变率,单位为伽吗/年,表 ${ \boldsymbol { 5 . 2 } } _ { \circ }$

表5.3是1975.0年代国际地磁参考场80项高斯系数和年变率的数值。它是国际地磁和高空物理协会（IAGA）在1975年8月全体会议上通过的，使用期是1975.0一$1 9 8 0 . 0 ^ { 1 6 ] }$ 。

需要指出，因人们占有资料的不同和资料精度的差异,上述做为地磁正常场标准的地磁场模型也有不同,如1975.0年代的模型除 IGRF 外尚有（IGS75）模型和AWC75模型[8]，目前各国地磁学家，特别是国际地磁和高空物理协会第一分组，正从资料的选取和方法的改进上致力于完善统一这些模型。

以上关于地磁场的数学表述,把空间分布复杂的地磁场,成功地统一于一个数学解析表达式(5.131)、(5.132)，这对于实际应用和理论计算都是很方便的。但这种抽象的描述不能给出地磁场分布和变化的直观图像，地磁图就是地磁场直观图像的一种好的表示方法。

把第2节所述地磁台和已归算到特定时刻的野外测点各地磁要素的数值，标绘于地图上，再把数值相等的点用曲线连起来构成一幅相应要素的等值线图，通常称作地磁图。它包括等偏图（偏角 $_ { D }$ )，等倾图（倾角 $\pmb { I }$ ）和等强度图 $( X , Y , Z , H , F )$ 。图5.8(a)一(d）是水平强度 $\pmb { H }$ ，偏角 $D$ ，倾角1，垂直强度Z1965.0年代的世界地磁图。地磁图也可以由高斯系数,按公式(5.132)和(5.96)计算得到相应年代各地地磁要素的数值编绘而成。

表5.31975.0年代国际地磁参考场的高斯系数[6]  

<table><tr><td colspan="2"></td><td colspan="2">基本磁场</td><td colspan="2">长期变化</td><td colspan="2"></td><td colspan="2">基本磁场</td><td colspan="2">长期变化</td></tr><tr><td>0</td><td>m</td><td>g(r）</td><td>h（x）</td><td></td><td>h （x/年）</td><td>Ⅱ</td><td>m</td><td>g（x）</td><td>h(x）</td><td>g</td><td>（r/年）</td></tr><tr><td>1</td><td>0</td><td>-30186</td><td></td><td>25.6</td><td></td><td>6</td><td>2</td><td>15</td><td>102</td><td>2.0</td><td>10.1</td></tr><tr><td>1</td><td>1</td><td>-2036</td><td>5735</td><td>10.0</td><td>-10.2</td><td>6</td><td>3</td><td>-210</td><td>88</td><td>2.8</td><td>10.2</td></tr><tr><td>2</td><td>0</td><td>-1898</td><td></td><td>-24.9</td><td></td><td>6</td><td>4</td><td>-1</td><td>143</td><td>0.0</td><td>11.3</td></tr><tr><td>2</td><td>1</td><td>2997</td><td>-2124</td><td>0.7</td><td>13.0</td><td>6</td><td>5</td><td>18</td><td>19</td><td>0.9</td><td>0.7</td></tr><tr><td>2</td><td>2</td><td>1551</td><td>-37</td><td>4.3</td><td>-18.9</td><td>6</td><td>6</td><td>-114</td><td>-4</td><td>10.1</td><td>1.7</td></tr><tr><td>3</td><td>Q</td><td>1299</td><td></td><td>13.8</td><td></td><td>7</td><td>0</td><td>66</td><td></td><td>0.0</td><td></td></tr><tr><td>3</td><td>1</td><td>-2144</td><td>-361</td><td>-10.4</td><td>6.9</td><td>7</td><td>1</td><td>-57</td><td>-68</td><td>0.0</td><td>-1.4</td></tr><tr><td>3</td><td>2</td><td>1296</td><td>249</td><td>-4.1</td><td>2.5</td><td>7</td><td>2</td><td>17</td><td>-24</td><td>0.0</td><td>10.1</td></tr><tr><td>3</td><td>3</td><td>805</td><td>-253</td><td>14.2</td><td>15.0</td><td>7</td><td>3</td><td>7</td><td>14</td><td>0.6</td><td>0.3</td></tr><tr><td>4</td><td>0</td><td>951</td><td></td><td>10.2</td><td></td><td>7</td><td>4</td><td>122</td><td>11</td><td>0.9</td><td>0.3</td></tr><tr><td>4</td><td>1</td><td>807</td><td>148</td><td>12.0</td><td>5.0</td><td>7</td><td>5</td><td>19</td><td>27</td><td>0.3</td><td>10.7</td></tr><tr><td>4</td><td>2</td><td>462</td><td>-264</td><td>13.9</td><td>0.8</td><td>7</td><td>6</td><td>1</td><td>-17</td><td>0.3</td><td>0.1</td></tr><tr><td>4</td><td>3</td><td>-393</td><td>39</td><td>-2.1</td><td>1.7</td><td>7</td><td>7</td><td>18</td><td>-14</td><td>10.5</td><td>0.8</td></tr><tr><td>4</td><td>4</td><td>235</td><td>-307</td><td>-3.1</td><td>11.0</td><td>8</td><td>0</td><td>11</td><td></td><td>0.2</td><td></td></tr><tr><td>5</td><td>0</td><td>-204</td><td></td><td>0.3</td><td></td><td>8</td><td>1</td><td>13</td><td>4</td><td>0.3</td><td>10.2</td></tr><tr><td>5</td><td>1</td><td>368</td><td>39</td><td>10.7</td><td>1.2</td><td>8</td><td>2</td><td>3</td><td>-15</td><td>0.0</td><td>10.4</td></tr><tr><td>5</td><td>2</td><td>275</td><td>142</td><td>1.1</td><td>2.3</td><td>8</td><td>3</td><td>-12</td><td>2</td><td>0.2</td><td>10.2</td></tr><tr><td>5</td><td>3</td><td>120</td><td>-147</td><td>-1.6</td><td>12.0</td><td>8</td><td>4</td><td>-4</td><td>-19</td><td>10.4</td><td>0.3</td></tr><tr><td>5</td><td>4</td><td>-161</td><td>199</td><td>10.5</td><td>1.3</td><td>8</td><td>5</td><td>6</td><td>1</td><td>10.3</td><td>0.4</td></tr><tr><td>5</td><td>5</td><td>138</td><td>74</td><td>1.0</td><td>1.1</td><td>8</td><td>6</td><td>12</td><td>18</td><td>0.6</td><td>10.3</td></tr><tr><td>6</td><td>0</td><td>46</td><td></td><td>0.2</td><td></td><td>8</td><td>7</td><td>9</td><td>16</td><td>10.3</td><td>10.6</td></tr><tr><td>6</td><td>1</td><td>57</td><td>-23</td><td>0.5</td><td>0.5</td><td>8</td><td>8</td><td>1</td><td>-19</td><td>10.1</td><td>0.3</td></tr></table>

![](images/e51641d22d612d4d65192a18e2d15c2d2b30e0274c605a5080c2be5ff15c0132.jpg)  
图5.91965.0年代国际地磁参考场（F)[)

图5.9是由表5.3高斯系数计算编绘的1965.0年代的国际地磁参考场总强度 $\pmb { F }$ 等值图。  
鉴于地磁场有缓慢的长期变化，地磁图一般每5一10年编绘一次。

地磁图上倾角为 $9 0 ^ { \circ }$ ，水平强度为零的点(实际上是一个小的区域（图 $5 . 8 ( \mathrm { c } ) ) )$ 称为磁极（magnetic pole)。由偏角的定义不难相信，等偏线将汇集于地磁南北极和地理南北极四个点。1965.0年代的北磁极和南磁极分别位于 $7 4 . 9 ^ { o } \mathrm { N } , 1 0 1 . 0 ^ { o } \mathrm { W } ; 6 7 . 1 ^ { \circ } \mathrm { S } , 1 4 2 . 7 ^ { \circ } \mathrm { E } _ { \circ }$ 倾角为零的等值线称为磁倾赤道。由各地磁倾角按偶极磁场模式(见第3节)

$$
\mathfrak { t a n } \phi = \frac { 1 } { 2 } \mathfrak { t a n } I
$$

所计算的纬度 $\pmb { \phi }$ 称为磁倾纬度。

地磁场的球谐分析和地磁图描述了地磁场主要部分的空间分布，以下我们将分述这种空间分布的主要特征。

# 2.中心偶极子磁场和地磁坐标

如前所述球谐分析中 $\pmb { n } \ll 1$ 的项，约占全部磁场的 $8 0 \mathrm { - } 8 5 \%$ ，代表了地磁场空间分布的主要特征。由下面的分析可以看出,它相当于一个在地心按一定方位放置、磁矩为M的偶极子所产生的磁场，这个偶极子称为“中心偶极子”。这就是通常所说的均匀磁化(总磁化强度为M)球体的磁场，因为一个均匀磁化的球体与一个中心偶极子在球外所产生的磁场是一样的。

由(5.131),取 $n = 1$ ，其磁位

$$
W = a \left( { \frac { a } { r } } \right) ^ { 2 } [ g _ { 1 } ^ { \ L \ L } \mathrm { c o s } \theta + g _ { 1 } ^ { \ L \ L } \mathrm { s i n } \theta \mathrm { c o s } \lambda + h _ { 1 } ^ { \ L \ L } \mathrm { s i n } \theta \mathrm { s i n } \lambda ] _ { o }
$$

取如图5.10所示坐标系， $o$ 为地心， $O z$ 与极轴重合指向地理北极， $_ { x y }$ 为赤道平面，$_ { o x }$ 指向格林尼冶子午圈。考察 $^ o$ 点一轴向偶极子 $M _ { z }$ 在观测点 $\pmb { P }$ 所产生的磁场，设其磁势为 $W _ { P }$ ，

$$
{ \cal W } _ { P } = \ ^ { M _ { z } \cos \theta } ,
$$

与(5.135)比较可得

$$
M _ { z } = a ^ { 3 } g _ { 1 } ^ { 0 } ,
$$

因此，（5.135）与 $g _ { 1 } ^ { 0 }$ 有关的项相当于一个地心轴向偶极子的磁场，其磁矩与 $g _ { 1 } ^ { 0 }$ 的关系由$( 5 . 1 3 7 _ { 1 } )$ 确定。

设在地心沿赤道平面放置一偶极子Mε，Mε与x轴的夹角为λ，则其磁势We为

$$
W _ { E } = { \frac { M _ { E } \cdot \mathbf { \nabla } r } { r ^ { 3 } } } = { \frac { M _ { x } x + M _ { y } y } { r ^ { 3 } } } ,
$$

x、y为观测点P(r,0,)的向径r的坐标分量(图5.10),由坐标关系

$$
\begin{array} { r } { x = r \sin \theta \cos \lambda , \quad y = r \sin \theta \sin \lambda , } \end{array}
$$

得到

$$
\begin{array} { r } { \dot { \boldsymbol { W } } _ { E } = \ \frac { M _ { x } } { r ^ { 2 } } \sin \theta \cos \lambda + \frac { M _ { y } } { r ^ { 2 } } \sin \theta \sin \lambda , } \end{array}
$$

与(5135)比较可得：

$$
M _ { x } = a ^ { 3 } g _ { 1 } ^ { 1 } ; ~ M _ { y } = a ^ { 3 } h _ { 1 0 }
$$

![](images/f823e2eede8287cb26a3eb45730e554a99f452986440097bb2a616a24b197c93.jpg)  
图5.10

![](images/8fd944f19e159930c9a756de3fd9a85c7f0a2007e6d1ab9959917ea03ac695d7.jpg)  
图5.11

即（5.135）中与 ${ \pmb g _ { 1 } ^ { 1 } }$ 和 $\pmb { h } _ { 1 } ^ { 1 }$ 有关的项相当于一个在赤道平面放置的中心偶极子的磁场，其偶极子强度与高斯系数的关系由 $( 5 . 1 3 7 _ { 2 } )$ 式确定。

综合(5.136)、(5.137)可以看出，与球谐分析 $\pmb { n } = 1$ 相应的磁场(5.135)等效于一个中心偶极子的磁场,偶极子的强度

$$
M = a ^ { 3 } [ ( g _ { 1 } ^ { 0 } ) ^ { 2 } + ( g _ { 1 } ^ { 1 } ) ^ { 2 } + ( h _ { 1 } ^ { 1 } ) ^ { 2 } ] ^ { \frac { 1 } { 2 } } ,
$$

偶极子的方位 $( \theta _ { 0 } , \lambda _ { 0 } )$

$$
\left. \begin{array} { l } { \tan \theta _ { 0 } = \frac { \lfloor \left( g _ { 1 } ^ { 1 } \right) ^ { 2 } + \left( h _ { 1 } ^ { 1 } \right) ^ { 2 } \rfloor ^ { 1 / 2 } } { g _ { 1 } ^ { 0 } } , } \\ { \tan \lambda _ { 0 } = \frac { \displaystyle h _ { 1 } ^ { 1 } } { \displaystyle g _ { 1 } ^ { 1 } } } \end{array} \right\}
$$

当由观测值的球谐分析（5.131）、（5.132）确定了高斯系数 $g _ { 1 } ^ { 0 } , \ g _ { 1 } ^ { 1 }$ 和 $\pmb { h } _ { 1 } ^ { 1 }$ 后，便可由(5.138）和(5.139)计算中心偶极子的强度和方向。由 $^ o$ 到 $( \theta _ { 0 } , \lambda _ { 0 } )$ 的连线叫做磁轴，磁轴与地面的交点叫做地磁极(geomagnetic pole)。必须注意,这里所说的地磁极与第3节中由地磁图所定义的磁极（magneticpole）位置和名称都不相同。由地磁极的定义可知地磁南北极一定是球对称的，磁北极和磁南极则不一定有这种对称性。根据1965.0年代国际地磁参考场的高斯系数gi、gi和hi按（5.139）式计算的地磁极的位置是：地磁北极$7 8 . 6 ^ { \circ } \mathbf { N }$ ， $\mathbf { 6 9 . 8 ^ { \circ } W }$ ，位于格陵兰岛,地磁南极 $7 8 . 6 ^ { \circ } { \bf S }$ ， $1 1 0 . 2 ^ { \circ } \mathbf { E }$ ,在南极大陆内。

许多与地磁场有关的物理现象不是相对于地理轴而是相对于地磁轴有明显的对称性，这种现象用地磁坐标描述是方便的。地面一点地磁坐标的定义是：观测点的向径r与地磁轴的夹角定义为地磁余纬，过观测点和地磁极的子午面与过地磁极和地理极的子午面的夹角定义为地磁经度A。若已知地磁极M的地理坐标（0。，φ）和观测点P的地理坐标(0，φ)。由图5.11所示球面三角形 NMP可求出P点的地磁坐标(0,A)，在球面三角形NMP中：

$$
\begin{array} { l } { \widehat { N M } = \theta _ { 0 } , \widehat { N P } = \theta } \\ { \widehat { M P } = \theta , \angle M N P = \lambda - \lambda _ { 0 } } \\ { \angle P M N = 1 8 0 ^ { \circ } - \Lambda } \end{array}
$$

由球面三角余弦和正弦定理

$$
\left. \begin{array} { c } { { \cos \Theta = \cos \theta \cos \theta _ { 0 } + \ \sin \theta \sin \theta _ { 0 } \cos \left( \lambda - \lambda _ { 0 } \right) } } \\ { { \sin A = \frac { \sin \theta \sin \left( \lambda - \lambda _ { 0 } \right) } { \sin \theta } } } \end{array} \right\}
$$

便可计算出 $\pmb { P }$ 点的地磁坐标 $\left( \Theta , \Lambda \right)$ 。这样计算的地磁纬度和由(5.134)式所定义的磁倾纬度不同，磁倾纬度是由实测倾角值计算得到。

和地磁坐标相应可定义地磁时，太阳两次经过观测点所在磁子午面的时间（上中天，下中天)定义为地磁午夜和正午的时间。磁时常用角度表示，即某一时刻太阳所在磁子午面与过观测点的磁子午面的夹角为这一点该时刻的地方磁时。若采用地磁坐标，则(5.135）简化为

$$
{ \cal W } ( r , \Theta , A ) = a \left( \frac { a } { r } \right) ^ { 2 } G _ { 1 } ^ { 0 } \cos \Theta
$$

其中 $G _ { 1 } ^ { 0 }$ 是新坐标系中的高斯系数。由(5.141)可得

$$
\left. \begin{array} { l } { { Z = \displaystyle \frac { \partial { \cal W } } { \partial r } = - 2 \left( \frac { a } { r } \right) ^ { 3 } G _ { 1 } ^ { 0 } \cos \Theta , } } \\ { { } } \\ { { X = \displaystyle \frac { \partial { \cal W } } { r \partial \Theta } = - \left( \frac { a } { r } \right) ^ { s } G _ { 1 } ^ { 0 } \sin \Theta , } } \\ { { } } \\ { { Y = \displaystyle \frac { - \partial { \cal W } } { r \sin \Theta } \ o \frac { } { \partial A } = 0 , } } \end{array} \right\} .
$$

其中 $\textstyle { \pmb { X } } , { \pmb { Y } }$ 为磁北、磁东分量。由(5.142)即可得到(5.134)式。(5.134)是偶极子磁场的重要关系式,它在古地磁学的研究中有重要应用。

# 3.非偶极子磁场和偏心偶极子

地磁场除去与 $\pmb { n = 1 }$ 项相联系的中心偶极子的磁场后，剩下部分称为非偶极子磁场。非偶极磁场约占总磁场的 $1 0 - 2 0 \%$ ，图5.12是1965.0年代的非偶极子磁场图，它是间隔为2000伽吗的垂直强度 $( z )$ 等值线图，图上同时用水平箭头的长度和方向标出水平强度 $( H )$ 的大小和方向。图（5.12)表明，地磁非偶极子磁场有几个正负中心，其中以亚洲（中国北部和蒙古）非洲和南极大陆的中心最为明显。

中心偶极子磁场做为地磁场的近似描述是成功的，这种近似对于与地磁有关的物理现象的理论研究和计算都是方便的。为提高这种描述的近似程度，施密特和巴特尔斯（Bartels）提出了偏心偶极子的描述方法。所谓偏心偶极子是指强度和方向与中心偶极子相同，但偏离地心放置的偶极子，从以下证明将会看到,这样的偶极子所产生的磁场,在地心球极坐标系中， $\pmb { n = 1 }$ 的项与中心偶极子完全相同，而 $\pmb { n } = 2$ 项的高斯系数与偶极子的位置有关。偏心偶极子的位置是这样确定的，使得它的 ${ \pmb { n } } = 2$ 项的高斯系数与地磁场 $\textbf { \em n } =$ 2阶高斯系数的差的平方和为最小。

如图5.13a所示，设 $^ o$ 为地心， $_ { o z }$ 为地球自转轴， $\pmb { x y }$ 为赤道平面， $O x , O y$ 为 $\lambda = 0$ ，$\lambda = 9 0 ^ { \circ }$ 的方向， $0 ^ { \prime } x ^ { \prime } , o ^ { \prime } y ^ { \prime }$ ， $\acute { o } z ^ { \prime }$ 与 $O { \boldsymbol { \mathfrak { x } } } , O y , O z$ 平行，观测点 $\pmb { P }$ 在两个坐标系中的坐标分别为 $P ( r , \theta , \lambda )$ ， $\pmb { P } ( \pmb { x } , \pmb { y } , \pmb { z } )$ 和 $P ( r ^ { \prime } , \theta ^ { \prime } , \lambda ^ { \prime } ) , P ( x ^ { \prime } , y ^ { \prime } , z ^ { \prime } ) , o ^ { \prime }$ 点的坐标为 $( r _ { 0 } , \theta _ { 0 } , \lambda _ { 0 } )$ 或 $( x _ { 0 } , y _ { 0 } , z _ { 0 } )$ 。若将一偶极子放于 $o ^ { \prime }$ ，其强度和方向与(5.138）5.139)所定义的中心偶极子相同。由(5.138)和(5.139)不难看出，这样的偶极子所产生的磁势在以 $o ^ { \prime }$ 为中心的球极坐标系中的表达式为：

$$
W ( r ^ { \prime } , \theta ^ { \prime } , \lambda ^ { \prime } ) = a \left( \frac { a } { r ^ { \prime } } \right) ^ { 2 } [ g _ { 1 } ^ { 0 } \mathrm { c o s } \theta ^ { \prime } + g _ { 1 } ^ { 1 } \mathrm { s i n } \theta ^ { \prime } \mathrm { c o s } \lambda ^ { \prime } + h _ { 1 } ^ { 1 } \mathrm { s i n } \theta ^ { \prime } \mathrm { s i n } \lambda ^ { \prime } ] ,
$$

![](images/3076ba9f7154889d32dd1f682e8257bd6df731b2276481ee993ce219a7d61fa8.jpg)

![](images/43738a67fe0972bc8bb796ec179de2071011d0d1812ea85370c34d9a983766e6.jpg)  
图5.13

由关系式：

$$
x ^ { \prime } = x - x _ { 0 } , \quad y ^ { \prime } = \nu - \nu _ { 0 } , \quad z ^ { \prime } = z - z _ { n } ,
$$

将(5.143)改写为：

$$
W = \left( \frac { a } { r ^ { \prime } } \right) ^ { 3 } [ ( g _ { 1 } ^ { \circ } z + g _ { 1 } ^ { \cdot } x + h _ { 1 } ^ { \cdot } y ) - ( g _ { 1 } ^ { \cdot } z _ { 0 } + g _ { 1 } ^ { \cdot } x _ { 0 } + h _ { 1 } ^ { \cdot } y _ { 0 } ) ] ,
$$

由图(5.13)不难得出：

$$
\begin{array} { r l } & { r ^ { \prime 2 } = r ^ { 2 } + r _ { 0 } ^ { 2 } - 2 r r _ { 0 } \cos \phi , } \\ & { \frac { 1 } { r ^ { \prime 3 } } = \frac { 1 } { r ^ { 3 } } \Big \{ 1 - \frac { 3 } { 2 } \left[ \Big ( \frac { r _ { 0 } } { r } \Big ) ^ { 2 } - 2 \Big ( \frac { r _ { 0 } } { r } \Big ) \cos \phi \right. \Big ] + \cdot \cdot \cdot \Big \} , } \end{array}
$$

代(5.145)到(5.143),则场势 $W$ 在球极坐标系 $( r ^ { \prime } , \theta ^ { \prime } , \lambda ^ { \prime } )$ 的表达式（5.143)将转换到球极 坐标系 $( r , \theta , \lambda )$ ，

$$
\begin{array} { r l } & { ( r , \theta , \lambda ) = a \left( \frac { a } { r } \right) ^ { 2 } [ g _ { 1 } ^ { 0 } \cos \theta + g _ { 1 } ^ { 1 } \sin \theta \cos \lambda + h _ { 1 } ^ { 1 } \sin \theta \sin \lambda ] } \\ & { ~ + \left( \frac { a } { r } \right) ^ { 3 } [ - g _ { 1 } ^ { \upsilon } z _ { 0 } + g _ { 1 } ^ { \prime } x _ { 0 } + h _ { 1 } ^ { 1 } y _ { 0 } ] + 3 r _ { 0 } \cos \phi \lfloor g _ { 1 } \cos \theta + } \\ & { ~ g _ { 1 } ^ { 1 } \sin \theta \cos \lambda + h _ { 1 } ^ { 1 } \sin \theta \sin \lambda ] + O \left( \frac { 1 } { r ^ { 4 } } \right) , } \end{array}
$$

其中 $O \left( { \frac { 1 } { r ^ { 4 } } } \right)$ 代表阶数 $\pmb { n } \geqslant 4$ 的其余各项。由(5.146)看出，中心偶极子沿经向平移后与$\frac { 1 } { r ^ { 2 } }$ 相应的偶极项确实不变,与(5.135)所示地磁中心偶极子的场完全相同。这就证明了本节开始所说偏心偶极子的第一个论断：强度和方向与中心偶极子相同，但偏离地心放置的偶极子在地心坐标系中 $\pmb { n } = 1$ 的项与中心偶极子的场完全相同。

下面由与 $\frac { 1 } { r ^ { 3 } }$ 有关的项来确定偏心偶极子的坐标。将北极 $_ { \pmb { N } }$ 和观测点 $\pmb { P }$ 投影到以 $^ { o }$ 为球心以 $\pmb { r _ { 0 } }$ 为半径的球面上，相应投影点为 $N ^ { \prime } , P ^ { \prime }$ ，由球面三角 $o ^ { \prime } N ^ { \prime } P ^ { \prime }$ （图5.13b）可以得出：

$$
\begin{array} { l } { { \cos \phi = \cos \theta \cos \theta _ { 0 } + \ \sin \theta \sin \theta _ { 0 } \cos ( \lambda - \lambda _ { 0 } ) , } } \\ { { \ r _ { 0 } \cos \phi = z _ { 0 } \cos \theta + x _ { 0 } \sin \theta \cos \lambda + y _ { 0 } \sin \theta \sin \lambda , } } \end{array}
$$

将(5.147)代人(5.146),并将(5.146)中与 $\stackrel { 1 } { \underset { r ^ { 3 } } { - } }$ 有关的项记作 $W _ { 2 } ,$

$$
W _ { 2 } ( r , \theta , \lambda ) = ( { \frac { a } { r } } ) ^ { 3 } ( { \mathcal { A } } _ { 0 } + { \mathcal { A } } _ { 1 } \cos 2 \theta + { \mathcal { A } } _ { 2 } \sin 2 \theta \cos \lambda + { \mathcal { A } } _ { 3 } \sin 2 \theta \sin \lambda
$$

$$
+ \ d _ { 4 } \sin ^ { 2 } \theta \cos 2 \lambda + \ d _ { 5 } \sin ^ { 2 } \theta \sin 2 \lambda ) ,
$$

其中 $\pmb { A }$ 为与 $x _ { 0 } \textmd { , } y _ { 0 } \textmd { , } z _ { 0 }$ 和 $g _ { 1 } ^ { 0 } , g _ { 1 } ^ { 1 } , h _ { 1 } ^ { 1 }$ 有关的常系数，

$$
\left. \begin{array} { l } { { d _ { \circ } = \displaystyle \frac { 1 } { 2 } g _ { 1 } ^ { 0 } z _ { 0 } - \frac { 1 } { 4 } g _ { 1 } ^ { 1 } x _ { 0 } - \frac { 1 } { 4 } h _ { 1 } ^ { 1 } y _ { 0 } , } } \\ { { \ } } \\ { { d _ { \circ } = 3 d _ { \circ } , \quad \displaystyle \mathcal { A } _ { 2 } = \frac { 3 } { 2 } \left( g _ { 1 } ^ { 0 } x _ { 0 } + g _ { 1 } ^ { 1 } z _ { 0 } \right) , } } \\ { { \ } } \\ { { d _ { \circ } = \displaystyle \frac { 3 } { 2 } \left( g _ { 1 } ^ { 0 } y _ { 0 } + h _ { 1 } ^ { 1 } z _ { 0 } \right) , \quad \displaystyle \mathcal { A } _ { 4 } = \frac { 3 } { 2 } \left( g _ { 1 } ^ { 1 } x _ { 0 } - h _ { 1 } ^ { 1 } y _ { 0 } \right) , \mathrm { ~ } \Bigg \vert } } \\ { { \ } } \\ { { \displaystyle \mathcal { A } _ { , } = \frac { 3 } { 2 } \left( g _ { 1 } ^ { 1 } y _ { 0 } + h _ { 1 } ^ { 1 } x _ { 0 } \right) _ { 0 } } } \end{array} \right\}
$$

进一步由二阶连带勒让德函数

$$
\left. \begin{array} { l } { { P _ { 2 } ( \cos \theta ) = \displaystyle { \frac { 1 } { 4 } } ( 3 \cos 2 \theta + 1 ) } } \\ { {  } } \\ { { P _ { 2 } ^ { 1 } ( \cos \theta ) = \displaystyle { \frac { \sqrt { 3 } } { 2 } } \sin 2 \theta } } \\ { {  } } \\ { { P _ { 2 } ^ { 2 } ( \cos \theta ) = \displaystyle { \frac { \sqrt { 2 } } { 2 } } \sin ^ { 2 } \theta } } \end{array} \right\} ,
$$

将(5.148)改写为球函数形式

$$
\begin{array} { c }  { W _ { 2 } = \displaystyle { a \left( \frac { a } { r } \right) ^ { 3 } [ g _ { 2 } ^ { \prime 0 } P _ { 2 } ( \cos \theta ) + g _ { 2 } ^ { \prime 1 } \cos { \lambda P _ { 2 } ^ { 1 } ( \cos \theta ) } + h _ { 2 } ^ { \prime 1 } \sin { \lambda P _ { 2 } ^ { 1 } ( \cos \theta ) } } } \\ { { + g _ { 2 } ^ { \prime 2 } \cos { 2 \lambda P _ { 2 } ^ { 2 } ( \cos \theta ) } + h _ { 2 } ^ { \prime 2 } \sin { 2 \lambda P _ { 2 } ^ { 2 } ( \cos \theta ) } ] _ { \scriptscriptstyle { 0 } } } } \end{array}
$$

其中

$$
a g _ { 2 } ^ { \prime 0 } = 4 A _ { 0 } , \quad a g _ { 2 } ^ { \prime 1 } = \frac 2 { \sqrt { { \mathrm { \small { ~ 3 ~ } } } } } A _ { 2 } , \quad a g _ { 2 } ^ { \prime 2 } = \frac 2 { \sqrt { { \mathrm { \small { ~ 3 ~ } } } } } A _ { 4 }
$$

$$
a h _ { 2 } ^ { 1 } = \frac { 2 } { \sqrt { 3 } } \ : { \cal A } _ { 3 } , a h _ { 2 } ^ { \prime } = \frac { 2 } { \sqrt { 3 } } \ : { \cal A } _ { 5 0 }
$$

在地磁场球谐函数表达式（5.131）中,=2的高斯系数为g,g,h,g²和h。为使偏心偶极子磁场尽可能与(5.131)中n=1,2的场相近,上面已经证明n=1的场是完全相同的，那么必须使（5.151）W的系数与（5.131）中"=2的相应高斯系数的差的平方和为最小，即

$\Sigma _ { G _ { 2 } } = ( g _ { 2 } ^ { 0 } - g _ { 2 } ^ { \prime 0 } ) ^ { 2 } + ( g _ { 2 } ^ { 1 } - g _ { 2 } ^ { \prime 1 } ) ^ { 2 } + ( g _ { 2 } ^ { 2 } - g _ { 2 } ^ { \prime 2 } ) ^ { 2 } + ( h _ { 2 } ^ { 1 } - h _ { 2 } ^ { \prime 1 } ) ^ { 2 } + ( h _ { 2 } ^ { 2 } - h _ { 2 } ^ { \prime 2 } ) ^ { 2 }$ 为最小。由(5.153)为最小的条件便可确定偏心偶极子的坐标：

$$
\begin{array} { r l } & { { { x } _ { 0 } } = a \left( { { L } _ { 1 } } - { { g } _ { 1 } ^ { 1 } } { E } \right) / 3 { { H } _ { 0 } ^ { 2 } } } \\ & { { { y } _ { 0 } } = a \left( { { L } _ { 2 } } - { { h } _ { 1 } ^ { 1 } } { E } \right) / 3 { { H } _ { 0 } ^ { 2 } } \vphantom { { \left( { { L } _ { 2 } } - { { h } _ { 1 } ^ { 1 } } { E } \right) } } , } \\ & { { { z } _ { 0 } } = a \left( { { L } _ { 3 } } - { { g } _ { 1 } ^ { 0 } } { E } \right) / 3 { { H } _ { 0 } ^ { 2 } } \vphantom { { \left( { { L } _ { 2 } } - { { g } _ { 1 } ^ { 0 } } \right) } } } \end{array}
$$

其中

$$
\left. \begin{array} { l } { { H _ { 0 } ^ { 2 } = ( g _ { 1 } ^ { 0 } ) ^ { 2 } + ( g _ { 1 } ^ { 1 } ) ^ { 2 } + ( h _ { 1 } ^ { 1 } ) ^ { 2 } } } \\ { { L _ { 0 } = 2 g _ { 1 } ^ { 0 } g _ { 2 } ^ { 0 } + \sqrt { \mathit { \Omega } _ { 3 } } \ : ( g _ { 1 } ^ { 1 } g _ { 2 } ^ { 1 } + h _ { 1 } ^ { 1 } h _ { 2 } ^ { 1 } ) } } \\ { { L _ { 1 } = - g _ { 1 } ^ { 1 } g _ { 2 } ^ { 0 } + \sqrt { \mathit { \Omega } _ { 3 } } \ : ( g _ { 1 } ^ { 0 } g _ { 2 } ^ { 1 } + g _ { 1 } ^ { 1 } g _ { 2 } ^ { 2 } + h _ { 1 } ^ { 1 } h _ { 2 } ^ { 2 } ) } } \\ { { L _ { 2 } = - h _ { 1 } ^ { 1 } g _ { 2 } ^ { 0 } + \sqrt { \mathit { \Omega } _ { 3 } } \ : ( g _ { 1 } ^ { 0 } h _ { 2 } ^ { 1 } - h _ { 1 } ^ { 1 } g _ { 2 } ^ { 2 } + g _ { 1 } ^ { 1 } h _ { 2 } ^ { 2 } ) } } \end{array} \right\}
$$

$$
E = ( L _ { 0 } g _ { 1 } ^ { 0 } + L _ { 1 } g _ { 1 } ^ { 1 } + L _ { 2 } h _ { 1 } ^ { 1 } ) / 4 H _ { 0 } ^ { 2 }
$$

根据1955.0年代地磁资料求得偏心偶极子的位置为 $1 5 ^ { \circ } 4 1 ^ { \prime } \mathrm { N }$ ， $1 5 0 ^ { \circ } 4 9 ^ { \prime } \mathrm { E }$ ，离开地心的距离 $r _ { 0 } = 4 3 6$ 公里。

除偶极项和 $W _ { 2 }$ 外,(5.146)中还有高阶项 $O \ ( { \frac { 1 } { \eta ^ { 4 } } } ) _ { \circ }$ 由(5145）和（5.144)不难看出,这些高阶项中都含有 $\left( { \frac { r _ { 0 } } { r } } \right) ^ { n } ( n \geqslant 2 )$ 的因子，当偏心偶极子的位置 $r _ { 0 } \ll r$ 时，(5.146)中$O \left( { \frac { 1 } { r ^ { 4 } } } \right)$ 与 $n = 1 , 2$ 项相比为高阶小量,因此可以忽略。

图5.14给出了中心偶极子和偏心偶极子地面磁场的比较。

![](images/cf74352dfd989d60aad526c97902c630cdcefe9c899cb74ff1f116974d57f5fa.jpg)  
图5.14中心(a)和偏心(b)偶极子地面磁场的分布

# （二）基本磁场的长期变化

观测和分析都表明地球基本磁场随时间有缓慢的变化。这种变化称为地磁场的长期变化，以伽吗/年（ $\cdot r /$ 年）表示。地磁场长期变化的时空规律是追踪地球内部物质运动的重要线索，是固体地球物理中的一个重要课题。由于长期变化具有全球性的统一特征，一般认为它是来源于地核内部或核幔边界。地磁长期变化的全球性主要特征是偶极子磁矩的衰减，非偶极子磁场的西向漂移和长期变化场自身的西向漂移。

# 1.长期变化现象

最早长期变化现象较为系统的记录是伦敦的偏角变化。图5.15同时绘出了伦敦和非洲南端希望峰偏角的变化，两者有类似的趋势，300年间变化达几十度之多，继发现偏角变化之后，也发现其他地磁要素有性质类似的长趋势变化。

![](images/181159e58ad447dad9582a775e149a3df74db2a91c8023dc69768705c62d9c5a.jpg)  
图5.15伦敦和希望峰偏角随时间的变化[]

<table><tr><td rowspan="2">器</td><td></td><td>2</td><td>3 6&#x27;81-</td><td>69 5 2</td><td>5</td><td>5 8 0</td><td>1</td><td></td><td>3 2</td><td>0 3 2</td><td></td><td></td><td>5 0</td><td>1 2 0 1</td><td>3 7 0</td></tr><tr><td>6</td><td>0 ： 1</td><td>7</td><td></td><td>一 2</td><td></td><td>9</td><td>1 3</td><td>3 7</td><td></td><td>5</td><td>0 2</td><td>5</td><td>0 8 2 2</td><td>0 9</td></tr><tr><td rowspan="2">6 </td><td>8 </td><td>23 8 Ⅱ 1</td><td></td><td>1</td><td></td><td>2 3</td><td>2 9 2 2 4</td><td>0</td><td>0 3 7 2</td><td>4 8 2 0</td><td>3</td><td>0 0 1</td><td>4 0</td><td>2</td><td>0 0</td></tr><tr><td>5</td><td>3 7 8 24</td><td>3 6 0 一</td><td>2 8 0 1</td><td>一 7 8 0 3</td><td>7 2 0 i</td><td>0 3 0</td><td>2</td><td>9</td><td>9 6 2 0</td><td>0 0 3 0</td><td>0</td><td>3 0</td><td>9 0 1</td><td>2 0 0</td></tr><tr><td rowspan="4">6</td><td></td><td>0 4 1</td><td>18</td><td>1 1 6 3 1</td><td>5</td><td>0 7 3 </td><td>7 元 2 2</td><td></td><td>3 2</td><td>8 4</td><td></td><td>2 2</td><td>2 9 0 0</td><td>2</td><td>0</td></tr><tr><td></td><td>1 3 6 5 8 2</td><td>3 1 1</td><td>1</td><td>6 6 0 0 1 1</td><td>0 2 1</td><td>2 0</td><td>1 0 8 3 0</td><td>4 6 0 1</td><td>1 3 0</td><td>7</td><td>0</td><td>5 8 1</td><td>6 0</td><td>2 2 0 2</td></tr><tr><td></td><td>1 9 0 7 4</td><td>1 1</td><td>9 1</td><td>0 0 4</td><td>9 0</td><td>水 2 3</td><td>1 5 5</td><td>8 9 1 2</td><td>1 8 0</td><td>1 1 4 2</td><td>0</td><td>0</td><td></td><td></td></tr><tr><td>8</td><td>： 9 3 8 8 7 0</td><td>8 0</td><td>4 5 1</td><td>4 9 3 一</td><td>8 4 0 5</td><td>1 9 2 1 0</td><td>5 0 3 一</td><td>7 5 1</td><td>1 6 2 0</td><td>1 0</td><td></td><td></td><td></td><td></td></tr><tr><td>5</td><td>H</td><td>3 0 1 2 16 7 1</td><td></td><td>2 5 8 3</td><td>7 6 1</td><td>0</td><td>一 1 5 3</td><td>2 1</td><td>7</td><td>3 0</td><td>7 2 0</td><td>7</td><td>2 5 1</td><td>1 1</td><td>1 0 0</td></tr><tr><td></td><td>5</td><td>6 5 B 5 2 1</td><td>8 0</td><td>1 8 ！</td><td>5 0 ！</td><td>2</td><td>0 0 2</td><td>2 2</td><td>8</td><td>0 0</td><td>5 2 0 0</td><td>7</td><td>2 0</td><td>2 5 0 1</td><td>5 6 0 0</td></tr><tr><td>6</td><td></td><td>0 0 16 1</td><td>5 0 B 1</td><td>0 4</td><td>1</td><td>5 2</td><td>5</td><td>0 6 1</td><td>2 5</td><td>6</td><td>6 4 0</td><td>3</td><td>8 3 0</td><td>0 2 1</td><td>5 0 2 0</td></tr><tr><td rowspan="3"></td><td>5</td><td>0 0 1 1 20</td><td>0 0 0 0</td><td>7 7 3 0 1 1</td><td>3 8 2</td><td>0 3</td><td>3 3</td><td>6</td><td>2 8 0 2</td><td>0</td><td>4</td><td>1 0</td><td>2</td><td>0</td><td>5 2 0</td><td></td></tr><tr><td></td><td>1 1 4 一</td><td></td><td>4 1</td><td>10</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="3"></td><td></td><td>9 2 18 一</td><td>0 2 6</td><td>0 3</td><td>1 0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>5 8 4</td><td></td><td>5 1</td><td>4 3</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="3">5</td><td>5</td><td>3 4 1</td><td>1 2</td><td>7</td><td>3</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>4 1</td><td></td><td>5 1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>8 2 4</td><td>1 1</td><td></td><td>2 7</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td>3</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>5</td><td>25 24 1</td><td></td><td>7 T</td><td>B 1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>5</td><td>1 2 8</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="2"></td><td>2 1</td><td>8</td><td>B</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="2">m</td><td>0</td><td></td><td>2 中</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="2">$</td><td></td><td colspan="18"></td></tr></table>

![](images/db7ca8db2c342bfc5da727d29669e6b7cb34bb6784bfe48ed67f56893d310569.jpg)  
图5.161965.0年代 $z$ 长期变化等值线图（Z为等值线,单位 $r /$ 年)[91

和地磁图一样，也可以把各要素长期变化的等值线绘于地图上，图5.16为1965.0年代垂直分量（Z）长期变化等值图,由图5.16看出，地磁长期变化有几个变化较大的中心，例如：在大西洋赤道附近的中心可达一 $1 8 0 \gamma /$ 年，南极大陆有同等强度的正的长期变化；同时还可以看到，在太平洋中部长期变化很小的事实。从不同年代长期变化地磁图的比较还发现，长期变化中心有缓慢向西移动的趋势，其平均移动趋势约为 $\mathbf { 0 . 3 ^ { \circ } } /$ 年。

在本章第二节中已经指出，上述长期变化的事实也将反映在不同年代地磁场球谐分析高斯系数的变化上。这种高斯系数随时间的变化可以由不同年代高斯系数的比较得出，但由全球地磁测量按公式(5.132)计算得到的高斯系数 $g _ { n } ^ { m } \setminus h _ { n } ^ { m }$ 会受到具体测点局部磁异常和局部干扰的影响，不难了解，这种影响将会带到由不同年代高斯系数的比较所确定的时间变化率 $\dot { g } _ { n } ^ { m } , \dot { h } _ { n } ^ { m }$ 中去，因此通常不采用这种直接比较方法，而是首先计算出各测点地磁要素的长期变化,然后由全球地磁长期变化（图5.16)的球谐分析求得相应的球谐系数。第二节的表5.3所列1965.0和1975.0年代高斯系数的年变率就是这种球谐分析的结果。为了解不同年代长期变化的全貌，表4同时给出了各年代不同作者所得 ${ \pmb { n } } \leqslant { \pmb { 6 } }$ 阶高斯系数的年变率。由表5.4不难看出，与基本磁场不同,长期变化的球谐系数 $\dot { g } _ { 2 } ^ { 0 }$ 和 $\pmb { \dot { h } } _ { 2 } ^ { 2 }$ 项最为显著，其收敛性也不像基本磁场那样迅速。

# 2.偶极子磁矩的衰减

根据不同年代地磁场球谐分析 $\pmb { n } = 1$ 阶的高斯系数，由公式(5.138)可以算出各年代

表5.5不同年代的地磁场偶极矩  

<table><tr><td>作 者</td><td>年</td><td>代</td><td>偶极矩(10&quot;高斯·厘米)</td></tr><tr><td>Erman &amp; Petersen</td><td>1829</td><td></td><td>8.45</td></tr><tr><td>Gauss</td><td></td><td>1835</td><td>8.56</td></tr><tr><td>Adams</td><td></td><td>1845</td><td>8.49</td></tr><tr><td>Adams</td><td></td><td>1880</td><td>8.36</td></tr><tr><td>Schmidt</td><td></td><td>1885</td><td>8.35</td></tr><tr><td>Fritsche</td><td></td><td>1885</td><td>8.34</td></tr><tr><td>Neumeyer &amp; Petersen</td><td></td><td>1885</td><td>8.33</td></tr><tr><td>Cain &amp; Hendricks</td><td></td><td>1900</td><td>8.30</td></tr><tr><td>Cain &amp; Hendricks</td><td></td><td>1920</td><td>8.20</td></tr><tr><td>Dyson &amp; Furner</td><td></td><td>1922</td><td>8.17</td></tr><tr><td>Cain &amp; Hendricks</td><td></td><td>1940</td><td>8.10</td></tr><tr><td>Jones &amp; Melotte</td><td></td><td>1942</td><td>8.01</td></tr><tr><td>Afanasieva</td><td></td><td>1945</td><td>8.01</td></tr><tr><td>Vestine and Others</td><td></td><td>1945</td><td>8.07</td></tr><tr><td>Finch&amp; Leaton</td><td></td><td>1955</td><td>8.06</td></tr><tr><td>Cain &amp; Hendricks</td><td></td><td>1960</td><td>8.02</td></tr><tr><td>Hurwitz and Others</td><td></td><td>1965</td><td>8.00</td></tr><tr><td>Leaton and Others</td><td></td><td>1965</td><td>8.00</td></tr></table>

的偶极子的磁矩。其结果列于表5.5和图 ${ \pmb 5 . 1 7 . }$

由表5.5和图5.17清楚地看到，近百余年来地磁偶极矩一直是单调衰减,其衰减速率100年可达 $5 \%$ ，若假定这种衰减趋势今后一直维持的话，大约2000年后，偶极子磁场即将消失，然而古地磁学的研究得出，这种衰减速度并不是不变的，特别重要的事实是在约2000年之前它是上升的。

![](images/ba24076a565efb6f08e2705694255a5cb14ff6968e7c7b52cabcfe6ba3efe5b9.jpg)  
图5.17地球磁偶极矩随时间的变化[,4.3]

# 3.非偶极子磁场的西向漂移和偏心偶极子的移动

早在17世纪英国天文学家哈利（E．Halley）在分析地磁偏角的变化时就曾指出，地磁场的分布图形有缓慢向西移动的事实。但西向漂移比较系统的研究却是在本世纪五十年

代开始的[[][3][4[15]。分析结果表明，西向漂移的主要成分是非偶极子磁场。

与流体中的物理场相似，地磁场的时间变化包括测点场的时间变化率和场的空间运动两个部份。若以 $X _ { i }$ 表示磁场的各分量或磁位，则有

$$
\frac { d X _ { i } } { d t } \dot { = } \frac { \partial X _ { i } } { \partial t } + ( \pmb { u } \cdot \nabla ) X _ { i 0 }
$$

其中 $\pmb { \ u }$ 即为场的运动速度， $\pmb { \alpha }$ 沿纬圈的分量， $- \textbf { \em u } _ { \lambda }$ 即为西向漂移速度。倘若假定西向漂移是非偶极子磁场长期变化的主要部份，则按(5.156)可由观测资料确定西向漂移速度。

将公式(5.131)改写为：

$$
\left. \begin{array} { c } { { W = a \displaystyle \sum _ { n = 1 } ^ { \infty } \sum _ { m = 0 } ^ { \infty } \hat { p } _ { n } ^ { m } \big ( \cos \theta \big ) G _ { n } ^ { m } \cos m \big ( \lambda + \lambda _ { n } ^ { m } \big ) , } } \\ { { \big ( G _ { n } ^ { m } \big ) ^ { 2 } = ( g _ { n } ^ { m } ) ^ { 2 } + \big ( h _ { n } ^ { m } \big ) ^ { 2 } , \quad \mathrm { t a n } m \lambda _ { n } ^ { m } = \displaystyle \frac { - h _ { n } ^ { m } } { g _ { n } ^ { m } } _ { 0 } } }  \end{array} \right\}
$$

因只考虑非偶极子磁场，计算中应除去 $\pmb { n } = 1$ 项。（5.157）中相位角 $2 _ { n } ^ { m }$ 随时间的变化8，即为高斯分析中相应各阶磁场的西向漂移速度。进一步，为研究不同纬度非偶极磁场的西向漂移，可将同一纬度不同经度处的非偶极磁场做关于经度 $\gimel$ 的傅氏分析，即

$$
\boldsymbol { W } = \boldsymbol { \Sigma } \boldsymbol { C } _ { m } \cos { \left( \lambda + \lambda _ { m } \right) } ,
$$

同样 $\frac { \partial \lambda _ { m } } { \partial \iota }$ 即为该纬度非偶极子磁场的西向漂移速度。(5.158)中傅氏系数 $C _ { m }$ 和 $\lambda _ { m }$ 与高斯系数的关系为：

$$
\begin{array} { r l } & { ( C _ { m } ) ^ { 2 } = \bigg [ \displaystyle \sum _ { n = m } ^ { \infty } g _ { n } ^ { m } P _ { n } ^ { m } ( \cos \theta ) \bigg ] ^ { 2 } + \bigg [ \displaystyle \sum _ { n = m } ^ { \infty } h _ { n } ^ { m } P _ { n } ^ { m } ( \cos \theta ) \bigg ] ^ { 2 } \quad } \\ & { \mathrm { t a n } m \lambda _ { m } = - \bigg [ \displaystyle \sum _ { n = m } ^ { \infty } h _ { n } ^ { m } P _ { n } ^ { m } ( \cos \theta ) \bigg ] \bigg / \bigg [ \displaystyle \sum _ { n = m } ^ { \infty } g _ { n } ^ { m } P _ { n } ^ { m } ( \cos \theta ) \bigg ] \bigg \} , } \end{array}
$$

行武毅 $\mathbf { [ 1 2 ] }$ 利用（5.159)研究了1829-1955年间 $\lambda _ { m }$ 的平均变化,其结果列于表 $5 . 6 \textdegree$ 由表5.6看出 $\frac { \partial \lambda _ { m } } { \partial \varepsilon }$ 取正值,这意味着磁场确实向西漂移， $\frac { \partial \lambda _ { 1 } } { \partial \iota }$ 的平均值为 $0 . 2 2 4 ^ { \circ } ;$ 1年。若上述计算中不除去偶极子磁场(与轴向偶极子无关)，则 $\frac { \partial \lambda _ { 1 } } { \partial \varepsilon }$ 的平均值仅为 $0 . 0 6 2 ^ { \circ } /$ 年。这说明地磁场的西向漂移中，非偶极子磁场确实是主要的。

表5.6不同纬度 $\lambda _ { m }$ 随时间的变化率[4（度/年）  

<table><tr><td>纬 度</td><td>a2/@t</td><td>a2/0t</td><td>a2/0t</td></tr><tr><td>80°N</td><td>0.097</td><td>0.000</td><td>10.012</td></tr><tr><td>60</td><td>0.275</td><td>0.050</td><td>10.060</td></tr><tr><td>40</td><td>0.370</td><td>0.115</td><td>-0.384</td></tr><tr><td>20</td><td>0.318</td><td>0.216</td><td>0.295</td></tr><tr><td>0</td><td>0.075</td><td>0.339</td><td>0.250</td></tr><tr><td>20</td><td>0.391</td><td>0.580</td><td>0.230</td></tr><tr><td>40</td><td>0.168</td><td>0.970</td><td>0.188</td></tr><tr><td>60</td><td>0146</td><td>1.11</td><td>0.165</td></tr><tr><td>80s</td><td>0.180</td><td>1.10</td><td>0.148</td></tr></table>

按西向漂移的意义，由场的时间变化率和经度变化率亦可求得西向漂移速度 $\pmb { u }$ ,计算公式为：

$$
\int _ { 0 } ^ { \varepsilon } \Big [ \frac { \partial H _ { P } } { \partial \tau } - u \frac { \partial H _ { P } } { \partial \lambda } \Big ] ^ { 2 } d t = \mathfrak { k } \mathfrak { k } / \mathfrak { l } \mathfrak { d } \mathfrak { s }
$$

由(5.160）(5.161)取极小值的条件，便可确定漂移速度 ${ \pmb u } _ { \pmb { \circ } }$ (5.160)要求已知同一纬度圈各处的磁位W及其时间变化率，它决定了同一纬度不同经度各测点的平均漂移速度；（5.161）是已知某观测点 $\pmb { P }$ 的时间变化率和经度变化率，求得 $\pmb { P }$ 点漂移速度 $\pmb { \mathscr { H } }$ 的时间平均值。前者不能显示漂移速度的经度差异，后者不能反映漂移速度的时间变化。行武毅2利用(5.160)和(5.161)式计算所得西向漂移速度分别列于表5.7和表 $5 . 8 \textdegree$

由表5.6一5.8我们看到，用不同方法求得的结果，其漂移速度都接近 $0 . 2 ^ { \circ } /$ 年。这种结果支持非偶极子磁场整体向西漂移的论断。从西向漂移的定义和相应计算公式不难了解,不管怎样,在一定条件下的漂移速度总是可以计算的,问题的关键在于,这样计算的漂移速度有意义,必须是在空间上具有整体的规律性，在时间上有一定的持续性。关于后者因地磁场全球可靠的记录时间不长,已有的分析结果还难以断言。而空间整体的规律性，虽然如上所述平均漂移速度都接近0.2°/年，但不同纬度分散较大，且没有显示任何明显的规律性(表5.6,5.7),表5.8所得平均结果中原各测点的漂移速度分散可达0.1°-0.4°，特别还存在少数测点有完全相反的漂移趋势。因此尽管目前多数学者都相信地磁场有西向漂移的趋势，但仍有人认为它并没有什么实质意义[5[22]。我们在了解上述计算结果时必须充分注意到这种现实。

表57由(5160)式计算的漂移速度″（度/年）[]  

<table><tr><td>纬 度</td><td>1922 5</td><td>1942 5</td><td>1957.5</td></tr><tr><td>80°N</td><td>0345</td><td>0176</td><td>0115</td></tr><tr><td>60N</td><td>0187</td><td>0093</td><td>0200</td></tr><tr><td>40N</td><td>0154</td><td>0099</td><td>0266</td></tr><tr><td>20N</td><td>0236</td><td>0188</td><td>0.275</td></tr><tr><td>0</td><td>0353</td><td>0196</td><td>0208</td></tr><tr><td>20s</td><td>0402</td><td>0240</td><td>0272</td></tr><tr><td>40S</td><td>0145</td><td>0243</td><td>0226</td></tr><tr><td>60s</td><td>0092</td><td>0205</td><td>0 228</td></tr><tr><td>80s</td><td>0075</td><td>0181</td><td>0246</td></tr><tr><td>下均</td><td>0 221</td><td>0180</td><td>0 226</td></tr></table>

表5834个台站不同要素西向漂移速度的平均值[2]  

<table><tr><td rowspan=1 colspan=1>地        磁        要        素</td><td rowspan=1 colspan=1>漂移速度“（度/年）</td></tr><tr><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>0.125±0.016</td></tr><tr><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>0192±0 006</td></tr><tr><td rowspan=1 colspan=1>Z</td><td rowspan=1 colspan=1>0 236±0.013</td></tr></table>

上述事实也在非偶极子磁场的地磁图上反映出来。我们在前面已经指出，非偶极子磁场存在几个强度较大的正负中心（图5.12)。行武毅等人[追踪这些中心的动向发现，有的中心呈现出西向漂移，而有的却没有明显的变位。图5.18是非洲负中心和蒙古正中心的位置和强度随时间的变化。图5.18显示出，非洲中心位置以大约0.28°/年的速度向西移动，在350年间强度变化了50%。但蒙古中心虽然强度有显著增强，但中心位置似乎没有变化，此外位于太平洋的两个正负中心也没有显示出明显的变位。

是非偶极子磁场西向漂移并无全球性特征，还是这种特征被其他因素所掩盖，或者需要重新探索地磁长期变化的规律性，这正是地磁长期变化研究所面临的课题。行武毅(T．Yukutake）假定,地磁场除去球谐分析中m=0的各项后，其余成分可区分为停滞部分和移动部分]。他认为上述关于漂移速度在不同地区的差异是由于被磁场停滞部分掩盖的结果。

最后需要指出,无论是上述的偶极矩的衰减部分，还是非偶极场的西向漂移，都不能包括长期变化相当显著的高斯系数g的变化。由图5.19看出，g取负号，绝对值在继续增大，150年间增加了2000余伽吗。

![](images/d982bc72d7b3636be6b05a19277fdfb48ca5870488ad934a12b497e08661da07.jpg)  
图5.18非洲和蒙古中心位置和强度的变化

![](images/ada03c7303369a8d8782a22f83de23f1bee820a035797d9f58858c136ba05b53.jpg)  
图5.19高斯系数 $\pmb { g _ { 2 } ^ { 0 } }$ 的时间变化

![](images/8ebb25f03fbe3b1b2f77a91523755a8d4f258a11375cc1a7feb3c5aaa156757b.jpg)  
图5.20偏心偶极子的移动]

魏斯汀（E.H.Vestine)[]研究了偏心偶极子的长期变化，发现它有向北、向西移动的趋势，西向漂移速度约为 $0 . 2 9 ^ { \circ } .$ /年，北向速度约为 $0 . 2 ^ { \circ } /$ 年。但很显然偏心偶极子的移动与上述非偶极子磁场的漂移和 $g _ { 2 } ^ { 0 }$ 的变化之间并不是相互独立的成分，而是不同方式的一种描述而已。偏心偶极子的移动绘于图5.20。魏斯汀（Vestine）还提出，长期变化与地球转速的变化有关[18][19],但有人对此持怀疑态度[20,行武毅则认为只有地球偶极子强度的变化才与地球转速相关[21。

# 四、地球的变化磁场

除稳定的基本磁场及其缓慢的长期变化外,地磁场还存在各种类型的短期变化，叫作地球的变化磁场。与基本磁场不同，变化磁场主要来源于地球外部。在地球表面这种变化磁场比起基本磁场要小得多，通常约为万分之几到千分之几,偶尔可达百分之几。变化磁场在地面上的数量虽小，但由于它来源于高空，因此其空间分布和时间变化能够反映高空各种电磁过程,对于研究高空物理现象，空间介质的性质和运动状态是很重要的。正如本章开始所说,地球变化磁场和空间电磁过程的关系,是地磁学迅速发展的一个分支领域,构成了空间物理的部分研究内容。

变化磁场包括非常复杂的多种类型。根据出现时间的特点可以划分为平静变化和干扰变化两类。平静变化是指时间上连续存在的周期性变化，它包括太阳静日变化 $( \pmb { S _ { q } } )$ 和太阴日变化 $( L )$ ；所谓干扰变化是偶尔出现,持续时间有长有短各类变化的总称，它包括太阳扰日变化 $( s _ { p } )$ ，磁暴场 $( D )$ ，钩扰 $( c , )$ 和地磁脉动 $P _ { \circ }$ 磁暴场 $( D )$ 又可区分为暴时变化 $( D _ { s t } )$ ，暴时扰日变化 $( D _ { s } )$ ，和极区亚暴 $( D _ { p } ) _ { \circ }$ 其中 $D _ { p }$ 在中低纬度又称为湾扰 $\left( B \right)$ ，暴时日变化 $( D , )$ 是通常扰日变化 $( { \cal { S } } _ { D } )$ 在磁暴时的特殊形式。以上各种变化除静日变化 $s _ { q }$ ，太阴日变化 $\pmb { L }$ ，湾扰 $\pmb { B }$ 和钩扰 $\pmb { c }$ ，与地方时有关外,其余变化场都与世界时有关，在全球各地依照同一的时间规律发生和演变。以上各类变化场 $\delta H$ 的分类可概括为

$$
\delta H = \delta H _ { q } + \delta H _ { D } , \qquad \delta H _ { q } = S _ { q } + L
$$

$$
\delta H _ { D } = S _ { D } + D + C _ { r } + P
$$

变化磁场的产生与太阳活动有关。太阳活动又有粒子辐射和光辐射之分。按着这种辐射源的不同，地磁学中又常将变化磁场分为 $^ { \mathfrak { s } } \mathrm { K } ^ { \mathfrak { s } }$ 变化和非 $^ { \mathfrak { s e } } \mathrm { K } ^ { \mathfrak { s } }$ 变化两类。所谓K变化，是指由于太阳辐射的高速等离子体到达地球与地磁场相互作用而产生的变化磁场；而非$^ { \bullet } \mathrm { K } ^ { \bullet \bullet }$ 变化则是由于太阳紫外辐射使高空大气电离，这种电离的大气在地磁场中运动所产生的附加磁场。除太阳静日变化，太阴日变化和钩扰是非 $^ { \pmb { \mathscr { \alpha } } } \mathrm { K } ^ { \pmb { \mathscr { \alpha } } }$ 一类变化外,其余均为 $^ { \bullet } \mathrm { K } ^ { \bullet }$ 变化。

从上述简要叙述已经可以看出，各种变化磁场不仅来原各异,其时间和空间变化规律也是相当复杂的。详细叙述各种变化的规律和理论远远超出了本书的限度。下面仅对其中较为重要的类型和概念，诸如地磁指数，太阳日变化，磁暴和磁亚暴等分段逐一介绍。

# （一）地磁指数，国际磁静日和磁扰日

既然地磁场存在有干扰变化，那末“干扰程度”的度量标准在地磁学中就应是必不可少的了。地磁场的于扰与太阳活动有关。这种干扰程度与太阳活动的统计相关性是日地关系研究的重要内容,也是探讨干扰的具体太阳活动源的向导。诚然,直接用磁场的度量标准做这种干扰程度的量度来进行上述统计相关也未尝不可。但很显然,由于干扰在地磁场中的表现千差万别,具体磁场数值的罗列很难直观反映这种干扰程度,在统计计算中也是不方便的。为此国际地磁和高空物理协会（IAGA）及其前身国际地磁和地电协会(IAME)规定了各种地磁指数作为地磁干扰程度的度量标准。这种地磁指数不下十多种，鉴于地磁指数概念在地磁学中经常遇到,是建立地磁静扰日的基础,在这里就其中常用的几个做简要介绍。

# 1.磁情记数 $\pmb { c }$ 和 $\pmb { C _ { t } }$

磁情记数 $^ c$ 是逐日静扰情况的量度，以0、1、2三个数字表示干扰程度。对于每个地磁台由世界时 $0 ^ { n }$ 至 $2 4 ^ { h }$ ，即一个整世界日的地磁记录，凭经验作出判断：若干扰程度适中，处于该地的平均状态， $c$ 记做 $^ { \bullet } 1 ^ { \circ }$ ，平静记做 $" 0 ^ { \circ }$ ，干扰强则记做 $^ { \bullet \bullet } 2 ^ { \bullet \bullet }$ 。磁情记数 $^ c$ 虽然粗糙，但却是干扰程度一种方便而迅速的量度。

各个国际合作台站把所得磁情记数 $^ { c }$ 迅速寄往荷兰德俾尔（DeBilt）中心台，然后将各台 $^ { c }$ 取算术平均并保留一位小数，这样得到的指数称为国际磁情记数，用 $c$ 表示。$\pmb { C } _ { t }$ 由0到2共21个等级，表示各世界日全球扰动的程度。

# 2.磁情指数 $\pmb { K }$ 和行星性指数 $\pmb { K } _ { p }$

对于小于一天的各不同时段扰动程度的区分，磁情记数 $c$ 和 $c$ ，是无能为力的。因此国际地磁和地电协会于1939年又确定了新的磁情指数 $\kappa$ 。与凭经验选取的指数 $\pmb { c }$ 不同，磁情指数 $\kappa$ 是太阳粒子辐射引起地磁扰动程度的一种较为精确的量度。 $\pmb { K }$ 的标度为从0至9的所有整数，共10级，每一级对应一定的干扰幅度 $\pmb { R }$ 。将各台一个世界日水平强度的磁照图按每三小时一个时段划分8段，消去非 $\pmb { \kappa }$ 变化 $s _ { q }$ 和 $c$ 后，按每时段的扰动幅度$\pmb R$ 求得对应的指数 $\pmb { K }$ 。由于扰动幅度 $\pmb R$ 随纬度有显著差异，而指数 $\kappa$ 是同一扰动源的客观量度，因此不同纬度的台站，幅度 $\pmb { R }$ 与 $\pmb { K }$ 的对应有不同的标度。关于各台对应标度的选取，老的台站是由1938年每个台的 $R$ 值与相应时段标准台的 $\pmb R$ 比较而统一建立的。新的台站可通过与同纬度各台的比较统计得出。并且规定 $K = 9$ 的下限幅度 $\pmb R$ 应与国际地磁和高空物理协会协商确定。表5.9为国际标准地磁台和我国北京地磁台的 $\pmb { K }$ 与 $\pmb R$ 的对应关系。

表5.9标准台（Nicmcgk， ${ \bar { 5 } } 2 ^ { \circ } 0 4 ^ { \prime } \mathbf { N }$ ， $1 2 ^ { \circ } 4 0 ^ { \prime } \mathbf { E } \rangle$   

<table><tr><td>K=0</td><td></td><td>1</td><td>2</td><td></td><td>3</td><td>4</td><td>5</td><td></td><td>6</td><td></td><td>7</td><td></td><td>8</td><td></td></tr><tr><td>Ru</td><td>5</td><td>10</td><td></td><td>20</td><td>40</td><td></td><td>70</td><td></td><td>120</td><td>200</td><td></td><td>330</td><td>500</td><td>(r)</td></tr><tr><td></td><td></td><td></td><td></td><td>北京台</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>K=0</td><td>1</td><td></td><td>2</td><td></td><td>3</td><td>4</td><td></td><td>5</td><td>6</td><td></td><td>7</td><td></td><td>8</td><td>9</td></tr><tr><td>R=</td><td>3</td><td>6</td><td></td><td>12</td><td>24</td><td></td><td>40</td><td>70</td><td></td><td>120</td><td></td><td>200</td><td>300</td><td>(r)</td></tr></table>

尽管 $\kappa$ 与 $\pmb R$ 的对应考虑了干扰的地理分布的影响，但这仅仅是统计意义上的，对于具体的一个台站，每个世界日8个具体的数K仍包含有局部因素。为此又选取全球分布适当的12个台站，将每日K指数汇集平均，得到消除局部影响的所谓行星性磁情指数Kp(Planetaryindex)。当12个台站K值取平均时，将每一级又分为三级，如K=4分成4-,4,4+，0和9只有0,0+,9,9,这样指数K,从0至9共28级。

# 3.指数 $\pmb { A } _ { \pmb { k } }$ 和 $\mathbf { A } _ { p }$

由于指数C和C，作为逐日扰动程度的量度比较粗糙，不能完全满足统计研究的要求，人们又选择了量度逐日扰动程度的新指数。能否采用3小时指数K或K。一天8个数的总和作为新的逐日干扰的量度呢？从下面例子容易理解，这显然是不合适的。例如某日K为11111111,另一天为00000008，两天K的总和全为8，但前者相当平静，而后者最后三小时却存在很强的扰动。这种弊病的产生是由于K指数的级数和磁场扰动幅度为准对数关系,直接相加等权求和是不适宜的。为克服这种弊病，可以把$\kappa$ 恢复为扰动量的磁场数，这与前面所说直接使用磁场数值量度干扰程度的不方便并不矛盾,这里采用的是已经按扰动规范化了的磁场数值。恢复的办法是按表5.10所定规范把 $\kappa$ 与磁场幅度联系起来。

表5.10 $\pmb { \kappa }$ 与等价幅度ak的转换表  

<table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>K</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td></tr><tr><td>ak</td><td></td><td>0</td><td>3</td><td>7</td><td>15</td><td>27</td><td>48</td><td>80</td><td>140</td><td>240</td><td>400</td></tr></table>

不同台站 $a k$ 的单位因子不同,由台站 $\kappa = 9$ 的下限幅度 $R$ 除以250来定。例如标准台（Niemegk） $K \simeq 9$ ， $R = 5 0 0$ ，则 $a k$ 单位为2伽吗。这样由表5.10和 $K = 9$ 的下限幅度 $\pmb R$ 即可确定指数 $\kappa$ 对应的扰动幅度 $a k , i$ 将每天8个 $a k$ 数平均，即得 $\pmb { A } _ { k }$ 指数。由于这里 $a k$ 已变为线性尺度，则指数 $\pmb { A } _ { k }$ 不仅可做为逐日干扰程度的量度，同样可以由 $a k$ 的月,季或年均值来量度逐月或逐年的干扰程度。

同样方式亦可将三小时K,指数按一定规范转换成扰动幅度得到指数Ap，其转换标准如表5.11所示。

表5.11 $\kappa _ { p }$ 与等价幅度 $\pmb { a } \pmb { p }$ 的转换表  

<table><tr><td>K</td><td>0</td><td>0+</td><td>1_</td><td>1</td><td>1+</td><td>2</td><td>2</td><td>2+</td><td>3</td><td>3</td><td>3+</td><td>4_</td><td>4</td><td>4</td></tr><tr><td>ap</td><td>0</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>9</td><td>12</td><td>15</td><td>18</td><td>22</td><td>27</td><td>32</td></tr><tr><td>K,</td><td>5</td><td>50</td><td>5+</td><td>6_</td><td>6</td><td>6+</td><td>7-</td><td>7</td><td>7</td><td>8</td><td>8</td><td>8+</td><td>9_</td><td>9</td></tr><tr><td>ap</td><td>39</td><td>48</td><td>56</td><td>67</td><td>80</td><td>94</td><td>111</td><td>132</td><td>154</td><td>179</td><td>207</td><td>236</td><td>300</td><td>400</td></tr></table>

对于世界标准台 $\pmb { a } \hbar$ 的单位为2伽吗。

此外还有15分钟指数Q和用来反映赤道环电流的月指数“等,这里不再逐一介绍。

# 4.国际地磁静扰日

地磁静扰日的划分对于变化磁场的许多研究是必须的。划分的标准是以K指数为基础，根据世界日每天①8个K指数的和；②8个K,指数的平方和；③8个Kp指数中最大的一个;求出这三个数的平均。其中每月这个平均数最大的五天定为国际磁扰日，由最小的10天再选出五天即为国际磁静日。从这种选择方式可以看出,静扰日并不表示绝对的静扰程度，它有赖于每月实际扰动的强弱。

# （二）太阳静日变化 $\textstyle { \pmb { S _ { q } } }$

太阳静日变化是以太阳日（24小时）为周期的平静日变化，由每月5天磁静日统计得出，通常记作 $\pmb { S _ { q } }$

静日某一时刻Sq的数值为该时刻磁场值减去Sa为零的基线值。零基线一般采用当天的日均值。恰普曼（S.Chapman）和普赖斯（A.T.Price）都曾先后提出，选用夜间值作为Sq基线比起日均值更为适宜。但随后发现,即使在夜间与Sq相联系的高空电流体系也并不为零。因此至今S的基线标准还无定论,通常仍沿用简便的日均值基线[22]。磁静日并非绝对的平静,还会包含一定的干扰成分,这种干扰的多数随机部分可由许多静日相同时刻的数值统计叠加消除之,而磁暴之后地磁场缓慢恢复的所谓“扰后效应”对磁静日的影响，则要通过非周期改正消除。其改正值是把每日地方时24和0的差值线性分配在每一时刻。为了反映S。场的季节差异，上述统计经常按天文季节进行，通常分为冬季(1，2和11，12月），春秋季(3,4和9,10月）和夏季(5,6，7，8月)三个季节。图5.21即为我国部分台站按上述计算步骤所得 $\pmb { S _ { q } }$ 变化。

![](images/5db535d202e681da0250b1b63619fd913d7d161f9c3f0602bcb8db788ac757c8.jpg)  
图5.21 我国六个台站1959年平均日变化S(Y向西为正)自上至下：长春，北京，兰州,余山,拉萨,广州。

下面分段叙述S场的形态,球谐分析和高空电流体系。

# 1. $\pmb { S _ { \pmb { \sigma } } }$ 的形态和纬度变化

Sa除随地方时变化外,在空间不同的地方有不同的特征。不过在同一纬度的各处，其周日变化差异较小，主要是随纬度而变化。图5.22为全球各纬度不同季节水平分量(H)偏角（D)和垂直分量(Z)的Sq变化。由图5.21，5.22不难看出，Sg的周日变化，不同分量规律不同，北向分量X（或H）和垂直分量Z在地方时11"，12附近有一个明显的极值,而另一个极值则不明显;偏角D（或Y)形似正弦波,有两个明显的极值，分别在9和15附近。S,的纬度变化主要表现在，X分量南北半球呈反对称分布(春秋季),在南北30°纬度线上变幅最小，30°南北两侧极值反向，在30N和30°S之间,11"附近有极大值,30°N以北和30°S以南两侧11则为极小值;与此相对应Z分量南北半球为对称分布（春秋季),在赤道附近极值反向，南北30°纬度线变幅最大，偏角D与Z一样在赤道处反相，南北半球呈对称分布(春秋季)，但变幅则是从赤道向南北两侧逐渐增加。从上述 Sa场的时空分布可以看出，南北纬度30°和地方时11附近具有特殊的意义。下面将会看到，这正是S。高空电流体系焦点的位置。S。的季节变化主要是幅度的不同，冬季变幅最小，夏季和春秋相差不大。太阳活动的高年和低年，S场不仅是幅度变化，其相位也有移动。从图5.21可以看出,我国地区的Sa场的时空变化和全球特征是一致的。

# 2. $\pmb { S _ { g } }$ 场的球谐分析

与基本磁场不同Sa场球谐分析同时包括内源场和外源场两部分，且(5.87)式中高斯系数g，h将为时间：的周期函数。因此可将它展成傅氏级数,即

$$
( g _ { n } ^ { m } \cos m \lambda + h _ { n } ^ { m } \sin m \lambda )
$$

$$
\begin{array} { r l r }   { = \sum _ { s = 0 } ^ { \infty } { [ ( g _ { n a } ^ { m , s } \cos { s t ^ { \prime } } + g _ { n b } ^ { m , s } \sin { s t ^ { \prime } } ) \cos { m \lambda } } } \\ & { } & { + ( h _ { n a } ^ { m s } \cos { s t ^ { \prime } } + h _ { n b } ^ { m s } \sin { s t ^ { \prime } } ) \sin { m \lambda } ] _ { 0 } } \end{array}
$$

![](images/2d05017221443874177bf8dcfe88a1d88119ac9eeb39c59f7c11619f3f6306d1.jpg)

![](images/0db9ad855b024f2f34029d1c37405d99874ded4b8126a2aab3a5e557754088a1.jpg)  
图5.22 $s _ { \pmb q }$ 场随纬度的分布[22]

$g _ { n a } ^ { m s } , ~ g _ { n b } ^ { m s } , ~ h _ { n a } ^ { m s }$ 和 $\pmb { h } _ { \pmb { n } \pmb { b } } ^ { m s }$ 分别为 ${ \pmb g } _ { n } ^ { m }$ 和 $\pmb { h } _ { \pmb { n } } ^ { m }$ 的傅氏系数， $\pmb { \prime }$ 为世界时。若采用日均值做为日变场的基线，则(5.162)中 $\pmb { \mathscr { s } }$ 从1开始。利用关系式

$$
t = \lambda + t ^ { \prime } \circ
$$

将(5.162)中世界时 $\prime$ 换成地方时 $\pmb { \ell }$ ，得

$$
g _ { n } ^ { m } c o s m \lambda + h _ { n } ^ { m } \sin m \lambda = \sum _ { s = 1 } ^ { \infty } \left[ g _ { n \cdot a } ^ { m \cdot s } \cos s \lambda \cos m \lambda + h _ { n \cdot b } ^ { m \cdot s } \sin s \lambda \sin m \lambda \right.
$$

$$
+ \ g _ { n \cdot b } ^ { m \cdot s } \sin s \lambda \cos m \lambda + \ h _ { n \cdot a } ^ { m \cdot s } \cos s \lambda \sin m \lambda ] \cos s t + [ g _ { \pi \cdot a } ^ { m \cdot s } \sin s \lambda \cos m \lambda
$$

$$
- \left. h _ { n \cdot a } ^ { m \cdot s } \cos s \lambda \sin m \lambda + h _ { n \cdot a } ^ { m \cdot s } \sin s \lambda \sin m \lambda - g _ { n \cdot b } ^ { m \cdot s } \cos s \lambda \cos m \lambda \right] \sin s t
$$

$$
\begin{array} { l } { { \displaystyle = \sum _ { s = 1 } ^ { \infty } \left[ \widehat { p } _ { n \cdot a } ^ { m \cdot s } \cos \left( m + s \right) \lambda + q _ { n \cdot a } ^ { m \cdot s } \sin \left( m + s \right) \lambda + r _ { n \cdot a } ^ { m \cdot s } \cos \left( m - s \right) \lambda \right. } } \\ { { \displaystyle \qquad + \left. \widehat { h } _ { n \cdot a } ^ { m \cdot s } \sin \left( m - s \right) \lambda \right] \cos s t + \left[ \widehat { p } _ { n \cdot b } ^ { m \cdot s } \cos \left( m + s \right) \lambda + q _ { n \cdot b } ^ { m \cdot s } \sin \left( m + s \right) \lambda \right. } } \\ { { \displaystyle \qquad + \left. r _ { n \cdot b } ^ { m \cdot s } \cos \left( m - s \right) \lambda + k _ { n \cdot b } ^ { m \cdot s } \sin \left( m - s \right) \lambda \right] \sin s t _ { 0 } } } \end{array}
$$

考虑到 $\pmb { S _ { q } }$ 的空间分布主要是随纬度变化，做为近似，假定它与经度无关，则（5.163）只有一种可能的选择,即 $m = s , p = q = 0 ,$ 。这时(5.163)简化为

$$
g _ { n } ^ { m } \cos m \lambda + h _ { n } ^ { m } \sin m \lambda = \sum _ { m = 1 } ^ { n } r _ { n \cdot a } ^ { m } \cos \varepsilon t + r _ { n \cdot b } ^ { m } \sin s t _ { 0 }
$$

将(5.164)代人(5.86)并仍沿用符号 $\big \{ \big \} \setminus h ;$ 得

$$
\begin{array} { l } { { \displaystyle W = a \sum _ { n = 1 } ^ { \infty } \sum _ { m = 1 } ^ { n } \left\{ \left[ \left( \frac { a } { r } \right) ^ { n + 1 } g _ { n } ^ { m i } + \left( \frac { r } { a } \right) ^ { n } g _ { n } ^ { m e } \right] \cos m t \right. } } \\ { { \displaystyle \qquad + \left. \left[ \left( \frac { a } { r } \right) ^ { n + 1 } h _ { n } ^ { m i } + \left( \frac { r } { a } \right) ^ { n } h _ { n } ^ { m e } \right] \sin m t \right\} P _ { n } ^ { m } ( \cos \theta ) _ { 0 } } } \end{array}
$$

虽然（5.165)与（5.161)形式相似,但两者系数意义不同，这里 $g , h$ 是高斯系数的傅氏系数,已不再是时间 $\pmb { \mathscr { t } }$ 的函数。在地球表面(5.165)简化为:

$$
\begin{array} { r l } {  { W | _ { m = \infty } = a \sum _ { n = 1 } ^ { \infty } \sum _ { m = 1 } ^ { n } ( a _ { n } ^ { \ m } \cos m t + b _ { n } ^ { m } \sin m t ) P _ { n } ^ { m } ( \cos \theta ) } } \\ & { = a \sum _ { n = 1 } ^ { \infty } \sum _ { m = 1 } ^ { n } [ E _ { n } ^ { m } \cos ( m t + \varepsilon _ { n } ^ { m } ) + I _ { n } ^ { m } \cos ( m t + L _ { n } ^ { m } ) ] P _ { n } ^ { m } ( \cos \theta ) } \\ & { = a \sum _ { n = 1 } ^ { \infty } \sum _ { m = 1 } ^ { n } [ C _ { n } ^ { m } \cos ( m t + \delta _ { n } ^ { m } ) ] P _ { n } ^ { m } ( \cos \theta ) _ { 0 } } \end{array}
$$

其中

$$
\left. { \begin{array} { l } { a _ { n } ^ { m } = g _ { n } ^ { m i } + g _ { n } ^ { m e } ; \quad b _ { n } ^ { m } = h _ { n } ^ { m i } + h _ { n } ^ { m e } _ { 0 } } \\ { ( E _ { n } ^ { m } ) ^ { 2 } = ( g _ { n } ^ { m e } ) ^ { 2 } + ( h _ { n } ^ { m e } ) ^ { 2 } ; \enspace ( l _ { n } ^ { m } ) ^ { 2 } = ( g _ { n } ^ { m i } ) ^ { 2 } + ( h _ { n } ^ { m i } ) ^ { 2 } _ { 0 } } \\ { \tan \varepsilon _ { n } ^ { m } = { \frac { h _ { n } ^ { m e } } { g _ { n } ^ { m e } } } ; \tan L _ { n } ^ { m } = { \frac { h _ { n } ^ { m i } } { g _ { n } ^ { m i } } } \circ } \\ { ( C _ { n } ^ { m } ) ^ { 2 } = ( a _ { n } ^ { m } ) ^ { 2 } + ( b _ { n } ^ { m } ) ^ { 2 } ; \enspace \tan \delta _ { n } ^ { m } = { \frac { b _ { n } ^ { m } } { a _ { n } ^ { m } } } } \end{array} } \right\}
$$

北向分量 $( X )$ ，东向分量（Y）和垂直分量 $( z )$ ，可由(5.165)微分求出,在地球表面

$$
\begin{array} { l } { { \left. { \cal X } = \displaystyle \frac { \partial { \cal W } } { r \partial \theta } \right| _ { r = a } = \sum _ { n = 1 } ^ { \infty } \sum _ { m = 1 } ^ { \infty } \left( a _ { n } ^ { m } \cos m t + b _ { n } ^ { m } \sin m t \right) \displaystyle \frac { \partial P _ { n } ^ { m } ( \cos \theta ) } { \partial \theta } , } } \\ { { \left. \mathrm { \cal Y } = - \displaystyle \frac { 1 } { r \sin \theta } \displaystyle \frac { \partial { \cal W } } { \partial \lambda } \right| _ { r = a } = \sum _ { n = 1 } ^ { \infty } \sum _ { m = 1 } ^ { n } \left( a _ { n } ^ { m } \sin m t - b _ { n } ^ { m } \cos m t \right) \displaystyle \frac { m P _ { n } ^ { m } ( \cos \theta ) } { \sin \theta } , } } \\ { { \left. { \cal Z } = \displaystyle \frac { \partial { \cal W } } { \partial r } \right| _ { r = a } = \sum _ { n = 1 } ^ { \infty } \sum _ { m = 1 } ^ { n } \left( \alpha _ { n } ^ { m } \cos m t + \beta _ { n } ^ { m } \sin m t \right) P _ { n } ^ { m } ( \cos \theta ) _ { 0 } } } \end{array}
$$

其中

$$
\begin{array} { c } { { \alpha _ { n } ^ { m } = n g _ { n } ^ { m e } - ( n + 1 ) g _ { n } ^ { m i } , } } \\ { { \beta _ { n } ^ { m } = n h _ { n } ^ { m e } - ( n + 1 ) h _ { n } ^ { m i } . } } \end{array} \}
$$

(5.168)可改写为

$$
\begin{array} { l } { { \displaystyle { \cal X } = \sum _ { m = 1 } \left[ \left( \sum _ { n = m } ^ { \infty } a _ { n } ^ { m } { \frac { \partial P _ { n } ^ { m } \left( \cos \theta \right) } { \partial \theta } } \right) \cos m t + \left( \sum _ { n = m } ^ { \infty } b _ { n } ^ { m } { \frac { \partial P _ { n } ^ { m } \left( \cos \theta \right) } { \partial \theta } } \right) \sin m t \right] } } \\ { { \displaystyle ~ = \sum _ { m = 1 } ^ { \infty } \left( a _ { m } ^ { x } \cos m t + b _ { m } ^ { x } \sin m t \right) } , } \end{array}
$$

其中 $a _ { m } ^ { \star } , \ b _ { m } ^ { \star }$ 是 $x$ 分量的傅氏系数：

$$
\begin{array} { l } { { a _ { m } ^ { x } = \displaystyle \sum _ { n = m } ^ { \infty } \bigg ( a _ { n } ^ { m } ~ { \frac { \partial P _ { n } ^ { m } ( \cos \theta ) } { \partial \theta } } \bigg ) , } } \\ { { b _ { m } ^ { x } = \displaystyle \sum _ { n = m } ^ { \infty } \bigg ( b _ { n } ^ { m } ~ { \frac { \partial P _ { n } ^ { m } ( \cos \theta ) } { \partial \theta } } \bigg ) _ { 0 } , } } \end{array}
$$

对于Y，Z分量有与(5.170)(5.171)相似的结果,相应的傅氏系数为 $a _ { m } ^ { \texttt { Y } } , \ b _ { m } ^ { \texttt { Y } } , \ a _ { m } ^ { \texttt { Z } } , \ b _ { m } ^ { \texttt { Z } }$ ，它们与球谐系数的关系为：

$$
\begin{array} { l } { { a _ { m } ^ { \Psi } = \displaystyle - \sum _ { n = m } ^ { \infty } b _ { n } ^ { m } { \frac { m P _ { n } ^ { m } \left( \cos \theta \right) } { \sin \theta } } , } } \\ { { b _ { m } ^ { \Psi } = \displaystyle \sum _ { n = m } ^ { \infty } a _ { n } ^ { m } { \frac { m P _ { n } ^ { m } \left( \cos \theta \right) } { \sin \theta } } _ { 0 } } } \\ { { a _ { m } ^ { z } = \displaystyle \sum _ { n = m } ^ { \infty } \alpha _ { n } ^ { m } P _ { n } ^ { m } ( \cos \theta ) , \left. \right\} } } \\ { { b _ { m } ^ { z } = \displaystyle \sum _ { n = m } ^ { \infty } \beta _ { n } ^ { m } P _ { n } ^ { m } ( \cos \theta ) _ { 0 } } } \end{array}
$$

分析工作就是根据（5.170)，首先求出各不同纬度台站日变场 $\pmb { S _ { q } }$ 的相应分量的傅氏系数$a _ { m } , \ b _ { m }$ ，再由（5.171)一(5.173）用最小二乘法解出球谐系数 $a _ { n } ^ { m } , b _ { n } ^ { m }$ 和 $\pmb { \alpha _ { n } ^ { m } }$ ， $\beta _ { n } ^ { m }$ ，并可根据(5.167),(5.169)将内外场区分开来。实际分析表明，日变场的傅氏分析取 $m = 4$ 已足够精确。图5.23为我国长春台取 $m = 4$ 的 $X$ 分量的计算值与观测值的比较，可以看到，除个别点稍有偏离外，两者几近一致。

![](images/8111fa3e5b50d27628f9bc6054415d6648fbbd450d5f2aafbbe88c9177b7115e.jpg)  
图5.23长春台1959年全年平均X分量观测值与傅氏分析计算值的比较(取m=4)[2s]细实线：日变傅氏级数各次谐波粗虚线：4次谐波叠加值和实测值 $^ +$ 偏离叠加值的实测值

1889 年舒斯特（A．Schuster）首先把高斯球谐分析用于Sq场，随后恰普曼，长谷川(M.Hasegawa)等人应用舒斯特方法获得了全球Sa场分析的重要结果。表5.12、5.13为各个作者所得不同年代Sq场的球谐系数C",8（见公式5.166),外场与内场幅度之比E"/I和位相差ε”一L"由表5.12看出,在地球表面Sa外场与内场之比约为3:1,内场位相落后外场约一小时。在表5.12、5.13中,春秋季和冬夏平均的Sq仅包含“十m为奇数之球谐函数,这表明与其相联系的场势相对于赤道呈对称分布,而夏冬两季之差则仅有”十m为偶数之球谐系数,即场势相对于赤道是反对称的，这与上述Sa场的纬度变化特征相符。

# 3. $\pmb { S _ { q } }$ 场的电流体系

观测已经证明，Sa的电流体系位于电离层的E区，因此首先简要叙述一下电离层的概貌。大约在50公里高度以上,大气由于太阳的光辐射而被电离,部分中性原子分解为正离子和电子,从而形成所谓电离层。因电离过程和离子成分的区别,电离层分为D,E,F,氨和质子等五个区。D区又可分为C,D两层,E、F区也各自分为E,E和F，F,层(图5.24)。各层高度并不完全确定,其典型高度和主要成分为：C层最低。C,D层分界约在70 公里,D层上界约在90 公里，该区正离子大部分是N+，负离子是电子和O，虽然这一层离地面最近,但因对电磁波的吸收很强,粒子自由程短，不易观测，所以性质却是了解最差的一个区； $\boldsymbol { \varepsilon }$ 区约由90公里至120一150公里，$\pmb { F }$ 层与氨层，氨层与质子层界面高度各自约为500公里和800公里，其离子成份，各层（ $\dot { D }$ 除外)主要负离子均为电子， $E , F$ 层正离子为 ${ \mathrm { O } } _ { 2 } ^ { + }$ ， $\mathbf { N } _ { 0 } ^ { + }$ ， ${ \pmb F } _ { 2 }$ 层为 $\mathrm { O ^ { + } }$ ，氮层和质子层分别为 $H _ { e } ^ { + }$ 和 $H ^ { + }$ 。各层电子浓度以 $D$ 区最低，其随高度的变化如图5.24所示。电离层为完全中性部分电离的气体，，有较好的导电性能。由于太阳、月亮的潮汐作用以及压力温度的变化，电离层将产生以水平向为主的运动，这种运动和地磁场相互作用即产生涡电流，这就是通常所说的"发电机”效应。 $S _ { q }$ 电流体系正是电离层这种发电机效应的结果。从图5.24可见， $E , F$ 层都有较高的电子浓度，为什么 $S _ { q }$ 的电流体系不在F区而在E区呢？这主要是由于两层电导率的差异。电离气体的电导率不仅取决于电子浓度，还与各种离子质量，电荷自由程以及周围磁场的强度和方向有关。沿磁场的方向电导率较大,而在磁场的垂直方向电导率较小。这由方程（5.27）磁场的"冻结"效应不难理解。正是由于磁场的存在，电离层的电导率将是各向异性的。若忽略电离层的厚度，这种各向异性电导率可用一阶张量表示。为了便于比较，表5.14列出了EF两层不同地磁纬度的电导率。由表5.14明显看出，在E层其电导率要较F层高一个量级或更多。因此Sq电流体系处于E层就不难理解了。这里我们不准备叙述S。发电机效应的数学理论，只重点介绍如何由地面S。场的实际分析确定该电流体系的分布。

<table><tr><td colspan="3">作 者</td><td colspan="4">Chapman (1919)</td><td colspan="2">Mchich (1937)</td><td colspan="2">Hasegawa &amp; otu （1950)</td><td colspan="2">Matsushita &amp; Maeda</td></tr><tr><td>年 黑 台</td><td colspan="2">代 子 数 站 数</td><td colspan="2">1902 5（低） 21</td><td colspan="2">1905 64（高） 21</td><td colspan="2">1923 6（低） 5</td><td colspan="2">1932--1933 8（低） 46</td><td colspan="2">1958 185（高） 69</td></tr><tr><td></td><td>m</td><td>”</td><td>E/1</td><td>s-L（度）</td><td>E/1</td><td>L （度）</td><td>E/</td><td>e-L</td><td>E/</td><td>e-L</td><td>E/</td><td>8-L（度）</td></tr><tr><td rowspan="5">冬夏季平均</td><td>1</td><td>2</td><td>3.0</td><td>120</td><td>2.8</td><td>10.3</td><td></td><td></td><td>2.3</td><td>109</td><td>2.7</td><td>-13</td></tr><tr><td>2 3</td><td>3 4</td><td>2.2</td><td>-18</td><td>2.3</td><td>119</td><td></td><td></td><td>2.4</td><td>-10</td><td>2.3</td><td>-15</td></tr><tr><td>平</td><td>均</td><td>2.4</td><td>-21</td><td>2.7</td><td>-20</td><td></td><td></td><td>2.2</td><td>-14</td><td>2.2</td><td>109</td></tr><tr><td></td><td></td><td>2.5</td><td>-20</td><td>2.6</td><td>-14</td><td></td><td></td><td>2.3</td><td>-11</td><td>2.4</td><td>-12</td></tr><tr><td colspan="2">加权平均*</td><td>2.6</td><td>-20</td><td>2.6</td><td>-10</td><td></td><td></td><td>2.3</td><td>-10</td><td>2.5</td><td>-13</td></tr><tr><td rowspan="5">春秋季</td><td>1</td><td>2 3</td><td>2.7</td><td>-23</td><td>2.9</td><td>10.5</td><td>2.4</td><td>-21</td><td></td><td></td><td>2.8</td><td>-13</td></tr><tr><td>2</td><td>4</td><td>2.0</td><td>-17</td><td>2.4</td><td>-18</td><td>2.1</td><td>-13</td><td></td><td></td><td>2.3</td><td>-13</td></tr><tr><td>3 平 </td><td>均</td><td>2.5</td><td>-21</td><td>2.4</td><td>-21</td><td>1.9</td><td>102</td><td></td><td></td><td>2.2</td><td>-11</td></tr><tr><td></td><td></td><td>2.4</td><td>120</td><td>2.6</td><td>-i5</td><td>2.1 2.2</td><td>-12 -16</td><td></td><td></td><td>2.4</td><td>-14</td></tr><tr><td colspan="2">加权平均</td><td>2.5</td><td>-21</td><td>2.7</td><td>-11</td><td></td><td></td><td></td><td></td><td>2.6</td><td>-13</td></tr></table>

<table><tr><td colspan="2">作</td><td colspan="2">者</td><td colspan="2">Schuster Frisch （1889）</td><td colspan="2">（1905)</td><td colspan="2">Chapman （1919）</td><td colspan="2">Benkova (1940)</td><td colspan="2">Hasegawa （1950）</td><td colspan="9">Matsuchita and Macda （1965a)</td></tr><tr><td colspan="3">年代 黑子数</td><td colspan="2">1870 139（高）</td><td colspan="2">1840-1896 混合</td><td colspan="3">1902 1905</td><td colspan="2">1933</td><td colspan="2">1932--1933 8（低）</td><td colspan="8">1958</td></tr><tr><td colspan="3">台站数</td><td colspan="2">4</td><td colspan="2">18</td><td colspan="3">5（低） 64（高） 21 21</td><td colspan="2">6（低） 46</td><td colspan="8">185（高） 46 69</td></tr><tr><td rowspan="2">季</td><td colspan="2">节 m</td><td colspan="3">A (A + A)/2</td><td colspan="3">(An+A)/2</td><td colspan="2">(A + A)/2 （A+W）/2</td><td colspan="2">(A+A)/2</td><td colspan="2">(E+Es)/2</td><td colspan="2">(x, + Y:)/2</td><td colspan="3">（A+A)/2</td><td>（△,+△）/</td></tr><tr><td>1 奇 2</td><td>n 2</td><td>C（x）（0） 15.4</td><td>024</td><td>c(x）（0） 10.2</td><td>030</td><td>c（x）6（0） 035</td><td>10.1</td><td>cm(x)o（0）</td><td>CR(r）</td><td>6（0） 019</td><td>c（r）（0）</td><td></td><td>C（x）0（0）</td><td></td><td>C（xon（0）</td><td></td><td>c（x）（0） 004</td><td>C(r)6（0） 0.1</td><td></td></tr><tr><td colspan="2"></td><td>3 4</td><td>7.1 3.2</td><td>211 067</td><td colspan="2">4.8 205 2.1 035</td><td>7.0 4.5 215 2.1</td><td colspan="2">5.9 047 2.7</td><td>024 207 040</td><td>7.5 4.2 209 1 1</td><td>10.5 5.2 1.6</td><td colspan="2">014 21.8 198 11.3 040 4.5</td><td>358 190 012</td><td>19.5 9.7 3.7</td><td>002 192 025</td><td>18.4 8.9 3.3</td><td>193 034</td><td>1.2 0.7</td><td>056 129 304</td></tr><tr><td colspan="3">季 节</td><td></td><td>:</td><td colspan="2">（△,+△,）/2（</td><td>（△,+△）/2(（△,+△,）/2|</td><td colspan="2"></td><td colspan="2"></td><td>(s.-w)/2</td><td colspan="3">（△+△）/2</td><td>(E.-E)/2</td><td></td><td colspan="2">(Y-Y)/2</td><td>（A-A)/2</td><td>（△,+△.）/2</td><td></td></tr><tr><td rowspan="7">偶</td><td>m</td><td>n</td><td></td><td>c(x）o（0）</td><td colspan="2">C(r）（0）</td><td></td><td colspan="2">c（x）（0）</td><td>c（x）（0）</td><td colspan="2">c(x） （0）</td><td colspan="2">c(x）8（0）</td><td>C(r）（0）</td><td></td><td>c（x（0）</td><td></td><td></td><td colspan="2">c（r）（0）</td><td>Cn（x） 5（0）</td></tr><tr><td>1</td><td>1</td><td>5.4</td><td>027</td><td>5.9</td><td>028</td><td></td><td>023</td><td>4.7</td><td>027</td><td>5.0</td><td colspan="2">039</td><td></td><td></td><td></td><td></td><td></td><td colspan="2"></td><td></td></tr><tr><td>1</td><td>3</td><td>2.5</td><td>311</td><td>1.5</td><td>247</td><td>4.3 2.1</td><td>344</td><td>2.8</td><td>337</td><td>0.8 318</td><td>3.8 0.9</td><td>005 339</td><td>2.9 2.7</td><td>281 267</td><td>2.3</td><td>320</td><td>2.2 1.8</td><td>310 1 251</td><td>6.5 064</td></tr><tr><td>2</td><td>2</td><td>3.9</td><td>255</td><td>2.9</td><td>242</td><td>2.1</td><td>343</td><td>3.0</td><td>243</td><td>2.8</td><td>244</td><td>0.9 198</td><td>5.1</td><td>246</td><td>2.1</td><td>258 239</td><td>2.3</td><td>232</td><td>0.9 076 3.4</td></tr><tr><td>2</td><td>4</td><td>0.9</td><td>162</td><td>1.0</td><td>186</td><td>1.1</td><td>205</td><td>0.9</td><td>210</td><td>0.9 194</td><td>0.4</td><td>203</td><td>0.9</td><td>148</td><td>3.2 0.4</td><td>141</td><td>0.1 113</td><td>0.9</td><td>246 201</td></tr><tr><td>3</td><td>3</td><td>1</td><td>1</td><td>1.4</td><td>088</td><td>1.2</td><td>091</td><td>1.4</td><td>104</td><td>1 1</td><td>1</td><td>，~</td><td>3.4</td><td>082</td><td>2.0</td><td>078</td><td>1.3 072</td><td>2.0</td><td>067</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

![](images/22ebe4bc6e87f647bfff04b29eb7508db7a974bc47ff190657cff516793f27b3.jpg)  
图5.24电离层分区和电子浓度的高度变化图[2]

设电离层E为与地心O同心,半径为R的球层（图5.25)。层上电流密度为(θ',2')，考虑 ${ \bf { } } j ( \theta ^ { \prime } , \lambda ^ { \prime } )$ 为无源场， $\nabla \cdot \pmb { j } = 0$ ，可定义电流函数 $\varPsi _ { e } ( \theta ^ { \prime } , \lambda ^ { \prime } )$

$$
\pmb { j } = \nabla \varPsi _ { e } \times \pmb { e } _ { r }
$$

表5.14 D、E、 ${ \pmb F }$ 层不同地磁纬度的电导率（单位：e．m.u.）  

<table><tr><td>磁纬(度）</td><td>区</td><td>Σxx</td><td>Ey</td><td>E，，</td></tr><tr><td rowspan="3">0</td><td>F</td><td>4.30×10-3</td><td>0</td><td>8.81×10-10 7.58×10-8</td></tr><tr><td>E</td><td>6.90×10-</td><td>0</td><td>7.97×10-10</td></tr><tr><td>D</td><td>7.78×10-10</td><td>0</td><td></td></tr><tr><td rowspan="3">30°</td><td>F</td><td>3.52×10</td><td>2.14×10-u 1.89×10-8</td><td>8.81×10-10 5.64×10-9</td></tr><tr><td>E</td><td>2.16×10-8 5.47×10-10</td><td>2.95×10-10</td><td>5.46×10-10</td></tr><tr><td>D</td><td></td><td></td><td></td></tr><tr><td rowspan="3">60°</td><td>F E</td><td>1.17×10- 7.21×10-</td><td>1.24×10- 1.09×10-8</td><td>8.81×10-10 5.44×10-9</td></tr><tr><td></td><td>3.91×10-10</td><td>2.99×10-10</td><td>3.91×10-10</td></tr><tr><td>D</td><td></td><td></td><td></td></tr><tr><td rowspan="3">90°</td><td>F</td><td>8.81×10-10</td><td>1.07×10-1 9.44×101</td><td>8.81×10-10 5.45×10-9</td></tr><tr><td>E</td><td>5.45×10-9</td><td>3.26×10-10</td><td>3.58×10-10</td></tr><tr><td>D</td><td>3.58×10-10</td><td></td><td></td></tr></table>

Σxx，Σxy，Σ,，为各向异性电导率的一阶张量元素,x向南,y向东。

![](images/d0d5bc595c23c2e553a93fbb7a8a9c6ef0ed990812665a5345a9bd484f56c326.jpg)  
图>.25

![](images/b0244f004a65ea9e8526c9bc7e1436f73f5cd51dbe8fa5a87c6e3242e4632b83.jpg)  
图5.26

即

$$
\left. \begin{array} { r } { { \frac { \partial \Psi _ { e } ( \theta ^ { \prime } , \lambda ^ { \prime } ) } { r \sin \theta ^ { \prime } \partial \lambda ^ { \prime } } = j e _ { \theta } , } } \\ { { - \frac { \partial \Psi _ { e } ( \theta ^ { \prime } , \lambda ^ { \prime } ) } { r \partial \theta } = r e _ { \lambda \circ } } } \end{array} \right\}
$$

$\pmb { \ U } _ { e } ( \theta \lambda )$ 的等值线有两个重要性质： $\textcircled{1}$ 等值线与电流密度 $\pmb { j }$ 的流线重合。这由图5.26所示等值线 $\Psi ( \theta \mathfrak { a } ) = \mathfrak { c } _ { 1 }$ 上任一点 $\pmb { P }$ 的切线

$$
\tan \alpha = \left. { \frac { \partial \varPsi } { r \sin \theta \partial \lambda } } \right| _ { P } \Biggl / \left. { \frac { \partial \varPsi } { r \partial \theta } } \right| _ { P } \circ
$$

正好等于 $- \frac { j e _ { \theta } } { \jmath e _ { \lambda } }$ ，不难证明。 $\textcircled{2}$ 相邻两等值线 $\pmb { \psi }$ 的差,即为流过两等值线间的电流强度。证明如下：设 $\Psi ( \theta , \lambda ) = C _ { 1 }$ 和 $C _ { 2 }$ 的两等值线间流过的电流强度为 $\pmb { I }$ （图5.26）

$$
I = \int _ { P } ^ { \varrho } j \cdot n d S ,
$$

$\pmb { \mathscr { n } }$ 为 $\pmb { s }$ 的法线,取 $\smash { \ z \ z \ } $ 与向量 $\pmb { r }$ 为右于螺旋,则

$$
\pmb { j } \cdot \pmb { n } = \frac { \partial \Psi } { \partial S } ,
$$

于是

$$
I = \int _ { \bar { r } } ^ { \varrho } \frac { \partial \varPsi } { \partial S } d S = \int _ { \bar { r } } ^ { \varrho } d \varPsi = C _ { \mathrm { z } } - C _ { \mathrm { \mathbf { 1 } } } 
$$

$\pmb { \cal I }$ 为相邻 $\pmb { \psi }$ 等值线的差。由 $\Psi _ { \epsilon }$ 的上述性质不难得出 $\Psi ( \theta ^ { \prime } , \lambda ^ { \prime } )$ 所定义的电流 $\pmb { j }$ 在地面观测点 $P ( \theta , \lambda )$ 的磁势

$$
W _ { e } ( \theta , \lambda ) = \int \int \varPsi _ { e } ^ { \prime } ( \theta ^ { \prime } , \lambda ^ { \prime } ) \frac { \partial } { \partial r } \ \frac { 1 } { \rho } d S ^ { \prime } { } _ { \circ }
$$

积分遍及半径为 $\pmb { R }$ 的球层（图5.25)，由图5.26三角形 $O P E$ 可以得出

$$
\rho ^ { \prime } = r ^ { \prime } + a ^ { 2 } - 2 a r \cos \delta = r ^ { 2 } \Bigl [ 1 - 2 \Bigl ( \begin{array} { c } { { a } } \\ { { r } } \end{array} \Bigr ) \cos \delta + \Bigl ( \frac { a } { r } \Bigr ) ^ { 2 } \Bigr ]
$$

$$
\frac { 1 } { \rho } = \frac { 1 } { r } \left[ 1 - 2 \left( \frac { a } { r } \right) \cos \delta + \left( \frac { a } { r } \right) ^ { 2 } \right] ^ { - \frac { 1 } { 2 } } \circ
$$

(5.176)方括号部分是关于 $\cos \delta$ 的勒让德函数的母函数即

$$
\left. \begin{array} { l } { \displaystyle \frac { 1 } { \rho } = \sum _ { n = 1 } ^ { \infty } \frac { a ^ { n } } { r ^ { n + 1 } } P _ { n } \big ( \cos \delta \big ) , } \\ { \displaystyle \frac { \partial } { \partial r } \left( \frac { 1 } { \rho } \right) = - \sum _ { n = 1 } ^ { \infty } \left( n + 1 \right) \sum _ { r ^ { n + 2 } } P _ { n } \big ( \cos \delta \big ) _ { 0 } } \end{array} \right\}
$$

利用关系式

$$
\cos \delta = \cos \theta \cos \theta ^ { \prime } + \sin \theta \sin \theta ^ { \prime } \cos ( \lambda ^ { \prime } - \lambda ) \circ
$$

将 $P _ { n } ( \cos \delta )$ 转变为对于极轴 $o N$ ，即关于 $\theta , \theta ^ { \prime } , \lambda , \lambda ^ { \prime }$ 的球面函数，

$$
P _ { n } ( \cos \delta ) = \sum _ { m = 0 } ^ { n } P _ { n } ^ { m } ( \cos \theta ^ { \prime } ) P _ { n } ^ { m } ( \cos \theta ) \cos { m ( \lambda ^ { \prime } - \lambda ) _ { 0 } }
$$

同样，流函数 $\phi ( \theta ^ { \prime } , \lambda ^ { \prime } )$ 亦可展成关于 $\theta ^ { \prime } , \lambda ^ { \prime }$ 的球面函数，

$$
\varPsi _ { \epsilon } ( \theta ^ { \prime } , \lambda ^ { \prime } ) = \sum _ { l = 1 } ^ { \infty } \sum _ { k = 0 } ^ { l } \varPsi _ { \epsilon } ^ { \star l } = \sum _ { l = 1 } ^ { \infty } \sum _ { k = 0 } ^ { l } \left( \alpha _ { l } ^ { \prime k } \cos k \lambda ^ { \prime } + b _ { l } ^ { \prime k } \sin k \lambda ^ { \prime } \right) P _ { l } ^ { \star } ( \cos \theta ^ { \prime } ) _ { 0 }
$$

由(5.177),(5.178)和(5.179)可以得到

$$
W ( \theta , \lambda ) = \int \int \Bigl [ \sum _ { n = 1 } ^ { \infty } \sum _ { m = 0 } ^ { n } - ( n + 1 ) \frac { a ^ { n } } { r ^ { n + 2 } } P _ { n } ^ { m } ( \cos \theta ^ { \prime } ) P _ { n } ^ { m } ( \cos \theta ) \cos m ( \lambda ^ { \prime } - \lambda ) \Bigr ]
$$

$$
\times \sum _ { l = 1 } ^ { \infty } \sum _ { k = 0 } ^ { l } [ ( a _ { l } ^ { \prime _ { k } } \cos k \lambda ^ { \prime } + b _ { l } ^ { \prime _ { k } } \sin k \lambda ^ { \prime } ] P _ { l } ^ { k } ( \cos \theta ^ { \prime } ) ] d S _ { \circ } ^ { \prime }
$$

由球面函数的正交性(5.89)式不难相信，(5.180)只有当 $l = n , k = m$ 时才不为零。积分结果可得：

$$
\begin{array} { r l r } { W _ { \epsilon } ( \theta , \lambda ) = - } & { \displaystyle \sum _ { n = 1 } ^ { \infty } \sum _ { m = 0 } ^ { n } \frac { 4 \pi ( n + 1 ) } { 2 n + 1 } \left( \frac { \alpha } { R } \right) ^ { n } [ a _ { n } ^ { \prime _ { m } } \cos m \lambda + b _ { n } ^ { \prime _ { m } } \sin m \lambda ] P _ { n } ^ { m } ( \cos \theta ) } & \\ & { \displaystyle \quad \quad = - \sum _ { n = 1 } ^ { \infty } \sum _ { m = 0 } ^ { n } \frac { 4 \pi ( n + 1 ) } { 2 n + 1 } \left( \frac { \alpha } { R } \right) ^ { n } \bar { \Psi } _ { n } ^ { m / } ( \theta , \lambda ) _ { 0 } } & { ( 5 . } \end{array}
$$

由磁势W(0,)在地球表面的球谐分析结果(5.166)中外源场部份和(5.181)比较,可得

$$
\begin{array} { l } { { \displaystyle \varPsi _ { e } ( \theta , \ t ) \ = \ \sum _ { n = 1 } ^ { \infty } \sum _ { m = 0 } ^ { n } \phi _ { n e } ^ { m } ( \theta , t ) } } \\ { { \displaystyle \ = - \ \sum _ { i \pi } \sum _ { n = 1 } ^ { \infty } 2 _ { \ n } ^ { \circ } \frac { 1 } { n } \left( \frac { R } { a } \right) ^ { n } \sum _ { m = 0 } ^ { n } \left[ g _ { n l } ^ { m } \cos m t + n _ { n l } ^ { m } \sin m t \right] P _ { n } ^ { m } ( \cos \theta ) } } \\ { { \displaystyle \ = - \ \sum _ { i \pi } \sum _ { n = 1 } ^ { \infty } \frac { 2 n } { \pi } \frac { 1 } { + 1 } \left( \frac { R } { a } \right) ^ { n } \sum _ { m = 0 } ^ { n } E _ { n } ^ { m } \cos \left( m t + \varepsilon _ { n } ^ { m } \right) } , } \end{array}
$$

或简化为

$$
\phi _ { n l } ^ { m } \left( \theta , t \right) = - \frac { 1 } { 4 \pi } \frac { 2 n + 1 } { n + 1 } \left( \frac { R } { a } \right) ^ { n } W _ { n l } ^ { m } \left( \theta , t \right) ,
$$

若S在地球表面的外源场球谐系数g、h或E”、已知，则由(5.182)即可求出相应外源场的电流函数(0,t),i的等值线即为电流线,流线方向由(5.174)决定，。相邻两等值线之差就是在它们之间通过的电流强度。（5.182）各量均为电磁单位(e.m.u.）。若

![](images/27260777d645cb12ea43554dad400f1e20e19feb957674717e8a2ba3169e98b1.jpg)  
图5.27 $s _ { q }$ 外源 $( \mathfrak { a } )$ ,内源(b）电流体系[2]相邻流线间电流强度为 $2 5 \times 1 0 ^ { 3 }$ 安培,实线为反时针方向,虚线顺时针方向，粗实线为零线，涡旋中心总电流强度单位为 $1 0 ^ { 3 }$ 安培

$\pmb { \phi }$ 以安培为单位,则需要乘以因子10，即

$$
\phi _ { n } ^ { m l } = - \frac { 1 0 } { 4 \pi } \frac { 2 n } { n } \frac { + 1 } { + 1 } \Big ( \frac { R } { a } \Big ) ^ { n } { \cal W } _ { n l } ^ { m } \circ
$$

式(5.184)中 $W _ { n l } ^ { m }$ ，若 $\pmb { \alpha }$ 以公里， $8 ^ { m } \setminus h _ { n l } ^ { m }$ 以伽吗为单位，则 $\pmb { \phi }$ 单位仍为安培。同样可以得出相应内原场的电流函数 $\phi _ { n _ { t } } ^ { m }$ ，

$$
\phi _ { n _ { i } } ^ { m } = \frac { 1 0 } { 4 \pi } \frac { 2 n + 1 } { n + 1 } \bigg ( \frac { a } { r _ { 0 } } \bigg ) ^ { n + 1 } W _ { n _ { i } } ^ { m } ,
$$

其中 $\yen 0$ 为内部电流体系的球层半径。在第六章地球内部的电磁感应一节将指出，内部电流正是外部电流体系感应的结果。图 $5 . 2 7 a , b$ 为国际地球物理年期间 $( \operatorname { I G Y } ) s _ { q }$ 场的外源和内源平均电流体系。电流体系有四个涡流中心,南北各两个。夜间的强度远小于白天。最强的涡旋中心约在南北地磁纬度 $3 0 ^ { \circ }$ 和地方时 $1 1 ^ { h } , 1 2 ^ { h }$ 附近，这与 $s _ { q }$ 场的时空规律相一致。但在春秋季南北半球电流体系并不完全对称。

# 4. $\pmb { S _ { q } }$ 场的经度效应和赤道异常

(5165)，(5.166)是在假定同一地方时 $s _ { q }$ 场与经度无关的条件下确立的。这一假定抓住了 $S _ { q }$ 场性质的主要方面，简化了分析方法，揭示了 $s _ { q }$ 场空间分布的基本规律。但Sa仍然存在着经度差异,即除随地方时变化外还有与世界时有关的部分。别科娃（N．P.Benkova）首先研究了全球Sa的经度效应,指出了Sq的经度变化约占总变化的20%。这里不详细介绍这一方法的技术细节,读者可参阅有关文献[23][24]。松下(S.Matsushita)在分析1958年（IGY）S。的变化时把全球按地磁经度分成三个区，第一区为欧（洲）非（洲)带,磁经度在45E和165E之间,第二为亚澳带，165E和285E之间,三为南北美带，285和45E之间[22]。分析结果显示出明显的经度差异。图5.28给出了反映这一差异主要特征的三个经度带外空电流体系焦点的位置和强度。

除上面所述Sa的正常变化规律外，在磁赤道两侧南北约±15°的狭长条带地区，Sa有显著的异常变化。当1922年在靠近磁赤道的秘鲁胡安·卡约(Huan Cuyo)地磁台首次

![](images/431a0e71357f29e448269729dde5ecba5b182dcec69ac296f53e5afaa7360b16.jpg)  
图5.281958年外空电流体系焦点的位置和强度在不同经度带上的分布[2]经度分带用虚线标出，图中细实线为磁倾纬度D.冬季；E.春秋；J夏