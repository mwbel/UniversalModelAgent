Chapter 5

# Direct Methods for Sparse Problems

A sparse matrix is any matrix with enough zeros that it pays to take advantage of them.

—J. H. Wilkinson

# 5.1 - Tools for Sparse Matrix Computations

# 5.1.1 - Introduction

A band matrix,whose nonzero elements are concentrated near the main diagonal, is a simple example of a sparse matrix.Methods for solving band least squares problems have been treated in Section 4.1. A significant part of large-scale scientific computing applications involves sparse matrices with more irregular sparsity paterns. By only storing and operating on nonzero elements in sparse matrices,large savings in computing time and memory can be achieved and can make otherwise intractable problems practical to solve.Examples include the fields of structural analysis,geodetic surveying, management science,and power systems analysis. This chapter treats effective direct methods for the solution of sparse least squares problems using Cholesky and QR factorizations. As the computation proceeds,one must try to minimize fill,which is the term used to denote the creation of new nonzero elements within sparse factors of the sparse matrix.

We initially assume that $A \in \mathbb { R } ^ { m \times n }$ has full column rank, although problems where rank $( A )$ $\mathbf { \mu } = m < n$ or $\operatorname { r a n k } ( A ) < \operatorname* { m i n } ( m , n )$ do occur in practice.Other issues,such as dimension, sparsity structure,and conditioning,should be considered when choosing the method to be used. Occurrence of weighted rows,the number of right-hand sides,and constraints on the solution must also be considered. If only part of the solution vector $x$ is needed, savings can be achieved. It may also be possible to take advantage of a sparse right-hand side $b$

An example of a symmetric irregular pattern arising from a structural problem in aerospace is illustrated in Figure 5.1.1. Other application areas can give patterns with quite diferent characteristics.

Solving a sparse least squares problem $\operatorname* { m i n } \| A x - b \| _ { 2 }$ of full column rank using the method of normal equations is usually performed in several steps as follows.

1. A symbolic phase in which a column permutation $P _ { c }$ is determined that approximately minimizes the number of nonzeros elements in the Cholesky factor $R$ of $( A P _ { c } ) ^ { T } ( A P _ { c } )$

![](../chunks/Numerical Methods for Least Squares Problems (Åke Björck) (z-library.sk, 1lib.sk, z-lib.sk_part_0004_pages_0211-0280/auto/images/5af3228f08edad849f19dc8b4f70608f4763c5c7f14a6e8a3caa0d61df185b98.jpg)  
Figure 5.1.1. Nonzero patern of a matrix arising from a structural problem and its Cholesky factor.

This step only works on the nonzero structure of $A$ and also generates a storage structre for $R$

2. A numerical phase in which $C = ( A P _ { c } ) ^ { T } ( A P _ { c } )$ is formed numerically and its Cholesky factor $R$ is computed and stored in the data structure generated in the symbolic phase.

3.For the given right-hand side $b$ form $c = P _ { c } ^ { T } A ^ { T } b$ solve $R ^ { T } z = c$ $R y \ : = \ : z$ and set $x = P _ { c } y$

Sparse QR factorization can give substantial improvements in accuracy compared to Cholesky factorization.As the factor $R$ is mathematically the same for both factorizations,the symbolic phase from the Cholesky factorization can be used. However,as for band least squares problems, the intermediate filland arithmetic cost for QR depend strongly on the row ordering.

There are several collections of sparse matrices arising from a wide range of applications that are used for development, testing,and performance evaluation for sparse matrix computations. One of the first was the Harwell-Boeing collection by Duff, Grimes,and Lewis [346,1989]. This was followed by the Matrix Market collection by Boisvert et al.[160,1997l, which has now been incorporated into the larger SuiteSparse collection by Davis and Hu [291, 2o11]. Whereas the largest matrix in Matrix Market has dimension 90,449 with 2.5 million nonzeros,the largest in the SuiteSparse collection has dimension 28 million with 76O million nonzeros!

# Notes and references

The literature on sparse matrix algorithms is extensive. George and Liu [457,1981] is an early classical text on sparse Cholesky factorization. Graph theory and its connections to sparse matrix computations are treated in George, Gilbert, and Liu [454,1993]. An excelent survey of the state of the art of direct methods for sparse linear systems is given by Davis [289,2oo6]; see also Davis,Rajamanickam,and Sid-Lakhdar [292,2o16] and Duff, Erisman,and Reid [345,2017]. A recent addition that complements theory with detailed outlines of algorithms and emphasizes the importance of sparse matrix factorizations for constructing preconditioners for iterative least squares methods is Scott and Tüma [991, 2023].

# 5.1.2 - Storage and Operations on Sparse Matrices

The main objective of storage schemes for sparse vectors and matrices is to economize on storage while facilitating subsequent operations.An important distinction is between static storage structures that remain fixed and a dynamic structure that can accommodate fill. A static structure like the general sparse storage scheme can be used when the number and location of the nonzeros in the matrix factors can be predicted. Otherwise,the data structure for the factors must dynamically allocate sufficient space for fill during the elimination.

It is useful to be able to predict fill that will occur in a matrix factorization so that storage structures can be fixed in advance.To do this,one usually appeals to a no-cancellation assumption: when two nonzero numerical quantities are added or subtracted, the result is assumed to be nonzero. The structural rank of a matrix is defined to be the maximum rank of all numerical matrices with the same nonzero pattern. For example, the matrix

$$
\left( \begin{array} { c c c } { { c _ { 1 1 } } } & { { 0 } } & { { c _ { 1 3 } } } \\ { { 0 } } & { { 0 } } & { { 0 } } \\ { { c _ { 3 1 } } } & { { 0 } } & { { c _ { 3 3 } } } \end{array} \right)
$$

has structural rank two, but if $c _ { 1 1 } c _ { 3 3 } - c _ { 1 3 } c _ { 3 1 } = 0$ ,the numerical rank is one.

In the following we denote the number of nonzero elements in a sparse matrix (or vector) by $n n z$ . A sparse vector $x$ can be stored in compressed form as the triple $( x C , i x , n n z )$ . Its $n n z$ nonzero elements are stored in the vector $x C$ . The indices of the elements in $x C$ are stored in the integer vector $_ { i x }$ ,so that

$$
x C _ { k } = x _ { i x ( k ) } , \quad k = 1 , \ldots , n n z .
$$

For example, in compressed form the vector $x = ( 0 , 4 , 0 , 0 , 1 , 0 , 0 , 0 , 6 , 0 )$ is stored as

$$
x C = ( 1 , 4 , 6 ) , \quad i x = ( 5 , 2 , 9 ) , \quad n n z = 3 .
$$

Note that it is not necessary to store the nonzero elements in any particular order in $x C$ This makes it easy to add further nonzero elements in $x$ —they can be appended in the last positions of $x C$ and $_ { i x }$

In the general sparse storage scheme for a sparse matrix $A$ ,nonzero elements are stored in coordinate form $( A C , i x , j x , n n z )$ ,that is,as an unordered one-dimensional array $A C$ with two integer vectors $_ { i x }$ and $j x$ containing the corresponding row and column indices,

$$
A C ( k ) = a _ { i j } , \quad i = i x ( k ) , \quad j = j x ( k ) , \quad k = 1 , \ldots , n n z ,
$$

where $n n z$ is the number of nonzero elements in $A$ ．This scheme is very convenient for the initial representation of a general sparse matrix because additional nonzero elements can be easily added to the structure.A drawback is that it is diffcult to access $A$ by rows or columns, as is usually needed in later operations. Also,the storage overhead is large because two integer vectors of length $n n z$ are required. This overhead can be decreased by using a clever compressed scheme due to Sherman; see George and Liu [457,1981,pp. 139-142].

In compressed storage by rows (CSR) a sparse matrix is stored as the collection of its sparse rows. For each row, the nonzeros are stored in $A C$ in compressed form. The corresponding column subscripts are stored in integer vector $j a$ ,so that the column subscript of element $A C ( k )$ is in $j a ( k )$ ．A third vector $i p$ gives the position in $A C$ of the first element in the ith row of $A$

In CSR the matrix

$$
A = \left( \begin{array} { c c c c c } { a _ { 1 1 } } & { 0 } & { a _ { 1 3 } } & { 0 } & { 0 } \\ { a _ { 2 1 } } & { a _ { 2 2 } } & { 0 } & { a _ { 2 4 } } & { 0 } \\ { 0 } & { 0 } & { a _ { 3 3 } } & { 0 } & { 0 } \\ { 0 } & { a _ { 4 2 } } & { 0 } & { a _ { 4 4 } } & { 0 } \\ { 0 } & { 0 } & { 0 } & { a _ { 5 4 } } & { a _ { 5 5 } } \\ { 0 } & { 0 } & { 0 } & { 0 } & { a _ { 6 5 } } \end{array} \right)
$$

would be stored as

$$
\begin{array} { r l } & { A C = ( a _ { 1 1 } , \ a _ { 1 3 } \ | \ a _ { 2 2 } , \ a _ { 2 1 } \ a _ { 2 4 } \ | \ a _ { 3 3 } \ | \ a _ { 4 2 } , \ a _ { 4 4 } \ | \ a _ { 5 4 } , \ a _ { 5 5 } \ | \ a _ { 6 5 } ) , } \\ & { \ j a = ( 1 , \ 3 , \ 2 , \ 1 , \ 4 , \ 3 , \ 2 , \ 4 , \ 4 , \ 5 , \ 5 ) , } \\ & { \ i p = ( 1 , \ 3 , \ 6 , \ 7 , \ 9 , \ 1 1 ) . } \end{array}
$$

The components in each row need not be ordered. To access a nonzero $a _ { i j }$ there is no direct way to calculate the corresponding index in the vector $A C$ ； some testing is needed on the subscripts in $j a$ . In CSR storage form,a complete row of $A$ can be retrieved efficiently,but elements in a particular column cannot be retrieved without a search of nearly all elements. Alternatively, a similar compressed storage by columns (CsC) form can be used.

For a sparse symmetric matrix it suffices to store either its upper or its lower triangular part, including the main diagonal. If the matrix is positive definite,then allits diagonal elements are positive,and it may be convenient to store them in a separate vector.

For problems in which all the nonzero matrix elements lie along a few subdiagonals the compressed diagonals storage mode is suitable.A matrix $A$ is then stored in two rectangular arrays $A D$ and a vector $l a$ of pointers. The array $A D$ has $n$ rows and nd columns,where $^ { n d }$ is the number of diagonals. $A D$ contains the diagonals of $A$ that have at least one nonzero element, and $l a$ contains the corresponding diagonal numbers. The superdiagonals are padded to length $n$ with $k$ trailing zeros,where $k$ is the diagonal number. The subdiagonals are padded to length $n$ with $| k |$ leading zeros.This storage scheme is particularly useful if the matrices come from a finite element or finite discretization on a tensor product grid. The matrix $A$ in (5.1.1) would be stored as

$$
A D = \left( \begin{array} { c c c c } { { a _ { 1 1 } } } & { { a _ { 1 3 } } } & { { a _ { 2 1 } } } & { { 0 } } \\ { { a _ { 2 2 } } } & { { a _ { 2 4 } } } & { { 0 } } & { { a _ { 4 2 } } } \\ { { a _ { 3 3 } } } & { { 0 } } & { { 0 } } & { { 0 } } \\ { { a _ { 4 4 } } } & { { 0 } } & { { a _ { 5 4 } } } & { { 0 } } \\ { { a _ { 5 5 } } } & { { 0 } } & { { a _ { 6 5 } } } & { { 0 } } \end{array} \right) , \qquad l a = ( 0 \ 2 \ - 1 \ - 2 ) .
$$

Operations on sparse vectors are simplified if one of the vectors is first uncompressed, i.e., stored as a dense vector. This can be done in time proportional to the number of nonzeros,and it allows direct random access to specified elements in the vector. Vector operations, such as adding a multiple of a sparse vector $x$ to an uncompressed sparse vector $y$ or computing an inner product $x ^ { T } y$ ,can then be performed in constant time per nonzero element. For example,assume $x$ is held in compressed form and $y$ in a full-length array. Then the operation $y : = a * x + y$ may be expressed as

$$
\begin{array} { c } { { \mathrm { f o r } k = 1 , \ldots , n n z } } \\ { { i = i x ( k ) ; \quad y ( i ) : = a * x ( k ) + y ( i ) ; } } \end{array}
$$

end

Efficient implementations of sparse matrix-vector products such as $A v$ and $A ^ { T } u$ are important in both direct and iterative methods for sparse linear least squares problems.The storage structure for $A$ should be chosen so that hardware features like vector registers can be exploited.

Some of the more common structures are described below. Let $u \in \mathbb { R } ^ { m }$ and $v \in \mathbb { R } ^ { n }$ be uncom-pressed vectors,and let $A$ be stored in CSR mode. Then the matrix-vector product $u = A v$ can be implemented as

$$
\begin{array} { r c l } { { } } & { { } } & { { \mathrm { y r } i = 1 : m , } } \\ { { } } & { { } } & { { u ( i ) = 0 ; } } \\ { { } } & { { } } & { { \mathrm { f o r } k = i p ( i ) : i p ( i + 1 ) - 1 , } } \\ { { } } & { { } } & { { u ( i ) = u ( i ) + A C ( k ) * v ( j a ( k ) ) ; } } \end{array}
$$

For the product $v = A ^ { T } u$ a similar code would access the elements of $A$ column by column, which is very inefficient. The product is better performed as

$$
\begin{array} { r l } & { v ( 1 : n ) = 0 ; } \\ & { \mathrm { f o r } i = 1 : m } \\ & { \quad \mathrm { f o r } k = i p ( i ) : i p ( i + 1 ) - 1 , } \\ & { \quad \quad j = j a ( k ) ; \quad v ( j ) = v ( j ) + A C ( k ) \ast u ( i ) ; } \end{array}
$$

A proposal for standard computational kernels (BLAS) aimed at iterative solvers is given by Duff et al. [349,1997]. The interface of the sparse BLAS in the standard from the BLAS technical forum is designed to shield one from concern over specific storage schemes; see Duff, Heroux,and Pozo [347, 2002].

# 5.1.3 - Graphs and Sparse Matrices

A graph $G = ( V , E )$ consists of a set of vertices or nodes $V = \{ v _ { 1 } , \ldots , v _ { n } \}$ and a set of edges $E$ . In an undirected graph an edge is an unordered pair of its vertices $( v _ { i } , v _ { j } )$ . A graph is directed if the edges $( v _ { i } , v _ { j } )$ are directed from $v _ { i }$ to $v _ { j }$ . Two vertices $v _ { i }$ and $v _ { j }$ in a graph $G$ are said to be adjacent if there is an edge $( v _ { i } , v _ { j } ) \in E$ .The edge is incident to the vertices $v _ { i }$ and $v _ { j }$

The nonzero structure of a symmetric matrix $C \in \mathbb { R } ^ { n \times n }$ can be modeled by an undirected adjacency graph $G ( C ) = ( V , E )$ with $n$ vertices $V = \{ 1 , \ldots , n \}$ and edges

$$
E = \{ ( i , j ) \mid c _ { i j } = c _ { j i } \neq 0 , i \neq j \} .
$$

The structure of a square unsymmetric matrix $C$ can be represented by a directed graph $G =$ $( X , E )$ ,where $( v _ { i } , v _ { j } )$ is a directed edge from $v _ { i }$ to $v _ { j }$ if and only if $c _ { i j } \neq 0$

The adjacency set of a vertex $v _ { i }$ in $G$ is defined as

$$
\mathrm { A d j } _ { G } ( v _ { i } ) = \{ v _ { j } \in V \mid v _ { i } \mathrm { a n d } v _ { j } \mathrm { a r e } \mathrm { a d j a c e n t } \} .
$$

The degree of a vertex $v _ { i }$ is the number of vertices adjacent to $v _ { i }$ and is denoted by $| \mathrm { A d j } _ { G } ( v _ { i } ) |$ A graph $\bar { G } = ( \bar { V } , \bar { E } )$ is a subgraph of $G = ( V , E )$ if $\bar { V } \subset V$ and $\bar { E } \subset E$ A walk of length $k$ in an undirected graph is an ordered sequence of $k + 1$ vertices $v _ { 1 } , \ldots , v _ { k + 1 }$ such that

$$
( v _ { i } , v _ { i + 1 } ) \in E , \quad i = 1 , \dots , k .
$$

A walk is a path if all edges are distinct. If $v _ { 1 } = v _ { k + 1 }$ , the walk is closed and called a cycle. Two nodes are said to be connected if there is a path between them. The distance between two vertices in a graph is the number of edges in the shortest path connecting them.A graph is said to be connected if every pair of distinct vertices is connected by a path. A graph that is not connected consists of at least two separate connected subgraphs.If $G = ( X , E )$ is a connected graph, then $Y \subset V$ is called a separator if $G$ becomes disconnected after removal of the nodes $Y$ . A directed graph is strongly connected if there is a path between every pair of distinct nodes along directed edges.

Graphs that do not contain cycles are called acyclic. A connected acyclic graph is called a tree; see Figure 5.1.2. In a tree,any pair of vertices is connected by exactly one path. A tree has at least two vertices of degree 1. Such vertices are called leaf vertices. If a graph $G$ is connected, then a spanning tree is a subgraph of $G$ that is a tree.In a tree an arbitrary vertex $r$ can be specified as the root of the tree. Then the tree becomes a directed rooted tree. An edge $( v _ { i } , v _ { j } ) \in G$ in a directed rooted tree is a directed edge from $v _ { i }$ to $v _ { j }$ if there is a path from $v _ { i }$ to $r$ such that the first edge of this path is from $v _ { i }$ t0 $v _ { j }$ . If there is a directed edge from $v _ { i }$ t0 $v _ { j }$ ， then $v _ { j }$ is called the parent of $v _ { i }$ ,and $v _ { i }$ is said to be a child of $v _ { j }$

A labeling(or ordering) of a graph $G$ with $n$ vertices is a mapping of the integers $\{ 1 , 2 , \ldots , n \}$ onto the vertices of $G$ .The integer $i$ assigned to a vertex is called the label (or number) of that vertex.A labeling of the adjacency graph of a symmetric matrix $C$ corresponds to a particular ordering of its rows and columns. For example, the graph of the structurally symmetric matrix

$$
\left( \begin{array} { l l l l l l } { \times } & { \times } & { } & { \times } & { \times } & { } \\ { \times } & { \times } & { \times } & { } & { } & { } \\ { } & { \times } & { \times } & { } & { } & { \times } & { \times } \\ { \times } & { } & { } & { \times } & { } & { } \\ { \times } & { } & { } & { } & { \times } & { } \\ { } & { } & { \times } & { } & { } & { \times } & { } \\ { } & { } & { \times } & { } & { } & { \times } & { } \\ { } & { } & { } & { } & { } & { \times } & { } \end{array} \right)
$$

is given in Figure 5.1.2.

![](../chunks/Numerical Methods for Least Squares Problems (Åke Björck) (z-library.sk, 1lib.sk, z-lib.sk_part_0004_pages_0211-0280/auto/images/804461651ff765da2ee2acbb913fb71835cfbd8efd901e65a12b612a7a5fa53d.jpg)  
Figure 5.1.2. The labeled graph $G ( C )$ of the matrix in (5.1.2).

The matrix of normal equations can be written as

$$
C = A ^ { T } A = \sum _ { i = 1 } ^ { m } a _ { i } a _ { i } ^ { T } ,
$$

where $a _ { i } ^ { T }$ is the $i$ th row of $A$ . This expresses $A ^ { T } A$ as the sum of $m$ matrices of rank one. By the no-cancellation assumption, the nonzero structure of $A ^ { T } A$ is the direct sum of the nonzero elements of the matrices $a _ { i } a _ { i } ^ { T }$ ， $i = 1 , \ldots , m$ . It follows that the graph $G ( A ^ { T } A )$ is the direct sum of the graphs $G ( a _ { i } a _ { i } ^ { T } )$ ， $i = 1 , \ldots , m$ . That is,its edges are the union of all edges not counting multiple edges. In $G ( a _ { i } a _ { i } ^ { T } )$ all pairs of vertices are connected. Such a graph is called a clique and corresponds to a dense submatrix in $A ^ { T } A$ .Clearly, the structure of $A ^ { T } A$ is not changed by dropping any row of $A$ whose nonzero structure is a subset of another row.

By the no-cancellation assumption,an alternative characterization of $G ( A ^ { T } A )$ is that $( A ^ { T } A ) _ { j k } \ \ne \ 0$ if and only if columns $j$ and $k$ intersect, i.e., if $a _ { i j } \neq 0$ and $a _ { i k } \neq 0$ for at least one row $i \in \{ 1 , \ldots , m \}$ . Therefore, $G ( A ^ { T } A )$ is also known as the column intersection graph of $A$

# 5.1.4- A Graph Model of Cholesky Factorization

The use of graphs to symbolically model the Cholesky factorization of a sparse symmetric matrix $C$ is due to Parter [886,1g61], although the details were later given by Rose [935,1972]. In sparse Cholesky factorization each row of the Cholesky factor $R$ depends on only a subset of the previous rows. The fill in the factorization can be analyzed by recursively forming a sequence of elimination graphs

$$
G _ { 0 } = G ( C ) , \quad G _ { i } ( C ) , \quad i = 1 , \ldots , n - 1 ,
$$

where $G _ { i } ( C )$ is formed from $G _ { i - 1 } ( C )$ by removing vertex $i$ and its incident edges and adding fill edges that make adjacent vertices in $G _ { i - 1 } ( C )$ pairwise adjacent. The sequence of elimination graphs for the matrix in (5.1.2) is pictured in Figure 5.1.3.It can be verified that the number of fill elements (edges) is 10.

![](../chunks/Numerical Methods for Least Squares Problems (Åke Björck) (z-library.sk, 1lib.sk, z-lib.sk_part_0004_pages_0211-0280/auto/images/3acd0062d6ec14b69034a957ca018f6ce4d05d49d85e79bc250f45b107227b3c.jpg)  
Figure 5.1.3. Sequence of elimination graphs of the matrix in (5.1.2).

The filled graph $G _ { F } ( C )$ is a graph with $n$ vertices and edges corresponding to al graphs $G _ { 0 } = G , G _ { i } , i = 1 , \ldots , n - 1$ . It bounds the structure of the Cholesky factor $R$ ：

$$
G ( R ^ { T } + R ) \subset G _ { F } ( C ) .
$$

Under a no-cancelltion assumption, (5.1.4) holds with equality.

Theorem 5.1.1. Let $G ( C ) = ( V , E )$ be the undirected graph of the symmetric matrix $C$ Then $( v _ { i } , v _ { j } )$ is an edge of the filled graph $G _ { F } ( C )$ if and only $i f \left( v _ { i } , v _ { j } \right) \in E$ ，or there is a path in $G ( C )$ from vertex $i$ to vertex $j$ passing only through vertices $v _ { k }$ with $k < \operatorname* { m i n } ( i , j )$

The filled graph $G _ { F } ( C )$ can be characterized by an elimination tree $T ( C )$ that captures the row dependencies in the Cholesky factorization.

Definition 5.1.2. The elimination tree of a symmetric matrix $C \in \mathbb { R } ^ { n \times n }$ with Cholesky factor $R$ is a directed rooted tree $T ( C )$ with $n$ vertices labeled from $1$ to $n _ { \ast }$ ，where vertex $p$ is the parent of node i if and only if

$$
p = \operatorname* { m i n } _ { j } \{ j > i | r _ { i j } \neq 0 \} .
$$

$T ( C )$ is uniquely represented by the parent vector $P A R E N T [ i ]$ ， $i = 1 , \ldots , n$ ，of the vertices of the tree. For example,the parent vector of the elimination tree in Figure 5.1.3 is $5 , 5 , 6 , 6 , 7 , 7 , 8 , 0$

$T ( C )$ can be obtained from the filled graph $G _ { F } ( C )$ by introducing directed edges from lower to higher numbered vertices.A directed edge from node $j$ to node $i > j$ indicates that row $i$ depends on row $j$ . This row dependency is exhibited by the following transitive reduction of $G _ { F } ( C )$ . If there is a directed path from $j$ to $i$ of length greater than one,the edge from $j$ to $i$ is redundant and thus removed. The elimination tree is generated by the removal of all such redundant edges.For the matrix $A$ in (5.1.2) the filled graph $G _ { F } ( A ^ { T } A )$ equals $G ( A ^ { T } A )$ with an added edge between vertices 7 and 9. The result of the transitive reduction and the elimination tree is shown in Figure 5.1.4.

![](../chunks/Numerical Methods for Least Squares Problems (Åke Björck) (z-library.sk, 1lib.sk, z-lib.sk_part_0004_pages_0211-0280/auto/images/5c0c60cc6aa8010bdc25b46016262df7f06342e7ae39b0e4b9f297312d760412.jpg)  
Figure 5.1.4. The transitive reduction and elimination tree $T ( A ^ { T } A )$

The node ordering of an elimination tree is such that children vertices are numbered before their parent node. Such orderings are called topological orderings. Al topological orderings of the elimination tree are equivalent in the sense that they give the same triangular factor $R$ A postordering is a topological ordering in which a parent node $j$ always has node $j - 1$ as one of its children. For example,the ordering of the vertices in the tree in Figure 5.1.4 can be made into a postordering by exchanging labels 3 and 5. Postorderings can be determined by a depth-first search; see Liu [755,199o]. An important advantage of using a postordering is that it simplifies data management, and the storage is reduced.

Elimination trees play a fundamental role in symmetric sparse matrix factorization and provide,in compact form,all information about the row dependencies. Schreiber [974,1982] was the first to note this and to define elimination trees formally. In the excellent review of the generation and use of elimination trees by Liu [755,199o] an eficient algorithm is given that determines the elimination tree of $C$ in time proportional to $\mathrm { n n z } ( R )$ and in storage proportional t0 $\mathtt { n n z } ( C )$ . When $C = A ^ { T } A$ it is possible to predict the structure of $R$ directly without forming $C$ ； see Gilbert,Moler,and Schreiber [469,1992].

# 5.1.5 - Minimizing Fillin Cholesky Factorization

The sparsity of the Cholesky factor $R$ of $A ^ { T } A$ depends on the ordering of the columns of $A$ but not on the ordering of the rows. In the symbolic phase of sparse Cholesky factorization a column permutation $P$ is determined that tries to limit the fill in $R$ .It would be desirable to find a column ordering that minimizes the number of nonzeros in $R$ .However, this is known to be an NP-complete problem,i.e.,it cannot be solved in polynomial time. Even the problem of finding an ordering that minimizes the bandwidth of $R$ is NP-complete; see Papadimitriou [876,1976]. Hence we have to rely on heuristic methods.A simple algorithm is to order the columns in $A$ after increasing the number of nonzero elements in the columns. More effective methods can be obtained by using information from successively reduced submatrices.

We first consider ordering methods that have the objective of minimizing the bandwidth of $A ^ { T } A$ or rather the number of elements in the envelope of $C = A ^ { T } A$ Recall that by Theorem 4.1.6, zeros outside the envelope of $C$ will not suffer fill in the Cholesky factorization. Such ordering methods often perform well for matrices that come from one-dimensional problems or problems that are in some sense tall and thin. The most widely used such method is the Cuthill-McKee (CM) algorithm [281,1969]. It starts by finding a peripheral vertex $r$ (i.e., a vertex with lowest degree) in $G ( C )$ and numbering this as vertex 1. It then performs a breadth-first search using a level structure rooted at $r$ .This partitions the vertices into disjoint levels

$$
L _ { 1 } = r , L _ { 2 } ( r ) , \ldots , L _ { h } ( r ) ,
$$

where $L _ { i } ( r ) , i \le h$ ， is the set of all vertices adjacent to $\boldsymbol { L } _ { i - 1 } ( \boldsymbol { r } )$ that are not in $L _ { j } ( r ) , j =$ $1 , \ldots , i - 1$ . The search ends when all vertices are numbered.

# Algorithm 5.1.1 (Cuthill-McKee Ordering).

1. Select a peripheral vertex $r$ , and set $L _ { 1 } = { \binom { r } { } }$

2. for $i = 1 , 2 , \dots$ until all vertices are numbered do:

Find all unnumbered vertices in Adj $( L _ { i } )$ and number them

after increasing degrees.

George [453,1971] observed that the ordering obtained by reversing the Cuthill-McKee (RCM) ordering gives the same bandwidth and usually results in less fill. An implementation of the RCM algorithm with run-time proportional to the number of nonzeros in the matrix is given by Chan and George [230,198o]. The performance of the RCM ordering strongly depends on the choice of the starting peripheral node. George and Liu [457,1981] recommend a strategy where a node of maximal or nearly maximal eccentricity is chosen as a starting node. The eccentricity of a node is defined as

$$
l ( x ) = \operatorname* { m a x } _ { y \in X } d ( x , y ) ,
$$

where $d ( x , y )$ is the length of the shortest path between the two vertices $x$ and $y$ in $G = ( \boldsymbol { X } , E )$

A substantially faster algorithm for bandwidth minimization is the GPS algorithm by Gibbs, Poole,and Stockmeyer [467,1976].Lewis [738,1982], [737,1982] describes some improvements to the implementation of the GPS and other profile reduction algorithms. Sloan [1004, 1986] gives a new algorithm that generally results in a smaller profile. Among other proposed methods for envelope reduction,we mention the spectral method of Barnard,Pothen, and Simon [81,1995]. This uses the eigenvector of the smallest positive eigenvalue of the Laplacian matrix corresponding to the given matrix.

The minimum degree (MD) ordering is the most widely used heuristic method for limiting fill. The name “minimum degree” comes from the graph-theoretic formulation of the Cholesky algorithm first given by Rose [935,1972]; see Section 5.1.3. MD is a greedy method that in each step of the Cholesky factorization selects the next pivot as the sparsest row and column. It is a symmetric analogue of an ordering algorithm proposed by Markowitz [778,1957] for unsymmetric matrices with applications to linear programming. This algorithm was adapted for symmetric matrices by Tinney and Walker [1O64,1967]. The MD ordering minimizes the local arithmetic and amount of fillthat occurs but in general will not minimize the global arithmetic or fill. However, it has proved to be very effective in reducing both of these objectives. If the graph of $C = A ^ { T } A$ is a tree, then the MD ordering results in no fill.

# Algorithm 5.1.2 (Minimum Degre Ordering).

Set $G ^ { ( 0 ) } = G ( C )$ and determine the degrees ofits vertices.

for $i = 1 , \ldots , n - 1$ do

1. Select a vertex of minimal degree in $G ^ { ( i - 1 ) }$ as pivot.

2. Construct the elimination graph $G ^ { ( i ) }$ and update the degrees of its vertices.

For the matrix $C$ in (5.1.2) the initial elimination order indicated gives 1O fll-in elements. A minimum degree ordering such as $4 , 5 , 6 , 7 , 1 , 2 , 3$ will result in no fill-in.Because several vertices in the graph have degree 1, the minimum degree ordering is not unique.

If there is more than one node of minimum degree at a particular step, the node is chosen from the set of all vertices of minimum degree. The way this tie-breaking is done can be important. Examples are known for which the minimum degree ordering will give poor results if the tiebreaking is systematically done poorly. It is an open question how good the orderings are if ties are broken randomly. A matrix for which the minimum degree algorithm is not optimal is given by Duff,Erisman,and Reid [344,1g86]. If the minimum degree node 5 is eliminated first, fill will occur in position $( 4 , 6 )$ . But with the elimination ordering shown in Figure 5.1.5,there is no fill. In the multiple minimum degree algorithm (MMD) by George and Liu [459,1989] a refinement of the elimination graph model is used to decrease the number of degree updates. The vertices $Y = \{ y _ { 1 } , \dots , y _ { p } \}$ are called indistinguishable if they have the same adjacency sets (including the node itself),i.e.,

$$
\operatorname { A d j } \left( v _ { i } \right) \cup v _ { i } = \operatorname { A d j } \left( v _ { j } \right) \cup v _ { j } , \quad 1 \leq i , j \leq p .
$$

If one of these vertices is eliminated,the degrees of the remaining vertices in the set will decrease by one,and they all will become of minimum degree. Hence,all vertices in $Y$ can be eliminated simultaneously,and the graph transformation needs to be updated only once. Indeed, indistinguishable vertices can be merged and treated as one supernode. For example,the graph in Figure 5.1.5 contains two sets $\{ 1 , 2 , 3 \}$ and $\{ 7 , 8 , 9 \}$ of supervertices.

![](../chunks/Numerical Methods for Least Squares Problems (Åke Björck) (z-library.sk, 1lib.sk, z-lib.sk_part_0004_pages_0211-0280/auto/images/b142a4bae7be4f6ec5f97d9214638d3a1e44fd663fa9c44df34572f96622c8e1.jpg)  
Figure 5.1.5.The graph of a matrix for which minimum degree is not optimal.

The structure of each row in $A \in \mathbb { R } ^ { m \times n }$ corresponds to a clique in the graph of $C = A ^ { T } A$ Thus,the generalized element approach can be used to represent $C$ as a sequence of cliques. This allows the minimum degree algorithm for $A ^ { T } A$ to be implemented directly from $A$ without forming the structure of $C = A ^ { T } A$ , with resulting savings in work and storage.

The most costly part of the minimum degree algorithm is recomputation of the degree of the vertices adjacent to the new pivot column. In the approximate minimum degree (AMD) algorithm an upper bound on the exact minimum degree is used instead, which leads to substantial savings in run-time, especially for very irregularly structured matrices. It has no effect on the quality of the ordering; see Amestoy, Davis,and Duff [18, 2004].

# 5.2 - Sparse QR Factorization

# 5.2.1 - Predicting Structure in Sparse QR

The factor $R$ in the QR factorization of $A$ is the same as the Cholesky factor of $A ^ { T } A$ Therefore, it may seem that the same symbolic algorithm can be used to determine the structure of $R$ in both Cholesky and QR factorizations.If $A$ contains at least one dense row, then by the nocancellation assumption it follows that $A ^ { T } A$ is full,and we conclude that the Cholesky factor $R$ is full.However, this may considerably overestimate the number of nonzeros in $R$ .For example, consider the matrices with nonzero structures,

$$
A _ { 1 } = \left( \begin{array} { l l l l l } { \times } & { \times } & { \times } & { \times } & { \times } \\ { \times } & { \times } & & & \\ & { \times } & { \times } & & \\ & & { \times } & { \times } & \\ & & & { \times } & { \times } \end{array} \right) , \qquad A _ { 2 } = \left( \begin{array} { l l l l l } { \times } & { \times } & { \times } & { \times } & { \times } \\ & { \times } & { \times } & & \\ & & { \times } & { \times } & \\ & & & { \times } & { \times } \\ & & & & { \times } \end{array} \right) .
$$

For both $A _ { 1 }$ and $A _ { 2 }$ the matrix of normal equations is full. But $A _ { 2 }$ is already upper triangular, and hence $R = A _ { 2 }$ is sparse.For $A _ { 2 }$ there will be cancellation in the Cholesky factorization of $A _ { 2 } ^ { T } A _ { 2 }$ that will occur irrespective of the numerical values of the nonzero elements. This is called structural cancellation, in contrast to numerical cancellation that occurs only for certain values of the nonzero elements. Coleman, Edenbrandt,and Gilbert [262,1986] prove that if $A$ has the so-called strong Hall property, then structural cancellation cannot occur.

Definition 5.2.1. A matrix $A \in \mathbb { R } ^ { m \times n }$ ， $m \geq n$ , is said to have the strong Hall property if for every subset of $k$ columns, $0 < k < n$ ，the corresponding submatrix has nonzeros in at least $k + 1$ rows. That is, when $m > n$ ,every subset of $k \leq n$ columns has the required property, and when $m = n$ ,every subset of $k < n$ columns has the property.

Theorem 5.2.2. Let $A \in \mathbb { R } ^ { m \times n }$ ， $m \geq n$ ， have the strong Hall property. Then the structure of $A ^ { T } A$ correctly predicts that of $R$ ,excluding numerical cancellations.

Note that $A _ { 2 }$ in (5.2.1) does not have the strong Hall property because the first column has only one nonzero element. However, the matrix $\tilde { A }$ obtained by deleting the first column has this property.

The structure of $R$ in QR factorization can also be predicted by performing the Givens or Householder QR algorithm symbolically. In Givens QR factorization, the intermediate fill can be modeled using the bipartite graph $G ( A ) = \{ R , C , E \}$ 、Here the two sets of vertices

$$
\mathcal { R } = ( r _ { 1 } , \ldots , r _ { k } ) , \quad \mathcal { C } = ( c _ { 1 } , \ldots , c _ { k } )
$$

correspond to the sets of rows and columns of $A$ $E$ is a set of edges $\{ r _ { i } , c _ { j } \}$ that connects a node in $\mathcal { R }$ to one in $\mathcal { C }$ ,and $\{ r _ { i } , c _ { j } \} \in E$ if and only if $a _ { i j }$ is nonzero; see George, Liu, and $\mathrm { N g }$ [465, $\mathrm { 1 9 8 4 } ]$ and Ostrouchov [851,1987]. The following result is due to George and Heath [455, 1980].

Theorem 5.2.3. The structure of $R$ as predicted by a symbolic factorization of $A ^ { T } A$ includes the structure of $R$ as predicted by the symbolic Givens method.

Manneback [772,1985] proves that the structure predicted by a symbolic Householder algorithm is strictly included in the structure predicted from $A ^ { T } A$ .Symbolic Givens and Householder factorizations can also overestimate the structure of $R$ .An example where structural cancellation occurs for the Givens rule is shown by Gentleman [452,1976].

# 5.2.2 - The Row Sequential QR Algorithm

One of the first algorithms for sparse QR factorization was given by George and Heath [455, 1980]. In this,a symbolic factorization of $A ^ { T } A$ is used to form a static data structure for $R$ .Then $A$ is merged into this data structure row by row using Givens rotations,avoiding intermediate fill-in.

Although the final factor $R$ in QR factorization is independent of the ordering of the rows in $A$ ，the row ordering can significantly affect the intermediate fll and the number of Givens rotations needed to compute the factorization. This fact was stressed in the treatment of QR algorithms for band matrices; see Section 4.1. An extreme example is shown below, where the cost for factorizing $A$ is reduced from $O ( m n ^ { 2 } )$ to $O ( n ^ { 2 } )$ ：

$$
A = \left( \begin{array} { l l l l } { \times } & { \times } & { \times } & { \times } \\ { \times } & & & \\ { \vdots } & & & \\ { \times } & & & \\ { \times } & & & \\ & { \times } & & \\ & & { \times } & \\ & & & { \times } \end{array} \right) , \qquad P A = \left( \begin{array} { l l l l } { \times } & & & \\ { \times } & & & \\ { \vdots } & & & \\ { \times } & & { \times } & \\ & { \times } & { \times } & { \times } \\ & & { \times } & \\ & & & { \times } \end{array} \right) .
$$

Several heuristic algorithms for determining a row ordering have been suggested. The following is an extension of the row ordering recommended for band sparse matrices.

# Algorithm 5.2.1 (Row-Ordering Algorithm).

Denote the column index for the first and last nonzero elements in the ith row of $A$ by $f _ { i } ( A )$ and $\ell _ { i } ( A )$ ,respectively.

1. Sort the rows by increasing $f _ { i } ( A )$ ,so that $f _ { i } ( A ) \leq f _ { k } ( A )$ if $i < k$

2. For each group of rows with $f _ { i } ( A ) = k ,$ $k = 1 , \dots , \operatorname* { m a x } _ { i } f _ { i } ( A )$ ，sort all the rows by increasing $\ell _ { i } ( A )$

If Algorithm 5.2.1 is applied to $A$ in (5.2.2),the good row ordering $P A$ is obtained. The algorithm will not in general determine a unique ordering. One way to resolve ties is to consider the cost of symbolically rotating a row $a _ { i } ^ { T }$ into all other rows with a nonzero element in column $\ell _ { i } ( A )$ . By cost we mean the total number of new nonzero elements created. The rows are then ordered according to ascending cost.With this ordering it follows that rows $1 , \ldots , f _ { i } ( A ) - 1$ in $R _ { i - 1 }$ will not be afected when the remaining rows are processed. Therefore these rows are the final first $f _ { i } ( A ) - 1$ rows in $R$

An alternative that has been found to_work well in some contexts is to order the rows by increasing values of $\ell _ { i } ( A )$ . When row $a _ { i } ^ { T }$ is processed using this ordering,all previous rows processed have nonzeros only in columns up to at most $\ell _ { i } ( A )$ . Hence,only columns $f _ { i } ( A )$ to $\ell _ { i } ( A )$ of $R _ { i - 1 }$ will be involved, and $R _ { i - 1 }$ has zeros in columns $\ell _ { i + 1 } ( A ) , \ldots , n$ No fill will be generated in row $a _ { i } ^ { T }$ in these columns.

Liu [754,1986] introduced the notion of row merge tree for structuring this operation. Let $R _ { 0 }$ be initialized to have the structure of the final $R$ with all elements equal to zero.Denote by $R _ { k - 1 } \in \mathbb { R } ^ { n \times n }$ the upper triangular matrix obtained after processing the first $k - 1$ rows. At step $k$ the $k$ th row of $A$ is first uncompressed into a full vector $a _ { k } ^ { T } = ( a _ { k 1 } , a _ { k 2 } , \ldots , a _ { k n } )$ The nonzero elements $a _ { k j } \neq 0$ are annihilated from left to right by plane rotations involving rows $j < k$ in $R _ { k - 1 }$ . This may create new nonzeros in both $R _ { k - 1 }$ and in the current row $a _ { k } ^ { T }$ Note that if $r _ { j j } = 0$ in $R _ { k - 1 }$ ,this means that this row in $R _ { k - 1 }$ has not yet been touched by any rotation,and hence the entire $j$ th row must be zero.When this occurs the remaining part of row $k$ can just be inserted as the $j$ th row in $R _ { k - 1 }$ . The algorithm is illustrated below using an example from George and $\mathrm { N g } \ [ 4 6 0 , 1 9 8 3 ]$

Assume that the first $k$ rows of $A$ have been processed to generate $R _ { k }$ . Nonzero elements of $R _ { k - 1 }$ are denoted by $\times$ ， nonzeros introduced into $R _ { k }$ and $a _ { k } ^ { T }$ during the elimination $a _ { k } ^ { T }$ are denoted by $^ +$ ，and elements involved in the elimination of $a _ { k } ^ { T }$ are circled. Nonzero elements created in $a _ { k } ^ { T }$ during the elimination are ultimately annihilated. The sequence of row indices involved in the elimination is $\{ 2 , 4 , 5 , 7 , 8 \}$ ,where 2 is the column index of the first nonzero in $a _ { k } ^ { T }$ Note that unlike in the Householder method,intermediate fill only takes place in the row being processed:

$$
\left[ \begin{array} { c c c c c c c c c c } { R _ { k - 1 } } \\ { a } \\ { \mathbf { \Gamma } } \\ { \otimes } & { 0 } & { \otimes } & { \oplus } & { \otimes } & { 0 } & { 0 } & { 0 } & { 0 } \\ & { \otimes } & { 0 } & { \oplus } & { \otimes } & { 0 } & { 0 } & { 0 } & { 0 } \\ & { \times } & { 0 } & { \times } & { 0 } & { 0 } & { 0 } & { \times } & { 0 } \\ & & { \otimes } & { \oplus } & { 0 } & { \otimes } & { 0 } & { 0 } & { 0 } \\ & & & { \otimes } & { \oplus } & { 0 } & { 0 } & { 0 } & { 0 } \\ & & & & & { \otimes } & { \otimes } & { 0 } & { 0 } \\ & & & & & & & { \times } & { \times } \\ { 0 } & { \otimes } & { 0 } & { \otimes } & { \oplus } & { 0 } & { \oplus } & { 0 } & { 0 } \end{array} \right] .
$$

From Theorem 5.2.3 it follows that if the structure of $R$ has been predicted from that of $A ^ { T } A$ , any intermediate matrix $R _ { i - 1 }$ willft into the predicted structure. The plane rotations can be applied simultaneously to a right-hand side $b$ to form $Q ^ { T } b$ 、In the original implementation the Givens rotations are discarded after use.Hence,only enough storage to hold the final $R$ and a few extra vectors for the current row and right-hand side(s) is needed in main memory.

Gilbert et al. [468, 2oo1] give an algorithm to predict the structure of $R$ working directly from $G ( A )$ . This algorithm runs in time proportional to $\mathtt { n n z } ( A )$ and makes the step of determining the structure of $A ^ { T } A$ redundant.

Variable row pivoting methods are studied by Gentleman [450,1973], Duff [340,1974l,and Zlatev [1151,1982]. These schemes have never become very popular because they require a dynamic storage structure and are complicated to implement.

# 5.2.3 - Multifrontal methods

The multifrontal method, introduced by Duff and Reid [352,1983l, is a method for solving a linear system $A x = b$ that organizes the factorization of a sparse matrix into a sequence of partial factorizations of smaller independent dense subproblems that can be solved in parallel. This gives good data locality and lower communication costs. The following theorem, which is the basis for the multifrontal method, is due to Duff [343,1986].

Theorem 5.2.4. Let $T [ j ]$ denote the subtree rooted in node $j$ Then if $k \notin T [ j ]$ ,columns $k$ and $j$ can be eliminated independently of each other.

If $T [ i ]$ and $T [ j ]$ are two disjoint subtrees of $T ( C )$ , columns $s \in T [ i ]$ and $t \in T [ j ]$ can be eliminated in any order. The elimination tree prescribes an order relation for the elimination of columns in the QR factorization,i.e., a column associated with a child node must be eliminated before the parent column. On the other hand,columns associated with different subtrees of $T ( C )$ are independent and can be eliminated in parallel.

Liu [754,1986] developed a multifrontal QR algorithm that generalizes the row-oriented Givens QR algorithm by using submatrix rotations. It achieves a significant reduction in time at the cost of a modest increase in working storage. A modified version of this algorithm that uses Householder reflections is given by George and Liu [458,1987]. Supervertices and other essential modifications of multifrontal methods are treated by Liu [755,1990].

Nested dissection orderings have been discussed in Section 4.3.2. Such orderings for solving general sparse positive definite systems have been analyzed by George, Poole, and Voigt [462, 1978] and George and Liu [457,1g81]. The use of such orderings for sparse least squares problems is treated in George,Heath,and Plemmons $[ 4 6 4 , \ 1 9 8 1 ]$ and George and $\mathrm { N g }$ [460, $\mathrm { 1 9 8 3 } ]$ . A planar graph is a graph that can be drawn in the plane without two edges crossing. Planar graphs are known to have small balanced separators. Lipton, Rose,and Tarjan [753,1979] show that for any planar graph with $n$ vertices there exists a separator with $O ( \sqrt { n } )$ vertices such that each subgraph has at most $n / 2$ vertices.

We illustrate the multifrontal QR factorization by the small $1 2 \times 9$ matrix

$$
\scriptstyle A = { \left( \begin{array} { l l l l l l } { \times } & & { \times } & & { \times } & { \times } \\ { \times } & & { \times } & & { \times } & { \times } \\ { \times } & & & { \times } & & { \times } & \\ & { \times } & & & { \times } & & { \times } \\ & { \times } & & & { \times } & & { \times } \\ & & { \times } & & & { \times } & { \times } \\ & & & { \times } & & { \times } & { \times } \\ & { \times } & & & { \times } & { \times } & \\ & & { \times } & & { \times } & { \times } \\ & & & { \times } & & { \times } & { \times } \\ & & & & { \times } & & { \times } \\ & & { \times } & & & { \times } & { \times } \\ & & & { \times } & & { \times } & { \times } \end{array} \right) } .
$$

This matrix arises from a $3 \times 3$ mesh problem using a nested dissection ordering. The graph $G ( A ^ { T } A )$ is

![](../chunks/Numerical Methods for Least Squares Problems (Åke Björck) (z-library.sk, 1lib.sk, z-lib.sk_part_0004_pages_0211-0280/auto/images/4b85d8991798130c2cb4aaecc6a540edd07d04ab0ba79386c5e68ffab686ea1a.jpg)

First, a QR factorization of rows 1-3 is performed. These rows have nonzeros only in columns $\{ 1 , 5 , 7 , 8 \}$ . With the zero columns omitted, this operation can be carried out as a QR factorization of a small dense matrix of size $3 \times 4$ ，The resulting first row equals the first of the final $R$ of the complete matrix and can be stored away. The remaining two rows form an update matrix $F _ { 1 }$ and will be processed later. The other three block rows 4-6,7-9,and 1O-12 can be reduced similarly in parallel. After this first stage the matrix has the form

$$
\begin{array} { r } { \left( \begin{array} { l l l l l l } { \times } & { } & { } & { \times } & { } & { \times } \\ { } & { } & { \times } & { } & { \times } & { } \\ { } & { \times } & { } & { \times } & { \times } & { } \\ { } & { } & { \times } & { } & { \times } & { \times } \\ { } & { } & { \times } & { } & { \times } & { } \\ { } & { \times } & { } & { \times } & { } & { \times } \\ { } & { } & { \times } & { } & { \times } & { } \\ { } & { } & { \times } & { } & { \times } & { } \\ { } & { \times } & { } & { \times } & { } & { \times } \\ { } & { } & { \times } & { } & { \times } & { } \\ { } & { } & { \times } & { } & { \times } & { \times } \\ { } & { } & { } & { \times } & { } & { \times } & { } \\ { } & { } & { } & { \times } & { } & { \times } & { } \end{array} \right) . } \end{array}
$$

In the second stage, $F _ { 1 } , F _ { 2 }$ and $F _ { 3 } , F _ { 4 }$ are simultaneously merged into two upper trapezoidal matrices by eliminating columns 5 and 6. In merging $F _ { 1 }$ and $F _ { 2 }$ , only the set of columns $\{ 5 , 7 , 8 , 9 \}$ needs to be considered. Reordering the rows by the index of the first nonzero element and performing a QR decomposition, we get

$$
\begin{array} { r } { Q ^ { T } \left( \begin{array} { l l l l } { \times } & { \times } & { \times } & \\ { \times } & & { \times } & { \times } \\ & { \times } & { \times } & \\ & & { \times } & { \times } \end{array} \right) = \left( \begin{array} { l l l l } { \times } & { \times } & { \times } & { \times } \\ & { \times } & { \times } & { \times } \\ & & { \times } & { \times } \\ & & & { \times } \end{array} \right) . } \end{array}
$$

The first row in each of the four blocks is a final row in $R$ and can be removed, which leaves four upper trapezoidal update matrices, $F _ { 1 } { - } F _ { 4 }$ . The merging of $F _ { 3 }$ and $F _ { 4 }$ is performed similarly. The first row in each reduced matrix is a final row in $R$ and is removed.In the final stage the remaining two upper trapezoidal (in this example, triangular) matrices are merged, giving the final factor $R$ .This corresponds to eliminating columns 7,8,and 9.

In the multifrontal method the vertices in the elimination tree are visited in turn given by the ordering.Each node $x _ { j }$ in the tree is associated with a frontal matrix $F _ { j }$ that consists of the set of rows $A _ { j }$ in $A$ ,with the first nonzero in location $j$ ,together with one update matrix contributed by each child node of $x _ { j }$ . After variable $j$ in the frontal matrix is eliminated,the first row in the reduced matrix is the $j$ th row of the upper triangular factor $R$ .The remaining rows form a new update matrix $U _ { j }$ that is stored in a stack until needed.

For $j = 1 , \dotsc , n$ do

1. Form the frontal matrix $F _ { j }$ by combining the set of rows $A _ { j }$ and the update matrix $U _ { s }$ for each child $x _ { s }$ of the node $x _ { j }$ in the elimination tree $T ( A ^ { T } A )$ .

2.By an orthogonal transformation, eliminate variable $x _ { j }$ in $F _ { j }$ to get $\bar { U } _ { j }$ .Remove the first row in $\bar { U } _ { j }$ ,which is the $j$ th row in the final matrix $R$ . The rest of the matrix is the update matrix $U _ { j }$

The frontal matrices in the multifrontal method are often too small for the efficient use of vector processors and matrix-vector operations in the solution of the subproblems. Therefore, a useful modification of the multifrontal method is to amalgamate several vertices into one large supernode. Instead of eliminating one column in each node,the decomposition of the frontal matrices then involves the elimination of several columns,and it may be possible to use Level 2 or even Level 3 BLAS; see Dongarra et al. [328,199o]. Vertices can be grouped together to form a supernode if they correspond to a block of contiguous columns in the Cholesky factor, where the diagonal block is fully triangular,and these rows all have identical off-block diagonal column structures. Because of the computational advantages of having large supervertices, it is advantageous to relax this condition and also amalgamate vertices that satisfy this condition if some local zeros are treated as nonzeros. A practical restriction is that if too many vertices are amalgamated, then the frontal matrices become sparse. Note also that nonnumerical operations often make up a large part of the total decomposition time,which limits the possible gain. For a discussion of supervertices and other modifications of the multifrontal method, see Liu [755,1990].

For a $K$ by $K$ grid problem with $n = K ^ { 2 }$ ， $m = s ( K - 1 ) ^ { 2 }$ it is known that $\mathtt { n n z } ( R ) =$ $O ( n \log n )$ ,but $Q$ has $O ( n { \sqrt { n } } )$ nonzeros; see George and $\mathrm { N g }$ [461, 1988]. Hence if $Q$ is needed, it should not be stored explicitly but represented by the Householder vectors of the frontal orthogonal transformations.Lu and Barlow [761,1996] show that these require only $O ( n \log n )$ storage. In many implementations the orthogonal transformations are not stored. Then the corrected seminormal equations (see Section 2.5.4) can be used to treat additional right-hand sides.

# 5.2.4 - Software for Sparse Least Squares Problems

Early software, such as YSMP by Eisenstat et al.[362,1982] and SPARSPAK by George and $\mathrm { N g } [ 4 6 3 , 1 9 8 4 ]$ ,focused on the Cholesky algorithm.A Fortran subroutine LLSSO1 that performs sparse QR factorization by fast Givens rotations was developed by Zlatev and Nielsen [1152, 1979]. The orthogonal matrix $Q$ is not stored,and elements in $R$ smaller than a user-specified tolerance are dropped. Other early QR factorization codes were developed by Lewis,Pierce, and Wah[739,1989],Matstoms [784,1992],and Puglisi [907,1993]. Matstoms [785,1994] develops multifrontal concepts for QR factorization such as the use of supernode elimination tree and node amalgamation for increasing the effciency. Sun [1O46,1996] gives a parallel multifrontal algorithm for sparse QR factorization suitable for distributed-memory multiprocessors.A multifrontal sparse rank-revealing QR factorization/least squares solution module by Pierce and Lewis [894,1997l is included in the commercial software package BCSLIB-EXT from Boeing Information and Support Services. This library is also available to researchers in laboratories and academia for testing.

The SuiteSparse collection by Davis [290,2o11] includes a “state-of-the-art” sparse Cholesky factorization and a multithreaded multifrontal sparse QR algorithm and is available at www. netlib .org. The Ceres nonlinear least squares solver for three-dimensional imagery in Google Earth relies on the sparse Cholesky factorization in SuiteSparse.The multithreaded multifrontal sparse QR factorization QR MUMPS by Buttari [195,2o13] builds on earlier implementations of Puglisi and Matstoms; see Amestoy, Duff,and Puglisi [19,1996].

The design of sparse matrix storage and computations for MATLAB is described by Gilbert, Moler,and Schreiber [469,1992]. A matrix is stored as either full or sparse. Conversion between full and sparse storage modes is done by the inbuilt functions spar se and full. A sparse matrix is stored in CSC format as the concatenation of the sparse vectors representing its columns. This makes it efcient to scan the columns of a sparse matrix but very inefficient to scan its rows. To facilitate a basic sparse operation, a sparse accumulator (SPA) that allows random access to the currently active column or row of a matrix is used. The SPA consists of a dense vector of real (or complex) values,a dense vector of true/false “occupied flags,” and an unordered list of the indices whose occupied flags are true. Almost all sparse operations are performed as operations between the SPA and a sparse vector. This allows many vector operations to be carried out in time proportional to the number of nonzero element in the vector. Factorizations such as LU, Cholesky,and QR of a sparse matrix yield sparse results but, otherwise,behave as the corresponding dense MATLAB operations.

Several column reorderings of the column are available in MATLAB for making the Cholesky and QR factors more sparse. MATLAB stores a permutation as a vector p containing a permutation of $1 , 2 , \ldots , n$ such that $\mathbb { A } \left( : , \thinspace \mathfrak { p } \right)$ is the matrix with permuted columns.The function $\mathtt { p } \ = \ \mathtt { c o l p e r m } ( \mathtt { A } )$ computes a permutation that sorts the columns so that they have increas-ing nonzero count. An approximate minimum degree ordering for the columns is given by $\mathtt { p } \ = \ \mathtt { c o l m m d } ( \mathtt { A }$ .

To solve a sparse least squares problem using a minimum degree ordering of the columns of $A$ and the corrected seminormal equations (CSNE; see Section 2.5.4), one writes the following in MATLAB.

# Algorithm 5.2.2 (Sparse Least Squares Solution by CSNE).

$$
{ \begin{array} { l l l } { \arcsin { \mathrm { ~ ( x , r ) ~ } } = { \mathrm { ~ s p a r s e l s e d s e q ( A , b ) ~ } } ; } \\ { { \begin{array} { l l l l } { \gamma _ { \mu } } & { \operatorname { - --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- } \\ { \mathrm { ~ q _ { \mu } ~ } } = { \mathrm { ~ c o l m m d ~ ( A ) ~ } } ; } & { \qquad \gamma _ { \mu } } & { { \mathrm { M i n i m i m u ~ d e g r e e ~ o r d e r i n g ~ o f ~ A ~ } } } \\ { \mathrm { ~ A } } & { \mathrm { ~ A } ( : , \mathrm { q } ) ; } & { \qquad \gamma _ { \mu } } & { { \mathrm { R e o r d e r ~ c o l u m s ~ o f ~ A e c o m p o s i t i o n } } } \\ { \mathrm { ~ R } } & { = { \mathrm { ~ c h o l ~ } } ( \mathrm { A } ^ { \prime } * \mathrm { k } ) ; } & { \qquad \gamma _ { \mu } } & { { \mathrm { S p a r s e ~ c h o ~ c h o l e s k y ~ d e c o m p o s i t i o n } } } \\ { \mathrm { ~ x } } & { \mathrm { ~ R } } & { \mathrm { ( ~ A } ^ { \prime } * \mathrm { b } ) ; } & { \qquad \gamma _ { \mu } } & { { \mathrm { L e a s t ~ } } \mathrm { ~ s q u a r e s ~ s o l u t i o n } } \\ { \mathrm { ~ x } } & { \mathrm { ~ + ~ \mathrm { ~ R } ~ } \mathrm { { ~ ( ~ A } ^ { \prime } * ( \mathrm { b } ~ - ~ \mathrm { ~ A } * \mathrm { x } ) ) } } & { \quad \forall _ { \mu } } & { { \mathrm { C o r r e c t i o n ~ s t e p } } } \\ { \mathrm { ~ x } } & { \mathrm { ~ ( q ) } } & { = \mathrm { ~ x } ; } & { } & { \gamma _ { \mathrm { { o } } } { \mathrm { ~ P e r m u t e ~ s o l u t i o n } } } \end{array} } } \\ { { \mathrm { ~ x } } } \end{array} }
$$

SuiteSparseQR is also available in MATLAB. This allows large-scale sparse least squares problems to be solved. The function $[ \mathbb { Q } , \mathbb { R } , \mathbb { p } ] \ = \ \mathsf { q r } \left( \mathbb { A } , \mathbf { \ell } ^ { \prime } \mathsf { v e c t o r } ^ { \prime } \right)$ returns the $m \times n$ factor $\mathtt { R }$ and $m \times m$ factor $\mathsf { Q }$ such that $\mathsf { A } \left( : , \mathsf { p } \right) \ = \ \mathsf { q } * \mathsf { R } .$ Because $\mathsf { Q }$ often is not very sparse,a better choice is to solve one or more least squares problems m $\mathrm { i n } \| A X - B \|$ using $[ { \mathsf C } , { \mathsf R } , { \mathsf p } ] \ = \ { \mathsf { q r } } ( { \mathsf { A } } , { \mathsf { B } } , 0 )$ and $\mathbb { X } \left( \mathbb { p } , : \right) \ = \ \mathbb { R } \backslash \mathbb { C }$

Example 5.2.5. We study the effect of two different column orderings in the QR factorization of a sparse matrix $A$ arising in a study of substance transport in rivers by Elfving and Skoglund [384, 2007]. Figures 5.2.1 and 5.2.2 show the location of nonzero elements in $A P$ and $R$ using two different column orderings available in MATLAB.With colperm the columns are ordered by increasing nonzero elements and give $\mathrm { n n z } ( R ) = 3 2 { , } 3 5 5$ .The colamd ordering gives $\mathtt { n n z } ( R ) =$ 15,903,a great improvement. □

# 5.2.5 - Rank-Revealing Sparse QR Factorization

For dense matrices $A$ ,rank-deficient problems are handled by column pivoting in the QR factorization of $A$ ； see Section 2.3.2. In sparse QR factorization the initial column ordering is chosen to produce a sparse $R$ -factor in advance of any numerical computation. If the columns are reordered, the updated $R$ will in general not fit into the previously generated storage structure.

If the row sequential QR algorithm is applied in exact arithmetic to a matrix $A$ of rank $r < n$ ， a row is inserted into $R$ only when it makes the diagonal entry nonzero. Hence the resulting $R \mathrm { . }$ - factor must have $n - r$ zero diagonal elements. Processing additional rows can only increase the absolute value of the diagonal elements. Hence if the final $R$ has a zero diagonal element, all elements in this row are zero,and the final $R$ will have the form depicted in Figure 5.2.3. By permuting the zero rows of $R$ to the bottom,and the columns of $R$ corresponding to the zero diagonal elements to the right, we obtain $R$ in rank-revealing form.

![](../chunks/Numerical Methods for Least Squares Problems (Åke Björck) (z-library.sk, 1lib.sk, z-lib.sk_part_0004_pages_0211-0280/auto/images/cde83a6231e8dfa601b66784832f0d627326a8cc7c7f738f0318e07241bb0c35.jpg)  
Figure 5.2.1. Nonzero pattern of a sparse matrix $A$ and the factor $R$ in its QR factorization using the MATLAB colperm reordering. Used with permission of Springer International Publishing; from Numerical Methods in Matrix Computations, Bjorck, $\mathring { A } k e$ ，2015；permission conveyed through Copyright Clearance Center, Inc.

![](../chunks/Numerical Methods for Least Squares Problems (Åke Björck) (z-library.sk, 1lib.sk, z-lib.sk_part_0004_pages_0211-0280/auto/images/6f31bf357e0ff249396b349f7f2527ceca94cc0617ba0d5bd341aa9ebf9b3250.jpg)  
Figure 5.2.2. Nonzero pattern of a sparse matrix $A$ and the factor $R$ in its QR factorization using the MATLAB colamd column ordering. Used with permission of Springer International Publishing; from Numerical Methods in Matrix Computations,Bjorck, $\mathring { A } k e ,$ ，2015；permission conveyed through Copyright Clearance Center, Inc.

![](../chunks/Numerical Methods for Least Squares Problems (Åke Björck) (z-library.sk, 1lib.sk, z-lib.sk_part_0004_pages_0211-0280/auto/images/15048f066a8f6ab72982ea9ea23ed3e1dc01f856eb2ce9e7dbe4d3e457e223ec.jpg)  
Figure 5.2.3. Structure of upper triangular matrix R for a rank-deficient matrix.

In finite-precision, the computed $R$ usually will not have any zero diagonal element, even when $\operatorname { r a n k } ( A ) \ < \ n$ .Although the rank is often revealed by the presence of small diagonal elements, this does not imply that the rest of the rows are negligible. Heath [596,1982] suggests the following postprocessing of $R$ Starting from the top, the diagonal of $R$ is examined for small elements. In each row whose diagonal element fals below a certain tolerance, the diagonal element is set to zero. The rest of the row is then reprocessed,zeroing out all its other nonzero elements. This might increase some previously small diagonal elements in rows below, which is why one has to start from the top. We again end up with a matrix of the form shown in Figure 5.2.3.However, it may be that $R$ is numerically rank-deficient yet has no small diagonal element.

Pierce and Lewis [894,1997] develop a rank-revealing algorithm for sparse QR factorizations based on techniques similar to those in Section 2.3.5. The factorization proceeds by columns, and inverse iteration is used to determine ill-conditioning. Let $R _ { j } = ( r _ { 1 } , \ldots , r _ { j } )$ be the matrix formed by the first $j$ columns of the final $R$ 、Assume that $R _ { j }$ is not too ill-conditioned,but $R _ { j + 1 } = { \left( \begin{array} { l l } { R _ { j } } & { r _ { j + 1 } } \end{array} \right) }$ is found to be almost rank-deficient. Then column $r _ { j + 1 }$ is permuted to the last position,and the algorithm is continued. This may happen several times during the numerical factorization.At the end we obtain a QR factorization

$$
\left( A _ { 1 } \quad A _ { 2 } \right) = Q \left( { R _ { 1 1 } } \quad R _ { 1 2 } \atop 0 \quad S \right) ,
$$

where $R _ { 1 1 } \in \mathbb { R } ^ { r \times r }$ is well-conditioned. In general $R _ { 1 2 }$ and $S$ will be dense,but provided $r \ll n$ ， this is often acceptable.An important fact stated in the theorem below is that $R _ { 1 1 }$ will always fit into the storage structure predicted for $R$ .The following theorem is implicit in Foster [424, 1986].

Theorem 5.2.6. Let $A = ( a _ { 1 } , a _ { 2 } , \ldots , a _ { n } )$ , and let

$$
A _ { { \mathcal { F } } _ { k } } = [ a _ { j _ { 1 } } , a _ { j _ { 2 } } , \dotsc , a _ { j _ { r } } ] , \qquad 1 \leq j _ { 1 } < j _ { 2 } < \dotsc < j _ { r } \leq n
$$

be a submatrix of $A$ Denote the Cholesky factors of $A ^ { T } A$ and $A _ { \mathcal { F } _ { k } } ^ { T } A _ { \mathcal { F } _ { k } }$ by $R$ and $R _ { \mathcal { F } _ { k } }$ ,respectively. Then the nonzero structure of $R _ { \mathcal { F } _ { k } }$ is included in the nonzero structure predicted for $R$ under the no-cancellation assumption.

Proof. Let $G = G ( \boldsymbol { X } , E )$ be the ordered graph of $A ^ { T } A$ . The ordered graph $G _ { \mathcal { F } _ { k } } = G _ { \mathcal { F } _ { k } } ( X _ { \mathcal { F } _ { k } }$ $E _ { \mathcal { F } _ { k } } )$ of $A _ { \mathcal { F } _ { k } } ^ { T } A _ { \mathcal { F } _ { k } }$ is obtained by deleting all vertices in $G$ not in $\mathcal { F } _ { k } = [ j _ { 1 } , j _ { 2 } , \dotsc , j _ { r } ]$ and all edges leading to the deleted vertices. Then $( R \mathcal { F } ) _ { i j } \neq 0$ only if there exists a path in $G _ { \mathcal { F } _ { k } }$ from node $i$ to node $j$ $( i < j )$ through vertices with numbers less than $i$ . If such a path exists in $G _ { \mathcal { F } _ { k } }$ ， it must exist also in $G$ ,and hence we will have predicted $R _ { i j } \neq 0$ □

# 5.3 - Special Topics

# 5.3.1 - Mixed Sparse-Dense Least Squares Problems

In some applications,least squares problems arise in which $A \in \mathbb { R } ^ { m \times n }$ is sparse, except for a small number of dense rows representing additional coupling terms. If the dense rows are ordered last,such problems have the form

$$
\operatorname* { m i n } _ { x } \| A x - b \| _ { 2 } = \operatorname* { m i n } _ { x } \left\| \left( A _ { d } \right) x - \left( { b } _ { s } \right) \right\| _ { 2 } ,
$$

where $A _ { s } \in \mathbb { R } ^ { m _ { s } \times n }$ is sparse, $A _ { d } \in \mathbb { R } ^ { m _ { d } \times n }$ is dense, and $m = m _ { s } + m _ { d }$ with $m _ { d } \ll n$ .Then $A ^ { T } A = A _ { s } ^ { T } A _ { s } + A _ { d } ^ { T } A _ { d }$ , and its Cholesky factor willbe dense. For large-scale mixed sparse-dense least squares problems, standard sparse Cholesky and QR methods are not practical because of their high memory and computing demands. We remark that finding a good partitioning between sparse and dense equations can be a nontrivial problem.

We now describe an updating method by Heath [596,1982] in which dense rows are first withheld from the QR factorization. The solution (not the factorization) to the sparse subproblem is then updated to incorporate the dense rows.Let the QR factorization of the sparse subproblem be

$$
\begin{array} { r } { \left( \begin{array} { c c } { A _ { s } } & { b _ { s } } \end{array} \right) = Q _ { s } \left( \begin{array} { c c } { R _ { s } } & { c _ { s } } \\ { 0 } & { d _ { s } } \end{array} \right) , } \end{array}
$$

where $Q _ { s }$ need not be formed or saved. If $\operatorname { r a n k } ( A _ { s } ) = n$ ，then $R _ { s }$ is nonsingular, and the solution $y$ to the sparse subproblem can be obtained from $R _ { s } y = c _ { s }$ . Setting $x = y + z$ and noting that $c _ { s } - R _ { s } y = 0$ , we can write the residuals to the sparse subproblem as

$$
r _ { s } = b _ { s } - A _ { s } ( y + z ) = Q _ { s } \left( \begin{array} { c } { - R _ { s } z } \\ { d _ { s } } \end{array} \right) .
$$

It follows that $z$ solves

$$
\operatorname* { m i n } _ { z } \left\| \left( \begin{array} { l } { R _ { s } } \\ { A _ { d } } \end{array} \right) z - \left( \begin{array} { l } { 0 } \\ { r _ { d } } \end{array} \right) \right\| _ { 2 } , \quad r _ { d } = b _ { d } - A _ { d } y .
$$

By the change of variables

$$
u = R _ { s } z , \quad v = r _ { d } - C _ { d } u , \quad C _ { d } = A _ { d } R _ { s } ^ { - 1 } \in \mathbb { R } ^ { m _ { d } \times n } ,
$$

this problem is seen to be that of finding the least-norm solution to the linear system

$$
\begin{array} { r l } { ( I _ { m _ { d } } } & { { } C _ { d } ) \left( \begin{array} { l } { v } \\ { u } \end{array} \right) = r _ { d } . } \end{array}
$$

This problem is the same as the small least squares problem

$$
\operatorname* { m i n } _ { \boldsymbol { v } } \left\| \left( \begin{array} { c } { I _ { m _ { d } } } \\ { C _ { d } ^ { T } } \end{array} \right) \boldsymbol { v } - \left( \begin{array} { c } { r _ { d } } \\ { 0 } \end{array} \right) \right\| _ { 2 } , \quad \boldsymbol { u } = C _ { d } ^ { T } \boldsymbol { v } ,
$$

which can be solved by QR factorization of the $( m _ { d } + n ) \times m _ { d }$ matrix.Note that for both problems the normal equations for $v$ are

$$
( C _ { d } C _ { d } ^ { T } + I _ { m _ { d } } ) v = r _ { d } .
$$

Finally, the solution $x$ to problem (5.3.1) is $x = y + z$ ，where $z$ is found by solving $R _ { s } z = u$ The algorithm is summarized below.

# Algorithm 5.3.1 (Solving a Sparse-Dense Lease Squares Problem by Updating).

1. Compue spaseQRfatriaton $\begin{array} { r } { ( \ A _ { s } \quad b _ { s } ) = Q _ { s } \left( \begin{array} { c c } { R _ { s } } & { c _ { s } } \\ { 0 } & { d _ { s } } \end{array} \right) . } \end{array}$

2. Solve $R _ { s } y = c _ { s }$ for y and form residual $r _ { d } = b _ { d } - A _ { d } y$

3. Compute $C _ { d } \in \mathbb { R } ^ { m _ { d } \times n }$ from $R _ { s } ^ { T } C _ { d } ^ { T } = A _ { d } ^ { T }$

4. Solve thefulranklastsaresproblm(.)for $v$ and form $u = C _ { d } ^ { T } v$

5. Form the solution $x = y + z$ ,where $R _ { s } z = u$

A fundamental diffculty arises with this updating method if $A _ { s }$ is ill-conditioned or singular. f $\operatorname { r a n k } ( A _ { s } ) < n$ ,then $R _ { s }$ is singular, and the algorithm breaks down. If $\sigma _ { \operatorname* { m i n } } ( A _ { s } ) \ll \sigma _ { \operatorname* { m i n } } ( A )$ ， then Algorithm 5.3.1 is not stable.

It is not unusual in practice for $A _ { s }$ to have $n _ { 2 } \ll n$ null columns. If the null columns are permuted to the last positions and $x$ is partitioned conformally, the problem becomes

$$
A = \left( A _ { 1 } \quad A _ { 2 } \right) = \left( \begin{array} { c c } { { A _ { s _ { 1 } } } } & { { 0 } } \\ { { A _ { d _ { 1 } } } } & { { A _ { d _ { 2 } } } } \end{array} \right) , \quad x = \left( \begin{array} { c } { { x _ { 1 } } } \\ { { x _ { 2 } } } \end{array} \right) ,
$$

where $A _ { 1 }$ has full column rank, $x _ { 1 } \in \mathbb { R } ^ { n _ { 1 } }$ and $x _ { 2 } ~ \in ~ \mathbb { R } ^ { n _ { 2 } }$ ，and $n = n _ { 1 } + n _ { 2 }$ . The previous updating scheme is generalized to this case by Heath [596,1982]. Let $z \in \mathbb { R } ^ { n _ { 1 } }$ and $W \in \mathbb { R } ^ { n _ { 1 } \times n _ { 2 } }$ be the solutions of the least squares problems

$$
\operatorname* { m i n } _ { z } \| A _ { 1 } z - b \| _ { 2 } , \qquad \operatorname* { m i n } _ { z } \| A _ { 1 } W - A _ { 2 } \| _ { 2 } ,
$$

respectively. In both least squares problems (5.3.7), $A _ { 1 }$ has full rank and $m _ { d }$ has dense rows and, thus problems (5.3.7) can be solved by the previous algorithm. Then $x _ { 2 }$ is obtained as the solution of the small dense least squares problem

$$
\operatorname* { m i n } _ { x _ { 2 } } \| ( A _ { 2 } - A _ { 1 } W ) x _ { 2 } - ( b - A _ { 1 } z ) \| _ { 2 }
$$

of size $m \times n _ { 2 }$ ,and $x _ { 1 } = z - W x _ { 2 }$ ; see Lemma 4.3.1.

Another approach for treating mixed sparse-dense least squares problems is matrix stretch-ing; see Grcar [530,199o] and Adlers and Bjorck [8,2ooo].In this approach,dense rows are replaced by several much sparser rows connected by additional linking variables. The strength and limitations of this approach are studied by Scott and Tüma [990, 2o1g9]. They propose a new stretching strategy that better limits the fillin the normal matrix and its Cholesky factorization.

Avron, $\mathrm { N g }$ ,and Toledo [45,2oo9] propose using an iterative method, such as LSQR, preconditioned by $R _ { s }$ from the sparse QR factorization of $A _ { s }$ . This requires $A _ { s }$ to have full column rank and be not too ill-conditioned. A Schur complement approach to preconditioning mixed sparse-dense problems is studied by Scott and Tuma [989,2o18]. In image reconstruction and certain other inverse problems, $A$ may be fairly sparse in all rows and columns, but $A ^ { T } A$ may be practically dense. Such problems are usually solved by preconditioned iterative methods; see Scott and Tuma [988, 2017].

# 5.3.2 - Canonical Block Triangular Form

Sometimes it can be helpful to permute $A$ into the canonical block upper triangular form discovered by Dulmageand Mendelsohn [353,1958], [354,1959],[355,1963l,and Johnson,Dulmage,

and Mendelsohn [675,1963]:

$$
P A Q = \left( \begin{array} { c c c } { { A _ { h } } } & { { U _ { h s } } } & { { U _ { h v } } } \\ { { } } & { { A _ { s } } } & { { U _ { s v } } } \\ { { } } & { { } } & { { A _ { v } } } \end{array} \right) .
$$

Here the block $A _ { h }$ is underdetermined (has more columns than rows), $A _ { s }$ is square, and $A _ { v }$ is overdetermined (has more rows than columns). All three blocks have a nonzero diagonal, and the submatrices $A _ { v }$ and $A _ { h } ^ { T }$ both have the strong Hall property. One or two of the diagonal blocks may be absent in the decomposition. The example below shows the coarse block triangular decomposition of a matrix $A \in \mathbb { R } ^ { 1 1 \times 1 0 }$ with structural rank 8.

<table><tr><td>×</td><td>8 ×</td><td>× 8</td><td>×</td><td>×</td><td>×</td><td>×</td></tr><tr><td></td><td></td><td>? ×</td><td>× 8</td><td></td><td>×</td><td>×</td></tr><tr><td></td><td></td><td></td><td></td><td>8 ×</td><td>× 8</td><td>×</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>8</td><td>×</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>8</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>×</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>×</td><td>×</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>×</td></tr></table>

It may be possible to further decompose the blocks $A _ { h }$ and $A _ { v }$ in the coarse decomposition (5.3.9) so that

$$
A _ { h } = \left( \begin{array} { c c c } { { A _ { h 1 } } } & { { } } & { { } } \\ { { } } & { { \ddots } } & { { } } \\ { { } } & { { } } & { { A _ { h p } } } \end{array} \right) , \qquad A _ { v } = \left( \begin{array} { c c c } { { A _ { v 1 } } } & { { } } & { { } } \\ { { } } & { { \ddots } } & { { } } \\ { { } } & { { } } & { { A _ { v q } } } \end{array} \right) ,
$$

where each $A _ { h 1 } , \ldots , A _ { h p }$ is underdetermined and each $A _ { v 1 } , \ldots , A _ { v q }$ is overdetermined. The submatrix $A _ { s }$ may be decomposable into block upper triangular form

$$
A _ { s } = \left( \begin{array} { c c c c } { A _ { s 1 } } & { U _ { 1 2 } } & { . . . } & { U _ { 1 , t } } \\ & { A _ { s 2 } } & { . . . } & { U _ { 2 , t } } \\ & & { \cdot . } & { \vdots } \\ & & & { A _ { s t } } \end{array} \right)
$$

with square diagonal blocks $A _ { s 1 } , \ldots , A _ { s t }$ that have nonzero diagonal elements. The resulting fine decomposition can be shown to be essentially unique. Any block triangular form can be obtained from any other by applying row permutations that involve the rows of a single block row, column permutations that involve the columns of a single block column, and symmetric permutations that reorder the blocks.

A square matrix that can be permuted to the form (5.3.1O), with $t > 1$ ,is said to be reducible; otherwise, it is called irreducible; see Definition 4.1.3.All the diagonal blocks $A _ { s 1 } , \ldots , A _ { s t }$ in the fine decomposition are irreducible.This implies that they have the strong Hal property; see Coleman, Edenbrandt,and Gilbert [262,1g86]. A two-stage algorithm for permuting a square and structurally nonsingular matrix $A$ to block upper triangular is given by Tarjan [1O57,1972]; see also Gustavson [555,1976],and Duff [341,1977], [342,1981]. The algorithm depends on the concept of matching in the bipartite graph of $A$ . This is a subset of its edges with no common end points and corresponds to a subset of nonzeros in $A$ such that no two belong to the same row or column. A maximum matching is one where the maximum number of edges equals the structural rank $r ( A )$

Pothen and Fan [902,1990],[901, $\mathrm { 1 9 8 4 } ]$ give an algorithm for the general case. The program MC13D by Duff and Reid [351,1978] in the HSL Mathematical Software Library implements the fine decomposition of $A _ { s }$ . It proceeds in three steps:

1. Find a maximum matching in the bipartite graph $G ( A )$ with row set $\mathcal { R }$ and column set $\mathcal { C }$   
2.According to the matching, partition $\mathcal { R }$ into sets $\mathcal { V R } , \mathcal { S R } , \mathcal { H R }$ and $\mathcal { C }$ into sets $\nu \mathcal { C } , S \mathcal { C }$ ， HC corresponding to the vertical, square,and horizontal blocks.   
3.Find the diagonal blocks of the submatrices $A _ { v }$ and $A _ { h }$ from the connected components in the subgraphs $G ( A _ { v } )$ and $G ( A _ { h } )$ . Find the block upper triangular form of $A _ { s }$ from the strongly connected components in the associated directed subgraph $G ( A _ { s } )$ , with edges directed from columns to rows.

In MATLAB the algorithm is available through the function $\mathrm { [ p , q , r , s , c c , r r ] ~ = ~ d m p e r m \left( A \right) }$ The output consists of row and column permutation vectors $p$ and $q$ ，such that $A ( p , q )$ has Dulmage-Mendelsohn block triangular form． The vectors $r$ and $s$ are index vectors indicating the block boundaries for the fine decomposition,while the vectors $c c$ and $r r$ indicate the boundaries of the coarse decomposition.

The reordering to block triangular form in a preprocessing phase can save work and intermediate storage in solving least squares problems. If $A$ has structural rank $n$ ,the first block row in (5.3.9) must be empty,and the original least squares problem can,after a reordering,be solved by a form of block back-substitution. First,partition $\tilde { x } = Q ^ { T } x$ and $\tilde { b } = P b$ conformally with $P A Q$ in (5.3.9) and compute the solution $\tilde { x } _ { v }$ of

$$
\operatorname* { m i n } _ { \tilde { \boldsymbol { x } } _ { v } } \| \boldsymbol { A } _ { v } \tilde { \boldsymbol { x } } _ { v } - \tilde { \boldsymbol { b } } _ { v } \| _ { 2 } .
$$

Next, compute the remaining part of the solution $\tilde { x } _ { k } , \ldots , \tilde { x } _ { 1 }$ from

$$
A _ { s i } \tilde { x } _ { i } = \tilde { b } _ { i } - \sum _ { j = i + 1 } ^ { k } U _ { i j } \tilde { x } _ { j } , \quad i = k , \ldots , 2 , 1 .
$$

Finally, set $x = Q \tilde { x }$ .We can solve subproblems (5.3.11) and (5.3.12) by computing the QR factorizations of $A _ { v }$ and $A _ { s , i }$ ， $i = 1 , \ldots , k$ .As $A _ { s 1 } , \ldots , A _ { s k }$ and $A _ { v }$ have the strong Hall property, the structures of the matrices $R _ { i }$ are correctly predicted by the structures of the corresponding normal matrices.

If $A$ has structural rank $n$ but is numerically rank-deficient, it will not be possible to factorize all the diagonal blocks in (5.3.1O). In this case the block triangular structure given by the Dulmage-Mendelsohn form cannot be preserved,or some blocks may become severely ilconditioned. If the structural rank is less than $n$ ,there isan underdetermined block $A _ { h }$ .In this case we can still obtain the form (5.3.1O) with a square block $A _ { 1 1 }$ by permuting the extra columns in the first block to the end.The least squares solution is then not unique,but there is a unique solution of minimum length.

The block triangular form of the matrices in the Harwell-Boeing test collection (Duff, Grimes,and Lewis [346,1989l) and the time required to compute them are given in Pothen and Fan [902,1990].


<!-- chunk 0005: pages 281-350 -->
