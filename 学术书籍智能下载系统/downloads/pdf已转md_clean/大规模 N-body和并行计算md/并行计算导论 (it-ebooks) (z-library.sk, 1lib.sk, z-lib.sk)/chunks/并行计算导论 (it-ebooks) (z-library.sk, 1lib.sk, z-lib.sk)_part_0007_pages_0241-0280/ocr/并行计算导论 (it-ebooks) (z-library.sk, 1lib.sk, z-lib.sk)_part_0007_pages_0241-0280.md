9 pthread_mutex_init(&(b -> count_lock)，NULL);   
10 pthread_cond_init(&(b -> ok_to_proceed)，NULL);   
1   
12   
13 void mylib_barrier (mylib_barrier_t \*b，int num_threads){   
14 pthread_mutex_lock(&(b -> count_lock));   
15 b -> count ++;   
16 if (b -> count $= \ast$ num_threads）{   
17 b -> count = 0;   
18 pthread_cond_broadcast(&(b -> ok_to_proceed)) ;   
19   
20 else   
while (pthread_cond_wait(&(b -> ok_to_proceed),   
&(b -> count_lock)） != 0);   
pthread_mutex_unlock(&(b -> count_lock));   
24 ！

在上面的障碍实现中，线程进入障碍，直至广播信号释放线程。线程逐个地被释放，因为互斥锁count_lock在线程间逐个地传递。因此，对于n个线程，这个函数的执行时间下界为非常小的 $O ( n )$ 。用多个障碍变量可加速这种障碍实现。

下面考虑另一种障碍实现方法：用 $n / 2$ 对条件变量-互斥锁来实现 $\pmb { n }$ 个线程的障碍。障碍工作如下：首先，线程配成对，每对线程共享一个条件变量-互斥锁对，指定的对成员等待两个线程以成对障碍的方式到达。一旦这种情况发生，所有指定的成员就被组织成对，这一过程一直进行到只有一个线程时才结束。此时，所有的线程都已到达障碍点。我们必须在这时释放所有的线程。不过，释放它们需要发出所有n/2个条件变量信号。完成这项工作我们同样采用层次策咯。线程对中指定的线程发送各自的条件变量信号。

1 typedef struct barrier_node {   
2 pthread_mutex_t count_lock;   
3 pthread_cond_t ok_to_proceed_up;   
4 pthread_cond_t ok_to_proceed_down;   
5 int count;   
6 mylib_barrier_t_internal;   
7   
8 typedef struct barrier_node mylog_logbarrier_t [MAX_THREADS] :   
9 pthread_t p_threads {MAX_THREADS] :   
10 pthread_attr_t attr;   
1   
12 void mylib_init_barrier(mylog_logbarrier_t b){   
13 int i;   
14 for (i = O;i < MAX_THREADS; i++）{   
15 b[i].count = 0;   
16 pthread_mutex_init (&(b[i) .count_lock)， NULL);   
17 pthread_cond_init(&(b[i].ok_to_proceed_up)， NULL);   
18 pthread_cond_init(&(bli].ok_to_proceed_down)，NULL);   
19 ！   
20   
21   
22 void mylib_logbarrier (mylog_logbarrier_t b, int num_threads,   
23 int thread_id){   
24 int i，base，index;   
25 $\ i \ = \ 2$ ;   
base = 0;   
27   
28 do{   
29 index = base + thread_id / i;   
30 if (thread_id & i == 0){   
31 pthread_mutex_lock(&(b[index) .count_lock));   
32 b[index] .count ++;   
3 while (b[index] .count < 2)   
pthread_cond_wait(&(b[index].ok_to_proceed_up),   
35 &(b[index].count_lock））;   
36 pthread_mutex_unlock(&(b[indexl .count_lock));   
37   
38 else{   
39 pthread_mutex_lock(&(b[index] .count_lock)）;   
40 blindex].count $\star + \star$   
41 if(b[index].count $= = 2$ ）   
42 pthread_cond_signal(&(b[index].ok_to_proceed_up));   
43 while (pthread_cond_wait(&(blindex] .ok_to_proceed_down),   
44 &(b[index].count_lock)） $! = 0 !$ ：   
45 pthread_mutex_unlock(&(b[index] .count_lock)）;   
46 break;   
47   
48 base $\approx$ base + num_threads/i;   
49 $i = i \times 2$ ：   
50 ）while (i <= num_threads);   
51 i=i/2;   
52 for(;i>1;i=i/2){   
53 base $\eqcirc$ base - num_threads/i;   
54 index base $\mathbf { + }$ thread_id / i;   
55 pthread_mutex_lock(&(b[index].count_lock));   
56 blindex].count = 0;   
57 pthread_cond_signal(&(b[index].ok_to_proceed_down));   
58 pthread_mutex_unlock(&(b[index] .count_lock));   
59   
60 ！

在这种障碍的实现中，可以把障碍看成为二叉树，线程到达树的叶节点。考虑有8个线程障碍的实例，线程0和线程1在一个叶节点配对。线程之一被指定为树的下一层中线程对的代表。在上面的例子中，线程0被指定为代表，它等待条件变量ok_to_proceed_up，以便线程1赶上。所有偶数编号的线程进入树的下一层。现在线程0与线程2配对，线程4与线程6配对。最终线程0与线程4配对。此时，线程0了解所有的线程已到达需要的障碍点，它通过发送条件变量ok_to_proceed_down信号释放线程。所有的线程被释放后，障碍完成。

容易看出，对于 $\pmb { n }$ 个线程的障碍，树中有 $\scriptstyle n - 1$ 个节点。每个节点与两个条件变量对应，一个变量用来释放线程，让线程赶上，另一个用来释放线程，让线程中止。另外，每个节点还与一个锁以及到达该节点的线程数目对应。树节点线性排列在数组mylog_logbarrier_t中，n/2个叶节点中含有前n/2个元素，更高一层中n/4个树节点含有n/4个元素，以此类推。

研究这个程序的性能很有意义。由于线性障碍中的线程一个接一个地被释放，可以作出合理的预测：即使在多处理器中，运行时间也与线程的数目成线性关系。图7-3绘出1000个线性障碍在32个处理器的SGIOrigin2000上的运行时间。串行障碍的线性运行时间很清楚地在运行时间中反映出来。在一个处理器上执行的对数障碍的工作量渐近地等于一个串行障碍（虽然有一个更大的常数）。然而，在并行计算机上，在二叉障碍树的子树被分配给不同处理器这样一种理想的情况下，运行时间以O(n/p+logp)增长。如果不能像子树分配给每个处理器一样相应地检查或者分配成块的线程，虽然这一点很难做到，但对数障碍还是显示出比串行性障碍好得多的性能。对于给定数目的处理器，当n变大时，对数障碍的性能趋于与n成线性关系，因为在式O(n/p+logp)中，n/p项在执行时间中开始对logp项占支配位置。无论从观察中还是从直观分析中都能得出这样的结论。

![](images/18a135411773672e1aa2e6b6f3f5e1c63b29d4957c51c370be64bb1313d0d969.jpg)  
图7-3在32个处理器的SGIOrigin 2000上，1000个线性障碍和对数障碍的运行时间与线程数目的函数关系

# 7.9设计异步程序的技巧

设计多线程应用程序时，一定要记住，不能假设有关其他线程的任何执行顺序。任何这种顺序都必须用前面讨论过的同步机制显式地建立：互斥锁、条件变量以及连接。另外，系统也可以提供其他同步手段。但是，由于可移植性的原因，不提倡使用其他形式的同步。

在许多线程库中，线程在半确定性的时间间隔切换，这样的库在程序中更能原谅同步错误。这种库称为轻微异步（slightly asynchronous）库。另一方面，内核线程（内核支持的线程）以及在多个处理器上调度的线程却较少宽容错误。因此，关于线程库中异步的等级，程序员一定不能做任何假设。

下面看看由于不正确地假设线程的相对执行时间而导致的常见错误：

·比方说，线程T1创建另一个线程T2，T2需要从T1得到一些数据。这种数据通过全局内存单元传送。然而，线程T1在创建T2后才把数据放到指定单元。此处隐含的假设为：T1在阻塞前不会被切换；或者T2只在T1存放完数据后才访问数据单元。由于T1在创建T2后可能立刻被切换，这种假设就可能导致错误。在这种情形下，T1将接收未被初始化的数据。

·假设和前一种情况一样，线程T1创建线程T2，然后需要传送数据给驻留堆栈中的线程T2。它通过传递一个指向线程T2在堆栈位置的指针传送数据。假设T1在T2被调度前运行结束。此时，栈帧已被释放，而一些其他的线程可能覆盖原先由栈帧指向的空间。在这种情况下，线程T2从单元读出的数据可能是无效的。同样的问题也会发生在全局变量上。

·强烈建议不要使用调度技术作为同步的手段。在并行计算机中，要记录调度决策是极其困难的。而且，当处理器数目改变时，根据线程的调度策略，这些问题可能会改变。事实上，较低优先级的线程运行时，较高优先级的线程可能在等待。

下面推荐有助于减少线程化程序错误的一些经验方法。

·在实际创建线程前，将线程的所有需求设置好。这包括初始化数据、设置线程属性、线程优先级以及互斥锁属性等。一旦创建一个线程，在创建线程重新调度前，新创建的线程可能实际运行结束。  
·当两个线程间的某些数据项存在生产者-消费者关系时，一定要保证生产者线程在数据被消费前存放数据，且保证中间缓冲区不溢出。  
·在消费者端，要保证数据能保留到所有潜在的消费者都消费了数据。这一点特别与堆栈变量有关。  
·在可能的情况下，定义和使用组同步以及数据复制。这样能显著地提升程序性能。

虽然上面这些简单技巧为编写无错误的线程程序提供了准则，在实际编程时还是要特别小心，以避免与同步有关的竞赛条件以及并行开销。

# 7.10OpenMP：基于命令的并行编程标准

本章的第一部分讲述了使用线程API在共享地址空间计算机上编程。虽然对这些API的标准化及支持已有了很长的时间，但使用者主要还是系统程序员而不是应用程序员。其原因之一是，像Pthreads这样的API被认为是低层原语。依照常识，许多应用程序可由较高层的结构（或命令）有效地支持，程序员不用对线程进行操作。这种基于命令的语言已存在很长时间，但直到最近才以OpenMP的形式完成了标准化。OpenMP是一种可以用FORTRAN、C以及 $\mathbf { C } + +$ 在共享地址空间计算机上进行编程的API。OpenMP命令提供对并发、同步以及数据处理的支持，但不需要显式设置互斥锁、条件变量、数据范围以及初始化。在本章其余部分将使用OpenMP C API。

# 7.10.1OpenMP编程模型

下面先用一个简单的程序来开始讲述OpenMP编程模型。C语言及 $C + +$ 中的OpenMP命令基于#pragma编译器命令，命令本身由命令名及后面的子句构成。

#pragma omp directive [clause list]

除非遇到parallel命令，否则OpenMP程序串行执行。parallel命令用来创建一组线程。线程的确切数目可由命令指定，用一个环境变量指定，或者在运行时用OpenMP函数指定。遇到parallel命令的主线程变为这一组线程的主（master）线程。在这一组中，它被分配的线程id为0。parallel命令的原型如下：

1 #pragma omp parallel [clause list]   
2 /\* structured block \*/   
3

每个由这条命令创建的线程执行由parallel命令指定的structured block。子句列表用来指定条件并行、线程数目以及数据处理。

·条件并行：子句if（标量表达式）决定并行结构是否将导致创建线程。一条parallel命令只能使用一个if子句。

·并发度：子句num_threads（整数表达式）指定由parallel命令创建的线程数目。

·数据处理：子句private（变量表）表示指定的变量集对每个线程都是本地的—一即每个线程对表中的每个变量都有一个副本。子句firstprivate（变量表）与子句private类似，除了进入线程变量的值要在parallel命令前初始化成相应的值以外。子句shared（变量表）表示表中的所有变量对于所有线程都是共享的，即只有一个副本。当用线程处理这些变量以保证串行性时，一定要特别小心。

![](images/751513fc88d6b0632e6f0dbe4f691e452eac255b87675e65e581d925cb19572b.jpg)  
图7-4OpenMP程序样本以及可能由OpenMP编译器执行的该程序的Pthreads 翻译

·观察对应的Pthreads翻译内容，就很容易理解OpenMP的并发模型。图7-4中列出一种可能的从OpenMP程序到Pthreads程序的翻译。感兴趣的读者可能注意到，这种翻译可以轻易地通过Yacc或CUP脚本自动实现。

# 例7.9 使用parallel命令

1 #pragma omp parallel if (is_parallel $\ l = \ \ l \textbf { 1 }$ ) num_threads(8) \   
2 private (a) shared (b) firstprivate(c)   
3 {   
4 /\* structured block \*/   
5 一

程序中，如果变量is_parallel的值等于1，就创建8个线程。每个线程得到变量a和变量c的私有副本，并共享变量b的值。此外，c的每个副本的值用parallel命令之前的c的值进行初始化。

变量的默认状态由子句default（shared）或default（none）指定。子句default（shared）表明，在默认情况下，一个变量被所有的线程共享。子句default（none）表明，线程中用到的每个变量的状态必须显式指定。通常要防止由无意的对共享数据的并发存取引起的错误。

像子句firstprivate指定变量的多个本地副本如何在线程中初始化一样，当多个线程退出时，子句reduction指定在不同线程中的变量的多个副本如何在主线程中组合成一个副本。子句reduction的用法为reduction（操作符：变量表)。这个子句用操作符对变量表中指定的标量变量进行归约。表中的变量被隐式指定为对线程私有。操作符可以是 $^ +$ ，\*，-，&，l，^，&&或Il。

# 例7.10 使用reduction子句

#pragma omp parallel reduction(+: sum) num_threads(8)   
3 /\* compute local sums here \*/   
4 ！   
5 /\* sum here contains sum of all local instances of sums \*/

本例中，8个线程中的每一个都获得变量sum的一个副本。当多个线程退出时，所有本地副本的和存储在变量的一个单一副本中 (在主线程)。 □

除了上面讲的数据处理子句外，还有另一个子句copyin。在我们讨论数据范围后，将在7.10.4节详细地讲述copyin子句。

至此，我们能用parallel命令及多种子句编写第一个OpenMP程序。为便于介绍我们引入两个函数：函数omp_get_num_threads（)返回并行范围内的线程数目，函数omp_get_thread_num()返回每个线程的整数id（回想主线程的id为0）。

# 例7.11 用OpenMP命令计算PI

我们第一个OpenMP程序仿照例7.2，用一个Pthreads程序计算 $\pmb { \pi }$ 。并行命令指定除npoints以外的所有变量都是本地的，npoints为穿过所有线程的二维空间中的随机点的总数。此外，命令指定有8个线程，所有线程执行完毕后sum的值是每个线程中的本地值之和。函数omp_get_num_threads用来确定线程的总数。和例7.2一样，一个for循环用来产生所需数目的随机点（在二维空间)，并确定有多少个点位于指定的单位直径的圆内。

1   
2 An OpenMP version of a threaded program to compute PI.   
3   
4   
5 #pragma omp parallel default (private) shared (npoints) \   
6 reduction(+: sum) num_threads(8)   
7 {   
8 num_threads $\clubsuit$ omp_get_num_threads(）;   
9 sample_points_per_thread npoints / num_threads;   
10 sum $\approx ~ 0$   
1 for $( \textbf { i } \textbf { \em o }$ i < sample_points_per_thread; $\pm +$   
12 rand_no_x $=$ (double) (rand_r(&seed))/(double)((2<<14)-1);   
13 rand_no_y (double) (rand_r(&seed))/(double)((2<<l4) -1):   
14 if (((rand_no_x - 0.5)\* (rand_no_x - 0.5) +   
15 (rand_no_y - 0.5) \* (rand_no_y - 0.5)) < 0.25)   
16 sum $^ { \ast \ast }$   
17   
18

# 与相应的POSIX线程程序相比，该程序在指定创建和终止线程方面更容易编写。

# 7.10.2在OpenMP中指定并发任务

命令parallel可以和其他命令--起用于指定通过迭代和任务的并发。OpenMP提供两条命令— -for和sections 用来指定并发的迭代和任务。

# 1.for命令

for命令用来在多个线程间分割并行迭代空间。for命令的一般形式如下：

#pragma omp for [clause 1ist] /\* for loop \*/

这种情况下可用的子句有private:firstprivate、lastprivate、reduction、schedule、nowait和ordered。前4个子句用来处理数据，这4个子句的语义和parallel命令中-样。子句lastprivate用来处理变量的多个本地副本在并行for循环结束时如何写回到单一副本中。当使用for循环（或者将会见到的sections命令）将工作分配给线程时，有时候需要在for循环的最后一次迭代（与串行执行定义的一样）中更新变量的值。这一点是通过lastprivate命令实现的。

# 例7.12 用for命令计算 $\pi$

回顾例7.11，for循环的每次迭代都是独立的，由此可以并发地执行。在这种情况下，可以用for命令简化程序。修改后的代码段如下：

1 #pragma omp parallel default(private) shared (npoints) \   
2 reduction(+: sum) num_threads(8)   
3 {   
4 $\sin = 0 ;$   
5 #pragma omp for   
6 for (i = 0; i < npoints; $\mathbf { i } + +$ ）{   
7 rand_no_x $\pmb { \ x }$ (double)(rand_r(&seed))/(double)((2<<l4)-1);   
8 rand_no_y $\pmb { \mathfrak { s } }$ (double)(rand_r(&seed))/(double) ((2<<l4)-1) :   
9 if (((rand_no_x - 0.5) \* (rand_no_x - 0.5) +   
10 (rand_no_y - 0.5) \* (rand_no_y - 0.5)) <a0.25)   
11 8um ++;   
12   
13

这个例子中的for命令用来指定后面紧跟着的for循环必须并行执行，即在多个线程间分割。请注意，与例7.1l中的sample_points_per_thread不同，本例中的循环索引从0到npoints。默认情况下，for命令的循环索引假设为私有。注意这段OpenMP代码与对应的串行代码间只有两条命令的区别。本例说明，将许多串行程序转换为基于OpenMP的线程程序非常简单。 □

# 2.将迭代分配给线程

for命令的schedule子句用来将迭代分配给线程。schedule命令的一般形式为schedule(scheduling_class[,parameter]）。OpenMP支持4种调度类:static、dynamic、guided和runtime。

# 例7.13 OpenMP中的调度类 一矩阵相乘

本例用稠密矩阵相乘来研究不同的调度类。将矩阵a与矩阵b相乘得到矩阵c的代码如下：

$$
\begin{array} { r l r l r l r l r l r } & { { } } & { \quad } & { } & { { } } & { \hat { \mathcal { G } } _ { \theta , \theta , \theta , \theta , \theta , \eta } } & { \quad } & { { } } & { \hat { \mathcal { G } } _ { \theta , \theta , \theta , \eta } } & { \quad } & { { } } & { \hat { \mathcal { G } } _ { \theta , \theta , \theta , \eta } } & { \quad } & { { } } & { \hat { \mathcal { G } } _ { \theta , \theta , \theta , \eta } } & { \quad } & { { } } & { \hat { \mathcal { G } } _ { \theta , \theta , \theta , \eta } } & { \quad } & { { } } & { \hat { \mathcal { G } } _ { \theta , \theta , \theta , \eta } } & { \quad } & { { } } & { \hat { \mathcal { G } } _ { \theta , \theta , \theta , \eta } } & { \quad } & { { } } & { \hat { \mathcal { G } } _ { \theta , \theta , \theta , \eta } } & { \quad } & { { } } & { \hat { \mathcal { G } } _ { \theta , \theta , \theta , \eta } } & { \quad } & { { } } & { \hat { \mathcal { G } } _ { \theta , \theta , \theta , \eta } } & { \quad } & { { } } & { \hat { \mathcal { G } } _ { \theta , \theta , \theta , \eta } } & { \quad } & { { } } & { \hat { \mathcal { G } } _ { \theta , \theta , \theta , \eta } } & { \quad } & { { } } & { \hat { \mathcal { G } } _ { \theta , \theta , \theta , \eta } } & { \quad } & { { } } & { \hat { \mathcal { G } } _ { \theta , \theta , \theta , \eta } } & { \quad } & { { } } & { \hat { \mathcal { G } } _ { \theta , \theta , \theta , \eta } } & { \quad } & { { } } & { \hat { \mathcal { G } } _ { \theta , \theta , \theta , \eta } } & { \quad } & { { } } & { \hat { \mathcal { G } } _ { \theta , \theta , \theta , \eta } } & { \quad } & { { } } & { \hat { \mathcal { G } } _ { \theta , \theta , \theta , \eta } } & { \quad } & { { } } & { \hat { \mathcal { G } } _ { \theta , \theta , \eta } } & { \quad } & { { } } & { \hat { \mathcal { G } } _ { \theta , \theta , \eta } } & { \quad } & { { } } &  \hat  \end{array}
$$

1 for(i = 0;i < dim;i++){   
2 for (j = 0;j < dim; j++){   
3 c(i,j)= 0;   
4 for (k = 0;k < dim;k++){   
5 c(i,j)+= a(i，k)\*b(k，j);   
6   
7   
8

上面的代码段指定一个三维迭代空间，为学习OpenMP中不同的调度类提供了理想的例子。 □

static调度 static调度类的一般形式为schedule(static[,chunk-size]）。它将迭代空间分割成大小为chunk-size的相等的块，并将这些块以循环的方式分配给线程。如果没有指定chunk-size，迭代空间就分成与线程数目一样多的块，每个块分配给每个线程。

# 例7.14矩阵相乘的循环static调度

下面修改后的矩阵相乘程序使最外面的迭代在多个线程间静态分割，如图7-5a所示。

1 #pragma omp parallel default(private) shared (a，b，c，dim)\   
2 num_threads(4)   
3 #pragma omp for schedule(static)   
4 5 for $\begin{array} { r l }  \mathrm {  ~  \begin{array} { l l l l l l l l l } { \mathrm {  ~  ( ~ i ~  ~ } = } & { 0 ; } & { \mathrm {  ~ i ~ } < } & { \mathrm { d } \mathrm { i m } ; } & { \mathrm {  ~ i ~ } + + \mathrm {  ~ \Lambda ~ } } \end{array} ) ~ } \{ \begin{array} { l l l l l l l l l } \\ { \mathrm {  ~  \begin{array} { l l l l l l l l l } { \mathrm {  ~ \Lambda ~ } } & { 0 ; } & { \mathrm {  ~ j ~ } < } & { \mathrm { d } \mathrm { i m } ; } & { \mathrm {  ~ j ~ } + + \mathrm {  ~ \Lambda ~ } } \end{array}  } \{ \begin{array} { l l l l l l l l l } { \mathrm {  ~ \Lambda ~ } } & { \mathrm {  \Lambda ~ } } & { \mathrm {  ~ \Lambda ~ } } & { \mathrm {  ~ \Lambda ~ } } & { \mathrm {  ~ \Lambda ~ } } & { \mathrm {  ~ \Lambda ~ } } & { \mathrm {  ~ \Lambda ~ } } \\ { \mathrm {  ~ \Lambda ~ } } & { \mathrm {  ~ c ~ } ( \mathrm {  ~ i ~ } , \mathrm {  ~ j ~ } ) } & { = } & { 0 ; } & { } & { } & { \mathrm {  ~ \Lambda ~ } } & { \mathrm {  ~ \Lambda ~ } } \end{array}  } &  \{ \begin{array} { l l l l l l l l l } { \mathrm {  ~ \Lambda ~ } } & { \mathrm {  \Lambda ~ } } & { \mathrm {  ~ \Lambda ~ } } & { \mathrm {  ~ \Lambda ~ } } & { \mathrm {  ~ \Lambda ~ } } & { \mathrm {  ~ \Lambda ~ } } \\ { \mathrm {  ~ \Lambda ~ } } & { \mathrm {  ~ c ~ } ( \mathrm {  ~ i ~ } , \mathrm {  ~ j ~ } ) } & { + = } & { \mathrm {  ~ a ~ } ( \mathrm { i ~ } , \mathrm {  ~ \Lambda ~ } ) } & { \mathrm {  ~ \Lambda ~ } } &  \star { \mathrm {  ~ \Lambda ~ } } \mathrm {  ~ \Lambda ~ } \mathrm {  ~ \Lambda ~ } \mathrm {  ~ \Lambda ~ } \mathrm {  ~ \Lambda ~ } \mathrm {  ~ \Lambda ~ } \mathrm {  ~ \Lambda ~ } \mathrm {  ~ \Lambda ~ } \mathrm {  ~ \Lambda ~ } \mathrm {  ~ \Lambda ~ } \mathrm {  ~ \Lambda ~ } \mathrm {  ~ \Lambda ~ } \mathrm {  ~ \Lambda ~ } \mathrm {  ~ \Lambda ~ } \mathrm {  ~ \Lambda ~ } \mathrm   \end{array} \end{array} \end{array}$   
6   
7   
8   
9   
10   
11

由于一共有4个线程，且没有指定块的大小，如果 ${ \dot { \bf d i m } } = { \bf 1 } 2 8$ ，则每个分区的大小为32列。使用schedule(static，16)将导致如图7-5b所示的迭代空间划分。若例7.13中程序的每个for循环在多线程间用schedule(static)并行化，且允许嵌套并行，则划分的结果如图7-5c所示，这是空间分割的另一个例子（参见7.10.6节）。 □

![](images/f70ae5b7581537393a19360aa2fb713bbda2a67acfa4c9171eb3970c5e800d8f.jpg)  
图7-5使用OpenMP的static调度类的3种不同调度

dynamic调度通常，由于许多原因，从不同类的计算机资源到非均匀处理器负载，同等划分的工作负载的执行时间有很大的差别。因此，OpenMP中有一个dynamic调度类，这个类的一般形式为schedule(dynamic[,chunk-size]）。迭代空间被划分成chunk-size大小的块。但是，这些块只在线程变为空闲时才分配给它们。这样就能考虑到由static调度造成的瞬时不平衡。如果没有指定chunk-size，则默认为每个块一个迭代。

guided调度如果迭代空间中有100次迭代，块大小为5，则迭代空间将被分成20块。如果有16个线程，在最佳情况下，12个线程的每个线程得到1块，其余4个线程的每个线程得到2块。因此，如果处理器与线程的数量一样多，这样的配送就会导致可观的空闲。这个问题（也称为边缘效应（edgeeffect））的解决办法是在计算的进行过程中减少块的大小。这是guided调度类的原则。这个类的一般形式为schedule(guided[,chunk-size])。在这个类中，当每个块分配给每个线程时，块的大小按指数缩小。chunk-size为应分配的最小块的大小。因此，当剩余的迭代数目小于chunk-size时，所有的迭代将一次分配完。如果chunk-size的大小没有指定，则默认为1。

运行时间通常需要将调度决策延迟到运行时间。例如，如果想看到不同的调度策略的影响，然后再选出最佳的一种，就可以将调度设置为runtime。在这种情况下，由环境变量OMP_SCHEDULE决定调度类以及块的大小。

当不用ompfor命令指定调度类时，实际的调度方法就没有指定，而要依靠具体的实现。for命令对跟在它后面的for循环设置另外的限制。例如，循环中不能有中断语句，循环控制变量必须是整数，for循环的设定初值的表达式必须是一个整数，逻辑表达式必须是<、<、>或者>，增量表达式中必须只有整数增加量或减少量。读者可以参考OpenMP手册了解关于这些限制的详细情况。

# 3.在多个for命令间同步

通常，并行结构中需要有一系列的for命令，而且这个并行结构在每个for命令结束时也不执行隐式障碍。OpenMP提供一个子句nowait，它可以和for命令一起使用，用来表明线程可以进入下一个语句，无需等待其他所有的线程结束for循环执行。下面的例子说明这个子句的用法。

# 例7.15使用nowait子句

这个例子中，变量name需要在两个列表——current_list和past_list中查找。如果该变量名存在于一个列表中，则必须被相应地处理。变量名也可能在两个列表中。此时，没有必要等待所有的线程在进入第二个循环前完成第一个循环的执行。因此，可以使用nowait子句节省空闲及同步开销，程序代码如下：

1 #pragma omp parallel   
2 {   
3 #pragma omp for nowait   
4 for (i = 0; i < nmax; $\mathbf { i } + +$ ）   
5 if (isEqual(name,current_list[i]）   
6 processCurrentName (name) ;   
7 #pragma omp for   
8 for (i = 0;i < mmax; $\mathbf { i } + +$ ）   
9 if (isEqual(name, past_list [i])   
10 processPastName (name) ;   
11

# 4.sections命令

for命令适用于划分跨越多个线程的迭代空间。现在考虑有3个任务（taskA，taskB,taskC）需要执行。假设这3个任务彼此独立，可以分配给不同的线程。在OpenMP中，可用sections命令进行这种非循环的并行任务分配。sections命令的一般形式如下：

1 #pragma omp sections [clause list]   
2 {   
3 {#pragma omp section   
4 /\* structured block \*/   
5 1   
6 [#pragma omp section   
7 /\* structured block \*/   
8 1   
9   
10 }

sections命令将与每个段对应的结构化块分配给一个线程（事实上可将一个以上的段分配给一个线程)。clause list中可能会包括如下子句——private、firstprivate、lastprivate、reduction以及nowait，这些子句的语法和语义与for命令中的一样。本例中，子句lastprivate指定更新变量值的sections命令的最后段（词法上的）；在sections命令的最后，子句nowait指定所有线程没有隐式同步。

为了执行3个并发任务taskA，taskB，taskC，相应的sections命令如下:

1 #pragma omp parallel   
2 {   
3 #pragma omp sections   
4 {   
5 #pragma omp section   
6   
7 taskA();   
8 ）   
9 #pragma omp section   
10 {   
11 taskB() ;   
12   
13 #pragma omp section   
14   
15 taskc() ;   
16 ）   
17   
18

如果有3个线程，每个段（此时即为相应的任务）分配给一个线程。线程在分配段执行结束时同步（除非使用了nowait子句)。注意，分支进人或分支跳出section块都是不合法的。

# 5.合并命令

到目前为止，讨论了用命令parallel创建并发的线程，用for命令和sections命令将工作分配给线程。如果没有指定parallel命令，则for命令和sections命令将串行执行（所有的工作都分配给一个线程，即主线程）。因此，parallel命令通常在for命令和sections命令之前。OpenMP允许程序员把parallel命令分别合并成parallel for和parallel sections命令。合并后命令的子句列表可以是parallel命令的子句列表，也可以是for/sections命令的子句列表。例如:

1 #pragma omp parallel default (private) shared (n) { #pragma omp for   
4 for (i=0<i<n;i++){   
5 /\* body of parallel for loop \*/   
6   
7

# 与

#pragma omp parallel for default (private) shared (n) { for(i=o<i<n; $\dot { \bar { \lambda } } + \dot { \bar { \lambda } }$ ）{ 4 /\* body of parallel for loop \*/ 5 6 7

# 相同，同时

1 #pragma omp parallel  
2 {  
3 #pragma omp sections  
4 {  
5 #pragma omp section  
6 {  
7 taskA() ;  
8  
9 #pragma omp section  
10 {  
1 taskB() ;  
12  
13 /\* other sections here \*/  
14 1  
15 ）

等同于:

1 #pragma omp parallel sections   
2 {   
3 #pragma omp section   
4 {   
5 taskA() ;   
6   
7 #pragma omp section   
8 {   
9 taskB() ;   
10   
11 /\* other sections here \*/   
12

# 6.嵌套parallel命令

回到程序7-13。要在多个线程间分割每个for循环，必须对程序作如下修改：

1 #pragma omp parallel for default(private) shared (a，b，c， dim)\   
2 num_threads(2）   
3 $\pm \mathrm { o r } ( \mathrm { \bf ~ i } = 0 ; \mathrm { \bf ~ i } < \mathrm { \bf ~ d i m } ; \mathrm { \bf ~ i } + + ) \left\{ \begin{array} { r l } \end{array} \right.$   
4 #pragma omp parallel for default(private) shared (a，b,c，dim) \   
5 num_threads(2)   
6 $\begin{array}{c} \begin{array} { l } { { \pm \mathrm { o r } ( \mathrm { j } \pm \mathrm {  ~ { \vec { \alpha } ~ } } ^ { } \circ \mathrm {  ~ { \vec { \alpha } ~ } } ^ { } \mathrm { j } \mathrm {  ~ { \vec { \mathrm {  ~ { \vec { \alpha } ~ } } } ~ } } ^ { } \mathrm { j } + \mathrm {  ~ { \vec { \alpha } ~ } } ^ { } ) } } \end{array} \left\{ \begin{array} { l } { { \pm \mathrm { o r } ( \mathrm { j } \pm \mathrm {  ~ { \vec { \alpha } ~ } } ^ { } \mathrm { j } + \mathrm {  ~ { \vec { \alpha } ~ } } ^ { } ) } } \\ { { \mathrm { c } ( \mathrm { i } , \mathrm { j } ) } } \end{array} \right. = 0 ;  \end{array}$   
7   
8 #pragma omp parallel for default(private) \   
9 shared (a，b，c，dim) num_threads(2)   
10 for (k = 0;k < dim;k++){   
11 c(i,j) += a(i,k)\*b(k,j):   
12 ）   
13   
14

先来看看这段代码是如何编写的。它没有将3个for命令嵌套到一个parallel命令中，而是使用了3个parallel for命令。这是因为OpenMP不允许for、sections以及single命令绑定到同一个被嵌套的parallel命令。进而，遇到嵌套的parallel命令时，这段代码只会产生一队逻辑线程。新产生的这队逻辑线程仍然由与外部parallel命令对应的同一线程执行。为了产生一组新的线程，必须用OMP_NESTED环境变量来启用嵌套并行。如果OMP_NESTED环境变量被设置为FALSE，那么内部的paralle1区域将串行化，并由一个线程执行。如果OMP_NESTED环境变量被设置为TRUE，则嵌套并行被启用。环境变量的默认状态为FALSE，即嵌套并行被禁用。OpenMP环境变量在7.10.6节详细地讲述。

在嵌套并行中，还有许多与同步结构相关的限制。关于这些限制的详细情况，读者可以查阅OpenMP手册。

# 7.10.3OpenMP中的同步结构

在7.5节，我们讨论了需要对多个线程的执行进行协调。这可能是由所需要的执行顺序、指令集的原子性或者代码段的串行执行需要造成的。PthreadsAPI支持互斥锁和条件变量。使用它们可以通过读-写锁、障碍以及监控器等形式实现更高层次的功能。OpenMP标准以易于使用的API提供这种高层的功能。本节将考查这些命令以及它们的使用。

# 1.同步点:barrier命令

barrier是最常用的同步原始变量。OpenMP提供了barrier命令，它的语法如下：

#pragma omp barrier

遇到此命令时，队中所有的线程都要等待其他的线程跟上，然后释放。当与嵌套的parallel命令一起使用时，barrier命令绑定到最近的parallel命令。对于按条件执行障碍，一定要注意，barrier命令必须包含在条件执行的复合语句中。这是因为pragma是编译器命令，不是语言的一部分。障碍也能通过结束及重新开始parallel区域实现。但是，与此相关的开销通常都会更高。因此，这不是实现障碍的可选方法。

# 2.单线程执行：single和master命令

一个并行段内的计算通常只需由一个线程执行。计算一个数字列表的平均值便是这样一个简单例子。每个线程计算部分列表中的本地和，并把这些本地和加到一个共享的全局和中，然后，让一个线程以全局和除以列表中的项目数得到平均值。最后一步可以用single命令实现。

single命令指定一个由单一（任意的）线程执行的结构化块。命令的语法如下：

1 #pragma omp single [clause list]   
2 structured block

子句表(clause list)可以是子句private、firstprivate以及nowait。这些子句的语义和前面的一样。遇到single块时，第一个线程进人块。所有其他的线程进行到块的末尾。如果在块的尾部指定了nowait子句，则其他的线程继续；否则这些线程在single块的尾部等待，直至线程完成块的执行。这条命令在计算全局数据以及进行I/O操作时很有用。

master命令是single命令的特殊情况，它指定只能由主线程执行结构化块。master命令的语法如下：

1 #pragma omp master   
2 structured block

与single命令相反，不存在伴随master命令的隐式障碍。

# 3.临界段：critical和atomic命令

在讨论Pthreads时，曾经考查用锁来保护临界区域，即必须串行地一次执行一个线程的区域。除了显式锁管理（7.10.5节）外，OpenMP提供critical命令实现临界区域。critical命令的语法如下:

1 #pragma omp critical [(name)]   
2 structured block

这里，可选标识符name用来标识临界区域。使用name可以使不同的线程执行不同的代码，且相互保护。

# 例7.16在生产者-消费者线程使用critical命令

在生产者-消费者模式中，生产者线程产生一个任务，并将它插人到任务队列。消费者线程从队列中提取任务，并一次执行一个任务。由于存在对任务队列的并发访问，这些访问必须用临界块串行化。特别地，将任务插人到队列以及从队列中提取任务必须被串行化。这可用下述方法实现：

#pragma omp parallel sections   
{   
3 #pragma parallel section   
4 {   
5 /\* producer thread \*/   
6 task $\mathbf { \delta m }$ produce_task();   
7 #pragma omp critical ( task_queue)   
8 {   
9 insert_into_queue(task) :   
10 一   
11   
12 #pragma parallel section   
13 {   
14 /\* consumer thread \*/   
15 #pragma omp critical ( task_queue)   
16 {   
17 task = extract_from_queue(task):   
18   
19 consume_task(task) :   
20 ！   
21 }

值得注意的是，队列满和队列空的条件必须在函数insert_into_queue和 extract_from_queue中显式处理。 □

critica1命令保证在程序执行的任意一点处，只有一个线程在由一个名称指定的临界段内部。如果某一线程已经在临界段内部（已命名），所有其他的线程必须等待该线程完毕才能进人命名的临界段。名称字段为可选项。如果没有指定名称，则临界段映射到一个默认名称，这个名称与所有未命名的临界段的名称相同。在整个程序中，临界段的名称都是全局的。

容易看出，命令critical是Pthreads中相应的mutex函数的直接应用。名称字段映射到进行锁操作的互斥锁名称。和Pthreads中一样，一定要记住，critical段表示程序中串行化的点，因此，一定要尽可能减小临界段的大小（在执行时间方面)，以求获得好的性能。

使用critical命令时一定要注意几个明显的安全措施。指令的block必须表示结构化块，即不允许跳入块或从块中跳出。容易看出，跳入块将导致非临界访问，而跳出块将导致未释放的锁，引起线程无限等待。

通常，临界段只由对某单个内存单元的一个更新组成，例如，整数相加或者增加一个增量。OpenMP提供另-个命令atomic，用来实现对内存单元的原子更新。atomic命令指定，对随后指令中内存单元的更新一定应作为原子操作进行。更新指令可以是下面几种形式之一：

1 x binary_operation $\approx$ expr、2 $\mathbf { x } + \mathbf { \nabla } \cdot$ 3 $+ + \ast$ 4 x--5 --x

这里， $\mathbf { e x p r }$ 是一个标量表达式，它不包括对 $\pmb { \mathrm { x } }$ 的引用， $\mathbf { x }$ 本身是标量类型的左值，binary_operation是{+，\*，-，/，&，|l，《,》}之一。应该记住，命令atomic只对载入及存储标量变量原子化。表达式的计值不是原子的。要非常小心地避免竞赛条件隐含其中，这也可以解释为什么atomic命令中的 $\mathbf { e x p r }$ 项不能包含更新的变量自身。所有的atomic命令都可以被critical命令代替，只要它们的名称相同。但是，与转换成critical命令相比，原子化硬件指令的实用性可以优化程序的性能。

# 4.按顺序执行：ordered命令

在许多情况下，需要像执行串行版本程序的颂序一样执行并行循环的代码段。例如，考虑一个for循环，于循环中的某点，计算一个存储在数组list中的列表与数组cumul_sum元素的累积和。数组 $\textsf { c u m u l \_ s u m }$ 的计算可在 $\yen 0$ 循环中用下标i串行地执行cumul_sum[i] cumul_sum[i-1]+list[i]得到。当在多个线程间执行这个for循环时，应该注意必须等到cumul_sum[i-1]的值计算后，才能计算cumul_sum[i]的值。所以，语句一定要在一个ordered块中执行。

ordered命令的语法如下：

1 #pragma omp ordered   
2 structured block

由于ordered命令代表for循环的按序执行，它必须位于for或parallel for命令的作用域内。进而，for或parallel for命令中必须含有ordered子句，用来表示在循环中包含ordered块。

# 例7.17用ordered命令计算列表的累积和

前面已经讲过，要计算列表中i个数的累积和，可以把当前数加到列表中i-1个数的累积和上。然而，这个循环必须按顺序执行。而且，第一个元素的累积和就是这个元素本身。因此，可用ordered命令编写代码如下:

1 cumul_sum[0] $\eqcirc$ list[0];   
2 #pragma omp parallel for private (i)\ shared (cumul_sum，list，n) ordered for (i = 1;i < n; $\pm + 1$   
5 {   
6 /\* other processing on list[i] if needed \*/   
7   
8 #pragma omp ordered   
9 {   
10 cumul_sum[i] $\eqcirc$ cumul_sum[i-1] $^ { + }$ list[i];   
1 ！   
12 +

需要特别注意的是，ordered命令代表程序中一个有序的串行化点。当所有先前的线程（由循环索引确定）退出后，只有一个线程能进入一个有序块。因此，如果循环的大部分包含在ordered命令中，则相应的加速比就不能达到。在上例中，除非在ordered命令之外有一个重要的处理与list[i]有关，并行形式不会比串行形式快。限制一个for命令中只能有一个ordered块。

# 5.内存一致性：flush命令

flush命令提供在线程间实现内存一致的机制。在共享地址空间计算机中，此命令看起来有点多余，但要注意，变量经常被分配给寄存器，而寄存器分配的变量可能会不一致。这时，通过强制变量写入内存系统或将变量从内存系统读出，flush命令提供一个内存栅栏。所有对共享变量的写操作必须在一个flush中提交到内存，所有在栅栏后对共享变量的引用必须从内存实现。由于私有变量只和一个线程相关，flush命令只应用于共享变量。

flush命令的语法如下：

1#pragma omp flush[(list)]

可选项1ist指定需要被刷新的变量，默认情况下，所有的共享变量都被刷新。

几个OpenMP命令中有隐式flush，特别是flush隐含在barrier中，在critical、ordered、parallel for以及parallel sections块的入口和出口处，在for、sections以及single块的出口处。如果有nowait子句，则不会隐含flush。在for、sections以及single块的入口处，以及master块的入口或出口处，也没有隐含flush。

# 7.10.4OpenMP中的数据处理

线程对数据的处理是影响程序性能的重要因素之一。前面已经简单地讲述了OpenMP支持的多种数据类，如private、shared、firstprivate以及lastprivate。现在再对它们进行更详细地讨论，了解如何使用这些数据类。下面我们给出一些实用的建议：

·如果一个线程初始化并使用了一个变量（如循环索引)，且没有其他的线程存取数据，那么应为线程制作一个变量的本地副本，数据也应该指定为private。·如果一个线程重复地读取一个变量，且此变量在程序的早期已被初始化，那么，对变量作一个副本并继承线程创建时变量的值是有利的。这样，当线程在处理器中调度时，数据可以驻留在同一处理器中（可能在它的高速缓存中），对数据的存取不会造成处理器间的通信。这样的数据应该指定为firstprivate。·如果多个线程处理一块数据，则必须寻求方法将这些处理分成多个本地操作，再加上一个全局操作。例如，如果多个线程记录着某个事件的计数，则最好保留本地计数，并在并行块的最后用求和操作让计数增加。子句reduction支持这样的操作。·如果多个线程处理一个大数据结构的不同部分，则程序员应寻求方法将大数据结构分成小数据结构，并使这些小数据结构对于处理它们的线程是私有的。·所有上面的方法都试过后，用子句shared可使剩余的数据项被多个线程共享。

除了private、shared、firstprivate以及lastprivate外，OpenMP还支持另一个数据类，称为threadprivate。

threadprivate和copyin命令在保持线程数目不变条件下，一组对象通过并行或串行块时以持久的方式使其对一个线程本地可用，通常这样做是有用的。与private变量相反，这些变量对于通过并行区域保持不变的对象是有用的，否则这些对象就必须复制到主线程的数据空间中，并在下一个并行块重新初始化。该类变量在OpenMP中用threadprivate命令支持。命令的语法如下:

# l#pragma omp threadprivate(variable_list)

这条命令隐含在variable_list中的所有变量对每个线程而言都是本地的，且在一个并行区域内被访问前初始化一次。此外，如果线程数目的动态调整被禁止和线程数目不变，则这些变量在不同的并行区域中能够保持不变。

与firstprivate相似，OpenMP提供一种机制，用于将同样的值分配给一个并行区域中所有线程的threadprivate变量。这就是copyin子句，它能和parallel命令一起使用，语法为copyin(variable_list）。

# 7.10.5OpenMP库函数

除了命令以外，OpenMP还提供许多函数，使程序员能够控制线程程序的执行。可以看出，这些函数和相应的Pthreads函数类似；但是，通常这些函数处在更高的抽象层次，更易于使用。

# 1.控制线程和处理器数目

下面的OpenMP函数与线程程序中用到的并发性和处理器数目有关：

1 #include <omp.h>   
2   
3 void omp_set_num_threads (int num_threads) :   
4 int omp_get_num_threads ();   
5 int omp_get_max_threads () ;   
6 int omp_get_thread_num ();   
7 int omp_get_num_procs ();   
8 int omp_in_parallel();

函数omp_set_num_threads设置默认的线程数目，如果parallel命令中没有使用num_threads子句，那么这些线程在遇到下一个parallel命令时创建。这个函数必须在并行区域的范围外调用，且必须启用对线程的动态调整（使用7.10.6节中讲述的OMP_DYNAMIC环境变量或者omp_set_dynamic库函数）。

函数omp_get_num_threads返回参与到队中的线程数目。它绑定到最靠近它的并行命令上，在没有并行命令时，返回1（指主线程)。函数omp_get_max_threads返回可能由遇到的parallel命令创建的最大线程数目，它没有num_threads子句。函数omp_get_thread_num对一个队中的每个线程返回一个唯一的线程id。此id取从0（指主线程）到omp_get_num_threads()-1的整数值。函数omp_get_num_procs返回在那一点可用来执行线程程序的处理器数目。最后，函数omp_in_parallel对于从并行区域内的调用返回一个非0值，从并行区域外的调用返回0。

# 2.控制和监控线程的创建

下面的OpenMP函数使程序员能够设置和监控线程的创建：

1 #include <omp.h>   
2   
3 void omp_set_dynamic (int dynamic_threads):   
4 int omp_get_dynamic (）:   
5 void omp_set_nested (int nested);   
6 int omp_get_nested ();

函数omp_set_dynamic允许程序员动态地改变在遇到并行区域时创建的线程数目。如果dynamic_threads的计值为0，则停止动态调整，否则启用动态调整。函数必须在并行区域外调用。相应的状态，即动态调整被启用或停止，可用函数omp_get_dynamic查询，它在动态调整启用时返回一个非0值，没有启用时返回0。

函数omp_set_nested在其参数nested为非0值时允许嵌套并行，在参数nested为0时停止嵌套并行。当嵌套并行停止时，所有随后遇到的嵌套并行区域都被串行化。嵌套并行的状态可用函数omp_get_nested查询，它在嵌套并行被启用时返回-个非0值，停止使用时返回0。

# 3.互斥

OpenMP提供对临界段和原子更新的支持，但有时使用一个显式锁更方便。对于这种程序，OpenMP提供初始化锁、锁定、解锁以及放弃锁的函数。在OpenMP中，锁数据结构的类型为omp_lock_t。OpenMP定义以下函数:

1 #include comp.h>   
2   
3 void omp_init_lock (omp_lock_t \*lock) ;   
4 void omp_destroy_lock (omp_lock_t \*lock);   
5 void omp_set_lock (omp_lock_t \*lock);   
6 void omp_unset_lock (omp_lock_t \*lock) ;   
7 int omp_test_lock (omp_lock_t \*lock);

一定要先初始化锁，然后才能使用锁。锁的初始化使用函数omp_init_lock。当锁不再需要时，必须用函数omp_destroy_lock放弃。对已被初始化的锁进行初始化，或放弃未初始化的锁，都是不合法的。-旦锁被初始化，它就可以用函数omp_set_lock锁定和函数omp_unset_1ock解锁。锁定一个先前被解锁的锁时，线程获得对锁的独占访问。所有其他的线程试图用omp_set_1ock锁定时都必须等待这个锁。只有拥有锁的线程可以对其解锁。如果线程试图对由其他线程拥有的锁进行解锁，则将得到不确定的结果。锁定和解锁操作先于初始化锁或在放弃锁后都不合法。函数omp_test_lock用来测试锁是否已被设置，如果函数返回一个非0值，则锁已被成功设置，否则锁当前被另一个线程拥有。

与Pthreads中的递归互斥锁一样，OpenMP也支持可嵌套锁，同一线程对可嵌套锁可以锁定多次。这种情况下，锁对象是omp_nest_lock_t，处理嵌套锁的相应函数为：

#include <omp.h> void omp_init_nest_lock (omp_nest_lock_t \*lock): void omp_destroy_nest_lock (omp_nest_lock_t \*lock) ; 5 void omp_set_nest_lock (omp_nest_lock_t \*lock) : 6 void omp_unset_nest_lock (omp_nest_lock_t \*lock); 7 int omp_test_nest_lock (omp_nest_lock_t \*lock):

这些函数的语义与对应的简单锁函数类似。注意，所有这些函数都在Pthreads中有直接对应的互斥锁调用。

# 7.10.6 OpenMP中的环境变

OpenMP提供额外的环境变量帮助控制并行程序的执行。OpenMP有如下的环境变量。

OMP_NUM_THREADS这个环境变量指定进入paral1e1区域时创建线程的默认数目。线程的数目既可用函数omp_set_num_threads改变，也可以用parallel命令的num_threads子句改变。注意只有当变量OMP_SET_DYNAMIC设置为TRUE或用非0参数调用函数omp_set_dynamic时，才能动态地改变线程数目。例如，如果程序执行前在csh中输入以下命令，那么默认的线程数目设置为8，

1setenV OMP_NUM_THREADS 8

OMP_DYNAMIC 当此变量设置为TRUE时，允许线程的数目在运行时用函数omP_set_num_threads或num_threads子句进行控制。如果用参数0调用函数omp_set_dynamic,则对线程数目的动态控制被停止。

OMP_NESTED当这个变量设置为TRUE时，启用嵌套并行，除非用参数0调用函数omp_set_nested停用嵌套并行。

OMP_SCHEDULE这个变量控制与使用runtime调度类的for命令有关的迭代空间的指定。变量的取值可以是static、dynamic以及guided，再加上可选的块大小。例如，

1 Betenv OMP_SCHEDULE "static,4"

指定在默认情况下，所有的for命令使用static调度，块大小为4。指定的其他例子包括：

1 Setenv OMP_SCHEDULE "dynamic"   
2 Betenv OMP_SCHEDULE "guided"

在这两个例子中，使用的默认块大小都是1。

# 7.10.7显式线程与基于OpenMP编程的比较

OpenMP在所有本地线程的顶部提供一个层，使得更容易执行许多与线程有关的任务。使用由OpenMP提供的命令，程序员无需再承担初始化属性对象、设置线程参数、划分迭代空间等工作。当要解决的问题具有静态的和/或正则的任务图时，这种便利尤其有用。在许多应用程序中，与从命令自动产生线程代码有关的开销是最小的。，

然而，使用命令也有缺点。用显式线程编写的程序将使数据交换更透明，这有助于减少一些与数据移动、假共享以及争用相关的开销。显式线程还提供更丰富的API，这些API的形式为条件等待、不同类型的锁以及对构建复合同步操作时的更大灵活性（如7.8节所述）。最后，由于显式线程比OpenMP使用更广泛，更容易找到Pthreads程序的工具和对它的支持。

程序员在决定使用何种API编程前，一定要权衡所有这些利弊。

# 7.11 书目评注

无论是显式的基于线程的编程，还是基于OpenMP的编程，都有许多优秀的参考文献。Lewis和Berg[LB97，LB95a]提供详细的Pthreads编程指南。Kleiman，Shah和Smaalders[KSS95]对线程系统及用线程编程提供出色的描述。其他几本书籍也讲述了与多线程编程有关的编程及系统软件问题[NBF96,But97,Gal95,Lew91,RRRR96,ND96]。

人们也开发了许多其他的线程API及系统，它们经常被用于各种应用程序中。这些系统包括：Java线程[Dra96,MK99,Hyd99,Lea99]、微软的线程API[PG98,CWP98,Wil00,BW97]以及Solaris线程API[KSS95,Sun95]。无论从硬件还是从软件来看，对线程系统的研究都有着很长的和富有成果的历史，可以追溯到HEP Denelcor[HLM84]时期。最近，又开发了一些软件系统，如Cilk[ $\mathbf { B } \mathbf { J } \mathbf { K } ^ { + } \mathbf { 9 } \mathsf { S }$ ,LRZ95]，OxfordBSP[HDM97]，Active Threads[Wei97] 以及EarthManna[ $\mathbf { H } \mathbf { M } \mathbf { T } ^ { + } \mathbf { 9 } 6 ]$ 1。多个系统提供对多线程的硬件支持，其中包括MITAlewifel $\mathbf { A D J ^ { + } 9 } 1 ]$ ，Horizon[KS88]，同时多线程[TEL95,Tul96]，多标量体系结构[Fra93]以及超线程体系结构[TY96]。

人们也研究了关于线程性能方面的问题。早期关于多线程处理器性能权衡方面的工作在[Aga89,SBCV90,Aga91,CGL92,LB95b]中已有介绍。人们也广泛地研究了共享内存的一致性模型。其他活跃的研究领域包括运行系统、编译器支持、基于对象的扩展、性能评估以及软件开发工具。人们还致力于在工作站网络上共享内存支持软件的研究。所有这些仅仅涉及有关用线程编程的问题。

由于出现时间不长，有关OpenMP编程的书籍相对较少[CDK+00]。在http：//www.openmp.org可以找到OpenMP标准及扩展的资料集。许多其他的文章（以及特刊）讨论了有关OpenMP性能、编译以及互用性方面的问题[Bra97,CM98,DM98,LHZ98,Thr99]。

# 习题

7.1估计下面执行Pthreads中的每一种操作花费的时间：

·线程创建   
·线程连接   
·成功锁定   
·成功解锁   
·成功trylock（试探锁）   
·不成功trylock（试探锁）   
·条件等待   
·条件标记   
·条件广播

针对每个操作，仔细记录计算每种函数调用时间所使用的方法，同时记录所用的计算机。

7.2使用多个线程插入到队列及从队列中提取多个线程，实现一个多存取线程队列。使用互斥锁同步对队列的存取。记录下1000次插入和1000次提取的时间，每次有64个插入线程（生产者）和64个提取线程（消费者）。

7.3使用条件变量（除了互斥锁以外）重做习题7.2。记录下进行与上题同样试验花费的时间，并对时间的差别加以评论。

7.4一个简单的流媒体播放器由以下部分组成：一个监视网络端口到达数据的线程，一个对数据包解压缩并产生图像序列中的帧的解压缩器线程，以及一个在规划的间隔显示帧的绘制线程。这3个线程必须通过共享缓冲实现通信一—界于网络和解压缩器之间的输入缓冲，以及界于解压缩器与绘制器之间的输出缓冲。实现这个简单的线程框架。网络线程调用虚拟函数listen_to_port从网络收集数据。就此程序而言，这个函数产生所需长度的随机字节串。解压缩线程调用函数decompress，该函数从输入缓冲取得数据，并返回预先确定大小的帧。对于这个习题，产生一个具有随机字节数的帧。最后，绘制器线程从输出缓冲取出帧，并调用显示函数。显示函数将一帧作为参数，对于这个习题，它没有操作。用条件变量实现这个线程框架。注意，很容易改变这3个虚拟函数，得到一个有意义的流媒体解压缩器。

7.5请使用二叉树搜索算法展示递归锁的用法。程序要求一个很大的数字列表。列表在多个线程间划分。每个线程试图用与树对应的单个锁将它的元素插人到树中。说明即使在线程数目不多的情况下，单个锁也会成为瓶颈。

7.6通过将锁与树中的每个节点对应（与单个锁和整个树对应相反)，改进二叉树搜索程序。线程在读或写节点时锁定该节点。考查这种实现的性能特点。

7.7用读-写锁进一步改善二叉树搜索程序。线程在读一个节点前对节点加上读出锁。线程只在需要写入树节点时才对节点加上写入锁。请实现该程序，并记录下使用读-写锁比常规锁带来性能改进时程序参数的范围。

7.8请实现用链解决冲突的线程散列表。散列表中，单个锁与含k个散列表项的块对应。线程如果试图读/写块中的元素，必须先锁定对应的块。考查你的实现中作为k的函数的性能。

7.9将散列表中的锁改为读-写锁，只在插人数据项到链表时才使用写入锁。考查此程序作为k的函数的性能。比较此实现与使用常规锁实现时的性能。

7.10编写一个线程程序计算Eratosthenes筛子。在实现前仔细考虑线程策略。弄清一些问题是重要的，例如，不能从筛子中去除6的倍数，除非已去除了3的倍数（此时可以看出，无需先去除6的倍数)。用流水作业（装配线）策略，即用当前最小元素构成装配线的下一站是解决问题的一种方法。

7.11请编写一个线程程序解决15迷宫问题。程序取某个初始位置，并有一张开放表记录未走过的位置。表按迷宫板度量的“优良度”排序。曼哈坦距离（即每个板格所需移动的x方向的位移和y方向的位移之和）是较好的度量方法之一。开放表是用堆来实现的工作队列。每个线程从工作队列中提取工作（迷宫板），将它扩张到所有可能的后继者，如果后继者还没有用过，则将它插入到工作队列中。使用散列表（习题7.9）记录以前未用过的项。请绘出程序线程数目对增加运行速度的关系曲线。你可以计算出对某个参考迷宫板程序的加速对于不同的线程数目是相同的。

7.12修改上面的程序，使之有多个（如k个）开放表。此时，每个线程取出一个随机的开放表，并试图从随机表中取出一个“迷宫板”，把表扩充后再插回到另一个随机选择的表中。请绘出现在程序对于线程数目的加速比曲线。将性能与上一题作比较。请小心使用锁及trylock（试探锁)，使串行化开销达到最小限度。

7.13实现并测试例7.14中矩阵相乘的OpenMP程序。使用OMP_NUM_THREADS环境变量控制线程的数目，并绘出不同线程数目的性能曲线。考虑如下三种情况：i)只有最外层的循环并行化；ii)最外层的两个循环并行化；ii)所有三个循环都并行化。这三种情况的结果是什么？

7.14考虑一个调用函数dummy的简单循环，函数包含一个可控制的延迟。所有对该函数的调用彼此独立。在4个使用static，dynamic和guided调度的线程间划分这个循环。对static调度和guided调度使用不同的参数。记录下当dummy函数的延迟变大时实验的结果。

7.15考虑以行压缩格式存储的一个稀疏矩阵（在网页或任何有关稀疏线性代数的书籍中可以找到这种格式的描述）。编写一个OpenMP程序计算这种矩阵与向量相乘的乘积。从

$$
\begin{array} { r } { \vdots \vdots \vdots \vdots \vdots \vdots \vdots \vdots \vdots \vdots \vdots \vdots \vdots \ddots } \end{array}
$$

Matrix Market (http://math.nist.gov/MatrixMarket/）下载样本矩阵，并测试程序的性能，以矩阵大小和线程数目作为性能的函数。

7.16用sections创建单-的producer任务及单一的consumer任务，在OpenMP中建立一个生产者-消费者程序框架。用锁来保证适当的同步。针对不同数目的生产者和消费者测试程序。

$$
 \begin{array} { c c c c c c c c c c c c c c c c c c c c c c } { { , } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } }  \end{array}
$$

# 第8章 稠密矩阵算法

在数值与非数值计算中经常使用矩阵与向量算法。本章讨论关于稠密矩阵（dense matrix）或者满矩阵（fulmatrix）的一些关键算法，这种矩阵没有或很少见可用的零元素。为了方便教学，我们专门论述方阵，但是在应用中，本章的算法同样适用于矩形矩阵。

由于矩阵和向量的规则结构，涉及矩阵与向量的并行计算容易用于数据分解（见3.3.2节）。取决于要进行的计算，可通过划分输入、输出或者中间数据导出分解。3.4.1节详细描述并行计算中各种划分矩阵的方案。本章讨论的算法使用一维和二维块、循环以及块循环等划分。

本章所述多数算法的另外一个特性是它们的每个进程只有一个任务。由于任务到进程的映射是一对一关系，我们通常并不明确地讨论任务，而是把问题直接分解或者划分成进程。

# 8.1 矩阵向口乘法

这一节，我们讨论的问题是，一个 $n \times n$ 稠密矩阵A乘一个 $\pmb { n } \times 1$ 向量 $x$ 产生一个 $n \times 1$ 结果向量y。算法8-1显示这个问题的一个串行算法，该算法需要 $n ^ { 2 }$ 次乘法和加法运算。

1. procedure MAT-VECT $( A , x , y )$   
2. begin   
3. for $i : = 0$ to n.- 1 do   
4. begin   
5. $y [ i ] : = 0 ;$   
6. for j := 0 to n -1 do   
7. $y [ i ] : = y [ i ] + A [ i , j ] \times x [ j ] ;$   
8. endfor;   
9. end MAT_VECT

假设一次乘法和加法运算需要一个单位时间，则串行运行时间为

$$
W = n ^ { 2 }
$$

根据使用的是一维行划分、一维列划分或者是二维划分，至少可能有三个不同的矩阵向量乘法的并行公式。

# 8.1.1一维行划分

本节讨论使用一维行块划分的矩阵-向量乘法的并行算法。使用一维列块划分的矩阵-向量乘法的并行算法类似（见习题8.2)，而且关于并行运行时间有相似的表达式。图8-1表示一维块划分方式下矩阵向量乘法运算中数据的分布与移动。

# 1.每个进程一行

首先考虑 $n \times n$ 矩阵A在 $\pmb { n }$ 个进程之间划分的情形，这时每个进程存储矩阵A的一整行以及

$$
 \begin{array} { r l } { \mathrm { ~ : ~ } } & { { } \quad , \cdots \qquad \cdots \qquad \cdots \qquad \cdots \qquad \vdots ^ { n } \cdots \qquad \vdots ^ { n } \cdots \qquad \vdots ^ { n } \cdots \qquad \vdots ^ { n } \cdots \qquad \vdots ^ { n } \cdots \qquad \vdots ^ { n } \cdots \qquad \vdots ^ { n } \cdots \qquad \vdots ^ { n } \cdots \qquad \vdots ^ { n } \cdots \qquad \vdots ^ { n } \cdots \qquad \vdots ^ { n } \cdots \qquad \vdots ^ { n } \cdots \qquad \vdots ^ { n } \cdots \qquad \vdots ^ { n } \cdots \qquad \vdots ^ { n } \cdots \qquad \vdots ^ { n } \cdots \qquad \vdots ^ { n } \cdots \qquad \vdots ^ { n } \cdots \qquad \vdots ^ { n } \cdots \qquad \vdots ^ { n } \cdots \qquad \vdots ^ { n } \cdots \qquad \vdots ^ { n } \cdots \qquad \vdots ^ { n } \cdots \qquad \vdots ^ { n } \cdots \qquad \vdots ^ { n } \cdots \qquad \vdots ^ { n } \cdots \qquad \vdots ^ { n } \cdots \qquad \vdots ^ { n } \cdots \qquad \vdots ^ { n } \cdots \qquad \vdots ^ { n } \cdots \qquad \vdots ^ { n } \cdots \qquad \vdots ^ { n } \cdots \qquad \vdots ^ { n } \cdots \qquad \vdots ^ { n } \cdots \qquad \vdots ^ { n } \cdots \qquad \vdots ^ { n } \cdots \qquad \vdots ^ { n } \cdots \qquad \vdots ^ { n } \cdots \qquad \vdots ^ { n } \cdots \qquad \vdots ^ { n } \cdots \qquad \vdots ^ { n } \cdots \qquad \vdots ^ { n } \cdots \qquad \vdots \qquad \vdots ^ { n } \cdots \qquad \vdots \qquad \vdots ^ { n } \cdots \qquad \vdots \qquad \vdots ^ { n } \cdots \qquad \qquad \vdots } \end{array}
$$

$n \times 1$ 向量 $x$ 的一个元素。关于一维行块划分矩阵与向量的初始分布如图8-1a所示。进程 $P _ { i }$ 最初拥有 $\dot { \boldsymbol { x } } [ i ]$ $| \mathcal { \vec { F } } [ [ A [ i , 0 ] , \ A [ i , 1 ] , \ \cdots , \ A [ i , n - 1 ]$ 并且负责计算 $y [ i ]$ 。矩阵 $\pmb { A }$ 的每一行与向量 $x$ 相乘（算法8-1），因此每个进程需要整个向量 $x$ 。但是因为每个进程开始时，只拥有向量 $x$ 的一个元素，所以需要用多对多广播的方法将所有的元素分布到所有的进程中。图8-1b说明了这个通信步骤。完成向量 $x$ 在进程中的分布后（图8-1c），进程 $P _ { i }$ 计算 $y [ i ] = \sum _ { j = 0 } ^ { n - 1 } ( A [ i , j ] \times x [ j ] )$ （算法8-1的第6和第7行)。如图8-1d所示，结果向量y的存储方法与初始向量 $\pmb { x }$ 完全相同。

![](images/ec3c80d8fe4440a5f075a2929e18ffbb45c5e49f3a0d04b8e53f6365a1bdcde1.jpg)  
图8-1使用一维行块划分的n×n矩阵与n×1向量的乘法对于每个进程一行的情况， $p = n$

并行运行时间每个进程从一个向量元素开始，在任意体系结构（表4-1）中，在n个进程中向量元素的多对多广播所需时间为(n)。每个进程中，向量x与矩阵A一行的乘法所需要的时间也为(n)。因此，完成全部n个进程需要的时间为0(n)，从而得到进程时间的乘积(n2)。由于串行算法的复杂度是(n2)，并行算法是成本最优的。

# 2.进程数少于n

考虑p个进程(p<n)的情况，使用块一维划分方法在进程之间划分矩阵。每个进程最初存储矩阵A的 $n / p$ 个整行和向量 $x$ 的 $n / p$ 个元素。由于矩阵A的每一行要与向量 $x$ 相乘，每个进程需要完整的向量 $x$ （即各个进程包含向量 $x$ 的所有部分）。这又要求使用如图8-1b和8-1c所示的多对多广播。多对多广播在 $p$ $( p < n )$ 个进程之间进行，传输的信息量为 $n / p$ 。完成通信之后，每个进程中矩阵A的 $n / p$ 个整行要与 $n \times 1$ 向量 $x$ 相乘，得到结果向量y的 $n / p$ 个元素。如图8-1d所示，结果向量y的分布方式与初始向量 $x$ 相同。

并行运行时间根据表4-1，在 $p ( p < n )$ 个进程之间进行的多对多广播，传输的信息量为$n / p$ ，通信时间为 $t _ { s } \log p + t _ { w } ( n / p ) ( p - 1 )$ 。当 $p$ 很大时，通信时间可用 $t _ { s } \log p + t _ { w } n _ { \cdot }$ 近似。完成通信之后，每个进程执行矩阵A的 $n / p$ 个行与向量 $x$ 的乘法所需要的时间为 $n ^ { 2 } / p$ 。因此，该过程的并行运行时间为

$$
T _ { P } = { \frac { n ^ { 2 } } { p } } + t _ { s } \log p + t _ { w } n
$$

这个并行公式的进程时间乘积为 $p T _ { p } = n ^ { 2 } + p t , \log p + p t _ { w } n _ { \circ } p = O ( n )$ 时，该算法是成本最优的。

可扩展性分析按照5.4.2节的分析步骤，通过逐个研究开销函数的各项，现在我们来推导矩阵向量乘法的等效率函数。考虑由公式(8-2)给出的关于超立方结构的并行运行时间。关系 $T _ { \circ } = p T _ { p } - w$ 给出超立方体上使用一维块划分时的矩阵-向量乘法开销函数的下述表达式：

$$
T _ { o } = t _ { s } p \log p + t _ { w } n p .
$$

回忆第5章，决定并行算法等效率函数的主要关系是 $W = K T _ { o }$ （公式(5-14)），其中 $K =$ E/(1-E)，E是期望效率。重写矩阵-向量乘法算法中的这个关系，首先只用T。的ts项，得到

$$
W = K t _ { s } p \log p
$$

公式(8-4)给出关于消息启动时间的等效率函数项。同理，对于开销函数中的tw项，可得

$$
W \ = \ K t _ { w } n p
$$

由于 $W = n ^ { 2 }$ （公式(8-1)），我们使用 $\pmb { K }$ 、 $p$ 和 $\pmb { t _ { w } }$ 导出W的表达式（即由 $\scriptstyle t _ { w }$ 导出的等效率函数）如下:

$$
\begin{array} { r c l } { { n ^ { 2 } } } & { { = } } & { { K t _ { w } n p } } \\ { { n } } & { { = } } & { { K t _ { w } { p } } } \\ { { n ^ { 2 } } } & { { = } } & { { K ^ { 2 } t _ { w } ^ { 2 } p ^ { 2 } } } \\ { { W } } & { { = } } & { { K ^ { 2 } t _ { w } ^ { 2 } p ^ { 2 } } } \end{array}
$$

现在考虑这个并行算法的并发度。使用一维划分时，最多可以使用n个进程实现n×n矩阵A和n×1向量x的乘法。换句话说，p=O(n)，它能得到下面的条件

$$
\begin{array} { r c l } { { n } } & { { = } } & { { \Omega ( p ) } } \\ { { n ^ { 2 } } } & { { = } } & { { \Omega ( p ^ { 2 } ) } } \\ { { W } } & { { = } } & { { \Omega ( p ^ { 2 } ) } } \end{array}
$$

通过比较公式(8-4)、(8-5)和(8-6)，可以确定总的渐近等效率函数。在三个公式中，(8-5)

和(8-6)给出最高的渐近速度，按照这个速度，问题的规模必需随着进程数的增加而增加，才能保持固定的效率。这个速度 $\Theta ( p ^ { 2 } )$ 就是使用一维划分时并行矩阵-向量乘法算法的渐近等效率函数。

# 8.1.2二维划分

本节讨论使用二维块划分在各个进程间分布矩阵时矩阵-向量乘法的并行算法。图8-2给出矩阵在各个进程中的分布，以及向量在各个进程中的分布与移动。

![](images/97c0d97c818b0ab86b241b264c5cd6c8199a940071b41a9fe5561549db9ed7f6.jpg)  
图8-2使用二维块划分的矩阵-向量乘法。对于每个进程一个元素的情形，对于 $\pmb { n } \pmb { n }$ 矩阵有 $p = n ^ { 2 }$

# 1.每个进程一个元

我们先考虑简单的情况，把n×n矩阵A在n2个进程中划分，这样每个进程只拥有矩阵A的一个元素。把n×1向量x分布在n个进程的最后一列，每个进程拥有向量x的一个元素。由于在计算中，向量x的每个元素要与矩阵A的每行的相应元素相乘，因此向量x的第i个元素必须分布在能与矩阵A每一行的第i个元素进行运算的进程中。图8-2a和b给出这样分布的通信步骤。请注意图8-2与图8-1的相似之处。在进行乘法运算前，矩阵A的元素与向量x的元素必须位于同样的相对位置，如图8-1c所示。但是，向量的通信步骤因不同的划分策略而异。使用一维划分时，向量的元素只需要通过水平的划分边界（图8-1)。而使用二维划分时，向量的元素需要通过水平与垂直的两个划分边界（图8-2)。

如图8-2a所示，使用二维划分时，第一个通信步骤是将向量x沿着矩阵A的主对角线排列。通常向量 $x$ 沿着矩阵A的主对角线而不是最后一列存储，此时上述步骤是不需要的。第二步是把向量元素从每个对角进程复制到相应列的所有进程上。如图8-2b所示，这个步骤包括 $\pmb { n }$ 个同时进行的一对多广播操作，每一列的进程包括一个操作。这两个通信步骤后，每个进程再将其矩阵元素与x的相应元素相乘。为了得到结果向量y，必须将每一行的乘积结果相加，并把结果放到最后一列的进程中。图8-2c显示这一步骤，该步骤以行的最后一个进程为目标，每一行都需要进行一次多对一归约操作（见4.1节)。在完成归约步骤后，并行矩阵-向量的乘法即告结束。

并行运行时间在这个算法中使用三个基本通信操作：将向量 $x$ 的元素沿矩阵A的主对角线分布的一对一通信；在每一列的 $\pmb { n }$ 个进程中对每个向量元素的一对多广播；在每---行中进行的多对一归约。每个操作需要的时间是 $\Theta ( \log \ n )$ 。由于在固定时间内每个进程执行一次乘法，这个算法的总体并行运行时间为(n)。计算成本（进程时间乘积）为(n²logn)；因此算法不是成本最优的。

# 2.进程数少于n2

使用二维块划分矩阵时，通过使用少于 $n ^ { 2 }$ 个进程增加每个进程的计算粒度，可能得到矩阵向量乘法的成本最优的并行算法。

考虑有 $p$ 个进程的逻辑二维格网，每个进程拥有矩阵的一个 $( n / { \sqrt { p } } ) \times ( n / { \sqrt { p } } )$ 块。向量只分布在最后一个进程列的 $\cdot n / \sqrt { p }$ 个进程中。图8-2显示这种情况下的初始数据映射和通信步骤。在进行乘法运算前，必须将所有的向量分布在每一行进程中。首先向量应该沿着主对角线排列。为此，最右列的每个进程必须把它的 $n / { \sqrt { p } }$ 个向量元素传输到它所在行的对角线进程中。然后，进行这n/√p个向量元素按列的一对多广播操作。接着，每个进程执行n2/p次乘法运算和n/√p个乘积的局部求和运算。在这一步的最后，如图8-2c所示，每个进程有n/√p个部分和，对它们必须沿着每一行累加，得到结果向量。因此，以每行的最右边进程为目标，本算法的最后一步是每行的 $n / \sqrt { p }$ 个值的多对一归约。

并行运行时间在第一步中，从最右边的进程发送大小为n/√p的消息到对角线上的进程（图8-2a)，需要的时间为t,+twn/√p。使用4.1.3节讲述的程序，我们可以执行按列的一对多广播操作，需要的时间最多为(ts+twn/√p)log(√p)。忽咯加法运算的时间，最后按行的多对一归约操作也需要同样的时间。假设一对乘法和加法需要单位时间，则计算中每个进程需要的时间大约为 $n ^ { 2 } / p$ 。因此，这个过程的并行运行时间为

$$
T _ { P } = \overbrace { n ^ { 2 } / p } ^ { \mathrm { ~ } } + \overbrace { t _ { s } + t _ { w } n / \sqrt { p } } ^ { \mathrm { ~ } } +
$$

$$
\begin{array} { r l r } { \overbrace { ( t _ { s } + t _ { w } n / \sqrt { p } ) \log ( \sqrt { p } ) } ^ { } } & { { } + } & { \overbrace { ( t _ { s } + t _ { w } n / \sqrt { p } ) \log ( \sqrt { p } ) } ^ { } } \end{array}
$$

$$
\approx \ { \frac { n ^ { 2 } } { p } } + t _ { s } \log p + t _ { w } { \frac { n } { \sqrt { p } } } \log p
$$

可扩展性分析使用公式(8-1)和(8-7)，并利用关系式 $T _ { o } = p T _ { p } - W$ （公式(5-1)），我们可以得到这个并行算法开销函数的下述表达式：

$$
T _ { o } = t _ { s } p \log p + t _ { w } n \sqrt { p } \log p
$$

现在我们按照5.4.2节的方法，逐一考虑开销函数的各项，进行近似等效率分析（更精确的等效率分析见习题8.4）。对开销函数的 $t _ { s }$ 项，公式(5-14)产生

$$
W = K t _ { s } p \log p
$$

公式(8-9)给出关于消息启动时间的等效率项。通过用问题的规模 $n ^ { 2 }$ 平衡 $t _ { \kappa } n \sqrt { p } \log p$ 项，可得到由 $\ell _ { w }$ 导出的等效率函数。利用公式(5-14)的等效率关系，可得：

$$
\begin{array} { r c l } { { W = n ^ { 2 } } } & { { = } } & { { K t _ { w } n \sqrt { p } \log p } } \\ { { n } } & { { = } } & { { K t _ { w } \sqrt { p } \log p } } \\ { { n ^ { 2 } } } & { { = } } & { { K ^ { 2 } t _ { w } ^ { 2 } p \log ^ { 2 } p } } \\ { { W } } & { { = } } & { { K ^ { 2 } t _ { w } ^ { 2 } p \log ^ { 2 } p } } \end{array}
$$

最后，由于二维划分的并发度为 $n ^ { 2 }$ （即可以使用的最大进程数目为 $m ^ { 2 }$ )，可得下列公式：

$$
\begin{array} { r c l } { { p } } & { { = } } & { { { \cal O } ( n ^ { 2 } ) } } \\ { { n ^ { 2 } } } & { { = } } & { { \Omega ( p ) } } \\ { { { \cal W } } } & { { = } } & { { \Omega ( p ) } } \end{array}
$$

在公式(8-9)、(8-10)、(8-11)中，等号右边最大的表达式决定本并行算法的整体等效率函数。为了简化分析，我们忽咯常数的影响，只考虑保持固定效率所需的问题规模增加的渐近速度。由tw（公式(8-10)）导致的渐近等效率项显然对由t,（公式(8-9)）和并发性（公式(8-11)）导致的渐近等效项占有优势。因此，整体渐近等效率函数为(plog²p)。

等效率函数也决定成本最优的标准（见5.4.3节）。如果等效率函数为0(plog²p)，则对于给定规模为W的问题，使成本最优的最大进程数目可由以下关系式确定：

$$
\begin{array} { r c l } { { p \log ^ { 2 } p } } & { { = } } & { { O ( n ^ { 2 } ) } } \\ { { } } & { { } } & { { } } \\ { { \log p + 2 \log \log p } } & { { = } } & { { O ( \log n ) } } \end{array}
$$

忽略低次项，

$$
\log p \ = \ O ( \log n )
$$

在公式(8-12)中用 $\log n$ 代替 $\log p$ ，

$$
\begin{array} { r c l } { { p \log ^ { 2 } n } } & { { = } } & { { O ( n ^ { 2 } ) } } \\ { { } } & { { } } & { { } } \\ { { p } } & { { = } } & { { O \left( \frac { n ^ { 2 } } { \log ^ { 2 } n } \right) } } \end{array}
$$

对于n×n矩阵-向量乘法的二维矩阵划分方法，公式(8-13)的右端给出成本最优时进程数目的渐近上界。

# 3.一维与二维划分的比较

比较公式(8-2)与(8-7)可见，在进程数目相等的情况下，矩阵-向量乘法中使用二维划分要比使用一维划分更快。如果进程数目超过 $n$ ，就不能使用一维划分。根据本节的分析，即使进程数目小于或者等于n，使用二维划分仍然是最好的选择。

在另两个划分方案中，二维划分有更好（更小）的渐近等效率函数。因此，使用二维划分的矩阵-向量乘法有更好的可扩展性；也就是说，与一维划分相比，二维划分可以在更多的进程中得到同样的效率。

# 8.2 矩阵与矩阵的乘法

本节讨论两个 $_ { n } \times n$ 稠密矩阵 $\pmb { A }$ 与 $B$ 相乘得到乘积矩阵 $C = A \times B$ 的并行算法。本章矩阵乘法的所有并行算法都基于算法8-2给出的传统串行算法。如果我们假定一次加法与乘法运算对（第8行）需要一个单位时间，则这个算法的串行运行时间为 $n ^ { 3 }$ 。虽然也可以找到具有更好渐近串行复杂度的矩阵乘法算法，例如Strassen算法，但是，为简单起见，在本书中我们仍然假定传统算法是可用的最好串行算法。习题8.5探讨用Strassen方法作为基本算法时的并行矩阵乘法算法的性能。

1. procedure MAT_MULT $( A , B , C )$   
2. begin   
3. for $i : = 0$ to n - 1 do   
4. for $j : = 0$ to n - 1 do   
5. begin   
6. $C [ i , j ] : = 0 ;$   
7. for $k : = 0$ to n - 1 do   
8. $C [ i , j ] : = C [ i , j ] + A [ i , k ] \times B [ k , j ] ;$   
9. endfor;   
10. end MAT_MULT

# 算法8-3 $\mathbf { n } \times \mathbf { n }$ 矩阵块大小为 $( { \boldsymbol { \mathsf { n } } } / { \boldsymbol { \mathsf { q } } } ) \times ( { \boldsymbol { \mathsf { n } } } / { \boldsymbol { \mathsf { q } } } )$ 的块矩阵桑法法

1. procedure BLOCK_MAT_MULT $( A , B , C )$   
2. begin   
3. for $i : = 0$ to q -1 do   
4. $\operatorname { f o r } j : = 0 \operatorname { t o } q - 1 \mathrm { d } \mathbf { 0 }$   
5. begin   
6. Initialize all elements of Ci.j to zero;   
7. for $k : = 0$ to q - l do   
8. $C _ { i , j } : = C _ { i , j } + A _ { i , k } \times B _ { k , j } ;$   
9. endfor;   
10. end BLOCK_MAT_MULT

在矩阵乘法以及矩阵的其他各种算法中，块矩阵运算是一个很有用的概念。在矩阵计算中，我们经常可以把对矩阵所有元素的标量代数运算转换成对原矩阵的子矩阵或者块矩阵的矩阵代数运算。这种对子矩阵的代数运算称为块矩阵运算（block matrixoperation）。例如，

$n \times n$ 矩阵可以看成块 $A _ { i , j } ( 0 < i , j < q )$ 的 $q \times q$ 矩阵，其中每个块 $A _ { i , j }$ 是原矩阵的一个 $( n / q ) \times ( n / q )$ 子矩阵。因此，算法8-2中表示的矩阵乘法算法可写成算法8-3，其中第8行的乘法与加法运算分别为矩阵的乘法与加法运算。算法8-2与算法8-3不仅是最后结果相同，而且每个算法的标量加法与标量乘法的总次数也完全相同。算法8-2需要进行n次标量的加法与乘法运算，而算法8-3需要执行q次矩阵乘法，每次涉及(n/q)×(n/q)个矩阵并需要(n/q)次标量加法与乘法运算。我们可以用p（选择q=√P）个进程实现并行块矩阵乘法，每个进程计算不同的Ci块。

下面几小节介绍算法8-3的几种并行形式。以下每个并行矩阵乘法算法都使用矩阵的块二维划分。

# 8.2.1 简单的并行算法

考虑两个n×n矩阵A和B，把它们分别划分成p个大小为(n/√p)×(n/√p)的块Ai和Bi(0<i,j<√p)。这些块映射到√p×√p个进程的逻辑格网。这些进程的标号为Pij(0<i,j<√p-1)。进程Pij最初存储Aij和Bij，并计算结果矩阵的块Cij。计算子矩阵Cij需要所有子矩阵Ai和Bkj(0<k<√p-1)。为了得到全部Ai和Bkj，要在这些进程的每行进行矩阵A的块的多对多广播操作，同时在这些进程的每列进行矩阵B的块的多对多广播操作。在Pij得到Ai,和Bkj(0<k$\le \sqrt { p - 1 } )$ 后，再执行算法8-3中第7和第8行的子矩阵乘法和加法运算。

性能与可扩展性分析本算法要在各进程组（每组√P个进程）中进行两次多对多广播步骤（每次包括在进程格网的所有行和列同时进行√P次广播）。传输的消息是包含n2/p个元素的子矩阵。从表4-1可知，总通信时间是2(t,log(√p)+tw(n²/p)(√p-1)）。通信步骤结束后，每个进程计算子矩阵Cij，需要进行(n/√p)×(n/√p)子矩阵的√p次乘法操作（算法8-3中第7、8行，q=√p）。这一过程需要的总时间为√p×(n/√p)=n³/p。所以并行运行时间近似为：

$$
T _ { P } = { \frac { n ^ { 3 } } { p } } + t _ { s } \log p + 2 t _ { w } { \frac { n ^ { 2 } } { \sqrt { p } } }
$$

进程-时间积为n+t,plogp+2twn2√p，当p=O(n2)时，并行算法是成本最优的。

由tw和ts导致的等效率函数分别是tsp logp和8(tw)p3/2。因此，由通信开销导致的整体等效率函数为(p3/2)。这个算法使用的最大进程数目为n²；所以p<n²或n>p3/2。从而由并发导致的等效率函数也是 $\Theta ( p ^ { 3 / 2 } )$ 。

本算法的一个显著缺陷是它对内存需求过大。在通信阶段的最后，每个进程有矩阵A和B的√p个块，每个块需要的内存为0(n2/p)，每个进程需要的内存为9(n2/√p)。全部进程需要的总内存为(n²√p），这是串行算法所需内存的√P倍。

# 8.2.2 Cannon算法

Cannon算法是8.2.1节提出的简单并行算法的内存高效版本。为了研究这个算法，我们再把矩阵A和B划分成p个方块，进程的标号从P00到Pp-i.P-，并在最初把子矩阵Ai和Bi分配给进程Pij。虽然第i行的每个进程需要全部√p个子矩阵Ai(0<k<√p)，但我们还是能调度第i行√p个进程的计算，使得每个进程在任何时刻都使用不同的Ai。每完成一次子矩阵乘法，这些块在各进程之间被轮流使用，使得每次轮流之后每个进程都可以得到新的 $A _ { i , k }$ 。对列使用同样的调度，则在任何时刻，任何进程至多拥有每个矩阵的一个块，在所有的进程中，该算法需要的总内存量为 $\Theta ( n ^ { 2 } )$ 。Cannon算法正是基于这个思想。图8-3说明Cannon算法中不同进程上子矩阵乘法的调度过程，·其中有16个进程。

![](images/aa440da9c399493f80fda548f03e0c892096a65b8c8ef36b78e47ac1317dbfae.jpg)  
a）A的初始排列

![](images/0d314780647dce0cc0e5769195895a056b7df720f5368180d481b16c6c94f012.jpg)  
b）B的初始排列

![](images/806ae157babad80149de475bf92a04e0a45a4bf40e6b2ae43751a50d8a1449fe.jpg)  
c）初始排列后的A和B

![](images/714826501fc179eb778a3f15ad770512da5a785803207a877e8de10a3f29e94f.jpg)  
d）初次移动后的子矩阵位置

<table><tr><td rowspan=1 colspan=1>A0.3B0</td><td rowspan=1 colspan=1>A0.0Bo1</td><td rowspan=1 colspan=1>A01B12</td><td rowspan=1 colspan=1>A0.2B23</td></tr><tr><td rowspan=1 colspan=1>A10B0.0</td><td rowspan=1 colspan=1>AB</td><td rowspan=1 colspan=1>A12B22</td><td rowspan=1 colspan=1>A13B3.3</td></tr><tr><td rowspan=1 colspan=1>A2.1B10</td><td rowspan=1 colspan=1>A2.2B2.1</td><td rowspan=1 colspan=1>A2.3B.2</td><td rowspan=1 colspan=1>A2.0B0.3</td></tr><tr><td rowspan=1 colspan=1>A3.2B2.0</td><td rowspan=1 colspan=1>A33B3.1</td><td rowspan=1 colspan=1>A30B0.2</td><td rowspan=1 colspan=1>A3.1B1.3</td></tr></table>

e）第二次移动后的子矩阵位置

![](images/ce372885651574caf40c2a6abb9694759529a2eb3658a6afa6285e6f7cfc9682.jpg)  
f）第三次移动后的子矩阵位置  
图8-3Cannon算法在16个进程上的通信步骤

在算法的第一个通信步骤中，用这样一种方式排列矩阵A和B的块，使得每个进程对其本地子矩阵相乘。如图8-3a所示，排列矩阵A和 $| B |$ 的块时，用i步把矩阵A的所有子矩阵 $A _ { i , j }$ 都移到左边（带回绕）。与之类似，用j步把矩阵 $B$ 的所有子矩阵 $B _ { i , j }$ 都移到上边 (带回绕)。进程的每行和每列都要进行循环移位操作（见4.6节)，并且保持子矩阵 $A _ { i , ( j + i ) \bmod \sqrt { p } }$ 和 $B _ { ( j + i ) \bmod \sqrt { p } , j }$ 在进程 $P _ { i , j }$ 中。图8-3c显示初始排列后的矩阵A和 $B$ 的块，此时每个进程可以进行第一次子矩阵相乘运算。完成-个子矩阵相乘步骤后，矩阵A的每个块向左移动一步，矩阵 $B$ 的每个块向右移动一步（也带回绕），如图8-3d所示。在进程 $P _ { i , j }$ 中一共进行 $\sqrt { p }$ 次这样的 $A _ { i , k }$ 与 $B _ { k , j } \left( 0 < k < \sqrt { p } \right.$ )的相乘和一步向上移位。这就完成矩阵A和B的乘法运算。

性能分析如图8-3a和b所示，两个矩阵的初始排列包括一次按行和一次按列的循环移位。在其中任何一次移位中，每个块移动的最大距离是 $\sqrt { p } - 1$ ，两次移位操作需要的总时间为$2 ( t _ { s } + t _ { w } n ^ { 2 } / p )$ （见表4-1）。本算法的每个计算与移位阶段中都有 $\sqrt { p }$ 次单步移位，每个单步移位需要的时间为 $t _ { s } + t _ { w } n ^ { 2 } / p$ ，因此，算法这一阶段两个矩阵的总通信时间为 $2 ( t _ { s } + t _ { w } n ^ { 2 } / p ) \sqrt { p }$ 。在带宽足够的网络中，当 $p$ 充分大时，与计算和移位阶段相比，初始排列的通信时间可以忽略不计。

每个进程要进行 $\sqrt { p }$ 次 $( n / { \sqrt { p } } ) \times ( n / { \sqrt { p } } )$ 子矩阵乘法运算。假设每次加法和乘法需要一个单位时间，每个进程花在计算中的总时间为 $n ^ { 3 } / p$ 。因此，本算法需要的总并行运行时间大约为

$$
T _ { P } = { \frac { n ^ { 3 } } { p } } + 2 { \sqrt { p } } t _ { s } + 2 t _ { w } { \frac { n ^ { 2 } } { \sqrt { p } } }
$$

Cannon算法的成本最优条件与8.2.1节提出的简单算法中的条件相同。与简单算法一样，Cannon算法的等效率函数是 $\Theta ( p ^ { 3 / 2 } )$ 。

# 8.2.3 DNS算法

到目前为止提出的矩阵相乘算法中，都对输入和输出矩阵进行块二维划分，而且对 $n \times n$ 矩阵使用的进程数不超过 $n ^ { 2 }$ 。由于在串行算法中有 $\Theta ( n ^ { 3 } )$ 次操作，所以这些算法的并行运算时间为 $\Omega ( n )$ 。我们现在给出一种并行算法，它基于划分中间数据，最多能够使用 $n ^ { 3 }$ 个进程，通过使用 $\Omega ( n ^ { 3 } / \log { \ n } )$ 个进程，执行矩阵乘积所需的时间为 $\Theta ( \log \ n )$ 。这个算法称为DNS算法，因为它是由Dekel、Nassimi和Sahni提出的。

我们首先介绍基本思想，不考虑进程间的通信。假设可以用 $n ^ { 3 }$ 个进程计算两个 $n \times n$ 矩阵的乘积。这些进程排列在一个三维 $n \times n \times n$ 逻辑阵列中。由于矩阵相乘算法要执行 $n ^ { 3 }$ 次标量乘法，每个进程都安排一次标量乘法。根据进程在阵列中的位置对它们标号，分配进程 $P _ { i , j , k } ( 0 <$ $i , j , k < n )$ 执行 $A [ i , k ] \times B [ k , j$ ]的乘法运算。每个进程完成一个乘法运算步骤后，再将各个进程$P _ { i , j , 0 } , \ P _ { i , j , 1 } , \ \cdots , \ P _ { i , j , n - 1 }$ 的内容相加，得到 $C [ i , j ]$ 。所有 $C [ i , j$ ]的求和运算可以同时在 $\log n$ 个步骤中进行。因此，乘法运算需要一个步骤；而求和运算需要log $\pmb { n }$ 个步骤；也就是说，用这个算法计算 $\textit { \textbf { n } } \times \textit { \textbf { n } }$ 矩阵的乘积所需时间为 $\Theta ( \log n )$ 。

基于这个思想，我们现在来描述矩阵乘法的一个并行实现。如图8-4所示，可以把进程排列设想成n个平面，每个平面n×n个进程。每个平面对应k的一个不同值。初始时，如图8-4a所示，矩阵分布在三维进程阵列的底部与k=0相对应的n2个进程中。最初进程Pij.拥有A[i,j和$B [ i , j ]$ 。

![](images/026ca2a387270157a362e2dafa35969ac327587b9ec5526d79ec952b93f1d95c.jpg)  
图8-4在64个进程上的 $4 \times$ 4矩阵A和B的乘法中DNS算法的通信步骤。c）中带阴影的进程存储A的第一行元素，d）中带阴影的进程存储B的第一列元素

进程 $P _ { i , j , }$ ·的纵向列计算 $A [ i , * ]$ 行与 $B [ * j ]$ 列的点积。因此， $\pmb { A }$ 的行与 $\pmb { B }$ 的列需要进行相应的移动，保证进程 $P _ { i , j , }$ ·的每个纵向列有 $\boldsymbol { A } [ i , * ]$ 行与 $B [ * , j ]$ 列。准确地说，进程 $P _ { i , j , k }$ 应有 $\lvert A [ i \mathcal { k } ]$ 与 $B [ k , j ]$ 。

图8-4a～c显示各个进程中分布的矩阵A的元素的通信模式。首先，把A的每一列移到不同的平面，保证第j列占据对应于k=j的平面中的同样位置，就像最初在对应于k=0的平面中所做的那样。图8-4b显示把A[i,j]从Pij.0移动到Pijj后矩阵A的分布。通过沿着j轴的一对多广播，矩阵A的各列在相应的平面上被复制n次。这一步骤的结果如图8-4c所示，其中n个进程Pij.0，

$$
\vdots \vdots \vdots \vdots \vdots \vdots \ddots \vdots \vdots \ddots \vdots \vdots \ddots
$$

$P _ { i , j , \imath } , \cdots , \ P _ { i , j , n - 1 }$ 都从 $P _ { i , j , j }$ 处得到 $A [ i , j ]$ 的一个副本。此时， $P _ { i , j }$ .的每个纵向列有了 $A [ i , * ]$ 行。  
准确地说，进程 $P _ { i , j , k }$ 有了 $A \{ i , k \}$ 。

矩阵 $B$ 的通信步骤是类似的，但是进程下标i和的作用相互对调。在开始的一对一通信步骤，把 $B \{ i , j \}$ 从 $P _ { i , j , 0 }$ 移动到 $P _ { i , j , i }$ ，然后从 $P _ { i , j , i }$ 广播到 $P _ { 0 . i . j } , P _ { 1 , i . j } , \cdots , P _ { n - 1 , i , j }$ 。图8-4d表示沿i轴进行这个一对多广播后矩阵 $B$ 的分布。至此，进程 $P _ { i , j , }$ \*的每个纵向列有了 $B [ * , j ]$ 列。现在进程 $P _ { i , j , k }$ 除 $A [ i , k ]$ 之外还拥有 $B \{ k , j \}$ 。

在这些通信步骤之后， $A [ i , k ]$ 与 $B [ k , j ]$ 在进程 $P _ { i , j , k }$ 中相乘。现在通过沿 $k$ 轴的多对一归约，可以得到乘积矩阵的所有元素C[i,j]。在这个步骤中，进程Pi,j.o累加来自进程Pi,j,，…，Pi,in-1的乘积结果。图8-4表示的是求 $C [ 0 , 0 ]$ 的这一步骤。

DNS算法中有三个主要的通信步骤，1.把 $A$ 的列和 $\pmb { B }$ 的行移动到它们各自的平面，2.沿A的j轴和B的i轴执行一对多传播，3.沿k轴进行多对一归约。所有这些操作都在各进程组（每组$\pmb { n }$ 个进程）中进行，所需时间为 $\Theta ( \log \ n )$ 。因此，用DNS算法对 $n ^ { 3 }$ 个进程进行两个 $n \times n$ 矩阵相乘所需的并行运行时间为 $\Theta ( \log n )$ 。

# 进程数少于 $n ^ { 3 }$ 的DNS算法

$n ^ { 3 }$ 个进程的DNS算法不是成本最优的，因为它的进程-时间乘积 $\Theta ( n ^ { 3 } \log { \textbf { \em n } } )$ 超过矩阵乘法的串行复杂度 $\Theta ( n ^ { 3 } )$ 。现在我们给出这个算法的成本最优的版本，其中使用的进程数少于 $n ^ { 3 }$ 个。习题8.6中提出使用进程少于 ${ \pmb n } ^ { 3 }$ 个的DNS算法的另一个变体。.

对于某个 $q < n$ ，假设 $p$ 是进程数， $p = q ^ { 3 }$ 。为了实现DNS算法，我们把两个矩阵划分成$( n / q ) \times ( n / q )$ 的块。从而每个矩阵可以看成是由这些块排成的 $q \times q$ 二维方阵。这个算法在 $q ^ { 3 }$ 个进程上的实现与在 $n ^ { 3 }$ 个进程上的实现非常相似。唯一的不同是现在对块操作而不是对矩阵的单个元素操作。由于 $1 < q < n$ ，进程数可在1与 ${ { n } ^ { 3 } }$ 之间变化。

性能分析第一个通信步骤是矩阵A和B的一对一通信，每个矩阵需要的时间为t,+tw(n/q)²。第二个通信步骤是矩阵A和B的一对多通信，每个矩阵需要的时间为t,logq+tw(n/q)²logq。最后的通信步骤是矩阵C的一次多对一归约，需要的时间为t,logq+tw(n/q)²logq。每个进程中(n/q)×(n/q)子矩阵相乘需要的时间为(n/q)3。第一步矩阵A和B一对一通信的时间可以忽略，因为它远远小于一对多通信的时间和多对一归约的时间。在最后的多对一归约步骤中，加法的计算时间也可以忽略，因为它的数量级小于子矩阵相乘时间的数量级。用这些假设，可得如下关于DNS算法并行运行时间的近似表达式：

$$
T _ { P } \approx \left( { \frac { n } { q } } \right) ^ { 3 } + 3 t _ { s } \log q + 3 t _ { w } \left( { \frac { n } { q } } \right) ^ { 2 } \log q
$$

由于 $p = q ^ { 3 }$ ，我们得到

$$
T _ { P } = { \frac { n ^ { 3 } } { p } } + t _ { s } \log p + t _ { w } { \frac { n ^ { 2 } } { p ^ { 2 / 3 } } } \log p
$$

并行算法的全部成本为n³+tsplogp+twn²p13logP。等效率函数为0(p(log p)3)。当n =$\Omega ( p ( \log p ) ^ { 3 } )$ 或者 $p = O ( n ^ { 3 } / ( \log n ) ^ { 3 } )$ 时，本算法是成本最优的。

# 8.3线性方程组求解

这一节我们讨论如何求解如下形式的线性方程组：

$$
{ \begin{array} { r c c c c c c } { a _ { 0 , 0 } x _ { 0 } } & { + } & { a _ { 0 , 1 } x _ { 1 } } & { + } & { \cdots \cdot + \ a _ { 0 , n - 1 } x _ { n - 1 } } & { = \ b _ { 0 } } \\ { a _ { 1 , 0 } x _ { 0 } } & { + } & { a _ { 1 , 1 } x _ { 1 } } & { + } & { \cdots \cdot + \ a _ { 1 , n - 1 } x _ { n - 1 } } & { = \ b _ { 1 } } \\ { \vdots } & { \vdots } & & { \vdots } & & { \vdots } \\ { a _ { n - 1 , 0 } x _ { 0 } } & { + } & { a _ { n - 1 , 1 } x _ { 1 } } & { + } & { \cdots \cdot + \ a _ { n - 1 , n - 1 } x _ { n - 1 } = \ b _ { n - 1 } } \end{array} }
$$

用矩阵表示法这个方程组可以写成 $A x = b$ 。此处系数矩阵 $\pmb { A }$ 是稠密的、 $A [ i , j ] = a _ { i , j } ,$ $b$ 是$n \times 1$ 向量 $[ b _ { 0 } , b _ { 1 } , \cdots , b _ { n - 1 } ] ^ { T }$ ， $\pmb { x }$ 是 $n \times 1$ 未知解向量 $[ x _ { 0 } \mathrm { ~ , ~ } x _ { 1 } \mathrm { ~ , ~ } \cdots \mathrm { ~ , ~ } x _ { n - 1 } ] ^ { T } .$ 。下面用 $A [ i , j ]$ 表示 $\mathbf { \alpha } _ { a _ { i , j } }$ ，用 $x [ i ]$ 表示 $x _ { i }$ 。

解方程组 $A x = b$ 通常分两个阶段。首先，用一些代数运算把 $A x = b$ 化简成上三角形式的方程组

$$
\begin{array} { r c c c c c c c c c c c c } { x _ { 0 } ~ + } & { u _ { 0 , 1 } x _ { 1 } ~ + } & { u _ { 0 , 2 } x _ { 2 } ~ + } & { \cdots } & { ~ + } & { u _ { 0 , n - 1 } x _ { n - 1 } } & { = } & { y _ { 0 } } & & & \\ & & { x _ { 1 } ~ + } & { u _ { 1 , 2 } x _ { 2 } ~ + } & { \cdots } & { ~ + } & { u _ { 1 , n - 1 } x _ { n - 1 } } & { = } & { y _ { 1 } } & & & \\ & & & & & & { \vdots } & & & { \vdots } \\ & & & & & & & { x _ { n - 1 } } & { ~ = } & { y _ { n - 1 } } & & \end{array}
$$

把这个方程组写成 $U x = y$ ，其中 $U$ 是单位上三角矩阵，即主对角线元素为1，而所有对角线下的元素为0。在形式上， $i < .$ 时 $U [ i , j ] = 0$ ，否则 $U [ i , j ] = u _ { i , j }$ 。此外 $U [ i , i ] = 1 \ ( 0 < i < n ) .$ 第二阶段，使用回代法（见8.3.3节)，按照相反的次序从 $x [ n { - } 1 ]$ 到 $x [ 0 ]$ ，求方程 $U x = y$ 的解。

我们将在8.3.1和8.3.2节中讨论用上三角化的经典高斯消元法的并行公式。在8.3.1节介绍直接高斯消元算法时，假设系数矩阵是非奇异的，并且用数值稳定的算法进行行列的置换。在8.3.2节讨论方程组稳定数值解的情形，在高斯消元算法的执行过程中，需要对矩阵的列进行置换。

虽然我们只讨论上三角化的高斯消元法，但也可用类似的方法把矩阵A分解成下三角矩阵L和单位上三角矩阵U的乘积，使得A=L×U。这种分解通常称为LU分解。在求解具有同样右端项的多个线性方程组时，进行LU分解是非常有用的。算法3.3给出了一个面向列的LU分解过程。

# 8.3.1简单高斯消元算法

串行的高斯消元算法有三个嵌套循环。根据循环的排列序，算法还有几种变体。算法8-4是高斯消元的一个变体。本节余下部分中将用来进行并行实现。这个算法程序把线性方程组Ax=b变成主对角线为1的上三角方程组Ux=y。我们假设矩阵U与A共享存储，并且覆盖A的上三角部分。算法8-4第6行计算的A[ij]实际是U[ij]。类似地，第8行A[k,k]=1实际是U[k,k]。第6、7行中，用A[k]作除数时，算法8-4假设A[kk]+0。

在这一节，我们仅讨论在算法8-4中对矩阵A的操作。程序第7行和第13行关于向量b的运算很简单，所以下面省略这些步骤。如果不执行第7、8、13、14行的步骤，则算法8-4进行关于A的LU分解，将A分成乘积L×U。在过程结束后，L存储在A的下三角部分，而U占据A的主对角线以上部分。

在k从0到n-1变化时，运用高斯消元过程系统地将变元x[k]从方程k+1到方程n-1中消去，从而把系数矩阵A变成上三角矩阵。如算法8-4所示，在外层循环的第k次迭代（从第3行开始）中，从第k+1到第n-1的每个方程都减去第k个方程的适当倍数（循环从第9行开始)。第k个方程（或者矩阵 $A$ 的第 $k$ 行）的倍数选择要保证从第 $k + 1$ 到第 $\hbar - 1$ 的每个方程中第 $k$ 个系数为零，从而从这些方程中消去 $x [ k ]$ 。在外层循环的第 $k$ 次迭代中，高斯消元过程的典型计算如图8-5所示。外层循环的第 $k$ 次迭代不包括第1行到第 $k$ 行和第1列到第 $k$ 列的任何计算。因此，在这一阶段，仅有A的右下方的 $( n - k ) \times ( n - k )$ 子矩阵（图8-5的阴影部分）参与运算过程。

算法8-4把线性方程组 $A X = 6$ 变成单位上三角方程组 $\mathsf { U } \mathsf { X } = \mathsf { y }$ 的串行高斯消元算法。矩阵U占用A的上三角部分。当A[k,k]在第6、7行中用作除数时，算法假设A $[ { \sf k } , { \sf k } ] \neq 0$

1. procedure GAUSSIAN_ELIMINATION $( A , b , y )$   
2. begin   
3. for $k : = 0$ to $n - 1$ do 1\* Outer loop \*/   
4. begin   
5. for $j : = k + 1$ to n -1 do   
6. $\begin{array} { r l } & { { \cal A } [ k , j ] : = { \cal A } [ k , j ] / { \cal A } [ k , k ] ; ~ / \ast \mathrm { D i v i s i o n } \mathrm { s t e p } \ast / } \\ & { \nu [ \dot { k } ] : = { b } [ k ] / { \cal A } [ k , k ] ; } \\ & { { \cal A } [ k , k ] : = 1 ; } \\ & { \mathrm { \bf \dot { \ m r } } i : = k + 1 \mathrm { t \bf 0 } n - 1 \mathrm { d \bf 0 } } \end{array} .$   
7.   
8.   
9. 1   
10. begin.   
11. for $j : = k + 1$ to n -1 do   
12. A[i,j] := A[i,j]- A[i,k] × A[k,j]; /\* Elimination step \*/   
13. $b [ i ] : = b [ i ] - A [ i , k ] \times y [ k ] ;$   
14. $A [ i , k ] : = 0 ;$   
15. endfor; 1\* Line 9 \*1   
16. endfor; /\* Line 3 \*/   
17. end GAUSSIAN_ELIMINATION

![](images/6442f4485f078c6c77bfd6521c61c568887630f1b02aedcec749311807fc96e5.jpg)  
图8-5高斯消元法中的一个典型计算

高斯消元法大约包括n2/2次除法运算（第6行）和(n/3)-(n2/2)次减法和乘法运算（第12行）。在本节，我们假设每次标量运算需要一个单位时间。根据这个假设，高斯消元过程的串行运行时间大约为 $2 n ^ { 3 } / 3$ （对于大的 $n$ )；即

$$
W = { \frac { 2 } { 3 } } n ^ { 3 }
$$

# 1.用一维划分的并行实现

现在考虑算法8-4的并行实现，其中系数矩阵在进程中间进行按行一维划分。算法采用一维按列划分的并行实现与之类似，其实现细节可以根据按行一维划分的实现过程确定（习题8.8和8.9)。

先考虑每个进程分配一行的情形，n×n系数矩阵A按照从P到Pn-的n个进程中的行划分。在这个映射中，进程P;最初存储的元素为A[ij]，0≤j<n。图8-6给出n=8时这种从矩阵到进程的映射。图中也说明 $k = 3$ 时外层循环迭代中的通信与计算情况。

<table><tr><td rowspan=2 colspan=1>P</td><td></td><td></td></tr><tr><td rowspan=1 colspan=2>1   （0,1）(0,2)(0.3)(0,4)(0,5)(0.6)（0.7)</td></tr><tr><td rowspan=1 colspan=1>P</td><td rowspan=1 colspan=2>0    ！   (1,2)(1,3)(1,4)(1.5)(1.6)(1,7)</td></tr><tr><td rowspan=1 colspan=1>P</td><td rowspan=1 colspan=2>0    0    1  (2.3)(2.4)(2.5)(2,6)(2.7)</td></tr><tr><td rowspan=1 colspan=1>P</td><td rowspan=1 colspan=2>0    0    0  (3,3)(3.4）(3.5)(3.6）(3,7）：</td></tr><tr><td rowspan=1 colspan=1>P</td><td rowspan=1 colspan=2>0    0    0  (4.3)（4.4)(4.5)(4.6)(4.7)</td></tr><tr><td rowspan=1 colspan=1>P</td><td rowspan=1 colspan=1>0    0</td><td rowspan=1 colspan=1>0  (5.3)(5.4)(5.5)(5.6)(5.7)</td></tr><tr><td rowspan=1 colspan=1>P</td><td rowspan=1 colspan=1>0    0</td><td rowspan=1 colspan=1>0  (6.3)(6.4)(6.5)(6.6)(6.7)</td></tr><tr><td rowspan=1 colspan=1>P</td><td rowspan=1 colspan=1>0    0</td><td rowspan=1 colspan=1>0  （7.3)(7.4)(7.5)（7,6)（7.7)</td></tr></table>

a）计算:

$$
\begin{array} { l } { \mathrm { i } ) \ A [ k , j ] : = A [ k , j ] / A [ k , k ] , \ k < j < n } \\ { \mathrm { i } ) \ A [ k , k ] : = 1 \ } \end{array}
$$

<table><tr><td>P</td><td>1 (0.1) (0.2) ：</td><td>(0.3)(0.4） (0.5）（ (0.6) （0.7)</td></tr><tr><td>P</td><td>0 1 (1,2)</td><td>(1.3） （1.4) （1,5) (1,6) (1.7)</td></tr><tr><td>P</td><td>0 0</td><td>1 (2,3) (2.4) (2.5) (2.6) (2,7)</td></tr><tr><td>P</td><td>0 0</td><td>0 1 13.4）.(3.5) 3.6）.(3.7) 1L</td></tr><tr><td>P4</td><td>0 0</td><td>0 （4.3）Y(4.4）（4,5）Y（4,6）Y（4,7)</td></tr><tr><td>P</td><td>0 0 0</td><td>(5,3）Y(5.4）Y（5.5）Y(5,6）Y(5.7) ： ： ·</td></tr><tr><td>P</td><td>0 0 0</td><td>(6.3)Y(6.4）Y（6,5）(6.6）Y(6.7) ：</td></tr><tr><td>P7</td><td>0 0 0</td><td>（7,3）V(7,4)V（7,5）V(7,6）V（77)</td></tr></table>

b）计算:

行A[k,]的一对多广播

<table><tr><td rowspan=1 colspan=1>P</td><td rowspan=1 colspan=1>1  (0,1）(0.2) (0.3） (0.4） (0.5)(0.6) (0.7)</td></tr><tr><td rowspan=1 colspan=1>P</td><td rowspan=1 colspan=1>0    1  (1.2)(1,3) (1,4) (1.5)(1,6) (1.7)</td></tr><tr><td rowspan=1 colspan=1>P</td><td rowspan=1 colspan=1>0    0    1  (2.3)(2.4)(2,5)(2,6) (2.7)</td></tr><tr><td rowspan=1 colspan=1>P</td><td rowspan=1 colspan=1>0    0    0    1  (3.4)(3,5)(3.6) (3,7)</td></tr><tr><td rowspan=1 colspan=1>P</td><td rowspan=1 colspan=1>0    0    0  （4.3)（4.4)(4.5)（4,6)(4，7)：</td></tr><tr><td rowspan=1 colspan=1>Ps</td><td rowspan=1 colspan=1>0    0    0  (5.3) (5.4)(5.5)(5.6) (5.7)</td></tr><tr><td rowspan=1 colspan=1>P</td><td rowspan=1 colspan=1>0    0    0  (6,3）（(6;4)(6.5)(6,6）(6,7)1</td></tr><tr><td rowspan=1 colspan=1>P</td><td rowspan=1 colspan=1>：    /00    0  （7.3) (7.4) (7.5) (7,6）.(7.7)</td></tr></table>

c）计算:

$$
\begin{array} { r l } & { \mathrm { ( i ) } ~ A [ i , j ] : = A [ i , j ] { - } A [ i , k ] \times A [ k , j ] , } \\ & { \quad \quad k < i < n \mathscr { F } { \sharp } k < j < n } \\ & { \mathrm { ( i i ) } ~ A [ i , k ] : = 0 , ~ k < i < n } \end{array}
$$

图8-6在8个进程中按行划分的 $8 \times 8$ 矩阵中，对应于 $k = 3$ 迭代的高斯消元步骤

算法8-4和图8-5表示在第k次迭代开始时， $A [ k , k ]$ 除 $A [ k , k + 1 ]$ ， $A \{ k , k + 2 \}$ ，…， $A [ k , n - 1 ]$ 的情形。参与运算的所有元素（由图8-6a阴影部分所示）属于同一个进程。所以这个步骤不需要任何通信。在算法的第二个计算步骤（第12行的消元步骤）中，矩阵参与计算部分的所有其他行都要使用第 $k$ 行修改后（经过除法运算）的元素。如图8-6b所示，这个过程需要一次从第k行参与计算部分到存储 $k + 1$ 至 $n { - } 1$ 行的各个进程的一对多广播。最后，如图8-6c中的阴影部分所示，在矩阵剩余的参与计算部分，计算 $A [ i , j ] : = A [ i , j ] { - } A [ i , k ] \times A [ k , j ]$

与图8-6a对应的第 $k$ 次迭代中的计算步骤需要在进程 $P _ { k }$ 中进行 $n ^ { - } k ^ { - 1 }$ 次除法运算。类似地，图8-6c中的计算步骤包括在所有的进程 $P _ { i }$ $( k < i < n )$ 的第 $k$ 次选代中进行 $n - k - 1$ 次减法和乘法运算。假设一次单独的算术运算需要一个单位时间，则第 $k$ 次迭代中需要的计算时间为 $3 ( n - k - 1 )$ 。注意，当 $P _ { k }$ 进行除法运算时，其他 $p - 1$ 个进程是空闲的，当进程 $P _ { k + 1 } , \ P _ { k + 2 } , \ \cdots , \ P _ { n - 1 }$ 执行消元操作步骤时，进程 $P _ { 0 } , \ P _ { 1 } , \ \cdots , \ P _ { k }$ 是空闲的。因此在高斯消元法的并行实现中，图8-6a和c显示的计算步骤需要的总时间为 $3 \sum _ { k = 0 } ^ { n - 1 } ( n - k - 1 ) = 3 n ( n - 1 ) / 2 \ 。$

所的时 $( t _ { s } + t _ { w } ( n { - } k { - } 1 ) ) \log n$ 全$\cdot \sum _ { k = 0 } ^ { n - 1 } ( t _ { s } + t _ { w } ( n - k - 1 ) ) \log n$ $[ t _ { s } n + t _ { w } ( n ( n - 1 ) / 2 ) ] \log n _ { \mathrm { ~ \normalfont ~ { ~ \cdot ~ } ~ } }$ 并行运行时间为

$$
T _ { P } = { \frac { 3 } { 2 } } n ( n - 1 ) + t _ { s } n \log n + { \frac { 1 } { 2 } } t _ { w } n ( n - 1 ) \log n
$$

由于进程数为 $\pmb { n }$ ，由(8-18)式中与 $\ell _ { w }$ 相关的项导致的成本（即进程-时间乘积）为 $\Theta ( n ^ { 3 } \log { n } )$ 。这个成本渐近地高于该算法的串行运行时间（公式(8-17))，因此这个并行实现不是成本最优的。

流水线通信与计算我们现在给出一个高斯消元法的并行实现，它在 $\pmb { n }$ 个进程上是成本最优的。

在刚讨论的并行高斯消元算法中，算法8-4的外层循环中的n个迭代是顺序执行的。在任何给定时间，所有的进程都在相同的迭代中运行。只有当第k次迭代的所有通信与计算全部完成后，才能开始第k+1次迭代。在进程异步工作的条件下，可以对算法的性能进行重大改进；也就是说，任何进程不必等待其他进程完成迭代就可以进行下一步迭代。我们把它称为高斯异步消元法或者高斯消元流水线法。图8-7说明算法8-4的流水线算法，其中5×5矩阵沿着行划分成5个进程的逻辑线性阵列。

在算法8-4的第k次迭代中，进程P把矩阵第k行的部分广播到进程Pk+1，Pk+2，，Pn-1（见图8-6b)。假设这些进程形成一个逻辑线性阵列，Pk+1是第一个从进程P接收第k行的进程，则P+必须把收到的数据转发到Pk+2。但是，把第k行转发到Pk+2之后，进程Pk+不必等待直到Pn-的所有进程收到第k行后再执行消元步骤（第12行）。类似地，只要Pk+2把第k行数据传送到Pk+3后就能开始自己的计算，以此类推。同时，完成第k次迭代的计算后，进程Pk+可以执行除法步骤（第6行），并且通过把第k+1行发送到进程Pk+2开始这一行的广播。

在流水线高斯消元法中，每个进程独立地重复执行下述操作步骤，直到n个迭代全部完成。为简单起见，我们假设步骤1）与步骤2）需要相同的时间（这样的假设不影响分析)：

1）如果一个进程有发送给其他进程的数据，就把那些数据发送给相关的进程。  
2）如果一个进程能够使用已经有的数据进行一些计算，就进行这种计算。  
3）否则，进程等待接收数据，用于进行上述操作。

图8-7显示在5个进程中，对5×5矩阵按行划分的高斯消元法流水线并行执行的16个步骤。如图8-7a所示，第一步是在进程P执行第0行的除法运算。然后把修正后的第0行送到进程P，（图8-7b)，进程Pi再把它传输到进程P2（图8-7c)。这样进程Pi可以独立地使用第0行执行消元步骤（图8-7d)。下一步进程 $P _ { 2 }$ 使用第0行执行消元步骤（图8-7e)。同时，已经完成第0次迭代的进程Pi开始它的第1次迭代的除法步骤。在任何给定的时间，可以在不同的进程中执行相同迭代的不同阶段。例如，在图8-7h中，当进程 $P _ { 3 }$ 和进程 $P _ { 4 }$ 进行第1次迭代的通信时，进程 $P _ { 2 }$ 执行同一次迭代的消元步骤。此外，在不同的进程中可以同时执行不止一次迭代。例如，在图8-7i中，当进程 $P _ { 3 }$ 进行第1次迭代的消元步骤时，进程 $P _ { 2 }$ 执行第2次迭代的除法步骤。

![](images/e3f39ea2a9120baa79df6a2b4a1ec699a872150ffc86aefe16a53afafdea18a9.jpg)  
.图8-7用每个进程一行划分的 $5 \times 5$ 矩阵的流水线高斯消元法

![](images/ce69bf8a2b5ae72c9cb879da4b603444c762ea7068605f0593ae14121df017f5.jpg)

$$
\begin{array} { r l r } { \mathrm { ~ . ~ } } & { { } \quad } & { \mathrm { ~ . ~ } } \\ { \mathrm { ~ . ~ } } & { { } \quad } & { \mathrm { ~ . ~ } } \\ { \mathrm { ~ . ~ } } & { { } \quad } & { \mathrm { ~ . ~ } } \\ { \mathrm { ~ . ~ } } & { { } \quad } & { \mathrm { ~ . ~ } } \\ { \mathrm { ~ . ~ } } & { { } \quad } & { \mathrm { ~ . ~ } } \\ { \mathrm { ~ . ~ } } & { { } \quad } & { \mathrm { ~ . ~ } } \\ { \mathrm { ~ . ~ } } & { { } \quad } & { \mathrm { ~ . ~ } } \\ { \mathrm { ~ . ~ } } & { { } \quad } & { \mathrm { ~ . ~ } } \end{array}
$$

在同步算法中，所有的进程在同一时间只能执行同一迭代，而高斯异步消元法或者流水线高斯消元法与此不同，它是成本最优的。如图8-7所示，算法8-4中外层循环的连续迭代的启动由数目固定的操作步骤分开。一共有 $\pmb { n }$ 个这样的迭代被启动。最后的迭代只改变系数矩阵的右下角元素；因此，在迭代启动以后，算法在固定的时间内完成。所以整个流水线过程的步骤总数为 $\Theta ( n )$ （习题8.7)。在任何步骤中，要么有 $O ( n )$ 个元素在直接连接的进程之间通信，要么有一行的 $O ( n )$ 个元素在进行除法运算，或有一行的 $O ( n )$ 个元素在执行消元。每个这样的过程需要的时间为 $O ( n )$ 。因此，每个这样完整的过程由 $\Theta ( n )$ 个复杂度为 $O ( n )$ 的步骤组成，它的并行运行时间为 $O ( n ^ { 2 } )$ 。由于使用 $\pmb { n }$ 个进程，成本是 $O ( n ^ { 3 } )$ ，与高斯消元法的串行复杂度的数量级相同。因此，用系数矩阵一维划分的流水线版本的并行高斯消元法是成本最优的。

进程数少于n的一维块划分前面并行高斯消元法的流水线实现可以方便地改为用于 $n > p$ 的情况。考虑在 $p$ 个进程中划分的 $n \times n$ 矩阵 $( p < n )$ ，每个进程分配 $n / p$ 个相邻的行。图8-8说明在用这样一种映射的典型高斯消元法迭代中的通信。如图所示，算法的第 $k$ 次迭代需要把第 $k$ 行的参与部分送到存储第 $k + 1 , \cdots , n { - } 1$ 行的进程。

![](images/377b76145a8bd1e50f62480135100ee9780e61ae46a1af5816d02b8b80a3c46f.jpg)  
图8-8对于用块一维划分的分布在4个进程间的 $8 \times 8$ 矩阵，对应于 $k = 3$ 的高斯消元迭代中的通信

图8-9a表示使用一维块划分时，一个所有行都属于矩阵参与部分的进程，在第 $k$ 次迭代的消元步骤中执行 $( n { - } k { - } 1 ) n / p$ 次乘法和减法运算。注意，在最后第 $( n / p ) - 1$ 次迭代中，没有进程包含所有参与运算的行，但是我们忽咯这个异常情况。如果使用这个算法的流水线版本，则第 $k$ 次迭代中的最大负载进程的算术运算次数 $( 2 ( n { - } k { - } 1 ) / p )$ ，要远大于同一次迭代中一个进程的通信字数 $( n { - } k { - } 1 )$ 。因此，对相对于 $p$ 充分大的 $\pmb { n }$ ，在每次迭代中计算相对于通信来说是主要的。假设每次标量的乘法与减法运算需要一个单位时间，那么这个算法总的并行运行时间（不考虑通信开销）为 $2 ( n / p ) { \sum } _ { k = 0 } ^ { n - 1 } ( n - k - 1 )$ ，近似等于 $n ^ { 3 } / p$ 。

即使不考虑该算法的通信成本，其进程时间乘积也是 $n ^ { 3 }$ 。因此，并行算法的成本高于串行运行时间（公式(8-17)），为它的3/2倍。对于一维块划分，高斯消元法的这种低效率是由负载分配不平衡造成的进程空闲引起的。如图8-9a所示，对于 $8 \times 8$ 矩阵和4个进程，在对应于 $k = 3$ 的迭代（在算法8-4的外部循环）中，一个进程完全空闲，一个进程部分空闲，只有两个进程在满负荷工作。在外层循环的迭代次数完成一半时，仅仅有一半的进程在工作。进程空闲使并行算法比串行算法的成本更大。

如果在使用图8-9b所示的循环一维映射的进程中划分矩阵，就可以缓解这个问题。使用循环一维划分，在任何迭代中，最大与最小负载进程的计算负载量最多相差一行（即算术运算量为 $O ( n )$ )。由于有 $\scriptstyle n$ 次迭代，使用一维循环映射时，由进程空闲引起的累积开销仅为 $O ( n ^ { 2 } p )$ ，而使用块映射时的累积开销为 $\Theta ( n ^ { 3 } )$ （习题8.12）。

![](images/37ea51232b8017fa0d0829f75e59a96fac99eb65bd2c9c8da2d463e4279957c8.jpg)  
图8-9在 $k = 3$ 的高斯消元迭代中，对4个进程的 $8 \times 8$ 矩阵使用块和循环一维划分时不同进程上的计算负载

# 2.二维划分的并行实现

现在我们来介绍算法8-4的并行实现，其中 $n \times n$ 矩阵 $A$ 映射到这样一个 $P _ { i j }$ 进程的 $n \times n$ 进程格网，进程最初 $P _ { i , j }$ 存储 $A [ i , j ]$ 。图8-10举例说明 $n = 8$ 时与 $k = 3$ 对应的外层循环迭代中的计算与通信步骤。算法8-4、图8-5和8-10表示在外层循环的第 $k$ 次迭代中，进程 $P _ { k , k + 1 } , P _ { k , k + 2 } , \cdots ,$ $P _ { k , n - 1 }$ 需要用 $\textstyle A [ k , k ]$ 分别除 $A [ k , k + 1 ]$ ， $A [ k , k + 2 ]$ ，…， $A [ k , n - 1 ]$ 。在完成第6行的除法后，用第 $k$ 行修改后的元素对矩阵参与部分的所有其他各行执行消元步骤。类似地，用第 $k$ 列的元素对矩阵参与部分的所有其他各列执行消元步骤。如图8-10所示，第 $k$ 次迭代中的通信需要 $\textstyle A [ i , k ]$ 沿第衔进行一对多广播（图8-10a）， $k \leqslant i < n , A [ k , j ]$ 沿第j列进行一对多广播（图8-10c）， $k < j < n _ { \circ }$ 如果这些广播在所有的进程上同步进行，则与一维划分的情形一样，它也不是成本最优的并行公式（习题8.11）。

![](images/2734ca1727a303fb4d7d779fa665cf53ab2d0753f1c6b2f021d3e7351dc942e9.jpg)  
图8-10对于分配在逻辑二维格网上64个进程的 $8 \times 8$ 矩阵，与 $k = 3$ 对应的高斯消元法迭代的计算步骤

a）按行广播A[i,k], $( k { - } 1 ) < i < n$ b $) A [ k , j ] : = A [ k , j ] / A [ k , k ] , k < j < n$