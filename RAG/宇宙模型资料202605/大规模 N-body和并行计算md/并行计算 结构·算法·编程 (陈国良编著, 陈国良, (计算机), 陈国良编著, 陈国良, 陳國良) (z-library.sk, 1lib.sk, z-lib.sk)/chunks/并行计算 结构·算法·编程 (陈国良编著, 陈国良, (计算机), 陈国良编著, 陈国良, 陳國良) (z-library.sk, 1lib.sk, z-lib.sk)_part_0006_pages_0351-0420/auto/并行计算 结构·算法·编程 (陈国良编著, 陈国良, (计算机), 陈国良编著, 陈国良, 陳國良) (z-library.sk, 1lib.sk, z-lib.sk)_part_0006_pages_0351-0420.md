# 第十四章 分布存储系统并行编程

从并行程序设计的角度来看，分布存储系统的主要特点是：系统通过互连网络将多个处理器连接起来，每个处理器均有自己的局部存储器，所有的局部存储器就构成了整个地址空间;整个地址空间有局部和全局两种编址方式，全局编址方式是指系统的所有局部存储器统一编址，用户程序空间是一个统一的全局地址空间，其中远程存储器的访问与局部存储器的访问一样用指令来完成，其指令地址由处理器号和局部存储器地址所组成。局部编址方式是系统中各局部存储器单独编址，用户程序空间是多地址空间,远程存储器的访问要通过调用消息传递库程序来实现的。

上述的特点，导致了分布存储系统的两种并行编程模型：消息传递模型和数据并行模型。实现消息传递有 SPMD(单程序多数据流)和MPMD(多程序多数据流)两种模式;实现数据并行有 SIMD(单指令多数据流)和 SPMD 两种模式。在分布存储的SIMD体系结构上可以实现 SPMD模式的数据并行;在分布存储的 MIMD体系结构上可以实现 SPMD模式的数据并行,也可以实现MPMD模式的消息传递。

本章首先讨论消息传递的并行编程,着重讨论MPI而顺便介绍一下PVM 并行编程环境;然后讨论数据并行编程,着重讨论HPF 而穿插提及一下Fortran 90。

# 14.1 基于消息传递的并行编程

所谓基于消息传递的并行编程,是指用户必须显式地通过发送和接收消息来实现处理器之间的数据交换。这种编程方式是大规模并行处理机MPP 和工作站机群COW采用的主要编程方式。在这种并行编程中，每个进程均有自己独立的地址空间,一个进程不能直接访问其它进程中的数据,这种远程访问必须通过消息传递来实现。因为消息传递的开销比较大，所以它主要用来开发大粒度和粗粒度的并行性。

根据问题分解的两种形式，消息传递并行性的开发也有两种形式：域分解形式,即将一个大的问题区域分解成若干个较小的问题区域,然后对其并行求解;函数分解(也有人称为功能分解)形式,即将一个大的问题分解成若干个子问题，然后对其并行求解。相应于这两种形式，就有所谓SPMD编程和MPMD编程两种模式。

# 14.1.1 SPMD并行程序

基于域分解的思想开发出的并行程序，通常组织成SPMD形式。SPMD就是同一程序复制到各个处理器上，而不同的数据分布在不同的处理器上。这样在系统中各处理器均运行相同的程序，但对不同的数据执行操作。在大量的处理器上运行用户软件,为了减少管理指令流的复杂性,加大并行粒度,用 SPMD程序代替SIMD程序是很自然的。

设计SPMD形式的消息传递程序的主要步骤是： $\textcircled{1}$ 数据划分：尽量考虑负载平衡、存储空间的均衡使用以及减少处理器之间的通信； $\textcircled{2}$ 优化通信：尽量提高计算/通信比,数据就地使用和合并短消息成一个长消息进行传输； $\textcircled{3}$ 全局操作：将各处理器之局部结果组合起来形成整个问题的解,像这样的操作包括全局同步、广播、归约、前缀运算、聚集/散射等。

编写 SPMD形式的程序有两种方式：主机/节点(Host/Node)式和无主机(Hostless)式,兹分述如下：

主机/节点结构在此结构中，一个应用程序由两部分组成：一是主机程序，二是节点程序。主机程序运行在控制节点上,节点程序运行在所有的计算节点上。这种形式的程序，实际上是一个主机程序控制一组以SPMD方式执行的节点程序。主机程序的功能是： $\textcircled{1}$ 申请和释放处理器,加载节点程序； $\textcircled{2}$ 执行I/O和处理用户界面； $\textcircled{3}$ 发送数据给各节点处理器,并收集各处理器的计算结果。节点程序的功能是： $\textcircled{1}$ 接收来自主机的输入信息； $\textcircled{2}$ 完成各自的局部计算,施行计算节点间的通信； $\textcircled{3}$ 回送计算结果给主机。主机/节点结构的主要优点是： $\textcircled{1}$ 易于并行编程：欲将一个已有的串行程序修改成主机/节点形式的并行程序时，原有程序中的I/O与用户界面部分(代码量大但运行时间短)可以完全不变，而只需并行化计算部分(代码量小但运行时间长),这样开发并行程序代价较低； $\textcircled{2}$ 充分利用主机的特殊能力：在很多MPP系统中,计算节点通常只提供最基本的操作系统功能，而图形功能、I/O功能和数据库接口功能等通常远不如控制节点强,对于需要图形功能或数据库接口功能的应用软件来说,主机/节点结构可以充分利用主机功能强的优势。但主机/节点结构也有些不足,主要是： $\textcircled{1}$ 调试困难：采用主机/节点结构，一般不允许节点程序直接进行自己的I/O,这样当用户试图用打印信息来定位错误时,用户必须同时修改主机和节点程序,以便两者协调输出所需之信息；②维护困难：因为主机/节点结构涉及到两类节点，当两类节点结构上(字节次序、最高有效位之位置、数据类型长度不一致等)有差异时，两个程序之间交换数据产生困难,给维护增加了难度；③可移植性差：因为主机/节点程序不能直接在串行机上执行，所以用户常常需要为一个应用软件保持一个并行版本和一个串行版本，用户负担过大，给程序移植带来困难。

无主机结构在此结构中，一个应用程序整个地运行在计算节点上，而控制节点不起上节所说的主机节点的作用，所运行的实际上是一个系统提供的通用$\mathbf { I } / \mathbf { O }$ 服务程序，它为计算节点提供I/O服务和计算节点所不具备的操作系统请求服务。在这种结构中，程序控制也是在计算节点上完成的。无主机结构的主要优点是： $\textcircled{1}$ 易于程序开发、维护和移植：因为只涉及一类节点，用户只需写一种应用程序； $\textcircled{2}$ 程序较易调试：因为程序可以在计算节点上，直接使用标准的I/O功能进行调试； $\textcircled{3}$ 程序的正确性易于保证：因为在无主机结构上书写的并行程序,可以不加修改或少量修改即可在串行机上运行。

由于上述优点,无主机结构已成为编写 SPMD程序的主要方式。

# 14.1.2 MPMD并行程序

基于函数分解思想开发出的并行程序,通常组织成MPMD形式。MPMD就是每个处理器执行不同的代码副本、各自对数据完成不同的运算。在诸如事务处理的应用中,由于各子功能本身固有的异构性;以及在异构网络环境下，由于各计算机资源差异性，用MPMD结构的程序是很合适的。

设计MPMD形式的消息传递程序的主要步骤是： $\textcircled{1}$ 子问题划分：尽量考虑各处理器负载均衡和充分利用各处理器的独特能力,在全系统范围内合理分配各子问题于不同处理器上； $\textcircled{2}$ 确定子问题之间的相互作用方式。

实现子问题之间相互作用方式有两种：数据流方式和客户/服务器方式，兹分述如下：

数据流方式在此方式的 MPMD程序中，用户将问题分解为各不相同的子问题；根据子问题的相关性来组织并行，按数据驱动(Data-Driven)的方式决定并行执行的先后次序。这种方式主要应用于异构型计算环境中的应用软件的开发。

客户/服务器方式在此方式的 MPMD程序中，用户将一些典型的不同的子问题求解作为相应的服务进程分布于各个计算节点上；整个问题的求解就归结为客户对各个服务器的一系列服务请求。这种方式主要应用于某类特殊的应用领域。在这些应用领域中，将一些普遍性的子功能(例如数据库应用中的插入、删除和查询等)作为服务进程,可以大大减轻用户重复开发具体应用软件的负担。

客户/服务器方式是一种需求驱动(Demand-Driven）（数据流方式是一种数据驱动）。用户所请求的服务可以是信息服务、计算服务或资源服务。客户/服务器方式的显著特点是非对等性，即客户与服务器地位不对等，服务器拥有客户所不具有的硬件资源和运算能力，服务器提供服务，客户请求服务。这种方式特别适合于子功能比较通用的应用领域。一个客户/服务器方式的MPMD程序示意图如图14.1所示。

![](images/f1659d525ca3694f6dd51f31c0d504ec94210760121ecb02b8c131d15f8b8fc4.jpg)  
图14.1客户/服务器方式的MPMD程序

# 14.2 MPI并行编程

在消息传递库方法的并行编程中，一组进程所执行的程序是用标准串行语言书写的代码加上用于消息接收和发送的库函数调用。其中,MPI(MessagePassing Interface)就是1994年5月发布的一种消息传递接口。它实际上是一个消息传递函数库的标准说明，吸取了众多消息传递系统的优点，是目前国际上最流行的并行编程环境之一（其它的系统包括P4、PVM、Express和PARMACS等）。MPI具有许多优点：具有可移植性和易用性；有完备的异步通信功能；有正式和详细的精确定义，因而为并行软件产业的增长提供了必要的条件。

在基于MPI编程模型中，计算是由一个或多个彼此通过调用库函数进行消息收、发通信的进程所组成。在绝大部分MPI实现中，一组固定的进程在程序初始化时生成，一个处理器生成一个进程。这些进程可以执行相同或不同的程序（相应地称为SPMD或MPMD模式）。进程间的通信可以是点到点的，也可以是群体的（Collective)。或许MPI最重要的特性就是使用了称之为通信体(Communicator)的机构,允许程序员定义一种封装内部通信结构的模块。所谓通信体就是一个进程组(Process Group)加上进程活动环境(Context),其中进程组就是一组有限和有序进程集合。所谓有限意即组内包含有限数目的n个进程;所谓有序意即n个进程依次按0,1,,n-1整数定序(Ranked)。MPI中的进程活动环境(Contexts),也称为上下文,是系统指定的超级标记(Supertag)，它能安全地将彼此相互冲突的通信区分开来。每个通信体都有一个不同的、系统指定的进程活动环境，一条在一个进程活动环境中发送的消息不能在另一个进程活动环境中被接收。通信体的作用，请参阅习题14.1。

# 14.2.1最基本的 MPI

MPI是个复杂的系统，它包含了129个函数(根据1994年发布的MPI标准)。事实上,1997年修订的标准,称之为MPI-2,已超过200,目前最常用的也有约30个。然而我们可以只使用其中的6个最基本的函数就能编写一个完整的 MPI程序去求解很多问题。这6个基本函数,包括启动和结束计算,识别进程以及发送与接收消息：

MPI_INIT: 启动MPI计算MPI_FINALIZE: 结束MPI计算MPI_COMM_SIZE: 确定进程数MPI_COMM_RANK: 确定自己的进程标识符MPI _SEND: 发送一条消息MPI_RECV: 接收一条消息

函数的功能及其参数描述在图14.2中,其中标号IN、OUT和 INOUT分别指明函数使用但不能修改参数、函数不使用但可修改参数以及函数既可使用也可修改参数。

MPI_INIT(int \*argc,char \* \* \* argv)   
Initiate a computation . argc,argv are required only in the C language binding, where they are the main program's arguments.

MPI_FINALIZE() Shut down a computation .

MPI_COMM_SIZE(comm,size) Determine the number of proceses in a computation .

IN comm communicator(handle) OUT size number of processes in the group of comm(integer)

MPI_COMM_RANK(comm,pid).

Determine the identifier of the current process.

IN comm communicator(handle) OUT pid process id in the group of comm(integer)

MPI_ SEND(buf,count,datatype,dest,tag,comm).   
Send a message.

IN buf address of send buffer(choice) IN count number of elements to send (integer≥0) IN datatype datatype of send buffer elerments(handle) IN dest process id of destination process(integer) IN tag message tag(integer) IN comm communicator(handle)

MPI_RECV(buf,count,datatype,source,tag,comm,status)   
Receive a message . OUT buf address of receive buffer(choice) IN count size of receive buffer,in elements(integer $\mathtt { > 0 }$ ） IN datatype datatype of receive buffer,elements(handle) IN source process id of source process,or MPI_ANY_SOURCE(integer) IN tag message tag,or MPI_ANY_TAG(integer) IN comm communicator( handle) OUT status status object(status)

只使用6个基本函数中的4个即可写出如下一段MPI程序：

program main   
begin MPI_INIT() $\big / \ast$ 启动计算 $\yen 7$ MPI_COMM_SIZE(MPI_COMM_WORLD,count) $\big / \big \langle \big \varkappa$ 找进程数 $\yen 7$ MPI_COMM_RANK(MPI_COMM_WORLD,myid) $\big / \ast$ 找自己的 $\yen 12$ print("I am",myid,"of",count) $\big / \big | \big | \big |$ 打印消息 $\yen 7$ MPI_FINALIZE（） $\big / \ast$ 结束计算 $\yen 7$   
end

其中,MPI_COMM_WORLD是一个缺省的进程组,它指明所有的进程都参与计算。

MPI不是一个独立的、自包含的软件系统,MPI进程是重量级、单线程的进程,MPI标准并不指明如何启动并行计算，它可通过命令行参数指明应被生成的进程数目，然后按SPMD方式或MPMD方式执行程序。MPI函数库本身是与语言无关的，也就是说,库函数的描述可以使用C语言、Fortran语言或其它的语言。目前 MPI库函数提供了C语言和 Fortran 语言描述(称为LanguageBinding)。在C语言描述中,函数名均冠以MPI前缀,且其首字母需大写。返回的状态值是整数；成功完成的返回代码是MPI_SUCCESS；失败时也会定义一组错误代码。编译时的常数均须大写且被定义在文件mpi.h中,mpi.h在任何需调用MPI的程序中必须被包含进来。句柄(Handles)由定义在mpi.h中的特殊类型所表示。具有类型IN的函数参数由值传送；具有类型OUT和 IN-OUT的函数参数由引用传送(例如指针）。MPI的数据类型定义成C和Fortran语言的数据类型，如表14.1所示。

在Fortran语言描述中,函数名均冠以MPI前缀，且均须大写。函数返回代码由一个附加的整数变量表示之;成功完成的返回代码是MPI_SUCCESS；失败时也会定义一组错误代码。编译时的常数均须大写且被定义在文件mpif.h中,它在任何需调用MPI的程序中必须被包含进来。所有句柄均具有类型 IN-TEGER。MPI的数据类型如表14.1所示。

表14.1 MPI中的数据类型一览表  

<table><tr><td rowspan=1 colspan=1>MPI(C Binding)</td><td rowspan=1 colspan=1>C</td><td rowspan=1 colspan=1>MPI(Fortran Binding)</td><td rowspan=1 colspan=1>Fortran</td></tr><tr><td rowspan=1 colspan=1>MPI_BYTE</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>MPI_BYTE</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>MPI_CHAR</td><td rowspan=1 colspan=1> signed char</td><td rowspan=1 colspan=1>MPI_CHARACTER</td><td rowspan=1 colspan=1>CHARACTER(1)</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>MPI_COMPLEX</td><td rowspan=1 colspan=1>COMPLEX</td></tr><tr><td rowspan=1 colspan=1>MPI_DOULBE</td><td rowspan=1 colspan=1>double</td><td rowspan=1 colspan=1>MPI_DOUBLE._PRECISION</td><td rowspan=1 colspan=1>DOUBLE1PRECISION</td></tr><tr><td rowspan=1 colspan=1>MPI_FLOAT</td><td rowspan=1 colspan=1>float</td><td rowspan=1 colspan=1>MPI_REAL</td><td rowspan=1 colspan=1>REAL</td></tr><tr><td rowspan=1 colspan=1>MPI_ INT</td><td rowspan=1 colspan=1>int</td><td rowspan=1 colspan=1>MPI_INTEGER</td><td rowspan=1 colspan=1>INTEGER</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>MPI _LOGICAL</td><td rowspan=1 colspan=1>LOGICAL</td></tr><tr><td rowspan=1 colspan=1>MPI_LONG</td><td rowspan=1 colspan=1>long</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>MPI_LONG_DOUBLE  ：</td><td rowspan=1 colspan=1>long double</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>MPI_PACKED</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>MPI_PACKED</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>MPI_SHORT</td><td rowspan=1 colspan=1>short</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>MPI_UNSIGNED_CHAR</td><td rowspan=1 colspan=1>unsigned char</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>MPI一UNSIGNED</td><td rowspan=1 colspan=1>unsigned int</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>MPI_UNSIGNED_LONG</td><td rowspan=1 colspan=1> unsigned long</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>MPI _UNSIGNED_SHORT</td><td rowspan=1 colspan=1> unsigned short</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

# 14.2.2群体通信

MPI并行程序中经常需要一些进程组间的群体通信(CollectiveCommunica-tion),包括：①路障(Barrier)：同步所有进程;②播送(Broadcast）：从一个进程发送一条数据给所有进程；③收集(Gather)：从所有进程收集数据到一个进程；④散射(Scatter)：从一个进程散发多条数据给所有进程；③归约(Reduction）：包括求和、求积等。这些函数的功能及其参数描述在图14.3中，播送、收集和散射的几何意义示于图14.4中。

MPI_REDUCE和 MPI_ALLREDUCE 均执行归约操作,它们组合每个进程中输入缓冲器中的值,返回组合后的值于单一根进程的输出缓冲器中（MPI_REDUCE)或者于所有进程的输出缓冲器中（MPI_ALLREDUCE)。组合所使用的操作包括最大和最小（MPI_MAX和MPI_MIN);求和与求积（MPI_SUM和 MPI_PROD);逻辑与、逻辑或以及异或(MPI_LAND、MPI_LOR 和MPI_LXOR);按位与、按位或以及按位异或(MPI_BAND、MPI_BOR 和 MPI_BXOR)。

MPI_BARRIER(comm)   
Global synchronization . IN comm communicator( handle)   
MPI_BCAST(inbuf,incnt,intype,root,comm）.   
Broadcast data from root to all processes . INOUT IN incnt number of elements in input buffer(integer) IN intype datatype of input buffer elements(handle) IN root process id of root process(integer) IN comm communicator( handle)   
MPI_ GATHER(inbuf,incnt,intype,outbuf,outcnt,outtype,root,comm)   
MPI_ SCATTER(inbuf,incnt,intype,outbuf,outcnt,outtype,root,comm)   
Collective data movement functions . IN inbuf address of input buffer(choice) IN incnt number of elements sent to each(integer) IN intype datatype of input buffer elements(handle) OUT outbuf address of output buffer (choice) IN outcnt number of elements received from each(integer) IN outtype datatype of output buffer elements(handle) IN root process id of root process(integer) IN comm communicator( handle)   
MPI_REDUCE(inbuf,outbuf,count,type,op,root,comm)   
MPI_ALLREDUCE(inbuf,outbuf,count,type,op,comm)   
Collectiue reduction functions . IN inbuf address of input buffer(choice) OUT outbuf address of output buffer(choice) IN count number of elements in input buffer(integer) IN type datatype of input buffer elements(handle) IN op operation;see text for list(handle) IN root process id of root process(integer) IN comm communicator(handle)

![](images/e2f90925660e69455d982317d0b5fecff71ac33f7231923115e5daa41adf36db.jpg)  
图14.4MPI播送、收集和散射的几何意义

# 14.2.3通信体

通信体(Communicator)提供了MPI中独立的安全的消息传递。不同的通信库使用独立的通信体,它隔离了内部和外部通信，避免了在通信库被调用和退出时的同步,也保证了在同一通信体的通信操作互不干扰。

MPI提供的通信体函数概括在图14.5中:①MPI_COMM_DUP:它生成一个新的通信体,具有相同的进程组但新的上下文,这可确保不同目的通信不会混淆； $\textcircled{2}$ MPI_COMM_SPLIT:它生成一个新的通信体,但只是给定进程组的子集，这些进程可相互通信而不必害怕与其它并发计算相冲突;③MPI_INTERCOMM_CREATE:它构造一个进程组之间的通信体,该通信体链接两组内的进程;④MPI_COMM_FREE:它用来释放上述三个函数所生成的通信体。

MPI_COMM_DUP(comm,newcomm) Create new communicator : same group , new context . IN comm communicator(handle) OUTnewcommcommunicator(handle) MPI_ COMM_ SPLIT(comm,color,key,newcomm) Partion group into disjoint subgroups. IN comm communicator(handle)

IN color subgroup control( integer) IN key process id control(integer) OUT newcomm communicator(handle)

MPI_INTERCOMM_CREATE(comm,leader,peer,rleader,tag,inter) Create an intercommunicator.

![](images/f60465d6da1512ea83bd5c275b0b8b59f7d482f7e4ae1422d4423b13195a25ad.jpg)  
图14.5MPI通信体函数

图14.6示出使用MPI_COMM_SPLIT生成新的通信体方法,其中第一个通信体是个8进程组，使用myid%3着色法并调用MPI_COMM_SPLIT(comm,color,myid,newcomm)就把原通信体劈成3个不相交的进程组。

![](images/ea8afc0dade7b2e0ce148ea9e21c70903a5af59b67cb81ea284883be7e4a96dc.jpg)  
图14.6使用MPI_COMM_SPLIT生成新通信体

![](images/549ad3be716f7d90f68261690c4e663503d18d205400df2a88f588d9e8d21640.jpg)  
图14.7在两进程组之间建立组间通信体

图14.7示出了在两进程组之间建立了一个组间通信体，其中顶上是原8进程组,这是一个MPI_COMM_WORLD;调用MPI_COMM_SPLIT生成两个进程组,每个包含4个进程;最后调用MPI_INTERCOMM_CREATE生成两组之间的组间通信体。

# 14.2.4导出数据类型

MPI中的导出数据类型(DerivedDatatype)允许将不连续的数据元素组合在一起,这种导出数据类型可以使用构造函数(ConstructorFunction)构造之。MPI提供的导出数据类型函数概括在图14.8中： $\textcircled { 1 } \mathbf { M P I }$ _TYPE_CONTIGU-OUS:它用来定义由一个或多个连续数据元素组成的类型; $\textcircled { 2 } \mathbf { M P I }$ _ TYPE _VECTOR:它用来定义由一个或多个成块数据元素组成的类型，这些成块的数据元素是由数组中的恒间距所分开； $\textcircled{3}$ MPI_TYPE_INDEXED:它用来定义由一个或多个基本的或先前已定义数据类型的数据块组成的类型,其中块的长度和块间位移量由数组指定； $\textcircled{4}$ MPI_TYPE_COMMIT:它用来提交数据类型,必须在使用导出数据类型之前使用; $\textcircled{5}$ MPI_TYPE_FREE:它用来释放导出数据类型,必须在使用导出数据类型之后使用。这些函数的作用,读者可参照习题14.2和14.3进一步理解之。

MPI_TYPE_CONTIGUOUS(count,oldtype,newtype)   
Construct datatype from contiguous elements . IN count number of elements(integer≥0) IN OUT newtype output datatype(handle)   
MPI_TYPE_VECTOR(count,blocklen,stride,oldtype,newtype)   
Construct datatype from blocks separated by stride. IN count number of elements(integer≥0) IN blocklen elements in a block( integer≥0) IN stride elements between start of each block(integer) IN oldtype input datatype(handle) OUT newtype output datatype(handle)   
MPI_TYPE_INDEXED(count,blocklens,indices,oldtype,newtype)   
Construct datatype with variable indices and sizes . IN count number of blocks(integer≥0) IN blocklens elements in eack block(array of integer ${ \geqslant } 0$ ） IN indices displacements for each block(array of integer) IN oldtype input datatype(handle) OUT newtype output datatype(handle)   
MPI_TYPE_COMMIT(type)   
Construct datatype so that it can be used in communication . INOUTtype datatype to be committed(handle)   
MPI_TYPE_FREE(type)   
Free a derived datatype. INOUTtype datatype to be freed(handle)

# 14.2.5点到点通信

点到点通信(Point-to-Point Communication)是MPI中比较复杂的一部分，其数据传送有阻塞和非阻塞两种机制：对于阻塞方式,它必须等到消息从本地送出之后才可以执行后续的语句，保证了缓冲区等资源的可再用性;对于非阻塞方式,它不须等到消息从本地送出就可执行后续的语句，从而允许通信和计算的重叠,但非阻塞调用的返回并不保证资源的可再用性。

如图14.9所示，阻塞和非阻塞有四种通信模式： $\textcircled{1}$ 标准模式,包括阻塞（标准)发送MPI_SEND、阻塞(标准)接收MPI_RECV、非阻塞(标准)发送MPI_ISEND 和非阻塞(标准)接收MPI_IRECV; $\textcircled{2}$ 缓冲模式，包括阻塞缓冲发送MPI_BSEND 和非阻塞缓冲发送MPI_IBSEND; $\textcircled{3}$ 同步模式,包括阻塞同步发送MPI_SSEND和非阻塞同步发送MPI_ISSEND; $\textcircled{4}$ 就绪模式，包括阻塞就绪发送MPI_RSEND和非阻塞就绪发送 MPI_IRSEND。在标准通信模式中，MPI根据当前的状况选取其它三种模式或用户定义的其它模式;缓冲模式在相匹配的接收未开始的情况下，总是将送出的消息放在缓冲区内，这样发送者可以很快地继续计算,然后由系统处理放在缓冲区中的消息，但这不仅占用内存，而且多用了一次内存拷贝;在同步模式中,MPI必须保证接收者执行到某一点,这样接收者是必须有确认信息的;在就绪模式下,系统默认与其相匹配的接收已经调用。

![](images/3b4d4f30e4370d9314f2eefb0937340194265c98e26bd690d63f62980e785f61.jpg)  
图14.9点到点消息通信四种模式

在点到点通信中,发送和接收语句必须是匹配的。为了区分不同进程或同一进程发送来的不同消息，在这些语句中采用了通信体Comm和标志位 tag来实现成对语句的匹配。

对于阻塞的标准通信 MPI_SEND 和 MPI_RECV 函数的格式及其说明,请参见前图14.2。其中发送的含义是将包含count个datatype类型的首地址为buf的消息发送至dest进程,该消息是与标志位tag和通信体comm封装在一块的;接收的含义是从 source进程接收标志为 tag 和通信体为 comm 的消息,将该消息写入首地址为buf的缓冲区,其返回值status中包含消息的大小、标志和来源等信息。

对于非阻塞的标准通信MPI_ISEND和MPI_IRECV 函数格式及其说明如下：

MPI_ISEND(buf,count,datatype,dest,tag,comm,request)

IN buf  
IN countIN datatype  
IN dest 参照图14.2中MPI-SEND函数说明  
IN tag  
IN comm  
OUT request

MPI_IRECV(buf,count,datatype,source,tag,comm,status,request)

OUT buf  
IN count  
IN datatype  
IN dest参照图14.2中MPI-REW函数说明  
IN tag  
IN count  
OUT status  
OUT request

它们的含义与MPI_SEND和MPI_RECV 函数基本上一致,因为它们是非阻塞的通信模式,语句结束后真正的消息发送或接收并没有完成，它仅将消息挂入消息队列中,所以用request指明返回队列指针。也正是因为非阻塞通信在语句结束后,真正的消息发送或接收并没有完成,所以必须用MPI_WAIT和MPI_TEST等语句来结束非阻塞通信,它们的格式及其说明如下：

MPI_WAIT(request,status) IN request OUTstatus   
MPI_TEST(request,flag,status) IN request

OUT flag OUT status

其中,MPI_TEST用来检测非阻塞操作是否真正结束, $\mathrm { f l a g } = 1$ 表示该请求re-quest指向的非阻塞通信已完成;MPI_WAIT则一直要等到非阻塞操作真正完成之后才返回。我们可以认为阻塞通信等于非阻塞通信加上MPI_WAIT。

在点到点通信中，除了上述的函数外还须提供系统询问(Inquiry)和探测(Probe)两个函数,它们的操作概括在图14.10中： $\textcircled { 1 } \mathbf { M P I }$ _IPROBE函数检查未决(Pending)消息的存在而不必接收这些消息，从而允许我们将局部计算与处理将要到来的消息交织在一起编写程序,该调用将设置一个布尔变量flag,以指明与指定的源、tag和通信体相匹配的信息是否有效；②MPI_PROBE函数与MPI_IPROBE相关,它阻塞一直到指定的源、tag和通信体有效,然后返回并设置其status变量; $\textcircled{3}$ MPI_GET_COUNT询问函数得到刚刚收到的消息的长度，其前两个参数分别是由上一个探测或MPI_RECV调用设置的状态目标和被接收的元素的数据类型，而第三个参数是一个用以返回所接收的元素数目的整数。

MPI_ IPROBE(source,tag,comm,flag,status)

Poll for a pending message.

IN source id of source process,or MPI_ANY_SOURCE(integer)   
IN tag message tag,or MPI_ANY_TAG(integer)   
IN comm communicator(handle)   
OUT flag (logical/Boolean)   
OUT status status object(status)

MPI_PROBE(source,tag,comm,status)

Return uhen message is pending.

IN source id of source process,or MPI_ANY_SOURCE(integer)   
IN tag message tag,or MPI_ANY_TAG(integer)   
IN comm communicator(handle)   
OUT status status object(status)

MPI_GET_COUNT(status,datatype,count)

Determine size of a message.

IN status status variable from receive( status) IN datatype datatype of receive buffer elements(handle) OUT count number of data elements in message(integer)

这些函数的用法可通过如下代码段理解之：

int count, $\star$ buf , source;   
MPI_Probe(MPI_ ANY_ SOURCE,0,comm,&status);   
Source $=$ status. MPI_SOURCE;   
MPI_ Get_count(status,MPI_ INT,&count);

buf $=$ malloc(count \* size of (int));

MPI_Recv(buf,count,MPI _ INT,source,0,comm,&status);

该段代码接收来自未知源和包含未知整数数目的消息：它首先用MPI_PROBE检测消息的到来;然后决定消息源，并用MPI_GET_COUNT决定消息的大小;最后分配一个合适大小的缓冲，并接收此消息。

到现在为止，已讨论了约30个MPI函数，它们的C语言说明和Fortran语言说明,综合在本章最后的附录一和附录二中。其中allgather(全收集)和all-toall(多到多)的含义和功能的解释，作为习题14.3留给读者完成。

最后,给出一个用C语言描述的MPI计算 $\pmb { \pi }$ 的示范程序（它是Hostless程序)如下,以供读者学习理解之用。

$/ / \star$ 计算 $\pmb { \pi } \pmb { \mathbb { C } }$ 语言MPI编程代码段 $\yen 74$   
# include "mpi.h"   
# include $<$ stdio.h>   
# include<math.h>   
double f(a)   
double a; return(4.0/(1.0+a \*a));   
一

int main(argc,argv) int argc; char $\bigstar$ argv[];

int done ${ \bf \mu } = { \bf 0 }$ ， $\mathbf { n }$ ,myid,numprocs,i;   
double PI25DT ${ \ o } = 3$ .141592653589793238462643;   
double mypi,pi,h,sum,x,a;   
double startwtime,endwtime; MPI _ Init(&argc,&argv);   
MPI_Comm_ size(MPI_COMM_WORLD,&numprocs);   
MPI_Comm_rank(MPI_COMM_WORLD,&myid);

$\mathbf { \hat { n } } = \mathbf { 0 }$

while(!done) i $\mathbf { f } ( \mathbf { m } \mathbf { y } \mathrm { i d } = \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \alpha } } } } } \mathbf { = } \mathbf { 0 } )$ printf("Enter the number of intervals:(O quits)"); $\mathbf { s c a n f } ( ^ { \prime \prime } \mathfrak { H } \mathrm { d } ^ { \prime \prime } , \& \mathrm { n } )$ ； $\mathbf { i f } ( \mathbf { n } = \mathbf { \Gamma } = \mathbf { 0 } ) \mathbf { n } = 1 0 0 \mathbf { ; }$ else $\mathbf { \hat { n } = 0 }$ ； startwtime $\asymp$ MPI _ Wtime(); ！ MPI_Bcast(&n,1,MPI_INT,0,MPI_COMM_WORLD); if $\mathbf { \hat { n } } = \mathbf { \hat { \mu } } = \mathbf { 0 } .$ ） done= 1; else ！ $\begin{array} { r l } & { \mathbf { h } { = } 1 . 0 / ( \mathbf { d o u b l e } ) \mathbf { n } ; } \\ & { { \mathrm { s u m } } { = } 0 . 0 } \\ & { \mathbf { f o r } ( \mathrm { i } { = } \mathrm { m y i d } + 1 ; \mathrm { i } { < } { = } \mathrm { n } ; \mathrm { i } + \mathrm { \ n u m p r o c s } ) } \\ & { \big ~ ; } \end{array}$ $\begin{array} { l } { \mathbf { x } = \mathbf { h } \ast \left( \left( \mathbf { d o u b l e } \right) \mathrm { i } - \mathbf { 0 } . 5 \right) ; } \\ { \mathbf { s u m } + = \mathbf { f } \left( \mathbf { x } \right) ; } \end{array}$ 一 1 $\mathtt { m y p i } { = } \mathtt { h } * \mathtt { s u m }$ MPI_Reduce(&mypi,&pi,1,MPI_DOUBLE,MPI_ SUM,0, MPI_COMM_WORLD); $ \begin{array} { l } { \mathbf { i f } \left( { \mathrm { m y i d } } = = 0 \right) } \\ { \qquad { \Big \} } \end{array} }$ printf ("pi is approximately $\%$ .16f,Error is %.16f\ n", pi,fabs(pi-PI25DT)); endwtime $\asymp$ MPI _Wtime(); printf("wall clock tin $\vert \mathbf { e } = \boldsymbol { \mathfrak { g } } _ { 0 } \mathbf { f } \setminus \mathbf { n } ^ { \prime \prime }$ ,endwtime - startwtime); 8 MPI_Finalize(); eturn(0);

# \*14.3 PVM并行编程

并行虚拟机PVM(ParallelVirtualMachine)是由美国橡树岭国家实验室ORNL(Oak Ridge National Laboratory)于1989 年开发的一种支持网络并行计算的支撑软件。后来,由 Tennessee 大学、Emory 大学、CMU等大学共同研制,并得到美国能源部、国家科学基金会、Convex公司的资助，于1995年发布3.3版本。它是一个自包含的自由软件,源代码公开,从网上可以得到,因而颇受大学、研究机构的欢迎并得到广泛应用。它已成为很流行的大型科学计算的并行软件,可在同构/异构型网络环境下模拟实现一个通用的基于分布存储的并行计算机系统,提供基于消息传递的并行程序设计接口,使网上的用户能够集中地使用众多的机器资源来求解大规模计算问题。

PVM虽然没有MPI功能那么强大,但由于其出现较早,且是一个自包含系统(MPI不是自包含的),同时PVM不是一个标准(MPI是个标准),这就意味它较易修改,所以在大型计算应用领域中得到广泛使用。目前PVM和MPI正在彼此靠拢,例如,MPI-2(相对而言,以前所讨论的MPI可称为MPI-1)已加进了进程管理的功能;而PVM也有较多的群体通信功能。如果PVM和MPI最终能归并成一个单一的和标准的库,则无疑对并行处理是非常有益的。

# 14.3.1 PVM概貌

PVM组成 它由两部分组成：监控进程(Daemon Process)和PVM例程库。监控进程(称之为 pvmd)驻留在虚拟机的每一台节点机上(PVM称节点为主机),提供类似于系统调用的接口,实现进程(PVM称进程为任务)控制、通信和错误检测;PVM可调用库(称之为libpvm3.a)提供并行程序设计所需的函数和过程,主要包括进程(任务)的创建与控制、进程(任务)间的通信、系统配置以及错误处理和动态进程组管理等。

PVM控制台(PVMConsole）在PVM安装[74]之后,用户从任何主机上键入下述命令就可生成PVM控制台：

pvm host _file

成功地执行此条命令,就可在调用的主机(称为master)上启动pvmd,而在其它各主机上列出一个任选host_file并在master主机上显示如下提示：

# pvm>

它指明该主机处于PVM控制台模式。PVM控制台是一个独立的交互的PVM进程,尤如 shell,用户键人一些命令就可管理虚拟机、调用PVM应用作业、监视作业的执行等。这些命令包括加人、删除主机和列出虚拟机配置,在虚拟机上启动运行多个任务和列出运行的作业以及PVM关机杀掉所有进程。

编译和运行PVM应用程序可用C语言或Fortran语言编写，它通过PVM提供的消息传递机制实现并行计算。因为PVM定义了许多常量和数据结构,为了使用PVM库函数,在C语言中要引入语句include $<$ pvm3.h>;在Fortran语言中要引人语句include‘ $\$ 1$ PVM_ROOT/include/fpvm3.h'。编好的程序可分别使用编译器cc或f77进行编译和链接。编译完后，如PVM是同构的则可将该目标代码拷贝到所有其它机器上;如PVM是异构的，则须将源代码拷贝到各个机器上重新编译。当所有工作完成后，在master主机上启动pvmd，该 pvmd进程将按用户的配置启动网络上其它节点上的pvmd进程,这样用户的应用程序就可在PVM上运行了。

# 14.3.2 PVM消息传递库

PVM库(libpvm3.a)提供并行程序设计所需的函数和过程，主要包括以下几类：

进程(任务)的创建与控制 $\textcircled{1}$ PVM进程通过调用pvm_mytid（）来进人PVM,同时获得自己的 TID; $\textcircled{2}$ 通过调用函数 pvm_exit（)退出 PVM; $\textcircled{3}$ 函数pvm_spawn(）用于生成 pvm 的子进程;④pvm_parent（）用于返回任务的父进程的 TID。它们的格式如下：

int pvm_mytid()   
int pvm _exit()   
int pvm_parent(）   
int pvm _ spawn(char $\pmb { \mathscr { k } }$ task ,char $\yen 123,456$ argv,int flag,char $\clubsuit$ where, int ntask,int $\pmb { \mathrm { \star } }$ tids)

进程(任务)间的通信①PVM通过调用pvm_initsend()函数来创建一个新的发送缓冲区，并将其置为活动缓冲区，参数encoding是数据打包时所使用的数据编码类型，包括pvmDataDefault(若PVM是同构的，则不进行数据格式转换；否则要按外部数据表示XDR进行数据格式转换）、PvmDataRaw(不对数据进行任何编码)和PvmDataInPlace(打包时数据仍放在原处）；②发送缓冲区中可以同时包含各种不同类型、不同长度的数据，所以在数据发送之前必须对其打包，所使用的函数包括pvm_pkint（）、pvm__pkbyte（）、pvm_pklong（）、pvm_pkshort(）、pvm_pkdouble(）、pvm_pkfloat(）和 pvm_pkstr(）等;③函数pvm_send（）用来将打好包的数据发送给其它的进程;④函数pvm_recv（）用来接收数据，参数tid给出目标进程的TID,msgtag给出消息的标志;③接收时必须对所收到的数据进行与发送时打包相对应的拆包，所使用的函数包括pvm_upkint（）、pvm_upkbyte（）、pvm_upklong（）、pvm_upkshort（）、pvm_upkdouble(）、pvm_upkfloat（）和 pvm_upkstr（）等。它们的格式如下：

int pvm _initsend(int encoding) int pvm _pkint(int \* np,int nitem,int stride) int pvm_send(int tid,int msgtag) int pvm _recv(int tid,int msgtag) int pvm _mcast(int tids,int nitem,int msgtag) int pvm_upkint(int \* np,int nitem,int stride)

动态进程(任务)组PVM支持进程(任务)组(Group)的概念。一个任务组中可包含多个任务;一个任务也可同时属于多个任务组。任务组可动态生成，任何任务可在任何时刻加入或离开一个任务组。任务组的创建有助于对组中任务进行广播、设置路障以及施行全局运算。任务组的引入，使得一个PVM任务既可以用 tid来标识,也可以用(组名，成员号)二元组来标识。任务组操作中最基本的函数是加人和离开任务组：

int pvm _joingroup(char \* group) int pvm _ lvgroup(char $\star$ group)

下面的函数可以从成员号inum获得tid,或从tid获得成员号以及获得一个任务组中的成员数：

int pvm_gettid(char \* group,int inum) int pvm_getinst(char \* group;int tid) int pvm _gsize(char \* group)

与任务组相关的其它操作,包括同步 pvm_barier（）:调用任务等待组中共有count个任务调用了pvm_barrier(）;广播pvm_bcast（）:对任务组中的所有成员进行播送;归约 pvm_reduce（):类似于 MPI中的归约,用于在指定的任务组的全体成员进行全局性运算,如在同组的所有任务中求最大/最小、求和等。这些函数的格式如下：

int pvm_barrier(char \* group,int count)   
int pvm _bcast(char $\clubsuit$ group,int msgtag)   
int pvm_reduce (void( \* func)(),void $\ast$ data,int nitem,int datatype, int msgtag,char $\clubsuit$ group,int root)

动态配置PVM可由用户调用PVM库函数进行动态配置。函数pvm_addhosts(）和pvm_delhosts(）用来加人和删除一个或多个主机：

int pvm_addhosts(char $^ { \star }$ $\clubsuit$ hosts,int nhost,int $^ { \ast }$ infos) int pvm_delhosts(char $\pmb { \mathscr { k } }$ $\pmb { \mathscr { k } }$ hosts ,int nhost ,int $\pmb { \mathscr { k } }$ infos) 它们将hosts指定的机器名加人到当前虚拟机中，或从当前虚拟机中删去这些 机器。

最后,给出一个用C语言描述的PVM计算 $\pmb { \pi }$ 的示范程序（它是一个 SPMD程序)如下，以供读者学习理解之用。

$/ / \ast$ 计算 $\pmb { \pi } \pmb { \mathbb { C } }$ 语言PVM编程代码段 $\yen 74$   
# define n $1 6 ~ / \ast$ number of tasks $\pmb { \mathscr { k } }$ /   
# include $\prime \prime \mathrm { p v m } 3 . \mathrm { h } ^ { \prime \prime }$   
main(int argc,char $\# \quad \#$ argv) int mytid,tids[n],me,i,N,rc,parent; double mypi, $\mathbf { h } , \mathbf { s u m } = \mathbf { 0 } . \mathbf { 0 } , \mathbf { x } ;$ $\mathtt { m e } = \mathtt { p v m }$ _joingroup("pi"); parent $=$ pvm _ parent(); if $\mathbf { \dot { m } e } = 0 .$ pvm_ spawn("pi",(char \* \* )0,0," ",n-1,tids); printf("Enter the number of regions:"); scanf("%d",&N); pvm_initsend(PvmDataRaw); pvm_pkint(&N,1,1); pvm _mcast(tids,n-1,5); else pvm __recv(parent,5); pvm_upkint(&N,1,1); $\mathrm { p v m \_ b a r r i e r { ( } ^ { \prime \prime } P I ^ { \prime \prime } , n ) } ; / * \mathrm { o p t i o n a l } * /$ ${ \bf h } = 1 . 0$ /(double)N; ${ \bf f o r ( i = m e + 1 ; i < = N ; i + \omega = n ) } \left\{ \right.$ $\mathbf { x } = \mathbf { h } \nmid ( ( \mathbf { d o u b l e } ) \mathbf { i } - \mathbf { 0 } . 5 ) ;$ $\mathbf { s u m } + = 4 . 0 / ( 1 . 0 + \mathbf { x } * \mathbf { x } ) ;$ $\mathrm { { m y p i } = h \ast \ s u m _ { \mathrm { { i } } } }$ pvm_reduce(PvmSum,&mypi,1,PVM_DOUBLE,6,"1 if( $\mathbf { m e } = { \mathbf { \eta } } = { \mathbf { 0 } }$ )printf("pi is approximately %.16f\n",mypi pvm_lvgroup("PI"); pvm_exit();

# 14.4 基于数据并行的并行编程

# 14.4.1数据并行模型的特点

关于数据并行模型已在第十三章的第13.2.2节进行了讨论，读者不妨先复习一下那里所讲的内容。

对于有些问题,常常要对大量的数据进行相同的、彼此独立的操作,这些量大且互不影响的操作是可以并行进行的,此即数据并行名称的由来。例如,矩阵相乘就呈现出数据并行的特点：当两个 ${ \pmb n } \times { \pmb n }$ 的矩阵 $\pmb { A }$ 和 $B$ 相乘而得到矩阵C时,其乘积元素 $C _ { i j }$ 就是 $\pmb { A }$ 的第 $i$ 行与 $B$ 的第 $j$ 列执行点积运算而求得。所以求每个 $C _ { i j }$ 元素可以并行地对不同的数据元素 $a _ { i k }$ 与 $b _ { k j }$ 执行相同的点积运算。如果我们用某种数据并行语言(下一节将要讨论)来编程实现这种计算,就可得到一个数据并行程序。一个数据并行程序包含一个单一的指令序列,每条指令作用于不同的数据项且以锁步方式同步执行,所以这种程序很自然地适合于在SIMD 机器上实现。当然这样的数据并行程序也可在MIMD机器上实现，只不过是在每条指令之后施行全局同步导致执行效率很低。实用的办法是在MIMD机器上使用 SPMD编程模式,在此模式下并行粒度要大一些。事实上，SPMD是 SIMD的特例,SPMD是一种中粒度的并行,是语句块和循环一级的同步,而不是像SIMD那样是指令级的同步。在SPMD模式下,每个处理器异步地执行相同的程序,只有当处理器间需要交换数据时才施行同步。由于减少了同步,SPMD模式在许多情况下比 SIMD模式更有效。在大规模并行处理MPP系统中，使用 SPMD模式进行编程时，用户程序把整个分布存储系统视为一个统一的全局空间,由编译实现程序的逻辑地址到物理地址的映射。

总之,数据并行程序是一个单一控制线程的、并行操作于不同数据项的、语句循环级同步的、单一地址空间的、通信可由变量指派而隐含地完成的一种并行程序。

# 14.4.2数据并行编程的基本问题

进行数据并行程序设计时常常需要考虑以下几个基本问题：

数据分布(DataDistribution）分布就是要建立数据集合到处理器集合之间的映射关系，数据分布就是把数据按一定规则分配到各个处理器的存储单元中去。数据分布规则实际上也就是数据地址计算规则。分布的目的是为了提高程序执行的并行性，增强数据局部性，减少通信，从而提高程序的执行效率。数据并行程序设计语言及其编译系统所扩充的最主要功能之一就是支持数据分布。

数据分布规则是将共享分布的数组按维分配到各个处理器上。常用分布方法有按块分布、循环分布、对准分布和静态/动态分布等。这些方法在下节介绍HPF时会看到。

任务分配(TaskAllocation）任务分配就是把计算任务分配给各个处理器上,使得程序可以在并行系统上高效执行。任务分配的原则是尽可能将计算和其所需数据对准，也就是数据分配到哪个处理器，就将用到这些数据的计算操作也分配到哪个处理器，此即所谓的属主-计算(Owner-Computes)的原则。在进行数据并行编程时，一般是先定义数据分布，再将并行循环中的迭代计算按数据分布模式分配到各个处理器上去执行，这样就实现了计算和数据的对准。

同步通信对于 SPMD模式数据并行编程,在共享变量模型下,同步机制--般包含临界区、锁、路障和事件等;对于 SPMD模式数据并行编程,编译系统给通信提供了较强的支持：对于点到点通信,程序员可以写成赋值语句，对于全局通信，程序员可以调用系统库程序。

处理器拓扑结构在数据并行语言中，处理器的拓扑结构是逐个数组确定的,是受数据分布影响的。处理器拓扑的形成就是把参加并行执行的处理器分配给分布数组的各维,即决定每维分几个处理器。处理器拓扑结构可由编译系统确定,所依据的规则是数据分布大致均匀、地址计算尽量简单和通信尽可能少。

# 14.5HPF并行编程

高性能Fortran(High Performance Fortran)简称 HPF,是一个支持数据并行的并行语言标准。它提供了一个全局名字空间和单线程控制，用户可以用分布(Distribution)和对准(Alignment)说明定义所希望的数据布局,用显式的并行结构表达并行机制。HPF中由于没有显式的任务划分和通信语句,代码的定义是在高层进行的,因此具有良好的移植性,通过具体机器上的编译器可以生成各种系统平台上的高效代码。

HPF 的产生可以追溯到DEC的 Lovman 和Rice大学的Kennedy在 Super-computing'91大会上发起的“Birdsof afeather"小组会。在这个会上主要讨论了关于分布存储机器上的高层编程方法。DEC首先抛砖引玉，提供了他们的HPF;紧接着于1992年1月在Rice大学召开了第一次HPF会议,会议决定组织HPF论坛;1992年3月论坛正式成立;1993年5月发布了HPF1.0版;1994年11月发布了HPF1.1版,到1997年1月发布了HPF2.0版。所有文档可从网上站点 http://www.crpc.rice.edu/HPF/home.html获得。

# 14.5.1 HPF的语言特点

以下的讨论立足于HPF2.0版本。HPF2.0语言包括三个部分： $\textcircled{1}$ 语言的基本部分,包括任何HPF编译器必须支持的特性; $\textcircled{2}$ 已经核准的扩展部分，包括满足某些特殊需要的高级结构(早期的编译器可能不支持这一部分); $\textcircled{3}$ 已被认可的外部接口,这是HPF论坛批准的一组接口。

当前的HPF2.0 版是基本 Fortran95,并吸取了HPF1.1版的一些特性；而HPF1.1版是基于Fortran90的,Fortran 90的数组语句为数据并行提供了一种自然的机制,HPF1.1扩展了Fortran90的这些特性,提供了实现数据并行操作的FORALL结构和几个内部与外部库。

HPF2.0的一些基本特性是： $\textcircled{1}$ 数据并行制导（Data Parallel·Directives）：HPF2.0提供的数据并行机制扩展了Fortran 95的数组语句和FORALL结构，其中 INDEPENDENT用于声明无依赖循环迭代,可以并行执行；REDUCTION用于标识被不同迭代修改的变量;②数据映射制导(Data MappingDirectives）：HPF提供了一组扩展的说明,用于指定数据的分布和对准，可将数据显式地定义到抽象的处理器上，所提供的ALIGN和DISTRIBUTION说明，能够让用户告诉编译器如何在各处理器间分配数据，以使通信开销最小和负载划分最均匀；$\textcircled{3}$ 新内部函数和库函数(New Intrinsic and Library Functions):HPF 提供了一组新的内部函数和库,包括请求底层硬件的系统函数、请求数据结构分布的映射请求函数以及一些计算的内部函数;HPF定义了一组新的库,为并行操作定义了一个标准的接口，包括归约（Reduction）、组合-散射（Combining-Scatter）、前缀(Prefix)及后缀(Suffix)分类(Sorting)和位操作(Bit-Manipulation）函数等; $\textcircled{4}$ 外部过程(Extrinsic Procedures):除了数据并行编程外,HPF为了匹配其它编程方法,HPF定义了一个显式接口，允许用不同语言(如C)或不同方法(如显式消息传递)所编制的程序能够被一个HPF程序调用。

# 14.5.2 HPF的数据并行机制

FORALL结构HPF 中新增的 FORALL 语句和 FORALL 结构类似于Fortran 90的数0组赋值语句，只是比Fortran90的数组赋值语句更灵活,并且FORALL语句能以指定的逻辑表达式对赋值语句进行限定。例如下述FORALL 语句：

$$
\mathrm { L } ( i = 2 \colon 5 , \mathrm { X } ( i ) > 0 ) \quad \mathrm { X } ( i ) = \mathrm { X } ( i - 1 ) + \mathrm { X } ( i + 1 )
$$

其中,i是索引变量；i=2:5称为 for-三元组,等价于i=2:5:1,表示i取值上界为5、下界为2而步长缺省时为1。在上述FORALL语句中,假定初始X={1,-1,2，-2,3,-3},在i的有效值范围内,满足X(i)>0的索引i的活动集合为

{3,5,同时计算如下赋值语句：

$$
\mathrm { X } ( 3 ) = \mathrm { X } ( 2 ) + \mathrm { X } ( 4 ) = - 3
$$

$$
{ \bf X } ( 5 ) = { \bf X } ( 4 ) + { \bf X } ( 6 ) = - 5
$$

FORALL语句结束后， $\dot { \mathbf { X } } = \left\{ 1 , - 1 , - 3 , - 2 , - 5 , - 3 \right\} ,$ 在 FORALL语句中,可能有不止一个for-三元组,则用的是组合索引,例如：

$\mathrm { F O R A L L } ( \textit { i } = 1 : 2 , \textit { j } = 1 : 3 , \mathrm { Y } ( \textit { i } , \boldsymbol { j } ) > 0 ) \quad \mathrm { Z } ( \textit { i } , \boldsymbol { j } ) = 1 / \mathrm { Y } ( \textit { i } , \boldsymbol { j } )$ 该语句等价于Fortran 90如下语句：

wher $\mathsf { \Lambda } _ { \mathsf { P } } ( \Upsilon ( 1 : 2 , 1 : 3 ) > 0 ) \cdot \mathsf { Z } ( 1 : 2 , 1 : 3 ) = 1 \Upsilon ( 1 : 2 , 1 : 3 )$ 则组合索引的有效值集合为{(1,1),(1,2),(1,3),(2,1),(2,2),(2,3)|,而组合索引的活动值取上述集合中使 $\Upsilon ( i , j ) > 0$ 的子集。

有时用户希望在一个FORALL 语句中包含几个赋值,这可使用 FORALL结构来实现。FORALL结构是对 FORALL语句的进一步扩充,即在FORALL和ENDFORALL之间可以写多条语句，但限制FORALL结构中只能使用赋值语句、FORALL语句、FORALL结构、WHERE语句以及WHILE结构。例如：

$$
\begin{array} { l } { \mathsf { A } ( \mathrm { I } ) = \mathsf { A } ( \mathrm { I } - \mathrm { 1 } ) + \mathsf { A } ( \mathrm { I } + \mathrm { 1 } ) } \\ { \mathsf { B } ( \mathrm { I } ) = \mathsf { A } ( \mathrm { I } ) } \end{array}
$$

上述代码，首先对从2到9的各个I求 $\mathbf { A } { \left( \ \mathrm { I } - 1 \right) } + \mathbf { A } { \left( \ \mathrm { I } + 1 \right) }$ 之值,并将结果送人A(2)到A(9)中;然后将求得的A(2)到A(9)之值送人B(2)到B(9)中。

！HPF $\$ 1$ PROCESSORS proc_name(dim1,,dimN)   
Declare and abstract processor array. proc_ name name of abstract processor array dim1,.,dimN size and shape of array

！ HPF $\$ 1$ ALIGN array WITH target

Align array with a target array.

array array to be aligned target array to be aligned to ！ HPF \$ DISTRIBUTE list_of_arrays[ONTO proc_ name] Distribute array(s)onto processor array.

list_ of _arrays arrays to be distributed proc_ name abstract processor array

数据分布 数据分布指的是将数据(主要是数组)分布到处理器上。HPF引入了如图14.11所示的一些指导数据分布的伪指令，指示编译器如何最佳地分布数据于计算节点上。图14.12是HPF数据分布模型。数据映射(分布)要达到的目的是：使处理器间的通信开销最小以及使负载在处理器上分布均匀。

![](images/96824a8f0005904c1a51fb10e06efbb1bae6d8d582656fd27f9c1bc3427bae85.jpg)  
图14.12 HPF数据分布模型

$\textcircled{1}$ PROCESSORS:伪指令 PROCESSORS说明抽象的处理器排列结构。例如：

它通知编译器,应用程序希望使用4个处理器排成线性阵列的抽象结构。同样，

！HPF $\$ 9$ PROCESSORS P(4,5)！HPF $\$ 1$ PROCESSORS Q(4,5,6)

分别指明20个处理器排成 $4 \times 5$ 的二维网孔和120个处理器排成 $4 \times 5 \times 6$ 的三维网孔。

$\textcircled{2}$ ALIGN:伪指令ALIGN用于描述数组间元素的对准。例如：

！HPF $\$ 9$ ALIGN A(I) WITH B(I)

表示把A的第Ⅰ个元素与B的第I个元素分配到同一个处理器上。同样，！HPF $\$ 8$ ALIGN A(I) WITH $\mathbb { B } ( \mathbb { I } + 2 )$

表示把A的第I个元素与B的第I+2个元素分配到同一个处理器上。图14.13示出了HPF对准语句的6个例子。

$\textcircled{3}$ DISTRIBUTE:伪指令DISTRIBUTE用于指明数组如何在计算机存储器间进行划分。数组每一维可按下述方式之一进行分布：

无分布BLOCK(n) 块状分布CYCLIC(n) 循环分布对于程序员可使用下述两种DISTRIBUTE伪指令：

！HPF $\$ 1$ DISTRIBUTE A(BLOCK) ONTO N！HPF $\$ 9$ DISTRIBUTE C(CYCLIC) ONTO N

图14.14示出了一个8×8的二维数组,使用分块和循环方式分布到4个处理器上的情况。图中带阴影的数据分布给第一个处理器。

![](images/9b1b2c587c95b08d5dec912fcf6aaecf37eae222475344ecb80e6cf8900a4bf4.jpg)  
图14.13HPF对准方式示例

![](images/1928f8bfd172c82886952bdaf03a8a16028c07123b46f21adb22b2f0ff30979c.jpg)  
图14.14 $\mathbf { 8 \times 8 }$ 的二维数组分布给4个处理器

下面给出 HPF 数据映射的一个综合例子。试考虑如下HPF代码段：integer A(100),B(100),C(101),i

！ HPF \$ ALIGN A(i) WITH B(i-1)  
！ HPF \$ PROCESSOR N(4)  
！ HPF \$ DISTRIBUTE A(BLOCK) ONTO N  
！HPF \$ DISTRIBUTE C(CYCLIC) ONTO NFORALL ( $i = 2 { : } 1 0 0 \rangle$ ）$\mathbf { A } ( \mathbf { \zeta } _ { i } ) = \mathbf { A } ( \mathbf { \zeta } _ { i } ) + \mathbf { B } ( \mathbf { \zeta } _ { i } - 1 )$ $\mathbf { C } ( \mathsf { \Delta } i ) = \mathbf { C } ( \mathsf { \Delta } i - 1 ) + \mathbf { C } ( \mathsf { \Delta } i ) + \mathbf { C } ( \mathsf { \Delta } i + 1 )$ ENDFORALL

图14.15描述了上述代码段实现的数据映射过程。HPF 中数据映射的实现分为两个阶段：逻辑映射和物理映射。前者由用户通过编译制导(CompilerDirectives)定义,将数据映射到抽象处理器节点上;后者由系统将上述抽象处理器节点映射到实际计算机物理节点上,这对用户是透明的。其中逻辑映射分为对准和分布两步。

![](images/264a362f98477fcd1c979061c0e0eaad4e87481f7caad17755ace72b5e0214da.jpg)  
图14.15HPF数据映射过程

外部过程HPF中增加了具有如下功能的库程序：①系统查询功能：它可给出有关处理器的信息,包括可用处理器数的NUMBER_OF_PROCESSOR库程序以及处理器构成信息的PROCESSOR_SHAPE库程序； $\textcircled{2}$ 变换查询功能：它可给出有关数据的分布、定位方面的信息,包括数据定位信息的HPF_ALIGNMENT_库程序,template信息的HPF_TEMPLATE库程序和数据分布状态信息的HPF_DISTRIBUTION库程序； $\textcircled{3}$ 计算库功能：它提供求数组中的最大值和前缀运算等。这些运算使用具有网络特性的库函数比起使用以For-tran描述的循环效果更好。在HPF中提供的库函数有归约函数、前缀及后缀函数、组合-散射函数、分类函数和位变换函数等。

# 14.5.3 HPF使用中的若干问题

语言的限制问题在Fortran中,数组元素按一定的顺序被分配在一维连续的存储区内,并可通过等价语句EQUIVALENCE和子程序调用中的虚实变量结合发生连接。因此会发生部分一维数组被二维数组覆盖以及某变量的一部分和另一变量的一部分拥有同一存储区的情况。在HPF程序中也会发生类似情况(参见习题14.6)。另外,关于子程序调用时的虚实变量结合也受到限制。例如在Fortran90中，能作到用数组元素的实变量代换虚变量，用二维数组代换一维数组。但在HPF中这样作就需要使用 SEQUENCE伪指令写出程序,例如：

REAL A(100,100),B(200)  
！ HPF \$ SEQUENCE A,BCALL S(A,B(51))ENDSUBROUTINE S(X,Y)REAL X(10000),Y(100)  
！ HPF \$ SEQUENCE X,Y：END

并行性问题因为HPF是单线程的，所以一个数据并行的程序逻辑上只有一个进程,尽管多个节点能够对不同的数据子域执行相同的程序。绝大部分并行性问题由系统管理,用户不用担心进程的生成、结束和有多少进程正在运行程序。因为HPF是语句级的数据并行,它允许在同一时间不同的节点执行不同的指令，因此可同时支持SIMD和 SPMD并行计算,但不支持MPMD计算。程序中的并行度是随所用的不同的数组指派或执行不同的FORALL语句而动态变化。

相互作用问题因为是松散同步，所以在数据并行编程中绝大多数相互作用问题都躲开了，除了归约操作外，Fortran90或HPF中不存在相互作用问题。

在Fortran 90中提供了9种内部函数以支持归约,但不支持前缀、递降、分类,它也不支持用户定义的归约操作。HPF通过一组库例程扩展了Fortran 90的能力，包括辅助的归约函数、scan函数和分类等。

数据并行程序只有一种相互作用模式，即语句级的松散同步。一条语句的所有操作均必须在下一语句的任一操作开始之前完成。通信经由数组赋值而呈隐式状。HPF提供一组数组分布伪指令，使用开拓数据局部性而可最小化通信开销。HPF除了提供 PROCESSORS、ALIGN和DISTRIBUTE 伪指令外,还提供REALIGN 和REDISTRIBUTE语句以调节通信模式的变化。

语义问题由于单线程和松散同步,所以数据并行程序具有清晰的语义,它不可能出现死锁或活锁,仅有的可能是由于无限循环而会造成非确定性。For-tran 90 和HPF在结构性、合成性和正确性方面类似于串行的Fortran90程序,并未因引人并行性而增加复杂性。

数据并行程序只要满足单赋值规则它就是确定的。

可编程性问题 因为Fortran和HPF均是高级语言标准,所以具有好的可移植性。又因为大多数并行性、相互作用和语义问题均由系统负责，所以For-tran 90 和HPF易于使用。但现在的Fortran90和HPF语言说明对通用性和效率尚有严格的限制,所以不少人仍在使用别的编程方法。Fortran90和HPF不支持开拓控制并行,它们也不适合于支持异步迭代、流水线计算等算法范例,数据库方面的应用也比较困难。HPF 的数据映射似乎也仅支持正规通信模式的数组,它是否有效地支持一般数据结构和非正规通信模式的并行算法，还值得怀疑。

最后,给出一个高斯消去法的 HPF 程序如下,以供读者学习理解之用(其Fortran 90程序见习题14.7)。

$/ / \ast$ 高斯消去法的HPF编程代码段\*//  
parameter $\mathtt { n } = 3 2$   
real $\mathbf { A ( n , n + 1 ) , x ( n ) }$   
integer $\vdots$ ,pivot_location(1)  
！HPF $\$ 9$ PROCESSOR Nodes(4)  
！HPF $\$ 9$ ALIGN $\mathbf { x } ( \mathrm { i } )$ WITH A(i,j)  
！HPF $\$ 1$ DISTRIBUTE A(BLOCK, $\star$ ） ONTO Nodes  
d $\mathbf { \delta } _ { \mathbf { \{ j } }  = \mathbf { 1 } , \mathbf { n } - \mathbf { 1 }$ ！pivotingpivot_ $\scriptstyle \mathrm { l o c a t i o n } = \mathbf { M A X L O C } ( \mathbf { A B S } ( \mathbf { A } ( \mathbf { i } \cdot \mathbf { n } , \mathbf { i } ) ) )$ swap $\mathfrak { o } \big ( \mathbf { A } ( \mathrm { i } , \mathrm { i } { : } \mathrm { n } + 1 ) , \mathbf { A } ( \mathrm { i } - 1 + \mathrm { p i v o t \_ l o c a t i o n } ( 1 ) , \mathrm { i } { : } \mathrm { n } + 1 ) \big )$ ！triangularization$\mathbf { A } ( \mathrm { i } , \mathrm { i } ; \mathbf { n } + 1 ) = \mathbf { A } ( \mathrm { i } , \mathrm { i } ; \mathbf { n } + 1 ) / \mathbf { A } ( \mathrm { i } , \mathrm { i } )$ FORALL $( { \bf j } = { \bf i } + 1 \cdot { \bf n } , { \bf k } = { \bf i } + 1 \cdot { \bf n } + 1 ) { \bf A } ( { \bf j } , { \bf k } ) = { \bf A } ( { \bf j } , { \bf k } ) - { \bf A } ( { \bf j } , { \bf i } ) * { \bf A } ( { \bf i } , { \bf k } )$   
end do  
！back substitution$\begin{array} { r l } & { \mathfrak { p i } = \mathfrak { n } , \mathbf { 1 } , - 1 } \\ & { \mathbf { x } ( \mathrm { i } ) = \mathrm { A } ( \mathrm { i } , \mathfrak { n } + \mathbf { 1 } ) } \\ & { \mathrm { A } ( 1 { : } \mathrm { i } - 1 , \mathfrak { n } + 1 ) = \mathrm { A } ( 1 { : } \mathrm { i } - 1 , \mathfrak { n } + 1 ) - \mathrm { A } ( 1 { : } \mathrm { i } - 1 , \mathrm { i } ) * \mathbf { x } ( \mathrm { i } ) } \end{array}$

end do

# 14.6 小结和导读

小结分布存储系统包括 SIMD-DM、MIMD-DM和COW-DM等并行计算机系统。在SIMD-DM并行系统上,使用数据并行程序设计模型,以SPMD编程方式编写并行程序,常用的编程语言有Fortran90 和HPF等;在MIMD-DM和COW-DM并行系统上,使用消息传递程序设计模型,以 SPMD和MPMD编程方式编写并行程序,常用的语言标准有MPI和PVM等。

数据并行语言标准除了本章所介绍的HPF和Fortran90外，目前还有For-tran 95、Fortran 2001 和 Fortran D、Vienna Fortran。其中 Fortran 95 和 Fortran2001是Fortran 90 的推广;Fortran D和 Vienna Fortran是MPI的推广。Fortran95发布于1997年,主要新特性是FORALL 语言和 FORALL结构,PURE 和ELEMENTAL过程以及结构和指针缺省初始化。Fortran 2001预计2001年发布,正被考虑中的新特性包括例外处理,与C语言的连接性，增强导出数据类型,附加支持高性能数值计算,新的I/O性质,面向对象等。Fortran D(后称为Fortran 90D)和ViennaFortran提供更通用的数据映射函数,包括支持动态和非正规数据分布等。

消息传递标准除了本章所介绍的1994 年发布的 MPI(称之为MPI-1外),1997年MPI论坛又发布了修订标准MPI-2。MPI-2相对于 MPI-1增加了很多功能,主要包括动态进程(MPI-1并行程序中的进程是静态的),点到点单边通信(MPI-1点到点通信是双边的),可扩放I/O支持(MPI-1完全不考虑I/O问题),Fortran 90 和 $\mathrm { C } + +$ 语言描述(MPI-1的语言描述是 Fortran 77和 C),增加实时处理,推广MPI-1的外部接口和环境工具,允许非阻塞群体通信、通信体间的群体通信、通信体间的拓扑结构(MPI-1只支持阻塞和通信体内的群体通信)等。

导读有关MPI的最初描述见[128],一本好的 PVM人门见[74]。关于网络并行计算与分布式编程环境，读者可参阅[197]。数据并行方法见[92]，HPF描述在[111]、[125],推广的HPF见[45],Fortran 90描述在[1],Fortran95 描述在[2],FortranD描述见[70],Vienna Fortran描述在[188]。关于并行程序设计的一本简明教材是[195]。关于消息传递程序设计和数据并行程序设计,读者可阅读[103]书的第13章和第14章。

# 习 题

14.1试考虑下述代码段中通信体的使用：

process 0:  
MPI_Send(msgl,countl,MPI_INT,tagl,comml);parallel_fft(…);  
process 1:  
MPI _Recv(msgl,countl,MPI _ INT,tagl,comml) ;parallel_fft(…);  
(1)试分析上述代码段的计算功能。  
(2)如果在parallel_fft $( \cdots )$ 中又包含了另一个发送程序：if(my-rank ${ \bf \Psi } = { \bf 0 }$ )MPI_Send(msg2,count1,MPI_INT,1,tag2,comm2);如果没有通信体则会发生什么情况？

14.2填上空白处,使下述两代码段完全等效：

(1)Call MPI_TYPE_CONTIGUOUS(10,MPI_REAL,tenrealtype,ier) Call MPI_TYPE_COMMIT(tenrealtype,ierr) Call MPI_ SEND(data,1,tenrealtype,dest,tag,MPI _ COMM_WORLD,ierr) Call MPI _TYPE_FREE(tenrealtype,ierr)   
(2)Call MPI_SEND(data., ， ,dest,tag, ,ierr)

14.3填上空白处,使下述两代码段完全等效：

(1)float data[1024];MPI _Datatype floattype;MPI_Type_vector(10,1,32,MPI_FLOAT,&floattype);MPI_Type_commit(& floattype);MPI _ Send(data,1,floattype,dest,tag,MPI_COMM_WORLD);MPI_Type_free(&floattype);  
(2)float data[1024],buff[10];for(_ ； _;i++）buff[i] $\mathbf { \Phi } = \mathbf { \Phi }$ data[. ：MPI__Send(buff, _,MPI_FLOAT, ）；

14.4在MPI群体通信中,还有allgather和altoall两个函数,它们可图示于图14.16中,试

解释两者的功能及意义。

![](images/ad801e61592d0b59bdc58e664218573cb0112b9418db4591a29c2cdbaecf55cf.jpg)  
图14.16allgather和 alltoall群体操作

14.5下面是PVM环境下的 hello程序,它是一个 host/node程序,试分析其工作过程。

//\*PVM主机/节点编程的hello代码段 $\bigstar$ // $\big / \ast \mathrm { \bf { h o s t } }$ 程序 hello. $\pmb { c } \star$ / # include <stdio.h> # include “pvm3.h" main() int cc,tid; char buf[100]; $\begin{array} { r l } & { \mathrm { p r i n t f } ( \mathrm { \ ' { ' } ^ { \prime } i } ^ { \prime } \mathrm { \ ` m ~ t } \% \times \mathrm { \ ` ~ n ' ~ } , \mathrm { p v m \_ m y t i d ( \cdot ) } ) ; } \\ & { \mathrm { c c = \mathrm { p v m \_ \mathrm { p n } - \mathrm { s p a w n } } ( \mathrm { \ ' { ' h e l l o } _ { \mathrm { - } } \ o t h e r \ " , ( \mathrm { c h a r } \times \mathrm {  ~ \times ~ } ) 0 , 0 , \mathrm { \cdots ~ } ^ { \prime \prime } , \mathrm { \bf { 1 } } , \& \mathrm { \ " { \mathrm { t i d } } } ) ; } } } \\ & { \mathrm { i f } ( \mathrm { c c = \bf { 1 } } ) \smash { \downarrow } } \\ & { \qquad \mathrm { c c = \mathrm { p v m \_ \mathrm { r e c v } ( \mathrm { - } 1 , \mathrm { - } 1 ) } ; } } \\ & { \qquad \mathrm { p v m \_ { \mathrm { b u f i n f o } } ( \mathrm { c c , \mathrm { ( i n t \ast ) } 0 , ( i n t \ast \mathrm { \Lambda ) } 0 , \& \mathrm { \vec { \mathrm { ~ } } t i d } ) ; } } } \\ & { \mathrm { p v m \_ \mathrm { \nu \mathrm { \nu \mathrm { \to } \nu t r i c } } ( \mathrm { b u f } ) ; } } \\ & { \mathrm { p r i n t f } ( \mathrm { \ ' f r o m \_ t y \mathrm { \nu } , \mathrm { \Lambda } } ; \mathrm { \Lambda } _ { \mathrm { \Lambda } } ^ { \prime } ) { _ \mathrm { \mathrm { 6 l } } } , \mathrm { \ n i d } , \mathrm {  { b u f } } ) ; } \end{array}$ else

printf("can't start hello _other\n"); pvm_exit(); /\* node 程序 heuo__ other.c \*/ # include "pvm3.h" # include"string.h" main() ！ int ptid; char buf[100]; ptid $\lneq$ pvm _ parent(); strcpy(buf,"heul,world from"); gethostname(buf $^ +$ strlen(buf),64); pvm _initsend(PvmDataDefault); pvm_pkstr(buf); pvm__send(ptid,1); pvm_exit(）; exit(0); ！

14.6试分析下述HPF代码段中数组元素的覆盖情况;如何用EQUIVALENCE语句使其变成正确的HPF程序？

REAL A(100),B(100) EQUIVALENCE(A(51),B(1))   
$! \ H P F \ S$ PROCESSORS P(4)   
$! \ H P F \ S$ DISTRIBUTE A(Block) ONTOP

14.7高斯消去法的Fortran90程序如下：试分析其计算过程并与高斯消去法的 HPF程序(课文中）加以比较。

$/ \varkappa$ 高斯消去法的Fortran90编程代码段 $\pmb { \mathscr { k } }$ /   
real $\mathbf { A ( n , n + 1 ) , x ( n ) }$   
integer i,pivot_loctation(1)   
do $\mathbf { \omega } _ { \mathbf { i } } = \mathbf { 1 } , \mathbf { n } - \mathbf { 1 }$ ！pivoting pivot_ location $\lneq$ MAXLOC(ABS(A(i: n,i))) swaj $\mathsf { p } \big ( \mathsf { A } \big ( \mathrm { i } , \mathrm { i } ; \mathsf { n } + 1 \big ) , \mathsf { A } \big ( \mathrm { i } - 1 + \mathsf { p i v o t \_ l o c a t i o n } \big ( 1 \big ) , \mathrm { i } ; \mathsf { n } + 1 \big ) \big )$ ！ triangularization $\begin{array} { r l } & { \mathbf { A } ( \mathrm { i } , \mathrm { i } ; \mathbf { n } + 1 ) = \mathbf { A } ( \mathrm { i } , \mathrm { i } ; \mathbf { n } + 1 ) / \mathbf { A } ( \mathrm { i } , \mathrm { i } ) } \\ & { \mathbf { A } ( \mathrm { i } + 1 ; \mathbf { n } , \mathrm { i } + 1 ; \mathbf { n } + 1 ) = \mathbf { A } ( \mathrm { i } + 1 ; \mathbf { n } , \mathrm { i } + 1 ; \mathbf { n } + 1 ) - \& } \end{array}$

SPREAD(A(i,i + 1:n + 1),1,n-i) \* SPREAD(A(i+ 1:n,i),2,n-i+1)

# end do

！back substitution ${ \begin{array} { r l } & { = \mathbf { n } , 1 , - 1 } \\ & { ~ \mathbf { x } ( \mathrm { i } ) = \mathbf { A } ( \mathrm { i } , \mathbf { n } + 1 ) } \\ & { ~ \mathbf { A } ( 1 { : } \mathrm { i } - 1 , \mathrm { n } + 1 ) = \mathbf { A } ( 1 { : } \mathrm { i } - 1 , \mathrm { n } + 1 ) - \mathbf { A } ( 1 { : } \mathrm { i } - 1 , \mathrm { i } ) * \mathbf { x } ( \mathrm { i } ) } \end{array} }$   
end do

14.8雅可比松弛法 Fortran90程序如下：参照它试写出雅可比松弛法的HPF程序;并将两者加以比较。

$^ { \prime \prime * }$ 雅可比松弛法的Fortran90编程代码段 $^ { \star }$ //   
parameter ${ \bf n } = { \bf 1 0 2 4 }$   
real $\mathrm { A ( n , n ) , x ( n ) , b ( n ) , e r r o r , T e m p ( n ) , D i a g A ( n ) }$   
integer i   
error $=$ SomeLargeValue   
初始化 $\mathbf { A } , \mathbf { x }$ 和 $\boldsymbol { \mathbf { b } }$   
do i=1,n $\mathrm { D i a g A ( i ) } = \mathbf { A } ( \mathrm { i , i } )$   
end do   
do while(error >ErrorBound)   
S1: $\begin{array} { r l } & { \mathrm { T e m p } { = } \left( \mathbf { b } - \mathbf { M A T M U L } ( \mathbf { A } , \mathbf { x } ) \right) \ \mathrm { \mathcal { N i a g A } } } \\ & { \mathbf { x } { = } \mathrm { T e m p } + \mathbf { x } } \\ & { \mathrm { e r r o r } { = } \mathbf { S U M } ( \mathrm { T e m p } \star \mathrm { T e m p } ) } \end{array}$   
S2:   
S3:   
end do

14.9雅可比松弛法MPI程序如下：参照它试写出雅可比松弛法PVM程序;并将两者加以比较。

$/ / \ast$ 雅可比松弛法的MPI编程代码段 $^ { * }$ //float Arow[N],X[N],NewX,B,error,Temp;MPI _Comm comm;  
error $\eqcirc$ SomeLargeValue;  
初始化 $\mathbf { A } , \mathbf { x }$ 和B  
MPI_Init(&argc,&argv);  
comm = MPI_COMM_WORLD;  
MPI_ Comm_rank(comm,&my_ rank);while(error>SomeErrorBound）{$\mathtt { T e m p } = \mathtt { B } ;$   
$\mathbf { f o r ( \vec { i } = 0 ; i < N ; i + \Delta + \Delta ) T e m p - = A r o w [ i ] * X [ i ] } ,$   
Temp/= A[my_rank];  
$\mathrm { \cal N e w } { \bf X } = { \sf T e m p } + { \bf X } \left[ \mathrm { \bf \ m y } \_ { \mathrm { \bf \ m a n k } } \right] ;$   
MPI_Allgather (&NewX,1,MPI_FLOAT,&X,1,MPI _FLOAT,comm);Temp $=$ Temp $\bigstar$ Temp;  
MPI _Allreduce (&Temp,&error,1,MPI _FLOAT,MPI_SUM,comm);

# 14.10Fortran 90 计算 $\pmb { \pi }$ 的程序如下：参照它试写出计算 $\pmb { \pi }$ 的 HPF程序;并将两者加以比较。

$/ / \ast$ 计算 $\pmb { \pi }$ Fortran 90编程代码段 $\star$ /

1. INTEGER,PARAMETER: : $\mathbf { N } { } = 1 3 1 0 7 2$   
2. INTEGER,PARAMETER: : LONG $=$ SELECTED_REAL_KIND(13,99)   
3. REAL( $\mathbf { \bar { \rho } } _ { \mathbf { K I N D } = \mathbf { L O N G } } ^ { \prime }$ PI,WIDTH   
4. INTEGER,DIMENSION(N) : : ID   
5. REAL $\mathbf { \tilde { \rho } } _ { \mathbf { K I N D } = \mathbf { L O N G } } )$ ,DIMENSION(N)::X,Y   
6. $\mathbf { W I D T H } = 1 . 0$ _LONG/N   
7. $\mathrm { I D } { = } \left( / ( \mathrm { I } , \mathrm { I } { = } 1 , \mathrm { N } ) / \right)$   
8. $\mathbf { X } = \left( \mathbf { I D } - \mathbf { 0 } . 5 \right) * \mathbf { W } \mathbf { I D T H }$   
9. $\mathbf { Y } { = } 4 . 0 / ( 1 . 0 + \mathbf { X } * \mathbf { X } )$   
10. $\mathbf { P I } = \mathbf { S U M } ( \mathbf { \nabla \mathbf { Y } } ) \ast \mathbf { W I D T H }$   
11. FORMAT('ESTIMATION OF PI WITH',I6,&   
12. 'INTERVALS IS',F14.12)   
13. PRINT10,N,PI   
14. END

# 附录一 MPI的函数的C语言说明

double MPI_Wtime(void)   
int MPI_Init(int $\clubsuit$ argc,char\* \* \* argv)   
int MPI_Finalize(void)

int MPI_Send(void \* buf,int count,MPI_Datatype datatype,int dest,int tag,MPI__Comm comm) int MPI_Recv (void \* buf,int count,MPI_Datatype datatype,int source,int tag,MPI_Comm comm,MPI Status \* status) int MPI_Isend (void \*buf,int count,MPI_Datatype datatype,int dest,int tag,MPI_Comm comm,MPI_

Request \* request)

int MPI_ Isend (void \* buf,int count,MPI_Datatype datatype,int dest,int tag,MPI_ Comm comm,MPI_ Request \* request)

int MPI_Wait(MPI_Request \* request,MPI_Status \* status) int MPI _Test(MPI_Request \* request,int $^ { \star }$ flag,MPI_Status \* status) int MPI_Iprobe(int source,int tag,MPI__Comm comm,int \* flag,MPI_Status \* status) int MPI_Probe(int source,int tag,MPI_Comm comm,MPI_Status \* status) int MPI _ Get __count(MPI __Status \* status,MPI _Datatype datatype,int \* count)

int MPI_ Type_contiguous(int count,MPI_Datatype oldtype,MPI_Datatype \* newtype) int MPI_ Type_vector (int count,int blocklength,int stride,MPI_Datatype oldtype,MPI_Datatype \* newtype)

int MPI_Type_indexed (int count,int \* array_of_blocklengths,int $\clubsuit$ array_of_displacements,MPI_Datatype oldtype,MPI_ Datatype \* newtype)  
int MPI_Type_commit(MPl_Datatype \* datatype)  
int MPI_ Type_free(MPI _ Datatype \* datatype)

int MPI_ Barier(MPI_Comm comm)

int MPI_Bcast(void \*bufer,intcount,MPIDatatypedatatpeintroot,MPICommcomm)

int MPI_ Gather (void \* sendbuf,int sendcount,MPI_Datatype sendtype,void \* recvbuf,int recvoount,MPI _Datatype recvtype,int root, MPI_ Comm comrm)

int MPI_ Scater (void \* sendbuf,int sendcount,MPI_Datatype sendtype,void \* recvbuf,int recvcount,MPI _Datatype recvtype,int root,MPI _Comm comm)

int MPI _ Algather (void $\nmid$ sendbuf,int sendount,MPIDatatype sendtype,void \* recvbuf,intrecvcount, MPI _Datatype recvtype,MPI _Comm comm)

int MPI_ Altoall(void \* sendbuf,int sendcount,MPI_Datatype sendtype,void \* recvbuf,int recvcount,MPI_Datatype recvtype,MPI__Comm comm)

int MPI_Reduce (void \* sendbuf,void \* recvbuf,int count,MPI_Datatype datatype,MPI_Op op ,int root, MPI _ Comm comm)

int MPI_ Alreduce (void \* sendbuf, Void \* recvbuf,int count,MPI__Datatype datatype,MPI_Op op,MPI _ Comm comm)

int MPI_Comm_ size(MPI _Comm comm,int \* size)   
int MPI_Comm_rank(MPI_Comm comm,int \* rank)   
int MPI_Comm_dup(MPI__Comm comm,MPI_Comm \* newcomm)   
int MPI __ Comm __ split(MPI _Comm comm,int color,int key,MPI __ Comm \* newcomm)   
int MPI__Comm_free(MPI__Comm \*comm)   
int MPI_Intercomm_create (MPI_Comm local_comm,int local_leader,MPI_Comm peer_comm,int remote_ leader,int tag,MPI _Comm \* newintercomm)

# 附录二 MPI的函数的Fortran语言说明

DOUBLE PRECISION MPI_WTIME() MPI_INIT(IERROR)

INTEGER IERROR MPI_FINALIZE(IERROR)

INTEGER IERROR

MPI_ SEND(BUF,COUNT,DATATYPE,DEST,TAG,COMM,IERROR)

<type>BUF( \*)

INTEGER COUNT,DATATYPE,DEST,TAG,COMM, IERROR

MPI_RECV(BUF,COUNT,DATATYPE,SOURCE,TAG,COMM,STATUS,IERROR)

<type>BUF（ \*）

INTEGER COUNT,DATATYPE,SOURCE,TAG,COMM,STATUS(MPI_ STATUS_ SIZE), IER-ROR

MPI_ ISEND(BUF,COUNT,DATATYPE,DEST,TAG,COMM,REQUEST,IERROR)

<type>BUF( \*)

INTEGER COUNT,DATATYPE,DEST,TAG,COMM,REQUEST,IERRORMPI_ IRECV(BUF,COUNT,DATATYPE,SOURCE,TAG,COMM,REQUEST,IERROR)

<type>BUF(\*)

INTEGER COUNT,DATATYPE,SOURCE,TAG,COMM,REQUEST,IERRORMPI_WAIT(REQUEST,STATUS,IERROR)

INTEGER REQUEST,STATUS(MPI_STATUS_SIZE),IERRORMPI_TEST(REQUEST,FLAG,STATUS,IERROR)

LOGICAL FLAG

INTEGER REQUEST,STATUS(MPI_ STATUS__SIZE), IERRORMPI_ IPROBE(SOURCE,TAG,COMM,FLAG,STATUS,IERROR)

LOGICAL FLAG

INTEGER SOURCE,TAG,COMM,STATUS(MPI_STATUS_SIZE),IERRORMPI_ PROBE(SOURCE,TAG,COMM,STATUS,IERROR)

INTEGER SOURCE,TAG,COMM,STATUS(MPI_STATUS_SIZE),IERRORMPI_GET_COUNT(STATUS,DATATYPE,COUNT,IERROR)

INTEGER STATUS(MPI_ STATUS_ SIZE),DATATYPE,_ COUNT,IERROR

MPI_TYPE_CONTIGUOUS(COUNT,OLDTYPE,NEWTYPE,IERROR)

INTEGER COUNT,OLDTYPE,NEWTYPE, IERROR MPI_TYPE_VECTOR(COUNT,BLOCKLENGTH,STRIDE,OLDTYPE,NEWTYPE,IERROR)

INTEGER COUNT,BLOCKLENGTH,STRIDE,OLDTYPE,NEWTYPE, IERRORMPI_TYPE__INDEXED(COUNT, ARRAY_OF_BLOCKLENGTHS,

ARRAY_OF__DISPLACEMENTS,OLDTYPE,NEWTYPE, IERROR)

INTEGER COUNT,ARRAY_OF_BLOCKLENGTHS( $\pmb { \mathscr { k } }$ ),ARRAY__ OF_DISPLACEMENTS（\*），

OLDTYPE,NEWTYPE,IERRORMPI_TYPE_COMMIT(DATATYPE,IERROR)

INTEGER DATATYPE,IERRORMPI_TYPE_FREE(DATATYPE,IERROR)

INTEGER DATATYPE,IERROR

MPI_BARRIER(COMM,IERROR)

INTEGER COMM,IERRORMPI_BCAST(BUFFER,COUNT,DATATYPE,ROOT,COMM,IERROR)

<type>BUFFER( $\pmb { \ k }$ ）

INTEGER COUNT,DATATYPE,ROOT,COMM,IERROR

ROOT,COMM,IERROR)

< type>SENDBUF( $\star$ ),RECVBUF( $\pmb { \mathscr { \star } }$ ）

INTEGER SENDCOUNT,SENDTYPE,RECVCOUNT,RECVTYPE,ROOT,COMM,IERROR MPI_ SCATTER(SENDBUF,SENDCOUNT,SENDTYPE,RECVBUF,RECVCOUNT,RECVTYPE,

ROOT,COMM,IERROR)

< type> SENDBUF( $\star$ ),RECVBUF( $\star$ ）

INTEGER SENDCOUNT,SENDTYPE,RECVCOUNT,RECVTYPE,ROOT,COMM,IERROR MPI_ ALLGATHER(SENDBUF,SENDCOUNT,SENDTYPE,RECVBUF,RECVCOUNT,

RECVTYPE,COMM,IERROR)

< type> SENDBUF( $\bigstar$ ),RECVBUF( \* )

INTEGER SENDCOUNT,SENDTYPE,RECVCOUNT,RECVTYPE,COMM,IERRORMPI_ ALLTOALL(SENDBUF,SENDCOUNT,SENDTYPE,RECVBUF,RECVCOUNT,RECVT

COMM,IERROR)

<type>SENDBUF( \*),RECVBUF（ \*)

INTEGER SENDCOUNT,SENDTYPE,RECVCOUNT,RECVTYPE,COMM,IERRORMPI_REDUCE(SENDBUF,RECVBUF,COUNT,DATATYPE,OF,ROOT,COMM,IERROR)

< type> SENDBUF( $\bigstar$ ),RECVBUF( $\pmb { \mathscr { k } }$ ）

INTEGER COUNT,DATATYPE,OP,ROOT,COMM, IERROR

MPI_ALLREDUCE(SENDBUF,RECVBUF,COUNT,DATATYPE,OP,COMM,IERROR)

< type>SENDBUF( $\star$ ),RECVBUF( $\divideontimes$ ） INTEGER COUNT,DATATYPE,OP,COMM,IERROR

MPI__COMM_SIZE(COMM,SIZE,IERROR)

INTEGER COMM,SIZE,IERRORMPI_COMM_RANK(COMM,RANK,IERROR)

INTEGER COMM,RANK,IERROR MPI_COMM_DUP(COMM,NEWCOMM,IERROR)

INTEGER COMM,NEWCOMM, IERROR

MPI_COMM_SPLIT(COMM,COLOR,KEY,NEWCOMM,IERROR)

INTEGER COMM,COLOR,KEY,NEWCOMM,IERROR MPI_COMM_FREE(COMM,IERROR)

INTEGER COMM,IERROR

API_ INTERCOMM_CREATE(LOCAL_COMM,LOCAL_LEADER,REER_COMM,

REMOTE_LEADER,TAG,NEWINTERCOMM,IERROR)

INTEGER LOCAL_ COMM,LOCAL_LEADER,PEER _ COMM; REMOTE_LEADER,TAG, NEWINTERCOMM,IERROR

# 第十五章 并行程序设计环境与工具

广义上讲,并行程序设计环境系由硬件平台、支撑语言、系统软件、应用软件包和软件工具等组成;狭义上讲,并行程序设计环境就是由一组并行程序设计工具所组成。所谓软件工具系指任何能帮助软件开发过程的辅助工具；而程序设计工具系指任何有助于程序员编程的辅助工具。显然软件工具含意较广,进行程序设计总要利用某些软件工具。所以本章先从一般的软件工具环境讲起，然后重点介绍并行程序设计语言的并行编译器以及并行程序的调试工具、性能分析工具和可视化设计工具。

# \*15.1 软件工具与环境

# 15.1.1 编码工具

编辑器(Editor） 它是一种具有编辑功能的程序设计工具,其功能从简单的文本编辑器到语法制导(Syntax-Directed)或语言敏感(Language-Sensitive)的编辑器。目前最普通的程序编辑器是知识语言(Language-Knowledgeable)编辑器,它借助语言知识来增强编辑能力,例如可自动缩进(Indentation)、括号检查，甚至简单交叉引用等。Emacs 就是这样的编辑器[79]。

编译器(Compiler）它将源代码转换成机器可执行的代码（或实际机器代码或能被解释的中间代码)形式。各种编译器的差别在于执行优化的程度不同以及它们是不是渐增的(Incremental,即只当变化时才编译)或成批的。并行编译的技术难点是对一个源程序如何识别出可并行执行的部分而将其并行化，同时保证整个程序的正确运行。本章第15.2节会专门对此进行讨论。

连接器和加载器(Linker andLoader）它们将编译好的文件与库连接在一起以产生一个可执行的文件。因为库的内容一直在增加,因此连接时间占了编辑-编译-查错总时间的相当部分。使用渐增连接器可缓解此问题，渐增连接器只修改那些已改变的可执行部分。

预处理程序(Preprocessor）它提供超过基本源语言范围的某些能力,这些能力可内置在源语言中(如C预处理器),也可以由它们自己的语言提供(如 Lex和Yacc)。

交叉引用程序(CrossReferencer）它提供将名字和其定义相关联的方法。交叉引用信息可有效地由编译器产生，它可以用在编辑器中,也可用在文本或者图形显示的独立系统中。普通图形交叉引用工具，可提供调用图和面向对象程序的类层次图的显示。

源级查错器(Source-LevelDebugger）它允许用户用设置断点等方法控制程序的执行。更先进的查错工具能够处理优化的代码和库以及同一系统中的多种语言。现今这些工具已配用程序的可视显示手段，允许程序员观察应用的数据结构。

查错辅助程序(Debugging Aids）它们提供超过程序设计语言范围的在编译或运行时的检查工具,还包括那些甚至编译器发现是合法结构的潜在问题的系统和库。

# 15.1.2 软件工程工具

这些工具牵涉到整个系统的维护而不是代码本身,现今这类工具包括：

系统构造程序(System Builder）该工具允许用户定义系统应如何建造系统模型，模型包括相关性、编译选项和应该执行什么命令等信息;然后工具应能够构筑原型系统或者基于一组源文件变化渐增的更新系统。

版本管理程序（Version Manager）该工具允许一个源文件的多种版本同时共存。这样就允许多个程序员共同开发系统,允许在新版本开发的同时维护已发布的系统的老版本,或者允许单一系统不同定制版本的共存。

设计编辑器(Design Editor）该工具使用户采用各种图形设计符号设计一个系统。CASE(Computer-Aided Software Engineering)就是这样的工具,它使用Petri网、SADT[150]、状态图和面向对象的设计OMT[151]等表示来开发软件。很多这样的工具至少能基于设计产生代码框架。如果提供足够的设计信息，有些工具能够模拟系统的若干方面,同时允许开发者在较高级测试设计。

代码产生器(Code Generator）该工具也称为第四代语言,它实际上是让程序员交互地指定系统的大部分而不必进行编码的专用高级语言。它们普遍地用于定义用户界面和程序与数据库系统的相互作用。

测试辅助程序（Testing Aids）该工具试图将测试软件系统的过程自动化。其范围从测试事例产生器(用于分析源代码或说明以产生一组测试实例)到回归测试系统(程序员产生测试事例,系统施行内务操作,包括运行每个测试实例、确定它是否成功或失败以及报告结果)。

# 15.1.3集成工具

软件工具可以使用不同的集成技术进行组合。早期,或采用不同工具的松散联合，或将所有相关的工具组合成单一系统。单一系统的优点是,紧密地将一些工具耦合在一起使得程序员对环境有所了解;其缺点是，此单一系统是个封闭系统,很难加入新的工具,或很难使用多种语言或者现存代码，而且系统相当庞大。紧密的联合可以解决不少问题,它是个开放系统,易于开发和利用新工具，且系统可以使用多种语言和库构筑之。然而，它把正确使用工具的义务转给程序员且不提供公共框架。目前已提出三种将工具集成为环境的方法：

数据集成(Data Integration）该方法使诸工具共享信息,为此要开发一个能保存各个工具必须共享的信息数据库。例如,编译器产生的中间表示可存人数据库中并且能被别的工具直接使用,以避免重新进行源程序语法分析。此法的缺点是，所要求的数据库很大，而且为了确保环境正常工作,数据库系统必须是先进的；同样这样的环境趋于封闭而不是开放。

公共前端(Common Front End）在软件开发中最流行的工具是用于生成程序、文本、系统模型等的文本编辑器。它相对容易地可嵌入编辑器的命令中，这些命令可调用其它工具并使用那些工具的输出。这种集成方法为各种工具提供一个公共的界面,而且如果它们有一个文本界面就可使新的工具很简单地被集成。因为这些工具实际不共享信息，所以程序员仍旧知道不同的工具及其使用方法。

控制集成(Control Integration）它涉及到工具之间的消息传递。在此，每当诸工具需共享信息时和调用命令时就彼此发送消息。通常不使用点到点消息传送,而是使用中央消息服务器作为中介物,每个工具都要告诉消息服务器它们对什么消息感兴趣。此法集成度较高，允许多种工具尤如是一个那样进行操作。

实际的环境可以是上述不同集成方法的组合。例如,PCTE标准[37]就使用了控制集成，以及在数据集成之上的公共前端实用程序。

# 15.1.4将来的工具与环境

因为软件的开发是个困难和费时的过程,所以人们不断地发展和推广现有的工具和环境。可以预计将来的工具一定比现在的好：较快的编译器、渐增的加载器、较好和更多的查错辅助程序和完善的编辑器等等。相应地,这些先进工具的集成会形成一个开放的环境。现在的研究旨在推广软件工具以支持一些新的领域：

过程工具(Process Tools）这些工具帮助管理软件开发过程,它们允许使用规则和步骤定义过程;然后提供过程内务操作和管理的帮助。

群件工具(Groupware Tools）这些工具允许多个程序员以受控方式联合工作。版本管理为多个程序员提供一个基础,而新的工具将会促进分布在不同场点的开发者之间的合作和交互能力的增强。

可视化工具（Visualization Tools）现行的可视化主要集中在类层次显示、调用图或模块的显示以及受限的数据结构可视化上，提供大量程序数据的高质量显示有待增强。这些将会变成软件环境的标准部分。

程序分析工具(Program Analysis Tools） 这些工具承担系统的详细语义分析并向用户提供反馈。反馈可能与潜在的问题、代码和说明之间的失配、帮助归并不同版本或重定工程代码(Reengineering Code)有关。

# 15.2 并行编译器

一旦一个程序以某种高级语言书写完成后,在正式运行前,必须将此程序转换成实际机器能够理解的机器语言(指令集)。此过程就是编译(Compile),而编译器实际上就是实现此转换的一种语言处理程序。编译过程可分为： $\textcircled{1}$ 词法分析； $\textcircled{2}$ 语法分析； $\textcircled{3}$ 中间代码产生； $\textcircled{4}$ 代码优化； $\textcircled{5}$ 代码生成等几个阶段。上述几个阶段或多或少都是顺序执行的。而并行化编译面临的任务是：给定一个在单处理机上运行较长的串行程序和一台具有多个处理器可同时工作的并行计算机,目的是将申行程序分解成若干个能并行执行或至少能重叠执行的代码段，使其在并行机上能较快地运行。所以并行编译器主要工作就是寻找代码的并行性,然后将其调度在并行机上高速正确地执行。

如图15.1所示，一个并行编译器大致可由三部分组成：流分析、程序优化和代码生成。其中，流分析是确定源代码中数据和控制的相关性;优化常常是将代码变换成与之等效但具有"更好"的形式,以利于尽量挖掘硬件潜力,最终达到全局优化的目的;代码生成通常涉及到从一种描述转换成另一种中间形式的描述，不同类型的计算机其并行代码的生成也各不相同。在正式讨论并行编译器之前,先对编译及其并行化作一概括介绍,以期读者对此有个感性的认识。

![](images/f81c689f779e56ba3980b5ca4c0cfdd850ed3181b7f3ec532fa17eee054ca550.jpg)  
图15.1并行编译过程

# 15.2.1 编译及其并行化

图15.2示出了编译器将一个高级语言的代码段翻译成汇编语言形式的机器目标代码的过程。最右边还给出了经过简单优化后使用较少指令的目标代码。

![](images/8f75f745b6bfa1f3bb85dbd7f6011262fdf83c1262f3a2f032e4369e573ec71a.jpg)  
图15.2例示编译过程

事实上,最左边的源代码经过词法分析器首先被分解成一些原子目标（即tokens),再把它们分类为操作符、常数、分隔符、标志符等;然后经过语法分析器,分析程序的文法结构、检查错误,最后转换成类似于图15.3的语法分析树；产生中间代码是为了便于移植和优化，中间代码和汇编语言的主要区别是,前者不必为每种操作之输人和输出指定实际的寄存器和存储器位置;优化的目的是使程序运行得较快和使用较少的存储器,其主要方法重排编译后的代码(即所谓代码移动),它是建立在流分析的基础上的,是程序向量化和并行化的关键。

![](images/ae5378ee1a8fdd375b0e4a1e954d135aeece98aae593ec4446b66b63b26e21c0.jpg)  
图15.3表达式 $\mathbf { A } \mathcal { B } \ast \mathbf { C }$ 与 $\mathsf { A } \div$ $\bf \Pi \cdot B \times C )$ 的分析树

一般而言，有两种并行化代码段的方法：SIMDizing(即向量化,Vectorizing)和MIMDizing(即并行化Parallelizing)。如图15.4所示，代码段的程序流图被分成几个不同的计算调度单元。此时，DO循环可被分布成三个不同的相互独立的循环,它们分别标志为"向量”、“向量"和“递归"：其中前两个循环执行简单的、相同的和独立的算术运算,因此每个循环都可用一条向量指令代替之，从而达到向量化;后一个循环涉及到递归,是彼此相关的,所以无法向量化,但可将代码分成可供MIMD多处理机执行的几个任务，每个处理器负责循环的若干次迭代,各处理器之间再施行必要的同步就可达到并行化。

![](images/516ff42a932c71f019b87379febe04ef042f43c9b7c0d2a16d252910a30c0cdc.jpg)  
图15.4两种并行化的方法

下面结合一段具体的程序代码，分别给出相应的向量化和并行化的结果，以期读者对两种并行化方法有个感性认识。

<table><tr><td rowspan=1 colspan=1>顺序代码</td><td rowspan=1 colspan=1>向量化代码</td><td rowspan=1 colspan=1>并行化代码</td></tr><tr><td rowspan=1 colspan=1>(1)A=B+C(2）DO 5 I=1,N(3)D(I)=A*E(I)(4) S=E(I) *5(5) T=T+S(6)A=D(N)-7</td><td rowspan=1 colspan=1>(1)A=B+C(3) D(1:N)=A*E(1:N)(3.1) Allocate S&#x27;(1:N)(4) S&#x27;(1:N)=E(1:N) * 5(5.1) S=S(N)(5.2) Free S&#x27;(N)(5.3) I=N+1(6) A=D(N)-7</td><td rowspan=1 colspan=1>A=B+CWith N ProcessorsLocal S&#x27;D(#)=A*E(#)S=E(#)*5T=T+S&#x27;   ■   SynchIF(# ·EQ·N)THENS=S&#x27;A=D(N)-7I=N+1ENDIF</td></tr></table>

# 15.2.2相关分析

要并行执行几个程序段，必须使每段与其它各段无关。研究计算程序中所有语句间的相关性称为相关分析(Dependency Analysis)。准确有效的相关测试对发挥并行化编译器的功效十分重要。先定义如下四种形式的相关。假定语句$\mathsf { S } _ { j }$ 继语句 $\mathsf { S } _ { i }$ 之后执行，其定义及符号约定如下：

$\textcircled{1}$ 流相关：如果从 $\mathsf { S } _ { i }$ 到 $\mathbf { S } _ { j }$ 存在执行通路,而且如果 $\mathbf { S } _ { i }$ 至少有一个输出可供$\mathsf { S } _ { j }$ 用作输人,则语句 $\mathbf { S } _ { j }$ 与语句 $\mathsf { S } _ { i }$ 流相关(Flow-Dependent),记之为 $\mathsf { S } _ { i } \delta \mathsf { S } _ { j }$ 。

$\textcircled{2}$ 反相关：如果S紧接 $\mathsf { S } _ { i }$ ，而且如果 $\mathbf { S } _ { j }$ 的输出与 $\mathsf { S } _ { i }$ 的输人重叠,则语句 $\mathsf { S } _ { j }$ 与语句 $\mathsf { S } _ { i }$ 反相关(Antidependent）,记之为 $\mathbf { S } _ { i } \overline { { \ 8 } } \mathbf { S } _ { j }$ 。

$\textcircled{3}$ 输出相关:如果两语句能产生(写)同一输出变量,则两者是输出相关(Out-put-Dependent）,记之为 $\mathsf { S } _ { i } \mathfrak { F S } _ { j }$ 。

$\textcircled{4}$ 控制相关：如果语句 $\mathsf { S } _ { j }$ 的执行依赖于语句 $\mathsf { S } _ { i } ( \mathsf { S } _ { i }$ 必须在 $\mathsf { S } _ { j }$ 之前执行),则语句 $\mathbf { S } _ { j }$ 与语句 $\mathsf { S } _ { i }$ 控制相关(Control-Dependent),记之为 $\mathrm { S } _ { i } \delta ^ { \mathrm { c S } _ { j } }$ 。

图15.5分析了上一节中所列举的顺序代码的各种相关(不包括控制相关)。

向量数组的相关分析比标量数据的相关分析要复杂得多，本节只概略讨论数据数组相关分析的基本概念,有兴趣的读者可参阅[100]。

相关距离向量和相关方向向量令 ${ \pmb { \alpha } } = ( { \pmb { \alpha } } _ { 1 } , { \pmb { \alpha } } _ { 2 } , \cdots , { \pmb { \alpha } } _ { n } )$ 和 $\pmb { \beta } = ( \beta _ { 1 } , \beta _ { 2 } , \cdots , \beta _ { n } )$ 是在 $\pmb { n }$ 层循环上界和下界范围内的 $\pmb { n }$ 个整数指标向量，假定 $\pmb { \alpha }$ 和 $\pmb { \beta }$ 存在数据相关性;则相关距离向量(Dependent Distance Vector $) \mathbf { D } { = } \left( D _ { 1 } , D _ { 2 } , \cdots , D _ { n } \right)$ 定义为$\beta - \alpha$ ,相关方向向量(Dependent Direction Vector) $\pmb { d } = ( d _ { 1 } , d _ { 2 } , \cdots , d _ { n } )$ 定义为：

$$
d _ { i } = \left\{ \begin{array} { l l } { < \ddagger { \alpha _ { i } } < \beta _ { i } } \\ { = \ddagger { \alpha _ { i } } < \beta _ { i } } \\ { > \ddagger { \alpha _ { i } } < \beta _ { i } } \end{array} \right.
$$

例如,假定有如下循环嵌套：

$$
\mathbf { D O } \mathbf { i } { = } \mathbf { L } _ { 1 } , \mathbf { U } _ { 1 }
$$

$$
\mathrm { { \bf D 0 } } \mathrm { { \bf j } } = \mathrm { L } _ { 2 } , \mathrm { { \bf U } } _ { 2 }
$$

$$
\mathbf { D O } \mathbf { \ k } = \mathrm { L } _ { 3 } , \mathrm { U } _ { 3 }
$$

$$
\mathbf { A } ( \mathrm { i } + 1 , \mathrm { j } , \mathrm { k } - 1 ) = \mathbf { A } ( \mathrm { i } , \mathrm { j } , \mathrm { k } ) + \mathbf { C }
$$

# Enddo

则数组A的三维迭代之间的相关距离向量和相关方向向量分别为(1,0，－1)和$( < , = , > )$ 。

![](images/963e07c78f77ea3f9724c31aab8ae9d76df0f2c7f0f0f53cd55afa13226e3201.jpg)

![](images/aef4826bfb9221e8247d2439f0768a776819de2817c04f486e5cc8aa5a356170.jpg)  
图15.5相关分析示例

相关类型：

<table><tr><td rowspan=1 colspan=1>（A=A</td><td rowspan=1 colspan=1>8（流），</td></tr><tr><td rowspan=1 colspan=1>1=AA=</td><td rowspan=1 colspan=1>（反）</td></tr><tr><td rowspan=1 colspan=1>A=A=</td><td rowspan=1 colspan=1>8（输出）</td></tr></table>

相关性：

381 683 68°l   
683   
584 48°4 48 5   
585 585585

相关方向向量对计算循环体间相关性十分有用。这里,相关性是通过相关方向向量中方向不是 $^ { \mathfrak { a } } = { } ^ { \mathfrak { a } }$ ”号的外层循环传递的。所以上述相关方向向量 $( < ,$ 、$\mathbf { \epsilon } = \mathbf { \epsilon } , > )$ 所表示的相关性就是在循环 $i$ 传递的。相关距离向量指明在对同一存储单元的两次访问之间循环迭代的实际距离。它们对开发并行性或优化存储器层次结构将起到指引作用。

相关方程(Dependent Equation）设 $\pmb { \alpha }$ 和 $\pmb { \beta }$ 是在 $\pmb { n }$ 层循环上界和下界范围内的n个整数指标向量。当且仅当存在α和β,并且α按字典序小于或等于β以及满足下述相关方程时，则从 $\mathbf { S } _ { i }$ 到 $\mathrm { \bf S } _ { j }$ 存在相关性：

$$
{ \int _ { i } ^ { } ( } \alpha { \ ) = } _ { E i } ( \beta )
$$

否则两次引用都是不相关的。

(15.2)式中的相关方程是循环指标变量的线性表达式。所以测试相关性相当于求解线性 Diophantine方程,它是NP-完全问题。

数据相关性测试(Dependency Testing）进行相关性测试目的有二：一是试图证明同一数组变量的下标引用对(即引用两个数组某维中的一对下标)之间的相关性是不存在的；二是若相关性存在，则应以某种方式（例如使用相关方向向量的最小全集)将它们表示出来。相关测试采用比较保守的策略，若不能证明任何相关性是不存在的话，则就认为它们是存在的。

进行相关性测试所追求的目标，就是构造相关距离向量或相关方向向量的全集。此全集可以表达对同一数组变量任意下标引用对之间可能存在的相关性。这实际上是求方程组(15.2)的通解，已如上述这是个NP-完全难解问题。精确测试是当且仅当相关性存在时,检查这些相关性,它所花费的开销太大，因而精确解无法实现,只好采用近似测试法。最常用的两个近似测试法是最大公约数测试,即GCD测试[183]和Banerjee不等式测试[24]。本书限于篇幅就不再讨论了。

# 15.2.3代码优化

代码优化(CodeOptimization)的目的是使代码执行速度达到最高,这就要求代码长度最短、存储器访问次数最少以及程序的并行性得到较好的开发。优化技术包括用流水线硬件完成向量化和同时用多台处理器实现并行化。向量化是把标量循环操作转换成等效的向量指令执行的过程；并行化的目的是把顺序代码转换成并行形式，使多台处理机能同时并行执行。向量硬件用来加速向量操作,多处理机或多计算机用来执行并行代码。本节简要讨论代码向量化方法和代码并行化方法。

代码向量化(CodeVectorization)方法向量是一维的,所以直观上讲,向量程序设计就是把标量程序中的由一种可向量化循环完成的操作改成向量操作。常用的代码向量化的基本方法包括：

①直接向量化法：它是把申行程序中的循环直接用数组运算语句来描述。

例15.1 DO $\mathbf { I } = 8 , 1 2 0 , 2$ $\mathbf { A } ( \mathbf { I } ) = \mathbf { B } { \bigl ( } \mathbf { I } + 3 { \bigr ) } + \mathbf { C } { \bigl ( } \mathbf { I } + 1 { \bigr ) }$ ENDDO

此标量循环可直接转换成一条由下列数组赋值语句定义的向量化指令：

$$
{ \bf A } ( 8 : 1 2 0 : 2 ) = { \bf B } ( 1 1 : 1 2 3 : 2 ) + { \bf C } ( 9 : 1 2 1 : 2 )
$$

②含条件语句的循环向量化：循环中的条件语句可以用WHERE语句向量化。

例15.2 DO $\mathbf { I } = 1 , \mathbf { N }$ $\mathrm { I F } \left( \mathrm { L } ( \mathrm { I } ) \cdot \mathrm { N E } \cdot 0 \right) \quad \mathrm { A } ( \mathrm { I } ) = \mathrm { A } ( \mathrm { I } ) - 1$ ENDDO

它可向量化为：

$$
\mathbf { W H E R E } ( \operatorname { L } ( \mathbf { \lambda } ) \cdot \mathbf { N E } \cdot \mathbf { 0 } ) \quad \mathbf { A } ( 1 : \mathbf { N } ) = \mathbf { A } ( 1 : \mathbf { N } ) - 1
$$

③语序重排向量化法：有时按照循环中原有的语序会因数据相关而妨碍向量化,此时交换一下语句顺序即可向量化。

例15.3 DO ${ \mathbf { I } } = { \mathbf { 1 } } \mathbf { \Gamma } , { \mathbf { N } }$ $\mathbf { A } ( \mathbf { \pi } _ { \mathrm { I } } ) = \mathbf { B } ( \mathbf { \pi } _ { \mathrm { I } } - \mathbf { 1 } )$ $\mathsf { B } ( \mathrm { I } ) = 2 * \mathsf { B } ( \mathrm { I } )$ ENDDO

上例中对B的引用导致一个妨碍向量化的流相关，但把两语句执行顺序交

换一下即可得到如下形式的向量化：

$\mathtt { B } ( 1 : \mathbb { N } ) = 2 * \mathtt { B } ( 1 : \mathbb { N } )$ $\mathrm { A } ( 1 { : } \mathrm { N } ) { = } \mathrm { B } ( 0 { : } \mathrm { N } - 1 )$

$\textcircled{4}$ 引入临时数组向量化法：通过引入中间数组，有时可消除妨碍向量化的数据相关，从而达到向量化之目的。

例15.4 D0 $\mathbf { I } = \mathbf { 1 } , \mathbf { N }$

$$
\mathbf { A } ( \mathbf { I } ) = \mathbf { B } ( \mathbf { I } ) + \mathbf { C } ( \mathbf { I } )
$$

$$
\mathrm { B } ( \mathrm { I } ) { = } 2 * \mathrm { A } ( \mathrm { I } + 1 )
$$

ENDDO

上例中关于数组A存在一个反相关,兹引临时数组TEMP 先把 $\mathbf { A } ( 2 : \mathbb { N } +$ 1)暂存起来,就可得到如下形式的向量化：

$\mathrm { T E M P } ( 1 { : } \mathrm { N } ) = \mathrm { A } ( 2 : \mathrm { N } + 1 )$ $\mathrm { A } ( \mathbf { 1 } { : } \mathbf { N } ) { = } \mathbf { B } ( \mathbf { 1 } { : } \mathbf { N } ) + \mathbf { C } ( \mathbf { 1 } { : } \mathbf { N } )$ $\mathrm { B } ( \mathrm { 1 { : } N } ) { = } 2 * \mathrm { T E M P } ( \mathrm { 1 { : } N } )$

$\textcircled{5}$ 交换循环向量化法：向量化通常在内循环而不是在外循环进行。当内循环不能向量化而外循环可以向量时，则交换一下内外循环即可实现向量化。

例15.5D0 ${ \bf I } = 2 , { \bf N }$

$$
\mathbf { D O } \quad \mathbf { J } = 2 , \mathrm { N }
$$

$$
\mathrm { A } ( \mathrm { I } , \mathrm { J } ) = ( \mathrm { A } ( \mathrm { I } , \mathrm { J } - 1 ) + \mathrm { A } ( \mathrm { I } , \mathrm { J } + 1 ) ) / 2
$$

ENDDO

ENDDO

上例中数组A在J维存在着数据相关,故在J维不能向量化,兹将两层循环交换如下：

$$
\begin{array} { r l } & { \mathrm { J } = 2 , \mathrm { N } } \\ & { \mathrm { { \bf D O } } \quad \mathrm { I } = 2 , \mathrm { N } } \\ & { \quad \quad \quad \mathrm { A } ( \mathrm { I , J } ) = ( \mathrm { A } ( \mathrm { I , J } - 1 ) + \mathrm { A } ( \mathrm { I , J } + 1 ) ) / 2 } \end{array}
$$

现在I维(内层循环)无相关性了,所以向量化的代码为：

DO ${ \mathbf { J } } = 2 , { \mathbf { N } }$ $\begin{array} { r } { \mathbf { A } ( 2 { : } \mathbf { N } , \mathbf { J } ) = \left( \mathbf { A } ( 2 { : } \mathbf { N } , \mathbf { J } - \mathbf { 1 } ) + \mathbf { A } ( 2 { : } \mathbf { N } , \mathbf { J } + \mathbf { 1 } ) \right) / 2 } \end{array}$   
ENDDO

③ 循环分离向量化法：有时一个循环中只有部分语句可向量化,此时可将整个循环分离成两个：一个含可向量化的语句；另一个含不可向量化的语句，然后将能向量化的循环向量化之。

例15.6 DO ${ \bf \Lambda } [ = 1 , 1 0 0$ $\operatorname { A } ( \operatorname { I } ) = \operatorname { B } ( \operatorname { I } ) + \operatorname { C } ( \operatorname { I } )$ $\mathrm { D } ( \mathrm { I } ) = \mathrm { D } ( \mathrm { I } - 1 ) * \mathrm { E } ( \mathrm { I } )$ ENDDO

上例中第一个语句可向量化,第二个则不能，可把它分离成如下两个循环：

DO ${ \bf { I } } = 1 , 1 0 0$ $\mathrm { A ( I ) = B ( I ) + C ( I ) }$   
ENDDO   
DO ${ \bf I } = { \bf 1 } , { \bf 1 0 0 }$ $\mathrm { D } ( \mathrm { I } ) = \mathrm { D } ( \mathrm { I } - 1 ) * \mathrm { E } ( \mathrm { I } )$   
ENDDO

这样第一个循环可向量化为：

DO ${ \bf I } = { \bf 1 } , { \bf 1 0 0 }$ $\mathrm { A } ( 1 { : } 1 0 0 ) = \mathrm { B } ( 1 { : } 1 0 0 ) + \mathrm { C } ( 1 { : } 1 0 0 )$

ENDDO

$\textcircled{7}$ 迭代区间分段向量化法：例如当循环迭代区间从正到负变化时，整个迭代区间可能要分成几段才能向量化。

例15.7 DIMENSION A(-200,200) D0 $\boldsymbol { \mathrm { I } } = - 1 0 0$ ,100 $\mathbf { A } ( \mathbf { \sigma } _ { \mathrm { I } } ) = \mathbf { 0 }$ $\mathbf { A } ( 2 \times \mathbf { I } ) = \mathbf { 1 }$ ENDDO

此程序运行结果是：

$\mathrm { A } ( - 2 0 0 ) , \mathrm { A } ( - 1 9 8 ) , \cdots , \mathrm { A } ( 0 )$ 等于1；  
$\mathbf { A } ( - 9 9 ) , \mathbf { A } ( - 9 7 ) , \cdots , \mathbf { A } ( - 1 )$ 等于0；  
A(1) $, \mathsf { A } ( 2 ) , \cdots , \mathsf { A } ( 1 0 0 )$ 等于0；  
A(102),A(104),…,A(200)等于1。

显然本例不能直接向量化为A(-100:100)=0和A(－200:200:2)=1,也不能向量化为A(-200:200:2)=1和A(－100:100)=0,但若从0为分界点，I≤0时可按该循环的语句顺序进行向量化;当I>0时则必须按语句反序进行向量化,此时可得到如下的向量代码：

$\mathbf { A } ( - 1 0 0 : 0 ) = 0$ $\mathrm { A } ( - 2 0 0 { : } 0 { : } 2 ) = 1$ $\mathrm { A } ( 2 : 2 0 0 : 2 ) = 1$ $\mathrm { A } ( 1 { : } 1 0 0 ) { = } 0$

向量化的方法还有很多,在此就不再进一步讨论了。

代码并行化(Code Parallelization)方法并行代码的优化是将一个程序展开成许多线程以供多台处理机并行执行，其目的是要减少总的执行时间。在此线程就是在一台处理机上执行的指令序列。能否将一个程序分成多个线程并行执行,依赖于程序的数据和控制相关性。理想的情况是任何两个线程之间无相关性,所以可以并行执行;当线程之间有强相关性时,若加上适当的同步操作,则含有任何相关性的两个线程也可并行执行,极端的情况是同步多得使两个线程事实上还是串行执行的。

循环一般占程序的大部分运行时间,而循环的并行化分析和改写又相对较容易,所以十多年来有关代码并行化的研究主要集中在循环的并行化方面。因为组织循环并行执行的开销一般比组织循环向量化执行的开销大得多，所以对嵌套循环作并行化时总是选择外层循环进行并行化。这样使存储器能对数组中的连续元素进行访问，并将带有长向量的循环放到最内层进行向量化,从而缩短了总的执行时间。

返回去再看一下例15.5中的两层循环嵌套。因为I循环中的所有相关关系都有相关方向 $^ { \bullet } = { } ^ { \bullet }$ ,所以这个外层循环是可以并行化的,其并行化后的代码如下：

$$
\begin{array} { r l } { \mathbf { D } \mathbf { 0 } } & { { } \mathbf { J } = 2 , \mathbf { N } } \end{array}
$$

$$
\mathrm { A } ( \mathrm { I } , \mathrm { J } ) = \left( \mathrm { A } ( \mathrm { I } , \mathrm { J } - 1 ) + \mathrm { A } ( \mathrm { I } , \mathrm { J } + 1 ) \right) / 2
$$

ENDALL

此时外层循环中的 $\Nu - 1$ 次迭代都可以调度给不同的处理机执行。每个新创建的线程都由一个带I常数下标的完整的」循环组成。

下面给出一个例子综合说明一个程序循环的串行执行、并行化、向量化执行的各种组合情况。

例15.8 在Allant FX/80 处理机上一个FX/Fortran循环的五种执行方式[10]示例在图15.6中。

FX/Fortran可以用标量、向量、并发标量、并发向量及并发外层/向量内层(COVI)等五种方式来生成代码以执行简单的DO循环。例中所涉及的计算可以对一维数据数组A(1:2048)进行;也可以对二维数据数组B(1:256:1:8)进行,其中,A(K)=B(I,J),而K=8(I-1)+J。

图15.6(a)示出了用一台处理机顺序执行标量的情况。若利用数组A,则所涉及的计算可用一个纯标量循环表示如下：

DO $\mathtt { K } = 1$ ,2048

$$
\mathbf { A } ( \mathbf { K } ) = \mathbf { A } ( \mathbf { K } ) + \mathbf { S }
$$

ENDDO

其中S是标量常数。

图15.6(d)示出了用一台配有向量硬件的处理机执行8条向量指令的情况。每条向量指令处理下列256次迭代：

$$
{ \mathrm { A } } ( 1 { : } 2 0 4 8 { : } 2 5 6 ) = { \mathrm { A } } ( 1 { : } 2 0 4 8 { : } 2 5 6 ) + { \mathrm { S } } _ { \circ }
$$

图15.6(c)示出了用8台处理机并行执行如下的标量计算(标量并发方式)：

DOALL ${ \tt I } = 1 , 8$ DO ${ \bf J } = { \bf 1 } , 2 5 6$ $\mathbf { B } ( \mathbf { I } , \mathbf { J } ) = \mathbf { B } ( \mathbf { I } , \mathbf { J } ) + \mathbf { S }$ ENDDO  
ENDALL

![](images/c8ba85c71ab45d4f20bb6a588cb28ac297f493d2d971a1dc8a980c53fd81aa14.jpg)  
图15.6Alliant 多处理机上FX/Fortran 循环五种执行方式

图15.6(d)示出了用8台全部配有向量硬件的处理机上以向量并发方式执行如下代码的情况：

DOALL $J { = } 1 , 8$ $\mathbf { A } ( \mathrm { K } { : } 2 0 4 0 + \mathrm { K } { : } 8 ) = \mathbf { A } ( \mathrm { K } { : } 2 0 4 0 + \mathrm { K } { : } 8 ) + \mathbf { S }$

ENDALL

图15.6(e)示出了8台处理机以COVI方式执行，内层向量化执行，外层并行化执行，以Fortran 90 表示符则有：

$$
\mathrm { B } ( 1 { : } 8 , 1 { : } 2 5 6 ) = \mathrm { B } ( 1 { : } 8 , 1 { : } 2 5 6 ) + \mathrm { S }
$$

在代码并行化时，下列的情况往往会阻止或妨碍并行化： $\textcircled{1}$ 多个人口或出□； $\textcircled{2}$ 函数调用或子例程调用; $\textcircled{3}$ 输入/输出语句； $\textcircled{4}$ 并行执行的非确定性； $\textcircled{5}$ 循环体间的相关性。

总之，对向量化只是向后相关性有影响，而对并行化则向前和向后相关性都有影响；同步代码的开销可能会超过并行化所带来的好处；大多数代码的并行化都集中在循环级;并行化循环应尽量在最外层进行；在考虑并行化的粒度时，必须在计算和通信之间折衷考虑等。

# 15.2.4代码生成

并行代码生成(CodeGeneration)涉及到将优化后的中间形式的代码转换成可执行的具体的机器目标代码。因为目标机包含有不同的并行结构，所以并行机的代码生成仍还限制在每台处理机的范围内进行。不同类型的计算机的并行代码的生成也很不一样。例如，超标量处理机可能用软件调度也可能用硬件调度来实现。在RISC或超标量处理机上如何优化寄存器分配，在多处理机上如何降低同步开销,在多计算机上分布的代码/数据如何实现消息传递等,这些问题都给并行代码的生成增添了不少困难。当代码自动生成不易实现时，还可以使用编译命令来帮助并行代码的生成。

代码生成所涉及的问题很多,包括执行次序、指令选择、寄存器分配、负载平衡、并行粒度、代码调度以及后优化(Postoptimization)等。先进的代码生成技术应以开发并行性为目标，要为并行机开发真正的“智能”编译器，目前还相差甚远。

# 15.3 并行程序调试和性能分析

并行程序的设计不仅编程难，而且调试和分析更难。调试的目的是为了获得一个正确的并行程序；而性能分析是为了获得一个高效的并行程序。本节就并行程序调试的难点、技术和方法，并行程序的静态性能、动态性能的分析方法和可视化设计环境与工具作一简单介绍。

# 15.3.1并行程序的调试

串行程序的调试,有比较成熟的技术和工具(如Unix的dbx)。通过这些工具，程序员(用户)可在其程序中设置断点、采用步进和施行跟踪等手段来控制程序的执行和观察程序的运行状态，从而能发现错误所在。由于串行程序中语句执行次序是确定的，所以只要输人数据不变，程序的走向和产生的结果是不变的，因而用户可以重复运行同一程序来逐步定位错误所在。

并行程序调试(Parallel Program Debugging)技术和手段尚不成熟，难以借鉴串行程序的调试方法。向量化的引人并未给程序调试带来太大的困难，因为向量化的程序仍是单指令流的程序，其仍具有运行确定的特点；并行化的引入给程序调试带来相当大的难度，因为并行化的程序语句执行的次序是不确定的。这种不确定性意味着特殊的机器指令执行序列是不可重现的，因而难以跟踪观察；同时不确定性使得并行程序对相同的输人多次运行会产生不同的结果，因而无法相互比较验证。并行程序的这一特点，使得无法使用通过运行测试来保证程序的正确性,给并行调试工具的开发带来相当困难。特别是并行调试工具还会带来所谓探针效应(ProbeEffect)，即调试工具本身的引入，可能掩盖了被调试程序中的时序错误。例如，当人们想通过输出某些运行轨迹来定位错误而加人了这些用来输出轨迹信息的测试指令时，可能改变了原指令的执行次序,从而使错误被屏蔽而不再出现。

导致并行程序产生不确定性的主要原因是：①共享变量竞争：在共享存储的多处理机系统中,通过读和写共享变量实现通信。当缺少必要的同步操作时，可能造成数据的不正确读出或写人；②发收消息竞争：在分布存储的多计算机上，通过发送和接收消息实现通信。但由于消息在行进中的遭遇不同，使得一个处理机所收到的消息次序，可能在每次程序执行中都不一样；③动态进程调度：在并行机上为了负载平衡常使用动态调度，当同步使用不当时，可能使程序在某种调度次序下正确，而在另一种调度次序下出错；④不确定的系统调用：当程序与其执行环境交互时可能引起不确定的行为；③交错的消息发送：当多个源进程向一个目的进程发送消息时，一个目的进程意外接收的消息可能妨碍了它接收真正需要的消息。

一般而言，分布式系统比共享系统中出现并行程序的不确定性更大，也更难测试。下面我们简要介绍三种常用的调试技术：断点调试、事件分析和静态分析。

断点调试(Break-PointDebugging）并行断点调试是串行断点调试方法在并行系统中的扩展。它是将多个串行断点组合在一起，每个并行任务使用一个串行断点进行调试，配合使用多窗口技术,使各个任务对应在各自的窗口中。目前已有不少商品化的调试器,其代表者有 Sequent的pdbx和Cray的mtdbx等；其断点的种类也很多：它可以是基于控制流的断点，即在源程序语句处中止程序的执行；也可以是基于事件的断点(俗称的自陷),即当例外或用户自定义的事件或访问某个变量时中止程序的执行；也可以是基于谓词的断点，即当某个条件表达式满足时中止程序的执行。

在并行环境中，断点尚有局部和全局之分：前者只中止碰到断点的任务；后者则中止并行程序中的所有任务，如果不能中止所有的任务，则有可能造成某个任务修改了它的状态，此时全局断点后所观察到的状态就不是断点发生时的状态。一般而言，全局断点的实现应有硬件直接支持。

断点调试方法的最大缺陷是探针效应，它使得无法处理时序性错误。但是，因为探针效应不会掩盖并行程序中的非时序性错误，以及当断点引人的延迟足够小时，诱发探针效应的机会也很少，所以尽管存在探针效应，它仍能在一定程度上支持并行调试。

事件分析(EventAnalysis）事件分析方法就是记录程序运行中的事件发生的有关信息,事后加以分析以帮助发现错误,系由两部分组成：一是程序运行时的事件信息记录部分；二是程序终止后的事件信息分析部分。所要记录的信息是事件分析所需要的。目前也有些商品化的此类调试器,其代表者有Cray 的GMAT和 BBN Butterfly 的 Instant。

此类调试方法所记录的事件轨迹信息主要用于阅览和重放：前者是通过对事件信息的整理,帮助用户查看有助于发现错误的有兴趣的信息,通常多窗口图形显示技术是不可少的，GMAT就属此类;后者是利用事件轨迹信息来控制程序的再执行，以重现程序的运行结果,Instant就属此类。

重放(Replay）在分布式多机系统上实现较多,其原因是重放要求记录下任务间所有同步通信的信息。而在分布式多机系统中，一般是采用消息传递同步通信的办法。同步通信和计算是分开的，所有的同步通信都必须使用通信原语指定消息收发的双方。这样在消息传递系统中，何时产生通信以及谁参与通信都很清楚，因而有关同步通信的信息就比较少，只要记录下这些少量的信息，在重放时控制程序再现这些同步通信的次序就可重放程序的运行结果。但在共享存储的多处理机系统中，同步通信和计算是分不开的，赋值和变量引用可以视为消息的发送和接收。这样每个共享存储单元的访问就可能是一次处理器间的同步通信。为了重放程序的执行，就必须记录下所有共享存储单元的访问次序，因而信息量极大。所以目前的程序重放在共享存储的多处理机系统中实现较少。

值得注意的是：即使在消息传递机制下，记录所有同步通信信息仍然是调试时的主要开销;事件分析方法尚需要硬件的支持；同样也存在着探针效应，不管其对性能影响大小如何。

静态分析(StaticAnalysis）静态分析技术目前还处于研究阶段，是在相关分析的基础上发展起来的，用来识别那些未由同步保证的任务间语句的相关性，可有效解决并行程序不确定性所引起的困难。使用静态分析工具自动检测并行程序中导致结果不确定的数据竞争，分析其产生的原因,针对性地修改程序,消除竞争,从而排除程序中的时序性错误;在此基础上,就可使用断点调试法来排除程序中的非时序性错误。但现阶段静态分析方法的计算时空量极大，限制了它能处理的程序规模;同时该方法对数据竞争的识别是保守的,可能会误判一些实际上不存在的数据竞争。所以它处理实际的并行程序的能力还有待于进一步完善。

并行程序的调试步骤并行程序的调试是复杂困难的，一般的方法和步骤为：①如果一个并行程序系由串行程序改写的，则首先应确保原串行程序运行是正确的；②如果并行机制支持单机运行并行程序，则首先应在较简单的运行环境下,尝试用单机执行并行程序,以确信并行程序的基本正确性；③如果并行程序允许处理器数目的变化,那么在单机运行正确的基础上可以逐步增加执行并行程序的处理器数以充分证实并行程序的正确性；④逐步增加并行程序中的并行成分以进一步对并行程序进行性能调试。当调试中出错时：①首先检查程序数据特性(共享或局部)定义是否正确；②在分布存储的系统上数据是分布在局存中的,当出错时应检查数据的分布是否正确;③检查数据相关或控制相关所造成的程序执行流向的可能错误；④检查同步机制是否错用或漏用同步信号使得某些相关不能满足而引起结果的不确定性，经验证明同步通信错误是较多的和难查的；③当出现固定错误时应多检查数据定义特性、依赖关系等方面；当出现不固定的错误时则应多检查同步通信等操作。

# 15.3.2并行程序的性能分析

并行程序的性能分析工具主要用来分析并行程序的性能，指导程序的优化；提供性能参数，改进系统的设计。性能分析工具一般分为静态和动态两种：前者采用模拟或分析方法获取源程序中的有关性能数据报告给用户；后者采用测量的方法收集程序运行中的各种性能数据，即时或事后报告给用户。动态性能分析所提供的数据比较准确,但灵活性较差,常随算法、问题规模、处理器数、输人数据集合以及具体的并行系统等而变化;静态性能分析能够针对不同的程序和运行环境给出性能预测，但预测的准确性却有待提高。

静态性能分析(Static Performance Analysis）静态性能分析也称为性能预测,是在源程序一级进行的。它可以是一个由用户调用的工具,也可能是一个由编译器调用的工具,编译器调用一般是为了某种优化作出决策。因为静态性能分析的方法是用模拟分析的方法实现的，而不真正地运行程序，所以只能对占用时间较多的重要的程序结构(例如循环和子程序调用等)进行分析。静态确定程序的运行轨迹一般是困难的，所以就此意义而言静态分析是一种试探性的方法。

静态性能分析所采用的体系结构模型一般是比较抽象的，忽略的一些细节常会对真实的性能有较大的影响，正是因为如此，静态性能分析的准确性是不理想的,但从现有的静态工具使用的情况来看，在大多数情况下还是能有效地指导程序优化的。静态性能预测的最大好处是可以用较小的时间代价，针对重要的程序结构，作出多种可能的性能选择。

动态性能分析(Dynamic Performance Analysis） 动态性能分析所获取的数据可由支持硬件提供,也可完全由软件的办法得到，当然硬件性能监测器也能同时收集软件所提供的信息。但硬件性能监测器可以提供很多对性能分析有很大帮助的有关机器CPU性能的参数，诸如功能部件的忙闲情况、各处理器间的通信模式、访存冲突率、Cache命中率、指令流出受阻率、同步通信频度、各类指令数等。不过这些性能参数几乎全是基于CPU的,对系统级或任务级的性能参数提供较少,所以硬件监测器在此方面的功能尚需进一步加强,同时分布存储系统除少数(如 Intel的Paragon)外一般都没有硬件监测器,这可能是因为在此类系统上,系统互连网络的性能更为关键,而CPU的性能主要由微处理器芯片所决定。

用软件的办法提供动态性能信息系由操作系统和并行运行支持系统完成，它们大都在完成其正常的功能外,还提供事件信息记录的功能。通过这些信息用户可以了解并行程序的有关性能，诸如并行度、负载平衡、等待时间等,进而可以帮助用户改进任务划分、同步互斥的组织等。但这些信息的记录都存在所谓“侵人性”,即信息记录的引人,或多或少会干扰程序的正常执行，加长程序的执行时间，甚至可能使所记录的信息不能正确反映程序的运行状态。此外，记录下来的信息太多，使得用户难以发现所感兴趣的有意义的信息。缓解此问题的办法有二：一是选择性地记录有关事件的轨迹信息;二是提供强有力的事件浏览手段。

动态性能分析工具又可分为联机的和脱机的：前者的信息记录部分和分析显示部分是同时工作的，记录的信息立即送给分析显示部分去分析，并将结果报告给用户；后者在程序运行时记录下有关信息，然后在运行中止后再进行分析并报告给用户。联机方式的优点是可及时反映程序的运行状态；缺点是信息量较小和分析程序较弱。脱机方式的优点是可提供较大的信息量和分析较准确；缺点是程序死锁时就得不到数据,不能及时反映运行状态。

并行程序的性能分析方法如何分析并行程序的性能虽无定规可循，但下述方法可供参考：①统计程序各部分执行时间,将性能分析的重点放在占时间较多的那些部分上;②分析计算量大的程序段中是计算部分、还是通信部分、还是I/O部分，从而找出并行程序的性能瓶颈;③对照理论计算的加速比和实际测量的加速比之差异,仔细分析所设计的并行程序的并行粒度是否合适、负载是否平衡、通信开销是否过大、存储访问冲突是否严重、Cache命中率是否不佳或cache颠簸现象过于明显等； $\textcircled{4}$ 从分析程序的效率和可扩放性出发，分析体系结构和算法的组合、问题尺寸和系统规模之间的比例关系等。

# 15.3.3并行程序的可视化设计环境与工具

20多年来，串行程序的设计经过结构化、过程化、面向对象技术、CASE技术、组件技术和可视化编程技术等的应用，大大提高了串行软件的开发效率。面对并行程序开发困难的局面，长期来，从事并行程序设计的人员也作了大量工作,试图将串行程序的这些有效技术引入到并行程序设计中来,并且也已开发出了一些试验性的可视并行程序设计语言和环境,包括HENCE、CODE、PSEE、Paralex、TRAPPER和GRADE等。它们的思路基本相同,都是用节点表示计算,用弧表示节点间的交互,通过一个可视的集成开发环境,采用统一的图形用户界面,将并行程序的设计、编辑、编译连接、调试和性能分析等工具集成起来，力图实现并行程序开发各个阶段的可视化。当前可视化的并行软件设计工具的趋势是,在一个图形的集成环境里,支持并行软件开发的全过程。一个典型的这样的工具集至少应包括三个主要的工具：一个可视化的程序设计工具,一个可视化的模拟系统和一个可视的程序正确性调试和行为分析工具。可视的程序设计工具和行为分析工具应该并存在同一个环境中，允许有关程序行为的信息与其设计联系起来。而目前许多现有的工具集只包含这些工具的一个子集,可视化性能分析工具通常作为一个单独的工具。

作为例子,下面给出一个使用图形应用开发环境GRADE(GRaphical Appli-cationDevelopmentEnvironment）开发并行程序的过程。它目前的组成为： $\textcircled{1}$ GRED:一个图形的并行程序编辑器，它支持图形编程语言GRAPNEL; $\textcircled{2}$ GRP2C:一个预编译器，它将图形语言程序转换成C语言和PVM函数调用的程序； $\textcircled{3} \mathrm {{ D D B G } }$ ：一个分布式调试工具； $\textcircled{4}$ Tape/PVM:一个监视工具,它在PVM程序执行期间生成跟踪文件(Trace File); $\textcircled{5}$ PROVE:一个可视化的工具,用于分析和解释Tape/PVM跟踪文件信息,并用图形方式表示出来。GRADE开发并行程序的流程如图15.7所示(其中矩形框代表不同的工具，椭圆框内是系统使用的数据文件,圆角方框表示对象库)： $\textcircled{1}$ 用户使用GRED图形语言编辑器设计和构造用图形编程语言GRAPNEL书写的并行程序; $\textcircled{2}$ 用GRP2C预编译器产生一个C/PVM源程序、一个MakeFile工程文件和一个支持图形化调试和程序行为动画显示的交叉引用文件; $\textcircled{3}$ 由生成器分别连接三个不同的库(GRAPNEL库：在GRAPNEL语言层隐藏PVM细节;PVM库:实现进程间和处理器间的通信;Tape/PVM库：为运行时监视和事件跟踪收集有关PVM调用的信息)生成可执行文件; $\textcircled{4}$ 可执行代码以调试(查错)模式或跟踪模式加载到处理器上执行：

在调试模式下,DDBG通过生成断点、单步执行和动画等指令控制程序的执行；在跟踪模式下，产生包含所有用户定义的跟踪信息的跟踪文件，这些事件通过PROVE可视化工具,为用户指出在GRAPNEL程序中的性能瓶颈。

GRADE打算作成一个复杂的程序设计环境，在此环境下用户可以用高层工具和抽象机制来开发并行程序,无需关心消息传递原语的低层细节。所有的通信原语可以用图形的方式定义,程序员在同一个图形用户界面下即可完成程序的设计，调试和性能调整。

![](images/00394bd73df6754f443d851147cc6669b558cdd473262d7d2ec5e3d0d1f75866.jpg)  
图15.7GRADE开发并行程序的流程

# 15.4 小结和导读

小结并行程序的编制、调试和性能分析是比较复杂和困难的，人们需要不同的工具来帮助程序员或用户减轻这些困难和提高程序生产率;需要一个较完善的和良好的程序设计环境来帮助调试程序、监视程序的运行和分析程序的性能。将来的工具环境应该是一个集成化的开放式的人机交互方式更为自然和谐

的环境。

本章除了概括性地介绍了一下软件工具（它包含了并行程序设计工具中的编辑、编译、连接、预处理、查错等编码工具,系统维护工具以及先进的集成工具)外，重点讨论了语言编译器。并行编译系统的技术难点是如何自动识别用户源程序中的可并行执行部分并将其并行化,其工作流程是：根据相关理论,把顺序程序转换为程序流图;将此进程流程图划分成若干并行模块;用分布式并行语言描述并行执行模块,并与系统结构相匹配；重新编译，生成可执行的目标代码。本章还对并行程序的调试和性能分析作了简要讨论。从本质上讲，调试是从并行程序执行错误的现象出发,通过某种手段找出错误代码的位置,就地改正，以获得一个正确的并行程序;性能分析以改善并行程序的性能为出发点，帮助用户发现和消除性能瓶颈，以获得一个高效的优化程序。本章最后对并行程序设计的可视化环境与工具作了简单介绍,并以GRADE为例,描述了如何用图形应用开发环境开发一个并行程序。

导读关于软件工具与环境的概述,读者可阅读[145]。Emacs编辑器描述在[79]中,SADT描述在[150]中,OMT描述在[151]中,PCTE标准描述在[37]中。关于编译原理、技术和工具,读者可阅读[8];并行编译的论述,读者可阅读[184];有关相关性分析,读者可阅读[195]和[100];关于相关测试中GCD测试读者可参阅[184],Banerjee不等式测试读者可参阅[24];有关AlliantFX/80多处理机介绍,读者可参考[10]。关于并行程序的测试和性能分析,读者可阅读[195]、[39]、[146]、[48]。关于并行程序设计语言与工具,读者可阅读[47]。关于可视化的并行程序设计环境与工具,读者可参阅[27]、[130]、[122]、[21][153]和[107]。

# 习 题

15.1分析下列代码段中三条语句间的相关关系;给出相应的相关方向向量和相关距离向量：

D0 $\mathbf { I } { = } 1 , \mathbf { N }$ DO $J { = } 2 , \Nu$ $\mathbf { S } _ { 1 }$ ： $\mathrm { \bf A } ( \mathrm { \bf I } , \mathrm { \bf J } ) = \mathrm { \bf A } ( \mathrm { \bf I } , \mathrm { \bf J } - \mathrm { \bf 1 } ) + \mathrm { \bf B } ( \mathrm { \bf I } , \mathrm { \bf J } )$ $\mathsf { S } _ { 2 }$ ： $\mathrm { C } ( \mathrm { I } , \mathrm { J } ) { = } \mathrm { A } ( \mathrm { I } , \mathrm { J } ) + \mathrm { D } ( \mathrm { I } + 1 , \mathrm { J } )$ S: $\mathbf { D ( \boldsymbol { I } , \boldsymbol { J } ) = 0 . 1 }$ ENDDOENDDO

15.2判定下列的循环,哪些是可向量化的：

$\textcircled{1}$ D0 $\mathbf { I } = 1 , \mathsf { N }$

S: A(I)=B(I)S: $\mathrm { C ( I ) } = \mathrm { A ( I ) } + \mathrm { B ( I ) }$ S: $\operatorname { E } ( \operatorname { I } ) = \operatorname { C } ( \operatorname { I } + 1 )$ ENDDO  
② DO I=1,N$\mathsf { S } _ { 1 }$ ： $\mathrm { A } ( \mathrm { I } ) = \mathrm { B } ( \mathrm { I } ) + \mathrm { C } ( \mathrm { I } + 1 )$ ${ \bf S } _ { 2 }$ ： $\mathrm { C } ( \mathrm { I } ) = \mathrm { A } ( \mathrm { I } ) \star \mathrm { D } ( \mathrm { I } )$ ENDDO  
$\textcircled{3}$ DO ${ \bf { I } } = { \bf { 1 } } , { \bf { N } }$ S: $\mathbf { A ( I ) } = \mathbf { A ( I - 1 ) } + \mathbf { 1 }$ ENDDO  
$\textcircled{4}$ DO $\mathbf { I } { = } 1 , \mathbf { N }$ S: $\mathbf { A ( I ) } = \mathbf { A ( I + 1 ) } + \mathbf { 1 }$ ENDDO  
$\textcircled{5}$ DO ${ \bf I } = 2 , { \bf N }$ D0 $\mathbf { J } { = } 2 , \mathbf { M }$ $\mathbf { A ( I , J ) } = \mathbf { A ( I , J - 1 ) } + 1$ ENDDOENDDO

15.3试述向量化下列代码段：

$\textcircled{1}$ DIMENSION A(200,200),B(200,200),C(200,200) DO $_ { 1 } = 1 , 2 0 0$ DO ${ \bf J } = 1 , 2 0 0$ $\mathrm { A ( I , J ) = B ( I , J ) * C ( I , J ) }$ ENDDO ENDDO

$\textcircled{2}$ DO ${ \bf I } = { \bf 1 } , { \bf 1 0 0 }$ $\mathbf { C ( \mathbf { I } ) = 0 . 0 }$ DO J= 1,100 $\mathrm { C } ( \mathrm { I } ) = \mathrm { C } ( \mathrm { I } ) + \mathrm { A } ( \mathrm { I } , \mathrm { J } ) * \mathrm { B } ( \mathrm { J } )$ ENDDO ENDDO

$\textcircled{3}$ D0 $\mathbf { I } { = } 1 , \mathbf { N }$ $\mathrm { B } ( \mathrm { I } , 1 ) = 0$ D0 $J { = } 1 , M$ $\mathrm { A ( I ) = A ( I ) + B ( I , J ) * C ( I , J ) }$ ENDDO $\mathrm { D } ( \mathbf { I } ) = \mathbf { E } ( \mathbf { I } ) + \mathbf { A } ( \mathbf { I } )$

# ENDDO

④ DO $\mathbf { I } = 2 , \mathbf { N }$ $\mathsf { S } _ { 1 }$ ： $\mathrm { T } ( \mathbf { I } ) = \mathbf { A } ( \mathrm { I } - \mathbf { 1 } ) + \mathbf { A } ( \mathrm { I } + \mathbf { 1 } )$ S: $\mathrm { A ( I ) } = \mathrm { B ( I ) } + \mathrm { C ( I ) }$ END

15.4分析下列循环，哪些是可并行化的：

$\textcircled{1}$ DO ${ \bf I } = 2 , { \bf N }$ $\mathrm { A } ( \mathrm { I } ) = \mathrm { B } ( \mathrm { I } ) - \mathrm { A } ( \mathrm { I } - 1 )$ ENDDO   
$\textcircled{2}$ DO $\mathtt { I } = 2 , \mathtt { N } , 2$ $\mathrm { A } ( \mathrm { I } ) = \mathrm { B } ( \mathrm { I } ) - \mathrm { A } ( \mathrm { I } - 1 )$ ENDDO   
$\textcircled{3}$ DO $\mathbf { I } { = } 1 , \mathbf { N }$ $\mathbf { X } { = } \mathbf { S Q R T } ( \mathbf { A ( I ) } )$ $\mathrm { B } ( \mathrm { I } ) = \mathbf { X } * \mathbf { C } ( \mathrm { I } ) + \mathbf { X } * \mathbf { D } ( \mathrm { I } )$ ENDDO   
$\textcircled{4}$ $\mathbf { I N D X } { = } \mathbf { 0 }$ DO $\mathbf { I } = \mathbf { A } , \mathbf { N }$ $\mathrm { I N D X } { = } \mathrm { I N D X } + 1$ $\mathrm { A } ( \mathrm { I } ) = \mathrm { B } ( \mathrm { I } ) + \mathrm { C } ( \mathrm { I N D X } )$ ENDDO   
$\textcircled{5}$ DO $\mathbf { I } { = } 1 , \mathbf { N }$ IF(A(I ) ·LT·EPSILON)GOTO 320 $\mathbf { A ( I ) } = \mathbf { A ( I ) } * \mathbf { B ( I ) }$ ENDDO 320 CONTINUE

15.5分析下列循环的语句数据相关性;如何进行循环调度并行化：

D0 $\mathbf { I } { = } 1 , \mathbf { N }$ DO $J { = } 2 , \Nu$   
$\mathsf { S } _ { \mathsf { I } }$ ： $\begin{array} { r l } & { \mathrm { \cal { A } ( I , J ) = \mathrm { \cal { B } ( I , J ) + C ( I , J ) } } } \\ & { \mathrm { \cal { C } ( I , J ) = \mathrm { \cal { D } ( I , J ) } } / 2 } \\ & { \mathrm { \cal { E } ( I , J ) = \mathrm { \cal { A } ( I , J - 1 ) } * \ x \ 2 + \mathrm { \cal { E } ( I , J - 1 ) } } } \end{array}$   
$\mathsf { S } _ { 2 }$ ：   
$\mathsf { S } _ { 3 }$ ： ENDDO ENDDO

# 算法索引

算法4.1 共享存储多处理器上求和算法 110  
算法4.2 分布存储多计算机上矩阵向量乘算法 111  
算法4.3 PRAM-EREW上累加求和算法 125  
算法4.4 APRAM上求和算法 125  
算法4.5 BSP上求和算法 126  
算法5.1 SISD上快排序算法 130  
算法5.2 PRAM-CRCW上为快排序构造二叉树算法 131  
算法5.3 失效函数的计算算法 134  
算法5.4 KMP串匹配算法 135  
算法5.5 SIMD-CC上求所有点对间最短路径算法 139  
算法5.6 超立方上快排序算法 142  
算法5.7 计算串匹配的 $\operatorname { d } { \mathrm { u e l } } ( \phi , q )$ 的算法 142  
算法6.1 MIMD机器上PSRS排序算法 144  
算法6.2 SIMD-EREW上Valiant归并算法 146  
算法6.3 PRAM上对数划分算法 147  
算法6.4 $( m , n )$ -选择网络算法 148  
算法6.5 Batcher双调归并算法 150  
算法6.6 PRAM上求上凸壳算法 152  
算法6.7 PRAM上求凸壳算法 152  
算法6.8 SIMD-TC上求最大值算法 153  
算法6.9 SIMD-TC上非递归求前缀和算法 154  
算法6.10 SIMD-EREW上求元素表序算法 155  
算法6.11 SIMD-CREW上求森林根的算法 157  
算法6.12 PRAM-CREW上Hirschberg求连通分量算法 163  
算法7.1 SISD上组合搜索算法 179  
算法7.2 SISD上分治(D&C)算法 179  
算法8.1 二维网孔上的X-Y选路算法 185  
算法8.2 超立方网络上的E-立方选路算法 186  
算法8.3 $^ { d }$ 维超立方上前缀和算法 199  
算法9.1 单处理机上矩阵转置算法 205  
算法9.2 单处理机上矩阵-向量乘算法 209  
算法9.3 单处理机上矩阵相乘算法 213  
算法9.4 单处理机上分块矩阵相乘算法 214  
算法9.5 Cannon分块乘法算法 216  
算法9.6 DNS乘法算法 221  
算法9.7 PRAM-CREW上矩阵相乘算法 225  
算法9.8 SIMD-MC²上Systolic矩阵相乘算法 225  
算法10.1 SISD上回代求解上三角方程组算法 229  
算法10.2 UMA上回代求解上三角方程组算法 230  
算法10.3 SISD上直接求解三对角方程组算法 231  
算法10.4 .SISD上求解稠密线性方程组高斯主元消去算法 234  
算法10.5 超立方多计算机上求解稠密线性方程组高斯主元消去算法 236  
算法10.6 PRAM上求解稠密线性方程组高斯-约旦消去算法 238  
算法10.7 SISD上求解线性方程组高斯－赛德尔迭代算法 240  
算法10.8 SISD上求解线性方程组雅可比迭代算法 244  
算法10.9 SISD上求解拉普拉斯方程雅可比迭代算法 246  
算法10.10 SISD上求解 $\mathbf { A } \mathbf { x } = \mathbf { b }$ 共轭梯度算法 254  
算法10.11 SISD上三对角方程组奇偶归约求解算法 257  
算法11.1 SISD上FFT迭代算法 266  
算法11.2 SISD上FFT递归算法 268  
算法11.3 SIMD-MC上FFT算法 270  
算法11.4 SIMD-BF上FFT算法 272  
算法11.5 SISD上Cormen 迭代计算FFT算法 275  
算法11.6 超立方上FFT算法 276  
算法11.7 SISD上Cormen 计算FFT算法 280

# 表格索引

表1.1 美国HPCC计划公布的重大挑战性应用课题一览表 5  
表1.2 美国ASCI计划中的并行机一览表 7  
表1.3 OptionRed系统硬件参数一览表 8  
表1.4 静态互连网络特性一览表 13  
表1.5 动态互连网络特性一览表 16  
表1.6 三代以太网特性一览表 18  
表1.7 ATM与OSI标准对应关系一览表 20  
表1.8 5种结构特性一览表 24  
表1.9 计算机科学中常用千进制单位量词一览表 33  
表2.1 5种商用SMP系统特性比较一览表 40  
表2.2 Origin2000结构配置属性一览表 41  
表2.3 Origin 2000不同层次存储器读延迟一览表 46  
表2.4 Origin 2000 带宽(GB/s)和延迟(ns)一览表 46  
表2.5 4种CC-NUMA结构比较一览表 47  
表2.6 典型MPP系统特性比较一览表 49  
表2.7 MPP所用的高性能CPU特性参数一览表 50  
表2.8 ASCI计划的3个高端MPP系统特性一览表 51  
表2.9 典型的机群系统特点一览表 61  
表2.10 20 世纪90年代我国自行研制的几种并行机一览表 68  
表2.11 曙光-1000与某些著名MPP系统性能比较一览表 75  
表2.12 SMP、MPP、COW性能比较一览表 81  
表3.1 处理器数及其相应执行时间一览表 94  
表3.2 $\Psi \big ( \pmb { \phi } , \pmb { \phi } ^ { \prime } \big )$ 一览表 94  
表3.3 $\Psi \big ( \pmb { \phi } , \pmb { \phi } ^ { \prime } \big )$ 上三角阵 95  
表3.4 $\Phi ( 0 , 2 5 , \phi , \phi ^ { \prime } )$ 上三角阵 97  
表4.1 机器的平均距离和对剖宽度一览表 119  
表4.2 $\mathbf { P } _ { i }$ 发送 $L _ { i , j }$ 个字节给 $\mathbf { P } _ { j }$ 时发送和接收时间一览表 120  
表4.3 一个超级步中的处理器发送和接收时间一览表 120  
表4.4 非阻塞发送和接收虫蚀式选路的通信单位数一览表 121  
表4.5 并行计算模型综合比较一览表 124  
表8.1 通信时间汇总一览表(使用CT方式) 196  
表12.1 串行程序设计和并行程序设计比较一览表 284  
表12.2 三种并行编程方法比较一览表 287  
表13.1 三种显式并行程序设计模型主要特性一览表 317  
表13.2 四种并行程序设计模型比较一览表 318  
表13.3 Pthreads中基本线程管理原语一览表 322  
表13.4 Pthreads中线程相互作用原语一览表 323  
表13.5 五种并行编程标准比较一览表 324  
表13.6 X3H5与OpenMP主要性能比较一览表 325  
表14.1 MPI中的数据类型一览表 338

# 示范程序索引

$/ / \star$ 用BSPLib求前缀和 $\yen 7/$ 128  
$/ / \varkappa$ 用UDP实现域名服务器代码段 $\pmb { \mathscr { k } }$ // 304  
$/ / \ast$ 用TCP实现域名服务器代码段 $\divideontimes$ // 305  
$/ / \ast$ 计算 $\pmb { \pi } \mathbf { C }$ 语言编程代码段 $\divideontimes$ // 311  
$\nearrow \nearrow$ 计算 $\pmb { \pi }$ 数据并行编程代码段 $\pmb { \mathscr { k } }$ // 314  
$/ \nearrow$ 计算 $\pmb { \pi }$ 消息传递编程代码段 $\pmb { \mathscr { k } }$ // 315  
$/ / \ast$ 计算 $\pmb { \pi }$ 共享变量编程代码段 $\star$ /1 317  
$\nearrow$ 计算 $\pmb { \pi }$ OpenMP编程代码段 $\star$ // 325  
$/ / \ast$ 计算 $\pmb { \pi }$ Pthreads编程代码段 $\star$ // 328  
$/ / \ast$ 计算 $\pmb { \pi }$ Fortran语言SPMD编程代码段 $\yen 7/$ 329  
$/ \nearrow \ *$ 求解N-皇后经理-员工编程代码段 $\pmb { \mathscr { k } }$ // 330  
$/ / \ast$ 计算 $\pmb { \pi } \mathbf { C }$ 语言MPI编程代码段 $\bigstar$ // 346  
$/ / \ast$ 计算 $\pmb { \pi } \mathbf { C }$ 语言PVM编程代码段 $\yen 74$ 351  
$\nearrow$ 高斯消去法的HPF编程代码段 $\star$ // 360  
$/ / * \mathsf { P V M }$ 主机/节点编程的hello代码段 $\yen 74$ 363  
$/ / \ast$ 高斯消去法的Fortran90编程代码段 $\yen 74$ 364  
$/ / \ast$ 雅可比松弛法的Fortran90编程代码段 $\star$ / 365  
$/ / \ast$ 雅可比松弛法的MPI编程代码段 $\star$ // 365  
$/ \nearrow \ *$ 计算 $\pmb { \pi }$ Fortran90编程代码段 $\bigstar$ // 366

# 参考文献

1Adams J et al.The Fortran 90 Handbook.McGraw-Hill,1992   
2Adams J et al.The Fortran 95 Handbook.MIT Press,1997   
3Adve S V,Hill M D,Vernon M.Comparison of Hardware and Software Cache and Cohercnce Schemes.Proc.18th Annu.Int.Symp.Computer Arch.,1991,298～308   
4 Agerwala T,Martin J L,Mirza J H,et al. SP2 System Architecture. IBM Systems Jourmal, 1995,34(2):152\~184   
5 Aggarwal A et al. Communication Complexity of PRAMs. Theoretical Computer Science,1990, 3:3\~28   
6 Agha G,Concurrent Object-Oriented Programming. Comm.of the ACM,1990,33(9):125\~ 141   
7Aho A,Hopcroft J,Ullman J. The Design and Analysis of Computer Algorithms. Addison-Wesley,1974   
8 Aho A V,Sethi R,Ulman J D.Compilers:Principles,Techniques,and Tools. Adison-Wesley, 1986   
9 Allan S J,Oldehoeft R,HEP SISAL: Paralel Functional Programming. Kowalik(Ed). Paralel MIMD Computation: HEP Supercomputers and Applications.MIT Press,1985   
10 Alliant. Alliant Product Summary. Alliant Computer Systems Corporation,1989   
11 Alpern B et al.The Uniform Memory Hierarchy Model of Computation.Algorithmic,1993   
12 Amdahl G M. Validity of Single-Processor Approach to Achieving Large-Scale Computing Capability. Proc.AFIPS Conf.，1967,483～ 485   
13Amza C et al. Treadmarks: Shared Memory Computing on Networks of Workstations. IEEE Computer,1996,29(2):18～28   
14 Anderson E et al. LAPACK User's Guide.SIAM,1992   
15 Anderson T E et al. A Case for NOW(Networks of Workstations). IEEE,Micro,1995,2:54～64   
16 ANSI Technical Committee X3H5. Parallel Processing Model for High-level Programming Languages,1993   
17 Accelerated Strategic Computing Initiative( ASCI) Program. A Report by US Department of Energy,Lawrence Livermore National Lab.，Los Alamos National Lab.，Sandia National Lab.,1996   
18 3ATM Forum.ATM User Network Interface: Version UNI3.1 Specification,1994   
19 Averbuch A,Gabber E,Gordissky B et al.A Parallel FFT on an MIMD Machine. Parallel Computing,1991,15:61～74   
20Baase S,Computer Algorithms: Introduction to Design and Analysis. Addison-Wesley,1978 21 Babaoglu Oet al. Paralex: An Environment for Paralel Programming in Distributed Systems. Proc.of ACM Int'1 Conf .on Supercomputing,1992   
22 Bailey D H et al. The NAS Paralel Benchmarks 2.0. NASA Ames Research Center Report, 1995,12: NAS-95-020   
23 Bal HE,Steiner JG,Tanenbaum A S.Programming Languages for Distributed Computing Systems. ACM Computing Surveys,1989,21(3):261～322   
24 Banerjee U.Dependence Analysis for Supercomputing.Boston: Kluwer Academic Press,1988   
25 Banerjee U. Dependence Analysis.Boston: Kluwer Academic Publishers,1996   
26 Batcher K E.Sorting Networks and Their Applications. AFIPS Proc.1968,307～314   
27 Beguelin A et al. Visualization and Debugging in a Heterogeneous Environment. IEEE Computers,1993,26(6)   
28 Berger M,Bokhair S.A Partitioning Strategy for Nonuniform Problems on Multiprocessors, IEEEXTran. Computs.,1987,C-36(5):570～580   
29 Berman F,Snyder L.On Mapping Parallel Algorithms into Parallel Architectures. Parallel J& Distributed Computing,1987,4(5):439～458   
30 Bermtsen J. Communication Effcient Matrix Multiplication on Hypercubes.Parallel Computing,1989,12:335～342   
31 Bertsekas D P and Tsitsilklis JN.Paralel and Distributed Computation: Numerical Methods. Prentice-Hall,1989   
32 Blume W,Eigenmann R.Performance Analysis of Paralelizing Compilers on the Perfect Benchmarks Programs. IEEE Trans.on Paralel and Distributed Systems,1992,3(6):643\~ 656   
33 Blume W et al. Automatic Detection of Parallelism: A Grand Chalenge for High-Performance Computing. IEEE Parallel and Distributed Technology,1994,2(3):37～47   
34 Blume W et al. Paralel Programming with Polaris. IEEE computer,1996,29(12):78～82   
35 Blumrich M A,Dubnicki C,Felten E W et al.Protected User-Level DMA for the SHRIMP Network Interface,Proc.2"dInt'1 Symp.on High-Performance Computer Architecture,1996   
36 Boden N J et al. Myrinet: A Gigabit-Per-Second Local Area Network. IEEE Micro.1995,2: 29\~36   
37 Boudier G et al. An Overview of PCTE $^ +$ .SIGPLAN,1982,2(24):248\~257   
38 Boyer R S,Moore J S.A Fast String Searching Algorithm. Comm.of the ACM,1997,20:762 \~772   
39 Brown J S. Debuggers for High Performance Computers,Proc.of the Superoomputing'93, 1993   
40Cannon L E.A Celular Computer to Implement the Kalman Filter Algorithm: Ph.D.thesis. Montana State Univ.,1969   
41Carriero N,Gelernter D.How to Write Parallel Programs. MIT Press,1990   
42Catlett C,Smarr.L. Metacomputing.Comm. of ACM,1992,35(6):44～52   
43Chaiken D,Fields C,Kwibara K et al. Director-Based Cache Coherence in Large-Scale Multiprocessor.IEEE Computer,1990,23(6):49～59   
44 Chan TF,Saad Y.Multigrid Algorithms on the Hypercube Multiprocessr. IEEE-TC,1986, C-35(11) :969\~977   
45 Chapman B et al.. Extending HPF for Advanced Data-Paralel Aplications. IEEE Paralel & Distributed Technology,1994,2(3):15～27   
46 Cheatham T,Fahmy A,Stefanescu D C et al.Bulk Synchronous Parallel ComputingA Paradigm for Transportable Software. Proc. of $2 8 ^ { \mathrm { { t h } } }$ Hawaii Int. Conf.on System Science,1995   
47 Cheng Y. A Survey of Parallel Programming Languages and Tols. Technical Report RND-93- 005,NASA Ames Research Center,1993   
48 Cheng D,Hood R.A Portable Debugger for Paralel and Distributed Programs,Proc.of the Superoomputing'94.1994   
49 Chlebus B,Vrto I.,Parallel Quick Sort.Journal of Paralel and Distributed Computing,1991, 11:332\~337   
50 Chronopoulos A T,Gear C W. On the Efficient Implementation of Pre-condition S-step Con-jugate Gradient Methods on Multiprocessors with Memory Hierarchy. Parallel Computing, 1989,11:37\~53   
51 Cole R, Vishkin U. Approximate Coin Tossing with Application's to List, Tree,and Graph Problems,Proc. 27hannu. IEEE Symposium on FOCS(Foundations of Computer Science), IEEE press1986,478～491   
52 Comer D E. Intermetworking with TCP/IP. $3 ^ { \alpha }$ Ed. Prentice-Hall,995   
53 Cooley JW,Tukey T W.An Algorithm for the Machine Calculation of Complex Fourier Series. Mathenatics of computation,1965,19(90):297～301   
54 Cormen T H,Leiserson C E,Rivest R L. Introduction to Algorithms.MIT Press,1990   
55 Culler D,Karp R,Patterson D,et al.LogP:Towards a Realistic Model of Paralel Computation.Proc.of 4th Symp. on Principles & Practice of Paralll Programming,ACM SIGPLAN, 1993,1\~12   
56 Cybenko G.Dynamic Load Balancing for Distributed Memory Multiprocessors.Parallel J& Distributed Computing,1989,7:279～301   
57 DeFanti T et al. Overview of the I-WAY: Wide Area Visual Supercomputing. Int'1 J.of Supercomputer Applications,1996,10(2)   
58 Dekel E,Nassimi D,Sahni S. Paralel Matrix and Graph Algorithms.SIAM J.on Computing, 1981,10:657\~673   
59 Dijkstra E D,Seijen W H,Gasteren A J M V. Derivation of a Termination Detection Algorithm for a Distributed Computation.Info.Proc.Lett.,1983,16(5):217～219   
501 Dincer K,FoxG C.Building a World-Wide Virtual Machine Based on Web and HPCC Technologies. Supercomputing'96 Conference Proceedings,1996