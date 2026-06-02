单独的进程和通信的个体活动，它采用各进程延迟通信的办法，将诸消息组合成一个尽可能大的通信实体施行选路传输，这就是所谓的整体大同步。它简化了算法(程序)的设计和分析，当然就牺牲了运行时间，因为延迟通信意味着所有的进程均必须等待最慢者。一种改进的办法是采用子集同步,即将所有的进程按快、慢程度分成若干个子集,于是整体的大同步就演变为子集内的同步。如果子集小到其中只包含成对的发/收者,则它就变成了异步的个体同步,这就是 logP模型了。也就是说,如果BSP中考虑到个体通信所造成的开销(Overhead)而去掉路障(Barrier)同步就变成了 $\mathrm { l o g P }$ ,即

$$
\mathrm { B S P + O v e r h e a d - B a r r i e r = l o g P }
$$

BSP 成本模型在 BSP的一个超级计算步中,其计算模型如图4.3所示。按此可抽象出 BSP的成本模型如下：

![](images/f5d9e76700cd655bb14771ccd73cd5b04b3df6613670cba7649286ef511ecdbc.jpg)  
图4.3BSP一个超级计算步中的计算模式

一个超级计算步成本 $= \operatorname* { m a x } \left\{ w _ { i } \right\} + \operatorname* { m a x } \left\{ h _ { i } g \right\} + L$ Processes

其中， ${ \boldsymbol { \ w } } _ { i }$ 是进程 $i ( \mathrm { P r o c e s s } _ { i } )$ 的局部计算时间， $h _ { i }$ 是 $\mathrm { P r o c e s s } _ { i }$ 发送或接收的最大信包数， $\pmb { g }$ 是带宽的倒数(时间步/信包)， $L$ 是路障同步时间(注意,在BSP 成本模型中并未考虑到I/O的传送时间)。所以,在BSP计算中,如果用了s个超级计算步,则总的运行时间为：

$$
T _ { \mathrm { B S P } } = \ \sum _ { i = 0 } ^ { s - 1 } \ w _ { i } + g \ \sum _ { i = 0 } ^ { s - 1 } \ h _ { i } + s L
$$

BSP的大同步机理BSP模型的创始人L.G.Valiant曾从理论上论证并行计算不必优化在单一消息级(Single-Message Level),他认为整体大同步能大大简化并行计算(算法和编程)的设计、分析、验证、性能预测和具体实现,而基于成对消息传递的个体异步并行计算(例如logP模型),在时间上的得益比起对计算性能上难以分析和预测来说，并不合算。目前，对BSP模型的质疑主要集中在两点，即延迟通信至某一特定点和频繁的路障同步，会不会造成性能下降和使成本过于昂贵。BSP模型的支持者们对这两个问题进行了研究，回答是：延迟通信能提供更多的优化通信的机会，采用组合小的消息和全局通信调度能减少拥挤和竞争;路障同步对共享存储结构是不太费时的，而对分布存储的结构，主要是目前低层软件绝大多数都不支持访问相应的硬件，所以比较昂贵，但不管怎样，路障同步所造成的成本可折合到全局通信中而予以部分地抵销。

BSP 和logP相互比较 $\textcircled{1}$ 现今最流行的并行计算模型是BSP和logP,已经证明两者本质上是等效的，且可以相互模拟：用BSP去模拟logP所进行的计算时,通常会慢常数倍,而用logP去模拟BSP所进行的计算时，通常会慢对数倍；$\textcircled{2}$ 直观上讲,BSP为算法(和程序)提供了更多的方便,而 logP却提供了较好的机器资源的控制； $\textcircled{3} \textcircled { 1 } \textcircled { \mathbf { S } } \mathbf { P }$ 所引起的精确度方面的损失比起其所提供的更结构化的编程风格的优点来是小的； $\textcircled{4}$ 总之,BSP模型在简明性、性能的可预测性、可移植性和结构化可编程性等方面更受人欢迎和喜爱。

# 4.3 小结和导读

小结并行计算模型是设计和分析并行算法的基础。PRAM模型由于过于抽象而不能很好地反映并行算法的实际运行性能，所以研究考虑通信、同步等因素的从而能较真实反映并行算法运行性能的所谓更实际的计算模型（MoreRealisticComputation Models)成为当今并行算法研究的主要动向之一。本节所讨论的APRAM、BSP、logP 和 ${ \sf C } ^ { 3 }$ 等模型就是属于这种模型。但过去几年来，主要是从理论分析的角度,来研究它们之上的一些典型的并行算法的设计与分析；而近期的研究热点却从这些模型上的算法研究转向这些模型的编程的研究，即从理论研究转向实际应用。因为任何并行算法的应用都最终落实到具体的编程上,所以这种转变是顺应应用要求的。例如，一些研究者就为BSP模型构造了一些函数库,这些BSP库就是一些为程序员编写BSP应用程序(这些应用程序按照 BSP的超级计算步的风格进行编写)所提供的一组简单有力的编程界面函数,此函数可改善程序的可移植性而不依赖于具体的并行机结构。尽管PVM和 MPI等也是目前可供使用的开发可移植并行代码的方法，但它们的功能过于复杂而不易被掌握，且它们均没有为编程者提供能设计高效代码的成本函数，而像BSP模型却提供了简单和可定量分析程序运行时间的成本函数。因此研究基于这些实用计算模型的并行编程方法是非常有意义的。

最后,将本章所讨论的几种并行计算模型综合比较于表4.5中。

表4.5并行计算模型综合比较一览表  

<table><tr><td rowspan=1 colspan=1>模型属性</td><td rowspan=1 colspan=1>PRAM</td><td rowspan=1 colspan=1>APRAM</td><td rowspan=1 colspan=1>BSP</td><td rowspan=1 colspan=1>logP</td><td rowspan=1 colspan=1>C</td></tr><tr><td rowspan=1 colspan=1>体系结构</td><td rowspan=1 colspan=1>SIMD-SM</td><td rowspan=1 colspan=1>MIMD-SM</td><td rowspan=1 colspan=1>MIMD-DM</td><td rowspan=1 colspan=1>MIMD-DM</td><td rowspan=1 colspan=1>MIMD-DM</td></tr><tr><td rowspan=1 colspan=1>计算模式</td><td rowspan=1 colspan=1>同步计算</td><td rowspan=1 colspan=1>异步计算</td><td rowspan=1 colspan=1>异步计算</td><td rowspan=1 colspan=1>异步计算</td><td rowspan=1 colspan=1>异步计算</td></tr><tr><td rowspan=1 colspan=1>同步方式</td><td rowspan=1 colspan=1>自动同步</td><td rowspan=1 colspan=1>路障同步</td><td rowspan=1 colspan=1>路障同步</td><td rowspan=1 colspan=1>隐式同步</td><td rowspan=1 colspan=1>路障同步</td></tr><tr><td rowspan=1 colspan=1>模型参数</td><td rowspan=1 colspan=1>1（单位时间步）</td><td rowspan=1 colspan=1>d,Bd:读/写时间B:同步时间</td><td rowspan=1 colspan=1>p,g,lp：处理器数g：带宽因子l:同步间隔</td><td rowspan=1 colspan=1>l,0,g,pl:通信延退0:额外开销g：带宽因子p:处理器数</td><td rowspan=1 colspan=1>l,s,h1：信包长度s:发送建立时间h：通信延迟</td></tr><tr><td rowspan=1 colspan=1>计算粒度</td><td rowspan=1 colspan=1>细粒度/中粒度</td><td rowspan=1 colspan=1>中粒度/大粒度</td><td rowspan=1 colspan=1>中粒度/大粒度</td><td rowspan=1 colspan=1>中粒度/大粒度</td><td rowspan=1 colspan=1>粗粒度</td></tr><tr><td rowspan=1 colspan=1>通信方式</td><td rowspan=1 colspan=1>读/写共享变量</td><td rowspan=1 colspan=1>读/写共享变量</td><td rowspan=1 colspan=1>发送/接收消息</td><td rowspan=1 colspan=1>发送/接收消息</td><td rowspan=1 colspan=1>发送/接收消息</td></tr><tr><td rowspan=1 colspan=1>编程地址空间</td><td rowspan=1 colspan=1>全局地址空间</td><td rowspan=1 colspan=1>单一地址空间</td><td rowspan=1 colspan=1>单地址/多地址空间</td><td rowspan=1 colspan=1>单地址/多地址空间</td><td rowspan=1 colspan=1>多地址空间</td></tr></table>

导读关于并行算法的设计和分析,读者可阅读[191]。最基本的PRAM模型来源于[65];推广的PRAM模型有存储竞争模型[108],延迟模型[138],局部PRAM[5],分层存储模型[11]等。关于更实际的并行计算模型综合介绍，读者可参阅[192];更为详细者,包括APRAM[76],BSP[176], $\mathrm { l o g P } [ 5 5 ]$ 和 $\mathbf { C } ^ { 3 } [ \mathbf { 8 } 7 ]$ 。关于并行计算模型的定量比较,读者可参阅[106]。对 BSP模型的质疑和回答，读者可参阅[162];有关 BSP 的函数库,读者可参阅[80,81]。如何使用 BSP模型进行编程,读者可参阅[82];如何使用大同步进行并行计算,读者可参阅[46]。

# 习 题

4.1试证明：

(1)如果 $f ( n ) = 1 0 n$ ，则 $f ( n ) = O ( n )$ 。

（2）如果 $f ( n ) = { \frac { 1 } { 3 } } n ^ { 3 } + { \frac { 1 } { 2 } } n ^ { 2 } + { \frac { 1 } { 6 } } n$ ，则 $f ( n ) = O ( n ^ { 3 } )$

(3）如果 $f ( n ) = n ^ { 2 } / 5$ ,则 $f ( n ) = \Omega ( n ^ { 2 } )$ 。

（4)如果 $f ( n ) = 0 . 0 0 1 n ^ { 2 }$ ，则 $f ( n ) = \Omega ( n ^ { 2 } ) ,$

4.2试证明 ${ \frac { 1 } { 2 } } n ^ { 2 } - 3 n = \Theta { \left( n ^ { 2 } \right) } ,$

[提示：按照紧致界 $\Theta ( \cdot )$ 的定义,求出满足要求的 ${ \pmb n } _ { \pmb 0 } \setminus { \pmb C } _ { 1 }$ 和 $c _ { 2 }$ 之值。]

4.3试证明 Brent定理：令 $\mathbf { { \cal { W } } } ( n )$ 是某并行算法 $\pmb { A }$ 在运行时间 $T ( n )$ 内所执行的运算数量，则 $A$ 使用 $\pmb { \mathscr { P } }$ 台处理器可在 $t ( n ) = O ( W ( n ) / p + T ( n ) )$ 时间内执行完毕。

4.4试分析算法4.2的执行过程。

4.5假定 $\bar { \mathsf { P } } _ { i } ( 1 { \leqslant i } { \leqslant n } )$ 开始时存有数据 $d _ { i }$ ，所谓累加求和系指用 $\sum _ { j = 1 } ^ { i } d _ { j }$ 来代替 $\mathtt { P } _ { i }$ 中的原始值 $d _ { i }$ 。算法4.3给出了在PRAM模型上累加求和算法：

# 算法4.3 PRAM-EREW上累加求和算法

输入： $\mathrm { \bf P } _ { i }$ 中保存有 $d _ { i }$ ：, $\iota \leqslant i \leqslant n$ 输出： $\mathrm { \bf P } _ { i }$ 中的内容为 $\sum _ { j = l } ^ { i } d _ { j }$

beginfor $j = 0$ to $\log n - 1$ dofor $i = 2 ^ { j } + 1$ to $\pmb { n }$ par-do$( \mathrm { i } ) \mathbf { P } _ { i } = d _ { i } - 2 ^ { i }$ $( \ddot { \mathrm { i } } ) d _ { i } = d _ { i } + d _ { i } - 2 ^ { j }$ endforendfor  
End(1)试用 $\pmb { n = 8 }$ 为例,按照上述算法逐步计算出累加和。  
(2)分析算法4.3的时间复杂度。

4.6在APRAM模型上设计算法时,应尽量使各处理器内的局部计算时间和读写时间大致与同步时间B相当。当在APRAM上计算n个数的和时,可以借用B叉树求和的办法。

假定有p个处理器计算n个数的和,此时每个处理器上分配n/p个数,各处理器先求出自身的局和;然后从共享存储器中读取它的B个孩子的局和，累加后置人指定的共享存储单元SM中;最后根处理器所计算的和即为全和。算法4.4示出了APRAM上的求和算法：

# 算法4.4 APRAM上求和算法

输入： $\pmb { n }$ 个待求和的数

输出：总和在共享存储单元SM中

# Begin

（1）各处理器求n/p个数的局和,并将其写人SM中(2) Barrier(3） for k=「logB(p(B-1)+1)]-2 downto 0 do(3.1) for all $\mathrm { \bf P } _ { i }$ $\bullet { \leqslant } i { \leqslant } p - 1$ ,d

if $\mathrm { P } _ { i }$ 在第 $k$ 级 then$\mathbf { P } _ { i }$ 计算其B个孩子的局和并与其自身局和相加,然后将结果写入SM中endifend for(3.2） Barrierend for

End

(1)试用APRAM模型之参数,写出算法的时间复杂度函数表达式。  
(2)试解释Barrier语句的作用。

4.7欲在BSP模型上计算 $_ { n }$ 个数的和，可以在 $^ { d }$ 叉树上进行。假定用 $\pmb { \mathscr { P } }$ 个处理器求 $\pmb { \mathscr { n } }$ 个数的和,则每个处理器分配有 $\pmb { n } / \pmb { \mathscr { p } }$ 个数。首先,各处理器求 $\pmb { n } / \pmb { p }$ 个数的局和;然后在 $^ d$ 叉树上自下而上求全和,其全过程如算法4.5所示。

# 算法4.5 BSP上求和算法

输入： $\pmb { n }$ 个待求和的数输出：总和在根处理器 ${ \bf P _ { 0 } }$ 中

#

Begin(1） for all $\mathbf { P } _ { i }$ $\scriptstyle \bigwedge _ { i } , 0 { \leqslant } i { \leqslant } p - 1 \ \mathbf { d } \mathbf { 0 }$ $\big / \star$ 各处理器求各自局和 $\star$ /(1.1) $\mathbf { P } _ { i }$ 计算 $\pmb { n } / \pmb { \mathscr { p } }$ 个数的局和(1.2) if $\mathtt { P } _ { i }$ 在第 $\lceil \log _ { \mathsf { B } } ( \phi ( B - 1 ) + 1 ) \rceil - 1$ 级 then$\mathrm { \bf P } _ { i }$ 将其局和发往父节点endifendfor(2） Barrier(3） ${ \mathrm { f o r ~ } } k = \lceil \log _ { B } ( { \boldsymbol { \beta } } - 1 ) + 1 ) \rceil - 2$ downto 0 do $\big / \ast$ 上播并求和 $\bigstar$ /(3.1) for all $\mathrm { \bf P } _ { i }$ $\ u _ { i } , 0 { \leqslant } i { \leqslant } p - 1$ doif $\mathbf { P } _ { i }$ 在第 $_ r$ 级 then$\mathbf { { P } } _ { i }$ 接收 $^ { d }$ 个孩子消息,并将它们与其本身局和相加;然后将结果发往父节点endifendfor(3.2） Barrierendfor  
End

(1)试分析算法4.5的时间复杂度。

$( 2 ) d$ 值如何确定？

4.8在给定时间 $\pmb { t }$ 内，尽可能多的计算输入值的和也是一个求和问题。如果在 $\scriptstyle \log \bar { \mathbf { P } }$ 模型上求此问题时,要是 $t < L + 2 { \cdot } 0$ ,则在一个单处理机上即可最快地完成；要是 $t > L + 2 \cdot 0$ 时,则根处理器应在 ${ \pmb t - 1 }$ 时间完成局和的接收工作，然后用一个单位时间完成加运算而得最终的全和。而根的远程子节点应在 $( t - 1 ) - ( L + 2 { \cdot } 0 )$ 时刻开始发送数据，其兄妹子节点应依次在 $\left( t - 1 \right) - \left( L + 2 { \cdot } 0 + g \right) , \left( t - 1 \right) - \left( L + 2 { \cdot } 0 + 2 g \right)$ ,…时刻开始发送数据。图4.4示出了 $\scriptstyle t = 2 8 , { \boldsymbol { \phi } } = 8 , L = 5 , \sigma = 2 , g = 4$ 的 $\scriptstyle \log \bar { P }$ 模型上的通信(即发送/接收)调度树。试分析此通信调度树的工作原理和图中节点中的数值是如何计算的？

$$
\begin{array} { r } { \overbrace { \bigodot \mathrm { P } _ { 1 } \bigoplus _ { \mathfrak { p } _ { 1 } } \mathrm { P } _ { 2 } \underbrace { \left( 1 ^ { 0 } \right) \mathrm { P } _ { 2 } \overbrace { \bigcirc \mathrm { P } _ { 3 } \overbrace { \bigcirc \mathrm { P } _ { 3 } \overbrace { \bigcirc \mathrm { P } _ { 4 } \overbrace { \bigcirc \mathrm { P } _ { 5 } \overbrace { \bigcirc \mathrm { P } _ { 6 } } } } } ^ { \bigcirc \ \ { \mathrm { P } _ { 6 } \large } } } } } ^ { \bigotimes \ \ \mathrm { P } _ { 0 } } } \end{array}
$$

图4.4 $\pmb { t = 2 8 }$ ， $\pmb { \hat { p } = 8 }$ ,L=5, $\scriptstyle \pmb { o } = 2$ ， $g = 4$ 的通信调度树

4.9按照图4.4通信调度树,在logP模型上的处理器进行连续接收和发送时必须相间时间间隔g,但可以用通信开销。和计算局和的时间来填充,从而可掩盖g的开销。一般而言,对于某处理器,若它有k个子节点，则它必须接收k个消息，所以至少要k（g－o）次局部加法来填充所有的g,因此在它接收k个消息中,至少要作.k(g－o-1)次自身内部数的加法来填充，这样才能充分掩盖g的开销。图4.5示出了按照图4.4所示的通信调度树时的计算时间调度图。试分析此计算调度图的工作原理和处理器Po与Ps填充计算情况。

![](images/78f1459ecb0d8492ec117e3112209578c2352d3bc5451cb4469b005257ac3d1c.jpg)  
图4.5 $\scriptstyle t = 2 8 , \phi = 8 , L = 5 , o = 2 , g = 4$ 的计算调度图

4.10试分析如下用 BSPLib并行求4个整数1,2,3,4的前缀和的过程(参见图4.6)。

![](images/750e321bd25c21c7aa17dc543c55182fd296f23fc8fe1d72d725ca686a0ee5e0.jpg)  
图4.6求整数1,2,3,4的前缀和过程

# $/ / \ast$ 用BSPLib求前缀和 $\pmb { \mathscr { k } }$ //

# include "bsp.h" int bsp._ allsums(int $_ { x }$ ） int i,left,right;

bsp-push-reg(&right,sizeof(int));   
bsp-push-reg(&letf,sizeof(int));   
bsp- sync();

right $\mathbf { \mu } = \mathbf { x }$ $\mathbf { f o r } ( i = 1 ; i < \mathrm { b s p } _ { - } \mathrm { n p r o c s } ( ) ; i \neq - 2 ) \left\{ \begin{array} { r l } \end{array} \right.$ if (bsp-pid() $^ +$ i<bsp- nprocs()) bsp-put(bsp-pid()+i,&right,&left,0,sizeof(int); bsp-sync(); ${ \mathrm { ~ ( b s p - p i d ( \lambda ) > \lambda } } = i { \mathrm { ~ ) ~ } } { \mathrm { ~ r i g h t = l e f t + r i g h t ; } }$ ！ bsp-pop-reg(&right); bsp-pop-reg(&left); returm right; 一 void main( bsp-begin(bsp-nprocs()); printf("On %d sum is %d\n",bsp-pid(),bsp-allsums( $1 +$ bsp- pid())); bsp-end(); ！

# 第五章 并行算法的一般设计方法

设计并行算法一般有三种方法： $\textcircled{1}$ 检测和开拓现有串行算法中的固有并行性而直接将其并行化,这种方法虽不是对所有问题总是可行的，但对很多应用问题仍不失为一种有效的方法； $\textcircled{2}$ 从问题本身的描述出发，根据问题固有的属性，从头开始设计一个全新的并行算法，这种方法虽有一定的难度;但所设计的并行算法通常是高效的； $\textcircled{3}$ 借用已有的并行算法使之可求解新的一类问题，这种方法对于一个初学者来说似乎有一定的难度，但对一个有经验的算法设计者来说有可能产生一个很优秀的并行算法。但是,并行算法的设计是复杂的且在发展中，目前尚无一套普遍适用的系统的设计方法。

# 5.1 串行算法的直接并行化

# 5.1.1设计方法描述

长期以来人们积累了大量优秀的串行算法，这是一批宝贵的财富。在设计并行算法时,要充分利用现有求解问题的串行算法,在其基础上而直接并行化,这显然是设计并行算法时一种优先考虑的方法。但使用这样方法时有两点需要考虑： $\textcircled{1}$ 对于一类具有内在顺序性的串行算法,则恐难于直接并行化。例如在某串行算法执行步中，每一步都要用到上一步的计算结果,则显然这样的串行算法步无法并行执行； $\textcircled{2}$ 并非任何优秀的串行算法都可以产生好的并行算法,相反一个不好的串行算法则有可能产生很优秀的并行算法。例如,枚举串行算法，显然是一种复杂度高的被视为不好的串行算法类,但其直接并行化所产生的并行算法则可能获得低复杂界的优秀的并行算法。所以，并不是说一个优秀的串行算法并行化后总能产生相应的好的并行算法。最后也须说明，直接并行化也并非想象的那样简单、直接。直接并行化的关键步是分析数据执行时的相关性以及检测算法结构的固有串行性。有时为了并行化，将原串行算法不作本质性修改也是需要的,例如调整执行顺序,复制共享变量等。

大家知道,科学和工程问题中的数值计算问题,依据其数值分析数学原理而产生了很多广泛使用的串行算法，在设计这些问题的并行算法时大多都是采用串行算法直接并行化的方法，这样诸如算法的稳定性、收敛性等复杂问题,在直接并行化后的算法中均无需考虑,这恐怕也是为什么现今的数值并行算法大都是已有串行算法直接并行化的结果的原因吧。

有关并行数值算法，本书专辟了第三篇进行了讨论，读者在学习后就会发现,在那些章节里的很多并行数值问题的算法都是已有的串行算法直接并行化的结果。下面举一个非数值串行算法直接并行化的例子。

# 5.1.2快排序算法的并行化

串行快排序 快排序(Quicksort)是常用的串行排序算法之一，虽然其最坏情况下的复杂度为 $O ( n ^ { 2 } )$ ,但其具有较好的平均复杂度 $\Theta \left( \pi \mathrm { l o g } n \right)$ 。快排序是基于分治策略的递归排序方法。其算法分为两步：首先将一个序列 $\left( A _ { q } , \cdots , A _ { r } \right)$ 分成两个非空子序列 $( A _ { q } , \cdots , A _ { s } )$ 和 $( A _ { s + 1 } , \cdots , A _ { r } )$ ,其中前一个子序列中的任一元素都小于等于后一个子序列中的任意元素;然后对该两子序列施行递归调用。此递归调用过程直至子序列中仅有两个元素为止。

如何按上述要求将一个序列划分成两个子序列？通常的办法是从（A,…,$A _ { r }$ )中选择一划分元素 $_ { x }$ ,也称之为主元(Pivot),由其将原序列划分成满足上述要求的两个子序列,选取此元素 $_ { _ x }$ 最简易的办法就是将 $( A _ { q } , \cdots , A _ { r } )$ 中的第一个元素作为主元。下面给出串行快排序的形式描述(算法5.1)：

算法5.1 SISD上快排序算法

输入：无序序列 $( A _ { q } , \cdots , A _ { r } )$   
输出：有序序列 $( A _ { q } , \cdots , A _ { r } )$   
Procedure QUICKSORT $( A , q , r )$   
Begin if $q < r$ then (1) $x = A _ { q }$ (2） $\mathbf { \vec { s } } = \mathbf { \vec { q } }$ (3) for $i = q + 1$ to $r$ do if $A _ { i } { \leqslant } x$ then (i) $\begin{array} { r } { s = s + 1 } \end{array}$ (ii $) \mathbf { \ s w a p } ( A _ { s } , A _ { i } )$

# endif

(4） swap $( A _ { q } , A _ { s } )$ （5）QUICKSORT $( A , q , s )$ （6）QUICKSORT $( A , s + 1 , r )$

# endif

# End

对于长度为 $\pmb { n }$ 的序列，在最坏情况下所划分的两个子序列长度分别为 $_ n -$ 1和1,相应的运行时间为 $t \left( n \right) = t \left( n - 1 \right) + \theta \left( n \right)$ ,其解为 $t \left( n \right) = \Theta { \left( n ^ { 2 } \right) }$ ；理想的情况是所划分的两个子序列等长，相应的运行时间为 $t \left( \pi \right) = 2 t \left( n / 2 \right) +$ $\Theta ( \mathfrak { n } )$ ,其解为 $t \left( n \right) = \Theta \left( n \ \log n \right)$ 。

快排序的并行化分析算法5.1,一种很自然的并行化方法是并行地调用快排序对两个所划分的子序列进行快排序(算法5.1.的第(5)和第(6)步)。这种并行化的方法并不改变串行算法本身的属性，所以将其很容易改写成并行执行的形式。但是用n个处理器排序n个数,如用一个处理器将(Ai,,A)划分成 $( A _ { 1 } , \cdots , A _ { s } )$ 和 $( A _ { s + 1 } , \cdots , A _ { n } )$ 是不会得到成本最优算法的，因为单是划分时间就是 $\Omega ( n )$ ,所以 $C ( n ) = \phi \left( n \right) \cdot t \left( n \right) = \Omega { \left( n ^ { 2 } \right) }$ 。可见只有将划分步(算法5.1的第(3)步)也进行并行化才有可能得到成本最优的算法。下面给出基于二叉树的并行选主元的 PRAM-CRCW模型上的快排序算法。

PRAM-CRCW上快排序算法 执行快排序可以看成是构造一棵二叉树，其中主元是根，小于等于主元的元素处于左子树，大于主元的元素处于右子树。算法首先从选第一个主元开始，它划分原序列为两个子序列;然后相继子序列中主元的选取则可并行执行。当这样的二叉树造好后，采用中序遍历的方法就可得到一个有序序列。令待排序的序列为（A,,A),处理器P;保存元素A;,LC[1:n]和RC[1:n]分别记录给定主元的左儿子和右儿子,fi中存有其元素是主元的处理器号。开始时所有处理器均将它们的处理器号写向变量root，但根据CRCW模型原理，最终只有一个处理器号写人变量root。Aroot中是第一个主元，并且root被复制给每个处理器i的f，然后那些其元素小于Af的处理器将其号码写人 $L C _ { f _ { i } }$ ,而大于 $A _ { f _ { i } }$ 的处理器将其号码写人 $R C _ { f _ { i } }$ 。因此所有那些其元素属于小序列的处理器便将其号码写人LCf,而所有那些其元素属于大序列的处理器便将其号码写人RCs。但是因为并发写操作只有两个值（一个对应于$L C _ { f _ { i } }$ ,另一个对应于 $R C _ { f _ { i } }$ )能被写进这些单元,所以这两个值就变成了下次迭代所需的主元的处理器号。按此算法一直继续到n个主元被选完。

# 算法5.2 PRAM-CRCW上为快排序构造二叉树算法

输入：序列 $( A _ { 1 } , \cdots , A _ { n } )$ 和 $\pmb { n }$ 个处理器

输出：供快排序用的一棵二叉树

# Begin

(1） for each processor $\textbf { \em i }$ do (1.1) $\mathfrak { r o o t } = \mathfrak { i }$

(1.2) $f _ { i } = { \mathrm { \bf { r o o t } } }$ (1.3) $L C _ { i } = R C _ { i } = n + 1$

# endfor

(2） repeat for each processor iroot ·do $\mathbf { i f } ( A _ { i } < A _ { f _ { i } } ) \lor ( A _ { i } = A _ { f _ { i } } \land i < f _ { i } ) \mathbf { t h e n }$ (2.1) $L C _ { f _ { i } } = i$ (2.2) if $i = L C _ { f _ { i } }$ then exit else $f _ { i } = L C _ { f _ { i } }$ endif else (2.3) $R C _ { f _ { i } } = i$ (2.4) if $\therefore R C _ { f _ { i } }$ then exit else $f _ { i } = R C _ { f _ { i } }$ endif endif end repeat

End

在算法每次迭代时,可在 $\Theta ( 1 )$ 时间内构造一级树,而树高为 $\Theta ( \log n )$ ,所以算法5.2的时间复杂度为 $\Theta ( \log n )$ 。

# 5.2从问题描述开始设计并行算法

对于有些问题,现有的串行算法恐难直接将其并行化,此时要从问题的描述出发,寻求可能的新途径,设计出一个新的并行算法。但这并不是说完全排除某些串行算法设计的基本思想,而是更着重从并行化的具体实现上开辟新的设计方法。本节拟以串匹配问题为例,来阐述这种设计方法。

# 5.2.1串匹配算法

定义5.1由字符集Σ(字符的非空有穷集合)中的字符所组成的任何有穷序列称之为串(又叫字符串)。串中包含的字符个数称为串的长度。

定义5.2给定长度为 $\pmb { n }$ 的正文串 text 和长度为 $_ { m }$ 的模式串pat( $\pmb { m } \leqslant$ $\pmb { n }$ ),欲找出 pat 在text 中出现的所有位置 $\pmb { i }$ ，如果找到就称之为匹配。

在以下的讨论中,约定 pat 和 text均以数组形式表示。按此,pat 出现在text的i位置,指的是 pat=text[i:i+m-1],此时则定义match(i)= true,否则定义match(i)=false。在下文中,为了书写方便,常将 text和pat也分别写作$T$ 和 $P$ 。

串匹配问题在诸如文字和图像处理中经常使用,是复杂性理论中最广泛研究的问题之一。串匹配问题的一种平易算法是把它视为以pat为键的搜索问题，即长度为 $\pmb { n }$ 的text可分成 $\pmb { n } - \pmb { m } + 1$ 个长度为 $\pmb { m }$ 的子串，检查各个子串是否与长度为 $\pmb { m }$ 的pat相匹配。这样在最坏情况下的时间复杂界为 $\left( \pmb { n } - \pmb { m } + 1 \right)$ $m = { \cal O } ( m n )$ ，所以这种古朴的串匹配算法是很少使用的。后来Knuth、Morris和Pratt三人提出了一个线性时间的经典的串匹配算法，通称之为KMP算法。但此算法一直没有发表,直至Boyer和 Moore两人也提出了设计串匹配的新算法时，这两种算法才同时发表，而相应地称后一种算法为BM算法。

目前已知的线性时间的串匹配算法均不易直接并行化，但参照串行算法的实质,结合使用申的周期数学性质却可开发出一些高效的并行串匹配算法。第一个最优的并行串匹配算法是由Galil提出，在PRAM-CRCW模型上,达到了$t \left( n \right) = O \left( \log n \right)$ 和 ${ \pmb { \mathscr { p } } } \left( \pmb { \mathscr { n } } \right) = \pmb { \mathscr { n } } \varLambda \mathrm { o g } n$ 的复杂界。后来Vishkin改进了Galil的算法,放宽了算法对字符集 $\sum$ 大小是固定的要求。可是由于Vishkin的并行算法十分复杂,所以本节只是着重介绍其设计思路(有兴趣的读者可参阅[191])。但在介绍这些内容之前,先来讨论一下KMP算法，以说明将其直接并行化的困难所在。

# \*5.2.2 KMP串行串匹配算法

定义5.3令串 $\mathbf { Y }$ 的长度为 $_ { m }$ ，如果 $Y = X ^ { k } X ^ { \prime }$ ，其中 $X ^ { k }$ 是 $\pmb { X }$ 本身重复 $\pmb { k }$ 次(k为正整数),X'是X的前缀(Prefix),则Y的子串X叫作Y的周期(Peri-od)。串Y的周期也就是Y的最短周期。如果串Y的周期长度p满足p≤m/2,则称串 $\mathbf { Y }$ 是周期的(Periodic)。

注意,在研究串匹配时，常将整个模式串(Pattern String)P本身当作正文串（Text String),而其从首字符起的子串当作模式串,这样我们如令 $D ( j )$ 是前缀P[1:j-1]的周期,其中D(1)=1,2≤j≤m+1,且P(m+1)是P中不出现的字符，则可定义模式串的失效函数(Failure Function） $\pmb { F }$ 如下：

$$
\left\{ \begin{array} { l } { F ( 1 ) = 0 } \\ { F ( j ) = j - D ( j ) \quad , \quad 2 \leqslant j \leqslant m + 1 } \end{array} \right.
$$

其几何意义如图5.1所示：(a)是为了计算失效函数的起始情况；(b)是计算的一般步骤。当P(j)=P(k)时,前移指针j和k且置F(k)=j;当P(j)≠P(k)时，则向右滑动，上面的模式使得F(j)和k对准，此时的F就是失效函数。

![](images/0d8f78b527245d988b5aaace55890ec765537baa56d68cced10a1907b80757b4.jpg)  
图5.1失效函数的确定

可以设计如下算法来计算失效函数：

# 算法5.3失效函数的计算算法

输入：模式申 $P [ 1 : m ]$

输出：失效函数 $F ( k ) , 1 { \leqslant } k { \leqslant } m + 1$

# Begin

(1) $F ( 1 ) = 0 ; F ( 2 ) = 1 ; k = 2 ; j = 1$ (2） while $k { \leqslant } m$ do

(2.1) if $P ( k ) = P ( j )$ then  
(i) $j = j + 1$   
(ii) $k = k + 1$   
(ii） $F ( k ) = j$

# endif

(2.2) if $P ( k ) { \neq } P ( j )$ then(i) $\scriptstyle { j = F ( j ) }$ (ii） if ${ \bf { j } } ^ { \mathrm { ~ } } = \bf { 0 }$ then$\begin{array} { l } { k = k + 1 } \\ { j = 1 } \\ { F ( k ) = 1 } \end{array}$ endif

# endif

# endwhile

End

显然计算 $P [ 1 : m ]$ 的失效函数可在 $O ( m )$ 时间内完成。

有了失效函数的定义，就可以讨论KMP算法了：设想模式 $P$ 置于正文 $T$ 之上,令 $P$ 向右滑动，用两指针 $j$ 和 $k$ 分别指示字符 $P ( j )$ 和 $T ( k )$ 的现行位置。开始时， $j = k = 1$ 然后分两种情况讨论： $\textcircled{1}$ 当 $P ( j ) = T ( k )$ 时,两指针前进1,且如果 $j = m + 1$ ，则表示已找到匹配，置match $\left( k - m \right) = 1 ;$ $\textcircled{2}$ 当 $P ( j ) { \neq } T ( k )$ 时，表示现行位置不匹配，应向右滑动 $P _ { j }$ 位，其下一可能的位置由如上所述的$D ( j )$ 决定，即令 $\begin{array} { r } { j = j - D ( j ) } \end{array}$ 。所以KMP算法的关键就是当模式与正文不匹配时，应如何利用已得到的“部分匹配"的结果,将模式向右滑动一段距离后再施行继续比较,这一距离可由前面所讨论的失效函数 $F ( j )$ 来决定。

# 算法5.4 KMP串匹配算法

输入： $T [ 1 { : } n ] , P [ 1 { : } m ] , F [ 1 { : } m + 1 ]$

输出：match(i)

Begin

(1) $_ { j } = 1 ; k = 1$   
(2）while $\pmb { k } - j { \leqslant } n - m$ do (2.1) if $T ( k ) = P ( j ) \mathfrak { t }$ hen (i) $k = k + 1$ (ii) ${ j = j + 1 }$ (ii)if $j = m + 1$ then match $\left( k - m \right) = 1$ endlif

# endif

(2.2) if $T ( k ) { \neq } P ( j )$ then(i) ${ \bf \nabla } _ { j } = F ( j )$ (ii） if $j = 0$ then$k = k + 1 ;$ $j = 1$ endif

# endif

# endwhile

End

显然算法5.4的时间复杂度为 $O ( n )$ 。

KMP算法的精髓在于使用了失效函数，使用它来调整两指针 $j$ 和 $\pmb { k }$ 。这种指针来回移动的办法并不太容易并行化,因为并行算法设计的基本策略是试图将 $_ T$ 串分段并行处理,但上述的KMP顺序算法很难有效地使用在分段并行处理中。

# 5.2.3并行串匹配算法的设计思路

设计并行串匹配算法的出发点设计并行串匹配算法应从何处人手呢？为此我们要从问题的描述出发，研究串匹配的基本性质。实际上，两串是否能匹配,是与串的自身前缀有关,这种前缀特性就是串的周期性(Periodicity)。所以研究串的数学性质(即周期性)是寻找并行化的一种可能的途径。

研究并行串匹配的基本方法与步骤既然串的周期特性对研究匹配是至关重要的，那么用什么量来表征它呢？为此首先引人了失配见证函数(WitnessFunction),其定义如下：

定义5.4对于给定的 $j ( 1 { \leqslant } j { \leqslant } m / 2 )$ ，如果 $P [ j : m ] \neq P [ 1 : m - j + 1 ]$ 则存在某个 ${ \pmb w } ( 1 { \leqslant } { \pmb w } { \leqslant } { \pmb m } - { \pmb j } + 1 )$ 使得 $P ( \boldsymbol { \mathbf { \ell } } _ { w } ) { \neq } P ( \boldsymbol { \mathbf { \ell } } _ { s } )$ ，其中 $\textstyle s = j - 1 + \pi$ ,记WIT$( j ) = w$ 。

于是,可以根据 $\pmb { W } \mathbb { T } ( j )$ 函数来区分申是周期的还是非周期的： $\textcircled{1}$ 对于所有$2 { \leqslant } j { \leqslant } m / 2$ ,当且仅当 $\mathbf { W I T } ( j ) { \neq } \mathbf { 0 }$ 时则串是非周期的； $\textcircled{2}$ 对于所有 $2 \leqslant j \leqslant m /$ 2,若存在某个 $\pmb { j }$ ，使得 $\mathbf { W I T } ( \ j ) = \mathbf { 0 }$ ,则串是周期的。

一旦确定了串的周期特性,则可先研究非周期串(Aperiodic String)的匹配，然后在此基础上再研究周期串的匹配。

对于非周期串匹配的研究，就是如何利用已计算出的WIT(i)快速地找出$P$ 在 $T$ 中匹配的位置。为了减少 $P$ 与 $T$ 的比较次数,引人了一种竞争(Duel)函数 $\mathsf { d u e l } ( \pmb { \mathscr { p } } , \pmb { q } )$ 的概念,即当模式在某一位置 $\pmb { \phi }$ 匹配时，则在另一位置 $\pmb q$ 一定不匹配，这样就排除了q位置。可以设计一个算法来计算duel（力，q）（参见习题5.8)。在duel(p,q)算法中,参数p,q与n,m有关,且p与q的选取应先从小范围，逐步到大范围，且在每个限定范围内可并行地求duel（p，q)，以确定竞争的幸存者。这样整个过程就像分组比赛一样，逐渐淘汰小组中的获胜者，最终只可能保留少数几个幸存者，它们就是些可能的匹配位置号码，最后再进行一次正确性验证即可。

并行串匹配算法举例为了更好地理解上述思路与步骤，现举一例说明之。

例5.1 令 T= abaababaababaababaababa(n = 23),P=abaababa （m=8)。由所计算的模式P的WIT(1)=0,WIT(2)=1,WIT(3)=2,WIT(4)=4可知P是非周期串。为了计算此非周期串与T的匹配情况,先要计算P相对于T的WIT[ $1 : n - m + 1 ]$ 之值。然后由其来计算 $\mathtt { d u e l } ( \pmb { \mathscr { p } } , \pmb { q } )$ 之值。计算 $\mathsf { d u e l } ( \pmb { \mathscr { p } } , \pmb { q } )$ 时,将 $T$ 与 $P$ 由小到大划分成一些大小为 $( 2 ^ { 1 } , 2 ^ { 2 } , \cdots )$ 的块，在相同大小的各块内并行地计算 $\operatorname { d u e l } ( p , q )$ 的值。其过程为：先将 $P$ 与 $T$ 各自划分成大小为2的一些块,这样模式块(ab)与正文块 $( \mathbf { a b } ) ( \mathbf { a a } ) ( \mathbf { b a } ) ( \mathbf { b a } ) ( \mathbf { a b } ) ( \mathbf { a b } ) ( \mathbf { a b } ) ( \mathbf { a } ) ( \mathbf { b a } )$ 进行匹配,可知在位置1,4,6,8,9,11,14和16出现匹配(即 $\operatorname { d u e l } ( \pmb { \mathscr { p } } , \pmb { q } )$ 的获胜者)；再将 $P$ 与 $T$ 各自划分成大小为4的一些块,这样模式块(abaa)与正文块(abaa)(baba)(abab)(aaba)进行匹配,可知在位置1,6,11和16出现匹配,而位置4,8,9和14被淘汰;最后需用模式(ababbaba)在正文的位置1,6,11和16进行匹配检查,以验证其正确性。□

至于周期串的匹配,情况更复杂,在此不再讨论，感兴趣的读者可参阅文献[191]。

# 5.3 借用已有算法求解新问题

# 5.3.1 设计方法描述

所谓"借用法"是指借用已知的某类问题的求解算法来求解另一类问题。此两类问题表面上看是迥然不同的,或似乎是互不相干的，所以按照常规的办法，求解这两类问题的算法似乎也毫无“亲缘"关系，因而一般初学者难以设法通过某种内在关系,将两类不同的问题在求解方法上统一起来。这实质上也正是借用法的难点所在。“借用"不是毫不费力的直接拿来使用,相反地,当欲借用时，不但要从问题求解方法的相似性方面仔细观察，寻求问题解法的共同点；而且所借来的方法要用得上算,效率要高,从而能达借用的目的。显然这并非易事。一个好的借用法所设计的算法，往往给人们带来深刻的印象，常常被教科书作为范例加以引用。

借用法虽无一般规律可循，但往往从求解问题的数学方法上能得到某种启示。例如，求一个有向图的传递闭包(TransitiveClosure)问题可以使用布尔矩阵乘法来实现,其方法如下：

假定A是一个n点有向图G的n阶布尔邻接矩阵,其矩阵元素aij为1,当且仅当有向图中从顶点i到顶点j之间有一条边时。所谓传递闭包,记之为A+,实际上也是一个n阶布尔矩阵,其矩阵元素bi为1,当且仅当：①从i到j存在一条有向边;或②对于某一顶点k,存在有向边i到k和k到j;或③i=j。按此，根据上述定义，可利用布尔矩阵乘法来求传递闭包。事实上,如令【为单位矩阵(仅对角元素为1),则(A+I)=1,表示当且仅当i和j 之间的路径长度为0(即i=j),或为1(i和j之间有一条边);(A+I)²=1,表示当且仅当i和j之间的路径长度为2或小于2;((A+I)²)²=1,表示当且仅当i和j之间的路径长度为4或小于4,…因此作 $\log n$ 次 $( A + I )$ 自乘就可求得传递闭包 $A ^ { + }$ ，因为对于 $\pmb { n }$ 点有向图， $_ i$ 和 $j$ 之间若有一路径存在,则其长度至多为 $\pmb { n }$ 。

下面将介绍一种利用矩阵乘法求所有点对间的最短路径方法，它是一种比较典型的借用已有算法来求解另一类问题的并行算法设计方法。

# 5.3.2利用矩阵乘法求所有点对间最短路径

最短路径问题有两类：一类是单源最短路径(Single-Source Shortest Path)，即在一个图中寻找从一个指定顶点到所有其它顶点之间的最短路径;另一类是所有点对间最短路径(All Pairs Shortest Paths),仅讨论后者。

定义5.5假定一有向图各边赋于非负整数权,那么一条路径的长度就是沿该路径所有边权之和；而最短路径问题就是对每一点对 $_ i$ 和 $j$ ,求找其间任何最短长度的路径。

矩阵乘法在求点对间最短路径中的应用对于一个 $\pmb { n }$ 个顶点的加权有向图 $G ( V , E )$ ,其权矩阵由 $W _ { n \times n }$ 表示。为了计算其所有顶点对之间的最短路径,可以先构造一个 $\mathbf { \Omega } _ { n } \times \mathbf { \Omega } _ { n }$ 的矩阵 $\pmb { D }$ ，使得对于所有的 $\dot { \iota }$ 和j， $d _ { i j }$ 是从 $\pmb { v _ { i } }$ 到 $\boldsymbol { v } _ { j }$ 的最短路径长度。只要 $G$ 中无负长度的环,可以假定 $\mathbf { \Delta } \mathbf { W }$ 有正、负或零元素。

令 $d _ { i j } ^ { k }$ 表示从 ${ \pmb v } _ { i }$ 到 $v _ { j }$ ,其间经过至多 $k - 1$ 个中间顶点时的最短路径长度。因此 $d _ { i j } ^ { 1 } = \tau \upsilon _ { i j }$ 。特别是从 $\boldsymbol { v } _ { i }$ 到 $\boldsymbol { v } _ { j }$ 无边存在 $( i \neq j )$ 时,则 $d _ { i j } ^ { 1 } = \infty$ 。同样 $d _ { i i } ^ { 1 } = 0 _ { \circ }$ 因 $G$ 中不存在负权的环,所以 $d _ { i j } = d _ { i j } ^ { n - 1 }$ 。

为了计算 $d _ { i j } ^ { k } \left( k > 1 \right)$ ,可以使用组合最优原理（Combinatorial OptimizationPrinciple) :

$$
d _ { i j } ^ { k } = \operatorname* { m i n } _ { l } \{ d _ { i l } ^ { k / 2 } + d _ { l j } ^ { k / 2 } \}
$$

也就是说， $d _ { i j } ^ { k }$ 取所有 $\iota$ 条路径 $( d _ { i l } ^ { k / 2 } + d _ { l j } ^ { k / 2 } )$ 中的最短者。因此矩阵 $\pmb { D }$ 就可以从$\pmb { D } ^ { 1 }$ 逐次计算 $D ^ { 2 } , D ^ { 4 } , \cdots , D ^ { n - 1 }$ ,然后取 $\pmb { D } = \pmb { D } ^ { n - 1 }$ 而求得。为了从 $\pmb { D } ^ { k / 2 }$ 计算 $\pmb { D } \pmb { k }$ ，可以使用标准的矩阵乘法,只是将原矩阵乘法中的“ $^ \bullet \times$ "操作代之以(5.2)式中的“+"操作;而将原矩阵乘法中的“∑"操作代之以(5.2)式中的“min"操作,这样的操作共执行 $\lceil \log ( n - 1 ) ^ { - }$ 次。这就是借用法中最关键之处，如果没有观察和联想到这一点,则就难以做到巧妙的借用。

SIMD-CC模型上求所有点对间最短路径算法因为本节重点是介绍借用矩阵乘法来求所有点对间的最短路径,所以有关矩阵乘法的算法就不介绍了，只是在主算法中以调用的形式来使用。关于SIMD-CC的矩阵乘法，读者可参阅本书第九章第9.4.4节的DNS乘法。

如第9.4.4节所述那样,假定n³个处理器排成n×n×n的立方体，每个处理器有A(i,j,k)、B(i,j,k)和C(i,j,k)三个寄存器。开始时A(0,j,k)=${ w _ { j k } } \left( 0 { \leqslant } j , k { \leqslant } n - 1 \right)$ 即图的权矩阵开始时存放在 $\pmb { A }$ 寄存器中；算法执行中将调用算法9.6DNS乘法，按照上述借用方法来计算所有点对间的最短路径；算法结束时， $C ( 0 , j , k )$ 中就是 ${ \pmb v } _ { j }$ 到 ${ \pmb v } _ { k }$ 的最短路径。

算法5.5 SIMD-CC上求所有点对间最短路径算法

输入： $A \left( 0 , j , k \right) = w _ { j k } , 0 { \leqslant } j , k { \leqslant } n - 1$   
输出： $C ( 0 , j , k )$ 中是 ${ \pmb v } _ { j }$ 到 ${ \pmb v } _ { { \pmb k } }$ 的最短路径长度， $\textstyle , 0 \leqslant j , k \leqslant n - 1$   
Begin

(1) $\big / \big \varkappa$ 构筑矩阵 $D ^ { 1 }$ ,并将其存人 $\pmb { A }$ 和 $B$ 寄存器中 $\yen 7$ for ${ \bf { j } } = { \bf { 0 } }$ to n -1 par - do for $k = 0$ to n -1 par- do (1.1) if $j \neq k$ & $A \left( 0 , j , k \right) = 0$ then $B ( 0 , j , k ) = \infty$ endif (1.2) $B ( 0 , j , k ) = A \left( 0 , j , k \right)$ end for end for

(2) $\curvearrowright$ 调用算法9.6构筑矩阵 $D ^ { 2 } , D ^ { 4 } , \cdots , D ^ { n - 1 } * /$ for $i = 1$ to $\lceil \log ( n - 1 ) \rceil$ do （2.1）DNS MULTIPLICATION $( A , B , C )$ $\big / \ast$ 调用算法 $9 . 6 \ast /$ (2.2) for ${ \bf { j } } = { \bf { 0 } }$ to n -1 par-do for ${ \pmb k } = { \bf 0 }$ to $n - 1 \ \mathbf { p a r } - \mathbf { d o }$ (i) $A \left( 0 , j , k \right) = C ( 0 , j , k )$ (ii) $B ( 0 , j , k ) = C ( 0 , j , k )$ end for

# end for

end for

End

显然，上述算法的时间复杂度为O(log²n)次，因为算法第(2)步重复$O ( \log n )$ 次,每次乘法时间也为 $O ( \log n )$ ，而 $\smash { p ( n ) = O ( n ^ { 3 } ) }$ 。

为了更好地理解上述算法,兹举一例如下。

例5.2试求图5.2(a)所示的有向加权图中所有点对间的最短路径,其步骤如下：

$\textcircled{1}$ 由图5.2(a)构筑邻接权矩阵如图5.2(b)所示。

![](images/844ff503c30dfefcbd704f4f062ff664362c274b343b1837a391c33e17f8bc45.jpg)  
图5.2利用矩阵乘法求所有点对间最短路径

$\textcircled{2}$ 算法开始前,用 $\boldsymbol { w } _ { j k }$ 之值初始化 $A \left( 0 , j , k \right) : A \left( 0 , 0 , 0 \right) = 0 , A \left( 0 , 0 , 1 \right) =$ $4 , A \left( 0 , 0 , 2 \right) = 1 , A \left( 0 , 0 , 3 \right) = 0 , A \left( 0 , 0 , 4 \right) = 7 , A \left( 0 , 0 , 5 \right) = 0 , x _ { 0 } = 1 2 .$ A(0,0,6)=0,A $\left( 0 , 1 , 0 \right) = 0 , A \left( 0 , 1 , 2 \right) = 8 , A \left( 0 , 1 , 3 \right) = 0 , A \left( 0 , 1 , 4 \right) = 0 , A \left( 0 , 2 , 2 \right) = 0 , A \left( 0 , 3 , 3 \right) = 0 , . $ ,1,5)=0,A(0, $1 , 6 ) = 0 , \cdots , A \left( 0 , 6 , 5 \right) = 1 , A \left( 0 , 6 , 6 \right) = 0 _ { \circ }$

$\textcircled{3}$ 由算法第(1)步计算出 $B ( 0 , j , k )$ ,它就是距离矩阵 $\pmb { D } ^ { 1 }$ （如图 ${ \mathfrak { s } } . 2 ( { \mathfrak { c } } )$ 所示）。$\textcircled{4}$ 由算法第(2)步的第1次循环计算 $\pmb { { \cal D } } ^ { 1 } \times \pmb { { \cal D } } ^ { 1 } = \pmb { { \cal D } } ^ { 2 }$ ,其中 $d _ { j k } ^ { 2 }$ 各元素计算如下：

$$
\begin{array} { l } { { d _ { 0 0 } ^ { 2 } = \displaystyle { \operatorname* { m i n } _ { 0 \leqslant t \leqslant 6 } \big \{ d _ { 0 0 } + d _ { 0 0 } , d _ { 0 1 } + d _ { 1 0 } , d _ { 0 2 } + d _ { 2 0 } , d _ { 0 3 } + d _ { 3 0 } , d _ { 0 4 } + d _ { 4 0 } , d _ { 0 5 } + d _ { 5 0 } , d _ { 0 6 } + d _ { 6 0 } , d _ { 7 } \leqslant 2 \big \} , } } } \\ { { d _ { 0 6 } + d _ { 6 0 } \big \} = 0 } } \end{array}
$$

$\begin{array} { l } { { d _ { 0 1 } ^ { 2 } = \displaystyle { \operatorname* { m i n } _ { 0 \leqslant i \leqslant 6 } \big \{ d _ { 0 0 } + d _ { 0 1 } , d _ { 0 1 } + d _ { 1 1 } , d _ { 0 2 } + d _ { 2 1 } , d _ { 0 3 } + d _ { 3 1 } , d _ { 0 4 } + d _ { 4 1 } , d _ { 0 5 } + d _ { 5 1 } \big \} } } } \\ { { \phantom { d _ { 0 1 } ^ { 2 } = d _ { 0 1 } ^ { 2 } } d _ { 0 6 } + d _ { 6 1 } \big \} = 4 } } \end{array}$ ，  
：  
$d _ { 6 6 } ^ { 2 } = \mathbf { 0 }$

$\pmb { D } ^ { 2 }$ 的整个矩阵如图5.2(d)所示。

$\textcircled{5}$ 由算法第(2)步的第2次迭代计算 $\pmb { D } ^ { 2 } \times \pmb { D } ^ { 2 } = \pmb { D } ^ { 4 }$ ，其结果如图5.2(e)所示。$\textcircled{6}$ 算法第(2)步最后一次迭代计算 $\scriptstyle D ^ { 4 } \times D ^ { 4 } = D ^ { 8 }$ ,其结果如图5.2(f)所示。□

# 5.4 小结和导读

小结设计并行算法是一件复杂的事,而并行算法的设计这门学科还属于发展中的一门学科，所以目前尚无一套普遍适用的、系统的设计方法学。本章只是给出一个非常一般的并行算法的设计方法，它不可能也不应该视为设计并行算法的全部方法。重要的是,通过所介绍的设计方法的学习,希望读者能从中得到更多的启迪,补充更多的算例,丰富、完善乃至开拓出更新更好的设计方法。

导读有关串行快排序算法,[95]和[154]是两篇很好参考文献；PRAM-CRCW上快排序算法,读者可参考[49]；超立方上的快排序算法,读者可参考[178];而网孔上的快排序算法,读者可参考[161]。有关并行串匹配算法，读者可参考[191]和[104];其中KMP算法来源于[110]和BM算法来源于[38];[72]和[177]是本章重点介绍的并行串匹配算法。有关图论问题的并行算法，[198]是本很全面的著作;本章所介绍的利用矩阵乘法求所有点对间的最短路径算法来源于[58]。

# 习 题

5.1试分析：

$\textcircled{1}$ 串行快排序算法最坏情况下的时间复杂度。  
$\textcircled{2}$ 串行快排序算法平均情况下的时间复杂度。

5.2给定序列(3,2,1,5,8,4,3,1),试用算法5.1逐步进行排序。

5.3给定序列(33,21,13,54,82,33,40,72)和8个处理器,试按照算法5.2构造一棵为在PRAM-CRCW模型上执行快排序所用的二叉树。

5.4令n是待排序的元素数,p=2d是d维超立方中处理器的数目。假定开始随机选定主元x,并将其播送给所有其它处理器,每个处理器按所接收到的x,对其n/p个元素按照≤x和>x进行划分,然后按维进行交换。这样在超立方上实现的快排序的算法如下：

# 算法5.6 超立方上快排序算法

输入： $\pmb { n }$ 个元素， $B = \pi / \beta$ ， $d = \log \phi$ 输出：按超立方编号进行全局排序

Begin

(1)u-piuwxvis lavi

(2) for $\dot { \iota } = 1$ to $^ d$ do (2.1) $\scriptstyle { \pmb { x } } = { \mathfrak { p i v o t } }$ $\big / \ast$ 选主元 $\yen 7$ (2.2）划分 $\pmb { B }$ 为 $\scriptstyle B _ { 1 }$ 和 $B _ { 2 }$ 满足 $B _ { 1 } { \leqslant } x { < } B _ { 2 }$ (2.3) if第 $\textbf { \em i }$ 位是零then (i）沿第 $\textbf { \em i }$ 维发送 $B _ { 2 }$ 给其邻者 (ii) $C =$ 沿第 $\textbf { \em i }$ 维接收的子序列 (ii） $B { = } B _ { 1 } \cup C$ else （i）沿第 $\textbf { \em i }$ 维发送 $\pmb { B _ { 1 } }$ 给其邻者 (ii) $C =$ 沿第 $\pmb { i }$ 维接收的子序列 (ii) $B = B _ { 2 } \bigcup C$

# endif

endfor

(3)使用串行快排序算法局部排序 $\scriptstyle B = n / _ { \beta }$ 个数End

$\textcircled{1}$ 试解释上述算法的原理。  
$\textcircled{2}$ 试举一例说明上述算法的逐步执行过程。

5.5令模式串 $\mathbf { { \nabla } } P =$ abcabcabcabcabcc。开始时， $j = 1$ 和 ${ \pmb k } = 2$ ，试按照算法5.3计算该模式 $\pmb { P }$ 的失效函数 $F ( 1 ) \sim F ( 1 6 )$ 。

5.6 $\textcircled{1}$ 令 $T =$ babaababaa, $\pmb { P } = \mathbf { a b } \mathbf { a b }$ ，试用算法5.4计算两者的匹配情况。$\textcircled{2}$ 试分析KMP算法为何不能简单并行化。

5.7假定 $P _ { 1 } =$ abaababa , $P _ { 2 } =$ abaabaab , $P _ { 3 } =$ abaabaaabaabab,试计算各自的 $\pmb { \ W } \pmb { \mathrm { T } } ( j )$ 函数，并判断它们的周期性。

5.8计算 $\mathbf { d u e l } ( \pmb { \mathscr { p } } , \pmb { q } )$ 函数的算法如下：

算法5.7计算串匹配的 $\mathbf { d u e l } ( \pmb { \mathscr { p } } , \pmb { q } )$ 的算法

输出：返回竞争幸存者的位置或null(表示 $\pmb { \mathscr { P } }$ 和 $\pmb q$ 之一不存在)

Procedure DUEL $( \pmb { \mathscr { p } } , \pmb { q } )$

Begin if ${ \pmb { \hat { p } } } =$ null then $\mathbf { d u e l } = \pmb q$ else if $q = \mathrm { \ n u l l }$ then duel $= \phi$ else

$$
\begin{array} { r } { j = q - p + 1 } \\ { w = \mathbf { W } \mathbf { I } \mathbf { T } ( j ) } \end{array}
$$

$$
\mathbf { W I T } ( q ) = \mathbf { \mathcal { w } }
$$

$$
\mathbf { d u e l } = \pmb { \mathscr { p } }
$$

$$
\begin{array} { l } { \displaystyle \mathtt { W I T } ( \pmb { \mathscr { p } } ) = \pmb { q } - \pmb { \mathscr { p } } + \pmb { 1 } } \\ { \displaystyle \mathtt { d u e l } = \pmb { q } } \end{array}
$$

# endif

# endif

$\textcircled{1}$ 令 $\mathbf { \nabla } T =$ abaababaababaababababa, $P =$ abaababa,试计算 $\pi \Pi ( i )$ ；  
$\textcircled{2}$ 试考虑 $\pmb { P = 6 , q = 9 }$ 的竞争情况。

5.9对于图5.2(a)的加权有向图,试用算法5.5,逐步求出 $\mathbf { D ^ { 2 } } , \mathbf { D ^ { 4 } }$ 和 $\mathbf { D } ^ { 8 }$ 中各元素 $d _ { i j } ^ { k }$

$$
\begin{array} { r l } { ( \begin{array} { c c c c c c c c } { { d _ { 0 0 } ^ { 2 } } } & { { d _ { 0 1 } ^ { 2 } } } & { { d _ { 0 2 } ^ { 2 } } } & { { d _ { 0 3 } ^ { 2 } } } & { { d _ { 0 4 } ^ { 2 } } } & { { d _ { 0 5 } ^ { 2 } } } & { { d _ { 0 6 } ^ { 2 } } } \\ { { d _ { 1 0 } ^ { 2 } } } & { { d _ { 1 1 } ^ { 2 } } } & { { d _ { 1 2 } ^ { 2 } } } & { { d _ { 1 3 } ^ { 2 } } } & { { d _ { 1 4 } ^ { 2 } } } & { { d _ { 1 5 } ^ { 2 } } } & { { d _ { 1 6 } ^ { 2 } } } \\ & & & { \vdots } & & & & & \\ & & & { \vdots } & & & & & & \\ { { d _ { 6 0 } ^ { 2 } } } & { { d _ { 6 1 } ^ { 2 } } } & { { d _ { 6 2 } ^ { 2 } } } & { { d _ { 6 3 } ^ { 2 } } } & { { d _ { 6 4 } ^ { 2 } } } & { { d _ { 6 5 } ^ { 2 } } } & { { d _ { 6 6 } ^ { 2 } } } \end{array} ) \qquad } &  ( \begin{array} { c c c c c c c } { { d _ { 0 0 } ^ { 4 } } } & { { d _ { 0 1 } ^ { 4 } } } & { { d _ { 0 2 } ^ { 4 } } } & { { d _ { 0 3 } ^ { 4 } } } & { { d _ { 0 4 } ^ { 4 } } } & { { d _ { 0 5 } ^ { 4 } } } & { { d _ { 0 6 } ^ { 4 } } } \\ { { d _ { 1 0 } ^ { 4 } } } & { { d _ { 1 1 } ^ { 4 } } } & { { d _ { 1 2 } ^ { 4 } } } & { { d _ { 1 3 } ^ { 4 } } } & { { d _ { 1 4 } ^ { 4 } } } & { { d _ { 1 5 } ^ { 4 } } } & { { d _ { 1 6 } ^ { 4 } } } \\ & & & { \vdots } & & \\ & & & & { d _ { 6 1 } ^ { 4 } } & { { d _ { 6 2 } ^ { 4 } } } & { { d _ { 6 3 } ^ { 4 } } } & { { d _ { 6 5 } ^ { 4 } } } & { { d _ { 6 6 } ^ { 4 } } } \\ & & & & { ( \mathbf { b } ) } &  D ^  4  \end{array} \end{array}
$$

$$
\left( \begin{array} { c c c c c c c } { { d _ { 0 0 } ^ { 8 } } } & { { d _ { 0 1 } ^ { 8 } } } & { { d _ { 0 2 } ^ { 8 } } } & { { d _ { 0 3 } ^ { 8 } } } & { { d _ { 0 4 } ^ { 8 } } } & { { d _ { 0 5 } ^ { 8 } } } & { { d _ { 0 6 } ^ { 8 } } } \\ { { d _ { 1 0 } ^ { 8 } } } & { { d _ { 1 1 } ^ { 8 } } } & { { d _ { 1 2 } ^ { 8 } } } & { { d _ { 1 3 } ^ { 8 } } } & { { d _ { 1 4 } ^ { 8 } } } & { { d _ { 1 5 } ^ { 8 } } } & { { d _ { 1 6 } ^ { 8 } } } \\ { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } \\ { { d _ { 6 0 } ^ { 8 } } } & { { d _ { 6 1 } ^ { 8 } } } & { { d _ { 6 2 } ^ { 8 } } } & { { d _ { 6 3 } ^ { 8 } } } & { { d _ { 6 4 } ^ { 8 } } } & { { d _ { 6 5 } ^ { 8 } } } & { { d _ { 6 6 } ^ { 8 } } } \end{array} \right)
$$

5.10对于图5.3所示的单位权有向图,试用布尔邻接矩阵乘法求出其传递闭包。

![](images/cc98eaecfc1043c955c9b6c19aa457b9c42ef719393037ada0b9f7169d2cc9a1.jpg)  
图5.3单位权有向图

# 第六章 并行算法的基本设计技术

并行算法的设计虽然是复杂的，且目前技术上尚不甚成熟，似乎又依赖于某些技巧，但也不是无章可循。随着并行算法设计学科的不断发展，人们逐渐地总结出了一些最基本的设计技术可供参考使用。从使用并行处理操作最朴素的思想出发，就可导出所谓划分设计技术，它是将一原始问题分成若干个部分，然后各部分由相应的处理器同时执行。这是最基本的设计技术,包括均匀划分技术、方根划分技术、对数划分技术和功能划分技术。从求解问题的方法学和求解策略出发，则可导出所谓分治设计技术,它是将一个大而复杂的问题分解成若干个特性相同的子问题,然后使用"各个击破"的办法逐步求解之。这是算法设计的普遍技术,既适合于串行算法的设计,又适合于并行算法的设计。从针对求解问题的特性出发，也可导出一些有效的并行算法设计技术,包括平衡树技术和倍增技术等。众所周知,流水线技术是并行处理中最基本的技术之一，它也可以被使用在并行算法的设计中，形成了流水线设计技术。本章所介绍的设计技术并非全面，同时只能作为设计并行算法的一般性指南，而不能作为可直接引用的手册。

# 6.1划分设计技术

用划分(Partitioning)法求解问题可分为两步： $\textcircled{1}$ 将给定的问题劈成 $\pmb { \mathscr { P } }$ 个独立的几乎等尺寸的子问题; $\textcircled{2}$ 用 $\pmb { \phi }$ 台处理器并行求解诸子问题。划分时关键在于如何将问题进行分组，使得子问题较容易并行求解，或者子问题的解较容易被组合成原问题的解。

# 6.1.1 均匀划分技术

假定待处理的序列长为 $\pmb { n }$ ,现有 $\pmb { \mathscr { P } }$ 台处理器，一种最基本的划分方法就是均分划分(Uniform Partition),系将 $\pmb { n }$ 个元素分割成 $\pmb { \mathscr { P } }$ 段,每段含有 $n / \phi$ 个元素且分配给一台处理器。下面以PSRS(Parallel Sorting by Regular Sampling)算法为例,来阐述均匀划分法的使用。

# 算法6.1 MIMD机器上PSRS排序算法

输入：长度为 $\pmb { n }$ 的无序序列, $\pmb { \mathscr { P } }$ 台处理器,每台处理器有 $\spadesuit / \phi$ 个元素

输出：长度为 $\pmb { n }$ 的有序序列

# Begin

（1）均匀划分： $\pmb { n }$ 个元素均匀地划分成 $\pmb { \hat { p } }$ 段,每台处理器有 $\pmb { n } / \hbar$ 个元素。  
（2）局部排序：各处理器利用串行排序算法，排序 $\scriptstyle n / \phi$ 个数。  
（3）选择样本：每台处理器各从自己的有序段中选取 $\pmb { \hat { p } }$ 个样本元素。  
（4）样本排序：用一台处理器将所有 $\scriptstyle { \pmb { \mathscr { p } } } ^ { 2 }$ 个样本元素，用串行排序算法排序之。  
(5）选择主元：用一台处理器选取 $\pmb { \hat { p } } - \pmb { 1 }$ 个主元，并将其播送给其余处理器。  
（6）主元划分：各处理器按主元将各自的有序段划分成 $\pmb { \hat { p } }$ 段。  
（7）全局交换：各处理器将其辖段按段号交换到相应的处理器。  
（8）归并排序：处理器使用归并排序将所接收的诸段施行排序。

End

算法6.1中的第(1)步是使用了均匀划分技术,从而使各段(除零头外)的规模(大小)均匀相等。算法的第(6)步也使用了划分技术,但它是非均匀的,各段的大小可能不等。

由于我们只是着重划分技术的描述,所以有关算法6.1的复杂度就不再讨论了。

例6.1示例说明 PSRS 排序过程。假定序列长度 ${ \pmb n } = 2 7$ ， $\pmb { \mathscr { p } } = 3$ ,则 PSRS排序过程如图6.1所示。□

![](images/9ecef42e6a68132f144ab82c49f1ce75bf19373049860d0fe8624fe763e0cc1f.jpg)  
图6.1例示 PSRS排序过程

# 6.1.2方根划分技术

假定待处理的序列长为 $\pmb { n }$ ，现欲将其分段处理。一种称之为平方根划分(SquareRoot Partition)的方法,就是取每第 $i \ { \sqrt { n } } \left( { \it \Omega } i = 1 , 2 , \cdots \right)$ 个元素作为划分元素而将序列划分成若干段,然后分段处理之。下面以Valiant归并算法为例，来阐述方根划分法的使用。

# 算法6.2 SIMD-EREW上 Valiant 归并算法

输入：两有序段 $\pmb { A }$ 和 $B$ 段定长度各为 $\pmb { n }$ 输出：长度为 ${ \pmb 2 } { \pmb n }$ 的有序序列

# Begin

(1）方根划分：将 $\pmb { A }$ 和 $B$ 中的第 $i \ { \sqrt { n } } \left( { i = 1 , 2 , \cdots } \right)$ 个元素作为划分元素，而将 $\pmb { A }$ 和 $B$ 分成了若干段。

(2）段间比较： $\pmb { A }$ 中所有的划分元素与 $B$ 中所有划分元素进行比较，以确定 $\pmb { A }$ 中划分元素应插入 $B$ 序列的哪一段。

(3）段内比较;A中的划分元素与其所插人的 $B$ 相应段中的元素进行比较,以确定该划分元素应插入 $B$ 相应段的哪一位置,而这些插入位置又将B重新划分成了若干段。

（4）段组归并：B被重新划分的各段与原A中相应各段构成了成对的一些段组,在各段组内,递归地执行(1)到(3)步,直到段组中某一序列长度为零为止。

End

算法6.2的第(1)步是使用了平方根划分技术，而在第(4)步的各段组内的递归调用时，各段组内的序列也使用了平方根划分技术。所感兴趣的是，这种划分技术使得算法达到了非常好的时间界。可以证明,算法6.2使用n个处理器可在 $O \left( \log \log n \right)$ 时间内完成两长度各为 $\pmb { n }$ 的有序序列的归并(见习题6.2)。

# 6.1.3对数划分技术

假定待处理的序列长为n，现欲将其分段处理。一种和上节所述的方根划分法不同的划分是对数划分（Logarithmic Partition）法，即取每第ilogn（i=1,2,…)个元素作为划分元素,而将序列划分成若干段,然后分段处理之。下面仍以两有序序列的归并为例，来阐述对数划分法的使用。

如算法6.2所示，为了确定A序列中的划分元素在B序列中的全局位序，所以划分元素必须在各段之间施行全局比较(算法6.2的第(2)步)。如果在选取 $\pmb { A }$ 序列中的划分元素时，就考虑到了它在 $B$ 序列中的全局位序，那么就不必对划分元素施行段间的全局比较，而可直接对按划分元素所断开的各段组两两进行归并，便可完成两个原序列的归并。下面所要讨论的归并算法就是基于上述思想。

定义6.1令 $X = \left( x _ { 1 } , x _ { 2 } , \cdots , x _ { t } \right) , x _ { i } \in S , S$ 为具有偏序关系的集合。所谓$\pmb { x }$ 在 $\pmb { X }$ 中的位序(Rank),记之为 $\mathbf { r a n k } ( { \boldsymbol { x } } : { \boldsymbol { X } } )$ ，就是 $\pmb { X }$ 中小于等于 $\pmb { x }$ 的元素的数目。令 $Y = \left( _ { y _ { 1 } } , _ { y _ { 2 } } \cdots , _ { y _ { s } } \right) , _ { y _ { i } } \in \mathfrak { s }$ 。所谓 $\operatorname { r a n k } ( Y { \boldsymbol { : } } X ) = ( r _ { 1 } , r _ { 2 } , \cdots , r _ { s } )$ 就是 $\mathbf { Y }$ 在 $\pmb { X }$ 中的位序，其中 $r _ { i } = \mathrm { r a n k } \left( y _ { i } : X \right)$ 。

例6.2 令 X=(25,-13,26,31,54,7), $Y = ( 1 3 , 2 7 , - 2 7 )$ ，则 $\operatorname { r a n k } ( Y : X )$ $= ( 2 , 4 , 0 )$ 。□

这样一来，归并问题就能视为确定每个来自序列 $\pmb { A }$ 或 $B$ 中的元素 $\pmb { x }$ 在 $A \cup$ $B$ 中的位序。而求找一个元素在另一个序列中的位置可以使用对半搜索的方法,其时间界为 $O ( \log n )$ 。

下面给出PRAM模型上对数划分算法。

算法6.3PRAM上对数划分算法

输入：两非降有序序列 $A = \left( a _ { 1 } , \cdots , a _ { n } \right) , B = \left( b _ { 1 } , \cdots , b _ { m } \right)$ ，假定 $\log m$ 和$k \left( m \right) = m \Lambda \log m$ 均为整数

输出：将 $\pmb { A }$ 和 $B$ 划分成 $\pmb { k } ( \pmb { m } )$ 对段组 $( A _ { i } , B _ { i } )$ ，使得 $\mid B _ { i } \mid = \log m \ , \Sigma \mid A _ { i } \mid$ $\mathbf { \mu } = \mathbf { \mu } _ { \pmb { n } }$ ,且对于所有 $1 { \leqslant } i { \leqslant } k \left( m \right) - 1 , A _ { i }$ 和 $B _ { i }$ 中的每一个 $_ i$ 元素均大于 $A _ { i - 1 }$ 和 $B _ { i ^ { - 1 } }$ 中的每一个元素

# Begin

(1) $j ( 0 ) = 0 ; j \left( k \left( m \right) \right) = n$   
(2） for $\dot { \pmb { \imath } } = 1$ to $k \left( m \right) - 1 { \mathrm { ~ p a r } } - \mathbf { d o }$ (2.1)求 $\operatorname { r a n k } ( b _ { i \log m } : A )$ (2.2) $\begin{array} { r } { j \left( i \right) = \operatorname { r a n k } \left( b _ { i \log m } : A \right) } \end{array}$ end for

#

(3） for ${ \bf { \nabla } } _ { \pmb { \imath } } = \mathbf { 0 }$ to $\pmb { k } ( \pmb { m } ) - 1$ par -do(3.1) (3.2) $\begin{array} { r l } & { B _ { i } = \left( b _ { i \log m + 1 } , \cdots , b _ { \left( i + 1 \right) \log m } \right) } \\ & { A _ { i } = \left( a _ { j \left( i \right) + 1 } , \cdots , a _ { j \left( i + 1 \right) } \right) } \end{array}$

# endfor

End

上述算法所产生的划分如图6.2所示。

一旦使用上述算法完成了两个序列的独立划分后，归并A和B的问题就变成了并行地成对归并段组 $( A _ { i } , B _ { i } )$ 的问题了。

例6.3 令A=(4,6,7,10,12,15,18,20), $B = ( 3 , 9 , 1 6 , 2 1 )$ 。本例中 $\pmb { m } = 4$ ，$k \left( 4 \right) = 2$ 。因为 $\operatorname { r a n k } ( 9 : A ) = 3$ ，所以可以得两对划分： $A _ { 0 } = ( 4 , 6 , 7 )$ ， $B _ { 0 } = ( 3 , 9 )$ 和 $A _ { 1 } =$ (10,12,15,18,20), $B _ { 1 } ( 1 6 , 2 1 )$ 。显然， $\pmb { A _ { 1 } }$ 和 $B _ { 1 }$ 中的任一元素都大于$A _ { 0 }$ 和 $B _ { 0 }$ 中的每一元素。因此可以成对归并 $( A _ { 0 } , B _ { 0 } )$ 和 $( A _ { 1 } , B _ { 1 } )$ ,而最终将 $A$ 和 $B$ 归并之。□

$$
\begin{array} { r l } { B = } &  \underbrace { B _ { 0 } } _ { \begin{array} { l } { \overbrace { b _ { 1 } \mathrm { ~  ~ \cdot ~ } \mathrm { ~  ~ \cdot ~ } \ b _ { \mathrm { i o g m } } } ^ { B _ { 0 } } } \left[ \begin{array} { l } { B _ { 1 } } \\ { b _ { \mathrm { l o g m + 1 } } \mathrm { ~  ~ \cdot ~ } \mathrm { ~  ~ \cdot ~ } \mathrm { ~  ~ \cdot ~ } b _ { \mathrm { 2 l o g m } } } \end{array} \right] \mathrm { ~  ~ \cdot ~ } \cdot \mathrm { ~  ~ \cdot ~ } \left[ \begin{array} { l } { B _ { i } } \\ { b _ { \mathrm { i l o g m + 1 } } \mathrm { ~  ~ \cdot ~ } \mathrm { ~  ~ \cdot ~ } b _ { ( i + 1 ) \mathrm { l o g m } } \left[ \mathrm { ~  ~ \cdot ~ } \mathrm { ~  \cdot ~ } \mathrm { ~  \cdot ~ } \right] } \end{array} \right] } _ { \begin{array} { l } { A } \\ { A = } & { \underbrace { \left[ a _ { 1 } \mathrm { ~  ~ \cdot ~ } \mathrm { ~  ~ \cdot ~ } \mathrm { ~  ~ \cdot ~ } a _ { j ( 1 ) } \mathrm { ~  ~ \cdot ~ } a _ { j ( 1 ) + 1 } \mathrm { ~  ~ \cdot ~ } \mathrm { ~  ~ \cdot ~ } \mathrm { ~  ~ \cdot ~ } a _ { j ( 2 ) } \mathrm { ~  ~ \cdot ~ } \mathrm { ~  ~ \cdot ~ } \mathrm { ~  ~ \cdot ~ } \mathrm { ~  ~ \cdot } \mathrm { ~  ~ \cdot ~ } a _ { j ( i ) + 1 } \mathrm { ~  ~ \cdot ~ } \mathrm { ~  ~ \cdot } \mathrm { ~  ~ \cdot ~ } a _ { j ( i + 1 ) } \mathrm { ~  ~ \cdot ~ } \mathrm { ~  ~ \cdot } \mathrm { ~  ~ \cdot ~ } \mathrm { ~  \cdot ~ } \mathrm { ~  ~ \cdot } \mathrm { ~  ~ \cdot } \mathrm { ~  ~ \cdot ~ } a _ { j ( i + 1 ) } \mathrm { ~  ~ \cdot ~ } \mathrm { ~  ~ \cdot } \mathrm { ~  ~ \cdot ~ } \mathrm { ~  ~ \cdot } \mathrm { ~  ~ \cdot ~ } \mathrm { ~  ~ \cdot } \mathrm { ~  ~ \cdot ~ } a _ { j ( i ) + 1 } \mathrm { ~  ~ \cdot ~ } \mathrm { ~  ~ \cdot } \mathrm { ~  ~ \cdot ~ } \right]} \end{array}  } _ { A _ { 1 } } } \end{array} \end{array}
$$

图6.2算法6.3所产生的划分

# 6.1.4功能划分技术

假定欲从长为 $\pmb { n }$ 的序列中选取前 $\pmb { m }$ 个最小者（此即所谓的 $( m , n )$ -选择（（m,n）-Selection))问题,那么应如何对原序列施行划分以便并行处理呢？此时可以使用所谓功能划分(Functional Partition)法,即将长为 $\pmb { n }$ 的序列划分成等长的一些组，每组中的元素数应大于或等于 $\pmb { m }$ (最后一组除外)。然后各组可并行处理，其算法如下：

算法6.4 $( m , n )$ -选择网络算法输入：长为 $\pmb { n }$ 的无序序列 $A = ( a _ { 1 } , \cdots , a _ { n } )$ 输出：序列中前 $_ { m }$ 个最小者

Begin

（1）功能划分：将 $\pmb { A }$ 划分成 $\pmb { \mathrm { g } } = \pmb { \mathrm { n } } / m$ 组,每组含 $_ { \pmb { \mathscr { n } } }$ 个元素。  
（2）局部排序：使用Batcher排序网络将各组并行进行排序。  
（3）两两比较;将所排序的各组两两进行比较,从而形成MIN序列。  
(4）排序-比较:对各个MIN序列,重复执行第(2)和第(3)步，直至最终选出 $\pmb { m }$ 个最小者为止。

End

算法6.4的执行过程示于图6.3。

![](images/dd6f690e59ebf76dc511e60b3800059e0620a905f0835e4baa6f9cb3bf68e846.jpg)  
图6.3 $( m - n )$ -选择过程(S表示排序，M表示归并）

# 6.2分治设计技术

分治(Divide-and-Conquer)策略是一种问题的求解技术,其思想是将一个大而复杂的问题分解成若干特性相同的子问题分而治之。若所得的子问题规模仍嫌过大，可反复使用分治策略,直至很容易求解诸子问题为止。使用分治法时，子问题的类型通常和原问题的类型相同,因此分治法很自然地导致递归(Recur-sion)过程。

一般而言，并行分治法分为三步： $\textcircled{1}$ 将输入划分成若干个规模近于相等的子问题； $\textcircled{2}$ 同时递归地求解各个子问题； $\textcircled{3}$ 归并各子问题的解成为原问题的解。用分治法和上节所介绍的划分法求解问题的共同点在于两者均试图将原问题分解成可并行求解的子问题,但分治法的侧重点在于子问题的归并上;而划分法的注意力则集中在原问题的划分上。

下面将通过两个例子来说明分治技术的使用。

# 6.2.1双调归并网络

定义6.2一个序列 $x _ { 0 } , x _ { 1 } , \cdots , x _ { n } \gets 1$ 是双调序列(Bitonic Sequence),如果：$\textcircled{1}$ 存在着一个 ${ \boldsymbol { x } } _ { k } ( 0 { \leqslant } k { \leqslant } n - 1 )$ 使得 $x _ { 0 } { \geqslant } \cdots { \geqslant } x _ { k } { \leqslant } x _ { k + 1 } { \leqslant } \cdots x _ { n - 1 }$ 成立；或者 $\textcircled{2}$ 此序列能够循环旋转使得条件 $\textcircled{1}$ 满足。

双调归并是基于下述的Batcher定理[26]：

Batcher定理:给定一个双调序列xo,x1,,xn-1,对于所有的0≤≤-1,执行 $x _ { i }$ 和 $x _ { i } + \frac { n } { 2 }$ 的比较交换得到 $s _ { i } = \operatorname* { m i n } \left\{ x _ { i } : x _ { i + { \frac { n } { 2 } } } \right\}$ 和 $l _ { i } = \operatorname* { m a x } \left\{ x _ { i } : x _ { i + \frac { n } { 2 } } \right\} \mathrm { ~ c ~ }$

则： $\textcircled{1}$ 所形成的小序列 $\mathbf { M I N } = ( s _ { 0 } , s _ { 1 } , \cdots , s _ { n / 2 - 1 } )$ 和大序列 $\mathbf { M A X } = \left( l _ { 0 } , l _ { 1 } \cdots , \right.$ $l _ { n / 2 - 1 } )$ 仍是双调序列； $\textcircled{2}$ 且对于所有 $0 { \leqslant } i , j { \leqslant } \frac { n } { 2 } - 1$ 满足 $\bullet _ { i } { \leqslant } l _ { j }$ 。

双调归并可以用比较器网络来实现，它是由Batcher比较器构成的。所谓比较器就是一个双输入和双输出的比较交换单元,它可将两输人中的小者置于上输出端,而大者置于下输出端。

下面是Batcher双调归并算法：

# 算法6.5Bateher双调归并算法

输入：双调序列 $X = \left( \ b { x _ { 0 } } , \ b { x _ { 1 } } , \cdots , \ b { x _ { n - 1 } } \right)$ 输出：非降有序序列Y=(yo,yi,,yn-1） Procedure BITONIC MERG（X) Begin

(1) $\mathbf { f o r } \ i = 0 \ \mathbf { t o } { \frac { n } { 2 } } - 1 \ \mathbf { p a r - d o }$ (1.1) $s _ { i } = \operatorname* { m i n } \{ x _ { i } : x _ { i + n / 2 } \}$ /\*":"表示比较 $\bigstar$ /(1.2) l= max|xi: xi +n/2l

end for

![](images/2dd6abfef7da83842a47bd354de4334c9c6c9d38763e9366ed4a16e4650e3d78.jpg)  
图6.4双调归并网络的递归构造

(2） Recursive Call:

(2.1) BITONIC MERG $\left( \mathbf { M I N } { = } \left( s _ { 0 } , \cdots , s _ { \frac { n } { 2 } - 1 } \right) \right)$

# (2.2） BITONIC MERG $( \mathbf { M A X } = ( l _ { 0 } , \cdots , l _ { \frac { n } { 2 } - 1 } ) )$

(3）output sequence MIN followed by sequence MAX

# End

双调归并网络的递归构造如图6.4所示。

# 6.2.2凸壳问题

定义6.3如果多边形 $\mathbf { Q }$ 上任意两点的连线均处于 $\pmb { Q }$ 之内,则此多边形 $\pmb { Q }$ 称之为凸多边形(Convex Polygon)。

定义6.4给定平面中 $\pmb { n }$ 点集合 $\pmb { S } = ( \mathbf { \nabla } _ { \pmb { p } _ { 1 } } , \cdots , \mathbf { \nabla } _ { \pmb { p } _ { n } } )$ ,所谓 $s$ 的凸亮（ConvexHull)就是包含 $s$ 中所有 $\pmb { n }$ 点的最小凸边形。

求平面凸壳的问题,就是要确定凸壳边界上的有序顶点表列 $C H ( s )$ 。

令 $\pmb { \mathscr { P } }$ 和 $\pmb q$ 是 $s$ 中具有最小和最大 $_ { x }$ 坐标的两个点。很清楚 $\pmb { \hat { p } }$ 和 $\pmb q$ 可将全凸壳CH(S)划分成上凸壳 UH(S)和下凸壳 LH(S),其中 UH(S)系由p到q的所有点组成,而 $L H ( S )$ 系由 $\pmb q$ 到 $\pmb { \hat { p } }$ 的所有点组成。

例如图6.5中,UH(S)=(v1,U2,U3,U4,Us),而 LH(S)=(vs,6,v7,vg,U1)。

![](images/8e10b0f28f670fdab69af882eda50b33d20d4c780aea378c4a19a56ebd953d5c.jpg)  
图6.5集合 S的凸壳CH(S)=(v1,U2,U3,U4,Us,U6,U7,vg)

这样一来,一个完整的凸壳CH(S)就是由上凸壳(Upper Convex Hull)UH(S）和下凸壳(Lower Convex Hull）LH(S）组成。而求 LH(S)和 UH(S)是相似的,所以下面只讨论上凸壳UH(S)的求法。

令x(p:)是点pi的x坐标，假定集合S中的点已按x坐标从小到大排序好,即𝑥(pi)<𝑥(pz)<<𝑥(pn)。那么求上凸壳UH(S)时可以使用分治技术。令 S=(p1,p2,…,p)和 S=(pz+1,P2+2,,pn),那么-且 UH(S1)和UH(S)递归地求出后,只要再求出UH(Si)和UH(S2)的上公切线(Upper

Common Tangent),那么求 $U H ( S )$ 的主要问题就解决了(参照图6.6)。下面给出求上凸壳算法：

算法6.6 PRAM上求上凸壳算法

输入： $S = ( \mathbf { \Gamma } _ { p 1 } , \cdots , \mathbf { \Gamma } _ { \phi _ { n } } )$ ，且 $x ( p _ { 1 } ) { < } x ( p _ { 2 } ) { < } \cdots { < } x ( p _ { n } )$   
输出：返回上凸壳顶点表列 $U H ( S )$   
Procedure UPPER HULL $( S , U H ( S ) ) ,$   
Begin  
(1) if $\textstyle \pmb { n } \leqslant 4$ then use a brute - force to determine $U H ( S )$ endif  
(2) $S _ { 1 } = \left( \phi _ { 1 } , \phi _ { 2 } , \cdots , \phi _ { 2 } ^ { n } \right)$ and $S _ { 2 } = \left( / { p } _ { \frac { n } { 2 } + 1 } ^ { n } , / { p } _ { \frac { n } { 2 } + 2 } ^ { n } , \cdots , / { p } _ { n } \right)$   
（3）递归调用并行计算 $U H ( S _ { 1 } )$ ， $U H ( S _ { 2 } )$ ：(3.1） UPPER HULL $( S _ { 1 } , U H ( S _ { 1 } ) )$ (3.2） UPPER HULL $( S _ { 2 } , U H ( S _ { 2 } ) )$   
(4)求 $U H ( S _ { 1 } )$ 和 $U H ( S _ { 2 } )$ 间上公切线,构造 $U H ( S )$

End

![](images/afb358cc82cb55cafdea7f5c551c5712ea26fdede1157259466876db5e2b7b30.jpg)  
图6.6示例求两上凸壳的上公切线

在 PRAM上求下凸壳的算法和算法6.6雷同。组合上凸壳与下凸壳算法就可导出如下 PRAM上求凸壳算法。

算法6.7PRAM上求凸壳算法输入： S=(p1,…,Pn)，pi=(xi,yi)输出：返回凸壳顶点表列 $C H ( S )$ Procedure CONVEX HULL $( S , C H ( S ) ) ,$ Begin

(1) $\big / \ast$ 识别极点 $\yen 7$ (1.1) $\mathbf { X M I N } = \operatorname* { m i n } \left\{ x _ { i } \right.$ 坐标 (1.2) $\mathbf { X M A X } { = } \mathbf { m a x } \left\{ x _ { i } \right.$ 坐标

(2） $\big / \big \varkappa$ 按 $_ { x }$ 坐标进行划分 $\yen 7$ (2.1) $S _ { 1 } =$ vertices from ${ \pmb \phi } _ { { \bf X M I N } }$ to ${ \pmb { \phi } } _ { \mathbf { X M A x } }$ (2.2) $S _ { 2 } =$ vertices from $\pmb { \mathscr { P } }$ XMAx to $\pmb { \phi }$ XMIN   
(3) $\big / \ast$ 递归调用上凸壳和下凸壳算法 $\yen 7$ （3.1）UPPER HULL $( S _ { 1 } , U H ( S _ { 1 } ) )$ (3.2) LOWER HULL $( S _ { 2 } , U H ( S _ { 2 } ) )$   
(4) $\nearrow$ 并接 $U H ( S _ { 1 } )$ 和 $L H ( S _ { 2 } ) \ast \prime$ $C H ( S ) = U H ( S _ { 1 } ) + L H ( S _ { 2 } )$

End

上述算法中,求上(下)公切线是很关键的。由于主要目的是展示分治技术在算法设计中的应用，所以公切线的求法就不再讨论，感兴趣的读者可参阅[104]中的第六章。

# 6.3平衡树设计技术

平衡树(Balanced Tree)方法是将输入元素作为叶节点构筑一棵平衡二叉树，然后自叶向根往返遍历。此法成功的部分原因是在树中能快速地存取所需要的信息。平衡二叉树的方法可推广到内节点的子节点的数目不只两个的任意平衡树。这种方法对数据的播送、压缩、抽取和前缀计算等甚为有效。

# 6.3.1求取最大值

使用平衡二叉树求取数的最大值时,根节点给出问题的解;叶节点存放待处理的数据;内节点执行相应子问题的计算。在树的同一深度上各内节点并行计算。

令 ${ \pmb n } = 2 ^ { m }$ ， $\pmb { A }$ 是一个 $_ { 2 n }$ 维的数组;待求最大值的 $\pmb { n }$ 个数开始存放在 $\boldsymbol { A } ( \boldsymbol { n } )$ ，$A { \big ( } n + 1 { \big ) } , \cdots , A { \big ( } 2 n - 1 { \big ) }$ ;所求得的最大值置于 A(1),于是算法描述如下：

# 算法6.8 SIMD-TC上求最大值算法

输入： $\pmb { n } = 2 ^ { m }$ 个数存在数组 $\pmb { A } \left( \pmb { n } : 2 \pmb { n } - \pmb { 1 } \right)$ 中输出：最大数置于A(1)中

# Begin

for $k = m - 1$ to 0 do for $j = 2 ^ { k }$ to 2k +1 -1 par- do

$$
A \left( j \right) = \operatorname* { m a x } \left\{ A \left( 2 j \right) , A \left( 2 j + 1 \right) \right\}
$$

# end for

end for

End

显然算法的时间 $t \left( n \right) = O \left( \log n \right)$ ,总比较次数为 $O ( n )$ ,而最大的处理器数 ${ \pmb { \mathscr { p } } } ( { \pmb { \mathscr { n } } } ) = { \pmb { \mathscr { n } } } / 2$ 。

# 6.3.2计算前缀和

对于取值于集合S上的满足二元结合运算 $^ { \star }$ 的 $\pmb { n }$ 个元素 ${ ( \pmb { x } _ { 1 } , \pmb { x } _ { 2 } , \cdots , \pmb { x } _ { n } ) }$ 的序列,所谓 $\pmb { n }$ 个元素的前缀和(Prefix-Sums)是指如下定义的 $\pmb { n }$ 个部分和(或积):

$$
s _ { i } = x _ { 1 } * x _ { 2 } * \cdots * x _ { i } , 1 { \leqslant i } { \leqslant n }
$$

显然，使用等式 $s _ { i } = s _ { i - 1 } \star x _ { i } ( 2 { \leqslant } i { \leqslant } n )$ 计算前缀和的平易的申行算法具有固有的顺序性,且时间为 $O ( n )$ 。

使用平衡二叉树计算前缀和时，在自叶向根正向遍历过程中，各内节点对其相应的子节点应用一次 $\bigstar$ 运算，因此每个节点 $_ { v }$ 保存了根在 $\pmb { v }$ 的子树的叶中所存储元素的和;在自根向叶反向遍历过程中，将计算出给定高度上各节点中所存储的元素的前缀和。

下面给出一个非递归求前缀和算法。令 $A \left( i \right) = x _ { i } \left( 1 { \leqslant } i { \leqslant } n \right)$ ;令 $B ( h , j )$ 和$C ( \boldsymbol { h } , \boldsymbol { j } )$ 是辅助变量集 $( 0 { \leqslant } h { \leqslant } \log n , 1 { \leqslant } j { \leqslant } n / 2 ^ { h } )$ ，其中数组 $B$ 用于记录正向遍历时树中各节点的信息,而数组 $c$ 用于记录反向遍历时树中各节点的信息。

算法6.9 SIMD-TC上非递归求前缀和算法 输入： $n = 2 ^ { k }$ 的数组 $A , k$ 为非负整数 输出：数组 $c$ ,其中 $c ( \mathbf { 0 } , j )$ 是第 $\pmb { j }$ 个前缀和 $( 1 { \leqslant } j { \leqslant } n )$ (1) for $j = 1$ to $\pmb { n }$ par -do $\big / \ast$ 初始化 $\yen 7$ $B ( 0 , j ) = A \left( j \right)$ end for

(2） for $h = 1$ to $\log n$ do $\big / \big \varkappa$ 正向遍历 $\yen 7$ for $j = 1$ to $n / 2 ^ { h }$ par -do$B \left( h , j \right) = B \left( h - 1 , 2 j - 1 \right) \ast B \left( h - 1 , 2 j \right)$ end forend for  
(3) for $\pmb { h } = \log \pmb { n }$ to 0 do $\big / \ast$ 反向遍历 $\yen 7$

for $j = 1$ to $\pmb { n } / 2 ^ { h }$ par - do

(i）if $j = \mathrm { e v e n }$ then $C ( h , j ) = C ( h + 1 , j / 2 ) \epsilon$ end if (ii）if $j = 1$ then $C ( h , 1 ) = B { \left( h , 1 \right) }$ end if （iii）if $j = \cosh \cosh \cosh \cosh$ then $C ( h , j ) = C ( h + 1 , ( j - 1 ) / 2 ) *$ $B ( h , j ) \mathrm { e n d i f }$

end for end for

End

# 6.4 倍增设计技术

倍增技术(Doubling Technique)又叫指针跳越(Pointer Jumping)技术,特别适合处理以链表或有向有根树之类表示的数据结构,在图论和链表算法中有着广泛的应用。每当递归调用时,所要处理的数据之间的距离将逐步加倍，经过 $\pmb { k }$ 步后就可完成距离为 $2 ^ { k }$ 的所有数据的计算。下面以表列中元素的位序(Rank)[简称表序问题(List Ranking Problem)]和求找森林的根为例,来说明此项技术的具体使用。

# 6.4.1表序问题的计算

令L是n个元素的表列，且每个元素分配一个处理器。所谓表序问题就是给表中每个元素k指定一个它在表列中的次第号(rank(k)）,rank(k)可视为元素k至表尾的距离。为此每个元素k都有一个指向下一个元素的指针 nect(k)。如果k是表中最后一个元素,则next(k)=k。具体算法形式描述如下：

# 算法6.10 SIMD-EREW上求元素表序算法

输入： $\pmb { n }$ 个元素的表列 $L$ 输出： $r a n k \left( k \right) , k \in L$

Begin

(1） for all $k \in L$ par -do (1.1) $P ( k ) = n e x t \left( k \right)$ (1.2) if P(k)≠k then distance(k)=1 else distance(k)= O end if end for

(2) repeat log n ]times (2.1) for all $k \in L { \mathrm { ~ p a r } } - \mathrm { d } \mathbf { 0 }$ if $P \ ( k ) { \neq } P ( P ( k ) )$ then

$$
d i s t a n c e ( k ) = d i s t a n c e ( k ) + d i s t a n c e ( P ( k ) )
$$

$$
P ( k ) = P ( P ( k ) )
$$

end if end for (2.2) for all k ∈ L par-do $r a n k \left( k \right) = d i s t a n c e \left( k \right)$ end for end repeat

End

显然,算法6.10的 $t { \big ( } n { \big ) } = O { \big ( } \log n { \big ) }$ ， ${ p ( n ) = n }$ 。

例6.4令 ${ \pmb n } = 7 .$ 。图6.7示例出算法6.10的执行过程。其中带箭头的弧为指针 $P ( k )$ ;弧上的数字为 $d i s t a n c e ( k )$ 的值。开始时,在算法6.10第(1.1)步 $P ( k )$ 进行初始化;在第(1.2)步计算出distance $( k )$ 的值。算法总共迭代三次，各元素的指针 $P ( k )$ 和 distance $( k )$ 依次标注在图6.7中。□

![](images/6fe06258922894d39002f09d625ee9ad565f4868e3d1c4e5d95e455202161e16.jpg)  
图6.7 $\pmb { n } = 7$ 算法6.10的执行过程

# 6.4.2 求森林的根

令森林 $F$ 是一组有根有向树,其中 $F$ 由长为 $\pmb { n }$ 的数组 $P$ 指定,使得如果 $( i$ ，$j )$ 是 $F$ 中的一条弧,则 $P ( i ) = j$ ,即 $j$ 是 $i$ 的父亲;如果 $_ i$ 是一个根,则 $P ( i ) = i ,$ 所谓找森林的根(Finding Roots of a Forest)的问题,就是对于每个节点 $j ( 1 \leqslant j \leqslant$ $^ { \textit { \textbf { n } } ) }$ ,确定包含该节点的树的根 $S ( j )$ 。开始时,每个节点 $_ i$ 的后继 $S ( i )$ 定义为$P ( i )$ 。指针跳越技术就是用后继的后继去修改每个节点的后继。重复使用此法，一个节点的后继就变成了越来越靠近树根的祖先。所以节点及其后继之间的距离将逐次加倍，经过 $k$ 次迭代后， $\pmb { i }$ 和 $\mathbb { S } ( i )$ 之间的距离则为 $2 ^ { k }$ 。算法的描述如下：

算法6.11 SIMD-CREW上求森林根的算法   
输入：森林 $\pmb { F }$ ,弧由 $( i , P ( i ) )$ 指定， $1 { \leqslant } i { \leqslant } n$   
输出：对每个节点 $\textbf { \em i }$ ,输出包含 $\textbf { \em i }$ 的树的根 $S ( i )$   
Begin for $1 { \leqslant } i { \leqslant } n$ par-do (1) $S ( i ) = P ( i )$ (2）while $S ( \mathfrak { i } ) { \neq } S ( S ( \mathfrak { i } ) )$ do $S ( \mathfrak { i } ) = S ( S ( \mathfrak { i } ) )$ end while end for   
End

令 $\hbar$ 是森林中树的最大高度,不难看出算法将迭代 $O ( \log  n )$ 次，每次选代作了O（n）次运算而花费了O(1)时间。所以算法的t（n）=O（logn），$W ( n ) = O ( n \log n ) ,$

例6.5图6.8中示例了使用指针跳越技术求森林的根的过程。本例中，如图6.8(a)所示，森林由两棵根在8和13的树组成。图中的弧相应于(i,P(i)）$( 1 { \leqslant } i { \leqslant } 1 3 )$ 。算法执行while语句的第一次循环后的结果如图6.8(b)所示,致使节点1,2,3,4,5,9,10和11改变它们的后继;第二次循环后如图 ${ \pmb 6 . 8 ( \mathfrak { c } ) }$ 所示，使得两棵树的高度都变为1。现在对于所有i,有S(i)=S(S(i)),所以算法结束。□(a)起始森林；(b)第一次迭代后的森林;(c)第二次迭代后的森林

![](images/91364ed5a5d83cedb403a47456129fd7b6dc28c5ffe37816b48a8af87d444ab5.jpg)  
图6.8求森林的根

# 6.5流水线设计技术

并行处理中,流水线(Pipelining)技术是一项重要的并行技术。它在VLSI并行计算中表现得尤为突出。其基本思想是将一个计算任务 $\pmb { t }$ 分成一系列子任务$t _ { 1 } , t _ { 2 } , \cdots , t _ { m }$ ,使得一旦 $t _ { 1 }$ 完成,后继的子任务就可立即开始,并以同样的速率进行计算。下面以一维心动(Systolic)阵列上离散傅氏变换(DFT)和卷积计算为例，说明流水线技术的使用。

# 6.5.1一维心动阵列上的DFT计算

一个 $\pmb { n }$ 点的离散傅里叶变换(Discrete Fourier Transform）,简记之为DFT,可定义为：给定序列 $( a _ { 0 } , a _ { 1 } , \cdots , a _ { n - 1 } )$ ,按如下规则变换成序列 $( b _ { 0 } , b _ { 1 } , \cdots , b _ { n - 1 } )$ ：

$$
b _ { j } = \sum _ { k = 0 } ^ { n - 1 } a _ { k } \omega ^ { k j } , 0 { \leqslant } j { \leqslant } n - 1
$$

其中， $\pmb { \omega }$ 是单位 $\pmb { n }$ 次元根，即 $\omega = e ^ { 2 \pi i / n }$ ， $\mathbf { i } = { \sqrt { - 1 } }$ 。

事实上(6.1)式的计算,可以等效于多项式求值：设想有一多项式 $_ { y } ( { \boldsymbol { x } } ) =$ $\sum _ { k = 0 } ^ { n - 1 } a _ { k } x ^ { k }$ ，叙求其在 $x = \omega ^ { j }$ $( 0 { \leqslant } j { \leqslant } n - 1 )$ 处的 $_ y ( x )$ 之值，即 $y ( \omega ^ { j } ) = \sum _ { k = 0 } ^ { n - 1 } a _ { k } \omega ^ { j k }$ 则显然此式和(6.1)式是完全一样的。

例如,欲计算一个5点的DFT,可以通过计算 $_ { \pmb { x } }$ 等于 $\omega ^ { 0 } , \omega ^ { 1 } , \omega ^ { 2 } , \omega ^ { 3 }$ 和 $\omega ^ { 4 }$ 处的如下多项式的值而求得：

$y \left( ⨏ _ { x } = \omega ^ { j } \right) = a _ { 4 } ( \omega ^ { j } ) ^ { 4 } + a _ { 3 } ( \omega ^ { j } ) ^ { 3 } + a _ { 2 } ( \omega ^ { j } ) ^ { 2 } + a _ { 1 } ( \omega ^ { j } ) ^ { 1 } + a _ { 0 }$ 即

$$
\left. \begin{array} { c } { { y ^ { \left( \omega ^ { 0 } \right) } = \alpha _ { 4 } \omega ^ { 0 } + \alpha _ { 3 } \omega ^ { 0 } + \alpha _ { 2 } \omega ^ { 0 } + \alpha _ { 1 } \omega ^ { 0 } + \alpha _ { 0 } } } \\ { { } } \\ { { y ^ { \left( \omega ^ { 1 } \right) } = \alpha _ { 4 } \omega ^ { 4 } + \alpha _ { 3 } \omega ^ { 3 } + \alpha _ { 2 } \omega ^ { 2 } + \alpha _ { 1 } \omega ^ { 1 } + \alpha _ { 0 } } } \\ { { } } \\ { { y ^ { \left( \omega ^ { 2 } \right) } = \alpha _ { 4 } \omega ^ { 8 } + \alpha _ { 3 } \omega ^ { 6 } + \alpha _ { 2 } \omega ^ { 4 } + \alpha _ { 1 } \omega ^ { 2 } + \alpha _ { 0 } } } \\ { { } } \\ { { y ^ { \left( \omega ^ { 3 } \right) } = \alpha _ { 4 } \omega ^ { 1 2 } + \alpha _ { 3 } \omega ^ { 9 } + \alpha _ { 2 } \omega ^ { 6 } + \alpha _ { 1 } \omega ^ { 3 } + \alpha _ { 0 } } } \\ { { } } \\ { { y ^ { \left( \omega ^ { 4 } \right) } = \alpha _ { 4 } \omega ^ { 1 6 } + \alpha _ { 3 } \omega ^ { 1 2 } + \alpha _ { 2 } \omega ^ { 8 } + \alpha _ { 1 } \omega ^ { 4 } + \alpha _ { 0 } } } \end{array} \right\}
$$

根据 Horner规则,(6.3)式可变换为如下的等效形式：

$$
\begin{array} { r l } & { y \big ( \omega ^ { 0 } \big ) = y _ { 0 } = \big ( \big ( \big ( \alpha _ { 4 } \omega ^ { 0 } + \alpha _ { 3 } \big ) \omega ^ { 0 } + \alpha _ { 2 } \big ) \omega ^ { 0 } + \alpha _ { 1 } \big ) \omega ^ { 0 } + \alpha _ { 0 } } \\ & { y \big ( \omega ^ { 1 } \big ) = y _ { 1 } = \big ( \big ( \big ( \alpha _ { 4 } \omega ^ { 1 } + \alpha _ { 3 } \big ) \omega ^ { 1 } + \alpha _ { 2 } \big ) \omega ^ { 1 } + \alpha _ { 1 } \big ) \omega ^ { 1 } + \alpha _ { 0 } } \\ & { y \big ( \omega ^ { 2 } \big ) = y _ { 2 } = \big ( \big ( \big ( \alpha _ { 4 } \omega ^ { 2 } + \alpha _ { 3 } \big ) \omega ^ { 2 } + \alpha _ { 2 } \big ) \omega ^ { 2 } + \alpha _ { 1 } \big ) \omega ^ { 2 } + \alpha _ { 0 } } \\ & { y \big ( \omega ^ { 3 } \big ) = y _ { 3 } = \big ( \big ( \big ( \alpha _ { 4 } \omega ^ { 3 } + \alpha _ { 3 } \big ) \omega ^ { 3 } + \alpha _ { 2 } \big ) \omega ^ { 3 } + \alpha _ { 1 } \big ) \omega ^ { 3 } + \alpha _ { 0 } } \\ & { y \big ( \omega ^ { 4 } \big ) = y _ { 4 } = \big ( \big ( \big ( \alpha _ { 4 } \omega ^ { 4 } + \alpha _ { 3 } \big ) \omega ^ { 4 } + \alpha _ { 2 } \big ) \omega ^ { 4 } + \alpha _ { 1 } \big ) \omega ^ { 4 } + \alpha _ { 0 } } \end{array}
$$

很明显，(6.4)式中所有的 $y _ { i } ( 0 { \leqslant } i { \leqslant } 4 )$ 都可以在图6.9所示的一维线性阵列上以流水线方式计算之。可以看出,每个 $y _ { i }$ 初始化为 $\alpha _ { 4 }$ （一般为 $a _ { n - 1 } )$ ，然后收集其有关项向右行进,当其积累完了所有项后,从最右单元输出。显然,在n－1=$O ( n )$ 个单元的心动阵列上,计算 $\pmb { n }$ 点DFT可在 $2 { \mathfrak { n } } - 1 = O ( { \mathfrak { n } } )$ 时间内完成。

![](images/c07cf84973bd52f9fac9aed9d50ac9b6d3af51da44cc6365c738e89728746e7f.jpg)  
图6.9(a)处理单元功能及其定义;(b)5点DFT在一维阵列上的计算过程

# 6.5.2一维心动阵列上的卷积计算

卷积(Convolution)在数学上可定义如下:给定权序列(wi,w2,,wn）和x序列(x1,x2,…,xm),m>n,试按下式计算 y序列(y1,y2,.,ym-n+1):

$$
y _ { j } = \ \sum _ { i = 1 } ^ { n } \ W _ { i } X _ { i + j - 1 } , \ 1 { \leqslant j } { \leqslant m - n + 1 }
$$

卷积在数字信号处理、模式识别、多项式求值等方面应用很广泛。例如(6.5)式中的乘、加代之以“比较”和“布尔与"操作，则卷积问题就变成了模式匹配问题。因为每个y；可在(n)时间内计算出，所以卷积可在@(nm)时间内计算完毕。

例如,给定4个权的序列(w1,W2,\~3,W4)和6个数的序列(𝑥1,x2,x3,$x _ { 4 } , x _ { 5 } , x _ { 6 } )$ ,则须计算如下的 $_ y$ 序列 $( y _ { 1 } , y _ { 2 } , y _ { 3 } )$ ：

$$
\left. { \begin{array} { r } { y _ { 1 } = x _ { 1 } w _ { 1 } + x _ { 2 } w _ { 2 } + x _ { 3 } w _ { 3 } + x _ { 4 } w _ { 4 } } \\ { y _ { 2 } = x _ { 2 } w _ { 1 } + x _ { 3 } w _ { 2 } + x _ { 4 } w _ { 3 } + x _ { 5 } w _ { 4 } } \\ { y _ { 3 } = x _ { 3 } w _ { 1 } + x _ { 4 } w _ { 2 } + x _ { 5 } w _ { 3 } + x _ { 6 } w _ { 4 } } \end{array} } \right\}
$$

当在一维心动阵列上计算上述卷积时需要4个处理单元 $C _ { 1 } { \setminus } C _ { 2 } \setminus C _ { 3 }$ 和 $C _ { 4 }$ ,其中每个 $C _ { i }$ 中存有 ${ \boldsymbol { \mathsf { w } } } _ { i }$ ,且执行(6.5)式计算。计算时，如图6.10所示，输人序列$x _ { 1 } \sim x _ { 6 }$ 由左方进人心动阵列，输出序列 $y _ { 1 } \sim y _ { 3 }$ 由右方进人心动阵列。开始时， $_ { \pmb { x } }$ 的元素每隔一拍流人阵列,而 $\pmb { y }$ 的元素须延迟3拍后也每隔一拍流人阵列。在前3拍时不作任何计算;而第4拍时 $C _ { 1 }$ 执行 $y _ { 1 } + x _ { 1 } \mathbf { w } _ { 1 }$ 操作( $\lvert _ { y _ { 1 } }$ 初始化为零)；类似地,在第5拍时C执行y1+xW2;在第6拍时,C和C分别同时计算y和y1所需的项。般而言,当C接收到xi和y；时,则执行操作xi+yj。

![](images/3d4321887a0dd26ee4746e6885514f2587dd4c31bde0d3e570b0ba2947d6b481.jpg)  
图6.10卷积在一维心动阵列上的执行过程

一般情况下，当权数为n和输入序列长度为m时，须用n个心动单元，y序列需滞后n-1个拍。因为y需要计算(m－𝑛+1)个元素，所以总共约需2(m－n)个节拍。当n<m时,此算法的成本为@(mn),显然是成本最优的。

# 6.6小结和导读

小结本章所介绍的都是并行算法设计的最基本的技术,远非所有的设计技术。这些技术虽具有一定的普适性,但也并非对所有问题均行之有效,况且也不全面,同时也只能作为设计并行算法的一般性指南，绝非是可直接引用的手册。其它的设计技术还有破对称(Symmetry Breaking)技术,它是打破某些问题的对称性的一种设计方法，在图论问题和随机算法中经常使用；加速级联（Ac-celerated Cascading)技术,它试图将一个最优但相对不快的算法与另一个非常快但非最优的算法"串接"起来,形成一个快速最优的算法，此法虽不具有普适性，但对有些问题却效果甚佳;随机法是在算法设计时,引入随机性使得算法在执行时,可以随机地选择下一执行步，从而可望得到平均性能较好的算法(即其复杂度比同一问题的确定性算法的最坏情况的复杂度要好),随机算法设计简单，但分析较复杂，经常要分析算法可在多少时间步内以多大的概率结束，用随机法设计的算法，其运行结果也可能是不正确的,但这种错误的概率应是很小的；贪心法(Greedy Method)是一种最直接的设计技术,其设计特点是,在算法的每一步都力图确保获得局部最优，这种设计方法的副作用是容易陷人局部最优。对于组合问题的算法设计技术,有动态规划法(Dynamic Programming),它是在每一判定步,列出多种可能的解，然后按照某种条件，舍弃那些肯定不能导致最优解的局部解，它和贪心法的区别在于，贪心法仅产生一个判定序列,而动态规划法可能产生很多判定序列，但依据“最优性原理”,非局部最优解的序列肯定不是最优的，所以不予考虑；回溯法(Backtracking)是一种穷举法,在问题求解时常使用深度优先搜索(Depth-First Searching)法,在搜索过程中，一旦碰到某个无法搜索下去的分支，就向其父节点回溯,再搜索该父节点的其它分支，如果所有的分支节点均无希望的解,则再向上追溯，如此等等,回溯法虽提供了一种规律性求解的方法，但其时间复杂度较高;分支界限法(Branchand Bound)与回溯法颇类似,但它是基于广度优先搜索(Breadth-First Searching)法，它利用部分解的最优性信息，避免考虑那些不能导致最优的解，以加快问题的求解，其解题过程是：对解集合反复进行分支，即反复构造其子集合，每次分支时都对所得到的子集合计算最优解的界，若它不能优于当前已知的最优解，则对此子集合就不再进行分支，否则继续分支，以探索更好的解，直到所得的子集合仅有一个解为止。

导读有关PSRS排序算法的设计和分析，读者可参阅[157];使用平方根划分法的归并算法是由Valiant提出[175];使用对数划分法的归并算法,读者可参阅[158];有关(m,n)-选择算法，读者可参阅[189]。分治方法的一般介绍，读者可参阅[97]；双调归并网络是由Batcher提出[26];用分治法求凸壳问题，读者可参阅[156]。并行前缀和计算,读者可参阅[116]。表序计算问题,读者可参阅[185];倍增技术在图论中的应用,Hirschberg求连通分量是一篇常被人引用的文章[93]。关于心动阵列的并行计算,[115]是一篇很经典的文章。加速级联技术由Cole等人提出[51];破对称设计技术,读者可参阅[77]。在[104]书的第九章专门讨论了随机算法。组合问题的算法设计技术,读者可参阅[179]。

# 习 题

6.1 $\textcircled{1}$ 试证明：当 $\scriptstyle \pmb { n } \geqslant \pmb { \phi } ^ { 3 }$ 时，算法6.1的时间复杂度为 $O \left( { \frac { n } { p } } \log n \right)$

$\textcircled{2}$ 令 $\boldsymbol { w _ { i } ^ { j } }$ 表示 $P _ { i }$ 中第 $j$ 段中的元素数,试证明算法6.1在执行过程中，处理器中所积累的元素数目不会超过 $2 n / \beta$ ，即 $\sum _ { j = 1 } ^ { P } w _ { i } ^ { j } < \frac { 2 n } { p } ,$

6.2 $\textcircled{1}$ 试举一典型算例,说明Valiant归并算法的执行过程。

$\textcircled{2}$ 试分析算法6.2所需的处理器数 ${ p ( n ) = O ( n ) }$ 0$\textcircled{3}$ 试证明算法6.2的时间复杂度为： $2 \log \log n + \mathrm { c o n s t } _ { \circ }$

6.3 $\textcircled{1}$ 试分析算法6.3的复杂度。

$\textcircled{2}$ 令 $A =$ (0,1,2,7,9,11,16,17,18,19,23,24,25,27,28,30,33,34), $B = ( 3 , 4 , 5 , 6 , 8 ,$ 10,12,13,14,15,20,21,22,26,29,31)。试按算法6.3,将其进行对数划分,并最终 将它们归并之。

6.4 $\textcircled{1}$ 试举一例，说明算法6.4的执行过程。

$\textcircled{2}$ 试证明算法6.4的正确性。

6.5 $\textcircled{1}$ 试证明Batcher定理。

$\textcircled{2}$ 画出一个16个输入的双调归并网络。

6.6 $\textcircled{1}$ 试分析算法6.9的总运算量 $\textstyle \mathbf { W } ( n ) = ?$

$\textcircled{2}$ 假定序列为(1,2,3,4,5,6,7,8),试用算法6.9求其前缀和。

6.7定义 $\log ^ { ( i ) } x$ 如下： $\log ^ { ( 1 ) } x = \log x , \log ^ { ( 2 ) } x = \log \log x , \log ^ { ( i ) } x = \log ( \log ^ { ( i - 1 ) } x )$ 。令函数$\log ^ { * } x = \operatorname* { m i n } \{ i \mid \log ^ { ( i ) } x { \leqslant } 1 \} \ ,$

当 $x { \leqslant } 2 ^ { 6 5 5 3 6 }$ 时,此函数界限是什么？

6.8对于 $\pmb { n = 8 }$ ,按照DFT定义，计算 $\pmb { w }$ 矩阵之各元素。

6.9试解释在一维心动阵列上计算卷积时，序列 $_ { x }$ 和 $_ y$ 为何要各间隔一拍进人阵列。

6.10顶点倒塌法是非常有名的求图的连通分量的算法,其基本思想是：连通的相邻的顶点可以合并成一个超顶点,并以它们中最小标号者标记之；此过程可继续在已合并的超顶点之间进行。在下列的算法中， $C ( i )$ 表示与 $\pmb { i }$ 相邻的最小的超顶点号码； $D ( i )$ 表示顶点 $\dot { \pmb { \mathscr { \imath } } }$ 所属连通分量的最小标号的顶点； $C ( \mathbf { \Phi } _ { i } ) = \operatorname* { m i n } _ { \mathbf { \Phi } _ { j } } \{ D ( \mathbf { \Phi } _ { j } ) \ \mid \ _ { A ( \mathbf { \Phi } _ { i } , \mathbf { \Phi } _ { j } ) = 1 , D ( \mathbf { \Phi } _ { i } ) \neq D ( \mathbf { \Phi } _ { j } ) } \}$ 语句为每个顶点 $_ i$ 找与它不属于相同分量的相邻的最小号码的顶点 $j$ ；语句 $C \left( \mathrm { \ i \right) = }$ $\operatorname* { m i n } _ { j } \{ C ( j ) ~ \vert ~ \smash { \cal D } ( j ) = i , C ( j ) \ne i \}$ 表示把每个超顶点的根连到最小号码的相邻的超顶点的根上。Hirschberg的求连通分量算法如下：

# 算法6.12 PRAM-CREW上Hirschberg求连通分量算法

输入：邻接矩阵 $\mathbf { A } _ { n } \mathbf { \times } _ { n }$

输出：向量 $\pmb { D } [ \pmb 0 : \pmb { n } - 1 ]$ ,其中 $D ( i )$ 表示向量 $\pmb { D }$ 的分量

Begin(1） for all $i \colon 0 { \leqslant } i { \leqslant } n - 1$ par -do /\*初始化\*/$D ( i ) = i$ end fordo step (2)through ( $6 ) \mathrm { f o r } \Gamma \mathrm { l o g } n$ literations:(2) for all $i , j \colon 0 { \leqslant } i , j { \leqslant } n - 1 \quad \mathrm { p a r } ^ { - } \mathrm { d } \mathbf { 0 }$ $\big / \varkappa$ 找相邻的最小者 $\divideontimes$ /(2.1) $C ( \mathbf { \Phi } _ { i } ) = \operatorname* { m i n } _ { \mathbf { \Phi } _ { j } } \{ D ( \mathbf { \Phi } _ { j } ) \ \mid _ { \mathbf { \Phi } _ { A } ( \mathbf { \Phi } _ { i } , \mathbf { \Phi } _ { j } ) = 1 \mathrm { ~ a n d ~ } D ( \mathbf { \Phi } _ { i } ) \neq D ( \mathbf { \Phi } _ { j } ) } \}$ (2.2） if none then $C ( i ) = D ( i )$ endifend for(3) for all $i , j \colon 0 { \leqslant } i , j { \leqslant } n - 1 \quad \mathrm { p a r } ^ { - } \mathrm { d } \mathbf { 0 }$ $\big / \varkappa$ 找每个超顶点的最小相邻超顶点 $\divideontimes$ /(3.1) $C ( \mathbf { \phi } _ { i } ) = \underset { \mathbf { \phi } _ { j } } { \min } \{ C ( \mathbf { \phi } _ { j } ) ~ \left| ~ \ _ { D ( \mathbf { \phi } _ { j } ) } = \mathbf { \phi } _ { i } \ \mathrm { a n d } ~ C ( \mathbf { \phi } _ { j } ) \neq \mathbf { \phi } _ { i } ~ \right\}$ (3.2） if none then $C ( i ) = D ( i )$ endifend for(4) for all i: $0 { \leqslant } i { \leqslant } n - 1$ par-do $D ( i ) = C ( i )$ end for(5）for $\lceil \log n$ literations do $\big / \ast$ 指针跳越,找各顶点新的超顶点 $\yen 7$ for all i : $0 { \leqslant } i { \leqslant } n - 1 \quad { \mathrm { p a r } } - { \mathrm { d o } } \ C ( i ) = C ( C ( i ) )$ end forend for(6) for all i: $0 { \leqslant } i { \leqslant } n - 1$ par-do$D ( i ) { = } \operatorname* { m i n } \{ C ( i ) , D ( C ( i ) ) \}$ end for  
End

$\textcircled{1}$ 试分析算法6.12的复杂度 $\ t ( \pmb { n } ) = ?$ 和 $\textstyle \mathbf { \hat { \Gamma } } \mathbf { \hat { \Gamma } } ( { \boldsymbol { \mathsf { n } } } ) = ?$ $\textcircled{2}$ 给定如图6.11所示无向图,试用算法6.12逐步求出该图的连通分量。

![](images/819cf614998d590b247bd20e7cf976eaa23cb082e47a549dd519dd064c2bad46.jpg)  
图6.11待求连通分量的无向图

# 第七章 并行算法的一般设计过程

设计一个高效的并行算法并非易事,其过程比较复杂,很难归结为一个单一化的过程而“一步到位”，往往需要几经反复方能达到要求。

本章试图从给定问题的描述出发，通过一系列步骤，最终设计出一个能展示出并发性、可扩放性、局部性和模块性的并行算法。此过程可分为四步，即任务划分（Partitioning）、通信（Communication）分析、任务组合（Agglomeration）和处理器映射(Mapping),简称为PCAM设计过程,它是一种设计方法学，是实际设计并行算法的自然过程,其基本要点是：首先尽量开拓算法的并发性和满足算法的可扩放性;然后着重优化算法的通信成本和全局执行时间，同时通过必要的整个过程的反复回溯,以期最终达到一个满意的设计选择。

上述设计过程的最后阶段是映射，也就是将经过优化的诸进程指派给具体的处理器去运行。这样PCAM算法设计过程的最终结果将是一个并行程序。所以就此意义而言,本章所讲的并行算法的设计过程,有时也不加严格区分地应用到并行程序的设计上。

# 7.1 PCAM设计方法学

已如上述,PCAM是 Partitioning、Communication、Agglomeration 和 Mapping首字母的拼写，它们代表了使用此法设计并行算法的四个阶段。其中在设计的前期主要考虑如并发性等与机器无关的特性，在设计的后期才考虑与机器有关的特性。也就是说,在设计的第一和第二阶段，关注的是并发性和可扩放性，并寻求开发出具有这些特性的并行算法，在设计的第三和第四阶段，才把注意力转移到局部性和别的与性能有关的问题上。并行算法设计的整个过程可概括于图7.1中，它从给定设计问题的说明开始，寻找一种计算任务的划分方法,确定诸任务的通信要求，组合可能的计算任务，最后将优化了的诸任务指派给实际的处理器。上述各阶段可简述如下：

$\textcircled{1}$ 划分：将整个计算分解成一些小的任务，其目的是尽量开拓并行执行的机会。  
$\textcircled{2}$ 通信：确定诸任务执行中所需交换的数据和协调诸任务的执行，由此可检测上述划分的合理性。

$\textcircled{3}$ 组合：按性能要求和实现的代价来考察前两阶段的结果,必要时可将一些小的任务组合成更大的任务以提高性能或减少通信开销。

$\textcircled{4}$ 映射：将每个任务分配到一个处理器上,其目的是最小化全局执行时间和通信成本以及最大化处理器的利用率。

![](images/cf2afa34ed378b4d8d94ed91de2f335a4c29163b5096b817c85c434c99206390.jpg)  
图7.1算法的 PCAM设计过程

虽然上述的设计过程是一步一步进行的,但实际上它们可以同时一并考虑；同样，虽然我们希望一个算法能用上述四步一次设计成功，但实际上设计过程的回溯反复总是难免的。

# 7.2划 分

所谓划分，就是使用域分解或功能分解的办法将原计算问题分割成一些小的计算任务，以充分揭示并行执行的机会，这犹如细小的砂粒比大块的砖瓦易于灌注一样，划分以充分开拓算法的并发性和可扩放性为目的；其方法是先集中数据的分解(称域分解),然后是计算功能的分解(称功能分解),两者互为补充；划分的要点是力图避免数据和计算的复制，应使数据集和计算集互不相交。

# 7.2.1域分解

域分解(Domain Decomposition)也叫数据划分。所要划分的对象是些数据，这些数据可以是算法(或程序)的输入数据,计算的输出数据,或者算法所产生的中间结果。

域分解的步骤是，首先分解与问题相关的数据，如果可能的话，应使这些小的数据片尽可能大致相等；其次再将每个计算关联到它所操作的数据上。由此划分将会产生一系列的任务。每个任务包括一些数据及其上的操作。当一个操作可能需要别的任务中的数据时，就会产生通信要求。

域分解的经验方法是，优先集中在最大数据的划分；或者那些经常被访问的数据结构上。在计算的不同阶段，可能要对不同的数据结构进行操作，或者需要对同一数据结构进行不同的分解，在此情况下，我们要分别对待，然后考虑将各阶段设计的分解和算法装配到一起。

图7.2示出了一个三维网格的域分解方法，在各格点上计算都是重复执行的,分解在X,Y和/或Z维是可能的，开始时，应集中在能提供最大灵活性的三维(即3-D)分解上，即每一个格点定义一个计算任务，每个任务维护与其格点有关的各种数据，并负责计算以修改状态。

![](images/f1a365697128ccce64bc9e838086906e65be82ab6a038c3e9b00281b957fbea8.jpg)  
图7.2三维网格问题的域分解法(各图中的阴影部分代表一个任务）

# 7.2.2功能分解

功能分解(FunctionalDecomposition)也叫计算划分,其基本出发点不同于域分解,它首先关注于被执行的计算上，而不是计算所需的数据上；然后，如果所作的计算划分是成功的，再继续研究计算所需的数据，这些数据可能是不相交的，这就意味着划分很成功；或者这些数据有相当的重叠，这就产生大量的通信，此时就暗示应考虑数据分解。

尽管域分解是绝大多数并行算法所使用的，但功能分解却有时能揭示问题的内在结构展示出优化的机遇，而对数据单独进行研究却往往难以作到这一点。

搜索树是功能分解的最好例子，此时无任何明显的可分解的数据结构，但却易于进行细粒度的功能分解：开始时根生成一个任务，对其评价后，如果它不是一个解，就生成一棵搜索子树,整个搜索过程如图7.3所示，自根以波前(Wave-front)形式逐级向树叶推进(见习题7.1)。

![](images/cc012809f6392d39612913262dca603a84004595ee8252e63e13b7061bbd7135.jpg)  
图7.3功能分解的搜索树

# 7.2.3划分判据

下面的一组问答题,可检验你所作的划分有无明显的缺陷。原则上讲,它们应得到肯定的回答：

$\textcircled{1}$ 你所划分的任务数,是否至少高于目标机上处理器数目的一个量级？如果不是，则你在后继的设计步骤中将缺少灵活性。  
$\textcircled{2}$ 你的划分是否避免了冗余的计算和存储要求,如果不是,则所产生的算法对大型问题可能是不可扩放的。  
$\textcircled{3}$ 诸划分的任务是否尺寸大致相当,如果不是,则分配处理器时很难做到工作量均衡。  
$\textcircled{4}$ 划分的任务数是否与问题尺寸成比例？理想情况下,问题尺寸的增加应引起任务数的增加而不是任务尺寸的增加。如果不是这样，则你的算法可能不能求解更大的问题，尽管有更多的处理器。  
③确认你是否采用了几种不同的划分法，多考虑几种选择可提高灵活性，同时既要考虑域分解又要考虑功能分解。

# 7.3通 信

由划分所产生的诸并行执行的任务，一般而言都不能完全独立执行，一个任务中的计算可能需要用到另一个任务中的数据,从而就产生了通信要求。所谓通信，就是为了进行并行计算，诸任务之间所需进行的数据传输。

在域分解中，通常难以确定通信要求，因为将数据划分成不相交的子集并未充分考虑在数据上执行操作时可能产生的数据交换，在功能分解时，通常容易确定通信要求，因为并行算法中诸任务之间的数据流就相应于通信要求。

在讨论通信时，将通信分成以下四种模式：

$\textcircled{1}$ 局部/全局通信：局部通信时，每个任务只与较少的几个近邻通信；全局通信中，每个任务与很多别的任务通信。  
$\textcircled{2}$ 结构化/非结构化通信：结构化通信时，一个任务和其近邻形成规整结构（如树、网格等);非结构化通信中，通信网则可能是任意图。  
$\textcircled{3}$ 静态/动态通信：静态通信，通信伙伴的身份不随时间改变，动态通信中，通信伙伴的身份则可能由运行时所计算的数据决定且是可变的。  
$\textcircled{4}$ 同步/异步通信：同步通信时，接收方和发送方协同操作;异步通信中，接收方获取数据无需与发送方协同。

# 7.3.1局部通信

当某一操作仅要求从近邻的其它任务获取数据时，就呈现局部通信(LocalCommunication)模式。一个典型的例子就是数值计算中的雅可比有限差分法(Finite Difference Method)。对于二维网格,可以使用5点格式(Five-Point Sten-cil)计算诸格点 $_ { \pmb { x } }$ 之值(参见第十章第10.4.2节)：

在迭代过程中,要求计算一系列 $x _ { i , j } ( 1 ) , x _ { i , j } ( 2 ) , x _ { i , j } ( 3 ) \cdots$ 之值。如图7.4,每个 $x _ { i , j } ( k )$ 之计算,都用其周围四个格点的值,其算法如下：

![](images/56e97e97db9bfbbc622e0e2971bbd41fdbf2da68732f2f7b20124d4e73f07037.jpg)  
图7.4二维网格雅可比5点差分格式的局部(四近邻)通信模式

# Begin

$\mathbf { f } \mathbf { 0 r } k \ = \ 1$ to $T$ do

（1）send $x _ { i , j } \ ( \ k \ - 1 )$ to each neighbor （2）receive $x _ { i - 1 , j } ( k - 1 ) , x _ { i + 1 , j } ( k - 1 ) , x _ { i , j - 1 } ( k - 1 ) , x _ { i , j + 1 } ( k - 1 ) f r o m$ neighbors (3) compute xi, (k)using Equation(7.1) end for End

雅可比方法易于并行化，所有格点可同时更新，但收敛速度较慢。改进的Gauss - Seidel 法如下：.

$$
\tau _ { i , j } \left( k \right) = \frac { 4 x _ { i , j } \left( k - 1 \right) + x _ { i - 1 , j } \left( k \right) + x _ { i + 1 , j } \left( k - 1 \right) + x _ { i , j - 1 } \left( k \right) + x _ { i , j + 1 } \left( k - 1 \right) + x _ { i - 1 , j - 1 } \left( k \right) } { 8 } .
$$

它迭代时利用了一半新值，一半旧值，虽加快串行迭代速度，但都不易并行化，为此出现了不少变体方案，如著名的红－黑着色(Red-Black Coloring)法（详见第十章有关章节)。总之，简单的Gauss-Seidel更新策略在串行算法中很有效,而在并行机上不理想,朴素的雅可比更新策略在并行机上很有效，但收敛不快，而红黑着色的更新策略组合了它们的优点，故应用很广。

# 7.3.2全局通信

全局通信(GlobalCommunication)系指有很多任务参与交换数据的一种通信模式,这种方式，可能导致过多的通信从而限制了并行执行的机会。

一个顺序求和算法 $S = \sum _ { i = 0 } ^ { N - 1 } x _ { i }$ ,就呈现出全局通信要求。如图7.5所示，一个根进程 $s$ ,负责从 $\pmb { n }$ 个分布式任务中一次接收一个值并相加之：

![](images/ceb6871ff704ae1851a34821ef6998722cff411f9701ebb70516c22ba6257fda.jpg)  
图7.5集中式顺序求和

显然,这种集中控制式的依次求和方式,妨碍了有效并行执行,为此,可以使

用分治策略来开拓求和的并行性：

$$
\sum _ { i = 0 } ^ { 2 ^ { n } - 1 } \ = \ \sum _ { i = 0 } ^ { 2 ^ { n - 1 } - 1 } \ + \ \sum _ { i = 2 ^ { n - 1 } } ^ { 2 ^ { n } - 1 }
$$

上式右边的两个求和可同时进行，且每个仍可按同样方式进一步分解之。图7.6示出了 $N = 8$ 的分治求和树，由此可见，分治法一方面提高了算法的并行度；同时也可将全局通信化为局部通信。

![](images/56ce126ad6151e0da83222eaf34e7ae4466d7de4480b19123e339d72dff7913b.jpg)  
图7.6 $N = 8$ 时的分治求和树

# 7.3.3非结构化、动态和异步通信

在静态的、结构化通信中,一个任务的通信伙伴形成一个规则的模式(如树、网格等),并且不随时间变化;而非结构化、动态通信则不然，模式不规整且又随时间变化。

非结构化的通信模式,对算法设计的前期不会造成实质性的困难，但却复杂化了任务的组合与处理器的映射,特别是当要求组合策略既能创建尺寸大致相等的任务，又能尽量减少任务间的通信要求时，就要求非常复杂的算法，而这些算法在通信要求是动态时又会在算法的执行中频繁地使用，所以必须权衡这些算法的利弊。

在同步通信中,通信中的双方均知道何时将要产生通信操作,所以发送者就显式地发送数据给接收者,在异步通信(Asynchronous Communication）中，发送者不能确定接收者何时需要数据,所以接收者要明确地(显式地)从发送者请求数据。例如,消息传递(Message-Passing)式通信方式就属异步通信。

# 7.3.4通信判据

下面的一组问答题,可检验你所作的通信设计是否合理。原则上讲,应给予它们肯定的回答：

$\textcircled{1}$ 所有任务是否均执行大致同样多的通信？如果不是，则所设计的算法的可扩放性可能是不好的。  
$\textcircled{2}$ 每个任务是否只与少许的近邻相通信？如果不是，则可能导致全局通信，在此情况下，应设法将全局通信结构化为局部通信结构。  
$\textcircled{3}$ 诸通信操作是否能并行执行？如果不是，则所设计的算法很可能是低效的和不可扩放的,在此情况下,设法试用分治技术来开发并行性。  
$\textcircled{4}$ 不同任务的计算能否并行执行？如果不是,则所设计的算法很可能是低效的和不可扩放的，在此情况下,可考虑重新安排通信/计算之次序等来改善之。

# 7.4组 合

在设计的第一和第二阶段,划分了任务并考虑了任务间的通信,不过所得到的算法仍是抽象的,因为并未考虑它在任何特定的并行机上的执行效率,在第三阶段，即组合(Agglomeration)阶段，将从抽象转到具体，即重新考察在划分和通信阶段所作的决择,力图得到一个在某一类并行机上能有效执行的并行算法。

组合的目的是通过合并小尺寸的任务来减少任务数，但它仍可能多于处理器的数目,理想的情况是,在组合时就将任务数减少到恰好每个处理器上一个，从而得到一个SPMD的程序,这时映射也宣告完成,另外,组合时我们也要考虑是否值得进行数据和/或计算的重复(Replication)。

用增加计算和通信的粒度的办法可减少通信成本,组合时要保持足够的灵活性同时要减少软件工程代价。这几个相互矛盾的准则在组合阶段要仔细考虑。

# 7.4.1增加粒度

在设计过程的划分阶段，致力于定义尽可能多的任务以增大并行执行的机会。但是定义大量的细粒度任务不一定能产生一个有效的并行算法，因为大量细粒度任务有可能增加通信代价和任务创建代价。

表面-容积效应(Surface-to-Volume Effects） 如果每个任务的通信伙伴是少的,则增加划分粒度常能减少通信次数，同时还能减少总通信量，参照图7.7来阐述所谓"表面-容积效应”：一个任务的通信需求比例于它所操作的子域的表面积,而计算需求却比例于子域的容积。在一个二维问题中，“表面积”比例于问题的尺寸,而"容积"比例于问题尺寸的平方。因此一个计算单元的通信/计算之比随问题(任务)尺寸的增加而减少。

图7.7(a)和(b)分别示出了细粒度和粗粒度的二维网格上5点法计算有限差分：在(a)中， ${ \bf 8 } \times { \bf 8 }$ 的网格上，计算被划分成 ${ 8 \times 8 = 6 4 }$ 个任务，每个任务负责计算一个格点;而在(b)中,同一计算问题被划分成 $2 \times 2 = 4$ 个任务，每个任务负责16个格点的计算。在(a)中，共需要 $6 4 \times 4 = 2 5 6$ 次通信，每个任务通信4次，总共传输256个数据值;而在(b)中，仅要求 $4 \times 4 = 1 6$ 次通信，总共传输 $1 6 \times 4$ $= 6 4$ 个数据值,可见同一计算问题,粗粒度划分的通信次数和通信量均比细粒度划分时有所下降。

![](images/ebdd06e3d730330aba380ccf71e909a89f4fa3965998783a03e3618153636706.jpg)  
图7.7在二维网格5点差分格式中,增加粒度对通信成本的影响

表面-容积效应启发我们,在其它条件等同的情况下,高维分解一般更有效。因为相对于一个给 定的容积(计算)它减少了表面积(通信)。因此从效率的角度,增加粒度的最好办法是在所有的维组合任务。

重复计算（Replication Computation）它也称为冗余计算。有时候可以采用不必要的多余的计算的方法来减少通信要求和/或执行时间。仍以二叉树上的求和 $\sum _ { i \mathop { = } 0 } ^ { N - 1 } x _ { i }$ 为例来说明之。

假定在二叉树上用 $N$ 个处理器来求 $N$ 个数的全和，且要求每个处理器上均保持最终的全和。为此如图7.8所示，必须先自叶向根逐级求和；然后自根向叶将全和逐级播送给每个处理器，共需 $2 \log N$ 步。

![](images/79fdff8d03950fc9bf5c0bddd45e78a9d9b3854b1c748369b22249adb1682332.jpg)  
图7.8二叉树上求全和

以上述方式求和时,处理器的利用率是逐级减半的,如果在树的每一级都充分利用所有的处理器参与计算，即在树的每一级,每个处理器(任务)均接收两个数据,执行一次局部求和,然后再发送结果至下一级的两个处理器,那么经过logN 级后，每个处理器中均积累了全和 $\sum _ { i = 0 } ^ { N - 1 } x _ { i }$ 。如图7.9所示,这实际上就是蝶式通信结构,它利用了重复计算的方法,只需 $\log N$ 步就可在各处理器中积累了最终的全和,但却以总共施行 $O \left( N \mathrm { l o g } N \right)$ 次计算和通信操作为代价。

![](images/1f7c6eb03d577a9380fce0a7724ee9c9fea7d62b62eff1f854631307e41cc05e.jpg)  
图7.9使用蝶式通信结构求全和

当对通信需求分析揭示了一组任务不能同时执行时，组合总是有益的，例如,用图7.8所示二叉树和图7.9所示蝶式图进行求和时，只有在树的和蝶式图的同一级中的任务方能同时执行，这样不同级中的任务可组合到一起而不会减少并行执行的机会,同时也可能产生优化的通信结构(参见习题7.3和7.4)。

# 7.4.2保持灵活性和减少软件工程成本

组合的主要目的是提高效率和减少通信成本,但也要注意保持足够的灵活性和降低软件工程代价。

在组合时，易于作出对算法的可扩放性带来不必要限制的决定,要维持一个算法(或程序)的可移植性和可扩放性，则创建可变数目的任务是很关键的，而组合时往往会使问题的任务数的变化范围受到限制。为了易于在映射时平衡负载,组合后的任务数,按照经验，至少应比处理器的数目多一个量级。其最优的任务数可由分析模型和实际经验共同决定。但灵活性也不一定需要一个设计总是创建大量的任务。粒度可由编译或运行参数来控制。重要的是，一个设计不要对能够生成的任务数加人不必要的限制。

组合时另一个应关心的问题是尽量减少软件工程代价,当并行化一个串行代码时,应尽量减少代码的巨大变化以减少软件开发开销,由此观点出发,最感兴趣的策略就是那些在算法设计时不需要大量修改代码的策略。

# 7.4.3组合判据

下面的一组问答题,可检验组合设计是否合理,原则上讲,应给予它们肯定的回答：

$\textcircled{1}$ 用增加局部性方法施行组合是否减少了通信成本？如果不是,检查能否由别的组合策略来达到。  
$\textcircled{2}$ 如果组合已造成重复计算，是否已权衡了其得益？  
$\textcircled{3}$ 如果组合已重复了数据,是否已证实这不会因限制问题尺寸和处理器数的变化范围而牺牲了可扩放性？  
$\textcircled{4}$ 由组合所产生的任务是否具有类似的计算和通信代价？  
$\textcircled{5}$ 任务数目是否仍然与问题尺寸成比例？如果不是,算法则是不可扩放的。  
$\textcircled{6}$ 如果组合减少了并行执行的机会，是否已证实现在的并发性仍能适应目前和将来的并行机？  
②在不导致负载不平衡,不增加软件工程代价和不减少可扩放性的前提下,任务数能否再进一步减少,在其它条件等同时,创建较少的大粒度的任务算法通常是简单高效的。  
⑧如果并行化现有的串行程序,是否考虑了修改串行代码所增加的成本？如果此成本是高的，应考虑别的组合策略，它能增加代码重用的机会。

# 7.5映 射

在设计的最后阶段,我们要指定每个任务到哪里去执行,此即映射（Map-ping)。开发映射的主要目的是减少算法的总的执行时间，其策略有二：一是把那些能够并发执行的任务放在不同的处理器上以增强并行度；二是把那些需频繁通信的任务置于同一个处理器上以提高局部性。这两个策略有时会冲突，这就需要权衡。

对于两个处理器而言,映射问题有最佳解;当处理器的数目大于等于3时，此问题是NP完全问题,但我们可以利用关于特定策略的知识，用启发式算法来获得有效的解。

在进行映射时,对于许多用域分解技术开发的算法，有固定数目的等尺寸任务,有结构化的局部/全局通信,此时映射很简单；对于更复杂的域分解算法,每个任务的工作量可能不一样,通信也许是非结构化的，有效的组合就不那么容易，此时可能要采用负载平衡算法。

在基于功能分解的算法中，常常会产生一些由短暂任务组成的计算，它们只在执行的开始与结束时需与别的任务协调，此时我们可以用任务调度（Task-Scheduling)算法来分配任务给那些可能处于空闲状态的处理器。

# 7.5.1负载平衡算法

基于域分解技术的算法有很多专用和通用的负载平衡技术(Load-BalancingTechniques),它们都是试图将划分阶段产生的细粒度任务组合成每一个处理器一个粗粒度的任务。下面简单介绍几种有代表性的方法。

递归对剖(Recursive Bisection）递归对剖技术用来将一个域划分成计算成本大致相等的子域,同时试图使通信代价最小,为此常使用分治方法：域首先在一维方向上分割成两个子域;然后分割以递归的方式在两个子域中进行，直至子域数和所要求的任务数一样多。

最直截了当的递归对剖技术是递归坐标对剖（RecursiveCoordinate Bisec-tion)它通常应用于非规整格点。这种技术所作的分割是基于域中物理格点坐标,每一步都沿较长的维进行划分。其优点是简单和低价，其缺点是不能优化通信性能。

递归对剖的一种变体叫做非平衡递归对剖（Unbalanced RecursiveBisec-tion),它使用具有较好长宽比(AspectsRatios)的子格点以降低通信成本,虽增加了计算划分的成本但却减少了通信成本。

还有一种称为递归图对剖(Recursive Graph Bisection)的技术,对复杂的非结构化的格点很有用，它使用连通信息来减少跨子域的格边数，从而可降低通信要求。

局部算法上述描述的技术是很昂贵的，因为它们都要求计算状态的全局知识。相反，局部负载平衡算法，只是使用邻近处理器的负载信息，来周期性地调整自己的负载，或转移到邻居，或从邻居迁人。例如，对于如图7.10所示的网格问题，每个处理器周期地与周围的处理器比较它们的计算负载，如果它们的差异超过了某个阈值就施行计算负载的迁移。

![](images/faff02f0ea2874ee8a3204e918a895b26393e14e2fb519cc1c85f15d8f677283.jpg)  
图7.10网格问题中的负载平衡

概率方法(Probabilistic Method）这是一种特别简单的方法，它将任务随机地分配给处理器。如果任务数足够多，则每个处理器预计能分配大致等量的计算,其优点是低价和可扩放性;缺点是要求跨处理器的通信和只有当任务数多于处理器数时才可能达到预期的负载分配。概率方法，当任务间很少有通信，和/或通信模式很少呈局部性时，才有可能最有效。

循环映射(Cyclic Mapping）如果知道每个格点计算负载是变化的,且呈现明显的空间局部性,则我们可以使用所谓循环指派法，即采用某种枚举方法，轮流地将各处理器分配给诸计算任务。这种方法可能使负载平衡，但牺牲了局部性且通信可能会增加。

此外,块循环分配(Block Cyclie Distribution)也是一种可能的处理器映射方法,此时,任务按块的形式轮流分配给处理器。

总之，递归对剖法需全局知识,性能好但代价高；局部算法代价小,但当负载变化大时调整很慢;概率方法代价低,可扩放性好，但通信代价可能较大，且只适用于任务数远多于处理器数时；循环映射技术实际是概率映射的一种形式，而概率方法比其它技术易于导致可观的通信。

# 7.5.2任务调度算法

当使用功能分解时，产生了很多弱局部性要求的任务。这些任务通常放在集中的或分散的任务池中,然后使用任务调度算法,将池中的任务分配给特定的处理器。

任务调度算法最关键之处是任务分配策略。策略的选择应在独立运算（以减少通信成本)和计算状态的全局知识(以改善负载平衡)之间折衷,常用的调度模式有经理/雇员方式和非集中方式,在非集中调度方案中,怎样检测整个问题的求解是否已经完成也是一个必须考虑的问题。

经理/雇员模式如图7.11所示，中心(经理)任务负责任务分配,每个雇员重复地从经理那里请求并执行具体任务。此策略的有效性依赖于雇员数和执行任务的成本，使用预取方法(以使计算和通信重叠)和缓存方法(使得雇员无任务时经理和雇员才通信)可以改善效率。这种方案的一种变体是层次经理/雇员模式,它将诸雇员分成不相交的集合,每一个都有一个小经理,雇员们从小经理那里领取任务,并周期地与经理和小经理施行通信。

![](images/0493fd6e528e4bd1e813d77322334a2143f9385eb36071fe5464e869488bf815.jpg)  
图7.11经理/雇员调度模式

非集中模式它也就是无中心管理者的分布式调度法。在每个处理器中均维持一个任务池,这些任务池实际上就变成了可供请求者异步访问的分布的数据结构。

结束检测任务调度算法需要一种机构检测何时操作结束,否则,空闲的雇员们将永不停止地发出工作请求,这种检测机构在集中式算法中容易实现,因为经理能容易地决定何时雇员们都空闲了;在分布式算法中则较困难，因为没有一个中央机构记录雇员空闲状况。

# 7.5.3映射判据

下面的一组问答题,可检验你所作的映射设计是否合理。.原则上讲，应给予它们肯定的回答：

① 如果采用集中式负载平衡方案,你是否已验证中央管理者不会成为瓶颈?

$\textcircled{2}$ 如果采用动态负载平衡方案,你是否衡量过不同策略的成本？

$\textcircled{3}$ 如果采用概率或循环法，你是否有足够多的任务来保证合理的负载平衡？典型地，任务数应10倍于处理器数。

$\textcircled{4}$ 如果要为一个复杂问题设计一个SPMD程序，你是否考虑过基于动态任务创建和消除的算法：后者可能得到一个更简单的算法，但性能可能有问题。

# 7.6小结和导读

小结本章已经描述了并行算法设计的四个步骤：首先将给定问题划分成一些小的任务，划分方法可以使用域分解法或功能分解法;其次分析诸任务之间的通信需求,通信可以是局部的和全局的，静态的和动态的，结构化的和非结构化的以及同步的和异步的;然后使用组合方法，在尽可能保持灵活性的同时,减少通信和开发成本;最终以最小化总执行时间为目标将诸任务分配给处理器，使用负载平衡和任务调度技术可以改善映射的质量，在每个设计步骤之后均列出了相应的设计检验准则以评价设计的好坏。

经过上述四个步骤设计出的并行算法，在开始编码实现之前尚须考虑以下几件事：对算法进行性能分析以选择好的算法，根据要求证实所作的设计是否满意,考虑算法具体实现时的代价和代码重用的可能性;最终考虑如何将算法装配到一个更大的系统中去。

通过上面的学习之后,我们最好以一个实例来加深课文中所述设计原理的理解以及阐述开发设计一个并行算法的逐步过程,为此我们在本章的习题中给出了一个综合练习，通过它读者一方面可以了解针对给定问题设计一个并行算法的全过程;另一方面也促使读者独立回答一些问题，,以达到复习巩固的目的。

导读论述算法程序设计过程的一篇经典文章是[139]。在实用的、可扩放的并行机上设计并行算法,读者可参阅[69,71]。并行程序的设计,读者参阅[41]。

映射问题的研究在计算机科学中很受重视。有关递归坐标对剖算法，读者可参阅[28];非平衡递归对剖算法由[105]提出，使用连通信息的递归对剖算法，读者可参阅[142];[160]等比较了划分非结构化网孔的不同算法，包括坐标对剖部，图对剖等；[69,131]等描述了循环分解法：[120]等描述了局部算法；有关调度结束检测算法，读者可参阅[59,148]。其它相关的文献包括[29,86,56,89,121,113,152]。[67]中的第2章集中地讨论了并行算法的设计方法学,章末的注释中列举了大量的有关此方面的参考文献，有兴趣的读者可追踪阅读。

# 习 题

7.1算法7.1是一个组合搜索算法,每当调用该算法扩展一个搜索树节点时,就检查该节点是否代表了一个问题的解：如果不是，则算法作递归调用以扩展其子节点。

算法7.1 SISD上组合搜索算法   
输入：给定问题A   
输出：问题A的解   
Procedure : SEARCH( A)   
Begin if(Solution(A)) then $\mathsf { S c o r e } = \mathsf { e v a l } ( \mathbf { A } )$ Report Solution and Score else for each child $\mathsf { A } ( { \boldsymbol { \mathbf { \mathit { i } } } } )$ of A do SEARCH(A(i)) endfor endif   
End

(1)如何构造此问题的并行搜索算法?

7.2分治策略是常用的问题求解技术,其算法可形式描述如下：

算法7.2 SISD上分治(D&C)算法   
输入：问题输人集   
输出：问题的解   
Begin if base case then solve problem else (1)partition problem into subproblem L and R (2)solve L using D&C (3)solve R using D&C (4)combine solutions to problem L and R endif

试用此算法求解 $N = 3 2$ 的全和,并画出相应的求和树。

7.3画出图7.8二叉树的通信图,并分析其计算和通信次数。

7.4画出图7.9蝶式图的通信图,并分析其计算和通信次数。

7.5(1）对于 $1 2 \times 6 = 7 2$ 个网格点，如有 $\pmb { \hat { p } = 1 2 }$ 个处理器，如何用循环指派法分配处理器？

(2）对于 ${ 8 \times 8 } = 6 4$ 个网格点，如有 ${ \pmb \phi } = { \pmb 4 }$ 个处理器，如何用循环指派法分配处理器？

(3)对于(1)和(2)两种情况,如何用块循环指派法分配处理器?

7.6设计并实现使用3点格式的1-D有限差分并行算法,假定每个处理器上分配一个任务，试分析所设计算法的性能。

7.7设计并实现使用5点格式的2-D有限差分的2-D分解并行算法，假定每个处理器上分配一个任务。试分析该算法的性能。

7.8试设计一个1-D和2-D格点的Gauss-Seidel并行算法。

7.9综合练习一大气模型的算法设计。

# (1)背影知识

大气模型(AtmosphereModel)是模拟影响气候的大气过程(风、云、雨等)的计算机程序，它可用来研究龙卷风的演变,预测明天的天气,或者研究大气中 $\mathrm { C O } _ { 2 }$ 浓度对气候的影响。大气模型是求解一组PDE方程,它描述大气基本流体动力学行为。这组方程的连续空间行为可用空间中的有限的离散点的行为近似表征。典型地，这些离散点都位于长方形经纬网格$N _ { x } \times N _ { y } \times N _ { z }$ 上,其中 $\ N _ { x } { \approx } 2 N _ { y } , N _ { y }$ 的区间为 ${ \mathfrak { s o } } \sim { \mathfrak { s o } } 0 , N _ { z }$ 的区间为 $1 5 \sim 3 0$ （如图7.12所示)。在每个格点上用一向量表示,其值代表该格点的压力、温度、风速、湿度等。大气模型执行时间积分，它根据当前状态决定将来的大气状态,积分逐步前进,每计算一固定量就前进一步,假定使用9点格式(Nine-Point Stencil)有限差分方法修改格点在水平维运动之值，用3点格式修改垂直维运动之值(如图7.13所示)。大气模型涉及到在规整的三维网格上执行有限差分计算,它是一大类科学数值计算的代表,大气模型包含了如下的一组基本预测方程,其中$\phi$ 和 $\lambda$ 是纬线和经线， $\pmb { z }$ 是高度， $\pmb { u }$ 和 $_ { v }$ 是速度的水平分量， $\pmb { w }$ 是垂直分量， $\pmb { \mathscr { p } }$ 是压力， $\rho$ 是密度， $T$ 是温度， $f$ 是洛伦兹力， $\pmb { g }$ 是重力， $F$ 和 $\pmb { Q }$ 是外力， $C _ { p }$ 是热容， $^ a$ 是地球半经， $R$ 为常数：

![](images/d79936d179c878db011639291802039b5640ddaaf25d263c753a37fa5c6dfc14.jpg)  
图7.12大气状态三维格点表示

![](images/affa7b08bb6a2a95f8c07dc45abe6fba07cf7dad00be4af3d33886581386c9a4.jpg)  
图7.13大气模型中使用的有限差分格式

$$
\begin{array} { r l } & { \frac { \mathrm { d } u } { \mathrm { d } t } - ( f + u \frac { \tan \phi } { a } ) _ { v } = - \frac { 1 } { a \cos \phi } \frac { 1 } { \rho } \frac { \partial \phi } { \partial \lambda } + F _ { \lambda } } \\ & { \frac { \mathrm { d } v } { \mathrm { d } t } + ( f + u \frac { \tan \phi } { a } ) _ { u } = \frac { 1 } { \rho a } \frac { \partial \phi } { \partial \phi } + F _ { \phi } } \end{array}
$$

流体静力学方程：g=-1p

质量守恒 $\frac { \partial \phi } { \partial t } = - \frac { 1 } { a \cos \phi } ( \frac { \partial } { \partial \lambda } ( \rho u ) + \frac { \partial } { \partial \phi } ( \rho v \cos \phi ) ) - \frac { \partial } { \partial z } ( \rho w )$   
能量守恒 $C _ { P } \frac { \mathrm { d } T } { \mathrm { d } t } - \frac { 1 } { \rho } \frac { \mathrm { d } \phi } { \mathrm { d } t } = Q$   
大气状态方程： $\scriptstyle { p = \rho R T }$

# (2)设计分析

划分在大气模型中,可用格点代表大气的状态,所以域分解是很自然的。参照图7.2,分解在 $x , y , z$ 方向上均是可能的。如果为了开拓最大并行度,则可将每个格点定义为一个任务，试问总共有多少个任务？

通信在大气模型中有三种不同形式的通信： $\textcircled{1}$ 有限差分格点计算引起的通信：在细粒度分解时,每个格点代表一个任务。参照图7.13,如在水平维使用9点格式,垂直使用3点格式，则格点间的通信量是多少？②全局计算所引起的通信：大气模型中,要周期性地计算大气质量，令 $M _ { i , j , k }$ 表示格点 $( { \ : } _ { i } , { \ : } _ { j } , k )$ 处的大气质量,则总质量为：

$$
T o t a l M a s s = \sum _ { i = 0 } ^ { N _ { x } - 1 N _ { y } - 1 N _ { z } - 1 } \sum _ { j = 0 } ^ { J - 1 } M _ { i , j , k }
$$

试问如何并行计算(7.10)式？③物理计算所引起的通信：由于一个格点视为一个任务，则大气模型物理分量的计算要求相当多的通信,例如在第k层(k≥1)的全晴空(TCS)(Total ClearSky)定义如下：

$$
\mathrm { T C S } _ { k } = \ \prod _ { i = 1 } ^ { k } \ ( 1 - \mathrm { c l d } _ { i } ) \mathrm { T C S } _ { i } = \mathrm { T C S } _ { k - 1 } ( 1 - \mathrm { c l d } _ { k } )
$$

其中,第0层是大气顶层,cld;是第i层的云的比例小数。试问如何并行计算(7.11)式?此时每个格点每个时间步总共需要多少次通信？试用通信判据评价一下所作的通信设计。

组合当使用细粒度的域分解时,任务数似乎是大的，似应进行组合：参照图7.14,少量的组合(每个任务从1个格点到4个格点)能减少9点格式计算所引起的通信需求(每个任务每个时间步从8条信息到4条信息);水平维通信需求相对较小，仅4条信息(8个数据）,而在垂直时，除了有限差分格式的计算所需的通信外(2条信息,2个数据),还有不同物理分量的计算(见(7.11)式),所以组合应在哪个方向上进行？从软件工程的角度,为了减少开销，应允许现行的串行代码尽量能在并行程序中不加修改地被重用,试问组合应在什么方向上进行？为什么？经过上述的组合分析，组合后任务数大约是多少？

![](images/bb7eb3fd4b31e0e238b4c2157f7f3f79622cbe56c3cc783601a90bfd5ac93360.jpg)  
图7.14大气模型中的组合方法

映射在不存在负载不平衡的情况下，可以使用图7.15所示的简单映射策略,每个处理器指派给单一任务。此任务负责多列的计算，从而可产生一个 SPMD程序，此分配策略如果每个任务每个时间步内执行等量计算,则是很有效的,但在大气模型中其物理分量计算变化相当大,例如辐射计算不能在晚上，云雾形成必须温度超过一定阈值。

![](images/c057959e39dd53a7b0b164d8a6599d1fe2ac35f3d1809dbade71d8d1aaea03c0.jpg)  
图7.15大气模型中的均匀映射

此类计算负载的变化能导至效率下降20%或更多，当此值不能接受时，应考虑别的映射方式,例如循环指派法，试解释采用循环映射的大气模型为何能改善负载平衡状态？

最后请你给出一个简短结论：即大气模型应使用几维划分？什么类型的分解？应该怎样组合？如何进行映射？

# 第三篇 并行数值算法

第八章 基本通信操作第九章 稠密矩阵运算第十章 线性方程组的求解第十一章 快速傅里叶变换

这一篇主要研究数值计算问题的并行算法,包括矩阵运算(第九章）、线性方程组的求解(第十章)和快速傅里叶变换(第十一章)。其中，矩阵运算是数值计算中最重要的一类运算，是线性代数和数值分析中最基本的运算操作；稠密和稀疏线性方程组是大型科学工程计算中最常用的数值计算问题;快速离散变换是数字信号处理等应用领域中最主要的数值计算形式。这些数值计算问题的特点是： $\textcircled{1}$ 计算量一般都涉及到一个具体的物理量,其数值可用实数(即浮点数),也可用虚数表示； $\textcircled{2}$ 求解问题的依据是基于数值分析中的数学原理； $\textcircled{3}$ 求解问题的算法可用直接法，但更普遍的是迭代法，且在理论上讲，每次迭代都应改善前一步的计算结果； $\textcircled{4}$ 计算结果，一般均应是满足预定精度要求的近似解。在讨论算法时，对数值计算的稳定性、收敛速度和精度分析等基本问题，乃是直接利用数值分析中的数学原理和结论，而着重讨论计算问题的基本原理,设计串行算法和分析串行算法中的并行性及并行化方法，对于有些典型问题还给出相应的并行算法。

由于任何并行算法，在执行时总会涉及到处理器之间的相互通信问题,所以本篇一开始(第八章)还讨论了在环、二维网孔和超立方等结构上,采用确定选路算法和存储转发与切通开关技术,进行一到一、一到多和多到多等一些基本通信操作。这些并非针对数值计算的问题,对于非数值并行算法也同样存在。

# 第八章 基本通信操作

大多数并行算法均会涉及到处理器间的数据(本章下文称消息)交换。数据交换方式可归结为处理器间的通信操作，而通信操作各式各样,本章只研究下一章矩阵运算中所使用的最频繁的一些基本通信操作，包括研究通信操作与处理器之间的互连拓扑，通信选路策略和消息传递机制关系。本章讨论采用确定的维序(Dimension-Ordering)选择方法,使用存储转发(Store-and-Forward,简记之为SF)和切通(Cut-Through,简记之为CT)开关技术，在环、二维网孔和超立方等连接上进行一到一、一到多、多到多等一些基本通信操作。：

# 8.1 选路方法与开关技术

# 8.1.1选路方法

所谓选路(Routing)系指消息从发源地到达目的地所取的走法，即行进的方法。-般可分为最短(Minimal)法和非最短(Nonminimal)法,有时相应地称为贪心(Greedy)法和随机(Random)法。贪心法总是在源和目的之间试图选择最短的路径,但往往会造成拥挤。随机法虽可能选路长度较长,但不易造成拥挤。选路方法也可分为确定的(Deterministic)和自适应的(Adaptive)：前者在源和目的之间确定一条唯一的路径;后者根据行进中的网络状态信息而自动地确定路径。

一种最常用确定的最短选路法是维序选路(Dimension-Ordered Routing)法，它是根据通信通道(下文也叫作链路、信道等)的维来确定消息如何穿越相继的通道。当此方法用于二维网孔中时就称为X-Y选路法,用于超立方网络中时就称为E-立方(E-Cube)选路法。

X-Y选路法在二维网孔中选路时,首先沿 $X$ 维方向确定路径,然后再沿$Y$ 维方向确定路径。

# 算法8.1 二维网孔上的X-Y选路算法

输入：待选路的信包(Packet)处于源处理器中输出：将各信包送至各自的目的地中

# Begin

（1）沿 $X$ 维将信包向左或向右选路至目的处理器所在的列(2）沿 $Y$ 维将信包向上或向下选路至目的处理器所在的行

End

例8.1 图8.1中示出了4个(源;目的)对的X-Y选路过程,其中节点(2,1)要选路到节点(7,6),节点(0,7)要选路到节点(4,2),节点(5,4)要选路到节点(2,0),节点(6,3)要选路到节点(1,5)。显然它们不会出现死锁或循环等待现象。□

![](images/c07c35fe5945a7305b90b3d868034c5e02ea9a288ff5181d3d3b91d5b536b2d4.jpg)  
图8.1 ${ \bf 8 \times 8 }$ 二维网孔中4个(源;目的)对的X-Y选路

E-立方选路法对于 $N = 2 ^ { n }$ 个节点的 $\pmb { n }$ 维立方体,令源节点的二进制编码为 $S = { s _ { n - 1 } } ^ { \dots } { s _ { 1 } } { s _ { 0 } }$ ,目的节点的二进制编码为 $D = d _ { n - 1 } \cdots d _ { 1 } d _ { 0 } ,$ 将 $\pmb { n }$ 维表示成i=1,2,…,n,其中第i维对应于节点地址的第i-1位。设V=Un-1,,10是路径中的任一中间节点，则确定一条从源 $S$ 到目的 $D$ 的E－立方选路算法如下：

# 算法8.2超立方网络上的E-立方选路算法

输入：待选路的信包在源处理器中输出：将源处理器中的信包送至其目的地

# Begin

(1)for $i = 1$ to $\pmb { n }$ do $\big / \ast$ 计算方向位 $\yen 7$ $r _ { i } = { { s _ { i - 1 } } \bigoplus { d _ { i - 1 } } }$ /\*为异-或运算符 $\star$ / end for   
(2) $i = 1 , V = S / \ast \sharp \sharp \sharp \ast /$   
(3）while $i \leqslant n$ do (3.1)if $r _ { i } = 1$ then从当前节点 $V$ 选路到节点为 $V \textcircled { + } 2 ^ { i - 1 }$ endif (3.2) $i = i + 1$

# endwhile

End

例8.2图8.2中示出了4维超立方的E-立方选路过程,其中 $\pmb { n } = 4$ ， $s =$ 0110, $D = 1 1 0 1 , R = r _ { 4 } r _ { 3 } r _ { 2 } r _ { 1 } = 1 0 1 1$ 。由于 $r _ { 1 } = 0 \oplus 1 = 1$ ,所以 $s$ 的下一节点为$s \oplus 2 ^ { 0 } = 0 1 1 1$ ；同样由于 $r _ { 2 } = 1 \oplus 0 = 1$ ，所以 $V = 0 1 1 1$ 的下一节点为 $V \bigoplus 2 ^ { 1 } =$ 0101;由于 $r _ { 3 } = 1 \oplus 1 = 0$ ,所以跳过第 ${ \dot { \pmb { \mathscr { i } } } } = 3$ 维；最后由于 ${ r _ { 4 } } = 0 \bigoplus 1 = 1$ ,所以 $v =$ 0101就选路到节点 $V \oplus 2 ^ { 3 } = 1 1 0 1$ ,它就是目的地。□

![](images/27f3b750e7565fef651eb25ad5b040b503be23d18f5f74664768eacd695a139a.jpg)  
图8.24维超立方中的E-立方选路

# 8.1.2开关技术

消息格式通信中乐于使用消息(Message)这一术语，它是节点间通信的逻辑单位，如图8.3所示，通常由一些定长的信包(Packet)组成。信包是带有选路信息的基本通信单位，可以把它分成一些定长的数据片,其中选路信息和顺序号作为(包)头，其余的是数据。消息格式的改进使开关技术由存储转发式演变成更先进的虫蚀(Wormhole)方式。

存储转发(SF)选路在存储转发网络中信包是基本的传输单位。在传输过程中，中间节点必须收齐且存储在缓冲器中后，它才可能传向下一节点（如图8.4(a)所示）。

令 $t _ { \textrm { s } }$ 是启动时间(包括打包、执行选路算法和建立通信介面的时间）， $t _ { \mathrm { h } }$ 是节点延迟时间(即包头穿越网络中两直接相连的处理器所需的时间）， $\pmb { t } _ { \mathbf { w } }$ 是传输每个字的时间(它是带宽的倒数）。

对于长度为 $_ { m }$ 的信包，穿越 $\iota$ 条链路,在存储转发的网络中总通信时间为：

$$
t _ { \mathrm { c o m m } } ( \mathrm { S F } ) = t _ { \mathrm { s } } + ( m t _ { \mathrm { w } } + t _ { \mathrm { h } } ) l
$$

如果 $t _ { \mathrm { h } } = t _ { \mathrm { s } } = 0 , t _ { \mathrm { w } } = 1$ ,则

$$
t _ { \mathrm { c o m m } } ( \mathrm { S F } ) = { \cal O } ( m \cdot l )
$$

![](images/c2340711f2f64f4d79265b821990142acb920fea9f22f405d8a48974e4e17fac.jpg)  
图8.3消息、信包和片的格式

![](images/397a683933c50b17f88cc213cf48630aa0a716d9d1f7bf4e5cdb7ddd47fe0d8f.jpg)  
图8.4两种开关技术的时间比较(a)SF通信时间；（b)CT通信时间

切通(CT)选路在切通网络中将信包进一步分成更小的片(数据片和包头)进行传输。虫蚀(Wormhole)选路是切通选路的一种形式。在传输过程中，中间节点只备有很小的片缓冲器，一旦收到包头就传至下一节点。同一信包中的所有片一同以流水线方式穿越网络(如图8.4(b)所示)。整个信包犹如一列火车,由火车头(包头)牵引着车厢(数据片)顺序前进。

对于长度为 $_ { \pmb { m } }$ 的信包,穿越 $\iota$ 条链路,在切通的网络中总通信时间为：

$$
t _ { \mathrm { c o m m } } ( \mathrm { C T } ) = t _ { s } + m t _ { \mathrm { w } } + l t _ { \mathrm { h } }
$$

如果 $t _ { \mathrm { s } } = 0 , t _ { \mathrm { h } } = t _ { \mathrm { w } } = 1$ ，则

$$
t _ { \mathrm { c o m m } } ( \mathbf { C T } ) = O ( m + l )
$$

一般情况下, $t _ { \textrm { s } }$ 是不容忽略的,而片的大小是远小于 $_ { m }$ 的,同时 $\pmb { t } _ { \mathbf { w } }$ 通常也比 $t _ { \boldsymbol { \mathrm { h } } }$ 大得多,所以(8.1)式和(8.2)式可近似写为：

$$
t _ { \mathrm { c o m m } } ( \mathrm { S F } ) = t _ { \mathrm { s } } + m t _ { \mathrm { w } } \cdot l
$$

$$
t _ { \mathrm { { c o m m } } } ( \mathrm { C T } ) = t _ { \mathrm { { s } } } + m t _ { \mathrm { { w } } }
$$

(8.1b)和(8.2b)式表明了这样的事实：存储转发网络的延迟与源和目的之间的距离成正比;而切通网络的延迟时间与源和目的之间的距离无关。

# 8.2单一信包一到一传输

单一信包施行点对点一到一传输是最基本的通信操作。当计算通信时间$t _ { \mathrm { c o m m } }$ 时， $l$ 是个重要参数。在具有 $\pmb { \mathscr { P } }$ 个处理器规则互连的网络中,它可定量计算之。

I的计算对于 $\pmb { \hat { p } }$ 个处理器连成环形， $\iota$ 至多为 $\pmb { \phi } / 2 . 1$ ;对于 $\sqrt { \pmb { \mathscr { p } } } \times \sqrt { \pmb { \mathscr { p } } }$ 个处理器连成周边环绕正方网孔(Wraparound Square Mesh),l至多为2L√p/2」；对于p个处理器连成超立方体,l至多为logp。一般的非规则互连的网络中的l并非容易计算。

SF网络传输时间上界单一信包用SF方式选路,在环上的通信时间为ts+twmLp/2」;在周边环绕正方网孔上的通信时间为ts+2twmL√p/2」;在超立方上的通信时间为ts+twmlogp。

CT网络传输时间使用CT方式,将单一信包从源直接发送至l远的目的地的通信时间为ts+twm+thl。对于m充分大的信包使用CT方式传输时,处理器之间传输单一信包的时间,与用SF方式在两直接相连的处理器之间传输单一信包的时间基本一样。

# 8.3一到多播送

所谓一到多播送(One-to-All Broadcast),是指开始时 $\mathrm { P } _ { 0 }$ 中保存有信包 $M$ ，播送结束后所有其它处理器中均得到信包 $m _ { \circ }$ 一到多播送的反操作叫作单点累积(Single-Node Accumulation),两者在以后讨论的数值算法中均经常使用。

# 8.3.1 使用 SF进行一到多播送

环约定环是双向的,且每个处理器一次只能发送一条信包。在8个处理器环上,使用 SF方式进行播送,其过程如图8.5所示,其中虚线箭头上的数字表示发送时间步。

![](images/62c85a068a88ef762c478263f506188fe31d3d305a50c3f84198d4a37e7d8293.jpg)  
图8.58个处理器的环上以SF方式播送过程

显然,在 $\pmb { \phi }$ 个处理器的环上,用SF方式进行播送的通信时间为：

$$
t _ { \mathrm { o n e - t o - a l l } } ( \mathrm { S F } ) = ( t _ { s } + m t _ { \mathrm { w } } ) \lceil \hat { p } / 2 \rceil
$$

环绕网孔一个 $\hat { \pmb { p } }$ 个处理器的正方网孔可以视为其行和列均由 $\sqrt { \pmb { \phi } }$ 个处理器所组成的环，所以可以使用环上播送方法来讨论网孔上的播送。在16个处理器环绕网孔上,使用 SF方式进行播送,其过程如图8.6所示。同样，虚线箭头上的数字表示发送时间步。

在 $\pmb { \mathscr { P } }$ 个处理器的环绕网孔上用 SF方式进行播送时，先完成一行中的播送，再同时进行各列中的播送,显然其通信时间为：

$$
t _ { \mathrm { o n e - t o - a l l } } ( \mathrm { S F } ) { = } 2 ( t _ { \mathrm { s } } + m t _ { \mathrm { w } } ) \Gamma \sqrt { \hat { p } } / 2 \rceil
$$

不难推知在三维网孔上施行播送的通信时间为：

$$
t _ { \mathrm { o n e - t o - a l l } } ( \mathrm { S F } ) = 3 ( t _ { \mathrm { s } } + m t _ { \mathrm { w } } ) \lceil p ^ { 1 / 3 } / 2 \rceil
$$

超立方一个有2d个处理器的超立方可以视为每维仅有2个处理器的d维网孔，因此网孔上的播送方法可以推广到超立方上。在8个处理器的超立方上,使用SF方式进行播送,其过程如图8.7所示。照例，虚线箭头上的数字表示发送时间步。

![](images/21bcc4e2850a9d82765845ef36b77a9a81d934b6b7e589d5d9585c5410091b4f.jpg)  
图8.616个处理器的环绕网孔上以 SF方式播送过程

不难计算出 $\pmb { \mathscr { P } }$ 个处理器的超立方上,用SF方式进行播送通信时间为：

$$
t _ { \mathrm { o n e - t o - a l i } } ( \mathrm { S F } ) = ( t _ { \mathrm { s } } + m t _ { \mathrm { w } } ) \log { \phi }
$$

![](images/40c388f45050b4f39a0b755293b7a7d8649507d0ff554d881a9d9c44000a8fa2.jpg)  
图8.78个处理器的超立方上以 SF方式播送过程

# 8.3.2使用CT进行一到多播送

环因为使用CT选路时,通信时间与中继节点无关,所以可以将超立方上的播送算法直接映射到环上。为此,对于一个如图8.8所示的8个处理器环，可以参照图8.7：先按高维播送，再按中维播送，最后按低维播送就可完成播送。剩下的问题是如何计算它的通信时间。

当按照图8.8所示的方式播送信包时，源处理器首先发送信包至p/2远的处理器;其次是已收到信包的处理器将它发送至p/4远的处理器。一般在第i步时信包发送的距离为p/2i,其通信时间为ts+mtw+thp/2i。因此总的通信时间为：

$$
t _ { \mathrm { o n e - t o - a l l } } ( \mathrm { C T } ) = \sum _ { i = 1 } ^ { \log p } ~ ( t _ { \mathrm { s } } + m t _ { \mathrm { w } } + t _ { \mathrm { h } } \phi / 2 ^ { i } )
$$