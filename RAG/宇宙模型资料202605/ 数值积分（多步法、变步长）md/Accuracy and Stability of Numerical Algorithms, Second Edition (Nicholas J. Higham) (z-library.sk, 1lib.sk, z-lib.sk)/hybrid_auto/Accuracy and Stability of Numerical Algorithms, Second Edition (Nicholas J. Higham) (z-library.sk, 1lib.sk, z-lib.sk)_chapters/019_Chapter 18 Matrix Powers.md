# Chapter 18 Matrix Powers

Unfortunately, the roundoff errors in the $m$ th power of a matrix, say $B^{m}$ , are usually small relative to $\| B \|^{m}$ rather than $\| B^{m} \|$ .

— CLEVE B. MOLER and CHARLES F. VAN LOAN, Nineteen Dubious Ways to Compute the Exponential of a Matrix (1978)

It is the size of the hump that matters:

the behavior of $\| p(A\Delta t)^n\| = \| p(A\Delta t)^{t / \Delta t}\|$ for small but nonzero $t$

The eigenvalues and the norm, by contrast, give sharp information

only about the limits $t\to \infty$ or $t\rightarrow 0$

— DESMOND J. HIGHAM and LLOYD N. TREFETHEN,

Stiffness of ODEs (1993)

Many people will go through life powering matrices and never see anything as dramatic as $J_{2}(0.99)^{k}$ .<sup>16</sup>

— G. W. STEWART, Matrix Algorithms. Volume II: Eigensystems (2001)

Powers of matrices occur in many areas of numerical analysis. One approach to proving convergence of multistep methods for solving differential equations is to show that a certain parameter-dependent matrix is uniformly "power bounded" [537, 1991, §V.7], [974, 1992]. Stationary iterative methods for solving linear equations converge precisely when the powers of the iteration matrix converge to zero. And the power method for computing the largest eigenvalue of a matrix computes the action of powers of the matrix on a vector. It is therefore important to understand the behaviour of matrix powers, in both exact and finite precision arithmetic.

It is well known that the powers $A^k$ of $A \in \mathbb{C}^{n \times n}$ tend to zero as $k \to \infty$ if $\rho(A) < 1$ , where $\rho$ is the spectral radius. However, this simple statement does not tell the whole story. Figure 18.1 plots the 2-norms of the first 30 powers of a certain $3 \times 3$ matrix with $\rho(A) = 0.75$ . The powers do eventually decay, but initially they grow rapidly. (In this and other similar plots, $k$ on the $x$ -axis is plotted against $\| fl(A^k)\|_2$ on the $y$ -axis, and the norm values are joined by straight lines for plotting purposes.) Figure 18.2 plots the 2-norms of the first 250 powers of a $14 \times 14$ nilpotent matrix $C_{14}$ discussed by Trefethen and Trummer [1158, 1987] (see §18.2 for details). The plot illustrates the statement of these authors that the matrix is not power bounded in floating point arithmetic, even though its 14th power should be zero.

These examples suggest two important questions.

- For a matrix with $\rho(A) < 1$ , how does the sequence $\{\|A^k\|\}$ behave? In particular, what is the size of the "hump" $\max_k \|A^k\|$ ?   
- What conditions on $A$ ensure that $fl(A^k) \to 0$ as $k \to \infty$ ?

We examine these questions in the next two sections.

# 18.1. Matrix Powers in Exact Arithmetic

In exact arithmetic the limiting behaviour of the powers of $A \in \mathbb{C}^{n \times n}$ is determined by $A$ 's eigenvalues. As already noted, if $\rho(A) < 1$ then $A^k \to 0$ as $k \to \infty$ ; if $\rho(A) > 1$ , $\|A^k\| \to \infty$ as $k \to \infty$ . In the remaining case of $\rho(A) = 1$ , $\|A^k\| \to \infty$ if $A$ has a defective eigenvalue $\lambda$ such that $|\lambda| = 1$ ; $A^k$ does not converge if $A$ has a nondefective eigenvalue $\lambda \neq 1$ such that $|\lambda| = 1$ (although the norms of the powers may converge); otherwise, the only eigenvalue of modulus 1 is the nondefective eigenvalue 1 and $A^k$ converges to a nonzero matrix. These statements are easily proved using the Jordan canonical form

$$
A = X J X ^ {- 1} \in \mathbb {C} ^ {n \times n}, \tag {18.1a}
$$

where $X$ is nonsingular and

$$
J = \operatorname {d i a g} \left(J _ {1}, J _ {2}, \dots , J _ {s}\right), \quad J _ {i} = \left[ \begin{array}{c c c c} \lambda_ {i} & 1 & & \\ & \ddots & \ddots & \\ & & \lambda_ {i} & 1 \\ & & & \lambda_ {i} \end{array} \right] \in \mathbb {C} ^ {n _ {i} \times n _ {i}}, \tag {18.1b}
$$

where $n_1 + n_2 + \dots + n_s = n$ . We will call a matrix for which $A^k \to 0$ as $k \to \infty$ (or equivalently, $\rho(A) < 1$ ) a convergent matrix.

![](images/43f12ede5d0dab8eb58f65a3c90fb1035a39c3cebf353b9bbd2d1d8fc5da8129.jpg)  
Figure 18.1. A typical hump for a convergent, nonnormal matrix.

![](images/59c320492e7ab64156444ec76231be179f9c33534830d35192cdf857f242b083.jpg)  
Figure 18.2. Diverging powers of a nilpotent matrix, $C_{14}$ .

The norm of a convergent matrix can be arbitrarily large, as is shown trivially by the scaled Jordan block

$$
J = \lambda \left[ \begin{array}{c c} 1 & \alpha \\ 0 & 1 \end{array} \right], \tag {18.2}
$$

with $|\lambda| < 1$ and $\alpha \gg 1$ . While the spectral radius determines the asymptotic rate of growth of matrix powers, the norm influences the initial behaviour of the powers. The interesting result that $\rho(A) = \lim_{k \to \infty} \|A^k\|^{1/k}$ for any norm (see Horn and Johnson [636, 1985, p. 299], for example) confirms the asymptotic role of the spectral radius. This formula for $\rho(A)$ has actually been considered as a means for computing it; see Wilkinson [1233, 1965, pp. 615-617] and Friedland [445, 1991].

An important quantity is the "hump" $\max_k\| A^k\|$ , which can be arbitrarily large for a convergent matrix. Figure 18.1 shows the hump for the $3\times 3$ upper triangular matrix with diagonal entries $3 / 4$ and off-diagonal entries 2; this matrix has 2-norm 3.57. The shape of the plot is typical of that for a convergent matrix with norm bigger than 1. Note that if $A$ is normal (so that in (18.1a) $J$ is diagonal and $X$ can be taken to be unitary) we have $\| A^k\| _2 = \| \mathrm{diag}(\lambda_i^k)\| _2 = \| A\| _2^k = \rho (A)^k$ , so the problem of bounding $\| A^k\|$ is of interest only for nonnormal matrices. The hump phenomenon arises in various areas of numerical analysis. For example, it is discussed for matrix powers in the context of stiff differential equations by D. J. Higham and Trefethen [577, 1993], and by Moler and Van Loan [868, 1978] for the matrix exponential $e^{At}$ with $t\to \infty$ .

More insight into the behaviour of matrix powers can be gained by considering the $2 \times 2$ matrix (18.2) with $0 \leq \lambda < 1$ and $\alpha > 0$ . We have

$$
J ^ {k} = \lambda^ {k} \left[ \begin{array}{c c} 1 & k \alpha \\ 0 & 1 \end{array} \right]
$$

and

$$
\frac {\| J ^ {k + 1} \| _ {\infty}}{\| J ^ {k} \| _ {\infty}} = \lambda \frac {1 + (k + 1) \alpha}{1 + k \alpha} \approx \lambda \left(1 + \frac {1}{k}\right) \text {f o r l a r g e} k. \tag {18.3}
$$

Hence

$$
\| J ^ {k + 1} \| _ {\infty} <   \| J ^ {k} \| _ {\infty} \quad \text {i f} \quad k > \frac {\lambda (1 + \alpha) - 1}{(1 - \lambda) \alpha}.
$$

It follows that the norms of the powers can increase for arbitrarily many steps until they ultimately decrease. Moreover, because $k^{-1}$ tends to zero quite slowly as $k \to \infty$ , the rate of convergence of $\| J^k \|_{\infty}$ to zero can be much slower than the convergence of $\lambda^k$ to zero (see (18.3)) when $\lambda$ is close to 1. In other words, nontrivial Jordan blocks retard the convergence to zero.

For this $2 \times 2$ matrix, the hump $\max_k \|J^k\|_{\infty}$ is easily shown to be approximately

$$
\rho^ {1 / \alpha - 1 / \log_ {e} \rho} \frac {\alpha}{\log_ {e} \rho},
$$

where $\rho = \lambda^{-1} > 1$ , this value being attained for $k \approx (\log_e \rho)^{-1} - \alpha^{-1}$ . Figure 18.3 displays the norms of the first 400 powers of the matrices with $\lambda = 0.99$ and $\alpha = 0, 0.001, 0.01, 0.1, 1$ . The size and location of the hump are complicated expressions even in this simple case. When we generalize to direct sums of larger Jordan

![](images/1847438c4df488bcc2410a377115f9d4d71efd503668c0639198626dd8666fda.jpg)  
Figure 18.3. Infinity norms of powers of $2 \times 2$ matrix $J$ in (18.2), for $\lambda = 0.99$ and $\alpha = 0$ (bottom line) and $\alpha = 10^{-k}$ , $k = 0:3$ .

blocks and incorporate a similarity transformation, giving (18.1a), the qualitative behaviour of the powers becomes too difficult to describe precisely.

In the rest of this section we briefly survey bounds for $\| A^k \|$ , where $\| \cdot \|$ is a consistent norm. First, however, we comment on the condition number $\kappa(X) = \| X \| \| X^{-1} \|$ that appears in various bounds in this chapter. The matrix $X$ in the Jordan form (18.1a) is by no means unique [453, 1959, pp. 220-221], [506, 1976]: if $A$ has distinct eigenvalues (hence $J$ is diagonal) then $X$ can be replaced by $XD$ , for any nonsingular diagonal $D$ , while if $A$ has repeated eigenvalues then $X$ can be replaced by $XT$ , where $T$ is a block matrix with block structure conformal with that of $J$ and which contains some arbitrary upper trapezoidal Toeplitz blocks. We adopt the convention that $\kappa(X)$ denotes the minimum possible value of $\kappa(X)$ over all possible choices of $X$ . This minimum value is not known for general $A$ , and the best we can hope is to obtain a good estimate of it. However, if $A$ has distinct eigenvalues then the results in Theorems 7.5 and 7.7 on diagonal scalings are applicable and enable us to determine (an approximation to) the minimal condition number. Explicit expressions can be given for the minimal 2-norm condition number for $n = 2$ ; see Young [1270, 1971, §3.8].

A trivial bound is $\| A^k \| \leq \| A \|^k$ . A sharper bound can be derived in terms of the numerical radius

$$
r (A) = \max  \left\{\left| \frac {z ^ {*} A z}{z ^ {*} z} \right|: 0 \neq z \in \mathbb {C} ^ {n} \right\},
$$

which is the point of largest modulus in the field of values of $A$ . It is not hard to show that $\| A \|_2 / 2 \leq r(A) \leq \| A \|_2$ [636, 1985, p. 331]. The (nontrivial) inequality $r(A^k) \leq r(A)^k$ [636, 1985, p. 333] leads to the bound

$$
\left\| A ^ {k} \right\| _ {2} \leq 2 r (A) ^ {k}.
$$

If $A$ is diagonalizable then, from (18.1a), we have the bound

$$
\left\| A ^ {k} \right\| _ {p} \leq \kappa_ {p} (X) \rho (A) ^ {k}, \tag {18.4}
$$

for any $p$ -norm. (Since $\rho(A) \leq \|A\|$ for any consistent norm (Problem 6.7), we also have the lower bound $\rho(A)^k \leq \|A^k\|_p$ .) This bound is unsatisfactory for two reasons. First, by choosing $A$ to have well-conditioned large eigenvalues and ill-conditioned small eigenvalues we can make the bound arbitrarily pessimistic (see Problem 18.1). Second, it models norms of powers of convergent matrices as monotonically decreasing sequences, which is qualitatively incorrect if there is a large hump.

The Jordan canonical form can also be used to bound the norms of the powers of a defective matrix. If $XJX^{-1}$ is the Jordan canonical form of $\delta^{-1}A$ then

$$
\left\| A ^ {k} \right\| _ {p} \leq \kappa_ {p} (X) (\rho (A) + \delta) ^ {k}, \tag {18.5}
$$

for all $\delta > 0$ . This is a special case of a result of Ostrowski [909, 1973, Thm. 20.1] and the proof is straightforward: We can write $\delta^{-1}A = X(\delta^{-1}D + M)X^{-1}$ , where $D = \mathrm{diag}(\lambda_i)$ and $M$ is the off-diagonal part of the Jordan form. Then $A = X(D + \delta M)X^{-1}$ , and (18.5) follows by powering and taking norms. An alternative way of writing this bound is

$$
\left\| A ^ {k} \right\| _ {p} \leq \kappa_ {p} (X) \kappa_ {p} (D) \bigl (\rho (A) + \delta \bigr) ^ {k},
$$

where $A = XJX^{-1}$ and $D = \mathrm{diag}(\delta^{n - 1},\delta^{n - 2},\ldots ,1)$ . Note that this is not the same $X$ as in (18.5): multiplying $A$ by a scalar changes $\kappa (X)$ when $A$ is not diagonalizable. Both bounds suffer from the same problems as the bound (18.4) for diagonalizable matrices.

Another bound in terms of the Jordan canonical form (18.1) of $A$ is given by Gautschi [469, 1953]. For convergent matrices, it can be written in the form

$$
\left\| A ^ {k} \right\| _ {F} \leq c k ^ {p - 1} \rho (A) ^ {k}, \tag {18.6}
$$

where $p = \max \{n_i : \lambda_i \neq 0\}$ and $c$ is a constant depending only on $A$ ( $c$ is not defined explicitly in [469, 1953]). The factor $k^{p-1}$ makes this bound somewhat more effective at predicting the shapes of the actual curve than (18.5), but again $c$ can be unsuitably large.

Since the norm estimation problem is trivial for normal matrices, it is natural to look for bounds that involve a measure of nonnormality. Consider the Schur decomposition $Q^{*}AQ = D + N$ , where $N$ is strictly upper triangular, and let $S$ represent the set of all such $N$ . The nonnormality of $A$ can be measured by Henrici's departure from normality [563, 1962]

$$
\Delta (A, \| \cdot \|) \equiv \Delta (A) = \min  _ {N \in S} \| N \|.
$$

For the Frobenius norm, Henrici shows that $\| N\| _F$ is independent of the particular Schur form and that

$$
\varDelta_ {F} (A) = \left(\| A \| _ {F} ^ {2} - \sum_ {i} | \lambda_ {i} | ^ {2}\right) ^ {1 / 2} \leq \left(\frac {n ^ {3} - n}{1 2}\right) ^ {1 / 4} \| A ^ {*} A - A A ^ {*} \| _ {F} ^ {1 / 2}.
$$

László [770, 1994] has recently shown that $\Delta_F(A)$ is within a constant factor of the distance from $A$ to the nearest normal matrix:

$$
\frac {\Delta_ {F} (A)}{\sqrt {n}} \leq \nu (A) \leq \Delta_ {F} (A),
$$

where $\nu(A) = \min\{\|E\|_F : A + E$ is normal\}. Henrici uses the departure from normality to derive the 2-norm bounds

$$
\left\| A ^ {k} \right\| _ {2} \leq \left\{ \begin{array}{l l} \sum_ {i = 0} ^ {n - 1} \binom {k} {i} \rho (A) ^ {k - i} \Delta_ {2} (A) ^ {i}, & \rho (A) > 0, \\ \Delta_ {2} (A) ^ {k}, & \rho (A) = 0 \text {a n d} k <   n. \end{array} \right. \tag {18.7}
$$

Empirical evidence suggests that the first bound in (18.7) can be very pessimistic. However, for normal matrices both the bounds are equalities.

Another bound involving nonnormality is given by Golub and Van Loan [509, 1996, Lem. 7.3.2]. They show that, in the above notation,

$$
\left\| A ^ {k} \right\| _ {2} \leq (1 + \theta) ^ {n - 1} \left(\rho (A) + \frac {\Delta_ {F} (A)}{1 + \theta}\right) ^ {k}
$$

for any $\theta \geq 0$ . This bound is an analogue of (18.5) with the Schur form replacing the Jordan form. Again, there is equality when $A$ is normal (if we set $\theta = 0$ ).

To compare bounds based on the Schur form with ones based on the Jordan form we need to compare $\Delta(A)$ with $\kappa(X)$ . If $A$ is diagonalizable then [795, 1969, Thm. 4]

$$
\kappa_ {2} (X) \geq \left(1 + \frac {\varDelta_ {F} (A) ^ {2}}{\| A \| _ {F} ^ {2}}\right) ^ {1 / 2};
$$

it can be shown by a $2 \times 2$ example that $\min_X \kappa_2(X)$ can exceed $\varDelta_F(A)/\|A\|_F$ by an arbitrary factor [224, 1993, §4.2.7], [208, 1996, §9.1.1].

Another tool that can be used to bound the norms of powers is the pseudospectrum of a matrix, popularized by Trefethen [389], [1154, 1992], [1155, 1999]. The $\epsilon$ -pseudospectrum of $A \in \mathbb{C}^{n \times n}$ is defined, for a given $\epsilon > 0$ , to be the set

$$
\Lambda_ {\epsilon} (A) = \{z: z \text {i s a n e i g e n v a l u e o f} A + E \text {f o r s o m e} E \text {w i t h} \| E \| _ {2} \leq \epsilon \},
$$

and it can also be represented, in terms of the resolvent $(zI - A)^{-1}$ , as

$$
\varLambda_ {\epsilon} (A) = \left\{z: \| (z I - A) ^ {- 1} \| _ {2} \geq \epsilon^ {- 1} \right\}.
$$

As Trefethen notes [1154, 1992], by using the Cauchy integral representation of $A^k$ (which involves a contour integral of the resolvent) one can show that

$$
\left\| A ^ {k} \right\| _ {2} \leq \epsilon^ {- 1} \rho_ {\epsilon} (A) ^ {k + 1}, \tag {18.8}
$$

where the $\epsilon$ -pseudospectral radius

$$
\rho_ {\epsilon} (A) = \max  \left\{\left| z \right|: z \in \Lambda_ {\epsilon} (A) \right\}. \tag {18.9}
$$

This bound is very similar in flavour to (18.5). The difficulty is transferred from estimating $\kappa(X)$ to choosing $\epsilon$ and estimating $\rho_{\epsilon}(A)$ .

Bai, Demmel, and Gu [48, 1997] consider $A$ with $\rho(A) < 1$ and manipulate the Cauchy integral representation of $A^k$ in a slightly different way from Trefethen to produce a bound in terms of the distance to the nearest unstable matrix,

$$
\begin{array}{l} d (A) = \min  \left\{\| \Delta A \| _ {2}: A + \Delta A \text {h a s a n e i g e n v a l u e o f m o d u l u s} 1 \right\} \\ = \min  \left\{\epsilon : \rho_ {\epsilon} (A) = 1 \right\}. \\ \end{array}
$$

Their bound is

$$
\| A ^ {k} \| _ {2} \leq \left\{ \begin{array}{l l} m \alpha_ {m} (1 - d (A)) ^ {m}, & m > (1 - d (A)) / d (A), \\ 1 / d (A), & m \leq (1 - d (A)) / d (A), \end{array} \right.
$$

where $e \leq \alpha_{m} := (1 + 1/m)^{m+1} \leq 4$ . Note that $d(A) \leq 1$ when $\rho(A) < 1$ , as is easily seen from the Schur decomposition. The distance $d(A)$ is not easy to compute. One approach is a bisection technique of Byers [194, 1988].

Finally, we mention that the Kreiss matrix theorem provides a good estimate of $\sup_{k\geq 0}\| A^k\|$ for a general $A\in \mathbb{C}^{n\times n}$ , albeit in terms of an expression that involves the resolvent and is not easy to compute:

$$
\phi (A) \leq \sup  _ {k \geq 0} \| A ^ {k} \| _ {2} \leq n e \phi (A),
$$

where $\phi(A) = \sup \left\{ (|z| - 1) \| (zI - A)^{-1} \|_2 : |z| > 1 \right\}$ and $e = \exp(1)$ . Details and references are given by Wegert and Trefethen [1212, 1994].

# 18.2. Bounds for Finite Precision Arithmetic

The formulae $A \cdot A^k$ or $A^k \cdot A$ can be implemented in several ways, corresponding to different loop orderings in each individual product, but as long as each product is formed using the standard formula $(AB)_{ij} = \sum_k a_{ik} b_{kj}$ , all these variations satisfy the same rounding error bounds. We do not analyse here the use of the binary powering technique, where, for example, $A^9$ is formed as $A((A^2)^2)$ ; alternate multiplication on the left and right $(fl(A^k) = fl(Afl(A^{k-2})A))$ ; or fast matrix multiplication techniques such as Strassen's method. None of these methods is equivalent to repeated multiplication in finite precision arithmetic.

We suppose, without loss of generality, that the columns of $A^m$ are computed one at a time, the $j$ th as $fl(A(A(\ldots (Ae_j)\ldots)))$ , where $e_j$ is the $j$ th unit vector. The error analysis for matrix-vector multiplication shows that the $j$ th computed column of $A^m$ satisfies

$$
f l \left(A ^ {m} e _ {j}\right) = \left(A + \Delta A _ {1}\right) \left(A + \Delta A _ {2}\right) \dots \left(A + \Delta A _ {m}\right) e _ {j}, \tag {18.10}
$$

where, for both real and complex matrices, we have (Problem 3.7)

$$
\left| \Delta A _ {i} \right| \leq \gamma_ {n + 2} | A |. \tag {18.11}
$$

It follows that

$$
\left| f l \left(A ^ {m} e _ {j}\right) \right| \leq \left(1 + \gamma_ {n + 2}\right) ^ {m} \left| A \right| ^ {m} e _ {j},
$$

and so a sufficient condition for convergence of the computed powers is that

$$
\rho (| A |) <   \frac {1}{1 + \gamma_ {n + 2}}. \tag {18.12}
$$

This result is useful in certain special cases: $\rho(|A|) = \rho(A)$ if $A$ is triangular or has a checkerboard sign pattern (since then $|A| = DAD^{-1}$ where $D = \mathrm{diag}(\pm 1)$ ); if $A$ is normal then $\rho(|A|) \leq \sqrt{n}\rho(A)$ (this bound being attained for a Hadamard matrix); and in Markov processes, where the $a_{ij}$ are transition probabilities, $|A| = A$ . However, in general $\rho(|A|)$ can exceed $\rho(A)$ by an arbitrary factor (see Problem 18.2).

To obtain sharper and more informative results it is necessary to use more information about the matrix. In the following theorem we give a sufficient condition, based on the Jordan canonical form, for the computed powers of a matrix to converge to zero. Although the Jordan form is usually eschewed by numerical analysts because of its sensitivity to perturbations, it is convenient to work with in this application and leads to an informative result.

Theorem 18.1 (Higham and Knight). Let $A \in \mathbb{C}^{n \times n}$ with the Jordan form (18.1) have spectral radius $\rho(A) < 1$ . A sufficient condition for $fl(A^m) \to 0$ as $m \to \infty$ is

$$
4 t \gamma_ {n + 2} \kappa_ {\infty} (X) \| A \| _ {\infty} <   (1 - \rho (A)) ^ {t}, \tag {18.13}
$$

where $t = \max_{i}n_{i}$

Proof. It is easy to see that if we can find a nonsingular matrix $S$ such that

$$
\| S ^ {- 1} A S \| _ {\infty} + \kappa_ {\infty} (S) \| \Delta A _ {i} \| _ {\infty} <   1 \tag {18.14}
$$

for all $i$ , then the product

$$
(A + \Delta A _ {1}) \dots (A + \Delta A _ {m}) = S \left(S ^ {- 1} A S + S ^ {- 1} \Delta A _ {1} S\right) \dots \left(S ^ {- 1} A S + S ^ {- 1} \Delta A _ {m} S\right) S ^ {- 1}
$$

tends to 0 as $m \to \infty$ . In the rest of the proof we construct such a matrix $S$ for the $\Delta A_i$ in (18.10).

Let $P(\epsilon) = \mathrm{diag}(P_1(\epsilon),\ldots ,P_s(\epsilon))$ where $0 < \epsilon < 1 - \rho (A)$ and

$$
P _ {i} (\epsilon) = \operatorname {d i a g} \left(\left(1 - \left| \lambda_ {i} \right| - \epsilon\right) ^ {1 - n _ {i}}, \left(1 - \left| \lambda_ {i} \right| - \epsilon\right) ^ {2 - n _ {i}}, \dots , 1\right) \in \mathbb {R} ^ {n _ {i} \times n _ {i}}.
$$

Now consider the matrix $P(\epsilon)^{-1}JP(\epsilon)$ . Its $i$ th diagonal block is of the form $\lambda_i I + (1 - |\lambda_i| - \epsilon)N$ , where the only nonzeros in $N$ are 1s on the first superdiagonal, and so

$$
\| P (\epsilon) ^ {- 1} X ^ {- 1} A X P (\epsilon) \| _ {\infty} = \| P (\epsilon) ^ {- 1} J P (\epsilon) \| _ {\infty} \leq \max _ {i} \big (| \lambda_ {i} | + 1 - | \lambda_ {i} | - \epsilon \big) = 1 - \epsilon .
$$

Defining $S = XP(\epsilon)$ , we have $\| S^{-1}AS\|_{\infty}\leq 1 - \epsilon$ and

$$
\kappa_ {\infty} (S) \leq \kappa_ {\infty} (P (\epsilon)) \kappa_ {\infty} (X) \leq (1 - \rho (A) - \epsilon) ^ {1 - t} \kappa_ {\infty} (X). \tag {18.15}
$$

Now we set $\epsilon = \theta (1 - \rho (A))$ where $0 < \theta < 1$ and we determine $\theta$ so that (18.14) is satisfied, that is, so that $\kappa_{\infty}(S)\| \varDelta A_i\|_{\infty}< \epsilon$ for all $i$ . From (18.11) and (18.15) we have

$$
\kappa_ {\infty} (S) := \| \varDelta A _ {i} \| _ {\infty} \leq \gamma_ {n + 2} (1 - \theta) ^ {1 - t} (1 - \rho (A)) ^ {1 - t} \kappa_ {\infty} (X) \| A \| _ {\infty}.
$$

Therefore (18.14) is satisfied if

$$
\gamma_ {n + 2} (1 - \theta) ^ {1 - t} (1 - \rho (A)) ^ {1 - t} \kappa_ {\infty} (X) \| A \| _ {\infty} <   \theta (1 - \rho (A)),
$$

that is, if

$$
\gamma_ {n + 2} \kappa_ {\infty} (X) \| A \| _ {\infty} <   (1 - \theta) ^ {t - 1} \theta (1 - \rho (A)) ^ {t}.
$$

If the integer $t$ is greater than 1 then the function $f(\theta) = (1 - \theta)^{t - 1}\theta$ has a maximum on $[0,1]$ at $\theta_{*} = t^{-1}$ and $f(\theta_{*}) = (t - 1)^{-1}(1 - t^{-1})^{t}$ satisfies $(4(t - 1))^{-1} \leq f(\theta_{*}) < e^{-1}$ . We conclude that for all integers $1 \leq t \leq n$ ,

$$
\gamma_ {n + 2} \kappa_ {\infty} (X) \| A \| _ {\infty} <   \frac {1}{4 t} (1 - \rho (A)) ^ {t}
$$

is sufficient to ensure that (18.14) holds.

If $A$ is normal then $\| A \|_2 = \rho(A) < 1$ , $t = 1$ , and $\kappa_2(X) = 1$ , so (18.13) can be written in the form

$$
\rho (A) <   \frac {1}{1 + c _ {n} u},
$$

where $c_{n}$ is a constant depending on $n$ . This condition is also easily derived by taking 2-norms in (18.10) and (18.11).

We can show the sharpness of the condition in Theorem 18.1 by using the Chebyshev spectral differentiation matrix $C_n \in \mathbb{R}^{n \times n}$ described by Trefethen and Trummer [1158, 1987]. The matrix $C_n$ arises from degree $n - 1$ polynomial interpolation of $n$ arbitrary data values at $n$ Chebyshev points, including a boundary condition at 1. It is nilpotent and is similar to a single Jordan block of dimension $n$ . We generate $C_n$ in MATLAB using gallery('chebspec', n). Figure 18.4 shows the norms of the powers of four variants of the $C_n$ matrix.

The powers of $C_8$ converge to zero, while the powers of $15C_8$ diverge. Using a technique for estimating $\kappa_2(X)$ described in [620, 1995], it can be shown that $u\kappa_2(X)\|C_8\|_2 \approx 1.08 \times 10^{-9}$ , which is safely less than 1, so that Theorem 18.1 predicts convergence. For $15C_8$ we have $u\kappa_2(X)\|15C_8\|_2 \approx 2.7$ , so the theorem correctly does not predict convergence.

Next, for the matrix $A = C_{13} + 0.36I$ , whose powers diverge, we have $u\kappa_2(X) \times \|A\|_2 / (1 - \rho(A))^{13} \approx 13.05$ , and for $A = C_{13} + 0.01I$ , whose powers converge, $u\kappa_2(X)\|A\|_2 / (1 - \rho(A))^{13} \approx 0.01$ , so again the theorem is reasonably sharp.

The plots reveal interesting scalloping patterns in the curves of the norms. For $C_8$ and $15C_8$ the dips are every eight powers, but the point of first dip and the dipping intervals are altered by adding different multiples of the identity matrix, as shown by the $C_{13}$ examples. Explaining this behaviour is an open problem (see Problem 18.3).

We saw in the last section that the powers of $A$ can be bounded in terms of the pseudospectral radius. Can the pseudospectrum provide information about

![](images/9070f594b65e64fc2caac1d5f0c645669724eddf878a167af3f49ec7d47aaf57.jpg)

![](images/43919ea9e0bf260142b47c1d7626ba726d630f18ec24d08187f0cacc1e48b57b.jpg)

![](images/010b307726103d58d0ea6ea63bd7be0114d9b747d995a5249e56b3cfcc2c200a.jpg)

![](images/95aa3ec6e23bff0f986e062e8d396d673a45ded30273dc4f2b5f62adcf158bf2.jpg)  
Figure 18.4. Computed powers of chebspec matrices.

the behaviour of the computed powers? Figure 18.5 shows approximations to the $\epsilon$ -pseudospectra for the matrices used in Figure 18.4, where $\epsilon = n\|A\|_2u$ ; the (computed) eigenvalues are plotted as crosses “ $\times$ ”. We see that the pseudospectrum lies inside the unit disc precisely when the powers converge to zero.

A heuristic argument based on (18.10) and (18.11) suggests that, if for randomly chosen perturbations $\Delta A_{i}$ with $\| \Delta A_i\| \leq c_n u\| A\|$ , most of the eigenvalues of the perturbed matrices lie outside the unit disc, then we can expect a high percentage of the terms $A + \Delta A_{i}$ in (18.10) to have spectral radius bigger than 1 and hence we can expect the product to diverge. On the other hand, if the $c_{n}u\| A\|$ -pseudospectrum is wholly contained within the unit disc, each $A + \Delta A_{i}$ will have spectral radius less than 1 and the product can be expected to converge. (Note, however, that if $\rho (A) < 1$ and $\rho (B) < 1$ it is not necessarily the case that $\rho (AB) < 1$ .) To make this heuristic precise, we need an analogue of Theorem 18.1 phrased in terms of the pseudospectrum rather than the Jordan form.

Theorem 18.2 (Higham and Knight). Suppose that $A \in \mathbb{C}^{n \times n}$ is diagonalizable with $A = X \operatorname{diag}(\lambda_i)X^{-1}$ and has a unique eigenvalue $\lambda_1$ of largest modulus. Suppose that $\|X\|_1 = \sum_{i=1}^n |x_{i1}|$ and $\|X^{-1}\|_\infty = \sum_{j=1}^n |y_{1j}|$ , where $X^{-1} = (y_{ij})$ . If $\rho_\epsilon(A) < 1$ for $\epsilon = c_n u \|A\|_2$ , where $c_n$ is a constant depending only on $n$ , then, provided that a certain $O(\epsilon^2)$ term can be ignored, $\lim_{m \to \infty} fl(A^m) = 0$ .

Proof. It can be shown (see [620, 1995]) that the conditions on $\|X\|_1$ and $\|X^{-1}\|_\infty$ imply there is a perturbation $\widetilde{A} = A + \Delta A$ of $A$ with $\| \Delta A \|_2 = \epsilon$ such that

$$
\rho (\widetilde {A}) \geq \rho (A) + \frac {\kappa_ {2} (X) \epsilon}{n ^ {2}} + O (\epsilon^ {2}).
$$

![](images/4f018afbb9ae914386483eeac4bca5e292b3147a305fad06af7b175d3ce158c0.jpg)  
chebspec(13) + 0.01*eye(13)

![](images/68bdfcc078fbcb87e4a4cc24ff5b6025b71b06cc8d08670139f374e6e31b2091.jpg)  
chebspec(13) + 0.36*eye(13)

![](images/93d17c4c04cfba4d6ecf8a29716363dd795edf023dba5d87acd4946291226971.jpg)

![](images/bd2c769aebad4f6cfcf28c13b9b5b333f2315943e825abeb3f54d4a219681fdb.jpg)  
Figure 18.5. Pseudospectra for chebspec matrices.

Hence, if $\rho_{\epsilon}(A) < 1$ then $\rho(A) + \kappa_2(X)\epsilon/n^2 < 1 + O(\epsilon^2)$ . Ignoring the $O(\epsilon^2)$ term and rearranging gives

$$
c _ {n} u \kappa_ {2} (X) \| A \| _ {2} / n ^ {2} <   1 - \rho (A).
$$

Using Theorem 18.1 we have the required result for $c_n = 4n^2 (n + 2)$ , since $t = 1$ .

Suppose we compute the eigenvalues of $A$ by a backward stable algorithm, that is, one that yields the exact eigenvalues of $A + E$ , where $\| E \|_2 \leq c_n u \| A \|_2$ , with $c_n$ a modest constant. (An example of such an algorithm is the QR algorithm [509, 1996, §7.5]). Then the computed spectral radius $\widehat{\rho}$ satisfies $\widehat{\rho} \leq \rho_{c_n u \| A \|_2}(A)$ . In view of Theorem 18.2 we can formulate a rule of thumb—one that bears a pleasing symmetry with the theoretical condition for convergence:

The computed powers of $A$ can be expected to converge to 0 if the spectral radius computed via a backward stable eigensolver is less than 1.

This rule of thumb has also been discussed by Trefethen and Trummer [1158, 1987] and Reichel and Trefethen [978, 1992]. In our experience the rule of thumb is fairly reliable when $\widehat{\rho}$ is not too close to 1. For the matrices used in our examples we have, using MATLAB's eig function,

$$
\widehat {\rho} \left(C _ {8}\right) = 0. 0 6 7, \quad \widehat {\rho} \left(1 5 C _ {8}\right) = 0. 9 8, \quad \widehat {\rho} \left(C _ {1 4}\right) = 1. 0 0 4,
$$

$$
\widehat {\rho} (C _ {1 3} + 0. 0 1 I) = 0. 7 2, \quad \widehat {\rho} (C _ {1 3} + 0. 3 6 I) = 1. 0 5,
$$

and we observed convergence of the computed powers for $C_8$ and $C_{13} + 0.01I$ and divergence for the other matrices.

![](images/6e6ee99148d89a4a56ca00d75aa0bc4456845b655d6d057ff129793e4b5b04f1.jpg)  
Figure 18.6. Pseudospectrum for SOR iteration matrix.

# 18.3. Application to Stationary Iteration

As we saw in the previous chapter, the errors in stationary iteration satisfy $e_k = (M^{-1}N)^k e_0$ , so convergence of the iteration depends on the convergence of $(M^{-1}N)^k$ to zero as $k \to \infty$ . While the errors in stationary iteration are not precisely modelled by the errors in matrix powering, because matrix powers are not formed explicitly, the behaviour of the computed powers $fl((M^{-1}N)^k)$ can be expected to give some insight into the behaviour of stationary iteration.

For the successive overrelaxation (SOR) example at the start of Chapter 17, the matrix $G = M^{-1}N$ is lower triangular with $g_{ij} = 0.5(-1)^{i - j}$ . The computed powers of $G$ in MATLAB reach a maximum norm of $\approx 10^{28}$ at $k = 99$ and then decay to zero; the eventual convergence is inevitable in view of the condition (18.12), which clearly is satisfied for this triangular $G$ . An approximation to the $u\| G\| _2$ -pseudospectrum is plotted in Figure 18.6, and we see clearly that part of the pseudospectrum lies outside the unit disk. These facts are consistent with the nonconvergence of the SOR iteration (see Figure 17.1).

That the pseudospectrum of $G$ gives insight into the behaviour of stationary iteration has also been observed by Trefethen [1152, 1990], [1154, 1992] and Chatelin and Frayssé [226, 1992], but no rigorous results about the connection are available.

# 18.4. Notes and References

This chapter is based closely on Higham and Knight [620, 1995].

The analysis for the powers of the matrix (18.2) is modelled on that of Stewart [1077, 1997], who uses the matrix to construct a Markov chain whose second

largest eigenvalue does not correctly predict the decay of the transient.

For some results on the asymptotic behaviour of the powers of a nonnegative matrix, see Friedland and Schneider [446, 1980].

Another application of matrix powering is in the scaling and squaring method for computing the matrix exponential, which uses the identity $e^A = (e^{A / m})^m$ together with a Taylor or Padé approximation to $e^{A / m}$ ; see Moler and Van Loan [868, 1978].

# Problems

18.1. Let $A \in \mathbb{C}^{n \times n}$ be diagonalizable: $A = X \Lambda X^{-1}$ , $\Lambda = \mathrm{diag}(\lambda_i)$ . Construct a parametrized example to show that the bound $\| A^k \|_2 \leq \kappa_2(X) \rho(A)^k$ can be arbitrarily weak.   
18.2. Show that $\rho(|A|)/\rho(A)$ can be arbitrarily large for $A \in \mathbb{R}^{n \times n}$ .   
18.3. (RESEARCH PROBLEM) Explain the scalloping patterns in the curves of norms of powers of a matrix, as seen, for example, in Figure 18.4. (Consider exact arithmetic, as the phenomenon is not rounding error dependent.)   
18.4. (RESEARCH PROBLEM) Obtain a sharp sufficient condition for $fl(A^k) \to 0$ in terms of the Schur decomposition of $A \in \mathbb{C}^{n \times n}$ with $\rho(A) < 1$ .
