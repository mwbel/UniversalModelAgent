$$
= t _ { \mathrm { s } } \mathrm { l o } 8 \phi + m t _ { \mathrm { w } } \mathrm { l o } 8 \phi + t _ { \mathrm { h } } \left( \frac { } { } \phi - 1 \right)
$$

对于充分大的 $m \mathrm { ~ , ~ } t _ { \mathrm { h } }$ 可忽略不计,所以上式可简化为：

$$
t _ { \mathrm { o n e - t o - a l l } } ( \mathbf { C T } ) = ( t _ { \mathrm { s } } + m t _ { \mathrm { w } } ) \log p
$$

它比(8.3)式大大改进。

![](images/fdb5069e6cefa599d4882391cc4519a91fe99620178281c8a76ffcdeb19ed50c.jpg)  
图8.88个处理器环上以CT方式播送过程

网孔在如图8.9所示的二维网孔上用CT方式播送时可分为两步：先完成一行中 $\sqrt { \pmb { \phi } }$ 个处理器间的播送；再同时进行各列中 $\sqrt { \pmb { \phi } }$ 个处理器间的播送。参照(8.7)式,可知每步的通信时间为 $\begin{array} { r } { \big ( t _ { \mathrm { s } } + m t _ { \mathrm { w } } \big ) \log \sqrt { \hat { p } } + t _ { \mathrm { h } } \big ( \sqrt { \hat { p } } - 1 \big ) } \end{array}$ ,因此总的通信时间为：

$$
t _ { \mathrm { o n e - t o a l l } } ( \mathrm { C T } ) = ( t _ { \mathrm { s } } + m t _ { \mathrm { w } } ) \log { \phi } + 2 t _ { \mathrm { h } } ( \sqrt { \phi } - 1 )
$$

![](images/ef5b343d03eda0e3b430923d4606a47dae45e903443e9e11d741a1559c3dca85.jpg)  
图8.9 $4 \times 4$ 网孔上以CT方式播送过程

超立方已如前述,一个 $2 ^ { d }$ 个处理器可视为每维只有2个处理器的 $\pmb { d }$ 维网孔,所以在超立方上用CT方式播送其通信时间为：

$$
t _ { \mathrm { o n e - t o - a l l } } ( \mathrm { C T } ) = ( t _ { \mathrm { s } } + m t _ { \mathrm { w } } ) \log p
$$

# 8.4多到多播送

多到多播送(All-to-All Broadcast)也称为多节点播送(Multinode Broadcast），此时所有 $\pmb { \mathscr { P } }$ 个处理器同时启动播送，只是各处理器播送各自的信包。多到多播送的反操作叫作多点累积(Multinode Accumulation),两者在矩阵运算、归约操作和求前缀和中常使用。

# 8.4.1 使用SF进行多到多播送

环在p个处理器的环中进行多到多播送,实际上就是一系列以流水线方式工作的p个处理器将各自的信包依次同向传递。传递完毕后,每个处理器都接收到了来自其它 $\left( \pmb { \hat { p } } - \pmb { 1 } \right)$ 个处理器中的信包,其总的通信时间为：

$$
t _ { \mathrm { a i l - t o - a l l } } ( \mathrm { S F } ) = ( t _ { s } + m t _ { \mathrm { w } } ) ( \mathbf { \nabla } _ { P } - \mathbf { 1 } )
$$

![](images/00dbd22224168cd99a246252766a2935b33e71faea613ff5d675b1ced034e611.jpg)  
图8.108个处理器的环上用SF方式多到多播送过程

图8.10示出了8个处理器环上用SF方式施行多到多播送的过程。其中，虚线箭头上圆括弧外的数字是时间步，圆括弧内的数字是该时间步所发送的信包所属的处理器号；各节点旁的圆括弧中的数字是该节点所积累的信包所属的处理器号。

环绕网孔如一到多播送一样，二维网孔上多到多播送可以处理成行环和列环的播送。为此,先按行进行多到多播送；再按列进行多到多播送。在 $\sqrt { \pmb { \phi } } \times$ $\sqrt { \phi }$ 的环绕网孔上,各行多到多的播送时间为 $\left( { t _ { \mathrm { s } } + m t _ { \mathrm { w } } } \right) \left( { \sqrt { \ p } - 1 } \right)$ ;经过行播送后各处理器中的信包大小变为 $m ~ { \sqrt { \beta } }$ ，所以再按列施行多到多播送时其时间为$\big ( t _ { \mathrm { s } } + m \ \sqrt { / } t _ { \mathrm { w } } \big ) \big ( \sqrt { / } - 1 \big )$ 。因此总的通信时间为：

$$
t _ { \mathrm { a l l - t o - a l l } } \mathrm { ( S F ) } = 2 t _ { \mathrm { s } } \mathrm { ( } \sqrt { \mathcal { p } } - 1 \mathrm { ) } + m t _ { \mathrm { w } } \mathrm { ( } \mathbf { \nabla } \mathbf { \mathcal { p } } - 1 \mathrm { ) }
$$

图8.11示出了 $3 \times 3$ 环绕网孔(为了清楚起见,环绕线未画出)上用 SF方式施行多到多播送的过程。

![](images/dc1cf9092005149a903aaaa623545ec67bf7fa7a505a28c5d42086809037a333.jpg)  
图8.11 $3 \times 3$ 环绕网孔上用SF方式进行多到多播送(a)起始数据分布；(b)行播送后的数据分布

超立方在超立方上施行多到多播送,很自然地是按超立方的维成对处理器交换数据(双向通道),各处理器中的信包大小每次加倍,第i步交换时信包大小为2i-1m,因此成对处理器交换信包的时间为ts+2i-1mtw,于是总的通信时间为：

$$
t _ { \mathrm { a l l - t o - a l l } } ( \mathrm { S F } ) = \sum _ { i = 1 } ^ { \log p } ~ ( t _ { \mathrm { i } } + 2 ^ { i - 1 } m t _ { \mathrm { w } } )
$$

$$
= t _ { s } \mathrm { l o g } p + m t _ { \mathrm { w } } ( \pmb { \phi } - 1 )
$$

图8.12示出了8个处理器的超立方上用SF方式施行多到多的播送过程。

![](images/14f6a859c52057cee4a825dd635c35989417444af2cd8ff4ff4e8c55b942c576.jpg)  
图8.128个处理器的超立方上用SF方式进行多到多播送(a)起始状态;(b)第2步之前的状态；(c)第3步之前的状态；(d)最终状态

# 8.4.2使用CT进行多到多播送

如前所述，使用CT方式进行一到多播送时，为了在环和网孔上获得较好的结果,只要将超立方上的算法映射到它们之上即可。但对于多到多播送而言,这样作未必好，因为它会造成通道拥挤。例如,要是将图8.12(c)超立方上成对处理器间的交换操作直接映射到图8.13所示的环上时，就会发现有4条信包同时穿过环的一条通道,从而造成拥挤。

然而,在双向线性阵列(无环绕网孔)上,使用CT方式进行多到多播送的通信时间与在环(带环绕网孔)上使用 SF方式进行多到多播送的通信时间是一样的。

值得提出的是,对于任何并行结构,其多到多播送之通信时间的下界为$m t _ { \mathrm { w } } ( \pmb { \mathscr { p } } - 1 )$ ，这可从(8.10)、(8.11)和(8.12)式中看出。事实上，不管使用何种结构和选路方式,每个处理器至少要接收到 $m t _ { \mathrm { w } } ( \pmb { \phi } - 1 )$ 个数据字。

![](images/f5f087c9fc387f51c300af3b25ac8403de99d84713274936d79bd71442d7b38d.jpg)  
图8.13图8.12(c)通信步映射到环上时所造成的拥挤

# 8.5小结和导读

小结在正文中已经讨论了一到多播送和多到多播送以及它们的反操作单点累积和多点累积。在章末习题8.6'和8.7也将介绍一到多个人通信(One-to-All Personalized Communication)和多到多个人通信(Al-t-All Personalized Com-munication)。为了更清楚地理解它们的含意,图8.14分别图示了它们的概念。

表8.1列出了本章所讨论的不同互连结构采用CT开关技术时的几种基本通信操作的通信时间,其中循环 $\mathbf { q } .$ 移位(Circular q-Shift）（见习题8.8)通信时间表达式中的 $r ( q )$ 是 $\pmb q$ 能被 $2 ^ { j }$ 整除的最大整数j。

表8.1通信时间汇总一览表(使用CT方式）  

<table><tr><td rowspan=1 colspan=1>通信操作</td><td rowspan=1 colspan=1>p-环</td><td rowspan=1 colspan=1>p×p-二维环绕网孔</td><td rowspan=1 colspan=1>p-超立方</td></tr><tr><td rowspan=1 colspan=1>一到多播送</td><td rowspan=1 colspan=1>(ts+ mtw)logp+th(p-1)</td><td rowspan=1 colspan=1>(ts+ mtw)logp+2th(p-1)</td><td rowspan=1 colspan=1>(ts+ mtw)logp</td></tr><tr><td rowspan=1 colspan=1>多到多播送</td><td rowspan=1 colspan=1>(t,+mtw)(p-1)</td><td rowspan=1 colspan=1>2t(p-1)+ mtw(p-1)</td><td rowspan=1 colspan=1>tslogp + mtw( p -1)</td></tr><tr><td rowspan=1 colspan=1>一到多个人通信</td><td rowspan=1 colspan=1>(ts+mtw)(p-1)</td><td rowspan=1 colspan=1>2ts(p-1)+ mtw(p-1)</td><td rowspan=1 colspan=1>tslogp +mtw(p-1)</td></tr></table>

（续表）

<table><tr><td rowspan=1 colspan=1>通信操作</td><td rowspan=1 colspan=1>p-环</td><td rowspan=1 colspan=1>p×√p-二维环绕网孔</td><td rowspan=1 colspan=1>p-超立方</td></tr><tr><td rowspan=1 colspan=1>多到多个人通信</td><td rowspan=1 colspan=1>(t,+ mtwp/2)(p-1)</td><td rowspan=1 colspan=1>(2tg+ mtwp)(p-1)</td><td rowspan=1 colspan=1>(t+mtw)(p-1)+p1o8p</td></tr><tr><td rowspan=1 colspan=1>循环q-移位</td><td rowspan=1 colspan=1>(t,+ mtw)Lp/2]</td><td rowspan=1 colspan=1>(t+mtw）（2L2+1)</td><td rowspan=1 colspan=1>t,+ mtw+th(logp -r(q))</td></tr></table>

# 一到多播送

![](images/de9a461ce45a34aa4eb85c882881c7f8c3c1c4caa916d64daa670e9af85b06aa.jpg)  
图8.14一到多和多到多个人通信(a)一到多播送和单点累积;(b)多到多播送和多点累积；(c)一到多个人通信和单点收集;(d)多到多个人通信

上表中的表达式对使用SF开关技术时绝大部分都相同,不同的是： $\textcircled{1}$ 对于一到多播送，在环上的通信时间为 $( t _ { \mathrm { s } } + m t _ { \mathrm { w } } ) \lceil \mathtt { \Delta } _ { P } / 2 \rceil$ ，在二维网孔上的通信时间为 $2 ( t _ { \mathrm { s } } + m t _ { \mathrm { w } } ) \lceil \sqrt { \hat { p } } / 2 \rceil$ ； $\textcircled{2}$ 对于多到多个人通信,在超立方上的通信时间为 $( { t _ { \mathrm { s } } } ^ { + }$ $m t _ { \mathbf { w } } \pmb { \mathscr { p } } \wedge 2 ) \log \pmb { \mathscr { p } } \circ$

本章所讨论的通信操作方法均可在SIMD机器上执行。然而由于在MIMD机器上施行同步比较复杂,所以本章所给出的通信时间表达式运用在MIMD机器上时可能相差很大。

导读关于多处理机的互连网络,读者可进一步参考互连网络综述[64]和互连网络专著[199]。有关通信选路策略和消息传递机制,读者可阅读[100]书中的第7.4节。[114]书中的第三章还详尽地讨论了诸如一到多个人通信、多到多个人通信和循环移位等其它一些基本通信操作。读者还可以从上述基本参考文献中追踪阅读一些更丰富和更新近的文献。

# 习 题

8.1对于一个 $\pmb { 8 } = 2 ^ { d }$ 个处理器(其编号从0到 $2 ^ { d } - 1 )$ 的环,如何将其嵌人 $\pmb { d }$ 维超立方中？[提示：可以使用8位Gray码对环上的处理器进行编号。一个8位Gray码为000,001，011,010,110,111,101,100.]

8.2对于一个 $2 \times 4$ 的网孔(处理器按行主方式依次编号为0,1,2,3,4,5,6,7),如何将其嵌人3维超立方中？[提示：将 $2 \times 4$ 的网孔使用Gray码按行主对其编号。]

8.3如图8.15所示,信包中的片0,1,2,3要分别去向目的地 $\mathbf { A } , \mathbf { B } , \mathbf { C } , \mathrm { D } _ { \circ }$ 此时片0占据信道CB,片1占据信道DC,片2占据信道AD,片3占信道 ${ \tt B A } _ { \tt o }$ 试问：

$\textcircled{1}$ 这将会产生什么现象？$\textcircled{2}$ 如果采用X-Y选路策略，可避免上述现象吗？为什么？

8.4假定在二叉树中,叶节点为处理器节点,内节点为开关节点(参照图8.16)。试证明在 $\pmb { \hat { p } }$ 个叶节点的二叉树中，进行 $\pmb { m }$ 个字的一到多播送的通信时间为：

$$
( t _ { \mathrm { s } } + m t _ { \mathrm { w } } + t _ { \mathrm { h } } ( \log { p } + 1 ) ) \log { p }
$$

[提示：信包穿越 $\mathbf { \nabla } _ { l } - \mathbf { 1 }$ 个开关节点所需的时间为 ${ \pmb t _ { s } } + m { \pmb t _ { \mathrm { w } } } + { \pmb t _ { \mathrm { h } } } { \pmb l } _ { \circ } ]$

8.5给定 $\pmb { \hat { p } }$ 个数 $n _ { 0 } , n _ { 1 } , \cdots , n _ { \hat { \rho } ^ { - 1 } }$ ，所谓前缀和(Prefix Sum)就是计算 $S _ { k } = \sum _ { i = 0 } ^ { k } n _ { i }$ ,其中 $0 \leqslant$ $\pmb { k } \leqslant _ { } p - 1$ 。算法8.3给出了超立方上求前缀和的方法。试按此算法，计算8个处理器的超立方上前缀和。

![](images/e772a88246f32c8b4692913c467ca410cfc62d73ea6a65377f32bb0f5bfb48a5.jpg)  
图8.15虫蚀选路网络中所出现的现象

![](images/9dc0dbcbcaf284c816db377da243278281438ea86b15474efefff6187e0ebe38.jpg)  
图8.168个处理器的树上一到多播送过程

# 算法8.3 $\pmb { d }$ 维超立方上前缀和算法

输入： $\pmb { \mathscr { P } }$ 个数开始存在 $\pmb { \hat { p } }$ 个处理器中输出：第 $k$ 个处理器存有前缀和 $S _ { k } = \sum _ { i = 0 } ^ { k } n _ { i } , 0 { \leqslant } k { \leqslant } p - 1$ Begin

(1）result $=$ my - number (2) $\mathbf { m s g } =$ result

for $i = 0$ to $d - 1$ do (3.1） ${ \mathrm { P a r t n e r } } = \mathbf { m } \mathbf { y } _ { - } \mathbf { i d } \mathbf { \widehat { \mathrm { { + } } } } { 2 ^ { i } }$ (3.2） Send msg to Partner

(3.3）Receive number from Partner   
(3.4） ${ \mathrm { m s g } } { = } { \mathrm { m s g } } + { \mathrm { n u m b e r } }$   
(3.5）if(Partner<my- id)then resul $=$ result $^ +$ number endif

end for

End

8.6一到多个人通信又称之为单点散射(Single-Node Scatter),它与一到多播送不同之处是，此时源处理器有 $\pmb { \hat { p } }$ 个信包,每一个去向一个目的地(见图 $8 . 1 4 ( \mathfrak { c } ) )$ 。图8.17示出了8个处理器的超立方上单点散射的过程。试证明：使用 SF和CT方式在超立方上施行一到多个人通信的通信时间为：

$$
t _ { \mathrm { o n e - t o - a l l - p e r s } } = t _ { s } \mathrm { l o g } \phi + m t _ { \mathrm { w } } ( \phi - 1 )
$$

![](images/bee5785de3781847a5a7a28f82184f1e811e3155668549d3483cb65fe28df112.jpg)  
图8.178个处理器的超立方上单点散射过程(a)起始分布;(b)第2步之前的分布; $\left( \mathbf { c } \right)$ 第3步之前的分布；(d)最终分布

8.7多到多个人通信又称之为全交换(Total Exchange),每个处理器发送各自彼此不同的大小为m的信包给其余处理器(见图8.14(d))。图8.18示出了6个处理器的环上全交换的过程,其中，{x,y|表示{源处理器,目的处理器,（{x1,y1}，x2,y2},，xn,yn}）表示传输过程中的信包流,每个处理器只接收属于它的信包，下传其余的信包。试证明：利用 SF方式,在环上施行全交换的通信时间为：

$$
t _ { \mathrm { { u a l - e x c h a n g e } } } = { \big ( } t _ { \mathrm { s } } + { \frac { 1 } { 2 } } m t _ { \mathrm { w } } { p } { \big ) } { \big ( } { p - 1 } { \big ) }
$$

[提示：第 $\pmb { i }$ 步传送的信包大小为 $m ( \pmb { p } - i ) _ { \circ } ]$

![](images/6b29e5c9d201afea7af27ff1d12ddce0b5f77b90942bcec89de4e31f2e24d4e0.jpg)  
图8.186个处理器的环上全交换过程

8.8在 $\pmb { \mathscr { p } }$ 个处理器,所谓循环 $\mathbf { q } \mathrm { . }$ 移位系指处理器 $_ i$ 发送包给处理器 $( i + q ) { \bmod { p } }$ 。图8.19示出了按行主编号的 $\sqrt { \pmb { \mathscr { p } } \times \pmb { \mathscr { p } } } = 4 \times 4$ 环绕网孔上施行 5-移位的过程：首先按行同时循环移位(qmod√p=1)次;然后作Lq/√p」=1次列补偿移位(如图8.19(b)所示);最后再作一次列移位。试证明：利用SF方式在正方形环绕二维网孔上施行循环q-移位的通信时间为：

$$
t _ { \mathrm { c i r c u l a r - s h i f t } } = ( t _ { s } + m t _ { \mathrm { w } } ) ( 2 \lfloor { \sqrt { \dot { p } } } / 2 \rfloor + 1 )
$$

![](images/598f6a49c061c4c94d6696f02d2ffe31b34945cf09e205593fb7f7b007b6917e.jpg)  
图8.19 $4 \times 4$ 环绕网孔上5-移位过程

(a)起始分布和第1通信步;(b)补偿列移位;(c)第3通信步中列移位；(d)最终分布

# 第九章 稠密矩阵运算

矩阵运算是数值计算中最重要的一类运算，特别是在线性代数和数值分析中,它是一种最基本的运算。本章讨论稠密矩阵的运算,包括矩阵转置、矩阵和向量相乘以及矩阵相乘等。在讨论并行矩阵算法时，将结合具体例子以图示的方法着重算法原理的叙述;在分析算法时，除了分析计算时间外,还要利用上一章所学的知识来分析通信时间;在实现算法时，强调矩阵到处理器的映射；同时为了教学的方便，限于讨论方阵，但所介绍的算法也同样适用于矩形阵。

# 9.1矩阵的划分

在科学和工程计算中，矩阵的阶都很高(元素很多),为了并行实现,很自然地要将其进行划分，然后指派给不同的处理器。下面将扼要讨论矩阵的两种常见的划分方法，即行列划分(又称为带状划分)和棋盘划分(又称为块状划分)。

# 9.1.1 带状划分

所谓带状划分（Striped Partitioning)就是将矩阵整行或整列地分成若干个组,每组指派给一个处理器。也可将若干行或若干列指派给一个处理器,而且这些行和列可以是连续的，也可以是等距相间的，前者称为块带状的（ $\mathbf { B l o c k } \mathbf { - }$ Striped),后者称为循环带状的(Cyclic-Striped)。

块带状划分如图9.1(a)所示,它是一种列块带状划分。在此情况下,对于一个 $\mathbf { \Omega } _ { n } \times \mathbf { \Omega } _ { n }$ 的矩阵和 $\pmb { \mathscr { p } }$ 个处理器（编号为 $\mathbf { P _ { 0 } } , \mathbf { P _ { 1 } } , \cdots , \mathbf { P _ { \pmb { \hat { \rho } } - 1 } } )$ 而言,每个处理器将均匀连续地分配有 $\pmb { n } / \pmb { \mathscr { p } }$ 列,其中 $\mathbf { P } _ { i }$ 包含有列 $\left( n / p \right) i , \left( n / p \right) i + 1 , \cdots , \left( n / \right)$ $\pmb { \mathscr { p } } ) ( i + 1 ) - 1 , 0 { \leqslant } i { \leqslant } \pmb { \mathscr { p } } - \pmb { 1 } _ { \pmb { \mathscr { c } } }$

循环带状划分如图9.1(b)所示,它是一种行循环带状划分。在此情况下，对于一个 $\mathbf { \Omega } _ { n } \times \mathbf { \Omega } _ { n }$ 的矩阵和 $\pmb { \hat { p } }$ 个处理器(编号为 $\mathbf { P } _ { 0 } , \mathbf { P } _ { 1 } , \cdots , \mathbf { P } _ { { \pmb { \phi } } - 1 } )$ 而言,每个处理器将均匀相间地分配有n/p行,其中P;包含有行i,i+p,i+2p,,i+（n-1)p,$0 { \leqslant } i { \leqslant } p - 1 ,$

![](images/88f778434d422b9b2b570fb7ba6dfc44355ca2f342b1a7934ccc97b8dbeac81c.jpg)  
图9.14个处理器上 $1 6 \times 1 6$ 矩阵带状划分(a)列块带状划分； (b)行循环带状划分

# 9.1.2棋盘划分

所谓棋盘划分(Checker Board Partitioning)就是将方阵划分成若干个子方阵，每个子方阵指派给一个处理器，此时任一处理器均不包含整行或整列。和带状划分类似,棋盘划分也可分为如图9.2(a)所示的块棋盘划分(Block-CheckerBoard

![](images/fd2848291ab301fbb8514e29fad56c00696a950bd04dc7422de6d0e4bf2d1a33.jpg)  
图9.216个处理器上 $\mathbf { 8 \times 8 }$ 矩阵棋盘划分(a)块棋盘划分； (b)循环棋盘划分

Partitioning)和如图9.2(b)所示的循环棋盘划分(Cyclic-Checker Board Partition-ing）。

矩阵划分成棋盘状可和处理器连成二维网孔相对应。对于一个 $n \times n$ 的方阵和 ${ \overline { { \pmb { p } } } } \times { \sqrt { \pmb { p } } }$ 的二维处理器阵列,每个处理器均匀地分配有 $( n / \sqrt { \hat { p } } ) \times ( n / \sqrt { \hat { p } } ) =$ $n ^ { 2 } / \phi$ 个矩阵元素。

值得指出的是,和带状划分相比,棋盘划分可开发更高的并行度。例如,对于一个 $\mathbf { \Omega } _ { n } \times \mathbf { \Omega } _ { n }$ 的方阵,棋盘划分最多可使用 $n ^ { 2 } .$ 个处理器进行并行计算,但使用带状划分可用的处理器不能多于 $\pmb { n }$ 个。

# 9.2矩阵转置

对于一个 ${ \pmb n } \times { \pmb n }$ 的方阵 $\pmb { A }$ ,将其元素 $a _ { i j }$ (沿主对角线)与 $a _ { j i }$ 互换,就构成了转置矩阵(Transposing Matrix) $\pmb { A } ^ { \textrm { T } }$ 。如果假定成对元素交换取单位时间，则显然串行矩阵转置算法9.1的运行时间为 $\left( n ^ { 2 } - n \right) / 2 = O ( n ^ { 2 } )$ 。

# 算法9.1单处理机上矩阵转置算法

输入： $\mathbf { A } _ { n } \times \mathbf { \mu } _ { n }$   
输出： $\smash { A _ { n \times n } ^ { \textrm { T } } }$   
Begin for $i = 2$ to $_ n$ do for $j = 1$ to $i - 1$ do $a _ { i j }  a _ { j i }$ endfor endfor   
End

# 9.2.1 棋盘划分的矩阵转置

以下仅讨论网孔和超立方上块棋盘划分的矩阵转置算法，它们对循环棋盘划分也同样适用。

网孔上的矩阵转置如图9.3所示,要是处理器数目p=n²,则网孔上的矩阵转置算法是非常简单的：对角线下的元素,先向上移至对角线,再向右移至目的地；对角线上的元素，先向下移至对角线，再向左移至目的地。

对于p<n²的情况,整个n×n的矩阵先分成p个大小为(n/√p)×（n/√p)的子块,然后算法分两步进行：第一步,将子块视为单个元素进行如图9.4(a)所示的子块转置;第二步,在各处理器内施行如图9.4(b)所示的局部转置。

（0，1） 0,2） 0,3） （0，0） （1.0） （2,0） （3,0）P0 P1 P ？ → P0 P1 P2 P  
（1.3 0，1） （1,1） （2,1） 3,1）P P6 P P4 P P6 P7, 1.....  
（2,0） (2. （2,3） 0,2) $\left( 1 , 2 \right)$ （2,2） （3,2）P8 P10 P P& P9 P10 ${ \bf P } _ { 1 1 }$ i  
（3,0） （3，1 （3,2) 0.3） （1.3） （2,3） （3,3）P12 4 .Pj3 P14 ↑ P12 P13 P14 P1s（a） （b）

![](images/39b2cd59f3d897e2c303061035b6d8e0a972ed00573dae057c64299f4ae0bb50.jpg)  
图9.316个处理器上棋盘划分的 $4 \times 4$ 矩阵的转置(a)通信过程； (b)最终结果  
图9.416个处理器上棋盘划分的 ${ \pmb 8 } \times { \pmb 8 }$ 矩阵的转置(a)子块转置； (b)子块内局部转置

整个算法的运行时间可分析如下：第一步的子块转置最长的路径约为$2 \sqrt { \pmb { \mathscr { p } } }$ ，移动单个子块的时间为 $t _ { \mathrm { s } } + t _ { \mathrm { w } } n ^ { 2 } / \phi$ ，所以各子块达到其目的地的时间为 $2 ( t _ { s } + t _ { \mathrm { w } } n ^ { 2 } / p ) \sqrt { \ p }$ ;第二步,假定成对元素局部交换取单位时间,则大小为$( n / \sqrt { \hbar } ) \times ( n / \sqrt { \hbar } )$ 子块约花了 $\scriptstyle { n ^ { 2 } } / ( 2 p )$ 的时间进行局部转置，所以算法总运行时间为：

$$
T _ { \mathrm { p } } = { \frac { n ^ { 2 } } { 2 \phi } } + 2 t _ { \mathrm { s } } \ { \sqrt { \hat { p } } } + 2 t _ { \mathrm { w } } \ { \frac { n ^ { 2 } } { \sqrt { \hat { p } } } }
$$

递归转置算法（Recursive Transposition Algorithm）如图9.5所示，一个$\mathbf { \Omega } _ { n } \times \mathbf { \Omega } _ { n }$ 的方阵先分成4个子方阵,对其施行转置，即右上与左下两个子方阵对调;然后每个子方阵再分成4个更小的子方阵施行转置;依此类推直到整个矩阵转置完毕。

![](images/1871df9ada8f6d37f6e57c7d2290e9e26662bc2878e883f7a59891769385550a.jpg)  
图9.5 ${ \pmb 8 } \times { \pmb 8 }$ 矩阵的递归转置法

(a)矩阵分成4块进行转置； (b)每块再分成4个子块进行转置；(c)每个子块中4个元素进行转置； (d)最终结果

超立方上的矩阵转置上面所介绍的递归转置算法可以很自然地映射到超立方上。如图9.6（a）所示，先将 $_ n \times n$ 的方阵分成4个 $\frac { n } { 2 } \times \frac { n } { 2 }$ 的子方阵，相应地将p个处理器的超立方考虑成4个p/4个处理器的子超立方;然后将右上子块与左下子块对调(如图9.6(a)所示， $\mathrm { P } _ { 8 }$ 中的子块与 ${ \bf P } _ { 2 }$ 中子块对调， $\mathrm { P } _ { 9 }$ 中子块与${ \bf P } _ { 3 }$ 中子块对调等等)。接着如图9.6(b)所示,再将各个 $\frac { n } { 2 } \times \frac { n } { 2 }$ 的子块分成4个更小的子块,并对它们施行转置。在最后递归步中，子超立方中只有一个处理器,显然总共进行了 $\log _ { 4 } { p } = ( \log { p } ) / 2$ 递归步,这时各子块的大小为 $( n / \sqrt { \ p } ) \times$ $( n / \sqrt { \ p } )$ ,它们要在每个处理器中施行局部转置,花费了约 $n ^ { 2 } / ( 2 \phi )$ 的时间。因为每个待通信的子块大小为 $\dot { n } ^ { 2 } / \phi$ ,所以使用存储转发选路时需 $2 ( t _ { \mathrm { s } } + t _ { \mathrm { w } } n ^ { 2 } / \phi )$ 时间,因此递归 $( \log p ) / 2$ 步的总通信时间为 $( t _ { s } + t _ { \mathrm { w } } \ n ^ { 2 } / p ) \mathrm { l o g } p$ ,这样算法总的运行时间为：

$$
T _ { \mathrm { p } } { = } \frac { n ^ { 2 } } { 2 \hat { p } } + ( t _ { \mathrm { s } } + t _ { \mathrm { w } } \frac { n ^ { 2 } } { \hat { p } } ) \log \hat { p }
$$

![](images/ec066e051791df00dd39e65ed51ab318362fc65dbf8aa33cdae3e65ae35202a6.jpg)  
图9.616个处理器的超立方上的矩阵递归转置(a)矩阵分成4块进行转置； (b)每块中4个子块进行转置

# 9.2.2带状划分的矩阵转置

如图9.7所示,假定对于一个 $n \times n$ 的矩阵,使用 $\pmb { n }$ 个处理器按行划分。

开始时,处理器 $\mathrm { P } _ { i }$ 中存有矩阵元素 $[ i , 0 ] , [ i , 1 ] , \cdots , [ i , n - 1 ]$ ,则在转置后，元素 $[ i , 0 ]$ 将属于 ${ \tt P } _ { 0 }$ ，元素 $[ i , 1 ]$ 将属于 $\mathbf { P _ { 1 } }$ ,如此等等。注意在转置过程中，每个处理器将发送不同的值给其它处理器,这实际上就是第八章中所讲的多到多个人通信。

一般而论， $\textstyle { p { \leqslant } n }$ 时每个处理器分配有 $n / \phi$ 行(共 $n ^ { 2 } / \phi$ 个元素),此时转置中所涉及到的多到多个人通信的子块大小为 $( n / p ) \times ( n / p )$ 。通信完毕后，每个处理器尚须对这些子块施行局部转置。假定成对元素交换取单位时间,则每个子块转置时间为 $n ^ { 2 } / ( 2 p ^ { 2 } )$ 。因为每个处理器有 $\pmb { \mathscr { P } }$ 个这样的子块,所以转置它们花费了 $n ^ { 2 } / ( 2 p )$ 时间。当在超立方上使用切通选路法对大小为 $n ^ { 2 } / \phi ^ { 2 }$ 的信包进行多到多个人通信时，其时间约为 $t _ { \mathrm { s } } ( \boldsymbol { \ p } - 1 ) + t _ { \mathrm { w } } \ n ^ { 2 } / \hbar + \left( 1 / 2 \right) t _ { \mathrm { h } } \ \boldsymbol { p } \log \boldsymbol { \phi }$ （参见第八章的表8.1)。所以这时算法总的运行时间为：

$$
T _ { \mathrm { p } } = { \frac { n ^ { 2 } } { 2 \phi } } + t _ { \mathrm { s } } ( \not p - 1 ) + t _ { \mathrm { w } } { \frac { n ^ { 2 } } { \phi } } + { \frac { 1 } { 2 } } t _ { \mathrm { h } } \not p \log \phi
$$

![](images/147f35c50f4f32badec6b43b862d4e2d3d8b621221f7cf1d5effe3b2e9737ea6.jpg)  
图9.74个处理器上 $4 \times 4$ 矩阵的转置

# 9.3 矩阵-向量乘法

对于一个n×n的方阵A乘以n×1的向量X就可得n×1的向量Y。如果假定一个乘-加运算取单位时间，则显然串行矩阵-向量乘法(Matrix-VectorMultiplication）算法9.2的运行时间为 $O ( n ^ { 2 } )$

# 算法9.2单处理机上矩阵-向量乘算法

输入： $A _ { n } \times _ { n } , X _ { n \times 1 }$   
输出: $\pmb { Y } _ { n \times 1 }$   
Begin for $i = 0$ to $n \sim 1$ do $y _ { i } = 0$ for $j = 0$ to $\pmb { n } - \pmb { 1 }$ do $y _ { i } = y _ { i } + a _ { i j } x _ { j }$ endfor endfor   
End

# 9.3.1带状划分的矩阵-向量乘法

以下仅讨论行带状划分矩阵-向量乘法,列带状矩阵-向量乘法是类似的。

$p = n$ 的情况,如图9.8(a)所示，开始时处理器 $\mathrm { \bf P } _ { i }$ 存放 $. \boldsymbol { r } _ { j }$ 和 $a _ { i , \ i } , a _ { i , \ i } , \cdots ,$ $a _ { i , n }$ 并负责计算 $y _ { i }$ 。由于矩阵-向量相乘要求每一行与整个向量相乘，所以如图9.8(b)所示每个处理器要将其向量元素向其余的处理器进行多到多播送。播送完毕后就可以如图9.8(c)那样进行 $y _ { i } = \sum _ { j = 0 } ^ { n - 1 } u _ { i j } x _ { j }$ aij的计算了。按此，通信和计算时间均为 $O ( n )$ ,它是成本最佳的。

![](images/123fd9a3da2e72a9b5bf878d092bf5dc47f076f4f3437e9bcad7a896f23f43d9.jpg)  
图9.8 $\beta = \pi$ 时按行划分的矩阵-向量乘法：

(a)起始分布；（b）向量多到多播送；$\left( \mathfrak { c } \right)$ 施行相乘；（d)结果向量 $\pmb { \gamma }$

$/ / < / \iota$ 的情况是类似的，只是开始时每个处理器存放有矩阵的 $n / /$ 行(共$n ^ { 2 } / 1 )$ 个元素)和向量的 $n / \mu$ 个元素。

超立方上矩阵乘向量参照第八章的表8.1可知、"/p个向量元索多到多播送时间为 $t _ { \mathrm { s } } \mathrm { l o g } \phi + \left( n / p \right) t _ { \mathrm { w } } \left( \mathbf { \Gamma } _ { \mathbf { \hat { P } } } - 1 \right)$ ,当 $\pmb { \phi }$ 充分大时它近似为 $t _ { \mathrm { s } } \mathrm { l o g } \ p + n t _ { \mathrm { w } } ,$ 。考虑到每个处理器要花 $n ^ { 2 } / \phi$ 的时间进行乘-加运算，所以超立方上并行矩阵-向量乘之总时间为：

$$
T _ { \mathrm { p } } = \frac { n ^ { 2 } } { \phi } + t _ { \mathrm { s } } \mathrm { l o g } \phi + n t _ { \mathrm { w } }
$$

当 ${ \boldsymbol { \mathbf { \mathit { p } } } } = { \boldsymbol { \mathbf { \mathit { n } } } }$ 时， $T _ { \mathfrak { p } } = O ( n )$ ,它是成本最佳的。

网孔上矩阵乘向量参照第八章的表8.1可知多到多播送 $n / \phi$ 个元素的时间为 $2 \big ( \sqrt { \ p } - 1 \big ) t _ { \mathrm { s } } + \frac { n } { \ p } t _ { \mathrm { w } } \big ( \ p - 1 \big )$ ,它可近似为 $2 t _ { \mathrm { s } } ( \sqrt { \hat { p } } - 1 ) + n t _ { \mathrm { w } }$ 。所以二维环绕 $\sqrt { \pmb { \mathscr { p } } } \times \sqrt { \pmb { \mathscr { p } } }$ 网孔上并行矩阵-向量乘之总时间为：

$$
T _ { \mathrm { p } } = \frac { n ^ { 2 } } { \phi } + 2 t _ { \mathrm { s } } ( \sqrt { \hat { p } } - 1 ) + n t _ { \mathrm { w } }
$$

# 9.3.2棋盘划分的矩阵-向量乘法

以下仅讨论块棋盘划分矩阵-向量乘法，循环棋盘划分时的矩阵-向量乘法是类似的。

$\pmb { p } = \pmb { n } ^ { 2 }$ 的情况此时每个处理器存放有矩阵的一个元素，而向量 $\pmb { x } _ { i }$ 通常是存放在 $P _ { i i }$ 中的。如果 $\pmb { x _ { i } }$ 是存放在处理器阵列的最后一列中，则进行矩阵-向量乘时，如图9.9(a)所示，先要将向量元素与矩阵主对角线对准;然后如图9.9(b)所示，在列方向上施行向量元素一到多播送；播送完毕后，接着如图9.9(c)和(d)所示,则施行乘-加和单点累积,最后按行收集结果向量 $\yen 0$

在网孔上，图9.9(a)所示的一到一通信、图9.9(b)所示的一到多播送和图9.9(c)所示的单点累积，时间均为 $O ( n )$ ;在超立方上则为 $O ( \log n )$ 。因为每个处理器执行乘-加操作的时间为常数，所以在 $\textbf { \em n } \times \textbf { \em n }$ 的网孔上和 $\pmb { n } ^ { 2 }$ 个处理器的超立方上的并行矩阵-向量乘之总时间分别为 $O ( n )$ 和 $O ( \log n )$ ,它们不是成本最佳的。

$\pmb { p } < \pmb { n } ^ { 2 }$ 的情况假定 $\pmb { \mathscr { p } }$ 个处理器排成 $\sqrt { \pmb { \mathscr { p } } } \times \sqrt { \pmb { \mathscr { p } } }$ 的二维网孔,每个处理器存放有 $( n / \sqrt { \hat { p } } ) \times ( n / \sqrt { \hat { p } } )$ 的子块, $\pmb { \mathscr { n } } / \sqrt { \pmb { \mathscr { p } } }$ 个向量元素存放在处理器阵列的最后一列中,则进行矩阵-向量乘时，首先最右列的每个处理器要发送 $n / { \sqrt { \phi } }$ 个向量元素至主对角线上的处理器;然后按列进行一到多播送 $n / \sqrt { \mathbf { \Lambda } } \mathbf { \Lambda }$ 个元素；接着每个处理器施行n²/p次乘法并积累了n/√p个部分和，它们均须按行累加以得到结果向量。

当在无环绕的网孔上用CT选路法执行矩阵-向量乘时：向量与主对角线对准的时间为 $t _ { \mathrm { s } } + \frac { n } { \sqrt { \hat { p } } } t _ { \mathrm { w } } + t _ { \mathrm { h } } \sqrt { \hat { p } }$ ;按列施行一到多播送时间为 $\big ( \mathrm { \Delta } t _ { s } + \frac { n } { \sqrt { \phi } } \mathrm { \Delta } t _ { \mathrm { w } } \big ) \log { \sqrt { \phi } }$

$+ \ t _ { \mathrm { h } } ( \sqrt { \beta } - 1 )$ ；按行单点累积的时间为 $( \mathbf { \widetilde { \Gamma } } _ { \mathrm { s } } + \frac { n } { \sqrt { \hat { \mathcal { P } } } } \mathbf { \widetilde { \Gamma } } _ { \mathrm { w } } ) \log \sqrt { \hat { \mathcal { P } } } + t _ { \mathrm { h } } ( \sqrt { \hat { \mathcal { P } } } - 1 )$ ;假定乘-加取单位时间,则计算时间为 $n ^ { 2 } / \phi$ 。所以在网孔上并行算法总运行时间约为：

$$
T _ { \mathrm { p } } { \approx } \frac { n ^ { 2 } } { \phi } + t _ { \mathrm { s } } \mathrm { l o g } \phi + t _ { \mathrm { w } } \frac { n } { \sqrt { \phi } } \log \phi + 3 t _ { \mathrm { h } } \sqrt { \phi }
$$

![](images/564092c81b1868edde3506a1ccedbb1b1d57552eee351ef3e07a5bd61de602c1.jpg)  
图9.9 $\scriptstyle { p = n ^ { 2 } }$ 时棋盘划分的矩阵-向量乘法(a)起始分布和一到一通信； (b)一到多播送；(c)施行乘-加与单点累积；(d)结果向量 $\pmb { y }$

类似地,当在二维网孔上用SF选路法执行矩阵-向量乘时,并行算法的总运行时间约为：

$$
T _ { \mathrm { p } } { \approx } \frac { n ^ { 2 } } { \dot { p } } + 2 t _ { \mathrm { s } } { \sqrt { \dot { p } } } + 3 n t _ { \mathrm { w } }
$$

带状与棋盘划分时矩阵-向量乘的比较比较(9.5)式与(9.6)式可知,在网孔上用同样多的处理器，棋盘划分的矩阵-向量乘法比带状划分时要快；如果 ${ \pmb { \mathscr { p } } } > { \pmb { \mathscr { n } } }$ ,则无法使用带状划分，而棋盘划分不受此限制；即使 $\pmb { \mathscr { p } } \leqslant \pmb { \mathscr { n } }$ ,棋盘划分也更优;上述结论也适合于超立方(见习题9.3)。同时由章末习题9.5和9.4可知，棋盘划分的矩阵-向量乘的可扩放性也比带状划分时的好。

# 9.4矩阵乘法

一个 $\mathbf { \Omega } _ { n } \times \mathbf { \Omega } _ { n }$ 的方阵 $\pmb { A }$ 乘以 $\mathbf { \Omega } _ { n } \times \mathbf { \Omega } _ { n }$ 的方阵 $\pmb { B }$ 就得一个 $\mathbf { \Omega } _ { n } \times \mathbf { \Omega } _ { n }$ 的方阵 $\pmb { c }$

$$
c _ { i j } = \sum _ { k = 0 } ^ { n - 1 } a _ { i k } b _ { k j } , 0 { \leqslant } i , j { \leqslant } n - 1 _ { _ { - } }
$$

矩阵相乘的关键是相乘的两个元素的下标要满足一定的要求(即对准)。为此常采用旋转矩阵元素的办法(如下面将要介绍的Cannon乘法)使元素下标对准,或采用适当复制矩阵元素的办法(如下面将要介绍的DNS算法)使元素下标对准,或采用流水线的办法(如习题9.10所示的心动阵列上的算法)使元素的下标对准。

如果假定一个乘-加运算取单位时间，则显然串行矩阵乘法算法9.3的运行时间为 $O ( n ^ { 3 } )$

# 算法9.3单处理机上矩阵相乘算法

输入： $A _ { n } \times \ l _ { n } \lor \ l _ { n } \times \ l _ { n }$   
输出： $C _ { n \times n }$   
Begin for ${ \bf { \sigma } } _ { i } = \mathbf { 0 }$ to $\pmb { n } - 1$ do for ${ \bf { \nabla } } j = { \bf { 0 } }$ to $\pmb { n } - 1$ do $c _ { i j } = 0$ for $k = 0$ to $\pmb { n } - 1$ do $c _ { i j } = c _ { i j } + a _ { i k } \cdot b _ { k j }$ endfor endfor endfor   
End

目前所知的串行矩阵乘法的时间复杂度均为O(n"）,其中2<x≤3。例如Strassen乘法的时间阶为 $O \big ( n ^ { 2 . 8 0 7 4 } \big )$ 。

# 9.4.1 简单并行分块乘法

分块矩阵乘法(Block Matrix Multiplication）矩阵运算中分块的概念是非常有用的，可以将对矩阵元素的代数运算推广到对矩阵的块(子矩阵)进行同样的代数运算。例如,一个 $\mathbf { \Omega } _ { n } \times \mathbf { \Omega } _ { n }$ 的矩阵 $\pmb { A }$ 可以视为一个 $q \times q$ 的方块阵 $A _ { i , j } ( 0 \leqslant$ $i , j { \leqslant } q - 1 )$ ,每个方块阵大小为 $( n / q ) \times ( n / q )$ 。这样算法9.3就可改写成算法9.4,相应地,将矩阵元素的乘-加运算代换为子矩阵的乘-加运算。算法9.4共执行了 $q ^ { 3 }$ 次矩阵乘法，每个矩阵乘法需 $( n / q ) ^ { 3 }$ 次乘-加运算，所以总的乘-加次数仍为 $\pmb { n } ^ { 3 }$ 。

使用 $\pmb { \mathscr { p } }$ 个处理器执行分块乘时，可取 $q = \sqrt { \mathfrak { p } }$ ,这样每个处理器计算一个$\mathbf { C } _ { i , j }$ 块。

算法9.4单处理机上分块矩阵相乘算法输入： $A _ { n } \times \smash { _ { n } , B _ { n \times n } }$ ,子块大小为 $( n / q ) \times ( n / q )$ 输出： $\pmb { C _ { n } } \times \pmb { n }$

Begin for ${ \pmb i } = { \bf 0 }$ to $q - 1$ do for ${ j = 0 }$ to $q - 1$ do $\mathbf { C } _ { i , j } = 0$ for $k = 0$ to $q - 1$ do $\mathbf { } C _ { i , j } = \mathbf { } C _ { i , j } + A _ { i , k } \cdot B _ { k , j } $ endfor endfor endfor   
End

并行分块乘法简单的并行分块乘法的过程是： $\textcircled{1}$ 分块：将 $\mathbf { A } _ { n } \times \mathbf { \partial } _ { n }$ 与 $\pmb { { \cal B } } _ { n } \times \mathbf { \nabla } _ { n }$ 分成 $\pmb { \mathscr { p } }$ 块 $\mathbf { A } _ { i , j }$ 和 $B _ { i , j } ( 0 { \leqslant } i , j { \leqslant } \sqrt { \ p } - 1 )$ ,每块大小为 $( n / \sqrt { \hbar } ) \times ( n / \sqrt { \hbar } )$ ,并将它们分配给√p×p个处理器(Po,o,Po,1,,Pp-1,√P-1),开始时P,,存放有块Ai,j与块Bi,,，,然后计算块Ci,;②通信：为了计算块Ci,j,则需要所有块Ai,与Bk,j(0≤k≤√p-1),为此在每行的处理器之间要进行A矩阵块的多到多播送，以得到Ai,k,而在每列的处理器之间要进行B矩阵块的多到多播送,以得到Bk,j;③乘-加计算:一旦Pi,;收到了Ai,o,Ai,1,…,Ai,p-1与Bo,;,B1,j,,B[-1,j之后,就同时进行乘-加运算。

当并行分块乘法执行在 $\pmb { \mathscr { P } }$ 个处理器的超立方上时，参照第八章表8.1可知，通信时间为 $2 \big ( t \llcorner \log \sqrt { \ p } + t _ { \ w } \frac { n ^ { 2 } } { \ p } \big ( \sqrt { \ p } - 1 \big ) \big )$ ;计算时间为 $q \times ( \frac { n } { q } ) ^ { 3 } = \sqrt { p } \times$ $( \frac { n } { \sqrt { \phi } } ) ^ { 3 } = n ^ { 3 } / \phi$ 。所以算法的并行运行时间为：

$$
T _ { \mathrm { p } } = \frac { n ^ { 3 } } { \hbar } + t _ { \mathrm { s } } \mathrm { l o g } \hbar + 2 t _ { \mathrm { w } } \frac { n ^ { 2 } } { \sqrt { \hbar } }
$$

当并行分块乘法执行在 $\sqrt { \pmb { p } } \times \sqrt { \pmb { p } }$ 的二维环绕网孔上时,参照第八章表8.1可知其通信时间为 $2 t _ { \mathrm { s } } \sqrt { \hat { p } } + 2 t _ { \mathrm { w } } \frac { n ^ { 2 } } { \sqrt { \hat { p } } }$ ；计算时间为 $n ^ { 3 } / \phi$ ，所以算法的并行运行时间为：

$$
T _ { \mathrm { p } } = { \frac { n ^ { 3 } } { \phi } } + 2 t _ { \mathrm { s } } { \sqrt { \hat { p } } } + 2 t _ { \mathrm { w } } { \frac { n ^ { 2 } } { \sqrt { \hat { p } } } }
$$

简单并行分块乘法的主要缺点是存储要求过大：通信结束时每个处理器拥有 $2 \sqrt { \ p }$ 个块,每块大小为 $n ^ { 2 } / \phi$ ,所以每个处理器要求 $O ( n ^ { 2 } / { \sqrt { p } } )$ 存储器， $\pmb { \phi }$ 个处理器共要求 $O ( n ^ { 2 } \sqrt { \pmb { \mathscr { p } } } )$ ,它是串行算法存储要求的 $\sqrt { \pmb { \mathscr { p } } }$ 倍。

# 9.4.2 Cannon 乘法

算法原理Cannon算法是一种存储有效的算法。为了使两矩阵的下标满足相乘的要求，它和上一节的并行分块乘法不同，不是阵列的各行和各列施行多到多播送，而是有目的地在各行和各列施行循环移位，从而使处理器的总存储要求可以降下来。照例,将矩阵 $\pmb { A }$ 和 $\pmb { B }$ 分成 $\pmb { \hat { p } }$ 个方块 $\mathbf { A } _ { i } , _ { j }$ 和 $B _ { i , j } ( 0 { \leqslant } i , j { \leqslant } \sqrt { \ p } -$ 1),每块大小为 $( n / \sqrt { \hat { p } } ) \times ( n / \sqrt { \hat { p } } )$ ,并将它们分配给 $\sqrt { \pmb { \mathscr { p } } } \times \sqrt { \pmb { \mathscr { p } } }$ 个处理器 $( \mathtt { P _ { 0 , 0 } }$ ，$\mathrm { P } _ { 0 , 1 } , \cdots , \mathrm { P } _ { \sqrt { \hat { p } } ^ { - 1 } , \sqrt { \hat { p } } ^ { - } 1 } )$ 。开始时处理器 $\mathbf { P } _ { i , j }$ 存放有块 $\mathbf { A } _ { i }$ ,和块 $\mathbf { \delta } _ { B _ { i , j } }$ ,并负责计算块 $\mathbf { C } _ { i , j }$ ,然后算法开始执行：

$\textcircled{1}$ 将块 $A _ { i , j } ( 0 { \leqslant } i , j < \sqrt { \ p } )$ 向左循环移动 $_ i$ 步；将块 $B _ { i , j } ( 0 { \leqslant } i , j < \sqrt { \ p } )$ 向上循环移动 $j$ 步；  
$\textcircled { 2 } \ \mathbb { P } _ { i , j }$ 执行乘-加运算；然后,将块 $A _ { i , j } ( 0 { \leqslant } i , j < \sqrt { \ p } )$ 向左循环移动1步；将块 $B _ { i , j } ( 0 { \leqslant } i , j < \sqrt { \dot { p } } )$ 向上循环移动1步；  
③重复第②步,在Pi,;中共执行p次乘-加运算和p次块Ai,;和Bi,的循环单步移位。

算法举例图9.10示例了在16个处理器上，用Cannon算法执行A4×4×$\mathbf { \delta } \mathbf { B } _ { 4 \times 4 }$ 的过程。其中(a)和(b)对应于上述算法的第 $\textcircled{1}$ 步；(c)、(d)、(e)和(f)对应于上述算法的第 $\textcircled{2}$ 和第 $\textcircled{3}$ 步。注意在算法第 $\textcircled{1}$ 步时， $\pmb { A }$ 矩阵的第0行不移位，第1行循环左移1位，第2行循环左移2位,第3行循环左移3位；类似地， $\pmb { B }$ 矩阵的第0列不移位,第1列循环上移1位,第2列循环上移2位,第3列循环上移3位。

算法描述假定矩阵 $\pmb { A }$ 和 $\pmb { B }$ 分成 $\pmb { \mathscr { P } }$ 块 $\mathbf { A } _ { i , j }$ 与 $B _ { i , j } ( 0 { \leqslant } i , j { \leqslant } \sqrt { \dot { p } } - 1 )$ ,处理器排成 $\sqrt { \pmb { \mathscr { p } } } \times \sqrt { \pmb { \mathscr { p } } }$ 的方阵，符号“ $\Leftarrow$ ”表示移位,则Cannon算法可形式描述如下：

# 算法9.5Cannon分块乘法算法

输入： $A _ { n } \times \ d _ { n } , B _ { n } \times \ d _ { n }$ 输出：Cn×n

Begin

(1)for ${ \pmb k } = { \bf 0 }$ to $\sqrt { \pmb { \mathscr { p } } } - 1$ do for all $\mathrm { P } _ { i , j }$ par-do (i)if $i > k$ then $A _ { i , j } {  } A _ { i , ( j + 1 ) \bmod { \sqrt { \hat { \rho } } } } \mathbf { e }$ ndif (ii)if $j > k$ then $B _ { i , j } {  } B _ { ( i + 1 ) \mathrm { m o d } \sqrt { \hat { p } } , j }$ endif endfor endfor (2)for all $\mathrm { P } _ { i , j } \mathrm { \bf ~ p a r { - } d o } C _ { i , j } = 0$ endfor (3)for ${ \pmb k } = { \bf 0 }$ to $\sqrt { \phi } - 1$ do for all $\mathbf { P } _ { i , j }$ par-do $\begin{array} { r l } & { \mathrm { ( i ) } C _ { i , j } = C _ { i , j } + A _ { i , j } \circ B _ { i , j } } \\ & { \mathrm { ( i i ) } A _ { i , j } { \Leftarrow } A _ { i , ( j + 1 ) \mathrm { m o d } \sqrt { \hslash } } } \\ & { \mathrm { ( i i i ) } B _ { i , j } { \Leftarrow } B _ { ( i + 1 ) \mathrm { m o d } \sqrt { \hslash } , j } } \end{array}$ endfor endfor End

算法分析当算法执行在 $\pmb { \mathscr { p } }$ 个处理器的超立方上时,若使用CT选路法,算法第(1)步的循环移位时间(参照第八章表8.1)为2（ts+tw $2 \big ( t _ { \mathrm { s } } + t _ { \mathrm { w } } \frac { n ^ { 2 } } { \phi } + t _ { \mathrm { h } } \log \sqrt { \phi } \big )$ ,算法第(3)步的单步移位时间为2（ts+tw $2 ( t _ { \mathrm { s } } + t _ { \mathrm { w } } \frac { n ^ { 2 } } { \phi } ) \sqrt { \phi }$ ，当 $\pmb { \mathscr { P } }$ 充分大时后者为主项。算法第(3)步共执行 $\sqrt { \phi }$ 次 $( n / \sqrt { \hat { p } } ) \times ( n / \sqrt { \hat { p } } )$ 子块乘法，其时间为 $\sqrt { \pmb { \mathscr { p } } } \times ( \pmb { n } \sqrt { \pmb { \mathscr { p } } } ) ^ { 3 } =$ $n ^ { 3 } / \phi$ 。所以在超立方上Cannon乘法的并行运行时间为：

$$
T _ { \mathrm { p } } = { \frac { n ^ { 3 } } { \hbar } } + 2 { \sqrt { \hbar } } t _ { \mathrm { s } } + 2 t _ { \mathrm { w } } { \frac { n ^ { 2 } } { \sqrt { \hbar } } }
$$

![](images/204600d07040cb0aaeb9fbf9e1777cdb6cdc602ca4814122f693d1891b2bc383.jpg)  
图9.1016处理器上Cannon乘法过程${ \bf \Pi } ( { \bf a } ) { \bf A }$ 阵起始对准； $( \boldsymbol { \mathbf { b } } ) \pmb { \mathbf { \{ \delta \mu } } $ 阵起始对准；(c)起始对准后的 $\pmb { A }$ 和 $\pmb { \cal B }$ ：(d)第一次移位后的子阵位置；(e)第二次移位后的子阵位置； (f)第三次移位后的子阵位置

当算法执行在 $\sqrt { \phi } \times \sqrt { \phi }$ 的二维网孔上时,算法第(1)步的循环移位时$2 (  { t _ { \mathrm { s } } } +  { t _ { \mathrm { w } } } \frac {  { n } ^ { 2 } } {  { p } } ) \sqrt {  { p } }$ 2)p,算法第(3)步的单步移位时间为2（ts+tw $2 ( t _ { \mathrm { s } } + t _ { \mathrm { w } } \frac { n ^ { 2 } } { \hat { P } } ) \sqrt { \hat { p } }$ 。算

法第(3)步的运算时间为 $n ^ { 3 } / \phi$ 。所以在二维网孔上Cannon乘法的并行运行时间为：

$$
T _ { \mathrm { p } } = { \frac { n ^ { 3 } } { \hbar } } + 4 { \sqrt { \hbar } } t _ { \mathrm { s } } + 4 t _ { \mathrm { w } } { \frac { n ^ { 2 } } { \sqrt { \hbar } } }
$$

# 9.4.3 Fox 乘法

算法原理 $\mathbf { F o x }$ 算法是另一种存储有效的算法，它和并行分块乘法及Can-non乘法均不同,执行Fox乘法时，行处理器施行一到多播送，而列处理器施行循环单步上移，从而使处理器的存储要求可以降下来。照例,将矩阵 $\pmb { A }$ 和 $\pmb { B }$ 分成 $\pmb { \hat { p } }$ 个方块 $\mathbf { A } _ { i }$ ,和 $\pmb { \mathscr { B } } _ { i }$ ,j $( 0 { \leqslant } i , j { \leqslant } \sqrt { \pmb { \phi } } - 1 )$ ,每块大小为 $( n / \sqrt { \hat { p } } ) \times ( n / \sqrt { \hat { p } } )$ ,并将它们分配给 $\sqrt { \pmb { \mathscr { p } } } \times \sqrt { \pmb { \mathscr { p } } }$ 个处理器 $( \mathrm { P } _ { \boldsymbol { 0 } , 0 , } \mathrm { P } _ { \boldsymbol { 0 } , 1 } , \cdots , \mathrm { P } _ { \sqrt { p } - 1 , \ \sqrt { p } - 1 } )$ 。开始时处理器 $\mathrm { P } _ { i , j }$ 存放有块 $\pmb { A } _ { i }$ ,;和块 $\mathbf { \delta } _ { B _ { i , j } }$ ,并负责计算块 $\mathbf { C } _ { i , j \circ }$ 假定首先选定对角块 $\mathbf { A } _ { i , i }$ 向同行的$\sqrt { \phi } - 1$ 个处理器进行一到多播送，则 $\mathtt { F o x }$ 算法执行以下各步 $\sqrt { \phi }$ 次迭代即可完成：

$\textcircled{1}$ 所选中的对角块 $\mathbf { A } _ { i }$ ,向所在行的 $\sqrt { \beta } - 1$ 个处理器进行一到多播送；  
$\textcircled{2}$ 各处理器将所收到的 $\pmb { A }$ 阵的块与 $\pmb { B }$ 阵原有的块进行乘-加运算；  
$\textcircled{3} \textbf { \textB { } }$ 阵的块向上循环1步；  
$\textcircled{4}$ 如果 $\mathbf { A } _ { i , j }$ 是本次播送的块,则下一次应选块 $A _ { i } , ( { j + 1 } ) _ { \mathrm { m o d } } \sqrt { { \small { \phi } } }$ 向同行的 $\sqrt { \pmb { \mathscr { p } } } -$ 1个处理器播送，然后转第 $\textcircled{2}$ 步。

算法举例图9.11示例了在16个处理器上，用 $\mathtt { F o x }$ 算法执行 $\mathbf { A _ { 4 } } \times 4 \mathbf { \Omega } \times \mathbf { \Omega }$ $\pmb { { \cal B } } _ { 4 \times 4 }$ 时的块 $\pmb { A }$ 的播送与块 $\pmb { B }$ 的单步循环上移的过程。

算法分析当算法执行在 $\pmb { \mathscr { P } }$ 个处理器的超立方上时,若使用CT选路法,块A的总的一到多播送时间(参照第八章表8.1)为 $\frac { 1 } { 2 } ( t _ { \mathrm { s } } \sqrt { \hbar } + t _ { \mathrm { w } } \frac { n ^ { 2 } } { \sqrt { \hbar } } ) \log { \hbar }$ ，而块$\pmb { \cal B }$ 的总的循环单步上移的时间比起它来不是主要的;照例 $\mathbf { P } _ { i , j }$ 执行运算的时间为 $n ^ { 3 } / \phi$ 。所以在超立方上Fox乘法的并行运行时间为：

$$
T _ { \mathrm { p } } = \frac { n ^ { 3 } } { \hbar } + \frac 1 2 t _ { \mathrm { s } } \sqrt { \hbar } \log { \phi } + \frac 1 2 t _ { \mathrm { w } } \frac { n ^ { 2 } } { \sqrt { \hbar } } \log { \phi }
$$

# 9.4.4 DNS 乘法

算法原理如前所述,使用棋盘划分最多可用 ${ \pmb n } ^ { 2 }$ 个处理器，算法的加速可达 $O ( n ^ { 2 } )$ 。下面介绍一种使用更多的处理器可得到更快的算法，即 DNS算法，从而加速比也更高。

DNS 是三位学者Dekel、Nassimi、Sahni 名字的首字母,他们的算法是运行在超立方连接的SIMD机器上的。

![](images/f41962f06b27e14c99f9b3c74064cf9d268a7549276552042281381aac26a69f.jpg)  
图9.1116个处理器上 $\mathbf { F o x }$ 乘法通信过程(a)A0,0等一到多播送， $\pmb { B _ { i } }$ ,j循环上移； $( \mathbf { b } ) \mathbf { A } 0 , 1$ 等一到多播送， $\mathbf { \delta } _ { B _ { i , j } }$ 循环上移；$( \mathsf { c } ) \mathbf { { A 0 } } , 2$ 等一到多播送， $\mathbf { \delta } _ { B _ { i , j } }$ 循环上移； $( \mathsf { d } ) \mathbf { A } \mathsf { 0 } , 3$ 等一到多播送

在 $\pmb { A } _ { n } \times _ { n } \times \pmb { B } _ { n } \times _ { n }$ 的运算中, $a _ { i s } \times b _ { s j }$ 的操作共有 $\pmb { n } ^ { 3 }$ 个。如果对矩阵 $\pmb { A }$ 和 $\pmb { B }$ 的元素进行适当的复制,则有可能利用 $\pmb { n } ^ { 3 }$ 个处理器同时执行 $n ^ { 3 }$ 个乘法运算,然后再作 $\log n$ 次求和运算即可得到最终的乘积元素 $c _ { i j }$ 。为此将处理器数目$\scriptstyle { p = n ^ { 3 } }$ 表示成 $\pmb { n } \times \pmb { n } \times \pmb { n }$ 的三维数组,其中 $\pmb { n } = 2 ^ { q }$ 。这样超立方中的处理器 $\mathbf { P } _ { r }$ 将处于位置 $( i , j , k )$ ,其中 $r = i n ^ { 2 } + j n + k$ ，且 $0 { \leqslant } i , j , k { \leqslant } n - 1$ 。令 $r$ 的二进制表示为 $r _ { 3 q - 1 } , \cdots , r _ { 2 q } r _ { 2 q - 1 } , \cdots , r _ { q } r _ { q - 1 } , \cdots , r _ { 0 }$ ，其中 $r _ { b }$ 表示从 $r _ { 0 }$ 数起的 $r$ 的第b位。显然下标i,j,k分别对应着r3q-1,,r2q,r2q-1,…,rq,rq-1,,r0o

假定每个处理器 $\mathrm { \bf P } _ { r }$ 有三个寄存器 $A _ { r } \setminus B _ { r } \setminus C _ { r }$ 。开始时处于位置 $( \mathbf { 0 } , j , k )$ 的处理器 $\mathbf { P } _ { s }$ 其 $\pmb { A } _ { s }$ 和 $\pmb { { \cal B } } _ { s }$ 中的内容为 $a _ { j k }$ 和 $b _ { j k }$ ,所有其它处理器的寄存器内容均置为0,算法结束时， $c _ { j k } = \sum _ { i = 0 } ^ { n - 1 } a _ { j i } \times b _ { j k } \circ$ aj×bjk。算法可分为三步：

$\textcircled{1}$ 数据复制： $\mathbf { A } _ { n } \times \mathbf { \nabla } _ { n }$ 与 $\pmb { { \cal B } } _ { n } \times \mathbf { \nabla } _ { n }$ 的元素加载到 $\mathbf { P } _ { 0 , j , k }$ 中的A和B寄存器中；通过A、B同时在 $\textbf { \em i }$ 维复制， $\pmb { A }$ 在 $\pmb { k }$ 维复制和 $\mathbf { B }$ 在 $j$ 维复制后，矩阵 $\pmb { A }$ 和 $\pmb { B }$ 元素就被分配到 $n ^ { 3 }$ 个处理器中了；

$\textcircled{2}$ 施行相乘：各处理器将A寄存器之内容与B寄存器之内容两两相乘；

$\textcircled{3}$ 求和运算：执行 $\sum _ { i = 0 } ^ { n - 1 } C _ { i , j , k \circ }$ (a)初始加载； $( \ b )  { \mathbf { A } } \setminus \pmb { B }$ 沿 $\pmb { i }$ 维复制； $( { \mathfrak { c } } ) \mathbf { { A } }$ 沿 $k$ 维复制； $( d ) B$ 沿 $\pmb { j }$ 维复制；(e)施行点积；(f)相加得最终结果

![](images/ac0a1e004bea125d8270bce1fe67151813965dc86c9219baf72d77103d39e112.jpg)  
图9.12 DNS乘法的执行过程

算法举例假定 $\pmb { A } = \left( \begin{array} { r r } { 1 } & { 2 } \\ { 3 } & { 4 } \end{array} \right) , \pmb { B } = \left( \begin{array} { r r } { - 5 } & { - 6 } \\ { 7 } & { 8 } \end{array} \right)$ ,图9.12示例了DNS乘法的过程：图9.12(a)是初始加载;图9.12(b)为A和B寄存器同时按 $_ i$ 维进行复制，即 $r _ { 2 } = 0$ 的那些处理器中 $A , B$ 寄存器之内容复制到 $r _ { 2 } = 1$ 的那些处理器的相应寄存器中；图 $9 . 1 2 ( \mathbf { c } )$ 为 $\pmb { A }$ 寄存器按 $k$ 维进行复制，即凡是 $\mathbf { \nabla } r _ { 0 } = r _ { 2 }$ 的那些处理器中 $\pmb { A }$ 寄存器之内容复制到 $r ^ { ( 0 ) }$ 的那些处理器的 $\pmb { A }$ 寄存器中,其中 $r ^ { ( 0 ) }$ 表示 $_ r$ 的第0位取反；图9.12(d)为 $B$ 寄存器按 $j$ 维进行复制，即凡是 $r _ { 1 } = r _ { 2 }$ 的那些处理器中 $B$ 寄存器之内容复制到 $r ^ { ( 1 ) }$ 的那些处理器的 $B$ 寄存器中,其中r(1)表示r的第1位取反;图9.12(e)为A和B寄存器中的元素之乘积;图9.12

（f)为最终之结果。

算法描述令 $r ^ { ( m ) }$ 表示 $r$ 的第 $\mathbf { \nabla } m$ 位取反； $\mid { \pmb { \mathscr { P } } } , r _ { m } = d \mid$ 表示整数 $r ( 0 { \leqslant } r { \leqslant }$ ${ \pmb { \rho } } - { \bf 1 } )$ 的集合， $r$ 的二进制表示为 $r _ { 3 q - 1 } \cdots r _ { m + 1 } \mathrm { d } r _ { m - 1 } \cdots r _ { 0 0 }$

算法9.6 DNS乘法算法输入： $A _ { n \times n } , B _ { n \times n } , n = 2 ^ { q }$ 输出： $C _ { n \times n }$

Begin

(1）for $m = 3 q \textrm { -- } 1$ to $2 q$ do $\big / \star$ 按 $i$ 维复制 $\mathbf { A } , \mathbf { B } \ast \mathbf { \ell } /$ for all $_ r$ in $\{ \pmb { \mathscr { p } } , r _ { m } = 0 \} \mathbf { p a r } - \mathbf { d o }$ $\begin{array} { l } { { ( 1 . 1 ) A _ { r } { } ^ { ( m ) } {  } A _ { r } } } \\ { { ( 1 . 2 ) B _ { r } { } ^ { ( m ) } {  } B _ { r } } } \end{array}$ endfor endfor

(2）for $m = q - 1$ to $0 ~ \mathrm { d } \mathbf { 0 } ~ / \star$ 按 $k$ 维复制 $\mathbf { A } \ast { \mathbf { \zeta } } ^ { \prime }$ for all $r$ in $\left\{ \ p , r _ { m } = r _ { 2 q + m } \right\}$ par-do ${ \pmb { A } } _ { r } { \bf \Sigma } ^ { ( m ) } {  } { \pmb { A } } _ { r }$ endfor endfor

(3）for $m = 2 q - 1$ to $\pmb q$ do $\big / \ast$ 按 $j$ 维复制 $\pmb { \mathcal { B } } \ast \boldsymbol { \mathit { \iota } }$ for all $r$ in $\left\{ \mathbf { \nabla } _ { \mathbf { \mathcal { P } } } , r _ { m } = r _ { q + m } \right\}$ par-do $\mathbf { B } _ { r } ^ { { ( m ) } } { \gets } \mathbf { B } _ { r }$ endfor endfor

(4） for $\boldsymbol r = 0$ to ${ \pmb { \mathscr { p } } } - 1 \ \mathbf { p a r } - \mathbf { d o } \ / \ { \pmb { \mathscr { x } } }$ 相乘 $\yen 7$ $\pmb { C } _ { r } = \pmb { A } _ { r } \times \pmb { B } _ { r }$ endfor

(5) for $m = 2 q$ to $3 q - 1$ do $\gamma *$ 求和 $\yen 7$ for $\mathbf { \nabla } _ { r } = \mathbf { 0 }$ to $\pmb { \mathscr { p } } - 1 \ \pmb { \mathrm { p a r } } - \ \pmb { \mathrm { d o } }$ $C _ { r } { = } C _ { r } { + } C _ { r } { ^ { ( m ) } }$ endfor endfor

End

![](images/a61572003f89b2136a8f363c4d78e5d3ab8562f4e6df6adc7bf6f89384cd23f6.jpg)  
图9.13 $4 \times 4$ 的矩阵在64个处理器上的DNS乘法(a)A、B起始分布；（b)Ai,,从P,j,o传到P.,;(c）所有 $\pmb { A } _ { i , j }$ 沿 $j$ 维播送；（d)所有 $\pmb { B } _ { i }$ 沿 $_ i$ 维播送

算法分析由算法9.6可知,使用 $n ^ { 3 }$ 个处理器的DNS 乘法,其并行运行时间为 $O ( \log n )$ ,它不是成本最佳的。

算法讨论在图9.12中,是以 $\pmb { A } _ { 2 \times 2 } \times 2 \pmb { B } _ { 2 \times 2 }$ 为例的，如果矩阵的阶超过2（例如为4),则这种表示就不方便了，但可以采用图9.13所示的方法进行DNS相乘。图9.13(a)是 $\pmb { A }$ 和 $\pmb { B }$ 的起始加载，此时 $\pmb { A }$ 矩阵的行按 $j$ 维分布； $\pmb { B }$ 矩阵的列按 $_ i$ 维分布。复制时，首先 $\pmb { A }$ 和 $\pmb { B }$ 同时沿 $\pmb { k }$ 维进行一到一播送,其中如图9.13(b), $\mathbf { A } _ { i , j }$ 从 $\mathrm { P } _ { i , j , 0 }$ 传到 $\mathbf { P } _ { i , j , j }$ (类似地 $\pmb { { \cal B } } _ { i }$ ,j从 $\mathbf { P } _ { i , j , 0 }$ 传到 $\mathbf { P } _ { i , j , i } )$ ；然后 $\pmb { A }$ 在不同的 $\pmb { k }$ 平面内将其列沿 $j$ 维同时进行一到多播送，其结果如图 $9 . 1 3 ( \mathfrak { c } )$ 所示。类似地, $\pmb { B }$ 在不同的 $k$ 平面内将其行沿 $_ i$ 维同时进行一到多播送,其结果如图9.13(d)所示。复制完毕后， $\mathbf { A } _ { i , k }$ 与 $\mathbf { B } _ { k }$ ,,就可以在 $\mathbf { P } _ { i , j , k }$ 中相乘了；然后每个乘积元素$\mathbf { { C } } _ { i } ,$ 再沿 $k$ 维进行单点累积。在此过程中,处理器 $\mathbf { P } _ { i , j , 0 }$ 就收集了来自处理器$\mathbf { P } _ { i , j , 1 } , \cdots , \mathbf { P } _ { i , j , n - 1 }$ 的乘积。为了清楚起见，图9.13(c)和 $(  { \mathbf d } )$ 只示出了 $\pmb { C } _ { 0 , 0 }$ 的计算。

当处理器的数目 $\ p < n ^ { 3 }$ 时,为了执行 DNS乘法,可以假定 $\pmb { \mathscr { p } } = q ^ { 3 }$ ,而 $q <$ $\pmb { n }$ 。此时原 ${ \pmb n } \times { \pmb n }$ 的矩阵可以划分成大小为 $( n / q ) \times ( n / q )$ 的一些块,每个矩阵可以视为 ${ \pmb q } \times { \pmb q }$ 的分块矩阵。这样在 $q ^ { 3 }$ 个处理器上执行DNS算法与在 $\mathbf { \dot { \boldsymbol { n } } } ^ { 3 }$ 个处理器上执行DNS算法类似，只是前者是块运算后者是单独元素运算。

当分块的DNS算法执行在 $\scriptstyle { p < n ^ { 3 } }$ 个处理器的超立方上时，若使用CT选路法,算法执行一到一传送的时间为 $t _ { \mathrm { s } } + t _ { \mathrm { w } } ( n / q ) ^ { 2 } + t _ { \mathrm { h } } \mathrm { l o g } q$ （见第八章8.2节）；算法执行一到多播送的时间为 $( t _ { \mathrm { s } } + t _ { \mathrm { w } } ( n / q ) ^ { 2 } ) \mathrm { l o g } q$ (见第八章表8.1);算法执行单点收集的时间为 $t \sqrt { \smash [ b ] { 3 } q + t  { \mathbf { w } } ( \ b { n } / q ) ^ { 2 }  { \log { q } } }$ 。假定乘-加操作取单位时间，则 $\left( n \right/$ $\mathbf { \boldsymbol { q } } ) \times ( \mathbf { \boldsymbol { n } } / q )$ 块阵乘法的时间为 $( n / q ) ^ { 3 }$ 。略去一到一传送时间和收集过程中的加法时间,则在超立方上使用CT选路法的DNS乘法之并行运行时间为：

$$
T _ { \mathrm { p } } { \approx } ( \frac { n ^ { 3 } } { q } ) + 3 t _ { \mathrm { s } } { \log } q + 3 t _ { \mathrm { w } } \bigl ( \frac { n } { q } \bigr ) ^ { 2 } { \log } q
$$

因为 $q = \pmb { \mathscr { p } } ^ { 1 / 3 }$ ，所以

$$
T _ { \mathrm { p } } = { \frac { n ^ { 3 } } { \hbar } } + t _ { \mathrm { s } } \mathrm { l o g } \hbar + t _ { \mathrm { w } } { \frac { n ^ { 2 } } { { \hbar } ^ { 2 / 3 } } } \mathrm { l o g } \hbar
$$

# 9.5小结和导读

小结本章所研究的矩阵都是稠密阵，又称为满阵(FullMatrices),与其相对是稀疏阵(SparseMatrices)。稠密阵几乎没有零元素，而稀疏阵其绝大多数元素均为零。之所以要区分出稀疏阵，是因为可以利用非零元素的号码与位置来减少运算时间。本章着重讨论了稠密阵的最基本的运算,包括矩阵转置、矩阵乘向量和矩阵乘法等运算。这些算法在执行过程中几乎用到了第八章所讲的所有基本通信操作，所以在分析算法的通信时间时，读者要不断参照第八章的有关

内容。

从处理器的利用能力等来看，棋盘划分比带状划分要好，这一点从第9.3节“矩阵-向量乘法”的讨论可以得到证实;简单的并行分块乘法虽然运行时间较快,但对存储要求过大;从存储要求来看，Cannon乘法和Fox乘法优于简单并行分块乘法，特别是Cannon乘法综合性能较优，所以使用得较普遍；从加速能力来看,DNS乘法的加速比较大，特别是它经常被别的算法作为基本算法加以调用,所以使用较广。

除了本章所讨论的矩阵运算外，矩阵的分解、矩阵的求逆和矩阵求特征值等也是很常见的矩阵运算，但限于篇幅，就不再讨论了。

导读关于并行与分布式数值算法，[31]是一本很好的参考书。有关矩阵运算,[78]是一本很经典的教本(此书的第一版有中译本：廉庆荣等译.矩阵计算.大连：大连理工大学出版社,1988)。本章所讨论的Cannon乘法、Fox乘法和DNS乘法，原始论文分别来源于[40]、[68]和[58]。这些算法的改进版本可参考[30]和[94]。有关并行矩阵算法的可扩放性分析，读者可阅读[84]。在[113,114]书中的第五章的参考文献注释中还列举了大量有关稠密矩阵的算法，读者可追踪进一步阅读。

# 习 题

9.1根据9.2.1节所讨论的矩阵转置算法：

$\textcircled{1}$ 试写出二维网孔上递归矩阵转置算法的形式描述；  
$\textcircled{2}$ 试写出超立方上递归矩阵转置算法的形式描述。

9.2根据9.3.2节所讨论的矩阵-向量乘法，试证明：在 $\pmb { \hat { p } }$ 个处理器的超立方上，用SF选路方法进行矩阵-向量乘法,其并行运行时间约为n²/p+tlogp+(3/2)tw(n/√p)logp。

）.3试分析在超立方上执行矩阵-向量乘法时，使用棋盘划分比带状划分为优。

9.4试证明:在使用带状划分的超立方上执行矩阵-向量乘时，其等效率函数$f _ { \mathtt { E } } ( \mathbf { \Psi } _ { \pmb { \mathscr { P } } } ) = O ( \mathbf { \Psi } _ { \pmb { \mathscr { P } } } ^ { 2 } ) _ { \mathtt { c } }$

[提示：将(9.4)式代人 $\pmb { \phi } ^ { \star } \mathbb { T } _ { \mathbb { P } } = \pmb { T } _ { 0 } + \pmb { W }$ 从而求出 $T _ { 0 }$ ，再由 $\pmb { W } = \pmb { K } \pmb { T } _ { 0 }$ 和 $\scriptstyle { \overrightarrow { W } } = n ^ { 2 }$ 求出 $\pmb { n }$ 与 $\pmb { \hat { p } }$ 的关系，最后求出等效率函数 $f _ { \Xi } ( \pmb { \mathscr { p } } ) = f ( \pmb { \mathscr { p } } ) ]$ 。

9.5试证明：在使用棋盘划分的网孔上执行矩阵-向量乘时，其等效率函数

$$
f _ { \mathrm { E } } ( \boldsymbol { \phi } ) = O ( \operatorname* { m a x } \{ \boldsymbol { \phi } ^ { 3 / 2 } , \boldsymbol { \phi } \log \boldsymbol { \phi } \} ) \mathrm { , }
$$

[提示：参见习题9.4的提示。]

9.6试证明：在超立方上，并行分块矩阵乘法和Cannon乘法的等效率函数均为fe（p）=$O ( p ^ { 3 / 2 } )$ ；而 $\mathtt { F o x }$ 乘法的等效率函数为 $f _ { \mathtt { E } } ( \mathtt { \Delta } _ { \mathtt { p } } ) = O ( \mathtt { \Delta } _ { \mathtt { p } } ^ { 3 / 2 } \mathrm { l o g } \mathtt { p } )$ 。

9.7根据9.4.3节所讨论的Fox乘法：

$\textcircled{1}$ 试写出 $\mathbf { F o x }$ 乘法的形式描述；

$\textcircled{2}$ 试分析 $\mathtt { F o x }$ 乘法的主要优点是什么。

9.8试推导：在 $\boldsymbol { p } ^ { 1 / 3 } \times \boldsymbol { p } ^ { 1 / 3 } \times \boldsymbol { p } ^ { 1 / 3 }$ 三维网孔上，使用CT选路方法时DNS乘法的并行运行时间。

9.9算法9.7给出了 $n ^ { 2 }$ 个处理器的并行系统上用PRAM-CREW模型施行两个 $\mathbf { \Omega } _ { n } \times \mathbf { \Omega } _ { n }$ 矩阵相乘的算法。假定存储器的读写时间为 $\pmb { t _ { a } }$ ，两个元素的乘－加时间为 $t _ { \mathrm { c } }$ 。试分析该算法的并行运行时间。

算法9.7 PRAM-CREW上矩阵相乘算法  
输入: Anxn,Bn×n  
输出： $C _ { n \times n }$   
Begin(1)将 ${ \pmb n } ^ { 2 }$ 个处理器组织成 ${ \pmb n } \times { \pmb n }$ 的网孔(2)for each $\mathrm { P } _ { i , j }$ do(2.1) $\pmb { c _ { i , j } = 0 }$ (2.2)for $k = 0$ to $\pmb { n } - \pmb { 1 }$ do$c _ { i , j } = c _ { i , j } + a _ { i , k } \times b _ { k , j }$ endforendfor  
End

9.10参照图9.14,算法9.8描述了m×k二维Systolic阵列上实现Am×n×Bxk=Cm×k的矩阵乘法,它是采用流水线原理,通过在时间上延迟矩阵元素的办法来达到一对下标合宜的矩阵元素适时相乘的目的。

算法9.8 $\mathbf { S I M D } ^ { - } \mathbf { M C } ^ { 2 }$ 上 Systolic矩阵相乘算法  
输入： $\mathbf { A } _ { m \times n } , \mathbf { B } _ { n \times k }$   
输出：在 $\mathrm { P } _ { i , j }$ 中存有乘积矩阵元素 $c _ { i , j }$   
Beginfor ${ \bf \nabla } _ { i } = 1$ to m par - dofor $j = 1$ to $k \ p a r - \mathrm { d } \mathbf { 0 }$ (1) $c _ { i , j } = 0$ (2） while $\ P _ { i , j }$ 收到 $^ { a }$ 和 $^ b$ 时 ${ \bf d o }$ $( 2 . 1 ) c _ { i , j } = c _ { i , j } + a \times b$ (2.2)if $i < m$ then 发送 $^ { b }$ 给 $\mathrm { P } _ { i + 1 , j }$ endif(2.3)if $j < k$ then 发送 $^ { a }$ 给 $\mathrm { P } _ { i , j + 1 }$ endifendwhileendforendfor  
End

![](images/e3745e7ca92cf04127b4413b56c656e1699b43531e430d3c85fb6ab84e7bb66d.jpg)  
图9.14矩阵 $\pmb { A }$ 和 $\pmb { \cal B }$ 的输入加载方式

试问： $\textcircled{1}$ 为了确保 ${ \pmb { a } } _ { i }$ 与 $\delta _ { s , j }$ 适时在 $\mathbf { P } _ { i , j }$ 相遇， $\pmb { A }$ 矩阵的第i行要比第i-1行 $( 2 \leqslant i \leqslant m )$ 滞后多少时间单位？同样， $\mathbf { B }$ 矩阵的第 $\pmb { j }$ 列要比第 $j - 1$ 列 $( 2 { \leqslant } j { \leqslant } k )$ 滞后多少时间单位？

$\textcircled{2}$ 当 $j = k$ 时， $\pmb { \alpha }$ 传送给 $\pmb { \mathrm { P } } _ { i , j + 1 }$ 吗？当 $i = m$ 时， $b$ 传送给 $\bar { \mathbf { P } } _ { i + 1 , j }$ 吗?

# 第十章 线性方程组的求解

很多科学与工程计算问题大都可以化为线性代数方程组的形式，所以有效的求解线性方程组在科学和工程计算中是非常重要的。虽然线性代数方程的求解方法和数值计算软件包(如Linpack等)均很成熟，但随着并行计算机的发展，问题的求解速度和解题规模都大大提高，因而使数值计算方法和相应的数学软件包都产生了变化,相应地线性方程组的有效并行求解也引起了人们的普遍关注。本章主要讨论基本线性方程组的求解,包括三角形方程组的求解、三对角方程组的求解、稠密线性方程组的求解和稀疏线性方程组的求解。对于每一种求解问题,我们首先讨论它的数值求解数学原理;接着给出其串行算法;然后分析串行算法中的并行性及并行化方法并给出相应的并行算法(有时我们只作简单的并行化分析）。

# 10.1三角形方程组的求解

# 10.1.1基本术语

本小节是预备性知识。为了读者阅读下文方便,先给出几个有关定义：

定义10.1一个 $\pmb { n }$ 个变量 $x _ { 1 } , x _ { 2 } , \cdots , x _ { n }$ 的线性方程(Linear Equation)可表示为：

$$
a _ { 1 } x _ { 1 } + a _ { 2 } x _ { 2 } + \cdots + a _ { n } x _ { n } = b
$$

其中， $a _ { 1 } , a _ { 2 } , \cdots , a _ { n }$ 和 $^ { b }$ 均为常数。

定义10.2变量 $x _ { 1 } , x _ { 2 } , \cdots , x _ { n }$ 的一组线性方程称为 $\pmb { n }$ 元线性方程组(Sys-tem of Linear Equations),也详称为 $\pmb { n }$ 个变量 $\pmb { n }$ 个方程线性联立方程组，简称为线性系(Linear System),可表示为：

$$
\begin{array} { c } { \alpha _ { 1 1 } x _ { 1 } + a _ { 1 2 } x _ { 2 } + \cdots + a _ { 1 n } x _ { n } = b _ { 1 } } \\ { \qquad \quad } \\ { a _ { 2 1 } x _ { 1 } + a _ { 2 2 } x _ { 2 } + \cdots + a _ { 2 n } x _ { n } = b _ { 2 } } \\ { \qquad \quad } \\ { \qquad \vdots \qquad \quad } \\ { \qquad \quad } \\ { a _ { \mathrm { \scriptsize ~ - ~ 1 ~ } } x _ { 1 } + a _ { \mathrm { \scriptsize ~ - ~ 2 ~ } } x _ { 2 } + \cdots + a _ { \mathrm { \scriptsize ~ ~ - ~ } } r = b } \end{array}
$$$$
\alpha _ { n 1 } x _ { 1 } + \alpha _ { n 2 } x _ { 2 } + \cdots + \alpha _ { n n } x _ { n } = b _ { n }
$$

它通常也可写成矩阵-向量形式：

$$
\begin{array} { r } { \left( \begin{array} { c c c c c } { a _ { 1 1 } } & { a _ { 1 2 } } & { \cdots } & { a _ { 1 n } } \\ { a _ { 2 1 } } & { a _ { 2 2 } } & { \cdots } & { a _ { 2 n } } \\ & { \vdots } & & & \\ { a _ { n 1 } } & { a _ { n 2 } } & { \cdots } & { a _ { n n } } \end{array} \right) \left( \begin{array} { c } { x _ { 1 } } \\ { x _ { 2 } } \\ { \vdots } \\ { x _ { n } } \end{array} \right) = \left( \begin{array} { c } { b _ { 1 } } \\ { b _ { 1 } } \\ { \vdots } \\ { b _ { n } } \end{array} \right) } \end{array}
$$

简记之为 $\mathbf { A } { \boldsymbol { \mathbf { \mathit { x } } } } = \mathbf { \mathit { \mathbf { b } } }$ 。其中矩阵 $\pmb { A }$ 中非零元素的位置和值决定了求解 $_ { x }$ 的困难复杂程度。通常一个顺序求解 $\mathbf { \nabla } \mathbf { \pmb { A } } \mathbf { \nabla } \pmb { x } = \mathbf { \nabla } \mathbf { \delta }$ 的算法的时间复杂度为 $O ( n ^ { 3 } )$

定义 10.3一个 $\textbf { \em n } \times \textbf { \em n }$ 的矩阵是上三角(Upper Triangular）的,如果 $i > j$ 时， $a _ { i j } = 0$ 。

定义 10.4一个 $\textbf { \em n } \times \textbf { \em n }$ 的矩阵是下三角(Lower Triangular)的,如果 $i < j$ 时， $\alpha _ { i j } = 0$ 。

定义10.5一个 $\pmb { n } \times \pmb { n }$ 的矩阵是三对角(Tridiagonal)的,当且仅当 $| i - j |$ $> 1$ 时， $a _ { i j } = 0 _ { \circ }$

相应地，在 $\mathbf { A } \mathbf { x } = \mathbf { b }$ 中,若系数矩阵 $\pmb { A }$ 是上(下)三角的,则称其为上(下)三角线性方程组；若系数矩阵 $\pmb { A }$ 是三对角的，则称其为三对角线性方程组。

零元素出现在适当位置的线性方程组比任意形式的方程组的求解要快得多。例如上三角线性方程组和下三角线性方程组，在串行机上可在 $O ( n ^ { 2 } )$ 时间界内求解;而三对角线性方程组则可在 $O ( n )$ 时间界内求解。

定义 10.6一个 $\pmb { n } \times \pmb { n }$ 的矩阵是对角占优(Diagonal Dominant）的,如果 $\mid a _ { i i } \mid$ $> \sum _ { j \neq i } ^ { } \mid a _ { i j } \mid , 1 { \leqslant i , j { \leqslant n _ { \circ } } }$

定义10.7一个n×n的矩阵是对称(Symmetric)的,如果aj=ai,1≤i,j$\leqslant n$ 。

定义10.8一个 ${ \pmb n } \times { \pmb n }$ 的矩阵称为正定(Positive Definite)的,如果对于非零向量 $\pmb { X }$ 及其转置 $\pmb { X } ^ { \mathsf { T } }$ ，则乘积 $\pmb { X } ^ { \updownarrow } \pmb { A } \pmb { X } > 0$ 。

例如所有对称的、对角占优的且 $a _ { j i } > 0$ 的矩阵都是正定的。

# 10.1.2上三角方程组的求解

SISD上回代解法先看一个例子。假定欲求解以下上三角方程组：

$$
\begin{array} { r } { { 1 } x _ { 1 } + { 1 } x _ { 2 } - { 1 } x _ { 3 } + { 4 } x _ { 4 } = 8 } \\ { - 2 x _ { 2 } - 3 x _ { 3 } + { 1 } x _ { 4 } = 5 } \\ { 2 x _ { 3 } - 3 x _ { 4 } = 0 } \\ { 2 x _ { 4 } = 4 } \end{array}
$$

先求解最后一个方程,得x4=2,将其值代入其它方程,清去x4这一项,从而有

$$
\begin{array} { r l } { { 1 } x _ { 1 } + 1 x _ { 2 } - 1 x _ { 3 } \quad } & { { } = 0 } \\ { - 2 x _ { 2 } - 3 x _ { 3 } \quad } & { { } = 3 } \end{array}
$$

$$
\begin{array} { r l r l } { { 2 } x _ { 3 } } & { { } } & { } & { { } = 6 } \\ { 2 x _ { 4 } } & { { } } & { } & { { } = 4 } \end{array}
$$

再求解第3个方程,得 $_ { x _ { 3 } } = 3$ ,将其代人第1和2个方程,消去 $x _ { 3 }$ 这一项,从而有

$$
\begin{array} { r l r l } { { 1 } x _ { 1 } + 1 x _ { 2 } } & { { } } & { } & { { } = 3 } \\ { - 2 x _ { 2 } } & { { } } & { } & { { } = 1 2 } \\ { 2 x _ { 3 } } & { { } } & { } & { { } = 6 } \\ { 2 x _ { 4 } } & { { } } & { } & { { } = 4 } \end{array} ,
$$

同样,消去 $x _ { 2 }$ ,最后将欲求解的上三角方程化成了如下形式的对角方程：

$$
\begin{array} { r l r l } { { 1 } x _ { 1 } } & { { } } & { } & { { } = 9 } \\ { - 2 x _ { 2 } } & { { } } & { } & { { } = 1 2 } \\ { 2 x _ { 3 } } & { { } } & { } & { { } = 6 } \\ { 2 x _ { 4 } } & { { } } & { = 4 } \end{array}
$$

易知 $x _ { 1 } = 9$

一个回代法(Back Substituting)求解上三角方程组的顺序算法如算法10.1。

算法10.1 SISD上回代求解上三角方程组算法

输入： $\mathbf { A } _ { n \times n } , \mathbf { \boldsymbol { b } } = [ b _ { 1 } , \cdots , b _ { n } ] ^ { \mathrm { T } }$ 输出： $\pmb { x } = [ \pmb { x } _ { 1 } , \cdots , \pmb { x } _ { n } ] ^ { \top }$

Begin

$$
x _ { i } = b _ { i } / a _ { i i }
$$

$$
\begin{array} { l } { b _ { j } = b _ { j } - a _ { j i } x _ { i } } \\ { a _ { j i } = 0 . } \end{array}
$$

# end for

end for

End

显然,算法10.1的复杂度为 $O ( n ^ { 2 } )$ 。

如果分析一下算法10.1,则知算法的(1.2)步,即j循环是可以并行化的，于是有如下UMA上回代求解上三角方程组的并行算法10.2。

UMA上回代解法 UMA是一种共享存储的 MIMD多处理机计算模型,其中所有处理器通过互连机制均匀一致地访问共享存储器。

算法10.2UMA上回代求解上三角方程组算法   
输入： $\mathbf { A } _ { n \times n } , \pmb { b } = \smash { \left[ b _ { 1 } , \cdots , b _ { n } \right] ^ { \mathrm { T } } }$   
输出： $\mathbf { X } = [ \mathbf { \Psi } _ { X _ { 1 } } , \cdots , \mathbf { \Psi } _ { X _ { n } } ] ^ { \mathrm { { T } } }$   
Begin for ${ \bf { \ell } } _ { i } = n$ to 1 do $x _ { i } = b _ { i } / a _ { i i }$ for all $\mathbf { P } _ { j }$ ,where $1 { \leqslant } j { \leqslant } p$ do $\times ~ { \pmb { p } }$ 为处理器数 $\yen 7$ for $k = j$ to ${ \bf \chi } _ { i } - 1$ step $\pmb { \hat { p } }$ do $\begin{array} { l } { b _ { k } = b _ { k } - a _ { k i } x _ { i } } \\ { a _ { k i } = 0 } \end{array}$ endfor endfor all endfor   
End

显然,算法10.2之复杂度为 $\boldsymbol { \hat { p } } \left( \boldsymbol { n } \right) = \boldsymbol { \hat { p } } , t \left( \boldsymbol { n } \right) = \boldsymbol { O } \left( \boldsymbol { n } \right)$ 。

# 10.2三对角方程组的求解

本节打算介绍两种求解三对角方程组的方法：直接求解法，适合于在串行机上执行,但不适合并行化;奇偶归约求解法,虽有较高的比例常数,但易于并行化。

# 10.2.1 三对角方程组直接求解法

例示直接求解方法三对角方程组中的系数矩阵，除了三条对角线上的元素为非零外，其余元素均为零,但通常没有只含一个变量的方程，因此不能用上节解上三角方程组的办法对它进行求解，为此需进行一些变换。先看一个具体例子。假定欲求解以下三对角方程组：

$$
\begin{array} { r c l } { { } } & { { } } & { { 1 6 x _ { 1 } + ~ 4 x _ { 2 } } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { 4 x _ { 1 } + 1 1 x _ { 2 } - ~ 5 x _ { 3 } } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { 2 x _ { 2 } + 1 4 x _ { 3 } - ~ 6 x _ { 4 } } } \\ { { } } & { { } } & { { ~ 5 x _ { 3 } + 1 8 x _ { 4 } } } \end{array}
$$

$$
\begin{array} { r l } { { \mathbf { \Omega } } } & { { } = 8 \qquad { \mathbb { O } } } \\ { { \mathbf { \Omega } } } & { { } = 7 \qquad { \mathbb { O } } } \\ { { \mathbf { \Omega } } } & { { } = 1 3 \qquad { \mathbb { O } } } \\ { { \mathbf { \Omega } } } & { { } = 2 4 \qquad { \mathbb { O } } } \end{array}
$$

首先， $\textcircled { 2 } - \frac { 1 } { 4 } \textcircled { 1 }$ ，消去第 $\textcircled{2}$ 个方程中的 $\pmb { x _ { 1 } }$

$$
\begin{array} { c } { 1 6 x _ { 1 } + 4 x _ { 2 } } \\ { 1 0 x _ { 2 } - 5 x _ { 3 } } \end{array}
$$

然后， $\textcircled { 3 } - \frac { 1 } { 5 } \textcircled { 2 }$ ，消去第 $\textcircled{3}$ 个方程中的 $x _ { 2 }$ ：

$$
\begin{array} { c } { { \ S x _ { 1 } + 4 x _ { 2 } } } \\ { { \ O } } \\ { { 1 0 x _ { 2 } - 5 x _ { 3 } } } \\ { { \ O } } \\ { { 1 5 x _ { 3 } - \ O 6 x _ { 4 } } } \\ { { \ O } } \\ { { \ S x _ { 3 } + 1 8 x _ { 4 } } } \end{array}
$$

$$
\begin{array} { r l } { { \mathbf { \Omega } } } & { { } \quad \mathbb { 0 } } \\ { { \mathbf { \Omega } } } & { { } = { \mathbf { 5 } } } \\ { { \mathbf { \Omega } } } & { { } \quad \mathbb { 2 } } \\ { { \mathbf { \Omega } } } & { { } \quad \mathbb { 3 } } \\ { { \mathbf { \Omega } } } & { { } \quad \mathbb { 4 } } \end{array} \qquad { \begin{array} { r l } { { \mathbb { D } } } & { { } } & { { \mathbb { 1 } } } \\ { { \mathbb { 2 } } } & { { } } \\ { { \mathbb { 3 } } } & { { } } \\ { { \mathbb { 2 } } } & { { } } \end{array} }
$$

最后， $\textcircled { 4 } - \frac { 1 } { 3 } \textcircled { 3 }$ ，消去第 $\textcircled{4}$ 个方程中的 $\pmb { x } _ { 3 }$ ：

$$
\begin{array} { c } { 1 6 x _ { 1 } + 4 x _ { 2 } } \\ { 1 0 x _ { 2 } - 5 x _ { 3 } } \\ { 1 5 x _ { 3 } - 6 x _ { 4 } } \\ { 2 0 x _ { 4 } } \end{array}
$$

$$
\begin{array} { l } { { \mathbf { \eta } } } \\ { { \mathbf { \eta } } } \\ { { \mathbf { \eta } } } \\ { { \mathbf { \eta } } } \\ { { \mathbf { \eta } } } \\ { { \mathbf { \eta } } } \end{array} \Vdash \mathbf { 1 } 2
$$

此时三对角方程组的最后一个方程只含一个变量,这样就可以用回代法直接求解了。

三对角方程组的一般形式在正式给出 SISD上求解三对角方程组的算法之前，先考虑三对角方程组的一般形式。注意，在三对角方程组中，第一个和最后一个方程中只含有两个变量，其余均有三个变量，于是可以将三对角方程组一般化表示如下：

$$
\begin{array} { r l r } { g _ { 1 } x _ { 1 } + h _ { 1 } x _ { 2 } } & { = b _ { 1 } } \\ { f _ { i } x _ { i - 1 } + g _ { i } x _ { i } + h _ { i } x _ { i + 1 } } & { = b _ { i } } & { , 2 \leqslant i \leqslant n - 1 } \\ { f _ { n } x _ { n - 1 } + g _ { n } x _ { n } } & { = b _ { n } } \end{array}
$$

SISD上直接求解法一个直接求解三对角方程组的顺序算法如算法10.3。

算法10.3 SISD上直接求解三对角方程组算法

输入： $\mathbf { \delta } _ { { \pmb { A } } _ { n } \times { \pmb { n } } } , { \pmb { b } } = [ b _ { 1 } , \cdots , b _ { n } ] ^ { \mathbb { T } }$ 输出： $\mathbf { \pmb { x } } = [ \mathbf { \mathscr { x } } _ { 1 } , \cdots , \mathbf { \mathscr { x } } _ { n } ] ^ { \mathsf { T } }$

Begin

(1） for ${ \dot { \pmb { \imath } } } = { \boldsymbol { 1 } }$ to $\pmb { n } - 1$ do$\begin{array} { r } { { g _ { i + 1 } } = { g _ { i + 1 } } - ( { f _ { i + 1 } } / { g _ { i } } ) { h _ { i } } } \\ { \smash { { b _ { i + 1 } } = { b _ { i + 1 } } - ( { f _ { i + 1 } } / { g _ { i } } ) { b _ { i } } } } \end{array}$

end for

(2） for $i = n$ to 2 do

$$
x _ { i } = b _ { i } / g _ { i }
$$

$$
b _ { i - 1 } = b _ { i - 1 } - x _ { i } h _ { i - 1 }
$$

# end for

End

显然,算法10.3的复杂度为 $O ( n )$

并行化分析仔细分析算法10.3,并参照上述具体例子可知,算法第(1)步,每次循环计算 $\pmb { g }$ 与 $^ { b }$ 时会用到前次循环计算的结果，所以此循环不能并行执行。同样,算法第(2)步,由于回代计算的顺序性,所以该循环也不能并行执行。因此,为了并行化必须另寻途径。

# 10.2.2三对角方程组奇偶归约求解法

奇偶归约法原理首先将(10.2)式所示的三对角方程组改写成如下的一个通式：

$$
f _ { i } x _ { i - 1 } + g _ { i } x _ { i } + h _ { i } x _ { i + 1 } = b _ { i } \quad , \quad 1 \leqslant i \leqslant n
$$

$$
f _ { 1 } = h _ { n } = 0
$$

然后奇偶归约法求解三对角方程组分成两步：第一步消去偶序号方程组中具有奇下标的 $\pmb { x _ { i } }$ 变量;第二步回代求解。消去 $\pmb { x } _ { 2 i - 1 }$ 和 $\pmb { x } _ { 2 i + 1 }$ 的方法可描述如下：

$$
\begin{array} { r l r } { \phantom { \frac { 1 } { 2 } } f _ { 2 i - 1 } x _ { 2 i - 2 } + g _ { 2 i - 1 } x _ { 2 i - 1 } + h _ { 2 i - 1 } x _ { 2 i } } & { = b _ { 2 i - 1 } } \\ { f _ { 2 i } x _ { 2 i - 1 } + g _ { 2 i } x _ { 2 i } + h _ { 2 i } x _ { 2 i + 1 } } & { = b _ { 2 i } } \\ { f _ { 2 i + 1 } x _ { 2 i } + g _ { 2 i + 1 } x _ { 2 i + 1 } + h _ { 2 i + 1 } x _ { 2 i + 2 } = b _ { 2 i + 1 } } \end{array}
$$

第一式乘以 $- f _ { 2 i } g _ { 2 i } ^ { - 1 } -$ 1后加到中间一式；第三式乘以 $- h _ { 2 i } g _ { 2 i } ^ { - 1 } +$ 后亦加到中间-式,这样中间一式就变为：

$$
\begin{array} { r l } & { - f _ { 2 i } g _ { 2 i - 1 } ^ { - 1 } f _ { 2 i - 1 } x _ { 2 i - 2 } + ( g _ { 2 i } - f _ { 2 i } g _ { 2 i - 1 } ^ { - 1 } h _ { 2 i - 1 } - h _ { 2 i } g _ { 2 i + 1 } ^ { - 1 } f _ { 2 i + 1 } ) x _ { 2 i } } \\ & { \qquad - h _ { 2 i } g _ { 2 i + 1 } ^ { - 1 } h _ { 2 i + 1 } x _ { 2 i + 2 } = b _ { 2 i } - f _ { 2 i } g _ { 2 i - 1 } ^ { - 1 } b _ { 2 i - 1 } - h _ { 2 i } g _ { 2 i + 1 } ^ { - 1 } b _ { 2 i + 1 } } \\ & { \qquad i = 1 , 2 , \cdots , \lfloor { n / 2 } \rfloor } \end{array}
$$

方程组(10.5)中只含偶下标的 $_ { \pmb { x } }$ 变量,它消去了原方程组(10.3)式中含奇下标的x变量,该方程仍然是一个三对角方程组，但变量少了一半。重复上述过程可使方程组的变量越来越少，最后只剩下二个或三个方程：

$$
\begin{array} { r } { g _ { 1 } x _ { 1 } + h _ { 1 } x _ { 2 } = b _ { 1 } } \\ { f _ { 2 } x _ { 1 } + g _ { 2 } x _ { 2 } = b _ { 2 } } \end{array}
$$

或

$$
\begin{array} { r l r } & { } & { \quad g _ { 1 } x _ { 1 } + h _ { 1 } x _ { 2 } \qquad = b _ { 1 } } \\ & { } & { f _ { 2 } x _ { 1 } + g _ { 2 } x _ { 2 } + h _ { 2 } x _ { 3 } = b _ { 2 } } \\ & { } & { f _ { 3 } x _ { 2 } + g _ { 3 } x _ { 3 } = b _ { 3 } } \end{array}
$$

从最后的方程组就可解得x1、x2或x1、x2、x30

一旦求出了上述 $_ { x }$ 的值,就可以开始回代,即将 $\boldsymbol { x } _ { 2 i - 2 } \ 、 \boldsymbol { x } _ { 2 i } \ 、 \boldsymbol { x } _ { 2 i + 2 }$ 代人(10.4)式即可解得 $x _ { 2 i - 1 }$ 和 $x _ { 2 i + 1 }$ 。此过程一直进行到解出了原方程组的所有变量为止。

SISD上奇偶归约法求解法习题10.1给出了一种 SISD上用奇偶归约法(Odd-Even Reduction)求解三对角方程组的算法形式描述。建议读者认真分析此算法，最好在计算机上编程实现它。

并行化分析根据上述求解原理可知,在第一步消元时可同时消去具有奇下标的 $_ { x }$ 变量，所以该步可直接并行化;同样，在回代时奇下标的变量亦可同时求解,所以也可直接并行化。

最后,如果对于所有的 $\dot { \pmb { \imath } }$ ，满足 $\mid _ { g _ { i } } \mid \geqslant \mid _ { f _ { i } } \mid + \mid h _ { i } \mid$ (即对角占优),则消去奇下标变量后的方程组仍具有对角占优的性质。所以只要三对角方程组是对角占优的,奇偶归约法就可使用(见习题10.2)。

# 10.3稠密线性方程组的求解

求解稠密线性方程组的经典数值方法有直接三角分解法(即LU分解法),正交三角分解法(即QR分解法)和蝶形分解法(即WZ分解法)。本节介绍最基本的求解稠密线性方程组的高斯消去法(Gaussian Elimination)。

# 10.3.1 有回代的高斯消去法

基本原理高斯消去法求解 $\mathbf { A } \mathbf { \boldsymbol { x } } = \mathbf { \boldsymbol { b } }$ 的基本思想是,将稠密系数矩阵 $\pmb { A }$ 化为上三角阵 $\pmb { T }$ ，然后对 $\pmb { T x } = \pmb { c }$ 施行回代求解。参照图10.1,在消元的过程中,在第i步时为了消去第i列的第i+1行到第n行中的元素(即化非零元素为零)，可以用行 $_ i$ 的倍数与其余行(第 $i + 1$ 行到第 $\pmb { n }$ 行)相减而达到目的。

![](images/688251f14221f4b666352468554c5c7eb1ffe4685a29b7589085b8b90e68f08c.jpg)  
图10.1高斯消去法过程

选主元的高斯消去法为了确保数值解的稳定性，在第 $\textbf { \em i }$ 步时,应先找第 $_ i$ 列中第 $\pmb { i }$ 行到第 $\pmb { n }$ 行中绝对值最大的元素，此元素称之为主元(Pivot)；再将此元素所在的行(称为主元行)与第 $_ i$ 行施行交换。由于交换系数矩阵的两行只相当于交换两方程的位置,所以不影响求解结果。在实际执行中，每次迭代时并不真正交换主元行与第 $\pmb { i }$ 行,而是引人一些参量，指明迭代时是否某一特定行已被选作主元行等就可以了。

SISD上高斯主元消去法一个有回代的、采用选主元的求解稠密线性方程组的高斯消去顺序算法如算法10.4。其中,marked $\pmb { 1 } : \pmb { n }$ ，指明哪些行已选作主元行;pivot $\mathbf { 1 } : \pmb { n } ^ { \prime }$ 指明行 $\textbf { \em i }$ 被用作主元行的迭代步数;picked指明选作主元行的行。

# 算法10.4SISD上求解稠密线性方程组高斯主元消去算法

输入： $\mathbf { A } _ { n } \times _ { n } , \mathbf { \boldsymbol { b } } = \{ b _ { 1 } , \cdots , b _ { n } \} ^ { \mathbf { T } }$ 输出： $\mathbf { \Psi } \mathbf { x } = [ \mathbf { \Psi } _ { x _ { 1 } } , \cdots , \mathbf { \Psi } _ { x _ { n } } ] ^ { \mathrm { T } }$

# Begin

(1) for ${ \bf \nabla } _ { i } = 1$ to $\pmb { n }$ do $\mathbf { m a r k e d } _ { i } = 0$ end for

(2) for ${ i } = 1$ to $\pmb { n } - \pmb { 1 }$ do (2.1) $\mathbf { \ t e m p { = } 0 }$ (2.2) for $j = 1$ to $\pmb { n }$ do i $\mathbf { i f } \ \mathbf { m a r k e d } _ { j } = 0$ and $| a _ { j i } | >$ temp then $\mathrm { t e m p } = \left| \boldsymbol { a } _ { j i } \right|$ $\operatorname { p i c k e d } = j$ endif endfor (2.4) (2.3) $\begin{array} { l } { \mathrm { m a r k e d } _ { \mathrm { \ p i c k e d } } = 1 } \\ { \mathrm { p i v o t } _ { \mathrm { \ p i c k e d } } = i } \end{array}$ (2.5) for $j = 1$ to $\pmb { n }$ do $\mathbf { i f } \ m a r \mathbf { k e d } _ { j } = 0$ then (i)temp= aji /a picked,i (ii)for $k = i + 1$ to $\pmb { n }$ do $a _ { j k } = a _ { j k } - a _ { \mathrm { p i c k e d } , k } \star \mathrm { t e m p }$ endfor $( \mathrm { i i i } ) b _ { j } = b _ { j } - b _ { k } \star \mathrm { t e m p } \ .$

# endif

# endfor

end for (3) for $i = 1$ to $\pmb { n }$ do if marked $\mathbf { \epsilon } _ { i } = 0$ then $\mathrm { p i v o t } _ { i } = n$ break end if end for

End

显然,算法10.4的复杂度为 $O ( n ^ { 3 } )$ 。

并行化分析根据算法10.4可知，一旦主元行选定,所有非主元行的修改可同时进行,也就是说算法(2.5)步和(ii)步的中层的 $j$ 循环和最内层的 $k$ 循环可并行化。下面将讨论超立方连接的多计算机上如何执行高斯主元消去法。为此必须研究每次迭代时的数据相关性以便选择适当的处理器分配。如图10.2所示,在第 $\mathbf { \chi } _ { i }$ 次迭代确定主元行时,要求比较 $_ i$ 列中的各数据;而一旦主元行确定，未被选中的行 $\pmb { j }$ 中的每个元素 $a _ { j k }$ 在更新时要用到 $a _ { j i } \setminus a _ { \mathrm { p i c k e d } , }$ i和 $\alpha _ { \mathrm { p i c k e d } , k ^ { \circ } }$ 显然， $\pmb { \alpha }$ 和 $^ b$ 的分配直接影响着通信要求。

![](images/a298a5419005094bbabbff8882e74ac0cd03bd9de09b1c0b3b67dd8ddb54d601.jpg)  
图10.2高斯消去法单步迭代时的数据相关性

超立方多计算机上高斯主元消去法假定采用按行划分法分配处理器，具体实现方法如算法10.5。其中,marked1:n/p指明哪些行已是主元行,pivot1:n/p指明迭代步数;value表示主元值;winner 是控制主元行的处理器。

算法10.5超立方多计算机上求解稠密线性方程组高斯主元消去算法

输入： $\mathbf { A } _ { n \times n } , \pmb { b } = [ b _ { 1 } , \cdots , b _ { n } ] ^ { \mathrm { T } }$ 输出： $\pmb { x } = [ \pmb { x } _ { 1 } , \cdots , \pmb { x } _ { n } ] ^ { \mathrm { T } }$

Begin

forall $\mathrm { \bf P } _ { i d }$ ，where $1 \leqslant i d \leqslant p$ do

(1）for ${ \bf \nabla } _ { i } = 1$ to $\scriptstyle { n / p }$ do $\nearrow$ 初始化；开始时所有行均非主元行 $\bigstar$ / $\mathbf { m a r k e d } _ { i } = 0$ end for

(2）for $i = 1$ to $\pmb { n } - 1$ do $\big / \big \varkappa$ 各处理器找主元候选者 $\yen 7$ (2.1) value ${ \bf \delta } = { \bf 0 }$ (2.2) for $j = 1$ to $n / \phi$ do $\begin{array} { r l } & { \mathrm { i f ~ } \operatorname* { m a r k e d } _ { j } = 0 \ \& \mid a _ { j i } \mid > \mathrm { v a l u e ~ t h e n } } \\ & { \mathrm { v a l u e } = \mid a _ { j i } \mid } \\ & { \mathrm { p i c k e d } = j } \end{array}$ end if end for

(2.3）winner $\mathbf { \mu } =$ id $\big / \big \varkappa$ 标记控制主元行的处理器 $\yen 7$ (2.4）MAX.TOURNAMENT (id,value,winner） $\big / . *$ 调用MAX

# 选全局最大主元 $\yen 7$

(2.5) if $i d \equiv$ winner then

(i) $\mathbf { m a r k e d } _ { \mathrm { p i c k e d } } = 1$   
(ii) $\mathbf { p i v o t } _ { \mathrm { p i c k e d } } = i$   
(iii） for $j = i$ to $\pmb { n }$ do temp.vector; = a picked,j end for   
${ \big ( } \mathrm { i } \mathbf { v } { \big ) } \ \mathrm { t e m p . } \mathbf { v e c t o r } _ { n + 1 } = b _ { \mathrm { p i c k e d } }$   
endif

(2.6） HC. BROADCAST( $\Dot { \pmb { \imath } } d$ , winner,temp. vector; $\tan + 1$ ） $\nearrow$ 主元处理器播送主元给其它处理器 $\yen 7$ (2.7) for $j = 1$ to $\pmb { n } / \pmb { \mathscr { p } }$ do $\big / \big \varkappa$ 未选中的行中消去列 $_ i$ 之元素 $\yen 7$

if marked; $\mathbf { \mu } = \mathbf { 0 }$ then  
(i) $\scriptstyle { \mathrm { t e m p } } = a _ { j i } / { \mathrm { t e m p } } . { \mathrm { v e c t o r } } _ { i }$   
(ii） for $k = i + 1$ to $\pmb { n }$ do$a _ { j k } = a _ { j k } - \mathrm { t e m p . } \mathrm { v e c t o r } _ { k } \times \mathrm { t e m p }$ end for

(iii) b;= b; - temp.vectorn+1 × temp

#

enai end for endfor (3）for $i = 1$ to $\pmb { n } / \pmb { \mathscr { p } }$ do $\big / \ast$ 定位从未被用作主元行的行 $\pmb { \mathscr { k } }$ / if marked ${ \bf \nabla } _ { i } = { \bf 0 }$ then $\mathsf { p i v o t } _ { i } = n$ break end if end for end for End MAX.TOURNAMENT( id ,value',winner) $\curvearrowright$ 被主程序所调用的过程 $\pmb { \mathscr { R } }$ / Reference:id,value',winner 局部变量:temp.value',temp.winner begin for $\mathbf { \nabla } _ { i } = \mathbf { 0 }$ to log ${ \pmb { \hat { p } } } - 1$ do （1）partner $= i d \oplus 2 ^ { i }$ (2）[partner]temp.value $\twoheadleftarrow$ value' (3）[partner]temp.winner $\twoheadleftarrow$ winner (4) if temp.value' $>$ value' then value' $\eqcirc$ temp. value' winner $\asymp$ temp. winner endif end for end

# 10.3.2无回代的高斯-约旦法

基本原理无回代的高斯－约旦法与有回代的高斯消去法基本思想一样，区别是，后者通过一系列的消元,最终使系数矩阵变成一个上三角阵，然后由第$\pmb { n }$ 个方程先解出 $x _ { n }$ ,令其代人第 $\dot { n } - 1$ 个方程解出 ${ \pmb x _ { n } } - { \pmb 1 }$ ,如此一直回代下去,最后由第一个方程解出 $x _ { 1 }$ ；而前者通过一系列消元,最终使系数矩阵变成一个对角阵,然后直接由第 $\textbf { \em i }$ 个方程解出 $x _ { i } ( i = 1 , 2 , \cdots , n )$ 。

下面以 $ \pmb { n = 4 }$ 为例来说明无回代的主元消去法的具体消元过程(为方便计算,令 $b _ { i }$ 改写成 $a _ { i } , _ { n + 1 } )$ ：

$\textcircled{1}$ 在系数矩阵中找绝对值最大者(主元),假定为 $\pmb { a } _ { 1 1 }$ ;将第一个方程乘以$- \ a _ { i 1 } / a _ { 1 1 }$ ,分别与第 $\textbf { \em i }$ 个方程相加 $( \mathbf { \it _ i } = 2 , 3 , 4 )$ ,于是有：

$$
\left( \begin{array} { c c c c } { { a _ { 1 1 } } } & { { a _ { 1 2 } } } & { { a _ { 1 3 } } } & { { a _ { 1 4 } } } \\ { { 0 } } & { { b _ { 2 2 } } } & { { b _ { 2 3 } } } & { { b _ { 2 4 } } } \\ { { 0 } } & { { b _ { 3 2 } } } & { { b _ { 3 3 } } } & { { b _ { 3 4 } } } \\ { { 0 } } & { { b _ { 4 2 } } } & { { b _ { 4 3 } } } & { { b _ { 4 4 } } } \end{array} \right) \left[ \begin{array} { c } { { x _ { 1 } } } \\ { { x _ { 2 } } } \\ { { x _ { 3 } } } \\ { { x _ { 4 } } } \end{array} \right] = \left[ \begin{array} { c } { { \alpha _ { 1 5 } } } \\ { { b _ { 2 5 } } } \\ { { b _ { 3 5 } } } \\ { { b _ { 4 5 } } } \end{array} \right]
$$

$\textcircled{2}$ 除去第一行,在剩下的系数矩阵中再找主元,假定为 $\pmb { b } _ { 2 2 }$ ;将第二个方程乘以 $- \ b _ { i 2 } / b _ { 2 2 }$ ,分别与第 $\textbf { \em i }$ 个方程相加 $( \mathbf { \zeta } _ { i } = 1 , 3 , 4 )$ ,于是有：

$$
\begin{array} { r } { \left\{ \begin{array} { c c c c } { \boxed { a _ { 1 1 } } } & { 0 } & { c _ { 1 3 } } & { c _ { 1 4 } } \\ { 0 } & { \boxed { b _ { 2 2 } } } & { b _ { 2 3 } } & { b _ { 2 4 } } \\ { 0 } & { 0 } & { c _ { 3 3 } } & { c _ { 3 4 } } \\ { 0 } & { 0 } & { c _ { 4 3 } } & { c _ { 4 4 } } \end{array} \right\} \left\{ \begin{array} { c } { x _ { 1 } } \\ { x _ { 2 } } \\ { x _ { 3 } } \\ { x _ { 4 } } \end{array} \right\} = \left\{ \begin{array} { c } { c _ { 1 5 } } \\ { b _ { 2 5 } } \\ { c _ { 3 5 } } \\ { c _ { 4 5 } } \end{array} \right\} } \end{array}
$$

$\textcircled{3}$ 重复之，最后得到的线性方程组为：

$$
\left\{ \begin{array} { c c c c } { { \boxed { \alpha _ { 1 1 } } } } & { { 0 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { \boxed { \hat { b } _ { 2 2 } } } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { \boxed { c _ { 3 3 } } } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { \boxed { d _ { 4 4 } } } } \end{array} \right\} \left\{ \begin{array} { c } { { x _ { 1 } } } \\ { { x _ { 2 } } } \\ { { x _ { 3 } } } \\ { { x _ { 4 } } } \end{array} \right\} = \left\{ \begin{array} { c } { { e _ { 1 5 } } } \\ { { e _ { 2 5 } } } \\ { { e _ { 3 5 } } } \\ { { d _ { 4 5 } } } \end{array} \right\}
$$

由此可直接解出 $x _ { 1 } = e _ { 1 5 } / \alpha _ { 1 1 } , x _ { 2 } = e _ { 2 5 } / b _ { 2 2 } , x _ { 3 } = e _ { 3 5 } / c _ { 3 3 }$ 和 $x _ { 4 } = d _ { 4 5 } / d _ { 4 4 }$ SISD上高斯-约旦主元消去法根据上述无回代求解稠密线性方程组的方法,参照算法10.4,读者不难写出 SISD上求解稠密线性方程组的高斯－约旦主元消去法的算法的形式描述,这作为习题留给读者去完成(习题10.6)。

PRAM上高斯-约旦消去法根据以上的讨论可知，一旦主元行选定后，消元的操作则可同时进行。选主元的方法和10.3.1节一样,所以下面算法10.6中，为了突出主题,选主元行部分并未示出，但读者可以参照算法10.5将它们补上。下面算法中假定使用 ${ n ^ { 2 } + n }$ 个处理器,并排成 $\pmb { n } \times \left( \pmb { n } + 1 \right)$ 的阵列。

算法10.6 PRAM上求解稠密线性方程组高斯-约旦消去算法输入： $\mathbf { A } _ { n } \times \mathbf { \mathit { \Pi } } _ { n } , \mathbf { \mathit { b } } = [ \mathbf { \mathit { b } } _ { 1 } , \cdots , \mathbf { \mathit { b } } _ { n } ] ^ { \mathrm { T } }$ 输出： ${ \pmb x } = [ { \pmb x } _ { 1 } , \cdots , { \pmb x } _ { n } ] ^ { \hat { \operatorname { T } } }$

Begin

(1）for $j = 1$ to $\pmb { n }$ do for $_ { i } = 1$ to $\pmb { n }$ par -do

for $k = j$ to n + 1 par - do if $i { \neq } j$ then $\alpha _ { i k } = \alpha _ { i k } - ( \alpha _ { i j } / \alpha _ { j j } ) \alpha _ { j k }$ end if end for end for end for (2） for $i = 1$ to $\pmb { n }$ par-do $x _ { i } = a _ { i , n + 1 } / a _ { i i }$ end for

End

注意此算法有可能多于一个处理器同时读取 $\alpha _ { i j } \setminus \alpha _ { j j }$ 和 $\alpha _ { j k }$ ,所以此PRAM应是 CREW的。

显然,算法的时间为 $O ( n )$ ，用了 $O ( n ^ { 2 } )$ 个处理器。

# 10.3.3 迭代求解的高斯-赛德尔法

基本原理 高斯-赛德尔求解线性方程组的方法,实际上是迭代(近似求解)法,不仅稠密线性系适用,而且稀疏线性系也适用。

在求解 $\mathbf { A } \mathbf { x } = \mathbf { b }$ 时,可以将系数矩阵 $\pmb { A }$ 分解为 $\pmb { A } = \pmb { E } + \pmb { D } + \pmb { F }$ ,其中 $\pmb { D } \cdot \pmb { E } \cdot \pmb { F }$ 均为 $\mathbf { \Omega } _ { n } \times \mathbf { \Omega } _ { n }$ 的矩阵,具体定义如下：

$$
d _ { i j } = { \left\{ \begin{array} { l l } { a _ { i j } ~ , ~ i = j } \\ { 0 ~ , ~ \operatorname { \circledast } { \mathbb { H } } } \end{array} \right. } e _ { i j } = { \left\{ \begin{array} { l l } { a _ { i j } ~ , ~ i > j } \\ { 0 ~ , ~ \operatorname { \circledast } { \mathbb { H } } } \end{array} \right. } f _ { i j } = { \left\{ \begin{array} { l l } { a _ { i j } ~ , ~ i < j } \\ { 0 ~ , ~ \operatorname { \circledast } { \mathbb { H } } } \end{array} \right. }
$$

这样， $A x = \left( D + E + F \right) x = b$ 可变换成 $\pmb { D x } = \pmb { b } - \pmb { E x } - \pmb { F x }$ 。如果给定初始解 ${ \pmb x } ( { \bf 0 } )$ ，则第 $k$ 次迭代可计算如下：

$$
\pmb { D } \pmb { x } \left( \pmb { k } \right) = \pmb { b } - \pmb { E } \pmb { x } \left( \pmb { k } \right) - \pmb { F } \pmb { x } \left( \pmb { k } - \pmb { 1 } \right)
$$

例如， $^ { n = 4 , k = 1 }$ 时，

$$
\alpha _ { 1 1 } x _ { 1 } ( 1 ) = b _ { 1 } - 0 - \big ( \alpha _ { 1 2 } x _ { 2 } ( 0 ) + \alpha _ { 1 3 } x _ { 3 } ( 0 ) + \alpha _ { 1 4 } x _ { 4 } ( 0 ) \big )
$$

$$
\alpha _ { 2 2 } x _ { 2 } ( 1 ) = b _ { 2 } - \left( \alpha _ { 2 1 } x _ { 1 } ( 1 ) - \left( \alpha _ { 2 3 } x _ { 3 } ( 0 ) + \alpha _ { 2 4 } x _ { 4 } ( 0 ) \right) \right.
$$

$$
\alpha _ { 3 3 } x _ { 3 } \big ( 1 \big ) = b _ { 3 } - \big ( \alpha _ { 3 1 } x _ { 1 } \big ( 1 \big ) + \alpha _ { 3 2 } x _ { 2 } \big ( 1 \big ) \big ) - \alpha _ { 3 4 } x _ { 4 } \big ( 0 \big )
$$

$$
\alpha _ { 4 4 } x _ { 4 } ( 1 ) = b _ { 4 } - \left( \alpha _ { 4 1 } x _ { 1 } ( 1 ) + \alpha _ { 4 2 } x _ { 2 } ( 1 ) + \alpha _ { 4 3 } x _ { 3 } ( 1 ) \right) - 0
$$

对于某一k和给定的误差允许值,如果下式成立，则认为迭代是收敛的：

$$
\operatorname* { m a x } _ { i = 1 } ^ { n } |  x _ { i } ( k + 1 ) - { x _ { i } } ( k ) | < \varepsilon
$$

(10.6）式能够加快顺序计算速度,因为当依次计算 ${ \pmb x } _ { 1 } , { \pmb x } _ { 2 }$ ,…时,第 $k$ 次迭代的

$x _ { i } ( k )$ 值,一部分可用上次迭代的值(相应于上三角部分),而一部分可用本次迭代的值(相应于下三角部分）。

SISD上高斯-赛德尔迭代法注意(10.6)式可以展开为如下形式：

$$
x _ { i } ( k ) = ( b _ { i } - \sum _ { j = 1 } ^ { i - 1 } a _ { i j } x _ { j } ( k ) - \sum _ { j = i + 1 } ^ { n } a _ { i j } x _ { j } ( k - 1 ) ) / a _ { i i } \quad , \quad i = 1 , \cdots , n
$$

按照(10.7)式可直接导出如下顺序算法 $1 0 . 7 _ { \circ }$

算法10.7 SISD上求解线性方程组高斯-赛德尔迭代算法

输入： $\mathbf { A } _ { n \times n } , \pmb { b } = [ b _ { 1 } , \cdots , b _ { n } ] ^ { \mathrm { T } }$ ，精度 $\varepsilon$

输出： ${ \pmb x } = [ { \pmb x } _ { 1 } , \cdots , { \pmb x } _ { n } ] ^ { \mathrm { T } }$

Begin

(1) for $i = 1$ to $\pmb { n }$ do

$$
x _ { i } = 0
$$

(2） ${ p / } = \varepsilon + 1$

(3）while $\pmb { \hat { p } } \mathbf { \mathcal { \gtrsim } } \varepsilon$ do (3.1) ${ \pmb \beta } = { \pmb 0 }$ (3.2) for $i = 1$ to $\pmb { n }$ do $\begin{array} { c } { { \left( \mathrm { i } \right) t = x _ { i } } } \\ { { \left( \mathrm { i i } \right) s = 0 } } \end{array}$ (ii)for $j = 1$ to $\pmb { n }$ do if $j \neq i$ then s=s+aixj end if $x _ { i } = ( b _ { i } - s ) / a _ { i i }$ if $| x _ { i } - t | > _ { \hat { P } }$ then $\mathbf { \nabla } _ { \pmb { \phi } } = | \mathbf { \nabla } _ { \mathbf { \mathcal { X } } _ { i } } - \mathbf { \nabla } _ { t } |$ endif end for end for

# end while

End

注意上述算法只有系数矩阵是对角占优的才适用。

并行化分析上述算法无法直接并行化,因为在第k次迭代时,对于j<i

（下三角部分）的 $x _ { i } ( k )$ 的计算必须等待 $x _ { i } ( k )$ 计算好,因而无法并行。有关它的并行化方法，在10.4节讨论稀疏线性方程组的求解时还要进一步讨论。

# 10.4稀疏线性方程组的求解

稀疏线性方程组系指系数矩阵中绝大多数元素均为零的方程组。之所以专门研究它，不仅仅是因为在科学和工程计算问题中会经常遇到它们,而且它们所涉及到的算法和数据结构也比稠密系统要复杂。

绝大多数科学和工程计算问题均代表了由数学模型所表示的一个物理系统。为了适合于计算机求解,连续物理系统的定义域必须离散化，其常用的方法就是将定义域网格化，这样在离散域上求解数学模型，就可在各格点上获得某些所要求的物理量。

通常离散物理域上每个格点的模拟计算，都是基于域上邻近格点的相互作用与影响。典型地,单格点的模拟就会产生一组线性方程。由于每一格点仅与其近邻有关，所以只有邻近格点的变量的系数是非零,而线性方程组的其余系数均为零，因而线性方程组就变成稀疏的了。

注意我们所考虑的稀疏矩阵，是指那些能够利用非零元素的位置与数量有效减少计算时间的稀疏矩阵。

# 10.4.1 稀疏矩阵的存储方式

通常我们用n×n的数组来存放n×n的稠密矩阵,但对稀疏矩阵而言，这种存储方式效率不高。研究有效的稀疏矩阵存储方式,不仅可节省存储单元，而且也可节省计算时间。但存储稀疏矩阵尚无一种通用的最佳的数据结构，不同的数据结构适合于不同的操作变换和不同的并行实现。以下我们仅研究几种最基本常用的稀疏矩阵存储方式。

坐标存储法(Coordinate Storage Scheme） 对于具有q个非零元素的稀疏矩阵,使用坐标存储法存储非零元素时，使用了三个q×1维的数组：值数组VAL和行列下标数组I和J。图10.3示出了6×6稀疏矩阵及其坐标存储法(行列下标编号从1开始，下同)。

缩行存储法(Compressed Row Storage Scheme） 对于具有q 个非零元素的稀疏矩阵，使用压缩稀疏行的办法存储非零元素时，也使用了三个数 组：一 个q×1维的值数组VAL,它按行序分成了n个段；一个q×1维的列下标数组J；一个n×1维的数组I,该数组中的元素指向各段中首元素在稀疏矩阵中的顺序号（只计算非零元素）。图10.4示出了图10.3中的稀疏矩阵使用缩行存储法时的 VAL、J和 $\mathrm { I } _ { \circ }$

![](images/9d82fa3c0de69ca157f68008e641f59092254053a53abd57f8d76192e1974fcb.jpg)  
图10.3 $6 \times 6$ 稀疏矩阵及其坐标存储法

![](images/a53ab289ab4c508b838649c6bdf64209353f8a6e70aef607b4e884bc1257f5cd.jpg)  
图10.4图10.3中稀疏矩阵的缩行存储法

对角存储法(Diagonal Storage Scheme） 对于具有 $\pmb { d }$ 条对角线的 $\mathbf { \mu } _ { n } \times \mathbf { \mu } _ { n }$ 的稀疏矩阵,使用对角存储法时,使用了两个数组：一个 ${ \pmb n } \times { \pmb d }$ 维的值数组VAL,它每一列存储了一条对角线;一个 $d \times 1$ 维的偏移数组(OFFSET),存储各对角线相对于主对角线偏移量。图10.5示出了一个稀疏矩阵及其对角存储方法。

![](images/26d5047180d87e0f5026987a7d9bf1d3fa12e8d7edafe225ce3e614e90dc60c4.jpg)  
图10.5稀疏矩阵的对角存储法

按行存储法(Elpack-Itpack Storage Scheme）对于一个 $\textbf { \em n } \times \textbf { \em n }$ 的稀疏矩阵,假定任意行中最多非零元素数为m，则使用这种存储法时使用了两个数组：一个𝑛×m维的值数组VAL,它每一行包含了稀疏矩阵中相应行中的非零元素;一个𝑛×m 维的数组J,它存储了VAL中相应元素的列号,其中行末的-1是行结束符。图10.6示出了一个稀疏矩阵及其按行存储法。

![](images/bc2b653a5b03a9ffc2999a57e9f102a59d9c94b7da103623ebd225e5cee005c9.jpg)  
图10.6稀疏矩阵的按行存储法

齿对角存储法(Jagged-Diagonal Storage Scheme） 对于具有 $\pmb q$ 个非零元素的稀疏矩阵，使用齿状对角线的形式存储非零元素时,首先将原矩阵按每行中非零元素之数目的降序重新排列之，然后辅之以三个数组：一个 $q \times 1$ 维的值数组VAL,它包含有若干段,每段存储一条齿状对角线；一个 $q \times 1$ 维的数组J,它存储VAL中相应元素的列号;一个 $m \times 1$ 维的数组I( $\mathbf { \nabla } m$ 是任意行中最多非零元素数),该数组之元素是指向各条齿状对角线中首元素依次在所有齿状对角线中的顺序号。图10.7示出了一个稀疏矩阵及其重新调整行序的稀疏矩阵以及它的齿对角存储法。

![](images/f0759fa56ed51d934269673d5ccd5340ccac1af68ea5a33326912f3a0f464d71.jpg)  
图10.7稀疏矩阵的齿对角存储法：(a)原始稀疏矩阵； (b)行重排稀疏矩阵;(c)数组VAL、J和I

# 10.4.2雅可比迭代法

前面10.3.3节已经介绍了线性方程组的迭代求解法。对于求解大型、稀疏线性方程组,迭代法(Iterative Method)是一种最常使用的方法,与直接法相比，它具有方法简单,存储空间小(迭代法通常只对系数矩阵中的非零元素进行运

算)等优点，特别是在有限步内无法得到问题的解时，迭代法就可在有限的迭代步数后，停止运算而得到足够好的近似解。本节先介绍雅可比迭代法，它是一种最简单的线性方程组的迭代解法。

SISD上雅可比迭代法对于求解线性方程组 $\mathbf { A } { \boldsymbol { \mathbf { \mathit { x } } } } = \mathbf { \mathit { b } }$ ,未知向量 $_ { x }$ 的分量可写成如下形式：

$$
x _ { i } = \frac { 1 } { a _ { i i } } \bigg [ b _ { i } - \sum _ { j \neq i } a _ { i j } x _ { j } \bigg ]
$$

雅可比迭代原理是,使用第 $k - 1$ 步所计算的变量 $x _ { i } ( k - 1 )$ ,来计算第 $k$ 步的 $\vert x _ { i } \langle k \rangle$ 之值：

$$
x _ { i } ( k ) = \frac { 1 } { a _ { i i } } \Big ( b _ { i } - \sum _ { j \neq i } a _ { i j } x _ { j } \big ( k - 1 \big ) \Big )
$$

算法10.8给出了串行雅可比迭代算法,注意为了确保该算法总能收敛,要求系数矩阵 $\pmb { A }$ 是对角占优的,即 $\vert a _ { i i } \vert > \sum _ { j \neq i } \mid a _ { i j } \vert$ ， $1 { \leqslant } i { \leqslant } n _ { \leqslant }$

# 算法10.8SISD上求解线性方程组雅可比迭代算法

输入： $\mathbf { A } _ { n } \times \mathbf { \ b _ { n } } , \pmb { b } = [ b _ { 1 } , \cdots , b _ { n } ] ^ { \mathrm { T } } , \varepsilon$ 输出： $\pmb { x } = \{ x _ { 1 } , \cdots , x _ { n } \} ^ { \mathbb { T } }$

# Begin

(1） for $i = 1$ to $_ n$ do $\mathbf { \nabla } \times \mathbf { \nabla } x _ { i }$ 赋初值 $\yen 7$ $x _ { i } = b _ { i } / a _ { i i }$ end for   
(2) $\operatorname { d i f f } = \varepsilon$   
(3）while diff≥ε do (3.1) $\operatorname { d i f f } = 0$ (3.2) for $i = 1$ to $\pmb { n }$ do (i) $\mathrm { n e w } x _ { i } = b _ { i }$ (ii）for $j = 1$ to $\mathbf { n }$ do if $ { j } \neq  { i }$ then $\mathrm { n e w } x _ { i } = \mathrm { n e w } x _ { i } - \alpha _ { i j } x _ { j }$ end if endfor (ii) $\mathrm { n e w } x _ { i } = \mathrm { n e w } x _ { i } / a _ { i i }$ end for (3.3) for $i = 1$ to $_ n$ do

$$
{ \mathrm { d i f f } } = \operatorname* { m a x } \left\{ { \mathrm { d i f f } } , \mid x _ { i } - { \mathrm { n e w } } x _ { i } \mid \right\}
$$

# end for

# end while

End

算法10.8并行化分析雅可比算法很适合于并行化，因为每次迭代均使用上次迭代的值。假定处理器按行分配，即每个处理器负责矩阵的若干行和相应的 $^ b$ 分量，则在while循环时产生两次通信要求：在(3.2)步,每个处理器 $\mathbf { P } _ { i }$ 在计算自己的 $x _ { i } ( k )$ 时,必须用到上次计算出的 $x _ { j } ( k - 1 ) , j \neq i _ { \mathfrak { c } }$ ，为此每个处理器计算出所负责的变量后,必须将其播送给所有其它的处理器;在(3.3)步,每个处理器计算出局部差值diff后,必须从中选取最大者作为下一次迭代的判据,这种求最大值操作是在所有处理器之间的全局操作。

偏微分方程的差分解法试考虑拉普拉斯方程的第一边值问题：

$$
\begin{array} { l } { { \displaystyle { \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } } + { \frac { \partial ^ { 2 } u } { \partial y ^ { 2 } } } = 0 } } \\ { { \displaystyle u \mid _ { s } = \mu ( x , y ) } } \end{array}
$$

其中， $\mu ( x , y )$ 为有界区域 $D$ 的边界 $S$ 上的已知函数。为了求解此偏微分方程，我们可以用差商代替偏导数,得到相应的差分方程,通过解差分方程就可得到偏微分方程的近似解。

试考虑在平面 $( x , y )$ 上一个以S为边界的有界区域 $D$ 上定解问题。为了用差分法求解,可以分别作平行x轴和y轴的直线簇x;=id,y=jd（i,j=0,$1 , \cdots , n ; d$ 为步距),从而构成一个等间距正方网格,而直线的诸交点 $( x _ { i } , y _ { j } )$ 称为格点，记之为 $( i , j )$ 。当 $i , j = 1 , 2 , \cdots , n - 1$ 时的格点称为内格点,在 $S$ 上的格点称为边界格点。所有内格点上，函数 ${ \mathbf { } } u \left( x , y \right)$ 的偏导数可用差商代替：

$$
\frac { \partial u \left( x , y \right) } { \partial x } { \approx } \frac { 1 } { d } \left[ u \left( x _ { i } + d , y _ { j } \right) - u \left( x _ { i } , y _ { j } \right) \right]
$$

$$
\frac { \partial u \left( x , y \right) } { \partial y } { \approx } \frac { 1 } { d } \left[ u \left( x _ { i } , y _ { j } + d \right) - u \left( x _ { i } , y _ { j } \right) \right]
$$

$$
\frac { \partial ^ { 2 } u \left( \boldsymbol { x } , \boldsymbol { y } \right) } { \partial x ^ { 2 } } \approx \frac { 1 } { d ^ { 2 } } \big [ u \left( \boldsymbol { x } _ { i } + d , \boldsymbol { y } _ { j } \right) - 2 u \left( \boldsymbol { x } _ { i } , \boldsymbol { y } _ { j } \right) + u \left( \boldsymbol { x } _ { i } - d , \boldsymbol { y } _ { j } \right) \big ]
$$

$$
\frac { \partial ^ { 2 } u \left( \boldsymbol { x } , \boldsymbol { y } \right) } { \partial \boldsymbol { y } ^ { 2 } } \approx \frac { 1 } { d ^ { 2 } } \big [ u \left( x _ { i } , \boldsymbol { y } _ { j } + d \right) - 2 u \left( x _ { i } , \boldsymbol { y } _ { j } \right) + u \left( x _ { i } , \boldsymbol { y } _ { j } - d \right) \big ]
$$

(10.11)式代人(10.10)式则有：

$$
u \left( x _ { i } , y _ { j } \right) = \frac { 1 } { 4 } \big [ u \left( x _ { i } + d , y _ { j } \right) + u \left( x _ { i } - d , y _ { j } \right) + u \left( x _ { i } , y _ { j } + d \right) + \big ]
$$

$$
u ( x _ { i } , y _ { j } - d ) ]
$$

若格点 $( i , j )$ 处的函数值 $u \left( x _ { i } , y _ { j } \right)$ 记之为 $\boldsymbol { u } _ { i j }$ ,且取 $d = 1$ ,则(10.12)式可简化为：

$$
u _ { i j } = \frac { 1 } { 4 } \left[ u _ { i + 1 , j } + u _ { i - 1 , j } + u _ { i , j + 1 } + u _ { i , j - 1 } \right]
$$

它就是有名的五点格式,即任一格点 $( \mathbf { \omega } _ { i } , \mathbf { \omega } _ { j } )$ 上 $\boldsymbol { u } _ { i j }$ 的值等于周围相邻四格点上解·的值的算术平均。

雅可比算法用于求解稀疏线性方程组当用算法10.8来求解(10.13)式所示的方程组时,效率很低,因为它相应的系数矩阵是稀疏的,每行只有五个非零元素,为此我们设计如下算法10.9来求解它。照例,使用第 $k - 1$ 步所计算的变量来计算第 $\pmb { k }$ 步的变量。

# 算法10.9 SISD上求解拉普拉斯方程雅可比迭代算法

输入：格点数 $\pmb { n }$ ,精度 $\varepsilon$ 输出： ：xi,j

Begin

(1）for $i = 1$ to $\pmb { n }$ do $\big / \ast$ 边界条件 $\bigstar$ / $\begin{array} { r l } & { x _ { 0 , i } = \mathrm { n o r t h } _ { i } } \\ & { x _ { n + 1 } , i = \mathrm { s o u t h } _ { i } } \\ & { x _ { i , 0 } = \mathrm { w e s t } _ { i } } \\ & { x _ { i , n + 1 } = \mathrm { e a s t } _ { i } } \end{array}$ end for

(2) for $i = 1$ to $\pmb { n }$ do $\big / \ast$ 赋初值 $\yen 7$ for $j = 1$ to $\pmb { n }$ do $x _ { i j } = c$ end for end for   
(3） $\operatorname { d i f f } = \varepsilon$   
（4）while diff≥ε do (4.1) $\operatorname { d i f f } = 0$ (4.2) for $i = 1$ to $\pmb { n }$ do for $j = 1$ to $_ { \pmb { n } }$ do $\mathrm { n e w } x _ { i j } = \frac { 1 } { 4 } ( x _ { i - 1 , j } + x _ { i + 1 , j } + x _ { i , j - 1 } + x _ { i , j + 1 } )$ end for

# end for

$$
\begin{array} { r l } & { \mathrm { d i f f } = \operatorname* { m a x } \{ \mathrm { d i f f } , \vert \operatorname { n e w } x _ { i j } - x _ { i j } \vert \} } \\ & { x _ { i j } = \mathrm { n e w } x _ { i j } } \end{array}
$$

# end for

# 'end for

end while

End

算法10.9并行化分析该算法是基于雅可比迭代原理,所有格点之值可同时更新。但在并行更新过程中会产生通信要求：在处理器按行分配时，如图10.8(a)所示，每个处理器负责 $\frac { n } { \pmb { \mathscr { p } } } \times \pmb { \mathscr { n } }$ 个元素，算法(4.2)步每次迭代计算 $\mathtt { n e w } x _ { i j }$ 时，处理器中的阴影区要分别传送 $\pmb { n }$ 个元素给对方的处理器和同时接收来自对方的 $\pmb { n }$ 个元素，令 $\lambda$ 为延迟时间， $\beta$ 为传送每个单值的时间，则每次迭代的通信时间为 $4 ( \lambda + n \beta )$ ;在处理器按块分配时,如图10.8(b)所示,每个处理器负责×个元素，算法执行(4.2)步计算 newxij时,处理器中的阴影区的通信时间为 $8 \left( \lambda + \frac { n } { \sqrt { \lambda } } \beta \right)$ 。同样,不管哪种处理器分配,算法(4.3)步计算全局diff时也会产生通信要求,为了减少此通信时间，可每迭代 $\pmb { k }$ 次才计算一次 diff 的全局值，其中 $k$ 值的大小与计算机的结构和求解问题类型有关。

![](images/2373f7e9a2e80b48443609116d5e29bae21acb2d4024daf8f27d5d11702f2d5a.jpg)  
图10.8处理器的两种划分(a)按行划分 $( \pmb { \phi } = 4 )$ ；(b)按块划分（ $\bf \Pi \cdot \langle \delta 1 6 \rangle$

# 10.4.3 高斯-赛德尔迭代法

基本原理曾在第10.3.3节介绍了求解稠密线性方程组的高斯-赛德尔迭

代法。本节着重介绍此法用于求解稀疏线性方程组。两者的计算原理是一样的,即在迭代时用最新算出的部分 $x _ { i }$ 值代替旧的 $x _ { i }$ 值参于迭代。不妨将(10.7)式改写成如下等效形式：

$$
x _ { i } ( k ) = \frac { 1 } { a _ { i i } } [ b _ { i } - \ \sum _ { j < i } a _ { i j } x _ { j } ( k ) - \ \sum _ { j > i } a _ { i j } x _ { j } ( k - 1 ) ]
$$

按此,在第 $k$ 次迭代时,只有当 $x _ { i - 1 } ( k )$ 计算完成后才能开始计算 $x _ { i } ( k )$ ,这意味着计算的顺序性。

并行化讨论诚然,按照(10.14)式迭代计算时会加快收敛速度,但已如上述，第 $k$ 次迭代时，对于系数矩阵的下三角部分， $x _ { j } ( k )$ 的计算必须等待所有 $x _ { i } ( k )$ 计算完毕时才能进行。这种计算的顺序性限制了并行化的实现,当系数矩阵为稠密阵时的确如此。然而,对于稀疏矩阵,x;(k)的计算不一定要等到x(k),…，$x _ { i - 1 } ( k )$ 都计算完毕才行。因为稀疏矩阵大多数元素均为零，如果 $a _ { i j } = 0$ ,那么(10.14)左边 $x _ { i } ( k )$ 不依赖于 $x _ { j } ( k )$ ,所以只要计算出 $j < i$ 且 $a _ { i j } \neq 0$ 的 $x _ { j } ( k )$ ，$x _ { i } ( k )$ 便可计算。由此可见,高斯-赛德尔迭代法的并行化程度与系数矩阵 $\pmb { A }$ 下三角部分中非零元素的分布状况有关。试考虑(10.13)式所示的五点差分格式的迭代计算问题,此时所有格点值的更新可按下述公式计算之：

$$
x _ { i , j } ( k ) = \frac { 1 } { 4 } \{ x _ { i - 1 , j } ( k ) + x _ { i , j - 1 } ( k ) + x _ { i + 1 , j } ( k - 1 ) + x _ { i , j + 1 } ( k - 1 ) \}
$$

对上式迭代计算进行数据相关分析。图10.9(a)示出了 $4 \times 4$ 格点迭代计算的数据相关性。由图可知， $x _ { 1 , 1 }$ 之新值必须先计算;一旦算出 $x _ { 1 , 1 }$ ，就可并行计算x1,2与x2,1;使用新计算的x1,2和x2,1,就可同时计算x1,3,x2,2和x3,1,与此同时也可计算𝑥1,i下一次迭代之值;同样,下一步就并行计算x1,4,x2,3,x3,2，$x _ { 4 , 1 } , x _ { 1 , 2 }$ 和 $x _ { 2 , 1 }$ 。按此,可以将变量分为两组,每一组中的变量可以同时更新。一种方法就是有名的红-黑着色法(Red-Black Coloring)。如图10.9(b)所示，在每一行和每一列,将格点交替地着成红色,其余的着成黑色,相同颜色的格点可同时更新。而格点的更新是以波前(Wavefront)形式从左上角向右下角逐步推进，并行化程度是不高的。事实上，使用红-黑法对格点进行着色后，所有红点的邻节点仅为黑色，同样所有黑点的邻节点仅为红色。这样，高斯-赛德尔迭代法第$k$ 次迭代时可分为两步：

![](images/046c7941dde0320af782cdc39b7ea4d016f57a328f0764a7a4049f2607d1e59b.jpg)  
图10.9高斯-赛德尔法并行化分析(a)数据相关分析；(b)红-黑着色法

$\textcircled{1}$ 第1步,同时计算所有的红点：

$$
x _ { i , j } ( k ) = \frac { 1 } { 4 } \{ x _ { i - 1 , j } ( k - 1 ) + x _ { i , j - 1 } ( k - 1 ) + x _ { i + 1 , j } ( k - 1 ) + x _ { i , j + 1 } ( k - 1 ) \}
$$

$\textcircled{2}$ 第2步，同时计算所有的黑点：

$$
x _ { i , j } ( k ) = \frac { 1 } { 4 } \{ _ { x _ { i - 1 , j } } ( k ) + x _ { i , j - 1 } ( k ) + x _ { i + 1 , j } ( k ) + x _ { i , j + 1 } ( k ) \}
$$

而第2步计算黑点时所用到的红点值均已在第1步计算出。

# 10.4.4超松弛迭代法

雅可比超松弛法(JacobiOverRelaxation）雅可比超松弛法是雅可比迭代法的变体,它组合旧 $\pmb { x _ { i } }$ 之值与用雅可比标准算法所算出的新 $\pmb { x _ { i } }$ 之值,来计算新的$\pmb { x _ { i } }$ 之值,其更新计算遵循如下方程：

$$
x _ { i } \left( k \right) = \left( 1 - \gamma \right) x _ { i } \left( k - 1 \right) + \frac { \gamma } { \alpha _ { i i } } { \left[ b _ { i } - \mathrm { ~ \sum _ { j \ne i } ~ } a _ { i j } x _ { j } \left( k - 1 \right) \right] }
$$

其中 $\gamma ( 0 { \leqslant } \gamma { \leqslant } 1 )$ 为松弛因子,当 $\gamma = 1$ 时上式就是标准的雅可比迭代公式(10.9)。  
适当选择 $\gamma$ 之值可加快收敛。

逐次超松弛法 SOR(Successive Over Relaxation） 逐次超松弛法是高斯-赛德尔迭代法的变体,它组合旧 $\pmb { x _ { i } }$ 之值与用高斯-赛德尔法所算出的新 $\dot { \boldsymbol { x } } _ { i }$ 之值，来计算新的 $\pmb { x _ { i } }$ 之值,其更新计算遵循如下方程：

$$
x _ { i } ( k ) = ( 1 - \gamma ) x _ { i } ( k - 1 ) + \frac { \gamma } { \alpha _ { i i } } [ b _ { i } - \ \sum _ { j < i } \alpha _ { i j } x _ { j } ( k ) - \ \sum _ { j > i } \alpha _ { i j } x _ { j } ( k - 1 ) ]
$$

其中， $\gamma ( 0 \leqslant \gamma \leqslant 1 )$ 为松弛因子。当 $\gamma = 1$ 时上式就是高斯-赛德尔迭代公式(10.14)。适当选择 $\gamma$ 之值可加快收敛。

# 10.4.5多重网格法

基本原理 多重网格(Multigrid)法是一类求解偏微分方程数值解的迭代方法,产生于两个事实：其一，迭代方法在粗网格上比细网格上收敛更快;其二，如果变量初始估计值合适，则迭代算法收敛也快。所以多重网格法就是基于上述事实,用前一组网格格点上的值去计算后一组网格格点上的值。其中,在细网格上的迭代可得到较准确的解，在粗网格上的迭代能加快收敛速度。适当地组合粗、细网格上的迭代就可得到多重网格迭代算法。

算法描述为了简化讨论,仅考虑二维网孔上的多重网格法。约定： $G ^ { 0 }$ 是$\mathbf { \Omega } _ { n } \times \mathbf { \Omega } _ { n }$ 维（ $\pmb { n }$ 是2的方幂)的最细网格, $G ^ { i }$ 表示较粗的网格 $( 1 { \leqslant } i < \log n )$ ， $G ^ { k }$ 中的格点 $( i , j )$ 对应着变元 $x _ { i j } ^ { k }$ 。例如,对于 $n = 1 6$ ，则 $G ^ { 0 }$ 为 $1 6 \times 1 6$ 的网格(最细网格）, $G ^ { 1 }$ 为 ${ \bf 8 } \times { \bf 8 }$ 的网格, $G ^ { 2 }$ 为 $4 \times 4$ 的网格, $G ^ { 3 }$ 为 $2 \times 2$ 的网格（最粗的网格）。

在多重网格算法中,有三类运算：

$\textcircled{1}$ 松弛(Relaxation):计算 $G ^ { k }$ 中所有 $x _ { i j } ^ { k }$ 之值,这可用雅可比迭代法、高斯-赛德尔迭代法、雅可比超松弛法、逐次超松弛法或其它迭代方法。

$\textcircled{2}$ 内插(Interpolation):用较粗网格 $G ^ { k }$ 中变量 $x _ { i , j } ^ { k }$ 之值,去计算较细网格$G ^ { k - 1 }$ 中变量 $x _ { i , j } ^ { k - 1 }$ 之值。一种简单内插法是以与 $x _ { i , j } ^ { k - 1 }$ 最近的 $G ^ { k }$ 中变量之值取平均值作为 $x _ { i , j } ^ { k - 1 }$ 之值。例如， $x _ { 3 , 5 } ^ { 0 } = \frac { 1 } { 4 } \big ( x _ { 2 , 4 } ^ { 1 } + x _ { 2 , 6 } ^ { 1 } + x _ { 4 , 4 } ^ { 1 } + x _ { 4 , 6 } ^ { 1 } \big ) _ { \circ }$

$\textcircled{3}$ 投射(Projection):用较细网格 $G ^ { k - 1 }$ 中变量 $x _ { i , j } ^ { k - 1 }$ 之值,去计算较粗网格$G ^ { k }$ 中变量 $x _ { i } ^ { k }$ j之值。一种投射法是内射法,它取与细网格点相重合的粗网格点之值作为粗网格点之值,即 $x _ { i , j } ^ { k } = x _ { i , j } ^ { k - 1 }$ 。例如， $x _ { 4 , 4 } ^ { 2 } = x _ { 4 , 4 } ^ { 1 }$ 。

使用多重网格法时,由于在粗网格上未知量少,从而问题计算规模比细网格上小,因此粗网格上问题的求解比细网格上容易。如果首先近似地求出粗网格上的解,然后将其插值到细网格上作为细网格迭代的初值,则细网格上的松弛收敛将会加快。这种将粗、细网格优点相互结合的方法,使多重网格法的应用非常广泛。

并行化通信分析多重网格算法中，松弛、内插和投射均会产生通信要求。其中,松弛计算的通信要求已在10.4.2节讨论过;而内射法(Injection)不产生通信要求;在简单内插时,细网格点之值由其近邻的诸粗网格点之值决定之。在此情况下,假定将最细网格 $G ^ { 0 }$ 指派给 $\mathbf { \Omega } _ { n } \times \mathbf { \Omega } _ { n }$ 的二维处理器阵列上,那么在较粗网格 $G ^ { 1 } , G ^ { 2 } , \cdots , G ^ { \log n - 1 }$ 上需要相互通信的处理器是不相邻的,其距离在 $G ^ { 1 }$ 上为2,在 $G ^ { 2 }$ 上为4,如此等等。

当把网格 $G ^ { 0 } , G ^ { 1 } , \cdots , G ^ { \log n - 1 }$ 映射到超立方上时,情况比映射到二维网孔上复杂。这时可以使用葛莱码把二维网孔映射到超立方上,但这只能确保 $G ^ { 0 }$ 中相邻的格点映射到超立方的相邻顶点上,而对较粗网格不能都这样。在最坏情况下， $\mathbf { \Omega } _ { n } \times \mathbf { \Omega } _ { n }$ 的网格中的某一点会有 $4 \log n - 2$ 个邻居,而点数为 $n ^ { 2 }$ 的超立方仅有 $2 \log { n }$ 个邻居。例如图10.10所示的 ${ \bf 8 \times 8 }$ 的网格中,点18有10个邻居，但64个顶点的超立方任一点都只有6个邻居。所以网格不能直接嵌入超立方中。但可以使G1,,Glg"中的邻点在超立方上相离为2。为此可将处理器编号分为两部分，一部分相应于行，另一部分相应于列;然后使用葛莱码将相邻的行和列元素映射到超立方相邻的顶点上。

![](images/df0018ccaea7bbe63116e30d761de68c97ed7fef08f346453e32a100d528f647.jpg)  
图10.10二维多重网格映射到超立方上

# 10.4.6共轭梯度法

共轭梯度(Conjugate Gradient)法,也叫共轭斜量法。从理论上讲它是属于直接法,但在实际计算过程中,由于不可避免地会出现舍人误差,所以常作为迭代法使用。该方法的最大特点是，当方程组的阶数很高时，往往只要经过比阶数小得多的迭代次数，就能得到满足精度要求的近似解。

基本思想共轭梯度法是属于最小化类的迭代方法。为了求解 $\mathbf { A } \pmb { x } = \pmb { b }$ 这样的一次函数,可以先构造一个二次函数 $q ( x )$ ,然后利用最小化原理对其求导$\partial q ( x ) / \partial x$ ,再令其为零。如果 $\partial q ( x ) / \partial x = A x - b = 0$ ,那么就可达到求解 $\mathbf { A } \mathbf { x }$ $- \ b = 0$ 的目的。所以关键的问题是如何构造一个所要求的二次函数。

构造二次函数 ${ \pmb q } ( { \pmb x } )$ 先定义一个二次齐次函数 $f ( x )$ ,再定义一个一次线性函数 $g ( x )$ ,将两者合成为 $q ( x )$ 。

$\textcircled{1}$ 定义二次齐次函数：

$$
\begin{array} { r } { f ( x _ { 1 } , x _ { 2 } , \cdots , x _ { n } ) = a _ { 1 1 } x _ { 1 } ^ { 2 } + a _ { 2 2 } x _ { 2 } ^ { 2 } + \cdots + a _ { n n } x _ { n } ^ { 2 } + \qquad } \\ { 2 a _ { 1 2 } x _ { 1 } x _ { 2 } + 2 a _ { 1 3 } x _ { 1 } x _ { 3 } + \cdots + 2 a _ { n - 1 , n } x _ { n - 1 } x _ { n } } \end{array}
$$

如果 $a _ { i j } = a _ { j i }$ ,则上式可写成如下形式：

$$
\begin{array} { r } { f ( x _ { 1 } , x _ { 2 } , \cdots , x _ { n } ) = \alpha _ { 1 1 } x _ { 1 } ^ { 2 } + a _ { 1 2 } x _ { 1 } x _ { 2 } + \cdots + a _ { 1 n } x _ { 1 } x _ { n } \ + } \\ { \qquad \quad \alpha _ { 2 1 } x _ { 2 } x _ { 1 } + \alpha _ { 2 2 } x _ { 2 } ^ { 2 } + \cdots + a _ { 2 n } x _ { 2 } x _ { n } \ + } \end{array}
$$

$$
\alpha _ { n 1 } x _ { n } x _ { 1 } + \alpha _ { n 2 } x _ { n } x _ { 2 } + \cdots + \alpha _ { n n } x _ { n } ^ { 2 }
$$

$$
x _ { n } ( a _ { n 1 } x _ { 1 } + a _ { n 2 } x _ { 2 } + \cdots + a _ { n n } x _ { n }
$$

$$
\mathbf { \Sigma } = ( \mathbf { \Sigma } _ { X _ { 1 } , X _ { 2 } } , \cdots , \mathbf { \Sigma } _ { X _ { n } } ) \left( \begin{array} { l l l l } { a _ { 1 1 } } & { a _ { 1 2 } } & { \cdots } & { a _ { 1 n } } \\ { a _ { 2 1 } } & { a _ { 2 2 } } & { \cdots } & { a _ { 2 n } } \\ { a _ { \mathbf { \Sigma } } } & { \vdots } & & \\ { a _ { n 1 } } & { a _ { n 2 } } & { \cdots } & { a _ { n n } } \end{array} \right) \left( \begin{array} { l } { x _ { 1 } } \\ { x _ { 2 } } \\ { \vdots } \\ { x _ { n } } \end{array} \right) = \mathbf { x } ^ { \mathrm { T } } A \mathbf { x }
$$

$\textcircled{2}$ 定义一次线性函数：

$$
\begin{array} { c } { g ( x _ { 1 } , x _ { 2 } , \cdots , x _ { n } ) = x _ { 1 } b _ { 1 } + x _ { 2 } b _ { 2 } + \cdots + x _ { n } b _ { n } } \\ { \qquad } \\ { = ( x _ { 1 } , x _ { 2 } , \cdots , x _ { n } ) \left( \begin{array} { l } { b _ { 1 } } \\ { b _ { 2 } } \\ { \vdots } \\ { b _ { n } } \end{array} \right) = { \pmb x } ^ { \mathrm { T } } { \pmb b } } \end{array}
$$

$\textcircled{3}$ 合成 $f ( x )$ 与 ${ \pmb g } ( { \pmb x } )$ ：

$$
q ( x ) = \frac { 1 } { 2 } \pmb { x } ^ { \mathrm { T } } \pmb { A } \pmb { x } - \pmb { x } ^ { \mathrm { T } } \pmb { b }
$$

求二次函数 ${ \pmb q } ( { \pmb x } )$ 的最小值为此要对 $q ( x )$ 求偏导数，即 $\partial q ( x ) / \partial x = \partial q$ $\left( x \right) / \partial x _ { 1 } + \partial q \left( x \right) / \partial x _ { 2 } + \cdots + \partial q \left( x \right) / \partial x _ { n }$ ,其中，

$$
{ \begin{array} { c } { { \frac { \partial q \left( x \right) } { \partial x _ { 1 } } } = { \frac { 1 } { 2 } } \left( 2 a _ { 1 1 } x _ { 1 } + 2 a _ { 1 2 } x _ { 2 } + 2 a _ { 1 3 } x _ { 3 } + \cdots + 2 a _ { 1 \pi } x _ { n } \right) - b _ { 1 } } \\ { { \frac { \partial q \left( x \right) } { \partial x _ { 2 } } } = { \frac { 1 } { 2 } } \left( 2 a _ { 2 1 } x _ { 1 } + 2 a _ { 2 2 } x _ { 2 } + 2 a _ { 2 3 } x _ { 3 } + \cdots + 2 a _ { 2 n } x _ { n } \right) - b _ { 2 } } \\ { \vdots } \\ { { \frac { \partial q \left( x \right) } { \partial x _ { n } } } = { \frac { 1 } { 2 } } \left( 2 a _ { n 1 } x _ { 1 } + 2 a _ { n 2 } x _ { 2 } + 2 a _ { n 3 } x _ { 3 } + \cdots + 2 a _ { n n } x _ { n } \right) - b _ { n } } \end{array} }
$$

所以，

$$
{ \frac { \partial q \left( { \boldsymbol { x } } \right) } { \partial { \boldsymbol { x } } } } = { \left( \begin{array} { l l l l l } { a _ { 1 1 } } & { a _ { 1 2 } } & { a _ { 1 3 } } & { \cdots } & { a _ { 1 n } } \\ { a _ { 2 1 } } & { a _ { 2 2 } } & { a _ { 2 3 } } & { \cdots } & { a _ { 2 n } } \\ & & & & { \vdots } \\ { a _ { n 1 } } & { a _ { n 2 } } & { a _ { n 3 } } & { \cdots } & { a _ { n n } } \end{array} \right) } { \left( \begin{array} { l } { x _ { 1 } } \\ { x _ { 2 } } \\ { \vdots } \\ { x _ { n } } \end{array} \right) } - { \left( \begin{array} { l } { b _ { 1 } } \\ { b _ { 2 } } \\ { \vdots } \\ { b _ { n } } \end{array} \right) } = \mathbf { A } \mathbf { x } - \mathbf { b }
$$

因此,所构造的二次函数 $q \left( x \right)$ ,求导后令其为零,正是要求解的线性方程组 $\mathbf { A } { \boldsymbol { x } } - \mathbf { b } = 0$ 。

共轭梯度法 ${ \pmb { \alpha } } ( { \pmb { k } } )$ 与 $\alpha ( k )$ 的求取用共轭梯度法求解 $\mathbf { A } { \boldsymbol { \mathbf { \mathit { x } } } } - \mathbf { \boldsymbol { \mathbf { b } } } = \mathbf { 0 }$ 的迭代公式如下：

$$
{ \pmb x } \left( \ b k \right) = { \pmb x } \left( \ b k - 1 \right) + { \pmb \alpha } \left( \ b k \right) { \pmb d } \left( \ b k \right)
$$

新向量 ${ \pmb x } ( k )$ 的值由老向量 $x \left( k - 1 \right)$ 、迭代步长 ${ \pmb { \alpha } } ( { \pmb { k } } )$ 和方向向量 $\pmb { d } ( k )$ 决定之，此时 $x ( k )$ 至多迭代 $_ n$ 次就可收敛。

$\textcircled{1}$ 求 ${ \pmb { \alpha } } ( { \pmb { k } } )$ ：对于给定的 ${ \pmb x } \left( { \pmb k } - 1 \right)$ 和 ${ \pmb d } \left( \pmb { k } \right) , { \pmb \alpha } \left( \pmb { k } \right)$ 的选取应使所构造的二次函数 $q ( x )$ 取最小值。由 $\frac { \partial q \left( \boldsymbol { x } \right) } { \partial \boldsymbol { x } } = \boldsymbol { A } \boldsymbol { x } \left( \boldsymbol { k } \right) - \boldsymbol { b } = \boldsymbol { 0 }$ 和 $\begin{array} { r } { \pmb { A } \pmb { x } \left( \pmb { k } \right) - \pmb { b } = \pmb { A } \left[ \pmb { x } \left( \pmb { k } - 1 \right) + \right. } \end{array}$ ${ \pmb { a } } \left( \beta \right) { \pmb { d } } \left( \beta \right) \} - { \pmb { b } } = 0$ ，可求出 ${ \pmb { \alpha } } ( k )$ 为：

$$
\pmb { \alpha } ( k ) = \frac { \pmb { b } - \pmb { A } \pmb { x } ( \pmb { k } - 1 ) } { \pmb { A } \pmb { d } ( \pmb { k } ) }
$$

令 ${ \pmb r } ( k )$ 为第 $k$ 次迭代的残向量：

$$
r ( k ) = A x ( k - 1 ) - b
$$

(10.22)代入(10.21）,则有

$$
\pmb { \alpha } ( k ) = - \frac { \pmb { r } ( k ) } { \pmb { A } \pmb { d } ( k ) } = - \frac { \pmb { d } ^ { \operatorname { T } } ( k ) \pmb { r } ( k ) } { \pmb { d } ^ { \operatorname { T } } ( k ) \pmb { A } \pmb { d } ( k ) }
$$

可见,每次迭代时唯一的矩阵－向量乘就是 $\pmb { A } \pmb { d } ( \pmb { k } )$ 。

$\textcircled{2}$ 求 $\pmb { d } ( \pmb { k } )$ ：求 $\pmb { d } ( \pmb { k } )$ 时,应使函数 $q ( x )$ 在 $\pmb { x _ { i } }$ 点最快地下降到 $x _ { i + 1 }$ ,而函数$q ( x )$ 在 $\boldsymbol { x } = \boldsymbol { x } _ { i }$ 点的变化率最快的方向就是 $q ( x )$ 在 $\pmb { x _ { i } }$ 处的梯度，即

$$
{ \mathrm { g r a d } } \ q \ { \Biggl | } _ { { \boldsymbol { x } } _ { i } } \ = \left( { \frac { \partial q } { \partial x _ { 1 } } } , { \frac { \partial q } { \partial x _ { 2 } } } , \cdots , { \frac { \partial q } { \partial x _ { n } } } \right) ^ { \mathrm { T } } { \Biggl | } _ { { \boldsymbol { x } } _ { i } }
$$

所以迭代时取梯度方向作为 $\pmb { d } _ { i }$ 。

可以证明,如果 $\pmb { A }$ 是对称正定的,且 $d _ { 1 } , d _ { 2 } , \cdots , d _ { n }$ 是相对于 $\pmb { A }$ 共轭的（即${ { d _ { i } } ^ { \mathrm { T } } } A { { d _ { j } } } = 0 , 1 { \leqslant } i , j { \leqslant } n , i { \neq } j )$ ，则 ${ \pmb x } \left( \ b k \right) = { \pmb x } \left( \ b k - 1 \right) + { \pmb \alpha } \left( \ b k \right) { \pmb d } \left( \ b k \right)$ 最多迭代 $_ n$ 次就可收敛到 $\mathbf { A } \mathbf { x } = \mathbf { \nabla } \delta$ 的解。

因此,从一组共轭矩阵 $\pmb { A }$ 的方向向量,作为迭代方向求解 $\mathbf { A } \mathbf { x } = \mathbf { b }$ 的方法称之为共轭梯度法。在此法中，一组共轭A的方向向量d(k)可选取如下：

$$
d \left( k \right) = - r \left( k \right) + \frac { r ^ { \operatorname { T } } ( k ) r \left( k \right) } { r ^ { \operatorname { T } } ( k - 1 ) r \left( k - 1 \right) } d \left( k - 1 \right)
$$

其中 $r ^ { \mathrm { T } } ( k ) r ( k )$ 表示残向量转置与残向量之内积。

共轭梯度算法步骤用共轭梯度法求解 $\mathbf { A } { \boldsymbol { \mathbf { \mathit { x } } } } - \mathbf { \boldsymbol { \mathit { b } } } = \mathbf { 0 }$ 的步骤如下：

$\textcircled{1}$ 初始化： ${ \pmb x } \left( 0 \right) = 0 , { \pmb d } \left( 0 \right) = 0 , { \pmb r } \left( 0 \right) = { \bf - \kappa \pmb \nu } _ { 0 }$ $\textcircled{2}$ 在第 $k$ 次迭代时,计算 ${ \pmb x } ( k )$ 分为四步：第1步：计算残向量(按照(10.22)式)：

$$
r ( k ) = A x ( k - 1 ) - b
$$

第2步：计算方向向量(按照(10.24)式)：

$$
\pmb { d } \left( k \right) = - r \left( k \right) + \frac { \pmb { r } ^ { \operatorname { T } } ( k ) \pmb { r } ( k ) } { \pmb { r } ^ { \operatorname { T } } ( k - 1 ) \pmb { r } ( k - 1 ) } \pmb { d } \left( k - 1 \right)
$$

第3步：计算步长(按照(10.23)式)：

$$
\pmb { \alpha } ( k ) = - \frac { \pmb { d } ^ { \operatorname { T } } ( k ) \pmb { r } ( k ) } { \pmb { d } ^ { \operatorname { T } } ( k ) \pmb { A } \pmb { d } ( k ) }
$$

第4步：计算新的近似变量(按照(10.20)式)：

$$
{ \pmb x } \big ( \pmb { k } \big ) = { \pmb x } \big ( \pmb { k } - 1 \big ) + { \pmb \alpha } \big ( \pmb { k } \big ) { \pmb d } \big ( \pmb { k } \big )
$$

SISD上共轭梯度算法用共轭梯度法求解 $\mathbf { A } \mathbf { x } = \mathbf { b }$ 的串行算法如算法10.10。其中,denom1,denom2,num1,num2,tempvect $\left[ 1 \colon n \right]$ 为临时变量,主算法调用两个过程 INNER.PRODUCT()和 MATRIX-VECTOR.PRODUCT（）。

算法10.10 SISD上求解 $\mathbf { A } \mathbf { \boldsymbol { x } } = \mathbf { \boldsymbol { b } }$ 共轭梯度算法

输入： $\mathbf { A } _ { n \times n } , \pmb { b } = [ b _ { 1 } , \cdots , b _ { n } ] ^ { \mathrm { T } } , \varepsilon$ 输出： $\pmb { x } = \big [ \pmb { x } _ { 1 } , \cdots , \pmb { x } _ { n } \big ] ^ { \mathrm { T } }$

Begin

(1） for $i = 1$ to $\pmb { n }$ do $\big / \ast$ 初始化 $\yen 7$

$$
\begin{array} { l } { { d _ { i } = 0 } } \\ { { \ } } \\ { { x _ { i } = 0 } } \\ { { r _ { i } = { \ - \ b _ { i } } } } \end{array}
$$

end for

$$
r _ { 1 : n } = M A T R I X { \cdot } V E C T O R . P R O D U C T ( a _ { 1 : n , 1 : n , x _ { 1 : n } } )
$$

$$
r _ { i } = r _ { i } - b _ { i }
$$

# end for

$$
\mathrm { n u m 1 } { = } \mathrm { I N N E R . P R O D U C T } ( r _ { 1 : n } , r _ { 1 : n } )
$$

$$
d _ { i } = - r _ { i } + \frac { \mathrm { n u m l } } { \mathrm { d e n o m l } } d _ { i }
$$

# end for

$$
{ \mathrm { n u m } } 2 = { \mathrm { I N N E R . P R O D U C T } } ( d _ { 1 : n } , r _ { 1 : n } ) \quad / *
$$

$$
d _ { 1 : n } )
$$

$$
\mathtt { d e n o m 2 } = \mathtt { I N N E R . P R O D U C T } ( d _ { 1 : n } , \mathrm { t e m p v e c t } _ { 1 , n } )
$$

(2.11） for $i = 1$ to $\pmb { n }$ do $\big / \ast$ 修正 $x _ { i } \ast { \mathrm { ~ } } /$

$$
x _ { i } = x _ { i } + \alpha d _ { i }
$$

# end for end for

End   
INNER.PRODUCT ${ \bf \Phi } ( a _ { 1 : n } , b _ { 1 : n } )$ begin result $\mathbf { \tau } = \mathbf { 0 }$ for $i = 1$ to $\pmb { n }$ do ${ \mathrm { r e s u l t } } = { \mathrm { r e s u l t } } + \alpha _ { i } b _ { i }$ end for return result end   
MATRIX-VECTOR.PRODUCT(a1:n,1:n , 61:n) begin for $i = 1$ to $\pmb { n }$ do $\mathbf { r e s u l t } _ { i } = 0$ for $j = 1$ to $\pmb { n }$ do ${ \mathrm { r e s u l t } } _ { i } = { \mathrm { r e s u l t } } _ { i } + a _ { i j } b _ { j }$ end for end for return result 1: n end

并行化通信分析假定算法10.10在分布存储的并行机上实现，且每个处理器在其局存中存有 $A$ 的若干行以及相应的向量 $\pmb { b } \sqrt { \pmb { d } } \setminus \pmb { r }$ 的分量。则由于并行化所造成的通信要求主要来源于向量内积(INNER.PRODUCT)和矩阵与向量乘积(MATRIX-VECTOR.PRODUCT)。在计算向量内积时，每个处理器计算它的局部积之和，为了计算总的积之和(即内积)要花费对数时间，所以向量内积的通信时间为 $O \left( { \frac { n } { \hbar } } + \log \hbar \right)$ 。在计算矩阵～向量之积时，每个处理器均需与其它处理器通信,以取得别的处理器中的向量 $\pmb { b }$ 之分量，为此可先把各个处理器中 $\pmb { b }$ 之分量集中在一个处理器中,然后由此处理器以树状形式播送给各处理器,这种通信策略的总耗费时间为 $O ( n \log { p } )$ 。

# 10.5 小结和导读

小结线性代数方程组的求解在科学和工程计算中应用非常广泛,这是因为很多科学与工程问题的计算，最终大都可以化为线性代数方程组的求解。本章主要讨论最基本的线性方程组的求解,包括三角形方程组、三对角方程组、稠密和稀疏线性方程组等的经典解法。

线性代数方程组的数值解法通常有两种：直接法和迭代法。直接法，又称消元法,是利用矩阵变换技巧,将一般的系数矩阵化为特殊形式(如上三角和对角形式)的矩阵以对方程组消解。其优点是可以预先估计运算量，并可得到问题的准确解，但由于实际计算过程中总存在着舍入误差,因此直接法得到的结果并非绝对精确，并且还存在着计算过程的稳定性问题。迭代法是一种逐步求精的近似求解过程,此法一般总是假定方程组中的系数 $a _ { i i } { \neq } 0 ( i = 1 , \cdots , n )$ 。其优点是简单,易于计算机编程，但它存在着迭代是否收敛和收敛快慢的问题。迭代求解的过程是，先给定初始解,然后逐次迭代下去，且理论上讲，每次迭代的结果都应改善前一次的计算结果。迭代过程由预先给定的精度要求来控制，但由于方程组的准确解一般是不知道的,因此判断某次迭代是否满足精度要求是困难的，通常我们总是认为当相邻两次迭代值 $x _ { i } \left( k \right)$ 与 $x _ { i } \left( k - 1 \right)$ 也很接近时, $x _ { i }$ 与 $x _ { i } \left( \boldsymbol { k } \right)$ 也很接近,因此就可直接用条件 $\operatorname* { m a x } _ { 1 \leqslant i \leqslant n } \big | x _ { i } ( k ) - x _ { i } ( k - 1 ) \big | < \varepsilon$ 来判定迭代是否终止。迭代法在求解稀疏线性方程组时经常使用，而很多的偏微分方程经差分化后也可化为稀疏线性方程组,所以在偏微分方程数值求解中,迭代法使用得尤其广泛。

导读[136]是一本很好的综述性专著,它全面地讨论了向量机和并行机上线性方程组的直接法和迭代法的并行求解方法;[91]是一篇有关并行数值算法的很好的综述文章;[149]展示了三角形方程组求解器可在多计算机上有效地实现;[96]首先引人奇－偶归约算法;[73]讨论了共享存储和分布存储结构的并行机上稠密线性方程组的并行算法;[90]综述了稀疏线性方程组的并行求解算法；[135]综述了在向量机和并行机上偏微分方程的求解方法；[44]讨论了超立方多处理机上的多重网格算法;[50]讨论了并行共轭梯度算法。在国内[202]全面地介绍了工程上常用的、行之有效的串行算法(主要偏重于数值问题的常用算法)；[201]较深人、系统地介绍了SIMD并行机上并行数值计算方法,对MIMD并行机上的数值算法也作了简要介绍;[195]深人而全面地论述了SIMD和MIMD模型上的数值代数、离散变换和卷积、微分方程、计算数论和最优化计算的并行算法,对并行排序算法也作了介绍。此外，在[143]书中第九章的参考文献注释中还列举了大量有关参考文献，读者可追踪进一步阅读。

# 习 题

10.1如果在(10.2)式中,引入虚变量 $\pmb { x _ { 0 } }$ 与 ${ \pmb x } _ { \pmb { \mathscr { n } } + 1 }$ 以及 ${ \pmb x } _ { - 1 }$ 与 $x _ { n + 2 }$ 且令它们为零：

$\textcircled{1}$ 试推导下式：

$$
f _ { i } \left( \frac { b _ { i - 1 } - f _ { i - 1 } x _ { i - 2 } - h _ { i - 1 } x _ { i } } { g _ { i - 1 } } \right) + g _ { i } x _ { i } + h _ { i } \left( \frac { b _ { i + 1 } - f _ { i + 1 } x _ { i } - h _ { i + 1 } x _ { i + 2 } } { g _ { i + 1 } } \right) = b _ { i }
$$

为了简化，记 $r _ { i } = f _ { \mathrm { i } } / g _ { \mathrm { i } - 1 } , \delta _ { \mathrm { i } } = h _ { \mathrm { i } } / g _ { \mathrm { i } + 1 } , 1 { \leqslant i } \leqslant n$ ,则(10.25)式可写成：$\begin{array} { r l } & { - \ r _ { i } \ f _ { i - 1 } x _ { i - 2 } + \big ( g _ { i } - r _ { i } h _ { i - 1 } - \delta _ { i } f _ { i + 1 } \big ) x _ { i } - \delta _ { i } h _ { i + 1 } x _ { i + 2 } = b _ { i } + r _ { i } b _ { i - 1 } - \delta _ { i } b _ { i + 1 } } \\ & { \qquad \quad 1 \leqslant i \leqslant n } \end{array}$ 根据(10.26)式,可设计如下 SISD上奇偶归约法求解三对角线性方程组算法10.11：

算法10.11 SISD上三对角方程组奇偶归约求解算法   
输入 $\mathbf { \partial } : A _ { n } \times \mathbf { \partial } _ { n } , b = \left[ b _ { 1 } , \cdots , b _ { n } \right] ^ { \mathbf { T } }$   
输出： $\mathbf { \pmb { x } } = \{ \pmb { x } _ { 1 } , \cdots , \pmb { x } _ { n } \} ^ { \bar { \mathbf { T } } }$   
Begin

(1) for ${ \bf { \sigma } } _ { i } = { \bf { 0 } }$ to $\log n - 1$ do (1.1) $\pmb { d } = 2 ^ { i }$ (1.2) for $\scriptstyle j = 2 i + 1$ to $\pmb { n } - 1$ step $\pmb { 2 } \pmb { d }$ do $\begin{array} { r l } & { r _ { j } = f _ { j } / g _ { j - d } , \ S _ { j } = h _ { j } / g _ { j + d } , f _ { j } ^ { \prime } = - r _ { j } f _ { j - d } , } \\ & { \boldsymbol { g } ^ { \prime } { } _ { j } = - \delta _ { j } f _ { i + d } - r _ { j } h _ { j - d } , \boldsymbol { h } ^ { \prime } { } _ { j } = \delta _ { j } h _ { j + d } } \\ & { \boldsymbol { b } ^ { \prime } { } _ { j } = b _ { j } + r _ { j } b _ { j - d } - \delta _ { j } b _ { j + d } } \end{array}$ end for (1.4) $\begin{array} { r l } & { r _ { n } = f _ { n } / g _ { n - d } } \\ & { f _ { n } = - \ r _ { n } f _ { n - d } } \\ & { g _ { n } = g _ { n } - \ r _ { n } h _ { n } - d } \\ & { b _ { n } = b _ { n } + \ r _ { n } b _ { n } - d } \end{array}$ (1.6) (1.7) for $\begin{array} { r } { j = 2 i + 1 } \end{array}$ to $\pmb { n } - 1$ step $2 d$ do $f _ { j } = f ^ { \prime } { } _ { j } , g _ { j } = g ^ { \prime } { } _ { j } , h _ { j } = h ^ { \prime } { } _ { j } , b _ { j } = b ^ { \prime } { } _ { j }$ end for end for

(2) ${ x _ { n } = b _ { n } / g _ { n } }$   
(3) for $\pmb { i } = \log \pmb { n } - 1$ to O step - 1 do (3.1) $d = 2 ^ { i }$ (3.2) $x _ { d } = ( b _ { d } - h _ { d } x _ { 2 d } ) / g _ { d }$ (3.3) for ${ j = 3 d }$ to $\pmb { n }$ step $^ { 2 d }$ do

$$
x _ { j } = ( b _ { j } - f _ { j } x _ { j - d } - h _ { j } x _ { j + d } ) / g _ { j }
$$

# end for

end for

End

$\textcircled{2}$ 假定：

$$
\begin{array} { r } { A = \left( \begin{array} { c c c c c c c c c } { 4 } & { 1 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 4 } & { 1 1 } & { - 5 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 2 } & { 1 4 } & { - 6 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 5 } & { 1 8 } & { - 4 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 1 } & { 2 } & { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 2 } & { 3 } & { 6 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 2 } & { 1 } & { 1 2 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 5 } & { 8 } \end{array} \right) , B = \left( \begin{array} { c } { 2 } \\ { 7 } \\ { 1 3 } \\ { 1 8 } \\ { 6 } \\ { 3 } \\ { 9 } \\ { 9 } \\ { - 1 } \end{array} \right) , } \end{array}
$$

10.2试证明：在奇偶归约算法中,如果对于所有 $_ i$ ，满足 $\mid _ { g _ { i } } \mid \geqslant \mid _ { f _ { i } } \mid + \mid _ { h _ { i } } \mid$ (即对角占优),则消去奇下标变量后的方程组仍具有对角占优的性质。

[提示：考查(10.5)式,对于所有 $\textbf { \em i }$ ,如果 $\mid _ { g _ { i } } \mid \geqslant \mid f _ { i } \mid + \mid h _ { i } \mid$ 其系数关系。]

10.3试分析高斯主元消去法算法10.4的复杂度为：

$$
( 2 n ^ { 3 } + 3 n ^ { 2 } - 2 n - 3 ) / 3
$$

10.4试用高斯主元消去法算法10.4,逐步求解下述线性方程组：

$$
\left( { \begin{array} { r r r r r } { - 1 } & { 2 } & { 1 } & { - 2 } \\ { 2 } & { 2 } & { 0 } & { 1 } \\ { 1 } & { - 1 } & { 3 } & { - 5 } \\ { - 2 } & { 3 } & { - 4 } & { 4 } \end{array} } \right) { \left( \begin{array} { l } { x _ { 1 } } \\ { x _ { 2 } } \\ { x _ { 3 } } \\ { x _ { 4 } } \end{array} \right) } = \left( { \begin{array} { l } { 4 } \\ { 3 } \\ { 2 } \\ { 1 } \end{array} } \right)
$$

10.5试分析算法10.5的复杂度。如果处理器按列分配,情况有何变化?

10.6根据10.3.2节所述原理,参照算法10.4,试写出 SISD上求解稠密线性方程组的高斯-约旦主元消去法的算法。

10.7试用高斯-赛德尔算法10.7,逐步求解下述线性方程组 ${ \bf \Pi } _ { \varepsilon } ^ { \prime } = 1 0 ^ { - 6 }$ ）

$$
\left( \begin{array} { c c c c } { { 1 } } & { { 3 } } & { { 2 } } & { { 1 3 } } \\ { { 7 } } & { { 2 } } & { { 1 } } & { { - 2 } } \\ { { 9 } } & { { 1 5 } } & { { 3 } } & { { - 2 } } \\ { { - 2 } } & { { - 2 } } & { { 1 1 } } & { { 5 } } \end{array} \right) \left( \begin{array} { c } { { x _ { 1 } } } \\ { { x _ { 2 } } } \\ { { x _ { 3 } } } \\ { { x _ { 4 } } } \end{array} \right) = \left( \begin{array} { c } { { 0 } } \\ { { 4 } } \\ { { 7 } } \\ { { - 1 } } \end{array} \right)
$$

# 10.8对于如下的泊松方程

$$
- \left( \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } + \frac { \partial ^ { 2 } u } { \partial y ^ { 2 } } \right) = f
$$

其中f=f(x,y)不为零,主要问题就是定出未知函数u=u(x,y)在某区域Ω内满足(10.27),且在边界 $\partial \varOmega$ 上满足给定的条件。

$\textcircled{1}$ 试推导其差分方程为：

$$
4 u _ { i , j } - ( u _ { i - 1 , j } + u _ { i + 1 , j } + u _ { i , j - 1 } + u _ { i , j + 1 } ) = h ^ { 2 } f _ { i , j } , 1 \leqslant i , j \leqslant n - 1
$$

其中， $\pmb { h }$ 为网格间距， $h = 1 / n \mathrm { ~ , ~ } u _ { i , j }$ 为格点 $( i , j )$ 的函数值 $u ( x _ { i } , y _ { j } )$

$\textcircled{2}$ 如何变换(10.28)式使其成为如下线性方程组：

$$
\pmb { A } \pmb { U } = \pmb { F }
$$

其中，系数矩阵 $\pmb { A }$ 为块三对角矩阵：

$$
\left( \begin{array} { l l l l } { s } & { \boldsymbol { \vartheta } } & & \\ { \boldsymbol { \vartheta } } & { s } & { \boldsymbol { \vartheta } } & \\ & { \cdot _ { \cdot } } & & \\ & { \boldsymbol { \vartheta } } & { s } & { \boldsymbol { \vartheta } } \\ & & & { \boldsymbol { \varrho } } & \end{array} \right)
$$

$\pmb { S }$ 和 $\pmb { Q }$ 都是 $\left( n - 1 \right) \times \left( n - 1 \right)$ 的矩阵，且 $\pmb { s }$ 本身又是三对角矩阵：

$$
\left( \begin{array} { c c c c c c } { { 1 } } & { { - \frac { 1 } { 4 } } } & { { } } & { { } } & { { } } & { { } } \\ { { - \frac { 1 } { 4 } } } & { { 1 } } & { { \frac { 1 } { 4 } } } & { { } } & { { } } & { { } } \\ { { } } & { { } } & { { \ddots } } & { { } } & { { } } & { { } } \\ { { } } & { { } } & { { - \frac { 1 } { 4 } } } & { { 1 } } & { { - \frac { 1 } { 4 } } } \\ { { } } & { { } } & { { } } & { { } } & { { - \frac { 1 } { 4 } } } & { { 1 } } \end{array} \right)
$$

而 $Q = - \frac { 1 } { 4 } I , I$ 为单位矩阵,向量 $\pmb { U }$ 未知：

$$
\begin{array} { r l } & { \pmb { U } ^ { \mathrm { T } } = ( u _ { 1 , 1 } , u _ { 1 , 2 } , \cdots , u _ { 1 , n - 1 } , u _ { 2 , 1 } , u _ { 2 , 2 } , \cdots , u _ { 2 , n - 1 } , \cdots , } \\ & { \qquad \quad u _ { n - 1 , 1 } , u _ { n - 1 , 2 } , \cdots , u _ { n - 1 , n - 1 } ) } \end{array}
$$

向量F已知,F(i-1)(n-1)+j= fi,jo

10.9试证明共轭梯度法求解 $\pmb { n }$ 阶线性方程组，最多迭代 $\pmb { n }$ 次即可收敛。

10.10试用共轭梯度法,求解下述方程组。假定

$$
{ \pmb x } ( 0 ) = [ 0 , 0 , 1 ] ^ { \mathrm { T } } \mathrm { : }
$$

$$
{ \left( \begin{array} { l l l } { 2 } & { 1 } & { 0 } \\ { 1 } & { 2 } & { 1 } \\ { 0 } & { 1 } & { 1 } \end{array} \right) } \left( { \begin{array} { l } { x _ { 1 } } \\ { x _ { 2 } } \\ { x _ { 3 } } \end{array} } \right) = { \left( \begin{array} { l } { 1 } \\ { 0 } \\ { 1 } \end{array} \right) }
$$

# 第十一章 快速傅里叶变换

20 世纪60年代是计算复杂性研究的主要里程碑。在此十年中发现了三个非常惊人的有效算法，即两整数乘法、离散的傅里叶变换和两矩阵相乘。其中1965年Cooley和Tukey所研究出的计算离散傅氏变换(DFT)的快速傅氏变换(FFT),将计算量从 $O ( n ^ { 2 } )$ 下降到 $O \left( n \log n \right)$ ，从而使得FFT在数字信号处理、石油勘探、地震预报、医学断层诊断、编码理论、量子物理及概率论等领域中都得到了广泛的应用。长期以来,各种快速FFT的算法不断出现，成为数值代数方面最活跃的一个研究领域，而其意义远远超过了算法研究的范围，进而为诸多科技领域的研究打开了一个崭新的局面。本章先从离散傅氏变换DFT讲起，引出Cooley-Tukey著名FFT蝶式计算图;然后讨论串行FFT迭代算法和串行FFT递归算法；最后研究并行FFT算法，包括网孔连接、蝶式连接、立方连接的SIMD机器上的并行FFT算法以及超立方多计算机上的并行FFT算法。因为傅氏变换会涉及到一些复数运算，所以把其作为预备知识给出，熟悉的读者可以不必读它。

# 11.1 离散傅氏变换

# $^ { \star }$ 11.1.1预备知识

复数及其表示复数 $Z$ 一般表示为 $z = a + \mathrm { i } b$ ,其中 $\mathbf { i } = { \sqrt { - 1 } }$ 称为虚数单位， $^ { a }$ 和 $\pmb { b }$ 分别为 $\pmb { z }$ 的实部和虚部。上述 $z = a + \mathrm { i } b$ 为复数的坐标表示法；它还有三角表示法 $z = r ( \cos \theta + \mathrm { i } \ \sin \theta )$ 。因为根据台劳级数，

$$
{ \begin{array} { r l } & { \sin \theta = \theta - \theta ^ { 3 } / 3 ! + \theta ^ { 5 } / 5 ! - \theta ^ { 7 } / 7 ! + \cdots } \\ & { \cos \theta = 1 - \theta ^ { 2 } / 2 ! + \theta ^ { 4 } / 4 ! - \theta ^ { 6 } / 6 ! + \cdots } \\ & { e ^ { \mathrm { i } \theta } = 1 + \mathrm { i } \theta - \theta ^ { 2 } / 2 ! - \mathrm { i } \theta ^ { 3 } / 3 ! + \theta ^ { 4 } / 4 ! + \mathrm { i } \theta ^ { 5 } / 5 ! + \cdots } \\ & { = ( 1 - \theta ^ { 2 } / 2 ! + \theta ^ { 4 } / 4 ! + \cdots ) + \mathrm { i } ( \theta - \theta ^ { 3 } / 3 ! + \theta ^ { 5 } / 5 ! + \cdots ) } \\ & { = \cos \theta + \mathrm { i } \sin \theta } \end{array} }
$$

所以复数还可以表示为指数形式 $z = r e ^ { \mathrm { i } \theta }$ 。如果 $r = 1 , \theta = 2 \pi / n$ ,则 $z = \mathrm { e } ^ { 2 \pi \mathrm { i } / n }$

单位根与单位元根方程 $x ^ { n } - 1 = 0$ 有 $\pmb { n }$ 个根,称为 $\pmb { n }$ 次单位根。如果复数 $\pmb { \omega }$ 是 $\pmb { n }$ 次单位根， $( \omega ^ { n } - 1 = 0 )$ ，则 $\omega ^ { k } ( k$ 为整数)也一定是 $\pmb { n }$ 次单位根,因为$( \omega ^ { k } ) ^ { n } = ( \omega ^ { n } ) ^ { k } = 1 ^ { k } = 1$ 。显然 $\omega ^ { n } - 1 = 0$ 有 $\pmb { n }$ 个根,如果这 $\pmb { n }$ 个根 $1 , \omega ^ { 1 } , \omega ^ { 2 } , \cdots ,$ $\omega ^ { n - 1 }$ 都不同,则称 $\omega ^ { 1 }$ 为 $\pmb { n }$ 次单位元根(Princ ipal nth Root of Unity）。显然$\omega = e ^ { 2 \pi \mathrm { i } / n }$ 是一个 $\pmb { n }$ 次单位元根。注意,不是所有的 $\pmb { n }$ 次单位根都可以称为 $\pmb { n }$ 次单位元根。例如,1是 $\pmb { n }$ 次单位根,但不是 $\pmb { n }$ 次单位元根。

在离散的傅氏变换中所定义的 $\pmb { \omega }$ 正好是一个 $\pmb { n }$ 次单位元根。

例11.1 如图11.1, $\pmb { n = 8 }$ 则有8个不同的8次单位根,其中 $\omega ^ { 1 }$ 为8次单位元根：

$$
\omega ^ { 1 } = \mathrm { e } ^ { 2 \pi \mathrm { i } / 8 } = \mathrm { e } ^ { \mathrm { i } \pi / 4 } = \cos { \frac { \pi } { 4 } } + \mathrm { i } \sin { \frac { \pi } { 4 } } = { \frac { \sqrt { 2 } } { 2 } } + \mathrm { i } { \frac { \sqrt { 2 } } { 2 } }
$$

$$
\begin{array} { r l } & { \quad _ { \pm } ^ { \pm } = ( e ^ { 2 \pi i \Phi } ) ^ { 2 } = \mathrm { e } ^ { i \pi / 2 } = \cos { \frac { \pi } { 2 } } + \mathrm { i } \sin { \frac { \pi } { 2 } } = 0 + \mathrm { i } } \\ & { \quad _ { \pm } ^ { 3 } = \omega ^ { 2 } \cdot \omega ^ { 1 } = \cos { \frac { 3 } { 4 } } \pi ^ { 4 } + \mathrm { i } \sin { \frac { 3 } { 4 } } \pi = - \frac { \sqrt { 2 } } { 2 } + \mathrm { i } \frac { \sqrt { 2 } } { 2 } } \\ & { \quad _ { \pm } ^ { 4 } = \omega ^ { 2 } \cdot \omega ^ { 2 } = \cos \pi + \mathrm { i } \sin \pi = - 1 + 0 } \\ & { \quad _ { \pm } ^ { 5 } = \omega ^ { 1 } \cdot _ { \omega ^ { 4 } } = \cos { \frac { 5 } { 4 } } \pi + \mathrm { i } \sin { \frac { 5 } { 4 } } \pi = - \frac { \sqrt { 2 } } { 2 } - \mathrm { i } \frac { \sqrt { 2 } } { 2 } } \\ & { \quad _ { \omega ^ { 6 } } = \omega ^ { 2 } \cdot _ { \omega ^ { 4 } } = 0 - \mathrm { i } } \\ & { \quad _ { \omega ^ { 7 } } = \omega ^ { 4 } \cdot _ { \omega ^ { 3 } } = \frac { \sqrt { 2 } } { 2 } - \mathrm { i } \frac { \sqrt { 2 } } { 2 } } \\ & { \quad _ { \omega ^ { 8 } } = \omega ^ { 4 } \cdot _ { \omega ^ { 8 } } = 1 + 0 \quad \Omega } \end{array}
$$

![](images/2f21e0d11990ac74515298431527839e03c31ae28c52cad3b9818088d48c1a97.jpg)  
图11.18次单位元根及其它的8次单位根

单位根的性质 $\textcircled{1}$ 对于 $n \geqslant 2 , \sum _ { k = 0 } ^ { n - 1 } \omega ^ { k } = 0 ; \textcircled { 2 } \omega ^ { n } = 1 , \omega ^ { n / 2 } = - 1 ; \textcircled { 3 } \omega ^ { s n + p } =$ $\omega ^ { p } { \big ( } s \circ \cdot n \cdot p$ 为正整数)。

# 11.1.2离散傅里叶变换

一个n 点离散傅里叶变换(Discrete Fourier Transform）,简记之为DFT,可定义