# Chapter 21

# Underdetermined Systems

I'm thinking of two numbers.

Their average is 3.

What are the numbers?

— CLEVE B. MOLER, The World's Simplest Impossible Problem (1990)

This problem arises in important algorithms used in mathematical programming ...

In these cases, $B$ is usually very large and sparse and,

because of storage difficulties,

it is often uneconomical to store and access $Q_{1} \ldots$

Sometimes it has been thought that [the seminormal equations method]

could be disasterously worse than [the $Q$ method] ...

It is the purpose of this note to show that such algorithms are

numerically quite satisfactory.

— C. C. PAIGE, An Error Analysis of a Method for Solving Matrix Equations (1973)

Having considered well-determined and overdetermined linear systems, we now turn to the remaining class of linear systems: those that are underdetermined.

# 21.1. Solution Methods

Consider the underdetermined system $Ax = b$ , where $A \in \mathbb{R}^{m \times n}$ with $m \leq n$ . The system can be analysed using a QR factorization

$$
A ^ {T} = Q \left[ \begin{array}{l} R \\ 0 \end{array} \right], \tag {21.1}
$$

where $Q \in \mathbb{R}^{n \times n}$ is orthogonal and $R \in \mathbb{R}^{m \times m}$ is upper triangular. (We could, alternatively, use an LQ factorization of $A$ , but we will keep to the standard notation.) We have

$$
b = A x = \left[ \begin{array}{l l} R ^ {T} & 0 \end{array} \right] Q ^ {T} x = R ^ {T} y _ {1}, \tag {21.2}
$$

where

$$
y = \left[ \begin{array}{c} y _ {1} \\ y _ {2} \end{array} \right] = Q ^ {T} x, \qquad y _ {1} \in \mathbb {R} ^ {m}.
$$

If $A$ has full rank then $y_{1} = R^{-T}b$ is uniquely determined and all solutions of $Ax = b$ are given by

$$
x = Q \left[ \begin{array}{c} y _ {1} \\ y _ {2} \end{array} \right], \quad y _ {2} \in \mathbb {R} ^ {n - m} \text {a r b i t r a r y}.
$$

The unique solution $x_{LS}$ that minimizes $\| x\| _2$ is obtained by setting $y_{2} = 0$ . We have

$$
\begin{array}{l} x _ {L S} = Q \left[ \begin{array}{c} R ^ {- T} b \\ 0 \end{array} \right] (21.3) \\ = Q \left[ \begin{array}{l} R \\ 0 \end{array} \right] R ^ {- 1} R ^ {- T} b = Q \left[ \begin{array}{l} R \\ 0 \end{array} \right] \left(R ^ {T} R\right) ^ {- 1} b (21.4) \\ = A ^ {T} \left(A A ^ {T}\right) ^ {- 1} b \\ = A ^ {+} b, \\ \end{array}
$$

where $A^{+} = A^{T}(AA^{T})^{-1}$ is the pseudo-inverse of $A$ . Hence $x_{LS}$ can be characterized as $x_{LS} = A^{T}y$ , where $y$ solves the normal equations $AA^{T}y = b$ .

Equation (21.3) defines one way to compute $x_{LS}$ . We will refer to this method as the "Q method". When $A$ is large and sparse it is desirable to avoid storing and accessing $Q$ , which can be expensive. An alternative method with this property uses the QR factorization (21.1) but computes $x_{LS}$ as $x_{LS} = A^T y$ , where

$$
R ^ {T} R y = b \tag {21.5}
$$

(cf. (21.4)). These latter equations are called the seminormal equations (SNE). As the "semi" denotes, however, this method does not explicitly form $AA^T$ , which would be undesirable from the standpoint of numerical stability. Note that equations (21.5) are different from the equations $R^T R x = A^T b$ for an overdetermined least squares (LS) problem, where $A = Q[R^T 0]^T \in \mathbb{R}^{m \times n}$ with $m \geq n$ , which are also called seminormal equations (see §20.6).

# 21.2. Perturbation Theory and Backward Error

A componentwise perturbation result for the minimum 2-norm solution to an underdetermined system is readily obtained.

Theorem 21.1 (Demmel and Higham). Let $A \in \mathbb{R}^{m \times n}$ ( $m \leq n$ ) be of full rank and $0 \neq b \in \mathbb{R}^m$ . Suppose $\| A^+ \Delta A \|_2 < 1$ and

$$
| \Delta A | \leq \epsilon E, \quad | \Delta b | \leq \epsilon f.
$$

If $x$ and $y$ are the minimum 2-norm solutions to $Ax = b$ and $(A + \Delta A)y = b + \Delta b$ , respectively, then, for any absolute norm,

$$
\frac {\| x - y \|}{\| x \|} \leq \left(\| | I - A ^ {+} A | \cdot E ^ {T} \cdot | A ^ {+ T} x | \| + \| | A ^ {+} | \cdot (f + E | x |) \|\right) \frac {\epsilon}{\| x \|} + O \left(\epsilon^ {2}\right). \tag {21.6}
$$

For any Hölder $p$ -norm, the bound is attainable to within a constant factor depending on $n$ .

Proof. The perturbed matrix $A + \Delta A = A(I + A^{+}\Delta A)$ has full rank, so we can manipulate the equation

$$
y = \left(A + \varDelta A\right) ^ {T} \left(\left(A + \varDelta A\right) \left(A + \varDelta A\right) ^ {T}\right) ^ {- 1} (b + \varDelta b)
$$

to obtain

$$
\begin{array}{l} y - x = \left(I - A ^ {+} A\right) \Delta A ^ {T} \left(A A ^ {T}\right) ^ {- 1} b + A ^ {+} (\Delta b - \Delta A x) + O \left(\epsilon^ {2}\right) \\ = (I - A ^ {+} A) \Delta A ^ {T} A ^ {+ T} x + A ^ {+} (\Delta b - \Delta A x) + O \left(\epsilon^ {2}\right). \tag {21.7} \\ \end{array}
$$

The required bound follows on using absolute value inequalities and taking norms. That the bound is attained to within a constant factor depending on $n$ for Hölder $p$ -norms is a consequence of the fact that the two vectors on the right-hand side of (21.7) are orthogonal.

Two special cases are worth noting, for later use. We will use the equality $\| I - A^{+}A\|_{2} = \min \{1,n - m\}$ , which can be derived by consideration of the QR factorization (21.1), for example. If $E = |A|H$ , where $H$ is a given nonnegative matrix, and $f = |b|$ , then we can put (21.6) in the form

$$
\frac {\| x - y \| _ {2}}{\| x \| _ {2}} \leq \min  \{3, n - m + 2 \} \max  \left\{\| H \| _ {2}, 1 \right\} \operatorname {c o n d} _ {2} (A) \epsilon + O \left(\epsilon^ {2}\right), \tag {21.8}
$$

where

$$
\operatorname {c o n d} _ {2} (A) = \left\| | A ^ {+} | | A | \right\| _ {2}.
$$

Note that $\operatorname{cond}_2(A)$ is independent of the row scaling of $A$ ( $\operatorname{cond}_2(DA) = \operatorname{cond}_2(A)$ for nonsingular diagonal $D$ ). If $E = \|A\|_2 e_m e_n^T$ and $f = \|b\|_2 e_m$ , where $e_m$ denotes the $m$ -dimensional vector of 1s, then

$$
\frac {\| x - y \| _ {2}}{\| x \| _ {2}} \leq \min  \{3, n - m + 2 \} (m n) ^ {1 / 2} \kappa_ {2} (A) \epsilon + O (\epsilon^ {2}). \tag {21.9}
$$

The following analogue of Lemma 20.6 will be needed for the error analysis in the next section. It says that if we perturb the two occurrences of $A$ in the normal equations $AA^T x = b$ differently, then the solution of the perturbed system is the solution of normal equations in which there is only one perturbation of $A$ and, moreover, this single perturbation is no larger, in the normwise or row-wise sense, than the two perturbations we started with.

Lemma 21.2 (Kielbasiński and Schwetlick). Let $A \in \mathbb{R}^{m \times n}$ ( $m \leq n$ ) be of full rank and suppose

$$
\left(A + \Delta A _ {1}\right) \bar {x} = b, \quad \bar {x} = \left(A + \Delta A _ {2}\right) ^ {T} \bar {y}.
$$

Assume that $3\max \big(\| A^{+}\varDelta A_{1}\|_{2},\| A^{+}\varDelta A_{2}\|_{2}\big) < 1$ . Then there is a vector $\widetilde{y}$ and a perturbation $\varDelta A$ with

$$
\varDelta A = \varDelta A _ {1} G _ {1} + \varDelta A _ {2} G _ {2}, \qquad G _ {1} ^ {T} = G _ {1} = G _ {1} ^ {2}, \quad G _ {1} + G _ {2} = I,
$$

such that

$$
(A + \varDelta A) \overline {{x}} = b, \qquad \overline {{x}} = (A + \varDelta A) ^ {T} \widetilde {y},
$$

that is, $\overline{x}$ is the minimum 2-norm solution to $(A + \Delta A)x = b$ .

Proof. The proof is similar to that of Lemma 20.6, but differs in some details. If $\overline{x} = (A + \Delta A_2)^T\overline{y} = 0$ we take $\Delta A = \Delta A_2$ . Otherwise, we set

$$
\Delta A := \Delta A _ {1} P + \Delta A _ {2} (I - P) =: \Delta A _ {2} + H P,
$$

where $P = \overline{x}\overline{x}^T /\overline{x}^T\overline{x}$ and $H = \varDelta A_{1}-\varDelta A_{2}$ . We have

$$
\left(A + \Delta A\right) ^ {T} \bar {y} = \left(A + \Delta A _ {2} + H P\right) ^ {T} \bar {y} = \beta \bar {x},
$$

where $\beta = 1 + \overline{x}^T H^T \overline{y} / \overline{x}^T \overline{x}$ , which shows that we need to set $\widetilde{y} = \beta^{-1} \overline{y}$ . To check that $(A + \Delta A) \overline{x} = b$ , we evaluate

$$
\begin{array}{l} (A + \varDelta A) \overline {{x}} = (A + \varDelta A _ {1} + H (P - I)) \overline {{x}} \\ = (A + \Delta A _ {1}) \bar {x} = b, \\ \end{array}
$$

as required. The vector $\widetilde{y}$ is undefined if $\beta = 0$ . But

$$
\begin{array}{l} \beta = 1 + \frac {\overline {{x}} ^ {T} H ^ {T} \overline {{y}}}{\overline {{x}} ^ {T} \overline {{x}}} = 1 + \frac {\overline {{x}} ^ {T} H ^ {T} (A + \Delta A _ {2}) ^ {+ T} \overline {{x}}}{\overline {{x}} ^ {T} \overline {{x}}} \\ \geq 1 - \left\| \left(A + \Delta A _ {2}\right) ^ {+} H \right\| _ {2} \\ \geq 1 - \frac {\| A ^ {+} H \| _ {2}}{1 - \| A ^ {+} \Delta A _ {2} \| _ {2}} \quad (\text {i f} \| A ^ {+} \Delta A _ {2} \| _ {2} <   1) \\ \geq 1 - \frac {\left(\| A ^ {+} \Delta A _ {1} \| _ {2} + \| A ^ {+} \Delta A _ {2} \| _ {2}\right)}{1 - \| A ^ {+} \Delta A _ {2} \| _ {2}}, \\ \end{array}
$$

which is positive if $3\max \bigl (\| A^{+}\varDelta A_{1}\|_{2},\| A^{+}\varDelta A_{2}\|_{2}\bigr) < 1$

Note that in Lemma 21.2 we have the normwise bound

$$
\left\| \varDelta A \right\| _ {p} \leq \left(\left\| \varDelta A _ {1} \right\| _ {p} ^ {2} + \left\| \varDelta A _ {2} \right\| _ {p} ^ {2}\right) ^ {1 / 2}, \quad p = 2, F.
$$

A normwise backward error formula for an arbitrary approximate minimum 2-norm solution is given by the following result.

Theorem 21.3 (Sun and Sun). Let $A \in \mathbb{R}^{m \times n}$ ( $m \leq n$ ), $b \in \mathbb{R}^m$ , and $r = b - Ay$ . The normwise backward error

$\eta_F(y) \coloneqq \min \{ \| [\Delta A, \theta \Delta b] \|_F : y \text{ is the minimum 2-norm solution to}$

$$
(A + \Delta A) y = b + \Delta b \}
$$

is given by $\eta_F(0) = \theta \| b\| _2$ and, for $y\neq 0$

$$
\eta_ {F} (y) = \sqrt {\frac {\theta^ {2} \| y \| _ {2} ^ {2}}{1 + \theta^ {2} \| y \| _ {2} ^ {2}} \cdot \frac {\| r \| _ {2} ^ {2}}{\| y \| _ {2} ^ {2}} + \sigma_ {m} ^ {2} \big (A (I - y y ^ {+}) \big)}. \qquad \square
$$

Note that if $m = n$ then $\sigma_{m}(A(I - yy^{+})) = 0$ and the formula in the theorem reduces to the formula in Problem 7.8 for linear systems.

# 21.3. Error Analysis

We now consider the stability of the Q method and the SNE method. For both methods we assume that the QR factorization is computed using Householder or Givens transformations.

Before presenting the results we define a measure of stability. The row-wise backward error for a minimum-norm underdetermined system $Ax = b$ is defined as

$$
\begin{array}{l} \omega^ {R} (y) := \min  \{\epsilon : \exists \Delta A \in \mathbb {R} ^ {m \times n}, \Delta b \in \mathbb {R} ^ {m} \text {w i t h} \\ \left\| \Delta A (i,:) \right\| _ {2} \leq \epsilon \| A (i,:) \| _ {2} \text {a n d} | \Delta b _ {i} | \leq \epsilon | b _ {i} |, i = 1: n, \\ s. t. y \text {i s} (A + \Delta A) y = b + \Delta b \}. \\ \end{array}
$$

Note the requirement in this definition that $y$ be the minimum norm solution; the usual row-wise backward error $\omega_{|A|ee^T,|b|}(y)$ (see (7.7)) is a generally smaller quantity. Let us say that a method is row-wise backward stable if it produces a computed solution $\hat{x}$ for which the row-wise backward error $\omega^R (\hat{x})$ is of order $u$ .

Theorem 21.4. Let $A \in \mathbb{R}^{m \times n}$ with $\operatorname{rank}(A) = m \leq n$ , and assume that a condition of the form $\operatorname{cond}_2(A) mn \gamma_n < 1$ holds. Suppose the underdetermined system $Ax = b$ is solved in the minimum 2-norm sense using the $Q$ method. Then the computed solution $\widehat{x}$ is the minimum 2-norm solution to $(A + \Delta A)x = b$ , where

$$
\| \Delta A (i,:) \| _ {2} \leq \tilde {\gamma} _ {m n} \| A (i,:) \| _ {2}, \quad i = 1: m.
$$

Proof. The $\mathbf{Q}$ method solves the triangular system $R^T y_1 = b$ and then forms $x = Q[y_1^T, 0]^T$ . Assuming the use of Householder QR factorization, from Theorem 19.4 we have that

$$
\left(A + \varDelta A _ {0}\right) ^ {T} = Q \left[ \begin{array}{c} \widehat {R} \\ 0 \end{array} \right],
$$

for some orthogonal matrix $Q$ , where $\| \Delta A_0(i, :) \|_2 \leq \tilde{\gamma}_{mn} \| A(i, :) \|_2$ , $i = 1: m$ . The computed $\widehat{y}_1$ satisfies

$$
\left(\widehat {R} + \varDelta \widehat {R}\right) ^ {T} \widehat {y} _ {1} = b, \qquad | \varDelta \widehat {R} | \leq \gamma_ {m} | \widehat {R} |.
$$

From Lemma 19.3, the computed solution $\widehat{x}$ satisfies

$$
\widehat {x} = \left(Q + \varDelta Q\right) \left[ \begin{array}{c} \widehat {y} _ {1} \\ 0 \end{array} \right], \qquad \| \varDelta Q \| _ {F} \leq m \widetilde {\gamma} _ {n}. \qquad \qquad (2 1. 1 0)
$$

We now rewrite the latter two equations in such a way that we can apply Lemma 21.2:

$$
\begin{array}{l} (A + \varDelta A _ {1}) \widehat {\boldsymbol {x}} := \left[ \begin{array}{l l} (\widehat {R} + \varDelta \widehat {R}) ^ {T} & 0 \end{array} \right] (Q + \varDelta Q) ^ {- 1} \cdot (Q + \varDelta Q) \left[ \begin{array}{l} \widehat {y} _ {1} \\ 0 \end{array} \right] = b, \\ \widehat {x} = (Q + \varDelta Q) \left[ \begin{array}{c} \widehat {R} \\ 0 \end{array} \right] \cdot \widehat {R} ^ {- 1} \widehat {y} _ {1} =: (A + \varDelta A _ {2}) ^ {T} \overline {{y}}. \\ \end{array}
$$

It is straightforward to show that

$$
\| \Delta A _ {k} (i,:) \| _ {2} \leq \tilde {\gamma} _ {m n} \| A (i,:) \| _ {2}, \quad i = 1: m, \quad k = 1: 2.
$$

The result follows on invocation of Lemma 21.2.

Theorem 21.4 says that the Q method is row-wise backward stable. This is not altogether surprising, since (Householder or Givens) QR factorization for the LS problem enjoys an analogous backward stability result (Theorem 20.3), albeit without the restriction of a minimum norm solution. Applying (21.8) to Theorem 21.4 with $H = e e^T$ we obtain the forward error bound

$$
\frac {\| \widehat {x} - x \| _ {2}}{\| x \| _ {2}} \leq n \widetilde {\gamma} _ {m n} \operatorname {c o n d} _ {2} (A) + O (u ^ {2}). \tag {21.11}
$$

The same form of forward error bound (21.11) can be derived for the SNE method [325, 1993]. However, it is not possible to obtain a result analogous to Theorem 21.4, nor even to obtain a residual bound of the form $\|b - A\widehat{x}\|_2 \leq c_{m,n}u\|A\|_2\|\widehat{x}\|_2$ (which would imply that $\widehat{x}$ solved a nearby system, though $\widehat{x}$ would not necessarily be the minimum norm solution). The method of solution guarantees only that the seminormal equations themselves have a small residual. Thus, as in the context of overdetermined LS problems, the SNE method is not backward stable. A possible way to improve the stability is by iterative refinement, as shown in [325, 1993].

Note that the forward error bound (21.11) is independent of the row scaling of $A$ , since $\mathrm{cond}_2(A)$ is. The bound is therefore potentially much smaller than the bound

$$
\frac {\| x - \widehat {x} \| _ {2}}{\| x \| _ {2}} \leq c _ {m, n} u \kappa_ {2} (A) + O (u ^ {2}),
$$

Table 21.1. Backward errors for underdetermined Vandermonde system.   

<table><tr><td></td><td>ηF/|[A,b]||F (θ=1)</td></tr><tr><td>Householder QR</td><td>1.6 × 10-17</td></tr><tr><td>MGS with x := Qy</td><td>1.8 × 10-3</td></tr><tr><td>MGS with x formed stably (see text)</td><td>3.4 × 10-17</td></tr><tr><td>SNE method (using Householder QR)</td><td>4.7 × 10-14</td></tr></table>

obtained by Paige [911, 1973] for the SNE method and by Jennings and Osborne [675, 1974] and Arioli and Laratta [32, 1985, Thm. 4] for the Q method.

Finally, we mention an alternative version of the Q method that is based on the modified Gram-Schmidt (MGS) method. The obvious approach is to compute the QR factorization $A^T = QR$ using MGS ( $Q \in \mathbb{R}^{n \times m}$ , $R \in \mathbb{R}^{m \times m}$ ), solve $R^T y = b$ , and then form $x = Qy$ . Since $Q$ is provided explicitly by the MGS method, the final stage is a full matrix-vector multiplication, unlike for the Householder method. However, because the computed $\widehat{Q}$ may depart from orthonormality, this method is unstable in the form described. The formation of $x = Qy$ should instead be done as follows:

$$
\begin{array}{l} x ^ {(n)} = 0 \\ f o r k = n: - 1: 1 \\ \alpha_ {k} = q _ {k} ^ {T} x ^ {(k)} \\ x ^ {(k - 1)} = x ^ {(k)} - \left(\alpha_ {k} - y _ {k}\right) q _ {k} \\ \end{array}
$$

$$
\begin{array}{l} e n d \\ x = x ^ {(0)} \\ \end{array}
$$

The recurrence can be written as $x^{(k-1)} = x^{(k)} + y_k q_k - (q_k^T x^{(k)}) q_k$ , and the last term is zero in exact arithmetic if the $q_k$ are mutually orthogonal. In finite precision arithmetic this correction term has the "magical" effect of making the algorithm stable, in the sense that it satisfies essentially the same result as the Q method in Theorem 21.4; see Björck and Paige [132, 1994].

A numerical example is instructive. Take the $20 \times 30$ Vandermonde matrix $A = (p_i^{j-1})$ , where the $p_i$ are equally spaced on $[0,1]$ , and let $b$ have elements equally spaced on $[0,1]$ . The condition number $\mathrm{cond}_2(A) = 7.6 \times 10^{12}$ . The backward error from Theorem 21.3 is shown in Table 21.1. For $A^T$ , the $\widehat{Q}$ supplied by MGS satisfies $\| \widehat{Q}^T \widehat{Q} - I \|_2 = 9 \times 10^{-3}$ , which explains the instability of the "obvious" MGS solver.

# 21.4. Notes and References

The seminormal equations method was suggested by Gill and Murray [482, 1973] and Saunders [1011, 1972]. Other methods for obtaining minimal 2-norm solutions of underdetermined systems are surveyed by Cline and Plemmons [246, 1976].

Theorem 21.1 is from Demmel and Higham [325, 1993]. The bound (21.9) is well known; it follows from Wedin's original version of our Theorem 20.1, which

applies to minimum 2-norm underdetermined problems as well as LS problems.

Theorem 21.3 is from Sun and Sun [1110, 1997] and solves a research problem posed in the first edition of this book.

Theorem 21.4 first appeared in the first edition of this book. Demmel and Higham [325, 1993] prove the weaker result that $\widehat{x}$ from the Q method is very close to a vector $\overline{x}$ that satisfies the criterion for row-wise backward stability, and Lawson and Hanson [775, 1995, Thm. 16.18] give a corresponding result in which $\overline{x}$ satisfies the criterion for general normwise backward stability. The key to showing actual backward stability is the use of Kielbasinski and Schwetlick's lemma, which is a modification of Lemma 8.2.11 in [734, 1988] and [735, 1992] (our Lemma 20.6). Demmel and Higham [325, 1993] also give error analysis for the seminormal equations method.

The new MGS algorithm for solving the minimum norm problem was first suggested by Björck and Paige [131, 1992]; see also Björck [127, 1994].

Arioli and Laratta [33, 1986] give error analysis of QR factorization methods for solving the general problem $\min \{\| x - c\| _2:Ax = b\}$ , where $A\in \mathbb{R}^{m\times n}$ with $m\leq n$ .

# 21.4.1. LAPACK

The same routines that solve the (overdetermined) LS problem also solve underdetermined systems for the solution of minimal 2-norm. Thus, xGELS solves a full rank underdetermined system with multiple right-hand sides by the Q method. Routines xGELSY and xGELSS solve rank-deficient problems with multiple right-hand sides, using, respectively, a complete orthogonal factorization (computed via QR factorization with column pivoting) and the singular value decomposition.

# Problems

21.1. (Björck [126, 1992]) Show that the system

$$
\left[ \begin{array}{l l} I & A \\ A ^ {T} & 0 \end{array} \right] \left[ \begin{array}{l} y \\ x \end{array} \right] = \left[ \begin{array}{l} b \\ c \end{array} \right] \tag {21.12}
$$

characterizes the solution to the following generalizations of the LS problem and the problem of finding the minimum norm solution to an underdetermined system:

$$
\min  _ {x} \| b - A x \| _ {2} ^ {2} + 2 c ^ {T} x, \tag {21.13}
$$

$$
\min  _ {y} \| y - b \| _ {2} \quad \text {s u b j e c t} \quad A ^ {T} y = c. \tag {21.14}
$$
