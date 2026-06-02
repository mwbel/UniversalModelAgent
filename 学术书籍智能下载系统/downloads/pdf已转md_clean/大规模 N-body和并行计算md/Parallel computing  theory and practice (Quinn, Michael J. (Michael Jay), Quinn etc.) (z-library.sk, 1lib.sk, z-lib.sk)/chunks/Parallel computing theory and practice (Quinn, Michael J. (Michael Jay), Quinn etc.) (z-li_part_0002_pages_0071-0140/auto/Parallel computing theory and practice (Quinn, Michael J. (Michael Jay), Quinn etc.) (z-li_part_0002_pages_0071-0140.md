We briefly described how one PRAM modelcan simulate another. For more information on the relationship between CREW PRAM models, see Fich et al. (1988).

We presented only the most common PRAM models in this chapter. The literature contains a variety of PRAM models. Some authors give different names to‘models we have discussed. Other authors have introduced models with unique capabilities. Here are a few references from the extensive literature on the subject.

Quinn and Deo (1984) and the first edition of this book,Designing Efficient Algorithms for Parallel Computers,referred to PRAM models as SIMD-SM: SIMD for the single instruction stream, multiple data-stream style of execution, and SM for shared memory.Perhaps for similar reasons,Akl (1989) refers to PRAM models as SM SIMD computers.

The SP-RAM (Shiloach and Vishkin 1982a) is identical to the ARBITRARY PRAM. The RP-RAM (Shiloach and Vishkin 1981) allows simultaneous reading and writing as well. If $m$ processors attempt to write a value into the same memory location simultaneously, then exactly one processor succeeds,and the probability of each processor succeeding is $1 / m$

Goldschlager's SIMDAG model (1982) is identical to the PRIORITY PRAM.

The PP-RAM (Reif 1982) is a PRAM with processors having the added capability to perform independent probabilistic choices on a fixed input. Probabilistic parallel algorithms often haveamuch lower expected time complexity than nonprobabilistic parallel algorithms.

As we have noted, the PRAM is not a realistic model. Algorithms to simulate PRAM computations on parallel models giving processors more restricted access to memory locations have been published by Alt et al. (1987),Karlin and Upfal (1988), Melhorn and Vishkin (1984), Upfal (1984), and Upfal and Wigderson (1987). Valient (1990) has proposed the bulk-synchronous parallel (BSP) model as an efficient bridge between parallel software and parallel hardware.

Fisher (1988) and Vitanyi (1988) have contested the PRAM model’s assumption that the time needed for a value to travel from a processor to an arbitrary register is a constant. They show how the complexity of PRAM algorithms changes when we assume that processors occupy physical space and signal transmission speeds are finite.

In this chapter we have given an algorithm for performing a preorder tree traversal. He and Yesha (1988) present a parallel algorithm for constructing depth-first spanning trees in planar graphs. The model of computation is CRCW PRAM, the number of processors required is $O ( n )$ ,and the time complexity is $O ( l o g ^ { 2 } n )$

Guan and Langston (1991) have published a time-space optimal parallelmerge algorithm for the EREW PRAM model.

Atallah et al. (1989) describe how a divide-and-conquer method can be used to design parallel algorithms for the CREW PRAM.

Nick's Class $\mathcal { N C }$ was named for Nick Pippenger by Cook (1983) A summary of parallel complexity classes appears in Cook.

2-1 Summarize the similarities and diffrences between the RAM model of serial computation and the PRAM model of parallel computation.   
2-2 Given a COMMON (CRCW) PRAM algorithm with time complexity O(t (n)), what is an upper bound on the time complexity of an algorithm to solve the same problem on the CREW model? Given a CREW algorithm with time complexity O(t(n), what is an upper bound on the time complexity of an algorithm to solve the same problem on the EREW model?   
2-3 Given a PRAM model with a single active processor,prove that [log pl instructions are both necessary and sufficient for $p$ processors to become active.   
2-4 A variant of the original PRAM model often found in literature assumes that the computation begins with any number of processors active. In this model there is no need for a processor to activate another processor. Show that the complexities of all PRAM algorithms described in Sec. 2.3 are unchanged, given this new model.   
2-5 Devise a PRAM algorithm to multiply two n × n matrices, where n =2\*.   
2-6 Modify the parallel-merge algorithm given in this book to accommodate each list having $n / 2$ disjoint values, but the merged list having two identical values. Analyze the complexity of your algorithm.   
2-7 Modify the parallel-merge algorithm given in this book to accommodate one list having $n$ values and the other list having $m$ values. Assume all $n + m$ valuesare distinct. Analyze the complexity of your algorithm.   
${ \bf 2 { - } } { \bf 8 } ^ { * }$ Devise an $O ( \log ^ { 2 } n )$ PRAM algorithm to sort a list of $n$ distinct elements. Hint: Use the parallel merge algorithm.   
2-9 Analyze the complexity and determine the number of processors required for the preorder tree-traversal algorithm in Sec. 2.3.   
2-10 Devise a PRAM algorithm to perform a postorder traversal of a rooted tree. Assume the same data structure as used by the algorithm in Fig. 2-15.   
$^ { 2 \cdot 1 1 ^ { * } }$ Devise a PRAM algorithm to perform a preorder traversal of a rooted tree, where the algorithm's input is a set of directed edges. Every vertex $v$ other than the root has a corresponding edge $( v , w )$ ,where $w$ is the parent of $v$ .The root vertex $r$ is distinguished by its corresponding edge $( r , r )$ .Hence a graph with $n$ vertices is represented by $n$ vertex pairs.   
${ \bf 2 } { \bf - 1 } { \bf 2 } ^ { * }$ Devise a PRAM algorithm to solve the graph coloring problem that has lower time complexity than the algorithm presented in the book. You may use a more powerful PRAM model.   
$^ { 2 - 1 3 ^ { * } }$ Devise a PRAM algorithm to solve the vertex cover problem. (Given a graph with $n$ vertices and a positive integer $k$ ,determine whether there is a set of $k$ vertices such that every edge in the graph is incident upon at least one of the vertices.) Assume the inputs to your algorithm are $n , k .$ and an $n \times n$ adjacency matrix $A$ representing an undirected graph.   
$2 { \cdot } 1 4 ^ { * }$ Devise a PRAM algorithm to solve the clique problem. (Given a graph with $n$ vertices and a positive integer $k$ ,determine if there isa set of $k$ vertices such that every pair of vertices in the set isconnected by an edge.)Assume the inputs

to your algorithm are $n , k$ and an $n \times n$ adjacency matrix A representing an undirected graph.

2-15 In Sec. 2.4 we learned that in order for a paralel algorithm to be cost optimal, the total number of operations it performs cannot be of a higher complexity class than an optimal sequential algorithm. In that case, why don't we simply choose any optimal sequential algorithm as the starting point for our parallel algorithm design?

2-16 For each problem listed below, design a cost-optimal polylogarithmic time PRAM algorithm and use Brent’s theorem to determine the number of processors that minimizes parallel execution time.

a List ranking b Preorder tree traversal $\mathbf { c } ^ { * }$ List merging

2-17 Why is it unrealistic to expect to solve an $\mathcal { N P }$ -complete problem on the PRAM in polylogarithmic time, using a polynomial number of processors?

2-18 Prove Theorem 2.4.

2-19 How could we formulate a polylogarithmic depth-first search algorithm in Sec. 2.3, when Sec. 2.5 says depth-first search is $\mathcal { P }$ -complete?

# 3

# PROCESSOR ARRAYS, MULTIPROCESSORS, AND MULTICOMPUTERS

The goal of this chapter is to introduce three important models of parallel computation and several associated parallel computer designs. The models are processor arrays,multiprocessors,and multicomputers,all of which have fostered actual parallel computers.

We present a number of processor organizations in Sec.3.1; these are mesh, binary tree,hypertree,pyramid,butterfly,hypercube,cube-connected cycles, shuffle-exchange,and de Bruijn. These processor organizations are evaluated according to criteria that help determine their practicality and versatility. Section 3.2 surveys a number of processor array models including the Connection Machine $\mathrm { C M } { - } 2 0 0 ^ { \mathrm { T M } }$ ,a well-known processor array. Section 3.3 discusses multiprocessors,multiple-CPU computers with global address space. We describe two commercial multiprocessors--the Sequent SymmetryTM and the BBN Butterfly $\mathrm { T C } 2 0 0 0 ^ { \mathrm { T M } }$ . In Sec. 3.4 we examine multicomputers,multiple-CPU computers with no global address space.Our example architectures are the nCUBE $2 ^ { \mathrm { T M } }$ ,Thinking Machines' $\mathrm { C M } { - } 5 ^ { \mathrm { T M } }$ ,and the Intel Paragon $\bf { X P / S ^ { \mathrm { { T M } } } }$ .Section 3.5 presents Flynn's taxonomy, the most common classification of sequential and parallel computer architectures. In Sec. 3.6 we discuss the terms used to describe the performance of parallel algorithms. These terms include speedup, scaled speedup, and parallelizability.

# 3.1 PROCESSOR ORGANIZATIONS

This section defines nine important processor organizations--methods of connecting processors in a parallel computer. A processor organization can be represented by a graph in which the nodes (vertices) represent processors and the edges represent communication paths between pairs of processors. (For readers unfamiliar with graph theory, a brief introduction to graph theoretic terms is given in Appendix A.) We evaluate these processor organizations according to criteria that helpus understand their effectiveness in implementing efficient parallel algorithms on real hardware. These criteria are:

1 Diameter. The diameter of a network is the largest distance between two nodes.Low diameter is better, because the diameter puts a lower bound on the complexity of parallel algorithms requiring communication between arbitrary pairs of nodes.

2 Bisection width of the network. The bisection width of a network is the minimum number of edges that must be removed in order to divide the network into two halves (within one). High bisection width is better, because in algorithms requiring large amounts of data movement, the size of the data set divided by the bisection width puts a lower bound on the complexity of the parallel algorithm.

3 Number of edges per node. It is best if the number of edges per node is a constant independent of the network size, because then the processor organization scales more easily to systems with large numbers of nodes.

4 Maximum edge length. For scalability reasons it is best if the nodes and edges of the network can be laid out in three-dimensional space so that the maximum edge length is a constant independent of the network size.

We now discuss the various type of processor organizations.

# 3.1.1 Mesh Networks

In a mesh network, the nodes are arranged into a $q$ -dimensional lattice. Communication is allowed only between neighboring nodes; hence interior nodes communicate with $2 q$ other processors. Figure 3-1a illustrates a twodimensional (2-D) mesh. Some variants of the mesh model allow wrap-around connections between processors on the edge of the mesh. These connections can connect processors in the same row or column (Fig. 3-1b) or adjacent rows or columns (Fig. 3-1c).

Let's evaluate the mesh network according to our four criteria. We assume thatthe mesh has no wrap-around connections. The diameter ofa $q$ -dimensional mesh with k9 nodes isq(k -1). Hence,from a theoretical point of view, mesh networks have the disadvantage that data routing requirements often prevent the development of polylogarithmic time parallel algorithms. In practice, however, some computer architects would rather implement fewer, faster links than more, slower links.

![](images/df16938696eda2fcfc1cbcae013708f73f63011da9e00b003ee9f356cbf98c04.jpg)  
FIGURE 3-1 Two-dimensional meshes. (a) Mesh with no wrap-around connections. (b) Mesh with wrap-around connections between processors in same row or column. (c) Mesh with wrap-around connections between processors in adjacent rows or columns.

The bisection width of a $q$ -dimensional mesh with $k ^ { q }$ nodes is $k ^ { q - 1 }$ .Themaximum number of edges per node is $2 q$ . The maximum edge length is a constant, independent of the number of nodes, for two- and three-dimensional meshes.

The two-dimensional mesh has been a popular topology for processor arrays, including Goodyear Aerospace's $\mathbf { M P P ^ { T M } }$ , the AMT DAPTM, and MasPar's MP-$1 ^ { \mathrm { T M } }$ . The Intel Paragon XP/S multicomputer connects processors with a twodimensional mesh.

# 3.1.2 Binary Tree Networks

In a binary tree network the $2 ^ { k } - 1$ nodes are arranged into a complete binary tree of depth $k - 1$ (Fig. 3-2). A node has at most three links. Every interior node can communicate with its two children and every node other than the root can communicate with its parent. The binary tree has low diameter, $2 ( k - 1 )$ ， but has a poor bisection width of one. Assuming nodes have volume,it is impossible'to arrange the nodes of a binary tree in three-dimensional space such that as the number of nodes increases,the length of the longest edge is always less than a specified constant.

![](images/bab8d52afb09c86122b96114d737a8e527a9fd437ddd3fa503e5362e50d062b0.jpg)  
FIGURE 3-2 Biriary tree network of size 15 and depth 3.

# 3.1.3 Hypertree Networks

A hypertree represents one approach to building a network with the low diameter of a binary tree but an improved bisection width.The easiest way to think of a hypertree network of degree $k$ and depth $d$ is to consider the network from two different angles (Fig. 3-3). From the front a hypertree network of degree $k$ and depth $d$ looks like a complete $k$ -ary tree of height $d$ (Fig. 3- 3a).From the side, the same hypertree network looks like an upside down binary tree of height $d$ (Fig. 3-3b). Joining the front and side views yields the complete network. Figure 3-3c illustrates a hypertree network of degree 4 and height 2.

A 4-ary hypertree with depth $^ d$ has $4 ^ { d }$ leaves and $2 ^ { d } ( 2 ^ { d + 1 } - 1 )$ nodes in all. The diameter of this network is $2 d$ and its bisection width is $2 ^ { d + 1 }$ . The number of edges per node is never more than six and the maximum edge length is an increasing function of the problem size.

![](images/15a4347fea5351be688e593495ff92c83fcdf67a4b663be1ba4410f3af2283de.jpg)  
FIGURE 3-3 Hypertree network of degree 4 and depth 2. (a) Front view.(b) Side view. (c) Complete network.

The data routing network of the Connection Machine CM-5 multicomputer is a 4-ary hypertree.

# 3.1.4 Pyramid Networks

The pyramid network can be seen as an attempt to combine the advantages of mesh networks with those of tree networks. A pyramid network of size $k ^ { 2 }$ is a complete 4-ary rooted tree of height $\log _ { 2 } k$ augmented with additional interprocessor links so that the processors in every tree level form a 2-D mesh network (Miller and Stout 1987). A pyramid of size k² has at its base a 2-D mesh network containing k² processors. The total number of processors in a pyramid of size k² is (4/3)k2-(1/3). The levels of the pyramid are numbered in ascending order such that the base has level number O,and the single processor at the apex of the pyramid has level number log2 k. Every interior processor is connected to nine other processors: one parent, four mesh neighbors, and four children. Figure 3-4 illustrates a pyramid network of size 16.

The advantage of the pyramid over the 2-D mesh is that the pyramid reduces the diameter of the network.For example, when a message must travel from one side of the mesh to the other, fewer link traversals are required if the message travels up and down the tree rather than across the mesh. The diameter of a pyramid of size $k ^ { 2 }$ is $2 \log k$

The addition of tree links does not give the pyramid a significantly higher bisection width than a 2-D mesh. The bisection width of a pyramid of size $k ^ { 2 }$ is $2 k$ ，

The maximum number of links per node is no greater than nine, regardless of the size of the network. Unlike a 2-D mesh, however, the length of the longest edge in the pyramid network is an increasing function of the network size.

![](images/f39a118787e74be575f8fa8e0b0c3aa9b6ae72c47965b9f196b533981605a720.jpg)

A butterfly network consists of $( k + 1 ) 2 ^ { k }$ nodes divided into $k + 1$ rows, or ranks, each containing $n = 2 ^ { k }$ nodes (Fig. 3-5). The ranks are labeled O through $k$ ,although the ranks O and $k$ are sometimes combined, giving each node four connections to other nodes.

Let node $( i , j )$ refer to the $j$ th node on the ith rank, where $0 \leq i \leq k$ and $0 \leq j < n$ .Thennode $( i , j )$ on rank $\textit { i } > 0$ is connected to two nodes on rank $i - 1$ ， $\mathtt { n o d e } ( i - 1 , j )$ and $\mathtt { n o d e } ( i - 1 , m )$ ，where $m$ is the integer found by inverting the $i$ th most significant bit in the binary representation of $j$ .Note that if $\mathrm { n o d e } ( i , j )$ is connected to $\mathtt { n o d e } ( i - 1 , m )$ ,then $\mathtt { n o d e } ( i , m )$ is connected to node $( i - 1 , j )$ . The entire network is made up of such “butterfly” patterns, hence the name. As the rank numbers decrease,the widths of the wings of the butterflies increase exponentially.For this reason the length of the longest network edge increases as the number of network nodes increases.

The diameter of a butterfly network with $( k + 1 ) 2 ^ { k }$ nodes is $2 k$ and the bisection width of a network of that size is $2 ^ { k - 1 }$ ·

A butterfly network serves to route data from nonlocal memory to processors on the BBN TC20oO multiprocessor described later in this chapter.

# 3.1.6 Hypercube (Cube-Connected) Networks

A cube-connected network, also called a binary $n$ -cube network, is a butterfly with its columns collapsed into single nodes. Formally, this network consists of $2 ^ { k }$ nodes forming a $k$ -dimensional hypercube. The nodes are labeled $0 , 1 , \ldots , 2 ^ { k } - 1$ ; two nodes are adjacent if their labels differ in exactly one bit position. A four-dimensional hypercube is shown in Fig. 3-6.

The diameter of a hypercube with $2 ^ { k }$ nodes is $k$ ，and the bisection width of that size network is $2 ^ { k - 1 }$ , the hypercube organization has low diameter and high bisection width at the expense of the number of edges per node and the length of the longest edge.The number of edges per node is $k$ -thelogarithm of the number of nodes in the network. The length of the longest edge in a hypercube network increases as the number of nodes in the network increases.

![](images/6d4e290bec8629a5389072013b0b6723403febdcd55d7fa4ee8d7d0e0d0fe1c2.jpg)  
FIGURE 3-5 Butterfly network with 32 nodes. (UIlman [1984].)

![](images/ecd664e08fa435deecfcb78fd67c7a8b48c6589dc0f1468b1c4c4938110a4288.jpg)  
FIGURE 3-6 A four-dimensional (16 node) hypercube.

The hypercube was the most popular processor organization for first- and second-generation multicomputers, and nCUBE continues to build systems based on this topology. In addition, processing element clusters on the Connection Machine CM-2o0 processor array are connected in a hypercube.

# 3.1.7 Cube-Connected Cycles Networks

The cube-connected cycles network is a $k$ -dimensional hypercube whose $2 ^ { k }$ "vertices” are actually cycles of $k$ nodes formed by the columns of a butterfly network whose ranks O and $k$ have been combined. For each dimension, every cycle has a node connected to a node in the neighboring cycle in that dimension. See Fig. 3-7 for a drawing of a 24-node cube-connected cycles network.

Formally, node $( i , j )$ is connected to node $( i , m )$ if and only if $m$ is the result of inverting the ith most significant bit of the binary representation of $j$ .Note that the connections are slightly different from those in the butterfly network, that is, if $\mathrm { n o d e } ( i , j )$ is connected to $\mathtt { n o d e } ( i - 1 , m )$ in the butterfly network, where $j \neq m$ ,thennode $( i , j )$ is connected to $\mathrm { n o d e } ( i , m )$ in the cube-connected cycles network. However,in the cube-connected cycles network, $\mathrm { n o d e } ( i , j )$ can still communicate with node $( i - 1 , m )$ by following two links, since there is a direct path from $\mathrm { n o d e } ( i , m )$ to node $( i - 1 , m )$

Compared to the hypercube, the cube-connected cycles processor organization has the advantage that the number of edges per node is three-a constant independent of network size. However, the cube-connected cycles network has the disadvantage that the network diameter is twice that of a hypercube and the bisection width is lower. Given a cube-connected cycles network of size $k 2 ^ { k }$ , its diameter is $2 k$ and its bisection width is $2 ^ { k - 1 }$

![](images/db41ba49d2a78a9dc7cdd96812105281e33d26d080a7f9ae4279fc871a20cbb1.jpg)  
FIGURE 3-7 Cube-connected cycles network with 24 nodes.The first subscript of each node denotes therank;the second subscript of each node denotes the column.

# 3.1.8 Shuffle-Exchange Networks

A shuffle-exchange network consists of $n = 2 ^ { k }$ nodes, numbered $0 , 1 , \ldots$ $n - 1$ ,and two kinds of connections,called shufe and exchange.Exchange connections link pairs of nodes whose numbers differ in their least significant bit. The perfect shuffle connection links node $_ i$ with node $2 i$ modulo $( n - 1 )$ ， with the exception that node $n - 1$ is connected to itself. See Fig. 3-8 for a drawing of an eight-node shuffle-exchange network. Shuffle connections are indicated by the solid arrows and the exchange links are represented by the dashed arrows.

To understand the derivation of the name perfect shuffle, consider shuffling a deck of eight cards, numbered 0, 1, 2, 3, 4, 5, 6, 7. If the deck is divided into two exact halves and shuffled perfectly, then the result is the following order: 0,4,1, 5, 2, 6, 3, 7. Reexamine Fig. 3-8 and notice that the final position of the card that began at index $i$ can be determined by following the shuffle link from node $i$

Let $a _ { k - 1 } a _ { k - 2 } \dots a _ { 1 } a _ { 0 }$ be the address of a node in a perfect shufle network, expressed in binary. A datum at this address willbe at address $a _ { k - 2 } \cdot \cdot \cdot a _ { 1 } a _ { 0 } a _ { k - 1 }$ following a shuffle operation. In other words, the change in the address of a piece of data after a shufle operation corresponds to a left cyclic rotation of the address by 1 bit (Prob. 3.4). If $n = 2 ^ { k }$ ,then $k$ shuffling operations move a datum back to its original location. The nodes through which a data item beginning at address $i$ travels in response to a sequence of shuffles are called the necklace of i. No necklace is longer than $k$ and a necklace shorter than $k$ is called a short necklace. Figure 3-9 illustrates the necklaces of the perfect shuffle network with eight nodes.

![](images/f9eae2b1256a23cf48df0d6a92832f6e5f620d6aad5562204a7035d1a3b9d53c.jpg)  
FIGURE 3-8 Shuffle-exchange network with eight nodes. Solid arrows denote shuffle connections. Dashed arrows denote exchange connections.

![](images/1176d2e85fc54803043c44adc29c326d75bd6e3b02d01087ad308029616b3d68.jpg)  
FIGURE 3-9 Necklaces of the shuffle-exchange network with eight nodes.

Every node in a shufle-exchange network has two outgoing and two incoming links.The length of the longest link increases as a function of network size. The number of long links has advantages with respect to network diameter and bisection width since the diameter of a shuffle exchange network is logarithmic in the number of nodes, that is, a network with $2 ^ { k }$ nodes has diameter $2 k - 1$ 。 The bisection width is at least $2 ^ { k - 1 } / k$

Siegel (1979) has shown that a composition of $k$ shuffle-exchange networks, called an omega network,is equivalent to a hypercube network with degree $k$ . The same effect can be achieved by building only one stage of the network and cycling through it $k$ times (Lawrie 1975).

# 3.1.9 de Bruijn Networks

A de Bruijn network consists of $n = 2 ^ { k }$ nodes. Let $a _ { k - 1 } a _ { k - 2 } \dots a _ { 1 } a _ { 0 }$ be the address of a node in the de Bruijn network. The two nodes reachable via directed edges from that node are

$$
\begin{array} { c } { { a _ { k - 2 } a _ { k - 3 } \cdot \cdot \cdot a _ { 1 } a _ { 0 } 0 } } \\ { { a _ { k - 2 } a _ { k - 3 } \cdot \cdot \cdot a _ { 1 } a _ { 0 } 1 } } \end{array}
$$

FIGURE 3-10 An 8-processor de Bruijn network.

![](images/fda0fea746f0a546e265ac0f27714b0159427549f791db107dfcdffec6b1af53.jpg)  
Figure 3-10 illustrates an eight-processor de Bruijn network.

<table><tr><td colspan="3"></td><td>Bisection</td><td>Constant Number</td><td>Constant Edge</td></tr><tr><td>Network</td><td>Nodes</td><td>Diameter</td><td>Width</td><td>of Edges</td><td>Length</td></tr><tr><td>1-D mesh</td><td>k</td><td>k-1</td><td>1</td><td>Yes</td><td>Yes</td></tr><tr><td> 2-D mesh</td><td>k2</td><td>2（k-1)</td><td>k k2</td><td>Yes</td><td>Yes</td></tr><tr><td>3-D mesh</td><td>K3</td><td>3(k-1)</td><td>1</td><td>Yes Yes</td><td>Yes</td></tr><tr><td>Binary tree</td><td>2k-1 2k(2k+1-1)</td><td>2（k-1) 2k</td><td>2k+1</td><td>Yes</td><td>No No</td></tr><tr><td>4-ary hypertree</td><td>(4k²-1)/3</td><td>2logk</td><td>2k</td><td>Yes</td><td>No</td></tr><tr><td>Pyramid Butterfly</td><td>(k+1）2k</td><td>2k</td><td>2k</td><td>Yes</td><td>No</td></tr><tr><td>Hypercube</td><td>2k</td><td>k</td><td>2k-1</td><td>No</td><td>No</td></tr><tr><td>Cube-connected cycles</td><td>k2k</td><td>2k</td><td>2k-1</td><td>Yes</td><td>No</td></tr><tr><td>Shuffle-exchange</td><td>2k</td><td>2k-1</td><td>≥2k-1/k</td><td>Yes</td><td>No</td></tr><tr><td>de Bruijn</td><td>2k</td><td>k</td><td>2k/k</td><td>Yes</td><td>No</td></tr></table>

The number of edges per node is a constant independent of the network size. The bisection width of a network with $2 ^ { k }$ nodes is $2 ^ { k } / k$ ,and the length of the longest edge increases with the size of the network. As with shuffle-exchange networks, de Bruijn networks contain shuffle connections.

The diameter of a de Bruijn network with $2 ^ { k }$ nodes is $k$ ，whichisabout half the diameter of a shuffle-exchange network with the same number of nodes.

The processors of the Triton $1 ^ { 1 \mathrm { { m } } }$ , a SIMD/MIMD parallel computer developed at the University of Karlsruhe,are connected with a de Bruijn network (Herter et al. 1992).

# 3.1.10 Processor Orginization Summary

Table 3.1 summarizes the characteristics of the processor organizations we have considered. Of the nine organizations, only the mesh has constant edge length. The hypercube is noteworthy as the only processor organization we have considered in which the number of edges per node is an increasing function of the network size.

# 3.2 PROCESSOR ARRAYS

A vector computer is a computer whose instruction set includes operations on vectors as well as scalars.Generally,there are two ways of implementing a vector computer. A pipelined vector processor streams vectors from memory to the CPU, where pipelined arithmetic units manipulate them. The Cray $1 ^ { \mathrm { T M } }$ and Cyber- ${ 2 0 5 ^ { \mathrm { { T M } } } }$ are well known pipelined vector processors. We do not consider these architectures further.

A processor array is a vector computer implemented as a sequential computer connected toa set of identical,synchronized processing elements capble of simultaneously performing the same operation on different data. The sequential computer is usually called the front end.

The front end is a general-purpose CPU that stores the program and the data that are not manipulated in parallel and also executes the sequential portions of the program.

Each processing element has a small local memory that it can access directly.Collectively, the individual local memories of the processing elements store the vector data that are manipulated in parallel. When the front end computer encounters an instruction whose operand is a vector, it issues a command to the processing elements to perform the instruction in parallel. Although the processing elements execute in parallel, units may be programmed to ignore any particular instruction. This ability to mask processing elements allows synchronization to be maintained through the various paths of control structures, such as clauses of an if...then...else statement.

In the course of a normal computation, data flows from the front end to the processor array，between processing elements,and from the processor array to the front end. Processing elements communicate values to each other via an interconnection network (Fig. 3-11), which is usually based on one of the processor organizations we described in the previous section. Over the years, the 2-D mesh has been easily the most popular processor organization for processor arrays. Processor arrays organized as hypercubes, shuffle-exchange networks, and cube-connected cycles networks have also been suggested. In later chapters we describe paralel algorithms based upon most of these models.

![](images/d93a6591281334c6df13a67ac4169761f296d28571ba55444b1a2d55361d8c19.jpg)  
FIGURE 3-11 Arealistic processor array model. Each processor has its own private memoryand processors canpass data only viaa limited interconnectionnetwork.

Processor arrays have an efficient mechanism for the front end to broadcast instructions and data items to the individual processing elements. In addition, processor arrays also support the efficient access of a particular memory location in the memory of an arbitrary processing element by the front end. The existence of fast operations for broadcast and arbitrary memory fetch plays an important role in many parallel algorithms.

# 3.2.1 Connection Machine CM-200

The Connection Machine CM-200 processor array is manufactured by Thinking Machines Corporation of Cambridge, Massachusets. The primary source of information for our description of the CM-2oo is Thinking Machines,1989.

The CM-2Oo has three principal components: a front end computer,a parallel processing unit,and an I/O system (Fig. 3-12). The front-end computer, usually a Sun workstation,stores serial data and executes the sequential portions of programs. Parallel data are stored in the parallel processing unit.“The frontend computer broadcasts parallel instructions to the parallel processing unit for execution. A high speed I/O system allows efficient data transfers between the parallel processing unit and I/O devices, such as frame buffers and parallel disk drives.

![](images/049df8c46fbcf5db3458332322b18052335d0e57772cbf60b51a02c142336dcc.jpg)  
FIGURE3-12Block diagramof theConnectionMachineCM-20processorarray.(Reprintedby permission of Thinking Machines Corporation.)

The front end can exchange data with the processing elements in three ways. It can broadcast a single value to all of the processing elements. Through global combining, it can obtain the sum, maximum, global OR,etc., of one value from each processing element. By using the scalar memory bus, the front end processor can read or write 32-bit values stored in any processing element.

The parallel processing unit contains between 2,048 and 65,536 processing elements, an instruction sequencer, interprocessor communication networks, and I/O controllers and/or framebuffer modules.

The front end issues parallel processing instructions to the sequencer, which interprets each instruction and generates a series of "nanoinstructions." It broadcasts these nanoinstructions over an instruction bus to the processing elements, which execute them.

Paris,the PARallel Instruction Set of the Connection Machine, simplifes the development of compilers by providing a variety of operations similar to a more typical machine's instruction set. Some Paris instructions perform arithmetic operations on various data types,others facilitate communication between the processing elements, and still others facilitate communication between the processing elements and the front end computer.

By supporting virtual processors, Paris also serves the important function of insulating the user from the underlying processor array. A program can assume the existence of any number of processing elements, and these virtual processors are then mapped to the physical processing elements. This feature allows the same program to run on Connection Machine systems with different numbers of physical processors.

In general, whenever a Paris arithmetic operation is performed, each physical processing element may execute the operation many times,once for each virtual processor mapped to it.Virtual processor versions of the three hardwaresupported routing mechanisms also exist in the Paris instruction set.

The individual processing elements of the Connection Machine are bit-serial processors.Each processing element has a context flag,indicating whether or not it is screened. Screened processing elements do not store the results of their computations. Every processing element also has three input bits (two from memory and one from a flag) and two result bits (one to memory and one to a flag).

A processing element can compute any two boolean functions on thre inputs. These functions are specified as two 8-bit bytes representing the truth tables for the two functions. In other words, the processing element “computes”the result of the boolean function by consulting the truth table entry indexed by the three input bits.

For example,the truth table in Fig. 3-13 is used to perform bit-serial addition. In this case the two functions on three inputs are “carry-out” and “sum." To add two $k$ -bit integers stored in its local memory,a processing element first loads the virtual processor context flag into a hardware flag register. All ALU operations are conditional upon the state of this flag. Second, the processor clearsa second flag that serves as the carry bit.Third, the processor iterates $k$ times through a cycle in which it reads the carry bit and one bit of each operand and computes the sum bit and carry-out bit. The computation begins with the least significant bits of the operands and ends with their most significant bits.

<table><tr><td colspan="2">INPUT BITS</td><td colspan="2">OUTPUT BITS</td></tr><tr><td>Memory</td><td>Memory Flag</td><td>Memory</td><td>Flag</td></tr><tr><td>0</td><td>0 1</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0 0</td><td>1</td><td></td></tr><tr><td>0</td><td>1</td><td>1</td><td>0</td></tr><tr><td>0 1</td><td>1 1 0 0</td><td>0</td><td>1</td></tr><tr><td>1</td><td>0</td><td>1</td><td>0</td></tr><tr><td>1</td><td>1</td><td>1 0</td><td>0</td></tr><tr><td></td><td>1</td><td>1</td><td>0 1</td></tr><tr><td>1</td><td></td><td>1</td><td>1</td></tr></table>

A single VLSI chip contains 16 processing elements plus routing hardware. Each pair of processor chips shares a group of memory chips,a floating-point interface chip, and a floating-point execution chip (Fig. 3-14).

The memory chips provide a 44-bit wide data path, which translates into 32 data bits and 12 bits of error-correcting code. The 32 data bits can be sent to the 32 bit-serial processing elements,one bit per processing element. Alternatively, the 32 data bits can be directed to the floating-point interface chip. The floating-point interface chip may use this data for memory address control for indirect addressing,or it may send the data to the floating-point execution chip.

The floating-point execution chip produces results in 32-bit quantities. The interface unit stores these results back into memory. The maximum performance of this unit in performing 32-bit floating-point arithmetic is 20 megaflops. A maximally configured Connection Machine has 2O48 floating-point chips and a peak performance of about 40 gigaflops.

The Connection Machine has three routing mechanisms. The most general routing mechanism, simply called the router, allows any processing element to communicate with any other processing element. Every processor chip contains one router node servicing all 16 processing elements on the chip. The router nodes are wired together to form a hypercube. In a fully configured Connection Machine having 65,536 processing elements on 4,096 $( 2 ^ { 1 2 } )$ processor chips, the network is a 12-dimensional hypercube. Each message travels through the router nodes until it reaches the chip containing the destination processor. The router nodes automatically forward messages and perform some dynamic load balancing. For example, the path a message takes may vary, depending upon which paths are available.

![](images/a390cfb3df0db2409024bdfb159cc1fd218f1525eb581d0ee119c424891be139.jpg)  
FIGURE 3-14 Architecture of processor chip pair on the Connection Machine CM-200.(Reprinted by permission of Thinking Machines Corporation.)

Each router node has an ALU capable of performing some arithmetic operations. The router checks to see if any messages share the same destination. If so,it combines the messages based upon the semantics of the parallel instruction being executed. For example, it may take the sum, maximum, or logical OR of the values, or it may simply discard all but one of the values.

The second routing mechanism is called the NEWS grid. A $j$ -dimensional mesh can be embedded in a $k$ -dimensional hypercube,if $j \le k$ Hence,a subset of the wiresthat supports the routercan forma Cartesian mesh,whichThinking Machines calls a NEWS grid. If all communications between processing elements are neighbors in a NEWS grid of any dimension less than or equal to the dimension of the hypercube,then the message-passing speed is much higher than if the messages must be passed through the router. The system passes such messages using three special transfer methods,two of which are implemented in hardware.

To demonstrate the three transfer methods, suppose the system's 4096 processor chips are organized as a $6 4 \times 6 4$ grid. Assume each processor chip's

16 processing elements are organized as a $4 \times 4$ grid, and finally,assume each processing element has 64 virtual processors organized as a $8 \times 8$ grid.

Suppose each virtual processor must send a value to the virtual processor to the north. Within each group of 64 virtual processors,56 of them are sending data to another virtual processor within the same processing element. The processing element “passes” the data values by copying the data within its own memory.Hence,the first specialized transfer method avoids interprocessor communication by rearranging data within local memory.

Each processing element must still send 8 data values to the processing element to the north. However,within each processor chip,12 of the 16 processing elements are sending values to other processing elements in the same chip. The second specialized transfer method uses special permuation circuitry on the chip to perform these 12 data transfers.

Each processor chip must still send 32 data values (8 values times 4 processing elements) to its neighbor to the north along one hypercube wire and then receive 32 data values from its neighbor to the south along another hypercube wire. This third specialized transfer method used in NEWS grids takes advantage of the regular communication pattern to determine actual wires to be used.

Scans and spreads are the third kind of message routing. A scan is a NEWS operation that performs a prefix sum. A spread is a form of broadcast that allows a single processing element to send a value to every other procesing element. Prefix sums or other scan operations may be incorporated into a spread.

A high-speed I/O capability increases the utility of a supercomputer. The Connection machine's DataVaultM is a parallel array of disk drives.A set of 8 DataVaults, connected to a 65,536-processor element Connection Machine, provides 48o gigabytes of secondary storage and data transfer rates above 100 megabytes per second. The Connection Machine also supports high speed output to a frame buffer driving a color monitor.

# 3.3 MULTIPROCESSORS

Multiple-CPU computers consist of a number of fully programmable processors,each capable of executing its own program. Multiprocessors are multiple-CPU computers with a shared memory. In a Uniform Memory Access (UMA, pronounced “you'ma") multiprocessor the shared memory is centralized. In a Non-Uniform Memory Access (NUMA,pronounced "new'ma") multiprocessor the shared memory is distributed.

# 3.3.1 Uniform Memory Access (UMA) Multiprocessors

The simplest processor intercommunication pattern assumes that all the processors work through a central switching mechanism to reach a centralized shared memory (Fig. 3-15). There are a variety of ways to implement this switching mechanism, including a common bus to global memory, a crossbar switch, andapacket-switched network.TheEncoreMultimaxTMand the Sequent Symmetry $\mathrm { S } 8 1 ^ { \mathrm { T M } }$ are examples of commercial uniform memory access (UMA) multiprocessors.

![](images/8bccc28ba4607ed7142bb0d16a52a9ffd032cf444ce80ea43df645550a401958.jpg)  
Theuniform memory access (UMA) multiprocessor model.All the processors work through a central switching mechanism to reach a shared global memoryand $1 / 0$ devices.

Systems using a bus, such as the Multimax or Symmetry,are limited in size, since only so many processors can share the bus before it becomes saturated. In the case of systems using a crossbar switch, the cost of the switch soon becomes the dominant factor,again limiting the number of processors which may be connected (Stone 1980).

UMA multiprocessors based on switching networks can conceivably contain a large number of processors,although no commercial computers using this architecture have yet appeared. The NYU Ultracomputer,an experimental UMA multiprocessor,is based on an omega switching network.Thecost of an omega network for a $p$ -processor system is $\Theta ( p \log p )$ --lower than the $\Theta ( p ^ { 2 } )$ cost of a crossbar switch.

Symmetry The Symmetry is a UMA multiprocessor manufactured by Sequent Computer Systems, Inc.of Beaverton, Oregon. The Symmetry is not a supercomputer-some contemporary workstations have higher floating-point performance. We have included this section because it is a commercial example of a UMA multiprocessor. Inaddition,it is likely tobethe onlypaallel computer that many readers can access.

The Symmetry uses a pipelined 64-bit bus to connect the system's CPUs, memory,andI/Odevices.The SequentSystem Bus (SSB) carries 32-or64-bit data items and addresses up to 32 bits in length. Read and write operations on the SSB are pipelined, meaning that after the SSB has transmitted a read or write request to system memory, it can handle another transaction even before the memory has responded to the first request. The sustained data transfer rate on the bus is 53.3 Mbytes per second.

The processors use a second one-bit wide bus to exchange interrupts and other low-level control and error signals.

A Symmetry processor is based on the Intel 80386 CPUTM,a 32-bit microprocessor, and an Intel 80387 floating-point coprocessor. An optional Weitek WTL 1167TM chip is available to enhance the speed of some floating-point operations. Since the Intel 80386 was not designed to be used as a multiprocessor

![](images/67e4198b3e349fe12556d3077b723ffe57372aa9de4bbbad9073d25357f05b7e.jpg)  
FIGURE3-16BlockdiagramoftheSequent Symmetrya UMAmultiprocessor. (Courtesy Hatcherand Quinn [1991].)

CPU, each processor has a System Link and Interrupt Controler to manage the interactions among processors. Additional hardware implements a cache memory.

The cache memories in the Symmetry multiprocessor play a vital role in keeping CPUs busy and reducing contention for the Sequent System Bus. The on-board cache memory responds quickly enough to allow the Intel 80386 CPU to operate at full speed. If the cache hit rate is high, then the burden each CPU puts on the system bus is light, allowing more processors to be active.

Each CPU has a 64-Kbyte cache. Whenever the CPU issues a read to an address in system memory that is not currently in the cache, the cache control suspends the CPU's execution and issues a 16-byte read request on the SSB to fetch the data from system memory. The least recently used 16-byte block in the selected row of the cache is swapped out to make room for the new block. At this point the cache controller resumes CPU execution and passes the requested data item to the CPU.

A central problem in the design of UMA multiprocessors is how to ensure cache consistency; that is, how to maintain consistency between copies of data in the main system memory and the local processor caches. To resolve this problem, a write-through caching policy was implemented in the older Sequent BalanceTM multiprocessor. Every data write is sent directly to system memory,and all copies of the data item in the other processors’ caches are invalidated.

The Symmetry uses a copy-back caching policy. When a processor modifies a data item in its own cache,it does not write the updated value to system memory until it swaps out the cache block or until another processor needs that data item. It does, however, signal the other processors that their copies of the data item are no longer up-to-date. The copy-back policy avoids the overhead of broadcasting all partial-block writes across the SSB into memory in those cases where no other processor accesses the modified data.

Single-byte load and store operations,as well as 16- and 32-byte loads and stores aligned on natural boundaries,always execute atomically. To ensure the atomic execution of any other operation, the operations must be protected with a locking routine that uses the Symmetry’s hardware locking mechanism. The locking mechanism locks 16-byte regions of processor cache memory (corresponding to the cache block size). The system supports the concurrent locking of disjoint regions.

# 3.3.2 Non-Uniform Memory Access (NUMA) Multiprocessors

Like UMA multiprocessors, non-uniform memory access (NUMA) multiprocessors are characterized by a shared address space. Unlike UMA multiprocessors,NUMA multiprocessor memory is distributed. Every processor has some nearby memory, and the shared address space on a NUMA multiprocessor is formed by combining these local memories.The time needed to access a particular memory location on a NUMA multiprocessor depends on whether that location is local to the processor.

TC2000 The TC2000, manufactured by BBN Systems and Technologies of Cambridge, Massachusetts, is a NUMA multiprocessor that has up to 128 processor nodes. Each processor node contains aMotorola 8810o CPU, three Motorola 882oo chips providing separate instruction and data caches, between 4 and 16 Mbytes of primary memory，and interfaces to the Butterfly switch anda VME bus (see Fig.3-17).The transaction bus connects these processor subsystems.

The maximum performance of a single processor is 20 megaflops.A fully figured 128-processor TC2000 would have a peak speed of about 2.5 gigaflops.

The hardware on each processor converts every 32-bit virtual address into a 34-bit physical address. The physical address may be in cache memory, the same processor's memory, or it may be in another processor's memory. Of course, cache memory accesses are the fastest. Private data and read-only shared data, such as program text, can be stored in cache memory. Data from the processor’s own physical memory can be fetched over the transaction bus. Data from another processor's memory is retrieved by sending a request through the Butterfly switching network (Fig.3-18).

![](images/697e589f69fc3cf574b6108c110121b805ae4f3462a9c2da1196fead3f9faa3c.jpg)  
FIGURE 3-17 A processor node of the BBNTC20o0. (Reprinted by permission of Bolt, Beranek，and Newman,Inc.)

Unlike UMA multiprocessors, such as the Sequent Symmetry, the TC2000 does not maintain cache consistency among all the processors’ data caches. That is why the operating system puts restrictions on what data can be cached.

Figure 3-19 illustrates the butterfly switch shown in Fig. 3-18 in more detail. Imagine that the cylinder of Fig. 3-18 has been split down the side,between the processors and the memories, then flattened and rotated 90 degrees. Each node of the switch is a VLSI switching element with eight inputs and eight outputs. Hence the number of switching elements in a $p$ -processor machine is plogg p.Data flow through the switch in packets;and the address bits route the data from the source to the destination.

![](images/2b21868c7aff89c984e1d5e1c603a86d4fa7fd0390e0c20cc80ba91b9f62f8ef.jpg)

![](images/63dbf627b83acb3b3444ac1131ea61f7c3cc71fafd8ffabd22d3a79485944898.jpg)  
FIGURE 3-18 Nonlocal memory references on the TC2000 are sent through the switch. (Reprinted by permission of Bolt, Beranek,andNewman,c.)   
FIGURE 3-19 Switching network for a 64-processor TC2000.

Since every processor has a VME interface, the I/O capability of the system grows at the same rate as the number of CPUs. The VME interface provides access to a wide variety of I/O devices,including A/D and D/A converters, secondary storage devices,and graphics processors.A 16-Mbyte window in each VME bus address space is mapped into the system's global address space, giving every processor in the system the potential to access to every I/O device.

Another computer, called the Test and Control System (TCS) master processor, provides several vital functions. The TCS master processor provides a user interface to the TCs. It also loads bootstrap programs into the processors' memories at system boot time,coordinates the activities of the slave processors, and receives messages sent by the slave processors. The TCS master processor is connected via a diagnostic bus toslave processors,which are located in the processor cards and in every pair of switch modules,and which continuously monitor the system for faults.

# 3.4 MULTICOMPUTERS

Another multiple-CPU architecture, the multicomputer, has no shared memory.Each processor has its own private memory and process interaction occurs through message passing. Commercial multicomputers include Intel’s Paragon

XP/S,Meiko’s Computing SurfaceTM， nCUBE's nCUBE 2, Parsytec's SuperClusterTM, and Thinking Machines' CM-5.

An important distinction between early multicomputers and contemporary systems is the change in how processors communicate. First generation multicomputers, such as the Intel $\mathrm { i P S C ^ { \mathrm { T M } } }$ ,the $\mathrm { n C U B E } / 1 0 ^ { \mathrm { T M } }$ ，and systems based on the T8Oo TransputerTM,are characterized by software managed store-andforward message passing (Fig. 3-2O). In order to send a messge from one processor to a nonadjacent processor, every intermediate processor along the message's path must store the entire message and then forward the message to the next processor down the line. Even if the data transfers are accomplished through DMA channels, the CPU is interrupted every time a DMA transfer is initiated.

In contrast, second generation multicomputers, such as the Intel $\mathrm { i P S C } / 2 ^ { \mathrm { T M } }$ ， Inteli $\mathrm { P S C } / 8 6 0 ^ { \mathrm { T M } }$ ,and nCUBE 2, have circuit-switched messge routing. For example, every iPSC/2 and iPSC/86O node has a routing logic daughter card called the Direct-Connect Module. The Direct-Connect Modules set upa circuit from the source node to the destination node. Once the circuit is set up, the message flows ina pipelined fashion from the source node to the destination nodenone of the intermediate nodes store the message. A message being passed from one node to a nonadjacent node does not interrupt the CPUs of the intermediate nodes and only the Direct-Connect Modules are involved (Fig. 3-21).

In a store-and-forward scheme,the time needed to send a message from one processor to another processor grows linearly with the number of “hops” the message must make to reach its destination. In contrast to a store-and-forward scheme, the time needed to send a message from one processor to another processor in a circuit-switched scheme is much less dependent on the distance between the processors.

Processor1 Processor1 Processor1 Processor1 RTY TY Y Processor 2 Processor2 Processor2 Processor2 E ER ERT ERTY Processor3 Processor3 Processor3 Processor3

![](images/b42ee7a3c56b970b838432937e8a6e2a3b5e6b8c42b8ad6ed5138d5305cbc9e2.jpg)  
FIGURE 3-20 Early multicomputers used store-and-forward routing.Every intermediateprocessoralong the message's path must store the entire message before forwarding the message to the next processor.

![](images/5c58be45f1692cc3e8dc1e3998137469cde880dcaef3da2b6dc8a15f8fe31bc5.jpg)  
FIGURE 3-21 The Direct-Connect Modules on the Intel iPSC/2 multicomputer support circuit-switched message routing whichallowsa connection to be established between the sendingand receivingprocessorsandkeeps the CPUsof intermediate nodes from being interrupted whena message passes through. (Courtesy Hatcher and Quinn [1991].)

The nCUBE 2 is manufactured by nCUBE Corporation of Foster City,California.The nCUBE 2 has three principal components: a front-end computer,a back-end array of processors,and parallel I/O devices (Fig. 3-22). Superficially, the nCUBE 2 resembles a processor array (compare Fig.3-22 with Fig. 3.11). However,the two architectures have a fundamental difference. The front-end computer of a processor array controls the activities of the processing elements, which synchronously perform simple computations. In contrast, the back-end (or node) processors of the nCUBE are full-fledged CPUs,and these CPUs execute their own instruction streams in parallel.

The nCUBE 2 contains up to 8,192 node processors. Each node processor has a peak performance of 2.5 megaflops. Hence the theoretical peak performance of a maximally-configured nCUBE 2 is about 20 gigaflops. Every node processor has between 1 and 64 megabytes of primary memory.

![](images/254dc7788275e0bfdb04d094632c2b367f627d3a816e92ec26e8fabb8a5fdbbf.jpg)  
FIGURE3-22Block diagram an nCUBE 2 multicomputer witheightback-end processors and two parallel I/Odevices.

The back-end processors are organized into a hypercube. The nCUBE 2 is a second generation multicomputer in that hardware-routed, DMA communication channels form the edges of the hypercube. The peak data-transfer rate between processors is 2.2 Mbytes per second.

Each node has a DMA channel dedicated to the data transfers to and from I/O devices.These I/O channels have the same speed as the internode communication channels.

Many early multicomputers, including the nCUBE 2, have two problems related to the front-end processor. First, the power of the front-end processor does not scale with the number of back end processors. If the number of users scales with the number of processors, then at some point the front end will be unable to support the users. Second,the front-end processor is isolated from the back-end processors.

# 3.4.2 Connection Machine CM-5

The Connection Machine CM-5 is the first multiple-CPU computer manufactured by Thinking Machines Corporation of Cambridge,Massachusets. Thinking Machines argues that since the CM-5 supports fast synchronization hardwareas well asmultiple CPUs,theCM-5isasuitable architecture for executing both data-parallel and control-parallel programs.

Figure 3-23 is a block diagram of the CM-5. Processing nodes, labeled with a $P$ , execute user programs. Control processors, labeled $C P$ ,act as partition managers-front ends for clusters of processing nodes. I/O control processors control I/O devices.

The CM-5 architecture remedies some of the problems associated with frontend processors of some earlier multicomputers. First, the system may contain multiple front-end processors,the partition managers. econd, these processors are based upon the SPARC CPU, the same processor as the back-end processors. Third, the partition managers are part of the same data routing network as the back-end processors.

The CM-5 processor organization is a 4-ary hypertree (Fig. 3-3). The processors are at the leaves of the tree and the interior nodes route data between the leaves. The minimum network bandwidth is 5 Mbytes/second.

Each CM-5 processing node consists of a SPARC CPU, network interface hardware, up to 32 megabytes of primary memory,and four pipelined vector processing units, each capable of performing up to 32 million double-precision floating-point operations per second. A fully configured CM-5 would have 16.384 processing nodes, 512 Gbytes of primary memory,and a theoretical peak performance of about 2 teraflops. (We should point out that a CM-5 built using1991 technology would occupy about 10,o00 square feet of floor space and would cost several hundred million dollars.)

![](images/42e02b3cab9f9093a9aa066217b36cdb6d8f78d5c8a8a5d81d52976fd128dc99.jpg)  
FIGURE 3-23 Block diagram of the Connection Machine CM-5. Processing nodes, labeled with a $P$ ， execute user programs.Control processors, labeled $C P$ actaspartitionmanagers-front endsforclustersof processing nodes.l/O control processors control $1 / 0$ devices. (Reprinted by permission of Thinking Machines Corporation.)

The Paragon XP/S is the fourth in a series of commercial multicomputers manufactured by Intel Corporation in Beaverton, Oregon. A number of important hardware and software features distinguish the Paragon XP/S from the nCUBE 2 and the CM-5.

I The first interesting feature of the Paragon is that its nodes are organized as a 2-D mesh (Fig.3-24).Much of the hardware is dedicated to improving the communication speed of the system. Custom mesh-routing chips lie at each mesh intersection. Each of these chips can route more than 20o Mbytes of data per second. Inside the node a custom network interface chip serves as the interface between a node and its mesh routing chip. Finally, an i860 XP processor within each node,is dedicated to message passing, which frees the application processors from the details of message passing. Figure 3-25 illustrates a node of the Paragon XP/S.

JA second distinguishing characteristic of the Paragon XP/S is that it goes even further than the CM-5 in eliminating barriers between the front-end and back-end processors. In the Intel scheme of things, a node can play one of three roles.A “service node” supports general user services such as text editors, compilers, and UNIX shels. A “compute node” executes users’ application programs, usually in conjunction with other compute nodes. And finally, I/O nodes serve as intermediaries between service and compute nodes and the I/O devices. As in the CM-5,all of these node types are part of the same routing network. There are no arbitrary bottlenecks between service nodes and compute

![](images/2ddee09bb98142c25d09fa678feee7f43b14e55ac3d64837704a0f7619a8f53d.jpg)  
FIGURE 3-24 The Paragon XP/S uses a 2-D mesh processor organization. At each mesh point a mesh routing chip passes data at up to 2oo Mbytes/second. (Reprinted by permission of Intel Corporation.Copyright $\circledcirc$ IntelCorporation1993.)

# FIGURE 3-25

Architecture of a Paragon XP/S node. Each node contain at least one i860 XP application processor,one i860 XP message processor, performance monitoring hardware,and a network interface chip. Compute and service nodes can have between 16 and 128 Mbytes of primary memory. I/O nodes can have between 16 and 64Mbytes of primarymemory. I/O nodesalsocontain at least one $1 / \dot { 0 }$ interface. (Reprintedby permissionof Intel Corporation. Copyright $\circledcirc$ IntelCorporation1993.)

Application   
Processor   
i860XP Memory 16 - 64 MBytes   
Message   
Processor   
i860XP Network Interface   
Performance   
Monitor Expansion Port   
Transfer 400 MBytes/sec   
Engines (2) Singlecycles 50MHz

The role of nodes in a compute partition canchange over time. In this figure the system'snodesare divided into three batch partitions (A,B,and C) between midnight and 8 AM. Between8 AMand5PM the nodes aredivided into one batch partition (D)and three interactive partitions (E, F,and G). The reallocation of nodes can be done as the system is running.

<table><tr><td rowspan=2 colspan=1>A</td><td rowspan=1 colspan=1>D</td></tr><tr><td rowspan=1 colspan=1>E</td></tr><tr><td rowspan=2 colspan=1>Bs</td><td></td></tr><tr><td rowspan=1 colspan=1>F</td></tr><tr><td rowspan=1 colspan=1>C</td><td rowspan=1 colspan=1>G</td></tr></table>

nodes or between compute nodes and I/O nodes. Unlike the CM-5, however, the XP/S can be reconfigured,altering the relative number of service and compute nodes.

For example, during the daytime the system may be configured so that it has a larger number of service nodes to support the number of people logged into the system, while at night the system may be reconfigured to have fewer support nodes and more compute nodes, so that production jobs may finish more quickly.

In addition, the nodes in the compute partition can be divided into a number of subpartitions. Some subpartitions can be used to execute batch jobs, while others use timesharing to support multiple users. Figure 3-26 illustrates how the subpartitioning of Paragon compute nodes can change over time.

A third distinguishing characteristic of the Paragon XP/S is that it supports virtual memorywhich allows each process toaccessmore memory than phys ically exists on a single node.

The theoretical peak performance of the $\mathrm { i } 8 6 0 \mathrm { X P }$ CPU is 75 million doubleprecision floating-point operations per second. If a Paragon XP/S system were constructed with 1024 nodes, each containing four $\mathrm { i 8 6 0 ~ X P }$ application processors, the theoretical peak performance of the system would be about 300 gigaflops. At 128 Mbytes primary memory per node, the aggregate primary memory of the system would be 128 Gbytes.

# 3.5 FLYNN'S TAXONOMY

Flynn's taxonomy is the best known classification scheme for serial and parallel computer architectures. In this section we present his scheme and use it to categorize the parallel architectures we have described in this chapter.

Flynn bases his taxonomy of computer architectures on the dual concepts of instruction stream anddata stream (Flynn 1966,1972).Aninstructionstram is a sequence of instructions performed by a computer; a data stream is a sequence of data manipulated by an instruction stream. Flynn categorizes an architecture by the multiplicity of hardware used to manipulate instruction and data streams. “The multiplicity is taken as the maximum possible number of simultaneous operations (instructions) or operands (data) being in the same phase of execution at the most constrained component of the organization” (Flynn's emphasis) (Flynn 1966). Four classes of computers result from the given multiplicity of instruction and data streams.

Single Instruction stream, Single Data stream (SISD) Most serial computers fall into this category. Although instruction execution may be pipelined, computers in this category can decode only a single instruction in unit time. A SISD computer may have multiple functional units, but these are under the direction of a single control unit.

Single Instruction stream,Multiple ata stream (SMD) Processor arrays fall into this category.A processor array executes a single stream of instructions, but contains a number of arithmetic processing units, each capable of fetching and manipulating its own data. Hence in any time unit, a single operation is in the same state of execution on multiple processing units, each manipulating different data. The Connection Machine CM-200 is a SIMD computer.

Multiple Instruction stream, Single Data stream (MISD) Of the four categories in Flynn's taxonomy, MIsD is the least intuitive. How can a computer have multiple instruction streams but only a single data stream? Some think systolic arrays fit into this category. The word “systolic” means a rhythmic contraction, especially of the heart muscle. A systolic array is a parallel computer that rhythmically “pumps” data from processor to processor. Each processor may modify the data before passing it on to the next processor, which may perform a different operation on the data (see Fig. 3-27).

Multiple Instruction stream, Multiple Data stream (MIMD) -This category contains most multiprocessor systems. Early multiprocessors were built to increase the throughput of multiprogrammed operating systems,and there was little interaction among the CPUs. In this book the label MIMD is reserved for multiple-CPU computers designed for parallel processing; that is, computers designed to allow efficient interactions among their CPUs. The Symmetry, TC2000, nCUBE 2, Paragon XP/S,and Connection Machine CM-5 are MID computers.

![](images/53a0c667c369bebea767383b12b74917f2af6e0a7d01562e568de5ed4ea7ee86.jpg)  
FIGURE 3-27 A comparison of a traditional SISD computation model with the systolic array computation model，whichsome consideranexampleof D processing. (Hennessyand Patterson [1990].)

Flynn's classification scheme is too vague to allow iron-clad labeling of supercomputers. It is only natural, then, that there is some disagreement among experts as to how to classify certain architectures.For example,in what category does the Cray-1,a pipelined vector processor, belong? Because it is a vector computer, Hockney and Jesshope (1981) label the Cray-1 an example of an SIMD architecture. Because it does not have multiple processing elements, Hwang and Briggs (1984) put the Cray-1 into the SISD category. Hwang and Briggs’position seems more consistent with Flynn's definition that we quoted earlier, so we categorize the Cray-1 as a SISD computer. In this text the terms SIMD computer and processor array are synonymous.

# 3.6 SPEEDUP,SCALED SPEEDUP,AND PARALLELIZABILITY

Two important measures of the quality of parallel algorithms implemented on multiprocessors and multicomputers are speedup and efficiency. The speedup achieved by a parallel algorithm running on $p$ processors is the ratio between the time taken by that parallel computer executing the fastest serial algorithm (on one processor) and the time taken by the same parallel computer executing the corresponding parallel algorithm using $p$ processors. The efficiency of a parallel algorithm running on $p$ processors is the speedup divided by $p$

An example illustrates the terminology. If the best known sequential algorithm executes in 8 seconds on a parallel computer,while a parallel algorithm solving the same problem executes in2 seconds when five processors are used, then we say that the parallel algorithm “exhibits a speedup of 4 with five processors.” A parallel algorithm that exhibits a speedup of 4 with five processors "has an efficiency of O.8 with five processors."

Some define the speedup of a parallel algorithm running on $p$ processors to be the time taken by the parallel algorithm on one processor divided by the time taken by the parallel algorithm using $p$ processors. This definition can be misleading since parallel algorithms frequently contain extra operations to facilitate parallelization. Comparing the execution time of a parallel algorithm running on many processors with that same algorithm running on one processor can exaggerate the speedup, because it masks the overhead of the parallel algorithm. In this book we use the term parallelizability to refer to the ratio between the time taken by a parallel computer executing a parallel algorithm on one processor and the time taken by the same parallel computer executing the same parallel algorithm on $p$ processors.

# 3.6.1 Can Speedup Be Greater than Linear?

Is superlinear speedup possible? Inother words, is it possible for the speedup achieved by a parallel algorithm to be greater than the number of processors used? The answer is that it depends upon the assumptions made.

Some people argue that speedup cannot be greater than linear (e.g., see Faber et al. 1986). They base their proof on the premise that a single processor can always emulate parallel processors. Suppose a parallel algorithm $A$ solves an instance of problem $\Pi$ in $T _ { p }$ units of time on a parallel computer with $p$ processors. Then algorithm $A$ can solve the same problem instance in $p \times T _ { p }$ units of time on the same computer with one processor through time slicing. Hence the speedup cannot be greater than $p$ .Since parallel algorithms usually haveassociated overhead,it is most likely there exists asequential algorithm that solves the problem instance in less than $p \times T _ { p }$ units of time,which means the speedup would be even less than linear.

We disagree with two assumptions made in the previous proof. One assumption is algorithmic, and the other is architectural. Let us first examine the questionable algorithmic assumption.

Is it reasonable to choose the algorithm after the problem instance is chosen? Speedup is intended to measure the time taken by the best sequential algorithm divided by the time taken by the parallel algorithm,but itis going too far to allow the definition of “best’ to change every time the problem instance changes. In other words, it is more realistic to assume that the best sequential algorithm and the parallel algorithm be chosen before the particular problem instance is chosen. In this case it is possible for the parallel algorithm to exhibit superlinear speedup for some problem instances. For example,when solving a search problem, a sequential algorithm may waste a lot of time examining a dead-end strategy. A parallel algorithm pursues many possible strategies simultaneously, and one of the processes may “luck out” and find the solution very quickly.

The second questionable assumption is that a single processor can always emulate multiple processors without a loss of efficiency. There are often architectural reasons why this assumption does not hold. For example, each CPU in a UMA multiprocessor has a certain amount of cache. A group of $p$ processors executing a parallel algorithm has $p$ times as much cache memory as a single processor. It is easy to construct circumstances in which the collective cache hit rate of a group of $p$ processors is significantly higher than the cache hit rate of a single processor executing the best sequential algorithm or emulating the parallel algorithm. In these circumstances the $p$ processors can execute a parallel algorithm more than $p$ times faster than a single processor executing the best sequential algorithm.

The reader may favor either side of the argument, but we have adopted the latter position. Later in the book examples of superlinear speedup are given where the problem instance is chosen after the sequential and parallel algorithms havebeenselected.

# 3.6.2 Scaled Speedup

Let $f$ be the fraction of operations in a computation that must be performed sequentially,wher $0 \leq f \leq 1$ .Amdahl's law states that the maximum speedup $s$ achievable by a parallel computer with $p$ processors performing the

computation is

$$
S \leq { \frac { 1 } { f + { \frac { ( 1 - f ) } { p } } } }
$$

A corollary follows immediately from Amdahl's law: a small number of sequential operations can significantly limit the speedup achievable by a parallel computer. For example, if 10 percent of the operations must be performed sequentially,then the maximum speedup achievable is 10, no matter how many processors a parallel computer has.

Amdahl's law is based upon the idea that parallel processing is used to reduce the time in which a problem of some particular size can be solved, and in some contexts this is a reasonable assumption.In many situations, however, parallel processing is used to increase the size of the problem that can be solved in a given (fixed) amount of time. For example, a design engineer checking the turbulence around an air foil may be willing to wait an hour for the computer to determine the solution. Increasing the speed of the computer allows the engineer to increase the resolution of the computed answer. Under these circumstances,Amdahl's law is not an accurate indicator of the value of parallel processing, because Amdahl’s law assumes that the sequential component is fixed.

However, for many problems the proportion of the operations that are sequential decreases as the problem size increases. Every parallel program has certain overhead costs, suchas creating processes,which are independent of the problem size. Other overhead costs, such as input/output and process synchronization,may increase with the problem size,but at a slower rate than the grain size. This phenomenon is called the Amdahl effect (Goodman and Hedetniemi 1977),and it explains why speedup is almost universally an increasing function of the size of the input problem (Fig. 3-28).

Scaled speedup is the ratio between how long a given optimal sequential program would have taken, had it been able to run on a single processor of a parallel computer,and the length of time that the parallel program requires when executing on multiple processors of the same parallel computer (Gustafson

![](images/4a3939d6cfe498d1940d9199299d6d21d911de2a5beb6f2b011dec52196b8e42.jpg)  
FIGURE 3-28 The Amdahl effect. As a general rule,speedup isan increasing function of the problem size.

1988; Gustafson et al. 1988). We define scaled efficiency to be scaled speedup divided by the number of processors used.

The difference between speedup and scaled speedup is subtle, yet important. In order to measure speedup, the algorithm must run on a single processor. On a multicomputer, that means the problem data must fit in the memory of that one processor. Far larger problems can be, and usually are, solved by systems with hundreds or thousands of processors,but the restriction that the problem be solvable by a single processor means that these large problems cannot be used to determine the speedup achieved by the parallel machine. The definition of scaled speedup allows the solution of these realistic, large problems on a multicomputer and an estimation of the execution time that would have been required if the same problems had been solved on a single processor with a massive primary memory.

For example, suppose we are interested in solving the largest system of linear equations we can in one minute. We would like to find out if we can make efficient use of a particular parallel computer to perform this task. A good sequential algorithm performs roughly $2 n ^ { 3 } / 3$ floating-point operations to solvea dense $n \times n$ system of linear equations. Given a processor capable of 100 million foating-point operations per second, the largest linear system we can solve in one minute is approximately

$$
{ \frac { \left( 2 n ^ { 3 } / 3 \right) \ { \mathrm { o p s } } } { 1 0 0 , 0 0 0 , 0 0 0 \ { \mathrm { o p s } } / { \mathrm { s e c } } } } \leq 6 0 \ { \mathrm { s e c } } \Rightarrow
$$

Now consider the implementation of a parallel linear system solver on a multicomputer system with 1024 processors. Assume that each processor performs 100 million floating point operations per second. Suppose sending or receiving a message requires 1 microsecond message initiation time plus 5 nanoseconds transmission time per floating-point value. A parallel linear system solver has each of the $p$ processors performing roughly $2 n ^ { 3 } / ( 3 p )$ floating-point operations and sending or receiving about $4 n \log p$ messages containing a total of about $n ^ { 2 } / 2$ floating-point values. Given these assumptions, the largest system we can solve in one minute on the 1024-processor system is (maintaining 3 digits of precision)

$$
{ \frac { \left( 2 n ^ { 3 } / 3 0 7 2 \right) { \mathrm { ~ o p s } } } { 1 \times 1 0 ^ { 8 } { \mathrm { ~ o p s } } / { \mathrm { s e c } } } } + { \frac { ( 4 0 n ) { \mathrm { ~ m s g s } } } { 1 \times 1 0 ^ { 6 } { \mathrm { ~ m s g s } } / { \mathrm { s e c } } } } + { \frac { \left( n ^ { 2 } / 2 \right) { \mathrm { ~ f l o a t s } } } { 2 \times 1 0 ^ { 8 } { \mathrm { ~ f l o a t s } } / { \mathrm { s e c } } } } \leq 6 0 { \mathrm { ~ s e c } } \Rightarrow
$$

$$
6 . 5 1 \times 1 0 ^ { - 1 2 } n ^ { 3 } + 4 . 0 0 \times 1 0 ^ { - 5 } n + 2 . 5 0 \times 1 0 ^ { - 9 } n ^ { 2 } \leq 6 0 \Rightarrow
$$

This calculation assumes, of course, that the entire system of equations fits in the aggregate primary memory of the multicomputer.

Now we can determine the scaled efficiency of the parallel implementation. A single 10o-megaflop processor executing the sequential algorithm would require roughly 59,00o seconds to solve a system of size 20,700. The scaled speedup of this application is $5 9 , 0 0 0 / 6 0$ or about 983. The scaled efficiency of the processors is 983/1024 or about $9 6 \%$ . In other words, the utilization of the 1024 processors is very high when solving a system of size 20,700 in 60 seconds.

# 3.7 SUMMARY

This chapter has discussed nine processor organizations and several parallel computer architectures. Processor organizations that have been suggested for parallel computers include the mesh,binary tree,hypertree,pyramid,butterfly, hypercube,cube-connected cycles, shuffle-exchange,and de Bruijn networks. We have evaluated these organizations according to four criteria: diameter, bisection width, number of connections per node, and whether or not increasing the number of nodes leads to an increase in the maximum connection length. These criteria help us determine both the suitability of the processor organization for supporting efcient parallel algorithms and the practicality of the organization from a manufacturing point of view.

Flynn's taxonomy divides all computers into four classes, based upon the serial/parallel processing of the instruction and data streams. Traditional sequential computers fall into the SISD category. Processor arrays are SIMD computers.Systolic arrays can be viewed as falling into the MiSD category, while multiple-CPU computers, both multiprocessors and multicomputers,are MIMD.

A processor array is a practical implementation of a SIMD model of computation, in which parallel processing is achieved through the application of a single operation to a data set. It is not feasible to construct a processor array in which every processing element shares access to a common memory.In a real processor array，each processing element has its own local memory. The underlying processor organization determines the manner in which data are passed from processing element to processing element. For this reason we characterize SIMD models by the organization of the processing elements.

We described in some detail the Connection Machine CM-20o,a well-known commercial processor array.

MIMD computers are a more general-purpose model of parallel computation, since they consist of a number of CPUs asynchronously executing independent instruction streams. MIMD computers can be categorized by the way that the CPUs access memory. UMA multiprocessors have a single, shared address space,and the distance froma CPU toany memory location isa constant.

NUMA multiprocessors also have a shared address space, but each memory cell is closer to one CPU than it is to the others.Multicomputers have no shared memory. Each CPU has its own private address space,and the processors interact through message passing.

In this chapter we described five commercial MIMD computers: the Sequent Symmetry,a UMA multiprocessor, the BBN TC2000,a NUMA multiprocessor, and the three multicomputers; the nCUBE 2, Thinking Machines CM-5,and Intel Paragon XP/S.

Speedup and efficiency are two important measures of the quality of a particular parallel algorithm implementation. Given the best sequential algorithm and a corresponding parallel algorithm, there may exist particular problem instances for which the parallel algorithm exhibits superlinear speedup (and hence efficiency greater than 1) for certain numbers of processors.

Amdahl’s law assumes that parallel processing is used to reduce the time needed to solve a problems of a fixed size. However, parallel computers are often used to increase the size of a problem that can be solved in a fixed amount of time. In these circumstances scaled speedup is superior to speedup as a measure of the quality of a parallel algorithm.

# 3.8 BIBLIOGRAPHIC NOTES

The texts by Siegel (1985), Ullman (1984), and Uhr (1984) contain a wealth of information on processor interconnection methodologies. Feng (1981） also surveys connection methods.

Miller and Stout (1984b,1985b, 1987) have described algorithms for pyramid computers. The shuffle-exchange network was introduced by Stone (1971). Additional references on shufle-exchange networks include Kumar and Reddy (1987), Lang and Stone (1976) and Wu and Feng (1981). Lawrie (1975) introduced the omega network,a multistage network based on perfect shuffle connections. Siegel (1979a) shows how other interconnection networks can simulate the perfect shuffle.

The evaluation of interconnection networks for multicomputers is the subject of a paper by Agrawal et al. (1986). Reed and Grunwald (1987) discuss methods that can be used to choose the best interconnection network for a class of applications. Bhuyan et al. (1989) give a tutorial on evaluation tools to help designers evaluate network performance.

The April 1989 issue of IEEE Transactions on Reliability isa special issue focusing on the reliability of parallel and distributed computing networks. Other papers discussing fault tolerance of interconnection networks include Adams (1987) and Das et al. (1990)

Papers discussing de Bruijn networks include (Esfahanian and Hakimi 1985 Pradhan 1985;Samatham and Pradhan 1989,1991; Sridar 1988).

Two other processor organizations, not discussed in this chapter, deserve mention. Rosenfeld (1985) has proposed the prism network as an alternative tc the pyramid. A prism network contains as many levels as a pyramid network, but,unlike a pyramid, every level of the prism contains the same number of processors. Prisms have a number of interesting attributes. A prism can simulate a pyramid in linear time. In addition, a prism can compute a fast Fourier transform in linear time. Also, the mesh-of-trees network has captured the interest of some theoreticians. Properties of this topology are discussed in Ullman (1984).

A parallel model is reasonable if the number of processors each processor can communicate with is bounded by a constant (Goldschlager 1982). A natural question is whether each of these reasonable processor organizations-mesh, pyramid,butterfly,shufle-exchange,de ruijn,cbe-connected cycles,ir tree,and hypertree—is superior for some class of problems or whether one of these is the best overall model. Galil and Paul (1981, 1983) show that a universal parallel model can simulate every reasonable parallel model “with only a small loss of time and with essentially the same number of processors." The heart of their universal computer is a sorting network that is used as a "post office” for sending and requesting information. Galil and Paul have shown that since cube-connected cycles are used as the sorting network, the cube-connected cycles network (and hence the butterfly) is an efficient general-purpose network. However,constants of proportionalityare unimportant toa theoretician,yetare vital to a computer architect interested in building a supercomputer. This may be one reason why commercial parallel computer companies have not rushed to build computers based upon the cube-connected cycles network.

Books on parallel computer architecture include Almasi and Gottlieb (1989), Frenkel (1986), Hockney and Jesshope (1981)， Hwang and Briggs (1984), Lipovski and Malek (1987), and Tabak (199O). The Hennessy and Patterson (1990) architecture book has an excellent chapter on parallel processing.

Duncan (1990, 1992) has surveyed parallel computer architectures, both SIMD and MIMD. Lubeck (1988) describes models and supercomputer performance and discusses benchmarking practices.

A large number of references exist for processor arrays. Books by Thurber (1976), Kuck (1978),Stone (1980),and Hwang and Briggs (1984) introduce the subject. Paul (1978), Thurber (1979),and Hwang, Su,and Ni (1981) have compared various processor array architectures. Hockney and Jesshope (1981) cover the DAP,a mesh-connected processor arrayin their monograph. The DAP is also discussed by Reddaway (1979). Barmes et al. (1968) and Falk (1976)are references for the ILLIAC IV computer. Batcher (1980)and Fung (1977)describe Goodyear's Massively Parallel Processor.

Enslow (1977) is an early survey of multiprocessor architectures.Fuller and Oleinick (1976)and Mashburn (1979) have writen about C.mmp,a multiprocessor developed at Carnegie-Mellon University in the 197Os. Gottlieb (1986) and Gottlieb et al. (1983) describe the New York University Ultracomputer. Mudge et al. (1987) argue that the number of CPUs in a UMA multiprocessor can be increased to a few hundred by replacing a single shared bus with a set of buses. Thakkar et al. (1990) also discuss methods to build larger UMA multiprocessors.

An important problem associated with UMA multiprocessors is cache coherency. Stenstrom (1990) has surveyed cache coherency schemes. Other articles discussing the cache coherency problem include (Archibald and Baer 1986;Chaiken etal. 1990; Cheong and Veidenbaum 1990; Eggers and Katz 1989;Gupta and Weber 1992;Hill andLarus1990; Teller1990).

Stenstrom (1988) surveys methods to reduce contention in UMA multiprocessors. Dinning (1989) and Graunke and Thakker (1990) describe synchronization algorithms for UMA multiprocessors.

Stone (1980) and Swan et al. (1977) are two of many sources of information on $\mathbf { C } \mathbf { m } ^ { * }$ ,a NUMA multiprocessor constructed at Carnegie-Mellon University. Cheriton et al. (1991) discuss Paradigm,a NUMA multiprocessor under development at Stanford University.

Seitz (1985) describes the implementation of the Cosmic Cube,a hypercube multicomputer built at the California Institute of Technology. Athas and Seitz (1988) describe contemporary multicomputer architectures and algorithms.

The February 1982 issue of Computer is dedicated to data-flow computing and it is a good place to start learning more about the subject. Particularly useful articles in this issue are those by Ackerman (1982),Davis and Keller (1982), Gajski et al. (1982),and Watson and Gurd (1981). Gurd, Kirkham, and Watson (1985) have described the prototype data-flow computer built at the University of Manchester.

Much attention has been given to designing parallel algorithms for VLSI circuits.A representative set of references includes Bilardi, Pracchi,and Preparata (1981); Chazelle and Monier (1981a,1981b); Kung (1982); Mead and Conway (1980); Lang et al. (1983); Leighton (1983);Leiserson (1983);Shroder (1983); Thompson (1980, 1983); and Ullman (1984).

Kutti (1985) has proposed a taxonomy for parallel and distributed systems that uses “the address space or buffer type as the key identifying element.” This classification scheme is able to distinguish multiprocessors from multicomputers, both of which fall into Flynn's MIMD category. Skillicorn (1988) has proposed an extension to Flynn's taxonomy that also serves to distinguish various MIMD computers. Yet another classification scheme has been proposed by Handler (1977).

Distributed shared memory is the implementation of the shared-memory abstraction on a multicomputer architecture. Nitzberg and Lo (1991) and Stumm and Zhou (199o) compare algorithms for implementing distributed shared memory.

Numerous papers describe models for predicting the speedup and/or scalability of parallel algorithms.A few referencesare Eager et al. (1989),Flatt and Kennedy (1989), Karp and Flatt (199O), and Nussbaum and Agarwal (1991).

3-1What is the difference between a binary $k$ -cube and a cube-connected network of degree $k$ ？

Given a $d$ -dimensional hypercube and a designated source node $s$ ,howmany nodes are distance $i$ from $s$ ,where $0 \leq i \leq d ^ { \circ }$ ？

$3 . 3 ^ { * }$ A shuffle-exchange network can simulate a hypercube network. Because not every pair of nodes connected in a hypercube.is connected in a shuffle-exchange network, a single hop along a communication link in a hypercube may turn into several hops in a shuffle-exchange network. Derive an upper bound on the maximum number of communications necessary in a shufle-exchange network to simulate a single communication in a hypercube.

3-4Given a shuffle-exchange network, prove that if a shuffle link connects nodes i and $j$ ,then $j$ isa single-bit left cyclic rotation of $i$

Given a shuffle-exchange network with $2 ^ { k }$ nodes,under what circumstances are nodes $i$ and $j$ exactly $2 k - 1$ link traversals apart?

Prove that the number of necklaces in an $n$ -node shuffle-exchange network is $O ( 2 ^ { k } / k )$ ·

3-7 Show how to perform the perfect shuffle network's exchange operation on a de Bruijn network.

3-8 A bipartite graph is a graph $G$ with the property that its set of vertices can be decomposed into two disjoint subsets $V _ { 1 }$ and $V _ { 2 }$ such that every edge in $G$ connects a vertex in $V _ { 1 }$ with a vertex in $V _ { 2 }$ .Which of the graphs described in Sec.3.1 are bipartite?

3-9Name two ways to implement vector computers.

3-10 What are the advantages and disadvantages of moving from the UMA multipro cessor model to the NUMA multiprocessor model?

3-11 Read this quote from Lillevik (1991): “The CSC Touchstone DELTA [multicomputer] System features a glass-like front door with an array of LEDs that indicate both processor and communication status. Physically, each node in the mesh is mapped to a corresponding position on the front door. At this location, there is both a red and green LED that the application can control. Between each set of node LEDs,a longer LED spans the distance and illuminates when a message traverses that position in the interconnect. As an application runs, the LEDs offer a rather unique picture or signature of node activity and this communication is useful for application debugging and performance tuning."What does this quote say about the state of application debugging and performance monitoring tools on some contemporary parallel computers?

3-12 The bisection bandwidth of a parallel computer is the bisection width of its underlying processor organization multiplied by the data transfer rate of each communication link.What is the bisection bandwidth of a Paragon XP/S configured as a $1 6 \times 6 4$ mesh? What is the bisection bandwidth of a CM-5 with 1024 nodes?

3-13Suppose a multiprocessor is built out of individual processors capable of sustain-ing 50 megaflops. What is the largest fraction of a program's execution time that could be devoted to sequential operations if the parallel computer is to exceed the performance of a supercomputer capable of sustaining 1 gigaflops?

3-14 Is it possible for the average speedup exhibited by a parallel algorithm to be superlinear?

3-15 Calculate the speedup that would be achieved on a system of size 2,080 by the hypothetical parallel linear system solver described in Sec.3.6 asa function of number of processors $p$ ,where $1 \leq p \leq 1 0 2 4$

# 4

There are many different languages in the world, yet none of them is without meaning. ButifIdo not know the language being spoken,the person who uses itwillbeaforeigner to me,and Iwill bea foreigner to him.

1 Corinthians 14:10-11

In this chapter we describe six of the languages used to program parallel computers and how these languages address the problems of parallel process allocation and coordination. In Sec.4.1 we present a high-level view of parallel programming issues. In Sec. 4.2 through 4.7,we introduce six parallel programming languages. In Sec. 4.8,we describe the pseudocode we will use to represent parallel algorithms in the remainder of the text.

Our focus is on imperative languages, because the majority of sequential and parallel programs are written in the imperative style. Many parallel programmers will continue to use imperative languages, even if research in logic programming and functional programming languages leads to efficient implementations on parallel machines. See the bibliographic notes at the end of this chapter for more references regarding paralel implementations of functional and declarative languages.

# 4.1 PROGRAMMING PARALLEL PROCESSES

Every parallel language must address certain issues,either explicitly or implicitly. There must be a way to create parallel processes,and there must be a way to coordinate the activities of these processes. Sometimes the processes work on'their own data and do not interact. But when processes exchange results, they must communicate and synchronize with each other. Communication and synchronization can be accomplished by sharing variables orby message passing.

There are two methods of synchronization: synchronization for precedence and synchronization for mutual exclusion. Precedence synchronization guarantees that one event does not begin until another event has finished. Mutual exclusion synchronization guarantees that only one process at a time enters a critical section of code where a data structure to be shared is manipulated.

# 4.1.1 An llustrative Example

The way in which the creation, communication, and synchronization of processes are ultimately implemented depends upon the target architecture. To illustrate this point,let’s consider the problem of computing,fora list of real numbers,the variance of the values: given $r _ { 1 } , r _ { 2 } , r _ { 3 } , . . . , r _ { n }$ ,compute $\sum _ { i } ^ { n } ( r _ { i } -$ $m ) ^ { 2 } / n$ where $\begin{array} { r } { m = \sum _ { 1 } ^ { n } r _ { i } / n } \end{array}$

Suppose we want to implement a parallel algorithm to perform this task on a UMA multiprocessor with four processors. We store the $n$ real numbers in shared memory.We also reserve four variables in shared memory: one will contain the grand total,another the mean, a third the global sum of squares, and a fourth the variance. In sequential code we initialize the two accumulator variables to zero.We create four processes,one per processor.Each process has a local temporary variable. Each process adds its share of the $n$ values, accumulating the sum in its local temporary variable. When the process is through computing its subtotal, it adds its subtotal to the shared variable, accumulating the grand total. Since multiple processes are accessing the same global variable, that portion of code is a critical section, and the processes must enforce mutual exclusion. A barrier synchronization step, inserted in the algorithm after the critical section, ensures that no process continues until all processes have added their subtotals to the grand total. In sequential code one process computes the average by dividing the grand total by $n$ . To compute the global sum of squares,the processes go through a process similar to that which computes the global sum. Again, the processes must enforce mutual exclusion as they add the sum of squares for their part of the list to the grand total. After another barrier synchronization, one process computes the variance by dividing the sum of squares by the number of values. We illustrate the procedure in Fig. 4-1.

Now let us consider how to solve the same problem on a four-node hypercube multicomputer. The program executing on the host processor allocates the

（b)

![](images/46920fb5a53e48e00104fd641d26e56cf9bcb4e259981a02c0487b797ca72fb6.jpg)  
FIGURE 4-1 Computation of variance of a list of numbers on a UMA multiprocessor. (a) Each process totalsits share of thevalues,accumulating the suminitsown temporary variable.When ithasfounditsbtotal,itddsitsbotaltothegrandtotalstoredinaaredale. (b)Asingleprocess computesthemeangiven the sum.(c) ach process findsoits setof three values,the sum of the square of the difference between each value and themeanaccumulating the sum of squaresinitsowntemporaryvariable.Whenithas found itssubtotal,itadds itssubtotal tothegrand totalstored inasharedvriable.(d)A singleprocess divides the sum of squaresby 12 to determine the variance.

hypercube (gaining access to the nodes) and starts a node process executing on each of the four nodes of the back end. There is no shared memory; the $n$ values are distributed among the local memories of the nodes. Each node process has four variables: two to accumulate sums,one to store the mean,and another to store the variance.Each node process initializes the two accumulator variables to zero. It then accumulates the sum of its local portion of the list into the global sum variable.At this point every process has a subtotal; the four subtotals must be combined to find the grand total. After two exchange-and-add steps,every process has the grand total. Every process can divide the grand total by $\eta$ to determine the mean.

A similar set of steps allows the processes to compute the variance of the list values. Every process has the result. One of the processes can pass the answer back to program running on the front end, which then deallocates the hypercube, surrendering access to the nodes. The procedure is illustrated in Fig. 4-2.

Low-level parallel languages present the programmer with constructs closely tied to the underlying architecture. For example,Sequent C, targeted toa UMA multiprocessor, enhances C by adding constructs for declaring shared variables, forking and killing parallel processes,locking and unlocking variables to enforce mutual exclusion, and enforcing barrier synchronizations. In contrast, nCUBE C, targeted to a hypercube multicomputer, enhances C by adding constructs for sending,receiving,and testing for the existence of messages between processors. We will examine both these low-level parallel languages later in this chapter.

High-level parallel languages present the programmer with a more abstract model of parallel computation. This can make programs shorter and easier to understand. Another advantage of a high-level parallel language is that it may be less dependent on the system architecture, increasing program portability. The disadvantage of a high-level language, of course, is that it makes compiler construction more challenging,since high-level languages increase the demands programmers make on the target hardware. We will explore four high-level parallel imperative languages in this chapter: the SIMD languages Fortran 90 and $\mathbf { C } ^ { * }$ ，and the MIMD languages occam and C-Linda.

Many have argued that the existence of billions of dollars’ worth of programs written in sequential languages-particularly FORTRAN--implies that the most reasonable approach to programming parallel computers is to provide users with compilers to translate sequential programs into code that works on parallel machines. For more than 20 years researchers have continued to develop more sophisticated analysis techniques to facilitate the translation process.Whether or not the approach is sound, it is outside the scope of this book. The bibliographic notes list books devoted to automatic parallelization of sequential programs.

# 4.1.2 A Sample Application

We will implement a solution to a simple numerical integration problem using each language. The parallel program must compute an approximation to $\pi$ by using numerical integration to find the area under the curve $4 / ( 1 + x ^ { 2 } )$ between 0 and 1 (Fig. 4-3).

![](images/b007853e104959a3f04ad4fdc0bd5656a7d6d141e26ef754be7bacf11a734b31.jpg)  
FIGURE 4-2 Computing the variance of a list of numbers on a four-node hypercube multicomputer. (a)Each process sums its own values.(b) Processes swap valuesandaccumulate total. Eachprocessdivides total by12 to get mean.(c) Each processcomputes,for itsowset of values,thesum of thesquaresof thedifferencebetweeneachvalueand the mean. (d) Processes swap valuesand accumulate total sumof squares.Each processdivides totalby12togetvariance.

The interval [O, 1] is divided into $n$ subintervals of width $1 / n$ .For each of these intervals the algorithm computes the area of a rectangle whose height is such that the curve $4 / ( 1 + x ^ { 2 } )$ intersects the topof therectangle at its midpoint. The sum of the areas of the $n$ rectangles approximates the area under the curve. Increasing $n$ reduces the difference between the sum of the rectangle's area and the.area under the curve.

![](images/2661185f7ba67574586719fcb265036fa167cc495eda9b33b25853e68a5c822a.jpg)  
FIGURE 4-3 The area under the curve $4 / ( 1 + x ^ { 2 } )$ between 0 and 1 is $\pi$ .Thearea of the rectangles approximatesthe areaunder the curve. (Courtesy Hatcher and Quinn (1991).

This algorithm is data-parallel, since the areas of all the rectangles can be computed simultaneously. Computing the area of each rectangle requires the same amount of work: hence load balancing is insignificant. If the language requires us to divide the work among the processors,we can do so easily.

# 4.2 FORTRAN 90

In 1978 the ANSI-accredited technical commitee,，X3J3, began working on a new version of the FORTRAN language. In the early 199Os the resulting language, Fortran 9O, was adopted as an ISO and ANSI standard. Fortran 90 is a superset of FORTRAN77. It includes allthe features of FORTRAN 77, plus

· Array operations · Improved facilities for numerical computations · Syntax to allow processors to support short integers, packed logicals, very large character sets,and high-precision real and complex numbers · User-defined data types, structures, and pointers

· Dynamic storage allocation   
· Modules to support abstract data types   
Internal procedures and recursive procedures   
，Improvements to input-output facilities   
New control structures   
· New intrinsic procedures   
· Terminal-oriented source form

The committee also marked many language features as obsolete, including arithmetic IF,some construct variations,assignedGO TO,assigned ormats, and the H edit descriptor. The next revision of the FORTRAN standard may not contain these features.

In this section we will describe only a small portion of the language. For a more complete description of the Fortran 90 language, refer to Metcalf and Reid (1990),our primary source for the information and examples in this section.

# 4.2.1 Fortran 90 Programmer's Model

The Fortran 90 programmer has a model of parallel computation similar to a PRAM (Fig. 4-4).A CPU and a vector unit share a single memory. The CPU executes sequential instructionsaccessing ariables stored inthered memory.To execute parallel operations,the CPU controls the vectorunit, which also storesand fetches data toand fromthe shared memory.

# 4.2.2 Fortran 90 Language Features

Fortran 90 gives the programmer the ability to specify the type of variables through type declaration statements,such as

REAL A,B, C INTEGER I

Each type may have several kinds. For example, a real variable may be stored in 4 bytes or 8 bytes. The Fortran 90 programmer may specify explicitly the kind,as wellas the type of the variable,as in the following example:

![](images/07a819bf47d4261278cd0901383fd203582674b43909f2a747b7106f53dfc437.jpg)  
-4The Fortran 90 programmer's model of parallel computation.

Fortran 90 introduces the notion of an array constant.For example, denotes a one-dimensional array with five elements. It is possible to construct an array of higher dimension by declaring an array constant, then changing its dimension with the RESHAPE function.

An implied Do notation can simplify the specification of array constants. For example, the array constant

may be specified as

Fortran 90 also allows operations on arrays. When applied to an array, the unary intrinsic operators $^ +$ and - return an array of the same dimensions, where the elements in the result array are found by applying the operator to the corresponding elements in the operand array. Numerical, relational, and logical binary intrinsic operators can manipulate arrays having the same dimensions. Each element in the result array is found by applying the operator to the corresponding elements in the operand arrays. A binary intrinsic operator can also manipulate an array and a scalar variable, resulting in an array of the same dimensions as the array operand.

# For example, given the array declarations

REAL,DIMENSION(100,50):: X,Y REAL,DIMENSION(10O) :: Z

the following are examples of legal array expressions:

$\mathrm { ~ \tt ~ { ~ X ~ } ~ } + \mathrm { ~ \tt ~ { ~ Y ~ } ~ }$ !Array of shape (100,50),elements $\mathbb { X } \left( \mathbb { I } , \mathbb { J } \right) + \mathbb { Y } \left( \mathbb { I } , \mathbb { J } \right)$   
$\mathrm { ~ X ~ + ~ } 1 . 0$ !Array of shape (100,50)，elements $\mathrm { ~ X ~ } ( \mathrm { ~ I ~ } , \bar { \mathrm { ~ J ~ } } ) + 1 . 0$   
X.EQ. Y ！ Array of shape (10o,50)，elements having !value .TRUE.if X(I,J).EQ.Y(I,J) and.FALSE. !otherwise   
X(1:100,3)+Z ! Array of shape (100), !elements $\mathbb { X } \left( \mathbb { I } , 3 \right) + \mathbb { Z }$ (I)

Sometimes it is important to be able to perform an operation on a subset of the array elements. The WHERE statement allows the programmer to specify which array elements are to be active. For example, the statement

replaces every positive element of A with its square root. In its most general form,the EREsatement divides thearray elementsintotwosets,first per forming one or more array assignments on the elements for which the expression is true, then performing one or more array asignments on the elements for which the expression is false.The syntax of the most general WHERE statement is

WHERE (logical-array-expression) array-assignment-statements

ELSEWHERE array-assignment-statements

END WHERE

Finally, new transformational functions allow the reduction of an array into a scalar value. For example, the function SUM returns the sum of the elements of the array passed to it as an argument.

# 4.2.3 Sample Program

Figure 4-5 contains a Fortran 90 program to compute π using numerical integration. The parameter N, declared in line 1, is the number of subintervals. In line 2 we declare parameter LONG, used to set up floating-point variables

1. INTEGER， PARAMETER : : $\mathbb { N } = 1 3 1 0 7 2$   
2. INTEGER， PARAMETER :: LONG $=$ SELECTED_REAL_KIND(13,99)  
3. REAL(KIND $=$ LONG)PI，WIDTH  
4. INTEGER,DIMENSION(N) :: ID  
5. REAL(KIND $=$ LONG),DIMENSION(N) :: X,Y  
6. WIDTH $=$ 1.0_LONG / N  
7. $\ I { \boldsymbol { \mathsf { D } } } =$ (/(I， $\ I = 1$ 、N)/)  
8. $ { \mathtt { X } } \ = \ \left( \ \underline { { \mathtt { I D } } } \ - \ 0 . 5 \right)$ $\star$ WIDTH  
9. $\mathrm { ~ Y ~ = ~ 4 ~ . ~ 0 ~ / ~ } \left( \mathrm { ~ 1 ~ . ~ 0 ~ + ~ X ~ ^ { \star } ~ X ~ } \right)$   
10. $\mathrm { P I } = \mathrm { S U M }$ (Y) $\star$ WIDTH  
11.10 FORMAT（' ESTIMATION OF PI WITH‘,I6， &  
12. 'INTERVALS IS ',F14.12)  
13. PRINT 10,N, PI  
14. END

with at least 13 digits of precision and exponents covering at least the range $1 0 ^ { - 9 9 }$ through $1 0 ^ { 9 9 }$ .These high precision floating-point variablesaredeclared in lines 3 and 5. In line 6 we compute the width of each subinterval. The array ID, declared in line 4 and initialized in line 7,represents the subinterval number associated with each array element. In line 8 we compute in parallel the midpoint of each of the subintervals,and in line 9 we compute in parallel the height of the function curve at each of these points. Line 1O contains the call to the SUM function, which adds the heights of all of the rectangles, then multiplies the total height by the rectangles’ width to yield the area under the curve.In line 13 we print the result.

4.3 C\*

In 1987, Thinking Machines Corporation announced the availablility of $\mathbf { C } ^ { * }$ ，a data-parallel extension of the C language suitable for programming the Connection Machine. In 1990, Thinking Machines announced $\mathbf { C } ^ { * }$ ,Version 6.0 with syntax and semantics radically different from the prior versions of $\mathbf { C } ^ { * }$ .We describe a few ways in which $\mathbf { C } ^ { * }$ ，Version 6.0 supports the programming of SIMD algorithms, and we conclude with a sample program.

# 4.3.1 $\ b { \ b { \ b { \ b { \ b { \ b { \ b { \ b { \ b { \ b { \ b { \ b { \ b { \ b { \ b { \ b { \ b { \ b { \ b { \ b { \ b } { \ b { \ b { \ b { \ b { \ b } } } } } } } } } } } } } } } } } } } } } } } }$ Programmer's Model

$\mathbf { C } ^ { * }$ programmers imagine they are programming a SIMD computer consisting of a front-end uniprocessor atached to an adaptable back-end parallel processor (Fig.4-6). The front-end processor stores the sequential variables and executes the sequential code. The back-end processors store the parallel variables and execute the parallel portions of the program. Each processing element in the back end has its own local memory.There isa single flow of control;at any one time either the front-end processor is executing a sequential operation, or the back-end processors are executing a parallel operation.

![](images/2b2f3724b508834d1f7adfe573b35dfade2eee8088ebbd081a8eac4ccabc2811.jpg)  
FIGURE 4-6 $\complement ^ { \star }$ programmer's model of paralel computation.

The back-end processor array is adaptable-that is, programmers can select the size and shape of the processing elements they want to activate. These parameters are independent of the size and topology of the underlying physical machine. For this reason we sometimes refer to processing elements as virtual processors.Furthermore,the configuration of the back-end processor array is adaptable between different points in the same program.

# 4.3.2 Language Features

$\mathbf { C } ^ { * }$ introduces the notion of a shape, which specifies the way in which parallel data are organized. By declaring a variable to be of some shape type,programmers indicate that they want the ability to perform parallel operations on that variable. For example,the variable declaration

sets up a template for parallel data. The subsequent declaration

real:foo a, b, c;

specifies that variablesa,band $\subset$ are $1 2 8 \times 1 2 8$ arrays upon which parallel operations can be performed.

Parallel operations usually occur within the context of a with statement. The with statement activates the positions of a shape, setting up a context in which variables of that type can be manipulated in parallel.

For example, given the previous two declarations, the statement

with (foo) $\{ \textsf { a } = \ln + \textsf { c } ; \}$

performs.an element-wise addition on each component of $^ \mathrm { b }$ and $\subset$ and stores the resulting values in the corresponding components of $a$

C\* has a set of built-in reduction operators that reduce parallel values into sequential values.For example, the following $\mathbf { C } ^ { * }$ segment computes the sum of all 16,384 values of $a$ and stores it in sequential variable sum:

main({ real sum; with (foo) $\{ \ s u m = \ ( \mathtt { + } = \mathtt { a } ) \ ; \ \}$

The where statement gives $\mathbf { C } ^ { * }$ programmers the ability to perform operations on a subset of the elements of a parallel variable.

For example, execution of the statements with(foo){ where( $a > 0 . 0$ ） $a = b + c$

results in the evaluation of the sum $\mathrm { ~ b ~ } + \mathrm { ~ c ~ }$ and the assignment of the resulting value to $a$ only at those positions in the shape where the value of $\ a$ is greater than zero.

Sometimes the value of each element of a parallel variable depends upon its relative location within the shape. The function pcoord,passed a dimension number, returns each element of a parallel variable to its position within that dimension of the shape. Figure 4-7 illustrates the workings of function pcoord.

![](images/958835e165d22cdd3b353e6b9e85d308712d5c92a092e1c231b5b6951241b4db.jpg)  
FIGURE 4-7 Function pcoord, passed a dimension number,returns to each element ofa parallel variable its position within that dimension of the shape. In this example the shape has dimension [2][3].

As we have seen, the with statement selects the current shape. If an operation is to be performed on certain elements of a parallel variable, the where statement can be used to “set the context.”

For example, given the following $\mathbf { C } ^ { * }$ declarations:

shape [65536]students;   
float:students credits， grade_points, gpa;   
int:students count;   
float upper-gpa, lower-gpa;

the code segment

with (students){ where (credits $> = 6 4 . 0$ ）{ gpa $=$ grade-points / credits; count $= 1$ ； upper-gpa $=$ ( $+ =$ gpa)/ ( $+ =$ count); }

computes the mean grade-point average of upper-division students (those who have at least 64 credits).

Nesting where statements conditionally shrinks the set of active positions.

The where statement has an else clause, which is analogous to the else clause of the C if statement. The meaning of the else clause is: “Perform the following operations on positions that were made inactive by the where condition" (Thinking Machines Corporation 1991). For example, given the previous declarations, the following code segment would compute the mean grade point average of both lower-division and upper-division students:

with (students){ where (credits $> 0 , 0$ ）{ count $= 1$ gpa $=$ grade-points / credits; where (credits $> = 6 4 . 0$ ） upper-gpa $=$ ( $+ =$ gpa)/ ( $+ =$ count) ; else lower-gpa $=$ $+ =$ gpa)/ ( $+ =$ count);

Note the use of nested where statements. The outer where statement excludes students with zero credit hours, to prevent divide-by-zero errors. The inner where statement divides the students with credit hours into two groups; those with at least 64 hours,and those with fewer than 64 hours.

Figure 4-8 illustrates how to implement our numerical integration program in $\mathbf { C } ^ { * }$ The program iswritten fora Connection Machine with 8192 processing elements. In line 1 we define INTERVALS so that the number of rectangles is a multiple of the number of processing elements. The $\mathbf { C } ^ { * }$ programmer thinks in terms of virtual processors, because the total number of elements in a shape can exceed the number of processing elements in the target machine. The compiler and operating system take care of virtual processor emulation.

In line 2 we declare a one-dimensional shape that corresponds to the set of subintervals into which we have divided the line segment [O,1]. In lines 4 and 5 we declare two scalar double-precision variables.Line 6is is the start of the with statement,which puts us ina parallel context.We declare a double precision variable $_ \mathrm { x }$ of shape type span in line 7. There is one value of $_ \mathrm { x }$ for each element of the shape. In line 8 we compute the midpoint of each rectangle on the $x$ axis. Note the use of function pcoord, which returns a unique value in the range $0 \dots 1 3 1 0 7 1$ to each of the elements of $_ \mathrm { x }$ In line 9 we compute the height of the function curve at each of the midpoints,add these heights, and store the result in scalar variable sum. We multiply the total height by the rectangles’ width in line 11 to determine the total area, and print the result in line 12.

FIGURE 4-8 Picomputationprogramwritten in $\complement ^ { \star }$ ,Version6.0.The program iswritten fora Connection Machine with 8192 processing elements.The line numbersare for reference purposes only; they are not part of the program.

1. #define INTERVALS ( $8 1 9 2 \AA ^ { + } 1 6$ )   
2. shape [INTERVALS] span;   
3.main(){   
4. double sum; /\* Sum of areas \*/   
5. doublewidth $^ { - 1 }$ .0/INTERvALS;/\* Width of rectangle \*/   
6。 with(span) (   
7. double: span x; /\* Midpoint of rectangle \*/   
/\* on xaxis \*/   
8. $\times =$ (pcoord(0)+0.5)\*width;   
9。 S $\displaystyle \mathrm {  ~ \ t u m ~ } = \mathrm {  ~ \left( ~ + = ~ \left( ~ 4 ~ . ~ 0 / ~ ( 1 ~ . 0 + x ^ { \star } x ) ~ \right) ~ \right) ~ }$ ；   
10. }   
11. sum $\star _ { = }$ width;   
12. printf ("Estimation of pi is %14.12f\n"，sum);   
13.}

# 4.4 SEQUENT C

# 4.4.1 Paraliel Programming Under DYNIXt

Sequent computers run the $\mathrm { D Y N I X ^ { \mathrm { T M } } }$ operating system, a version of UNIXTM tailored for the multiprocessor environment. In addition to the operating-system calls typically found in a UNIX system,DYNIX provides a set of routines to facilitate parallel processing. The commercial parallel programming languages the Sequent hardware uses are simple extensions of sequential languages that allow programmers to declare shared variables that interact via mutual exclusion and barrier synchronization. The resulting languages are primitive. In this section we describe parallel programming from the perspective of Sequent C programmers. The primary source for this information is Osterhaug (1986).

Shared Data Parallel processes on the Sequent coordinate their activities byaccessing shared data structures. The keyword, shared, placed before a global variable declaration, indicates that all processes are to share a single instance of that variable.For example,if a 1O-element global array is declared int a[1O], then every active process has its own copy of the array; if one process modifies a value in its copy of a, no other process's value will change. On the other hand, if the array is declared shared int a[1O],then all active processes share a single instance of the array,and changes made by one process can be detected by the other processes.

Parallel Processing FunctionsThe standard parallel programming model on the Sequent is straightforward and intuitive. A program begins execution as a single process. This process is responsible for executing those parts of the program that are inherently sequential. When control reaches a part of the computation that may be performed in parallel, the original process forks a number of other processes, each process performing its share of the work. The total number of processes accessng shared data cannot exceed the number of physical processors less one. Because there are at least as many CPUs as active processes, each process may execute on its own CPU. This allows a major reduction in the execution time, assuming that the computer is not executing any other jobs. When control reaches an inherently sequential portion of the computation,onlythe original process executes the code;theremining processes wait until control reaches another portion of the computation that can be divided into pieces and executed concurrently. The program cycles through these two modes until termination (Fig. 4-9).

Parallel programs executing on the Sequent alternate between sequential and parallel execution. The transition from parallel to sequential execution is always delimited bya barrier synchronization. In addition, data dependencies may require the insertion of barrier synchronizations within parallel code, No process may proceed beyond a barrier synchronization point until every process has reached the barrier.

![](images/f5b01623024d8863d498b3c8fb588128248b47b5c52ac16aee8c5b78c2cd9a50.jpg)  
FIGURE 4-9 Sequent C programs alternate betweena single thread of execution and multiple threads of execution. (Courtesy Hatcher and Quinn[1991].）

The existence of a shared memory means that all process interactions can be performed through variables accessible to all the processes. For example, if a group of processes are working together to solve a large problem divided into numerous subproblems, the processes can share a variable that stores the index of the next unsolved subproblem.

Sequent's microtasking library has seven key functions:

m_set_procs $( p )$ : By calling m_set_procs with argument $p$ ,the parent process initializes to value $p$ a shared variable that controls the number of processes created by a subsequent call to m_fork.The value of $p$ cannot exceed the number of physical processors in the system minus one. The function also initializes barriers and locks.

m_fork(name $i , a x g , \ldots I )$ : The parent process creates a number of child processes, then the parent process and the child processes begin executing function name with the arguments (if any) also specified by the call to m_fork. After all the processes (the parent and all the children) have completed execution of function name, the parent process resumes execution with the code after $\scriptstyle { \mathrm { ~ m } } _ { - } { \mathrm { f } } \circ x { \mathrm { k } }$ ,while the child processes busy wait until the next call to m_f ork. Therefore, the first call to m_fork is more expensive than subsequent calls, because only the first call entails process creation.

m-get_myid: A process calls function m_get_myid to get its unique process number. If the total number of active processes is $p$ , then the process number of the parent is O, while the process numbers of the child processes range from 1 to $p - 1$

m_get_numprocs: Function m-get_numprocs returns the number of processes executing in parallel. Given the total number of processes and its own process number, a process can determine which portion of a computation is its responsibility.

m_lock, m_unlock: Functions m_lock and m_unlock ensure mutually exclusive execution of the code that the two calls surround. Once a process has entered a block of code delimited by m_lock and m_unlock, no other process mayenter until the first process has left.

m_kill_procs: Function m_kill_procs kills the child processes created by the first call to m_fork.

# 4.4.2 Monitors

Most parallel algorithms implemented on multiprocessors require a process to performa series of operations on a shared data structure,as if it were an atomic operation. For example, a process may need to fetch the value at the beginning of a linked list and advance the list pointer to the next list element. When the hardware cannot perform the entire series of operations as an atomic operation, the process must have some way to enforce mutual exclusion, keeping all other processes from referencing the resource while it is being modified. The piece of code in which mutual exclusion must be enforced is called a critical section.

Unfortunately, it is easy to miss critical sections, unless you think of the shared resource in a systematic way. One way to structure accesses to shared resources is by using a monitor. A monitor consists of variables representing the state of some resource, procedures that implement operations on that resource,and initialization code. The values of the variables are initialized before any procedure in the monitor is called; these values are retained between procedure invocations and may be accessed only by procedures in the monitor. Monitor procedures resemble ordinary procedures in the programming language with one significant exception. The execution of the procedures in the same monitor is guaranteed to be mutually exclusive. Hence monitors are a structured way of implementing mutual exclusion.

Programming languages that support monitors include Concurrent Pascal (Brinch Hansen 1975,1977) and Modula (Wirth 1977a,1977b,1977c).Even if your parallel programming language does not support monitors, you can implement one yourself. For example, in the Sequent C language, you can implement a monitor by declaring a shared lock variable for each resource,putting an s_lock statement that accesses the variable at the start of each procedure, and putting an s_unlock statement at the end of each procedure (Fig. 4-10). You also must have enough self-discipline to use only these procedures to access the shared resource.

# 4.4.3 Sample Programt

We present a sample program writen in Sequent C. The program computes an approximation to $\pi$ by using numerical integration to find the area under the curve $4 / ( 1 + x ^ { 2 } )$ between 0 and 1 (Fig. 4-11).

/\* stack.h file included by modules calling stack functions \*/ void stack_init(); /\* Initialize stack \*/ int stack_empty();/\* Returns TRUE if stack is empty \*/ void push() ; /\* Pushes integer onto stack \*/ int pop(); /\* Pops integer from stack \*/

/\* stack.c file implementing the monitor \*/   
shared slock_t stack_lock;   
shared int top-of_stack,stack[MAX_STACK_SIZE];   
void stack_init() { s_init_lock (&stack_lock); top-of_stack $= - 1$   
int stack.empty() { int result; s_lock(&stack_lock); result $=$ (top_of_stack $< . 0$ ）； s-unlock(&stack_lock); return result;   
void push (i) inti; s_lock(&stack_lock); stack[++top_of_stack] $= \dot { \textrm { 1 } }$ ； s_unlock(&stack_lock);   
int pop (){ int result; s_lock(&stack_lock); result $=$ stack[top_of_stack- -]; s.unlock(&stack_lock); return result;   
#include $<$ stdio.h>   
#include $<$ parallel/microtask.h>   
#include $<$ parallel/parallel.h>   
shared double pi; /\* Approximation to pi \*/   
main (argc,argv) int argc; char \*argv[]; void computepi() ; int intervals;  /\* Number of intervals \*/ int numprocs; /\* Number of processes to be forked \*/ numprocs $=$ atoi (argv[1]); intervals $=$ atoi (argv[2]); m_set_procs (numprocs); $\mathrm { \sf p } \dot { \mathrm { 1 } } = 0 . 0$ m_fork (computepi, numprocs,intervals); printf ("Estimation of pi is %14.12f.\n", pi); m_kill_procs (); return 0;   
void computepi (numprocs， intervals) int numprocs,intervals; int id; /\* Index of this process \*/ inti; double localsum, width, x; id $=$ m-get.myid (); localsum $= 0 . 0$ ； width $= 1$ .0/intervals; for( $\mathrm { \perp = i d }$ $\mathrm { ~ i ~ } <$ intervals; i $+ =$ numprocs) { $\mathbf { x } = \mathbf { \left( \thinspace i + 0 \cdot 5 \right) }$ \*width; localsum $\mathbf { \Phi } + = \mathbf { \Phi } \left( 4 \mathbf { \Phi } . 0 / \left( 1 \mathbf { \Phi } . 0 + \mathbf { X } ^ { \star } \mathbf { X } \right) \mathbf { \Phi } \right)$ localsum $\star _ { = }$ width; m_lock (); pi $+ =$ localsum; m_unlock ();   
）

The program begins with directives to the compiler to include standard header files. The header files stored in microtask.h and parallel.h contain information on the parallel library functions.

The double-precision floating-point variable pi willcontain the approximation to $\pi _ { \bullet }$ Since all processes will need access to $\mathrm { \ p i }$ in order to store their subtotals, pi is declared resident in shared memory.

The main procedure parses the command line, cals m_set_procs to set the program’s level of parallelism, initializes pi,and calls m_fork to initiate the parallel computation of pi. After all processes have finished executing function Comput epi, the parent process prints the current value of variable pi, kils the child processes,and terminates.

In function computepi, every process cals function m-get_myid to find its unique identifying number in the range O...numprocs. By setting the initial value of the loop index i to id and making the loop increment value numprocs, the processes as a whole cover every value of $\dot { \ I }$ in the range 0...intervals-1 exactly once.

Once every process has computed its share of the sum, it must add its subtotal to pi. Because the statement pi $+ =$ local sum is not an atomic operation, the processes must mutually exclude each other when executing it. They create the necessary critical section through the calls to functions m_lock and m_unlock.

# 4.5 nCUBE Ct

# 4.5.1 The Run-Time Model

An nCUBE programmer usually writes a single program that executes on every node processor. Each node program begins execution as soon as the operating system loads it into the node. To implement a data-parallel application, the programmer assigns each processor responsibility for storing and manipulating its share of the data structure. This is called programming in the SPMD (Single Program,Multiple Data) style (Karp 1987).Processors work on their own local data until they reach a point in the computation when they need to interact with other processors to: swap data items,communicate results,perform a combining operation on partial results, etc. If a processor initiates a communication with a partner that has not finished its own computation, then the initiator must wait for its partner to catch up. Once the processors have performed the necessary communications, they can resume work on local data. One way to view the entire computation is to consider the activities of the processors, as they cycle between computing and communicating，with occasional periods of waiting (Fig. 4-12).

A SPMD program executing on a multicomputer such as the nCUBE consists of alternating segments in which processors work independently on local data, then exchange values with other processors through calls to communication routines. In Fig. 4-12 black represents computing, white represents waiting, and gray represents communicating.

![](images/08e21eaaffc889e6fd72d972b61b02ab546e6d79d78f9af95c3b3e95baf0d857.jpg)  
FIGURE 4-12 This figure gives an abstract view of the nCUBE C run-time model. Every processor begins executionas soonas the executable is loaded into itsmemory.Black represents time spent computing，white represents time spent waiting fora message,and gray represents time spent communicating with other processors. (Courtesy Hatcher and Quinn 1991.)

# 4.5.2 Extensions to the C Language

The C programs running on the nodes are inherently parallel, in the sense that every node is active from the time its program is loaded. For this reason there is no need for a process creation mechanism in nCUBE C. In fact, three new functions are sufficient for us to run our sample application on the nCUBE:

whoami: Returns information about the node process, including the dimension of the allocated hypercube and the position of the node in the allocated hypercube.

nwrite: Sends a message to another node. Arguments to this function include the destination node number,the address of the message to be sent, the length of the message, and the message type,an integer. Function nwrite is nonblocking.

nread: Receives a message from another node. Arguments to this function include the source node number, the message type,the address where the message is to be stored,and the maximum number of bytes to be read. The value returned from the function is the number of bytes actually read. The user has the option of specifying that the message to be read can be of any type or from any source, or both. Function nread blocks until a message fiting the source and type criteria has been read.

# 4.5.3 Sample Program

An nCUBE C program to perform the π computation appears in two parts (see Figs.4-13 and 4-14).Look at the code in Fig.4-13. The two “include” files allow the node program to callfunctions from the C I/O library. All messages sent by the fan-in function are of type FANIN.

/\* Node program \*/   
#include $<$ special.h>   
#include $<$ stdio.h>   
#include   
#include   
main (argc,argv) int argc; char \*argv[];   
[ void fan_in(); int cube_dim; /\* Dimension of allocated hypercube \* inti; int intervals; /\* Number of intervals \*/ int nodenum; /\* Position of node in \*/ /\* allocated hypercube \*/ int not_used; /\* Place holder $^ \star /$ int num_procs; /\* Number of active processors \*/ double sum; /\* Sum of areas \*/ double width; /\* Width of interval \*/ double x; /\* Midpoint of rectangle on x axis \*/ /\* argv[0] is name of file containing host program \*/ /\* argv[1] is name of file containing node program \*/ /\* argv[2] is dimensional of allocated hypercube \*/ /\* argv[3] is number of intervals \*/ intervals $=$ atoi(argv[3]); width=1.0/intervals; whoami (&nodenum，&not_used，&not_used，&cube_dim); num_procs $\mathit { \Theta } = \mathit { \Theta } \exists \ < \mathit { \Theta } <$ cube_dim; sum $= 0 . 0$ ； for ( $\dot { \textrm { 2 } } =$ nodenum; $\mathrm { ~ i ~ } <$ intervals; i+=num-procs) { $\mathbf { x } = \left( \mathrm {  ~ i ~ } + 0 . 5 \right)$ \*width; sum $+ =$ width\*( $\left( 4 \cdot 0 / \left( 1 . 0 \star \mathbf { x } ^ { \star } \mathbf { x } \right) \right)$ ； fan_in (&sum,nodenum, cube_dim); if (!nodenum) printf ("Estimation of pi is %14.12f\n",sum); CUIDO anuta $\pi$ ueing numarical intearation

void fan_in (value,nodenum,cube_dim) double \*value;int nodenum,cube_dim; int dest，i,source,type; double tmp; type $=$ FANIN; for( $\mathrm { ~ i ~ } =$ cube_dim-1; $\mathrm { \dot { \perp } } > = 0$ ;i--) if (nodenum $<$ ( $\mathrm { ~ 1 ~ \ll ~ i ~ }$ ）{ source $=$ nodenum $\hat { }$ ( $1 \ll \mathrm { i }$ ）； nread (&tmp，sizeof(double)，&source,&type); \*value $+ =$ tmp; }else if (nodenum $<$ ( $\uparrow \ll \mathrm { i }$ (i+1))){ dest $=$ nodenum $\hat { }$ ( $\underline { { 1 } } \ll \dot { \perp }$ ）； nwrite (value,sizeof(double)，dest,type);

IGURE 4-14 nCuBE C source code for function fan_in, which accumulates each node's subtotal into a sum stored on node 0.

Each node processor executes the function main. Every processor has its own local copy of each of the variables declared inside main.

The nodes will estimate $\pi$ by approximating the area under the curve $4 / ( 1 +$ $x ^ { 2 } )$ between O and 1 with intervals rectangles.

The node process calls function whoami to determine the dimension of the allocated hypercube, as well as its position in the allocated hypercube. The number of processors is 2 raised to the power of the cube dimension.

Once a processor has computed the sum of the areas of its share of the rectangles,it participates in calling function fan_in. After completion of function fan_in, processor O has the total value, which it prints.

Function fan_in is shown separately in Fig. 4-14. Passed the address of a double-precision floating-point value, the node number, and the cube dimension,function fan_in computes the sum of every processor's value at that address,using a binomial tree communication pattern (Fig. 4-15). Initially all the processors are active. During each iteration the algorithm divides the active processors into two sets of equal size. The processors in the upper half send their values to the processors in the lower half. The processors in the lower half add the two values, while the processors in the upper half become inactive.If a processor is sending a value, variable dest contains the number of the processor receiving the value; if a processor is receiving a value, variable source contains the number of the processor sending the value. After one iteration per cube dimension, processor O is the only remaining active processor, and it contains the global sum in variable value. Other processors will have either the original value or a partial sum.

![](images/7366bdbcae698a79e3749f252d0cf01602d3060dd1f73f8c7ad23c98a382008f.jpg)  
FIGURE 4-15 Function fan_in in Fig. 4-14 computes the sum of values stored on the hypercube nodesusing thecommunicationpatternshownbythearrows.Together,thearrowsform a binomial tree.

# 4.6 OCCAM

Inmos Limited of Great Britain developed occam as a programming Ianguage for its Transputer series of processors. The design of occam was heavily influenced by the work done by Hoare on communicating sequential processes (Hoare 1978). Because the occam language has been closely associated with the evolution of the Transputer chip, it has improved as the hardware of successive Transputers has become more sophisticated. For example, the original occam language did not use floating-point data, because the T414 processor did not support it. This feature was added to the language with the introduction of the T8oo processor, which used floating-point hardware.

# 4.6.1 Programmer's Model

At the macro level the occam programmer views a parallel computation as a collection of asynchronously executing processes communicating via a synchronous message-passing protocol. An occam program is built from three kinds of primitive process: assignment, input,and output. The programmer can assemble more complicated processes by specifiying when they must execute sequentially and when they can execute in parallel.

Figure 4-16 represents the structure of a hypothetical occam program. At the global level the program is one occam process, indicated by the ellipse E around the graph. In this example, the process has six subprocesses that must execute sequentially. (Control dependencies are shown with dashed arrows.) All but the fourth process are primitive processes,indicated by small circles. The fourth process is a built-up process, as indicated by ellipse D. Built-up processes can represent either a sequential or a parallel collection of simpler processes. The primitive process represented by a filled gray circle is an input process

inside a sequential collection of processes (A) inside a parallel collection of processes (B) inside a sequential collection of processes (C) inside a parallel collection of processes (D) inside a sequential collection of processes (E).

![](images/a7dffaac13995b6645d0f57d842247141c0edf1cb275b11e73e7eec9e4fa7774.jpg)  
FIGURE 4-16 The occam programmer'smodel of parallel computation. Primitive processes appear ascircles.Ellipses indicate processes builtupas sequential or parallel collectionsof processes.Control dependencies are shownas dashed arrows.Communications appear as bold arrows between primitive processes.

The assignment process, one of the three primitive processes in an occam program, assigns the value of an expression to a variable. An input process assigns to a variable the value read from a channel. An output process evaluates an expression and writes the result to a channel.

A channel is a one-way, point-to-point, synchronous link from one process to another process. An occam channel is a logical entity independent of the underlying hardware.

# 4.6.2 Language Constructs

In this section we describe features of the occam language that are used in the sample program.

The assignment process allows the value of an expression with, at most, one operator assigned to a variable. For example,

assigns to variable sum the sum of the values of variables partial1 and partial2.

The input process reads a value from a channel and assigns that value to a variable. For example,

channel1 ? partial1

assigns to variable part ial1 the value input from channel channel1.

The output process writes a value to a channel. For example,

channel3 ！ sum

outputs value of sum to channel channe13.

All communication in occam is synchronous. A process performing output on a channel does not complete until the process performing input on the same channel executes.

The SEQ (pronounced “seek") construction specifies that a number of processes should execute sequentially. In the following piece of code, integers are input from two different channels,added,and the sum output toa third channel:

SEQ channel1 ? partial1 channel2 ? partial2 sum : $=$ partial1 $^ +$ partial2 channel3 ! sum

In occam, indentation indicates which processes are part of the SEQ. The indentation must be exactly two characters. A SEQ construction terminates when the final process in the sequence terminates.

The PAR construction specifies that a number of processes may execute in parallel. The following piece of code performs the same task as the previous example, but allows the two inputs to occur simultaneously:

SEQ PAR channel1 ? partial1 channel2 ? partial2 sum : $=$ partial1 $^ +$ partial2

A PAR construction terminates when its last constituent process terminates.

The IF construct allows the conditional execution of processes. A boolean control expression precedes each process that may be executed. The control expressions are evaluated from top to bottom. The process associated with the first condition that evaluates to true is executed.

The following IF construct guarantees that variable $a$ has a value in the range of O through 1O. If the value of a is already inside that range, no work needs to be done (indicated by the SKIP process).

IF $\begin{array} { c } { { \tt a > 1 0 } } \\ { { { \tt a : \tt a \tt 1 0 } } } \\ { { { \tt a < 0 } } } \\ { { { \tt a : \tt a \tt 0 } } } \end{array}$ TRUE SKIP

ALT, the alternation construct, allows control to flow to the first alternative the system finds to be true. In an ALT the conditions of an alternation may depend upon input. A blocked input process in one condition of the alternation will not prevent a later condition from being evaluated.

Consider this ALT construct:

ALT temperature.channel ?value IF value $>$ high.value high.value : $=$ value TRUE SKIP enable report.channel ? check SEQ result.channel !high.value high.value : $= - 1 0 0$

If the alternation process gets the next value from the input channel temperature.channel, then it checks to see if the input value is a new high value,and if so, the value is recorded. If the process first gets a value from the input channel report .channel, then the process outputs its recorded high value to result .channel. However, input from report .channel is ignored if the boolean variable enable is false.

The replicator construct allows the constructs SEQ， PAR， IF, and ALT to execute some number of times. For example, the construct

PAR i = [0 FOR 10]

creates 10 replicated parallel processes, each with a unique value of i in the range from O through 9.

The remaining features of occam used in the sample program are intuitive. We will explain them as we describe the sample code.

1.DEF $\mathtt { N } = \mathtt { 4 } 0 0 0 0 0$ ： 2. DEF PROCESSES $= 8$ ： 3.DEF CHUNK $= \mathrm { { N } }$ / PROCESSES : 4. CHAN sum[PROCESSES] : 5.PAR‘ 6. PAR $\mathrm { ~ i ~ } = \mathrm { ~ [ ~ 0 ~ }$ FOR PROCESSES] 7. REAL6 $4 \times$ , localsum,width : 8. SEQ 9. localsum : $= 0 . 0$   
10. width $: = \mathrm { ~ 1 ~ . ~ 0 ~ ~ / ~ N ~ }$   
11. X: $=$ ((i \* CHUNK) $+ ~ 0 . 5$ ） $\star$ width   
12. SEQ $\dot { \perp } =$ [0 FOR CHUNK]   
13. SEQ   
14. localsum : $=$ localsum $^ +$ (4.0/(1.0+(x\*x)))   
15. $\textbf { x } : = \textbf { x } +$ width   
16. localsum : $=$ localsum \* width   
17. sum[i] ! localsum   
18. REAL64 pi :   
19. INT gOt [PROCESSES] :   
20. SEQ   
21. pi : $= 0 . 0$   
22。 SEQ $\begin{array} { r l } { \dot { \mathrm { ~ \textbar { ~ } ~ } } = } & { { } [ 0 } \end{array}$ FOR PROCESSES]   
23. got[i] : $=$ FALSE   
24. SEQ $\mathrm { ~ i ~ } = \mathrm { ~ [ ~ 0 ~ }$ FOR PROCESSES]   
25. REAL64 y :   
26. SEQ   
27. ALT $\dot { \mathrm { ~ \scriptsize ~ i ~ } } =$ [0 FOR PROCESSES]   
28. (got[i] $=$ FALSE) & sum[i] ? Y   
29. got[i]: $=$ TRUE   
30. pi: $\mathbf { \Sigma } = \mathbf { p } \mathbf { i } \mathbf { \Sigma } + \mathbf { y }$   
31. output ! "Approximation to pi is "; pi

The occam program in Fig. 4-17 computes $\pi$ using the numerical integration method already described. Lines 1-3 define constants. N is the number of intervals, PROCESSES is the number of processes we will create, and CHUNK is the number of intervals per process. (For the program to execute correctly, N must be a multiple of PRoCESSEs.) In line 4 we define one channel per process. The process will use this channel to output its partial sum to the process that is finding the grand total.

Lines 5-31 constitute a parallel construct with PROCESSES+1 processes. All but one of the processes execute lines 6-17. Each process computes the sum of the areas of its share of rectangles. The last process executes lines 18-31 where it collects the output of the sum-finding processes, computes the grand total, and prints the result.

![](images/23a844f603cc25c9a52e29d9bc1e07bc2decba45725e1096f42a1f6b80c4623a.jpg)  
IGURE 4-18 The Linda programmer's model of parallel computation.

# 4.7 C-LINDA

Linda consists of several operations that work on tuple space, a shared associative memory. Incorporating Linda operations into a sequential base language yields a parallel programming language. For example, in C-Linda, Linda primitives have been added to C. In this section we describe the Linda programming model and present two C-Linda programs to solve the numerical integration problem.

# 4.7.1 Programmer's Model

Linda is a MIMD model of parallel computation. The Linda programmer envisions an asynchronously executing group of processes that interact by means of a associative shared memory, tuple space.Tuple space consists of a collection of logical tuples. Parallelism is achieved by creating process tuples,which are evaluated by processors needing work. Parallel processes interact by sharing data tuples. After a process tuple has finished execution, it returns to tuple space as a data tuple.

In many MIMD languages, such as occam, processes may interact with each other in complicated ways (see Fig. 4-16). Proponents of Linda say that forcing all process interactions to occur through tuple space simplifies parallel programming.

# 4.7.2 C-Linda Language Constructs

Six functions enable a process to interact with tuple space. Function out, passed tuple t as an argument, causes t to be added to tuple space. The process executing the out operation continues immediately.