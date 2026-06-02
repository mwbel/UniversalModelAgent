# Chapter 8 Triangular Systems

In the end there is left the coefficient of one unknown and the constant term. An elimination between this equation and one from the previous set that contains two unknowns yields an equation with the coefficient of another unknown and another constant term, etc. The quotient of the constant term by the unknown yields the value of the unknown in each case. — JOHN V. ATANASOFF, Computing Machine for the Solution of Large Systems of Linear Algebraic Equations (1940)   
The solutions of triangular systems are usually computed to high accuracy. This fact ... cannot be proved in general, for counter examples exist. However, it is true of many special kinds of triangular matrices and the phenomenon has been observed in many others. The practical consequences of this fact cannot be over-emphasized. — G. W. STEWART, Introduction to Matrix Computations (1973)   
In practice one almost invariably finds that if $L$ is ill-conditioned, so that $\| L\| \| L^{-1}\| \gg 1$ , then the computed solution of $Lx = b$ (or the computed inverse) is far more accurate than [standard norm bounds] would suggest. — J. H. WILKINSON, Rounding Errors in Algebraic Processes (1963)

Triangular systems play a fundamental role in matrix computations. Many methods are built on the idea of reducing a problem to the solution of one or more triangular systems, including virtually all direct methods for solving linear systems. On serial computers triangular systems are universally solved by the standard back and forward substitution algorithms. For parallel computation there are several alternative methods, one of which we analyse in §8.4.

Backward error analysis for the substitution algorithms is straightforward and the conclusion is well known: the algorithms are extremely stable. The behaviour of the forward error, however, is intriguing, because the forward error is often surprisingly small—much smaller than we would predict from the normwise condition number $\kappa$ , or, sometimes, even the componentwise condition number cond. The quotes from Stewart and Wilkinson at the start of this chapter emphasize the high accuracy that is frequently observed in practice. The analysis we give in this chapter provides a partial explanation for the observed accuracy of the substitution algorithms. In particular, it reveals three important but nonobvious properties:

- the accuracy of the computed solution from substitution depends strongly on the right-hand side;   
- a triangular matrix may be much more or less ill conditioned than its transpose; and   
- the use of pivoting in LU, QR, and Cholesky factorizations can greatly improve the conditioning of a resulting triangular system.

As well as deriving backward and forward error bounds, we show how to compute upper and lower bounds for the inverse of a triangular matrix.

# 8.1. Backward Error Analysis

Recall that for an upper triangular matrix $U \in \mathbb{R}^{n \times n}$ the system $Ux = b$ can be solved using the formula $x_{i} = (b_{i} - \sum_{j=i+1}^{n} u_{ij}x_{j}) / u_{ii}$ , which yields the components of $x$ in order from last to first.

Algorithm 8.1 (back substitution). Given a nonsingular upper triangular matrix $U \in \mathbb{R}^{n \times n}$ this algorithm solves the system $Ux = b$ .

$$
\begin{array}{l} x _ {n} = b _ {n} / u _ {n n} \\ f o r i = n - 1: - 1: 1 \\ s = b _ {i} \\ f o r j = i + 1: n \\ s = s - u _ {i j} x _ {j} \\ e n d \\ x _ {i} = s / u _ {i i} \\ e n d \\ \end{array}
$$

Cost: $n^2$ flops.

We will not state the analogous algorithm for solving a lower triangular system, forward substitution. All the results below for back substitution have obvious analogues for forward substitution. Throughout this chapter $T$ denotes a matrix that can be upper or lower triangular.

To analyse the errors in substitution we need the following lemma.

Lemma 8.2. Let $y = (c - \sum_{i=1}^{k-1} a_i b_i) / b_k$ be evaluated in floating point arithmetic according to

$$
\begin{array}{l} s = c \\ f o r i = 1: k - 1 \\ s = s - a _ {i} b _ {i} \\ e n d \\ y = s / b _ {k} \\ \end{array}
$$

Then the computed $\widehat{y}$ satisfies

$$
b _ {k} \widehat {y} \left(1 + \theta_ {k}\right) = c - \sum_ {i = 1} ^ {k - 1} a _ {i} b _ {i} \left(1 + \theta_ {i}\right), \tag {8.1}
$$

where $|\theta_i| \leq \gamma_i = i u / (1 - i u)$ .

Proof. Analysis very similar to that leading to (3.2) shows that $\widehat{s} := f l(c - \sum_{i=1}^{k-1} a_i b_i)$ satisfies

$$
\widehat {s} = c \left(1 + \delta_ {1}\right) \dots \left(1 + \delta_ {k - 1}\right) - \sum_ {i = 1} ^ {k - 1} a _ {i} b _ {i} \left(1 + \epsilon_ {i}\right) \left(1 + \delta_ {i}\right) \dots \left(1 + \delta_ {k - 1}\right),
$$

where $|\epsilon_i|, |\delta_i| \leq u$ . The final division yields, using (2.5), $\widehat{y} = fl(\widehat{s} / b_k) = \widehat{s} / (b_k(1 + \delta_k))$ , $|\delta_k| \leq u$ , so that, after dividing through by $(1 + \delta_1) \dots (1 + \delta_{k-1})$ , we have

$$
b _ {k} \widehat {y} \frac {1 + \delta_ {k}}{(1 + \delta_ {1}) \dots (1 + \delta_ {k - 1})} = c - \sum_ {i = 1} ^ {k - 1} a _ {i} b _ {i} \frac {1 + \epsilon_ {i}}{(1 + \delta_ {1}) \dots (1 + \delta_ {i - 1})}.
$$

The result is obtained on invoking Lemma 3.1.

Two remarks are in order. First, we chose the particular form of (8.1), in which $c$ is not perturbed, in order to obtain a backward error result for $Ux = b$ in which $b$ is not perturbed. Second, we carefully kept track of the terms $1 + \delta_{i}$ in the proof, so as to obtain the best possible constants. Direct application of the lemma to Algorithm 8.1 yields a backward error result.

Theorem 8.3. The computed solution $\widehat{x}$ from Algorithm 8.1 satisfies

$$
(U + \Delta U) \widehat {x} = b, \qquad | \Delta u _ {i j} | \leq \left\{ \begin{array}{l l} \gamma_ {n - i + 1} | u _ {i i} |, & i = j, \\ \gamma_ {| i - j |} | u _ {i j} |, & i \neq j. \end{array} \right. \qquad \square
$$

Theorem 8.3 holds only for the particular ordering of arithmetic operations used in Algorithm 8.1. A result that holds for any ordering is a consequence of the next lemma.

Lemma 8.4. If $y = (c - \sum_{i=1}^{k-1} a_i b_i) / b_k$ is evaluated in floating point arithmetic, then, no matter what the order of evaluation,

$$
b _ {k} \widehat {y} (1 + \theta_ {k} ^ {(0)}) = c - \sum_ {i = 1} ^ {k - 1} a _ {i} b _ {i} (1 + \theta_ {k} ^ {(i)}),
$$

where $|\theta_k^{(i)}| \leq \gamma_k$ for all $i$ . If $b_k = 1$ , so that there is no division, then $|\theta_k^{(i)}| \leq \gamma_{k - 1}$ for all $i$ .

Proof. The result is not hard to see after a little thought, but a formal proof is tedious to write down. Note that the ordering used in Lemma 8.2 is the one for which this lemma is least obvious! The last part of the lemma is useful when analysing unit lower triangular systems, and in various other contexts. $\square$

Theorem 8.5. Let the triangular system $Tx = b$ , where $T \in \mathbb{R}^{n \times n}$ is nonsingular, be solved by substitution, with any ordering. Then the computed solution $\widehat{x}$ satisfies

$$
(T + \Delta T) \widehat {x} = b, \quad | \Delta T | \leq \gamma_ {n} | T |. \quad \square
$$

In technical terms, this result says that $\widehat{x}$ has a tiny componentwise relative backward error. In other words, the backward error is about as small as we could possibly hope.

In most of the remaining error analyses in this book, we will derive results that, like the one in Theorem 8.5, do not depend on the ordering of the arithmetic operations. Results of this type are more general, usually no less informative, and easier to derive, than ones that depend on the ordering. However, it is important to realise that the actual error does depend on the ordering, possibly strongly so for certain data. This point is clear from Chapter 4 on summation.

# 8.2. Forward Error Analysis

From Theorems 8.5 and 7.4 there follows the forward error bound

$$
\frac {\| x - \widehat {x} \| _ {\infty}}{\| x \| _ {\infty}} \leq \frac {\operatorname {c o n d} (T , x) \gamma_ {n}}{1 - \operatorname {c o n d} (T) \gamma_ {n}}, \tag {8.2}
$$

where

$$
\operatorname {c o n d} (T, x) = \frac {\| | T ^ {- 1} | | T | | x | \| _ {\infty}}{\| x \| _ {\infty}}, \quad \operatorname {c o n d} (T) = \| | T ^ {- 1} | | T | \| _ {\infty}.
$$

This bound can, of course, be arbitrarily smaller than the corresponding bound involving $\kappa_{\infty}(T) = \| T\|_{\infty}\| T^{-1}\|_{\infty}$ , for the reasons explained in Chapter 7. For further insight, note that, in terms of the traditional condition number, $\kappa (T)$ , ill conditioning of a triangular matrix stems from two possible sources: variation in the size of the diagonal elements and rows with off-diagonal elements which are large relative to the diagonal elements. Significantly, because of its row scaling invariance, $\operatorname{cond}(T,x)$ is susceptible only to the second source.

Despite its pleasing properties, $\operatorname{cond}(T,x)$ can be arbitrarily large. This is illustrated by the upper triangular matrix

$$
U (\alpha) = \left(u _ {i j}\right), \quad u _ {i j} = \left\{ \begin{array}{l l} 1, & i = j, \\ - \alpha , & i <   j, \end{array} \right. \tag {8.3}
$$

for which

$$
\left(U (\alpha) ^ {- 1}\right) _ {i j} = \left\{ \begin{array}{l l} 1, & i = j, \\ \alpha (1 + \alpha) ^ {j - i - 1}, & j > i. \end{array} \right. \tag {8.4}
$$

We have $\operatorname{cond}(U(\alpha), e) = \operatorname{cond}(U(\alpha)) \sim 2\alpha^{n-1}$ as $\alpha \to \infty$ . Therefore we cannot assert that all triangular systems are solved to high accuracy. Nevertheless, for any $T$ there is always at least one system for which high accuracy is obtained: the system $Tx = e_1$ if $T$ is upper triangular, or $Tx = e_n$ if $T$ is lower triangular. In both cases $\operatorname{cond}(T, x) = 1$ , and the solution comprises the computation of just a single scalar reciprocal.

To gain further insight we consider special classes of triangular matrices, beginning with one produced by certain standard factorizations with pivoting. In all the results below, the triangular matrices are assumed to be $n \times n$ and nonsingular, and $\widehat{x}$ is the computed solution from substitution.

Lemma 8.6. Suppose the upper triangular matrix $U \in \mathbb{R}^{n \times n}$ satisfies

$$
\left| u _ {i i} \right| \geq \left| u _ {i j} \right| \quad f o r a l l j > i. \tag {8.5}
$$

Then the unit upper triangular matrix $W = |U^{-1}||U|$ satisfies $w_{ij} \leq 2^{j - i}$ for all $j > i$ , and hence $\operatorname{cond}(U) \leq 2^n - 1$ .

Proof. We can write $W = |V^{-1}||V|$ where $V = D^{-1}U$ and $D = \mathrm{diag}(u_{ii})$ . The matrix $V$ is unit upper triangular with $|v_{ij}| \leq 1$ , and it is easy to show that $\left|(V^{-1})_{ij}\right| \leq 2^{j - i - 1}$ for $j > i$ . Thus, for $j > i$ ,

$$
w _ {i j} = \sum_ {k = i} ^ {j} \bigl | (V ^ {- 1}) _ {i k} \bigr | | v _ {k j} | \leq 1 + \sum_ {k = i + 1} ^ {j} 2 ^ {k - i - 1} \cdot 1 = 2 ^ {j - i}. \qquad \square
$$

Theorem 8.7. Under the conditions of Lemma 8.6, the computed solution $\widehat{x}$ to $Ux = b$ obtained by substitution satisfies

$$
\left| x _ {i} - \widehat {x} _ {i} \right| \leq 2 ^ {n - i + 1} \gamma_ {n} \max  _ {j \geq i} | \widehat {x} _ {j} |, \quad i = 1: n.
$$

Proof. From Theorem 8.5 we have

$$
| \boldsymbol {x} - \widehat {\boldsymbol {x}} | = | U ^ {- 1} \varDelta U \widehat {\boldsymbol {x}} | \leq \gamma_ {n} | U ^ {- 1} | | U | | \widehat {\boldsymbol {x}} |.
$$

Using Lemma 8.6 we obtain

$$
\left| x _ {i} - \widehat {x} _ {i} \right| \leq \gamma_ {n} \sum_ {j = i} ^ {n} w _ {i j} | \widehat {x} _ {j} | \leq \gamma_ {n} \max  _ {j \geq i} | \widehat {x} _ {j} | \sum_ {j = i} ^ {n} 2 ^ {j - i} \leq 2 ^ {n - i + 1} \gamma_ {n} \max  _ {j \geq i} | \widehat {x} _ {j} |.
$$

Lemma 8.6 shows that for $U$ satisfying (8.5), $\operatorname{cond}(U)$ is bounded for fixed $n$ , no matter how large $\kappa(U)$ . The bounds for $|x_i - \widehat{x}_i|$ in Theorem 8.7, although large if $n$ is large and $i$ is small, decay exponentially with increasing $i$ —thus, later components of $x$ are always computed to high accuracy relative to the elements already computed.

Analogues of Lemma 8.6 and Theorem 8.7 hold for lower triangular $L$ satisfying

$$
\left| l _ {i i} \right| \geq \left| l _ {i j} \right| \quad \text {f o r a l l} j <   i. \tag {8.6}
$$

Note, however, that if the upper triangular matrix $T$ satisfies (8.5) then $T^T$ does not necessarily satisfy (8.6). In fact, $\operatorname{cond}(T^T)$ can be arbitrarily large, as shown by the example

$$
\begin{array}{l} T = \left[ \begin{array}{c c c} 1 & 1 & 0 \\ 0 & \epsilon & \epsilon \\ 0 & 0 & 1 \end{array} \right], \\ \operatorname {c o n d} (T) = 5, \quad \operatorname {c o n d} (T ^ {T}) = 1 + \frac {2}{\epsilon}. \\ \end{array}
$$

An important conclusion is that a triangular system $Tx = b$ can be much more or less ill conditioned than the system $T^T y = c$ , even if $T$ satisfies (8.5).

Lemma 8.6 and Theorem 8.7, or their lower triangular analogues, are applicable to

- the lower triangular matrices from Gaussian elimination with partial pivoting, rook pivoting, and complete pivoting;   
- the upper triangular matrices from Gaussian elimination with rook pivoting and complete pivoting;   
- the upper triangular matrices from the Cholesky and QR factorizations with complete pivoting and column pivoting, respectively.

A more specialized class of upper triangular matrices than those satisfying (8.5) is those that are row diagonally dominant, that is, $U \in \mathbb{R}^{n \times n}$ satisfying

$$
| u _ {i i} | \leq \sum_ {j = i + 1} ^ {n} | u _ {i j} |, \quad i = 1: n - 1.
$$

Such matrices arise as the upper triangular matrices in the LU factorization without pivoting of row diagonally dominant matrices, and for them a much stronger result than Lemma 8.6 holds.

Lemma 8.8. If the upper triangular matrix $U \in \mathbb{R}^{n \times n}$ is row diagonally dominant then $\left(|U^{-1}||U|\right)_{ij} \leq i + j - 1$ and $\operatorname{cond}(U) \leq 2n - 1$ .

Proof. The proof follows that of Lemma 8.6, with $D$ and $V$ as defined there. Using the fact that $U$ , and hence $V$ , is row diagonally dominant we find that both

$V$ and $V^{-1}$ have elements bounded in magnitude by 1. The bound $|w_{ij}|\leq i + j - 1$ , where $W = |U^{-1}||U|$ , is then immediate. Finally,

$$
\begin{array}{l} \| W \| _ {\infty} = \parallel | W | e \| _ {\infty} = \parallel | V ^ {- 1} | | V | e \| _ {\infty} \\ \leq \left\| \left| V ^ {- 1} \right| [ 2 2 \dots 2 1 ] ^ {T} \right\| _ {\infty} \\ = 2 n - 1. \quad \square \\ \end{array}
$$

It follows from Lemma 8.8 and (8.2) that row diagonally dominant upper triangular systems are solved to essentially perfect normwise relative accuracy.

Next, we consider triangular $T$ satisfying

$$
t _ {i i} > 0, \quad t _ {i j} \leq 0 \quad \text {f o r a l l} i \neq j.
$$

It is easy to see that such a matrix has an inverse with nonnegative elements, and hence is an $M$ -matrix (for definitions of an $M$ -matrix see the Notes and References). Associated with any square matrix $A$ is the comparison matrix:

$$
M (A) = \left(m _ {i j}\right), \quad m _ {i j} = \left\{ \begin{array}{l l} \left| a _ {i i} \right|, & i = j, \\ - \left| a _ {i j} \right|, & i \neq j. \end{array} \right. \tag {8.7}
$$

For any nonsingular triangular $T$ , $M(T)$ is an $M$ -matrix. Furthermore, it is easy to show that $|T^{-1}| \leq M(T)^{-1}$ (see Theorem 8.12).

The following result shows that among all matrices $R$ such that $|R| = |T|$ , $R = M(T)$ is the one that maximizes $\operatorname{cond}(R, x)$ .

Lemma 8.9. For any triangular $T$ ,

$$
\operatorname {c o n d} (T, x) \leq \operatorname {c o n d} (M (T), x) = \left. \left\| \left(2 M (T) ^ {- 1} \operatorname {d i a g} \left(\left| t _ {i i} \right|\right) - I\right) | x | \right. \right\rVert_ {\infty} \Big / \| x \| _ {\infty}.
$$

Proof. The inequality follows from $|T^{-1}| \leq M(T)^{-1}$ , together with $|T| = |M(T)|$ . Since $M(T)^{-1} \geq 0$ , we have

$$
\begin{array}{l} \left| M (T) ^ {- 1} \right| \left| M (T) \right| = M (T) ^ {- 1} \left(2 \operatorname {d i a g} \left(\left| t _ {i i} \right|\right) - M (T)\right) \\ = 2 M (T) ^ {- 1} \operatorname {d i a g} \left(\left| t _ {i i} \right|\right) - I, \\ \end{array}
$$

which yields the equality.

If $T = M(T)$ has unit diagonal then, using Lemma 8.9,

$$
\operatorname {c o n d} (T) = \operatorname {c o n d} (T, e) = \| 2 T ^ {- 1} - I \| _ {\infty} \approx 2 \frac {\kappa (T)}{\| T \| _ {\infty}}.
$$

This means, for example, that the system $U(1)x = b$ (see (8.3)), where $x = e$ , is about as ill conditioned with respect to componentwise relative perturbations in $U(1)$ as it is with respect to normwise perturbations in $U(1)$ .

The next result gives a forward error bound for substitution that is proved directly, without reference to the backward error result Theorem 8.5 (indeed, it cannot be obtained from that result!). The bound can be very weak, because $\| M(T)^{-1} \|$ can be arbitrarily larger than $\| T^{-1} \|$ (see Problem 8.2), but it yields a pleasing bound in the special case described in the corollary.

Theorem 8.10. The computed solution $\widehat{x}$ obtained from substitution applied to the triangular system $Tx = b$ of order $n$ satisfies

$$
| x - \widehat {x} | \leq \left((n ^ {2} + n + 1) u + O (u ^ {2})\right) M (T) ^ {- 1} | b |.
$$

Proof. Without loss of generality, suppose $T = L$ is lower triangular. The proof is by induction on the components of $x$ . The result clearly holds for the first component. Assume that it holds for the first $n - 1$ components. An analogue of Lemma 8.4 shows that

$$
l _ {n n} \widehat {x} _ {n} = b _ {n} (1 + \theta_ {n + 1} ^ {(0)}) - \sum_ {j = 1} ^ {n - 1} l _ {n j} \widehat {x} _ {j} (1 + \theta_ {n + 1} ^ {(j)}),
$$

where $\left| \theta_{n+1}^{(j)} \right| \leq \gamma_{n+1}$ for all $j$ . Subtracting from $l_{nn}x_n = b_n - \sum_{j=1}^{n-1} l_{nj}x_j$ gives

$$
l _ {n n} (x _ {n} - \widehat {x} _ {n}) = - b _ {n} \theta_ {n + 1} ^ {(0)} - \sum_ {j = 1} ^ {n - 1} l _ {n j} (x _ {j} - \widehat {x} _ {j}) + \sum_ {j = 1} ^ {n - 1} l _ {n j} \widehat {x} _ {j} \theta_ {n + 1} ^ {(j)},
$$

so that

$$
\left| x _ {n} - \widehat {x} _ {n} \right| \leq \gamma_ {n + 1} \frac {\left| b _ {n} \right|}{\left| l _ {n n} \right|} + \sum_ {j = 1} ^ {n - 1} \frac {\left| l _ {n j} \right|}{\left| l _ {n n} \right|} \left| x _ {j} - \widehat {x} _ {j} \right| + \gamma_ {n + 1} \sum_ {j = 1} ^ {n - 1} \frac {\left| l _ {n j} \right|}{\left| l _ {n n} \right|} \left| \widehat {x} _ {j} \right|. \tag {8.8}
$$

Write

$$
M (L) = \left[ \begin{array}{c c} M _ {1 1} & 0 \\ - m ^ {T} & m _ {n n} \end{array} \right], \qquad M (L) ^ {- 1} = \left[ \begin{array}{c c} M _ {1 1} ^ {- 1} & 0 \\ m _ {n n} ^ {- 1} m ^ {T} M _ {1 1} ^ {- 1} & m _ {n n} ^ {- 1} \end{array} \right].
$$

Then the inductive assumption can be written as $|\widehat{x}(1:n-1) - x(1:n-1)| \leq \mu_{n-1}M_{11}^{-1}|b(1:n-1)|$ , which implies $|\widehat{x}(1:n-1)| \leq (\mu_{n-1} + 1)M_{11}^{-1}|b(1:n-1)|$ . Hence (8.8) gives

$$
\begin{array}{l} \left| x _ {n} - \widehat {x} _ {n} \right| \leq \gamma_ {n + 1} m _ {n n} ^ {- 1} | b _ {n} | + \mu_ {n - 1} m _ {n n} ^ {- 1} m ^ {T} M _ {1 1} ^ {- 1} | b (1: n - 1) | \\ + \gamma_ {n + 1} \left(\mu_ {n - 1} + 1\right) m _ {n n} ^ {- 1} m ^ {T} M _ {1 1} ^ {- 1} | b (1: n - 1) | \\ \leq \left(\mu_ {n - 1} + \gamma_ {n + 1} \left(\mu_ {n - 1} + 1\right)\right) \left(M (L) ^ {- 1} | b |\right) _ {n}. \\ \end{array}
$$

We have the recurrence $\mu_{k} = (1 + \gamma_{k + 1})\mu_{k - 1} + \gamma_{k + 1}\leq (1 + \gamma_{n + 1})\mu_{k - 1} + \gamma_{n + 1},$ $\mu_0 = u$ , which yields

$$
\mu_ {n} \leq \left(1 + \gamma_ {n + 1}\right) ^ {n} u + \left(\left(1 + \gamma_ {n + 1}\right) ^ {n} - 1\right) \leq \left(n ^ {2} + n + 1\right) u + O \left(u ^ {2}\right).
$$

Corollary 8.11. The computed solution obtained from substitution applied to the triangular system $Tx = b$ of order $n$ , where $T = M(T)$ and $b \geq 0$ , satisfies

$$
\left| x - \widehat {x} \right| \leq \big ((n ^ {2} + n + 1) u + O (u ^ {2}) \big) | x |.
$$

□

Corollary 8.11 shows that, when $T$ is an $M$ -matrix and the right-hand side is nonnegative, the solution is obtained to high relative accuracy in every component. The reason for the high accuracy is that for such a system there are no subtractions of like-signed numbers, so that each $x_{i}$ is computed as a sum of nonnegative quantities. A consequence of the corollary is that the inverse of a triangular $M$ -matrix can be computed to high relative accuracy.

Triangular systems of the type in Corollary 8.11 occur in linear equations obtained by discretizing certain elliptic partial differential equations, such as the Poisson equation on a rectangle, with zero boundary conditions and a positive forcing function: these problems yield symmetric positive definite $M$ -matrices, and the LU factors of an $M$ -matrix are themselves $M$ -matrices. Such systems also occur when evaluating the bounds of the next section.

# 8.3. Bounds for the Inverse

In this section we describe bounds for the inverse of a triangular matrix and show how they can be used to bound condition numbers. All the bounds in this section have the property that they depend only on the absolute values of the elements of the matrix. The norm estimation methods of Chapter 15, on the other hand, do take account of the signs of the elements.

The bounds are all based on the following theorem, whose easy proof we omit.

Theorem 8.12. If $U$ is a nonsingular upper triangular matrix then

$$
\left| U ^ {- 1} \right| \leq M (U) ^ {- 1} \leq W (U) ^ {- 1} \leq Z (U) ^ {- 1},
$$

where the upper triangular matrices $W(U)$ and $Z(U)$ are defined as follows:

$$
\begin{array}{l} w _ {i j} = \left\{ \begin{array}{l l} | u _ {i i} |, & i = j, \\ - \max  _ {i + 1 \leq k \leq n} | u _ {i k} |, & i <   j, \end{array} \right. \\ z _ {i j} = \left\{ \begin{array}{l l} \alpha , & i = j, \\ - \alpha \beta , & i <   j, \end{array} \right. \\ \end{array}
$$

where $\alpha = \min_{k}|u_{kk}|$ , $\beta = \max_{i < j}|u_{ij}| / |u_{ii}|$ .

Theorem 8.12 is a special case of results in the theory of $M$ -matrices. For more general results couched in terms of matrix minorants and diagonal dominance, respectively, see Dahlquist [288, 1983] and Varga [1190, 1976]; see also Householder [644, 1964, Exercise 15, p. 58].

An obvious implication of the theorem is that for any vector $z$ and any absolute norm

$$
\| | U ^ {- 1} | | z | \| \leq \| M (U) ^ {- 1} | z | \| \leq \| W (U) ^ {- 1} | z | \| \leq \| Z (U) ^ {- 1} | z | \|.
$$

By taking $z = |U|e$ , $z = |U||x|$ , and $z = e$ , respectively, we obtain upper bounds for $\operatorname{cond}(U)$ , $\operatorname{cond}(U,x)$ , and $\kappa_{\infty}(U)$ . The cost of computing these bounds is just the cost of solving a triangular system with coefficient matrix $M(U)$ , $W(U)$ , or

$Z(U)$ , which is easily seen to be $O(n^{2})$ , $O(n)$ , and $O(1)$ flops, respectively. By comparison, computing any of these condition numbers exactly costs $O(n^{3})$ flops.

As an example, here is how to compute an upper bound for $\| T^{-1}\|_{\infty}$ in $n^2$ flops.

Algorithm 8.13. Given a nonsingular upper triangular matrix $U \in \mathbb{R}^{n \times n}$ , this algorithm computes $\mu = \| M(U)^{-1}\|_{\infty} \geq \| U^{-1}\|_{\infty}$ .

$$
\begin{array}{l} y _ {n} = 1 / \left| u _ {n n} \right| \\ f o r i = n - 1: - 1: 1 \\ s = 1 \\ f o r j = i + 1: n \\ s = s + \left| u _ {i j} \right| y _ {j} \\ e n d \\ y _ {i} = y _ {i} / \left| u _ {i i} \right| \\ \end{array}
$$

$$
\begin{array}{l} e n d \\ \mu = \| y \| _ {\infty} \\ \end{array}
$$

How good are these upper bounds? We know from Problem 8.2 that the ratio $\| M(T)^{-1} \| / \| T^{-1} \|$ can be arbitrarily large, therefore any of the upper bounds can be arbitrarily poor. However, with suitable assumptions on $T$ , more can be said.

It is easy to show that if $T$ is bidiagonal then $|T^{-1}| = M(T)^{-1}$ . Since a bidiagonal system can be solved in $O(n)$ flops, it follows that the three condition numbers of interest can each be computed exactly in $O(n)$ flops when $T$ is bidiagonal.

As in the previous section, triangular matrices that result from a pivoting strategy also lead to a special result.

Theorem 8.14. Suppose the upper triangular matrix $U \in \mathbb{R}^{n \times n}$ satisfies

$$
\left| u _ {i i} \right| \geq \left| u _ {i j} \right| \quad f o r a l l j > i.
$$

Then, for the 1-, 2-, and $\infty$ -norms,

$$
\frac {1}{\min _ {i} \left| u _ {i i} \right|} \leq \| U ^ {- 1} \| \leq \| M (U) ^ {- 1} \| \leq \| W (U) ^ {- 1} \| \leq \| Z (U) ^ {- 1} \| \leq \frac {2 ^ {n - 1}}{\min _ {i} \left| u _ {i i} \right|}. \tag {8.9}
$$

Proof. The left-hand inequality is trivial. The right-hand inequality follows from the expression $\| Z(U)^{-1}\|_{1,\infty} = (\beta +1)^{n - 1} / \alpha$ (see Problem 8.5), together with $\| A\| _2\leq \sqrt{\|A\|_1\|A\|_\infty}$ .

The inequalities from the second onwards in (8.9) are all equalities for the matrix with $u_{ii} = 1$ and $u_{ij} = -1$ ( $j > i$ ). The question arises of whether equality is possible for the upper triangular matrices arising from QR factorization with column pivoting, which satisfy the inequalities (see Problem 19.5)

$$
u _ {k k} ^ {2} \geq \sum_ {i = k} ^ {j} u _ {i j} ^ {2}, \quad j = k + 1: n, \quad k = 1: n. \tag {8.10}
$$

That equality is possible is shown by the parametrized matrix of Kahan [687, 1966]

$$
U _ {n} (\theta) = \operatorname {d i a g} (1, s, \dots , s ^ {n - 1}) \left[ \begin{array}{c c c c c} 1 & - c & - c & \dots & - c \\ & 1 & - c & \dots & - c \\ & & \ddots & \ddots & \vdots \\ & & & \ddots & - c \\ & & & & 1 \end{array} \right], \tag {8.11}
$$

where $c = \cos(\theta)$ , $s = \sin(\theta)$ . It is easily verified that $U_{n}(\theta)$ satisfies the inequalities (8.10)—as equalities, in fact. From (8.4), $U_{n}(\theta)^{-1} = (\beta_{ij})$ is given by

$$
\beta_ {i j} = \left\{ \begin{array}{l l} s ^ {1 - j}, & i = j, \\ s ^ {1 - j} c (c + 1) ^ {j - i - 1}, & i <   j. \end{array} \right.
$$

Thus as $\theta \to 0$ , $s^{n - 1}U_n(\theta)^{-1}\to [0,0,\ldots ,0,x]$ , where $x = [2^{n - 2},2^{n - 1},\dots ,1,1]^T$ , and hence, for small $\theta$

$$
\left\| U _ {n} (\theta) ^ {- 1} \right\| _ {1, 2, \infty} \approx \frac {2 ^ {n - 1}}{\left| u _ {n n} \right|}.
$$

It can also be verified that the matrix $\overline{U}_n(\theta) = (\overline{u}_{ij})$ defined by $\overline{u}_{ij} = (-1)^{j - i}|u_{ij}|$ satisfies, for small $\theta$ , $\| \overline{U}_n(\theta)\|^{-1}\approx 1 / |u_{nn}|$ , while $\| M(\overline{U}_n(\theta))\|^{-1}\approx 2^{n - 1} / |u_{nn}|$ . Hence the upper bounds for $\| U^{-1}\|$ can all be too big by a factor of order $2^{n - 1}$ .

# 8.4. A Parallel Fan-In Algorithm

Substitution is not the only way to solve a triangular system. In this section we describe a different approach that has been suggested for parallel computation.

Any lower triangular matrix $L \in \mathbb{R}^{n \times n}$ can be factorized $L = L_{1}L_{2}\ldots L_{n}$ , where $L_{k}$ differs from the identity matrix only in the $k$ th column:

$$
L _ {k} = \left[ \begin{array}{c c c c c} I _ {k - 1} & & & & \\ & l _ {k k} & & & \\ & l _ {k + 1, k} & 1 & & \\ & \vdots & & \ddots & \\ & l _ {n k} & & & 1 \end{array} \right]. \tag {8.12}
$$

The solution to a linear system $Lx = b$ may therefore be expressed as

$$
x = L ^ {- 1} b = M _ {n} M _ {n - 1} \dots M _ {1} b, \tag {8.13}
$$

where $M_{i} = L_{i}^{-1}$ . When evaluated in the natural right-to-left order, this formula yields a trivial variation of a column-oriented version of substitution.

The fan-in algorithm evaluates the product (8.13) in $\lceil \log (n + 1)\rceil$ steps by the fan-in operation (which is the operation used in pairwise summation: see §4.1). For example, for $n = 7$ the calculation is specified by

$$
\boldsymbol {x} = \big ((M _ {7} M _ {6}) (M _ {5} M _ {4}) \big) \big ((M _ {3} M _ {2}) (M _ {1} b) \big),
$$

where all the products appearing within a particular size of parenthesis can be evaluated in parallel. In general, the evaluation can be expressed as a binary tree of depth $\lceil \log (n + 1) \rceil + 1$ , with products $M_{1}b$ and $M_{i}M_{i - 1}$ ( $i = 3,5,\ldots,2 \lfloor (n - 1)/2 \rfloor + 1$ ) at the top level and a single product yielding $x$ at the bottom level. This algorithm was proposed and analysed by Sameh and Brent [1008, 1977], who show that it can be implemented in $\frac{1}{2} \log^2 n + O(\log n)$ time steps on $\frac{1}{68} n^3 + O(n^2)$ processors. The algorithm requires about $n^3 / 10$ operations and thus is of no interest for serial computation. Some pertinent comments on the practical significance of $\log n$ terms in complexity results are given by Edelman [377, 1993].

To derive an error bound while avoiding complicated notation that obscures the simplicity of the analysis, we take $n = 7$ . The result we obtain is easily seen to be valid for all $n$ . We will not be concerned with the precise values of constants, so we write $c_{n}$ for a constant depending on $n$ . We assume that the inverses $M_{i} = L_{i}^{-1}$ are formed exactly, because the errors in forming them affect only the constants. From the error analysis of matrix-vector and matrix-matrix multiplication (§3.5), we find that the computed solution $\hat{\pmb{x}}$ satisfies

$$
\widehat {x} = \left(\left(M _ {7} M _ {6} + \Delta_ {7 6}\right) \left(M _ {5} M _ {4} + \Delta_ {5 4}\right) + \Delta_ {7 6 5 4}\right) \left(\left(M _ {3} M _ {2} + \Delta_ {3 2}\right) \left(M _ {1} + \Delta_ {1}\right) b\right), \tag {8.14}
$$

where

$$
\begin{array}{l} \left| \Delta_ {i, i - 1} \right| \leq c _ {n} u \left| M _ {i} \right| \left| M _ {i - 1} \right| + O \left(u ^ {2}\right), \quad i = 5, 7, \\ \left| \Delta_ {7 6 5 4} \right| \leq c _ {n} u \left(\left| M _ {7} M _ {6} \right| \left| M _ {5} M _ {4} \right| + \left| M _ {7} M _ {6} M _ {5} M _ {4} \right|\right) + O \left(u ^ {2}\right), \\ \left| \Delta_ {3 2} \right| \leq c _ {n} u \left(\left| M _ {3} \right| \left| M _ {2} \right| + \left| M _ {3} M _ {2} \right|\right) + O \left(u ^ {2}\right), \\ \left| \Delta_ {1} \right| \leq c _ {n} u \left| M _ {1} \right| + O \left(u ^ {2}\right). \\ \end{array}
$$

Premultiplying (8.14) on the left by $L$ , we find that the residual $r = L\widehat{x} - b$ is a sum of terms of the form

$$
L \left(M _ {7} \dots M _ {j + 1}\right) \Delta_ {j, \dots , k} M _ {k - 1} \dots M _ {1} b = L _ {1} \dots L _ {j} \Delta_ {j, \dots , k} L _ {k} \dots L _ {7} x.
$$

All these terms share the same upper bound, which we derive for just one of them. For $j = 5$ , $k = 4$ we have

$$
\begin{array}{l} \left| L _ {1} \dots L _ {5} \Delta_ {5 4} L _ {4} \dots L _ {7} x \right| \leq c _ {n} u \left| L _ {1} \dots L _ {5} \right| \left| M _ {5} \right| \left| M _ {4} \right| \left| L _ {4} \dots L _ {7} x \right| + O \left(u ^ {2}\right) \\ = c _ {n} u \left| L _ {1} \dots L _ {5} \right| \left| \left| L _ {6} L _ {7} L ^ {- 1} L _ {1} \dots L _ {4} \right| \right. \\ \times \left| L _ {5} L _ {6} L _ {7} L ^ {- 1} L _ {1} L _ {2} L _ {3} | | L _ {4} \dots L _ {7} x \right| + O \left(u ^ {2}\right) \\ \leq c _ {n} u | L | | L ^ {- 1} | | L | | L ^ {- 1} | | L | | x | + O \left(u ^ {2}\right), \\ \end{array}
$$

where we have used the property that, for any $L \in \mathbb{R}^{n \times n}$ , $|L_1| \ldots |L_n| = |L|$ . The overall residual bound is therefore of the form

$$
\left| b - L \widehat {x} \right| \leq d _ {n} u | L | | L ^ {- 1} | | L | | L ^ {- 1} | | L | | x | + O \left(u ^ {2}\right), \tag {8.15}
$$

or, on taking norms,

$$
\left\| b - L \widehat {x} \right\| _ {\infty} \leq d _ {n} u \| | L | | L ^ {- 1} | | L | | L ^ {- 1} | | L | | x | \| _ {\infty} + O \left(u ^ {2}\right). \tag {8.16}
$$

By considering the binary tree associated with the fan-in algorithm, and using the fact that the matrices at the $i$ th level of the tree have at most $2^{i-1}$ nontrivial

columns, it is easy to see that we can take $d_{n} = an\log n$ , where $a$ is a constant of order 1.

It is not hard to find numerical examples where the bound in (8.16) is approximately attained (for $d_n = 1$ ) and greatly exceeds $u\| L\|_{\infty}\| \widehat{x}\|_{\infty}$ , which is the magnitude required for normwise backward stability. One way to construct such examples is to use direct search (see Chapter 26).

The key fact revealed by (8.16) is that the fan-in algorithm is only conditionally stable. In particular, the algorithm is normwise backward stable if $L$ is well conditioned. A special case in which (8.15) simplifies is when $L$ is an $M$ -matrix and $b \geq 0$ : Problem 8.4 shows that in this case $|L^{-1}||L||x| \leq (2n - 1)|x|$ , so (8.15) yields $|L\widehat{x} - b| \leq (2n - 1)^{2}d_{n}u|L||x| + O(u^{2})$ , and we have componentwise backward stability (to first order).

We can obtain from (8.16) the result

$$
(L + \Delta L) \widehat {x} = b, \quad \| \Delta L \| _ {\infty} \leq \alpha_ {n} u \kappa_ {\infty} (L) ^ {2} \| L \| _ {\infty} + O \left(u ^ {2}\right), \tag {8.17}
$$

which was proved by Sameh and Brent [1008, 1977] (with $\alpha_{n} = \frac{1}{4} n^{2}\log n + O(n\log n)$ ). However, (8.17) is a much weaker bound than (8.15) and (8.16). In particular, a diagonal scaling $Lx = b\rightarrow D_1LD_2\cdot D_2^{-1}x = D_1b$ (where $D_{j}$ is diagonal) leaves (8.15) (and, to a lesser extent, (8.16)) essentially unchanged, but can change the bound (8.17) by an arbitrary amount.

A forward error bound can be obtained directly from (8.14). We find that

$$
\begin{array}{l} \left| x - \widehat {x} \right| \leq d _ {n} ^ {\prime} u | M _ {7} | | M _ {6} | \dots | M _ {1} | | b | + O \left(u ^ {2}\right) \\ = d _ {n} ^ {\prime} u M (L) ^ {- 1} | b | + O \left(u ^ {2}\right), \tag {8.18} \\ \end{array}
$$

where $M(L)$ is the comparison matrix (a bound of the same form as that in Theorem 8.10 for substitution—see the Notes and References and Problem 8.10), which can be weakened to

$$
\frac {\| x - \widehat {x} \| _ {\infty}}{\| x \| _ {\infty}} \leq c _ {n} u \frac {\| M (L) ^ {- 1} | L | | x | \| _ {\infty}}{\| x \| _ {\infty}} + O \left(u ^ {2}\right). \tag {8.19}
$$

We also have the bound

$$
\frac {\| x - \widehat {x} \| _ {\infty}}{\| x \| _ {\infty}} \leq d _ {n} u \frac {\| (| L ^ {- 1} | | L |) ^ {3} | x | \| _ {\infty}}{\| x \| _ {\infty}} + O \left(u ^ {2}\right), \tag {8.20}
$$

which is an immediate consequence of (8.15). Either bound in (8.19) and (8.20) can be arbitrarily larger than the other, for fixed $n$ . An example where (8.20) is the better bound (for large $n$ ) is provided by the matrix with $l_{ij} \equiv 1$ , for which $|L^{-1}||L|$ has maximum element 2 and $M(L)^{-1}|L|$ has maximum element $2^{n-1}$ .

# 8.5. Notes and References

Section 8.2 is based on Higham [586, 1989]. Many of the results presented in §§8.2 and 8.3 have their origin in the work of Wilkinson. Indeed, these sections are effectively a unification and extension of Wilkinson's results in [1229, 1961], [1232, 1963], and [1233, 1965].

Classic references for Theorems 8.3 and 8.5 are Wilkinson [1229, 1961, p. 294], [1232, 1963, pp. 100-102], Forsythe and Moler [431, 1967, §21], and Stewart [1065, 1973, pp. 150, 408-410].

Analogues of Theorem 8.7 and Corollary 8.11 for matrix inversion are proved by Wilkinson in [1229, 1961, pp. 322-323], and Corollary 8.11 itself is proved in [1233, 1965, pp. 250-251]. Lemma 8.8 appears to have first been obtained by Peña [933, 1998], and it was also derived by Malyshev [811, 2000].

A matrix $A \in \mathbb{R}^{n \times n}$ is an $M$ -matrix if $a_{ij} \leq 0$ for all $i \neq j$ and all the eigenvalues of $A$ have nonnegative real part. This is one of many equivalent definitions [106, 1994, Chap. 6]. An $M$ -matrix may be singular. A particularly useful characterization of a nonsingular $M$ -matrix is a nonsingular matrix $A \in \mathbb{R}^{n \times n}$ for which $a_{ij} \leq 0$ for all $i \neq j$ and $A^{-1} \geq 0$ . For more information on $M$ -matrices see Berman and Plemmons [106, 1994] and Horn and Johnson [637, 1991, §2.5].

A result of the form of Theorem 8.10 holds for any triangular system solver that does not rely on algebraic cancellation—in particular, for the fan-in algorithm, as already seen in (8.18). See Problem 8.10 for a more precise formulation of this general result.

Stewart [1079, 1997] shows that $\operatorname{cond}(U)$ is small if the upper triangular matrix $U$ is rank-revealing in a certain sense, and he argues that the $U$ produced by pivoted LU, Cholesky, and QR factorizations tend to be rank-revealing. His analysis provides further insight into why triangular systems are typically solved to high accuracy in practice.

The bounds in §8.3 have been investigated by various authors. The unified presentation given here is based on Higham [582, 1987]. Karasalo [710, 1974] derives an $O(n)$ flops algorithm for computing $\| M(T)^{-1}\|_F$ . Manteuffel [814, 1981] derives the first two inequalities in Theorem 8.12, and Algorithm 8.13. A different derivation of the equations in Algorithm 8.13 is given by Jennings [674, 1982, §9]. The formulae given in Problem 8.5 are derived directly as upper bounds for $\| T^{-1}\|_{1,\infty}$ by Lemeire [781, 1975].

That $\| B^{-1}\|_{\infty}$ can be computed in $O(n)$ flops when $B$ is bidiagonal, by exploiting the relation $\| B^{-1}\|_{\infty} = \| M(B)^{-1}e\|_{\infty}$ , was first pointed out by Higham [579, 1986]. Demmel and Kahan [329, 1990] derive an estimate for the smallest singular value $\sigma_{\min}$ of a bidiagonal matrix $B$ by using the inequality $\overline{\sigma} \leq \sigma_{\min}(B) \leq \sqrt{n}\overline{\sigma}$ , where $\overline{\sigma} = \min(\| B^{-1}\|_{\infty}^{-1}, \| B^{-1}\|_1^{-1})$ . They compute $\overline{\sigma}$ in $O(n)$ flops as

$$
\overline {{\sigma}} = \min (\left\| M (B) ^ {- 1} e \right\| _ {\infty} ^ {- 1}, \left\| M (B) ^ {- T} e \right\| _ {\infty} ^ {- 1}).
$$

Section 8.4 is adapted from Higham [605, 1995], in which error analysis is given for several parallel methods for solving triangular systems.

The fan-in method is topical because the fan-in operation is a special case of the parallel prefix operation and several fundamental computations in linear algebra are amenable to a parallel prefix-based implementation, as discussed by Demmel [315, 1992], [316, 1993]. (For a particularly clear explanation of the parallel prefix operation see the textbook by Buchanan and Turner [171, 1992, §13.2].) The important question of the stability of the parallel prefix implementation of Sturm sequence evaluation for the symmetric tridiagonal eigenproblem is answered by Mathias [822, 1995]. Mathias shows that for positive definite matrices the relative error in a computed minor can be as large as a multiple of $\lambda_{n}^{-3}$ , where $\lambda_{n}$ is

the smallest eigenvalue of the matrix; the corresponding bound for serial evaluation involves $\lambda_{n}^{-1}$ . The analogy with (8.20), where we also see a condition cubing effect, is intriguing.

Higham and Pothen [622, 1994] analyse the stability of the "partitioned inverse method" for parallel solution of sparse triangular systems with many right-hand sides. This method has been studied by several authors in the 1990s; see Alvarado, Pothen, and Schreiber [17, 1993] and the references therein. The idea of the method is to factor a sparse triangular matrix $L \in \mathbb{R}^{n \times n}$ as $L = L_{1}L_{2}\ldots L_{n} = G_{1}G_{2}\ldots G_{m}$ , where each $G_{i}$ is a product of consecutive $L_{j}$ terms and $1 \leq m \leq n$ , with $m$ as small as possible subject to the $G_{i}$ being sparse. Then the solution to $Lx = b$ is evaluated as

$$
x = G _ {m} ^ {- 1} G _ {m - 1} ^ {- 1} \dots G _ {1} ^ {- 1} b,
$$

where each $G_{i}^{-1}$ is formed explicitly and the product is evaluated from right to left. The advantage of this approach is that $x$ can be computed in $m$ serial steps of parallel matrix-vector multiplication.

# 8.5.1. LAPACK

Computational routine xTRTRS solves a triangular system with multiple right-hand sides; xTBTRS is an analogue for banded triangular matrices. There is no driver routine for triangular systems.

# Problems

Before you start an exercise session, take sure you have a glass of water and a mat or towel nearby.

— MARIE HELVIN, Model Tips for a Healthy Future (1994)

8.1. Show that under the no-guard-digit model (2.6), Lemma 8.2 remains true if (8.1) is changed to

$$
b _ {k} \widehat {y} (1 + \theta_ {k}) = c - \sum_ {i = 1} ^ {k - 1} a _ {i} b _ {i} (1 + \theta_ {i + 2}),
$$

and that the corresponding modification of Theorem 8.5 has

$$
(T + \Delta T) \widehat {x} = b, \quad | \Delta T | \leq \gamma_ {n + 1} | T |.
$$

8.2. Show that for a triangular matrix $T$ the ratio $\| M(T)^{-1} \| / \| T^{-1} \|$ can be arbitrarily large.

8.3. Suppose the unit upper triangular matrix $U \in \mathbb{R}^{n \times n}$ satisfies $|u_{ij}| \leq 1$ for $j > i$ . By using Theorem 8.10, show that the computed solution $\widehat{x}$ from substitution on $Ux = b$ satisfies

$$
\left| x _ {i} - \widehat {x} _ {i} \right| \leq 2 ^ {n - i} \left(\left(n ^ {2} + n + 1\right) u + O \left(u ^ {2}\right)\right) \| b \| _ {\infty}.
$$

Compare with the result of applying Theorem 8.7.

8.4. Let $T \in \mathbb{R}^{n \times n}$ be triangular and suppose $T = M(T)$ and $Tx = b \geq 0$ . Show that $|T^{-1}||T||x| \leq (2n - 1)|x|$ , and hence that $\operatorname{cond}(T, x) \leq 2n - 1$ . This result shows that a triangular $M$ -matrix system with a nonnegative right-hand side is very well conditioned with respect to componentwise relative perturbations, irrespective of the size of $\kappa(T)$ (and so leads to an alternative proof of Corollary 8.11).

8.5. Show that for a triangular $T \in \mathbb{R}^{n \times n}$ , $\| Z(T)^{-1} \| = (\beta + 1)^{n - 1} / \alpha$ for both the 1- and $\infty$ -norms ( $\alpha$ and $\beta$ are defined in Theorem 8.12).

8.6. Write detailed algorithms for efficiently computing the quantities

$$
\left\| M (U) ^ {- 1} | z | \right\| _ {\infty}, \quad \left\| W (U) ^ {- 1} | z | \right\| _ {\infty}.
$$

8.7. Bounds from diagonal dominance. (a) Prove the following result (Ahlberg and Nilson [9, 1963], Varah [1188, 1975]): if $A \in \mathbb{R}^{n \times n}$ (not necessarily triangular) satisfies

$$
\alpha_ {i} := \left| a _ {i i} \right| - \sum_ {j \neq i} \left| a _ {i j} \right| > 0, \quad i = 1: n
$$

(that is, $A$ is strictly diagonally dominant by rows), then

$$
\left\| A ^ {- 1} \right\| _ {\infty} \leq \frac {1}{\min  _ {i} \alpha_ {i}}.
$$

(b) Hence show that (Varga [1190, 1976]) if $A \in \mathbb{R}^{n \times n}$ satisfies

$$
\beta_ {i} := | a _ {i i} | d _ {i} - \sum_ {j \neq i} | a _ {i j} | d _ {j} > 0, \quad i = 1: n,
$$

for some positive diagonal matrix $D = \mathrm{diag}(d_i)$ (that is, $AD$ is strictly diagonally dominant by rows), then

$$
\| A ^ {- 1} \| _ {\infty} \leq \frac {\| D \| _ {\infty}}{\min  _ {i} \beta_ {i}}.
$$

(c) Use part (b) to provide another derivation of the upper bound $\| M(T)^{-1}e\|_{\infty}$ $\geq \| T^{-1}\|_{\infty}$

8.8. (a) Let $A \in \mathbb{R}^{n \times n}$ be nonsingular. For a given $i$ and $j$ , determine, if possible, $\alpha_{ij}$ such that $A + \alpha_{ij} e_i e_j^T$ is singular. Where is the "best" place to perturb $A$ to make it singular?

(b) Let $T = U(1)$ in (8.3), so that, for example,

$$
T _ {4} = \left[ \begin{array}{c c c c} 1 & - 1 & - 1 & - 1 \\ & 1 & - 1 & - 1 \\ & & 1 & - 1 \\ & & & 1 \end{array} \right].
$$

Show that $T_{n}$ is made singular by subtracting $2^{2 - n}$ from a certain element of $T_{n}$ .

8.9. (Zha [1279, 1993]) Show that if $c$ and $s$ are nonnegative (with $c^2 + s^2 = 1$ ) then the Kahan matrix $U_n(\theta)$ in (8.11) has $s^{n-2}\sqrt{1 + c}$ as its second smallest singular value. (That there should be such an explicit formula is surprising; none is known for the smallest singular value.)

8.10. Consider a method for solving triangular systems $Tx = b$ that computes $x_{i} = f_{i}(T,b)$ where, for all $i$ , $f_{i}$ is a multivariate rational function in which the only divisions are by diagonal elements of $L$ and such that when $T = M(T)$ and $b \geq 0$ there are no subtractions in the evaluation of $f_{i}$ . Show that a bound holds of the form in Theorem 8.10, namely, for $T \in \mathbb{R}^{n \times n}$ ,

$$
\left| x - \widehat {x} \right| \leq \left(c _ {n} u + O \left(u ^ {2}\right)\right) M (T) ^ {- 1} | b |. \tag {8.21}
$$

Give an example of a triangular system solver for which (8.21) is not satisfied.
