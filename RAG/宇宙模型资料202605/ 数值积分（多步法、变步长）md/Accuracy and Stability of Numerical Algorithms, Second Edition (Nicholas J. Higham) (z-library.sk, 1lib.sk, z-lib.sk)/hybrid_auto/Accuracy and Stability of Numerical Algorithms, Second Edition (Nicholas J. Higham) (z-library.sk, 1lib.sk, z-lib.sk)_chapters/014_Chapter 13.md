# Chapter 13

# Block LU Factorization

Block algorithms are advantageous for at least two important reasons. First, they work with blocks of data having $b^2$ elements, performing $O(b^3)$ operations. The $O(b)$ ratio of work to storage means that processing elements with an $O(b)$ ratio of computing speed to input/output bandwidth can be tolerated. Second, these algorithms are usually rich in matrix multiplication. This is an advantage because nearly every modern parallel machine is good at matrix multiplication. BERT S. SCHREIBER, Block Algorithms for Parallel Machines (1988)

It should be realized that, with partial pivoting, any matrix has a triangular factorization. DECOMP actually works faster when zero pivots occur because they mean that the corresponding column is already in triangular form. GEORGE E. FORSYTHE, MICHAEL A. MALCOLM, and CLEVE B. MOLER, Computer Methods for Mathematical Computations (1977)

It was quite usual when dealing with very large matrices to perform an iterative process as follows: the original matrix would be read from cards and the reduced matrix punched without more than a single row of the original matrix being kept in store at any one time; then the output hopper of the punch would be transferred to the card reader and the iteration repeated. MARTIN CAMPBELL-KELLY, Programming the Pilot ACE (1981)

# 13.1. Block Versus Partitioned LU Factorization

As we noted in Chapter 9 (Notes and References), Gaussian elimination (GE) comprises three nested loops that can be ordered in six ways, each yielding a different algorithmic variant of the method. These variants involve different computational kernels: inner product and saxpy operations (level-1 BLAS), or outer product and gaxpy operations (level-2 BLAS). To introduce matrix-matrix operations (level-3 BLAS), which are beneficial for high-performance computing, further manipulation beyond loop reordering is needed. We will use the following terminology, which emphasises an important distinction.

A partitioned algorithm is a scalar (or point) algorithm in which the operations have been grouped and reordered into matrix operations.

A block algorithm is a generalization of a scalar algorithm in which the basic scalar operations become matrix operations ( $\alpha + \beta$ , $\alpha \beta$ , and $\alpha / \beta$ become $A + B$ , $AB$ , and $AB^{-1}$ ), and a matrix property based on the nonzero structure becomes the corresponding property blockwise (in particular, the scalars 0 and 1 become the zero matrix and the identity matrix, respectively). A block factorization is defined in a similar way and is usually what a block algorithm computes.

A partitioned version of the outer product form of LU factorization may be developed as follows. For $A \in \mathbb{R}^{n \times n}$ and a given block size $r$ , write

$$
\left[ \begin{array}{l l} A _ {1 1} & A _ {1 2} \\ A _ {2 1} & A _ {2 2} \end{array} \right] = \left[ \begin{array}{c c} L _ {1 1} & 0 \\ L _ {2 1} & I _ {n - r} \end{array} \right] \left[ \begin{array}{c c} I _ {r} & 0 \\ 0 & S \end{array} \right] \left[ \begin{array}{c c} U _ {1 1} & U _ {1 2} \\ 0 & I _ {n - r} \end{array} \right], \tag {13.1}
$$

where $A_{11}$ is $r\times r$

Algorithm 13.1 (partitioned LU factorization). This algorithm computes an LU factorization $A = LU \in \mathbb{R}^{n \times n}$ using a partitioned outer product implementation, using block size $r$ and the notation (13.1).

1. Factor $A_{11} = L_{11}U_{11}$ .   
2. Solve $L_{11}U_{12} = A_{12}$ for $U_{12}$ .   
3. Solve $L_{21}U_{11} = A_{21}$ for $L_{21}$ .   
4. Form $S = A_{22} - L_{21}U_{12}$ .   
5. Repeat steps 1-4 on $S$ to obtain $L_{22}$ and $U_{22}$ .

Note that in step 4, $S = A_{22} - A_{21}A_{11}^{-1}A_{12}$ is the Schur complement of $A_{11}$ in $A$ . Steps 2 and 3 require the solution of the multiple right-hand side triangular systems, so steps 2-4 are all level-3 BLAS operations. This partitioned algorithm does precisely the same arithmetic operations as any other variant of GE, but it does the operations in an order that permits them to be expressed as matrix operations.

A genuine block algorithm computes a block LU factorization, which is a factorization $A = LU \in \mathbb{R}^{n \times n}$ , where $L$ and $U$ are block triangular and $L$ has identity matrices on the diagonal:

$$
L = \left[ \begin{array}{c c c c} I & & & \\ L _ {2 1} & I & & \\ \vdots & & \ddots & \\ L _ {m 1} & \ldots & L _ {m, m - 1} & I \end{array} \right], \quad U = \left[ \begin{array}{c c c c} U _ {1 1} & U _ {1 2} & \ldots & U _ {1 m} \\ & U _ {2 2} & & \vdots \\ & & \ddots & U _ {m - 1, m} \\ & & & U _ {m m} \end{array} \right].
$$

In general, the blocks can be of different dimensions. Note that this factorization is not the same as a standard LU factorization, because $U$ is not triangular. However, the standard and block LU factorizations are related as follows: if $A = LU$ is a block LU factorization and each $U_{ii}$ has an LU factorization $U_{ii} = \overline{L}_{ii}\overline{U}_{ii}$ , then $A = L\mathrm{diag}(\overline{L}_{ii})\cdot \mathrm{diag}(\overline{U}_{ii})U$ is an LU factorization. Conditions for the existence of a block LU factorization are easy to state.

Theorem 13.2. The matrix $A = (A_{ij})_{i,j=1}^{m} \in \mathbb{R}^{n \times n}$ has a unique block LU factorization if and only if the first $m - 1$ leading principal block submatrices of $A$ are nonsingular.

Proof. The proof is entirely analogous to the proof of Theorem 9.1. $\square$

This theorem makes clear that a block LU factorization may exist when an LU factorization does not.

If $A_{11} \in \mathbb{R}^{r \times r}$ is nonsingular we can write

$$
A = \left[ \begin{array}{l l} A _ {1 1} & A _ {1 2} \\ A _ {2 1} & A _ {2 2} \end{array} \right] = \left[ \begin{array}{c c} I & 0 \\ L _ {2 1} & I \end{array} \right] \left[ \begin{array}{c c} A _ {1 1} & A _ {1 2} \\ 0 & S \end{array} \right], \tag {13.2}
$$

which describes one block step of an outer-product-based algorithm for computing a block LU factorization. Here, $S$ is again the Schur complement of $A_{11}$ in $A$ . If the $(1,1)$ block of $S$ of appropriate dimension is nonsingular then we can factorize $S$ in a similar manner, and this process can be continued recursively to obtain the complete block LU factorization. The overall algorithm can be expressed as follows.

Algorithm 13.3 (block LU factorization). This algorithm computes a block LU factorization $A = LU \in \mathbb{R}^{n \times n}$ , using the notation (13.2).

1. $U_{11} = A_{11}$ $U_{12} = A_{12}$   
2. Solve $L_{21}A_{11} = A_{21}$ for $L_{21}$ .   
3. $S = A_{22} - L_{21}A_{12}$   
4. Compute the block LU factorization of $S$ , recursively.

Given a block LU factorization of $A$ , the solution to a system $Ax = b$ can be obtained by solving $Ly = b$ by forward substitution (since $L$ is triangular) and solving $Ux = y$ by block back substitution. There is freedom in how step 2 of Algorithm 13.3 is accomplished, and how the linear systems with coefficient matrices $U_{ii}$ that arise in the block back substitution are solved. The two main possibilities are as follows.

Implementation 1: $A_{11}$ is factorized by GEPP. Step 2 and the solution of linear systems with $U_{ii}$ are accomplished by substitution with the LU factors of $A_{11}$ .

Implementation 2: $A_{11}^{-1}$ is computed explicitly, so that step 2 becomes a matrix multiplication and $Ux = y$ is solved entirely by matrix-vector multiplications. This approach is attractive for parallel machines.

A particular case of partitioned LU factorization is recursively partitioned LU factorization. Assuming, for simplicity, that $n$ is even, we write

$$
\left[ \begin{array}{l l} A _ {1 1} & A _ {1 2} \\ A _ {2 1} & A _ {2 2} \end{array} \right] = \left[ \begin{array}{c c} L _ {1 1} & 0 \\ L _ {2 1} & I _ {n / 2} \end{array} \right] \left[ \begin{array}{c c} I _ {n / 2} & 0 \\ 0 & S \end{array} \right] \left[ \begin{array}{c c} U _ {1 1} & U _ {1 2} \\ 0 & I _ {n / 2} \end{array} \right], \tag {13.3}
$$

where each block is $n / 2 \times n / 2$ . The algorithm is as follows.

Algorithm 13.4 (recursively partitioned LU factorization). This algorithm computes an LU factorization $A = LU \in \mathbb{R}^{n \times n}$ using a recursive partitioning, using the notation (13.3).

1. Recursively factorize $\left[ \begin{array}{l}A_{11}\\ A_{21} \end{array} \right] = \left[ \begin{array}{l}L_{11}\\ L_{21} \end{array} \right]U_{11}$   
2. Solve $L_{11}U_{12} = A_{12}$ for $U_{12}$ .   
3. Form $S = A_{22} - L_{21}U_{12}$ .   
4. Recursively factorize $S = L_{22}U_{22}$ .

In contrast with Algorithm 13.1, this recursive algorithm does not require a block size to be chosen. Intuitively, the recursive algorithm maximizes the dimensions of the matrices that are multiplied in step 3: at the top level of the recursion two $n/2 \times n/2$ matrices are multiplied, at the next level two $n/4 \times n/4$ matrices, and so on. Toledo [1145, 1997] shows that Algorithm 13.4 transfers fewer words of data between primary and secondary computer memory than Algorithm 13.1 and shows that it outperforms Algorithm 13.1 on a range of computers. He also shows that the large matrix multiplications in Algorithm 13.4 enable it to benefit particularly well from the use of Strassen's fast matrix multiplication method (see §23.1).

What can be said about the numerical stability of partitioned and block LU factorization? Because the partitioned algorithms are just rearrangements of standard GE, the standard error analysis applies if the matrix operations are computed in the conventional way. However, if fast matrix multiplication techniques are used (for example, Strassen's method), the standard results are not applicable. Standard results are, in any case, not applicable to block LU factorization; its stability can be very different from that of LU factorization. Therefore we need error analysis for both partitioned and block LU factorization based on general assumptions that permit the use of fast matrix multiplication.

Unless otherwise stated, in this chapter an unsubscripted norm denotes $\| A \| \coloneqq \max_{i,j} |a_{ij}|$ . We make two assumptions about the underlying level-3 BLAS (matrix-matrix operations).

(1) If $A \in \mathbb{R}^{m \times n}$ and $B \in \mathbb{R}^{n \times p}$ then the computed approximation $\hat{C}$ to $C = AB$ satisfies

$$
\widehat {C} = A B + \Delta C, \quad \| \Delta C \| \leq c _ {1} (m, n, p) u \| A \| \| B \| + O \left(u ^ {2}\right), \tag {13.4}
$$

where $c_{1}(m,n,p)$ denotes a constant depending on $m, n,$ and $p$ .

(2) The computed solution $\widehat{X}$ to the triangular systems $TX = B$ , where $T \in \mathbb{R}^{m \times m}$ and $B \in \mathbb{R}^{m \times p}$ , satisfies

$$
T \widehat {X} = B + \Delta B, \quad \| \Delta B \| \leq c _ {2} (m, p) u \| T \| \| \widehat {X} \| + O \left(u ^ {2}\right). \tag {13.5}
$$

For conventional multiplication and substitution, conditions (13.4) and (13.5) hold with $c_{1}(m,n,p) = n^{2}$ and $c_{2}(m,p) = m^{2}$ . For implementations based on Strassen's method, (13.4) and (13.5) hold with $c_{1}$ and $c_{2}$ rather complicated functions of the dimensions $m$ , $n$ , $p$ , and the threshold $n_{0}$ that determines the level of recursion (see Theorem 23.2 and [592, 1990]).

# 13.2. Error Analysis of Partitioned LU Factorization

An error analysis for partitioned LU factorization must answer two questions. The first is whether partitioned LU factorization becomes unstable in some fundamental way when fast matrix multiplication is used. The second is whether the constants in (13.4) and (13.5) are propagated stably into the final error bound (exponential growth of the constants would be disastrous).

We will analyse Algorithm 13.1 and will assume that the block level LU factorization is done in such a way that the computed LU factors of $A_{11} \in \mathbb{R}^{r \times r}$ satisfy

$$
\widehat {L} _ {1 1} \widehat {U} _ {1 1} = A _ {1 1} + \Delta A _ {1 1}, \quad \| \Delta A _ {1 1} \| \leq c _ {3} (r) u \| \widehat {L} _ {1 1} \| \| \widehat {U} _ {1 1} \| + O \left(u ^ {2}\right). \tag {13.6}
$$

Theorem 13.5 (Demmel and Higham). Under the assumptions (13.4)-(13.6), the LU factors of $A \in \mathbb{R}^{n \times n}$ computed using the partitioned outer product form of LU factorization with block size $r$ satisfy $\widehat{L}\widehat{U} = A + \Delta A$ , where

$$
\left\| \Delta A \right\| \leq u (\delta (n, r) \| A \| + \theta (n, r) \| \widehat {L} \| \| \widehat {U} \|) + O \left(u ^ {2}\right), \tag {13.7}
$$

and where

$$
\begin{array}{l} \delta (n, r) = 1 + \delta (n - r, r), \quad \delta (r, r) = 0, \\ \theta (n, r) = \max  \left\{c _ {3} (r), c _ {2} (r, n - r), 1 + c _ {1} (n - r, r, n - r) + \delta (n - r, r) \right. \\ \left. + \theta (n - r, r) \right\}, \quad \theta (r, r) = c _ {3} (r). \\ \end{array}
$$

Proof. The proof is essentially inductive. To save clutter we will omit “ $+O(u^2)$ ” from each bound. For $n = r$ , the result holds trivially. Consider the first block stage of the factorization, with the partitioning (13.1). The assumptions imply that

$$
\begin{array}{l} \widehat {L} _ {1 1} \widehat {U} _ {1 2} = A _ {1 2} + \Delta A _ {1 2}, \quad \| \Delta A _ {1 2} \| \leq c _ {2} (r, n - r) u \| \widehat {L} _ {1 1} \| \| \widehat {U} _ {1 2} \|, (13.8) \\ \widehat {L} _ {2 1} \widehat {U} _ {1 1} = A _ {2 1} + \Delta A _ {2 1}, \quad \| \Delta A _ {2 1} \| \leq c _ {2} (r, n - r) u \| \widehat {L} _ {2 1} \| \| \widehat {U} _ {1 1} \|. (13.9) \\ \end{array}
$$

To obtain $S = A_{22} - L_{21}U_{12}$ we first compute $C = \widehat{L}_{21}\widehat{U}_{12}$ , obtaining

$$
\widehat {C} = \widehat {L} _ {2 1} \widehat {U} _ {1 2} + \varDelta C, \qquad \| \varDelta C \| \leq c _ {1} (n - r, r, n - r) u \| \widehat {L} _ {2 1} \| \| \widehat {U} _ {1 2} \|,
$$

and then subtract from $A_{22}$ , obtaining

$$
\widehat {S} = A _ {2 2} - \widehat {C} + F, \quad \| F \| \leq u \left(\| A _ {2 2} \| + \| \widehat {C} \|\right). \tag {13.10}
$$

It follows that

$$
\begin{array}{l} \widehat {S} = A _ {2 2} - \widehat {L} _ {2 1} \widehat {U} _ {1 2} + \Delta S, (13.11a) \\ \| \Delta S \| \leq u \left(\| A _ {2 2} \| + \| \widehat {L} _ {2 1} \| \| \widehat {U} _ {1 2} \| + c _ {1} (n - r, r, n - r) \| \widehat {L} _ {2 1} \| \| \widehat {U} _ {1 2} \|\right). (13.11b) \\ \end{array}
$$

The remainder of the algorithm consists of the computation of the LU factorization of $\widehat{S}$ , and by our inductive assumption (13.7), the computed LU factors satisfy

$$
\begin{array}{l} \widehat {L} _ {2 2} \widehat {U} _ {2 2} = \widehat {S} + \Delta \widehat {S}, (13.12a) \\ \| \Delta \widehat {S} \| \leq \delta (n - r, r) u \| \widehat {S} \| + \theta (n - r, r) u \| \widehat {L} _ {2 2} \| \| \widehat {U} _ {2 2} \|. (13.12b) \\ \end{array}
$$

Combining (13.11) and (13.12), and bounding $\| \widehat{S}\|$ using (13.10), we obtain

$$
\widehat {L} _ {2 1} \widehat {U} _ {1 2} + \widehat {L} _ {2 2} \widehat {U} _ {2 2} = A _ {2 2} + \Delta A _ {2 2},
$$

$$
\begin{array}{l} \| \Delta A _ {2 2} \| \leq u ([ 1 + \delta (n - r, r) ] \| A _ {2 2} \| + [ 1 + c _ {1} (n - r, r, n - r) + \delta (n - r, r) ] \\ \times \| \widehat {L} _ {2 1} \| \| \widehat {U} _ {1 2} \| + \theta (n - r, r) \| \widehat {L} _ {2 2} \| \| \widehat {U} _ {2 2} \|. \tag {13.13} \\ \end{array}
$$

Collecting (13.6), (13.8), (13.9), and (13.13) we have $\widehat{L}\widehat{U} = A + \Delta A$ , where bounds on $\| \Delta A_{ij} \|$ are given in the equations just mentioned. These bounds for the blocks of $\Delta A$ can be weakened slightly and expressed together in the more succinct form (13.7). $\square$

These recurrences for $\delta(n, r)$ and $\theta(n, r)$ show that the basic error constants in assumptions (13.4)-(13.6) combine additively at worst. Thus, the backward error analysis for the LU factorization is commensurate with the error analysis for the particular implementation of the BLAS3 employed in the partitioned factorization. In the case of the conventional BLAS3 we obtain a Wilkinson-style result for GE without pivoting, with $\theta(n, r) = O(n^3)$ (the growth factor is hidden in $\widehat{L}$ and $\widehat{U}$ ).

Although the above analysis is phrased in terms of the partitioned outer product form of LU factorization, the same result holds for other "ijk" partitioned forms (with slightly different constants), for example, the gaxpy or sdot forms and the recursive factorization (Algorithm 13.4). There is no difficulty in extending the analysis to cover partial pivoting and solution of $Ax = b$ using the computed LU factorization (see Problem 13.6).

# 13.3. Error Analysis of Block LU Factorization

Now we turn to block LU factorization. We assume that the computed matrices $\widehat{L}_{21}$ from step 2 of Algorithm 13.3 satisfy

$$
\widehat {L} _ {2 1} A _ {1 1} = A _ {2 1} + E _ {2 1}, \quad \| E _ {2 1} \| \leq c _ {4} (n, r) u \| \widehat {L} _ {2 1} \| \| A _ {1 1} \| + O \left(u ^ {2}\right). \tag {13.14}
$$

We also assume that when a system $U_{ii}x_i = d_i$ of order $r$ is solved, the computed solution $\widehat{x}_i$ satisfies

$$
\left(U _ {i i} + \Delta U _ {i i}\right) \widehat {x} _ {i} = d _ {i}, \quad \| \Delta U _ {i i} \| \leq c _ {5} (r) u \| U _ {i i} \| + O \left(u ^ {2}\right). \tag {13.15}
$$

The assumptions (13.14) and (13.15) are satisfied for Implementation 1 of Algorithm 13.3 and are sufficient to prove the following result.

Theorem 13.6 (Demmel, Higham, and Schreiber). Let $\widehat{L}$ and $\widehat{U}$ be the computed block LU factors of $A \in \mathbb{R}^{n \times n}$ from Algorithm 13.3 (with Implementation 1), and let $\widehat{x}$ be the computed solution to $Ax = b$ . Under the assumptions (13.4), (13.14), and (13.15),

$$
\begin{array}{l} \widehat {L} \widehat {U} = A + \Delta A _ {1}, \quad (A + \Delta A _ {2}) \widehat {x} = b, \\ \left\| \Delta A _ {i} \right\| \leq d _ {n} u \left(\left\| A \right\| + \left\| \widehat {L} \right\| \left\| \widehat {U} \right\|\right) + O \left(u ^ {2}\right), \quad i = 1: 2, \tag {13.16} \\ \end{array}
$$

where the constant $d_{n}$ is commensurate with those in the assumptions.

Proof. We omit the proof (see Demmel, Higham, and Schreiber [326, 1995] for details). It is similar to the proof of Theorem 13.5. $\square$

The bounds in Theorem 13.6 are valid also for other versions of block LU factorization obtained by "block loop reordering", such as a block gaxpy based algorithm.

Theorem 13.6 shows that the stability of block LU factorization is determined by the ratio $\| \widehat{L} \| \| \widehat{U} \| / \| A \|$ (numerical experiments show that the bounds are, in fact, reasonably sharp). If this ratio is bounded by a modest function of $n$ , then $\widehat{L}$ and $\widehat{U}$ are the true factors of a matrix close to $A$ , and $\widehat{x}$ solves a slightly perturbed system. However, $\| \widehat{L} \| \| \widehat{U} \|$ can exceed $\| A \|$ by an arbitrary factor, even if $A$ is symmetric positive definite or diagonally dominant by rows. Indeed, $\| L \| \geq \| L_{21} \| = \| A_{21} A_{11}^{-1} \|$ , using the partitioning (13.2), and this lower bound for $\| L \|$ can be arbitrarily large. In the following two subsections we investigate this instability more closely and show that $\| L \| \| U \|$ can be bounded in a useful way for particular classes of $A$ . Without further comment we make the reasonable assumption that $\| L \| \| U \| \approx \| \widehat{L} \| \| \widehat{U} \|$ , so that these bounds may be used in Theorem 13.6.

What can be said for Implementation 2? Suppose, for simplicity, that the inverses $A_{11}^{-1}$ (which are used in step 2 of Algorithm 13.3 and in the block back substitution) are computed exactly. Then the best bounds of the forms (13.14) and (13.15) are

$$
\begin{array}{l} \widehat {L} _ {2 1} A _ {1 1} = A _ {2 1} + \Delta A _ {2 1}, \quad \| \Delta A _ {2 1} \| \leq c _ {4} (n, r) u \kappa \left(A _ {1 1}\right) \| A _ {2 1} \| + O \left(u ^ {2}\right), \\ \left(U _ {i i} + \Delta U _ {i i}\right) \widehat {x} _ {i} = d _ {i}, \quad \| \Delta U _ {i i} \| \leq c _ {5} (r) u \kappa \left(U _ {i i}\right) \| U _ {i i} \| + O \left(u ^ {2}\right). \\ \end{array}
$$

Working from these results, we find that Theorem 13.6 still holds provided the first-order terms in the bounds in (13.16) are multiplied by $\max_i\kappa (\widehat{U}_{ii})$ . This suggests that Implementation 2 of Algorithm 13.3 can be much less stable than Implementation 1 when the diagonal blocks of $U$ are ill conditioned, and this is confirmed by numerical experiments.

# 13.3.1. Block Diagonal Dominance

One class of matrices for which block LU factorization has long been known to be stable is block tridiagonal matrices that are diagonally dominant in an appropriate block sense. A general matrix $A \in \mathbb{R}^{n \times n}$ is block diagonally dominant by columns with respect to a given partitioning $A = (A_{ij})$ and a given norm if, for all $j$ ,

$$
\left\| A _ {j j} ^ {- 1} \right\| ^ {- 1} - \sum_ {i \neq j} \| A _ {i j} \| =: \gamma_ {j} \geq 0. \tag {13.17}
$$

This definition implicitly requires that the diagonal blocks $A_{jj}$ are all nonsingular. $A$ is block diagonally dominant by rows if $A^T$ is block diagonally dominant by columns. For the block size 1, the usual property of point diagonal dominance is obtained. Note that for the 1- and $\infty$ -norms diagonal dominance does not imply block diagonal dominance, nor does the reverse implication hold (see Problem 13.2). Throughout our analysis of block diagonal dominance we take the norm to be an arbitrary subordinate matrix norm.

First, we show that for block diagonally dominant matrices a block LU factorization exists, using the key property that block diagonal dominance is inherited by the Schur complements obtained in the course of the factorization. In the analysis we assume that $A$ has $m$ block rows and columns.

Theorem 13.7 (Demmel, Higham, and Schreiber). Suppose $A \in \mathbb{R}^{n \times n}$ is nonsingular and block diagonally dominant by rows or columns with respect to a subordinate matrix norm in (13.17). Then $A$ has a block LU factorization, and all the Schur complements arising in Algorithm 13.3 have the same kind of diagonal dominance as $A$ .

Proof. This proof is a generalization of Wilkinson's proof of the corresponding result for point diagonally dominant matrices [1229, 1961, pp. 288-289], [509, 1996, Thm. 3.4.3] (as is the proof of Theorem 13.8 below). We consider the case of block diagonal dominance by columns; the proof for row-wise diagonal dominance is analogous.

The first step of Algorithm 13.3 succeeds, since $A_{11}$ is nonsingular, producing a matrix that we can write as

$$
A ^ {(2)} = \left[ \begin{array}{c c} U _ {1 1} & U _ {1 2} \\ 0 & S \end{array} \right].
$$

For $j = 2$ : $m$ we have

$$
\begin{array}{l} \sum_{\substack{i = 2\\ i\neq j}}^{m}\| A_{ij}^{(2)}\| = \sum_{\substack{i = 2\\ i\neq j}}^{m}\| A_{ij} - A_{i1}A_{11}^{-1}A_{1j}\| \\ \leq \sum_{\substack{i = 2\\ i\neq j}}^{m}\| A_{ij}\| +\| A_{1j}\| \| A_{11}^{-1}\| \sum_{\substack{i = 2\\ i\neq j}}^{m}\| A_{i1}\| \\ \leq \sum_{\substack{i = 2\\ i\neq j}}^{m}\| A_{ij}\| +\| A_{1j}\| \| A_{11}^{-1}\| \big(\| A_{11}^{-1}\|^{-1} - \| A_{j1}\| \big),\quad \text{using (13.17)}, \\ = \sum_{\substack{i = 2\\ i\neq j}}^{m}\| A_{ij}\| +\| A_{1j}\| -\| A_{1j}\| \| A_{11}^{-1}\| \| A_{j1}\| \\ \leq \left\| A _ {j j} ^ {- 1} \right\| ^ {- 1} - \left\| A _ {1 j} \right\| \left\| A _ {1 1} ^ {- 1} \right\| \left\| A _ {j 1} \right\|, \quad \text {u s i n g (1 3 . 1 7)}, \\ = \min  _ {\| x \| = 1} \| A _ {j j} x \| - \| A _ {1 j} \| \| A _ {1 1} ^ {- 1} \| \| A _ {j 1} \| \\ \leq \min  _ {\| x \| = 1} \| \left(A _ {j j} - A _ {j 1} A _ {1 1} ^ {- 1} A _ {1 j}\right) x \| \\ = \min  _ {\| x \| = 1} \| A _ {j j} ^ {(2)} x \|. \tag {13.18} \\ \end{array}
$$

Now if $A_{jj}^{(2)}$ is singular it follows that $\sum_{i=2, i \neq j}^{m} \|A_{ij}^{(2)}\| = 0$ ; therefore $A^{(2)}$ , and hence also $A$ , is singular, which is a contradiction. Thus $A_{jj}^{(2)}$ is nonsingular, and

(13.18) can be rewritten

$$
\sum_{\substack{i = 2\\ i\neq j}}^{m}\| A_{ij}^{(2)}\| \leq \| A_{jj}^{(2)^{-1}}\|^{-1},
$$

showing that $A^{(2)}$ is block diagonally dominant by columns. The result follows by induction.

The next result allows us to bound $\| U\|$ for a block diagonally dominant matrix.

Theorem 13.8 (Demmel, Higham, and Schreiber). Let $A$ satisfy the conditions of Theorem 13.7. If $A^{(k)}$ denotes the matrix obtained after $k - 1$ steps of Algorithm 13.3, then

$$
\max _ {k \leq i, j \leq m} \| A _ {i j} ^ {(k)} \| \leq 2 \max _ {1 \leq i, j \leq m} \| A _ {i j} \|.
$$

Proof. Let $A$ be block diagonally dominant by columns (the proof for row diagonal dominance is similar). Then

$$
\begin{array}{l} \sum_ {i = 2} ^ {m} \left\| A _ {i j} ^ {(2)} \right\| = \sum_ {i = 2} ^ {m} \left\| A _ {i j} - A _ {i 1} A _ {1 1} ^ {- 1} A _ {1 j} \right\| \\ \leq \sum_ {i = 2} ^ {m} \| A _ {i j} \| + \| A _ {1 j} \| \| A _ {1 1} ^ {- 1} \| \sum_ {i = 2} ^ {m} \| A _ {i 1} \| \\ \leq \sum_ {i = 1} ^ {m} \| A _ {i j} \|, \\ \end{array}
$$

using (13.17). By induction, using Theorem 13.7, it follows that $\sum_{i=k}^{m}\|A_{ij}^{(k)}\| \leq \sum_{i=1}^{m}\|A_{ij}\|$ . This yields

$$
\max  _ {k \leq i, j \leq m} \| A _ {i j} ^ {(k)} \| \leq \max  _ {k \leq j \leq m} \sum_ {i = k} ^ {m} \| A _ {i j} ^ {(k)} \| \leq \max  _ {k \leq j \leq m} \sum_ {i = 1} ^ {m} \| A _ {i j} \|.
$$

From (13.17), $\sum_{i\neq j}\| A_{ij}\| \leq \| A_{jj}^{-1}\|^{-1}\leq \| A_{jj}\|$ , so

$$
\max  _ {k \leq i, j \leq m} \| A _ {i j} ^ {(k)} \| \leq 2 \max  _ {k \leq j \leq m} \| A _ {j j} \| \leq 2 \max  _ {1 \leq j \leq m} \| A _ {j j} \| = 2 \max  _ {1 \leq i, j \leq m} \| A _ {i j} \|.
$$

The implications of Theorems 13.7 and 13.8 for stability are as follows. Suppose $A$ is block diagonally dominant by columns. Also, assume for the moment that the (subordinate) norm has the property that

$$
\max  _ {i, j} \| A _ {i j} \| \leq \| A \| \leq \sum_ {i, j} \| A _ {i j} \|, \tag {13.19}
$$

which holds for any $p$ -norm, for example. The subdiagonal blocks in the first block column of $L$ are given by $L_{i1} = A_{i1}A_{11}^{-1}$ and so $\| [L_{21}^T,\dots ,L_{m1}^T ]^T\| \leq 1$ , by (13.17) and (13.19). From Theorem 13.7 it follows that $\| [L_{j + 1,j}^T,\dots ,L_{mj}^T ]^T\| \leq 1$

for $j = 2$ : $m$ . Since $U_{ij} = A_{ij}^{(i)}$ for $j \geq i$ , Theorem 13.8 shows that $\| U_{ij} \| \leq 2 \| A \|$ for each block of $U$ (and $\| U_{ii} \| \leq \| A \|$ ). Therefore $\| L \| \leq m$ and $\| U \| \leq m^2 \| A \|$ and so $\| L \| \| U \| \leq m^3 \| A \|$ . For particular norms the bounds on the blocks of $L$ and $U$ yield a smaller bound for $\| L \|$ and $\| U \|$ . For example, for the 1-norm we have $\| L \|_1 \| U \|_1 \leq 2m \| A \|_1$ and for the $\infty$ -norm $\| L \|_\infty \| U \|_\infty \leq 2m^2 \| A \|_\infty$ . We conclude that block LU factorization is stable if $A$ is block diagonally dominant by columns with respect to any subordinate matrix norm satisfying (13.19).

Unfortunately, block LU factorization can be unstable when $A$ is block diagonally dominant by rows, for although Theorem 13.8 guarantees that $\| U_{ij} \| \leq 2 \| A \|$ , $\| L \|$ can be arbitrarily large. This can be seen from the example

$$
A = \left[ \begin{array}{c c} A _ {1 1} & 0 \\ \frac {1}{2} I & I \end{array} \right] = \left[ \begin{array}{c c} I & 0 \\ \frac {1}{2} A _ {1 1} ^ {- 1} & I \end{array} \right] \left[ \begin{array}{c c} A _ {1 1} & 0 \\ 0 & I \end{array} \right] = L U,
$$

where $A$ is block diagonally dominant by rows in any subordinate norm for any nonsingular matrix $A_{11}$ . It is easy to confirm numerically that block LU factorization can be unstable on matrices of this form.

Next, we bound $\| L\| \| U\|$ for a general matrix and then specialize to point diagonal dominance. From this point on we use the norm $\| A\| \coloneqq \max_{i,j}|a_{ij}|$ . We partition $A$ according to

$$
A = \left[ \begin{array}{l l} A _ {1 1} & A _ {1 2} \\ A _ {2 1} & A _ {2 2} \end{array} \right], \quad A _ {1 1} \in \mathbb {R} ^ {r \times r}, \tag {13.20}
$$

and denote by $\rho_{n}$ the growth factor for GE without pivoting. We assume that GE applied to $A$ succeeds.

To bound $\| L\|$ , we note that, under the partitioning (13.20), for the first block stage of Algorithm 13.3 we have $\| L_{21}\| = \| A_{21}A_{11}^{-1}\| \leq n\rho_n\kappa (A)$ (see Problem 13.4). Since the algorithm works recursively with the Schur complement $S$ , and since every Schur complement satisfies $\kappa (S)\leq \rho_n\kappa (A)$ (see Problem 13.4), each subsequently computed subdiagonal block of $L$ has norm at most $n\rho_n^2\kappa (A)$ . Since $U$ is composed of elements of $A$ together with elements of Schur complements of $A$ ,

$$
\| U \| \leq \rho_ {n} \| A \|. \tag {13.21}
$$

Overall, then, for a general matrix $A \in \mathbb{R}^{n \times n}$ ,

$$
\| L \| \| U \| \leq n \rho_ {n} ^ {2} \kappa (A) \cdot \rho_ {n} \| A \| = n \rho_ {n} ^ {3} \kappa (A) \| A \|. \tag {13.22}
$$

Thus, block LU factorization is stable for a general matrix $A$ as long as GE is stable for $A$ (that is, $\rho_{n}$ is of order 1) and $A$ is well conditioned.

If $A$ is point diagonally dominant by columns then, since every Schur complement enjoys the same property, we have $\| L_{ij} \| \leq 1$ for $i > j$ , by Problem 13.5. Hence $\| L \| = 1$ . Furthermore, $\rho_n \leq 2$ (Theorem 9.9 or Theorem 13.8), giving $\| U \| \leq 2 \| A \|$ by (13.21), and so

$$
\| L \| \| U \| \leq 2 \| A \|.
$$

Thus block LU factorization is perfectly stable for a matrix point diagonally dominant by columns.

If $A$ is point diagonally dominant by rows then the best we can do is to take $\rho_n \leq 2$ in (13.22), obtaining

$$
\| L \| \| U \| \leq 8 n \kappa (A) \| A \|. \tag {13.23}
$$

Hence for point row diagonally dominant matrices, stability is guaranteed if $A$ is well conditioned. This in turn is guaranteed if the row diagonal dominance amounts $\gamma_{j}$ in the analogue of (13.17) for point row diagonal dominance are sufficiently large relative to $\| A\|$ , because $\| A^{-1}\|_{\infty} \leq (\min_j\gamma_j)^{-1}$ (see Problem 8.7(a)).

# 13.3.2. Symmetric Positive Definite Matrices

Further useful results about the stability of block LU factorization can be derived for symmetric positive definite matrices. First, note that the existence of a block LU factorization is immediate for such matrices, since all their leading principal submatrices are nonsingular. Let $A$ be a symmetric positive definite matrix, partitioned as

$$
A = \left[ \begin{array}{c c} A _ {1 1} & A _ {2 1} ^ {T} \\ A _ {2 1} & A _ {2 2} \end{array} \right], \qquad A _ {1 1} \in \mathbb {R} ^ {r \times r}.
$$

The definiteness implies certain relations among the submatrices $A_{ij}$ that can be used to obtain a stronger bound for $\| L\| _2$ than can be deduced for a general matrix (cf. Problem 13.4).

Lemma 13.9. If $A$ is symmetric positive definite then $\| A_{21}A_{11}^{-1}\|_2 \leq \kappa_2(A)^{1/2}$ .

Proof. This lemma is a corollary of Lemma 10.12, but we give a separate proof. Let $A$ have the Cholesky factorization

$$
A = \left[ \begin{array}{c c} R _ {1 1} ^ {T} & 0 \\ R _ {1 2} ^ {T} & R _ {2 2} ^ {T} \end{array} \right] \left[ \begin{array}{c c} R _ {1 1} & R _ {1 2} \\ 0 & R _ {2 2} \end{array} \right], \qquad R _ {1 1} \in \mathbb {R} ^ {r \times r}.
$$

Then $A_{21}A_{11}^{-1} = R_{12}^{T}R_{11}\cdot R_{11}^{-1}R_{11}^{-T} = R_{12}^{T}R_{11}^{-T}$ , so

$$
\left\| A _ {2 1} A _ {1 1} ^ {- 1} \right\| _ {2} \leq \left\| R _ {1 2} \right\| _ {2} \left\| R _ {1 1} ^ {- 1} \right\| _ {2} \leq \left\| R \right\| _ {2} \left\| R ^ {- 1} \right\| _ {2} = \kappa_ {2} (R) = \kappa_ {2} (A) ^ {1 / 2}.
$$

The following lemma is proved in a way similar to the second inequality in Problem 13.4.

Lemma 13.10. If $A$ is symmetric positive definite then the Schur complement $S = A_{22} - A_{21}A_{11}^{-1}A_{21}^{T}$ satisfies $\kappa_2(S) \leq \kappa_2(A)$ .

Using the same reasoning as in the last subsection, we deduce from these two lemmas that each subdiagonal block of $L$ is bounded in 2-norm by $\kappa_2(A)^{1/2}$ . Therefore $\| L \|_2 \leq 1 + m \kappa_2(A)^{1/2}$ , where there are $m$ block stages in the algorithm. Also, it can be shown that $\| U \|_2 \leq \sqrt{m} \| A \|_2$ . Hence

$$
\left\| L \| _ {2} \| U \| _ {2} \leq \sqrt {m} \left(1 + m \kappa_ {2} (A) ^ {1 / 2}\right) \| A \| _ {2}. \right. \tag {13.24}
$$

Table 13.1. Stability of block and point LU factorization. $\rho_{n}$ is the growth factor for GE without pivoting.   

<table><tr><td>Matrix property</td><td>Block LU</td><td>Point LU</td></tr><tr><td>Symmetric positive definite</td><td>κ(A)1/2</td><td>1</td></tr><tr><td>Block column diagonally dominant</td><td>1</td><td>ρn</td></tr><tr><td>Point column diagonally dominant</td><td>1</td><td>1</td></tr><tr><td>Block row diagonally dominant</td><td>ρn3κ(A)</td><td>ρn</td></tr><tr><td>Point row diagonally dominant</td><td>κ(A)</td><td>1</td></tr><tr><td>Arbitrary</td><td>ρn3κ(A)</td><td>ρn</td></tr></table>

It follows from Theorem 13.6 that when Algorithm 13.3 is applied to a symmetric positive definite matrix $A$ , the backward errors for the LU factorization and the subsequent solution of a linear system are both bounded by

$$
c _ {n} \sqrt {m} u \| A \| _ {2} \left(2 + m \kappa_ {2} (A) ^ {1 / 2}\right) + O \left(u ^ {2}\right). \tag {13.25}
$$

Any resulting bound for $\| x - \widehat{x} \|_2 / \| x \|_2$ will be proportional to $\kappa_2(A)^{3/2}$ , rather than $\kappa_2(A)$ as for a stable method. This suggests that block LU factorization can lose up to 50% more digits of accuracy in $x$ than a stable method for solving symmetric positive definite linear systems. The positive conclusion to be drawn, however, is that block LU factorization is guaranteed to be stable for a symmetric positive definite matrix that is well conditioned.

The stability results for block LU factorization are summarized in Table 13.1, which tabulates a bound for $\| A - \widehat{L}\widehat{U}\| /(c_nu\| A\|)$ for block and point LU factorization for the matrix properties considered in this chapter. The constant $c_{n}$ incorporates any constants in the bound that depend polynomially on the dimension, so a value of 1 in the table indicates unconditional stability.

# 13.4. Notes and References

The distinction between a partitioned algorithm and a block algorithm is rarely made in the literature (exceptions include the papers by Schreiber [1021, 1988] and Demmel, Higham, and Schreiber [326, 1995]); the term "block algorithm" is frequently used to describe both types of algorithm. A partitioned algorithm might also be called a "blocked algorithm" (as is done by Dongarra, Duff, Sorensen, and van der Vorst [349, 1998]), but the similarity of this term to "block algorithm" can cause confusion and so we do not recommend this terminology. Note that in the particular case of matrix multiplication, partitioned and block algorithms are equivalent. Our treatment of partitioned LU factorization has focused on the stability aspects; for further details, particularly concerning implementation on high-performance computers, see Dongarra, Duff, Sorensen, and van der Vorst [349, 1998] and Golub and Van Loan [509, 1996].

Recursive LU factorization is now regarded as the most efficient way in which to implement LU factorization on machines with hierarchical memories [535, 1997], [1145, 1997], but it has not yet been incorporated into LAPACK.

Block LU factorization appears to have first been proposed for block tridiagonal matrices, which frequently arise in the discretization of partial differential equations. References relevant to this application include Isaacson and Keller [667, 1966, p. 59], Varah [1187, 1972], Bank and Rose [62, 1977], Mattheij [827, 1984], [828, 1984], and Concus, Golub, and Meurant [262, 1985].

For an application of block LU factorization to linear programming, see Eldersveld and Saunders [388, 1992].

Theorem 13.5 is from Demmel and Higham [324, 1992]. The results in §13.3 are from Demmel, Higham, and Schreiber [326, 1995], which extends earlier analysis of block LU factorization by Demmel and Higham [324, 1992].

Block diagonal dominance was introduced by Feingold and Varga [406, 1962], and has been used mainly in generalizations of the Gershgorin circle theorem. Varah [1187, 1972] obtained bounds on $\| L\|$ and $\| U\|$ for block diagonally dominant block tridiagonal matrices; see Problem 13.1.

Theorem 13.7 is obtained in the case of block diagonal dominance by rows with $\min_j\gamma_j > 0$ by Polman [946, 1987]; the proof in [946, 1987] makes use of the corresponding result for point diagonal dominance and thus differs from the proof we have given.

At the cost of a much more difficult proof, Lemma 13.9 can be strengthened to the attainable bound $\| A_{21}A_{11}^{-1}\|_2 \leq (\kappa_2(A)^{1/2} - \kappa_2(A)^{-1/2}) / 2$ , as shown by Demmel [307, 1983, Thm. 4], but the weaker bound is sufficient for our purposes.

# 13.4.1. LAPACK

LAPACK does not implement block LU factorization, but its LU factorization (and related) routines for full matrices employ partitioned LU factorization in order to exploit the level-3 BLAS and thereby to be efficient on high-performance machines.

# Problems

13.1. (Varah [1187, 1972]) Suppose $A$ is block tridiagonal and has the block LU factorization $A = LU$ (so that $L$ and $U$ are block bidiagonal and $U_{i,i+1} = A_{i,i+1}$ ). Show that if $A$ is block diagonally dominant by columns then

$$
\left\| L _ {i, i - 1} \right\| \leq 1, \quad \left\| U _ {i i} \right\| \leq \left\| A _ {i i} \right\| + \left\| A _ {i - 1, i} \right\|,
$$

while if $A$ is block diagonally dominant by rows then

$$
\left\| L _ {i, i - 1} \right\| \leq \left\| A _ {i, i - 1} \right\| / \left\| A _ {i - 1, i} \right\|, \quad \left\| U _ {i i} \right\| \leq \left\| A _ {i i} \right\| + \left\| A _ {i, i - 1} \right\|.
$$

What can be deduced about the stability of the factorization for these two classes of matrices?

13.2. Show that for the 1- and $\infty$ -norms diagonal dominance does not imply block diagonal dominance, and vice versa.

13.3. If $A \in \mathbb{R}^{n \times n}$ is symmetric, has positive diagonal elements, and is block diagonally dominant by rows, must it be positive definite?

13.4. Let $A \in \mathbb{R}^{n \times n}$ be partitioned

$$
A = \left[ \begin{array}{c c} A _ {1 1} & A _ {1 2} \\ A _ {2 1} & A _ {2 2} \end{array} \right], \quad A _ {1 1} \in \mathbb {R} ^ {r \times r}, \tag {13.26}
$$

with $A_{11}$ nonsingular. Let $\| A\| \coloneqq \max_{ij}|a_{ij}|$ . Show that $\| A_{21}A_{11}^{-1}\| \leq n\rho_n\kappa (A)$ , where $\rho_{n}$ is the growth factor for GE without pivoting on $A$ . Show that the Schur complement $S = A_{22} - A_{21}A_{11}^{-1}A_{12}$ satisfies $\kappa (S)\leq \rho_n\kappa (A)$ .

13.5. Let $A \in \mathbb{R}^{n \times n}$ be partitioned as in (13.26), with $A_{11}$ nonsingular, and suppose that $A$ is point diagonally dominant by columns. Show that $\| A_{21}A_{11}^{-1}\|_1 \leq 1$ .

13.6. Show that under the conditions of Theorem 13.5 the computed solution to $Ax = b$ satisfies

$$
(A + \varDelta A) \widehat {\boldsymbol {x}} = b, \qquad \| \varDelta A \| \leq c _ {n} u \big (\| A \| + \| \widehat {L} \| \| \widehat {U} \| \big) + O (u ^ {2}),
$$

and the computed solution to the multiple right-hand side system $AX = B$ (where (13.5) is assumed to hold for the multiple right-hand side triangular solves) satisfies

$$
\left\| A \widehat {X} - B \right\| \leq c _ {n} u \big (\left\| A \right\| + \left\| \widehat {L} \right\| \left\| \widehat {U} \right\| \big) \left\| \widehat {X} \right\| + O (u ^ {2}).
$$

In both cases, $c_{n}$ is a constant depending on $n$ and the block size.

13.7. Let $X = \left[ \begin{array}{cc}A & B\\ CD \end{array} \right] \in \mathbb{R}^{n\times n}$ , where $A$ is square and nonsingular. Show that

$$
\det  (X) = \det  (A) \det  (D - C A ^ {- 1} B).
$$

Assuming $A, B, C, D$ are all $m \times m$ , give a condition under which $\det(X) = \det(AD - CB)$ .

13.8. By using a block LU factorization show that

$$
\left[ \begin{array}{c c} A & B \\ C & D \end{array} \right] ^ {- 1} = \left[ \begin{array}{c c} A ^ {- 1} + A ^ {- 1} B S ^ {- 1} C A ^ {- 1} & - A ^ {- 1} B S ^ {- 1} \\ - S ^ {- 1} C A ^ {- 1} & S ^ {- 1} \end{array} \right],
$$

where $A$ is assumed to be nonsingular and $S = D - CA^{-1}B$ .

13.9. Let $A \in \mathbb{R}^{n \times m}$ , $B \in \mathbb{R}^{m \times n}$ . Derive the expression

$$
(I - A B) ^ {- 1} = I + A (I - B A) ^ {- 1} B
$$

by considering block LU and block UL factorizations of $\left[ \begin{array}{cc}I & A\\ B & I \end{array} \right]$ . Deduce the Sherman-Morrison-Woodbury formula

$$
\left(T - U W ^ {- 1} V ^ {T}\right) ^ {- 1} = T ^ {- 1} + T ^ {- 1} U \left(W - V ^ {T} T ^ {- 1} U\right) ^ {- 1} V ^ {T} T ^ {- 1},
$$

where $T\in \mathbb{R}^{n\times n}$ $U\in \mathbb{R}^{n\times r}$ $W\in \mathbb{R}^{r\times r}$ $V\in \mathbb{R}^{r\times n}$
