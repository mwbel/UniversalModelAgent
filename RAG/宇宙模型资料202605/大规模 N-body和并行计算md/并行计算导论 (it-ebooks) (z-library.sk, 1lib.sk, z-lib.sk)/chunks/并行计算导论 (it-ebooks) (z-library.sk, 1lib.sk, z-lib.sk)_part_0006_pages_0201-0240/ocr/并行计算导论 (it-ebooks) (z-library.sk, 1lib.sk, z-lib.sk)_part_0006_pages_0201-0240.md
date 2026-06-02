$$
i = \{ \alpha _ { } 1 , \alpha _ { } 2 , \beta _ { } 1 \} .
$$

个数组以块的形式来分配矩阵A、 $B$ 以及结果矩阵 $C$ 。也就是说，如果每个矩阵的大小为 $n \times n$ ，进程的总数为 $p$ ，那么每个矩阵都被分成大小为 $n / \sqrt { p } \times n / \sqrt { p }$ （假设 $p$ 是完全平方数）的方块。对网格中的进程 $P _ { i , j }$ 分配每个矩阵的 $A _ { i , j }$ 、 $B _ { i , j }$ 和 $C _ { i , j }$ 块。经过初始的数据对齐后，算法将执行 $\sqrt { p }$ 步。在每一步中，每个进程都对本地可获得的矩阵A和 $B$ 中的块相乘，然后把A中的块送给左侧的进程， $B$ 中的块送给上面的进程。

程序6-2显示实现Cannon算法的MPI函数。矩阵的维数用参数 $\pmb { n }$ 提供。参数a、b、 $\pmb { \subset }$ 分别指向矩阵A、 $B$ 、 $C$ 中在本地存储的部分。数组的大小为 $n / \sqrt { p } \times n / \sqrt { p }$ ，其中 $p$ 是进程的数目。这个例行程序假设 $p$ 是完全平方数，且 $\pmb { n }$ 是 $\sqrt { p }$ 的整数倍数。参数comm存储描述进程的通信器，这些进程调用MatrixMatrixMultiply函数。本章中剩余的程序以函数的形式提供，而不用完全独立的程序形式。

1 MatrixMatrixMultiply(int n, double \*a， double \*b， double \*c,   
2 MPI_Comm comm)   
3 {   
4 int i;   
5 int nlocal;   
6 int npes, dims[2]， periods[2];   
7 int myrank,my2drank,mycoords [2]；   
8 int uprank, downrank， leftrank, rightrank, coords [2];   
9 int shiftsource, shiftdest;   
10 MPI_Status status;   
11 MPI_Comm comm_2d;   
12   
13 /\* Get the communicator related information \*/   
14 MPI_Comm_size(comm, &npes);   
15 MPI_Comm_rank(comm, &myrank）;   
16   
17 /\* Set up the Cartesian topology \*/   
18 dims[0] = dims[1] = sqrt(npes);   
19   
20 /\* Set the periods for wraparound connections \*/   
21 periods[0] = periods[1] = 1;   
22   
23 /\* Create the Cartesian topology, with rank reordering \*/   
24 MPI_Cart_create(comm，2，dims，periods，1，&comm_2d) :   
25   
26 /\* Get the rank and coordinates with respect to the new topology \*/   
27 MPI_Comm_rank(comm_2d, &my2drank) ;   
28 MPI_Cart_coords(comm_2d, my2drank，2, mycoords);   
29   
30 1\* Compute ranks of the up and left shifts \*/   
31 MPI_Cart_shift(comm_2d,0，-1, &rightrank,&leftrank);   
32 MPI_Cart_shift(comm_2d,i， -1, &downrank,&uprank);   
33   
34 /\* Determine the dimension of the local matrix block \*/   
35 nlocal $\mathbf { z }$ n/dims[0]:   
36   
37 /\* Perform the initial matrix alignment. First for A and then for B \*/   
38 MPI_Cart_shift(comm_2d,0, -mycoords[0]，&shiftsource,&shiftdest):   
39 MPI_Sendrecv_replace(a, nlocal\*nlocal, MPI_DoUBLE, shiftdest,   
40 1，shiftsource,1，comm_2d，&status):   
41   
42 MPI_Cart_shift(comm_2d,1， -mycoords[1]，&shiftsource，&shiftdest);   
43 MPI_Sendrecv_replace(b, nlocal\*nlocal, MPI_DOUBLE,   
44 shiftdest，i，shiftsource，1，comm_2d,&status);   
45   
46 17 /\* Get into the main computation loop \*/ for (i=0; i<dims[0); i++)   
18 MatrixMultiply(nlocal，a, b，c)； /\*c=c + a\*b\*/   
49   
50 /\* Shift matrix a left by one \*/   
51 MPI_Sendrecv_replace(a，nlocal\*nlocal，MPI_DoUBLE,   
52 leftrank，1，rightrank，1，comm_2d，&status);   
53   
54 /\* Shift matrix b up by one \*/   
55 MPI_Sendrecv_replace (b，nlocal\*nlocal， MPI_DoUBLE,   
56 uprank，1，downrank，1，comm_2d，&status);   
57   
58   
59 /\* Restore the original distribution of a and b \*/   
60 MPI_Cart_shift(comm_2d,0， $^ { + }$ mycoords[0]，&shiftsource，&shiftdest）;   
61 MPI_Sendrecv_replace(a，nlocal\*nlocal， MPI_DOUBLE,   
62 shiftdest，i，shiftsource，1，comm_2d,&status);   
63   
64 MPI_Cart_shift(comm_2d,1， $^ { + }$ mycoords[1]，&shiftsource，&shiftdest）;   
65 MPI_Sendrecv_replace(b，nlocal\*nlocal，MPI_DOUBLE,   
66 shiftdest，1，shiftsource，1，comm_2d，&status):   
67   
68 MPI_Comm_free(&comm_2d): /\* Free up communicator \*/   
69 ）   
70   
71 /\* This function performs a serial matrix-matrix multiplication $c = a ^ { \alpha } b$ \*/   
72 MatrixMultiply(int n, double $\yen 8$ ，double \*b，double $\yen 0$   
73   
74 inti，j、k;   
75   
76 for (i=0;i<n;i++)   
77 for (j=0:j<n;j++)   
78 for (k=0; k<n; k++)   
79 c[i\*n+j] += a{i\*n+k]\*b[k\*n+j];   
80

# 6.5计算与通信重

到目前为止，每当进行点对点通信时，我们开发的MPI程序都使用阻塞式发送和接收操作。前面已经讲过，阻塞式发送操作在消息从发送缓冲复制出之前一直阻塞着（无论是在源进程的系统缓冲还是发送到目标进程)。同样，阻塞式接收操作只有在消息接收完毕并复制到接收缓冲后才返回。例如，考虑程序6-2中Cannon的矩阵相乘算法。在主计算循环（47行至57行）的每一次迭代中，首先要计算存储在a和b中的子矩阵的矩阵相乘，然后用MPI_Sendrecv_replace交换a中的块和b中的块，这个操作在指定的矩阵块被相应的进程发送和接收前一直阻塞。在每一次迭代中，每个进程花费时间 ${ \cal O } ( n ^ { 3 } / p ^ { 1 . 5 } )$ 进行矩阵相乘，花费时间 $O ( n ^ { 2 } / p )$ 进行矩阵A和B的块交换。现在，由于矩阵A和 $\pmb { B }$ 中的块在处理器之间交换时并不改变，可以让矩阵和矩阵相乘的运算与这些块的传送重叠。许多新近的分布式内存并行计算机都有专门的通信控制器，能够执行消息传送操作而不需要CPU的干预。

# 无阻塞式通信操作

为了让计算与通信重叠，MPI提供一对执行无阻塞式发送和接收操作的函数。它们分别是MPI_Isend和MPI_Irecv。MPI_Isend开始一个发送操作，但不等它完成，也就是说，在数据复制出缓冲区前就返回。同样，MPI_Irecv开始一个接收操作，但在数据接收完毕并且复制到缓冲区前就返回。依靠相应的硬件支持，在两个函数返回前，消息的传送和接收就能和程序中的计算操作同时进行。

然而，在程序的后面部分，开始一个无阻塞式发送或接收操作的进程必须确保操作在计算前已经结束。这是因为，开始无阻塞式发送操作的进程可能需要覆盖存储待发送数据的缓冲区，或者开始无阻塞式接收操作的进程可能需要使用它请求的数据。为了检查无阻塞式发送和接收操作是否完成，MPI提供一对函数MPI_Test和MPI_Wait。前者检查无阻塞式操作是否已完成，后者等待（即阻塞）直到无阻塞式操作真正结束。

MPI_Isend和MPI_Irecv的调用序列如下:

int MPI_Isend(void \*buf， int count， MPI_Datatype datatype,int dest， int tag, MPI_Comm comm, MPI_Request \*request)  
int MPI_Irecv(void \*buf， int count， MPI_Datatype datatype,int source，int tag， MPI_Comm comm， MPI_Request \*request)

注意这两个函数与相应的阻塞式发送和接收函数有类似的参数。主要区别是这两个函数中多了参数request。MPI_Isend和MPI_Irecv函数分配一个请求(request)对象并返回一个指向request变量的指针。这个请求对象作为MPI_Test和MPI_Wait函数中的参数，用来确定那些我们需要查询其状态或等待其完成的操作。

注意，与阻塞式接收操作类似，MPI_Irecv函数不用status参数，但是与接收操作有关的状态信息通过MPI_Test和MPI_Wait函数返回。

int MPI_Test(MPI_Request \*request， int \*flag,MPI_Status \*status) int MPI_Wait(MPI_Request \*request， MPI_Status \*status)

MPI_Test测试由request确定的无阻塞式发送或接收操作是否已完成。如果已完成，则返回 $\mathtt { f } 1 \mathtt { a } \mathtt { g } = \{ \mathtt { t r u e } \}$ （在C语言中的非0值)，否则返回{false}（C语言中的0值)。在无阻塞式操作完成后，由变量request指向的请求对象被解除分配，request被设置为MPI_REQUEST_NULL。同时status对象被设置为包含与操作有关的信息。如果操作未完成，request就不被修改，status对象中的值是未定义的。MPI_Wait函数在由request确定的无阻塞式操作完成前一直阻塞。在这种情况下，它解除分配request对象，将其设置为MPI_REQUEST_NULL，并在status对象中返回有关已完成操作的信息。

对于程序员想要显式解除分配一个请求对象的情况，MPI提供下述函数：

int MPI_Request_free(MPI_Request \*request)

注意，请求对象的解除分配对相关的无阻塞式发送和接收操作没有任何影响。也就是说，如果这些操作未完成，它们会继续进行直至完成。因此，一定要小心地对请求对象进行显式解除分配，因为没有请求对象就不能测试无阻塞式操作是否已完成。

无阻塞式通信操作可以和相应的阻塞式操作相匹配。例如，进程可以用无阻塞式发送操作发送消息，此消息可以由其他进程用阻塞式接收操作接收。

避免死锁使用无阻塞式通信操作可以除去绝大多数与阻塞式通信操作相关的死锁。例如，我们在6.3节讨论过，下面的代码是不安全的。

1 int a[10]，b[10]，myrank;  
2 MPI_Status status;  
3  
4 MPI_Comm_rank(MPI_COMM_WORLD，&myrank） ;  
5 if (myrank == 0）{  
6 MPI_Send(a，10，MPI_INT，1，1，MPI_COMM_WORLD):  
7 MPI_Send(b，10，MPI_INT，1，2，MPI_COMM_WORLD);  
8 ）  
9 else if (myrank $\ = \texttt { \textbf { 1 } }$ ）{  
10 MPI_Recv(b，10，MPI_INT，0，2，&status，MPI_COMM_WORLD) :  
1 MPI_RecV(a，10，MPI_INT，0，1，&status，MPI_COMM_WORLD);  
12  
13

然而，如果将发送和接收操作中的任一个用它们对应的无阻塞式操作代替，代码就将是安全的，并可以在任何MPI实现上正确运行。

1 int a[10]，b[10]，myrank;  
2 MPI_Status status;  
3 MPI_Request requests [2] ;  
4  
5 MPI_Comm_rank(MPI_COMM_WORLD，&myrank）;  
6 if (myrank $\qquad = \bullet \quad 0$ ）  
7 MPI_Send(a，10、MPI_INT，1，1，MPI_COMM_WORLD);  
8 MPI_Send(b，10，MPI_INT，1，2，MPI_COMM_WORLD);  
9  
10 else if (myrank $\mathbf { \lambda } = \mathbf { \lambda } \mathbf { 1 }$ ）{  
1 MPI_Irecv(b, 10, MPI_INT，0， 2，&requests[0], MPI_COMM_WORLD);  
12 MPI_IreCv(a，10，MPI_INT，0，1，&requests[1]， MPI_COMM_WORLD);  
13  
14

这个例子也说明，由任意进程启动的无阻塞式操作，可以按相应消息的传送或接收所确定的任意顺序完成。例如，第二个接收操作将在第一个之前完成。

# 实例：Cannon的矩阵与矩阵相乘（使用无阻塞式操作）

程序6-3显示用无阻塞式发送和接收操作实现的Cannon算法的MPI程序，其中的参数与程序6-2中的相同。

1 MatrixMatrixMultiply_NonBlocking(int n, double \*a， double \*b, 2 double \*c，MPI_Comm comm) 3 { 4 int i，j，nlocal; 5 double \*a_buffers[2]，\*b_buffers[2] : 6 int npes,dims[2]，periods[2]; 7 int myrank， my2drank， mycoords {2] ; 8 int uprank， dowmrank， leftrank,rightrank， coords[2]; 9 int shiftsource, shiftdest; 10 MPI_Status status; 11 MPI_Comm comm_2d: 12 MPI_Request reqs [4]: 13 14 /\* Get the communicator related information \*/ 15 MPI_Comm_size(comm,&npes) ; 16 MPI_Comm_rank(comm，&myrank） ; 17 18 /\* Set up the Cartesian topology \*/ 19 dims [0] $\eqcirc$ dims[1] sqrt(npes); 20 21 /\* Set the periods for wraparound connections \*/ 22 periods[0] $\eqcirc$ periods[1] = 1; 23 24 /\* Create the Cartesian topology, with rank reordering \*/ 25 MPI_Cart_create(comm，2，dims，periods，1，&comm_2d) : 26 27 /\* Get the rank and coordinates with respect to the new topology \*/ 28 MPI_Comm_rank(comm_2d, &my2drank) ; 29 MPI_Cart_coords(comm_2d, my2drank,2， mycoords); 30 31 1\* Compute ranks of the up and left shifts \*/ 32 MPI_Cart_shift(comm_2d,0,-1，&rightrank，&leftrank); 33 MPI Cart shift(comm 2d，1， -1，&downrank,&uprank);

34   
35 /\*Determine the dimension of the local matrix block \*/   
36 nlocal $\approx$ n/dims[0];   
37   
38 /\* Setup the a_buffers and b_buffers arrays \*/   
39 a_buffers[0] $\eqcirc$ a；   
40 a_buffers[1] $\eqsim$ (double \*) malloc(nlocal\*nlocal\*sizeof(double)) ;   
41 b_buffers[0] $= 6$ ；   
42 bbuffers[1] $\mathbf { \equiv }$ (double $^ { * }$ )malloc(nlocal\*nlocal\*sizeof (double));   
43   
44 /\* Perform the initial matrix alignment. First for A and then for $B ^ { \star } /$   
45 MPI_Cart_shift(comm_2d, 0, -mycoords[0l, &shiftsource,&shiftdest);   
46 MPI_Sendrecv_replace(a_buffersl0l, nlocal\*nlocal, MPI_DOUBLE,   
47 shiftdest，i， shiftsource，1，comm_2d,&status);   
48   
49 MPI_Cart_shift(comm_2d, 1, -mycoords[1], &shiftsource,&shiftdest):   
50 MPI_Sendrecv_replace(b_buffers[0l, nlocal\*nlocal,MPI_DOUBLE,   
51 shiftdest，i，shiftsource,1，comm_2d，&status);   
52   
53 /\* Get into the main computation loop \*/   
54 for $\dot { \bf 1 } = 0$ ；i<dims[0]； i++）{   
55 MPI_Isend(a_buffers[i%2]，nlocal\*nlocal, MPI_DOUBLE,   
56 1eftrank,1，comm_2d,&reqs[01）；   
MPI_Isend(b_buffers[i82], nlocal\*nlocal，MPI_DOUBLE,   
58 uprank，1,comm_2d,&reqs[1]）；   
59 MPI_Irecv(a_buffers[(i+1)&2),nlocal\*nlocal, MPI_DOUBLE,   
60 rightrank,1， comm_2d,&reqs[2]);   
61 MPI_Irecv(b_buffers[(i+1)s2],nlocal\*nlocal, MPI_DOUBLE,   
62 downrank，1，comm_2d，&reqs[3]）;   
63   
64 /\*c = c + a\*b \*/   
65 MatrixMuitiply(nlocal, a_bufferslis2], b_buffers[i&2], c);   
66   
67 for_(j=0; j<4; j++)   
68 MPI_Wait(&reqs[j],&status):   
69 ）   
70   
71 /\* Restore the original distribution of a and b \*/   
72 MPI_Cart_shift(comm_2d,0. +mycoordsl0]， &shiftsource, &shiftdest);   
73 MPI_Sendrecv_replace(a_buffers [i82]， nlocal\*nlocal, MPI_DoUBLE,   
74 shiftdest,i, shiftsource,1， comm_2d,&status);   
75   
76 MPI_Cart_shift(comm_2d,1， +mycoords[1],&shiftsource, &shiftdest);   
77 MPI_Sendrecv_replace(b_buffers [i&2], nlocal\*nlocal, MPI_DOUBLE,   
78 shiftdest，i,shiftsource，1，comm_2d,&status);   
79   
80 MPI_Comm_free(&comm_2d): /\* Free up communicator \*/   
81   
82 free(a_buffers[1]);   
83 free(b_buffers1l）;   
84 ！

阻塞式程序（程序6-2）与这个无阻塞式程序之间有两个主要区别。第一个区别是，无阻塞式程序需要使用另两个数组a_buffers和b_buffers，它们作为块A和块B的缓冲区，在执行涉及前面块的计算进行时被接收。第二个区别是，在主计算循环，无阻塞式程序首先启动无阻塞式发送操作，将本地存储的块A和块B发送到网格左边和上边的进程，然后启动无阻塞式接收操作，接收下一次迭代来的网格右边和下边进程的块。在启动这4个无阻塞式操作后，继续进行当前存储块的矩阵与矩阵相乘。最后，在进行下一次迭代前，使用MPI_Wait等待发送和接收操作完成。

注意，为了让计算与通信重叠，我们必需使用两个辅助数组 —一个用于A，一个用于B。这是为了保证到来的消息不覆盖在计算中使用的块A和块B，计算与数据传送是并发进行的。

这样，性能的提高（通过计算与通信重叠）以增加内存需求为代价。这是消息传递程序中经常作出的一种折中，因为对于低耦合分布式内存的并行计算机而言，通信开销非常大。

# 6.6聚合的通信和计算操作

MPI提供了大量的函数，用来进行许多常用的聚合通信操作。特别，MPI支持第4章讲到的绝大多数基本通信操作。所有MPI提供的聚合通信函数以通信器作为参数，通信器定义参与聚合操作的一组进程。属于通信器的所有进程都参与到操作中，并且都必需调用聚合通信函数。虽然聚合通信操作不像障碍那样工作（即处理器可能跳过对聚合通信操作的调用，即使在其他的进程到达它之前)，但它像下述意义下的虚拟同步：即使在聚合调用前或者聚合调用后进行了一次全局同步操作，并行程序也应该正确运行。由于操作是虚拟同步的，操作不需要标志。在一些聚合函数中，要求数据从单个进程（源进程）发送，或者由单个进程（目标进程）接收。在这些函数中，源进程或目标进程是对例行程序提供的参数之一。所有组内（即通信器）的进程必须指定相同的源进程或目标进程。对于绝大多数聚合通信操作，MPI提供两个不同的变体，一个用来在每个进程间传送同样大小的数据，另一个传送的数据大小可以不同。

# 6.6.1障碍

在MPI中，障碍同步操作用MPI_Barrier函数实现。

int MPI_Barrier(MPI_Comm comm)

MPI_Barrier函数中只有通信器一个参数，它定义被同步的进程组。对MPI_Barrier的调用只有在组中的所有进程调用了这个函数后才返回。

# 6.6.2广播

4.1节中讲过的一对多广播操作在MPI中用MPI_Bcast函数实现。

int MPI_Bcast(void \*buf， int count， MPI_Datatype datatype,int source，MPI_Comm comm)

MPI_Bcast将存储在进程source的缓冲区buf中的数据发送到组中所有其他的进程。每个进程接收到的数据都存储在缓冲区buf中。被广播的数据中，类型为datatype的数据有count项。由source进程发送的数据量必需等于每个进程要接收的数据量，也就是说，在所有的进程中，count和datatype字段必需匹配。

# 6.6.3归约

4.1节中讲过的多对一归约操作在MPI函数中用MPI_Reduce函数实现。

int MPI_Reduce(void \*sendbuf，void \*recvbuf， int count,MPI_Datatype datatype，MPI_Op op，int target,MPI_Comm comm)

MPI_Reduce函数使用由op指定的操作符将组内每个进程中存储于缓冲区sendbuf的元素组合起来，并用等级为target的进程中的缓冲区recvbuf返回组合后的值。sendbuf和recvbuf中类型为datatype的数据项数目都必需为count。注意，所有的进程都必需提供

$$
\begin{array} { r } { \mathcal { S } _ { \lambda } : = : \mathcal { S } _ { \lambda } ( \mathbf { x } _ { \lambda } ) , \quad \mathcal { S } _ { \lambda } : = : \mathcal { S } _ { \lambda } ( \mathbf { x } _ { \lambda } ) , } \end{array}
$$

一个recvbuf数组，即使这些进程不是归约操作的目标（target)。当count大于1时，组合操作按序列中的每个数据项的逐个进行。所有的进程都必需以同样的count、datatype、op、target和comm调用MPI_Reduce。

MPI提供一系列预定义的操作，可以用于对存储于sendbuf中的元素进行组合。MPI也允许程序员自己定义操作，但本书不讨论这一点。表6-3列出了预定义的操作。例如，为了计算存储在sendbuf中的元素的最大值，op参数的值就必需为 $\mathbf { M P I \_ M A X }$ 。并非表中所有的操作都能应用于MPI支持的所有可能的数据类型。例如，按位或操作（即 ${ \tt O P } = { \tt M P I } \_ { { \tt B O R } } )$ 对实型的数据就没有定义，如MPI_FLOAT和MPI_REAL。表6-3中的最后一列显示可以用于每个操作的不同数据类型。

表6-3预定义的归约操作  

<table><tr><td>操作</td><td>含义</td><td>数据类型</td></tr><tr><td>MPI_MAX</td><td>最大值</td><td>C整型及浮点型</td></tr><tr><td>MPI_MIN</td><td>最小值</td><td>C整型及浮点型</td></tr><tr><td>MPI_SUM</td><td>求和</td><td>C整型及浮点型</td></tr><tr><td>MPI_PROD</td><td>求积</td><td>C整型及浮点型</td></tr><tr><td>MPI_LAND</td><td>逻辑与</td><td>C整型</td></tr><tr><td>MPI_BAND</td><td>按位与</td><td>C整型及字节型</td></tr><tr><td>MPI_LOR</td><td>逻辑或</td><td>C整型</td></tr><tr><td>MPI_BOR</td><td>按位或</td><td>C整型及字节型</td></tr><tr><td>MPI_LXOR</td><td>逻辑异或</td><td>C整型</td></tr><tr><td>MPI_BXOR</td><td>按位异或</td><td>C整型及字节型</td></tr><tr><td>MPI_MAXLOC</td><td>最大-最小值单元</td><td>数据对</td></tr><tr><td>MPI_MINLOC</td><td>最小-最小值单元</td><td>数据对</td></tr></table>

MPI_MAXLOC操作对数值对 $( \nu _ { i } , l _ { i } )$ 进行组合，并返回数值对 $( \nu , l )$ ，其中 $\nu$ 是所有 $\nu _ { i }$ 中的最大值， $l$ 是当 $\nu = \nu _ { i }$ 时所有 $l _ { i }$ 中的最小值。同样，MPI_MINLOC操作对数值对进行组合，并返回数值 $( \nu , l )$ 对，其中 $\pmb { \nu }$ 是所有 $v _ { j }$ 中的最小值，是当 $\nu = \nu _ { i }$ 时所有 $l _ { i }$ 中的最小值。MPI_MAXLOC和MPI_MINLOC可以用来计算位于不同进程中的一系列数的最大值或最小值，并求出存储最大值或最小值的第一个进程，如图6-6所示。由于MPI_MAXLOC和MPI_MINLOC需要成对的数据，MPI又定义了一组新的数据类型，如表6-4所示。在C语言中，这些数据类型是用包含相应类型的结构实现的。

![](images/b3bdab199b40526ebe7189c968b28d056bef70ba2959361a00e6a2250f9286fe.jpg)  
图6-6一个使用MPI_MINLOC和MPI_MAXLOC操作符的例子

如果所有的进程都需要归约操作的结果，则可使用MPI提供的MPI_Allreduce操作。这个函数提供4.3节讲述的全归约操作的功能。

int MPI_Allreduce(void \*sendbuf，void \*recvbuf， int count,MPI_Datatype datatype， MPI_Op op，MPI_Comm comm)注意，由于所有的进程都接收归约操作的结果，此函数中不含target参数。

表6-4用于MPI_MAXLOC和MPI_MINLOC归约操作的MPI数据对数据类型  

<table><tr><td>MPI数据类型</td><td>C数据类型</td></tr><tr><td>MPI_2INT</td><td>int对</td></tr><tr><td>MPI_SHORT_INT</td><td>short和int</td></tr><tr><td>MPI_LONG_INT</td><td>long和int</td></tr><tr><td>MPI_LONG_DOUBLE__INT</td><td>long double和int</td></tr><tr><td>MPI_FLOAT_INT</td><td>float和int</td></tr><tr><td>MPI_DOUBLE_INT</td><td>double和int</td></tr></table>

# 6.6.4前缀

4.3节讲述的前缀和操作在MPI中用MPI_Scan函数实现。

int MPI_Scan(void \*sendbuf， void \*recvbuf， int count,MPI_Datatype datatype， MPI_Op op， MPI_Comm comm)

MPI_Scan对存储在每个进程的缓冲区sendbuf中的数据进行前缀归约，并在缓冲区revcbuf中返回结果。在归约操作的最后，等级为i的进程的接收缓冲区，将存储等级由0到i（包括i）的进程的发送缓冲区中的归约结果。MPI_Scan支持的操作类型（即op）以及对函数中不同变量的限制，都与MPI_Reduce归约操作相同。

# 6.6.5收

4.4节讲述的收集操作在MPI中用MPI_Gather函数实现。

int MPI_Gather(void \*sendbuf， int sendcount,MPI_Datatype senddatatype， void \*recvbuf， int recvcount,MPI_Datatype recvdatatype， int target， MPI_Comm comm)

每个进程（包括target进程）将存储在数组sendbuf中的数据发送给target进程。结果，如果p是通信comm中处理器的数目，则目标进程将接收的缓冲区总数为p。数据按等级颂序存储在目标进程的recvbuf数组中。就是说，来自等级为的进程的数据存储在recvbuf中，起始单元为i\*sendcount（假设数组recvbuf与recvdatatype的类型相同）。

每个进程发送的数据必需具有相同的类型和大小，即调用MPI_Gather时，参数sendcount和senddatatype必需在每个进程中具有同样的值。只有目标进程需要知道有关接收缓存的信息，如接收缓存的长度及类型，而其他所有进程都忽咯这些信息。参数recvcount指定每个进程接收的元素数目而不是接收的元素总数目。所以，recvcount必需和sendcount相同，这两者的类型也必需匹配。

MPI还提供MPI_A1lgather函数，它为所有的进程收集数据而不是仅给目标进程。

int MPI_Allgather(void \*sendbuf， int sendcount,MPI_Datatype senddatatype， void \*recvbuf， int recvcount,MPI_Datatype recvdatatype， MPI_Comm comm)

其中各个参数的含义与函数MPI_Gather中的相似；但是，每个进程都必需提供一个recvbuf数组来存储收集的数据。

上面提到的收集操作中，每个进程发送的数组大小都相等，此外，MPI还提供了数组大小可以不等的收集操作，MPI称这种操作为向量（vector）变体。MPI_Gather和MPI_Allgather操作的向量变体分别由函数MPI_Gatherv和MPI_Allgatherv提供。

int MPI_Gatherv(void \*sendbuf， int sendcount,MPI_Datatype senddatatype， void \*recvbuf,int \*recvcounts，int \*displs,MPI_Datatype recvdatatype， int target， MPI_Comm comm)

int MPI_Allgatherv(void \*sendbuf, int sendcount，MPI_Datatype senddatatype, void \*recvbuf,int \*recvcounts， int \*displs， MPI_Datatype recvdatatype,MPI_Comm comm)

将recvcount参数用数组recvcounts代替，这两个函数就能使每个进程发送不同数量的数据元素。进程i发送的数据量等于recvcounts[i]。注意Recvcounts与通信器comm的大小相等。数组参数displs的大小也和它们相等。displs用来确定由每个进程发送出的数据存储于revcbuf中的位置。特别，由进程i发送出的数据存储于recvbuf中起始单元为displs[i]的地方。注意与非向量变体相反，对于不同的进程，参数sendcount也可以不同。

# 6.6.6散发

4.4节讲到的散发操作在MPI中用MPI_Scatter函数实现。

int MPI_Scatter(void \*sendbuf，int sendcount,MPI_Datatype senddatatype， void \*recvbuf， int recvcount,MPI_Datatype recvdatatype， int source， MPI_Comm comm)

源进程将发送缓冲sendbuf中的不同部分发送给每个进程，也包括它自身。接收到的数据存储于recvbuf中。进程i接收sendcount个类型为senddatatype连续的元素，这些元素从源进程中缓冲区sendbuf的i \*sendcount单元开始（假设sendbuf与senddatatype的类型相同）。所有进程调用MPI_Scatter时，都必须使用同样值的sendcount、senddatatype、recvcount、recvdatatype、source以及comm参数。再次注意,sendcount是发送到每一个进程的元素数目。

与收集操作类似，MPI提供散发操作的向量变体，称为MPI_Scatterv，它允许将不同数量的数据发送给不同的进程。

int MPI_Scatterv(void \*sendbuf， int \*sendcounts，int \*displs,MPI_Datatype senddatatype， void \*recvbuf， int recvcount,MPI_Datatype recvdatatype，int source，MPI_Comm comm)

从上面的函数可以看出，数组sendcounts代替了参数sendcount，该数组确定发送给每个进程的元素数目。特别地，target进程发送sendcounts[i]个元素给进程i。同样，数组displs用来确定这些元素从sendbuf的何处发送出。特别，如果sendbuf和senddatatype的类型相同，那么发送到进程的数据起始于数组sendbuf的displs[i]处。

数组sendcounts和displs的大小与通信器中的进程数目相等。注意如果适当地设置displs数组，就能用MPI_Scatterv发送sendbuf中的重叠区域。

# 6.6.7多对多

4.5节中讲过的多对多私自通信操作在MPI中用MPI_Alltoal1函数实现。

int MPI_Alltoall(void \*sendbuf， int sendcount,MPI_Datatype senddatatype，void \*recvbuf， int recvcount,MPI_Datatype recvdatatype， MPI_Comm comm)

每个进程发送数组sendbuf中的不同部分给其他每个进程，包括它自身。每个进程发送给进程isendcount个类型为senddatatype连续的元素，这些元素从它的sendbuf数组中i\*sendcount单元开始。接收到的数据存储于数组recvbuf中。每个进程从进程i接收recvcount个类型为recvdatatype的元素，并将这些元素存储在recvbuf数组中从i\*sendcount开始的单元。所有进程调用MPI_Alltoall时；必须使用同样值的sendcount、senddatatype、recvcount、recvdatatype以及comm参数。注意,sendcount和recvcount是发送到每个进程以及从每个进程接收到的元素数目。

对于多对多私自通信操作，MPI也提供一个向量变体MPI_Alltoal1v，它允许每个进程发送或接收不同数量的数据。

int MPI_Alltoallv(void \*sendbuf, int \*sendcounts, int \*sdisplsMPI_Datatype senddatatype， void \*recvbuf， int \*recvcounts,int \*rdispls， MPI_Datatype recvdatatype， MPI_Comm comm)

参数sendcounts用来指定发送到每个进程的元素数目，而参数sdispls用来指定这些元素在sendbuf中存储的位置。特别，每个进程发送给进程isendcounts[i]个连续的元素，从数组sendbuf的sdispls[i]单元开始。参数recvcounts用来指定每个进程接收的元素数目，而参数rdispls用来指定这些元素存储在recvbuf中的位置。特别，每个进程从进程i接收recvcounts[i]个元素，这些元素存储在recvbuf中连续的单元，从rdispls[i]单元开始。所有进程调用MPI_A11toal1v时，必须使用同样值的senddatatype、recvdatatype以及comm参数。

# 6.6.8实例：一维矩阵与向口相乘

我们第一个使用聚合通信的消息传递程序是将稠密n×n矩阵A与向量b相乘，即x=Ab。如8.1节中的讨论，一种并行执行这种乘法的方法是让每个进程计算乘积向量x的不同部分。特别，p个进程中的每一个计算x中n/p个连续的元素。这个算法可通过将矩阵A按行分配用MPI实现，每个进程接收n/p个行，与进程计算的乘积向量x中的部分相对应。向量b也以与x类似的方式分配。

程序6-4显示按行分配矩阵A的MPI程序。矩阵的维数用参数n给出，参数a和参数b分别指向矩阵A和向量b中本地存储的部分，而参数x指向输出的矩阵与向量乘积的本地部分。这个程序假设 $n$ 是处理器数目的整数倍。

计算x的另一种方法是将对x中每个元素进行点乘的任务并行化。也就是说，对于向量x中的每个元素xi，所有进程都计算一部分，将部分的点乘结果相加得到最终结果。这个算法可通过将矩阵A按列方式分配用MPI实现。每个进程得到矩阵 $A$ 中 $n / p$ 个连续的列，以及向量 $b$ 中与这些列相对应的元素。此外，计算结束后我们将乘积向量 $x$ 按与向量 $b$ 类似的方式分配。程序6-5显示这种按列分配矩阵的MPI程序。

1 RowMatrixVectorMultiply(int n，double \*a，double \*b，double \*x, 2 MPI_Comm comm) 3 { 4 int i，j; 5 int nlocal; /\* Number of locally stored rows of A \*/ 6 double \*fb; /\* Will point to a buffer that stores the entire vector b \*/ 7 int npes,myrank; 8 MPI_Status status; 9 10 /\* Get information about the communicator \*/ 11 MPI_Comm_size(comm,&npes); 12 MPI_Comm_rank(comm，&myrank) ; 13 14 /\* Allocate the memory that will store the entire vector b \*/ 15 fb = (double \*)malloc(n\*sizeof (double)) : 16 17 nlocal = n/npes; 18 19 /\* Gather the entire vector b on each processor using MPI's ALLGATHER operation \*/ 20 MPI_Allgather(b，nlocal，MPI_DOUBLE，fb，nlocal，MPI_DOUBLE， 21 comm) : 22 23 /\*Perform the matrix-vector multiplication involving the locally stored submatrix \*/ 24 for $\mathbf { i } = 0$ : i<nlocal; i++) { 25 $\mathbf { x } \left\{ \mathbf { i } \right\} \ \textbf { \asymp } \ 0 \mathrm { . 0 } \mathrm { ~ } ,$ 26 for (j=0; j<n; j++) 27 xli] += a[i\*n+j]\*fb[j]; 28 29 30 free(fb); 31

# 程序6-5按列的矩阵与向口相

1 ColMatrixvectorMultiply(int n, double \*a, double \*b, double \*x, 2 MPI_Comm comm) 3 { 4 int i,j； 5 int nlocal; 6 double \*px; 7 double \*fx: 8 int npes, myrank; 9 MPI_Status status; 10 11 /\* Get identity and size information from the communicator \*/ 12 MPI_Comm_size(comm,&npes) : 13 MPI_Comm_rank (comm, &myrank) ; 14 15 nlocal = n/npes: 16 17 /\* Allocate memory for arrays storing intermediate results. \*/ 18 px = (double \*) malloc(n\*sizeof (double)) : 19 fx = (double \*)malloc(n\*sizeof(double)): 20 21 /\* Compute the partial-dot products that correspond to the local columns of A. \*/ 22 for (i=0: i<n; i++){ 23 $\mathbf { p x } \left[ \mathbf { i } \right] = 0 , 0 ,$ 24 for (j=0: j<nlocal; j++) 25 pxlil += ali\*nlocal+i1\*blil:

26 1   
27   
28 /\* Sum-up the results by performing an element-wise reduction operation \*/   
29 MPI_Reduce(px，fx，n，MPI_DOUBLE，MPI_SUM，0，comm);   
30   
31 /\* Redistribute fx in a fashion similar to that of vector b \*/   
32 MPI_Scatter(fx， nlocal，MPI_DOUBLE，x， nlocal, MPI_DOUBLE，0,   
33 comm） ;   
34   
35 free(px):free(fx);   
36

比较上面两个矩阵向量相乘的程序可以发现，按行的程序只需要进行一次MPI_Allgather操作，而按列的程序需要进行一次MPI_Reduce和MPI_Scatter操作。通常，按行序分配更好，因为它造成的通信开销较小（见习题6.6)。但是，在许多时候，程序不仅要计算 $\pmb { A x }$ ，还要计算 $A ^ { T } x$ 。在这种情况下，按行分配可用来计算 $\pmb { A } \pmb { x }$ ，但计算 $\pmb { A } ^ { \tau _ { x } }$ 则需要按列分配（对A的按行分配是 $\pmb { A }$ 的转置 $A ^ { T }$ 的按列分配)。使用按列分配的程序，要比先转置矩阵再用按行分配的程序简便得多。使用全聚集（all-gather）操作的对偶操作，就能使使用按列分配的程序与使用按行分配的程序运行得一样快（见习题6.7)。但是，MPI中没有提供这种对偶操作。

# 6.6.9实例：单源最短路径

我们的第二个使用聚合通信操作的消息传递程序是计算图中从源顶点s到其他所有顶点的最短路径，程序使用10.3节中描述的Dijkstra的单源最短路径算法。程序6-6为这个程序的代码。

参数n存储图中的顶点总数，参数source存储计算单源最短路径的源顶点，参数wgt指向图的加权邻接矩阵的本地存储部分。参数lengths指向一个向量，该向量将用来存储从源顶点到本地存储顶点的最短路径。最后，参数comm是将被MPI例行程序使用的通信器。注意这个例行程序假设顶点数目是处理器数目的整数倍。

程序6-6 Dijkstra的单源短路径   

<table><tr><td>1 2 { 3 4 5 6</td><td>SingleSource(int n， int source， int *wgt， int *lengths, MPI_Comm comm) int i,j; int nlocal : /* The number of vertices stored locally */ int *marker : /* Used to mark the vertices belonging to Vo */ int firstvtx: /* The index number of the first vertex that is stored locally */ 7 int last vtx: /* The index number of the last vertex that is stored locally */ 8 int u,udist; 9 int lminpair[2]，gminpair[2]; 10 int npes，myrank;</td></tr></table>

24 /\* This array is used to indicate $i f$ the shortest part to a vertex has been found or not. \*/   
25 /\*if marker[u] is one, then the shortest path to ${ \pmb v }$ has been found, otherwise it has not. \*/   
26 marker $\approx$ (int $\ast 1$ malloc(nlocal\*sizeof(int));   
27 for $\dot { 1 } \dot { 2 } = 0$ : j<nlocal; ${ \dot { \mathsf { J } } } + + { \dot { \mathsf { I } } }$ ）   
28 marker[j] = 1;   
29   
30 /\*The process that stores the source vertex, marks it as being seen \*/   
31 if (source $> =$ firstvtx && source $< =$ lastvtx)   
32 marker [source-firstvtx] $\qquad = \ 0$   
33   
34 /\*The main loop of Dijkstra's algorithm $^ { \star } /$   
35 for( ${ \dot { \bf 1 } } = { \bf 1 }$ ；i<n;i++）{   
36 /\* Step 1: Find the local vertex that is at the smallest distance from source \*/   
37 1minpai $\pmb { \mathrm { \check { x } } }$ [0] $\ncong$ MAXINT; /\* set it to an architecture dependent large number \*/   
38 lminpair[1] = -1;   
39 for $\dot { \ b ] } = 0$ : j<nlocal； j++）{   
40 if (marker[j] && lengths[j] < lminpair[0]）{   
41 lminpair[0] $\mathbf { \delta m }$ lengthslj]:   
42 1minpair[1] $\mathbf { \beta } =$ firstvtx+j:   
43   
44   
45   
46 /\* Step 2: Compute the global minimum vertex, and insert it into $\pmb { V _ { c } }$ \*/   
47 MPI_Allreduce(lminpair，gminpair，1，MPI_2INT,MPI_MINLOC,   
48 comm) ;   
49 udist gminpair[0];   
50 u = gminpair[1];   
51   
52 /\* The process that stores the minimum vertex, marks it as being seen \*/   
53 if $u =$ lminpair[1]）   
54 marker[u-firstvtx] = 0;   
55   
56 /\* Step 3: Update the distances given that u got inserted \*/   
57 for (j=0; j<nlocal； j++){   
58 if(marker[j] && udist $\star$ wgt[u\*nlocal+j] < lengths[j]）   
59 lengths[j] udist $^ { + }$ wgt[u\*nlocal+j] ;   
60 1   
61   
62   
63 free(marker) :   
64 ！

Dijkstra的并行单源最短路径算法的主计算循环要分三步执行。第一步，每个进程寻找 $V _ { o }$ 中本地存储的与源点距离最短的顶点；第二步，确定在所有进程中距离最短的顶点，该顶点包含在V.中；第三步，所有的进程更新它们的距离数组以反映出 $V _ { c }$ 中加入了新的顶点。

第一步的实现需要扫描 $V _ { o }$ 中本地存储的顶点，并确定具有更小lengths[v]值的顶点 $\nu$ 。计算结果存储于数组lminpair中。特别地，lminpair[0]存储顶点的距离，lminpair[1]存储顶点自身。使用这种存储方案的原因在我们考虑下一步时就会清楚，那时必需计算所有顶点中离源点最短的顶点。通过对存储在lminpair[O]中的距离值进行一次最小归约，就能计算出最短距离。然而，除了求出最短距离外，还要求出处于最短距离的顶点。因此，最适合的归约操作是MPI_MINLOC，因为它不但返回最小值，还返回与最小值相对应的下标值。因为MPI_MINLOC，我们使用二元素数组lminpair来存储距离以及达到这个距离的顶点。此外，由于所有进程都需要归约操作的结果来进行第三步，我们使用MPI_Allreduce来执行归约操作。归约操作的结果在数组gminpair中返回。在每次迭代中，第三步和最后一步通过扫描属于V,的本地顶点并更新这些顶点离源顶点的最短距离来实现。

避免负载不平衡程序6-6分配W的n/p个连续列给每个处理器，在每次迭代中，程序使用MPI_MINLOC归约操作选出顶点 $\nu$ 包含到 $V _ { c }$ 中。对于操作数 $( a , i )$ 和 $( a , j )$ ，回顾MPI_MINLOC将返回下标较小的一个（因为两者的值相同)。因此，对于离源顶点同样近的顶点，这有利于编号较小的顶点。这可能导致负载不平衡，因为存储在低等级进程中的顶点会比存储在高等级进程中的顶点更快地包含到 $V _ { c }$ 中（特别当 $V _ { o }$ 中的多个顶点到源顶点的最小距离相同时）。因此集合 $V _ { \prime \prime }$ 的大小在较高等级的进程中会较大，在整体运行时间中占支配地位。

改正这个问题的一个方法是，将W列按循环的方式分配。在这种分配方式中，进程i得到从顶点i开始的每个第 $p$ 顶点。这个方案也分配 $n / p$ 个顶点给每个进程，但是这些进程的下标跨越几乎整个图。因此，MPI_MINLOC有利于较小编号的顶点不会导致负载不平衡。

# 6.6.10实例：样本排序

下面再看最后一个使用聚合通信的程序，将 $\pmb { n }$ 个元素的序列A用将在9.5节讲述的样本排序算法进行排序。程序6-7是该程序的代码。

SampleSort函数将存储在每个进程中的元素序列作为输人，并返回指向一个数组的指针，该数组存储排序的序列以及序列中元素的数目。SampleSort函数的元素是整型的，且按增序排序。参数n指定待排序的元素的总数目；参数elmnts指定一个指针，指向存储这些元素的本地部分的数组。返回时，参数nsorted将存储返回的排序的数组中的元素个数。这个例行程序假设n是进程数目的整数倍。

1 int \*Samplesort(int n， int \*elmnts， int \*nsorted, MPI_Comm comm) 2 { 3 int i，j，nlocal，npes,myrank; 4 int \*sorted_elmnts,\*splittere, \*allpicks; 5 int \*scour.ts， \*sdispls， \*rcounts， \*rdispls; 6 7 /\* Get communicator-related information \*/ 8 MPI_Comm_size(comm,&npes); 9 MPI_Comm_rank(comm，&myrank） ; 10 11 nlocal $\Bumpeq$ n/npes: 12 13 /\* Allocate memory for the arrays that willstore the splitters \*/ 14 splitters $\Bumpeq$ (int $\ast$ )malioc(npes\*sizeof(int)); 15 allpicks $=$ (int $\pmb { * }$ )malloc(npes\*(npes-1)\*sizeof (int)); 16 17 /\* Sort local array \*/ 18 qsort(elmnts，nlocal，sizeof(int)，IncOrder); 19 20 /\* Select local npes-1 equally spaced elements \*/ 21 for $\mathbf { i } = \mathbf { 1 }$ ; i<npes; $\dot { \bf 1 } + + 1$ 22 splitters[i-1] $\mathbf { \eqcirc }$ elmnts[i\*nlocal/npes]: 23 24 /\* Gather the samples in the processors $\$ 7$ 25 MPI_Allgather(splitters, npes-1, MPI_INT,allpicks, npes-1, 26 MPI_INT,COmm); 27 28 /\* sort these samples \*/ 29 qsort(allpicks，npes\*(npes-1)，sizeof(int)， Incorder); 30 31 /\* Select splitters $^ { \star } /$ 32 for( $\dot { \bar { \mathbf { \lambda } } } = \hat { \mathbf { \lambda } }$ ; i<npes; $\begin{array} { r } { \dot { \bf 1 } + \boldsymbol { + } \dot { \bf \rho } , } \end{array}$ 33 splitters[i-1] $\equiv$ allpicks[i\*npes]; 34 splitters (npes-1] MAXINT; 35 36 /\* Compute the number of elements that belong to each bucket \*/ 37 scounts $\cong$ (int $\star 1$ malloc(npes\*sizeof(int)）; 38 for( $\therefore = 0$ :i<npes; $\dot { \bar { \mathbf { 1 } } } + \mathbf { + }$ ）

$$
. \qquad : \qquad \cdot \qquad \cdot \qquad \cdot \qquad \cdot \qquad \cdot \qquad \cdot
$$

39 scounts[i] = 0;   
40   
41 for (j=i=0;i<nlocal；i++）{   
42 if(elmnts[i] < splitters[j])   
43 scounts[j]++;   
44 else   
45 scounts $[ + +  j ] + +$   
46   
47   
48 /\*Determine the starting location of each bucket's elements in the elmnts array \*/   
49 sdispls $\approx$ (int $\ast$ )malloc(npes\*sizeof(int));   
50 sdispls[0] $= 0$ ；   
51 for $\mathbf { i } = \mathbf { 1 }$ ; i<npes; $\mathbf { i } + + 1$   
52 Bdispls[i] $\Bumpeq$ sdispls[i-1] +scounts[i-1]:   
53   
54 /\* Perform an all-to-allto inform the corresponding processes of the number of elements \*/   
55 /\* they are going to receive. This information is stored in rcounts array \*/   
56 rcounts $\approx$ (int \*)malloc(npes\*sizeof(int));   
57 MPI_Alltoall(scounts,1，MPI_INT,rcounts,1， MPI_INT,comm);   
58   
59 /\* Based on rcounts determine where in the local array the data from each processor \*/   
60 /\* will be stored. This array willstore the received elements as wellas the final \*/   
61 /\* sorted sequence $^ { * }$   
62 rdispls = (int \*)malloc(npes\*sizeof(int)):   
63 rdiapls(0] = 0:   
64 for $\mathbf { i } \cong \mathbf { 1 }$ :icnpes: $\dot { \bf 1 } + { \bf + }$ ）   
65 rdispls[i] = rdispls[i-1]+rcounts[i-1] ;   
66   
67 \*nsorted rdispls[npes-1] $^ { + }$ rcounts[i-1] ;   
68 sorted_elmnts = (int \*)malloc((\*nsorted)\*sizeof(int)):   
69   
70 /\* Each process sends and receives the corresponding elements, using the MPl_Altoallv \*/   
71 /\* operation. The arrays scounts and sdispls are used to specify the number of elements \*/   
72 1\* to be sent and where these elements are stored, respectively. The arrays rcounts \*/   
73 1\* and rdispls are used to specify the number of elements to be received, and where these \*/   
74 /\* elements will be stored, respectively. \*/   
75 MPI_Alltoallv(elmnts, scounts, sdispls， MPI_INT, sorted_elmnts,   
76 rcounts，rdispls，MPI_INT，comm);   
77   
78 /\* Perform the final local sort \*/   
79 qsort(sorted_elmnts， \*nsorted, sizeof(int)， Incorder):   
80   
81 free(splitters): free(allpicks): free(scounts); free(sdispls);   
82 free(rcounts);free(rdispls);   
83   
84 return sorted_elmnts;   
85

# 6.7 进程组和通信器

在许多并行程序中，通信操作需要限制在部分进程中。MPI提供几种方法将属于某一通信器的进程组划分为子组，每个子组都与不同的通信器相对应。通常使用MPI_Comm_split函数划分进程图，函数的定义如下：

int MPI_Comm_split(MPI_Comm comm，int color，int key, MPI_Comm \*newcomm)

此函数是聚合操作函数，因此必需由通信器comm中的所有进程调用。除了通信器comm外，函数还有两个输入参数color和key，并将属于通信器comm的进程组划分成不相连的子组。每个子组包含对color参数提供同样值的所有进程。在每个子组内部，进程按由参数key的值定义的顺序确定等级，与它们在老的通信器（即comm）中进程等级的划分相联系。newcomm参数为每个子组返回一个新的通信器。图6-7的例子展示用MPI_Comm_split函数将通信器分裂的过程。如果每个进程都用图6-7所示的color和key的参数值调用MPI_Comm__split，那么将创建3个通信器，分别包含进程{0,1,2}、{3,4,5,6}以及{7}。

![](images/62ab7afe30511dd7f4d10b841870978a33ead159591a4c5bd24cf16355fa1c01.jpg)  
图6-7使用MPI_Comm_split将通信器中的进程组划分为子组

分裂笛卡儿拓扑结构在许多并行算法中，进程按虚拟网格排列，在算法的不同步骤中，通信必需限制在网格的一个不同子集内。MPI提供了一种方法，能方便地将笛卡儿拓扑结构划分成低维网格的形式。

MPI提供函数MPI_Cart_sub，用于将笛卡儿拓扑结构划分成构成低维网格的子结构。例如，可以将二维结构划分成组，每个组包含沿着该结构的行或列的进程。函数MPI_Cart_sub的调用序列如下:

int MPI_Cart_sub(MPI_Comm comm_cart，int \*keep_dims, MPI_Comm \*comm_subcart)

数组keep_dims用于指定如何划分笛卡儿拓扑结构。特别，如果keep_dims[i]为真（在C语言中为0)，那么在新的子结构中，第i维保持不变。例如，考虑一个 $2 \times 4 \times 7$ 的三维结构。如果keep_dims的值是{true,false,true}，那么原始结构将分裂为4个大小为 $2 \times 7$ 的二维子结构，如图6-8a所示。如果keep_dims的值是{false,false,true}，那么原始结构将分裂为8个大小为7的一维子结构，如图6-8b所示。注意，新创建的子结构的数目等于沿未保留的各维上的进程数目的乘积。原始结构由通信器comm_cart指定，返回的通信器comm_subcart存储创建的子结构的信息。每个进程只返回一个通信器，对于不属于同一子结构的进程，由返回的通信器指定的组也不同。

属于某一给定子结构的进程可用如下方法确定：假设某三维结构的大小为 $d _ { 1 } \times d _ { 2 } \times d _ { 3 }$ ，且keep_dims值设定为{true,false,true}。若进程用坐标 $( x , y , z )$ 给出，则属于同一子结构的进程组的坐标由 $( * , y , * )$ 给出，这里坐标位置的 $\omega _ { \pmb { \hat { \imath } } } \mathbf { \hat { \imath } }$ 表示该坐标可以取任意可能的值。同时注意，由于第二个坐标的值可以是 $d _ { 2 }$ ，一共创建 $d _ { 2 }$ 个子结构。

![](images/1bd79f1f26575a192616ef8cc4de743af4e2ebe69828e00b471dc105a3677fc2.jpg)  
图6-8分裂大小为2×4×7的笛卡儿拓扑结构：a）分成大小为2×1×7的4个子结构；b）分成大小为 $1 \times 1 \times 7$ 的8个子结构

![](images/6072a8878970bc907233360f604dc2bdb1da55016cb01d5a3f1ccdad2e6c7122.jpg)

![](images/5f7494828e9f149181ccb1bc841b66c4cdab3ed8278099ac936ce0c26cb67167.jpg)  
图6-8（续）

由函数MPI_Cart_sub创建的子结构中的进程坐标也可以通过原始结构中的坐标获得，无需考虑与未保留维对应的坐标。例如，在基于列的子结构中，进程的坐标等于它在二维结构中的行坐标。如坐标为(2,3)的进程，在子结构中有一个坐标为(2)，与网格中的第3列对应。

# 实例：二维矩阵与向口相乘

在6.6.8节，我们提供了两个程序，计算对矩阵按行及按列分配时的矩阵与向量相乘$x = A b$ 。如8.1.2节的讲述，对矩阵分配还可以使用另一种二维的方法，据此可以得到矩阵与向量相乘算法二维并行形式。

程序6-8说明如何用这些结构及其划分来实现二维矩阵与向量相乘。参数 $\pmb { \nmid }$ 指定矩阵的维数，参数a和参数b分别指向矩阵A和向量 $b$ 中本地存储的部分，参数 $\mathbf { x }$ 指向输出矩阵与向量乘积的本地部分。注意只有沿着进程网格第一列的进程才会在开始时存储b，并在返回时，同样的进程将存储结果 $\mathbf { x }$ 。为了简化程序，假设进程数目 $p$ 是完全平方数，且 $\pmb { n }$ 是 $\sqrt { p }$ 的整数倍。

# 程序6-8 二维矩阵与向口相乘

<table><tr><td>1</td><td colspan="3"> MatrixVectorMultiply_2D(int n， double *a， double *b， double *x,</td></tr><tr><td>2 3</td><td>{</td><td>MPI_Comm comm)</td><td></td></tr><tr><td>4</td><td colspan="3">int ROW=0， COL=1: /* Improve readability */</td></tr><tr><td>5</td><td>int i，j，nlocal;</td><td></td><td></td></tr><tr><td>6</td><td>double *px: /* Will store partial dot products */</td><td></td><td></td></tr><tr><td>7</td><td>int npes，dims[2]，periods[2]，keep_dims[2] ;</td><td></td><td></td></tr><tr><td>8</td><td>int myrank，my2drank， mycoords[2];</td><td></td><td></td></tr><tr><td>9</td><td>int other_rank，coords[2];</td><td></td><td></td></tr><tr><td>10</td><td>MPI_Status status:</td><td></td><td></td></tr><tr><td>11</td><td>MPI_Comm comm_2d，comm_row，comm_col;</td><td></td><td></td></tr><tr><td>12</td><td></td><td></td><td></td></tr><tr><td>13</td><td>/* Get information about the communicator */</td><td></td><td></td></tr><tr><td>14</td><td>MPI_Comm_size(comm, &amp;npes) :</td><td></td><td></td></tr><tr><td>15</td><td>MPI_Comm_rank(comm, &amp;myrank) :</td><td></td><td></td></tr><tr><td>16</td><td></td><td></td><td></td></tr><tr><td>17</td><td>/* Compute the size of the square grid */ dims[ROW] = dims[COL] = sqrt (npes);</td><td></td><td></td></tr><tr><td>18 19</td><td></td><td></td><td></td></tr><tr><td>20</td><td>nlocal = n/dims[ROW] ;</td><td></td><td></td></tr><tr><td>21</td><td></td><td></td><td></td></tr><tr><td>22</td><td>/* Allocate memory for the array that will hold the partial dot-products */</td><td></td><td></td></tr><tr><td>23</td><td>px = malloc(nlocal*sizeof(double)) ;</td><td></td><td></td></tr><tr><td>24</td><td></td><td></td><td></td></tr><tr><td>25</td><td>/* Set up the Cartesian topology and get the rank &amp; coordinates of the process in this topology</td><td></td><td></td></tr><tr><td>26</td><td></td><td>periods [Row] = periods [COL] = 1； /* Set the periods for wrap-around connections</td><td></td></tr></table>

27   
28 MPI_Cart_create(MPI_COMM_WORLD，2，dims，periods，1，&comm_2d);   
29   
30 MPI_Comm_rank (comm_2d， &my2drank) ； /\* Get my rank in the new topology \*/   
31 MPI_Cart_coords(comm_2d， my2drank，2，mycoords): /\*Get my coordinates \*/   
32   
33 /\* Create the row-based sub-topology \*/   
34 keep_dims {ROW] $= 0$ i   
35 keep_dims [COL] $\mathit { \Theta } = \mathit { \Theta } $ ；   
36 MPI_Cart_sub(comm_2d，keep_dims,&comm_row);   
37   
38 /\* Create the column-based sub-topology \*/   
39 keep_dims [ROW] $\mathbf { \lambda } = \mathbf { \lambda } \mathbf { 1 }$ ：   
40 keep_dims [COL] $= 0 ;$   
41 MPI_Cart_sub(comm_2d,keep_dims，&comm_col):   
42   
43 /\* Redistribute the b vector. $^ { \star } /$   
44 /\* Step 1. The processors along the Oth column send their data to the diagonal processors \*/   
45 if (mycoords [COL] $\yen 0$ && mycoords [ROW] $! = 0 !$ { /\* I'm in the first column $^ { \ast } /$   
46 coords [ROW] $\lneq$ mycoords [ROW] ;   
47 coords [cOL] $\risingdotseq$ mycoords [ROw] ;   
48 MPI_Cart_rank(comm_2d,coords,&other_rank);   
49 MPI_Send(b，nlocal，MPI_DoUBLE，other_rank，1，comm_2d);   
50 ）   
51 if (mycoords[ROW] $z =$ mycoords [coL] && mycoords[ROW] ${ \bf \updownarrow } = { \bf \up0 } { \bf \dagger }$   
52 coords [ROW] $\approxeq$ mycoords [ROW]；   
53 coords[CoL] $\yen 0$ ：   
54 MPI_Cart_rank(comm_2d, coords, &other_rank);   
55 MPI_Recvb, nlocal， MPI_DOUBLe,other_rank,1, comm_2d,   
56 &status);   
57   
58   
59 /\* Step 2. The diagonal processrs perform a column-wise broadcast \*/   
60 coords [0] mycoords [CoL] ;   
61 MPI_Cart_rank(comm_col, coords, &other_rank);   
62 MPI_Bcast(b,nlocal,MPI_DoUBLE,other_rank,comm_col);   
63   
64 /\* Get into the main computational loop \*/   
65 for $\therefore 0$ ；i<nlocal; $\dot { \mathbf { 1 } } + \mathbf { \star }$ ）   
66 $\pmb { \mathrm { p x } } \{ \mathbf { i } \} = 0 . 0$ i   
67 for $\dot { \ b { \mathscr { I } } } = \pmb { 0 }$ : j<nlocal; j++)   
68 px[i] += a[i\*nlocal+j]\*b[j]；   
69 ！   
70   
71 /\*Perform the sum-reductionalong therows toadd upthepartial dot-products \*/   
72 coords[0] $= 0$ ；   
73 MPI_Cart_rank(comm_row, coords, &other_rank);   
74 MPI_Reduce(px， X，nlocal, MPI_DOUBLE,MPI_SUM, other_rank,   
75 comm_row);   
76   
77 MPI_Comm_free(&comm_2d)； /\* Free up communicator \*/   
78 MPI_Comm_free(&comm_row)；/\* Free up communicator \*/   
79 MPI_Comm_free(&comm_col）; /\*Free up communicator \*/   
80   
81 free(px) :   
82 1

# 6.8书目评注

有关MPI的最好资料来源是MPI库本身的实际参考手册[Mes94]。在写这本书时，MPI标准已有两个主要版本。第一个版本1.0版于1994年发布，其最近的修订1.2版，已由绝大多数硬件供应商实现。MPI标准的第二个版本2.0版[Mes97]，对1.x版的许多方面进行了增强，如单侧通信、动态进程创建以及扩展的聚合操作等。然而，虽然标准在1997年就制定了，却没有广泛可用的MPI-2实现来支持由标准指定的所有特性。除了上面提到的参考手册外，许多书籍也致力于使用MPI的并行编程[Pac98,GSNL98,GLS99]。

除了由多个硬件提供商提供的MPI实现外，许多政府研究机构和大学也开发了多个公用的MPI实现，其中包括由Argonne国家实验室发布的MPICH[GLDS96,GL96b]（从http://www-unix.mcs.anl.gov/mpi/mpich可以获得相关信息），以及由Indianna大学发布的LAM-MPI（在http://www.lam-mpi.org可以获得相关信息)，这些MPI实现已得到广泛的应用，并能移植到多种不同的体系结构中。事实上，这些MPI实现已被用作一些专门化MPI实现的出发点，而这些专门化MPI实现很适合用在如千兆以太网和Myrinet网等流行的互连网络中。

# 习题

6.1试描述只由发送进程执行缓冲操作的有缓冲发送和接收的消息传递协议。为了使这些协议切实可行，需要什么样的硬件支持？

6.2无阻塞式通信操作的优点之一是它们能使数据的传送与计算并发进行。试讨论为了实现计算与通信的最大重叠对程序进行重新组织的类型。发送进程是不是比接收进程更能从这种重叠中受益？

6.3如6.3.4节所述，MPI标准允许用两种不同形式的MPI_Send操作实现—--一种使用有缓冲的发送；另一种使用阻塞式发送。试讨论MPI允许这两种不同实现的潜在原因。特别，请考虑不同的消息大小及不同的体系结构特点。

6.4考虑如图6-5所示的从16个处理器到4×4二维网格的不同映射。说明在n=√p×√p个处理器时，四种映射方案分别如何映射。

6.5考虑矩阵与矩阵相乘的Cannon算法。我们讨论的Cannon算法中，矩阵A和矩阵B都被限制为正方形矩阵，映射到正方形网格的进程中。然而，Cannon算法可以扩展到A、B以及进程网格都不是正方形的情形。若矩阵A的大小为n×k，矩阵B的大小为k×m，则矩阵A和B相乘得到的矩阵C的大小为n×m。同样，设排列在q行r列的网格中的进程数目为q×r。请用Cannon算法设计一个MPI程序，实现在 $q \times r$ 的进程网格上，将上述的两个矩阵相乘。

6.6当矩阵的维数不是进程数目的整数倍时，说明按行的矩阵与向量相乘的程序（程序6-4）需要修改才能正确运行。

6.7考虑按列实现的矩阵与向量相乘（程序6-5)。另一种实现方法是用MPI_A1lreduce进行需要的归约操作，然后让每个进程从向量fx处复制向量x的本地存储部分。这种实现的成本是什么？还有一种实现方法是以不同的进程作为根，执行p个单节点归约操作。这种实现的成本是什么？

6.8考虑6.6.9节中所述的Dijkstra单源最短路径算法。说明为什么加权邻接矩阵的按列序分配要优于按行序分配。

·6.9对于q×r的进程网格上大小为n×m的矩阵，说明二维矩阵与向量相乘的程序（程序6-8）为什么需要修改才能正确执行。

# 第7章 共享地址空间平台的编程

显式并行编程要求指定并行任务以及这些任务间的交互。这些交互可能表现为并发任务的同步形式，或中间结果的通信形式。在共享地址空间结构中，由于所有的处理器可以访问部分（或者全部）内存，通信是隐式指定的。因此，在共享地址空间计算机上的编程模式侧重于并发与同步的构建，以及相关开销最小化的技术等。本章将讨论共享地址空间的编程模式及其性能问题，以及基于命令模式编程的扩充等。

在不同的数据共享、并发模型和同步支持机制中，共享地址空间编程模式可能有所不同。在默认情况下，基于模型的进程假设与一个进程相关的所有数据都是私有的，除非用shmget和shmat这样的UNIX系统调用进行另外说明。虽然这一点在多用户系统中对提供保护很重要，但当用多个并发聚集协作解决同一个问题时是不需要的。与加强保护域相关的开销使得这种进程不大适用于并行编程。相反，轻量级进程及线程假设所有的内存都是全局的。通过释放保护域，轻量级进程及线程支持更快的运行。因此，这是并行编程的首选模型，构成本章的核心。通过推动线程的创建和同步，基于命令的编程模型扩充线程模型。在本章我们对使用线程和并行命令的编程进行多方面讨论。

# 7.1线程基础

线程（thread）是程序流程中的单一控制流。下面用一个简单的例子来讲述线程：

# 例7.1什么是线程

下面的代码段计算两个大小为 $n \times n$ 的稠密矩阵的乘积。

$$
\begin{array} { r l } { \{ { \bf \Upsilon } { \cal { r o w } } ~ = ~ 0 ~ ; ~ { \bf \Upsilon } { \cal { r o w } } ~ < ~ \Omega _ { i } ~ ; ~ { \bf \Upsilon } { \cal { r o w } } + + \} } & { { } } \\ { \{ { \bf \Upsilon } { \cal { \sf o r } } ~ \langle { \sf c o l u m n ~ \Omega _ { \tau } ~ = ~ 0 } ~ ; ~ { \bf \Upsilon } { \sf c o l u m n ~ < ~ \Omega _ { n } } ; ~ { \bf \dot { \Omega } } { \bf { \sigma } } { \mathrm { c o l u m n } } + \rangle }  & { { } } \\ { \{ { \bf \Upsilon } { \cal { \sf c } } ~ [ { \bf \Upsilon } { \cal { r o w } } ] ~ [ { \bf \Omega } \mathrm { c o l u m n } ] ~ = } ~  & { { } } \\ { \{ { \bf \Upsilon } { \sf d o t \_ p r o d u c t } ~ \{ { \bf \Upsilon } ( { \bf g e t \_ r o w } ~ ( a , ~ { \bf \Omega } { \bf r o w } ) ~ , ~ { \bf \Omega } { \bf r o w } ) ~ , }  & { { } } \\ { \{ { \bf \Upsilon } { \sf g e t \_ c o l } ~ ( { \bf b } , ~ { \bf \Omega } { \bf c o l } ) ~ \} ~ ; }  & { { } } \end{array}
$$

在这个代码段中有 $n ^ { 2 }$ 次迭代，每一次迭代都能独立执行。这样一种独立的指令序列称为一个线程。在上面的例子中，共有 $n ^ { 2 }$ 个线程，每一个对应for循环中的一次迭代。由于每个线程能独立于其他线程执行，它们可在多处理器中并发调度。上面的代码段可以修改如下：

！ for $\tt { r o w } = 0$ ; row < n; row++)   
2 for (column = 0; column < n; column $^ { + + }$ ）   
3 c[row] [column]   
4 create_thread(dot_product(get_row(a, row),   
5 get_col(b,col)));

这里，我们使用create_thread函数提供创建线程的机制，指定一个C语言函数为线程。这样，系统就能在多处理器中对线程进行调度。 □

线程的逻辑内存模型要在多处理器中执行例7.1的代码，每个处理器必须对矩阵a、b、c进行访问。这是通过一共享地址空间实现的（在第2章中讲述)。如图7-1a所示，在线程的逻辑计算机模型中，所有内存对于每个线程是全局可访问的。然而，由于线程作为函数调用，与函数调用相对应的堆栈通常被处理成线程本地的堆栈，这也是出于对堆栈活性的考虑。由于线程是在运行时调度（而且任何对线程执行的事先调度都是不安全的），无法确定哪些堆栈是活的。因此，只有那些较差的程序才将堆栈（线程本地变量）当成全局数据。这就隐含如图7-1b所示的一个逻辑计算机模型，模型中的内存模块M中保存线程本地（分配的堆栈）数据。

虽然这种逻辑计算机模型给出同等可访问地址空间的观点，但是，模型的物理实现偏离这个假设。在像Origin 2000这样的分布式共享地址空间计算机中，物理上访问本地内存的成本要比访问远程内存的成本少一个数量级。即使在所有处理器对内存真正可以同等访问的结构中（如有全局共享内存的共享总线结构)，处理器上高速缓存的存在还是会使内存存取时间出现偏差。所以，内存的本地访问问题对于在这样的结构中榨取性能是十分重要的。

![](images/9fefd26490862aec55885b40cb6f3fc6cc662eda3bf47c49c8706dc564f14854.jpg)  
图7-1基于线程的编程模式中的逻辑计算机模型

# 7.2为什么要用线程

与消息传递编程模型相比，线程编程模型既有显著的优点，又有一些缺点。在讨论线程API之前，先简单地看一下这些优缺点。

软件可移植性线程应用程序可以在串行计算机上开发，并且不作任何改变地在并行计算机上运行。这种在不同的结构平台上移植程序的能力是线程API的一个非常重要的优点。它的意义不仅仅在于软件的利用率上，还在于应用程序的开发上，因为超级计算机时间通常既少又贵。

躲避延迟无论是串行还是并行程序，其最大的开销之一都是内存存取、I/O以及通信方面的存取延迟。但通过在同一处理器上执行多个线程，线程API就能躲避延迟时间（见第2章）。实际上，当一个线程等待通信操作时，其他的线程可以利用CPU，这样就能屏蔽相应的开销。

调度及负载平銜在编写共享地址空间并行程序时，程序员要表现并发就必须最小化远程交互以及空闲。虽然在许多结构化的应用程序中，分配同等的任务给处理器很容易实现，但在一些非结构化以及动态的应用程序（如游戏及离散优化）中，这一点却很难做到。线程API允许程序员指定大量的并发任务，并支持系统级的从任务到处理器的动态映射，以最小化空闲的开销。通过在系统级提供这种支持，线程API使程序员摆脱显式调度和平衡负载的负担。

容易编程，广泛使用因为上述优点，线程化的程序要比相应的使用消息传递API的程序容易编写得多。但是，要使这两种程序达到同样的性能还需要其他方面的努力。随着POSIX线程API被广泛接受，开发POSIX线程的工具也越来越多，越来越稳定。从程序开发及软件工

程的角度来说，这些特点都很重要。

# 7.3 POSIX线程API

许多供应商提供专用的线程API。IEEE指定一个标准1003.1c-1995，POSIXAPI。POSIX也称为Pthreads，已成为标准的被绝大多数供应商支持的线程API。我们将使用Pthreads API来引出多线程的概念。这些概念本身在很大程度上独立于API，可以与其他的线程API（NT线程、Solaris线程以及Java线程等）一起用于编程。本章提出的所有说明性程序既能在工作站上运行，也能在支持Pthreads的并行计算机上运行。

# 7.4 线程基础：创建和终止

首先用一个简单的计算 $\pmb { \pi }$ 值的程序来开始我们的讨论。

# 例7.2计算 $\pi$ 的线程程序

这里所用的方法，是基于在单位长度的正方形中产生随机数，并计算落在正方形的内接圆中的点的数目。由于圆的面积 $( \pi r ^ { 2 } )$ 等于 $\pi / 4$ ，正方形的区域为 $1 \times 1$ ，落在圆中的随机点的数目应该接近 $\pi / 4$ 。

使用线程计算 $\pi$ 值的一个简单策略是：分配固定数目的点给每个线程，每个线程产生这些随机点并记录下落在圆内部的点的数目。在所有的线程执行完毕后，将所有的点相加计算 $\pmb { \pi }$ 的值（将记录下的点数总和除以分配给所有线程的点，再乘以4）。

要实现这个线程程序，需要用一个函数创建线程并等待所有的线程完成执行（这样才能计算点数)。线程可以在PthreadsAPI中用函数pthread_create创建。这个函数的原型为

1 #include <pthread.h>   
2 int   
3 pthread_create (   
4 pthread_t \*thread_handle,   
5 const pthread_attr_t \*attribute,   
6 void \* (\*thread_function)(void \*),   
7 void \*arg);

pthread_create函数创建一个单一的线程，对应thread_function函数(以及任何其他的由thread_function调用的函数）的调用。成功地创建一个线程后，有一个唯一的标识符与之对应，标识符被分配到由thread_handle指向的位置。线程的属性由参数attribute给出，当该参数为NULL时，创建一个具有默认属性的线程。在7.6节中将详细讨论attribute参数。字段arg指定一个指针，指向函数thread_function的参数。这个参数通常用来将工作区或其他线程指定的数据传送给一个线程。在compute_pi例子中，它用来传送一个当作随机种子的整数id。变量thread_handle要写在函数pthread_create返回之前；新的线程一旦创建就会立刻执行。如果线程在同一个处理器上调度，新的线程可能先占其创建者。这一点非常重要，因为在线程创建之前，所有的线程初始化程序都必须完成。否则，就可能出现基于线程调度的错误。这是一类很常见的错误，由数据存取时的竞争状态所致，这种竞争状态只在某些执行实例中会出现。成功地创建一个线程后，pthread_create返回0；否则返回-个错误代码。有关错误代码详细内容，读者可以参考Pthread说明书。

在上面计算π值的程序中，首先读入所需线程的数目num_threads，以及所需的样本点数目sample_points。这些点在线程间平均分配。程序中使用数组hits来分配整数id给每个线程（这个id被随机数发生器作为产生随机数的种子)。同一数组也被用于记录每个线程返回前命中的次数（圆内的点数）。程序用pthread_create函数创建num_threads个线程，每个线程都调用函数compute_pi。

在每个compute_pi线程产生了分配数目的随机点并计算出命中率后，必须将结果结合起来以确定 $\pmb { \pi }$ 。主程序必须等待所有的线程运行完毕。这一点是通过函数pthread_join实现的，它挂起正在调用的线程，直到指定的线程终止。函数pthread_join的原型如下:

1 int   
2 pthread_join (   
3 pthread_t thread,   
4 void \*\*ptr):

对这个函数的调用将等待由thread给出其id的线程终止。在对pthread_join的一次成功的调用中，传递给 $\mathtt { p t h r e a d \_ e x i t }$ 的值返回到由 $\phi + I$ 指向的位置。在pthread_join调用成功完成后返回0，否则返回一个错误代码。

所有的线程结合后，将合并后的命中率乘以4.0就得到 $\pmb { \pi }$ 的值。完整的程序代码如下：

1 #include <pthread.h>   
2 #include <stdlib.h>   
3   
4 #define MAX_THRRADS 512   
5 void \*compute_pi (void \*);   
6   
7 int total_nits， total_misses, hits [MAX_THREADS],   
8 sample_points, sample_points_per_thread, num_threads;   
9   
10 main(）{   
11 int i;   
12 pthread_t P_threads [MAX_THREADS] ;   
13 pthread_attr_t attr;   
14 double computed_pi;   
15 double time_start, time_end;   
16 struct timeval tv:   
17 struct timezone tz;   
18   
19 pthread_attr_init (&attr):   
20 pthread_attr_setsCope (&attr, PTHREAD_SCOPE_SYSTEM) ;   
21 printf("Enter number of sample points: ");   
22 Bcanf("td",&sample_points);   
23 printf("Enter number of threads: ");   
24 scanf("td", &num_threads);   
25   
26 gettimeofday(&tv, &tz);   
27 time_start = (double)tv.tv_sec +   
28 (double)tv.tv_usec / 1000000.0;   
29   
30 total_hits 0；   
31 Bample_points_per_thread = sample_points / num_threads:   
32 for (i=0; i< num_threads; i++){   
33 hits[i] = i;   
34 pthread_create(&p_threads[il，&attr, compute_pi,   
35 (void $\bigstar$ ）&hits[i]);   
36 ！   
37 for (i=o; i< num_threads; $\mathbf { i } + +$ {   
38 pthread_join(p_threads[i]，NULL) ;   
39 total_hits $+ =$ hits[i];   
40   
41 computed_pi $=$ 4.0\*(double) total_hits /   
42 ((double)(sample_points)）;   
43 gettimeofday(&tv，&tz);   
44 time_end $\simeq$ (double)tv.tv_sec +   
45 (double)tv.tv_usec / 10o0000.0;   
46   
47 printf("Computed $p I = 8 1 f \backslash n "$ ，computed_pi);   
48 printf(" %lf\n", time_end - time_start);   
49   
50   
51 void \*compute_pi (void $\star _ { \ 8 }$ ）{   
52 int seed,i,\*hit_pointer;   
53 double rand_no_x,rand_no_y;   
54 int local_hits;   
55   
56 hit_pointer (int $\bigstar$ ）;   
57 seed = \*hit_pointer;   
58 local_hits $\qquad = \quad 0$   
59 for (i = 0: i < sample_points_per_thread; i++){   
60 rand_no_x $\cong$ (double)(rand_r(&seed))/(double)((2<<l4)-1) ;   
61 rand_no_y $\eqcirc$ (double)(rand_r(&seed))/(double) ((2<<l4)-1);   
62 if (((rand_no_x - 0.5) \* (rand_no_x - 0.5) +   
63 (rand_no_y - 0.5) \* (rand_no_y - 0.5)) < 0.25)   
64 local_hits ++;   
65 seed \*= i;   
66 ！   
67 \*hit_pointer $\eqcirc$ local_hitsi   
68 pthread_exit(0);   
69

编程须知读者必须注意，在上面的例子中用到函数rand_r(而不是如drand48这样更好的随机数产生器)。这是因为许多函数（包括rand和drand48）都不是可重入的(reentrant)。可重入函数是在调用过程中当另一个实例被挂起后还能安全地调用的函数。容易看出为什么所有线程函数必须是可重入的，因为线程在执行过程中可能被先占。如果另一个线程在先占的这一点开始执行同一个函数，不可重人的函数就可能出现意想不到的情况。

性能须知我们在4处理器的SGIOrigin2000上执行这个程序。线程数的对数与执行时间的关系曲线如图7-2所示（曲线标记为“local”）。从图中可以看出，使用32个线程时，程序的运行时间大约比使用单线程时的时间少3.92倍。在4个处理器的计算机中，它对应的并行效率为0.98。

图7-2中的其他曲线解释一种称为假共辛（false sharing）的重要性能开销。考虑将程序作如下修改：代替对本地变量local_hits加1和分配到在循环外部的数组中，现在直接将hits数组中对相应的项加1。具体做法是把第64行改为\*(hit_pointer)++；，并删除第67行。容易验证修改后的程序与修改前的程序在语义上是完全相同的，然而，执行修改后的程序在图7-2中得到的却是标记为“spaced_1”的性能曲线。这表示性能非但没有提升，反而显著地降低了。

程序看上去没有什么大的改变，但影响却非常大，这可以用所谓假共享的现象来解释。在本例中，两个相邻接的数据项（很可能位于同一高速缓存行中）持续地被多个线程写入，这些线程可能在不同的处理器上调度。从第2章的讨论可知，向共享高速缓存行写人将导致无效操作，随后的读操作必须从最近的写操作位置取高速缓存行。由于重复地进行增1操作，与hits数组相对应的高速缓存行将产生大量的无效操作和读操作。两个线程“虚假地”共享数据因为数据正好位于同一高速缓存行，这种情况称为假共享。

![](images/616dee79511a26f7af292af91c522ddcfa9643f622744bba095affb32396da48.jpg)  
图7-2compute_pi程序的执行时间与线程数的关系曲线

实际上用这个简单的例子可以估计系统的高速缓存行的大小。将hits改成二维数组，并且只用数组的第一列来存储点数。通过改变第二维的大小，就能强制hits数组中第一列的数据项放到不同的高速缓存行中（因为在C语言中，数组按行存储)。这个实验的结果在图7-2中由标记为“space_16”和“space_32”的曲线说明，这两条曲线对应的hits数组的第二维大小分别为16及32。从图中很容易看出，当数据项在空间上分开时，就能提高性能。这一点和我们的理解是一致的，因为将数据项分开，就能使数据项进人不同的高速缓存行，从而降低假共享的开销。 □在理解如何创建及连接线程后，再来研究Pthreads中线程同步的机制。

# 7.5Pthreads中的同步原语

虽然通信在共享地址空间编程中是隐式的，但与编写正确的线程程序相关的主要工作是使得与数据存取或调度有关的并发线程同步。

# 7.5.1共享变的互斥

使用pthread_create和pthread_join调用能创建并发的任务。这些任务共同操作数据并完成给定的任务。当多个线程试图操作同一数据项时，如果没有采取适当的方法使这些线程同步，结果往往会不一致。考察下面由多线程执行的代码段，其中my_cost是线程本地的变量，而best_cost是由所有线程共享的全局变量。

1 /\* each thread tries to update variable best_cost as follows \*/   
2 if (my_cost < best_cost) best_cost my_cost;

为了理解共享数据存取问题，先来试验上面代码段的一个执行实例。假设有两个线程，变量best_cost的初始值为100，在线程t1和t2中my_cost的值分别为50和75。如果两个线程并发地执行if语句中的条件，那么两个线程都会进入语句的then部分。依据哪个线程首先执行，最终best_cost的值可以是50，也可以是75。这里有两个问题：首先是结果的不确定性；其次，也是更重要的，在两个线程串行化也不能使变量best_cost的值为75的情况下，这个值是不一致的。这种情况不是人们希望看到的，有时也称为竞赛条件（这样称呼是因为计算的结果取决于竞争线程间的竞赛）。

上面提到的情况发生的原因是，前面讲到的测试并更新操作是原子操作，即不能再分成子操作的操作。而且，代码与一个临界段对应；即在任何时候，该代码段只能由一个线程执行。在像C语言这样的高级语言中，许多语句看上去是原子语句，但事实上不是；例如，语句global_count $+ = 5$ 可能包含几条汇编指令，因此，在处理该语句时一定要小心。

线程API用mutex-lock（互斥锁）为实现临界段和原子操作提供支持。mutex-lock有两种状态：锁定状态与非锁定状态。在任意时刻，只有一个线程能锁定一个互斥锁。锁是原子操作，通常与操作共享数据的一段代码有关。要存取共享数据，线程必须首先获得mutex-lock，如果mutex-lock已经锁定，则进程就不能获得锁。这是因为，锁定的mutex-lock表示另一个线程当前处于临界段，不允许其他任何线程进入。当线程离开临界段后，它必须对mutex-lock解锁，这样其他的线程才能进入临界段。在程序的开始，所有的mutex-lock都必须初始化为非锁定状态。

Pthreads API提供多个处理mutex-lock的函数。函数pthread_mutex_lock可用来锁定mutex-lock。函数的原型为：

1 int   
2 pthread_mutex_lock (   
3 pthread_mutex_t \*mutex_lock);

对此函数的调用试图锁定互斥锁mutex-lock（mutex-lock的数据类型预定义为pthread_mutex_t）。如果mutex-lock已经锁定，则调用的线程阻塞；否则mutex-lock被锁定，并且调用的线程返回。函数成功返回时返回数值0。其他的值则表示死锁等错误情况。

离开临界段时，线程必须为与mutex-lock关联的段解锁。否则，其他的线程将不能进入这个段，通常会导致死锁。Pthreads函数pthread_mutex_unlock用来对mutex-lock解锁，这个函数的原型如下：

1 int   
2 pthread_mutex_unlock (   
3 pthread_mutex_t \*mutex_lock);

调用此函数时，对于正常的mutex-lock，锁被放弃，阻塞的线程之一被调度进入临界段。指定的线程由调度策略确定。在7.6节讨论一些其他类型的锁（不同于正常的锁)，以及相关的pthread_mutex_unlock函数的语义。如果程序员试图对已经解锁的互斥锁或对被另一个线程锁定的互斥锁，进行pthread_mutex_unlock操作，其结果是不确定的。

使用互斥锁之前，还需要另一个函数，即将互斥锁初始化为未锁定状态的函数。执行这一任务的pthreads函数为pthread_mutex_init，它的原型如下:

1 int   
2 pthread_mutex_init (   
3 pthread_mutex_t \*mutex_lock,   
4 const pthread_mutexattr_t \*lock_attr);

此函数将互斥锁mutex_lock初始化为未锁定状态。互斥锁的属性由参数lock_attr指定。如果该参数设置为NULL，则函数将使用互斥锁的默认属性（正常互斥锁)。线程的属性对象在7.6节更详细讨论。

# 例7.3计算一整数列表的最小项

有了基本的mutex-lock函数后，下面来编写一个简单的线程程序，计算一整数列表中的最小值。整数列表在线程间平等划分，每个线程划分的大小存储在变量partial_list_size中，指针list_ptr指向每个线程部分列表的起始位置，并传递给变量partial_list_size。完整的线程程序如下：

1 #include <pthread.h>   
2 void \*find_min(void \*list_ptr);   
3 pthread_mutex_t minimum_value_lock;   
4 int minimum_value, partial_list_size;   
5   
6 main(）{   
7 /\* declare and initialize data structures and list \*/   
8 minimum_value $\eqcirc$ MIN_INT;   
9 pthread_init();   
10 pthread_mutex_init (&minimum_value_lock, NULL);   
11   
12 /\* initialize lists,list_ptr, and partial_list_size \*/   
13 /\* create and join threads here \*/   
14   
15   
16 void \*find_min(void \*list_ptr){   
17 int \*partial_list_pointer,my_min,i;   
18 my_min $\cong$ MIN_INT;   
19 partial_list_pointer $\mathbf { \beta } =$ (int \*） list_ptr;   
20 for (i = 0; i < partial_list_size; i++)   
21 if (partial_list_pointer[i] < my_min)   
22 my_min $\cong$ partial_list_pointer[i];   
23 /\* lock the mutex associated with minimum_value and   
24 update the variable as required \*/   
25 pthread_mutex_lock(&minimum_value_lock);   
26 if (my_min $\blacktriangleleft$ minimum_value)   
27 minimum_value = my_min;   
28 /\* and unlock the mutex \*/   
29 pthread_mutex_unlock (&minimum_value_lock) ;   
30 pthread_exit(0);   
31 ）

编程须知 在本例中，对minimum_value的测试并更新操作由互斥锁minumum_value_lock保护。线程执行pthread_mutex_lock以获得对变量minumum_value的独占存取。只要这次存取获得后，数值便按要求更新，随后锁被释放。由于在任意时刻只有一个线程能持有一个锁，也就只有一个线程能对变量进行测试并更新。

# 例7.4生产者-消费者工作队列

互斥锁的一-个常见的用法是在线程间建立生产者-消费者关系。生产者创建任务，并把它们插入到工作队列中。消费者线程从任务队列中取出任务并执行。让我们来考虑这种模式的--个简单情况，其中每个任务队列中只能保存一个任务（通常情况下，工作队列会更长，但长度是有限的)。生产者-消费者关系是普遍存在的，习题7.4是在多媒体处理中的一个例子。-个简单的（和不正确的）线程程序里，生产者线程创建任务，并将任务放到共享的数据结构中，而消费者线程从共享数据结构中取出任务，并执行任务。但是，这种简单的程序并没有考虑如下可能性：

·当前面一个任务没有被消费者线程取出时，生产者线程一定不能覆盖共享缓冲区。  
·在共享数据结构非空之前，消费者线程一定不能取出任务。  
·每一个消费者线程一次只能取出一个任务。

为了实施，我们可以用变量task_available。如果这个变量为0，则消费者线程必须等待，但生产者线程可以把任务插入到共享数据结构task_queue中。如果task_available为1，则生产者线程必须等待，不能马上将任务插入共享数据结构中，但消费者线程之一可以取出已有的任务。所有这些对变量task_available的操作必须由mutex_lock保护，以保证只有一个线程对它执行测试并更新。这个程序的线程版本如下：

1 pthread_mutex_t task_queue_lock;   
2 int task_available;   
3   
4 /\* other shared data structures here \*/   
5   
6 main(）{   
7 /\* declarations and initializations \*/   
8 task_available $\qquad = \quad 0$   
9 pthread_init();   
10 pthread_mutex_init(&task_queue_lock，NULL);   
11 /\* create and join producer and consumer threads \*/   
12 ）   
13   
14 void \*producer(void \*producer_thread_data){   
15 int inserted;   
16 struct task my_task;   
17 while （!done()）{   
18 inserted = 0;   
19 create_task(&my_task);   
20 while (inserted $\ r = \ O \left( \Omega \right)$ {   
21 pthread_mutex_lock(&task_queue_lock):   
22 if (task_available $\qquad = \qquad 0$   
23 insert_into_queue(my_task);   
24 task_available = 1;   
25 inserted = 1;   
26   
27 pthread_mutex_unlock(&task_queue_lock);   
28 ！   
29   
30 ）   
31   
32 void \*consumer(void \*consumer_thread_data){   
33 int extracted;   
34 struct task my_task;   
35 /\* local data structure declarations \*/   
36 while （!done()）{   
37 extracted = 0;   
38 while (extracted $\qquad = \qquad 0$ ）{   
39 pthread_mutex_lock(&task_queue_lock) ;   
40 if (task_available == 1){   
41 extract_from_queue(&my_task);   
42 task_available $\qquad = \ 0$   
43 extracted $\mathbf { \lambda } = \mathbf { \lambda } \mathbf { 1 }$ ；   
44   
45 pthread_mutex_unlock(&task_queue_lock) ;   
46   
47 process_task(my_task);   
48   
49

编程须知在本例中，生产者线程创建一个任务，并等待队列中的空间。这一点由变量task_available为0指示。对这个变量的测试并更新，以及向共享队列插入任务和从共享队列中取出任务，都由互斥锁task_queue_lock保护。一旦任务队列中的空间可用，则最近创建的任务就插入到任务队列中，于是变量task_available被设置为1，说明有任务可用。在生产者线程中，变量inserted设置为1，表示最近创建的任务已被插入队列，这样生产者就可以产生下一个任务。无论最近创建的任务是否成功地插入到队列中，锁都会被解除。这样消费者线程在队列中有任务的情况下就能从队列中获取任务。如果锁没有被解除，线程就会死锁，这是因为消费者线程无法得到锁来获取任务，生产者也不能将任务插入到任务队列中。消费者线程等待任务变成可用的并在可用时执行它。如像生产者线程那样，在while循环的每一次迭代中，消费者都要解除锁，使生产者在队列为空的情况下将任务插入到队列中。 □

# 1.锁开销

锁表示串行化的点，因为临界段必须由线程一个接一个地执行。将大段程序封装在锁中会导致性能下降。最小化临界段的大小很重要。例如在上面的例子中，函数create_task和process_task处于临界段之外，但insert_into_queue和extract_from_queue函数处于临界段之内。前者在临界段之外是为了使临界段尽可能地小，而insert_into_queue和extract_from_queue函数处于临界段之中，是因为如果锁在更新task_available后被解除，但没有插人或获取任务，当其他的线程正在进行插入或获取时就可能获得对共享数据结构的访问，这样就会导致错误。因此，一定要非常小心地处理临界段和共享数据结构，以避免这种错误发生。

# 2.减小锁开销

用另一个函数pthread_mutex_trylock可以减少与锁相关的空闲开销。这个函数试图锁定mutex_1ock。如果锁定成功，函数返回0；如果锁已被其他的线程锁定，函数返回一个值EBUSY而不是阻塞线程操作。这样就能使线程执行其他的任务，并轮询互斥锁。此外，在典型的系统中，通常pthread_mutex_trylock要比pthread_mutex_lock快得多，因为它无需处理当多个线程等待锁时与锁有关的队列。函数pthread_mutex_trylock的原型如下：

1 int   
2 pthread_mutex_trylock (   
3 pthread_mutex_t \*mutex_lock) ;

我们用下面的例子来说明这个函数的用法：

# 例7.5找出一个列表中k个匹配的数

本例从给定的列表中找出k个与查询项匹配的数。列表在所有线程间同等划分。假设列表有n项，有p个线程，每个线程负责查找列表的 $n / p$ 项。使用pthread_mutex_trylock函数求解的程序段如下：

1 void \*find_entries(void \*start_pointer) {   
2   
3 /\* This is the thread function \*/   
4   
5 struct database_record \*next_record;   
6 int count;   
7 current_pointer start_pointer;   
8 do   
9 next_record = find_next_entry(current_pointer);   
10 count $\yen 1$ output_record(next_record) ;   
11 }while (count < reguested_number_of_records);   
12   
13   
14 int output_record(struct database_record \*record_ptr){   
15 int count;   
16 pthread_mutex_lock(&output_count_lock) :   
17 output_count ++;   
18 count $\yen 1$ output_count;   
19 pthread_mutex_unlock(&output_count_lock);   
20   
21 if (count $< \equiv$ requested_number_of_records)   
22 print_record(record_ptr):   
23 return (count);   
24 1

这个程序段从数据库的一部分中找到一项，更新全局计数器，然后再找下一项。如果一个锁定-更新计数-解锁循环所需的时间为t，找到一个匹配数的时间为t，那么总的查找时间就是 $( t _ { 1 } + t _ { 2 } ) \times n _ { m a x }$ ，其中 $\pmb { n _ { m a x } }$ 是任一线程找到的最大匹配数目。如果 $t _ { 1 }$ 与 $t _ { 2 }$ 相当，那么锁将导致可观的开销。

用pthread_mutex_trylock函数能减少锁开销。每个线程现在寻找下一项，并试图得到锁并更新计数。如果另一个线程已经得到了锁，则把记录插入本地列表中，而线程能继续查找其他匹配的数。当线程最终得到锁时，就把到目前为止在本地找到的所有项插入到列表中（只要这个数目不超过所需要的数目）。相应的output_record函数如下：

1 int output_record(struct database_record \*record_ptr){   
2 int count;   
3 int lock_status;   
4 lock_status = pthread_mutex_trylock(&output_count_lock):   
5 if (lock_status $\approxeq$ EBUSY）{   
6 insert_into_local_list(record_ptr);   
7 return(0);   
8 ）   
9 else{   
10 count output_count;   
1 output_count ${ \boldsymbol { \mathbf { \mathit { \Phi } } } } + { \boldsymbol { \mathbf { \mathit { \varepsilon } } } } =$ number_on_local_list + 1;   
12 pthread_mutex_unlock(&output_count_lock) ;   
13 print_records(record_ptr，local_list,   
14 requested_number_of_records - count);   
15 return(count $^ +$ number_on_local_list $\star$ 1）；   
16 ！   
17

编程须知认真研究这个函数发现，如果更新全局计数的锁不可用，则函数将当前记录插入到-个本地列表中并返回；如果锁可用，则先将本地列表中的记录数目加到全局计数中，并再加1（代表当前记录)。然后再解除相关的锁，并用函数print_records打印要求的记录。

性能须知这个版本代码比前面的代码的执行时间短，原因有两点：第一，前面也已提到，执行pthread_mutex_trylock的时间通常比执行pthread_mutex_lock的时间少得多。第二，由于每个锁可能有多个记录插入，锁操作的数目也减少了。实际查找的记录数目（经过所有线程）可能要比真正需要的记录数目略微大一点（因为在本地列表中可能有的项永远不会被打印)。然而，由于这个时间原本该是花在锁空闲上的，这种开销不会造成性能降低。

上面的例子说明用函数pthread_mutex_trylock而不用pthread_mutex_lock的原因。通常pthread_mutex_trylock函数用来减少与互斥锁相关的空闲开销。如果计算中临界段可以被延迟，其他的计算可以在这个间歇期进行，那么pthread_mutex_trylock将是选择的函数。另一个前面也曾提到过的关键因素是，对于绝大多数的实现而言，函数pthread_mutex_trylock比函数pthread_mutex_lock开销更小。事实上，对于高度优化的代码，即使需要使用函数pthread_mutex_lock，通常也需要在循环内部使用函数pthread_mutex_trylock，因为如果在最初的几次调用中获得了锁，使用pthread_mutex_trylock也会比pthread_mutex_lock开销小。 □

# 7.5.2用于同步的条件变□

如上一节提到的，不加区别地使用锁可能导致由阻塞线程引起的空闲开销。虽然函数pthread_mutex_trylock减少这种开销，却带来对可用锁轮询的开销。例如，如果重写生产者-消费者的例子用函数pthread_mutex_trylock而不用pthread_mutex_lock,那么生产者和消费者就必须周期性地轮询锁的可用性（以及随后的缓冲区空间或队列中任务的可用性)。解决此问题的一个自然方法是，中止生产者的执行，直到空间变为可用（使用中断驱动机制而不是轮询机制)。空间的可用性由消费任务的消费者线程给出信号。实现该功能要使用条件变量（condition variable）。“

条件变量是用来同步线程的数据对象。这个变量允许某一线程阻塞自己，直到指定的数据到达预定的状态。在生产者-消费者例子中，对消费者线程给出信号前，共享变量task_available必须变成l。布尔条件task_available==1称为一个谓词，某一条件变量与这个谓词对应。如果谓词为真，条件变量就用来给出信号表示一个或多个等待条件的线程。一个条件变量可与多个谓词对应。但是，由于这样会造成程序难以排错，强烈建议不要这样做。

一个条件变量总是有一个互斥锁与之对应。一个线程锁定这个互斥锁并测试对共享变量（在这种情况下对task_available）定义的谓词；如果谓词非真，则线程等待与使用函数pthread_cond_wait的谓词相关的条件变量。这个函数的原型如下:

1 int pthread_cond_wait (pthread_cond_t \*cond,   
2 pthread_mutex_t \*mutex);

对此函数的调用阻塞线程的执行，直至线程收到来自另一个线程的信号或者被一个操作系统的信号中断。除了阻塞线程外，函数pthread_cond_wait解除对互斥锁的锁定。这一点非常重要，否则没有其他线程能够对共享变量task_available进行操作，且谓词永远不会满足。当线程在得到信号被释放后，在恢复执行前等待重新获得互斥锁。把每个条件变量想象成与--个队列联系是方便的。执行对变量条件等待的线程放弃它们的锁并进入队列。当条件发出信号（使用函数pthread_cond_sign）时，队列中的线程之一便解除阻塞，并在互斥锁变为可用时，它就被送给这个线程（线程变成可运行的)。

在上面的生产者-消费者例子中，生产者线程产生任务，由于对互斥锁的锁定已被放弃（通过等待消费者），生产者线程能够将任务插入到队列中，并在锁定互斥锁后置task_available为1。由于谓词得到满足，生产者必须通过发出信号来唤醒消费者线程之。这是用函数pthread_cond_signal实现的，函数的原型如下:

函数至少对当前等待条件变量cond的一个线程解除阻塞。然后生产者通过显式调用函数pthread_mutex_unlock放弃对互斥锁的锁定，使被阻塞的消费者线程之一消费任务。

在用条件变量重写生产者-消费者例子前，需要介绍两个初始化及消除条件变量的函数调用，分别为pthread_cond_init及pthread_cond_destroy。这两个函数调用的原型如下：

1 int pthread_cond_init(pthread_cond_t \*cond,   
2 const pthread_condattr_t \*attr);   
3 int pthread_cond_destroy(pthread_cond_t \*cond) ;

函数pthread_cond_init初始化一个条件变量（由cond指向），其属性由属性对象attr定义。将attr置为NULL对条件变量赋予默认的属性。如果在程序的某处，条件变量不再是需要的，可以用函数pthread_cond_destroy将它废弃。有了这两个处理条件变量的函数，就可以重写生产者-消费者程序段如下：

# 例7.6使用条件变量的生产者-消费者程序

条件变量在工作队列满时，可用来阻塞生产者线程的执行，而在工作队列为空时，可用来阻塞消费者线程的执行。两个条件变量cond_queue_empty和cond_queue_full分别用来指定空和满的队列。与cond_queue_empty相关的谓词为task_available==0,与cond_queue_full相关的谓词为task_available $\mathbf { \lambda } = \mathbf { \lambda } \mathbf { 1 }$ 。

生产者队列锁定与共享变量task_available对应的互斥锁task_queue_cond_lock。它检查task_available是否为0（即队列为空)。如果为空，生产者就将任务插人到工作队列中，并通过给出条件变量cond_queue_ful1的信号唤醒所有等待的消费者线程。然后继续创建其他的任务。如果task_available为1（即队列是满的)，生产者对条件变量cond_queue_empty执行条件等待（即等待队列变空）。此时，不难看出隐式解除对task_queue_cond_lock的锁定的原因。如果没有解除锁定，所有的消费者都不能消费任务，队列永远也不会变空。此时，生产者线程被阻塞。由于消费者可获得锁，消费者线程可以消费任务，并在任务从工作队列除去时给出条件变量cond_queue_empty的信号。

消费者线程锁定互斥锁task_queue_cond_lock，检查共享变量task_available是否为1。如果不是，它就执行对condqueue_full的条件等待。（注意，信号是在任务插入到工作队列时从生产者处产生的。）如果有任务可用，消费者将任务从工作队列中取出并发送信号给生产者。以这种方式，生产者和消费者线程通过彼此发信号进行操作。不难看出，这种操作方式与基于中断的操作类似，但不同于pthread_mutex_trylock基于轮询的操作。完成这种生产者-消费者行为的程序段如下：

1 pthread_cond_t cond_queue_empty， cond_queue_full;   
2 pthread_mutex_t task_queue_cond_lock;   
3 int task_available;   
4   
5 /\* other data structures here \*/   
6   
7 main(）{   
8 /\* declarations and initializations \*/   
9 task_available = 0;   
10 pthread_init();   
1 pthread_cond_init(&cond_queue_empty，NULL) :   
12 pthread_cond_init(&cond_queue_fuil, NULL) ;   
13 pthread_mutex_init(&task_queue_cond_lock，NULL) ;   
14 /\* create and join producer and consumer threads \*/   
15 1   
16   
17 void \*producer(void \*producer_thread_data) (   
18 int inserted;   
19 while （idone(））{   
20 create_task():   
21 pthread_mutex_lock(&task_queue_cond_lock);   
22 while (task_available $\ l = \ 1$ ） pthread_cond_wait (&cond_queue_empty, &task_queue_cond_lock); insert_into_queue(); task_availabie $\mathbf { \lambda } = \mathbf { \lambda } \mathbf { 1 }$ ；   
27 pthread_cond_signal(&cond_queue_full) ; pthread_mutex_unlock(&task_queue_cond_lock);   
1   
void \*consumer(void \*consumer_thread_data) { while （idone()）{ pthread_mutex_lock (&task_queue_cond_lock) ; while (task_available == 0) pthread_cond_wait(&cond_queue_full,   
37 &task_queue_cond_lock);   
38 my_task $\ P$ extract_from_queue();   
39 task_available = 0;   
40 pthread_cond_signal(&cond_queue_empty) ;   
41 pthread_mutex_unlock(&task_queue_cond_lock);   
42 process_task(my_task) :   
43 ！   
44 1

编程须知在这个代码段中，有一点要特别注意：对与条件变量相关的谓词的检查是在循环内进行的。可能有人会认为，当cond_queue_full被断定时，task_available的值必定为1。但是，对条件的检查最好在循环内进行，因为线程可能会由于其他的原因（如OS信号）被唤醒。在其他情况下，如果条件变量通过条件广播发出信号（对所有等待的线程发出信号而不只是对一个线程)，较早得到锁的线程就会使条件无效。当有多个生产者及消费者时，一个队列中可用的任务可能要被其他的消费者之一消费。

性能须知当线程执行条件等待时，它将自己从可运行列表中移走一一因此，在它唤醒前不会使用CPU周期。这一点与互斥锁相反，互斥锁在轮询锁时要消耗CPU周期。 □

在上面的例子中，每个任务只能被一个消费者线程消费。因此，我们每次选择向一个阻塞的线程发信号。在某些其他的计算中，唤醒所有等待条件变量的线程而不是单个线程可能会有利。这一点可以通过函数pthread_cond_broadcast实现。

lint pthread_cond_broadcast (pthread_cond_t \*cond);

这样做的一个例子是在生产者-消费者程序中，工作队列很大，在每个插入周期都有多个任务要插入到工作队列。这一问题留给读者作为习题（习题7.2）。使用函数pthread_cond_broadcast的另-个例子是7.8.2节所述的实现障碍。

在条件等待时设置超时通常是很有用的。使用函数pthread_cond_timedwait，线程就能执行等待条件变量，直至指定的时间届满。此时，如果线程没有收到信号或广播，就会被自己唤醒。这个函数的原型为：

1 int pthread_cond_timedwait (pthread_cond_t \*cond,   
2 pthread_mutex_t \*mutex,   
3 const struct timespec \*abstime):

如果在收到信号或广播前，指定的绝对时间abstime届满，函数返回一个出错信息。当函数成为可用时，它也会重新获得互斥锁。

# 7.6控制线程及同步的性

到目前为止的讨论中，我们发现，像线程及同步变量这样的实体通常都与几种属性有关。例如，不同线程的调度方式可能也不同（如循环调度、优先调度，等等)，堆栈的大小可能也不一样，等等。同样，像互斥锁这样的同步变量也可能有多种不同的类型。Pthreads API允许程序员用属性对象（atributeobject）改变实体的默认属性。

属性对象是一个数据结构，用来描述实体（线程、互斥锁、条件变量）的性质。在创建线程或同步变量时，可以指定决定实体性质的属性对象。一旦创建，线程或同步变量的性质就大体上固定了（Pthreads允许用户改变线程的优先权），以后对属性对象的修改不能改变先于用属性对象创建的实体的性质。使用属性对象的好处有：第一，它将程序语义与实现分开。线程的性质由用户指定。这些性质在系统层次如何实现对于用户来说是透明的。这样就能使程序在不同操作系统间有更大的可移植性。第二，使用属性对象增强程序的模块性及可读性。第三，它使程序员修改程序更容易。比如，如果用户想对所有线程的调度从循环调度形式改为时间片调度形式，他们只需改变属性对象中的指定属性。

要创建具备要求性质的属性对象，首先必须创建带有默认性质的对象，然后按要求修改对象。下面我们考查为线程和同步变量完成属性对象创建的Pthreads函数。

# 7.6.1线程的性对象

函数pthread_attr_init用来创建线程的属性对象。此函数的原型如下：

int 2 pthread_attr_init ( 3 pthread_attr_t \*attr);

这个函数用默认值初始化属性对象attr。初始化成功后，函数返回0，否则返回一个错误代码。属性对象可用函数pthread_attr_destroy取消，这个函数的原型如下:

1 int   
2 pthread_attr_destroy (   
3 pthread_attr_t \*attr);

成功地取消属性对象attr后，函数的调用返回0。与属性对象有关的各个性质可用如下的函数修改:pthread_attr_setdetachstate,pthread_attr_setguardsize_np, pthread_attr_setstacksize,pthread_attr_setinheritsched,pthread_attr_setschedpolicy和pthread_attr_setschedparam。这些函数分别用来设置线程属性对象的分离状态、堆栈保护大小、堆栈大小、调度策略是否从创建线程继承、调度策略（在未继承的情况下）以及调度参数。读者可以参考Pthreads手册了解这些函数的详细描述。对于绝大多数并行程序而言，通常默认的线程性质就够用了。

# 7.6.2互斥锁的属性对象

Pthreads API支持三种不同的锁。对这三种锁的锁定和解锁使用同样的函数；然而，锁的类型由锁属性决定。到目前为止的例子中用到的互斥锁称为正常互斥锁（normalmutex）。这是一种默认类型的锁。在任意时刻，只允许一个线程锁定互斥锁。如果获得锁的线程试图再一次锁定它，则第二次锁定调用将导致死锁。

考虑下面在二叉树中搜索元素的线程例子。为了保证在搜索过程中其他的线程不改变树，线程使用一个互斥锁tree__lock锁定树。搜索函数如下:

1 search_tree(void \*tree_ptr)   
2 {   
3 struct node \*node_pointeri   
4 node_pointer = (struct node \*) tree_ptr;   
5 pthread_mutex_lock(&tree_lock) :   
6 if (is_search_node(node_pointer) $\ r = \ r _ { 1 }$ ）{   
7 /\* solution is found nere \*/   
8 print_node(node_pointer);   
9 pthread_mutex_unlock(&tree_lock);   
10 return(1);   
1 ！   
12 else{   
13 if (tree_ptr -> left $\downarrow =$ NULL)   
14 Bearch_tree((void $\bigstar$ )tree_ptr -> left);   
15 if (tree_ptr -> right $\ ! =$ NULL)   
16 Bearch_tree((void $\bigstar$ )tree_ptr -> right);   
17   
18 printf("Search unsuccessful\n") :   
19 pthread_mutex_unlock(&tree_lock);   
20 ！

如果tree_lock是正常互斥锁，则第一个对函数search_tree的递归调用将导致死锁，因为已获得锁的线程试图锁定一个互斥锁。为了解决这个问题，Pthreads API支持一种递归互斥锁（recursivemutex）。递归互斥锁允许单一的线程多次锁定互斥锁。线程每次锁定一个互斥锁时，锁计数器加1，每次解锁计数器减1。如果其他任何线程想成功锁定一个递归互斥锁，锁计数器必须为0（即每一个被其他线程的锁定必须有一个对应的解锁)。当线程函数需要递归地调用自已时，就要用到递归互斥锁。

除了正常及递归互斥锁以外，PthreadsAPI还支持第三种互斥锁，称为错误检查互斥锁(errorcheckmutex）。错误检查互斥锁的操作与正常互斥锁相似——一个线程只能锁定一个互斥锁一次。然而，与正常互斥锁不同，当线程试图锁定一个已经锁定的互斥锁时，错误检查丘斥锁将返回-一个错误而不是死锁。因此，错误检查互斥锁在排错时更有用。

五斥锁的类型可用互斥锁属性对象来指定。为了对默认值创建和初始化一个互斥锁属性对象，Pthreads提供函数pthread_mutexattr_init。这个函数的原型如下：

int 2 pthread_mutexattr_init ( 3 pthread_mutexattr_t \*attr):

这个函数创建并初始化一个互斥锁属性对象attr，互斥锁的默认类型为正常互斥锁。Pthreads提供函数pthread_mutexattr_settype_np用来设置由互斥锁属性对象指定的类型。这个函数的原型如下：

1 int.   
2 pthread_mutexattr_settype_np (   
3 pthread_mutexattr_t \*attr,   
4 int type);

这里，·type指定互斥锁的类型，与正常、递归和错误检查这三种互斥锁的类型相对应，它可以取下述值：

· PTHREAD_MUTEX_NORMAL_NP · PTHREAD_MUTEX_RECURSIVE_NP · PTHREAD_MUTEX_ERRORCHECK_NP

用函数pthread_attr_destroy可以取消互斥锁属性对象，函数以互斥锁属性对象attr作为唯一参数。

# 7.7线程注销

考虑在象棋比赛中用来对一系列位置进行估值的一个简单程序。假设有k次移动，每次移动由一个独立的线程估值。如果在任意时刻，某一位置确立具有某个品质，那么对其他已知品质差的位置必须停止估值。换句话说，对相应棋盘位置进行估值的线程必须被注销。POSIX线程用函数pthread_cancel提供线程注销功能。这个函数的原型如下：

1 int   
2 pthread_cancel (   
3 pthread_t thread);

这里，thread是要被注销线程的句柄。一个线程可以注销自己，也可以注销其他线程。调用此函数后，注销就发送给指定的线程，但不能保证指定的线程一定会收到注销，也不能保证指定的线程执行注销。线程可以保护自己不被注销。当真正执行注销时，调用清理函数恢复线程数据结构。这一过程与调用函数pthread_exit终止线程类似。对线程的注销独立于发送原来注销请求的线程。函数pthread_cancel在注销发送后返回，而注销操作可能推迟执行。注销成功时返回0，但并不代表请求的线程已被注销；这仅说明指定的线程是有效的注销线程。

# 7.8 复合同步结构

虽然Pthreads API提供了一系列基本的同步结构，但是经常需要更高层次的结构。这些较高

层次的结构可以用基本同步结构来构造。在本节中，将考查这些结构以及它们的性能和应用。

# 7.8.1读-写锁

在许多应用程序中，某一数据结构会被频繁地读出，但很少写入。对于这种情况，多读可以在不带来任何一致性问题的情况下进行。然而，写必须被串行化。这就引出了另一种结构一一读写锁。正在读共享数据项的线程获得对变量的读出锁，如果其他线程已经有了读出锁，则读出锁就被授与。如果存在对数据的写人锁（或者有排队的写入锁)，线程将执行条件等待。同样，如果有多个线程请求写入锁，这些线程也必须执行条件等待。我们使用这些原则设计读出锁函数mylib_rwlock_rlock、写人锁函数mylib_rwlock_wlock以及解锁函数mylib_rwlock_unlock。

所述的读-写锁基于一种称为mylib_rwlock_t的数据结构。这种结构含有读出者的数量、写人者（0/1整数表示写人者是否存在）、读出者能进行时发出的条件变量readers_proceed信号、写入者能进行时发出的条件变量writer_proceed信号、挂起的写人者计数器pending_writes以及与共享数据结构相对应的互斥锁read_write_lock。函数mylib_rwlock_init用来对这个数据结构的不同分量进行初始化。

函数mylib_rwlock_rlock试图对数据结构加上读出锁。它检查是否有写入锁或挂起的写入者。如果有，就执行对条件变量readers_proceed的条件等待，否则读出者计数器加1，并授与-个读出锁。函数mylib_rwlock_wlock试图对数据结构加上写入锁。它检查是否有读出者或写入者；如果有，挂起的写入者计数器加1，并执行对条件变量writer_proceed的等待。如果没有读出者或写人者，就授予一个写人锁并继续。

函数mylib_rwlock_unlock解除读出锁或写人锁。它检查是否存在写入锁，如果有，该函数就会通过设置writer的字段为0为数据结构解锁。如果有读出者存在，读出者readers的数量减1。如果没有剩余的读出者，但有挂起的写入者，函数发出写入者之一继续的信号（通过发出writer_proceed信号)。如果没有挂起的写入者，但有挂起的读出者，则函数发出所有读出者线程继续的信号。初始化和锁定/解锁的代码如下：

1 typedef struct {   
2 int readers;   
3 int writer;   
4 pthread_cond_t readers_proceed;   
5 pthread_cond_t writer_proceed;   
6 int pending_writers:   
7 pthread_mutex_t read_write_lock;   
8 )mylib_rwlock_t;   
9   
10   
11 void mylib_rwlock_init (mylib_rwlock_t \*1){   
12 1 -> readers = 1 -> writer = 1 -> pending_writers = 0;   
13 pthread_mutex_init(&(l -> read_write_lock), NULL);   
14 pthread_cond_init (&(l -> readers_proceed), NULL) ;   
15 pthread_cond_init(&(1 -> writer_proceed), NULL);   
16   
17   
18 void mylib_rwlock_rlock(mylib_rwlock_t $^ { \star 1 }$ ）{   
19 /\* if there is a write lock or pending writers, perform condition   
20 wait.. else increment count of readers and grant read lock \*/   
21   
2 pthread_mutex_lock(&(l -> read_write_lock));   
while ((l -> pending_writers > 0) Il (l -> writer > 0))   
pthread_cond_wait(&(l -> readers_proceed),   
25 &(1 -> read_write_lock));   
26 1 -> readers $\mathrel { + { + } }$ ；   
2 pthread_mutex_unlock(&(1 -> read_write_lock));   
  
29   
30   
31 void mylib_rwlock_wlock(mylib_rwlock_t \*1){   
32 /\* if there are readers or writers, increment pending writei   
33 count and wait. On being woken， decrement pending writers   
34 count and increment writer count \*/   
35   
36 pthread_mutex_lock(&(1 -> read_write_lock));   
37 while ((l -> writer > 0) Il (1 -> readers > 0)){   
38 1 -> pending_writers $^ { + \dagger }$   
39 pthread_cond_wait(&(l -> writer_proceed),   
40 &(1 -> read_write_lock)):   
41   
42 1 -> pending_writers --;   
43 1 -> writer ++   
44 pthread_mutex_unlock(&(1 -> read_write_lock));   
45   
46   
47   
48 void mylib_rwlock_unlock(mylib_rwlock_t \*1){   
49 /\* if there is a write lock then unlock, else if there are   
50 read locks, decrement count of read locks. If the count   
is O and there is a pending writer， let it through， else   
if there are pending readers, let them all go through \*/   
pthread_mutex_lock(&(l -> read_write_lock));   
if (l -> writer > 0)   
1 -> writer = 0;   
else if (l -> readers > 0)   
58 1 -> readere --;   
59 pthread_mutex_unlock(&(l -> read_write_lock));   
60 if ((l -> readers == O) && (1 -> pending_writers > 0))   
61 pthread_cond_signal(&(l -> writer_proceed)) ;   
62 else if (l -> readers > 0)   
63 pthread_cond_broadcast(&(l -> readers_proceed)):   
64

下面用一些例子说明读-写锁的用法。

# 例7.7用读-写锁计算一个数字列表中的最小数

计算一个数字列表中的最小值是读-写锁的一个简单应用。在前面的实现中，一个锁与最小值相关。所有线程在需要的时候锁定并更新最小值。通常，检查最小值的次数要大于最小值更新的次数。因此，好的方法是用读出锁允许多次读，只在需要时在写入锁后写入。相应的程序段如下：

1 void \*find_min_rw(void \*list_ptr){   
2 int \*partial_1ist_pointer,my_min,i;   
3 my_min $\approx$ MIN_INT:   
4 partial_list_pointer = (int \*) list_ptr;   
5 for (i = 0; i.< partial_list_size; i++)   
6 if (partial_list_pointer{i] < my_min)   
7 my_min = partial_list_pointer[i];   
8 /\* lock the mutex associated with minimum_value and   
9 update the variable as required \*/   
10 mylib_rwlock_rlock(&read_write_lock);   
11 if (my_min < minimum_value){   
12 mylib_rwlock_unlock(&read_write_lock);   
13 mylib_rwlock_wlock(&read_write_lock);   
14 minimum_value $\Bumpeq$ my_min;   
15   
16 /\* and unlock the mutex \*/   
17 mylib_rwlock_unlock(&read_write_lock);   
18 'pthread_exit(0);   
19

编程须知在本例中，每个线程计算自己部分列表中的最小元素。然后试图对与全局最小值对应的锁加上读出锁。如果全局最小值大于本地最小值（这样就需要一次更新)，则放弃读出锁，寻找写入锁。一旦获得写入锁，就能更新全局最小值。从读-写锁得到的性能增益受线程数量及所需更新（写人锁）数量的影响。在极端的情况下，全局最小值中的第一个值也是真正的最小值，就不用再寻找写人锁。此时，这种使用读-写锁的版本的程序性能较好。相反，如果每个线程必须更新全局最小值，就会有过多的读出锁，增加程序的开销。 □

# 例7.8用读-写锁实现散列表

在从数据库查询到状态空间搜索这样的应用程序中，一个常见的操作是从数据库中搜索-个关键码，数据库按散列表组织。在本例中，假设通过将冲突的项链接成链表来处理冲突。每个链表有一个锁与之对应。锁保证不会在同时对链表更新和查找。这里我们考虑两种程序版本：一种使用互斥锁，另一种使用本节中介绍的读-写锁。

使用互斥锁的程序版本将关键码散列到表中，锁定与表索引对应的互斥锁，并在链表中进行搜索/更新。实现这个操作的线程函数如下：

1 manipulate_hash_table(int entry){   
2 int table_index，found;   
3 struct 1ist_entry \*node， \*new_node:   
4   
5 table_index $\Lleftarrow$ hash(entry):   
6 pthread_mutex_lock(&hash_table[table_index] .1ist_lock);   
7 found = 0;   
8 node $\Bumpeq$ hash_table[table_index] .next;   
9 while ((node $\downarrow =$ NULL)&& （!found)）{   
10 if (node -> value $u = =$ entry)   
1 found $\ l \equiv \ \ l \ 1$ i   
12 else   
13 node node -> next:   
14   
15 pthread_mutex_unlock(&hash_table[table_index] .list_lock);   
16 if (found)   
17 return(1):   
18 else   
19 insert_into_hash_table(entry);   
20

这里，函数insert_into_hash_table在进行实际插人前必须锁定hash_table[table_index].list_lock。当在散列表中发现大部分查询时（即它们不需要被插入）,这些搜索就会被串行化。容易看出，可以安全地允许多个线程搜索散列表，只有对表的更新必须被串行化。这样就能用读-写锁来实现。函数manipulate_hash_table可以重写如下：

1 manipulate_hash_table(int entry)   
2   
3 int table_index，found;   
4 struct list_entry \*node， \*new_node;   
5   
6 table_index $=$ hash(entry);   
7 mylib_rwlock_rlock(&hash_table[table_index].list_lock);   
8 found $\qquad = \ 0$ ；   
9 node $\approx$ hash_table[table_index].next;   
10 while ((node $\mathrel { \mathop : } =$ NULL）&& （!found)）{   
11 if (node -> value $\approx =$ entry)   
12 found $\textbf { \textit { \textbf { \_ } } 1 }$ ；   
13 else   
14 node $=$ node -> next;   
15 ！   
16 mylib_rwlock_rlock(&hash_table[table_index].list_lock);   
17 if (found)   
18 return(1):   
19 else   
20 insert_into_hash_table(entry);   
21 ！

这里，函数insert_into_hash_table在进行实际插入前必须得到hash_table[table_index].list_lock的写入锁。

编程须知在这个例子中，假设list_lock字段已被定义为类型mylib_rwlock_t,并且所有与散列表相关的读-写锁已用函数mylib_rwlock_init初始化。与使用互斥锁相比，使用mylib_rwlock_rlock允许多个线程并发地搜索各自的数据项。这样的话，如果成功的搜索次数超过插入次数，就能得到很好的性能。注意，函数insert_into_hash_table必须做适当的修改才能使用写入锁（而不是如像前面的互斥锁）。 □

弄清使用读-写锁优于使用正常锁的情况是很重要的。由于在写入时，读-写锁与正常互斥锁相比没有优势，只在有大量的读出操作时使用读-写锁才有利。此外，当临界段变大时，使用读-写锁的优势更大。这是因为，由正常互斥锁导致的串行化开销比较高。最后，由于读-写锁依赖条件变量，支撑的线程系统必须提供快速条件等待、发信号以及广播函数。通过对读-写锁做一个简单的分析，可以了解使用读-写锁的优点（习题7.7）。

# 7.8.2障碍

在线程化程序（以及其他的并行程序）中，barrier（障碍）是重要且经常用到的结构。用障碍调用挂起一个线程，直至其他所有加入障碍的线程到达障碍。障碍可以用计数器、互斥锁以及条件变量实现。（障碍也可以只使用互斥锁实现，然而，这样的实现会引起繁忙等待的开销。）一个整数（计数器）用于记录到达障碍的线程数目，如果计数小于线程总数目，线程执行条件等待。最后进入的线程（将计数器设置为线程数目）使用条件广播唤醒所有的线程。完成这个过程的代码如下：

1 typedef struct {   
2 pthread_mutex_t count_lock;   
3 pthread_cond_t ok_to_proceed;   
4 int count:   
5 }mylib_barrier_t;   
6   
7 void mylib_init_barrier(mylib_barrier_t \*b){   
8 b -> count = 0;