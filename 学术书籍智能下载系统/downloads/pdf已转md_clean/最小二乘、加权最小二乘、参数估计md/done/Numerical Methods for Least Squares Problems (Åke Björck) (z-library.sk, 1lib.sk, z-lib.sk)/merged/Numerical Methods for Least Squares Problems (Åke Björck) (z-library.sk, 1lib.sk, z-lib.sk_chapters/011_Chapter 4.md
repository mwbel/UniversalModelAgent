Chapter 4

# Special Least Squares Problems

# 4.1 - Band Least Squares Problems

# 4.1.1 - Properties of Band Matrices

Band matrices occur frequently in many algorithms for computing eigenvalues and singular values as well as in problems of approximations and differential equations.We define the bandwidth of a square matrix $A \in \mathbb { R } ^ { n \times n }$ to be

$$
w = \operatorname* { m a x } _ { a _ { i j } \neq 0 } | i - j | ,
$$

i.e., all nonzero elements in each row of $A$ lie in at most $w$ contiguous positions. If $w \ll n$ ， then only a small proportion of the $n ^ { 2 }$ elements are nonzero,and they are located in a band centered along the principal diagonal. Band linear systems and least squares problems with small bandwidth $w \ll n$ arise in applications where each variable $x _ { i }$ is coupled to only a few other variables $x _ { j }$ such that $| j - i |$ is small. Clearly, the bandwidth of a matrix depends on the ordering of its rows and columns.

The lower bandwidth $r$ and upper bandwidth $s$ are the smallest integers such that

$$
a _ { i j } = 0 { \mathrm { ~ i f ~ } } j < i - r { \mathrm { ~ o r ~ } } j > i + s , \quad i = 1 , \ldots , n .
$$

In other words,the number of nonzero diagonals below and above the main diagonal are $r$ and $s$ ,respectively. The maximum number of nonzero elements in any row is $w = r + s + 1$ .For example,the matrix

$$
\left( \begin{array} { l l l l l l } { a _ { 1 1 } } & { a _ { 1 2 } } & & & & \\ { a _ { 2 1 } } & { a _ { 2 2 } } & { a _ { 2 3 } } & & & \\ { a _ { 3 1 } } & { a _ { 3 2 } } & { a _ { 3 3 } } & { a _ { 3 4 } } & & \\ & { a _ { 4 2 } } & { a _ { 4 3 } } & { a _ { 4 4 } } & { a _ { 4 5 } } & \\ & & { a _ { 5 3 } } & { a _ { 5 4 } } & { a _ { 5 5 } } & { a _ { 5 6 } } \\ & & & { a _ { 6 4 } } & { a _ { 6 5 } } & { a _ { 6 6 } } \end{array} \right)
$$

has $r = 2$ ， $s = 1$ ,and $w = 4$ If $A$ is symmetric, then $r = s$ .Several frequently occurring classes of band matrices have special names, e.g., a matrix for which $r = s = 1$ is called tridiagonal. If $r = 0 , s = 1 ( r = 1 , s = 0 ) \mathrm { . }$ ,the matrix is called upper (lower) bidiagonal.

To avoid storage of zero elements,the diagonals of a band matrix can be stored either as columns in an array of dimension $n \times w$ or as rows in an array of dimension $w \times n$ . For example,

the matrix in (4.1.3) above can be stored as

$$
\left[ \begin{array} { c c c c } { { \ast } } & { { \ast } } & { { a _ { 1 1 } } } & { { a _ { 1 2 } } } \\ { { \scriptstyle a _ { 2 1 } } } & { { a _ { 2 2 } } } & { { a _ { 2 3 } } } \\ { { a _ { 3 1 } } } & { { a _ { 3 2 } } } & { { a _ { 3 3 } } } & { { a _ { 3 4 } } } \\ { { a _ { 4 2 } } } & { { a _ { 4 3 } } } & { { a _ { 4 4 } } } & { { a _ { 4 5 } } } \\ { { a _ { 5 3 } } } & { { a _ { 5 4 } } } & { { a _ { 5 5 } } } & { { a _ { 5 6 } } } \\ { { a _ { 6 4 } } } & { { a _ { 6 5 } } } & { { a _ { 6 6 } } } & { { \ast } } \end{array} \right] \quad \mathrm { o r } \quad \left[ \begin{array} { c c c c c } { { \ast } } & { { a _ { 1 2 } } } & { { a _ { 2 3 } } } & { { a _ { 3 4 } } } & { { a _ { 4 5 } } } & { { a _ { 5 6 } } } \\ { { a _ { 1 1 } } } & { { a _ { 2 2 } } } & { { a _ { 3 3 } } } & { { a _ { 4 4 } } } & { { a _ { 5 5 } } } & { { a _ { 6 6 } } } \\ { { a _ { 2 1 } } } & { { a _ { 3 2 } } } & { { a _ { 4 3 } } } & { { a _ { 5 4 } } } & { { a _ { 6 5 } } } & { { \ast } } \\ { { a _ { 3 1 } } } & { { a _ { 4 2 } } } & { { a _ { 5 3 } } } & { { a _ { 6 4 } } } & { { \ast } } & { { \ast } } \end{array} \right] .
$$

Except for a few elements indicated by asterisks in the initial and final rows,only nonzero elements of $A$ are stored. Passing along a column in the first storage scheme moves along a diagonal of the matrix,and the rows are aligned. Some elements in the lower right corner are not used. How to perform the subscript computations efciently in algorithms where the matrix is stored in band mode is described in“Contribution $\mathbf { I } / 4 ^ { \mathbf { \mathfrak { s } } }$ of Wilkinson and Reinsch [1123,1971] and in Chapter 4 of Dongarra et al. [322,1979].

It is convenient to use the following MATLAB notation for manipulating band matrices.

Definition 4.1.1. If $a \in \mathbb { R } ^ { n }$ is a vector, then $A = \mathrm { d i a g } \left( a , k \right)$ is a square matrix of order $n + | k |$ with the elements of a on its kth diagonal,where $k = 0$ is the main diagonal, $k > 0$ is above the main diagonal, and $k < 0$ is below the main diagonal. If $A$ is a square matrix of order $n$ ， then $\mathrm { d i a g } \left( A , k \right) \in \mathbb { R } ^ { \left( n - k \right) }$ ， $| k | < n$ , is the column vector consisting of the elements of the kth diagonal of $A$

For example, $\mathrm { d i a g } \left( A , 0 \right)$ is the main diagonal of $A$ ,and if $0 \leq k < n$ ,the $k$ th superdiagonal and subdiagonal of $A$ are

$$
\begin{array} { r } { \mathrm { d i a g } \left( A , k \right) = \left( a _ { 1 , k + 1 } , a _ { 2 , k + 2 } , \ldots , a _ { n - k , n } \right) ^ { T } , } \\ { \mathrm { d i a g } \left( A , - k \right) = \left( a _ { k + 1 , 1 } , a _ { k + 2 , 2 } , \ldots , a _ { n , n - k } \right) ^ { T } . } \end{array}
$$

Clearly, the product of two diagonal matrices $D _ { 1 }$ and $D _ { 2 }$ is another diagonal matrix whose elements are equal to the elementwise product of the diagonals.The following elementary but very useful result shows which diagonals in the product of two square band matrices are nonzero.

Theorem 4.1.2. Let $A \in \mathbb { R } ^ { n \times n }$ and $A _ { 2 } \in \mathbb { R } ^ { n \times n }$ have lower bandwidths $r _ { 1 }$ and $r _ { 2 }$ and upper bandwidths $s _ { 1 }$ and $s _ { 2 }$ ，respectively. Then the products $A B$ and $B A$ have lower and upper bandwidths $r _ { 3 } \le \operatorname* { m i n } \{ r _ { 1 } + r _ { 2 } \}$ and $s _ { 3 } \leq \operatorname* { m i n } \{ s _ { 1 } + s _ { 2 } \}$

Proof. The elements of $C = A B$ are $\begin{array} { r } { c _ { i j } = \sum _ { k = 1 } ^ { n } a _ { i k } b _ { j k } } \end{array}$ . By definition, $a _ { i k } = 0$ if $k > i + r _ { 1 }$ and $b _ { k j } = 0$ if $j > k + r _ { 2 }$ . It follows that $a _ { i k } b _ { j k } = 0$ unless $k \leq i + r _ { 1 }$ and $j \le k + r _ { 2 }$ . But this implies that $k + j \leq i + r _ { 1 } + k + r _ { 2 }$ or $j \leq i + ( r _ { 1 } + r _ { 2 } )$ ,i.e., $C$ has bandwidth at most $r _ { 1 } + r _ { 2 }$ ： The second case follows from the observations that if a matrix has lower bandwidth $r$ ，then $A ^ { T }$ has upper bandwidth $r$ ,and that $( A B ) ^ { T } = B ^ { T } A ^ { T }$ .□

Note that Theorem 4.1.2 holds also for negative values of the bandwidths. For example, a strictly upper triangular matrix $A$ can be said to have lower bandwidth $r = - 1$ . It follows that $A ^ { 2 }$ has lower bandwidth $r = - 2$ ,etc.,and $A ^ { n } = 0$

When the bandwidth of $A \in \mathbb { R } ^ { n \times n }$ and $B \in \mathbb { R } ^ { n \times n }$ are small compared to $n$ the usual algorithms for forming the product $A B$ are not effective on vector computers. Instead, the product can be formed by writing $A$ and $B$ as a sum of their diagonals and multiplying crosswise. For example, if $A$ and $B$ are tridiagonal, then by Theorem 4.1.2 the product $C = A B$ has upper and lower bandwidths two. The five nonzero diagonals of $C$ can be computed by $3 ^ { 2 } = 9$ pointwise vector multiplications independent of $n$

Definition 4.1.3. A square matrix $A \in \mathbb { R } ^ { n \times n }$ ， $n \geq 2$ ，is said to be reducible if there is a partitioning of the index set $\{ 1 , 2 , \ldots , n \}$ into two nonempty disjoint subsets $S$ and $T$ such that $a _ { i j } = 0$ whenever $i \in S$ and $j \in T$ . Otherwise, $A$ is called irreducible. Equivalently, $A$ is reducible if there is a permutation matrix $P$ such that

$$
P ^ { T } A P = \left( \begin{array} { c c } { A _ { 1 1 } } & { A _ { 1 2 } } \\ { 0 } & { A _ { 2 2 } } \end{array} \right) ,
$$

where $A _ { 1 1 }$ and $A _ { 2 2 }$ are nonempty square submatrices.

If $A$ is reducible,then after a permutation the linear system $A x = b$ is reduced to $P ^ { T } A P y =$ $P ^ { T } b = c$ ， $y = P ^ { T } x$ or

$$
A _ { 1 1 } y _ { 1 } + A _ { 1 2 } y _ { 2 } = c _ { 1 } , \qquad A _ { 2 2 } y _ { 2 } = c _ { 2 } .
$$

The original system has been reduced to two smaller sets of equations. Hence,only the diagonal blocks $A _ { 1 1 }$ and $A _ { 2 2 }$ need to be factorized. If again $A _ { 1 1 }$ or $A _ { 2 2 }$ is reducible,then such a reduction can be carried out again.This can be continued until a triangular block form with irreducible diagonal blocks is obtained. This observation motivates the term reducible.

It is well known (see Duf, Erisman,and Reid [344,1986]) that the inverse of any irreducible matrix $A$ is structurally full,i.e.,it is always possible to find numerical values such that all entries in $A ^ { - 1 }$ will be nonzero.In particular, the inverse of an irreducible band matrix in general has no Zero elements. Therefore,it is important to avoid computing the inverse explicitly. Even storing the elements of $A ^ { - 1 }$ may be infeasible.However, if theLU factorization of $A$ can be carried out without pivoting, then the band structure in $A$ is preserved in the LU factors.

Theorem 4.1.4. Let $A$ have lower bandwidth $r$ and upper bandwidth $s$ ， and assume that the factorization $A = L U$ exists.Then,assuming that LU factorization can be carried out without row and columns permutations, $L$ will have lower bandwidth $r$ and $U$ have upper bandwidth $s$

Proof. The proof is by induction. Assume that the first $k - 1$ columns of $L$ and rows of $U$ have bandwidths $r$ and $s$ .Then for $p = 1 { : } k - 1$ ，

$$
l _ { i p } = 0 , \quad i > p + r , \qquad u _ { p j } = 0 , \quad j > p + s .
$$

The assumption is trivially true for $k = 1$ . Since $a _ { k j } = 0$ for $j > k + s$ , (4.1.5) yields

$$
u _ { k j } = a _ { k j } - \sum _ { p = 1 } ^ { k - 1 } l _ { k p } u _ { p j } = 0 - 0 = 0 , \quad j > k + s .
$$

Similarly, it follows that $l _ { i k } = 0$ ， $i > k + r$ , which completes the induction step.

An important but hard problem is to find a reordering of the rows and columns of $A$ that minimizes the bandwidth of the LU or Cholesky factors. However, there are heuristic algorithms that give almost optimal results; see Section 5.1.5.

When $A$ is tridiagonal,

$$
A = \left( \begin{array} { c c c c c c } { { a _ { 1 } } } & { { c _ { 2 } } } & { { } } & { { } } & { { } } & { { } } \\ { { b _ { 2 } } } & { { a _ { 2 } } } & { { c _ { 3 } } } & { { } } & { { } } & { { } } \\ { { } } & { { \ddots } } & { { \ddots } } & { { \ddots } } & { { } } & { { } } \\ { { } } & { { } } & { { b _ { n - 1 } } } & { { a _ { n - 1 } } } & { { c _ { n } } } \\ { { } } & { { } } & { { } } & { { b _ { n } } } & { { a _ { n } } } \end{array} \right) ,
$$

$L$ can be taken to be lower unit bidiagonal with subdiagonal elements $\gamma _ { 2 } , \ldots , \gamma _ { n }$ ,and $U$ to be upper bidiagonal with diagonal $d _ { 1 } , \ldots , d _ { n }$ and superdiagonal $c _ { 2 } , \ldots , c _ { n }$ .Equating elements in $A$ and $L U$ shows that the upper diagonal in $U$ equals that in $A$ . The other elements in $L$ and $U$ are obtained by the following recursion: $d _ { 1 } = a _ { 1 }$ ，

$$
\gamma _ { k } = b _ { k } / d _ { k - 1 } , \qquad d _ { k } = a _ { k } - \gamma _ { k } c _ { k } , \quad k = 2 : n .
$$

Here $\gamma _ { k }$ and $d _ { k }$ can overwrite $b _ { k }$ and $a _ { k }$ , respectively. The solution to the system $A x = L ( U x ) =$ $g$ is then obtained by solving $L y = f$ by forward substitution: $y _ { 1 } = g _ { 1 }$ ，

$$
y _ { i } = g _ { i } - \gamma _ { i } y _ { i - 1 } , \quad i = 2 , \ldots , n ,
$$

and then solving $U x = y$ by back-substitution: $x _ { n } = y _ { n } / d _ { n }$

$$
x _ { i } = ( y _ { i } - c _ { i + 1 } x _ { i + 1 } ) / d _ { i } , \quad i = n - 1 , \ldots , 2 , 1 .
$$

The total number of flops for the factorization is about $3 n$ and is $2 . 5 n$ for the solution of the triangular systems.Note that the divisions in the substitution can be avoided if(4.1.7) is modified to compute $d _ { k } ^ { - 1 }$ . This may be more eficient because on many computers a division takes more time than a multiplication.

# 4.1.2 - Band Cholesky Factorization

Taking advantage of a band structure of $A \in \mathbb { R } ^ { m \times n }$ in a least squares problem $\operatorname* { m i n } _ { x } \| A x - b \| _ { 2 }$ can lead to significant savings.The matrix of normal equations can be formed rowwise as

$$
C = A ^ { T } A = \sum _ { i = 1 } ^ { m } a _ { i } a _ { i } ^ { T }
$$

in about $m w ^ { 2 }$ flops, where $a _ { i } ^ { T }$ ， $i = 1 , \ldots , m$ , denotes the rows of $A$

Lemma 4.1.5. Assume that $A \in \mathbb { R } ^ { m \times n }$ has row bandwidth $w$ .Then $A ^ { T } A$ has upper and lower bandwidths $s = r = w - 1$

Proof. From the definition (4.1.1) of bandwidth it follows that $a _ { i j } a _ { i k } \neq 0 \Rightarrow | j - k | < w$ This implies that

$$
| j - k | \geq w \Rightarrow ( A ^ { T } A ) _ { j k } = \sum _ { i = 1 } ^ { m } a _ { i j } a _ { i k } = 0 ,
$$

and hence $s \leq w - 1$

Theorem 4.1.6. Let $C = L L ^ { T }$ be the Cholesky factorization of the symmetric positive definite band matrix $C$ 、Then the symmetric matrix $L + L ^ { T }$ inherits the band structure of $C$

Proof. The proof is similar to that of Theorem 4.1.4.

The next algorithm computes the Cholesky factor $L$ of a symmetric (Hermitian） positive definite matrix $C$ using a column sweep ordering. Recall that no pivoting is needed for stability. Only the lower triangular part of $A$ is used.

# Algorithm 4.1.1 (Band Cholesky Algorithm).

function L $=$ bcholf(A,r);   
$\%$ BCHOLF computes the lower triangular Cholesky $\%$ factor L of a positive definite Hermitian $\%$ matrix A of upper and lower bandwidth r.   
%   
$\mathrm { ~ n ~ } =$ size(A,1);   
$\begin{array} { r l } & { \mathrm { ~ f o r ~ j ~ = ~ 1 : n ~ } } \\ & { \mathrm { ~ p ~ = ~ m i n ( j + r , n ) ~ ; ~ q ~ = ~ m a x ( 1 , i - r ) ~ ; } } \\ & { \mathrm { ~ i \ k ~ = ~ q _ { \ell } ~ j - 1 ~ ; ~ j ~ n ~ = ~ j + 1 : p ~ ; } } \\ & { \mathrm { ~ A \left( j , j \right) ~ = ~ s q r t \left( A \left( j , j \right) ~ - ~ A \left( j , i k \right) \ast A \left( j , i k \right) ^ { \circ } \right) ~ ; } } \\ & { \mathrm { ~ A \left( j n , j \right) ~ = ~ \mathsf { \Lambda } \left( A \left( j n , j \right) ~ - ~ A \left( j n , i k \right) \ast A \left( j , i k \right) ^ { \circ } \right) / A \left( j , j \right) ~ ; } } \\ & { \mathrm { ~ e n d } } \\ & { \mathrm { ~ L ~ = ~ t r i \mathsf { 1 } \left( A \right) ~ ; } } \end{array}$

If $r \ll n$ , then this algorithm requires about $n r ( r { + 3 } )$ flops and $n$ square roots to compute the Cholesky factor $L$ When $s \ll n$ this is much less than the $n ^ { 3 } / 3$ flops required in the full case. In the semidefinite case, diagonal pivoting is required, which can destroy the band structure.

The least squares solution is obtained by solving the triangular systems $L y = c = A ^ { T } b$ and $L ^ { T } x = y$ by forward- and back-substitution:

$$
\begin{array} { l l } { { y _ { i } = b _ { i } - \displaystyle \sum _ { j = p } ^ { i - 1 } r _ { j i } y _ { j } , } } & { { i = 1 , \ldots , n , \quad p = \operatorname* { m a x } ( 1 , i - r ) , } } \\ { { { } } } & { { { } } } \\ { { { \displaystyle x _ { i } = \left( y _ { i } - \displaystyle \sum _ { j = i + 1 } ^ { q } r _ { i j } x _ { j } \right) / r _ { i i } , } } } & { { i = n , \ldots , 1 , \quad q = \operatorname* { m i n } ( i + r , n ) . } } \end{array}
$$

Effcient band versions of band forward and back-substitution can be derived. Each requires about $2 ( 2 n - r ) ( r + 1 ) \approx 4 n r$ flops and can be organized so that $y$ and, finally, $x$ overwrite $c$ in storage. Thus,if full advantage is taken of the band structure of the matrices involved, the solution of a least squares problem where $A$ has bandwidth $w \ll n$ requires a total of about $( m + n ) w ^ { 2 } + 4 n w$ flops.

Let $A$ be symmetric positive definite and tridiagonal as in (4.1.6) with $c _ { i } = b _ { i }$ ， $i = 2 , \ldots , n$ ， and write the Cholesky factorization in symmetric form as $A = L D L ^ { T }$ ， $D = \operatorname* { d i a g } \left( d _ { 1 } , \ldots , d _ { n } \right)$ Then the elements in $D$ and $L$ are obtained as follows. Set $d _ { 1 } = a _ { 1 }$ ,and

$$
\gamma _ { k } = b _ { k } / d _ { k - 1 } , \qquad d _ { k } = a _ { k } - \gamma _ { k } b _ { k } , \quad k = 2 , \ldots , n .
$$

Eliminating $\gamma _ { k }$ gives

$$
d _ { k } = a _ { k } - b _ { k } ^ { 2 } / d _ { k - 1 } , \quad k = 2 , \ldots , n .
$$

Sometimes it is more convenient to set $L D = U ^ { T }$ and determine the factorization $A = U ^ { T } D ^ { - 1 } U$

# 4.1.3 - Computing Elements of the Covariance Matrix

Methods for computing the covariance matrix

$$
C _ { x } = ( A ^ { T } A ) ^ { - 1 } = ( R ^ { T } R ) ^ { - 1 } = R ^ { - 1 } R ^ { - T }
$$

are given in Section 2.1.5. In the case when $R$ is banded, or generally sparse,an algorithm by Golub and Plemmons [505,1g8o] can be used with great savings to compute all elements of $C _ { x }$ in positions where $R$ has nonzero elements. This includes the diagonal elements of $C _ { x }$ that give the variances of least squares solution $x$ .We denote by $\kappa$ the index set $\{ ( i , j ) \in \mathcal { K } \mid r _ { i j } \neq 0 \}$ Note that because $R$ is the Cholesky factor of $A ^ { T } A$ ,its structure is such that $( i , j ) \in \mathcal { K }$ and $( i , k ) \in \mathcal { K }$ imply that $( j , k ) \in \mathcal { K }$ if $j < k$ and $( k , j ) \in \mathcal { K }$ if $j > k$ .From (4.1.12) it follows that

$$
R C _ { x } = R ^ { - T } ,
$$

where $R ^ { - T }$ is lower triangular with diagonal elements $1 / r _ { i i } , i = 1 , \ldots , n$ . Equating the last columns of the identity (4.1.13) gives

$$
R c _ { n } = r _ { n n } ^ { - 1 } e _ { n } , \quad e _ { n } = ( 0 , \ldots , 0 , 1 ) ^ { T } ,
$$

where $c _ { n }$ is the last column of $C _ { x }$ . From this equation the elements in $c _ { n }$ can be computed by back-substitution, ging $c _ { n n } = r _ { n n } ^ { - 2 }$ and

$$
c _ { i n } = - r _ { i i } \sum _ { \stackrel { j = i + 1 } { ( i , j ) \in { \cal K } } } ^ { n } r _ { i j } c _ { j n } , i = n - 1 , \ldots , 1 .
$$

By symmetry $c _ { n i } = c _ { i n }$ ， $i = 1 , \ldots , n - 1$ ,also the last row of $C _ { x }$ is determined. We only need to save the elements with row indices greater than or equal to the first nonzero element in the $k$ th column of $R$

Now assume that the elements $c _ { i j }$ ， $( i , j ) \in \mathcal { K }$ , in columns $j = n , \ldots , k + 1$ have been computed. Then

$$
c _ { k k } = r _ { k k } ^ { - 1 } \left[ r _ { k k } ^ { - 1 } - \sum _ { j = k + 1 \atop ( k , j ) \in { \cal K } } ^ { n } r _ { k j } c _ { k j } \right] .
$$

Similarly, for $i = k - 1 , \ldots , f _ { k }$ ，

$$
c _ { i k } = - r _ { i i } ^ { - 1 } \left[ \sum _ { \substack { j = i + 1 } } ^ { k } r _ { i j } c _ { j k } + \sum _ { \substack { j = k + 1 } } ^ { n } r _ { i j } c _ { k j } \right] , \quad ( i , k ) \in \mathcal { K } .
$$

If the Cholesky factor $R$ has bandwidth $p$ , then the elements of $C _ { x }$ in the $p + 1$ bands of the upper triangular part of $C _ { x }$ can be computed by the above algorithm in about ${ \scriptstyle { \frac { 2 } { 3 } } } n p ( p + 1 )$ flops. An important particular case is when $R$ is bidiagonal. Computing the two diagonals of $C _ { x }$ then requires only about ${ \begin{array} { l } { { \frac { 4 } { 3 } } n } \end{array} }$ flops.

# 4.1.4 - QR Factorization of a Band Matrix

We now consider how to use the more stable Householder and Givens QR factorizations to solve banded least squares problems. In the standard Householder QR,we set $A ^ { ( 1 ) } = A$ and

$$
A ^ { ( k + 1 ) } = P _ { k } A ^ { ( k ) } , \quad k = 1 , \dots , n ,
$$

where the sequence of Householder reflections $P _ { k }$ is chosen to annihilate the subdiagonal ele-ments in the $k$ th column of $A ^ { ( k ) }$ . As shown by Reid [919, $1 9 6 7 ]$ this will cause each column in the remaining unreduced part of the matrix that has a nonzero inner product with the column being reduced to take on the sparsity pattern of their union. Hence, even though the final $R$ retains the bandwidth of $A$ ,large intermediate fll can take place with consequent cost in operations and storage. Thus, Householder QR factorization of a banded matrix $A \in \mathbb { R } ^ { m \times n }$ of bandwidth $w$ can require as much as 2mnw flops, and the intermediate storage required can exceed by a large amount that needed for the final factors.Note also that forming $Q$ explicitly should be avoided, because this factor may contain an order of magnitude more nonzero elements than either $A$ and $R$ .This rules out the use of MGS (modified Gram-Schmidt) for banded matrices.

For QR factorization of a band matrix, the order in which the rows are processed is critical for efficiency. We say that a band matrix $A$ is in standard form if its rows are ordered so that $f _ { i } ( A ) , i = 1 , 2 , \ldots , m$ , form a nondecreasing sequence

$$
i \leq k \Rightarrow f _ { i } ( A ) \leq f _ { k } ( A ) .
$$

A band matrix $A$ in standard form can be writen in partitioned form as

$$
A = \left( \begin{array} { c } { { A } } \\ { { A _ { 2 } } } \\ { { \vdots } } \\ { { \dot { A } _ { q } } } \end{array} \right) , \qquad b = \left( \begin{array} { c } { { b _ { 1 } } } \\ { { b _ { 2 } } } \\ { { \vdots } } \\ { { b _ { q } } } \end{array} \right) ,
$$

where $A _ { k } \in \mathbb { R } ^ { ( m _ { k } , n ) }$ and $m = m _ { 1 } + \cdot \cdot \cdot + m _ { q }$ Here $A _ { k }$ consists of all rows of $A$ for which the first nonzero element is in column $k$ ， $k = 1 , \ldots , q$ . The row ordering within the blocks $A _ { k }$ may be specified by sorting the rows so that the column indices $l _ { i } ( A _ { k } )$ within each block form a nondecreasing sequence. In many applications, $A$ is naturally given in standard form.

The structure of $A ^ { T } A$ , and therefore of $R$ ,can be generated as follows.

Theorem 4.1.7. Assume that $A \in \mathbb { R } ^ { m \times n }$ is a band matrix in standard form partitioned as in (4.1.17), and let $w _ { k }$ be the bandwidth of the block $A _ { k }$ . Then the band structure of the upper triangular Cholesky factor $R$ is given by $l _ { 1 } ( R ) = w _ { 1 }$ ，

$$
l _ { k } ( R ) = \operatorname* { m a x } \{ w _ { k } + k - 1 , l _ { k - 1 } ( R ) \} , \quad k = 2 , \ldots , q .
$$

Proof. The proof is by induction.

The first efficient QR algorithm for band matrices was given in Chapter 27 of Lawson and Hanson [727,1995]. It uses Householder transformations and assumes that $A$ is partitioned in the form (4.1.17). First, $R = R _ { 0 }$ is initialized to be an empty upper triangular matrix of bandwidth $w$ .The QR factorization proceeds in $q$ steps, $k = 1 , 2 , \ldots , q$ In step $k$ the $k$ th block $A _ { k }$ is merged as follows into the previously computed upper triangular $( R _ { k - 1 } , d _ { k - 1 } )$ by an orthogonal transformation:

$$
\begin{array} { r } { Q _ { k } ^ { T } \left( { \cal A } _ { k } ^ { } - 1 { \cal \Delta } _ { } \right) = \left( { \cal R } _ { k } ^ { } \right) , } \end{array}
$$

where $Q _ { k }$ is a product of Householder reflections giving an upper trapezoidal $R _ { k }$ .Note that this and later steps do not involve the first $k - 1$ rows and columns of $R _ { k - 1 }$ . Hence,at the beginning of step $k$ the first $k - 1$ rows of $R _ { k - 1 }$ are rows in the final matrix $R$ .At termination we have obtained $( R _ { q } , d _ { q } )$ such that $R _ { q } x = d _ { q }$ . This Householder algorithm uses a total of about $2 w ( w + 1 ) ( m + 3 n / 2 )$ fops,

Example 4.1.8. The least squares approximation of a discrete set of data by a linear combination of cubic B-splines is often used for smoothing noisy data values observed at $m$ distinct points; see Reinsch $[ 9 2 2 , 1 9 6 7 ]$ and Craven and Wahba [278,1979]. Let $\begin{array} { r } { s ( t ) = \sum _ { j = 1 } ^ { n } x _ { j } B _ { j } ( t ) } \end{array}$ where

$B _ { j } ( t ) , j = 1 , \ldots , n$ , be normalized cubic B-splines,and let $( y _ { i } , t _ { i } )$ ， $i = 1 , \ldots , m$ , be given data points. Determine $x$ to minimize

$$
\sum _ { i = 1 } ^ { m } ( s ( t _ { i } ) - y _ { i } ) ^ { 2 } = \| A x - y \| _ { 2 } ^ { 2 } .
$$

The only B-splines with nonzero values for $t \in [ \lambda _ { k - 1 } , \lambda _ { k } ]$ are $B _ { j }$ ， $j = k , k + 1 , k + 2 , k + 3$ Hence $A$ will be a band matrix with $w = 4$ .For a problem with $m = 1 7$ ， $n = 1 0$ ， $A$ consists of blocks $A _ { k }$ ， $k = 1 , \ldots , 7 .$ ，The Householder QR factorization is illustrated in Figure 4.1.1,where $A$ is shown after the first three blocks have been reduced by Householder reflections $P _ { 1 } , \ldots , P _ { 9 }$ Elements zeroed by $P _ { j }$ are denoted by $j$ and fill elements by $^ +$

We now describe an alternative algorithm using plane rotations for the QR factorization of a band matrix.

# Algorithm 4.1.2 (Sequential Givens QR Factorization).

Let $A \in \mathbb { R } ^ { m \times n }$ be a band matrix in standard form with row bandwidth w. Initialize $R = R _ { 0 }$ to be an upper triangular matrix of bandwidth w with zero elements. For $i = 1 , \ldots , m$ plane rotations are used to merge the ith row with $R _ { i - 1 }$ ，giving $R _ { i }$

$$
[ c , s ] = \operatorname { g i v r o t } ( r _ { j j } , a _ { i j } ) ;
$$

$$
\binom { r _ { j } ^ { T } } { a _ { i } ^ { T } } : = \left( \begin{array} { l l } { c } & { s } \\ { - s } & { c } \end{array} \right) \left( \begin{array} { l } { r _ { j } ^ { T } } \\ { a _ { i } ^ { T } } \end{array} \right) ;
$$

The reduction is shown schematically in Figure 4.1.1. The ith step only involves the $w \times w$ upper triangular part of $R _ { i - 1 }$ formed by rows and columns $f _ { i } ( A )$ to $l _ { i } ( A )$ . If at some stage $r _ { i i } = 0$ ,then the whole ith row in $R _ { i - 1 }$ must be zero,and the remaining part of the current row $a _ { i } ^ { T }$ can just be copied into row $i$ of $R _ { i - 1 }$

If $A$ has constant bandwidth and is in standard form, then at step $i$ the last $\left( n - l _ { i } ( A ) \right)$ columns of $R$ have not been touched and are still zero as initialized. Furthermore,at this stage the first $\left( f _ { i } ( A ) - 1 \right)$ rows are final rows of $R$ and can be saved on secondary storage. Since primary storage is only needed for the active triangular part, shown in Figure 4.1.2, very large problems can be handled. Clearly, the number of plane rotations needed to process the $i$ th row isatmost $\operatorname* { m i n } ( i - 1 , w )$ and requires at most $4 w ^ { 2 }$ flops. Hence, the complete factorization requires $4 m w ^ { 2 }$ flops, and $\scriptstyle { \frac { 1 } { 2 } } w ( w + 3 )$ locations of storage.We remark that if $A$ is not in standard form,then the operation count can only be bounded by 4mnw flops.

![](../chunks/Numerical Methods for Least Squares Problems (Åke Björck) (z-library.sk, 1lib.sk, z-lib.sk_part_0003_pages_0141-0210/auto/images/eee64f745374c9543834497f509aff633e2fbac0b9051fe4a4af6853cbb67e25.jpg)  
Figure 4.1.2. Reduction of a band matrix.

The solution to a band least squares problem $\mathrm { m i n } _ { x } \| A x - b \| _ { 2 }$ is obtained by applying QR factorization to the extended matrix $( A b )$ . The solution is then obtained from a band upper triangular system $R x = c _ { 1 }$ . In order to treat additional right-hand sides not available at the time of factorization,the plane rotations from the QR factorization need to be saved.As described in Section 2.2.1,a plane rotation can be represented by a single floating-point number. Since at most $w$ rotations are needed to process each row, it follows that $Q$ can be stored in no more space than that allocated for $A$

# 4.2 - Bidiagonalization

# 4.2.1 - Bidiagonal Decomposition

For a general $m \times n$ matrix $A$ ,the closest-to-diagonal form that can be achieved in a finite number of operations is a bidiagonal form. Golub and Kahan [495,1965] show that this form can be obtained by a sequence of two-sided Householder reflections $B = U ^ { T } A V$ ，where $U \in \mathbb { R } ^ { m \times m }$ and $V \in \mathbb { R } ^ { n \times n }$ are orthogonal. This preserves the singular values of $A$ ,and the singular vectors of $B$ are closely related to those of $A$ .Householder bidiagonalization (HHBD) is often the first step toward computing the SVD (singular value decomposition); see Section 7.1.1.

Theorem 4.2.1 (HHBD). For any matrix $A \in \mathbb { R } ^ { m \times n }$ , orthogonal matrices $U = ( u _ { 1 } , \ldots , u _ { m } ) \in$ $\mathbb { R } ^ { m \times m }$ and $V = ( v _ { 1 } , \ldots , v _ { n } ) \in \mathbb { R } ^ { n \times n }$ can be found such that $U ^ { T } A V$ is upper bidiagonal. If $m \geq n$ ,then

$$
U ^ { T } A V = \left( \begin{array} { l } { B } \\ { 0 } \end{array} \right) , \quad B = \left( \begin{array} { l l l l l } { \beta _ { 1 } } & { \alpha _ { 2 } } & & & \\ & { \beta _ { 2 } } & { \alpha _ { 3 } } & & \\ & & { \ddots } & { \ddots } & \\ & & & { \beta _ { p - 1 } } & { \alpha _ { p } } \\ & & & & { \beta _ { p } } \end{array} \right) \in \mathbb { R } ^ { p \times p } ,
$$

where $\beta _ { i } \ \ge \ 0 , \ \alpha _ { i } \ \ge \ 0 ,$ and $\textit { p } = \textit { n }$ if $m \ < \ n$ ，then $U ^ { T } A V = \left( \begin{array} { c c } { { B } } & { { 0 } } \end{array} \right)$ ，where $p \ = \ m$ B ∈ Rpx(p+1),and Bep+1 = ap+1ep.

Proof. $U$ and $V$ are constructed as products of Householder reflectors $Q _ { k } \in \mathbb { R } ^ { m \times m }$ from the left and $P _ { k } \in \mathbb { R } ^ { n \times n }$ ， $k = 1 , \hdots , p$ , from the right, applied alternately to $A$ .Here $Q _ { k }$ is chosen to zero out all elements in the $k$ th column below the main diagonal,and $P _ { k }$ is chosen to zero out all elements in the $k$ th row to the right of $B$ .First, $Q _ { 1 }$ is applied to $A$ to zero out all elements, except one in the first column of $Q _ { 1 } A$ .When $P _ { 1 }$ is next applied to zero out the elements in the first row not in $B$ ,the first column in $Q _ { 1 } A$ is left unchanged. These two transformations determine $\beta _ { 1 }$ and $\alpha _ { 2 }$ . All later steps are similar. With $A ^ { ( 1 ) } = \bar { A }$ set $A ^ { ( k + 1 ) } = ( Q _ { k } A ^ { ( k ) } ) P _ { k }$ . This determines not only the bidiagonal elements $\beta _ { k }$ and $\alpha _ { k + 1 }$ in the $k$ th row of $B$ but also the $k$ th columns in $U$ and $V$ ：

$$
u _ { k } = U e _ { k } = Q _ { 1 } \ldots Q _ { k } e _ { k } , \qquad v _ { k } = V e _ { k } = P _ { 1 } \ldots P _ { k } e _ { k } , \quad k = 1 , \ldots , p .
$$

Here, some of the transformations may be skipped. For example, if $m = n$ ,then $Q _ { n } = I _ { n }$ and $P _ { n - 1 } = P _ { n } = I _ { n }$ . Similarly,a complex matrix $A \in \mathbb { C } ^ { m \times n }$ can be reduced to real bidiagonal form using a sequence of complex Householder reflections. □

By applying the HHBD algorithm of Theorem 4.2.1 to $A ^ { T }$ , any matrix $A \in \mathbb { R } ^ { m \times n }$ can be transformed into lower bidiagonal form. (This is equivalent to starting the reduction of $A$ with a right transformation $P _ { 1 }$ instead of with $Q _ { 1 }$ .）

HHBD requires approximately $4 ( m n ^ { 2 } - { \textstyle { \frac { 1 } { 3 } } } n ^ { 3 } )$ flops or roughly twice as many as needed for Householder QR factorization. If the matrices $U _ { p } = ( u _ { 1 } , \ldots , u _ { p } )$ and/or $V _ { p } = ( v _ { 1 } , \ldots , v _ { p } )$ are wanted,the corresponding products of Householder reflections can be accumulated at a cost of $2 ( m n ^ { 2 } - { \textstyle \frac { 1 } { 3 } } n ^ { 3 } ) $ and ${ \scriptstyle { \frac { 4 } { 3 } } } n ^ { 3 }$ fops, respectively. For a square matrix, these counts are ${ \scriptstyle { \frac { 8 } { 3 } } } n ^ { 3 }$ for the reduction and ${ \scriptstyle { \frac { 4 } { 3 } } } n ^ { 3 }$ for computing each of the matrices $U$ and $V$

HHBD is a backward stable algorithm, i.e.,the computed matrix $B$ is the exact result for a matrix $A + E$ ,where

$$
\| E \| _ { F } \leq c n ^ { 2 } \mathbf { u } \| A \| _ { F } ,
$$

and $c$ is a constant of order unity. Further,if the stored Householder vectors are used to generate $U$ and $V$ explicitly, the computed matrices are close to the exact matrices $U$ and $V$ that reduce $A + E$ . This guarantees that the computed singular values of $B$ and the transformed singular vectors of $B$ are those of a matrix close to $A$

An alternative two-step reduction to bidiagonal form was suggested by Lawson and Han-son [727,1995l and later analyzed by T. Chan [222,1982]. This first computes the pivoted QR factorization

$$
A P = Q \left( { \begin{array} { c } { R } \\ { 0 } \end{array} } \right)
$$

and then transforms the upper triangular $R \in \mathbb { R } ^ { n \times n }$ into bidiagonal form. Column pivoting in the initial QR factorization makes the two-step algorithm potentially more accurate. Householder bidiagonalization cannot take advantage of the triangular structure of $R$ ,but with plane rotations it can be done.In the first step the elements $r _ { 1 n } , \ldots , r _ { 1 3 }$ in the first row are annihilated in this order. To zero out element $r _ { 1 j }$ a plane rotation $G _ { j - 1 , j }$ is first applied from the right.This introduces a new nonzero element ${ r _ { j , j - 1 } }$ , which is annihilated by a rotation $\tilde { G } _ { j - 1 , j }$ from the left. The first few rotations in the process are pictured below. (Recall that $\oplus$ denotes the element to be zeroed,and fill-in elements are denoted by $^ +$ ）

$$
\left( { \begin{array} { l l l l l } { \times } & { \times } & { \times } & { \times } & { \oplus } \\ { \times } & { \times } & { \times } & { \times } & { \oplus } \\ & { \times } & { \times } & { \times } & { \times } \\ & & { \times } & { \times } & { \times } \\ & & { + } & { \times } & { \to } \end{array} } \right) \Rightarrow \quad \left( { \begin{array} { l l l l l } { \times } & { \times } & { \times } & { \times } & { 0 } \\ & { \times } & { \times } & { \times } & { \times } \\ & & { \times } & { \times } & { \times } \\ & & & { \times } & { \times } \\ & & & { \oplus } & { \times } \end{array} } \right) \Rightarrow \quad \left( { \begin{array} { l l l l l } { \times } & { \times } & { \times } & { \oplus } & { 0 } \\ & { \times } & { \times } & { \times } & { \times } \\ & & { \times } & { \times } & { \times } \\ & & { + } & { \times } & { \times } \\ & & { 0 } & { \times } \end{array} } \right) .
$$

Two plane rotations are needed to zero each element. The total cost is $6 n$ flops,and the operation count for the reduction of $R$ to bidiagonal form is $2 n ^ { 3 }$ flops and lower than for the Householder algorithm. However, if the product of either the left or right transformation is needed, then Householder reduction requires less work; see Chan [222,1982]. A similar “zero chasing" technique can be used to reduce the bandwidth of an upper triangular band matrix while preserving the band structure; see Golub,Luk,and Overton [498,1981].

The bidiagonal decomposition is a powerful tool for analyzing and solving least squares problems. Let $U ^ { T } A V = C$ ,where $U$ and $V$ are square orthogonal matrices. Then the pseudoinverses of $A$ and $C$ are related as $A ^ { \dagger } = V C ^ { \dagger } U ^ { T }$ ,and the pseudoinverse solution is

$$
x = A ^ { \dagger } b = V ( C ^ { \dagger } ( U ^ { T } b ) ) .
$$

In particular, consider the HHBD algorithm with $A \in \mathbb { R } ^ { m \times n }$ $m \ge n = \operatorname { r a n k } ( A )$ Setting $x = V y$ and using the orthogonal invariance of the 2-norm, we have

$$
\begin{array} { r l } & { \| A x - b \| _ { 2 } ^ { 2 } = \| U ^ { T } A V y - U ^ { T } b \| _ { 2 } ^ { 2 } = \bigg \| \left( \begin{array} { l } { B } \\ { 0 } \end{array} \right) y - \left( \begin{array} { l } { c } \\ { d } \end{array} \right) \bigg \| _ { 2 } ^ { 2 } } \\ & { \qquad = \| B y - c \| _ { 2 } ^ { 2 } + \| d \| _ { 2 } ^ { 2 } . } \end{array}
$$

Clearly, the minimum of $\| A x - b \| _ { 2 } ^ { 2 }$ is obtained when $\mathit { B y } \ : = \ : c$ ，The least squares solution $x = V y = P _ { 1 } \cdot \cdot \cdot P _ { n - 2 } y$ is computed by forming $U ^ { T } b = Q _ { n } \cdot \cdot \cdot Q _ { 1 } b$ and solving $B y = c$ by back-substitution:

$$
y _ { n } = c _ { n } / \beta _ { n } , y _ { k } = ( c _ { k } - \alpha _ { k + 1 } c _ { k - 1 } ) / \beta _ { k } , k = n - 1 : - 1 : 1 .
$$

This takes $2 ( m n + n ^ { 2 } )$ flops. Computing the residual vector

$$
r = Q _ { 1 } \cdot \cdot \cdot Q _ { n } \binom { 0 } { d }
$$

needs an additional $4 m n - 2 n ^ { 2 }$ flops. Computing $r = b - A x$ directly requires mn flops.

To be efficient on modern computers,a blocked version of Householder bidiagonalization is needed.This poses new diffculties that are not present in the blocked Householder QR factorization described in Section 2.6.1.A blocked implementation of Householder bidiagonalization is given by Dongarra, Sorensen,and Hammarling [327,1989l; see also Dongarra et al. [323, 2018,Algorithm 1]. Householder reflectors $H _ { k } = I - \tau _ { k } v _ { k } v _ { k } ^ { T }$ are used to eliminate elements below the diagonal in column $k$ ，while $G _ { k } = I - \pi _ { k } u _ { k } u _ { k } ^ { T }$ eliminate elements to the right of the superdiagonal in row $k$ ：

$$
\begin{array} { r l } & { A ^ { ( k ) } = H _ { k } A ^ { ( k - 1 ) } G _ { k } = ( I - \tau _ { k } v _ { k } v _ { k } ^ { T } ) A ^ { ( k - 1 ) } ( I - \pi _ { k } u _ { k } u _ { k } ^ { T } ) } \\ & { \qquad = A ^ { ( k - 1 ) } - v _ { k } y _ { k } ^ { T } - z _ { k } u _ { k } ^ { T } , } \end{array}
$$

where $y _ { k } = \tau _ { k } ( A ^ { ( k - 1 ) } ) ^ { T } v _ { k }$ and $z _ { k } = \pi _ { k } ( A ^ { ( k - 1 ) } u _ { k } - ( y _ { k } ^ { T } u _ { k } ) v _ { k } )$ . Blocking together $p$ applications gives

$$
A ^ { ( p ) } = H _ { p } \cdot \cdot \cdot H _ { 1 } A G _ { 1 } \cdot \cdot \cdot G _ { p } = A - V _ { p } Y _ { p } ^ { T } - X _ { p } U _ { p } ^ { T } .
$$

To determine $H _ { k }$ it suffices to update column $k$ of the trailing matrix $A ^ { ( k - 1 ) }$ ,and $G _ { k }$ can be determined after row $i$ of $H _ { k } A ^ { ( k - 1 ) }$ is updated. The remaining update of the trailing matrix can be delayed, but each step still requires two matrix-vector products involving the full trailing matrix. If $m = n$ ,then about one half of the total $8 n ^ { 3 } / 3$ flops in the decomposition will be matrix-vector and the other half matrix-matrix operations.

# Notes and references

Ralha [909,2oo3] developed a one-sided bidiagonalization algorithm that starts by computing the factorization $F = A V$ . Here $V$ is a product of Householder reflections chosen so that $T = V ^ { T } A ^ { T } A V$ is tridiagonal but without explicitly forming $A ^ { T } A$ Next, a Gram-Schmidt QR of $F$ is used to compute $F = A V = U B$ ，where $B$ is upper bidiagonal. Ralha's algorithm uses fewer arithmetic operations than the two-sided Householder algorithm but lacks numerical stability. A modified backward stable version of Ralha's algorithm was developed by Barlow, Bosner,and Drmac [71, 2005].

# 4.2.2 - Core Problems by Bidiagonalization

Consider the least squares problem

$$
\operatorname* { m i n } _ { x } \| A x - b \| _ { 2 } .
$$

Suppose $U \in \mathbb { R } ^ { m \times m }$ and $V \in \mathbb { R } ^ { n \times n }$ can be found so that

$$
U ^ { T } \left( \textit { b } | \textit { A V } \right) = \left( \begin{array} { c } { c _ { 1 } } \\ { 0 } \end{array} \bigg | \begin{array} { c c } { A _ { 1 1 } } & { 0 } \\ { 0 } & { A _ { 2 2 } } \end{array} \right) .
$$

Setting $x = V y$ ,the problem splits (4.2.8) into two independent approximation subproblems

$$
\operatorname* { m i n } _ { y _ { 1 } } \| A _ { 1 1 } y _ { 1 } - c _ { 1 } \| _ { 2 } , \quad \operatorname* { m i n } _ { y _ { 2 } } \| A _ { 2 2 } y _ { 2 } \| _ { 2 } , \quad y = \left( { y _ { 1 } } \atop { y _ { 2 } } \right) ,
$$

where $A _ { 1 1 }$ and $A _ { 2 2 }$ may be rectangular. Clearly, the solution to the second subproblem is $y _ { 2 } = 0$ Hence,all information needed for solving the original approximation problem is contained in the first subproblem. The pseudoinverse solution $x ^ { \dagger }$ of the original problem (4.2.8) is related to the pseudoinverse solution $y ^ { \dagger }$ of the transformed problem (4.2.10) by

$$
x ^ { \dagger } = V _ { 1 } y _ { 1 } ^ { \dagger } , \quad V = \left( V _ { 1 } \quad V _ { 2 } \right) .
$$

Paige and Strakos [868, 2oo6] state the following definition.

Definition 4.2.2. The subproblem $\operatorname* { m i n } _ { y } \| A _ { 1 1 } y - c _ { 1 } \| _ { 2 }$ in (4.2.10) is said to be a core problem of $\operatorname* { m i n } _ { x }$ $\| A x - b \| _ { 2 }$ if $A _ { 1 1 }$ is minimally dimensioned for all orthogonal $U$ and $V$ that give the form (4.2.9).

We now show that a core subproblem can be found by bidiagonalization of the compound matrix $\left( \begin{array} { l l } { b } & { A } \end{array} \right)$ ，where $A \in \mathbb { R } ^ { m \times n }$ ， $m > n$ (Note that here $b$ is placed in front of $A$ contrary to our previous practice!) This yields an upper bidiagonal decomposition $U ^ { T } \left( \textit { b } | \textit { A } \right) \widetilde { V }$ Because $\widetilde { V }$ does not act on the first column $b$ , we can write

$$
U ^ { T } (  \ b \ | \ A \ ) ( \begin{array} { c c } { { 1 } } & { { 0 } } \\ { { 0 } } & { { V } } \end{array} ) = ( \ \beta _ { 1 } e _ { 1 } \ | \ U ^ { T } A V \ ) .
$$

Hence $U ^ { T } b = \beta _ { 1 } e _ { 1 }$ ， so that $\beta _ { 1 } = \| b \| _ { 2 }$ and $u _ { 1 } = U e _ { 1 } = b / \beta _ { 1 }$ .Further, we have the lower bidiagonal decomposition,

$$
U ^ { T } A V = { \binom { B } { 0 } } , \quad B = \left( { \begin{array} { c c c c c } { \alpha _ { 1 } } & & & & \\ { \beta _ { 2 } } & { \alpha _ { 2 } } & & & \\ & { \ddots } & { \ddots } & & \\ & & { \beta _ { n } } & { \alpha _ { n } } \\ & & & & { \beta _ { n + 1 } } \end{array} } \right) \in \mathbb { R } ^ { ( n + 1 ) \times n } .
$$

The bidiagonalization process is terminated when the first zero bidiagonal element in $B$ is encountered. Then a core problem has been found. There are two possible cases. If $\alpha _ { k } > 0$ but $\beta _ { k + 1 } = 0$ ， $k \leq n$ , then the transformed matrix splits as follows:

$$
U ^ { T } \left( \textit { b } | \textit { A V } \right) = \left( \begin{array} { c c } { \beta _ { 1 } e _ { 1 } } \\ { 0 } \end{array} \left| \begin{array} { c c } { B _ { 1 1 } } & { 0 } \\ { 0 } & { A _ { 2 2 } } \end{array} \right. \right) ,
$$

where

$$
B _ { 1 1 } = \left( \begin{array} { l l l l } { \alpha _ { 1 } } & & & \\ { \beta _ { 2 } } & { \alpha _ { 2 } } & & \\ & { \ddots } & { \ddots } & \\ & & { \beta _ { k } } & { \alpha _ { k } } \end{array} \right) \in \mathbb { R } ^ { k \times k }
$$

has full row rank, and $A _ { 2 2 }$ is the part of $A$ that is not yet in bidiagonal form. The pseudoinverse solution $x = V y$ is now found by solving the square nonsingular lower bidiagonal core system

$$
B _ { 1 1 } y _ { 1 } = \beta _ { 1 } e _ { 1 }
$$

and setting $x ^ { \dagger } = V _ { 1 } y _ { 1 }$ ; see (4.2.11). Because the residual for (4.2.16) is zero,it follows that the original system $A x = b$ must be consistent.

If instead the bidiagonalization terminates with $\beta _ { k + 1 } ~ > ~ 0$ and $\alpha _ { k + 1 } = 0$ ，then the firs columns of the transformed matrix split with a rectangular lower bidiagonal matrix of ful :olumn rank,

$$
B _ { 1 1 } = \left( \begin{array} { l l l l l } { \alpha _ { 1 } } & & & & \\ { \beta _ { 2 } } & { \alpha _ { 2 } } & & & \\ & { \ddots } & { \ddots } & & \\ & & { \beta _ { k } } & { \alpha _ { k } } \\ & & & & { \beta _ { k + 1 } } \end{array} \right) \in \mathbb { R } ^ { { ( k + 1 ) } \times { k } } .
$$


<!-- chunk 0004: pages 211-280 -->
The least squares core problem is then

$$
\operatorname* { m i n } _ { y _ { 1 } } \| B _ { 1 1 } y _ { 1 } - \beta _ { 1 } e _ { 1 } \| _ { 2 } .
$$

The solution can be found effciently by a QR factorization of $B _ { 1 1 }$ .Proof that systems (4.2.16) and (4.2.18) are minimally dimensioned, and therefore core problems,is given by Paige and Strakos [868,20o6,Theorems 3.2 and 3.3].

# Notes and references

Core problems play an important role in a unified treatment of the scaled TLS (STLS) problem; see Paige and Strakos [867,2002],[868, 20o6]. Hnetynková et al. [630,2011] give a new clas-sification of multivariate TLS problems $A X \approx B$ that reveals subtleties not captured previously. The definition of the core problem is extended to the multiple right-hand side case $A X \approx B$ by Plesinger [899,20o8] and Hnetynkova, Plesinger, and Strakos [632,2013], [633, 2015].

# 4.2.3 - Golub-Kahan-Lanczos Bidiagonalization

When $A$ is large and sparse,Householder bidiagonalization is not effcient because any sparsity in $A$ is usually destroyed in the early intermediate steps. Golub and Kahan [495,1965l give an alternative algorithm that generates the elements in $B$ and the columns of $U$ and $V$ sequentially and only uses matrix-vector products with $A$ and $A ^ { T }$ . We call this algorithm Golub-Kahan-Lanczos bidiagonalization (GKLBD） because of its close relationship to symmetric Lanczos tridiagonalization of the symmetric matrix

$$
\left( \begin{array} { l l } { 0 } & { A } \\ { A ^ { T } } & { 0 } \end{array} \right)
$$

with special starting vectors.

By Theorem 4.2.1 it follows that the existence of orthogonal $U \in \mathbb { R } ^ { m \times m }$ and $V \in \mathbb { R } ^ { n \times n }$ is such that $U ^ { T } A V$ is upper or lower bidiagonal. Then we have

$$
\begin{array} { r l } & { A \left( \begin{array} { l } { v _ { 1 } , v _ { 2 } , v _ { 3 } , \ldots } \end{array} \right) = \left( \begin{array} { l l } { u _ { 1 } , u _ { 2 } , u _ { 3 } , \ldots } \end{array} \right) \left( \begin{array} { l l } { B } & { 0 } \\ { 0 } & { 0 } \end{array} \right) , } \\ & { A ^ { T } \left( \begin{array} { l l } { u _ { 1 } , u _ { 2 } , u _ { 3 } , \ldots } \end{array} \right) = \left( \begin{array} { l l } { v _ { 1 } , v _ { 2 } , v _ { 3 } , \ldots } \end{array} \right) \left( \begin{array} { l l } { B ^ { T } } & { 0 } \\ { 0 } & { 0 } \end{array} \right) , } \end{array}
$$

where some of the zero blocks may be empty. Assume now that $B$ is lower bidiagonal,

$$
B = \left( \begin{array} { c c c c c } { { \alpha _ { 1 } } } & { { } } & { { } } & { { } } & { { } } \\ { { \beta _ { 2 } } } & { { \alpha _ { 2 } } } & { { } } & { { } } & { { } } \\ { { } } & { { \beta _ { 3 } } } & { { \ddots } } & { { } } & { { } } \\ { { } } & { { } } & { { \ddots } } & { { } } & { { \alpha _ { n } } } \\ { { } } & { { } } & { { } } & { { } } & { { \beta _ { n + 1 } } } \end{array} \right) .
$$

Equating columns on both sides of equations (4.2.19)-(4.2.20) gives $\alpha _ { 1 } v _ { 1 } = A ^ { T } u _ { 1 }$ ，

$$
\begin{array} { l } { A v _ { k } = \beta _ { k + 1 } u _ { k + 1 } + \alpha _ { k } u _ { k } , } \\ { A ^ { T } u _ { k + 1 } = \alpha _ { k + 1 } v _ { k + 1 } + \beta _ { k + 1 } v _ { k } , \quad k = 1 , \ldots , n . } \end{array}
$$

Given an initial unit vector $u _ { 1 } \in \mathbb { R } ^ { m }$ , this yields an iterative process for generating $U$ and $V$ columnwise and $B$ rowwise from

$$
\begin{array} { l } { \beta _ { k + 1 } u _ { k + 1 } = A v _ { k } - \alpha _ { k } u _ { k } , } \\ { \alpha _ { k + 1 } v _ { k + 1 } = A ^ { T } u _ { k + 1 } - \beta _ { k + 1 } v _ { k } , \quad k = 1 , 2 , \ldots , } \end{array}
$$

where $\beta _ { k + 1 }$ and $\alpha _ { k + 1 }$ are normalization constants.As long as no zero bidiagonal element occurs, the choice of $u _ { 1 }$ uniquely determines this process. It terminates with a core subproblem when the first zero bidiagonal element is encountered. After $k$ steps the recurrence relations (4.2.23)- (4.2.24) can be summarized in matrix form as

$$
\begin{array} { l } { A V _ { k } = U _ { k + 1 } B _ { k } , } \\ { A ^ { T } U _ { k + 1 } = V _ { k } B _ { k } ^ { T } + \alpha _ { k + 1 } v _ { k + 1 } e _ { k + 1 } ^ { T } . } \end{array}
$$

The Bidiag1 algorithm of Paige and Saunders [866,1982] is obtained for the special starting vector

$$
u _ { 1 } = b / \beta _ { 1 } , \quad \beta _ { 1 } = \| b \| _ { 2 } .
$$

In exact arithmetic, it generates the same lower bidiagonal decomposition of $A$ as HHBD, transforming $\left( \begin{array} { l l } { b } & { A } \end{array} \right)$ into upper bidiagonal form.Bidiag1 is the basis of the important iterative least squares algorithm LSQR of Paige and Saunders [866,1982].

A similar GKLBD processcan be devisedfor the case when $U ^ { T } A V = R$ is upper bidiagonal,

$$
R = \left( \begin{array} { c c c c c c } { { \rho _ { 1 } } } & { { \gamma _ { 2 } } } & { { } } & { { } } & { { } } & { { } } \\ { { } } & { { \rho _ { 2 } } } & { { \gamma _ { 3 } } } & { { } } & { { } } & { { } } \\ { { } } & { { } } & { { \rho _ { 3 } } } & { { \ddots } } & { { } } & { { } } \\ { { } } & { { } } & { { } } & { { \ddots } } & { { \gamma _ { n } } } \\ { { } } & { { } } & { { } } & { { } } & { { } } & { { \rho _ { n } } } \end{array} \right) .
$$

Given an initial unit vector $v _ { 1 } \in \mathbb { R } ^ { n }$ ,equating columns in(4.2.19)-(4.2.20)yields $A v _ { 1 } = \rho _ { 1 } u _ { 1 }$ ，

$$
\begin{array} { l } { { A ^ { T } u _ { k } = \rho _ { k } v _ { k } + \gamma _ { k + 1 } v _ { k + 1 } , } } \\ { { \ } } \\ { { A v _ { k } = \gamma _ { k } u _ { k - 1 } + \rho _ { k } u _ { k } , \quad k = 1 , 2 , \ldots , n - 1 . } } \end{array}
$$

These equations can be used to generate not only successive columns in $U$ and $V$ but also the columns of $R$ . As long as no zero bidiagonal element is encountered,we have

$$
\begin{array} { l } { \gamma _ { k + 1 } v _ { k + 1 } = A ^ { T } u _ { k } - \rho _ { k } v _ { k } , } \\ { \qquad } \\ { \rho _ { k + 1 } u _ { k + 1 } = A v _ { k + 1 } - \gamma _ { k + 1 } u _ { k } , \quad k = 1 , 2 , \ldots . } \end{array}
$$

These equations uniquely determine $v _ { k + 1 }$ and $u _ { k + 1 }$ as_ well as $\gamma _ { k + 1 }$ and $\rho _ { k + 1 }$ After $k$ steps this process has generated $U _ { k } \in \mathbb { R } ^ { m \times k }$ and $V _ { k } \in \mathbb { R } ^ { n \times k }$ and a square upper bidiagonal matrix $R _ { k } \in \mathbb { R } ^ { k \times k }$ such that

$$
\begin{array} { l } { { A V _ { k } = U _ { k } R _ { k } , } } \\ { { \ A ^ { T } U _ { k } = V _ { k } R _ { k } ^ { T } + \gamma _ { k + 1 } v _ { k + 1 } e _ { k } ^ { T } . } } \end{array}
$$

Taking the initial vector to be $v _ { 1 } = A ^ { T } b / \gamma _ { 1 }$ ， $\gamma _ { 1 } = \| A ^ { T } b \| _ { 2 }$ , gives the Bidiag2 algorithm of Paige and Saunders [866,1982]. In exact arithmetic, this generates the same quantities as HHBD, transforming $\left( A ^ { T } b \quad A ^ { T } \right)$ into upper bidiagonal form.

In finite-precision arithmetic there can be a severe loss of orthogonality in $U _ { k }$ and $V _ { k }$ computed by both forms of GKLBD. One effect is that the finite termination property of HHBD is lost; see Section 6.2.5.

# 4.2.4 - Bidiagonalization and Krylov Subspaces

GKLBD generates vectors by repeated matrix-vector products with a fixed matrix. Such vectors span subspaces of a particular structure called Krylov subspaces. Let $C \in \mathbb { R } ^ { n \times n }$ be a given square matrix,and let $v \in \mathbb { R } ^ { n }$ be a given nonzero vector. The sequence of vectors $v , C v , C ^ { 2 } v$ ， $C ^ { 3 } v , \ldots$ is called a Krylov sequence and is easily generated recursively by $v _ { 1 } = v$ ， $v _ { k } = C v _ { k - 1 }$ ， $k = 2 , 3 , \ldots .$ The subspace spanned by the frst $k$ vectors is called a Krylov subspace, denoted by

$$
{ \mathcal K } _ { k } ( C , v ) = \operatorname { s p a n } \{ v , C v , \ldots , C ^ { k - 1 } v \} .
$$

Such subspaces with $C = A ^ { T } A$ or $C = A A ^ { T }$ play a fundamental role in methods for solving large-scale least squares problems.

There can be at most $n$ linearly independent vectors in $\mathbb { R } ^ { n }$ . Hence,in any Krylov sequence $v , C v , C ^ { 2 } v , C ^ { 3 } v , \ldots$ there is a first vector ${ \cal C } ^ { p + 1 } v , p \le n$ ,that is a linear combination of the preceding ones.Then

$$
\begin{array} { r } { \mathcal { K } _ { p + 1 } ( C , v ) = \mathcal { K } _ { p } ( C , v ) , } \end{array}
$$

and the Krylov sequence terminates. The maximum dimension $p$ of $\mathcal { K } _ { k } ( C , v )$ is called the grade of $v$ with respect to $C$ .From (4.2.34) it follows that at termination, ${ \cal { K } } _ { p } ( C , v )$ is an invariant subspace of $C$ . Conversely, if the vector $v$ lies in an invariant subspace of $C$ of dimension $p$ ,its Krylov sequence terminates for $k = p$

Krylov subspaces satisfy the following easily verified invariance properties:

1. Scaling: $\mathcal { K } _ { m } ( \beta C , \alpha v ) = \mathcal { K } _ { m } ( C , v ) , \alpha \neq 0 , \beta \neq 0 .$

2. Translation: $\begin{array} { r } { \mathcal { K } _ { m } ( C - \mu I , v ) = \mathcal { K } _ { m } ( C , v ) . } \end{array}$ 3. Similarity: $\begin{array} { r } { \mathcal { K } _ { m } ( U ^ { H } C U , U ^ { H } v ) = U ^ { H } \mathcal { K } _ { m } ( C , v ) } \end{array}$ for any unitary matrix $U$

Theorem 4.2.3. As long as no zero bidiagonal element is encountered, the orthonormal vectors $( u _ { 1 } , \ldots , u _ { k } )$ and $( v _ { 1 } , \ldots , v _ { k } )$ generated by Bidiagl are bases for the Krylov subspaces

$$
\begin{array} { r } { \mathcal { R } ( U _ { k } ) = { \mathcal K } _ { k } ( A A ^ { T } , b ) , \qquad { \mathcal R } ( V _ { k } ) = { \mathcal K } _ { k } ( A ^ { T } A , A ^ { T } b ) , \quad k = 1 , 2 , \dots . } \end{array}
$$

Proof. We have $\beta _ { 1 } u _ { 1 } = b$ and $\alpha _ { 1 } v _ { 1 } = A ^ { T } u _ { 1 }$ If $\beta _ { 1 } \alpha _ { 1 } \neq 0$ ，then $( \beta _ { 1 } \alpha _ { 1 } ) v _ { 1 } = A ^ { T } b$ Hence (4.2.35) holds for $k = 1$ . Assume now that (4.2.35) is true for some $k \geq 1$ .If $\beta _ { k + 1 } \alpha _ { k + 1 } \neq 0$ ,it follows fr0m (4.2.23)-(4.2.24) that

$$
\begin{array} { r l } & { \mathcal { R } ( U _ { k + 1 } ) = \mathcal { R } ( U _ { k } ) \cup A \mathcal { K } _ { k } ( A ^ { T } A , A ^ { T } b ) = \mathcal { K } _ { k + 1 } ( A A ^ { T } , b ) , } \\ & { \mathcal { R } ( V _ { k + 1 } ) = \mathcal { R } ( V _ { k } ) \cup A ^ { T } \mathcal { K } _ { k } ( A A ^ { T } , b ) = \mathcal { K } _ { k + 1 } ( A ^ { T } A , A ^ { T } b ) . } \end{array}
$$

Hence (4.2.35) holds for $k + 1$ . The theorem now follows by induction in $k$

By Theorem 4.2.3 the matrices $U _ { k }$ and $V _ { k }$ can also be obtained by Gram-Schmidt orthogonalization of the Krylov sequences

$$
u _ { 1 } , A A ^ { T } u _ { 1 } , ( A A ^ { T } ) ^ { 2 } u _ { 1 } , \ldots , \qquad v _ { 1 } , A ^ { T } A v _ { 1 } , ( A ^ { T } A ) ^ { 2 } v _ { 1 } , \ldots .
$$

Hence, the uniqueness of the bases is a consequence of the uniqueness (up to a diagonal scaling with elements $\pm 1$ ) of the QR factorization of a real matrix of full column rank.

Bidiagl terminates for some $k \leq \mathrm { r a n k } ( A )$ when the subspaces $\mathcal { K } _ { k } ( A ^ { T } A , A ^ { T } b )$ have reached maximum rank. Then the subspaces

$$
\mathcal { K } _ { k } ( A A ^ { T } , A A ^ { T } b ) = A \mathcal { K } _ { k } ( A ^ { T } A , A ^ { T } b )
$$

have also reached maximal rank. At termination the pseudoinverse solution $x _ { k } = V _ { k } y _ { k }$ is obtained for some $y _ { k } \in \mathbb { R } ^ { k }$ , where $\mathcal { R } ( V _ { k } ) = \mathcal { K } _ { k } ( A ^ { T } A , A ^ { T } b )$

Bidiag2 terminates with $\beta _ { k + 1 } = 0$ for some $k \leq \mathrm { r a n k } ( A )$ when the subspaces $\mathcal { K } _ { k } ( A ^ { T } A , A ^ { T } b )$ have reached maximum rank. Then the subspaces $\mathcal { K } _ { k } ( A A ^ { T } , A A ^ { T } b ) = A \mathcal { K } _ { k } ( A ^ { T } A , A ^ { T } b )$ have also reached maximal rank. Bidiag2 generates vectors giving orthogonal bases for

$$
\begin{array} { r } { \mathcal { R } ( V _ { k } ) = \mathcal { K } _ { k } ( A ^ { T } A , A ^ { T } b ) , \qquad \mathcal { R } ( U _ { k } ) = \mathcal { K } _ { k } ( A A ^ { T } , A A ^ { T } b ) . } \end{array}
$$

Bidiagl and Bidiag2 generate the same $V _ { k }$ ,but $U _ { k }$ differs. The upper bidiagonal matrix $R _ { k }$ in Bidiag2 is the same as the matrix obtained by QR factorization of the lower bidiagonal $B _ { k }$ in Bidiagl; see Paige and Saunders [866,1982].

Collecting previous results we can now state the following.

Theorem 4.2.4 (Krylov Subspace Approximations). Let p be the grade of $A ^ { T } b$ with respect to $A ^ { T } A .$ Then the projected least squares problems

$$
\operatorname* { m i n } _ { \boldsymbol { x } _ { k } } \| A \boldsymbol { x } _ { k } - \boldsymbol { b } \| _ { 2 } ~ s u b j e c t ~ t o ~ \boldsymbol { x } _ { k } \in \mathcal { K } _ { k } ( A ^ { T } A , A ^ { T } \boldsymbol { b } ) , \quad 1 \leq k \leq p ,
$$

have full rank. The solutions $x _ { k }$ are uniquely determined, and the residuals satisfy $r _ { k } = b -$ $A x _ { k } \perp \mathcal { K } _ { k } ( A A ^ { T } , A A ^ { T } b )$ Independent of $b$ and the size or rank of $A$ ，the Krylov subspace approximations terminate with the pseudoinverse solution $x _ { p } = A ^ { \dagger } b$ for some $p \leq \mathrm { r a n k } ( A )$

From the nested property of the Krylov subspaces $\mathcal { K } _ { k } ( A ^ { T } A , A ^ { T } b )$ ， $k = 1 , 2 , \dots$ , it follows that the sequence of residual norms $\| r _ { k } \| _ { 2 } , k = 1 , 2 , . . .$ ，are monotonically decreasing. For $k < p$ the Krylov subspace approximations depend nonlinearly on $b$ in a highly complicated way.

At termination,all bidiagonal elements in $B$ and $R$ of Bidiagl and Bidiag2 are positive. Such bidiagonal matrices are said to be unreduced and have the following property.

Lemma 4.2.5. For any unreduced bidiagonal matrix $B$ , all singular values $\sigma _ { i }$ must be distinct.

Proof. If $B$ is unreduced, then $T = B ^ { T } B$ is symmetric tridiagonal with positive off-diagonal elements $\gamma _ { i } = \rho _ { i } \gamma _ { i + 1 }$ . Such a tridiagonal matrix is also called unreduced and, by Parlett [884, 1998,Lemma 7.7.1], has distinct eigenvalues $\lambda _ { i }$ . The lemma now follows from the fact that $\lambda _ { i } = \sigma _ { i } ^ { 2 }$ □

Theorem 4.2.6. Let $A$ have p distinct, possibly multiple, nonzero singular values. Then,Bidiagl and Bidiag2 terminate with an unreduced bidiagonal matrix $B _ { k } = U _ { k } ^ { T } A V _ { k }$ of rank $k \leq p .$

Proof. Since $B _ { k }$ is unreduced, it follows from Lemma 4.2.5 that all its singular values must be distinct: $\sigma _ { 1 } > \sigma _ { 2 } > \cdot \cdot \cdot > \sigma _ { k } > 0$ .But these are also singular values of $A$ ，and hence $k \leq p$ □

Theorem 4.2.6 states that if $A$ has singular values of multiplicity greater than one,then Bidiagl and Bidiag2 terminate in less than $\operatorname { r a n k } ( A )$ steps. For example,let square $A = I _ { n } + u v ^ { T }$ ， $u , v \ne 0$ ，and $\operatorname { r a n k } ( A ) = n$ . The singular values of $A$ are the square roots of the eigenvalues of $A ^ { T } A = I _ { n } + u v ^ { T } + v u ^ { T } + ( u ^ { T } u ) v v ^ { T }$ $A ^ { T } A$ has one eigenvalue equal to 1 of multiplicity $( n - 2 )$ corresponding to eigenvectors $x$ that are orthogonal to $u$ and $v$ .Hence, $A$ has at most three distinct singular values,and, in exact arithmetic, bidiagonalization must terminate after at most three steps.

If $b$ is orthogonal to the left singular subspaces corresponding to some of the singular values, Bidiagl terminates in $k \leq p$ steps; see Bjorck [137, 2014,Lemma 2.1].

# 4.2.5 - Partial Least Squares Algorithms

The NIPALS (Nonlinear Iterative PArtial Least Squares) method was devised by H. Wold [1127, 1966] to model relations between sets of observed variables and a number of latent (not directly observed variables. Initially, the main applications were prediction and cause-effect inference in statistics and economics. S. Wold et al.[1128,1984] developed the recursive NIPALS-PLS algorithm for use in chemometrics and pointed out its equivalence to Krylov subspace approximations. Today, partial least squares (PLS) is a widely used multivariate regression technique with a broad spectrum of applications in research and industry, such as bioinformatics, food science, medicine, pharmacology, social sciences,and physiology; see Vinzi et al.[1093, 2010].

NIPALS-PLS. Set $A _ { 0 } = A$ ， $b _ { 0 } = b$ ,and for $k = 1 , 2 , \ldots$

$$
\begin{array} { r l } & { \hat { v } _ { k } = A _ { k - 1 } ^ { T } b _ { k - 1 } , \quad v _ { k } = \hat { v } _ { k } / \| \hat { v } _ { k } \| _ { 2 } , } \\ & { \hat { u } _ { k } = A _ { k - 1 } v _ { k } , \quad u _ { k } = \hat { u } _ { k } / \| \hat { u } _ { k } \| _ { 2 } , } \\ & { p _ { k } ^ { T } = u _ { k } ^ { T } A _ { k - 1 } , \quad \zeta _ { k } = u _ { k } ^ { T } b _ { k - 1 } , } \\ & { ( A _ { k } , b _ { k } ) = ( A _ { k - 1 } , b _ { k - 1 } ) - u _ { k } ( p _ { k } ^ { T } , \zeta _ { k } ) . } \end{array}
$$

The $k$ th PLS approximation is $x _ { k } = V _ { k } y _ { k }$ ,where $y _ { k }$ satisfies

$$
( P _ { k } ^ { T } V _ { k } ) y _ { k } = z _ { k } , \quad z _ { k } = ( \zeta , . . . , \zeta _ { k } ) ^ { T } ,
$$

$V _ { k } ~ = ~ ( v _ { 1 } , \ldots , v _ { k } )$ ， $U _ { k } \ = \ ( u _ { 1 } , \ldots , u _ { k } )$ ，and $P _ { k } = \left( p _ { 1 } , \ldots , p _ { k } \right)$ .Note that in (4.2.41） the orthogonal projections of $A _ { k - 1 }$ and $b _ { k - 1 }$ onto $u _ { k }$ are subtracted:

$$
( A _ { k } , b _ { k } ) = ( I - u _ { k } u _ { k } ^ { T } ) ( A _ { k - 1 } , b _ { k - 1 } ) .
$$

The process terminates when either $\| \hat { v } _ { k } \| _ { 2 }$ or $\| \hat { u } _ { k } \| _ { 2 }$ is zero. Note that if $u _ { k } ^ { T } A _ { k - 1 } v _ { k } \neq 0$ ,the rank of $A _ { k }$ is exactly one less than that of $A _ { k - 1 }$

In the PLS literature, $u _ { k }$ are called score vectors, $v _ { k }$ loading weights, and $p _ { k }$ loading vectors. Summing the equations in (4.2.41) gives

$$
A = U _ { k } P _ { k } ^ { T } + A _ { k } , \qquad b = U _ { k } z _ { k } ^ { T } + b _ { k } .
$$

Then $\begin{array} { r } { U _ { k } P _ { k } ^ { T } = \sum _ { i = 1 } ^ { k } u _ { i } p _ { i } ^ { T } } \end{array}$ is a rank $k$ approximation to te da atix $A$ . The data residuals are given by

$$
A _ { k } = A - U _ { k } P _ { k } ^ { T } = ( I - U _ { k } U _ { k } ^ { T } ) A .
$$

# Algorithm 4.2.1 (NIPALS-PLS Algorithm).

function [x,U,P,V] $=$ nipalspls(A,b,k)   
$\%$ NIPALSPLS computes the first $\mathtt { k }$ PLS factors for the   
$\%$ least squares problem min $| \mathbf { | } \mathbf { A x } \ \textrm { - } \mathbf { b } | \mathbf { | } \ \mathbf { - } 2$ ·   
$\%$ --- [m,n] = size(A)； U = zeros(m,k); $\begin{array} { r l } { \texttt { V } = } \end{array}$ zeros $( \mathtt { n } , \mathtt { k } )$ ； $\mathrm { ~ \mathsf ~ { ~ P ~ } ~ } = \mathrm { ~ \mathsf ~ { ~ V ~ } ~ }$ ； $_ z =$ zeros(k,1); for ${ \\\texttt { i } } = { \texttt { 1 : k } }$ $\begin{array} { r l } & { \mathrm { ~ \tt ~ v ~ = ~ \tt ~ A ^ { \tt ~ 7 } * b } ; \quad \mathrm { ~ n ~ \tt ~ v ~ = ~ \tt ~ n o r m ( v ) ~ } ; } \\ & { \mathrm { ~ i ~ f ~ \tt ~ n ~ v ~ = ~ 0 ~ } , \quad \mathrm { ~ b ~ r e a k , ~ \ e n d ~ \tt ~ } } \\ & { \mathrm { ~ \tt ~ v ~ = ~ \tt ~ v / n v } ; } \\ & { \mathrm { ~ u _ \tt ~ = ~ \tt ~ A ^ { \tt ~ * } v } ; \quad \mathrm { ~ u _ \tt ~ = ~ u _ \tt / n o r m ( u ) ~ } ; } \\ & { \mathrm { ~ \tt ~ \tt ~ 9 _ e ~ I \textmu a t e ~ \tt ~ A ^ \tt ~ a n d ~ b _ \tt ~ } } \\ & { \mathrm { ~ \tt ~ p ~ = ~ \tt ~ A ^ { \tt ~ * } * u _ \tt ~ ; ~ { \tt ~ z } ( i ) ~ = ~ b _ \tt ~ > ~ u _ \tt ~ ; ~ } } \\ & { \mathrm { ~ \tt ~ A ~ = ~ \tt ~ A ^ \tt ~ - ~ u * \mathrm { p } ~ } ; \quad \mathrm { ~ b ~ \tt ~ = ~ b ~ - ~ u * z \mathrm { ~ ( ~ i ) ~ } ; ~ \mathrm { ~ \tt ~ \forall ~ } _ \mathrm { \tt ~ 0 } ~ } } \\ & { \mathrm { ~ \tt ~ V \left( : ~ , ~ i ~ \right) ~ = ~ v _ \tt ~ ; ~ \ u ( \tt ~ ; ~ i ) ~ = ~ u _ \tt ~ ; ~ \ u _ \tt ~ P ( : , ~ i ) ~ = ~ p _ \tt ~ ; ~ } } \end{array}$ ate data end $\mathrm {  ~ x ~ } = \mathrm {  ~ V } * \left( \left( \mathrm { P } ^ { \prime } * \mathrm { v } \right) \setminus \mathrm { z } \right) ;$ % Regression coefficients   
end

NIPALS-PLS uses three matrix-vector products and one rank-one deflation that together require 8mn flops per PLS factor. The flop counts for the additional scalar products and the final back-substitution for solving the upper triangular systems are negligible in comparison. For $k \ll \operatorname* { m i n } ( m , n )$ this is the same number of flops per step as required using Householder bidiagonalization.

In exact arithmetic, NIPALS-PLS computes the sequence of Krylov subspace approximations defined in Theorem 4.2.4. The following important result is due to Eldén [375, 2004].

Theorem 4.2.7. The vectors $\{ v _ { 1 } , \ldots , v _ { k } \}$ and $\{ u _ { 1 } , \ldots , u _ { k } \}$ generated by NIPALS-PLS form orthonormal bases for $\mathcal { K } _ { k } ( A ^ { T } A , A ^ { T } b )$ and $\mathcal { K } _ { k } ( A A ^ { T } , A A ^ { T } b )$ ,respectively. In exact arithmetic, these vectors are the same as the columns of $V _ { k }$ and $U _ { k }$ from the Bidiag2 algorithm. It also follows that $P _ { k } ^ { T } V _ { k }$ is an upper bidiagonal matrix, and $x _ { k }$ is the kth Krylov subspace approximation.

In floating-point arithmetic there will be a progressive loss of orthogonality in $U _ { k }$ and $V _ { k }$ in NIPALS-PLS,and the computed off-bidiagonal elements in $P _ { k } ^ { T } V _ { k }$ will not be negligible. The loss of orthogonality is approximately proportional to the condition number $\kappa ( P _ { k } ^ { T } V _ { k } )$ ; see Bjorck [137, 2014]._However, relations (4.2.43) still hold to working precision. Although in theory the matrix $P _ { k } ^ { T } V _ { k }$ is upperbidiagonal,thiswillnotbethecaseinfloating-poitopu-tation. It is not clear if neglecting the of-bidiagonal elements in $P _ { k } ^ { T } V _ { k }$ improves the accuracy of the solution. In the implementation above we follow the original NIPALS-PLS algorithm and treat $P _ { k } ^ { T } V _ { k }$ as afull matrix. This increases the arithmetic cost of solving the subproblem (4.2.42) from $2 k$ flops to $2 k ^ { 3 } / 3$ flops. Tests show only marginal differences in accuracy for these options.

The high accuracy of NIPALS-PLS seems to be partly due to the fact that the augmented data matrix $( A , b )$ is deflated before the next step of orthogonalization is carried out.In exact arithmetic,the vectors $u _ { 1 } , \ldots , u _ { k }$ are mutually orthogonal. Then $\zeta _ { k } = u _ { k } ^ { T } b _ { k - 1 } = u _ { k } ^ { T } b$ and NIPALS-PLS can be“simplified”by omitting the deflation of $b$ .In floating-point arithmetic this omission can substantially increase the loss of orthogonality in $U _ { k }$ and $V _ { k }$ and cause a loss of accuracy in the computed $x _ { k }$ . It is unfortunate that omitting the deflation of $b$ seems to have become the norm rather than the exception.For example,Manne [771, $\mathrm { 1 9 8 7 } ]$ proposes a marginally faster PLS algorithm by omitting the deflation of $b$ .The implementation of NIPALS tested by Andersson [29,2oog] also omits this deflation. Unfortunately, this practice has spread even to some commercial statistical software packages.

In the context of iterative methods for least squares problems, the Bidiag2 process is known to lead to a less stable algorithm than Bidiag1; see Paige and Saunders [866,1g82]. For PLS it is more direct to use the Bidiag2 process.In the implementation below,orthogonality in the computed basis vectors $u _ { k }$ and $v _ { k }$ is preserved by reorthogonalizing the new basis vectors $u _ { k + 1 }$ and $v _ { k + 1 }$ against all previous basis vectors.Then there is no difference in stability between Bidiagl and Bidiag2,as confrmed by tests in Bjorck and Indahl [148,2o17].The additional cost of reorthogonalizing is about $4 ( m + n ) k ^ { 2 }$ flops for $k$ factors. Unless $k$ is very large, this overhead is acceptable.

# Algorithm 4.2.2 (Bidiag2-PLS).

$[ \mathrm { x } , \mathrm { U } , \mathrm { B } , \mathrm { V } ] = \mathrm { b i d i a g 2 p 1 s ( \mathrm { A } , \mathrm { b } , \mathrm { k } ) }$   
$\%$ BIDIAG2-PLS computes the first k PLS factors using Golub--Kahan bidiagonalization   
%--- $\mathtt { [ m , n ] } \ = \ \mathtt { s i z e ( A ) }$ ； $\tt { B } \thinspace =$ zeros(k,2)；% B stored by diagonals $\begin{array} { l } { { \mathrm {  ~ x ~ } = \mathrm {  ~ z e r o s ~ } ( \mathrm {  ~ n ~ } , \mathrm {  ~ k ~ } ) ; \mathrm {  ~ { \cal ~ U } ~ } = \mathrm {  ~ z e r o s ~ } ( \mathrm {  ~ n ~ } , \mathrm {  ~ k ~ } ) ; \mathrm {  ~ { \cal ~ V } ~ } = \mathrm {  ~ z e r o s ~ } ( \mathrm {  ~ n ~ } , \mathrm {  ~ k ~ } ) } } \\ { { \mathrm {  ~ v ~ } = \mathrm {  ~ A ~ } ^ { \prime } * { \mathrm {  ~ b ~ } } ; \mathrm {  ~ { \cal ~ V } ~ } = \mathrm {  ~ v / n o r m ~ } ( \mathrm {  ~ v } ) ; } } \\ { { \mathrm {  ~ w ~ } = \mathrm {  ~ A ~ } { \ast \mathrm {  ~ v ~ } } ; \mathrm {  ~ { \cal ~ r h o } ~ } = \mathrm { \ n o r m ~ } ( \mathrm {  ~ w ~ } ) ; \mathrm {  ~ { \cal ~ U } ~ } = ( \mathrm {  ~ 1 / r h o ~ } ) { \ast \mathrm {  ~ w ~ } } ; } } \\ { { \mathrm {  ~ V ~ } ( : , { \bf ~ 1 } ) = \mathrm {  ~ v } ; \mathrm {  ~ { \cal ~ U } ~ } ( : , { \bf ~ 1 } ) = \mathrm {  ~ w ~ } ; \mathrm {  ~ { \cal ~ B } ~ } ( 1 , { \bf ~ 1 } ) = \mathrm {  ~ r h o ~ } ; } } \\ { { \mathrm {  ~ z ~ } = \mathrm {  ~ v / r h o ~ } ; \mathrm {  ~ { \cal ~ x } ~ } ( : , { \bf ~ 1 } ) = ( \mathrm {  ~ { \cal ~ { \cal ~ G } } ~ } ^ { \prime } * { \mathrm {  ~ b } } ) * { \bf z } ; } } \end{array}$ ； for $\dot { \mathtt { \_ { \lambda } } } = 2 : \mathtt { k }$ % Bidiagonalization V = A'\*w - rho\*v; $\begin{array} { l l l l l } { \dot { \mathrm {  ~ \gamma ~ } } } & { \dot { \mathrm {  ~ \dots ~ } } } & { \mathrm {  ~ \Im ~ } } & { \dot { \mathrm {  ~ \Im ~ } } } & { \mathrm {  ~ \gamma ~ } } \\ { \mathrm {  ~ \nabla ~ } } & { = \mathrm {  ~ \nabla ~ } \mathrm { V } \ast \left( \mathrm { V } ^ { \prime } \ast \mathrm {  ~ \times ~ } \mathrm {  ~ \nabla ~ } \right) ; } & { \mathrm {  ~ \sqrt { \eta } _ { \mathrm { \tiny ~ a } } ~ } \mathrm { R e o r t h o g } } \\ { \mathrm {  ~ \mathrm { g a m m a ~ } } } & { = \mathrm {  ~ \ n o r m } \left( \mathrm { v } \right) ; } & { \mathrm {  ~ \mathrm { \cal ~ B } \left( i - 1 , 2 \right) ~ } } & { = \mathrm {  ~ \ g a m m a ~ } ; } \\ { \mathrm {  ~ \nabla ~ } } & { = \mathrm {  ~ \Gamma ~ } ( 1 / \mathrm { g a m m a } ) \ast \mathrm {  ~ \nabla ~ } \mathrm { V } \left( \mathrm {  ~ \cdot ~ } , \mathrm {  ~ i ~ } \right) } & { = \mathrm {  ~ \ v ~ } ; } \\ { \mathrm {  ~ \overline { { \cal ~ } } } } & { \dot { \mathrm {  ~ \nabla ~ } } } & { \dot { \mathrm {  ~ A } } \ast \mathrm {  ~ \nabla ~ } - \mathrm {  ~ \ g a m m a \ast \mathrm {  ~ \nabla ~ } } ; } \\ { \mathrm {  ~ \nabla ~ } } & { \dot { \mathrm {  ~ \nabla ~ } } } & { = \mathrm {  ~ \nabla ~ } \mathrm { V } \ast \left( \mathrm { U } ^ { \prime } \ast \mathrm {  ~ \times ~ } \mathrm {  ~ \nabla ~ } \right) ; } & { \mathrm {  ~ \nabla ~ } \mathrm { \sqrt { \eta } _ { \mathrm { \tiny ~ R } } \ e o r t h o g } } \\ { \mathrm {  ~ \mathrm { \texttt ~ { ~ r h o ~ } } } } & { = \mathrm {  ~ \ n o r m } \left( \mathrm { u } \right) ; } & { \mathrm {  ~ \mathrm { \cal ~ B } \left( i ~ \right)} , 1  } & { = \mathrm {  ~ \ r h o ~ } \mathrm {  ~ \nabla ~ } \mathrm { r h o ~ } ; } \end{array}$ onalize onalize if rho $\ c = ~ 0$ ，break，end $\begin{array} { r } { \texttt { w } = \ ( 1 / \mathrm { r h o } ) * _ { \texttt { W } } ; \quad \mathrm { U } \left( : , \mathtt { i } \right) \ = \ \texttt { w } ; } \end{array}$ $\mathrm { \Lambda ~ z ~ = ~ ( 1 / r h o ) * ( v ~ - ~ \ g a m m a * z ) ~ ; ~ \% ~ U p d \hat { \Lambda } ~ }$ ite solution $\mathbf { x } \left( : , \mathbf { i } \right) \ = \ \mathbf { x } \left( : , \mathbf { i } - 1 \right) \ \ + \ \left( \mathbf { w } ^ { \prime } * \mathbf { b } \right) * \mathbf { z } ;$ end   
end

Example 4.2.8. Like TSVD (truncated SVD) approximations, the PLS approximations are orthogonal projections of the pseudoinverse solution onto a nested sequence of subspaces of dimension $k \ll n$ ； see Section 3.6.2. Both sequences have regularization properties. However, because PLS only requires a partial bidiagonalization of $A$ , it is much less expensive to compute than TSVD.Further, for PLS the subspaces depend (nonlinearly) on the right-hand side $b$ and are tailored to the specific right-hand side.Therefore,the minimum error for an illconditioned problem is often achieved with a lower dimensional subspace for PLS rather than for TSVD.Consider the discretized problem $K f = g$ in Example 3.6.1 for the linear operator $K ( s , t ) = e ^ { - ( s - t ) ^ { 2 } }$ with $m = n = 1 0 0$ Let $f$ be known, set $g = K f$ ,and let ${ \widehat { g } } = g + e$ be a perturbed right-hand side, where $e$ is normally distributed with zero mean and variance $1 0 ^ { - 4 }$ . Figure 4.2.1 shows the relative error $\| f _ { k } - f \| _ { 2 } / \| f \| _ { 2 }$ and the relative residual norm $\| { K f _ { k } - g } \| _ { 2 } / \| g \| _ { 2 }$ for the PLS and TSVD solutions as a function of $k$ . The results are almost identical.For PLS the smallest error occurs for $k = 1 0$ and for TSVD occurs for $k = 1 2$ .For larger values of $k$ the error increases rapidly, but the residual norm is almost constant.

![](../chunks/Numerical Methods for Least Squares Problems (Åke Björck) (z-library.sk, 1lib.sk, z-lib.sk_part_0004_pages_0211-0280/auto/images/61b0c8c7de0103a9631a1bdf865bcb6db1887abcc06ca715fb2666b081d5604a.jpg)  
Figure 4.2.1. Relative error $\| f _ { k } - f \| _ { 2 } / \| f \| _ { 2 }$ (solid line)and relative residual $\| K f _ { k } - f \| _ { 2 } / \| f \| _ { 2 }$ (dashed line) after k steps. PLS (left) and TSVD (right). Used with permission of Springer International Publishing;from Numerical Methods in Matrix Computations,Bjorck, $\mathring { A } k e _ { : }$ ，2015；permission conveyed through Copyright Clearance Center, Inc.

Many algorithms that differ greatly in speed and accuracy have been proposed for PLS. Both NIPALS-PLS and HHBD perform transformations on $A$ that require $A$ to be explicitly available. This makes them less suitable for large-scale problems. Andersson [29, 2oog] tested nine different PLS algorithms on a set of contrived benchmark problems.The only provably backward stable method among them, HHBD, was much slower than NIPALS-PLS,which also was one of the most accurate,even though it was used here without deflation of $b$ .The version of Bidiag2- PLS used did not employ reorthogonalization and gave poor accuracy. In further tests by Bjorck and Indahl [148, 2O17] the most accurate algorithms were HHBD,NIPALS-PLS with deflation, and Bidiag2-PLS with reorthogonalization. For large-scale problems, Bidiag2-PLS is the method of choice. On some large simulated data sets of size $3 0 , 0 0 0 \times 1 0 , 0 0 0$ and 100 extracted com-ponents, Bidiag2-PLS was about seven times faster than NIPALS. Notably, the popular SIMPLS algorithm by de Jong [295,1993l, used by the MATLAB function plsregres s, gave poor accuracy. This was true even when it was improved by reorthogonalization, as suggested by Faber and Ferré [390, 2008].

# Notes and references

The close relationship between PLS and bidiagonalization is explored by Manne [771,1987] and Helland [599,1988]. Many extensions of the basic PLS algorithm treated here have been devised; see S.Wold, Sjostrom,and Eriksson [1129,2oo1]. An overview of advances in PLS is given by Rosipal and Krämer [937, 2005].

Simon and Zha [996, 2ooo] show that in many applications it may suffice to reorthogonalize either $u _ { k }$ or $v _ { k }$ . However, tests by Bjorck and Indahl [148,2o17] show that such onesided reorthogonalization could lead to a substantial loss of precision compared to full reorthogonalization.

# 4.3 - Some Structured Problems

# 4.3.1 - Two-Block Least Squares Problems

It is sometimes useful to partition a least squares problem into two blocks as

$$
\operatorname* { m i n } _ { y , z } \left\| \left( \begin{array} { l l } { A } & { B } \end{array} \right) \left( \begin{array} { l } { y } \\ { z } \end{array} \right) - b \right\| _ { 2 } ^ { 2 } ,
$$

where $A \in \mathbb { R } ^ { m \times n _ { 1 } }$ ， $B \in \mathbb { R } ^ { m \times n _ { 2 } }$ . One example is periodic spline approximation, which leads to a problem of augmented band form, where $A$ is a band matrix and $B$ is a full matrix with a small number of columns.

If $z$ is given, then $y$ must solve the problem

$$
\operatorname* { m i n } _ { y } \| A y - ( b - B z ) \| _ { 2 } .
$$

Substituting the solution $y = A ^ { \dagger } ( b - B z )$ into (4.3.2) to eliminate $y$ ，we see that $z$ solves the problem

$$
\operatorname* { m i n } _ { z } \| ( I - A A ^ { \dagger } ) ( B z - b ) \| _ { 2 } ,
$$

where $I - A A ^ { \dag } = P _ { \mathcal { N } ( A ^ { T } ) }$ is the orthogonal projector onto $\mathcal { N } ( A ^ { T } )$ . Thus (4.3.1) has been split into two separate least squares problems (4.3.3) and (4.3.2).

One advantage of this is that different methods can be used to solve the two least squares subproblems for $z$ and $y$ .Moreover, the subproblem for $z$ is always better conditioned than the original problem.Hence, $z$ can sometimes be computed with sufficient accuracy by the method of normal equations;see Foster [427,1991]. Another application is when $n _ { 2 } \gg n _ { 1 }$ and the subproblem for $z$ can be solved by an iterative method; see Section 6.3.6.

The normal equations of (4.3.1) are

$$
\left( \begin{array} { c c } { { A ^ { T } A } } & { { A ^ { T } B } } \\ { { B ^ { T } A } } & { { B ^ { T } B } } \end{array} \right) \left( \begin{array} { c } { { y } } \\ { { z } } \end{array} \right) = \left( \begin{array} { c } { { A ^ { T } b } } \\ { { B ^ { T } b } } \end{array} \right) .
$$

Eliminating $y$ gives $S z = s$ ，where $S$ is the Schur complement of $A ^ { T } A$ . This can be written

$$
\begin{array} { r } { S = B ^ { T } P _ { N ( A ^ { T } ) } B , \quad s = B ^ { T } P _ { N ( A ^ { T } ) } b , } \end{array}
$$

where $P _ { \mathcal { N } ( A ^ { T } ) } = I - A ( A ^ { T } A ) ^ { - 1 } A ^ { T }$ . When $z \in \mathbb { R } ^ { n _ { 2 } }$ has been determined, we obtain $y \in \mathbb { R } ^ { n _ { 1 } }$ from

$$
A ^ { T } A y = A ^ { T } ( b - B z ) .
$$

For beter stability, methods based on orthogonal factorizations should be used. After $n _ { 1 }$ steps,a partial Householder QR factorization reduces the first block in $\left( \begin{array} { l l } { A } & { B } \end{array} \right)$ to the upper triangular form,

$$
Q _ { 1 } ^ { T } \left( \begin{array} { c c c } { { A } } & { { B } } & { { b } } \end{array} \right) = \left( \begin{array} { c c c } { { R _ { 1 1 } } } & { { R _ { 1 2 } } } & { { c _ { 1 } } } \\ { { 0 } } & { { A _ { 2 2 } } } & { { c _ { 2 } } } \end{array} \right) ,
$$

where $Q _ { 1 } = P _ { 1 } \cdot \cdot \cdot P _ { n _ { 1 } }$ .By the orthogonal invariance of the 2-norm,

$$
\begin{array} { r } { \| A x - b \| _ { 2 } = \left\| \left( \begin{array} { c c } { R _ { 1 1 } } & { R _ { 1 2 } } \\ { 0 } & { A _ { 2 2 } } \end{array} \right) \left( \begin{array} { c } { y } \\ { z } \end{array} \right) - \left( \begin{array} { c } { c _ { 1 } } \\ { c _ { 2 } } \end{array} \right) \right\| _ { 2 } . } \end{array}
$$

This gives for $z$ and $y$ the subproblems

$$
\operatorname* { m i n } _ { z } \| A _ { 2 2 } z - c _ { 2 } \| _ { 2 } , \qquad R _ { 1 1 } y = c _ { 1 } - R _ { 1 2 } z .
$$

Similarly, after $n _ { 1 }$ steps of MGS we have obtained the partial factorization

$$
\left( \begin{array} { c c } { A } & { b } \end{array} \right) = \left( Q _ { 1 } \quad A ^ { ( n _ { 1 } + 1 ) } \quad b ^ { ( n _ { 1 } + 1 ) } \right) \left( \begin{array} { c c c } { R _ { 1 1 } } & { R _ { 1 2 } } & { c _ { 1 } } \\ { 0 } & { I } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right) ,
$$

where $Q _ { 1 } ^ { T } A ^ { ( n _ { 1 } + 1 ) } = 0 $ The original problem then decomposes into (compare (4.3.7))

$$
\operatorname* { m i n } _ { z } \| A ^ { ( n _ { 1 } + 1 ) } z - b ^ { ( n _ { 1 } + 1 ) } \| _ { 2 } , \qquad R _ { 1 1 } y = c _ { 1 } - R _ { 1 2 } z .
$$

The following lemma gives an alternative formulation without explicitly referring to orthogonal projections.

Lemma 4.3.1. Let $z \in \mathbb { R } ^ { n _ { 2 } }$ and $W \in \mathbb { R } ^ { n _ { 2 } \times n _ { 1 } }$ be the solutions to the least squares problems

$$
\operatorname* { m i n } _ { \boldsymbol { w } } \| \boldsymbol { A } \boldsymbol { w } - \boldsymbol { b } \| _ { 2 } , \qquad \operatorname* { m i n } _ { \boldsymbol { W } } \| \boldsymbol { A } \boldsymbol { W } - \boldsymbol { B } \| _ { F } .
$$

Then the solution to (4.3.1) is given by $y = z - W z ,$ where $z$ solves

$$
\operatorname* { m i n } _ { z } \| ( B - A W ) z - ( b - A w ) \| _ { 2 } .
$$

Proof. If $w$ and $W$ solve (4.3.8), then $A w = P _ { A } b$ and $A W = P _ { A } B$ .Hence the least squares problems (4.3.9) and (4.3.3) are equivalent. Further, $y = z - W x$ solves (4.3.2),because $A y =$ $A ( z - W z ) = P _ { A } ( b - A z )$ □

A common practice in linear regression is to preprocess the data by centering the data, i.e., subtracting out the means. This can be interpreted as a simple case of a two-block least squares problem, where

$$
( e \quad B ) \left( { \begin{array} { l } { \xi } \\ { z } \end{array} } \right) = b , \quad e = ( 1 , \ldots , 1 ) ^ { T } .
$$

Multiplying $B \in \mathbb { R } ^ { m \times n }$ and $b \in \mathbb { R } ^ { m }$ with the projection matrix $( I - e e ^ { T } / m )$ gives

$$
\bar { B } = B - \frac { 1 } { m } e ( e ^ { T } B ) , \quad \bar { b } = b - \frac { e ^ { T } b } { m } e .
$$

This makes the columns of $\bar { B }$ and $\bar { b }$ orthogonal to $e$ .The reduced least squares problem becomes $\mathrm { m i n } _ { x } \| \bar { B } z - \bar { b } \| _ { 2 }$ . After solving the reduced problem for $z$ ,we obtain $\xi = e ^ { T } ( b - B z ) / m$

Example 4.3.2. The Hald cement data (see [561,1952,p. 647]) are used in Draper and Smith [331,1998,Appendix B] and several other books as an example of regression analysis. The right-hand side consists of $m = 1 3$ observations of the heat evolved in cement during hardening. The explanatory variables are four different ingredients of the mix and a constant term:

For the least squares problem $\| A x - b \| _ { 2 }$ ， $\kappa ( A ) \approx 3 . 2 4 5 \cdot 1 0 ^ { 3 }$ indicates that about six digits may be lost when using the normal equations. The first column of ones in $A = ( e , B )$ is added to extract the mean values. The first variable $\xi$ in $x = ( \xi , y )$ can be eliminated by setting

$$
\bar { B } = B - e p ^ { T } , \quad c = b - \beta e ,
$$

where $p = ( e ^ { T } B ) / m$ ， $\beta = e ^ { T } b / m$ ,and $\xi = \beta - p ^ { T } y$ ，The reduced problem $\begin{array} { r } { \operatorname* { m i n } _ { y } \| \bar { B } y - c \| _ { 2 } } \end{array}$ is much better conditioned: $\kappa ( \bar { B } ) = 2 3 . 0$ . Normalizing the columns of $B$ to have unit length decreases the condition number by only a small amount to $\kappa ( B D ) = 1 9 . 6 $

# 4.3.2 - Block-Angular Problems

As noted by Rice [925, 1983], many large sparse least squares problems possess a natural multi-level block structure. An early example is geodetic survey problems. A technique for breaking down such problems into geographically defined subproblems was introduced by Helmert [600, 1880]; see Golub and Plemmons [505,198o]). Other examples are photogrammetry (Golub, Luk,and Pagano [499,1979l), Doppler radar positioning (Manneback, Murigande,and Toint [773,1985l),and economic models (Duchin and Szyld [339,1979l).

The substructuring can reflect a “local connection” in the underlying physical problem. For example, a geodetic position network consists of geodetic stations connected through observations.To each station corresponds a set of unknown coordinates to be determined. This data may naturally be arranged by counties, then by states, then by countries. Let $\boldsymbol { B }$ be sets of stations that separate the other stations into $p$ blocks $\mathcal { A } _ { 1 } , \ldots , \mathcal { A } _ { p }$ in such a way that station variables in $A _ { i }$ are not connected by observations to station variables in $A _ { j }$ if $i \neq j$ . Order the variables so that those in $\mathcal { A } _ { 1 } , \ldots , \mathcal { A } _ { p }$ appear first and those in $\boldsymbol { B }$ last. The dissection can also be continued by dissecting each of the regions $\mathcal { A } _ { 1 } , \ldots , \mathcal { A } _ { p }$ into separate subregions,and so on in a recursive fashion. The blocking of the region for one and two levels of dissection for $p = 2$ is pictured in Figure 4.3.1. In such a nested dissection, it is advantageous to perform the dissection in such a way that in each stage of the dissection,the numbers of variables in the two partitions are roughly the same. Also,the number of variables in the separator nodes should be as small as possible.

![](../chunks/Numerical Methods for Least Squares Problems (Åke Björck) (z-library.sk, 1lib.sk, z-lib.sk_part_0004_pages_0211-0280/auto/images/3f9b9eac12fc1a07cec687b47abb257808fe2b33f99a3636a16f89e072d896b0.jpg)  
Figure 4.3.1. One and two levels of dissection of a region.

The block structure in the matrix of the corresponding linear system induced by one and two levels of dissection for $p = 2$ is shown here:

$$
A = \left( \begin{array} { l l l } { { A _ { 1 } } } & { { } } & { { B _ { 1 } } } \\ { { } } & { { A _ { 2 } } } & { { B _ { 2 } } } \end{array} \right) , \qquad A = \left( \begin{array} { l l l l l l l } { { A _ { 1 } } } & { { } } & { { } } & { { B _ { 1 } } } & { { } } & { { D _ { 1 } } } \\ { { } } & { { A _ { 2 } } } & { { } } & { { B _ { 2 } } } & { { } } & { { D _ { 2 } } } \\ { { } } & { { } } & { { A _ { 3 } } } & { { } } & { { C _ { 3 } } } & { { D _ { 3 } } } \\ { { } } & { { } } & { { } } & { { A _ { 4 } } } & { { } } & { { C _ { 4 } } } & { { D _ { 4 } } } \end{array} \right) .
$$

There is a finer structure in $A$ not shown here. For example, in one level of dissection most of the equations involve variables in $A _ { 1 }$ or $A _ { 2 }$ only but not in $B$

For a least squares problems $\mathrm { m i n } _ { x } \| A x - b \| _ { 2 }$ arising from a one-level dissection into $p$ regions,the matrix has a bordered block diagonal or block-angular form,

$$
A = \left( \begin{array} { c c c c c } { A _ { 1 } } & & & & { B _ { 1 } } \\ & { A _ { 2 } } & & & { B _ { 2 } } \\ & & { \ddots } & & & { \vdots } \\ & & & { A _ { p } } & { B _ { p } } \end{array} \right) , \quad x = \left( \begin{array} { c } { x _ { 1 } } \\ { x _ { 2 } } \\ { \vdots } \\ { x _ { p } } \\ { x _ { p + 1 } } \end{array} \right) , \quad b = \left( \begin{array} { c } { b _ { 1 } } \\ { b _ { 2 } } \\ { \vdots } \\ { b _ { p } } \end{array} \right) ,
$$

where

$$
A _ { i } \in \mathbb { R } ^ { m _ { i } \times n _ { i } } , \quad B _ { i } \in \mathbb { R } ^ { m _ { i } \times n _ { p + 1 } } , \quad i = 1 , \dots , p ,
$$

and $m = m _ { 1 } + m _ { 2 } + \cdot \cdot \cdot + m _ { p }$ ， $n = n _ { 1 } + n _ { 2 } + \cdot \cdot \cdot + n _ { p + 1 }$ . For some problems,the blocks $A _ { i }$ and/or $B _ { i }$ are themselves large sparse matrices,often of the same general sparsity pattern as $A$ .There is a wide variation in the number and size of blocks. Some problems have large blocks with $p$ of moderate size (1O-1OO),while others have many more but smaller blocks.

The normal matrix $A ^ { T } A$ ，with $A$ given as in (4.3.14), has a doubly bordered block diagonal form

$$
\boldsymbol { A } ^ { T } \boldsymbol { A } = \left( \begin{array} { c c c c } { \boldsymbol { A } _ { 1 } ^ { T } \boldsymbol { A } _ { 1 } } & & & { \boldsymbol { A } _ { 1 } ^ { T } \boldsymbol { B } _ { 1 } } \\ & { \boldsymbol { A } _ { 2 } ^ { T } \boldsymbol { A } _ { 2 } } & & { \boldsymbol { A } _ { 2 } ^ { T } \boldsymbol { B } _ { 2 } } \\ & & { \ddots } & & { \vdots } \\ & & & { \boldsymbol { A } _ { p } ^ { T } \boldsymbol { A } _ { p } } & { \boldsymbol { A } _ { p } ^ { T } \boldsymbol { B } _ { p } } \\ { \boldsymbol { B } _ { 1 } ^ { T } \boldsymbol { A } _ { 1 } } & { \boldsymbol { B } _ { 2 } ^ { T } \boldsymbol { A } _ { 2 } } & { \cdots } & { \boldsymbol { B } _ { p } ^ { T } \boldsymbol { A } _ { p } } & { \boldsymbol { C } } \end{array} \right) ,
$$

where $\begin{array} { r } { C = \sum _ { i = 1 } ^ { p } B _ { i } ^ { T } B _ { i } } \end{array}$ . The right-hand side $f = ( f _ { 1 } , \dots , f _ { p + 1 } )$ of the normal equations is

$$
f _ { i } = A _ { i } ^ { T } b _ { i } , \quad i = 1 , \ldots , p , \quad f _ { p + 1 } = \sum _ { i = 1 } ^ { p } B _ { i } ^ { T } b _ { i } .
$$

f $\operatorname { r a n k } ( A ) = n$ ,the upper triangular Cholesky factor $R$ of $A ^ { T } A$ exists and has a block structure similar to that of $A$ ：

$$
R = \left( \begin{array} { c c c c c c } { { R _ { 1 } } } & { { } } & { { } } & { { } } & { { S _ { 1 } } } \\ { { } } & { { R _ { 2 } } } & { { } } & { { } } & { { S _ { 2 } } } \\ { { } } & { { } } & { { \ddots } } & { { } } & { { \vdots } } \\ { { } } & { { } } & { { } } & { { R _ { p } } } & { { S _ { p } } } \\ { { } } & { { } } & { { } } & { { } } & { { R _ { p + 1 } } } \end{array} \right) .
$$

Equating the blocks in $R ^ { T } R = A ^ { T } A$ gives

$$
\begin{array} { r l } & { R _ { i } ^ { T } R _ { i } = A _ { i } ^ { T } A _ { i } , \qquad R _ { i } ^ { T } S _ { i } = A _ { i } ^ { T } B _ { i } , \quad i = 1 , \ldots , p , } \\ & { R _ { p + 1 } ^ { T } R _ { p + 1 } = C - \displaystyle \sum _ { i = 1 } ^ { p } S _ { i } ^ { T } S _ { i } , } \end{array}
$$

where the Cholesky factors $R _ { i } \in \mathbb { R } ^ { n _ { i } \times n _ { i } }$ and $S _ { i }$ can be computed independently and in parallel. The least squares solution is then obtained from the two-block triangular systems $R ^ { T } z = A ^ { T } b =$ $f$ and $R x = z$ .This amounts to first solving the lower triangular systems

$$
R _ { i } ^ { T } z _ { i } = A _ { i } ^ { T } b _ { i } , \quad i = 1 , \ldots , p , \qquad R _ { p + 1 } ^ { T } z _ { p + 1 } = f _ { p + 1 } - \sum _ { i = 1 } ^ { p } S _ { i } ^ { T } z _ { i } ,
$$

and then the upper triangular systems

$$
R _ { p + 1 } x _ { p + 1 } = z _ { p + 1 } , \qquad R _ { i } x _ { i } = z _ { i } - S _ { i } x _ { p + 1 } , \quad i = 1 , \ldots , p .
$$

Again, nearly all of these systems can be solved in parallel.

A more accurate algorithm based on QR factorization for solving block-angular least squares algorithms is given by Golub,Luk,and Pagano [499,1979]. This proceeds in the following three steps:

1.Reduce the diagonal block $A _ { i }$ to upper triangular form by a sequence of orthogonal transformations applied to $( A _ { i } , B _ { i } )$ and the right-hand side $b _ { i }$ ,yielding

$$
Q _ { i } ^ { T } ( A _ { i } , B _ { i } ) = \left( { \begin{array} { c c } { R _ { i } } & { S _ { i } } \\ { 0 } & { T _ { i } } \end{array} } \right) , \qquad Q _ { i } ^ { T } b _ { i } = \left( { \begin{array} { c } { c _ { i } } \\ { d _ { i } } \end{array} } \right) , \quad i = 1 , \dots , p .
$$

Any sparse structure in the blocks $A _ { i }$ should be exploited.

2. Form

$$
T = \left( \begin{array} { c } { { T _ { 1 } } } \\ { { \vdots } } \\ { { \vdots } } \\ { { T _ { p } } } \end{array} \right) , \qquad d = \left( \begin{array} { c } { { d _ { 1 } } } \\ { { \vdots } } \\ { { \vdots } } \\ { { d _ { p } } } \end{array} \right) ,
$$

and compute the QR factorization

$$
\begin{array} { r l } { Q _ { p + 1 } ^ { T } \left( T \right. } & { { } d ) = \left( \begin{array} { c c } { R _ { p + 1 } } & { c _ { p + 1 } } \\ { 0 } & { d _ { p + 1 } } \end{array} \right) . } \end{array}
$$

The residual norm is given by $\rho = \| d _ { p + 1 } \| _ { 2 }$

3. Solve $x _ { p + 1 } , x _ { p } , \dotsc , x _ { 1 }$ from the upper triangular systems

$$
R _ { p + 1 } x _ { p + 1 } = c _ { p + 1 } , \qquad R _ { i } x _ { i } = c _ { i } - S _ { i } x _ { p + 1 } , \quad i = 1 , \ldots , p .
$$

There are several ways to organize this algorithm. In steps 1 and 3 the computations can be performed in parallel on the $p$ subsystems. It is then advantageous to continue the reduction in step 1 so that the matrices $T _ { i }$ ， $i = 1 , \ldots , p$ ,are brought into upper trapezoidal form.

Large problems may require too much memory,even if we take into account the block-angular structure. Cox [275,199o] suggests two modifications by which the storage requirement can be reduced. By merging steps 1 and 2, it is not necessary to hold all blocks $T _ { i }$ simultaneously in memory. Even more storage can be saved by discarding $R _ { i }$ and $S _ { i }$ after they have been computed in step 1 and recomputing them for step 3. Indeed,only $R _ { i }$ needs to be recomputed, because after $y$ has been computed in step 2, $x _ { i }$ is the solution to the least squares problems

$$
\operatorname* { m i n } _ { x _ { i } } \| A _ { i } x _ { i } - g _ { i } \| _ { 2 } , \qquad g _ { i } = b _ { i } - B _ { i } y .
$$

Hence,to determine $x _ { i }$ we only need to (re)compute the QR factorizations of $( A _ { i } , g _ { i } )$ ， $i \ =$ $1 , \ldots , p$ . In some practical problems this modification can reduce the storage requirement by an order of magnitude,while recomputation of $R _ { i }$ only increases the operation count by a small percentage.

From the structure of the $R$ -factor in (4.3.15), the diagonal blocks of the covariance matrix $C = ( R ^ { T } R ) ^ { - 1 } = R ^ { - 1 } R ^ { - T }$ can be writen as (see Golub, Plemmons,and Sameh [506,1988])

$$
\begin{array} { r l } & { C _ { p + 1 , p + 1 } = R _ { p + 1 } ^ { - 1 } R _ { p + 1 } ^ { - T } , } \\ & { C _ { i , i } = R _ { i } ^ { - 1 } ( I + W _ { i } ^ { T } W _ { i } ) R _ { i } ^ { - T } , \quad W _ { i } ^ { T } = S _ { i } R _ { p + 1 } ^ { - 1 } , \quad i = 1 , \ldots , p . } \end{array}
$$

Hence,if we compute the QR factorizations

$$
Q _ { i } \left( { \begin{array} { c } { W _ { i } } \\ { I } \end{array} } \right) = \left( { \begin{array} { c } { U _ { i } } \\ { 0 } \end{array} } \right) , \quad i = 1 , \ldots , p ,
$$

we have $I + W _ { i } ^ { T } W _ { i } = U _ { i } ^ { T } U _ { i }$ and

$$
\begin{array} { r } { C _ { i , i } = ( U _ { i } R _ { i } ^ { - T } ) ^ { T } ( U _ { i } R _ { i } ^ { - T } ) , \quad i = 1 , \ldots , p . } \end{array}
$$

This method assumes that all the matrices $R _ { i }$ and $S _ { i }$ have been retained. For a discussion of how to compute variances and covariances when the storage saving algorithm is used, see Cox [275, 1990].

In some applications the matrices $R _ { i }$ will be sparse,but a lot of fill occurs in the blocks $B _ { i }$ in step 1. Then the triangular matrix $R _ { p + 1 }$ will be full and expensive to compute. For such problems a block-preconditioned iterative method may be more efcient; see Section 6.3. Then an iterative method,such as CGLS or LSQR,is applied to the problem

$$
\operatorname* { m i n } _ { y } \| ( A M ^ { - 1 } ) y - b \| _ { 2 } , \quad y = M x ,
$$

where a suitable preconditioner is $M = \operatorname { d i a g } \left( R _ { 1 } , \dotsc , R _ { p } , R _ { p + 1 } \right)$ ; see Golub, Manneback, and Toint [500, 1986].

# Notes and references

Dissection and orthogonal decompositions in geodetic survey problems are treated by Golub and Plemmons [505,198o]. Avila and Tomlin [44,1979] discuss parallelism in the solution of very large least squares problems by nested dissection and the method of normal equations. Weil and Kettler [1116,1971] give a heuristic algorithm for permuting a general sparse matrix into blockangular form. The dissection procedure described above is a variation of the nested dissection orderings developed for general sparse positive definite systems; see Section 5.1.5.

# 4.3.3 - Kronecker Product Structure

Sometimes least squares problems occur with a highly regular block structure. Here we consider least squares problems of the form

$$
\operatorname* { m i n } _ { x } \| ( A \otimes B ) x - f \| _ { 2 } ,
$$

where $A \otimes B$ is the Kronecker product of $A \in \mathbb { R } ^ { m \times n }$ and $B \in \mathbb { R } ^ { p \times q }$ . This product is the $m p \times n q$ block matrix

$$
A \otimes B = \left( \begin{array} { c c c c } { { a _ { 1 1 } B } } & { { a _ { 1 2 } B } } & { { \cdot \cdot \cdot } } & { { a _ { 1 n } B } } \\ { { a _ { 2 1 } B } } & { { a _ { 2 2 } B } } & { { \cdot \cdot \cdot } } & { { a _ { 2 n } B } } \\ { { \vdots } } & { { \vdots } } & { { \vdots } } \\ { { a _ { m 1 } B } } & { { a _ { m 2 } B } } & { { \cdot \cdot \cdot } } & { { a _ { m n } B } } \end{array} \right) .
$$

Problems with Kronecker structure arise in several application areas, including signal and image processing, photogrammetry,and multidimensional approximation; see Fausett and Fulton [399, 1994]. Grosse $[ 5 4 0 , 1 9 8 0 ]$ describes a tensor factorization algorithm and how it applies to least squares fiting of multivariate data on a rectangular grid. Such problems can be solved with great savings in storage and operations. These savings are essential for problems where $A$ and $B$ are large. It is not unusual to have several hundred thousand equations and unknowns.

The Kronecker product and its relation to linear matrix equations, such as Lyapunov's equation,are treated in Horn and Johnson [640,1991, Chapter 4]. See also Henderson and Searle [602, $\mathbf { 1 9 8 1 } ]$ and Van Loan [1O83, 2ooo]. We now state some elementary facts about Kronecker products that follow from its definition:

$$
\begin{array} { r l } & { ( A + B ) \otimes C = ( A \otimes C ) + ( B \otimes C ) , } \\ & { A \otimes ( B + C ) = ( A \otimes B ) + ( A \otimes C ) , } \\ & { A \otimes ( B \otimes C ) = ( A \otimes B ) \otimes C , } \\ & { ( A \otimes B ) ^ { T } = A ^ { T } \otimes B ^ { T } . } \end{array}
$$

A further important relation, which is not so obvious,is given next.

Lemma 4.3.3. If the ordinary products $A C$ and $B D$ are defined, then

$$
( A \otimes B ) ( C \otimes D ) = A C \otimes B D .
$$

Proof. See Lancaster and Tismenetsky [713,1985, Chap. 12.1].

As a corollary of this lemma we obtain the identity

$$
( A _ { 1 } \otimes B _ { 1 } ) ( A _ { 2 } \otimes B _ { 2 } ) \cdot \cdot \cdot ( A _ { p } \otimes B _ { p } ) = ( A _ { 1 } A _ { 2 } \cdot \cdot \cdot A _ { n } ) \otimes ( B _ { 1 } B _ { 2 } \cdot \cdot \cdot B _ { n } ) ,
$$

assuming al the products are defined. We can also conclude that if $P$ and $Q$ are orthogonal $n \times n$ matrices, then $P \otimes Q$ is an orthogonal $n ^ { 2 } \times n ^ { 2 }$ matrix. Furthermore,if $A$ and $B$ are square and nonsingular, it follows that $A \otimes B$ is nonsingular and

$$
( A \otimes B ) ^ { - 1 } = A ^ { - 1 } \otimes B ^ { - 1 } .
$$

This generalizes to pseudoinverses, as shown in the following lemmas.

Lemma 4.3.4. Let $A ^ { \dagger }$ and $B ^ { \dagger }$ be the pseudoinverses of $A$ and $B$ Then

$$
( A \otimes B ) ^ { \dagger } = A ^ { \dagger } \otimes B ^ { \dagger } .
$$

Proof. The lemma follows by verifying that $X = A ^ { \dagger } \otimes B ^ { \dagger }$ satisfies the four Penrose conditions in Theorem 1.2.11. □

We now introduce a function, closely related to the Kronecker product, that converts a matrix into a vector. For a matrix $C = ( c _ { 1 } , c _ { 2 } , \ldots , c _ { n } ) \in \mathbb { R } ^ { m \times n }$ we define

$$
\operatorname { v e c } \left( C \right) = \left( { c _ { 2 } } \right) .
$$

Hence vec $( C )$ is the vector formed by stacking the columns of $C$ into one column vector of length mn.We now state a result that shows how the vec-function is related to the Kronecker product.

Lemma 4.3.5. If $A \in \mathbb { R } ^ { m \times n }$ ， $B \in \mathbb { R } ^ { p \times q }$ ,and $F \in \mathbb { R } ^ { q \times n }$ ,then

$$
( A \otimes B ) \mathrm { v e c } ( F ) = \mathrm { v e c } ( B F A ^ { T } ) .
$$

By Lemma 4.3.5, we can write the solution to the Kronecker least squares problem (4.3.23 as

$$
\begin{array} { r } { x = ( A \otimes B ) ^ { \dagger } f = ( A ^ { \dagger } \otimes B ^ { \dagger } ) f = \mathrm { v e c } ( B ^ { \dagger } F ( A ^ { \dagger } ) ^ { T } ) , } \end{array}
$$

where $f = \operatorname { v e c } \left( F \right)$ . This allows a great reduction in the cost of solving (4.3.23). For example, if both $A$ and $B$ are $m \times n$ matrices, the cost of computing the least squares solution is reduced from $O ( m ^ { 2 } n ^ { 4 } )$ to $O ( m n ^ { 2 } )$ .

In some areas, the most common approach to computing the least squares solution to (4.3.23) is from normal equations.If we assume that both $A$ and $B$ have full column rank,we can use the expressions

$$
A ^ { \dagger } = ( A ^ { T } A ) ^ { - 1 } A ^ { T } , \qquad B ^ { \dagger } = ( B ^ { T } B ) ^ { - 1 } B ^ { T } .
$$

However, because of the instability associated with the explicit formation of $A ^ { T } A$ and $B ^ { T } B$ ,an approach based on orthogonal decompositions should generally be preferred. From the complete QR factorizations of $A$ and $B$ ，

$$
A \Pi _ { 1 } = Q _ { 1 } \left( \begin{array} { c c } { { R _ { 1 } } } & { { 0 } } \\ { { 0 } } & { { 0 } } \end{array} \right) V _ { 1 } ^ { T } , \qquad B \Pi _ { 2 } = Q _ { 2 } \left( \begin{array} { c c } { { R _ { 2 } } } & { { 0 } } \\ { { 0 } } & { { 0 } } \end{array} \right) V _ { 2 } ^ { T } ,
$$

with $R _ { 1 } , R _ { 2 }$ upper triangular and nonsingular, we obtain

$$
\begin{array} { r } { A ^ { \dagger } = \Pi _ { 1 } V _ { 1 } \left( \begin{array} { c c } { R _ { 1 } ^ { - 1 } } & { 0 } \\ { 0 } & { 0 } \end{array} \right) Q _ { 1 } ^ { T } , \qquad B ^ { \dagger } = \Pi _ { 2 } V _ { 2 } \left( \begin{array} { c c } { R _ { 2 } ^ { - 1 } } & { 0 } \\ { 0 } & { 0 } \end{array} \right) Q _ { 2 } ^ { T } . } \end{array}
$$

These expressions can be used in (4.3.27) to compute the pseudoinverse solution of problem (4.3.23),even in the rank-deficient case.

From Lemma 4.3.5, the following simple expression for the singular values and vectors of the Kronecker product $A \otimes B$ ,in terms of the singular values and vectors of $A$ and $B$ ,is obtained.

Lemma 4.3.6. Let $A$ and $B$ have the SVDs $A = U _ { 1 } \Sigma _ { 1 } V _ { 1 } ^ { T }$ and $B = U _ { 2 } \Sigma _ { 2 } V _ { 2 } ^ { T }$ . Then

$$
A \otimes B = ( U _ { 1 } \otimes U _ { 2 } ) ( \Sigma _ { 1 } \otimes \Sigma _ { 2 } ) ( V _ { 1 } \otimes V _ { 2 } ) ^ { T }
$$

is the SVD of $A \otimes B$

Barrlund [84,1998] develops an efficient solution method for constrained least squares problems with Kronecker structure:

$$
\operatorname* { m i n } _ { x } \| ( A _ { 1 } \otimes A _ { 2 } ) x - f \| _ { 2 } { \mathrm { s u b j e c t } } \operatorname { t o } ( B _ { 1 } \otimes B _ { 2 } ) x = g .
$$

With $\operatorname { v e c } \left( X \right) = x$ ， $\operatorname { v e c } \left( F \right) = f$ , and vec $( G ) = g$ , this becomes

$$
\operatorname* { m i n } _ { X } \| A _ { 2 } X A _ { 1 } ^ { T } - F \| _ { F } \quad { \mathrm { s u b j e c t ~ t o } } \quad B _ { 2 } X B _ { 1 } ^ { T } = G .
$$

This problem can be solved by a nulspace method; cf. Section 3.4.2. By a change of variables the unknowns are split into two sets.The first set is determined by the constraints,and the other set belongs to the nullspace of the constraints.

# 4.3.4 - Strongly Rectangular Systems

The least squares problem

$$
\operatorname* { m i n } _ { x \in S } \| x \| _ { 2 } , \quad S = \{ x \in \mathbb { R } ^ { n } \mid \| b - A x \| _ { 2 } = \operatorname* { m i n } \} ,
$$

where $A \in \mathbb { R } ^ { m \times n }$ , is said to be strongly overdetermined if $m \gg n$ and strongly underdetermined if $m \ll n$ . Candes et al. [2O5, 2o11] mentions a case in stationary video background subtraction, where $n$ is about $1 0 ^ { 3 }$ and $m$ can exceed $1 0 ^ { 6 }$ ．Examples from other application areas,such as seismology, natural language processing, and analysis of the human genome,are given by Meng [788,2014].

Demmel et al. [306, 2o12] give a family of stable, efcient, and communication-reducing algorithms called TSQR for computing the QR factorization of a strongly overdetermined matrix $A \in \mathbb { R } ^ { m \times n }$ ， $m \gg n$ . (Such matrices are also called “tall-and-skinny."） In TSQR a rowwise partitioning of $A$ into blocks $A _ { i }$ ， $i = 0 , \ldots , N - 1$ , is used.In the first stage,factorizations

$$
A _ { i } = Q _ { i } R _ { i } , \quad i = 0 , \dots , N - 1 ,
$$

are computed. Subsequent stages merge pairs of the resulting upper triangular matrices in a divide-and-conquer fashion until a single factor $R$ has been obtained. This requires about $\log _ { 2 } N$ stages. The algorithm is exemplified below for $N = 4$ .After the first step we have obtained

$$
A = \left( \begin{array} { l } { A _ { 0 } } \\ { A _ { 1 } } \\ { A _ { 2 } } \\ { A _ { 3 } } \end{array} \right) = \left( \begin{array} { l } { Q _ { 0 } R _ { 0 } } \\ { Q _ { 1 } R _ { 1 } } \\ { Q _ { 2 } R _ { 2 } } \\ { Q _ { 3 } R _ { 3 } } \end{array} \right) = \left( \begin{array} { l l l l } { Q _ { 0 } } & & & \\ & { Q _ { 1 } } & & \\ & & { Q _ { 2 } } & \\ & & & { Q _ { 2 } } \end{array} \right) \left( \begin{array} { l } { R _ { 0 } } \\ { R _ { 1 } } \\ { R _ { 2 } } \\ { R _ { 3 } } \end{array} \right) .
$$

In the next two steps the QR factorizations of the stacked upper triangular factors are merged into one upper triangular matrix

$$
\left( \begin{array} { l } { { \left( \begin{array} { l } { { R _ { 0 } } } \\ { { R _ { 1 } } } \end{array} \right) } } \\ { { \left( \begin{array} { l } { { R _ { 2 } } } \\ { { R _ { 3 } } } \end{array} \right) } } \end{array} \right) = \left( \begin{array} { l l } { { Q _ { 0 1 } } } & { { } } \\ { { } } & { { Q _ { 2 3 } } } \end{array} \right) \left( \begin{array} { l } { { R _ { 0 1 } } } \\ { { R _ { 2 3 } } } \end{array} \right) , \qquad \left( \begin{array} { l } { { R _ { 0 1 } } } \\ { { R _ { 2 3 } } } \end{array} \right) = Q _ { 0 , 1 , 2 , 3 } R .
$$

The representation of the factor $Q$ in TSQR is different from the standard Householder QR factorization. It is implicitly given by a tree of smaller Householder transformations

$$
Q = \left( \begin{array} { c c c c } { { Q _ { 0 } } } & { { } } & { { } } & { { } } \\ { { } } & { { Q _ { 1 } } } & { { } } & { { } } \\ { { } } & { { } } & { { Q _ { 2 } } } & { { } } \\ { { } } & { { } } & { { } } & { { Q _ { 2 } } } \end{array} \right) \left( \begin{array} { c c c } { { Q _ { 0 1 } } } & { { } } & { { } } \\ { { } } & { { Q _ { 2 3 } } } \end{array} \right) Q _ { 0 , 1 , 2 , 3 } .
$$

In general, the combination process in TSQR forms a tree with the row blocks $A _ { i }$ as leaves and the final $R$ as a root. The version pictured above corresponds to a binary tree. The tree shape can be chosen to minimize either the communication between processors or the volume of memory trafic between the main memory and the cache memory of each processor.

The initial Householder QR factorizations of the $N$ blocks $A _ { i }$ require $2 N n ^ { 2 } ( p - n / 3 )$ flops. Merging two triangular QR factorizations of dimension $n \times n$ takes $2 n ^ { 3 } / 3$ flops．The total arithmetic cost of TSQR is higher than that for the direct Householder QR factorization of $A$ ， but for strongly rectangular systems most of the arithmetic work is spent in computing the QR factorizations of the submatrices,which can be done in parallel.

An implementation of TSQR using the message passage interface (MPI) operation AllReduce for multiple processors is given by Langou [719, 2oo7]. Experiments show that the AllReduce QR algorithm obtains nearly linear speed-up. As shown by Mori et al.[811, 2o12],although the number of floating-point operations is larger, the bounds for the backward error and the deviation from orthogonality are smaller for the AllReduce QR algorithm than for standard Householder QR.

Another communication-avoiding QR algorithm suitable for tall-and-skinny matrices is the Cholesky QR algorithm. Let $A \in \mathbb { R } ^ { m \times n }$ have full column rank and $A ^ { T } A = R ^ { T } R$ be its Cholesky factorization. The Cholesky QR algorithm then computes $Q _ { 1 } = A R ^ { - 1 }$ by block forward substitution, giving

$$
A = Q _ { 1 } R ;
$$

see Section 1.2.1. The arithmetic cost of this algorithm is $2 m n ^ { 2 } + n ^ { 3 } / 3$ flops. The Cholesky QR algorithm is ideal from the viewpoint of high performance computing. It requires only one global reduction between parallel processing units,and most of the arithmetic work can be performed as matrix-matrix operations.However, the loss of orthogonality $\| I - Q _ { 1 } ^ { T } Q _ { 1 } \| _ { F }$ can only be bounded by the squared condition number of $A$

Yamamoto et al.[1136, 2015] suggest a modified Cholesky QR2 algorithm, where $R$ and $Q _ { 1 }$ from Cholesky QR are refined as follows.First,compute $E = Q _ { 1 } ^ { T } Q _ { 1 }$ and its Cholesky factorization $E = S ^ { T } S$ .The refined factorization is taken to be $A = P U$ ,where

$$
P = Q S ^ { - 1 } , \quad U = S R .
$$

This updating step doubles the arithmetic cost. The Cholesky QR2 algorithm has good stability properties provided the initial Cholesky factorization does not break down. However, the QR2 algorithm may fail for matrices with a condition number roughly greater than $\mathbf { u } ^ { - 1 / 2 }$

Yamazaki, Tomov,and Dongarra [1137, 2o15] extend the applicability of the Cholesky QR2 algorithm as follows. An initial Cholesky factorization of $R ^ { T } R = A ^ { T } A + s I$ is computed, where $s \geq 0$ is a shift that guarantees that the factorization runs to completion. Further, some intermediate results are accumulated in higher precision. The resulting Cholesky QR3 algorithm uses three Cholesky QR steps and yields a computed $Q$ with loss of orthogonality $\lVert I - Q _ { 1 } ^ { T } Q _ { 1 } \rVert _ { F }$ and residual $\| A - Q R \| _ { F } / \| A \| _ { F }$ of order u. See also Fukaya et al. [435, 2020].

# 4.3.5 - Multilinear and Tensor Calculus

In many science and engineering applications,the data encountered have a multidimensional structure with more than two dimensions. Consider vector spaces $X _ { 1 }$ ， $X _ { 2 } , \ldots$ ， $X _ { d }$ and $Y$ ，and let $x _ { \nu } \in X _ { \nu }$ . A function $A \colon X _ { 1 } \times X _ { 2 } \times \cdots \times X _ { d } \to Y$ is called $d$ -multilinearif itis linear in each of its arguments $x _ { i }$ separately. For example, the expression $( P x _ { 1 } ) ^ { T } Q x _ { 2 } + ( R x _ { 3 } ) ^ { T } S x _ { 4 }$ defines a four-linear function, mapping or operator, provided the constant matrices $P , Q , R , S$ have appropriate size. If $d = 2$ ,the term bilinear function is used.

Let $X _ { \nu } = \mathbb { R } ^ { n _ { \nu } }$ ， $\nu = 1 , 2 , \ldots , d$ ， $Y = \mathbb { R } ^ { m }$ ,and let $e _ { j _ { i } }$ be one of the basis vectors of $X _ { i }$ Thensuperscriptscanbeused todenotecoordinates inthesespaces.For example,@.jd denotes the ith coordinate of $A ( e _ { j _ { 1 } } , e _ { j _ { 2 } } , \dots , e _ { j _ { d } } )$ .Because of the linearity, the $i$ th coordinate of $A ( x _ { 1 } , x _ { 2 } , \ldots , x _ { d } )$ ， $x _ { \nu } \in X _ { \nu }$ ,reads

$$
\sum _ { j _ { 1 } = 1 } ^ { n _ { 1 } } \sum _ { j _ { 2 } = 1 } ^ { n _ { 2 } } \ldots \sum _ { j _ { k } = 1 } ^ { n _ { k } } a _ { j _ { 1 } , j _ { 2 } , \ldots , j _ { d } } ^ { i } x _ { 1 } ^ { j _ { 1 } } x _ { 2 } ^ { j _ { 2 } } \ldots x _ { d } ^ { j _ { d } } .
$$

The following sum convention is often used. If an index occurs as both a subscript and a su-perscript, the product should be summed over the range of this index. For example, the ith coordinate of $A ( x _ { 1 } , x _ { 2 } , \ldots , x _ { d } )$ is writen $a _ { j _ { 1 } , j _ { 2 } , \ldots , j _ { d } } ^ { i } x _ { 1 } ^ { j _ { 1 } } x _ { 2 } ^ { j _ { 2 } } \cdot \cdot \cdot x _ { k } ^ { j _ { d } } .$ 2.. (Remember the superscripts are not exponents.)

Suppose $X _ { i } = X$ ， $i = 1 , 2 , \ldots , d$ 、Then the set of $d$ -linear mappings from $X ^ { k }$ to $Y$ is itself a linear space, denoted by $L _ { k } ( X , Y )$ . For $k = 1$ ,we have the space of linear functions.Linear functions can,of course, be described in vector-matrix notation as a set of matrices $L ( \mathbb { R } ^ { n } , \mathbb { R } ^ { m } ) =$ $\mathbb { R } ^ { m \times n }$ . Matrix notation can also be used for each coordinate of a bilinear function. Norms of multilinear operators are defined analogously to subordinate matrix norms. For example,

$$
\begin{array} { r } { \| A ( x _ { 1 } , x _ { 2 } , \ldots , x _ { k } ) \| _ { \infty } \leq \| A \| _ { \infty } \| x _ { 1 } \| _ { \infty } \| x _ { 2 } \| _ { \infty } \ldots \| x _ { k } \| _ { \infty } , } \end{array}
$$

where

$$
\| A \| _ { \infty } = \operatorname* { m a x } _ { i = 1 } ^ { m } \sum _ { j _ { 1 } = 1 } ^ { n _ { 1 } } \sum _ { j _ { 2 } = 1 } ^ { n _ { 2 } } \cdot \cdot \cdot \sum _ { j _ { k } = 1 } ^ { n _ { k } } | a _ { j _ { 1 } , j _ { 2 } , \dots , j _ { k } } ^ { i } | .
$$

A multilinear function $A$ is called symmetric if $A ( x _ { 1 } , x _ { 2 } , \ldots , x _ { k } )$ is symmetric with respect to its arguments. In the cases mentioned above, where matrix notation can be used, the matrix becomes symmetric if the multilinear function is symmetric.

Multidimensional data can be represented by a tensor or, using a coordinate representation, a hypermatrix. Mathematical theory and computational methods for tensor problems are still being developed, and notation may vary among papers. In the following, we denote tensors by calligraphic letters; e.g., we refer to

$$
\mathcal { A } = ( a _ { i _ { 1 } , . . . , i _ { d } } ) \in \mathbb { R } ^ { n _ { 1 } \times \cdots \times n _ { d } }
$$

as a $d$ -mode tensor, $d > 2$ The case $d = 2$ corresponds to matrices. In the following we emphasize the case $d = 3$ because the main difference between matrices and hypermatrices comes in the transition from $d = 2$ to 3.Subarrays are formed by keeping a subset of the indices constant.A 3-mode tensor (4.3.38) can be thought of as being built up by matrix slices in three ways by fixing one of the indices, e.g.,

$$
\begin{array} { r } { ( a _ { : , : , j } ) \in \mathbb { R } ^ { n _ { 1 } \times n _ { 2 } } , \quad j = 1 : n _ { 3 } . } \end{array}
$$

Similarly,by fixing any two indices, we get a vector or fiber

$$
\begin{array} { r } { ( a _ { : , j , k } ) \in \mathbb { R } ^ { n _ { 1 } } , \quad j = 1 : n _ { 2 } , \quad k = 1 : n _ { 3 } . } \end{array}
$$

A tensor is said to be symmetric if its elements are equal under any permutations of the indices, i.e., for a 3-mode tensor,

$$
a _ { i , j , k } = a _ { i , k , j } = a _ { j , k , i } = a _ { j , i , k } = a _ { k , i , j } = a _ { k , j , i } \ \forall { i , j , k } ;
$$

see Comon et al.[263,2oo8]. A tensor is diagonal if $a _ { i _ { 1 } , i _ { 2 } , \dots , i _ { d } } \neq 0$ only if $i _ { 1 } = i _ { 2 } = \cdot \cdot \cdot = i _ { d }$

Elementwise addition and scalar multiplication trivially extend to hypermatrices of arbitrary order. The tensor or outer product is denoted by $\circ$ (not to be confused with the Hadamard product of matrices). For example, if $A = ( a _ { i j } ) \in \mathbb { R } ^ { m \times n }$ and $B = ( b _ { k l } ) \in \mathbb { R } ^ { p \times q }$ are matrices, then

$$
\mathcal { C } = A \circ B = ( a _ { i , j , k , l } )
$$

is a 4-mode tensor. The 1-mode contraction product of two 3-mode hypermatrices ${ \mathcal { A } } =$ $( a _ { i , j , k } ) \in \mathbb { R } ^ { n \times n _ { 2 } \times n _ { 3 } }$ and $\boldsymbol { B } = ( b _ { i , l , m } ) \in \mathbb { R } ^ { n \times m _ { 2 } \times m _ { 3 } }$ with conforming first dimension is the 4-mode tensor $\mathcal { C } \in \mathbb { R } ^ { n _ { 2 } \times n _ { 3 } \times m _ { 2 } \times m _ { 3 } }$ defined as

$$
\mathcal { C } = \langle \mathcal { A } , \mathcal { B } \rangle _ { 1 } , \quad c _ { j , k , l , m } = \sum _ { i = 1 } ^ { n } a _ { i , j , k } b _ { i , l , m } .
$$

Contractions need not be restricted to one pair of indices at a time.The inner product of two 3-mode tensors of the same size and the Frobenius norm of a tensor are defined as

$$
\langle \boldsymbol { A } , \boldsymbol { B } \rangle = \sum _ { i , j , k } a _ { i j k } b _ { i j k } , \qquad \| \boldsymbol { A } \| _ { F } ^ { 2 } = \langle \boldsymbol { A } , \boldsymbol { A } \rangle ^ { 1 / 2 } = \sum _ { i , j , k } a _ { i j k } ^ { 2 } .
$$

The matrix Holder norm for $p = 1 , \infty$ is similarly generalized.

The columns of $A$ can be stacked or unfolded into a column vector by the operation $\mathrm { v e c } ( A )$ A second way would be to unfold its rows into a row vector. Similarly,a 3-mode tensor $\mathcal { A }$ can be unfolded or matricized by stacking in some order the matrix slices obtained by fixing one of its three modes.Following Eldén and Savas [380,2oog],we use the notation

$$
\begin{array} { r l } & { A _ { ( 1 ) } = ( A _ { : , 1 , : } , A _ { : , 2 , : } , \ldots , A _ { : , n _ { 2 } , : } ) \in \mathbb R ^ { n _ { 1 } \times n _ { 2 } n _ { 3 } } , } \\ & { A _ { ( 2 ) } = ( A _ { : , : , 1 } ^ { T } , A _ { : , : , 2 } ^ { T } , \ldots , A _ { : : , n _ { 3 } } ^ { T } ) \in \mathbb R ^ { n _ { 2 } \times n _ { 1 } n _ { 3 } } , } \\ & { A _ { ( 3 ) } = ( A _ { 1 , : , : } ^ { T } , A _ { 2 , : , : } ^ { T } , \ldots , A _ { n _ { 1 } , : , : } ^ { T } ) \in \mathbb R ^ { n _ { 3 } \times n _ { 1 } n _ { 2 } } , } \end{array}
$$

where a colon indicates all elements of a mode. Different papers sometimes use different orderings of the columns. The specific permutation is not important as long as it is consistent.

A matrix $C \in \mathbb { R } ^ { p \times q }$ can be multiplied from the left and right by other matrices $\ b X \in \mathbb { R } ^ { m \times p }$ and $Y \in \mathbb { R } ^ { n \times q }$ , and we write

$$
A = X C Y ^ { T } , \qquad a _ { i j } = \sum _ { \alpha = 1 } ^ { p } \sum _ { \beta = 1 } ^ { q } x _ { i \alpha } y _ { j \beta } c _ { \alpha \beta } .
$$

The corresponding tensor-matrix multiplication of a 3-mode tensor $\mathcal { C } \in \mathbb { R } ^ { p \times q \times r }$ by three matrices $\boldsymbol { X } \in \mathbb { R } ^ { l \times p }$ ， $Y \in \mathbb { R } ^ { m \times q }$ ,and $Z \in \mathbb { R } ^ { n \times r }$ transforms $\mathcal { C }$ into the 3-mode tensor $\mathcal { A } \in \mathbb { R } ^ { l \times m \times n }$ with entries

$$
a _ { i j k } = \sum _ { \alpha = 1 } ^ { p } \sum _ { \beta = 1 } ^ { q } \sum _ { \gamma = 1 } ^ { r } x _ { i , \alpha } y _ { j , \beta } z _ { k \gamma } c _ { \alpha \beta \gamma } .
$$

A notation for this operation suggested by Silva and Lim [993, 2008] is

$$
{ \mathcal { C } } = ( X , Y , Z ) \cdot A ,
$$

where the mode of each multiplication is understood from the ordering of the matrices. It is convenient to use a separate notation for multiplication by transposed matrices. For ${ \mathcal { C } } =$ $( X ^ { T } , Y ^ { T } , Z ^ { T } ) \cdot { \mathcal { A } }$ we also write

$$
{ \mathcal { C } } = { \mathcal { A } } \cdot ( X , Y , Z ) .
$$

For a matrix $A \in \mathbb { R } ^ { m \times n }$ there are three ways to define the rank $r$ ,all of which yield the same value. The rank is equal to the dimension of the subspace of $\mathbb { R } ^ { m }$ spanned by its columns and the dimension of the subspace of $\mathbb { R } ^ { n }$ spanned by its rows.Also,the rank is the minimum number of terms in the expansion of $A$ as a sum of rank-one matrices; cf. the SVD expansion. For a tensor of mode $d > 2$ ,these three definitions yield different results.

The column rank and row rank of a matrix are generalized as follows. For a 3-mode tensor $\mathcal { A } \in \mathbb { R } ^ { n _ { 1 } \times n _ { 2 } \times n _ { 3 } }$ ,let $r _ { 1 }$ be the dimension of the subspace of $\mathbb { R } ^ { n _ { 1 } }$ spanned by the $n _ { 2 } n _ { 3 }$ vectors with entries $a _ { : , i _ { 2 } , i _ { 3 } } , i _ { 2 } = 1 : n _ { 2 } , i _ { 3 } = 1 : n _ { 3 }$ . In other words, $r _ { 1 } ( \mathcal { A } ) = \mathrm { r a n k } ( A _ { ( 1 ) } )$ , with similar interpretations for $r _ { 2 }$ and $r _ { 3 }$ . The triple $( r _ { 1 } , r _ { 2 } , r _ { 3 } )$ is called the multirank of $\mathcal { A }$ and $r _ { 1 } , r _ { 2 } , r _ { 3 }$ can all be different.

The outer product of vectors $\boldsymbol { x } \in \mathbb { R } ^ { \ell }$ ， $y \in \mathbb { R } ^ { m }$ ,and $z \in \mathbb { R } ^ { n }$ is the 3-mode hypermatrix

$$
\mathcal { T } = x \circ y \circ z \in \mathbb { R } ^ { l \times m \times n } , \quad t _ { i _ { 1 } i _ { 2 } i _ { 3 } } = x _ { i _ { 1 } } y _ { i _ { 2 } } z _ { i _ { 3 } } .
$$

If nonzero, we call this a rank-one tensor. The tensor rank of $\mathcal { A }$ is the smallest number $r$ such that $\mathcal { A }$ may be written as a sum of rank-one hypermatrices:

$$
\mathcal { A } = \sum _ { p = 1 } ^ { r } x _ { p } \circ y _ { p } \circ z _ { p } .
$$

When $d = 2$ this definition agrees with the usual definition of the rank of a matrix. Generalization of this definition of rank to higher order tensors is straightforward.However, for $d \geq 3$ there is no algorithm for determining the rank of a given tensor,and this problem is NP-hard.Furthermore, de Silva and Lim [993,2oo8] show that the problem of finding the best rank- $p$ approximation in general has no solution, even for $d = 3$

Tensor decompositions originated with Hitchcock [629,1927] and much later were taken up and used to analyze data in psychometrics (Tucker [1O70,1966]). In the last decades the use of tensor methods has spread to other fields,such as chemometrics (Bro [180,1997l),signal and image processing,data mining,and patern recognition (Eldén [376, 2o19]). Tensor decompositions are used in machine learning and parameter estimation.

Low-rank approximations of a given two-dimensional array of data can be found from the SVD of a matrix. In many applications one would like to approximate a given tensor $\mathcal { A }$ with a sum of rank-one tensors to minimize

$$
\left. \boldsymbol { \mathcal { A } } - \sum _ { i = 1 } ^ { p } \lambda _ { i } \boldsymbol { x } _ { i } \circ y _ { i } \circ z _ { i } \right. _ { F } .
$$

Weights $\lambda _ { i }$ are introduced to let us assume that vectors $x _ { i } , y _ { i }$ ，and $z _ { i }$ are normalized to have length one.Hillar and Lim [628,2O13] have shown that this problem (and indeed, most other tensor problems) are NP-hard. Therefore,we assume that the number $p < r$ of factors is fixed. A popular algorithm for computing such an approximate decomposition is alternating least squares (ALS). First, the vectors $y _ { i }$ and $z _ { i }$ are fixed, and $x _ { i }$ is determined to minimize (4.3.46). Next, $x _ { i } , z _ { i }$ are fixed,and we solve for $y _ { i }$ .Finally, $x _ { i } , y _ { i }$ are fixed,and we solve for $z _ { i }$ .Define the matrices

$$
\begin{array} { r } { X = ( x _ { 1 } , \dotsc , x _ { p } ) \in \mathbb { R } ^ { n _ { 1 } \times p } , \quad Y = ( y _ { 1 } , \dotsc , y _ { p } ) \in \mathbb { R } ^ { n _ { 2 } \times p } , \quad Z = ( z _ { 1 } , \dotsc , z _ { p } ) \in \mathbb { R } ^ { n _ { 3 } \times p } . } \end{array}
$$

With $y _ { i } , z _ { i }$ fixed, the minimizing problem can be written in matrix form as

$$
\operatorname* { m i n } _ { X } \| A _ { ( 1 ) } - \widehat { X } ( Z \odot Y ) ^ { T } \| _ { F } ,
$$

where $A _ { ( 1 ) } \in \mathbb { R } ^ { n _ { 1 } \times n _ { 2 } n _ { 3 } }$ is the matrix obtained by unfolding $\mathcal { A }$ along the first mode, and

$$
Z \odot Y = ( z _ { 1 } \otimes y _ { 1 } , \dots , z _ { p } \otimes y _ { p } ) \in \mathbb { R } ^ { n _ { 2 } n _ { 3 } \times p }
$$

is the matching columnwise Kronecker product, also called the Khatri-Rao product, of $Z$ and $Y$ The solution can be written

$$
\hat { X } = A _ { ( 1 ) } [ ( Z \odot Y ) ^ { T } ] ^ { \dagger } ,
$$

and then the columns of $\hat { X }$ are normalized to give $\hat { X } = X \mathrm { d i a g } \left( \lambda _ { i } \right)$ .Because of the special form of the Khatri-Rao product, the solution can also be written as

$$
\hat { X } = X _ { ( 1 ) } ( Z \odot Y ) ( Z ^ { T } Z . * Y ^ { T } Y ) ^ { \dagger } ,
$$

where $^ *$ is the Hadamard (elementwise） matrix product. This version is not always suitable because of the squared condition number. Similar formulas for the two other modes are easily derived. At each inner iteration a pseudoinverse must be computed. ALS can take many iterations and is not guaranteed to converge to a global minimum. Also,the solution obtained depends on the starting point.

The idea of expressing a tensor as a sum of rank-one tensors has been proposed under different names by several authors. In psychometrics it was called CANDECOMP (canonical decom-position) and PARAFAC (parallel factors); see Kolda and Bader [7O5, 2oo9]. Here, following Leurgans,Ross,and Abel [735,1993l, we callit the CP decomposition. In matrix computations, the SVD expansion

$$
A = U \Sigma V ^ { T } = \sum _ { i = 1 } ^ { r } \sigma _ { i } u _ { i } v _ { i } ^ { T } \in \mathbb { R } ^ { m \times n } , \quad r \leq \operatorname* { m i n } \{ m , n \} ,
$$

expresses a matrix $A$ of rank $r$ as the weighted sum of rank-one matrices $u _ { i } v _ { i } ^ { T }$ ,where $u _ { i } \in \mathbb { R } ^ { m }$ and $v _ { i } \in \mathbb { R } ^ { n }$ ， $i = 1 : r$ ，are mutually orthogonal. This expansion has the desirable property that for any unitarily invariant norm, the best approximation of $A$ by a matrix of rank $r < n$ is obtained by truncating the expansion; see the Eckart-Young-Mirksy Theorem 1.3.8.

The high-order SVD (HOSVD) is a generalization of the SVD to 3-mode hypermatrices

$$
\mathcal { A } = \left( U , V , W \right) \cdot \mathcal { C } ,
$$

where $U , V$ ，and $W$ are square and orthogonal, and $\mathcal { C }$ has the same size as $\mathcal { A }$ .Further, the different matrix slices of $\mathcal { C }$ are mutually orthogonal (with respect to the standard inner product on matrix spaces） and with decreasing Frobenius norm. Because of the imposed orthogonality conditions, the HOsVD of $\mathcal { A }$ is essentially unique. It is rank-revealing in the sense that if $\mathcal { A }$ has multirank $( r _ { 1 } , r _ { 2 } , r _ { 3 } )$ , then the last $n _ { 1 } - r _ { 1 } , n _ { 2 } - r _ { 2 }$ and $n _ { 3 } - r _ { 3 }$ slices along the different modes of the core tensor $\mathcal { C }$ are zero matrices. Algorithms for computing the HOsVD are described by Lathauwer,De Moor, and Vandewalle [296, 2ooo]. The matrix $U$ is obtained from the SVD of the $l \times m n$ matrix obtained from unfolding ${ \mathcal { A } } , V$ and $W$ are obtained similarly. Since $U , V$ ,and $W$ are orthogonal, $\mathcal { C } = \left( c _ { i j k } \right)$ is easily computed from $\mathcal { C } = ( U ^ { T } , V ^ { T } , W ^ { T } ) \cdot \mathcal { A }$

Suppose we want to approximate tensor $\mathcal { A }$ by another tensor $\boldsymbol { B }$ of lower multirank. Then we want to solve

$$
\operatorname* { m i n } _ { \operatorname { r a n k } ( \mathcal { B } ) = ( p , q , r ) } \| \mathcal { A } - \mathcal { B } \| _ { F } ,
$$

where the Frobenius tensor norm is defined as in (4.3.4O).This is the basis of the Tucker model [1O7O,1966]. Unlike the matrix case,this problem cannot be solved by truncating the HOSVD of $\mathcal { A }$ .It is no restriction to assume that $\boldsymbol { \mathcal { B } } \ : = \ : ( \boldsymbol { U } , \boldsymbol { V } , \boldsymbol { W } ) \cdot \boldsymbol { \mathcal { C } }$ ，where $U \in \mathbb { R } ^ { n \times p }$ ， $V \in \mathbb { R } ^ { n _ { 2 } \times q }$ ,and $W \in \mathbb { R } ^ { n _ { 3 } \times p }$ are orthogonal matrices. Because of the orthogonal invariance of the Frobenius norm, $U , V$ ,and $W$ are only determined up to a rotation. With the core tensor $\mathcal { C }$ eliminated, problem (4.3.48) can be rewritten as a maximization problem with objective function

$$
\Phi ( U , V , W ) = \frac { 1 } { 2 } \big \| ( U ^ { T } , V ^ { T } , W ^ { T } ) \cdot \boldsymbol { \mathcal { A } } \big \| _ { F } ^ { 2 }
$$

subject to $U ^ { T } U = I$ $V ^ { T } V = I$ ,and $W ^ { T } W = I$ (compare with the corresponding matrix problem for $d = 2$ ). This can be formulated and solved as an optimization problem on a Grassmann manifold; see Eldén and Savas [380, 2oog] and Savas and Lim [968,2010].

# Notes and references

An extensive survey of tensor methods is given by Kolda and Bader [7O5, 2oog]. The theory of tensors and hypermatrices is surveyed by Lim [747,2o13]. An introduction to the theory and computation of tensors is given by Wei and Ding [1114,2o16]. Tensor rank problems are studied by de Silva and Lim [993,20o8] and Comen et al. [264,20o9]. A tutorial on CP decomposition and its applications is given by Bro [180,1997]. The N-way Toolbox for MATLAB (Andersson and Bro [28,2oool) for analysis of multiway data can be downloaded from http://www.models.kvl.dk/source/. MATLAB tools for tensor computations have also been developed by Bader and Kolda [52,2oo6],[53,20o7]. A MATLAB Tensor toolbox supported by Sandia National Labs and MathSci.ai is available on the web.Hankel tensors arise from signal processing and data fiting; see Papy, De Lauthauwer, and Van Huffel [878, 2005]. Tensors with Cauchy structure are also of interest; see Chen,Li,and Qi [240, 2016].

# 4.4 - Total Least Squares

# 4.4.1- Errors-in-Variables Models

In the standard linear model it is assumed that the observed vector $b \in \mathbb { R } ^ { m }$ is related to the unknown parameter vector $x$ by the linear equation $A x = b + e$ ,where $A \in \mathbb { R } ^ { m \times n }$ is known and $e$ is a vector of random errors.If the components of $e$ are uncorrelated and have zero means and the same variance,then by the Gauss-Markov theorem (Theorem 1.1.4) the best linear unbiased estimate of $x$ is given by the solution of the least squares problem

$$
\operatorname* { m i n } _ { r } \| r \| _ { 2 } \quad { \mathrm { s u b j e c t ~ t o } } \quad A x = b + r .
$$

The assumption that all errors are confined to $b$ is frequently unrealistic. Sampling or modeling errors will often affect both $A$ and $b$ . In the errors-in-variables model it is assumed that

$$
( A + E ) x = b + f ,
$$

where the rows of the error matrix $\textbf { ( } E \textbf { ~ } f \textbf { ) }$ are independently and identically distributed with zero mean and the same variance. This model has independently been developed in statistics, where it is known as “latent root regression.” The optimal estimates of the parameters $x$ in this model satisfy the total least squares7 (TLS) problem

$$
\operatorname* { m i n } _ { E , f } \parallel ( E \quad f ) \parallel _ { F } \quad \mathrm { s u b j e c t t o } \quad ( A + E ) x = b + f ,
$$

where $\| \cdot \| _ { F }$ denotes the Frobenius matrix norm. The TLS problem is equivalent to finding the “nearest’consistent linear system, where the distance is measured in the Frobenius norm of $\left( \begin{array} { l l } { E } & { f } \end{array} \right)$ . When a minimizing perturbation has been found, any $x$ satisfying (4.4.2) is said to solve the TLS problem.

A complete and rigorous treatment of both theoretical and computational aspects of the TLS problem is developed in the monograph by Van Huffel and Vandewalle [1O77,1991]. They find that in typical applications, gains of $1 0 { - } 1 5 \%$ in accuracy can be obtained by using TLS instead of standard least squares methods.

The TLS solution depends on the relative scaling of the data $A$ and $b$ .Paige and Strakos [867, 2002] study the scaled TLS(STLS) problem

$$
\operatorname* { m i n } _ { E , f } \parallel ( E \quad \gamma f ) \parallel _ { F } \quad \mathrm { s u b j e c t t o } \quad ( A + E ) x = b + f ,
$$

where $\gamma$ is a given positive scaling parameter. For small values of $\gamma$ ，perturbations in $b$ will be favored. In the limit when $\gamma  0$ in (4.4.4), the solution equals the ordinary least squares

solution.On the other hand, large values of $\gamma$ favor perturbations in $A$ .In the limit when $1 / \gamma \to 0$ , we obtain the data least squares (DLS) problem

$$
\operatorname* { m i n } _ { E } \| E \| _ { F } \quad { \mathrm { s u b j e c t ~ t o } } \quad ( A + E ) x = b ,
$$

where perturbations are restricted to the data matrix $A$

# 4.4.2 - Total Least Squares and SVD

Writing the constraint $( A + E ) x = b + f$ as

$$
\begin{array} { r } { ( A + E \quad b + f ) \left( \begin{array} { c } { x } \\ { - 1 } \end{array} \right) = 0 } \end{array}
$$

shows that the matrix $\left( { \begin{array} { l l } { A + E } & { b + f } \end{array} } \right)$ is rank-deficient and that $\begin{array} { r l } { \left( x ^ { T } } & { { } - 1 \right) ^ { T } } \end{array}$ is a right singular vector corresponding to a zero singular value. The TLS problem can be analyzed in terms of the SVD

$$
C = ( \boldsymbol { A } \quad \boldsymbol { b } ) = U \Sigma V ^ { T } = \sum _ { i = 1 } ^ { n + 1 } \sigma _ { i } u _ { i } v _ { i } ^ { T } .
$$

Assume that $\sigma _ { n + 1 } > 0$ . Then,by the Eckart-Young-Mirsky theorem (Theorem 1.3.8) the unique perturbation $\scriptscriptstyle \left( E \_ f \right)$ of minimum Frobenius norm that makes $( A + E ) x = b + f$ consistent is the rank-one perturbation

$$
\begin{array} { r l } { ( E } & { { } f ) = - \sigma _ { n + 1 } u _ { n + 1 } v _ { n + 1 } ^ { T } , } \end{array}
$$

ind $\begin{array} { r } { \operatorname* { m i n } _ { E , f } \| ( E \textrm { ~ \textit { f } } ) \| _ { F } = \sigma _ { n + 1 } } \end{array}$ .Multiplying (4.4.8) from the right with $v _ { n + 1 }$ and using 4.4.7) gives

$$
\left( \begin{array} { l l } { E } & { f } \end{array} \right) v _ { n + 1 } = - \sigma _ { n + 1 } u _ { n + 1 } = - \left( \begin{array} { l l } { A } & { b } \end{array} \right) v _ { n + 1 } ,
$$

i.e., $\begin{array} { r l } { ( A + E } & { { } b + f ) v _ { n + 1 } = 0 } \end{array}$ If $v _ { n + 1 , n + 1 } \neq 0$ ,the problem is called generic, and the TLS solution is obtained by scaling $v _ { n + 1 }$ so that its last component is $- 1$ ：

$$
\binom { x } { - 1 } = - \frac { 1 } { \gamma } v _ { n + 1 } , \quad \gamma = e _ { n + 1 } ^ { T } v _ { n + 1 } .
$$

Otherwise, the TLS problem has no solution and is called nongeneric.

Let $\hat { \sigma } _ { i }$ ， $i = 1 , \ldots , n$ ,be the singular values of $A$ . By Theorem 1.3.5 these interlace the singular values of $( A b )$ ：

$$
\sigma _ { 1 } \geq \hat { \sigma } _ { 1 } \geq \cdot \cdot \cdot \geq \sigma _ { n } \geq \hat { \sigma } _ { n } \geq \sigma _ { n + 1 } .
$$

The condition $\hat { \sigma } _ { n } > \sigma _ { n + 1 }$ ensures that $A ^ { T } A - \sigma _ { n + 1 } ^ { 2 } I$ is symmetric positive definite and that the TLS problem has a unique solution.

If $A$ is rank-deficient, then so is $( A b )$ ，and $\hat { \sigma } _ { n } = \sigma _ { n + 1 } = 0$ Assume now that $\sigma _ { p } >$ $\sigma _ { p + 1 } = \cdot \cdot \cdot = \sigma _ { n + 1 }$ for some $p < n$ .Let $V _ { 2 } = ( v _ { p + 1 } , \ldots , v _ { n + 1 } )$ be the corresponding right singular vectors. Then the minimum is attained for any rank-one perturbation of the form

$$
\begin{array} { r } { \left( \begin{array} { l l } { E } & { f } \end{array} \right) = - \left( \begin{array} { l l } { \boldsymbol A + E } & { \boldsymbol b + f } \end{array} \right) \boldsymbol v \boldsymbol v ^ { T } , \quad \boldsymbol v = V _ { 2 } \boldsymbol z . } \end{array}
$$

Assume that a unit vector $z$ can be found such that

$$
V _ { 2 } z = { \binom { y } { \gamma } } , \quad \gamma \neq 0 .
$$

Then $x = - \gamma ^ { - 1 } y$ is a TLS solution. In this case the TLS solution is not unique. A unique TLS solution of least-norm can be found as follows. Since $V _ { 2 } z$ has unit length, minimizing $\| x \| _ { 2 }$ is equivalent to choosing the unit vector $z \in \mathbb { R } ^ { n - p + 1 }$ to maximize $\gamma$ in (4.4.11). Set $z = Q e _ { 1 }$ ， where $Q$ is a Householder reflector such that

$$
V _ { 2 } Q = \left( { \begin{array} { c c } { { y } } & { { { \hat { V } } _ { 2 } } } \\ { { \gamma } } & { { 0 } } \end{array} } \right) .
$$

Then the least-norm TLS solution is $x = - \gamma ^ { - 1 } y$ f $e _ { n + 1 } ^ { T } V _ { 2 } \ = \ 0$ ， then the TLS problem is nongeneric. This case can only occur when $\hat { \sigma } _ { n } = \sigma _ { n + 1 }$ .By an argument similar to that for $p = n$ ,it then holds that $b \perp u _ { j }$ ， $j = p : n$ . Nongeneric TLS problems can be treated by adding constraints on the solution; see Van Huffel and Vandewalle [1O77,1991].

From the relationship between the SVD of $\widetilde { A } = \left( A \quad b \right)$ and the eigendecomposition of the symmetric matrix $\widetilde { A } ^ { T } \widetilde { A }$ (see Section 1.2.2) it follows that the TLS solution $x$ can be characterized by

$$
\left( \begin{array} { c c } { { A ^ { T } A } } & { { A ^ { T } b } } \\ { { b ^ { T } A } } & { { b ^ { T } b } } \end{array} \right) v = \sigma _ { n + 1 } ^ { 2 } v , \quad v = \left( \begin{array} { c } { { x } } \\ { { - 1 } } \end{array} \right) ,
$$

where $\sigma _ { n + 1 } ^ { 2 }$ is the smallest eigenvalue of the matrix $\widetilde { A } ^ { T } \widetilde { A }$ ,and $v$ is a corresponding eigenvector. From (4.4.12) it follows that

$$
\begin{array} { r } { ( A ^ { T } A - \sigma _ { n + 1 } ^ { 2 } I _ { n } ) x = A ^ { T } b , \qquad b ^ { T } ( b - A x ) = \sigma _ { n + 1 } ^ { 2 } . } \end{array}
$$

In the first equation of (4.4.13) a positive multiple of the unit matrix is subtracted from the matrix of normal equations $A ^ { T } A x = A ^ { T } b$ ，This shows that TLS can be considered as a procedure for deregularizing the LS problem. (Compare with Tikhonov regularization, where a multiple of the unit matrix is added to improve the conditioning;see Section 3.5.3.） From a statistical point of view, TLS can be interpreted as removing bias by subtracting the error covariance matrix estimated by $\sigma _ { n + 1 } ^ { 2 } I$ from the data covariance matrix $A ^ { T } A$

Because of the nonlinear dependence of $x _ { \mathrm { { T L S } } }$ on the data $A , \ b$ ,a strict analysis of the sensitivity and conditioning of the TLS problem is more complicated than for the least squares problem. Golub and Van Loan [511,198o] show that an approximate condition number for the TLS problem is

$$
\kappa _ { T L S } ( A b ) = \kappa ( A ) \frac { \hat { \sigma } _ { n } } { \hat { \sigma } _ { n } - \sigma _ { n + 1 } } .
$$

This shows that the condition number for the TLS problem willbe much larger than $\kappa ( A )$ when the relative distance $1 - \sigma _ { n + 1 } / \hat { \sigma } _ { n }$ between $\sigma _ { n + 1 }$ and $\hat { \sigma } _ { n }$ is small. Subtracting the normal equations from (4.4.13), we obtain

$$
x _ { \mathrm { T L S } } - x _ { \mathrm { L S } } = \sigma _ { n + 1 } ^ { 2 } ( A ^ { T } A - \sigma _ { n + 1 } ^ { 2 } I ) ^ { - 1 } x _ { \mathrm { L S } } ,
$$

where $x _ { \mathrm { { T L S } } }$ and $x _ { \mathrm { L S } }$ denote the TLS and LS solutions. Taking norms in (4.4.15), we obtain the upper bound

$$
\| x _ { \mathrm { T L S } } - x _ { \mathrm { L S } } \| _ { 2 } \leq \frac { \sigma _ { n + 1 } ^ { 2 } } { \hat { \sigma } _ { n } ^ { 2 } - \sigma _ { n + 1 } ^ { 2 } } \| x _ { \mathrm { L S } } \| _ { 2 } \leq \frac { \sigma _ { n + 1 } } { 2 ( \hat { \sigma } _ { n } - \sigma _ { n + 1 } ) } \| x _ { \mathrm { L S } } \| _ { 2 } ,
$$

where the last inequality follows from

$$
\hat { \sigma } _ { n } ^ { 2 } - \sigma _ { n + 1 } ^ { 2 } = ( \hat { \sigma } _ { n } + \sigma _ { n + 1 } ) ( \hat { \sigma } _ { n } - \sigma _ { n + 1 } ) \geq 2 \sigma _ { n + 1 } ( \hat { \sigma } _ { n } - \sigma _ { n + 1 } ) .
$$

From this we deduce that when the errors in $A$ and $b$ are small the difference between the LS and TLS solutions is small. Otherwise,the solutions can differ considerably.

In many parameter estimation problems,some of the columns of $A$ are known exactly. It is no loss of generality to assume that the $n _ { 1 }$ error-free columns are the first in $A = \left( \begin{array} { l l } { A _ { 1 } } & { A _ { 2 } } \end{array} \right) \in$ $\mathbb { R } ^ { m \times n }$ ， $n = n _ { 1 } + n _ { 2 }$ . The mixed LS-TLS model is

$$
\left( A _ { 1 } \quad A _ { 2 } + E _ { 2 } \right) { \binom { x _ { 1 } } { x _ { 2 } } } = b + f , \qquad A _ { 1 } \in \mathbb { R } ^ { m \times n _ { 1 } } ,
$$

where the rows of the errors $\left( \begin{array} { l l } { E _ { 2 } } & { f } \end{array} \right)$ are independently and identically distributed with zero mean and the same variance.The problem can then be expressed as

$$
\operatorname* { m i n } _ { E _ { 2 } , f } \Vert \left( E _ { 2 } \quad f \right) \Vert _ { F } , \qquad \left( A _ { 1 } \quad A _ { 2 } + E _ { 2 } \right) \binom { x _ { 1 } } { x _ { 2 } } = b + f .
$$

When $A _ { 2 }$ is empty, this reduces to solving an ordinary least squares problem with multiple right-hand sides.When $A _ { 1 }$ is empty,this is the standard TLS problem.When the columns of $A _ { 1 }$ are linearly independent, the mixed LS-TLS can be solved as a two-block problem; see Section 4.3.1. First, compute the QR factorization

$$
Q ^ { T } \left( \begin{array} { l l l } { A _ { 1 } } & { A _ { 2 } } & { b } \end{array} \right) = \left( \begin{array} { c c c } { R _ { 1 1 } } & { R _ { 1 2 } } & { c _ { 1 } } \\ { 0 } & { R _ { 2 2 } } & { c _ { 2 } } \end{array} \right) ,
$$

where $R _ { 1 1 } \in \mathbb { R } ^ { n _ { 1 } \times n _ { 1 } }$ is upper triangular and $R _ { 2 2 } \ \in \ \mathbb { R } ^ { ( m - n _ { 1 } ) \times n _ { 2 } }$ . Next, compute $x _ { 2 }$ as the solution to the TLS problem

$$
\operatorname* { m i n } _ { E , G } \parallel ( E _ { \mathrm { ~ \it ~ \ / ~ g ~ } } ) \parallel _ { F } , \qquad ( R _ { 2 2 } + E ) x _ { 2 } = c _ { 2 } + g .
$$

Finally, $x _ { 1 }$ is obtained from the triangular system $R _ { 1 1 } x _ { 1 } = c _ { 1 } - R _ { 1 2 } x _ { 2 }$

# 4.4.3 - Multidimensional TLS

In this section we consider some generalizations of the TLS problem. The errors-in-variable model has been used in statistics for a long time.Multivariate problems were treated much later in the statistical literature.In the multidimensional TLS problem with multiple right-hand sides $B = ( b _ { 1 } , \ldots , b _ { d } ) \in \mathbb { R } ^ { m \times d }$ ， $d > 1$ ,the rows of $\left( \begin{array} { l l } { A } & { B } \end{array} \right)$ are assumed to be independently and identically distributed with zero mean and the same variance:

$$
\operatorname* { m i n } _ { E , F } \| \left( E \quad F \right) \| _ { F } , \qquad ( A + E ) X = B + F .
$$

Hence we consider perturbations $\left( \begin{array} { l l } { E } & { F } \end{array} \right)$ such that

$$
\begin{array} { r } { ( A + E \quad B + F ) \left( \begin{array} { c } { X } \\ { - I _ { d } } \end{array} \right) = 0 . } \end{array}
$$

Note that $A$ is similarly perturbed for all right-hand sides.Hence,the multidimensional TLS problem is different from separately solving $d$ one-dimensional TLS problems with right-hand sides $b _ { 1 } , \ldots , b _ { d }$ .This gives improved predictive power of the multidimensional TLS solution.

The solution to the multidimensional TLS problem can be expressed in terms of the SVD

$$
\boldsymbol { C } = \left( \boldsymbol { A } \quad \boldsymbol { B } \right) = \boldsymbol { U } \boldsymbol { \Sigma } \boldsymbol { V } ^ { T } = \boldsymbol { U } _ { 1 } \boldsymbol { \Sigma } _ { 1 } \boldsymbol { V } _ { 1 } ^ { T } + \boldsymbol { U } _ { 2 } \boldsymbol { \Sigma } _ { 2 } \boldsymbol { V } _ { 2 } ^ { T } ,
$$

where $\Sigma _ { 1 } = \operatorname { d i a g } \left( \sigma _ { 1 } , \ldots , \sigma _ { n } \right)$ ， $\Sigma _ { 2 } = \operatorname { d i a g } \left( \sigma _ { n + 1 } , \ldots , \sigma _ { n + d } \right)$ . By the Eckart-Young-Mirsky theorem, $\| \left( \begin{array} { l l } { E } & { F } \end{array} \right) \| _ { F } ^ { 2 }$ is minimized for the perturbation

$$
\begin{array} { r } { \left( \begin{array} { l l } { E } & { F } \end{array} \right) = - U _ { 2 } \Sigma _ { 2 } V _ { 2 } ^ { T } = - C V _ { 2 } V _ { 2 } ^ { T } , } \end{array}
$$

$\scriptstyle \sum _ { i = n + 1 } ^ { n + d } { \boldsymbol { \sigma } } _ { i } ^ { 2 }$ Ii $\sigma _ { n } ~ > ~ \sigma _ { n + 1 }$ $V _ { 2 }$

$$
V _ { 2 } = { \binom { V _ { 1 2 } } { V _ { 2 2 } } }
$$

and $V _ { 2 2 } \in \mathbb { R } ^ { d \times d }$ is nonsingular,then the TLS solution is

$$
\begin{array} { r } { X = - V _ { 1 2 } V _ { 2 2 } ^ { - 1 } = ( A ^ { T } A - \sigma _ { n + 1 } I ) ^ { - 1 } A ^ { T } B \in \mathbb { R } ^ { n \times d } . } \end{array}
$$

The last formula generalizes (4.4.13). For $d = 1$ , we recover the previous expression (4.4.10) for the TLS solution.

We now show that if $\hat { \sigma } _ { n } > \sigma _ { n + 1 }$ , then $V _ { 2 2 }$ is nonsingular. From (4.4.20) it follows that

$$
A V _ { 1 2 } + B V _ { 2 2 } = U _ { 2 } \Sigma _ { 2 } .
$$

If $V _ { 2 2 }$ is singular, then $V _ { 2 2 } z = 0$ for some unit vector $z$ ,and hence $U _ { 2 } \Sigma _ { 2 } z = A V _ { 1 2 } z$ From

$$
V _ { 2 } ^ { T } V _ { 2 } = V _ { 1 2 } ^ { T } V _ { 1 2 } + V _ { 2 2 } ^ { T } V _ { 2 2 } = I
$$

it follows that $V _ { 2 2 } ^ { T } V _ { 2 2 } z = z$ and $\| V _ { 2 2 } x \| _ { 2 } = 1$ . But then

$$
\sigma _ { n + 1 } \geq \| U _ { 2 } \Sigma _ { 2 } x \| _ { 2 } = \| A V _ { 1 2 } x \| _ { 2 } \geq \hat { \sigma } _ { n } .
$$

This is a contradiction,and hence $V _ { 2 2 }$ is nonsingular.

A unique solution to the multidimensional TLS problem exists if $\hat { \sigma } _ { n } > \sigma _ { n + 1 }$ .If this condition is not satisfied, then the TLS problem can stillhave a solution, but it is no longer unique. As for the case $d = 1$ ,we then seek a solution of minimum norm $\| X \| _ { F }$ .Wei [1112,1992] shows that a sufficient condition for a least-norm multidimensional TLS solution to exist is that

$$
\hat { \sigma } _ { p } > \sigma _ { p + 1 } = \cdot \cdot \cdot = \sigma _ { n } = \cdot \cdot \cdot = \sigma _ { n + d } .
$$

When this condition is satisfied,the following extension of the classical SVD algorithm computes the least-norm solution; see Van Huffel and Vandevalle [1077,1991, Section 3.6.1].For $d = 1$ and $p = n$ the algorithm coincides with the classical SVD algorithm described earlier.

# Algorithm 4.4.1.

Given a data matrix $A \in \mathbb { R } ^ { m \times n }$ and an observation matrix $B \in \mathbb { R } ^ { m \times d }$ , do the following:

1. Compute the SVD of the extended matrix $C = ( \boldsymbol { A } \quad \boldsymbol { B } ) \in \mathbb { R } ^ { m \times ( n + d ) } .$

$$
C = U \Sigma V ^ { T } = \sum _ { i = 1 } ^ { n + d } u _ { i } \sigma _ { i } v _ { i } ^ { T } .
$$

2. Suppose $p \leq \operatorname* { m i n } \{ n , \operatorname { r a n k } ( C ) ) \}$ , and partition $V$ so that

$$
V = \stackrel { n } { d } \left( \stackrel { p } { V _ { 2 1 } } \stackrel { q } { V _ { 2 2 } } \right) \in \mathbb { R } ^ { ( n + d ) \times ( n + d ) } ,
$$

where $V _ { 1 1 } \in \mathbb { R } ^ { n \times p }$ and $V _ { 2 2 } \in \mathbb { R } ^ { d \times q }$ ， $q = n - p + d $

3.If $V _ { 2 2 } = 0$ ，then the problem is nongeneric. Otherwise,if $V _ { 2 2 }$ has full row rank, compute the least-norm TLS solution as

$$
X = - V _ { 1 2 } V _ { 2 2 } ^ { \dag } = ( V _ { 1 1 } ^ { T } ) ^ { \dag } V _ { 2 1 } ^ { T } .
$$

From the CS decomposition it follows that if $V _ { 2 2 }$ has full column rank,then so has $V _ { 1 1 }$ For a proof of the equivalence of the formulas in (4.4.25),see Van Huffel and Vandevalle[1077, 1991,Theorem 3.10]. The second expression for $X$ only requires computation of the $k$ largest right singular vectors of $( A b )$ and is advantageous when $k$ is small.

Algorithm 4.4.1 for solving the multidimensional TLS problem only requires a small part of the full SVD, namely the $d \ll n$ right singular vectors corresponding to the smallest singular values. For this purpose Van Huffel, Vandewalle,and Haegemans [1O78,1987] developed a modified partial QRSVD (PSVD) algorithm. In the Householder bidiagonalization phase the singular vectors $U$ and $V$ are initialized by the accumulated products of the Householder reflections.During the QRSVD iterations, plane rotations are applied to $U$ and $V$ to generate the left and right singular values. A great amount of work is saved in the PSVD algorithm by delaying the initializing of $U$ and $V$ until the end of the diagonalizing phase.The Householder reflections are then applied only to the (small number of) desired singular vectors of the bidiagonal matrix. A second modification in PSVD is to perform only a partial diagonalization of the bidiagonal matrix.The iterative process is stopped as soon as convergence has occurred to all desired singular values. Assume that at the $i$ th step of the diagonalization phase,we have the block bidiagonal form

$$
B ^ { ( i ) } = \left( \begin{array} { c c c c c } { { B _ { 1 } ^ { ( i ) } } } & { { } } & { { } } & { { } } & { { } } \\ { { } } & { { B _ { 2 } ^ { ( i ) } } } & { { } } & { { } } & { { } } \\ { { } } & { { } } & { { \ddots } } & { { } } & { { } } \\ { { } } & { { } } & { { } } & { { B _ { s } ^ { ( i ) } } } \end{array} \right) ,
$$

where $B _ { j } ^ { ( i ) }$ $j = 1 , \dots , s$ areunreducedupperbidiagonalmatrices.Supposethatabasisfora singular subspace corresponding to the singular values $\sigma _ { i } \leq \theta$ is desired. Then spectrum slicing (see Section 7.2.1) can be used to partition these blocks into three classes:

$$
\begin{array} { r l } & { C _ { 1 } = \{ B _ { j } \mid \mathrm { a l l ~ s i n g u l a r ~ v a l u e s } > \theta \} , } \\ & { C _ { 2 } = \{ B _ { j } \mid \mathrm { a l l ~ s i n g u l a r ~ v a l u e s } \leq \theta \} , } \\ & { C _ { 3 } = \{ B _ { j } \mid \mathrm { a t ~ l e a s t ~ o n e ~ s i n g u l a r ~ v a l u e } > \theta \mathrm { a n d ~ a t ~ l e a s t ~ o n e } \leq \theta \} . } \end{array}
$$

If $C _ { 3 }$ is empty, then the algorithm stops. Otherwise, one QR iteration is applied to each block in $C _ { 3 }$ ,and the partition is reclassified. If no bound on the singular values can be given but, instead, the dimension $p$ of the desired subspace is known, then a bound $\theta$ can be computed with the bisection method from Section 7.2.1. A complete description of the PSVD algorithm is given in Van Huffel and Vandevalle [1077,1991, Section 4.3]. A Fortran 77 implementation of PSVD is available from Netlib.

# 4.4.4 - Solving Large-Scale TLS Problems

For large or structured TLS problems,computing the PSVD may be prohibitive because the sparsity or structure of the matrix is lost in the reduction to bidiagonal form. Then an iterative algorithm may be advantageous. Similarly, this applies when a sequence of slowly varying TLS problems has to be solved. In this case the solution of the previous problem can be used as an initial approximation.

Let $\sigma _ { n + 1 } ^ { 2 }$ be the smallest eigenvalue of $\widetilde { A } ^ { T } \widetilde { A }$ where $\widetilde { \cal A } = ( \cal { A } b )$ If $\begin{array} { r l } { \left( x ^ { T } } & { { } - 1 \right) ^ { T } } \end{array}$ is a corresponding eigenvector, then

$$
\widetilde { A } ^ { T } \widetilde { A } \left( \begin{array} { c } { { x } } \\ { { - 1 } } \end{array} \right) = \sigma _ { n + 1 } ^ { 2 } \left( \begin{array} { c } { { x } } \\ { { - 1 } } \end{array} \right) .
$$

This characterization of the TLS solution suggests the following alternative formulation of the TLS problem. The unique minimum $\sigma _ { n + 1 } ^ { 2 }$ of the Rayleigh quotient $\rho ( x ) = v ^ { T } \widetilde { A } v / \| v \| _ { 2 } ^ { 2 }$ , where

$$
{ \widetilde { A } } = \left( A \quad b \right) , \qquad v = \left( { x \atop - 1 } \right) ,
$$

is attained for $x = x _ { T L S }$ . Hence the TLS problem is equivalent to $\operatorname* { m i n } _ { x } \rho ( x )$ , where

$$
\rho ( x ) = \frac { \| r \| _ { 2 } ^ { 2 } } { \| x \| _ { 2 } ^ { 2 } + 1 } , \quad r = - \widetilde { A } \left( \begin{array} { c } { { x } } \\ { { - 1 } } \end{array} \right) = b - A x .
$$

In the algorithm of Bjorck, Heggernes,and Matstoms [147,2ooo] the TLS solution $x$ is computed by applying inverse iteration to the symmetric eigenvalue problem (4.4.26). Let $x ^ { ( k ) }$ be the current approximation. Then $x ^ { ( k + 1 ) }$ and the scalars $\beta _ { k } , k = 0 , 1 , 2 , \ldots$ ,are computed by solving

$$
\widetilde { A } ^ { T } \widetilde { A } \left( { \begin{array} { c } { x ^ { ( k + 1 ) } } \\ { - 1 } \end{array} } \right) = \beta _ { k } \left( { \begin{array} { c } { x ^ { ( k ) } } \\ { - 1 } \end{array} } \right) .
$$

If the compact QR factorization

$$
\begin{array} { r } { \widetilde { A } = \left( A \begin{array} { l l } { b } & { b } \end{array} \right) = Q \left( \begin{array} { l l } { R } & { c } \\ { 0 } & { \eta } \end{array} \right) , \quad Q \in \mathbb { R } ^ { m \times ( n + 1 ) } , } \end{array}
$$

is known,then the solution of (4.4.28)is obtained by solving the two triangular systems

$$
\begin{array} { r l } { \left( \begin{array} { c c } { R ^ { T } } & { 0 } \\ { c ^ { T } } & { \eta } \end{array} \right) \left( \begin{array} { c } { z ^ { ( k ) } } \\ { - \gamma _ { k } } \end{array} \right) = \left( \begin{array} { c } { x ^ { ( k ) } } \\ { - 1 } \end{array} \right) , } & { { } \qquad \left( \begin{array} { c c } { R } & { c } \\ { 0 } & { \eta } \end{array} \right) \left( \begin{array} { c } { x ^ { ( k + 1 ) } } \\ { - 1 } \end{array} \right) = \beta _ { k } \left( \begin{array} { c } { z ^ { ( k ) } } \\ { - \gamma _ { k } } \end{array} \right) . } \end{array}
$$

After eliminating $\gamma _ { k }$ , this becomes

$$
x ^ { ( k + 1 ) } = x _ { L S } + \beta _ { k } R ^ { - 1 } ( R ^ { - T } x ^ { ( k ) } ) , \quad \beta _ { k } = \eta ^ { 2 } / ( 1 + x _ { L S } ^ { T } x ^ { ( k ) } ) .
$$

The iterations are initialized by taking

$$
x ^ { ( 0 ) } = x _ { L S } = R ^ { - 1 } c , \quad \beta _ { 0 } = \eta ^ { 2 } / ( 1 + \| x _ { L S } \| ^ { 2 } ) .
$$

From classical convergence results for symmetric inverse iteration it follows that

$$
| | x ^ { ( k ) } - x _ { T L S } | | _ { 2 } = O ( ( \sigma _ { n + 1 } / \sigma _ { n } ) ^ { 2 k } ) , \qquad | \rho ( x ^ { ( k ) } ) - \sigma _ { n + 1 } ^ { 2 } | = O ( ( \sigma _ { n + 1 } / \sigma _ { n } ) ^ { 4 k } ) .
$$

By using Rayleigh-quotient iteration (RQI), a better rate of convergence can be obtained. For properties of the Rayleigh quotient of symmetric matrices, see Section 7.3.1.

Fasino and Fazzi [398,2o18] note that by the characterization (4.4.27) the TLS problem is equivalent to the nonlinear least squares problem $\operatorname* { m i n } _ { x } \| f ( x ) \| _ { 2 }$ ，where

$$
f ( x ) = \mu ( x ) ( b - A x ) , \quad \mu ( x ) = ( 1 + x ^ { T } x ) ^ { - 1 / 2 } ,
$$

and solved by a Gauss-Newton method (see Section 8.1.2). If $x _ { k }$ is the current approximation, this requires solution of a sequence of linear least squares problems

$$
\operatorname* { m i n } _ { h _ { k } } \| f ( x _ { k } ) + h _ { k } J ( x _ { k } ) \| _ { 2 } , \quad x _ { k + 1 } = x _ { k } + h _ { k } ,
$$

where $J ( x _ { k } ) = \mu ( x _ { k } ) \big \lrcorner ( A + \mu ( x _ { k } ) ^ { 2 } r _ { k } x _ { k } ^ { T } \big )$ ，with $r _ { k } = b - A x _ { k }$ is the Jacobian of $f ( x )$ at $x _ { k }$ Since $A + \mu ( x _ { k } ) ^ { 2 } r _ { k } x _ { k } ^ { T }$ is a rank-one modification of $A$ , its QR factorization can be cheaply computed by modifying the QR factorization of $A$ ； see Section 3.3.2. In fact, this method is closely related to inverse iteration and has a rate of convergence similar to that shown by Peters and Wilkinson [891,1979].

# 4.4.5 - Regularized TLS

When $A$ is nearly rank-deficient,regularization is required to stabilize the TLS solution. Similar to TSVD, truncated TLS (TTLS) reduces an il-conditioned problem to an exactly rank-deficient problem by treating small singular values of $( A , b )$ as zeros. Fierro and Bunch [405,1994] show that under certain conditions,TTLS is superior to TSVD in suppressing noise in $A$ and $b$ ；see also [406,1996].

Let $k \leq \mathrm { r a n k } ( A )$ be the number of singular values to be retained. Then the TTLS solution

$$
x _ { k } = - V _ { 1 2 } V _ { 2 2 } ^ { \dagger } = ( V _ { 1 1 } ^ { T } ) ^ { \dagger } V _ { 2 1 } ^ { T }
$$

can be computed by Algorithm 4.4.1. The second expression for is better to use when $k$ is smal The rorm of $x _ { k }$ is $\| x _ { k } \| _ { 2 } = \left( \| V _ { 2 2 } \| _ { 2 } ^ { - 2 } - 1 \right) ^ { 1 / 2 }$ Irincreaes ith $k$ wile henomofthe residual matrix

$$
\Vert \left( \begin{array} { l l } { A } & { b } \end{array} \right) - \left( \begin{array} { l l } { \tilde { A } } & { \tilde { b } } \end{array} \right) \Vert _ { F } = \left( \sigma _ { k + 1 } ^ { 2 } + \cdot \cdot \cdot + \sigma _ { n + 1 } ^ { 2 } \right) ^ { 1 / 2 }
$$

decreases with $k$ . The TTLS solution $x _ { k }$ can be written as a filtered sum

$$
x _ { k } = \sum _ { i = 1 } ^ { n } f _ { i } \frac { \hat { u } _ { i } ^ { T } b } { \hat { \sigma } _ { i } } \hat { v } _ { i } ,
$$

where $A = \hat { U } \hat { \Sigma } \hat { V } ^ { T }$ is the SVD of $A$ . Fierro et al. [404,1997] show that when $\hat { u } _ { i } ^ { T } b \neq 0$ and $i \leq k$ ,the filter factors $f _ { i }$ are close to one,and for $i > k$ they are small.

Another approach to regularization is to restrict the TLS solution by a quadratic constraint. The RTLS problem is

$$
\operatorname* { m i n } _ { E , f } \| \left( E \quad f \right) \| _ { F } \quad \mathrm { s u b j e c t ~ t o } \quad ( A + E ) x = b + f , \quad \| L x \| _ { 2 } \leq \delta ,
$$

where $\delta > 0$ is a regularization parameter, and the matrix $L \in \mathbb { R } ^ { p \times n }$ defines a seminorm on the solution space.In practice, the parameter $\delta$ is usually not exactly specified but has to be estimated from the given data using the techniques discussed for the TLS problem in Section 3.6.4.

The optimal solution of the RTLS problem is different from $x _ { \mathrm { T L S } }$ only when the quadratic constraint is active,i.e.,

$$
\| L x _ { \mathrm { T L S } } \| _ { 2 } > \delta .
$$

In this case the constraint in (4.4.35) holds with equality at the optimal solution,and the RTLS solution can be characterized by the following first-order optimality conditions for (4.4.35); see Golub,Hansen,and O'Leary [492,1999].

Theorem 4.4.1. The solution to the regularized TLS problem (4.4.35) with the inequality constraint replaced by equality is a solution to the eigenvalue problem

$$
( A ^ { T } A - \lambda _ { I } I + \lambda _ { L } L ^ { T } L ) x = A ^ { T } b ,
$$

where

$$
\lambda _ { I } = \phi ( x ) = \frac { \| b - A x \| _ { 2 } ^ { 2 } } { 1 + \| x \| ^ { 2 } } , \qquad \lambda _ { L } = \frac { 1 } { \delta ^ { 2 } } \big ( b ^ { T } ( b - A x ) - \phi ( x ) \big ) .
$$

Sima, Van Hufel,and Golub [994,2o04l give methods for solving the RTLS problem using an iterative method that in each step solves a quadratic eigenvalue problem. In practice, very few steps are required. Their method can be applied to large problems using existing fast methods based on projection onto Krylov subspaces for solving quadratic eigenvalue problems.

The first-order conditions for RTLS given in Theorem 4.4.1 are the same as for the constrained minimization problem

$$
\operatorname* { m i n } _ { x } { \frac { \| b - A x \| _ { 2 } ^ { 2 } } { 1 + \| x \| _ { 2 } ^ { 2 } } } \quad { \mathrm { s u b j e c t ~ t o } } \quad \| L x \| _ { 2 } \leq \delta .
$$

This Rayleigh quotient formulation of the RTLS problem is closely related to Tikhonov regularization of TLS,

$$
\operatorname* { m i n } _ { E , r } \| \left( E \quad f \right) \| _ { F } + \rho \| L x \| _ { 2 } ^ { 2 } \quad \mathrm { s u b j e c t } \ \mathrm { t o } \quad ( A + E ) x = b + f ,
$$

and equivalent to the nonconvex minimization problem

$$
\operatorname* { m i n } _ { x } \left\{ \frac { \| b - A x \| _ { 2 } ^ { 2 } } { 1 + \| x \| _ { 2 } ^ { 2 } } + \rho \| L x \| _ { 2 } ^ { 2 } \right\} .
$$

Beck and Ben-Tal [96,2oo6] show that this problem can be reduced to a sequence of trust-region problems and give detailed algorithms. Algorithms for large-scale Tikhonov regularization of TLS are developed by Lampe and Voss [712, 2013].

Guo and Renaut [554, 2oo2] show that the eigenvalue problem in Theorem 4.4.1 can be formulated as

$$
( M + \lambda _ { L } N ) \left( \begin{array} { c } { { x } } \\ { { - 1 } } \end{array} \right) = \lambda _ { I } \left( \begin{array} { c } { { x } } \\ { { - 1 } } \end{array} \right) ,
$$

where $\lambda _ { L }$ is given as in (4.4.37), and

$$
M = \left( \begin{array} { c c } { { A ^ { T } A } } & { { A ^ { T } b } } \\ { { b ^ { T } A } } & { { b ^ { T } b } } \end{array} \right) , \qquad N = \left( \begin{array} { c c } { { L ^ { T } L } } & { { 0 } } \\ { { 0 } } & { { - \delta ^ { 2 } } } \end{array} \right) .
$$

Based on this formulation, they suggest an algorithm using shifted inverse iteration to solve the eigenvalue problem (4.4.41). As an initial solution, the corresponding regularized LS solution $x ^ { ( 0 ) } = x _ { R L S }$ is used.Anadditional complication is that the matrix $B$ depends on the RTLS solution. Their algorithm is further analyzed and refined in Renaut and Guo [924, 2oo5]. Lampe and Voss [711, 2oo8] develop a related but faster method that uses a nonlinear Arnoldi process (see Section 6.4.5) and a modified root-finding method.

# Notes and references

M. Wei [1111,1992] gives algebraic relations between the total least squares and least squares problems with more than one solution. Several papers study the sensitivity and conditioning of the TLS problem and give bounds for the condition number; see Zhou et al.[1149, 2009], Baboulin and Gratton [51,2o11], Jia and Li [670,2o13],and Xie, Xiang,and Y. Wei [1134,2O17]. A perturbation analysis of TTLS is given by Gratton，Titley-Peloquin,and Ilunga [529, 2013].

De Moor [297, 1993l studies more general structured and weighted TLS problems and considers applications in systems and control theory. These problems can be solved via a nonlinear GSVD.A review of developments and extensions of the TLS method to weighted and struc-tured approximation is given by Markovsky and Van Huffel [777,2oo7]. A recent bibliography on total least squares is given by Markovsky [776, 2O1o]. Standard TLS methods may not be appropriate when $A$ has a special structure such as Toeplitz or Vandermonde. The structured least-norm problem (STLN) preserves structure and can minimize errors also in the $\ell _ { 1 }$ -norm and others; see Rosen,Park,and Glick [936,1996] and Van Huffel,Park,and Rosen [1076,1996].

# 4.5 - Least Squares Problems with Special Bases

# 4.5.1 $-$ Approximation by Orthogonal Polynomials

It is frequently desired to model a given function $y = f ( x )$ by a linear combination of basis functions:

$$
\bar { f } = \sum _ { k = 0 } ^ { n } c _ { k } \phi _ { k } ( x ) .
$$

It is often convenient to choose the $n + 1$ basis functions as a triangle family of polynomials, where

$$
\phi _ { k } ( x ) = \sum _ { j = 0 } ^ { k } a _ { k j } x ^ { j }
$$

is a polynomial of degree $k$ with nonzero leading coeficient $a _ { k k }$ . The coefficients of such a family form a nonsingular lower triangular matrix $A = \left( a _ { i , j } \right)$ ， $0 \leq j \leq i \leq n$ .Then the monomials $x ^ { k }$ ， $k = 0 , \ldots , n$ ,can be expressed recursively and uniquely as linear combinations $x ^ { k } = b _ { k , 0 } p _ { 0 } + b _ { k , 1 } p _ { 1 } + \cdot \cdot \cdot + b _ { k , k } p _ { k }$ , where the associated matrix is $B = ( b _ { i , j } ) = A ^ { - 1 }$

Definition 4.5.1. Let thereal-valued functions $f$ and $g$ be defined on a finite grid $G = \{ x _ { i } \} _ { i = 0 } ^ { m }$ of distinct points. Then, the inner product of $( f , g )$ is defined by

$$
( f , g ) = \sum _ { i = 0 } ^ { m } f ( x _ { i } ) g ( x _ { i } ) w _ { i } ,
$$

where $\{ w _ { i } \} _ { i = 0 } ^ { m }$ are given positive weights. The norm of $f$ is $\| f \| = ( f , f ) ^ { 1 / 2 }$

An important consideration is the choice of a proper basis for the space of approximating functions. The functions $\phi _ { 0 } , \phi _ { 1 } , \ldots , \phi _ { n }$ are said to form an orthogonal system if $( \phi _ { i } , \phi _ { j } ) = 0$ for $i \neq j$ and $\| \phi _ { i } \| \neq 0$ for all $i$ ，If,in addition, $\lVert \phi _ { i } \rVert = 1$ for all $i$ ，then the sequence is called an orthonormal system.We remark that the notation used is such that the results can be generalized with minor changes to cover the least squares approximation when $f$ is approximated by an infinite sequence of orthogonal functions $\phi _ { 0 } , \phi _ { 1 } , \phi _ { 2 } , . . . .$

We study the least squares approximation problem to determine coeficients $c _ { 0 } , c _ { 1 } , \ldots , c _ { n }$ in (4.5.1) such that the weighted Euclidean norm

$$
\| \overline { { f } } - f \| ^ { 2 } = \sum _ { i = 0 } ^ { m } w _ { i } | \overline { { f } } ( x _ { i } ) - f ( x _ { i } ) | ^ { 2 }
$$

of the error is minimized. Note that interpolation is a special case ( ${ \bf \Phi } _ { n } = m $ ）of this problem. By a family of orthogonal polynomials we mean here a triangle family of polynomials, which is an orthogonal system with respect to the inner product (4.5.2) for some given weights.

Theorem 4.5.2. Let $\phi _ { 0 } , \phi _ { 1 } , \ldots , \phi _ { n }$ be linearly independent functions. Then the least squares approximation problem has the unique solution

$$
f ^ { * } = \sum _ { j = 0 } ^ { n } c _ { j } \phi _ { j } ,
$$

which is characterized by the orthogonality property $( f ^ { * } - f , \phi _ { j } ) = 0$ ， $j = 0 , 1 , \ldots , n$ .The coefficients $c _ { j }$ ,called orthogonal coefcients or Fourier coefcients, satisfy the normal equations

$$
\sum _ { j = 0 } ^ { n } ( \phi _ { j } , \phi _ { k } ) c _ { j } = ( f , \phi _ { k } ) , \quad k = 0 , \ldots , n .
$$

Ifthe functions form an orthogonal system, the coeffcients are given by

$$
c _ { j } = ( f , \phi _ { j } ) / ( \phi _ { j } , \phi _ { j } ) , \quad j = 0 , \ldots , n .
$$

Expansions of functions in terms of orthogonal polynomials are easy to manipulate, have good convergence properties,and give a well-conditioned representation (with the exception of weight distributions on certain grids). We now prove some results from the general theory of orthogonal polynomials.

Theorem 4.5.3. Let $\{ x _ { i } \} _ { i = 0 } ^ { m } \in ( a , b )$ be distinct points, and let $\{ w _ { i } \} _ { i = 0 } ^ { m }$ be a set of weights. Then there is an associated triangle family of orthogonal polynomials $\phi _ { 0 } , \phi _ { 1 } , \ldots , \phi _ { m }$ . The family is uniquely determined apart from the fact that the leading coefficients $a _ { 0 } , a _ { 1 } , a _ { 2 } , \dotsc$ can be given arbitrary nonzero values. The orthogonal polynomials satisfy $a$ three-term recursion formula, $\phi _ { - 1 } ( x ) = 0$ ， $\phi _ { 0 } ( x ) = a _ { 0 }$ ，

$$
\phi _ { n + 1 } ( x ) = \alpha _ { n } ( x - \beta _ { n } ) \phi _ { n } ( x ) - \gamma _ { n } \phi _ { n - 1 } ( x ) , \quad n \ge 0 ,
$$

where $\alpha _ { n } = { a _ { n + 1 } } / { a _ { n } }$ and

$$
\beta _ { n } = \frac { ( x \phi _ { n } , \phi _ { n } ) } { \| \phi _ { n } \| ^ { 2 } } , \qquad \gamma _ { n } = \frac { \alpha _ { n } \| \phi _ { n } \| ^ { 2 } } { \alpha _ { n - 1 } \| \phi _ { n - 1 } \| ^ { 2 } } \quad ( n > 0 ) .
$$

If the weight distribution is symmetric about $x = \beta$ ,then $\beta _ { n } = \beta$ for all $n$

Proof. Suppose that the $\phi _ { j }$ have been constructed for $0 \leq j \leq n , \phi _ { j } \neq 0 ( n \geq 0 )$ . We now seek a polynomial of degree $n + 1$ with leading coefficient $a _ { n + 1 }$ that is orthogonal to $\phi _ { 0 } , \phi _ { 1 } , \ldots , \phi _ { n }$ For a triangle family of polynomials $\{ \phi _ { j } \} _ { j = 0 } ^ { n }$ , we can write

$$
\phi _ { n + 1 } = \alpha _ { n } x \phi _ { n } - \sum _ { i = 0 } ^ { n } c _ { n , i } \phi _ { i } .
$$

Hence $\phi _ { n + 1 }$ is orthogonal to $\phi _ { j }$ $0 \leq j \leq n$ , if and only if

$$
\alpha _ { n } ( x \phi _ { n } , \phi _ { j } ) - \sum _ { i = 0 } ^ { n } c _ { n , i } ( \phi _ { i } , \phi _ { j } ) = 0 , \quad j = 0 , 1 , \ldots , n .
$$

Since $( \phi _ { i } , \phi _ { j } ) = 0$ ， $i \neq j$ , it follows that

$$
c _ { n , j } \| \phi _ { j } \| ^ { 2 } = \alpha _ { n } ( x \phi _ { n } , \phi _ { j } ) , \quad 0 \leq j \leq n ,
$$

which determines the coefficients $c _ { n , j }$ ．From the definition of inner product it follows that $( x \phi _ { n } , \phi _ { j } ) = ( \phi _ { n } , x \phi _ { j } )$ . But $x \phi _ { j }$ is a polynomial of degree $j + 1$ and is therefore orthogonal to $\phi _ { n }$ if $j + 1 < n$ So $c _ { n j } = 0$ ， $j < n - 1$ ,and thus

$$
\phi _ { n + 1 } = \alpha _ { n } x \phi _ { n } - c _ { n , n } \phi _ { n } - c _ { n , n - 1 } \phi _ { n - 1 } .
$$

This has the same form as (4.5.5) if we set $\beta _ { n } = c _ { n , n } / \alpha _ { n }$ ， $\gamma _ { n } = c _ { n , n - 1 }$ . To get the expression in (4.5.6) for $\gamma _ { n }$ , we take the inner product of equation (4.5.7） with $\phi _ { n + 1 }$ . From orthogonal-ity it follows that $\left( \phi _ { n + 1 } , \phi _ { n + 1 } \right) = \alpha _ { n } ( \phi _ { n + 1 } , x \phi _ { n } )$ . Decreasing all indices by one, we obtain $( \phi _ { n } , x \phi _ { n - 1 } ) = \| \phi _ { n } \| ^ { 2 } / \alpha _ { n - 1 }$ ， $n \geq 1$ .Substituting this in the expression for $\gamma _ { n }$ gives the desired result. □

The proof of the above theorem shows a way to construct $\beta _ { n }$ ， $\gamma _ { n }$ ,and the values of the polynomials $\phi _ { n }$ at the grid points for $n = 1 , 2 , 3 , \ldots .$ This is called the Stieltjes procedure. For $n = m$ , the constructed polynomial must be equal to $a _ { m + 1 } ( x - x _ { 0 } ) ( x - x _ { 1 } ) \cdots ( x - x _ { m } )$ ， because this polynomial is zero at all the grid points and thus orthogonal to all functions on the grid. Since $\| \phi _ { m + 1 } \| = 0$ ,the construction stops at $n = m$ . This is natural because there cannot be more than $m + 1$ orthogonal (or even linearly independent) functions on a grid with $m + 1$ points.

Given the coefcients in an orthogonal expansion, the values of $f$ can be efficiently computed using the following algorithm. (The proof is left as a somewhat difficult exercise.)

$\begin{array} { r } { p _ { k } \ = \ \sum _ { j = 0 } ^ { k } c _ { j } \phi _ { j } } \end{array}$ $\phi _ { j } ( x )$ gonal $p ( x ) \stackrel { \textstyle - } { = } A _ { 0 } y _ { 0 }$ $y _ { n + 2 } = y _ { n + 1 } = 0$

$$
y _ { k } = \alpha _ { k } ( x - \beta _ { k } ) y _ { k + 1 } - \gamma _ { k + 1 } y _ { k + 2 } + c _ { k } , \quad k = n , n - 1 , \ldots , 0 .
$$

From Theorem 4.5.2 follows the important result that the coefcients in the best approximating polynomial $p _ { k }$ of degree $k$ are independent of $k$ and given by $c _ { j } = ( f , \phi _ { j } ) / ( \phi _ { j } , \phi _ { j } )$ . Hence approximations of increasing degree can be recursively generated as follows.Assume that $\phi _ { i }$ ， $i = 1 , \ldots , k$ ,and $p _ { k }$ have been computed. In the next step the coefficients $\beta _ { k } , \gamma _ { k }$ are computed from (4.5.6) and $\phi _ { k + 1 }$ by (4.5.5). The next approximation of $f$ is then given by

$$
p _ { k + 1 } = p _ { k } + c _ { k + 1 } \phi _ { k + 1 } , \quad c _ { k + 1 } = ( f , \phi _ { k + 1 } ) / \| \phi _ { k + 1 } \| ^ { 2 } .
$$

The coefficients $\{ \beta _ { k } , \gamma _ { k } \}$ in the recursion formula (4.5.5) and the orthogonal functions $\phi _ { j }$ at the grid points are computed using the Stieltjes procedure together with the orthogonal coefficients $\{ c _ { j } \}$ for $j = 1 , 2 , \dots , n$ . The total work required is about 4mn flops, assuming unit weights and that the grid is symmetric. If there are differing weights,then about mn additional operations are needed; similarly,mn additional operations are required if the grid is not symmetric.If the orthogonal coefficients are determined simultaneously for several functions on the same grid,then only about mn additional operations per function are required. (In the above, we assume that $m \gg 1$ ， $n \gg 1 .$ ）Hence,the procedure is much more economical than the general methods based on normal equations or QR factorization,which all require $O ( m n ^ { 2 } )$ flops.

In practice the computed $\phi _ { k + 1 }$ will gradually lose orthogonality to the previously computed $\phi _ { j }$ . Since $\phi _ { k + 1 } ^ { T } p _ { k } = 0$ ,an alternative expression for the new coefficient is

$$
c _ { k + 1 } = { \left( r _ { k } , \phi _ { k + 1 } \right) } / { \| \phi _ { k + 1 } \| ^ { 2 } } , \quad r _ { k } = f - p _ { k } .
$$

This expression, which involves the residual $r _ { k }$ , will give better accuracy in the computed coefficients. Indeed, when using the classical formula,one sometimes finds that the residual norm increases when the degree of the approximation is increased! Note that the difference between the two variants discussed here is similar to the difference between CGS and MGS.

The Stieltjes procedure may be sensitive to propagation of roundoff errors. An alternative procedure for computing the recurrence coeficients in (4.5.5) and the values of the orthogonal polynomials has been given by Gragg and Harrod [523,1984l; see also Boley and Golub [169, $\mathrm { 1 9 8 7 } ]$ . In this procedure these quantities are computed from an inverse eigenvalue problem for a certain symmetric tridiagonal matrix. Reichel [916,1991] compares this scheme with the Stieltjes procedure and shows that the Gragg-Harrod procedure generally yields better accuracy.

Expansions in orthogonal polynomials also have the very important advantage of avoiding the difficulties with ill-conditioned systems of equations that occur even for moderate $n$ when the coefficientsinapolyomial $\textstyle \sum _ { j = 0 } ^ { n } c _ { j } x ^ { j }$ andthectiot For equidistant data, te Gram polynomials $\{ P _ { n , m } \} _ { n = 0 } ^ { m }$ , which are orthogonal withrespectto the inner product

$$
( f , g ) = \sum _ { i = 0 } ^ { m } f ( x _ { i } ) g ( x _ { i } ) , \quad x _ { i } = - 1 + 2 i / m ,
$$

are relevant. These satisfy the recursion formula $P _ { - 1 , m } ( x ) = 0$ ， $P _ { 0 , m } = ( m + 1 ) ^ { - 1 / 2 }$ ，

$$
P _ { n + 1 , m } ( x ) = \alpha _ { n , m } x P _ { n , m } ( x ) - \gamma _ { n , m } P _ { n - 1 , m } ( x ) , \quad n \ge 0 ,
$$

where the coefficients are given by $( n < m )$

$$
\alpha _ { n , m } = \frac { m } { n + 1 } \left( \frac { 4 ( n + 1 ) ^ { 2 } - 1 } { ( m + 1 ) ^ { 2 } - ( n + 1 ) ^ { 2 } } \right) ^ { 1 / 2 } , \qquad \gamma _ { n , m } = \frac { \alpha _ { n , m } } { \alpha _ { n - 1 , m } } .
$$

When $n \ll m ^ { 1 / 2 }$ , these polynomials are well behaved. However, when $n \gg m ^ { 1 / 2 }$ , they have very large oscillations between the grid points,and a large maximum norm in $[ - 1 , 1 ]$ . Related to this is the fact that when fitting a polynomial to equidistant data, one should never choose $n$ larger than about $2 m ^ { 1 / 2 }$

One of the motivations for the method of least squares is that it effectively reduces the influence of random errors in measurements. Suppose that the values of a function have been measured at points $x _ { 0 } , x _ { 1 } , \ldots , x _ { m }$ Let $f ( x _ { p } )$ be the measured value,and let ${ \bar { f } } ( x _ { p } )$ be the “true”(unknown) function value, which is assumed to be the same as the expected value of the measured value. Thus,no systematic errors are assumed to be present. Suppose further that the errors in measurement at the various points are statistically independent. Then we have $f ( x _ { p } ) = { \bar { f } } ( x _ { p } ) + \epsilon$ ,where

$$
\mathcal { E } ( \epsilon ) = 0 , \qquad \mathcal { V } ( \epsilon ) = s ^ { 2 } I ,
$$

and $\mathcal { E }$ denotes expected value and $\nu$ variance. The problem is to use the measured data to estimate the coeficients in the series $\begin{array} { r } { f ( x ) = \sum _ { j = 0 } ^ { n } c _ { j } \phi ( x ) } \end{array}$

According to the Gauss-Markov theorem (Theorem 1.1.4) the least squares estimates $c _ { j } ^ { * }$ have a smaller variance than the values one gets by any other linear unbiased estimation method. This minimum property holds not only for estimates of the coeffcients $c _ { j }$ but also for every linear function of the coefficients, such as the estimate of the value $f ( \alpha )$ at an arbitrary point $\alpha$ .By Lemma 1.1.1, the covariance matrix of the estimates $c _ { j } ^ { * }$ equals $s ^ { 2 } I$ and $c _ { j } ^ { * }$ and $c _ { k } ^ { * }$ are uncorrelated if $j \neq k$ and the variance of the estimate $c _ { j } ^ { * }$ is $s ^ { 2 }$ .From this it follows that

$$
\mathcal { V } \{ f _ { n } ^ { * } ( \alpha ) \} = \mathcal { V } \bigg \{ \sum _ { j = 0 } ^ { n } c _ { j } ^ { * } \phi _ { j } ( \alpha ) \bigg \} = \sum _ { j = 0 } ^ { n } \mathcal { V } \{ c _ { j } ^ { * } \} | \phi _ { j } ( \alpha ) | ^ { 2 } = s ^ { 2 } \sum _ { j = 0 } ^ { n } | \phi _ { j } ( \alpha ) | ^ { 2 } .
$$

As an average, taken over the grid of measurement points, the variance of the smoothed function values is

$$
\frac { 1 } { m + 1 } \sum _ { j = 0 } ^ { n } \mathcal { V } \{ f _ { n } ^ { * } ( x _ { i } ) \} = \frac { s ^ { 2 } } { m + 1 } \sum _ { j = 0 } ^ { n } \sum _ { i = 0 } ^ { m } | \phi _ { j } ( x _ { i } ) | ^ { 2 } = s ^ { 2 } \frac { n + 1 } { m + 1 } .
$$

Between the grid points, however, the variance can, in many cases, be significantly larger: For $j \gg m ^ { 1 / 2 }$ the Gram polynomials can be much larger between the grid points. Set

$$
s _ { I } ^ { 2 } = s ^ { 2 } \sum _ { j = 0 } ^ { n } { \frac { 1 } { 2 } } \int _ { - 1 } ^ { 1 } | \phi _ { j } ( \alpha ) | ^ { 2 } d \alpha .
$$

Thus, $s _ { I } ^ { 2 }$ is an average variance for $f _ { n } ^ { * } ( \alpha )$ taken over the entire interval $[ - 1 , 1 ]$ . The following values were obtained for the ratio $k$ between $s _ { I } ^ { 2 }$ and $s ^ { 2 } ( n + 1 ) / ( m + 1 )$ when $m = 4 1$ ；see Dahlquist and Bjorck [283,1974, Section 4.4.5]:

$$
\left[ { \begin{array} { c c c c c c c } { n } & { 5 } & { 1 0 } & { 1 5 } & { 2 0 } & { 2 5 } & { 3 0 } & { 3 5 } \\ { k } & { 1 . 0 } & { 1 . 1 } & { 1 . 7 } & { 2 6 } & { 7 \cdot 1 0 ^ { 3 } } & { 1 . 7 \cdot 1 0 ^ { 7 } } & { 8 \cdot 1 0 ^ { 1 1 } } \end{array} } \right]
$$

These results are related to the recommendation that one should choose $n < 2 m ^ { 1 / 2 }$ when fitting a polynomial to equidistant data. This recommendation seems to contradict the Gauss-Markov theorem, but in fact it only means that one gives up the requirement that the estimate be unbiased. Still,it is remarkable that this can lead to such a drastic reduction of the variance of the estimates $f _ { n } ^ { * }$

# 4.5.2 - Chebyshev Interpolation

The most important family of orthogonal polynomials is perhaps the Chebyshev polynomials.8 The easily verified formula

$$
\cos ( n + 1 ) \phi + \cos ( n - 1 ) \phi = 2 \cos \phi \cos ( n \phi ) , \quad n \geq 1 ,
$$

can be used recursively to express $\cos ( n \phi )$ as a polynomial in $\cos \phi$ . If we set $x = \cos \phi$ ,then $\phi \ : = \ : \operatorname { a r c c o s } \ : x$ ，and we obtain the Chebyshev polynomials for $- 1 \leq x \leq 1$ by the formula $T _ { n } ( x ) = \cos ( n \operatorname { a r c c o s } x )$ ， $n \geq 0$ . From trigonometric formulas it follows that the Chebyshev polynomials satisfy the recursion formula

$$
T _ { 0 } ( x ) = 1 , \quad T _ { 1 } ( x ) = x , \quad T _ { n + 1 } ( x ) = 2 x T _ { n } ( x ) - T _ { n - 1 } ( x ) , \quad n \geq 0 .
$$

The leading coefficient of $T _ { n } ( x )$ is $2 ^ { n - 1 }$ for $n \geq 1$ and 1 for $n = 0$ . The symmetry property $T _ { n } ( - x ) = ( - 1 ) ^ { n } T _ { n } ( x )$ also follows from the recurrence formula.

Theorem 4.5.5. $T _ { n } ( x )$ has $n$ zeros in $[ - 1 , 1 ]$ given by the Chebyshev abscissae,

$$
x _ { k } = \cos \Big ( \frac { 2 k + 1 } { n } \frac \pi 2 \Big ) , \quad k = 0 , 1 , \dots , n - 1 ,
$$

and $n + 1$ extrema $T _ { n } ( x _ { k } ^ { \prime } ) = ( - 1 ) ^ { k }$ attained at $x _ { k } ^ { \prime } = \cos ( k \pi / n )$ ， $k = 0 , \ldots , n$ These results follow directly by noting that $| \cos ( n \phi ) |$ has maxima for $\phi _ { k } ^ { \prime } = k \pi / n$ ，and $\cos ( n \phi _ { k } ) = 0$ for $\phi _ { k } = ( 2 k + 1 ) \pi / ( 2 n )$

The Chebyshev polynomials $T _ { 0 } , T _ { 1 } , \dots , T _ { n - 1 }$ are orthogonal with respect to the inner product

$$
( f , g ) = \sum _ { k = 0 } ^ { n - 1 } f ( x _ { k } ) g ( x _ { k } ) ,
$$

where $\{ x _ { k } \}$ are the Chebyshev abscissae (4.5.15) for $T _ { n }$ .If $i \neq j$ ,then $( T _ { i } , T _ { j } ) = 0 , 0 \leq i , j <$ $n$ ,and

$$
( T _ { i } , T _ { j } ) = { \left\{ \begin{array} { l l } { { \frac { 1 } { 2 } } n } & { { \mathrm { i f ~ } } i = j \neq 0 , } \\ { n } & { { \mathrm { i f ~ } } i = j = 0 . } \end{array} \right. }
$$

If one intends to approximate a function in the entire interval $[ - 1 , 1 ]$ by a polynomial and can choose the points at which the function is computed or measured, one should choose the Chebyshev abscissae.With these points, interpolation is a fairly well-conditioned problem in the entire interval,and one can conveniently fit a polynomial of lower degree than $m$ if one wishes to smooth errors in measurement. The risk of disturbing surprises between the grid points is insignificant.

Let $p ( x )$ denote the interpolation polynomial of a function $f ( x )$ at the Chebyshev abscissae $x _ { k }$ (4.5.15). From Theorem 4.5.3 we get

$$
p ( x ) = \sum _ { j = 0 } ^ { n - 1 } c _ { j } T _ { j } ( x ) , \quad c _ { i } = { \frac { 1 } { \| T _ { i } \| ^ { 2 } } } \sum _ { k = 0 } ^ { n - 1 } f ( x _ { k } ) T _ { i } ( x _ { k } ) ,
$$

where $\Vert T _ { i } \Vert _ { 2 }$ is given as in (4.5.16).

Expansions in terms of Chebyshev polynomials are an important aid in the study of functions on the interval $[ - 1 , 1 ]$ . If one is working in terms of a parameter $t$ that varies in the interval $[ a , b ]$ ， then one should make the substitution

$$
t = { \frac { 1 } { 2 } } ( a + b ) + { \frac { 1 } { 2 } } ( a - b ) x
$$

$( t \in [ a , b ] \Leftrightarrow x \in [ - 1 , 1 ] )$ and work with the Chebyshev points

$$
t _ { k } = { \frac { 1 } { 2 } } ( a + b ) + { \frac { 1 } { 2 } } ( a - b ) x _ { k } , \quad k = 0 , \ldots , n - 1 .
$$

The remainder term in interpolation using the values of the function $f$ at the points $x _ { i } , i =$ $0 , 1 , \ldots , n - 1$ , is equal to

$$
\frac { f ^ { ( n ) } ( \xi ) } { ( n ) ! } ( x - x _ { 0 } ) ( x - x _ { 1 } ) \cdot \cdot \cdot ( x - x _ { n - 1 } ) .
$$

Here $\xi$ depends on $x$ ,but one can say that the error curve behaves for the most part like a polynomial curve $y = a ( x - x _ { 0 } ) ( x - x _ { 1 } ) \cdot \cdot \cdot ( x - x _ { n - 1 } )$ . A similar oscillating curve is typical for error curves arising from least squares approximation. The zeros of the error are then about the same as the zeros for the first neglected term in the orthogonal expansion. This contrasts sharply with the error curve for Taylor approximation at $x _ { 0 }$ ,whose usual behavior is described approximately by the formula $y = a ( x - x _ { 0 } ) ^ { n - 1 }$ . From the min-max property of the Chebyshev polynomials it follows that placing the interpolation points of the Chebyshev abscissae will minimize the maximum magnitude of

$$
q ( x ) = ( x - x _ { 0 } ) ( x - x _ { 1 } ) \cdot \cdot \cdot ( x - x _ { n - 1 } )
$$

in the interval $[ - 1 , 1 ]$ . This corresponds to choosing $q ( x ) = T _ { m + 1 } ( x ) / 2 ^ { m }$

For computing $p ( x )$ , one can use Clenshaw's recursion formula; see the previous section. (Note that $\alpha _ { k } \ = \ 2$ for $k > 0$ ，but $\alpha _ { 0 } \ = \ 1 .$ ）Occasionally,one is interested in the partial sums of the expansion. To smooth errors in measurement, it can be advantageous to break off the summation before the last term.If the values of the function are afflicted with statistically independent errors in measurement with standard deviation $s$ ，then (see the next section） the series can be broken off when,for the first time,

$$
\left\| \boldsymbol { f } - \sum _ { j = 0 } ^ { k } c _ { j } T _ { j } \right\| < s n ^ { 1 / 2 } .
$$

If the measurement points are the Chebyshev abscisse,then no difficulties arise in fitting a polynomial to the data. In this case the Chebyshev polynomials have a magnitude between the grid points that is not much larger than their magnitude at the grid points.The average variance for $f _ { n } ^ { * } ( \alpha )$ becomes the same both on the interval $[ - 1 , 1 ]$ and the grid of measurement points: $s ^ { 2 } ( n + 1 ) / ( m + 1 )$

The choice of $n$ ,when $m$ is given, is a question of compromising between taking into account the systematic error, i.e., the truncation error (which decreases when $n$ increases) and taking into account the random errors (which grow as $n$ increases). In the Chebyshev case, $\left| c _ { j } \right|$ decreases quickly with $j$ if $f$ is a sufficiently smooth function, while the part of $c _ { j } ^ { * }$ that comes from errors in measurement varies randomly with magnitude about $s ( 2 / ( m + 1 ) ) ^ { 1 / 2 }$ . The expansion should then be broken off when the coefficients begin to “behave randomly.”The coeficients in an expansion in terms of the Chebyshev polynomials can hence be used for filtering away the“noise” from the signal, even when $s$ is initially unknown.

# 4.5.3 - Discrete Fourier Analysis

According to a mathematical theorem first given by Fourier (1768-1830), every periodic function $f ( t )$ with period $2 \pi / \omega$ can, under certain very general conditions, be expanded into a series of the form

$$
f ( t ) = \sum _ { k = 0 } ^ { \infty } ( a _ { k } \cos k \omega t + b _ { k } \sin k \omega t ) ,
$$

where $a _ { k } , b _ { k }$ are real constants.Fourier analysis is one of the most useful and valuable tools in applied mathematics.It has applications also to problems that are not a priori periodic. One important area of application is in digital signal processing, e.g.,in interpreting radar and sonar signals. Another application is statistical time series,which arise in communications theory, control theory,and the study of turbulence.

An expansion of the form (4.5.17) can be expressed in several equivalent ways. Another form, more convenient for manipulations,is

$$
f ( t ) = \sum _ { - \infty } ^ { \infty } c _ { k } e ^ { i k \omega t } ,
$$

where $c _ { 0 } = a _ { 0 }$ $a _ { 0 } , c _ { k } = ( a _ { k } - i b _ { k } ) / 2 , c _ { - k } = ( a _ { k } + i b _ { k } ) / 2 , k > 0$ .This form allows the function to have complex values.Function $f$ with period $2 \pi$ can be approximated by partial sums of these series.We call these finite sums trigonometric polynomials. If a function of $t$ has period $p$ ， then the substitution $x = 2 \pi t / p$ transforms the function into a function of $x$ with period $2 \pi$

When the functions to be modeled are known only on a discrete equidistant set of sampling points,a discrete version of the Fourier analysis can be used. The discrete inner product of two complex-valued functions $f$ and $g$ of period $2 \pi$ is defined as follows (the bar over $g$ indicates complex conjugation):

$$
( f , g ) = \sum _ { \beta = 0 } ^ { N - 1 } f ( x _ { \beta } ) \bar { g } ( x _ { \beta } ) , \quad x _ { \beta } = 2 \pi \beta / N .
$$

Theorem 4.5.6. With inner product (4.5.19) the following orthogonality relations hold for the functions $\phi _ { j } ( x ) = e ^ { i j x }$ ， $j = 0 , \pm 1 , \pm 2 , . . .$ ：

$$
\left( \phi _ { j } , \phi _ { k } \right) = \left\{ \begin{array} { l l } { N } & { i f ( j - k ) / N i s a n i n t e g e r , } \\ { 0 } & { o t h e r w i s e . } \end{array} \right.
$$

Proof. With $h = 2 \pi / N$ ， $x _ { \beta } = h \beta$ , we have

$$
\left( \phi _ { j } , \phi _ { k } \right) = \sum _ { \beta = 0 } ^ { N - 1 } e ^ { i j x _ { \beta } } e ^ { - i k x _ { \beta } } = \sum _ { \beta = 0 } ^ { N - 1 } e ^ { i ( j - k ) h \beta } .
$$

This is a geometric series with ratio $q = e ^ { i ( j - k ) h }$ $( j - k ) / N$ is an integer, then $q = 1$ and the sum is $N$ . Otherwise, $q \neq 1$ but $q ^ { N } = e ^ { i ( j - k ) 2 \pi } = 1$ From the summation formula of a geometric series, $( \phi _ { j } , \phi _ { k } ) = ( q ^ { N } - 1 ) / ( q - 1 ) = 0$ □

$f$ has a expnsionof the form $\begin{array} { r } { f = \sum _ { j = 0 } ^ { N - 1 } c _ { j } \phi _ { j } } \end{array}$

$$
( f , \phi _ { k } ) = \sum _ { j = a } ^ { b } c _ { j } ( \phi _ { j } , \phi _ { k } ) = c _ { k } ( \phi _ { k } , \phi _ { k } ) , \quad a \leq k \leq b ,
$$

because $( \phi _ { j } , \phi _ { k } ) = 0$ for $j \neq k$ . Thus, changing $k$ to $j$ , we have

$$
c _ { j } = \frac { ( f , \phi _ { j } ) } { ( \phi _ { j } , \phi _ { j } ) } = \frac { 1 } { N } \sum _ { \beta = 0 } ^ { N - 1 } f ( x _ { \beta } ) e ^ { - i j x _ { \beta } } .
$$

Note that the calculations required to compute the coeficients $c _ { j }$ according to (4.5.20), called Fourier analysis,are of essentially the same type as in the calculations needed to tabulate $f ^ { * } ( x )$ for $x = 2 \pi \beta / N$ ， $\beta = 0 , 1 , \ldots , N - 1$ , when the expansion in (4.5.21) is known, the so-called Fourier synthesis.

Theorem 4.5.7. Every function $f ( x )$ defined on the grid $x _ { \beta } = 2 \pi \beta / N _ { ; }$ $\beta = 0 , \ldots , N - 1$ can be interpolated by a trigonometric polynomial

$$
f ( x ) = \sum _ { j = - k } ^ { k + \theta } c _ { j } e ^ { i j x } ,
$$

where

$$
\theta = \left\{ \begin{array} { l l } { { 1 } } & { { i f N e \nu e n , } } \\ { { 0 } } & { { i f N o d d , } } \end{array} \right. \qquad k = \left\{ \begin{array} { l l } { { N / 2 - 1 } } & { { i f N e \nu e n , } } \\ { { ( N - 1 ) / 2 } } & { { i f N o d d . } } \end{array} \right.
$$

If the sum in (4.5.21) is terminated when $j < k + \theta _ { \mathrm { { i } } }$ ， one obtains the trigonometric polynomial that is the best least squares approximation, among alltrigonometric polynomials with the same number of terms,to $f$ on the grid.

Proof. The expression for $c _ { j }$ was formally derived previously (see (4.5.20)). Because

$$
e ^ { - i ( N - j ) x _ { \beta } } = e ^ { i j x _ { \beta } } , \quad c _ { - j } = c _ { N - j } ,
$$

$f ( x )$ coincidesonthegrid withtefunction $\begin{array} { r } { f ^ { * } ( x ) = \sum _ { j = 0 } ^ { N - 1 } c _ { j } e ^ { i j x } } \end{array}$ However,between the grid points, $f$ and $f ^ { * }$ are not identical. Functions of several variables can be treated analogously by taking one variable at a time. □

By (4.5.20), the discrete Fourier coefficients $c _ { j }$ for a function

$$
f ( x ) = \sum _ { j = 0 } ^ { N - 1 } c _ { j } e ^ { i j x } ,
$$

whose values are known at the points $x = 2 \pi \beta / N , \beta = 0 , \ldots , N - 1$ are

$$
c _ { j } = \sum _ { \beta = 0 } ^ { N - 1 } f ( x _ { \beta } ) \omega ^ { j \beta } , \quad f _ { \beta } = \frac { 1 } { N } f ( x _ { \beta } ) , \quad j = 0 , \ldots , N - 1 ,
$$

where $\omega = e ^ { - 2 \pi i / N }$ is the $n$ th root of unity $\boldsymbol { \omega } ^ { N } = 1 \dot { }$ ). Hence $c _ { j }$ is a polynomial of degree $N - 1$ in $\omega ^ { j }$ .Let $F _ { N } \in \mathbb { R } ^ { N \times N }$ be the Fourier matrix with elements

$$
( F _ { N } ) _ { j \beta } = \omega ^ { j \beta } , \quad j , \beta = 0 , \dots , N - 1 .
$$

It folows that the discrete Fourier transform can be expressed as a matrix-vector multiplication $c = F _ { N } f$ ，where the discrete Fourier transform (DFT) matrix $F _ { N }$ is a complex symmetric Vandermonde matrix. Furthermore,

$$
\frac { 1 } { N } F _ { N } ^ { H } F _ { N } = I ,
$$

i.e., $N ^ { - 1 / 2 } F _ { N }$ is a unitary matrix, and the inverse transform is

$$
f = \frac { 1 } { N } F _ { N } ^ { H } c .
$$

If implemented in a naive way, the DFT will take $N ^ { 2 }$ operations to compute all $c _ { j }$ (here, one operation equals one complex addition and one complex multiplication). The application of discrete Fourier analysis to large-scale problems became feasible only with the invention of the so-called fast Fourier transform (FFT) that reduces the computational complexity to $O ( N \log N )$ The FFT,developed in 1965 by Cooley and Tukey [269,1965],is based on the divide-andconquer strategy. Consider the special case when $N = 2 ^ { p }$ and set

$$
\beta = \left\{ \begin{array} { l l } { 2 \beta _ { 1 } } & { \mathrm { i f ~ } \beta \mathrm { ~ e v e n } , } \\ { 2 \beta _ { 1 } + 1 } & { \mathrm { i f ~ } \beta \mathrm { ~ o d d } , } \end{array} \right. \quad 0 \leq \beta _ { 1 } \leq \frac { 1 } { 2 } N - 1 .
$$

Then the sum in (4.5.22) can be split into an even part and an odd part:

$$
c _ { j } = \sum _ { \beta _ { 1 } = 0 } ^ { \frac 1 2 N - 1 } f _ { 2 \beta _ { 1 } } ( \omega ^ { 2 } ) ^ { j \beta _ { 1 } } + \sum _ { \beta _ { 1 } = 0 } ^ { \frac 1 2 N - 1 } f _ { 2 \beta _ { 1 } + 1 } ( \omega ^ { 2 } ) ^ { j \beta _ { 1 } } \omega ^ { j } .
$$

Let $\alpha$ be the quotient and $j _ { 1 }$ the remainder when $j$ is divided by ${ \scriptstyle { \frac { 1 } { 2 } } } N$ ,i.e., $j = \alpha _ { 2 } ^ { \underline { { { 1 } } } } N + j _ { 1 }$ Then, because $\omega ^ { N } = 1$ ，

$$
( \omega ^ { 2 } ) ^ { j \beta _ { 1 } } = ( \omega ^ { 2 } ) ^ { \alpha ( 1 / 2 ) N \beta _ { 1 } } ( \omega ^ { 2 } ) ^ { j _ { 1 } \beta _ { 1 } } = ( \omega ^ { N } ) ^ { \alpha \beta _ { 1 } } ( \omega ^ { 2 } ) ^ { j _ { 1 } \beta _ { 1 } } = ( \omega ^ { 2 } ) ^ { j _ { 1 } \beta _ { 1 } } .
$$

Thus, if for $j _ { 1 } = 0 , 1 , \ldots , \textstyle { \frac { 1 } { 2 } } N - 1$ we set

$$
\phi ( j _ { 1 } ) = \sum _ { \beta _ { 1 } = 0 } ^ { \frac 1 2 N - 1 } f _ { 2 \beta _ { 1 } } ( \omega ^ { 2 } ) ^ { j _ { 1 } \beta _ { 1 } } , \quad \psi ( j _ { 1 } ) = \sum _ { \beta _ { 1 } = 0 } ^ { \frac 1 2 N - 1 } f _ { 2 \beta _ { 1 } + 1 } ( \omega ^ { 2 } ) ^ { j _ { 1 } \beta _ { 1 } } ,
$$

where $\left( \omega ^ { 2 } \right) ^ { \frac { 1 } { 2 } N } = 1$ , then by (4.5.24),

$$
c _ { j } = \phi ( j _ { 1 } ) + \omega ^ { j } \psi ( j _ { 1 } ) , \quad j = 0 , 1 , \ldots , N - 1 .
$$

The two sums on the right are elements of the DFTs of length $N / 2$ applied to the parts of $f$ with odd and even subscripts. The DFT of length $N$ is obtained by combining these two DFTs. Since (N/2)=-1,it follows that

$$
\begin{array} { l } { y _ { j _ { 1 } } = \phi _ { j _ { 1 } } + \omega _ { N } ^ { j _ { 1 } } \psi _ { j _ { 1 } } , } \\ { y _ { j _ { 1 } + N / 2 } = \phi _ { j _ { 1 } } - \omega _ { N } ^ { j _ { 1 } } \psi _ { j _ { 1 } } , \quad j _ { 1 } = 0 , \hdots , N / 2 - 1 . } \end{array}
$$

These expressions are called the butterfly relations because of the data flow pattern. The computation of $\phi _ { j _ { 1 } }$ and $\psi _ { j _ { 1 } }$ is equivalent to two Fourier transforms with $m = N / 2$ terms instead of one with $N$ terms. If $N / 2$ is even,the same idea can be applied to these two Fourier transforms. One then gets four Fourier transforms,each of which has $N / 4$ terms. If $N = 2 ^ { p }$ , this reduction can be continued recursively until we get $N$ DFTs with one term. Each step involves an evenodd permutation. In the first step the points with last binary digit equal to O are ordered first, and those with last digit equal to 1 are ordered last. In the next step the two resulting subsequences of length $N / 2$ are reordered according to the second binary digit, etc.

The number of complex operations (one multiplication and one addition) required to compute $\{ y _ { j } \}$ from the butterfly relations when $\{ \phi _ { j _ { 1 } } \}$ and $\{ \psi _ { j _ { 1 } } \}$ have been computed is $2 ^ { p }$ , assuming that the powers of $\omega$ are precomputed and stored. If we denote by $q _ { p }$ the total number of operations needed to compute the DFT when $N = 2 ^ { p }$ ， we have $q _ { p } \leq 2 q _ { p - 1 } + 2 ^ { p }$ ， $p \geq 1$ Since $q _ { 0 } = 0$ ,it follows by induction that

$$
q _ { p } \leq p 2 ^ { p } = N \log _ { 2 } N .
$$

Hence, when $N$ is a power of two,the FFT solves the problem with at most $N \cdot \log _ { 2 } N$ complex operations. For example, when $N = 2 ^ { 2 0 } = 1 , 0 4 8 , 5 7 6$ the FFT algorithm is theoretically a factor of 84,00o faster than the “conventional” $O ( N ^ { 2 } )$ algorithm. The FFT algorithm not only uses fewer operations to evaluate the DFT, it also is more accurate.For the conventional method, the roundoff error is proportional to $N$ .For the FFT algorithm,the roundoff error is proportional to $\log _ { 2 } N$

Most implementations of FFT avoid explicit recursion and instead use two stages.

· A reordering stage in which the data vector $f$ is permuted in bit-reversal order. ·A second stage in which first $N / 2$ FFT transforms of length 2 are computed on adjacent elements,followed by $N / 4$ transforms of length 4,etc., until the final result is obtained by merging two FFTs of length $N / 2$

It is not difficult to see that the combined effect of the reordering in the first stage is a bitreversal permutation of the data points. For $i = 0 : N - 1$ ,let the index $i$ have the binary expansion $i = b _ { 0 } + b _ { 1 } \cdot 2 + \cdot \cdot \cdot + b _ { t - 1 } \cdot 2 ^ { t - 1 }$ ,and set

$$
r ( i ) = b _ { t - 1 } + \cdot \cdot \cdot + b _ { 1 } \cdot 2 ^ { t - 2 } + b _ { 0 } \cdot 2 ^ { t - 1 } .
$$

That is, $r ( i )$ is the index obtained by reversing the order of the binary digits.If $i < r ( i )$ ,then exchange $f _ { i }$ and $f _ { r ( i ) }$ . We denote the permutation matrix performing the bit-reversal ordering by $P _ { N }$ . Note that if an index is reversed twice,we end up with the original index. This means that $P _ { N } ^ { - 1 } = P _ { N } ^ { T } = P _ { N }$ ,i.e., $P _ { N }$ is symmetric. The permutation can be carred out“in place" by a sequence of pairwise interchanges or transpositions of the data points. For example, for $N =$ 16,the pairs (1,8), (2,4), (3,12),(5,10), (7,14),and (11,13) are interchanged. The bit-reversal permutation can take a substantial fraction of the total time to do the FFT. Which implementation is best depends strongly on the computer architecture.

When $N = 2 ^ { p }$ the FFT algorithm can be interpreted as a sparse factorization of the DFT matrix,

$$
F _ { N } = A _ { k } \cdot \cdot \cdot A _ { 2 } A _ { 1 } P _ { N } ,
$$

where $P _ { N }$ is the bit-reversal permutation matrix, and $A _ { 1 } , \ldots , A _ { k }$ are block diagonal matrices:

$$
A _ { q } = \mathrm { d i a g } ( \underbrace { B _ { L } , \ldots , B _ { L } } _ { r } ) , \quad L = 2 ^ { q } , \quad r = N / L .
$$

Here the matrix $B _ { k } \in \mathbb { C } ^ { L \times L }$ is theradix-2buterfly matrix defied by

$$
\begin{array} { r } { B _ { L } = \left( \begin{array} { c c } { I _ { L / 2 } } & { \Omega _ { L / 2 } } \\ { I _ { L / 2 } } & { - \Omega _ { L / 2 } } \end{array} \right) , } \end{array}
$$

$$
\Omega _ { L / 2 } = \mathrm { d i a g } \left( 1 , \omega _ { L } , . . . , \omega _ { L } ^ { L / 2 - 1 } \right) , \quad \omega _ { L } = e ^ { - 2 \pi i / L } . \nonumber
$$

This is usually referred to as the Cooley-Tukey FFT algorithm.

The discrete cosine transform (DCT) was discovered in 1974 by Ahmed, Natarajan, and Rao [11,1974l; see also Rao and Yio [913,199o]. The DCT has real entries as opposed to the complex entries of the FFT matrix.Depending on the type of boundary condition (Dirichlet or Neumann, centered at a mesh point or midpoint) there are different variants. The DCT-2 transform is used extensively in image processing. It uses the real basis vectors

$$
v _ { i , j } = { \sqrt { \frac { N } { 2 } } } \cos { \big ( } ( j - 1 ) ( i + { \textstyle { \frac { 1 } { 2 } } } ) { \big ) } \pi ,
$$

divided by $\sqrt { 2 }$ if $j = 1$ . Strang [1044,1999] surveys the four possible variants of cosine transforms DCT-1,..,DCT-4 and their use for different boundary conditions.

# Notes and references

The computational advantage of the Stieltjes approach for polynomial approximation was pointed out by Forsythe [422,1956]. Van Loan [1082,1992] gives a unified treatment of FFT algorithms based on the factorization of the Fourier matrix $F _ { N }$ into a product of sparse matrix factors. Ideas related to the FFT can be found in many previous works;see Cooley [267,199o]. Excellent surveys of the use of the discrete Fourier transform are given by Cooley,Lewis,and Welsh [268, 1969] and Henrici [604,1979].

# 4.5.4 - Vandermonde Systems

A Vandermonde matrix has the form

$$
V = V ( x _ { 0 } , x _ { 1 } , \ldots , x _ { n } ) = \left( \begin{array} { c c c c } { { 1 } } & { { 1 } } & { { \cdots } } & { { 1 } } \\ { { x _ { 0 } } } & { { x _ { 1 } } } & { { \cdots } } & { { x _ { n } } } \\ { { \vdots } } & { { \vdots } } & { { } } & { { \vdots } } \\ { { x _ { 0 } ^ { n } } } & { { x _ { 1 } ^ { n } } } & { { \cdots } } & { { x _ { n } ^ { n } } } \end{array} \right) ,
$$

where {xk}κ=0 is a sequence of $n + 1$ distinct real numbers. Vandermonde matrices arise in many applications,such as interpolation and approximation of linear functionals. Consider first the problem of constructing a polynomial

$$
p ( x ) = a _ { 0 } + a _ { 1 } x + \cdot \cdot \cdot + a _ { n } x ^ { n }
$$

that interpolates data

$$
( x _ { i } , f _ { i } ) , \quad i = 0 , 1 , \ldots , n .
$$

It is easily shown that coefficients $a = ( a _ { 0 } , a _ { 1 } , \ldots , a _ { n } ) ^ { T }$ satisfy the dual Vandermonde system $V ^ { T } a = f$ . The primal system $V w = b$ arises from the problem of determining the weights $w _ { 0 } , w _ { 1 } , \ldots , w _ { n }$ in a quadrature formula when given the moments

$$
w _ { 0 } x _ { 0 } ^ { i } + w _ { 1 } x _ { 1 } ^ { i } + \cdot \cdot \cdot + w _ { n } x _ { n } ^ { i } = b _ { i } , \quad i = 1 , \dots , n .
$$

Vandermonde systems are often extremely ill-conditioned because they correspond to an interpolation problem with a monomial basis. An accurate and fast algorithm for solving primal or dual Vandermonde systems in $O ( n ^ { 2 } )$ multiplications and $O ( n )$ is given by Bjorck and Pereyra [152,197o]. This algorithm corresponds to decomposition of the inverse $V ^ { - 1 }$ into a product

$$
V ^ { - 1 } = { \cal U } _ { 0 } \cdot \cdot \cdot { \cal U } _ { n - 1 } L _ { n - 1 } \cdot \cdot \cdot L _ { 0 }
$$

of upper and lower bidiagonal matrices. These algorithms are generalized to confluent Vandermonde systems by Bjorck and Elfving [140,1973]. The corresponding dual system then is a Hermite interpolation problem.

The fast Bjorck-Pereyra algorithms often achieve better accuracy in the computed solution than standard (and more expensive) methods like Gaussian elimination with partial pivoting. Indeed, some problems connected with Vandermonde systems that,traditionally,have been thought to be too ill-conditioned to be attacked, can be solved with good precision.

The determinant of a square submatrix of a matrix $A$ is called a minor of $A$ . If all minors of $A$ are positive, then $A$ is called totally positive.Let the Vandermonde matrix $V$ have points $\{ x _ { k } \} _ { k = 0 } ^ { n }$ that are positive and monotonically ordered: $0 < x _ { 0 } < x _ { 1 } < \cdot \cdot \cdot < x _ { n }$ . Then from the well-known formula

$$
\operatorname* { d e t } ( V ) = \prod _ { i > j } ( x _ { i } - x _ { j } )
$$

it follows that $V = V ( x _ { 0 } , x _ { 1 } , \dots , x _ { n } )$ has positive determinant and positive leading principal minors. More generally, it is known that $V$ is totally positive. For such Vandermonde systems, Higham [612, $\mathbf { 1 9 8 7 } ]$ shows that if the right-hand side is sign-interchanging, $( - 1 ) ^ { k } b _ { k } \geq 0$ ,then the error in the solution computed by the Bjorck-Pereyra algorithm can be bounded by a quantity independent of $\kappa ( V )$

A Vandermonde-like matrix $V = \left( v _ { i j } \right)$ has elements $v _ { i j } = \phi _ { i } ( x _ { j } )$ ， $0 \leq i , j \leq n$ ，where $\{ \phi _ { i } \} _ { 0 } ^ { n }$ is a family of orthonormal polynomials that satisfy a three-term recurrence of the form (4.5.5). Such matrices generally have much smaller condition numbers than the classical Vandermonde matrices. Higham [613,1988] and Reichel [916,1991] give fast algorithms of Bjorck-Pereyra type for such systems. Demmel and Koev [311, 2oo5l prove that Bjorck-Pereyra-type algorithms exist not only for such systems but also for any totally positive linear system for which the initial minors can be computed accurately.

Let $V \in \mathbb { R } ^ { m \times n }$ be a rectangular Vandermonde matrix consisting of the first $n < m$ columns of $V ( x _ { 0 } , x _ { 1 } , \dots , x _ { m } )$ . It is natural to ask whether fast methods exist for solving the primal Vandermonde least squares problem

$$
\operatorname* { m i n } _ { x } \| V x - b \| _ { 2 } .
$$

Demeure [301,198g],[302,199o] has given an algorithm of complexity $O ( m n )$ for computing the QR factorization of $V$ ，which can be used to solve problem (4.5.34).However, because this algorithm forms $V ^ { T } V$ , it is likely to be unstable.A fast algorithm based on the Gragg-Harrod scheme [523, $\mathrm { 1 9 8 4 } ]$ for computing the QR factorization of transposed Vandermonde-like matrices is given by Reichel [916,1991]. This algorithm can be used to solve overdetermined dual Vandermonde-like systems in the least squares sense in $O ( m n )$ operations.

# Notes and references

A survey of properties of totally positive matrices is given by Fallat [393, 2Oo1]. Higham [623, 2002,Chapter 22],surveys algorithms for Vandermonde systems. The remarkable numerical stability obtained for Vandermonde systems has counterparts for other classes of structured ma-trices. Boros, Kailath,and Olshevsky [171,1999l derive fast paralel Bjorck-Pereyra-type algorithms for solving Cauchy linear equation $C x = d$ ，

$$
C = \left( \begin{array} { c c c } { \frac { 1 } { x _ { 0 } - y _ { 0 } } } & { \cdots } & { \frac { 1 } { x _ { 0 } - y _ { n } } } \\ { \vdots } & { \ddots } & { \vdots } \\ { \frac { 1 } { x _ { n } - y _ { 0 } } } & { \cdots } & { \frac { 1 } { x _ { n } - y _ { n } } } \end{array} \right) .
$$

This class of systems includes Hilbert linear systems with sign-interchanging right-hand side. Martinez and Pena [780,1998] discuss algorithms of similar type for Cauchy-Vandermonde matrices of the form $( C V )$

# 4.5.5 - Toeplitz and Hankel Least Squares Problems

A Toeplitz matrix $T = ( t _ { i j } )$ is a matrix with constant entries along each diagonal parallel to the main diagonal. A rectangular Toeplitz matrix

$$
T = \left( \begin{array} { c c c c c c } { t _ { 0 } } & { t _ { 1 } } & { \dots } & { t _ { n } } \\ { t _ { - 1 } } & { t _ { 0 } } & { \ddots } & { \vdots } \\ { \vdots } & { \ddots } & { \ddots } & { t _ { 1 } } \\ { t _ { - n } } & { \dots } & { t _ { - 1 } } & { t _ { 0 } } \\ { \vdots } & { \vdots } & { \vdots } & { \vdots } \\ { t _ { - m } } & { t _ { - m + 1 } } & { \dots } & { t _ { - m + n } } \end{array} \right) \in \mathbb { R } ^ { ( m + 1 ) \times ( n + 1 ) }
$$

is defined by its $n + m + 1$ elements $t _ { - m } , \ldots , t _ { 0 } , \ldots , t _ { n }$ in the first row and column. Toeplitz matrices arise from discretization of convolution-type integral equations and play a fundamental role in signal processing, time-series analysis, econometrics,and image deblurring; see Hansen, Nagy,and O'Leary [583,2006].

The BBH algorithm of Bojanczyk,Brent,and de Hoog [162,1986] is a fast algorithm for computing the QR factorization of a Toeplitz matrix. It is related to a classical algorithm of Schur and requires $O ( m n + n ^ { 2 } )$ instead of $O ( m n ^ { 2 } )$ operations．The basic idea of the BBH algorithm is to partition $T$ in two different ways,

$$
T = \left( \begin{array} { c c } { { t _ { 0 } } } & { { u ^ { T } } } \\ { { v } } & { { T _ { 0 } } } \end{array} \right) = \left( \begin{array} { c c } { { T _ { 0 } } } & { { \tilde { u } } } \\ { { \tilde { v } ^ { T } } } & { { t _ { m - n } } } \end{array} \right) ,
$$

where $T _ { 0 }$ is a submatrix of $T$ ， $u$ and $\tilde { v }$ are $n - 1$ dimensional vectors, $v$ and $\tilde { u }$ are $m - 1$ vectors, and $t _ { 0 }$ and $t _ { m - n }$ are scalars. Let $R$ be the Cholesky factor of $T ^ { T } T$ , and partition $R$ as

$$
R = \left( \begin{array} { c c } { { r _ { 1 1 } } } & { { z ^ { T } } } \\ { { 0 } } & { { R _ { b } } } \end{array} \right) = \left( \begin{array} { c c } { { R _ { t } } } & { { \tilde { z } } } \\ { { 0 } } & { { r _ { n n } } } \end{array} \right) ,
$$

where $r _ { 1 1 }$ and $r _ { n n }$ are scalars.The factor $R$ in the QR factorization of $T$ is implicitly derived from the cross-product $T ^ { T } T$ Setting $R ^ { T } R \ : = \ : T ^ { T } T$ and using the partitioning (4.5.36) and (4.5.37), we get

$$
\left( \begin{array} { c c } { { r _ { 1 1 } ^ { 2 } } } & { { r _ { 1 1 } z ^ { T } } } \\ { { r _ { 1 1 } z } } & { { z z ^ { T } + R _ { b } ^ { T } R _ { b } } } \end{array} \right) = \left( \begin{array} { c c } { { t _ { 0 } ^ { 2 } + v ^ { T } v } } & { { t _ { 0 } u ^ { T } + v ^ { T } T _ { 0 } } } \\ { { t _ { 0 } u + T _ { 0 } ^ { T } v } } & { { u u ^ { T } + T _ { 0 } ^ { T } T _ { 0 } } } \end{array} \right)
$$

and

$$
\left( \begin{array} { l l } { R _ { t } ^ { T } R _ { t } } & { R _ { t } ^ { T } \tilde { z } } \\ { \tilde { z } ^ { T } R _ { t } } & { \tilde { z } ^ { T } \tilde { z } + r _ { n n } ^ { 2 } } \end{array} \right) = \left( \begin{array} { c c } { T _ { 0 } ^ { T } T _ { 0 } + \tilde { v } \tilde { v } ^ { T } } & { T _ { 0 } ^ { T } \tilde { u } + t _ { m - n } \tilde { v } } \\ { \tilde { u } ^ { T } T _ { 0 } + t _ { m - n } \tilde { v } ^ { T } } & { \tilde { u } ^ { T } \tilde { u } + t _ { m - n } ^ { 2 } } \end{array} \right) .
$$

From (4.5.38) and (4.5.39) we see that

$$
z z ^ { T } + R _ { b } ^ { T } R _ { b } = u u ^ { T } + T _ { 0 } ^ { T } T _ { 0 } , \qquad R _ { t } ^ { T } R _ { t } = T _ { 0 } ^ { T } T _ { 0 } + \tilde { v } \tilde { v } ^ { T } .
$$

Eliminating the term $T _ { 0 } ^ { T } T _ { 0 }$ , we obtain

$$
\boldsymbol { R _ { b } ^ { T } } \boldsymbol { R _ { b } } = \boldsymbol { R _ { t } ^ { T } } \boldsymbol { R _ { t } } + \boldsymbol { u u ^ { T } } - \boldsymbol { \tilde { v } } \boldsymbol { \tilde { v } ^ { T } } - \boldsymbol { z z ^ { T } } ,
$$

which is the basic equality used by the BBH algorithm. This shows that if $R _ { t }$ were known, $R _ { b }$ would be computed by one Cholesky updating step and two Cholesky downdating steps; see Section 3.3.4. Moreover, because updating and downdating can proceed by rows, the first $k$ rows of $R _ { b }$ can be obtained from the frst $k$ rows of $R _ { b }$ . But the $k \mathrm { t h }$ row of $R _ { b }$ defines the $( k + 1 ) \operatorname { t h }$ row of $R _ { t }$ ,and the first row of $R$ can be obtained from (4.5.38):

$$
r _ { 1 1 } = \sqrt { t _ { 0 } ^ { 2 } + v ^ { T } v } , \qquad z ^ { T } = ( t _ { 0 } u ^ { T } + v ^ { T } T _ { 0 } ) / r _ { 1 1 } .
$$

It follows that (4.5.40) provides a method for computing $R$ one row at a time.

The BBH algorithm requires $m n ^ { 2 } + 6 n ^ { 2 }$ multiplications and is more effcient than the $O ( m n ^ { 2 } )$ methods when $n > 2 5 6$ .Nagy [818,1993] modified the BBH algorithm to compute $R ^ { - 1 }$ ， $Q ^ { T } b$ ， and the solution $x$ using a linear amount of storage and $2 m n + 1 4 n ^ { 2 }$ multiplications.Another possibility is to use the corrected seminormal equations to obtain $x$ ，This can also be implemented in linear storage (see Nagy [818,1993l). Another fast algorithm by Chun, Kailath,and Lev-Ari [249, $\mathrm { 1 9 8 7 } ]$ is essentially equivalent to the BBH algorithm.

For ill-conditioned problems the BBH algorithm does not perform well, because it uses the explicit cross-product matrix. Park and Eldén [881，1997l give a forward error analysis that allows the conditioning of the problem to be monitored. For ill-conditioned problems their algorithm uses the corrected seminormal equations to produce more accurate triangular factors than those of other fast algorithms.

Discretization of a convolution-type Volterra integral equations of the first kind,

$$
\int _ { 0 } ^ { t } K ( t - s ) f ( t ) d t = g ( s ) , \quad 0 \leq t \leq T ,
$$

gives a linear system with an upper triangular Toeplitz matrix

$$
T = \left( \begin{array} { c c c c c c } { { t _ { 1 } } } & { { t _ { 2 } } } & { { \dots } } & { { t _ { n - 1 } } } & { { t _ { n } } } \\ { { } } & { { t _ { 1 } } } & { { t _ { 2 } } } & { { } } & { { t _ { n - 1 } } } \\ { { } } & { { } } & { { \ddots } } & { { \ddots } } & { { } } & { { \vdots } } \\ { { } } & { { } } & { { } } & { { t _ { 1 } } } & { { t _ { 2 } } } \\ { { } } & { { } } & { { } } & { { } } & { { t _ { 1 } } } \end{array} \right) .
$$

For the Tikhonov regularization problem

$$
\operatorname* { m i n } _ { \boldsymbol { x } } \| T \boldsymbol { x } - b \| _ { 2 } ^ { 2 } + \lambda ^ { 2 } \| L \boldsymbol { x } \| _ { 2 } ^ { 2 } ,
$$

where both $T$ and $L$ are upper triangular and Toeplitz, Eldén [370,1984l gives an algorithm that only requires $9 n ^ { 2 }$ flops for computing the solution for a given value of $\lambda$ .His algorithm can be modified to handle also the case when $T$ and $L$ have a few nonzero diagonals below the main diagonal. Eldén's algorithm uses $n ^ { 2 } / 2$ storage locations.A modification that only uses $O ( n )$ storage locations is given by Bojanczyk and Brent [161,1986].

An alternative to direct methods for Toeplitz least squares problems is to use iterative methods,such as the preconditioned conjugate gradient method; see Section 6.2.2. This requires in each iteration step one matrix-vector multiplication with $T$ and $T ^ { H }$ . Such products can be implemented in $O ( m \log m )$ operations and $O ( m + n )$ storage using FFT; see Section 6.3.7.

Let $T = ( t _ { i j } )$ be a Toeplitz matrix, and let $J$ denote the reverse permutation matrix. Then $H = T J$ has constant entries along each antidiagonal, i.e., $H$ is a Hankel matrix. For example, if $n = 2$ ， $m = 3$ ,then

$$
H = T J = \left( \begin{array} { c c c } { { t _ { 2 } } } & { { t _ { 1 } } } & { { t _ { 0 } } } \\ { { t _ { 1 } } } & { { t _ { 0 } } } & { { t _ { - 1 } } } \\ { { t _ { 0 } } } & { { t _ { - 1 } } } & { { t _ { - 2 } } } \\ { { t _ { - 1 } } } & { { t _ { - 2 } } } & { { t _ { - 3 } } } \end{array} \right) .
$$

Since the reverse permutation matrix satisfies $J ^ { - 1 } = J$ we have $H J = T$ Hence,methods discussed in this section for solving Toeplitz least squares problems apply to Hankel least squares problems as well.

# Notes and references

There is an extensive literature on Toeplitz matrices.Bunch [186,1985] investigates the stability properties of classical and fast algorithms for solving Toeplitz systems. Surveys can be found in Brent [179,1988] and Bojanczyk,Brent,and de Hoog [163,1993]. An $O ( m n )$ algorithm for QR factorization of Toeplitz and block Toeplitz matrices was given by Sweet [i053,1984] but was later shown to be unstable.A different approach is used by Cybenko [282,1987], who gives an algorithm for computing $R ^ { - 1 }$ and $Q \in \mathbb { R } ^ { m \times n }$ based on the so-called lattice algorithm. This algorithm requires that all submatrices $T _ { : , 1 : i }$ ， $i = 1 , \ldots , n$ ,be well-conditioned,which is not always the case in applications.Hansen and Gesmar [581,1993l give a modification of Cybenko's algorithm in which a block step is used to skip over linearly dependent columns. For solving symmetric positive definiteToeplitz linear systems,a “superfast” algorithm that only requires $\bar { O ( m \log ^ { 2 } n ) }$ operations has been proposed; see Ammar and Gragg [2O,1988].
