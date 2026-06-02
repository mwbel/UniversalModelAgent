blocking send（阻塞式发送），236buffered receive（有缓冲接收），237buffered send（有缓冲发送），237non-blockingreceive（无阻塞式接收），239non-blocking send（无阻塞式发送），239non-buffered receive（无缓冲接收），236non-buffered send（无缓冲发送），236receive（接收），235send（发送），235principles（原理），233SPMD model（SPMD模型），234  
microprocessor architectures（微处理器体系结构），12  
MIMD （参看multiple instruction stream multiple datastream），26，74，506  
minimal routing（最小路由选择，参看routingmechanism）  
minimum cost-optimal execution time（最小成本最优执行时间），218  
minimum execution time（最小执行时间），218  
minimum spanningtree（最小生成树），432Kruskal’s algorithm（Kruskal算法），463Prim’s algorithm（Prim算法），432,463for sparse graphs（用于稀疏图），451shared-address-space（共享地址空间），463Sollin’salgorithm（Sollin算法），463,467CRCW PRAM，463CREW PRAM，463mesh of trees（树格网），463，ring（环），463  
minimum-congestion mapping（最小拥塞映射），82  
MIPS,12  
MISD(参看multiple instruction stream,single datastream)，74  
module parallel computer（模块并行计算机），75  
Moore’sLaw（摩尔定律），2  
motion planning（动作规划），473  
MPC（参看module parallel computer），75  
MPI,240concepts（概念）avoiding deadlocks（避免死锁），246,257Cartesian topologies（笛卡儿拓扑结构），252collective communication operations （聚合通信操作），260communicators（通信器），243,272embeddings（嵌人），251groups（组），272overlapping communication with computation（计算与通信重叠）、255

topologies（拓扑结构），251examples（例子）Cannon’s algorithm（Cannon算法），254Dijkstra’s single-source shortest-path （Dijkstra单源最短路径算法），268matrix-vector multiplication（矩阵-向量相乘）,266,274odd-even sort（奇偶排序），249sample sort（样本排序），270operations（操作）all-to-all（多对多），265barrier（障碍），260broadcast（广播），261collective（聚合），260create Cartesian topologies（创建笛卡儿拓扑结构），252gather（收集），263non-blocking send and receive（无阻塞发送与接收），256prefix sum（前缀和），263querying Cartesian topologies（在笛卡儿拓扑结构中查询），252querying non-blocking send and receive （无阻塞发送和接收查询)，256querying the communicator（查询通信器），243reduction（归约），261scatter（散发），264send and receive（发送与接收），244,248splittingacommunicator（分裂通信器），272sub-dividing Cartesian topologies（细分笛卡儿拓扑结构），273MPI_Allgather, 264MPI_Allgatherv, 264MPI_Allreduce, 263MPI_Alltoall, 265MPI_Alltoallv, 266MPI_Barrier, 260MPI_Bcast, 261MPI_Cart_coord, 253MPI_Cart_create, 252MPI_Cart_rank,253MPI_Cart_shift,253MPI_Cart_sub,273MPI_Comm_rank, 243MPI_Comm_size, 243MPI_Comm_split, 272MPI_COMM_WORLD,243MPI_Finalize， 242

MPI_Gatherv, 264MPI_Get_count, 246MPI_Init,242MPI_Irecv,256MPI_Isend,256MPI_PROC_NULL,253MPI_Recv,244MPI_Reduce,261MPI_Request_free,257MPI_Scan,263MPI_Scatter, 264MPI_Scatterv,265MPI_Send,244MPI_Sendrecv,248MPI_Sendrecv_replace,248MPI_Status,245MPI_SUCCESS,242MPI_Test, 256MPI_Wait, 256multi-prefix（多前缀），189multiknapsack（多背包），508multilevel work-distribution（多层任务分配），505,513multiple instruction stream,multiple data stream （多指令流，多数据流），26,74,506multiple instruction stream,single data stream（多指令流,单数据流），74multistage network（多级网络），36butterfly（蝶形），78,79omega，36,37,78blocking nature of（阻塞特性），38perfect shuffle（完全混洗），36multithreading（多线程）impact on bandwidth（对带宽的影响），23mutex（万斥锁）alleviating overheads（减少开销），292errorcheck（错误检查），300normal（正常的），300overheads of serialization（串行化开销），292recursive（递归的），300nutex-unlock（互斥锁解锁），288nutual exclusion（相互排斥），287iegative-weight cycles（负权圈），463

network topologies（网络拓扑结构），33node latency（节点延迟，参看per-hop time）node splitting（节点分裂），505non-minimal routing（非最小路由选择，参看routing

mechanism）non-uniformmemory access（非一致内存访问），27noncomparison-based sorting（基于非比较的排序），37nonterminal nodes（非终端节点），471nowait clause in OpenMP（OpenMP中的nowait子句），31!NP-hard（NP难问题），473num_threads clause in OpenMP （OpenMP中的num_threads子句），312NUMA （参看non-uniform memory access）

odd-even sort（奇偶排序），416odd-even transposition sort（奇偶转换排序），417in shellsort（在希尔排序中），398scalability（可扩展性），398  
omega network （omega网络,参看multistage network）  
$\pmb { \Omega }$ notation（Ω符号），567  
omp for，315  
omp parallel,312  
omp_destroy_lock,330  
omp_destroy_nest_lock,330  
OMP_DYNAMIC,331  
omp_get_dynamic,329  
omp_get_max_threads,329  
omp_get_nested,329  
omp_get_num_procs,329  
omp_get_num_threads,329  
omp_get_thread_num,329  
omp_init_lock,330  
omp_init_nest_lock,330  
OMP_NESTED,322,331  
OMP_NUM_THREADS,330  
OMP_SCHEDULE,331  
OMP_SET_DYNAMIC,331  
omp_set_dynamic,329  
omp_set_lock,330  
omp_set_nest_lock,330  
omp_set_nested,329  
omp_set_num_threads,329  
omp_test_lock,330  
omp_test_nest_lock,330  
omp_unset_lock,330  
omp_unset_nest_lock,330  
one-to-al broadcast（一对多广播），149,166、185,187,341-343,351,352,357,361,368,435，442dual of（对偶）on balanced binary tree（在平衡二叉树上），153on hypercube（在超立方体中），153with all-port communication（用全端口通信），189on linear array（在线性阵列中），150onmesh（在格网中），152pipeliningmultiple broadcasts（流水线多播），16:357pseudocode（伪码），156.157  
ne-to-all personalized communication（-对多私自通信，参看scatter）  
）notation（O符号），567  
pen list（开放表），478  
'penMP,311  
atomic instructions（原子指令），325barrier（障碍），322conditional parallelism（条件并行），312critical sections（临界段），323data handing（数据处理），312,327defining parallel regions（定义并行区域），312dynamiccontrol（动态控制）number of threads（线程数），329environment variables（环境变量），330  
for loops（for循环）scheduling（调度），316library functions（库函数），328  
local variable（局部变量）  
initialization（初始化），314  
master block（主块），323  
memory consistency（内存一致性），326mergingdirectives（合并命令），320  
mutual exclusion（相互排斥），329  
nesting directives（嵌套命令），321  
numberof threads（线程数），312,328  
ordered execution（有序执行），325  
programmingmodel（编程模型），312  
reduction（归约），314  
scheduling across for loops（跨越for循环调度），319  
singleblock（单个块），323  
splitting for loops（分裂for循环），315  
synchronization（同步），322  
task parallelism（任务并行化），319  
timal matrix parenthesization（最优矩阵带括号方法），  
527  
timization equation（优化方程），516  
Jered directive in OpenMP(OpenMP中的ordered命令）,  
325  
t-of-order execution（乱序执行），15  
erhead（开销），115  
methods to reduce（归约方法），132  
erhead function（开销函数），197,215，217，227,228,231sources of（源）extra computations（额外计算）．196interprocessor communication（处理器间通信），196load imbalance（负载不平衡），196processor idling（处理器空闲），196  
owncr-computesrule（拥有者计算规则），103  
packet routing（包路由选择），54message transfer time（消息传送时间），56  
packing（包），189  
parallel best-first search（并行最佳优先搜索），496  
parallelcomputing（并行计算）books（书），8conferences（参看文献），9journals（期刊），9  
parallel depth-first search（并行深度优先搜索）analysis（分析），488,485-495assumptions（假设），486contention（争用）in accessing global variables（访问全局变量），489depth-first branch-and-bound（深度优先分支定界），495iterative deepening $\mathbb { A } ^ { * }$ （迭代加深 $\mathbf { A } ^ { * }$ )，496termination detection（终止检测），490Dijkstra’s token algorithm（Dijkstra令牌算法），490tree-based algorithm（基于树的算法），491  
parallel efficiency（并行效率，参看efficiency）  
parallel efficient problems（并行效率问题），227  
parallel platforms（并行平台）communication costs（通信成本），53message passing（消息传递），53shared-address-space（共享地址空间），61control structure（控制结构），25dichotomy of（二分法），24interconnection networks（互连网络），32logicalorganization（逻辑组织），24physical organization（物理组织），24,31  
parallel processes（并行进程），93.versus processors（与处理器比较），94  
parallelrandom access machine（并行随机访问计算机），9,31-32,75,76,227BPRAM，76concurrent write（并发写）arbitrary（任意），31common（普通），31priority（优先级），31sum（求和），32CRCW,31

CREW，31ERCW、31EREW，31,32LPRAM，76parallelruntime（并行运行时间），197cost-optimal（成本最优的），219minimum（最小的），219parallel speedup（并行加速比，参看speedup）parallel system（并行系统），195scalable（可扩展的），211,214,215,226ideally scalable（理想可扩展的），217unscalable（不可扩展的），215parallel tasks（并行任务），86characteristics of（特点），110-112parallelism（并行化）implicit（隐式），12partialpivoting（部分选主元法），366with 1-D mapping（1维映射），367with 2-D mapping（2维映射），368partitioning（划分），98input data（输人数据），101intermediate data（中间数据），101output data（输出数据），98path（路径），429cycle（圈），430shortest（最短的），436simple（简单的），429single-source shortest paths（单源最短路径），436weight of（权），430PC\* classof problems（PC\*类问题），227PE problems（PE问题，参看parallel efficient problems）Pentium（奔腾处理器），12Streaming SIMD Extensions （SIMD流扩充），25per-hop time（每站时间），54per-word transfer time（每字传送时间），54perfect shuffle（完全混洗），36permutation communication operation（置换通信操作），179,189permutations（置换），189pipelining（流水线），12,141pivoting（选主元，参看partial pivoting）pointer jumping（指针跳转），189Poisson equation（泊松方程），561polynomial function（多项式函数），565degree of（次），565linear（线性的），565positive definite matrix（正定矩阵），369POSIX threads（POSIX线程），282

Power4,12  
prefetching（预取），23  
example（例子），23  
prefix sums（前缀和），167,189,191,231  
pseudocode（伪码），168  
priorityqueue（优先队列）  
inJohnson’salgorithm（在Johnson算法中），455  
private clause in OpenMP（OpenMP中的private子句）,  
315  
problemsize（问题规模），213,226  
process mapping（进程映射）  
impact of（影响），65  
processor-time product（处理器-时间乘积，参看cost）  
producer-consumer（生产者-消费者），290  
using condition variables（使用条件变量），296  
pthread_attr_destroy,299,301  
pthread_attr_init,299  
pthread_attr_setdetachstate,299  
pthread_attr_setguardsize_np,299  
pthread_attr_setinheritsched,299  
pthread_attr_setschedparam,299  
pthread_attr_setschedpolicy,299  
pthread_attr_setstacksize,299  
pthread_cancel,301  
pthread_cond_broadcast,298  
pthread_cond_destroy,296  
pthread_cond_init,296  
pthread_cond_signal,295  
pthread_cond_timedwait,298  
pthread_cond_wait,295  
pthread_create,283  
pthread_join,284  
pthread_mutex_init,289  
pthread_mutex_lock,288  
pthread_mutex_t,288  
pthread_mutex_trylock,292,294  
pthread_mutex_unlock,288  
pthread_mutexattr_init,301  
pthread_mutexattr_settype_np,301  
Pthreads,282

quadratic function（二次函数.)，565  
quadratic-assignment（二次分配），508  
quicksort（快速排序），96,399constructed binary tree（结构化二叉树），402CRCW PRAM，402divide-and-conquer（分治），399,401pivot（主元），400

selection schemes（选择方案），401,417radix sort（基数排序），415randomized routing（随机路由选择），59reachablevertices（可达顶点），429read-write locks（读写锁），302reconfigurablemesh（可重构格网），74,80recursive decomposition（递归分解，参看decomposition）recursive doubling（递归加倍），149reduction（归约），75all-reduce（全归约）,166,185,187,189all-to-all（多对多）,157,187all-to-all reduction（多对多归约）,191,192all-to-one（多对-）,149,187,192all-to-one reduction（多对一归约）,149,166,192dual of（…的对偶，参看dual）reduction clause in OpenMP,314 （OpenMP中的reduction子句）reentrant functions（可重入函数），285RGC（参看Gray code）ring network（环形网络），44routing mechanism（路由选择机制），63adaptive（自适应的），64deterministic（确定性的），64dimension-ordered routing（维序路由选择），64E-cube routing（E立方体路由选择），64minimal（最小值），63non-minimal（非最小值），63XY-routing（XY路由选择），64RP-3,560RTA（参看recursive transposition algorithm）runtime（运行时间，参看parallel runtime）runtime scheduling in OpenMP（OpenMP中的运行时调度），318sample sort（样本排序），412hypercube（超立方体），418MPl implementation（MPI实现），270sample selection（样本选择），412splitters（分割器），412satisfiability problem（可满足性问题），492scalability（可扩展性），208-218,226,227scalabilitymetrics（可扩展性度量），222scaled speedup（可扩展加速比），223memory-constrained（内存受限的），223time-constrained（时间受限的），223serial fraction（串行部分），225scaled-speedup（可扩展加速比，参看speedup,scaled）scaling（扩展），205

time-constrained（时间受限的），231,376scan（扫描，参看prefix sums）scan vector model（扫描向量模型），189scatter（散发），167,187dualof（…的对偶，参看dual）on hypercube（在超立方体），169with all-port communication（全端口通信），189on linear array（在线性阵列），191on mesh（在格网），191schedule clause in OpenMP(OpenMP中的schedule子句）,315,316scientific computing（科学计算），537books（书），9search overhead factor（搜索开销因子），480sections directive in OpenMP （OpenMP中的sections命令），319selection（选择），189serializability（可串行性），287serializable schedule（串行调度），46SGI Origin 2000,27,30shared address space（共享地址空间），27shared clause in OpenMP（OpenMP中的shared子句）,313shared-address-space architecture（共享地址空间结构），29in parallel graph search（在并行图搜索中），496,498-500,508shared-address-space programming（共享地址空间编程）directives（命令），279lightweight processes（轻量级进程），279processes（进程），279threads（线程），279shared-memory computer（共享内存计算机），29shellsort（希尔排序），398hypercube（超立方体），417performance（性能），399shortest path（最短路径)，436,437SIMD（参看single instruction stream,multiple datastream）single directive in OpenMP （OpenMP中的single子句）,323single instruction stream,multiple data stream（单指令流,多数据流），25,26,28,74,506advantages of（优点），26examples of （例子），75single instruction stream; single data stream（单指令流，单数据流），74single-level work-distribution（单层任务分配），512,

# 513

single-port communication（单端口通信），148，186.189  
singie-source shortest paths（单源最短路径），436,4Bellman-Ford algorithm（Bellman-Ford算法），46:Dijkstra’s algorithm（Dijkstra算法），436,438,4CRCW PRAM，463EREW PRAM，463MPI implementation（MPI实现），268for multistage graph（多级图），518Johnson's algorithm（Johnson算法），455，464usingapriorinty queue（使用优先队列），456using distributed queues（使用分布式队列），45  
smoothsort（平滑排序）hypercube（超立方体），418  
snoopycache systems（侦听高速缓存系统），49performance of（性能），49  
sorting（排序），379comparison-based（基于比较的），379external（外部的），379internal（内部的），379lower-bound（下界），380noncomparison-based（基于非比较的），379process enumeration（进程枚举），380stable（稳定的），415  
sorting networks（排序网络），382,384bitonic（双调），384comparator（比较器），380depth（深度），382,386odd-even sort（奇偶排序），416  
spanning binomial tree（生成二叉树），189  
spanning forest（生成树林），432,446,447,449merging different forests（合并不同的树林），447  
spanning tree（生成树），189,432,446,447  
sparse graphs（稀疏图），431,450-451examples（例子），450grid graphs（网格图），451work imbalance（任务不平衡），451  
speculative decomposition（推测性分解，参看decomposition）  
speculative execution（推性执行），16  
speech recognition（语音识别），473  
speedup（加速比），198,198,210scaled（可扩展的），230,375superlinear（超线性的），200,228caches（高速缓存），200suboptimal serial algorithm（次优串行算法），20  
speedup anomalies（加速比异常），508speedup anomalies in parallel search（并行搜索中的加速比异常），501-505acceleration anomalies（加速异常），502analysis forDFS（DFS分析），502assumptions（假设），503best-first search（最佳优先搜索），502deceleration anomalies（减速异常），502SPMD，234  
stack splitting（堆栈分割），482,505  
star-connected network（星形连接网络），39  
startup time（启动时间）、54  
state-space graph（状态空间图），471nonterminal node（非终端节点），471states（状态），471terminal node（终端节点），471  
static interconnection networks（静态互连网络，参看interconnection networks）  
store-and-forward routing（存储转发路由选择），54message transfer time（消息传送时间），54  
subgraph（子图），430  
Sun Ultra HPC, 27  
superlinear speedup（超线性加速比），228,480  
superscalar execution（超标量执行），12example（例子），13  
symmetric matrix（对称矩阵），431  
synchronization（同步）removing it（消除），443  
$t _ { h }$ （参看per-hop time）  
$t _ { s }$ （参看startup time）  
$\pmb { t _ { w } }$ （参看per-word transfer time）  
task parallelism（任务并行化），140  
task-dependency graph（任务依赖图），86  
task-interaction graph（任务交互图），92  
tautology verification（重言式验证），506  
terminal node（终端节点），471  
$\boldsymbol { \Theta }$ notation（0符号），567  
thread（线程），280  
threadprivate directive in OpenMP (OpenMP中的  
threadprivate命令），328  
threads（线程）accessing shared data（访问共享数据），287advantages of（优点），281attributes（属性），298cancellation（取消），301creation（创建），282join（加人），284latency hiding（延迟隐藏），281

logicalmemorymodel（逻辑内存模型），280motivation for（动机），281mutex-locks（斥锁），288mutualexclusion（相万排斥），287portability（可移植性），281reentrant functions（可重入函数），285schedulingand load balancing（调度及负载平衡），281termination（终止），282,284time（时间，参看parallelruntime）time-constrainedscaling（时间受限的扩展，参看scaling）total exchange（总体交换，参看all-to-all personalizedcommunication）transitiveclosureof agraph（图的传递闭包），445transpose algorithm（转置算法，参看fast Fouriertransform)tree（树），430,446spanning（生成），432treenetwork（树形网络），42dynamic（动态的），42fattree（胖树，参看fat tree）static（静态的），42tree search（树搜索）static allocation（静态分配），480triangularmatrix（角矩阵），353,369,370triangular system（三角系统），353,369,370twiddle factors（旋转因子），538,551-552,563

UMA（参看uniform memory access）

undirectedgraph（无向图），429,431,432,433connected（连通的），430connectedcomponents（连通分量），446  
uniformmemory access（一致内存访问），27  
update protocol（更新协议），47  
vertex（顶点），429adjacent（邻接的），429connected（连通的），445reachable（可达的），429  
vertex collapsing（顶点压缩），464  
VeryLong Instruction Word Processors（超长指令字处理器），15  
VLIW（参看Very Long Instruction Word Processors）  
VLSI floor-planoptimization（VLSI布置图优化），473  
VPP 500,74  
wall-clock time（挂钟时间），195  
wave（波）spreading of computation（计算的扩散），461  
weightedadjacencymatrix（加权邻接矩阵），431  
weighted graphs（加权图），430  
work-splitting（任务分割）cutoffdepth（截止深度），483half-split（半分割），482tree search（树形搜索），482

XY-routing（XY路由选择，参看routing mechanism）