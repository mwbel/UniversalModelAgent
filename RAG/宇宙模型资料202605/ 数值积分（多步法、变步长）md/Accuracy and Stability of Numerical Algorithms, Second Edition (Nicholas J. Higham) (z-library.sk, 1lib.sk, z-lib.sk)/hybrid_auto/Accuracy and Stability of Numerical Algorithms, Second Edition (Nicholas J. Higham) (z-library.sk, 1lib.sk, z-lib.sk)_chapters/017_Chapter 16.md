# Chapter 16

# The Sylvester Equation

We must commence, not with a square, but with an oblong arrangement of terms consisting, suppose, of $m$ lines and $n$ columns. This will not in itself represent a determinant, but is, as it were, a Matrix out of which we may form various systems of determinants by fixing upon a number $p$ , and selecting at will $p$ lines and $p$ columns, the squares corresponding to which may be termed determinants of the $p$ th order.

— J. J. SYLVESTER, Additions to the Articles, "On a New Class of Theorems," and "On Pascal's Theorem" (1850)

I have in previous papers defined a "Matrix" as a rectangular array of terms, out of which different systems of determinants may be engendered, as from the womb of a common parent; these cognate determinants being by no means isolated in their relations to one another, but subject to certain simple laws of mutual dependence and simultaneous deprivation.

— J. J. SYLVESTER, On the Relation Between the Minor Determinants of Linearly Equivalent Quadratic Functions (1851)

The linear matrix equation

$$
A X - X B = C, \tag {16.1}
$$

where $A \in \mathbb{R}^{m \times m}$ , $B \in \mathbb{R}^{n \times n}$ , and $C \in \mathbb{R}^{m \times n}$ are given and $X \in \mathbb{R}^{m \times n}$ is to be determined, is called the Sylvester equation. It is of pedagogical interest because it includes as special cases several important linear equation problems:

1. linear system: $Ax = c$   
2. multiple right-hand side linear system: $AX = C$   
3. matrix inversion: $AX = I$   
4. eigenvector corresponding to given eigenvalue $b$ : $(A - bI)x = 0$   
5. commuting matrices: $AX - XA = 0$

The Sylvester equation arises in its full generality in various applications. For example, the equations

$$
\left[ \begin{array}{c c} I & - X \\ 0 & I \end{array} \right] \left[ \begin{array}{c c} A & - C \\ 0 & B \end{array} \right] \left[ \begin{array}{c c} I & X \\ 0 & I \end{array} \right] = \left[ \begin{array}{c c} A & A X - X B - C \\ 0 & B \end{array} \right]
$$

show that block-diagonalizing a block triangular matrix is equivalent to solving a Sylvester equation. The Sylvester equation can also be produced from finite difference discretization of a separable elliptic boundary value problem on a rectangular domain, where $A$ and $B$ represent application of a difference operator in the " $y$ " and " $x$ " directions, respectively [1059, 1991].

That (16.1) is merely a linear system is emphasized by writing it in the form

$$
\left(I _ {n} \otimes A - B ^ {T} \otimes I _ {m}\right) \operatorname {v e c} (X) = \operatorname {v e c} (C), \tag {16.2}
$$

where $A \otimes B \coloneqq (a_{ij}B)$ is a Kronecker product and the vec operator stacks the columns of a matrix into one long vector. For future reference, we note the useful relation

$$
\operatorname {v e c} (A X B) = \left(B ^ {T} \otimes A\right) \operatorname {v e c} (X).
$$

(See Horn and Johnson [637, 1991, Chap. 4] for a detailed presentation of properties of the Kronecker product and the vec operator.) The $mn \times mn$ coefficient matrix in (16.2) has a very special structure, illustrated for $n = 3$ by

$$
\left[ \begin{array}{ccc} A - b _ {1 1} I & - b _ {2 1} I & - b _ {3 1} I \\ - b _ {1 2} I & A - b _ {2 2} I & - b _ {3 2} I \\ - b _ {1 3} I & - b _ {2 3} I & A - b _ {3 3} I \end{array} \right].
$$

In dealing with the Sylvester equation it is vital to consider this structure and not treat (16.2) as a general linear system.

Since the $mn$ eigenvalues of $I_{n}\otimes A - B^{T}\otimes I_{m}$ are given by

$$
\lambda_ {i j} \left(I _ {n} \otimes A - B ^ {T} \otimes I _ {m}\right) = \lambda_ {i} (A) - \lambda_ {j} (B), \quad i = 1: m, \quad j = 1: n, \tag {16.3}
$$

the Sylvester equation is nonsingular precisely when $A$ and $B$ have no eigenvalues in common.

In this chapter we briefly discuss the Schur method for solving the Sylvester equation and summarize its rounding error analysis. Then we determine the backward error for the Sylvester equation, investigate its relationship with the residual, and derive a condition number. All these results respect the structure of the Sylvester equation and are relevant to any solution method. We also consider the special case of the Lyapunov equation and mention how the results extend to generalizations of the Sylvester equation.

# 16.1. Solving the Sylvester Equation

One way to solve the Sylvester equation is to apply Gaussian elimination with partial pivoting (GEPP) to the "big" system (16.2), but the structure of the coefficient matrix cannot be exploited and the cost is a prohibitive $O(m^3 n^3)$ flops. A more efficient method, requiring $O(m^3 + n^3)$ flops, is obtained with the aid of Schur decompositions of $A$ and $B$ . Let $A$ and $B$ have the real Schur decompositions

$$
A = U R U ^ {T}, \quad B = V S V ^ {T}, \tag {16.4}
$$

where $U$ and $V$ are orthogonal and $R$ and $S$ are quasi-triangular, that is, block triangular with $1 \times 1$ or $2 \times 2$ diagonal blocks, and with any $2 \times 2$ diagonal blocks having complex conjugate eigenvalues. (See Golub and Van Loan [509, 1996, §7.4.1] for more details of the real Schur decomposition.)

With the decompositions (16.4), the Sylvester equation transforms to

$$
R Z - Z S = D \quad (Z = U ^ {T} X V, \quad D = U ^ {T} C V), \tag {16.5}
$$

or, equivalently, $Pz = d$ , where $P = I_n \otimes R - S^T \otimes I_m$ , $z = \operatorname{vec}(Z)$ and $d = \operatorname{vec}(D)$ . If $R$ and $S$ are both triangular then $P$ is block triangular with triangular diagonal blocks, so $Pz = d$ can be solved by substitution. Expressed in the notation of (16.5), the solution process takes the form of $n$ substitutions: if $S$ is upper triangular then

$$
(R - s _ {j j} I) Z (:, j) = D (:, j) + Z (:, 1: j - 1) S (1: j - 1, j), \quad j = 1: n.
$$

Suppose now that $R$ and $S$ are quasi-triangular, and for definiteness assume that they are both upper quasi-triangular. Partitioning $Z = (Z_{ij})$ conformally with $R = (R_{ij})$ and $S = (S_{ij})$ we have

$$
R _ {i i} Z _ {i j} - Z _ {i j} S _ {j j} = D _ {i j} - \sum_ {k = i + 1} ^ {m} R _ {i k} Z _ {k j} + \sum_ {k = 1} ^ {j - 1} Z _ {i k} S _ {k j}. \tag {16.6}
$$

These equations can be used to determine the blocks of $Z$ working up the block columns from first to last. Since $R_{ii}$ and $S_{jj}$ are both of order 1 or 2, each system (16.6) is a linear system of order 1, 2, or 4 for $Z_{ij}$ ; in the latter two cases it is usually solved by GEPP (or even Gaussian elimination with complete pivoting—see Problem 16.4).

This Schur decomposition method for solving the Sylvester equation is due to Bartels and Stewart [84, 1972]. What can be said about its numerical stability? In the case where $R$ and $S$ are both triangular, Theorem 8.5 shows that

$$
(P + \Delta P) \hat {z} = d, \quad | \Delta P | \leq c _ {m, n} u | P |, \tag {16.7}
$$

where $c_{m,n}$ denotes a constant depending on the dimensions $m$ and $n$ (in fact, we can take $c_{m,n} \approx mn$ ). Thus $|d - P\widehat{z}| \leq c_{m,n}u|P||\widehat{z}|$ , which implies the weaker inequality

$$
| D - (R \widehat {Z} - \widehat {Z} S) | \leq c _ {m, n} u (| R | | \widehat {Z} | + | \widehat {Z} | | S |). \tag {16.8}
$$

If $R$ or $S$ is quasi-triangular then the error analysis depends on how the systems of dimension 2 or 4 are solved. If GEPP followed by fixed precision iterative refinement is used for each of these systems " $\overline{P}\overline{z} = \overline{d}$ ", and if for each system $\overline{P}$ is not too ill conditioned and the vector $|\overline{P}||\overline{z}|$ is not too badly scaled, then (16.7) and (16.8) remain valid (see §12.2). Otherwise, we have only a normwise bound

$$
\left\| D - (R \widehat {Z} - \widehat {Z} S) \right\| _ {F} \leq c _ {m, n} ^ {\prime} u (\left\| R \right\| _ {F} + \left\| S \right\| _ {F}) \left\| \widehat {Z} \right\| _ {F}.
$$

Because the transformation of a matrix to Schur form (by the QR algorithm) is a backward stable process<sup>13</sup> it is true overall that

$$
\| C - (A \hat {X} - \hat {X} B) \| _ {F} \leq c _ {m, n} ^ {\prime \prime} u (\| A \| _ {F} + \| B \| _ {F}) \| \hat {X} \| _ {F}. \tag {16.9}
$$

Thus the relative residual is guaranteed to be bounded by a modest multiple of the unit roundoff $u$ .

Golub, Nash, and Van Loan [503, 1979] suggested a modification of the Bartels-Stewart algorithm in which $A$ is reduced only to upper Hessenberg form: $A = U H U^T$ . The reduced system $H Z - Z S = D$ can be solved by solving $n$ systems that are either upper Hessenberg or differ from upper Hessenberg form by the addition of an extra subdiagonal. As shown in [503, 1979], the Hessenberg-Schur algorithm has a smaller flop count than the Bartels-Stewart algorithm, with the improvement depending on the relative sizes of $m$ and $n$ . The computed solution $\widehat{X}$ again satisfies (16.9).

The use of iterative methods to solve the Sylvester equation has attracted attention recently for applications where $A$ and $B$ are large and sparse [628, 1995], [645, 1992], [1059, 1991], [1202, 1988]. The iterations are usually terminated when an inequality of the form (16.9) holds, so here the size of the relative residual is known a priori (assuming the method converges).

# 16.2. Backward Error

We saw in the last section that standard methods for solving the Sylvester equation are guaranteed to produce a small relative residual. Does a small relative residual imply a small backward error? The answer to this question for a general linear system is yes (Theorem 7.1). But for the highly structured Sylvester equation the answer must be no, because for the special case of matrix inversion we know that a small residual does not imply a small backward error (§14.1). In this section we investigate the relationship between residual and backward error for the Sylvester equation.

The normwise backward error of an approximate solution $Y$ to (16.1) is defined by

$$
\begin{array}{l} \eta (Y) = \min  \left\{\epsilon : (A + \Delta A) Y - Y (B + \Delta B) = C + \Delta C, \| \Delta A \| _ {F} \leq \epsilon \alpha , \right. \\ \left\| \Delta B \right\| _ {F} \leq \epsilon \beta , \left\| \Delta C \right\| _ {F} \leq \epsilon \gamma \}. \tag {16.10} \\ \end{array}
$$

The tolerances $\alpha$ , $\beta$ , and $\gamma$ provide some freedom in how we measure the perturbations. Of most interest is the choice $\alpha = \|A\|_F$ , $\beta = \|B\|_F$ , $\gamma = \|C\|_F$ , for which we will call $\eta$ the normwise relative backward error. The equation $(A + \Delta A)Y - Y(B + \Delta B) = C + \Delta C$ may be written

$$
\Delta A Y - Y \Delta B - \Delta C = R, \tag {16.11}
$$

where the residual $R = C - (AY - YB)$ . A small backward error implies a small relative residual since, using the optimal perturbations from (16.10) in (16.11), we have

$$
\| R \| _ {F} = \left\| \Delta A Y - Y \Delta B - \Delta C \right\| _ {F} \leq ((\alpha + \beta) \| Y \| _ {F} + \gamma) \eta (Y). \tag {16.12}
$$

To explore the converse question of what the residual implies about the backward error we begin by transforming (16.11) using the SVD of $Y$ (see §6.4), $Y = U\Sigma V^T$ , where $U \in \mathbb{R}^{m \times m}$ and $V \in \mathbb{R}^{n \times n}$ are orthogonal and $\Sigma = \mathrm{diag}(\sigma_i) \in \mathbb{R}^{m \times n}$ . The numbers $\sigma_1 \geq \sigma_2 \geq \dots \geq \sigma_{\min(m,n)} \geq 0$ are the singular values of $Y$ and we define, in addition, $\sigma_{\min(m,n)+1} = \dots = \sigma_{\max(m,n)} = 0$ . Equation (16.11) transforms to

$$
\widehat {\Delta A} \Sigma - \Sigma \widehat {\Delta B} - \widetilde {\Delta C} = \widetilde {R}, \tag {16.13}
$$

where

$$
\widetilde {\varDelta A} = U ^ {T} \varDelta A U, \quad \widetilde {\varDelta B} = V ^ {T} \varDelta B V, \quad \widetilde {\varDelta C} = U ^ {T} \varDelta C V, \quad \widetilde {R} = U ^ {T} R V.
$$

This is an underdetermined system, with $mn$ equations in $m^2 + n^2 + mn$ unknowns. We can write it in the uncoupled form<sup>14</sup>

$$
\frac {\widetilde {\Delta} a _ {i j}}{\alpha} \cdot \alpha \sigma_ {j} - \beta \sigma_ {i} \cdot \frac {\widetilde {\Delta} b _ {i j}}{\beta} - \gamma \cdot \frac {\widetilde {\Delta} c _ {i j}}{\gamma} = \widetilde {r} _ {i j}, \quad i = 1: m, \quad j = 1: n. \tag {16.14}
$$

For each $i$ and $j$ it is straightforward to show that the minimum of $(\alpha^{-1}\widetilde{\Delta} a_{ij})^2 + (\beta^{-1}\widetilde{\Delta} b_{ij})^2 + (\gamma^{-1}\widetilde{\Delta} c_{ij})^2$ subject to (16.14) is attained for

$$
\begin{array}{l} \frac {\widetilde {\Delta a _ {i j}}}{\alpha} = \frac {\alpha \sigma_ {j}}{\alpha^ {2} \sigma_ {j} ^ {2} + \beta^ {2} \sigma_ {i} ^ {2} + \gamma^ {2}} \widetilde {r} _ {i j}, \\ \frac {\widetilde {\Delta} b _ {i j}}{\beta} = \frac {- \beta \sigma_ {i}}{\alpha^ {2} \sigma_ {j} ^ {2} + \beta^ {2} \sigma_ {i} ^ {2} + \gamma^ {2}} \widetilde {r} _ {i j}, \\ \frac {\widetilde {\Delta c _ {i j}}}{\gamma} = \frac {- \gamma}{\alpha^ {2} \sigma_ {j} ^ {2} + \beta^ {2} \sigma_ {i} ^ {2} + \gamma^ {2}} \widetilde {r} _ {i j}. \\ \end{array}
$$

These matrices minimize

$$
\left\| \left[ \begin{array}{l l l} \widetilde {\Delta A} & \widetilde {\Delta B} & \widetilde {\Delta C} \\ \hline \alpha & \beta & \gamma \end{array} \right] \right\| _ {F} \equiv \left(\left\| \frac {\Delta A}{\alpha} \right\| _ {F} ^ {2} + \left\| \frac {\Delta B}{\beta} \right\| _ {F} ^ {2} + \left\| \frac {\Delta C}{\gamma} \right\| _ {F} ^ {2}\right) ^ {1 / 2}.
$$

Since $\eta(Y)$ is the minimum value of $\max\{\|\alpha^{-1}\Delta A\|_F, \|\beta^{-1}\Delta B\|_F, \|\gamma^{-1}\Delta C\|_F\}$ , it follows that

$$
\frac {\xi}{\sqrt {3}} \leq \eta (Y) \leq \xi , \tag {16.15}
$$

where

$$
\begin{array}{l} \xi := \min  \{\| [ \alpha^ {- 1} \widetilde {\Delta A} \beta^ {- 1} \widetilde {\Delta B} \gamma^ {- 1} \widetilde {\Delta C} ] \| _ {F} \} \\ = \left(\sum_ {i = 1} ^ {m} \sum_ {j = 1} ^ {n} \frac {\widetilde {r} _ {i j} ^ {2}}{\alpha^ {2} \sigma_ {j} ^ {2} + \beta^ {2} \sigma_ {i} ^ {2} + \gamma^ {2}}\right) ^ {1 / 2}. \tag {16.16} \\ \end{array}
$$

This expression shows that the backward error is approximately equal not to the normwise relative residual $\| R\| _F / ((\alpha +\beta)\| X\| _F + \gamma)$ , but to a componentwise residual corresponding to the diagonalized equation (16.13).

From (16.15) and (16.16) we deduce that

$$
\eta (Y) \leq \mu \frac {\| R \| _ {F}}{(\alpha + \beta) \| Y \| _ {F} + \gamma}, \tag {16.17}
$$

where

$$
\mu := \frac {(\alpha + \beta) \| Y \| _ {F} + \gamma}{\left(\alpha^ {2} \sigma_ {n} ^ {2} + \beta^ {2} \sigma_ {m} ^ {2} + \gamma^ {2}\right) ^ {1 / 2}}. \tag {16.18}
$$

The scalar $\mu \geq 1$ is an amplification factor that measures by how much, at worst, the backward error can exceed the normwise relative residual. We now examine $\mu$ more closely, concentrating on the normwise relative backward error, for which $\alpha = \| A\|_{F}$ , $\beta = \| B\|_{F}$ , and $\gamma = \| C\|_{F}$ .

First, note that if $n = 1$ and $B = 0$ , so that the Sylvester equation reduces to a linear system $Ay = c$ , then $\sigma_{1} = \| y\|_{2}$ and $\sigma_{k} = 0$ for $k > 1$ , so $\mu = (\| A\|_{F}\| y\|_{2} + \| c\|_{2}) / (\| A\|_{F}^{2}\| y\|_{2}^{2} + \| c\|_{2}^{2})^{1 / 2}$ . Clearly, $1\leq \mu \leq \sqrt{2}$ , and so we recover Theorem 7.1 (for the 2-norm) from (16.12) and (16.17), to within a constant factor.

If $m = n$ then

$$
\mu = \frac {\left(\| A \| _ {F} + \| B \| _ {F}\right) \| Y \| _ {F} + \| C \| _ {F}}{\left(\left(\| A \| _ {F} ^ {2} + \| B \| _ {F} ^ {2}\right) \sigma_ {\min } (Y) ^ {2} + \| C \| _ {F} ^ {2}\right) ^ {1 / 2}}. \tag {16.19}
$$

We see that $\mu$ is large only when

$$
\| Y \| _ {F} \gg \sigma_ {\min } (Y) \quad \text {a n d} \quad \| Y \| _ {F} \gg \frac {\| C \| _ {F}}{\| A \| _ {F} + \| B \| _ {F}}, \tag {16.20}
$$

that is, when $Y$ is ill conditioned and $Y$ is a large-normed solution to the Sylvester equation. In the general case, with $m \neq n$ , one of $\sigma_m^2$ and $\sigma_n^2$ is always zero and hence $\mu$ can be large for a third reason: $A$ (if $m < n$ ) or $B$ (if $m > n$ ) greatly exceeds the rest of the data in norm; in these cases the Sylvester equation is badly

scaled. However, if we set $\alpha = \beta = \| A\| _F + \| B\| _F$ , which corresponds to regarding $A$ and $B$ as comprising a single set of data, then bad scaling does not affect $\mu$ .

If we allow only $A$ and $B$ to be perturbed in (16.10) (as may be desirable if the right-hand side $C$ is known exactly), then $\gamma = 0$ and (16.19) and (16.20) remain valid with $\| C \|_F$ replaced by zero. In this case $\mu \geq \| Y \|_F \| Y^+ \|_2 \approx \kappa_2(Y)$ (for any $m$ and $n$ ), so $\mu$ is large whenever $Y$ is ill conditioned (and included in this case is matrix inversion). Conditions involving controllability which guarantee that the solution to the Sylvester equation with $m = n$ is nonsingular are given by Hearon [554, 1977], while Datta [292, 1988] gives a determinantal condition for nonsingularity. It is an open problem to derive conditions for the Sylvester equation to have a well-conditioned solution (see Problem 16.5).

The following numerical example illustrates the above analysis. This particular example was carefully chosen so that the entries of $A$ and $B$ are of a simple form, but equally effective examples are easily generated using random, ill-conditioned $A$ and $B$ of dimension $m, n \geq 2$ . Let

$$
A = \left[ \begin{array}{c c} 1 & - 1 \\ 1 & - 1 \end{array} \right], \quad B = A - \alpha \left[ \begin{array}{c c} 1 + \alpha & 0 \\ 0 & 1 \end{array} \right].
$$

Define $C$ by the property that $\operatorname{vec}(C)$ is the singular vector corresponding to the smallest singular value of $I_n \otimes A - B^T \otimes I_m$ . With $\alpha = 10^{-6}$ , we solved the Sylvester equation in MATLAB by the Bartels-Stewart algorithm and found that the computed solution $\widehat{X}$ satisfies

$$
\begin{array}{l} \frac {\| R \| _ {F}}{(\| A \| _ {F} + \| B \| _ {F}) \| \widehat {X} \| _ {F} + \| C \| _ {F}} = 2. 8 2 \times 1 0 ^ {- 1 7}, \quad \sigma (\widehat {X}) = \left\{2 \times 1 0 ^ {1 8}, 5 \times 1 0 ^ {5} \right\}, \\ \eta (\widehat {X}) \approx \xi = 2. 2 1 \times 1 0 ^ {- 8}, \quad \mu = 5. 6 6 \times 1 0 ^ {1 2}. \\ \end{array}
$$

Although $\widehat{X}$ has a very acceptable residual (as it must in view of (16.9)), its backward error is eight orders of magnitude larger than is necessary to achieve backward stability. We solved the same Sylvester equation using GEPP on the system (16.2). The relative residual was again less than $u$ , but the backward error was appreciably larger: $\eta (\widehat{X})\approx 1.53\times 10^{-5}$ .

One conclusion we can draw from the analysis is that standard methods for solving the Sylvester equation are at best conditionally backward stable, since there exist rounding errors such that $\widetilde{r}_{m,n}$ is the only nonzero element of $\widetilde{R}$ , and then (16.17) is an approximate equality, with $\mu$ possibly large.

# 16.2.1. The Lyapunov Equation

If we put $B = -A^T$ in the Sylvester equation we obtain

$$
A X + X A ^ {T} = C,
$$

which is called the Lyapunov equation. This equation plays a major role in control and systems theory and it can be solved using the same techniques as for the Sylvester equation.

If $C = C^T$ then $C = AX + XA^T = X^TA^T + AX^T = C^T$ , so $X$ and $X^T$ are both solutions to the Lyapunov equation. If the Lyapunov equation is nonsingular (equivalently, $\lambda_i(A) + \lambda_j(A) \neq 0$ for all $i$ and $j$ , by (16.3)) it therefore has a unique symmetric solution.

We assume that $C$ is symmetric and that $Y$ is a symmetric approximate solution. The definition of backward error is now

$$
\begin{array}{l} \eta (Y) = \min  \left\{\epsilon : (A + \Delta A) Y + Y (A + \Delta A) ^ {T} = C + \Delta C, \| \Delta A \| _ {F} \leq \epsilon \alpha , \right. \\ \Delta C = \Delta C ^ {T}, \| \Delta C \| _ {F} \leq \epsilon \gamma \}. \\ \end{array}
$$

The analogue of (16.11) is $\Delta A Y + Y \Delta A^T - \Delta C = R \coloneqq C - A Y - Y A^T$ . Let $Y = U \Lambda U^T$ be a spectral decomposition, with $\Lambda = \mathrm{diag}(\lambda_i)$ . Then the residual equation transforms to

$$
\widetilde {\varDelta A} \varLambda + \varLambda \widetilde {\varDelta A} ^ {T} - \widetilde {\varDelta C} = \widetilde {R},
$$

where $\widetilde{\Delta A} = U^T\Delta AU$ , $\widetilde{\Delta C} = U^T\Delta CU$ , and $\widetilde{R} = U^T R U$ . This system can be written in uncoupled form as

$$
\frac {\widetilde {\Delta} a _ {i j}}{\alpha} \cdot \alpha \lambda_ {j} + \alpha \lambda_ {i} \cdot \frac {\widetilde {\Delta} a _ {j i}}{\alpha} - \gamma \cdot \frac {\widetilde {\Delta} c _ {i j}}{\gamma} = \widetilde {r} _ {i j}, \quad i, j = 1: n. \tag {16.21}
$$

We can obtain the minimum value of $\| [\alpha^{-1}\Delta A\gamma^{-1}\Delta C]\| _F$ by minimizing

$$
(\alpha^ {- 1} \widetilde {\varDelta a} _ {i j}) ^ {2} + (\alpha^ {- 1} \widetilde {\varDelta a} _ {j i}) ^ {2} + 2 (\gamma^ {- 1} \widetilde {\varDelta c} _ {i j}) ^ {2}
$$

subject to (16.21), for $i,j = 1:n$ . The solution is

$$
\frac {\widetilde {\Delta a} _ {i j}}{\alpha} = \frac {2 \alpha \lambda_ {j}}{2 \alpha^ {2} (\lambda_ {i} ^ {2} + \lambda_ {j} ^ {2}) + \gamma^ {2}} \widetilde {r} _ {i j}, \qquad \frac {\widetilde {\Delta c} _ {i j}}{\gamma} = \frac {- \gamma}{2 \alpha^ {2} (\lambda_ {i} ^ {2} + \lambda_ {j} ^ {2}) + \gamma^ {2}} \widetilde {r} _ {i j}.
$$

(Note that $\widetilde{\Delta C}$ is symmetric since $\widetilde{R}$ is.) It follows that $\xi / \sqrt{2} \leq \eta(Y) \leq \xi$ , where

$$
\xi^ {2} = \sum_ {i, j = 1} ^ {n} \frac {(4 \alpha^ {2} \lambda_ {j} ^ {2} + \gamma^ {2}) \widetilde {r} _ {i j} ^ {2}}{(2 \alpha^ {2} (\lambda_ {i} ^ {2} + \lambda_ {j} ^ {2}) + \gamma^ {2}) ^ {2}} \leq \sum_ {i, j = 1} ^ {n} \frac {2 \widetilde {r} _ {i j} ^ {2}}{(2 \alpha^ {2} (\lambda_ {i} ^ {2} + \lambda_ {j} ^ {2}) + \gamma^ {2})},
$$

where the last inequality is usually a good approximation. Comparing with (16.16) we see that respecting the extra structure of the Lyapunov equation has essentially no effect on the backward error.

Finally, the analogue of (16.17) and (16.18) is

$$
\eta (Y) \leq \mu \frac {\| R \| _ {F}}{2 \alpha \| Y \| _ {F} + \gamma}, \qquad \mu := \frac {\sqrt {2} (2 \alpha \| Y \| _ {F} + \gamma)}{(4 \alpha^ {2} \lambda_ {*} ^ {2} + \gamma^ {2}) ^ {1 / 2}},
$$

where $\lambda_{*} = \min_{i}|\lambda_{i}|$

# 16.3. Perturbation Result

To derive a perturbation result we consider the perturbed Sylvester equation

$$
(A + \Delta A) (X + \Delta X) - (X + \Delta X) (B + \Delta B) = C + \Delta C,
$$

which, on dropping second-order terms, becomes

$$
A \Delta X - \Delta X B = \Delta C - \Delta A X + X \Delta B.
$$

This system may be written in the form

$$
P \operatorname {v e c} (\varDelta X) = - \left[ \begin{array}{l l l} X ^ {T} \otimes I _ {m} & - I _ {n} \otimes X & - I _ {m n} \end{array} \right] \left[ \begin{array}{l} \operatorname {v e c} (\varDelta A) \\ \operatorname {v e c} (\varDelta B) \\ \operatorname {v e c} (\varDelta C) \end{array} \right], \qquad (1 6. 2 2)
$$

where $P = I_{n}\otimes A - B^{T}\otimes I_{m}$ . If we measure the perturbations normwise by

$$
\epsilon = \max  \left\{\frac {\| \Delta A \| _ {F}}{\alpha}, \frac {\| \Delta B \| _ {F}}{\beta}, \frac {\| \Delta C \| _ {F}}{\gamma} \right\},
$$

where $\alpha, \beta$ , and $\gamma$ are tolerances as in (16.10), then

$$
\frac {\| \Delta X \| _ {F}}{\| X \| _ {F}} \leq \sqrt {3} \Psi \epsilon \tag {16.23}
$$

is a sharp bound (to first order in $\epsilon$ ), where

$$
\Psi = \left\| P ^ {- 1} \left[ \alpha \left(X ^ {T} \otimes I _ {m}\right) - \beta \left(I _ {n} \otimes X\right) - \gamma I _ {m n} \right] \right\| _ {2} / \| X \| _ {F} \tag {16.24}
$$

is the corresponding condition number for the Sylvester equation. The bound (16.23) can be weakened to

$$
\frac {\| \Delta X \| _ {F}}{\| X \| _ {F}} \leq \sqrt {3} \Phi \epsilon , \tag {16.25}
$$

where

$$
\varPhi = \left\| P ^ {- 1} \right\| _ {2} \frac {(\alpha + \beta) \left\| X \right\| _ {F} + \gamma}{\left\| X \right\| _ {F}}.
$$

If $\| P^{-1} \|_2 (\alpha + \beta) \epsilon < 1/2$ then twice the upper bound in (16.25) can be shown to be a strict bound for the error. The perturbation bound (16.25) with $\alpha = \| A \|_F$ , $\beta = \| B \|_F$ , and $\gamma = \| C \|_F$ is the one that is usually quoted in the literature for the Sylvester equation (see [503, 1979] and [569, 1988], for example), and corresponds to applying standard perturbation theory for $Ax = b$ to (16.2). Note that $\| P^{-1} \|_2 = \operatorname{sep}(A, B)^{-1}$ , where $\operatorname{sep}$ is the separation of $A$ and $B$ ,

$$
\operatorname {s e p} (A, B) = \min  _ {X \neq 0} \frac {\| A X - X B \| _ {F}}{\| X \| _ {F}}. \tag {16.26}
$$

The sep function is an important tool for measuring invariant subspace sensitivity [509, 1996, §7.2.4], [1064, 1973], [1189, 1979].

For the Lyapunov equation, a similar derivation to the one above shows that the condition number is

$$
\left\| \left(I _ {n} \otimes A + A \otimes I _ {n}\right) ^ {- 1} \left[ \alpha \left(\left(X ^ {T} \otimes I _ {n}\right) + \left(I _ {n} \otimes X\right) \Pi^ {T}\right), - \gamma I _ {n ^ {2}} \right] \right\| _ {2} / \| X \| _ {F}, \tag {16.27}
$$

where $\Pi$ is the vec-permutation matrix, which is defined by the property that $\operatorname{vec}(A^T) = \Pi \operatorname{vec}(A)$ .

How much can the bounds (16.23) and (16.25) differ? The answer is by an arbitrary factor. To show this we consider the case where $B$ is normal (or equivalently, $A$ is normal if we transpose the Sylvester equation). We can assume $B$ is in Schur form, thus $B = \mathrm{diag}(\mu_j)$ (with the $\mu_j$ possibly complex). Then $P = \mathrm{diag}(A - \mu_{jj}I_m)$ , and it is straightforward to show that if $X = [x_1,\ldots ,x_n]$ , and if we approximate the 2-norms in the definitions of $\varPsi$ and $\varPhi$ by Frobenius norms, then

$$
\begin{array}{l} \Psi^ {2} \approx \left(\alpha^ {2} \sum_ {j = 1} ^ {n} \| x _ {j} \| _ {2} ^ {2} \| (A - \mu_ {j j} I _ {m}) ^ {- 1} \| _ {F} ^ {2} + \beta^ {2} \sum_ {j = 1} ^ {n} \| (A - \mu_ {j j} I _ {m}) ^ {- 1} X \| _ {F} ^ {2} \right. \\ + \gamma^ {2} \sum_ {j = 1} ^ {n} \left. \left\| (A - \mu_ {j j} I _ {m}) ^ {- 1} \right\| _ {F} ^ {2}\right) / \| X \| _ {F} ^ {2}, \\ \end{array}
$$

while

$$
\varPhi^ {2} \approx \sum_ {j = 1} ^ {n} \left\| (A - \mu_ {j j} I _ {m}) ^ {- 1} \right\| _ {F} ^ {2} \big ((\alpha + \beta) + \gamma / \| X \| _ {F} \big) ^ {2}.
$$

These formulae show that in general $\varPsi$ and $\varPhi$ will be of similar magnitude, and we know that $\varPsi\leq\varPhi$ from the definitions. However, $\varPsi$ can be much smaller than $\varPhi$ . For example, suppose that $\gamma = 0$ and

$$
\left\| \left(A - \mu_ {n n} I _ {m}\right) ^ {- 1} \right\| _ {F} \gg \max _ {j \neq n} \left\| \left(A - \mu_ {j j} I _ {m}\right) ^ {- 1} \right\| _ {F}.
$$

Then if

$$
\frac {\| x _ {n} \| _ {2}}{\| X \| _ {F}} \ll 1 \quad \text {a n d} \quad \frac {\| (A - \mu_ {n n} I _ {m}) ^ {- 1} X \| _ {F}}{\| X \| _ {F}} \ll \| (A - \mu_ {n n} I _ {m}) ^ {- 1} \| _ {F},
$$

we have $\varPsi\ll\varPhi$ . Such examples are easily constructed. To illustrate, let $A = \mathrm{diag}(2,2,\ldots,2,1)$ and $B = \mathrm{diag}(1/2,1/2,\ldots,1/2,1-\epsilon)$ , with $\epsilon > 0$ , so that $A - \mu_{nn}I_m = \mathrm{diag}(1 + \epsilon,1 + \epsilon,\ldots,1 + \epsilon,\epsilon)$ , and let $X = (A - \mu_{nn}I_m)Y$ , where $Y = [y,y,\ldots,y,0]$ with $\|(A - \mu_{nn}I_m)y\|_2 = \|A - \mu_{nn}I_m\|_2$ and $\|y\|_2 = 1$ . Then, if $\gamma = O(\epsilon)$ ,

$$
\varPsi = O (\alpha^ {2} + \beta^ {2}), \quad \varPhi \approx \epsilon^ {- 1} (\alpha^ {2} + \beta^ {2}).
$$

To summarize, the "traditional" perturbation bound (16.25) for the Sylvester equation can severely overestimate the effect of a perturbation on the data when only $A$ and $B$ are perturbed, because it does not take account of the special structure of the problem. In contrast, the perturbation bound (16.23) does respect the Kronecker structure, and consequently is attainable for any given $A$ , $B$ , and $C$ .

To obtain an a posteriori error bound for a computed solution $\widehat{X} \coloneqq X + \Delta X$ we can set $\Delta A = 0$ , $\Delta B = 0$ , and $\Delta C = A\widehat{X} - \widehat{X}B - C = R$ in (16.22), which leads to

$$
\frac {\| X - \widehat {X} \| _ {F}}{\| X \| _ {F}} \leq \| P ^ {- 1} \| _ {2} \frac {\| R \| _ {F}}{\| X \| _ {F}}. \tag {16.28}
$$

A similar but potentially much smaller bound is described in the next section.

# 16.4. Practical Error Bounds

For the Sylvester equation we can obtain an analogue of the practical error bound (7.31) by identifying $Ax = b$ with (16.2). For the computed residual of a computed solution $\widehat{X}$ we have

$$
\begin{array}{l} \widehat {R} = f l (C - \left(f l (A \widehat {X}) - f l (\widehat {X} B)\right)) = R + \Delta R, \\ \left| \Delta R \right| \leq u | C | + \gamma_ {m + 2} | A | | \widehat {X} | + \gamma_ {n + 2} | \widehat {X} | | B | =: R _ {u}. \\ \end{array}
$$

Therefore the bound is

$$
\frac {\| X - \widehat {X} \|}{\| \widehat {X} \|} \leq \frac {\| | P ^ {- 1} | (\left| \operatorname {v e c} (\widehat {R}) \right| + \operatorname {v e c} \left(R _ {u}\right)) \|}{\| \widehat {X} \|}, \tag {16.29}
$$

where $\| X\| \coloneqq \max_{i,j}|x_{ij}|$ . After transformation by the technique illustrated in (15.1), this bound can be estimated by the LAPACK norm estimator (Algorithm 15.4) at the cost of solving a few linear systems with coefficient matrices $I_{n}\otimes A - B^{T}\otimes I_{m}$ and its transpose—in other words, solving a few Sylvester equations $AX - XB = C$ and $A^T X - XB^T = D$ . If the Bartels-Stewart algorithm is used, these solutions can be computed with the aid of the previously computed Schur decompositions of $A$ and $B$ . The condition number $\varPsi$ in (16.24) and $\operatorname{sep}(A,B) = \| P^{-1}\|_2^{-1}$ can both be estimated in much the same way; alternatively, the power method can be used (see Ghavimi and Laub [480, 1995]). Other algorithms for efficiently estimating $\operatorname{sep}(A,B)$ given Schur decompositions of $A$ and $B$ are given by Byers [191, 1984] and Kågström and Poromaa [682, 1992].

The attraction of (16.29) is that large elements in the $j$ th column of $P^{-1}$ may be countered by a small $j$ th element of $\operatorname{vec}(\widehat{R}) + \operatorname{vec}(R_u)$ , making the bound much smaller than (16.28). In this sense (16.29) has better scaling properties than (16.28), although (16.29) is not actually invariant under diagonal scalings of the Sylvester equation.

We give a numerical example to illustrate the advantage of (16.29) over (16.28). Let

$$
A = J _ {3} (0), \quad B = J _ {3} (1 0 ^ {- 3}), \quad c _ {i j} \equiv 1,
$$

where $J_{n}(\lambda)$ denotes a Jordan block of size $n$ with eigenvalue $\lambda$ . Solving the Sylvester equation by the Bartels-Stewart algorithm we found that the bounds are

$$
(1 6. 2 8): 8. 0 0 \times 1 0 ^ {- 3}, \quad (1 6. 2 9): 6. 3 6 \times 1 0 ^ {- 1 5}
$$

(where in evaluating (16.28) we replaced $R$ by $|\widehat{R}| + R_u$ , as in (16.29)). Here, $\operatorname{sep}(A, B) = 1.67 \times 10^{-16}$ , and the bound (16.29) is small because relatively large

columns of $P^{-1}$ are nullified by relatively small elements of $|\operatorname{vec}(\widehat{R})| + \operatorname{vec}(R_u)$ . For this example, with $\alpha = \| A\|_F$ , $\beta = \| B\|_F$ , $\gamma = \| C\|_F$ , we have

$$
\varPsi = 7. 0 0 \times 1 0 ^ {9}, \quad \Phi = 1. 7 0 \times 1 0 ^ {1 6},
$$

confirming that the usual perturbation bound (16.25) for the Sylvester equation can be very pessimistic. Furthermore,

$$
\frac {\| R \| _ {F}}{(\| A \| _ {F} + \| B \| _ {F}) \| \widehat {X} \| _ {F} + \| C \| _ {F}} = 7. 0 2 \times 1 0 ^ {- 2 4},
$$

$$
\sigma (\widehat {X}) = \{6 \times 1 0 ^ {1 5}, 5 \times 1 0 ^ {8}, 3 \times 1 0 ^ {2} \},
$$

$$
\eta (\widehat {X}) \approx \xi = 1. 0 0 \times 1 0 ^ {- 1 9}, \quad \mu = 2. 2 6 \times 1 0 ^ {1 3},
$$

so we have an example where the backward error is small despite a large $\mu$ .

# 16.5. Extensions

The Sylvester equation can be generalized in two main ways. One retains the linearity but adds extra coefficient matrices, yielding the generalized Sylvester equations

$$
A X B + C X D = E \tag {16.30}
$$

and

$$
A X - Y B = C, \quad D X - Y E = F. \tag {16.31}
$$

These two forms are equivalent, under conditions on the coefficient matrices [236, 1987]; for example, defining $Z \coloneqq XB$ and $W \coloneqq -CX$ , (16.30) becomes $AZ - WD = E$ , $CZ + WB = 0$ . Applications of generalized Sylvester equations include the computation of stable eigendecompositions of matrix pencils [327, 1987], [328, 1988], [683, 1996], [684, 1996] and the implementation of numerical methods for solving implicit ordinary differential equations [391, 1980].

The second generalization incorporates a quadratic term, yielding the algebraic Riccati equation

$$
A X + X B - X F X + G = 0. \tag {16.32}
$$

This general Riccati equation and its symmetric counterpart with $B = A^T$ and $F$ and $G$ symmetric are widely used in control theory.

The backward error results and perturbation theory of this chapter can be generalized in a straightforward way to (16.31) and (16.32). See Kågström [681, 1994] for (16.31) and Ghavimi and Laub [480, 1995] for (16.32). The backward error derivations do not extend to (16.30), because in this equation the coefficient matrices appear nonlinearly.

A variation of the Lyapunov equation called the discrete-time Lyapunov equation has the form

$$
X - F ^ {T} X F = Q,
$$

where $F, Q \in \mathbb{R}^{n \times n}$ . As in (16.30), the data appears nonlinearly. Ghavimi and Laub [481, 1995] show how to derive an approximation to the backward error by linearizing an equation characterizing the optimal perturbations. Generalized

versions of the Lyapunov equation and the discrete-time Lyapunov equation are considered by Penzl [934, 1998].

Another generalization of the Sylvester equation, mainly of theoretical interest, is

$$
\sum_ {i = 1} ^ {k} A _ {i} X B _ {i} = C,
$$

where $A_i \in \mathbb{R}^{m \times m}$ and $B_i \in \mathbb{R}^{n \times n}$ , $i = 1:k$ . See Lancaster [764, 1970] for associated theory.

# 16.6. Notes and References

This chapter is based on Higham [602, 1993]. The backward error derivations make use of ideas of Ghavimi and Laub [480, 1995].

The Sylvester equation is so named because Sylvester considered the homogeneous version of the equation [1119, 1884].

Bhatia and Rosenthal [109, 1997] give a survey of theoretical results for the Sylvester equation in both finite- and infinite-dimensional spaces.

For details of the role of the Sylvester equation in the eigenproblem see Bai, Demmel, and McKenney [46, 1993], [49, 1993] and the references therein.

Iterative methods that make use of matrix inversion to solve the Sylvester equation are described by Miller [849, 1988] and Roberts [988, 1980].

Hammarling [540, 1982] gives a method for solving the Lyapunov equation $AX + X A^{T} = -C$ in the case where $A$ has eigenvalues with negative real parts and $C$ is positive semidefinite; his method directly computes the Cholesky factor of the solution (which is indeed symmetric positive definite—see Problem 16.2).

A survey of the vec operator, the Kronecker product, and the vec-permutation matrix is given together with historical comments by Henderson and Searle [561, 1981]. Historical research by Henderson, Pukelsheim, and Searle [560, 1983] indicates that the Kronecker product should be called the Zehfuss product, in recognition of an 1858 paper by Zehfuss that gives a determinantal result involving the product.

The vec-permutation matrix $\Pi$ (which appears in (16.27)) is given explicitly by

$$
\varPi = \sum_ {i, j = 1} ^ {n} \left(e _ {i} e _ {j} ^ {T}\right) \otimes \left(e _ {j} e _ {i} ^ {T}\right),
$$

and has the property that $(A\otimes B)\Pi = \Pi (B\otimes A)$ . It is also known as the commutation matrix [804, 1979], [805, 1979],

Applications of the Lyapunov equation in control theory, including special situations where an approximate solution of low rank is required, are discussed by Hodel [630, 1992]. A much older reference to applications is Barnett and Storey [78, 1968].

Algorithms and software for solving (16.30) are developed by Gardiner, Wette, Laub, Amato, and Moler [457, 1992], [458, 1992].

Perturbation theory for Lyapunov and Riccati equations can be found in the work of Byers [192, 1985], Hewer and Kenney [569, 1988], [724, 1990], and Gahinet, Laub, Kenney, and Hewer [450, 1990].

Chu [236, 1987] determines conditions for the existence of unique solutions to the generalized Sylvester equations (16.30) and (16.31). The appropriate conditions for (16.30) are that the pencils $A + \lambda C$ and $D + \lambda B$ are regular and the spectra of the pencils have an empty intersection, which neatly generalizes the conditions for the Sylvester equation to have a unique solution; the conditions for (16.31) are analogous.

There is much work on algorithms and software for solving the algebraic Riccati equation. For a sampling, see Laub [771, 1979], Arnold and Laub [37, 1984], Byers [193, 1987], Gardiner, and Laub [456, 1991], and Kenney, Laub, and Papadopoulos [729, 1992].

An algorithm for estimating a generalization of sep that occurs in perturbation theory for the generalized Sylvester equation (16.31) is developed by Kågström and Westin [685, 1989].

Another generalization of the Sylvester equation is to take just one equation from (16.31), $AX - YB = C$ ((16.13) is of this form). This equation can be underdetermined or overdetermined, depending on the dimensions of the coefficient matrices. Conditions involving generalized inverses that are both necessary and sufficient for the existence of a solution are given by Baksalary and Kala [58, 1979]. Zietak examines the inconsistent case [1283, 1985] for one choice of dimensions giving an overdetermined system. Stewart [1073, 1992] shows how to compute a minimum Frobenius norm least squares solution. The even more general equation $AXB + CYD = E$ has also been analysed by Baksalary and Kala [59, 1980], who again give necessary and sufficient conditions for the existence of a solution.

# 16.6.1. LAPACK

The computations discussed in this chapter can all be done using LAPACK. The Bartels-Stewart algorithm can be implemented by calling xGEES to compute the Schur decomposition, using the level-3 BLAS routine xGEMM to transform the right-hand side $C$ , calling xTRSYL to solve the (quasi-) triangular Sylvester equation, and using xGEMM to transform back to the solution $X$ . The error bound (16.29) can be estimated using xLACON in conjunction with the above routines.

Routine xLASY2 solves a real Sylvester equation $AX \pm XB = \sigma C$ in which $A$ and $B$ have dimension 1 or 2 and $\sigma$ is a scale factor. It is called by xTRSYL.

LAPACK also contains a code xTGSYL for solving (16.31), for the case where the coefficient matrices are in (quasi-) triangular form. See Kågström and Poromaa [684, 1996] for a description of the underlying algorithm.

# Problems

16.1. Show that the Sylvester equation $AX - XA = I$ has no solution.

16.2. (Bellman [101, 1970, §10.18]) Show that if the expression

$$
X = - \int_ {0} ^ {\infty} e ^ {A t} C e ^ {B t} d t
$$

exists for all $C$ it represents the unique solution of the Sylvester equation $AX + XB = C$ . (Hint: consider the matrix differential equation $\frac{dZ}{dt} = AZ(t) + Z(t)B$ , $Z(0) = C$ .) Deduce that the Lyapunov equation $AX + XA^T = -C$ has a symmetric positive definite solution if $A$ has eigenvalues with negative real parts and $C$ is symmetric positive definite.

16.3. (Byers and Nash [195, 1987]) Let $A \in \mathbb{R}^{n \times n}$ and consider

$$
\operatorname {s e p} (A, - A ^ {T}) = \min  _ {X \neq 0} \frac {\| A X + X A ^ {T} \| _ {F}}{\| X \| _ {F}}.
$$

Show that there exists a minimizer $X$ that is either symmetric or skew-symmetric.

16.4. How would you solve a Sylvester equation $AX - XB = C$ in which $A$ and $B$ are of dimension 1 or 2? Compare your method with the one used in the LAPACK routine xLASY2.

16.5. (RESEARCH PROBLEM) Derive conditions for the Sylvester equation to have a well-conditioned solution.
