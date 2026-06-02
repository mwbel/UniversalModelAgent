Moore定律，为夺性能/价格之冠,产品必须在短期内开发成功； $\textcircled{2}$ 通用：SP必须是个能支持不同的技术和商业应用、流行的编程模式和不同操作模式的通用系统； $\textcircled{3}$ 高性能：SP必须提供整体性能,不仅是处理器速度快，而且存储器和通信系统要快，有优良的编译器和各种库等； $\textcircled{4}$ 有效性：SP必须呈现好的可靠性和可用性,使得用户能够方便地在其上运行商业成品代码。为了满足上述目的,IBM设计小分队采用的策略是：灵活的机群结构;专用互连网络;标准的系统环境；标准的编程模式和有选择的单一系统映像支持。

$\textcircled{1}$ 机群结构：为了达到赶市场和通用的目的,选用机群结构是个关键，其中每个节点都是个RS/6000工作站且各有本地磁盘;每个节点内驻留一个完整的AIX(IBM的Unix);各节点经其I/O总线(非本地存储总线)连向专门设计的多级高速网络。SP系列尽量使用标准的工作站组件,只有不能满足要求时才使用专用的硬件和软件。这样的结构既简单又灵活且系统的规模是可扩放的（从很少的几个节点到数百个节点)。

②标准环境:SP使用标准的、开放式的、分布式Unix环境，它能利用现存的标准软件以进行系统管理、作业管理、存储管理等,所有这些软件IBM工作站AIX操作系统中均有。对于那些AIX环境不能有效执行的应用,SP 提供了一组高性能服务，诸如高性能开关(HPS)、用户级通信协议(US协议）、优化的消息传递库(MPL）、并行程序开发和执行环境、并行文件系统、并行数据库和高性能I/O子系统等。

③标准编程模式：SP系统以标准编程模式支持以下三种应用方式：①串行计算：尽管 SP2是个并行机,但它允许现有的以C、C++和 Fortran编写的串行程序可不加修改地运行在单节点的SP系统上,这是可以理解的，因为机群结构和标准的环境确保了这一点;②并行科技计算:SP现在支持MPL、MPI、PVM、HPF模式,正打算支持共享存储的模式;③并行商用计算：IBM正在并行化一些关键数据库、事务监视子系统,现今IBMDB2数据库系统的并行版本已在 SP2上实现。

④系统可用性：SP系统由上千个部件组成，它们原先是为低价的、规模不大的工作站设计的,现把它们组织在一起必然经常失效。但SP是个机群结构，而机群结构意味着是一个分开的操作系统映像,它和SMP结构驻留在共享存储器中的单一操作系统映像不同(它的OS出错将导致全系统崩溃),机群结构一个节点映像失效不会导致全系统崩溃;另外SP的诸节点均同时连向以太网和高性能开关网,这样一个网络的失效，节点间还可使用另一个网络进行通信；还有 SP的软件基础设施也提供了故障检测、诊断、系统重组和故障恢复等服务。

③ 部分单一系统映像：在一个分布系统中,用户看到的是一些单独的、分开的工作站，真正的单一系统映像是很难实现的，且对某些商业应用它也不是个关键的要求。所以IBM的设计者们，只是在单进入点、单文件层、单控制点和单作业管理系统方面实现了单一系统映像，而在SP系统中并不实现单地址空间。

系统结构SP系统简化框图如图2.9所示。一个SP系统可含 $2 \sim 5 1 2$ 个节点，每个节点有其自己的局存和本地磁盘。所有的节点均连向两个网络：普通的以太网和HPS(High Performance Switch）。以太网虽慢但有很多好处：当HPS失效时，它可作为后援；当HPS正被开发或改进时，仍可利用以太网查错、测试和维持系统运行；此外以太网也可用来系统监视、引导、加载和管理等。

![](images/942e4df6865015a4504a5d9222fb275e4871d88426ef523bc50a82be84fe3c9d.jpg)  
图2.9SP系统结构

①系统互连：高性能开关（HPS)由节点内的开关硬件和开关帧（SwitchFrames)组成。图2.10示出了IBMSP2中所使用的128路高性能开关，其中每帧由一个16路开关板所连接的16个处理节点(No～N15）所组成,8个帧再用一个附加级开关板连接起来(图中细线代表8位的双向链路，而粗线代表4个8位的双向链路）,每一开关板上有两级开关芯片，所以此多级互连网络(MIN)总共有4个开关板。HPS是一个使用此开关的由40MHz时钟驱动的带缓冲的多级Ω互连网络。它使用了虫蚀选路法，一个8位的flits在无竞争时穿过一级（即一个开关芯片）只需5个时钟（即125ns)。因此HPS无竞争时的硬件延迟是很小的，对于512个节点仅875ns。但实际延迟比此值高得多，一个进程发送一个空包给另一个进程至少花40μs,这种消息传递延迟大部分是由软件开销造成的。HPS能提供成对节点之间的双向传输带宽为40MB/s。

②节点结构：SP2有三种不同的节点，分别是宽节点（WideNode）、窄节点（ThinNode)和窄节点1,它们主要差别在于存储器的容量、数据路径宽度和I/O总线的槽数的不同，但是所有的这些节点都使用时钟为66.7MHz的POWER(Performance OptimizedWith Enhanced RISC)-2微处理器。每个处理器有一个32KB的指令高速缓存、256KB的数据高速缓存、指令和转移控制单元、两个定点运算单元、两个各能执行乘-加操作的浮点运算单元。由于定点和浮点运算可同时进行，所以 POWER-2具有4×66.7 Mflops=267 Mflops的峰值速度。POWER-2是个超标量处理器，它使用短指令流水线、先进的转移预测技术和寄存器重命名技术，使得它在每个时钟周期内能执行6条指令：两条取/存指令、两条浮点乘-加指令、一条变址增一指令和一条条件转移指令。

![](images/44c18f7f8b91604ae47f2bf999fef37ed4911abaadffadd3ebdec2a4d03af0d8.jpg)  
图2.10 SP2中的128 路高性能开关(HPS)

I/O子系统和网络接口SP的I/O子系统如图2.11所示，它基本上是围绕着HPS构筑起来的,并用LAN的信关与 SP系统以外的机器相连。SP的节点有4类：主机节点 $( \mathrm { H } )$ 用于用户登录和交互处理;I/O节点主要执行I/O功能(如全局文件服务);信关节点(G)用于连网;计算节点(C)专负责计算。

![](images/4efd3332b17686467549f1d6ead594e0190549ee9d36b670b0a0c7e11d05a95c.jpg)  
图2.11 SPI/O子系统

每个 SP 节点通过网络接口电路(NIC)与HPS 相连,NIC也叫作开关适配器或通信适配器。如图2.12所示,适配器包含-个8MB的DRAM和受控于-个40MHz的i860 微处理器。适配器经微通道接口搭在微通道（Micro（han-nel)上,它是一个标准的I/O总线并用于将外设连向RS/6000工作站和IBMPC机，同时适配器也经过存储和开关管理单元（MSMU:Memoryand SwitchManage-ment Unit)连向 HPS(经由各为8位宽的 IN-FIFO和OUT-FIFO)。除此之外,它还包含·些控制/状态寄存器和用作 i860总线控制器,检查和刷新DRAM。另外，个4 KB 的双向FIFO(BIDI)缓冲器用于连接微通道和 i860总线。

![](images/a002d52cc56687b65d3eb427759733536042be43bd0a39e44071578d3a7ce5ce.jpg)  
图2.12SP通信适配器

参照图2.12来解释一下数据从节点发往HPS的过程：当节点处理器告诉适配器要发送数据时,i860 将直接存储访问DMA(DirectMemory Access)传输所必需的信息(称为Header)写人BIDI,当此Header抵达BIDI之首部时,左部DMA(L-DMA)负责将数据从节点(微通道)传人BIDI;完成时，L-DMA将硬件计数器增--,i860 写另一个Header至右部 DMA(R-DMA),R-DMA 负责将数据从BIDI传至MSMU中的OUT-FIFO,然后再将数据传送至 $\mathrm { H P S } _ { \circ }$

从HPS接收数据是类似的：当数据到达时，MSMU通知i860,它就写一个Header以启动R-DMA,R-DMA 就负责将数据从IN-FIFO传至BIDI;完成时，i860向BIDI写人一个Header,当它抵达 BIDI之首部时,L-DMA抽取此Head-er,并负责将数据从BIDI传至微通道。

系统软件SP系统软件层次如图2.13所示，其核心部分是IBMAIX操作系统。SP沿用了绝大部分RS/6000工作站环境，包括数据库管理系统（如DB2),在线事务处理监视器(如（ICS/6000),系统管理和作业管理,标准操作系统 AIX,Fortran、 $\therefore \ l ( \cdot + \cdot +$ 编译器,数学和工程库(如ESSL)以及上万个串行应用程序等。SP系统只加入了若干新软件和改进了某些现存的软件，它们都是可扩放并行机群系统所要求的。

图2.13SP系统软件层次  

<table><tr><td rowspan=1 colspan=4>应  用</td></tr><tr><td rowspan=1 colspan=4>应用子系统（数据库、事务处理监视器等）</td></tr><tr><td rowspan=1 colspan=1>系统管理</td><td rowspan=1 colspan=1>作业管理</td><td rowspan=1 colspan=1>并行环境</td><td rowspan=1 colspan=1>编译器等</td></tr><tr><td rowspan=1 colspan=4>全局服务（提供单一系统映像）</td></tr><tr><td rowspan=1 colspan=4>有效性服务</td></tr><tr><td rowspan=1 colspan=2>高性能服务</td><td rowspan=1 colspan=2>标准操作系统（AIX）</td></tr><tr><td rowspan=1 colspan=4>标准RS/6000硬件（处理器、存储器、I/O设备、适配器）</td></tr></table>

$\textcircled{1}$ 并行环境:AIX并行环境PE(Parallel Environment)为用户提供了开发和执行并行程序的平台，如图2.14所示，它包含4部分：

并行操作环境 POE（Parallel Operating Environment），消息传递库 MPL（Message Passing Library),可视化工具VT(Visualization Tool)和并行查错 Pdbx(ParallelDebugger)。其中POE用于控制并行程序的执行，它是由一个运行在家用节点(是一个连向 SP节点的RS/6000 工作站)上的划分管理程序(PartitionManager)来控制。家用节点是用户调用并行程序的地方，并行程序作为SP计算节点上--个或多个任务来运行。家用节点提供标准的UnixI/O设备（如Stdin、Stdout和 Stderr),它通过LAN(如以太网)与计算节点进行标准的I/O通信。例如用户从家用节点的键盘上按 $\mathsf { c u r l } + \mathsf { C }$ 键可终止所有的任务，用Printf语句就可在家用节点的屏幕上显示输出。

![](images/04754da7107ddbadc8f7630ad8e2fba56c53f559a1f5cf6637bac78d409203c7.jpg)  
图2.14 SP机群的并行环境(PE)

消息传递通信是经由HPS或以太网执行专门MPL功能实现的,这个库提供诸如进程管理、点到点通信、整体通信等33种功能,IBM SP还支持MPI的不同版本。

②高性能服务：IBMSP除了能直接使用标准的、商用的原来为RS/6000工作站和基于TCP/IP网络的分布系统所开发的软件外，它还提供了一些高性能服务，包括高性能通信子系统、高性能文件系统、并行库、并行数据库和高性能1/0等。

SP支持两种通信协议：基于IP的协议(执行在核空间)和US协议(执行在用户空间),两者均可在HPS上或常规网（如以太网）上使用。但US协议具有较好的性能，可它每个节点中只允许有-个任务去使用US协议；当每个节点上有多个任务时，使用基于IP的协议可导致较好的整个系统的利用率。

③ 并行I/O文件系统:SP高性能文件系统称之为并行I/O文件系统PI-OFS(ParallelI/OFile System）,对绝大多数应用和系统实用程序它是与POSIX-致的，Unix 操作和命令(如 read、write、open、close、ls、cp 和mv 等）与顺序U-nix系统中的--样,除了允许传统的Unix文件系统接口外,PIOFS提供了并行接口以便能对文件进行并行分布和操作。

IBM开发了称之为DB2并行版本的并行数据库软件程序，它能运行在 SP和其它机群平台上。数据库分布在多个节点中，数据库功能则装人数据驻留的节点上。DB2并行版本在机器规模和问题规模两方面都是可扩放的，它能运行在数百个节点上并能处理多达万亿字节(Terabytes)的大型数据库。

$\textcircled{4}$ 有效性服务：SP系统由一组运行在节点上的守护程序(Daemon)提供软件有效性基础设施。心跳(Heartbeat)守护程序周期地也改变心跳信息以指示哪些节点是存在的。属籍(Membership)服务能识别节点和进程属于某一组。当属籍关系因节点失效、停机或再启动改变时，通告(Notification)服务用来通知活动的成员，并随后调用恢复(Recovery)服务协调恢复以使活动的成员继续工作。

$\textcircled{5}$ 全局服务：SP系统提供的全局服务有外部系统数据储存库 SDR(SystemDataRepository),它维持有关节点、开关和现行作业等全系统的信息。当部分系统失效时 SDR对重组系统是有用的,其内容能将系统带回失效前的状态。

采用通过HPS支持TCP/IP和UDP/IP可实现全局网络访问。通过网络文件系统(NFS)可提供单一文件系统。除了NFS外,SP还为全局磁盘访问提供虚拟共事磁盘VSD(Virtual Shared Disk)技术。VSD 是位于 AIX 逻辑盘组管理器LVM(LogicalVolume Manager)之顶的一个设备驱动层。当一个节点进程欲访问本地共享磁盘时，VSD直接传递请求至节点的LVM;当一个节点进程欲访问远程共享磁盘时,VSD传递请求至远程磁盘的VSD,然后再将其传至远程节点的LVM。

$\textcircled{6}$ 系统管理:SP系统控制台(C)是一台控制工作站(见图2.9)。SP系统管理器从此单控制点管理整个SP系统：包括系统安装、监视和配置、系统操作、用户管理、文件管理、作业记费、打印和邮件服务等。此外,SP中的每个节点、开关等都有一块能自动检测环境条件的监视卡以及时控制硬件部件。管理者能使用这些设施开/关电源和监视器,复位单节点和开关等部件。还有,SP支持用户交互和批处理两种作业模式，它们既可以是串行程序也可以是并行程序。

# 2.3工作站机群COW

工作站机群COW(Cluster ofWorkstations)是实现并行计算的一种新主流技术,是属于分布式存储的MIMD并行计算机结构，系由工作站和互连网络两部分组成。由于这种结构用于并行计算的主要资源是工作站,所以工作站机群的名称便由此产生。工作站机群COW这一名称,在早期的研究阶段，也曾被称为工作站网络 NOW(Network of Workstations);在近几年的商业和企业界的应用中，也把使用机群技术(Clustering)构筑的MPP(如前面第2.2.2节所讲的

SP2)有区别地称作机群。本节着重讨论早期带有研究性质的（OW，首先介绍其基本原理及其有关问题;然后介绍一下Berkeley 大学的NOW研究计划。

# 2.3.1 COW的基本原理与技术

什么是COW随着工作站性能迅速提高和价格日益下降以及高速网络产品陆续问世，--种新型的并行计算系统便应运而生。这种系统将一群工作站用某种结构的网络互连起来,充分利用各工作站的资源,统一调度、协调处理,以实现高效并行计算。图2.15示出了COW的硬件组成，它由工作站和互连网络两部分组成,工作站上增加一块主机接口板以实现连网。互连网络可以是普通的LAN(如以太网、令牌环和FDDI等),也可以是高速开关网络(如ATM、交换式高速以太网等)。工作站是个广义的称呼,它可以是高档微机,甚至也可以是个对称多处理机SMP。一个实用的COW还应有一个高效的软件环境,如图2.16所示,包括操作系统(可为通用的Unix、AIX,也可为改进和修改的操作系统）、通信协议(实现工作站到互连网络的数据通信服务）、可由用户调用的通信原语库以及并行程序设计环境与工具等。从用户、程序员和系统管理员的角度看，(OW 相当于单一并行系统,感觉不到多个工作站的实际存在;从程序设计模式的角度看,它与MPP一样可采用面向消息传递的 SPMD(Single Program Multi-ple Data)编程方式,即各个工作站均运行同一个程序,但分别加载不同的数据，从而可支持粗粒度的并行应用程序。

![](images/e38e7eaf09dab43bf1c5d5c53e14cb95b1ac44165891dd666079c3c24454303c.jpg)  
图2.15（OW的一般结构  
图2.16（OW的软件结构

<table><tr><td rowspan=1 colspan=1>并行应用程序</td><td rowspan=1 colspan=1>并行工其包</td></tr><tr><td rowspan=1 colspan=1>并行程序设计环境、通信原语库</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=2>通信协议</td></tr><tr><td rowspan=1 colspan=2>操作系统</td></tr><tr><td rowspan=1 colspan=2>处理机与高速通信部件</td></tr></table>

为什么发展COW和前面所介绍的对称多处理机 SMP和大规模并行机

MPP相比，COW在实用上具有一些明显的优点： $\textcircled{1}$ 投资风险小：用户在购置传统巨型机或MPP系统时，总是担心使用效率不高和性能发挥得不好，如果购置后在一定程度上确实出现此问题，就相当于搁置或浪费了大批资金，但COW不存在此问题，因为即使COW在技术上不够先进，但每台高性能的工作站仍可照旧使用，不会浪费资金； $\textcircled{2}$ 编程方便：用户无需学用新的并行程序设计语言（如并行C、并行 $\ b { \mathbb { C } } + \ b { \mathbb { + } }$ 、并行Fortran等），只要利用所提供的并行程序设计环境，在常规 ${ \mathbb C } \mathrm { , } { \mathbb C } + +$ 和Fortran等程序中相应的地方插人少量的几条原语，即可使这些程序在COW上运行，这一点是最受用户欢迎的； $\textcircled{3}$ 系统结构灵活：用户将不同性能的工作站使用不同的体系结构和各种互连网络构成同构或异构的工作站机群系统，从而可弥补单一体系结构适应面窄的弱点，可更充分地满足各类应用要求； $\textcircled{4}$ 性能/价格比高：一般一台巨型机或MPP都很昂贵(费用常以几百万元、几千万元计),而一台高性能工作站相对便宜(费用仅以几万元或十几万元计），一个COW系统从浮点运算能力来看，虽然每台工作站只有几Mflops到几十Mflops,但一群工作站的总体运算性能可高达Gflops的量级，能接近一些巨型机的性能，但价格却低了很多； $\textcircled{5}$ 能充分利用分散的计算资源：当个人工作站处于空闲状态时,COW可在空闲时间内给这些工作站加载并行计算任务，从而工作站资源可得到充分利用； $\textcircled{6}$ 可扩放性好：用户可根据需要增加工作站的数目，以高带宽和低延迟的网络技术支持获得高的加速比，从而获得应用问题的高可扩放性。

COW的关键技术实现工作站机群需要解决的主要问题是通信性能和并行编程环境。因为组成COW的硬件环境中工作站的性能已相当高，且还在不断的提高，相对而言工作站性能不是关键问题;相反，负责数据通信的互连网络却是一项关键技术，因为COW系统中并行计算时各工作站之间需要经过互连网络交换数据，某些工作站上的程序所需要的数据也往往要通过网络获取或提交。如果网络通信延迟时间很长，再加上用于通信的软件开销(此部分不可忽视)可能就限制了COW技术对某些问题的适应性。近几年来网络技术发展很快,ATM给予COW技术强大的支持,其156Mb/s的传输速率以及高带宽的特性保证了数据通信的高速进行；另外 IEEE/ANSIP1596互连标准 SCI(ScalableCoherenceInterface)可支持多达64K个节点互连,并能实现二级高速缓存一致性协议，传输速率可以达到1Gb/s,从而可很好地支持工作站的互连。

伴随高速网络而产生的另一关键技术是工作站到网络的主机接口网络接口的设计，它应尽量保持网络的传输速度与主机数据收发速度相匹配,其中增加高速缓存或采用DMA是可供选择的两种技术。网络接口使工作站可以利用网络传输数据，但也增加了通信延迟,它占用工作站CPU时间，从而影响了COW的性能。一般,一次通信时间延迟可如图2.17所示，其中D为操作系统调度时间,A用于分配缓冲，C用于拷贝数据到系统缓冲区,S为启动发送/接收时间，T为链路传输时间,F用于定位中断源，X用于从接收队列获取数据。一般减少延迟的方法有： $\textcircled{1}$ 设计精简通信协议以减少数据移动的次数和协议处理时间； $\textcircled{2}$ 采用主动消息(ActiveMessage)携带数据处理命令以重叠计算和通信； $\textcircled{3}$ 定制通信处理单元以消除通信对工作站CPU的依赖。

另外，COW要走向实用必须为用户提供一个良好使用环境和一套完善的工具系统，主要包括： $\textcircled{1}$ 并行编程环境，如一些通信原语库、多种编程语言( $\mathrm { L } \mathbf { x } - \mathrm { \partial }$ press、PVM、Linda、 $\boldsymbol { \mathrm { P _ { + } } }$ 、MPI)的支持以及并行编译器等； $\textcircled{2}$ 可视化监视/调试器（如 Express 的 domtool、基于PVM的 XPVM等）; $\textcircled{3}$ 并行图形库（如基于Express的Plotix等）; $\textcircled{4}$ 并行文件系统和数据库，以适应开展分布式事务处理的研究与开发。

![](images/3665163e00e50fcde518804dead9745a79103989a7effaa682a32833e0ac5865.jpg)  
图2.17-次通信的时间延迟

COW研究的新进展随着（OW研究的深人开展，很多大学和实验室都建立了各具特色的实验型（OW系统。表2.9列出了几例具有代表性的机群研究计划,它在一定程度上反映了COW技术的新进展。其中,NOW系统涉及到了机群计算的很多问题,包括结构、支持Web服务器的软件、单一系统映像、I/O和文件系统、有效通信和强化的可用性(我们在下一节专门讨论它);Princeton的 SHRIMP计划，集中研究在基于PC机的机群上，支持有效通信和共享存储，开发了专门的网络接口板，可以达页面迁移级共享虚拟存储器；Wisconsin的WindTunnel计划,正在调研如何用商用节点和网络构成的松散耦合机群上实现高速缓存-致性共享存储器;Rice的TreadMarks是一个软件实现共享存储的工作站机群的优秀例子,它用用广空间运行时的库来实现存储器共享;由Chica-go、Maryland 和 Pennsylvania 共同发起的 NSCP(National Scalable （luster Pro-jcct)计划,旨在研究异构机群上的元计算(Metacompuling),NSCP样机系统是由上述三所大学的局部网通过Intcrnet互连起来而构成;Argonne 的Globus计划也是研究元计算的，它将北美17个站点上的超级计算机、海量存储器和可视化设备用ATM网连起来;Syracuse 的 WWVM(Word-Wide Virtual Machine）计划,目的在 于使用 Internet 和 HPCC(High Performance Computing and Communi-cation)技术实现高性能计算；Virginia的Legion 计划,意在美国本土的国家虚拟计算机设施上开发元计算软件；香港大学的PearlCluster计划是一个用ATM连接的基于Unix 服务器和工作站(如 SUN、HP、Alpha、SGI)的机群系统(参见图1.19),其优异特性包括:支持 SSI的中间件(Middleware）、两种语言Internet搜索工具和Java接口的MPI通信子系统等,它们都用于财务数字库和分布式多媒体的应用。

表2.9典型的机群系统特点一览表  

<table><tr><td rowspan=1 colspan=1>名称</td><td rowspan=1 colspan=1>系统特点</td></tr><tr><td rowspan=1 colspan=1>Berkeley :NOW</td><td rowspan=1 colspan=1>非服务器工作站网络主动消息，协同文件系统，全局Unix扩展</td></tr><tr><td rowspan=1 colspan=1>Princeton :SHRIMP</td><td rowspan=1 colspan=1>PC商用组件，通过专用网络接口达到共享虚拟存储，支持有效通信</td></tr><tr><td rowspan=1 colspan=1>Karsruhe:Parastation</td><td rowspan=1 colspan=1>用于分布并行处理的有效通信网络和软件开发</td></tr><tr><td rowspan=1 colspan=1>Rice:Tread Marks</td><td rowspan=1 colspan=1>软件实现的分布共享存储的工作站机群</td></tr><tr><td rowspan=1 colspan=1>Wisconsin :Wind Tunnel</td><td rowspan=1 colspan=1>在经由商用网络互连的工作站机群上实现分布式共享存储</td></tr><tr><td rowspan=1 colspan=1>Chica、Maryl、Penns:NSCP</td><td rowspan=1 colspan=1>国家可扩放机群计划：在通过因特网互连的3个本地机群系统上进行元计算</td></tr><tr><td rowspan=1 colspan=1>Argonne:Globus</td><td rowspan=1 colspan=1>在由ATM连接的北美17个站点的WAN上开发元计算平台和软件</td></tr><tr><td rowspan=1 colspan=1> Syracuse:WWVM</td><td rowspan=1 colspan=1>使用因特网和HPCC技术，在世界范围的虚拟机上进行高性能计算</td></tr><tr><td rowspan=1 colspan=1>HKU:Pearl Cluster</td><td rowspan=1 colspan=1>研究机群在分布式多媒体和金融数字库方面的应用</td></tr><tr><td rowspan=1 colspan=1>Virginia:Legion</td><td rowspan=1 colspan=1>在国内虚拟计算机设施上开发元计算软件</td></tr></table>

# $\yen 2.3.2$ Berkeley的 NOW计划

NOW(Network of Workstation)是美国加州大学Berkeley分校所开发,是一个颇有影响的计划,采用了很多先进技术,涉及到工作站机群很多共同问题，而且具有很多优异的特性： $\textcircled{1}$ 采用商用千兆网络和主动消息通信协议支持有效的通信； $\textcircled{2}$ 通过用户级整个机群软件GLUnix提供单一系统映像、资源管理和可用性； $\textcircled{3}$ 开发了一种新的无服务器网络文件系统xFS以支持可扩放性和单一文件层次的高可用性; $\textcircled{4}$ 最近NOW的开发者们正在开发一个软件框架Webos以构筑高可用性、渐增可扩放的地理 $\mathbf { W } \mathbf { e b }$ 服务器。

主动消息主动消息(Active Message)是实现低开销通信的一种异步通信机制。其基本想法是在消息头部控制信息中携带一个用户级子例程(称作消息处理程序)的地址。当信息头到达目的节点时，调用消息处理程序从网络上抽取剩下的数据，并把它集成到正在进行的计算中。主动消息相当高效和灵活，以至于各种系统中都逐渐地以它为基本的通信机制。但在主动消息下，程序应是以SPMD方式设计的,因为允许发送者指定消息处理程序在接收方的地址，所以必须让所有的节点上有一致的代码映像。

在普通主动消息中提供了如图2.18所示的一组基本函数(原语)和实用函数。当发送请求消息W时，调用如下请求函数：

am- request-2(Destination,request- handler, $x , y )$ ；

其中请求消息W由 request-handler、两个整数 $_ { x }$ 和 $_ { y }$ 、隐含的请求进程的虚拟节点号组成。请求原语am-request- $\mathbf { M } ( \cdots )$ 有5个版本( $\pmb { M } = \pmb { 0 } \sim 4 )$ ，每个均有 $M$ 个整数变量。该请求发送W至Destination(目的)进程。am-request是阻塞式的,即直到W被发出才返回。当W到达时,Destination进程调用request_han-dler子例程进行处理。

# 基本函数：

int am-request_M(vnn-t dest,request_ handler,int arg0,.,int arg(M-1))   
int am-reply_M(vnn-t dest,reply-handler,int argO,.,int arg(M-1))   
int am-get(vnn-t source,void " Iva,void\* rva,int nbytes, handler-t request_handler,void\* handler-arg)   
int am-store(vnn-t dest,void\*rva,void"lva,int nbytes, handler-t reply-handler,void\* handler-arg)   
void am-poll( void)

实用函数：

int am- enable(.…) //initializes the active message layer// int am-disable(void)//exits the active message layer// int am- procs(void) //returns the total number of processes of program// int am-my- proc(void) //returns the caling process's virtual node number// int am-max- size(void)//returns the max.No.of bytes for a get/store//

类似地,当发送应答消息W时，调用如下的应答函数：

am-reply-2(Destination,reply-handler, $x , y )$ ；

其中应答消息W由 reply_handler、两个整数 $_ { \pmb { x } }$ 和 $\pmb { y }$ 、隐含的应答进程的虚拟节点号组成。应答原语am-reply-M(…)有5个版本(M=0～4),每个均有M个整数变量。该应答发送W至目的进程。am-reply是阻塞式的,即直到W被发出才返回。当W到达时，目的进程调用reply-handler子例程进行处理。

am-store和am-get两个函数是用来在两个进程间传送大块数据。其中，am-store函数定义如下：

am- store(Dest,lva, rva, $\mathbf { N }$ ,request_handler,handler-arg);它将请求进程中从地址lva开始的连续 $N$ 个字节传至目的进程中从地址rva开始的存储区中。当收完所有 $N$ 个字节后,目的进程(Dest)调用request-handler,并传给它下述参数:请求进程的 VNN(Virtual Node Number）、rva、N和 handler-arg。类似地,am-get函数定义如下：

am- get(source,rva,lva, $\mathbf { N }$ ,reply_handler,handler-arg);

它将应答进程中从地址rva开始连续的 $N$ 个字节取至源进程中从地址lva开始的存储区中。当收完所有 $N$ 个字节后,调用者调用reply-handler并传给它下述参数：源进程的VNN、lva、N和handler-arg。

主动消息是个一般通用的通信机制,与具体硬件和软件平台无关，它已经在MPP、COW甚至PVM上予以实现,并取得了低延迟、高带宽优良性能,之所以如此是因为： $\textcircled{1}$ 用户级底层功能：主动消息通信常可完全在用户空间实现,可消除上下文切换等所造成的开销,没有必要施行系统调用，用户可直接访问网络接口硬件,消息处理程序也就是普通的用户级子例程; $\textcircled{2}$ 简捷：普通主动消息只有5条原语,每个只具有非常简单的功能和协议,且没有像TCP协议中的缓冲管理或误差检测等额外开销； $\textcircled{3}$ 计算和通信重叠：一般的消息传递型软件(如 PVM和MPI)可通过非阻塞发送/接收操作支持计算和通信的重叠,但在发送和接收双方均要有消息缓冲。主动消息处理长、短消息是不同的,对于4个或更少字的短数据块,可使用阻塞式am-request进行发送,而对大块数据传输，则可使用am-store或am-get。在普通主动消息中,提供了非阻塞的am-store以方便通信与计算的重叠。

GLUnix机群需要能支持可用性和单一系统映像的新的操作系统功能，但传统的工作站OS均无此功能,为此需要对其进行扩充,其方法有二：微(内)核法与用户级守护程序和库方法。微核法(例如Mach和WindowsNT)就是将提供所有服务的整体核代之以一些模块，并且绝大多数最基本的服务只是由少量的称之为微核(Microkernel)的小模块提供,其它的服务均在用户模式下提供。这种模块化法便于移植且灵活,但也有一些缺点：①原始的OS模块须重写；②在不同的结构上进行移植仍需付出努力;③微核系统比整体系统开销大(涉及到上下文切换、进程间通信和交叉保护边界等)。用户级守护程序和库方法能够作为用户级服务和库被实现,此法的优点是不要求修改核且易于实现,但同样它也有着和微核一样的额外开销。

NOW使用了GLUnix方法,它代表全局层(GLobalLayer)Unix,是指运行在工作站标准Unix之上的一个软件层,属于自包含软件。其主要的想法是机群操作系统应由低层和高层两层组成：其中低层是执行在核模式下的节点商用操作系统；高层是能提供机群所需的一些新功能的用户级操作系统。特别是，新全局层能提供机群内节点的单一系统映像，使得所有的处理器、存储器、网络容量和磁盘带宽均能被分配给串行和并行应用，并且它能够作为被保护的、用户级操作系统库予以实现。GLUnix方法能使很多机群性质在用户级实现，其优点是： $\textcircled{1}$ 易于实现：GLUnix完全在用户级实现,不须修改核(第一个GLUnix原型只用3个月就完成了）； $\textcircled{2}$ 可移植性：因为它只依赖基本系统中很小一组标准性质,所以GLUnix能移植在任何支持进程间通信、进程信令(Signaling)和访问负载信息的操作系统上； $\textcircled{3}$ 有效性：在应用地址空间内，使用过程调用的办法能够调用机群所需的一些新性质,无须跨硬件的保护边界、无须核自陷和上下文切换,在GLUnix中删除了系统调用开销；可以使用共享存储段或进程间通信原语,协调多个节点上的GLUnix的多个副本； $\textcircled{4}$ 鲁棒性：因为GLUnix是在用户级，所以能够使用常规的查错工具对它进行测试，错误可被检测、诊断和删除。总之,GLUnix原型对下述的绝大部分特性都已提供：并行程序的共调度；空间资源的检测、进程的迁移和负载平衡；快速用户级通信；远程调页和可用性支持。

xFS无服务器文件系统将文件服务的功能分布到机群的所有节点上,它和传统的中央文件服务器的对照见图2.19。传统的中央文件服务器执行的主要功能是： $\textcircled{1}$ 中央存储：数据文件和元数据都存储在连向文件服务器的一个或多个稳定磁盘上。一个文件的元数据系由一组文件属性(例如文件类型、文件大小、设备ID、节点号、属主D和文件访问许可等)所组成； $\textcircled{2}$ 中央缓存：为了改进性能，每个客户可以缓存某些局部文件块，而文件服务器缓存其主存中经常使用的文件块；③中央管理：服务器执行所有文件系统管理功能，包括元数据和高速缓存一致性管理。在xFS中,所有的服务器和客户的功能由分散的所有节点实现之。xFS仅有的限制是，作为管理器也必须是个客户,因为管理器使用了客户接口。

![](images/dfc58e3ae9565d4011bf334c12a88a710af9629b15170f38e5c9d99272b2443f.jpg)  
图2.19两类文件系统对照

(a）中央文件服务器系统；（b)xFS无服务器网络文件系统

$\textcircled{1}$ 廉价冗余磁盘阵列RAID(Redunant Array of Inexpensive Disks):无工作站文件系统能用来生成软件RAID以提供高性能和高可用性。现今,xFS使用单奇偶校验磁盘条(Striping)。一个文件数据块在多个存储服务器节点上按条划分,在另一节点上有奇偶校验块。如果一个节点失效,失效磁盘的内容,可利用其余盘和奇偶盘之异或操作重建之。RAID的缺点是所谓“小-写问题”(Small-Write Problem)：即如果一次写所修改的仅是条的一部分而不是整个条，则系统必须重新计算奇偶校验而导致大的开销。xFS使用登录条(Log-based striping)的方法解决此问题：每个客户首先将写接合到各用户的登录(Log)上(它就是记录所有写操作的一个存储缓存器);然后此登录采用登录段(Logsegment)提交给磁盘,每个段系由K-1登录片(LogFragment)组成,它与奇偶校验片一道送向K个存储服务器。但此法对大型多服务器机群也有问题：很多发往存储服务器的小片可能使登录存储器很大；很多客户同时写登录会造成竞争。xFS采用将存储服务器分成一些称之为条组(StripeGroup)的子集的办法来解决此问题。如图2.20所示,8个服务器分成2组，每组4个服务器。其中，A条组中，第一段由片1,2,3组成,相应的奇偶校验片为p;第二段由片4,5,6组成，相应的奇偶校验片q。B条组中情况类似。这样客户1和客户2可同时分别向各自组写人登录而不会冲突。

![](images/a93721b4912b0f3de4c77c6dd8792664971ec1f66cb5ef91f9742c4c1d61124e.jpg)  
图2.20 $\tt { x F S }$ 中的条组方法

②协同文件缓存(Cooperalive File（aching)：协同文件缓存的思想很简单：机群每个客户节点都辟出--部分作为文件(高速)缓存。协同文件缓存算法利用所有这些存储器生成一个大的、全机群上的文件缓存。当一个客户未找到其本地文件缓存时，不需要到磁盘中去找，只要到另个客户的存储器中去找该数据。如图2.21所示，文件稳定地存在服务器磁盘中，习惯上这些文件也缓存至客户存储器中、客户本地磁盘中和服务器的存储器中。xFS也允许一个文件缓存在远地存储器中。有两种协同文件缓存算法：贪心转发法(Greedy Forward-ing)和N-概率转发法(N-Chance Forwarding)。贪心转发法工作原理是：一个访问文件和客户首先试用其本地高速缓存,如果数据块不在那里，它便将请求转发给服务器。服务器先搜索其本地高速缓存，若命中，便将数据返给客户并维护其高速缓存目录;若未找到，服务器便查阅其高速缓存目录并把请求转发给保存所请求数据的客户，然后该客户便直接将数据返回给请求的客户。贪心转发法的优点是实现简单,但其缺点是同一数据块可能被很多高速缓存所复制。当一客户第一次读一个数据块时,此块从服务器磁盘中读出并将其缓存在服务器高速缓存和客户高速缓存中，而另一读同一块的客户将把它缓存在其本地文件高速缓存中。这种重复降低了协同高速缓存的有效空间，因而也增加了命不中的比率,而且使高速缓存一致性管理更加困难。N-概率转发法是贪心转发法的一般化,它采用缓存一个数据块仅于一个客户高速缓存中的办法避免重复。这样的数据块叫作单块(Singlet)。当一个客户从另一客户的高速缓存中取出一块时，此块就被丢掉，并发一条消息给服务器告诉它此块已被移去。单块所带来的问题是，如果一个单块被丢掉，它就给后来的数据块腾出了位置，此单块也就从整个协同高速缓存中丢失。N-概率转发法可缓解此问题，只要客户高速缓存未满，它和贪心转发法完全一样。当任一客户的本地高速缓存满时，就要丢掉一个数据块，此时客户首先要检查一下此块是否为单块：如不是，客户就丢掉它；如是,客户就将块循环计数器置为N，并发送该块给一个随机的客户。如果第二个客户稍后要丢掉这一块,它就将循环计数器减一，并发送该块给另一客户。此过程一直继续到循环计数器为零,这时就把该块丢掉。

![](images/d1ed05bfd0734bc463270d83ff5df253f667e7ec96d6bd6e4875767f4468df93.jpg)  
图2.21客户/服务器机群中缓存文件的不同方式

③分布式管理：xFS的文件系统管理功能是全分布的，它使用了位于多个节点上的多管理器(Manager)。为了理解如何达到分布管理,参照图2.22来看一下 xFS中一个文件的读过程：当一个客户试图读一个文件块时，它发送一个带有文件(路径)名和位移(Name& Offset)的请求,在xFS的目录(Dir)中使用文件名客户就能找到文件的索引(Index),用此索引客户搜索本地高速缓存（U-nix Cache),如果数据块在其中(命中),则数据就被读出;如果高速缓存未命中，那么客户用索引号查阅管理器映射表(ManagerMap)，此表指明哪个物理节点管理哪组索引号，也就是正确的管理者在哪里，于是索引和位移信息就经网络发正确的管理者，管理者留意诸如数据块是否在磁盘中或被缓存、块的精确位置、高速缓存块是否是一致的某信息。如果块被缓存在某一客户的本地高速缓存中且是一致的,那么管理者就转发读请求给那个客户,客户就从其本地高速缓存中读取数据并直接发给原先的客户；如果数据块不在协同高速缓存中，管理者就再查阅imap表以找到索引节点(inode),它包含了文件所有数据块的地址，此地址就可用来找到正确的存储服务器，于是数据块就可从那里读出并传给原先请求的客户。

![](images/d8a6b5d6bbe2fa8bc4afd7d42feb2bd78e47447cb2ce92fe9f717412e7f4aa0c.jpg)  
图2.22xFS中一个简化文件的访问过程

一个xFS的原型已在32个节点的机群上实现，它展示了良好的可扩放性，其读带宽已达13.8 MB/s,而写带宽已达13.9 MB/s。

# 2.4国产曙光系列并行机系统

我国的高性能计算机的发展起步并不晚：早在20世纪60年代后期到70年代,我国就自行研制了大型计算机（MainframeComputer),其典型代表机器有150、905、718和 DJS260 等,它们采用单/双 CPU,其峰值速度约为1MOPS（Million Operations Per Second），即俗称的百万次机器;20世纪70 年代后期到80 年代,我国研制了向量机和多处理机,其典型代表机器有757、银河1/2号等，它们采用 $1 \sim 4$ 个CPU,其峰值速度达 $1 0 ^ { \mathrm { - } } 1 0 0 \ \mathrm { M O P S }$ ,即俗称的亿次机器；20世纪80年代后期到现在，我国研制了对称多处理机（SMP）、大规模并行机(MPP)和工作站机群(COW),其典型代表机器有曙光1号、曙光-1000/1000A、

YH-3和曙光-2000等,它们采用 $4 \sim 1 2 8$ 个 CPU,其峰值速度达1Gflops～几十Gflops,即俗称的百亿次机器，我国1999年将正式推出千亿次高性能计算机。表2.10列出了我国20世纪90年代自行研制的有代表性的几种并行机,虽不全面,但足以“管中窥豹,可见一斑”。

表2.1020世纪90年代我国自行研制的几种并行机一览表  

<table><tr><td rowspan=1 colspan=1>机器型号</td><td rowspan=1 colspan=1>完成年代</td><td rowspan=1 colspan=1>研制单位</td><td rowspan=1 colspan=1>CPU芯片</td><td rowspan=1 colspan=1>CPU数</td><td rowspan=1 colspan=1>峰值速度(Gflops)</td></tr><tr><td rowspan=1 colspan=1>BJ-02</td><td rowspan=1 colspan=1>1991</td><td rowspan=1 colspan=1>中科院计算所</td><td rowspan=1 colspan=1>TransputerT800</td><td rowspan=1 colspan=1>17</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Dawning-1</td><td rowspan=1 colspan=1>1993</td><td rowspan=1 colspan=1>国家智能机中心</td><td rowspan=1 colspan=1>M88000</td><td rowspan=1 colspan=1>4~16</td><td rowspan=1 colspan=1>0.03~0.1</td></tr><tr><td rowspan=1 colspan=1>BJ-1</td><td rowspan=1 colspan=1>1994</td><td rowspan=1 colspan=1>中科院计算所</td><td rowspan=1 colspan=1>i860/xp</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Dawning-1000</td><td rowspan=1 colspan=1>1995</td><td rowspan=1 colspan=1>国家智能机中心</td><td rowspan=1 colspan=1>i860/xr</td><td rowspan=1 colspan=1>36</td><td rowspan=1 colspan=1>2.5</td></tr><tr><td rowspan=1 colspan=1>PAR95</td><td rowspan=1 colspan=1>1995</td><td rowspan=1 colspan=1>631研究所</td><td rowspan=1 colspan=1>i860/xr</td><td rowspan=1 colspan=1>40</td><td rowspan=1 colspan=1>3.2</td></tr><tr><td rowspan=1 colspan=1>990-STAR</td><td rowspan=1 colspan=1>1996</td><td rowspan=1 colspan=1>709研究所</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>16</td><td rowspan=1 colspan=1>1.3</td></tr><tr><td rowspan=1 colspan=1>Dawning-1000A</td><td rowspan=1 colspan=1>1997</td><td rowspan=1 colspan=1>国家智能机中心</td><td rowspan=1 colspan=1>PowerPC</td><td rowspan=1 colspan=1>8~16</td><td rowspan=1 colspan=1>3.2~6.4</td></tr><tr><td rowspan=1 colspan=1>YH-3</td><td rowspan=1 colspan=1>1997</td><td rowspan=1 colspan=1>国防科大</td><td rowspan=1 colspan=1>MIPSR4000</td><td rowspan=1 colspan=1>128</td><td rowspan=1 colspan=1>13</td></tr><tr><td rowspan=1 colspan=1>Dawning-2000-I</td><td rowspan=1 colspan=1>1998</td><td rowspan=1 colspan=1>国家智能机中心</td><td rowspan=1 colspan=1>Power604e</td><td rowspan=1 colspan=1>32</td><td rowspan=1 colspan=1>20.0</td></tr></table>

# 2.4.1全对称共事存储多处理机系统：曙光1号

曙光1号是一台全对称紧耦合共享存储的多处理机系统，支持中细粒度并行计算,实现多线程技术,采用RISC和标准总线连接方法，系统配置灵活。采用SNIX(Symmetric UNIX)操作系统并在其上提供大量的 Unix实用程序、编程环境、用户图形介面,以支持人工智能、科学计算和信息处理系统的开发和应用，从而具有市场竞争能力。

硬件系统曙光1号的基本系统是图2.23所示的系统板。在一块系统板内通过100 MB/s带宽的高速局部总线实现了4个CPU、8个CMMU(CacheMemory Management Unit)共享 $6 4 ~ \mathrm { M B }$ 的内存以及与I/O总线、VME 总线、BIT总线的通信。曙光1号系统板,通过符合VME总线标准的底板上的9个插槽,可以配置1～4块模块系统板、1～2块存储扩展板和其它的I/O功能板而构成更大的曙光1号系统(图2.24)。

![](images/bb0f3d2bdbbabdaa955daad9ef0f4e56331c61ddca0029f66be84b36f13cda32.jpg)  
图2.23曙光1号系统板

![](images/bb3c0d269ea1debde76731814b5039a26088d0602ef6009db56c5ad0927cd6d5.jpg)  
图2.24曙光1号系统

曙光1号硬件特性可汇总如下：

$\textcircled{1}$ 处理器：

·MC88100芯片， $4 \sim 1 6$ 个；主频 $2 5 ~ \mathrm { M H z }$ ；字长32位；指令系统共51条指令；4个CPU整数运算速度168VAXMIPS、浮点运算速度30 Mflops。

·MIC88200芯片， ${ \tt 8 } \sim 3 2$ 个;每个自带16 KB高速缓存,共 $1 2 8 \sim 5 1 2$ KB的高速缓存。

$\textcircled{2}$ 存储器： $6 4 ~ \mathrm { M B } { \sim } 7 6 8 ~ \mathrm { M B }$ 动态存储器，按字节奇偶校验，存储器分为4个体、4路交叉访问，页式管理。

$\textcircled{3}$ I/O功能：

·I/O总线：两个SCSI接口（单端的和差分的）；一个以太网接口（支持IEEE802.3协议）。  
·BIT总线： $4 \sim 1 6$ 异步通信接口；固化监控程序接口EPROM；日期时钟和系统保护接口NVRAM;中断控制接口等。  
·VME 总线:支持 VME Revision D C.1和 IEEE1014 以及 VEM RevisionD 协议;提供9插槽的VME机箱。

$\textcircled{4}$ 硬磁盘：5.25英寸的 $3 0 0 ~ \mathrm { M B } { \sim } 1 . 0 ~ \mathrm { G B } _ { \odot }$ $\textcircled{5}$ 磁带机：盒式磁带机320 Mb(600英尺）。$\textcircled{6}$ 任选件：终端服务器 $1 6 \sim 3 2$ 个。

软件系统曙光1号软件构成层次如图2.25所示，其设计目标为： $\textcircled{1}$ 采用国际标准，提供开放式计算环境； $\textcircled{2}$ 通过并行化操作系统核心及核心之上的各种实用程序，提高系统的响应及任务吞吐能力； $\textcircled{3}$ 通过增加各种并行机制，支持中细粒度的并行计算； $\textcircled{4}$ 在系统软件的各个层次上提供灵活的界面，支持不同用户的需求。图2.26以圆形方式对图2.25进行了说明，现从内到外对各层略作说明如下： $\textcircled{1}$ 监控器作为系统加电后首先运行的软件，其主要功能是硬件配置的设置、硬件测试及引导 Sysboot等，它被固化到512KBEPROM只读存储器中；Sysboot完成SNIX核心加载的主要工作，将根文件系统中的OS核心代码读人到DRAM的首地址，并控制所有处理器同时跳转到核心正文段起始地址执行，还对I/O设备做预处理操作等。 $\textcircled{2}$ 系统库函数包括标准Unix库函数与 SNIX扩展的库函数；前者包括C语言标准库函数Libc.a、数学运算库函数Libm.a、操作COFF文件格式库函数Libld.a和字符终端处理库函数Libcurses.a等；后者包括提供Pthreads并行线程函数以及实现虚处理器的低层库函数。 $\textcircled{3}$ SNIX核心是整个曙光1号软件运行的基础。核心之上的软件可视为多机硬件功能的扩展。从硬件角度看，SNIX核心又是一个多机资源管理与分配器；从核心构成看，它除保留单机Unix的基本成分外，还增加了处理器管理与处理器通信模块;从程序设计考虑,SNIX核心向用户程序提供一个真正的并行运行环境。在文件系统方面,SNIX核心对Unix System V进行了较多的功能扩展,同时支持系统V文件系统与BSD快速文件系统,并在两者之上实现了镜像文件系统与虚文件系统：镜像文件系统可将用户数据在多个磁盘上重复存放，以便当一个磁盘上的数据丢失时可从另一磁盘上恢复；虚文件系统删去了传统Unix 对用户数据文件大小的限制，以支持大规模的数据库处理系统。④SNIX保留了所有Unix实用程序：包括 Shell程序(sh、csh、ksh等）、编辑工具(vi、edit、view、cd 等）、网络实用程序(rlogin、telnet、ftp、mail 等）和一般工具(ls、rm、who、cp、cat等)；编译器(yacc、lex、cpp、cc、cflow、dis、lint 等）和调试程序(adb、sdb、ctrace、strip等);用户管理、文件管理、性能管理、打印机管理等。SNIX并行化的实用程序包括 make、fgrep、apply、find、fsck 等。③SNIX提供了较丰富的高级语言编译系统；曙光1号并行程序设计语言使用C+并行库函数(Pthreads）、并行For-tran 与并行 Ada,其中并行 Fortran 还提供了一个串行的 Fortran 程序并行识别器；曙光1号还提供了专门的并行程序Debugger。 $\textcircled{6}$ 曙光1号通过标准的以太网(TCP/IP)与其它计算机相连;SNIX提供的网络实用程序包括rlogin、telnet、call、rcp、mail等;用户还可通过电话线采用uucp访问曙光1号;曙光1号还通过网络文件系统NFS与不同的异种机相连，实现共享网络节点机的软硬件资源；使用 Socket还可进行分布式程序设计。 $\textcircled{7}$ 曙光1号提供MIT开发的窗口系统X Window和图形用户界面Motif。 $\textcircled{8}$ 曙光1号提供 Oracle、Ingres 和Postgres 数据库管理系统。 $\textcircled{9}$ 曙光1号提供了分布式程序设计环境Express,它将支持由2个或4个曙光1号系统板通过以太网或VME 总线构成的分布式系统,向用户提供一个同时使用8个或16个 MC88100 处理器进行计算的虚拟计算机;Ex-press 支持 SIMD与MIMD并行程序设计模型。 $\textcircled{10}$ 曙光1号支持的智能应用程序开发环境包括基于规则的推理机、面向对象推理机、框架管理系统、知识库管理系统和意见综合系统等;还提供“知识级的问题求解建模环境KMEPS”、“对象函数型人工智能语言系统”“面向对象的地图数据库系统MDB"和点方法几何定理证明软件系统等。

<table><tr><td rowspan=1 colspan=3>智能应用开发环境</td></tr><tr><td rowspan=1 colspan=3>分布式程序设计环境</td></tr><tr><td rowspan=1 colspan=3>数据库管理系统</td></tr><tr><td rowspan=1 colspan=3>XWindow/Motif图形用户界面</td></tr><tr><td rowspan=1 colspan=3>网络通信软件</td></tr><tr><td rowspan=1 colspan=3>程序设计语言开发环境</td></tr><tr><td rowspan=1 colspan=3>操作系统实用程序</td></tr><tr><td rowspan=1 colspan=3>操作系统SNIX核心界面库函数</td></tr><tr><td rowspan=1 colspan=1>监控器</td><td rowspan=1 colspan=1>OS引导程序Sysboot</td><td rowspan=1 colspan=1>SNIX核心</td></tr><tr><td rowspan=1 colspan=3>曙光1号硬件系统</td></tr></table>

![](images/a26853c5c11cdb5cb7b5cf3d998df25914b59782907e6ea504150c862cff5e29.jpg)  
图2.26曙光1号软件层次的圆形表示

# 2.4.2大规模并行处理系统：曙光-1000

曙光-1000 是一台分布存储的大规模并行处理·MPP(Massively Parallel Pro-cesing)系统,它突破了MPP中一些技术关键,采用20世纪90年代大量先进技术,其峰值速度达25亿次,可广泛应用于科学工程计算、气象预报、石油勘探、地震数据处理和银行等商务处理中。其技术特点是： $\textcircled{1}$ 良好的可扩放性,包括硬件和软件两个方面； $\textcircled{2}$ 大量的节点、强大的计算能力和大容量存储器; $\textcircled{3}$ 自行设计的稳定可靠的虫蚀通信芯片； $\textcircled{4}$ 使用带流控的消息传递协议； $\textcircled{5}$ 优良的优化并行编译器； $\textcircled{6}$ 先进的并行编程环境、并行查错工具、自动并行化工具和包括 PVM、MPI、Express、NX 等的编程工具。曙光-1000 整体性能达到 20 世纪90 年代初期世界先进水平,其主要技术指标是： $\textcircled{1}$ 使用 $6 \times 6$ 的二维网孔连接,共36个节点,其中计算节点32个，服务节点2个和I/O节点2个； $\textcircled{2}$ 峰值速度达单精度2.56 Gflops,双精度1.92 Gflops,实际速度为1.58 Gflops; $\textcircled{3}$ 存储容量为每个节点32MB,共1GB;④硬盘容量可超过5GB;③二维网孔连接、虫蚀选路，总通信容量为4.8GB/s;⑥计算节点和通信网络间带宽为2.8GB/s;?支持并行C、C++和Fortran,提供并行优化重构工具Port和自动并行化工具Autpar、动态监视和分析工具ParaVision以及单计算节点上源代码与目标代码的优化工具；③基于Unix的分布式并行操作系统;③提供并行程序查错环境NDB;①提供并行程序设计和运行环境 PVM、MPI、Express、NX 和 $\mathrm { P } _ { 4 }$ 等。

硬件系统曙光-1000是一台分布存储、消息传递的MPP系统,如图2.27所示，在6×6二维网孔的每个格点上有一个虫蚀路由芯片WRC（WormholeRouting Chip)和一个计算节点(或服务节点或I/O节点),系统监视器(Monitor)负责系统初始化和硬件故障诊断,用户工作平台可以是工作站 SUN Sparc-Ⅱ(或其它工作站)也可以是终端(它们都称为前端机),它们通过 $1 0 \ \mathrm { M b / s }$ 的以太网连向服务节点。

![](images/5a533eb3ea6eb2fcd23fca8a8899ebf6ad900db2fae9e9e890c2ab149f12698c.jpg)  
图2.27曙光-1000系统框图

$\textcircled{1}$ 二维网孔和WRC：二维网孔是一种可扩展的互连网络。格点上的计算节点(或服务节点或I/O节点)都连向WRC。节点编号(物理地址)由X方向编号和Y方向编号两部分组成,节点间相对地址包含在消息中。一个WRC有10条输人/输出通道,每个通道包含8条数据线。一条指明消息结束的尾信号线、一条发送请求线REQ和一条应答线ACK。当一条消息自源发往目的时,它只穿过途中的WRC,并不进入与WRC相连的节点处理器。消息选路采用X-Y选路算法(见8.1.1节算法8.1)。

$\textcircled{2}$ 计算节点：它是一块插人板,其核心是一个 $\mathbf { i } 8 6 0 \mathbf { x } \mathbf { r }$ 芯片,其主频为 40$\mathbf { M H z }$ ,字长64位,单精度浮点运算速度为80 Mflops、双精度为60Mflops,标量计算速度为40 MIPS;它有带奇偶校验的32MBDRAM、8KB EPROM和2 KBNVRAM;节点与网孔的接口模块包含16KBFIFO,网孔与各节点间的通信带宽为 $3 3 \mathrm { \ M B / s }$ ,消息具有CRC校验,RS-232接口直接连向监视器上的多用户卡,以便监视器能监视与诊断所有的节点处理器。在所有的计算节点上运行OS与用户程序。

③服务节点：服务节点用于管理系统资源,它是一台50MHz的具有EISA总线的486PC机。EISA总线与网孔网络之间有一接口模块 EMI,在EMI卡上有DMA机制;在数据通路FIFO-网孔-FIFO上使用CRC校验;EMI卡和网孔之间的通信速度是16MB/s。如有较多的用户和图形显示设备，则可使用2个服务节点，两者可使用共享系统资源表的方法协同工作。

$\textcircled{4}$ I/O节点：和服务节点一样,I/O节点也是一台带有EISA总线、具有EMI插卡的486PC机。一个I/O节点使用插在EISA总线上的 SCSI卡可接人4GB硬盘。系统可提供一个或两个I/O节点，当用户要求大的I/O吞吐率时可使用更多的I/O节点，但计算节点则须相应减少。I/O节点和网孔之间的数据传输速度为16MB/s。每个I/O节点上运行并行文件系统,执行并行文件操作。

$\textcircled{5}$ 系统控制台：也就是监视器，它运行SCOUNIX,其中有一块多用户卡，连向32个RS-232串行口。控制台与计算节点可执行点到点通信，也可向所有计算节点同时播送消息。其主要功能是初始化系统、监视计算节点上操作系统和用户程序的运行、动态地查看节点处理器资源组态表和诊断失效的计算节点。

$\textcircled{6}$ 前端机：曙光-1000 用户工作平台是 SUN Sparc-Ⅱ或 SGI图形工作站或终端,所有这些设备均经由LAN(如以太网)连向系统服务节点。LAN遵从TCP/IP协议,其速率为10 Mb/s。事实上,网孔系统可视为前端系统的计算服务器，在前端机上用户程序被编辑、编译(使用C和Fortran77i860交叉编译器）、链接和查错，当编译成功后，应用程序的目标代码通过以太网传到服务节点；然后由服务节点发往计算节点;最终的计算结果由前端机显示输出。

系统软件曙光-1000系统软件包括操作系统、并行优化编译及工具和并行编程环境及并行查错工具等。

$\textcircled{1}$ 操作系统：曙光-1000的操作系统是基于Unix的分布式操作系统。在计算节点上运行微核操作系统,支持虚拟存储管理、自陷处理、作业管理和消息传递；在服务节点上运行基于Mach2.6操作系统，支持多线程，其主要功能是系统管理，特别是节点处理器的分配与去分配;在I/O节点上运行并行文件服务器PFS。服务节点和I/O节点与计算节点具有相同的消息传递接口。系统执行带有流控的消息传递协议。

$\textcircled{2}$ 并行优化编译和工具：节点程序编译优化包括源码级优化和目标码级优化,前者使用循环(Loop)交换、循环合并和循环分离的办法开拓并行性；后者采用充分利用流水线、双指令模式和双操作指令(由i860 所提供的)和浮点加载指令以向量化循环的方式开拓并行性。Autopar是自行开发的自动并行化工具,它能识别并行循环、执行数据划分和产生并行的Fortran 源代码。Paravision 是曙光-1000 并行程序的可视化工具,它能够移植到其它MPP系统上，用户使用它能观察程序动态运行过程,包括消息传递条件、负载平衡情况和是否出现死锁等。

$\textcircled{3}$ 并行编程环境和并行查错工具：为了便利用户编程和运行并行程序，曙光-1000 移植了4种成熟的界面环境,即 NX、Express、PVM和 MPI。其中 NX原是Paragon 系统上的用户并行编程界面,而 Express、PVM和 MPI均是世界上广泛使用的并行编程和运行环境。并行程序查错器包括源代码查错程序 NDB和汇编代码查错程序ADB,它们的主要功能是显示、设置和取消指令断点、读/写存储器、逐步或连续运行程序或发送和接收现行进程状态。它们能够查错运行在多个节点上的程序。

表2.11列出了曙光-1000与某些著名MPP系统的性能比较，性能指标是利用求解标准线性方程组测得的，其中 $\mathbf { R } \left( \mathbf { m a x } \right)$ 是机器能够达到的最高速度，$\mathrm { N } ( \mathrm { m a x } )$ 是速度达到 $\mathbf { R } ( \mathbf { m a x } )$ 时线性方程组的阶， $\mathrm { N } \left( { \frac { 1 } { 2 } } \right)$ 是速度达到 $\frac { 1 } { 2 } \mathrm { R } ( \operatorname* { m a x } )$ 时线性方程组的阶。

表2.11 曙光-1000与某些著名MPP系统性能比较一览表  

<table><tr><td rowspan=1 colspan=1>机器名称</td><td rowspan=1 colspan=1>计算节点数目</td><td rowspan=1 colspan=1>R(max)Gflops</td><td rowspan=1 colspan=1>N(max)阶数</td><td rowspan=1 colspan=1>N(1/2)阶数</td></tr><tr><td rowspan=1 colspan=1>曙光-1000</td><td rowspan=1 colspan=1>32</td><td rowspan=1 colspan=1>1. 12</td><td rowspan=1 colspan=1>15 000</td><td rowspan=1 colspan=1>4 000</td></tr><tr><td rowspan=3 colspan=1>Paragon XPS(50MHz)</td><td rowspan=1 colspan=1>256</td><td rowspan=1 colspan=1>7.6</td><td rowspan=1 colspan=1>16 000</td><td rowspan=1 colspan=1>4 000</td></tr><tr><td rowspan=1 colspan=1>128</td><td rowspan=1 colspan=1>4.0</td><td rowspan=1 colspan=1>12 000</td><td rowspan=1 colspan=1>3000</td></tr><tr><td rowspan=1 colspan=1>64</td><td rowspan=1 colspan=1>2.0</td><td rowspan=1 colspan=1>8000</td><td rowspan=1 colspan=1>2 000</td></tr><tr><td rowspan=4 colspan=1>Delta（40MHz)</td><td rowspan=1 colspan=1>192</td><td rowspan=1 colspan=1>5.2</td><td rowspan=1 colspan=1>15 000</td><td rowspan=1 colspan=1>4 500</td></tr><tr><td rowspan=1 colspan=1>128</td><td rowspan=1 colspan=1>3.5</td><td rowspan=1 colspan=1>12 500</td><td rowspan=1 colspan=1>3 500</td></tr><tr><td rowspan=1 colspan=1>64</td><td rowspan=1 colspan=1>1.7.</td><td rowspan=1 colspan=1>8 000</td><td rowspan=1 colspan=1>2 500</td></tr><tr><td rowspan=1 colspan=1>32</td><td rowspan=1 colspan=1>0.9</td><td rowspan=1 colspan=1>6000</td><td rowspan=1 colspan=1>2 000</td></tr><tr><td rowspan=2 colspan=1>IBMSP2</td><td rowspan=1 colspan=1>32</td><td rowspan=1 colspan=1>6.1</td><td rowspan=1 colspan=1>19 000</td><td rowspan=1 colspan=1>4 088</td></tr><tr><td rowspan=1 colspan=1>16</td><td rowspan=1 colspan=1>3.0</td><td rowspan=1 colspan=1>13 500</td><td rowspan=1 colspan=1>1</td></tr><tr><td rowspan=2 colspan=1>CM-5</td><td rowspan=1 colspan=1>128</td><td rowspan=1 colspan=1>7.7</td><td rowspan=1 colspan=1>18 432</td><td rowspan=1 colspan=1>8 192</td></tr><tr><td rowspan=1 colspan=1>64</td><td rowspan=1 colspan=1>3.8</td><td rowspan=1 colspan=1>13 056</td><td rowspan=1 colspan=1>6016</td></tr><tr><td rowspan=1 colspan=1>Cray T3D32</td><td rowspan=1 colspan=1>32</td><td rowspan=1 colspan=1>3.2</td><td rowspan=1 colspan=1>14 592</td><td rowspan=1 colspan=1>1 616</td></tr><tr><td rowspan=1 colspan=1> SGI Challenge</td><td rowspan=1 colspan=1>36</td><td rowspan=1 colspan=1>1.28</td><td rowspan=1 colspan=1>8000</td><td rowspan=1 colspan=1>2 000</td></tr><tr><td rowspan=1 colspan=1>Ncube-2</td><td rowspan=1 colspan=1>256</td><td rowspan=1 colspan=1>0.482</td><td rowspan=1 colspan=1>10 784</td><td rowspan=1 colspan=1>1 504</td></tr><tr><td rowspan=1 colspan=1>Maspar MP-1 266</td><td rowspan=1 colspan=1>16 384</td><td rowspan=1 colspan=1>0.47</td><td rowspan=1 colspan=1>11 264</td><td rowspan=1 colspan=1>1280</td></tr></table>

# $\times 2 . 4 . 3$ 超级并行计算机系统：曙光-2000

曙光天潮系列"曙光-2000"是基于分布存储和消息传递体系结构的通用可扩放并行计算机系统，其节点数为 $4 \sim 1 2 8$ 个，节点CPU采用先进的PowerPC604e微处理器,通过高速以太网和虫蚀路由芯片组成的二维网孔互连。每个节点上运行完整的IBMAIX操作系统,系统与IBMRS/6000二进制兼容。可广泛应用于科技计算和商业计算的多种领域中。

设计准则为了将曙光-2000设计成一种通用、灵活的可扩放并行机系统，设计者们在广泛分析和深入理解当前硬件、软件技术发展趋势，不同应用领域的需求和用户环境要求的基础上,遵循了一系列设计准则： $\textcircled{1}$ 一个高性能的可扩放并行系统必须采用标准的微处理器、软件构件(Component)和操作系统，只应在标准技术无法满足可扩放并行系统某些特殊要求(如通信延迟)时，才采用定制的硬件和软件； $\textcircled{2}$ 采用最新的技术，保证性能价格比的领先优势。为此必须尽可能少地依赖于技术供应商,低层的体系结构必须足够灵活,在OS级上对各节点采用松散耦合方式； $\textcircled{3}$ 对低延迟和高带宽的要求使得在今后几年内可扩放并行计算机系统仍然依赖于定制的内部网络和通信子系统； $\textcircled{4}$ 系统的编程和执行环境应与标准的、开放的、分布式Unix环境一致； $\textcircled{5}$ 系统应当有选择地在下列领域提供高性能服务：通信系统、高性能文件系统、并行库、并行数据库、高速I/O,以利于高效地进行超级计算、并行查询和高性能事务处理; $\textcircled{6}$ 消除造成系统崩溃的单一故障点和从失效中快速恢复，可获得系统高可用性。为此必须有足够的硬件和软件备份(Replication),同时提供支持可用性的基础软件(故障检测、诊断、系统重配置和恢复等)； $\textcircled{7}$ 对于单一系统映像进行有选择地支持，只进行重要资源(如文件、目录服务)和命令的全局化以及提供对系统管理的单点控制。

体系结构曙光-2000体系结构如图2.28所示。曙光-2000系统可由${ \pmb 4 } \sim { \pmb 1 } 2 { \pmb 8 }$ 个处理节点组成。每个节点包括可靠的高效的RISC微处理器 Power-PC,运行完整的IBMAIX操作系统。诸节点由高速以太网和二维网孔互连；通信网卡通过PCI总线与节点相连,外围子系统通过I/O接口与节点相连；系统管理员通过控制台管理系统;用户工作站或终端通过外部以太网访问节点。曙光-2000系统的节点可分为计算节点和I/O与登录服务节点：前者用于执行用户提交的任务;后者用于支持用户作业在计算节点上的运行。

$\textcircled{1}$ 节点处理器：PowerPC微处理器采用超标量技术（即每个周期同时执行多条指令)和很多复杂结构技术来获得高性能。它拥有6个处理单元(浮点单元FPU、转移处理单元BPU、存/取单元LSU、2个单周期整数单元 SCIU和多周期整数单元MCIU),可同时执行4条指令， $3 0 0 ~ \mathrm { M F l z }$ 主频的处理器可达到每秒6亿次浮点运算。每个处理器的一级高速缓存容量为 $3 2 \mathrm { \ K B }$ 数据/32KB指令,二级高速缓存容量为1MB;内存容量为 ${ \bf 1 } 2 8 \mathrm { - } 5 { \bf 1 } 2 { \mathrm { \ m B } }$ ；内置硬盘容量为4.3GB;I/O总线速率为 $1 3 3 \mathrm { \ M B / s } _ { \circ }$

![](images/78ce665c88cbdba66cd7d4806b04a81f66c0ca2e064d36ad189e21c20043b17c.jpg)  
图2.28曙光-2000体系结构框图

$\textcircled{2}$ 通信子系统：曙光-2000采用二维网孔互连，使用“虫蚀"选路，从而具有可扩放性、低延迟、高带宽、低处理器开销和可靠灵活之特性。在二维网孔中，点与点之间采用基于消息包的固定路由、无缓冲的传输机制，点与点之间的通信带宽保持常数，不依赖于拓扑中两节点的物理位置。WRC芯片有10个通道，如图2.29所示，每个通道16位数据宽度， ${ 5 0 ~ \mathrm { M H z } }$ 频率，数据带宽 $1 0 0 ~ \mathrm { M B / s } _ { \circ }$ 芯片内部有X、Y两个路选择控制器和4级16位数据缓冲器。曙光-2000节点通过一块PCI网络接口板与底板相连,其中PMI-16接口板由PCI的DMA引擎控制数据传输,PMI-960接口板由一个Intel960协处理器负责DMA传输和协议控制。接口板和节点内存之间采用DMA方式传输，减少了消息传递中处理器的开销。

![](images/0f31e45be117c51b1af25ef5b81f211cfb147088d09d7519a79ec2f34f23b77b.jpg)  
图2.29WRC路由芯片结构示意图

软件系统曙光-2000软件逻辑结构如图2.30所示。其中，每个节点均由一个完整的AIX4.2以上操作系统管理,它提供了大量的多用户通信和系统管理技术、编译器等，符合主要的工业标准；在低层它提供了用于消息传递的基本通信库BCL、PVM和MPI;在高层提供集成并行程序设计环境IPPE、并行可视化工具ParaVT、并行调试器 DCDB、KISS(Keep It Simple and Scalable）、基于Web 的用户界面、自动并行化工具AutoPAR、可扩放文件系统COSMOS、批作业管理JOSS、资源管理RMS和曙光服务器聚集软件DSC;此外，曙光-2000系统还提供了一系列广泛的IBMRS/6000 兼容的开放软件工具来支持管理和操作，包括IBM的C和Fortran编译器、数学和工程库ESSL、数据库DB2等。

<table><tr><td rowspan=1 colspan=8>科学与工程计算应用</td><td rowspan=1 colspan=7>网络服务应用</td><td rowspan=1 colspan=5>数据库与事务处理应用</td><td rowspan=1 colspan=1>其它</td></tr><tr><td rowspan=1 colspan=20>应         用          层          软        件</td><td rowspan=2 colspan=1>中间件数据库</td></tr><tr><td rowspan=1 colspan=9>并行算法与数学库图形图像处理算法</td><td rowspan=1 colspan=4>新材料计算</td><td rowspan=1 colspan=4>气象气候计算</td><td rowspan=1 colspan=2>并行DB</td><td rowspan=1 colspan=1>其它</td></tr><tr><td rowspan=1 colspan=1>DSC</td><td rowspan=1 colspan=3>KISS</td><td rowspan=1 colspan=2>IPPE</td><td rowspan=1 colspan=3>AutoPAR</td><td rowspan=1 colspan=2>ParaVT</td><td rowspan=1 colspan=3>HPF</td><td rowspan=1 colspan=2>DCDB</td><td rowspan=1 colspan=4>分布共享存储软件包</td><td rowspan=1 colspan=1>ESSL</td></tr><tr><td rowspan=1 colspan=8>系统管理软件</td><td rowspan=1 colspan=4>上层通信库</td><td rowspan=2 colspan=9>编译器（C,Fortran,JAVA)基本函数库</td></tr><tr><td rowspan=1 colspan=2>资源管理</td><td rowspan=1 colspan=3>作业管理</td><td rowspan=1 colspan=3>机群管理</td><td rowspan=1 colspan=1>PVM</td><td rowspan=1 colspan=1>MPI</td><td rowspan=1 colspan=2>NX</td></tr><tr><td rowspan=1 colspan=21>HA核心和Agent</td></tr><tr><td rowspan=1 colspan=7>BCL通信库</td><td rowspan=1 colspan=14>COSMOS 库和 Daemon</td></tr><tr><td rowspan=1 colspan=21>PMI Driver   DNS,NFS,NIS                                                         文件系统核心扩展AIX操作系统</td></tr><tr><td rowspan=1 colspan=3>Monitor960</td><td></td><td rowspan=1 colspan=4>Monitor960BCL板上固件</td><td rowspan=2 colspan=14>硬                         件</td></tr><tr><td rowspan=1 colspan=7>PMI板</td></tr></table>

$\textcircled{1}$ 并行环境：它由BCL、IPPE、ParaVT和DCDB 组成,用户可用来开发、调试和修改并行Fortran 和C程序，并且可启动、监视和控制程序的运行。其中，BCL支持Fortran和C的显式消息传递模型,提供大量的函数集和子程序以支持进程间点到点通信和用户非阻塞通信，并支持多用户方式用户空间通信；IPPE 提供启动、监视、控制并行应用的用户环境，主要功能包括编译、链接并行代码和通信库,并行任务分区、并行作业加载和监视作业的运行,傻瓜界面KISS提供基于Web的查询和使用界面；ParaVT提供并行应用的性能监视和跟踪可视化,前者在程序运行时实时地显示系统的活动状态；后者用户可设置跟踪点以观察并行进程间的通信情况、识别死锁、负载变化和性能瓶颈等；DCDB是一个源代码级的调试器,支持图形化使用界面,是在Unix串行调试器dbx或gdb 基础上附加了一些专用的并行程序调试功能。

$\textcircled{2}$ 可扩放文件系统：COSMOS可有效解决超级计算应用对单个文件的可扩展高带宽的要求，并能提高网络文件系统吞吐量的可扩放性。它支持对条带化(Stripe)方式分布存储的文件的并行访问;它允许一个并行程序的多个进程对同一文件进行访问;可支持异步的I/O和规模大于2GB的文件;COSMOS支持标准Unix文件系统调用,用户通过UNIXioctl操作可获得其它的功能。由于每个计算节点上运行一个Client Daemon、每个COSMOS 服务节点土运行一个StorageDaemon(或有选择地运行ManagerDaemon),所以这些服务进程相互通信形成了一个可扩放服务器来满足用户请求。

$\textcircled{3}$ 可用性服务：曙光-2000所提供的可用性服务包括系统管理软件中的系统监控和NCIC-HA高可用软件包。目前曙光-2000 系统可用性服务的主要功能包括心跳服务、资源组服务、通知服务和恢复协调服务。其中心跳服务就是监视系统的状态是否正常,包括侦测和交换心跳信息;资源组服务就是定义节点和应用程序、系统资源(如IP)属于一个故障切换资源组,通常该组包括那些相关的应用服务成员；通知服务就是在组的结构和节点状态发生了变化时通知组内成员；恢复服务提供了当组内结构和节点状态发生变化时，当前组中备份节点恢复进程的启动机制,即故障切换(Takeover)。这些服务是由运行在节点上的HA守护进程(Daemon)所实现的。

$\textcircled{4}$ 全局服务：对于曙光-2000来说，一个全面的单一系统映像并不是迫切需要的,它只对特殊资源(包括磁盘、文件和通信网络等)提供单一系统映像。在曙光-2000中,通过网络文件系统NFS来提供对文件的全局访问,全局网络访问是通过网络路由机制和TCP/IP及UDP/IP对互连网络的支持来进行的。在此方式下,可使曙光-2000上的应用以单一的IP地址对外提供服务；曙光-2000 还打算使用虚拟共享磁盘VSD提供对磁盘的全局访问,使用VSD,运行在任何节点上的应用程序可以透明地访问任一其它节点上的磁盘，就像该磁盘是连接在自身节点上一样；另一个全局服务是系统数据储存库 SDR,它提供曙光-2000系统中各节点和控制工作上的数据存储和检索，这包括各个节点和互连网络的配置的全局信息以及系统中资源和作业的信息，这些重要的系统数据不仅要储存在实现这些系统功能的服务节点上,而且也应被保存在这些节点以外的全局储存库SDR上。当重要的系统服务发生故障时，故障节点可以通过查询SDR来重新恢复正常工作,在此期间,对服务的请求只是被延迟,但不会引起其它的故障

发生。

$\textcircled{5}$ 系统管理：曙光-2000的系统管理和监控软件是建立在大量的AIX工作站环境中已有的系统管理工具和命令的界面上的，它使得在多节点上可以运行传统的系统管理命令，这些命令的功能包括系统安装、重启/关机、系统操作、用户管理、安全管理、作业记帐、硬件监控、打印和邮件服务等;曙光-2000的单点控制在系统控制台上进行，它是一台独立的天演系列工作站,与系统中每一机柜相连,用户可从网络的任何一个地方登录到控制台；系统管理软件使用基于SN-MP 协议的客户/服务方式来从控制台启动系统管理命令，基于JAVA的图形化界面用于确定在哪一个节点上进行操作、修改和收集节点应答;硬件监控软件使得系统员可以监控曙光-2000系统的硬件状态。

$\textcircled{6}$ 作业管理：用户可以使用批处理或交互方式使用曙光-2000：在批处理方式中,作业是通过网络作业调度程序提交的;在交互方式中,用户使用Unixrlogin/telnet命令登录到曙光-2000系统上,通过相应的网络地址就可直接访问某个特定的节点。曙光-2000的资源管理器的主控服务运行在控制台上，它将相应的节点分配给并行作业，当并行作业被提交时，用户通过函数或命令向资源管理器申请作业所需的节点，如果有相应数量的可用节点,资源管理器就返回一个可用节点表,这些节点就构成了该并行作业的节点分区;当节点分区确定后，分区管理进程就在分区内的每个节点上加载一份作业的可执行代码,并通知该节点上的守护进程启动代码的执行;当作业完成后,分区管理进程负责清除和终止工作,并交回分区内的所有节点。

# 2.5小结和导读

小结本章讨论了当代三种并行计算机系统 SMP、MPP和COW,它们系统特性的比较可综合于表2.12中。注意,MPP 和COW之间的界线渐趋模糊，例如IBMSP2被视为MPP,但它具有机群结构(除了使用高性能开关网络作为通信网络外)。COW的性能/价格比优于MPP,所以机群技术是发展可扩放并行计算的主流趋势。

导读有关当代三种并行机系统的全面介绍,[103]是一本及时新作,有关Origin 2000的介绍,读者可参阅[117],[155]和[181];有关 SP2的介绍,读者可参阅[14],[169]和[163];有关COW的一般介绍,读者可参阅[200];Berkeley:NOW计划描述在[15]中;Princeton:SHRIMP 描述在[63]中;Karsruhe:Parasta-tion 描述在[180]中;Rice:TreadMarks 描述在[13]中;Wisconsin:Wind Tunnel描述在[144]中;NSCP 计划描述在[42]中;Argonne:Globus 描述在[57]中;Syra-cuse:WWVM描述在[60]中;Virginia:Legion描述在[83]中和香港大学:Pearl-cluster描述在[102]中。曙光-1号报导在[193]中;曙光-1000报导在[129]中和曙光-2000取材于[194]。

表2.12 SMP、MPP、COW性能比较一览表  

<table><tr><td rowspan=1 colspan=1>系统特性</td><td rowspan=1 colspan=1>SMP</td><td rowspan=1 colspan=2>MPP</td><td rowspan=1 colspan=1>COw</td></tr><tr><td rowspan=1 colspan=1>节点数目(N)</td><td rowspan=1 colspan=1>≤0(10)</td><td rowspan=1 colspan=2>0(100)~0(1000)</td><td rowspan=1 colspan=1>≤0(100)</td></tr><tr><td rowspan=1 colspan=1>节点复杂程度</td><td rowspan=1 colspan=1>中/粗粒度</td><td rowspan=1 colspan=2>细/中粒度</td><td rowspan=1 colspan=1>中粒度</td></tr><tr><td rowspan=1 colspan=1>节点间通信</td><td rowspan=1 colspan=1>共享存储</td><td rowspan=1 colspan=2>消息传递/共享存储</td><td rowspan=1 colspan=1>消息传递</td></tr><tr><td rowspan=1 colspan=1>作业调度</td><td rowspan=1 colspan=1>单一运行队列</td><td rowspan=1 colspan=2>主机上单一运行队列</td><td rowspan=1 colspan=1>多队列但协同</td></tr><tr><td rowspan=1 colspan=1>支持单一系统映像</td><td rowspan=1 colspan=1>总是</td><td rowspan=1 colspan=2>部分</td><td rowspan=1 colspan=1>希望</td></tr><tr><td rowspan=1 colspan=1>节点OS副本和类型</td><td rowspan=1 colspan=1>一个（单一）</td><td rowspan=1 colspan=2>N(微核）和1个主机OS（单一）</td><td rowspan=1 colspan=1>N(希望同构)</td></tr><tr><td rowspan=1 colspan=1>地址空间</td><td rowspan=1 colspan=1>单一</td><td rowspan=1 colspan=2>多个</td><td rowspan=1 colspan=1>多个</td></tr><tr><td rowspan=1 colspan=1>所有权</td><td rowspan=1 colspan=1>一个单位</td><td rowspan=1 colspan=2>一个单位</td><td rowspan=1 colspan=1>一个或多个单位</td></tr><tr><td rowspan=1 colspan=1>网络协议</td><td rowspan=1 colspan=1>非标准</td><td rowspan=1 colspan=2>非标准</td><td rowspan=1 colspan=1>标准/非标准</td></tr><tr><td rowspan=1 colspan=1>系统可用性</td><td rowspan=1 colspan=1>常常是低的</td><td rowspan=1 colspan=2>低中</td><td rowspan=1 colspan=1>高或容错</td></tr><tr><td rowspan=1 colspan=1>性能/价格比</td><td rowspan=1 colspan=1>一般</td><td rowspan=1 colspan=2>一般</td><td rowspan=1 colspan=1>高</td></tr><tr><td rowspan=1 colspan=1>处理器类型</td><td rowspan=1 colspan=1>商用</td><td rowspan=1 colspan=2>商用</td><td rowspan=1 colspan=1>商用</td></tr><tr><td rowspan=1 colspan=1>互连网络</td><td rowspan=1 colspan=1>总线/交叉开关</td><td rowspan=1 colspan=2>定制</td><td rowspan=1 colspan=1>商用</td></tr><tr><td rowspan=1 colspan=1>系统存储器</td><td rowspan=1 colspan=1>集中共享</td><td rowspan=1 colspan=2>分布共享</td><td rowspan=1 colspan=1>分布共享</td></tr><tr><td rowspan=1 colspan=1>访存模型</td><td rowspan=1 colspan=1>UMA</td><td rowspan=1 colspan=2>NORMA</td><td rowspan=1 colspan=1>NORMA</td></tr><tr><td rowspan=1 colspan=1>代表机器</td><td rowspan=1 colspan=1>Intel SHV,Sun Fire,DEC8400,IBMR60,SGI Power Challenge曙光1号</td><td rowspan=1 colspan=2>Intel Paragon,IBM SP2Intel/Sandia ASCIOption Red,曙光-1000/2000</td><td rowspan=1 colspan=1>Berkeley NOW,Princeton SHRIMP,Rice Tread Marks,HKU Pearlcluster</td></tr></table>

# 习 题

.2.1对于一个100 MHz时钟频率的总线连接的SMP系统,假定总线宽度为8个字节,为了传输16个字节的数据,那么总线带宽可达多少?

2.2试解释系统带宽与系统互连对剖宽度之间的关系,并举一例说明之。

2.3参照图2.6:

$\textcircled{1}$ 试重画图2.6(e),并补上快速链路;

$\textcircled{2}$ 试重画图2.6(f),并补上略去的节点；  
$\textcircled{3}$ 试画出128个节点(256个处理器)的胖超立方；  
$\textcircled{4}$ 试画出512个节点(1024个处理器)的胖超立方。

2.4下面是NOW中使用主动消息,两个进程施行短消息通信的过程,其中进程Q计算数组A,进程P计算标量 $\pmb { x }$ 最终的结果是 $\mathbf { x }$ 与A[7]之和。试解释远程读取的具体过程。

进程P 进程Q   
compute x compute A ： ：   
am- enable(··); am- enable(·…);   
am-request_1(Q,request_h,7); ：   
am - poll(); am- poll();   
$\mathbf { s u n } { \stackrel { \cdot \cdot } { - } } \mathbf { x } + \mathbf { y }$ ： ： am-disable();   
am-disable(); int request- h( vnn-t P,intk)   
int reply- $\mathtt { h } ( \mathtt { v m n \_ t } , \mathbf { Q } , \mathtt { i n t z } )$ {am-relpy-1(P,reply-h A[k]); $\left\{ \mathbf { y } { } = \mathbf { z } { } \right\}$

2.5根据 $\mathbf { x F S }$ ，试回答：

$\textcircled { 1 } \mathbf { x } \mathbf { F } \mathbf { S }$ 与集中式文件服务器之间的主要区别是什么？$\textcircled{2}$ 为了增强可用性， $\bf { x F S }$ 使用了哪些主要技术？

2.6根据2.2.2节有关 $\mathtt { S P 2 }$ 的介绍,试回答：

$\textcircled { 1 } \mathbf { S } \mathbf { P }$ 设计者为了赶上市场作了什么决策？  
$\textcircled{2} \mathbf { S } \mathbf { P }$ 设计者为了达到系统通用采用了什么相应技术？  
③SP系统是如何支持4种SSI的:单一进人点、单一文件层次、单一控制点和单一作业管理系统？  
$\textcircled{4} \textcircled { \mathbf { S P } }$ 设计者为了增加带宽,在通信子系统中主要使用了什么技术？

2.7试解释 RAID(Redundant Array of Inexpensive Disks)工作原理。

2.8试述曙光-2000 系统的可靠性和可用性特色。

2.9试比较 SMP,SSMP,CC-NUMA 和基于机群的MPP以及DSM在体系结构上的异同点。

# 第三章 并行计算性能评测

并行计算的性能评测与并行计算机体系结构、并行算法和并行程序设计一道构成了“并行计算"研究的四大分支,它们相辅相成的发展着。在并行系统上进行计算的主要目的就是要加速整个计算的过程,所以研究并行系统(并行算法并行程序)的加速比性能是最根本的；随着计算负载的增加和机器规模的扩大，研究计算系统的性能是否能随处理器数目的增加而按比例的增加也是很重要的,这就是所谓的并行计算的可扩放性(Scalability)问题；为了客观、公正地评估计算机的性能,提高并行机的使用水平和效率,减少用户引进和购买高性能计算机的盲目性，所以了解掌握一些基本的基准程序也是很必要的。本章将对以上三个问题逐一作简要讨论。

# 3.1加速比性能定律

简单地讲，并行系统的加速(比)是指对于一个给定的应用，并行算法(或并行程序)的执行速度相对于串行算法(或串行程序)的执行速度加快了多少倍，本节将要讨论三种加速比性能定律：适用于固定计算负载的AmdahI定律；适用于可扩放问题的Gustafson定律和受限于存储器的Sun和Ni定律。为了以下讨论方便,兹定义如下参数：令p是并行系统中处理器数；W是问题规模(下文中也常叫作计算负载、工作负载,它定义为给定问题的总计算量),W,是应用程序中的串行分量,W中可并行化部分为Wp(显然W+W,=W);f是串行分量比例(f=W/W,W=W1),1-f为并行分量比例(显然f+(1-f)=1);T,=T1为串行执行时间,T,为并行执行时间;S为加速(比),E为效率。

# 3.1.1 Amdahl 定律

Amdahl加速定律的基本出发点是：①对于很多科学计算，实时性要求很高，即在此类应用中时间是个关键因素，而计算负载是固定不变的。为此在一定的计算负载下，为达到实时性可利用增加处理器数来提高计算速度；②因为固定的计算负载是可分布在多个处理器上的，这样增加了处理器就加快了执行速度，从而达到了加速的目的。在此意义下,1967年Amdahl推导出了如下固定负载的加速公式：

$$
S = \frac { W _ { \mathrm { s } } + W _ { \mathrm { \theta } _ { \mathrm { p } } } } { W _ { \mathrm { s } } + \ W _ { \mathrm { p } } / p }
$$

为了归一化， $W _ { \mathrm { s } } + W _ { \mathrm { p } }$ 可相应地表示为 $f + ( 1 - f )$ ，所以

$$
S = { \frac { f + ( 1 - f ) } { f + { \frac { 1 - f } { p } } } } = { \frac { p } { 1 + f ( p - 1 ) } }
$$

当 $\hbar \to \infty$ 时,上式极限为：

$$
S = \frac { 1 } { f }
$$

这就是著名的Amdahl加速定律,它意味着随着处理器数目的无限增大，并行系统所能达到的加速之上限为 $1 / f$ ，此结论在历史上曾对并行系统的发展起到了悲观的作用。

Amdahl定律的几何意义可清楚地表示在图3.1(a)、(b)和(c)中。

![](images/4e0b6a82a7c4f3620f74dcdc59dbd09e5d04798986b21f4461c0479c5501e4be.jpg)  
图3.1Amdahl加速定律

实际上并行加速不仅受限于程序的串行分量，而且也受并行程序运行时的

额外开销影响。令 $W _ { \mathrm { o } }$ 为额外开销，则(3.1)式应修改为：

$$
S = { \frac { W _ { \mathrm { s } } + W _ { \mathrm { p } } } { W _ { \mathrm { s } } + { \frac { W _ { \mathrm { p } } } { \dot { p } } } + W _ { \mathrm { o } } } } = { \frac { W } { f W + { \frac { W \left( 1 - f \right) } { \dot { p } } } + W _ { \mathrm { o } } } } = { \frac { \dot { p } } { 1 + f ( \dot { p } - 1 ) + W _ { \mathrm { o } } \dot { p } / W } }
$$

当 ${ p \to \infty }$ 时，上式变为：

$$
S = \frac { 1 } { f + W _ { o } / W }
$$

可见,串行分量越大和并行额外开销越大，则加速越小。

# 3.1.2 Gustafson 定律

Gustafson加速定律的基本出发点是： $\textcircled{1}$ 对于很多大型计算，精度要求很高，即在此类应用中精度是个关键因素，而计算时间是固定不变的。此时为了提高精度，必须加大计算量，相应地亦必须增多处理器数才能维持时间不变； $\textcircled{2}$ 除非学术研究，在实际应用中没有必要固定工作负载而使计算程序运行在不同数目的处理器上,增多处理器必须相应地增大问题规模才有实际意义。按此意义，1987年Gustafson给出了如下放大问题规模的加速公式：

$$
S ^ { ' } = \frac { W _ { \mathrm { s } } + \ p W _ { \mathrm { p } } } { W _ { \mathrm { s } } + \ p \cdot W _ { \mathrm { p } } / _ { p } } = \frac { W _ { \mathrm { s } } + \ p W _ { \mathrm { p } } } { W _ { \mathrm { s } } + \ W _ { \mathrm { p } } }
$$

归一化后可得

$$
S ^ { \prime } = f + \ p ( 1 - f ) = p + f ( 1 - p ) = p - f ( p - 1 )
$$

当 $\pmb { \hat { p } }$ 充分大时， $s ^ { \prime }$ 与 $\pmb { \mathscr { P } }$ 几乎成线性关系，其斜率为 $1 \mathrm { ~ - ~ } f$ 。这就是著名的Gustafson加速定律，它意味着随着处理器数目的增加,加速几乎与处理器数成比例的线性增加,串行比例 $f$ 不再是程序的瓶颈，这对并行系统的发展是个非常乐观的结论。

Gustafson 定律的几何意义可清楚地表示在图3.2(a)、(b)和 $\left( \mathbf { c } \right)$ 中。

同样,当考虑到并行程序运行时的额外开销 $\mathbf { { w } } _ { \mathbf { { o } } }$ 时,(3.6)式应修改为：

$$
S ^ { \prime } = \frac { W _ { s } + \ p W _ { p } } { W _ { s } + W _ { p } + W _ { o } } = \frac { f + \ p \left( 1 - f \right) } { 1 + W _ { o } / W }
$$

注意： ${ { \bf { W } } _ { \bf { 0 } } }$ 是 $\pmb { \hat { p } }$ 的函数,它可能随 $\pmb { \hat { p } }$ 增大、减小或不变。一般化的Gustafson定律欲达到线性加速必须使 $\Psi _ { \mathbf { 0 } }$ 随 $\pmb { \phi }$ 减小,但这常常是困难的。

# 3.1.3 Sun 和 Ni定律

Xian-He Sun 和Lionel Ni于1993 年曾将 Amdahl 定律和 Gustafson 定律一般化,提出了存储受限的加速定律。其基本思想是只要存储空间许可，应尽量增大问题规模以产生更好或更精确的解(此时可能使执行时间略有增加)。换句话说，假若有足够的存储容量,并且规模可扩放的问题满足Gustafson定律规定的时间要求，那么就有可能进一步增大问题规模求得更好或更精确的解。

![](images/3879ee581fbd2cf223f1d5ab80a27c49b8759a3a37da3d9cf8f18e092bc4e587.jpg)  
图3.2Gustafson加速定律

给定·个存储受限问题，假定在单节点上使用了全部存储容量 $M$ 并在相应于W的时间内求解之,此时工作负载 $\boldsymbol { W } = \boldsymbol { \mathscr { J } } \boldsymbol { W } + \left( 1 - \boldsymbol { \mathscr { J } } \right) \boldsymbol { W }$ 。在 $\pmb { \mathscr { p } }$ 个节点的并行系统上,能够求解较大规模的问题是因为存储容量可增加到 $_ { \mathit { p M } }$ 。令因子${ \bf \Xi } ( { \bf \Lambda } _ { \bf \dot { J } } )$ 反映存储容量增加 $\pmb { \mathscr { p } }$ 倍时工作负载的增加量，所以扩大后的工作负载$W = \ j W + \left( 1 - f \right) \zeta i ( \ j ) W ,$ ，对照(3.6)式,存储受限的加速公式相应为：

$$
S ^ { \prime \prime } { = } \frac { \not { I W } + \left( 1 - \not { I ^ { \prime } } \right) \not { G } \left( p \right) W } { \not { J W } + \left( 1 - \not { I ^ { \prime } } \right) \not { G } \left( p \right) W \not { J p } }
$$

归一化后可得

$$
S ^ { \prime \prime } { = } \frac { \int { + \left( 1 - j ^ { \prime } \right) ( j ^ { } ( p ) } } { \int { + \left( 1 - j ^ { \prime } \right) ( j ^ { } ( p ) / p } }
$$

Sun 和 ${ \ N i }$ 定律的儿何意义可清楚地表示在图3.3(a)和(b)中。

同样，当考虑到并行程序运行时的额外开销 $W _ { \mathrm { 0 } }$ 时，(3.9)式和(3.10)式可修改为：

$$
S ^ { \prime \prime } { = } \frac { f W + \left( 1 - f \right) W G \left( \rlap { / } p \right) } { f W + \left( 1 - f \right) G \left( \rlap { / } p \right) W / \rlap { / } p + W _ { 0 } } { = } \frac { f + \left( 1 - f \right) G \left( \rlap { / } p \right) } { f + \left( 1 - f \right) G \left( \rlap { / } p \right) / \rlap { / } p + W _ { 0 } / W }
$$

![](images/dc8f2284af0f7b2f51d35692f9b914836194d5fd11893704c797ead1930ba4c0.jpg)  
图3.3Sun和 $\mathbf { N _ { i } }$ 加速定律

由(3.10)可知，当 $G ( \pmb { \mathscr { p } } ) = \mathbf { 1 }$ 时，它变为 $\frac { 1 } { f + ( 1 - f ) / \phi }$ ，这就是 Amdahl加速定律(3.2)式;当 $G ( { \boldsymbol { \mathbf { \mathit { \phi } } } } ) = \phi$ 时,它变为 $f + \phi ( 1 - f )$ ,这就是Gustafson 加速定律(3.7)式；当 $G ( { \pmb \cdot } ) > _ { P }$ 时,它相应于计算负载比存储要求增加得快,此时 $\mathtt { s u n }$ 和${ \bf N } _ { \mathbf { i } } ^ { \mathbf { \cdot } }$ 加速均比Amdahl加速和Gustafson加速为高。

# 3.1.4有关加速的讨论

在实际应用中,可供参考的加速经验公式是：

$$
\scriptstyle { \pmb { \mathscr { p } } } \lambda _ { 0 \pmb { \mathscr { g } } \pmb { \mathscr { p } } } { \leqslant } S { \leqslant } p
$$

可达线性加速的应用问题有诸如矩阵相加、内积运算等,此类问题几乎没有通信开销;对于分治类的应用问题,它类似于二叉树,树的同级可并行执行,但向根逐级推进时，并行度将逐渐减少,此类问题可望达到 $\pmb { \phi } \pmb { \Lambda } \infty \pmb { \Lambda } p$ 的加速;对于通信密集类的应用问题,其加速经验公式可参考下式：

$$
S = 1 / C ( \mathbf { \Omega } _ { \hat { P } } )
$$

其中 $C ( \pmb { \mathscr { p } } )$ 是 $\pmb { \mathscr { P } }$ 个处理器的某一通信函数,或为线性的或为对数的。

严格的线性加速是难以达到的，更何况超线性加速（Superlinear Speedup）。但在某些算法或程序中,可能会出现超线性加速现象：例如,在某些并行搜索算法中,允许不同的处理器在不同的分枝方向上同时搜索，当某一处理器一旦迅速地找到了解，它就向其余的处理器发出中止搜索的信号，这就会提前取消那些在串行算法中所作的无谓的搜索分枝，从而出现超线性加速现象；又如，在绝大多数并行机中，每个处理器均有少量的高速缓存，当某一问题执行在大量的处理器上,而其大多的数据均放在高速缓存中时，总的计算时间趋于减少，如果由于这种高速缓存效应所造成的计算时间下降补尝了由于通信等所造成的额外开销时间，则有可能造成超线性加速现象。

最后值得指出的是，加速的含意对科学研究者和工程实用者可能有所不同：前者乐于使用绝对加速(Absolute Speedup)的定义，即对于给定的问题,最佳串行算法所用的时间除以同一问题其并行算法所用的时间；后者乐于使用相对加速(Rel-ative Speedup)的定义,即对于给定的问题,同一个算法在单处理器上运行的时间除以在多个处理器上运行的时间。显然相对加速的定义是较宽松和实际的。

# 3.2 可扩放性评测标准

评价并行计算性能的指标，除了上节所介绍的加速比以外，并行计算的可扩放性(Scalability)也是主要性能指标之一。可扩放性最简朴的含意是在确定的应用背景下,计算机系统(或算法或编程等)性能随处理器数的增加而按比例提高的能力。现今它已成为并行处理中一个重要的研究问题，被越来越广泛地用来描述并行算法(并行程序)能否有效利用可扩充的处理器数的能力。

# 3.2.1并行计算的可扩放性

从上节所介绍的三种加速定律可知，增加处理器数和求解问题的规模都可能提高加速比，而影响加速的因素有： $\textcircled{1}$ 求解问题中的串行分量； $\textcircled{2}$ 并行处理所引起的额外开销(通信、等待、竞争、冗余操作和同步等); $\textcircled{3}$ 加大的处理器数超过了算法中的并发程度。增加问题的规模有利于提高加速的因素是： $\textcircled{1}$ 较大的问题规模可提供较高的并发度； $\textcircled{2}$ 额外开销的增加可能慢于有效计算的增加； $\textcircled{3}$ 算法中的串行分量比例不是固定不变的(串行部分所占的比例随着问题规模的增大而缩小)。一般情况下，增加处理器数，是会增大额外开销和降低处理器的利用率的,所以对于一个特定的并行系统、并行算法或并行程序，它们能否有效利用不断增加的处理器的能力应是受限的，而度量这种能力就是可扩放性这一指标。

按照Webster 字典所作的定义(Scalability is the ability to scale,i.e,the abili-ty to adjust according toaproportion),可扩放性涉及到调整什么和按什么比例两方面的问题。对于并行计算而言，要调整的是处理器数 $\pmb { \hat { p } }$ 和问题规模W,两者可按不同比例进行调整,此比例关系(可能是线性的、多项式的或指数的等)就反

映了可扩放的程度。

当研究可扩放性时，总是将并行算法和体系结构一并考虑，也就是说可扩放性应该是算法和结构的组合。所以当谈论算法的可扩放性时，实际上是指该算法针对某一特定机器结构的可扩放性；同样当谈论体系结构的可扩放性时，实际上是指运行于该体系结构的机器上的某一个(或某一类)并行算法的可扩放性。

进行可扩放性研究的主要目的是： $\textcircled{1}$ 确定解决某类问题用何种并行算法与何种并行体系结构的组合，可以有效地利用大量的处理器； $\textcircled{2}$ 对于运行于某种体系结构的并行机上的某种算法，根据算法在小规模处理机上的运行性能，预测该并行算法当移植到大规模处理机上后运行的性能； $\textcircled{3}$ 对固定的问题规模，确定在某类并行机上最优的处理器数与可获得的最大的加速比； $\textcircled{4}$ 用于指导改进并行算法和并行机体系结构,以使并行算法尽可能地充分利用可扩充的大量处理器。

尽管可扩放性如此重要,并且已被广泛的研究，但目前仍无一个公认的、标准的和被普遍接受的严格定义和评判它的标准。下面从不同的角度,介绍三种典型的可扩放性度量方法，即等效率、等速度和平均延迟方法。

# 3.2.2等效率度量标准

可扩放性的概念是与加速比和效率的概念紧密相关的，为此必须先从加速$s$ 和效率 $E$ 讲起。

令 $t _ { \mathrm { ~ e ~ } } ^ { i }$ 和 $t _ { 0 } ^ { i }$ 分别是并行系统上第 $\textbf { \em i }$ 个处理器的有用计算时间和额外开销时间(包括通信、同步和空闲等待时间等);所有 $t _ { e } ^ { i }$ 之和记之为 $T _ { \mathrm { e } } = \sum _ { i = 0 } ^ { { \boldsymbol { p } } - 1 } t _ { \mathrm { e } } ^ { i }$ ，所有 $t _ { 0 } ^ { i }$ 之和记之为 $T _ { 0 } = \sum _ { i = 0 } ^ { { p - 1 } } t _ { 0 } ^ { i }$ to;令Tp是p个处理器系统上并行算法的运行时间，对于任意 $_ i$ ,显然有 $T _ { \mathrm { p } } = \mathrm { \Delta } t _ { \mathrm { e } } ^ { i } + \mathrm { \Delta } t _ { 0 } ^ { i }$ ，且

$$
\begin{array} { r } { T _ { e } + \ T _ { o } = \ p T _ { p } } \end{array}
$$

问题的规模W可定义为由最佳串行算法所完成的计算量,也称工作负载或工作量，即 $W = T _ { \mathrm { e } }$ 。所以并行算法的加速和效率可分别定义如下：

$$
S = { \frac { T _ { \mathrm { e } } } { T _ { \mathrm { p } } } } = \underbrace { { \frac { T _ { \mathrm { e } } } { T _ { \mathrm { e } } + T _ { \mathrm { o } } } } } _ { \displaystyle { \hat { p } } } = { \frac { \displaystyle { \hat { p } } } { \displaystyle { 1 + { \frac { T _ { \mathrm { o } } } { T _ { \mathrm { e } } } } } } } = { \frac { \displaystyle { \hat { p } } } { \displaystyle { 1 + { \frac { T _ { \mathrm { o } } } { W } } } } }
$$

$$
E = { \frac { S } { \phi } } = { \frac { 1 } { 1 + { \frac { T _ { \circ } } { T _ { \mathrm { e } } } } } } = { \frac { 1 } { 1 + { \frac { T _ { \circ } } { W } } } }
$$

在通常情况下，如果问题规模W保持不变(即T。保持不变),则随着处理器数p的增加，开销T。也会随之增大,根据(3.16)式,效率E也会相应下降。为了维持效率E不变,就要保持T/T。的值不变,故需要在处理器数p增大的同时相应地增加问题规模W的值（即 $T _ { \epsilon }$ 的值)才有可能抵消由于 $\boldsymbol { p }$ 的增大而导致 $T _ { \mathrm { { o } } }$ 增大的影响，从而保持效率不变。也就是说，为了维持一定的效率（介于0与1之间),当处理数 $\pmb { \mathit { p } }$ 增大时，需要相应地增大问题规模W的值。由此定义函数 $f _ { \mathrm { { F } } } ( \mathbf { \Gamma } _ { P } )$ 为问题规模W随处理器数 $\boldsymbol { p }$ 变化的函数，称此函数为等效率函数(ISO-efficiency Function),它是由Kumar 等人1987年提出的。

按照等效率函数的定义，对于某一并行算法(或并行程序),为了维持运行效率保持不变，随着处理器数目的增加，若只需增加较小的工作量(即问题规模),比如说W随 $\pmb { \mathscr { p } }$ 呈线性或亚线性增长，则表示该算法具有良好的可扩放性;若需增加非常大的问题规模,比如说W随 $\pmb { \mathscr { p } }$ 呈指数级增长，则表示该算法是不可扩放的。

图3.4给出了三种等效率函数曲线，曲线1表示算法具有很好的扩放性;曲线2表示算法是可扩放的；曲线3表示算法是不可扩放的。

![](images/c5bfc7384a6162eabda91d1af3d808250584b675a85a1719ba480db72891a43c.jpg)  
图3.4等效率函数曲线

下面使用等效率函数方法来分析超立方网络上的FFT算法的可扩放性。

对于 $_ { n }$ 点 FFT算法，假定一个计算单位的成本是 $t _ { \mathrm { c } }$ ，则 $T _ { \mathrm { c } } = \mathbf { \boldsymbol { W } } = t _ { \mathrm { c } } \pi \mathrm { l o g } n _ { \mathrm { ~ o ~ } }$ 假定使用 $\smash { p = 2 ^ { d } }$ 个处理器来进行计算，则每个处理器计算 $n / p$ 个值。因为在并行计算FFT时，最多只能使用 $^ { n }$ 个处理器(否则多余的处理器无事可做),所以等效率函数的下界为 $\Omega \big ( \hbar \log p \big )$ ,它是算法固有并行度的函数,与并行结构无关。

利用(3.16)式计算等效率函数时,关键是如何计算 $T _ { \mathrm { { o } } }$ 。在计算FFT时 $T _ { \mathrm { { o } } }$ 主要来源于两个处理器之间的通信,从一个处理器发送一条消息至另一个处理器所涉及到的开销包括： $\textcircled{1}$ 通信建立时间 $t _ { \textrm { s } }$ ，它与消息长短和所走过的距离无关； $\textcircled{2}$ 跨步 $\left( \mathrm { H o } _ { \mathfrak { g } } \ltimes \right)$ 延迟 $t _ { \mathfrak { h } }$ ,它等于相邻两计算节点之间一个单位消息的延迟时间（不包括$t _ { \mathrm { s } } ) { : \textcircled { \cdot } }$ 每个字节占用时间 $t _ { \mathrm { b } }$ ，它等于通信带宽 $B$ (字节/秒)的倒数。所以条长为$\nu \eta$ 的消息，从源到目的其间经由 $l$ 个跨步点时的通信开销为： $t _ { \mathrm { s } } + \big ( t _ { \mathfrak { h } } , m + t _ { \mathfrak { h } } \big ) l _ { \mathrm { ~ o ~ } }$ 令 $l _ { j }$ 是第 $j$ 次迭代计算时两通信处理器之间的海明距离，且假定它们等长；假定不同消息选路时互不重叠。因为每个处理器包含有 $n / p$ 个数据,所以总的通信开

销 $T _ { \circ }$ 为：

$$
T _ { \mathrm { o } } \mathrm { = } \phi \sum _ { j \mathrm { = 0 } } ^ { d \mathrm { - 1 } } \big [ t _ { \mathrm { s } } + \big ( t _ { \mathrm { h } } + t _ { \mathrm { b } } n / \phi \big ) l _ { j } \big ]
$$

在超立方网络中，所有成对通信的处理器之间的距离恒为1,所以(3.17)式变为：

$$
T _ { \circ } = \dot { p } \sum _ { j = 0 } ^ { \log \beta - 1 } \left( t _ { s } + t _ { \mathrm { h } } + t _ { \mathrm { b } } n / \dot { p } \right) = \left( t _ { \mathrm { h } } + t _ { s } \right) \dot { p } \log \phi + t _ { \mathrm { b } } \pi \log \phi \ .
$$

当 $\pmb { \hat { p } }$ 增加时,为了维持 $E$ 在某一值, $\pmb { n }$ 亦必须增加使得 $T _ { \mathrm { e } } = k T _ { \mathrm { o } }$ ,即

$$
t _ { \mathrm { c } } n \log n = k \left[ \left( t _ { \mathrm { h } } + t _ { \mathrm { s } } \right) \hbar \log \phi + t _ { \mathrm { b } } n \log \phi \right]
$$

其中 $k = E / ( 1 - E )$ 。由于 $n \log _ { \mathcal { P } } \gg _ { \mathcal { P } } \log _ { \mathcal { P } }$ ,所以(3.19)式中第二项为主项,即可考虑 $t _ { \mathrm { c } } n \log n = k t _ { \mathrm { b } } n \log \phi$ 之情况,经过简单代数变换，则得

$$
n = p ^ { k t } \mathfrak { { b } } ^ { / t } \mathfrak { { c } }
$$

因为 $\boldsymbol { W } = \boldsymbol { t } _ { \mathrm { c } } n \log \boldsymbol { n }$ ,所以等效率函数 $f _ { \mathbb { E } } ( \mathbf { \nabla } _ { \mathcal { P } } )$ 为：

$$
W = f _ { \mathrm { E } } ( \mathbf { \nabla } _ { \phi } ) = k t _ { \mathrm { b } } \mathbf { \nabla } \phi ^ { k t _ { \mathrm { b } } / t _ { \mathrm { c l o g } \phi } }
$$

上式中只要 ktb/t<1,则W的增长率小于O(plogp);-旦ktb/t>1,则等效率函数随着 $k \frac { t _ { \mathrm { b } } } { t _ { \mathrm { c } } }$ 的增大急剧恶化;当 $t _ { b } = t _ { c }$ 时，若 $k < 1$ （即 ${ E < } 0 . 5 )$ ，则W$\mathbf { \Psi } = \theta \left( \ p \log { \mathbf { \alpha } } \right)$ ；若 $k > 1$ （即 $\mathbf { \mathcal { E } } > \mathbf { 0 } \mathbf { \mathcal { . } } \mathbf { \mathcal { 5 } } )$ ，例如说 $E = 0 . 9$ ，则 $k = 9$ ，于是 $\pmb { W } =$ $\Theta \big ( \ b { \phi } ^ { \boldsymbol { \mathfrak { s } } } \mathrm { l o g } \ b { \phi } \big )$ 。此时的等效率函数要差得多。这说明,如果 $t _ { \mathrm { b } } = t _ { \mathrm { c } }$ ,在大的超立方网络上很难得到比0.5高得多的效率。

# 3.2.3等速度度量标准

等效率度量标准最大优点是，可用简单的、可定量计算的、少量的参数就能计算出等效率函数，并由其复杂性可指明算法的可扩放程度。这对于具有网络互连结构的并行机来说是很合适的,因为已如上一节例子那样，T。是可一步一步计算出的。也正是这个T。是计算等效率函数的唯一关键参数，所以如果它不能够方便地计算出，则等效率函数度量可扩放性的方法就受到了限制。我们知道开销T。通常包括了通信、同步、等待等非有效计算时间。不幸的是,在共享存储的并行计算机中,T。则主要是非局部访问的读/写时间、进程调度时间、存储竞争时间以及高速缓存一致性操作时间等,而这些时间都是难以准确计算的。所以用解析计算的方法度量可扩放性不应是一种唯一的方法。事实上，两位中国学者 Xian-He Sun 和 Xiao Dong Zhang于 1994 年分别提出了以试验测试为主要手段的两种评测可扩放性的标准，即等速度(ISO-speed)和平均延迟(AverageLatency)标准。本节先介绍前者，下节再介绍后者。

大家知道,速度是一个非常重要的机器参数，一般在机器性能指标中都明确地给出，并常以每秒多少次浮点运算(Flops)来表明(按照约定的含意，浮点运算数目就是工作负载W)。所以若用速度来度量可扩放性,在原理上讲是更方便的,而等速度方法的基本出发点就在于此。

在并行系统中，提高速度可以使用增加处理器数的办法，如果速度能以处理器数的增加而线性增加(此即意味着平均速度不变),则说明此系统具有很好的扩放性。为此先作如下定义：

令 $\pmb { \mathscr { p } }$ 表示处理器个数,W表示要求解问题的工作量或称问题规模(在此可指浮点操作个数)， $T$ 为并行执行时间，则定义并行计算的速度 $V$ 为工作量W除以并行时间 $T$ ：

$$
V = W / T
$$

而 $\pmb { \hat { p } }$ 个处理器的并行系统的平均速度定义为并行计算速度 $\boldsymbol { V }$ 除以处理器个数$\pmb { \phi }$ ：

$$
\overline { { V } } = \frac { V } { \rho } { \overset { . } { = } } \frac { \overline { { W } } } { \rho T }
$$

根据平均速度(3.23)式,就可定义等平均速度(简称为等速度)可扩放度量标准如下：

对于运行于并行机上的某个算法，当处理器数目增加时,若增大一定的工作量能维持整个并行系统的平均速度不变，则称该计算是可扩放的。

注意,平均速度为常数,意即速度与处理器数目成线性比例增长,亦即加速比为线性的。

按此定义,令W是使用 $\pmb { \mathscr { P } }$ 个处理器时算法的工作量,令 $\mathbf { \overrightarrow { W } } ^ { \prime }$ 表示当处理数从 $\pmb { \hat { p } }$ 增大到 $\pmb { \hat { p } } ^ { \prime }$ 时,为了保持整个系统的平均速度不变所需执行的工作量，则可得到处理器数从 $\pmb { \hat { p } }$ 到 $\pmb { \hat { p } } ^ { \prime }$ 时平均速度可扩放度量标准公式为：

$$
\Psi ( \boldsymbol { \phi } , \boldsymbol { \phi } ^ { \prime } ) = \frac { W / p } { W ^ { \prime } / p ^ { \prime } } = \frac { \boldsymbol { \phi } ^ { \prime } W } { \boldsymbol { \phi } W ^ { \prime } }
$$

用上述公式计算出的值介于0与1之间,值越大表示可扩放性越好。

当平均速度严格保持不变时,即

$$
\frac { W } { T \hat { p } } = \frac { W ^ { \prime } } { T ^ { \prime } \hat { p ^ { \prime } } } \to \frac { \hat { p ^ { \prime } } W } { \hat { p } W ^ { \prime } } = \frac { T } { T ^ { \prime } }
$$

所以，(3.24)式可变为：

$$
\Psi ^ { \prime } ( \phi , \phi ^ { \prime } ) = \frac { T } { T ^ { \prime } }
$$

当p=1时,记T=T;当处理器个数为p'时,记T=Tp;相应地记p=1时 $\boldsymbol { \Psi } ( \boldsymbol { 1 } , \boldsymbol { \phi } ^ { \prime } )$ 为 $\pmb { \varPsi } ( \pmb { \mathscr { p } } ^ { \prime } )$ ,于是有

$$
\Psi ( \ p ^ { ' } ) = \frac { \hbar ^ { 2 } W } { W ^ { ' } } = \frac { T _ { 1 } } { T _ { \mathrm { p ^ { ' } } } } = \frac { W } { W ^ { ' } / p ^ { ' } } = \frac  \frac { \hbar \pi } { \hbar \pi } \pm \frac { \hbar } { \hbar } . \pm \frac { \gamma } { \hbar } \ \frac { \hbar } { \hbar } \pm \frac { \gamma } { \hbar } \ \frac { \hbar } { \hbar } \pm \frac { \hbar } { \hbar } \pm \frac { \hbar } { \hbar } \pm \frac { \gamma } { \hbar \pi } \pm \frac { \hbar } { \hbar \pi } \pm \frac { \gamma } { \hbar \pi } \pm \frac { \hbar } { \hbar } \pm \frac { \gamma } { \hbar } \pm \frac { \hbar } { \hbar } \pm \frac { \gamma } { \hbar } \pm \frac { \hbar } { \hbar } \pm \frac { \gamma } { \hbar } \pm \frac { \hbar } { \hbar } \pm \frac { \gamma } { \hbar } \pm \frac { \hbar } { \hbar } \pm \frac { \gamma } { \hbar } \pm \frac { \hbar } { \hbar } \pm \frac { \gamma } { \hbar } \pm \frac { \hbar } { \hbar } \pm \frac { \gamma } { \hbar } \pm \frac { \gamma } { \hbar \pi } \pm \frac { \hbar } { \hbar } \pm \frac { \gamma } { \hbar } \pm \frac { \gamma } { \hbar } \pm \frac { \hbar } { \hbar } \pm \frac { \gamma } { \hbar } \pm \frac { \gamma } { \hbar \pi } \pm \frac { \hbar } { \hbar } \pm \frac { \gamma } { \hbar } \pm \frac { \gamma } { \hbar \pi } \pm \frac { \gamma } { \hbar \pi } \pm \frac { \gamma } { \hbar \pi } \pm \frac { \gamma } { \hbar \pi } \pm \frac { \gamma } { \hbar } \pm \frac { \gamma } { \hbar } \pm \frac { \gamma } { \hbar } \pm \frac { \gamma } { \hbar \pi } \pm \frac { \gamma } { \hbar \pi } \pm \frac { \gamma } { \hbar \pi } \pm \frac { \gamma } { \hbar \pi } \pm \frac { \gamma } { \hbar \pi } \pm \frac { \gamma } { \hbar } \pm \frac { \gamma } { \hbar } \pm \frac { \gamma } { \hbar } \pm \frac { \gamma } { \hbar \pi } \pm \frac { \gamma } { \hbar \pi } \pm \frac { \gamma } { \hbar \pi } \pm \frac { \gamma } { \hbar \pi } \pm \frac { \gamma } { \hbar } \pm \frac { \gamma } { \hbar } \pm \frac { \gamma } { \hbar } \pm \frac { \gamma } { \hbar } \pm \frac  
$$

(3.26)式给出的可扩放性定义与传统的加速比定义有点类似，其主要差别在于：加速比的定义是保持问题规模不变；而可扩放性定义是保持平均速度不变。如图3.5所示，加速比是标志并行处理相对于串行处理所获得性能增加；而如图3.6所示，可扩放性是标志从小规模系统到大规模系统所引起的性能衰减。

![](images/3126c0a33f534b879d5991c2b8837c2c375a18009aa27a58cf1e231823166ec5.jpg)  
图3.5加速比：问题规模不变,时间变短

![](images/63118f117a3e66dc599541eb302a4ab3d6eeacc0e37a23b9eb2a7e6b136b4c7c.jpg)  
图3.6可扩放性：平均速度不变,时间加长

一般有三种方法可得到等速度可扩放性标准： $\textcircled{1}$ 测量法：使用软件方法，即采用控制程序去调用应用程序，找寻所希望的固定的平均速度；②计算法：首先找出平均速度和执行时间之间的关系，再使用(3.25)式计算之；③预计法：采用推导一般可扩放性公式来研究可扩放性。

下面，只简单介绍一下第二种方法，它结合一组测量的数据（V和T）借助几何作图法和通过使用公式(3.25),最终画出一组等速度可扩放性曲线,其具体步骤是：

① 测量平均速度V和并行执行时间T：给定某一应用程序，使其运行在m。个处理器的并行机上,固定mo,改变工作量范围W到W',测量相应平均速度和运行时间,改变mo到m1,固定m1,改变工作量范围W到W',测量相应平均速度和运行时间；重复之，可绘制出一组如图3.7所示的一组V-T曲线。

![](images/aa3e8d1191139ca696bd3dbfe4f762f8c1480ea21f7d125ece0e1258051c86da.jpg)  
图3.7 ${ \overline { { \boldsymbol { v } } } } - { \boldsymbol { T } }$ 曲线

$\textcircled{2}$ 选择参考平均速度 $\overline { { V } } _ { \frac { 1 } { 2 } }$ ,求出不同处理器数时的执行时间 $T _ { \mathrm { i } }$ ：令 $\overline { { V } } _ { \infty }$ 是在单处理机上、 ${ \pmb W }  \infty$ 时的渐近平均速度;取其一半 $\frac { 1 } { 2 } \overline { { V } } _ { \infty }$ 作为参考平均速度$\overline { { V } } _ { \frac { 1 } { 2 } }$ ,在图3.7之纵坐标上，过点 $\overline { { V } } _ { \frac { 1 } { 2 } }$ 作平行于水平轴的直线;过该直线与诸曲线的交点,分别作平行于垂直轴的直线,它们与 $\pmb { X }$ 轴的交点就是相应于各处理器的执行时间。

$\textcircled{3}$ 根据(3.25)式，计算 $\Psi \big ( \boldsymbol { \phi } , \boldsymbol { \phi } ^ { \prime } \big )$ 之值,它就是所要求的等速度可扩放性标准。

对于某一应用程序,若取 $\overline { { V } } \frac { 1 } { 2 } = \frac { 1 } { 2 } \overline { { V } } _ { \infty } = \frac { 1 } { 2 } \times 1 . 7 \left( \mathrm { M f l o p s } \right) = 0 . 8 5 \left( \mathrm { M f l o p s } \right) ,$ 根据图3.7,可作出表3.1所示的处理器个数与相应执行时间表;当平均速度不变时，根据表3.1,利用(3.25)式，就可计算出如表3.2所示的诸 $\bar { \pmb { \Psi } } ( \pmb { \phi } , \pmb { \phi } ^ { \prime } )$ 之值；根据表3.2,再补充一些数据项,就可作出如表3.3所示的 $\Psi \big ( \ b { \phi } , \ b { \phi } ^ { \prime } \big )$ 上三角阵。

表3.1处理器数及其相应执行时间一览表  

<table><tr><td rowspan=1 colspan=1>处理器数</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>：  2</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>16</td><td rowspan=1 colspan=1>32</td><td rowspan=1 colspan=1>64</td><td rowspan=1 colspan=1>128</td></tr><tr><td rowspan=1 colspan=1>执行时间</td><td rowspan=1 colspan=1>0.004 029</td><td rowspan=1 colspan=1>0.09 13</td><td rowspan=1 colspan=1>0.013 62</td><td rowspan=1 colspan=1>0.017 44</td><td rowspan=1 colspan=1>0.021 44</td><td rowspan=1 colspan=1>0.025 61</td><td rowspan=1 colspan=1>0.029 6</td><td rowspan=1 colspan=1>0.033 38</td></tr></table>

表3.2 $\yen ( p , p ^ { \prime } )$ 一览表  

<table><tr><td rowspan=1 colspan=1>(1,2)</td><td rowspan=1 colspan=1>亚(2,4)</td><td rowspan=1 colspan=1>亚(4,8)</td><td rowspan=1 colspan=1>(8,16)</td><td rowspan=1 colspan=1>亚(16,32)</td><td rowspan=1 colspan=1>亚(32,64)</td><td rowspan=1 colspan=1>(64,128)</td></tr><tr><td rowspan=1 colspan=1>0.441</td><td rowspan=1 colspan=1>0.670</td><td rowspan=1 colspan=1>0.781</td><td rowspan=1 colspan=1>0.831</td><td rowspan=1 colspan=1>0.837</td><td rowspan=1 colspan=1>0.865</td><td rowspan=1 colspan=1>0.887</td></tr></table>

表3.3 $\yen ( p , p ^ { \prime } )$ 上三角阵  

<table><tr><td rowspan=1 colspan=1>处理器数</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>16</td><td rowspan=1 colspan=1>32</td><td rowspan=1 colspan=1>64</td><td rowspan=1 colspan=1>128</td></tr><tr><td rowspan=1 colspan=1>1248163264128</td><td rowspan=1 colspan=1>1.000</td><td rowspan=1 colspan=1>0.4411.000</td><td rowspan=1 colspan=1>0.2960.6701.000</td><td rowspan=1 colspan=1>0.2310.5240.7811.000</td><td rowspan=1 colspan=1>0.1880.4260.6350.8131.000</td><td rowspan=1 colspan=1>0.1570.3570.5320.6810.8371.000</td><td rowspan=1 colspan=1>0.1360.3080.4600.5890.7240.8651.000·</td><td rowspan=1 colspan=1>0.1210.2740.4080.5220.6420.7670.8871.000</td></tr></table>

$\textcircled{4}$ 根据表3.3,对其每一行都可作出一条 $\pmb { \psi } ( \pmb { \phi } ^ { \prime } )$ 与 $\pmb { \phi } ^ { \prime }$ 的变化曲线，显然增大起始的处理器数可改善系统的可扩放性。图3.8示出了 $\pmb { \psi } ( \pmb { \phi } ^ { \prime } )$ 与 $\pmb { \hat { p } ^ { \prime } }$ 变化曲线簇，曲线越平坦，可扩放性越好。

![](images/02b97e76282e377706819e615103980d4f597d75449171607b9aadefa3b7f944.jpg)  
图3.8以 $\pmb { \hat { p } }$ 为参数的 $\pmb { \psi } ( \pmb { \phi } ^ { \prime } )$ 与 $\pmb { \hat { p } } ^ { \prime }$ 变化曲线簇

# 3.2.4平均延迟度量标准

等速度度量标准最大优点是，使用机器性能速度指标这一明确的物理量来度量可扩放性是比较直观的。它有一系列优点： $\textcircled{1}$ 速度是由工作负载W和执行时间 $T$ 决定的,而W反映了应用程序的性质， $T$ 反映了结构和程序效率的影响；②速度是各种结构的机器相互可比较的量;③执行时间包含了计算和延迟这两个主要的时间量；④速度是比较容易测量的，因为W可由所执行的浮点操作数决定。但它也有一些不足：①仅用浮点操作数作为W是不全面的，某些非浮点运算可能造成性能的主要变化；②延迟虽包含在执行时间中，但它未明确地定义为W的函数。实际上，可扩放性测定可以在系统和应用的更低层上，它们能更精确地抓住影响性能的结构因素和程序开销模式。下面将介绍使用测量平均延迟开销的办法来度量可扩放性。为此先作如下定义：

参照图3.9,令 $T _ { i }$ 为 $\boldsymbol { \mathrm { { P } } } _ { i }$ 的执行时间、它还包括在运行时所招致的延迟 $L _ { i }$ ，程序运行时还包括启动与停止时间。所以第 $i$ 个处理器 $\mathrm { \bf P } _ { i }$ 的总延迟时间为 ${ } ^ { \bullet } L _ { i }$ $+$ 启动时间 $^ +$ 停止时间”。定义系统平均延迟时间 $\overline { { L } } ( W , \boldsymbol { p } )$ 为：

$$
\overline { { L } } ( W , \ / p ) = \sum _ { i ^ { - } 1 } ^ { \prime ^ { \prime } } ( T _ { \mathrm { p a r a } } - T _ { i } + L _ { i } ) / p
$$

因为， $p T _ { \mathrm { p s t r a } } { = } T _ { \mathrm { o } } { + } T _ { \mathrm { s u t } } ( T _ { \mathrm { s u t } }$ 为串行执行时间)和 $T _ { \mathrm { o } } \mathrm { = } f \overline { { L } } \mathrm { ( } W , \mathbf { \phi } _ { p } \mathrm { ) }$ ，所以

$$
\overline { { L } } ( \ : W , / p ) = T _ { \mathrm { p a r a } } - T _ { \mathrm { s a q } } / p
$$

执行时间

![](images/3e049b90442328184f377925219e57c22fdc28593b1dac103d3a02957a9022a0.jpg)  
图3.9定义平均延迟示意图

对于一个算法-机器组合，令 $\overline { { L } } ( W , \boldsymbol { p } )$ 表示在 $p$ 个处理器上求解工作量为W问题的平均延迟; $\overline { { L } } ( \boldsymbol { W } ^ { \prime } , \boldsymbol { p } ^ { \prime } )$ 表示在 ${ \boldsymbol { p } } ^ { \prime }$ 个处理器上求解工作量为W'问题的平均延迟。当处理器数由 $\boldsymbol { \mathscr { p } }$ 变到 $p ^ { ' }$ ,而维持并行执行效率不变,则定义平均延迟可扩放性度量标准为：

$$
\bar { \phi } ( E , \boldsymbol { \rho } , \boldsymbol { \rho } ^ { \prime } ) = \frac { \overline { { L } } ( W , \boldsymbol { \rho } ) } { \overline { { L } } ( W ^ { \prime } , \boldsymbol { \rho } ^ { \prime } ) }
$$

用上述公式计算出的值介于0与1之间,值越大表示可扩放性越好。

下面,简单介绍一下使用平均延迟度量可扩放性的全过程：

①给定系统处理器数的变化范围和期望的效率E,按如下流程调整工作量W,直到满足所要求的E,最后计算出平均延迟。

②绘制延迟曲线：对于·个给定的应用问题，指定所要求的效率，变化处理器个数从 $\pmb { \hat { p } _ { 1 } }$ 到 $\pmb { \mathscr { p } } _ { i }$ ,按照图3.10流程调整W,就可画出一条曲线;变化不同的

$E$ ,就可画出一簇曲线。

$\textcircled{3}$ 根据上一步的结果，就可作出 $\overline { { L } } ( W , / )$ 与处理器个数变化关系表；由此表按照公式(3.29)就可计算出 $\Phi ( E , p , p ^ { \prime } )$ 之值；再由这些 $\Phi ( E , p , p ^ { \prime } )$ 就可构筑类似于表3.3的 $\Phi ( E , p , p ^ { \prime } )$ 上三角阵。文献[187]给出了这样的一个上三角阵，它是5000个元素的快排序算法，为了保持 $E = 0 . 2 5$ ,问题规模从在2个处理器上的 $W = 4 ~ 8 6 6$ 调整至32个处理器上的 $W = 9$ 753184,完整的上三角阵如表3.4所示，其中表项值越大，可扩放性越好。

![](images/bf76e40e262b6b7b14b5c7dbf49e9e718ab910f10e9faefebe882707891441b9.jpg)  
图3.10调整问题规模W的过程

表3.4 $\Phi ( 0 , 2 5 , \rho , \rho ^ { \prime } )$ 上三角阵  

<table><tr><td>处理器数</td><td>2</td><td>4</td><td>8</td><td>16</td><td>24</td><td>32</td></tr><tr><td>2</td><td>1.000</td><td>0.941 9</td><td>0.695 7</td><td>0.220 4</td><td>0.032 9</td><td>0.0090</td></tr><tr><td>4</td><td></td><td>1.000 0</td><td>0.667 7</td><td>0.2116</td><td>0.031 6</td><td>.0.008 6</td></tr><tr><td>8</td><td></td><td></td><td>1.000</td><td>0.316 9</td><td>0.047 3</td><td>0.012 9</td></tr><tr><td>16</td><td></td><td></td><td></td><td>1.0000</td><td>0.149 3</td><td>0.040 8</td></tr><tr><td>24</td><td></td><td></td><td></td><td></td><td>1.000 0</td><td>0.273 2</td></tr><tr><td>32</td><td></td><td></td><td></td><td></td><td></td><td>1.000 0</td></tr></table>

# 3.2.5有关可扩放性标准的讨论

以上三节分别介绍了三种典型的可扩放性度量标准：等效率、等速度和平均延迟。等效率度量标准是在保持效率 $E$ 不变的前提下，研究问题规模W如何随处理器个数 $\pmb { \mathscr { P } }$ 而变化；等速度度量标准是在保持平均速度不变的前提下，研究处理器数 $\pmb { \mathscr { P } }$ 增多时应该相应地增加多少工作量W；平均延迟度量标准则是在效率 $E$ 不变的前提下，用平均延迟的比值来标志随着处理器数 $\pmb { \hat { p } }$ 的增加需要增加的工作量 $\mathbf { \Delta } \mathbf { w }$ 。三种评判可扩放性的标准的基本出发点都是抓住了影响算法可扩放性的基本参数 $T _ { \circ }$ ,只是等效率标准是采用解析计算的方法得到 $T _ { \circ }$ ；等速度标准是将 $T _ { \mathfrak { o } }$ 隐含在所测量的执行时间中；而平均延迟标准则是保持效率为恒值时,通过调节W与 $\pmb { \mathscr { p } }$ 来测量并行和串行执行时间,最终通过平均延迟反映出$T _ { o }$ ,所以等速度与平均延迟标准都是辅之以测试手段而得到有关性能参数（如速度与时间等)来评判可扩放性的;而等效率标准是通过解析计算开销参数 $T _ { o }$ 来评判可扩放性的。平均速度 $\overline { { V } }$ 和平均延迟 $\overline { L }$ 两个物理量的引入,目的近乎一样： $\varPsi ( \phi , \phi ^ { \prime } ) = T / T ^ { \prime }$ 保持不变，意即 $T _ { 0 }$ 随 $\pmb { \hat { p } }$ 变化很小； $\pmb { \mathscr { P } } \left( E , \pmb { \mathscr { p } } , \pmb { \mathscr { p } } ^ { \prime } \right) = \overline { { L } } \sqrt { L } ^ { \prime }$ 保持不变,亦意即 $T _ { \circ }$ 随 $\pmb { \hat { p } }$ 变化甚小。

事实上,三种度量可扩放性的标准是彼此等效的,这可简单推导如下：

由于运行在 $\pmb { \hat { p } }$ 个处理器上的工作量为 $\pmb { W }$ 的程序串行执行时间为 $\pmb { W } \pmb { t } _ { \pmb { c } }$ ,其效率 $E = \frac { W t _ { \mathrm { c } } } { \phi T _ { \mathrm { p } } }$ ,而程序的平均速度 $\overline { { V } } = \frac { W } { \rho T _ { \mathrm { ~ p ~ } } }$ ，所以 $E = \overline { { V } } \cdot \mathbf { \sigma } _ { t _ { \circ } }$ ,其中 $t _ { \mathfrak { c } }$ 为常数。这表明等效率与等速度两种度量可扩放性的标准在物理意义上是一致的

由于平均速度V=W $\overline { { V } } = \frac { \overrightarrow { W } } { \vert \overrightarrow { P } / } , \thinspace \thinspace \thinspace \phi T = T _ { \circ } + \ T _ { \mathrm { s e q } }$ ，而 $\mathcal { T } _ { \circ } \mathbf { = } \overset { \cdot } { p _ { \mathbf { \theta } } } \widetilde { L } ( \textbf { \em W } , \mathbf { \phi } )$ 且 $T _ { \mathrm { s e q } } = \mathbf { W } t _ { \mathrm { c } }$ 所以

$$
\overline { { V } } = \frac { W } { \hat { p } T } = \frac { W } { T _ { \mathrm { o } } + T _ { \mathrm { s e q } } } = \frac { W } { \hat { p } \widetilde { L } \left( W , \mathbf { \nabla } \mathbf { , } p \right) + W t _ { \mathrm { c } } } = \frac { W / p } { \widetilde { L } \left( W , \mathbf { \nabla } \mathbf { , } p \right) + W t _ { \mathrm { c } } / p }
$$

由此可推导出

$$
\overline { { L } } ( \mathrm { ~ W ~ } , \mathbf { \phi } ) = \frac { W } { \rho } \left( \frac { 1 } { \overline { { \mathbf { V } } } } - \mathbf { \phi } _ { t _ { c } } \right)
$$

当 $\widehat { V }$ 保持不变时， $\frac { 1 } { \overline { { V } } } - t _ { c }$ 为常数，所以

$$
\frac { \overline { { L } } ( \boldsymbol { W } , \boldsymbol { \phi } ) } { \overline { { L } } ( \boldsymbol { W } ^ { \prime } , \boldsymbol { \phi } ^ { \prime } ) } = \frac { \boldsymbol { W } } { \dot { p } } \Big / \frac { \boldsymbol { W } ^ { \prime } } { \dot { p } ^ { \prime } } = \frac { \boldsymbol { \phi } ^ { \prime } \boldsymbol { W } } { \dot { p } \boldsymbol { W } ^ { \prime } }
$$

根据(3.24)式和(3.29)式，(3.30)式表明从等速度度量标准可以导出平均延迟度量标准,两者是完全一致的。

最后要说的是，既然等速度和平均延迟两个可扩放性评判标准都是立足于测量的办法,那么就要为此提供一套测试手段、工具、环境以搜集、测量、分析有关数据并显示可扩放性性能。

# \*3.3 基准测试程序

基准测试程序(Benchmark)用于测试和预测计算机系统的性能，揭示不同结构机器的长处和短处，为用户决定购买或使用哪种机器最适合他们的应用要求提供决策。基准测试程序试图提供一个客观、公正的评价机器性能的标准。但真正做到完全公正并非易事，要涉及到的因素很多，包括硬件、体系结构、编译优化、编程环境、测试条件、解题算法等。一组标准的测试程序要提供一组控制测试条件和步骤的规则说明,包括测试平台环境、输入数据、输出结果和性能指标等。

不同的基准测试程序，侧重目的也有所不同：有的测试CPU性能，有的测试文件服务器性能,有的测试输入／输出界面,有的则测试网络通信速度等。根据不同用途,测试程序可有专用和通用之分。目前国际上流行的通用测试程序可分为好几类:①综合型（如Dhrystone、Whetstone 等）;②核心型（如LivermoreFortran Kernels、NASA 之 NAS 等）; $\textcircled{3}$ 数学库（如 Linpack、FFT等）; $\textcircled{4}$ 应用型（如 SPEC、Perfect、Splash 等）； $\textcircled{5}$ 并行型（如 NAS 之 NPB、PARKBENCH等）。本节仅仅介绍一些常见测试程序,它们很多都可在Internet上公开查到：http：//www.netlib.org/Liblist.html。在这里你可查到 LINPACK、LAPACK、BLAS、BLACS、Livermore Loops、Dhrystone、Whetstone、NAS、SPEC、 $\sin$ 等包含源代码的基准测试程序。

# 3.3.1基本测试程序

Whetstone它是为比较不同的计算机的浮点性能而设计的综合型基准测试程序，最早用Algol-60写成，后用Fortran改写。这是从英国国立物理实验室1970年时常用的数值计算程序中取出的最频繁使用的有代表性的程序段。这些程序段语句被转换到称之为Whetstone虚拟计算机上的指令，因而得名Whetstone基准程序。此基准程序既包括整数运算，又包括浮点运算，涉及到数组下标索引、子程序调用、参数传递、条件转移和三角/超越函数等，使用系统完成的Kwhetstone/s数来度量。

测试程序可访问Netlib/benchmark/whetstone

Dhrystone它主要为测试整数与逻辑运算性能而设计的综合型基准测试程序,用Ada、C和Pascal 写成,是一种CPU密集(CPU-intensive)型测试程序,由很多整型语句与逻辑语句的小循环组成。它使用系统完成的KDhrystone/s数来度量（注意VAX11/780 的性能为1.7KDhrystone/s,而VAX11/780 通常定义为1个 MIPS 性能标准,一个MIPS代表每秒 $1 0 ^ { 6 }$ 指令）。

测试程序可访问Netlib/benchmark/dhrystone

人们对Whetstone和Dhrystone这两个综合型基准程序的批评是，它们不能预测用户程序性能,这些基准程序的主要缺点是对编译程序比较敏感。

SPEC SPEC 是 Standard Performance Evaluation Cooperation 的 首字母缩写,它是作为 NCGA(National Computer Graphics Association)的一个小组于 20世纪80 年代创立,这个小组的创始者来源于Hewlett-Packard、DEC、MIPS 和Sun Microsystems,他们拥有一组基准测试程序以评测新机器的性能。第一组基准程序叫作 SPEC89,包含10个程序;SPEC92扩充至20个程序,6个整数程序和14个浮点程序分别称为 SPECint92和 SPECfp92。最近 SPEC又发布了一些新的基准测试程序（如 SPEC95、SPEChpc96、SPECweb96等）。SPEC 原主要是测试CPU性能的，现在强调开发能反映真实应用(如实际负载等)的基准测试程序,并已推广至客户/服务器计算、商业应用、I/O子系统等。

SPEC基准测试程序使用的单位是所测试机器执行性能与VAX11/780执行性能之比值。

# 3.3.2数学库测试程序

LinPACK自20世纪70年代中期以来,国际上曾开发过一批基于Fortran语言的求解线性代数方程组的子程序，于1979 年正式发布了LinPACK包。因为线性代数方程组在各个领域中应用甚广，所以该软件包就很自然地成为测试各种机器性能的测试程序。LinPACK测试的基准是用全精度64位字长的子程序求解100 阶线性方程组的速度,测试的结果以Mflops(每秒百万次浮点运算）作单位给出。LinPACK的测试报告由J.Dongarra经常更新发布(通常每月发布一次）。LinPACK 是使用 BLASI(Basic Algebra Subprograms1）的第一个线性代数软件包。BLAS1执行通常意义下的标量－向量运算(如标量乘向量、向量加、向量内积等),主要为向量计算机而设计的，它用Fortran77写成，但有些计算机商也提供汇编语言的BLAS1版本。

LAPACK尽管LinPACK作为测试程序现在仍很有生命力,但作为实际求解线性代数问题的软件包已经落伍了。所以1992年推出了代替LinPACK及EisPACK(特征值软件包)的LAPACK,它使用了数值线性代数中最新、最精确的算法，同时采用了将大型矩阵分解成小块矩阵的方法从而可有效地使用存储器。LAPACK 是建立在 BLAS1、BLAS2 和 BLAS3 基础上的,其中 BLAS2 执行矩阵－向量运算,BLAS3 执行矩阵-矩阵运算。

ScaLAPACK ScaLAPACK是LAPACK 的增强版,主要为可扩放的、分布存储的并行计算机而设计的。ScaLAPACK支持稠密和带状矩阵上各类操作，诸如乘法、转置和分解等。在国际上,ScaLAPACK例程可以加人多个并行算法，并且可根据数据分布、问题规模和机器大小选择这些算法，然而用户却不必关心这些细节。

# 3.3.3并行测试程序

NAS Parallel Benchmark(NPB） 它是 1991 年美国 NAS(Numerical Aero-dynamic Simulation)项目所开发的并行测试程序,其目的是为了比较各种并行机性能,有时也简称为NPB(NAS Parallel Benchmark)并行测试程序,系由8个程序组成,测试范围从整数排序到复杂的数值计算。测试结果以单处理机的CrayY-MP/1为单位(Class A)或 Cray C90/1为单位(ClassB)作比较。

NPB由5个核心程序组成： $\textcircled{1}$ EP(Embarrassingly Parallel):用于计算 Gauss伪随机数，因为它几乎不要求处理器之间相互通信，所以很适合于并行计算，而所测得的结果往往可以作为一个特定并行系统浮点计算性能可能达到的上限；$\textcircled { 2 } \mathrm { M G } ( \mathrm { M u l t i G r i d } )$ ：用4个V循环多重网格算法求解三维波松方程的离散周期近似解； $\textcircled{3} \textcircled { C }$ (ConjugateGradient)：用于求解大型稀疏对称正定矩阵的最小特征值的近似值,它表征了非结构风格计算和非规整远程通信计算类问题；④FT(Fast Fourier Transformation)：用于求解基于FFT谱分析法的三维偏微分方程，它也要求远程通信； $\textcircled{5}$ IS(Integer Sort)：用于基于桶排序的二维大整数排序,它要求大量的全交换通信。另外还有计算流体力学中3个模拟程序：①LU(LowerUpper Triangular)：用于基于对称超松弛法求解块稀疏方程组; $\textcircled{2}$ SP(Scalar Pen-ta-Diagonal)：用于求解5对角线方程组； $\textcircled{3}$ BT(Block Tri-Diagonal):用于求解3对角块方程组。

有关 NAS 并行基准程序的 WWW home Page 地址为:http://www.nas.nasa. gov/NAS/NPB/software/npbsoftware. html

PARKBENCH PARKBENCH(PARallel Kernels and BENCHmarks）是在1992年超级计算会议上确定的项目。与会者认为并行测试的重点应放在可扩放、分布存储、消息传递的体系结构上。主要目标是确定并行机用户与厂商双方都能接受的内容丰富的一批并行测试程序及标准，并把结果公布于网上,以减少不必要的重复工作。

现在的基准程序系为分布存储的多计算机编写，使用Fortran77加上PVM或MPI;为共享存储结构的Fortran90 和HPF版本的基准程序正在开发中。目前,PARKBENCH包括4类：①底层基准程序：测试一些基本结构参数，诸如算术运算速度、高速缓存和存储器速度、通信启动时间和带宽以及同步开销等；②核心基准程序：涉及到广泛的经常使用的科学计算子程序，诸如矩阵运算（稠密矩阵乘法、转置、LU分解、QR分解，矩阵三对角化等）、FFT运算、求解PDE 和NPB核基准程序等；③密集应用基准程序：目前仅包括谱变换、浅水（Shallow-

Water)模拟和3个NPB模似应用程序； $\textcircled{4}$ HPF编译基准程序：测试HPF编译器性能，主要集中在显式并行HPF结构的并行实现上。

PARKBENCH是个正在研究的课题，测试程序的内容尚未完全定型。目前所包含的核心测试程序主要来自 NPB。

# 3.4 小结和导读

小结本章仅讨论了并行计算的加速比、可扩放性和基准测试程序等基本性能评测问题。评价并行系统(并行计算)的性能指标还有其它一些。对于评价计算速度而言,就有算法(或程序)的执行时间，这对某些实时应用是很关键的；处理机每秒执行的指令数 MIPS(Million Instructions Persecond）、每秒执行的浮点运算数 FlOPS(Floating Point Operations Per Second);峰值速度 $R _ { \mathrm { p e a k } }$ （通常以Mflops/Gflops/Tflops/Pflops表示）、可达最大持续速度 $R _ { \operatorname* { m a x } }$ 。对于评价系统效率而言,就有效率(Efficiency) $E = S / _ { \mathcal { P } }$ ；利用率(Utility) $U = R _ { \mathrm { m a x } } / R _ { \mathrm { p e a k } }$ ;吞吐率（Throughput)W(即每秒执行的程序数，或单位时间内所能处理的作业数）。对于评价通信系统而言,就有通信容量(Capacity)、通信带宽(Bandwidth)和通信延迟(Latency)等。

此外,所介绍的基准测试程序大都限于科学和工程计算方面,其实在联机事务处理、商业计算、数据库等方面也有不少有名的基准测试程序。例如，TPC(Transaction Processing Council)基准程序就很流行,目前 TPC-A和 TPC-B已在1995年6月废弃，而TPC-C(测试事务处理价格/性能比）、TPC-D(测试决策支持系统)和TPC-E(测试大型企业支持计算环境的能力)在商业应用中广泛使用。

导读Amdahl加速定律最早描述在[12]中;Gustafson定律描述在[85]中；Sun和Ni加速定律描述在[170]中等效率标准是由Kumar等提出[112]；等速度标准是由Sun等提出[171];平均延迟标准由Zhang等提出[187];有关并行算法的可扩放性分析，读者可参阅[192],在那里还描述了很多其它的可扩放评判标准。有关计算机性能评价，[66]是篇很好的综述;LinPACK的使用手册，见[61]；LAPACK的使用手册，见[14];有关NAS并行基准程序，请见Ames研究中心报告[22]。最后读者可按下述WWW主页地址,在Internet上查阅到很多基准测试程序,它们还会给出程序的源代码和测试的结果：http://www.netlib.org/liblist . html。

# 习 题

3.1试讨论公式(3.4)、(3.8)和(3.11)三者的物理意义和相互关系。

3.2两个 $N \times N$ 阶的矩阵相乘，时间复杂度为 $T _ { 1 } = C N ^ { 3 } { \bf s }$ ,其中 $c$ 为常数；在 $\pmb { n }$ 节点的并行机上并行矩阵乘法的时间为 $T _ { n } = ( C N ^ { 3 } / n + b N ^ { 2 } / \sqrt { \ n } ) \mathbf { s } .$ 其中 $\pmb { b }$ 是另一常数,第一项代表计算时间，第二项代表通信开销；

$\textcircled{1}$ 试求固定负载时的加速并讨论其结果；  
$\textcircled{2}$ 试求固定时间时的加速并讨论其结果；  
$\textcircled{3}$ 试求存储受限时的加速并讨论其结果。

3.3试讨论本文所讲的三种加速定律的使用场合和它们的相互关系。

3.4试解释图3.8的物理意义。

3.5根据表3.1中的数据,试复算表3.3所有表项之值。

3.6试综合比较等效率、等速度和平均延迟三种可扩放性度量标准的异同点。

3.7试证明等效率、等速度和平均延迟三种可扩放性质量标准的相互等效性。

i.8用一台 $4 0 ~ \mathrm { M H z }$ 的处理机执行标准测试程序,它含的混合指令数和相应所需的时钟周期数如下：

<table><tr><td>指令类型</td><td>指令数</td><td>时钟周期数</td></tr><tr><td>整数运算</td><td>45 000</td><td>1</td></tr><tr><td>数据传送</td><td>32 000</td><td>2</td></tr><tr><td>浮点</td><td>15 000</td><td>2</td></tr><tr><td>控制传送</td><td>8000</td><td>2</td></tr></table>

试求有效每条指令执行的周期数CPI和每秒执行的指令数 ${ \bf M I P S } _ { \circ }$ 提示：令 $\pmb { \tau }$ 为时钟周期 $\bf ( n s )$ ， $f { = } 1 / \tau$ 为时钟频率( $\mathbf { \nabla } [ \mathbf { M H } \mathbf { z } )$ ， $T$ 为程序执行时的CPU时间， $I _ { \mathrm { c } }$ 为指令条数，C为程序执行的总周期数，则有 $T = I _ { \mathrm { c } } \times \mathrm { C P I } \times \tau$ 和 $\mathrm { M I P S } = { \frac { I _ { \mathrm { c } } } { T \times 1 0 ^ { 6 } } } = { \frac { f } { \mathrm { C P I } \times 1 0 ^ { 6 } } } =$ $\frac { f \times I _ { \mathrm { c } } } { \mathrm { C } \times 1 0 ^ { 6 } } ]$

3.9假定在一台 $4 0 ~ \mathrm { M F }$ 的处理机上运行200000条指令的目标代码，程序主要由4种指令组成,根据程序跟踪实验结果，已知指令混合比和每种指令所需周期数如下：

<table><tr><td>指令类型</td><td>CPI</td><td>指令混合比</td></tr><tr><td>算术和逻辑</td><td>1</td><td>60%</td></tr><tr><td>高速缓存命令中的加载/存放</td><td>2</td><td>18%</td></tr><tr><td>转移</td><td>4</td><td>12%</td></tr><tr><td>高速缓存缺失的存储访问</td><td>8</td><td>10%</td></tr></table>

$\textcircled{1}$ 计算在单处理机上用上述跟踪这些数据运行程序的平均CPI;  
$\textcircled{2}$ 根据 $\textcircled{1}$ 所得CPI,计算相应的MIPS速率。

3.10试分析行主编号的 $\sqrt { \pmb { p } } \times \sqrt { \pmb { p } }$ 网孔上 $\pmb { n }$ 点FFT算法的可扩放性。假定通信建立时间为$\pmb { t _ { s } }$ ，跨步延迟为 $t _ { \mathfrak { n } }$ ,传送单位信包的时间为 $\pmb { t _ { \mathrm { b } } }$ ,单位计算时间为 $\pmb { t _ { c 0 } }$

$\textcircled{1}$ 试计算处理器 $\mathrm { P } _ { i }$ 的通信跨步数hops；

$\textcircled{2}$ 试计算总的通信延迟 $T _ { \circ }$ ；

$\textcircled{3}$ 试计算等效率函数 $\begin{array} { r } { \mathbf { W } = f _ { \mathrm { E } } ( \mathbf { \Sigma } _ { \pmb { \phi } } ) } \end{array}$ 并加以讨论。[提示：对照FFT与网孔连接拓朴，可以发现处理器间的通信仅发生在同一行或同一列,且最大的通信 $h o p s = \sqrt { \ p } \cdot 2 _ { \circ } ]$

# 第二篇 并行算法的设计

第四章 并行算法的设计基础第五章 并行算法的一般设计方法第六章 并行算法的基本设计技术第七章 并行算法的一般设计过程

这一篇主要研究如何设计并行算法,包括并行算法的一般设计方法(第五章),并行算法的基本设计技术(第六章)和并行算法的一般设计过程(第七章)。而任何并行算法的设计都是基于某一特定的并行计算模型的，所以在本篇的开始,首先介绍了设计并行算法常用的并行计算模型,包括PRAM模型、APRAM模型、BSP模型、 $\mathrm { l o g P }$ 模型和 $\mathrm { C } ^ { 3 }$ 模型等。至于并行算法的具体实现(它主要涉及到并行程序设计),将放在本书的第四篇中讲述。

本篇第五章,将介绍并行算法的三种常用设计方法,包括“并行化"法（直接将一个串行算法并行化)，“全新"法(根据问题的特性,从头开始设计一个新的并行算法)和"借用"法(借用已知某类问题的现有算法,求解另一类与之有内在相似性的问题)。第六章,从利用并行处理技术最朴素的思想出发,介绍了算法设计的划分技术;从求解问题的方法和策略出发,介绍了算法设计的分治技术；从针对问题的特性出发,介绍了设计并行算法的平衡树法和倍增法;最后还介绍了基于重叠思想的并行处理技术中广泛使用的流水线设计技术。第七章,从设计方法学的角度,介绍如何从问题描述开始,逐步设计并行算法的全过程,包括任务划分、通信分析、任务组合和处理器映射等四个过程。它是实际设计一个并行算法的自然过程,其中前两个过程着重算法并发性和可扩放性的开拓；后两个过程着重优化算法的执行时间和均衡处理器的负载。

# 第四章 并行算法的设计基础

任何并行算法的设计都是基于某一特定的并行计算模型，而并行计算模型是从各种具体的并行机中抽象出来的，它能在一定程度上反映出具体并行机的属性，又可使算法研究不再局限于某一种具体的并行机。并行计算模型一般可分为抽象计算模型和实用计算模型。本章主要研究同步PRAM模型，异步APRAM模型,大同步BSP模型,异步LogP模型和粗粒度 $C ^ { 3 }$ 模型。但在讨论这些计算模型之前,先要简要地介绍一下并行算法的基础知识,包括并行算法的定义、分类，并行算法的表达，并行算法的复杂性度量以及并行算法中的同步和通信问题等。

# \*4.1 并行算法的基础知识

# 4.1.1并行算法的定义和分类

定义4.1 算法是解题方法的精确描述，是一组有穷的规则，它们规定了解决某一特定类型问题的一系列运算。

定义4.2 并行算法是一些可同时执行的诸进程的集合，这些进程互相作用和协调动作从而达到给定问题的求解。

并行算法可从不同的角度分类成数值计算的和非数值计算的并行算法；同步的、异步的和分布式的并行算法;共享存储的和分布存储的并行算法;确定的和随机的并行算法等等。

定义4.3数值计算是指基于代数关系运算的一类诸如矩阵运算、多项式求值、求解线性方程组等数字计算问题。求解数值计算问题的算法称为数值算法（Numerical Algorithm）。

定义4.4非数值计算是指基于比较关系运算的一类诸如排序、选择、搜索、匹配等符号处理问题。求解非数值计算问题的算法称为非数值算法（Non-numerical Algorithm）。

定义4.5 同步算法(Synchronized Algorithm)是指算法的诸进程的执行必须相互等待的一类并行算法。

定义4.6 异步算法(Asynchronized Algorithm)是指算法的诸进程的执行不必相互等待的一类并行算法。

定义4.7 分布算法(Distributed Algorithm)是指由通信链路连接的多个场点(Site)或节点,协同完成问题求解的一类并行算法。

按照上述意义,在局网环境下进行的计算称为分布计算(Distributed Com-puting)。在 Internet 流行的今天,可把工作站机群 COW(Cluster of Worksta-tions)环境下进行的计算称为网络计算(Network Computing)。推而广之,有人把基于Internet 的计算则称为元计算(Metacomputing)。

定义4.8 确定算法(Deterministic Algorithm)是指算法的每一步都能明确地指明下一步应该如何行进的一种算法。

定义4.9 随机算法(Randomized Algorithm)是指算法的每一步,随机地从指定范围内选取若干参数,由其来确定算法的下一步走向的一种算法。

# 4.1.2并行算法的表达

描述一个算法,可以使用自然语言进行物理描述;也可使用某种程序设计语言进行形式化描述。语言的选用，应避免二义性,且力图直观、易懂而不苛求严格的语法格式。像描述串行算法所选用的语言一样,类-Algol、Pidgin-Algol、类-Pascal等语言均可选用。在这些语言中,允许使用任何类型的数学描述,通常也无数据类型的说明部分，但只要需要，任何数据类型都可引进。

在描述并行算法时,所有描述串行算法的语句及过程调用等均可使用，而只是为了表达并行性而引人几条并行语句：

par-do语句当算法的若干步要并行执行时,我们可使用“Do in paralel"语句,简记之为"par-do"进行描述：

其中"end for"也可代之以"odrap”。

for all语句当几个处理器同时执行相同的操作时,可以使用“forall"语句描述之：

for all $\mathbf { P } _ { i }$ , where $0 { \leqslant } i { \leqslant } k$ do

end for

注意，为了算法书写简洁,在意义明确的前提下,参数类型总是省去,同时语句括弧"begin...end"的使用也比较随便。

# 4.1.3并行算法的复杂性度量

复杂度的渐近表示对算法进行分析时，常使用上界（Upper Bound）、下界（Lower Bound)和紧致界(Tightly Bound)的概念,现分别定义如下：

定义4.10令 $f ( n )$ 和 ${ \pmb g } ( { \pmb n } )$ 是定义在自然数集合 $N$ 上的两个函数,如存在两个正常数 $c$ 和 $\pmb { n _ { 0 } }$ ,使得对于所有 $n \geqslant n _ { 0 }$ 均有 $f ( n ) { \leqslant } c g \left( n \right)$ ,则称 ${ \pmb g } ^ { \prime } ( { \pmb n } )$ 是$f ( n )$ 的一个上界,记作 $f ( n ) = O ( g ( n ) )$ 。

定义 4.11 $f ( n )$ 和 $\mathbf { \delta } _ { g } ( { \boldsymbol { \mathbf { \mathit { n } } } } )$ 定义如上,如存在两个正常数 $c$ 和 $\pmb { n _ { 0 } }$ ,使得对于所有 $n \geqslant n _ { 0 }$ 均有 $f ( n ) { \ggeq } c g \left( n \right)$ ，则称 ${ \pmb g } ( { \pmb n } )$ 是 $f ( n )$ 的一个下界，记作 $f ( n ) =$ $\Omega ( \boldsymbol { g } ( \boldsymbol { n } ) )$ 。

定义4.12 $f ( n )$ 和 ${ \pmb g } ( { \pmb n } )$ 定义如上,如存在正常数 $c _ { 1 } 、 c _ { 2 }$ 和 $\pmb { n _ { 0 } }$ ,使得对于所有 $n { \geqslant } n _ { 0 }$ 均有 $c _ { 1 } g ( n ) { \leqslant } f ( n ) { \leqslant } c _ { 2 } g ( n )$ ,则称 ${ \pmb g } ( { \pmb n } )$ 是 $\scriptstyle f ( n )$ 的一个紧致界，记作 $f ( n ) = \Theta ( g ( n ) )$ 。

![](images/42f14de528e17c4772beb36f1ee025c34b6dcc643afce5b8fb7af13b8af1b6dc.jpg)  
图4.1给出了上界、下界和紧致界的几何解释。  
图4.1上界(a)、下界(b)和紧致界(c)的几何解释

并行算法的复杂性度量在分析算法时,如果对算法的所有输入分析其平均性态时的复杂度则称之为期望复杂度(Expected Complexity),为此往往需要对输人的分布作某种假定,这在大多数情况下并非容易。所以感兴趣的是分析在某些输人时,使得算法的时、空复杂度呈现最坏情况下的算法复杂度,称之为最坏情况下的复杂度(Worst-Case Complexity）。

在分析并行算法时,通常要分析如下几个指标：

$\textcircled{1}$ 运行时间 $t ( n )$ ：运行时间就是算法运行在给定模型上求解问题所需的时间(它主要是输入规模n的函数),通常包含计算时间和通信时间,分别用计算时间步和选路时间步作单位。

$\textcircled{2}$ 处理器数 ${ \pmb { \hat { p } } } ( { \pmb { \hat { n } } } )$ ：它是求解给定问题所用的处理器数目,通常取 ${ \pmb { \phi } } ( { \pmb { n } } ) =$

$n ^ { 1 - \varepsilon } , 0 < \varepsilon < 1$ 是常见的。

$\textcircled{3}$ 并行算法的成本 $c ( n )$ ：它定义为并行算法的运行时间 $t ( n )$ 与其所需的处理器数 ${ \pmb { \mathscr { p } } } ^ { \prime } ( { \pmb { \mathscr { n } } } )$ 之乘积，即 $c ( \boldsymbol { n } ) = \boldsymbol { t } \left( \boldsymbol { n } \right) \cdot \boldsymbol { p } ( \boldsymbol { n } ) ,$

定义4.13如果求解一个问题的并行算法之成本,在数量级上等于最坏情况下串行求解此问题所需的执行步数，则称此并行算法是成本最优的。

$\textcircled{4}$ 总运算量 $\mathbf { \boldsymbol { W } } ( \boldsymbol { n } )$ ：即并行算法所完成的总的操作数量。此时我们并不关心也不必指明算法使用了多少台处理器。当给定了并行系统中的处理器数时，就可使用下述Brent 定理计算出相应的运行时间。

Brent定理令 $\mathbf { { \cal { W } } } ( n )$ 是某并行算法 $\pmb { A }$ 在运行时间 $T ( n )$ 内所执行的运算量,则 $A$ 使用 $\pmb { \mathscr { P } }$ 台处理器可在 $t ( n ) = O ( W ( n ) / p + T ( n ) )$ 时间内执行完毕。

$\textrm { \textbf { W } } ( \mathbf { \mu } _ { n } )$ 和 $c ( \pmb { n } )$ 密切相关。按照成本之定义和Brent定理，则有 $c \left( \varkappa \right) =$ $t ( n ) \cdot p = O ( \mathbf { \nabla } W ( n ) + p \cdot T ( n ) )$ 当 ${ \pmb { \phi } } = O ( { \pmb W } ( { \pmb n } ) / T ( { \pmb n } ) )$ 时， $\boldsymbol { W } ( n )$ 和 $c ( \pmb { n } )$ 两者是渐近一致的;而对于任意的 $\pmb { \hat { p } }$ ，则 $c ( n ) > W ( n )$ 。这说明一个算法在运行过程中，不一定都能充分地利用有效的处理器去工作。

# 4.1.4并行算法中的同步与通信

同步同步是在时间上强使各执行进程在某一点必须相互等待。在并行算法的各进程异步执行过程中,为了确保各处理器的正确工作顺序以及对共享可写数据的正确访问(互斥访问),程序员需在算法的适当点设置同步点。同步可用软件、硬件和固件的办法来实现。下面以MIMD-SM多处理器系统中 $\pmb { n }$ 个数的求和为例,说明如何用同步语句 $\mathbf { l o c k }$ 和unlock来确保对共享可写数据的互斥访问。假定系统中有p个处理器P,,Pp-1;输人数组A=(ao,,an-1)存放在共享存储器中;全局变量用于存放结果;局部变量L包含各处理器计算的子和;lock和unlock语句执行在临界区,加锁是个原子操作;在for循环中各进程异步地执行各语句,并结束在"endfor”。

# 算法4.1 共享存储多处理器上求和算法

输入： $A = \left( a _ { 0 } , \cdots , a _ { n - 1 } \right)$ ,处理器数 $\pmb { \mathscr { P } }$

输出： $S = \textstyle \sum a _ { i }$

# Begin

(1) $S = 0$   
(2） for all $\mathrm { P } _ { i }$ where $\scriptstyle 0 \leqslant i \leqslant j - 1$ do(2.1) $L = 0$ (2.2) for $j = i$ to $\pmb { n }$ step $\pmb { \mathscr { P } }$ do$L = L + a _ { j }$

end for(2.3) lock(S)$S = S + L$ (2.4） unlock（S)end for

End

通信通信是在空间上对各并发执行的进程施行数据交换。通信可使用通信原语来表达：在共享存储的多处理器中,可使用global read(X,Y)和globalwrite( $U , V )$ 来交换数据，前者将全局存储器中数据 $X$ 读人局部变量 $Y$ 中，后者将局部数据 $U$ 写人共享存储变量 $\boldsymbol { v }$ 中;在分布存储的多计算机中,可使用 send$( X , i )$ 和 receive( $\mathbf { \delta } _ { Y , j } )$ 来交换数据，前者是处理器发送数据 $\pmb { X }$ 给 $\mathbf { { P } } _ { i }$ ,后者是处理器从 $\mathrm { \bf P } _ { j }$ 接收数据 $\mathbf { r }$ 。下面以MIMD-DM多计算机系统中矩阵向量乘法为例说明之。假定分布式连接拓扑为环。矩阵A和向量X划分成p块;A=（A1，$\cdots , A _ { \phi } )$ 和 $\mathbf X = ( \ v x _ { 1 } , \cdots , \ v x _ { \phi } )$ ,其中 $\pmb { A } _ { i }$ 的大小为 ${ \pmb n } \times { \pmb r } , { \pmb x } _ { i }$ 的大小为 $r$ 。假定有 $\pmb { \hat { p } }$ $\leqslant n$ 个处理器, $r = n / \phi$ 为一整数。为了计算 $\mathbf { \mu } _ { \mathbf { y } } = \mathbf { \nabla } _ { \mathbf { A } } \mathbf { X }$ ，先由处理器 $_ i$ 计算 $\textstyle z _ { i } =$ $\mathbf { A } _ { i } x _ { i }$ $( 1 { \leqslant } i { \leqslant } p )$ ,再累加求和 $z _ { 1 } + \cdots + z _ { p } ,$ ，如果 $\mathbf { P } _ { i }$ 开始在其局存中保存 $\pmb { B } =$ $\mathbf { A } _ { i }$ 和 ${ \boldsymbol { \mathbf { \mathit { w } } } } = { \boldsymbol { \mathbf { \mathit { x } } } } _ { i }$ （则 $( 1 { \leqslant } i { \leqslant } p ) .$ ),则各处理器可局部计算乘积 $\pmb { { \cal B } } \mathbf { w } _ { i }$ ；然后采用在环中顺时针循环部分和的方法将这些向量累加起来;最终输出向量保存在P中。对于每个处理器都执行如下算法：

# 算法4.2 分布存储多计算机上矩阵向量乘算法

输入：处理器数 $\pmb { \phi }$ ,第 $_ i$ 个大小为 $\pmb { n } \times \pmb { r }$ 的子矩阵 $B = A \left( 1 \colon n , \left( i - 1 \right) r + 1 \right.$ $: i r )$ ,其中 $\gamma = { \mathfrak { n } } / { \mathfrak { p } }$ ；第 $_ i$ 个大小为 $\boldsymbol { r }$ 的子向量 ${ \pmb w } = x \big ( \big ( i - 1 \big ) r + 1$ ：$_ { i r }$ ）。

输出： $\mathbf { P } _ { i }$ 计算 $\mathbf { y } = \pmb { A } _ { 1 } x _ { 1 } + \cdots + \pmb { A } _ { i } x _ { i }$ ,并向右传送此结果;算法结束时， ${ \bf P } _ { 1 }$ 保存乘积 $\pmb { A } \pmb { X }$ 。

# Begin

(1） Compute $\boldsymbol { z } = \boldsymbol { B } \boldsymbol { w }$   
(2) if $i = 1$ then $y _ { i } = 0$ else receive $( y , l e f t )$ endif   
(3) $y = y + z$   
(4） send $( y , r i g h t )$   
(5) if $i = 1$ then receive $( y , l e f t )$ endif

End

# 4.2 并行计算模型

所谓计算模型实际上就是硬件和软件之间的一种桥梁，使用它能够设计分析算法，在其上高级语言能被有效地编译且能够用硬件来实现。在串行计算时，冯·诺依曼机就是一个理想的串行计算模型,在此模型上硬件设计者可设计多种多样的冯·诺依曼机而无须虑及被执行的软件；而软件工程师能够编写各种可在此模型上有效执行的程序而无须考虑所使用的硬件。但在并行计算时,尚未有一个类似于冯·诺依曼机的真正通用的并行计算模型。现在流行的计算模型要么过于简单、抽象(如PRAM);要么过于专用(如互连网络模型和VLSI计算模型)。因而急需发展一种更为实用、能够较真实反映现代并行机性能的并行计算模型。本节先简要讨论一下PRAM模型；然后分别介绍异步PRAM模型、BSP模型、logP模型和 ${ \bf C } ^ { 3 }$ 模型；最后对 BSP和logP进行了评注。

# 4.2.1 PRAM模型

PRAM模型描述 PRAM(Parallel Random Access Machine)模型,即并行随机存取机器,也称之为共享存储的 SIMD模型,是一种抽象的并行计算模型。在这种模型中，假定存在着一个容量无限大的共享存储器;有有限或无限个功能相同的处理器,且其均具有简单的算术运算和逻辑判断功能;在任何时刻各处理器均可通过共享存储单元相互交换数据。根据处理器对共享存储单元同时读、同时写的限制,PRAM模型又可分为： $\textcircled{1}$ 不允许同时读和同时写（Exclusive-Readand Exclusive-Write)的 PRAM模型,简记之为PRAM-EREW; $\textcircled{2}$ 允许同时读但不允许同时写(Concurrent-Read and Exclusive-Write)的 PRAM模型,简记之为PRAM-CREW。③允许同时读和同时写（Concurrent-Read and Concurrent-Write)的PRAM模型,简记之为PRAM-CRCW。显然,允许同时写是不现实的，于是又对PRAM-CRCW模型作了进一步的约定：①只允许所有的处理器同时写相同的数,此时称为公共(Common)的PRAM-CRCW,简记之为CPRAM-CR-CW;②只允许最优先的处理器先写，此时称为优先(Priority)的PRAM-CRCW，简记之为PPRAM-CRCW;③允许任意处理器自由写，此时称为任意(Arbitrary）的PRAM-CRCW,简记之为APRAM-CRCW。上述模型中,PRAM-EREW是最弱的计算模型,而PRAM-CRCW是最强的计算模型。令Tm表示某一并行算法在并行计算模型 $\mathbf { M }$ 上的运行时间,则

$$
T _ { \mathrm { E R E W } } { \geq } T _ { \mathrm { C R E W } } { \geq } T _ { \mathrm { C R C W } }
$$

$$
T _ { \mathrm { E R E W } } = O ( \ T _ { \mathrm { C R E W } } \cdot \log p ) = O ( \ T _ { \mathrm { C R C W } } \cdot \log p )
$$

其中, $\pmb { \mathscr { P } }$ 为处理器的数目。（4.2)式的含义是,一个具有时间复杂度为TcREw或TcRcw的算法,可在PRAM-EREW模型上花费 $\log p$ 倍时间模拟实现之。

PRAM模型优点著名的PRAM模型有很多优点：它特别适合于并行算法的表达、分析和比较;使用简单,很多诸如处理器间通信、存储管理和进程同步等并行机的低级细节均隐含于模型中;易于设计算法和稍加修改便可运行在不同的并行机上;且有可能在PRAM模型中加人一些诸如同步和通信等需要考虑的问题。

PRAM模型缺点PRAM是一个同步模型,这就意味着所有的指令均按锁步方式操作，用户虽感觉不到同步的存在,但它的确是很费时的;共享单一存储器的假定,显然不适合于分布存储的异步的MIMD机器;假定每个处理器均可在单位时间内访问任何存储单元而略去存取竞争和有限带宽等是不现实的。

PRAM模型推广随着人们对PRAM的理解深化,在使用它的过程中也对其做了若干推广,主要的有存储竞争模型,它将存储器分成一些模块,每个模块一次均可处理一个访问，从而可在模块级处理存储器的竞争;延迟模型,它考虑了信息的产生和能够使用之间的通信延迟；局部PRAM模型,此模型考虑到了通信带宽，它假定每个处理器均有无限的局存,而访问全局存储器是较昂贵的；分层存储模型,它将存储器视为分层的存储模块,每个模块由其大小和传送时间表征,多处理机由模块树表示,叶为处理器;异步PRAM模型,它是下一节我们要专门讨论的模型。

尽管PRAM模型是很不实际的并行计算模型,但在目前算法界仍被广泛使用,且被普遍地接受下来,特别是算法理论研究者非常喜欢它。

# 4.2.2异步 PRAM模型

模型特点 分相(Phase)PRAM模型是一个异步的 PRAM模型,简记之为APRAM,系由 $\pmb { \mathscr { P } }$ 个处理器组成，其特点是每个处理器都有其局存、局部时钟和局部程序;处理器间的通信经过共享全局存储器;无全局时钟,各处理器异步地独立执行各自的指令;处理器任何时间依赖关系需明确地在各处理器的程序中加人同步(路)障(Synchronization Barrier);一条指令可在非确定(无界)但有限的时间内完成。

APRAM模型中的指令类型APRAM模型中有四类指令： $\textcircled{1}$ 全局读：将全局存储单元中的内容读人局存单元中；②局部操作：对局存中的数执行操作，其结果存人局存中；③全局写：将局存单元中的内容写人全局存储单元中;④同步：同步是计算中的一个逻辑点,在该点各处理器均需等待别的处理器到达后才能继续执行其局部程序。

APRAM模型中的计算在APRAM中,计算系由一系列用同步障分开的全局相所组成。如图4.2所示，在各全局相内，每个处理器异步地运行其局部程序；每个局部程序中的最后一条指令是一条同步障指令；各处理器均可异步地读取和写入全局存储器,但在同一相内不允许两个处理器访问同一单元。正是因为不同的处理器访问存储单元总是由一同步障所分开,所以指令完成的时间上的差异并不影响整个计算。

![](images/4b9a8dbafaba1acdbd63a4a145e77b47fce1d031490f6d42f687364ce5dac0f1.jpg)  
图4.2APRAM中的异步计算, $\star$ 表示局部操作

APRAM模型中的时间计算使用 APRAM模型计算算法的时间复杂度时,假定局部操作取单位时间；全局读／写时间为d,它定量化了通信延迟,代表读／写全局存储器的平均时间,d随机器中的处理器增加而增加;同步障的时间为 $B$ ,它是处理器数 $\pmb { \mathscr { P } }$ 的非降函数 $B = B ( { \boldsymbol { \mathbf { \rho } } } _ { \beta } )$ 。在APRAM中假定上述参数服从如下关系：

$$
2 { \leqslant } d { \leqslant } B { \leqslant } p
$$

同时 $B { \big ( } \phi { \big ) } \in O { \big ( } d \log \phi { \big ) }$ 或 $B ( \phi ) \in O ( d \log \phi / \log d )$ 。令 $t _ { p \mathbf { h } }$ 为全局相内各处理器指令执行时间中最长者，则整个程序运行时间T为各相的时间之和加上B乘以同步障次数,即

总之，APRAM模型比起PRAM来更接近于实际的并行机;且保留了PRAM编程的简捷性;由于使用了同步障,所以不管各处理器遭到的延迟多长，程序必定是正确的;且因为APRAM模型中的成本参数是定量化的,所以算法的分析也是不难的。

# 4.2.3BSP模型

BSP模型的基本参数 BSP(Bulk Synchronous Parallel)模型,字面的含义是“大"同步模型(相应地,APRAM模型也叫作"轻量"同步模型),早期最简单的版本叫作XPRAM模型,它是作为计算机语言和体系结构之间的桥梁,并以下述三个参数描述的分布存储的多计算机模型： $\textcircled{1}$ 处理器/存储器模块（下文也简称为处理器）； $\textcircled{2}$ 施行处理器/存储器模块对之间点到点传递消息的选路器； $\textcircled{3}$ 执行以时间间隔 $L$ 为周期的所谓路障同步器。所以BSP模型将并行机的特性抽象为三个定量参数 $\phi , g , L$ ,分别对应于处理器数、选路器吞吐率(亦称带宽因子）、全局同步之间的时间间隔。

BSP 模型中的计算在BSP模型中,计算系由一系列用全局同步分开的周期为 $L$ 的超级步(Superstep)所组成。在各超级步中,每个处理器均执行局部计算,并通过选路器接收和发送消息;然后作一全局检查,以确定该超级步是否已由所有的处理器完成：若是,则前进到下一超级步,否则下一个 $L$ 周期被分配给未曾完成的超级步。

BSP模型的性质和特点 BSP模型是个分布存储的MIMD计算模型,其特点是： $\textcircled{1}$ 它将处理器和选路器分开，强调了计算任务和通信任务的分开，而选路器仅施行点到点的消息传递，不提供组合、复制或广播等功能，这样做既掩盖了具体的互连网络拓扑，又简化了通信协议； $\textcircled{2}$ 采用路障方式的以硬件实现的全局同步是在可控的粗粒度级,从而提供了执行紧耦合同步式并行算法的有效方式，而程序员并无过分的负担； $\textcircled{3}$ 在分析BSP模型的性能时，假定局部操作可在一个时间步内完成,而在每一超级步中,一个处理器至多发送或接收 $h$ 条消息（称为h-relation)。假定 $\pmb { \mathscr { s } }$ 是传输建立时间,所以传送 $h$ 条消息的时间为 $g h + s$ ,如果 $_ { g h } \geqslant 2 s$ ,则 $L$ 至少应 $\geqslant g h$ 。很清楚,硬件可将 $L$ 设置尽量小（例如使用流水线或宽的通信带宽使 $\pmb { g }$ 尽量小),而软件可以设置 $L$ 之上限(因为 $L$ 愈大，并行粒度愈大)。在实际使用中， $\pmb { g }$ 可定义为每秒处理器所能完成的局部计算数目与每秒选路器所能传输的数据量之比。如果能合适地平衡计算和通信，则BSP模型在可编程性方面具有主要的优点,而直接在BSP模型上执行算法(不是自动地编译它们),此优点将随着 $\pmb { g }$ 的增加而更加明显； $\textcircled{4}$ 为PRAM模型所设计的算法,均可采用在每个BSP处理器上模拟一些PRAM处理器的方法实现之。理论分析证明,这种模拟在常数因子范围内是最佳的，只要并行宽松度（ParallelSlackness),即每个BSP处理器所能模拟的PRAM处理器的数目足够大。在并发情况下,多个处理器同时访问分布式的存储器会引起一些问题,但使用散列方法可使程序均匀地访问分布式存储器。在PRAM-EREW情况下，如果所选用的散列函数足够有效，则L至少是对数的,于是模拟可达最佳,这是因为我们欲在p个物理处理器的BSP模型上,模拟u≥plogp个虚拟处理器,可将u/p≥$\log \phi$ 个虚拟处理器分配给每个物理处理器。在一个超级步内， $_ { v }$ 次存取请求可均匀摊开，每个处理器大约u/p次，因此机器执行本次超级步的最佳时间为

$O ( v / p )$ ,且概率是高的。同样,在 $_ { v }$ 个处理器的PRAM-CRCW模型中,能够在$\boldsymbol { \mathscr { P } }$ 个处理器（如果 $v = \boldsymbol { \phi } ^ { 1 + \epsilon } , \epsilon > 0 )$ ,和 $L \geqslant \log \phi$ 的 BSP模型上用 $O ( v / \phi )$ 的时间也可达到最佳模拟。

对 BSP模型的评注 $\textcircled{1}$ 在并行计算时，Valiant试图也为软件和硬件之间架起一座类似于冯·诺依曼机的桥梁，他论证了BSP模型可以起到这样的作用,正是因为如此,BSP模型也常叫作桥模型; $\textcircled{2}$ 一般而言，分布存储的MIMD模型编程能力均较差,但在 BSP模型中,如果 计算和通信可合适的平衡(例如 $g = 1 \AA$ ），则它在可编程方面呈现出主要的优点； $\textcircled{3}$ 在 BSP模型上,曾直接实现了一些重要的算法(如矩阵乘、并行前缀运算、FFT和排序等),它们均避免了自动存储管理的额外开销； $\textcircled{4} \textcircled { 1 } \textcircled { < } \textcircled { 2 }$ 模型可有效地在超立方网络和光交叉开关互连技术上实现,呈现出该模型与特定的工艺技术无关,只要选路器有一定的通信吞吐率； $\textcircled{5}$ 在 BSP模型中,超级步的长度必须能充分地适应任意的h-relation,这一点是人们最不喜欢的; $\textcircled{6}$ 在BSP模型中,在超级步开始发送的消息,即使网络延迟时间比超级步的长度短,它也只能在下一个超级步才能使用； $\textcircled{7}$ BSP模型中的全局路障同步假定是用特殊的硬件支持的,这在很多并行机中可能没有相应的现成的硬件机构； $\textcircled{8}$ Valiant所提出的编程模拟环境，在算法模拟时的常数可能不是很小的,如果考虑到进程间的切换(可能不仅要设置寄存器，而且可能还有部分高速缓存)则此常数可能很大。

# 4.2.4 logP模型

logP模型提出的背景 $\textcircled{1}$ 根据技术发展的趋势：20世纪90年代末和未来的并行机发展的主流之一是巨量并行机,即MPC（MassivelyParallel Comput-ers),它系由成千个功能强大的处理器/存储器节点,通过受限带宽的和可观延迟的互连网络所构成。所以我们建立并行计算模型应充分考虑此情况，这样基于此模型的并行算法才能在现有和未来的并行机上有效运行；②根据已有的编程经验：现有的共享存储、消息传递和数据并行等编程风范都很流行，但尚无一个公认的和占支配地位的编程方式，因此应寻求一种与上述任一特定编程风格无关的计算模型;③根据现有的理论模型：共享存储PRAM模型和互连网络的SIMD模型作为开发并行算法还不够合适,因为它们既未包含分布存储的情况,也未考虑通信同步等实际因素，从而也不能精确地反映运行在真实并行机上的算法的性态。所以在此背景下，一个以MPC为背景的新计算模型，即logP 模型,便由D.Culler等人提出了。

logP模型的参数logP模型是一种分布存储的、点到点通信的多处理机模型,其中通信网络由一组参数来描述，但它并不涉及到具体的网络结构,也不假定算法一定要用显式的消息传递操作进行描述。很凑巧,logP恰好是以下几个定量参数的拼写，其中，①L(Latency)表示在网络中消息从源到目的地所遭到的延退； $\textcircled { 2 } \textcircled { \scriptsize { \times } } ( \textcircled { \scriptsize { \times } } \mathbf { v e r h e a d } )$ 表示处理器发送或接收一条消息所需的额外开销（包含操作系统核心开销和网络软件开销),在此期间内它不能进行其它的操作； $\textcircled{3} \textcircled { 8 }$ $\left( \mathsf { G a p } \right)$ 表示处理器可连续进行消息发送或接收的最小时间间隔； $\textcircled{4} \textcircled{4}$ (Processor)表示处理器/存储器模块数。很显然， $\pmb { g }$ 的倒数相应于处理器的通信带宽；而 $L$ 和 $\pmb { g }$ 反映了通信网络的容量。 $L , o$ 和 $\pmb { g }$ 都可以表示成处理器周期（假定一个周期完成一次局部操作，并定义为一个时间单位)的整倍数。

对logP模型的论证 $\textcircled { 1 } \log \tt { P }$ 模型充分揭示了分布存储并行机的性能瓶颈，用 $L \setminus o$ 和 $\pmb { g }$ 三个参数刻画了通信网络的特性，但却屏蔽了网络拓扑、选路算法和通信协议等具体细节。本质上讲,通信网络是一个启动率为 $\pmb { g }$ 、延迟为 $L$ 、端点处理器开销各为零的流水线部件；网络的容量假定是有限的，在任何时刻至多只能有 $L / g$ 条消息从一个处理器传到另一个处理器，且任何消息均可在有限但非确定的时间内到达目的地;在网络容限范围内,点到点的传输一条消息的时间为 $2 \cdot \bullet + L$ ； $\textcircled{2}$ 尽管拓扑结构对网络性能影响很大，但 $\scriptstyle \log \mathbf { P }$ 模型在计算通信时间时却屏蔽了这一点,这是因为通过上千个节点的网络(如超立方、蝶形网、网孔、胖树等)的平均距离分析,发现它们的差别仅为2倍,而这种差别对整个消息传输时间的影响是很小的;③对于一个具体的并行机，由通道带宽为w、经过H个跨步(Hops)的网络传送一个M位的消息所花的时间为T(M,H)=Tsend+「M/w]+H·r+Trev,其中Tsend为发送开销，即第一位数据被送上网络之前处理器为网络接口准备数据的时间；Trev为接收开销，即从最后一位数据到达直到接收处理器用此数据进行处理的时间；M/w1为将消息的最后一位送到网上所需的时间;H·r是最后一位数据通过网络达到目的节点的时间（r为中继节点的时延）。对于logP而言,合理的参数选取是:o=（Tsend+Trev)/2,L=H·r+「M/w],g=「M/b7(b为处理器对剖宽度)。此处,通过对具有上千个处理器的典型并行机的测试和分析，发现在网络空载或轻载时·T(M,H)中起主导作用的是 $T _ { \mathrm { s e n d } }$ 和 $T _ { r e v }$ (这就意味着通信接口部件对系统性能影响更大),而它们对网络和结构却不敏感。但是如果网络重载时就会出现竞争资源的现象，从而等待时间将迅速增加，正是因为如此，logP模型对网络的容量加以了限制；④在logP模型中，假定每个节点只有一个处理器，它既用于计算又负责接收和发送消息，所以为了发送或接收一个字处理器均要付出开销o。对于长的消息，某些并行机提供了专门的硬件支持，但这样作充其量也只不过能使每个节点的性能提高一倍。所以在logP模型中对长消息不作特别处理;③尽管在某些并行机中，使用了特殊的硬件支持数据的广播、前缀运算或全局同步等，但logP模型中必须通过隐含地发送消息来执行这些操作,因为用硬件完成这些操作，其功能是受到了限制的（例如它们可能只对整数有效而对浮点数则不行)。此外，对于logP模型设计算法时最普通的全局操作是路障，它是一种由硬件支持的原语操作。用硬件支持这一操作比对全局数据进行操作要简单，而且路障作为原语的优点是假定处理器以同步方式退出路障可简化算法的分析； $\textcircled{6}$ 在 $\scriptstyle \log \mathbf { P }$ 模型中使用了无竞争的通信模式，因为用这种模式重复传输时可以利用整个带宽,反之其它的通信模式往往依赖于选路算法、路由缓冲器数和互连拓扑结构，而 $\mathrm { l o g P }$ 模型将网络的内部结构抽象成了几个性能参数,它就不能区别互连结构的优劣了。logP模型能够反映各种通信模式的一种可能的推广方式是提供多种 $\pmb { g }$ ,对于特定的通信模式可以采用适当的 $\pmb { g }$ 进行算法分析； $\textcircled{7}$ 在 $\scriptstyle \log \mathbf { P }$ 模型中提倡使用多线程(Multithreading)技术来屏蔽网络延迟(但此技术受通信带宽和进程切换开销的限制）。

对logP模型的评注 $\textcircled { 1 } \log \tt { P }$ 模型将现代和将来的并行机的特性进行了精确的综合，以少量的参数 $L , o , g$ 和 $\pmb { \hat { p } }$ 刻画了并行机的主要瓶颈。这个模型的详尽程度足以反映了并行算法设计时的主要实际问题，而其简捷性也足以支持详细的算法分析。对于那些非平易的算法，用这种比较复杂的模型（显然比PRAM复杂得多)来分析时仍是可操作的，因为这些参数的重要程度在不同的环境下是不同的，往往可以略去其中的一个或几个参数而使模型更简单一些； $\textcircled{2}$ logP 模型无须说明编程风格或通信协议,它可以等同地用于共享存储、消息传递和数据并行等各种风范； $\textcircled { 3 } \log \textcircled { 2 }$ 模型的可用性已由诸如播送、求和、FFT、LU分解、排序、图的连通性等算法得以证实，并且它们都已在CM-5机器上加以实现； $\textcircled{4}$ 事实上,如果使 $\scriptstyle \log \mathbf { P }$ 模型中的参数 $g = 0 , L = 0$ 和 ${ \pmb o } = { \bf 0 }$ ，则 $\scriptstyle \log \mathbf { P }$ 就等同于PRAM;同时logP模型也是BSP模型的改进和细化：例如在一个超级步中并非要所有的处理器都发送或接收h条那么多的消息；在一个超级步中消息一旦到达处理器就可立即使用它，而不必像BSP那样一定要等到下一个超级步；logP模型全部采用消息同步而不像BSP那样要用专门的硬件支持。总之，尽管logP模型的可用性还有待于用大量的算法实例进一步证实，但它毕竟打开了研究模型的新途径，它不仅为算法设计者提供了设计适合于近代并行机的巨量并行算法的手段，而且对设计并行机体系结构也提供了指导性意见。

# 4.2.5 $\mathbf { C } ^ { 3 }$ 模型

动机与背景 ①C³（Computation,Communication,Congestion）模型是一个与体系结构无关的粗粒度的并行计算模型，它同时也考虑了由工作站或高档微机组成的高性能可扩放的并行机群系统为目标，旨在能反映计算复杂度、通信模式和通信期间潜在的拥挤诸因素对粗粒度网络算法的影响;②在粗粒度机器上，并行算法的性能非常敏感于通信模式,而前述的BSP和logP模型都只采用点到点的消息传递来进行通信，复杂的通信操作系由编程实现，这无疑加重了程序员的负担。而 $\mathrm { C } ^ { 3 }$ 模型强调用公用的通信操作来开发粗粒度的并行算法； $\textcircled{3}$ 以前所提出的模型,均未反映通信操作中所引起的潜在拥挤，而 ${ \bf C } ^ { 3 }$ 模型却考虑到了网络链路拥挤和处理器拥挤对并行算法性能的影响。

$C ^ { 3 }$ 模型中的计算在 $C ^ { 3 }$ 模型中，和BSP与 $\scriptstyle \log \bar { P }$ 相似,计算可划分为一系列超级步；同步出现在两超级步之间且用路障同步机构实现之；在每个超级步内施行局部计算继之以发送/接收消息；一个超级步的时间由所完成的计算单位数和通信单位数来度量，其中计算单位数取决于所作的局部计算量，而通信单位数取决于处理器所发送的数据量、处理器所接收的数据量、消息的传输延迟和处理器间超容限通信所引起的拥挤；在分析算法的时间复杂度时,必须累加每一个超级步中的计算和通信单位数,所有超级步中的总计算单位数与通信单位数之比可以指示算法的性态。

$\mathbf { C } ^ { 3 }$ 模型的参数及其计算首先定义用于确定计算和通信单位数的并行系统参数：令 $\pmb { \phi }$ 代表处理器数， $\iota$ 表示信包的长度， $\pmb { s }$ 表示执行发送的建立时间， $\pmb { h }$ 表示延迟(用两个处理器间平均距离表示，即 $h = \sum _ { 1 \leqslant i , j \leqslant p } d _ { i j } / \phi ^ { 2 }$ ,其中 $d _ { i j }$ 是两个处理器间的最小距离)。表4.1给出了常用互连结构的平均距离 $\boldsymbol { h }$ （也同时给出了对剖宽度 $^ { b }$ ）。

$\textcircled{1}$ 计算单位数：假定在一个超级步中,处理器 $\mathbf { P } _ { i }$ 访问 $t _ { i }$ 个字节,则超级步的计算单位数为： $\operatorname* { m a x } _ { 1 \leqslant i \leqslant p } \lceil t _ { i } / l \rceil _ { \circ }$

$\textcircled{2}$ 无拥挤时的通信单位数：通信单位数与不同的选路方案和不同的发送、接收原语有关。最常用的选路方案有存储转发和虫蚀两种；大多数机器都支持阻塞和非阻塞的发送和接收原语。施行存储转发选路时一个处理器可存储 $\pmb { k }$ 条信包，而虫蚀选路时一条信包存储于 $k$ 个(或更多)处理器中。所谓阻塞发送系指一个源处理器从开始发送

表4.1机器的平均距离和对剖宽度一览表  

<table><tr><td rowspan=1 colspan=1>互连结构</td><td rowspan=1 colspan=1>平均距离h</td><td rowspan=1 colspan=1>对剖宽度b</td></tr><tr><td rowspan=1 colspan=1>一维阵列</td><td rowspan=1 colspan=1>p/2</td><td rowspan=1 colspan=1>1</td></tr><tr><td rowspan=1 colspan=1>二叉树</td><td rowspan=1 colspan=1>O(logp)</td><td rowspan=1 colspan=1>1</td></tr><tr><td rowspan=1 colspan=1>二维网孔</td><td rowspan=1 colspan=1>2/3p</td><td rowspan=1 colspan=1>VP</td></tr><tr><td rowspan=1 colspan=1>三维网孔</td><td rowspan=1 colspan=1>p1</td><td rowspan=1 colspan=1>p2</td></tr><tr><td rowspan=1 colspan=1>蝶形网</td><td rowspan=1 colspan=1>O(logp)</td><td rowspan=1 colspan=1>0(p/logp)</td></tr><tr><td rowspan=1 colspan=1>洗牌交换</td><td rowspan=1 colspan=1>O(logp)</td><td rowspan=1 colspan=1>0（p/logp)</td></tr><tr><td rowspan=1 colspan=1>超立方</td><td rowspan=1 colspan=1>(logp)/2</td><td rowspan=1 colspan=1>p/2</td></tr><tr><td rowspan=1 colspan=1>胖树</td><td rowspan=1 colspan=1>4log4p-2/3</td><td rowspan=1 colspan=1>0(p)</td></tr><tr><td rowspan=1 colspan=1>完全图</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0(p²/4)</td></tr></table>

一条消息，直至它被目的处理器收到后源处理器的发送操作才终止；而非阻塞发送时源处理器在填满发送缓冲器后只要等到消息被取走即可。在无拥挤时处理器 $\mathbf { { P _ { i } } }$ 发送 $L _ { i , j }$ 个字节给 $\mathbf { P } _ { j }$ 时的发送和接收时间如表4.2所示。

在一个超级步中,令 $\pmb { n } _ { \mathrm { s } } ( i )$ 是 $\mathbf { P } _ { i }$ 所发送的消息数， ${ \pmb n } _ { \mathbf { r } } ( i )$ 是 $\mathbf { P } _ { i }$ 所接收的消息数， $S _ { i }$ 是处理器 $\mathbf { P } _ { i }$ 在无拥挤环境中发送 $\pmb { n } _ { \mathrm { s } } ( \pmb { i } )$ 条消息的总时间， $R _ { i }$ 为总接收时间，则无拥挤时的 $S _ { i }$ 和 $R _ { i }$ 如表4.3所示。所以一个超级步内无拥挤时的通信单位数 $= \operatorname* { m a x } _ { 1 \leqslant i \leqslant p } \left\{ \ S _ { i } + R _ { i } \right\}$

表4.2 $\mathbf { P } _ { i }$ 发送 $\mathbb { L } _ { i , j }$ 个字节给 $\mathbf { p } _ { j }$ 时发送和接收时间一览表  

<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2>非阻塞发送和接收</td><td rowspan=1 colspan=2>阻塞发送和非阻塞接收</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>发送时间si,j</td><td rowspan=1 colspan=1>接收时间rj</td><td rowspan=1 colspan=1>发送时间sij</td><td rowspan=1 colspan=1>接收时间ri,j</td></tr><tr><td rowspan=1 colspan=1>存储转发</td><td rowspan=1 colspan=1>ii*</td><td rowspan=1 colspan=1>i,i</td><td rowspan=1 colspan=1>2(s + h)+  Lii *h</td><td rowspan=1 colspan=1>s+h+            *h</td></tr><tr><td rowspan=1 colspan=1>虫蚀</td><td rowspan=1 colspan=1>s+            × h</td><td rowspan=1 colspan=1>L</td><td rowspan=1 colspan=1>2(s +h)+ Lii +h1</td><td rowspan=1 colspan=1>s+h+  Lii +h</td></tr></table>

表4.3一个超级步中的处理器发送和接收时间一览表  

<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2>非阻塞发送和接收</td><td rowspan=1 colspan=2>阻塞发送和非阻塞接收</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>发送时间S</td><td rowspan=1 colspan=1>接收时间R</td><td rowspan=1 colspan=1>发送时间S</td><td rowspan=1 colspan=1>接收时间R</td></tr><tr><td rowspan=1 colspan=1>存储转发</td><td rowspan=1 colspan=1>mLis*n(i)+1*h+M L1</td><td rowspan=1 colspan=1>新[]</td><td rowspan=1 colspan=1>2(s+h)*n(i)+h*M11jsp</td><td rowspan=1 colspan=1>(s+h)*n(i)+1&lt;p</td></tr><tr><td rowspan=1 colspan=1>虫蚀</td><td rowspan=1 colspan=1>s*n(i)+h+[]</td><td rowspan=1 colspan=1>M[]</td><td rowspan=1 colspan=1>2(s +h)*n(i)+h+M 11ip</td><td rowspan=1 colspan=1>+(s+h)*n(i)+h+ML11≤p</td></tr></table>

$\textcircled{3}$ 链路拥挤和处理器拥挤：拥挤是一种全局现象,与体系结构、选路策略和处理器对之间的传送数据量有关。度量拥挤是在所有消息都同时选路的假定下进行的。令cong表示通信处理器对的总数,即cong=∑n(i),其中1≤cong$\leqslant _ { \pmb { p } } ( _ { \pmb { \mathscr { p } } } - 1 ) ; _ { \pmb { \mathscr { b } } }$ 为机器对剖宽度,它被定义为将机器对分成处理器数彼此相当的两半所必须移去的最少链路数(参见表4.1);令 $L _ { \mathbf { m } }$ 是任意处理器对之间最大信包数，即 $L _ { \mathfrak { m } } = \operatorname* { m a x } _ { 1 \leqslant i , j \leqslant p } \biggl [ \frac { L _ { i , j } } { l } \biggr ] ; L _ { a }$ 为平均信包数，即 $L _ { a } = \frac { 1 } { c o n g } \sum _ { 1 \leqslant i , j \leqslant p } \left[ \frac { L _ { i , j } } { l } \right]$ ,则链路上的拥挤 $\displaystyle C _ { l } = L _ { \mathrm { m } } \star \left\lceil \frac { c o n g } { b } \right\rceil$ ;处理器上的拥挤 $C _ { \hat { P } } = L _ { a } \star \ \left\lceil \frac { c o n g } { \hat { P } } \right\rceil \star h$ 。所以，在一个超级步中总的通信单位数为 $\operatorname* { m a x } _ { 1 \leqslant i \leqslant p } \big \{ S _ { i } + R _ { i } \big \} + C _ { l } + C _ { p } \circ$

$\textcircled{4}$ 公共通信模式的通信单位数： $\mathrm { C } ^ { 3 }$ 模型的提出者,为常用的通信模式(如一到一、多到多、多到一、一到多等)计算出了非阻塞发送和接收时用虫蚀选路式的通信单位数，兹概括于表4.4中,其中为了简化表示,每条消息长度记为 $\mathrm { L } _ { \circ }$

表4.4非阻塞发送和接收虫蚀式选路的通信单位数一览表  

<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>S1</td><td rowspan=1 colspan=1>R1</td><td rowspan=1 colspan=1>C</td><td rowspan=1 colspan=1>C</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>一到s+[÷]+h</td><td rowspan=1 colspan=1>[]</td><td rowspan=1 colspan=1>[1]x[]</td><td rowspan=1 colspan=1>[11*h</td></tr><tr><td rowspan=1 colspan=1>多到多</td><td rowspan=1 colspan=1>(p-1)*(s+[÷])+h</td><td rowspan=1 colspan=1>[/]*（p-1)</td><td rowspan=1 colspan=1>1=11</td><td rowspan=1 colspan=1>[11*h*(p-1)</td></tr><tr><td rowspan=1 colspan=1>多到一</td><td rowspan=1 colspan=1>s+[1+h</td><td rowspan=1 colspan=1>[1*（0-1|[1</td><td rowspan=1 colspan=1>[1*（0-1|[1</td><td rowspan=1 colspan=1>[1*h</td></tr><tr><td rowspan=1 colspan=1>一到多</td><td rowspan=1 colspan=1>s+[/]*(p-1)+h</td><td rowspan=1 colspan=1>[]</td><td rowspan=1 colspan=1>[11</td><td rowspan=1 colspan=1>[]*h</td></tr></table>

对 ${ \bf C } ^ { 3 }$ 模型的评注 $\textcircled { 1 } \mathbf { C } ^ { 3 }$ 模型特别适合于粗粒度算法的开发与分析，模型特别强调了通信瓶颈的作用,在此方面它比BSP 和 $\scriptstyle \log \mathbf { P }$ 模型都要准确和详尽得多； $\textcircled { 2 } \textcircled { \times } 3$ 模型作为开发敏感于并行机参数的粗粒度算法的平台,已经研究了诸如各种通信模式、矩阵向量乘法、确定二元图像的连通性等并行算法,并已在Delta和Paragon机器上验证了 $\mathrm { C } ^ { 3 }$ 模型的有效性; $\textcircled{3}$ 粗粒度并行机上并行算法的性能非常敏感于通信模式,容易拥挤的通信模式很容易造成通信瓶颈,并行机参数之间的关系以及这些参数与通信数据量之间的关系对如何执行选路操作有着至关重要的影响，同时在准备信包和建立选路路径过程中所招致的大的软件开销也起着重要的作用。此外，粗粒度算法通常是将串行和并行解题方法结合在一起,决定哪些子问题以及多大的子问题应该串行解，哪些应是并行解,这对算法的总体性能也是个非常关键的问题。

# 4.2.6对BSP和logP的评注

从 BSP 到logPBSP 把所有的计算和通信视为一个整体行为而不是一个