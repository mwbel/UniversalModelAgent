# Chapter 10

# Cholesky Factorization

The matrix of that equation system is negative definite—which is a positive definite system that has been multiplied through by $-1$ . For all practical geometries the common finite difference Laplacian operator gives rise to these, the best of all possible matrices. Just about any standard solution method will succeed, and many theorems are available for your pleasure.

FORMAN S. ACTON, Numerical Methods That Work (1970)

Many years ago we made out of half a dozen transformers a simple and rather inaccurate machine for solving simultaneous equations—the solutions being represented as flux in the cores of the transformers. During the course of our experiments we set the machine to solve the equations—

$$
X + Y + Z = 1
$$

$$
X + Y + Z = 2
$$

$$
X + Y + Z = 3
$$

The machine reacted sharply—it blew the main fuse and put all the lights out.

B.V.BOWDEN,The Organization of a Typical Machine (1953)

There does seem to be some misunderstanding about the purpose of an a priori backward error analysis. All too often, too much attention is paid to the precise error bound that has been established. The main purpose of such an analysis is either to establish the essential numerical stability of an algorithm or to show why it is unstable and in doing so to expose what sort of change is necessary to make it stable. The precise error bound is not of great importance.

— J. H. WILKINSON, Numerical Linear Algebra on Digital Computers (1974)

# 10.1. Symmetric Positive Definite Matrices

Symmetric positive definiteness is one of the highest accolades to which a matrix can aspire. Symmetry confers major advantages and simplifications in the eigenproblem and, as we will see in this chapter, positive definiteness permits economy and numerical stability in the solution of linear systems.

A symmetric matrix $A \in \mathbb{R}^{n \times n}$ is positive definite if $x^T A x > 0$ for all nonzero $x \in \mathbb{R}^n$ . Well-known equivalent conditions to $A = A^T$ being positive definite are

- $\det(A_k) > 0$ , $k = 1:n$ , where $A_k = A(1:k,1:k)$ is the leading principal submatrix of order $k$ .   
- $\lambda_{k}(A) > 0$ , $k = 1:n$ , where $\lambda_{k}$ denotes the $k$ th largest eigenvalue.

The first of these conditions implies that $A$ has an LU factorization, $A = LU$ (see Theorem 9.1). Another characterization of positive definiteness is that the pivots in LU factorization are positive, since $u_{kk} = \operatorname*{det}(A_k) / \operatorname*{det}(A_{k - 1})$ . By factoring out the diagonal of $U$ and taking its square root, the LU factorization can be converted into a Cholesky factorization: $A = R^T R$ , where $R$ is upper triangular with positive diagonal elements. This factorization is so important that it merits a direct proof.

Theorem 10.1. If $A \in \mathbb{R}^{n \times n}$ is symmetric positive definite then there is a unique upper triangular $R \in \mathbb{R}^{n \times n}$ with positive diagonal elements such that $A = R^T R$ .

Proof. The proof is by induction. The result is clearly true for $n = 1$ . Assume it is true for $n - 1$ . The leading principal submatrix $A_{n - 1} = A(1:n - 1,1:n - 1)$ is positive definite, so it has a unique Cholesky factorization $A_{n - 1} = R_{n - 1}^T R_{n - 1}$ . We have a factorization

$$
A = \left[ \begin{array}{c c} A _ {n - 1} & c \\ c ^ {T} & \alpha \end{array} \right] = \left[ \begin{array}{c c} R _ {n - 1} ^ {T} & 0 \\ r ^ {T} & \beta \end{array} \right] \left[ \begin{array}{c c} R _ {n - 1} & r \\ 0 & \beta \end{array} \right] =: R ^ {T} R \tag {10.1}
$$

if

$$
R _ {n - 1} ^ {T} r = c, \tag {10.2}
$$

$$
r ^ {T} r + \beta^ {2} = \alpha . \tag {10.3}
$$

Equation (10.2) has a unique solution since $R_{n-1}$ is nonsingular. Then (10.3) gives $\beta^2 = \alpha - r^T r$ . It remains to check that there is a unique real, positive $\beta$ satisfying this equation. From the equation

$$
0 <   \det (A) = \det (R ^ {T}) \det (R) = \det (R _ {n - 1}) ^ {2} \beta^ {2}
$$

we see that $\beta^2 > 0$ , hence there is a unique $\beta > 0$ .

The proof of the theorem is constructive, and provides a way to compute the Cholesky factorization that builds $R$ a column at a time. Alternatively, we can work directly from the equations

$$
a _ {i j} = \sum_ {k = 1} ^ {i} r _ {k i} r _ {k j}, \quad j \geq i,
$$

which follow by equating $(i,j)$ elements in $A = R^T R$ . By solving these equations in the order $(1,1)$ , $(1,2)$ , $(2,2)$ , $(1,3)$ , $(2,3)$ , $(3,3)$ , $\ldots$ , $(n,n)$ , we obtain the following algorithm.

Algorithm 10.2 (Cholesky factorization). Given a symmetric positive definite $A \in \mathbb{R}^{n \times n}$ this algorithm computes the Cholesky factorization $A = R^T R$ .

for $j = 1:n$

for $i = 1:j - 1$

$$
r _ {i j} = \left(a _ {i j} - \sum_ {k = 1} ^ {i - 1} r _ {k i} r _ {k j}\right) / r _ {i i}
$$

end

$$
r _ {j j} = \left(a _ {j j} - \sum_ {k = 1} ^ {j - 1} r _ {k j} ^ {2}\right) ^ {1 / 2}
$$

end

Cost: $n^3 / 3$ flops (half the cost of LU factorization).

As for Gaussian elimination (GE), there are different algorithmic forms of Cholesky factorization. Algorithm 10.2 is the jik or "sdot" form. We describe the kij, outer product form in §10.3.

Given the Cholesky factorization $A = R^T R$ , a linear system $Ax = b$ can be solved via the two triangular systems $R^T y = b$ and $Rx = y$ .

If we define $D = \mathrm{diag}(r_{ii}^2)$ then the Cholesky factorization $A = R^{T}R$ can be rewritten as $A = LDL^{T}$ , where $L = R^{T}\mathrm{diag}(r_{ii})^{-1}$ is unit lower triangular. The $LDL^{\mathrm{T}}$ factorization is sometimes preferred over the Cholesky factorization because it avoids the need to compute the $n$ square roots that determine the $r_{ii}$ . The $LDL^{\mathrm{T}}$ factorization is certainly preferred for solving tridiagonal systems, as it requires $n$ fewer divisions than Cholesky factorization in the substitution stage. All the results for Cholesky factorization in this chapter have analogues for the $LDL^{\mathrm{T}}$ factorization. Block $LDL^{\mathrm{T}}$ factorization for indefinite matrices is discussed in §11.1.

# 10.1.1. Error Analysis

Error bounds for Cholesky factorization are derived in a similar way to those for LU factorization. Consider Algorithm 10.2. Using Lemma 8.4 we have

$$
\left| a _ {i j} - \sum_ {k = 1} ^ {i} \widehat {r} _ {k i} \widehat {r} _ {k j} \right| \leq \gamma_ {i} \sum_ {k = 1} ^ {i} | \widehat {r} _ {k i} | | \widehat {r} _ {k j} |. \tag {10.4}
$$

From a variation of Lemma 8.4 in which the division is replaced by a square root (see Problem 10.3), we have

$$
\left| a _ {j j} - \sum_ {k = 1} ^ {j} \widehat {r} _ {k j} ^ {2} \right| \leq \gamma_ {j + 1} \sum_ {k = 1} ^ {j} \widehat {r} _ {k j} ^ {2}.
$$

A backward error result is immediate.

Theorem 10.3. If Cholesky factorization applied to the symmetric positive definite matrix $A \in \mathbb{R}^{n \times n}$ runs to completion then the computed factor $\widehat{R}$ satisfies

$$
\widehat {R} ^ {T} \widehat {R} = A + \Delta A, \quad | \Delta A | \leq \gamma_ {n + 1} | \widehat {R} ^ {T} | | \widehat {R} |. \quad \square \tag {10.5}
$$

Theorem 10.4. Let $A \in \mathbb{R}^{n \times n}$ be symmetric positive definite and suppose Cholesky factorization produces a computed factor $\widehat{R}$ and a computed solution $\widehat{x}$ to $Ax = b$ . Then

$$
(A + \Delta A) \widehat {x} = b, \quad | \Delta A | \leq \gamma_ {3 n + 1} | \widehat {\boldsymbol {R}} ^ {T} | | \widehat {\boldsymbol {R}} |. \tag {10.6}
$$

Proof. The proof is analogous to the proof of Theorem 9.4. $\square$

These results imply that Cholesky factorization enjoys perfect normwise backward stability. The key inequality is (using Lemma 6.6)

$$
\| | R ^ {T} | | R | \| _ {2} = \| | R | \| _ {2} ^ {2} \leq n \| R \| _ {2} ^ {2} = n \| A \| _ {2},
$$

whose analogue for the computed $\widehat{R}$ is, from (10.5),

$$
\| | \widehat {R} ^ {T} | | \widehat {R} | \| _ {2} \leq n (1 - n \gamma_ {n + 1}) ^ {- 1} \| A \| _ {2}.
$$

Thus (10.6) implies

$$
\left\| \Delta A \right\| _ {2} \leq \left\| \left| \Delta A \right| \right\| _ {2} \leq \gamma_ {3 n + 1} n \left(1 - n \gamma_ {n + 1}\right) ^ {- 1} \| A \| _ {2} \leq 4 n (3 n + 1) u \| A \| _ {2}, \tag {10.7}
$$

where for the last inequality we have assumed that $\max((3n + 1)u, n\gamma_{n+1}) < 1/2$ . Another indicator of stability is that the growth factor for GE is exactly 1 (see Problem 10.4). It is important to realize that the multipliers can be arbitrarily large (consider, for example, $\left[ \begin{array}{cc} \theta^2 & \theta \\ \theta & 2 \end{array} \right]$ as $\theta \to 0$ ). But, remarkably, for a positive definite matrix the size of the multipliers has no effect on stability.

Note that the perturbation $\Delta A$ in (10.6) is not symmetric, in general, because the backward error matrices for the triangular solves with $R$ and $R^T$ are not the transposes of each other. For conditions guaranteeing that a "small" symmetric $\Delta A$ can be found, see Problem 7.12.

The following rewritten version of Theorem 10.3 provides further insight into Cholesky factorization.

Theorem 10.5 (Demmel). If Cholesky factorization applied to the symmetric positive definite matrix $A \in \mathbb{R}^{n \times n}$ runs to completion then the computed factor $\widehat{R}$ satisfies

$$
\widehat {R} ^ {T} \widehat {R} = A + \Delta A, \quad | \Delta A | \leq (1 - \gamma_ {n + 1}) ^ {- 1} \gamma_ {n + 1} d d ^ {T},
$$

where $d_{i} = a_{ii}^{1 / 2}$

Proof. Theorem 10.3 shows that $\widehat{R}^T\widehat{R} = A + \Delta A$ with $|\Delta A| \leq \gamma_{n+1} |\widehat{R}^T||\widehat{R}|$ . Denoting by $\widehat{r}_i$ the $i$ th column of $\widehat{R}$ , we have

$$
\| \widehat {r} _ {i} \| _ {2} ^ {2} = \widehat {r} _ {i} ^ {T} \widehat {r} _ {i} = a _ {i i} + \Delta a _ {i i} \leq a _ {i i} + \gamma_ {n + 1} | \widehat {r} _ {i} | ^ {T} | \widehat {r} _ {i} |,
$$

so that $\| \widehat{r_i}\| _2^2\leq (1 - \gamma_{n + 1})^{-1}a_{ii}$ . Then, using the Cauchy-Schwarz inequality,

$$
| \widehat {r} _ {i} ^ {T} \widehat {r} _ {j} | \leq \| \widehat {r} _ {i} \| _ {2} \| \widehat {r} _ {j} \| _ {2} \leq (1 - \gamma_ {n + 1}) ^ {- 1} (a _ {i i} a _ {j j}) ^ {1 / 2},
$$

giving

$$
\left| \widehat {\boldsymbol {R}} ^ {T} \right| \left| \widehat {\boldsymbol {R}} \right| \leq \left(1 - \gamma_ {n + 1}\right) ^ {- 1} d d ^ {T} \tag {10.8}
$$

and the required bound for $\Delta A$

Standard perturbation theory applied to Theorem 10.4 yields a bound of the form $\| x - \widehat{x}\| /\| x\| \leq c_n u\kappa (A) + O(u^2)$ . However, with the aid of Theorem 10.5 we can obtain a potentially much smaller bound. The idea is to write $A = DHD$ where $D = \mathrm{diag}(A)^{1 / 2}$ , so that $H$ has unit diagonal. van der Sluis's result (Corollary 7.6) shows that

$$
\kappa_ {2} (H) \leq n \min  _ {F \text {d i a g o n a l}} \kappa_ {2} (F A F), \tag {10.9}
$$

so $D$ is nearly a condition-minimizing diagonal scaling. It follows that $\kappa_2(H) \leq n\kappa_2(A)$ and that $\kappa_2(H) \ll \kappa_2(A)$ is possible if $A$ is badly scaled. Note that $1 \leq \| H \|_2 \leq n$ , since $H$ is positive definite with $h_{ii} \equiv 1$ .

Theorem 10.6 (Demmel, Wilkinson). Let $A = DHD \in \mathbb{R}^{n \times n}$ be symmetric positive definite, where $D = \mathrm{diag}(A)^{1/2}$ , and suppose Cholesky factorization successfully produces a computed solution $\hat{x}$ to $Ax = b$ . Then the scaled error $D(x - \hat{x})$ satisfies

$$
\frac {\| D (x - \widehat {x}) \| _ {2}}{\| D x \| _ {2}} \leq \frac {\kappa_ {2} (H) \epsilon}{1 - \kappa_ {2} (H) \epsilon}, \tag {10.10}
$$

where $\epsilon = n(1 - \gamma_{n + 1})^{-1}\gamma_{3n + 1}$

Proof. Straightforward analysis shows that (cf. the proof of Theorem 9.4) $(A + \Delta A)\widehat{x} = b$ , where

$$
\Delta A = \Delta A _ {1} + \Delta_ {1} \widehat {R} + \widehat {R} ^ {T} \Delta_ {2} + \Delta_ {1} \Delta_ {2},
$$

with $|\varDelta A_1| \leq (1 - \gamma_{n + 1})^{-1}\gamma_{n + 1}dd^T$ (by Theorem 10.5) and $|\varDelta_1| \leq \gamma_n|\widehat{R}^T|, |\varDelta_2| \leq \gamma_n|\widehat{R}|$ . Scaling with $D$ , we have

$$
\left(H + D ^ {- 1} \Delta A D ^ {- 1}\right) D \widehat {x} = D ^ {- 1} b,
$$

and standard perturbation theory gives

$$
\frac {\| D (x - \widehat {x}) \| _ {2}}{\| D x \| _ {2}} \leq \frac {\kappa_ {2} (H) \| D ^ {- 1} \varDelta A D ^ {- 1} \| _ {2}}{1 - \kappa_ {2} (H) \| D ^ {- 1} \varDelta A D ^ {- 1} \| _ {2}}.
$$

But, using (10.8) and $\| D^{-1}dd^{T}D^{-1}\|_{2} = \| ee^{T}\|_{2} = n$ , we have

$$
\begin{array}{l} \| D ^ {- 1} \Delta A D ^ {- 1} \| _ {2} \leq \frac {\gamma_ {n + 1}}{1 - \gamma_ {n + 1}} \| D ^ {- 1} d d ^ {T} D ^ {- 1} \| _ {2} \\ + \left(2 \gamma_ {n} + \gamma_ {n} ^ {2}\right) \| D ^ {- 1} | \widehat {R} ^ {T} | | \widehat {R} | D ^ {- 1} \| _ {2} \\ \leq n \left(1 - \gamma_ {n + 1}\right) ^ {- 1} \gamma_ {3 n + 1}, \\ \end{array}
$$

using Lemma 3.3, which yields the result.

□

Care needs to be exercised when interpreting bounds that involve scaled quantities, but in this case the interpretation is relatively easy. Suppose that $H$ is well conditioned and $\kappa_2(D)$ is large, which represents the artificial ill conditioning that the $DHD$ scaling is designed to clarify. The vector $Dx = H^{-1}D^{-1}b$ is likely

to have components that do not vary much in magnitude. Theorem 10.6 then guarantees that we obtain the components of $Dx$ to good relative accuracy and this means that the components of $x$ (which will vary greatly in magnitude) are obtained to good relative accuracy.

So far, our results have all contained the proviso that Cholesky factorization runs to completion—in other words, the results assume that the argument of the square root is always positive. Wilkinson [1236, 1968] showed that success is guaranteed if $20n^{3/2}\kappa_2(A)u \leq 1$ , that is, if $A$ is not too ill conditioned. It would be nice to replace $A$ in this condition by $H$ , where $A = DHD$ . Justification for doing so is that Algorithm 10.2 is scale invariant, in the sense that if we scale $A \gets FAF$ , where $F$ is diagonal, then $R$ scales to $RF$ ; moreover, if $F$ comprises powers of the machine base, then even the rounding errors scale according to $F$ . The following theorem gives an appropriate modification of Wilkinson's condition.

Theorem 10.7 (Demmel). Let $A = DHD \in \mathbb{R}^{n \times n}$ be symmetric positive definite, where $D = \mathrm{diag}(A)^{1/2}$ . If $\lambda_{\min}(H) > n\gamma_{n+1} / (1 - \gamma_{n+1})$ then Cholesky factorization applied to $A$ succeeds (barring underflow and overflow) and produces a nonsingular $\widehat{R}$ . If $\lambda_{\min}(H) \leq -n\gamma_{n+1} / (1 - \gamma_{n+1})$ then the computation is certain to fail.

Proof. The proof is by induction. Consider Algorithm 10.2. The first stage obviously succeeds and gives $\widehat{r}_{11} > 0$ , since $a_{11} > 0$ . Suppose the algorithm has successfully completed $k - 1$ stages, producing a nonsingular $\widehat{R}_{k - 1}$ , and consider equations (10.1)-(10.3) with $n$ replaced by $k$ . The $k$ th stage can be completed, but may give a pure imaginary $\widehat{\beta}$ (it will if $fl(\alpha - \widehat{r}^T \widehat{r}) < 0$ ). However, in the latter event, the error analysis of Theorem 10.5 is still valid! Thus we obtain $\widehat{R}_k$ satisfying $\widehat{R}_k^* \widehat{R}_k = A_k + \Delta A_k$ , $|\Delta A_k| \leq (1 - \gamma_{k + 1})^{-1} \gamma_{k + 1} d_k d_k^T$ , where $d_k = [a_{11}^{1/2}, \ldots, a_{kk}^{1/2}]^T$ . Now, with $D_k = \mathrm{diag}(d_k)$ , we have

$$
\begin{array}{l} \lambda_ {\min } \left(D _ {k} ^ {- 1} \left(A _ {k} + \Delta A _ {k}\right) D _ {k} ^ {- 1}\right) = \lambda_ {\min } \left(H _ {k} + D _ {k} ^ {- 1} \Delta A _ {k} D _ {k} ^ {- 1}\right) \\ \geq \lambda_ {\min } \left(H _ {k}\right) - \left\| D _ {k} ^ {- 1} \Delta A _ {k} D _ {k} ^ {- 1} \right\| _ {2} \\ \geq \lambda_ {\min } (H _ {k}) - \frac {\gamma_ {k + 1}}{1 - \gamma_ {k + 1}} \| e e ^ {T} \| _ {2} \\ \geq \lambda_ {\min } (H) - k \frac {\gamma_ {k + 1}}{1 - \gamma_ {k + 1}} > 0, \\ \end{array}
$$

using the interlacing of the eigenvalues [509, 1996, Thm. 8.1.7] and the condition of the theorem. Hence $D_{k}^{-1}(A_{k} + \Delta A_{k})D_{k}^{-1}$ is positive definite, and therefore so is the congruent matrix $A_{k} + \Delta A_{k}$ , showing that $\widehat{R}_{k}$ must be real and nonsingular, as required to complete the induction.

If Cholesky succeeds, then, by Theorem 10.5, $D^{-1}(A + \Delta A)D^{-1}$ is positive definite and so $0 < \lambda_{\min}(H) + \| D^{-1}\Delta AD^{-1}\|_2 \leq \lambda_{\min}(H) + n(1 - \gamma_{n+1})^{-1}\gamma_{n+1}$ . Hence if $\lambda_{\min}(H) \leq -n\gamma_{n+1} / (1 - \gamma_{n+1})$ then the computation must fail.

Note that, since $\| H\| _2\geq 1$ , the condition for success of Cholesky factorization can be weakened slightly to $\kappa_{2}(H)n\gamma_{n + 1} / (1 - \gamma_{n + 1}) < 1$ .

# 10.2. Sensitivity of the Cholesky Factorization

The Cholesky factorization has perturbation bounds that are similar to those for LU factorization, but of a simpler form thanks to the positive definiteness ( $\|A^{-1}\|_2$ replaces $\|U^{-1}\|_2\|L^{-1}\|_2$ in the normwise bounds).

Theorem 10.8 (Sun). Let $A \in \mathbb{R}^{n \times n}$ be symmetric positive definite with the Cholesky factorization $A = R^T R$ and let $\Delta A$ be a symmetric matrix satisfying $\| A^{-1}\Delta A\|_2 < 1$ . Then $A + \Delta A$ has the Cholesky factorization $A + \Delta A = (R + \Delta R)^T (R + \Delta R)$ , where

$$
\frac {\| \varDelta R \| _ {F}}{\| R \| _ {p}} \leq 2 ^ {- 1 / 2} \frac {\kappa_ {2} (A) \epsilon}{1 - \kappa_ {2} (A) \epsilon}, \qquad \epsilon = \frac {\| \varDelta A \| _ {F}}{\| A \| _ {p}}, \quad p = 2, F.
$$

Moreover, if $\rho(|\widetilde{G}|) < 1$ , where $\widetilde{G} = (R + \Delta R)^{-T}\Delta A(R + \Delta R)^{-1}$ , then

$$
\left| \Delta R \right| \leq \operatorname {t r i u} \left(\left| \widetilde {G} \right| \left(I - \left| \widetilde {G} \right|\right) ^ {- 1}\right) \left| R + \Delta R \right|,
$$

where triu(·) denotes the upper triangular part.

Note that the Cholesky factor of $A_{k} = A(1:k,1:k)$ is $R_{k}$ , and $\kappa_{2}(A_{k + 1}) \geq \kappa_{2}(A_{k})$ by the interlacing property of the eigenvalues. Hence if $A_{k + 1}$ (and hence $A$ ) is ill conditioned but $A_{k}$ is well conditioned then $R_{k}$ will be relatively insensitive to perturbations in $A$ but the remaining columns of $R$ will be much more sensitive.

# 10.3. Positive Semidefinite Matrices

If $A$ is symmetric and positive semidefinite ( $x^T A x \geq 0$ for all $x$ ) then a Cholesky factorization exists, but the theory and computation are more subtle than for positive definite $A$ .

The questions of existence and uniqueness of a Cholesky factorization are answered by the following result.

Theorem 10.9. Let $A \in \mathbb{R}^{n \times n}$ be positive semidefinite of rank $r$ . (a) There exists at least one upper triangular $R$ with nonnegative diagonal elements such that $A = R^T R$ . (b) There is a permutation $\Pi$ such that $\Pi^T A \Pi$ has a unique Cholesky factorization, which takes the form

$$
\boldsymbol {\Pi} ^ {T} \boldsymbol {A} \boldsymbol {\Pi} = \boldsymbol {R} ^ {T} \boldsymbol {R}, \quad \boldsymbol {R} = \left[ \begin{array}{c c} R _ {1 1} & R _ {1 2} \\ 0 & 0 \end{array} \right], \tag {10.11}
$$

where $R_{11}$ is $r \times r$ upper triangular with positive diagonal elements.

Proof. (a) Let the symmetric positive semidefinite square root $X$ of $A$ have the QR factorization $X = QR$ with $r_{ii} \geq 0$ . Then $A = X^2 = X^T X = R^T Q^T QR = R^T R$ . (b) The algorithm with pivoting described below amounts to a constructive proof. □

Note that the factorization in part (a) is not in general unique. For example,

$$
\left[ \begin{array}{c c} 0 & 0 \\ 0 & 1 \end{array} \right] \equiv \left[ \begin{array}{c c} 0 & 0 \\ \cos \theta & \sin \theta \end{array} \right] \left[ \begin{array}{c c} 0 & \cos \theta \\ 0 & \sin \theta \end{array} \right].
$$

For practical computations a factorization of the form (10.11) is needed, because this factorization so conveniently displays the rank deficiency. Such a factorization can be computed using an outer product Cholesky algorithm, comprising $r = \operatorname{rank}(A)$ stages. At the $k$ th stage, a rank-1 matrix is subtracted from $A$ so as to introduce zeros into positions $k: n$ in the $k$ th row and column. Ignoring pivoting for the moment, at the start of the $k$ th stage we have

$$
A ^ {(k)} = \left(a _ {i j} ^ {(k)}\right) = A - \sum_ {i = 1} ^ {k - 1} r _ {i} r _ {i} ^ {T} = \underset {n - k + 1} {\overset {k - 1} {\sum}} \left[ \begin{array}{c c} k - 1 & n - k + 1 \\ 0 & 0 \\ 0 & A _ {k} \end{array} \right], \tag {10.12}
$$

where $r_i^T = [0, \ldots, 0, r_{ii}, \ldots, r_{in}]$ . The reduction is carried one stage further by computing

$$
\begin{array}{l} r _ {k k} = \sqrt {a _ {k k} ^ {(k)}}, \\ r _ {k j} = a _ {k j} ^ {(k)} / r _ {k k}, \quad j = k + 1: n, \\ a _ {i j} ^ {(k + 1)} = a _ {i j} ^ {(k)} - r _ {k i} r _ {k j}, \quad i, j = k + 1: n. \\ \end{array}
$$

Overall we have,

$$
A = \sum_ {i = 1} ^ {r} r _ {i} r _ {i} ^ {T} = R ^ {T} R, \qquad R ^ {T} = [ r _ {1}, \dots , r _ {r} ].
$$

To avoid breakdown when $a_{kk}^{(k)}$ vanishes (or is negative because of rounding errors), pivoting is incorporated into the algorithm as follows. At the start of the $k$ th stage an element $a_{ss}^{(k)} > 0$ ( $s \geq k$ ) is selected as pivot, and rows and columns $k$ and $s$ of $A_k$ , and the $k$ th and $s$ th elements of $r_i$ , $i = 1: k - 1$ , are interchanged. The overall effect is to compute the decomposition (10.11), where the permutation $\Pi$ takes account of all the interchanges.

The standard form of pivoting is defined by

$$
s = \min  \Big \{j: a _ {j j} ^ {(k)} = \max  _ {k \leq i \leq n} a _ {i i} ^ {(k)} \Big \}.
$$

This is equivalent to complete pivoting in GE, since $A_{k}$ is positive semidefinite so its largest element lies on the diagonal (see Problem 10.1). We note for later reference that this pivoting strategy produces a matrix $R$ that satisfies (cf. Problem 19.5)

$$
r _ {k k} ^ {2} \geq \sum_ {i = k} ^ {\min  (j, r)} r _ {i j} ^ {2}, \quad j = k + 1: n, \quad k = 1: r. \tag {10.13}
$$

It will be convenient to denote by $\mathbf{cp}(A) \coloneqq \Pi^T A \Pi$ the permuted matrix obtained from the Cholesky algorithm with complete pivoting.

# 10.3.1. Perturbation Theory

In this section we analyse, for a positive semidefinite matrix, the effect on the Cholesky factorization of perturbations in the matrix. This perturbation theory will be used in the error analysis of the next section.

Throughout this section $A$ is assumed to be an $n \times n$ positive semidefinite matrix of rank $r$ whose leading principal submatrix of order $r$ is positive definite. For $k = 1:r$ we will write

$$
A = \begin{array}{c} k \\ n - k \end{array} \left[ \begin{array}{l l} A _ {1 1} & A _ {1 2} \\ A _ {1 2} ^ {T} & A _ {2 2} \end{array} \right] \tag {10.14}
$$

and other matrices will be partitioned conformally.

We have the identity

$$
A = \begin{array}{c} k \\ n - k \end{array} \left[ \begin{array}{l} R _ {1 1} ^ {T} \\ R _ {1 2} ^ {T} \end{array} \right] \left[ \begin{array}{l l} R _ {1 1}, & R _ {1 2} \end{array} \right] + \left[ \begin{array}{c c} 0 & 0 \\ 0 & S _ {k} (A) \end{array} \right], \tag {10.15}
$$

where $R_{11}$ is the Cholesky factor of $A_{11}$ , $R_{12} = R_{11}^{-T}A_{12}$ , and

$$
S _ {k} (A) = A _ {2 2} - A _ {1 2} ^ {T} A _ {1 1} ^ {- 1} A _ {1 2}
$$

is the Schur complement of $A_{11}$ in $A$ . Note that $S_r(A) \equiv 0$ , so that for $k = r$ , (10.15) is the (unique) Cholesky factorization of $A$ . The following lemma shows how $S_k(A)$ changes when $A$ is perturbed.

Lemma 10.10. Let $E$ be symmetric and assume $A_{11} + E_{11}$ is nonsingular. Then

$$
S _ {k} (A + E) = S _ {k} (A) + E _ {2 2} - \left(E _ {1 2} ^ {T} W + W ^ {T} E _ {1 2}\right) + W ^ {T} E _ {1 1} W + O \left(\| E \| ^ {2}\right), \tag {10.16}
$$

where $W = A_{11}^{-1}A_{12}$

Proof. We can expand

$$
\left(A _ {1 1} + E _ {1 1}\right) ^ {- 1} = A _ {1 1} ^ {- 1} - A _ {1 1} ^ {- 1} E _ {1 1} A _ {1 1} ^ {- 1} + A _ {1 1} ^ {- 1} E _ {1 1} A _ {1 1} ^ {- 1} E _ {1 1} A _ {1 1} ^ {- 1} + O \left(\left\| E _ {1 1} \right\| ^ {3}\right).
$$

The result is obtained by substituting this expansion into $S_{k}(A + E) = (A_{22} + E_{22}) - (A_{12} + E_{12})^{T}(A_{11} + E_{11})^{-1}(A_{12} + E_{12})$ , and collecting terms. $\square$

Lemma 10.10 shows that the sensitivity of $S_{k}(A)$ to perturbations in $A$ is governed by the matrix $W = A_{11}^{-1}A_{12}$ . The question arises of whether, for a given $A$ , the potential $\| W\| _2^2$ magnification of $E$ indicated by (10.16) is attainable. For the no-pivoting strategy, $\varPi = I$ , the answer is trivially "yes", since we can take $E = \left[ \begin{array}{cc}\gamma I & 0\\ 0 & 0 \end{array} \right]$ , with $|\gamma |$ small, to obtain $\| S_k(A + E) - S_k(A)\| _2 = \| W\| _2^2\| E\| _2 + O\big(\| E\| _2^2\big)$ . For complete pivoting, however, the answer is complicated by the possibility that the sequence of pivots will be different for $A + E$ than for $A$ , in which case Lemma 10.10 is not applicable. Fortunately, a mild assumption on $A$ is enough to rule out this technical difficulty, for small $\| E\| _2$ . In the next lemma we redefine $A\coloneqq \mathrm{cp}(A)$ in order to simplify the notation.

Lemma 10.11. Let $A \coloneqq \operatorname{cp}(A)$ . Suppose that

$$
\left(S _ {i} (A)\right) _ {1 1} > \left(S _ {i} (A)\right) _ {j j}, \quad j = 2: n - i, \quad i = 0: r - 1 \tag {10.17}
$$

(where $S_0(A) \coloneqq A$ ). Then, for sufficiently small $\| E \|_2$ , $A + E = \mathrm{cp}(A + E)$ . For $E = \left[ \begin{array}{cc} \gamma I & 0 \\ 0 & 0 \end{array} \right]$ , with $|\gamma|$ sufficiently small,

$$
\left\| S _ {k} \big (\operatorname {c p} (A + E) \big) - S _ {k} (A) \right\| _ {2} = \left\| W \right\| _ {2} ^ {2} \| E \| _ {2} + O \big (\left\| E \right\| _ {2} ^ {2} \big).
$$

Proof. Note that since $A = \mathrm{cp}(A)$ , (10.17) simply states that there are no ties in the pivoting strategy (since $\big(S_i(A)\big)_{11} \equiv a_{i+1,i+1}^{(i+1)}$ in (10.12)). Lemma 10.10 shows that $S_i(A + E) = S_i(A) + O\big(\|E\|_2\big)$ , and so, in view of (10.17), for sufficiently small $\|E\|_2$ we have

$$
\left(S _ {i} (A + E)\right) _ {1 1} > \left(S _ {i} (A + E)\right) _ {j j}, \quad j = 2: n - i, \quad i = 0: r - 1.
$$

This shows that $A + E = \mathrm{cp}(A + E)$ . The last part then follows from Lemma 10.10.

We now examine the quantity $\| W\| _2 = \| A_{11}^{-1}A_{12}\| _2$ . We show first that $\| W\| _2$ can be bounded in terms of the square root of the condition number of $A_{11}$ .

Lemma 10.12. If $A$ , partitioned as in (10.14), is symmetric positive definite and $A_{11}$ is positive definite then $\| A_{11}^{-1}A_{12}\|_2\leq \sqrt{\|A_{11}^{-1}\|_2\|A_{22}\|_2}$ .

Proof. Write $A_{11}^{-1}A_{12} = A_{11}^{-1/2}A_{11}^{-1/2}A_{12}$ and use $\| A_{11}^{-1/2}\|_2 = \| A_{11}^{-1}\|_2^{1/2}$ , together with $\| A_{11}^{-1/2}A_{12}\|_2 = \| A_{12}^T A_{11}^{-1}A_{12}\|_2^{1/2} \leq \| A_{22}\|_2^{1/2}$ , which follows from the fact that the Schur complement $A_{22} - A_{12}^T A_{11}^{-1}A_{12}$ is positive semidefinite.

Note that, by the arithmetic-geometric mean inequality $\sqrt{xy} \leq (x + y) / 2$ ( $x, y \geq 0$ ), we also have, from Lemma 10.12, $\| A_{11}^{-1}A_{12}\|_2 \leq (\| A_{11}^{-1}\|_2 + \| A_{22}\|_2) / 2$ .

The inequality of Lemma 10.12 is an equality for the positive semidefinite matrix

$$
A = \left[ \begin{array}{c c} \alpha I _ {k, k} & I _ {k, n - k} \\ I _ {n - k, k} & \alpha^ {- 1} I _ {n - k, n - k} \end{array} \right], \quad \alpha > 0, \tag {10.18}
$$

where $I_{p,q}$ is the $p \times q$ identity matrix. This example shows that $\| W\| _2$ can be arbitrarily large. However, for $A\coloneqq \mathrm{cp}(A)$ , $\| W\| _2$ can be bounded solely in terms of $n$ and $k$ . The essence of the proof, in the next lemma, is that large elements in $A_{11}^{-1}$ are countered by small elements in $A_{12}$ . Hereafter we set $k = r$ , the value of interest in the following sections.

Lemma 10.13. Let $A \coloneqq \operatorname{cp}(A)$ and set $k = r$ . Then

$$
\left\| A _ {1 1} ^ {- 1} A _ {1 2} \right\| _ {2, F} \leq \sqrt {\frac {1}{3} (n - r) \left(4 ^ {r} - 1\right)}. \tag {10.19}
$$

There is a parametrized family of rank- $r$ matrices $A(\theta) = \mathrm{cp}(A(\theta))$ , $\theta \in (0, \frac{\pi}{2}]$ , for which

$$
\left\| A _ {1 1} (\theta) ^ {- 1} A _ {1 2} (\theta) \right\| _ {2, F} \rightarrow \sqrt {\frac {1}{3} (n - r) (4 ^ {r} - 1)} \quad a s \quad \theta \rightarrow 0.
$$

Proof. The proof is a straightforward computation. The matrix $A(\theta) \coloneqq R(\theta)^T R(\theta)$ , where

$$
R (\theta) = \operatorname {d i a g} (1, s, \dots , s ^ {r - 1}) \left[ \begin{array}{c c c c c c c c} 1 & - c & - c & \dots & - c & - c & \dots & - c \\ & 1 & - c & \dots & - c & - c & \dots & - c \\ & & 1 & & \vdots & \vdots & & \vdots \\ & & & \ddots & \vdots & \vdots & & \vdots \\ & & & & 1 & - c & \dots & - c \end{array} \right] \in \mathbb {R} ^ {r \times n}, \tag {10.20}
$$

with $c = \cos \theta, s = \sin \theta$ . This is the $r \times n$ version of Kahan's matrix (8.11). $R$ satisfies the inequalities (10.13) (as equalities) and so $A(\theta) = \mathrm{cp}(A(\theta))$ .

We conclude this section with a "worst-case" example for the Cholesky factorization with complete pivoting. Let $U(\theta) = \mathrm{diag}(r, r - 1, \ldots, 1)R(\theta)$ , where $R(\theta)$ is given by (10.20), and define the rank- $r$ matrix $C(\theta) = U(\theta)^T U(\theta)$ . Then $C(\theta)$ satisfies the conditions of Lemma 10.11. Also,

$$
\begin{array}{l} \| W \| _ {2} = \left\| C _ {1 1} (\theta) ^ {- 1} C _ {1 2} (\theta) \right\| _ {2} = \left\| U _ {1 1} (\theta) ^ {- 1} U _ {1 2} (\theta) \right\| _ {2} = \left\| R _ {1 1} (\theta) ^ {- 1} R _ {1 2} (\theta) \right\| _ {2} \\ \rightarrow \sqrt {\frac {1}{3} (n - r) (4 ^ {r} - 1)} \quad \text {a s} \theta \rightarrow 0. \\ \end{array}
$$

Thus, from Lemma 10.11, for $E = \left[ \begin{array}{cc}\gamma^I & 0\\ 0 & 0 \end{array} \right]$ , with $|\gamma |$ and $\theta$ sufficiently small,

$$
\left\| S _ {r} \big (\operatorname {c p} (C (\theta) + E) \big) \right\| _ {2} \approx \frac {1}{3} (n - r) \left(4 ^ {r} - 1\right) \| E \| _ {2}.
$$

This example can be interpreted as saying that in exact arithmetic the residual after an $r$ -stage Cholesky factorization of a semidefinite matrix $A$ can overestimate the distance of $A$ from the rank- $r$ semidefinite matrices by a factor as large as $(n - r)(4^r - 1)/3$ .

# 10.3.2. Error Analysis

In this section we present a backward error analysis for the Cholesky factorization of a positive semidefinite matrix. An important consideration is that a matrix of floating point numbers is very unlikely to be "exactly" positive semidefinite; errors in forming or storing $A$ will almost certainly render the smallest eigenvalue nonzero, and possibly negative. Therefore error analysis for a rank- $r$ positive semidefinite matrix may appear, at first sight, to be of limited applicability. One way around this difficulty is to state results for $A = \widetilde{A} + \Delta A$ , where $A$ is the matrix stored on the computer, $\widetilde{A}$ is positive semidefinite of rank $r$ , and $\Delta A$ is a perturbation, which could represent the rounding errors in storing $A$ , for example. However, if the perturbation $\Delta A$ is no larger than the backward error for the Cholesky factorization, then this extra formalism can be avoided by thinking of $\Delta A$ as being included in the backward error matrix. Hence for simplicity, we frame the error analysis for a positive semidefinite $A$ .

The analysis makes no assumptions about the pivoting strategy, so $A$ should be thought of as the pre-permuted matrix $\Pi^T A \Pi$ .

Theorem 10.14. Let $A$ be an $n \times n$ symmetric positive semidefinite matrix of floating point numbers of rank $r \leq n$ . Assume that $A_{11} = A(1:r,1:r)$ is positive definite with

$$
\lambda_ {\min } \left(H _ {1 1}\right) > r \gamma_ {r + 1} / \left(1 - \gamma_ {r + 1}\right), \tag {10.21}
$$

where $A_{11} = D_{11}H_{11}D_{11}$ and $D_{11} = \mathrm{diag}(A_{11})^{1/2}$ . Then, in floating point arithmetic, the Cholesky algorithm applied to $A$ successfully completes $r$ stages (barring underflow and overflow), and the computed $r \times n$ Cholesky factor $\widehat{R}_r$ satisfies

$$
\left\| A - \widehat {R} _ {r} ^ {T} \widehat {R} _ {r} \right\| _ {2} \leq 2 r \gamma_ {r + 1} \| A \| _ {2} \left(\| W \| _ {2} + 1\right) ^ {2} + O \left(u ^ {2}\right), \tag {10.22}
$$

where $W = A_{11}^{-1}A_{12}$

Proof. First, note that condition (10.21) guarantees successful completion of the first $r$ stages of the algorithm by Theorem 10.7.

Analysis very similar to that leading to Theorem 10.3 shows that

$$
A + E = \widehat {R} _ {r} ^ {T} \widehat {R} _ {r} + \widehat {A} ^ {(r + 1)}, \tag {10.23}
$$

where

$$
\widehat {R} _ {r} = \mathbf {\nabla} _ {r} \left[ \begin{array}{c c} \widehat {r} & n - r \\ \widehat {R} _ {1 1} & \widehat {R} _ {1 2} \end{array} \right], \qquad \widehat {A} ^ {(r + 1)} = \mathbf {\nabla} _ {n - r} ^ {r} \left[ \begin{array}{c c} r & n - r \\ 0 & 0 \\ 0 & \widehat {S} _ {r + 1} \end{array} \right],
$$

and

$$
| E | \leq \gamma_ {r + 1} \left(\left| \widehat {R} _ {r} ^ {T} \right| \left| \widehat {R} _ {r} \right| + \left| \widehat {A} ^ {(r + 1)} \right|\right). \tag {10.24}
$$

Taking norms in (10.24) and using the inequality $\| |B| \|_2 \leq \sqrt{\operatorname{rank}(B)} \| B \|_2$ from Lemma 6.6, we obtain

$$
\begin{array}{l} \| E \| _ {2} \leq \gamma_ {r + 1} \left(r \| \widehat {R} _ {r} ^ {T} \| _ {2} \| \widehat {R} _ {r} \| _ {2} + \sqrt {n - r} \| \widehat {A} ^ {(r + 1)} \| _ {2}\right) \\ = \gamma_ {r + 1} \left(r \| \widehat {R} _ {r} ^ {T} \widehat {R} _ {r} \| _ {2} + \sqrt {n - r} \| \widehat {A} ^ {(r + 1)} \| _ {2}\right) \\ = \gamma_ {r + 1} (r \| A + E - \widehat {A} ^ {(r + 1)} \| _ {2} + \sqrt {n - r} \| \widehat {A} ^ {(r + 1)} \| _ {2}) \\ \leq \gamma_ {r + 1} \left(r \| A \| _ {2} + r \| E \| _ {2} + n \| \widehat {A} ^ {(r + 1)} \| _ {2}\right), \\ \end{array}
$$

which implies

$$
\left\| E \right\| _ {2} \leq \frac {\gamma_ {r + 1}}{1 - r \gamma_ {r + 1}} \left(r \| A \| _ {2} + n \| \widehat {A} ^ {(r + 1)} \| _ {2}\right). \tag {10.25}
$$

Our aim is to obtain an a priori bound for $\| A - \widehat{R}_r^T\widehat{R}_r\| _2$ . It is clear from (10.23)-(10.25) that to do this we have only to bound $\| \widehat{A}^{(r + 1)}\| _2$ . To this end, we interpret (10.23) in such a way that the perturbation theory of §10.3.1 may be applied.

Equation (10.23) shows that $\widehat{S}_{r+1}$ is the true Schur complement for the matrix $A + E$ and that $A_{11} + E_{11} = \widehat{R}_{11}^T\widehat{R}_{11}$ is positive definite. Hence we can use Lemma 10.10 to deduce that

$$
\begin{array}{l} \| \widehat {A} ^ {(r + 1)} \| _ {2} = \| \widehat {S} _ {r + 1} \| _ {2} \leq \| E _ {2 2} \| _ {2} + 2 \| E _ {1 2} \| _ {2} \| W \| _ {2} + \| W \| _ {2} ^ {2} \| E _ {1 1} \| _ {2} + O (u ^ {2}) \\ \leq \left\| E \right\| _ {2} \left(\left\| W \right\| _ {2} + 1\right) ^ {2} + O (u ^ {2}). \\ \end{array}
$$

Substituting from (10.25) we find that

$$
\| \widehat {A} ^ {(r + 1)} \| _ {2} \leq r \gamma_ {r + 1} \| A \| _ {2} (\| W \| _ {2} + 1) ^ {2} + O (u ^ {2}).
$$

Finally, using (10.23) and (10.25), we obtain

$$
\| A - \widehat {R} _ {r} ^ {T} \widehat {R} _ {r} \| _ {2} \leq 2 r \gamma_ {r + 1} \| A \| _ {2} \big (\| W \| _ {2} + 1) ^ {2} + O (u ^ {2}). \qquad \square
$$

Theorem 10.14 is just about the best result that could have been expected, because the bound (10.22) is essentially the same as the bound obtained on taking norms in Lemma 10.10. In other words, (10.22) simply reflects the inherent mathematical sensitivity of $A - R^T R$ to small perturbations in $A$ .

We turn now to the issue of stability. Ideally, for $A$ as defined in Theorem 10.14, the computed Cholesky factor $\widehat{R}_r$ produced after $r$ stages of the algorithm would satisfy

$$
\left\| A - \widehat {R} _ {r} ^ {T} \widehat {R} _ {r} \right\| _ {2} \leq c _ {n} u \| A \| _ {2},
$$

where $c_{n}$ is a modest constant. Theorem 10.14 shows that stability depends on the size of $\| W\| _2 = \| A_{11}^{-1}A_{12}\| _2$ (to the extent that $\| W\| _2$ appears in a realistic bound for the backward error).

If no form of pivoting is used then $\| W\| _2$ can be arbitrarily large for fixed $n$ (see (10.18)) and the Cholesky algorithm must in this case be classed as unstable. But for complete pivoting we have from Lemma 10.13 the upper bound $\| W\| _2\leq (\frac{1}{3} (n - r)(4^r -1))^{1 / 2}$ . Thus the Cholesky algorithm with complete pivoting is stable if $r$ is small, but stability cannot be guaranteed, and seems unlikely in practice, if $\| W\| _2$ (and hence, necessarily, $r$ and $n$ ) is large.

Numerical experiments show that $\| W\| _2$ is almost always small in practice (typically less than 10) [588, 1990]. However, it is easy to construct examples where $\| W\| _2$ is large. For example, if $R$ is a Cholesky factor of $A$ from complete pivoting then let $C = M(R)^T M(R)$ , where $M(R)$ is the comparison matrix; $C$ will usually have a much larger value of $\| W\| _2$ than $A$ .

An important practical issue is when to terminate the Cholesky factorization of a semidefinite matrix. The LINPACK routine xCHDC proceeds with the factorization until a nonpositive pivot is encountered, that is, up to and including stage $k - 1$ , where $k$ is the smallest integer for which

$$
\widehat {a} _ {i i} ^ {(k)} \leq 0, \quad i = k: n. \tag {10.26}
$$

Usually $k > r + 1$ , due to the effect of rounding errors.

A more sophisticated termination criterion is to stop as soon as

$$
\left\| \widehat {S} _ {k} \right\| \leq \epsilon \| A \| \quad \text {o r} \quad \widehat {a} _ {i i} ^ {(k)} \leq 0, \quad i = k: n, \tag {10.27}
$$

for some readily computed norm and a suitable tolerance $\epsilon$ . This criterion terminates as soon as a stable factorization is achieved, avoiding unnecessary work in eliminating negligible elements in the computed Schur complement $\widehat{S}_k$ . Note that $\| \widehat{S}_k\|$ is indeed a reliable order-of-magnitude estimate of the true residual, since

$\widehat{S}_k$ is the only nonzero block of $\widehat{A}^{(k)}$ and, by (10.23) and (10.25), $A - \widehat{R}_{k - 1}^T\widehat{R}_{k - 1} = \widehat{A}^{(k)} - E$ with $\| E\| = O(u)\big(\| A\| +\| \widehat{A}^{(k)}\|\big)$ .

Another possible stopping criterion is

$$
\max  _ {k \leq i \leq n} \widehat {a} _ {i i} ^ {(k)} \leq \epsilon \widehat {a} _ {1 1} ^ {(1)}. \tag {10.28}
$$

This is related to (10.27) in that if $A$ (pre-permuted) and $\widehat{A}_k$ are positive semidefinite then $a_{11}^{(1)} = \max_{i,j} |a_{ij}| \approx \| A \|_2$ , and similarly $\max_{k \leq i \leq n} \widehat{a}_{ii}^{(k)} \approx \| \widehat{S}_k \|_2$ . Note that (10.28) bounds $\kappa_2(\widehat{R}_{k-1})$ , since if (10.28) holds first at the $k$ th stage then, using Theorem 8.14,

$$
\frac {\kappa_ {2} \left(\widehat {R} _ {k - 1}\right)}{(k - 1) ^ {1 / 2} 2 ^ {k - 2}} \leq \frac {| \widehat {r} _ {1 1} |}{| \widehat {r} _ {k - 1 , k - 1} |} = \left(\frac {\widehat {a} _ {1 1} ^ {(1)}}{\widehat {a} _ {k - 1 , k - 1} ^ {(k - 1)}}\right) ^ {1 / 2} \leq \epsilon^ {- 1 / 2}.
$$

Practical experience shows that the criteria (10.27) and (10.28) with $\epsilon = nu$ both work well, and much more effectively than (10.26) [588, 1990]. We favour (10.28) because of its negligible cost.

# 10.4. Matrices with Positive Definite Symmetric Part

Any matrix $A \in \mathbb{R}^{n \times n}$ can be written

$$
A \equiv A _ {S} + A _ {K}, \qquad A _ {S} = (A + A ^ {T}) / 2, \quad A _ {K} = (A - A ^ {T}) / 2,
$$

where $A_S$ is the symmetric part of $A$ and $A_S$ is the skew-symmetric part of $A$ . A number of results for symmetric positive definite matrices can be extended to matrices with positive definite symmetric part or, equivalently, to matrices for which $x^T A x > 0$ for all $x \neq 0$ ; these matrices are sometimes called nonsymmetric positive definite matrices.

A matrix with positive definite symmetric part clearly has nonsingular leading principal submatrices, and so has an LU factorization, $A = LU$ . It can even be shown that pivots $u_{ii}$ are positive. However, there is no guarantee that the factorization is stable without pivoting, as the example $\left[ \begin{array}{cc}\epsilon & 1\\ -1 & \epsilon \end{array} \right]$ shows. The standard error analysis for LU factorization applies (Theorems 9.3 and 9.4), and so the question is whether $|\widehat{L} ||\widehat{U} |$ can be suitably bounded. Golub and Van Loan [508, 1979] show that, for the exact LU factors,

$$
\left\| | L | | U | \right\| _ {F} \leq n \| A _ {S} + A _ {K} ^ {T} A _ {S} ^ {- 1} A _ {K} \| _ {2}. \tag {10.29}
$$

Let $\chi(A) = \|A_S + A_K^T A_S^{-1} A_K\|_2 \|A_S^{-1}\|_2$ , which is just $\kappa_2(A)$ when $A$ is symmetric. Mathias [820, 1992] shows that $\|\widehat{L}\| \widehat{U}\|_F$ (involving now the computed LU factors) is at most a factor $1 + 30un^{3/2} \chi(A)$ times larger than the upper bound in (10.29), and that the LU factorization (without pivoting) succeeds if $24n^{3/2} \chi(A)u \leq 1$ .

These results show that it is safe not to pivot provided that the symmetric part of $A$ is not too ill conditioned relative to the norm of the skew-symmetric part.

If $A$ is symmetric ( $A_K = 0$ ) then we recover the results for symmetric positive definite matrices.

For complex matrices $A$ with positive definite Hermitian part $(A + A^{*}) / 2$ , or equivalently, $\operatorname{Re} x^{*}Ax > 0$ for all nonzero $x \in \mathbb{C}$ , the results above can be extended. A particular class of such matrices is those of the form

$$
A = B + i C, \quad B, C \in \mathbb {R} ^ {n \times n} \text {b o t h s y m m e t r i c p o s i t i v e d e f i n i t e .} \tag {10.30}
$$

These matrices arise in computational electrodynamics [1183, 2001]. They are nonsingular and have an LU factorization. George, Ikramov, and Kucherov [477, 2002] show that the growth factor $\rho_{n} < 3$ , and so LU factorization without pivoting is perfectly normwise backward stable. An even smaller bound of about 1.28 holds when $B = I$ , as shown in [660, 2000].

# 10.5. Notes and References

André-Louis Cholesky (1875-1918) was a French military officer involved in geodesy and surveying in Crete and North Africa. His work was published posthumously on his behalf by Benoit [103, 1924]. Biographies of Cholesky are given by Brezinski [164, 1996] and in [28, 1922]. In some books his name is misspelled "Choleski". Discussions about Cholesky—in particular, concerning the pronunciation of his name!—can be found in the electronic mail magazine NA-Digest, volume 90, 1990, issues 7, 8, 10-12, and 24.

The properties of the Cholesky factorization are intimately associated with the properties of the Schur complement, as is apparent from some of the proofs in this chapter. The same is true for GE in general. An excellent survey of the Schur complement, containing historical comments, theory, and applications, is given by Cottle [274, 1974].

For results on the Cholesky factorization in Hilbert space see Power [952, 1986].

A book by George and Liu [478, 1981] is devoted to the many practical issues in the implementation of Cholesky factorization for the solution of sparse symmetric positive definite systems.

There is no floating point error analysis of Cholesky factorization in Wilkinson's books, but he gives a detailed analysis in [1236, 1968], showing that $\widehat{R}^T\widehat{R} = A + E$ , with $\|E\|_2 \leq 2.5n^{3/2}u\|A\|_2$ . It is unfortunate that this paper is in a rather inaccessible proceedings, because it is a model of how to phrase and interpret an error analysis. Meinguet [840, 1983] and Sun [1104, 1992] give componentwise backward error bounds similar to those in Theorems 10.3 and 10.4. Kielbasinski [733, 1987] reworks Wilkinson's analysis to improve the constant.

The fact that $\kappa_{2}(H)$ can replace the potentially much larger $\kappa_{2}(A)$ in the forward error bound for the Cholesky method was stated informally and without proof by Wilkinson [1236, 1968, p. 638]. Demmel [311, 1989] made this observation precise and explored its implications; Theorems 10.5, 10.6, and 10.7 are taken from [311, 1989].

The bounds in Theorem 10.8 are from Sun [1102, 1991], [1103, 1992]. Similar bounds are given by Stewart [1068, 1977], [1075, 1993], Barrlund [81, 1991], and Sun [1104, 1992]. More refined perturbation bounds are derived and explored by Chang, Paige, and Stewart [220, 1996] and Stewart [1078, 1997]. Perturbation

results of a different flavour, including one for structured perturbations of the form of $\varDelta A$ in Theorem 10.5, are given by Drmac, Omladic, and Veselic [356, 1994].

The perturbation and error analysis of §10.3 for semidefinite matrices is from Higham [588, 1990], wherein a perturbation result for the QR factorization with column pivoting is also given. For an application in optimization that makes use of Cholesky factorization with complete pivoting and the analysis of §10.3.1 see Forsgren, Gill, and Murray [420, 1995]. An extension of Theorem 10.14 to Toeplitz matrices is given by Stewart [1084, 1997], who shows that for these matrices pivoting is not needed in order for $\| W\|$ to be bounded in terms of $n$ and $r$ only.

Fletcher and Powell [418, 1974] describe several algorithms for updating an $\mathrm{LDLT}^{\mathrm{T}}$ factorization of a symmetric positive definite $A$ when $A$ is modified by a rank-1 matrix. They give detailed componentwise error analysis for some of the methods.

An excellent way to test whether a given symmetric matrix $A$ is positive (semi)definite is to attempt to compute a Cholesky factorization. This test is less expensive than computing the eigenvalues and is numerically stable. Indeed, if the answer "yes" is obtained, it is the right answer for a nearby matrix, whereas if the answer is "no" then $A$ must be close to an indefinite matrix. See Higham [583, 1988] for an application of this definiteness test. An algorithm for testing the definiteness of a Toeplitz matrix is developed by Cybenko and Van Loan [287, 1986], as part of a more complicated algorithm. According to Kerr [730, 1990], misconceptions of what is a sufficient condition for a matrix to be positive (semi)definite are rife in the engineering literature (for example, that it suffices to check the definiteness of all $2 \times 2$ submatrices). See also Problem 10.8. For some results on definiteness tests for Toeplitz matrices, see Makhoul [807, 1991].

That pivoting is not necessary for the class of complex symmetric matrices (10.30) was first noted by Higham [610, 1998], who also investigates the behaviour of block $\mathbf{LDL}^{\mathrm{T}}$ factorization with the Bunch-Kaufman pivoting strategy (see §11.1) when applied to such matrices. The proof of the growth factor bound in [610, 1998] is incorrect; the subsequent proof that $\rho_{n} < 3$ in [477, 2002] is quite lengthy, and obtaining a sharp bound for the growth factor is an open problem (see Problem 10.12).

# 10.5.1. LAPACK

Driver routines xPOSV (simple) and xPOSVX (expert) use the Cholesky factorization to solve a symmetric (or Hermitian) positive definite system of linear equations with multiple right-hand sides. (There are corresponding routines for packed storage, in which one triangle of the matrix is stored in a one-dimensional array: PP replaces PO in the names.) The expert driver incorporates iterative refinement, condition estimation, and backward and forward error estimation and has an option to scale the system $AX = B$ to $(D^{-1}AD^{-1})DX = D^{-1}B$ , where $D = \mathrm{diag}(a_{ii}^{1/2})$ . Modulo the rounding errors in computing and applying the scaling, the scaling has no effect on the accuracy of the solution prior to iterative refinement, in view of Theorem 10.6. The Cholesky factorization is computed by the routine xPOTRF, which uses a partitioned algorithm that computes $R$ a block row at a time. The drivers xPTSV and xPTSVX for symmetric positive definite tridiagonal matrices use

$\mathbf{LDLT}^{\mathrm{T}}$ factorization. LAPACK does not currently contain a routine for Cholesky factorization of a positive semidefinite matrix, but there is such a routine in LINPACK (xCHDC).

# Problems

10.1. Show that if $A \in \mathbb{R}^{n \times n}$ is symmetric positive definite then

$$
\left| a _ {i j} \right| <   \sqrt {a _ {i i} a _ {j j}} \quad \text {f o r a l l} i \neq j.
$$

What does this statement imply about $\max_{i,j}|a_{ij}|$ ?

10.2. If $A$ is a symmetric positive definite matrix, how would you compute $x^T A^{-1} x$ ?

10.3. Let $y = \left(c - \sum_{i=1}^{k-1} a_i b_i\right)^{1/2}$ be evaluated in floating point arithmetic in any order. Show that

$$
\widehat {y} ^ {2} (1 + \theta_ {k + 1}) = c - \sum_ {i = 1} ^ {k - 1} a _ {i} b _ {i} (1 + \theta_ {k - 1} ^ {(i)}),
$$

where $|\theta_{k - 1}^{(i)}|\leq \gamma_{k - 1}$ for all $i$ , and $|\theta_{k + 1}|\leq \gamma_{k + 1}$ .

10.4. Let $A \in \mathbb{R}^{n \times n}$ be symmetric positive definite. Show that the reduced submatrix $B$ of order $n - 1$ at the end of the first stage of GE is also symmetric positive definite. Deduce that $0 < a_{kk}^{(k)} \leq a_{kk}^{(k - 1)} \leq \dots \leq a_{kk}^{(1)} = a_{kk}$ and hence that the growth factor $\rho_n = 1$ .

10.5. Show that the backward error result (10.6) for the solution of a symmetric positive definite linear system by Cholesky factorization implies

$$
(A + \Delta A) \widehat {x} = b, \quad \| \Delta A \| _ {M} \leq \gamma_ {3 n + 1} (1 - \gamma_ {n + 1}) ^ {- 1} \| A \| _ {M},
$$

where $\| A\| _M = \max_{i,j}|a_{ij}|$ (which is not a consistent matrix norm—see §6.2). The significance of this result is that the bound for $\| \varDelta A\| _M/\| A\| _M$ contains a linear polynomial in $n$ , rather than the quadratic that appears for the 2-norm in (10.7).

10.6. Let $A = \mathrm{cp}(A) \in \mathbb{R}^{n \times n}$ be positive semidefinite of rank $r$ and suppose it has the Cholesky factorization (10.11) with $\varPi = I$ . Show that $Z = [W, -I]^T$ is a basis for the null space of $A$ , where $W = A_{11}^{-1}A_{12}$ .

10.7. Prove that (10.13) holds for the Cholesky decomposition with complete pivoting.

10.8. Give an example of a symmetric matrix $A \in \mathbb{R}^{n \times n}$ for which the leading principal submatrices $A_k$ satisfy $\det(A_k) \geq 0$ , $k = 1:n$ , but $A$ is not positive semidefinite (recall that $\det(A_k) > 0$ , $k = 1:n$ , implies that $A$ is positive definite). State a condition on the minors of $A$ that is both necessary and sufficient for positive semidefiniteness.

10.9. Suppose the outer product Cholesky factorization algorithm terminates at the $(k + 1)\mathrm{st}$ stage (see (10.15)), with a negative pivot in the $(k + 1, k + 1)$ position. Show how to construct a direction of negative curvature for $A$ (a vector $p$ such that $p^T A p < 0$ ).

10.10. What is wrong with the following argument? A positive semidefinite matrix is the limit of a positive definite one as the smallest eigenvalue tends to zero. Theorem 10.3 shows that Cholesky factorization is stable for a positive definite matrix, and therefore, by continuity, it must be stable for a positive semidefinite matrix, implying that Theorem 10.14 is unnecessarily weak (since $\| W\| _2$ can be large).

10.11. Let

$$
A = \left[ \begin{array}{c c} A _ {1 1} & A _ {1 2} \\ A _ {2 1} & A _ {2 2} \end{array} \right] \in \mathbb {C} ^ {n \times n}
$$

have positive definite Hermitian part. Show that the Schur complement $S = A_{22} - A_{21}^{*}A_{11}^{-1}A_{12}$ also has positive definite Hermitian part. In other words, show that GE preserves positive definiteness.

10.12. (RESEARCH PROBLEM) Investigate the sharpness of the bound $\rho_{n} < 3$ of [477, 2002] for matrices of the form (10.30).
