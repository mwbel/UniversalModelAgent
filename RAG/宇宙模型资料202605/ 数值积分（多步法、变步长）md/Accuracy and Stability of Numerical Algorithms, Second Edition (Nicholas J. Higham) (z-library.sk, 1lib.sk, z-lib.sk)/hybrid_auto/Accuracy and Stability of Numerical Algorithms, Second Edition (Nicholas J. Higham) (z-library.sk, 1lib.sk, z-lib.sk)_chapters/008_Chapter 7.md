# Chapter 7

# Perturbation Theory for Linear Systems

Our hero is the intrepid, yet sensitive matrix $A$ .

Our villain is $E$ , who keeps perturbing $A$ .

When $A$ is perturbed he puts on a crumpled hat: $\widetilde{A} = A + E$ .

— G. W. STEWART and JI-GUANG SUN, Matrix Perturbation Theory (1990)

The expression 'ill-conditioned' is sometimes used merely as a term of abuse applicable to matrices or equations ...

It is characteristic of ill-conditioned sets of equations that small percentage errors in the coefficients given may lead to

large percentage errors in the solution.

— A. M. TURING, Rounding-Off Errors in Matrix Processes (1948)

In this chapter we are concerned with a linear system $Ax = b$ , where $A \in \mathbb{R}^{n \times n}$ . In the context of uncertain data or inexact arithmetic there are three important questions:

(1) How much does $x$ change if we perturb $A$ and $b$ ; that is, how sensitive is the solution to perturbations in the data?   
(2) How much do we have to perturb the data $A$ and $b$ for an approximate solution $y$ to be the exact solution of the perturbed system—in other words, what is the backward error of $y$ ?   
(3) What bound should we compute in practice for the forward error of a given approximate solution?

To answer these questions we need both normwise and componentwise perturbation theory.

# 7.1. Normwise Analysis

First, we present some classical normwise perturbation results. We denote by $\| \cdot \|$ any vector norm and the corresponding subordinate matrix norm. As usual, $\kappa (A) = \| A\| \| A^{-1}\|$ is the matrix condition number. Throughout this chapter the matrix $E$ and the vector $f$ are arbitrary and represent tolerances against which the perturbations are measured (their role becomes clear when we consider componentwise results).

Our first result makes precise the intuitive feeling that if the residual is small then we have a "good" approximate solution.

Theorem 7.1 (Rigal and Gaches). The normwise backward error

$$
\eta_ {E, f} (y) := \min  \left\{\epsilon : (A + \Delta A) y = b + \Delta b, \| \Delta A \| \leq \epsilon \| E \|, \| \Delta b \| \leq \epsilon \| f \| \right\} \tag {7.1}
$$

is given by

$$
\eta_ {E, f} (y) = \frac {\| r \|}{\| E \| \| y \| + \| f \|}, \tag {7.2}
$$

where $r = b - Ay$ .

Proof. It is straightforward to show that the right-hand side of (7.2) is a lower bound for $\eta_{E,f}(y)$ . This lower bound is attained for the perturbations

$$
\Delta A _ {\min } = \frac {\| E \| \| y \|}{\| E \| \| y \| + \| f \|} r z ^ {T}, \quad \Delta b _ {\min } = - \frac {\| f \|}{\| E \| \| y \| + \| f \|} r, \tag {7.3}
$$

where $z$ is a vector dual to $y$ (see §6.1).

For the particular choice $E = A$ and $f = b$ , $\eta_{E,f}(y)$ is called the normwise relative backward error.

The next result measures the sensitivity of the system.

Theorem 7.2. Let $Ax = b$ and $(A + \Delta A)y = b + \Delta b$ , where $\| \Delta A \| \leq \epsilon \| E \|$ and $\| \Delta b \| \leq \epsilon \| f \|$ , and assume that $\epsilon \| A^{-1} \| \| E \| < 1$ . Then

$$
\frac {\| x - y \|}{\| x \|} \leq \frac {\epsilon}{1 - \epsilon \| A ^ {- 1} \| \| E \|} \left(\frac {\| A ^ {- 1} \| \| f \|}{\| x \|} + \| A ^ {- 1} \| \| E \|\right), \tag {7.4}
$$

and this bound is attainable to first order in $\epsilon$ .

Proof. The bound (7.4) follows easily from the equation $A(y - x) = \Delta b - \Delta Ax + \Delta A(x - y)$ . It is attained to first order in $\epsilon$ for $\Delta A = \epsilon \| E \| \| x \| w v^T$ and $\Delta b = -\epsilon \| f \| w$ , where $\| w \| = 1$ , $\| A^{-1}w \| = \| A^{-1} \|$ , and $v$ is a vector dual to $x$ .

Associated with the way of measuring perturbations used in these two theorems is the normwise condition number

$$
\begin{array}{l} \kappa_ {E, f} (A, x) := \lim  _ {\epsilon \rightarrow 0} \sup  \left\{\frac {\| \Delta x \|}{\epsilon \| x \|}: (A + \Delta A) (x + \Delta x) = b + \Delta b, \right. \\ \left. \left\| \Delta A \right\| \leq \epsilon \| E \|, \quad \| \Delta b \| \leq \epsilon \| f \| \right\}. \\ \end{array}
$$

Because the bound of Theorem 7.2 is sharp, it follows that

$$
\kappa_ {E, f} (A, x) = \frac {\| A ^ {- 1} \| \| f \|}{\| x \|} + \| A ^ {- 1} \| \| E \|. \tag {7.5}
$$

For the choice $E = A$ and $f = b$ we have $\kappa(A) \leq \kappa_{E,f}(A,x) \leq 2\kappa(A)$ , and the bound (7.4) can be weakened slightly to yield the familiar form

$$
\frac {\| x - y \|}{\| x \|} \leq \frac {2 \epsilon \kappa (A)}{1 - \epsilon \kappa (A)}.
$$

A numerical example illustrates the above results. Let $A$ be the $6 \times 6$ Vandermonde matrix with $(i,j)$ element $j^{2(i-1)}$ and let $b = e_1$ be the first unit vector, so that $x$ is the first column of $A^{-1}$ . We take $y$ to be the approximate solution to $Ax = b$ computed by Gaussian elimination with partial pivoting. Computations are performed in MATLAB $(u \approx 1.1 \times 10^{-16})$ . We find that $\eta_{A,b}(y) = 4.16 \times 10^{-20}$ for the $\infty$ -norm, and $\kappa_{\infty}(A) = 1.93 \times 10^8$ . This is an admirably small backward error, but it may be uninformative for two reasons. First, the elements of $A$ vary over 7 orders of magnitude, so while our backward error perturbations are small compared with the large elements of $A$ , we may be making large perturbations in the small elements (indeed we are in this particular example). Second, we are perturbing the zero elements of $b$ (as can be seen from (7.3) together with the fact that for this example the residual $r$ has no zero entries); this is unsatisfactory if we wish to regard $y$ as the first column of the inverse of a perturbed matrix.

Next, let $b = Ae$ , where $e = [1, 1, \dots, 1]^T$ , and let $z$ be the solution to the perturbed system $(A + \Delta A)z = b$ , where $\Delta A = \mathrm{tol}|A|$ with $\mathrm{tol} = 10^{-10}$ ; thus we are perturbing each element of $A$ by a small relative amount. We find that

$$
\frac {\| x - z \| _ {\infty}}{\| x \| _ {\infty}} = 1. 0 0 \times 1 0 ^ {- 1 0}, \tag {7.6}
$$

while the corresponding bound from (7.4) with $\epsilon = \mathrm{tol}$ , $E = A$ , and $f = 0$ is $1.97 \times 10^{-2}$ . Thus the normwise forward error bound is extremely pessimistic for this special choice of perturbation.

To obtain a more satisfactory backward error measure and a sharper perturbation bound in this example, we need componentwise analysis.

# 7.2. Componentwise Analysis

The componentwise backward error is defined as

$$
\omega_ {E, f} (y) = \min  \{\epsilon : (A + \Delta A) y = b + \Delta b, | \Delta A | \leq \epsilon E, | \Delta b | \leq \epsilon f \}, \tag {7.7}
$$

where $E$ and $f$ are now assumed to have nonnegative entries. Absolute values and inequalities between matrices or vectors are understood to hold componentwise. In this definition each element of a perturbation is measured relative to its individual tolerance, so, unlike in the normwise definition, we are making full use of the $n^2 + n$ parameters in $E$ and $f$ .

How should $E$ and $f$ be chosen? There are four main choices of interest. The most common choice of tolerances is $E = |A|$ and $f = |b|$ , which yields the componentwise relative backward error. For this choice

$$
a _ {i j} = 0 \Rightarrow \Delta a _ {i j} = 0 \quad \text {a n d} \quad b _ {i} = 0 \Rightarrow \Delta b _ {i} = 0
$$

in (7.7), and so if $\omega_{E,f}(y)$ is small then $y$ solves a problem that is close to the original one in the sense of componentwise relative perturbations and has the same sparsity pattern. Another attractive property of the componentwise relative backward error is that it is insensitive to the scaling of the system: if $Ax = b$ is scaled to $(S_1AS_2)(S_2^{-1}x) = S_1b$ , where $S_1$ and $S_2$ are diagonal, and $y$ is scaled to $S_2^{-1}y$ , then $\omega$ remains unchanged.

The choice $E = |A|ee^{T}$ , $f = |b|$ gives a row-wise backward error. The constraint $|\Delta A| \leq \epsilon E$ is now $|\Delta a_{ij}| \leq \epsilon \alpha_{i}$ , where $\alpha_{i}$ is the 1-norm of the $i$ th row of $A$ , so perturbations to the $i$ th row of $A$ are being measured relative to the norm of that row (and similarly for $b$ ). A columnwise backward error can be formulated in a similar way, by taking $E = ee^{T}|A|$ and $f = \| b\|_{1}e$ here, perturbations to the $j$ th column of $A$ (or to $b$ ) are measured relative to the 1-norm of that column.

The fourth natural choice of tolerances is $E = \| A \| ee^T$ and $f = \| b \| e$ , for which $\omega_{E,f}(y)$ is the same as the normwise backward error $\eta_{E,f}(y)$ , up to a constant.

As for the normwise backward error in Theorem 7.1, there is a simple formula for $\omega_{E,f}(y)$ .

Theorem 7.3 (Oettli and Prager). The componentwise backward error is given by

$$
\omega_ {E, f} (y) = \max  _ {i} \frac {\left| r _ {i} \right|}{(E | y | + f) _ {i}}, \tag {7.8}
$$

where $r = b - Ay$ , and $\xi / 0$ is interpreted as zero if $\xi = 0$ and infinity otherwise.

Proof. It is easy to show that the right-hand side of (7.8) is a lower bound for $\omega(y)$ , and that this bound is attained for the perturbations

$$
\Delta A = D _ {1} E D _ {2}, \quad \Delta b = - D _ {1} f, \tag {7.9}
$$

where $D_{1} = \mathrm{diag}\big(r_{i} / (E|y| + f)_{i}\big)$ and $D_{2} = \mathrm{diag}\big(\mathrm{sign}(y_{i})\big)$ .

The next result gives a forward error bound corresponding to the component-wise backward error.

Theorem 7.4. Let $Ax = b$ and $(A + \Delta A)y = b + \Delta b$ , where $|\Delta A| \leq \epsilon E$ and $|\Delta b| \leq \epsilon f$ , and assume that $\epsilon \| |A^{-1}|E \| < 1$ , where $\| \cdot \|$ is an absolute norm. Then

$$
\frac {\| x - y \|}{\| x \|} \leq \frac {\epsilon}{1 - \epsilon \| | A ^ {- 1} | E \|} \frac {\| | A ^ {- 1} | (| E | x | + f) \|}{\| x \|}, \tag {7.10}
$$

and for the $\infty$ -norm this bound is attainable to first order in $\epsilon$ .

Proof. The bound (7.10) follows easily from the equation $A(y - x) = \Delta b - \Delta Ax + \Delta A(x - y)$ . For the $\infty$ -norm the bound is attained, to first order in $\epsilon$ , for $\Delta A = \epsilon D_1ED_2$ and $\Delta b = -\epsilon D_1f$ , where $D_2 = \mathrm{diag}(\mathrm{sign}(x_i))$ and $D_1 = \mathrm{diag}(\xi_j)$ , where $\xi_j = \mathrm{sign}(A^{-1})_{kj}$ and $\| |A^{-1}|(|E|x| + f)\|_{\infty} = \big(|A^{-1}|(|E|x| + f)\big)_k$ .

Theorem 7.4 implies that the condition number

$$
\begin{array}{l} \operatorname {c o n d} _ {E, f} (A, x) := \lim  _ {\epsilon \rightarrow 0} \sup  \left\{\frac {\| \Delta x \| _ {\infty}}{\epsilon \| x \| _ {\infty}}: (A + \Delta A) (x + \Delta x) = b + \Delta b, \right. \\ \left. \left| \Delta A \right| \leq \epsilon E, \left. \left| \Delta b \right| \leq \epsilon f \right\} \right. \\ \end{array}
$$

is given by

$$
\operatorname {c o n d} _ {E, f} (A, x) = \frac {\| | A ^ {- 1} | (\left| E | x | + f\right) \| _ {\infty}}{\| x \| _ {\infty}}. \tag {7.11}
$$

This condition number depends on $x$ or, equivalently, on the right-hand side $b$ . A worst-case measure of sensitivity applicable to all $x$ is

$$
\operatorname {c o n d} _ {E, f} (A) = \max  _ {x} \operatorname {c o n d} _ {E, f} (A, x), \tag {7.12}
$$

where in practice we can take any convenient approximation to the maximum that is correct to within a constant factor.

For the special case $E = |A|$ and $f = |b|$ we have the condition numbers introduced by Skeel [1040, 1979]:

$$
\begin{array}{l} \operatorname {c o n d} (A, x) := \frac {\| | A ^ {- 1} | | A | | x | \| _ {\infty}}{\| x \| _ {\infty}}, (7.13) \\ \operatorname {c o n d} (A) := \operatorname {c o n d} (A, e) = \| | A ^ {- 1} | | A | \| _ {\infty} \leq \kappa_ {\infty} (A). (7.14) \\ \end{array}
$$

These differ from $\operatorname{cond}_{|A|, |b|}(A, x)$ and $\operatorname{cond}_{|A|, |b|}(A)$ , respectively, by at most a factor 2.

How does cond compare with $\kappa$ ? Since $\operatorname{cond}(A)$ is invariant under row scaling $Ax = b \to (DA)x = Db$ , where $D$ is diagonal, it can be arbitrarily smaller than $\kappa_{\infty}(A)$ . In fact, it is straightforward to show that

$$
\min  \left\{\kappa_ {\infty} (D A): D \text {d i a g o n a l} \right\} = \operatorname {c o n d} (A), \tag {7.15}
$$

where the optimal scaling $D_R$ equilibrates the rows of $A$ , that is, $D_R A$ has rows of unit 1-norm ( $D_R | A | e = e$ )

Chandrasekaran and Ipsen [217, 1995] note the following inequalities. First, with $D_R$ as just defined,

$$
\frac {\kappa_ {\infty} (A)}{\kappa_ {\infty} \left(D _ {R}\right)} \leq \operatorname {c o n d} (A) \leq \kappa_ {\infty} (A) \tag {7.16}
$$

(these inequalities imply (7.15)). Thus $\operatorname{cond}(A)$ can be much smaller than $\kappa_{\infty}(A)$ only when the rows of $A$ are badly scaled. Second, if $D_C$ equilibrates the columns of $A$ ( $e^T|A|D_C = e^T$ ) then

$$
\frac {\kappa_ {1} (A)}{n \kappa_ {\infty} (D _ {C})} \min  _ {j} \frac {\| A ^ {- 1} e _ {j} \| _ {\infty}}{\| A ^ {- 1} \| _ {1}} \leq \operatorname {c o n d} (A, x) \leq \kappa_ {\infty} (A).
$$

These inequalities show that $\operatorname{cond}(A, x)$ can be much smaller than $\kappa_{\infty}(A)$ only when the columns of either $A$ or $A^{-1}$ are badly scaled.

Returning to the numerical example of §7.1, we find that $\omega_{E,f}(y) = 5.76 \times 10^{-15}$ for $E = |A|$ and $f = |b|$ or $f = 0$ . This tells us that if we measure changes to $A$ in a componentwise relative sense, then for $y$ to be the first column of the inverse of a perturbed matrix we must make relative changes to $A$ of just over one order of magnitude larger than the unit roundoff. For the perturbed system, Theorem 7.4 with $\epsilon = \mathrm{tol}$ , $E = |A|$ , and $f = 0$ gives the bound

$$
\frac {\| x - z \| _ {\infty}}{\| x \| _ {\infty}} \leq 4. 3 7 \times 1 0 ^ {- 7},
$$

which is five orders of magnitude smaller than the normwise bound from Theorem 7.2, though still three orders of magnitude larger than the actual forward error (7.6).

An example of Kahan [687, 1966] is also instructive. Let

$$
A = \left[ \begin{array}{r r r} 2 & - 1 & 1 \\ - 1 & \epsilon & \epsilon \\ 1 & \epsilon & \epsilon \end{array} \right], \quad b = \left[ \begin{array}{c} 2 (1 + \epsilon) \\ - \epsilon \\ \epsilon \end{array} \right], \tag {7.17}
$$

where $0 < \epsilon \ll 1$ , so that $x = [\epsilon, -1, 1]^T$ . The normwise condition number $\kappa_{\infty}(A)$ is $2(1 + \epsilon^{-1})$ , so the system is very sensitive to arbitrary perturbations in $A$ and $b$ . Moreover,

$$
| A ^ {- 1} | | A | = \left[ \begin{array}{l l l} 1 & \epsilon & \epsilon \\ \frac {2 \epsilon + 1}{2 \epsilon} & 1 & 1 \\ \frac {2 \epsilon + 1}{2 \epsilon} & 1 & 1 \end{array} \right],
$$

so $\operatorname{cond}(A) = 3 + (2\epsilon)^{-1}$ , which implies that the system is also very sensitive to componentwise perturbations for some right-hand sides. However, $\operatorname{cond}(A,x) = 5/2 + \epsilon$ , so for this particular $b$ the system is very well conditioned under componentwise perturbations.

A word is in order concerning the choice of condition number. Every condition number for a linear system is defined with respect to a particular class of perturbations. It is important to use the right condition number for the occasion. For example, if $\widehat{x}$ is a computed solution to $Ax = b$ and we know its normwise backward error $\eta_{A,b}(\widehat{x})$ , then it is the condition number $\kappa(A)$ that appears in the relevant forward error bound (multiplying $\eta_{A,b}(\widehat{x})$ ) and therefore tells us something about the accuracy of $\widehat{x}$ . The componentwise condition number $\operatorname{cond}(A,x)$ is relevant only if we are dealing with the componentwise relative backward error,

Table 7.1. Four classes of perturbations and the corresponding condition numbers. The terms $\operatorname{cond}(A, x)$ and $\operatorname{cond}(A)$ are defined in (7.13) and (7.14).   

<table><tr><td></td><td>Componentwise relative</td><td>Row-wise</td><td>Columnwise</td><td>Normwise</td></tr><tr><td>E</td><td>|A|</td><td>|A|eeT</td><td>eeT|A|</td><td>||A||∞eeT</td></tr><tr><td>f</td><td>|b|</td><td>|b|</td><td>||b||1e</td><td>||b||∞e</td></tr><tr><td>condE,f(A,x)</td><td>cond(A,x)</td><td>cond(A) ||x||1/||x||∞</td><td>||A-1||∞ ||A||x||1/||x||∞</td><td>κ∞(A)</td></tr><tr><td>condE,f(A)</td><td>cond(A)</td><td>n cond(A)</td><td>κ∞(A)</td><td>κ∞(A)</td></tr></table>

$\omega_{|A|,|b|}(\widehat{x})$ . Looked at another way, each algorithm has an associated error analysis that determines the condition number relevant to that algorithm.

Table 7.1 summarizes the four main classes of perturbations and the corresponding condition numbers $\operatorname{cond}_{E,f}(A,x)$ and $\operatorname{cond}_{E,f}(A)$ . The row-wise and columnwise condition numbers in the table (which are lower bounds that are at most a constant factor smaller than the actual condition numbers) follow from Problem 7.6.

# 7.3. Scaling to Minimize the Condition Number

In the last section we noted the invariance of $\operatorname{cond}(A)$ under row scaling, which contrasts with the strong dependence of $\kappa_{\infty}(A)$ upon the row scaling. The opportunity to scale the rows or columns of $A$ arises in various applications, so we now take a closer look at the effect of scaling on the normwise condition number.

First, we consider one-sided scaling, by giving a generalization of a well-known result of van der Sluis [1176, 1969]. It shows that, for one-sided scaling in a Hölder $p$ -norm, equilibrating the rows or columns is a nearly optimal strategy. We state the result for rectangular matrices $A$ , for which we define $\kappa_p(A) \coloneqq \| A \|_p \| A^+ \|_p$ , where $A^+$ is the pseudo-inverse of $A$ (see Problem 20.3).

Theorem 7.5 (van der Sluis). Let $A \in \mathbb{R}^{m \times n}$ , let $\mathcal{D}_k \subset \mathbb{R}^{k \times k}$ denote the set of nonsingular diagonal matrices, and define

$$
D _ {C} := \operatorname {d i a g} \left(\left\| A (:, j) \right\| _ {p}\right) ^ {- 1}, \quad D _ {R} := \operatorname {d i a g} \left(\left\| A (i,:) \right\| _ {p}\right) ^ {- 1}.
$$

Then

$$
\kappa_ {p} \left(A D _ {C}\right) \leq n ^ {1 - 1 / p} \min  _ {D \in \mathcal {D} _ {n}} \kappa_ {p} (A D) \quad i f \operatorname {r a n k} (A) = n, \tag {7.18}
$$

$$
\kappa_ {p} (D _ {R} A) \leq m ^ {1 / p} \min  _ {D \in \mathcal {D} _ {m}} \kappa_ {p} (D A) \quad i f \operatorname {r a n k} (A) = m. \tag {7.19}
$$

Proof. For any $X \in \mathbb{R}^{m \times n}$ we have, from (6.12),

$$
\max  _ {j} \| A (:, j) \| _ {p} \leq \| A \| _ {p} \leq n ^ {1 - 1 / p} \max  _ {j} \| A (:, j) \| _ {p}. \tag {7.20}
$$

Therefore

$$
\left\| A D _ {C} \right\| _ {p} \leq n ^ {1 - 1 / p}. \tag {7.21}
$$

Now, for any $D \in \mathcal{D}_n$ ,

$$
\begin{array}{l} \| D _ {C} ^ {- 1} A ^ {+} \| _ {p} = \| D _ {C} ^ {- 1} D \cdot D ^ {- 1} A ^ {+} \| _ {p} \\ \leq \max  _ {j} \left(\left| d _ {j j} \right| \| A (:, j) \| _ {p}\right) \| D ^ {- 1} A ^ {+} \| _ {p} \\ \leq \left\| A D \right\| _ {p} \left\| D ^ {- 1} A ^ {+} \right\| _ {p} = \kappa_ {p} (A D), \tag {7.22} \\ \end{array}
$$

using the first inequality in (7.20). Multiplying (7.21) and (7.22) and minimizing over $D$ , we obtain (7.18). Inequality (7.19) follows by noting that $\kappa_{p}(DA) = \kappa_{q}(A^{T}D)$ , where $p^{-1} + q^{-1} = 1$ (see (6.21)).

For $p = \infty$ , (7.19) confirms what we already know from (7.15) and (7.16) for square matrices: that in the $\infty$ -norm, row equilibration is an optimal row scaling strategy. Similarly, for $p = 1$ , column equilibration is the best column scaling, by (7.18). Theorem 7.5 is usually stated for the 2-norm, for which it shows that row and column equilibration produce condition numbers within factors $\sqrt{m}$ and $\sqrt{n}$ , respectively, of the minimum 2-norm condition numbers achievable by row and column scaling.

As a corollary of Theorem 7.5 we have the result that among two-sided diagonal scalings of a symmetric positive definite matrix, the one that gives $A$ a unit diagonal is not far from optimal.

Corollary 7.6 (van der Sluis). Let $A \in \mathbb{R}^{n \times n}$ be symmetric positive definite and let $D_{*} = \mathrm{diag}(a_{ii}^{-1/2})$ . Then

$$
\kappa_ {2} \left(D _ {*} A D _ {*}\right) \leq n \min  _ {D \in \mathcal {D} _ {n}} \kappa_ {2} (D A D). \tag {7.23}
$$

Proof. Let $A = R^T R$ be a Cholesky factorization, note that $\kappa_2(DAD) = \kappa_2(RD)^2$ , and apply Theorem 7.5 to $RD$ .

Is the scaling $D_{*}$ in Corollary 7.6 ever optimal? Forsythe and Straus [432, 1955] show that it is optimal if $A$ is symmetric positive definite with property A (that is, there exists a permutation matrix $P$ such that $PAP^T$ can be expressed as a block $2 \times 2$ matrix whose $(1,1)$ and $(2,2)$ blocks are diagonal). Thus, for example, any symmetric positive definite tridiagonal matrix with unit diagonal is optimally scaled.

We note that by using (6.23) in place of (7.20), the inequalities of Theorem 7.5 and Corollary 7.6 can be strengthened by replacing $m$ and $n$ with the maximum number of nonzeros per column and row, respectively.

Here is an independent result for the Frobenius norm.

Theorem 7.7 (Stewart and Sun). Let $A = [a_1, \ldots, a_n] \in \mathbb{R}^{n \times n}$ be nonsingular, with $B := A^{-1} = [b_1, \ldots, b_n]^T$ , and let $D_C = \mathrm{diag}((\|b_j\|_2 / \|a_j\|_2)^{1/2})$ . Then

$$
\sum_ {j} \| a _ {j} \| _ {2} \| b _ {j} \| _ {2} = \kappa_ {F} (A D _ {C}) = \min  _ {D \in \mathcal {D} _ {n}} \kappa_ {F} (A D).
$$

Proof. For $D = \mathrm{diag}(d_i) \in \mathcal{D}_n$ , we have, using the Cauchy-Schwarz inequality,

$$
\kappa_ {F} (A D) = \left(\sum_ {j} d _ {j} ^ {2} \| a _ {j} \| _ {2} ^ {2}\right) ^ {1 / 2} \left(\sum_ {j} d _ {j} ^ {- 2} \| b _ {j} \| _ {2} ^ {2}\right) ^ {1 / 2} \geq \sum_ {j} \| a _ {j} \| _ {2} \| b _ {j} \| _ {2},
$$

with equality if $d_j \| a_j \|_2 = \alpha d_j^{-1} \| b_j \|_2$ for all $j$ , for some $\alpha \neq 0$ . There is equality for $d_j^2 = \| b_j \|_2 / \| a_j \|_2$ .

As we have seen in this and the previous section, the minimum value of $\kappa_{\infty}(DA)$ is $\| |A^{-1}||A|\|_{\infty}$ . The next result shows that for two-sided scalings the matrix $|A^{-1}||A|$ again features in the formula for the minimal condition number. A matrix is irreducible if it cannot be symmetrically permuted to block triangular form. A Perron vector of $B \geq 0$ is a nonnegative eigenvector corresponding to the eigenvalue $\rho(B)$ , where $\rho$ denotes the spectral radius.

Theorem 7.8 (Bauer). Let $A \in \mathbb{R}^{n \times n}$ be nonsingular and suppose that $|A||A^{-1}|$ and $|A^{-1}||A|$ are irreducible. Then

$$
\min  _ {D _ {1}, D _ {2} \in \mathcal {D} _ {n}} \kappa_ {\infty} \left(D _ {1} A D _ {2}\right) = \rho \left(\left| A \right| \left| A ^ {- 1} \right|\right). \tag {7.24}
$$

The minimum is attained for $D_{1} = \mathrm{diag}(x)^{-1}$ and $D_{2} = \mathrm{diag}(|A^{-1}|x)$ , where $x > 0$ is a right Perron vector of $|A||A^{-1}|$ (so that $|A||A^{-1}| = \rho(|A||A^{-1}|)x$ ).

Proof. See Problem 7.10. $\square$

Rump [1002, 2002] shows that (7.24) holds for any nonsingular $A$ if the minimum on the left-hand side is replaced by an infimum.

For the Kahan example (7.17),

$$
\rho (| A ^ {- 1} | | A |) \approx 2. 6 2 + 1. 7 9 \epsilon \ll 3 + (2 \epsilon) ^ {- 1} = \| | A ^ {- 1} | | A | \| _ {\infty},
$$

and, in fact, $\kappa_{\infty}(DAD) = 3$ for $D = \mathrm{diag}(\epsilon^{1/2}, \epsilon^{-1/2}, \epsilon^{-1/2})$ , so a symmetric two-sided scaling is nearly optimal in this case.

# 7.4. The Matrix Inverse

We briefly discuss componentwise perturbation theory for the matrix inverse. With $X \coloneqq A^{-1}$ and $X + \Delta X \coloneqq (A + \Delta A)^{-1}$ , a componentwise condition number is

$$
\mu_ {E} (A) := \lim  _ {\epsilon \rightarrow 0} \sup  \left\{\frac {\| \Delta X \| _ {\infty}}{\epsilon \| X \| _ {\infty}}: | \Delta A | \leq \epsilon E \right\} \leq \frac {\| | A ^ {- 1} | E | A ^ {- 1} | \| _ {\infty}}{\| A ^ {- 1} \| _ {\infty}}. \tag {7.25}
$$

In general, the inequality is strict, but there is equality when $|A^{-1}| = D_1A^{-1}D_2$ for $D_i$ of the form $\mathrm{diag}(\pm 1)$ [444, 1992, Thm. 1.10], [479, 1982]. Another componentwise condition number is evaluated in Problem 7.11. We saw in Theorem 6.5 that the reciprocal of the normwise condition number for matrix inversion is the normwise relative distance to singularity. Is the same true for an appropriate componentwise condition number? The componentwise distance to singularity,

$$
d _ {E} (A) := \min  \left\{\epsilon : A + \Delta A \text {s i n g u l a r ,} | \Delta A | \leq \epsilon E \right\},
$$

has been characterized by Rohn [990, 1989], [991, 1990] as

$$
d _ {E} (A) = \frac {1}{\operatorname * {m a x} _ {S _ {1} , S _ {2}} \rho_ {0} (S _ {1} A ^ {- 1} S _ {2} E)},
$$

where the maximum is taken over all signature matrices $S_{i} = \mathrm{diag}(\pm 1)$ and where

$$
\rho_ {0} (X) = \max  \left\{\left| \lambda \right|: \lambda \text {i s a r e a l e i g e n v a l u e o f} A \right\}.
$$

This formula involves $4^n$ eigenproblems and thus is computationally intractable (in fact it has been shown to be NP-hard by Poljak and Rohn [945, 1993]).

Demmel [313, 1992] shows by complexity arguments that there can be no simple relationship between $d_E(A)$ and the quantity $\| |A^{-1}|E\|_{\infty}$ , which is an upper bound for $\mu_E(A)$ . However, $d_E(A)$ behaves like $1 / \rho (|A^{-1}|E)$ , as

$$
\frac {1}{\rho \left(\left| A ^ {- 1} \right| E\right)} \leq d _ {E} (A) \leq \frac {(3 + 2 \sqrt {2}) n}{\rho \left(\left| A ^ {- 1} \right| E\right)}, \tag {7.26}
$$

and the upper bound is almost sharp because examples are known for which $d_{E}(A) = n / \rho (|A^{-1}|E)$ . The lower bound was obtained by Demmel [313, 1992], and the more difficult upper bound and the observation about its sharpness are due to Rump [999, 1999] (see also the references therein for the history of the bound). In the case $E = |A|$ these inequalities are aesthetically pleasing because $d_{|A|}(A)$ is invariant under two-sided diagonal scalings of $A$ and $\rho (|A^{-1}||A|)$ is the minimum $\infty$ -norm condition number achievable by such scalings, as shown by Theorem 7.8.

# 7.5. Extensions

The componentwise analyses can be extended in three main ways.

(1) We can use more general measures of size for the data and the solution. Higham and Higham [575, 1992] measure $\Delta A$ , $\Delta b$ , and $\Delta x$ by

$$
\nu_ {p} \left(\left[ \left(\Delta a _ {i j} / e _ {i j}\right) \left(\Delta b _ {i} / f _ {i}\right) \right]\right), \quad \nu_ {p} \left(\left(\Delta x _ {i} / g _ {i}\right)\right),
$$

where $\nu_{p}(A) = \left(\sum_{i,j}|a_{ij}|^{p}\right)^{1 / p}, 1\leq p\leq \infty$ , and the $e_{ij}$ , $f_{i}$ , and $g_{i}$ are tolerances. They show that the corresponding backward error is given by the explicit formula

$$
\left\| \left(\frac {r _ {j}}{\| D _ {j} \left[ \begin{array}{c} y \\ - 1 \end{array} \right] \| _ {q}}\right) \right\| _ {p},
$$

where $r = b - Ay$ , $D_{j} = \mathrm{diag}(e_{j1},\ldots ,e_{jn},f_{j})$ , and $p^{-1} + q^{-1} = 1$ ; bounds for the corresponding condition number are also obtained. Theorem 7.3, and Theorem 7.4 with the $\infty$ -norm, correspond to $p = \infty$ and $g_{i}\equiv \| x\|_{\infty}$ . If we take $p = \infty$ and $g = |x|$ , we are measuring the change in the solution in a componentwise relative sense, as $\nu_{p}((\varDelta x_{i}/g_{i}))=\max _{i}|\varDelta x_{i}|/|x_{i}|$ , and the condition number is [575, 1992]

$$
\left\| \operatorname {d i a g} (| x _ {i} |) ^ {- 1} | A ^ {- 1} | (E | x | + f) \right\| _ {\infty}.
$$

This latter case has also been considered by Rohn [989, 1989] and Gohberg and Koltracht [494, 1993]. It is also possible to obtain individual bounds for $|\Delta x_i| / |x_i|$ ,

$i = 1:n$ , by refraining from taking norms in the analysis; see Chandrasekaran and Ipsen [217, 1995] and Problem 7.1.

(2) The backward error results and the perturbation theory can be extended to systems with multiple right-hand sides. For the general $\nu_{p}$ measure described in (1), the backward error can be computed by finding the minimum $p$ -norm solutions to $n$ underdetermined linear systems. For details, see Higham and Higham [575, 1992].

(3) Structure in $A$ and $b$ can be preserved in the analysis. For example, if $A$ is symmetric or Toeplitz then its perturbation can be forced to be symmetric or Toeplitz too, while still using componentwise measures. References include Higham and Higham [574, 1992] and Gohberg and Koltracht [494, 1993] for linear structure, and Bartels and D. J. Higham [86, 1992] and Sun [1109, 1998] for Vandermonde structure. A symmetry-preserving normwise backward error for linear systems is explored by Bunch, Demmel, and Van Loan [180, 1989], while Smoktunowicz [1053, 1995] considers the componentwise case (see Problem 7.12). Symmetry-preserving normwise condition numbers for the matrix inverse and linear systems are treated by D. J. Higham [573, 1995], who shows that they cannot differ much from the general condition numbers. Rump [997, 1998] proves the same thing for componentwise condition numbers, and also shows that when symmetry is exploited in the definitions the componentwise condition number and componentwise distance to singularity can differ by an arbitrary factor.

# 7.6. Numerical Stability

The backward errors examined in this chapter lead to definitions of numerical stability of algorithms for solving linear systems. Precise and formal definitions of stability can be given, but there are so many possibilities, across different problems, that to define and name each one tends to cloud the issues of interest. We therefore adopt an informal approach.

A numerical method for solving a square, nonsingular linear system $Ax = b$ is normwise backward stable if it produces a computed solution such that $\eta_{A,b}(\widehat{x})$ is of order the unit roundoff. How large we allow $\eta_{A,b}(\widehat{x}) / u$ to be, while still declaring the method backward stable, depends on the context. It is usually implicit in this definition that $\eta_{A,b}(\widehat{x}) = O(u)$ for all $A$ and $b$ , and a method that yields $\eta_{A,b}(\widehat{x}) = O(u)$ for a particular $A$ and $b$ is said to have performed in a normwise backward stable manner.

The significance of normwise backward stability is that the computed solution solves a slightly perturbed problem, and if the data $A$ and $b$ contain uncertainties bounded only normwise ( $A \to A + \Delta A$ with $\| \Delta A \| = O(u \| A \|)$ ) and similarly for $b$ ), then $\widehat{x}$ may be the exact solution to the problem we wanted to solve, for all we know.

Componentwise backward stability is defined in a similar way: we now require the componentwise backward error $\omega_{|A|,|b|}(\widehat{x})$ to be of order $u$ . This is a more stringent requirement than normwise backward stability. The rounding errors incurred by a method that is componentwise backward stable are in size and effect equivalent to the errors incurred in simply converting the data $A$ and $b$ to floating point numbers before the solution process begins.

Table 7.2. Backward and forward stability.   

<table><tr><td colspan="2">Componentwise backward stability ⇒ Componentwise forward stability</td></tr><tr><td>ω|A|,|b|(x̂) = O(u)</td><td>||x - x̂||/||x|| = O( cond(A, x)u)</td></tr><tr><td>↓</td><td>↓</td></tr><tr><td colspan="2">Normwise backward stability ⇒ Normwise forward stability</td></tr><tr><td>ηA,b(x̂) = O(u)</td><td>||x - x̂||/||x|| = O(κ(A)u)</td></tr></table>

If a method is normwise backward stable then, by Theorem 7.2, the forward error $\| x - \widehat{x} \| / \| x\|$ is bounded by a multiple of $\kappa(A)u$ . However, a method can produce a solution whose forward error is bounded in this way without the normwise backward error $\eta_{A,b}(\widehat{x})$ being of order $u$ . Hence it is useful to define a method for which $\| x - \widehat{x}\| /\| x\| = O(\kappa(A)u)$ as normwise forward stable. By similar reasoning involving $\omega_{|A|,|b|}(\widehat{x})$ , we say a method is componentwise forward stable if $\| x - \widehat{x}\| /\| x\| = O(\operatorname{cond}(A,x)u)$ . Table 7.2 summarizes the definitions and the relations between them. There are several examples in this book of linear-equation-solving algorithms that are forward stable but not backward stable: Cramer's rule for $n = 2$ (\$1.10.1), Gauss-Jordan elimination (\$14.4), and the seminormal equations method for underdetermined systems (\$21.3).

Other definitions of numerical stability can be useful (for example, row-wise backward stability means that $\eta_{|A|ee^T,|b|}(\widehat{x}) = O(u)$ ), and they will be introduced when needed.

# 7.7. Practical Error Bounds

Suppose we have a computed approximation $\widehat{x}$ to the solution of a linear system $Ax = b$ , where $A \in \mathbb{R}^{n \times n}$ . What error bounds should we compute?

The backward error can be computed exactly, from the formulae

$$
\begin{array}{l} \eta_ {E, f} (\widehat {x}) = \frac {\| r \|}{\| E \| \| \widehat {x} \| + \| f \|}, \\ \omega_ {E, f} (\widehat {x}) = \max  _ {i} \frac {\left| r _ {i} \right|}{(E | \widehat {x} | + f) _ {i}}, \tag {7.27} \\ \end{array}
$$

at the cost of one or two matrix-vector products, for $r = b - A\widehat{x}$ and $E|\widehat{x}|$ . The only question is what to do if the denominator is so small as to cause overflow or division by zero in the expression for $\omega_{E,f}(\widehat{x})$ . This could happen, for example, when $E = |A|$ and $f = |b|$ and, for some $i$ , $a_{ij}x_j = 0$ for all $j$ , as is most likely in a sparse problem. LAPACK's xyyRFS ("refine solution") routines apply iterative refinement in fixed precision, in an attempt to satisfy $\omega_{|A|,|b|} \leq u$ . If the $i$ th component of the denominator in (7.27) is less than safe_min/u, where safe_min is the smallest number such that 1/safe_min does not overflow, then they add $(n + 1)$ safe_min to the $i$ th components of the numerator and denominator. A more sophisticated strategy is advocated for sparse problems by Arioli, Demmel,

and Duff [30, 1989]. They suggest modifying the formula (7.27) for $\omega_{|A|,|b|}$ by replacing $|b_i|$ in the denominator by $\| A(i,:)\| _1\| \widehat{x}\|_\infty$ when the $i$ th denominator is very small. See [30, 1989] for details and justification of this strategy.

Turning to the forward error, one approach is to evaluate the forward error bound from Theorem 7.2 or Theorem 7.4, with $\epsilon$ equal to the corresponding backward error. Because $x$ in (7.10) is unknown, we should use the modified bound

$$
\frac {\| x - \widehat {x} \| _ {\infty}}{\| \widehat {x} \| _ {\infty}} \leq \omega_ {E, f} (\widehat {x}) \frac {\| | A ^ {- 1} | (E | \widehat {x} | + f) \| _ {\infty}}{\| \widehat {x} \| _ {\infty}}. \tag {7.28}
$$

If we have a particular $E$ and $f$ in mind for backward error reasons, then it is natural to use them in (7.28). However, the size of the forward error bound varies with $E$ and $f$ , so it is natural to ask which choice minimizes the bound.

Lemma 7.9. The upper bound in (7.28) is at least as large as the upper bound in

$$
\frac {\| x - \widehat {x} \| _ {\infty}}{\| \widehat {x} \| _ {\infty}} \leq \frac {\| | A ^ {- 1} | | r | \| _ {\infty}}{\| \widehat {x} \| _ {\infty}}, \tag {7.29}
$$

and is equal to it when $E|\widehat{x}| + f$ is a multiple of $|r|$ .

Proof. First note that $r = b - A\widehat{x}$ implies $|x - \widehat{x}| \leq |A^{-1}||r|$ , which implies (7.29). Now, for $z \geq 0$ ,

$$
| A ^ {- 1} | | r | = | A ^ {- 1} | \left(z _ {i} \frac {| r _ {i} |}{z _ {i}}\right) \leq \max  _ {i} \frac {| r _ {i} |}{| z _ {i} |} | A ^ {- 1} | z,
$$

with equality if $z$ is a multiple of $r$ . Taking $z = E|\widehat{x}| + f$ gives

$$
| A ^ {- 1} | | r | \leq \omega_ {E, f} (\widehat {x}) | A ^ {- 1} | (E | \widehat {x} | + f),
$$

with equality when $E|\hat{x}| + f$ is a multiple of $|r|$ . The truth of this statement is preserved when $\infty$ -norms are taken, so the result follows.

Since the bound (7.29) is obtained by taking absolute values in the equation $x - \widehat{x} = A^{-1}r$ , it is clearly the smallest possible such bound subject to ignoring signs in $A^{-1}$ and $r$ . It is reasonable to ask why we do not take $\| A^{-1}r\|_{\infty} / \| \widehat{x}\|_{\infty}$ as our error bound. (Theoretically it is an exact bound!) One reason is that we cannot compute $r$ or $\| A^{-1}r\|_{\infty}$ exactly. In place of $r$ we compute $\widehat{r} = fl(b - A\widehat{x})$ , and

$$
\widehat {r} = r + \Delta r, \quad | \Delta r | \leq \gamma_ {n + 1} (| A | | \widehat {x} | + | b |). \tag {7.30}
$$

Therefore a strict bound, and one that should be used in practice in place of (7.29), is

$$
\frac {\| x - \widehat {x} \| _ {\infty}}{\| \widehat {x} \| _ {\infty}} \leq \frac {\| | A ^ {- 1} | (\left| \widehat {r} \right| + \gamma_ {n + 1} (| A | | \widehat {x} | + | b |)) \| _ {\infty}}{\| \widehat {x} \| _ {\infty}}. \tag {7.31}
$$

Given an LU factorization of $A$ this bound can be cheaply estimated without computing $A^{-1}$ (see Chapter 15), and this is done by LAPACK's xyyRFS routines. Note also that if we did compute $A^{-1}r$ then we might as well apply a step of iterative refinement, which could well provide a more stable and accurate solution (see Chapter 12).

The LAPACK linear equation solvers estimate only one condition number: the standard condition number $\kappa_{1}(A)$ (or, rather, its reciprocal, referred to as rcond), which is returned by the xyyCON routines.

# 7.8. Perturbation Theory by Calculus

The perturbation results in this book are all derived algebraically, without any use of derivatives. Calculus can also be used to derive perturbation bounds, often in a straightforward fashion.

As a simple example, consider a linear system $A(t)x(t) = b(t)$ , where $A(t) \in \mathbb{R}^{n \times n}$ and $x(t), b(t) \in \mathbb{R}^n$ are assumed to be continuously differentiable functions of $t$ . Differentiating gives

$$
\dot {A} (t) x (t) + A (t) \dot {x} (t) = \dot {b} (t),
$$

or, dropping the $t$ arguments,

$$
\dot {x} = - A ^ {- 1} \dot {A} x + A ^ {- 1} \dot {b}.
$$

Taking norms, we obtain

$$
\frac {\| \dot {x} \|}{\| x \|} \leq \| A ^ {- 1} \| \| \dot {A} \| + \| A ^ {- 1} \| \frac {\| \dot {b} \|}{\| x \|} = \kappa (A) \left(\frac {\| \dot {A} \|}{\| A \|} + \frac {\| \dot {b} \|}{\| A \| \| x \|}\right). \tag {7.32}
$$

This bound shows that $\kappa(A)$ is a key quantity in measuring the sensitivity of a linear system. A componentwise bound could have been obtained just as easily.

To convert the bound (7.32) to the more standard form of perturbation bound we can choose $A(t) = A + tE$ , $b(t) = b + tf$ and write $x(\epsilon) = x(0) + \epsilon \dot{x}(0) + O(\epsilon^2)$ , which leads to a first-order version of the bound (7.4).

The calculus technique is a useful addition to the armoury of the error analyst (it is used by Golub and Van Loan [509, 1996], for example), but the algebraic approach is preferable for deriving rigorous perturbation bounds of the standard forms.

# 7.9. Notes and References

This chapter draws on the survey paper Higham [604, 1994].

Theorem 7.3 is due to Oettli and Prager [898, 1964], and predates the normwise backward error result Theorem 7.1 of Rigal and Gaches [986, 1967]. In addition to Theorem 7.1, Rigal and Gaches give a more general result based on norms of blocks that includes Theorems 7.3 and 7.1 as special cases. Theorem 7.1 is also obtained by Kovarik [749, 1976].

Theorems 7.1 and 7.3 both remain valid when $A$ is rectangular. Componentwise backward error for rectangular $A$ was considered by Oettli, Prager, and Wilkinson [899, 1965], but their results are subsumed by those of Oettli and Prager [898, 1964] and Rigal and Gaches [986, 1967].

For a linear system $Ax = b$ subject to componentwise perturbations, Oetli [897, 1965] shows how linear programming can be used to obtain bounds on the components of $x$ when all solutions of the perturbed system lie in the same orthant. Cope and Rust [271, 1979] extend this approach by showing, in general, how to bound all the solutions that lie in a given orthant. This type of analysis can also be found in the book by Kuperman [758, 1971], which includes an independent derivation of Theorem 7.3. See also Hartfiel [550, 1980].

Theorem 7.4 is a straightforward generalization of a result of Skeel [1040, 1979, Thms. 2.1 and 2.2]. It is clear from Bauer's comments in [91, 1966] that the bound (7.10), with $E = |A|$ and $f = |b|$ , was known to him, though he does not state the bound. This is the earliest reference we know in which componentwise analysis is used to derive forward perturbation bounds.

Theorem 7.8 is from Bauer [90, 1963]. Bauer actually states that equality holds in (7.24) for any $A$ , but his proof of equality is valid only when $|A^{-1}||A|$ and $|A||A^{-1}|$ have positive Perron vectors. Businger [187, 1968] proves that a sufficient condition for the irreducibility condition of Theorem 7.8 to hold (which, of course, implies the positivity of the Perron vectors) is that there do not exist permutations $P$ and $Q$ such that $PAQ$ is in block triangular form.

Theorem 7.7 is from Stewart and Sun [1083, 1990, Thm. 4.3.5].

Further results on scaling to minimize the condition number $\kappa(A)$ are given by Forsythe and Straus [432, 1955], Bauer [92, 1969], Golub and Varah [504, 1974], McCarthy and Strang [832, 1974], Shapiro [1033, 1982], [1034, 1985], [1035, 1991], and Watson [1209, 1991].

Chan and Foulser [213, 1988] introduce the idea of "effective conditioning" for linear systems, which takes into account the projections of $b$ onto the range space of $A$ . See Problem 7.5, and for an application to partial differential equations see Christiansen and Hansen [234, 1994].

For an example of how definitions of numerical stability for linear equation solvers can be extended to incorporate structure in the problem, see Bunch [179, 1987].

An interesting application of linear system perturbation analysis is to Markov chains. A discrete-time Markov chain can be represented by a square matrix $P$ , where $p_{ij}$ is the probability of a transition from state $i$ to state $j$ . Since state $i$ must lead to some other state, $\sum_{j} p_{ij} = 1$ , and these conditions can be written in matrix-vector form as

$$
P e = e. \tag {7.33}
$$

A nonnegative matrix satisfying (7.33) is called a stochastic matrix. The initial state of the Markov chain can be defined by a vector $z^T$ , where $z_i$ denotes the probability that the $i$ th state of the chain is occupied. Then the state of the chain at the next time unit is given by $z^T P$ . The steady state or stationary vector of the chain is given by

$$
\pi^ {T} = \lim  _ {k \rightarrow \infty} z ^ {T} P ^ {k}.
$$

An important question is the sensitivity of the individual components of the steady-state vector to perturbations in $P$ . This is investigated, for example, by Ipsen and Meyer [665, 1994], who measure the perturbation matrix normwise, and by O'Cinneide [896, 1993], who measures the perturbation matrix componentwise. For a matrix-oriented development of Markov chain theory see Berman and Plemmons [106, 1994].

It is possible to develop probabilistic perturbation theory for linear systems and other problems by making assumptions about the statistical distribution of the perturbations. We do not consider this approach here (though see Problem 7.14), but refer the interested reader to the papers by Fletcher [416, 1985], Stewart [1072, 1990], and Weiss, Wasilkowski, Wozniakowski, and Shub [1214, 1986].

# Problems

7.1. Under the conditions of Theorem 7.4, show that

$$
\left| x - y \right| \leq \epsilon (I - \epsilon | A ^ {- 1} | E) ^ {- 1} | A ^ {- 1} | (f + E | x |).
$$

Hence derive a first-order bound for $|x_i - y_i| / |x_i|$ .

7.2. Let $Ax = b$ , where $A \in \mathbb{R}^{n \times n}$ . Show that for any vector $y$ and any subordinate matrix norm,

$$
\frac {\| r \|}{\| A \| \| x \|} \leq \frac {\| x - y \|}{\| x \|} \leq \kappa (A) \frac {\| r \|}{\| A \| \| x \|},
$$

where the residual $r = b - Ay$ . Interpret this result.

7.3. Prove (7.16) and deduce (7.15).

7.4. Let $A \in \mathbb{R}^{n \times n}$ be symmetric positive definite and let $A = DHD$ , where $D = \mathrm{diag}(a_{ii}^{1/2})$ (this is the scaling used in Corollary 7.6). Show that $\operatorname{cond}(H) \leq \kappa_{\infty}(H) \leq n \operatorname{cond}(H)$ .   
7.5. (Chan and Foulser [213, 1988]) Let $A \in \mathbb{R}^{n \times n}$ have the SVD $A = U\Sigma V^T$ , where $\Sigma = \mathrm{diag}(\sigma_i)$ , $\sigma_1 \geq \dots \geq \sigma_n$ , and define the projection matrix $P_k := U_kU_k^T$ , where $U_k = U(:, n + 1 - k: n)$ . Show that if $Ax = b$ and $A(x + \Delta x) = (b + \Delta b)$ then

$$
\frac {\| \Delta x \| _ {2}}{\| x \| _ {2}} \leq \frac {\sigma_ {n + 1 - k}}{\sigma_ {n}} \frac {\| b \| _ {2}}{\| P _ {k} b \| _ {2}} \frac {\| \Delta b \| _ {2}}{\| b \| _ {2}}, \quad k = 1: n.
$$

What is the interpretation of this result?

7.6. (a) For the choice of tolerances $E = |A|ee^{T}$ , $f = |b|$ , corresponding to a row-wise backward error, show that

$$
\operatorname {c o n d} (A) \frac {\| x \| _ {1}}{\| x \| _ {\infty}} \leq \operatorname {c o n d} _ {E, f} (A, x) \leq 2 \operatorname {c o n d} (A) \frac {\| x \| _ {1}}{\| x \| _ {\infty}}.
$$

(b) For $E = e e^T |A|$ and $f = \| b \|_1 e$ , corresponding to a columnwise backward error, show that

$$
\| A ^ {- 1} \| _ {\infty} \frac {\| | A | | x | \| _ {1}}{\| x \| _ {\infty}} \leq \operatorname {c o n d} _ {E, f} (A, x) \leq 2 \| A ^ {- 1} \| _ {\infty} \frac {\| | A | | x | \| _ {1}}{\| x \| _ {\infty}}.
$$

7.7. Show that

$$
\begin{array}{l} \omega_ {| A |, | b |} (y) \leq \omega_ {| A |, 0} (y) \leq \frac {2 \omega_ {| A | , | b |} (y)}{1 - \omega_ {| A | , | b |} (y)}, \\ \eta_ {A, b} (y) \leq \eta_ {A, 0} (y) \leq \frac {2 \eta_ {A , b} (y)}{1 - \eta_ {A , b} (y)}. \\ \end{array}
$$

7.8. Let $A \in \mathbb{R}^{m \times n}$ and $b \in \mathbb{R}^m$ . Show that the normwise backward error defined in terms of a parameter $\theta \geq 0$ by

$$
\eta_ {F} (y) := \min  \left\{\| [ \Delta A, \theta \Delta b ] \| _ {F}: (A + \Delta A) y = b + \Delta b \right\}
$$

is given by

$$
\eta_ {F} (y) = \frac {\theta \| r \| _ {2}}{\sqrt {\theta^ {2} \| y \| _ {2} ^ {2} + 1}},
$$

where $r = b - Ay$ .

7.9. Let $A \in \mathbb{R}^{n \times n}$ be nonsingular. A componentwise condition number for the problem of computing $c^T x$ , where $Ax = b$ , can be defined by

$$
\begin{array}{l} \chi_ {E, f} (A, x) := \lim  _ {\epsilon \rightarrow 0} \sup  \left\{\frac {| c ^ {T} \Delta x |}{\epsilon | c ^ {T} x |}: (A + \Delta A) (x + \Delta x) = b + \Delta b, \right. \\ \left. \right.\left| \Delta A \right| \leq \epsilon E, \left.\left| \Delta b \right| \leq \epsilon f \right\}. \\ \end{array}
$$

Obtain an explicit formula for $\chi_{E,f}(A,x)$ . Show that $\chi_{E,f}(A,x) \geq 1$ if $E = |A|$ or $f = |b|$ . Derive the corresponding normwise condition number $\psi_{E,f}(A,x)$ , in which the constraints are $\| \Delta A \|_2 \leq \epsilon \| E \|_2$ and $\| \Delta b \|_2 \leq \epsilon \| f \|_2$ .

7.10. (Bauer [90, 1963]) Let $A, B, C \in \mathbb{R}^{n \times n}$ . (a) Prove that if $B$ and $C$ have positive elements then

$$
\min  _ {D _ {1}, D _ {2} \in \mathcal {D} _ {n}} \| D _ {1} B D _ {2} \| _ {\infty} \| D _ {2} ^ {- 1} C D _ {1} ^ {- 1} \| _ {\infty} = \rho (B C),
$$

where $\mathcal{D}_n = \{\mathrm{diag}(d_i):d_i > 0,i = 1:n\}$ . (Hint: consider $D_{1} = \mathrm{diag}(x_{1})^{-1}$ and $D_{2} = \mathrm{diag}(Cx_{1})$ , where $x_{1} > 0$ is a right Perron vector of $BC$ : $BCx_{1} = \rho (BC)x_{1}$ .)

(b) Deduce that if $|A|$ and $|A^{-1}|$ have positive entries, then

$$
\operatorname * {m i n} _ {D _ {1}, D _ {2} \in \mathcal {D} _ {n}} \kappa_ {\infty} (D _ {1} A D _ {2}) = \rho (| A | | A ^ {- 1} |).
$$

(c) Show that for any nonsingular $A$

$$
\inf  _ {D _ {1}, D _ {2} \in \mathcal {D} _ {n}} \kappa_ {\infty} (D _ {1} A D _ {2}) \leq \rho (| A | | A ^ {- 1} |).
$$

(d) Strengthen (b) by showing that for any nonsingular $A$ such that $|A||A^{-1}|$ and $|A^{-1}||A|$ are irreducible,

$$
\operatorname * {m i n} _ {D _ {1}, D _ {2} \in \mathcal {D} _ {n}} \kappa_ {\infty} (D _ {1} A D _ {2}) = \rho (| A | | A ^ {- 1} |).
$$

(e) What can you deduce about $\min_{D_1, D_2 \in \mathcal{D}_n} \kappa(D_1 AD_2)$ for the 1- and 2-norms?

7.11. (Bauer [91, 1966, p. 413], Rohn [989, 1989]) We can modify the definition of $\mu_E(A)$ in (7.25) by measuring $\Delta X$ componentwise relative to $X$ , giving

$$
\mu_ {E} ^ {\prime} (A) := \operatorname * {l i m} _ {\epsilon \to 0} \operatorname * {s u p} \Bigl \{\operatorname * {m a x} _ {i, j} \frac {| \varDelta x _ {i j} |}{\epsilon | x _ {i j} |}: | \varDelta A | \leq \epsilon E \Bigr \}
$$

(where $X = A^{-1}$ and $X + \Delta X = (A + \Delta A)^{-1}$ ). Show that

$$
\mu_ {E} ^ {\prime} (A) = \max _ {i j} \frac {\left(\left| A ^ {- 1} \right| E \left| A ^ {- 1} \right|\right) _ {i j}}{\left(\left| A ^ {- 1} \right|\right) _ {i j}}.
$$

7.12. Let $A \in \mathbb{R}^{n \times n}$ be symmetric and let $y$ be an approximate solution to $Ax = b$ . If $y$ has a small backward error, so that $y$ solves a nearby system, does it follow that $y$ solves a nearby symmetric system? This problem answers the question for both the normwise and componentwise relative backward errors.

(a) (Bunch, Demmel, and Van Loan [180, 1989]) Show that if $(A + G)y = b$ then there exists $H = H^T$ such that $(A + H)y = b$ with $\|H\|_2 \leq \|G\|_2$ and $\|H\|_F \leq \sqrt{2}\|G\|_F$ . (This result does not require $A = A^T$ .)   
(b) (Smoktunowicz [1053, 1995]) Show that if $A$ is symmetric and diagonally dominant and $(A + G)y = b$ with $|G| \leq \epsilon |A|$ , then there exists $H = H^T$ such that $(A + H)y = b$ with $|H| \leq 3\epsilon |A|$ . (For a general symmetric $A$ there may not exist such an $H$ , as is easily shown by a $2 \times 2$ example [574, 1992].)   
(c) (Smoktunowicz [1053, 1995]) Show that if $A$ is symmetric positive definite and $(A + G)y = b$ with $|G| \leq \epsilon |A|$ then there exists $H = H^T$ such that $(A + H)y = b$ with $|H| \leq (2n - 1)\epsilon |A|$ .

7.13. Suppose that $A \in \mathbb{R}^{n \times n}$ has $w_i$ nonzeros in its $i$ th row, $i = 1:n$ . Show that the inequality (7.31) can be replaced by

$$
\frac {\| x - \widehat {x} \| _ {\infty}}{\| \widehat {x} \| _ {\infty}} \leq \frac {\| \left. | A ^ {- 1} \right| \left(| \widehat {r} | + \Gamma (| A | | \widehat {x} | + | b |\)\right) \| _ {\infty}}{\| \widehat {x} \| _ {\infty}},
$$

where $\Gamma = \mathrm{diag}(\gamma_{w_{i + 1}})$ . This bound is potentially much smaller than (7.31) for large, sparse matrices.

7.14. (D. J. Higham, after Fletcher [416, 1985]) Suppose the nonsingular, square matrix $A$ is perturbed to $A + \Delta A$ and $b$ to $b + \Delta b$ . Then, to first order, the solution of $Ax = b$ is perturbed to $x + \Delta x$ , where

$$
\Delta x = - A ^ {- 1} \Delta A x + A ^ {- 1} \Delta b.
$$

Suppose that the perturbations have the form

$$
\Delta a _ {i j} = \epsilon_ {i j} e _ {i j}, \quad \Delta b _ {i} = \delta_ {i} f _ {i},
$$

where the $\epsilon_{ij}$ and $\delta_i$ are independent random variables, each having zero mean and variance $\sigma^2$ . (As usual, the matrix $E$ and vector $f$ represent fixed tolerances.) Let $\mathcal{E}$ denote the expected value.

(a) Show that

$$
\mathcal {E} (\| \varDelta x \| _ {2} ^ {2}) = \sigma^ {2} \| [ A ^ {- 1} ] [ E ] [ x ] + [ A ^ {- 1} ] [ f ] \| _ {1},
$$

where square brackets denote the operation of elementwise squaring: $[B]_{ij} = b_{ij}^2$ .

(b) Hence explain why

$$
\operatorname {c o n d e x p} (A, x) := \frac {\left(\| [ A ^ {- 1} ] [ E ] [ x ] + [ A ^ {- 1} ] [ f ] \| _ {1}\right) ^ {1 / 2}}{\| x \| _ {2}}
$$

may be regarded as an "expected condition number" for the linear system $Ax = b$ .

(c) For the case where $e_{ij} \equiv \| A\|_2$ and $f_j \equiv \| b\|_2$ , compare $\mathrm{condexp}(A,x)$ with the "worst-case" condition number $\kappa_{A,b}(A,x)$ for the 2-norm.

7.15. (Horn and Johnson [637, 1991, p. 331]) Prove that for any nonsingular $A \in \mathbb{R}^{n \times n}$ ,

$$
\operatorname * {i n f} _ {D _ {1}, D _ {2} \in \mathcal {D} _ {n}} \kappa_ {2} (D _ {1} A D _ {2}) \geq \| A \circ A ^ {- T} \| _ {2},
$$

where $\circ$ is the Hadamard product $(A \circ B = (a_{ij}b_{ij}))$ and $\mathcal{D}_n$ is defined as in Problem 7.10. (Hint: use the inequality $\| A \circ B \|_2 \leq \| A \|_2 \| B \|_2$ .) Discuss the attainability of this bound.
