# Chapter 11

# Symmetric Indefinite and Skew-Symmetric Systems

Unfortunately, there is no stable scheme exactly analogous to Gaussian elimination with partial pivoting; one cannot construct an algorithm for which there is a bound on the element growth of the sequence $A^{(k)}$ when at each stage only one column of $A^{(k)}$ is examined.

— JAMES R. BUNCH and LINDA KAUFMAN, Some Stable Methods for Calculating Inertia and Solving Symmetric Linear Systems (1977)

The comparison count is much less ... than for the complete pivoting scheme, and in practice this fact has had a much larger impact than originally anticipated, sometimes cutting the execution time by about $40\%$ . — JAMES R. BUNCH and LINDA KAUFMAN, Some Stable Methods for Calculating Inertia and Solving Symmetric Linear Systems (1977)

This fixed inertia property is why skew-symmetric matrices are easier to decompose than symmetric indefinite matrices. — JAMES R. BUNCH, A Note on the Stable Decomposition of Skew-Symmetric Matrices (1982)

A symmetric matrix $A \in \mathbb{R}^{n \times n}$ is indefinite if $(x^T A x)(y^T A y) < 0$ for some $x, y \in \mathbb{R}^n$ , or, equivalently, if $A$ has both positive and negative eigenvalues. Linear systems with symmetric indefinite coefficient matrices arise in many applications, including least squares problems, optimization, and discretized incompressible Navier-Stokes equations. How can we solve $Ax = b$ efficiently?

Gaussian elimination with partial pivoting (GEPP) can be used to compute the factorization $PA = LU$ , but it does not take advantage of the symmetry to reduce the cost and storage. We might try to construct a factorization $A = LDL^T$ , where $L$ is unit lower triangular and $D$ is diagonal. But this factorization may not exist, even if symmetric pivoting is allowed, and if it does exist its computation may be unstable. For example, consider

$$
A \equiv P A P ^ {T} = \left[ \begin{array}{l l} \epsilon & 1 \\ 1 & \epsilon \end{array} \right] = \left[ \begin{array}{l l} 1 & 0 \\ 1 / \epsilon & 1 \end{array} \right] \left[ \begin{array}{l l} \epsilon & 0 \\ 0 & \epsilon - 1 / \epsilon \end{array} \right] \left[ \begin{array}{l l} 1 & 1 / \epsilon \\ 0 & 1 \end{array} \right].
$$

There is arbitrarily large element growth for $0 < \epsilon \ll 1$ , and the factorization does not exist for $\epsilon = 0$ .

For solving dense symmetric indefinite linear systems $Ax = b$ , two types of factorization are used. The first is the block LDL $^{\mathrm{T}}$ factorization (or symmetric indefinite factorization)

$$
P A P ^ {T} = L D L ^ {T}, \tag {11.1}
$$

where $P$ is a permutation matrix, $L$ is unit lower triangular, and $D$ is block diagonal with diagonal blocks of dimension 1 or 2. This factorization is essentially a symmetric block form of GE, with symmetric pivoting. Note that by Sylvester's inertia theorem, $A$ and $D$ have the same inertia $^{10}$ , which is easily determined from $D$ (see Problem 11.2).

The second factorization is that produced by Aasen's method,

$$
P A P ^ {T} = L T L ^ {T},
$$

where $P$ is a permutation matrix, $L$ is unit lower triangular with first column $e_1$ , and $T$ is tridiagonal. Aasen's factorization is much less widely used than block LDL $^{\mathrm{T}}$ factorization, but it is mathematically interesting. We describe both factorizations in this chapter.

A matrix $A \in \mathbb{R}^{n \times n}$ is skew-symmetric if $A^T = -A$ . In the final section of this chapter we describe a form of block LDL $^{\mathrm{T}}$ factorization specialized to skew-symmetric matrices.

# 11.1. Block $\mathbf{LDL}^{\mathrm{T}}$ Factorization for Symmetric Matrices

If the symmetric matrix $A \in \mathbb{R}^{n \times n}$ is nonzero, we can find a permutation $\pi$ and an integer $s = 1$ or 2 so that

$$
\boldsymbol {\Pi} \boldsymbol {A} \boldsymbol {\Pi} ^ {T} = \mathbf {\Pi} _ {n - s} ^ {s} \left[ \begin{array}{l l} \boldsymbol {E} & \boldsymbol {C} ^ {T} \\ \boldsymbol {C} & \boldsymbol {B} \end{array} \right], \tag {11.2}
$$

with $E$ nonsingular. Having chosen such a $\varPi$ we can factorize

$$
\varPi A \varPi^ {T} = \left[ \begin{array}{c c} I _ {s} & 0 \\ C E ^ {- 1} & I _ {n - s} \end{array} \right] \left[ \begin{array}{c c} E & 0 \\ 0 & B - C E ^ {- 1} C ^ {T} \end{array} \right] \left[ \begin{array}{c c} I _ {s} & E ^ {- 1} C ^ {T} \\ 0 & I _ {n - s} \end{array} \right]. \qquad (1 1. 3)
$$

Repeating this process recursively on the $(n - s) \times (n - s)$ Schur complement

$$
\widetilde {A} = B - C E ^ {- 1} C ^ {T}
$$

yields the factorization (11.1). This factorization method is sometimes called the diagonal pivoting method, and it costs $n^3 / 3$ operations (the same cost as Cholesky factorization of a positive definite matrix) plus the cost of determining the permutations $\varPi$ . It can be thought of as a generalization of Lagrange's method for reducing a quadratic form to diagonal form (devised by Lagrange in 1759 and rediscovered by Gauss in 1823) [857, 1961, p. 371].

We describe three different strategies for choosing the permutations.

# 11.1.1. Complete Pivoting

Bunch and Parlett [183, 1971] devised the following strategy for choosing $\Pi$ . It suffices to describe the interchanges for the first stage of the factorization.

Algorithm 11.1 (Bunch-Parlett complete pivoting strategy). This algorithm determines the pivot for the first stage of the symmetric indefinite factorization applied to a symmetric matrix $A \in \mathbb{R}^{n \times n}$ using the complete pivoting strategy of Bunch and Parlett.

$$
\alpha = (1 + \sqrt {1 7}) / 8 (\approx 0. 6 4)
$$

$$
\mu_ {0} = \max  _ {i, j} | a _ {i j} | =: | a _ {p q} | (q \geq p), \mu_ {1} = \max  _ {i} | a _ {i i} | =: | a _ {r r} |
$$

$$
\text {i f} \mu_ {1} \geq \alpha \mu_ {0}
$$

Use $a_{rr}$ as a $1 \times 1$ pivot ( $s = 1$ , $\Pi$ swaps rows and

columns 1 and $r$ ).

else

Use $\left[ \begin{array}{ll}a_{pp} & a_{qp}\\ a_{qp} & a_{qq} \end{array} \right]$ as a $2\times 2$ pivot ( $s = 2$ , $\varPi$ swaps rows and

columns 1 and $p$ , and 2 and $q$ , in that order).

end

Note that $\mu_{1}$ is the best $1\times 1$ pivot under symmetric permutations and $\mu_0$ is the pivot that would be chosen by GE with complete pivoting. This strategy says "as long as there is a diagonal pivot element not much smaller than the complete pivot, choose it as a $1\times 1$ pivot", that is, "choose a $1\times 1$ pivot whenever possible". If the strategy dictates the use of a $2\times 2$ pivot then that pivot $E$ is indefinite (see Problem 11.2).

The parameter $\alpha$ is derived by minimizing a bound on the element growth. For the following analysis we assume that the interchanges have already been done. If $s = 1$ then

$$
\widetilde {a} _ {i j} = b _ {i j} - c _ {i 1} \frac {1}{e _ {1 1}} c _ {1 j} \quad \Rightarrow \quad | \widetilde {a} _ {i j} | \leq \mu_ {0} + \frac {\mu_ {0} ^ {2}}{\mu_ {1}} \leq \left(1 + \frac {1}{\alpha}\right) \mu_ {0}.
$$

Now consider the case $s = 2$ . The $(i,j)$ element of the Schur complement $\widetilde{A} = B - CE^{-1}C^T$ is

$$
\widetilde {a} _ {i j} = b _ {i j} - \left[ \begin{array}{l l} c _ {i 1} & c _ {i 2} \end{array} \right] E ^ {- 1} \left[ \begin{array}{l} c _ {j 1} \\ c _ {j 2} \end{array} \right]. \tag {11.4}
$$

Now

$$
E ^ {- 1} = \left[ \begin{array}{c c} e _ {1 1} & e _ {1 2} \\ e _ {2 1} & e _ {2 2} \end{array} \right] ^ {- 1} = \frac {1}{\det  (E)} \left[ \begin{array}{c c} e _ {2 2} & - e _ {1 2} \\ - e _ {2 1} & e _ {1 1} \end{array} \right]
$$

and, using the symmetry of $E$

$$
\det  (E) = e _ {1 1} e _ {2 2} - e _ {2 1} ^ {2} = e _ {1 1} e _ {2 2} - \mu_ {0} ^ {2} \leq \mu_ {1} ^ {2} - \mu_ {0} ^ {2} \leq (\alpha^ {2} - 1) \mu_ {0} ^ {2}.
$$

Assuming $\alpha \in (0,1)$ , we have $|\operatorname{det}(E)| \geq (1 - \alpha^2) \mu_0^2$ . Thus

$$
| E ^ {- 1} | \leq \frac {1}{(1 - \alpha^ {2}) \mu_ {0}} \left[ \begin{array}{c c} \alpha & 1 \\ 1 & \alpha \end{array} \right].
$$

Since $|c_{ij}|\leq \mu_0$ , we obtain from (11.4)

$$
| \widetilde {a} _ {i j} | \leq \mu_ {0} + \frac {2 (1 + \alpha) \mu_ {0} ^ {2}}{(1 - \alpha^ {2}) \mu_ {0}} = \left(1 + \frac {2}{1 - \alpha}\right) \mu_ {0}.
$$

To determine $\alpha$ we equate the maximum growth for two $s = 1$ steps with that for one $s = 2$ step:

$$
\left(1 + \frac {1}{\alpha}\right) ^ {2} = 1 + \frac {2}{1 - \alpha},
$$

which reduces to the quadratic equation $4\alpha^2 - \alpha - 1 = 0$ . We require the positive root

$$
\alpha = \frac {1 + \sqrt {1 7}}{8} \approx 0. 6 4.
$$

The analysis guarantees the growth factor bound $\rho_{n} \leq (1 + \alpha^{-1})^{n - 1} = (2.57)^{n - 1}$ , where $\rho_{n}$ is defined in the same way as for GE. This bound is pessimistic, however; a much more detailed analysis by Bunch [175, 1971] shows that the growth factor is no more than $3.07(n - 1)^{0.446}$ times larger than the bound (9.14) for LU factorization with complete pivoting—a very satisfactory result. Strictly speaking, bounding the growth factor bounds only $\|D\|$ , not $\|L\|$ . But it is easy to show that for $s = 1$ and 2 no element of $CE^{-1}$ exceeds $\max \{1 / \alpha, 1 / (1 - \alpha)\}$ in absolute value, and so $\|L\|$ is bounded independently of $A$ .

Since complete pivoting requires the whole active submatrix to be searched at each stage, it needs up to $n^3 / 6$ comparisons, and so the method is rather expensive.

# 11.1.2. Partial Pivoting

Bunch and Kaufman [181, 1977] devised a pivoting strategy that requires only $O(n^{2})$ comparisons. At each stage it searches at most two columns and so is analogous to partial pivoting for LU factorization. The strategy contains several logical tests. As before, we describe the pivoting for the first stage only. Recall that $s$ denotes the size of the pivot block.

Algorithm 11.2 (Bunch-Kaufman partial pivoting strategy). This algorithm determines the pivot for the first stage of the symmetric indefinite factorization applied to a symmetric matrix $A \in \mathbb{R}^{n \times n}$ using the partial pivoting strategy of Bunch and Kaufman.

$$
\alpha = (1 + \sqrt {1 7}) / 8 (\approx 0. 6 4)
$$

$\omega_{1} =$ maximum magnitude of any subdiagonal entry in column 1.

If $\omega_{1} = 0$ there is nothing to do on this stage of the factorization.

$$
i f \left| a _ {1 1} \right| \geq \alpha \omega_ {1}
$$

(1) Use $a_{11}$ as a $1 \times 1$ pivot ( $s = 1$ , $\Pi = I$ ).

else

$r =$ row index of first (subdiagonal) entry of maximum magnitude in column 1.

$\omega_{r} =$ maximum magnitude of any off-diagonal entry in column $r$

$$
i f \left| a _ {1 1} \right| \omega_ {r} \geq \alpha \omega_ {1} ^ {2}
$$

(2) Use $a_{11}$ as a $1 \times 1$ pivot ( $s = 1$ , $\Pi = I$ ).

else if $|a_{rr}| \geq \alpha \omega_r$

(3) Use $a_{rr}$ as a $1 \times 1$ pivot ( $s = 1$ , $\varPi$ swaps rows and columns 1 and $r$ ).

else

(4) Use $\begin{bmatrix} a_{11} & a_{r1} \\ a_{r1} & a_{rr} \end{bmatrix}$ as a $2 \times 2$ pivot ( $s = 2$ , $\Pi$ swaps

rows and columns 2 and $r$ ).

end

end

To understand the Bunch-Kaufman pivoting strategy it helps to consider the matrix

$$
\left[ \begin{array}{c c c c c c} a _ {1 1} & \dots & a _ {r 1} (\omega_ {1}) & \dots & \dots & \dots \\ \vdots & & \vdots & & \\ a _ {r 1} (\omega_ {1}) & \dots & a _ {r r} & \dots & a _ {i r} (\omega_ {r}) & \dots \\ \vdots & & \vdots & & \\ \vdots & & a _ {i r} (\omega_ {r}) & & \\ \vdots & & \vdots & & \end{array} \right],
$$

and to note that the pivot is one of $a_{11}$ , $a_{rr}$ , and $\left[ \begin{array}{cc}a_{11} & a_{r1}\\ a_{r1} & a_{rr} \end{array} \right]$ .

The parameter $\alpha$ is derived by element growth considerations. We consider each of the four cases in the algorithm in turn, noting that for cases (1) and (2) the elements of the Schur complement are given by<sup>11</sup>

$$
\widetilde {a} _ {i j} = a _ {i j} - \frac {a _ {i 1} a _ {1 j}}{a _ {1 1}}.
$$

Case (1):

$$
| \widetilde {a} _ {i j} | \leq | a _ {i j} | + \frac {1}{\alpha} | a _ {1 j} | \leq \left(1 + \frac {1}{\alpha}\right) \max  _ {i, j} | a _ {i j} |.
$$

Case (2): Using symmetry,

$$
| \widetilde {a} _ {i j} | \leq | a _ {i j} | + \frac {\omega_ {1} ^ {2}}{| a _ {1 1} |} \leq | a _ {i j} | + \frac {\omega_ {r}}{\alpha} \leq \left(1 + \frac {1}{\alpha}\right) \operatorname * {m a x} _ {i, j} | a _ {i j} |.
$$

Case (3): The original $a_{rr}$ is now the pivot, and $|a_{rr}| \geq \alpha \omega_r$ , so

$$
| \widetilde {a} _ {i j} | \leq | a _ {i j} | + \frac {\omega_ {r}}{| a _ {r r} |} | a _ {1 j} | \leq \left(1 + \frac {1}{\alpha}\right) \operatorname * {m a x} _ {i, j} | a _ {i j} |.
$$

Case (4): This is where we use a $2 \times 2$ pivot, which, after the interchanges, is $E = (\Pi^T A \Pi)(1:2,1:2) = \left[ \begin{array}{cc}a_{11} & a_{r1} \\ a_{r1} & a_{rr} \end{array} \right]$ . Now

$$
\left| \operatorname * {d e t} (E) \right| = \left| a _ {r 1} ^ {2} - a _ {1 1} a _ {r r} \right| \geq \omega_ {1} ^ {2} - \left| a _ {1 1} \right| \alpha \omega_ {r} \geq \omega_ {1} ^ {2} - \alpha (\alpha \omega_ {1} ^ {2}) = \omega_ {1} ^ {2} (1 - \alpha^ {2}).
$$

The elements of the Schur complement $\widetilde{A} = B - CE^{-1}C^T$ are given by

$$
\widetilde {a} _ {i j} = b _ {i j} - \operatorname * {d e t} (E) ^ {- 1} \left[ \begin{array}{l l} a _ {i 1} & a _ {i r} \end{array} \right] \left[ \begin{array}{l l} a _ {r r} & - a _ {r 1} \\ - a _ {r 1} & a _ {1 1} \end{array} \right] \left[ \begin{array}{l} a _ {j 1} \\ a _ {j r} \end{array} \right],
$$

so

$$
\begin{array}{l} | \widetilde {a} _ {i j} | \leq | b _ {i j} | + \left(\omega_ {1} ^ {2} (1 - \alpha^ {2})\right) ^ {- 1} \left[ \begin{array}{l l} \omega_ {1} & \omega_ {r} \end{array} \right] \left[ \begin{array}{l l} \alpha \omega_ {r} & \omega_ {1} \\ \omega_ {1} & | a _ {1 1} | \end{array} \right] \left[ \begin{array}{l} \omega_ {1} \\ \omega_ {r} \end{array} \right] \\ \leq \left| b _ {i j} \right| + \frac {2 \omega_ {1} ^ {2} \omega_ {r} (1 + \alpha)}{\omega_ {1} ^ {2} (1 - \alpha^ {2})} = \left| b _ {i j} \right| + \frac {2 \omega_ {r}}{1 - \alpha} \leq \left(1 + \frac {2}{1 - \alpha}\right) \max  _ {i, j} | a _ {i j} |. \\ \end{array}
$$

This analysis shows that the bounds for the element growth for $s = 1$ and $s = 2$ are the same as the respective bounds for the complete pivoting strategy. Hence, using the same reasoning, we again choose $\alpha = (1 + \sqrt{17}) / 8$ .

The growth factor for the partial pivoting strategy is bounded by $(2.57)^{n - 1}$ . As for GEPP, large growth factors do not seem to occur in practice. But unlike for GEPP, no example is known for which the bound is attained; see Problem 11.10.

To explain the numerical stability of partial pivoting we need the following general result on the stability of block $\mathbf{LDL}^{\mathrm{T}}$ factorization.

Theorem 11.3. Let block $\mathrm{LDL}^{\mathrm{T}}$ factorization with any pivoting strategy be applied to a symmetric matrix $A \in \mathbb{R}^{n \times n}$ to yield the computed factorization $PAP^T \approx \widehat{L} \widehat{D} \widehat{L}^T$ , where $P$ is a permutation matrix and $D$ has diagonal blocks of dimension 1 or 2. Let $\widehat{x}$ be the computed solution to $Ax = b$ obtained using the factorization. Assume that for all linear systems $Ey = f$ involving $2 \times 2$ pivots $E$ the computed solution $\widehat{x}$ satisfies

$$
(E + \Delta E) \hat {y} = f, \quad | \Delta E | \leq \left(c u + O \left(u ^ {2}\right)\right) | E |, \tag {11.5}
$$

where $c$ is a constant. Then

$$
P (A + \varDelta A _ {1}) P ^ {T} = \widehat {L} \widehat {D} \widehat {L} ^ {T}, \qquad (A + \varDelta A _ {2}) \widehat {x} = b,
$$

where

$$
\left| \varDelta A _ {i} \right| \leq p (n) u \big (\left| A \right| + P ^ {T} | \widehat {L} | | \widehat {D} | | \widehat {L} ^ {T} | P \big) + O (u ^ {2}), \qquad i = 1: 2,
$$

with $p$ a linear polynomial.

For partial pivoting the condition (11.5) can be shown to hold for the two most natural ways of solving the $2 \times 2$ systems: by GEPP and by use of the explicit inverse (as is done in LINPACK and LAPACK); see Problem 11.5. Thus Theorem 11.3 is applicable to partial pivoting, and the question is whether it implies backward stability, that is, whether the matrix $|\widehat{L}||\widehat{D}||\widehat{L}^T|$ is suitably bounded relative to $A$ . If the elements of $L$ were bounded by a constant then the inequality $\| |L||D||L^T\|_{\infty} \leq \| L\|_{\infty}\| D\|_{\infty}\| L^T\|_{\infty}$ would immediately yield a satisfactory bound. However, for partial pivoting $L$ is unbounded, as we now show by example. For $\epsilon > 0$ , partial pivoting produces the factorization, with $P = I$ ,

$$
A = \left[ \begin{array}{l l l} 0 & \epsilon & 0 \\ \epsilon & 0 & 1 \\ 0 & 1 & 1 \end{array} \right] = \left[ \begin{array}{c c c} 1 & & \\ 0 & 1 & \\ 1 / \epsilon & 0 & 1 \end{array} \right] \left[ \begin{array}{c c c} 0 & \epsilon & \\ \epsilon & 0 & \\ & & 1 \end{array} \right] \left[ \begin{array}{c c c} 1 & 0 & 1 / \epsilon \\ & 1 & 0 \\ & & 1 \end{array} \right] = L D L ^ {T}. \tag {11.6}
$$

As $\epsilon \to 0$ , $\| L \|_{\infty} \| D \|_{\infty} \| L^{T} \|_{\infty} / \| A \|_{\infty} \to \infty$ . Nevertheless, it can be shown that for every $A$ the matrix $|L| |D| |L^{T}|$ satisfies the bound [608, 1997]

$$
\left\| \left| L \right| \right\lvert \left| D \right| \left\lvert \left| L ^ {T} \right. \right\rvert \left\| _ {M} \leq 3 6 n \rho_ {n} \right\| A \left\| _ {M}, \right.
$$

where $\| A\| _M = \max_{i,j}|a_{ij}|$ and $\rho_{n}$ is the growth factor. The normwise stability of the Bunch-Kaufman partial pivoting strategy can be summarized as follows.

Theorem 11.4. Let $A \in \mathbb{R}^{n \times n}$ be symmetric and let $\widehat{x}$ be a computed solution to the linear system $Ax = b$ produced by block LDL $^{\mathrm{T}}$ factorization with the Bunch-Kaufman partial pivoting strategy, where linear systems involving $2 \times 2$ pivots are solved by GEPP or by use of the explicit inverse. Then

$$
(A + \varDelta A) \widehat {\boldsymbol {x}} = \boldsymbol {b}, \qquad \| \varDelta A \| _ {M} \leq p (n) \rho_ {n} u \| A \| _ {M} + O (u ^ {2}),
$$

where $p$ is a quadratic.

# 11.1.3. Rook Pivoting

For solving linear systems, Theorem 11.4 shows that block $\mathbf{LDL}^{\mathrm{T}}$ factorization with the Bunch-Kaufman partial pivoting strategy has satisfactory backward stability. But for certain other applications the possibly large $L$ factor makes the factorization unsuitable. An example is a modified Cholesky factorization algorithm of Cheng and Higham [228, 1998], of interest in optimization and for constructing preconditioners. In this algorithm a block $\mathbf{LDL}^{\mathrm{T}}$ factorization of a symmetric $A$ is computed and then the $D$ factor is perturbed to make it positive definite. The perturbation of $D$ corresponds to a perturbation of $A$ up to $\| L\|^2$ times larger, so it is essential in this application that $\| L\|$ is of order 1. A small $\| L\|$ can be ensured by a symmetric form of rook pivoting (cf. §9.1) proposed by Ashcraft, Grimes, and Lewis [38, 1998, §2.4]. This pivoting strategy is broadly similar to partial pivoting, but it has an iterative phase.

Algorithm 11.5 (symmetric rook pivoting). This algorithm determines the pivot for the first stage of the symmetric indefinite factorization applied to a symmetric matrix $A \in \mathbb{R}^{n \times n}$ using the rook pivoting strategy of Ashcraft, Grimes, and Lewis.

$$
\alpha = (1 + \sqrt {1 7}) / 8 (\approx 0. 6 4)
$$

$\omega_{1} =$ maximum magnitude of any subdiagonal entry in column 1.

If $\omega_{1} = 0$ there is nothing to do on this stage of the factorization.

if $|a_{11}| \geq \alpha \omega_1$

Use $a_{11}$ as a $1 \times 1$ pivot ( $s = 1$ , $\Pi = I$ ).

else

$$
i = 1
$$

repeat

$r =$ row index of first (subdiagonal) entry of maximum magnitude in column $i$ .

$\omega_{r} =$ maximum magnitude of any off-diagonal entry in column $r$

if $|a_{rr}| \geq \alpha \omega_r$

Use $a_{rr}$ as a $1 \times 1$ pivot ( $s = 1$ , $\Pi$ swaps rows and columns 1 and $r$ ).

else if $\omega_{i} = \omega_{r}$

Use $\left[ \begin{array}{cc}a_{ii} & a_{ri}\\ a_{ri} & a_{rr} \end{array} \right]$ as a $2\times 2$ pivot $(s = 2,\Pi$ swaps

rows and columns 1 and $i$ , and 2 and $r$ ).

else

$$
i = r, \omega_ {i} = \omega_ {r}
$$

end

until a pivot is chosen

end

The repeat loop in Algorithm 11.5 searches for an element $a_{ri}$ that is simultaneously the largest in magnitude in the $r$ th row and the $i$ th column, and it uses this element to build a $2 \times 2$ pivot; the search terminates prematurely if a suitable $1 \times 1$ pivot is found. Note that the pivot test in case (2) of the partial pivoting strategy (Algorithm 11.2) is omitted in Algorithm 11.5—this is essential to obtain a bounded $L$ [38, 1998].

Since the value of $\omega_{i}$ increases strictly from one pivot step to the next, the search in Algorithm 11.5 takes at most $n$ steps. The overall cost of the searching is therefore between $O(n^{2})$ and $O(n^{3})$ comparisons. Matrices are known for which the entire Schur complement must be searched at each step, in which case the cost is $O(n^{3})$ comparisons. However, probabilistic results (very similar to those for nonsymmetric rook pivoting) and experimental evidence suggest that usually only $O(n^{2})$ comparisons are required [38, 1998].

The following properties are readily verified, using the property that any $2 \times 2$ pivot satisfies

$$
\left| \left[ \begin{array}{c c} a _ {i i} & a _ {r i} \\ a _ {r i} & a _ {r r} \end{array} \right] ^ {- 1} \right| \leq \frac {1}{\omega_ {r} (1 - \alpha^ {2})} \left[ \begin{array}{c c} \alpha & 1 \\ 1 & \alpha \end{array} \right].
$$

1. Every entry of $L$ is bounded by $\max \{1 / (1 - \alpha), 1 / \alpha\} \approx 2.78$ .

2. Every $2 \times 2$ pivot block $D_{ii}$ satisfies $\kappa_2(D_{ii}) \leq (1 + \alpha) / (1 - \alpha) \approx 4.56$ .

3. The growth factor for the factorization satisfies the same bound as for partial pivoting. Also, Theorem 11.4 holds.

At the cost of a worst case $O(n^{3})$ searching overhead, the symmetric rook pivoting strategy thus gives an $L$ factor with elements of order 1 and produces well-conditioned $2 \times 2$ blocks of $D$ .

As noted by Cheng [227, 1998], we can also derive a forward error bound analogous to (9.23) in §9.7. For any pivoting strategy satisfying the conditions of Theorem 11.3 we have

$$
\begin{array}{l} \frac {\| x - \widehat {x} \| _ {\infty}}{\| x \| _ {\infty}} \leq p (n) u \left(\operatorname {c o n d} (A, x) + \| | A ^ {- 1} | P ^ {T} | \widehat {L} | | \widehat {D} | | \widehat {L} ^ {T} | P \| _ {\infty}\right) + O \left(u ^ {2}\right) \\ \leq p (n) u \operatorname {c o n d} (A) \operatorname {c o n d} \left(\left| D \right| \left| L ^ {T} \right|\right) + O \left(u ^ {2}\right). \tag {11.7} \\ \end{array}
$$

The term $\operatorname{cond}(|D||L^T|)$ is unbounded for partial pivoting but is bounded exponentially in $n$ for rook pivoting, in view of properties 1 and 2 above. In theory, then, rook pivoting seems more likely than partial pivoting to produce a $\operatorname{cond}(A)$ -bounded forward error and hence to be insensitive to poor row (and hence column) scaling of $A$ .

# 11.1.4. Tridiagonal Matrices

How should we solve a symmetric tridiagonal linear system $Ax = b$ ? Most commonly GEPP is used, which unfortunately destroys the symmetry and so does not reveal the inertia. A factorization $PA = LU$ is obtained, where $L$ has at most one nonzero below the diagonal in each column and $U$ has upper bandwidth 2 ( $u_{ij} = 0$ for $j > i + 2$ ). Block LDL $^{\mathrm{T}}$ factorization using partial, rook, or complete pivoting exploits the symmetry, but these pivoting strategies do not preserve the bandwidth.

Bunch [177, 1974] suggested computing a block $\mathbf{LDL}^{\mathrm{T}}$ factorization without interchanges, with a particular strategy for choosing the pivot size (1 or 2) at each stage of the factorization. Bunch's strategy for choosing the pivot size is fully defined by describing the choice of the first pivot.

Algorithm 11.6 (Bunch's pivoting strategy). This algorithm determines the pivot size, $s$ , for the first stage of block $\mathbf{LDL}^{\mathrm{T}}$ factorization applied to a symmetric tridiagonal matrix $A \in \mathbb{R}^{n \times n}$ .

$$
\begin{array}{l} \alpha = (\sqrt {5} - 1) / 2 \approx 0. 6 2 \\ \sigma = \max  \left\{\left| a _ {i j} \right|: i, j = 1: n \right\} (\text {c o m p u t e o n c e , a t t h e s t a r t o f t h e} \\ \end{array}
$$

$$
\begin{array}{l} i f \sigma | a _ {1 1} | \geq \alpha a _ {2 1} ^ {2} \\ s = 1 \\ \end{array}
$$

$$
\begin{array}{l} e l s e \\ s = 2 \\ \end{array}
$$

$$
e n d
$$

The result is a factorization

$$
A = L D L ^ {T}, \tag {11.8}
$$

where $L$ is unit lower triangular and $D$ is block diagonal with each diagonal block having dimension 1 or 2. The value of $\alpha$ is derived in a similar way as for the Bunch-Kaufman partial pivoting strategy, by equating growth bounds. The inertia of $A$ is the same as that of $D$ , which can be read from the (block) diagonal of $D$ , since any $2 \times 2$ block can be shown to have one negative and one positive eigenvalue.

The numerical stability of this method is described in the next result.

Theorem 11.7. Let block $\mathrm{LDL}^{\mathrm{T}}$ factorization with the pivoting strategy of Algorithm 11.6 be applied to a symmetric tridiagonal matrix $A \in \mathbb{R}^{n \times n}$ to yield the computed factorization $A \approx \widetilde{L} \widetilde{D} \widetilde{L}^T$ , and let $\widehat{x}$ be the computed solution to $Ax = b$ obtained using the factorization. Assume that all linear systems $Ey = f$ involving $2 \times 2$ pivots $E$ are solved by GEPP or by use of the explicit inverse. Then

$$
A + \Delta A _ {1} = \widehat {L} \widehat {D} \widehat {L} ^ {T}, \qquad (A + \Delta A _ {2}) \widehat {x} = b,
$$

where

$$
\left\| \Delta A _ {i} \right\| _ {M} \leq c u \| A \| _ {M} + O \left(u ^ {2}\right), \quad i = 1: 2, \tag {11.9}
$$

with $c$ a constant.

Theorem 11.7 shows that block $\mathrm{LDL}^{\mathrm{T}}$ factorization with the pivoting strategy of Algorithm 11.6 is a perfectly normwise backward stable way to factorize a symmetric tridiagonal matrix $A$ and to solve a linear system $Ax = b$ . Block $\mathrm{LDL}^{\mathrm{T}}$ factorization therefore provides an attractive alternative to GEPP for solving such linear systems.

# 11.2. Aasen's Method

Aasen's method [1, 1971] factorizes a symmetric matrix $A \in \mathbb{R}^{n \times n}$ as

$$
P A P ^ {T} = L T L ^ {T},
$$

where $L$ is unit lower triangular with first column $e_1$ ,

$$
T = \left[ \begin{array}{ccccc} \alpha_ {1} & \beta_ {1} &  &  &  \\ \beta_ {1} & \alpha_ {2} & \beta_ {2} &  &  \\  & \ddots & \ddots & \ddots &  \\  &  & \ddots & \ddots & \beta_ {n - 1} \\  &  &  & \beta_ {n - 1} & \alpha_ {n} \\ \end{array} \right]
$$

is tridiagonal, and $P$ is a permutation matrix.

To derive Aasen's method, we initially ignore interchanges and assume that the first $i - 1$ columns of $T$ and the first $i$ columns of $L$ are known. We show how to compute the $i$ th column of $T$ and the $(i + 1)$ st column of $L$ . A key role is played by the matrix

$$
H = T L ^ {T}, \tag {11.10}
$$

which is easily seen to be upper Hessenberg. Equating $i$ th columns in (11.10) we obtain

$$
\left[ \begin{array}{c} \frac {h _ {1 i}}{h _ {2 i}} \\ \vdots \\ \frac {h _ {i - 1 , i}}{h _ {i i}} \\ \frac {h _ {i + 1 , i}}{0} \\ \vdots \\ 0 \end{array} \right] = T \left[ \begin{array}{c} l _ {i 1} \\ l _ {i 2} \\ \vdots \\ l _ {i, i - 1} \\ 1 \\ 0 \\ \vdots \\ 0 \end{array} \right] = \left[ \begin{array}{c} \alpha_ {1} l _ {i 1} + \beta_ {1} l _ {i 2} \\ \beta_ {1} l _ {i 1} + \alpha_ {2} l _ {i 2} + \beta_ {2} l _ {i 3} \\ \vdots \\ \beta_ {i - 2} l _ {i, i - 2} + \alpha_ {i - 1} l _ {i, i - 1} + \beta_ {i - 1} \\ \beta_ {i - 1} l _ {i, i - 1} + \underline {{\alpha_ {i}}} \\ \frac {\beta_ {i}}{0} \\ \vdots \\ 0 \end{array} \right]. \tag {11.11}
$$

We use an underline to denote an unknown quantity to be determined.

The first $i - 1$ equations in (11.11) are used to compute $h_{1i}, \ldots, h_{i-1,i}$ . The next two equations contain two unknowns each so cannot yet be used. The $(i,i)$ and $(i+1,i)$ elements of the equation $A = LH$ give

$$
a _ {i i} = \sum_ {j = 1} ^ {i - 1} l _ {i j} h _ {j i} + \underline {{h _ {i i}}}, \tag {11.12}
$$

$$
a _ {i + 1, i} = \sum_ {j = 1} ^ {i} l _ {i + 1, j} h _ {j i} + \underline {{h _ {i + 1 , i}}}, \tag {11.13}
$$

which we solve for $h_{ii}$ and $h_{i+1,i}$ . Now we can return to the last two nontrivial equations of (11.11) to obtain $\alpha_i$ and $\beta_i$ . Finally, the $i$ th column of the equation $A = LH$ yields

$$
a _ {k i} = \sum_ {j = 1} ^ {i + 1} l _ {k j} h _ {j i}, \quad k = i + 2: n,
$$

which yields the elements below the diagonal in the $(i + 1)\mathrm{st}$ column of $L$ :

$$
l _ {k, i + 1} = \frac {a _ {k i} - \sum_ {j = 1} ^ {i} l _ {k j} h _ {j i}}{h _ {i + 1 , i}}, \quad k = i + 2: n. \tag {11.14}
$$

The factorization has thereby been advanced by one step.

The operation count for Aasen's method is the same as for block LDL $^{\mathrm{T}}$ factorization.

To ensure that the factorization does not break down, and to improve its numerical stability, interchanges are incorporated. Before the evaluation of (11.13) and (11.14) we compute $v_{k} = a_{ki} - \sum_{j=1}^{i} l_{kj} h_{ji}$ , $k = i + 1$ : $n$ , find $r$ such that $|v_{r}| = \max \{ |v_{k}| : k = i + 1 : n \}$ , and then swap $v_{i+1}$ and $v_{r}$ and make corresponding interchanges in $A$ and $L$ . This partial pivoting strategy ensures that $|l_{ij}| \leq 1$ for $i > j$ .

To solve a linear system $Ax = b$ using the factorization $PAP^T = LTL^T$ we solve in turn

$$
L z = P b, \quad T y = z, \quad L ^ {T} w = y, \quad x = P w. \tag {11.15}
$$

The system $Ty = z$ has a symmetric tridiagonal coefficient matrix that is indefinite in general. It is usually solved by GEPP, but the symmetry-preserving method of §11.1.4 can be used instead. The next result gives a backward error bound for Aasen's method; for simplicity, pivoting is ignored, that is, $A$ is assumed to be "pre-pivoted".

Theorem 11.8. Let $A \in \mathbb{R}^{n \times n}$ be symmetric and suppose Aasen's method produces computed factors $\widehat{L}, \widehat{T}$ and a computed solution $\widehat{x}$ to $Ax = b$ . Then

$$
(A + \Delta A) \widehat {x} = b, \quad | \Delta A | \leq \gamma_ {3 n + 1} | \widehat {L} | | \widehat {T} | | \widehat {L} ^ {T} | + \gamma_ {2 n + 4} | \widehat {L} | \Pi^ {T} | \widehat {M} | | \widehat {U} | | \widehat {L} ^ {T} |,
$$

where $\widehat{\Pi T} \approx \widehat{M U}$ is the computed factorization produced by GEPP. Moreover,

$$
\left\| \varDelta A \right\| _ {\infty} \leq \left(n - 1\right) ^ {2} \gamma_ {1 5 n + 2 5} \| \widehat {T} \| _ {\infty}.
$$

Theorem 11.8 shows that Aasen's method is a backward stable method for solving $Ax = b$ provided that the growth factor

$$
\rho_ {n} = \frac {\operatorname * {m a x} _ {i , j} \left| t _ {i j} \right|}{\operatorname * {m a x} _ {i , j} \left| a _ {i j} \right|}
$$

is not too large.

Using the fact that the multipliers in Aasen's method with partial pivoting are bounded by 1, it is straightforward to show that if $\max_{i,j} |a_{ij}| = 1$ then $T$ has a bound illustrated for $n = 5$ by

$$
| T | \leq \left[ \begin{array}{c c c c c} 1 & 1 & & & \\ 1 & 1 & 2 & & \\ & 2 & 4 & 8 & \\ & & 8 & 1 6 & 3 2 \\ & & & 3 2 & 6 4 \end{array} \right].
$$

Hence

$$
\rho_ {n} \leq 4 ^ {n - 2}.
$$

Whether this bound is attainable for $n \geq 4$ is an open question. Cheng [227, 1998] reports experiments using direct search optimization in which he obtained growth of 7.99 for $n = 4$ and 14.61 for $n = 5$ , which are to be compared with the corresponding bounds of 16 and 64.

# 11.2.1. Aasen's Method Versus Block $\mathbf{LDL}^{\mathbf{T}}$ Factorization

While block $\mathbf{LDL}^{\mathrm{T}}$ of a symmetric matrix using the Bunch-Kaufman partial pivoting strategy is implemented in all the major program libraries, the only library we know to contain Aasen's method is the IMSL Fortran 90 library [546, 1997]. A comparison of the two methods in the mid 1970s found little difference between them in speed [87, 1976], but no thorough comparison on modern computer architectures has been published. See [38, 1998] for some further comments. The greater popularity of block $\mathbf{LDL}^{\mathrm{T}}$ factorization may be due to the fact that it is generally easier to work with a block diagonal matrix with blocks of size at most 2 than with a tridiagonal one.

Note that since $|l_{ij}| \leq 1$ for Aasen's method with pivoting, the method is superior to block LDL $^{\mathrm{T}}$ factorization with partial pivoting for applications in which a bounded $L$ is required.

# 11.3. Block $\mathbf{LDL}^{\mathrm{T}}$ Factorization for Skew-Symmetric Matrices

Several properties follow from the definition of a skew-symmetric matrix $A \in \mathbb{R}^{n \times n}$ : the diagonal is zero, the eigenvalues come in pure imaginary complex conjugate pairs, and the matrix is singular if $n$ is odd. Because of the zero diagonal, a skew-symmetric matrix does not usually have an LU factorization, even if symmetric pivoting $PAP^T$ (which preserves skew-symmetry) is allowed. To obtain a factorization that always exists and respects the skew-symmetry we must turn to a block $LDL^{\mathrm{T}}$ factorization. We consider a factorization

$$
P A P ^ {T} = L D L ^ {T}, \tag {11.16}
$$

where $L$ is unit lower triangular and $D$ is block diagonal with skew-symmetric diagonal blocks of dimension 1 or 2.

To begin the factorization we choose a permutation $\pi$ so that

$$
\varPi A \varPi^{T}=\mathbf{\Sigma}_{n-s}^{s}\left[\begin{array}{cc}s&n-s\\ E&C&B\end{array}\right],\qquad E=\left\{\begin{array}{cc}0,&s=1,\\ \left[\begin{array}{cc}0&-e_{21}\\ e_{21}&0\end{array}\right],&s=2,\end{array}\right.
$$

where we take $s = 1$ and $\varPi = I$ if the first column of $A$ is zero, or else $s = 2$ , in which case $\varPi$ can be chosen so that $E$ is nonsingular (we assume that $A$ is nonzero). If $s = 1$ there is nothing to do; otherwise we factorize

$$
\Pi A \Pi^ {T} = \left[ \begin{array}{c c} I _ {s} & 0 \\ C E ^ {- 1} & I _ {n - s} \end{array} \right] \left[ \begin{array}{c c} E & 0 \\ 0 & B + C E ^ {- 1} C ^ {T} \end{array} \right] \left[ \begin{array}{c c} I _ {s} & E ^ {- 1} C ^ {T} \\ 0 & I _ {n - s} \end{array} \right].
$$

The Schur complement $B + CE^{-1}C^T$ (note the “+”) inherits skew-symmetry from $A$ , and so the process can be repeated recursively, yielding on completion the factorization (11.16), with $D$ having diagonal blocks 0 or of the form $\left[ \begin{array}{cc}0 & -d_{i+1,i}\\ d_{i+1,i} & 0 \end{array} \right]$ with $d_{i+1,i} \neq 0$ . Bunch [178, 1982] proposed the following partial pivoting-type pivoting strategy.

Algorithm 11.9. (Bunch's pivoting strategy) This algorithm determines the pivot for the first stage of the block $\mathbf{LDL}^{\mathrm{T}}$ factorization of a skew-symmetric matrix $A\in \mathbb{R}^{n\times n}$ using the pivoting strategy of Bunch.

if $\| A(2:n,1)\|_{\infty} = 0$

Use $a_{11}$ as a $1 \times 1$ pivot ( $s = 1$ , $\Pi = I$ , and no elimination required).

else

$\left|a_{pq}\right| = \max (\left\| A(2:n,1)\right\|_{\infty},\left\| A(2:n,2)\right\|_{\infty})$ $(p > q)$

Use $\left[ \begin{array}{cc}0 & -a_{pq}\\ a_{pq} & 0 \end{array} \right]$ as a $2\times 2$ pivot ( $s = 2$ , $\varPi$ swaps rows and

columns 1 and $q$ , and 2 and $p$ , in that order).

end

The numerical stability of the factorization is much easier to analyse than for the symmetric indefinite factorizations. It suffices to consider the $2 \times 2$ pivots, since $1 \times 1$ pivots involve no computation. We define $A := \Pi A \Pi^T$ . Note first that a row of $CE^{-1}$ has the form

$$
\left[ \begin{array}{c c} a _ {i 1} & a _ {i 2} \end{array} \right] \left[ \begin{array}{c c} 0 & 1 / a _ {2 1} \\ - 1 / a _ {2 1} & 0 \end{array} \right] = \left[ \begin{array}{c c} - a _ {i 2} / a _ {2 1} & a _ {i 1} / a _ {2 1} \end{array} \right].
$$

The pivoting strategy ensures that both these elements are bounded in modulus by 1, so the same is therefore true for every element of $L$ . Next, note that an element of $S = B + CE^{-1}C^T$ has the form

$$
s _ {i - 2, j - 2} = a _ {i j} - \left(\frac {a _ {i 2}}{a _ {2 1}}\right) a _ {j 1} + \left(\frac {a _ {i 1}}{a _ {2 1}}\right) a _ {j 2}.
$$

It follows that $|s_{ij}| \leq 3\max_{i,j}|a_{ij}|$ . Since the number of $2 \times 2$ pivots is at most $(n - 2) / 2$ , whether $n$ is odd or even, the growth factor for the whole elimination satisfies

$$
\frac {\operatorname* {m a x} _ {i , j , k} \left| a _ {i j} ^ {(k)} \right|}{\operatorname* {m a x} _ {i , j} \left| a _ {i j} \right|} \leq (\sqrt {3}) ^ {n - 2} \approx (1. 7 3) ^ {n - 2}.
$$

This bound is smaller than that for partial pivoting on a general matrix! In practice, the growth factor is usually much smaller than this bound.

The conclusion is that block $\mathbf{LDL}^{\mathrm{T}}$ factorization with Bunch's pivoting strategy has excellent numerical stability properties. It is, of course, possible to incorporate rook pivoting or complete pivoting into the factorization to obtain even smaller worst-case growth factor bounds.

This factorization is not applicable to complex skew-Hermitian matrices ( $A = -A^{*}$ ), because they do not have zero diagonal. Bunch [178, 1982] suggests applying one of the block $\mathrm{LDL}^{\mathrm{T}}$ factorizations for Hermitian indefinite matrices to $iA$ .

# 11.4. Notes and References

A major source of symmetric indefinite linear systems is the least squares problem, because the augmented system is symmetric indefinite; see Chapter 20. Other sources of such systems are interior methods for solving constrained optimization problems (see Forsgren, Gill, and Shinnerl [421, 1996], S. J. Wright [1262, 1997], and M. H. Wright [1259, 1992]) and linearly constrained optimization problems (see Gill, Murray, Saunders, and M. H. Wright [485, 1991] and Nocedal and S. J. Wright [894, 1999]).

The idea of using a block $\mathbf{LDL}^{\mathrm{T}}$ factorization with some form of pivoting for symmetric indefinite matrices was first suggested by Kahan in 1965 [183, 1971]. Bunch and Parlett [183, 1971] developed the complete pivoting strategy and Bunch [175, 1971] proved its stability. Bunch [177, 1974] discusses a rather expensive partial pivoting strategy that requires repeated scalings. Bunch and Kaufman [181, 1977] found the efficient partial pivoting strategy presented here, which is the one now widely used, and Bunch, Kaufman, and Parlett [182, 1976] give an Algol code implementing the block $\mathbf{LDL}^{\mathrm{T}}$ factorization with this pivoting strategy. Dongarra, Duff, Sorensen, and Van der Vorst [349, 1998, §5.4.5] show

how to develop a partitioned version of the block $\mathbf{LDL}^{\mathrm{T}}$ factorization with partial pivoting.

Liu [794, 1987] shows how to incorporate a threshold into the Bunch-Kaufman partial pivoting strategy for sparse symmetric matrices; see also Duff et al. [361, 1991]. The partial pivoting strategy and variants of it described by Bunch and Kaufman [181, 1977] do not preserve band structure, but the fill-in depends on the number of $2 \times 2$ pivots, which is bounded by the number of negative eigenvalues (see Problem 11.2). Jones and Patrick [676, 1993], [677, 1994] show how to exploit this fact.

The complete and partial pivoting strategies of Bunch et al. use a fixed number of tests to determine each pivot. Another possibility is to prescribe growth bounds corresponding to $1 \times 1$ and $2 \times 2$ pivots and to search in some particular order for a pivot satisfying the bound. Fletcher [415, 1976] uses this approach to define a pivoting strategy that is very similar to rook pivoting and which usually requires only $O(n^2)$ operations. Duff, Reid, and co-workers apply the same approach to the block $\mathbf{LDLT}^{\mathrm{T}}$ factorization for sparse matrices, where sparsity considerations also influence the choice of pivot [366, 1979], [361, 1991]; their Fortran codes MA27 [364, 1982] and MA47 [365, 1995] implement the methods.

The backward error results Theorem 11.3 for block $\mathbf{LDL}^{\mathrm{T}}$ factorization and Theorem 11.4 for partial pivoting are from Higham [608, 1997], who observed that despite the widespread use of partial pivoting no proof of stability had been given.

Gill, Murray, Ponceleón, and Saunders [483, 1992] show how for sparse, symmetric indefinite systems the block $\mathbf{LDL}^{\mathrm{T}}$ factorization can be used to construct a (positive definite) preconditioner for an iterative method.

The work of Ashcraft, Grimes, and Lewis [38, 1998] was motivated by an optimization problem in which solving symmetric linear systems using the Bunch-Kaufman partial pivoting strategy led to convergence difficulties, which were traced to the fact that $\| L\|$ is unbounded. The theme of [38] is that pivoting strategies such as rook pivoting that bound $\| L\|$ lead to higher accuracy. A class of linear systems is given in [38] where rook pivoting provides more accurate solutions than partial pivoting, and the experimental results can be partially explained using the bound (11.7), as shown by Cheng [227, 1998].

Theorem 11.7 is from Higham [613, 1999].

Aasen [1, 1971] states without proof a backward error bound for the factorization produced by his method. Theorem 11.8 and a related bound for the factorization are derived by Higham [612, 1999].

Dax and Kaniel [298, 1977] propose computing a factorization $PAP^T = LDL^T$ for symmetric indefinite matrices by an extended form of Gaussian elimination in which extra row operations are used to "build up" a pivot element prior to the elimination operations; here, $L$ is unit lower triangular and $D$ is diagonal. A complete pivoting strategy for determining the permutation $P$ is described in [298, 1977], and partial pivoting strategies are described in Dax [296, 1982].

Bunch [176, 1971] shows how to scale a symmetric matrix so that in every nonzero row and column the largest magnitude of an element is 1.

# 11.4.1. LAPACK

Driver routines xSYSV (simple) and xSYSVX (expert) use block $\mathbf{LDL}^{\mathrm{T}}$ factorization with partial pivoting to solve a symmetric indefinite system of linear equations with multiple right-hand sides. For Hermitian matrices the corresponding routines are xHESV (simple) and xHESVX (expert). (Variants of these routines for packed storage have names in which SP replaces SY and HP replaces HE.) The expert drivers incorporate iterative refinement, condition estimation, and backward and forward error estimation. The factorization is computed by the routine xSYTRF or xHETRF.

# Problems

11.1. Explain why if $A$ is nonzero a nonsingular pivot $E$ in (11.2) can be found.   
11.2. Consider block $\mathbf{LDL}^{\mathrm{T}}$ factorization applied to a symmetric matrix. Show that with the symmetric partial pivoting, rook pivoting, or complete pivoting strategies any $2 \times 2$ pivot is indefinite. Hence give a formula for the inertia in terms of the block sizes of the block diagonal factor. Show how to avoid overflow in computing the inverse of a $2 \times 2$ pivot.   
11.3. Describe the effect of applying the block $\mathbf{LDL}^{\mathrm{T}}$ factorization with partial pivoting to a $2\times 2$ symmetric matrix.   
11.4. What factorization is computed if the block $\mathbf{LDL}^{\mathrm{T}}$ factorization with partial pivoting is applied to a symmetric positive definite matrix?   
11.5. (Higham [608, 1997]) Show that the condition (11.5) is satisfied for the $2 \times 2$ pivots from partial pivoting if the system is solved by GEPP or by use of the explicit inverse.   
11.6. Show that for matrices of the form generated by the MATLAB code

$$
A = \text {z e r o s} (n);
$$

$$
A (n, 1) = 2;
$$

$$
\begin{array}{l} f o r \quad i = 2: n - 1 \\ A (i + 1, i) = n - i + 2; \\ \end{array}
$$

end

$$
\begin{array}{l} A = A + A ^ {\prime}; \\ A (2, 2) = n; \\ \end{array}
$$

rook pivoting (Algorithm 11.5) requires the maximum number of comparisons on each stage of the factorization [38, 1998].

11.7. (Sorensen and Van Loan; see [349, 1998, §5.3.2]) Suppose the partial pivoting strategy in Algorithm 11.2 is modified by redefining

$$
\omega_ {r} = \| A (:, r) \| _ {\infty}
$$

(thus “ $\omega_r^{\mathrm{new}} = \max(\omega_r^{\mathrm{old}}, |a_{rr}|)$ ”). Show that the same growth factor bound holds as before and that for a positive definite matrix no interchanges are done and only $1 \times 1$ pivots are used.

11.8. For the matrix $A$ in (11.6) what are the factorizations produced by block LDL $^{\mathrm{T}}$ with rook pivoting and complete pivoting?

11.9. A matrix of the form

$$
A = \left[ \begin{array}{c c} H & B ^ {T} \\ B & - G \end{array} \right],
$$

where $H \in \mathbb{R}^{n \times n}$ and $G \in \mathbb{R}^{m \times m}$ are symmetric positive definite, has been called a symmetric quasidefinite matrix by Vanderbei [1186, 1995]. Show that (a) $A$ is nonsingular, (b) for any permutation $\pi$ , $\Pi^T A \Pi$ has an LU factorization, (c) $AS$ is nonsymmetric positive definite, where $S = \mathrm{diag}(I, -I)$ . (This last property reduces the question of the stability of an $\mathrm{LDL}^{\mathrm{T}}$ factorization of $A$ to that of the stability of the LU factorization of a nonsymmetric positive definite matrix, for which see §10.4. This reduction is pointed out and exploited by Gill, Saunders, and Shinnerl [487, 1996].)

11.10. (RESEARCH PROBLEM) Investigate the attainability of the growth factor bounds for block $\mathbf{LDL}^{\mathrm{T}}$ factorization with

(a) partial pivoting,   
(b) rook pivoting,   
(c) Bunch's partial pivoting strategy for skew-symmetric matrices.

Similarly, investigate the attainability of the growth factor bound for Aasen's method.
