# Chapter 14

# Matrix Inversion

It is amusing to remark that we were so involved with it on that we probably talked of nothing else for months.

Just in this period Mrs. von Neumann acquired a big, rather wild but gentle Irish Setter puppy,

which she called Inverse in honor of our work!

— HERMAN H. GOLDSTINE, The Computer: From Pascal to von Neumann (1972)

The most computationally intensive portion of the tasks assigned to the processors is integrating the KKR matrix inverse over the first Brillouin zone.

To evaluate the integral,

hundreds or possibly thousands of complex double precision matrices

of order between 80 and 300 must be formed and inverted.

Each matrix corresponds to a different vertex of the tetrahedrons

into which the Brillouin zone has been subdivided.

— M. T. HEATH, G. A. GEIST, and J. B. DRAKE,

Superconductivity Computations,

in Early Experience with the Intel iPSC/860

at Oak Ridge National Laboratory (1990)

Press $\boxed{1 / x}$ to invert the matrix.

Note that matrix inversion can produce erroneous results

if you are using ill-conditioned matrices.

— HEWLETT-PACKARD, HP 48G Series User's Guide (1993)

Almost anything you can do with $A^{-1}$ can be done without it.

— GEORGE E. FORSYTHE and CLEVE B. MOLER,

Computer Solution of Linear Algebraic Systems (1967)

# 14.1. Use and Abuse of the Matrix Inverse

To most numerical analysts, matrix inversion is a sin. Forsythe, Malcolm, and Moler put it well when they say [430, 1977, p. 31] "In the vast majority of practical computational problems, it is unnecessary and inadvisable to actually compute $A^{-1}$ ." The best example of a problem in which the matrix inverse should not be computed is the linear equations problem $Ax = b$ . Computing the solution as $x = A^{-1} \times b$ requires $2n^3$ flops, assuming $A^{-1}$ is computed by Gaussian elimination with partial pivoting (GEPP), whereas GEPP applied directly to the system costs only $2n^3 / 3$ flops.

Not only is the inversion approach three times more expensive, but it is much less stable. Suppose $X = A^{-1}$ is formed exactly, and that the only rounding errors are in forming $x = fl(Xb)$ . Then $\widehat{x} = (X + \Delta X)b$ , where $|\Delta X| \leq \gamma_n |X|$ , by (3.11). So $A\widehat{x} = A(X + \Delta X)b = (I + A\Delta X)b$ , and the best possible residual bound is

$$
\left| b - A \widehat {x} \right| \leq \gamma_ {n} | A | | A ^ {- 1} | | b |.
$$

For GEPP, Theorem 9.4 yields

$$
\left| b - A \widehat {x} \right| \leq \gamma_ {3 n} | \widehat {L} | | \widehat {U} | | \widehat {x} |.
$$

Since it is usually true that $\| |\widehat{L} ||\widehat{U} ||_{\infty}\approx \| A\|_{\infty}$ for GEPP, we see that the matrix inversion approach is likely to give a much larger residual than GEPP if $A$ is ill conditioned and if $\| x\|_{\infty}\ll \| |A^{-1}||b|\|_{\infty}$ . For example, we solved fifty $25\times 25$ systems $Ax = b$ in MATLAB, where the elements of $x$ are taken from the normal $N(0,1)$ distribution and $A$ is random with $\kappa_2(A) = u^{-1 / 2}\approx 9\times 10^7$ . As Table 14.1 shows, the inversion approach provided much larger backward errors than GEPP in this experiment.

Given the inexpedience of matrix inversion, why devote a chapter to it? The answer is twofold. First, there are situations in which a matrix inverse must be computed. Examples are in statistics [63, 1974, §7.5], [806, 1984, §2.3], [834, 1989, p. 342 ff], where the inverse can convey important statistical information, in certain matrix iterations arising in eigenvalue-related problems [47, 1997], [193, 1987], [621, 1994], in the computation of matrix functions such as the square root [609, 1997] and the logarithm [231, 2001], and in numerical integrations arising in superconductivity computations [555, 1990] (see the quotation at the start of the chapter). Second, methods for matrix inversion display a wide variety of stability properties, making for instructive and challenging error analysis. (Indeed, the first major rounding error analysis to be published, that of von Neumann and Goldstine, was for matrix inversion—see §9.13).

Table 14.1. Backward errors $\eta_{A,b}(\widehat{x})$ for the $\infty$ -norm.   

<table><tr><td></td><td>min</td><td>max</td></tr><tr><td>x = A-1 × b</td><td>6.66e-12</td><td>1.69e-10</td></tr><tr><td>GEPP</td><td>3.44e-18</td><td>7.56e-17</td></tr></table>

Matrix inversion can be done in many different ways—in fact, there are more computationally distinct possibilities than for any other basic matrix computation. For example, in triangular matrix inversion different loop orderings are possible and either triangular matrix-vector multiplication, solution of a triangular system, or a rank-1 update of a rectangular matrix can be employed inside the outer loop. More generally, given a factorization $PA = LU$ , two ways to evaluate $A^{-1}$ are as $A^{-1} = U^{-1} \times L^{-1} \times P$ , and as the solution to $UA^{-1} = L^{-1} \times P$ . These methods generally achieve different levels of efficiency on high-performance computers, and they propagate rounding errors in different ways. We concentrate in this chapter on the numerical stability, but comment briefly on performance issues.

The quality of an approximation $Y \approx A^{-1}$ can be assessed by looking at the right and left residuals, $AY - I$ and $YA - I$ , and the forward error, $Y - A^{-1}$ . Suppose we perturb $A \to A + \Delta A$ with $|\Delta A| \leq \epsilon |A|$ ; thus, we are making relative perturbations of size at most $\epsilon$ to the elements of $A$ . If $Y = (A + \Delta A)^{-1}$ then $(A + \Delta A)Y = Y(A + \Delta A) = I$ , so that

$$
\begin{array}{l} \left| A Y - I \right| = \left| \Delta A Y \right| \leq \epsilon | A | | Y |, (14.1) \\ \left| Y A - I \right| = \left| Y \Delta A \right| \leq \epsilon | Y | | A |, (14.2) \\ \end{array}
$$

and, since $(A + \Delta A)^{-1} = A^{-1} - A^{-1}\Delta AA^{-1} + O(\epsilon^{2})$

$$
\left| A ^ {- 1} - Y \right| \leq \epsilon \left| A ^ {- 1} \right| \left| A \right| \left| A ^ {- 1} \right| + O \left(\epsilon^ {2}\right). \tag {14.3}
$$

(Note that (14.3) can also be derived from (14.1) or (14.2).) The bounds (14.1)-(14.3) represent "ideal" bounds for a computed approximation $Y$ to $A^{-1}$ , if we regard $\epsilon$ as a small multiple of the unit roundoff $u$ . We will show that, for triangular matrix inversion, appropriate methods do indeed achieve (14.1) or (14.2) (but not both) and (14.3).

It is important to note that neither (14.1), (14.2), nor (14.3) implies that $Y + \Delta Y = (A + \Delta A)^{-1}$ with $\| \Delta A \|_{\infty} \leq \epsilon \| A \|_{\infty}$ and $\| \Delta Y \|_{\infty} \leq \epsilon \| Y \|_{\infty}$ , that is, $Y$ need not be close to the inverse of a matrix near to $A$ , even in the norm sense. Indeed, such a result would imply that both the left and right residuals are bounded in norm by $(2\epsilon + \epsilon^{2}) \| A \|_{\infty} \| Y \|_{\infty}$ , and this is not the case for any of the methods we will consider.

To illustrate the latter point we give a numerical example. Define the matrix $A_{n} \in \mathbb{R}^{n \times n}$ as triu(qr(vand(n))), in MATLAB notation (vand is a routine from the Matrix Computation Toolbox—see Appendix D); in other words, $A_{n}$ is the upper triangular QR factor of the $n \times n$ Vandermonde matrix based on equispaced points on [0, 1]. We inverted $A_{n}$ , for $n = 5:80$ , using MATLAB's inv function, which uses GEPP. The left and right normwise relative residuals

$$
\operatorname {r e s} _ {\mathrm {L}} = \frac {\| \widehat {X} A - I \| _ {\infty}}{\| \widehat {X} \| _ {\infty} \| A \| _ {\infty}}, \qquad \operatorname {r e s} _ {\mathrm {R}} = \frac {\| A \widehat {X} - I \| _ {\infty}}{\| A \| _ {\infty} \| \widehat {X} \| _ {\infty}},
$$

are plotted in Figure 14.1. We see that while the left residual is always less than the unit roundoff, the right residual becomes large as $n$ increases. These matrices are very ill conditioned (singular to working precision for $n \geq 20$ ), yet it is still reasonable to expect a small residual, and we will prove in §14.3.2 that the left residual must be small, independent of the condition number.

![](images/fa829b7c1b9cb5d0af1b68b63bf5228e11517e032fcd9d53030fdfc10fed2e61.jpg)  
Figure 14.1. Residuals for inverses computed by MATLAB's inv function.

In most of this chapter we are not concerned with the precise values of constants (§14.4 is the exception); thus $c_n$ denotes a constant of order $n$ . To simplify the presentation we introduce a special notation. Let $A_i \in \mathbb{R}^{m_i \times n_i}$ , $i = 1: k$ , be matrices such that the product $A_1A_2 \ldots A_k$ is defined and let

$$
p = \sum_ {i = 1} ^ {k - 1} n _ {i}.
$$

Then $\varDelta(A_1,A_2,\ldots,A_k)\in\mathbb{R}^{m_1\times n_k}$ denotes a matrix bounded according to

$$
\left| \Delta \left(A _ {1}, A _ {2}, \dots , A _ {k}\right) \right| \leq c _ {p} u \left| A _ {1} \right| \left| A _ {2} \right| \dots \left| A _ {k} \right|.
$$

This notation is chosen so that if $\widehat{C} = fl(A_1A_2\ldots A_k)$ , with the product evaluated in any order, then

$$
\widehat {C} = A _ {1} A _ {2} \dots A _ {k} + \Delta \left(A _ {1}, A _ {2}, \dots , A _ {k}\right).
$$

# 14.2. Inverting a Triangular Matrix

We consider the inversion of a lower triangular matrix $L \in \mathbb{R}^{n \times n}$ , treating unblocked and blocked methods separately. We do not make a distinction between partitioned and block methods in this section. All the results in this and the next section are from Du Croz and Higham [357, 1992].

# 14.2.1. Unblocked Methods

We focus our attention on two " $j$ " methods that compute $L^{-1}$ a column at a time. Analogous "i" and "k" methods exist, which compute $L^{-1}$ row-wise or use outer products, respectively, and we comment on them at the end of the section.

The first method computes each column of $X = L^{-1}$ independently, using forward substitution. We write it as follows, to facilitate comparison with the second method.

# Method 1.

for $j = 1:n$

$$
\begin{array}{l} x _ {j j} = l _ {j j} ^ {- 1} \\ X (j + 1: n, j) = - x _ {j j} L (j + 1: n, j) \\ \text {S o l v e} L (j + 1: n, j + 1: n) X (j + 1: n, j) = X (j + 1: n, j), \\ \begin{array}{l} \text {b y} \end{array} \\ \end{array}
$$

end

In BLAS terminology, this method is dominated by $n$ calls to the level-2 BLAS routine xTRSV (TRiangular SolVe).

The second method computes the columns in the reverse order. On the $j$ th step it multiplies by the previously computed inverse $L(j + 1:n, j + 1:n)^{-1}$ instead of solving a system with coefficient matrix $L(j + 1:n, j + 1:n)$ .

# Method 2.

for $j = n: - 1:1$

$$
\boldsymbol {x} _ {j j} = l _ {j j} ^ {- 1}
$$

$$
X (j + 1: n, j) = X (j + 1: n, j + 1: n) L (j + 1: n, j)
$$

$$
X (j + 1: n, j) = - x _ {j j} X (j + 1: n, j)
$$

end

Method 2 uses $n$ calls to the level-2 BLAS routine xTRMV (TRiangular Matrix times Vector). On most high-performance machines xTRMV can be implemented to run faster than xTRSV, so Method 2 is generally preferable to Method 1 from the point of view of efficiency (see the performance figures at the end of §14.2.2). We now compare the stability of the two methods.

Theorem 8.5 shows that the $j$ th column of the computed $\tilde{X}$ from Method 1 satisfies

$$
(L + \Delta L _ {j}) \widehat {x} _ {j} = e _ {j}, \quad | \Delta L _ {j} | \leq c _ {n} u | L |.
$$

It follows that we have the componentwise residual bound

$$
\left| L \widehat {X} - I \right| \leq c _ {n} u | L | | \widehat {X} | \tag {14.4}
$$

and the componentwise forward error bound

$$
| \widehat {X} - L ^ {- 1} | \leq c _ {n} u | L ^ {- 1} | | L | | \widehat {X} |. \tag {14.5}
$$

Since $\widehat{X} = L^{-1} + O(u)$ , (14.5) can be written as

$$
\left| \widehat {X} - L ^ {- 1} \right| \leq c _ {n} u \left| L ^ {- 1} \right| \left| | L | \right| \left| L ^ {- 1} \right| + O \left(u ^ {2}\right), \tag {14.6}
$$

which is invariant under row and column scaling of $L$ . If we take norms we obtain normwise relative error bounds that are either row or column scaling independent: from (14.6) we have

$$
\frac {\left\| \widehat {X} - L ^ {- 1} \right\| _ {\infty}}{\left\| L ^ {- 1} \right\| _ {\infty}} \leq c _ {n} u \operatorname {c o n d} \left(L ^ {- 1}\right) + O \left(u ^ {2}\right), \tag {14.7}
$$

and the same bound holds with $\operatorname{cond}(L^{-1})$ replaced by $\operatorname{cond}(L)$ .

Notice that (14.4) is a bound for the right residual, $L\widehat{X} - I$ . This is because Method 1 is derived by solving $LX = I$ . Conversely, Method 2 can be derived by solving $XL = I$ , which suggests that we should look for a bound on the left residual for this method.

Lemma 14.1. The computed inverse $\widehat{X}$ from Method 2 satisfies

$$
| \widehat {X} L - I | \leq c _ {n} u | \widehat {X} | | L |. \tag {14.8}
$$

Proof. The proof is by induction on $n$ , the case $n = 1$ being trivial. Assume the result is true for $n - 1$ and write

$$
L = \left[ \begin{array}{c c} \alpha & 0 \\ y & M \end{array} \right], \qquad X = L ^ {- 1} = \left[ \begin{array}{c c} \beta & 0 \\ z & N \end{array} \right],
$$

where $\alpha, \beta \in \mathbb{R}, y, z \in \mathbb{R}^{n-1}$ , and $M, N \in \mathbb{R}^{(n-1) \times (n-1)}$ . Method 2 computes the first column of $X$ by solving $XL = I$ according to

$$
\beta = \alpha^ {- 1}, \qquad z = - \beta N y.
$$

In floating point arithmetic we obtain

$$
\begin{array}{l} \widehat {\beta} = \alpha^ {- 1} (1 + \delta), \quad | \delta | \leq u, \\ \widehat {z} = - \widehat {\beta} \widehat {N} y + \Delta (\widehat {\beta}, \widehat {N}, y). \\ \end{array}
$$

Thus

$$
\begin{array}{l} \widehat {\beta} \alpha = 1 + \delta , \\ \widehat {z} \alpha + \widehat {N} y = - \delta \widehat {N} y + \alpha \Delta (\widehat {\beta}, \widehat {N}, y). \\ \end{array}
$$

This may be written as

$$
\begin{array}{l} | \widehat {X} L - I | (1: n, 1) \leq \left[ \begin{array}{c} u \\ u | \widehat {N} | | y | + c _ {n} u (1 + u) | \widehat {N} | | y | \end{array} \right] \\ \leq c _ {n} ^ {\prime} u \left(| \widehat {X} | | L |\right) (1: n, 1). \\ \end{array}
$$

By assumption, the corresponding inequality holds for the $(2:n, 2:n)$ submatrices and so the result is proved. $\square$

Lemma 14.1 shows that Method 2 has a left residual analogue of the right residual bound (14.4) for Method 1. Since there is, in general, no reason to choose between a small right residual and a small left residual, our conclusion is that Methods 1 and 2 have equally good numerical stability properties.

More generally, it can be shown that all three $i$ , $j$ , and $k$ inversion variants that can be derived from the equations $LX = I$ produce identical rounding errors under suitable implementations, and all satisfy the same right residual bound; likewise, the three variants corresponding to the equation $XL = I$ all satisfy the same left residual bound. The LINPACK routine xTRDI uses a $k$ variant derived from $XL = I$ ; the LINPACK routines xGEDI and xPODI contain analogous code for inverting an upper triangular matrix (but the LINPACK Users' Guide [341, 1979, Chaps. 1 and 3] describes a different variant from the one used in the code).

# 14.2.2. Block Methods

Let the lower triangular matrix $L \in \mathbb{R}^{n \times n}$ be partitioned in block form as

$$
L = \left[ \begin{array}{c c c c} L _ {1 1} & & & \\ L _ {2 1} & L _ {2 2} & & \\ \vdots & & \ddots & \\ L _ {N 1} & \dots & \dots & L _ {N N} \end{array} \right], \tag {14.9}
$$

where we place no restrictions on the block sizes, other than to require the diagonal blocks to be square. The most natural block generalizations of Methods 1 and 2 are as follows. Here, we use the notation $L_{p;q,r;s}$ to denote the submatrix comprising the intersection of block rows $p$ to $q$ and block columns $r$ to $s$ of $L$ .

Method 1B.

for $j = 1:N$

$$
\begin{array}{l} X _ {j j} = L _ {j j} ^ {- 1} (\text {b y M e t h o d 1}) \\ X _ {j + 1: N, j} = - L _ {j + 1: N, j} X _ {j j} \\ \text {S o l v e} L _ {j + 1: N, j + 1: N} X _ {j + 1: N, j} = X _ {j + 1: N, j}, \\ \text {b y} \\ \end{array}
$$

end

Method 2B.

for $j = N: - 1:1$

$$
X _ {j j} = L _ {j j} ^ {- 1} (\text {b y M e t h o d 2})
$$

$$
X _ {j + 1: N, j} = X _ {j + 1: N, j + 1: N} L _ {j + 1: N, j}
$$

$$
X _ {j + 1: N, j} = - X _ {j + 1: N, j} X _ {j j}
$$

end

One can argue that Method 1B carries out the same arithmetic operations as Method 1, although possibly in a different order, and that it therefore satisfies the same error bound (14.4). For completeness, we give a direct proof.

Lemma 14.2. The computed inverse $\widehat{X}$ from Method 1B satisfies

$$
\left| L \widehat {X} - I \right| \leq c _ {n} u \left| L \right| \left| \widehat {X} \right|. \tag {14.10}
$$

Proof. Equating block columns in (14.10), we obtain the $N$ independent inequalities

$$
\left| L \widehat {X} _ {1: N, j} - I _ {1: N, j} \right| \leq c _ {n} u | L | | \widehat {X} _ {1: N, j} |, \quad j = 1: N. \tag {14.11}
$$

It suffices to verify the inequality with $j = 1$ . Write

$$
L = \left[ \begin{array}{c c} L _ {1 1} & 0 \\ L _ {2 1} & L _ {2 2} \end{array} \right], \qquad X = \left[ \begin{array}{c c} X _ {1 1} & 0 \\ X _ {2 1} & X _ {2 2} \end{array} \right],
$$

where $L_{11}, X_{11} \in \mathbb{R}^{r \times r}$ and $L_{11}$ is the $(1,1)$ block in the partitioning of (14.9). $X_{11}$ is computed by Method 1 and so, from (14.4),

$$
\left| L _ {1 1} \widehat {X} _ {1 1} - I \right| \leq c _ {r} u \left| L _ {1 1} \right| \left| \widehat {X} _ {1 1} \right| = c _ {r} u \left(\left| L \right| \left| \widehat {X} \right|\right) _ {1 1}. \tag {14.12}
$$

$X_{21}$ is computed by forming $T = -L_{21}X_{11}$ and solving $L_{22}X_{21} = T$ . The computed $\widehat{X}_{21}$ satisfies

$$
L _ {2 2} \widehat {X} _ {2 1} + \Delta \left(L _ {2 2}, \widehat {X} _ {2 1}\right) = - L _ {2 1} \widehat {X} _ {1 1} + \Delta \left(L _ {2 1}, \widehat {X} _ {1 1}\right).
$$

Hence

$$
\begin{array}{l} \left| L _ {2 1} \widehat {X} _ {1 1} + L _ {2 2} \widehat {X} _ {2 1} \right| \leq c _ {n} u \left(\left| L _ {2 1} \right| \left| \widehat {X} _ {1 1} \right| + \left| L _ {2 2} \right| \left| \widehat {X} _ {2 1} \right|\right) \\ = c _ {n} u \left(| L | | \widehat {X} |\right) _ {2 1}. \tag {14.13} \\ \end{array}
$$

Together, inequalities (14.12) and (14.13) are equivalent to (14.11) with $j = 1$ , as required.

We can attempt a similar analysis for Method 2B. With the same notation as above, $X_{21}$ is computed as $X_{21} = -X_{22}L_{21}X_{11}$ . Thus

$$
\widehat {X} _ {2 1} = - \widehat {X} _ {2 2} L _ {2 1} \widehat {X} _ {1 1} + \Delta \left(\widehat {X} _ {2 2}, L _ {2 1}, \widehat {X} _ {1 1}\right). \tag {14.14}
$$

To bound the left residual we have to postmultiply by $L_{11}$ and use the fact that $X_{11}$ is computed by Method 2:

$$
\widehat {X} _ {2 1} L _ {1 1} + \widehat {X} _ {2 2} L _ {2 1} (I + \Delta (\widehat {X} _ {1 1}, L _ {1 1})) = \Delta (\widehat {X} _ {2 2}, L _ {2 1}, \widehat {X} _ {1 1}) L _ {1 1}.
$$

This leads to a bound of the form

$$
\left| \widehat {X} _ {2 1} L _ {1 1} + \widehat {X} _ {2 2} L _ {2 1} \right| \leq c _ {n} u \left| \widehat {X} _ {2 2} \right| \left| L _ {2 1} \right| \left| \widehat {X} _ {1 1} \right| \left| L _ {1 1} \right|,
$$

which would be of the desired form in (14.8) were it not for the factor $|\widehat{X}_{11}||L_{11}|$ . This analysis suggests that the left residual is not guaranteed to be small. Numerical experiments confirm that the left and right residuals can be large simultaneously for Method 2B, although examples are quite hard to find [357, 1992]; therefore the method must be regarded as unstable when the block size exceeds 1.

The reason for the instability is that there are two plausible block generalizations of Method 2 and we have chosen an unstable one that does not carry out the same arithmetic operations as Method 2. If we perform a solve with $L_{jj}$ instead of multiplying by $X_{jj}$ we obtain the second variation, which is used by LAPACK's xTRTRI.

# Method 2C.

for $j = N: - 1:1$

$$
X _ {j j} = L _ {j j} ^ {- 1} \left(\text {b y M e t h o d 2}\right)
$$

$$
X _ {j + 1: N, j} = X _ {j + 1: N, j + 1: N} L _ {j + 1: N, j}
$$

Solve $X_{j + 1:N,j}L_{jj} = -X_{j + 1:N,j}$ by back substitution.

end

For this method, the analogue of (14.14) is

$$
\widehat {X} _ {2 1} L _ {1 1} + \varDelta (\widehat {X} _ {2 1}, L _ {1 1}) = - \widehat {X} _ {2 2} L _ {2 1} + \varDelta (\widehat {X} _ {2 2}, L _ {2 1}),
$$

which yields

$$
\left| \widehat {X} _ {2 1} L _ {1 1} + \widehat {X} _ {2 2} L _ {2 1} \right| \leq c _ {n} u \big (\left| \widehat {X} _ {2 1} \right| \left| L _ {1 1} \right| + \left| \widehat {X} _ {2 2} \right| \left| L _ {2 1} \right| \big).
$$

Hence Method 2C enjoys a very satisfactory residual bound.

Table 14.2. Mflop rates for inverting a triangular matrix on a Cray 2.   

<table><tr><td colspan="2"></td><td>n = 128</td><td>n = 256</td><td>n = 512</td><td>n = 1024</td></tr><tr><td rowspan="3">Unblocked:</td><td>Method 1</td><td>95</td><td>162</td><td>231</td><td>283</td></tr><tr><td>Method 2</td><td>114</td><td>211</td><td>289</td><td>330</td></tr><tr><td>k variant</td><td>114</td><td>157</td><td>178</td><td>191</td></tr><tr><td>Blocked:</td><td>Method 1B</td><td>125</td><td>246</td><td>348</td><td>405</td></tr><tr><td rowspan="2">(block size 64)</td><td>Method 2C</td><td>129</td><td>269</td><td>378</td><td>428</td></tr><tr><td>k variant</td><td>148</td><td>263</td><td>344</td><td>383</td></tr></table>

Lemma 14.3. The computed inverse $\widehat{X}$ from Method 2C satisfies

$$
\left| \widehat {X} L - I \right| \leq c _ {n} u \left| \widehat {X} \right| | L |. \quad \square
$$

In summary, block versions of Methods 1 and 2 are available that have the same residual bounds as the point methods. However, in general, there is no guarantee that stability properties remain unchanged when we convert a point method to block form, as shown by Method 2B.

In Table 14.2 we present some performance figures for inversion of a lower triangular matrix on a Cray 2. These clearly illustrate the possible gains in efficiency from using block methods, and also the advantage of Method 2 over Method 1. For comparison, the performance of a $k$ variant is also shown (both $k$ variants run at the same rate). The performance characteristics of the $i$ variants are similar to those of the $j$ variants, except that since they are row oriented rather than column oriented, they are liable to be slowed down by memory-bank conflicts, page thrashing, or cache missing.

# 14.3. Inverting a Full Matrix by LU Factorization

Next, we consider four methods for inverting a full matrix $A \in \mathbb{R}^{n \times n}$ , given an LU factorization computed by GEPP. We assume, without loss of generality, that there are no row interchanges. We write the computed LU factors as $L$ and $U$ . Recall that $A + \Delta A = LU$ , with $|\Delta A| \leq c_n u |L||U|$ (Theorem 9.3).

# 14.3.1. Method A

Perhaps the most frequently described method for computing $X = A^{-1}$ is the following one.

# Method A.

for $j = 1:n$

Solve $Ax_{j} = e_{j}$

end

Compared with the methods to be described below, Method A has the disadvantages of requiring more temporary storage and of not having a convenient

partitioned version. However, it is simple to analyse. From Theorem 9.4 we have

$$
\left. \left(A + \Delta A _ {j}\right) \widehat {x} _ {j} = e _ {j}, \quad \left| \Delta A _ {j} \right| \leq c _ {n} ^ {\prime} u | L | | U |, \right. \tag {14.15}
$$

and so

$$
\left| A \widehat {X} - I \right| \leq c _ {n} ^ {\prime} u | L | | U | | \widehat {X} |. \tag {14.16}
$$

This bound departs from the form (14.1) only in that $|A|$ is replaced by its upper bound $|L||U| + O(u)$ . The forward error bound corresponding to (14.16) is

$$
| \widehat {X} - A ^ {- 1} | \leq c _ {n} ^ {\prime} u | A ^ {- 1} | | L | | U | | \widehat {X} |. \tag {14.17}
$$

Note that (14.15) says that $\widehat{x}_j$ is the $j$ th column of the inverse of a matrix close to $A$ , but it is a different perturbation $\Delta A_j$ for each column. It is not true that $\widehat{X}$ itself is the inverse of a matrix close to $A$ , unless $A$ is well conditioned.

# 14.3.2. Method B

Next, we consider the method used by LINPACK's xGEDI, LAPACK's xGETRI, and MATLAB's inv function.

# Method B.

Compute $U^{-1}$ and then solve for $X$ the equation $XL = U^{-1}$ .

To analyse this method we will assume that $U^{-1}$ is computed by an analogue of Method 2 or 2C for upper triangular matrices that obtains the columns of $U^{-1}$ in the order 1 to $n$ . Then the computed inverse $X_U \approx U^{-1}$ will satisfy the residual bound

$$
\left| X _ {U} U - I \right| \leq c _ {n} u \left| X _ {U} \right| \left| U \right|.
$$

We also assume that the triangular solve from the right with $L$ is done by back substitution. The computed $\widehat{X}$ therefore satisfies $\widehat{X}L = X_U + \Delta(\widehat{X}, L)$ and so

$$
\widehat {X} (A + \varDelta A) = \widehat {X} L U = X _ {U} U + \varDelta (\widehat {X}, L) U.
$$

This leads to the residual bound

$$
\begin{array}{l} \left| \widehat {X} A - I \right| \leq c _ {n} u \left(\left| U ^ {- 1} \right| \left| U \right| + 2 \left| \widehat {X} \right| \left| L \right| \left| U \right|\right) \\ \leq c _ {n} ^ {\prime} u | \widehat {X} | | L | | U |, \tag {14.18} \\ \end{array}
$$

which is the left residual analogue of (14.16). From (14.18) we obtain the forward error bound

$$
| \widehat {X} - A ^ {- 1} | \leq c _ {n} ^ {\prime} u | \widehat {X} | | L | | U | | A ^ {- 1} |.
$$

Note that Methods A and B are equivalent, in the sense that Method A solves for $X$ the equation $LUX = I$ while Method B solves $XLU = I$ . Thus the two methods carry out analogous operations but in different orders. It follows that the methods must satisfy analogous residual bounds, and so (14.18) can be deduced from (14.16).

We mention in passing that the LINPACK manual states that for Method B a bound holds of the form $\| A\widehat{X} - I \| \leq d_n u \| A \| \| \widehat{X} \|$ [341, 1979, p. 1.20]. This is incorrect, although counterexamples are rare; it is the left residual that is bounded this way, as follows from (14.18).

# 14.3.3. Method C

The next method that we consider is from Du Croz and Higham [357, 1992]. It solves the equation $UXL = I$ , computing $X$ a partial row and column at a time. To derive the method partition

$$
X = \left[ \begin{array}{l l} x _ {1 1} & x _ {1 2} ^ {T} \\ x _ {2 1} & X _ {2 2} \end{array} \right], \qquad L = \left[ \begin{array}{c c} 1 & 0 \\ l _ {2 1} & L _ {2 2} \end{array} \right], \qquad U = \left[ \begin{array}{c c} u _ {1 1} & u _ {1 2} ^ {T} \\ 0 & U _ {2 2} \end{array} \right],
$$

where the $(1,1)$ blocks are scalars, and assume that the trailing submatrix $X_{22}$ is already known. Then the rest of $X$ is computed according to

$$
\begin{array}{l} x _ {2 1} = - X _ {2 2} l _ {2 1}, \\ x _ {1 2} ^ {T} = - u _ {1 2} ^ {T} X _ {2 2} / u _ {1 1}, \\ x _ {1 1} = 1 / u _ {1 1} - x _ {1 2} ^ {T} l _ {2 1}. \\ \end{array}
$$

The method can also be derived by forming the product $X = U^{-1} \times L^{-1}$ using the representation of $L$ and $U$ as a product of elementary matrices (and diagonal matrices in the case of $U$ ). In detail the method is as follows.

Method C.

for $k = n: -1: 1$

$$
X (k + 1: n, k) = - X (k + 1: n, k + 1: n) L (k + 1: n, k)
$$

$$
X (k, k + 1: n) = - U (k, k + 1: n) X (k + 1: n, k + 1: n) / u _ {k k}
$$

$$
x _ {k k} = 1 / u _ {k k} - X (k, k + 1: n) L (k + 1: n, k)
$$

end

The method can be implemented so that $X$ overwrites $L$ and $U$ , with the aid of a work vector of length $n$ (or a work array to hold a block row or column in the partitioned case). Because most of the work is performed by matrix-vector (or matrix-matrix) multiplication, Method C is likely to be the fastest of those considered in this section on many machines. (Some performance figures are given at the end of the section.)

A straightforward error analysis of Method C shows that the computed $\widehat{X}$ satisfies

$$
| U \widehat {X} L - I | \leq c _ {n} u | U | | \widehat {X} | | L |. \tag {14.19}
$$

We will refer to $U\widehat{X}L - I$ as a "mixed residual". From (14.19) we can obtain bounds on the left and right residual that are weaker than those in (14.18) and (14.16) by a factor $|U^{-1}||U|$ on the left or $|L||L^{-1}|$ on the right, respectively. We also obtain from (14.19) the forward error bound

$$
| \widehat {X} - A ^ {- 1} | \leq c _ {n} u | U ^ {- 1} | | U | | \widehat {X} | | L | | L ^ {- 1} |,
$$

which is (14.17) with $|A^{-1}|$ replaced by its upper bound $|U^{-1}||L^{-1}| + O(u)$ and the factors reordered.

The LINPACK routine $\mathbf{xSIDI}$ uses a special case of Method C in conjunction with block $\mathrm{LDLT}^{\mathrm{T}}$ factorization with partial pivoting to invert a symmetric indefinite matrix; see Du Croz and Higham [357, 1992] for details.

# 14.3.4. Method D

The next method is based on another natural way to form $A^{-1}$ and is used by LAPACK's xPOTRI, which inverts a symmetric positive definite matrix.

# Method D.

Compute $L^{-1}$ and $U^{-1}$ and then form $A^{-1} = U^{-1} \times L^{-1}$ .

The advantage of this method is that no extra workspace is needed; $U^{-1}$ and $L^{-1}$ can overwrite $U$ and $L$ , and can then be overwritten by their product. However, Method D is significantly slower on some machines than Methods B or C, because it uses a smaller average vector length for vector operations.

To analyse Method D we will assume initially that $L^{-1}$ is computed by Method 2 (or Method 2C) and, as for Method B above, that $U^{-1}$ is computed by an analogue of Method 2 or 2C for upper triangular matrices. We have

$$
\widehat {X} = X _ {U} X _ {L} + \Delta \left(X _ {U}, X _ {L}\right). \tag {14.20}
$$

Since $A = LU - \Delta A$

$$
\widehat {X} A = X _ {U} X _ {L} L U - X _ {U} X _ {L} \Delta A + \Delta \left(X _ {U}, X _ {L}\right) A. \tag {14.21}
$$

Rewriting the first term of the right-hand side using $X_{L}L = I + \Delta(X_{L}, L)$ , and similarly for $U$ , we obtain

$$
\widehat {X} A - I = \Delta \left(X _ {U}, U\right) + X _ {U} \Delta \left(X _ {L}, L\right) U - X _ {U} X _ {L} \Delta A + \Delta \left(X _ {U}, X _ {L}\right) A, \tag {14.22}
$$

and so

$$
\begin{array}{l} \left| \hat {X} A - I \right| \leq c _ {n} ^ {\prime} u \left(\left| U ^ {- 1} \right| | U | + 2 \left| U ^ {- 1} \right| \left| L ^ {- 1} \right| | L | | U | + \left| U ^ {- 1} \right| \left| L ^ {- 1} \right| | A |\right) \\ \leq c _ {n} ^ {\prime \prime} u | U ^ {- 1} | | L ^ {- 1} | | L | | U |. \tag {14.23} \\ \end{array}
$$

This bound is weaker than (14.18), since $|\widehat{X}| \leq |U^{-1}||L^{-1}| + O(u)$ . Note, however, that the term $\Delta(X_U, X_L)A$ in the residual (14.22) is an unavoidable consequence of forming $X_U X_L$ , and so the bound (14.23) is essentially the best possible.

The analysis above assumes that $X_{L}$ and $X_{U}$ both have small left residuals. If they both have small right residuals, as when they are computed using Method 1, then it is easy to see that a bound analogous to (14.23) holds for the right residual $A\widehat{X} - I$ . If $X_{L}$ has a small left residual and $X_{U}$ has a small right residual (or vice versa) then it does not seem possible to derive a bound of the form (14.23). However, we have

$$
\left| X _ {L} L - I \right| = \left| L ^ {- 1} \left(L X _ {L} - I\right) L \right| \leq \left| L ^ {- 1} \right| \left| L X _ {L} - I \right| \left| L \right|, \tag {14.24}
$$

and since $L$ is unit lower triangular with $|l_{ij}| \leq 1$ , we have $|(L^{-1})_{ij}| \leq 2^{n - 1}$ , which places a bound on how much the left and right residuals of $X_L$ can differ. Furthermore, since the matrices $L$ from GEPP tend to be well conditioned $(\kappa_{\infty}(L) \ll n2^{n - 1})$ , and since our numerical experience is that large residuals tend to occur only for ill-conditioned matrices, we would expect the left and right residuals of $X_L$ almost always to be of similar size. We conclude that even in the

"conflicting residuals" case, Method D will, in practice, usually satisfy (14.23) or its right residual counterpart, according to whether $X_U$ has a small left or right residual respectively. Similar comments apply to Method B when $U^{-1}$ is computed by a method yielding a small right residual.

These considerations are particularly pertinent when we consider Method D specialized to symmetric positive definite matrices and the Cholesky factorization $A = R^T R$ . Now $A^{-1}$ is obtained by computing $X_{R} = R^{-1}$ and then forming $A^{-1} = X_{R}X_{R}^{T}$ ; this is the method used in the LINPACK routine xP0DI [341, 1979, Chap. 3]. If $X_{R}$ has a small right residual then $X_{R}^{T}$ has a small left residual, so in this application we naturally encounter conflicting residuals. Fortunately, the symmetry and definiteness of the problem help us to obtain a satisfactory residual bound. The analysis parallels the derivation of (14.23), so it suffices to show how to treat the term $X_{R}X_{R}^{T}R^{T}R$ (cf. (14.21)), where $R$ now denotes the computed Cholesky factor. Assuming $RX_{R} = I + \Delta(R,X_{R})$ , and using (14.24) with $L$ replaced by $R$ , we have

$$
\begin{array}{l} X _ {R} X _ {R} ^ {T} R ^ {T} R = X _ {R} \left(I + \Delta \left(R, X _ {R}\right) ^ {T}\right) R \\ = I + F + X _ {R} \Delta (R, X _ {R}) ^ {T} R, \quad | F | \leq | R ^ {- 1} | | \Delta (R, X _ {R}) | | R |, \\ = I + G, \\ \end{array}
$$

and

$$
| G | \leq c _ {n} u (| R ^ {- 1} | | R | | R ^ {- 1} | | R | + | R ^ {- 1} | | R ^ {- T} | | R ^ {T} | | R |).
$$

From the inequality $\| |B| \|_2 \leq \sqrt{n} \| B \|_2$ for $B \in \mathbb{R}^{n \times n}$ (see Lemma 6.6), together with $\| A \|_2 = \| R \|_2^2 + O(u)$ , it follows that

$$
\left\| G \right\| _ {2} \leq 2 n ^ {2} c _ {n} u \| A \| _ {2} \| A ^ {- 1} \| _ {2},
$$

and thus overall we have a bound of the form

$$
\| \widehat {X} A - I \| _ {2} \leq d _ {n} u \| A \| _ {2} \| \widehat {X} \| _ {2}.
$$

Since $\widehat{X}$ and $A$ are symmetric the same bound holds for the right residual.

# 14.3.5. Summary

In terms of the error bounds, there is little to choose between Methods A, B, C, and D. Numerical results reported in [357, 1992] show good agreement with the bounds. Therefore the choice of method can be based on other criteria, such as performance and the use of working storage. Table 14.3 gives some performance figures for a Cray 2, covering both blocked (partitioned) and unblocked forms of Methods B, C, and D.

On a historical note, Tables 14.4 and 14.5 give timings for matrix inversion on some early computing devices; times for two more modern machines are given for comparison. The inversion methods used for the timings on the early computers in Table 14.4 are not known, but are probably methods from this section or the next.

Table 14.3. Mflop rates for inverting a full matrix on a Cray 2.   

<table><tr><td colspan="2"></td><td>n = 64</td><td>n = 128</td><td>n = 256</td><td>n = 512</td></tr><tr><td rowspan="3">Unblocked:</td><td>Method B</td><td>118</td><td>229</td><td>310</td><td>347</td></tr><tr><td>Method C</td><td>125</td><td>235</td><td>314</td><td>351</td></tr><tr><td>Method D</td><td>70</td><td>166</td><td>267</td><td>329</td></tr><tr><td rowspan="3">Blocked: (block size 64)</td><td>Method B</td><td>142</td><td>259</td><td>353</td><td>406</td></tr><tr><td>Method C</td><td>144</td><td>264</td><td>363</td><td>415</td></tr><tr><td>Method D</td><td>70</td><td>178</td><td>306</td><td>390</td></tr></table>

Table 14.4. Times (minutes and seconds) for inverting an $n \times n$ matrix. Source for DEUCE, Pegasus, and Mark 1 timings: [200, 1981].   

<table><tr><td>n</td><td>DEUCE(English Electric)1955</td><td>Pegasus(Ferranti)1956</td><td>ManchesterMark 11951</td><td>HP 48G Calculator1993</td><td>Sun SPARC-station ELC1991</td></tr><tr><td>8</td><td>20s</td><td>26s</td><td>-</td><td>4s</td><td>.004s</td></tr><tr><td>16</td><td>58s</td><td>2m 37s</td><td>-</td><td>18s</td><td>.01s</td></tr><tr><td>24</td><td>3m 36s</td><td>7m 57s</td><td>8m</td><td>48s</td><td>.02s</td></tr><tr><td>32</td><td>7m 44s</td><td>17m 52s</td><td>16m</td><td>-</td><td>.04s</td></tr></table>

Table 14.5. Additional timings for inverting an $n \times  n$ matrix.   

<table><tr><td>Machine</td><td>Year</td><td>n</td><td>Time</td><td>Reference</td></tr><tr><td>Aiken Relay Calculator</td><td>1948</td><td>38</td><td>59 1/2 hours</td><td>[858, 1948]</td></tr><tr><td>IBM 602 Calculating Punch</td><td>1949</td><td>10</td><td>8 hours</td><td>[1195, 1949]</td></tr><tr><td>SEAC (National Bureau of Standards)</td><td>1954</td><td>49</td><td>3 hours</td><td>[1141, 1954]</td></tr><tr><td>Datatron</td><td>1957</td><td>80a</td><td>2 1/2 hours</td><td>[847, 1957]</td></tr><tr><td>IBM 704</td><td>1957</td><td>115b</td><td>19m 30s</td><td>[354, 1957]</td></tr></table>

${}^{a}$ Block tridiagonal matrix,using an inversion method designed for such matrices.   
${}^{b}$ Symmetric positive definite matrix.

# 14.4. Gauss-Jordan Elimination

Whereas Gaussian elimination (GE) reduces a matrix to triangular form by elementary operations, Gauss-Jordan elimination (GJE) reduces it all the way to diagonal form. GJE is usually presented as a method for matrix inversion, but it can also be regarded as a method for solving linear equations. We will take the method in its latter form, since it simplifies the error analysis. Error bounds for matrix inversion are obtained by taking unit vectors for the right-hand sides.

At the $k$ th stage of GJE, all off-diagonal elements in the $k$ th column are eliminated, instead of just those below the diagonal, as in GE. Since the elements in the lower triangle (including the pivots on the diagonal) are identical to those that occur in GE, Theorem 9.1 tells us that GJE succeeds if all the leading principal submatrices of $A$ are nonsingular. With no form of pivoting GJE is unstable in general, for the same reasons that GE is unstable. Partial and complete pivoting are easily incorporated.

Algorithm 14.4 (Gauss-Jordan elimination). This algorithm solves the linear system $Ax = b$ , where $A \in \mathbb{R}^{n \times n}$ is nonsingular, by GJE with partial pivoting.

for $k = 1:n$

Find $r$ such that $|a_{rk}| = \max_{i \geq k} |a_{ik}|$ .

$A(k,k:n)\leftrightarrow A(r,k:n),b(k)\leftrightarrow b(r)\%$ Swap rows $k$ and $r$

row_ind = [1: k-1, k+1: n] % Row indices of elements to eliminate.

$m = A(row ind, k) / A(k, k) \%$ Multipliers.

$A(row\_ind, k: n) = A(row\_ind, k: n) - m * A(k, k: n)$

$(*)$ $b(row\_ ind) = b(row\_ ind) - m * b(k)$

end

$$
x _ {i} = b _ {i} / a _ {i i}, i = 1: n
$$

Cost: $n^3$ flops.

Note that for matrix inversion we repeat statement (*) for $b = e_1, e_2, \ldots, e_n$ in turn, and if we exploit the structure of these right-hand sides the total cost is $2n^3$ flops—the same as for inversion by LU factorization.

The numerical stability properties of GJE are rather subtle and error analysis is trickier than for GE. An observation that simplifies the analysis is that we can consider the algorithm as comprising two stages. The first stage is identical to GE and forms $M_{n-1}M_{n-2}\ldots M_1A = U$ , where $U$ is upper triangular. The second stage reduces $U$ to diagonal form by elementary operations:

$$
N _ {n} N _ {n - 1} \dots N _ {2} U = D, \quad N _ {k} = I - n _ {k} e _ {k} ^ {T}, \quad e _ {i} ^ {T} n _ {k} = 0, i \geq k.
$$

The solution $x$ is formed as $x = D^{-1}N_{n}\ldots N_{2}y$ , where $y = M_{n - 1}\ldots M_{1}b$ . The rounding errors in the first stage are precisely the same as those in GE, so we will ignore them for the moment (that is, we will consider $L$ , $U$ , and $y$ to be exact) and consider the second stage. We will assume, for simplicity, that there are no row interchanges. As with GE, this is equivalent to assuming that all row interchanges are done at the start of the algorithm.

Define $U_{k+1} = N_k \ldots N_2U$ (so $U_2 = U$ ) and note that $N_k$ and $U_k$ have the forms

$$
U _ {k} = \left[ \begin{array}{c c} D _ {k - 1} & [ v _ {k} W _ {k} ] \\ 0 & Z _ {k} \end{array} \right], \quad D _ {k - 1} \in \mathbb {R} ^ {(k - 1) \times (k - 1)}, \text {d i a g o n a l},
$$

$$
N _ {k} = \left[ \begin{array}{c c} I _ {k - 1} & \left[ n _ {k} \quad 0 \right] \\ 0 & I _ {n - k + 1} \end{array} \right],
$$

where $n_k = \left[ -u_{1k} / u_{kk}, \ldots, -u_{k-1,k} / u_{kk} \right]^T$ . The computed matrices obviously satisfy

$$
\widehat {U} _ {k + 1} = \widehat {N} _ {k} \widehat {U} _ {k} + \Delta_ {k}, \tag {14.25a}
$$

$$
\Delta_ {k} = \left[ \begin{array}{c c} 0 _ {k - 1} & \Delta^ {(k)} \\ 0 & 0 _ {n - k + 1} \end{array} \right], \quad | \Delta_ {k} | \leq \gamma_ {3} | \widehat {N} _ {k} | | \widehat {U} _ {k} | \tag {14.25b}
$$

(to be precise, $\widehat{N}_k$ is defined as $N_{k}$ but with $(\widehat{N}_k)_{ik} = -\widehat{u}_{ik} / \widehat{u}_{kk})$ . Similarly, with $x_{k + 1} = \widehat{N}_k\dots \widehat{N}_2y$ , we have

$$
\widehat {x} _ {k + 1} = \widehat {N} _ {k} \widehat {x} + f _ {k}, \quad e _ {i} ^ {T} f _ {k} = 0, i \geq k, | f _ {k} | \leq \gamma_ {3} | \widehat {N} _ {k} | | \widehat {x} _ {k} |. \tag {14.26}
$$

Because of the structure of $\widehat{N}_k$ , $\Delta_k$ , and $f_k$ , we have the useful property that

$$
\widehat {N} _ {i} \Delta_ {j} = \Delta_ {j}, \quad i \geq j, \quad \widehat {N} _ {i} f _ {j} = f _ {j}, \quad i \geq j.
$$

Without loss of generality, we now assume that the final diagonal matrix $D$ is the identity (i.e., the pivots are all 1); this simplifies the analysis a little and has a negligible effect on the final bounds. Thus (14.25) and (14.26) yield

$$
I = \widehat {U} _ {n + 1} = \widehat {N} _ {n} \dots \widehat {N} _ {2} U + \sum_ {k = 2} ^ {n} \Delta_ {k}, \tag {14.27}
$$

$$
\widehat {x} = \widehat {x} _ {n + 1} = \widehat {N} _ {n} \dots \widehat {N} _ {2} y + \sum_ {k = 2} ^ {n} f _ {k}. \tag {14.28}
$$

Now

$$
\begin{array}{l} \left| \Delta_ {k} \right| \leq \gamma_ {3} \left| \widehat {N} _ {k} \right| \left| \widehat {U} _ {k} \right| \leq \gamma_ {3} \left| \widehat {N} _ {k} \right| \left| \widehat {N} _ {k - 1} \widehat {U} _ {k - 1} + \Delta_ {k - 1} \right| \\ \leq \gamma_ {3} (1 + \gamma_ {3}) | \widehat {N} _ {k} | | \widehat {N} _ {k - 1} | \widehat {U} _ {k - 1} | \\ \leq \dots \leq \gamma_ {3} (1 + \gamma_ {3}) ^ {k - 2} | \hat {N} _ {k} | \dots | \hat {N} _ {2} | | U |, \\ \end{array}
$$

and, similarly,

$$
\left| f _ {k} \right| \leq \gamma_ {3} \left(1 + \gamma_ {3}\right) ^ {k - 2} \left| \widehat {N} _ {k} \right| \dots \left| \widehat {N} _ {2} \right| | y |.
$$

But defining $\widetilde{n}_k = [n_k^T 0]^T \in \mathbb{R}^n$ , we have

$$
\begin{array}{l} \left| \widehat {N} _ {k} \right| \dots \left| \widehat {N} _ {2} \right| = I + \left| \widetilde {n} _ {k} \right| e _ {k} ^ {T} + \dots + \left| \widetilde {n} _ {2} \right| e _ {2} ^ {T} \\ \leq | \hat {N} _ {n} | \dots | \hat {N} _ {2} | = | \hat {N} _ {n} \dots \hat {N} _ {2} | =: | X |, \\ \end{array}
$$

where $X = U^{-1} + O(u)$ (by (14.27)). Hence

$$
\begin{array}{l} \sum_ {k = 2} ^ {n} | \varDelta_ {k} | \leq (n - 1) \gamma_ {3} (1 + \gamma_ {3}) ^ {n - 2} | X | | U |, \\ \sum_ {k = 2} ^ {n} \left| f _ {k} \right| \leq (n - 1) \gamma_ {3} \left(1 + \gamma_ {3}\right) ^ {n - 2} | X | | y |. \\ \end{array}
$$

Combining (14.27) and (14.28) we have, for the solution of $Ux = y$ ,

$$
\widehat {x} = \left(I - \sum_ {k = 2} ^ {n} \varDelta_ {k}\right) U ^ {- 1} y + \sum_ {k = 2} ^ {n} f _ {k} = \left(I - \sum_ {k = 2} ^ {n} \varDelta_ {k}\right) x + \sum_ {k = 2} ^ {n} f _ {k},
$$

which gives the componentwise forward error bound

$$
\left| x - \hat {x} \right| \leq (n - 1) \gamma_ {3} \left(1 + \gamma_ {3}\right) ^ {n - 2} | X | \left(| U | | x | + | y |\right). \tag {14.29}
$$

This is an excellent forward error bound: it says that the error in $\widehat{x}$ is no larger than the error we would expect for an approximate solution with a tiny componentwise relative backward error. In other words, the forward error is bounded in the same way as for substitution. However, we have not, and indeed cannot, show that the method is backward stable. The best we can do is to derive from (14.27) and (14.28) the result

$$
(U + \Delta U) \widehat {x} = y + \Delta y, \tag {14.30a}
$$

$$
\left| \Delta U \right| \leq (n - 1) \gamma_ {3} \left(1 + \gamma_ {3}\right) ^ {n - 2} | U | | X | | U |, \tag {14.30b}
$$

$$
\left| \Delta y \right| \leq (n - 1) \gamma_ {3} \left(1 + \gamma_ {3}\right) ^ {n - 2} | U | | X | | y |, \tag {14.30c}
$$

using $\widehat{N}_2^{-1}\ldots \widehat{N}_n^{-1} = U + O(u)$ . These bounds show that, with respect to the system $Ux = y$ , $\widehat{x}$ has a normwise backward error bounded approximately by $\kappa_{\infty}(U)(n - 1)\gamma_3$ . Hence the backward error can be guaranteed to be small only if $U$ is well conditioned. This agrees with the comments of Peters and Wilkinson [938, 1975] that "the residuals corresponding to the Gauss-Jordan solution are often larger than those corresponding to back-substitution by a factor of order $\kappa$ ."

A numerical example helps to illustrate the results. We take $U$ to be the upper triangular matrix with 1s on the diagonal and -1s everywhere above the diagonal ( $U = U(1)$ from (8.3)). This matrix has condition number $\kappa_{\infty}(U) = n2^{n-1}$ . Table 14.6 reports the normwise relative backward error $\eta_{U,b}(\hat{x}) = \| U\hat{x} - b\|_{\infty} / (\| U\|_{\infty}\|\hat{x}\|_{\infty} + \| b\|_{\infty})$ (see (7.2)) for $b = Ux$ , where $x = e/3$ . Clearly, GJE is backward unstable for these matrices—the backward errors show a dependence on $\kappa_{\infty}(U)$ . However, the relative distance between $\hat{x}$ and the computed solution from substitution (not shown in the table) is less than $\kappa_{\infty}(U)u$ , which shows that the forward error is bounded by $\kappa_{\infty}(U)u$ , confirming (14.29).

By bringing in the error analysis for the reduction to upper triangular form, we obtain an overall result for GJE.

Table 14.6. GJE for $Ux = b$   

<table><tr><td>n</td><td>ηU,b(x̂)</td><td>κ∞(U)u</td></tr><tr><td>16</td><td>2.0e-14</td><td>5.8e-11</td></tr><tr><td>32</td><td>6.4e-10</td><td>7.6e-6</td></tr><tr><td>64</td><td>1.7e-2</td><td>6.6e4</td></tr></table>

Theorem 14.5. Suppose GJE successfully computes an approximate solution $\widehat{x}$ to $Ax = b$ , where $A \in \mathbb{R}^{n \times n}$ is nonsingular. Then

$$
| b - A \hat {x} | \leq 8 n u | \hat {L} | | \hat {U} | | \hat {U} ^ {- 1} | | \hat {U} | | \hat {x} | + O (u ^ {2}), \tag {14.31}
$$

$$
\left| x - \widehat {x} \right| \leq 2 n u \left(\left| A ^ {- 1} \right| \left| \widehat {L} \right| \left| \widehat {U} \right| + 3 \left| \widehat {U} ^ {- 1} \right| \left| \widehat {U} \right|\right) \left| \widehat {x} \right| + O \left(u ^ {2}\right), \tag {14.32}
$$

where $A\approx \widehat{L}\widehat{U}$ is the factorization computed by GE.

Proof. For the first stage (which is just GE), we have $A + \Delta A_1 = \widehat{L} \widehat{U}$ , $|\Delta A_1| \leq \gamma_n |\widehat{L}| |\widehat{U}|$ , and $(\widehat{L} + \Delta L) \widehat{y} = b$ , $|\Delta L| \leq \gamma_n |\widehat{L}|$ , by Theorems 9.3 and 8.5.

Using (14.30), we obtain

$$
(\widehat {L} + \Delta L) (\widehat {U} + \Delta U) \widehat {x} = (\widehat {L} + \Delta L) (\widehat {y} + \Delta y) = b + (\widehat {L} + \Delta L) \Delta y,
$$

or $A\widehat{x} = b - r$ , where

$$
r = \left(\Delta A _ {1} + \widehat {L} \Delta U + \Delta L \widehat {U} + \Delta L \Delta U\right) \widehat {x} - (\widehat {L} + \Delta L) \Delta y. \tag {14.33}
$$

The bound (14.31) follows. To obtain (14.32) we use (14.29) and incorporate the effects of the errors in computing $y$ . Defining $x_0$ by $\widehat{L} \widehat{U} x_0 = b$ , we have

$$
\boldsymbol {x} - \widehat {\boldsymbol {x}} = (\boldsymbol {x} - \boldsymbol {x} _ {0}) + (\boldsymbol {x} _ {0} - \widehat {\boldsymbol {U}} ^ {- 1} \widehat {\boldsymbol {y}}) + (\widehat {\boldsymbol {U}} ^ {- 1} \widehat {\boldsymbol {y}} - \widehat {\boldsymbol {x}}),
$$

where the last term is bounded by (14.29) and the first two terms are easily shown to be bounded by $\gamma_{n}|A^{-1}||\widehat{L} ||\widehat{U} ||\widehat{x} | + O(u^{2})$

Theorem 14.5 shows that the stability of GJE depends not only on the size of $|\widehat{L}||\widehat{U}|$ (as in GE), but also on the condition of $U$ . The vector $|\widetilde{U}^{-1}||\widehat{U}||\widehat{x}|$ is an upper bound for $|\widehat{x}|$ , and if this bound is sharp then the residual bound is very similar to that for LU factorization. Note that for partial pivoting we have

$$
\begin{array}{l} \left\| \left| \widehat {U} ^ {- 1} \right| \left| \widehat {U} \right| \right\| _ {\infty} \leq n \| A ^ {- 1} \| _ {\infty} \cdot n \rho_ {n} \| A \| _ {\infty} + O (u) \\ = n ^ {2} \rho_ {n} \kappa_ {\infty} (A) + O (u), \\ \end{array}
$$

and, similarly, $\| |A^{-1}||\widehat{L} ||\widehat{U} ||_{\infty}\leq n^{2}\rho_{n}\kappa_{\infty}(A)$ , so (14.32) implies

$$
\frac {\| x - \widehat {x} \| _ {\infty}}{\| x \| _ {\infty}} \leq 8 n ^ {3} \rho_ {n} \kappa_ {\infty} (A) u + O \left(u ^ {2}\right),
$$

which shows that GJE with partial pivoting is normwise forward stable.

The bounds in Theorem 14.5 have the pleasing property that they are invariant under row or column scaling of $A$ , though of course if we are using partial pivoting then row scaling can change the pivots and alter the bound.

As mentioned earlier, to obtain bounds for matrix inversion we simply take $b$ to be each of the unit vectors in turn. For example, the residual bound becomes

$$
\left| A \widehat {X} - I \right| \leq 8 n u | \widehat {L} | | \widehat {U} | | \widehat {U} ^ {- 1} | | \widehat {U} | | \widehat {X} | + O (u ^ {2}).
$$

The question arises of whether there is a significant class of matrices for which GJE is backward stable. The next result proves that GJE without pivoting is forward stable for symmetric positive definite matrices and provides a smaller residual bound than might be expected from Theorem 14.5. We make the natural assumption that symmetry is exploited in the elimination.

Corollary 14.6. Suppose GJE successfully computes an approximate solution $\widehat{x}$ to $Ax = b$ , where $A \in \mathbb{R}^{n \times n}$ is symmetric positive definite. Then, provided the computed pivots are positive,

$$
\| b - A \widehat {x} \| _ {2} \leq 8 n ^ {3} u \kappa_ {2} (A) ^ {1 / 2} \| A \| _ {2} \| x \| _ {2} + O \left(u ^ {2}\right),
$$

$$
\frac {\| x - \widehat {x} \| _ {2}}{\| x \| _ {2}} \leq 8 n ^ {5 / 2} u \kappa_ {2} (A) + O \left(u ^ {2}\right),
$$

where $A \approx \widehat{L} \widehat{U}$ is the factorization computed by symmetric GE.

Proof. By Theorem 9.3 we have $A + \Delta A = \widehat{L}\widehat{U}$ , where $\Delta A$ is symmetric and satisfies $|\Delta A| \leq \gamma_n|\widehat{L}||\widehat{U}|$ . Defining $D = \mathrm{diag}(\widehat{U})^{1/2}$ we have, by symmetry, $A + \Delta A = \widehat{L}D \cdot D^{-1}\widehat{U} \equiv R^T R$ . Hence

$$
\begin{array}{l} \| | \widehat {U} ^ {- 1} | | \widehat {U} | \| _ {2} = \| | R ^ {- 1} D ^ {- 1} | | D R | \| _ {2} \\ = \left\| \left| R ^ {- 1} \right| \right\| R \| _ {2} \\ \leq n \kappa_ {2} (R) = n \kappa_ {2} (A + \Delta A) ^ {1 / 2} \\ = n \kappa_ {2} (A) ^ {1 / 2} + O (u). \\ \end{array}
$$

Furthermore, it is straightforward to show that $\| |\widehat{L} ||\widehat{U} ||_2 = \| |R^T ||R||_2 \leq n(1 - n\gamma_n)^{-1}\| A\| _2$ . The required bounds follow (note that the first term on the right-hand side of (14.32) dominates).

Our final result shows that if $A$ is row diagonally dominant then GJE without pivoting is both forward stable and row-wise backward stable (see Table 7.1).

Corollary 14.7. If GJE successfully computes an approximate solution $\widehat{x}$ to $Ax = b$ , where $A \in \mathbb{R}^{n \times n}$ is row diagonally dominant, then

$$
\begin{array}{l} \left| b - A \widehat {x} \right| \leq 3 2 n ^ {2} u | A | e e ^ {T} | \widehat {x} | + O \left(u ^ {2}\right), \\ \frac {\| x - \widehat {x} \| _ {\infty}}{\| x \| _ {\infty}} \leq 4 n ^ {3} u \left(\kappa_ {\infty} (A) + 3\right) + O \left(u ^ {2}\right). \\ \end{array}
$$

Proof. The bounds follow from Theorem 14.5 on noting that $U$ is row diagonally dominant and using Lemma 8.8 to bound $\operatorname{cond}(U)$ and (9.17) to bound $\| |L||U| \|_{\infty}$ .

# 14.5. Parallel Inversion Methods

Vavasis [1192, 1989] shows that GEPP is P-complete, a complexity result whose implication is that GEPP cannot be efficiently implemented on a highly parallel computer with a large number of processors. This result provides motivation for looking for non-GE-based methods for solving linear systems on massively parallel machines. In this section we briefly describe some matrix inversion methods whose computational complexity makes them contenders for linear system solution on parallel, and perhaps other, machines.

Csanky [285, 1976] gives a method for inverting an $n \times n$ matrix (and thereby solving a linear system) in $O(\log^2 n)$ time on $O(n^4)$ processors. This method has optimal computational complexity amongst known methods for massively parallel machines, but it involves the use of the characteristic polynomial and it has abysmal numerical stability properties (as can be seen empirically by applying the method to $3I$ , for example!).

A more practical method is Newton's method for $A^{-1}$ , which is known as the Schulz iteration [1027, 1933]:

$$
X _ {k + 1} = X _ {k} (2 I - A X _ {k}) = (2 I - X _ {k} A) X _ {k}.
$$

It is known that $X_{k}$ converges to $A^{-1}$ (or, more generally, to the pseudo-inverse if $A$ is rectangular) if $X_0 = \alpha_0A^T$ and $0 < \alpha_0 < 2 / \| A\| _2^2$ [1056, 1974]. The Schulz iteration is attractive because it involves only matrix multiplication—an operation that can be implemented very efficiently on high-performance computers. The rate of convergence is quadratic, since if $E_{k} = I - AX_{k}$ or $E_{k} = I - X_{k}A$ then

$$
E _ {k + 1} = E _ {k} ^ {2} = \dots = E _ {0} ^ {2 ^ {k + 1}}.
$$

Like Csanky's method, the Schulz iteration has polylogarithmic complexity, but, unlike Csanky's method, it is numerically stable [1056, 1974]. Unfortunately, for scalar $a > 0$ ,

$$
0 <   x _ {k} \ll a ^ {- 1} \Rightarrow x _ {k + 1} = 2 x _ {k} - x _ {k} a x _ {k} \lesssim 2 x _ {k},
$$

and since $x_{k} \to a^{-1}$ , convergence can initially be slow. Overall, about $2\log_2\kappa_2(A)$ iterations are required for convergence in floating point arithmetic. Pan and Schreiber [919, 1991] show how to accelerate the convergence by at least a factor 2 via scaling parameters and how to use the iteration to carry out rank and projection calculations. For an interesting application of the Schulz iteration to a sparse matrix possessing a sparse inverse, see [14, 1993], and for its adaptation to Toeplitz-like (low displacement rank) matrices see [917, 2001, Chap. 6] and [918, 1999].

For inverting triangular matrices a divide and conquer method with polylogarithmic complexity is readily derived. See Higham [605, 1995] for details and error analysis.

Another inversion method is one of Strassen, which makes use of his fast matrix multiplication method: see Problem 23.8 and §26.3.2.

# 14.6. The Determinant

It may be too optimistic to hope that determinants will fade out of the mathematical picture in a generation; their notation alone is a thing of beauty to those who can appreciate that sort of beauty.

— E. T. BELL, Review of "Contributions to the History of Determinants, 1900-1920", by Sir Thomas Muir (1931)

Like the matrix inverse, the determinant is a quantity that rarely needs to be computed. The common fallacy that the determinant is a measure of ill conditioning is displayed by the observation that if $Q \in \mathbb{R}^{n \times n}$ is orthogonal then $\operatorname*{det}(\alpha Q) = \alpha^n \operatorname*{det}(Q) = \pm \alpha^n$ , which can be made arbitrarily small or large despite the fact that $\alpha Q$ is perfectly conditioned. Of course, we could normalize the matrix before taking its determinant and define, for example,

$$
\psi (A) := \frac {1}{\operatorname * {d e t} (D ^ {- 1} A)} = \frac {\operatorname * {d e t} (D)}{\operatorname * {d e t} (A)}, \qquad D = \mathrm {d i a g} (\left\| A (i,:) \right\| _ {2}),
$$

where $D^{-1}A$ has rows of unit 2-norm. This function $\psi$ is called the Hadamard condition number by Birkhoff [112, 1975], because Hadamard's determinantal inequality (see Problem 14.11) implies that $\psi(A) \geq 1$ , with equality if and only if $A$ has mutually orthogonal rows. Unless $A$ is already row equilibrated (see Problem 14.13), $\psi(A)$ does not relate to the conditioning of linear systems in any straightforward way.

As good a way as any to compute the determinant of a general matrix $A \in \mathbb{R}^{n \times n}$ is via GEPP. If $PA = LU$ then

$$
\det (A) = \det (P) ^ {- 1} \det (U) = (- 1) ^ {r} u _ {1 1} \dots u _ {n n}, \tag {14.34}
$$

where $r$ is the number of row interchanges during the elimination. If we use (14.34) then, barring underflow and overflow, the computed determinant $\widehat{d} = fl(\det(A))$ satisfies

$$
\widehat {d} = \det  (\widehat {U}) (1 + \theta_ {n}),
$$

where $|\theta_n| \leq \gamma_n$ , so we have a tiny relative perturbation of the exact determinant of a perturbed matrix $A + \Delta A$ , where $\Delta A$ is bounded in Theorem 9.3. In other words, we have almost the right determinant for a slightly perturbed matrix (assuming the growth factor is small).

However, underflow and overflow in computing the determinant are quite likely, and the determinant itself may not be a representable number. One possibility is to compute $\log |\operatorname{det}(A)| = \sum_{i=1}^{n} \log |u_{ii}|$ ; as pointed out by Forsythe and Moler [431, 1967, p. 55], however, the computed sum may be inaccurate due to cancellation. Another approach, used in LINPACK, is to compute and represent $\operatorname{det}(A)$ in the form $y \times 10^e$ , where $1 \leq |y| < 10$ and $e$ is an integer exponent.

# 14.6.1. Hyman's Method

In §1.16 we analysed the evaluation of the determinant of a Hessenberg matrix $H$ by GE. Another method for computing $\operatorname{det}(H)$ is Hyman's method [652, 1957], which is superficially similar to GE but algorithmically different. Hyman's method has an easy derivation in terms of LU factorization that leads to a very short error analysis. Let $H \in \mathbb{R}^{n \times n}$ be an unreduced upper Hessenberg matrix ( $h_{i+1,i} \neq 0$ for all $i$ ) and write

$$
H = \left[ \begin{array}{l l} h ^ {T} & \eta \\ T & y \end{array} \right], \qquad H _ {1} = \left[ \begin{array}{l l} T & y \\ h ^ {T} & \eta \end{array} \right], \qquad h, y \in \mathbb {R} ^ {n - 1}, \eta \in \mathbb {R}.
$$

The matrix $H_{1}$ is $H$ with the first row cyclically permuted to the bottom, so $\operatorname{det}(H_{1}) = (-1)^{n - 1}\operatorname{det}(H)$ . Since $T$ is a nonsingular upper triangular matrix, we have the LU factorization

$$
H _ {1} = \left[ \begin{array}{c c} I & 0 \\ h ^ {T} T ^ {- 1} & 1 \end{array} \right] \left[ \begin{array}{c c} T & y \\ 0 & \eta - h ^ {T} T ^ {- 1} y \end{array} \right] \equiv L U, \tag {14.35}
$$

from which we obtain $\operatorname{det}(H_1) = \operatorname{det}(T)(\eta - h^T T^{-1}y)$ . Therefore

$$
\det (H) = (- 1) ^ {n - 1} \det (T) (\eta - h ^ {T} T ^ {- 1} y). \tag {14.36}
$$

Hyman's method consists of evaluating (14.36) in the natural way: by solving the triangular system $Tx = y$ by back substitution, then forming $\eta - h^T x$ and its product with $\operatorname{det}(T) = h_{21}h_{32}\ldots h_{n,n-1}$ .

For the error analysis we assume that no underflows or overflows occur. From the backward error analysis for substitution (Theorem 8.5) and for an inner product (see (3.4)) we have immediately, on defining $\mu \coloneqq \eta - h^T T^{-1} y$ ,

$$
\widehat {\mu} = \left(\eta - (h + \Delta h) ^ {T} (T + \Delta T) ^ {- 1} y\right) (1 + \delta),
$$

where

$$
\left| \Delta h \right| \leq \gamma_ {n - 1} | h |, \quad \left| \Delta T \right| \leq \gamma_ {n - 1} | T |, \quad | \delta | \leq u.
$$

The computed determinant therefore satisfies

$$
\widehat {d} := f l (\det  (H)) = \left(1 + \theta_ {n}\right) \det  (T) \left(\eta - (h + \Delta h) ^ {T} (T + \Delta T) ^ {- 1} y\right),
$$

where $|\theta_n| \leq \gamma_n$ . This is not a backward error result, because only one of the two $T_s$ in this expression is perturbed. However, we can write $\operatorname{det}(T) = \operatorname{det}(T + \Delta T)(1 + \theta_{(n-1)^2})$ , so that

$$
\widehat {d} = \det  (T + \varDelta T) \big (\eta (1 + \theta_ {n ^ {2} - n + 1}) - (h + \varDelta h) ^ {T} (T + \varDelta T) ^ {- 1} y (1 + \theta_ {n ^ {2} - n + 1}) \big).
$$

We conclude that the computed determinant is the exact determinant of a perturbed Hessenberg matrix in which each element has undergone a relative perturbation not exceeding $\gamma_{n^2 - n + 1} \approx n^2 u$ , which is a very satisfactory result. In fact, the constant $\gamma_{n^2 - n + 1}$ can be reduced to $\gamma_{2n - 1}$ by a slightly modified analysis; see Problem 14.14.

# 14.7. Notes and References

Classic references on matrix inversion are Wilkinson's paper *Error Analysis of Direct Methods of Matrix Inversion* [1229, 1961] and his book *Rounding Errors in Algebraic Processes* [1232, 1963]. In discussing Method 1 of §14.2.1, Wilkinson says "The residual of $X$ as a left-hand inverse may be larger than the residual as a right-hand inverse by a factor as great as $\| L\| \| L^{-1}\| \ldots$ . We are asserting that the computed $X$ is almost invariably of such a nature that $XL - I$ is equally small" [1232, 1963, p. 107]. Our experience concurs with the latter statement. Triangular matrix inversion provides a good example of the value of rounding error analysis: it helps us identify potential instabilities, even if they are rarely manifested in practice, and it shows us what kind of stability is guaranteed to hold.

In [1229, 1961] Wilkinson identifies various circumstances in which triangular matrix inverses are obtained to much higher accuracy than the bounds of this chapter suggest. The results of §8.2 provide some insight. For example, if $T$ is a triangular $M$ -matrix then, as noted after Corollary 8.11, its inverse is computed to high relative accuracy, no matter how ill conditioned $L$ may be.

Sections 14.2 and 14.3 are based closely on Du Croz and Higham [357, 1992].

Method D in §14.3.4 is used by the Hewlett-Packard HP-15C calculator, for which the method's lack of need for extra storage is an important property [570, 1982].

GJE is an old method. It was discovered independently by the geodesist Wilhelm Jordan (1842-1899) (not the mathematician Camille Jordan (1838-1922)) and B.-I. Clasen [16, 1987].

An Algol routine for inverting positive definite matrices by GJE was published in the Handbook for Automatic Computation by Bauer and Reinsch [94, 1971]. As a means of solving a single linear system, GJE is $50\%$ more expensive than GE when cost is measured in flops; the reason is that GJE takes $O(n^{3})$ flops to solve the upper triangular system that GE solves in $n^2$ flops. However, GJE has attracted interest for vector computing because it maintains full vector lengths throughout the algorithm. Hoffmann [633, 1987] found that it was faster than GE on the CDC Cyber 205, a now-defunct machine with a relatively large vector startup overhead.

Turing [1166, 1948] gives a simplified analysis of the propagation of errors in GJE, obtaining a forward error bound proportional to $\kappa(A)$ . Bauer [91, 1966] does a componentwise forward error analysis of GJE for matrix inversion and obtains a relative error bound proportional to $\kappa_{\infty}(A)$ for symmetric positive definite $A$ . Bauer's paper is in German and his analysis is not easy to follow. A summary of Bauer's analysis (in English) is given by Meinguet [839, 1969].

The first thorough analysis of the stability of GJE was by Peters and Wilkinson [938, 1975]. Their paper is a paragon of rounding error analysis. Peters and Wilkinson observe the connection with GE, then devote their attention to the "second stage" of GJE, in which $Ux = y$ is solved. They show that each component of $x$ is obtained by solving a lower triangular system, and they deduce that, for each $i$ , $(U + \Delta U_i)x^{(i)} = y + \Delta y_i$ , where $|\Delta U_i| \leq \gamma_n |U|$ and $|\Delta y_i| \leq \gamma_n |y|$ , and where the $i$ th component of $x^{(i)}$ is the $i$ th component of $\widehat{x}$ . They then show that $\widehat{x}$ has relative error bounded by $2n\kappa_{\infty}(U)u + O(u^2)$ , but that $\widehat{x}$ does not necessarily

have a small backward error. The more direct approach used in our analysis is similar to that of Dekker and Hoffmann [303, 1989], who give a normwise analysis of a variant of GJE that uses row pivoting (elimination across rows) and column interchanges.

Peters and Wilkinson [938, 1975] state that "it is well known that Gauss-Jordan is stable" for a diagonally dominant matrix. In the first edition of this book we posed proving this statement as a research problem. In answer to this question, Malyshev [811, 2000] shows that normwise backward stability is easily proved using Theorem 14.5, as shown in Corollary 14.7. Our observation that row-wise backward stability holds is new. Malyshev also shows that GJE without pivoting is backward unstable for matrices diagonally dominant by columns.

Goodnight [512, 1979] describes the use of GJE in statistics for solving least squares problems. Parallel implementation of GJE is discussed by Quintana, Quintana, Sun, and van de Geijn [966, 2001].

Demmel [316, 1993] points out the numerical instability of Csanky's method. For discussion of the numerical properties of Csanky's method and the Schulz iteration from a computational complexity viewpoint see Codenotti, Leoncini and Preparata [248, 2001].

For an application of the Hadamard condition number see Burdakov [184, 1997].

Error analysis of Hyman's method is given by Wilkinson [1228, 1960], [1232, 1963, pp. 147-154], [1233, 1965, pp. 426-431]. Although it dates from the 1950s, Hyman's method is not obsolete: it has found use in methods designed for high-performance computers; see Ward [1207, 1976], Li and Zeng [784, 1992], and Dubrulle and Golub [359, 1994].

Some fundamental problems in computational geometry can be reduced to testing the sign of the determinant of a matrix, so the question arises of how to be sure that the sign is determined correctly in floating point arithmetic. For work on this problem see Pan and Yu [920, 2001] and the references therein.

Intimately related to the matrix inverse is the adjugate matrix,

$$
\operatorname {a d j} (A) = \left((- 1) ^ {i + j} \det  (A _ {j i})\right),
$$

where $A_{ij}$ denotes the submatrix of $A$ obtained by deleting row $i$ and column $j$ . Thus the adjugate is the transpose of the matrix of cofactors of $A$ , and for nonsingular $A$ , $A^{-1} = \operatorname{adj}(A) / \det(A)$ . Stewart [1081, 1998] shows that the adjugate can be well conditioned even when $A$ is ill conditioned, and he shows how $\operatorname{adj}(A)$ can be computed in a numerically stable way from a rank revealing decomposition of $A$ .

# 14.7.1. LAPACK

LAPACK contains computational routines, but not high-level drivers, for matrix inversion. Routine xGETRI computes the inverse of a general square matrix by Method B using an LU factorization computed by xGETRF. The corresponding routine for a symmetric positive definite matrix is xPOTRI, which uses Method D, with a Cholesky factorization computed by xPOTRF. Inversion of a symmetric indefinite matrix is done by xSYTRI. Triangular matrix inversion is done by xTRTRI,

which uses Method 2C. None of the LAPACK routines computes the determinant, but it is easy for the user to evaluate it after computing an LU factorization.

# Problems

14.1. Reflect on this cautionary tale told by Acton [4, 1970, p. 246].

It was 1949 in Southern California. Our computer was a very new CPC (model 1, number 1)—a 1-second-per-arithmetic-operation clunker that was holding the computational fort while an early electronic monster was being coaxed to life in an adjacent room. From a nearby aircraft company there arrived one day a $16 \times 16$ matrix of 10-digit numbers whose inverse was desired ... We labored for two days and, after the usual number of glitches that accompany any strange procedure involving repeated handling of intermediate decks of data cards, we were possessed of an inverse matrix. During the checking operations ... it was noted that, to eight significant figures, the inverse was the transpose of the original matrix! A hurried visit to the aircraft company to explore the source of the matrix revealed that each element had been laboriously hand computed from some rather simple combinations of sines and cosines of a common angle. It took about 10 minutes to prove that the matrix was, indeed, orthogonal!

14.2. Rework the analysis of the methods of §14.2.2 using the assumptions (13.4) and (13.5), thus catering for possible use of fast matrix multiplication techniques.

14.3. Show that for any nonsingular matrix $A$ ,

$$
\kappa (A) \geq \operatorname * {m a x} \left\{\frac {\| A X - I \|}{\| X A - I \|}, \frac {\| X A - I \|}{\| A X - I \|} \right\}.
$$

This inequality shows that the left and right residuals of $X$ as an approximation to $A^{-1}$ can differ greatly only if $A$ is ill conditioned.

14.4. (Mendelsohn [841, 1956]) Find parametrized $2 \times 2$ matrices $A$ and $X$ such that the ratio $\|AX - I\| / \|XA - I\|$ can be made arbitrarily large.

14.5. Let $X$ and $Y$ be approximate inverses of $A \in \mathbb{R}^{n \times n}$ that satisfy

$$
| A \widehat {X} - I | \leq u | A | | \widehat {X} | \quad \mathrm {a n d} \quad | \widehat {Y} A - I | \leq u | \widehat {Y} | | A |,
$$

and let $\widehat{x} = fl(\widehat{X} b)$ and $\widehat{y} = fl(\widehat{Y} b)$ . Show that

$$
| A \widehat {x} - b | \leq \gamma_ {n + 1} | A | | \widehat {X} | | b | \quad \mathrm {a n d} \quad | A \widehat {y} - b | \leq \gamma_ {n + 1} | A | | \widehat {Y} | | A | | x |.
$$

Derive forward error bounds for $\widehat{x}$ and $\widehat{y}$ . Interpret all these bounds.

14.6. What is the inverse of the matrix on the front cover of the LAPACK Users' Guide [20, 1999]? (The first two editions gave the inverse on the back cover.) Answer the same question for the LINPACK Users' Guide [341, 1979].

14.7. Show that for any matrix having a row or column of 1s, the elements of the inverse sum to 1.

14.8. Let $X = A + iB \in \mathbb{C}^{n \times n}$ be nonsingular, where $A$ and $B$ are real. Show that $X^{-1}$ can be expressed in terms of the inverse of the real matrix of order $2n$ ,

$$
Y = \left[ \begin{array}{c c} A & - B \\ B & A \end{array} \right].
$$

Show that if $X$ is Hermitian positive definite then $Y$ is symmetric positive definite. Compare the economics of real versus complex inversion.

14.9. For a given nonsingular $A \in \mathbb{R}^{n \times n}$ and $X \approx A^{-1}$ , it is interesting to ask what is the smallest $\epsilon$ such that $X + \Delta X = (A + \Delta A)^{-1}$ with $\| \Delta X \| \leq \epsilon \| X \|$ and $\| \Delta A \| \leq \epsilon \| A \|$ . We require $(A + \Delta A)(X + \Delta X) = I$ , or

$$
A \Delta X + \Delta A X + \Delta A \Delta X = I - A X.
$$

It is reasonable to drop the second-order term, leaving a generalized Sylvester equation that can be solved using singular value decompositions of $A$ and $X$ (cf. §16.2). Investigate this approach computationally for a variety of $A$ and methods of inversion.

14.10. For a nonsingular $A \in \mathbb{R}^{n \times n}$ and given integers $i$ and $j$ , under what conditions is $\operatorname{det}(A)$ independent of $a_{ij}$ ? What does this imply about the suitability of $\operatorname{det}(A)$ for measuring conditioning?

14.11. Prove Hadamard's inequality for $A \in \mathbb{C}^{n \times n}$ :

$$
| \det  (A) | \leq \prod_ {k = 1} ^ {n} \| a _ {k} \| _ {2},
$$

where $a_{k} = A(:, k)$ . When is there equality? (Hint: use the QR factorization.)

14.12. (a) Show that if $A^T = QR$ is a QR factorization then the Hadamard condition number $\psi(A) = \prod_{i=1}^{n} \rho_i / |r_{ii}|$ , where $\rho_i = \| R(:, i) \|_2$ . (b) Evaluate $\psi(A)$ for $A = U(1)$ (see (8.3)) and for the Pei matrix $A = (\alpha - 1)I + ee^T$ .

14.13. (Guggenheimer, Edelman, and Johnson [530, 1995]) (a) Prove that for a nonsingular $A \in \mathbb{R}^{n \times n}$ ,

$$
\kappa_ {2} (A) <   \frac {2}{| \det  (A) |} \left(\frac {\| A \| _ {F}}{n ^ {1 / 2}}\right) ^ {n}. \tag {14.37}
$$

(Hint: apply the arithmetic-geometric mean inequality to the $n$ numbers $\sigma_1^2 / 2$ , $\sigma_1^2 / 2$ , $\sigma_2^2$ , ..., $\sigma_{n-1}^2$ , where the $\sigma_i$ are the singular values of $A$ .) (b) Deduce that if $A$ has rows of unit 2-norm then

$$
\kappa_ {2} (A) <   \frac {2}{| \det  (A) |} = 2 \psi (A),
$$

where $\psi$ is the Hadamard condition number. For more on this type of bound see [842, 1997], and for a derivation of (14.37) from a different perspective see [336, 1993].

14.14. Show that Hyman's method for computing $\operatorname{det}(H)$ , where $H \in \mathbb{R}^{n \times n}$ is an unreduced upper Hessenberg matrix, computes the exact determinant of $H + \Delta H$ where $|\Delta H| \leq \gamma_{2n-1}|H|$ , barring underflow and overflow. What is the effect on the error bound of a diagonal similarity transformation $H \to D^{-1}HD$ , where $D = \operatorname{diag}(d_i)$ , $d_i \neq 0$ ?

14.15. (Godunov, Antonov, Kiriljuk, and Kostin [493, 1993]) Show that if $A \in \mathbb{R}^{n \times n}$ and $\kappa_2(A)\| \Delta A\| _2 / \| A\| _2 < 1$ then

$$
\frac {\left| \det (A + \varDelta A) - \det (A) \right|}{\det (A)} \leq \frac {n \kappa_ {2} (A) \frac {\left\| \varDelta A \right\| _ {2}}{\left\| A \right\| _ {2}}}{1 - n \kappa_ {2} (A) \frac {\left\| \varDelta A \right\| _ {2}}{\left\| A \right\| _ {2}}}.
$$
