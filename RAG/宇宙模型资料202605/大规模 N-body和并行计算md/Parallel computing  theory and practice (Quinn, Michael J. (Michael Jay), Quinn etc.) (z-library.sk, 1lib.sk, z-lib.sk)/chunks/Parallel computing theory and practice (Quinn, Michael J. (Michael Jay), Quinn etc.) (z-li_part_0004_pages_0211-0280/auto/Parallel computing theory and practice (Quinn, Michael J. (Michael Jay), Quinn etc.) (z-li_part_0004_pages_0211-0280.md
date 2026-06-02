![](images/740c60bb5d273bb36feca72165e2b68df92fff498bbdf67e500735dda27919a5.jpg)  
FIGURE 7-11 Speedup of parallel matrix multiplicationalgorithm onlightly loadedSequent Symmetry.The algorithm is multiplying two $2 5 6 \times 2 5 6$ floating-point matrices.

synchronize exactly once; synchronization overhead, then, is $\Theta ( p )$ .Hence the complexity of this parallel algorithm is $\Theta ( n ^ { 3 } / p + p )$ .Note that since there are only $n$ rows, at most $n$ processes may execute this algorithm. If we ignore memory contention, we can expect speedup to be nearly linear. Figure 7-11 plots the speedup achieved by a lightly loaded Sequent Symmetry multiplying a pair of $2 5 6 \times 2 5 6$ matrices containing floating-point numbers.

Is it realistic to ignore memory access times? Yes, it is often possible to do so on UMA multiprocessors,where every global memory cellis an equal distance from every processor. But it is dangerous to ignore memory access times on loosely coupled multiprocessors,where some matrix elements may be much easier to access than others. Recall that on loosely coupled multiprocessors it is important to keep local as many memory references as possible. The algorithm illustrated in Fig. 7-10 does not do this well. Indeed, not only must a typical process access $n / p$ rows of A, but also it must access every element of $\textbf { B } n / p$ times! Only a single addition and a single multiplication occur for every element of B fetched. This is not a good ratio. Implementation of this algorithm on a BBN TC200O would yield poor speedup.

Another method must be found to partition the problem. One attractive method is to take advantage of block matrix multiplication. Assume that A and $\mathbf { B }$ are both $n \times n$ matrices,where $n = 2 k$ .Then $\mathbf { A }$ and $\mathbf { B }$ can be thought of as conglomerates of four smaller matrices,each of size $k \times k$ ：

$$
{ \bf A } = \left( \begin{array} { l l } { { A _ { 1 1 } } } & { { A _ { 1 2 } } } \\ { { A _ { 2 1 } } } & { { A _ { 2 2 } } } \end{array} \right) \qquad { \bf B } = \left( \begin{array} { l l } { { B _ { 1 1 } } } & { { B _ { 1 2 } } } \\ { { B _ { 2 1 } } } & { { B _ { 2 2 } } } \end{array} \right)
$$

Given this partitioning of $\mathbf { A }$ and $\mathbf { B }$ into blocks, $\mathbf { C }$ is defined as follows:

$$
\mathbf { C } = { \left( \begin{array} { l l } { C _ { 1 1 } } & { C _ { 1 2 } } \\ { C _ { 2 1 } } & { C _ { 2 2 } } \end{array} \right) } = { \left( \begin{array} { l l } { A _ { 1 1 } B _ { 1 1 } + A _ { 1 2 } B _ { 2 1 } } & { A _ { 1 1 } B _ { 1 2 } + A _ { 1 2 } B _ { 2 2 } } \\ { A _ { 2 1 } B _ { 1 1 } + A _ { 2 2 } B _ { 2 1 } } & { A _ { 2 1 } B _ { 1 2 } + A _ { 2 2 } B _ { 2 2 } } \end{array} \right) }
$$

If we assign processes to do the block matrix multiplications, then the number of multiplications and additions per matrix-element fetch increases. For example, assume that there are $p = ( n / k ) ^ { 2 }$ processes. Then the matrix multiplication is performed by dividing A and $\mathbf { B }$ into $p$ blocks of size $k \times k$ .Each block multiplication requires $2 k ^ { 2 }$ memory fetches, $k ^ { 3 }$ additions, and $k ^ { 3 }$ multiplications. The number of arithmetic operations per memory access has risen from 2,in the previous algorithm, to $k = n / \sqrt { p }$ ,in the new algorithm, a significant improvement. An example of this block matrix approach to parallel matrix multiplication is shown in Fig. 7-12.

Ostlund, Hibbard,and Whiteside (1982) have implemented this matrix multiplication algorithm on $\mathbf { C m ^ { * } }$ for various matrix sizes. The results of their experiment are shown in Fig. 7-13.

Design Strategy 6 Reduce average memory latency time by increasing locality.

The block matrix multiplication aIgorithm performs beter on the NUMA multiprocessor because it increases the number of computations performed per nonlocal memory fetch. For similar reasons,a careful choice of block sizes to maximize the cache hit-rate can yield a sequential block-oriented matrix multiplicationalgorithm that executes faster than the traditional algorithm illustrated in Fig. 7-1.

FIGURE 7-12 Block-matrix approach to paralel-matrix multiplication.

$$
\begin{array} { r l r } { \left( \begin{array} { c c c c } { 1 } & { 0 } & { 2 } & { 3 } \\ { 4 } & { - 1 } & { 1 } & { 5 } \\ { - 2 } & { - 3 } & { - 4 } & { 2 } \\ { - 1 } & { 2 } & { 0 } & { 0 } \end{array} \right) \left( \begin{array} { c c c c } { - 1 } & { 1 } & { 2 } & { - 3 } \\ { - 5 } & { - 4 } & { 2 } & { - 2 } \\ { 3 } & { - 1 } & { 0 } & { 2 } \\ { 1 } & { 0 } & { 4 } & { 5 } \end{array} \right) } & { = } & { \left( \begin{array} { c c c c } { 8 } & { - 1 } & { 1 4 } & { 1 6 } \\ { 9 } & { 7 } & { 2 6 } & { 1 7 } \\ { 7 } & { 1 4 } & { - 2 } & { 1 4 } \\ { - 9 } & { - 9 } & { 2 } & { - 1 } \end{array} \right) } \end{array}
$$

STEP 1: Compute C,j= A,1 B1,j

$$
\begin{array} { r l r } { ( \begin{array} { c c } { 1 } & { 0 } \\ { 4 } & { - 1 } \end{array} ) ( \begin{array} { c c } { - 1 } & { 1 } \\ { - 5 } & { - 4 } \end{array} ) _ { 1 } ^ { \top } ( \begin{array} { c c } { 1 } & { 0 } \\ { 4 } & { - 1 } \end{array} ) ( \begin{array} { c c } { 2 } & { - 3 } \\ { 2 } & { - 2 } \end{array} ) } & { = } & { ( \begin{array} { c c c } { - 1 } & { 1 } & { | \begin{array} { c c } { 2 } & { - 3 } \\ { 1 } & { 0 } & { | \begin{array} { c c } { 4 } & { - 1 0 } \\ { - - 4 - - 3 } & { - - 4 - 2 } \\ { 1 7 } & { 1 0 } & { 1 } \end{array} | } } \\ { - 1 } & { 2 } \end{array} ) _ { 1 } ^ { \top } ( \begin{array} { c c } { - 2 } & { - 3 } \\ { - 1 } & { 2 } \end{array} ) ( \begin{array} { c c } { 2 } & { - 3 } \\ { 2 } & { - 2 } \end{array} ) } \\ { ( \begin{array} { c c } { - 2 } & { - 3 } \\ { - 1 } & { 2 } \end{array} ) ( \begin{array} { c c } { - 1 } & { 1 } \\ { - 5 } & { - 4 } \end{array} ) _ { 1 } ^ { \top } ( \begin{array} { c c } { - 2 } & { - 3 } \\ { - 1 } & { 2 } \end{array} ) ( \begin{array} { c c } { 2 } & { - 3 } \\ { 2 } & { - 2 } \end{array} ) } & { = } &  ( \begin{array} { c c c } { - 1 } & { 1 } &  | \begin{array} { c c } { 2 } & { - 3 } \\ { 1 } & { 8 } & { | \begin{array} { c c } { 4 } & { - 1 0 } \\ { - 1 } & { - 4 - 3 } & { - 1 0 } \\ { 1 7 } & { 1 0 } & { 1 2 } & { 1 2 } \\ { - 9 } & { - 9 } & { | \begin{array} { c c } { 1 } & { 2 } & { - 1 } \end{array} | } \end{array} ) } \end{array} \end{array} \end{array} \end{array}
$$

STEP 2:Compute C,j=Ci,j +A,2B2,j

$$
\begin{array} { r l r } { \left( \begin{array} { l l } { 2 } & { 3 } \\ { 1 } & { 5 } \\ { 1 } & { 5 } \end{array} \right) \left( \begin{array} { l l } { 3 } & { - 1 } \\ { 1 } & { 0 } \\ { 1 } & { - 0 } \end{array} \right) \left( \begin{array} { l l } { 2 } & { 3 } \\ { 1 } & { 5 } \end{array} \right) \left( \begin{array} { l l } { 0 } & { 2 } \\ { 4 } & { 5 } \end{array} \right) } & { = } & { \left( \begin{array} { l l l l } { 8 } & { - 1 } & { 1 4 } & { 1 6 } \\ { 9 } & { 7 } & { 2 6 } & { 1 7 } \\ { - - - - - - - - - - - } \\ { 7 } & { 1 4 } & { - 2 } & { 1 4 } \\ { 9 } & { 9 } \end{array} \right) } \\ { \left( \begin{array} { l l } { 4 } & { 0 } \end{array} \right) \left( \begin{array} { l l } { 3 } & { - 1 } \\ { 1 } & { 0 } \end{array} \right) \left( \begin{array} { l l } { - 4 } & { 2 } \\ { 0 } & { 0 } \end{array} \right) \left( \begin{array} { l l } { 0 } & { 2 } \\ { 4 } & { 5 } \end{array} \right) } & { = } & { \left( \begin{array} { l l l l } { 9 } & { - 1 } & { 1 4 } & { 1 6 } \\ { 9 } & { - 1 } & { 1 } & { 1 6 } \\ { - 9 } & { - 9 } & { 1 } & { 2 } & { - 1 } \end{array} \right) } \end{array}
$$

![](images/fc8718cee2d0436a25f6f8cb9652fdc9a8d2b8f3eb327d51dd82278a5943b468.jpg)

# 7.4 ALGORITHMS FOR MULTICOMPUTERS

# 7.4.1 Row-Column-Oriented Algorithm

Let's consider how we can parallelize the standard sequential matrix multiplication algorithm. Multiplying two $n \times n$ matrices A and $\mathbf { B }$ involves the computation of $n ^ { 2 }$ dot products. Each dot product operation is between a row of A and a column of B. Given that at any moment in time every matrix element must be stored in the local memory of exactly one processor, it is natural to partition A into rows and B into columns. Assume that $n$ is a power of two and we are executing the algorithm on an $n$ -processor hypercube.

The triply nested for loop of the serial algorithm is shown in Fig. 7-14a. To maximize grain size we want to parallelize the outmost for loop. A straightforward parallelization of the outer loop would demand that all parallel processes first access column O of $^ { b }$ , then column 1 of $^ { b }$ ,etc.This results in a sequence of broadcast steps, each having complexity $\Theta ( \log n )$ on a $n$ -processor hypercube.

Contention for shared resources can dramatically lower the performance of a parallel algorithm. In the case of a multiprocessor, too much contention for the same memory bank is called a hot spot. On a multicomputer, the processor that controls the variable must broadcast its value to the other processors. If the order in which the processors access the data items is unimportant, we can rewrite the parallel algorithm to eliminate the contention.

Design Strategy 7 Eliminate contention for shared resources by changing temporal order of data accesses.

Let's apply this strategy to the matrix multiplication problem. If we change the order in which the algorithm computes the elements of each row of $c$ (Fig.7-14b), then it is only one more jump to reach an efcient parallel algorithm (Fig. 7-14c).

In this solution, the processes are organized as a ring. After each process has used its current column of $^ b$ ,it fetches the next column of $^ { b }$ from its successor

(a) Original sequential code segment:

for $i \gets 0$ to $n - 1$ do for $j \gets 0$ to $n - 1$ do $t ~ \gets ~ 0$ for $k \gets 0$ to $n - 1$ do $t ~  ~ t ~ + ~ a [ i ] [ k ] ~ \times ~ b [ k ] [ j ]$ endfor $c [ i ] [ j ] \ \gets \ t$ endfor   
endfor

(b) After changing the access order:

for $i \gets 0$ to $n - 1$ do for $j \gets i$ to $i + n - 1$ do $\textit { m } \gets \textit { j }$ modulo $n$ $t ~ \gets ~ 0$ for $k \gets 0$ to $n - 1$ do $t ~  ~ t ~ + ~ a [ i ] [ k ] ~ \times ~ b [ k ] [ m ]$ endfor $c [ i ] [ m ] \ \gets \ t$ endfor   
endfor

(c) After parallelization:

for all $P _ { i }$ ,where $0 ~ \leq ~ i ~ < ~ n$ do for $j \gets i$ to $i + n - 1$ do $t ~ \gets ~ 0$ for $k \gets 0$ to $n - 1$ do $t ~  ~ t ~ + ~ a [ k ] ~ \times ~ b [ k ]$ endfor $c [ ( j )$ modulo $n ]  t$ $b [ 0 . . . ( n - 1 ) \ \in \ s u c c e s s o r ( b [ 0 . . . ( n - 1 ) ] )$ endfor   
endfor

on the ring. Because we can embed a ring in a hypercube with dilation 1 using Gray codes, each message can be sent in time ?(1),compared to the (log n) time needed to perform each broadcast.

Now let's generalize our solution. Suppose we are multiplying an l × m and an m ×n matrix on p processors, where p < l and p <n. Assume l and n are integer multiples of p.Each processor begins with a contiguous set of l/p rows of A and a contiguous set of n/p columns of B and multiplies the (l/p) × m submatrix of A with the m × (n/p) submatrix of B, producing a (l/p) × (n/p)

submatrix of the product matrix (see Fig. 7-15). Then every processor passes its piece of $\mathbf { B }$ to its successor processor. Again each processor multiplies its piece of A with its piece of B (Fig.7-15b). After $p$ iterations,ach rocesor has multiplied its piece ofA with every pieceofB,buildinga $( l / p ) \times n$ section of the product matrix.

How many computations and communications are performed by the processors? We will let thenumber of multiplications serveas the measure of computational effort. During every iteration each processor multiplies an $( l / p ) \times m$ matrix by an $m \times ( n / p )$ matrix, passes the $m \times ( n / p )$ matrix to its ring successor,and receives an $m \times ( n / p )$ matrix from its ring predecessor. Hence, every iteration requires $( l / p ) m ( n / p )$ computational steps. Making the standard assumption that sending or receiving a message has message latency $\lambda$ plus message transmission time $\beta$ times the number of values sent, every iteration has communication time $2 ( \lambda + m ( n / p ) \beta )$ .Over $p$ iterations, the total number of computational steps is $( l / p ) m ( n / p ) p = l m n / p$ and the total communication time is $2 ( p \lambda + m n \beta )$

This algorithm achieves reasonable performance on hypercube multicomputers.Figure 7-16 illustrates the speedup achieved by a parallel implementation of the algorithm on the nCUBE 3200.

As the number of processors increases,a scrutiny of this algorithm's performance reveals two related deficiencies that point us to an improved algorithm. First, notice that the communication time increases linearly with the number of processors. Second, notice that the number of computations performed per iteration is inversely proportional to the number of processors used.

# 7.4.2 Block-Oriented Algorithm

To improve the efficiency of the multicomputer-targeted matrix multiplication algorithm, we want to maximize the number of multiplications performed per iteration. This is done by keeping the submatrices as square as possible.

Once again we are to multiply an $l \times m$ matrix $\mathbf { A }$ by an $m \times n$ matrix $\mathbf { B }$ Assume that $l , m$ ,and $n$ are integer multiples of $\sqrt { p }$ ,where $p$ is an even power of 2.We organize the processors as a two-dimensional mesh with wraparound connections, and give each processor a $( l / { \sqrt { p } } ) \times ( m / { \sqrt { p } } )$ subsection of A and a $( m / \sqrt { p } ) \times ( n / \sqrt { p } )$ subsection of $\mathbf { B }$

Having chosen this data allocation, a new matrix multiplication algorithm is a corollary of two results shown earlier this chapter. Recall that block matrix multiplication is performed analogously to scalar matrix multiplication; each occurrence of scalar multiplication is replaced by an occurrence of matrix multiplication. Also recall that we have found an efficient algorithm to multiply matrices on a two-dimensional mesh of processing elements. We use the same staggering technique to position the blocks of A and B,so that every processor multiplies two submatrices every iteration.

It is easy to show that every processor performs an equal number of multi-plications. To determine the communication time required, we take into account

![](images/317c20ce72a4287aa688608a4841b5d736eca989927af6d5f2f1a5fda5cf6bc4.jpg)

# FIGURE 7-15

First hypercube matrix multiplication algorithm.Matrix A is divided into p groups of contiguous rows;matrix B is divided into p groups of contiguous columns.The processors are organized asa ring.Each processor has one piece of A and one piece ofB.(a) First step of parallel algorithmassuming four processors.Each processor multiplies itsAsubmatrix withitsBsubmatrix，yieldingaportionofC.Eachproceor passes its portion of B to its predecessor on the ring of processors. (b) In step two, processors multiply matrices and pass elements of B.(c) Step three.(d) In step four there isno need to pass elements of B,unless we need to get them back to their starting place.When the algorithm is complete,each processor has computeda portion of C correspondng to the rows of A it controls.

![](images/3b1ce2cccf1dda2e927a66fe7511b6c35aeb08541775b7686703817a26a1f6af.jpg)  
FIGURE 7-16 Scaled speedup of two hypercubemulticomputermatrix multiplicationalgorithmson nCUBE3200.Bothalgorithms are multiplying a pair of $2 5 6 \times 2 5 6$ matrices containing floatingpoint numbers. The solid line corresponds to the firstalgorithm,and the dashed line corresponds to the second, block-orientedalgorithm.

that for each of $\sqrt { p } - 1$ iterations,every processor sends and receives a portion of matrix $\mathbf { A }$ and a portion of matrix B. In addition, both the staggering and unstaggering of matrices $\mathbf { A }$ and $\mathbf { B }$ require $\sqrt { p } / 2 - 1$ iterations in which portions of A and $\mathbf { B }$ are sent and received. Unlike the SIMD algorithm, which requires $\sqrt { p } - 1$ iterations for the staggering and unstaggering steps, this MIMD algorithm requires $\sqrt { p } / 2$ iterations, because some processing elements can move blocksof $\mathbf { A }$ to the right while other processing elements move blocks of A to the left,and some processing elements can move blocks of $\mathbf { B }$ down while other processing elements move blocks of $\mathbf { B }$ up. No block begins more than $\sqrt { p } / 2$ moves away from its staggered position. Hence the total communication time is

$$
\begin{array} { r l r } {  { ( 2 \sqrt { p } - 1 ) ( 2 ( \lambda + ( l / \sqrt { p } ) ( m / \sqrt { p } ) \beta + \lambda + ( m / \sqrt { p } ) ( n / \sqrt { p } ) \beta ) ) } } \\ & { } & \\ & { = } & { 2 ( 2 \sqrt { p } - 1 ) ( \lambda + [ ( m / \sqrt { p } ) ( ( l / \sqrt { p } ) + ( n / \sqrt { p } ) ) ] \beta ) } \end{array}
$$

Figure 7-16 illustrates the speedup achieved by the second hypercube matrix multiplication algorithm.

Both the block-oriented algorithm and the row-column-oriented algorithms require the same number of computation steps. When does the second algorithm require less communication time? Assume that we are multiplying two $n \times n$ matrices, where $n$ is an integer multiple of $p$ ·

$$
\begin{array} { r l } & { \quad 2 p \lambda + 2 n ^ { 2 } \beta > ( 2 \sqrt { p } - 1 ) 2 ( \lambda + ( n / \sqrt { p } ) ( 2 n / \sqrt { p } ) \beta ) } \\ & { \Rightarrow \quad p \lambda + n ^ { 2 } \beta > ( 2 \sqrt { p } - 1 ) ( \lambda + ( 2 n ^ { 2 } / p ) \beta ) } \\ & { \Rightarrow \quad p \lambda + n ^ { 2 } \beta > ( 2 \sqrt { p } - 1 ) \lambda + ( 4 n ^ { 2 } / \sqrt { p } - 2 n ^ { 2 } / p ) \beta } \end{array}
$$

It is easy to determine that $p \ge 2 \sqrt { p } - 1$ for all $p \geq 1$ and $n ^ { 2 } \geq ( 4 n ^ { 2 } / \sqrt { p } -$ $2 n ^ { 2 } / p )$ for all $p \geq 1 6$ (Recall our analysis assumes $p$ must be an even power of 2.) It follows that the block-oriented matrix multiplication algorithm is uniformly superior to the row-column-oriented algorithm when the number of processors is an even power of 2 greater than or equal to 16.

# 7.5 SUMMARY

Gentleman (1978) has shown that multiplying two $n \times n$ matrices on the 2-D mesh SIMD model has complexity $\Omega ( n )$ ,and we have derived amatrix multiplication algorithm for the 2-D mesh SIMD model that achieves this lower bound. Dekel et al. (1981) have devised efficient routing algorithms allowing $n ^ { 3 } = 2 ^ { 3 q }$ processing elements on either a hypercube SIMD or a shuffle-exchange SIMD model to multiply two $n \times n$ matrices in $\Theta ( \log n )$ time.

Matrix multiplication provides many different opportunities for parallelization on UMA multiprocessors. Developing an efficient matrix multiplication algorithm for the NUMA multiprocessor model is complicated by the nonhomogeneous memory structure. Reshaping the algorithm to use block matrix multiplication increases the ratio of arithmetic operations to nonlocal memory accesses and leads to a more efficient algorithm. Examining parallel algorithms for the hypercube multicomputer model, we found that the algorithm based upon a block decomposition of the matrices scaled better than the algorithm based upon a row-column decomposition.

Our study of matrix multiplication on MIMD computers yielded three more parallel algorithm design strategies:

5 If load balancing is not a problem, maximize grain size. 6 Reduce average memory latency time by increasing locality. 7 Eliminate contention for shared resources by changing temporal order of data accesses.

# 7.6 BIBLIOGRAPHIC NOTES

All the matrix multiplication algorithms presented in this chapter are parallelizations of the most common sequential algorithm. Multicomputer matrix multiplication algorithms using the row-column decomposition have been published in many places, including Organick (1985). A parallelization of Strassen's algorithm appears in Chandra (1976).

Ramakrishnan and Varman (1984) have designed an optimal algorithm for performing matrix multiplication on theone-dimensional mesh-connected SIMD model.

The block-oriented matrix multiplication algorithm described in this chapter has been published by variousauthors,including Berntsen(1989).

Hwang and Cheng (1982) have designed a VLSI block matrix multiplication algorithm that ilustrates how matrices can be multiplied when there are far fewer processing elements than matrix elements. VLSI algorithms used to perform matrix multiplication or related algorithms have also been published by Horowitz (1979),Kulkarni and Yen (1982),Leiserson (1983),andUlman (1984).

7-1 Write an $\Theta ( \log n )$ matrix multiplication algorithm for the CREW PRAM model. Assume that $n = 2 ^ { k }$ ,where $k$ is a positive integer.   
7-2 What is $\sigma ( k )$ for the hypercube SIMD model?   
7-3 Gentleman’s theorem assumes that every element of A and $\mathbf { B }$ is stored exactly once in the parallel computer and that no processing element contains more than one element of either matrix.Are these assumptions realistic? Explain.   
7-4 Add a postamble to the 2-D mesh SIMD matrix multiplication algorithm that unstaggers matrices A and $\mathbf { B }$ so that at the end of the algorithm $A ( i , j ) = a _ { i , j }$ ， $B ( i , j ) = b _ { i , j }$ and $C ( i , j ) = c _ { i , j }$   
7-5 Write a parallel algorithm that multiplies two $n \times n$ matrices in time $\Theta ( n )$ on the 2-D mesh SIMD model with no wraparound connections.Processing element $P ( i , j )$ has local variables $A ( i , j ) , B ( i , j )$ ,and $C ( i , j )$ .When the algorithm begins execution, $A ( i , j ) = a _ { i , j }$ and $B ( i , j ) = b _ { i , j }$ .After $\Theta ( n )$ steps, $C ( i , j ) = c _ { i , j }$ .No processing element should use more than a constant number of variables.   
7-6 Write a parallel algorithm that transposes an $n \times n$ matrix in time $\Theta ( n )$ on the 2- D mesh SIMD model with wraparound connections. Processing element $P ( i , j )$ has local variables $A ( i , j )$ and $T ( i , j )$ ,where $1 \leq i$ ， $j \leq n$ .When the algorithm begins execution, $A ( i , j ) = a _ { i , j }$ .After $\Theta ( n )$ steps, $T ( i , j ) = a _ { j , i }$ .No processing element should use more than a constant number of variables.   
7-7 Repeat the previous exercise with all assumptions identical, except that the model does not have wraparound connections.   
7-8 Determine the processor eficiency of the hypercube SIMD matrix multiplication algorithm as a function of the matrix dimension $_ n$   
7-9 If $p \leq n$ processors are available for matrix multiplication on a UMA multiprocessor,what would be the complexity of the algorithm resulting from parallelizing the middle for loop of the sequential algorithm? Would’ you expect this algorithm to achieve better or worse speedup than the algorithm presented in this book? Why?   
7-10 The block-oriented hypercube matrix multiplication algorithm has been outlined

for use when the number of processors is an even power of 2. Describe how to modify the algorithm so that it may execute on a hypercube of odd dimension.

# 8

The meeting of two personalities is like the contact of two chemical substances; if there isany reaction,bothare transformed.

Carl Gustav Jung,Modern Man in Search ofa Soul

The discrete Fourier transform has many applications in science and engineering. For example, it is frequently used in digital signal processing. A straightforward implementation of the discrete Fourier transform has time complexity $\Theta ( n ^ { 2 } )$ . The fast Fourier transform is an $\Theta ( n \log n )$ algorithm to perform the discrete Fourier transform,and it can be parallelized easily.

Section 8.1 summarizes what the discrete Fourier transform does in the context of one important application area-speech recognition. Section 8.2 is a formal presentation of the discrete Fourier transform and the inverse discrete Fourier transform. In Sec. 8.3 we present the fast Fourier transform algorithm and describe how to implement it on a hypercube multicomputer.

This chapter relies upon an understanding of complex numbers. Readers needing a refresher course in complex numbers will find a brief presentation in Appendix B.

# 8.1 INTRODUCTION

Fourier analysis studies the representation of continuous functions by a potentially infinite series of sinusoidal (sine and cosine) functions.We can view the discrete Fourier transform as a function that maps a sequence over time {f(k)} to another sequence over frequency {F(j)). The sequence {f(k)} represents a sampling of a signal's distribution as a function of time. The sequence {F(j)} represents a distribution of Fourier coeffcients as a function of frequency. We can use $\{ F ( j ) \}$ to compute the sinusoidal components of the sampled signal.

Figure 8-1 illustrates this process.We begin,inFig.8-1a, with a plotof {f(k)}， 16 samples of signal strength between time O and time 2π. Figure 8-1b is the plot of {F(j)},a sequence of 16 complex numbers representing the frequency distribution. From the nonzero elements of {F(j)) we candetermine thefrequencyof thetermsgeneratingtheignal,whrere quency means the number of complete cycles the wave completes between time O and time 2π . Nonzero real components correspond to cosine functions; nonzero imaginary components correspond to sine function. From Fig.8-1b we see that there are nonzero real components with frequency 2 and 5 and nonzero imaginary components with frequency 1 and 2. Hence the function generating the signal is of the form

$$
s _ { 1 } \sin x + c _ { 2 } \cos ( 2 x ) + s _ { 2 } \sin ( 2 x ) + c _ { 5 } \cos ( 5 x )
$$

For each frequency, divide the amplitude shown in the left half of Fig.8-1b by 8 (half of 16) to determine the coefficients of the various sinusoidal components. The frequency 1 component is 16i. Dividing 16 by 8 yields a coeficient of 2 for the function sin x. The frequency 2 component is -8- 16i. Dividing -8 by 8 yields a coeficient of $^ { - 1 }$ for the function $\cos ( 2 x )$ , just as the coefficient for the function $\sin ( 2 x )$ is $^ { - 2 }$ .We use the same method to calculate that 0.5 is the coefficient of the function cos(5x). The four terms generating the signal are

$$
2 \sin x - \cos ( 2 x ) - 2 \sin ( 2 x ) + 0 . 5 \cos ( 5 x )
$$

In Fig.8-1c we plot the four sinusoidal components and their sum,a continuous function,and inFig.8-1d we plot thecontinuous functionagainst the sampled data points.

The discrete Fourier transform has many applications in science and engineering. In this section we describe one such application-speech recognition by computer.

Most speech analysis has been done by studying the spectral parameters of the speech signal.

Decomposing complex speech signals into periodically recurrent sinusoidal components is the central activity of signal processing work,and is justified by (1) sinusoids being “natural signals” of linear physical (electronic) systems; (2) resonances being prominent cues to articulation configurations; (3) voice sounds being composed out of harmonics of the voice fundamental frequency;and (4) the ear appearing to do some form of spectral analysis.Also, sinusoids (and some other exponential signals) can be added ("superimposed") in linear systems without interfering with each other; thus the sinusoidal parts that we decompose the signal input into for frequency analysis act as independent, "orthogonal signals" (Lea 1980).

![](images/6eefda12dfaeb0cc01578345371550b87b0e3fa97aee03c80938a35c396ad3fd.jpg)  
FIGURE 8-1 Example of the discrete Fourier transform. (a) A set of 16 data points representing samples of signal strength in the time interval O to (but not through) $2 \pi$ .(b)Thediscrete Fourier transtorm yields theamplitudesand frequencies of the constituent sine and cosine functions.(c) Aplot of the four constituent functionsand their sum,a continuous function.(d) Aplot of the continuous functionand the original 16 samples.

The discrete Fourier transform can be used to transform digitized samples of human speech into two-dimensional plots (see Fig. 8-2). The graph shows detected frequencies as a function of time. Each narrow vertical strip shows the amplitudes of the detected frequencies as shades of gray.As the person talks, the speech signal changes, and so do the frequencies that make up the signal. Plots such as this can be used as inputs to speech recognition systems,which atempt to determine spoken phonemes through pattern recognition.

![](images/8867538efb9950d6e7859bb2db639f2d5748fe6b6d719eace0ec649592c771ad.jpg)  
FIGURE 8-2 Discrete Fourier transform of the waveform corresponding to "Angorra catsare furrier... Theupperportion plotsthestrengthof theinput signal asa function of time.The lower portionplotsfrequencyandamplitudeasafunctionoftime.Eachnarrowverticai strip representsthe discrete Fouriertransform of the waveformusingamoving $1 0 ~ \mathsf { m s }$ window withina3msincrement.Thedarker theplotat somevertical positionthehigher the amplitudeat that frequency.(Figure courtesy Ron Coleand Yeshwant Muthusamyof the OregonGraduate institute of Scienceand Technology.)

# 8.2 THE DISCRETE FOURIER TRANSFORM

Given an $n$ element vector $x$ ,the discrete Fourier transform (DFT) is the matrix-vector product $F _ { n } x$ ,where $f ( i , j ) = \omega _ { n } ^ { i j }$ for $0 \leq i , j < n$

For example, to compute the discrete Fourier transform of the vector $( 2 , 3 )$ ， we need to know $\omega _ { 2 }$ , the second primitive root of unity,which is $^ { - 1 }$ .The discrete Fourier transform of (2, 3) is

$$
\left( \omega _ { 2 } ^ { 0 \times 0 } \omega _ { 2 } ^ { 0 \times 1 } \right) \left( \begin{array} { c } { { x _ { 0 } } } \\ { { x _ { 1 } } } \end{array} \right) = \left( \begin{array} { c c } { { 1 } } & { { 1 } } \\ { { 1 } } & { { - 1 } } \end{array} \right) \left( \begin{array} { c } { { 2 } } \\ { { 3 } } \end{array} \right) = \left( \begin{array} { c } { { 5 } } \\ { { - 1 } } \end{array} \right)
$$

Now let's compute the discrete Fourier transform of the vector $( 1 , 2 , 4 , 3 )$ 1 We will need to use the fourth primitive root of unity, which is $i$

$$
\left( \begin{array} { c } { { \omega _ { 4 } ^ { 0 } \ \omega _ { 4 } ^ { 0 } \ \omega _ { 4 } ^ { 0 } \ \omega _ { 4 } ^ { 0 } } } \\ { { \omega _ { 4 } ^ { 0 } \ \omega _ { 4 } ^ { 1 } \ \omega _ { 4 } ^ { 2 } \ \omega _ { 4 } ^ { 3 } } } \\ { { \omega _ { 4 } ^ { 0 } \ \omega _ { 4 } ^ { 2 } \ \omega _ { 4 } ^ { 0 } \ \omega _ { 4 } ^ { 2 } } } \\ { { \omega _ { 4 } ^ { 0 } \ \omega _ { 4 } ^ { 3 } \ \omega _ { 4 } ^ { 2 } \ \omega _ { 4 } ^ { 1 } } } \end{array} \right) \left( \begin{array} { c } { { x _ { 0 } } } \\ { { x _ { 1 } } } \\ { { x _ { 2 } } } \\ { { x _ { 3 } } } \end{array} \right) = \left( \begin{array} { c c c c } { { 1 } } & { { 1 } } & { { 1 \ i \ i } } & { { 1 } } \\ { { 1 } } & { { i \ i } } & { { - 1 \ i } } & { { - i } } \\ { { 1 \ - 1 } } & { { 1 } } & { { - 1 } } \\ { { 1 \ - i \ - 1 } } & { { i } } \end{array} \right) \left( \begin{array} { c } { { 1 } } \\ { { 2 } } \\ { { 4 } } \\ { { 3 } } \end{array} \right) = \left( \begin{array} { c } { { 1 0 } } \\ { { - 3 - i } } \\ { { 0 } } \\ { { - 3 + i } } \end{array} \right)
$$

To get a better feel for the pattern of the exponents in the $F$ matrix, look at Fig. 8-3, which presents $F _ { 8 }$

Let's put the discrete Fourier transform to use by returning to the example presented in Sec. 8.1. We have a vector of 16 complex numbers representing signal strength in the time interval O to $2 \pi$ . To simplify the presentation we show each number to only 3 digits of accuracy:

The discrete Fourier transform of this vector is

$$
( 0 , 1 6 i , - 8 - 1 6 i , 0 , 0 , 4 , 0 , 0 , 0 , 0 , 4 , 0 , 0 , - 8 + 1 6 i , - 1 6 i )
$$

To determine the coefficients of the sine and cosine functions making up this signal,we examine the nonzero elements in the first half of the transformed sequence. (The terms at positions 9 through 15 are a reflection of the terms in positions 1 through 7,with the signs of the imaginary parts reversed.) If we begin counting at O, the real portion of term $k$ is 8 times the coefficient of the function $\cos ( k x )$ , and the imaginary portion of term $k$ is 8 times the coefficient of the function $\mathrm { s i n } ( k x )$ . (Eight is half the length of the transformed sequence.) Thus the combination of sine and cosine functions making up the curve is

$$
2 \sin ( x ) - \cos ( 2 x ) - 2 \sin ( 2 x ) + 0 . 5 \cos ( 5 x )
$$

# 8.2.1 Inverse Discrete Fourier Transform

Given an $n$ element vector $x$ , the inverse discrete Fourier transform is $1 / n \mathrm { t h }$ the matrix-vector product $F _ { n } ^ { - 1 } x$ ,where $f ^ { - 1 } ( i j ) = \omega _ { n } ^ { - i j }$ for $0 \leq i , j < n$ and $\omega _ { n }$ is the primitive $n$ th root of unity.

For example, the inverse discrete Fourier transform of the vector (10,-3-i, $0 , - 3 + i )$ is

$$
\frac { 1 } { 4 } \left( \begin{array} { c c c c } { { \omega _ { 4 } ^ { 0 } } } & { { \omega _ { 4 } ^ { 0 } } } & { { \omega _ { 4 } ^ { 0 } } } & { { \omega _ { 4 } ^ { 0 } } } \\ { { \omega _ { 4 } ^ { 0 } } } & { { \omega _ { 4 } ^ { - 1 } } } & { { \omega _ { 4 } ^ { - 2 } } } & { { \omega _ { 4 } ^ { - 3 } } } \\ { { \omega _ { 4 } ^ { 0 } } } & { { \omega _ { 4 } ^ { - 2 } } } & { { \omega _ { 4 } ^ { 0 } } } & { { \omega _ { 4 } ^ { - 2 } } } \\ { { \omega _ { 4 } ^ { 0 } } } & { { \omega _ { 4 } ^ { - 3 } } } & { { \omega _ { 4 } ^ { - 2 } } } & { { \omega _ { 4 } ^ { - 1 } } } \end{array} \right) \left( \begin{array} { c } { { x _ { 0 } } } \\ { { x _ { 1 } } } \\ { { x _ { 2 } } } \\ { { x _ { 3 } } } \end{array} \right) = \frac { 1 } { 4 } \left( \begin{array} { c c c c } { { 1 } } & { { 1 } } & { { 1 } } & { { 1 } } \\ { { 1 } } & { { - i } } & { { - 1 } } & { { i } } \\ { { 1 } } & { { - 1 } } & { { 1 } } & { { - 1 } } \\ { { 1 } } & { { i } } & { { - 1 } } & { { - i } } \end{array} \right) \left( \begin{array} { c } { { 1 0 } } \\ { { - 3 - i } } \\ { { 0 } } \\ { { - 3 + i } } \end{array} \right)
$$

$$
= \frac { 1 } { 4 } \left( \begin{array} { l } { 4 } \\ { 8 } \\ { 1 6 } \\ { 1 2 } \end{array} \right) = \left( \begin{array} { l } { 1 } \\ { 2 } \\ { 4 } \\ { 3 } \end{array} \right)
$$

# 8.2.2 Sample Application: Polynomial Multiplication

The discrete Fourier transform evaluates a polynomial at the $n$ complex nth roots of unity. Let $f ( x ) = a _ { n - 1 } x ^ { n - 1 } + a _ { n - 2 } x ^ { n - 2 } + \ldots + a _ { 1 } x + a _ { 0 }$ bea polynomial of degree $n - 1$ ,and let $\omega$ be the primitive nth root of unity. Then

$$
\left( \begin{array} { c } { { f ( \omega ^ { 0 } ) } } \\ { { f ( \omega ^ { 1 } ) } } \\ { { \cdots } } \\ { { f ( \omega ^ { n - 1 } ) } } \end{array} \right) = F \left( \begin{array} { c } { { a _ { 0 } } } \\ { { a _ { 1 } } } \\ { { \cdots } } \\ { { a _ { n - 1 } } } \end{array} \right)
$$

because $f ( \omega ^ { i } ) = a _ { 0 } + a _ { 1 } \omega ^ { i } + a _ { 2 } \omega ^ { 2 i } + \dots a _ { n - 1 } \omega ^ { ( n - 1 ) i }$ for $0 \leq i < n$

The inverse discrete Fourier transform takes the values of a polynomial a the $n$ complex nth roots of unity and produces the polynomial’s coefficients.

Suppose we want to multiply two polynomials

$$
p ( x ) = \sum _ { i = 0 } ^ { n - 1 } a _ { i } x ^ { i } \quad { \mathrm { a n d } } \quad q ( x ) = \sum _ { i = 0 } ^ { n - 1 } b _ { i } x ^ { i }
$$

The product of these two polynomials of degree $n - 1$ is the $( 2 n - 2 )$ degree polynomial

$$
p ( x ) q ( x ) = \sum _ { i = 0 } ^ { 2 n - 2 } \sum _ { j = 0 } ^ { i } a _ { j } b _ { i - j } x ^ { i }
$$

We can compute the coeficients of the resulting polynomial $p ( x ) q ( x )$ by convoluting the coefficient vectors of the original polynomials.

For example, to multiply the two polynomials

$$
\begin{array} { l } { { p ( x ) = 2 x ^ { 3 } - 4 x ^ { 2 } + 5 x - 1 } } \\ { { \qquad } } \\ { { q ( x ) = x ^ { 3 } + 2 x ^ { 2 } + 3 x + 2 } } \end{array}
$$

yielding

$$
r ( x ) = a _ { 6 } x ^ { 6 } + a _ { 5 } x ^ { 5 } + \cdot \cdot \cdot + a _ { 1 } x + a _ { 0 }
$$

we convolute the coefficient vectors:

$$
\begin{array} { r l } & { a _ { 6 } = 2 \times 1 = 2 } \\ & { a _ { 5 } = 2 \times 2 + ( - 4 ) \times 1 = 0 } \\ & { a _ { 4 } = 2 \times 3 + ( - 4 ) \times 2 + 5 \times 1 = 3 } \\ & { a _ { 3 } = 2 \times 2 + ( - 4 ) \times 3 + 5 \times 2 + ( - 1 ) \times 1 = 1 } \\ & { a _ { 2 } = ( - 4 ) \times 2 + 5 \times 3 + ( - 1 ) \times 2 = 5 } \\ & { a _ { 1 } = 5 \times 2 + ( - 1 ) \times 3 = 7 } \\ & { a _ { 6 } = ( - 1 ) \times 2 = - 2 } \end{array}
$$

resulting in

$$
f ( x ) = 2 x ^ { 6 } + 3 x ^ { 4 } + x ^ { 3 } + 5 x ^ { 2 } + 7 x - 2
$$

Another way to multiply two polynomials of degree $n - 1$ is to evaluate them atthe $n$ complex nth roots of unity, perform an element-wise multiplication of the polynomials’ values at these locations,and then interpolate the results to produce the coefficients of the product polynomial. Let’s apply this method to the previous example.

First we perform the discrete Fourier transform on the coeficients of $p ( x )$ We list the coefficients’ order from low to high. Since the polynomial has degree 3,the last four coefficients are O. To simplify the figure, we only show two digits beyond the decimal point.

$$
( \begin{array} { c c c c c } { { 1 } } & { { 1 } } & { { 1 } } & { { 1 } } & { { 1 } } & { { 1 } } \\ { { 1 } } & { { \omega ^ { 1 } } } & { { \omega ^ { 2 } } } & { { \omega ^ { 3 } } } & { { \omega ^ { 4 } } } & { { \omega ^ { 5 } } } & { { \omega ^ { 7 } } } \\ { { 1 } } & { { \omega ^ { 2 } } } & { { \omega ^ { 4 } } } & { { \omega ^ { 6 } } } & { { 1 } } & { { \omega ^ { 2 } } } & { { \omega ^ { 4 } } } \\ { { 1 } } & { { \omega ^ { 3 } } } & { { \omega ^ { 6 } } } & { { \omega ^ { 1 } } } & { { \omega ^ { 4 } } } & { { \omega ^ { 7 } } } & { { \omega ^ { 5 } } } \\ { { 1 } } & { { \omega ^ { 4 } } } & { { 1 } } & { { \omega ^ { 4 } } } & { { 1 } } & { { \omega ^ { 4 } } } & { { 1 } } \\ { { 1 } } & { { \omega ^ { 5 } } } & { { \omega ^ { 2 } } } & { { \omega ^ { 7 } } } & { { \omega ^ { 4 } } } & { { \omega ^ { 1 } } } & { { \omega ^ { 6 } } } \\ { { 1 } } & { { \omega ^ { 6 } } } & { { \omega ^ { 4 } } } & { { \omega ^ { 2 } } } & { { 1 } } & { { \omega ^ { 6 } } } & { { \omega ^ { 2 } } } \\ { { 1 } } & { { \omega ^ { 7 } } } & { { \omega ^ { 6 } } } & { { \omega ^ { 5 } } } & { { \omega ^ { 4 } } } & { { \omega ^ { 3 } } } & { { \omega ^ { 2 } } } \end{array} ) ( \begin{array} { c } { { - 1 } } \\ { { 5 } } \\ { { - 4 } } \\ { { 2 } } \\ { { 0 } } \\ { { 0 } } \\ { { 0 } } \\ { { 0 } } \end{array} ) = ( \begin{array} { c } { { 2 } } \\ { { 1 . 1 2 + . 9 5 i } } \\ { { 3 + 3 i } } \\ { { - 3 . 1 2 + 8 . 9 5 i } } \\ { { - 1 . 1 2 + 8 . 9 5 i } } \\ { { - 1 . 1 2 - 8 . 9 5 i } } \\ { { - 3 . 1 2 - 8 . 9 5 i } } \\   \end{array}
$$

Next we perform the discrete Fourier transform on thecoefficients of $q ( x )$ Again, we are only showing two digits beyond the decimal point.

$$
( \begin{array} { c c c c c c } { { 1 } } & { { 1 } } & { { 1 } } & { { 1 } } & { { 1 } } & { { 1 } } & { { 1 } } \\ { { 1 } } & { { \omega ^ { 1 } } } & { { \omega ^ { 2 } } } & { { \omega ^ { 3 } } } & { { \omega ^ { 4 } } } & { { \omega ^ { 5 } } } & { { \omega ^ { 7 } } } \\ { { 1 } } & { { \omega ^ { 2 } } } & { { \omega ^ { 4 } } } & { { \omega ^ { 6 } } } & { { 1 } } & { { \omega ^ { 2 } } } & { { \omega ^ { 4 } } } & { { \omega ^ { 6 } } } \\ { { 1 } } & { { \omega ^ { 3 } } } & { { \omega ^ { 6 } } } & { { \omega ^ { 1 } } } & { { \omega ^ { 4 } } } & { { \omega ^ { 7 } } } & { { \omega ^ { 5 } } } \\ { { 1 } } & { { \omega ^ { 4 } } } & { { 1 } } & { { \omega ^ { 4 } } } & { { 1 } } & { { \omega ^ { 4 } } } & { { 1 } } & { { \omega ^ { 4 } } } \\ { { 1 } } & { { \omega ^ { 5 } } } & { { \omega ^ { 2 } } } & { { \omega ^ { 7 } } } & { { \omega ^ { 4 } } } & { { \omega ^ { 1 } } } & { { \omega ^ { 6 } } } & { { \omega } } \\ { { 1 } } & { { \omega ^ { 6 } } } & { { \omega ^ { 4 } } } & { { \omega ^ { 2 } } } & { { 1 } } & { { \omega ^ { 6 } } } & { { \omega ^ { 4 } } } & { { \omega ^ { 1 } } } \\ { { 1 } } & { { \omega ^ { 7 } } } & { { \omega ^ { 6 } } } & { { \omega ^ { 5 } } } & { { \omega ^ { 4 } } } & { { \omega ^ { 3 } } } & { { \omega ^ { 2 } } } & { { \omega ^ { 1 } } } \end{array} ) ( \begin{array} { c } { { 2 } } \\ { { 3 } } \\ { { 2 } } \\ { { 1 } } \\ { { 0 } } \\ { { 0 } } \\ { { 0 } } \\ { { 0 } } \end{array} ) = ( \begin{array} { c } { { 8 } } \\ { { 3 . 4 1 + 4 . 8 3 i } } \\ { { 2 i } } \\ { { . 5 9 + . 8 3 i } }  \end{array}
$$

Now we perform an element-wise multiplication of the two polynomials at these eight points.

$$
\left( \begin{array} { c } { 2 } \\ { 1 . 1 2 + . 9 5 i } \\ { 3 + 3 i } \\ { - 3 . 1 2 + 8 . 9 5 i } \\ { - 1 . 2 } \\ { - 3 . 1 2 - 8 . 9 5 i } \\ { 3 - 3 i } \\ { 1 . 1 2 - 9 5 i } \end{array} \right) \left( \begin{array} { c } { 8 } \\ { 3 . 4 1 + 4 . 8 3 i } \\ { 2 i } \\ { 5 9 + . 8 3 i } \\ { 0 } \\ { . 5 9 - . 8 3 i } \\ { - 2 i } \\ { 3 . 4 1 - 4 . 8 3 i } \end{array} \right) = \left( \begin{array} { c } { 1 6 } \\ { - . 7 6 + 8 . 6 6 i } \\ { - . 6 + 6 i } \\ { - 9 . 2 5 + 2 . 6 6 i } \\ { 0 } \\ { - 9 . 2 5 - 2 . 6 6 i } \\ { - 6 - 6 i } \\ { - . 7 6 - 8 . 6 6 i } \end{array} \right)
$$

In the final step we perform the inverse discrete Fourier transform on the product vector:

$$
\frac { 1 } { 8 } \left( \begin{array} { c c c c c } { 1 } & { 1 } & { 1 } & { 1 } & { 1 } & { 1 } \\ { 1 } & { \omega ^ { 7 } } & { \omega ^ { 6 } } & { \omega ^ { 5 } } & { \omega ^ { 4 } } & { \omega ^ { 3 } } & { \omega ^ { 2 } } & { \omega ^ { 1 } } \\ { 1 } & { \omega ^ { 6 } } & { \omega ^ { 4 } } & { \omega ^ { 2 } } & { 1 } & { \omega ^ { 6 } } & { \omega ^ { 4 } } & { \omega ^ { 2 } } \\ { 1 } & { \omega ^ { 5 } } & { \omega ^ { 2 } } & { \omega ^ { 7 } } & { \omega ^ { 4 } } & { \omega ^ { 1 } } & { \omega ^ { 6 } } & { \omega ^ { 3 } } \\ { 1 } & { \omega ^ { 4 } } & { 1 } & { \omega ^ { 4 } } & { 1 } & { \omega ^ { 4 } } & { 1 } & { \omega ^ { 4 } } \\ { 1 } & { \omega ^ { 3 } } & { \omega ^ { 6 } } & { \omega ^ { 1 } } & { \omega ^ { 4 } } & { \omega ^ { 7 } } & { \omega ^ { 2 } } & { \omega ^ { 5 } } \\ { 1 } & { \omega ^ { 2 } } & { \omega ^ { 4 } } & { \omega ^ { 6 } } & { 1 } & { \omega ^ { 2 } } & { \omega ^ { 4 } } & { \omega ^ { 6 } } \\ { 1 } & { \omega ^ { 1 } } & { \omega ^ { 2 } } & { \omega ^ { 3 } } & { \omega ^ { 4 } } & { \omega ^ { 5 } } & { \omega ^ { 6 } } \end{array} \right) \left( \begin{array} { c } { 1 6 } \\ { - 7 6 + 8 . 6 6 i } \\ { - 6 + 6 i } \\ { - 9 . 2 5 + 2 . 6 6 i } \\ { - 9 . 2 5 } \\ { 0 } \\ { - 9 . 2 5 - 2 . 6 6 i } \\ { - 6 . 6 6 i } \\ { - 7 6 - 8 . 6 6 i } \end{array} \right) = \left( \begin{array} { c } { - 2 } \\ { 7 } \\ { 5 } \\ { 1 } \\ { 3 } \\ { 0 } \\ { 2 } \\ { 0 } \end{array} \right)
$$

The vector produced by the inverse discrete Fourier transform contains the coeffcients of the product polynomial in order from low to high. In other words,

$$
r ( x ) = 2 x ^ { 6 } + 3 x ^ { 4 } + x ^ { 3 } + 5 x ^ { 2 } + 7 x - 2
$$

# 8.3 THE FAST FOURIER TRANSFORM

At the end of Sec. 8.2 we demonstrated how we can use the discrete Fourier transform and inverse discrete Fourier transform to multiply two polynomials.Why would we use this complicated algorithm to perform convolutions or multiply polynomials,when it can be done directly in time $\Theta ( n ^ { 2 } ) ?$ Because we do not have to perform the discrete Fourier transform and inverse discrete Fourier transform using matrix-vector multiplication. An algorithm with time complexity $\Theta ( n \log n )$ exists, and it is amenable to parallelization. The improved algorithm is called the fast Fourier transform (FFT).

The fast Fourier transform uses a divide-and-conquer strategy to evaluate a polynomial of degree $n$ at the $n$ complex nth roots of unity. To evaluate $f ( x )$ ， a polynomial of degree $n$ where $n$ is a power of 2, the algorithm defines two new polynomials of degree $n / 2$ ：

$$
\begin{array} { l } { { f ^ { [ 0 ] } ( x ) = a _ { 0 } + a _ { 2 } x + a _ { 4 } x ^ { 2 } + \cdot \cdot \cdot + a _ { n - 2 } x ^ { n / 2 - 1 } } } \\ { { \nonumber } } \\ { { f ^ { [ \mathrm { i } ] } ( x ) = a _ { 1 } + a _ { 3 } x + a _ { 5 } x ^ { 2 } + \cdot \cdot \cdot + a _ { n - 1 } x ^ { n / 2 - 1 } } } \end{array}
$$

Function $f ^ { [ 0 ] } ( x )$ contains the elements of $f ( x )$ associated with the even powers of $x$ ，while function $f ^ { [ 1 ] } ( x )$ contains the elements associated with the odd powers of $x$

Note that $f ( x ) = f ^ { [ 0 ] } ( x ^ { 2 } ) + x f ^ { [ 1 ] } ( x ^ { 2 } )$ , so the problem of evaluating $f ( x )$ at the points $\omega _ { n } ^ { 0 }$ ， $\omega _ { n } ^ { 1 }$ ..， $\omega _ { n } ^ { n - 1 }$ reduces to evaluating $f ^ { [ 0 ] }$ and $f ^ { [ 1 ] }$ at $( \omega _ { n } ^ { 0 } ) ^ { 2 }$ ， $( \omega _ { n } ^ { 1 } ) ^ { 2 }$ ， ...， $( \omega _ { n } ^ { n - 1 } ) ^ { 2 }$ ,and then computing $f ( x ) = f ^ { [ 0 ] } ( x ^ { 2 } ) + x f ^ { [ 1 ] } ( x ^ { 2 } )$ ·

Halving lemma. If $n$ is an even positive number,then the squares of the $n$ complex nth roots of unity are identical to the $\dot { n } / 2$ complex $( n / 2 ) \mathrm { t h }$ roots of unity.

Proof. The proof of the halving lemma appears in Appendix B.

By the halving lemma, we know that the set of points $( \omega _ { n } ^ { 0 } ) ^ { 2 }$ ， $( \omega _ { n } ^ { 1 } ) ^ { 2 }$ ， $( \omega _ { n } ^ { n - 1 } ) ^ { 2 }$ consists of only $n / 2$ unique values.Inother words,toevaluate the polynomial $f ( x )$ at the $n$ complex nth roots of unity we need only evaluate the polynomials $f ^ { [ 0 ] } ( x )$ and $f ^ { [ 1 ] } ( x )$ at the $n / 2$ complex $( n / 2 )$ th roots of unity.

A recursive implementation of the fast Fourier transform algorithm appears in Fig.8-4. The analysis of the algorithm is straightforward.Let $T ( n )$ denote the time neededtoperform the fast Fourier transformonapolynomial of degree $n$ ,where $n$ is a power of 2.

$$
\begin{array} { c } { { T ( n ) = 2 T \left( { \frac { n } { 2 } } \right) + \Theta ( n ) } } \\ { { { } } } \\ { { = \Theta ( n \log n ) } } \end{array}
$$

A carefully written iterative version of the FFT algorithm eliminates the second evaluation of ωkyl1l[k] every iteration of the for loop and requires fewer index computations. The resulting algorithm, adopted from Cormen et al. (1990)and presented inFig.8-5,is the basis for our parallelalgorithm.

Figure 8-6 illustrates how the FFT algorithm combines the elements of the original sequence.Thedataftow patternought tolook familiar; itisidentical to a butterfly network. For this reason a multicomputer with either a butterfly or hypercube processororganization is ideally suited toexecutetheFFTalgorithm.

RECURSIVE.FFT $( a , n )$ Parameter $_ n$ {Number of elements in a} $a [ 0 . . . ( n - 1 ) ]$ {Coefficientsof polynomial tobe evaluated) Local $\omega _ { n }$ {Primitiventhroot of unity) {Evaluatepolynomial here] $a ^ { [ 0 ] }$ {Even-numberedcoefficients] $a ^ { [ 1 ] }$ {Odd-numbered coefficients] y {Result of transform} y[0] {Result of FFT of $a ^ { [ 0 ] }$ y[1] {Result of FFT of $a ^ { [ 1 ] }$   
begin if $n \ = \ 1$ then return $^ a$ else $\begin{array} { r l } { \omega _ { n } } & { \gets ~ e ^ { 2 \pi \mathit { \omega } i / n } } \\ { \omega } & { \gets ~ 1 } \\ { a ^ { [ 0 ] } ~ \gets ~ ( a [ 0 ] , ~ a [ 2 ] , ~ \dots , ~ a [ n - 2 ] ) } \\ { a ^ { [ 1 ] } ~ \gets ~ ( a [ 1 ] , ~ a [ 3 ] , ~ \dots , ~ a [ n - 1 ] ) } \\ { y ^ { [ 0 ] } ~ \gets \mathsf { R E C U R S I V E . F F T } \left( a ^ { [ 0 ] } \right) } \\ { y ^ { [ 1 ] } ~ \gets \mathsf { R E C U R S I V E . F F T } \left( a ^ { [ 1 ] } \right) } \end{array}$ for $k \gets 0$ to $n / 2 \mathrm { ~ - ~ } 1$ do $y [ k ] ~  ~ y ^ { [ 0 ] } [ k ] ~ + ~ \omega ~ y ^ { [ 1 ] } [ k ]$ $y [ k + n / 2 ] ~  ~ y ^ { [ 0 ] } [ k ] ~ - ~ \omega ~ y ^ { [ 1 ] } [ k ]$ $\omega ~  ~ \omega ~ \times ~ \omega _ { n }$ endfor return $y$ endif   
end

# 8.3.1 Implementation on a Hypercube Multicomputer

Let's use the efficient iterative algorithm as a starting point for writing a parallel FFT algorithm suitable for implementation on a hypercube multicomputer. We will assume that each of the $p$ processors begins the algorithm with a contiguous group of coeficients. For example, if $n = 1 6$ and $p = 4$ ，processor 0 has coefficients $a _ { 0 } , a _ { 1 } , a _ { 2 }$ and $a _ { 3 }$ ;processor 1 has coefficients $a _ { 4 }$ ， $a _ { 5 }$ ， $a _ { 6 }$ and $a _ { 7 }$ ， and so on. We also assume that at the end of the computation each processor will contain a contiguous group of output values corresponding to its set of input coefficients. In other words, the processor starting the computation with $a _ { i } , a _ { i + 1 } , \dotsc , { a _ { j } }$ must end the computation with $y _ { i } , y _ { i + 1 } , \ldots , y _ { j }$

We can draw a diagram that indicates the flow of data between the processors, to help us understand when we must insert message-passing calls into our parallel algorithm. When message passing is required, the diagram will also help us determine the communication pattern. Figure 8-7 is a communication

Parameter $n$ {Number of elements in a} $a [ 0 . . . ( n - 1 ) ]$ {Coefficients of polynomial to be evaluated} Local $A [ 0 . . . ( n - 1 ) ]$ {Coefficients in bit reverse order] $j$ {Iterates through lower half of butterfly} $k$ {Iterates through indices with same relative} {position} $m$ {Current butterfly width} $s$ {Iteration number} $t , \ u$ {Temporaries) $\omega$ {Evaluate polynomial here} $\omega _ { m }$ {Primitive mth root of unity} begin REVERSE.INDEX.BITS.AND.COPY $( a , A )$ for $s \gets 1$ to $\log ( n )$ do $\begin{array} { l } { m  2 ^ { s } } \\ { \omega _ { m }  e ^ { 2 \pi \ i / m } } \\ { \omega  1 } \end{array}$ for $j ~ \gets ~ 0$ to $m / 2 \mathrm { ~ - ~ } 1$ do for $k \gets j$ to $n - 1$ step $m$ do $\begin{array} { l } { t  \omega \times A [ k + m / 2 ] } \\ { u  A [ k ] } \\ { A [ k ]  u + t } \\ { A [ k + m / 2 ]  u - t } \end{array}$ endfor $\omega ~  ~ \omega ~ \times ~ \omega _ { m }$ endfor endfor end

pattern for the FFT computation where $n = 1 6$ and $p = 4$ .The original step in which the algorithm permutes the $a _ { i }$ 's requires an irregular communication. Every processor must send values to every other processor,and the individual coefficients are scatered.In this situation we shouldcalla routing library function that implements random write.

Once the processors have permuted the values of the $a _ { i } { \bf \ddot { s } } .$ ,then each processor can perform $\log n - \log p$ iterations of the FFT without communicating with another processor. During each of the final $\log p$ iterations, each processor must send a copy of allits partially computed results to one other processor and receive partially computed results from that processor as well. In the first such swap every processor trades values with the processor whose number is different in the least significant bit. In the next step the swaps are between processors whose numbers differ in the second least significant bit. In the last such swap, processors whose numbers differ in the most significant bit trade values. In other words,to perform the FFT every processor will,at some point, swap values across every dimension of the hypercube.

![](images/936fabe47fae5ca6af8d4691a3e0937151980e6ff7717b45db8396057b6678d1.jpg)  
FIGURE 8-6This diagram illustrates how the FFT algorithm manipulates a set of input coefficients $a _ { 0 }$ $a _ { 1 }$ $a _ { n - 1 }$ withcomplexrootsof unity $( \omega _ { 2 } ^ { 0 } , \omega _ { 4 } ^ { 0 } , \omega _ { 4 } ^ { 1 } ;$ etc.)togeeatee sequence $y _ { 0 }$ ， $y _ { 2 }$ 。···· $y _ { n - 1 }$ .(Courtesy Cormen et al.1990.)

With these processor communication requirements in mind, we construct the parallel algorithm. Every processor will control two arrays of complex values. The first array, $^ a$ ,contains a contiguous group of input coeficients.The second array, $y$ holds intermeiateues.Ateedof theomputationry contains a contiguous group of transformed values. The parallel algorithm has three phases. In the first phase the processors permute the a’s. Each processor must compute, for each element of $^ a$ ,its destination in the form of (processor number, index in $y$ ),and send its value of $^ { a }$ there. In the second phase the processors perform the first $\log n - \log p$ iterations of the FFT by performing the required multiplications,additions,and subtractions on complex numbers. No message passing is required. In the third phase the processors perform the final $\log p$ iterations of the FFT by swapping y’sand performing the requisite multiplications, additions, and subtractions.

![](images/ad6c63890f5823aab30ca68b7717069e3c70bcdc29834fc2f7a4f97dbc24c0b8.jpg)  
Imagine we want to implement an $n$ element FFT on a $p$ -processor hypercube multicomputer so that at the beginning of the computation every processor containsa contiguous set of input elements,and at the end of the computation every processor containsa contiguous set of output elements.The permutation of the input elements requiresarandom-write operation,the first log $n - 1 0 9 p$ iterations of the FFT require no interprocessor ommunicationandthelst $\log p$ iterationsrequire that everyprocessor swap copies of its valueswith a processor adjacent across some dimension of the hypercube. This figure ilustrates the case where $n = 1 6$ and $p = 4$

The paralel algorithm appears in Figs. 8-8a and 8-8b. Figure 8-9 displays the performance of the parallel algorithm transforming a 4096-element sequence on a 64-processor nCUBE 3200. The solid curve is the speedup achieved if the permutation time of the input values is included. The dashed curve is the speedup achieved if the permutation time is not taken intoaccount. As we can see,thespeedupissignificantly higher when the permutation time is not counted.

Global $_ n$ {Number of sample points] $p$ {Number of processors) Local $a [ 0 . . . ( n / p - 1 ) ]$ {Input elements) pos {power) $t [ 0 . . . ( n / p - 1 ) ]$ {Temporary values) $u [ 0 . . . ( n / p - 1 ) ]$ {Temporary values) $y [ 0 . . . ( n / p - 1 ) ]$ {Output elements) @m {Complex mth root of unity) {Power of complex mth root of unity) {Permute input elements) forall $P _ { i }$ ,where $0 ~ \leq ~ i ~ < ~ p$ do for $k \gets 0$ to $n / p \ - \ 1$ do $i d \  \ i \ \times ( n / p ) \ + \ k$ dest.processor REVERSE(id)/(n/p) dest.offset REVERSE(id)modulo $( n / p )$ [dest.processorlyldest.offset] $\iff a [ k ]$ endfor endfor {Perform iterations not requiring interprocessor communication] for $s \gets 1$ to $\log ( n / p )$ do $m \gets 2 ^ { s }$ @m←e2π i／m for all $P _ { i }$ ,where $0 ~ \leq ~ i ~ < ~ p$ do $\omega ~ \gets ~ 1$ for $j \gets 0$ to $m / 2 - 1$ do for $k \gets j$ to $n / p - 1$ step $m$ do $\begin{array} { l } { q  \omega \times y [ k + m / 2 ] } \\ { r  y [ k ] } \\ { y [ k ]  r + q } \\ { y [ k + m / 2 ]  r - q } \end{array}$ endfor $\omega ~  ~ \omega ~ \times ~ \omega _ { m }$ endfor endfor endfor

A parallelFFTalgorithm suitableforimplementationonahypercubemulticomputer (part 1 of 2).

The discrete Fourier transform plays an important role in many scientific and engineering applications.The fast Fourier transform algorithm is interesting for two reasons. First, it is an $\Theta ( n \log n )$ implementation of the discrete Fourier transform,inotrast toaiveimplementationich has imecomleity

Perform iterations requiring interprocessor communication}   
or $s \gets 1$ to $\log ( p )$ do   
m ←2s +l0g(n/p)   
Wm←e2π/m   
forall $P _ { i }$ ,where $0 ~ \leq ~ i ~ < ~ p$ do if $i ~ / ~ 2 ^ { s - 1 }$ is odd then pos $ \ ( i \ \times \ ( n / p ) )$ modulo $m / 2$ ω←e2（pos）π/m for $i \gets 0$ to $n / p - 1$ do $t [ i ]  \omega \times y [ i ]$ $\omega ~  ~ \omega ~ \times ~ \omega _ { m }$ endfor endif shift $ 2 ^ { s - 1 }$ partner $ k \otimes$ shift {Exclusive or} if $i ~ / ~ 2 ^ { s - 1 }$ is odd then [partner]ut else [partner]uy endif endfor for all $P _ { i }$ ,where $0 ~ \leq ~ i ~ < ~ p$ do if $i ~ / ~ 2 ^ { s - 1 }$ is odd then for $i \gets 0$ to $n / p - 1$ do $y [ i ] ~  ~ u [ i ] ~ - ~ t [ i ]$ endfor else for $i  0$ to $n / p - 1$ do $y [ i ] \  \ y [ i ] \ + \ u [ i ]$ endfor endif endfor   
endfor

$\Theta ( n ^ { 2 } )$ . Second, the fast Fourier transform is amenable to parallelization on computers supporting the appropriate data-access paterns.

In this chapter we have presented the discrete Fourier transform algorithm and shown how a set of discrete data samples can be modeled by a continuous function, which is the sum of sine and cosine functions. We have described the inverse discrete Fourier transform and have shown how the discrete Fourier transformand inverse discrete Fourier transform can be used to multiply poly nomials. We have developed recursive and iterative versions of the fast Fourier transform algorithm, and we have demonstrated one way to implement the fast Fourier transform on a hypercube multicomputer.

![](images/413b2848a42eb63c1824acea44d243860fb509312e126e3d343bf81eb3ce6839.jpg)  
FIGURE 8-9 Speedup_achieved by the parallel FFTalgorithmon a 64-processor nCUBE 3200 hypercubemulticomputer,when the input sequence has 4096 elements.The solid speedup curve takes into account time spent permuting the input values; the dashed speedup curve assumes values are input inbit-reverseorder.

# 8.5 BIBLIOGRAPHIC NOTES

Introductions in computer science texts to the sequential fast Fourier transform algorithmincludeoooftdUan974);ase(978); al. (1990);and Horowitz and Sahni (1978). Another presentation of the parallel fast Fourier transform is Leighton (1992).

Early papers describing parallel FFTalgorithms include Bergland (1972); Brigham(1973);Chow,Vranesic,andYen(1983);CorinthiosandSmith(1975); CyreandLipovski1972];DereandSakriso(197);Flanders(1982);Jeoe (1980); Kulkarni and Yen (1982); Lambiote andKorn (1979); Parker (1980); Pease (1968,1977); Preparata and Vuillemin (1981); Ramamoorthy and Chang (1971);Redinbo (1979);Stone (1971);Thompson (1983a,1983b);Woldand Despain (1984); and Zhang and Yun (1984).

Brass and Pawley (1986) discuss the implementation of two- and threedimensional FFT algorithms on SIMD computers and provide timings for their algorithmsonthe ICLDistributed ArrayProcessr.Norton and Silberger(197) explore the performance that might be possible from FFT programs written in a high-level language. Swarztrauber (1987) presents multiprocessor FFT algorithms for both hypercube multicomputers and vector multiprocessors. Chamberlain (1988) describes the implementation of a parallel FFT algorithm on a 64-processor Intel iPSC. Averbuch et al. (1990) document the performance of a parallel FFT algorithm on acustom MIMD machine. Huang and Paker (1991) present a parallel FFT algorithm suitable for MIMD computers and timings for transputer networks of various sizes.

8-1Represent each of the following complex numbers in the form $r e ^ { i \theta }$

a   
b $i$   
C $4 + 3 i$   
d $- 2 - 5 i$   
e $2 - i$

3-2For each value of $n$ in the range $2 , \ldots , 5$ , represent the principal nth root of unity as $x + i y$ and $r e ^ { i \theta }$

8-3For each vector below,show the result of applying the discrete Fourier transform to it. a (7, 11) b (13, 17, 19, 23) c (2,1, 3,7,5,4, 0, 6)

8-4For each vector below, show the result of applying the inverse discrete Fourier transform to it. a (7, 11) b (13, 17, 19, 23) c (2, 1,3,7, 5,4,0, 6)

Devise a parallel FFT algorithm suitable for implementation on a UMA multiprocessor.

Write a sequential algorithm to perform the inverse FFT. Given $n = 2 ^ { k }$ ,the algorithm should expect the input elements in order $y _ { 0 } , y _ { 1 } , \dotsc , y _ { n - 1 }$ and produce the output elements in order $a _ { 0 } , a _ { 1 } , \ldots , a _ { n - 1 }$

Writea parallel versionof the inverse FFTalgorithm suitable for implementation on a hypercube multicomputer.

Write a parallel version of the inverse FFT algorithm suitable for implementation on a UMA multiprocessor.

8-9 You can organize the computation of the FFT so that no permutation step is necessary at thebeginningof thealgorithm.With this algorithm theoutput elements are inbit-reverse order (seeFig.8-9).Writeasequential version of this FFT algorithm.

8-10Paralelize the sequentia algorithm you designed in the previous example.

8-11 You can implement an inverse FFT algorithm that assumes its inputs are in bitreverse order (see Fig.8-1O).Writea sequential version of such an inverse FFT algorithm.

8-12Paralelize the sequential algorithm you designed in the previous example.

8-13 One application of the discrete Fourier transform is to filter noise from an input signal. Figure 8-11 displays a noisy signal. The curve represents signal strength, and the spikes represent noise. Noise introduces high-frequency components into the continuous function modeling the data points.We can filter out noise by eliminating the high-frequency components.

Figure 8-12 illustrates a three-step process to remove noise from a signal. In the first step the FFT algorithm transforms the input signal into its spectral decomposition. In the second step a filtering algorithm eliminates the high-

![](images/bc5d05be18a403f5e746352ba8f1b45be331f50dde57a6f7d61e473b17b1c51b.jpg)

With no permutation step at the beginning of the FFT algorithm, the output elements $y _ { 0 } , \ldots , y _ { 7 }$ arein bit-reverse order.

![](images/63e3d1e399bf6fb07b0c40f5adbf80a66d59a1fe415cb9ef3fdb6c7e276965ce.jpg)  
FIGURE 8-11  Input signal with noise.

![](images/89f002b412f964461c2b2bd4b863b912c91e45e94e6644d5305235d8d4237af4.jpg)  
FIGURE8-12Atree-stepprocess toremove noisefromasignal:FFTlow-passfilterandise FFT.

frequency components of the spectal decomposition. In the third step the inverse FFTalgorithm transforms the remaining frequency information intoa signal (see Fig. 8-13).

Write an algorithm to filter high-frequency noise from an input sample of 512 data points. The filtering program should not modify the amplitude of spectral components with frequency less than or equal to 20. Spectral components with frequency greater than or equal to 3O should be eliminated. For a component with frequency $x$ ,where $2 0 < x < 3 0$ , the program should multiply its amplitude by $( 1 - ( x - 2 0 ) / 1 0 )$

![](images/b7cfc81e1f99f529546121a03fb15ad4109ad23fcc1964e656d0c91cb29c0f07.jpg)  
FIGURE 8-13 Input signal of Fig. 8-11 after filtering.

8-14 Suppose you want to implement a parallel version of the three-stage signal filtering algorithm illustrated in Fig. 8-12, and suppose the target machine is a hypercube multicomputer. Describe how you would map the tasks to the processors. Justify your design.

# 9

Concern for man himself and his fate must always form the chief interest ofalltechnical endeavors,concernfor the great unsolvedproblemsofthe organizationoflabor and the distributionof goods-in order that the creations of ourmind shallbeablessing and not a curse to mankind. Never forget this in the midst of your diagrams and equations.

Albert Einstein, Address at the California Institute of Technology,1931

This chapter surveys the parallelization of algorithms used to solve systems of linearequations. Many scientific and engineering problems can take the form of a system of linear equations.Because systems in realistic problems are often quite large, there is good reason to solve these systems efficiently on parallel computers. In Sec. 9.1 we present two examples and introduce the terminology used in the remainder of the chapter. Sections 9.2 through 9.4 cover direct methods for solving linear systems. In Sec. 9.2 we explore how to parallelize the back substitution algorithm used for solving upper triangular systems. Section 9.3 describes odd-even reduction,a parallel algorithm to solve tridiagonal systems. Parallelization of the well-known gaussian elimination algorithm is discussed in Sec. 9.4.

Sections 9.5 through 9.9 cover indirect, or iterative,methods. In Sec. 9.5 we describe the inherently parallel Jacobi algorithm. Section 9.6 discusses ways to parallelize the Gauss-Seidel algorithm,which exhibits faster convergence to a solution than the Jacobi algorithm. Jacobi overrelaxation and successive overrelaxation, variants of the previous two algorithms,are summarized in

Sec. 9.7. Section 9.8 describes multigrid methods, which are often used for the numerical solution of partial differential equations.Finally, Sec. 9.9 covers the parallelization of the conjugate gradient method, a fast converging algorithm that can be used to solve systems of linear equations having certain properties.

# 9.1 TERMINOLOGY

This section defines some important terms and illustrates how problems can be expressed as systems of linear equations. If you have a good background in numerical linear algebra, you may wish to skip to Sec. 9.2.

Definition 9.1. A linear equation in the $n$ variables $x _ { 1 } , x _ { 2 } , x _ { 3 } , \ldots , x _ { n }$ is an equation that can be expressed as

$$
a _ { 1 } x _ { 1 } + a _ { 2 } x _ { 2 } + a _ { 3 } x _ { 3 } + \ldots a _ { n } x _ { n } = b
$$

where $a _ { 1 } , a _ { 2 } , a _ { 3 } , \ldots , a _ { n }$ ,and $^ { b }$ are constants.

Definition 9.2. A finite set of linear equations in the variables $x _ { 1 }$ ， $x _ { 2 }$ ， $x _ { 3 }$ 。..， $x _ { n }$ is called a system of linear equations or a linear system.A set of numbers $s _ { 1 }$ ， $s _ { 2 }$ 。···， $s _ { n }$ is a solution to a system of linear equations if and only if making the substitutions $x _ { 1 } = s _ { 1 }$ ， $x _ { 2 } = s _ { 2 }$ ， $x _ { 3 } = s _ { 3 }$ $x _ { n } = s _ { n }$ satisfies every equation in the linear system.

A system of $n$ linear equations in $n$ variables

$$
\begin{array} { l } { { a _ { 1 1 } x _ { 1 } + a _ { 1 2 } x _ { 2 } + a _ { 1 3 } x _ { 3 } \ldots + a _ { 1 n } x _ { n } = b _ { 1 } } } \\ { { a _ { 2 1 } x _ { 1 } + a _ { 2 2 } x _ { 2 } + a _ { 2 3 } x _ { 3 } \ldots + a _ { 2 n } x _ { n } = b _ { 2 } } } \\ { { a _ { 3 1 } x _ { 1 } + a _ { 3 2 } x _ { 2 } + a _ { 3 3 } x _ { 3 } \ldots + a _ { 3 n } x _ { n } = b _ { 3 } } } \\ { { \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots } } \\ { { a _ { n 1 } x _ { 1 } + a _ { n 2 } x _ { 2 } + a _ { n 3 } x _ { 3 } \ldots \ldots + a _ { n n } x _ { n } = b _ { n } } } \end{array}
$$

is usually expressed as $\mathbf { A } \mathbf { x } = \mathbf { b }$ ,where $\mathbf { A }$ is an $n \times n$ matrix containing the $a _ { i , j } s$ and $\mathbf { X }$ and $\mathbf { b }$ are $n$ -element vectors storing $x _ { i } \mathbf { s }$ and $b _ { i } \mathbf { s }$ ,respectively. The location and value of the nonzero elements of matrix A determine how difficult it is to solve for $\mathbf { X }$ In the most general case,a sequential algorithm having time complexity $O ( n ^ { 3 } )$ can solve a system of linear equations.

Here is a problem that generates a linear system with no special form. (The example is taken from Hallday and Resnick[1974].)Consider theelementary circuit shown in Fig. 9-1. Two batteries supply electromotive force E1 and E2 to the circuit. Three resistors provide resistance R1, R2,and R3 to the current. Given these values, we want to compute the three currents $i _ { 1 } , i _ { 2 }$ and $i _ { 3 }$

Byapplying physical laws we can expressthe problem as three equations, involving the three unknown values $i _ { 1 } , i _ { 2 }$ and $i _ { 3 }$

$$
\begin{array} { r } { i _ { 1 } \qquad - i _ { 2 } \qquad + i _ { 3 } \ = \quad 0 } \\ { - R _ { 1 } i _ { 1 } \qquad + R _ { 3 } i _ { 3 } = - E _ { 1 } } \\ { - R _ { 2 } i _ { 2 } \ : - R _ { 3 } i _ { 3 } = \quad E _ { 2 } } \end{array}
$$

![](images/0e54fd8def2667bbcbc28bdad070e8f37755a41d0cdc12866f70fca1a8095a1a.jpg)  
FIGURE 9-1 Anelementarycircuit with two batteriesandthreeresistors. (Drawingadaptedfrom figure in Hallidayand Resnick[1974].)

Linear systems with zeroes in the right places can be solved faster than linear systemsof arbitrary form. Examples include triangular,tridiagonal,and positive definite systems.

Definition 9.3. An $n \times n$ matrix $\mathbf { A }$ is upper triangular if

$$
i > j \Rightarrow a _ { i j } = 0
$$

Definition 9.4. An $n \times n$ matrix $\mathbf { A }$ is lower triangular if

$$
i < j \Rightarrow a _ { i j } = 0
$$

Upper triangular and lower triangular systems are solvable in $O ( n ^ { 2 } )$ time on sequential computers.

Definition 9.5. An $n \times n$ matrix $\mathbf { A }$ is tridiagonal if and only if

$$
| i - j | > 1 \Rightarrow a _ { i j } = 0
$$

A linear system $\mathbf { A } \mathbf { x } = \mathbf { b }$ is called tridiagonal if coefficient matrix A is tridiagonal. Sequential algorithms with time complexity $\Theta ( n )$ exist to solve tridiagonal systems.

Let's see how a tridiagonal linear system can be used to solve problems. Suppose we want to determine the steady-state temperature distribution in a rod of conducting material (Fig. 9-2). We assume the rod has a uniform cross section, so that all points in a cross section have equal temperature.This enables us to describe temperature as a function of distance from one end of the rod. We assume the temperatures $T _ { 1 }$ and $T _ { 2 }$ at the ends of the rod are fixed through exposure to a constant heat source. Finally,we assume that the rod is swathed in insulating material. In other words,no heat escapes from the sides of the rod—all heat transfer is at the ends.

![](images/db807215317a873d548d30cf84db8c26d9fa5d4a201bfc665bf4662af07d2296.jpg)  
FIGURE 9-2 An insulated rod with fixed end temperatures $\tau _ { \uparrow }$ and $T _ { 2 }$ We want to know the temperatures at points $x _ { 1 }$ ， $x _ { 2 }$ , $x _ { 3 }$ ， $x _ { 4 }$ ，which divide the bar into five segments of equal length.

Finding the steady-state temperature at four evenly spaced points $x _ { 1 } , x _ { 2 } , x _ { 3 }$ ， and $x _ { 4 }$ can be expressed as a system of linear equations:

$$
\begin{array} { r l r } { x _ { 1 } } & { - 0 . 5 x _ { 2 } } & { = 0 . 5 T _ { 1 } } \\ { - 0 . 5 x _ { 1 } } & { + x _ { 2 } } & { - 0 . 5 x _ { 3 } } & { = 0 \quad 0 } \\ { - 0 . 5 x _ { 2 } } & { + x _ { 3 } } & { - 0 . 5 x _ { 4 } = \quad 0 } \\ { - 0 . 5 x _ { 3 } } & { + x _ { 4 } } & { = 0 . 5 T _ { 2 } } \end{array}
$$

Here are three more definitions that we will use later in this chapter.

Definition 9.6. An $n \times n$ matrix $\mathbf { A }$ is diagonally dominant if $| a _ { i , i } | > \Sigma _ { j \neq i } | a _ { i , j } |$ for $1 \leq i \leq n$

Definition 9.7. An $n \times n$ matrix A is symmetric if $a _ { i j } = a _ { j i }$ for $1 \leq i , j \leq n$

Definition 9.8. An $n \times n$ matrix Ais oiivedefiiteifitissmetriciagoally dominant, and $a _ { i i } > 0$ for $1 \leq i \leq n$

# 9.2 BACK SUBSTITUTION

In this section we describe the paralelization of an algorithm used to solve the linear system $\mathbf { A } \mathbf { x } = \mathbf { b }$ where A is upper triangular.

Given a system of linear equations $\mathbf { A } \mathbf { x } = \mathbf { b }$ ， where A is an upper triangular $n \times n$ matrix,the back substitution algorithm solves the linear system in time @(n2). Let's view the algorithm by using a simple example. Suppose we want to solve the system

$$
\begin{array} { r } { { 1 } x _ { 1 } + { 1 } x _ { 2 } - { 1 } x _ { 3 } + 4 x _ { 4 } = 8 } \\ { - 2 x _ { 2 } - 3 x _ { 3 } + 1 x _ { 4 } = 5 } \\ { 2 x _ { 3 } - 3 x _ { 4 } = 0 } \\ { 2 x _ { 4 } = 4 } \end{array}
$$

We can solve the last equation directly, since it has only a single unknown. After we have determined that x4 =2, we can simplify the other equations by

removing their $x _ { 4 }$ terms and adjusting the value of their $\mathbf { b }$ terms:

$$
\begin{array} { r l r } { { 1 } x _ { 1 } + 1 x _ { 2 } - 1 x _ { 3 } } & { { } = 0 } \\ { - 2 x _ { 2 } - 3 x _ { 3 } } & { { } = 3 } \\ { 2 x _ { 3 } } & { { } = 6 } \\ { 2 x _ { 4 } = 4 } \end{array}
$$

Now the third equation has only a single unknown,and a simple division yields $x _ { 3 } = 3$ Again,weusethis information tosimplify the two equationsabove it:

$$
\begin{array} { c c } { { 1 x _ { 1 } + 1 x _ { 2 } } } & { { = 3 } } \\ { { - 2 x _ { 2 } } } & { { = 1 2 } } \\ { { 2 x _ { 3 } } } & { { = 6 } } \\ { { 2 x _ { 4 } = 4 } } & { { } } \end{array}
$$

We have simplified the second equation to contain only a single unknown,and dividing $b _ { 2 }$ by $a _ { 2 2 }$ yields $x _ { 2 } = - 6$ After subtracting $x _ { 2 } \times a _ { 1 2 }$ from $b _ { 1 }$ we have

$$
\begin{array} { r l r } & { } & { \mathrm { { \small ~ \alpha ~ } } = ~ 9 } \\ & { } & { - 2 x _ { 2 } ~ \mathrm { { \small ~ \alpha ~ } } = 1 2 } \\ & { } & { 2 x _ { 3 } ~ \mathrm { { \small ~ \alpha ~ } } = ~ 6 } \\ & { } & { 2 x _ { 4 } = ~ 4 } \end{array}
$$

and it is easy to see that $x _ { 1 } = 9$

A sequential algorithm to perform back substitution appears in Fig. 9-3. The time complexity of this algorithm is $\Theta ( n ^ { 2 } )$ 。

How amenable to parallelization is the back substitution algorithm? It is often difficult to determine the inherent parallelism of an algorithm from a simple examination of the code. Sometimes construction of a task graph can make the parallelism (or lack of parallelism) apparent. The task graph has these properties:

# BACK.SUBSTITUTION (SISD):

Global $n$ {Size of system} $a [ 1 . . . n ] [ 1 . . . n ]$ {Elements of A} $b [ 1 . . . n ]$ {Elements of b) $x [ 1 . . . n ]$ {Elements of $x$ i {Column index) $j$ {Row index) 1. begin 2. for $i \gets n$ downto 1 do 3. $x [ i ] ~  ~ b [ i ] ~ / ~ a [ i ] [ i ]$ 4. for $j \gets 1$ to $i - 1$ do 5. $b [ j ] ~  ~ b [ j ] ~ - ~ x [ i ] ~ \times ~ a [ j ] [ i ]$ 6. $a [ j ] [ i ] ~  ~ 0$ {This line is optional) 7. endfor 8. endfor 9.end

1. It contains one vertex for every time a variable is assigned a value. 2. It contains one vertex for every variable that is accessed but never assigned avalue. 3. It contains one edge for every use-def dependency between a variable referenced on the right-hand side of an assignment statement and a variable assigned a value on the left-hand side. The edge is directed toward the variable assigned a value.

We have used these rules to construct a task graph for the back substitution algorithm applied to an upper triangular system of size 4 (see Fig. 9-4). Note that there are multiple vertices corresponding to each variable $b [ i ]$ ，since the algorithm repeatedly updates these variables.

Once the task graph has been constructed, we label each vertex according to the following rules:

1. If no edges enter a vertex, the vertex has label 0. 2. If the vertex has at least one incoming edge, its label is equal to 1 plus the maximum label of any vertex associated with an incoming edge.

The labels inside the vertices in Fig. 9-4 have been assigned using these rules.   
The labels represent the depth of each part of the computation in the task graph.   
We have used bold arcs to indicate one of the critical paths of the task graph.   
It is evident from the critical path that the elements of $x$ must be computed one at a time.

With this knowledge, it is clear our only alternative is to parallelize the inner for loop. Theparallel algorithm,esigned fora UMA multiprocessorars in Fig. 9-5. The grain size is small;even in the first iteration there are only $n - 1$ multiplications and $n - 1$ subtractions. As the algorithm progresses, the

![](images/69e3fbefdba8f97974a6ddf609d5f63ad71ef2ca075dce924a81c5b2ec86b0c3.jpg)  
FIGURE9-4 Task graph for the sequential back substitution algorithm solving an upper triangular systemof size4.Elementsof vectorbareupdated,sothegraphshowsonevetefor eachvalue of each element.The label inside each vertex indicates the depth of the task in the graph.Acritical path is highlighted.

Global n {Size of system} $p$ {Number of processes] $a [ 1 . . . n ] [ 1 . . . n ]$ {Elements of A} $b [ 1 . . . n ]$ {Elements of b} $x [ 1 . . . n ]$ {Elements of x} $_ i$ {Column index} Local $j$ {Process identifier) $k$ {Row index} begin for $i \gets n$ downto 2 do $x [ i ] \  \ b [ i ] \ / \ a [ i ] [ i ]$ forall $P _ { j }$ where $1 ~ \leq ~ j ~ \leq ~ p$ do for $k \gets j$ to $i - 1$ step $p$ do $b [ k ] ~  ~ b [ k ] ~ - ~ x [ i ] ~ \times ~ a [ k ] [ i ]$ $a [ k ] [ i ] ~  ~ 0$ {This line is optional) endfor endforall endfor end

number decreases linearly to 1 multiplication and 1 subtraction. For this reason we cannot expect this algorithm to achieve high speedup.

Figure 9-6 illustrates the speedup achieved by our parallel back substitution algorithm on a lightly loaded Sequent Symmetry UMA multiprocessor. Note the Amdahl effect: speedup on any fixed number of processors increases with the problem size.

![](images/a8e49f748bc360f78b9f80656f2610422ff3efb76c6b9d36308b5a0bd29ea5af.jpg)  
FIGURE 9-5 Parallel version of back substitution algorithm suitable for implementation on a UMA multiprocessor.   
FIGURE 9-6 Speedup achieved on Sequent Symmetryby theparallel back substitution algorithm solving triangular systems of various sizes.

In this section we explore two algorithms for solving tridiagonal systems of linear equations. The first is a straightforward algorithm, suitable for execution on a serial computer, but is unsuitable for parallelization. The second algorithm,called odd-even reduction or cyclic reduction, has a higher constant of proportionality, but can be parallelized.

We begin by developing the straightforward sequential algorithm. Consider the following tridiagonal linear system:

$$
\begin{array} { r l r } { 1 6 x _ { 1 } } & { + 4 x _ { 2 } } & { = \ 8 } \\ { 4 x _ { 1 } } & { + 1 1 x _ { 2 } } & { - 5 x _ { 3 } } & { = \ 7 } \\ & { \ 2 x _ { 2 } } & { + 1 4 x _ { 3 } } & { - 6 x _ { 4 } \ = \ 1 3 } \\ & { \ } & { 5 x _ { 3 } } & { + 1 8 x _ { 4 } = 2 4 } \end{array}
$$

Unlike the upper triangular system we encountered in the last section, the tridiagonal system generally does not contain any equations with exactly one variable. For this reason we must combine equations to determine the values of the variables.

We may perform three operations on a system of linear equations without changing the value of the solution (Anton 1981):

1. Multiply every term of an equation by a nonzero constant   
2. Interchange two equations   
3. Add a multiple of one equation to another equation

First we eliminate x1 from the second equation by subtracting 1/4 times the first equation from the second equation:

$$
\begin{array} { r l r } { 1 6 x _ { 1 } + 4 x _ { 2 } } & { } & { = 8 } \\ { 1 0 x _ { 2 } } & { - 5 x _ { 3 } } & { = 5 } \\ { 2 x _ { 2 } } & { + 1 4 x _ { 3 } } & { - 6 x _ { 4 } = 1 3 } \\ & { } & { 5 x _ { 3 } + 1 8 x _ { 4 } = 2 4 } \end{array}
$$

Next we eliminate x2 from the third equation by subtracting 1/5 times the second equation from the third equation:

$$
\begin{array} { r l r } { 1 6 x _ { 1 } + 4 x _ { 2 } } & { } & { = ~ 8 } \\ { 1 0 x _ { 2 } - 5 x _ { 3 } } & { = ~ 5 } \\ { 1 5 x _ { 3 } } & { - 6 x _ { 4 } = 1 2 } \\ { 5 x _ { 3 } } & { + 1 8 x _ { 4 } = 2 4 } \end{array}
$$

Finally, we remove x3 from the fourth equation by subtracting 1/3 times the third equation from the fourth equation:

$$
\begin{array} { r l r } { 1 6 x _ { 1 } + 4 x _ { 2 } } & { } & { = 8 } \\ { 1 0 x _ { 2 } } & { } & { = 5 } \\ { 1 5 x _ { 3 } } & { } & { - 6 x _ { 4 } = 1 2 } \\ & { } & { 2 0 x _ { 4 } = 2 0 } \end{array}
$$

Here the last equation has a single unknown,and we can solve for $x _ { 4 }$ directly. Once $x _ { 4 }$ is known,itiseasy tosolve for $x _ { 3 }$ .The algorithm continues in this fashion until the values for the rest of the variables have been determined.

Let's consider the form of the equations in the tridiagonal system. Except for the first and last equations,each equation has three variables in it.

$$
\begin{array} { r l } { g _ { 1 } x _ { 1 } + h _ { 1 } x _ { 2 } = b _ { 1 } \quad ~ } & { { } } \\ { \quad } & { { } } \\ { f _ { i } x _ { i - 1 } + g _ { i } x _ { i } + h _ { i } x _ { i + 1 } = b _ { i } \quad } & { { } 2 \leq i \leq n - 1 } \\ { \quad } & { { } } \\ { f _ { n } x _ { n - 1 } + g _ { n } x _ { n } = b _ { n } \quad } & { { } } \end{array}
$$

A sequential algorithm to solve a tridiagonal system of equations appears in Fig. 9-7. The algorithm has two for loops,each performing $n - 1$ iterations (assuming the size of the linear system is $n$ ).The steps within each for loop require constant time. Hence the complexity of the sequential algorithm to solve a tridiagonal system of linear equations is $\Theta ( n )$ ·

FIGURE9-7 Sequential algorithm to solve a system of tridiagonal equations.The algorithm performs $9 n - 8$ floating-point operations,assuming the expression $f [ i + 1 ] / g [ j ]$ is evaluated only once per iteration of the first for loop.

# TRIDIAGONAL.SYSTEM.SOLVER (SISD):

{This algorithm solves the set of equations $g _ { 1 } \ x _ { 1 } \ + \ h _ { 1 } \ x _ { 2 } \ = \ b _ { 1 }$ $f _ { i } \ x _ { i - 1 } \ + \ g _ { i } \ x _ { i } + h _ { i } \ x _ { i + 1 } \ = \ b _ { i }$ for $1 ~ < ~ i ~ < ~ n$ $f _ { n } \ x _ { n - 1 } \ + \ g _ { n } \ x _ { n } \ = \ b _ { n }$

Global $\begin{array} { l } { { n } } \\ { { f [ 2 . . . n ] , g [ 1 . . . n ] , h [ 1 . . . ( n - 1 ) ] } } \\ { { b [ 1 . . . n ] } } \\ { { x [ 1 . . . n ] } } \end{array}$ {Coefficients of {Size of tridiagonal system} $x$ {Constant vector} { Solution vector }   
begin   
for $i \gets 1$ to $n - 1$ do   
$\begin{array} { r l r } { g [ i + 1 ] ~  ~ g [ i + 1 ] ~ - ~ ( f [ i + 1 ] / g [ i ] ) ~ \times ~ h [ i ] } & { } \\ { b [ i + 1 ] ~  ~ b [ i + 1 ] ~ - ~ ( f [ i + 1 ] / g [ i ] ) ~ \times ~ b [ i ] } & { } \end{array}$   
endfor   
for $i \gets n$ downto 2 do   
$x [ i ] ~  ~ b [ i ] ~ / ~ g [ i ]$   
$b [ i - 1 ]  b [ i - 1 ] - x [ i ] \times h [ i - 1 ]$   
endfor   
$x [ 1 ]  b [ 1 ] / g [ 1 ]$   
end

![](images/c2112aaaa4d637b75f0ba4c14b1c11e31d3b6f8dd05e50849c74dea8916fe4f6.jpg)  
FIGURE 9-8 Data flow diagram illustrating data dependencies in the first loop of the tridiagonal-system solver of Fig.9-7, fora system of size 4.The number inside each vertex is the length of the longest path preceding the vertex. The overlapping circlesrepresent instanceswhere the new value of a variable iscomputed from an expression containing its previous value.

We can determine if an algorithm can be parallelized by exploring its data dependencies.Figure9-8 is a data-flow diagram for the first loopof the algorithm solving a system of size 4. The overlapping circles represent instances where the new value of a variable is computed from an expression containing its previous value. The data flow diagram makes clear that this particular algorithm is not amenable to paralelization.

Toachieve some paralelism, we must take another problem solving approach. First, we want to represent all $n$ equations the same way. We can do this by introducing pseudovariables $x _ { 0 }$ and $x _ { n + 2 }$ ,both having value0.Now we are able to write

$$
f _ { i } x _ { i - 1 } + g _ { i } x _ { i } + h _ { i } x _ { i + 1 } = b _ { i } \qquad 1 \leq i \leq n
$$

Rewriting equation 9.14 to solve for $x _ { i }$ we get

$$
x _ { i } = ( b _ { i } - f _ { i } x _ { i - 1 } - h _ { i } x _ { i + 1 } ) / g _ { i } \qquad 1 \leq i \leq n
$$

If we introduce two more pseudovariables $x _ { - 1 }$ and $x _ { n + 2 }$ ,both having value 0, we can use equation 9.15 to substitute for $x _ { i - 1 }$ and $x _ { i + 1 }$ in equation 9.14:

$$
f _ { i } \left( \frac { b _ { i - 1 } - f _ { i - 1 } x _ { i - 2 } - h _ { i - 1 } x _ { i } } { g _ { i - 1 } } \right) + g _ { i } x _ { i } +
$$

$$
h _ { i } \left( \frac { b _ { i + 1 } - f _ { i + 1 } x _ { i } - h _ { i + 1 } x _ { i + 2 } } { g _ { i + 1 } } \right) = b _ { i } \qquad 1 \leq i \leq n
$$

To simplify this equation we define

$$
\begin{array} { c c } { \gamma _ { i } = f _ { i } / g _ { i - 1 } } & { 1 \le i \le n } \\ { \delta _ { i } = h _ { i } / g _ { i + 1 } } & { 1 \le i \le n } \end{array}
$$

Now we can rewrite it as

$$
\begin{array} { c } { { \gamma _ { i } f _ { i - 1 } x _ { i - 2 } + ( g _ { i } - \gamma _ { i } h _ { i - 1 } - \delta _ { i } f _ { i + 1 } ) x _ { i } - \delta _ { i } h _ { i + 1 } x _ { i + 2 } = } } \\ { { { } } } \\ { { b _ { i } + \gamma _ { i } h _ { i - 1 } + \delta _ { i } h _ { i + 1 } \qquad 1 \leq i \leq n } } \end{array}
$$

By this transformation we have expressed the value of $x _ { i }$ in terms of $x _ { i - 2 }$ and $x _ { i + 2 }$ . Taken as a whole, the equations for $x _ { 2 }$ ， $x _ { 4 }$ ， $x _ { 6 }$ 。...， $x _ { n }$ form a tridiagonal system with $n / 2$ variables. Applying this technique recursively yieldsa divideand-conquer algorithm,called odd-even reduction or cyclic reduction, to solve a tridiagonal system of linear equations. The odd-even reduction algorithm was first published by Hockney (1965).

Figure 9-9 illustrates the odd-even reduction algorithm for a system of size 8. In the first step the coefficients of $x _ { 1 } , x _ { 3 } , x _ { 5 }$ and $x _ { 7 }$ are eliminated; the remaining system is tridiagonal and has only the variables with even indices. In the second step the coefficients of $x _ { 2 }$ and $x _ { 6 }$ are eliminated. In step three $x _ { 4 }$ is eliminated,and we are left with a single equation in a single unknown. Once the value of $x _ { 8 }$ is known, the value of $x _ { 4 }$ can be found. With the values of $x _ { 8 }$ and $x _ { 4 }$ computed,thealgorithm can determine the values of $x _ { 2 }$ and $x _ { 6 }$ ， and once $x _ { 2 }$ ， $x _ { 4 }$ ， $x _ { 6 }$ ,and $x _ { 8 }$ are known,the algorithm finds values for $x _ { 1 } , x _ { 3 }$ $x { 5 }$ ,and $x _ { 7 }$

The odd-even reduction algorithm appears in pseudocode in Fig. 9-10. The time complexity of odd-even reduction is $\Theta ( n )$ , the same as that of the sequential algorithm presented earlier. However, odd-even reduction is much more amenable to parallelization,as shown in Fig. 9-9,as all three inner for loops can be executed in parallel. We have implemented a parallel odd-even reduction algorithm on the Sequent Symmetry system and measured its performance solving a tridiagonal system of size 65,536.The parallelizability and speedup of this algorithm are shown in Fig. 9-11.

FIGURE 9-9 This diagram illustrates how the odd-even reduction algorithm eliminates variables in a tridiagonal system of size8.Inthefirst stepvariables $x _ { 1 }$ ， $x _ { 3 }$ ， $x _ { 5 }$ and $x _ { 7 }$ are eliminated. In the second step variables $x _ { 2 }$ and $x _ { 6 }$ areeliminated.In stepthreevariable $x _ { 4 }$ is eliminated.Here the equationhasa singlevariable $x _ { 8 }$ -whosevaluecanbecomputed directly.Oncethevalueof $x _ { 8 }$ isknownthealgoritmsolsfor $x _ { 4 }$ Givenvalues for $x _ { 8 }$ and $x _ { 4 }$ ，thealgorithm computes the valuesof $x _ { 2 }$ and $x _ { 6 }$ and so on.

![](images/a3e6c92c7be467a52bb9a696d811b5910cf8f432da89f9606652e9ff7cc8f498.jpg)

{This algorithm solves a system of tridiagonal equations)

Global n {Number of equations in linear system} $f [ 1 . . . n ]$ , g[1...n], h[1...n] {Coefficients of the tridiagonal equation $b [ 1 . . . n ]$ {Constant vector} $n e w . f [ 1 . . . n ]$ , new.g[1...n], {Newly computed coefficients} new.h[1..n], new.b[1...n] $x [ 1 . . . n ]$ {Solution vector) d {Distance between terms being combin γ[1..n], δ[1.n] {Temporaries) begin for $i \gets 0$ to $\log n \ - \ 1$ do $d \gets 2 ^ { i }$ for $j \gets 2 \times i + 1$ to $n - 1$ step $2 \times \textit { d }$ do $\gamma [ j ] ~  ~ f [ j ] ~ / \ l { g } [ j - d ]$ $\delta [ j ] ~  ~ h [ j ] / g [ j + d ]$ $n e w . f [ j ] \ \gets \ - \gamma [ j ] \ \times \ f [ j - d ]$ neu $\cdot g [ j ] ~  ~ - ~ \delta [ j ] ~ \times ~ f [ j + d ] ~ - ~ \gamma [ j ] ~ \times ~ h [ j - i ]$ $n e w . h [ j ] \ \gets \ \delta [ j ] \ \times \ h [ j + d ]$ $n e w . b [ j ] ~  ~ b [ j ] ~ + ~ \gamma [ j ] ~ \times ~ b [ j - d ] ~ + ~ \delta [ j ] ~ \times ~ b [ j + d ] ~$ endfor $\gamma [ n ] ~  ~ f [ n ] ~ / { g [ n - d ] }$ $f [ n ] ~  ~ - \gamma [ j ] ~ \times ~ f [ n - d ]$ $g [ n ] \  \ g [ n ] \ - \ \gamma [ n ] \ \times \ h [ n - d ]$ $b [ n ] \  \ b [ n ] \ + \ \gamma [ n ] \ \times \ b [ n - d ]$ for $j \ \gets \ 2 \times \ i \ + \ 1$ to $n - 1$ step $2 \times \ d$ do $f [ j ] ~  ~ n e w . f [ j ] , g [ j ] ~  ~ n e w . g [ j ] , h [ j ] ~  ~ n e w . h [ j ] , b [ j ] ~  ~ n e w . b [ j ]$ endfor endfor $x [ n ] ~  ~ b [ n ] ~ / ~ g [ n ]$ for $i  \log n  1$ downto 0 step $^ { - 1 }$ do $d \gets 2 ^ { i }$ $x [ d ] ~  ~ ( b [ d ] ~ - ~ h [ d ] ~ \times ~ x [ 2 \times ~ d ] ) / g [ d ]$ for j ← 3× d to n step2 ×d $x [ j ] ~  ~ ( b [ j ] ~ - ~ f [ j ] ~ \times ~ x [ j - d ] ~ - ~ h [ j ] ~ \times ~ x [ j + d ] ) / g [ j ]$ endfor endfor end

FIGURE 9-10 Sequential implementation of the odd-even reductionalgorithm to solve a tridiagonal system of linear equations.

![](images/07cdfe1a8ca770414677255f634b04a4b46c78718ecc71e2add26ccb4d43c2f5.jpg)  
FIGURE 9-11 Speedup (solid line) and parallelizability (dotted line) of parallel odd-even reductionon Sequent Symmetry ona tridiagonal system of size 65,636.

As Fig.9-11makes clear,although thealgorithm is easily paralelizableits speedup is poor. Let's explore the reasons for this.

The total number of floating-point operations performed by the sequential algorithm of Fig. 9-7 is

$$
\sum _ { i = 1 } ^ { n - 1 } 6 + \sum _ { i = 2 } ^ { n } 3 + 1 = 9 n - 8
$$

The total number of floating-point operations performed by the odd-even reduction algorithm is

$$
\sum _ { i = 1 } ^ { \log n - 1 } \left( \left( \sum _ { j = 1 } ^ { n / 2 ^ { i } - 1 } 1 3 \right) + 7 \right) + 1 + \sum _ { i = 1 } ^ { \log n - 1 } \left( \left( \sum _ { j = 1 } ^ { n / 2 ^ { i } - 1 } 5 \right) + 3 \right) =
$$

$$
1 3 \left( n - 2 - ( \log n - 1 ) \right) + 7 ( \log n - 1 ) + 1 + 5 ( n - 2 - ( \log n - 1 ) )
$$

$$
+ 3 ( \log n - 1 ) = 1 8 n - 8 \log n - 2 7
$$

Taking the ratio of equations 9.19 and 9.20

$$
\operatorname* { l i m } _ { n  \infty } ( { \frac { 9 n - 8 } { 1 8 n - 8 \log n - 2 7 } } ) = \frac { 1 } { 2 }
$$

We should not expect a parallel implementation of odd-even reduction to exhibit an efficiency greater than 50 percent.

# 9.4 GAUSSIAN ELIMINATION

In this section we describe the parallelization of gaussian elimination, a wellknown algorithm for solving the linear system $\mathbf { A } \mathbf { x } = \mathbf { b }$ when the matrix A has nonzero elements in arbitrary locations. Gaussian elimination reduces $\mathbf { A } \mathbf { x } = \mathbf { b }$ to an upper triangular system ${ \bf T } { \bf X } = { \bf c }$ ,at which point back substitution can be performed to solve for $\mathbf { X }$

Recall that we can replace any row of a linear system by the sum of that row and a nonzero multiple of any row of the system. We used this technique in Sec. 9.3 to eliminate nonzero elements from below the main diagonal in tridiagonal systems. Gaussian elimination uses the same technique.

Figure 9-12 illustrates one iteration of the. algorithm. All nonzero elements below the diagonal and to the left of column $i$ havealready been eliminated. In step $\ B _ { i }$ the nonzero elements below the diagonal in column $i$ are eliminated by replacing each row $j$ ，where $i + 1 \le j \le n$ ， with the sum of row $j$ and $- a _ { j , i } / a _ { i , i }$ times row $i$ After $n - 1$ such iterations, the linear system is upper triangular.

In the straightforward gaussian elimination algorithm just described, row i is the pivot row,i.e., the row used to drive to zero all nonzero elements below the diagonal in column i. This approach does not exhibit good numerical stability on digital computers. However,a simple variant, called gaussian elimination with partial pivoting, does produce reliable results. In step $i$ of gaussian elimination with partial pivoting, rows i through $n$ are searched for the row whose column $i$ element has the largest absolute value. This row is swapped (pivoted) with row i. Here the algorithm uses multiples of the pivot row, now stored as row $i$ ,to reduce to zero all nonzero elements of column $_ i$ in rows $i + 1$ though $_ n$

A sequential gaussian elimination algorithm appears in Fig. 9-13. Rather than actually swapping the pivot row and row $i$ in each iteration, the algorithm makes use of indirection. Array element pivot[i] contains the iteration number in which row $i$ was used as the pivot row. Another array is introduced to make it easy to determine if a particular row has been used as a pivot row; array element marked[i] is set to 1 when row $i$ is chosen as a pivot row.

Let's determine how well-suited gaussian elimination is to parallelization. First, we count every arithmetic operation and comparison involving floating-

IGURE9-12 During iteration i of the gaussian eliminationalgorithm,allelements incolumn i for each row $j$ belowrow $j$ aredriven to0bysubtractingamultipleofrow $j$ fromrow $j$

![](images/647dfbef79bda08fb8ab6ceca2d72fe92a22b8ba77a49169be98e2a442d0036d.jpg)

Global n {Size of linear system} a[1..n][1..n] (Coefficients of equations) $b [ 1 . . . n ]$ {Right-hand sides of equations) marked[1...n] {Indicates which rows have been pivot rows] pivot[1...n] {Indicates iteration each row was used as pivot) picked {Row picked as pivot row)

begin for $i \gets 1$ to $_ n$ do markedli] $ \mathrm { ~ 0 ~ }$ endfor for $i \gets 1$ to $n - 1$ do $t m p \gets 0$ for $j \gets i$ to $_ n$ do ifmarked $[ j ] = 0$ and $| a [ j ] [ i ] | ~ > ~ t m p$ then tmp $ \ | a [ j ] [ i ] |$ picked $ j$ endif endfor marked[picked]←1 pivot[picked] $\gets \ i$ for $j \gets 1$ to $_ n$ do ifmarked $[ j ] = 0$ then $t m p \ \gets \ a [ j ] [ i ] \ / \ a [ p i c k e d ] [ i ]$ for $k \gets i + 1$ to $n$ do $a [ j ] [ k ] ~  ~ a [ j ] [ k ] ~ - ~ a [ p i c k e d ] [ k ] ~ \times ~ t m p$ endfor $b [ j ] ~  ~ b [ j ] ~ - ~ b [ k ] ~ \times ~ t m p$ endif endfor   
endfor for $i \gets 1$ to $n$ do if marked[i] $= ~ 0$ then pivot[i] $ N$ break endif   
endfor   
end

IGURE 9-13 Sequential gaussian elimination algorithm with partial pivoting. The algorithm assumes thelinearsystem isnonsingular,i.e.,hasaolution.

point numbers in the algorithm of Fig. 9-13. The algorithm has $n - 1$ iterations, where the iteration number i varies from 1 to $n - 1$ During iteration $i$ there are $n - i$ comparison steps to determine the pivot row. Once the pivot row is known, the algorithm must reduce $n - i$ rows,where each row-reduction step requires 2(n -i) floating-point operations to modify the coefficients of A,and two more floating-point operations to modify the row’s entry in $\mathbf { b }$ Hence the total number of floating-point operations and comparisons is

$$
\sum _ { i = 1 } ^ { n - 1 } \left( ( n - i + 1 ) + \sum _ { j = i + 1 } ^ { n } \left( 1 + \sum _ { k = i + 1 } ^ { n + 1 } 2 \right) \right) =
$$

$$
\begin{array} { r } { \displaystyle \sum _ { i = 1 } ^ { n - 1 } \left( ( n - i + 1 ) + \sum _ { j = i + 1 } ^ { n } ( 2 n - 2 i + 3 ) \right) = } \\ { \displaystyle \sum _ { i = 1 } ^ { n - 1 } \left( 2 n ^ { 2 } + 4 n + 1 + 2 i ^ { 2 } - 4 i ( n + 1 ) \right) = } \end{array}
$$

$$
\frac { 2 n ^ { 3 } + 3 n ^ { 2 } - 2 n - 3 } { 3 }
$$

Most of these operations occur inside the innermost for loop. A study of the algorithm's data dependencies reveals that both the innermost for loop indexed by $k$ and the middle for loop indexed by $j$ can be executed in parallel. In other words, once the pivot row has been found, the modifications to all unmarked rows may occur simultaneously. Within each row,once the multiplier $a [ j ] [ i ] / a [ p i c k e d ] [ i ]$ has been computed, modifications to elements $i + 1$ through $n$ of each row may occur simultaneously. Since most of the operations counted in the last equation occur inside these for loops, the algorithm seems to be well-suited to parallelization.

Let's consider the implementation of gaussian elimination on a multicomputer. Assume $n$ is a multiple of $p$ .How should we distribute the elements of matrices $a$ and $^ { b }$ to the memories of the individual processors? If we examine the data flow of the algorithm for iteration i (Fig. 9-14), we see that determining the pivot row pickedrequires thatdataitems inolumni becompared,while determining the new value of a particular element a[jl[k] requires three values besides the current value of a[ji[k]. These values are a[j]li],a[picked][i],and $a \{ p i c k e d \} [ k ]$

Clearly the data distribution determines the points in the algorithm where communication is required. Suppose we assign to each processor a contiguous group of rows of $a$ and the associated elements of $^ b$ (Fig. 9-15). Given this distribution of data, the processors must interact in order to determine the pivot row. Once the pivot row has been determined, the processor owning the pivot row must broadcast its elements to the other processors, so that they

![](images/26538777fcebd300078e72cc700c5d9690986ade6a225ccc2c5b91b3cec764bb.jpg)  
Data dependencies during a single iteration of the gaussian eliminationalgorithm.During iteration $j$ the column $j$ element ofeveryunmarkedrowmust be examined to determine the identity ofthepivot rowpicked. Once the pivotrow has been identifiedryt ofeveryunmarkedrow $j$ must bemodified，ichr accessingall]，apicked], anda[picked][k].

![](images/7519b52892aff57a308d7c4a3e6d7f47e144b780520b884e9086e3e33044db9b.jpg)  
FIGURE 9-15 A row-oriented decomposition of the data for the multicomputer-targeted gaussian eliminationalgorithm.in this example $n = 1 6$ and $p = 4$

# MULTICOMPUTER):

Local n {Size of linear system} a[1...n/ p][1..n] {Coefficients of equations} $b [ 1 . . . n / p ]$ {Right-hand sides of equations} marked[1..n/ p] {Indicates which rows have been pivot rows] pivot[1...n/ p] {Indicates iteration each row was used as pivot) picked {Row picked as pivot row) magnitude {Pivot value) winner {Processor controlling pivot row} i， $j$ begin for all $P _ { i d }$ ,where $1 ~ \leq ~ i d ~ \leq ~ p$ do {Initially no rows have been used as pivot rows] for $i \gets 1$ to $n / p$ do marked[i] $ 0$ endfor for $i \gets 1$ to $n - 1$ do {Each processor finds candidate for pivot row} magnitude $ \mathrm { 0 }$ for $j \gets i$ to $n / p$ do ifmarked $[ j ] = 0$ and $| a [ j ] [ i ] | \ >$ magnitude then magnitude $ \ | a [ j ] [ i ] |$ picked $ j$ endif endfor winner $ i d$ {Tournament reduction determines globally best pivot row} MAX.TOURNAMENT(id,agnitude，r) if $i d =$ winner thenmarked[picked] $ 1$ pivot[picked] $\gets \ i$ for $j \gets i + 1$ to $n$ do $t m p . v e c t o r [ j ] ~  ~ a [ p i c k e d ] [ j ]$ tmp.vector $[ n + 1 ] \  \ b$ [picked] endfor endif

{Processor owning pivot row broadcasts it to other processors) HYPERCUBE.BOADCAST (id,winner,tmp.vector[(i+1).(n+1)l) {Processors eliminate column i values in their unmarked rows) for $j \gets 1$ to $n / p$ do ， if marked[j] $\mathit { \Theta } = \mathit { \Theta } 0$ then $t m p \gets a [ j ] [ i ] / t m p . \upsilon e c t o r [ i ]$ for $k \gets i + 1$ to $n$ do a[j][k] ← a[j][k] - tmp.vector[k] × tmp endfor b[j] ← b[j] - tmp.vector[n+1] × tmp endif endfor endfor {Locate row never used as a pivot row) for $i \gets 1$ to $n / p$ do if marked[i] $\mathit { \Theta } = \mathit { \Theta } 0$ then pivot[i] $ n$ break endif endfor endfor end

can update the values of the umarked rows they control. Pseudocode for this algorithm appears in Figs. 9-16 and 9-17.

We call the processor interaction to determine the pivot row a tournament, because we are interested in the identity of the pivot row (the winner) more than the magnitude of the value stored at column $i$ in the pivot row (the score). If we are interested in the identity of the processor with the largest value, we call the interaction a max-tournament. If we are interested in the identity of the processor with the smallest value, we call the interaction a min-tournament. We can implement a tournament algorithm as a simple variant of the reduction algorithm. Figure 9-18 ilustrates max-tournament for a hypercube. At each step.of the algorithm, two variables are maintained. Variable value contains the largest value encountered so far,and variable winner contains the number of the processor submitting that value. Although the pseudocode expresses the exchange of these values as two message-passing steps,a real implementation would undoubtedly combine these values into a single structure that could be passed all at once.

A different distribution of data structures results in a different multicomputer algorithm. For example, if we assign to each processor an interleaved group

MAX.TOURNAMENT (id, value, winner) Reference id, value, winner

{This procedure is called from inside a for all statement} begin for $i \gets 0$ to log $p \ - \ 1$ do partner $ i d \otimes 2 ^ { i }$ [partner]tmp.value $\Leftarrow$ value [partner]tmp.winner $\Leftarrow$ winner if tmp.value $>$ value then value tmp.value winner tmp.winner endif endfor end

of columns of $^ { a }$ and a copy of $^ { b }$ ,then the processors do not need to interact to determine the pivot row. Instead, during iteration i the processor controlling column $i$ examines the elements corresponding to unmarked rows and finds the element with the largest magnitude.No tournament is necessary.This processor then broadcasts elements of column $i$ and the identity of the pivot row to the other processors.

Recall that the grain size of a parallel computation is the amount of work performed per processor interaction. The strategy of maximizing grain size, which we have already discussed in the context of multiprocessors,is also important whendesigning algorithms formulticomputers. (seeDesignStrategy 5 in Chap. 7.)

On a multicomputer in which message latency is relatively high, maximizing grain size means minimizing the number of messages sent.In particular, if the messages are small, it makes sense to combine messages heading for the same destination processor in order to reduce message passing overhead.

For example, in the row-oriented version of parallel gaussian elimination, the processor controlling the pivot row must make elements $i + 1$ through $n$ of that row available to all the processors executing the for loop. Rather than broadcast these values one at a time, it makes more sense to broadcast the entire set of $n - i$ row elements.

Likewise, the column-oriented, parallel gaussian-elimination algorithm should be implemented so that during iteration i the processor controlling column i combines the elements of column i and the variable containing the identity of the pivot row intoa single message.

Comparing the row-oriented versus the column-oriented implementations of gaussian eliationwesethatthreisaommuicatioomputate off. In the row-oriented algorithm, processors work together to determine the pivot row. Given a system of size $n$ and $p$ processors, no processor eed examine more than $n / p$ values. However,once a processor has determined its local maximum, it must communicate with other processors in order to determine the global maximum. In iteration $i$ of the column-oriented algorithm one processor must perform $n - i$ comparisons, but no communication is required. Both algorithms require a broadcast step after the pivot row has been found. In the case of the row-oriented algorithm a single row is broadcast. In the case of the column-oriented algorithm a single column is broadcast.

![](images/5cb306b07b089a2be798116822794b371681c794614775ffc9a45910f86405e0.jpg)  
FIGURE9-19 Scaled speedupachieved bya row-oriented parallel implementation of gaussian eliminationona64rocessoruE32oforlinearstemsofriousses.

For any fixed $p$ ,as $n  \infty$ ,the time required by the row-oriented algorithm to find the pivot row must be less than that required by the column-oriented algorithm. For this reason, we have chosen to implement the row-oriented algorithm. Figure 9-19 illustrates the scaled speedup achieved by a row-oriented parallel implementation of gaussian elimination on a 64-processor nCUBE 3200, for linear systems of various sizes.

# 9.5 THE JACOBI ALGORITHM

In the remaining sections of this chapter we will examine iterative methods for solving systems of linear equations. Iterative algorithms are frequently used to solve the large, sparse linear systems generated when working with partial differential equations, using discrete methods. Iterative methods have two advantages over direct methods. First,"while these methods do not formally yield [a solution] in a finite number of steps, one can terminate such a procedure after a finite number of iterations when it has produced a sufficiently good approximate answer.” Second, “most iterative schemes possess the attractive feature that they require arithmetic operations only on the nonzero entries of the [coefficient] matrix A" (Allen et al. 1988).

Most of the iterative algorithms described in this chapter have the property that, if they converge, then they converge upon a correct solution. However, on some inputs the algorithms may never converge.A discussion of the conditions under which these algorithms converge upon a solution is beyond the scope of this book; see Bertsekas and Tsitsiklis (1989) for a mathematical treatment of this important topic.

The first iterative algorithm to be considered is the Jacobi algorithm. We make the standard assumption that we want to solve the linear system $\mathbf { A } \mathbf { x } = \mathbf { b }$ to determine the value of an unknown vector $\mathbf { x }$ Note that

$$
x _ { i } = \frac { 1 } { a _ { i , i } } \Bigg [ b _ { i } - \sum _ { j \neq i } a _ { i , j } x _ { j } \Bigg ]
$$

If we knew every value of $x _ { j }$ ,where $j \neq i$ , we could compute $x _ { i }$ directly. Of course, we do not know these values-they are what we are trying to determine-but if we had an estimate for every such value of $x _ { j }$ ,wecould come up with an estimate for $x _ { i }$ . The Jacobi algorithm relies upon estimates for every element of vector $\mathbf { x }$ to come up with a new estimate for $\mathbf { x }$ .It uses values computed for each variable $x _ { i }$ during iteration $t$ to generate new values during iteration $t + 1$ ：

$$
x _ { i } ( t + 1 ) \frac { 1 } { a _ { i , i } } \left( b _ { i } - \sum _ { j \neq i } a _ { i , j } x _ { j } ( t ) \right)
$$

A pseudocode version of the sequential Jacobi algorithm appears in Fig. 9-20.

The Jacobi algorithm is amenable to parallelization because the computation of each element of $\mathbf { x }$ may proceed simultaneously. The new estimate of $\mathbf { x }$ is computed from the old estimate of $\mathbf { X }$ and the value of A and $\mathbf { b }$

Let us consider how to implement a paralel Jacobi algorithm on a multicomputer.Asinthe case of gaussaneliminationthedata decomposition determines where in the algorithm communication is required. Suppose each processor isresponsible for acontiguous set of rows of A,as wellas the corresponding elements of b. With this data decomposition, processor interaction occurs at two places during every iteration of the do...while loop. First,every processor must have a copy of the entire vector X computed during the previous iteration. Hence every processor must broadcast its elements of x to all other processors. Second, although each processor may compute a local value of diff based upon the change in values of its own elements of x,these local values must be combined to yield a global value of diff Hence a max-reduction operation is necessary. At the end of the max-reduction step, every processor will have the same value for diff, which will cause all processors to exit the do...while loop on the same iteration.

Input n {Size of linear system) $\epsilon$ {Convergence criterion} $a [ 1 . . . n ] [ 1 . . . n ]$ {Coefficients of linear equations) $b [ 1 . . . n ]$ {Constants associated with equations) Output $\mathbf { \lambda } _ { x [ 1 \ldots n ] }$ {Old estimate of solution vector] Global newx[1..n] {New estimate of solution vector] diff {Maximum change of any element of solution} i， $j$ (Loop indices) begin {Estimate values of elements of $x$ } for $i \gets 1$ to $n$ do $x [ i ]  b [ i ] / a [ i ] [ i ]$ endfor {Refine estimates of x until values converge} do $d i f f \gets ~ 0$ for $i \gets 1$ to $n$ do $n e w x [ i ] \ \gets \ b [ i ]$ for $j \gets 1$ to $_ n$ do if $\textit { j } \neq \textit { i }$ then $n e w x [ i ] ~  ~ n e w x [ i ] ~ - ~ a [ i ] [ j ] ~ \times ~ x [ j ]$ endif endfor $n e w x [ i ] ~  ~ n e w x [ i ] / ~ a [ i ] [ i ]$ endfor for $i \gets 1$ to $n$ do $\begin{array} { l } { { d i f f  m a x ( \mathit { d i f f } , \mathit { \Delta } | x [ i ] \ - \ n e w x [ i ] | ) } } \\ { { x [ i ] \  \ n e w x [ i ] } } \end{array}$ endfor while $d i f f > \epsilon$ end

FIGURE 9-20 Sequential implementation of the Jacobi algorithm.

Figure 9-21 illustrates the parallelizability of the paralel Jacobi algorithm on the nCUBE 3200,for a linear system of size 128.

# 9.5.1 Sparse Linear Systems

As we discussed earlier,the discretization of partial differential equations often results in sparse linear systems. For example, consider the two-dimensional steady state temperature distribution problem illustrated in Fig. 9-22.A thin steel plate is surrounded on three sides by a condensing steam bath (temperature $1 0 0 ^ { \circ } \mathrm { ~ C ~ } )$ . The fourth side touches an ice bath (temperature $0 ^ { \circ } \mathrm { \bf C }$ ).An insulating blanket covers the top and the bottom of the plate. We must find the steadystate temperature distribution at 100 evenly spaced points forming a $1 0 \times 1 0$ mesh in the plate.

![](images/204c14c9b749c9235cd073cfd45f2bfbb735d7740a7f50703d8690253d9dcc36.jpg)  
FIGURE 9-21 Parallelizability of the parallel Jacobialgorithm solvinga dense $1 2 8 \times 1 2 8$ linear system on the nCUBE 3200 multicomputer.   
FIGURE 9-22 Two-dimensional steady state temperature distribution problem.   
One of 100 points where temperature is to be determined

This is an example of a linear second-order partial differential equation. When thesteadystate temperaturedistribution has been found,asetofiference equations relates the values of variables on neighboring mesh points:

$$
x _ { i , j } = \frac { x _ { i - 1 , j } + x _ { i , j - 1 } + x _ { i + 1 , j } + x _ { i , j + 1 } } { 4 }
$$

Here the subscripts $i$ and $j$ refer to the coordinates of the mesh points.

We could construct matrix A and vector b and use the Jacobi algorithm already described to solve for x. Because vector x has 1OO elements, matrix A would have size 100 × 100 and vector b would have size 100. This approach is inefficient,because matrix A is sparse,with only five nonzero elements per row.With only a constant number of nonzero elements in each row,we waste time executing an @(n) for loop to compute the new value of each element of x.

A better approach is constructing a version of the Jacobi algorithm using the previous equation, which performs the same computations more efficiently. In this procedure the values at all the mesh points are simultaneously updated, according to the formula

$$
x _ { i , j } ^ { ' } = \frac { x _ { i - 1 , j } + x _ { i , j - 1 } + x _ { i + 1 , j } + x _ { i , j + 1 } } { 4 }
$$

The values on the right-hand side of the equation are the old values of the variables; the value on the left-hand side represents the new approximation.

A sequential algorithm to solve the two-dimensional steady state temperature distribution problem appears in Fig. 9-23. Let's consider how to develop a parallel version of this algorithm suitable for implementation on a hypercube multicomputer. Each processor will be responsible for a subset of the elements of the two-dimensional matrix x and the corresponding elements of matrix newx. Notice that computing the value of an element of newx requires only the values of the four neighboring elements of x. If each processor is assigned a rectangular region of $x$ and newx,then computing elements of newx on the interior of the rectangle can be performed using locally available values of $x$ Computing elements of newx on the edge of the rectangle require values stored in the memories of other processors. If we assign regions to processors so that neighboring processors control neighboring regions,then nearest neighbor communications are sufficient to implement the parallel algorithm.

If every processor is responsible for a contiguous set of rows or a contiguous set of columns of $x$ and newx, then the interprocessor communication patern for computing newx forms aone-dimensional array.If every processor is responsible for a block of elements,thecommunication patern forms a twodimensional array.Both communication pattrns map into hypercubes,as we learned in Chap. 5.But which alocation of data to processors results in the faster algorithm?

Suppose we want to map an $n \times n$ mesh onto $p$ processors. To simplify the analysis, assume $n$ is a multiple of both $p$ and $\sqrt { p }$ . Consider first the roworiented data distribution scheme illustrated in Fig. 9-24a. Every processor manages a submesh of size $( n / p ) \times n$ .During each iteration every interior processor must send $n$ values to both its neighbors and receive $n$ values from these neighbors. If $\lambda$ is the message latency and $\beta$ is the time needed to transmit a single value, then the total time spent each iteration communicating values is

$$
4 ( \lambda + n \beta )
$$

Parameter n {Number of points in each dimensiol E {Convergence criterion} north[1...n], south[1...n], east[1...n], west[1...n] {Boundary conditions] Global $x [ 0 . . . ( n + 1 ) ] [ 0 . . . ( n + 1 ) ]$ {Solution) $n e w x [ 0 . . . n + 1 ] [ 0 . . . n + 1 ]$ {New estimate of solution} diff {Maximum change} i， $j$ {Loop indices} begin {Boundary conditions} for $i \gets 1$ to $n$ do $x [ 0 ] [ i ] \ \gets \ n o r t h [ i ]$ $x [ n + 1 ] [ i ] \  \ s o u t h [ i ]$ $x [ i ] [ 0 ] ~  ~ w e s t [ i ]$ $x [ i ] [ n + 1 ] ~  ~ e a s t [ i ]$ endfor {Initialize values of elements of $x$ } for $i \gets 1$ to $n$ do $x [ i ] ~  ~ 5 0$ endfor {Refine estimates of $x$ until values converge] do $d i f f \gets 0$ for $i \gets 1$ to $_ n$ do for $j \gets 1$ to $n$ do $\begin{array} { r } { \widetilde { \small { n e w x [ i ] [ j ] } } ~  ~ ( x [ i - 1 ] [ j ] ~ + ~ x [ i ] [ j - 1 ] ~ + ~ x [ i + 1 ] [ j ] ~ + ~ x [ i ] [ j + 1 ] ) / 4 } \end{array}$ endfor endfor for $i \gets 1$ to $n$ do for $j \gets 1$ to n do $\begin{array} { r l } & { d i f f \gets \mathsf { m a x } ( \mathop { d i f f } , \lvert n e w x [ i ] [ j ] - x [ i ] [ j ] \rvert ) } \\ & { x [ i ] [ j ] \gets n e w x [ i ] [ j ] } \end{array}$ endfor endfor whilediff $> \epsilon$ end

![](images/ea13b667aec14239e0ea31eb2ef7d88f7c0da62fb0a694ab246c8528f201ca86.jpg)  
Possible data distributions for solving the two-dimensional steady-state temperature distribution problem ona multicomputer. (a) illustration ofa 16 ×16 meshmapped onto 4 processors ina row-oriented fashion.Each processor manages an $( n / p ) \times n$ region.Shaded elements must be transmitted to neighboring processor. (b) llustration of a $1 6 \times 1 6$ meshmapped onto16 processors inablock-oriented fashion.Each processor managesa region of size $( n / { \sqrt { \mathsf { p } } } ) \times ( n / { \sqrt { \mathsf { p } } } )$ Shaded elements must be transmitted to neighboring processor(s).

Now consider the block-oriented data distribution scheme illustrated in Fig. 9-24b. Every processor manages a submesh of size (n/√p) × (n/√p). During each iteration every interior processor must send $n / { \sqrt { p } }$ values to all four neighbors and receive n/√P values from these neighbors.The total time spent communicating values in each iteration is

$$
8 { \bigg ( } \lambda + { \frac { n } { \sqrt { p } } } \beta { \bigg ) }
$$

Let's determine when the block-oriented approach is superior to the roworiented approach.

$$
\begin{array} { c } { { 8 \big ( \lambda + n \beta / \sqrt { p } \big ) < 4 ( \lambda + n \beta ) \Rightarrow } } \\ { { \mathrm { ~ } } } \\ { { \lambda < \big ( 1 - 2 / \sqrt { p } \big ) n \beta \Rightarrow } } \\ { { \mathrm { ~ } } } \\ { { n > \displaystyle \frac { \lambda } { \big ( 1 - 2 / \sqrt { p } \big ) \beta } } } \end{array}
$$

For example, suppose we are implementing a paralel version of the algorithm in Fig.9-23 on a 64-processor multicomputer for which $\lambda = 5 0 \beta$ .The block-oriented algorithm is superior to the row-oriented algorithm when

$$
n > \frac { 5 0 } { \left( 1 - \frac { 2 } { 8 } \right) 1 } \approx 6 6
$$

We assume in our analysis that $n$ is a multiple of $p$ , so we conclude that the row-oriented algorithm is slightly superior totheblock-oriented algorithm when $n = 6 4$ ,but the block-oriented algorithm is superiorfor $n = 1 2 8$ ,192,256,....

Until now we have concentrated on the interprocessor communication necessary to compute the value of newx. Interprocessor communication is also required to compute the global value of diff. On a hypercube multicomputer this reduction step has time complexity $\Theta ( \log p )$ . In the parallelization of the first Jacobi algorithm for dense linear systems,every iteration already has communication time complexity $\Theta ( \log p )$ ,and the reduction step does not increase the communication complexity of the algorithm. The second Jacobi algorithm relies upon neighbor communications to give each processor the values of $x$ it requires to compute newx. In this algorithm the introduction of an $\Theta ( \log p )$ communication step would be detrimental to the execution time of the parallel algorithm. We dodge the problem by modifying the algorithm so that the global value of diff is updated only once per $k$ iterations,where $k$ is some integer $\geq 1$ The best value of $k$ is a function of the architecture and the problem type. If $k$ is too small,time iswastedfinding the global value of diff when further iterations are necessary.If $k$ is too large, time is wasted performing further iterations when the values of $x$ have already converged on a solution.

# 9.6 THE GAUSS-SEIDEL ALGORITHM

The Jacobi algorithm attempts to solve the system of equations $\mathbf { A } \mathbf { x } = \mathbf { b }$ through repeated applications of the assignment

$$
x _ { i } ( t + 1 ) \frac { 1 } { a _ { i , i } } \Biggl ( b _ { i } - \sum _ { j \neq i } a _ { i , j } x _ { j } ( t ) \Biggr )
$$

where $x _ { i } ( k )$ is the value of $x _ { i }$ computed during iteration $k$ . The Gauss-Seidel algorithm atempts to increase the rate at which the values of x converge upon a solution by always using the most recently computed value for each element xi. For example, the following equation illustrates how new values of xi are computed when the evaluation order is x1, x2,..., Xn:

$$
x _ { i } ( t + 1 ) \frac { 1 } { a _ { i , i } } \left( b _ { i } - \sum _ { j < i } a _ { i , j } x _ { j } ( t + 1 ) - \sum _ { j > i } a _ { i , j } x _ { j } ( t ) \right)
$$

Other evaluation orders are also possible. For example, the variables could be updated in the order xn, Xn-1, ...,x1. The Gauss-Seidel algorithm can produce different results on the same input if the variable evaluation order is changed.

Let us consider the parallelism inherent in the Gauss-Seidel algorithm. First we consider the case where matrix A is dense. Assume without loss of generality that the variable evaluation order is x1, x2,..., xn. If matrix A is dense, then the algorithm has a significant sequential component, because the value of xi(t +1) must be determined before finishing the computation of xi+1(t +1), for all $1 \leq i < n$

If matrix A is sparse, then the Gauss-Seidel algorithm is more amenable to paralelization. Consider the solution of the two-dimensional heat eauation seen in Sec. 9.5. The values at all the mesh points are updated according to the formula

![](images/a9ad43f40d2c2dd26c3e00908147a93451e302bc04856d14723ab75641c60049.jpg)  
FIGURE 9-25 (a) Data dependencies in a single iteration of the Gauss-Seidel algorithm. (b) Two colors aresuficient to label every vertex of the data dependency graph so that each pair ofadjacentverticeshasonevertexofeachcolor.Thisisusualycalleda“red-black" coloring scheme.All vertices having the same color may be updated simultaneously in the parallel Gauss-Seidel algorithm.

$$
x _ { i , j } ( t + 1 ) = \frac { x _ { i - 1 , j } ( t + 1 ) + x _ { i , j - 1 } ( t + 1 ) + x _ { i + 1 , j } ( t ) + x _ { i , j + 1 } ( t ) } { 4 }
$$

Figure 9-25a illustrates the data dependencies for a $4 \times 4$ mesh of variables. The new value of $x _ { 1 , 1 }$ must be computed first. Once the parallel algorithm has computed $x _ { 1 , 1 }$ , it may compute $x _ { 1 , 2 }$ and $x _ { 2 , 1 }$ in parallel. With newly computed values of x1,2 and x2,1,the parallel algorithm may simultaneously compute x1.3, $x _ { 2 , 2 }$ ,and $x _ { 3 , 1 }$ .At the same time it may compute the next iteration's value for $x _ { 1 , 1 }$ ·

Continuing in this fashion,the parallel algorithm in the next step can compute $x _ { 1 , 4 } , \ x _ { 2 , 3 } , \ x _ { 3 , 2 } , \ x _ { 4 , 1 } , \ x _ { 1 , 2 }$ ,and $x _ { 2 , 1 }$ . Concluding this argument, the set of variables is divided into two sets.Each set representsa group of variables thatmaybeupdatedsimultaneously.Figure9-25bilustrates thepartioning of the variables intothese two sets,is called a red-black coloringof thedata dependency graph.

# 9.7 JACOBI OVERRELAXATION AND SUCCESSIVE OVERRELAXATION

Jacobi overelaxation is a variant of the Jacobi algorithm that computes the new value of each $x _ { i }$ through a combination of the old value of $x _ { i }$ and the new value of $x _ { i }$ computed by using the standard Jacobi algorithm. Jacobi overrelaxation replaces the update operation shown in equation 9.24 with

$$
x _ { i } ( t + 1 ) = ( 1 - \gamma ) x _ { i } ( t ) + \frac { \gamma } { a _ { i , i } } \left( b _ { i } - \sum _ { j \neq i } a _ { i , j } x _ { j } ( t ) \right)
$$

Successive overrelaxation (SOR) is a variant of the Gauss-Seidel algorithm that computes the new value of each xi through a combination of the old value of xi and the new value of xi, computed by using the standard Gauss-Seidel algorithm. Successive overrelaxation replaces the update operation shown in equation 9.33 with

$$
x _ { i } ( t + 1 ) = ( 1 - \gamma ) x _ { i } ( t ) + \frac { \gamma } { a _ { i , i } } \left( b _ { i } - \sum _ { j < i } a _ { i , j } x _ { j } ( t + 1 ) - \sum _ { j > i } a _ { i , j } x _ { j } ( t ) \right)
$$

When $\gamma$ is chosen properly, Jacobi overrelaxation and SOR can converge to a solution much faster than the Jacobi and Gauss-Seidel algorithms, respectively.

# 9.8 MULTIGRID METHODS

Multigrid methods form a class of iterative algorithms used for the numerical solution of partial differential equations. The motivation for multigrid methods springs from two observations:

1. Iterative algorithms converge to solutions faster on coarser grids than on finer grids 2. Iterative algorithms converge quicker if the initial approximations of the values of the variables are good

A multigrid method finds a discrete solution to a partial differential equation by iterating between finer and coarser grids, using the values computed at the previous set of grid points to generate initial estimates for the values at the new set of grid points (see Fig. 9-26). In this section we describe the computations performed by multigrid methods and the communications necessary to implement these computations on a multicomputer.

To simplify the discussion, we consider the execution of multigrid methods on two-dimensional grids. Suppose the finest grid, $G ^ { 0 }$ ,has dimension $n \times n$ ， where $n$ is a power of 2. We denote coarser grids by $G ^ { i }$ ,where $1 \leq i < \log n$ With every grid point $( i , j )$ in grid $G ^ { k }$ there isanasociatedvarable $x _ { i , j } ^ { k }$ Multigrid algorithms perform three kinds of computations:

1. Relaxation: Compute thevalues of all $x _ { i , j } ^ { k }$ on grid $G ^ { k }$ . This computation is performdngheJcbissdelJcoierrelation another iterative algorithm.

2.Interpolation: Compute values of finer grid variables on grid $G ^ { k - 1 }$ as a function of coarser grid variables on grid $G ^ { k }$ . One interpolation algorithm computes the value of $x _ { i , j } ^ { k - 1 }$ to betheaverageoftheueson $G ^ { k }$ closest to location $( i , j )$ .Foreamplesingtsitep $x _ { 3 , 5 } ^ { 0 }$ would be assignedtheaveragef2.4442d4

![](images/954815413bd8e3f806b135bb245cb1a332785c627585078a64054e24252b6fbf.jpg)  
FIGURE 9-26 Illustration of grids used inthemultigrid algorithm.The finest $( 1 6 \times 1 6 )$ grid is $G ^ { 0 }$ $G ^ { 1 }$ isthe $8 \times 8$ grid, $G ^ { 2 }$ isthe $4 \times 4$ grid,and $G ^ { 3 }$ is the $2 \times 2$ grid.

3. Projection: Compute values of coarser grid variables on grid Gk as a func  
tion of finer grid variables on grid Gk-1. A simple projection algorithm, called $x _ { i , j } ^ { k - 1 }$ $x _ { i , j } ^ { k }$ $x _ { 4 , 4 } ^ { 2 }$ $x _ { 4 , 4 } ^ { 1 }$

We have described the communication requirements of relaxation algorithms in previoussections.Here we focus on thecommunications required to support interpolation and projection on two-dimensional meshes and hypercubes.

Suppose we map the finest grid $G ^ { 0 }$ onto an $n \times n$ mesh of processors. Performing relaxation on $G ^ { 0 }$ requires only nearest neighbor communications. However, the processors that must communicate in order to perform relaxation on the coarser grids $G ^ { 1 }$ ， $G ^ { 2 }$ 。..， $G ^ { \log n }$ are no longeradjacent.Communicating processors are distance two apart when performing relaxation on $G ^ { 1 }$ ,distance four apart when performing relaxation on $G ^ { 2 }$ ,and so on.Depending upon the hardware of the target architecture, this communication may or may not have a significant impact on the performance of the algorithm.

Now let's consider mapping grids $G ^ { 0 }$ through $G ^ { \log n - 1 }$ onto a hypercube. As we saw in Chap.5,it is possible to embed a two-dimensional mesh into a hypercube using a binary Gray code. Thus we can map the points of grid $G ^ { 0 }$ into the nodes of the hypercube so that every pair of neighboring mesh vertices are mapped to neighboring hypercube nodes. However, it is not possible to find a mapping so that this property is preserved for every grid, $G ^ { 0 }$ through Glogn-1, because there are not enough connections. In the worst case, a node has $4 \log n - 2$ neighbors in the $n \times n$ multigrid mesh,while ithas only $2 \log n$ neighbors in a hypercube of dimension $n ^ { 2 }$ .For example, consider the $8 ~ \times$ 8 multigrid mesh ilustrated inFig.9-27.Node18 has10 neighbors.Since every node in a 64-node hypercube has only six neighbors, the mesh can't be embedded in the hypercube with dilation 1.

![](images/4cb9875e65f14f3cb1c575962933e9983d564cc4e02e6159d1eb90a41102f41b.jpg)  
FIGURE 9-27 Mapping a two-dimensional multigrid into a hypercube ensuring that neighboring processors in $G ^ { 0 }$ aremapped to neighboring nodes in the hypercube,and neighboring processors in $G ^ { \uparrow }$ and $G ^ { 2 }$ are mapped to nodes distance 2 apart in the hypercube.

For this reason we embed the multigrid mesh in the hypercube so that neighboring nodes in $G ^ { 0 }$ are neighboring nodes in the hypercube and neighboring nodes in $G ^ { 1 }$ through $G ^ { \log n }$ are distance 2 away in the hypercube. Using the technique first described in Chap.5,we divide the processor number into two fields,one representing the row and the other representing the column. We use a Gray code to map adjacent row and column elements to adjacent hypercube nodes.

# 9.9 CONJUGATE GRADIENT

In this section we describe the conjugate gradient method, used to increase the convergence rate of solutions to linear systems in which the coefficient matrix is positive definite.

An iteration of the conjugate gradient method is of the form

$$
x ( t ) = x ( t - 1 ) + s ( t ) d ( t )
$$

The new value of vector $\mathbf { X }$ is a function of the old value of vector $\mathbf { X }$ ascalar step size $s$ ,and a direction vector $\mathbf { d }$

The values of $\mathbf { X }$ are guaranteed to converge in, at most, $n$ iterations. Before iteration 1, values of x(O), d(O) and g(O) must be set. In our implementation of the algorithm $\mathbf { x } ( 0 )$ and ${ \bf d } ( 0 )$ ,both are initialized tothezerovectorand ${ \bf g } ( 0 )$ is initialized to $- \mathbf { b }$ Every iteration $t$ calculates $\mathbf { x } ( t )$ in four steps.

Step 1: Compute the gradient

$$
g ( t ) = A x ( t - 1 ) - b
$$

Step 2: Compute the direction vector

$$
d ( t ) = - g ( t ) + \frac { g ( t ) ^ { T } g ( t ) } { g ( t - 1 ) ^ { T } g ( t - 1 ) } d ( t - 1 )
$$

where g(t)Tg(t) represents the inner product of the transpose of vector g(t) and vector ${ \bf g } ( t )$

Step 3: Compute the step size

$$
s ( t ) = - \frac { d ( t ) ^ { T } g ( t ) } { d ( t ) ^ { T } A d ( t ) }
$$

Step 4: Compute the new approximation of $\mathbf { X }$ ：

$$
x ( t ) = x ( t - 1 ) + s ( t ) d ( t )
$$

The conjugate gradient algorithm converges upon a solution after at most $n$ iterations (Bertsekas and Tsitsiklis 1989).

Apseudocodeimplementationof theconjugategradientmethodappears in Fig. 9-28. The program cals subroutines INNER.PRODUCT and MATRIX.VECTOR.PRODUCT,detailed in Fig.9-29.

Let's consider the paralel implementation of the conjugate gradient algorithm on a distributed memory architecture. Assume each processor has in its local memory one or more rows of $^ a$ ,as well as the corresponding elements of vectors $b , \ d$ ，and $g$ . Given this data decomposition, the only interprocessor communications occur within functions INNER.PRODUCT and MATRIX.VECTOR.PRODUCT.

Inside the parallel version of function INNER.PRODuCT,every processor computes the sum of its local products. When a processor has computed its subtotal, it performs a sum reduction with the other processors to determine the inner product. The parallel version of the function has communication time complexity $\Theta ( n / p + \log p )$ ,where $n$ is the size of the linear system and $p$ is the number of processors.

Function MATRIX.VECTOR.PRODUCT requires each processor to have access to every other processor's portion of vector $b$ at some point during the computation. One way to do this is to fan-in the processors' components of $b$ to the memory of a single processor, then have that processor broadcast the entire array $b$ to the other processors. This strategy results in a communication time complexity of $\Theta ( n \log p )$ ·

Parameter n E   
Input $a [ 1 . . . n ] [ 1 . . . n ]$ $b [ 1 . . . n ]$   
Output $x [ 1 . . . n ]$   
Global $d [ 1 . . . n ]$ $g [ 1 . . . n ]$ i iteration S denoml,denom2, num1, num2, tmpvec[1...n]   
(Size of linear system}   
{Convergence criterion}   
{Coefficients of linear system}   
{Right-hand side of equations)   
{Solution vector}   
{Direction vector}   
{Gradient vector}   
{Vector element being manipulated)   
{Iteration number}   
{Step size}   
{Temporary variables)   
begin for $i \gets 1$ to $n$ do $\begin{array} { l } { d [ i ] ~  ~ 0 } \\ { x [ i ] ~  ~ 0 } \\ { g [ i ] ~  ~ - b [ i ] } \end{array}$ endfor for iteration $ 1$ to $n$ do denoml INNER.PRODUCT $( g [ 1 . . . n ] , g [ 1 . . . n ] )$ $g [ 1 . . . n ] \ $ MATRIX.VECTOR.PRODUCT (a[1...n][1..n], x[1...n]) for $i \gets 1$ to $n$ do $g [ i ]  g [ i ] - b [ i ]$ endfor num1 INNER.PRODUCT $( g [ 1 . . . n ] , g [ 1 . . . n ] )$ if num1 $< \epsilon$ break endif for $i \gets 1$ to $n$ do $d [ i ] ~  ~ - g [ i ] ~ + ~ ( n u m e r a t o r / d e n o m i n a t o r ) \times ~ d [ i ]$ endfor num $2 $ INNER.PRODUCT $( d [ 1 . . . n ] , g [ 1 . . . n ] )$ tmpvec[1..n] MATRIX.VECTOR.PRODUCT (a[1..n][1...n],   
$d [ 1 . . . n ] )$ denom $2 $ INNER.PRODUCT (d[1...n], t.mpvec[1...n]) $s \gets - n u m 2 \ /$ denom2 for $i \gets 1$ to $n$ do $x [ i ] \  \ x [ i ] \ + \ s \ \times \ d [ i ]$ endfor endfor   
end   
INNER.PRODUCT (a[1...n], b[1...n]): Value a[1...n], b[1...n] Local i,result   
begin result $ 0$ for $i \gets 1$ to $n$ do result $ \ r e s u l t \ + \ a [ i ] \ \times \ b [ i ]$ endfor return result   
end   
MATRIX.VECTOR.PRODUCT (a[1..n][1...n], b[1...n]): Valuea[1...n][1..n], b[1...n] Local i, $j$ ,result[1..n]   
begin for $i \gets 1$ to $_ n$ do result[i] $ \mathrm { ~ 0 ~ }$ for $j \gets 1$ to $_ n$ do result[i] result[i] + a[i]j] × b[j] endfor endfor return result[1...n]   
end

FIGURE 9-29 Functions calld as subroutines by program CONJUGATE.GRADIENT (see Fig. 9-28). Function INNER.PRODUCTreturnsa scalarvaluerepresenting theinnerproduct (dotproduct) of twovectors.FunctionMATRIX.VECTOR.PRODUCTreturnsavector representing the product of a matrix and a vector.

Many problems in science and engineering can be expressed as systems of linear equations. In this chapter we surveyed several sequential algorithms used to solve systems of linear equations,and we considered how to implement parallel versions of these algorithms on both shared memory and distributed memory systems.

We began with an examination of the back substitution algorithm to solve upper triangular systems.Next we considered the odd-even reduction algorithm for solving tridiagonal systems. Then we looked at the well-known gaussian elimination algorithm for solving arbitrary linear systems.All these algorithms are direct--the number of steps performed by the algorithm is independent of the particular system's coeffcient values.

The last portion of the chapter discussed iterative algorithms for solving linear systems. The execution time of these algorithms is a function of the coefficients of the system being solved. Iterative algorithms are frequently used to solve large, sparse systems arising from the solution of partial differential equations.We examined two versions of the Jacobi algorithm. The first is suitable for solving arbitrary systems; the second is useful when variables have a structured relationship to each other, as in the solution to the two-dimensional heat equation.We also looked at the Gauss-Seidel algorithm, which can exhibit faster convergence than the Jacobi algorithm,as well as variants of these algorithms, Jacobi overrelaxation and successive overrelaxation. Multigrid methods, which further accelerate convergence upon a solution, were also discussed. Finally, we discussed the parallelizability of the conjugate gradient algorithm, an iterative algorithm that can converge rapidly onto a solution when the system is positive definite.

# 9.11 BIBLIOGRAPHIC NOTES

Bertsekas and Tsitsiklis (1989) are the primary source for this chapter. They discuss algorithms to solve nonlinear problems, shortest path problems,network flow problems,and many other topics. Other books that describe parallel numerical algorithms include Dongarra et al. (1991); Fox et al. (1988); Hockney and Jesshope (1981); Hord (1990), Kowalik (1985); and Schendel (1984). Sameh (1977) and Heller (1978) have surveyed parallel numerical algorithms.

Romine and Ortega (1988) have demonstrated that a triangular system solver can be implemented eficiently on a multicomputer “if the machine is able to accomplish fan-in communication reasonably efficiently.”

Odd-even reduction (also called cyclic reduction) can be used to solve firstorder recurrence relations.The algorithm was introduced by Kogge and Stone (1973).

Many articles describe paralel algorithms for solving tridiagonal linear systems. A sampling includes Kim and Lee (1990); Krechel et al. (1990); Lin and Chung (1990); Piskoulisjki (1992);Reale (1990); Sun et al. [1992];and van der Vorst (1987a,1987b).

Bini (1984) presents a parallel algorithm for solving certain Toeplitz linear systems.

Articleson the solution of banded linear systems includeBar-On (1987)and Oyama et al. (1990).

Galivan et al. (1990) have surveyed parallel algorithms for dense linear algebra computations.

References in the literature to parallel algorithms for solving dense linear systems using gaussian elimination or LU decomposition include Bader and Gehrke (1991);Bampis etal. (1991);Bjorstad (1987);BoreddyandPaulraj (1990); Chu and George (1987); Cosnard et al. (1988); Dongarra (1984); Dongarra and Johnsson (1987); Dongarra and Sameh (1984); Geist and Heath (1986)；Marrakchi and Robert (1989); Ortega (1988); Ortega and Romine (1988); Parkinson and Wunderlich (1984);and Yuand Wang(990).

Sameh and Kuck (1978) and Cosnard and Robert (1986) present parallel algorithms for $Q R$ factorization.

Heath et al. (1991) have surveyed parallel algorithms for sparse linear systems. Aykanat et al. (1988) have examined iterative algorithms for solving large sparse systems on hypercube multicomputers. Alaghband and Jordan (1989) have studied sparse gaussian elimination on UMA multiprocessors.

Dimitriadis and Karplus (1990) describe the solution of ordinary differential equations on multiprocessors.

Ortega and Voigt (1985) survey the literature regarding the solution of partial differential equations on vector and parallel computers.

Gropp (1987) and Patrick et al. (1987) have studied the effect of data distribution on the performance of parallel algorithms used to solve partial differential equations. Other papers describing parallel implementation of the SOR algorithm include Bonomo and Dyksen (1989);Evans (1984); and Missirlis (1987); Robert and Trystram (1988) present results that improve upon the work of Missirlis (1987).

Fox and Oto (1984); Reed et al. (1987); and Vrsalovic etal. (1985) explore how the performance of MIMD computers solving partial differential equations is influenced by the interaction between the discretization stencil and the data partitioning.

References to parallel multigrid algorithms include Alef (1991); Chan and Saad (1986); Hoppe and Muhlenbein (1986);Ribbens (1989); and Yadlin and Caughey (1991).

Parallel conjugate gradient algorithms are discussed in Chronopoulos and Gear (1989);Decker etal. (1992);di BrozoloandRobert (1989);Meurant (1987), and O'Leary (1987).

Uresin and Dubois (1990) provide sufficient conditions for the convergence of asynchronous itertive algorithms.Dubois and Briggs (1991) develop a model to estimate the effects of hardware and software contention on the efficiency of asynchronous algorithms.

# 9.12 PROBLEMS

9-1Is the linear system that is a result of the problem illustrated in Fig. 9-1 tridiagonal?

9-2Is the tridiagonal linear system that is a result of the problem illustrated in Fig. 9-2 diagonally dominant? Is it positive definite?

9-3Why is line 6 of the back substitution algorithm,

$$
a [ j ] [ i ]  0
$$

not needed?

9-4 Forward substitution is an analog to the back substitution algorithm. It is used to solve lower triangular systems.Write a sequential forward substitution algorithm in pseudocode.

9-5Prove that it is possible to implement the odd-even reduction algorithm in $\Theta ( n )$ time using $\Theta ( n / \log p )$ processors on the CREW PRAM.

Devise an algorithm implementing gaussian elimination without pivoting on the 2-D mesh SIMD model. Analyze the time complexity of the parallel algorithm.

9-7Show that a lower bound on the complexity of performing gaussian elimination with row pivoting on the 2-D mesh SIMD model is $\Omega ( n ^ { 4 / 3 } )$ (Bertsekas and Tsitsiklis 1989).

9-8 Describe a way to reduce the communication overhead of the row-broadcast step of the parallel gaussian elimination algorithm by overlapping some of the communication with computation.

9-9If a column-oriented gaussian elimination algorithm is implemented, the columns should be interleaved among the processors. In other words, given $n$ columns and $p$ processors, column i should be assigned to processor( $i$ modulo $p$ ),for $0 \leq i \leq n - 1$ .Whyisan interleaved, rather than a contiguous,allocation of columns to processors important for high efficiency?

9-10 Write a multicomputer-targeted gaussian elimination algorithm in which columns of the coefficient matrix A are mapped to processors.

Write a parallel program implementing the more general version of the Jacobi algorithm capable of solving arbitrary linear systems.

-12Write a parallel program implementing a version of the Jacobi algorithm capable of solving the two-dimensional heat equation.

9-13 The analysis of the row-oriented versus block-oriented versions of the parallel Jacobi algorithm for the two-dimensional heat equation assumes that sending and receiving messages cannot occur simultaneously. Do the analysis again, assuming that message sends and receives happen simultaneously.

9-14 Write two parallel programs implementing parallel Gauss-Seidel algorithms for UMA multiprocessors. In the first algorithm processes should synchronize when they exchange the values of boundary variables. The synchronization ensures that each process is getting the current value. The second algorithm should be asynchronous. When a process needs the value of a boundary variable updated by another process, it grabs the value currently in that location. Compare the performance of these two parallel programs.

${ \bf 9 . 1 5 * }$ Prove that the multigrid-into-hypercube embedding described in this book has the property that neighboring nodes in $G ^ { 0 }$ are neighboring nodes in the hypercube and neighboring nodes in $G ^ { 1 }$ through $G ^ { \log n }$ are distance two away in the hypercube.

9-16Write a parallel program implementing a simple multigrid algorithm that uses relaxation and interpolation,but not projection. Your algorithm should begin by performing relaxation on the coarsest grid until the values converge,then interpolating these values onto the next finer grid and perform relaxation on that grid.The algorithm should repeat this process until it has performed relaxation on the finest grid.

9-17 Write a parallel program implementing the conjugate gradient algorithm. Test your algorithm on a positive definite system and ona linear system that is not positive definite. What happens in each case?

# 10

# SORTING

Had I been present at the creation,I would have given some useful hints for the better ordering of the universe.

Reaction of Alfonso X to a description of the intricasies of the Ptolemaic system

Sorting is one of the most common activities performed on serial computers.Many algorithms incorporate a sort so that information may be accessed efficiently later. Sorting has additional importance to designers of parallel algorithms; it is frequently used to perform general data permutations on distributed memory computers. These data-movement operations can be used to solve problems in graph theorycomputational geometry,and image processing in optimal or near optimal time.

Much work has been done developing parallel sorting algorithms,and we can do little more than explore the basics in this chapter. We will examine a variety of sorting algorithms for processor arrays, multiprocessors, and multicomputers. All these algorithms are internal sorts-that is,they sort tables small enough to fit entirely in primary memory. In addition, all the algorithms described in this chapter sort by comparing pairs of elements.

A nonstandard CRCW PRAM can sort $n$ elements in constant time (if the time needed to spawn n² processors is not counted). We describe a constanttime enumeration-sort algorithm in Sec. 10.1. In Sec. 10.2 we explore the lower bounds of sorting on more practical parallel architectures. Section 10.3 describes odd-even transposition sort, an optimal algorithm for processor arrays organized as a one-dimensional mesh. The much-cited bitonic merge sort algorithm is the subject of Sec. 10.4. We explore the implementation of bitonic merge sort for a variety of processor organizations. In Sec. 10.5 we discuss several quicksort-based parallel algorithms suitable for implementation on MIMD computers. Section 10.6 describes random read and random write and explains how we can use sorting to implement these general data-routing strategies.

# 10.1 ENUMERATION SORT

Assume that we are given a table of $n$ elements, denoted $a _ { 0 } , a _ { 1 } , \ldots , a _ { n - 1 }$ ,on which a linear order has been defined. Thus for any two elements $a _ { i }$ and $a _ { j }$ , exactly one of the following cases must be true: $a _ { i } ~ < ~ a _ { j }$ ， $a _ { i } ~ = ~ a _ { j }$ ,or $a _ { i } > a _ { j }$ . The goal of sorting is to find a permutation $( \pi _ { 0 } , \pi _ { 1 } , \ldots , \pi _ { n - 1 } )$ such that $a _ { \pi _ { 0 } } \leq a _ { \pi _ { 1 } } \leq \cdots a _ { \pi _ { n - 1 } }$

An enumeration sort computes the final position of each element in the sorted list by comparing it with the other elements and counting the number of elements having smaller value (Knuth 1973). If $j$ elements have smaller value than $a _ { i }$ ,then $\pi _ { j } = i$ ; i.e., element $a _ { i }$ is the $( j + 1 )$ element on the sorted list, following aπo,...,aπj-1'

If two or more elements have the same value, we must amend the algorithm slightly. If,for each element in the unsorted list, the algorithm counts the number of elements having smaller value or the same value and smaller index in the unsorted list, the algorithm will produce a unique count for each list element.

Muller and Preparata (1975) have shown that a nonstandard PRAM model can perform an enumeration sort in logarithmic time. In fact, the algorithm requires $\Theta ( \log n )$ time to spawn $n ^ { 2 }$ processors and $\Theta ( 1 )$ time to perform an the sort.If the sort issimply asubroutine toamore general algorithm that requires at least n² active processors, then it is fair to disregard the processor spawning time and consider that the sort has constant time complexity.

Imagine a CRCW PRAM model in which,if multiple processors simultaneously write values to a single memory location,the sum of the values is assigned to that location. This model is not as radical as we might think-its conflict resolution mechanism is similar to the fetch-and-add mechanism of the New York University Ultracomputer (Almasi and Gottlieb 1989).

Given n² processors,this CRCW PRAM model can compare every pair of elements and compute each element's list position in constant time. Once the machine has computed each element’s position, one more step is sufficient to move the element to its sorted location. See Fig.10-1.

Unfortunately,even if we make the assumptions described earlier and call this a constant-time algorithm,it is not cost optimal. It performs O(n2) comparisons, whereas a good sequential algorithm can sort a list of n elements with only ?(n log n) comparisons. In addition, the algorithm relies upon a powerful PRAM model. Moving tothe CREW PRAMmodel, for example, would lead to further increases in the cost of the parallel algorithm. Hence we must look elsewhere for a parallel algorithm suitable for implementation on an actual parallel computer.

Parameter n {Number of elements] Global $a [ 0 . . . ( n - 1 ) ]$ {Elements to be sorted} position[o...(n \~ 1)] {Sorted positions} sorted[0...(n - 1)] {Contains sorted elements] begin spawn ( $P _ { i , j }$ , for all $0 ~ \leq ~ i , ~ j ~ < ~ n )$ for all $P _ { i , j }$ where $\mathrm { ~ { ~ \bf ~ 0 ~ } ~ } \le \mathrm { ~ \it ~ { ~ i ~ } ~ }$ $\textit { j } < \textit { n }$ do position[i] $ 0$ if $a [ i ] ~ < ~ a [ j ]$ or $( a [ i ] = a [ j ]$ and $\textit { i } \textbf { < } j )$ then position[i] $ 1$ endif endfor for all $P _ { i , 0 }$ where $0 ~ \leq ~ i ~ < ~ n$ do sorted[position[i] $]  a [ i ]$ endfor end

FIGURE 10-1 A set of $n$ elements can be sorted in $\Theta ( \mathsf { l o g } n )$ time with $n ^ { 2 }$ processors, given a CRCw PRAMmodel inwhere simultaneouswrites tothe samememory locationcause the sum of the values to be assigned.If the time needed to spawn the processors isnot counted， thealgorithm executes in constant time.

# 10.2 LOWER BOUNDS ON PARALLEL SORTING

Section 10.1 has demonstrated that sorting can be performed in constant time, given enough processors and a model of parallel computation powerful enough. Whatare the lower bounds for sorting on more reasonable models of parallel computation? In this section we derive lower bounds for sorting on one- and two-dimensional meshes and the shufle-exchange network.

Theorem 10.1. Assume that $n$ elements are to be sorted on a processor array organized as a one-dimensional mesh.Also assume that before and after the sort the elements are to be distributed evenly,one element per processor.Thena lower bound on the time complexity of any sorting algorithm is $\Theta ( n )$ ·

Proof. The bisection width of a one-dimensional mesh network with $n$ nodes is 1. Suppose the sorted positions of all elements originally on one side of the bisection are on the other side of the bisection,and vice versa. Then all $n$ elements must pass through one link to reach the other side. Since a link can only carry one element at a time, the number of time steps needed to swap elements across the bisection is at least $n$ .Hence a lower bound on the complexity of any sort on the one-dimensional mesh network executing under the given constraints is $\Theta ( n )$ 。

Theorem 10.2. Assume that $_ n$ elements are to be sorted on a processor array organized as a two-dimensional mesh. Also assume that before and after the sort the elements are distributed evenly, one element per processor. Thena lower bound on the time complexity of any sorting algorithm is $\Theta ( { \sqrt { n } } )$ ·

Proof. The bisection width of a two-dimensional mesh network with $n$ nodes is less than or equal to $\left\lceil { \sqrt { n } } \right\rceil$ . Suppose the sorted positions of all elements originally on one side of the bisection are on the other side of the bisection,and vice versa. Then all $n$ elements must pass through one of no more than $\lceil { \sqrt { n } } \rceil$ links to reach the other side.Since a link can only carry one element ata time,the number of steps needed to swap elements across the bisection is at least $n / \left\lceil { \sqrt { n } } \right\rceil$ .Hence a lower bound on the complexity of any sort on a processor array organized as a two-dimensional mesh and executing under the given constraints is $\Theta ( n / \left\lceil { \sqrt { n } } \right\rceil ) = \Theta ( { \sqrt { n } } )$

Theorem 10.3. Assume that $n = 2 ^ { k }$ elements are to be sorted on a processor array organized as a shuffle-exchange network.Also assume that before and after the sort the elements are distributed evenly,one element per processor. A lower bound on any sorting algorithm is $\Theta ( \log n )$

Proof. Suppose the sorted position of an element originally at node O is node $n - 1$ Moving that element fromnode O to node $n - 1$ demands at least $\log n$ exchange operations and at least $\log n - 1$ shuffle operations. For this reason a lower bound on any shufle-exchange-based sorting algorithm executing under the given constraints is $\Theta ( \log n )$ ·

# 10.3 ODD-EVEN TRANSPOSITION SORT

The odd-even transposition sort is designed for the processor array model in which the processing elements are organized into a one-dimensional mesh. Assume that $A = ( a _ { 0 } , a _ { 1 } , \dotsc , a _ { n - 1 } )$ is the set of $n$ elements to be sorted. Each of the $n$ processing elements contains two local variables: $a$ ,aunique element of array $A$ ,and $t$ ,a variable containing a value retrieved froma neighboring processing element.

The algorithm performs $n / 2$ iterations, and each iteration has two phases. In the first phase, called odd-even exchange,the value of $a$ inevery oddnumbered processor (except processor $n - 1 \mathrm { \Omega }$ is compared with the value of $a$ stored in the successor processor.The values are exchanged,if necessaryo that the lower-numbered processor contains the smaller value. In the second phase, called even-odd exchange, the value of a in every even-numbered processor is compared with the value of $a$ in the successor processor. As in the first phase,thealues areexhanged,ifcessary,sothat the lower-numd processor contains the smaller value. After n/2 iterations the values must be sorted. Fig. 10-2 contains the odd-even transposition sort algorithm. An example of this algorithm's execution appears in Fig. 10-3.

Theorem 10.4. The complexity of sorting n elements on a one-dimensional mesh processor array with n processors using odd-even transposition sort is (n). (See Habermann 1972.)