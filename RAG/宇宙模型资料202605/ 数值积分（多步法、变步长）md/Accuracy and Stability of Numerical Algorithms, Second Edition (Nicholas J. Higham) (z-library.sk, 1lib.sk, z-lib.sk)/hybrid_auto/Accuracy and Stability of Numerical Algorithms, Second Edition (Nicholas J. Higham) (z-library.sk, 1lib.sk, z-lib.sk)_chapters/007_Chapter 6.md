# Chapter 6

# Norms

While it is true that all norms are equivalent theoretically, only a homely one like the $\infty$ -norm is truly useful numerically. — J. H. WILKINSON<sup>9</sup>, Lecture at Stanford University (1984)

Matrix norms are defined in many different ways in the older literature, but the favorite was the Euclidean norm of the matrix considered as a vector in $n^2$ -space. Wedderburn (1934) calls this the absolute value of the matrix and traces the idea back to Peano in 1887. ALSTON S. HOUSEHOLDER, The Theory of Matrices in Numerical Analysis (1964)

Norms are an indispensable tool in numerical linear algebra. Their ability to compress the $mn$ numbers in an $m \times n$ matrix into a single scalar measure of size enables perturbation results and rounding error analyses to be expressed in a concise and easily interpreted form. In problems that are badly scaled, or contain a structure such as sparsity, it is often better to measure matrices and vectors componentwise. But norms remain a valuable instrument for the error analyst, and in this chapter we describe some of their most useful and interesting properties.

# 6.1. Vector Norms

A vector norm is a function $\| \cdot \| : \mathbb{C}^n \to \mathbb{R}$ satisfying the following conditions:

1. $\| x\| \geq 0$ with equality iff $x = 0$   
2. $\| \alpha x\| = |\alpha |\| x\|$ for all $\alpha \in \mathbb{C}$ , $x\in \mathbb{C}^n$   
3. $\| x + y\| \leq \| x\| +\| y\|$ for all $x,y\in \mathbb{C}^n$ (the triangle inequality).

The three most useful norms in error analysis and in numerical computation are

$$
\begin{array}{l} \| x \| _ {1} = \sum_ {i = 1} ^ {n} | x _ {i} |, \quad \text {" M a n h a t t a n " o r " t a x i c a b " n o r m ,} \\ \| x \| _ {2} = \left(\sum_ {i = 1} ^ {n} | x _ {i} | ^ {2}\right) ^ {1 / 2} = (x ^ {*} x) ^ {1 / 2}, \quad \text {E u c l i d e a n l e n g t h}, \\ \| x \| _ {\infty} = \max  _ {1 \leqslant i \leqslant n} | x _ {i} |. \\ \end{array}
$$

These are all special cases of the Hölder $p$ -norm:

$$
\left\| x \right\| _ {p} = \left(\sum_ {i = 1} ^ {n} | x _ {i} | ^ {p}\right) ^ {1 / p}, \qquad p \geq 1.
$$

The 2-norm has two properties that make it particularly useful for theoretical purposes. First, it is invariant under unitary transformations, for if $Q^{*}Q = I$ , then $\| Qx\|_{2}^{2} = x^{*}Q^{*}Qx = x^{*}x = \| x\|_{2}^{2}$ . Second, the 2-norm is differentiable for all $x$ , with gradient vector $\nabla \| x\|_{2} = x / \| x\|_{2}$ .

A fundamental inequality for vectors is the Hölder inequality (see, for example, [547, 1967, App. 1])

$$
\left| x ^ {*} y \right| \leq \| x \| _ {p} \| y \| _ {q}, \quad \frac {1}{p} + \frac {1}{q} = 1. \tag {6.1}
$$

This is an equality when $p, q > 1$ if the vectors $(|x_i|^p)$ and $(|y_i|^q)$ are linearly dependent and $x_i y_i$ lies on the same ray in the complex plane for all $i$ ; equality is also possible when $p = 1$ and $p = \infty$ , as is easily verified. The special case with $p = q = 2$ is called the Cauchy-Schwarz inequality:

$$
\left| x ^ {*} y \right| \leq \left\| x \right\| _ {2} \| y \| _ {2}.
$$

For an arbitrary vector norm $\| \cdot \|$ the dual norm is defined by

$$
\| x \| _ {D} = \max  _ {z \neq 0} \frac {\left| z ^ {*} x \right|}{\| z \|}. \tag {6.2}
$$

It follows from the Hölder inequality that the dual of the $p$ -norm is the $q$ -norm, where $p^{-1} + q^{-1} = 1$ . The definition of dual norm yields, trivially, the general Hölder inequality $|x^{*}y| \leq \| x\| \| y\|_{D}$ . For a proof of the reassuring result that the dual of the dual norm is the original norm (the "duality theorem") see Horn and Johnson [636, 1985, Thm. 5.5.14].

In some analyses we need the vector $z$ dual to $y$ , which is defined by the property

$$
z ^ {*} y = \| z \| _ {D} \| y \| = 1. \tag {6.3}
$$

That such a vector $z$ exists is a consequence of the duality theorem (see [636, 1985, Cor. 5.5.15]).

How much two $p$ -norms of a vector can differ is shown by the attainable inequalities [462, 1983, pp. 27-28], [498, 1983, Lem. 1.1]

$$
\left\| x \right\| _ {p _ {2}} \leq \left\| x \right\| _ {p _ {1}} \leq n ^ {\left(\frac {1}{p _ {1}} - \frac {1}{p _ {2}}\right)} \left\| x \right\| _ {p _ {2}}, \quad p _ {1} \leq p _ {2}. \tag {6.4}
$$

The $p$ -norms have the properties that $\| x\|$ depends only on the absolute value of $x$ , and the norm is an increasing function of the absolute values of the entries of $x$ . These properties are important enough to warrant a definition.

# Definition 6.1. A norm on $\mathbb{C}^n$ is

1. monotone if $|x| \leq |y| \Rightarrow \| x \| \leq \| y \|$ for all $x, y \in \mathbb{C}^n$ , and   
2. absolute if $\| |x| \| = \| x \|$ for all $x \in \mathbb{C}^n$ .

The following nonobvious theorem shows that these two properties are equivalent.

Theorem 6.2 (Bauer, Stoer, and Witzgall). A norm on $\mathbb{C}^n$ is monotone if and only if it is absolute.

Proof. See Horn and Johnson [636, 1985, Thm. 5.5.10], or Stewart and Sun [1083, 1990, Thm. 2.1.3]. $\square$

# 6.2. Matrix Norms

A matrix norm is a function $\| \cdot \| : \mathbb{C}^{m \times n} \to \mathbb{R}$ satisfying obvious analogues of the three vector norm properties. The simplest example is the Frobenius norm

$$
\| A \| _ {F} = \left(\sum_ {i = 1} ^ {m} \sum_ {j = 1} ^ {n} | a _ {i j} | ^ {2}\right) ^ {1 / 2} = \left(\mathrm {t r a c e} (A ^ {*} A)\right) ^ {1 / 2}
$$

(which is sometimes called the Euclidean norm and denoted $\| \cdot \| _E$ ).

A very important class of matrix norms are those subordinate to vector norms. Given a vector norm on $\mathbb{C}^n$ , the corresponding subordinate matrix norm on $\mathbb{C}^{m\times n}$ is defined by

$$
\| A \| = \max  _ {x \neq 0} \frac {\| A x \|}{\| x \|}, \tag {6.5}
$$

or, equivalently,

$$
\| A \| = \max  _ {\| x \| = 1} \| A x \|.
$$

(Strictly speaking, this definition uses two different norms: one on $\mathbb{C}^m$ in the numerator of (6.5) and one on $\mathbb{C}^n$ in the denominator. Thus the norm used in the definition is assumed to form a family defined on $\mathbb{C}^s$ for any $s$ .)

For the 1-, 2-, and $\infty$ -vector norms it can be shown that

$$
\begin{array}{l} \| A \| _ {1} = \max  _ {1 \leq j \leq n} \sum_ {i = 1} ^ {m} | a _ {i j} |, \quad \text {" m a x c o l u m n s u m "}, \\ \| A \| _ {\infty} = \max  _ {1 \leq i \leq m} \sum_ {j = 1} ^ {n} | a _ {i j} |, \quad \text {" m a x r o w s u m "}, \\ \| A \| _ {2} = \left(\rho \left(A ^ {*} A\right)\right) ^ {1 / 2} = \sigma_ {\max } (A), \quad \text {s p e c t r a l n o r m}, \\ \end{array}
$$

where the spectral radius

$$
\rho (B) = \max  \left\{\left| \lambda \right|: \det  (B - \lambda I) = 0 \right\},
$$

and where $\sigma_{\max}(A)$ denotes the largest singular value of $A$ . To remember the formulae for the 1- and $\infty$ -norms, note that 1 is a vertical symbol (for columns) and $\infty$ is a horizontal symbol (for rows).

From the expression for the $\infty$ -norm it is immediate that

$$
\left\| A \right\| _ {\infty} = \left\| \left| A \right| e \right\| _ {\infty}, \qquad e = [ 1, 1, \dots , 1 ] ^ {T},
$$

where $|A| = (|a_{ij}|)$ . This useful relation will be employed frequently in later chapters.

A norm is consistent if it satisfies $\| AB\| \leq \| A\| \| B\|$ whenever the product $AB$ is defined. The Frobenius norm and all subordinate norms are consistent. An example of a norm that is not consistent is the "max norm" $\| A\| = \max_{i,j}|a_{ij}|$ . The best bound that holds for all $A\in \mathbb{C}^{m\times n}$ and $B\in \mathbb{C}^{n\times p}$ is $\| AB\| \leq n\| A\| \| B\|$ , with equality when $a_{ij}\equiv 1$ and $b_{ij}\equiv 1$ .

A norm for which $\| UAV\| = \| A\|$ for all unitary $U$ and $V$ is called a unitarily invariant norm. These norms have an interesting theory, which we will not explore here (see [107, 1997, Chap. 4], [637, 1991, §3.5], or [1083, 1990, §2.3]). Only two unitarily invariant norms will be needed for our analysis: the 2-norm and the Frobenius norm. That these two norms are unitarily invariant follows easily from the formulae above. For any unitarily invariant norm, the useful property holds that $\| A^{*}\| = \| A\|$ . The 2-norm satisfies the additional relation $\| A^{*}A\|_{2} = \| A\|_{2}^{2}$ .

The unitary invariance of the 2- and Frobenius norms has implications for error analysis, for it means that multiplication by unitary matrices does not magnify

Table 6.1. Constants $\alpha_{pq}$ such that $\| x\| _p\leq \alpha_{pq}\| x\| _q$ $x\in \mathbb{C}^n$   

<table><tr><td></td><td></td><td colspan="3">q</td></tr><tr><td></td><td>1</td><td>2</td><td>∞</td><td></td></tr><tr><td rowspan="3">p</td><td>1</td><td>√n</td><td>n</td><td></td></tr><tr><td>2</td><td>1</td><td>√n</td><td></td></tr><tr><td>∞</td><td>1</td><td>1</td><td>1</td></tr></table>

Table 6.2. Constants $\alpha_{pq}$ such that $\| A\| _p\leq \alpha_{pq}\| A\| _q$ $A\in \mathbb{C}^{m\times n}$ . Here, $\| A\| _M\coloneqq \max_{i,j}|a_{ij}|$ and $\| A\| _S\coloneqq \sum_{i,j}|a_{ij}|$ .   

<table><tr><td rowspan="2" colspan="2"></td><td colspan="6">q</td></tr><tr><td>1</td><td>2</td><td>∞</td><td>F</td><td>M</td><td>S</td></tr><tr><td rowspan="6">p</td><td>1</td><td>1</td><td>√m</td><td>m</td><td>√m</td><td>m</td><td>1</td></tr><tr><td>2</td><td>√n</td><td>1</td><td>√m</td><td>1</td><td>√mn</td><td>1</td></tr><tr><td>∞</td><td>n</td><td>√n</td><td>1</td><td>√n</td><td>n</td><td>1</td></tr><tr><td>F</td><td>√n</td><td>√rank(A)</td><td>√m</td><td>1</td><td>√mn</td><td>1</td></tr><tr><td>M</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>S</td><td>n</td><td>√mn rank(A)</td><td>m</td><td>√mn</td><td>mn</td><td>1</td></tr></table>

errors. For example, if $A \in \mathbb{C}^{n \times n}$ is contaminated by errors $E$ and $Q$ is unitary, then

$$
Q (A + E) Q ^ {*} = Q A Q ^ {*} + F,
$$

and $\| F\| _2 = \| QEQ^*\| _2 = \| E\| _2$ . In contrast, if we do a general, nonsingular similarity transformation

$$
X (A + E) X ^ {- 1} = X A X ^ {- 1} + G,
$$

then $\| G\| _2 = \| EX^{-1}\| _2\leq \kappa_2(X)\| E\| _2$ , where

$$
\kappa (X) = \| X \| \| X ^ {- 1} \|
$$

is the condition number of $X$ . The condition number satisfies $\kappa(X) \geq 1$ ( $\kappa_F(X) \geq \sqrt{n}$ ) and can be arbitrarily large. Justification for calling $\kappa$ a condition number is found in Theorem 6.4 below.

In perturbation theory and error analysis it is often necessary to switch between norms. Therefore inequalities that bound one norm in terms of another are required. It is well known that on a finite-dimensional space any two norms differ by at most a constant that depends only on the dimension (so-called norm equivalence). Tables 6.1 and 6.2 give attainable inequalities for the vector and matrix norms of most interest.

The definition of subordinate matrix norm can be generalized by permitting different norms on the input and output space:

$$
\| A \| _ {\alpha , \beta} = \max  _ {x \neq 0} \frac {\| A x \| _ {\beta}}{\| x \| _ {\alpha}}. \tag {6.6}
$$

Note that, in general, the submultiplicative property $\| AB\|_{\alpha ,\beta}\leq \| A\|_{\alpha ,\beta}\| B\|_{\alpha ,\beta}$ does not hold, but we do have

$$
\| A B \| _ {\alpha , \beta} \leq \| A \| _ {\gamma , \beta} \| B \| _ {\alpha , \gamma}, \tag {6.7}
$$

for any third vector norm $\| \cdot \|_{\gamma}$ . The choice $\alpha = 1$ and $\beta = \infty$ produces the max norm, mentioned above, $\| A\|_{1,\infty} = \max_{i,j}|a_{ij}|$ .

At least two important results about matrix norms hold for this mixed subordinate norm. The first is a simple formula for the matrix condition number of a nonsingular $A \in \mathbb{C}^{n \times n}$ , defined by

$$
\kappa_{\alpha ,\beta}(A):= \lim_{\epsilon \to 0}\sup_{\| \varDelta A\|_{\alpha ,\beta}\leq \epsilon \| A\|_{\alpha ,\beta}}\left(\frac{\|(A + \varDelta A)^{-1} - A^{-1}\|_{\beta,\alpha}}{\epsilon\|A^{-1}\|_{\beta,\alpha}}\right).
$$

Note that this definition uses the $\| \cdot \|_{\alpha, \beta}$ norm on the data space and the $\| \cdot \|_{\beta, \alpha}$ norm on the solution space, as is natural.

We need the following lemma.

Lemma 6.3. Given vector norms $\| \cdot \|_{\alpha}$ and $\| \cdot \|_{\beta}$ and vectors $x \in \mathbb{C}^n$ , $y \in \mathbb{C}^m$ such that $\| x \|_{\alpha} = \| y \|_{\beta} = 1$ , there exists a matrix $B \in \mathbb{C}^{m \times n}$ with $\| B \|_{\alpha, \beta} = 1$ such that $Bx = y$ .

Proof. Recall that the dual of the $\alpha$ -norm is defined by $\|z\|_{\alpha}^{D} = \max_{\|w\|_{\alpha}=1} |z^{*}w|$ . Let $z$ be a vector dual to $x$ , so that $z^{*}x = \|z\|_{\alpha}^{D}\|x\|_{\alpha} = 1$ , and hence $\|z\|_{\alpha}^{D} = 1$ . Let $B = yz^{*}$ . Then $Bx = y$ and

$$
\| B \| _ {\alpha , \beta} = \max  _ {\| w \| _ {\alpha} = 1} \| y z ^ {*} w \| _ {\beta} = \| y \| _ {\beta} \max  _ {\| w \| _ {\alpha} = 1} | z ^ {*} w | = \| y \| _ {\beta} \| z \| _ {\alpha} ^ {D} = 1,
$$

asrequired.

Theorem 6.4. For nonsingular $A \in \mathbb{C}^{n \times n}$ , the matrix condition number $\kappa_{\alpha, \beta}(A)$ satisfies

$$
\kappa_ {\alpha , \beta} (A) = \| A \| _ {\alpha , \beta} \| A ^ {- 1} \| _ {\beta , \alpha}. \tag {6.8}
$$

Proof. In view of the expansion

$$
(A + \Delta A) ^ {- 1} - A ^ {- 1} = - A ^ {- 1} \Delta A A ^ {- 1} + O (\| \Delta A \| ^ {2}),
$$

the result is proved if we can show that

$$
\sup  _ {\| \Delta A \| _ {\alpha , \beta} \leq 1} \| A ^ {- 1} \Delta A A ^ {- 1} \| _ {\beta , \alpha} = \| A ^ {- 1} \| _ {\beta , \alpha} ^ {2}. \tag {6.9}
$$

That (6.9) holds with the equality replaced by “ $\leq$ ” follows from two applications of (6.7). To show the opposite inequality, we have

$$
\left\| A ^ {- 1} \Delta A A ^ {- 1} \right\| _ {\beta , \alpha} = \max  _ {\| y \| _ {\beta} = 1} \left\| A ^ {- 1} \Delta A A ^ {- 1} y \right\| _ {\alpha} \geq \left\| A ^ {- 1} \Delta A x \right\| _ {\alpha} \left\| A ^ {- 1} \right\| _ {\beta , \alpha}, \tag {6.10}
$$

where, for the lower bound, we have chosen $y$ so that $\| A^{-1}y\|_{\alpha} = \| A^{-1}\|_{\beta ,\alpha}$ and where $A^{-1}y = \| A^{-1}\|_{\beta ,\alpha}x$ with $\| x\|_{\alpha} = 1$ . Now, from Lemma 6.3, there

# 6.2 MATRIX NORMS

exists a matrix $\Delta A$ with $\| \Delta A \|_{\alpha, \beta} = 1$ such that $\Delta Ax = y$ . In (6.10) this gives $\| A^{-1} \Delta AA^{-1} \|_{\beta, \alpha} \geq \| A^{-1} \|_{\beta, \alpha}^2$ , as required.

The next result concerns the relative distance to singularity for a matrix $A \in \mathbb{C}^{n \times n}$ :

$$
\operatorname {d i s t} _ {\alpha , \beta} (A) := \operatorname * {m i n} \left\{\frac {\| \varDelta A \| _ {\alpha , \beta}}{\| A \| _ {\alpha , \beta}}: A + \varDelta A \right. \mathrm {s i n g u l a r} \left. \right\}.
$$

It states that the relative distance to singularity is the reciprocal of the condition number.

Theorem 6.5 (Gastinel, Kahan). For nonsingular $A \in \mathbb{C}^{n \times n}$ , we have

$$
\mathrm {d i s t} _ {\alpha , \beta} (A) = \left(\| A \| _ {\alpha , \beta} \| A ^ {- 1} \| _ {\beta , \alpha}\right) ^ {- 1} = \kappa_ {\alpha , \beta} (A) ^ {- 1}.
$$

Proof. If $A + \Delta A$ is singular, then there exists $x \neq 0$ such that $(A + \Delta A)x = 0$ . Hence

$$
\left\| x \right\| _ {\alpha} = \left\| A ^ {- 1} \varDelta A x \right\| _ {\alpha} \leq \left\| A ^ {- 1} \right\| _ {\beta , \alpha} \left\| \varDelta A x \right\| _ {\beta} \leq \left\| A ^ {- 1} \right\| _ {\beta , \alpha} \left\| \varDelta A \right\| _ {\alpha , \beta} \left\| x \right\| _ {\alpha},
$$

giving

$$
\frac {\left\| \varDelta A \right\| _ {\alpha , \beta}}{\left\| A \right\| _ {\alpha , \beta}} \geq \kappa_ {\alpha , \beta} (A) ^ {- 1}.
$$

To show that a suitable perturbation achieves this lower bound, let $y$ be such that $\| y\|_{\beta} = 1$ and $\| A^{-1}y\|_{\alpha} = \| A^{-1}\|_{\beta ,\alpha}$ , and write $x = A^{-1}y$ . By Lemma 6.3 there exists $B$ with $\| B\|_{\alpha ,\beta} = 1$ such that $Bx / \| x\|_{\alpha} = -y$ . Letting $\varDelta A=B/\|x\|_{\alpha}$ we have $\| \varDelta A\|_{\alpha ,\beta} / \| A\|_{\alpha ,\beta} = \kappa_{\alpha ,\beta}(A)^{-1}$ , and $A + \varDelta A$ is singular because $(A+\varDelta A)A^{-1}y=0$ .

The next lemma collects some results that will be needed in later chapters.

Lemma 6.6. Let $A, B \in \mathbb{R}^{m \times n}$ .

$$
\| A \| _ {F} \leq \| B \| _ {F}, \quad \| A \| _ {2} \leq \sqrt {\operatorname {r a n k} (B)} \| B \| _ {2}, \quad | A | \leq e e ^ {T} | B |.
$$

(a) If $\|a_j\|_2 \leq \|b_j\|_2$ , $j = 1:n$ , then   
(b) If $|A| \leq B$ then $\| A \|_2 \leq \| B \|_2$ .   
(c) If $|A| \leq |B|$ then $\| A \|_2 \leq \sqrt{\operatorname{rank}(B)} \| B \|_2$ .   
(d) $\| A\| _2\leq \| |A|\| _2\leq \sqrt{\mathrm{rank}(A)}\| A\| _2$

Proof. The first inequality of (a) is trivial. For the second, we have, using Table 6.2,

$$
\left\| A \right\| _ {2} \leq \left\| A \right\| _ {F} \leq \left\| B \right\| _ {F} \leq \sqrt {\operatorname {r a n k} (B)} \| B \| _ {2}.
$$

The third inequality follows from

$$
\left| a _ {j} \right| \leq \left\lVert a _ {j} \right\rVert_ {2} e \leq \left\lVert b _ {j} \right\rVert_ {2} e \leq \left\lVert b _ {j} \right\rVert_ {1} e = (e ^ {T} | b _ {j} |) e = (e e ^ {T}) | b _ {j} |.
$$

For (b) we have

$$
\| A \| _ {2} = \max  _ {\| x \| _ {2} = 1} \| A x \| _ {2} \leq \max  _ {\| x \| _ {2} = 1} \| | A | | x | \| _ {2} \leq \max  _ {\| x \| _ {2} = 1} \| B | x | \| _ {2} = \| B \| _ {2}.
$$

Finally, (c) is a special case of (a), and (d) is a special case of (b) and (c).

Note that the second inequality in (a) is sharp: there is equality if $A = B$ has rank 1 and in the case $A = e e^{T}$ , $B = \sqrt{n} I$ , in which $B$ has full rank.

# 6.3. The Matrix $p$ -Norm

The matrix $p$ -norm is the norm subordinate to the Hölder $p$ -norm:

$$
\| A \| _ {p} = \max  _ {x \neq 0} \frac {\| A x \| _ {p}}{\| x \| _ {p}}, \quad p \geq 1. \tag {6.11}
$$

Formulae for $\| A\| _p$ are known only for $p = 1,2,\infty$ . For other values of $p$ , how to estimate or compute $\| A\| _p$ is an interesting problem, the study of which, as well as being interesting in its own right, yields insight into the properties of the 1, 2, and $\infty$ norms.

By taking $x = e_j$ in (6.11), using (6.4), and using (6.21) below, we can derive the bounds, for $A \in \mathbb{C}^{m \times n}$ ,

$$
\max  _ {j} \| A (:, j) \| _ {p} \leq \| A \| _ {p} \leq n ^ {1 - 1 / p} \max  _ {j} \| A (:, j) \| _ {p}, \tag {6.12}
$$

$$
\max  _ {i} \| A (i,:) \| _ {p / (p - 1)} \leq \| A \| _ {p} \leq m ^ {1 / p} \max  _ {i} \| A (i,:) \| _ {p / (p - 1)}. \tag {6.13}
$$

Matrix norms can be compared using the following elegant result of Schneider and Strang [1018, 1962] (see also [636, 1985, Thm. 5.6.18]): if $\| \cdot \|_{\alpha}$ and $\| \cdot \|_{\beta}$ denote two vector norms and the corresponding subordinate matrix norms, then for $A \in \mathbb{C}^{m \times n}$

$$
\max  _ {A \neq 0} \frac {\| A \| _ {\alpha}}{\| A \| _ {\beta}} = \left(\max  _ {0 \neq x \in \mathbb {C} ^ {m}} \frac {\| x \| _ {\alpha}}{\| x \| _ {\beta}}\right) \left(\max  _ {0 \neq x \in \mathbb {C} ^ {n}} \frac {\| x \| _ {\beta}}{\| x \| _ {\alpha}}\right). \tag {6.14}
$$

From (6.4) and (6.14), we have, when $m = n$

$$
\max  _ {A \neq 0} \frac {\| A \| _ {p _ {1}}}{\| A \| _ {p _ {2}}} = n \left(\frac {1}{\min  \left(p _ {1} , p _ {2}\right)} - \frac {1}{\max  \left(p _ {1} , p _ {2}\right)}\right). \tag {6.15}
$$

Note that, unlike for vectors, $p_1 < p_2$ does not imply $\| A \|_{p_1} \geq \| A \|_{p_2}$ . The result (6.15) implies, for example, that for all $p \geq 1$

$$
\frac {\| A \| _ {1}}{n ^ {1 - 1 / p}} \leq \| A \| _ {p} \leq n ^ {1 - 1 / p} \| A \| _ {1}, \tag {6.16}
$$

$$
\frac {\left\| A \right\| _ {2}}{n ^ {| 1 / p - 1 / 2 |}} \leq \left\| A \right\| _ {p} \leq n ^ {| 1 / p - 1 / 2 |} \left\| A \right\| _ {2}. \tag {6.17}
$$

Upper bounds for $\| A\| _p$ that do not involve $m$ or $n$ can be obtained from the interesting property that $\log \| A\| _p$ is a convex function of $1 / p$ for $p\geq 1$

![](images/1ab05684252172f29495cd357885063e042463e27ec8e24d460b32c1eb248c95.jpg)

![](images/991edfc93738f61805cf568354c8d197bdd0fb89a98fb003863482216e5db051.jpg)

![](images/9101dc5928e80e6a81fca7c7d0879f663911e2474fd964bcb66a052d62d5c1bf.jpg)

![](images/a949e92f91466a91b8ddf9407c035b216d621a9a162d94f100b545d09d0179b7.jpg)  
Figure 6.1. Plots of $p$ versus $\| A \|_p$ , for $1 \leq p \leq 15$ . Fourth plot shows $1/p$ versus $\log \| A \|_p$ for the matrices in the first three plots.

(see Figure 6.1), which is a consequence of the Riesz-Thorin theorem [548, 1952, pp. 214, 219], [489, 1991]. The convexity implies that if $f(\alpha) = \| A\|_{1 / \alpha}$ , then for $0\leq \alpha ,\beta \leq 1$

$$
\log f \left(\theta \alpha + (1 - \theta) \beta\right) \leq \theta \log f (\alpha) + (1 - \theta) \log f (\beta), \quad 0 \leq \theta \leq 1.
$$

Writing $p_1 = 1 / \alpha$ and $p_2 = 1 / \beta$ , this inequality can be expressed as

$$
\left\| A \right\| _ {p} \leq \left\| A \right\| _ {p _ {1}} ^ {\theta} \left\| A \right\| _ {p _ {2}} ^ {1 - \theta}, \quad p = \frac {p _ {1} p _ {2}}{(1 - \theta) p _ {1} + \theta p _ {2}}, \tag {6.18}
$$

$$
1 \leq p _ {1}, p _ {2} \leq \infty , \quad 0 \leq \theta \leq 1.
$$

Two interesting special cases are

$$
\left\| A \right\| _ {p} \leq \left\| A \right\| _ {1} ^ {1 / p} \left\| A \right\| _ {\infty} ^ {1 - 1 / p} \tag {6.19}
$$

and

$$
\left\| A \right\| _ {p} \leq \left\| A \right\| _ {1} ^ {2 / p - 1} \left\| A \right\| _ {2} ^ {2 - 2 / p}, \quad 1 \leq p \leq 2. \tag {6.20}
$$

Note that (6.19) includes the well-known inequality $\| A \|_2 \leq \sqrt{\|A\|_1 \|A\|_\infty}$ .

Two further results that are familiar for $p = 1,2,\infty$ are

$$
\left\| A ^ {*} \right\| _ {p} = \left\| A \right\| _ {q}, \quad \frac {1}{p} + \frac {1}{q} = 1 \tag {6.21}
$$

(see also Problem 6.3), and

$$
\left\| \left[ \begin{array}{l l} 0 & A \\ A ^ {*} & 0 \end{array} \right] \right\| _ {p} = \operatorname * {m a x} (\| A \| _ {p}, \| A \| _ {q}).
$$

The bounds (6.16) and (6.17) imply that given the ability to compute $\| A\| _1$ , $\| A\| _2$ , and $\| A\|_{\infty}$ we can estimate $\| A\| _p$ correct to within a factor $n^{1 / 4}$ . These a priori estimates are at their best when $p$ is close to 1, 2, or $\infty$ , but in general they will not provide even one correct significant digit. The bound in (6.18) can be much smaller than the other upper bounds given above, but how tight it is depends on how nearly $\log \| A\|_p$ is linear in $p$ . Numerical methods are needed to obtain better estimates; these are developed in Chapter 15.

# 6.4. Singular Value Decomposition

Any matrix $A \in \mathbb{C}^{m \times n}$ has a singular value decomposition (SVD)

$$
A = U \Sigma V ^ {*}, \quad \Sigma = \operatorname {d i a g} \left(\sigma_ {1}, \sigma_ {2}, \dots , \sigma_ {p}\right) \in \mathbb {C} ^ {m \times n}, \quad p = \min  (m, n),
$$

where $\sigma_1 \geq \sigma_2 \geq \dots \geq \sigma_p \geq 0$ and $U \in \mathbb{C}^{m \times m}$ , $V \in \mathbb{C}^{n \times n}$ are both unitary. The $\sigma_i$ are the singular values of $A$ and the columns of $U$ and $V$ are the left and right singular vectors of $A$ , respectively.

The rank of $A$ is equal to the number of nonzero singular values. If $A$ is real, $U$ and $V$ can be taken to be real.

For any unitarily invariant norm, $\| A\| = \| \Sigma \|$ , and hence

$$
\left\| A \right\| _ {2} = \sigma_ {1} (A), \quad \left\| A \right\| _ {F} = \left(\sum_ {i = 1} ^ {n} \sigma_ {i} ^ {2}\right) ^ {1 / 2}. \tag {6.22}
$$

The SVD is an extremely useful tool in numerical linear algebra. Aside from exploiting these norm relations, our main use of the SVD in this book is in Chapter 20 on the least squares problem.

# 6.5. Notes and References

The matrix condition number appears to have been first introduced explicitly by Turing [1166, 1948], who defined, for example, the $N$ -condition number of $A \in \mathbb{R}^{n \times n}$ as $n^{-1} N(A) N(A^{-1})$ , where $N(\cdot)$ is Turing's notation for the Frobenius norm. Todd [1140, 1968] gives a short survey of the matrix condition number with many references.

Theorem 6.2 was originally proved by Bauer, Stoer, and Witzgall, in a paper that contains many interesting results on monotonic norms [95, 1961].

Tables of constants in inequalities between different norms have been given by various authors; see, for example, Stone [1088, 1962] and Zielke [1282, 1988].

Our development of the mixed subordinate norm $\| \cdot \|_{\alpha, \beta}$ is based on that of D. J. Higham [573, 1995].

Theorem 6.5 is proved by Kahan [687, 1966, pp. 775-776], who attributes it to Gastinel but gives no reference. For the 2-norm, this result goes back to a paper by Eckart and Young [370, 1936]. Theorem 6.5 is an instance of a relationship that holds for many problems: the condition number is the reciprocal of the distance to the nearest singular problem (one with an infinite condition number). This relationship applies to matrix inversion, eigenvalue and eigenvector computation,

polynomial zero-finding, and pole assignment in linear control systems. For an in-depth study see Demmel [309, 1987].

Schneider and Weinberger [1019, 1998] study classes of matrices for which (6.14) is attained in the case of Hölder $p$ -norms.

Direct proofs of inequality (6.19) can be found in Kato [716, 1976, p. 29] and Todd [1143, 1977, pp. 25-26]. The inequality does not seem to be well known.

For historical comments on the development of norms in numerical analysis, see Householder [644, 1964, Chap. 2] and Stewart and Sun [1083, 1990, Chap. 2].

For more details on the SVD see Golub and Van Loan [509, 1996, §2.5.3], Stewart and Sun [1083, 1990, pp. 30-34], and Horn and Johnson [636, 1985, §7.3], [637, 1991, §3.1]. The history of the SVD is described by Stewart [1074, 1993] and Horn and Johnson [637, 1991, §3.0].

# Problems

Problems worthy

of attack

prove their worth

by hitting back.

PIET HEIN, Grooks (1966)

6.1. Prove the inequalities given in Tables 6.1 and 6.2. Show that each inequality in Table 6.2 (except the one for $\alpha_{S,2}$ ) is attainable for a matrix of the form $A = xy^T$ , where $x,y \in \{e,e_j\}$ , where $e = [1,1,\ldots,1]^T$ . Show that equality in $\| A \|_S \leq \alpha_{S,2} \| A \|_2$ is attained for square real matrices $A$ iff $A$ is a scalar multiple of a Hadamard matrix (see §9.4 for the definition of a Hadamard matrix), and for square complex matrices if $a_{rs} = \exp(2\pi i(r - 1)(s - 1)/n)$ (this is a Vandermonde matrix based on the roots of unity).   
6.2. Let $x, y \in \mathbb{C}^{n \times n}$ . Show that, for any subordinate matrix norm, $\| xy^* \| = \| x \| \| y \|_D$ .   
6.3. Show that a subordinate matrix norm $\| \cdot \|$ on $\mathbb{C}^{n\times n}$ satisfies

$$
\| A \| = \max  _ {x, y \neq 0} \frac {\operatorname {R e} y ^ {*} A x}{\| y \| _ {D} \| x \|}.
$$

Deduce that $\| A^{*}\| = \| A\|_{D}$ , where the latter norm is the norm subordinate to the vector norm $\| \cdot \| _D$ .

From ancient times until now the

study of magic squares has flourished as a kind of cult,

often with occult trappings, whose initiates range from

such eminent mathematicians as Arthur Cayley and Oswald Veblen

to laymen such as Benjamin Franklin.

— MARTIN GARDNER, More Mathematical Puzzles and Diversions (1961)

6.4. Let $M_n \in \mathbb{R}^{n \times n}$ denote a magic square matrix, that is, an $n \times n$ matrix containing the integers from 1 to $n^2$ arranged in such a way that the row and column sums are all the same. Let $\mu_n$ denote the magic sum of $M_n$ (thus, $\mu_n = n(n^2 + 1)/2$ ). Show that $\| M_n \|_p = \mu_n$ for all $1 \leq p \leq \infty$ . (This result is a

special case of an apparently little-known result of Stoer and Witzgall, which states that the norm of a doubly stochastic matrix is 1 for any norm subordinate to a permutation-invariant absolute vector norm [1087, 1962].)

6.5. Show that $\| ABC\| _F\leq \| A\| _2\| B\| _F\| C\| _2$ for any $A,B,$ and $C$ such that the product is defined. (This result remains true when the Frobenius norm is replaced by any unitarily invariant norm [637, 1991, p. 211].)

6.6. Show that for any nonsingular $A \in \mathbb{C}^{n \times n}$ ,

$$
\kappa_ {\alpha , \beta} (A) = \frac {\max  _ {x \neq 0} \frac {\| A x \| _ {\beta}}{\| x \| _ {\alpha}}}{\min  _ {x \neq 0} \frac {\| A x \| _ {\beta}}{\| x \| _ {\alpha}}}.
$$

6.7. Show that for any $A \in \mathbb{C}^{n \times n}$ and any consistent matrix norm, $\rho(A) \leq \|A\|$ , where $\rho$ is the spectral radius.

6.8. Show that for any $A \in \mathbb{C}^{n \times n}$ and $\delta > 0$ there is a consistent norm $\|\cdot\|$ (which depends on $A$ and $\delta$ ) such that $\|A\| \leq \rho(A) + \delta$ , where $\rho$ is the spectral radius. Hence show that if $\rho(A) < 1$ then there is a consistent norm $\|\cdot\|$ such that $\|A\| < 1$ .

6.9. Let $A \in \mathbb{C}^{m \times n}$ . Use (6.22) to obtain a bound of the form $c_1 \| A \|_2 \leq \| A \|_F \leq c_2 \| A \|_2$ , where $c_1$ and $c_2$ are constants that depend on $n$ . When is there equality in the upper bound? When is there equality in the lower bound?

6.10. Show that

$$
\left\| \left[ \begin{array}{c c} I & F \\ 0 & I \end{array} \right] \right\| _ {2} = \sqrt {\frac {2 + \| F \| _ {2} ^ {2} + \| F \| _ {2} \sqrt {4 + \| F \| _ {2} ^ {2}}}{2}}.
$$

Deduce that when $\| F\| _2 = 1$ , the norm is $(1 + \sqrt{5}) / 2$ , the golden ratio.

6.11. Let $A \in \mathbb{C}^{n \times n}$ . Prove that (a) $\| A \|_{1, \beta} = \max_j \| A(:, j) \|_{\beta}$ , and (b) $\| A \|_{\alpha, \infty} = \max_i \| A(i,:)^* \|_{\alpha}^D$ . What is $\| A \|_{1, \infty}$ ?

6.12. (Tao [1128, 1984]) Show that if $A$ is Hermitian positive definite then

$$
\left\| A \right\| _ {\infty , 1} = \max  \left\{x ^ {*} A x: \| x \| _ {\infty} = 1 \right\}.
$$

(Rohn [992, 1995] shows that the problem of computing $\| A\|_{\infty ,1}$ is NP-hard.)

6.13. Prove that if $H \in \mathbb{R}^{n \times n}$ is a Hadamard matrix then

$$
\left\| H \right\| _ {p} = \max  \left\{n ^ {1 / p}, n ^ {1 - 1 / p} \right\}.
$$

(See §9.4 for the definition of a Hadamard matrix.)

6.14. Show that if $A \in \mathbb{R}^{m \times n}$ has at most $\mu$ nonzeros per row then

$$
\max  _ {j} \| A (:, j) \| _ {p} \leq \| A \| _ {p} \leq \mu^ {1 - 1 / p} \max  _ {j} \| A (:, j) \| _ {p}, \tag {6.23}
$$

while if $A$ has at most $\mu$ nonzeros per column then

$$
\max  _ {i} \| A (i,:) \| _ {q} \leq \| A \| _ {p} \leq \mu^ {1 / p} \max  _ {i} \| A (i,:) \| _ {q}, \tag {6.24}
$$

where $p^{-1} + q^{-1} = 1$ . (These inequalities generalize (6.12) and (6.13).)

6.15. Show that if $A \in \mathbb{C}^{n \times n}$ then for any $p$ -norm $(1 \leq p \leq \infty)$ ,

$$
\| A \| _ {p} \leq \| | A | \| _ {p} \leq n ^ {\min  (1 / p, 1 - 1 / p)} \| A \| _ {p} \leq \sqrt {n} \| A \| _ {p}.
$$

6.16. Define the function $\nu : \mathbb{C}^n \to \mathbb{R}$ by

$$
\nu (x) = \sum_ {i = 1} ^ {n} \left(| \operatorname {R e} x _ {i} | + | \operatorname {I m} x _ {i} |\right).
$$

Is $\nu$ a vector norm on $\mathbb{C}^n$ ? Derive an explicit expression for

$$
\nu (A) = \max  _ {\nu (x) = 1} \nu (A x), \quad A \in \mathbb {C} ^ {n \times n}.
$$

(For the relevance of $\nu$ see §27.8.)
