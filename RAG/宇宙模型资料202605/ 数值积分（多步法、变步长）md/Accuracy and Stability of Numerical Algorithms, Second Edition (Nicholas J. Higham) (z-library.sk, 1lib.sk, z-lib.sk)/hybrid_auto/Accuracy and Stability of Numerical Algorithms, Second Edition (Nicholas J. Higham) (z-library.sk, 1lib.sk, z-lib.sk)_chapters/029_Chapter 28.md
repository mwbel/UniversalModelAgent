# Chapter 28

# A Gallery of Test Matrices

Many tricks or treats associated with the Hilbert matrix may seem rather frightening or fascinating.

— MAN-DUEN CHOI, Tricks or Treats with the Hilbert Matrix (1983)

I start by looking at a 2 by 2 matrix.

Sometimes I look at a 4 by 4 matrix.

That's when things get out of control and too hard.

Usually 2 by 2 or 3 by 3 is enough, and I look at them, and I compute with them, and I try to guess the facts.

First, think of a question.

Second, I look at examples, and then third,

guess the facts.

— PAUL R. HALMOS $^{23}$ (1991)

When people look down on matrices,

remind them of great mathematicians such as

Frobenius, Schur, C. L. Siegel, Ostrowski, Motzkin, Kac, etc.,

who made important contributions to the subject.

— OLGA TAUSSKY, How I Became a Torchbearer for Matrix Theory (1988)

Ever since the first computer programs for matrix computations were written in the 1940s, researchers have been devising matrices suitable for test purposes and investigating the properties of these matrices. In the 1950s and 1960s it was common for a whole paper to be devoted to a particular test matrix: typically its inverse or eigenvalues would be obtained in closed form.

Early collections of test matrices include those of Newman and Todd [891, 1958] and Rutishauser [1006, 1968]; most of Rutishauser's matrices come from continued fractions or moment problems. Two well-known books present collections of test matrices. Gregory and Karney [524, 1969] deal exclusively with the topic, while Westlake [1217, 1968] gives an appendix of test matrices.

In this chapter we present a gallery of matrices. We describe their properties and explain why they are useful (or not so useful, as the case may be) for test purposes. The coverage is limited, and all the matrices we consider are available in MATLAB. A comprehensive, well-documented collection of parametrized test matrices is contained in MATLAB's gallery function (see help gallery), and MATLAB has several other special matrices that can be used for test purposes (see help elmat).

In addition to the matrices discussed in this chapter, interesting matrices discussed elsewhere in this book include magic squares (Problem 6.4), the Kahan matrix (equation (8.11)), Hadamard matrices (§9.4), and Vandermonde matrices (Chapter 22).

Table 28.1 lists MATLAB functions that can be used to generate many of the test matrices considered in this book.

The matrices described here can be modified in various ways while still preserving some or all of their interesting properties. Among the many ways of constructing new test matrices from old are

- similarity transformations $A \gets X^{-1}AX$ ,   
unitary transformations $A\gets UAV$ , where $U^{*}U = V^{*}V = I$   
- Kronecker products $A \gets A \otimes B$ or $B \otimes A$ (for which MATLAB has a function kron),   
powers $A\gets A^k$

# 28.1. The Hilbert and Cauchy Matrices

The Hilbert matrix $H_{n} \in \mathbb{R}^{n \times n}$ , with elements $h_{ij} = 1 / (i + j - 1)$ , is perhaps the most famous of all test matrices. It was widely used in the 1950s and 1960s for testing inversion algorithms and linear equation solvers. Its attractions were threefold: it is very ill conditioned for even moderate values of $n$ , formulae are known for the elements of the inverse, and the matrix arises in a practical problem: least squares fitting by a polynomial expressed in the monomial basis.

Despite its past popularity and notoriety, the Hilbert matrix is not a good test matrix. It is too special. Not only is it symmetric positive definite, but it is totally positive. This means, for example, that Gaussian elimination without pivoting is guaranteed to produce a small componentwise relative backward error (as is

Table 28.1. MATLAB functions for generating matrices discussed in this book.   

<table><tr><td>compan</td><td>Companion matrix</td></tr><tr><td>frank</td><td>Frank matrix—ill-conditioned eigenvalues</td></tr><tr><td>gallery</td><td>Large collection of test matrices</td></tr><tr><td>gallery(&#x27;chebspec&#x27;,...)</td><td>Chebyshev spectral differentiation matrix</td></tr><tr><td>gallery(&#x27;clement&#x27;,...)</td><td>Clement matrix—tridiagonal with zero diagonal entries</td></tr><tr><td>gallery(&#x27;kahan&#x27;,...)</td><td>Kahan matrix—upper trapezoidal</td></tr><tr><td>gallery(&#x27;orthog&#x27;,...)</td><td>Orthogonal and nearly orthogonal matrices</td></tr><tr><td>gallery(&#x27;pei&#x27;,...)</td><td>Pei matrix</td></tr><tr><td>gallery(&#x27;randsvd&#x27;,...)</td><td>Random matrix with preassigned singular values and specified bandwidth</td></tr><tr><td>gallery(&#x27;toeppen&#x27;,...)</td><td>Pentadiagonal Toeplitz matrix</td></tr><tr><td>gallery(&#x27;tridiag&#x27;,...)</td><td>Tridiagonal matrix</td></tr><tr><td>hadamard</td><td>Hadamard matrix</td></tr><tr><td>hilb</td><td>Hilbert matrix</td></tr><tr><td>invhilb</td><td>Inverse Hilbert matrix</td></tr><tr><td>magic</td><td>Magic square</td></tr><tr><td>pascal</td><td>Pascal matrix</td></tr><tr><td>rand</td><td>Matrix of uniformly distributed random numbers</td></tr><tr><td>randn</td><td>Matrix of normally distributed random numbers</td></tr><tr><td>toeplitz</td><td>Toeplitz matrix</td></tr><tr><td>vander</td><td>Vandermonde matrix</td></tr></table>

Cholesky factorization). Thus the Hilbert matrix is not a typical ill-conditioned matrix.

The $(i,j)$ element of the inverse of the Hilbert matrix $H_{n}$ is the integer

$$
(- 1) ^ {i + j} (i + j - 1) \binom {n + i - 1} {n - j} \binom {n + j - 1} {n - i} \binom {i + j - 2} {i - 1} ^ {2}, \tag {28.1}
$$

and

$$
\det  \left(H _ {n}\right) = \frac {\left(1 ! 2 ! \dots (n - 1)!\right) ^ {4}}{\left(1 ! 2 ! \dots (2 n - 1)!\right)} \sim 2 ^ {- 2 n ^ {2}}. \tag {28.2}
$$

There are many ways to rewrite the formula (28.1). These formulae are best obtained as special cases of those for the Cauchy matrix below.

The Cholesky factor $R_{n}$ of the inverse of the Hilbert matrix is known explicitly, as is $R_{n}^{-1}$ :

$$
r _ {i j} = \frac {\sqrt {2 i - 1} [ (j - 1) ! ] ^ {2}}{(i + j - 1) ! (j - i) !}, \quad j \geq i, \tag {28.3}
$$

$$
(R _ {n} ^ {- 1}) _ {i j} = (- 1) ^ {i + j} \sqrt {2 j - 1} \binom {i + j - 2} {i - 1} \binom {j - 1} {i - 1}, \qquad j \geq i. \qquad (2 8. 4)
$$

One interesting application of these formulae is to compute the eigenvalues of $H_{n}$ as the squares of the singular values of $R_{n}$ ; if $R_{n}$ is evaluated from (28.3) and

Table 28.2. Condition numbers of Hilbert and Pascal matrices.   

<table><tr><td>n</td><td>κ2(Hn)</td><td>κ2(Pn)</td></tr><tr><td>2</td><td>1.9281e1</td><td>6.8541e0</td></tr><tr><td>3</td><td>5.2406e2</td><td>6.1984e1</td></tr><tr><td>4</td><td>1.5514e4</td><td>6.9194e2</td></tr><tr><td>5</td><td>4.7661e5</td><td>8.5175e3</td></tr><tr><td>6</td><td>1.4951e7</td><td>1.1079e5</td></tr><tr><td>7</td><td>4.7537e8</td><td>1.4934e6</td></tr><tr><td>8</td><td>1.5258e10</td><td>2.0645e7</td></tr><tr><td>9</td><td>4.9315e11</td><td>2.9078e8</td></tr><tr><td>10</td><td>1.6026e13</td><td>4.1552e9</td></tr><tr><td>11</td><td>5.2307e14</td><td>6.0064e10</td></tr><tr><td>12</td><td>1.7132e16</td><td>8.7639e11</td></tr><tr><td>13</td><td>5.6279e17</td><td>1.2888e13</td></tr><tr><td>14</td><td>1.8534e19</td><td>1.9076e14</td></tr><tr><td>15</td><td>6.1166e20</td><td>2.8396e15</td></tr><tr><td>16</td><td>2.0223e22</td><td>4.2476e16</td></tr></table>

the one-sided Jacobi algorithm is used to compute the singular values then high relative accuracy is obtained for every eigenvalue, as shown by Mathias [821, 1995].

The condition number of the Hilbert matrix grows at an exponential rate: $\kappa_{2}(H_{n})\sim \exp (3.5n)$ [1141, 1954]. See Table 28.2 for the first few condition numbers (these were obtained by computing the inverse exactly using MATLAB's Symbolic Math Toolbox [825] and then computing the norm of the numeric representation of the inverse; the numbers given are correct to the figures shown).

It is an interesting fact that the matrix $\widetilde{H}_n = (1 / (i + j)) \in \mathbb{R}^{n \times n}$ (a submatrix of $H_{n+1}$ ) satisfies $\mu_n := \| \widetilde{H}_n \|_2 = \pi + O(1 / \log n)$ as $n \to \infty$ , as proved by Taussky [1131, 1949]. The convergence to $\pi$ is very slow: $\mu_{200} = 2.01$ , $\mu_{300} = 2.08$ , $\mu_{400} = 2.12$ .

That $H_{n}^{-1}$ is known explicitly is not as useful a property for testing an inversion algorithm as it might appear, because $H_{n}$ cannot be stored exactly in floating point arithmetic. This means that when we attempt to invert $H_{n}$ we at best invert $H_{n} + \Delta H$ (the matrix actually stored on the computer), where $|\Delta H| \leq uH_{n}$ , and $(H_{n} + \Delta H)^{-1}$ can differ greatly from $H_{n}^{-1}$ , in view of the ill conditioning. A possible way round this difficulty is to start with the integer matrix $H_{n}^{-1}$ , but its entries are so large that they are exactly representable in IEEE double precision arithmetic only for $n$ less than 13.

The Hilbert matrix is a special case of a Cauchy matrix $C_n \in \mathbb{R}^{n \times n}$ , whose elements are $c_{ij} = 1 / (x_i + y_j)$ , where $x, y \in \mathbb{R}^n$ are given $n$ -vectors (take $x_i = y_i = i - 0.5$ for the Hilbert matrix). The following formulae give the inverse and determinant of $C_n$ , and therefore generalize those for the Hilbert matrix. The

$(i,j)$ element of $C_n^{-1}$ is

$$
\frac{\prod_{1\leq k\leq n}(x_{j} + y_{k})(x_{k} + y_{i})}{(x_{j} + y_{i})\prod_{\substack{1\leq k\leq n\\ k\neq j}}(x_{j} - x_{k})\prod_{\substack{1\leq k\leq n\\ k\neq i}}(y_{i} - y_{k})}
$$

and

$$
\det  (C _ {n}) = \frac {\prod_ {1 \leq i <   j \leq n} \left(x _ {j} - x _ {i}\right) \left(y _ {j} - y _ {i}\right)}{\prod_ {1 \leq i , j \leq n} \left(x _ {i} + y _ {j}\right)},
$$

the latter formula having been published by Cauchy in 1841 [207, 1841, pp. 151-159]. The LU factors of $C_n$ were found explicitly by Cho [232, 1968]:

$$
l _ {i j} = \frac {x _ {j} + y _ {j}}{x _ {i} + y _ {i}} \prod_ {k = 1} ^ {j - 1} \frac {\left(x _ {j} + y _ {k}\right) \left(x _ {i} - x _ {k}\right)}{\left(x _ {i} + y _ {k}\right) \left(x _ {j} - x _ {k}\right)}, \quad 1 \leq j <   i \leq n,
$$

$$
u _ {i j} = \frac {1}{x _ {i} + y _ {j}} \prod_ {k = 1} ^ {i - 1} \frac {\left(x _ {i} - x _ {k}\right) \left(y _ {j} - y _ {k}\right)}{\left(x _ {k} + y _ {j}\right) \left(x _ {i} + y _ {k}\right)}, \qquad 1 \leq i \leq j \leq n.
$$

It is known that $C_n$ is totally positive if $0 < x_1 < \dots < x_n$ and $0 < y_1 < \dots < y_n$ (as is true for the Hilbert matrix) [1133, 1962, p. 295]. Interestingly, the sum of all the elements of $C_n^{-1}$ is $\sum_{i=1}^{n} (x_i + y_i)$ [743, 1997, Ex. 44, §1.2.3]. By exploiting their structure, singular value decompositions of Cauchy matrices can be computed to high accuracy; see Demmel [318, 1999].

# 28.2. Random Matrices

Random matrices are widely used for test purposes. Perhaps the earliest use of random matrices in numerical analysis was by von Neumann and Goldstine [1200, 1947], [501, 1951], who estimated the size of their error bounds for matrix inversion (see §9.13) for the case of random matrices; to do this, they had to estimate the condition number of a random matrix.

Intuitively, one might expect random matrices to be good at revealing programming errors and unusual behaviour of algorithms, but this expectation is not necessarily correct. For example, Miller [853, 1984, pp. 96-97] describes a mutation experiment involving Fortran codes for Gaussian elimination without pivoting, Gaussian elimination with partial pivoting, and Gauss-Jordan elimination with partial pivoting. For each code, all possible mutants were generated, where a mutant is obtained by making a single typographical change to the source code. All the mutants were tested on a single random linear system $Ax = b$ , with known solution, where $a_{ij}$ was chosen from the uniform $[-1,1]$ distribution. Many mutants were detected by their failure to pass the test of producing a solution with forward error less than a tolerance. However, some mutants passed this test, including all those that solve a system correctly in exact arithmetic; mutants in

the latter class include those that select an incorrect pivot row and thus implement a numerically unstable algorithm. A conclusion to be drawn from Miller's experiment is that random test data can reveal some programming errors, but will not reveal all.

A good example of a problem for which random test matrices are very poor at revealing algorithmic weaknesses is matrix condition number estimation. The popular condition estimation algorithms can yield poor estimates but, in practice, never produce them for a random matrix (see Chapter 15). The role of random matrices here is to indicate the average quality of the estimates.

Edelman [376, 1993] summarizes the properties of random matrices well when he says that

What is a mistake is to psychologically link a random matrix with the intuitive notion of a "typical" matrix or the vague concept of "any old matrix." In contrast, we argue that "random matrices" are very special matrices. The larger the size of the matrices the more predictable they are because of the central limit theorem.

Various results are known about the behaviour of matrices with elements from the normal $N(0,1)$ distribution. Matrices of this type are generated by MATLAB's randn function. Let $A_{n}$ denote a full $n \times n$ matrix, $T_{n}$ a triangular matrix, and $\tilde{T}_n$ a unit triangular matrix, all with elements from this distribution, and let $E(\cdot)$ be the expectation operator. Then, in the appropriate probabilistic sense, the following results hold as $n \to \infty$ :

$$
E \left(\log \left(\kappa_ {2} \left(A _ {n}\right)\right)\right) \approx \log n + 1. 5 3 7 \quad (\text {r e a l d a t a}), \tag {28.5}
$$

$$
E \left(\log \left(\kappa_ {2} \left(A _ {n}\right)\right)\right) \approx \log n + 0. 9 8 2 \quad \text {(c o m p l e x d a t a)}, \tag {28.6}
$$

$$
\left\| A _ {n} \right\| _ {2} \approx 2 \sqrt {n} \quad (\text {r e a l d a t a}), \tag {28.7}
$$

$$
\left\| A _ {n} \right\| _ {2} \approx 2 \sqrt {2} \sqrt {n} \quad (\text {c o m p l e x d a t a}), \tag {28.8}
$$

$$
\rho (A _ {n}) \approx \sqrt {n} \quad (\text {r e a l o r c o m p l e x d a t a}), \tag {28.9}
$$

$$
\kappa_ {2} \left(T _ {n}\right) ^ {1 / n} \approx 2 \quad (\text {r e a l d a t a}), \tag {28.10}
$$

$$
\kappa_ {2} \left(\widetilde {T} _ {n}\right) ^ {1 / n} \approx 1. 3 0 6 \quad (\text {r e a l d a t a}). \tag {28.11}
$$

For details of (28.5)-(28.8) see Edelman [371, 1988], and for (28.10), (28.11) see Viswanath and Trefethen [1197, 1998]. Edelman conjectures that the condition number results are true for any distribution with mean 0—in particular, the uniform $[-1,1]$ distribution used by MATLAB's rand. The results (28.5) and (28.6) show that random matrices from the normal $N(0,1)$ distribution tend to be very well conditioned.

The spectral radius result (28.9) has been proved as an upper bound on $\rho(A_n)$ by Geman [471, 1986] for independent identically distributed random variables $a_{ij}$ with zero mean and unit variance, and computer experiments suggest the approximate equality for the standard normal distribution [471, 1986].

A question of interest in eigenvalue applications is how many eigenvalues of a random real matrix are real. The answer has been given by Edelman, Kostlan, and Shub [381, 1994]: denoting by $E_{n}$ the expected number of real eigenvalues of an $n \times n$ matrix from the normal $N(0,1)$ distribution,

$$
\operatorname * {l i m} _ {n \to \infty} \frac {E _ {n}}{\sqrt {n}} = \sqrt {\frac {2}{\pi}}.
$$

Thus the proportion of real eigenvalues, $E_{n} / n$ , tends to zero as $n \to \infty$ . Exact formulae for $E_{n}$ for finite $n$ are also given in [381, 1994].

As a final, and more straightforward, example of the special nature of random matrices, note that a square matrix from the uniform [0,1] distribution has all positive entries with probability 1, and therefore has a real and positive dominant eigenvalue, by the Perron-Frobenius theory [636, 1985, Chap. 8]. The remaining eigenvalues tend to be of much smaller magnitude than the dominant one [27, 1990].

# 28.3. "Randsvd" Matrices

By randsvd²⁴ we mean a matrix $A \in \mathbb{R}^{m \times n}$ formed as $A = U\Sigma V^T$ , where $U \in \mathbb{R}^{m \times m}$ and $V \in \mathbb{R}^{n \times n}$ are random orthogonal matrices and $\Sigma = \mathrm{diag}(\sigma_i)$ ( $\sigma_i \geq 0$ ) is a given matrix of singular values. This type of matrix has a predetermined singular value distribution (and 2-norm condition number), but is, nevertheless, random.

Randsvd matrices have been widely used as test matrices, for example for condition estimators [582, 1987], [1070, 1980], and in the LAPACK testing software. Singular value distributions of interest include, with $\alpha \coloneqq \kappa_2(A) \geq 1$ a parameter,

1. one large singular value: $\sigma_{1} = 1$ , $\sigma_{i} = \alpha^{-1}$ , $i = 2$ : $n$ ;   
2. one small singular value: $\sigma_{i} = 1$ , $i = 1$ : $n - 1$ , $\sigma_{n} = \alpha^{-1}$ ;   
3. geometrically distributed singular values: $\sigma_{i} = \beta^{1 - i}$ , $i = 1:n$ , where $\beta = \alpha^{1 / (n - 1)}$ ;   
4. arithmetically distributed singular values: $\sigma_{i} = 1 - (1 - \alpha^{-1})(i - 1) / (n - 1)$ , $i = 1:n$ .

To be precise about what we mean by "random orthogonal matrix" we specify matrices from the Haar distribution, which is a natural distribution over the space of orthogonal matrices, defined in terms of a measure called the Haar measure [874, 1982, §2.1.4]. If $A \in \mathbb{R}^{n \times n}$ has elements from the normal $N(0, \sigma^2)$ distribution and $A$ has the QR factorization $A = QR$ , with the factorization normalized so that the diagonal elements of $R$ are positive, then $Q$ is from the Haar distribution, for any variance $\sigma^2$ [113, 1979], [1070, 1980]. If we compute $Q$ from this prescription, the cost is $2n^3$ flops. For our randsvd application, a more efficient approach is based on the following result of Stewart [1070, 1980].

Theorem 28.1 (Stewart). Let the independent vectors $x_{i} \in \mathbb{R}^{i}$ have elements from the normal $N(0,1)$ distribution for $i = 1:n - 1$ . Let $P_{i} = \mathrm{diag}(I_{n - i},\overline{P}_{i})$ , where $\overline{P}_i$ is the Householder transformation that reduces $x_{i}$ to $r_{ii}e_1$ . Then the product $Q = DP_{1}P_{2}\ldots P_{n - 1}$ is a random orthogonal matrix from the Haar distribution, where $D = \mathrm{diag}(\mathrm{sign}(r_{ii}))$ .

This result allows us to compute a product form representation of a random $n \times n$ orthogonal matrix from the Haar distribution in $O(n^2)$ flops. If we implicitly compute $U \in \mathbb{R}^{m \times m}$ and $V \in \mathbb{R}^{n \times n}$ using the construction in Theorem 28.1, and then form $A = U\Sigma V^T$ , exploiting the structure, the cost is $m^3 + n^3$ flops. The alternative, which involves obtaining $U$ and $V$ from the QR factorization of random matrices $A$ , is about twice as expensive.

Note that forming $U\Sigma V^T$ with $U$ and $V$ single Householder matrices, as is sometimes done in the literature, is not recommended, as it produces matrices of a very special form: diagonal plus a rank-2 correction.

The construction of randsvd matrices is, of course, easily adapted to produce random symmetric matrices $A = Q\Lambda Q^T$ with given eigenvalues.

# 28.4. The Pascal Matrix

The numbers in Pascal's triangle satisfy, practically speaking,

infinitely many identities.

— RONALD L. GRAHAM, DONALD E. KNUTH, and OREN PATASHNIK,

Concrete Mathematics (1994)

A particularly entertaining test matrix is the Pascal matrix $P_{n} \in \mathbb{R}^{n \times n}$ , defined by

$$
p _ {i j} = \frac {(i + j - 2) !}{(i - 1) ! (j - 1) !} = \left( \begin{array}{c} i + j - 2 \\ j - 1 \end{array} \right).
$$

The rows of Pascal's triangle appear as anti-diagonals of $P_{n}$ :

$$
\gg P = \text {p a s c a l} (6)
$$

$$
P =
$$

<table><tr><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>1</td><td>3</td><td>6</td><td>10</td><td>15</td><td>21</td></tr><tr><td>1</td><td>4</td><td>10</td><td>20</td><td>35</td><td>56</td></tr><tr><td>1</td><td>5</td><td>15</td><td>35</td><td>70</td><td>126</td></tr><tr><td>1</td><td>6</td><td>21</td><td>56</td><td>126</td><td>252</td></tr></table>

The earliest references to the Pascal matrix appear to be in 1958 by Newman and Todd [891, 1958] and by Rutishauser [1007, 1958] (see also Newman [890, 1962, pp. 240-241]); Newman and Todd say that the matrix was introduced to them by Rutishauser. The matrix was independently suggested as a test matrix by Caffney [196, 1963].

Rutishauser [1006, 1968, §8] notes that $P_{n}$ belongs to the class of moment matrices $M$ whose elements are contour integrals

$$
m _ {i j} = \int_ {C} z ^ {j - 1} (\bar {z}) ^ {i - 1} w (z) d z.
$$

All moment matrices corresponding to a positive weight function $w(z)$ on a contour $C$ are Hermitian positive definite (as is easily verified by considering the quadratic form $y^{*}My$ ). The choice $C = [0,1]$ , with weight function $w(z) = 1$ , yields the

Hilbert matrix. The Pascal matrix is obtained for $C$ the circle $\{z:|z - 1| = 1\}$ and $w(z) = (2\pi i(z - 1))^{-1}$ (not $w(z) = (2\pi)^{-1}$ as stated in [1006, 1968]); the change of variable $z = 1 + \exp (i\theta)$ yields a moment integral with a positive weight function.

Remarkably, the Cholesky factor of the Pascal matrix again contains the rows of Pascal's triangle, now arranged columnwise:

$$
\gg R = \operatorname {c h o l} (P)
$$

R =

<table><tr><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>0</td><td>0</td><td>1</td><td>3</td><td>6</td><td>10</td></tr><tr><td>0</td><td>0</td><td>0</td><td>1</td><td>4</td><td>10</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>5</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td></tr></table>

The scaled and transposed Cholesky factor $S = R^T$ diag $(1, -1, 1, -1, \ldots, (-1)^{n+1})$ is returned by $\text{pascal}(\mathbf{n}, 1)$ :

$$
\gg \mathrm {S} = \text {p a s c a l} (6, 1)
$$

S =

<table><tr><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>-1</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>-2</td><td>1</td><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>-3</td><td>3</td><td>-1</td><td>0</td><td>0</td></tr><tr><td>1</td><td>-4</td><td>6</td><td>-4</td><td>1</td><td>0</td></tr><tr><td>1</td><td>-5</td><td>10</td><td>-10</td><td>5</td><td>-1</td></tr></table>

It is involutory: $S^2 = I$ . This special property leads us to several more properties of $P = P_n$ . First, since $P = SS^T$ , $P^{-1} = S^{-T}S^{-1} = S^T S$ , and so $P^{-1}$ has integer entries (as is also clear from the fact that $\operatorname{det}(P) = \operatorname{det}(R)^2 = 1$ ). Moreover,

$$
P = S S ^ {T} = S (S ^ {T} S) S ^ {- 1} = S P ^ {- 1} S ^ {- 1},
$$

so $P$ and $P^{-1}$ are similar and hence have the same eigenvalues. In other words, the eigenvalues appear in reciprocal pairs. In fact, the characteristic polynomial $\pi_n$ has a palindromic coefficient vector, which implies the reciprocal eigenvalues property, since $\pi_n(\lambda) = \lambda^n\pi_n(1 / \lambda)$ . This is illustrated as follows (making use of MATLAB's Symbolic Math Toolbox):

$$
\gg \operatorname {c h a r p o l y} (\mathrm {P})
$$

ans $=$ 1-351\*x+6084\*x^2-13869\*x^3+6084\*x^4-351\*x^5+x^6  
>>eig(P)  
ans $=$

```txt
0.0030   
0.0643   
0.4893   
2.0436   
15.5535   
332.8463 
```

Since $P$ is symmetric, its eigenvalues are its singular values and so we also have that $\| P \|_2 = \| P^{-1} \|_2$ and $\| P \|_F = \| P^{-1} \|_F$ . Now

$$
p _ {n n} \leq \| P \| _ {2} \leq (\| P \| _ {1} \| P \| _ {\infty}) ^ {1 / 2} = \left(\frac {2 n - 1}{n}\right) p _ {n n},
$$

where for the last equality we used a binomial coefficient summation identity from [517, 1994, §5.1]. Hence, using Stirling's approximation $(n! \sim \sqrt{2\pi n} (n / e)^n)$ ,

$$
\kappa_ {2} (P _ {n}) \sim \left(\frac {(2 n) !}{(n !) ^ {2}}\right) ^ {2} \sim \frac {1 6 ^ {n}}{n \pi}.
$$

Thus $P_{n}$ is exponentially ill conditioned as $n\to \infty$

It is worth pointing out that it is not hard to generate symmetric positive definite matrices with determinant 1 and the reciprocal root property. Let $X = ZDZ^{-1}$ where $Z$ is nonsingular and $D = \mathrm{diag}(\pm 1) \neq \pm I$ . Then $X^2 = I$ and the matrix $A = X^T X$ has the desired properties. If we choose $Z$ lower triangular then $X$ is the Cholesky factor of $A$ up to a column scaling by $\mathrm{diag}(\pm 1)$ .

The inverse of the Pascal matrix was found explicitly by Cohen [258, 1975]: the $(i,j)$ element is

$$
(- 1) ^ {i - j} \sum_ {k = 0} ^ {n - i} {\binom {i + k - 1} {k}} \binom {i + k - 1} {i + k - j}, \qquad i \geq j.
$$

The Pascal matrix can be made singular simply by subtracting 1 from the $(n,n)$ element. To see this, note that

$$
\begin{array}{l} P - e _ {n} e _ {n} ^ {T} = S S ^ {T} - e _ {n} e _ {n} ^ {T} = S (I - (S e _ {n}) (S e _ {n}) ^ {T}) S ^ {T} \\ = S \operatorname {d i a g} (1, 1, \dots , 1, 0) S ^ {T}. \\ \end{array}
$$

This perturbation, $\Delta P = -e_n e_n^T$ , is far from being the smallest one that makes $P$ singular, which is $\Delta P_{\mathrm{opt}} = -\lambda_n v_n v_n^T$ , where $\lambda_n$ is the smallest eigenvalue of $P$ and $v_n$ is the corresponding unit eigenvector, for $\| \Delta P_{\mathrm{opt}} \|_2 = \lambda_n = \| P^{-1} \|_2^{-1}$ is of order $(n!)^2 / (2n)! \sim 4^{-n} \sqrt{n\pi}$ , as we saw above.

A more subtle property of the Pascal matrix is that it is totally positive. Karlin [712, 1968, p. 137] shows that the matrix with elements $\binom{i+j-1}{j}$ ( $i,j=0,1,\ldots$ ) is totally positive; the Pascal matrix is a submatrix of this one and hence is also totally positive. From the total positivity it follows that the Pascal matrix has distinct eigenvalues, which (as we already know from the positive definiteness) are real and positive, and that its $i$ th eigenvector (corresponding to the $i$ th largest eigenvalue) has exactly $i-1$ sign changes [454, 1959, Thm. 13, p. 105].

$T = \text{pascal}(\mathbf{n}, 2)$ is obtained by rotating $S$ clockwise through 90 degrees and multiplying by $-1$ if $n$ is even:

$$
\begin{array}{l} \gg \mathrm {T} = \text {p a s c a l} (6, 2) \\ \mathrm {T} = \\ \begin{array}{c c c c c c} - 1 & - 1 & - 1 & - 1 & - 1 & - 1 \\ 5 & 4 & 3 & 2 & 1 & 0 \\ - 1 0 & - 6 & - 3 & - 1 & 0 & 0 \\ 1 0 & 4 & 1 & 0 & 0 & 0 \\ - 5 & - 1 & 0 & 0 & 0 & 0 \\ 1 & 0 & 0 & 0 & 0 & 0 \end{array} \\ \end{array}
$$

It has the surprising property that it is a cube root of the identity, a property noted by Turnbull [1167, 1929, p. 332]:

$$
\gg \mathrm {T} * \mathrm {T}
$$

$$
\text {a n s} =
$$

$$
\begin{array}{c c c c c c} 0 & 0 & 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 & - 1 & - 5 \\ 0 & 0 & 0 & 1 & 4 & 1 0 \\ 0 & 0 & - 1 & - 3 & - 6 & - 1 0 \\ 0 & 1 & 2 & 3 & 4 & 5 \\ - 1 & - 1 & - 1 & - 1 & - 1 & - 1 \end{array}
$$

$$
\gg \mathrm {T} * \mathrm {T} * \mathrm {T}
$$

$$
\text {a n s} =
$$

$$
\begin{array}{c c c c c c} 1 & 0 & 0 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 & 0 & 1 \end{array}
$$

Finally, we note that it is trivial to plot an approximation to the Sierpinski gasket [931, 1992, §2.2], [518, 1992] in MATLAB: simply type spy(rem(pascal(n), 2)). See Figure 28.1. The picture produced by this command is incorrect for large $n$ , however, because the elements of $\text{pascal}(\mathfrak{n})$ become too large to be exactly representable in floating point arithmetic.

# 28.5. Tridiagonal Toeplitz Matrices

A tridiagonal Toeplitz matrix has the form

$$
T _ {n} (c, d, e) = \left[ \begin{array}{c c c c} d & e & & \\ c & d & \ddots & \\ & \ddots & \ddots & e \\ & & c & d \end{array} \right].
$$

![](images/8cc05202c27cb7b8893b3a3ffd4645917ec2fe959f00caf8a179035333215452.jpg)  
Figure 28.1. spy(rem(pascal(32),2)).

Such matrices arise, for example, when discretizing partial differential equations or boundary value problems for ordinary differential equations. The eigenvalues are known explicitly [1004, 1947], [1005, 1952], [1143, 1977, pp. 155-156]:

$$
d + 2 (c e) ^ {1 / 2} \cos (k \pi / (n + 1)), \quad k = 1: n.
$$

The eigenvalues are also known for certain variations of the symmetric matrix $T_{n}(c,d,c)$ in which the $(1,1)$ and $(n,n)$ elements are modified; see Gregory and Karney [524, 196g].

The matrix $T_{n}(-1,2,-1)$ is minus the well-known second difference matrix, which arises in applying central differences to a second derivative operator. Its inverse has $(i,j)$ element $-i(n - j + 1) / (n + 1)$ (cf. Theorem 15.9). The condition number satisfies $\kappa_{2}(T_{n}) \sim (4 / \pi^{2})n^{2}$ .

One interesting property of $T_{n}(c,d,e)$ is that the diagonals of its LU factorization converge as $n\to \infty$ when $T_{n}$ is symmetric and diagonally dominant, and this allows some savings in the computation of the LU factorization, as shown by Malcolm and Palmer [810, 1974]. Similar properties hold for cyclic reduction; see Bondeli and Gander [150, 1994].

# 28.6. Companion Matrices

The companion matrix associated with the characteristic polynomial

$$
\det  (A - \lambda I) = (- 1) ^ {n} \left(\lambda^ {n} - a _ {n - 1} \lambda^ {n - 1} - \dots - a _ {0}\right)
$$

of $A\in \mathbb{C}^{n\times n}$ is the matrix

$$
C = \left[ \begin{array}{c c c c c} a _ {n - 1} & a _ {n - 2} & \dots & \dots & a _ {0} \\ 1 & 0 & \dots & \dots & 0 \\ 0 & 1 & \ddots & & 0 \\ \vdots & & \ddots & 0 & 0 \\ 0 & \dots & \dots & 1 & 0 \end{array} \right].
$$

In MATLAB $C$ can be computed from $A$ via $\mathbb{C} = \text{compan}(\text{poly}(\mathsf{A}))$ . It is easy to check that $C$ has the same characteristic polynomial as $A$ , and that if $\lambda$ is an eigenvalue of $C$ then $[\lambda^{n-1}, \lambda^{n-2}, \ldots, \lambda, 1]^T$ is a corresponding eigenvector. Since $C - \lambda I$ has rank at least $n-1$ for any $\lambda$ , $C$ is nonderogatory, that is, in the Jordan form no eigenvalue appears in more than one Jordan block. It follows that $A$ is similar to $C$ only if $A$ is nonderogatory.

There are no explicit formulae for the eigenvalues of $C$ , but, perhaps surprisingly, the singular values have simple representations, as found by Kenney and Laub [725, 1988] (see also Kittaneh [736, 1995]):

$$
\begin{array}{l} \sigma_ {1} ^ {2} = \frac {1}{2} \left(\alpha + \sqrt {\alpha^ {2} - 4 a _ {0} ^ {2}}\right), \\ \sigma_ {i} ^ {2} = 1, \quad i = 2: n - 1, \\ \sigma_ {n} ^ {2} = \frac {1}{2} \left(\alpha - \sqrt {\alpha^ {2} - 4 a _ {0} ^ {2}}\right), \\ \end{array}
$$

where $\alpha = 1 + a_0^2 +\dots +a_{n - 1}^2$ . These formulae generalize to block companion matrices, as shown by Higham and Tisseur [625, 2001].

The compat function is a useful means for generating new test matrices from old. For any $A \in \mathbb{C}^{n \times n}$ , compat(poly(A)) is a nonnormal matrix with the same eigenvalues as $A$ (to be precise, compat(poly(A)) is normal if and only if $a_0 = 1$ and $a_i = 0$ for $i > 0$ ).

Companion matrices tend to have interesting pseudospectra, as illustrated in Figure 28.2. For more information on the pseudospectra of companion matrices see Toh and Trefethen [1144, 1994].

# 28.7. Notes and References

The earliest reference to the Hilbert matrix appears to be [626, 1894], wherein Hilbert obtains the formula (28.2) for $\operatorname{det}(H_n)$ .

The formula (28.1) for $H_{n}^{-1}$ is taken from Choi [233, 1983], who describes various interesting properties of the Hilbert matrix and its infinite analogue. An excellent reference for the derivation of formulae for the inverse of the Cauchy and Hilbert matrices is Knuth [743, 1997, pp. 37-38]. Another reference for the Cauchy matrix is Tyrtyshnikov [1172, 1991]. The formulae (28.3) and (28.4) for the Cholesky factor and its inverse are from Choi [233, 1983] and Todd [1141, 1954].

Forsythe and Moler [431, 1967] have a chapter devoted to the Hilbert matrix, in which they describe the underlying least squares problem and discuss numerical

![](images/cfa15cf50f30b7863349bbb826c4a04157f5bcd3259f9c09ac909cd3fe05dbe0.jpg)

![](images/d79575065f3715ff1003563f82f2d612a23608e9ff80b89d22289d6343363d9a.jpg)  
Figure 28.2. Pseudospectra of compan(poly(A)).

computation of the inverse. There have been many papers on the Hilbert matrix; two of particular interest are by Todd [1141, 1954], [1142, 1961].

Other references on the eigenvalues and condition numbers of random matrices include Edelman [372, 1991], [375, 1992] and Kostlan [748, 1992].

Anderson, Olkin, and Underhill [25, 1987] suggest another way to construct random orthogonal matrices from the Haar distribution, based on products of random Givens rotations.

The involutory triangular matrix $\text{pascal}(\mathfrak{n},1)$ arises in the stepsize changing mechanism in an ordinary differential equation code based on backward differentiation formulae; see Shampine and Reichelt [1032, 1997].

We mention some other collections of test matrices. The Harwell-Boeing collection of sparse matrices, largely drawn from practical problems, is presented by Duff, Grimes, and Lewis [362, 1989], [363, 1992]. Bai, Day, Demmel, and Dongarra [44, 1997] present a collection of test matrices for large-scale nonsymmetric eigenvalue problems. Zielke [1281, 1986] gives various parametrized rectangular matrices of fixed dimension with known generalized inverses. Demmel and McKenney [332, 1989] present a suite of Fortran 77 codes for generating random square and rectangular matrices with prescribed singular values, eigenvalues, band structure, and other properties. This suite is part of the testing code for LAPACK (see below), and MATLAB's gallery ('randsvd', ...) is modeled on it.

The Web repository Matrix Market [147, 1997] at http://math.nist.gov/MatrixMarket/ contains a large collection of test matrices, comprising both individual matrices of fixed dimension (usually large and sparse, coming from applications) and matrix generators that can produce matrices of arbitrary dimension. The matrices can be downloaded in a variety of formats. Matrix Market includes matrices from several of the collections mentioned above.

In testing matrix algorithms it can be useful to be able to construct matrices with some given combination of eigenvalues, singular values, and diagonal elements (subject to any necessary constraints on the given data). Algorithms of this type can be summarized as follows.

- Construct symmetric $A$ with given diagonal elements and given eigenvalues. See Chan and Li [209, 1983], [210, 1983] and Zha and Zhang [1280, 1995]

(see also Ikramov [659, 1998]). A special case is the generation of random correlation matrices with specified eigenvalues (a correlation matrix is a symmetric positive semidefinite matrix with ones on the diagonal); see Davies and Higham [293, 2000] and the references therein.

- Construct $A$ with given eigenvalues and given singular values. See Chu [238, 2000], and see Kosowski and Smoktunowicz [747, 2000] for the case of triangular matrices with unit diagonal (the latter paper solves a research problem posed in the first edition of this book).   
- Construct $A$ with given singular values and given diagonal elements. See Chu [237, 1999].

Note that not all these algorithms come with a guarantee that the construction is numerically stable: caveat emptor!

# 28.7.1. LAPACK

The LAPACK distribution contains a suite of routines for generating test matrices, located in the directory LAPACK/TESTING/MATGEN (in Unix notation). These routines (whose names are of the form xLAzzz) are used for testing when LAPACK is installed and are not described in the LAPACK Users' Guide [20, 1999].

# Problems

28.1. Investigate the spectral and pseudospectral properties of pentadiagonal Toeplitz matrices. See Figure 28.3. MATLAB's gallery('toeppen', ...) generates matrices of this type. References are Beam and Warming [96, 1993] and Reichel and Trefethen [978, 1992].

28.2. (RESEARCH PROBLEM) Two methods for generating a real orthogonal matrix from the Haar distribution are Stewart's method (Theorem 28.1), based on Householder transformations, and a method of Anderson, Olkin, and Underhill [25, 1987], based on Givens rotations. Compare the efficiency of these two methods when used to generate randsvd matrices. Investigate the use of the Givens rotations approach to construct random banded matrices with given singular values and random symmetric banded matrices with given eigenvalues, and compare with the technique of generating a full matrix and then using band reduction (as implemented in MATLAB's gallery('randsvd', ...)).

![](images/59091926db5abc483a108fdb2754bcddfa8df56ec612afcc898e705808b5cc3d.jpg)

![](images/df907ca518e02035217da85172e8eb26e4a5399bd41bfe9cfbb740517e9515f7.jpg)

![](images/42219b9506cf537b8b2cada5a0157edaf6f1c32d9818fb1936c2d56de24092ee.jpg)

![](images/5eb4199c7f38c391714ceca5fcd12699052e38d8b62f5f2411747cef7be03c92.jpg)  
Figure 28.3. Pseudospectra of $32 \times 32$ pentadiagonal Toeplitz matrices, gallery('toeppen', 32, a, b, c, d, e). Shown are the parameters (a, b, c, d, e).

# Appendix A Solutions to Problems

1.1. Since $\widetilde{E}_{\mathrm{rel}}(\widehat{x}) = E_{\mathrm{rel}}(\widehat{x})|x| / |\widehat{x}|$ and $\widehat{x} = x(1 \pm E_{\mathrm{rel}}(\widehat{x}))$ , we have

$$
\frac {E _ {\mathrm {r e l}} (\widehat {x})}{1 + E _ {\mathrm {r e l}} (\widehat {x})} \leq \widetilde {E} _ {\mathrm {r e l}} (\widehat {x}) \leq \frac {E _ {\mathrm {r e l}} (\widehat {x})}{1 - E _ {\mathrm {r e l}} (\widehat {x})}.
$$

Hence if $E_{\mathrm{rel}}(\hat{x}) < 0.01$ , say, then there is no difference between $E_{\mathrm{rel}}$ and $\tilde{E}_{\mathrm{rel}}$ for practical purposes.

1.2. Nothing can be concluded about the last digit before the decimal point. Evaluating $y$ to higher precision yields

<table><tr><td>t</td><td>y</td></tr><tr><td>35</td><td>262537412640768743.99999999999925007</td></tr><tr><td>40</td><td>262537412640768743.9999999999992500725972</td></tr></table>

This shows that the required digit is, in fact, 3. The interesting fact that $y$ is so close to an integer was pointed out by Lehmer [779, 1943], who explains its connection with number theory. It is known that $y$ is irrational [1090, 1991].

1.3. $x / (\sqrt{x + 1} +1).$

2. $2\sin \frac{x - y}{2}\cos \frac{x + y}{2}$ .

3. $(x - y)(x + y)$ . Cancellation has not been avoided, but it is now harmless if $x$ and $y$ are known exactly (see also Problem 3.8).

4. $\sin x / (1 + \cos x)$

5. $c = \left((a - b)^2 + ab(2\sin \theta / 2)^2\right)^{1/2}$ .

1.4. $a + ib = (x + iy)^2 = x^2 - y^2 + 2ixy$ , so $b = 2xy$ and $a = x^2 - y^2$ , giving $x^2 - b^2 / (4x^2) = a$ , or $4x^4 - 4ax^2 - b^2 = 0$ . Hence

$$
x ^ {2} = \frac {4 a \pm \sqrt {1 6 a ^ {2} + 1 6 b ^ {2}}}{8} = \frac {a \pm \sqrt {a ^ {2} + b ^ {2}}}{2}.
$$

If $a \geq 0$ we use this formula with the plus sign, since $x^2 \geq 0$ . If $a < 0$ this formula is potentially unstable, so we use the rewritten form

$$
x ^ {2} = \frac {b ^ {2}}{2 (- a + \sqrt {a ^ {2} + b ^ {2}})}.
$$

In either case we get two values for $x$ and recover $y$ from $y = b / (2x)$ . Note that there are other issues to consider here, such as scaling to avoid overflow.

1.5. A straightforward evaluation of $\log(1 + x)$ is not sufficient, since the addition $1 + x$ loses significant digits of $x$ when $x$ is small. The following method is effective (for another approach, see Hull, Fairgrieve, and Tang [649, 1994]): calculate $w = 1 + x$ and then compute

$$
f (x) = \left\{ \begin{array}{l l} x, & w = 1, \\ \frac {x \log w}{w - 1}, & w \neq 1. \end{array} \right. \tag {A.1}
$$

The explanation of why this method works is similar to that for the method in §1.14.1. We have $\widehat{w} = (1 + x)(1 + \delta)$ , $|\delta| \leq u$ , and if $\widehat{w} = 1$ then $|x| \leq u + u^2 + u^3 + \dots$ , so from the Taylor series $f(x) = x(1 - x/2 + x^2/3 - \dots)$ we see that $f(x) = x$ is a correctly rounded result. If $\widehat{w} \neq 1$ then

$$
\widehat {f} = \frac {(x \log \widehat {w}) (1 + \epsilon_ {1}) (1 + \epsilon_ {2})}{(\widehat {w} - 1) (1 + \epsilon_ {3})} (1 + \epsilon_ {4}), \quad | \epsilon_ {i} | \leq u.
$$

Defining $\widehat{w} \eqqcolon 1 + z$

$$
g (\widehat {w}) := \frac {\log \widehat {w}}{\widehat {w} - 1} = \frac {\log (1 + z)}{z} = 1 - z / 2 + z ^ {2} / 3 - \dots ,
$$

so if $\widehat{w} \approx w \approx 1$ (thus $x \approx 0$ ) then

$$
g (w) - g (\widehat {w}) \approx \frac {\widehat {w} - w}{2} = \frac {(1 + x) \delta}{2} \approx \frac {\delta}{2} \approx \frac {g (w) \delta}{2}.
$$

Thus, with $1 + \theta \coloneqq (1 + \epsilon_1)(1 + \epsilon_2)(1 + \epsilon_3)^{-1}(1 + \epsilon_4)$

$$
\widehat {f} = x g (\widehat {w}) (1 + \theta) \approx x g (w) (1 + \theta) = f (x) (1 + \theta),
$$

showing that $\widehat{f}$ is an accurate approximation to $f(x) = \log (1 + x)$ . Figure A.1 shows MATLAB plots of $\log (1 + x)$ , using MATLAB's built-in log function, and $\log 1p$ , an M-file of Cleve Moler that implements (A.1). Close to the origin the lack of smoothness of the curve for the $\log$ evaluation is clear.

1.7.From (1.4)we have

$$
\begin{array}{l} (n - 1) V (x + \Delta x) = \sum_ {i = 1} ^ {n} \left(x _ {i} + \Delta x _ {i} - \bar {x} - n ^ {- 1} \sum_ {j = 1} ^ {n} \Delta x _ {j}\right) ^ {2} \\ = (n - 1) V (x) + 2 \sum_ {i = 1} ^ {n} \left(x _ {i} - \bar {x}\right) \left(\Delta x _ {i} - n ^ {- 1} \sum_ {j = 1} ^ {n} \Delta x _ {j}\right) \\ + \sum_ {i = 1} ^ {n} \left(\Delta x _ {i} - n ^ {- 1} \sum_ {j = 1} ^ {n} \Delta x _ {j}\right) ^ {2} \\ = (n - 1) V (x) + 2 \sum_ {j = 1} ^ {n} \left(x _ {i} - \bar {x}\right) \Delta x _ {i} \\ + \sum_ {i = 1} ^ {n} \left(\Delta x _ {i} - n ^ {- 1} \sum_ {j = 1} ^ {n} \Delta x _ {j}\right) ^ {2}. \\ \end{array}
$$

This yields the following inequality, which is attainable to first order:

$$
(n - 1) | V (x) - V (x + \varDelta x) | \leq 2 \epsilon \sum_ {i = 1} ^ {n} | x _ {i} - \overline {{x}} | | x _ {i} | + \epsilon^ {2} \sum_ {i = 1} ^ {n} \left(| x _ {i} | + n ^ {- 1} \sum_ {j = 1} ^ {n} | x _ {j} |\right) ^ {2}.
$$

![](images/1951425f507d135c2fa1b1eb630eab1fbcee961736c437e7d03107a6ebe7cbd7.jpg)

![](images/e3b0fad0973633c3432eee916c0e6f814dbf2ab5b0a21901b14d7ec739e82351.jpg)  
Figure A.1. $\log (1 + x)$ evaluated using MATLAB's log (top) and using the formula (A.1) (bottom).

Dividing by $\epsilon (n - 1)V(x)$ and taking the limit as $\epsilon \to 0$ gives the expression for $\kappa_{C}$ . The result for $\kappa_{N}$ follows from

$$
\left| \sum_ {j = 1} ^ {n} (x _ {i} - \overline {{{{x}}}}) \varDelta x _ {i} \right| \leq \left(\sum_ {i = 1} ^ {n} (x _ {i} - \overline {{{{x}}}}) ^ {2}\right) ^ {1 / 2} \epsilon \| x \| _ {2} = \epsilon (n - 1) ^ {1 / 2} V (x) ^ {1 / 2} \| x \| _ {2},
$$

where the inequality is attainable (Cauchy-Schwarz), together with the relation $(n - 1)V(x) = \| x\| _2^2 -n\overline{x}^2$ . That $\kappa_{N}\geq \kappa_{C}$ is easily verified.

1.8. The general solution to the recurrence is

$$
x _ {k} = \frac {1 0 0 ^ {k + 1} a + 6 ^ {k + 1} b + 5 ^ {k + 1} c}{1 0 0 ^ {k} a + 6 ^ {k} b + 5 ^ {k} c},
$$

where $a, b$ , and $c$ are arbitrary constants. The particular starting values chosen yield $a = 0, b = c = 1$ , so that

$$
x _ {k} = \frac {6 ^ {k + 1} + 5 ^ {k + 1}}{6 ^ {k} + 5 ^ {k}} = 6 - \frac {1}{1 + (6 / 5) ^ {k}}.
$$

Rounding errors in the evaluation (and in the representation of $x_{1}$ on a binary machine) cause a nonzero "a" term to be introduced, and the computed values are approximately of the form

$$
\widehat {x} _ {k} \approx \frac {1 0 0 ^ {k + 1} \eta + 6 ^ {k + 1} + 5 ^ {k + 1}}{1 0 0 ^ {k} \eta + 6 ^ {k} + 5 ^ {k}},
$$

for a constant $\eta$ of order the unit roundoff. Hence the computed iterates rapidly converge to 100. Note that resorting to higher precision merely delays the inevitable convergence to 100. Priest [955, 1992, pp. 54-56] gives some interesting observations on the stability of the evaluation of the recurrence.

# 1.9. Writing

$$
C := \operatorname {a d j} (A) = \left[ \begin{array}{c c} a _ {2 2} & - a _ {1 2} \\ - a _ {2 1} & a _ {1 1} \end{array} \right],
$$

we have

$$
\begin{array}{l} \widehat {x} = f l \left(\frac {1}{d} C b\right) \\ = \frac {1}{d} (C + \varDelta C) b, \qquad | \varDelta C | \leq \gamma_ {3} | C |, \\ = x + \frac {1}{d} \Delta C b. \\ \end{array}
$$

So

$$
\frac {\| x - \widehat {x} \| _ {\infty}}{\| x \| _ {\infty}} \leq \gamma_ {3} \frac {\| | A ^ {- 1} | | b | \| _ {\infty}}{\| x \| _ {\infty}} \leq \gamma_ {3} \operatorname {c o n d} (A, x).
$$

Also, $r = b - A\widehat{x} = -(1 / d)A\Delta Cb$ , so $|r|\leq \gamma_3|A||A^{-1}||b|$ , which implies the normwise residual bound. Note that the residual bound shows that $\| r\|_{\infty} / (\| A\|_{\infty}\| x\|_{\infty})$ will be small if $x$ is a large-normed solution ( $\| x\|_{\infty}\approx \| A^{-1}\|_{\infty}\| b\|_{\infty}$ ).

1.10. Let $\widehat{m} = fl(\overline{x})$ . For any standard summation method we have (see §4.2)

$$
\begin{array}{l} \hat {m} = n ^ {- 1} \sum_ {i = 1} ^ {n} x _ {i} (1 + \delta_ {i}), \quad | \delta_ {i} | \leq \gamma_ {n - 1}, \\ = m + \Delta m, \quad \Delta m := n ^ {- 1} \sum_ {i = 1} ^ {n} x _ {i} \delta_ {i}. \\ \end{array}
$$

Then, since $fl\big((x_i - \widehat{m})^2\big) = (x_i - \widehat{m})^2(1 + \alpha_i)^2(1 + \beta_i), |\alpha_i|, |\beta_i| \leq u, \widehat{V}$ satisfies

$$
\begin{array}{l} (n - 1) \widehat {V} = \sum_ {i = 1} ^ {n} \left(x _ {i} - \widehat {m}\right) ^ {2} \left(1 + \epsilon_ {i}\right), \quad \left| \epsilon_ {i} \right| \leq \gamma_ {n + 3} \\ = \sum_ {i = 1} ^ {n} \left[ \left(x _ {i} - m\right) ^ {2} - 2 \varDelta m (x _ {i} - m) + \varDelta m ^ {2} \right] \left(1 + \epsilon_ {i}\right) \\ = (n - 1) V + \sum_ {i = 1} ^ {n} \left(x _ {i} - m\right) ^ {2} \epsilon_ {i} \\ + \sum_ {i = 1} ^ {n} (- 2 \Delta m (x _ {i} - m) + \Delta m ^ {2}) (1 + \epsilon_ {i}). \\ \end{array}
$$

Hence, defining $\mu \coloneqq n^{-1}\sum_{i = 1}^{n}|x_i|$ , so that $|\varDelta m|\leq\gamma_{n-1}\mu$

$$
\begin{array}{l} (n - 1) | V - \widehat {V} | \leq \gamma_ {n + 3} (n - 1) V + \sum_ {i = 1} ^ {n} | - 2 \Delta m (x _ {i} - m) \epsilon_ {i} + \Delta m ^ {2} (1 + \epsilon_ {i}) | \\ \leq \gamma_ {n + 3} (n - 1) V + 2 \gamma_ {n - 1} \gamma_ {n + 3} \mu \sqrt {n (n - 1) V} + \gamma_ {n - 1} ^ {2} \mu^ {2} n (1 + \gamma_ {n + 3}), \\ \end{array}
$$

that is,

$$
\begin{array}{l} \frac {| V - \widehat {V} |}{V} \leq \gamma_ {n + 3} + 2 \theta \gamma_ {n - 1} \gamma_ {n + 3} + \theta^ {2} \gamma_ {n - 1} ^ {2} (1 + \gamma_ {n + 3}) \\ = (n + 3) u + O \left(u ^ {2}\right), \\ \end{array}
$$

where

$$
\theta = \mu \sqrt {\frac {n}{(n - 1) V}} \leq \frac {\| x \| _ {2}}{\sqrt {(n - 1) V}} = \frac {1}{2} \kappa_ {N}.
$$

2.1. There are $1 + 2(e_{\max} - e_{\min} + 1)(\beta - 1)\beta^{t - 1}$ normalized numbers (the "1" is for zero), and $2(\beta^{t - 1} - 1)$ subnormal numbers. For IEEE arithmetic we therefore have

<table><tr><td></td><td>Normalized</td><td>Subnormal</td></tr><tr><td>Single precision</td><td>4.3 × 109</td><td>1.7 × 107</td></tr><tr><td>Double precision</td><td>1.8 × 1019</td><td>9 × 1015</td></tr></table>

2.2. Without loss of generality suppose $x > 0$ . We can write $x = m \times \beta^{e - t}$ , where $\beta^{t - 1} \leq m < \beta^t$ . The next larger floating point number is $x + \Delta x$ , where $\Delta x = \beta^{e - t}$ , and

$$
\beta^ {- 1} \epsilon_ {M} | x | = \beta^ {- t} | x | <   \frac {| x |}{m} = | \varDelta x | \leq \beta^ {e - t} (\beta^ {1 - t} m) = \epsilon_ {M} | x |.
$$

The same upper bound clearly holds for the "next smaller" case, and the lower bound in this case is also easy to see.

2.3. The answer is the same for all adjacent nonzero pairs of single precision numbers. Suppose the numbers are 1 and $1 + \epsilon_{M}(\text{single}) = 1 + 2^{-23}$ . The spacing of the double precision numbers on $[1,2]$ is $2^{-52}$ , so the answer is $2^{29} - 1 \approx 5.4 \times 10^{8}$ .   
2.4. Inspecting the proof of Theorem 2.2 we see that $|y_i| \geq \beta^{e-1}$ , $i = 1, 2$ , and so we also have $|fl(x) - x| / |fl(x)| \leq u$ , that is, $fl(x) = x / (1 + \delta)$ , $|\delta| \leq u$ . Note that this is not the same $\delta$ as in Theorem 2.2, although it has the same bound, and unlike in Theorem 2.2 there can be equality in this bound for $\delta$ .   
2.5. The first part is trivial. Since, in binary notation,

$$
x = 0. 1 1 0 0 1 1 0 0 1 1 0 0 1 1 0 0 1 1 0 0 1 1 0 0 \mid 1 1 0 0 \dots \times 2 ^ {- 3},
$$

we have, rounding to 24 bits,

$$
\widehat {x} = 0. 1 1 0 0 \quad 1 1 0 0 \quad 1 1 0 0 \quad 1 1 0 0 \quad 1 1 0 0 \quad 1 1 0 1 \times 2 ^ {- 3}.
$$

Thus

$$
\begin{array}{l} \widehat {x} - x = \left(0. 0 0 1 - 0. 0 0 0 \overline {{1 1 0 0}}\right) _ {2} \times 2 ^ {- 2 1} \times 2 ^ {- 3} \\ = \left(\frac {1}{8} - \frac {1}{1 0}\right) \times 2 ^ {- 2 4} = \frac {1}{4 0} \times 2 ^ {- 2 4}, \\ \end{array}
$$

and so $(x - \widehat{x}) / x = -\frac{1}{4} \times 2^{-24} = -\frac{1}{4} u$ .

2.6. Since the double precision significand contains 53 bits, $p = 2^{53} = 9007199254740992 \approx 9.01 \times 10^{15}$ . For single precision, $p = 2^{24} = 16777216 \approx 1.68 \times 10^7$ .

2.7.

1. True, since in IEEE arithmetic $fl(a \text{ op } b)$ is defined to be the rounded value of $a \text{ op } b$ , round $(a \text{ op } b)$ , which is the same as round $(b \text{ op } a)$ .   
2. True for round to nearest (the default) and round to zero, but false for round to $\pm \infty$ .   
3. True, because $fl(a + a) \coloneqq \operatorname{round}(a + a) = \operatorname{round}(2 * a) \eqqcolon fl(2 * a)$ .   
4. True: similar to 3.   
5. False, in general.

6. True for binary arithmetic. Since the division by 2 is exact, the inequality is equivalent to $2a \leq fl(a + b) \leq 2b$ . But $a + b \leq 2b$ , so, by the monotonicity of rounding, $fl(a + b) = \text{round}(a + b) \leq \text{round}(2b) = 2b$ . The lower bound is verified similarly.

2.8. Examples in 3-digit decimal arithmetic are $fl((5.01 + 5.02) / 2) = fl(10.0 / 2) = 5.0$ and $fl((5.02 + 5.04) / 2) = fl(10.1 / 2) = 5.05$ .

The left-hand inequality is immediate, since $fl((b - a) / 2) \geq 0$ . The right-hand inequality can possibly be violated only if $a$ and $b$ are close (otherwise $(a + b) / 2$ is safely less than $b$ , so the inequality will hold). But then, by Theorem 2.5, $fl(b - a)$ is obtained exactly, and the result will have several zero low-order digits in the significand because of cancellation. Consequently, if the base is even the division is done exactly, and the right-hand inequality follows by the monotonicity of rounding. Alternatively, and even more simply, for any base we can argue that $fl((b - a) / 2) \leq b - a$ , so that $a + fl((b - a) / 2) \leq b$ and, again, the result follows by the monotonicity of rounding.

2.9.

$$
\begin{array}{l} \sqrt {1 - 2 ^ {- 5 3}} = 1 - \frac {1}{2} \cdot 2 ^ {- 5 3} - \frac {1}{8} \cdot 2 ^ {- 1 0 6} - \dots \\ = 0. \underbrace {1 1 \ldots 1} _ {5 3} 0 \underbrace {1 1 \ldots 1} _ {5 4} 0 1 1 \ldots \quad (\text {b i n a r y}). \\ \end{array}
$$

Rounded directly to 53 bits this yields $1 - 2^{-53}$ . But rounded first to 64 bits it yields

$$
0. \underbrace {1 1 \ldots 1} _ {5 3} 1 \underbrace {0 0 \ldots 0} _ {1 0},
$$

and when this number is rounded to 53 bits using the round to even rule it yields 1.0.

2.12. The spacing between the floating point numbers in the interval $(1/2, 1]$ is $\epsilon/2$ (cf. Lemma 2.1), so $|1/x - fl(1/x)| \leq \epsilon/4$ , which implies that $|1 - xfl(1/x)| \leq \epsilon x/4 < \epsilon/2$ . Thus

$$
1 - \epsilon / 2 <   x f l (1 / x) <   1 + \epsilon / 2.
$$

Since the spacing of the floating point numbers just to the right of 1 is $\epsilon$ , $xfl(1/x)$ must round to either $1 - \epsilon/2$ or 1.

2.13. If there is no double rounding the answer is 257, 736, 490. For a proof that combines mathematical analysis with computer searching, see Edelman [379, 1994].

2.15. The IEEE standard does not define the results of exponentiation. The choice $0^0 = 1$ can be justified in several ways. For example, if $p(x) = \sum_{j=0}^{n} a_j x^j$ then $p(0) = a_0 = a_0 \times 0^0$ , and the binomial expansion $(x + y)^n = \sum_{k=0}^{n} \binom{n}{k} x^k y^{n-k}$ yields $1 = 0^0$ for $x = 0$ , $y = 1$ . For more detailed discussions see Goldberg [496, 1991, p. 32] and Knuth [742, 1992, pp. 406-408].

2.17. If the rounding mode is round to zero or round to $-\infty$ then $fl(2x_{\max}) = x_{\max}$ .

2.18. No. A counterexample in 2-digit base 10 arithmetic is $fl(2.0 - 0.91) = fl(1.09) = 1.1$ .

2.19. Every floating point number (whether normalized or unnormalized) is a multiple of $\mu = \beta^{e_{\min} - t}$ (although the converse is not true), therefore $x \pm y$ is also a multiple of $\mu$ . The subnormal numbers are equally spaced between $\mu$ and $\beta^{e_{\min} - 1}$ , the smallest positive normalized floating point number. But since $fl(x \pm y)$ underflows, $|x \pm y| < \beta^{e_{\min} - 1}$ , and therefore $x \pm y$ is exactly representable as a subnormal number. Thus $fl(x \pm y) = x \pm y$ .

2.20. The function $fl(\sqrt{x})$ maps the set of positive floating point numbers onto a set of floating point numbers with about half as many elements. Hence there exist two distinct floating point numbers $x$ having the same value of $fl(\sqrt{x})$ , and so the condition $(\sqrt{x})^2 = |x|$ cannot always be satisfied in floating point arithmetic. The requirement $\sqrt{x^2} = |x|$ is reasonable for base 2, however, and is satisfied in IEEE arithmetic, as we now show.

Without loss of generality, we can assume that $1 \leq x < 2$ , since scaling $x$ by a power of 2 does not alter $x / fl(\sqrt{x^2})$ . By definition, $fl(\sqrt{x^2})$ is the nearest floating point number to $\sqrt{fl(x^2)} = \sqrt{x^2(1 + \delta)}$ , $|\delta| \leq u$ , and

$$
\sqrt {f l (x ^ {2})} = | x | (1 + \delta) ^ {1 / 2} = | x | \left(1 + \frac {\delta}{\sqrt {1 + \delta} + 1}\right) = | x | + \theta .
$$

Now the spacing of the floating point numbers between 1 and 2 is $\epsilon_{M} = 2u$ , so

$$
\left| \theta \right| \leq (2 - 2 u) \frac {u}{\sqrt {1 - u} + 1}.
$$

Hence $|\theta| < u$ if $u \leq \frac{1}{4}$ (say), and then $|x|$ is the nearest floating point number to $\sqrt{fl(x^2)}$ , so that $fl(\sqrt{fl(x^2)}) = |x|$ .

In base 10 floating point arithmetic, the condition $\sqrt{x^2} = |x|$ can be violated. For example, working to 5 significant decimal digits, if $x = 3.1625$ then $fl(x^2) = fl(10.00140625) = 10.001$ , and $fl(\sqrt{10.001}) = fl(3.16243577\dots) = 3.1624 < x$ .

2.21. On a Cray Y-MP the answer is yes, but in base 2 IEEE arithmetic the answer is no. It suffices to demonstrate that $fl(x / \sqrt{x^2}) = \mathrm{sign}(x)$ ( $x \neq 0$ ), which is shown by the proof of Problem 2.20.

2.22. The test " $x > y$ " returns false if $x$ or $y$ is a NaN, so the code computes $\max(\mathrm{NaN}, 5) = 5$ and $\max(5, \mathrm{NaN}) = \mathrm{NaN}$ , which violates the obvious requirement that $\max(x, y) = \max(y, x)$ . Since the test $x \neq x$ identifies a NaN, the following code implements a reasonable definition of $\max(x, y)$ :

$\% \max (x,y)$ if $x\neq x$ then $\begin{array}{r}\max = y \end{array}$ else if $y\neq y$ then $\begin{array}{rl} & {\max = x}\\ & {\mathrm{else~if}y > x\mathrm{then}}\\ & {\max = y}\\ & {\mathrm{else}}\\ & {\max = x}\\ & {\mathrm{end}}\\ & {\mathrm{end}} \end{array}$ end

A further refinement is to ensure that $\max(-0, +0) = +0$ , which is not satisfied by the code above since $-0$ and $+0$ compare as equal; this requires bit-level programming.

2.23. We give an informal proof; the details are obtained by using the model $fl(x \circ p y) = (x \circ p y)(1 + \delta)$ , but they obscure the argument.

Since $a, b$ , and $c$ are nonnegative, $a + (b + c)$ is computed accurately. Since $c \leq b \leq a$ , $c + (a - b)$ and $a + (b - c)$ are the sums of two positive numbers and so are computed

accurately. Since $a, b$ , and $c$ are the lengths of sides of a triangle, $a \leq b + c$ ; hence, using $c \leq b \leq a$ ,

$$
b \leq a \leq b + c \leq 2 b,
$$

which implies that $a - b$ is computed exactly, by Theorem 2.5. Hence $c - (a - b)$ is the difference of two exactly represented numbers and so is computed accurately. Thus $fl(A) = fl\left(\frac{1}{4}\sqrt{\hat{x}}\right)$ , where $\hat{x}$ is an accurate approximation to the desired argument $x$ of the square root. It follows that $fl(A)$ is accurate.

2.24. For a machine with a guard digit, $y = x$ , by Theorem 2.5 (assuming $2x$ does not overflow). If the machine lacks a guard digit then the subtraction produces $x$ if the last bit of $x$ is zero, otherwise it produces an adjacent floating point number with a zero last bit; in either case the result has a zero last bit. Gu, Demmel, and Dhillon [528, 1994] apply this bit zeroing technique to numbers $d_{1}, d_{2}, \ldots, d_{n}$ arising in a divide and conquer bidiagonal SVD algorithm, their motivation being that the differences $d_{i} - d_{j}$ can then be computed accurately even on machines without a guard digit.

2.25. The function $f(x) = 3x - 1$ has the single root $x = 1/3$ . We can have $fl(f(x)) = 0$ only for $x \approx 1/3$ . For $x \approx 1/3$ the evaluation can be summarized as follows:

$$
\begin{array}{l} x - 0. 5 \approx - \frac {1}{6}, \\ - \frac {1}{6} + x \approx \frac {1}{6}, \\ \frac {1}{6} - 0. 5 \approx - \frac {1}{3}, \\ - \frac {1}{3} + x \approx 0. \\ \end{array}
$$

The first, second, and fourth subtractions are done exactly, by Theorem 2.5. The result of the first subtraction has a zero least-significant bit and the result of the second has two zero least-significant bits; consequently the third subtraction suffers no loss of trailing bits and is done exactly. Therefore $f(x)$ is computed exactly for $x \equiv fl(x)$ near $1/3$ . But $fl(x)$ can never equal $1/3$ on a binary machine, so $fl(f(x)) \neq 0$ for all $x$ .

2.26. If $x$ and $y$ are $t$ -digit floating point numbers then $xy$ has $2t - 1$ or $2t$ significant digits. Since the error $fl(xy) - xy$ is less than oneulp in $xy$ (i.e., beyond the $t$ th significant digit), the difference $xy - fl(xy)$ is exactly representable in $t$ digits, and it follows from the definition of FMA that the difference is computed exactly.

2.27. We have

$$
\begin{array}{l} \widehat {w} = b c \left(1 + \delta_ {1}\right), \\ \widehat {e} = (\widehat {w} - b c) (1 + \delta_ {2}), \\ (1 + \delta_ {4}) \widehat {x} = (a d - \widehat {w}) (1 + \delta_ {3}) + \widehat {e}, \\ \end{array}
$$

where $|\delta_i| \leq u$ , $i = 1:4$ . Hence

$$
(1 + \delta_ {4}) \widehat {x} = (a d - b c - b c \delta_ {1}) (1 + \delta_ {3}) + b c \delta_ {1} (1 + \delta_ {2}) = x + x \delta_ {3} - b c \delta_ {1} (\delta_ {3} - \delta_ {2}),
$$

so that

$$
\left| x - \widehat {x} \right| \leq u \left(\left| x \right| + \left| \widehat {x} \right|\right) + 2 u ^ {2} | b c |,
$$

which implies high relative accuracy unless $u|bc| \gg |x|$ . For comparison, the bound for standard evaluation of $fl(ad - bc)$ is $|x - \widehat{x}| \leq \gamma_2(|ad| + |bc|)$ .

2.28. We would like (2.8) to be satisfied, that is, we want $\widehat{z} = fl(x / y)$ to satisfy

$$
\widehat {z} = (x / y) (1 + \delta) + \eta , \quad | \delta | \leq u, \quad | \eta | \leq \lambda u. \tag {A.2}
$$

This implies that

$$
\left| \widehat {z} y - x \right| = \left| x \delta + \eta y \right| \leq u | x | + \lambda u | y |.
$$

In place of $r = \widehat{z} y - x$ we have to use $\widehat{r} = fl(\widehat{z} y - x) = \widehat{z} y(1 + \epsilon) - x$ , where $|\epsilon| \leq u$ , and where we can assume the subtraction is exact, since the case of interest is where $\widehat{z} y \approx x$ (see Theorem 2.5). Thus $|\widehat{r}| = |r + \widehat{z} y\epsilon| \leq |r| + u|\widehat{z}||y|$ , and bounding $|\widehat{z}||y|$ using (A.2) we obtain

$$
\left| \widehat {r} \right| \leq | r | + u (1 + u) | x | + \lambda u ^ {2} | y | \approx | r | + u | x |.
$$

Therefore the convergence test is

$$
| \widehat {r} | \leq 2 u | x | + \lambda u | y |.
$$

Since $\lambda u$ underflows to zero it cannot be precomputed, and we should instead compute $\lambda(u|y|$

3.1. The proof is by induction. Inductive step: for $\rho_{n} = +1$

$$
\begin{array}{l} \prod_ {i = 1} ^ {n} (1 + \delta_ {i}) = (1 + \delta_ {n}) (1 + \theta_ {n - 1}) = 1 + \theta_ {n}, \\ \theta_ {n} = \delta_ {n} + (1 + \delta_ {n}) \theta_ {n - 1}, \\ \left| \theta_ {n} \right| \leq u + (1 + u) \frac {(n - 1) u}{1 - (n - 1) u} \\ = \frac {u (1 - (n - 1) u) + (1 + u) (n - 1) u}{1 - (n - 1) u} \\ = \frac {n u}{1 - (n - 1) u} \leq \gamma_ {n}. \\ \end{array}
$$

For $\rho_{n} = -1$ we find, similarly, that

$$
| \theta_ {n} | \leq \frac {n u - (n - 1) u ^ {2}}{1 - n u + (n - 1) u ^ {2}} \leq \gamma_ {n}.
$$

3.2. This result can be proved by a modification of the proof of Lemma 3.1. But it follows immediately from the penultimate line of the proof of Lemma 3.4.

3.3. The computed iterates $\widehat{q}_k$ satisfy

$$
(1 + \delta_ {k}) \widehat {q} _ {k} = a _ {k} + \frac {b _ {k}}{\widehat {q} _ {k + 1}} (1 + \epsilon_ {k}), \quad | \delta_ {k} |, | \epsilon_ {k} | \leq u.
$$

Defining $\widehat{q}_k = q_k + e_k$ , we have

$$
\begin{array}{l} q _ {k} + e _ {k} + \delta_ {k} \widehat {q} _ {k} = a _ {k} + \frac {b _ {k}}{q _ {k + 1} + e _ {k + 1}} + \frac {b _ {k} \epsilon_ {k}}{\widehat {q} _ {k + 1}} \\ = a _ {k} + \frac {b _ {k}}{q _ {k + 1}} - \frac {b _ {k} e _ {k + 1}}{q _ {k + 1} \left(q _ {k + 1} + e _ {k + 1}\right)} + \frac {b _ {k} \epsilon_ {k}}{\widehat {q} _ {k + 1}}. \\ \end{array}
$$

This gives

$$
\left| e _ {k} \right| \leq u \left| \widehat {q} _ {k} \right| + \frac {\left| b _ {k} \right| \left| e _ {k + 1} \right|}{\left(\left| \widehat {q} _ {k + 1} \right| - \left| e _ {k + 1} \right|\right) \left| \widehat {q} _ {k + 1} \right|} + u \frac {\left| b _ {k} \right|}{\left| \widehat {q} _ {k + 1} \right|}.
$$

The running error bound $\mu$ can therefore be computed along with the continued fraction as follows:

$$
\begin{array}{l} q _ {n + 1} = a _ {n + 1} \\ f _ {n + 1} = 0 \\ f o r k = n: - 1: 0 \\ r _ {k} = b _ {k} / q _ {k + 1} \\ q _ {k} = a _ {k} + r _ {k} \\ f _ {k} = \left| q _ {k} \right| + \left| r _ {k} \right| + \left| b _ {k} \right| f _ {k + 1} / \left(\left| q _ {k + 1} - u f _ {k + 1} \right|\right) \left| q _ {k + 1} \right|) \\ e n d \\ \mu = u f _ {0} \\ \end{array}
$$

The error bound is valid provided that $|q_{k + 1}| - uf_{k + 1} > 0$ for all $k$ . Otherwise a more sophisticated approach is necessary (for example, to handle the case where $q_{k + 1} = 0$ , $q_k = \infty$ , and $q_{k - 1}$ is finite).

3.4. We prove just the division result and the last result. Let $(1 + \theta_{k}) / (1 + \theta_{j}) = 1 + \alpha$ . Then $\alpha = (\theta_{k} - \theta_{j}) / (1 + \theta_{j})$ , so

$$
\begin{array}{l} | \alpha | \leq \frac {\frac {k u}{1 - k u} + \frac {j u}{1 - j u}}{1 - \frac {j u}{1 - j u}} = \frac {(k + j) u - 2 k j u ^ {2}}{(1 - 2 j u) (1 - k u)} \\ = \frac {(k + j) u - 2 k j u ^ {2}}{1 - (2 j + k) u + 2 j k u ^ {2}} \leq \frac {(k + j) u}{1 - (2 j + k) u} \leq \gamma_ {k + 2 j}. \\ \end{array}
$$

However, it is easy to verify that, in fact,

$$
\frac {(k + j) u - 2 k j u ^ {2}}{(1 - 2 j u) (1 - k u)} \leq \frac {(k + j) u}{1 - (k + j) u}
$$

if $j\leq k$

For the last result,

$$
\begin{array}{l} \gamma_ {k} + \gamma_ {j} + \gamma_ {k} \gamma_ {j} = \frac {k u (1 - j u) + j u (1 - k u) + k j u ^ {2}}{(1 - k u) (1 - j u)} \\ = \frac {(k + j) u - k j u ^ {2}}{1 - (k + j) u + k j u ^ {2}} \\ <   \frac {(k + j) u}{1 - (k + j) u} = \gamma_ {k + j}. \\ \end{array}
$$

3.5. We have $fl(AB) = AB + \Delta C = (A + \Delta CB^{-1})B =: (A + \Delta A)B$ , where $\Delta A = \Delta CB^{-1}$ , and $|\Delta C| \leq \gamma_n |A||B|$ by (3.13). Similarly, $fl(AB) = A(B + \Delta B)$ , $|\Delta B| \leq \gamma_n |A^{-1}||A||B|$ .

3.6. We have

$$
\left| R \right| = \left| A \Delta B + \Delta A B + \Delta A \Delta B \right| \leq 2 \epsilon E F + \epsilon^ {2} E F,
$$

which implies

$$
\epsilon^ {2} g _ {i j} + 2 \epsilon g _ {i j} - | r _ {i j} | \geq 0 \quad \text {f o r a l l} i, j.
$$

Solving these inequalities for $\epsilon$ gives the required lower bound.

The definition is flawed in general as can be seen from rank considerations. For example if $A$ and $B$ are vectors and $\operatorname{rank}(C) \neq 1$ , then no perturbations $\Delta A$ and $\Delta B$ exist to satisfy $C = (A + \Delta A)(B + \Delta B)!$ . Thus we have to use a mixed forward/backward stability definition in which we perturb $C$ by at most $\epsilon$ as well as $A$ and $B$ .

3.7. Lemma 3.5 shows that (3.2) holds provided that each $(1 + \delta)^{k}$ product is replaced by $(1 + \epsilon)(1 + \delta)^{k - 1}$ , where $|\epsilon| \leq \sqrt{2}\gamma_{2}$ , where the $1 + \epsilon$ corresponds to a multiplication $x_{i}y_{i}$ . Thus we have

$$
\widehat {S} _ {n} = \sum_ {i = 1} ^ {n} x _ {i} y _ {i} (1 + \alpha_ {i}), \quad \text {w h e r e} \quad 1 + \alpha_ {i} = (1 + \theta_ {n - 1} ^ {(i)}) (1 + \epsilon_ {i}).
$$

It is easy to show that $|\alpha_i| \leq \gamma_{n+2}$ , so the only change required in (3.4) is to replace $\gamma_n$ by $\gamma_{n+2}$ . The complex analogue of (3.11) is $\widehat{y} = (A + \Delta A)x$ , $|\Delta A| \leq \gamma_{n+2}|A|$ .

3.8. We have $fl((x + y)(x - y)) = (x + y)(x - y)(1 + \theta_3), |\theta_3| \leq \gamma_3 = 3u / (1 - 3u)$ , so the computed result has small relative error. Moreover, if $y / 2 \leq x \leq y$ then $x - y$ is computed exactly, by Theorem 2.5, hence $fl((x + y)(x - y)) = (x + y)(x - y)(1 + \theta_2)$ . However, $fl(x^2 - y^2) = x^2(1 + \theta_2) - y^2(1 + \theta_2')$ , so that

$$
\left| \frac {f l (x ^ {2} - y ^ {2}) - (x ^ {2} - y ^ {2})}{x ^ {2} - y ^ {2}} \right| = \left| \frac {x ^ {2} \theta_ {2} - y ^ {2} \theta_ {2} ^ {\prime}}{x ^ {2} - y ^ {2}} \right| \leq \gamma_ {2} \frac {x ^ {2} + y ^ {2}}{| x ^ {2} - y ^ {2} |},
$$

and we cannot guarantee a small relative error.

If $|x| \gg |y|$ then $fl(x^2 - y^2)$ suffers only two rounding errors, since the error in forming $fl(y^2)$ will not affect the final result, while $fl((x + y)(x - y))$ suffers three rounding errors; in this case $fl(x^2 - y^2)$ is likely to be the more accurate result.

3.9. Assume the result is true for $m - 1$ . Now

$$
\prod_ {j = 0} ^ {m} (X _ {j} + \varDelta X _ {j}) = (X _ {m} + \varDelta X _ {m}) \prod_ {j = 0} ^ {m - 1} (X _ {j} + \varDelta X _ {j}),
$$

so

$$
\begin{array}{l} \left\| \prod_ {j = 0} ^ {m} (X _ {j} + \varDelta X _ {j}) - \prod_ {j = 0} ^ {m} X _ {j} \right\| = \left\| X _ {m} \left[ \prod_ {j = 0} ^ {m - 1} (X _ {j} + \varDelta X _ {j}) - \prod_ {j = 0} ^ {m - 1} X _ {j} \right] \right. \\ + \Delta X _ {m} \prod_ {j = 0} ^ {m - 1} \left(X _ {j} + \Delta X _ {j}\right) \Bigg \| \\ \leq \left\| X _ {m} \right\| \left(\prod_ {j = 0} ^ {m - 1} \left(1 + \delta_ {j}\right) - 1\right) \prod_ {j = 0} ^ {m - 1} \left\| X _ {j} \right\| \\ + \delta_ {m} \| X _ {m} \| _ {2} \prod_ {j = 0} ^ {m - 1} \left(\| X _ {j} \| \left(1 + \delta_ {j}\right)\right) \\ = \left(\prod_ {j = 0} ^ {m} (1 + \delta_ {j}) - 1\right) \prod_ {j = 0} ^ {m} \| X _ {j} \|. \\ \end{array}
$$

3.10. Without loss of generality we can suppose that the columns of the product are computed one at a time. With $x_{j} = A_{1}\ldots A_{k}e_{j}$ we have, using (3.11),

$$
f l \left(x _ {j}\right) = \left(A _ {1} + \Delta A _ {1}\right) \dots \left(A _ {k} + \Delta A _ {k}\right) e _ {j}, \quad \| \Delta A _ {i} \| _ {2} \leq \sqrt {n} \gamma_ {n} \| A _ {i} \| _ {2},
$$

and so, by Lemma 3.6,

$$
\left\| x _ {j} - f l \left(x _ {j}\right) \right\| _ {2} \leq \left[ \left(1 + \sqrt {n} \gamma_ {n}\right) ^ {k} - 1 \right] \left\| A _ {1} \right\| _ {2} \dots \left\| A _ {k} \right\| _ {2}.
$$

Squaring these inequalities and summing over $j$ yields

$$
\left\| A _ {1} \dots A _ {k} - f l (A _ {1} \dots A _ {k}) \right\| _ {F} \leq \sqrt {n} \bigl [ \bigl (1 + \sqrt {n} \gamma_ {n} \bigr) ^ {k} - 1 \bigr ] \| A _ {1} \| _ {2} \dots \| A _ {k} \| _ {2},
$$

which gives the result.

3.11. The computations can be expressed as

$$
\begin{array}{l} y _ {1} = x ^ {2} \\ y _ {i + 1} = \sqrt {y _ {i}}, i = 1: m \\ z _ {1} = y _ {m + 1} \\ z _ {i + 1} = z _ {i} ^ {2}, i = 1: m - 1 \\ \end{array}
$$

We have

$$
\begin{array}{l} \widehat {y} _ {1} = x ^ {2} \left(1 + \delta_ {0}\right) \\ \widehat {y} _ {i + 1} = \sqrt {\widehat {y} _ {i}} (1 + \delta_ {i}), i = 1: m \\ \widehat {z} _ {1} = \widehat {y} _ {m + 1} \\ \widehat {z} _ {i + 1} = \widehat {z} _ {i} ^ {2} (1 + \epsilon_ {i}), i = 1: m - 1 \\ \end{array}
$$

where $|\delta_i|, |\epsilon_i| \leq u$ . Solving these recurrences, we find that

$$
\widehat {y} _ {m + 1} = \left(1 + \delta_ {m}\right) \left(1 + \delta_ {m - 1}\right) ^ {1 / 2} \left(1 + \delta_ {m - 2}\right) ^ {1 / 4} \dots \left(1 + \delta_ {0}\right) ^ {1 / 2 ^ {m}} y _ {1} ^ {1 / 2 ^ {m}}.
$$

It follows that

$$
(1 - u) ^ {2} y _ {1} ^ {\frac {1}{2 ^ {m}}} \leq \widehat {y} _ {m + 1} \leq (1 + u) ^ {2} y _ {1} ^ {\frac {1}{2 ^ {m}}},
$$

which shows that $\widehat{y}_{m+1}$ differs negligibly from $y_{m+1}$ . For the repeated squarings, however, we find that

$$
\begin{array}{l} \widehat {z} _ {m} = (1 + \epsilon_ {m - 1}) (1 + \epsilon_ {m - 2}) ^ {2} (1 + \epsilon_ {m - 3}) ^ {4} \dots (1 + \epsilon_ {1}) ^ {2 ^ {m - 1}} \widehat {z} _ {1} ^ {2 ^ {m - 1}} \\ = \left(1 + \theta_ {2 ^ {m} - 1}\right) \widehat {z} _ {1} ^ {2 ^ {m - 1}} = \left(1 + \theta_ {2 ^ {m} + 1}\right) | x |, \\ \end{array}
$$

where we have used Lemma 3.1. Hence the squarings introduce a relative error that can be approximately as large as $2^{m}u$ . Since $u = 2^{-53}$ , this relative error is of order 0.1 for $m = 50$ , which explains the observed results for $m = 50$ .

3.12. The analysis is just a slight extension of that for an inner product. The analogue of (3.3) is

$$
\begin{array}{l} \widehat {J} (f) = w _ {1} f \left(x _ {1}\right) \left(1 + \eta_ {1}\right) \left(1 + \theta_ {n}\right) + w _ {2} f \left(x _ {2}\right) \left(1 + \eta_ {2}\right) \left(1 + \theta_ {n} ^ {\prime}\right) \\ + w _ {3} f \left(x _ {3}\right) \left(1 + \eta_ {3}\right) \left(1 + \theta_ {n - 1}\right) + \dots + w _ {n} f \left(x _ {n}\right) \left(1 + \eta_ {n}\right) \left(1 + \theta_ {2}\right). \\ \end{array}
$$

Hence

$$
\left| I (f) - \widehat {J} (f) \right| \leq \left(\eta + \gamma_ {n} + \eta \gamma_ {n}\right) \sum_ {i = 1} ^ {n} \left| w _ {i} \right| | f (x _ {i}) |.
$$

Setting $M = \max \{|f(x)| : a \leq x \leq b\}$ , we have

$$
\left| I (f) - \widehat {J} (f) \right| \leq M \left(\eta + \gamma_ {n} + \eta \gamma_ {n}\right) \sum_ {i = 1} ^ {n} | w _ {i} |. \tag {A.3}
$$

Any reasonable quadrature rule designed for polynomial $f$ has $\sum_{i=1}^{n} w_i = b - a$ , so one implication of (A.3) is that it is best not to have weights of large magnitude and varying sign; ideally, $w_i \geq 0$ for all $i$ (as for Gaussian integration rules, for example), so that $\sum_{i=1}^{n} |w_i| = b - a$ .

4.1. A condition number is

$$
C (x) = \operatorname * {m a x} \left\{\left| \frac {S _ {n} (x) - S _ {n} (x + \varDelta x)}{\epsilon S _ {n} (x)} \right|: | \varDelta x | \leq \epsilon | x | \right\}.
$$

It is easy to show that

$$
C (x) = \frac {S _ {n} (| x |)}{| S _ {n} (x) |} = \frac {\sum_ {i = 1} ^ {n} | x _ {i} |}{\left| \sum_ {i = 1} ^ {n} x _ {i} \right|}.
$$

The condition number is 1 if the $x_{i}$ all have the same sign.

4.2. In the $(i - 1)\mathrm{st}$ floating point addition the “ $2^{k - t}$ ” portion of $x_{i}$ does not propagate into the sum (assuming that the floating point arithmetic uses round to nearest with ties broken by rounding to an even last bit or rounding away from zero), thus there is an error of $2^{k - t}$ and $\widehat{S}_i = i$ . The total error is

$$
2 ^ {- t} (1 + 2 ^ {2} + 2 ^ {4} + \dots + 2 ^ {2 (r - 1)}) = 2 ^ {- t} \frac {4 ^ {r} - 1}{3},
$$

while the upper bound of (4.4) is

$$
(n - 1) u \sum_ {i = 1} ^ {n} | x _ {i} | + O (u ^ {2}) \leq 2 ^ {r} 2 ^ {- t} 2 ^ {r} + O (2 ^ {- 2 t}) \approx 2 ^ {- t} 4 ^ {r},
$$

which agrees with the actual error to within a factor 3; thus the smaller upper bound of (4.3) is also correct to within this factor. The example just quoted is, of course, a very special one, and as Wilkinson [1232, 1963, p. 20] explains, "in order to approach the upper bound as closely as this, not only must each error take its maximum value, but all the terms must be almost equal."

4.3. With $S_{k} = \sum_{i = 1}^{k}x_{i}$ , we have

$$
\widehat {S} _ {k} = f l \left(\widehat {S} _ {k - 1} + x _ {k}\right) = \left(\widehat {S} _ {k - 1} + x _ {k}\right) \left(1 + \delta_ {k}\right), \quad | \delta_ {k} | \leq u, \quad k = 2: n.
$$

By repeated use of this relation it follows that

$$
\widehat {S} _ {n} = \left(x _ {1} + x _ {2}\right) \prod_ {k = 2} ^ {n} (1 + \delta_ {k}) + \sum_ {i = 3} ^ {n} x _ {i} \prod_ {k = i} ^ {n} (1 + \delta_ {k}),
$$

which yields the required expression for $\widehat{S}_n$ . The bound on $|E_n|$ is immediate.

The bound is minimized if the $x_{i}$ are in increasing order of absolute value. This observation is common in the literature and it is sometimes used to conclude that the increasing ordering is the best one to use. This reasoning is fallacious, because minimizing an error bound is not the same as minimizing the error itself. As (4.3) shows, if we know nothing about the signs of the rounding errors then the "best" ordering to choose is one that minimizes the partial sums.

4.4. Any integer between 0 and 10 inclusive can be produced. For example, $fl(1 + 2 + 3 + 4 + M - M) = 0$ , $fl(M - M + 1 + 2 + 3 + 4) = 10$ , and $fl(2 + 3 + M - M + 1 + 4) = 5$ .

4.5. This method is sometimes promoted on the basis of the argument that it minimizes the amount of cancellation in the computation of $S_{n}$ . This is incorrect: the “±” method does not reduce the amount of cancellation—it simply concentrates all the cancellation into one step. Moreover, cancellation is not a bad thing per se, as explained in §1.7.

The “ $\pm$ ” method is an instance of Algorithm 4.1 (assuming that $S_{+}$ and $S_{-}$ are computed using Algorithm 4.1) and it is easy to see that it maximizes $\max_i |T_i|$ over all methods of this form (where, as in §4.2, $T_i$ is the sum computed at the $i$ th stage). Moreover, when $\sum_{i=1}^{n} |x_i| \gg |\sum_{i=1}^{n} x_i|$ the value of $\max_i |T_i|$ tends to be much larger for the “ $\pm$ ” method than for the other methods we have considered.

4.6. Suppose, without loss of generality, that $|a| \geq |b|$ . By definition, $fl(a + b)$ solves $\min |(a + b) - x|$ over all floating point numbers $x$ . Since $a$ is a floating point number,

$$
\operatorname {e r r} (a, b) \leq | (a + b) - a | = | b |,
$$

which gives the first part. Now the least significant nonzero bit of $\mathrm{err}(a,b)$ is no smaller than 1ulp in $b$ (cf. Figure 4.1), and by the first part, $|\mathrm{err}(a,b)|\leq |b|$ . Hence the significand of $\mathrm{err}(a,b)$ is no longer than that of $b$ , which means that it is representable as a floating point number in the absence of overflow.

4.7. The main concern is to evaluate the denominator accurately when the $x_{i}$ are close to convergence. The bound (4.3) tells us to minimize the partial sums; these are, approximately, for $x_{i} \approx \xi$ , (a) $-\xi$ , 0, (b) 0, 0, (c) $2\xi$ , 0. Hence the error analysis of summation suggests that (b) is the best expression, with (a) a distant second. That (b) is the best choice is confirmed by Theorem 2.5, which shows there will be only one rounding error when the $x_{i}$ are close to convergence. A further reason to prefer (b) is that it is less prone to overflow than (a) and (c).

4.8. This is, of course, not a practical method, not least because it is very prone to overflow and underflow. However, its error analysis is interesting. Ignoring the error in the log evaluation, and assuming that exp is evaluated with relative error bounded by $u$ , we have, with $|\delta_i| \leq u$ for all $i$ , and for some $\delta_{2n}$

$$
\begin{array}{l} \widehat {S} _ {n} = \log \left(e ^ {x _ {1}} \dots e ^ {x _ {n}} \left(1 + \delta_ {1}\right) \dots \left(1 + \delta_ {2 n - 1}\right)\right) \\ = \log \left(e ^ {x _ {1}} \dots e ^ {x _ {n}} \left(1 + \delta_ {2 n}\right) ^ {2 n - 1}\right) \\ = x _ {1} + \dots + x _ {n} + (2 n - 1) \log (1 + \delta_ {2 n}) \\ \approx x _ {1} + \dots + x _ {n} + (2 n - 1) \delta_ {2 n}. \\ \end{array}
$$

Hence the best relative error bound we can obtain is $|S_{n} - \widehat{S}_{n}| / |S_{n}| \lesssim (2n - 1)u / |S_{n}|$ . Clearly, this method of evaluation guarantees a small absolute error, but not a small relative error when $|S_{n}| \ll 1$ .

4.9. Method (a) is recursive summation of $a, h, h, \ldots, h$ . From (4.3) we have $|a + i\widehat{h} - \widehat{x}_i| \leq [ia + \frac{1}{2} i(i + 1)\widehat{h}]u + O(u^2)$ . Hence, since $\widehat{h} = h(1 + \epsilon), |\epsilon| \leq u$ ,

$$
\begin{array}{l} \left| x _ {i} - \widehat {x} _ {i} \right| \leq | i h - i \widehat {h} | + | a + i \widehat {h} - \widehat {x} _ {i} | \leq i h u + i (| a | + \frac {1}{2} (i + 1) h) u + O \left(u ^ {2}\right) \\ = i (| a | + \frac {1}{2} (i + 3) h) u + O \left(u ^ {2}\right). \\ \end{array}
$$

For (b), using the relative error counter notation (3.10), $\widehat{x}_i = (a + i\widehat{h} < 1) < 1 > = a < 1 > + ih < 3 >$ . Hence

$$
\left| x _ {i} - \widehat {x} _ {i} \right| \leq u | a | + \gamma_ {3} i h.
$$

For (c), $\widehat{x}_i = a(1 - < 1 > i / n) < 2 > + (i / n)b < 3>$ , hence

$$
\left| x _ {i} - \widehat {x} _ {i} \right| \leq \gamma_ {2} | a | + \gamma_ {3} | a | i / n + \gamma_ {3} | b | i / n \leq \gamma_ {3} \big (\left| a \right| (1 + i / n) + \left| b \right| i / n \big).
$$

The error bound for (b) is about a factor $i$ smaller than that for (a). Note that method (c) is the only one guaranteed to yield $\widehat{x}_n = b$ (assuming $fl(n / n) = 1$ , as holds in IEEE arithmetic), which may be important when integrating a differential equation to a given end-point.

If $a \geq 0$ then the bounds imply

(a): $|x_i - \widehat{x}_i| \lesssim iu|x_i|$ ,

(b): $|x_{i} - \widehat{x}_{i}| \leq \gamma_{3}|x_{i}|$ ,

(c): $|x_{i} - \widehat{x}_{i}| \leq \gamma_{3}(a + i / n(a + b)) = \gamma_{3}(a + i / n(b - a + 2a))$

$$
= \gamma_ {3} (a + i h + 2 a i / n) \leq 3 \gamma_ {3} | x _ {i} |.
$$

Thus (b) and (c) provide high relative accuracy for all $i$ , while the relative accuracy of (a) can be expected to degrade as $i$ increases.

5.1. By differentiating the Horner recurrence $q_{i} = xq_{i + 1} + a_{i}$ , $q_{n} = a_{n}$ , we obtain

$$
q _ {i} ^ {\prime} = x q _ {i + 1} ^ {\prime} + q _ {i + 1}, \quad q _ {n} ^ {\prime} = 0, \quad q _ {n - 1} ^ {\prime} = a _ {n},
$$

$$
q _ {i} ^ {\prime \prime} = x q _ {i + 1} ^ {\prime \prime} + 2 q _ {i + 1} ^ {\prime}, \quad q _ {n} ^ {\prime \prime} = q _ {n - 1} ^ {\prime \prime} = 0, \quad q _ {n - 2} ^ {\prime \prime} = 2 a _ {n},
$$

$$
q _ {i} ^ {\prime \prime \prime} = x q _ {i + 1} ^ {\prime \prime \prime} + 3 q _ {i + 1} ^ {\prime \prime}, \quad q _ {n} ^ {\prime \prime \prime} = q _ {n - 1} ^ {\prime \prime \prime} = q _ {n - 2} ^ {\prime \prime \prime} = 0, \quad q _ {n - 3} ^ {\prime \prime \prime} = 6 a _ {n}.
$$

The factors 2, 3, ..., can be removed by redefining $r_i^{(k)} = q_i^{(k)} / k!$ . Then $r_i^{(k)} = x r_{i+1}^{(k)} + r_{i+1}^{(k-1)}$ , $r_{n-k}^{(k)} = a_n$ .

5.2. Analysis similar to that for Horner's rule shows that

$$
f l (p (x)) = a _ {0} <   n > + a _ {1} x <   n + 1 > + \dots + a _ {n} x ^ {n} <   n + 1 >.
$$

The total number of rounding errors is the same as for Horner's algorithm, but they are distributed more equally among the terms of the polynomial. Horner's rule can be expected to be more accurate when the terms $|a_{i}x^{i}|$ decrease rapidly with $i$ , such as when $p(x)$ is the truncation of a rapidly convergent power series. Of course, this algorithm requires twice as many multiplications as Horner's method.

5.3. Accounting for the error in forming $y$ , we have, using the relative error counter notation (3.10),

$$
\begin{array}{l} f l (p (x)) = \left\lceil a _ {0} <   1 > + a _ {2} x ^ {2} <   4 > + \dots + a _ {n - 2} x ^ {n - 2} <   3 m - 2 > + a _ {n} x ^ {n} <   3 m > \left. \right. \\ + x <   1 > \left(a _ {1} <   1 > + a _ {3} x ^ {2} <   4 > + \dots + a _ {2 n - 1} x ^ {2 n - 1} <   3 m - 3 >\right) ] <   1 > \\ = \sum_ {i = 0} ^ {n} a _ {i} x ^ {i} \left(1 + \theta_ {3 m + 1} ^ {(i)}\right), \quad \left| \theta_ {3 m + 1} ^ {(i)} \right| \leq \gamma_ {3 m + 1}. \\ \end{array}
$$

Thus the relative backward perturbations are bounded by $(3n / 2 + 1)u$ instead of $2nu$ for Horner's rule.

5.4. Here is a MATLAB M-file to perform the task.

```matlab
function [a, perm] = leja(a)  
%LEJA LEJA ordering.  
% [A, PERM] = LEJA(A) reorders the points A by the  
% Leja ordering and returns the permutation vector that  
% effects the ordering in PERM. 
```

```matlab
n = max(size(a));  
perm = (1:n)';  
% a(1) = max(abs(a)).  
[t, i] = max(abs(a));  
if i ~ = 1  
    a([1 i]) = a([i 1]);  
    perm([1 i]) = perm([i 1]);  
end 
```

```matlab
p = ones(n,1);  
for k=2:n-1  
    for i=k:n 
```

$\begin{array}{rl} & {\mathrm{p(i)} = \mathrm{p(i)*(a(i) - a(k - 1))};}\\ & {\mathrm{end}}\\ & {\mathrm{[t,i] = max(abs(p(k:n)))};}\\ & {\mathrm{i = i + k - 1};}\\ & {\mathrm{if~i~\sim = ~k}}\\ & {\mathrm{a([k~i]) = a([i~k])};}\\ & {\mathrm{p([k~i]) = p([i~k])};}\\ & {\mathrm{perm([k~i]) = perm([i~k])};}\\ & {\mathrm{end}}\\ & {\mathrm{end}} \end{array}$ $\begin{array}{r l} & {\mathrm{i} = \mathrm{i} + \mathrm{k} - 1;}\\ & {\mathrm{if~i~\sim = ~k}}\\ & {\mathrm{a([k~i]) = a([i~k])};}\\ & {\mathrm{p([k~i]) = p([i~k])};}\\ & {\mathrm{perm([k~i]) = perm([i~k])};}\\ & {\mathrm{end}} \end{array}$

5.5. It is easy to show that the computed $\widehat{p}$ satisfies $\widehat{p} = p(x)(1 + \theta_{2n + 1}), |\theta_{2n + 1}| \leq \gamma_{2n + 1}$ . Thus $\widehat{p}$ has a tiny relative error. Of course, this assumes that the roots $x_i$ are known exactly!

6.1. For $\alpha_{S,2}$ , if $A \in \mathbb{C}^{m \times n}$ then, using the Cauchy-Schwarz inequality,

$$
\| A \| _ {S} ^ {2} = \left(\sum_ {i, j} | a _ {i j} |\right) ^ {2} \leq m n \| A \| _ {F} ^ {2} \leq m n \operatorname {r a n k} (A) \| A \| _ {2} ^ {2}.
$$

The first inequality is an equality iff $|a_{ij}| \equiv \alpha$ , and the second inequality is an equality iff $A$ is a multiple of a matrix with orthonormal columns. If $A$ is real and square, these requirements are equivalent to $A$ being a scalar multiple of a Hadamard matrix. If $A$ is complex and square, the requirements are satisfied by the given Vandermonde matrix, which is $\sqrt{n}$ times a unitary matrix.

6.2. $\| xy^{*}\| = \max_{\| z\| = 1}\| xy^{*}z\| = \| x\| \max_{\| z\| = 1}|y^{*}z| = \| x\| \| y\| _D.$   
6.3. By the Hölder inequality,

$$
\operatorname {R e} y ^ {*} A x \leq \left| y ^ {*} A x \right| \leq \| y \| _ {D} \| A \| \| x \|. \tag {A.4}
$$

We now show that equality is possible throughout (A.4). Let $x$ satisfy $\| A \| = \| Ax \| / \| x \|$ and let $y$ be dual to $Ax$ . Then

$$
\operatorname {R e} y ^ {*} A x = y ^ {*} A x = \left\| y \right\| _ {D} \left\| A x \right\| = \left\| y \right\| _ {D} \left\| A \right\| \left\| x \right\|,
$$

as required. The last part follows by applying this equality to $A^{*}$ and using the fact that the dual of the dual vector norm is the original norm.

6.4. From (6.19) we have $\| M_n\| _p\leq \mu_n^{1 / p}\mu_n^{1 - 1 / p} = \mu_n$ . But by taking $x$ in the definition (6.11) to be the vector of all ones, we see that $\| M_n\| _p\geq \mu_n$ .

6.5. If $A = PDQ^{*}$ is an SVD then

$$
\begin{array}{l} \| A B \| _ {F} = \left\| P D Q ^ {*} B \right\| _ {F} = \left\| D Q ^ {*} B \right\| _ {F} \\ \leq \left\| \operatorname {d i a g} \left(\max  _ {i} \sigma_ {i}\right) Q ^ {*} B \right\| _ {F} = \left(\max  _ {i} \sigma_ {i}\right) \| Q ^ {*} B \| _ {F} \\ = \| A \| _ {2} \| B \| _ {F}. \\ \end{array}
$$

Similarly, $\| BC\| _F\leq \| B\| _F\| C\| _2$ , and these two inequalities together imply the required one.

6.6. By (6.6) and (6.8) it suffices to show that $\| A^{-1}\|_{\beta ,\alpha} = (\min_{x\neq 0}\| Ax\|_{\beta} / \| x\|_{\alpha})^{-1}$ . We have

$$
\begin{array}{l} \| A ^ {- 1} \| _ {\beta , \alpha} = \max  _ {x \neq 0} \frac {\| A ^ {- 1} x \| _ {\alpha}}{\| x \| _ {\beta}} \\ = \max  _ {y \neq 0} \frac {\| y \| _ {\alpha}}{\| A y \| _ {\beta}} \quad (y = A ^ {- 1} x) \\ = \left(\min  _ {x \neq 0} \| A x \| _ {\beta} / \| x \| _ {\alpha}\right) ^ {- 1}. \\ \end{array}
$$

6.7. Let $\lambda$ be an eigenvalue of $A$ and $x$ the corresponding eigenvector, and form the matrix $X = [x,x,\ldots ,x]\in \mathbb{C}^{n\times n}$ . Then $AX = \lambda X$ , so $|\lambda |\| X\| = \| AX\| \leq \| A\| \| X\|$ , showing that $|\lambda |\leq \| A\|$ . For a subordinate norm it suffices to take norms in the equation $Ax = \lambda x$ .

6.8. The following proof is much simpler than the usual proof based on diagonal scaling to make the off-diagonal of the Jordan matrix small (see, e.g., Horn and Johnson [636, 1985, Lem. 5.6.10]). The proof is from Ostrowski [909, 1973, Thm. 19.3].

Let $\delta^{-1}A$ have the Jordan canonical form $\delta^{-1}A = XJX^{-1}$ . We can write $J = \delta^{-1}D + N$ , where $D = \mathrm{diag}(\lambda_i)$ and the $\lambda_{i}$ are the eigenvalues of $A$ . Then $A = X(D + \delta N)X^{-1}$ , so

$$
\| A \| := \| X ^ {- 1} A X \| _ {\infty} = \| D + \delta N \| _ {\infty} \leq \rho (A) + \delta .
$$

Note that we actually have $\| A \| = \rho(A) + \delta$ if the largest eigenvalue occurs in a Jordan block of size greater than 1. If $A$ is diagonalizable then with $\delta = 0$ we get $\| A \| = \rho(A)$ . The last part of the result is trivial.

6.9. We have $\| A \|_2 \leq \| A \|_F \leq \sqrt{n} \| A \|_2$ (in fact, we can replace $\sqrt{n}$ by $\sqrt{r}$ , where $r = \operatorname{rank}(A)$ ). There is equality on the left when $\sigma_2 = \dots = \sigma_n = 0$ , that is, when $A$ has rank 1 ( $A = xy^*$ ) or $A = 0$ . There is equality on the right when $\sigma_1 = \dots = \sigma_n = \alpha$ , that is, when $A = \alpha Q$ where $Q$ has orthonormal columns, $\alpha \in \mathbb{C}$ .

6.10. Let $F = P\Sigma Q^{*}$ be an SVD. Then

$$
\left\| \left[ \begin{array}{c c} I & F \\ 0 & I \end{array} \right] \right\| _ {2} = \left\| \left[ \begin{array}{c c} P & 0 \\ 0 & Q \end{array} \right] \left[ \begin{array}{c c} I & \Sigma \\ 0 & I \end{array} \right] \left[ \begin{array}{c c} P ^ {*} & 0 \\ 0 & Q ^ {*} \end{array} \right] \right\| _ {2} = \left\| \left[ \begin{array}{c c} I & \Sigma \\ 0 & I \end{array} \right] \right\| _ {2}.
$$

But $\left[ \begin{array}{cc}I & \Sigma \\ 0 & I \end{array} \right]$ can be permuted into the form $\mathrm{diag}(D_i)$ , where $D_{i} = \left[ \begin{array}{cc}1 & \sigma_{i}\\ 0 & 1 \end{array} \right]$ . It is easy to find the singular values of $D_{i}$ , and the maximum value is attained for $\sigma_{1} = \| F\|_{2}$ .

6.11. (a)

$$
\| A x \| _ {\beta} = \left\| \sum_ {j} x _ {j} A (:, j) \right\| _ {\beta} \leq \max _ {j} \| A (:, j) \| _ {\beta} \sum_ {j} | x _ {j} |,
$$

with equality for $x = e_k$ , where the maximum is attained for $j = k$ .

(b)

$$
\| A x \| _ {\infty} = \max  _ {i} | A (i,:) x | \leq \max  _ {i} \left(\| A (i,:) ^ {*} \| _ {\alpha} ^ {D} \| x \| _ {\alpha}\right) = \| x \| _ {\alpha} \max  _ {i} \| A (i,:) ^ {*} \| _ {\alpha} ^ {D}.
$$

Equality is attained for an $x$ that gives equality in the Hölder inequality involving the $k$ th row of $A$ , where the maximum is attained for $i = k$ . Finally, from either formula, $\| A \|_{1,\infty} = \max_{i,j} |a_{ij}|$ .

6.12. Using the Cholesky factorization $A = R^{*}R$ ,

$$
\begin{array}{l} \| A \| _ {\infty , 1} = \max  _ {x \neq 0} \frac {\| A x \| _ {1}}{\| x \| _ {\infty}} = \max  \left\{y ^ {*} A x: \| x \| _ {\infty} = 1, \| y \| _ {\infty} = 1 \right\} \\ = \max  \left\{\left(R y\right) ^ {*} R x: \| x \| _ {\infty} = 1, \| y \| _ {\infty} = 1 \right\} \\ = \max  \left\{\left(R x\right) ^ {*} R x: \| x \| _ {\infty} = 1 \right\} \\ = \max  \left\{x ^ {*} A x: \| x \| _ {\infty} = 1 \right\}. \\ \end{array}
$$

6.13. $H^T$ is also a Hadamard matrix, so by the duality result (6.21) it suffices to show that $\|H\|_p = n^{1/p}$ for $1 \leq p \leq 2$ . Since $|h_{ij}| \equiv 1$ , (6.12) gives $\|H\|_p \geq n^{1/p}$ . Since $\|H\|_1 = n$ and $\|H\|_2 = n^{1/2}$ , (6.20) gives $\|H\|_p \leq n^{1/p}$ , and so $\|H\|_p = n^{1/p}$ for $1 \leq p \leq 2$ , as required.

6.14. We prove the lower bound in (6.23) and the upper bound in (6.24); the other bounds follow on using $\| A^T\| _p = \| A\| _q$ . The lower bound in (6.23) is just (6.12). Now assume that $A$ has at most $\mu$ nonzeros per column. Define

$$
D _ {i} = \operatorname {d i a g} (s _ {i 1}, \ldots , s _ {i n}), \qquad s _ {i j} = \left\{ \begin{array}{l l} 1, & a _ {i j} \neq 0, \\ 0, & a _ {i j} = 0, \end{array} \right.
$$

and note that

$$
\sum_ {i} \| D _ {i} x \| _ {p} ^ {p} = \sum_ {i, j} s _ {i j} | x _ {j} | ^ {p} = \sum_ {j} | x _ {j} | ^ {p} \sum_ {i} s _ {i j} \leq \mu \| x \| _ {p} ^ {p}.
$$

We have

$$
\begin{array}{l} \| A x \| _ {p} ^ {p} = \sum_ {i} | A (i,:) x | ^ {p} = \sum_ {i} | A (i,:) D _ {i} x | ^ {p} \\ \leq \sum_ {i} \| A (i,:) \| _ {q} ^ {p} \| D _ {i} x \| _ {p} ^ {p} \\ \leq \max  _ {i} \| A (i,:) \| _ {q} ^ {p} \sum_ {i} \| D _ {i} x \| _ {p} ^ {p} \\ \leq \max  _ {i} \| A (i, \cdot) \| _ {q} ^ {p} \mu \| x \| _ {p} ^ {p}, \\ \end{array}
$$

which gives the upper bound in (6.24).

6.15. The lower bound follows from $\| Ax\| _p / \| x\| _p\leq \| |A||x|\| _p / \| |x|\| _p$ . From (6.12) we have

$$
\left\| \left| A \right| \right. \| _ {p} \leq n ^ {1 - 1 / p} \operatorname * {m a x} _ {j} \| \left| A | e _ {j} \right\| _ {p} = n ^ {1 - 1 / p} \operatorname * {m a x} _ {j} \| A e _ {j} \| _ {p} \leq n ^ {1 - 1 / p} \| A \| _ {p}.
$$

By (6.21), we also have $\| |A| \|_p = \| |A^T| \|_q \leq n^{1 - 1/q} \| A^T \|_q = n^{1/p} \| A \|_p$ and the result follows.

6.16. The function $\nu$ is not a vector norm because $\nu(\alpha x) \neq |\alpha| \nu(x)$ does not hold for all $\alpha \in \mathbb{C}$ , $x \in \mathbb{C}^n$ . However, $\nu(\alpha x) \leq \nu(\alpha) \nu(x)$ , and the other two norm conditions hold, so it makes sense to define the "subordinate norm". We have

$$
\begin{array}{l} \nu (A x) = \nu \left(\sum_ {j} x _ {j} A (:, j)\right) \leq \sum_ {j} \nu (x _ {j} A (:, j)) \\ \leq \sum_ {j} \nu (x _ {j}) \nu (A (:, j)) \leq \max  _ {j} \nu (A (:, j)) \sum_ {j} \nu (x _ {j}) \\ = \max  _ {j} \nu (A (:, j)) \nu (x). \\ \end{array}
$$

There is equality for $x_{j}$ an appropriate unit vector $e_{j}$ . Hence $\nu(A) = \max_{j} \nu(A(:, j))$ .

7.1. It is straightforward to obtain from $A(y - x) = \Delta b - \Delta Ax + \Delta A(x - y)$ the inequality $(I - \epsilon |A^{-1}|E)|x - y| \leq \epsilon |A^{-1}|(f + E|x|)$ . In general, if $B \geq 0$ and $\rho(B) < 1$ then $I - B$ is nonsingular. Since $\rho(\epsilon |A^{-1}|E) \leq \epsilon \| |A^{-1}|E \| < 1$ , we can premultiply by $(I - \epsilon |A^{-1}|E)^{-1} \geq 0$ to obtain the bound for $|x - y|$ . For the last part,

$$
\frac {\left| x _ {i} - y _ {i} \right|}{\left| x _ {i} \right|} \leq \frac {\epsilon \left(\left| A ^ {- 1} \right| (f + E | x |)\right) _ {i}}{\left| x _ {i} \right|} + O \left(\epsilon^ {2}\right).
$$

7.2. Take norms in $r = A(x - y)$ and $x - y = A^{-1}r$ . The result says that the normwise relative error is at least as large as the normwise relative residual and possibly $\kappa(A)$ times as large. Since the upper bound is attainable, the relative residual is not a good predictor of the relative error unless $A$ is very well conditioned.

7.3. Let $D_R$ equilibrate the rows of $A$ , so that $B = D_R A$ satisfies $|B|e = e$ . Then

$$
\operatorname {c o n d} (B) = \| | B ^ {- 1} | | B | e \| _ {\infty} = \| | B ^ {- 1} | e \| _ {\infty} = \| B ^ {- 1} \| _ {\infty} = \kappa_ {\infty} (B).
$$

Hence $\kappa_{\infty}(D_R A) = \operatorname{cond}(D_R A) = \operatorname{cond}(A)$ , which implies $\kappa_{\infty}(A) \leq \kappa_{\infty}(D_R) \operatorname{cond}(A)$ . The inequality $\operatorname{cond}(A) \leq \kappa_{\infty}(A)$ is trivial, and the deduction of (7.15) is immediate.

7.4. The first inequality is trivial. For the second, since $h_{ii} \equiv 1$ and $|h_{ij}| \leq 1$ we have $|H| \geq I$ and $\| H \|_{\infty} \leq n$ . Hence

$$
\left\| \left| H ^ {- 1} \right| \right| H | \left\| _ {\infty} \geq \left\| \left| H ^ {- 1} \right| \right. \right\| _ {\infty} = \left\| H ^ {- 1} \right\| _ {\infty} \geq \left\| H ^ {- 1} \right\| _ {\infty} \frac {\left\| H \right\| _ {\infty}}{n} = \frac {\kappa_ {\infty} (H)}{n}.
$$

7.5. We have $\Delta x = A^{-1}\Delta b$ , which yields $\| \Delta x \|_2 \leq \sigma_n^{-1} \| \Delta b \|_2$ . Now

$$
\begin{array}{l} \| x \| _ {2} ^ {2} = \| V \Sigma^ {- 1} U ^ {T} b \| _ {2} = \sum_ {i = 1} ^ {n} \frac {\left(u _ {i} ^ {T} b\right) ^ {2}}{\sigma_ {i} ^ {2}} \qquad (u _ {i} = U (:, i)) \\ \geq \sum_ {i = n + 1 - k} ^ {n} \frac {(u _ {i} ^ {T} b) ^ {2}}{\sigma_ {i} ^ {2}} \\ \geq \frac {1}{\sigma_ {n + 1 - k} ^ {2}} \sum_ {i = n + 1 - k} ^ {n} (u _ {i} ^ {T} b) ^ {2} = \frac {\| P _ {k} b \| _ {2} ^ {2}}{\sigma_ {n + 1 - k} ^ {2}}, \\ \end{array}
$$

which yields the result.

If we take $k = n$ we obtain the bound that would be obtained by applying standard perturbation theory (Theorem 7.2). The gist of this result is that the full $\kappa_{2}(A)$ magnification of the perturbation will not be felt if $b$ contains a significant component in the subspace $\mathrm{span}(U_k)$ for a $k$ such that $\sigma_{n+1-k} \approx \sigma_n$ . This latter condition says that $x$ must be a large-normed solution: $\|x\|_2 \approx \|A^{-1}\|_2 \|b\|_2$ .

7.6. (a) Use $\| |A^{-1}|E|x| \|_{\infty} = \| x \|_1 \| |A^{-1}| |A|e \|_{\infty} = \| x \|_1 \| |A^{-1}| |A| \|_{\infty}$ . For the upper bound, use $f \leq |A||x|$ .

(b) Use $\| |A^{-1}|E|x|\|_{\infty} = \| |A^{-1}|ee^{T}|A||x|\|_{\infty} = \| A^{-1}\|_{\infty}\| |A||x||_{1}.$

7.7. We will prove the result for $\omega$ ; the proof for $\eta$ is entirely analogous. The lower bound is trivial. Let $\epsilon = \omega_{|A|,|b|}(y)$ and $r = b - Ay$ . Then $|r| \leq \epsilon(|A||y| + |b|)$ and $(A + \Delta A)y = b + \Delta b$ with $|\Delta A| \leq \epsilon|A|$ and $|\Delta b| \leq \epsilon|b|$ . Hence $|b| = |(A + \Delta A)y - \Delta b| \leq (1 + \epsilon)|A||y| + \epsilon|b|$ , yielding $|b| \leq (1 - \epsilon)^{-1}(1 + \epsilon)|A||y|$ . Thus

$$
| r | \leq \epsilon \left(1 + \frac {1 + \epsilon}{1 - \epsilon}\right) | A | | y | = \frac {2 \epsilon}{1 - \epsilon} | A | | y |,
$$

which implies the result, by Theorem 7.3.

7.8. The constraint on $\Delta A$ and $\Delta b$ can be written

$$
\left[ \begin{array}{c c} \Delta A & \theta \Delta b \end{array} \right] \left[ \begin{array}{c} y \\ - \theta^ {- 1} \end{array} \right] = r,
$$

and so

$$
\| r \| _ {2} \leq \left(\| y \| _ {2} ^ {2} + \theta^ {- 2}\right) ^ {1 / 2} \| [ \Delta A, \theta \Delta b ] \| _ {2} \leq \theta^ {- 1} \left(\theta^ {2} \| y \| _ {2} ^ {2} + 1\right) ^ {1 / 2} \| [ \Delta A, \theta \Delta b ] \| _ {F},
$$

which gives a lower bound on $\eta_F(y)$ . The bound is attained for the rank-1 perturbation $[\varDelta A,\theta\varDelta b]=r[y^T,-\theta^{-1}]^T/(\|y\|_2^2+\theta^{-2})$ .

7.9. We have $\Delta x = A^{-1}(\Delta b - \Delta Ax) + O(\epsilon^2)$ . Therefore $c^T\Delta x = c^TA^{-1}(\Delta b - \Delta Ax) + O(\epsilon^2)$ , and so

$$
\frac {| c ^ {T} \Delta x |}{\epsilon | c ^ {T} x |} \leq \frac {| c ^ {T} A ^ {- 1} | (f + E | x |)}{| c ^ {T} x |} + O (\epsilon),
$$

this inequality being sharp. Hence

$$
\chi_ {E, f} (A, x) = \frac {| c ^ {T} A ^ {- 1} | (f + E | x |)}{| c ^ {T} x |}.
$$

The lower bound for $\chi_{|A|,|b|}(A,x)$ follows from the inequalities $|c^T x| = |c^T A^{-1} \cdot Ax| \leq |c^T A^{-1}||A||x|$ and $|c^T x| = |c^T A^{-1}b| \leq |c^T A^{-1}||b|$ . A slight modification to the derivation of $\chi_{E,f}(A,x)$ yields

$$
\psi_ {E, f} (A, x) = \| c ^ {T} A ^ {- 1} \| _ {2} \frac {\| f \| _ {2} + \| E \| _ {2} \| x \| _ {2}}{| c ^ {T} x |}.
$$

7.10. (a) For any $D_{1}, D_{2} \in \mathcal{D}_{n}$ we have

$$
\rho (B C) = \rho \left(D _ {1} B C D _ {1} ^ {- 1}\right) \leq \left\| D _ {1} B C D _ {1} ^ {- 1} \right\| _ {\infty} \leq \left\| D _ {1} B D _ {2} \right\| _ {\infty} \left\| D _ {2} ^ {- 1} C D _ {1} ^ {- 1} \right\| _ {\infty}. \tag {A.5}
$$

The rest of the proof shows that equality can be attained in this inequality.

Let $x_{1} > 0$ be a right Perron vector of $BC$ , so that $BCx_{1} = \pi x_{1}$ , where $\pi = \rho(BC) > 0$ . Define

$$
x _ {2} = C x _ {1}, \tag {A.6}
$$

so that $x_{2} > 0$ and

$$
B x _ {2} = \pi x _ {1}. \tag {A.7}
$$

(We note, incidentally, that $x_{2}$ is a right Perron vector of $CB$ : $CBx_{2} = \pi x_{2}$ .)

Now define

$$
D _ {1} = \operatorname {d i a g} \left(x _ {1}\right) ^ {- 1}, \quad D _ {2} = \operatorname {d i a g} \left(x _ {2}\right). \tag {A.8}
$$

Then, with $e = [1, 1, \ldots, 1]^T$ , (A.7) can be written $BD_2e = \pi D_1^{-1}e$ , or $D_1BD_2e = \pi e$ . Since $D_1BD_2 > 0$ , this gives $\|D_1BD_2\|_{\infty} = \pi$ . Similarly, (A.6) can be written $D_2e = CD_1^{-1}e$ , or $D_2^{-1}CD_1^{-1}e = e$ , which gives $\|D_2^{-1}CD_1^{-1}\|_{\infty} = 1$ . Hence for $D_1$ and $D_2$ defined by (A.8) we have $\|D_1BD_2\|_{\infty}\|D_2^{-1}CD_1^{-1}\|_{\infty} = \pi = \rho(BC)$ , as required.

Note that for the optimal $D_{1}$ and $D_{2}$ , $D_{1}BD_{2}$ and $D_{2}^{-1}CD_{1}^{-1}$ both have the property that all their rows sums are equal.

(b) Take $B = |A|$ and $C = |A^{-1}|$ , and note that $\kappa_{\infty}(D_1AD_2) = \| D_1|A|D_2\|_{\infty} \times \| D_2^{-1}|A^{-1}|D_1^{-1}\|_{\infty}$ . Now apply (a).

(c) We can choose $F_1 > 0$ and $F_2 > 0$ so that $|A| + tF_1 > 0$ and $|A^{-1}| + tF_2 > 0$ for all $t > 0$ . Hence, using (a),

$$
\begin{array}{l} \inf  _ {D _ {1}, D _ {2} \in \mathcal {D} _ {n}} \kappa_ {\infty} (D _ {1} A D _ {2}) \leq \inf  _ {D _ {1}, D _ {2} \in \mathcal {D} _ {n}} \| D _ {1} (| A | + t F _ {1}) D _ {2} \| _ {\infty} \| D _ {2} ^ {- 1} (| A ^ {- 1} | + t F _ {2}) D _ {1} ^ {- 1} \| _ {\infty} \\ = \rho \bigl (\bigl (| A | + t F _ {1} \bigr) \bigl (| A ^ {- 1} | + t F _ {2} \bigr) \bigr). \\ \end{array}
$$

Taking the limit as $t \to 0$ yields the result, using continuity of eigenvalues.

(d) A nonnegative irreducible matrix has a positive Perron vector, from standard Perron-Frobenius theory (see, e.g., Horn and Johnson [636, 1985, Chap. 8]). Therefore the result follows by noting that in the proof of (a) all we need is for $D_{1}$ and $D_{2}$ in (A.8) to be defined and nonsingular, that is, for $x_{1}$ and $x_{2}$ to be positive vectors. This is the case if $BC$ and $CB$ are irreducible (since $x_{2}$ is a Perron vector of $CB$ )

(e) Using $\kappa_{1}(A) = \kappa_{\infty}(A^{T})$ , $\rho(A) = \rho(A^{T})$ , and $\rho(AB) = \rho(BA)$ , it is easy to show that the results of (a)-(d) remain true with the $\infty$ -norm replaced by the 1-norm. From $\|A\|_{2} \leq \left(\|A\|_{1}\|A\|_{\infty}\right)^{1/2}$ it then follows that $\inf_{D_{1}, D_{2} \in \mathcal{D}_{n}} \kappa_{2}(D_{1}AD_{2}) \leq \rho(|A||A^{-1}|)$ . In fact, the result in (a) holds for any $p$ -norm, though the optimal $D_{1}$ and $D_{2}$ depend on the norm; see Bauer [90, 1963, Lem. 1(i)].

7.11. That $\mu_E^{\prime}(A)$ cannot exceed the claimed expression follows by taking absolute values in the expression $\Delta X = -(A^{-1}\Delta AA^{-1} + A^{-1}\Delta A\Delta X)$ . To show it can equal it we need to show that if the maximum is attained for $(i,j) = (r,s)$ then

$$
\left| \Delta x _ {r s} \right| = \epsilon \left(\left| A ^ {- 1} \right| E \left| A ^ {- 1} \right|\right) _ {r s}
$$

can be attained, to first order in $\epsilon$ . Equality is attained for $\Delta A = D_{1}ED_{2}$ , where $D_{1} = \mathrm{diag}(\mathrm{sign}(A^{-1})_{ri})$ , $D_{2} = \mathrm{diag}(\mathrm{sign}(A^{-1})_{is})$ .

7.12. (a) We need to find a symmetric $H$ satisfying $Hy = b - Ay \eqqcolon r$ . Consider the QR factorization

$$
Q ^ {T} \left[ \begin{array}{c c} y & r \end{array} \right] = \left[ \begin{array}{c c} t _ {1 1} & t _ {1 2} \\ 0 & t _ {2 2} \\ \vdots & \vdots \\ 0 & 0 \end{array} \right].
$$

The constraint can be rewritten $Q^T HQ \cdot Q^T y = Q^T r$ , and it is satisfied by $Q^T HQ \coloneqq \mathrm{diag}(\widetilde{H}, 0_{n-2})$ if we can find $\widetilde{H} \in \mathbb{R}^{2 \times 2}$ such that

$$
\widetilde {H} t = u, \quad \widetilde {H} = \widetilde {H} ^ {T}, \quad \text {w h e r e} \quad t = \left[ \begin{array}{c} t _ {1 1} \\ 0 \end{array} \right], \quad u = \left[ \begin{array}{c} t _ {1 2} \\ t _ {2 2} \end{array} \right].
$$

We can take $\widetilde{H} \coloneqq (\|u\|_2 / \|t\|_2)P$ , where $P \in \mathbb{R}^{2 \times 2}$ is either a suitably chosen Householder matrix, or the identity if $t$ is a positive multiple of $u$ . Then

$$
\begin{array}{l} \| H \| _ {2} = \| \widetilde {H} \| _ {2} = \| u \| _ {2} / \| t \| _ {2} \\ = \| r \| _ {2} / \| y \| _ {2} = \| G y \| _ {2} / \| y \| _ {2} \leq \| G \| _ {2}, \\ \end{array}
$$

and $\| H\| _F = \| \widetilde{H}\| _F\leq \sqrt{2}\| \widetilde{H}\| _2\leq \sqrt{2}\| G\| _2\leq \sqrt{2}\| G\| _F$

(b) We can assume, without loss of generality, that

$$
\left| y _ {1} \right| \leq \left| y _ {2} \right| \leq \dots \leq \left| y _ {n} \right|. \tag {A.9}
$$

Define the off-diagonal of $H$ by $h_{ij} = h_{ji} = g_{ij}$ for $j > i$ , and let $h_{11} = g_{11}$ . The $i$ th equation of the constraint $Hy = Gy$ will be satisfied if

$$
h _ {i i} y _ {i} = g _ {i i} y _ {i} + \sum_ {j = 1} ^ {i - 1} \left(g _ {i j} - g _ {j i}\right) y _ {j}. \tag {A.10}
$$

If $y_{i} = 0$ set $h_{ii} = 0$ ; then (A.10) holds by (A.9). Otherwise, set

$$
h _ {i i} = g _ {i i} + \sum_ {j = 1} ^ {i - 1} \left(g _ {i j} - g _ {j i}\right) \frac {y _ {j}}{y _ {i}}, \tag {A.11}
$$

which yields

$$
\left| h _ {i i} \right| \leq \epsilon \left| a _ {i i} \right| + 2 \epsilon \sum_ {j = 1} ^ {i - 1} \left| a _ {i j} \right| \leq 3 \epsilon \left| a _ {i i} \right|,
$$

by the diagonal dominance.

(c) Let $D = \mathrm{diag}(a_{ii}^{1/2})$ and $A =: D\widetilde{A}D$ . Then $\widetilde{a}_{ii} \equiv 1$ and $|\widetilde{a}_{ij}| \leq 1$ for $i \neq j$ . The given condition can be written $(\widetilde{A} + \widetilde{G})\widetilde{y} = \widetilde{b}$ , $|\widetilde{G}| \leq \epsilon |\widetilde{A}|$ , where $\widetilde{y} = Dy$ and $\widetilde{b} = D^{-1}b$ . Defining $\widetilde{H}$ as in the proof of (b), we find from (A.11) that $|\widetilde{h}_{ii}| \leq \epsilon + 2\epsilon (i - 1) \leq (2n - 1)\epsilon$ so that $|\widetilde{H}| \leq (2n - 1)|\widetilde{A}|$ . With $H := D\widetilde{H}D$ , we find that $H = H^T$ , $(A + H)y = b$ , and $|H| \leq (2n - 1)\epsilon |A|$ .

7.13. By examining the error analysis for an inner product (§3.1), it is easy to see that for any $x \in \mathbb{R}^n$ ,

$$
\left| f l (A x) - A x \right| \leq \operatorname {d i a g} \left(\gamma_ {w _ {i}}\right) | A | | x |.
$$

Hence $\widehat{r} = fl(b - A\widehat{x})$ satisfies

$$
\widehat {r} = r + \Delta r, \quad | \Delta r | \leq \Gamma (| A | | \widehat {x} | + | b |), \tag {A.12}
$$

which is used in place of (7.30) to obtain the desired bound.

7.14. (a) Writing $A^{-1} = (\alpha_{ij})$ , we have

$$
\Delta x _ {i} = - \sum_ {j = 1} ^ {n} \alpha_ {i j} \sum_ {k = 1} ^ {n} \epsilon_ {j k} e _ {j k} x _ {k} + \sum_ {j = 1} ^ {n} \alpha_ {i j} \delta_ {j} f _ {j}.
$$

By the independence of the $\epsilon_{ij}$ and $\delta_{i}$ ,

$$
\mathcal {E} (\varDelta x _ {i} ^ {2}) = \sigma^ {2} \left(\sum_ {j = 1} ^ {n} \sum_ {k = 1} ^ {n} \alpha_ {i j} ^ {2} e _ {j k} ^ {2} x _ {k} ^ {2} + \sum_ {j = 1} ^ {n} \alpha_ {i j} ^ {2} f _ {j} ^ {2}\right) = \sigma^ {2} \left([ A ^ {- 1} ] [ E ] [ x ] + [ A ^ {- 1} ] [ f ]\right) _ {i}.
$$

Hence

$$
\mathcal {E} \left(\| \Delta x \| _ {2} ^ {2}\right) = \sum_ {i = 1} ^ {n} \mathcal {E} \left(\Delta x _ {i} ^ {2}\right) = \sigma^ {2} \| [ A ^ {- 1} ] [ E ] [ x ] + [ A ^ {- 1} ] [ f ] \| _ {1}.
$$

(b) A traditional condition number would be based on the maximum of $\| \Delta x\| _2 / (\sigma \| x\| _2)$ over all "perturbations to the data of relative size $\sigma$ ". The expression $\mathrm{condexp}(A,b)$ uses the "expected perturbation" $\sqrt{\mathcal{E}(\|\Delta x\|_2^2)} /(\sigma \| x\|_2)$ rather than the worst case.

(c) For $e_{ij} \equiv \|A\|_2$ and $f_i \equiv \|b\|_2$ we have

$$
[ A ^ {- 1} ] [ E ] [ x ] + [ A ^ {- 1} ] [ f ] = \big (\| A \| _ {2} ^ {2} \| x \| _ {2} ^ {2} + \| b \| _ {2} ^ {2} \big) [ A ^ {- 1} ] \left[ \begin{array}{c} 1 \\ 1 \\ \vdots \\ 1 \end{array} \right],
$$

so

$$
\frac {\left(\| [ A ^ {- 1} ] [ E ] [ x ] + [ A ^ {- 1} ] [ f ] \| _ {1}\right) ^ {1 / 2}}{\| x \| _ {2}} = \left(\| A \| _ {2} ^ {2} + \frac {\| b \| _ {2} ^ {2}}{\| x \| _ {2} ^ {2}}\right) ^ {1 / 2} \| A ^ {- 1} \| _ {F}.
$$

But

$$
\kappa_ {A, b} (A, x) = \left(\| A \| _ {2} + \frac {\| b \| _ {2}}{\| x \| _ {2}}\right) \| A ^ {- 1} \| _ {2}.
$$

Hence

$$
2 ^ {- 1 / 2} \kappa_ {A, b} (A, x) \leq \operatorname {c o n d e x p} (A, x) \leq \sqrt {n} \kappa_ {A, b} (A, x).
$$

This inequality shows that when perturbations are measured normwise there is little difference between the average and worst-case condition numbers.

# 7.15. We have

$$
\begin{array}{l} \left\| A \circ A ^ {- T} \right\| _ {2} = \left\| D _ {1} A D _ {2} \circ D _ {1} ^ {- 1} A ^ {- T} D _ {2} ^ {- 1} \right\| _ {2} = \left\| \left(D _ {1} A D _ {2}\right) \circ \left(D _ {1} A D _ {2}\right) ^ {- T} \right\| _ {2} \\ \leq \left\| D _ {1} A D _ {2} \right\| _ {2} \left\| \left(D _ {1} A D _ {2}\right) ^ {- T} \right\| _ {2} = \kappa_ {2} \left(D _ {1} A D _ {2}\right). \\ \end{array}
$$

Note that this result gives a lower bound for the optimal condition number, while Bauer's result in Problem 7.10(c) gives an upper bound. There is equality for diagonal $A$ , trivially. For triangular $A$ we have $\| A \circ A^{-T} \|_2 = 1 = \rho(|A||A^{-1}|)$ and so there is equality in view of Problem 7.10(e).

# 8.1. Straightforward.

8.2. Let

$$
T (\lambda) = \left[ \begin{array}{c c c} \lambda^ {- 1} & 1 & 1 \\ 0 & \lambda^ {- 1} & \lambda^ {- 1} \\ 0 & 0 & \lambda^ {- 2} \end{array} \right].
$$

Then

$$
T (\lambda) ^ {- 1} = \left[ \begin{array}{c c c} \lambda & - \lambda^ {2} & 0 \\ 0 & \lambda & - \lambda^ {2} \\ 0 & 0 & \lambda^ {2} \end{array} \right], \quad M (T (\lambda)) ^ {- 1} = \left[ \begin{array}{c c c} \lambda & \lambda^ {2} & 2 \lambda^ {3} \\ 0 & \lambda & \lambda^ {2} \\ 0 & 0 & \lambda^ {2} \end{array} \right].
$$

As $\lambda \to \infty$ , $\| M(T(\lambda))^{-1}\| /\| T(\lambda)^{-1}\| \sim \lambda$ . This $3\times 3$ example can be extended to an $n\times n$ one by padding with an identity matrix.

8.3. The bound follows from Theorem 8.10, since $\left(M(U)^{-1}\right)_{ij} \leq 2^{j - i - 1} (j > i)$ . Using $\|b\|_{\infty} \leq \|U\|_{\infty} \|x\|_{\infty} \leq n \|x\|_{\infty}$ we get a similar result to that given by Theorem 8.7.

8.4. Assume $T$ is upper triangular, and write $T = D - U$ , where $D = \mathrm{diag}(t_{ii}) \geq 0$ and $U \geq 0$ is strictly upper triangular. Then, using the fact that $(D^{-1}U)^n = 0$ ,

$$
\begin{array}{l} \left| T ^ {- 1} \right| \left| T \right| = \left(I - D ^ {- 1} U\right) ^ {- 1} D ^ {- 1} \cdot (D + U) \\ = \sum_ {i = 0} ^ {n - 1} \left(D ^ {- 1} U\right) ^ {i} \cdot \left(I + D ^ {- 1} U\right) \\ = \sum_ {i = 0} ^ {n - 1} (D ^ {- 1} U) ^ {i} + \sum_ {i = 1} ^ {n - 1} (D ^ {- 1} U) ^ {i}. \\ \end{array}
$$

Now $0 \leq b = Tx = (D - U)x$ , so $Dx \geq Ux$ , that is, $x \geq D^{-1}Ux$ . Hence

$$
| T ^ {- 1} | | T | x = \sum_ {i = 0} ^ {n - 1} (D ^ {- 1} U) ^ {i} x + \sum_ {i = 1} ^ {n - 1} (D ^ {- 1} U) ^ {i} x \leq (n + n - 1) x,
$$

which gives the result, since $x = T^{-1}b \geq 0$ .

# 8.5.Use (8.4).

8.7. (a) Write

$$
\| A ^ {- 1} \| _ {\infty} = \max _ {x \neq 0} \frac {\| A ^ {- 1} x \| _ {\infty}}{\| x \| _ {\infty}} =: \frac {\| b \| _ {\infty}}{\| y \| _ {\infty}},
$$

where $Ab = y$ . Let $|b_k| = \| b\|_{\infty}$ . From

$$
a _ {k k} b _ {k} = y _ {k} - \sum_ {j \neq k} a _ {k j} b _ {j},
$$

it follows that

$$
\left| a _ {k k} \right| \left| b _ {k} \right| \leq \left\| y \right\| _ {\infty} + \sum_ {j \neq k} \left| a _ {k j} \right| \left\| b \right\| _ {\infty},
$$

and hence that $\| b\|_{\infty} / \| y\|_{\infty}\leq 1 / \alpha_{k}\leq 1 / (\min_{i}\alpha_{i})$

(b) Apply the result of (a) to $AD$ and use the inequality $\| A^{-1}\|_{\infty} \leq \| (AD)^{-1}\|_{\infty}\| D\|_{\infty}$ .   
(c) If $A$ is triangular then we can achieve any diagonal dominance factors $\beta_{i}$ we like, by appropriate column scaling. In particular, we can take $\beta_{i} \equiv 1$ in (b), which requires $M(A)d = e$ , where $d = De$ . Then $\| D\|_{\infty} = \| d\|_{\infty} = \| M(A)^{-1}e\|_{\infty}$ , so the bound is $\| A^{-1}\|_{\infty} \leq \| M(A)^{-1}e\|_{\infty}$ , as required.

8.8. (a) Using the formula $\operatorname*{det}(I + xy^T) = 1 + y^T x$ we have $\operatorname*{det}(A + \alpha e_i e_j^T) = \operatorname*{det}(A(I + \alpha A^{-1} e_i e_j^T)) = \operatorname*{det}(A)(1 + \alpha e_j^T A^{-1} e_i)$ . Hence we take $\alpha_{ij} = -(e_j^T A^{-1} e_i)^{-1}$ if $e_j^T A^{-1} e_i \neq 0$ ; otherwise there is no $\alpha_{ij}$ that makes $A + \alpha_{ij} e_i e_j^T$ singular.

It follows that the "best" place to perturb $\tilde{A}$ to make it singular (the place that gives the smallest $\alpha_{ij}$ ) is in the $(s, r)$ position, where the element of largest absolute value of $A^{-1}$ is in the $(r, s)$ position.

(b) The off-diagonal elements of $T_{n}^{-1}$ are given by $(T_{n}^{-1})_{ij} = 2^{j - i - 1}$ . Hence, using part (a), $T_{n} + \alpha e_{n}e_{1}^{T}$ is singular, where $\alpha = -2^{2 - n}$ . In fact, $T_{n}$ is also made singular by subtracting $2^{1 - n}$ from all the elements in the first column.

8.9. Here is Zha's proof. If $s = 1$ the result is obvious, so assume $s < 1$ . Define the $n$ -vectors

$$
\boldsymbol {v} ^ {T} = \left[ \begin{array}{l l l l} \mathbf {0}, & \dots , & \mathbf {0}, & \frac {1}{\sqrt {2}}, - \frac {1}{\sqrt {2}} \end{array} \right]
$$

and

$$
u ^ {T} = \left[ \begin{array}{l l l l} 0, & \dots , & 0, & \sqrt {\frac {1 + c}{2}}, \frac {- s}{\sqrt {2 (1 + c)}} \end{array} \right]
$$

and let $\sigma = s^{n - 2}\sqrt{1 + c}$ . It is easy to check that

$$
U _ {n} (\theta) v = \sigma u, \quad U _ {n} (\theta) ^ {T} u = \sigma v,
$$

which shows that $\sigma$ is a singular value of $U_{n}(\theta)$ . With $\sigma_{i}$ denoting the $i$ th largest singular value,

$$
\sigma_ {n} (U _ {n} (\theta)) \leq s ^ {n - 1} <   \sigma = s ^ {n - 2} \sqrt {1 + c}.
$$

Now we prove by induction that $\sigma_{n-1}(U_n(\theta)) = \sigma$ . For $n = 2$ it is easy to check by direct computation that $\sigma_1(U_2(\theta)) = \sqrt{1 + c}$ . Using the interlacing property of the singular values [509, 1996, §8.6.1] and the inductive assumption, we have

$$
\sigma_ {n - 2} (U _ {n} (\theta)) \geq \sigma_ {n - 2} (U _ {n - 1} (\theta)) = s ^ {n - 3} \sqrt {1 + c} > \sigma .
$$

Therefore $\sigma_{n - 1}(U_n(\theta)) = \sigma$

8.10. For a solver of this form, it is not difficult to see that

$$
\left| f l \left(f _ {i} (T, b)\right) - f _ {i} (T, b) \right| \leq c _ {n} u \bar {f} _ {i} (M (T), | b |) + O \left(u ^ {2}\right),
$$

where $\overline{f}_i$ denotes $f_i$ with all its coefficients replaced by their absolute values, and where $\overline{f}_i(M(T),|b|)$ is a rational expression consisting entirely of nonnegative terms. This is the required bound expressed in a different notation. An example (admittedly, a contrived one) of a solver that does not satisfy (8.21) is, for a $2\times 2$ lower triangular system $Lx = b$ ,

$$
x _ {1} = b _ {1} / l _ {1 1}, \quad x _ {2} = \left(\left(b _ {2} - b _ {1}\right) \left(l _ {1 1} + l _ {2 1}\right) + b _ {1} l _ {1 1} - b _ {2} l _ {2 1}\right) / \left(l _ {1 1} l _ {2 2}\right).
$$

9.1. The proof is by induction. Assume the result is true for matrices of order $n - 1$ , and suppose

$$
\left[ \begin{array}{c c} \alpha & a ^ {T} \\ b & C \end{array} \right] = \left[ \begin{array}{c c} 1 & 0 \\ l & M \end{array} \right] \left[ \begin{array}{c c} \alpha & a ^ {T} \\ 0 & V \end{array} \right] \in \mathbb {R} ^ {n \times n}
$$

is a unique LU factorization. Then $MV = C - la^{T}$ has a unique LU factorization, and so by the inductive hypothesis has nonsingular leading principal submatrices of order 1 to $n - 2$ . Thus $v_{ii} \neq 0$ , $i = 1:n - 2$ . If $\alpha = 0$ then $b = 0$ and $l$ is arbitrary subject to $C - la^{T}$ having an LU factorization. But $C - (l + \Delta l)a^{T}$ has nonsingular leading principal submatrices of order 1 to $n - 2$ for sufficiently small $\Delta l$ (irrespective of $a$ ), so has an LU factorization for sufficiently small $\Delta l$ . Thus if $\alpha = 0$ we have a contradiction to the uniqueness of the factorization. Hence $\alpha \neq 0$ , which completes the proof.

9.2. $A(\sigma)$ fails to have an LU factorization without pivoting only if one of its leading principal submatrices is singular, that is, if $\sigma \in \lambda(A(\sigma)(1:k,1:k))$ , for $k \in \{1,2,\ldots,n-1\}$ . There are thus $1 + 2 + \dots + (n - 1) = \frac{1}{2}(n - 1)n$ "danger" values of $\sigma$ , which may not all be distinct.

9.3. If $0 \notin F(A)$ then all the principal submatrices of $A$ must be nonsingular, so the result follows by Theorem 9.1. Note that $A$ may have a unique LU factorization even when $0$ is in the field of values, as shown by the matrices

$$
A = \left[ \begin{array}{c c} 1 & 1 \\ 1 & 0 \end{array} \right] \quad (z = e _ {2}) \quad \text {a n d} \quad A = \left[ \begin{array}{c c c} 1 & 1 & 1 \\ 1 & 0 & 0 \\ 1 & 0 & 1 \end{array} \right] \quad (z = e _ {2}),
$$

so the implication is only one way. Note also that $0 \notin F(A)$ iff $e^{i\theta}A$ has positive definite Hermitian part for some real $\theta$ (Horn and Johnson [637, 1991, Thm. 1.3.5]).

9.4. The changes are minor. Denoting by $\widehat{P}$ and $\widehat{Q}$ the computed permutations, the result of Theorem 9.3 becomes

$$
\widehat {L} \widehat {U} = \widehat {P} A \widehat {Q} + \Delta A, \quad | \Delta A | \leq \gamma_ {n} | \widehat {L} | | \widehat {U} |,
$$

and that of Theorem 9.4 becomes

$$
(A + \Delta A) \widehat {x} = b, \quad | \Delta A | \leq \gamma_ {3 n} \widehat {P} ^ {T} | \widehat {L} | | \widehat {U} | \widehat {Q} ^ {T}.
$$

9.5.

$$
A = \left[ \begin{array}{c c} 1 & 1 \\ 1 & 0 \end{array} \right] = \left[ \begin{array}{c c} 1 & 0 \\ 1 & 1 \end{array} \right] \left[ \begin{array}{c c} 1 & 1 \\ 0 & - 1 \end{array} \right] = L U; \qquad | L | | U | = \left[ \begin{array}{c c} 1 & 1 \\ 1 & 2 \end{array} \right].
$$

9.6. Since $A$ is nonsingular and every submatrix has a nonnegative determinant, the determinantal inequality shows that $\det(A(1:p, 1:p)) > 0$ for $p = 1:n - 1$ , which guarantees the existence of an LU factorization (Theorem 9.1). That the elements of $L$ and $U$ are nonnegative follows from (9.2).

GE computes $a_{ij}^{(k + 1)} = a_{ij}^{(k)} - m_{ik}a_{kj}^{(k)} = a_{ij}^{(k)} - l_{ik}u_{kj}\leq a_{ij}^{(k)}$ , since $l_{ik},u_{kj}\geq 0$ . Thus $a_{ij} = a_{ij}^{(1)}\geq a_{ij}^{(2)}\geq \dots \geq a_{ij}^{(r)}, r = \min (i,j)$ . For $i > j$ , $a_{ij}^{(r)}\geq a_{ij}^{(r + 1)} = \dots = a_{ij}^{(n)} = 0$ ; for $j\geq i$ , $a_{ij}^{(r)} = \dots = a_{ij}^{(n)} = u_{ij}\geq 0$ . Thus $0\leq a_{ij}^{(k)}\leq a_{ij}$ for all $i,j,k$ and hence $\rho_n\leq 1$ . But $\rho_n\geq 1$ , so $\rho_{n} = 1$ .

9.7. The number of square submatrices is

$$
\begin{array}{l} \sum_ {k = 1} ^ {n} \binom {n} {k} ^ {2} = \binom {2 n} {n} \quad ([ 5 1 7, 1 9 9 4, \S 5. 1 ]) \\ = \frac {(2 n) !}{(n !) ^ {2}} \\ \sim \frac {\sqrt {2 \pi (2 n)} (2 n / e) ^ {2 n}}{\left(\sqrt {2 \pi n} (n / e) ^ {n}\right) ^ {2}} \quad \text {(S t i r l i n g ' s a p p r o x i m a t i o n)} \\ \sim \frac {1}{\sqrt {n}} \left(\frac {2 n / e}{n / e}\right) ^ {2 n} \sim \frac {4 ^ {n}}{\sqrt {n}} = O (4 ^ {n}). \\ \end{array}
$$

The number of rectangular submatrices is

$$
\sum_ {k = 1} ^ {n} \sum_ {l = 1} ^ {n} \binom {n} {k} \binom {n} {l} = \left(\sum_ {k = 1} ^ {n} \binom {n} {k}\right) ^ {2} = (2 ^ {n} - 1) ^ {2},
$$

which, interestingly, is not many more than the number of square submatrices.

9.8. The given fact implies that $JAJ$ is totally nonnegative. Hence it has an LU factorization $JAJ = LU$ with $L \geq 0$ and $U \geq 0$ . This means that $A = (JLJ)(JUJ) \equiv \widetilde{L}\widetilde{U}$ is an LU factorization, and $|\widetilde{L}||\widetilde{U}| = LU = JAJ = |A|$ .

9.9. With $l_j$ the $j$ th column of $L$ and $u_i^T$ the $i$ th row of $U$ , we have

$$
A ^ {(k)} = A - l _ {1} u _ {1} ^ {T} - \dots - l _ {k - 1} u _ {k - 1} ^ {T} = A - L (:, 1: k - 1) U (1: k - 1,:),
$$

hence

$$
\left| A ^ {(k)} \right| \leq | A | + \left| L (:, 1: k - 1) \right| \left| \left| U (1: k - 1,:) \right| \leq | A | + \left| L \right| \right| U |.
$$

Equating $(i,j)$ elements gives

$$
\left| a _ {i j} ^ {(k)} \right| \leq \left| a _ {i j} \right| + \| \left| L \right| \left| U \right| \| _ {\infty},
$$

from which the result follows on dividing by $\max_{i,j}|a_{ij}|$ .

9.10. By inspecting the equations in Algorithm 9.2 we see that the computed LU factors satisfy

$$
A - \widehat {L} \widehat {U} = \epsilon \widehat {l} _ {i j} \widehat {u} _ {j j} e _ {i} e _ {j} ^ {T}.
$$

Since $\widehat{L}\widehat{U}\widehat{x} = b$ , we have, writing $\alpha = \epsilon \widehat{l}_{ij}\widehat{u}_{jj}$ and using the Sherman-Morrison formula (Problem 26.2),

$$
\widehat {x} = \left(A - \alpha e _ {i} e _ {j} ^ {T}\right) ^ {- 1} b = \left(A ^ {- 1} + \frac {\alpha A ^ {- 1} e _ {i} e _ {j} ^ {T} A ^ {- 1}}{1 - \alpha e _ {j} ^ {T} A ^ {- 1} e _ {i}}\right) b = x + \frac {\alpha A ^ {- 1} e _ {i} x _ {j}}{1 - \alpha e _ {j} ^ {T} A ^ {- 1} e _ {i}}.
$$

So

$$
x - \widehat {x} = - \frac {\epsilon \widehat {l} _ {i j} \widehat {u} _ {j j} x _ {j}}{1 - \epsilon \widehat {l} _ {i j} \widehat {u} _ {j j} A ^ {- 1} (j , i)} A ^ {- 1} (:, i).
$$

The error $x - \widehat{x}$ is a rational function of $\epsilon$ and is zero if $x_{j} = 0$ , but it will typically be of order $\epsilon \kappa_{\infty}(A)\| x\|_{\infty}$ .

9.11. $\alpha(B) = \alpha(A)$ , and $B^{-1} = \frac{1}{2}\left[ \begin{array}{cc}A^{-1} & A^{-1}\\ A^{-1} & -A^{-1} \end{array} \right]$ , so $\beta(B) = \frac{1}{2}\beta(A)$ . Hence $\theta(B) = (\alpha(B)\beta(B))^{-1} = 2\theta(A)$ . Taking $A = S_n$ , $g(2n) \geq \rho_{2n}^c(B) \geq \theta(B) = 2\theta(S_n) = n + 1$ .

9.12. First, the size or accuracy of the pivots is not the fundamental issue. The error analysis shows that instability corresponds to large elements in the intermediate matrices or in $L$ or $U$ . Second, in $PAQ = LU$ , $u_{nn}^{-1}$ is an element of $A^{-1}$ (see (9.11)), so it is not necessarily true that the pivoting strategy can force $u_{nn}$ to be small. Third, from a practical point of view it is good to obtain small final pivots because they reveal near singularity of the matrix.

9.13. Because the rows of $U$ are the pivot rows, $\mu_j$ is the maximum number of times any element in the $j$ th column of $A$ was modified during the reduction. Since the multipliers are bounded by $\tau^{-1}$ , the bound for $\max_i |a_{ij}^{(k)}|$ follows easily. Thus

$$
\rho_ {n} \leq (1 + \tau^ {- 1}) ^ {\max  _ {j} \mu_ {j}}.
$$

10.1. Observe that if $x = \alpha e_i - e_j$ , where $e_i$ is the $i$ th unit vector, then for any $\alpha$ we have, using the symmetry of $A$ ,

$$
0 <   x ^ {T} A x = \alpha^ {2} a _ {i i} - 2 \alpha a _ {i j} + a _ {j j}.
$$

Since the right-hand side is a quadratic in $\alpha$ , the discriminant must be negative, that is, $4a_{ij}^2 - 4a_{ii}a_{jj} < 0$ , which yields the desired result. This result can also be proved using the Cholesky decomposition and the Cauchy-Schwarz inequality: $A = R^T R \Rightarrow a_{ij} = r_i^T r_j \leq \|r_i\|_2 \|r_j\|_2 = (a_i, a_{jj})^{1/2}$ (there is strict inequality for $i \neq j$ , since $r_i \neq \alpha r_j$ ). The inequality implies that $|a_{ij}| \leq \max(a_{ii}, a_{jj})$ , which shows that $\max_{i,j} |a_{ij}| = \max_{i} a_{ii}$ , that is, the largest element of $A$ lies on the diagonal.

10.2. Compute the Cholesky factorization $A = R^T R$ , solve $R^T y = x$ , then compute $y^T y$ . In addition to being more efficient than forming $A^{-1}$ explicitly, this approach guarantees a nonnegative result.

10.3. Let $s = c - \sum_{i=1}^{k-1} a_i b_i$ . By Lemma 8.4,

$$
\widehat {s} \left(1 + \theta_ {k - 1} ^ {(0)}\right) = c - \sum_ {i = 1} ^ {k - 1} a _ {i} b _ {i} \left(1 + \theta_ {k - 1} ^ {(i)}\right).
$$

Then $\widehat{\pmb{y}} = f l(\sqrt{\widehat{s}}) = \sqrt{\widehat{s}} (1 + \delta), |\delta |\leq u$ . Hence

$$
\hat {y} ^ {2} (1 + \theta_ {k + 1}) = \frac {\widehat {y} ^ {2}}{(1 + \delta) ^ {2}} (1 + \theta_ {k - 1} ^ {(0)}) = c - \sum_ {i = 1} ^ {k - 1} a _ {i} b _ {i} (1 + \theta_ {k - 1} ^ {(i)}),
$$

as required.

10.4. $A = \left[ \begin{array}{cc}\alpha & a^T\\ a & C \end{array} \right]\Rightarrow A^{(2)} = \left[ \begin{array}{cc}\alpha & a^T\\ 0 & B \end{array} \right],$ where $B = C - aa^{T} / \alpha$ . Let $y = [1,\theta z]^T$ . Then $0 < y^{T}Ay = \theta^{2}z^{T}Cz + 2\theta z^{T}a + \alpha$ for all $\theta$ and so the discriminant $4(z^{T}a)^{2} - 4\alpha z^{T}Cz < 0$ if $z\neq 0$ , that is, $z^{T}Bz = z^{T}Cz - \frac{1}{\alpha} (z^{T}a)^{2} > 0$ (since $\alpha = a_{11} > 0$ ). This shows that $B$ is positive definite.

By induction, the elimination succeeds (i.e., all pivots are nonzero) and all the reduced submatrices are positive definite. Hence $a_{rr}^{(r)} > 0$ for all $r$ . Therefore

$$
a _ {k k} ^ {(r + 1)} = a _ {k k} ^ {(r)} - \frac {a _ {k r} ^ {(r)}}{a _ {r r} ^ {(r)}} a _ {r k} ^ {(r)} = a _ {k k} ^ {(r)} - \frac {a _ {r k} ^ {(r) 2}}{a _ {r r} ^ {(r)}} \leq a _ {k k} ^ {(r)}.
$$

Thus $a_{kk} = a_{kk}^{(1)} \geq \dots \geq a_{kk}^{(k)} > 0$ . Since the largest element of a positive definite matrix lies on the diagonal (Problem 10.1), for any $i, j, k$ there exists $r$ such that

$$
| a _ {i j} ^ {(k)} | \leq a _ {r r} ^ {(k)} \leq \dots \leq a _ {r r} ^ {(1)} = a _ {r r} \leq \max _ {i, j} | a _ {i j} |,
$$

which shows that the growth factor $\rho_{n} = 1$ (since $\rho_{n}\geq 1$ ).

10.5.From (10.8),

$$
| \widehat {R} ^ {T} | | \widehat {R} | \leq (1 - \gamma_ {n + 1}) ^ {- 1} (a _ {i i} ^ {1 / 2} a _ {j j} ^ {1 / 2}) \leq (1 - \gamma_ {n + 1}) ^ {- 1} (\underset {i} {\operatorname * {m a x}} a _ {i i}),
$$

so

$$
\parallel \left| \widehat {R} \right. ^ {T} \parallel \widehat {R} \parallel_ {M} \leq \left(1 - \gamma_ {n + 1}\right) ^ {- 1} \parallel A \parallel_ {M},
$$

as required.

10.6. $W = A_{11}^{-1}A_{12} = R_{11}^{-1}R_{12}$ , so $RZ = 0$ and hence $AZ = 0$ . $Z$ is of dimension $n \times (n - r)$ and of full rank, so it spans $\mathrm{null}(A)$ .

10.7. The inequalities (10.13) follow from the easily verified fact that, for $j \geq k$ ,

$$
a _ {j j} ^ {(k)} = \sum_ {i = k} ^ {\min  (j, r)} r _ {i j} ^ {2}.
$$

10.8. Examples of indefinite matrices with nonnegative leading principal minors are

$$
\left[ \begin{array}{c c} 0 & 0 \\ 0 & - 1 \end{array} \right] \quad \text {a n d} \quad \left[ \begin{array}{c c c} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 1 & 0 & 0 \end{array} \right].
$$

A necessary and sufficient condition for definiteness is that all the principal minors of $A$ (of which there are $2^{n-1}$ ) be nonnegative (not just the leading principal minors); see, e.g., Horn and Johnson [636, 1985, p. 405] or Mirsky [857, 1961, p. 405] (same page number in both books!).

10.9. For the matrix $Z = \left[-\left(R_{11}^{-1}R_{12}\right)^T,I\right]^T\in \mathbb{R}^{n\times (n - k)}$ we have, from (10.15), $Z^T AZ = S_k(A)$ and so we can take $p = Ze_1$ , the first column of $Z$ .

10.10. Theorem 10.3 is applicable only if Cholesky succeeds, which can be guaranteed only if the (suitably scaled) matrix $A$ is not too ill conditioned (Theorem 10.7). Therefore the standard analysis is not applicable to positive semidefinite matrices that are very close to being singular. Theorem 10.14 provides a bound on the residual after $\operatorname{rank}(A)$ stages and, in particular, on the computed Schur complement, which would be zero in exact arithmetic. The condition of Theorem 10.7 ensures that all the computed Schur complements are positive definite, so that even if magnification of errors by a factor $\| W\|_2^2$ occurs, it is absorbed by the next part of the Cholesky factor. The proposed appeal to continuity is simply not valid.

10.11. For any nonzero $x \in \mathbb{C}^n$ we have

$$
0 <   \operatorname {R e} \left[ \begin{array}{c c} x _ {1} ^ {*} & x _ {2} ^ {*} \end{array} \right] \left[ \begin{array}{c c} A _ {1 1} & A _ {1 2} \\ A _ {2 1} & A _ {2 2} \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right].
$$

Putting $x_{1} = -A_{11}^{-1}A_{12}x_{2}$ we obtain

$$
0 <   \operatorname {R e} \left[ \begin{array}{c c} x _ {1} ^ {*} & x _ {2} ^ {*} \end{array} \right] \left[ \begin{array}{c} 0 \\ - A _ {2 1} ^ {*} A _ {1 1} ^ {- 1} A _ {1 2} x _ {2} + A _ {2 2} x _ {2} \end{array} \right] = \operatorname {R e} x _ {2} ^ {*} (A _ {2 2} - A _ {2 1} ^ {*} A _ {1 1} ^ {- 1} A _ {1 2}) x _ {2},
$$

which shows that $S$ is positive definite.

11.1. If a nonsingular pivot matrix $E$ of dimension 1 or 2 cannot be found, then all $1 \times 1$ and $2 \times 2$ principal submatrices of the symmetric matrix $A$ are singular, and this is easily seen to imply that $A$ is the zero matrix.

11.2. The analysis in §11.1 shows that for a $2 \times 2$ pivot $E$ , $\operatorname{det}(E) \leq (\alpha^2 - 1)\mu_0^2$ for complete pivoting and $\operatorname{det}(E) \leq (\alpha^2 - 1)\omega_r^2$ for partial pivoting ( $r = 1$ ) and rook pivoting. Now $\alpha^2 - 1 < 0$ and $\mu_0$ and $\omega_r$ are nonzero if a $2 \times 2$ pivot is needed. Hence $\operatorname{det}(E) < 0$ , which means that $E$ has one positive and one negative eigenvalue. Note that if $A$ is positive definite it follows that all pivots are $1 \times 1$ .

If the block diagonal factor has $p_+$ positive $1 \times 1$ diagonal blocks, $p_-$ negative $1 \times 1$ diagonal blocks, $p_0$ zero $1 \times 1$ diagonal blocks, and $q \times 2$ diagonal blocks, then the inertia is $(+, -, 0) = (p_+ + q, p_- + q, p_0)$ .

Denote a $2 \times 2$ pivot by

$$
E = \left[ \begin{array}{c c} a & b \\ b & c \end{array} \right],
$$

and consider partial pivoting. We know $\operatorname{det}(E) = ac - b^2 < 0$ and $|b| \geq |a|$ , so the formula $\operatorname{det}(E) = [(a / b)c - b]b$ minimizes the risk of overflow. Similarly, the formula

$$
E ^ {- 1} = \frac {1}{b [ (a / b) (c / b) - 1 ]} \left[ \begin{array}{l l} c / b & - 1 \\ - 1 & a / b \end{array} \right]
$$

helps to avoid overflow; this is the formula used in LINPACK's xSIDI and LAPACK's xSYTRI. The same formulae are suitable for rook pivoting and complete pivoting because then $|b| \geq \max(|a|, |c|)$ .

11.3. The partial pivoting strategy simplifies as follows: if $|a_{11}| \geq \alpha |a_{21}|$ use a $1 \times 1$ pivot $a_{11}$ , if $|a_{22}| \geq \alpha |a_{12}|$ use a $1 \times 1$ pivot $a_{22}$ , else use a $2 \times 2$ pivot, that is, do nothing.

11.4. There may be interchanges, because the tests $|a_{11}| \geq \alpha \omega_1$ and $\alpha \omega_1^2 \leq |a_{11}| \omega_r$ can both fail, for example for $A = \left[ \begin{array}{cc} 1 & \theta \\ \theta & 2\theta^2 \end{array} \right]$ with $\theta > \alpha^{-1}$ . But there can be no $2 \times 2$ pivots, as they would be indefinite (Problem 11.2). Therefore the factorization is $PAP^T = LDL^T$ for a diagonal $D$ with positive diagonal entries.

11.7. That the growth factor bound is unchanged is straightforward to check. No $2 \times 2$ pivots are used for a positive definite matrix because, as before (Problem 11.2), any $2 \times 2$ pivot is indefinite. To show that no interchanges are required for a positive definite matrix we show that the second test, $\alpha \omega_1^2 \leq |a_{11}|\omega_r$ , is always passed. The submatrix $\left[ \begin{array}{cc}a_{11} & a_{r1}\\ a_{r1} & a_{rr} \end{array} \right]$ is positive definite, so $a_{11}a_{rr} - a_{r1}^2 > 0$ . Hence

$$
\left| a _ {1 1} \right| \omega_ {r} \geq a _ {1 1} a _ {r r} > a _ {r 1} ^ {2} = \omega_ {1} ^ {2} \geq \alpha \omega_ {1} ^ {2},
$$

as required.

11.8. Complete pivoting and rook pivoting both yield

$$
P A P ^ {T} = \left[ \begin{array}{c c c} 1 & 1 & 0 \\ 1 & 0 & \epsilon \\ 0 & \epsilon & 1 \end{array} \right] = \left[ \begin{array}{c c c} 1 & & \\ 1 & 1 & \\ & - \epsilon & 1 \end{array} \right] \left[ \begin{array}{c c c} 1 & & \\ & - 1 & \\ & & 1 + \epsilon^ {2} \end{array} \right] \left[ \begin{array}{c c c} 1 & 1 & \\ & 1 & - \epsilon \\ & & 1 \end{array} \right].
$$

Unlike for partial pivoting, $\| L\|_{\infty}$ is bounded independently of $\epsilon$ as $\epsilon \to 0$ .

11.9. (a) The nonsingularity of $A$ follows from the factorization

$$
\left[ \begin{array}{c c} H & B ^ {T} \\ B & - G \end{array} \right] = \left[ \begin{array}{c c} I & 0 \\ B H ^ {- 1} & I \end{array} \right] \left[ \begin{array}{c c} H & B ^ {T} \\ 0 & - (G + B H ^ {- 1} B ^ {T}) \end{array} \right],
$$

since $G + BH^{-1}B^{T}$ is symmetric positive definite.

(b) It suffices to show that the first $n + m - 1$ leading principal submatrices of $\Pi^T A \Pi$ are nonsingular for any permutation matrix $\Pi$ . But these submatrices are of the form $\overline{\Pi}^T A_p \overline{\Pi}$ , where $A_p$ is a principal submatrix of $A$ and $\overline{\Pi}$ is a permutation matrix. Any such $A_p$ is of the form

$$
A _ {p} = \left[ \begin{array}{l l} H _ {p} & B _ {p} ^ {T} \\ B _ {p} & - G _ {p} \end{array} \right],
$$

where $H_{p}$ and $G_{p}$ are principal submatrices of $H$ and $G$ , respectively, and so are positive definite. Thus $A_{p}$ is symmetric quasidefinite and hence nonsingular by (a), as required. (c)

$$
A S = \left[ \begin{array}{c c} H & - B ^ {T} \\ B & G \end{array} \right],
$$

so $(AS + (AS)^T) / 2 = \mathrm{diag}(H,G)$ , which is symmetric positive definite.

12.1.

$$
| A | | x | \leq \| A \| _ {\infty} \| x \| _ {\infty} e \leq \| A \| _ {\infty} \| x \| _ {\infty} \frac {| x |}{\operatorname* {m i n} _ {i} | x _ {i} |} = \| A \| _ {\infty} \frac {\operatorname* {m a x} _ {i} | x _ {i} |}{\operatorname* {m i n} _ {i} | x _ {i} |} | x |.
$$

12.2. The inequality (12.5) yields, with $\widehat{x}_0\coloneqq 0$ , and dropping the subscripts on the $g_{i}$ and $G_{i}$ ,

$$
| x - \widehat {x} _ {2} | \leq G | x - \widehat {x} _ {1} | + g \leq G ^ {2} | x - \widehat {x} _ {0} | + G g + g = G ^ {2} | x | + (G + I) g.
$$

Now $G \approx |F| \leq 2\gamma_n |A^{-1}| |\widehat{L}||\widehat{U}| \lesssim 2\gamma_n |A^{-1}| |B| A|$ , where $B = |\widehat{L}||\widehat{L}^{-1}|$ can be assumed to have a modest $\infty$ -norm. Now, using Problem 12.1,

$$
\begin{array}{l} G ^ {2} | x | \lesssim 2 n ^ {2} u ^ {2} | A ^ {- 1} | (B | A | | A ^ {- 1} | B) | A | | x | \\ \lesssim 2 n ^ {2} u ^ {2} \| B | A | | A ^ {- 1} | B \| _ {\infty} \sigma (A, x) | A ^ {- 1} | | A | | x | \\ \leq 2 n ^ {2} \| B \| _ {\infty} ^ {2} \cdot u \operatorname {c o n d} \left(A ^ {- 1}\right) \sigma (A, x) \cdot u | A ^ {- 1} | | A | | x | \\ \lesssim 2 n ^ {2} \| B \| _ {\infty} ^ {2} \cdot u | A ^ {- 1} | | A | | x |, \\ \end{array}
$$

under the conditions of Theorem 12.4. The term $Gg$ can be bounded in a similar way. The required bound for $\| x - \widehat{x}_2\|_\infty /\| x\|_\infty$ follows.

13.1. The equations for the blocks of $L$ and $U$ are $U_{11} = A_{11}$ and

$$
\left. \begin{array}{c}L _ {i, i - 1} = A _ {i, i - 1} U _ {i - 1, i - 1} ^ {- 1} \\ U _ {i i} = A _ {i i} - L _ {i, i - 1} A _ {i - 1, i} \end{array} \right\} \quad i \geq 2.
$$

First, consider the case where $A$ is block diagonally dominant by columns. We prove by induction that

$$
\left\| A _ {k, k - 1} \right\| \left\| U _ {k - 1, k - 1} ^ {- 1} \right\| \leq 1, \quad k \geq 2.
$$

which implies both the required bounds. This inequality clearly holds for $k = 2$ ; suppose it holds for $k = i$ . We have

$$
U _ {i i} = A _ {i i} \left(I - A _ {i i} ^ {- 1} L _ {i, i - 1} A _ {i - 1, i}\right) =: A _ {i i} (I - P),
$$

where

$$
\begin{array}{l} \| P \| \leq \| A _ {i i} ^ {- 1} \| \left(\| A _ {i, i - 1} \| \| U _ {i - 1, i - 1} ^ {- 1} \|\right) \| A _ {i - 1, i} \| \\ \leq \left\| A _ {i i} ^ {- 1} \right\| \left\| A _ {i - 1, i} \right\| \\ \leq 1 - \left\| A _ {i i} ^ {- 1} \right\| \left\| A _ {i + 1, i} \right\|, \\ \end{array}
$$

using the block diagonal dominance for the last inequality. Hence

$$
\| U _ {i i} ^ {- 1} \| \leq \frac {\| A _ {i i} ^ {- 1} \|}{1 - \| P \|} \leq \frac {1}{\| A _ {i + 1 , i} \|},
$$

as required.

The proof for $A$ block diagonally dominant by rows is similar. The inductive hypothesis is that

$$
\left\| U _ {k - 1, k - 1} ^ {- 1} \right\| \left\| A _ {k - 1, k} \right\| \leq 1,
$$

and with $P$ defined as before, we have

$$
\begin{array}{l} \| P \| \leq \| A _ {i i} ^ {- 1} \| \| A _ {i, i - 1} \| \| U _ {i - 1, i - 1} ^ {- 1} \| \| A _ {i - 1, i} \| \\ \leq \left\| A _ {i i} ^ {- 1} \right\| \left\| A _ {i, i - 1} \right\| \\ \leq 1 - \left\| A _ {i i} ^ {- 1} \right\| \left\| A _ {i, i + 1} \right\|, \\ \end{array}
$$

giving $\| U_{ii}^{-1}\| \leq \| A_{i,i + 1}\|^{-1}$ , as required.

For block diagonal dominance by columns in the $\infty$ -norm we have $\|L\|_{\infty} \leq 2$ and $\|U\|_{\infty} \leq 3\|A\|_{\infty}$ , so block LU factorization is stable. If $A$ is block diagonally dominant by rows, stability is assured if $\|A_{i,i-1}\|/\|A_{i-1,i}\|$ is suitably bounded for all $i$ .

13.2. The block $2 \times 2$ matrix

$$
\left[ \begin{array}{cc|cc} \epsilon & 2 & 1 & 0 \\ 2 & \epsilon & 0 & 1 \\ \hline 1 & 0 & \epsilon & 2 \\ 0 & 1 & 2 & \epsilon \\ \end{array} \right]
$$

is block diagonally dominant by rows and columns in the 1- and $\infty$ -norms for $\epsilon = 1/2$ , but is not point diagonally dominant by rows or columns. The block $2 \times 2$ matrix

$$
\left[ \begin{array}{c c c c} 2 & 1 & 1 & 0 \\ 1 & 1 & 0 & 0 \\ \hline 1 & 0 & 2 & 1 \\ 0 & 0 & 1 & 1 \end{array} \right]
$$

is point diagonally dominant by rows and columns but not block diagonally dominant by rows or columns in the $\infty$ -norm or 1-norm.

13.3. No. A counterexample is the first matrix in the solution to Problem 13.2, with $\epsilon = 1/2$ , which is clearly not positive definite because the largest element does not lie on the diagonal.

13.4. From (13.2) it can be seen that $(A^{-1})_{21} = -S^{-1}A_{21}A_{11}^{-1}$ , where the Schur complement $S = A_{22} - A_{21}A_{11}^{-1}A_{12}$ . Hence

$$
\left\| A _ {2 1} A _ {1 1} ^ {- 1} \right\| \leq n \| S \| \left\| \left(A ^ {- 1}\right) _ {2 1} \right\| \leq n \| S \| \left\| A ^ {- 1} \right\|,
$$

where the factor $n$ comes from the fact that this norm is not consistent—see §6.2. $S$ is the trailing submatrix that would be obtained after $r - 1$ steps of GE. It follows immediately that $\| S \| \leq \rho_n \| A \|$ .

For the last part, note that $\| S^{-1} \| \leq \| A^{-1} \|$ , because $S^{-1}$ is the $(2,2)$ block of $A^{-1}$ , as is easily seen from (13.2).

13.5. The proof is similar to that of Problem 8.7(a). We will show that $\| A_{11}^{-T}A_{21}^{T}\|_{\infty}\leq 1$ Let $y = A_{11}^{-T}A_{21}^{T}x$ and let $|y_{k}| = \| y\|_{\infty}$ . The kth equation of $A_{11}^{T}y = A_{21}^{T}x$ gives

$$
a_{kk}y_{k} = \sum_{i = r + 1}^{n}a_{ik}x_{i - r} - \sum_{\substack{i = 1\\ i\neq k}}^{r}a_{ik}y_{i}.
$$

Hence

$$
\| y \| _ {\infty} = | y _ {k} | \leq \| x \| _ {\infty} \sum_ {i = r + 1} ^ {n} \left| \frac {a _ {i k}}{a _ {k k}} \right| + \| y \| _ {\infty} \sum_ {i = 1 \atop i \neq k} ^ {r} \left| \frac {a _ {i k}}{a _ {k k}} \right|,
$$

which yields $\| y\|_{\infty}\leq \| x\|_{\infty}$ in view of the column diagonal dominance, as required.

13.7. We have the block LU factorization

$$
X = \left[ \begin{array}{l l} A & B \\ C & D \end{array} \right] = \left[ \begin{array}{c c} I & 0 \\ C A ^ {- 1} & I \end{array} \right] \left[ \begin{array}{c c} A & B \\ 0 & D - C A ^ {- 1} B \end{array} \right],
$$

so that

$$
\det  (X) = \det  (A) \det  (D - C A ^ {- 1} B).
$$

Hence $\operatorname{det}(X) = \operatorname{det}(AD - ACA^{-1}B)$ , which equals $\operatorname{det}(AD - CB)$ if $C$ commutes with $A$ .

13.8. The result is obtained by inverting

$$
\left[ \begin{array}{c c} A & B \\ C & D \end{array} \right] ^ {- 1} = \left[ \begin{array}{c c} I & 0 \\ C A ^ {- 1} & I \end{array} \right] \left[ \begin{array}{c c} A & B \\ 0 & S \end{array} \right].
$$

13.9. We have

$$
\left[ \begin{array}{c c} I & A \\ B & I \end{array} \right] = \left[ \begin{array}{c c} I & 0 \\ B & I \end{array} \right] \left[ \begin{array}{c c} I & A \\ 0 & I - B A \end{array} \right] = \left[ \begin{array}{c c} I & A \\ 0 & I \end{array} \right] \left[ \begin{array}{c c} I - A B & 0 \\ B & I \end{array} \right].
$$

Inverting both factorizations and equating (1,1) blocks gives the required relation. The Sherman-Morrison-Woodbury formula is obtained by setting $A = T^{-1}U$ and $B = W^{-1}V^T$ .

14.2. The new bounds have norms in place of absolute values and the constants are different.

14.3. Immediate from $AX - I = A(XA - I)A^{-1}$ .

14.4. With $0 < \epsilon \ll 1$ , let

$$
A = \left[ \begin{array}{c c} \frac {1}{\epsilon} & 1 \\ \frac {1}{\epsilon^ {2}} - 1 & \frac {1}{\epsilon} \end{array} \right], \qquad X = \left[ \begin{array}{c c} 1 - \epsilon + \frac {2}{\epsilon} & - 2 - \epsilon \\ 2 - \epsilon + \frac {1}{\epsilon} - \frac {1}{\epsilon^ {2}} & - 1 - \epsilon + \frac {1}{\epsilon} \end{array} \right].
$$

Then

$$
A X = \left[ \begin{array}{l l} O (\epsilon^ {- 2}) & O (\epsilon^ {- 1}) \\ O (\epsilon^ {- 3}) & O (\epsilon^ {- 2}) \end{array} \right]
$$

while

$$
X A = \left[ \begin{array}{c c} 1 + \epsilon & - \epsilon \\ \epsilon & 1 - \epsilon \end{array} \right].
$$

Hence $\|AX - I\| / \|XA - I\| \to \infty$ as $\epsilon \to 0$ . Note that in this example every element of $AX - I$ is large.

14.5. We have $\widehat{x} = fl(\widehat{X} b) = \widehat{X} b + f_1$ , where $|f_1| \leq \gamma_n |\widehat{X}| |b|$ . Hence $A\widehat{x} = A\widehat{X} b + Af_1 = b + r_1$ , where $|r_1| \leq u |A||\widehat{X}||b| + \gamma_n |A||\widehat{X}||b| \leq \gamma_{n+1} |A||\widehat{X}||b|$ . Similarly,

$$
\hat {y} = f l (\hat {Y} b) = \hat {Y} b + f _ {2}, \quad | f _ {2} | \leq \gamma_ {n} | \hat {Y} | | b |. \tag {A.13}
$$

Hence $A\widehat{y} = A\widehat{Y} b + Af_{2} = A(\widehat{Y} A)x + Af_{2} = b + r_{2}$ , where

$$
| r _ {2} | \leq u | A | | \widehat {Y} | | A | | x | + \gamma_ {n} | A | | \widehat {Y} | | b | \leq \gamma_ {n + 1} | A | | \widehat {Y} | | A | | x |.
$$

Clearly,

$$
\left| x - \widehat {x} \right| \leq (n + 1) u \left| A ^ {- 1} \right| \left| A \right| \left| A ^ {- 1} \right| \left| b \right| + O \left(u ^ {2}\right).
$$

From (A.13), $\widehat{y} = \widehat{Y} Ax + f_2$ , so

$$
| y - \widehat {y} | \leq u | \widehat {Y} | | A | | x | + \gamma_ {n} | \widehat {Y} | | b | \leq (n + 1) u | A ^ {- 1} | | A | | x | + O (u ^ {2}).
$$

The first conclusion is that the approximate left inverse yields the smaller residual bound, while the approximate right inverse yields the smaller forward error bound. Therefore which inverse is "better" depends on whether a small backward error or a small forward error is desired. The second conclusion is that neither approximate inverse yields a componentwise backward stable algorithm, despite the favourable assumptions on $\widehat{X}$ and $\widehat{Y}$ . Multiplying by an explicit inverse is simply not a good way to solve a linear system.

14.6. Here is a hint: notice that the matrix on the front cover of the LAPACK Users' Guide has the form

$$
\left[ \begin{array}{c c c} 1 & 1 & 1 \\ 1 & 1 & - 1 \\ 1 & - 1 & 1 \end{array} \right] \otimes \left[ \begin{array}{c c} 1 & 1 \\ 1 & - 1 \end{array} \right] \mathrm {d i a g} (L, A, P, A, C, K).
$$

14.7. If the $i$ th row of $A$ contains all 1s then simply sum the elements in the $i$ th row of the equation $AA^{-1} = I$ .

14.8. $(A + iB)(P + iQ) = I$ is equivalent to $AP - BQ = I$ and $AQ + BP = 0$ , or

$$
\left[ \begin{array}{c c} A & - B \\ B & A \end{array} \right] \left[ \begin{array}{c} P \\ Q \end{array} \right] = \left[ \begin{array}{c} I \\ 0 \end{array} \right],
$$

so $X^{-1}$ is obtainable from the first $n$ columns of $Y^{-1}$ . The definiteness result follows from

$$
\begin{array}{l} (x + i y) ^ {*} (A + i B) (x + i y) = x ^ {T} (A x - B y) + y ^ {T} (A y + B x) \\ + i \left[ x ^ {T} (A y + B x) - y ^ {T} (A x - B y) \right] \\ = \left[ \begin{array}{c c} x ^ {T} & y ^ {T} \end{array} \right] \left[ \begin{array}{c c} A & - B \\ B & A \end{array} \right] \left[ \begin{array}{c} x \\ y \end{array} \right], \\ \end{array}
$$

where we have used the fact that $A = A^T$ and $B = -B^T$ . Doubling the dimension (from $X$ to $Y$ ) multiplies the number of flops by a factor of 8, since the flop count for inversion is cubic in the dimension. Yet complex operations should, in theory, cost between about two and eight times as much as real ones (the extremes being for addition and division). The actual relative costs of inverting $X$ and $Y$ depend on the machine and the compiler, so it is not possible to draw any firm conclusions. Note also that $Y$ requires twice the storage of $X$ .

14.10. As in the solution to Problem 8.8, we have

$$
\det  (A + \alpha e _ {i} e _ {j} ^ {T}) = \det  (A) (1 + \alpha e _ {j} ^ {T} A ^ {- 1} e _ {i}).
$$

If $(A^{-1})_{ji} = 0$ , this expression is independent of $\alpha$ , and hence $\operatorname{det}(A)$ is independent of $a_{ij}$ . (This result is clearly correct for a triangular matrix.) That $\operatorname{det}(A)$ can be independent of $a_{ij}$ shows that $\operatorname{det}(A)$ , or even a scaling of it, is an arbitrarily poor measure of conditioning, for $A + \alpha e_i e_j^T$ approaches a multiple of a rank-1 matrix as $\alpha \to \infty$ .

14.11. That Hadamard's inequality can be deduced from QR factorization was noted by Householder [643, 1958, p. 341]. From $A = QR$ we have $q_k^T A = e_k^T R$ , so that

$$
\left| r _ {k k} \right| = \left| q _ {k} ^ {T} a _ {k} \right| \leq \left\| a _ {k} \right\| _ {2}.
$$

Hadamard's inequality follows since $|\operatorname{det}(A)| = |\operatorname{det}(R)| = |r_{11} \ldots r_{nn}|$ . There is equality when $|q_k^T a_k| = \|a_k\|_2$ for $k = 1:n$ , that is, when $a_k = \alpha_k q_k$ , $k = 1:n$ , for some scalars $\alpha_k$ . In other words, there is equality when $R$ in the QR factorization is diagonal.

14.12. (a) Straightforward. (b) For $A = U(1)$ , $\psi(A) = \sqrt{n!}$ . For the Pei matrix, $\psi(A) = (\alpha^2 + n - 1)^{n/2} / ((n + \alpha - 1)(\alpha - 1)^{n-1})$ .   
14.13. (a) The geometric mean of $\sigma_1^2 / 2$ , $\sigma_1^2 / 2$ , $\sigma_2^2$ , ..., $\sigma_{n-1}^2$ is

$$
\left(\frac {1}{4} \sigma_ {1} ^ {4} \sigma_ {2} ^ {2} \dots \sigma_ {n - 1} ^ {2}\right) ^ {1 / n} = \left(\frac {1}{4} \frac {\sigma_ {1} ^ {2}}{\sigma_ {n} ^ {2}} \sigma_ {1} ^ {2} \sigma_ {2} ^ {2} \dots \sigma_ {n} ^ {2}\right) ^ {1 / n} = \left(\frac {1}{2} \kappa_ {2} (A) | \operatorname * {d e t} (A) |\right) ^ {2 / n}.
$$

Since the geometric mean does not exceed the arithmetic mean,

$$
\left(\frac {1}{2} \kappa_ {2} (A) | \det  (A) |\right) ^ {2 / n} \leq \frac {1}{n} \left(\sigma_ {1} ^ {2} + \dots + \sigma_ {n - 1} ^ {2}\right) <   \frac {1}{n} \left(\sigma_ {1} ^ {2} + \dots + \sigma_ {n} ^ {2}\right) = \frac {1}{n} \| A \| _ {F} ^ {2},
$$

which gives the required bound. (b) is trivial.

14.14. The key observation is that for a triangular system $Tx = b$ , $T \in \mathbb{R}^{n \times n}$ , the computed solution from substitution satisfies

$$
(T + \Delta T) \hat {x} = b + \Delta b, \quad | \Delta T | \leq \gamma_ {n} | T |, \quad \operatorname {d i a g} (T) = 0, \quad | \Delta b | \leq \gamma_ {n} | b |. \tag {A.14}
$$

This result holds for any order of evaluation and is proved (for any particular order of evaluation) using a variation on the proof of Lemma 8.2 in which we do not divide through by the product of $1 + \delta_{i}$ terms. Using (A.14) we have

$$
\widehat {d} = \left(1 + \theta_ {n}\right) \det  (T) \big (\eta - \left(h + \varDelta h\right) ^ {T} (T + \varDelta T) ^ {- 1} (y + \varDelta y) \big),
$$

where $|\theta_n| \leq \gamma_n, |\Delta y| \leq \gamma_{n-1}|y|$ , and $|\Delta h| \leq \gamma_{n-1}|h|$ . But, since $\operatorname{diag}(\Delta T) = 0$ , $\det(T) = \det(T + \Delta T)$ , hence

$$
\widehat {d} = \det  (T + \Delta T) \big (\eta (1 + \theta_ {n}) - (h + \widetilde {\Delta h}) ^ {T} (T + \Delta T) ^ {- 1} (y + \Delta y) \big),
$$

where $|\widetilde{\Delta} h| \leq \gamma_{2n-1}|h|$ . The conclusion is that $\widehat{d} = \det(H + \Delta H)$ , where $|\Delta H| \leq \gamma_{2n-1}|H|$ .

If $\widehat{f} = f l(\operatorname*{det}(D^{-1}H D))$ then

$$
\widehat {f} = \det  (D ^ {- 1} H D + \Delta), \quad | \Delta | \leq \gamma_ {2 n - 1} | D ^ {- 1} H D | = \gamma_ {2 n - 1} | D ^ {- 1} | | H | D |.
$$

Thus

$$
\widehat {f} = \det  (D ^ {- 1} (H + D \Delta D ^ {- 1}) D) = \det  (H + D \Delta D ^ {- 1}), \quad | D \Delta D ^ {- 1} | \leq \gamma_ {2 n - 1} | H |.
$$

A diagonal similarity therefore has no effect on the error bound and so there is no point in scaling $H$ before applying Hyman's method.

14.15. We use the fact that $\operatorname{det}(A) = \prod_{i=1}^{n} \sigma_i(A)$ , where $\sigma_i(A)$ is the $i$ th largest singular value of $A$ . We have

$$
\frac {\det  (A + \Delta A) - \det  (A)}{\det  (A)} = \prod_ {i = 1} ^ {n} \frac {\sigma_ {i} (A + \Delta A)}{\sigma_ {i} (A)} - 1.
$$

Now, using standard singular value inequalities [509, 1996, §8.6],

$$
\frac {\sigma_ {i} (A + \Delta A)}{\sigma_ {i} (A)} \leq \frac {\sigma_ {i} (A) + \sigma_ {1} (\Delta A)}{\sigma_ {i} (A)} \leq 1 + \frac {\sigma_ {1} (\Delta A)}{\sigma_ {n} (A)} = 1 + \kappa_ {2} (A) \frac {\| \Delta A \| _ {2}}{\| A \| _ {2}}
$$

and

$$
\frac {\sigma_ {i} (A + \Delta A)}{\sigma_ {i} (A)} \geq \frac {\sigma_ {i} (A) - \sigma_ {1} (\Delta A)}{\sigma_ {i} (A)} \geq 1 - \frac {\sigma_ {1} (\Delta A)}{\sigma_ {n} (A)} = 1 - \kappa_ {2} (A) \frac {\| \Delta A \| _ {2}}{\| A \| _ {2}}.
$$

Hence

$$
\prod_ {i = 1} ^ {n} \frac {\sigma_ {i} (A + \Delta A)}{\sigma_ {i} (A)} - 1 = \prod_ {i = 1} ^ {n} (1 + \theta_ {i}) - 1, \quad | \theta_ {i} | \leq \kappa_ {2} (A) \frac {\| \Delta A \| _ {2}}{\| A \| _ {2}}, \quad i = 1: n,
$$

and the result follows from Lemma 3.1.

15.1. We have

$$
\begin{array}{l} \| | A | | A ^ {- 1} | | A | \| _ {\infty} = \| | A | | A ^ {- 1} | | A | e \| _ {\infty} \\ = \left\| | A | | A ^ {- 1} | D _ {1} e \right\| _ {\infty}, \quad D _ {1} = \operatorname {d i a g} (| A | e) \\ = \left\| | A | | A ^ {- 1} | D _ {1} \right\| _ {\infty} \\ \approx \parallel | A | \parallel A ^ {- 1} | D _ {1} \parallel_ {1} \\ = \left\| D _ {1} \right\vert A ^ {- T} \left\| A ^ {T} \right\vert \| _ {\infty} \\ = \| D _ {1} | A ^ {- T} | D _ {2} \| _ {\infty}, \quad D _ {2} = \operatorname {d i a g} (| A ^ {T} | e) \\ = \left\| D _ {1} A ^ {- T} D _ {2} \right\| _ {\infty}, \\ \end{array}
$$

where $\approx$ means "within a factor $n$ of".

15.4. Straightforward, since $L$ is unit lower triangular with $|l_{ij}|\leq 1$ .

15.7. Let $D = \mathrm{diag}(d_j)$ , where $d_1 = 1$ and

$$
d _ {j} = \prod_ {k = 1} ^ {j - 1} \frac {a _ {k , k + 1}}{a _ {k + 1 , k}}, \qquad j = 2: n.
$$

Then $T = DA$ is tridiagonal, symmetric and irreducible. By applying Theorem 15.9 and using symmetry, we find that

$$
(A ^ {- 1}) _ {i j} = \left\{ \begin{array}{l l} x _ {i} y _ {j} d _ {j}, & i \leq j, \\ y _ {i} x _ {j} d _ {j}, & i \geq j. \end{array} \right.
$$

There is one degree of freedom in the vectors $x$ and $y$ , which can be expended by setting $x_{1} = 1$ , say.

16.1. The equation would imply, on taking traces, $0 = \operatorname{trace}(I)$ , which is false.

16.2. It is easily checked that the differential equation given in the hint has the solution $Z(t) = e^{At}Ce^{Bt}$ . Integrating the differential equation between 0 and $\infty$ gives, assuming that $\lim_{t\to \infty}Z(t) = 0$ ,

$$
- C = A \left(\int_ {0} ^ {\infty} Z (t)\right) d t + \left(\int_ {0} ^ {\infty} Z (t) d t\right) B.
$$

Hence $-\int_0^\infty Z(t)dt = -\int_0^\infty e^{At}Ce^{Bt}dt$ satisfies the Sylvester equation. For the Lyapunov equation, the integral $-\int_0^\infty e^{At}(-C)e^{A^T t}dt$ exists under the assumption on $A$ , and the corresponding quadratic form is easily seen to be positive.

# 16.3. Since

$$
\left\| A X + X A ^ {T} \right\| _ {F} = \left\| \left(A X + X A ^ {T}\right) ^ {T} \right\| _ {F} = \left\| A X ^ {T} + X ^ {T} A ^ {T} \right\| _ {F},
$$

$X^T$ is a minimizer if $X$ is. If $X + X^{T} = 0$ then $X$ is a skew-symmetric minimizer. Otherwise, note that the minimization problem is equivalent to finding the right singular vector corresponding to the smallest singular value $\sigma_{\mathrm{min}}$ of $P = I\otimes A + A\otimes I$ . Since $\operatorname {vec}(X)$ and $\operatorname {vec}(X^T)$ (suitably normalized) are both singular vectors corresponding to $\sigma_{\mathrm{min}}$ , so is their sum, $\operatorname {vec}(X + X^T)\neq 0$ . Thus the symmetric matrix $X + X^{T}$ is a minimizer.

Byers and Nash [195, 1987] investigate conditions under which a symmetric minimizer exists.

16.4. xLASY2 uses Gaussian elimination with complete pivoting to solve the $2 \times 2$ or $4 \times 4$ linear system that arises on converting to the Kronecker product form (16.2). For complete pivoting on a $4 \times 4$ matrix the growth factor is bounded by 4 (§9.4), versus 8 for partial pivoting. The reasons for using complete pivoting rather than partial pivoting are that, first, the small increase in cost is regarded as worthwhile for a reduction in the error bound by a factor of 2 and, second, complete pivoting reveals the rank better than partial pivoting, enabling better handling of ill-conditioned systems [46, 1993, p. 78].

17.1. Since $\rho(B) < 1$ , a standard result (Problem 6.8) guarantees the existence of a consistent norm $\| \cdot \|_{\rho}$ for which $\| B \|_{\rho} < 1$ . The series $\sum_{k=0}^{\infty} \| B^{k} \|_{\rho} \leq \sum_{k=0}^{\infty} \| B \|_{\rho}^{k} = (1 - \| B \|_{\rho})^{-1}$ is clearly convergent, and so, by the equivalence of norms, $\sum_{k=0}^{\infty} \| B^{k} \|$ is convergent for any norm.

Since $(|B^k|)_{ij} \leq \| B^k\|_\infty$ , the convergence of $\sum_{k=0}^\infty \| B^k\|_\infty$ ensures that of $\sum_{k=0}^\infty |B^k|$ . (The convergence of $\sum_{k=0}^\infty |B^k|$ can also be proved directly using the Jordan canonical form.)

18.1. Let $X_{n}$ be the $n \times n$ version of the upper triangular matrix

$$
\left[ \begin{array}{cccc} 1 & - \theta & - \theta & - \theta \\  & 1 & - \theta & - \theta \\  &  & 1 & - \theta \\  &  &  & 1 \end{array} \right] D ^ {- 1}, \qquad \theta > 0,
$$

where $D = \mathrm{diag}(\sqrt{1 + (j - 1)\theta^2})$ , so that $\| X_{n}(:,j)\|_{2} = 1$ , $j = 1:n$ . From (8.4), $X_{n}^{-1}$ is the obvious $n\times n$ analogue of

$$
D \left[ \begin{array}{cccc} 1 & \theta & \theta (\theta + 1) & \theta (\theta + 1) ^ {2} \\ & 1 & \theta & \theta (\theta + 1) \\ & & 1 & \theta \\ & & & 1 \end{array} \right].
$$

Let $\varLambda=\mathrm{diag}(0,\ldots,0,\lambda)$ , with $|\lambda|<1$ . Then

$$
\begin{array}{l} \| A ^ {k} \| _ {2} = \| X _ {n} \Lambda^ {k} X _ {n} ^ {- 1} \| _ {2} = | \lambda | ^ {k} \| X _ {n} e _ {n} e _ {n} ^ {T} X _ {n} ^ {- 1} \| _ {2} \\ = | \lambda | ^ {k} \| X _ {n} (:, n) \| _ {2} \| X _ {n} ^ {- 1} (n,:) \| _ {2} = | \lambda | ^ {k} \sqrt {1 + (n - 1) \theta^ {2}}. \\ \end{array}
$$

But

$$
\kappa_ {2} (X _ {n}) \rho (A) ^ {k} \geq | \lambda | ^ {k} \max  _ {i, j} | x _ {i j} | \max  _ {i, j} | (X _ {n} ^ {- 1}) _ {i j} | \geq | \lambda | ^ {k} \theta^ {n - 1}.
$$

Therefore $\kappa_{2}(X_{n})\rho (A)^{k} / \| A^{k}\|_{2}\to \infty$ as $\theta \rightarrow \infty$ . There is still the question of whether $X_{n}$ is optimally scaled. We can perturb the zero eigenvalues of $A$ to distinct, sufficiently small numbers so that $\| A^k\| _2$ is essentially unchanged and so that the only freedom in $X_{n}$ is a diagonal scaling. Since $X_{n}$ has columns of unit 2-norm, $\min_{F = \mathrm{diag}(f_i)}\kappa_2(X_nF)\geq n^{-1 / 2}\kappa_2(X_n)$ (Theorem 7.5), so even for the optimally scaled $X_{n}$ the bound can be arbitrarily poor.

18.2. A simple example is

$$
A = \left[ \begin{array}{c c c} 1 & 2 & 2 \\ 2 & 1 & 2 \\ \alpha & - \alpha & 1 \end{array} \right],
$$

for which $\lambda(A) = \{-1, 1, 3\}$ and $\lambda(|A|) = \{-1, 2 \pm (4\alpha + 1)^{1/2}\}$ , so $\rho(|A|)/\rho(A) \to \infty$ as $\alpha \to \infty$ .

19.1. For the Householder matrix $I - (2 / v^T v) vv^T$ there is an eigenvalue $-1$ with eigenvector $v$ , and there are $n - 1$ eigenvalues $1$ , with eigenvectors any basis for $\operatorname{span}(v)^\perp$ . A Givens matrix $G(i, j, \theta)$ has eigenvalues $e^{\pm i\theta}$ , together with $n - 2$ eigenvalues $1$ .

19.2. Straightforward manipulation shows that a bound holds of the form $cnu + O(u^2)$ , where $c$ is a constant of order 10.

19.3. We must have $x^{*}Px = x^{*}y$ , so $x^{*}y$ must be real. Also, we need $x^{*}x = y^{*}y$ and $x \neq y$ . Then, with $v = x - y$ , $v^{*}v = 2v^{*}x$ , so $Px = y$ .

LAPACK uses modified Householder matrices $P = I - \tau vv^{*}$ that are unitary but not Hermitian ( $\tau$ is not real). The benefit of this approach is that such a $P$ can always be chosen so that $Px = \alpha e_{1}$ , with $\alpha$ real (for this equation to hold for a genuine Householder matrix $P$ it would be necessary that $x_{1}$ be real). For more details see Lehoucq [780, 1996].

19.4. False. $\operatorname{det}(P) = -1$ for any Householder matrix and $\operatorname{det}(G) = 1$ for any Givens matrix, so $\operatorname{det}(Q) = 1$ . Moreover, whereas $P$ is generally a full, symmetric matrix, $Q$ has some zero entries and is generally nonsymmetric.

19.5. The inequalities follow from the fact that, in the notation of (19.3), $\| x_{k}\|_{2} = |r_{kk}|$ and $\| c_k(:,j)\| _2^2 = \sum_{i = k}^{j}r_{ij}^2$ , the latter equality being a consequence of the invariance of the 2-norm under orthogonal transformations. The last part follows because QR factorization with column pivoting on $A$ is essentially equivalent to Cholesky factorization with complete pivoting applied to $A^T A$ .

19.6. The second inequality in (19.38) follows from (19.1) and the first from

$$
v _ {k} ^ {T} v _ {k} = \left| 2 \sigma_ {k} \left(\sigma_ {k} - a _ {k k} ^ {(k)}\right) \right| \geq 2 \sigma_ {k} ^ {2} = 2 \| a _ {k} ^ {(k)} (k: m) \| _ {2} ^ {2}.
$$

From the proof of Lemma 19.2 we see that (19.39) holds with $f_{j}^{(k)}(1:k - 1) = 0$ and

$$
| f _ {j} ^ {(k)} | \leq u | \widehat {a} _ {j} ^ {(k)} | + \tilde {\gamma} _ {m - k} \left(| \beta_ {k} | | v _ {k} | ^ {T} | \widehat {a} _ {j} ^ {(k)} |\right) | v _ {k} |.
$$

Now

$$
\begin{array}{l} \left(| \beta_ {k} | | v _ {k} | ^ {T} | \widehat {a} _ {j} ^ {(k)} |\right) | v _ {k} | = 2 \frac {\left| v _ {k} \right| ^ {T} \left| \widehat {a} _ {j} ^ {(k)} \right|}{\left\| v _ {k} \right\| _ {2} ^ {2}} | v _ {k} | \\ \leq 2 \frac {\| \widehat {a} _ {j} ^ {(k)} (k : m) \| _ {2}}{\| v _ {k} (k : m) \| _ {2}} | v _ {k} | \\ \leq \sqrt {2} \frac {\left\| \widehat {a} _ {j} ^ {(k)} (k : m) \right\| _ {2}}{\left\| \widehat {a} _ {k} ^ {(k)} (k : m) \right\| _ {2}} \left| v _ {k} \right|, \\ \end{array}
$$

using (19.38), and (19.40) follows. Consider a badly row-scaled problem and $k = 1$ , and assume that $v_{1}$ has the same scaling as $a_{j}^{(1)}$ (which row pivoting or row sorting both ensure). Then the bound (19.40) shows that the error will scale in the same way as long as $\| \widehat{a}_{j}^{(1)}(1:m)\|_{2} / \| \widehat{a}_{1}^{(1)}(1:m)\|_{2}$ is not too large; column pivoting guarantees that this ratio is bounded by 1. For the full development of this argument see Higham [614, 2000].

19.7. If $y = |W|x$ and $W$ comprises $r$ disjoint rotations then, in a rather loose notation,

$$
\begin{array}{l} \| y \| _ {2} ^ {2} \leq \sum_ {k = 1} ^ {r} \left\| \left| \left[ \begin{array}{c c} c _ {k} & s _ {k} \\ - s _ {k} & c _ {k} \end{array} \right] \right| \left[ \begin{array}{c} x _ {i _ {k}} \\ x _ {j _ {k}} \end{array} \right] \right\| _ {2} ^ {2} + \sum_ {k = 2 r + 1} ^ {m} x _ {i _ {k}} ^ {2} \\ \leq 2 \sum_ {k = 1} ^ {2 r} x _ {i _ {k}} ^ {2} + \sum_ {k = 2 r + 1} ^ {m} x _ {i _ {k}} ^ {2} \leq 2 \| x \| _ {2} ^ {2}. \\ \end{array}
$$

19.8. Straightforward. This problem shows that the CGS and MGS methods correspond to two different ways of representing the orthogonal projection onto $\operatorname{span}\{q_1, \ldots, q_j\}$ .

19.9. Assume, without loss of generality, that $\|a_1\|_2 \leq \|a_2\|_2$ . If $E$ is any matrix such that $A + E$ is rank deficient then

$$
0 = \sigma_ {\min } (A + E) \geq \sigma_ {\min } (A) - \| E \| _ {2} \Rightarrow \sigma_ {\min } (A) \leq \| E \| _ {2}.
$$

We take $E = [e_1, 0]$ , where $e_1$ is chosen so that $e_1^T a_1 = 0$ and $a_1 + e_1 = \alpha a_2$ , for some $\alpha$ . From Pythagoras's theorem we have that $\| e_1 \|_2 = \tan \theta \| a_1 \|_2$ , and so

$$
\sigma_ {\min } (A) \leq \tan \theta \| a _ {1} \| _ {2} = \tan \theta \min  (\| a _ {1} \| _ {2}, \| a _ {2} \| _ {2}).
$$

Together with the trivial bound $\sigma_{\max}(A) = \| A\| _2\geq \max (\| a_1\| _2,\| a_2\| _2)$ , this yields the result.

19.10. We find that

$$
\widehat {Q} _ {C G S} = \left[ \begin{array}{c c c} 1 & 0 & 0 \\ \epsilon & - \frac {1}{\sqrt {2}} & - \frac {1}{\sqrt {2}} \\ 0 & \frac {1}{\sqrt {2}} & 0 \\ 0 & 0 & \frac {1}{\sqrt {2}} \end{array} \right], \qquad \widehat {Q} _ {M G S} = \left[ \begin{array}{c c c} 1 & 0 & 0 \\ \epsilon & - \frac {1}{\sqrt {2}} & - \frac {1}{\sqrt {6}} \\ 0 & \frac {1}{\sqrt {2}} & - \frac {1}{\sqrt {6}} \\ 0 & 0 & \sqrt {\frac {2}{3}} \end{array} \right].
$$

For $\widehat{Q}_{MGS}$ , $|\widehat{q}_i^T\widehat{q}_j| \leq \epsilon/\sqrt{2}$ for $i \neq j$ , but for $\widehat{Q}_{CGS}$ , $|\widehat{q}_2^T\widehat{q}_3| = 1/2$ . It is easy to see that $fl(1 + \epsilon^2) = 1$ implies $\epsilon \leq \sqrt{u}$ and that $\kappa_2(A) = \epsilon^{-1}\sqrt{3 + \epsilon^2}$ . Hence for $\widehat{Q}_{MGS}$ , $|\widehat{q}_i^T\widehat{q}_j| \lesssim \kappa_2(A)u/\sqrt{6}$ , showing, as expected, that the loss of orthogonality for MGS is bounded in terms of $\kappa_2(A)u$ .

19.11. $P$ is the product $P_{n} \ldots P_{1}$ , where $P_{k}$ is defined in (19.28). Since $v_{k}^{T}v_{k - 1} = e_{k}^{T}e_{k - 1} + q_{k}^{T}q_{k - 1} = 0$ , we have

$$
P _ {k} P _ {k - 1} = \left(I - v _ {k} v _ {k} ^ {T}\right) \left(I - v _ {k - 1} v _ {k - 1} ^ {T}\right) = I - v _ {k} v _ {k} ^ {T} - v _ {k - 1} v _ {k - 1} ^ {T}.
$$

Hence

$$
P = I - \sum_ {k = 1} ^ {n} v _ {k} v _ {k} ^ {T} = I - \sum_ {k = 1} ^ {n} \left[ \begin{array}{c c} e _ {k} e _ {k} ^ {T} & - e _ {k} q _ {k} ^ {T} \\ - q _ {k} e _ {k} ^ {T} & q _ {k} q _ {k} ^ {T} \end{array} \right].
$$

This is of the required form, with $Q = [q_1, \ldots, q_n]$ the matrix from the MGS method applied to $A$ .

19.12. With $Q$ defined as in the hint,

$$
\begin{array}{l} \Delta A = Q R - A = \left(Q - P _ {2 1}\right) R + \Delta A _ {2} \\ = \left(V W ^ {T} - P _ {2 1}\right) R + \Delta A _ {2} \\ = V (I - S) W ^ {T} R + \Delta A _ {2} \\ = V (I + S) ^ {- 1} C ^ {2} W ^ {T} R + \Delta A _ {2} \\ = V (I + S) ^ {- 1} W ^ {T} \cdot W C U ^ {T} \cdot U C W ^ {T} \cdot R + \Delta A _ {2} \\ = V (I + S) ^ {- 1} W ^ {T} \cdot P _ {1 1} ^ {T} P _ {1 1} R + \Delta A _ {2} \\ = V (I + S) ^ {- 1} W ^ {T} \cdot P _ {1 1} ^ {T} \Delta A _ {1} + \Delta A _ {2}, \\ \end{array}
$$

and the result follows.

19.13. To produce the Householder method's $P$ we have to explicitly form the product of the individual Householder transformations. As long as this is done in a stable way the computed $\widehat{P}$ is guaranteed to be nearly orthogonal. MGS's $\widehat{Q}$ is formed in an algebraically different way, and the rounding errors in its formation are different from those in the formation of $P$ ; in other words, $\widehat{Q}$ is not a submatrix of $\widehat{P}$ . Consequently, there is no reason to expect $\widehat{Q}$ to be nearly orthonormal. Further insight can be gained by a detailed look at the structure of the computed $\widehat{P}$ ; see Björck and Paige [131, 1992, §4].

19.14. It is straightforward to show that $A^T A - I = (A - U)^T (A + U)$ . Taking norms gives the lower bound. Since $A + U = U(H + I)$ we have, from the previous relation,

$$
\left(\boldsymbol {A} - \boldsymbol {U}\right) ^ {T} \boldsymbol {U} = \left(\boldsymbol {A} ^ {T} \boldsymbol {A} - \boldsymbol {I}\right) (\boldsymbol {H} + \boldsymbol {I}) ^ {- 1}.
$$

Hence

$$
\| A - U \| _ {2} = \left\| (A - U) ^ {T} U \right\| _ {2} \leq \left\| A ^ {T} A - I \right\| _ {2} \left\| (H + I) ^ {- 1} \right\| _ {2} \leq \frac {\left\| A ^ {T} A - I \right\| _ {2}}{1 + \sigma_ {\min } (A)},
$$

since the eigenvalues of $H$ are the singular values of $A$ . In fact, the result holds for any unitarily invariant norm (but the denominators must be left unchanged).

20.1. One approach is to let $x$ be a solution and $y$ an arbitrary vector, and consider $f(\alpha) = \| A(x + \alpha y) - b\| _2^2$ . By expanding this expression it can be seen that if the normal equations are not satisfied then $\alpha$ and $y$ can be chosen so that $f(\alpha) < f(0)$ . Alternatively, note that for $f(x) = (b - Ax)^T (b - Ax) = x^T A^T Ax - 2b^T Ax + b^T b$ we have $\nabla f(x) = 2(A^T Ax - A^T b)$ and $\nabla^2 f(x) = 2A^T A$ , so any solution of the normal equations is a local minimum of $f$ , and hence a global minimum since $f$ is quadratic. The normal equations can be written as $(b - Ax)^T A = 0$ , which shows that the residual $b - Ax$ is orthogonal to range $(A)$ .

20.2. $A = Q\bigl [ \begin{array}{c}R\\ 0 \end{array} \bigr ]$ . The computed upper triangular QR factor $\widehat{R}$ satisfies $A + \varDelta A = Q\bigl [\widehat{\mathbf{\Gamma}}_0\bigr ]$ with $\| \varDelta a_j\| _2\leq \tilde{\gamma}_{mn}\| a_j\| _2$ , by Theorem 19.4. By Lemma 19.3, the computed transformed right-hand side satisfies $\widehat{c} = Q^T (b + \varDelta b)$ , with $\| \varDelta b\| _2\leq \tilde{\gamma}_{mn}\| b\| _2$

By Theorem 8.5, the computed solution $\widehat{x}$ to the triangular system $\widehat{R} x = \widehat{c}$ satisfies

$$
(\widehat {R} + \Delta R) \widehat {x} = \widehat {c}, \quad | \Delta R | \leq \gamma_ {n} | \widehat {R} |.
$$

So $\widehat{x}$ exactly solves the LS problem

$$
\left[ \begin{array}{c} \widehat {R} + \varDelta R \\ 0 \end{array} \right] x \approx \left[ \begin{array}{c} \widehat {c c} \\ \widehat {d} \end{array} \right],
$$

which is equivalent to the LS problem, on premultiplying by $Q$ ,

$$
(A + \overline {{\Delta A}}) x := \left(A + \Delta A + Q \left[ \begin{array}{c} \Delta R \\ 0 \end{array} \right]\right) x \approx b + \Delta b.
$$

We have

$$
\begin{array}{l} \left\| \overline {{\Delta a _ {j}}} \right\| _ {2} \leq \left\| \Delta a _ {j} \right\| _ {2} + \gamma_ {n} \left\| \widehat {r} _ {j} \right\| _ {2} \\ = \| \Delta a _ {j} \| _ {2} + \gamma_ {n} \| a _ {j} + \Delta a _ {j} \| _ {2} \\ \leq \tilde {\gamma} _ {m n} \| a _ {j} \| _ {2}. \quad \square \\ \end{array}
$$

20.3. A straightforward verification.

20.4. Notice that

$$
\| A X - I _ {m} \| _ {F} ^ {2} = \| A [ x _ {1}, \dots , x _ {m} ] - [ e _ {1}, \dots , e _ {m} ] \| _ {F} ^ {2} = \sum_ {i = 1} ^ {m} \| A x _ {i} - e _ {i} \| _ {2} ^ {2},
$$

which is minimized if $\| Ax_i - e_i \|_2$ is minimized for $i = 1:m$ . Thus we have $m$ independent LS problems. The solution is $x_i = A^+ e_i$ , $i = 1:m$ , that is, $X = A^+ I_m = A^+$ . This is the unique solution only if $A$ has full rank, but it is always the unique minimum Frobenius norm solution.

20.5. By Theorem 19.13 there is an orthonormal matrix $[W_1, w_{n+1}] \in \mathbb{R}^{m \times (n+1)}$ such that

$$
\left[ \begin{array}{c c} A + \varDelta A & b + \varDelta b \end{array} \right] = \left[ \begin{array}{c c} W _ {1} & w _ {n + 1} \end{array} \right] \left[ \begin{array}{c c} \widehat {R} & \widehat {z} \\ 0 & \widehat {\rho} \end{array} \right],
$$

where $\| \Delta a_{j}\|_{2}\leq c_{m,n}u\| a_{j}\|_{2}$ and $\| \Delta b\| _2\leq c_{m,n}u\| b\| _2$ . The computed solution $\widehat{x}$ to $\widehat{R} x = \widehat{z}$ satisfies

$$
(\widehat {R} + \Delta R) \widehat {x} = \widehat {z}, \quad | \Delta R | \leq \gamma_ {n} | \widehat {R} |.
$$

Therefore $\widehat{x}$ exactly solves the LS problem

$$
\left[ \begin{array}{c} \widehat {R} + \Delta R \\ 0 \end{array} \right] x \approx \left[ \begin{array}{c} \widehat {z} \\ \widehat {\rho} \end{array} \right],
$$

which, on premultiplying by $[W_1, w_{n+1}]$ , is equivalent to the LS problem

$$
W _ {1} (\widehat {R} + \Delta \widehat {R}) x \approx W _ {1} \widehat {z} + w _ {n + 1} \widehat {\rho},
$$

or

$$
(A + \overline {{\Delta A}}) x := (A + \Delta A + W _ {1} \Delta R) x \approx b + \Delta b.
$$

We have

$$
\left\| \overline {{\Delta a _ {j}}} \right\| _ {2} \leq \left\| \Delta a _ {j} \right\| _ {2} + \gamma_ {n} \left\| \hat {r} _ {j} \right\| _ {2} \leq c _ {m, n} u \left\| a _ {j} \right\| _ {2}.
$$

20.6. Subtracting $\widehat{r}^T\widehat{r} = b^T\widehat{r} -\widehat{x}^TA^T\widehat{r}$ from $r^T r = r^T b$ , we have

$$
\begin{array}{l} r ^ {T} r - \widehat {r} ^ {T} \widehat {r} = b ^ {T} (r - \widehat {r}) + \widehat {x} ^ {T} A ^ {T} \widehat {r} \\ = b ^ {T} A (\widehat {x} - x) + \widehat {x} ^ {T} \left(A ^ {T} b - A ^ {T} A \widehat {x}\right) \\ = x ^ {T} A ^ {T} A (\widehat {x} - x) + \widehat {x} ^ {T} \left(A ^ {T} b - A ^ {T} A \widehat {x}\right) \\ = (x - \widehat {x}) ^ {T} \left(A ^ {T} A \widehat {x} - A ^ {T} b\right) \\ = (x - \hat {x}) ^ {T} (\Delta c - \Delta A \hat {x}) \quad \text {b y} (2 0. 1 2). \\ \end{array}
$$

Taking norms gives the result.

20.7. By constructing a block LU factorization it is straightforward to show that

$$
\det  (C (\alpha) - \lambda I) = (\alpha - \lambda) ^ {m - n} \det  (A ^ {T} A + \lambda (\alpha - \lambda) I).
$$

Hence the eigenvalues of $C(\alpha)$ are $\lambda = \alpha$ ( $m - n$ times) together with the solutions of $\lambda (\alpha - \lambda) = -\sigma_i^2$ , namely, $\lambda = \alpha / 2 \pm (\alpha^2 / 4 + \sigma_i^2)^{1/2}$ , $i = 1:n$ .

Now

$$
\sigma_ {\mathrm {m i n}} (C (\alpha)) = \min \Bigl \{\alpha , \left(\frac {\alpha^ {2}}{4} + \sigma_ {n} ^ {2}\right) ^ {1 / 2} - \frac {\alpha}{2} \Bigr \},
$$

so the minimum condition number must occur when $\alpha = (\alpha^2 /4 + \sigma_n^2)^{1 / 2} - \alpha /2$ . This gives $\alpha = \sigma_{n} / \sqrt{2}$ , for which

$$
\kappa_ {2} (C (\alpha)) = \frac {1}{2} + \left(\frac {1}{4} + 2 \kappa_ {2} (A) ^ {2}\right) ^ {1 / 2}.
$$

The lower bound for the maximum is achieved for $\alpha = \sigma_1 / \sqrt{2}$ .

20.8. Let $y = 0$ and $\| (A + \Delta A)y - b\| _2 = \min$ . If $b = 0$ then we can take $\varDelta A=0$ . Otherwise, the normal equations tell us that $(A + \varDelta A)^T b = 0$ , so $\| \varDelta A\| _2\geq \| A^T b\| _2 / \| b\| _2$ . This lower bound is achieved, and the normal equations satisfied, for $\varDelta A^{T}=-\left(A^{T}b\right)b^{T}/b^{T}b$ . Hence, for $\theta = \infty$ ,

$$
\eta_ {F} (0) = \left\{ \begin{array}{l l} \| A ^ {T} b \| _ {2} / \| b \| _ {2}, & b \neq 0, \\ 0, & b = 0. \end{array} \right.
$$

20.9. For the case $\lambda_{*} < 0$ we have

$$
\begin{array}{l} \eta_ {F} (y) = \lambda_ {\min } \left(A A ^ {T} - \mu \frac {r r ^ {T}}{\| y \| _ {2} ^ {2}} + \mu \frac {\| r \| _ {2} ^ {2}}{\| y \| _ {2} ^ {2}} I\right) ^ {1 / 2} \\ = \lambda_ {\min } \left(A A ^ {T} + \mu \frac {\| r \| _ {2} ^ {2}}{\| y \| _ {2} ^ {2}} \left(I - \frac {r r ^ {T}}{\| r \| _ {2} ^ {2}}\right)\right) ^ {1 / 2} \\ = \lambda_ {\min } \left(A A ^ {T} + \mu \frac {\| r \| _ {2} ^ {2}}{\| y \| _ {2} ^ {2}} \left(I - \frac {r r ^ {T}}{\| r \| _ {2} ^ {2}}\right) ^ {2}\right) ^ {1 / 2} \\ = \sigma_ {\min } \left(\left[ A \sqrt {\mu} \frac {\| r \| _ {2}}{\| y \| _ {2}} \left(I - \frac {r r ^ {T}}{\| r \| _ {2} ^ {2}}\right) \right]\right). \\ \end{array}
$$

20.10. This is a standard result that can be derived by considering the first- and second-order optimality conditions in the theory of constrained optimization.

20.11. Setting $B = 0$ and $d = 0$ and using $\| b\| _2\leq \| r\| _2 + \| A\| _F\| x\| _2$ we obtain

$$
\frac {\| \varDelta x \| _ {2}}{\| x \| _ {2}} \leq \epsilon \widetilde {\kappa} (A) \Big (2 + (\widetilde {\kappa} (A) + 1) \frac {\| r \| _ {2}}{\| A \| _ {F} \| x \| _ {2}} \Big) + O (\epsilon^ {2}),
$$

where $\widetilde{\kappa}(A) = \| A \|_F \| A^+ \|_2$ , which is a first-order approximation of (20.1).

21.1. Setting the gradient of (21.13) to zero gives $A^T A x - A^T b + c = 0$ , which can be written as $y = b - A x$ , $A^T y = c$ , which is (21.12). The Lagrangian for (21.14) is $L(y, x) = \frac{1}{2} (y - b)^T (y - b) + x^T (A^T y - c)$ . We have $\nabla_y L(y, x) = y - b + A x$ and $\nabla_x L(y, x) = A^T y - c$ . Setting the gradients to zero gives the system (21.12).

22.1. The modified version has the same flop count as the original version.

22.4. The summation gives

$$
\sum_ {j = 0} ^ {n} x ^ {j} \sum_ {i = 0} ^ {n} w _ {i j} = \sum_ {i = 0} ^ {n} l _ {i} (x) \equiv 1,
$$

which implies the desired equality. It follows that all columns of $V^{-1}$ except the first must have both positive and negative entries. In particular, $V^{-1} \geq 0$ is not possible. The elements of $V^{-1}$ sum to 1, independently of the points $\alpha_{i}$ (see also Problem 14.7).

22.5. We have $U(i,:)T(\alpha_0,\ldots ,\alpha_n) = W(i,:)V(\alpha_0,\ldots ,\alpha_n)$ . But $T = LV$ , where $L$ has the form illustrated for $n = 5$ by

$$
L = \left[ \begin{array}{c c c c c} 1 & & & & \\ 0 & 1 & & & \\ - 1 & 0 & 2 & & \\ 0 & - 3 & 0 & 4 & \\ 1 & 0 & - 8 & 0 & 8 \end{array} \right]
$$

and $Le = e$ , so $U(i,:)L = W(i,:)$ , or $U(i,:)^T = L^{-T}W(i,:)^T$ . But $L^{-T} \geq 0$ by the given $x^n$ formula, so $\|L^{-T}\|_1 = \|L^{-1}\|_\infty = \|L^{-1}e\|_\infty = \|e\|_\infty = 1$ , hence $\|U(i,:)\|_1 \leq \|W(i,:)\|_1$ .

As an aside, we can evaluate $\| L\|_{\infty}$ as

$$
\| L \| _ {\infty} = | T _ {n} (\sqrt {- 1}) | = \frac {1}{2} \left[ (1 + \sqrt {2}) ^ {n} + (1 - \sqrt {2}) ^ {n} \right],
$$

after a little trigonometric algebra.

22.7. Denote the matrix by $C$ . For the zeros of $T_{n+1}$ we have

$$
C C ^ {T} = (n + 1) \operatorname {d i a g} \left(1, \frac {1}{2}, \frac {1}{2}, \dots , \frac {1}{2}\right).
$$

It follows that $\| C\| _2^2 = \sqrt{n + 1}$ $\| C^{-1}\| _2^2 = 2 / \sqrt{n + 1}$ , giving the result.

Extrema of $T_{n}$ : we have

$$
C D C ^ {T} = \frac {n}{2} D ^ {- 1}, \qquad D = \operatorname {d i a g} \left(\frac {1}{2}, 1, 1, \dots , 1, \frac {1}{2}\right).
$$

Hence $B = CD^{1/2}$ satisfies $BB^T = \frac{n}{2} D^{-1}$ , and so $\kappa_2(B) = \kappa_2(D)^{1/2} = \sqrt{2}$ . Then $\kappa_2(C) \leq \kappa_2(D^{1/2})\kappa_2(B) = 2$ .

22.8. The first expression follows from the formula (15.10) for the inverse of an upper bidiagonal matrix. The expression shows that a small componentwise relative change in a bidiagonal matrix causes only a small componentwise relative change in the inverse. For the second part, we note that in Algorithm 22.2, for the monomials, we have $U_{k} + \Delta U_{k} = \mathrm{diag}(1 + \epsilon_{i})\widetilde{U}_{k}$ , $|\epsilon_i| \leq u$ , where $\widetilde{U}_k$ agrees with $U_{k}$ everywhere except in certain superdiagonal elements, where $(\widetilde{U}_k)_{i,i+1} = (U_k)_{i,i+1}(1 + \delta_{i,i+1})$ , $|\delta_{i,i+1}| \leq u$ . The result now follows by applying the first part (and noting that $U_{k}$ is of dimension $n + 1$ ).

22.9. The increasing ordering is never produced, since the algorithm must choose $\alpha_{1}$ to maximize $|\alpha_{1} - \alpha_{0}|$ .

22.11. The dual condition number is

$$
\frac {\| | V ^ {- T} | | V ^ {T} \operatorname {d i a g} (0 , 1 , 2 , \dots , n) a | \| _ {\infty}}{\| a \| _ {\infty}}.
$$

See Higham [581, 1987] for proofs.

23.1. Consider the case where $m \leq \min(n, p)$ , and suppose $n = jm$ and $p = km$ for some integers $j$ and $k$ . Then the multiplication of the two matrices can be split into $m \times m$ blocks:

$$
A B = \left[ \begin{array}{c c c c} A _ {1} & A _ {2} & \ldots & A _ {j} \end{array} \right] \left[ \begin{array}{c c c} B _ {1 1} & \ldots & B _ {1 k} \\ \vdots & & \vdots \\ B _ {j 1} & \ldots & B _ {j k} \end{array} \right],
$$

which involves a total of $jk$ multiplications of $m \times m$ matrices, each involving $O(m^{\alpha})$ operations. Thus the total number of operations is $O(jkm^{\alpha})$ , or $O(m^{\alpha - 2}np)$ , as required, and we can show similar results for the cases when $n$ and $p$ are the smallest dimensions.

23.2. $\frac{1}{2} n^3 + n^2$ multiplications and $\frac{3}{2} n^3 + 2n(n - 1)$ additions.

23.3. For large $n = 2^k$ , $S_n(8) / S_n(n) \approx 1.96 \times (7/8)^k$ and $S_n(1) / S_n(8) \approx 1.79$ . The ratio $S_n(8) / S_n(n)$ measures the best possible reduction in the amount of arithmetic by using Strassen's method in place of conventional multiplication. The ratio $S_n(1) / S_n(8)$ measures how much more arithmetic is used by recurring down to the scalar level instead of stopping once the optimal dimension $n_0$ is reached. Of course, the efficiency of a practical code for Strassen's method also depends on the various non-floating point operations.

23.5. Apart from the differences in stability, the key difference is that Winograd's formula relies on commutativity and so cannot be generalized to matrices.

23.7. Some brief comments are given by Douglas, Heroux, Slishman, and Smith [351, 1994].

23.9. The inverse is

$$
\left[ \begin{array}{c c c} I & - A & A B \\ 0 & I & - B \\ 0 & 0 & I \end{array} \right].
$$

Hence we can form $AB$ by inverting a matrix of thrice the dimension. This result is not of practical value, but it is useful for computational complexity analysis.

25.1. (a) We have

$$
\left\| x _ {k + 1} - a \right\| = \left\| G \left(x _ {k}\right) - a + e _ {k} \right\| \leq \beta \| x _ {k} - a \| + \alpha . \tag {A.15}
$$

If $\| x_{k} - a \| \leq \alpha / (1 - \beta)$ then

$$
\left\| x _ {k + 1} - a \right\| \leq \beta \frac {\alpha}{1 - \beta} + \alpha = \frac {\alpha}{1 - \beta}.
$$

If $\| x_{k} - a \| > \alpha / (1 - \beta)$ , so that $\beta \| x_{k} - a \| < \| x_{k} - a \| - \alpha$ , then, using (A.15),

$$
\left\| x _ {k + 1} - a \right\| <   \left(\left\| x _ {k} - a \right\| - \alpha\right) + \alpha = \left\| x _ {k} - a \right\|.
$$

(b) We break the proof into two cases. First, suppose that $\| x_{m} - a\| \leq \alpha /(1 - \beta)$ for some $m$ . By part (a), the same inequality holds for all $k\geq m$ and we are finished. Otherwise, $\| x_{k} - a\| >\alpha /(1 - \beta)$ for all $k$ . By part (a) the positive sequence $\| x_{k} - a\|$ is monotone decreasing and therefore it converges to a limit $l$ . Suppose that $l = \alpha /(1 - \beta) + \delta$ where $\delta >0$ . Since $\beta < 1$ , for some $k$ we must have

$$
\left\| x _ {k} - a \right\| <   \frac {\alpha}{1 - \beta} + \frac {\delta}{\beta}.
$$

By (A.15),

$$
\left\| x _ {k + 1} - a \right\| <   \frac {\beta \alpha}{1 - \beta} + \delta + \alpha = \frac {\alpha}{1 - \beta} + \delta = l,
$$

which is a contradiction. Hence $l = \alpha / (1 - \beta)$ , as required.

(c) The vectors $e_k$ can be regarded as representing the rounding errors on the $k$ th iteration. The bound in (b) tells us that provided the error vectors are bounded by $\alpha$ , we can expect to achieve a relative error no larger than $\alpha / (1 - \beta)$ . In other words, the result gives us an upper bound on the achievable accuracy. When this result is applied to stationary iteration, $\beta$ is a norm of the iteration matrix; to make $\beta$ less than 1 we may have to use a scaled norm of the form $\| A \| := \| XAX^{-1} \|$ .

26.2. With $n = 3$ and almost any starting data, the backward error can easily be made of order 1, showing that the method is unstable. However, the backward error is found to be roughly of order $\kappa_{\infty}(A)u$ , so the method may have a backward error bound proportional to $\kappa_{\infty}(A)$ (this is an open question).

27.1. (b) An optimizing compiler might convert the test xp1 > 1 to $x + 1 > 1$ and then to $x > 0$ . (For a way to stop this conversion in Fortran, see the solution to Problem 27.3.) Then the code would compute a number of order $2^{e_{\min}}$ instead of a number of order $2^{-t}$ .

27.3. The algorithm is based on the fact that the positive integers that can be exactly represented are $1, 2, \ldots, \beta^t$ and

$$
\beta^ {t} + \beta , \beta^ {t} + 2 \beta , \beta^ {t} + 3 \beta , \dots , \beta^ {t + 1}, \beta^ {t + 1} + \beta^ {2}, \dots .
$$

In the interval $[\beta^t, \beta^{t+1}]$ the floating point numbers are spaced $\beta$ apart. This interval must contain a power of 2, $a = 2^k$ . The first while loop finds such an $a$ (or, rather, the floating point representation of such an $a$ ) by testing successive powers $2^i$ to see if both $2^i$ and $2^i + 1$ are representable. The next while loop adds successive powers of 2 until the next floating point number is found; on subtracting $a$ the base $\beta$ is produced. Finally $t$ is determined as the smallest power of $\beta$ for which the distance to the next floating point number exceeds 1.

The routine can fail for at least two reasons. First, an optimizing compiler might simplify the test while $(\mathbf{a} + 1) - \mathbf{a} == 1$ to while $1 == 1$ , thus altering the meaning of the program. Second, in the same test the result $(\mathbf{a} + 1)$ might be held in an extra length register and the subtraction done in extra precision. The computation would then reflect this higher precision and not the intended one. We could try to overcome this problem by saving the result $\mathbf{a} + 1$ in a variable, but an optimizing compiler might undo this effort by dispensing with the variable and storing the result in a register. In Fortran, the compiler's unwanted efforts can be nullified by a test of the form while foo(a+1) - a == 1, where foo is a function that simply returns its argument. The problems caused by the use of extra length registers were discussed by Gentleman and Marovich [476, 1974]; see also Miller [853, 1984, §2.2].

27.4. (This description is based on Schreiber [1022, 1989].) The random number generator in matgen repeats after 16384 numbers [744, 1998, §3.2.1.2, Thm. B]. The dimension $n = 512$ divides the period of the generator $(16384 = 512 \times 32)$ , with the effect that the first 32 columns of the matrix are repeated 16 times $(512 = 32 \times 16)$ , so the matrix has this structure:

$$
\begin{array}{l} B = \text {r a n d} (5 1 2, 3 2); \\ A = [ B, B, B, B, B, B, B, B, B, B, B, B, B, B, B ] \\ \end{array}
$$

Now consider the first 32 steps of Gaussian elimination. We apply 32 transformations to $A$ that have the effect, in exact arithmetic, of making $B$ upper trapezoidal. In floating point arithmetic, they leave a residue of small numbers (about $u \approx 10^{-7}$ in size) in rows 33 onward. Because of the structure of the matrix, identical small numbers occur in each of the 15 blocks of $A$ to the right of the first. Thus, the remaining $(512 - 32) \times (512 - 32)$ submatrix has the same block structure as $A$ (but with 15 block columns). Hence this process repeats every 32 steps:

after 32 steps the elements drop to $\approx 10^{-7}$   
after 64 steps the elements drop to $\approx 10^{-14}$   
after 96 steps the elements drop to $\approx 10^{-21}$   
after 128 steps the elements drop to $\approx 10^{-28}$   
after 160 steps the elements drop to $\approx 10^{-35}$   
after 192 steps the elements would drop to $\approx 10^{-42}$

but that is less than the underflow threshold. The actual pivots do not exactly match the analysis, which is probably due to rank deficiency of one of the submatrices generated. Also, underflow occurs earlier than predicted, apparently because two small numbers (both $O(10^{-21})$ ) are multiplied in a saxpy operation.

27.5. Let $s_i$ and $t_i$ denote the values of $s$ and $t$ at the start of the $i$ th stage of the algorithm. Then

$$
\sum_ {k = 1} ^ {i - 1} x _ {k} ^ {2} = t _ {i} ^ {2} s _ {i}. \tag {A.16}
$$

If $|x_i| > t_i$ then the algorithm uses the relation

$$
\sum_ {k = 1} ^ {i} x _ {k} ^ {2} = t _ {i} ^ {2} s _ {i} + x _ {i} ^ {2} = x _ {i} ^ {2} \big ((t / x _ {i}) ^ {2} s _ {i} + 1 \big),
$$

so with $s_{i+1} = (t_i / x_i)^2 s_i + 1$ and $t_{i+1} = |x_i|$ , (A.16) continues to hold for the next value of $i$ . The same is true trivially in the case $|x_i| \leq t_i$ .

This is a one-pass algorithm using $n$ divisions that avoids overflow except, possibly, on the final stage in forming $t\sqrt{s}$ , which can overflow only if $\| x \|_2$ does.

27.7. (a) The matrix $A \coloneqq I + Y^2 = I - Y^T Y$ is symmetric positive semidefinite since $\| Y \|_2 \leq 1$ , hence it has a (unique) symmetric positive semidefinite square root $X$ satisfying $X^2 = A = I + Y^2$ . The square root $X$ is a polynomial in $A$ (see, for example, Higham [580, 1987]) and hence a polynomial in $Y$ ; therefore $X$ and $Y$ commute, which implies that $(X + Y)^T(X + Y) = (X - Y)(X + Y) = X^2 - Y^2 = I$ , as required.

27.8. $|x| / 3$ could underflow to zero, or become unnormalized, when $\sqrt{|x|} / \sqrt{3}$ does not.

# Appendix B

# Acquiring Software

Caveat receptor ...

Anything free comes with no guarantee!

— JACK DONGARRA and ERIC GROSSE, Netlib mail header

In this appendix we provide information on how to acquire software mentioned in the book. First, we describe some basic aspects of the Internet.

# B.1. Internet

A huge variety of information and software is available over the Internet, the worldwide combination of interconnected computer networks. The location of a particular object is specified by a URL, which stands for "Uniform Resource Locator". Examples of URLs are

http://www.netlib.org/index.html

ftp://ftp.netlib.org

The first example specifies a World Wide Web server (http = hypertext transfer protocol) together with a file in hypertext format (html = hypertext markup language), while the second specifies an anonymous ftp site. In any URL, the site address may, optionally, be followed by a filename that specifies a particular file. For more details about the Internet see on-line information, or one of the many books on the subject.

# B.2. Netlib

Netlib is a repository of freely available mathematical software, documents, and databases of interest to the scientific computing community [350, 1987], [168, 1994]. It includes

research codes,   
- golden oldies (classic programs that are not available in standard libraries),   
the collected algorithms of the ACM,   
- program libraries such as EISPACK, LINPACK, LAPACK, and MINPACK.   
- back issues of NA-Digest, a weekly digest for the numerical analysis community,   
- databases of conferences and performance data for a wide variety of machines.

Netlib also enables the user to download technical reports from certain institutions, to download software and errata for textbooks, and to search a "white pages" database.

Netlib can be accessed in several ways.

Over the World Wide Web: http://www.netlib.org   
- By anonymous ftp: ftp://ftp.netlib.org

- By electronic mail. For an introduction and master index, send a one-line email message as follows:

mail netlib@netlib.org  
send index

Netlib is mirrored at various sites throughout the world.

# B.3. MATLAB

MATLAB is a commercial program sold by The MathWorks, Inc. It runs on a variety of platforms. The MathWorks maintains a collection of user-contributed M-files, which is accessible over the Internet.

For information contact

The MathWorks, Inc.

3 Apple Hill Drive

Natick, MA 01760-2098

USA

Tel: +508-647-7000

Fax: +508-647-7001

Web: www.mathworks.com

Newsgroup: comp.soft.sys.matlab

FTP: ftp.mathworks.com

E-mail: info@mathworks.com

# B.4. NAG Library and NAGWare F95 Compiler

The Numerical Algorithms Group (NAG) produces a variety of software products. Relevant to this book are the f95 compiler and the NAG Library, a large numerical program library available in several programming languages.

For information contact

NAG Ltd.

Wilkinson House

Jordan Hill Road

Oxford, OX2 8DR

UK

Tel: +44 1865 511245

Fax: +44 1865 310139

email: sales@nag.co.uk

Web: http://www.nag.co.uk

NAG has subsidiaries and distributors, whose addresses can be obtained from the above sources.

# Appendix C Program Libraries

Since the programming is likely to be the main bottleneck in the use of an electronic computer we have given a good deal of thought to the preparation of standard routines of considerable generality for the more important processes involved in computation. By this means we hope to reduce the time taken to code up large-scale computing problems, by building them up, as it were, from prefabricated units.

— J. H. WILKINSON, The Automatic Computing Engine at the National Physical Laboratory (1948)

In spite of the self-contained nature of the linear algebra field, experience has shown that even here the preparation of a fully tested set of algorithms is a far greater task than had been anticipated.

— J. H. WILKINSON and C. REINSCH, Handbook for Automatic Computation: Linear Algebra (1971)

In this appendix we briefly describe some of the freely available program libraries that have been mentioned in this book. These packages are all available from netlib (see §B.2).

# C.1. Basic Linear Algebra Subprograms

The Basic Linear Algebra Subprograms (BLAS) are sets of Fortran primitives for matrix and vector operations. They cover all the common operations in linear algebra. There are three levels, corresponding to the types of object operated upon. In the examples below, $x$ and $y$ are vectors, $A, B, C$ are rectangular matrices, and $T$ is a square triangular matrix. Names of BLAS routines are given in parentheses. The leading "x" denotes the Fortran data type, whose possible values are some or all of

```txt
S real   
D double precision   
C complex   
Z complex\*16, or double complex 
```

Level 1: [774, 1979] Vector operations. Inner product: $x^T y$ (xdot); $y \gets \alpha x + y$ (xAXPY); vector 2-norm $(y^T y)^{1/2}$ (xNRM2); swap vectors $x \leftrightarrow y$ (xSWAP); scale a vector $x \gets \alpha x$ (xSCAL); and other operations.

Level 2: [347, 1988], [348, 1988] Matrix-vector operations. Matrix times vector (gaxpy): $y \gets \alpha Ax + \beta y$ (xGEMV); rank-1 update: $A \gets A + \alpha xy^T$ (xGER); triangular solve: $x \gets T^{-1}x$ (xTRSV); and variations on these.

Level 3: [342, 1990], [343, 1990] Matrix-matrix operations. Matrix multiplication: $C \gets \alpha AB + \beta C$ (xGEMM); multiple right-hand side triangular solve: $A \gets \alpha T^{-1}A$ (xTRSM); rank- $r$ and rank- $2r$ updates of a symmetric matrix (xSYRK, xSYR2K); and variations on these.

The BLAS are intended to be called in innermost loops of linear algebra codes. Usually, most of the computation in a code that uses BLAS calls is done inside these calls. LINPACK [341, 1979] uses the level-1 BLAS throughout (model Fortran implementations of the level-1 BLAS are listed in [341, 1979, App. D]). LAPACK [20, 1999] exploits all three levels, using the highest possible level at all times.

Each set of BLAS comprises a set of subprogram specifications only. The specifications define the parameters to each routine and state what the routine must do, but not how it must do it. Thus the implementor has freedom over the precise implementation details (loop orderings, block algorithms, special code for special cases) and even the method (fast versus conventional matrix multiply), but the implementation is required to be numerically stable, and code that tests the numerical stability is provided with the model implementations [343, 1990], [348, 1988].

For more details on the BLAS and the advantages of using them, see the defining papers listed above, or, for example, [349, 1998] or [509, 1996, Chap. 1].

Automated techniques for producing BLAS tuned to particular machines have been developed in the ATLAS project [1218, 2001].

More recently, a BLAS Technical Forum Standard has been produced that extends the functionality of the original level-1, -2, and -3 BLAS, adding BLAS to handle sparse and banded matrices, further dense matrix computations (many based on LAPACK auxiliary routines), and extended and mixed precision computations [88, 2002], [137, 2001]. It provides bindings for Fortran 95, Fortran 77, and C. For more on the Extended and Mixed Precision BLAS see §27.10. The Web site of the BLAS Technical Forum is http://www.netlib.org/blas/blast-forum/

# C.2. EISPACK

EISPACK is a collection of Fortran 66 subroutines for computing eigenvalues and eigenvectors of matrices [1047, 1976], [455, 1977]. It contains 58 subroutines and 13 drivers. The subroutines are the basic building blocks for eigensystem computations; they perform such tasks as reduction to Hessenberg form, computation of some or all of the eigenvalues/vectors, and back transformations, for various types of matrix (real, complex, symmetric, banded, etc.). The driver subroutines provide easy access to many of EISPACK's capabilities; they call from one to five other EISPACK subroutines to do the computations.

EISPACK is primarily based on Algol 60 procedures developed in the 1960s by 19 different authors and published in the journal Numerische Mathematik. An edited collection of these papers was published in the Handbook for Automatic Computation [1246, 1971].

# C.3. LINPACK

LINPACK is a collection of Fortran 66 subroutines that analyse and solve linear equations and linear least squares problems [341, 1979]. The package solves linear systems whose matrices are general, banded, symmetric indefinite, symmetric positive definite, triangular, or tridiagonal. In addition, the package computes the QR and singular value decompositions and applies them to least squares problems. All the LINPACK routines use calls to the level-1 BLAS in the innermost loops; thus most of the floating point arithmetic in LINPACK is done within the level-1 BLAS.

# C.4. LAPACK

LAPACK [20, 1999] was released on February 29, 1992. As the announcement stated, "LAPACK is a transportable library of Fortran 77 subroutines for solving the most common problems in numerical linear algebra: systems of linear equations, linear least squares problems, eigenvalue problems, and singular value problems. It has been designed to be efficient on a wide range of modern high-performance computers."

LAPACK has been developed since 1987 by a worldwide team of numerical analysts. It can be regarded as a successor to LINPACK and EISPACK, as it

has virtually all their capabilities and much more besides. LAPACK improves on LINPACK and EISPACK in four main respects: speed, accuracy, robustness, and functionality. It was designed at the outset to exploit the level-3 BLAS.

Interfaces from LAPACK (or translations of LAPACK) to other languages are available for Fortran 95 [65, 2001], C, C++, and Java; see the links on the LAPACK home page at http://www.netlib.org/lapack/

A related project ScaLAPACK has produced a subset of LAPACK routines redesigned for distributed memory parallel machines [135, 1997].

Other work includes developing codes that take advantage of the careful rounding and exception handling of IEEE arithmetic [331, 1994]. For more details of all these topics see [20, 1999].

LAPACK undergoes regular updates, which are announced on the electronic newsletter NA-Digest. At the time of writing, the current release is version 3.0, last updated May 31, 2000, and the package contains over 1000 routines and over 735,000 lines of Fortran 77 code, including testing and timing code.

Mark 16 onward of the NAG Fortran 77 Library contains much of LAPACK in Chapters F07 and F08.

# C.4.1. Structure of LAPACK

The LAPACK routines can be divided into three classes.

The drivers solve a complete problem. The simple drivers have a minimal specification, while the expert drivers have additional capabilities of interest to the sophisticated user. The computational routines perform individual tasks such as computing a factorization or reducing a matrix to condensed form; they are called by the drivers. The auxiliary routines perform relatively low-level operations such as unblocked factorizations, estimating or computing matrix norms, and solving a triangular system with scaling to prevent overflow.

The driver and computational routines have names of the form xyyzzz. The first letter specifies the data type, which is one of S, D, C, and Z. The second two letters refer to the type of matrix. A partial list of types is as follows (there are 27 types in all):

BD bidiagonal   
GB general band   
GE general   
GT general tridiagonal   
HS upper Hessenberg   
OR (real) orthogonal   
PO symmetric or Hermitian positive definite   
PT symmetric or Hermitian positive definite tridiagonal   
SB (real) symmetric band   
ST (real) symmetric tridiagonal   
SY symmetric   
TR triangular (or quasi-triangular)

The last three characters specify the computation performed.

TRF factorize

TRS solve a (multiple right-hand side) linear system using the factorization

CON estimate $1 / \kappa_{1}(A)$ (or compute it exactly when $A$ is tridiagonal and symmetric positive definite or Hermitian positive definite)

RFS apply fixed precision iterative refinement and compute the componentwise relative backward error and a forward error bound

TRI use the factorization to compute $A^{-1}$

EQU compute factors to equilibrate the matrix

The auxiliary routines follow a similar naming convention, with most of them having $\mathbf{yy} = \mathbf{LA}$ .

# Appendix D The Matrix Computation Toolbox

The Matrix Computation Toolbox is a collection of MATLAB M-files containing functions for constructing test matrices, computing matrix factorizations, visualizing matrices, and carrying out direct search optimization. Various other miscellaneous functions are also included.

This toolbox supersedes the Test Matrix Toolbox [606, 1995] that was described in the first edition of this book. Most of the test matrices in that toolbox have been incorporated into MATLAB in the gallery function. The new toolbox incorporates some of the other routines in the Test Matrix Toolbox and adds several new ones.

Of particular relevance to this book are functions for

- Cholesky factorization with complete pivoting for a symmetric positive semidefinite matrix: cholp;   
- rounding matrix elements to a specified number of bits—useful for simulating lower precision in experiments: chop;   
- GE with one of four optional pivoting strategies: no pivoting, partial pivoting, rook pivoting, and complete pivoting: ges;   
- Gauss-Jordan elimination with no pivoting or partial pivoting for solving a linear system: gj;   
- generalized QR factorization: gqr;   
- the classical and modified Gram-Schmidt methods for QR factorization: gs_c, gs_m;   
- block $\mathbf{LDL}^{\mathrm{T}}$ factorization of symmetric matrices with partial pivoting or rook pivoting: ldlt_symm;   
- block $\mathbf{LDL}^{\mathrm{T}}$ factorization of symmetric tridiagonal matrices with Bunch's pivoting strategy: ldlt_sytr;   
- block $\mathbf{LDL}^{\mathrm{T}}$ factorization of skew-symmetric matrices with Bunch's partial pivoting strategy: ldlt_skew;   
- solving the equality constrained least squares problem: lse;   
- two- and three-dimensional views of pseudospectra: ps, pscont;

- direct search optimization by the alternating directions method, ad, the multidirectional search method, mds, and the Nelder-Mead simplex method, nms;   
- the $p$ -norm of a matrix: pnorm;   
- Strassen's method for matrix multiplication and Winograd's variant: strassen, strassenw;   
- converting between a triangular matrix and the nontrivial elements of its vec (useful in direct search optimization): treshape;   
- the vec-permutation matrix: vecperm.

The Matrix Computation Toolbox is available from

http://www.ma.man.ac.uk/~higham/mctoolbox

We summarize the contents of the toolbox in the following tables, which list the M-files by category, with short descriptions.

<table><tr><td colspan="2">Demonstration</td></tr><tr><td>mctdemo</td><td>Demonstration of Matrix Computation Toolbox.</td></tr></table>

<table><tr><td colspan="2">Test Matrices</td></tr><tr><td>augment</td><td>Augmented system matrix.</td></tr><tr><td>gfpp</td><td>Matrix giving maximal growth factor for Gaussian elimination with partial pivoting.</td></tr><tr><td>makejcf</td><td>A matrix with specified Jordan canonical form.</td></tr><tr><td>rschur</td><td>An upper quasi-triangular matrix.</td></tr><tr><td>vand</td><td>Vandermonde matrix.</td></tr><tr><td>vecperm</td><td>Vec-permutation matrix.</td></tr></table>

<table><tr><td colspan="2">Factorizations and Decompositions</td></tr><tr><td>cholp</td><td>Cholesky factorization with complete pivoting of a positive semidefinite matrix.</td></tr><tr><td>cod</td><td>Complete orthogonal decomposition.</td></tr><tr><td>gep</td><td>Gaussian elimination with pivoting: none, complete, partial, or rook.</td></tr><tr><td>gj</td><td>Gauss-Jordan elimination with no pivoting or partial pivoting to solve Ax = b.</td></tr><tr><td>gqr</td><td>Generalized QR factorization.</td></tr><tr><td>gs_c</td><td>Classical Gram-Schmidt QR factorization.</td></tr><tr><td>gs_m</td><td>Modified Gram-Schmidt QR factorization.</td></tr><tr><td>ldlt_skew</td><td>Block LDLT factorization for a skew-symmetric matrix.</td></tr><tr><td>ldlt_symm</td><td>Block LDLT factorization with partial pivoting or rook pivoting for a symmetric indefinite matrix.</td></tr><tr><td>ldlt_sytr</td><td>Block LDLT factorization for a symmetric tridiagonal matrix.</td></tr><tr><td>matsignt</td><td>Matrix sign function of a triangular matrix.</td></tr><tr><td>poldec</td><td>Polar decomposition.</td></tr><tr><td>signm</td><td>Matrix sign decomposition.</td></tr><tr><td>trap2tri</td><td>Unitary reduction of trapezoidal matrix to triangular form.</td></tr><tr><td colspan="2">Visualization</td></tr><tr><td>fv</td><td>Field of values (or numerical range).</td></tr><tr><td>gersh</td><td>Gershgorin disks.</td></tr><tr><td>ps</td><td>Dot plot of a pseudospectrum.</td></tr><tr><td>pscont</td><td>Contours and colour pictures of pseudospectra.</td></tr><tr><td>see</td><td>Pictures of a matrix.</td></tr></table>

<table><tr><td colspan="2">Direct Search Optimization</td></tr><tr><td>adsmax</td><td>Alternating directions method.</td></tr><tr><td>mdsmax</td><td>Multidirectional search method.</td></tr><tr><td>mmsmax</td><td>Nelder-Mead simplex method.</td></tr></table>

<table><tr><td colspan="2">Miscellaneous</td></tr><tr><td>chop</td><td>Round matrix elements.</td></tr><tr><td>cpltaxes</td><td>Determine suitable axis for plot of complex vector.</td></tr><tr><td>dual</td><td>Dual vector with respect to Hölder p-norm.</td></tr><tr><td>lse</td><td>Solve the equality constrained least squares problem.</td></tr><tr><td>matrix</td><td>Matrix Computation Toolbox information and matrix access by number.</td></tr><tr><td>pnorm</td><td>Estimate of matrix p-norm (1 ≤ p ≤ ∞).</td></tr><tr><td>rootm</td><td>Pth root of a matrix.</td></tr><tr><td>seqcheb</td><td>Sequence of points related to Chebyshev polynomials.</td></tr><tr><td>seqm</td><td>Multiplicative sequence.</td></tr><tr><td>show</td><td>Display signs of matrix elements.</td></tr><tr><td>skewpart</td><td>Skew-symmetric (skew-Hermitian) part.</td></tr><tr><td>sparsify</td><td>Randomly set matrix elements to zero.</td></tr><tr><td>strassen</td><td>Strassen&#x27;s fast matrix multiplication algorithm.</td></tr><tr><td>strassenw</td><td>Strassen&#x27;s fast matrix multiplication algorithm (Winograd variant).</td></tr><tr><td>sub</td><td>Principal submatrix.</td></tr><tr><td>symmpart</td><td>Symmetric (Hermitian) part.</td></tr><tr><td>treshape</td><td>Reshape vector to or from (unit) triangular matrix.</td></tr></table>

# Bibliography

![](images/a9ec24350db409ae6237ae2b75db18e5f74cdf5b271c7f941835118b1cdda8ff.jpg)

- The distribution of the year of publication of the references in this bibliography is shown in the graph above.   
- Many of the unpublished references are available on the Web and can be found by using Google (www.google.com) to search on author and title. For the more difficult-to-obtain unpublished references a URL is given when known.   
- Many of the author's papers are available from http://www.ma.man.ac.uk/~higham/   
- Many of Kahan's manuscripts are available from http://http.cs.berkeley.edu/~wkahan.   
- NA Digest is a weekly electronic mail magazine available at http://www.netlib.org/na-digest-htm1

[1] Jan Ole Aasen. On the reduction of a symmetric matrix to tridiagonal form. BIT, 11:233-242, 1971.   
[2] Nabih N. Abdelmalek. Round off error analysis for Gram-Schmidt method and solution of linear least squares problems. BIT, 11:345-368, 1971.   
[3] ACM Turing Award Lectures: The First Twenty Years, 1966-1985. Addison-Wesley, Reading, MA, USA, 1987. xviii+483 pp. ISBN 0-201-54885-2.   
[4] Forman S. Acton. Numerical Methods That Work. Harper and Row, New York, 1970. xviii+541 pp. Reprinted by Mathematical Association of America, Washington, D.C., with new preface and additional problems, 1990. ISBN 0-88385-450-3.   
[5] Forman S. Acton. Real Computing Made Real: Preventing Errors in Scientific and Engineering Calculations. Princeton University Press, Princeton, NJ, USA, 1996. xv+259 pp. ISBN 0-691-03663-2.   
[6] Duane A. Adams. A stopping criterion for polynomial root finding. Comm. ACM, 10:655-658, 1967.   
[7] Vijay B. Aggarwal and James W. Burgmeier. A round-off error model with applications to arithmetic expressions. SIAM J. Comput., 8(1):60-72, 1979.   
[8] Alan A. Ahac, John J. Buoni, and D. D. Olesky. Stable LU factorization of $H$ -matrices. Linear Algebra Appl., 99:97-110, 1988.   
[9] J. H. Ahlberg and E. N. Nilson. Convergence properties of the spline fit. J. Soc. Indust. Appl. Math., 11(1):95-104, 1963.   
[10] Paul Halmos by parts (interviews by Donald J. Albers). In *Paul Halmos: Celebrating 50 Years of Mathematics*, John H. Ewing and F. W. Gehring, editors, Springer-Verlag, Berlin, 1991, pages 3-32.   
[11] Gölz Alefeld and Jürgen Herzberger. Introduction to Interval Computations. Academic Press, New York, 1983. xviii+333 pp. ISBN 0-12-049820-0.   
[12] M. Almacany, C. B. Dunham, and J. Williams. Discrete Chebyshev approximation by interpolating rationals. IMA J. Numer. Anal., 4:467-477, 1984.   
[13] P. Alonso, M. Gasca, and J. M. Peña. Backward error analysis of Neville elimination. Appl. Numer. Math., 23:193-204, 1997.   
[14] B. Alpert, G. Beylkin, R. Coifman, and V. Rokhlin. Wavelet-like bases for the fast solution of second-kind integral equations. SIAM J. Sci. Comput., 14(1):159-184, 1993.   
[15] H. Alt and J. van Leeuwen. The complexity of basic complex operations. Computing, 27:205-215, 1981.   
[16] Steven C. Althoen and Renate Mclaughlin. Gauss-Jordan reduction: A brief history. Amer. Math. Monthly, 94(2):130-142, 1987.   
[17] Fernando L. Alvarado, Alex Pothen, and Robert S. Schreiber. Highly parallel sparse triangular solution. In Graph Theory and Sparse Matrix Computations, J. Alan George, John R. Gilbert, and Joseph W. H. Liu, editors, volume 56 of IMA Volumes in Mathematics and Its Applications, Springer-Verlag, New York, 1993, pages 141-158.   
[18] Pierluigi Amodio and Francesca Mazzia. Backward error analysis of cyclic reduction for the solution of tridiagonal systems. Math. Comp., 62(206):601-617, 1994.   
[19] Andrew A. Anda and Haesun Park. Fast plane rotations with dynamic scaling. SIAM J. Matrix Anal. Appl., 15(1):162-174, 1994.

[20] E. Anderson, Z. Bai, C. H. Bischof, S. Blackford, J. W. Demmel, J. J. Dongarra, J. J. Du Croz, A. Greenbaum, S. J. Hammarling, A. McKenney, and D. C. Sorensen. LAPACK Users' Guide. Third edition, Society for Industrial and Applied Mathematics, Philadelphia, PA, USA, 1999. xxvi+407 pp. ISBN 0-89871-447-8.   
[21] E. Anderson, Z. Bai, and J. Dongarra. Generalized QR factorization and its applications. Linear Algebra Appl., 162-164:243-271, 1992.   
[22] Edward Anderson. Robust triangular solves for use in condition estimation. Technical Report CS-91-142, Department of Computer Science, University of Tennessee, Knoxville, TN, USA, August 1991. 35 pp. LAPACK Working Note 36.   
[23] I. J. Anderson. A distillation algorithm for floating-point summation. SIAM J. Sci. Comput., 20(5):1797-1806, 1999.   
[24] T. W. Anderson. The Statistical Analysis of Time Series. Wiley, New York, 1971. xiv+704 pp. ISBN 0-471-02900-9.   
[25] T. W. Anderson, I. Olkin, and L. G. Underhill. Generation of random orthogonal matrices. SIAM J. Sci. Statist. Comput., 8(4):625-629, 1987.   
[26] T. Ando. Totally positive matrices. Linear Algebra Appl., 90:165-219, 1987.   
[27] Alan L. Andrew. Eigenvalues and singular values of certain random matrices. J. Comput. Appl. Math., 30:165-171, 1990.   
[28] Anonymous. Le Commandant Cholesky. Bulletin Géodésique, pages 159-161, 1922. Translation by Richard W. Cottle ("Major Cholesky") appears in [806, Appendix] and in NA Digest, Volume 90, Issue 7, 1990.   
[29] Anonymous. James Wilkinson (1919-1986). Annals of the History of Computing, 9(2):205-210, 1987. From the introduction: “A series of lightly edited extracts from messages that were sent over various computer networks during the period October 5, 1986–February 13, 1987”.   
[30] M. Arioli, J. W. Demmel, and I. S. Duff. Solving sparse linear systems with sparse backward error. SIAM J. Matrix Anal. Appl., 10(2):165-190, 1989.   
[31] M. Arioli, I. S. Duff, and P. P. M. de Rijk. On the augmented system approach to sparse least-squares problems. Numer. Math., 55:667-684, 1989.   
[32] M. Arioli and A. Laratta. Error analysis of an algorithm for solving an underdetermined linear system. Numer. Math., 46:255-268, 1985.   
[33] M. Arioli and A. Laratta. Error analysis of algorithms for computing the projection of a point onto a linear manifold. Linear Algebra Appl., 82:1-26, 1986.   
[34] Mario Arioli. A stopping criterion for the conjugate gradient algorithm in a finite element method framework. Technical Report 1179, Istituto di Analisi Numerica - C.N.R., Pavia, Italy, 2000. 12 pp.   
[35] Mario Arioli, Iain S. Duff, and Daniel Ruiz. Stopping criteria for iterative solvers. SIAM J. Matrix Anal. Appl., 13(1):138-144, 1992.   
[36] Mario Arioli and Francesco Romani. Stability, convergence, and conditioning of stationary iterative methods of the form $x^{(i+1)} = Px^{(i)} + q$ for the solution of linear systems. IMA J. Numer. Anal., 12:21-30, 1992.   
[37] William F. Arnold and Alan J. Laub. Generalized eigenproblem algorithms and software for algebraic Riccati equations. Proc. IEEE, 72(12):1746-1754, 1984.   
[38] Cleve Ashcraft, Roger G. Grimes, and John G. Lewis. Accurate symmetric indefinite linear equation solvers. SIAM J. Matrix Anal. Appl., 20(2):513-561, 1998.

[39] R. L. Ashenhurst and N. Metropolis. Error estimation in computer calculation. Amer. Math. Monthly, 72(2):47-58, 1965.   
[40] Edgar Asplund. Inverses of matrices $\{a_{ij}\}$ which satisfy $a_{ij} = 0$ for $j > i + p$ . Math. Scand., 7:57-60, 1959.   
[41] John V. Atanasoff. Computing machine for the solution of large systems of linear algebraic equations. Unpublished manuscript, Iowa State College, Ames, IA, USA, August 1940. Reprinted in [972, pp. 315-335].   
[42] Owe Axelsson. Iterative Solution Methods. Cambridge University Press, 1994. xiii+654 pp. ISBN 0-521-44524-8.   
[43] Ivo Babuska. Numerical stability in mathematical analysis. In Proc. IFIP Congress, Information Processing 68, North-Holland, Amsterdam, The Netherlands, 1969, pages 11-23.   
[44] Zhaojun Bai, David Day, James Demmel, and Jack Dongarra. A test matrix collection for non-Hermitian eigenvalue problems (release 1.0). Technical Report CS-97-355, Department of Computer Science, University of Tennessee, Knoxville, TN, USA, March 1997. 45 pp. LAPACK Working Note 123.   
[45] Zhaojun Bai and James W. Demmel. Computing the generalized singular value decomposition. SIAM J. Sci. Comput., 14(6):1464-1486, 1993.   
[46] Zhaojun Bai and James W. Demmel. On swapping diagonal blocks in real Schur form. Linear Algebra Appl., 186:73-95, 1993.   
[47] Zhaojun Bai, James W. Demmel, Jack J. Dongarra, Antoine Petitet, Howard Robinson, and K. Stanley. The spectral decomposition of nonsymmetric matrices on distributed memory parallel computers. SIAM J. Sci. Comput., 18(5):1446-1461, 1997.   
[48] Zhaojun Bai, James W. Demmel, and Ming Gu. Inverse free parallel spectral divide and conquer algorithms for nonsymmetric eigenproblems. Numer. Math., 76:279-308, 1997.   
[49] Zhaojun Bai, James W. Demmel, and Alan McKenney. On computing condition numbers for the nonsymmetric eigenproblem. ACM Trans. Math. Software, 19(2): 202-223, 1993.   
[50] D. H. Bailey and H. R. P. Ferguson. A Strassen-Newton algorithm for high-speed parallelizable matrix inversion. In Proceedings of Supercomputing '88, IEEE Computer Society Press, New York, 1988, pages 419-424.   
[51] David H. Bailey. The computation of $\pi$ to 29,360,000 decimal digits using Borweins' quartically convergent algorithm. Math. Comp., 50(181):283-296, 1988.   
[52] David H. Bailey. Extra high speed matrix multiplication on the Cray-2. SIAM J. Sci. Statist. Comput., 9(3):603-607, 1988.   
[53] David H. Bailey. Algorithm 719: Multiprecision translation and execution of FORTRAN programs. ACM Trans. Math. Software, 19(3):288-319, 1993.   
[54] David H. Bailey. A Fortran 90-based multiprecision system. ACM Trans. Math. Software, 21(4):379-387, 1995.   
[55] David H. Bailey, Robert Krasny, and Richard Pelz. Multiple precision, multiple processor vortex sheet roll-up computation. In Proceedings of the Sixth SIAM Conference on Parallel Processing for Scientific Computing, Volume I, Richard F. Sincovec, David E. Keyes, Michael R. Leuze, Linda R. Petzold, and Daniel A. Reed, editors, Society for Industrial and Applied Mathematics, Philadelphia, PA, USA, 1993, pages 52-56.

[56] David H. Bailey, King Lee, and Horst D. Simon. Using Strassen's algorithm to accelerate the solution of linear systems. J. Supercomputing, 4:357-371, 1991.   
[57] David H. Bailey, Horst D. Simon, John T. Barton, and Martin J. Fouts. Floating point arithmetic in future supercomputers. Internat. J. Supercomputer Appl., 3 (3):86-90, 1989.   
[58] J. K. Baksalary and R. Kala. The matrix equation $AX - YB = C$ . Linear Algebra Appl., 25:41-43, 1979.   
[59] J. K. Baksalary and R. Kala. The matrix equation $AXB + CYD = E$ . Linear Algebra Appl., 30:141-147, 1980.   
[60] Susanne M. Balle, Per Christian Hansen, and Nicholas J. Higham. A Strassen-type matrix inversion algorithm for the Connection Machine. Technical Report CNC/1993/028, Centre for Novel Computing, University of Manchester, Manchester, England, October 1993. 29 pp.   
[61] C. Ballester and V. Pereyra. On the construction of discrete approximations to linear differential expressions. Math. Comp., 21:297-302, 1967.   
[62] Randolph E. Bank and Donald J. Rose. Marching algorithms for elliptic boundary value problems. I: The constant coefficient case. SIAM J. Numer. Anal., 14(5): 792-829, 1977.   
[63] Yonathan Bard. Nonlinear Parameter Estimation. Academic Press, New York, 1974. x+341 pp. ISBN 0-12-078250-2.  
[64] V. Bargmann, D. Montgomery, and J. von Neumann. Solution of linear systems of high order. Report prepared for Navy Bureau of Ordnance, 1946. Reprinted in [1130, pp. 421-477].   
[65] V. A. Barker, L. S. Blackford, J. J. Dongarra, J. J. Du Croz, S. J. Hammarling, M. Marinova, J. Wasniewski, and P. Yalamov. LAPACK95 Users' Guide. Society for Industrial and Applied Mathematics, Philadelphia, PA, USA, 2001. xviii+258 pp. ISBN 0-89871-504-0.   
[66] J. L. Barlow, N. K. Nichols, and R. J. Plemmons. Iterative methods for equality-constrained least squares problems. SIAM J. Sci. Statist. Comput., 9(5):892-906, 1988.   
[67] Jesse L. Barlow. On the distribution of accumulated roundoff error in floating point arithmetic. In Proc. 5th IEEE Symposium on Computer Arithmetic, Ann Arbor, Michigan, 1981, pages 100-105.   
[68] Jesse L. Barlow. Probabilistic Error Analysis of Floating Point and CRD Arithmetics. PhD thesis, Northwestern University, Evanston, IL, USA, June 1981.   
[69] Jesse L. Barlow. A note on monitoring the stability of triangular decomposition of sparse matrices. SIAM J. Sci. Statist. Comput., 7(1):166-168, 1986.   
[70] Jesse L. Barlow. Error analysis and implementation aspects of deferred correction for equality constrained least squares problems. SIAM J. Numer. Anal., 25(6): 1340-1358, 1988.   
[71] Jesse L. Barlow. Error analysis of a pairwise summation algorithm to compute the sample variance. Numer. Math., 58:583-590, 1991.   
[72] Jesse L. Barlow and E. H. Bareiss. On roundoff error distributions in floating point and logarithmic arithmetic. Computing, 34:325-347, 1985.   
[73] Jesse L. Barlow and E. H. Bareiss. Probabilistic error analysis of Gaussian elimination in floating point and logarithmic arithmetic. Computing, 34:349-364, 1985.

[74] Jesse L. Barlow and Ilse C. F. Ipsen. Scaled Givens rotations for the solution of linear least squares problems on systolic arrays. SIAM J. Sci. Statist. Comput., 8 (5):716-733, 1987.   
[75] Jesse L. Barlow and Udaya B. Vemulapati. A note on deferred correction for equality constrained least squares problems. SIAM J. Numer. Anal., 29(1):249-256, 1992.   
[76] Jesse L. Barlow and Udaya B. Vemulapati. Rank detection methods for sparse matrices. SIAM J. Matrix Anal. Appl., 13(4):1279-1297, 1992.   
[77] Jesse L. Barlow and Hongyuan Zha. Growth in Gaussian elimination, orthogonal matrices, and the 2-norm. SIAM J. Matrix Anal. Appl., 19(3):807-815, 1998.   
[78] S. Barnett and C. Storey. Some applications of the Lyapunov matrix equation. J. Inst. Maths. Applics., 4:33-42, 1968.   
[79] Geoff Barrett. Formal methods applied to a floating-point number system. IEEE Trans. Software Engrg., 15(5):611-621, 1989.   
[80] Richard Barrett, Michael Berry, Tony F. Chan, James Demmel, June Donato, Jack Dongarra, Victor Eijkhout, Roldan Pozo, Charles Romine, and Henk van der Vorst. Templates for the Solution of Linear Systems: Building Blocks for Iterative Methods. Society for Industrial and Applied Mathematics, Philadelphia, PA, USA, 1994. xiii+112 pp. ISBN 0-89871-328-5.   
[81] Anders Barrlund. Perturbation bounds for the $LDL^{H}$ and $LU$ decompositions. BIT, 31:358-363, 1991.   
[82] Anders Barrlund. Perturbation bounds for the generalized $QR$ factorization. Linear Algebra Appl., 207:251-271, 1994.   
[83] D. W. Barron and H. P. F. Swinnerton-Dyer. Solution of simultaneous linear equations using a magnetic-tape store. Comput. J., 3(1):28-33, 1960.   
[84] R. H. Bartels and G. W. Stewart. Algorithm 432: Solution of the matrix equation $AX + XB = C$ . Comm. ACM, 15(9):820-826, 1972.   
[85] Sven G. Bartels. Two topics in matrix analysis: Structured sensitivity for Vandermonde-like systems and a subgradient method for matrix norm estimation. M.Sc. Thesis, Department of Mathematics and Computer Science, University of Dundee, Dundee, Scotland, September 1991.   
[86] Sven G. Bartels and Desmond J. Higham. The structured sensitivity of Vandermonde-like systems. Numer. Math., 62:17-33, 1992.   
[87] Victor Barwell and Alan George. A comparison of algorithms for solving symmetric indefinite systems of linear equations. ACM Trans. Math. Software, 2(3): 242-251, 1976.   
[88] Basic Linear Algebra Subprograms Technical (BLAST) Forum Standard. Int. J. High Performance Applications and Supercomputing, 2002. To appear.   
[89] F. L. Bauer. Optimal scaling of matrices and the importance of the minimal condition. In Proc. IFIP Congress 1962, Cicely M. Popplewell, editor, Information Processing 62, North-Holland, Amsterdam, The Netherlands, 1963, pages 198-201.   
[90] F. L. Bauer. Optimally scaled matrices. Numer. Math., 5:73-87, 1963.   
[91] F. L. Bauer. Genauigkeitsfragen bei der Lösung linearer Gleichungssysteme. Z. Angew. Math. Mech., 46(7):409-421, 1966.   
[92] F. L. Bauer. Remarks on optimally scaled matrices. Numer. Math., 13:1-3, 1969.

[93] F. L. Bauer. Computational graphs and rounding errors. SIAM J. Numer. Anal., 11(1):87-96, 1974.   
[94] F. L. Bauer and C. Reinsch. Inversion of positive definite matrices by the Gauss-Jordan method. In Linear Algebra, J. H. Wilkinson and C. Reinsch, editors, volume II of Handbook for Automatic Computation, Springer-Verlag, Berlin, 1971, pages 45-49. Contribution I/3.   
[95] F. L. Bauer, J. Stoer, and C. Witzgall. Absolute and monotonic norms. Numer. Math., 3:257-264, 1961.   
[96] Richard M. Beam and Robert F. Warming. The asymptotic spectra of banded Toeplitz and quasi-Toeplitz matrices. SIAM J. Sci. Comput., 14(4):971-1006, 1993.   
[97] Albert E. Beaton, Donald B. Rubin, and John L. Barone. The acceptability of regression solutions: Another look at computational accuracy. J. Amer. Statist. Assoc., 71(353):158-168, 1976.   
[98] Bernhard Beckermann. The condition number of real Vandermonde, Krylov and positive definite Hankel matrices. Numer. Math., 85:553-577, 2000.   
[99] C. Gordon Bell and Allen Newell. Computer Structures: Readings and Examples. McGraw-Hill, New York, 1971. xix+668 pp. ISBN 07-004357-4.   
[100] E. T. Bell. Review of “Contributions to the History of Determinants, 1900-1920”, by Sir Thomas Muir. Amer. Math. Monthly, 38:161-164, 1931. Reprinted in [397].   
[101] Richard Bellman. Introduction to Matrix Analysis. Second edition, McGraw-Hill, New York, 1970. xxiii+403 pp. Reprinted by Society for Industrial and Applied Mathematics, Philadelphia, PA, USA, 1997. ISBN 0-89871-399-4.   
[102] Frank Benford. The law of anomalous numbers. Proceedings of the American Philosophical Society, 78(4):551-572, 1938.   
[103] Commandant Benoit. Note sur une méthode de résolution des équations normales provenant de l'application de la méthode des moindres carrés à un système d'équations linéaires en nombre inférieur à celui des inconnues. Application de la méthode à la résolution d'un système défini d'équations linéaires (Procedé du Commandant Cholesky). Bulletin Géodésique (Toulouse), 2:67-77, 1924. Cited in [28, Cottle's translation].   
[104] N. F. Benschop and H. C. Ratz. A mean square estimate of the generated roundoff error in constant matrix iterative processes. J. Assoc. Comput. Mach., 18(1):48-62, 1971.   
[105] M. C. Berenbaum. Direct search methods in the optimisation of cancer chemotherapy. Br. J. Cancer, 61:101-109, 1991.   
[106] Abraham Berman and Robert J. Plemmons. Nonnegative Matrices in the Mathematical Sciences. Society for Industrial and Applied Mathematics, Philadelphia, PA, USA, 1994. xx+340 pp. Corrected republication, with supplement, of work first published in 1979 by Academic Press. ISBN 0-89871-321-8.   
[107] Rajendra Bhatia. Matrix Analysis. Springer-Verlag, New York, 1997. xi+347 pp. ISBN 0-387-94846-5.   
[108] Rajendra Bhatia and Kalyan Mukherjea. Variation of the unitary part of a matrix. SIAM J. Matrix Anal. Appl., 15(3):1007-1014, 1994.   
[109] Rajendra Bhatia and Peter Rosenthal. How and why to solve the operator equation $AX - XB = Y$ . Bull. London Math. Soc., 29:1-21, 1997.

[110] Dario Bini and Grazia Lotti. Stability of fast algorithms for matrix multiplication. Numer. Math., 36:63-72, 1980.   
[111] Dario Bini and Victor Y. Pan. *Polynomial and Matrix Computations*. Volume 1: Fundamental Algorithms. Birkhäuser, Boston, MA, USA, 1994. xvi+415 pp. ISBN 0-8176-3786-9.   
[112] Garrett Birkhoff. Two Hadamard numbers for matrices. Comm. ACM, 18(1): 25-29, 1975.   
[113] Garrett Birkhoff and Surender Gulati. Isotropic distributions of test matrices. J. Appl. Math. Phys. (ZAMP), 30:148-158, 1979.   
[114] Garrett Birkhoff and Saunders Mac Lane. A Survey of Modern Algebra. Fourth edition, Macmillan, New York, 1977. xi+500 pp. ISBN 0-02-310070-2.   
[115] Christian H. Bischof. Incremental condition estimation. SIAM J. Matrix Anal. Appl., 11(2):312-322, 1990.   
[116] Christian H. Bischof, John G. Lewis, and Daniel J. Pierce. Incremental condition estimation for sparse matrices. SIAM J. Matrix Anal. Appl., 11(4):644-659, 1990.   
[117] Christian H. Bischof and Charles F. Van Loan. The WY representation for products of Householder matrices. SIAM J. Sci. Statist. Comput., 8(1):s2-s13, 1987.   
[118] Åke Björck. Iterative refinement of linear least squares solutions I. BIT, 7:257-278, 1967.   
[119] Åke Björck. Solving linear least squares problems by Gram-Schmidt orthogonalization. BIT, 7:1-21, 1967.   
[120] Åke Björck. Iterative refinement of linear least squares solutions II. BIT, 8:8-30, 1968.   
[121] Åke Björck. Comment on the iterative refinement of least-squares solutions. J. Amer. Statist. Assoc., 73(361):161-166, 1978.   
[122] Åke Björck. Stability analysis of the method of seminormal equations for linear least squares problems. Linear Algebra Appl., 88/89:31-48, 1987.   
[123] Åke Björck. Iterative refinement and reliable computing. In Reliable Numerical Computation, M. G. Cox and S. J. Hammarling, editors, Oxford University Press, 1990, pages 249-266.   
[124] Åke Björck. Least squares methods. In Handbook of Numerical Analysis, P. G. Ciarlet and J. L. Lions, editors, volume I: Finite Difference Methods—Solution of Equations in $\mathbb{R}^n$ , Elsevier/North-Holland, Amsterdam, The Netherlands, 1990.   
[125] Åke Björck. Component-wise perturbation analysis and error bounds for linear least squares solutions. BIT, 31:238-244, 1991.   
[126] Åke Björck. Pivoting and stability in the augmented system method. In Numerical Analysis 1991, Proceedings of the 14th Dundee Conference, D. F. Griffiths and G. A. Watson, editors, volume 260 of Pitman Research Notes in Mathematics, Longman Scientific and Technical, Essex, UK, 1992, pages 1-16.   
[127] Åke Björck. Numerics of Gram-Schmidt orthogonalization. Linear Algebra Appl., 197/198:297-316, 1994.   
[128] Åke Björck. Numerical Methods for Least Squares Problems. Society for Industrial and Applied Mathematics, Philadelphia, PA, USA, 1996. xvii+408 pp. ISBN 0-89871-360-9.   
[129] Åke Björck and Tommy Elfving. Algorithms for confluent Vandermonde systems. Numer. Math., 21:130-137, 1973.

[130] Åke Björck and Gene H. Golub. Iterative refinement of linear least squares solutions by Householder transformation. BIT, 7:322-337, 1967.   
[131] Åke Björck and C. C. Paige. Loss and recapture of orthogonality in the modified Gram-Schmidt algorithm. SIAM J. Matrix Anal. Appl., 13(1):176-190, 1992.   
[132] Åke Björck and C. C. Paige. Solution of augmented linear systems using orthogonal factorizations. BIT, 34:1-24, 1994.   
[133] Åke Björck and Victor Pereyra. Solution of Vandermonde systems of equations. Math. Comp., 24(112):893-903, 1970.   
[134] P. Bjørstad, F. Manne, T. Sørevik, and M. Vajtersic. Efficient matrix multiplication on SIMD computers. SIAM J. Matrix Anal. Appl., 13(1):386-401, 1992.   
[135] L. S. Blackford, J. Choi, A. Cleary, E. D'Azevedo, J. Demmel, I. Dhillon, J. Dongarra, S. Hammarling, G. Henry, A. Petitet, K. Stanley, D. Walker, and R. C. Whaley. *ScaLAPACK Users' Guide*. Society for Industrial and Applied Mathematics, Philadelphia, PA, USA, 1997. xxvi+325 pp. ISBN 0-89871-397-8.   
[136] L. S. Blackford, A. Cleary, A. Petitet, R. C. Whaley, J. Demmel, I. Dhillon, H. Ren, K. Stanley, J. Dongarra, and S. Hammarling. Practical experience in the numerical dangers of heterogeneous computing. ACM Trans. Math. Software, 23 (2):133-147, 1997.   
[137] L. S. Blackford, J. Demmel, J. Dongarra, I. Duff, S. Hammarling, G. Henry, M. Heroux, L. Kaufman, A. Lumsdaine, A. Petitet, R. Pozo, K. Remington, and R. C. Whaley. An updated set of Basic Linear Algebra Subprograms (BLAS), February 2001. Submitted to ACM Trans. Math. Software. 20 pp.   
[138] G. Blanch. Numerical evaluation of continued fractions. SIAM Rev., 6(4):383-421, 1964.   
[139] J. H. Bleher, A. E. Roeder, and S. M. Rump. ACRITH: High-accuracy arithmetic. An advanced tool for numerical computation. In Proceedings of the 7th Symposium on Computer Arithmetic, Kai Hwang, editor, IEEE Computer Society Press, Silver Spring, MD, USA, 1985, pages 318-321.   
[140] J. H. Bleher, S. M. Rump, U. Kulisch, M. Metzger, Ch. Ullrich, and W. Walter. A study of a FORTRAN extension for engineering/scientific computation with access to ACRITH. Computing, 39:93-110, 1987.   
[141] B. Bliss, M.-C. Brunet, and E. Gallopoulos. Automatic program instrumentation with applications in performance and error analysis. In Expert Systems for Scientific Computing, E. N. Houstis, J. R. Rice, and R. Vichnevetsky, editors, North-Holland, Amsterdam, The Netherlands, 1992, pages 235-260.   
[142] Richard M. Bloch. Mark I calculator. In [552], pages 23-30.   
[143] James L. Blue. A portable Fortran program to find the Euclidean norm of a vector. ACM Trans. Math. Software, 4(1):15-23, 1978.   
[144] E. Bodewig. Review of “Rounding-Off Errors in Matrix Processes” by A. M. Turing. Math. Rev., 10:405, 1949.   
[145] Gerd Bohlender. Floating-point computation of functions with maximum accuracy. IEEE Trans. Comput., C-26(7):621-632, 1977.   
[146] Z. Bohte. Bounds for rounding errors in the Gaussian elimination for band systems. J. Inst. Maths. Applics., 16:133-142, 1975.

[147] Ronald F. Boisvert, Roldan Pozo, Karin Remington, Richard F. Barrett, and Jack J. Dongarra. Matrix Market: A Web resource for test matrix collections. In Quality of Numerical Software: Assessment and Enhancement, Ronald F. Boisvert, editor, Chapman and Hall, London, 1997, pages 125-136.   
[148] Daniel Boley, Gene H. Golub, Samy Makar, Nirmal Saxena, and Edward J. McCluskey. Floating point fault tolerance with backward error assertions. IEEE Trans. Comput., 44(2):302-311, 1994.   
[149] Jo A. M. Bollen. Numerical stability of descent methods for solving linear equations. Numer. Math., 43:361-377, 1984.   
[150] S. Bondeli and W. Gander. Cyclic reduction for special tridiagonal systems. SIAM J. Matrix Anal. Appl., 15(1):321-330, 1994.   
[151] T. Boros, T. Kailath, and V. Olshevsky. Fast algorithms for solving Vandermonde and Chebyshev-Vandermonde systems. Manuscript, 1994. 22 pp.   
[152] J. M. Borwein, P. B. Borwein, and D. H. Bailey. Ramanujan, modular equations, and approximations to Pi or how to compute one billion digits of Pi. Amer. Math. Monthly, 96(3):201-219, 1989.   
[153] B. V. Bowden. The organization of a typical machine. In *Faster than Thought: A Symposium on Digital Computing Machines*, B. V. Bowden, editor, Pitman, London, 1953, pages 67-77.   
[154] H. J. Bowdler, R. S. Martin, G. Peters, and J. H. Wilkinson. Solution of real and complex systems of linear equations. Numer. Math., 8:217-234, 1966. Also in [1246, pp. 93-110], Contribution I/7.   
[155] David W. Boyd. The power method for $\ell^p$ norms. Linear Algebra Appl., 9:95-101, 1974.   
[156] Carl B. Boyer. A History of Mathematics. Second edition, Wiley, New York, 1989. xviii+762 pp. Revised by Uta C. Merzbach. ISBN 0-471-50357-6.   
[157] Jeff Boyle. An application of Fourier series to the most significant digit problem. Amer. Math. Monthly, 101(11):879-886, 1994.   
[158] R. P. Brent. Algorithms for matrix multiplication. Technical Report CS 157, Department of Computer Science, Stanford University, Stanford, CA, USA, March 1970. ii+52 pp.   
[159] R. P. Brent. Error analysis of algorithms for matrix multiplication and triangular decomposition using Winograd's identity. Numer. Math., 16:145-156, 1970.   
[160] Richard P. Brent. On the precision attainable with various floating-point number systems. IEEE Trans. Comput., C-22(6):601-607, 1973.   
[161] Richard P. Brent. A Fortran multiple-precision arithmetic package. ACM Trans. Math. Software, 4(1):57-70, 1978.   
[162] Richard P. Brent. ALGORITHM 524 MP, a Fortran multiple-precision arithmetic package. ACM Trans. Math. Software, 4(1):71-81, 1978.   
[163] Richard P. Brent, Judith A. Hooper, and J. Michael Yohe. An AUGMENT interface for Brent's multiple precision arithmetic package. ACM Trans. Math. Software, 6(2):146-149, 1980.   
[164] Claude Brezinski. André Louis Cholesky. In A Numerical Analysis Conference in Honour of Jean Meinguet, 1996, pages 45-50. Published as a supplement to the Bulletin of the Belgian Mathematical Society. Also available as Publication ANO-347, Laboratoire d'Analyse Numérique et d'Optimisation, Université des Sciences et Technologies de Lille, Nov. 1995, http://ano.univ-lille1.fr.

[165] William L. Briggs and Van Emden Henson. The DFT: An Owner's Manual for the Discrete Fourier Transform. Society for Industrial and Applied Mathematics, Philadelphia, PA, USA, 1995. xv+434 pp. ISBN 0-89871-342-0.   
[166] J. L. Britton, editor. Collected Works of A. M. Turing: Pure Mathematics. North-Holland, Amsterdam, The Netherlands, 1992. xxii+287 pp. ISBN 0-444-88059-3.   
[167] W. S. Brown. A simple but realistic model of floating-point arithmetic. ACM Trans. Math. Software, 7(4):445-480, 1981.   
[168] Shirley V. Browne, Jack J. Dongarra, Stan C. Green, Keith Moore, Thomas H. Rowan, and Reed C. Wade. Netlib services and resources. Report ORNL/TM-12680, Oak Ridge National Laboratory, Oak Ridge, TN, USA, April 1994. 42 pp.   
[169] Marie-Christine Brunet. Contribution à la Fiabilité de Logiciels Numériques et à L'analyse de Leur Comportement: Une Approche Statistique. PhD thesis, Université de Paris IX Dauphine, U.E.R. Mathématiques de la Décision, January 1989. viii+214 pp.   
[170] Marie-Christine Brunet and Françoise Chatelin. CESTAC, a tool for a stochastic round-off error analysis in scientific computing. In Numerical Mathematics and Applications, R. Vichnevetsky and J. Vignes, editors, Elsevier Science Publishers B.V. (North-Holland), Amsterdam, The Netherlands, 1986, pages 11-20.   
[171] James L. Buchanan and Peter R. Turner. Numerical Methods and Analysis. McGraw-Hill, New York, 1992. xv+751 pp. ISBN 0-07-008717-2, 0-07-112922-7 (international paperback edition).   
[172] W. Buchholz. Fingers or fists? (The choice of decimal or binary representation). Comm. ACM, 2(12):3-11, 1959.   
[173] W. Buchholz. Origin of the word byte. Annals of the History of Computing, 3(1): 72, 1981.   
[174] B. Bukhberger and G. A. Emel'yanenko. Methods of inverting tridiagonal matrices. U.S.S.R. Computational Math. and Math. Phys., 13:10-20, 1973.   
[175] James R. Bunch. Analysis of the diagonal pivoting method. SIAM J. Numer. Anal., 8(4):656-680, 1971.   
[176] James R. Bunch. Equilibration of symmetric matrices in the max-norm. J. Assoc. Comput. Mach., 18(4):566-572, 1971.   
[177] James R. Bunch. Partial pivoting strategies for symmetric matrices. SIAM J. Numer. Anal., 11(3):521-528, 1974.   
[178] James R. Bunch. A note on the stable decomposition of skew-symmetric matrices. Math. Comp., 38(158):475-479, 1982.   
[179] James R. Bunch. The weak and strong stability of algorithms in numerical linear algebra. Linear Algebra Appl., 88/89:49-66, 1987.   
[180] James R. Bunch, James W. Demmel, and Charles F. Van Loan. The strong stability of algorithms for solving symmetric linear systems. SIAM J. Matrix Anal. Appl., 10(4):494-499, 1989.   
[181] James R. Bunch and Linda Kaufman. Some stable methods for calculating inertia and solving symmetric linear systems. Math. Comp., 31(137):163-179, 1977.   
[182] James R. Bunch, Linda Kaufman, and Beresford N. Parlett. Decomposition of a symmetric matrix. Numer. Math., 27:95-109, 1976.

[183] James R. Bunch and Beresford N. Parlett. Direct methods for solving symmetric indefinite systems of linear equations. SIAM J. Numer. Anal., 8(4):639-655, 1971.   
[184] Oleg Burdakov. A greedy algorithm for the optimal basis problem. BIT, 37(3): 591-599, 1997.   
[185] Peter Bürgisser, Michael Clausen, and M. Amin Shokrollahi. Algebraic Complexity Theory. Springer-Verlag, Berlin, 1997. xxiii+618 pp. ISBN 0-540-60582-7.   
[186] P. Businger and G. H. Golub. Linear least squares solutions by Householder transformations. Numer. Math., 7:269-276, 1965. Also in [1246, pp. 111-118], Contribution I/8.   
[187] P. A. Businger. Matrices which can be optimally scaled. Numer. Math., 12: 346-348, 1968.   
[188] P. A. Businger. Monitoring the numerical stability of Gaussian elimination. Numer. Math., 16:360-361, 1971.   
[189] J. C. Butcher. The Numerical Analysis of Ordinary Differential Equations: Runge-Kutta and General Linear Methods. Wiley, Chichester, UK, 1987. xv+512 pp. ISBN 0-471-91046-5.   
[190] B. L. Buzbee, G. H. Golub, and C. W. Nielson. On direct methods for solving Poisson's equations. SIAM J. Numer. Anal., 7(4):627-656, 1970.   
[191] Ralph Byers. A LINPACK-style condition estimator for the equation $AX - XB^T = C$ . IEEE Trans. Automat. Control, AC-29(10):926-928, 1984.   
[192] Ralph Byers. Numerical condition of the algebraic Riccati equation. In Linear Algebra and Its Role in Systems Theory, B. N. Datta, editor, volume 47 of Contemporary Math., American Mathematical Society, Providence, RI, USA, 1985, pages 35-49.   
[193] Ralph Byers. Solving the algebraic Riccati equation with the matrix sign function. Linear Algebra Appl., 85:267-279, 1987.   
[194] Ralph Byers. A bisection method for measuring the distance of a stable matrix to the unstable matrices. SIAM J. Sci. Statist. Comput., 9(5):875-881, 1988.   
[195] Ralph Byers and Stephen Nash. On the singular “vectors” of the Lyapunov operator. SIAM J. Alg. Discrete Methods, 8(1):59-66, 1987.   
[196] John Caffney. Another test matrix for determinants and inverses. Comm. ACM, 6(6):310, 1963.   
[197] D. Calvetti and L. Reichel. A Chebychev-Vandermonde solver. Linear Algebra Appl., 172:219-229, 1992.   
[198] D. Calvetti and L. Reichel. Fast inversion of Vandermonde-like matrices involving orthogonal polynomials. BIT, 33:473-484, 1993.   
[199] S. L. Campbell and C. D. Meyer, Jr. Generalized Inverses of Linear Transformations. Pitman, London, 1979. xi+272 pp. Reprinted by Dover, New York, 1991. ISBN 0-486-66693-X.   
[200] Martin Campbell-Kelly. Programming the Pilot ACE: Early programming activity at the National Physical Laboratory. Annals of the History of Computing, 3(2): 133-162, 1981.   
[201] Martin Campbell-Kelly. Review of “Alan Turing: The Enigma”, by Andrew Hodges. Annals of the History of Computing, 6(2):176-178, 1984.   
[202] Wei-Lu Cao and William J. Stewart. A note on inverses of Hessenberg-like matrices. Linear Algebra Appl., 76:233-240, 1986.

[203] Ole Caprani. Implementation of a low round-off summation method. BIT, 11: 271-275, 1971.   
[204] B. E. Carpenter and R. W. Doran, editors. A. M. Turing's ACE Report of 1946 and Other Papers, volume 10 of Charles Babbage Institute Reprint Series for the History of Computing. MIT Press, Cambridge, MA, USA, 1986. vii+141 pp. ISBN 0-262-03114-0.   
[205] John W. Carr III. Error analysis in floating point arithmetic. Comm. ACM, 2(5): 10-15, 1959.   
[206] Russell Carter. Y-MP floating point and Cholesky factorization. Int. J. High Speed Computing, 3(3/4):215-222, 1991.   
[207] A. Cauchy. Exercices d'Analyse et de Phys. Math., volume 2. Paris, 1841. Cited in [1013].   
[208] Françoise Chaitin-Chatelin and Valérie Frayssé. Lectures on Finite Precision Computations. Society for Industrial and Applied Mathematics, Philadelphia, PA, USA, 1996. xv+235 pp. ISBN 0-89871-358-7.   
[209] N. N. Chan and Kim-Hung Li. Algorithm 115: A FORTRAN subroutine for finding a real symmetric matrix with prescribed diagonal elements and eigenvalues. Comput. J., 26(2):184-186, 1983.   
[210] N. N. Chan and Kim-Hung Li. Diagonal elements and eigenvalues of a real symmetric matrix. J. Math. Anal. Appl., 91:562-566, 1983.   
[211] Raymond H. Chan and Michael K. Ng. Conjugate gradient methods for Toeplitz systems. SIAM Rev., 38(3):427-482, 1996.   
[212] T. F. Chan and P. C. Hansen. Some applications of the rank revealing QR factorization. SIAM J. Sci. Statist. Comput., 13(3):727-741, 1992.   
[213] Tony F. Chan and David E. Foulser. Effectively well-conditioned linear systems. SIAM J. Sci. Statist. Comput., 9(6):963-969, 1988.   
[214] Tony F. Chan, Gene H. Golub, and Randall J. LeVeque. Algorithms for computing the sample variance: Analysis and recommendations. The American Statistician, 37(3):242-247, 1983.   
[215] Tony F. Chan and John Gregg Lewis. Computing standard derivations: Accuracy. Comm. ACM, 22(9):526-531, 1979.   
[216] Shivkumar Chandrasekaran and Ilse C. F. Ipsen. Backward errors for eigenvalue and singular value decompositions. Numer. Math., 68:215-223, 1994.   
[217] Shivkumar Chandrasekaran and Ilse C. F. Ipsen. On the sensitivity of solution components in linear systems of equations. SIAM J. Matrix Anal. Appl., 16(1): 93-112, 1995.   
[218] Xiao-Wen Chang and Christopher C. Paige. On the sensitivity of the LU factorization. BIT, 38(3):486-501, 1998.   
[219] Xiao-Wen Chang and Christopher C. Paige. Componentwise perturbation analyses for the QR factorization. Numer. Math., 88:319-345, 2001.   
[220] Xiao-Wen Chang, Christopher C. Paige, and G. W. Stewart. New perturbation analyses for the Cholesky factorization. IMA J. Numer. Anal., 16(4):457-484, 1996.   
[221] Xiao-Wen Chang, Christopher C. Paige, and G. W. Stewart. Perturbation analyses for the QR factorization. SIAM J. Matrix Anal. Appl., 18(3):775-791, 1997.

[222] Bruce W. Char, Keith O. Geddes, Gaston H. Gonnet, Benton L. Leong, Michael B. Monagan, and Stephen M. Watt. Maple V Library Reference Manual. Springer-Verlag, Berlin, 1991. xxv+698 pp. ISBN 3-540-97592-6.   
[223] Bruce A. Chartres and James C. Geuder. Computable error bounds for direct solution of linear equations. J. Assoc. Comput. Mach., 14(1):63-71, 1967.   
[224] Françoise Chatelin. Eigenvalues of Matrices. Wiley, Chichester, UK, 1993. xviii+382 pp. ISBN 0-471-93538-7.   
[225] Françoise Chatelin and Marie-Christine Brunet. A probabilistic round-off error propagation model. Application to the eigenvalue problem. In *Reliable Numerical Computation*, M. G. Cox and S. J. Hammarling, editors, Oxford University Press, 1990, pages 139-160.   
[226] Françoise Chatelin and Valérie Frayssé. Elements of a condition theory for the computational analysis of algorithms. In Iterative Methods in Linear Algebra, R. Beauwens and P. de Groen, editors, Elsevier Science Publishers B.V. (North-Holland), Amsterdam, The Netherlands, 1992, pages 15-25.   
[227] Sheung Hun Cheng. Symmetric Indefinite Matrices: Linear System Solvers and Modified Inertia Problems. PhD thesis, University of Manchester, Manchester, England, January 1998. 150 pp.   
[228] Sheung Hun Cheng and Nicholas J. Higham. A modified Cholesky algorithm based on a symmetric indefinite factorization. SIAM J. Matrix Anal. Appl., 19 (4):1097-1110, 1998.   
[229] Sheung Hun Cheng and Nicholas J. Higham. Implementation for LAPACK of a block algorithm for matrix 1-norm estimation. Numerical Analysis Report No. 393, Manchester Centre for Computational Mathematics, Manchester, England, August 2001. 19 pp. LAPACK Working Note 152.   
[230] Sheung Hun Cheng and Nicholas J. Higham. Parallel implementation of a block algorithm for matrix 1-norm estimation. In Euro-Par 2001, Parallel Processing, Rizos Sakellariou, John Keane, John Gurd, and Len Freeman, editors, volume 2150 of Lecture Notes in Computer Science, Springer-Verlag, Berlin, 2001, pages 568-577.   
[231] Sheung Hun Cheng, Nicholas J. Higham, Charles S. Kenney, and Alan J. Laub. Approximating the logarithm of a matrix to specified accuracy. SIAM J. Matrix Anal. Appl., 22(4):1112-1125, 2001.   
[232] Choong Yun Cho. On the triangular decomposition of Cauchy matrices. Math. Comp., 2(104):819-825, 1968.   
[233] Man-Duen Choi. Tricks or treats with the Hilbert matrix. Amer. Math. Monthly, 90:301-312, 1983.   
[234] Søren Christiansen and Per Christian Hansen. The effective condition number applied to error analysis of certain boundary collocation methods. J. Comput. Appl. Math., 54:15-36, 1994.   
[235] Eleanor Chu and Alan George. A note on estimating the error in Gaussian elimination without pivoting. ACM SIGNUM Newsletter, 20(2):2-7, 1985.   
[236] King-wah Eric Chu. The solution of the matrix equations $AXB - CXD = E$ and $(YA - DZ, YC - BZ) = (E, F)$ . Linear Algebra Appl., 93:93-105, 1987.   
[237] Moody T. Chu. On constructing matrices with prescribed singular values and diagonal elements. Linear Algebra Appl., 288:11-22, 1999.

[238] Moody T. Chu. A fast recursive algorithm for constructing matrices with prescribed eigenvalues and singular values. SIAM J. Numer. Anal., 37(3):1004-1020, 2000.   
[239] C. W. Clenshaw. A note on the summation of Chebyshev series. M.T.A.C., 9 (51):118-120, 1955.   
[240] C. W. Clenshaw and F. W. J. Olver. Beyond floating point. J. Assoc. Comput. Mach., 31(2):319-328, 1984.   
[241] C. W. Clenshaw, F. W. J. Olver, and P. R. Turner. Level-index arithmetic: An introductory survey. In Numerical Analysis and Parallel Processing, Lancaster 1987, Peter R. Turner, editor, volume 1397 of Lecture Notes in Mathematics, Springer-Verlag, Berlin, 1989, pages 95-168.   
[242] A. K. Cline. An elimination method for the solution of linear least squares problems. SIAM J. Numer. Anal., 10(2):283-289, 1973.   
[243] A. K. Cline, C. B. Moler, G. W. Stewart, and J. H. Wilkinson. An estimate for the condition number of a matrix. SIAM J. Numer. Anal., 16(2):368-375, 1979.   
[244] A. K. Cline and R. K. Rew. A set of counter-examples to three condition number estimators. SIAM J. Sci. Statist. Comput., 4(4):602-611, 1983.   
[245] Alan K. Cline, Andrew R. Conn, and Charles F. Van Loan. Generalizing the LINPACK condition estimator. In Numerical Analysis, Mexico 1981, J. P. Hennart, editor, volume 909 of Lecture Notes in Mathematics, Springer-Verlag, Berlin, 1982, pages 73-83.   
[246] R. E. Cline and R. J. Plemmons. $l_{2}$ -solutions to underdetermined linear systems. SIAM Rev., 18(1):92-106, 1976.   
[247] William D. Clinger. How to read floating point numbers accurately. SIGPLAN Notices, 25(6):92-101, 1990.   
[248] B. Codenotti, M. Leoncini, and F. P. Preparata. The role of arithmetic in fast parallel matrix inversion. Algorithmica, 30(4):685-707, 2001.   
[249] W. J. Cody. Implementation and testing of function software. In *Problems and Methodologies in Mathematical Software Production*, Paul C. Messina and Almerico Murli, editors, volume 142 of Lecture Notes in Computer Science, Springer-Verlag, Berlin, 1982, pages 24-47.   
[250] W. J. Cody. ALGORITHM 665 MACHAR: A subroutine to dynamically determine machine parameters. ACM Trans. Math. Software, 14(4):303-311, 1988.   
[251] W. J. Cody. Floating-point standards—Theory and practice. In Reliability in Computing: The Role of Interval Methods in Scientific Computing, Ramon E. Moore, editor, Academic Press, Boston, MA, USA, 1988, pages 99-107.   
[252] W. J. Cody. Algorithm 714. CELEFUNT: A portable test package for complex elementary functions. ACM Trans. Math. Software, 19(1):121, 1993.   
[253] W. J. Cody, J. T. Coonen, D. M. Gay, K. Hanson, D. Hough, W. Kahan, R. Karpinski, J. Palmer, F. N. Ris, and D. Stevenson. A proposed radix- and word-length-independent standard for floating-point arithmetic. IEEE Micro, 4 (4):86-100, 1984.   
[254] W. J. Cody and Jerome T. Coonen. ALGORITHM 722: Functions to support the IEEE standard for binary floating-point arithmetic. ACM Trans. Math. Software, 19(4):443-451, 1993.

[255] William J. Cody, Jr. Static and dynamic numerical characteristics of floating-point arithmetic. IEEE Trans. Comput., C-22(6):598-601, 1973.   
[256] William J. Cody, Jr. and William Waite. Software Manual for the Elementary Functions. Prentice-Hall, Englewood Cliffs, NJ, USA, 1980. x+269 pp. ISBN 0-13-822064-6.   
[257] A. M. Cohen. A note on pivot size in Gaussian elimination. Linear Algebra Appl., 8:361-368, 1974.   
[258] A. M. Cohen. The inverse of a Pascal matrix. Mathematical Gazette, 59(408): 111-112, 1975.   
[259] Marty S. Cohen, T. E. Hull, and V. Carl Hamacher. CADAC: A controlled-precision decimal arithmetic unit. IEEE Trans. Comput., C-32(4):370-377, 1983.   
[260] Apple Computer. *Apple Numerics Manual*. Second edition, Addison-Wesley, Reading, MA, USA, 1988.   
[261] Apple Computer. Inside Macintosh: PowerPC Numerics. Addison-Wesley, Reading, MA, USA, 1994. ISBN 0-201-40728-0.   
[262] P. Concus, G. H. Golub, and G. Meurant. Block preconditioning for the conjugate gradient method. SIAM J. Sci. Statist. Comput., 6(1):220-252, 1985.   
[263] Andrew R. Conn, Nicholas I. M. Gould, and Philippe L. Toint. LANCELOT: A Fortran Package for Large-Scale Nonlinear Optimization (Release A). Springer-Verlag, Berlin, 1992. xviii+330 pp. ISBN 0-387-55470-X.   
[264] Samuel D. Conte and Carl de Boor. Elementary Numerical Analysis: An Algorithmic Approach. Third edition, McGraw-Hill, Tokyo, 1980. xii+432 pp. ISBN 0-07-066228-2.   
[265] James W. Cooley. How the FFT gained acceptance. In A History of Scientific Computing, Stephen G. Nash, editor, Addison-Wesley, Reading, MA, USA, 1990, pages 133-140.   
[266] James W. Cooley. Lanczos and the FFT: A discovery before its time. In Proceedings of the Cornelius Lanczos International Centenary Conference, J. David Brown, Moody T. Chu, Donald C. Ellison, and Robert J. Plemmons, editors, Society for Industrial and Applied Mathematics, Philadelphia, PA, USA, 1994, pages 3-9.   
[267] James W. Cooley and John W. Tukey. An algorithm for the machine calculation of complex Fourier series. Math. Comp., 19(90):297-301, 1965.   
[268] James W. Cooley and John W. Tukey. On the origin and publication of the FFT paper. Current Contents, (51-52):8-9, 1993.   
[269] Brian A. Coomes, Hüseyin Kocak, and Kenneth J. Palmer. Rigorous computational shadowing of orbits of ordinary differential equations. Numer. Math., 69 (4):401-421, 1995.   
[270] Jerome T. Coonen. Underflow and the denormalized numbers. Computer, 14: 75-87, 1981.   
[271] J. E. Cope and B. W. Rust. Bounds on solutions of linear systems with inaccurate data. SIAM J. Numer. Anal., 16(6):950-963, 1979.   
[272] Don Coppersmith and Shmuel Winograd. Matrix multiplication via arithmetic progressions. In Proceedings of the Nineteenth Annual ACM Symposium on Theory of Computing, ACM Press, New York, 1987, pages 1-6.

[273] Marius Cornea-Hasegan and Bob Norin. IA-64 floating-point operations and the IEEE standard for binary floating-point arithmetic. Intel Technology Journal, Q4, 1999. http://developer.intel.com/technology/itj/.   
[274] Richard W. Cottle. Manifestations of the Schur complement. Linear Algebra Appl., 8:189-211, 1974.   
[275] Anthony J. Cox and Nicholas J. Higham. Stability of Householder QR factorization for weighted least squares problems. In Numerical Analysis 1997, Proceedings of the 17th Dundee Biennial Conference, D. F. Griffiths, D. J. Higham, and G. A. Watson, editors, volume 380 of Pitman Research Notes in Mathematics, Addison Wesley Longman, Harlow, Essex, UK, 1998, pages 57-73.   
[276] Anthony J. Cox and Nicholas J. Higham. Accuracy and stability of the null space method for solving the equality constrained least squares problem. BIT, 39(1): 34-50, 1999.   
[277] Anthony J. Cox and Nicholas J. Higham. Backward error bounds for constrained least squares problems. BIT, 39(2):210-227, 1999.   
[278] Anthony J. Cox and Nicholas J. Higham. Row-wise backward stable elimination methods for the equality constrained least squares problem. SIAM J. Matrix Anal. Appl., 21(1):313-326, 1999.   
[279] M. G. Cox and S. J. Hammarling, editors. Reliable Numerical Computation. Oxford University Press, 1990. xvi+339 pp. ISBN 0-19-853564-3.   
[280] Fred D. Crary. A versatile precompiler for nonstandard arithmetics. ACM Trans. Math. Software, 5(2):204-217, 1979.   
[281] Prescott D. Crout. A short method for evaluating determinants and solving systems of linear equations with real or complex coefficients. Trans. Amer. Inst. Elec. Eng., 60:1235-1241, 1941.   
[282] Colin W. Cryer. Pivot size in Gaussian elimination. Numer. Math., 12:335-345, 1968.   
[283] Colin W. Cryer. The LU-factorization of totally positive matrices. Linear Algebra Appl., 7:83-92, 1973.   
[284] Colin W. Cryer. Some properties of totally positive matrices. Linear Algebra Appl., 15:1-25, 1976.   
[285] L. Csanky. Fast parallel matrix inversion algorithms. SIAM J. Comput., 5(4): 618-623, 1976.   
[286] A. R. Curtis and J. K. Reid. On the automatic scaling of matrices for Gaussian elimination. J. Inst. Maths. Applics., 10:118-124, 1972.   
[287] George Cybenko and Charles F. Van Loan. Computing the minimum eigenvalue of a symmetric positive definite Toeplitz matrix. SIAM J. Sci. Statist. Comput., 7(1):123-131, 1986.   
[288] G. Dahlquist. On matrix majorants and minorants, with applications to differential equations. Linear Algebra Appl., 52/53:199-216, 1983.   
[289] Germund Dahlquist and Åke Björck. Numerical Methods. Prentice-Hall, Englewood Cliffs, NJ, USA, 1974. xviii+573 pp. Translated by Ned Anderson. ISBN 0-13-627315-7.   
[290] J. W. Daniel, W. B. Gragg, L. Kaufman, and G. W. Stewart. Reorthogonalization and stable algorithms for updating the Gram-Schmidt QR factorization. Math. Comp., 30(136):772-795, 1976.

[291] B. Danloy. On the choice of signs for Householder's matrices. J. Comput. Appl. Math., 2(1):67-69, 1976.   
[292] Karabi Datta. The matrix equation $XA - BX = R$ and its applications. Linear Algebra Appl., 109:91-105, 1988.   
[293] Philip I. Davies and Nicholas J. Higham. Numerically stable generation of correlation matrices and their factors. BIT, 40(4):640-651, 2000.   
[294] Philip J. Davis. Circulant Matrices. Wiley, New York, 1979. xv+250 pp. ISBN 0-471-05771-1.   
[295] Philip J. Davis and Philip Rabinowitz. Methods of Numerical Integration. Second edition, Academic Press, London, 1984. xiv+612 pp. ISBN 0-12-206360-0.   
[296] Achiya Dax. Partial pivoting strategies for symmetric Gaussian elimination. Math. Programming, 22:288-303, 1982.   
[297] Achiya Dax. The convergence of linear stationary iterative processes for solving singular unstructured systems of linear equations. SIAM Rev., 32(4):611-635, 1990.   
[298] Achiya Dax and S. Kaniel. Pivoting techniques for symmetric Gaussian elimination. Numer. Math., 28:221-241, 1977.   
[299] Jane M. Day and Brian Peterson. Growth in Gaussian elimination. Amer. Math. Monthly, 95(6):489-513, 1988.   
[300] Carl de Boor and Allan Pinkus. Backward error analysis for totally positive linear systems. Numer. Math., 27:485-490, 1977.   
[301] Lieuwe Sytse de Jong. Towards a formal definition of numerical stability. Numer. Math., 28:211-219, 1977.   
[302] T. J. Dekker. A floating-point technique for extending the available precision. Numer. Math., 18:224-242, 1971.   
[303] T. J. Dekker and W. Hoffmann. Rehabilitation of the Gauss-Jordan algorithm. Numer. Math., 54:591-599, 1989.   
[304] Ron S. Dembo, Stanley C. Eisenstat, and Trond Steihaug. Inexact Newton methods. SIAM J. Numer. Anal., 19(2):400-408, 1982.   
[305] Cédric J. Demeure. Fast QR factorization of Vandermonde matrices. Linear Algebra Appl., 122/3/4:165-194, 1989.   
[306] Cédric J. Demeure. $QR$ factorization of confluent Vandermonde matrices. IEEE Trans. Acoust., Speech, Signal Processing, 38(10):1799-1802, 1990.   
[307] James W. Demmel. The condition number of equivalence transformations that block diagonalize matrix pencils. SIAM J. Numer. Anal., 20(3):599-610, 1983.   
[308] James W. Demmel. Underflow and the reliability of numerical software. SIAM J. Sci. Statist. Comput., 5(4):887-919, 1984.   
[309] James W. Demmel. On condition numbers and the distance to the nearest ill-posed problem. Numer. Math., 51:251-289, 1987.   
[310] James W. Demmel. On error analysis in arithmetic with varying relative precision. In Proceedings of the Eighth Symposium on Computer Arithmetic, Como, Italy, Mary Jane Irwin and Renato Stefanelli, editors, IEEE Computer Society, Washington, D.C., 1987, pages 148-152.   
[311] James W. Demmel. On floating point errors in Cholesky. Technical Report CS-89-87, Department of Computer Science, University of Tennessee, Knoxville, TN, USA, October 1989. 6 pp. LAPACK Working Note 14.

[312] James W. Demmel. On the odor of IEEE arithmetic. *NA Digest*, Volume 91, Issue 39, 1991. (Response to a message "IEEE Arithmetic Stinks" in Volume 91, Issue 33.)   
[313] James W. Demmel. The componentwise distance to the nearest singular matrix. SIAM J. Matrix Anal. Appl., 13(1):10-19, 1992.   
[314] James W. Demmel. Open problems in numerical linear algebra. IMA Preprint Series #961, Institute for Mathematics and Its Applications, University of Minnesota, Minneapolis, MN, USA, April 1992. 21 pp. LAPACK Working Note 47.   
[315] James W. Demmel. A specification for floating point parallel prefix. Technical Report CS-92-167, Department of Computer Science, University of Tennessee, Knoxville, TN, USA, July 1992. 8 pp. LAPACK Working Note 49.   
[316] James W. Demmel. Trading off parallelism and numerical stability. In Linear Algebra for Large Scale and Real-Time Applications, Marc S. Moonen, Gene H. Golub, and Bart L. De Moor, editors, volume 232 of NATO ASI Series E, Kluwer Academic Publishers, Dordrecht, The Netherlands, 1993, pages 49-68.   
[317] James W. Demmel. Applied Numerical Linear Algebra. Society for Industrial and Applied Mathematics, Philadelphia, PA, USA, 1997. xi+419 pp. ISBN 0-89871-389-7.   
[318] James W. Demmel. Accurate singular value decompositions of structured matrices. SIAM J. Matrix Anal. Appl., 21(2):562-580, 1999.   
[319] James W. Demmel. A note on accurate floating point summation. Manuscript, 2001. 5 pp.   
[320] James W. Demmel, Inderjit Dhillon, and Huan Ren. On the correctness of some bisection-like parallel eigenvalue algorithms in floating point arithmetic. *Electron. Trans.* Numer. Anal., 3:116-149, 1995.   
[321] James W. Demmel, Benjamin Diament, and Gregorio Malajovich. On the complexity of computing error bounds. Found. Comput. Math., 1(1):101-125, 2001.   
[322] James W. Demmel, J. J. Dongarra, and W. Kahan. On designing portable high performance numerical libraries. In Numerical Analysis 1991, Proceedings of the 14th Dundee Conference, D. F. Griffiths and G. A. Watson, editors, volume 260 of Pitman Research Notes in Mathematics, Longman Scientific and Technical, Essex, UK, 1992, pages 69-84.   
[323] James W. Demmel, Ming Gu, Stanley Eisenstat, Ivan Slapnicar, Krešimir Veselic, and Zlatko Drmac. Computing the singular value decomposition with high relative accuracy. Linear Algebra Appl., 299:21-80, 1999.   
[324] James W. Demmel and Nicholas J. Higham. Stability of block algorithms with fast level-3 BLAS. ACM Trans. Math. Software, 18(3):274-291, 1992.   
[325] James W. Demmel and Nicholas J. Higham. Improved error bounds for underdetermined system solvers. SIAM J. Matrix Anal. Appl., 14(1):1-14, 1993.   
[326] James W. Demmel, Nicholas J. Higham, and Robert S. Schreiber. Stability of block LU factorization. Numerical Linear Algebra with Applications, 2(2):173-190, 1995.   
[327] James W. Demmel and Bo Kågström. Computing stable eigendecompositions of matrix pencils. Linear Algebra Appl., 88/89:139-186, 1987.   
[328] James W. Demmel and Bo Kågström. Accurate solutions of ill-posed problems in control theory. SIAM J. Matrix Anal. Appl., 9(1):126-145, 1988.

[329] James W. Demmel and W. Kahan. Accurate singular values of bidiagonal matrices. SIAM J. Sci. Statist. Comput., 11(5):873-912, 1990.   
[330] James W. Demmel and F. Krückeberg. An interval algorithm for solving systems of linear equations to prespecified accuracy. Computing, 34:117-129, 1985.   
[331] James W. Demmel and Xiaoye Li. Faster numerical algorithms via exception handling. IEEE Trans. Comput., 43(8):983-992, 1994.   
[332] James W. Demmel and A. McKenney. A test matrix generation suite. Preprint MCS-P69-0389, Mathematics and Computer Science Division, Argonne National Laboratory, Argonne, IL, USA, March 1989. 16 pp. LAPACK Working Note 9.   
[333] John E. Dennis, Jr. and Robert B. Schnabel. Numerical Methods for Unconstrained Optimization and Nonlinear Equations. Prentice-Hall, Englewood Cliffs, NJ, USA, 1983. xiii+378 pp. Reprinted by Society for Industrial and Applied Mathematics, Philadelphia, PA, USA, 1996. ISBN 0-13-627216-9 (original), 0-89871-364-1 (reprint).   
[334] John E. Dennis, Jr. and Virginia Torczon. Direct search methods on parallel machines. SIAM J. Optim., 1(4):448-474, 1991.   
[335] John E. Dennis, Jr. and Homer F. Walker. Inaccuracy in quasi-Newton methods: Local improvement theorems. Math. Prog. Study, 22:70-85, 1984.   
[336] John E. Dennis, Jr. and Henry Wolkowicz. Sizing and least-change secant methods. SIAM J. Numer. Anal., 30(5):1291-1314, 1993.   
[337] J. Descloux. Note on the round-off errors in iterative processes. Math. Comp., 17: 18-27, 1963.   
[338] Inderjit Dhillon. Reliable computation of the condition number of a tridiagonal matrix in $O(n)$ time. SIAM J. Matrix Anal. Appl., 19(3):776-796, 1998.   
[339] Harold G. Diamond. Stability of rounded off inverses under iteration. Math. Comp., 32(141):227-232, 1978.   
[340] John D. Dixon. Estimating extremal eigenvalues and condition numbers of matrices. SIAM J. Numer. Anal., 20(4):812-814, 1983.   
[341] J. J. Dongarra, J. R. Bunch, C. B. Moler, and G. W. Stewart. LINPACK Users' Guide. Society for Industrial and Applied Mathematics, Philadelphia, PA, USA, 1979. ISBN 0-89871-172-X.   
[342] J. J. Dongarra, J. J. Du Croz, I. S. Duff, and S. J. Hammarling. A set of Level 3 basic linear algebra subprograms. ACM Trans. Math. Software, 16:1-17, 1990.   
[343] J. J. Dongarra, J. J. Du Croz, I. S. Duff, and S. J. Hammarling. Algorithm 679. A set of Level 3 basic linear algebra subprograms: Model implementation and test programs. ACM Trans. Math. Software, 16:18-28, 1990.   
[344] J. J. Dongarra, F. G. Gustavson, and A. Karp. Implementing linear algebra algorithms for dense matrices on a vector pipeline machine. SIAM Rev., 26(1): 91-112, 1984.   
[345] Jack Dongarra, Victor Eijkhout, and Piotr Luszczek. Recursive approach in sparse matrix LU factorization. In Proceedings of the 1st SGI Users Conference, Cracow, Poland, October 2000, pages 409-418. ACC Cyfronet UMM.   
[346] Jack J. Dongarra. Performance of various computers using standard linear equations software. Technical Report CS-89-85, Department of Computer Science, University of Tennessee, Knoxville, TN, USA, August 2001. 58 pp.

[347] Jack J. Dongarra, Jeremy J. Du Croz, Sven J. Hammarling, and Richard J. Hanson. An extended set of Fortran basic linear algebra subprograms. ACM Trans. Math. Software, 14(1):1-17, 1988.   
[348] Jack J. Dongarra, Jeremy J. Du Croz, Sven J. Hammarling, and Richard J. Hanson. Algorithm 656. An extended set of Fortran basic linear algebra subprograms: Model implementation and test programs. ACM Trans. Math. Software, 14(1): 18-32, 1988.   
[349] Jack J. Dongarra, Iain S. Duff, Danny C. Sorensen, and Henk A. van der Vorst. Numerical Linear Algebra for High-Performance Computers. Society for Industrial and Applied Mathematics, Philadelphia, PA, USA, 1998. xviii+342 pp. ISBN 0-89871-428-1.   
[350] Jack J. Dongarra and Eric Grosse. Distribution of mathematical software via electronic mail. Comm. ACM, 30(5):403-407, 1987.   
[351] Craig C. Douglas, Michael Heroux, Gordon Slishman, and Roger M. Smith. GEMMW: A portable level 3 BLAS Winograd variant of Strassen's matrix-matrix multiply algorithm. J. Comput. Phys., 110:1-10, 1994.   
[352] Craig C. Douglas and Gordon Slishman. Variants of matrix-matrix multiplication for Fortran-90. ACM SIGNUM Newsletter, 29:4-6, 1994.   
[353] Jim Douglas, Jr. Round-off error in the numerical solution of the heat equation. J. Assoc. Comput. Mach., 6:48-58, 1959.   
[354] Thomas C. Doyle. Inversion of symmetric coefficient matrix of positive-definite quadratic form. M.T.A.C., 11:55-58, 1957.   
[355] J. Drkošová, A. Greenbaum, M. Rozložník, and Z. Strakos. Numerical stability of GMRES. BIT, 35:309-330, 1995.   
[356] Zlatko Drmac, Matjaz Omladic, and Krešimir Veselic. On the perturbation of the Cholesky factorization. SIAM J. Matrix Anal. Appl., 15(4):1319-1332, 1994.   
[357] Jeremy J. Du Croz and Nicholas J. Higham. Stability of methods for matrix inversion. IMA J. Numer. Anal., 12:1-19, 1992.   
[358] Augustin A. Dubrulle. A class of numerical methods for the computation of Pythagorean sums. IBM J. Res. Develop., 27(6):582-589, 1983.   
[359] Augustin A. Dubrulle and Gene H. Golub. A multishift QR iteration without computation of the shifts. Numerical Algorithms, 7:173-181, 1994.   
[360] I. S. Duff, A. M. Erisman, and J. K. Reid. Direct Methods for Sparse Matrices. Oxford University Press, 1986. xiii+341 pp. ISBN 0-19-853408-6.   
[361] I. S. Duff, N. I. M. Gould, J. K. Reid, J. A. Scott, and K. Turner. The factorization of sparse symmetric indefinite matrices. *IMA J. Numer. Anal.*, 11:181-204, 1991.   
[362] Iain S. Duff, Roger G. Grimes, and John G. Lewis. Sparse matrix test problems. ACM Trans. Math. Software, 15(1):1-14, 1989.   
[363] Iain S. Duff, Roger G. Grimes, and John G. Lewis. Users' guide for the Harwell-Boeing sparse matrix collection (release 1). Report RAL-92-086, Atlas Centre, Rutherford Appleton Laboratory, Didcot, Oxon, UK, December 1992. 84 pp.   
[364] Iain S. Duff and John K. Reid. MA27—A set of Fortran subroutines for solving sparse symmetric sets of linear equations. Technical Report AERE R10533, AERE Harwell Laboratory, July 1982. Published by Her Majesty's Stationary Office, London.

[365] Iain S. Duff and John K. Reid. MA47, a Fortran code for direct solution of indefinite sparse symmetric linear systems. Report RAL-95-001, Atlas Centre, Rutherford Appleton Laboratory, Didcot, Oxon, UK, January 1995. 63 pp.   
[366] Iain S. Duff, John K. Reid, Neils Munskgaard, and Hans B. Nielsen. Direct solution of sets of linear equations whose matrix is sparse, symmetric and indefinite. J. Inst. Maths. Applics., 23:235-250, 1979.   
[367] Bogdan Dumitrescu. Improving and estimating the accuracy of Strassen's algorithm. Numer. Math., 79:485-499, 1998.   
[368] William Dunham. Journey Through Genius: The Great Theorems of Mathematics. Penguin, New York, 1990. xiii+300 pp. ISBN 0-14-014739-X.   
[369] Paul S. Dwyer. Linear Computations. Wiley, New York, 1951. xi+344 pp.   
[370] Carl Eckart and Gale Young. The approximation of one matrix by another of lower rank. Psychometrika, 1(3):211-218, 1936.   
[371] Alan Edelman. Eigenvalues and condition numbers of random matrices. SIAM J. Matrix Anal. Appl., 9(4):543-560, 1988.   
[372] Alan Edelman. The distribution and moments of the smallest eigenvalue of a random matrix of Wishart type. Linear Algebra Appl., 159:55-80, 1991.   
[373] Alan Edelman. The first annual large dense linear system survey. ACM SIGNUM Newsletter, 26:6-12, 1991.   
[374] Alan Edelman. The complete pivoting conjecture for Gaussian elimination is false. The Mathematica Journal, 2:58-61, 1992.   
[375] Alan Edelman. On the distribution of a scaled condition number. Math. Comp., 58(197):185-190, 1992.   
[376] Alan Edelman. Eigenvalue roulette and random test matrices. In Linear Algebra for Large Scale and Real-Time Applications, Marc S. Moonen, Gene H. Golub, and Bart L. De Moor, editors, volume 232 of NATO ASI Series E, Kluwer Academic Publishers, Dordrecht, The Netherlands, 1993, pages 365-368.   
[377] Alan Edelman. Large dense numerical linear algebra in 1993: The parallel computing influence. Internat. J. Supercomputer Appl., 7(2):113-128, 1993.   
[378] Alan Edelman. Scalable dense numerical linear algebra in 1994: The multicomputer influence. In Proceedings of the Fifth SIAM Conference on Applied Linear Algebra, John G. Lewis, editor, Society for Industrial and Applied Mathematics, Philadelphia, PA, USA, 1994, pages 344-348.   
[379] Alan Edelman. When is $x * (1 / x) \neq 1$ ? Manuscript, 1994.   
[380] Alan Edelman. The mathematics of the Pentium division bug. SIAM Rev., 39(1): 54-67, 1997.   
[381] Alan Edelman, Eric Kostlan, and Michael Shub. How many eigenvalues of a random matrix are real? J. Amer. Math. Soc., 7(1):247-267, 1994.   
[382] Alan Edelman and Walter Mascarenhas. On the complete pivoting conjecture for a Hadamard matrix of order 12. Linear and Multilinear Algebra, 38(3):181-188, 1995.   
[383] Alan Edelman and H. Murakami. Polynomial roots from companion matrix eigenvalues. Math. Comp., 64(210):763-776, 1995.   
[384] Alan Edelman and G. W. Stewart. Scaling for orthogonality. IEEE Trans. Signal Processing, 41(4):1676-1677, 1993.

[385] Editor's note. SIAM J. Matrix Anal. Appl., 12(3), 1991.   
[386] Timo Eirola. Aspects of backward error analysis of numerical ODEs. J. Comput. Appl. Math., 45(1-2):65-73, 1993.   
[387] Lars Eldén. Perturbation theory for the least squares problem with linear equality constraints. SIAM J. Numer. Anal., 17(3):338-350, 1980.   
[388] Samuel K. Eldersveld and Michael A. Saunders. A block- $LU$ update for large-scale linear programming. SIAM J. Matrix Anal. Appl., 13(1):191-201, 1992.   
[389] Mark Embree and Lloyd N. Trefethen. Pseudospectra gateway. http://www.comlab.ox.ac.uk/pseudospectra/.   
[390] W. H. Enright. A new error-control for initial value solvers. Appl. Math. Comput., 31:288-301, 1989.   
[391] Michael A. Epton. Methods for the solution of $AXD - BXC = E$ and its application in the numerical solution of implicit ordinary differential equations. BIT, 20:341-345, 1980.   
[392] A. M. Erisman, R. G. Grimes, J. G. Lewis, W. G. Poole, and H. D. Simon. Evaluation of orderings for unsymmetric sparse matrices. SIAM J. Sci. Statist. Comput., 8(4):600-624, 1987.   
[393] A. M. Erisman and J. K. Reid. Monitoring the stability of the triangular factorization of a sparse matrix. Numer. Math., 22:183-186, 1974.   
[394] Terje O. Espelid. On floating-point summation. SIAM Rev., 37(4):603-607, 1995.   
[395] Christopher Evans. Interview with J. H. Wilkinson. Number 10 in Pioneers of Computing, 60-Minute Recordings of Interviews. Science Museum, London, 1976.   
[396] Ömer Egecioglu, E. Gallopoulos, and C. K. Koc. A parallel method for fast and practical high-order Newton interpolation. BIT, 30:268-288, 1990.   
[397] John Ewing, editor. A Century of Mathematics Through the Eyes of the Monthly. Mathematical Association of America, Washington, D.C., 1994. xi+323 pp. ISBN 0-88385-459-7.   
[398] John H. Ewing and F. W. Gehring, editors. Paul Halmos: Celebrating 50 Years of Mathematics. Springer-Verlag, New York, 1991. viii+320 pp. ISBN 3-540-97509-8.   
[399] V. N. Faddeeva. Computational Methods of Linear Algebra. Dover, New York, 1959. x+252 pp. ISBN 0-486-60424-1.   
[400] Shaun M. Fallat. Bidiagonal factorizations of totally nonnegative matrices. Amer. Math. Monthly, 108(8):697-712, 2001.   
[401] Ky Fan and A. J. Hoffman. Some metric inequalities in the space of matrices. Proc. Amer. Math. Soc., 6:111-116, 1955.   
[402] R. W. Farebrother. A memoir of the life of M. H. Doolittle. IMA Bulletin, 23 (6/7):102, 1987.   
[403] R. W. Farebrother. Linear Least Squares Computations. Marcel Dekker, New York, 1988. xiii+293 pp. ISBN 0-8247-7661-5.   
[404] Charles Farnum. Compiler support for floating-point computation. Software—Practice and Experience, 18(7):701-709, 1988.   
[405] Richard J. Fateman. High-level language implications of the proposed IEEE floating-point standard. ACM Trans. Program. Lang. Syst., 4(2):239-257, 1982.

[406] David G. Feingold and Richard S. Varga. Block diagonally dominant matrices and generalizations of the Gerschgorin circle theorem. Pacific J. Math., 12:1241-1250, 1962.   
[407] Alan Feldstein and Richard Goodman. Loss of significance in floating point subtraction and addition. IEEE Trans. Comput., C-31(4):328-335, 1982.   
[408] Alan Feldstein and Peter Turner. Overflow, underflow, and severe loss of significance in floating-point addition and subtraction. IMA J. Numer. Anal., 6: 241-251, 1986.   
[409] Warren E. Ferguson, Jr. Exact computation of a sum or difference with applications to argument reduction. In Proc. 12th IEEE Symposium on Computer Arithmetic, Bath, England, Simon Knowles and William H. McAllister, editors, IEEE Computer Society Press, Los Alamitos, CA, USA, 1995, pages 216-221.   
[410] Warren E. Ferguson, Jr. and Tom Brightman. Accurate and monotone approximations of some transcendental functions. In Proc. 10th IEEE Symposium on Computer Arithmetic, Peter Kornerup and David W. Matula, editors, IEEE Computer Society Press, Los Alamitos, CA, USA, 1991, pages 237-244.   
[411] William R. Ferng, Gene H. Golub, and Robert J. Plemmons. Adaptive Lanczos methods for recursive condition estimation. Numerical Algorithms, 1(1):1-19, 1991.   
[412] C. T. Fike. Methods of evaluating polynomial approximations in function evaluation routines. Comm. ACM, 10(3):175-178, 1967.   
[413] C. T. Fike. Computer Evaluation of Mathematical Functions. Prentice-Hall, Englewood Cliffs, NJ, USA, 1968. xii+227 pp.   
[414] Patrick C. Fischer. Further schemes for combining matrix algorithms. In Automata, Languages and Programming, Jacques Loeckx, editor, volume 14 of Lecture Notes in Computer Science, Springer-Verlag, Berlin, 1974, pages 428-436.   
[415] R. Fletcher. Factorizing symmetric indefinite matrices. Linear Algebra Appl., 14: 257-272, 1976.   
[416] R. Fletcher. Expected conditioning. IMA J. Numer. Anal., 5:247-273, 1985.   
[417] R. Fletcher. Practical Methods of Optimization. Second edition, Wiley, Chichester, UK, 1987. xiv+436 pp. ISBN 0-471-91547-5.   
[418] R. Fletcher and M. J. D. Powell. On the modification of $LDL^T$ factorizations. Math. Comp., 28(128):1067-1087, 1974.   
[419] Brian Ford. Parameterization of the environment for transportable numerical software. ACM Trans. Math. Software, 4(2):100-103, 1978.   
[420] Anders Forsgren, Philip E. Gill, and Walter Murray. Computing modified Newton directions using a partial Cholesky factorization. SIAM J. Sci. Comput., 16(1): 139-150, 1995.   
[421] Anders Forsgren, Philip E. Gill, and Joseph R. Shinnerl. Stability of symmetric ill-conditioned systems arising in interior methods for constrained optimization. SIAM J. Matrix Anal. Appl., 17(1):187-211, 1996.   
[422] George E. Forsythe. Gauss to Gerling on relaxation. Mathematical Tables and Other Aids to Computation, 5:255-258, 1951.   
[423] George E. Forsythe. Solving linear algebraic equations can be interesting. Bull. Amer. Math. Soc., 59(4):299-329, 1953.

[424] George E. Forsythe. Reprint of a note on rounding-off errors. SIAM Rev., 1(1): 66-67, 1959.   
[425] George E. Forsythe. Algorithm 16: Crout with pivoting. Comm. ACM, 3(9): 507-508, 1960.   
[426] George E. Forsythe. Today's computational methods of linear algebra. SIAM Rev., 9:489-515, 1967.   
[427] George E. Forsythe. Solving a quadratic equation on a computer. In The Mathematical Sciences: A Collection of Essays, National Research Council's Committee on Support of Research in the Mathematical Sciences, editor, MIT Press, Cambridge, MA, USA, 1969, pages 138-152.   
[428] George E. Forsythe. What is a satisfactory quadratic equation solver? In Constructive Aspects of the Fundamental Theorem of Algebra, Bruno Dejon and Peter Henrici, editors, Wiley-Interscience, London, 1969, pages 53-61.   
[429] George E. Forsythe. Pitfalls in computation, or why a math book isn't enough. Amer. Math. Monthly, 77:931-956, 1970.   
[430] George E. Forsythe, Michael A. Malcolm, and Cleve B. Moler. Computer Methods for Mathematical Computations. Prentice-Hall, Englewood Cliffs, NJ, USA, 1977. xi+259 pp. ISBN 0-13-165332-6.   
[431] George E. Forsythe and Cleve B. Moler. Computer Solution of Linear Algebraic Systems. Prentice-Hall, Englewood Cliffs, NJ, USA, 1967. xi+148 pp.   
[432] George E. Forsythe and E. G. Straus. On best conditioned matrices. Proc. Amer. Math. Soc., 6:340-345, 1955.   
[433] Leslie Foster. Modifications of the normal equations method that are numerically stable. In Numerical Linear Algebra, Digital Signal Processing and Parallel Algorithms, G. H. Golub and P. M. Van Dooren, editors, volume F70 of NATO ASI Series, Springer-Verlag, Berlin, 1991, pages 501-512.   
[434] Leslie V. Foster. Gaussian elimination with partial pivoting can fail in practice. SIAM J. Matrix Anal. Appl., 15(4):1354-1362, 1994.   
[435] Leslie V. Foster. The growth factor and efficiency of Gaussian elimination with rook pivoting. J. Comput. Appl. Math., 86:177-194, 1997. Corrigendum in J. Comput. Appl. Math., 98:177, 1998.   
[436] L. Fox. An Introduction to Numerical Linear Algebra. Oxford University Press, 1964. xi+328 pp.   
[437] L. Fox. How to get meaningless answers in scientific computation (and what to do about it). IMA Bulletin, 7(10):296-302, 1971.   
[438] L. Fox. All about Jim Wilkinson, with a commemorative snippet on backward error analysis. In The Contribution of Dr. J. H. Wilkinson to Numerical Analysis, Symposium Proceedings Series No. 19, The Institute of Mathematics and Its Applications, Southend-On-Sea, Essex, UK, 1978, pages 1-20.   
[439] L. Fox. James Hardy Wilkinson, 1919-1986. Biographical Memoirs of Fellows of the Royal Society, 33:671-708, 1987.   
[440] L. Fox, H. D. Huskey, and J. H. Wilkinson. Notes on the solution of algebraic linear simultaneous equations. Quart. J. Mech. Appl. Math., 1:149-173, 1948.   
[441] P. A. Fox, A. D. Hall, and N. L. Schryer. The PORT mathematical subroutine library. ACM Trans. Math. Software, 4(2):104-126, 1978.

[442] Philippe Francois and Jean-Michel Muller. The SCALP perturbation method. In Proceedings of IMACS '91, 13th World Congress on Computation and Applied Mathematics, Dublin, Volume 1, 1991, pages 59-60.   
[443] Werner L. Frank. Computing eigenvalues of complex matrices by determinant evaluation and by methods of Danilewski and Wielandt. J. Soc. Indust. Appl. Math., 6:378-392, 1958.   
[444] V. Frayssé. Reliability of Computer Solutions. PhD thesis, L'Institut National Polytechnique de Toulouse, Toulouse, France, July 1992. CERFACS Report TH/PA/92/11.   
[445] Shmuel Friedland. Revisiting matrix squaring. Linear Algebra Appl., 154-156: 59-63, 1991.   
[446] Shmuel Friedland and Hans Schneider. The growth of powers of a nonnegative matrix. SIAM J. Alg. Discrete Methods, 1(2):185-200, 1980.   
[447] Matteo Frigo and Steven G. Johnson. FFTW: An adaptive software architecture for the FFT. In Proceedings of International Conference on Acoustics, Speech and Signal Processing, Volume 3, 1998, pages 1381+.   
[448] Andreas Frommer. Proving conjectures by use of interval arithmetic. In *Perspectives on Enclosure Methods*, A. Facius, U. Kulisch, and R. Lohner, editors, Springer-Verlag, New York, 2001, pages 1-13.   
[449] R. E. Funderlic, M. Neumann, and R. J. Plemmons. LU decompositions of generalized diagonally dominant matrices. Numer. Math., 40:57-69, 1982.   
[450] Pascal M. Gahinet, Alan J. Laub, Charles S. Kenney, and Gary A. Hewer. Sensitivity of the stable discrete-time Lyapunov equation. IEEE Trans. Automat. Control, AC-35(11):1209-1217, 1990.   
[451] Shmuel Gal and Boris Bachelis. An accurate elementary mathematical library for the IEEE floating point standard. ACM Trans. Math. Software, 17(1):26-45, 1991.   
[452] K. A. Gallivan, R. J. Plemmons, and A. H. Sameh. Parallel algorithms for dense linear algebra computations. SIAM Rev., 32(1):54-135, 1990.   
[453] F. R. Gantmacher. The Theory of Matrices, volume one. Chelsea, New York, 1959. x+374 pp. ISBN 0-8284-0131-4.   
[454] F. R. Gantmacher. The Theory of Matrices, volume two. Chelsea, New York, 1959. ix+276 pp. ISBN 0-8284-0133-0.   
[455] B. S. Garbow, J. M. Boyle, J. J. Dongarra, and C. B. Moler. Matrix Eigensystem Routines—EISPACK Guide Extension, volume 51 of Lecture Notes in Computer Science. Springer-Verlag, Berlin, 1977. viii+343 pp. ISBN 3-540-08254-9.   
[456] Judith D. Gardiner and Alan J. Laub. Parallel algorithms for algebraic Riccati equations. Internat. J. Control, 54(6):1317-1333, 1991.   
[457] Judith D. Gardiner, Alan J. Laub, James J. Amato, and Cleve B. Moler. Solution of the Sylvester matrix equation $AXB^T + CXD^T = E$ . ACM Trans. Math. Software, 18(2):223-231, 1992.   
[458] Judith D. Gardiner, Matthew R. Wette, Alan J. Laub, James J. Amato, and Cleve B. Moler. Algorithm 705: A FORTRAN-77 software package for solving the Sylvester matrix equation $AXB^T + CXD^T = E$ . ACM Trans. Math. Software, 18(2):232-238, 1992.

[459] Martin Gardner. More Mathematical Puzzles and Diversions. Penguin, New York, 1961. 187 pp. ISBN 0-14-020748-1.   
[460] Harvey L. Garner. A survey of some recent contributions to computer arithmetic. IEEE Trans. Comput., C-25(12):1277-1282, 1976.   
[461] M. Gasca and J. M. Pena. Total positivity and Neville elimination. Linear Algebra Appl., 165:25-44, 1992.   
[462] Noel Gastinel. Linear Numerical Analysis. Kershaw Publishing, London, 1983. ix+341 pp. First published in English by Academic Press, London, 1970. ISBN 0-901665-16-9.   
[463] Carl Friedrich Gauss. Theory of the Combination of Observations Least Subject to Errors. Part One, Part Two, Supplement. Society for Industrial and Applied Mathematics, Philadelphia, PA, USA, 1995. xi+241 pp. Translated from the Latin by G. W. Stewart. ISBN 0-89871-347-1.   
[464] Walter Gautschi. On inverses of Vandermonde and confluent Vandermonde matrices. Numer. Math., 4:117-123, 1962.   
[465] Walter Gautschi. Norm estimates for inverses of Vandermonde matrices. Numer. Math., 23:337-347, 1975.   
[466] Walter Gautschi. On inverses of Vandermonde and confluent Vandermonde matrices III. Numer. Math., 29:445-450, 1978.   
[467] Walter Gautschi. The condition of Vandermonde-like matrices involving orthogonal polynomials. Linear Algebra Appl., 52/53:293-300, 1983.   
[468] Walter Gautschi. How (un)stable are Vandermonde systems? In Asymptotic and Computational Analysis, R. Wong, editor, volume 124 of Lecture Notes in Pure and Applied Mathematics, Marcel Dekker, New York and Basel, 1990, pages 193-210.   
[469] Werner Gautschi. The asymptotic behaviour of powers of matrices. Duke Math. J., 20:127-140, 1953.   
[470] David M. Gay. Correctly rounded binary-decimal and decimal-binary conversions. Numerical Analysis Manuscript 90-10, AT&T Bell Laboratories, Murray Hill, NJ, USA, November 1990. 16 pp.   
[471] Stuart Geman. The spectral radius of large random matrices. Ann. Probab., 14 (4):1318-1328, 1986.   
[472] W. M. Gentleman. An error analysis of Goertzel's (Watt's) method for computing Fourier coefficients. Comput. J., 12:160-165, 1969.   
[473] W. M. Gentleman and G. Sande. Fast Fourier transforms--for fun and profit. In *Fall Joint Computer Conference*, volume 29 of *AFIPS Conference Proceedings*, Spartan Books, Washington, D.C., 1966, pages 563-578.   
[474] W. Morven Gentleman. Least squares computations by Givens transformations without square roots. J. Inst. Maths. Applics., 12:329-336, 1973.   
[475] W. Morven Gentleman. Error analysis of $QR$ decompositions by Givens transformations. Linear Algebra Appl., 10:189-197, 1975.   
[476] W. Morven Gentleman and Scott B. Marovich. More on algorithms that reveal properties of floating point arithmetic units. Comm. ACM, 17(5):276-277, 1974.   
[477] Alan George, Khakim D. Ikramov, and Andrey B. Kucherov. On the growth factor in Gaussian elimination for generalized Higham matrices. Numerical Linear Algebra with Applications, 9:107-114, 2002.

[478] Alan George and Joseph W-H Liu. Computer Solution of Large Sparse Positive Definite Systems. Prentice-Hall, Englewood Cliffs, NJ, USA, 1981. xii+324 pp. ISBN 0-13-165274-5.   
[479] A. J. Geurts. A contribution to the theory of condition. Numer. Math., 39:85-96, 1982.   
[480] Ali R. Ghavimi and Alan J. Laub. Backward error, sensitivity, and refinement of computed solutions of algebraic Riccati equations. Numerical Linear Algebra with Applications, 2(1):29-49, 1995.   
[481] Ali R. Ghavimi and Alan J. Laub. Residual bounds for discrete-time Lyapunov equations. IEEE Trans. Automat. Control, 40(7):1244-1249, 1995.   
[482] P. E. Gill and W. Murray. A numerically stable form of the simplex algorithm. Linear Algebra Appl., 7:99-138, 1973.   
[483] Philip E. Gill, Walter Murray, Dulce B. Ponceleón, and Michael A. Saunders. Preconditioners for indefinite systems arising in optimization. SIAM J. Matrix Anal. Appl., 13(1):292-311, 1992.   
[484] Philip E. Gill, Walter Murray, Michael A. Saunders, and Margaret H. Wright. User's guide for NPSOL (version 4.0): A Fortran package for nonlinear programming. Technical Report SOL 86-2, Department of Operations Research, Stanford University, Stanford, CA, USA, January 1986. 53 pp.   
[485] Philip E. Gill, Walter Murray, Michael A. Saunders, and Margaret H. Wright. Inertia-controlling methods for general quadratic programming. SIAM Rev., 33 (1):1-36, 1991.   
[486] Philip E. Gill, Walter Murray, and Margaret H. Wright. Practical Optimization. Academic Press, London, 1981. xvi+401 pp. ISBN 0-12-283952-8.   
[487] Philip E. Gill, Michael A. Saunders, and Joseph R. Shinnerl. On the stability of Cholesky factorization for symmetric quasidefinite systems. SIAM J. Matrix Anal. Appl., 17(1):35-46, 1996.   
[488] S. Gill. A process for the step-by-step integration of differential equations in an automatic digital computing machine. Proc. Cambridge Phil. Soc., 47:96-108, 1951.   
[489] T. A. Gillespie. Noncommutative variations on theorems of Marcel Riesz and others. In Paul Halmos: Celebrating 50 Years of Mathematics, John H. Ewing and F. W. Gehring, editors, Springer-Verlag, Berlin, 1991, pages 221-236.   
[490] Wallace J. Givens. Numerical computation of the characteristic values of a real symmetric matrix. Technical Report ORNL-1574, Oak Ridge National Laboratory, Oak Ridge, TN, USA, 1954. 107 pp.   
[491] James Glanz. Mathematical logic flushes out the bugs in chip designs. Science, 267:332-333, 1995. 20 January.   
[492] J. Gluchowska and A. Smoktunowicz. Solving the linear least squares problem with very high relative accuracy. Computing, 45:345-354, 1990.   
[493] S. K. Godunov, A. G. Antonov, O. P. Kiriljuk, and V. I. Kosten. Guaranteed Accuracy in Numerical Linear Algebra. Kluwer Academic Publishers, Dordrecht, The Netherlands, 1993. xi+535 pp. ISBN 0-7923-2352-1.   
[494] I. Gohberg and I. Koltracht. Mixed, componentwise, and structured condition numbers. SIAM J. Matrix Anal. Appl., 14(3):688-704, 1993.

[495] I. Gohberg and V. Olshysky. Fast inversion of Chebyshev-Vandermonde matrices. Numer. Math., 67(1):71-92, 1994.   
[496] David Goldberg. What every computer scientist should know about floating-point arithmetic. ACM Computing Surveys, 23(1):5-48, 1991.   
[497] I. Bennett Goldberg. 27 bits are not enough for 8-digit accuracy. Comm. ACM, 10(2):105-106, 1967.   
[498] Moshe Goldberg and E. G. Straus. Multiplicativity of $l_{p}$ norms for matrices. Linear Algebra Appl., 52/53:351-360, 1983.   
[499] Herman H. Goldstine. The Computer: From Pascal to von Neumann. Princeton University Press, Princeton, NJ, USA, 1972. xii+378 pp. 1993 printing with new preface. ISBN 0-691-02367-0.   
[500] Herman H. Goldstine. A History of Numerical Analysis from the 16th through the 19th Century. Springer-Verlag, New York, 1977. xiv+348 pp. ISBN 0-387-90277-5.   
[501] Herman H. Goldstine and John von Neumann. Numerical inverting of matrices of high order II. Proc. Amer. Math. Soc., 2:188-202, 1951. Reprinted in [1130, pp. 558-572].   
[502] G. H. Golub. Numerical methods for solving linear least squares problems. Numer. Math., 7:206-216, 1965.   
[503] G. H. Golub, S. Nash, and C. F. Van Loan. A Hessenberg-Schur method for the problem $AX + XB = C$ . IEEE Trans. Automat. Control, AC-24(6):909-913, 1979.   
[504] G. H. Golub and J. M. Varah. On a characterization of the best $\ell_2$ -scaling of a matrix. SIAM J. Numer. Anal., 11(3):472-479, 1974.   
[505] G. H. Golub and J. H. Wilkinson. Note on the iterative refinement of least squares solution. Numer. Math., 9:139-148, 1966.   
[506] G. H. Golub and J. H. Wilkinson. Ill-conditioned eigensystems and the computation of the Jordan canonical form. SIAM Rev., 18(4):578-619, 1976.   
[507] Gene H. Golub. Bounds for the round-off errors in the Richardson second order method. BIT, 2:212-223, 1962.   
[508] Gene H. Golub and Charles F. Van Loan. Unsymmetric positive definite linear systems. Linear Algebra Appl., 28:85-97, 1979.   
[509] Gene H. Golub and Charles F. Van Loan. Matrix Computations. Third edition, Johns Hopkins University Press, Baltimore, MD, USA, 1996. xxvii+694 pp. ISBN 0-8018-5413-X (hardback), 0-8018-5414-8 (paperback).   
[510] R. Goodman and A. Feldstein. Round-off error in products. Computing, 15: 263-273, 1975.   
[511] R. H. Goodman, A. Feldstein, and J. Bustoz. Relative error in floating-point multiplication. Computing, 35:127-139, 1985.   
[512] James H. Goodnight. A tutorial on the SWEEP operator. The American Statistician, 33(3):149-158, 1979.   
[513] N. I. M. Gould. On growth in Gaussian elimination with complete pivoting. SIAM J. Matrix Anal. Appl., 12(2):354-361, 1991.   
[514] W. Govaerts and J. D. Pryce. Block elimination with one iterative refinement solves bordered linear systems accurately. BIT, 30:490-507, 1990.

[515] Willy J. F. Govaerts. Numerical Methods for Bifurcations of Dynamical Equilibria. Society for Industrial and Applied Mathematics, Philadelphia, PA, USA, 2000. xxii+362 pp. ISBN 0-89871-442-7.   
[516] W. B. Gragg and G. W. Stewart. A stable variant of the secant method for solving nonlinear equations. SIAM J. Numer. Anal., 13(6):889-903, 1976.   
[517] Ronald L. Graham, Donald E. Knuth, and Oren Patashnik. *Concrete Mathematics: A Foundation for Computer Science*. Second edition, Addison-Wesley, Reading, MA, USA, 1994. xiii+657 pp. ISBN 0-201-55802-5.   
[518] Andrew Granville. Zaphod Beeblebrox's brain and the fifty-ninth row of Pascal's triangle. Amer. Math. Monthly, 99:318-331, 1992.   
[519] Anne Greenbaum. Behavior of slightly perturbed Lanczos and conjugate-gradient recurrences. Linear Algebra Appl., 113:7-63, 1989.   
[520] Anne Greenbaum. The Lanczos and conjugate gradient algorithms in finite precision arithmetic. In Proceedings of the Cornelius Lanczos International Centenary Conference, J. David Brown, Moody T. Chu, Donald C. Ellison, and Robert J. Plemmons, editors, Society for Industrial and Applied Mathematics, Philadelphia, PA, USA, 1994, pages 49-60.   
[521] Anne Greenbaum. Estimating the attainable accuracy of recursively computed residual methods. SIAM J. Matrix Anal. Appl., 18(3):535-551, 1997.   
[522] Anne Greenbaum. Iterative Methods for Solving Linear Systems. Society for Industrial and Applied Mathematics, Philadelphia, PA, USA, 1997. xiii+220 pp. ISBN 0-89871-396-X.   
[523] Anne Greenbaum and Zdeněk Strakos. Predicting the behavior of finite precision Lanczos and conjugate gradient computations. SIAM J. Matrix Anal. Appl., 13 (1):121-137, 1992.   
[524] Robert T. Gregory and David L. Karney. A Collection of Matrices for Testing Computational Algorithms. Wiley, New York, 1969. ix+154 pp. Reprinted with corrections by Robert E. Krieger, Huntington, New York, 1978. ISBN 0-88275-649-4.   
[525] Andreas Griewank. On solving nonlinear equations with simple singularities or nearly singular solutions. SIAM Rev., 27(4):537-563, 1985.   
[526] Roger G. Grimes and John G. Lewis. Condition number estimation for sparse matrices. SIAM J. Sci. Statist. Comput., 2(4):384-388, 1981.   
[527] Ming Gu. Backward perturbation bounds for linear least squares problems. SIAM J. Matrix Anal. Appl., 20(2):363-372, 1998.   
[528] Ming Gu, James W. Demmel, and Inderjit Dhillon. Efficient computation of the singular value decomposition with applications to least squares problems. Technical Report CS-94-257, Department of Computer Science, University of Tennessee, Knoxville, TN, USA, October 1994. 19 pp. LAPACK Working Note 88.   
[529] Thorkell Gudmundsson, Charles S. Kenney, and Alan J. Laub. Small-sample statistical estimates for matrix norms. SIAM J. Matrix Anal. Appl., 16(3):776-792, 1995.   
[530] Heinrich W. Guggenheimer, Alan S. Edelman, and Charles R. Johnson. A simple estimate of the condition number of a linear system. College Mathematics Journal, 26(1):2-5, 1995.   
[531] Marten Gulliksson. Iterative refinement for constrained and weighted linear least squares. BIT, 34:239-253, 1994.

[532] Mårten Gulliksson. Backward error analysis for the constrained and weighted linear least squares problem when using the weighted QR factorization. SIAM J. Matrix Anal. Appl., 16(2):675-687, 1995.   
[533] Marten Gulliksson and Per-Ake Wedin. Modifying the QR-decomposition to constrained and weighted linear least squares. SIAM J. Matrix Anal. Appl., 13(4): 1298-1313, 1992.   
[534] John L. Gustafson and Srinivas Aluru. Massively parallel searching for better algorithms or, how to do a cross product with five multiplications. Scientific Programming, pages 203-213, 1996.   
[535] F. G. Gustavson. Recursion leads to automatic variable blocking for dense linear-algebra algorithms. IBM Journal of Research and Development, 41(6):737-755, 1997.   
[536] William W. Hager. Condition estimates. SIAM J. Sci. Statist. Comput., 5(2): 311-316, 1984.   
[537] E. Hairer and G. Wanner. Solving Ordinary Differential Equations II. Springer-Verlag, Berlin, 1991. xv+601 pp. ISBN 3-540-53775-9.   
[538] Marshall Hall, Jr. Combinatorial Theory. Blaisdell, Waltham, MA, USA, 1967. x+310 pp.   
[539] Hozumi Hamada. A new real number representation and its operation. In Proceedings of the Eighth Symposium on Computer Arithmetic, Como, Italy, Mary Jane Irwin and Renato Stefanelli, editors, IEEE Computer Society, Washington, D.C., 1987, pages 153-157.   
[540] S. J. Hammarling. Numerical solution of the stable, non-negative definite Lyapunov equation. IMA J. Numer. Anal., 2:303-323, 1982.   
[541] S. J. Hammarling and J. H. Wilkinson. The practical behaviour of linear iterative methods with particular reference to S.O.R. Report NAC 69, National Physical Laboratory, Teddington, UK, September 1976. 19 pp.   
[542] Sven Hammarling. A note on modifications to the Givens plane rotation. J. Inst. Maths. Applics., 13:215-218, 1974.   
[543] Sven J. Hammarling. The numerical solution of the general Gauss-Markov linear model. In Mathematics in Signal Processing, T. S. Durrani, J. B. Abbiss, and J. E. Hudson, editors, Oxford University Press, 1987, pages 451-456.   
[544] Rolf Hammer, Matthias Hocks, Ulrich Kulisch, and Dietmar Ratz. Numerical Toolbox for Verified Computing I. Basic Numerical Problems: Theory, Algorithms, and Pascal-XSC Programs. Springer-Verlag, Berlin, 1993. xiii+337 pp. ISBN 3-540-57118-3.   
[545] R. W. Hamming. Numerical Methods for Scientists and Engineers. Second edition, McGraw-Hill, New York, 1973. ix+721 pp. ISBN 0-07-025887-2.   
[546] Richard J. Hanson. Aasen's method for linear systems with self-adjoint matrices. Visual Numerics, Inc., http://www.vni.com/books/whitepapers/Aasen.html, July 1997.   
[547] G. H. Hardy. A Course of Pure Mathematics. Tenth edition, Cambridge University Press, 1967. xii+509 pp. ISBN 0-521-09227-2.   
[548] G. H. Hardy, J. E. Littlewood, and G. Pólya. Inequalities. Second edition, Cambridge University Press, 1952. xii+324 pp.

[549] Richard Harter. The optimality of Winograd's formula. Comm. ACM, 15(5):352, 1972.   
[550] D. J. Hartfiel. Concerning the solution set of $Ax = b$ where $P \leq A \leq Q$ and $p \leq b \leq q$ . Numer. Math., 35:355-359, 1980.   
[551] A Manual of Operation for the Automatic Sequence Controlled Calculator. Harvard University Press, Cambridge, MA, USA, 1946. Reprinted, with new foreword and introduction, Volume 8 in the Charles Babbage Institute Reprint Series for the History of Computing, MIT Press, Cambridge, MA, USA, 1985. xxxii+561 pp. ISBN 0-262-01084-4.   
[552] Proceedings of a Symposium on Large-Scale Digital Calculating Machinery, volume 16 of The Annals of the Computation Laboratory of Harvard University. Harvard University Press, Cambridge, MA, USA, 1948. Reprinted, with a new introduction by William Aspray, Volume 7 in the Charles Babbage Institute Reprint Series for the History of Computing, MIT Press, Cambridge, MA, USA, 1985. xxix+302 pp. ISBN 0-262-08152-0.   
[553] John R. Hauser. Handling floating-point exceptions in numeric programs. ACM Trans. Program. Lang. Syst., 18(2):139-174, 1996.   
[554] John Z. Hearon. Nonsingular solutions of $TA - BT = C$ . Linear Algebra Appl., 16:57-63, 1977.   
[555] M. T. Heath, G. A. Geist, and J. B. Drake. Early experience with the Intel iPSC/860 at Oak Ridge National Laboratory. Report ORNL/TM-11655, Oak Ridge National Laboratory, Oak Ridge, TN, USA, September 1990. 26 pp.   
[556] Michael T. Heath. Numerical methods for large sparse linear least squares problems. SIAM J. Sci. Statist. Comput., 5(3):497-513, 1984.   
[557] A. S. Hedayat, N. J. A. Sloane, and John Stufken. Orthogonal Arrays: Theory and Applications. Springer-Verlag, New York, 1999. xxiii+416 pp. ISBN 0-387-98766-5.   
[558] Piet Hein. *Grooks*. Number 85 in Borgens Pocketbooks. Second edition, Borgens Forlag, Copenhagen, Denmark, 1992. 53 pp. First published in 1966. ISBN 87-418-1079-1.   
[559] H. V. Henderson and S. R. Searle. On deriving the inverse of a sum of matrices. SIAM Rev., 23(1):53-60, 1981.   
[560] Harold V. Henderson, Friedrich Pukelsheim, and Shayle R. Searle. On the history of the Kronecker product. Linear and Multilinear Algebra, 14:113-120, 1983.   
[561] Harold V. Henderson and S. R. Searle. The vec-permutation matrix, the vec operator and Kronecker products: A review. Linear and Multilinear Algebra, 9: 271-288, 1981.   
[562] John L. Hennessy and David A. Patterson. Computer Architecture: A Quantitative Approach. Second edition, Morgan Kaufmann, San Francisco, CA, USA, 1996. xxiii+760+appendices pp. ISBN 1-55860-329-8.   
[563] Peter Henrici. Bounds for iterates, inverses, spectral variation and fields of values of non-normal matrices. Numer. Math., 4:24-40, 1962.   
[564] Peter Henrici. Discrete Variable Methods in Ordinary Differential Equations. John Wiley, New York, 1962. xi+407 pp.   
[565] Peter Henrici. Error Propagation for Difference Methods. John Wiley, New York, 1963. vi+73 pp.

[566] Peter Henrici. Elements of Numerical Analysis. Wiley, New York, 1964. xv+328 pp.   
[567] Peter Henrici. Test of probabilistic models for the propagation of roundoff errors. Comm. ACM, 9(6):409-410, 1966.   
[568] Peter Henrici. A model for the propagation of rounding error in floating arithmetic. In *Interval Mathematics* 1980, Karl L. E. Nickel, editor, Academic Press, New York, 1980, pages 49-73.   
[569] Gary Hewer and Charles Kenney. The sensitivity of the stable Lyapunov equation. SIAM J. Control Optim., 26(2):321-344, 1988.   
[570] HP-15C Advanced Functions Handbook. Hewlett-Packard, Portable Computer Division, Corvallis, OR, USA, 1982. 221 pp. Part number 00015-90011 Rev. C.   
[571] HP 48G Series User's Guide. Hewlett-Packard, Corvallis Division, Corvallis, OR, USA, 1993. Part number 00048-90126, Edition 3.   
[572] Yozo Hida, Xiaoye S. Li, and David H. Bailey. Algorithms for quad-double precision floating point arithmetic. In Proc. 15th IEEE Symposium on Computer Arithmetic, IEEE Computer Society Press, Los Alamitos, CA, USA, 2001, pages 155-162.   
[573] Desmond J. Higham. Condition numbers and their condition numbers. Linear Algebra Appl., 214:193-213, 1995.   
[574] Desmond J. Higham and Nicholas J. Higham. Backward error and condition of structured linear systems. SIAM J. Matrix Anal. Appl., 13(1):162-175, 1992.   
[575] Desmond J. Higham and Nicholas J. Higham. Componentwise perturbation theory for linear systems with multiple right-hand sides. Linear Algebra Appl., 174:111-129, 1992.   
[576] Desmond J. Higham and Nicholas J. Higham. MATLAB Guide. Society for Industrial and Applied Mathematics, Philadelphia, PA, USA, 2000. xxii+283 pp. ISBN 0-89871-516-4.   
[577] Desmond J. Higham and Lloyd N. Trefethen. Stiffness of ODEs. BIT, 33:285-303, 1993.   
[578] Nicholas J. Higham. Computing the polar decomposition—with applications. SIAM J. Sci. Statist. Comput., 7(4):1160-1174, 1986.   
[579] Nicholas J. Higham. Efficient algorithms for computing the condition number of a tridiagonal matrix. SIAM J. Sci. Statist. Comput., 7(1):150-165, 1986.   
[580] Nicholas J. Higham. Computing real square roots of a real matrix. Linear Algebra Appl., 88/89:405-430, 1987.   
[581] Nicholas J. Higham. Error analysis of the Björck-Pereyra algorithms for solving Vandermonde systems. Numer. Math., 50(5):613-632, 1987.   
[582] Nicholas J. Higham. A survey of condition number estimation for triangular matrices. SIAM Rev., 29(4):575-596, 1987.   
[583] Nicholas J. Higham. Computing a nearest symmetric positive semidefinite matrix. Linear Algebra Appl., 103:103-118, 1988.   
[584] Nicholas J. Higham. Fast solution of Vandermonde-like systems involving orthogonal polynomials. IMA J. Numer. Anal., 8:473-486, 1988.   
[585] Nicholas J. Higham. FORTRAN codes for estimating the one-norm of a real or complex matrix, with applications to condition estimation (Algorithm 674). ACM Trans. Math. Software, 14(4):381-396, 1988.

[586] Nicholas J. Higham. The accuracy of solutions to triangular systems. SIAM J. Numer. Anal., 26(5):1252-1265, 1989.   
[587] Nicholas J. Higham. Matrix nearness problems and applications. In Applications of Matrix Theory, M. J. C. Gover and S. Barnett, editors, Oxford University Press, 1989, pages 1-27.   
[588] Nicholas J. Higham. Analysis of the Cholesky decomposition of a semi-definite matrix. In Reliable Numerical Computation, M. G. Cox and S. J. Hammarling, editors, Oxford University Press, 1990, pages 161-185.   
[589] Nicholas J. Higham. Bounding the error in Gaussian elimination for tridiagonal systems. SIAM J. Matrix Anal. Appl., 11(4):521-530, 1990.   
[590] Nicholas J. Higham. Computing error bounds for regression problems. In Statistical Analysis of Measurement Error Models and Applications, Contemporary Mathematics 112, Philip J. Brown and Wayne A. Fuller, editors, American Mathematical Society, Providence, RI, USA, 1990, pages 195-208.   
[591] Nicholas J. Higham. Experience with a matrix norm estimator. SIAM J. Sci. Statist. Comput., 11(4):804-809, 1990.   
[592] Nicholas J. Higham. Exploiting fast matrix multiplication within the level 3 BLAS. ACM Trans. Math. Software, 16(4):352-368, 1990.   
[593] Nicholas J. Higham. How accurate is Gaussian elimination? In Numerical Analysis 1989, Proceedings of the 13th Dundee Conference, D. F. Griffiths and G. A. Watson, editors, volume 228 of Pitman Research Notes in Mathematics, Longman Scientific and Technical, Essex, UK, 1990, pages 137-154.   
[594] Nicholas J. Higham. Iterative refinement enhances the stability of $QR$ factorization methods for solving linear equations. Numerical Analysis Report No. 182, University of Manchester, Manchester, England, April 1990.   
[595] Nicholas J. Higham. Stability analysis of algorithms for solving confluent Vandermonde-like systems. SIAM J. Matrix Anal. Appl., 11(1):23-41, 1990.   
[596] Nicholas J. Higham. Iterative refinement enhances the stability of $QR$ factorization methods for solving linear equations. BIT, 31:447-468, 1991.   
[597] Nicholas J. Higham. Three measures of precision in floating point arithmetic. *NA Digest*, Volume 91, Issue 16, 1991. Electronic mail magazine: na.help@na-net. orn1.gov.   
[598] Nicholas J. Higham. Estimating the matrix $p$ -norm. Numer. Math., 62:539-555, 1992.   
[599] Nicholas J. Higham. Stability of a method for multiplying complex matrices with three real matrix multiplications. SIAM J. Matrix Anal. Appl., 13(3):681-687, 1992.   
[600] Nicholas J. Higham. The accuracy of floating point summation. SIAM J. Sci. Comput., 14(4):783-799, 1993.   
[601] Nicholas J. Higham. Optimization by direct search in matrix computations. SIAM J. Matrix Anal. Appl., 14(2):317-333, 1993.   
[602] Nicholas J. Higham. Perturbation theory and backward error for $AX - XB = C$ . BIT, 33:124-136, 1993.   
[603] Nicholas J. Higham. The matrix sign decomposition and its relation to the polar decomposition. Linear Algebra Appl., 212/213:3-20, 1994.

[604] Nicholas J. Higham. A survey of componentwise perturbation theory in numerical linear algebra. In Mathematics of Computation 1943-1993: A Half Century of Computational Mathematics, Walter Gautschi, editor, volume 48 of Proceedings of Symposia in Applied Mathematics, American Mathematical Society, Providence, RI, USA, 1994, pages 49-77.   
[605] Nicholas J. Higham. Stability of parallel triangular system solvers. SIAM J. Sci. Comput., 16(2):400-413, 1995.   
[606] Nicholas J. Higham. The Test Matrix Toolbox for MATLAB (version 3.0). Numerical Analysis Report No. 276, Manchester Centre for Computational Mathematics, Manchester, England, September 1995. 70 pp.   
[607] Nicholas J. Higham. Iterative refinement for linear systems and LAPACK. IMA J. Numer. Anal., 17(4):495-509, 1997.   
[608] Nicholas J. Higham. Stability of the diagonal pivoting method with partial pivoting. SIAM J. Matrix Anal. Appl., 18(1):52-65, 1997.   
[609] Nicholas J. Higham. Stable iterations for the matrix square root. Numerical Algorithms, 15(2):227-242, 1997.   
[610] Nicholas J. Higham. Factorizing complex symmetric matrices with positive definite real and imaginary parts. Math. Comp., 67(224):1591-1599, 1998.   
[611] Nicholas J. Higham. Handbook of Writing for the Mathematical Sciences. Second edition, Society for Industrial and Applied Mathematics, Philadelphia, PA, USA, 1998. xvi+302 pp. ISBN 0-89871-420-6.   
[612] Nicholas J. Higham. Notes on accuracy and stability of algorithms in numerical linear algebra. In The Graduate Student's Guide to Numerical Analysis '98, Mark Ainsworth, Jeremy Levesley, and Marco Marletta, editors, Springer-Verlag, Berlin, 1999, pages 48-82.   
[613] Nicholas J. Higham. Stability of block $\mathbf{LDL}^{\mathrm{T}}$ factorization of a symmetric tridiagonal matrix. Linear Algebra Appl., 287:181-189, 1999.   
[614] Nicholas J. Higham. QR factorization with complete pivoting and accurate computation of the SVD. Linear Algebra Appl., 309:153-174, 2000.   
[615] Nicholas J. Higham. Evaluating Padé approximants of the matrix logarithm. SIAM J. Matrix Anal. Appl., 22(4):1126-1135, 2001.   
[616] Nicholas J. Higham and Desmond J. Higham. Large growth factors in Gaussian elimination with pivoting. SIAM J. Matrix Anal. Appl., 10(2):155-164, 1989.   
[617] Nicholas J. Higham and Hyun-Min Kim. Numerical analysis of a quadratic matrix equation. IMA J. Numer. Anal., 20(4):499-519, 2000.   
[618] Nicholas J. Higham and Philip A. Knight. Componentwise error analysis for stationary iterative methods. In Linear Algebra, Markov Chains, and Queueing Models, Carl D. Meyer and Robert J. Plemmons, editors, volume 48 of IMA Volumes in Mathematics and Its Applications, Springer-Verlag, New York, 1993, pages 29-46.   
[619] Nicholas J. Higham and Philip A. Knight. Finite precision behavior of stationary iteration for solving singular systems. Linear Algebra Appl., 192:165-186, 1993.   
[620] Nicholas J. Higham and Philip A. Knight. Matrix powers in finite precision arithmetic. SIAM J. Matrix Anal. Appl., 16(2):343-358, 1995.   
[621] Nicholas J. Higham and Pythagoras Papadimitriou. A parallel algorithm for computing the polar decomposition. Parallel Comput., 20(8):1161-1173, 1994.

[622] Nicholas J. Higham and Alex Pothen. Stability of the partitioned inverse method for parallel solution of sparse triangular systems. SIAM J. Sci. Comput., 15(1): 139-148, 1994.   
[623] Nicholas J. Higham and G. W. Stewart. Numerical linear algebra in statistical computing. In The State of the Art in Numerical Analysis, A. Iserles and M. J. D. Powell, editors, Oxford University Press, 1987, pages 41-57.   
[624] Nicholas J. Higham and Françoise Tisseur. A block algorithm for matrix 1-norm estimation, with an application to 1-norm pseudospectra. SIAM J. Matrix Anal. Appl., 21(4):1185-1201, 2000.   
[625] Nicholas J. Higham and Françoise Tisseur. Bounds for eigenvalues of matrix polynomials. Numerical Analysis Report 371, Manchester Centre for Computational Mathematics, Manchester, England, January 2001. 16 pp. To appear in Linear Algebra Appl.   
[626] David Hilbert. Ein Beitrag zur Theorie des Legendre'schen Polynoms. Acta Mathematica, 18:155-159, 1894.   
[627] F. B. Hildebrand. Introduction to Numerical Analysis. Second edition, McGraw-Hill, New York, 1974. xiii+669 pp. Reprinted by Dover, New York, 1987. ISBN 0-486-65363-3.   
[628] Marlis Hochbruck and Gerhard Starke. Preconditioned Krylov subspace methods for Lyapunov matrix equations. SIAM J. Matrix Anal. Appl., 16(1):156-171, 1995.   
[629] R. W. Hockney and C. R. Jesshope. Parallel Computers 2: Architecture, Programming and Algorithms. Adam Hilger, Bristol, 1988. xv+625 pp. ISBN 0-85274-812-4.   
[630] A. ScottEdward Hodel. Recent applications of the Lyapunov equation in control theory. In Iterative Methods in Linear Algebra, R. Beauwens and P. de Groen, editors, Elsevier Science Publishers B.V. (North-Holland), Amsterdam, The Netherlands, 1992, pages 217-227.   
[631] Andrew Hodges. *Alan Turing: The Enigma*. Burnett Books, London, 1983. xix+586 pp. 1992 edition with preface, Vintage, London. ISBN 0-09-911641-3.   
[632] Christoph M. Hoffmann. The problems of accuracy and robustness in geometric computation. Computer, March:31-41, 1989.   
[633] W. Hoffmann. Solving linear systems on a vector computer. J. Comput. Appl. Math., 18:353-367, 1987.   
[634] W. Hoffmann. Iterative algorithms for Gram-Schmidt orthogonalization. Computing, 41:335-348, 1989.   
[635] R. C. Holt and J. R. Cordy. The Turing programming language. Comm. ACM, 31(12):1410-1423, 1988.   
[636] Roger A. Horn and Charles R. Johnson. Matrix Analysis. Cambridge University Press, 1985. xiii+561 pp. ISBN 0-521-30586-1.   
[637] Roger A. Horn and Charles R. Johnson. Topics in Matrix Analysis. Cambridge University Press, 1991. viii+607 pp. ISBN 0-521-30587-X.   
[638] Jim Horning. Note on program reliability. ACM SIGSOFT Software Engineering Notes, 4(4):6, 1979. Cited in [1159].   
[639] Harold Hotelling. Some new methods in matrix calculation. Ann. Math. Statist., 14(1):1-34, 1943.

[640] David Hough. Applications of the proposed IEEE 754 standard for floating-point arithmetic. Computer, 14:70-74, 1981.   
[641] David Hough. Random story. *NA Digest*, Volume 89, Issue 1, 1989.   
[642] Patricia D. Hough and Stephen A. Vavasis. Complete orthogonal decomposition for weighted least squares. SIAM J. Matrix Anal. Appl., 18(2):369-392, 1997.   
[643] Alston S. Householder. Unitary triangularization of a nonsymmetric matrix. J. Assoc. Comput. Mach., 5:339-342, 1958.   
[644] Alston S. Householder. The Theory of Matrices in Numerical Analysis. Blaisdell, New York, 1964. xi+257 pp. Reprinted by Dover, New York, 1975. ISBN 0-486-61781-5.   
[645] D. Y. Hu and L. Reichel. Krylov subspace methods for the Sylvester equation. Linear Algebra Appl., 172:283-313, 1992.   
[646] T. E. Hull. Correctness of numerical software. In Performance Evaluation of Numerical Software, Lloyd D. Fosdick, editor, North-Holland, Amsterdam, The Netherlands, 1979, pages 3-15.   
[647] T. E. Hull. Precision control, exception handling and a choice of numerical algorithms. In Numerical Analysis Proceedings, Dundee 1981, G. A. Watson, editor, volume 912 of Lecture Notes in Mathematics, Springer-Verlag, Berlin, 1982, pages 169-178.   
[648] T. E. Hull, A. Abraham, M. S. Cohen, A. F. X. Curley, C. B. Hall, D. A. Penny, and J. T. M. Sawchuk. Numerical TURING. ACM SIGNUM Newsletter, 20(3): 26-34, 1985.   
[649] T. E. Hull, Thomas F. Fairgrieve, and Ping Tak Peter Tang. Implementing complex elementary functions using exception handling. ACM Trans. Math. Software, 20(2):215-244, 1994.   
[650] T. E. Hull and J. R. Swenson. Tests of probabilistic models for propagation of roundoff errors. Comm. ACM, 9(2):108-113, 1966.   
[651] Julian Hunt. Rounding and other approximations for measurements, records and targets. Mathematics Today, 33:73-77, 1997.   
[652] M. A. Hyman. Eigenvalues and eigenvectors of general matrices. Presented at the 12th National Meeting of the Association for Computing Machinery, Houston, Texas, 1957. Cited in [1232].   
[653] IBM. Engineering and Scientific Subroutine Library, Guide and Reference, Release 3. Fourth Edition (Program Number 5668-863), 1988.   
[654] ISO/IEC 10967-1 (1994-12): Information Technology—Language Independent Arithmetic—Part 1: Integer and Floating Point Arithmetic. International Electrotechnical Commission, Geneva, Switzerland, 1994. 92 pp.   
[655] IEEE Standard for Binary Floating-Point Arithmetic, ANSI/IEEE Standard 754-1985. Institute of Electrical and Electronics Engineers, New York, 1985. Reprinted in SIGPLAN Notices, 22(2):9-25, 1987.   
[656] A Radix-Independent Standard for Floating-Point Arithmetic, IEEE Standard 854-1987. IEEE Computer Society, New York, 1987.   
[657] IEEE Computer Society Microprocessor Standards Committee, Floating-Point Working Group. A proposed standard for binary floating-point arithmetic, Draft 8.0 of IEEE Task P754 (with introductory comments by David Stevenson). Computer, 14:51-62, 1981.

[658] Yasuhiko Ikebe. On inverses of Hessenberg matrices. Linear Algebra Appl., 24: 93-97, 1979.   
[659] Khakim D. Ikramov. A remark on "A note on constructing a symmetric matrix with specified diagonal entries and eigenvalues". BIT, 38(4):807, 1998.   
[660] Khakim D. Ikramov and Andrey B. Kucherov. Bounding the growth factor in Gaussian elimination for Buckley's class of complex symmetric matrices. Numerical Linear Algebra with Applications, 7(5):269-274, 2000.   
[661] ILAS Education Committee. Report on graduate linear algebra courses. Manuscript from the International Linear Algebra Society, November 1993. http://gauss.technion.ac.il/iic/GRAD-ED.SYLLABI.4 pp.   
[662] Cray Research Inc. UNICOS Math and Scientific Library Reference Manual. Number SR-2081, Version 5.0, Eagan, MN, USA, 1989.   
[663] D. C. Ince, editor. Collected Works of A. M. Turing: Mechanical Intelligence. North-Holland, Amsterdam, The Netherlands, 1992. xix+227 pp. ISBN 0-444-88058-5.   
[664] F. Incertis. A faster method of computing matrix Pythagorean sums. IEEE Trans. Automat. Control, AC-30(3):273-275, 1985.   
[665] Ilse C. F. Ipsen and Carl D. Meyer. Uniform stability of Markov chains. SIAM J. Matrix Anal. Appl., 15(4):1061-1074, 1994.   
[666] Masao Iri. History of automatic differentiation and rounding error estimation. In Automatic Differentiation of Algorithms: Theory, Implementation, and Application, Andreas Griewank and George F. Corliss, editors, Society for Industrial and Applied Mathematics, Philadelphia, PA, USA, 1991, pages 3-16.   
[667] Eugene Isaacson and Herbert Bishop Keller. Analysis of Numerical Methods. Wiley, New York, 1966. xv+541 pp. Reprinted by Dover, New York, 1994. ISBN 0-486-68029-0.   
[668] William Jalby and Bernard Philippe. Stability analysis and improvement of the block Gram-Schmidt algorithm. SIAM J. Sci. Statist. Comput., 12(5):1058-1073, 1991.   
[669] Ho-Jong Jang. A constrained least-squares approach to the rapid reanalysis of structures. Linear Algebra Appl., 265:185-202, 1997.   
[670] M. Jankowski, A. Smoktunowicz, and H. Wozniakowski. A note on floating-point summation of very many terms. J. Information Processing and Cybernetics-EIK, 19(9):435-440, 1983.   
[671] M. Jankowski and H. Wozniakowski. Iterative refinement implies numerical stability. BIT, 17:303-311, 1977.   
[672] M. Jankowski and H. Wozniakowski. The accurate solution of certain continuous problems using only single precision arithmetic. BIT, 25:635-651, 1985.   
[673] Paul Jansen and Peter Weidner. High-accuracy arithmetic software—some tests of the ACRITH problem-solving routines. ACM Trans. Math. Software, 12(1): 62–70, 1986.   
[674] A. Jennings. Bounds for the singular values of a matrix. IMA J. Numer. Anal., 2:459-474, 1982.   
[675] L. S. Jennings and M. R. Osborne. A direct error analysis for least squares. Numer. Math., 22:325-332, 1974.

[676] Mark T. Jones and Merrell L. Patrick. Bunch-Kaufman factorization for real symmetric indefinite banded matrices. SIAM J. Matrix Anal. Appl., 14(2):553-559, 1993.   
[677] Mark T. Jones and Merrell L. Patrick. Factoring symmetric indefinite matrices on high-performance architectures. SIAM J. Matrix Anal. Appl., 15(1):273-283, 1994.   
[678] William B. Jones and W. J. Thron. Numerical stability in evaluating continued fractions. Math. Comp., 28(127):795-810, 1974.   
[679] T. L. Jordan. Experiments on error growth associated with some linear least-squares procedures. Math. Comp., 22:579-588, 1968.   
[680] George Gheverghese Joseph. The Crest of the Peacock: Non-European Roots of Mathematics. Penguin, London, 1991. xv+371 pp. ISBN 0-14-012529-9.   
[681] Bo Kågström. A perturbation analysis of the generalized Sylvester equation $(AR - LB, DR - LE) = (C, F)$ . SIAM J. Matrix Anal. Appl., 15(4):1045-1060, 1994.   
[682] Bo Kägström and Peter Poromaa. Distributed and shared memory block algorithms for the triangular Sylvester equation with $\text{sep}^{-1}$ estimators. SIAM J. Matrix Anal. Appl., 13(1):90-101, 1992.   
[683] Bo Kågström and Peter Poromaa. Computing eigenspaces with specified eigenvalues of a regular matrix pair $(A, B)$ and condition estimation: Theory, algorithms and software. Numerical Algorithms, 12:369-407, 1996.   
[684] Bo Kägström and Peter Poromaa. LAPACK-style algorithms and software for solving the generalized Sylvester equation and estimating the separation between regular matrix pairs. ACM Trans. Math. Software, 22(1):78-103, 1996.   
[685] Bo Kägström and Lars Westin. Generalized Schur methods with condition estimators for solving the generalized Sylvester equation. IEEE Trans. Automat. Control, AC-34(7):745-751, 1989.   
[686] W. Kahan. Further remarks on reducing truncation errors. Comm. ACM, 8(1): 40, 1965.   
[687] W. Kahan. Numerical linear algebra. Canadian Math. Bulletin, 9:757-801, 1966.   
[688] W. Kahan. A survey of error analysis. In Proc. IFIP Congress, Ljubljana, Information Processing 71, North-Holland, Amsterdam, The Netherlands, 1972, pages 1214-1239.   
[689] W. Kahan. Implementation of algorithms (lecture notes by W. S. Haugeland and D. Hough). Technical Report 20, Department of Computer Science, University of California, Berkeley, CA, USA, 1973.   
[690] W. Kahan. Interval arithmetic options in the proposed IEEE floating point arithmetic standard. In *Interval Mathematics* 1980, Karl L. E. Nickel, editor, Academic Press, New York, 1980, pages 99-128.   
[691] W. Kahan. Why do we need a floating-point arithmetic standard? Technical report, University of California, Berkeley, CA, USA, February 1981. 41 pp.   
[692] W. Kahan. Mathematics written in sand—the HP-15C, Intel 8087, etc. In Statistical Computing Section, Proceedings of the American Statistical Association, Toronto, 1983, pages 12–26.   
[693] W. Kahan. To solve a real cubic equation. Technical Report PAM-352, Center for Pure and Applied Mathematics, University of California, Berkeley, CA, USA, November 1986. 20 pp.

[694] W. Kahan. Branch cuts for complex elementary functions or much ado about nothing's sign bit. In The State of the Art in Numerical Analysis, A. Iserles and M. J. D. Powell, editors, Oxford University Press, 1987, pages 165-211.   
[695] W. Kahan. Doubled-precision IEEE standard 754 floating-point arithmetic. Manuscript, February 1987.   
[696] W. Kahan. How Cray's arithmetic hurts scientific computation (and what might be done about it). Manuscript prepared for the Cray User Group meeting in Toronto, June 1990. 42 pp.   
[697] W. Kahan. Analysis and refutation of the LCAS. ACM SIGNUM Newsletter, 26 (3):2-15, 1991.   
[698] W. Kahan. Computer benchmarks versus accuracy. Draft manuscript, June 1994.   
[699] W. Kahan. The improbability of probabilistic error analyses for numerical computations. Manuscript, March 1996. 34 pp.   
[700] W. Kahan. Lecture notes on the status of IEEE Standard 754 for binary floating-point arithmetic. Manuscript, May 1996. 30 pp.   
[701] W. Kahan. Miscalculating area and angles of a needle-like triangle. Manuscript, July 1997. 20 pp.   
[702] W. Kahan. What has the volume of a tetrahedron to do with computer programming languages? Manuscript, April 2001. 31 pp.   
[703] W. Kahan and I. Farkas. Algorithm 168: Newton interpolation with backward divided differences. Comm. ACM, 6(4):165, 1963.   
[704] W. Kahan and I. Farkas. Algorithm 169: Newton interpolation with forward divided differences. Comm. ACM, 6(4):165, 1963.   
[705] W. Kahan and E. LeBlanc. Anomalies in the IBM ACRITH package. In Proceedings of the 7th Symposium on Computer Arithmetic, Kai Hwang, editor, IEEE Computer Society Press, Silver Spring, MD, USA, 1985, pages 322-331.   
[706] W. Kahan and J. Palmer. On a proposed floating-point standard. ACM SIGNUM Newsletter, 14:13-21, 1979.   
[707] David K. Kahaner, Cleve B. Moler, and Stephen G. Nash. Numerical Methods and Software. Prentice-Hall, Englewood Cliffs, NJ, USA, 1989. xii+495 pp. ISBN 0-13-627258-4.   
[708] Ming-Yang Kao and Jie Wang. Linear-time approximation algorithms for computing numerical summation with provably small errors. SIAM J. Comput., 29 (5):1568-1576, 2000.   
[709] Igor Kaporin. A practical algorithm for faster matrix multiplication. Numerical Linear Algebra with Applications, 6:687-700, 1999.   
[710] Ilkka Karasalo. A criterion for truncation of the QR-decomposition algorithm for the singular linear least squares problem. BIT, 14:156-166, 1974.   
[711] A. Karatsuba and Yu. Ofman. Multiplication of multidigit numbers on automata. Soviet Physics—Doklady, 7(7):595-596, 1963.   
[712] Samuel Karlin. Total Positivity, volume 1. Stanford University Press, Stanford, CA, USA, 1968.   
[713] Rune Karlson and Bertil Waldén. Estimation of optimal backward perturbation bounds for the linear least squares problem. BIT, 37(4):862-869, 1997.

[714] Alan H. Karp and Peter Markstein. High-precision division and square root. ACM Trans. Math. Software, 23(4):561-589, 1997.   
[715] Richard Karpinski. Paranoia: A floating-point benchmark. BYTE, 10(2):223-235, 1985.   
[716] Tosio Kato. *Perturbation Theory for Linear Operators*. Second edition, Springer-Verlag, Berlin, 1976. xx+619 pp. ISBN 3-540-97588-5.   
[717] Linda Kaufman. Matrix methods for queuing problems. SIAM J. Sci. Statist. Comput., 4(3):525-552, 1983.   
[718] R. Baker Kearfott. Algorithm 763: INTERVAL_ARITHMETIC: A Fortran 90 module for an interval data type. ACM Trans. Math. Software, 22(4):385-392, 1996.   
[719] R. Baker Kearfott. Interval computations: Introduction, uses, and resources. Euromath Bulletin, 2(1):95-112, 1996. http://interval.louisiana.edu/preprints.html.   
[720] Herbert B. Keller. On the solution of singular and semidefinite linear systems by iteration. SIAM J. Numer. Anal., 2(2):281-290, 1965.   
[721] C. T. Kelley. Iterative Methods for Linear and Nonlinear Equations. Society for Industrial and Applied Mathematics, Philadelphia, PA, USA, 1995. xiii+165 pp. ISBN 0-89871-352-8.   
[722] C. T. Kelley. Iterative Methods for Optimization. Society for Industrial and Applied Mathematics, Philadelphia, PA, USA, 1999. xv+180 pp. ISBN 0-89871-433-8.   
[723] William J. Kennedy, Jr. and James E. Gentle. Statistical Computing. Marcel Dekker, New York, 1980. xi+591 pp. ISBN 0-8247-6898-1.   
[724] Charles Kenney and Gary Hewer. The sensitivity of the algebraic and differential Riccati equations. SIAM J. Control Optim., 28(1):50-69, 1990.   
[725] Charles Kenney and Alan J. Laub. Controllability and stability radii for companion form systems. Math. Control Signals Systems, 1:239-256, 1988.   
[726] Charles Kenney, Alan J. Laub, and M. S. Reese. Statistical condition estimation for linear least squares. SIAM J. Matrix Anal. Appl., 19(4):906-923, 1998.   
[727] Charles Kenney, Alan J. Laub, and M. S. Reese. Statistical condition estimation for linear systems. SIAM J. Sci. Comput., 19(2):566-583, 1998.   
[728] Charles S. Kenney and Alan J. Laub. Small-sample statistical condition estimates for general matrix functions. SIAM J. Sci. Comput., 15(1):36-61, 1994.   
[729] Charles S. Kenney, Alan J. Laub, and Philip M. Papadopoulos. Matrix-sign algorithms for Riccati equations. IMA J. Math. Control Inform., 9:331-344, 1992.   
[730] Thomas H. Kerr. Fallacies in computational testing of matrix positive definiteness/semidefiniteness. IEEE Trans. Aerospace and Electronic Systems, 26(2):415-421, 1990.   
[731] Andrzej Kielbasiński. Summation algorithm with corrections and some of its applications. Math. Stos., 1:22-41, 1973. (In Polish, cited in [670] and [672].)   
[732] Andrzej Kielbasinski. Iterative refinement for linear systems in variable-precision arithmetic. BIT, 21:97-103, 1981.   
[733] Andrzej Kielbasiński. A note on rounding-error analysis of Cholesky factorization. Linear Algebra Appl., 88/89:487-494, 1987.

[734] Andrzej Kielbasiński and Hubert Schwetlick. Numerische Lineare Algebra: Eine Computerorientierte Einführung. VEB Deutscher, Berlin, 1988. 472 pp. ISBN 3-87144-999-7.   
[735] Andrzej Kielbasiński and Hubert Schwetlick. Numeryczna Algebra Liniowa: Wprowadzenie do Obliczenia Zautomatyzowanych. Wydawnictwa Naukowo-Techniczne, Warszawa, 1992. 502 pp. ISBN 83-204-1260-9.   
[736] Fuad Kittaneh. Singular values of companion matrices and bounds on zeros of polynomials. SIAM J. Matrix Anal. Appl., 16(1):333-340, 1995.   
[737] R. Klatte, U. W. Kulisch, C. Lawo, M. Rauch, and A. Wiethoff. C-XSC: A $C++$ Class Library for Extended Scientific Computing. Springer-Verlag, Berlin, 1993. ISBN 0-387-56328-8.   
[738] R. Klatte, U. W. Kulisch, M. Neaga, D. Ratz, and Ch. Ullrich. PASCAL-XSC—Language Reference with Examples. Springer-Verlag, Berlin, 1992.   
[739] Philip A. Knight. Error Analysis of Stationary Iteration and Associated Problems. PhD thesis, University of Manchester, Manchester, England, September 1993. 135 pp.   
[740] Philip A. Knight. Fast rectangular matrix multiplication and $QR$ decomposition. Linear Algebra Appl., 221:69-81, 1995.   
[741] Donald E. Knuth. Evaluation of polynomials by computer. Comm. ACM, 5(12): 595-599, 1962.   
[742] Donald E. Knuth. Two notes on notation. Amer. Math. Monthly, 99(5):403-422, 1992.   
[743] Donald E. Knuth. The Art of Computer Programming, Volume 1, Fundamental Algorithms. Third edition, Addison-Wesley, Reading, MA, USA, 1997. xix+650 pp. ISBN 0-201-89683-4.   
[744] Donald E. Knuth. The Art of Computer Programming, Volume 2, Seminumerical Algorithms. Third edition, Addison-Wesley, Reading, MA, USA, 1998. xiii+762 pp. ISBN 0-201-89684-2.   
[745] Donald E. Knuth. Digital Typography. CSLI Lecture Notes Number 78. Center for the Study of Language and Information, Stanford University, Stanford, CA, USA, 1999. xv+685 pp. ISBN 0-57586-010-4.   
[746] T. W. Körner. Fourier Analysis. Cambridge University Press, Cambridge, UK, 1988. xii+591 pp. ISBN 0-521-38991-7.   
[747] Przemyslaw Kosowski and Alicja Smoktunowicz. On constructing unit triangular matrices with prescribed singular values. Computing, 64:279-285, 2000.   
[748] Eric Kostlan. On the spectra of Gaussian matrices. Linear Algebra Appl., 162-164: 385-388, 1992.   
[749] Z. V. Kovarik. Compatibility of approximate solutions of inaccurate linear equations. Linear Algebra Appl., 15:217-225, 1976.   
[750] Antoni Kreczmar. On memory requirements of Strassen's algorithms. volume 45 of Lecture Notes in Computer Science, Springer-Verlag, Berlin, 1976, pages 404-407.   
[751] Shankar Krishnan, Mark Foskey, Tim Culver, John Keyser, and Dinesh Manocha. PRECISE: Efficient multiprecision evaluation of algebraic roots and predicates for reliable geometric computation. In Proc. ACM Symposium on Computational Geometry, David Eppstein, Dan Halperin, and Dinesh Manocha, editors, ACM Press, 2001, pages 274-283.

[752] Koichi Kubota. PADRE2, a Fortran precompiler yielding error estimates and second derivatives. In Automatic Differentiation of Algorithms: Theory, Implementation, and Application, Andreas Griewank and George F. Corliss, editors, Society for Industrial and Applied Mathematics, Philadelphia, PA, USA, 1991, pages 251-262.   
[753] J. Kuczyński and H. Wozniakowski. Estimating the largest eigenvalue by the power and Lanczos algorithms with a random start. SIAM J. Matrix Anal. Appl., 13(4):1094-1122, 1992.   
[754] H. Kuki and W. J. Cody. A statistical study of the accuracy of floating point number systems. Comm. ACM, 16(4):223-230, 1973.   
[755] Ulrich W. Kulisch and Willard L. Miranker. Computer Arithmetic in Theory and in Practice. Academic Press, New York, 1981. xiii+249 pp. ISBN 0-12-428650-X.   
[756] Ulrich W. Kulisch and Willard L. Miranker, editors. A New Approach to Scientific Computation. Academic Press, New York, 1983. xv+384 pp. ISBN 0-12-428660-7.   
[757] Ulrich W. Kulisch and Willard L. Miranker. The arithmetic of the digital computer: A new approach. SIAM Rev., 28(1):1-40, 1986.   
[758] I. B. Kuperman. Approximate Linear Algebraic Equations. Van Nostrand Reinhold, London, 1971. xi+225 pp. ISBN 0-442-04546-8.   
[759] M. La Porte and J. Vignes. Etude statistique des erreurs dans l'arithmetique des ordinateurs; application au contrôle des résultats d'algebrees numériques. Numer. Math., 23:63-72, 1974.   
[760] J. D. Laderman. A noncommutative algorithm for multiplying $3 \times 3$ matrices using 23 multiplications. Bull. Amer. Math. Soc., 82(1):126-128, 1976.   
[761] Julian Laderman, Victor Pan, and Xuan-He Sha. On practical algorithms for accelerated matrix multiplication. Linear Algebra Appl., 162-164:557-588, 1992.   
[762] Jeffrey C. Lagarias, James A. Reeds, Margaret H. Wright, and Paul E. Wright. Convergence properties of the Nelder-Mead simplex method in low dimensions. SIAM J. Optim., 9(1):112-147, 1998.   
[763] Peter Lancaster. Error analysis for the Newton-Raphson method. Numer. Math., 9:55-68, 1966.   
[764] Peter Lancaster. Explicit solutions of linear matrix equations. SIAM Rev., 12(4): 544-566, 1970.   
[765] Cornelius Lanczos. Applied Analysis. Prentice-Hall, Englewood Cliffs, NJ, USA, 1956. xx+539 pp. Reprinted by Dover, New York, 1988. ISBN 0-486-65656-X.   
[766] Philippe Langlois. Automatic linear correction of rounding errors. BIT, 41(3): 515-539, 2001.   
[767] John L. Larson, Mary E. Pasternak, and John A. Wisniewski. Algorithm 594: Software for relative error analysis. ACM Trans. Math. Software, 9(1):125-130, 1983.   
[768] John L. Larson and Ahmed H. Sameh. Efficient calculation of the effects of roundoff errors. ACM Trans. Math. Software, 4(3):228-236, 1978. Errata 5(3):372, 1979.   
[769] John L. Larson and Ahmed H. Sameh. Algorithms for roundoff error analysis—A relative error approach. Computing, 24:275-297, 1980.   
[770] Lajos László. An attainable lower bound for the best normal approximation. SIAM J. Matrix Anal. Appl., 15(3):1035-1043, 1994.

[771] Alan J. Laub. A Schur method for solving algebraic Riccati equations. IEEE Trans. Automat. Control, AC-24(6):913-921, 1979.   
[772] Peter Läuchli. Jordan-Elimination und Ausgleichung nach kleinsten Quadraten. Numer. Math., 3:226-240, 1961.   
[773] Simon Lavington. Early British Computers: The Story of Vintage Computers and the People Who Built Them. Manchester University Press, 1980. 139 pp. ISBN 0-7190-0803-4.   
[774] C. L. Lawson, R. J. Hanson, D. R. Kincaid, and F. T. Krogh. Basic linear algebra subprograms for Fortran usage. ACM Trans. Math. Software, 5(3):308-323, 1979.   
[775] Charles L. Lawson and Richard J. Hanson. Solving Least Squares Problems. Society for Industrial and Applied Mathematics, Philadelphia, PA, USA, 1995. xii+337 pp. Revised republication of work first published in 1974 by Prentice-Hall. ISBN 0-89871-356-0.   
[776] Lam Lay-Yong and Shen Kangshen. Methods of solving linear equations in traditional China. Historia Mathematica, 16(2):107-122, 1989.   
[777] Vincent Lefèvre and Jean-Michel Muller. Worst cases for correct rounding of the elementary functions in double precision. In Proc. 15th IEEE Symposium on Computer Arithmetic, IEEE Computer Society Press, Los Alamitos, CA, USA, 2001.   
[778] Vincent Lefevre, Jean-Michel Muller, and Arnaud Tisserand. Toward correctly rounded transcendentals. IEEE Trans. Comput., 47(11):1235-1243, 1998.   
[779] D. H. Lehmer. Tables to many places of decimals. Mathematical Tables and Other Aids to Computation, 1(1):30-31, 1943.   
[780] R. B. Lehoucq. The computation of elementary unitary matrices. ACM Trans. Math. Software, 22(4):393-400, 1996.   
[781] Frans Lemeire. Bounds for condition numbers of triangular and trapezoid matrices. BIT, 15:58-64, 1975.   
[782] H. Leuprecht and W. Oberaigner. Parallel algorithms for the rounding exact summation of floating point numbers. Computing, 28:89-104, 1982.   
[783] Robert Michael Lewis, Virginia J. Torczon, and Michael W. Trossett. Direct search methods: Then and now. J. Comput. Appl. Math., 124:191-207, 2000.   
[784] T. Y. Li and Zhonggang Zeng. Homotopy-determinant algorithm for solving nonsymmetric eigenvalue problems. Math. Comp., 59(200):483-502, 1992.   
[785] X. S. Li, J. W. Demmel, D. H. Bailey, G. Henry, Y. Hida, J. Iskandar, W. Kahan, A. Kapur, M. C. Martin, T. Tung, and D. J. Yoo. Design, implementation and testing of Extended and Mixed Precision BLAS. Technical Report CS-00-451, Department of Computer Science, University of Tennessee, Knoxville, TN, USA, October 2000. 61 pp. LAPACK Working Note 149.   
[786] Xiaoye S. Li and James W. Demmel. Making sparse Gaussian elimination scalable by static pivoting. In Proceedings of SC98: High Performance Networking and Computing Conference, Orlando, Florida, 1998. CD ROM.   
[787] Thomas Lickteig. The computational complexity of division in quadratic extension fields. SIAM J. Comput., 16(2):278-311, 1987.   
[788] Seppo Linnainmaa. Analysis of some known methods of improving the accuracy of floating-point sums. BIT, 14:167-202, 1974.

[789] Seppo Linnainmaa. Towards accurate statistical estimation of rounding errors in floating-point computations. BIT, 15:165-173, 1975.   
[790] Seppo Linnainmaa. Taylor expansion of the accumulated rounding error. BIT, 16:146-160, 1976.   
[791] Seppo Linnainmaa. Software for doubled-precision floating-point computations. ACM Trans. Math. Software, 7(3):272-283, 1981.   
[792] Peter Linz. Accurate floating-point summation. Comm. ACM, 13(6):361-362, 1970.   
[793] Elliot Linzer. On the stability of transform-based circular deconvolution. SIAM J. Numer. Anal., 29(5):1482-1492, 1992.   
[794] Joseph W. H. Liu. A partial pivoting strategy for sparse symmetric matrix decomposition. ACM Trans. Math. Software, 13(2):173-182, 1987.   
[795] Georghios Loizou. Nonnormality and Jordan condition numbers of matrices. J. Assoc. Comput. Mach., 16(4):580-584, 1969.   
[796] J. W. Longley. An appraisal of least squares programs for the electronic computer from the point of view of the user. J. Amer. Statist. Assoc., 62:819-841, 1967.   
[797] Hao Lu. Fast solution of confluent Vandermonde linear systems. SIAM J. Matrix Anal. Appl., 15(4):1277-1289, 1994.   
[798] Hao Lu. Fast algorithms for confluent Vandermonde linear systems and generalized Trummer's problem. SIAM J. Matrix Anal. Appl., 16(2):655-674, 1995.   
[799] Hao Lu. Solution of Vandermonde-like systems and confluent Vandermonde-like systems. SIAM J. Matrix Anal. Appl., 17(1):127-138, 1996.   
[800] J. N. Lyness and J. J. Kaganove. Comments on the nature of automatic quadrature routines. ACM Trans. Math. Software, 2(1):65-81, 1976.   
[801] J. N. Lyness and C. B. Moler. Van der Monde systems and numerical differentiation. Numer. Math., 8:458-464, 1966.   
[802] M. Stuart Lynn. On the round-off error in the method of successive over-relaxation. Math. Comp., 18(85):36-49, 1964.   
[803] Allan J. Macleod. Some statistics on Gaussian elimination with partial pivoting. ACM SIGNUM Newsletter, 24(2/3):10-14, 1989.   
[804] Jan R. Magnus and Heinz Neudecker. The commutation matrix: Some properties and applications. Ann. Statist., 7(2):381-394, 1979.   
[805] Jan R. Magnus and Heinz Neudecker. Matrix Differential Calculus with Applications in Statistics and Econometrics. Revised edition, Wiley, Chichester, UK, 1999. xviii+395 pp. ISBN 0-471-98633-X.   
[806] J. H. Mainndon. Statistical Computation. Wiley, New York, 1984. xviii+370 pp. ISBN 0-471-86452-8.   
[807] John Makhoul. Toeplitz determinants and positive semidefiniteness. IEEE Trans. Signal Processing, 39(3):743-746, 1991.   
[808] Michael A. Malcolm. On accurate floating-point summation. Comm. ACM, 14 (11):731-736, 1971.   
[809] Michael A. Malcolm. Algorithms to reveal properties of floating-point arithmetic. Comm. ACM, 15(11):949-951, 1972.   
[810] Michael A. Malcolm and John Palmer. A fast method for solving a class of tridiagonal linear systems. Comm. ACM, 17(1):14-17, 1974.

[811] Alexander N. Malyshev. A note on the stability of Gauss-Jordan elimination for diagonally dominant matrices. Computing, 65(3):281-284, 2000.   
[812] Alexander N. Malyshev. Optimal backward perturbation bounds for the LSS problem. BIT, 41(2):430-432, 2001.   
[813] Alexander N. Malyshev and Miloud Sadkane. Computation of optimal backward perturbation bounds for large sparse linear least squares problems. BIT, 41(4): 739-747, 2002.   
[814] Thomas A. Manteuffel. An interval analysis approach to rank determination in linear least squares problems. SIAM J. Sci. Statist. Comput., 2(3):335-348, 1981.   
[815] Maple. Waterloo Maple Inc., Waterloo, Ontario, Canada. http://www.maplesoft.com.   
[816] John Markoff. Circuit flaw causes Pentium chip to miscalcate, Intel admits. New York Times, 1994. 24 November.   
[817] R. S. Martin, G. Peters, and J. H. Wilkinson. Iterative refinement of the solution of a positive definite system of equations. Numer. Math., 8:203-216, 1966. Also in [1246, pp. 31-44], Contribution I/2.   
[818] Mathematica. Wolfram Research, Inc., Champaign, IL, USA. http://www.wolfram.com.   
[819] Gleanings far and near. Mathematical Gazette, 22(170):95, 1924.   
[820] Roy Mathias. Matrices with positive definite Hermitian part: Inequalities and linear systems. SIAM J. Matrix Anal. Appl., 13(2):640-654, 1992.   
[821] Roy Mathias. Accurate eigensystem computations by Jacobi methods. SIAM J. Matrix Anal. Appl., 16(3):977-1003, 1995.   
[822] Roy Mathias. The instability of parallel prefix matrix multiplication. SIAM J. Sci. Comput., 16(4):956-973, 1995.   
[823] Roy Mathias. Analysis of algorithms for orthogonalizing products of unitary matrices. Numerical Linear Algebra with Applications, 3(2):125-145, 1996.   
[824] MATLAB. The MathWorks, Inc., Natick, MA, USA. http://www.mathworks.com.   
[825] Symbolic Math Toolbox Version 2: User's Guide. The MathWorks, Inc., Natick, MA, USA. Online version.   
[826] Shouichi Matsui and Masao Iri. An overflow/underflow-free floating-point representation of numbers. J. Information Processing, 4(3):123-133, 1981.   
[827] R. M. M. Mattheij. Stability of block LU-decompositions of matrices arising from BVP. SIAM J. Alg. Discrete Methods, 5(3):314-331, 1984.   
[828] R. M. M. Matthaeij. The stability of LU-decompositions of block tridiagonal matrices. Bull. Austral. Math. Soc., 29:177-205, 1984.   
[829] David W. Matula. In-and-out conversions. Comm. ACM, 11(1):47-50, 1968.   
[830] David W. Matula. A formalization of floating-point numeric base conversion. IEEE Trans. Comput., C-19(8):681-692, 1970.   
[831] David W. Matula and Peter Kornerup. Finite precision rational arithmetic:Slash number systems. IEEE Trans. Comput., C-34(1):3-18, 1985.   
[832] Charles McCarthy and Gilbert Strang. Optimal conditioning of matrices. SIAM J. Numer. Anal., 10(2):370-388, 1974.

[833] Daniel D. McCracken and William S. Dorn. Numerical Methods and Fortran Programming: With Applications in Science and Engineering. Wiley, New York, 1964. xii+457 pp.   
[834] P. McCullagh and J. A. Nelder. Generalized Linear Models. Second edition, Chapman and Hall, London, 1989. xix+511 pp. ISBN 0-412-31760-5.   
[835] B. D. McCullough and H. D. Vinod. The numerical reliability of econometric software. Journal of Economic Literature, 37:633-665, 1999.   
[836] William Marshall McKeeman. Algorithm 135: Crout with equilibration and iteration. Comm. ACM, 5:553-555, 1962.   
[837] K. I. M. McKinnon. Convergence of the Nelder-Mead simplex method to a nonstationary point. SIAM J. Optim., 9(1):148-158, 1998.   
[838] J. L. Mead, R. E. Renaut, and B. D. Welfert. Stability of a pivoting strategy for parallel Gaussian elimination. BIT, 41(3):633-639, 2001.   
[839] Jean Meinguet. On the estimation of significance. In Topics in Interval Analysis, Elden Hansen, editor, Oxford University Press, 1969, pages 47-64.   
[840] Jean Meinguet. Refined error analyses of Cholesky factorization. SIAM J. Numer. Anal., 20(6):1243-1250, 1983.   
[841] N. S. Mendelsohn. Some elementary properties of ill conditioned matrices and linear equations. Amer. Math. Monthly, 63(5):285-295, 1956.   
[842] Jorma Kaarlo Merikoski, Uoti Arpala, Ari Virtanen, Tin-Yau Tam, and Frank Uhlig. A best upper bound for the 2-norm condition number of a matrix. Linear Algebra Appl., 254:355-365, 1997.   
[843] Michael Metcalf and John K. Reid. Fortran 90/95 Explained. Second edition, Oxford University Press, 1999. 358 pp. ISBN 0-19-850558-2.   
[844] N. Metropolis. Methods of significance arithmetic. In The State of the Art in Numerical Analysis, David A. H. Jacobs, editor, Academic Press, London, 1977, pages 179-192.   
[845] Gérard Meurant. A review on the inverse of symmetric tridiagonal and block tridiagonal matrices. SIAM J. Matrix Anal. Appl., 13(3):707-728, 1992.   
[846] Carl D. Meyer, Jr. and R. J. Plemmons. Convergent powers of a matrix with applications to iterative methods for singular linear systems. SIAM J. Numer. Anal., 14(4):699-705, 1977.   
[847] H. I. Meyer and B. J. Hollingsworth. A method of inverting large matrices of special form. M.T.A.C., 11:94-97, 1957.   
[848] Victor J. Milenkovic. Verifiable implementations of geometric algorithms using finite precision arithmetic. Artificial Intelligence, 37:377-401, 1988.   
[849] D. F. Miller. The iterative solution of the matrix equation $X A + B X + C = 0$ . Linear Algebra Appl., 105:131-137, 1988.   
[850] Webb Miller. Computational complexity and numerical stability. SIAM J. Comput., 4(2):97-107, 1975.   
[851] Webb Miller. Software for roundoff analysis. ACM Trans. Math. Software, 1(2): 108-128, 1975.   
[852] Webb Miller. Graph transformations for roundoff analysis. SIAM J. Comput., 5 (2):204-216, 1976.

[853] Webb Miller. The Engineering of Numerical Software. Prentice-Hall, Englewood Cliffs, NJ, USA, 1984. viii+167 pp. ISBN 0-13-279043-2.   
[854] Webb Miller and David Spooner. Software for roundoff analysis, II. ACM Trans. Math. Software, 4(4):369-387, 1978.   
[855] Webb Miller and David Spooner. Algorithm 532: Software for roundoff analysis. ACM Trans. Math. Software, 4(4):388-390, 1978.   
[856] Webb Miller and Celia Wrathall. Software for Roundoff Analysis of Matrix Algorithms. Academic Press, New York, 1980. x+151 pp. ISBN 0-12-497250-0.   
[857] L. Mirsky. An Introduction to Linear Algebra. Oxford University Press, 1961. viii+440 pp. Reprinted by Dover, New York, 1990. ISBN 0-486-66434-1.   
[858] Herbert F. Mitchell, Jr. Inversion of a matrix of order 38. M.T.A.C., 3:161-166, 1948.   
[859] Cleve B. Moler. Iterative refinement in floating point. J. Assoc. Comput. Mach., 14(2):316-321, 1967.   
[860] Cleve B. Moler. Matrix computations with Fortran and paging. Comm. ACM, 15 (4):268-270, 1972.   
[861] Cleve B. Moler. Algorithm 423: Linear equation solver. Comm. ACM, 15(4):274, 1972.   
[862] Cleve B. Moler. Cramer's rule on 2-by-2 systems. ACM SIGNUM Newsletter, 9 (4):13-14, 1974.   
[863] Cleve B. Moler. Three research problems in numerical linear algebra. In Numerical Analysis, G. H. Golub and J. Oliger, editors, volume 22 of Proceedings of Symposia in Applied Mathematics, American Mathematical Society, Providence, RI, USA, 1978, pages 1-18.   
[864] Cleve B. Moler. Cleve's corner: The world's simplest impossible problem. The Math Works Newsletter, 4(2):6-7, 1990.   
[865] Cleve B. Moler. Technical note: Double-rounding and implications for numeric computations. The MathWorks Newsletter, 4:6, 1990.   
[866] Cleve B. Moler. A tale of two numbers. SIAM News, 28:1,16, 1995. Also in MATLAB News and Notes, Winter 1995, 10-12.   
[867] Cleve B. Moler and Donald Morrison. Replacing square roots by Pythagorean sums. IBM J. Res. Develop., 27(6):577-581, 1983.   
[868] Cleve B. Moler and Charles F. Van Loan. Nineteen dubious ways to compute the exponential of a matrix. SIAM Rev., 20(4):801-836, 1978.   
[869] Ole Møller. Note on quasi double-precision. BIT, 5:251-255, 1965.   
[870] Ole Møller. Quasi double-precision in floating point addition. BIT, 5:37-50, 1965. See also [869] for remarks on this article.   
[871] J. Strother Moore, Thomas W. Lynch, and Matt Kaufmann. A mechanically checked proof of the AMD5 $_K$ 86 floating-point division program. IEEE Trans. Comput., 47(9):913-926, 1998.   
[872] Ramon E. Moore. Interval Analysis. Prentice-Hall, Englewood Cliffs, NJ, USA, 1966. xi+145 pp.   
[873] Ramon E. Moore. Methods and Applications of Interval Analysis. Society for Industrial and Applied Mathematics, Philadelphia, PA, USA, 1979. xi+190 pp. ISBN 0-89871-161-4.

[874] Robb J. Muirhead. Aspects of Multivariate Statistical Theory. Wiley, New York, 1982. xix+673 pp. ISBN 0-471-09442-0.   
[875] Jean-Michel Muller. Arithmetique des Ordinateurs. Masson, Paris, 1989. 214 pp. In French. Cited in [442]. ISBN 2-225-81689-1.   
[876] Jean-Michel Muller. Elementary Functions: Algorithms and Implementation. Birkhäuser, Boston, MA, USA, 1997. xv+204 pp. ISBN 0-8176-3990-X.   
[877] K. H. Müller. Rounding error analysis of Horner's scheme. Computing, 30:285-303, 1983.   
[878] FPV: A floating-point validation package. Release I. User's guide. Technical Report NP 1201, NAG Ltd., Oxford, May 1986.   
[879] M. Zuhair Nashed and L. B. Rall. Annotated bibliography on generalized inverses and applications. In Generalized Inverses and Applications, M. Zuhair Nashed, editor, Academic Press, New York, 1976, pages 771-1041.   
[880] Larry Neal and George Poole. A geometric analysis of Gaussian elimination. II. Linear Algebra Appl., 173:239-264, 1992.   
[881] J. A. Nelder and R. Mead. A simplex method for function minimization. Comput. J., 7:308-313, 1965.   
[882] David Nelson, editor. The Penguin Dictionary of Mathematics. Second edition, Penguin, London, 1998. 461 pp. ISBN 0-14-051342-6.   
[883] A. Neumaier. Rundungsfehleranalyse einiger Verfahren zur Summation endlicher Summen. Z. Angew. Math. Mech., 54:39-51, 1974.   
[884] A. Neumaier. Inner product rounding error analysis in the presence of underflow. Computing, 34:365-373, 1985.   
[885] A. Neumaier. On the comparison of $H$ -matrices with $M$ -matrices. Linear Algebra Appl., 83:135-141, 1986.   
[886] M. Neumann and R. J. Plemmons. Backward error analysis for linear systems associated with inverses of $H$ -matrices. BIT, 24:102-112, 1984.   
[887] A. C. R. Newbery. Error analysis for Fourier series evaluation. Math. Comp., 27 (123):639-644, 1973.   
[888] A. C. R. Newbery. Error analysis for polynomial evaluation. Math. Comp., 28 (127):789-793, 1974.   
[889] Simon Newcomb. Note on the frequency of use of the different digits in natural numbers. Amer. J. Math., 4:39-40, 1881.   
[890] Morris Newman. Matrix computations. In Survey of Numerical Analysis, John Todd, editor, McGraw-Hill, New York, 1962, pages 222-254.   
[891] Morris Newman and John Todd. The evaluation of matrix inversion programs. J. Soc. Indust. Appl. Math., 6(4):466-476, 1958.   
[892] K. Nickel. Das Kahan-Babuskasche Summierungsverfahren in Triplex-ALGOL 60. Z. Angew. Math. Mech., 50:369-373, 1970.   
[893] Karl Nickel. Interval-analysis. In The State of the Art in Numerical Analysis, David A. H. Jacobs, editor, Academic Press, London, 1977, pages 193-225.   
[894] Jorge Nocedal and Stephen J. Wright. Numerical Optimization. Springer-Verlag, New York, 1999. xx+636 pp. ISBN 0-387-98793-2.   
[895] Yvan Notay. On the convergence rate of the conjugate gradients in presence of rounding errors. Numer. Math., 65:301-317, 1993.

[896] Colm Art O'Cinneide. Entrywise perturbation theory and error analysis for Markov chains. Numer. Math., 65:109-120, 1993.   
[897] W. Oettli. On the solution set of a linear system with inaccurate coefficients. SIAM J. Numer. Anal., 2(1):115-118, 1965.   
[898] W. Oettli and W. Prager. Compatibility of approximate solution of linear equations with given error bounds for coefficients and right-hand sides. Numer. Math., 6:405-409, 1964.   
[899] W. Oettli, W. Prager, and J. H. Wilkinson. Admissible solutions of linear systems with not sharply defined coefficients. SIAM J. Numer. Anal., 2(2):291-299, 1965.   
[900] Dianne Prost O'Leary. Estimating matrix condition numbers. SIAM J. Sci. Statist. Comput., 1(2):205-209, 1980.   
[901] J. Oliver. An error analysis of the modified Clenshaw method for evaluating Chebyshev and Fourier series. J. Inst. Maths. Applics., 20:379-391, 1977.   
[902] J. Oliver. Rounding error propagation in polynomial evaluation schemes. J. Comput. Appl. Math., 5(2):85-97, 1979.   
[903] F. W. J. Olver. A new approach to error arithmetic. SIAM J. Numer. Anal., 15 (2):368-393, 1978.   
[904] F. W. J. Olver. Error analysis of complex arithmetic. In Computational Aspects of Complex Analysis, volume 102 of NATO Advanced Study Institute Series C, D. Reidel, Dordrecht, Holland, 1983, pages 279-292.   
[905] F. W. J. Olver. Error bounds for polynomial evaluation and complex arithmetic. IMA J. Numer. Anal., 6:373-379, 1986.   
[906] F. W. J. Olver and J. H. Wilkinson. A posteriori error bounds for Gaussian elimination. IMA J. Numer. Anal., 2:377-406, 1982.   
[907] James M. Ortega. An error analysis of Householder's method for the symmetric eigenvalue problem. Numer. Math., 5:211-225, 1963.   
[908] James M. Ortega. Numerical Analysis: A Second Course. Academic Press, New York, 1972. xiii+201 pp. Republished by Society for Industrial and Applied Mathematics, Philadelphia, PA, USA, 1990. ISBN 0-89871-250-5 (original), 0-89871-250-5 (SIAM).   
[909] A. M. Ostrowski. Solution of Equations in Euclidean and Banach Spaces. Academic Press, New York, 1973. xx+412 pp. Third edition of Solution of Equations and Systems of Equations. ISBN 0-12530260-6.   
[910] Michael L. Overton. Numerical Computing with IEEE Floating Point Arithmetic: Including One Theorem, One Rule of Thumb, and One Hundred and One Exercises. Society for Industrial and Applied Mathematics, Philadelphia, PA, USA, 2001. xiv+104 pp. ISBN 0-89871-482-6.   
[911] C. C. Paige. An error analysis of a method for solving matrix equations. Math. Comp., 27(122):355-359, 1973.   
[912] C. C. Paige. Some aspects of generalized QR factorizations. In Reliable Numerical Computation, M. G. Cox and S. J. Hammarling, editors, Oxford University Press, 1990, pages 73-91.   
[913] C. C. Paige and M. Wei. History and generality of the CS decomposition. Linear Algebra Appl., 208/209:303-326, 1994.   
[914] C.-T. Pan. On the existence and computation of rank-revealing LU factorizations. Linear Algebra Appl., 316:199-222, 2000.

[915] Victor Y. Pan. Strassen algorithm is not optimal. Trilinear technique of aggregating, uniting and canceling for constructing fast algorithms for matrix multiplication. In Proc. 19th Annual Symposium on the Foundations of Computer Science, Ann Arbor, MI, USA, 1978, pages 166-176.   
[916] Victor Y. Pan. How can we speed up matrix multiplication? SIAM Rev., 26(3): 393-415, 1984.   
[917] Victor Y. Pan. Structured Matrices and Polynomials: Unified Superfast Algorithms. Birkhäuser, Boston, MA, USA, 2001. xxiv+278 pp. ISBN 0-8176-4240-4.   
[918] Victor Y. Pan, Sheryl Branham, Rhys E. Rosholt, and Ai-Long Zheng. Newton's iteration for structured matrices. In *Fast Reliable Algorithms for Matrices with Structure*, Thomas Kailath and Ali H. Sayed, editors, Society for Industrial and Applied Mathematics, Philadelphia, PA, USA, 1999, pages 189-210.   
[919] Victor Y. Pan and Robert Schreiber. An improved Newton iteration for the generalized inverse of a matrix, with applications. SIAM J. Sci. Statist. Comput., 12(5):1109-1130, 1991.   
[920] Victor Y. Pan and Y. Yu. Certification of numerical computation of the sign of the determinant of a matrix. Algorithmica, 30(4):708-724, 2001.   
[921] Behrooz Parhami. Computer Arithmetic: Algorithms and Hardware Designs. Oxford University Press, New York, 2000. xx+490 pp. ISBN 0-19-512583-5.   
[922] Beresford N. Parlett. Laguerre's method applied to the matrix eigenvalue problem. Math. Comp., 18:464-485, 1964.   
[923] Beresford N. Parlett. Matrix eigenvalue problems. Amer. Math. Monthly, 72(2): 59-66, 1965.   
[924] Beresford N. Parlett. Analysis of algorithms for reflections in bisectors. SIAM Rev., 13(2):197-208, 1971.   
[925] Beresford N. Parlett. The contribution of J. H. Wilkinson to numerical analysis. In A History of Scientific Computing, Stephen G. Nash, editor, Addison-Wesley, Reading, MA, USA, 1990, pages 17-30.   
[926] Beresford N. Parlett. The Symmetric Eigenvalue Problem. Society for Industrial and Applied Mathematics, Philadelphia, PA, USA, 1998. xxiv+398 pp. Unabridged, amended version of book first published by Prentice-Hall in 1980. ISBN 0-89871-402-8.   
[927] Beresford N. Parlett and Inderjit S. Dhillon. Relatively robust representations of symmetric tridiagonals. Linear Algebra Appl., 309:121-151, 2000.   
[928] Michael S. Paterson and Larry J. Stockmeyer. On the number of nonscalar multiplications necessary to evaluate polynomials. SIAM J. Comput., 2(1):60-66, 1973.   
[929] David A. Patterson and John L. Hennessy. Computer Organization and Design: The Hardware/Software Interface. Second edition, Morgan Kaufmann, San Francisco, CA, USA, 1998. xxix+759+appendices pp. ISBN 1-55860-428-6.   
[930] Vern Paxson. A program for testing IEEE decimal-binary conversion. Manuscript. ftp://ftp.ee.lbl.gov/testbase-report.ps.Z, May 1991. 40 pp.   
[931] Heinz-Otto Peitgen, Hartmut Jürgens, and Dietmar Saupe. Fractals for the Classroom. Part One: Introduction to Fractals and Chaos. Springer-Verlag, New York, 1992. xiv+450 pp. ISBN 0-387-97041-X.

[932] J. M. Pena. Pivoting strategies leading to small bounds of the errors for certain linear systems. IMA J. Numer. Anal., 16(2):141-153, 1996.   
[933] J. M. Pena. Pivoting strategies leading to diagonal dominance by rows. Numer. Math., 81:293-304, 1998.   
[934] Thilo Penzl. Numerical solution of generalized Lyapunov equations. Adv. in Comput. Math., 8:33-48, 1998.   
[935] Colin Percival. Rapid multiplication modulo the sum and difference of highly composite numbers. Math. Comp., 2002. To appear.   
[936] G. Peters and J. H. Wilkinson. The least squares problem and pseudo-inverses. Comput. J., 13(3):309-316, 1970.   
[937] G. Peters and J. H. Wilkinson. Practical problems arising in the solution of polynomial equations. J. Inst. Maths. Applics., 8:16-35, 1971.   
[938] G. Peters and J. H. Wilkinson. On the stability of Gauss-Jordan elimination with pivoting. Comm. ACM, 18(1):20-24, 1975.   
[939] Karl Petersen. *Ergodic Theory*. Cambridge University Press, Cambridge, UK, 1981. xi+329 pp. ISBN 0-521-23632-0.   
[940] M. Pichat. Correction d'une somme en arithmetique à virgule flottante. Numer. Math., 19:400-406, 1972.   
[941] Daniel J. Pierce and Robert J. Plemmons. Fast adaptive condition estimation. SIAM J. Matrix Anal. Appl., 13(1):274-291, 1992.   
[942] P. J. Plauger. Properties of floating-point arithmetic. Computer Language, 5(3): 17-22, 1988.   
[943] R. J. Plemmons. Regular splittings and the discrete Neumann problem. Numer. Math., 25:153-161, 1976.   
[944] Robert J. Plemmons. Linear least squares by elimination and MGS. J. Assoc. Comput. Mach., 21(4):581-585, 1974.   
[945] Svatopluk Poljak and Jiří Rohn. Checking robust nonsingularity is NP-hard. Math. Control Signals Systems, 6:1-9, 1993.   
[946] Ben Polman. Incomplete blockwise factorizations of (block) $H$ -matrices. Linear Algebra Appl., 90:119-132, 1987.   
[947] George Poole and Larry Neal. The rook's pivoting strategy. J. Comput. Appl. Math., 123:353-369, 2000.   
[948] M. J. D. Powell. A survey of numerical methods for unconstrained optimization. SIAM Rev., 12(1):79-97, 1970.   
[949] M. J. D. Powell. A view of unconstrained minimization algorithms that do not require derivatives. ACM Trans. Math. Software, 1(2):97-107, 1975.   
[950] M. J. D. Powell. Direct search algorithms for optimization calculations. Acta Numerica, 7:287-336, 1998.   
[951] M. J. D. Powell and J. K. Reid. On applying Householder transformations to linear least squares problems. In Proc. IFIP Congress 1968, North-Holland, Amsterdam, The Netherlands, 1969, pages 122-126.   
[952] Stephen Power. The Cholesky decomposition in Hilbert space. IMA Bulletin, 22 (11/12):186-187, 1986.

[953] William H. Press, Saul A. Teukolsky, William T. Vetterling, and Brian P. Flannery. Numerical Recipes in FORTRAN: The Art of Scientific Computing. Second edition, Cambridge University Press, 1992. xxvi+963 pp. ISBN 0-521-43064-X.   
[954] Douglas M. Priest. Algorithms for arbitrary precision floating point arithmetic. In Proc. 10th IEEE Symposium on Computer Arithmetic, Peter Kornerup and David W. Matula, editors, IEEE Computer Society Press, Los Alamitos, CA, USA, 1991, pages 132-143.   
[955] Douglas M. Priest. On Properties of Floating Point Arithmetics: Numerical Stability and the Cost of Accurate Computations. PhD thesis, Mathematics Department, University of California, Berkeley, CA, USA, November 1992. 126 pp. ftp://ftp.icsi.berkeley.edu/pub/theory/priest-thesis.ps.Z.   
[956] J. D. Pryce. Round-off error analysis with fewer tears. IMA Bulletin, 17:40-47, 1981.   
[957] J. D. Pryce. A new measure of relative error for vectors. SIAM J. Numer. Anal., 21(1):202-215, 1984.   
[958] J. D. Pryce. Multiplicative error analysis of matrix transformation algorithms. IMA J. Numer. Anal., 5:437-445, 1985.   
[959] Chiara Puglisi. Modification of the Householder method based on the compact WY representation. SIAM J. Sci. Statist. Comput., 13(3):723-726, 1992.   
[960] Heinrich Puschmann and Joaquín Cortés. The coordinex problem and its relation to the conjecture of Wilkinson. Numer. Math., 42:291-297, 1983.   
[961] Heinrich Puschmann and Marcelo Nordio. Zwei Unzalässige Verständkungen der Vermutung von Wilkinson. Linear Algebra Appl., 72:167-176, 1985. In German.   
[962] Gerald D. Quinlan. Round-off error in long-term orbital integrations using multi-step methods. Celestial Mechanics and Dynamical Astronomy, 58:339-351, 1994.   
[963] Kevin Quinn. Ever had problems rounding off figures? This stock exchange has. Wall Street Journal, 1983. 8 November.   
[964] Thomas Quinn and Scott Tremaine. Roundoff error in long-term planetary orbit integrations. *Astron. J.*, 99(3):1016-1023, 1990.   
[965] Thomas R. Quinn, Scott Tremaine, and Martin Duncan. A three million year integration of the earth's orbit. *Astron. J.*, 101(6):2287-2305, 1991.   
[966] Enrique S. Quintana, Gregorio Quintana, Xiaobai Sun, and Robert van de Geijn. A note on parallel matrix inversion. SIAM J. Sci. Comput., 22(5):1762-1771, 2001.   
[967] Ralph A. Raimi. The peculiar distribution of first digits. Scientific American, 221 (6):109-120, 1969.   
[968] Ralph A. Raimi. The first digit problem. Amer. Math. Monthly, 83:521-538, 1976.   
[969] Louis B. Rall. Automatic Differentiation: Techniques and Applications, volume 120 of Lecture Notes in Computer Science. Springer-Verlag, Berlin, 1981. viii+165 pp.   
[970] Louis B. Rall. Tools for mathematical computation. In Computer Aided Proofs in Analysis, Kenneth R. Meyer and Dieter S. Schmidt, editors, volume 28 of IMA Volumes in Mathematics and Its Applications, Springer-Verlag, New York, 1991, pages 217-228.   
[971] George U. Ramos. Roundoff error analysis of the fast Fourier transform. Math. Comp., 25(116):757-768, 1971.

[972] Brian Randell, editor. The Origins of Digital Computers: Selected Papers. Third edition, Springer-Verlag, Berlin, 1975. xvi+580 pp. ISBN 3-540-11319-3.   
[973] Wolfgang Rath. Fast Givens rotations for orthogonal similarity transformations. Numer. Math., 40:47-56, 1982.   
[974] Satish C. Reddy and Lloyd N. Trefethen. Stability of the method of lines. Numer. Math., 62:235-267, 1992.   
[975] Lothar Reichel. Newton interpolation at Leja points. BIT, 30:332-346, 1990.   
[976] Lothar Reichel. Fast QR decomposition of Vandermonde-like matrices and polynomial least squares approximation. SIAM J. Matrix Anal. Appl., 12(3):552-564, 1991.   
[977] Lothar Reichel and Gerhard Opfer. Chebyshev-Vandermonde systems. Math. Comp., 57(196):703-721, 1991.   
[978] Lothar Reichel and Lloyd N. Trefethen. Eigenvalues and pseudo-eigenvalues of Toeplitz matrices. Linear Algebra Appl., 162-164:153-185, 1992.   
[979] J. K. Reid. A note on the stability of Gaussian elimination. J. Inst. Maths. Applics., 8:374-375, 1971.   
[980] J. K. Reid. Sparse matrices. In The State of the Art in Numerical Analysis, A. Iserles and M. J. D. Powell, editors, Oxford University Press, 1987, pages 59-85.   
[981] J. K. Reid. Implicit scaling of linear least squares problems. BIT, 40(1):146-157, 2000.   
[982] John F. Reiser and Donald E. Knuth. Evading the drift in floating-point addition. Inform. Process. Lett., 3(3):84-87, 1975.   
[983] Werner C. Rheinboldt. On measures of ill-conditioning for nonlinear equations. Math. Comp., 30(133):104-111, 1976.   
[984] John R. Rice. Experiments on Gram-Schmidt orthogonalization. Math. Comp., 20:325-328, 1966.   
[985] John R. Rice. A theory of condition. SIAM J. Numer. Anal., 3(2):287-310, 1966.   
[986] J. L. Rigal and J. Gaches. On the compatibility of a given solution with the data of a linear system. J. Assoc. Comput. Mach., 14(3):543-548, 1967.   
[987] T. G. Robertazzi and S. C. Schwartz. Best “ordering” for floating-point addition. ACM Trans. Math. Software, 14(1):101-110, 1988.   
[988] J. D. Roberts. Linear model reduction and solution of the algebraic Riccati equation by use of the sign function. Internat. J. Control, 32(4):677-687, 1980. First issued as report CUED/B-Control/TR13, Department of Engineering, University of Cambridge, 1971.   
[989] Jiri Rohn. New condition numbers for matrices and linear systems. Computing, 41:167-169, 1989.   
[990] Jiri Rohn. Systems of linear interval equations. Linear Algebra Appl., 126:39-78, 1989.   
[991] Jiri Rohn. Nonsingularity under data rounding. Linear Algebra Appl., 139:171-174, 1990.   
[992] Jiri Rohn. NP-hardness results for some linear and quadratic problems. Technical Report No. 619, Institute of Computer Science, Academy of Sciences of the Czech Republic, Prague, January 1995. 11 pp.

[993] D. R. Ross. Reducing truncation errors using cascading accumulators. Comm. ACM, 8(1):32-33, 1965.   
[994] M. W. Routh, P. A. Swartz, and M. B. Denton. Performance of the super modified simplex. Analytical Chemistry, 49(9):1422-1428, 1977.   
[995] Thomas Harvey Rowan. Functional Stability Analysis of Numerical Algorithms. PhD thesis, University of Texas at Austin, Austin, TX, USA, May 1990. xii+205 pp.   
[996] Axel Ruhe. Numerical aspects of Gram-Schmidt orthogonalization of vectors. Linear Algebra Appl., 52/53:591-601, 1983.   
[997] Siegfried M. Rump. Structured perturbations and symmetric matrices. Linear Algebra Appl., 278:121-132, 1998.   
[998] Siegfried M. Rump. Fast and parallel interval arithmetic. BIT, 39(3):534-554, 1999.   
[999] Siegfried M. Rump. Ill-conditioned matrices are componentwise near to singularity. SIAM Rev., 41(1):102-112, 1999.   
[1000] Siegfried M. Rump. INTLAB—INTerval LABoratory. In *Developments in Reliable Computing*, Tibor Csendes, editor, Kluwer Academic Publishers, Dordrecht, The Netherlands, 1999, pages 77–104.   
[1001] Siegfried M. Rump. Self-validating methods. Linear Algebra Appl., 324:3-13, 2001.   
[1002] Siegfried M. Rump. Optimal scaling for $P$ -norms and componentwise distance to singularity. IMA J. Numer. Anal., 2002. To appear.   
[1003] David M. Russinoff. A mechanically checked proof of IEEE compliance of the floating point multiplication, division and square root algorithms of the AMD-K7 processor. LMS J. Computer Math., 1:148-200, 1998.   
[1004] D. E. Rutherford. Some continuant determinants arising in physics and chemistry. Proc. Royal Soc. Edin., 62, A:229-236, 1947.   
[1005] D. E. Rutherford. Some continuant determinants arising in physics and chemistry—II. Proc. Royal Soc. Edin., 63, A:232-241, 1952.   
[1006] H. Rutishauser. On test matrices. In *Programmation en Mathématiques Numériques*, Besançon, 1966, volume 7 (no. 165) of *Éditions Centre Nat. Recherche Sci.*, Paris, 1968, pages 349-365.   
[1007] Heinz Rutishauser. Solution of eigenvalue problems with the LR-transformation. In Further Contributions to the Solution of Simultaneous Linear Equations and the Determination of Eigenvalues, number 49 in Applied Mathematics Series, National Bureau of Standards, United States Department of Commerce, Washington, D. C., 1958, pages 47-81.   
[1008] Ahmed H. Sameh and Richard P. Brent. Solving triangular systems on a parallel computer. SIAM J. Numer. Anal., 14(6):1101-1113, 1977.   
[1009] Klaus Samelson and Friedrich L. Bauer. Optimale Rechengenaugkeit bei Rechenanlagen mit gleitendem Komma. Z. Angew. Math. Phys., 4:312-316, 1953.   
[1010] J. M. Sanz-Serna and S. Larsson. Shadows, chaos, and saddles. Appl. Numer. Math., 13:181-190, 1993.   
[1011] M. A. Saunders. Large-scale linear programming using the Cholesky factorization. Report CS 252, Department of Computer Science, Stanford University, January 1972.

[1012] Werner Sautter. Error analysis of Gauss elimination for the best least squares problem. Numer. Math., 30:165-184, 1978.   
[1013] I. Richard Savage and Eugene Lukacs. Tables of inverse of finite segments of the Hilbert matrix. In Contributions to the Solution of Systems of Linear Equations and the Determination of Eigenvalues, Olga Taussky, editor, number 39 in Applied Mathematics Series, National Bureau of Standards, United States Department of Commerce, Washington, D. C., 1954, pages 105-108.   
[1014] James B. Scarborough. Numerical Mathematical Analysis. Second edition, Johns Hopkins University Press, Baltimore, MD, USA, 1950. xviii+511 pp.   
[1015] James C. Schatzman. Accuracy of the discrete Fourier transform and the fast Fourier transform. SIAM J. Sci. Comput., 17(5):1150-1166, 1996.   
[1016] Charles W. Schelin. Calculator function approximation. Amer. Math. Monthly, 90(5):317-325, 1983.   
[1017] R. Scherer and K. Zeller. Shorthand notation for rounding errors. Computing, Suppl. 2:165-168, 1980.   
[1018] Hans Schneider and W. Gilbert Strang. Comparison theorems for supremum norms. Numer. Math., 4:15-20, 1962.   
[1019] Hans Schneider and Hans F. Weinberger. On matrices for which norm bounds are attained. Linear Algebra Appl., 275-276:563-577, 1998.   
[1020] J. L. Schonfelder and M. Razaz. Error control with polynomial approximations. IMA J. Numer. Anal., 1:105-114, 1980.   
[1021] Robert S. Schreiber. Block algorithms for parallel machines. In Numerical Algorithms for Modern Parallel Computer Architectures, M. H. Schultz, editor, number 13 in IMA Volumes In Mathematics and Its Applications, Springer-Verlag, Berlin, 1988, pages 197-207.   
[1022] Robert S. Schreiber. Hough's random story explained. *NA Digest*, Volume 89, Issue 3, 1989.   
[1023] Robert S. Schreiber and Beresford N. Parlett. Block reflectors: Theory and computation. SIAM J. Numer. Anal., 25(1):189-205, 1988.   
[1024] Robert S. Schreiber and Charles F. Van Loan. A storage efficient WY representation for products of Householder transformations. SIAM J. Sci. Statist. Comput., 10:53-57, 1989.   
[1025] N. L. Schryer. A test of a computer's floating-point arithmetic unit. Computing Science Technical Report No. 89, AT&T Bell Laboratories, Murray Hill, NJ, USA, 1981.   
[1026] N. L. Schryer. Determination of correct floating-point model parameters. In Sources and Development of Mathematical Software, Wayne R. Cowell, editor, Prentice-Hall, Englewood Cliffs, NJ, USA, 1984, pages 360-366.   
[1027] Günther Schulz. Iterative Berechnung der reziproken Matrix. Z. Angew. Math. Mech., 13:57-59, 1933.   
[1028] Robert Sedgewick. Algorithms. Second edition, Addison-Wesley, Reading, MA, USA, 1988. xii+657 pp. ISBN 0-201-06673-4.   
[1029] Charles Severance. An interview with the old man of floating-point. Reminiscences elicited from William Kahan by Charles Severance, February 1998. http://www.cs.berkeley.edu/~wkahan/ieee754status/754story.html. A shortened version appears in Computer, 31(3):114-115, March 1998.

[1030] Lawrence F. Shampine. Numerical Solution of Ordinary Differential Equations. Chapman and Hall, New York, 1994. x+484 pp. ISBN 0-412-05151-6.   
[1031] Lawrence F. Shampine and Richard C. Allen, Jr. Numerical Computing: An Introduction. W. B. Saunders, Philadelphia, PA, USA, 1973. vii+258 pp. ISBN 0-7216-8150-6.   
[1032] Lawrence F. Shampine and Mark W. Reichelt. The MATLAB ODE suite. SIAM J. Sci. Comput., 18(1):1-22, 1997.   
[1033] Alexander Shapiro. Optimally scaled matrices, necessary and sufficient conditions. Numer. Math., 39:239-245, 1982.   
[1034] Alexander Shapiro. Optimal block diagonal $l_{2}$ -scaling of matrices. SIAM J. Numer. Anal., 22(1):81-94, 1985.   
[1035] Alexander Shapiro. Upper bounds for nearly optimal diagonal scaling of matrices. Linear and Multilinear Algebra, 29:147-147, 1991.   
[1036] H. P. Sharangpani and M. L. Barton. Statistical analysis of floating point flaw in the Pentium processor (1994). Technical report, Intel Corporation, November 1994. 31 pp.   
[1037] David Shepherd and Greg Wilson. Making chips that work. New Scientist, pages 61-64, 1989. 13 May.   
[1038] Jonathan Richard Shewchuk. Adaptive precision floating-point arithmetic and fast robust geometric predicates. Discrete and Computational Geometry, 18(3): 305-363, 1997.   
[1039] Gautam M. Shroff and Christian H. Bischof. Adaptive condition estimation for rank-one updates of QR factorizations. SIAM J. Matrix Anal. Appl., 13(4):1264-1278, 1992.   
[1040] Robert D. Skeel. Scaling for numerical stability in Gaussian elimination. J. Assoc. Comput. Mach., 26(3):494-526, 1979.   
[1041] Robert D. Skeel. Iterative refinement implies numerical stability for Gaussian elimination. Math. Comp., 35(151):817-832, 1980.   
[1042] Robert D. Skeel. Effect of equilibration on residual size for partial pivoting. SIAM J. Numer. Anal., 18(3):449-454, 1981.   
[1043] Robert D. Skeel. Safety in numbers: The boundless errors of numerical computation. Working Document 89-3, Department of Computer Science, University of Illinois, Urbana, IL, USA, 1989. 9 pp.   
[1044] Robert D. Skeel and Jerry B. Keiper. Elementary Numerical Computing with Mathematica. McGraw-Hill, New York, 1993. xiv+434 pp. ISBN 0-07-057820-6.   
[1045] Gerard L. G. Sleijpen, Henk A. Van der Vorst, and Jan Modersitzki. Differences in the effects of rounding errors in Krylov solvers for symmetric indefinite linear systems. SIAM J. Matrix Anal. Appl., 22(3):726-751, 2000.   
[1046] Steve Smale. Some remarks on the foundations of numerical analysis. SIAM Rev., 32(2):211-220, 1990.   
[1047] B. T. Smith, J. M. Boyle, J. J. Dongarra, B. S. Garbow, Y. Ikebe, V. C. Klema, and C. B. Moler. Matrix Eigensystem Routines—EISPACK Guide, volume 6 of Lecture Notes in Computer Science. Second edition, Springer-Verlag, Berlin, 1976. vii+551 pp. ISBN 3-540-06710-8.   
[1048] David M. Smith. Algorithm 693: A FORTRAN package for floating-point multiple-precision arithmetic. ACM Trans. Math. Software, 17(2):273-283, 1991.

[1049] David M. Smith. Algorithm 786: Multiple-precision complex arithmetic and functions. ACM Trans. Math. Software, 24(4):359-367, 1998.   
[1050] Francis J. Smith. An algorithm for summing orthogonal polynomial series and their derivatives with applications to curve-fitting and interpolation. Math. Comp., 19:33-36, 1965.   
[1051] Jon M. Smith. Scientific Analysis on the Pocket Calculator. Wiley, New York, 1975. xii+380 pp. ISBN 0-471-79997-1.   
[1052] Robert L. Smith. Algorithm 116: Complex division. Comm. ACM, 5(8):435, 1962.   
[1053] Alicja Smoktunowicz. A note on the strong componentwise stability of algorithms for solving symmetric linear systems. Demonstratio Mathematica, 28(2):443-448, 1995.   
[1054] Alicja Smoktunowicz and Jolanta Sokolnicka. Binary cascades iterative refinement in doubled-mantissa arithmetics. BIT, 24:123-127, 1984.   
[1055] James N. Snyder. On the improvement of the solutions to a set of simultaneous linear equations using the ILLIAC. Mathematical Tables and Other Aids to Computation, 9:177-184, 1955.   
[1056] Torsten Söderström and G. W. Stewart. On the numerical properties of an iterative method for computing the Moore-Penrose generalized inverse. SIAM J. Numer. Anal., 11(1):61-74, 1974.   
[1057] D. C. Sorensen. Analysis of pairwise pivoting in Gaussian elimination. IEEE Trans. Comput., C-34:274-278, 1985.   
[1058] J. Spieß. Untersuchungen des Zeitgewinn durch neue Algorithmen zur Matrix-Multiplikation. Computing, 17:23-36, 1976.   
[1059] Gerhard Starke and Wilhelm Niethammer. SOR for $AX - XB = C$ . Linear Algebra Appl., 154-156:355-375, 1991.   
[1060] Guy L. Steele, Jr. and Jon L. White. How to print floating-point numbers accurately. SIGPLAN Notices, 25(6):112-126, 1990.   
[1061] Irene A. Stegun and Milton Abramowitz. Pitfalls in computation. J. Soc. Indust. Appl. Math., 4(4):207-219, 1956.   
[1062] Pat H. Sterbenz. *Floating-Point Computation*. Prentice-Hall, Englewood Cliffs, NJ, USA, 1974. xiv+316 pp. ISBN 0-13-322495-3.   
[1063] G. W. Stewart. Error analysis of the algorithm for shifting the zeros of a polynomial by synthetic division. Math. Comp., 25(113):135-139, 1971.   
[1064] G. W. Stewart. Error and perturbation bounds for subspaces associated with certain eigenvalue problems. SIAM Rev., 15(4):727-764, 1973.   
[1065] G. W. Stewart. Introduction to Matrix Computations. Academic Press, New York, 1973. xiii+441 pp. ISBN 0-12-670350-7.  
[1066] G. W. Stewart. Modifying pivot elements in Gaussian elimination. Math. Comp., 28(126):537-542, 1974.   
[1067] G. W. Stewart. On the perturbation of pseudo-inverses, projections and linear least squares problems. SIAM Rev., 19(4):634-662, 1977.   
[1068] G. W. Stewart. Perturbation bounds for the $QR$ factorization of a matrix. SIAM J. Numer. Anal., 14(3):509-518, 1977.   
[1069] G. W. Stewart. Research, development, and LINPACK. In Mathematical Software III, John R. Rice, editor, Academic Press, New York, 1977, pages 1-14.

[1070] G. W. Stewart. The efficient generation of random orthogonal matrices with an application to condition estimators. SIAM J. Numer. Anal., 17(3):403-409, 1980.   
[1071] G. W. Stewart. A note on complex division. ACM Trans. Math. Software, 11(3): 238-241, 1985.   
[1072] G. W. Stewart. Stochastic perturbation theory. SIAM Rev., 32(4):579-610, 1990.   
[1073] G. W. Stewart. Note on a generalized Sylvester equation. IMA Preprint Series #985, Institute for Mathematics and Its Applications, University of Minnesota, Minneapolis, MN, USA, May 1992. 3 pp.   
[1074] G. W. Stewart. On the early history of the singular value decomposition. SIAM Rev., 35(4):551-566, 1993.   
[1075] G. W. Stewart. On the perturbation of LU, Cholesky, and QR factorizations. SIAM J. Matrix Anal. Appl., 14(4):1141-1145, 1993.   
[1076] G. W. Stewart. Gauss, statistics, and Gaussian elimination. Journal of Computational and Graphical Statistics, 4(1):1-11, 1995.   
[1077] G. W. Stewart. On Markov chains with sluggish transients. Communication in Statistics, Stochastic Models, 13:85-95, 1997.   
[1078] G. W. Stewart. On the perturbation of LU and Cholesky factors. IMA J. Numer. Anal., 17(1):1-6, 1997.   
[1079] G. W. Stewart. The triangular matrices of Gaussian elimination and related decompositions. IMA J. Numer. Anal., 17(1):7-16, 1997.   
[1080] G. W. Stewart. Matrix Algorithms. Volume I: Basic Decompositions. Society for Industrial and Applied Mathematics, Philadelphia, PA, USA, 1998. xx+458 pp. ISBN 0-89871-414-1.   
[1081] G. W. Stewart. On the adjugate matrix. Linear Algebra Appl., 283:151-164, 1998.   
[1082] G. W. Stewart. Matrix Algorithms. Volume II: Eigensystems. Society for Industrial and Applied Mathematics, Philadelphia, PA, USA, 2001. xix+469 pp. ISBN 0-89871-503-2.   
[1083] G. W. Stewart and Ji-guang Sun. Matrix Perturbation Theory. Academic Press, London, 1990. xv+365 pp. ISBN 0-12-670230-6.   
[1084] Michael Stewart. Cholesky factorization of semidefinite Toeplitz matrices. Linear Algebra Appl., 254:497-525, 1997.   
[1085] Josef Stoer. Einführung in die Numerische Mathematik I. Springer-Verlag, Berlin, 1972. ix+250 pp. ISBN 0-387-05750-1.   
[1086] Josef Stoer and R. Bulirsch. Introduction to Numerical Analysis. Springer-Verlag, New York, 1980. ix+609 pp. ISBN 0-387-90420-4.   
[1087] Josef Stoer and C. Witzgall. Transformations by diagonal matrices in a normed space. Numer. Math., 4:158-171, 1962.   
[1088] Betty Jane Stone. Best possible ratios of certain matrix norms. Numer. Math., 4:114-116, 1962.   
[1089] David R. Stoutemyer. Automatic error analysis using computer algebraic manipulation. ACM Trans. Math. Software, 3(1):26-43, 1977.   
[1090] David R. Stoutmyer. Crimes and misdemeanours in the computer algebra trade. Notices Amer. Math. Soc., 38(7):778-785, 1991.   
[1091] Gilbert Strang. A proposal for Toeplitz matrix calculations. Studies in Applied Mathematics, 74:171-176, 1986.

[1092] Gilbert Strang. Introduction to Linear Algebra. Wellesley-Cambridge Press, Wellesley, MA, USA, 1993. viii+472 pp. ISBN 0-9614088-5-5.   
[1093] V. Strassen. Gaussian elimination is not optimal. Numer. Math., 13:354-356, 1969.   
[1094] F. Stummel. Rounding error analysis of elementary numerical algorithms. Computing, Suppl. 2:169-195, 1980.   
[1095] F. Stummel. Perturbation theory for evaluation algorithms of arithmetic expressions. Math. Comp., 37(156):435-473, 1981.   
[1096] F. Stummel. Optimal error estimates for Gaussian elimination in floating-point arithmetic. Z. Angew. Math. Mech., 62:T355-T357, 1982.   
[1097] F. Stummel. Strict optimal error estimates for Gaussian elimination. Z. Angew. Math. Mech., 65:T405-T407, 1985.   
[1098] Friedrich Stummel. Forward error analysis of Gaussian elimination, Part I: Error and residual estimates. Numer. Math., 46:365-395, 1985.   
[1099] Friedrich Stummel. Forward error analysis of Gaussian elimination, Part II: Stability theorems. Numer. Math., 46:397-415, 1985.   
[1100] SPARCompiler FORTRAN: Numerical Computation Guide. Sun Microsystems, Inc., Mountain View, CA, USA, October 1992. Part No. 800-7097-11, Revision A.   
[1101] SPARCompiler FORTRAN 2.0.1: User's Guide. Sun Microsystems, Inc., Mountain View, CA, USA, October 1992. Part No. 800-6552-11, Revision A.   
[1102] Ji-guang Sun. Perturbation bounds for the Cholesky and QR factorizations. BIT, 31:341-352, 1991.   
[1103] Ji-guang Sun. Componentwise perturbation bounds for some matrix decompositions. BIT, 32(4):702-714, 1992.   
[1104] Ji-guang Sun. Rounding-error and perturbation bounds for the Cholesky and $LDL^T$ factorizations. Linear Algebra Appl., 173:77-97, 1992.   
[1105] Ji-guang Sun. A note on backward perturbations for the Hermitian eigenvalue problem. BIT, 35:385-393, 1995.   
[1106] Ji-guang Sun. On perturbation bounds for the QR factorization. Linear Algebra Appl., 215:95-111, 1995.   
[1107] Ji-guang Sun. Optimal backward perturbation bounds for the linear least-squares problem with multiple right-hand sides. IMA J. Numer. Anal., 16(1):1-11, 1996.   
[1108] Ji-guang Sun. On optimal backward perturbation bounds for the linear least squares problem. BIT, 37(1):179-188, 1997.   
[1109] Ji-guang Sun. Bounds for the structured backward errors of Vandermonde systems. SIAM J. Matrix Anal. Appl., 20(1):45-59, 1998.   
[1110] Ji-guang Sun and Zheng Sun. Optimal backward perturbation bounds for under-determined systems. SIAM J. Matrix Anal. Appl., 18(2):393-402, 1997.   
[1111] Xiaobai Sun and Christian H. Bischof. A basis-kernel representation of orthogonal matrices. SIAM J. Matrix Anal. Appl., 16(4):1184-1196, 1995.   
[1112] W. H. Swann. Direct search methods. In Numerical Methods for Unconstrained Optimization, W. Murray, editor, Academic Press, London, 1972, pages 13-28.

[1113] W. H. Swann. Constrained optimization by direct search. In Numerical Methods for Constrained Optimization, P. E. Gill and W. Murray, editors, Academic Press, London, 1974, pages 191-217.   
[1114] Earl E. Swartzlander, Jr., editor. Computer Arithmetic, volume 21 of Benchmark Papers in Electrical Engineering and Computer Science. Dowden, Hutchinson and Ross, Stroudsburg, PA, USA, 1980.   
[1115] Earl E. Swartzlander, Jr. and Aristides G. Alexopolous. The sign/logarithm number system. IEEE Trans. Comput., C-24(12):1238-1242, 1975.   
[1116] D. W. Sweeney. An analysis of floating-point addition. IBM Systems Journal, 4: 31-42, 1965. Reprinted in [1114, pp. 317-328].   
[1117] J. J. Sylvester. Additions to the articles, “On a New Class of Theorems,” and “On Pascal's Theorem”. Philosophical Magazine, 37:363-370, 1850. Reprinted in [1120, pp. 1451-151].   
[1118] J. J. Sylvester. On the relation between the minor determinants of linearly equivalent quadratic functions. Philosophical Magazine, (Fourth Series) 1:295-305, 1851. Reprinted in [1120, pp. 241-250].   
[1119] J. J. Sylvester. Sur l'équation en matrices $px = xq$ . Comptes Rendus de l'Académie des Sciences, pages 67-71 and 115-116, 1884.   
[1120] The Collected Mathematical Papers of James Joseph Sylvester, volume 1 (1837-1853). Cambridge University Press, 1904. xii+650 pp.   
[1121] Ping Tak Peter Tang. Table-driven implementation of the exponential function in IEEE floating-point arithmetic. ACM Trans. Math. Software, 15(2):144-157, 1989.   
[1122] Ping Tak Peter Tang. Accurate and efficient testing of the exponential and logarithm functions. ACM Trans. Math. Software, 16(3):185-200, 1990.   
[1123] Ping Tak Peter Tang. Table-driven implementation of the logarithm function in IEEE floating-point arithmetic. ACM Trans. Math. Software, 16(3):378-400, 1990.   
[1124] Ping Tak Peter Tang. Table-lookup algorithms for elementary functions and their error analysis. In Proc. 10th IEEE Symposium on Computer Arithmetic, Peter Kornerup and David W. Matula, editors, IEEE Computer Society Press, Los Alamitos, CA, USA, 1991, pages 232-236.   
[1125] Ping Tak Peter Tang. Table-driven implementation of the expm1 function in IEEE floating-point arithmetic. ACM Trans. Math. Software, 18(2):211-222, 1992.   
[1126] W. P. Tang and G. H. Golub. The block decomposition of a Vandermonde matrix and its applications. BIT, 21:505-517, 1981.   
[1127] Pham Dinh Tao. Convergence of a subgradient method for computing the bound norm of matrices. Linear Algebra Appl., 62:163-182, 1984. In French.   
[1128] Pham Dinh Tao. Some methods for computing the maximum of quadratic form on the unit ball of the maximum norm. Numer. Math., 45:377-401, 1984. In French.   
[1129] Manfred Tasche and Hansmartin Zeuner. Worst and average case roundoff error analysis for FFT. BIT, 41(3):563-581, 2001.   
[1130] A. H. Taub, editor. John von Neumann Collected Works, volume V, Design of Computers, Theory of Automata and Numerical Analysis. Pergamon, Oxford, 1963. ix+784 pp.

[1131] Olga Taussky. A remark concerning the characteristic roots of the finite segments of the Hilbert matrix. Quarterly Journal of Mathematics, 20:80-83, 1949.   
[1132] Olga Taussky. How I became a torchbearer for matrix theory. Amer. Math. Monthly, 95(9):801-812, 1988.   
[1133] Olga Taussky and Marvin Marcus. Eigenvalues of finite matrices. In Survey of Numerical Analysis, John Todd, editor, McGraw-Hill, New York, 1962, pages 279-313.   
[1134] Henry C. Thacher, Jr. Algorithm 43: Crout with pivoting II. Comm. ACM, 4(4): 176-177, 1961.   
[1135] Ronald A. Thisted. Elements of Statistical Computing: Numerical Computation. Chapman and Hall, New York, 1988. xx+427 pp. ISBN 0-412-01371-1.   
[1136] D'Arcy Wentworth Thompson. On Growth and Form. The Complete Revised Edition. Cambridge University Press, 1942. viii+1116 pp. Reprinted by Dover, New York, 1992. ISBN 0-486-67135-6.   
[1137] Martti Tienari. A statistical model of roundoff error for varying length floating-point arithmetic. BIT, 10:355-365, 1970.   
[1138] Françoise Tisseur. Newton's method in floating point arithmetic and iterative refinement of generalized eigenvalue problems. SIAM J. Matrix Anal. Appl., 22 (4):1038-1057, 2001.   
[1139] Françoise Tisseur and Karl Meerbergen. The quadratic eigenvalue problem. SIAM Rev., 43(2):235-286, 2001.   
[1140] J. Todd. On condition numbers. In *Programmation en Mathématiques Numériques*, Besançon, 1966, volume 7 (no. 165) of *Éditions Centre Nat. Recherche Sci.*, Paris, 1968, pages 141-159.   
[1141] John Todd. The condition of the finite segments of the Hilbert matrix. In Contributions to the Solution of Systems of Linear Equations and the Determination of Eigenvalues, Olga Taussky, editor, number 39 in Applied Mathematics Series, National Bureau of Standards, United States Department of Commerce, Washington, D. C., 1954, pages 109-116.   
[1142] John Todd. Computational problems concerning the Hilbert matrix. J. Res. Nat. Bur. Standards-B, 65(1):19-22, 1961.   
[1143] John Todd. Basic Numerical Mathematics, Vol. 2: Numerical Algebra. Birkhäuser, Basel, and Academic Press, New York, 1977. 216 pp. ISBN 0-12-692402-3.   
[1144] Kim-Chuan Toh and Lloyd N. Trefethen. Pseudozeros of polynomials and pseudospectra of companion matrices. Numer. Math., 68(3):403-425, 1994.   
[1145] Sivan Toledo. Locality of reference in LU decomposition with partial pivoting. SIAM J. Matrix Anal. Appl., 18(4):1065-1081, 1997.   
[1146] Virginia J. Torczon. Multi-Directional Search: A Direct Search Algorithm for Parallel Machines. PhD thesis, Rice University, Houston, TX, USA, May 1989. vii+85 pp.   
[1147] Virginia J. Torczon. On the convergence of the multidirectional search algorithm. SIAM J. Optim., 1(1):123-145, 1991.   
[1148] Virginia J. Torczon. On the convergence of pattern search algorithms. SIAM J. Optim., 7(1):1-25, 1997.

[1149] L. Tornheim. Maximum third pivot for Gaussian reduction. Technical report, Calif. Research Corp., Richmond, CA, 1965. Cited in [282].   
[1150] J. F. Traub. Associated polynomials and uniform methods for the solution of linear problems. SIAM Rev., 8(3):277-301, 1966.   
[1151] Lloyd N. Trefethen. Three mysteries of Gaussian elimination. ACM SIGNUM Newsletter, 20:2-5, 1985.   
[1152] Lloyd N. Trefethen. Approximation theory and numerical linear algebra. In Algorithms for Approximation II, J. C Mason and M. G. Cox, editors, Chapman and Hall, London, 1990, pages 336-360.   
[1153] Lloyd N. Trefethen. The definition of numerical analysis. SIAM News, 25:6 and 22, 1992. Reprinted in IMA Bulletin, 29 (3/4), pp. 47-49, 1993.   
[1154] Lloyd N. Trefethen. Pseudospectra of matrices. In Numerical Analysis 1991, Proceedings of the 14th Dundee Conference, D. F. Griffiths and G. A. Watson, editors, volume 260 of Pitman Research Notes in Mathematics, Longman Scientific and Technical, Essex, UK, 1992, pages 234-266.   
[1155] Lloyd N. Trefethen. Spectra and pseudospectra. In The Graduate Student's Guide to Numerical Analysis '98, Mark Ainsworth, Jeremy Levesley, and Marco Marletta, editors, Springer-Verlag, Berlin, 1999, pages 217-250.   
[1156] Lloyd N. Trefethen and David Bau III. Numerical Linear Algebra. Society for Industrial and Applied Mathematics, Philadelphia, PA, USA, 1997. xii+361 pp. ISBN 0-89871-361-7.   
[1157] Lloyd N. Trefethen and Robert S. Schreiber. Average-case stability of Gaussian elimination. SIAM J. Matrix Anal. Appl., 11(3):335-360, 1990.   
[1158] Lloyd N. Trefethen and Manfred R. Trummer. An instability phenomenon in spectral methods. SIAM J. Numer. Anal., 24(5):1008-1023, 1987.   
[1159] Henry S. Tropp. FORTRAN anecdotes. Annals of the History of Computing, 6 (1):59-64, 1984.   
[1160] Henry S. Tropp. Origin of the term bit. Annals of the History of Computing, 6 (2):152-155, 1984.   
[1161] Nai-kuan Tsao. A note on implementing the Householder transformation. SIAM J. Numer. Anal., 12(1):53-58, 1975.   
[1162] Nai-kuan Tsao. A simple approach to the error analysis of division-free numerical algorithms. IEEE Trans. Comput., C-32(4):343-351, 1983.   
[1163] Warwick Tucker. A rigorous ODE solver and Smale's 14th problem. Found. Comput. Math., 2(1):53-117, 2002.   
[1164] A. M. Turing. On computable numbers, with an application to the Entscheidungsproblem. Proc. London Math. Soc., 42:230-265, 1936.   
[1165] A. M. Turing. Proposal for development in the Mathematics Division of an Automatic Computing Engine (ACE). Report E.882, Executive Committee, National Physical Laboratory, Teddington, UK, 1945. Reprinted in [204, pp. 20-105] and [663, pp. 1-86].   
[1166] A. M. Turing. Rounding-off errors in matrix processes. Quart. J. Mech. Appl. Math., 1:287-308, 1948. Reprinted in [166] with summary and notes (including corrections).   
[1167] H. W. Turnbull. The Theory of Determinants, Matrices, and Invariants. Blackie, London and Glasgow, 1929. xvi+338 pp.

[1168] H. W. Turnbull and A. C. Aitken. An Introduction to the Theory of Canonical Matrices. Blackie, London and Glasgow, 1932. xiii+200 pp. Reprinted with appendix, 1952.   
[1169] Peter R. Turner. The distribution of leading significant digits. IMA J. Numer. Anal., 2:407-412, 1982.   
[1170] Peter R. Turner. Further revelations on L.S.D. IMA J. Numer. Anal., 4:225-231, 1984.   
[1171] Peter R. Turner. Will the "real" real arithmetic please stand up? Notices Amer. Math. Soc., 38(4):298-304, 1991.   
[1172] Evgenij E. Tyrtyshnikov. Cauchy-Toeplitz matrices and some applications. Linear Algebra Appl., 149:1-18, 1991.   
[1173] Patriot missile defense: Software problem led to system failure at Dhahran, Saudi Arabia. Report GAO/IMTEC-92-26, Information Management and Technology Division, United States General Accounting Office, Washington, D.C., February 1992. 16 pp.   
[1174] Minoru Urabe. Roundoff error distribution in fixed-point multiplication and a remark about the rounding rule. SIAM J. Numer. Anal., 5(2):202-210, 1968.   
[1175] J. V. Uspensky. Theory of Equations. McGraw-Hill, New York, 1948. vii+353 pp.   
[1176] A. van der Sluis. Condition numbers and equilibration of matrices. Numer. Math., 14:14-23, 1969.   
[1177] A. van der Sluis. Condition, equilibration and pivoting in linear algebraic systems. Numer. Math., 15:74-86, 1970.   
[1178] A. van der Sluis. Stability of the solutions of linear least squares problems. Numer. Math., 23:241-254, 1975.   
[1179] Charles F. Van Loan. A note on the evaluation of matrix polynomials. IEEE Trans. Automat. Control, AC-24(2):320-321, 1979.   
[1180] Charles F. Van Loan. On the method of weighting for equality-constrained least-squares problems. SIAM J. Numer. Anal., 22(5):851-864, 1985.   
[1181] Charles F. Van Loan. On estimating the condition of eigenvalues and eigenvectors. Linear Algebra Appl., 88/89:715-732, 1987.   
[1182] Charles F. Van Loan. Computational Frameworks for the Fast Fourier Transform. Society for Industrial and Applied Mathematics, Philadelphia, PA, USA, 1992. xiii+273 pp. ISBN 0-89871-285-8.   
[1183] Ursula van Rienen. Numerical Methods in Computational Electrodynamics: Linear Systems in Practical Applications. Number 12 in Lecture Notes in Computational Science and Engineering. Springer-Verlag, Berlin, 2001. xiii+375 pp. ISBN 3-540-67629-5.   
[1184] M. van Veldhuizen. A note on partial pivoting and Gaussian elimination. Numer. Math., 29:1-10, 1977.   
[1185] A. van Wijngaarden. Numerical analysis as an independent science. BIT, 6:66-81, 1966.   
[1186] Robert J. Vanderbei. Symmetric quasi-definite matrices. SIAM J. Optim., 5(1): 100-113, 1995.   
[1187] J. M. Varah. On the solution of block-tridiagonal systems arising from certain finite-difference equations. Math. Comp., 26(120):859-868, 1972.

[1188] J. M. Varah. A lower bound for the smallest singular value of a matrix. Linear Algebra Appl., 11:3-5, 1975.   
[1189] J. M. Varah. On the separation of two matrices. SIAM J. Numer. Anal., 16(2): 216-222, 1979.   
[1190] Richard S. Varga. On diagonal dominance arguments for bounding $\| A^{-1}\|_{\infty}$ . Linear Algebra Appl., 14:211-217, 1976.   
[1191] Richard S. Varga. Scientific Computation on Mathematical Problems and Conjectures. Society for Industrial and Applied Mathematics, Philadelphia, PA, USA, 1990. vi+122 pp. ISBN 0-89871-257-2.   
[1192] S. A. Vavasis. Gaussian elimination with partial pivoting is P-complete. SIAM J. Disc. Math., 2:413-423, 1989.   
[1193] Brigitte Verdonk, Annie Cuyt, and Dennis Verschaeren. A precision and range independent tool for testing floating-point arithmetic I: Basic operations, square root and remainder. ACM Trans. Math. Software, 27(1):92-118, 2001.   
[1194] Brigitte Verdonk, Annie Cuyt, and Dennis Verschaeren. A precision and range independent tool for testing floating-point arithmetic II: Conversions. ACM Trans. Math. Software, 27(1):119-140, 2001.   
[1195] Frank M. Verzuh. The solution of simultaneous linear equations with the aid of the 602 calculating punch. M.T.A.C., 3:453-462, 1949.   
[1196] J. Vignes and R. Alt. An efficient stochastic method for round-off error analysis. In Accurate Scientific Computations, Proceedings, 1985, Willard L. Miranker and Richard A. Toupin, editors, volume 235 of Lecture Notes in Computer Science, Springer-Verlag, Berlin, 1986, pages 183-205.   
[1197] D. Viswanath and L. N. Trefethen. Condition numbers of random triangular matrices. SIAM J. Matrix Anal. Appl., 19(2):564-581, 1998.   
[1198] Emil Vitasek. The numerical stability in solution of differential equations. In Conference on the Numerical Solution of Differential Equations, J. Ll. Morris, editor, volume 109 of Lecture Notes in Mathematics, Springer-Verlag, Berlin, 1969, pages 87-111.   
[1199] I. V. Viten'ko. Optimum algorithms for adding and multiplying on computers with a floating point. U.S.S.R. Computational Math. and Math. Phys., 8(5):183-195, 1968.   
[1200] John von Neumann and Herman H. Goldstine. Numerical inverting of matrices of high order. Bull. Amer. Math. Soc., 53:1021-1099, 1947. Reprinted in [1130, pp. 479-557].   
[1201] H. A. Van Der Vorst. The convergence behaviour of preconditioned CG and CG-S in the presence of rounding errors. In Preconditioned Conjugate Gradient Methods, Owe Axelsson and Lily Yu. Kolotilina, editors, volume 1457 of Lecture Notes in Mathematics, Springer-Verlag, Berlin, 1990, pages 126-136.   
[1202] Eugene L. Wachpress. Iterative solution of the Lyapunov matrix equation. Appl. Math. Lett., 1(1):87-90, 1988.   
[1203] Bertil Waldén, Rune Karlson, and Ji-guang Sun. Optimal backward perturbation bounds for the linear least squares problem. Numerical Linear Algebra with Applications, 2(3):271-286, 1995.   
[1204] Peter J. L. Wallis, editor. Improving Floating-Point Programming. Wiley, London, 1990. xvi+191 pp. ISBN 0-471-92437-7.

[1205] W. D. Wallis. Hadamard matrices. In Combinatorial and Graph-Theoretical Problems in Linear Algebra, Richard A. Brualdi, Shmuel Friedland, and Victor Klee, editors, volume 50 of IMA Volumes in Mathematics and Its Applications, Springer-Verlag, New York, 1993, pages 235-243.   
[1206] W. D. Wallis, Anne Penfold Street, and Jennifer Seberry Wallis. Combinatorics: Room Squares, Sum-Free Sets, Hadamard Matrices, volume 292 of Lecture Notes in Mathematics. Springer-Verlag, Berlin, 1972. 508 pp. ISBN 3-540-06035-9.   
[1207] Robert C. Ward. The QR algorithm and Hyman's method on vector computers. Math. Comp., 30(133):132-142, 1976.   
[1208] Willis H. Ware, editor. Soviet computer technology—1959. Comm. ACM, 3(3): 131-166, 1960.   
[1209] G. A. Watson. An algorithm for optimal $\ell_2$ scaling of matrices. IMA J. Numer. Anal., 11:481-492, 1991.   
[1210] J. H. M. Wedderburn. Lectures on Matrices, volume 17 of American Mathematical Society Colloquium Publications. American Mathematical Society, Providence, RI, USA, 1934. vii+205 pp.   
[1211] Per-Ake Wedin. Perturbation theory for pseudo-inverses. BIT, 13:217-232, 1973.   
[1212] Elias Wegert and Lloyd N. Trefethen. From the Buffon needle problem to the Kreiss matrix theorem. Amer. Math. Monthly, 101(2):132-139, 1994.   
[1213] Musheng Wei. Perturbation of the least squares problem. Linear Algebra Appl., 141:177-182, 1990.   
[1214] N. Weiss, G. W. Wasilkowski, H. Wožniakowski, and M. Shub. Average condition number for solving linear equations. Linear Algebra Appl., 83:79-102, 1986.   
[1215] Burton Wendroff. Theoretical Numerical Analysis. Academic Press, New York, 1966. xi+239 pp.   
[1216] Wilhelm Werner. Polynomial interpolation: Lagrange versus Newton. Math. Comp., 43(167):205-217, 1984.   
[1217] Joan R. Westlake. A Handbook of Numerical Matrix Inversion and Solution of Linear Equations. Wiley, New York, 1968.   
[1218] R. Clint Whaley, Antoine Petitet, and Jack J. Dongarra. Automated empirical optimization of software and the ATLAS project. Parallel Comput., 27(1-2):3-25, 2001.   
[1219] Michael White. Isaac Newton: The Last Sorcerer. Fourth Estate, London, 1997. 402 pp. ISBN 1-85702-706-X.   
[1220] B. A. Wichmann. Towards a formal specification of floating point. Comput. J., 32:432-436, 1989.   
[1221] B. A. Wichmann. A note on the use of floating point in critical systems. Comput. J., 35(1):41-44, 1992.   
[1222] M. V. Wilkes. Arithmetic on the EDSAC. IEEE Annals of the History of Computing, 19(1):13-15, 1997.   
[1223] J. H. Wilkinson. The Automatic Computing Engine at the National Physical Laboratory. Proc. Roy. Soc. London Ser. A, 195:285-286, 1948.   
[1224] J. H. Wilkinson. Progress report on the Automatic Computing Engine. Report MA/17/1024, Mathematics Division, Department of Scientific and Industrial Research, National Physical Laboratory, Teddington, UK, April 1948. 127 pp.

[1225] J. H. Wilkinson. Linear algebra on the Pilot ACE. In Automatic Digital Computation, Her Majesty's Stationery Office, London, 1954. Reprinted in [1248, pp. 337-344].   
[1226] J. H. Wilkinson. The Pilot ACE. In Automatic Digital Computation, Her Majesty's Stationery Office, London, 1954, pages 5-14. Reprinted in [99, pp. 193-199] and [1248, pp. 219-228].   
[1227] J. H. Wilkinson. The use of iterative methods for finding the latent roots and vectors of matrices. Mathematical Tables and Other Aids to Computation, 9:184-191, 1955.   
[1228] J. H. Wilkinson. Error analysis of floating-point computation. Numer. Math., 2: 319-340, 1960.   
[1229] J. H. Wilkinson. Error analysis of direct methods of matrix inversion. J. Assoc. Comput. Mach., 8:281-330, 1961.   
[1230] J. H. Wilkinson. Error analysis of eigenvalue techniques based on orthogonal transformations. J. Soc. Indust. Appl. Math., 10(1):162-195, 1962.   
[1231] J. H. Wilkinson. Plane-rotations in floating-point arithmetic. In Experimental Arithmetic, High Speed Computing and Mathematics, volume 15 of Proceedings of Symposia in Applied Mathematics, American Mathematical Society, Providence, RI, USA, 1963, pages 185-198.   
[1232] J. H. Wilkinson. *Rounding Errors in Algebraic Processes.* Notes on Applied Science No. 32, Her Majesty's Stationery Office, London, 1963. vi+161 pp. Also published by Prentice-Hall, Englewood Cliffs, NJ, USA. Reprinted by Dover, New York, 1994. ISBN 0-486-67999-3.   
[1233] J. H. Wilkinson. The Algebraic Eigenvalue Problem. Oxford University Press, 1965. xviii+662 pp. ISBN 0-19-853403-5 (hardback), 0-19-853418-3 (paperback).   
[1234] J. H. Wilkinson. Error analysis of transformations based on the use of matrices of the form $I - 2ww^{H}$ . In Error in Digital Computation, Louis B. Rall, editor, volume 2, Wiley, New York, 1965, pages 77-101.   
[1235] J. H. Wilkinson. Bledy Zaokraglen w Procesach Algebraicznych. PWW, Warszawa, 1967. Polish translation of [1232].   
[1236] J. H. Wilkinson. A priori error analysis of algebraic processes. In Proc. International Congress of Mathematicians, Moscow 1966, I. G. Petrovsky, editor, Mir Publishers, Moscow, 1968, pages 629-640.   
[1237] J. H. Wilkinson. *Rundungsfehler*. Springer-Verlag, Berlin, 1969. German translation of [1232].   
[1238] J. H. Wilkinson. The Algebraic Eigenvalue Problem. Nauka, U.S.S.R. Academy of Sciences, 1970. 564 pp. Russian translation of [1233].   
[1239] J. H. Wilkinson. Modern error analysis. SIAM Rev., 13(4):548-568, 1971.   
[1240] J. H. Wilkinson. Some comments from a numerical analyst. J. Assoc. Comput. Mach., 18(2):137-147, 1971. Reprinted in [3].   
[1241] J. H. Wilkinson. The classical error analyses for the solution of linear systems. IMA Bulletin, 10(5/6):175-180, 1974.   
[1242] J. H. Wilkinson. Numerical linear algebra on digital computers. IMA Bulletin, 10(9/10):354-356, 1974.

[1243] J. H. Wilkinson. Turing's work at the National Physical Laboratory and the construction of Pilot ACE, DEUCE, and ACE. In A History of Computing in the Twentieth Century: A Collection of Essays, N. Metropolis, J. Howlett, and Gian-Carlo Rota, editors, Academic Press, New York, 1980, pages 101-114.   
[1244] J. H. Wilkinson. The state of the art in error analysis. In NAG Newsletter 2/85, Numerical Algorithms Group, Oxford, UK, November 1985, pages 5-28.   
[1245] J. H. Wilkinson. Error analysis revisited. IMA Bulletin, 22(11/12):192-200, 1986.   
[1246] J. H. Wilkinson and C. Reinsch, editors. Linear Algebra, volume II of Handbook for Automatic Computation. Springer-Verlag, Berlin, 1971. ix+439 pp. ISBN 3-540-05414-6.   
[1247] James H. Wilkinson. The perfdigious polynomial. In Studies in Numerical Analysis, G. H. Golub, editor, volume 24 of Studies in Mathematics, Mathematical Association of America, Washington, D.C., 1984, pages 1-28.   
[1248] M. R. Williams and Martin Campbell-Kelly, editors. The Early British Computer Conferences, volume 14 of Charles Babbage Institute Reprint Series for the History of Computing. MIT Press, Cambridge, MA, USA, 1989. xvi+508 pp. ISBN 0-262-23136-0.   
[1249] S. Winograd. A new algorithm for inner product. IEEE Trans. Comput., C-18: 693-694, 1968.   
[1250] S. Winograd. On multiplication of $2 \times 2$ matrices. Linear Algebra Appl., 4:381-388, 1971.   
[1251] Jack Woehr. A conversation with William Kahan. *Dr. Dobb's Journal*, 271:18-32, 1997.   
[1252] Jack M. Wolfe. Reducing truncation errors by programming. Comm. ACM, 7(6): 355-356, 1964.   
[1253] Stephen Wolfram. The Mathematica Book. Fourth edition, Wolfram Media, Champaign, IL, USA and Cambridge University Press, Cambridge, UK, 1999. xxvi+1470 pp. ISBN 1-57955-004-5 (Wolfram), 0-521-64314-7 (Cambridge).   
[1254] Michael Woodger. The history and present use of digital computers at the National Physical Laboratory. Process Control and Automation, pages 437-442, 1958. Reprinted in [204, pp. 125-140].   
[1255] H. Wozniakowski. Numerical stability for solving nonlinear equations. Numer. Math., 27:373-390, 1977.   
[1256] H. Wozniakowski. Numerical stability of the Chebyshev method for the solution of large linear systems. Numer. Math., 28:191-209, 1977.   
[1257] H. Wozniakowski. Roundoff-error analysis of iterations for large linear systems. Numer. Math., 30:301-314, 1978.   
[1258] H. Wozniakowski. Roundoff-error analysis of a new class of conjugate-gradient algorithms. Linear Algebra Appl., 29:507-529, 1980.   
[1259] Margaret H. Wright. Interior methods for constrained optimization. Acta Numerica, pages 341-407, 1992.   
[1260] Margaret H. Wright. Direct search methods: Once scorned, now respectable. In Numerical Analysis 1995, Proceedings of the 16th Dundee Conference, D. F. Griffiths and G. A. Watson, editors, volume 344 of Pitman Research Notes in Mathematics, Addison Wesley Longman, Harlow, Essex, UK, 1996, pages 191-208.

[1261] Stephen J. Wright. A collection of problems for which Gaussian elimination with partial pivoting is unstable. SIAM J. Sci. Statist. Comput., 14(1):231-238, 1993.   
[1262] Stephen J. Wright. *Primal-Dual Interior-Point Methods*. Society for Industrial and Applied Mathematics, Philadelphia, PA, USA, 1997. xx+289 pp. ISBN 0-89871-382-X.   
[1263] P. Y. Yalamov. Graphs and stability of algorithms. Preprint N27, University of Rousse, Bulgaria, February 1995. 17 pp.   
[1264] Plamen Y. Yalamov. On the almost strong stability of the circular deconvolution algorithm. SIAM J. Matrix Anal. Appl., 22(2):358-363, 2000.   
[1265] Man-Chung Yeung and Tony. F. Chan. Probabilistic analysis of Gaussian elimination without pivoting. SIAM J. Matrix Anal. Appl., 18(2):499-517, 1997.   
[1266] E. L. Yip. A note on the stability of solving a rank- $p$ modification of a linear system by the Sherman-Morrison-Woodbury formula. SIAM J. Sci. Statist. Comput., 7 (3):507-513, 1986.   
[1267] J. M. Yohe. Implementing nonstandard arithmetics. SIAM Rev., 21(1):34-56, 1979.   
[1268] J. M. Yohe. Software for interval arithmetic: A reasonably portable package. ACM Trans. Math. Software, 5(1):50-63, 1979.   
[1269] J. M. Yohe. Portable software for interval arithmetic. Computing, Suppl. 2:211-229, 1980.   
[1270] David M. Young. Iterative Solution of Large Linear Systems. Academic Press, New York, 1971. xxiv+570 pp. ISBN 0-12-773050-8.   
[1271] David M. Young. A historical overview of iterative methods. Computer Physics Communications, 53:1-17, 1989.   
[1272] David M. Young and Robert T. Gregory. A Survey of Numerical Mathematics, volume 1. Addison-Wesley, Reading, MA, USA, 1972. x+492+appendices pp. Reprinted by Dover, New York, 1988. ISBN 0-486-65691-8.   
[1273] Tjalling J. Ypma. The effect of rounding errors on Newton-like methods. IMA J. Numer. Anal., 3:109-118, 1983.   
[1274] Tjalling J. Ypma. Finding a multiple zero by transformations and Newton-like methods. SIAM Rev., 25(3):365-378, 1983.   
[1275] Tjalling J. Ypma. Historical development of the Newton-Raphson method. SIAM Rev., 37(4):531-551, 1995.   
[1276] Gideon Yuval. A simple proof of Strassen's result. Inform. Process. Lett., 7(6): 285-286, 1978.   
[1277] Adam T. Zawilski. Numerical stability of the cyclic Richardson iteration. Numer. Math., 60:251-290, 1991.   
[1278] Hongyuan Zha. A componentwise perturbation analysis of the $QR$ decomposition. SIAM J. Matrix Anal. Appl., 14(4):1124-1131, 1993.   
[1279] Hongyuan Zha. Problem 10312. Amer. Math. Monthly, 100(5):499, 1993.   
[1280] Hongyuan Zha and Zhenyue Zhang. A note on constructing a symmetric matrix with specified diagonal entries and eigenvalues. BIT, 35:448-452, 1995.   
[1281] G. Zielke. Report on test matrices for generalized inverses. Computing, 36:105-162, 1986.

[1282] Gerhard Zielke. Some remarks on matrix norms, condition numbers, and error estimates for linear equations. Linear Algebra Appl., 110:29-41, 1988.   
[1283] K. Zietak. On a particular case of the inconsistent linear matrix equation $AX + YB = C$ . Linear Algebra Appl., 66:249-258, 1985.   
[1284] Abraham Ziv. Relative distance—An error measure in round-off error analysis. Math. Comp., 39(160):563-569, 1982.   
[1285] Abraham Ziv. Fast evaluation of elementary mathematical functions with correctly rounded last bit. ACM Trans. Math. Software, 17(3):410-423, 1991.   
[1286] Abraham Ziv. Converting approximate error bounds into exact ones. Math. Comp., 64(209):265-277, 1995.   
[1287] Zahari Zlatev, Jerzy Wasniewski, and Kjeld Schaumburg. Condition number estimators in a sparse matrix software. SIAM J. Sci. Statist. Comput., 7(4):1175-1189, 1986.

# Name Index

Science is organized knowledge.

— HERBERT SPENCER, Essays On Education (1861)

A suffix "t" after a page number denotes a table, "f" a figure, "n" a footnote, and "q" a quotation.

Aasen, Jan Ole, 214, 222, 224, 227

Abdelmalek,NabihN.,376,403

Abramowitz,Milton,30

Acton,FormanS.,30,195q,283q,486

Adams, Duane A., 103

Aelfric,xxiq

Aggarwal,VijayB.,76

Ahac,AlanA.,190

Ahlberg,J.H.,154

Aitken, Alexander Craig, 91, 374

Albers, Donald J., 511n

Alefeld, Goltz, 483

Alexopolous, Aristides G., 49

Allen, Jr., Richard C., 76

Almacany, Montaha, 415q

Alt,H.,447

Aluru, Srinivas, 446

Alvarado, Fernando L., 153

Amato,JamesJ.,317

Amodio, Pierluigi, 190

Anda, Andrew A., 376

Anderson, Edward, 287q, 397, 404

Anderson,IainJ.,88

Anderson, T. W., 524, 525

Ando,T.,188

Antonov,A.G.,285

Arioli, Mario, 130, 301, 324, 337, 402-404, 413, 414

Arnold, William F., 318

Ashcraft,Cleve,188,219,227

Ashenhurst, R. L., 486

Asplund,Edgar,302

Atanasoff, John V., 139q

Axelsson,Owe,337

Babuska,Ivo,90

Bachelis,Boris,50

Bai,Zhaojun,317,346,397,404,524

Bailey, David H., 436, 446-448, 457, 478, 489 q, 501, 502

Baksalary,J.K.,318

Balle,SusanneM.,448

Ballester, C., 429

Bank,RandolphE.,257

Bareiss,E.H.,49,189

Bargmann,V.,183

Barlow, Jesse L., 29, 47, 49, 181, 189, 299, 376, 397

Barnett,S.,317

Barone, John L., 381 q, 402

Barrett,Geoff,56

Barrlund, Anders, 181, 190, 209, 405

Bartels, R. H., 307

Bartels, Sven G., 129, 301, 429

Bau III, David, 169, 337

Bauer, F. L., 53, 76, 107, 114, 127, 133, 135, 177, 281, 547

Beam, Richard M., 525

Beaton, Albert E., 381 q, 402

Bell, E. T., 279 q

Bellman, Richard, 318

Benford, Frank, 47

Benoit,Commandant,209

Benschop,N.F.,323

Berman, Abraham, 133, 152

Bhatia,Rajendra,317,374

Bini, Dario, 429, 443, 444

Birkhoff, Garrett, 279, 479

Bischof, Christian H., 297-299, 363, 376

Björck, Åke, 76, 241, 353q, 371, 375-377, 379, 380, 386, 388, 389, 391, 391q, 392, 399, 402-405, 413, 414, 423, 423q, 425, 429, 565

Bjørstad,Petter,448

Blanch, G., 505

Bliss,B.,485

Blue,JamesL.,499

Bodewig,E.,185

Bohlender,Gerd,88

Bohte, Z., 173

Boley, Daniel, 242

Bollen, Jo A. M., 323

Bondeli,S.,522

Boros,T.,429

Borwein, J. M., 489q

Borwein,P.B.,489q

Bowden,B.V.,195q

Bowdler,H.J.,188

Boyd, David W., 289, 291, 301

Boyle, Jeff, 47

Brent, Richard P., 47, 150, 151, 436, 439, 440, 447, 483, 501, 505

Brezinski, Claude, 209

Briggs, William L., 456

Brightman, Tom, 56

Brown, W. S., 495, 498, 498 q

Brunet, Marie-Christine, 485, 486

Buchan, John, 57q

Buchanan,JamesL.,152

Buchholz,W.,56

Bukhberger,B.,302

Bulirsch,R.,76,187

Bunch, James R., 129, 133, 136, 213 q, 215, 216, 221, 225-227, 231 q

Buoni, John J., 190

Burdakov,Oleg,282

Burgmeier,JamesW.,76

Businger, Peter A., 133, 180, 403

Butcher, J. C., 90

Byers, Ralph, 302, 315, 318, 319, 346, 562

Caffney, John, 518

Calvetti, D., 428-430

Calvin (and Hobbes), 471q

Campbell, S. L., 332

Campbell-Kelly, Martin, 245q

Cao, Wei-Lu, 302

Caprani,Ole,90

Cardano, Geronimo, 479

Carr III, John W., 53

Carter, Russell, 493, 494

Cauchy, Augustin-Louis, 515

Cayley,Arthur,434

Chaitin-Chatelin, Françoise, 351, 468, 485, 486

Chan, N. N., 524

Chan, Raymond H., 457

Chan, Tony F., 11q, 29, 133, 134, 189, 377

Chandrasekaran, Shivkumar, 123, 129, 377

Chang, Xiao-Wen, 190, 209, 377

Chartres, Bruce A., 186

Chatelin, Françoise, see Chaitin-Chatelin, Françoise

Cheng, Sheung Hun, 219, 221, 224, 227, 295

Cho, Choong Yun, 515

Choi, Man-Duen, 511q, 523

Cholesky, André-Louis, 209

Christiansen, Soren, 133

Chu,Eleanor,181

Chu, King-wah Eric, 318

Chu, Moody T., 525

Clasen,B.-I.,281

Clenshaw,C.W.,49,102

Cline,AlanK.,287q,295,297,404

Cline, R. E., 413

Clinger,WilliamD.,57

Codenotti,B.,282

Cody, Jr., William J., 51, 55, 56, 493, 495, 496, 501 q

Cohen,A.M.,169,170,520

Concus,P.,257

Conn, Andrew R., 297

Conte,SamuelD.,187

Cooley,JamesW.,456

Coomes, Brian A., 29

Coonen, Jerome T., 55, 493

Cope,J.E.,132

Coppersmith, Don, 436

Cortés, Joaquín, 189

Cottle, Richard W., 209

Cox, Anthony J., 362, 375, 395, 396, 398, 400, 404, 405

Crout, Prescott D., 187

Cryer, Colin W., 169, 170, 188, 189

Csanky,L.,278

Curtis,A.R.,190

Cuyt, Annie, 496

Cybenko, George, 210

Dahlquist, Germund, 76, 147

Daniel,J.W.,376

Datta, Karabi, 311

Davies, Philip I., 525

Davis, Philip J., 90, 457

Dax,Achiya,227,332

Day, David, 524

Day, Jane M., 189

deBoor,Carl,186-188

de Jong,Lieuwe Sytse,29

de Rijk, P. P. M., 402-404

Dekker,T.J.,53,84,282,501

del Ferro, Scipione, 479

Demeure, Cédric J., 429

Dennel, James W., 42, 49, 56, 57, 77, 90, 115, 128-130, 136, 152, 182, 188, 191, 198-200, 209, 232, 242, 249-253, 256, 257, 282, 288, 301, 317, 337, 346, 409, 413, 414, 483, 492, 496, 501, 515, 524, 534

Dennis, Jr., John E., 323, 468, 475, 476

Descloux,J.,469

Dhillon, Inderjit S., 56, 301, 304, 534

Diament, Benjamin, 288

Diamond, Harold G., 57

Dixon,John D.,298

Dongarra, Jack J., 185, 187, 226, 231 q, 232, 256, 397, 404, 496, 524, 573 q

Doolittle, Myrick Hascall, 187

Dorn, William S., 76, 90, 102

Douglas,CraigC.,446,569

Douglas, Jr., Jim, 185

Doyle, Sir Arthur Conan, 287 q

Drake, J. B., 259q

Drmac,Zlatko,210

Du Croz, Jeremy J., 262, 269, 281

Dubrulle, Augustin A., 282, 507

Duff,IainS.,131,187,193,226,227 256,301,337,402-404,524

Dumitrescu, Bogdan, 447

Duncan, Martin, 87

Dunham, C. B., 415q

Dwyer,PaulS.,157q

Eckart, Carl, 114

Edelman,Alan，59，150，169，170，189 191,284,377,480n,516,516q 524,532

Egecioglu, Omer, 103

Eijkhout, Victor, 232

Eirola, Timo, 29

Eldén,Lars,396,404

Eldersveld, Samuel K., 257

Elfving, Tommy, 429

Emel'yanenko, G. A., 302

Enright, Wayne H., 29

Erisman,A.M.,180,181,186,193

Espelid, Terje O., 90

Faddeeva, V. N., 188

Fairgrieve, Thomas F., 50, 528

Fallat, Shaun M., 189

Fan, Ky, 377

Farebrother, R. W., 402

Farkas,I.,103

Farnum, Charles, 494, 494q

Fateman, Richard J., 55

Feingold, David G., 257

Feldstein,A.,57

Ferguson,H.R.P.,448,478

Ferguson, Jr., Warren E., 45, 56

Ferng, William R., 299

Fike, C. T., 93q, 104

Fischer, Patrick C., 446

Flannery, Brian P., 476, 487, 505

Fletcher, Roger, 133, 136, 188, 210, 227

Forsgren, Anders, 210, 226

Forsythe, George E., 29, 29q, 30, 48, 53, 76, 86, 126, 133, 152, 186, 188, 190, 235, 240, 242, 245 q, 259 q, 260, 279, 302, 321 q, 489 q, 523

Foster, Leslie V., 159, 167, 170, 403

Foulser, David E., 133, 134

Fox,L.,xxixq,xxx,30,31q,105n,184 186

Francois, Philippe, 32

Frayssé,Valérie,351,468,486

Friedland,Shmuel,342,352

Frommer, Andreas, 482

Funderlic, R. E., 190

Gaches,J.,120,132

Gahinet, Pascal M., 318

Gal,Shmuel,50

Gallivan, K. A., 180

Gallopoulos,E.,103,485

Gander, Walter, 522

Gantmacher, F. R., 161

Gardiner, Judith D., 317, 318

Gardner, Martin, 115q

Garner, Harvey L., 57

Gasca,M.,180,189

Gastinel, Noel, 111, 114

Gauss, Carl Friedrich, 1 q, 187, 215, 321 q, 381, 456

Gautschi, Walter, 415q, 419

Gautschi,Werner,344

Gay, David M., 57

Geist, G. A., 259q

Geman, Stuart, 516

Gentle,JamesE.,29

Gentleman，W.Morven，103,375,376 456,570

George,Alan,181,209

Geuder,JamesC.,186

Ghavimi, Ali R., 315-317

Gill, Philip E., 210, 226, 227, 229, 413, 476

Gill,S.,83

Givens, Wallace J., 29, 61q

Gluchowska, J., 404

Godunov,S.K.,285

Gohberg,I.,128,129,428

Goldberg, David, 35q, 53, 85, 532

Goldberg,I.Bennett,57

Goldstine,HermanH.,1n,29,48,183 184，188，259q，260,515

Golub, Gene H., xxviii, 11 q, 24, 29, 115, 132, 133, 172, 187, 208, 231 q, 256, 257, 282, 299, 307, 308, 308 n, 323, 345, 375, 377, 380-382, 389, 399, 402-405, 429

Goodman,R.,57

Goodnight,JamesH.,282

Gould, Nicholas I. M., 170, 189

Govaerts,WillyJ.F.,241

Gragg,W.B.,295,376

Graham, Ronald L., 79q, 518q

Greenbaum, Anne, 324, 337

Gregory, Robert T., 29, 512, 522

Griewank, Andreas, 469

Grimes, Roger G., 188, 219, 227, 302, 524

Grosse, Eric, 573q

Gu,Ming,346,404,406,534

Gudmundsson,Thorkell,298

Guggenheimer, Heinrich W., 284

Gulliksson,Marten,405

Gustafson,JohnL.,446

Gustavson,F.G.,187

Hager, William W., 292, 301

Hall, Jr., Marshall, 168

Halmos,PaulR.,511q

Hamada,Hozumi,49

Hammarling,SvenJ.,317,322,323,376 397，500

Hamming,R.W.,53,431

Hansen, Per Christian, 133, 377, 448

Hanson, Richard J., 375, 376, 399, 402, 403, 414, 499

Harter, Richard, 446

Hartfiel, D. J., 132

Hauser, John R., 57, 59

Hearon,JohnZ.,311

Heath, Michael T., 259q, 388

Hedayat,A.S.,168

Hein,Piet,31q,115q

Helvin, Marie, 153 q

Henderson, Harold V., 317, 487

Hennessy, John L., 35 n, 53

Henrici, Peter, 48, 49, 61q, 77, 344

Henson, Van Emden, 456

Heroux, Michael, 446, 569

Herzberger, Jirgen, 483

Hewer, Gary, 318

Higham, Desmond J., 114, 128, 129, 136, 167, 187, 339 q, 342, 394, 429

Higham, Nicholas J., 65, 90, 128, 129, 132, 151-153, 167, 187, 190, 210, 219, 227, 228, 240-242, 249-253, 256, 257, 262, 269, 278, 281, 292, 294, 295, 298, 301-304, 317, 324, 347, 349, 351, 362, 375, 377, 378, 380, 394-396, 398, 400, 402-405, 40 413, 414, 429, 431, 446-448, 486, 505, 523, 525, 564, 569, 571

Hilbert, David, 523

Hildebrand,F.B.,28,35q

Hodel,A.Scottedward,317

Hodges, Andrew, xxix

Hoffman,A.J.,377

Hoffmann, Christoph M., 29

Hoffmann,W.,281,282,376

Hooper, Judith A., 501

Horn, Roger A., 107, 115, 137, 152, 306, 342, 543, 547, 551, 554

Horning, Jim, 489 q

Hotelling, Harold, 183, 433q

Hough, David, 43, 506, 507

Hough, Patricia D., 395

Householder, Alston S., 2, 105q, 115, 147, 161, 374, 403, 560

Hull, T. E., 48, 50, 485, 485 q, 503, 528

Hunt, Julian, 54

Huskey,H.D.,184

Hyman,M.A.,280

Ikebe,Yasuhiko,300,302,304

Ikramov, Khakim D., 209, 525

Incertis,F.,509

Ipsen, Ilse C. F., 123, 129, 133, 376, 377

Iri, Masao, 49, 485

Isaacson,Eugene,186,257

Jalby, William, 376

Jankowski, M., 85, 240, 241

Jansen,Paul,483

Jennings,A.,152

Jennings,L.S.,413

Johnson, Charles R., 107, 115, 137, 152, 284, 306, 342, 543, 547, 551, 554

Johnson,Samuel,667

Jones,MarkT.,227

Jones,WilliamB.,505

Jordan, Camille, 281

Jordan, T. L., 402

Jordan, Wilhelm, 281

Kagstrom,Bo,302,315,316,318

Kahan, William M. (Velvel), 1q, 26, 29, 30, 32, 42, 43 q, 44 q, 45, 47 q, 49, 55, 58, 59 q, 60, 69, 78, 83-86, 88, 103, 111, 114, 124, 149, 152, 157 q, 226, 242, 404, 483, 486, 491 q, 494-496, 498 q, 499, 504

Kahaner, David K., 381q

Kailath,T.,429

Kala,R.,318

Kaniel,S.,227

Kaporin,Igor,447

Karasalo, Ilkka, 152

Karatsuba,A.,447

Karlin,Samuel,520

Karlson,Rune,392,404,406

Karney, David L., 512, 522

Karp,A.,187

Karpinski, Richard, 52, 495

Kato, Tosio, 115

Kaufman, Linda, 213q, 216, 226, 227, 376

Kaufmann, Matt, 56

Kearfott, R. Baker, 483

Keiper, Jerry B., 31

Keller, Herbert Bishop, 186, 257, 321 q

Kelley, C. T., 468, 476

Kennedy, Jr., William J., 29

Kenney, Charles S., 298, 318, 523

Kerr, Thomas H., 210

Kielbasinski,Andrzej，77，85，209，241393，404，410，414

Kincaid,D.R.,499

Kiriljuk,O.P.,285

Kittaneh, Fuad, 523

Knight, Philip A., 324, 347, 349, 351, 447, 448

Knuth, Donald E., xxiii, xxviii, 49, 53, 54, 61 q, 79 q, 84, 85, 104, 447, 471 q, 489 q, 518 q, 523, 532

KoC, C K., 103

Kocak,Huseyin,29

Koltracht,I.,128,129

Körner, T. W., 451 q

Kornerup, Peter, 49

Kosowski,Przemyslaw,525

Kostin,V.I.,285

Kostlan, Eric, 516, 524

Kovarik,Z.V.,132

Kowalewski, G., 428

Krasny, Robert, 502

Kreczmar, Antoni, 446

Krogh,F.T.,499

Krückerberg,F.,191

Kubota, Koichi, 485

Kucherov, Andrey B., 209

Kuczyński, J., 298

Kuki,H.,56

Kulisch, Ulrich W., 483

Kuperman,I.B.,132

LaPorte,M.,486

La Touche, Mrs., 79 q, 80

Laderman, Julian, 437, 446

Lagrange, Joseph Louis, 215

Lancaster, Peter, 317, 468

Lanczos, Cornelius, 486

Langlois, Philippe, 484

Laratta,A.,413,414

Larson, John L., 485

Larsson,S.,29

Laszlo,Lajos,345

Laub,AlanJ.,298,315-318,523

Lauchli, Peter, 379

Lawson, Charles L., 375, 376, 399, 402, 403, 414, 499

LeBlanc,E.,483

Lee, King, 446, 447

Lefevre, Vincent, 50

Lehmer,D.H.,527

Lehoucq, Richard B., 563

Lemeire, Frans, 152

Leoncini,M.,282

Leuprecht,H.,88

LeVeque, Randall J., 11q, 29

Lewis, John G., 29, 188, 219, 227, 299, 302, 524

Lewis, Robert Michael, 472

Li, Kim-Hung, 524

Li, T. Y., 282

Li, Xiaoye S., 232, 492

Lickteig, Thomas, 447

Linnainmaa, Seppo, 49, 76, 84, 90, 501

Linz,Peter,90

Linzer, Elliot, 456

Liu, Joseph W. H., 209, 227

Longley,JamesW.,402

Lotti, Grazia, 443, 444

Lu,Hao,429

Luszczek,Piotr,232

Lynch, Thomas W., 56

Lyness,J.N.,429

Lynn, M. Stuart, 323

MacLane,Saunders,479

Macleod, Allan J., 189

Makhoul, John, 210

Malajovich, Gregorio, 288

Malcolm, Michael A., 29, 86, 88, 188, 245 q, 260, 302, 495, 506, 522

Malyshev, Alexander N., 152, 282, 404, 405

Manne,F.,448

Manteuffel, Thomas A., 152

Marovich, Scott B., 570

Martin,R.S.,188

Mascarenhas,Walter,189

Mathias,Roy,152,208,377,514

Matsui, Shouichi, 49

Mattheij,R.M.M.,257

Matula, David W., 49, 53, 57

Mazzia, Francesca, 190

McCarthy, Charles, 133

McCracken, Daniel D., 76, 90, 102

McKeeman, William Marshall, 188, 240

McKenney,Alan,317,524

McKinnon, K. I. M., 476

Mead,J.L.,180

Meinguet, Jean, 209, 281

Mendelsohn,N.S.,283

Metropolis,N.,486

Meurant, Gérard, 257, 302

Meyer, Jr., Carl D., 133, 332

Milenkovic, Victor J., 29

Miller,D.F.,317

Miller, Webb, 76, 104, 438, 441, 471q, 484, 485, 504, 515, 570

Miranker, Willard L., 483

Mirsky,L.,554

Moler, Cleve B., 29, 30, 55, 76, 86, 152, 186, 188, 190, 231 q, 235, 240, 242, 245 q, 259 q, 260, 279, 295, 302, 317, 339 q, 342, 352, 381 q, 407 q, 429, 500, 505, 507, 523

Møller,Ole,83

Montgomery, D., 183

Moore,J.Strother,56

Moore,RamonE.,483

Morrison, Donald, 500, 507

Mukherjea, Kalyan, 374

Muller, Jean-Michel, 32, 50

Muller, K. H., 102

Murakami, H., 480 n

Murray, Walter, 210, 226, 227, 413, 476

Nash, Stephen G., 308, 319, 381q, 562

Nashed, M. Zuhair, 402

Neal, Larry, 188

Neumaier,A.,57,85

Neumann,M.,190

Newbery,A.C.R.,102,103

Newcomb, Simon, 47

Newman, Morris, 512, 518

Ng, Michael K., 457

Nickel, Karl, 85, 482 q, 483

Nilson,E.N.,154

Nocedal, Jorge, 226, 468

Nordio, Marcelo, 189

Notay, Yvan, 324

Oberaigner, W., 88

O'Cinneide, Colm Art, 133

Oettli,W.,122,132

Ofman,Yu.,447

O'Leary, Dianne Prost, 302

Olesky, D. D., 190

Oliver,J.,103,428

Olkin, Ingram, 524, 525

Olshevsky,V.,428,429

Olver,F.W.J.,49,69,77,102,187

Omladic,Matjaž,210

Opfer, Gerhard, 429

Ortega,JamesM.,376

Osborne,M.R.,413

Ostrowski,A.M.,344,543

Overton, Michael L., 35q

Paige, Christopher C., 190, 209, 371, 376, 377, 380, 386, 397, 403, 404, 407 q, 413, 414, 565

Palmer,John,522

Palmer, Kenneth J., 29

Pan, Ching-Tsuan, 183

Pan, Victor Y., 278, 282, 429, 436, 437, 446

Papadimitriou, Pythagoras, 377

Papadopoulos, Philip M., 318

Parhami,Behrooz,56

Park, Haesun, 376

Parlett, Beresford N., xxviii, xxx, 24, 30, 55, 76, 79 q, 184, 215, 226, 353 q, 375, 376

Pasternak, Mary E., 485

Patashnik,Oren,79q,518q

Paterson, Michael S., 102

Patrick, Merrell L., 227

Patterson, David A., 35 n, 53

Paxson,Vern,57

Pelz, Richard, 502

Pena,J.M.,152,179,180,189,190

Penzl, Thilo, 317

Percival, Colin, 457

Pereyra, Victor, 423, 423q, 425, 429

Peters, G., 103, 188, 275, 281, 282, 404

Peterson, Brian, 189

Philippe, Bernard, 376

Pichat,M.,88

Pierce, Daniel J., 299

Pinkus, Allan, 186, 188

Plemmons, Robert J., 133, 152, 180, 190, 299, 332, 404, 413

Poljak, Svatopluk, 128

Polman,Ben,257

Ponceleón, Dulce B., 227

Poole, George, 188

Poromaa,Peter,302,315,318

Pothen, Alex, 153

Powell, M. J. D., 210, 362, 375, 395, 404, 472, 474

Power, Stephen, 209

Prager,W.,122,132

Preparata,F.P.,282

Press,WilliamH.,476,487,505

Priest, Douglas M., 28, 29, 54, 87-89, 92, 499, 501, 529

Pryce,J.D.,69,241

Puglisi,Chiara,365

Pukelsheim, Friedrich, 317

Puschmann, Heinrich, 189

Quinlan, Gerald D., 87

Quinn, Thomas R., 87

Quintana,EnriqueS.,282

Quintana, Gregorio, 282

Rabinowitz, Philip, 90

Raimi,RalphA.,48

Rall, Louis B., 402, 483, 485

Ramos, George U., 456

Rath, Wolfgang, 376

Ratz,H.C.,323

Razaz,M.,102

Reese,M.S.,298

Reichel,Lothar,103,350,428-430,525

Reichelt,MarkW.,524

Reid, John K., 180, 181, 186, 190, 193, 227, 362, 375, 395, 400, 404

Reinsch,C.,xxix,281,577q

Reiser,JohnF.,54

Ren,Huan,56

Renaut, R. E., 180

Rew,R.K.,287q,297

Rheinboldt,WernerC.,467,467q

Rice,John R.,29,376

Rigal,J.L.,120,132

Robertazzi,T.G.,89

Roberts, J. D., 317

Rohn,Jiri,116,128,135

Romani, Francesco, 324

Rose, Donald J., 257

Rosenthal, Peter, 317

Ross,D.R.,88

Rowan, Thomas Harvey, 485, 486

Rubin, Donald B., 381 q, 402

Ruhe, Axel, 376

Ruiz, Daniel, 337

Rump,SiegfriedM.,127-129,191,482 483

Russoinoff, David M., 56

Rust,B.W.,132

Rutishauser,Heinz,512,518

Sadkane,Miloud,404

Sameh, Ahmed H., 150, 151, 180, 485

Samelson,Klaus,53

Sande,G.,456

Sanz-Serna, J. M., 29

Saunders, Michael A., 226, 227, 229, 257, 413

Sautter,Werner,186

Scarborough,JamesB.,28,54

Schatzman,JamesC.,456

Schaumburg,Kjeld,302

Schelin,CharlesW.,50

Scherer, R., 76

Schneider,Hans,112,115,352

Schonfelder, J. L., 102

Schreiber, Robert S., 153, 168, 180, 245q, 250-253, 256, 257, 278, 365, 375, 571

Schryer,N.L.,496

Schulz, Gunther, 183, 278

Schwartz,S.C.,89

Schwetlick,Hubert，77，393，404，410 414

Searle,ShayleR.,317,487

Sha,Xuan-He,437,446

Shampine, Lawrence F., 29, 76, 86, 524

Shannon, Claude E., 56

Shapiro, Alexander, 133

Shepherd, David, 56

Shewchuk, Jonathan Richard, 29, 91

Shinnerl, Joseph R., 226, 229

Shroff,GautamM.,299

Shub, Michael, 133, 516

Simon,HorstD.,446,447

Skeel, Robert D., 31, 123, 133, 178, 186, 187, 190, 231q, 235, 240, 482q

Slishman,Gordon,446,569

Sloane,N.J.A.,168

Smale, Steve, 2 n

Smith, David M., 502

Smith,FrancisJ.,103,427

Smith, Jon M., 32

Smith, Robert L., 500, 506

Smith, Roger M., 446, 569

Smoktunowicz,Alicja,85,129,136,241 404,525

Snyder,JamesN.,231q,240

Sokolnicka,Jolanta,241

Sorensen, Danny C., 180, 187, 226, 228, 256

Sorevik,T.,448

Spencer, Herbert, 657

Spieß, J., 446

Spononer, David, 485

Steele, Jr., Guy L., 57

Stegun,IreneA.,30

Sterbenz, Pat H., 29, 30, 45, 53, 56, 486

Stewart, G. W. (Pete), xxviii, 68, 102, 107, 115, 119 q, 126, 133, 139 q, 152, 163, 187, 190, 209, 231 q, 240, 241, 282, 295, 302, 307, 318, 339 q, 351, 373, 374, 376, 377, 382, 384, 397, 400, 402-404, 500, 517, 525

Stewart, Michael, 210

Stewart,WilliamJ.,302

Stockmeyer, Larry J., 102

Stoer,Josef,76,107,114,116,187

Stone, Betty Jane, 114

Storey, C., 317

Stoutemyer, David R., 486

Strakoš,Zdeněk,324

Strang, Gilbert, 13q, 112, 133, 457

Strassen, Volker, 278, 434, 448, 449

Straus,E.G.,126,133

Street, Anne Penfold, 168

Stufken,John,168

Stummel, Friedrich, 30, 76, 187

Sun, Ji-guang, 107, 115, 119q, 126, 129, 133, 181, 190, 201, 209, 374, 377, 382, 384, 392, 400, 402, 404, 406, 411, 414, 429

Sun, Xiaobai, 282, 376

Sun,Zheng,411,414

Swann,W.H.,472

Swartzlander, Jr., Earl E., 49

Sweeney,D.W.,56

Swenson, J. R., 48

Sylvester,JamesJoseph,305q,317,434

Tang, Ping Tak Peter, 50, 496, 528

Tang,W.P.,429

Tao, PhamDinh,116,301

Tartaglia, Niccolo, 479

Tasche,Manfred,456

Taussky, Olga, 511q, 514

Teukolsky,SaulA.,476,487,505

Thacher, Jr., Henry C., 188

Thisted, Ronald A., 29

Thompson, Sir D'arcy Wentworth, 1 q

Thron,W.J.,505

Tienari, Martti, 49

Tisserand, Arnaud, 50

Tisseur, Françoise, 294, 461, 462, 468, 523

Todd, John, 114, 115, 512, 518, 523, 524

Toh, Kim-Chuan, 480n, 523

Toledo,Sivan,248

Torchon, Virginia J., 472, 475, 476

Tornheim,L.,169,170

Traub,J.F.,428

Trefethen,LloydN.,5q,157q,168,169 180，323，337，339q，340，342 345，346，348，350，351，480n, 516，523，525

Tremaine, Scott, 87

Tropp, Henry S., 489 n

Trossett, Michael W., 472

Trummer, Manfred R., 340, 348, 350

Tsao,Nai-kuan,76,375

Tucker,Warwick,482

Tukey,JohnW.,56,456

Turing,AlanMathison，xxix，xxx，29 114，119q,184,185,281,481

contributions in 1948 paper "Roundingoff errors...”, 184-185, 281

Turnbull,H.W.,374,521

Turner, Peter R., 47, 49, 152

Tyrtyshnikov, Evgenij E., 523

Underhill, L. G., 524, 525

Ungar,Peter,447

Urabe, Minoru, 57

Uspensky, J. V., 487

Vajtersic,M.,448

van de Geijn, Robert, 282

van der Sluis, A., 125, 126, 190, 199, 381 q, 402

Van der Vorst, Henk A., 187, 226, 256, 324

van Leeuwen, J., 447

Van Loan, Charles F., xxviii, 24, 102, 115, 129, 132, 136, 172, 187, 208, 210, 228, 231 q, 256, 297, 307, 308, 308 n, 339 q, 342, 345, 352, 363, 365, 375, 377, 380, 382, 397, 402, 405, 451 q, 452, 456

van Veldhuizen, M., 189

vanWijngaarden,A.,498

Vanderbei, Robert J., 229

Varah,JamesM.,133,154,257

Varga, Richard S., 147, 154, 257, 505

Vavasis, Stephen A., 278, 395

Vemulapati, Udaya B., 299, 397

Verdonk, Brigitte, 496

Verschaeren,Dennis,496

Veselic, Krešimir, 210

Vetterling, William T., 476, 487, 505

Vieta,Franciscus,479

Vignes, J., 486

Viswanath,D.,516

Vitasek, Emil, 90

Viten'ko,I.V.,86

von Neumann, John, 29, 48, 183, 184, 188, 260, 515

Waite, William, 495, 496

Waldén,Bertil,392,404,406

Walker, Homer F., 323, 468

Wallis, Jennifer Seberry, 168

Wallis,W.D.,168

Ward, Robert C., 282

Warming, Robert F., 525

Wasilkowski, G. W., 133

Wasniewski, Jerzy, 302

Watson, G. A., 133

Watterson, Bill, 471

Wedderburn, J. H. M., 105q

Wedin, Per-Åke, 382, 400, 402, 405, 413

Wegert, Elias, 346

Wei,Musheng,380,402

Weidner, Peter, 483

Weinberger,HansF.,115

Weiss,N.,133

Welfert,B.D.,180

Wendroff, Burton, 186, 190

Werner, Wilhelm, 103

Westin, Lars, 302, 318

Westlake, Joan R., 512

Wette, Matthew R., 317

White, Jon L., 57

White, Michael, 459q

Wichmann,B.A.,496,499

Wilkinson, J. H., xxv, xxviii-xxx, 12, 22, 27 q, 29, 29 q, 30, 35 q, 48,

52, 53, 55, 61q, 66, 67, 67q,

69，76，77，90，91，93q，94,

102, 103, 105q, 132, 139q, 151,

152, 165, 167, 169, 172, 177 q,

180, 183-190, 195q, 199, 200

209, 232, 240, 252, 275, 281,

282, 295, 322, 323, 337 q, 342

353q,357,375,376,376q,378

381, 389, 402-404, 459q, 472,

481, 539, 577 q

first program for Gaussian elimination, 188

on the purpose of a priori error analysis, 195 q

solving linear systems on desk calculator in 1940s, 184

user participation in a computation, 27

Williams, Jack, 415q

Wilson, Greg, 56

Winograd, Shmuel, 434-436, 448

Wisniewski, John A., 485

Witzgall, C., 107, 114, 116

Wolfe,JackM.,88

Woodger, Michael, 157 q, 433 q

Woziakowski,H.,85,133,240,241,298 324，328，466，468

Wrathall, Celia, 485

Wright, Margaret H., 226, 471q, 472, 476

Wright, Stephen J., 167, 226, 468

Yalamov, Plamen Y., 76, 456, 457

Yeung, Man-Chung, 189

Yip, E. L., 487

Yohe,J.Michael,483,501

Young, David M., 29, 322t, 343

Young, Gale, 114

Ypma,TjallingY.,468,469

Yu,Y.,282

Yuval, Gideon, 446

Zawilski,AdamT.,324

Zehfuss, Johann Georg, 317

Zeller, K., 76

Zeng,Z.,282

Zeuner,Hansmartin,456

Zha,Hongyuan,154,189,374,524

Zhang,Zhenyue,524

Zielke, Gerhard, 114, 524

Zietak,K.,318

Ziv, Abraham, 50, 56, 76

Zlatev,Zahari,302

# Subject Index

Knowledge is of two kinds.

We know a subject ourselves,

or we know where we can find information upon it.

SAMUEL JOHNSON, Boswell's Life of Johnson (1775)

A suffix "t" after a page number denotes a table, "f" a figure, "n" a footnote, and "q" a quotation. Mathematical symbols and Greek letters are indexed as if they were spelled out. The solution to a problem is not indexed if the problem itself is indexed under the same term.

Aasen's method, 222-225

growth factor, 224

absolute error, 3

absolute norm, 107

accuracy versus precision, 6, 28

ACRITH,483

adjugatematrix,282

Aitken extrapolation, 91

alternating directions method, 474-475

ATLAS, 579

Augment precompiler, 483, 501

augmented system, 383

iterativerefinementon,389

scaling and conditioning, 391

Automatic Computing Engine (ACE), 53, 185t, 188, 337

automatic differentiation, 485

automatic error analysis, 471-487, see also interval analysis; running error analysis

condition estimation, 477-478

roots of a cubic, 479-481

Strassen's inversion method, 478- 479

using direct search optimization, 472- 474

back substitution, 140

backward error, 6-7

columnwise, 122

componentwise, 122, 128

evaluating, 130

componentwise relative, 122

definition, 6

least squares problem, 392-395, 406

linear system

Oettli-Prager theorem, 122

Rigal-Gaches theorem, 12, 120

Lyapunov equation, 311-312

mixed forward-backward error, 7, 456

normwise, 120

normwise relative, 120

preserving symmetric structure, 394- 395

row-wise, 122

structured, 129

Sylvester equation, 308-311

symmetric structure, preserving, 136

underdetermined system, 411

backward error analysis

development by Wilkinson, 29-30, 185-186

indifferential equations,29

motivation, 6

not a panacea, 1q

purpose, 65, 195q

backward stability

componentwise, 129

definition, 7

normwise, 129

row-wise, 130

banded matrix, growth factor, 173

Bartels-Stewart method, 307-308

base, of floating point arithmetic, 36

Bauer's scaling theorem, 127, 133

bilinear noncommutative matrix multiplication algorithm, 436-437

error analysis, 443-444

binary-decimal conversion, 57

bit, 56

BLAS (Basic Linear Algebra Subprograms), 578

Extended and Mixed Precision, 64, 241, 462, 503, 579

fast level 3, 447

Technical Forum Standard, 503, 579

xNRM2 (2-norm), 499-500, 507

block algorithm

advantages of, 245q

definition, 246

block diagonal dominance, 251-255, 257

and block LU factorization, 252-255

definition, 251

block $\mathbf{LDL}^{\mathrm{T}}$ factorization (of symmetric matrix), 214-222

complete pivoting and its stability, 215-216

for tridiagonal matrix, 221-222

growth factor

complete pivoting, 216

partial pivoting, 218

rook pivoting, 221

partial pivoting and its stability, 216-219

rook pivoting and its stability, 219- 221

block $\mathbf{LDL}^{\mathrm{T}}$ factorization (of skew-symmetric matrix), 225-226

growth factor, 226

block LU factorization, 246, 247

computation, 247

error analysis, 250-256

existence and uniqueness, 247

stability

for (point) diagonally dominant matrix, 254-255

for block diagonally dominant matrix, 251-255

for block tridiagonal matrix, 257

for symmetric positive definite matrix, 255-256

Bunch-Kaufman partial pivoting strategy, 216-219

Bunch-Parlett complete pivoting strategy, 215-216

byte, 56

calculator, displaying words on, 32

cancellation, 9-10, 27

in summation, 83, 539

not a bad thing, 10

of rounding errors, 19-22

Cauchymatrix,514-515

determinant, 515

inverse, 515

LU factors, 515

Cauchy-Schwarz inequality, 106

CELEFUNT package, 496

CESTAC,486

Chebyshev spectral differentiation matrix, 340, 348

Cholesky factorization, 196

computation of, 197

conditions for success in floating point, 200

error analysis, 197-200

existence and uniqueness, 196

perturbation bounds, 201

semidefinite matrix

complete pivoting, 202

computation of, 202

error analysis, 205-208

existence and uniqueness, 201

perturbation theory, 203-205

termination criteria, 207-208

chopping, 54

circulant matrix, 454

circulant system, error analysis for solution by FFT, 454-456

colon notation, 2

commutation matrix, 317

companion matrix, 522-523

singular values, 523

comparison matrix, 145

compensated summation, 83-88

complete pivoting, 158

early use of, 188

fallaciouscriticismof,193

for symmetric indefinite matrices, 215-216

growth factor, 169-170, 189

conjecture proved false, 170

use of, in practice, 188, 562

complexarithmetic,error analysis,71- 73,77

complex number

division without overflow, 500, 506

square root of, 32

componentwise relative error, 4

condition number

distance to singularity and, 111, 114, 127

estimation, 287-304

asymptotic cost, 288

block 1-norm estimator, 294-295

counterexamples,287q,288,292- 294，297，302

counterexamples by direct search, 477-478

for tridiagonal matrices, 299-301

incremental, 298

LAPACK estimator, 292-294, 477-478

LINPACK estimator, 295-297

probabilistic methods, 297-298

general theory, 29

Hadamard, 279, 282, 284

minimizing by scaling, 123, 125-127, 133

of function, 8

of linear system

componentwise, 123

normwise, 121

of matrix (rectangular), 382

of matrix (square), 109, 110, 114

of nonlinear system, 464-467

of summation, 91

Skeel's, 123

conjugate gradient method, 324, 336

circulant preconditioner, 457

continued fraction

algorithms and error analysis, 505

evaluating in IEEE arithmetic, 490- 491

running error bound, 77

convergent matrix, 332, 340

conversion, binary-decimal, 57

correct significant digits, 3-4, 28

correlation matrix, 525

Cramer's rule, (in)stability of, 13-14, 30, 33

Cray computers

adoption of IEEE arithmetic, 44

arithmetic on, 35q, 493

puzzling results from Cray Y-MP and Cray 2, 493-494

UNICOS library, 436, 438

Crout's method, 163

CS decomposition, 380, 400

cubic equation

Newton's method, 486-487

stability of explicit formulae for roots, 479-481

cyclic reduction, 190

denormalized numbers, see subnormal numbers

departure from normality (Henrici's), 344-345

determinant, 279-280

computation of, 279-280

of upper Hessenberg matrix, 24-25

perturbation bound, 285

testing sign of, 282

diagonal dominance, 172, see also block diagonal dominance

diagonally dominant matrix

and block LU factorization, 254-255

Gaussian elimination, error bounds for, 177

growth factor, bound for, 172

inverse, bound for, 154

inverse by Gauss-Jordan elimination, error bound for, 277

nonsingularity of, 190

triangular, bound for cond, 144

tridiagonal bound for inverse, 300

bound for LU factors, 175

differential equations, see ordinary differential equations

direct search optimization methods, 474- 477

discretization error, 5

distance to singularity

componentwise, 127

normwise, 111

divided differences, 21, 99-101

confluent, 419-420

Doolittle's method, 162-163, 187

double rounding, 43, 58

Drazin inverse, 331-332

drift, in floating point arithmetic, 54

dualnorm,107

dual vector, 107

effective conditioning, 133

EISPACK,579

ELEFUNT package, 496

elementary functions, 50

equilibration, 123, 126, 178

error

absolute, 3

backward, see backward error

forward, see forward error

mixed forward-backward error, 7, 456

relative, 3, 4

sources of, 5-6

error analysis, see rounding error analysis

ESSL library (IBM), 436, 438

Euler's method, with compensated summation, 86

$\mathrm{expm1}$ function $(e^x - 1)$ , 30

fan-in algorithm, 152

for summation, 80

for triangular system solution, 149- 151

fast Fourier transform, 451-457

Cooley-Tukey factorization of DFT matrix, 452

error bound, 453

for solving circulant systems, 454- 456

inverse transform, 454

fast matrix multiplication, 433-449

bilinear noncommutative algorithm, 436-437

deriving methods, 446

error analysis, 438-446

in the level-3 BLAS, 447

Miller's error results, 438

record exponent, 436

Strassen's method, 434-436

Winograd's variant, 435-436, 442-443

3M method for complex multiplication, 437-438

Winograd's method, 434

FFT, see fast Fourier transform

FFTW,457

fixed point arithmetic, 53

fl operator (rounding), 38

floating point arithmetic, 35-60

alternatives to, 49

banned from safety-critical systems, 496

base, 36

choice of, 47, 56

binary-decimal conversion, 57

chopping, 54

compiler optimization, dangers of, 494

complexarithmetic,erroranalysis, 71-73

determining properties of, 494-495

drift in, 54

earliest subroutines, 35q

elementary functions, 50

formal op algebra, 54-55

fused multiply-add operation, 46- 47, 60

gradual underflow, see gradual underflow

guard digit, see guard digit

IEEE arithmetic, see IEEE arithmetic

Language Independent Arithmetic (LIA-1), 499

mantissa, 36 n

model, 54, 498-499

Brown's, 495, 498-499

complexarithmetic,71

standard, 40

with underflow, 56-57

without guard digit, 44

monotonic, 56

multiple precision, 501-503

parameters for selected machines, 37t

parameters in software, specifying, 496-497

representation error, 47

rounding, see rounding; double rounding

significand,36

software issues, 489-509

speed of operations (relative), 56

subnormal numbers, 37, 42, 492

subtraction done exactly, 45

testing accuracy of, 51-52

testing correctness of, 495-496

unit roundoff, 3, 38

wobbling precision, 39, 47

floating point coprocessors, 42

floating point numbers

characterization, 36

normalized, 36

spacing between, 37

subnormal, 37, 42

testing for equality, 493

flop, 3

Fortran 95

environmental inquiry functions, 495

matmul, 447

forward error, 6-7

definition, 6

for linear system, 12

linearized expression for, 484

mixed forward-backward error, 7, 456

forward stability

componentwise, 130

definition, 9

normwise, 130

forward substitution, 141

Fourier matrix, 168

FPV (floating point verification) package, 495-496

Frank matrix, 463

Frobeniusnorm,107

fused multiply-add operation, 46-47, 60

$\gamma_{n}$ (error constant)

definition, 63

properties, 67

$\tilde{\gamma}_n$ (error constant), 68

Gauss-Jordan elimination, 273-277, 281-282

algorithm, 273

error analysis, 273-277

Gauss-Seidel method, 321q, 329

Gaussian elimination, 158-163, see also LU factorization

aposteriori stability tests,180-181

complete pivoting, 158, see also complete pivoting

computer programs

first,188

history of, 188

connection with LU factorization, 161

error analysis, 163-166

history of, 183-187

growth factor, 165-173, see also growth factor

inancientChina,187

loop orderings, 187

need for pivoting, 158

on diagonally dominant matrix, 170- 172

on Hessenberg matrix, 24-25

on tridiagonal matrix, 174

pairwise elimination, 180, 189

parallel variants of, 179-180

partial pivoting, 158, 162, see also partial pivoting

pessimism of its accuracy in 1940s, 183

pivoting strategy, choice of, 178- 179

rook pivoting, 159, see also rook pivoting

row-wise error bounds, 177

scaling, row and column, 177-179

threshold pivoting, 193

use by Gauss, 187

versus Cramer's rule, 13-14

without pivoting, instability of, 15

GE, see Gaussian elimination

Gelfand'sproblem,48

generalized QR factorization, 397-398

geometric computation, accuracy of al- gorthims in, 29

GEPP, see Gaussian elimination, partial pivoting

Givens rotation, 365

disjoint rotations, 367-368, 379

fast, 376

GNU MP library, 502

gradual underflow, 38, 42, 45, 56

Gram-Schmidt method, 369-373

classical, 369

error analysis, 371, 373

modified, 370

connection with Householder QR factorization, 353q, 371-372, 376

error analysis, 371-373

error analysis for application to LS problem, 386

stability, 24

reorthogonalization, 376

group inverse, 331

growth factor, 165-173

a posteriori estimates for, 180-181

define using exact or computed quan

tities?, 165, 189

forbandedmatrix,173

for block $\mathbf{LDL}^{\mathrm{T}}$ factorization, 216, 218, 221, 226

for complete pivoting, 169-170

for diagonally dominant matrix, 172

for partial pivoting, 166-173

large growth in practical problems, 167

for random matrices, 189

for rook pivoting, 170

for tridiagonal matrix, 173

for upper Hessenberg matrix, 172

lower bound for, 167

maximization by direct search, 472- 473

numerical maximization for complete pivoting, 170, 189

statistical model of, 168

guard digit, 44

test for, 52

Haar distribution, random orthogonal matrix from, 517-518

Hadamard condition number, 279, 282, 284

Hadamard matrix, 116, 168, 170, 193

Hadamard's inequality, 284

Halley's method, 508

Harwell-Boeing sparse matrix collection, 524

Heron's formula, 45

Hessenberg matrix

determinant of, 24-25, 30, 280

Gaussian elimination, 24-25, 30

growth factor for, 172

Hewlett-Packard HP 48G calculator condition estimator, 302

exhausting its range and precision, 15-16

hidden bit, 41

Hilbert matrix, 512-515, 523-524

Cholesky factor, 513

determinant, 513

inverse, 513

Holder inequality, 106, 107

Horner's method, 94-104

for derivatives, 96-99

for rational function, 26

running error bound, 95-96, 103

Hough's underflow story, 506-507

Householder transformation, 354-355

aggregated (WY representation), 363- 365

block, 375

choice of sign in, 355

error analysis, 357-363

history of, 374-375

in QR factorization, 355-357

Hyman's method, 30, 280, 285

IBM, ESSL library, 436, 438

IEEE arithmetic, 39, 41-43

double rounding, 43, 58

exception handling, 41, 491-492

exception, 41-42

exploiting in software, 490-493

extended formats, 42

gradual underflow, 42

implementation using formal methods, 55-56

$\infty$ ,42,490,492

NaN, 41-42, 490, 492

parameters, 37t, 41

recommended auxiliary functions, 492-493

rounding modes, 41

signed zeros, 42

Standard 754, 41

Standard 854, 43

subnormal numbers, 42, 492

index of a matrix, 331

inertia, 214n

$\infty$ (IEEE arithmetic), 42, 490, 492

inner product

error analysis, 62-65

in extended precision, 64

reducing constant in error bound, 63

Intel

Itanium chip, 46

Pentium chip, division bug, 55

Internet, 574

interval analysis, 41, 190, 481-484

dependencies, 482

fallibility, 483-484

Gaussian elimination, 482

super-accurate inner product, 483

intervalarithmetic,se∈nterval analysis INTLAB,483

inverse iteration, 24

inverse matrix, 259-285

bound using diagonal dominance, 154

Csanky's method for, 278

error analysis

for Gauss-Jordan elimination, 273-277

for LU factorization, 267-271

for triangular matrix, 262-267

high-accuracy computation of, 281

in solving $Ax = b$ ,stability,260

left and right residuals, 261

Newton's method for, 278

perturbation theory, 127-128

Schulz iteration, 278

Strassen's method for, 448-449, 478-479

times for computation on early computers, 272t

triangular

bounds for, 147-149

methods for, 262-267

why not to compute, 260

involutary matrix, 519

irreducible matrix, 127

Itanium chip, 46

iterative methods, see also stationary iterative methods

dates of publication, 322 t

error analysis, 325-335

survey of, 323-324

stopping criteria, 335-337, 467-468

iterative refinement

backward error analysis, 235-239, 463

condition number estimate from, 242

for least squares problem, 388-391, 403

for square linear system, 27, 184, 231-243, 462-463

with QR factorization, 368-369

for Vandermonde system, 427-428

forward error analysis, 232-235, 463

in fixed precision, 179, 234, 494

in mixed precision, 234

LAPACK convergence test, 241

practical issues, 241-242

Jacobi method, forward error analysis, 328-329

Jordan canonical form, 340

Kahan matrix, 149, 205

second smallest singular value, 154

Kreiss matrix theorem, 346

Kronecker product, 306, 317

LANCELOT,170,189

LAPACK, 579-581

block $\mathbf{LDL}^{\mathrm{T}}$ factorization (of symmetric matrix), 228

block and partitioned LU factorization, 257

Cholesky factorization, 210-211

condition number estimation, 292- 294, 303

forward error bound for linear systems, 131

iterativerefinement,241-242

least squares problem, 405

linear system, 191

LU factorization, 178, 191-192, 257

matrix 1-norm estimator, 292-294, 477-478

matrix inversion, 282-283

QR factorization, 377-378

Sylvester equation, 318

test matrix generation, 525

triangular systems, 153

$2\times 2$ problems, solving, 497-498

underdetermined system, 414

xLAMCH for determining machine parameters, 495

Latin, neoclassic, publishing papers in, 456

$\mathbf{LDL}^{\mathrm{T}}$ factorization, 197

least significant digit, 36

least squares problem, 382

augmented system, 383 scaling and conditioning of, 391

backward error, 392-395, 406

iterativerefinement,388-391,403

linear equality constrained, 396-400 backward error, 405

elimination method, 399-400

method of weighting, 397

null space method, 397-399

perturbation theory, 396

linear inequality constrained, 405

Longley test problem, 402

modified Gram-Schmidt, error analysis, 386

normal equations, 382, 405

error analysis, 386-388

versus QR factorization, 388

perturbation theory, 382-384

QR factorization, error analysis, 384- 385

quadratic constrained, 405

seminormal equations, 391-392

weighted, 395

Leja ordering, 100, 101, 103, 104, 427

level index arithmetic, 49

linear system

large dense, in applications, 191

perturbation theory, 119-137

practical forward error bounds, 131

records for largest solved, 191t

scaling before Gaussian elimination, 177-179, 190

times for solution on early computers, 185t

LINPACK,579

Cholesky factorization of semidefinite matrix, 207

condition estimator, 295-297, 302

iterativerefinement,241

LU factorization, 178

matrix inversion, 264, 268, 269, 271

tridiagonal system solution, 303

$\log (1 + x)$ , accurate evaluation, 32

logarithmic distribution of numbers, 47, 49

Longley test problem, 402

LU factorization, 161, see also Gaussian elimination

aposteriori stability tests,180-181

block, see block LU factorization

complete pivoting, 158, see also complete pivoting

Crout's method, 163

determinantal formulae for factors, 161

Doolittle's method, 162-163

error analysis, 163-166 history of, 183-187

existence and uniqueness, 161

for nonsymmetric positive definite matrix, 208-209

growth factor, 165-173, see also growth factor

loop orderings, 187

of diagonally dominant matrix, 170- 172

of Hessenberg matrix, 24-25

of tridiagonal matrix, 174

parallel variants of, 179-180

partial pivoting, 158, 162, see also partial pivoting

partitioned,246 error analysis of,249-250

perturbation bounds, 181-182

pivoting strategy, choice of, 178- 179

rank-revealing, 182-183

recursively partitioned, 248

rook pivoting, 159, see also rook pivoting

scaling, row and column, 177-179

stability for $M$ -matrix, 190

threshold pivoting, 193

versus Cramer's rule, 13-14

without pivoting, instability of, 15

Lyapunov equation, 311

backward error, 311-312

discrete-time, 316-317

$M$ -matrix, 145, 152

stability of LU factorization, 190

triangular, 145-147

machar code, 495

machine epsilon, 37

magic square matrix, $p$ norm of, 115

mantissa, 36 n

Maple, 6, 170, 502

Markov chain, perturbation analysis for, 133

Mathematica, 6, 170, 502

MATLAB,3,575

compan,513t,523

condest,xxii,295

eig, 464

eps, 39

fft, 454

frank, 513t

gallery, 512, 513t, 583

gallery('chebspec',...),348,513t

gallery('clement',...), 239, 513t

gallery('frank',...), 463

gallery('kahan',...), 513t

gallery('orthog',...),239,473n 477,513t

gallery('pei', ..., 513t

gallery('randsvd',...),513t,517n 524,525

gallery('toeppen',...),513t,525

gallery('tridiag',...), 513t

hadamard, 513t

hilb, 513t

ifft, 454

invhilb, 513t

inv, 261, 268

magic, 513t

normest1,295

pascal, 513t, 524

pow2, 493

rand, 513t, 516

randn, 513t, 516

rccond,294

realmax, 39

realmin, 39

roots, 480

toeplitz, 513t

vander, 513t

Matrix Computation Toolbox, 583-585

Symbolic Math Toolbox, 3, 6, 463, 514, 519

matrix

adjugate, 282

block diagonally dominant, 251

Cauchy, 514-515

circulant, 454

commutation, 317

companion, 522-523

comparison, 145

condition number, 109, 110, 114, 382

confluent Vandermonde-like, 419

convergent, 332, 340

correlation, 525

diagonally dominant, 172

distance to singularity, 111, 127

Drazin inverse, 331-332

Fourier, 168

Frank, 463

group inverse, 331

Hadamard, 116, 168, 170, 193

Hilbert, 512-515, 523-524

inversion, 259-285, see also inverse matrix

involuntary, 519

irreducible, 127

Kahan, 149, 154, 205

$M$ -matrix, 145, 152

magic square, 115

moment, 518

nonsymmetric positive definite, 208

Pascal, 518-521

Pei, 284, 304

polynomials, 102

powers of, 339-352, see also powers of a matrix

pseudo-inverse, 382, 402, 405, 408

random, 515-518

randsvd, 517-518, 525

second difference, 522

semiconvergent, 332

skew-symmetric, 214, 225

submatrices, number of, 192

Sylvester's introduction of term, 305

symmetric indefinite, 214

symmetric positive definite, 196

symmetric positive semidefinite, 201

symmetricquasidefinite,229

test, 511-525

totally nonnegative, 164

tridiagonal, 174-176

Toeplitz, 521-522

Vandermonde, 416

Vandermonde-like, 418

vec-permutation, 314, 317

Matrix Market, 524

matrix multiplication

backward error, 77

error analysis, 69-71, 78

fast methods, 433-449

matrix norm, see norm

meaningless answers, why you might get them, 30-31

misconceptions, of floating point arithmetic, 28

mixed forward-backward error, 7, 456

modified Gram-Schmidt method, see Gram-Schmidt method, modified

moment matrix, 518

monotone norm, 107

monotonicity

of floating point arithmetic, 56

of rounding, 38

Moore-Penrose conditions, 405

most significant digit, 36

multidirectional search method, 475-477

multiple precision arithmetic, 501-503

Bailey's package MPFUN, 501-502

Brent's package, 483, 501

GNU MP library, 502

mutation testing, 515-516

NAGLibrary,575

LAPACK in, 580

machine constants, 497

NaN (not a number), 41-42, 490, 492

Nelder-Mead simplex method, 476-477

netlib,574-575

Neville elimination, 180, 189

Newton's method, 460

for eigenproblem, 463-464

formatrixinverse,278

forreciprocation,46

inexact, 468

limiting accuracy, 461

limitingresidual,462

sources of error in, 460

stopping criteria, 467-468

Newton-Schulz iteration, 183

nonsymmetric positive definite matrix, 208

LU factorization, stability of, 208-209

norm, 105-117

$\| \cdot \|_{\alpha ,\beta}$ , explicit formulae for, 116

absolute, 107

consistent, 108

dual, 107

Frobenius, 107

Holder inequality, 106

matrix, 107-112

norm equivalence constants, 109t

matrix $p$ -norm, 112-114

of magic square matrix, 115

monotone, 107

subordinate matrix, 108, 109

2-norm, evaluation without overflow, 499-500

unitarily invariant, 108

vector, 106-107

norm equivalence constants, 109t

normal distribution, 3

normal equations, 382, 405

error analysis, 386-388

notation, explanation of, 2-3, 67-69

$0^0$ ,definition,59

NPSOL, 189

numerical analysis, definition, 5-6

numerical radius, 343

numerical stability

definition, 7, 29

for linear equation solvers, 129-130

Oettli-Prager backward error theorem, 122

ordinary differential equations

accuracy of mesh point formation, 92

backward error in, 29

Euler's method with compensated summation, 86

outer product, error analysis, 64-65

overflow, 16, 38

avoiding, 499-501

$\pmb{p}$ -norm power method, 289-291, 301- 302

pairwise (fan-in) summation, 80

pairwise elimination, 180, 189

parallel prefix operation, 103, 152

paranoia code, 495

partial pivoting, 158, 162

early use of, 188

for skew-symmetric matrices, 225

for symmetric indefinite matrices, 216-219

growth factor, 166-173

large growth in practical problems, 167

threshold pivoting, 193

partitioned algorithm, definition, 246

partitioned LU factorization, 246

error analysis, 249-250

Pascal matrix, 518-521

Cholesky factor, 519

eigenvalue reciprocity, 519

inverse, 520

total positivity, 520

Patriot missile software problem, 503-504

Peimatrix,284,304

Pentium chip, division bug, 55

performance profile, for LAPACK norm estimator, 294

perturbation theory

by calculus, 132

linear systems, 119-137

statistical, 133, 136

Sylvester equation, 313-315

pi $(\pi)$ ,high-precision calculation as computer test,489q

polar decomposition, 377, 380

polynomials, 93-104, see also Horner's method

divided differences, 99-101

fast evaluation schemes, 103-104

matrix, evaluation of, 102

Newton form, 99-101

PORT library, machine constants, 497

portability of software, 496-499

positive definite matrix, see nonsymmetric positive definite matrix; symmetric positive definite matrix

power method, 22

formatrix1-normestimation,292- 295

formatrix $p$ -normestimation,289- 291，301-302

powers of a matrix, 339-352

behaviour of stationary iteration, 351

departure from normality, 344-345

hump, 342-343

in exact arithmetic, 340-346

in finite precision arithmetic, 346- 350

pseudospectrum, 345-346, 349-350

role of spectral radius, 340-342

PRECISE,486

precision

effect of increasing, 17-19

versus accuracy, 6, 28

program verification, applied to error analysis, 485

pseudo-inverse, 382, 402, 405, 408

pseudospectral radius, 345

pseudospectrum, 345-346, 349-350

of companion matrix, 523

Pythagorean sum, 500, 507-509

QR factorization, 355

column pivoting, 362, 378

generalized,397-398

Givens, 365-366

cancellation of errors in, 21-22

error analysis, 366-368

Householder, 355-357

error analysis, 359-363

error analysis for application to LS problem, 384-385

error analysis for partitioned (WY representation), 363-365

iterativerefinementforlinear system,368-369

perturbation theory, 373-374

rank-revealing, 377

row pivoting, 362

row sorting, 362

quadratic equation, solving, 10-11, 29

quadrature

accuracy of grid formation, 92

error bound for evaluation of rule, 78

quasidefinite matrix, see symmetric quasidefinite matrix

random matrices, 515-518

condition number of, 516

correlation matrices, 525

expected number of real eigenvalues, 516-517

orthogonal, 517, 524

spectral radius of, 516

tend to be well conditioned, 516

2-norm of, 516

with given singular values, 517-518

randsvd matrix, 517-518, 524, 525

range reduction, 51

RCOND condition estimator (LAPACK, LINPACK, MATLAB), 302, 477-478

recursively partitioned LU factorization, 248

relative error, 3, 4

componentwise, 4

relative error counter, $< k>$ , 68

relative precision, 69

relative residual, 12

research problems, 92, 104, 193, 212, 229, 242, 304, 319, 352, 406, 430, 449, 469, 487, 525

residual, relative, 12

Riccati equation, algebraic, 316

Rigal-Gaches backward error theorem, 120

rook pivoting, 159-160, 188

average number of comparisons, 160, 220

for symmetric indefinite matrices, 219-221

growth factor, 170

rounding, 4, 38

dealing with ties, 38, 54

modes in IEEE arithmetic, 41

monotonicity of, 38

to even versus to odd, 54

rounding error analysis

automatic, 471-487

demystified, 74-76

graphs in, 76

model

standard, 40

with underflow, 56-57

without guard digit, 44

notation, 67-69

ordering of operations, effect of, 70, 141, 142

purpose of, 65, 195q

statistical approach, 48-49

rounding errors

accumulation of, 14

are not random, 25-26, 48

beneficial effects of, 22-24

cancellation of, 19-22

in subtraction, 45

statistical assumptions on, 48-49

rules of thumb

condition for computed powers of matrix to converge to zero, 350

forward error related to backward error and condition number, 9

relative speed of floating point operations, 56

square root of constants in error bound, 48

Runge-Kutta method, 83, 90

running error analysis, 66, 486

for continued fraction, 77

for Horner's method, 95-96, 103

for inner product, 65-67

sample variance, see variance

ScaLAPACK,580

scaling a linear system before Gaussian elimination, 177-179, 190

scaling to minimize the condition number, 123, 125-127, 178

Schulz iteration, 183, 278

Schur complement, 203, 209, 215, 246, 252

perturbation bounds for symmetric positive semidefinite matrix, 203-208

second difference matrix, 522

semiconvergent matrix, 332

seminormal equations

for least squares problem, 391-392

for underdetermined system, 408

separation (sep), of two matrices, 313

Sherman-Morrison formula, 190, 487

Sherman-Morrison-Woodbury formula, 258, 558

Sierpinski gasket, 521

significancearithmetic,486

significand,36

significant digits

correct, 3-4, 28

least and most significant, 36

singular value decomposition (SVD), 114- 115

skew-symmetric matrix, 214, 225

software

avoiding underflow and overflow, 499-501

effects of underflow, 501

issues in floating point arithmetic, 489-509

portability, 496-499

specifyingarithmeticparameters,496- 497

specifying numerical constants, 498

SOR method, forward error analysis, 329

square root, of complex number, 32

stability, see backward stability; forward stability

stable algorithms, designing, 26-28

stationary iterative methods, 321-337

andpowersofamatrix,351

backward error analysis, 330-331

forward error analysis, 325-329 singular systems, 333-335

Jacobi method, 328-329

scale independence, 327

singular systems, theory for, 331- 333

SOR method, 329

stopping criteria, 335-337

statistics, see also variance

computational references, 29

sticky bit, 41

Strassen's method, 434-436

accuracy compared with conventional multiplication, 441-442

error analysis, 440-443

error versus operation count, 14

for inversion, 448-449, 478-479

implementation issues, 446-447

Winograd's variant, 435-436, 442-443

subdifferential, of a vector norm, 289

subgradient, 290

subnormal numbers, 37, 42, 492

substitution, back and forward, 140-141

subtraction, exactness in floating point arithmetic, 45

successive overrelaxation method, see SOR method

summation, 79-92

choice of method: summary, 89-90

compensated and applications, 83- 88

condition number, 91

criterion for minimizing error, 82

distillation algorithms, 88

doubly compensated, 87-88

error analysis, 81-83

insertion method, 80

pairwise (fan-in), 80

recursive, 80

ordering in, 17, 82-83

statistical error estimates, 88-89

SVD (singular value decomposition), 114-115

Sylvester equation, 306

backward error, 308-311

Bartels-Stewart method, 307-308

generalizations, 316-318

perturbation theory, 313-315

practical error bounds, 315-316

solution methods, 307-308

symbolic manipulation package, 6

Symbolic Math Toolbox, 3, 6, 463, 514, 519

symmetric indefinite factorization, see block LDLT factorization (of symmetric matrix)

symmetric indefinite matrix, 214

symmetric positive definite matrix, 196

and block LU factorization, 255-256

practical test for, 210

symmetric positive semidefinite matrix, 201

determinantal conditions for, 211

symmetricquasidefinitematrix,229

synthetic division, 96

tablemaker's dilemma, 4, 50

test

for accuracy of floating point arithmetic, 51-52

for guard digit, 52

test matrices, 511-525, see also MATLAB; matrix; random matrices

Matrix Computation Toolbox, 583-585

Harwell-Boeing collection, 524

Matrix Market, 524

3M method, 437-438, 447-448, 502

error analysis, 444-446

threshold pivoting, 193

Toeplitz matrix

pseudospectra, 525, 526f

tridiagonal, 521-522

totally nonnegative matrix, 164, 520

LU factorization, 164-165, 188

row scaling in, 179

test for, 188

transformations, well conditioned, 27

triangular matrix

bounds for inverse, 147-149

condition numbers, 142-143

inversion methods

blocked, 265-267

unblocked, 262-264

$M$ -matrix, 145-147

triangular systems, 139-155

accuratesolutionof,139q,143,144 147

conditioning, 144-145

fan-in algorithm, 149-151

partitioned inverse method, 153

substitution

backward error analysis, 140-142

forward error analysis, 142-147

tridiagonal matrix, 174-176

condition number estimation, 299-301

growth factor, 173

LU factorization, 174

error analysis of, 174-176

structure of inverse, 300-302

Toeplitz, 521-522

truncation error, 5

Turing Award of the ACM, xxix, 55

Turing programming language, 503

Numerical Turing, 503

twisted factorization, 303

$2\times 2$ problems, reliable solution of, 497- 498

ulp(unit in last place),39

uncertainty, in data, 5

underdetermined system, 408

backward error

normwise, 411

row-wise, 411

modified Gram-Schmidt, 413

perturbation theory, 409-411

Q method (QR factorization), 408 error analysis, 411-413

seminormal equations, 408 error analysis, 412

underflow, 16, 38

avoiding, 499-501

effects on software, 501

gradual, 38, 42, 45, 56

model for error analysis, 56-57

UNICOS library (Cray), 436, 438

unit roundoff, 3, 38

update formula, involving small correction, 27

van der Sluis's theorem, 125

Vancouver Stock Exchange, inaccurate index, 54

Vandermonde matrix

bounds and estimates for condition number, 417-418

definition, 416

inverse, 416-418

inversion algorithm, 417

LU factorization in factored form, 422

QR factorization, 429

structured condition number, 428-429

Vandermonde system, 415-431

accuracy independent of condition number, 425

algorithm

dual, 421

for primal, 422-423

forresidualofconfluent system, 427

backward error analysis, 425-426

complexity results, 429

curinginstability,427-428

forward error analysis, 424-425

history of solution methods, 429

preventing instability, 426-427

structured backward error, 429

Vandermonde-like matrix

confluent, definition, 419

definition, 418

determinant, 430

variance

algorithms for computing, 11-12, 29

condition numbers for, 32

error bound for two-pass formula, 33

vec operator, 306

vec-permutation matrix, 314, 317, 584

Venus probe, loss due to program bug, 489q

Wedin'sleast squaresperturbation theorem,382

proof, 400-402

Winograd's method, 434, 448

error analysis, 439-440

scaling for stability, 439-440

wobbling precision, 39, 47

WY representation of product of Householder matrices, 363-365

$0^0$ ,definition,59

Accuracy and Stability of Numerical Algorithms gives a thorough, up-to-date treatment of the behavior of numerical algorithms in finite precision arithmetic. It combines algorithmic derivations, perturbation theory, and rounding error analysis, all enlivened by historical perspective and informative quotations.

This second edition expands and updates the coverage of the first edition (1996) and includes numerous improvements to the original material. Two new chapters treat symmetric indefinite systems and skew-symmetric systems, and nonlinear systems and Newton's method. An expanded treatment of Gaussian elimination incorporates rook pivoting and additional error bounds. Other new topics include rank-revealing LU factorizations, weighted and constrained least squares problems, and the fused multiply-add operation found on some modern computer architectures.

Although not designed specifically as a textbook, this new edition is a suitable reference for an advanced course. It can also be used by instructors at all levels as a supplementary text from which to draw examples, historical perspective, statements of results, and exercises.

From reviews of the first edition:

"This definitive source on the accuracy and stability of numerical algorithms is quite a bargain and a worthwhile addition to the library of any statistician heavily involved in computing."

Robert L Strawderman, Journal of the American Statistical Association, March 1999.

"This text may become the new 'Bible' about accuracy and stability for the solution of systems of linear equations. It covers 688 pages carefully collected, investigated, and written ...One will find that this book is a very suitable and comprehensive reference for research in numerical linear algebra, software usage and development, and for numerical linear algebra courses."

N. Kockler, Zentralblatt für Mathematik, Band 847/96.

"Nick Higham has assembled an enormous amount of important and useful material in a coherent, readable form. His book belongs on the shelf of anyone who has more than a casual interest in rounding

![](images/2484e3633c6a51cc69bdbeb2197c8899f54e483cef1616aa1c268e67bbeeeebc.jpg)

error and matrix computations." — G.W. Stewart, SIAM Review, March 1997.

Nicholas J. Higham is Richardson Professor of Applied Mathematics at the University of Manchester, England. He is the author of more than 80 publications and is a member of the editorial boards of Foundations of Computational Mathematics, the IMA Journal of Numerical Analysis, Linear Algebra and Its Applications, and the SIAM Journal on Matrix Analysis and Applications.

For more information about SIAM books, journals, conferences, memberships, or activities, contact:

![](images/b8d834687e7dcc311b6c3fe46cdd202b94acc84bc0662819a0ccee077dbc1605.jpg)

Society for Industrial and Applied Mathematics

3600 University City Science Center

Philadelphia, PA 19104-2688

215-382-9800·Fax 215-386-7999

siam@siam.org \* www.siam.org
