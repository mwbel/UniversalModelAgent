# 第二章 当代并行机系统：SMP、MPP 和 COW

自20世纪70年代初到现在，并行计算机的发展已有20多年的历史了。在此期间,出现了各种不同类型的并行机,包括向量机、SIMD计算机和MIMD 计算机。随着计算机的发展，曾经风行一时的向量机和SIMD计算机现已退出历史舞台，而MIMD类型的并行机却占了主导地位。当代主流的并行机是可扩放的并行机,包括共享存储的对称多处理机(SMP)和分布存储的大规模并行机(MPP)与工作站机群(COW)。本章首先讨论SMP的结构特性及其代表机器Origin2000;然后讨论MPP的结构特性及其代表机器SP2;接着讨论COW的基本原理及其代表系统NOW；最后介绍一下我国曙光系列并行机，包括曙光1号、曙光-1000 和曙光-2000,它们分别属于 SMP和MPP系统。

# 2.1 对称多处理机 SMP

对称多处理机 SMP(Symmetric Multiprocessor)结构在现今的并行服务器中几乎普遍采用。SMP 系统属于UMA（Uniform Memory Access）机,NUMA(Nonuniform Memory Access)机是 SMP 系统的自然推广,而 CC-NUMA(Coher-ent-CacheNUMA)实际上是将一些SMP作为单节点而彼此连接起来所构成的分布共享存储系统(见图1.25)。本节首先讨论多处理机系统(SMP和CC-NU-MA)的结构特性;然后简介一个当今有代表性的商用超级服务器系统Origin2000,以期对多处理机系统有个一般了解。

# 2.1.1 SMP和 CC-NUMA 结构特性

对称多处理器 SMP结构特性 参照图1.20(b),共享存储的 SMP系统结构具有如下特性： $\textcircled{1}$ 对称性：系统中任何处理器均可访问任何存储单元和I/O设备； $\textcircled{2}$ 单地址空间：单地址空间有很多好处,例如因为只有一个OS和DB 等副本驻留在共享存储器中，所以OS可按工作负载情况在多个处理器上调度进程从而易达到动态负载平衡，又如因为所有数据均驻留在同一共享存储器中,所以用户不必担心数据的分配和再分配； $\textcircled{3}$ 高速缓存及其一致性：多级高速缓存可支持数据的局部性，而其一致性可由硬件来增强； $\textcircled{4}$ 低通信延迟：处理器间的通信可用简单的读/写指令来完成(而多计算机系统中处理器间的通信要用多条指令才能完成发送/接收操作）。

目前大多数商用SMP系统都是基于总线连接的，占了并行计算机很大市场,但是 SMP也具有如下问题： $\textcircled{1}$ 欠可靠：总线、存储器或OS失效均会造成系统崩溃，这是SMP系统的最大问题； $\textcircled{2}$ 可观的延迟：尽管SMP比MPP通信延迟要小,但相对处理器速度而言仍相当可观(竞争会加剧延迟),一般为数百个处理器周期,长者可达数千个指令周期; $\textcircled{3}$ 慢速增加的带宽：有人估计，主存和磁盘容量每3年增加4倍,而SMP存储器总线带宽每3年只增加2倍,I/O总线带宽增加速率则更慢,这样存储器带宽的增长跟不上处理器速度或存储容量的步伐;$\textcircled{4}$ 不可扩放性：总线是不可扩放的,这就限制最大的处理器数一般不能超过10。为了增大系统的规模，可改用交叉开关连接,或改用CC-NUMA或机群结构。

CC-NUMA系统如图1.25所示，高速缓存一致性非均匀存储访问 CC-NUMA机,就是将一些小规模的SMP作为单节点,通过系统互连网络扩展至一个大规模多处理器系统。SMP节点中的所有局部存储器构成了共享主存,这样就可保持 SMP易编程的优点,同时由于可方便地加入更多的节点从而改善了常规 SMP系统的可扩放性。因为对于给定的应用,可利用数据局部性,在绝大部分时间内同时访问多个局部存储器，从而也缓解了竞争和带宽问题。

目前绝大多商用CC-NUMA均使用基于目录的高速缓存一致性协议。CC-NUMA机最显著的优点是程序员无需明确地在节点上分配数据,系统的硬件和软件开始时自动在各节点中分配数据,在应用程序运行期间,高速缓存一致性硬件设施会自动地将数据移至要使用它的地方。例如某一程序有P和Q两个进程,执行如下访问数组A和B的代码段：

P Q第一步：Use(A) Use(B)第二步：Use(B) Use(A)

图2.1(a)所示的初始数据分配是很适合上述代码段的第一步的;在第二步时,硬件能自动地将B移人节点1和将A移人节点2,程序员不必作这些,但在多计算机系统中却要求程序员作明确的数据分配。

商用 SMP服务器SMP 是现今最成功的并行计算机,它经常工作在网络环境中,所以其安全性、集成能力和易于管理是很重要的。表2.1综合比较了现今流行的5种商用 SMP 系统特性,这些参数均是最大或最优值(表中B为字节)。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0070/auto/images/0e43d3930947d3b63c15484ad75d7bcade60fca69f688531767829080e8e701a.jpg)  
图2.1CC-NUMA使用远程高速缓存重新分配数据（a)第一步的数据分配；(b)第二步的数据再分配

表2.15种商用SMP系统特性比较一览表  

<table><tr><td rowspan=1 colspan=1>系统特性</td><td rowspan=1 colspan=1>、DECAlphaserver84005/440</td><td rowspan=1 colspan=1>HP9000/T600</td><td rowspan=1 colspan=1>IBMRS600/R40</td><td rowspan=1 colspan=1>Sum UltraEnterprise6000</td><td rowspan=1 colspan=1>SGI PowerChallenge XL</td></tr><tr><td rowspan=1 colspan=1>处理器数目</td><td rowspan=1 colspan=1>：12福</td><td rowspan=1 colspan=1>：  心</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>厦   加：</td><td rowspan=1 colspan=1>36</td></tr><tr><td rowspan=1 colspan=1>处理器类型i</td><td rowspan=1 colspan=1>437 MHzAlpha21164E</td><td rowspan=1 colspan=1>180MHzPA8000</td><td rowspan=1 colspan=1>112MHzPowerPC604     1</td><td rowspan=1 colspan=1>167MHzUtraSPARC</td><td rowspan=1 colspan=1>195MHz： MIPSLR10000</td></tr><tr><td rowspan=1 colspan=1>处理器片外高速缓存容量</td><td rowspan=1 colspan=1>福4MB心</td><td rowspan=1 colspan=1>8MB</td><td rowspan=1 colspan=1>1 MB！</td><td rowspan=1 colspan=1>512MB</td><td rowspan=1 colspan=1>4MB</td></tr><tr><td rowspan=1 colspan=1>最大主存容量</td><td rowspan=1 colspan=1>28GB</td><td rowspan=1 colspan=1>116GB</td><td rowspan=1 colspan=1>i  .2GB</td><td rowspan=1 colspan=1>30GB</td><td rowspan=1 colspan=1>16GB</td></tr><tr><td rowspan=1 colspan=1>互连网络及带宽               ！</td><td rowspan=1 colspan=1>BUS2.1GB/</td><td rowspan=1 colspan=1>BUS960MB/s</td><td rowspan=1 colspan=1>1BUS+Xbar1.8GB/s</td><td rowspan=1 colspan=1>！BUS+Xbar2.6GB/s</td><td rowspan=1 colspan=1>BUS1:2 GB/s</td></tr><tr><td rowspan=1 colspan=1>外磁盘容量</td><td rowspan=1 colspan=1>192 GB</td><td rowspan=1 colspan=1>168GB</td><td rowspan=1 colspan=1>38 GB</td><td rowspan=1 colspan=1>63.GB</td><td rowspan=1 colspan=1>144GB：：！</td></tr><tr><td rowspan=1 colspan=1>I/O通道</td><td rowspan=1 colspan=1>12 PCI总线，每个133MB/s</td><td rowspan=1 colspan=1>N/A1</td><td rowspan=1 colspan=1>2MCA,每个160 MB/s</td><td rowspan=1 colspan=1>30 Sbus,每个200 MB/s</td><td rowspan=1 colspan=1>6 Power Channel-2HIO,每个320MB/s</td></tr><tr><td rowspan=1 colspan=1>I/O槽</td><td rowspan=1 colspan=1>144PCI精</td><td rowspan=1 colspan=1>112HPPB1</td><td rowspan=1 colspan=1>15MCA</td><td rowspan=1 colspan=1>45 Sbus</td><td rowspan=1 colspan=1>12 HIO槽</td></tr><tr><td rowspan=1 colspan=1>I/O带宽</td><td rowspan=1 colspan=1>1.2 GB/s</td><td rowspan=1 colspan=1>1GB/s！</td><td rowspan=1 colspan=1>320 MB/s</td><td rowspan=1 colspan=1>2.6GB/8</td><td rowspan=1 colspan=1>每个HIO槽320MB/s5</td></tr></table>

# $\times 2 . 1 . 2$ SGI/Cray Origin 2000超级服务器

1996年10月，SGI/Cray公司推出了Origin 2000系统，它采用了CC-NUMA结构，此结构也被称之为可扩放共享存储多处理机S2MP或S2MP(Scalable

Shared Memory Multiprocessor)。设计时吸取了DASH的经验,所设计的系统规模可达到1024个处理器和1TB主存，其中 $1 \sim 6 4$ 个处理器的系统叫SGIOri-gin 2000,而大于等于128个处理器的系统叫（ray Origin 2000。现有的Origin2000的结构配置属性综合于表2.2中。

表2.2Origin2000结构配置属性一览表  

<table><tr><td rowspan=1 colspan=1>属性</td><td rowspan=1 colspan=1>立式（Deskside)配置</td><td rowspan=1 colspan=1>装架式（Rack）配置</td></tr><tr><td rowspan=1 colspan=1>处理器数目</td><td rowspan=1 colspan=1>1~8</td><td rowspan=1 colspan=1>2~128</td></tr><tr><td rowspan=1 colspan=1>峰值速度(Gflops)</td><td rowspan=1 colspan=1>3.12</td><td rowspan=1 colspan=1>49.92</td></tr><tr><td rowspan=1 colspan=1>高速缓存容量（MB)</td><td rowspan=1 colspan=1>1~32</td><td rowspan=1 colspan=1>2~512</td></tr><tr><td rowspan=1 colspan=1>物理存储器容量(GB)</td><td rowspan=1 colspan=1>0.064~16</td><td rowspan=1 colspan=1>0.064~256</td></tr><tr><td rowspan=1 colspan=1>总计峰值存储带宽(GB/s)</td><td rowspan=1 colspan=1>3.12</td><td rowspan=1 colspan=1>49.92</td></tr><tr><td rowspan=1 colspan=1>I/端口数目</td><td rowspan=1 colspan=1>14</td><td rowspan=1 colspan=1>208</td></tr><tr><td rowspan=1 colspan=1>总计峰值I/O带宽(GB/s)</td><td rowspan=1 colspan=1>6.2</td><td rowspan=1 colspan=1>102</td></tr></table>

系统结构Origin2000系统结构如图2.2所示。它的每个节点包括1或2个 MIPSR10000处理器（时钟 $1 9 5 ~ \mathrm { M F z }$ ,峰值速度395Mllops)，-个可高达 $4 \ \mathrm { M B }$ 的高速缓存和-个DSM主存(物理上分散在各节点中，但可被所有节点访问),硬件增强了基于目录的高速缓存一致性。如图2.3所示，一个HUB(ASIC交叉开关)连接系统中的处理器、存储器、互连网络和I/O系统,HUB有4个双向端口，使用 $1 9 5 ~ \mathrm { M H z }$ 的时钟，每个口可提供单向 $7 8 0 ~ \mathrm { M B / s }$ 的峰值带宽和全双工1.56(GB/s的峰值带宽,它用于节点内和节点间通信选路,4个成对的接口电路(ififo,ofifo)负责内部和外部信息格式的转换。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0070/auto/images/ec0c5beeb0d9bf90eb65487a6de36c50aba959d8af257051c9357207b6299a33.jpg)  
图2.2Origin 2000系统结构

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0070/auto/images/67425eb9f31a0c84a8dfb1c4b9ceb06542748905390a81dc513f69236c036ee7.jpg)  
图2.3Origin 2000中交叉开关HUB芯片

①I/O子系统:Origin 2000的I/O子系统示于图2.4中,其中,XBOW是一个8端口的交叉开关(各口均使用XIO协议):2个连向节点,其余6个连向XIO设备或者ASIC小部件，包括图形小部件G(GraphicsWidget）和桥接小部件B(BridgeWidget)。通过 32位或 64位的PCI总线,不同的I/O设备（ATM、HiPPI、FDDI、SCSI等)均可连向Origin 2000。Origin 2000 可提供单- I/O空间，即任何处理器能访间任·[O设备。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0070/auto/images/fd01944a045c817e9f7c614aee8aadd5151e343603d587eec2cbd6ec15c52d10.jpg)  
图2.4Orgin 2000的I/0子系统

$\textcircled{2}$ 互连系统:Origin2000的互连系统由CrayLink电缆和图2.5所示的路出器组成。SGI SPIDER路由器提供可靠的虫蚀选路，它是6端口的交叉开关,这些端口连向节点或别的路由器。路由器允许6个端口同时全双工工作。由于外部频率$( 3 9 0 ~ \mathrm { M H z } )$ 和路由器芯片内部频率 $( 9 7 . 5 ~ \mathrm { M H z } )$ 的不同，所以需使用源同步驱动器SSD(Source Synchronous Driver)和源同步接收器 SSR(Source Synchronous Receiver)施行内/外频率 $( 9 7 . 5 ~ \mathrm { M H z } / 3 9 0 ~ \mathrm { M H z } )$ 和字长(64位/16位)的转换。链路级协议LLP(Link-Level Protocol)确保信息可靠传输（使用CRC误差检测和重发校正），施行流控、缓解竞争和拥挤等。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0070/auto/images/98c7c65bf763c0b024e46740468ae68f96d45e23f8e44d02a9090825685f7b0f.jpg)  
图2.5Origin 2000的 SPIDER 路由器芯片

$\textcircled{3}$ 胖超立方拓扑:Origin 2000 中采用了胖超立方(Fat Hypercube)拓扑。如图2.6所示，胖超立方是将传统的2元超立方加以修改而得，其优点是保持了超立方线性对剖宽度的优点且避免了节点度的增加。在此拓扑中,每个路由器R芯片有6个端口，其中的2个连向节点，其余的4个用于网络连接。按照一般的超立方，度为4的节点最多也只能构造16个顶点的超立方（即Origin 2000中的32个节点),但使用了胖超立方拓扑,可允许Origin 2000连接多达512个节点(1024个处理器)。图2.6(a)只有-个节点，它有2个处理器，还可连向XBOW交叉开关；图2.6(b)中，-个SPIDER路由器R连向2个节点;图2.6(c)中2个R连向4个节点；以此方式可达32个节点(图2.6(f)),至此，如果把R视为超立方的顶点，则它就是普通的2元超立方连接。注意，未被使用的路由器端可连向快速链路( $\operatorname { E x } -$ pressLink)以降低延迟和增大对剖带宽(如图2.6(d)中的虚线连接)。当超过32个节点时，Origin2000的胖超立方中使用了额外的路由器（称之为元路由器，Metaroutcr),8个元路由器构成·个（ray Rouler，这些元路由器只用作中间选路，不连向任何节点，·个64个节点(32个顶点，即路由器)的胖超立方拓扑如图2.6$( \mathbf { g } )$ 所示，其中4个8顶点的子立方中每个顶点都连向一个元路由器，这种胖超立方可·直扩放到1024个处理器，读者不妨想一想应如何构造？

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0070/auto/images/b2a48e88c7329597d22fb37518c742c989f421bb7148ffd78af9f6024ea6f591.jpg)  
图2.6Origin 2000的胖超立方拓扑

(a)2个处理器;(b)4个处理器； $\left( { \mathfrak { c } } \right) { \mathfrak { s } }$ 个处理器；(d)I6个处理器；(c)32个处理器；(f)64个处理器； $( \pmb { \mu } )$ 128个处理器

$\textcircled{4}$ 分布共享存储子系统：Origin 2000 系统中有一个分布式共享存储子系统，节点内的存储模块叫近存储器,别的节点中的存储模块叫远存储器。节点中的主存储器和目录存储器使用同步DRAM可组织成多达8个体(Bank),每个体提供4路交叉访问，使用4路交叉访间的存储子系统带宽高达 $78 0 ~ \mathrm { M B / s _ { o } }$

软件环境Origin 2000 运行细胞(Cellular)IRIX操作系统。其1996 年版本是--个64位的多线程、多道程序操作系统,它的设计目标要满足可兼容性、可扩放性（扩展到128个或更多处理器）可用性和高吞吐率的要求。

$\textcircled{1}$ 细胞概念：为了增强细胞IRIX的可扩放性,使用了细胞概念(Cell（oncept)和存储器管理软件的办法。前者能模块化操作系统核，后者能有效地开拓 S2MP的硬件。细胞IRIX结构把核文本和数据分散成 SMP大小的称作细胞的块,其中每个细胞包含一个核文本和数据结构的副本,并负责控制--个由--组处理器、存储器和IO设备组成的机器模块,细胞概念的关键特性是将操作系统服务分散化和局部化,多个细胞可驻留在--个Origin 2000 系统中，允许一些应用同时地、独立地

访问多个机器模块。

$\textcircled{2}$ 存储管理：细胞IRIX的存储管理软件包括存储器复制、迁移和置放机制(存储管理的基本单位是页)：复制机制复制一个只读页的副本。当一个页是只读时，硬件检测共享情况并调用存储管理子系统执行存储器复制;迁移机制移动页面靠近最经常访问它的处理器。当一页被访问时，硬件计数器记录外节点的访问次数,如其值超过某一阈值,则存储管理子系统将迁移该页面;置放机制是初始分配数据和线程以开拓局部性。细胞IRIX环境允许用户告诉系统页面彼此间应如何置放、如何映射线程到页面和如何定位线程离硬件资源的远近。

$\textcircled{3}$ 可用性支持：Origin2000的可用性支持包括硬件和软件：硬件设计使用冗余供电与冷却、热可插磁盘、廉价冗余磁盘阵列RAID(Redundant Array of Inexpen-sive Disks)等技术,因特网支持节点间多条路径、硬件链路层协议提供错误包的检测与重发等;IRIX系统软件包含进一步增强可用性支持(如文件系统快速再启动、监视通信故障时间、磁盘镜像等),提供访问保护权限和检查点再启动机制以及高有效网络、数据库与其它应用的附加支持(通过支持队列、套接字、XWindows、图形等）。

$\textcircled{4}$ 吞吐率支持：Origin2000 通过使用优化调度(它支持大量的处理器和用户进程)和一个64位的称之为xFS的日志文件系统(它支持高吞吐率和确保I/O速率)来有效地使用系统和增强系统吞吐率。细胞IRIX提供3种调度机制： $\textcircled{1}$ 帧调度(Frame Scheduling)：帧调度器能完全掌管调度和分发进程给一个或多个CPU以确保进程执行的精确速率； $\textcircled{2}$ 组调度(Gang Scheduling)：细胞IRIX能调度一组线程,这些线程可用锁或信号灯相互通信； $\textcircled{3}$ 处理器相似（Processor Affinity)：细胞IRIX能自动记下某一CPU,在该CPU上,上次运行的进程试图运行在同一CPU上。xFS文件系统采用范圈(Extent)概念和日志(Journaling)技术来达到高吞吐率;采用允许应用预约文件系统带宽来确保I/O速率。范围的使用有助于减少磁盘寻找时间和旋转延迟，因而增加了I/O吞吐率；日志(也称为记录,Logging)是一种记录所有文件系统变化的技术，此技术也有助于减少系统恢复时间，因为系统崩溃后,系统只访问少量的最近更新的文件登录，而不必像Unix文件系统那样执行很花时间的文件系统检查。

系统性能因为Origin2000 结构设计很注重整体特性，所以存储器、I/O互连网络的能力都能随机器规模的增大而成比例地增加。表2.3列出了Origin2000中不同层次存储器的读延迟;表2.4列出Origin 2000的总计带宽和存储器读延迟。

表2.3Origin2000不同层次存储读延迟一览表  

<table><tr><td rowspan=1 colspan=1>数据位置</td><td rowspan=1 colspan=1>读延迟(时钟数)</td></tr><tr><td rowspan=1 colspan=1>寄存器</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>1级高速缓存(片上)</td><td rowspan=1 colspan=1>1~3</td></tr><tr><td rowspan=1 colspan=1>2级高速缓存(片外)</td><td rowspan=1 colspan=1>10</td></tr><tr><td rowspan=1 colspan=1>本地存储器</td><td rowspan=1 colspan=1>61</td></tr><tr><td rowspan=1 colspan=1>远程存储器(1个路由器以远)</td><td rowspan=1 colspan=1>117</td></tr><tr><td rowspan=1 colspan=1>远程存储器(2个路由器以远)</td><td rowspan=1 colspan=1>137</td></tr><tr><td rowspan=1 colspan=1>远程存储器(3个路由器以远)</td><td rowspan=1 colspan=1>157</td></tr></table>

表2.4Origin 2000 带宽(GB/s)和延迟 $\mathbf { \eta } ( \mathbf { n s } )$ 一览表  

<table><tr><td rowspan=1 colspan=1>系统配置I/O:节点:CPU</td><td rowspan=1 colspan=1>总计峰值存储器带宽</td><td rowspan=1 colspan=1>总计峰值I/O带宽</td><td rowspan=1 colspan=1>互连网络对剖带宽</td><td rowspan=1 colspan=1>存储器读延迟</td></tr><tr><td rowspan=1 colspan=1>1:1:2</td><td rowspan=1 colspan=1>0.78</td><td rowspan=1 colspan=1>1.56</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>313</td></tr><tr><td rowspan=1 colspan=1>2:2:4</td><td rowspan=1 colspan=1>1.56</td><td rowspan=1 colspan=1>3.12</td><td rowspan=1 colspan=1>1.56</td><td rowspan=1 colspan=1>497</td></tr><tr><td rowspan=1 colspan=1>2:4:8</td><td rowspan=1 colspan=1>3.12</td><td rowspan=1 colspan=1>6.24</td><td rowspan=1 colspan=1>3.12</td><td rowspan=1 colspan=1>601</td></tr><tr><td rowspan=1 colspan=1>4:8:16</td><td rowspan=1 colspan=1>6.24</td><td rowspan=1 colspan=1>12.48</td><td rowspan=1 colspan=1>6.24</td><td rowspan=1 colspan=1>703</td></tr><tr><td rowspan=1 colspan=1>8:16:32</td><td rowspan=1 colspan=1>12.48</td><td rowspan=1 colspan=1>24.96</td><td rowspan=1 colspan=1>12.48</td><td rowspan=1 colspan=1>805</td></tr><tr><td rowspan=1 colspan=1>16:32:64</td><td rowspan=1 colspan=1>24.96</td><td rowspan=1 colspan=1>51.2</td><td rowspan=1 colspan=1>12.48</td><td rowspan=1 colspan=1>908</td></tr><tr><td rowspan=1 colspan=1>32 :64 :128</td><td rowspan=1 colspan=1>49.92</td><td rowspan=1 colspan=1>99.84</td><td rowspan=1 colspan=1>24.96</td><td rowspan=1 colspan=1>1 112</td></tr></table>

由此可看出,总计带宽(存储器、I/O和互连网络)几乎随处理器数线性增加,而延迟只是对数增长。这种低延迟和高带宽使得Origin 2000系统在市场上具有很大的优势。

小结表2.5列出了常用的4种CC-NUMA结构特性比较,其中DASH是个研究样机,而其它几种都已是商品。表中 SCI(Scalabel Coherence Interface)是可扩放一致性接口,它是将传统的总线式底板扩展至全双工、点到点互连结构,SCI互连可以是环形结构或交叉开关结构。

表2.54种CC-NUMA结构比较一览表  

<table><tr><td rowspan=1 colspan=1>结构特性</td><td rowspan=1 colspan=1> StanfordDash</td><td rowspan=1 colspan=1> SequentNUMA-Q</td><td rowspan=1 colspan=1>HP/ConvexEXemplar</td><td rowspan=1 colspan=1>SGI/CrayOrigin 2000</td></tr><tr><td rowspan=1 colspan=1>节点结构</td><td rowspan=1 colspan=1>4CPU SMP节点监听总线</td><td rowspan=1 colspan=1>4CPU SMP节点监听总线</td><td rowspan=1 colspan=1>8CPU SMP节点交叉开关</td><td rowspan=1 colspan=1>2CPU非SMP节点HUB</td></tr><tr><td rowspan=1 colspan=1>节点互连</td><td rowspan=1 colspan=1>2D网孔</td><td rowspan=1 colspan=1>SCI 环</td><td rowspan=1 colspan=1>多 2D SCI环</td><td rowspan=1 colspan=1>胖超立方</td></tr><tr><td rowspan=1 colspan=1>高速缓存一致性协议</td><td rowspan=1 colspan=1>节点内监听全局目录</td><td rowspan=1 colspan=1>SCI 链表一致性协议</td><td rowspan=1 colspan=1>修改的 SCI协议</td><td rowspan=1 colspan=1>修改的Dash协议</td></tr><tr><td rowspan=1 colspan=1>其它</td><td rowspan=1 colspan=1>节点内高速缓存到高速缓存共享</td><td rowspan=1 colspan=1>节点高速缓存组调度相似性调度</td><td rowspan=1 colspan=1>节点高速缓存</td><td rowspan=1 colspan=1>组调度、页面迁移、置放、复制</td></tr></table>

# 2.2大规模并行机 MPP

大规模并行处理机MPP(Massively Parallel Processor)一词的含义过去并不明确,其意义常随时间而变。按照现今的技术,它是指由成百上千个处理器组成的大型(Large-Scale)计算机系统。1997年7月由 Intel和 Sandia研制成的ASCI OptionRed,其处理器数已达9216个,是属于高端MPP系统。MPP系统是属于NORMA(No-Remote Memory Access)模型的机器。早期也曾把非高速缓存一致性NUMA，即NCC-NUMA(Non-Cache Coherent NUMA)模型的机器(例如 Cray T3E)也算作MPP系统,但现在看来T3E仍划分在NUMA类为宜(参见图1.27)。同样现在也把使用机群(Cluster)方法构造的MPP系统(例如 IBMSP2和曙光-2000)也有时单列为机群一类;而把CC-NUMA模型的机器(例如 SGI/Cray Origin 2000)算作是可扩放共享存储多处理机。本节首先讨论MPP的结构特性及其有关问题;然后简介一个当今颇为流行的机群型：大规模并行机 SP2,以期对 MPP系统有个初步了解。

# 2.2.1 MPP结构特性

MPP公共结构所有的 MPP均使用物理上分布的存储器，且使用分布的I/O也渐渐变多。现今的 MPP公共结构如图2.7所示,其中每个节点有一个或多个处理器和高速缓存(P/C)、一个局部存储器、有或没有磁盘和网络接口电路(NIC:Network Interface Circuitry),它们均连向本地互连网络(早期多为总线而近期多为交叉开关),而节点间通过高速网络(HSN:High Speed Network)相连。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0070/auto/images/19b9a9aeeb180a9910ffa9378b96cc18794547c645f075e14e8f0a2cccfba9ad.jpg)  
图2.7MPP公共系统结构

MPP设计问题设计MPP系统所应考虑的问题是：①可扩放性：MPP著名特性就是系统能扩展至成千个处理器，而存储器和I/O的容量及带宽亦能按比例的增加。为此，采用物理上分布的存储器结构，它能提供比集中存储器结构更高的总计存储带宽，因此有潜在的高可扩放性；要平衡处理能力与存储和I/O的能力，因为存储器和I/O子系统的速度不可能与处理器成比例地提高；要平衡计算能力与交互能力，因为进程/线程的管理、通信与同步等都相当费时间。②系统成本：因为MPP系统中包含大量的元件，为了保证系统的低成本应确保每个元件的低成本。为此，应采用现有的商用CMOS微处理器，这些芯片原为PC机、工作站和服务器开发的，自然成本要低，并且按照Mo0re定律其性能每一年半到二年要翻一番；要采用相对稳定的结构，如第一章第1.3.1节所讲的可扩放并行机Shel结构（图1.21)；要使用物理上分布的存储器结构，它比同规模机器的中央(集中）存储器结构要便宜；要采用SMP节点方式以削减互连规模。但是现有的商用微处理器是为小系统(如PC机、工作站和SMP服务器等)而不是为MPP设计的，使用它虽在可扩放性和低成本方面有所得益，但用于MPP也带来一些问题：诸如微处理器地址空间不足够大（例如使用在CrayT3DMPP中的Alpha21064微处理器，它只能提供33位物理地址空间，而T3D最大物理存储容量为128GB)，所以设计者必须加人专门硬件以扩大物理地址空间规模；微处理器和它的计算能力相比，它缺乏足够的操作系统支持，使其难以有效地支持进程管理、通信和同步等。③通用性和可用性：MPP要走向成功之路，它必须是个通用系统，能支持不同的应用(技术和商业）、不同算法范例、不同操作模式,而不能局限于很窄的应用。为此，MPP要支持异步MIMD模式(SIMD似已过时）；要支持流行的标准编程模式（如PVM、MPI和HPF)；诸节点应能按大、小作业要求进行不同的组合以支持交互和批处理模式；互连拓扑应对用户透明，对用户而言他(她)所看到的是一组全连接的节点；MPP应在不同层次上支持单一系统映像SSI(Single-SystemImage),因为紧耦合的MPP常使用分布式操作系统，所以要在硬件级和OS级提供此映像；据估计1000个处理器的MPP系统，每天至少有一个处理器失效，所以MPP必须使用高可用性的技术。④通信要求：MPP和COW的关键差别是节点间的通信，COW使用标准的

LAN,而MPP使用高速、专用高带宽、低延迟的互连网络,无疑在通信方面优于COW。然而通信技术的迅速发展,COW对MPP颇具威胁,从而MPP对通信技术也提出了更高的要求。 $\textcircled{5}$ 存储器和I/O能力：因为MPP是可扩放系统,所以就要求非常大的总计存储器和I/O设备容量，然而I/O方面的进展仍落后于系统中的其余部分,故如何提供一个可扩放的I/O子系统就成为MPP的热门研究课题。

MPP的过去和现在早期的 MPP主要应用于科学和工程超级计算,著名的系统有TM(Thinking Machine） CM2/CM5、NSSA/Goodyear MPP、nCUBE、CrayT3D/T3E、Intel Paragon、MasPar MP1、Fujitsu VPP500 和 KSR1 等。表2.6列出了部分MPP系统的特性比较。表2.7列出了MPP所用的几个典型微处理器特性参数,其中 SPEC(Standard Performance Evaluation Corporation)代表标准性能评价公司,它对目前高性能CPU等进行整数(int)和浮点数(fp)运算性能测试。当今微处理器系列及其代表性的CPU芯片如图2.8所示。现在，很多MPP都已成功地应用在商业和网络应用中。据统计，截止1997年所销售的 SP2系统,大约有一半用于商业(如仓库、决策支持系统和数字图书馆等),剩下的一半大部分用于LAN系统中，只有很少的部分用于科学超级计算。此外,美国开始执行的ASCI计划(见第一章第1.1.2节)也包括研制三台高端 MPP计算机,它们是Intel 公司与 SNL(Sandia 国家实验室)联合研制的Option Red(红选择）、IBM公司与LLNL(LawrenceLivermore国家实验室)联合研制的Blue Pacific(蓝太平洋）和SGI公司与LANL(Los Alamos 国家实验室)联合研制的 Blue Mountain(蓝山）,其主要性能综合于表2.8中。

表2.6典型MPP系统特性比较一览表  

<table><tr><td rowspan=1 colspan=1>结构特性</td><td rowspan=1 colspan=1>IBM SP2</td><td rowspan=1 colspan=1>Cray T3D</td><td rowspan=1 colspan=1>Cray T3E</td><td rowspan=1 colspan=1>Intel Paragon</td><td rowspan=1 colspan=1>Intel/Sandia Option Red</td></tr><tr><td rowspan=1 colspan=1>典型配置</td><td rowspan=1 colspan=1>400个节点100 Gflops</td><td rowspan=1 colspan=1>512个节点153 Gflops</td><td rowspan=1 colspan=1>512个节点1.2 Tflops</td><td rowspan=1 colspan=1>400个节点40 Gflops</td><td rowspan=1 colspan=1>4536个节点1.8 Tflops</td></tr><tr><td rowspan=1 colspan=1>推出日期</td><td rowspan=1 colspan=1>1994</td><td rowspan=1 colspan=1>1993</td><td rowspan=1 colspan=1>1996</td><td rowspan=1 colspan=1>1992</td><td rowspan=1 colspan=1>1996</td></tr><tr><td rowspan=1 colspan=1>CPU类型</td><td rowspan=1 colspan=1>67 MHz267 MflopsPOWER2</td><td rowspan=1 colspan=1>150 MHz150 MflopsAlpha 21064</td><td rowspan=1 colspan=1>300 MHz600 MflopsAlpha 21164</td><td rowspan=1 colspan=1>50 MHz100 MflopsInteli 860</td><td rowspan=1 colspan=1>200 MHz200 MflopsPentium Pro</td></tr><tr><td rowspan=1 colspan=1>节点结构数据存储</td><td rowspan=1 colspan=1>1 CPU64 MB~2 GB局存1~4.5GB本地磁盘</td><td rowspan=1 colspan=1>2 CPU64 MB主存50 GB共享磁盘</td><td rowspan=1 colspan=1>4~8 CPU256 MB~16 GB16～128 MBDSM主存，共享磁盘</td><td rowspan=1 colspan=1>1~2 CPU256 MB~16 GB16～128 MB局存，48GB共享磁盘</td><td rowspan=1 colspan=1>2 CPU32～256MB局存,共享磁盘</td></tr><tr><td rowspan=1 colspan=1>互连网络</td><td rowspan=1 colspan=1>多级互连网络</td><td rowspan=1 colspan=1>3-D环绕</td><td rowspan=1 colspan=1>3-D环绕</td><td rowspan=1 colspan=1>2-D网孔</td><td rowspan=1 colspan=1>Split2-D 网孔</td></tr><tr><td rowspan=1 colspan=1>访存模型</td><td rowspan=1 colspan=1>NORMA</td><td rowspan=1 colspan=1>NUMA</td><td rowspan=1 colspan=1>NCC-NUMA</td><td rowspan=1 colspan=1>NORMA</td><td rowspan=1 colspan=1>NORMA</td></tr><tr><td rowspan=1 colspan=1>节点OS</td><td rowspan=1 colspan=1>Complete AIX（IBM Unix)</td><td rowspan=1 colspan=1>微核</td><td rowspan=1 colspan=1>基于 Chorus微核</td><td rowspan=1 colspan=1>微核</td><td rowspan=1 colspan=1>轻量级核(LWK)</td></tr><tr><td rowspan=1 colspan=1>编程模型</td><td rowspan=1 colspan=1>消息传递</td><td rowspan=1 colspan=1>共享变量、消息传递、PVM</td><td rowspan=1 colspan=1>共享变量、消息传递、PVM</td><td rowspan=1 colspan=1>消息传递</td><td rowspan=1 colspan=1>基于PUMA Portals消息传递</td></tr><tr><td rowspan=1 colspan=1>编程语言</td><td rowspan=1 colspan=1>MPI、PVMHPF、Linda</td><td rowspan=1 colspan=1>MPI、HPF</td><td rowspan=1 colspan=1>MPI、HPF</td><td rowspan=1 colspan=1>NX、MPIPVM</td><td rowspan=1 colspan=1>NX、PVM、HPF</td></tr><tr><td rowspan=1 colspan=1>点到点通信延迟</td><td rowspan=1 colspan=1>40 μs</td><td rowspan=1 colspan=1>2us</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>30 us</td><td rowspan=1 colspan=1>10 μus</td></tr><tr><td rowspan=1 colspan=1>点到点带宽</td><td rowspan=1 colspan=1>35 MB/s</td><td rowspan=1 colspan=1>150 MB/s</td><td rowspan=1 colspan=1>480 MB/s</td><td rowspan=1 colspan=1>175 MB/s</td><td rowspan=1 colspan=1>380 MB/s</td></tr></table>

表2.7 MPP所用的高性能CPU特性参数一览表  

<table><tr><td></td><td rowspan=1 colspan=2>属性</td><td rowspan=1 colspan=1>Pentium Pro</td><td rowspan=1 colspan=1>Power PC620</td><td rowspan=1 colspan=1>Alpha 21164A Ultra SPARCI</td><td rowspan=1 colspan=1>Alpha 21164A Ultra SPARCI</td><td rowspan=1 colspan=1>MIPS R10000</td></tr><tr><td></td><td rowspan=1 colspan=2>工艺</td><td rowspan=1 colspan=1>BiCMOS</td><td rowspan=1 colspan=1>CMOS</td><td rowspan=1 colspan=1>CMOS</td><td rowspan=1 colspan=1>CMOS</td><td rowspan=1 colspan=1>CMOS</td></tr><tr><td></td><td rowspan=1 colspan=2>晶体管数</td><td rowspan=1 colspan=1>5.5 M/15.5 M</td><td rowspan=1 colspan=1>7 M</td><td rowspan=1 colspan=1>9.6 M</td><td rowspan=1 colspan=1>5.4 M</td><td rowspan=1 colspan=1>6.8 M</td></tr><tr><td></td><td rowspan=1 colspan=2>时钟频率</td><td rowspan=1 colspan=1>150 MHz</td><td rowspan=1 colspan=1>133 MHz</td><td rowspan=1 colspan=1>417 MHz</td><td rowspan=1 colspan=1>200 MHz</td><td rowspan=1 colspan=1>200 MHz</td></tr><tr><td></td><td rowspan=1 colspan=2>电压</td><td rowspan=1 colspan=1>2.9 V</td><td rowspan=1 colspan=1>3.3 V</td><td rowspan=1 colspan=1>2.2 V</td><td rowspan=1 colspan=1>2.5 V</td><td rowspan=1 colspan=1>3.3 V</td></tr><tr><td></td><td rowspan=1 colspan=2>功率</td><td rowspan=1 colspan=1>20 w</td><td rowspan=1 colspan=1>30 W</td><td rowspan=1 colspan=1>20 W</td><td rowspan=1 colspan=1>28W</td><td rowspan=1 colspan=1>30 W</td></tr><tr><td></td><td rowspan=1 colspan=2>字长</td><td rowspan=1 colspan=1>32位</td><td rowspan=1 colspan=1>64位</td><td rowspan=1 colspan=1>64位</td><td rowspan=1 colspan=1>64位</td><td rowspan=1 colspan=1>64位</td></tr><tr><td></td><td rowspan=1 colspan=2>I/O高速缓存</td><td rowspan=1 colspan=1>8 KB/8 KB</td><td rowspan=1 colspan=1>32 KB/32 KB</td><td rowspan=1 colspan=1>8 KB/8 KB</td><td rowspan=1 colspan=1>16 KB/16 KB</td><td rowspan=1 colspan=1>32 KB/32 KB</td></tr><tr><td></td><td rowspan=1 colspan=2>2级高速缓存</td><td rowspan=1 colspan=1>256 KB（多芯片模块）</td><td rowspan=1 colspan=1>1~128 MB（片外）</td><td rowspan=1 colspan=1>96 KB（片上）</td><td rowspan=1 colspan=1>16 MB（片外）</td><td rowspan=1 colspan=1>16 MB（片外）</td></tr><tr><td></td><td rowspan=1 colspan=1>执行单元</td><td></td><td rowspan=1 colspan=1>5个单元</td><td rowspan=1 colspan=1>6个单元</td><td rowspan=1 colspan=1>4个单元</td><td rowspan=1 colspan=1>9个单元</td><td rowspan=1 colspan=1>5个单元</td></tr><tr><td></td><td rowspan=1 colspan=2>超标量</td><td rowspan=1 colspan=2>3路(Way)</td><td rowspan=1 colspan=1>4路</td><td rowspan=1 colspan=1>4路</td><td rowspan=1 colspan=1>4路</td><td rowspan=1 colspan=1>4路</td></tr><tr><td></td><td rowspan=1 colspan=2>流水线深度</td><td rowspan=1 colspan=2>14级</td><td rowspan=1 colspan=1>4~8级</td><td rowspan=1 colspan=1>7~9级</td><td rowspan=1 colspan=1>9级</td><td rowspan=1 colspan=1>5~7级</td></tr><tr><td></td><td rowspan=1 colspan=1>SPECint 92</td><td rowspan=1 colspan=2>366</td><td rowspan=1 colspan=1>225</td><td rowspan=1 colspan=1>&gt;500</td><td rowspan=1 colspan=1>350</td><td rowspan=1 colspan=1>300</td></tr><tr><td></td><td rowspan=1 colspan=1>SPECfp 92</td><td rowspan=1 colspan=2>283</td><td rowspan=1 colspan=1>300</td><td rowspan=1 colspan=1>&gt;750</td><td rowspan=1 colspan=1>550</td><td rowspan=1 colspan=1>600</td></tr><tr><td></td><td rowspan=1 colspan=1>SPECint 95</td><td rowspan=1 colspan=2>8.09</td><td rowspan=1 colspan=1>225</td><td rowspan=1 colspan=1>&gt;11</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>7.4</td></tr><tr><td></td><td rowspan=1 colspan=1>SPECfp 95</td><td rowspan=1 colspan=2>6.70</td><td rowspan=1 colspan=1>300</td><td rowspan=1 colspan=1>&gt;17</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>15</td></tr><tr><td rowspan=1 colspan=2>其它特性</td><td rowspan=1 colspan=2>CISC/RISC混合</td><td rowspan=1 colspan=1>短流水线长L1高速缓存</td><td rowspan=1 colspan=1>最高时钟频率最大片上2级高速缓存</td><td rowspan=1 colspan=1>多媒体和图形指令</td><td rowspan=1 colspan=1>MP机群总线可支持4 CPU</td></tr></table>

表2.8ASCI计划的3个高端 MPP系统特性一览表  

<table><tr><td rowspan=1 colspan=1>特性</td><td rowspan=1 colspan=1>Intel/SNLOption Red</td><td rowspan=1 colspan=1>IBM/LLNLBlue Pacific</td><td rowspan=1 colspan=1>SGI/LANLBlue Mountain</td></tr><tr><td rowspan=1 colspan=1>处理器</td><td rowspan=1 colspan=1>Pentium Pro200 MHz200 Mflops</td><td rowspan=1 colspan=1>POWER3200 MHz 800 Mflops</td><td rowspan=1 colspan=1>MIPS1 Gflops</td></tr><tr><td rowspan=1 colspan=1>系统结构</td><td rowspan=1 colspan=1>NORMA-MPP</td><td rowspan=1 colspan=1>Cluster</td><td rowspan=1 colspan=1>CC-NUMA</td></tr><tr><td rowspan=1 colspan=1>处理器数</td><td rowspan=1 colspan=1>9 216</td><td rowspan=1 colspan=1>4 096</td><td rowspan=1 colspan=1>3072</td></tr><tr><td rowspan=1 colspan=1>峰值速度(T=1012)</td><td rowspan=1 colspan=1>1.8 Tflops</td><td rowspan=1 colspan=1>3.2 Tflops</td><td rowspan=1 colspan=1>&gt;3 Tflops</td></tr><tr><td rowspan=1 colspan=1>存储容量</td><td rowspan=1 colspan=1>594 GB</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>N/A</td></tr><tr><td rowspan=1 colspan=1>磁盘容量</td><td rowspan=1 colspan=1>1 TB</td><td rowspan=1 colspan=1>&gt;5 TB</td><td rowspan=1 colspan=1>N/A</td></tr><tr><td rowspan=1 colspan=1>推出时间</td><td rowspan=1 colspan=1>1997.6</td><td rowspan=1 colspan=1>1998.12</td><td rowspan=1 colspan=1>1998.12</td></tr></table>

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0070/auto/images/eb9039be60d1bffdc23cc85e9794fea0c7cf8e63f2d677bb258bb9dc369757d1.jpg)  
图2.8微处理器系列及其代表性CPU芯片

# \*2.2.2 机群型大规模并行机 SP2

1991年秋,IBM决定涉足于 MPP 的研究,开动了 SP(Scalable POWERpar-allel)计划。1992年2月开始组队,1993年4月就公布了第一个产品 SP1,继之于1994年7月就宣布了SP2。IBM的 SP是比较特殊的,它采用了机群的办法来构筑MPP。到1998 年之前,其在世界上的总装机量超过3000,实属MPP系统成功之例。

设计目标和策略IBM设计 SP系统时提出了如下目标： $\textcircled{1}$ 赶市场：遵循着


<!-- chunk 0002: pages 71-140 -->
Moore定律，为夺性能/价格之冠,产品必须在短期内开发成功； $\textcircled{2}$ 通用：SP必须是个能支持不同的技术和商业应用、流行的编程模式和不同操作模式的通用系统； $\textcircled{3}$ 高性能：SP必须提供整体性能,不仅是处理器速度快，而且存储器和通信系统要快，有优良的编译器和各种库等； $\textcircled{4}$ 有效性：SP必须呈现好的可靠性和可用性,使得用户能够方便地在其上运行商业成品代码。为了满足上述目的,IBM设计小分队采用的策略是：灵活的机群结构;专用互连网络;标准的系统环境；标准的编程模式和有选择的单一系统映像支持。

$\textcircled{1}$ 机群结构：为了达到赶市场和通用的目的,选用机群结构是个关键，其中每个节点都是个RS/6000工作站且各有本地磁盘;每个节点内驻留一个完整的AIX(IBM的Unix);各节点经其I/O总线(非本地存储总线)连向专门设计的多级高速网络。SP系列尽量使用标准的工作站组件,只有不能满足要求时才使用专用的硬件和软件。这样的结构既简单又灵活且系统的规模是可扩放的（从很少的几个节点到数百个节点)。

②标准环境:SP使用标准的、开放式的、分布式Unix环境，它能利用现存的标准软件以进行系统管理、作业管理、存储管理等,所有这些软件IBM工作站AIX操作系统中均有。对于那些AIX环境不能有效执行的应用,SP 提供了一组高性能服务，诸如高性能开关(HPS)、用户级通信协议(US协议）、优化的消息传递库(MPL）、并行程序开发和执行环境、并行文件系统、并行数据库和高性能I/O子系统等。

③标准编程模式：SP系统以标准编程模式支持以下三种应用方式：①串行计算：尽管 SP2是个并行机,但它允许现有的以C、C++和 Fortran编写的串行程序可不加修改地运行在单节点的SP系统上,这是可以理解的，因为机群结构和标准的环境确保了这一点;②并行科技计算:SP现在支持MPL、MPI、PVM、HPF模式,正打算支持共享存储的模式;③并行商用计算：IBM正在并行化一些关键数据库、事务监视子系统,现今IBMDB2数据库系统的并行版本已在 SP2上实现。

④系统可用性：SP系统由上千个部件组成，它们原先是为低价的、规模不大的工作站设计的,现把它们组织在一起必然经常失效。但SP是个机群结构，而机群结构意味着是一个分开的操作系统映像,它和SMP结构驻留在共享存储器中的单一操作系统映像不同(它的OS出错将导致全系统崩溃),机群结构一个节点映像失效不会导致全系统崩溃;另外SP的诸节点均同时连向以太网和高性能开关网,这样一个网络的失效，节点间还可使用另一个网络进行通信；还有 SP的软件基础设施也提供了故障检测、诊断、系统重组和故障恢复等服务。

③ 部分单一系统映像：在一个分布系统中,用户看到的是一些单独的、分开的工作站，真正的单一系统映像是很难实现的，且对某些商业应用它也不是个关键的要求。所以IBM的设计者们，只是在单进入点、单文件层、单控制点和单作业管理系统方面实现了单一系统映像，而在SP系统中并不实现单地址空间。

系统结构SP系统简化框图如图2.9所示。一个SP系统可含 $2 \sim 5 1 2$ 个节点，每个节点有其自己的局存和本地磁盘。所有的节点均连向两个网络：普通的以太网和HPS(High Performance Switch）。以太网虽慢但有很多好处：当HPS失效时，它可作为后援；当HPS正被开发或改进时，仍可利用以太网查错、测试和维持系统运行；此外以太网也可用来系统监视、引导、加载和管理等。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/942e4df6865015a4504a5d9222fb275e4871d88426ef523bc50a82be84fe3c9d.jpg)  
图2.9SP系统结构

①系统互连：高性能开关（HPS)由节点内的开关硬件和开关帧（SwitchFrames)组成。图2.10示出了IBMSP2中所使用的128路高性能开关，其中每帧由一个16路开关板所连接的16个处理节点(No～N15）所组成,8个帧再用一个附加级开关板连接起来(图中细线代表8位的双向链路，而粗线代表4个8位的双向链路）,每一开关板上有两级开关芯片，所以此多级互连网络(MIN)总共有4个开关板。HPS是一个使用此开关的由40MHz时钟驱动的带缓冲的多级Ω互连网络。它使用了虫蚀选路法，一个8位的flits在无竞争时穿过一级（即一个开关芯片）只需5个时钟（即125ns)。因此HPS无竞争时的硬件延迟是很小的，对于512个节点仅875ns。但实际延迟比此值高得多，一个进程发送一个空包给另一个进程至少花40μs,这种消息传递延迟大部分是由软件开销造成的。HPS能提供成对节点之间的双向传输带宽为40MB/s。

②节点结构：SP2有三种不同的节点，分别是宽节点（WideNode）、窄节点（ThinNode)和窄节点1,它们主要差别在于存储器的容量、数据路径宽度和I/O总线的槽数的不同，但是所有的这些节点都使用时钟为66.7MHz的POWER(Performance OptimizedWith Enhanced RISC)-2微处理器。每个处理器有一个32KB的指令高速缓存、256KB的数据高速缓存、指令和转移控制单元、两个定点运算单元、两个各能执行乘-加操作的浮点运算单元。由于定点和浮点运算可同时进行，所以 POWER-2具有4×66.7 Mflops=267 Mflops的峰值速度。POWER-2是个超标量处理器，它使用短指令流水线、先进的转移预测技术和寄存器重命名技术，使得它在每个时钟周期内能执行6条指令：两条取/存指令、两条浮点乘-加指令、一条变址增一指令和一条条件转移指令。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/44c18f7f8b91604ae47f2bf999fef37ed4911abaadffadd3ebdec2a4d03af0d8.jpg)  
图2.10 SP2中的128 路高性能开关(HPS)

I/O子系统和网络接口SP的I/O子系统如图2.11所示，它基本上是围绕着HPS构筑起来的,并用LAN的信关与 SP系统以外的机器相连。SP的节点有4类：主机节点 $( \mathrm { H } )$ 用于用户登录和交互处理;I/O节点主要执行I/O功能(如全局文件服务);信关节点(G)用于连网;计算节点(C)专负责计算。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/4efd3332b17686467549f1d6ead594e0190549ee9d36b670b0a0c7e11d05a95c.jpg)  
图2.11 SPI/O子系统

每个 SP 节点通过网络接口电路(NIC)与HPS 相连,NIC也叫作开关适配器或通信适配器。如图2.12所示,适配器包含-个8MB的DRAM和受控于-个40MHz的i860 微处理器。适配器经微通道接口搭在微通道（Micro（han-nel)上,它是一个标准的I/O总线并用于将外设连向RS/6000工作站和IBMPC机，同时适配器也经过存储和开关管理单元（MSMU:Memoryand SwitchManage-ment Unit)连向 HPS(经由各为8位宽的 IN-FIFO和OUT-FIFO)。除此之外,它还包含·些控制/状态寄存器和用作 i860总线控制器,检查和刷新DRAM。另外，个4 KB 的双向FIFO(BIDI)缓冲器用于连接微通道和 i860总线。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/a002d52cc56687b65d3eb427759733536042be43bd0a39e44071578d3a7ce5ce.jpg)  
图2.12SP通信适配器

参照图2.12来解释一下数据从节点发往HPS的过程：当节点处理器告诉适配器要发送数据时,i860 将直接存储访问DMA(DirectMemory Access)传输所必需的信息(称为Header)写人BIDI,当此Header抵达BIDI之首部时,左部DMA(L-DMA)负责将数据从节点(微通道)传人BIDI;完成时，L-DMA将硬件计数器增--,i860 写另一个Header至右部 DMA(R-DMA),R-DMA 负责将数据从BIDI传至MSMU中的OUT-FIFO,然后再将数据传送至 $\mathrm { H P S } _ { \circ }$

从HPS接收数据是类似的：当数据到达时，MSMU通知i860,它就写一个Header以启动R-DMA,R-DMA 就负责将数据从IN-FIFO传至BIDI;完成时，i860向BIDI写人一个Header,当它抵达 BIDI之首部时,L-DMA抽取此Head-er,并负责将数据从BIDI传至微通道。

系统软件SP系统软件层次如图2.13所示，其核心部分是IBMAIX操作系统。SP沿用了绝大部分RS/6000工作站环境，包括数据库管理系统（如DB2),在线事务处理监视器(如（ICS/6000),系统管理和作业管理,标准操作系统 AIX,Fortran、 $\therefore \ l ( \cdot + \cdot +$ 编译器,数学和工程库(如ESSL)以及上万个串行应用程序等。SP系统只加入了若干新软件和改进了某些现存的软件，它们都是可扩放并行机群系统所要求的。

图2.13SP系统软件层次  

<table><tr><td rowspan=1 colspan=4>应  用</td></tr><tr><td rowspan=1 colspan=4>应用子系统（数据库、事务处理监视器等）</td></tr><tr><td rowspan=1 colspan=1>系统管理</td><td rowspan=1 colspan=1>作业管理</td><td rowspan=1 colspan=1>并行环境</td><td rowspan=1 colspan=1>编译器等</td></tr><tr><td rowspan=1 colspan=4>全局服务（提供单一系统映像）</td></tr><tr><td rowspan=1 colspan=4>有效性服务</td></tr><tr><td rowspan=1 colspan=2>高性能服务</td><td rowspan=1 colspan=2>标准操作系统（AIX）</td></tr><tr><td rowspan=1 colspan=4>标准RS/6000硬件（处理器、存储器、I/O设备、适配器）</td></tr></table>

$\textcircled{1}$ 并行环境:AIX并行环境PE(Parallel Environment)为用户提供了开发和执行并行程序的平台，如图2.14所示，它包含4部分：

并行操作环境 POE（Parallel Operating Environment），消息传递库 MPL（Message Passing Library),可视化工具VT(Visualization Tool)和并行查错 Pdbx(ParallelDebugger)。其中POE用于控制并行程序的执行，它是由一个运行在家用节点(是一个连向 SP节点的RS/6000 工作站)上的划分管理程序(PartitionManager)来控制。家用节点是用户调用并行程序的地方，并行程序作为SP计算节点上--个或多个任务来运行。家用节点提供标准的UnixI/O设备（如Stdin、Stdout和 Stderr),它通过LAN(如以太网)与计算节点进行标准的I/O通信。例如用户从家用节点的键盘上按 $\mathsf { c u r l } + \mathsf { C }$ 键可终止所有的任务，用Printf语句就可在家用节点的屏幕上显示输出。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/04754da7107ddbadc8f7630ad8e2fba56c53f559a1f5cf6637bac78d409203c7.jpg)  
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

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/e38e7eaf09dab43bf1c5d5c53e14cb95b1ac44165891dd666079c3c24454303c.jpg)  
图2.15（OW的一般结构  
图2.16（OW的软件结构

<table><tr><td rowspan=1 colspan=1>并行应用程序</td><td rowspan=1 colspan=1>并行工其包</td></tr><tr><td rowspan=1 colspan=1>并行程序设计环境、通信原语库</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=2>通信协议</td></tr><tr><td rowspan=1 colspan=2>操作系统</td></tr><tr><td rowspan=1 colspan=2>处理机与高速通信部件</td></tr></table>

为什么发展COW和前面所介绍的对称多处理机 SMP和大规模并行机

MPP相比，COW在实用上具有一些明显的优点： $\textcircled{1}$ 投资风险小：用户在购置传统巨型机或MPP系统时，总是担心使用效率不高和性能发挥得不好，如果购置后在一定程度上确实出现此问题，就相当于搁置或浪费了大批资金，但COW不存在此问题，因为即使COW在技术上不够先进，但每台高性能的工作站仍可照旧使用，不会浪费资金； $\textcircled{2}$ 编程方便：用户无需学用新的并行程序设计语言（如并行C、并行 $\ b { \mathbb { C } } + \ b { \mathbb { + } }$ 、并行Fortran等），只要利用所提供的并行程序设计环境，在常规 ${ \mathbb C } \mathrm { , } { \mathbb C } + +$ 和Fortran等程序中相应的地方插人少量的几条原语，即可使这些程序在COW上运行，这一点是最受用户欢迎的； $\textcircled{3}$ 系统结构灵活：用户将不同性能的工作站使用不同的体系结构和各种互连网络构成同构或异构的工作站机群系统，从而可弥补单一体系结构适应面窄的弱点，可更充分地满足各类应用要求； $\textcircled{4}$ 性能/价格比高：一般一台巨型机或MPP都很昂贵(费用常以几百万元、几千万元计),而一台高性能工作站相对便宜(费用仅以几万元或十几万元计），一个COW系统从浮点运算能力来看，虽然每台工作站只有几Mflops到几十Mflops,但一群工作站的总体运算性能可高达Gflops的量级，能接近一些巨型机的性能，但价格却低了很多； $\textcircled{5}$ 能充分利用分散的计算资源：当个人工作站处于空闲状态时,COW可在空闲时间内给这些工作站加载并行计算任务，从而工作站资源可得到充分利用； $\textcircled{6}$ 可扩放性好：用户可根据需要增加工作站的数目，以高带宽和低延迟的网络技术支持获得高的加速比，从而获得应用问题的高可扩放性。

COW的关键技术实现工作站机群需要解决的主要问题是通信性能和并行编程环境。因为组成COW的硬件环境中工作站的性能已相当高，且还在不断的提高，相对而言工作站性能不是关键问题;相反，负责数据通信的互连网络却是一项关键技术，因为COW系统中并行计算时各工作站之间需要经过互连网络交换数据，某些工作站上的程序所需要的数据也往往要通过网络获取或提交。如果网络通信延迟时间很长，再加上用于通信的软件开销(此部分不可忽视)可能就限制了COW技术对某些问题的适应性。近几年来网络技术发展很快,ATM给予COW技术强大的支持,其156Mb/s的传输速率以及高带宽的特性保证了数据通信的高速进行；另外 IEEE/ANSIP1596互连标准 SCI(ScalableCoherenceInterface)可支持多达64K个节点互连,并能实现二级高速缓存一致性协议，传输速率可以达到1Gb/s,从而可很好地支持工作站的互连。

伴随高速网络而产生的另一关键技术是工作站到网络的主机接口网络接口的设计，它应尽量保持网络的传输速度与主机数据收发速度相匹配,其中增加高速缓存或采用DMA是可供选择的两种技术。网络接口使工作站可以利用网络传输数据，但也增加了通信延迟,它占用工作站CPU时间，从而影响了COW的性能。一般,一次通信时间延迟可如图2.17所示，其中D为操作系统调度时间,A用于分配缓冲，C用于拷贝数据到系统缓冲区,S为启动发送/接收时间，T为链路传输时间,F用于定位中断源，X用于从接收队列获取数据。一般减少延迟的方法有： $\textcircled{1}$ 设计精简通信协议以减少数据移动的次数和协议处理时间； $\textcircled{2}$ 采用主动消息(ActiveMessage)携带数据处理命令以重叠计算和通信； $\textcircled{3}$ 定制通信处理单元以消除通信对工作站CPU的依赖。

另外，COW要走向实用必须为用户提供一个良好使用环境和一套完善的工具系统，主要包括： $\textcircled{1}$ 并行编程环境，如一些通信原语库、多种编程语言( $\mathrm { L } \mathbf { x } - \mathrm { \partial }$ press、PVM、Linda、 $\boldsymbol { \mathrm { P _ { + } } }$ 、MPI)的支持以及并行编译器等； $\textcircled{2}$ 可视化监视/调试器（如 Express 的 domtool、基于PVM的 XPVM等）; $\textcircled{3}$ 并行图形库（如基于Express的Plotix等）; $\textcircled{4}$ 并行文件系统和数据库，以适应开展分布式事务处理的研究与开发。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/3665163e00e50fcde518804dead9745a79103989a7effaa682a32833e0ac5865.jpg)  
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

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/dfc58e3ae9565d4011bf334c12a88a710af9629b15170f38e5c9d99272b2443f.jpg)  
图2.19两类文件系统对照

(a）中央文件服务器系统；（b)xFS无服务器网络文件系统

$\textcircled{1}$ 廉价冗余磁盘阵列RAID(Redunant Array of Inexpensive Disks):无工作站文件系统能用来生成软件RAID以提供高性能和高可用性。现今,xFS使用单奇偶校验磁盘条(Striping)。一个文件数据块在多个存储服务器节点上按条划分,在另一节点上有奇偶校验块。如果一个节点失效,失效磁盘的内容,可利用其余盘和奇偶盘之异或操作重建之。RAID的缺点是所谓“小-写问题”(Small-Write Problem)：即如果一次写所修改的仅是条的一部分而不是整个条，则系统必须重新计算奇偶校验而导致大的开销。xFS使用登录条(Log-based striping)的方法解决此问题：每个客户首先将写接合到各用户的登录(Log)上(它就是记录所有写操作的一个存储缓存器);然后此登录采用登录段(Logsegment)提交给磁盘,每个段系由K-1登录片(LogFragment)组成,它与奇偶校验片一道送向K个存储服务器。但此法对大型多服务器机群也有问题：很多发往存储服务器的小片可能使登录存储器很大；很多客户同时写登录会造成竞争。xFS采用将存储服务器分成一些称之为条组(StripeGroup)的子集的办法来解决此问题。如图2.20所示,8个服务器分成2组，每组4个服务器。其中，A条组中，第一段由片1,2,3组成,相应的奇偶校验片为p;第二段由片4,5,6组成，相应的奇偶校验片q。B条组中情况类似。这样客户1和客户2可同时分别向各自组写人登录而不会冲突。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/a93721b4912b0f3de4c77c6dd8792664971ec1f66cb5ef91f9742c4c1d61124e.jpg)  
图2.20 $\tt { x F S }$ 中的条组方法

②协同文件缓存(Cooperalive File（aching)：协同文件缓存的思想很简单：机群每个客户节点都辟出--部分作为文件(高速)缓存。协同文件缓存算法利用所有这些存储器生成一个大的、全机群上的文件缓存。当一个客户未找到其本地文件缓存时，不需要到磁盘中去找，只要到另个客户的存储器中去找该数据。如图2.21所示，文件稳定地存在服务器磁盘中，习惯上这些文件也缓存至客户存储器中、客户本地磁盘中和服务器的存储器中。xFS也允许一个文件缓存在远地存储器中。有两种协同文件缓存算法：贪心转发法(Greedy Forward-ing)和N-概率转发法(N-Chance Forwarding)。贪心转发法工作原理是：一个访问文件和客户首先试用其本地高速缓存,如果数据块不在那里，它便将请求转发给服务器。服务器先搜索其本地高速缓存，若命中，便将数据返给客户并维护其高速缓存目录;若未找到，服务器便查阅其高速缓存目录并把请求转发给保存所请求数据的客户，然后该客户便直接将数据返回给请求的客户。贪心转发法的优点是实现简单,但其缺点是同一数据块可能被很多高速缓存所复制。当一客户第一次读一个数据块时,此块从服务器磁盘中读出并将其缓存在服务器高速缓存和客户高速缓存中，而另一读同一块的客户将把它缓存在其本地文件高速缓存中。这种重复降低了协同高速缓存的有效空间，因而也增加了命不中的比率,而且使高速缓存一致性管理更加困难。N-概率转发法是贪心转发法的一般化,它采用缓存一个数据块仅于一个客户高速缓存中的办法避免重复。这样的数据块叫作单块(Singlet)。当一个客户从另一客户的高速缓存中取出一块时，此块就被丢掉，并发一条消息给服务器告诉它此块已被移去。单块所带来的问题是，如果一个单块被丢掉，它就给后来的数据块腾出了位置，此单块也就从整个协同高速缓存中丢失。N-概率转发法可缓解此问题，只要客户高速缓存未满，它和贪心转发法完全一样。当任一客户的本地高速缓存满时，就要丢掉一个数据块，此时客户首先要检查一下此块是否为单块：如不是，客户就丢掉它；如是,客户就将块循环计数器置为N，并发送该块给一个随机的客户。如果第二个客户稍后要丢掉这一块,它就将循环计数器减一，并发送该块给另一客户。此过程一直继续到循环计数器为零,这时就把该块丢掉。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/d1ed05bfd0734bc463270d83ff5df253f667e7ec96d6bd6e4875767f4468df93.jpg)  
图2.21客户/服务器机群中缓存文件的不同方式

③分布式管理：xFS的文件系统管理功能是全分布的，它使用了位于多个节点上的多管理器(Manager)。为了理解如何达到分布管理,参照图2.22来看一下 xFS中一个文件的读过程：当一个客户试图读一个文件块时，它发送一个带有文件(路径)名和位移(Name& Offset)的请求,在xFS的目录(Dir)中使用文件名客户就能找到文件的索引(Index),用此索引客户搜索本地高速缓存（U-nix Cache),如果数据块在其中(命中),则数据就被读出;如果高速缓存未命中，那么客户用索引号查阅管理器映射表(ManagerMap)，此表指明哪个物理节点管理哪组索引号，也就是正确的管理者在哪里，于是索引和位移信息就经网络发正确的管理者，管理者留意诸如数据块是否在磁盘中或被缓存、块的精确位置、高速缓存块是否是一致的某信息。如果块被缓存在某一客户的本地高速缓存中且是一致的,那么管理者就转发读请求给那个客户,客户就从其本地高速缓存中读取数据并直接发给原先的客户；如果数据块不在协同高速缓存中，管理者就再查阅imap表以找到索引节点(inode),它包含了文件所有数据块的地址，此地址就可用来找到正确的存储服务器，于是数据块就可从那里读出并传给原先请求的客户。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/d8a6b5d6bbe2fa8bc4afd7d42feb2bd78e47447cb2ce92fe9f717412e7f4aa0c.jpg)  
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

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/bb0f3d2bdbbabdaa955daad9ef0f4e56331c61ddca0029f66be84b36f13cda32.jpg)  
图2.23曙光1号系统板

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/bb3c0d269ea1debde76731814b5039a26088d0602ef6009db56c5ad0927cd6d5.jpg)  
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

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/a26853c5c11cdb5cb7b5cf3d998df25914b59782907e6ea504150c862cff5e29.jpg)  
图2.26曙光1号软件层次的圆形表示

# 2.4.2大规模并行处理系统：曙光-1000

曙光-1000 是一台分布存储的大规模并行处理·MPP(Massively Parallel Pro-cesing)系统,它突破了MPP中一些技术关键,采用20世纪90年代大量先进技术,其峰值速度达25亿次,可广泛应用于科学工程计算、气象预报、石油勘探、地震数据处理和银行等商务处理中。其技术特点是： $\textcircled{1}$ 良好的可扩放性,包括硬件和软件两个方面； $\textcircled{2}$ 大量的节点、强大的计算能力和大容量存储器; $\textcircled{3}$ 自行设计的稳定可靠的虫蚀通信芯片； $\textcircled{4}$ 使用带流控的消息传递协议； $\textcircled{5}$ 优良的优化并行编译器； $\textcircled{6}$ 先进的并行编程环境、并行查错工具、自动并行化工具和包括 PVM、MPI、Express、NX 等的编程工具。曙光-1000 整体性能达到 20 世纪90 年代初期世界先进水平,其主要技术指标是： $\textcircled{1}$ 使用 $6 \times 6$ 的二维网孔连接,共36个节点,其中计算节点32个，服务节点2个和I/O节点2个； $\textcircled{2}$ 峰值速度达单精度2.56 Gflops,双精度1.92 Gflops,实际速度为1.58 Gflops; $\textcircled{3}$ 存储容量为每个节点32MB,共1GB;④硬盘容量可超过5GB;③二维网孔连接、虫蚀选路，总通信容量为4.8GB/s;⑥计算节点和通信网络间带宽为2.8GB/s;?支持并行C、C++和Fortran,提供并行优化重构工具Port和自动并行化工具Autpar、动态监视和分析工具ParaVision以及单计算节点上源代码与目标代码的优化工具；③基于Unix的分布式并行操作系统;③提供并行程序查错环境NDB;①提供并行程序设计和运行环境 PVM、MPI、Express、NX 和 $\mathrm { P } _ { 4 }$ 等。

硬件系统曙光-1000是一台分布存储、消息传递的MPP系统,如图2.27所示，在6×6二维网孔的每个格点上有一个虫蚀路由芯片WRC（WormholeRouting Chip)和一个计算节点(或服务节点或I/O节点),系统监视器(Monitor)负责系统初始化和硬件故障诊断,用户工作平台可以是工作站 SUN Sparc-Ⅱ(或其它工作站)也可以是终端(它们都称为前端机),它们通过 $1 0 \ \mathrm { M b / s }$ 的以太网连向服务节点。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/5a533eb3ea6eb2fcd23fca8a8899ebf6ad900db2fae9e9e890c2ab149f12698c.jpg)  
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

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/78ce665c88cbdba66cd7d4806b04a81f66c0ca2e064d36ad189e21c20043b17c.jpg)  
图2.28曙光-2000体系结构框图

$\textcircled{2}$ 通信子系统：曙光-2000采用二维网孔互连，使用“虫蚀"选路，从而具有可扩放性、低延迟、高带宽、低处理器开销和可靠灵活之特性。在二维网孔中，点与点之间采用基于消息包的固定路由、无缓冲的传输机制，点与点之间的通信带宽保持常数，不依赖于拓扑中两节点的物理位置。WRC芯片有10个通道，如图2.29所示，每个通道16位数据宽度， ${ 5 0 ~ \mathrm { M H z } }$ 频率，数据带宽 $1 0 0 ~ \mathrm { M B / s } _ { \circ }$ 芯片内部有X、Y两个路选择控制器和4级16位数据缓冲器。曙光-2000节点通过一块PCI网络接口板与底板相连,其中PMI-16接口板由PCI的DMA引擎控制数据传输,PMI-960接口板由一个Intel960协处理器负责DMA传输和协议控制。接口板和节点内存之间采用DMA方式传输，减少了消息传递中处理器的开销。

![](../chunks/并行计算 结构·算法·编程 (陈国良编著, 陈国良, (计算机), 陈国良编著, 陈国良, 陳國良) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/0f31e45be117c51b1af25ef5b81f211cfb147088d09d7519a79ec2f34f23b77b.jpg)  
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
