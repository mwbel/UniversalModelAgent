# Chapter 20

# The Least Squares Problem

For some time it has been believed that orthogonalizing methods

did not suffer this squaring of the condition number ...

It caused something of a shock, therefore,

when in 1966 Golub and Wilkinson ... asserted that

already the multiplications $QA$ and $Qb$ may produce errors in the solution

containing a factor $\chi^2 (A)$

A. VAN DER SLUIS,

Stability of the Solutions of Linear Least Squares Problems (1975)

Most packaged regression problems do compute a cross-products matrix and solve the normal equations using a matrix inversion subroutine.

All the programs ... that disagreed

(and some of those that agreed) with the unperturbed solution

tried to solve the normal equations.

— ALBERT E. BEATON, DONALD B. RUBIN, and JOHN L. BARONE,

The Acceptability of Regression Solutions:

Another Look at Computational Accuracy (1976)

On January 1, 1801 Giuseppe Piazzi discovered the asteroid Ceres.

Ceres was only visible for forty days

before it was lost to view behind the sun ...

Gauss, using three observations, extensive analysis,

and the method of least squares, was able to

determine the orbit with such accuracy that Ceres was

easily found when it reappeared in late 1801.

DAVID K. KAHANER, CLEVE B. MOLER, and STEPHEN G. NASH,

Numerical Methods and Software (1989)

In this chapter we consider the least squares (LS) problem $\min_x\| b - Ax\| _2$ , where $A\in \mathbb{R}^{m\times n}$ ( $m\geq n$ ) has full rank. We begin by examining the sensitivity of the LS problem to perturbations. Then we examine the stability of methods for solving the LS problem, covering QR factorization methods, the normal equations and seminormal equations methods, and iterative refinement. Finally, we show how to compute the backward error of an approximate LS solution.

We do not develop the basic theory of the LS problem, which can be found in standard textbooks (see, for example, Golub and Van Loan [509, 1996, §5.3]). However, we recall the fundamental result that any solution of the LS problem satisfies the normal equations $A^T A x = A^T b$ (see Problem 20.1). Therefore if $A$ has full rank there is a unique LS solution. More generally, whatever the rank of $A$ the vector $x_{LS} = A^{+}b$ is an LS solution, and it is the solution of minimal 2-norm. Here, $A^{+}$ is the pseudo-inverse of $A$ (given by $A^{+} = (A^{T}A)^{-1}A^{T}$ when $A$ has full rank); see Problem 20.3. (For more on the pseudo-inverse see Stewart and Sun [1083, 1990, §3.1].)

# 20.1. Perturbation Theory

Perturbation theory for the LS problem is, not surprisingly, more complicated than for linear systems, and there are several forms in which bounds can be stated. We begin with a normwise perturbation theorem that is a restatement of a result of Wedin [1211, 1973, Thm. 5.1]. For an arbitrary rectangular matrix $A$ we define the condition number $\kappa_{2}(A) = \| A \|_{2} \| A^{+} \|_{2}$ . If $A$ has $r = \mathrm{rank}(A)$ nonzero singular values, $\sigma_{1} \geq \dots \geq \sigma_{r}$ , then $\kappa_{2}(A) = \sigma_{1} / \sigma_{r}$ .

Theorem 20.1 (Wedin). Let $A \in \mathbb{R}^{m \times n}$ ( $m \geq n$ ) and $A + \Delta A$ both be of full rank, and let

$$
\begin{array}{l} \left\| b - A x \right\| _ {2} = \min , \quad r = b - A x, \\ \left\| (b + \Delta b) - (A + \Delta A) y \right\| _ {2} = \min , \quad s = b + \Delta b - (A + \Delta A) y, \\ \| \Delta A \| _ {2} \leq \epsilon \| A \| _ {2}, \quad \| \Delta b \| _ {2} \leq \epsilon \| b \| _ {2}. \\ \end{array}
$$

Then, provided that $\kappa_{2}(A)\epsilon < 1$

$$
\frac {\| x - y \| _ {2}}{\| x \| _ {2}} \leq \frac {\kappa_ {2} (A) \epsilon}{1 - \kappa_ {2} (A) \epsilon} \left(2 + \left(\kappa_ {2} (A) + 1\right) \frac {\| r \| _ {2}}{\| A \| _ {2} \| x \| _ {2}}\right), \tag {20.1}
$$

$$
\frac {\| r - s \| _ {2}}{\| b \| _ {2}} \leq (1 + 2 \kappa_ {2} (A)) \epsilon . \tag {20.2}
$$

These bounds are approximately attainable.

Proof. We defer a proof until §20.10, since the techniques used in the proof are not needed elsewhere in this chapter. $\square$

The bound (20.1) is usually interpreted as saying that the sensitivity of the LS problem is measured by $\kappa_{2}(A)$ when the residual is small or zero and by $\kappa_{2}(A)^{2}$ otherwise. This means that the sensitivity of the LS problem depends strongly on $b$ as well as $A$ , unlike for a square linear system.

Here is a simple example where the $\kappa_{2}(A)^{2}$ effect is seen:

$$
A = \left[ \begin{array}{c c} 1 & 0 \\ 0 & \delta \\ 0 & 0 \end{array} \right], \quad \varDelta A = \left[ \begin{array}{c c} 0 & 0 \\ 0 & 0 \\ 0 & \delta / 2 \end{array} \right], \quad b = \left[ \begin{array}{c} 1 \\ 0 \\ 1 \end{array} \right], \quad \varDelta b = 0.
$$

It is a simple exercise to verify that

$$
x = \left[ \begin{array}{c} 1 \\ 0 \end{array} \right], \quad r = \left[ \begin{array}{c} 0 \\ 0 \\ 1 \end{array} \right], \quad y = \left[ \begin{array}{c} 1 \\ \frac {2}{5 \delta} \end{array} \right], \quad s = \left[ \begin{array}{c} 0 \\ - \frac {2}{5} \\ \frac {4}{5} \end{array} \right].
$$

Since $\kappa_{2}(A) = 1 / \delta$

$$
\begin{array}{l} \frac {\| x - y \| _ {2}}{\| x \| _ {2}} = \frac {2}{5 \delta} \lesssim \kappa_ {2} (A) ^ {2} \frac {\| \Delta A \| _ {2}}{\| A \| _ {2}} = \frac {1}{2 \delta}, \\ \frac {\| r - s \| _ {2}}{\| b \| _ {2}} = \frac {1}{\sqrt {5}} \lesssim \kappa_ {2} (A) \frac {\| \varDelta A \| _ {2}}{\| A \| _ {2}} = \frac {1}{2}. \\ \end{array}
$$

Surprisingly, it is easier to derive componentwise perturbation bounds than normwise ones for the LS problem. The key idea is to express the LS solution and its residual as the solution of the augmented system

$$
\left[ \begin{array}{l l} I & A \\ A ^ {T} & 0 \end{array} \right] \left[ \begin{array}{l} r \\ x \end{array} \right] = \left[ \begin{array}{l} b \\ 0 \end{array} \right], \tag {20.3}
$$

which is simply another way of writing the normal equations, $A^T A x = A^T b$ . This is a square nonsingular system, so standard techniques can be applied. The perturbed system of interest is

$$
\left[ \begin{array}{c c} I & A + \Delta A \\ (A + \Delta A) ^ {T} & 0 \end{array} \right] \left[ \begin{array}{l} s \\ y \end{array} \right] = \left[ \begin{array}{c} b + \Delta b \\ 0 \end{array} \right], \tag {20.4}
$$

where we assume that

$$
\left| \Delta A \right| \leq \epsilon E, \quad \left| \Delta b \right| \leq \epsilon f. \tag {20.5}
$$

From (20.3) and (20.4) we obtain

$$
\left[ \begin{array}{c c} I & A \\ A ^ {T} & 0 \end{array} \right] \left[ \begin{array}{c} s - r \\ y - x \end{array} \right] = \left[ \begin{array}{c} \Delta b - \Delta A y \\ - \Delta A ^ {T} s \end{array} \right].
$$

Premultiplying by the inverse of the matrix on the left (obtainable from Problem 13.8) gives

$$
\left[ \begin{array}{c} s - r \\ y - x \end{array} \right] = \left[ \begin{array}{c c} I - A A ^ {+} & (A ^ {+}) ^ {T} \\ A ^ {+} & - (A ^ {T} A) ^ {- 1} \end{array} \right] \left[ \begin{array}{c} \Delta b - \Delta A y \\ - \Delta A ^ {T} s \end{array} \right]. \tag {20.6}
$$

Looking at the individual block components we obtain

$$
\left| s - r \right| \leq \epsilon \left(\left| I - A ^ {+} A \right| (f + E | y |\right) + \left| A ^ {+} \right| ^ {T} E ^ {T} | s |\left. \right), \tag {20.7}
$$

$$
| y - x | \leq \epsilon \left(| A ^ {+} | (f + E | y |) + | \left(A ^ {T} A\right) ^ {- 1} | E ^ {T} | s |\right). \tag {20.8}
$$

(Note that $\| I - AA^{+}\|_{2} = \min \{1,m - n\}$ , as is easily proved using the SVD.) On taking norms we obtain the desired perturbation result.

Theorem 20.2. Let $A \in \mathbb{R}^{m \times n}$ ( $m \geq n$ ) and $A + \Delta A$ be of full rank. For the perturbed LS problem described by (20.4) and (20.5) we have

$$
\frac {\| x - y \|}{\| x \|} \leq \epsilon \frac {\| | A ^ {+} | (f + E | y |) \| + \| | (A ^ {T} A) ^ {- 1} | E ^ {T} | s | \|}{\| x \|}, \tag {20.9}
$$

$$
\frac {\| r - s \|}{\| r \|} \leq \epsilon \frac {\| | I - A A ^ {+} | (f + E | y |) \| + \| | A ^ {+} | ^ {T} E ^ {T} | s | \|}{\| r \|}, \tag {20.10}
$$

for any absolute norm. These bounds are approximately attainable.

For a square system, we have $s = 0$ , and we essentially recover Theorem 7.4. Note, however, that the bounds contain the perturbed vectors $y$ and $s$ . For theoretical analysis it may be preferable to use alternative bounds in which $x$ and $r$ replace $y$ and $s$ and there is an extra factor

$$
\left(1 - \epsilon \left\| \left[ \begin{array}{c c} | I - A A ^ {+} | & | A ^ {+} | ^ {T} \\ | A ^ {+} | & | (A ^ {T} A) ^ {- 1} | \end{array} \right] \left[ \begin{array}{c c} 0 & E \\ E ^ {T} & 0 \end{array} \right] \right\|\right) ^ {- 1},
$$

where the term in parentheses is assumed to be positive. For practical computation (20.9) is unsatisfactory because we do not know $s = b + \Delta b - (A + \Delta A)y$ . However, as Stewart and Sun observe [1083, 1990, p. 159], $\widehat{r} = b - Ay$ is computable and

$$
\left| s \right| \leq \left| \widehat {r} \right| + \epsilon (f + E | y |),
$$

and using this bound in (20.9) makes only a second-order change.

The componentwise bounds enjoy better scaling properties than the normwise ones. If $E = |A|$ and $f = |b|$ then the bounds (20.7) and (20.8), and to a lesser extent (20.9) and (20.10), are invariant under column scalings $b - Ax \to b - AD \cdot D^{-1}x$ ( $D$ diagonal). Row scaling does affect the componentwise bounds, since it changes the LS solution, but the componentwise bounds are less sensitive to the row scaling than the normwise bounds, in a way that is difficult to make precise.

# 20.2. Solution by QR Factorization

Let $A \in \mathbb{R}^{m \times n}$ , with $m \geq n$ and $\operatorname{rank}(A) = n$ . If $A$ has the QR factorization

$$
Q ^ {T} A = \left[ \begin{array}{l} R \\ 0 \end{array} \right]
$$

then

$$
\begin{array}{l} \| A x - b \| _ {2} ^ {2} = \| Q ^ {T} A x - Q ^ {T} b \| _ {2} ^ {2} =: \left\| \left[ \begin{array}{c} R x - c \\ - d \end{array} \right] \right\| _ {2} ^ {2} \\ = \| R x - c \| _ {2} ^ {2} + \| d \| _ {2} ^ {2}. \\ \end{array}
$$

It follows that the unique LS solution is $x = R^{-1}c$ , and the residual $\| b - Ax\|_2 = \| d\|_2$ . Thus the LS problem can be solved with relatively little extra work beyond the computation of a QR factorization. Note that $Q$ is not required explicitly;

we just need the ability to apply $Q^T$ to a vector. The cost of the solution is $2n^{2}(m - n / 3)$ flops if we use Householder QR factorization.

It is well known that the Givens and Householder QR factorization algorithms provide a normwise backward stable way to solve the LS problem. The next result expresses this fact for the Householder method and also provides columnwise backward error bounds (essentially the same result holds for the Givens method).

Theorem 20.3. Let $A \in \mathbb{R}^{m \times n}$ ( $m \geq n$ ) have full rank and suppose the LS problem $\min_x \| b - Ax \|_2$ is solved using the Householder QR factorization method. The computed solution $\widehat{x}$ is the exact LS solution to

$$
\min  _ {x} \| (b + \Delta b) - (A + \Delta A) \hat {x} \| _ {2},
$$

where

$$
\| \Delta a _ {j} \| _ {2} \leq \tilde {\gamma} _ {m n} \| a _ {j} \| _ {2}, \quad j = 1: n, \quad \| \Delta b \| _ {2} \leq \tilde {\gamma} _ {m n} \| b \| _ {2}.
$$

Proof. The proof is a straightforward generalization of the proof of Theorem 19.5 and is left as an exercise (Problem 20.2). $\square$

As for Theorem 19.5 (see (19.14)), Theorem 20.3 remains true if we set $\Delta b \equiv 0$ , but in general there is no advantage to restricting the perturbations to $A$ .

Theorem 20.3 is a strong result, but it does not bound the residual of the computed solution, which, after all, is what we are trying to minimize. How close, then, is $\| b - A\widehat{x}\| _2$ to $\min_{x}\| b - Ax\|_{2}$ ? We can answer this question using the perturbation theory of §20.1. With $\widehat{r} := b + \varDelta b - (A + \varDelta A)\widehat{x}$ , $x := x_{LS}$ , and $r := b - Ax$ , (20.6) yields

$$
\widehat {r} - r = (I - A A ^ {+}) (\Delta b - \Delta A \widehat {x}) - (A ^ {+}) ^ {T} \Delta A ^ {T} \widehat {r},
$$

so that

$$
(b - A \widehat {x}) - r = - A A ^ {+} (\Delta b - \Delta A \widehat {x}) - (A ^ {+}) ^ {T} \Delta A ^ {T} \widehat {r}.
$$

Substituting the bounds for $\Delta A$ and $\Delta b$ from Theorem 20.3, written in the form $|\Delta A| \leq \tilde{\gamma}_{mn} ee^T |A|$ , $|\Delta b| \leq \tilde{\gamma}_{mn} ee^T |b|$ , and noting that $\| AA^+ \|_2 = 1$ , we obtain

$$
\begin{array}{l} \| (b - A \hat {x}) - r \| _ {2} \leq \tilde {\gamma} _ {m n} \left(\| e e ^ {T} (| b | + | A | | x |) \| _ {2} + \| | A ^ {+} | ^ {T} | A ^ {T} | e e ^ {T} | r | \| _ {2}\right) + O \left(u ^ {2}\right) \\ \leq m \tilde {\gamma} _ {m n} \left(\| | b | + | A \| x | \| _ {2} + \operatorname {c o n d} _ {2} \left(A ^ {T}\right) \| r \| _ {2}\right) + O \left(u ^ {2}\right), \\ \end{array}
$$

where $\operatorname{cond}_2(A) \coloneqq \| |A^+||A\|$

$$
\left\| b - A \widehat {x} \right\| _ {2} \leq m \widetilde {\gamma} _ {m n} \| | b | + | A | | x | \| _ {2} + \left(1 + m \widetilde {\gamma} _ {m n} \operatorname {c o n d} _ {2} \left(A ^ {T}\right)\right) \| r \| _ {2} + O \left(u ^ {2}\right).
$$

This bound contains two parts. The term $m\tilde{\gamma}_{mn} \| |b| + |A||x| \|_2$ is a multiple of the bound for the error in evaluating $fl(b - Ax)$ , and so is to be expected. The factor $1 + m\tilde{\gamma}_{mn} \operatorname{cond}_2(A^T)$ will be less than 1.1 (say) provided that $\operatorname{cond}_2(A^T)$ is not too large. Note that $\operatorname{cond}_2(A^T) \leq n\kappa_2(A)$ and $\operatorname{cond}_2(A^T)$ is invariant under column scaling of $A$ ( $A \gets A \operatorname{diag}(d_i), d_i \neq 0$ ). The conclusion is that, unless $A$ is very ill conditioned, the residual $b - A\widehat{x}$ will not exceed the larger of the true residual $r = b - Ax$ and a constant multiple of the error in evaluating $fl(r)$ —a very satisfactory result.

# 20.3. Solution by the Modified Gram-Schmidt Method

The modified Gram-Schmidt (MGS) method can be used to solve the LS problem. However, we must not compute $x$ from $x = R^{-1}(Q^T b)$ , because the lack of orthonormality of the computed $\hat{Q}$ would adversely affect the stability. Instead we apply MGS to the augmented matrix $[A \quad b]$ :

$$
\left[ \begin{array}{c c} A & b \end{array} \right] = \left[ \begin{array}{c c} Q _ {1} & q _ {n + 1} \end{array} \right] \left[ \begin{array}{c c} R & z \\ 0 & \rho \end{array} \right].
$$

We have

$$
\begin{array}{l} A x - b = \left[ \begin{array}{c c} A & b \end{array} \right] \left[ \begin{array}{c} x \\ - 1 \end{array} \right] = \left[ \begin{array}{c c} Q _ {1} & q _ {n + 1} \end{array} \right] \left[ \begin{array}{c} R x - z \\ - \rho \end{array} \right] \\ = Q _ {1} (R x - z) - \rho q _ {n + 1}. \\ \end{array}
$$

Since $q_{n+1}$ is orthogonal to the columns of $Q_1$ , $\| b - Ax\|_2^2 = \| Rx - z\|_2^2 + \rho^2$ , so the LS solution is $x = R^{-1}z$ . Of course, $z = Q_1^T b$ , but $z$ is now computed as part of the MGS procedure instead of as a product between $Q^T$ and $b$ .

Björck [119, 1967] showed that this algorithm is forward stable, in the sense that the forward error $\| x - \widehat{x}\| _2 / \| x\| _2$ is as small as that for a normwise backward stable method. It was subsequently shown by Björck and Paige [131, 1992] that the algorithm is, in fact, normwise backward stable (see also Björck [127, 1994]), that is, a normwise result of the form in Theorem 20.3 holds. Moreover, a columnwise result of the form in Theorem 20.3 holds too—see Problem 20.5. Hence the possible lack of orthonormality of $\widehat{Q}$ does not impair the stability of the MGS method as a means for solving the LS problem.

# 20.4. The Normal Equations

The oldest method of solving the LS problem is to form and solve the normal equations, $A^T A x = A^T b$ . Assuming that $A$ has full rank, we can use the following procedure:

Form $C = A^T A$ and $c = A^T b$ .

Compute the Cholesky factorization $C = R^T R$ .

Solve $R^T y = c$ , $Rx = y$ .

Cost: $n^2 (m + n / 3)$ flops.

If $m \gg n$ , the normal equations method requires about half as many flops as the Householder QR factorization approach (or the MGS method). However, it has less satisfactory numerical stability properties. There are two problems. The first is that information may be lost when $\widehat{C} = fl(A^T A)$ is formed—essentially because forming the cross product is a squaring operation that increases the dynamic range of the data. A simple example is the matrix

$$
A = \left[ \begin{array}{c c} 1 & 1 \\ \epsilon & 0 \end{array} \right], \qquad 0 <   \epsilon <   \sqrt {u},
$$

for which

$$
A ^ {T} A = \left[ \begin{array}{c c} 1 + \epsilon^ {2} & 1 \\ 1 & 1 \end{array} \right], \qquad f l (A ^ {T} A) = \left[ \begin{array}{c c} 1 & 1 \\ 1 & 1 \end{array} \right].
$$

Even though $A$ is distance approximately $\epsilon$ from a rank-deficient matrix, and hence unambiguously full rank if $\epsilon \approx \sqrt{u / 2}$ , the computed cross product is singular. In general, whenever $\kappa_{2}(A) \geq u^{-1 / 2}$ we can expect $\widehat{C}$ to be singular or indefinite, in which case Cholesky factorization is likely to break down (Theorem 10.7).

The second weakness of the normal equations method is more subtle and is explained by a rounding error analysis. In place of $C = A^T A$ and $c = A^T b$ we compute

$$
\begin{array}{l} \widehat {C} = A ^ {T} A + \Delta C _ {1}, \quad | \Delta C _ {1} | \leq \gamma_ {m} | A ^ {T} | | A |, \\ \hat {c} = A ^ {T} b + \Delta c, \quad | \Delta c | \leq \gamma_ {m} | A ^ {T} | | b |. \\ \end{array}
$$

By Theorems 10.3 and 10.4, the computed Cholesky factor $\widehat{R}$ and solution $\widehat{x}$ satisfy

$$
\begin{array}{l} \widehat {R} ^ {T} \widehat {R} = \widehat {C} + \Delta C _ {2}, \quad | \Delta C _ {2} | \leq \gamma_ {n + 1} | \widehat {R} ^ {T} | | \widehat {R} |, \tag {20.11} \\ (\widehat {C} + \Delta C _ {3}) \widehat {x} = \widehat {c}, \quad | \Delta C _ {3} | \leq \gamma_ {3 n + 1} | \widehat {\boldsymbol {R}} ^ {T} | | \widehat {\boldsymbol {R}} |. \\ \end{array}
$$

Overall,

$$
\begin{array}{l} \left(A ^ {T} A + \Delta A\right) \widehat {x} = A ^ {T} b + \Delta c, \tag {20.12} \\ \left| \Delta A \right| \leq \gamma_ {m} \left| A ^ {T} \right| \left| A \right| + \gamma_ {3 n + 1} \left| \widehat {R} ^ {T} \right| \left| \widehat {R} \right|, \quad \left| \Delta c \right| \leq \gamma_ {m} \left| A ^ {T} \right| \left| b \right|. \\ \end{array}
$$

By bounding $\| |\widehat{R}^T ||\widehat{R}||_2$ with the aid of (20.11), we find that

$$
\begin{array}{l} \left\| \Delta A \right\| _ {2} \leq \left(m n + 3 n ^ {2} + n\right) u \| A \| _ {2} ^ {2} + O \left(u ^ {2}\right), (20.13a) \\ \left\| \Delta c \right\| _ {2} \leq m n ^ {1 / 2} u \| A \| _ {2} \| b \| _ {2} + O \left(u ^ {2}\right). (20.13b) \\ \end{array}
$$

These bounds show that we have solved the normal equations in a backward stable way, as long as $\| A \|_2 \| b \|_2 \approx \| A^T b \|_2$ . But if we try to translate this result into a backward error result for the LS problem itself, we find that the best backward error bound contains a factor $\kappa_2(A)$ [623, 1987]. The best forward error bound we can expect, in view of (20.13), is of the form

$$
\frac {\| x - \widehat {x} \| _ {2}}{\| x \| _ {2}} \lesssim c _ {m, n} \kappa_ {2} (A) ^ {2} u \tag {20.14}
$$

(since $\kappa_2(A^TA) = \kappa_2(A)^2$ ). Now we know from Theorem 20.1 that the sensitivity of the LS problem is measured by $\kappa_2(A)^2$ if the residual is large, but by $\kappa_2(A)$ if the residual is small. It follows that the normal equations method has a forward error bound that can be much larger than that possessed by a backward stable method.

A mitigating factor for the normal equations method is that, in view of Theorem 10.6, we can replace (20.14) by the (not entirely rigorous) bound

$$
\frac {\| D (x - \widehat {x}) \| _ {2}}{\| D x \| _ {2}} \lesssim c _ {m, n} \kappa_ {2} (B) ^ {2} u,
$$

where $A = BD$ , with $D = \mathrm{diag}(\|A(:,i)\|_2)$ , so that $B$ has columns of unit 2-norm. Van der Sluis's result (Theorem 7.5) shows that

$$
\kappa_ {2} (B) \leq \sqrt {n} \underset {F} {\operatorname * {m i n}} _ {\mathrm {d i a g o n a l}} \kappa_ {2} (A F).
$$

Hence the normal equations method is, to some extent, insensitive to poor column scaling of $A$ .

Although numerical analysts almost invariably solve the full rank LS problem by QR factorization, statisticians frequently use the normal equations (though perhaps less frequently than they used to, thanks to the influence of numerical analysts). The normal equations do have a useful role to play. In many statistical problems the regression matrix is contaminated by errors of measurement that are very large relative to the roundoff level; the effects of rounding errors are then likely to be insignificant compared with the effects of the measurement errors, especially if IEEE double precision (as opposed to single precision) arithmetic is used.

The normal equations (NE) versus (Householder) QR factorization debate can be summed up as follows.

- The two methods have a similar computational cost if $m \approx n$ , but the NE method is up to twice as fast for $m \gg n$ . (This statement assumes that $A$ and $b$ are dense; for details of the storage requirements and computational cost of each method for sparse matrices, see, for example, Björck [128, 1996] and Heath [556, 1984].)   
- The QR method is always backward stable. The NE method is guaranteed to be backward stable only if $A$ is well conditioned.   
- The forward error from the NE method can be expected to exceed that for the QR method when $A$ is ill conditioned and the residual of the LS problem is small.   
- The QR method lends itself to iterative refinement, as described in the next section. Iterative refinement can be applied to the NE method, but the rate of convergence inevitably depends on $\kappa_{2}(A)^{2}$ instead of $\kappa_{2}(A)$ .

# 20.5. Iterative Refinement

As for square linear systems, iterative refinement can be used to improve the accuracy and stability of an approximate LS solution. However, for the LS problem there is more than one way to construct an iterative refinement scheme.

By direct analogy with the square system case, we might consider the scheme

1. Compute $r = b - A\widehat{x}$   
2. Solve the LS problem $\min_d\| Ad - r\| _2$   
3. Update $y = \widehat{x} + d$ .

(Repeat from step 1 if necessary, with $\widehat{x}$ replaced by $y$ .)

This scheme is certainly efficient—a computed QR factorization (for example) of $A$ can be reused at each step 2. Golub and Wilkinson [505, 1966] investigated this scheme and found that it works well only for nearly consistent systems.

An alternative approach suggested by Björck [118, 1967] is to apply iterative refinement to the augmented system (20.3), so that both $x$ and $r$ are refined simultaneously. Since this is a square, nonsingular system, existing results on the convergence and stability of iterative refinement can be applied, and we would expect the scheme to work well. To make precise statements we need to examine the augmented system method in detail.

For the refinement steps we need to consider an augmented system with an arbitrary right-hand side:

$$
r + A x = f, \tag {20.15a}
$$

$$
A ^ {T} r = g. \tag {20.15b}
$$

If $A$ has the QR factorization

$$
A = Q \left[ \begin{array}{c} R \\ 0 \end{array} \right],
$$

where $R\in \mathbb{R}^{n\times n}$ , then (20.15) transforms to

$$
Q ^ {T} r + \left[ \begin{array}{c} R \\ 0 \end{array} \right] x = Q ^ {T} f,
$$

$$
\left[ \begin{array}{c c} R ^ {T} & 0 \end{array} \right] Q ^ {T} r = g.
$$

This system can be solved as follows:

$$
h = R ^ {- T} g,
$$

$$
d = Q ^ {T} f = \left[ \begin{array}{c} d _ {1} \\ d _ {2} \end{array} \right],
$$

$$
r = Q \left[ \begin{array}{c} h \\ d _ {2} \end{array} \right],
$$

$$
x = R ^ {- 1} \left(d _ {1} - h\right).
$$

The next result describes the effect of rounding errors on the solution process. The bounds are columnwise, but we state them as componentwise inequalities for convenience.

Theorem 20.4. Let $A \in \mathbb{R}^{m \times n}$ be of full rank $n \leq m$ and suppose the augmented system (20.15) is solved using a Householder QR factorization of $A$ as described above. The computed $\widehat{x}$ and $\widehat{r}$ satisfy

$$
\left[ \begin{array}{c c} I & A + \varDelta A _ {1} \\ (A + \varDelta A _ {2}) ^ {T} & 0 \end{array} \right] \left[ \begin{array}{c} \widehat {r} \\ \widehat {x} \end{array} \right] = \left[ \begin{array}{c} f + \varDelta f \\ g + \varDelta g \end{array} \right],
$$

where

$$
\left| \Delta A _ {i} \right| \leq m n \tilde {\gamma} _ {m} G | A |, \quad i = 1: 2,
$$

$$
\left| \Delta f \right| \leq m ^ {1 / 2} n \tilde {\gamma} _ {m} \left(H _ {1} | f | + H _ {2} | \hat {r} |\right),
$$

$$
\left| \Delta g \right| \leq m ^ {1 / 2} n \tilde {\gamma} _ {m} \left| A ^ {T} \right| H _ {3} | \widehat {r} |,
$$

with $\| G\| _F = 1$ ， $\| H_i\| _F = 1$ ， $i = 1:3$

Proof. The proof does not involve any new ideas and is rather tedious, so we omit it. $\square$

Consider first fixed precision iterative refinement. Theorem 20.4 implies that the computed solution $(\hat{r}^T, \hat{x}^T)^T$ to (20.15) satisfies

$$
\begin{array}{l} \left| \left[ \begin{array}{c} f \\ g \end{array} \right] - \left[ \begin{array}{c c} I & A \\ A ^ {T} & 0 \end{array} \right] \left[ \begin{array}{c} \widehat {r} \\ \widehat {x} \end{array} \right] \right| \leq m n \widetilde {\gamma} _ {m} \left(\left[ \begin{array}{c c} H _ {2} & G | A | \\ | A ^ {T} | (G ^ {T} + H _ {3}) & 0 \end{array} \right] \left[ \begin{array}{c} | \widehat {r} | \\ | \widehat {x} | \end{array} \right] \right. \\ \left. + \left[ \begin{array}{c c} H _ {1} & 0 \\ 0 & 0 \end{array} \right] \left[ \begin{array}{c} | f | \\ | g | \end{array} \right]\right). \\ \end{array}
$$

Unfortunately, this bound is not of a form that allows us to invoke Theorem 12.4. However, we can apply Theorem 12.3, which tells us that the corrected solution $(\widehat{s}^T,\widehat{y}^T)^T$ obtained after one step of iterative refinement satisfies

$$
\begin{array}{l} \left| \left[ \begin{array}{c} b \\ 0 \end{array} \right] - \left[ \begin{array}{c c} I & A \\ A ^ {T} & 0 \end{array} \right] \left[ \begin{array}{c} \widehat {s} \\ \widehat {y} \end{array} \right] \right| \leq m n \widetilde {\gamma} _ {m} \left[ \begin{array}{c c} H _ {1} & 0 \\ 0 & 0 \end{array} \right] \left[ \begin{array}{c} | \widehat {r} _ {1} | \\ | \widehat {r} _ {2} | \end{array} \right] + u \left[ \begin{array}{c c} I & | A | \\ | A ^ {T} | & 0 \end{array} \right] \left[ \begin{array}{c} | \widehat {s} | \\ | \widehat {y} | \end{array} \right] \\ + \gamma_ {m + n + 1} \left(\left[ \begin{array}{c c} I & | A | \\ | A ^ {T} | & 0 \end{array} \right] \left[ \begin{array}{c} | \widehat {s} | \\ | \widehat {y} | \end{array} \right] + \left[ \begin{array}{c} | b | \\ 0 \end{array} \right]\right) \\ + O \left(u ^ {2}\right). \tag {20.16} \\ \end{array}
$$

Here, $(\widehat{r}_1^T,\widehat{r}_2^T)^T$ denotes the residual of the augmented system corresponding to the original computed solution. We will make two simplifications to the bound (20.16). First, since $(\widehat{r}_1^T,\widehat{r}_2^T)^T = O(u)$ , the first term in the bound may be included in the $O(u^{2})$ term. Second, (20.16) yields $|b - \widehat{s} -A\widehat{y}| = O(u)$ and so $|\widehat{s} |\leq |A||\widehat{y}| + |b| + O(u)$ . With these two simplifications, (20.16) may be written

$$
\left|\left[ \begin{array}{c}b\\ 0 \end{array} \right] - \left[ \begin{array}{cc}I & A\\ A^{T} & 0 \end{array} \right]\left[ \begin{array}{c}\widehat{s}\\ \widehat{y} \end{array} \right]\right|\leq 2\gamma_{m + n + 2}\left(\left[ \begin{array}{cc}0 & |A|\\ |A^{T}| & 0 \end{array} \right]\left[ \begin{array}{c}|\widehat{s}|\\ |\widehat{y} | \end{array} \right] + \left[ \begin{array}{c}|b\\ 0 \end{array} \right]\right) + O(u^{2}).
$$

In view of the Oettli-Prager result (Theorem 7.3) this inequality tells us that, asymptotically, the solution $\hat{y}$ produced after one step of fixed precision iterative refinement has a small componentwise relative backward error with respect to the augmented system. However, this backward error allows the two occurrences of $A$ in the augmented system coefficient matrix to be perturbed differently, and thus is not a true componentwise backward error for the LS problem. Nevertheless, the result tells us that iterative refinement can be expected to produce some improvement in stability. Note that the bound in Theorem 20.2 continues to hold if we perturb the two occurrences of $A$ in the augmented system differently. Therefore the bound is applicable to iterative refinement (with $E = |A|$ , $f = |b|$ ), and so we can expect iterative refinement to mitigate the effects of poor row and column scaling of $A$ . Numerical experiments show that these predictions are borne out in practice [596, 1991].

Turning to mixed precision iterative refinement, we would like to apply the analysis of §12.1, with “ $A x = b$ ” again identified with the augmented system. However, the analysis of §12.1 requires a backward error result in which only the

coefficient matrix is perturbed (see (12.1)). This causes no difficulties because from Theorem 20.4 we can deduce a normwise result (cf. Problem 7.7):

$$
\left(\left[ \begin{array}{l l} I & A \\ A ^ {T} & 0 \end{array} \right] + \varDelta\right) \left[ \begin{array}{l} \widehat {r} \\ \widehat {x} \end{array} \right] = \left[ \begin{array}{l} f \\ g \end{array} \right], \qquad \| \varDelta \| _ {2} \leq c _ {m, n} u \left\| \left[ \begin{array}{l l} I & A \\ A ^ {T} & 0 \end{array} \right] \right\| _ {2}.
$$

The theory of §12.1 then tells us that mixed precision iterative refinement will converge as long as the condition number of the augmented system matrix is not too large and that the rate of convergence depends on this condition number. How does the condition number of the augmented system relate to that of $A$ ? Consider the matrix that results from the scaling $A \gets \alpha^{-1}A$ ( $\alpha > 0$ ):

$$
C (\alpha) = \left[ \begin{array}{l l} \alpha I & A \\ A ^ {T} & 0 \end{array} \right]. \tag {20.17}
$$

Björck [118, 1967] shows that the eigenvalues of $C(\alpha)$ are

$$
\lambda (C (\alpha)) = \left\{ \begin{array}{l l} \frac {\alpha}{2} \pm \left(\frac {\alpha^ {2}}{4} + \sigma_ {i} ^ {2}\right) ^ {1 / 2}, & i = 1: n, \\ \alpha , & m - n \text {t i m e s}, \end{array} \right. \tag {20.18}
$$

where $\sigma_{i}$ , $i = 1$ : $n$ , are the singular values of $A$ , and that

$$
\sqrt {2} \kappa_ {2} (A) \leq \min  _ {\alpha} \kappa_ {2} (C (\alpha)) \leq 2 \kappa_ {2} (A), \quad \max  _ {\alpha} \kappa_ {2} (C (\alpha)) > \kappa_ {2} (A) ^ {2}, \tag {20.19}
$$

with $\min_{\alpha} \kappa_2(C(\alpha))$ being achieved for $\alpha = \sigma_n / \sqrt{2}$ (see Problem 20.7). Hence $C(\alpha)$ may be much more ill conditioned than $A$ . However, in our analysis we are at liberty to take $\min_{\alpha} \kappa_2(C(\alpha))$ as the condition number, because scaling the LS problem according to $b - Ax \gets (b - Ax) / \alpha$ does not change the computed solution or the rounding errors in any way (at least not if $\alpha$ is a power of the machine base). Therefore it is $\kappa_2(A)$ that governs the behaviour of mixed precision iterative refinement, irrespective of the size of the LS residual. As Björck [123, 1990] explains, this means that "in a sense iterative refinement is even more satisfactory for large residual least-squares problems." He goes on to explain that "When residuals to the augmented system are accumulated in precision $\beta^{-t_2}$ , $t_2 \geq 2t_1$ , this scheme gives solutions to full single-precision accuracy even though the initial solution may have no correct significant figures."

Iterative refinement can be applied with the MGS method. Björck [118, 1967] gives the details and shows that mixed precision refinement works just as well as it does for Householder's method.

# 20.6. The Seminormal Equations

When we use a QR factorization to solve an LS problem $\min_x\| b - Ax\| _2$ , the solution $x$ is determined from the equation $Rx = Q^{T}b$ (or via a similar expression involving $Q$ for the MGS method). But if we need to solve for several right-hand sides that are not all available when the QR factorization is computed, we need to store $Q$ before applying it to the right-hand sides. If $A$ is large and sparse it is

undesirable to store $Q$ , as it can be much more dense than $A$ . We can, however, rewrite the normal equations as

$$
R ^ {T} R x = A ^ {T} b,
$$

which are called the seminormal equations. The solution $x$ can be determined from these equations without the use of $Q$ . Since the cross product matrix $A^T A$ is not formed explicitly and $R$ is determined stably via a QR factorization, we might expect this approach to be more stable than the normal equations method.

Björck [122, 1987] has done a detailed error analysis of the seminormal equations (SNE) method, under the assumption that $R$ is computed by a backward stable method. His forward error bound for the SNE method is of the same form as that for the normal equations method, involving a factor $\kappa_2(A)^2$ . Thus the SNE method is not backward stable. Björck considers applying one step of fixed precision iterative refinement to the SNE method, and he calls the resulting process the corrected seminormal equations (CSNE) method:

$$
\begin{array}{l} R ^ {T} R x = A ^ {T} b \\ r = b - A x \\ R ^ {T} R w = A ^ {T} r \\ y = x + w \\ \end{array}
$$

It is important that the normal equations residual be computed as shown, as $A^T(b - Ax)$ , and not as $A^Tb - A^TAx$ . Björck derives a forward error bound for the CSNE method that is roughly of the form

$$
\frac {\| x - y \| _ {2}}{\| x \| _ {2}} \leq c _ {m, n} \left(\kappa_ {2} (A) u \cdot \kappa_ {2} (A) ^ {2} u \left(1 + \frac {\| b \| _ {2}}{\| A \| _ {2} \| x \| _ {2}}\right) + \frac {\kappa_ {2} (A) ^ {2} u \| r \| _ {2}}{\| A \| _ {2} \| x \| _ {2}}\right).
$$

Hence, if $\kappa_{2}(A)^{2}u\leq 1$ , the CSNE method has a forward error bound similar to that for a backward stable method, and the bound is actually smaller than that for the QR method if $\kappa_{2}(A)^{2}u\ll 1$ and $r$ is small. However, the CSNE method is not backward stable for all $A$ .

# 20.7. Backward Error

Although it has been known since the 1960s that a particular method for solving the LS problem, namely the Householder QR factorization method, yields a small normwise backward error (see §20.2), it was for a long time an open problem to obtain a formula for the backward error of an arbitrary approximate solution. Little progress had been made towards solving this problem until Waldén, Karlson, and Sun [1203, 1995] found an extremely elegant solution. We will denote by $\lambda_{\min}$ and $\sigma_{\min}$ the smallest eigenvalue of a symmetric matrix and the smallest singular value of a general matrix, respectively.

Theorem 20.5 (Waldén, Karlson, and Sun). Let $A \in \mathbb{R}^{m \times n}$ ( $m \geq n$ ), $b \in \mathbb{R}^m$ , $0 \neq y \in \mathbb{R}^n$ , and $r = b - Ay$ . The normwise backward error

$$
\eta_ {F} (y) := \min  \left\{\| [ \Delta A, \theta \Delta b ] \| _ {F}: \| (A + \Delta A) y - (b + \Delta b) \| _ {2} = \min  \right\} \tag {20.20}
$$

is given by

$$
\eta_ {F} (y) = \left\{ \begin{array}{c c} \frac {\| r \| _ {2}}{\| y \| _ {2}} \sqrt {\mu}, & \lambda_ {*} \geq 0, \\ \left(\frac {\| r \| _ {2} ^ {2}}{\| y \| _ {2} ^ {2}} \mu + \lambda_ {*}\right) ^ {1 / 2}, & \lambda_ {*} <   0, \end{array} \right.
$$

where

$$
\lambda_ {*} = \lambda_ {\mathrm {m i n}} \bigg (A A ^ {T} - \mu \frac {r r ^ {T}}{\| y \| _ {2} ^ {2}} \bigg), \quad \mu = \frac {\theta^ {2} \| y \| _ {2} ^ {2}}{1 + \theta^ {2} \| y \| _ {2} ^ {2}}. \qquad \square
$$

The backward error (20.20) is not a direct generalization of the usual norm-wise backward error for square linear systems, because it minimizes $\| [\varDelta A,\theta\varDelta b]\|_{F}$ instead of $\max \{\|\varDelta A\|_2/\|E\|_2, \| \varDelta b\|_2/\|f\|_2\}$ . However, the parameter $\theta$ allows us some flexibility: taking the limit $\theta \to \infty$ forces $\varDelta b=0$ , giving the case where only $A$ is perturbed.

Theorem 20.5 can be interpreted as saying that if $\lambda_{*} \geq 0$ then the backward error is the same as that given in Problem 7.8 for a consistent linear system. If $\lambda_{*} < 0$ , however, the nearest perturbed system of which $y$ is the LS solution is inconsistent. A sufficient condition for $\lambda_{*} < 0$ is $b \notin \operatorname{range}(A)$ (assuming $\mu \neq 0$ ), that is, the original system is inconsistent.

The formulae given in Theorem 20.5 are unsuitable for computation because they can suffer from catastrophic cancellation when $\lambda_{*} < 0$ . Instead, the following alternative formula derived in [1203, 1995] should be used (see Problem 20.9):

$$
\eta_ {F} (y) = \min  \left\{\phi , \sigma_ {\min } \left(\left[ A \quad \phi \left(I - r r ^ {+}\right) \right]\right) \right\}, \quad \phi = \sqrt {\mu} \frac {\| r \| _ {2}}{\| y \| _ {2}}. \tag {20.21}
$$

To illustrate Theorem 20.5, we consider an LS problem with a $25 \times 15$ Vandermonde matrix $A = (p_j^{i-1})$ , where the $p_i$ are equally spaced on $[0,1]$ , and $b = Ax$ with $x_i = i$ (giving a zero residual problem). The condition number $\kappa_2(A) = 1.47 \times 10^9$ . We solved the LS problem in MATLAB in four different ways: by using the NE with Cholesky factorization, via Householder QR factorization, and via the MGS method, using both the stable approach described in §20.3 and the unstable approach in which $Q^T b$ is formed as a matrix-vector product (denoted MGS(bad)). The results, including the norms of the residuals $r = b - A\hat{x}$ , are shown in Table 20.1. As would be expected from the analysis in this chapter, the QR and stable MGS methods produce backward stable solutions, but the NE method and the unstable MGS approach do not.

As we saw in the analysis of iterative refinement, sometimes we need to consider the augmented system with different perturbations to $A$ and $A^T$ . The next result shows that from the point of view of normwise perturbations and columnwise perturbations the lack of "symmetry" in the perturbations has little effect on the backward error of $y$ .

Lemma 20.6 (Kielbasinski and Schwetlick). Let $A \in \mathbb{R}^{m \times n}$ ( $m \geq n$ ) and consider the perturbed augmented system

$$
\left[ \begin{array}{c c} I & A + \varDelta A _ {1} \\ (A + \varDelta A _ {2}) ^ {T} & 0 \end{array} \right] \left[ \begin{array}{c} s \\ y \end{array} \right] = \left[ \begin{array}{c} b \\ 0 \end{array} \right].
$$

Table 20.1. LS backward errors and residual for Vandermonde system.   

<table><tr><td></td><td>ηF||[A,b]∥F(θ=1)</td><td>ηF∥A∥F(θ=∞)</td><td>r2</td></tr><tr><td>NE</td><td>3.1 × 10-11</td><td>8.6 × 10-10</td><td>2.4 × 10-7</td></tr><tr><td>QR</td><td>4.7 × 10-18</td><td>1.3 × 10-16</td><td>3.4 × 10-14</td></tr><tr><td>MGS</td><td>5.6 × 10-18</td><td>1.6 × 10-16</td><td>4.0 × 10-14</td></tr><tr><td>MGS(bad)</td><td>2.0 × 10-11</td><td>5.5 × 10-10</td><td>4.4 × 10-7</td></tr></table>

There is a vector $\widehat{s}$ and a perturbation $\Delta A$ with

$$
\Delta A = G _ {1} \Delta A _ {1} + G _ {2} \Delta A _ {2}, \quad G _ {1} ^ {T} = G _ {1} = G _ {1} ^ {2}, \quad G _ {1} + G _ {2} = I, \tag {20.22}
$$

such that

$$
\left[ \begin{array}{c c} I & A + \varDelta A \\ (A + \varDelta A) ^ {T} & 0 \end{array} \right] \left[ \begin{array}{c} \widehat {s} \\ y \end{array} \right] = \left[ \begin{array}{c} b \\ 0 \end{array} \right],
$$

that is, $y$ solves the LS problem $\min_x\| (A + \Delta A)x - b\| _2$

Proof. If $s = b - (A + \Delta A_1)y = 0$ we take $\Delta A = \Delta A_1$ . Otherwise, we set

$$
\Delta A := P \Delta A _ {2} + (I - P) \Delta A _ {1} =: \Delta A _ {1} + P H,
$$

where $P = s s^T / s^T s$ and $H = \Delta A_2 - \Delta A_1$ . We have

$$
\widehat {s} := b - (A + \Delta A) y = b - (A + \Delta A _ {1}) y - P H y = \beta s,
$$

where $\beta = 1 - s^T H y / s^T s$ . Then

$$
\begin{array}{l} (A + \Delta A) ^ {T} \hat {s} = (A + \Delta A _ {2} + (P - I) H) ^ {T} \beta s \\ = \beta \left(\left(A + \Delta A _ {2}\right) ^ {T} s + H ^ {T} (P - I) s\right) = 0. \quad \square \\ \end{array}
$$

Note that (20.22) implies a bound stronger than just $\| \varDelta A\| _2\leq \| \varDelta A_1\| _2+$ $\| \varDelta A_2\| _2$

$$
\| \varDelta A \| _ {p} \leq \big (\| \varDelta A _ {1} \| _ {p} ^ {2} + \| \varDelta A _ {2} \| _ {p} ^ {2} \big) ^ {1 / 2}, \qquad p = 2, F.
$$

Turning to componentwise backward error, the simplest approach is to apply the componentwise backward error $\omega_{E,f}(y)$ to the augmented system (20.3), setting

$$
E = \left[ \begin{array}{l l} 0 & E _ {A} \\ E _ {A} ^ {T} & 0 \end{array} \right]
$$

so as not to perturb the diagonal blocks $I$ and 0 of the augmented system coefficient matrix. However, this approach allows $A$ and $A^T$ to undergo different perturbations $\Delta A_1$ and $\Delta A_2$ with $\Delta A_1 \neq \Delta A_2^T$ and thus does not give a true backward error, and Lemma 20.6 is of no help. This problem can be overcome by using a structured componentwise backward error to force symmetry of the perturbations; see Higham and Higham [574, 1992] for details. One problem remains: as far as the backward error of $y$ is concerned, the vector $r$ in the augmented system

is a vector of free parameters, so to obtain the true componentwise backward error we have to minimize the structure-preserving componentwise backward error over all $r$ . This is a nonlinear optimization problem to which no closed-form solution is known. Experiments show that when $y$ is a computed LS solution, $r = b - Ay$ is often a good approximation to the minimizing $r$ [574, 1992], [596, 1991].

# 20.8. Weighted Least Squares Problems

In many applications of the LS problem the rows of $A$ have widely varying norms (with corresponding variation in the size of the elements of $b$ ), typically because in the underlying model some observations have been given greater weight than others. Such weighted LS problems also arise when the method of weighting is used to approximate the solution to the linearly constrained LS problem; see §20.9.2.

As we saw in §19.4, Householder QR factorization needs to be implemented with column pivoting together with row pivoting or row sorting, and with the correct choice of sign in the Householder vectors, if a row-wise backward stable QR factorization is to be obtained. The following result describes the row-wise stability of Householder QR factorization for solving the LS problem.

Theorem 20.7 (Powell and Reid; Cox and Higham). Suppose the LS problem $\min_x\| b - Ax\| _2$ , where $A\in \mathbb{R}^{m\times n}$ is of full rank $n$ , is solved using Householder QR factorization with column pivoting, with the choice of sign (19.1). Then the computed solution $\widehat{x}$ is the exact solution to

$$
\min _ {x} \| (b + \Delta b) - (A + \Delta A) x \| _ {2},
$$

where the perturbations satisfy

$$
| \varDelta a _ {i j} | \leq j ^ {2} \tilde {\gamma} _ {m} \alpha_ {i} \max  _ {s} | a _ {i s} |, \qquad | \varDelta b _ {i} | \leq n ^ {2} \tilde {\gamma} _ {m} \beta_ {i} \max  (\phi \max  _ {s} | a _ {i s} |, | b _ {i} |),
$$

where

$$
\begin{array}{l} \alpha_ {i} = \frac {\operatorname* {m a x} _ {j , k} | a _ {i j} ^ {(k)} |}{\operatorname* {m a x} _ {j} | a _ {i j} |}, \quad \beta_ {i} = \frac {\operatorname* {m a x} \big (\phi \operatorname* {m a x} _ {j , k} | a _ {i j} ^ {(k)} | , | b _ {i} ^ {(k)} | \big)}{\operatorname* {m a x} \big (\phi \operatorname* {m a x} _ {j} | a _ {i j} | , | b _ {i} | \big)}, \\ \phi = \max  _ {k} \frac {\| b ^ {(k)} (k : m) \| _ {2}}{\| a _ {k} ^ {(k)} (k : m) \| _ {2}}. \quad \square \\ \end{array}
$$

The theorem shows that row-wise backward stability holds if $\max_i\{\alpha_i,\beta_i\}$ and $\phi$ are of order 1. With row pivoting or row sorting, $\max_i\{\alpha_i,\beta_i\} \leq \sqrt{m} (1 + \sqrt{2})^{n - 1}$ . The scalar $\phi$ is easily seen to be independent of the row ordering and so is beyond our control.

No formula for the row-wise backward error of an approximate LS solution is known (see Problem 20.13).

For a treatment of the weighted LS problem from a forward error perspective see Hough and Vavasis [642, 1997].

# 20.9. The Equality Constrained Least Squares Problem

We now consider the LS problem with linear equality constraints

$$
\text {L S E}: \quad \min  _ {B x = d} \| b - A x \| _ {2}, \tag {20.23}
$$

where $A \in \mathbb{R}^{m \times n}$ and $B \in \mathbb{R}^{p \times n}$ , with $m + p \geq n \geq p$ . Note that the condition $m \geq n - p$ ensures that the LSE problem is overdetermined. We will assume that

$$
\operatorname {r a n k} (B) = p, \quad \operatorname {n u l l} (A) \cap \operatorname {n u l l} (B) = \{0 \}. \tag {20.24}
$$

The assumption that $B$ is of full rank ensures that the system $Bx = d$ is consistent and hence that the LSE problem has a solution. The second condition in (20.24), which is equivalent to the condition that the matrix $[A^T, B^T]^T$ has full rank $n$ , then guarantees that there is a unique solution.

The LSE problem arises in various applications, including the analysis of large-scale structures [66, 1988], [669, 1997], and the solution of the inequality constrained least squares problem [775, 1995, Chap. 23].

# 20.9.1. Perturbation Theory

We begin with a perturbation result for the LSE problem.

Theorem 20.8 (Eldén; Cox and Higham). Consider the LSE problem as defined above and a perturbed problem defined by $A + \Delta A$ , $b + \Delta b$ , $B + \Delta B$ , and $d + \Delta d$ with solution $y$ , where

$$
\max  \left\{\frac {\| \varDelta A \| _ {F}}{\| A \| _ {F}}, \frac {\| \varDelta b \| _ {2}}{\| b \| _ {2}}, \frac {\| \varDelta B \| _ {F}}{\| B \| _ {F}}, \frac {\| \varDelta d \| _ {2}}{\| d \| _ {2}} \right\} \leq \epsilon .
$$

Assume that the condition (20.24) is satisfied by both problems. Then

$$
\begin{array}{l} \frac {\| \Delta x \| _ {2}}{\| x \| _ {2}} \leq \epsilon \left[ \kappa_ {A} (B) \left(\frac {\| d \| _ {2}}{\| B \| _ {F} \| x \| _ {2}} + 1\right) + \kappa_ {B} (A) \left(\frac {\| b \| _ {2}}{\| A \| _ {F} \| x \| _ {2}} + 1\right) \right. \\ \left. + \kappa_ {B} (A) ^ {2} \left(\frac {\| B \| _ {F}}{\| A \| _ {F}} \| A B _ {A} ^ {+} \| _ {2} + 1\right) \frac {\| r \| _ {2}}{\| A \| _ {F} \| x \| _ {2}} \right] + O (\epsilon^ {2}), \tag {20.25} \\ \end{array}
$$

where

$$
\kappa_ {B} (A) = \| A \| _ {F} \| (A P) ^ {+} \| _ {2}, \quad \kappa_ {A} (B) = \| B \| _ {F} \| B _ {A} ^ {+} \| _ {2},
$$

and

$$
P = I - B ^ {+} B, \quad B _ {A} ^ {+} = (I - (A P) ^ {+} A) B ^ {+}. \quad \square
$$

As a check, we can recover the perturbation bound (20.1) to first order by setting $B = 0$ and $d = 0$ (see Problem 20.11).

The bound (20.25) shows that if the residual $r$ is small or zero, the sensitivity is governed by $\kappa_A(B)$ and $\kappa_B(A)$ , otherwise by $\kappa_A(B)$ and $\kappa_B(A)^2 \| B \|_F \| AB_A^+ \|_2 / \| A \|_F$ . A sufficient condition for the LSE problem to be well conditioned is that $B$ and $AP$ are both well conditioned.

An analogous bound can be derived for $\Delta r$ that has no direct dependence on $\kappa_A(B)$ and in which $\kappa_B(A)$ appears only to the first power.

# 20.9.2. Methods

We describe three classes of methods for solving the LSE problem. The method of weighting is based on the observation that the solution to the LSE problem (20.23) is the limit of the solution of the unconstrained problem

$$
\min  \left\| \left[ \begin{array}{l} A \\ \mu B \end{array} \right] x - \left[ \begin{array}{l} b \\ \mu d \end{array} \right] \right\| _ {2} \tag {20.26}
$$

as the weight $\mu$ tends to infinity. Therefore the LSE solution can be approximated by solving (20.26) for a suitably large weight. For insightful analysis of how to choose the weight see Stewart [1080, 1998, pp. 317-320]. Van Loan [1180, 1985] describes an algorithm that solves (20.26) for a single weight and uses a refinement procedure to approximate the required limit. The algorithm is analysed further by Barlow and Vemulapati [70, 1988], [75, 1992].

Two further classes of methods for solving the LSE problem are null space methods and elimination methods, with each class having more than one variation. A basic difference between the classes is that the latter QR factorizes the constraint matrix $B$ while the former QR factorizes $B^T$ .

We first describe the null space methods, so-called because they employ an orthogonal basis for the null space of the constraint matrix. We begin with a version based on the generalized QR factorization. The generalized QR factorization was introduced by Hammarling [543, 1987] and Paige [912, 1990] and further analysed by Anderson, Bai, and Dongarra [21, 1992] and is of interest in its own right.

Theorem 20.9 (generalized QR factorization). Let $A \in \mathbb{R}^{m \times n}$ and $B \in \mathbb{R}^{p \times n}$ with $m + p \geq n \geq p$ . There are orthogonal matrices $Q \in \mathbb{R}^{n \times n}$ and $U \in \mathbb{R}^{m \times m}$ such that

$$
U ^ {T} A Q = \begin{array}{c} m - n + p \\ n - p \end{array} \left[ \begin{array}{c c} p & n - p \\ L _ {1 1} & 0 \\ L _ {2 1} & L _ {2 2} \end{array} \right], \quad B Q = p \left[ \begin{array}{c c} p & n - p \\ S & 0 \end{array} \right], \tag {20.27}
$$

where $L_{22}$ and $S$ are lower triangular. More precisely, we have

$$
U ^ {T} A Q = \left\{ \begin{array}{l l} n & \text {i f} m \geq n, \\ \left[ \begin{array}{c c} 0 & \\ n & L \end{array} \right] & \\ n - m & m \\ m [ X & L ] & \text {i f} m <   n, \end{array} \right. \tag {20.28}
$$

where $L$ is lower triangular. The assumptions (20.24) are equivalent to $S$ and $L_{22}$ being nonsingular.

Proof. Let

$$
Q ^ {T} B ^ {T} = \left[ \begin{array}{c} S ^ {T} \\ 0 \end{array} \right]
$$

be a QR factorization of $B^T$ . We can determine an orthogonal $U$ so that $U^T(AQ)$ has the form (20.28), where $L$ is lower triangular (for example, we can construct

$U$ as a product of suitably chosen Householder transformations). Clearly, $B$ has full rank if and only if $S$ is nonsingular. Partition $Q = [Q_{1} Q_{2}]$ conformably with $[S 0]$ and assume $S$ is nonsingular. Then, clearly, $\mathrm{null}(B) = \mathrm{range}(Q_{2})$ . We can write

$$
A \left[ \begin{array}{c c} Q _ {1} & Q _ {2} \end{array} \right] = \left[ \begin{array}{c c} U _ {1} & U _ {2} \end{array} \right] \left[ \begin{array}{c c} L _ {1 1} & 0 \\ L _ {2 1} & L _ {2 2} \end{array} \right],
$$

so that $AQ_{2} = U_{2}L_{22}$ . It follows that $\mathrm{null}(A) \cap \mathrm{null}(B) = \{0\}$ is equivalent to $L_{22}$ being nonsingular.

While (20.28) is needed to define the generalized QR factorization precisely, the partitioning of $U^T A Q$ in (20.27) enables us to explain the application to the LSE problem without treating the cases $m \geq n$ and $m < n$ separately.

Using (20.27) the constraint $Bx = d$ may be written

$$
S y _ {1} = \left[ \begin{array}{c c} S & 0 \end{array} \right] \left[ \begin{array}{c} y _ {1} \\ y _ {2} \end{array} \right] = d, \qquad y = Q ^ {T} x.
$$

Hence the constraint determines $y_1 \in \mathbb{R}^p$ as the solution of the triangular system $S y_1 = d$ and leaves $y_2 \in \mathbb{R}^{n - p}$ arbitrary. Since

$$
\left\| b - A x \right\| _ {2} = \left\| c - U ^ {T} A Q y \right\| _ {2}, \quad c = U ^ {T} b,
$$

we see that we have to find

$$
\operatorname * {m i n} _ {y _ {2}} \left\| \left[ \begin{array}{c} c _ {1} \\ c _ {2} \end{array} \right] - \left[ \begin{array}{c c} L _ {1 1} & 0 \\ L _ {2 1} & L _ {2 2} \end{array} \right] \left[ \begin{array}{c} y _ {1} \\ y _ {2} \end{array} \right] \right\| _ {2} = \operatorname * {m i n} _ {y _ {2}} \left\| \left[ \begin{array}{c} c _ {1} - L _ {1 1} y _ {1} \\ (c _ {2} - L _ {2 1} y _ {1}) - L _ {2 2} y _ {2} \end{array} \right] \right\| _ {2}.
$$

Therefore $y_{2}$ is the solution to the triangular system $L_{22}y_{2} = c_{2} - L_{21}y_{1}$ . The solution $x$ is recovered from $x = Qy$ . We refer to this solution process as the GQR method. It is the method used by the LAPACK driver routine xGGLSE [20, 1999]. The operation count for the method is a complicated function of $m$ , $n$ , and $p$ ; for $m \gg n \gg p$ it is approximately $2mn^{2}$ flops.

The stability of the GQR method is summarized by the following result.

Theorem 20.10 (Cox and Higham). Suppose the LSE problem (20.23) is solved using the GQR method, where the generalized QR factorization is computed using Householder transformations, and let the assumptions (20.24) be satisfied. Let $\hat{x}$ denote the computed solution.

(a) $\widehat{x} = \overline{x} +\varDelta \overline{x}$ , where $\overline{x}$ solves

$$
\min  \left\{\| b + \Delta b - (A + \Delta A) x \| _ {2}: (B + \Delta B) x = d \right\},
$$

where

$$
\| \Delta \bar {x} \| _ {2} \leq \tilde {\gamma} _ {n p} \| \bar {x} \| _ {2}, \quad \| \Delta b \| _ {2} \leq \tilde {\gamma} _ {m n} \| b \| _ {2},
$$

$$
\| \Delta A \| _ {F} \leq \tilde {\gamma} _ {m n} \| A \| _ {F}, \quad \| \Delta B \| _ {F} \leq \tilde {\gamma} _ {n p} \| B \| _ {F}.
$$

(b) $\widehat{\pmb{x}}$ solves

$$
\min  \left\{\| b + \Delta b - (A + \Delta A) x \| _ {2}: (B + \Delta B) x = d + \Delta d \right\},
$$

where

$$
\begin{array}{l} \| \Delta b \| _ {2} \leq \tilde {\gamma} _ {m n} \| b \| _ {2} + \tilde {\gamma} _ {n p} \| A \| _ {F} \| \widehat {x} \| _ {2}, \quad \| \Delta A \| _ {F} \leq \tilde {\gamma} _ {m n} \| A \| _ {F}, \\ \| \Delta B \| _ {F} \leq \tilde {\gamma} _ {n p} \| B \| _ {F}, \quad \| \Delta d \| _ {2} \leq \tilde {\gamma} _ {n p} \| B \| _ {F} \| \widehat {x} \| _ {2}. \\ \end{array}
$$

The first part of the theorem says that $\widehat{x}$ is very close to the exact solution of a slightly different LSE problem; this is a mixed form of stability. The second part says that $\widehat{x}$ exactly solves a perturbed LSE problem in which the perturbations to $A$ and $B$ are tiny but those to $b$ and $d$ can be relatively large when $x$ is large-normed. It is an open problem whether genuine backward stability holds. In any case, the stability of the GQR method can be regarded as quite satisfactory.

The GQR method can be modified to reduce the amount of computation and the modified versions have the same stability properties [276, 1999].

The final class of methods for solving the LSE problem is based on elimination. First, we use QR factorization with column pivoting to factorize

$$
B \Pi = Q \left[ \begin{array}{l l} R _ {1} & R _ {2} \end{array} \right], \quad R _ {1} \in \mathbb {R} ^ {p \times p} \text {u p p e r t r i a n g u l a r , n o n s i n g u l a r .} \tag {20.29}
$$

Note that column pivoting is essential here in order to obtain a nonsingular $R_{1}$ . Then, partitioning $\Pi^T x = [\widetilde{x}_1^T, \widetilde{x}_2^T]^T$ , $\widetilde{x}_1 \in \mathbb{R}^p$ and substituting the factorization (20.29) into the constraints yields

$$
R _ {1} \widetilde {\boldsymbol {x}} _ {1} = Q ^ {T} d - R _ {2} \widetilde {\boldsymbol {x}} _ {2}.
$$

By solving for $\widetilde{x}_1$ and partitioning $A\Pi = [\widetilde{A}_1, \widetilde{A}_2]$ , $\widetilde{A}_1 \in \mathbb{R}^{m \times p}$ we reduce the LSE problem to the unconstrained problem

$$
\operatorname * {m i n} _ {\widetilde {x} _ {2}} \left\| (\widetilde {A} _ {2} - \widetilde {A} _ {1} R _ {1} ^ {- 1} R _ {2}) \widetilde {x} _ {2} - (b - \widetilde {A} _ {1} R _ {1} ^ {- 1} Q ^ {T} d) \right\| _ {2}.
$$

Solving this unconstrained problem by QR factorization completes the elimination method as originally presented by Björck and Golub [130, 1967] (see also Lawson and Hanson [775, 1995, Chap. 21]). It is instructive to think of the method in terms of transformations on the matrix “ $B$ -over- $A$ :”

$$
\begin{array}{l} p \quad n - p \\ \left[ \begin{array}{c} B \\ A \end{array} \right] = \mathbf {\Pi} _ {m} ^ {p} \left[ \begin{array}{c c} B _ {1} & B _ {2} \\ A _ {1} & A _ {2} \end{array} \right] \to \left[ \begin{array}{c c} R _ {1} & R _ {2} \\ \widetilde {A} _ {1} & \widetilde {A} _ {2} \end{array} \right] \\ \rightarrow \left[\begin{array}{c c}R _ {1}&R _ {2}\\0&\widetilde {A} _ {2} - \widetilde {A} _ {1} R _ {1} ^ {- 1} R _ {2}\end{array}\right]\rightarrow \left[\begin{array}{c c}R _ {1}&R _ {2}\\0&R _ {3}\\0&0\end{array}\right], \tag {20.30} \\ \end{array}
$$

where $R_3 \in \mathbb{R}^{(n - p) \times (n - p)}$ is upper triangular. Note that the penultimate transformation is simply the annihilation of $\widetilde{A}_1$ by Gaussian elimination. The $B$ -over- $A$ matrix also arises in the method of weighting; see (20.26).

Another elimination method that also produces the factorization (20.30) was derived by Cox and Higham [278, 1999] and independently by Reid [981, 2000].

A row-wise backward error result is available for both elimination methods [278, 1999]. The computed solution exactly solves a perturbed LSE problem for which row-wise backward error bounds involving row-wise growth factors hold for both the objective function and the constraints. If row sorting or row pivoting is used (separately on $A$ and $B$ ) then the growth factors have similar behaviour to the $\alpha_{i}$ in Theorem 19.6.

# 20.10. Proof of Wedin's Theorem

In this section we give a proof of Theorem 20.1. We define $P_A \coloneqq AA^+$ , the orthogonal projection onto range(A).

Lemma 20.11. Let $A, B \in \mathbb{R}^{m \times n}$ . If $\operatorname{rank}(A) = \operatorname{rank}(B)$ and $\eta = \| A^+ \|_2 \| A - B \|_2 < 1$ , then

$$
\| B ^ {+} \| _ {2} \leq \frac {1}{1 - \eta} \| A ^ {+} \| _ {2}.
$$

Proof. Let $r = \operatorname{rank}(A)$ . A standard result on the perturbation of singular values gives

$$
\sigma_ {r} (B) \geq \sigma_ {r} (A) - \| A - B \| _ {2},
$$

that is,

$$
\left\| B ^ {+} \right\| _ {2} ^ {- 1} \geq \left\| A ^ {+} \right\| _ {2} ^ {- 1} - \left\| A - B \right\| _ {2} > 0,
$$

which gives the result on rearranging.

□

Lemma 20.12. Let $A, B \in \mathbb{R}^{m \times n}$ . If $\operatorname{rank}(A) = \operatorname{rank}(B)$ then

$$
\left\| P _ {A} (I - P _ {B}) \right\| _ {2} = \left\| P _ {B} (I - P _ {A}) \right\| _ {2} \leq \left\| A - B \right\| _ {2} \min \{\left\| A ^ {+} \right\| _ {2}, \left\| B ^ {+} \right\| _ {2} \}.
$$

Proof. We have

$$
\begin{array}{l} \| P _ {B} (I - P _ {A}) \| _ {2} = \| \left(P _ {B} (I - P _ {A})\right) ^ {T} \| _ {2} \\ = \left\| \left(I - P _ {A}\right) P _ {B} \right\| _ {2} \\ = \| (I - A A ^ {+}) B B ^ {+} \| _ {2} \\ = \| \left(I - A A ^ {+}\right) (A + (B - A)) B ^ {+} \| _ {2} \\ = \| (I - A A ^ {+}) (B - A) B ^ {+} \| _ {2} \\ \leq \| A - B \| _ {2} \| B ^ {+} \| _ {2}. \\ \end{array}
$$

The result then follows from the (nontrivial) equality $\| P_A(I - P_B)\| _2 = \| P_B(I - P_A)\| _2$ ; see, for example, Stewart [1067, 1977, Thm. 2.3] or Stewart and Sun [1083, 1990, Lem. 3.3.5], where proofs that use the CS decomposition are given. $\square$

Proof of Theorem 20.1. Let $B\coloneqq A + \Delta A$ . We have, with $r = b - Ax$

$$
\begin{array}{l} y - x = B ^ {+} (b + \Delta b) - x = B ^ {+} (r + A x + \Delta b) - x \\ = B ^ {+} (r + B x - \Delta A x + \Delta b) - x \\ = B ^ {+} (r - \Delta A x + \Delta b) - (I - B ^ {+} B) x \\ = B ^ {+} (r - \Delta A x + \Delta b), \tag {20.31} \\ \end{array}
$$

since $B$ has full rank. Now

$$
B ^ {+} r = B ^ {+} \left(B B ^ {+}\right) r = B ^ {+} P _ {B} r = B ^ {+} P _ {B} \left(I - P _ {A}\right) r. \tag {20.32}
$$

Applying Lemmas 20.11 and 20.12, we obtain

$$
\begin{array}{l} \| B ^ {+} r \| _ {2} \leq \| B ^ {+} \| _ {2} (\| B - A \| _ {2} \| A ^ {+} \| _ {2}) \| r \| _ {2} \\ \leq \frac {\| A ^ {+} \| _ {2}}{1 - \| A ^ {+} \| _ {2} \| \Delta A \| _ {2}} \| \Delta A \| _ {2} \| A ^ {+} \| _ {2} \| r \| _ {2} \\ = \frac {\kappa_ {2} (A) ^ {2} \epsilon}{1 - \kappa_ {2} (A) \epsilon} \frac {\| r \| _ {2}}{\| A \| _ {2}}. \tag {20.33} \\ \end{array}
$$

Similarly,

$$
\begin{array}{l} \| B ^ {+} (- \Delta A x + \Delta b) \| _ {2} \leq \frac {\| A ^ {+} \| _ {2}}{1 - \kappa_ {2} (A) \epsilon} \epsilon (\| A \| _ {2} \| x \| _ {2} + \| b \| _ {2}) \\ = \frac {\kappa_ {2} (A) \epsilon}{1 - \kappa_ {2} (A) \epsilon} \left(1 + \frac {\| b \| _ {2}}{\| A \| _ {2} \| x \| _ {2}}\right) \| x \| _ {2} \\ \leq \frac {\kappa_ {2} (A) \epsilon}{1 - \kappa_ {2} (A) \epsilon} \left(2 + \frac {\| r \| _ {2}}{\| A \| _ {2} \| x \| _ {2}}\right) \| x \| _ {2}. \tag {20.34} \\ \end{array}
$$

The bound for $\| x - y\| _2 / \| x\| _2$ is obtained by using inequalities (20.33) and (20.34) in (20.31).

Turning to the residual, using (20.31) we find that

$$
\begin{array}{l} s - r = \Delta b + B (x - y) - \Delta A x \\ = \Delta b - B B ^ {+} (r - \Delta A x + \Delta b) - \Delta A x \\ = (I - B B ^ {+}) (\Delta b - \Delta A x) - B B ^ {+} r. \\ \end{array}
$$

Since $\| I - BB^{+}\|_{2} = \min \{1,m - n\}$

$$
\| r - s \| _ {2} \leq \| \Delta b \| _ {2} + \| \Delta A x \| _ {2} + \| B B ^ {+} r \| _ {2} \leq \epsilon (\| b \| _ {2} + \| A \| _ {2} \| x \| _ {2}) + \| B B ^ {+} r \| _ {2}.
$$

Using (20.32), Lemma 20.12, and $\| BB^{+}\|_{2} = 1$ , we obtain

$$
\| B B ^ {+} r \| _ {2} = \| B B ^ {+} P _ {B} (I - P _ {A}) r \| _ {2} \leq \| \Delta A \| _ {2} \| A ^ {+} \| _ {2} \| r \| _ {2} \leq \kappa_ {2} (A) \epsilon \| r \| _ {2}.
$$

Hence

$$
\frac {\| r - s \| _ {2}}{\| b \| _ {2}} \leq \epsilon \left(1 + \frac {\| A \| _ {2} \| x \| _ {2}}{\| b \| _ {2}} + \kappa_ {2} (A) \frac {\| r \| _ {2}}{\| b \| _ {2}}\right) \leq \epsilon (1 + 2 \kappa_ {2} (A)).
$$

For the attainability, see Wedin [1211, 1973, §6].

Note that, as the proof has shown, Wedin's theorem actually holds without any restriction on $m$ and $n$ , provided we define $x = A^{+}b$ and $y = (A + \Delta A)^{+}(b + \Delta b)$ when $m < n$ (in which case $r = 0$ ). We consider underdetermined systems in detail in the next chapter. The original version of Wedin's theorem also requires only $\operatorname{rank}(A) = \operatorname{rank}(A + \Delta A)$ and not that $A$ have full rank.

# 20.11. Notes and References

The most comprehensive and up-to-date treatment of the LS problem is the book by Björck [128, 1996], which is an updated and expanded version of [124, 1990]. It treats many aspects not considered here, including rank-deficient and modified problems. An early book devoted to numerical aspects of the LS problem was written by Lawson and Hanson [775, 1995] (originally published in 1974), who, together with Stewart [1065, 1973], were the first to present error analysis for the LS problem in textbook form.

The history of the LS problem is described in the statistically oriented book by Farebrother [403, 1988].

The pseudo-inverse $A^{+}$ underlies the theory of the LS problem, since the LS solution can be expressed as $x = A^{+}b$ . An excellent reference for perturbation theory of the pseudo-inverse is Stewart and Sun [1083, 1990, §3.3]. The literature on pseudo-inverses is vast, as evidenced by the annotated bibliography of Nashed and Rall [879, 1976], which contains 1,776 references published up to 1976.

Normwise perturbation theory for the LS problem was developed by various authors in the 1960s and 1970s. The earliest analysis was by Golub and Wilkinson [505, 1966], who gave a first-order bound and were the first to recognize the potential $\kappa_{2}(A)^{2}$ sensitivity. A nonasymptotic perturbation bound was given by Björck [119, 1967], who worked from the augmented system.

An early set of numerical experiments on the Householder, Gram-Schmidt, and normal equations methods for solving the LS problem was presented by Jordan [679, 1968]; this paper illustrates the incomplete understanding of perturbation theory and error analysis for the LS problem at that time.

van der Sluis [1178, 1975] presents a geometric approach to LS perturbation theory and gives lower bounds for the effect of worst-case perturbations. Golub and Van Loan [509, 1996, Thm. 5.3.1] give a first-order analogue of Theorem 20.1 expressed in terms of the angle $\theta$ between $b$ and $\mathrm{range}(A)$ instead of the residual $r$ .

Wei [1213, 1990] gives a normwise perturbation result for the LS problem with a rank-deficient $A$ that allows $\operatorname{rank}(A + \Delta A) > \operatorname{rank}(A)$ .

Componentwise perturbation bounds of the form in Theorem 20.2 were first derived by Björck in 1988 and variations have been given by Arioli, Duff, and de Rijk [31, 1989], Björck [125, 1991], and Higham [590, 1990].

Higham [590, 1990] examined the famous test problem from Longley [796, 1967]—a regression problem which has a notoriously ill-conditioned $16 \times 7$ coefficient matrix with $\kappa_{2}(A) \approx 5 \times 10^{9}$ . The inequality (20.8) was found to give tight bounds for the effect of random componentwise relative perturbations of the problem generated in experiments of Beaton, Rubin, and Barone [97, 1976]. Thus

componentwise perturbation bounds are potentially useful in regression analysis as an alternative to the existing statistically based techniques.

The tools required to prove Theorem 20.3 are developed in Wilkinson's book *The Algebraic Eigenvalue Problem* [1233, 1965]. Normwise (rather than columnwise) results of this form were derived informally by Golub and Wilkinson (assuming the use of extended precision inner products) [505, 1966], stated by Wilkinson [1234, 1965, p. 93] and Stewart [1065, 1973], and proved by Lawson and Hanson [775, 1995, Chap. 16].

The idea of using QR factorization to solve the LS problem was mentioned in passing by Householder [643, 1958]. Golub [502, 1965] worked out the details, using Householder QR factorization, and this method is sometimes called "Golub's method". In the same paper, Golub suggested the form of iterative refinement described at the start of §20.5 (which is implemented in a procedure by Businger and Golub [186, 1965]), and showed how to use QR factorization to solve the LSE problem (20.23).

Higham and Stewart [623, 1987] compare the normal equations method with the QR factorization method, with emphasis on aspects relevant to regression problems in statistics.

Foster [433, 1991] proposes a class of methods for solving the LS problem that are intermediate between the normal equations method and the MGS method, and that can be viewed as block MGS algorithms.

The most general analysis of QR factorization methods for solving the LS and related problems is by Björck and Paige [132, 1994], who consider an augmented system with an arbitrary right-hand side (see Problem 21.1) and prove a number of subtle stability results.

Error analysis for solution of the LS problem by the classical Gram-Schmidt method with reorthogonalization is given by Abdelmalek [2, 1971], who obtains a forward error bound as good as that for a backward stable method.

It was Björck [118, 1967] who first recognized that iterative refinement should be applied to the augmented system for best results, and he gave a detailed rounding error analysis for the use of a QR factorization computed by the Householder or MGS methods. Björck and Golub [130, 1967] show how to compute and refine the solution to the LSE problem using Householder transformations, while Björck [120, 1968] gives a similar approach based on the Gram-Schmidt method. In [121, 1978], Björck dispels some misconceptions of statisticians about (mixed precision) iterative refinement for the LS problem; he discusses standard refinement together with two versions of refinement based on the seminormal equations.

Theorem 20.4 and the following analysis are from Higham [596, 1991].

Arioli, Duff, and de Rijk [31, 1989] investigate the application of fixed precision iterative refinement to large, sparse LS problems, taking the basic solver to be the block $\mathbf{LDL}^{\mathrm{T}}$ factorization code MA27 [364, 1982] from the Harwell Subroutine Library (applied to the augmented system); in particular, they use scaling of the form (20.17). Björck [126, 1992] determines, via an error analysis for solution of the augmented system by block $\mathbf{LDL}^{\mathrm{T}}$ factorization, a choice of $\alpha$ in (20.17) that minimizes a bound on the forward error.

The idea of implementing iterative refinement with a precision that increases on each iteration (see the Notes and References to Chapter 12) can be applied to

the LS problem; see Gluchowska and Smoktunowicz [492, 1990].

The use of the seminormal equations was first suggested by Kahan, in the context of iterative refinement, as explained by Golub and Wilkinson [505, 1966].

Stewart [1069, 1977] discusses the problem of finding the normwise backward error for the LS problem and offers some backward perturbations that are candidates for being of minimal norm. The problem is also discussed by Higham [590, 1990]. Componentwise backward error for the LS problem has been investigated by Arioli, Duff, and de Rijk [31, 1989], Björck [125, 1991], and Higham [590, 1990].

As noted by Gu [527, 1998], the formula (20.21) has the disadvantage that the matrix $[A\phi(I - rr^{+})]$ has badly scaled columns when $\phi$ is large, which can cause standard methods for computing the SVD to return an inaccurate computed smallest singular value. However, SVD methods developed in [323, 1999], [614, 2000] do not suffer from this difficulty as they are insensitive to the column scaling. The formula (20.21) requires computation of the SVD of an $m \times (n + m)$ matrix, which can be prohibitively expensive for large problems. Karlson and Waldén [713, 1997] derive upper and lower bounds for the quantity $\eta_{F}(y)|_{\theta = \infty}$ in which only $A$ is perturbed. Their bounds can be computed in $O(mn)$ operations but the bounds can differ by an arbitrary factor. Gu [527, 1998] derives an approximation to $\eta_{F}(y)|_{\theta = \infty}$ that differs from it by a factor less than 2 and can be computed in $O(mn^{2})$ operations. For large, sparse $A$ , Malyshev and Sadkane [813, 2002] show how to use Lanczos bidiagonalization to compute an upper bound for $\eta_{F}(y)|_{\theta = \infty}$ .

Theorem 20.5 has been extended to the multiple right-hand side LS problem by Sun [1107, 1996]. In [1108, 1997], Sun shows that adding the requirement in (20.20) that $y$ is the solution of minimum 2-norm does not change the backward error if $y$ and $b$ are both nonzero (a result that is, of course, immediate if $A + \Delta A$ has full rank at the minimum).

Lemma 20.6 is from a book by Kielbasiński and Schwetlick, which has been published in German [734, 1988] and Polish [735, 1992] editions, but not in English. The lemma is their Lemma 8.2.11, and can be shown to be equivalent to a result of Stewart [1067, 1977, Thm. 5.3].

Other methods for solving the LS problem not considered in this chapter include those of Peters and Wilkinson [936, 1970], Cline [242, 1973], and Plemmons [944, 1974], all of which begin by computing an LU factorization of the rectangular matrix $A$ . Error bounds for these methods can be derived using results from this chapter and Chapters 9 and 19.

A result similar to Theorem 20.7 was originally proved under some additional assumptions by Powell and Reid [951, 1969]. The result as stated is proved by Cox and Higham [278, 1999, Thm. 4.1], and originally appeared in a slightly weaker form in [275, 1998].

Theorem 20.8 is from Cox and Higham [276, 1999] and is essentially the same perturbation result as that obtained by Eldén [387, 1980], differing only in the assumptions on the perturbations. The bound (20.25) does not yield a condition number for the LSE problem, since it is not attainable. A sharp bound involving Kronecker products is obtained in [276, 1999], but it is more difficult to interpret. That the null space method for solving the LSE problem can be conveniently expressed in terms of the generalized QR factorization was pointed out by Paige [912, 1990] and Anderson, Bai, and Dongarra [21, 1992].

Perturbation bounds for the generalized QR factorization are given by Bar-lund [82, 1994].

No analogue of Theorem 20.5 is known for the LSE problem, but upper bounds on the normwise backward error of an approximate LSE solution are derived by Cox and Higham [277, 1999], where they are shown by experiment to be of practical use. A backward error formula for the problem of least squares minimization over a sphere, $\min_{\| x\| _2\leq \alpha}\| b - Ax\| _2$ , is given by Malyshev [812, 2001].

Theorem 20.10 is from Cox and Higham [276, 1999].

The use of a weighted QR factorization for solving weighted and/or linearly constrained LS problems is proposed and investigated by Gulliksson and Wedin [533, 1992], [531, 1994], [532, 1995].

In this chapter we have not treated LS problems with linear inequality constraints or quadratic constraints, or generalized LS problems. For coverage of these, see Björck [128, 1996, Chap. 5] and Golub and Van Loan [509, 1996, §§5.6.3, 12.1] and the references therein.

# 20.11.1. LAPACK

Driver routine xGELS solves the full rank LS problem by Householder QR factorization. It caters for multiple right-hand sides, each of which defines a separate LS problem. Thus, xGELS solves $\min \{\| B - AX\| _F:X\in \mathbb{R}^{n\times p}\}$ , where $A\in \mathbb{R}^{m\times n}$ ( $m\geq n$ ) and $B\in \mathbb{R}^{m\times p}$ . This routine does not return any error bounds, but code for computing an error bound (essentially (20.1)) is given in [20, 1999, §4.5]. Iterative refinement is not supported for LS problems in LAPACK.

Driver routines xGELSY and xGELSS, xGELSD solve the rank-deficient LS problem with multiple right-hand sides, using, respectively, a complete orthogonal factorization (computed via QR factorization with column pivoting), the SVD, and a divide and conquer implementation of the SVD.

LAPACK also contains routines for solving the LSE problem (xGGLSE, which uses the GQR method) and a generalized form of weighted LS problem (xGGGLM). Code for computing an error bound (essentially (20.25)) is given in [20, 1999, §4.6].

# Problems

20.1. Show that any solution to the LS problem $\min_x\| b - Ax\| _2$ satisfies the normal equations $A^T A x = A^T b$ . What is the geometrical interpretation of these equations?

20.2. Prove Theorem 20.3.

20.3. The pseudo-inverse $X \in \mathbb{R}^{n \times m}$ of $A \in \mathbb{R}^{m \times n}$ can be defined as the unique matrix satisfying the four Moore-Penrose conditions

(i) $AXA = A$ (ii) $XAX = X,$   
(iii) $AX = (AX)^T$ , (iv) $XA = (XA)^T$

Let $A = U\Sigma V^T$ be an SVD, with $\Sigma = \mathrm{diag}(\sigma_i)$ and let $r = \mathrm{rank}(A)$ . Show that $X = V\mathrm{diag}(\sigma_1^{-1},\ldots ,\sigma_r^{-1},0,\ldots ,0)U^T$ satisfies (i)-(iv) and hence is the pseudo-inverse of $A$ . Show that $(A^{+})^{+} = A$ .

20.4. Show that the pseudo-inverse $A^{+}$ of $A \in \mathbb{R}^{m \times n}$ solves the problem

$$
\min  _ {X \in \mathbb {R} ^ {n \times m}} \| A X - I _ {m} \| _ {F}.
$$

Is the solution unique?

20.5. Prove a result analogous to Theorem 20.3 for the MGS method, as described in §20.3.   
20.6. Consider the LS problem $\min_x\| b - Ax\| _2$ , where $A\in \mathbb{R}^{m\times n}$ . Let $\widehat{x}$ be the computed LS solution obtained from the normal equations method and $x$ the exact solution, and define $\widehat{r} = b - A\widehat{x}$ , $r = b - Ax$ . Using (20.12) and (20.13) show that a bound holds of the form

$$
\left| r ^ {T} r - \widehat {r} ^ {T} \widehat {r} \right| \leq c _ {m, n} u \| x - \widehat {x} \| _ {2} \| A \| _ {2} \left(\| A \| _ {2} \| \widehat {x} \| _ {2} + \| b \| _ {2}\right) + O \left(u ^ {2}\right).
$$

20.7. Prove (20.18) and (20.19).   
20.8. (Waldén, Karlson, and Sun [1203, 1995]) Partially complete the gap in Theorem 20.5 by evaluating $\eta_F(0)$ for the case “ $\theta = \infty$ ”, that is, $\Delta b \equiv 0$ .   
20.9. Prove (20.21).   
20.10. Show that $x$ solves the LSE problem (20.23) if and only if

$$
\begin{array}{l} A ^ {T} (b - A x) = B ^ {T} \lambda , \\ B x = d, \\ \end{array}
$$

where $\lambda \in \mathbb{R}^p$ is a vector of Lagrange multipliers. These are the normal equations for the LSE problem.

20.11. Show that for the unconstrained LS problem (20.25) reduces to a first-order approximation of (20.1).   
20.12. (RESEARCH PROBLEM) For the unconstrained least squares problem Gu [527, 1998] proves that mixed stability implies backward stability. Can this result be extended to the LSE problem?   
20.13. (RESEARCH PROBLEM) Derive a computable expression for the row-wise backward error of an approximate LS solution.
