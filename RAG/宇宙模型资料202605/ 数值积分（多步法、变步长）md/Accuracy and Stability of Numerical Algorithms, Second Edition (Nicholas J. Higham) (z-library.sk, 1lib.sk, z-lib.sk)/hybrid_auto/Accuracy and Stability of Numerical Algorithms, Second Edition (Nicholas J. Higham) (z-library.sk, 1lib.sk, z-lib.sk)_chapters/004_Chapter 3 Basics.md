# Chapter 3 Basics

A method of inverting the problem of round-off error is proposed which we plan to employ in other contexts and which suggests that it may be unwise to separate the estimation of round-off error from that due to observation and truncation.

— WALLACE J. GIVENS, Numerical Computation of the Characteristic Values of a Real Symmetric Matrix (1954)

The enjoyment of one's tools is an essential ingredient of successful work.

— DONALD E. KNUTH, The Art of Computer Programming, Volume 2, Seminumerical Algorithms (1998)

The subject of propagation of rounding error, while of undisputed importance in numerical analysis, is notorious for the difficulties which it presents when it is to be taught in the classroom in such a manner that the student is neither insulted by lack of mathematical content nor bored by lack of transparence and clarity.

— PETER HENRICI, A Model for the Propagation of Rounding Error in Floating Arithmetic (1980)

The two main classes of rounding error analysis are not, as my audience might imagine, 'backwards' and 'forwards', but rather 'one's own' and 'other people's'. One's own is, of course, a model of lucidity; that of others serves only to obscure the essential simplicity of the matter in hand.

— J. H. WILKINSON, The State of the Art in Error Analysis (1985)

Having defined a model for floating point arithmetic in the last chapter, we now apply the model to some basic matrix computations, beginning with inner products. This first application is simple enough to permit a short analysis, yet rich enough to illustrate the ideas of forward and backward error. It also raises the thorny question of what is the best notation to use in an error analysis. We introduce the “ $\gamma_{n}$ ” notation, which we use widely, though not exclusively, in the book. The inner product analysis leads immediately to results for matrix-vector and matrix-matrix multiplication.

Also in this chapter we determine a model for rounding errors in complex arithmetic, derive some miscellaneous results of use in later chapters, and give a high-level overview of forward error analysis and backward error analysis.

# 3.1. Inner and Outer Products

Consider the inner product $s_n = x^T y$ , where $x, y \in \mathbb{R}^n$ . Since the order of evaluation of $s_n = x_1y_1 + \dots + x_ny_n$ affects the analysis (but not the final error bounds), we will assume that the evaluation is from left to right. (The effect of particular orderings is discussed in detail in Chapter 4, which considers the special case of summation.) In the following analysis, and throughout the book, a hat denotes a computed quantity.

Let $s_i = x_1y_1 + \dots + x_iy_i$ denote the $i$ th partial sum. Using the standard model (2.4), we have

$$
\begin{array}{l} \widehat {s} _ {1} = f l \left(x _ {1} y _ {1}\right) = x _ {1} y _ {1} \left(1 + \delta_ {1}\right), \\ \widehat {s} _ {2} = f l \left(\widehat {s} _ {1} + x _ {2} y _ {2}\right) = \left(\widehat {s} _ {1} + x _ {2} y _ {2} (1 + \delta_ {2})\right) (1 + \delta_ {3}) \\ = \left(x _ {1} y _ {1} (1 + \delta_ {1}) + x _ {2} y _ {2} (1 + \delta_ {2})\right) (1 + \delta_ {3}) \\ = x _ {1} y _ {1} \left(1 + \delta_ {1}\right) \left(1 + \delta_ {3}\right) + x _ {2} y _ {2} \left(1 + \delta_ {2}\right) \left(1 + \delta_ {3}\right), \tag {3.1} \\ \end{array}
$$

where $|\delta_i| \leq u, i = 1:3$ . For our purposes it is not necessary to distinguish between the different $\delta_i$ terms, so to simplify the expressions let us drop the subscripts on the $\delta_i$ and write $1 + \delta_i \equiv 1 \pm \delta$ . Then

$$
\begin{array}{l} \widehat {s} _ {3} = f l \left(\widehat {s} _ {2} + x _ {3} y _ {3}\right) = \left(\widehat {s} _ {2} + x _ {3} y _ {3} (1 \pm \delta)\right) (1 \pm \delta) \\ = \left(x _ {1} y _ {1} (1 \pm \delta) ^ {2} + x _ {2} y _ {2} (1 \pm \delta) ^ {2} + x _ {3} y _ {3} (1 \pm \delta)\right) (1 \pm \delta) \\ = x _ {1} y _ {1} (1 \pm \delta) ^ {3} + x _ {2} y _ {2} (1 \pm \delta) ^ {3} + x _ {3} y _ {3} (1 \pm \delta) ^ {2}. \\ \end{array}
$$

The pattern is clear. Overall, we have

$$
\widehat {s} _ {n} = x _ {1} y _ {1} (1 \pm \delta) ^ {n} + x _ {2} y _ {2} (1 \pm \delta) ^ {n} + x _ {3} y _ {3} (1 \pm \delta) ^ {n - 1} + \dots + x _ {n} y _ {n} (1 \pm \delta) ^ {2}. \tag {3.2}
$$

There are various ways to simplify this expression. A particularly elegant way is to use the following result.

Lemma 3.1. If $|\delta_i| \leq u$ and $\rho_i = \pm 1$ for $i = 1:n$ , and $nu < 1$ , then

$$
\prod_ {i = 1} ^ {n} (1 + \delta_ {i}) ^ {\rho_ {i}} = 1 + \theta_ {n},
$$

where

$$
\left| \theta_ {n} \right| \leq \frac {n u}{1 - n u} =: \gamma_ {n}.
$$

# Proof. See Problem 3.1. $\square$

The $\theta_{n}$ and $\gamma_{n}$ notation will be used throughout this book. Whenever we write $\gamma_{n}$ there is an implicit assumption that $nu < 1$ , which is true in virtually any circumstance that might arise with IEEE single or double precision arithmetic.

Applying the lemma to (3.2) we obtain

$$
\widehat {s} _ {n} = x _ {1} y _ {1} \left(1 + \theta_ {n}\right) + x _ {2} y _ {2} \left(1 + \theta_ {n} ^ {\prime}\right) + x _ {3} y _ {3} \left(1 + \theta_ {n - 1}\right) + \dots + x _ {n} y _ {n} \left(1 + \theta_ {2}\right). \tag {3.3}
$$

This is a backward error result and may be interpreted as follows: the computed inner product is the exact one for a perturbed set of data $x_{1},\ldots ,x_{n}$ , $y_{1}(1 + \theta_{n}),y_{2}(1 + \theta_{n}^{\prime}),\ldots ,y_{n}(1 + \theta_{2})$ (alternatively, we could perturb the $x_{i}$ and leave the $y_{i}$ alone). Each relative perturbation is certainly bounded by $\gamma_{n} = nu / (1 - nu)$ , so the perturbations are tiny.

The result (3.3) applies to one particular order of evaluation. It is easy to see that for any order of evaluation we have, using vector notation,

$$
f l \left(x ^ {T} y\right) = (x + \Delta x) ^ {T} y = x ^ {T} (y + \Delta y), \quad | \Delta x | \leq \gamma_ {n} | x |, \quad | \Delta y | \leq \gamma_ {n} | y |, \tag {3.4}
$$

where $|x|$ denotes the vector with elements $|x_i|$ and inequalities between vectors (and, later, matrices) hold componentwise.

A forward error bound follows immediately from (3.4):

$$
\left| x ^ {T} y - f l \left(x ^ {T} y\right) \right| \leq \gamma_ {n} \sum_ {i = 1} ^ {n} \left| x _ {i} y _ {i} \right| = \gamma_ {n} \left| x \right| ^ {T} | y |. \tag {3.5}
$$

If $y = x$ , so that we are forming a sum of squares $x^T x$ , this result shows that high relative accuracy is obtained. However, in general, high relative accuracy is not guaranteed if $|x^T y| \ll |x|^T |y|$ .

It is easy to see that precisely the same results (3.3)-(3.5) hold when we use the no-guard-digit rounding error model (2.6). For example, expression (3.1) becomes $\widehat{s}_2 = x_1y_1(1 + \delta_1)(1 + \delta_3) + x_2y_2(1 + \delta_2)(1 + \delta_4)$ , where $\delta_4$ has replaced a second occurrence of $\delta_3$ , but this has no effect on the error bounds.

It is worth emphasizing that the constants in the bounds above can be reduced by focusing on particular implementations of an inner product. For example, if $n = 2m$ and we compute

$$
\begin{array}{l} s _ {1} = x (1: m) ^ {T} y (1: m) \\ s _ {2} = x (m + 1: n) ^ {T} y (m + 1: n) \\ s _ {n} = s _ {1} + s _ {2} \\ \end{array}
$$

then $|s_n - \widehat{s}_n| \leq \gamma_{n/2+1}|x^T||y|$ . By accumulating the inner product in two pieces we have almost halved the error bound. This idea can be generalized by breaking the inner product into $k$ pieces, with each mini inner product of length $n/k$ being evaluated separately and the results summed. The error bound is now $\gamma_{n/k+k-1}|x^T||y|$ , which achieves its minimal value of $\gamma_{2\sqrt{n}-1}|x^T||y|$ for $k = \sqrt{n}$ (or, rather, we should take $k$ to be the nearest integer to $\sqrt{n}$ ). But it is possible to do even better by using pairwise summation of the products $x_i y_i$ (this method is described in §4.1). With pairwise summation, the error bound becomes

$$
| s _ {n} - \widehat {s} _ {n} | \leq \gamma_ {\lceil \log_ {2} n \rceil + 1} | x ^ {T} | | y |.
$$

Since many of the error analyses in this book are built upon the error analysis of inner products, it follows that the constants in these higher-level bounds can also be reduced by using one of these nonstandard inner product implementations. The main significance of this observation is that we should not attach too much significance to the precise values of the constants in error bounds.

Inner products are amenable to being calculated in extended precision. If the working precision involves a $t$ -digit significand then the product of two floating point numbers has a significand of $2t - 1$ or $2t$ digits and so can be represented exactly with a $2t$ -digit significand. Some computers always form the $2t$ -digit product before rounding to $t$ digits, thus allowing an inner product to be accumulated at $2t$ -digit precision at little or no extra cost, prior to a final rounding.

The extended precision computation can be expressed as $fl(f l_{e}(x^{T}y))$ , where $f l_{e}$ denotes computations with unit roundoff $u_{e}$ ( $u_{e} < u$ ). Defining $\widehat{s}_n = f l_e(x^T y)$ , the analysis above holds with $u$ replaced by $u_{e}$ in (3.3) (and with the subscripts on the $\theta_{i}$ reduced by 1 if the multiplications are done exactly). For the final rounding we have

$$
f l \left(f l _ {e} \left(x ^ {T} y\right)\right) = \widehat {s} _ {n} (1 + \delta), \quad | \delta | \leq u,
$$

and so, overall,

$$
| x ^ {T} y - f l (f l _ {e} (x ^ {T} y)) | \leq u | x ^ {T} y | + \frac {n u _ {e}}{1 - n u _ {e}} (1 + u) | x | ^ {T} | y |.
$$

Hence, as long as $nu_{e}|x|^{T}|y| \leq u|x^{T}y|$ , the computed inner product is about as good as the rounded exact inner product. The effect of using extended precision inner products in an algorithm is typically to enable a factor $n$ to be removed from the overall error bound.

Because extended precision inner product calculations are machine dependent it has always been difficult to write portable programs that use them, but the widespread adoption of IEEE arithmetic and the development of the Extended and Mixed Precision BLAS (see §27.10) make portability much easier to achieve now. Most modern numerical codes (for example, those in EISPACK, LINPACK, and LAPACK) do not use extended precision inner products. One process in which these more accurate products are needed is the traditional formulation of iterative refinement, in which the aim is to improve the accuracy of the computed solution to a linear system (see Chapter 12).

We have seen that computation of an inner product is a backward stable process. What can be said for an outer product $A = xy^T$ , where $x, y, \in \mathbb{R}^n$ ? The

analysis is easy. We have $\widehat{a}_{ij} = x_iy_i(1 + \delta_{ij})$ , $|\delta_{ij}| \leq u$ , so

$$
\widehat {A} = x y ^ {T} + \Delta , \quad | \Delta | \leq u | x y ^ {T} |. \tag {3.6}
$$

This is a satisfying result, but the computation is not backward stable. In fact, $\widehat{A} = (x + \Delta x)(y + \Delta y)^T$ does not hold for any $\Delta x$ and $\Delta y$ (let alone a small $\Delta x$ and $\Delta y$ ) because $\widehat{A}$ is not in general a rank-1 matrix.

This distinction between inner and outer products illustrates a general principle: a numerical process is more likely to be backward stable when the number of outputs is small compared with the number of inputs, so that there is an abundance of data onto which to "throw the backward error". An inner product has the minimum number of outputs for its $2n$ scalar inputs, and an outer product has the maximum number (among standard linear algebra operations).

# 3.2. The Purpose of Rounding Error Analysis

Before embarking on further error analyses, it is worthwhile to consider what a rounding error analysis is designed to achieve. The purpose is to show the existence of an a priori bound for some appropriate measure of the effects of rounding errors on an algorithm. Whether a bound exists is the most important question. Ideally, the bound is small for all choices of problem data. If not, it should reveal features of the algorithm that characterize any potential instability and thereby suggest how the instability can be cured or avoided. For some unstable algorithms, however, there is no useful error bound. (For example, no bound is known for the loss of orthogonality due to rounding error in the classical Gram-Schmidt method; see §19.8.)

The constant terms in an error bound (those depending only on the problem dimensions) are the least important parts of it. As discussed in §2.8, the constants usually cause the bound to overestimate the actual error by orders of magnitude. It is not worth spending much effort to minimize constants because the achievable improvements are usually insignificant.

It is worth spending effort, though, to put error bounds in a concise, easily interpreted form. Part of the secret is in the choice of notation, which we discuss in §3.4, including the question of what symbols to choose for variables (see the discussion in Higham [611, 1998, §3.5]).

If sharp error estimates or bounds are desired they should be computed a posteriori, so that the actual rounding errors that occur can be taken into account. One approach is to use running error analysis, described in the next section. Other possibilities are to compute the backward error explicitly, as can be done for linear equation and least squares problems (see §§7.1, 7.2, 20.7, and 21.2), or to apply iterative refinement to obtain a correction that approximates the forward error (see Chapter 12).

# 3.3. Running Error Analysis

The forward error bound (3.5) is an a priori bound that does not depend on the actual rounding errors committed. We can derive a sharper, a posteriori bound by reworking the analysis. The inner product evaluation may be expressed as

$$
s _ {0} = 0
$$

$$
f o r i = 1: n
$$

$$
s _ {i} = s _ {i - 1} + x _ {i} y _ {i}
$$

end

Write the computed partial sums as $\widehat{s}_i \eqqcolon s_i + e_i$ and let $\widehat{z}_i \coloneqq fl(x_i y_i)$ . We have, using (2.5),

$$
\widehat {z} _ {i} = \frac {x _ {i} y _ {i}}{1 + \delta_ {i}}, \quad | \delta_ {i} | \leq u \quad \Rightarrow \quad \widehat {z} _ {i} = x _ {i} y _ {i} - \delta_ {i} \widehat {z} _ {i}.
$$

Similarly, $(1 + \epsilon_{i})\widehat{s}_{i} = \widehat{s}_{i - 1} + \widehat{z}_{i}$ , where $|\epsilon_i| \leq u$ , or

$$
s _ {i} + e _ {i} + \epsilon_ {i} \widehat {s} _ {i} = s _ {i - 1} + e _ {i - 1} + x _ {i} y _ {i} - \delta_ {i} \widehat {z} _ {i}.
$$

Hence $e_i = e_{i - 1} - \epsilon_i\widehat{s}_i - \delta_i\widehat{z}_i$ , which gives

$$
\left| e _ {i} \right| \leq \left| e _ {i - 1} \right| + u \left| \widehat {s} _ {i} \right| + u \left| \widehat {z} _ {i} \right|.
$$

Since $e_0 = 0$ , we have $|e_n| \leq u\mu_n$ , where

$$
\mu_ {i} = \mu_ {i - 1} + | \widehat {s} _ {i} | + | \widehat {z} _ {i} |, \quad \mu_ {0} = 0.
$$

Algorithm 3.2. Given $x, y \in \mathbb{R}^n$ this algorithm computes $s = f l(x^T y)$ and a number $\mu$ such that $|s - x^T y| \leq \mu$ .

$$
s = 0
$$

$$
\mu = 0
$$

$$
f o r i = 1: n
$$

$$
z = x _ {i} y _ {i}
$$

$$
s = s + z
$$

$$
\mu = \mu + | s | + | z |
$$

end

$$
\mu = \mu * u
$$

This type of computation, where an error bound is computed concurrently with the solution, is called running error analysis. The underlying idea is simple: we use the modified form (2.5) of the standard rounding error model to write

$$
\left| x \operatorname {o p} y - f l (x \operatorname {o p} y) \right| \leq u | f l (x \operatorname {o p} y) |,
$$

which gives a bound for the error in $x \mathrm{op} y$ that is easily computed, since $fl(x \mathrm{op} y)$ is stored on the computer. Key features of a running error analysis are that few inequalities are involved in the derivation of the bound and that the actual computed intermediate quantities are used, enabling advantage to be taken of cancellation and zero operands. A running error bound is, therefore, usually smaller than an a priori one.

There are, of course, rounding errors in the computation of the running error bound, but their effect is negligible for $nu \ll 1$ (we do not need many correct significant digits in an error bound).

Running error analysis is a somewhat neglected practice nowadays, but it was widely used by Wilkinson in the early years of computing. It is applicable to almost any numerical algorithm. Wilkinson explains [1245, 1986]:

When doing running error analysis on the ACE at no time did I write down these expressions. I merely took an existing program (without any error analysis) and modified it as follows. As each arithmetic operation was performed I added the absolute value of the computed result (or of the dividend) into the accumulating error bound.

For more on the derivation of running error bounds see Wilkinson [1244, 1985] or [1245, 1986]. A running error analysis for Horner's method is given in §5.1.

# 3.4. Notation for Error Analysis

Another way to write (3.5) is

$$
\left| x ^ {T} y - f l \left(x ^ {T} y\right) \right| \leq n u \left| x \right| ^ {T} | y | + O \left(u ^ {2}\right). \tag {3.7}
$$

In general, which form of bound is preferable depends on the context. The use of first-order bounds such as (3.7) can simplify the algebra in an analysis. But there can be some doubt as to the size of the constant term concealed by the big-oh notation. Furthermore, in vector inequalities an $O(u^2)$ term hides the structure of the vector it is bounding and so can make interpretation of the result difficult; for example, the inequality $|x - y| \leq nu|x| + O(u^2)$ does not imply that $y$ approximates every element of $x$ with the same relative error (indeed the relative error could be infinite when $x_i = 0$ , as far as we can tell from the bound).

In more complicated analyses based on Lemma 3.1 it is necessary to manipulate the $1 + \theta_{k}$ and $\gamma_{k}$ terms. The next lemma provides the necessary rules.

Lemma 3.3. For any positive integer $k$ let $\theta_{k}$ denote a quantity bounded according to $|\theta_{k}| \leq \gamma_{k} = ku / (1 - ku)$ . The following relations hold:

$$
(1 + \theta_ {k}) (1 + \theta_ {j}) = 1 + \theta_ {k + j},
$$

$$
\begin{array}{l} \frac {1 + \theta_ {k}}{1 + \theta_ {j}} = \left\{ \begin{array}{l l} 1 + \theta_ {k + j}, & j \leq k, \\ 1 + \theta_ {k + 2 j}, & j > k, \end{array} \right. \\ \gamma_ {k} \gamma_ {j} \leq \gamma_ {\min  (k, j)} \quad f o r \max  (j, k) u \leq 1 / 2, \\ i \gamma_ {k} \leq \gamma_ {i k}, \\ \end{array}
$$

$$
\begin{array}{l} \gamma_ {k} + u \leq \gamma_ {k + 1}, \\ \gamma_ {k} + \gamma_ {j} + \gamma_ {k} \gamma_ {j} \leq \gamma_ {k + j}. \\ \end{array}
$$

Proof. See Problem 3.4. $\square$

Concerning the second rule in Lemma 3.3, we certainly have

$$
\prod_ {i = 1} ^ {k} (1 + \delta_ {i}) ^ {\pm 1} \Big / \prod_ {i = 1} ^ {j} (1 + \delta_ {i}) ^ {\pm 1} = 1 + \theta_ {k + j},
$$

but if we are given only the expression $(1 + \theta_{k}) / (1 + \theta_{j})$ and the bounds for $\theta_{k}$ and $\theta_{j}$ , we cannot do better than to replace it by $\theta_{k + 2j}$ for $j > k$ .

In some error analyses it is not worth the trouble to keep precise track of the constants in the $\gamma_{k}$ terms. The notation

$$
\tilde {\gamma} _ {k} = \frac {c k u}{1 - c k u} \tag {3.8}
$$

is then useful, where $c$ denotes a small integer constant whose exact value is unimportant. Thus we can write, for example, $3\gamma_{n} = \tilde{\gamma}_{n}$ , $m\tilde{\gamma}_{n} = n\tilde{\gamma}_{m} = \tilde{\gamma}_{mn}$ , and $\gamma_{2} + \gamma_{3}(1 + \gamma_{5}) = \tilde{\gamma}_{1}$ .

Another style of writing bounds is made possible by the following lemma.

Lemma 3.4. If $|\delta_i| \leq u$ for $i = 1:n$ and $nu \leq 0.01$ , then

$$
\prod_ {i = 1} ^ {n} (1 + \delta_ {i}) = 1 + \eta_ {n},
$$

where $|\eta_n| \leq 1.01nu$ .

Proof. We have

$$
| \eta_ {n} | = \left| \prod_ {i = 1} ^ {n} (1 + \delta_ {i}) - 1 \right| \leq (1 + u) ^ {n} - 1.
$$

Since $1 + x \leq e^{x}$ for $x \geq 0$ , we have $(1 + u)^{n} < \exp(nu)$ , and so

$$
\begin{array}{l} (1 + u) ^ {n} - 1 <   n u + \frac {(n u) ^ {2}}{2 !} + \frac {(n u) ^ {3}}{3 !} + \dots \\ <   n u \left(1 + \frac {n u}{2} + \left(\frac {n u}{2}\right) ^ {2} + \left(\frac {n u}{2}\right) ^ {3} + \dots\right) \\ = n u \frac {1}{1 - n u / 2} \\ \leq n u \frac {1}{0 . 9 9 5} <   1. 0 1 n u. \quad \square \\ \end{array}
$$

Note that this lemma is slightly stronger than the corresponding bound we can obtain from Lemma 3.1: $|\theta_n| \leq nu / (1 - nu) < nu / 0.99 = 1.0101 \dots nu$ .

Lemma 3.4 enables us to derive, as an alternative to (3.5),

$$
\left| x ^ {T} y - f l \left(x ^ {T} y\right) \right| \leq 1. 0 1 n u \left| x \right| ^ {T} | y |. \tag {3.9}
$$

A convenient device for keeping track of powers of $1 + \delta$ terms was introduced by Stewart [1065, 1973, App. 3]. His relative error counter $< k>$ denotes a product

$$
<   k > = \prod_ {i = 1} ^ {k} (1 + \delta_ {i}) ^ {\rho_ {i}}, \quad \rho_ {i} = \pm 1, \quad | \delta_ {i} | \leq u. \tag {3.10}
$$

The counters can be manipulated using the rules

$$
\begin{array}{l} <   j > <   k > = <   j + k >, \\ \frac {<   j >}{<   k >} = <   j + k >. \\ \end{array}
$$

At the end of an analysis it is necessary to bound $| < k > -1|$ , for which any of the techniques described above can be used.

Wilkinson explained in [1244, 1985] that he used a similar notation in his research, writing $\psi^r$ for a product of $r$ factors $1 + \delta_i$ with $|\delta_i| \leq u$ . He also derived results for specific values of $n$ before treating the general case—a useful trick of the trade!

An alternative notation to $fl(\cdot)$ to denote the rounded value of a number or the computed value of an expression is $[-]$ , suggested by Kahan. Thus, we would write $[a + [bc]]$ instead of $fl(a + fl(bc))$ .

A completely different notation for error analysis was proposed by Olver [903, 1978], and subsequently used by him and several other authors. For scalars $x$ and $y$ of the same sign, Olver defines the relative precision rp as follows:

$$
y \approx x; \operatorname {r p} (\alpha) \quad \text {m e a n s t h a t} \quad y = e ^ {\delta} x, \quad | \delta | \leq \alpha .
$$

Since $e^{\delta} = 1 + \delta + O(\delta^{2})$ , this definition implies that the relative error in $x$ as an approximation to $y$ (or vice versa) is at most $\alpha + O(\alpha^{2})$ . But, unlike the usual definition of relative error, the relative precision possesses the properties of

$$
\begin{array}{l} \text {s y m m e t r y :} \quad y \approx x; \operatorname {r p} (\alpha) \quad \Longleftrightarrow \quad x \approx y; \operatorname {r p} (\alpha), \\ \text {a d d i t i v i t y :} \quad y \approx x; \operatorname {r p} (\alpha) \text {a n d} z \approx y; \operatorname {r p} (\beta) \quad \Longrightarrow \quad z \approx x; \operatorname {r p} (\alpha + \beta). \\ \end{array}
$$

Proponents of relative precision claim that the symmetry and additivity properties make it easier to work with than the relative error.

Pryce [956, 1981] gives an excellent appraisal of relative precision, with many examples. He uses the additional notation $1(\delta)$ to mean a number $\theta$ with $\theta \approx 1$ ; $\mathbf{rp}(\delta)$ . The $1(\delta)$ notation is the analogue for relative precision of Stewart's $< k>$ counter for relative error. In later papers, Pryce extends the rp notation to vectors and matrices and shows how it can be used in the error analysis of some basic matrix computations [957, 1984], [958, 1985].

Relative precision has not achieved wide use. The important thing for an error analyst is to settle on a comfortable notation that does not hinder the thinking process. It does not really matter which of the notations described in this section is used, as long as the final result is informative and expressed in a readable form.

# 3.5. Matrix Multiplication

Given error analysis for inner products it is straightforward to analyse matrix-vector and matrix-matrix products. Let $A \in \mathbb{R}^{m \times n}$ , $x \in \mathbb{R}^n$ , and $y = Ax$ . The vector $y$ can be formed as $m$ inner products, $y_i = a_i^T x$ , $i = 1: m$ , where $a_i^T$ is the $i$ th row of $A$ . From (3.4) we have

$$
\widehat {y} _ {i} = \left(a _ {i} + \Delta a _ {i}\right) ^ {T} x, \qquad | \Delta a _ {i} | \leq \gamma_ {n} | a _ {i} |.
$$

This gives the backward error result

$$
\hat {y} = (A + \Delta A) x, \quad | \Delta A | \leq \gamma_ {n} | A | \quad (A \in \mathbb {R} ^ {m \times n}), \tag {3.11}
$$

which implies the forward error bound

$$
| y - \widehat {y} | \leq \gamma_ {n} | A | | x |. \tag {3.12}
$$

Normwise bounds readily follow (see Chapter 6 for norm definitions): we have

$$
\| y - \widehat {y} \| _ {p} \leq \gamma_ {n} \| A \| _ {p} \| x \| _ {p}, \quad p = 1, \infty ,
$$

and for the 2-norm, using Lemma 6.6,

$$
\| y - \widehat {y} \| _ {2} \leq \min  (m, n) ^ {1 / 2} \gamma_ {n} \| A \| _ {2} \| x \| _ {2}.
$$

This inner product formation of $y$ can be expressed algorithmically as

$\%$ Sdot or inner product form. $y(1:m) = 0$ for $i = 1:m$ for $j = 1:n$ $y(i) = y(i) + a(i,j)x(j)$ end   
end

The two loops can be interchanged to give

$\%$ Saxpy form. $y(1:m) = 0$ for $j = 1:n$ for $i = 1:m$ $y(i) = y(i) + a(i,j)x(j)$ end   
end

The terms "sdot" and "saxpy" come from the BLAS (see §C.1). Sdot stands for (single precision) dot product, and saxpy for (single precision) $\alpha$ times $x$ plus $y$ . The question of interest is whether (3.11) and (3.12) hold for the saxpy form. They do: the saxpy algorithm still forms the inner products $a_i^T x$ , but instead of forming each one in turn it evaluates them all "in parallel", a term at a time. The key observation is that exactly the same operations are performed, and hence exactly the same rounding errors are committed—the only difference is the order in which the rounding errors are created.

This "rounding error equivalence" of algorithms that are mathematically identical but algorithmically different is one that occurs frequently in matrix computations. The equivalence is not always as easy to see as it is for matrix-vector products.

Now consider matrix multiplication: $C = AB$ , where $A \in \mathbb{R}^{m \times n}$ and $B \in \mathbb{R}^{n \times p}$ . Matrix multiplication is a triple loop procedure, with six possible loop orderings, one of which is

$C(1:m,1:p) = 0$ for $i = 1:m$

for $j = 1$ : $p$ for $k = 1$ : $n$ $C(i,j) = C(i,j) + A(i,k)B(k,j)$ end  
end

As for the matrix-vector product, all six versions commit the same rounding errors, so it suffices to consider any one of them. The "jik" and "jki" orderings both compute $C$ a column at a time: $c_{j} = Ab_{j}$ , where $c_{j} = C(:, j)$ and $b_{j} = B(:, j)$ . From (3.11),

$$
\widehat {c} _ {j} = (A + \Delta A _ {j}) b _ {j}, \quad | \Delta A _ {j} | \leq \gamma_ {n} | A |.
$$

Hence the $j$ th computed column of $C$ has a small backward error: it is the exact $j$ th column for slightly perturbed data. The same cannot be said for $\widehat{C}$ as a whole (see Problem 3.5 for a possibly large backward error bound). However, we have the forward error bound

$$
| C - \widehat {C} | \leq \gamma_ {n} | A | | B | \quad (A \in \mathbb {R} ^ {m \times n}, B \in \mathbb {R} ^ {n \times p}), \tag {3.13}
$$

and the corresponding normwise bounds include

$$
\| C - \widehat {C} \| _ {p} \leq \gamma_ {n} \| A \| _ {p} \| B \| _ {p}, \qquad p = 1, \infty , F.
$$

The bound (3.13) falls short of the ideal bound $|C - \widehat{C}| \leq \gamma_n |C|$ , which says that each component of $C$ is computed with high relative accuracy. Nevertheless (3.13) is the best bound we can expect, because it reflects the sensitivity of the product to componentwise relative perturbations in the data: for any $i$ and $j$ we can find a perturbation $\Delta A$ with $|\Delta A| \leq u |A|$ such that $|(A + \Delta A)B - AB|_{ij} = u(|A||B|)_{ij}$ (similarly for perturbations in $B$ ).

# 3.6. Complex Arithmetic

To carry out error analysis of algorithms in complex arithmetic we need a model for the basic arithmetic operations. Since complex arithmetic must be implemented using real arithmetic, the complex model is a consequence of the corresponding real one. We will assume that for complex numbers $x = a + ib$ and $y = c + id$ we compute

$$
x \pm y = a \pm c + i (b \pm d), \tag {3.14a}
$$

$$
x y = a c - b d + i (a d + b c), \tag {3.14b}
$$

$$
x / y = \frac {a c + b d}{c ^ {2} + d ^ {2}} + i \frac {b c - a d}{c ^ {2} + d ^ {2}}. \tag {3.14c}
$$

Lemma 3.5. For $x, y \in \mathbb{C}$ the basic arithmetic operations computed according to (3.14) under the standard model (2.4) satisfy

$$
f l (x \pm y) = (x \pm y) (1 + \delta), \quad | \delta | \leq u,
$$

$$
f l (x y) = x y (1 + \delta), \quad | \delta | \leq \sqrt {2} \gamma_ {2},
$$

$$
f l (x / y) = (x / y) (1 + \delta), \quad | \delta | \leq \sqrt {2} \gamma_ {4}.
$$

Proof. Throughout the proof, $\delta_{i}$ denotes a number bounded by $|\delta_i| \leq u$ . Addition/subtraction:

$$
\begin{array}{l} f l (x + y) = (a + c) \left(1 + \delta_ {1}\right) + i (b + d) \left(1 + \delta_ {2}\right) \\ = x + y + (a + c) \delta_ {1} + i (b + d) \delta_ {2}, \\ \end{array}
$$

so

$$
\left| f l (x + y) - (x + y) \right| ^ {2} \leq \left(\left| a + c \right| ^ {2} + \left| b + d \right| ^ {2}\right) u ^ {2} = \left(\left| x + y \right| u\right) ^ {2},
$$

as required.

Multiplication:

$$
\begin{array}{l} f l (x y) = \left(a c \left(1 + \delta_ {1}\right) - b d \left(1 + \delta_ {2}\right)\right) \left(1 + \delta_ {3}\right) \\ + i \left(a d \left(1 + \delta_ {4}\right) + b c \left(1 + \delta_ {5}\right)\right) \left(1 + \delta_ {6}\right) \\ = a c \left(1 + \theta_ {2}\right) - b d \left(1 + \theta_ {2} ^ {\prime}\right) + i \left(a d \left(1 + \theta_ {2} ^ {\prime \prime}\right) + b c \left(1 + \theta_ {2} ^ {\prime \prime \prime}\right)\right) \\ = x y + e, \\ \end{array}
$$

where

$$
\begin{array}{l} \left| e \right| ^ {2} \leq \gamma_ {2} ^ {2} \left(\left(| a c | + | b d |\right) ^ {2} + \left(| a d | + | b c |\right) ^ {2}\right) \\ \leq 2 \gamma_ {2} ^ {2} (a ^ {2} + b ^ {2}) (c ^ {2} + d ^ {2}) \\ = 2 \gamma_ {2} ^ {2} | x y | ^ {2}, \\ \end{array}
$$

as required.

Division:

$$
\begin{array}{l} f l \left(c ^ {2} + d ^ {2}\right) = \left(c ^ {2} \left(1 + \delta_ {1}\right) + d ^ {2} \left(1 + \delta_ {2}\right)\right) \left(1 + \delta_ {3}\right) \\ = c ^ {2} \left(1 + \theta_ {2}\right) + d ^ {2} \left(1 + \theta_ {2} ^ {\prime}\right) \\ = \left(c ^ {2} + d ^ {2}\right) \left(1 + \theta_ {2} ^ {\prime \prime}\right). \\ \end{array}
$$

Then

$$
\begin{array}{l} f l (\operatorname {R e} x / y) = \frac {\left(a c \left(1 + \delta_ {4}\right) + b d \left(1 + \delta_ {5}\right)\right) \left(1 + \delta_ {6}\right)}{\left(c ^ {2} + d ^ {2}\right) \left(1 + \theta_ {2} ^ {\prime \prime}\right)} \\ = \frac {a c \left(1 + \theta_ {2} ^ {\prime \prime \prime}\right) + b d \left(1 + \theta_ {2} ^ {\prime \prime \prime \prime}\right)}{\left(c ^ {2} + d ^ {2}\right) \left(1 + \theta_ {2} ^ {\prime \prime}\right)} \\ = \operatorname {R e} x / y + e _ {1}, \\ \end{array}
$$

where, using Lemma 3.3,

$$
\left| e _ {1} \right| \leq \frac {\left| a c \right| + \left| b d \right|}{c ^ {2} + d ^ {2}} \gamma_ {4}.
$$

Using the analogous formula for the error in $fl(\operatorname{Im} x / y)$ ,

$$
\begin{array}{l} | f l (x / y) - x / y | ^ {2} \leq \frac {\left(| a c | + | b d |\right) ^ {2} + \left(| b c | + | a d |\right) ^ {2}}{\left(c ^ {2} + d ^ {2}\right) ^ {2}} \gamma_ {4} ^ {2} \\ \leq \frac {2 (a ^ {2} + b ^ {2}) (c ^ {2} + d ^ {2})}{(c ^ {2} + d ^ {2}) ^ {2}} \gamma_ {4} ^ {2} \\ = 2 \gamma_ {4} ^ {2} | x / y | ^ {2}, \\ \end{array}
$$

which completes the proof.

It is worth stressing that $\delta$ in Lemma 3.5 is a complex number, so we cannot conclude from the lemma that the real and imaginary parts of $fl(x \operatorname{op} y)$ are obtained to high relative accuracy—only that they are obtained to high accuracy relative to $|x \operatorname{op} y|$ .

As explained in §27.8, the formula (3.14c) is not recommended for practical use since it is susceptible to overflow. For the alternative formula (27.1), which avoids overflow, similar analysis to that in the proof of Lemma 3.5 shows that

$$
f l (x / y) = (x / y) (1 + \delta), \quad | \delta | \leq \sqrt {2} \gamma_ {7}.
$$

Bounds for the rounding errors in the basic complex arithmetic operations are rarely given in the literature. Indeed, virtually all published error analyses in matrix computations are for real arithmetic. However, because the bounds of Lemma 3.5 are of the same form as for the standard model (2.4) for real arithmetic, most results for real arithmetic (including virtually all those in this book) are valid for complex arithmetic, provided that the constants are increased appropriately.

# 3.7. Miscellany

In this section we give some miscellaneous results that will be needed in later chapters. The first three results provide convenient ways to bound the effect of perturbations in a matrix product. The first two results use norms and the third, components.

Lemma 3.6. If $X_{j} + \Delta X_{j}\in \mathbb{R}^{n\times n}$ satisfies $\| \Delta X_j\| \leq \delta_j\| X_j\|$ for all $j$ for a consistent norm, then

$$
\left\| \prod_ {j = 0} ^ {m} (X _ {j} + \varDelta X _ {j}) - \prod_ {j = 0} ^ {m} X _ {j} \right\| \leq \left(\prod_ {j = 0} ^ {m} (1 + \delta_ {j}) - 1\right) \prod_ {j = 0} ^ {m} \| X _ {j} \|.
$$

Proof. The proof is a straightforward induction, which we leave as an exercise (Problem 3.9). $\square$

The second lemma is a variation on the first, with an analogous proof that employs the inequality in Problem 6.5. It is useful when analysing Householder transformations (see Chapter 19).

Lemma 3.7. If $X_{j} + \Delta X_{j}\in \mathbb{R}^{n\times n}$ satisfies $\| \Delta X_j\| _F\leq \delta_j\| X_j\| _2$ for all $j$ , then

$$
\left\| \prod_ {j = 0} ^ {m} \left(X _ {j} + \Delta X _ {j}\right) - \prod_ {j = 0} ^ {m} X _ {j} \right\| _ {F} \leq \left(\prod_ {j = 0} ^ {m} \left(1 + \delta_ {j}\right) - 1\right) \prod_ {j = 0} ^ {m} \| X _ {j} \| _ {2}.
$$

In comparing the last lemma with Lemma 3.6 for the Frobenius norm, note that the product $\|X_1\|_2 \ldots \|X_k\|_2$ can be much smaller than $\|X_1\|_F \ldots \|X_k\|_F$ ; the extreme case occurs when the $X_i$ are orthogonal.

A componentwise result is entirely analogous.

Lemma 3.8. If $X_{j} + \Delta X_{j}\in \mathbb{R}^{n\times n}$ satisfies $|\Delta X_j|\leq \delta_j|X_j|$ for all $j$ , then

$$
\left| \prod_ {j = 0} ^ {m} \left(X _ {j} + \Delta X _ {j}\right) - \prod_ {j = 0} ^ {m} X _ {j} \right| \leq \left(\prod_ {j = 0} ^ {m} \left(1 + \delta_ {j}\right) - 1\right) \prod_ {j = 0} ^ {m} | X _ {j} |.
$$

The final result describes the computation of the "rank-1 update" $y = (I - ab^T)x$ , which is an operation arising in various algorithms, including the Gram-Schmidt method and Householder QR factorization.

Lemma 3.9. Let $a, b, x \in \mathbb{R}^n$ and let $y = (I - ab^T)x$ be computed as $\widehat{y} = fl(x - a(b^Tx))$ . Then $\widehat{y} = y + \Delta y$ , where

$$
| \varDelta y | \leq \gamma_ {n + 3} (I + | a | | b ^ {T} |) | x |,
$$

so that

$$
\left\| \Delta y \right\| _ {2} \leq \gamma_ {n + 3} (1 + \| a \| _ {2} \| b \| _ {2}) \| x \| _ {2}.
$$

Proof. Consider first the computation of $w = a(b^{T}x)$ . We have

$$
\begin{array}{l} \widehat {w} := (a + \Delta a) b ^ {T} (x + \Delta x), \quad | \Delta a | \leq u | a |, \quad | \Delta x | \leq \gamma_ {n} | x |, \\ = a \left(b ^ {T} x\right) + a \left(b ^ {T} \Delta x\right) + \Delta a b ^ {T} (x + \Delta x) \\ =: w + \Delta w, \\ \end{array}
$$

where

$$
\left| \Delta w \right| \leq \left(\gamma_ {n} + u \left(1 + \gamma_ {n}\right)\right) \left| a \right| \left| b ^ {T} \right| \left| x \right|.
$$

Finally, $\widehat{y} = f l(x - \widehat{w})$ satisfies

$$
\widehat {y} = x - a \left(b ^ {T} x\right) - \Delta w + \Delta y _ {1}, \quad | \Delta y _ {1} | \leq u (| x | + | \widehat {w} |),
$$

and

$$
\left| - \Delta w + \Delta y _ {1} \right| \leq u \left(\left| x \right| + \left| a \right| \left| b ^ {T} \right| \left| x \right|\right) + \left(1 + u\right) \left(\gamma_ {n} + u \left(1 + \gamma_ {n}\right)\right) \left| a \right| \left| b ^ {T} \right| \left| x \right|.
$$

Hence $\widehat{y} = y + \Delta y$ , where

$$
\begin{array}{l} \left| \Delta y \right| \leq \left[ u I + \left(2 u + u ^ {2} + \gamma_ {n} + 2 u \gamma_ {n} + u ^ {2} \gamma_ {n}\right) \left| a \right| \left| b ^ {T} \right| \right] | x | \\ \leq \gamma_ {n + 3} (I + | a | | b ^ {T} |) | x |. \\ \end{array}
$$

# 3.8. Error Analysis Demystified

The principles underlying an error analysis can easily be obscured by the details. It is therefore instructive to examine the basic mechanism of forward and backward error analyses. We outline a general framework that reveals the essential simplicity.

Consider the problem of computing $z = f(a)$ , where $f: \mathbb{R}^n \to \mathbb{R}^m$ . Any algorithm for computing $z$ can be expressed as follows. Let $x_1 = a$ and $x_{k+1} = g_k(x_k)$ , $k = 1:p$ , where

$$
x _ {k + 1} = \left[ \begin{array}{c} x _ {k} \\ \xi_ {k} \end{array} \right], \qquad \xi_ {k} \in \mathbb {R}.
$$

The $k$ th stage of the algorithm represents a single floating point operation and $x_{k}$ contains the original data together with all the intermediate quantities computed so far. Finally, $z = \overline{I} x_{p + 1}$ , where $\overline{I}$ is comprised of a subset of the columns of the identity matrix (so that each $z_{i}$ is a component of $x_{p + 1}$ ). In floating point arithmetic we have

$$
\widehat {x} _ {k + 1} = g _ {k} \left(\widehat {x} _ {k}\right) + \Delta x _ {k + 1},
$$

where $\Delta x_{k+1}$ represents the rounding errors on the $k$ th stage and should be easy to bound. We assume that the functions $g_k$ are continuously differentiable and denote the Jacobian of $g_k$ at $a$ by $J_k$ . Then, to first order,

$$
\begin{array}{l} \widehat {x} _ {2} = g _ {1} (a) + \Delta x _ {2}, \\ \widehat {x} _ {3} = g _ {2} (\widehat {x} _ {2}) + \Delta x _ {3} = g _ {2} \left(g _ {1} (a) + \Delta x _ {2}\right) + \Delta x _ {3} \\ = g _ {2} \left(g _ {1} (a)\right) + J _ {2} \Delta x _ {2} + \Delta x _ {3}, \\ \end{array}
$$

$$
\begin{array}{l} \widehat {x} _ {4} = g _ {3} \left(\widehat {x} _ {3}\right) + \Delta x _ {4} = g _ {3} \left(g _ {2} \left(g _ {1} (a)\right) + J _ {2} \Delta x _ {2} + \Delta x _ {3}\right) + \Delta x _ {4} \\ = g _ {3} \left(g _ {2} \left(g _ {1} (a)\right)\right) + J _ {3} J _ {2} \Delta x _ {2} + J _ {3} \Delta x _ {3} + \Delta x _ {4}. \\ \end{array}
$$

The pattern is clear: for the final $\widehat{z} = \widehat{x}_{p + 1}$ we have

$$
\begin{array}{l} \hat {z} = \bar {I} \left[ g _ {p} \left(\dots g _ {2} \left(g _ {1} (a)\right) \dots\right) + J _ {p} \dots J _ {2} \Delta x _ {2} + J _ {p} \dots J _ {3} \Delta x _ {3} + \dots \right. \\ \left. + J _ {p} \Delta x _ {p} + \Delta x _ {p + 1} \right] \\ = f (a) + \overline {{I}} [ J _ {p} \ldots J _ {2}, \ldots , J _ {p}, I ] \left[ \begin{array}{c} \Delta x _ {2} \\ \Delta x _ {3} \\ \vdots \\ \Delta x _ {p + 1} \end{array} \right] =: f (a) + J h. \\ \end{array}
$$

In a forward error analysis we bound $f(a) - \widehat{z}$ , which requires bounds for (products of) the Jacobians $J_{k}$ . In a backward error analysis we write, again to first order,

$$
f (a) + J h = \widehat {z} = f (a + \Delta a) = f (a) + J _ {f} \Delta a,
$$

where $J_{f}$ is the Jacobian of $f$ . So we need to solve, for $\Delta a$

$$
\underbrace {J _ {f}} _ {m \times n} \underbrace {\Delta a} _ {n \times 1} = \underbrace {J} _ {m \times q} \underbrace {h} _ {q \times 1}, \qquad q = p (n + (p + 1) / 2).
$$

In most matrix problems there are fewer outputs than inputs ( $m < n$ ), so this is an underdetermined system. For a normwise backward error analysis we want a solution of minimum norm. For a componentwise backward error analysis, in which we may want (for example) to minimize $\epsilon$ subject to $|\Delta a| \leq \epsilon |a|$ , we can write

$$
J h = J _ {f} D \cdot D ^ {- 1} \Delta a =: B c, \quad D = \operatorname {d i a g} \left(a _ {i}\right),
$$

and then we want the solution $c$ of minimal $\infty$ -norm.

The conclusions are that forward error analysis corresponds to bounding derivatives and that backward error analysis corresponds to solving a large underdetermined linear system for a solution of minimal norm. In principal, therefore, error analysis is straightforward! Complicating factors in practice are that the Jacobians

$J_{k}$ may be difficult to obtain explicitly, that an error bound has to be expressed in a form that can easily be interpreted, and that we may want to keep track of higher-order terms.

# 3.9. Other Approaches

In this book we do not describe all possible approaches to error analysis. Some others are mentioned in this section.

Linearized rounding error bounds can be developed by applying equations that describe, to first order, the propagation of absolute or relative errors in the elementary operations $+, -, *,$ . The basics of this approach are given in many textbooks (see, for example, Dahlquist and Björck [289, 1974, §2.2] or Stoer and Bulirsch [1086, 1980, §1.3]), but for a thorough treatment see Stummel [1094, 1980], [1095, 1981]. Ziv [1286, 1995] shows that linearized bounds can be turned into true bounds by increasing them by a factor that depends on the algorithm.

Rounding error analysis can be phrased in terms of graphs. This appears to have been first suggested by McCracken and Dorn [833, 1964], who use "process graphs" to represent a numerical computation and thereby to analyse the propagation of rounding errors. Subsequent more detailed treatments include those of Bauer [93, 1974], Miller [852, 1976], and Yalamov [1263, 1995]. The work on graphs falls under the heading of automatic error analysis (for more on which see Chapter 26) because processing of the large graphs required to represent practical computations is impractical by hand. Linnainmaa [790, 1976] shows how to compute the Taylor series expansion of the forward error in an algorithm in terms of the individual rounding errors, and he presents a graph framework for the computation.

Some authors have taken a computational complexity approach to error analysis, by aiming to minimize the number of rounding error terms in a forward error bound, perhaps by rearranging a computation. Because this approach ignores the possibility of cancellation of rounding errors, the results need to be interpreted with care. See Aggarwal and Burgmeier [7, 1979] and Tsao [1162, 1983].

# 3.10. Notes and References

The use of Lemma 3.1 for rounding error analysis appears to originate with the original German edition [1085, 1972] of a book by Stoer and Bulirsch [1086, 1980]. The lemma is also used, with $\rho_{i} \equiv 1$ , by Shampine and Allen [1031, 1973, p. 18].

The notation $\tilde{\gamma}_n$ in (3.8) was suggested to the author by Beresford Parlett and replaces the more clumsy notation $\gamma_{cn}$ used in the first edition of this book.

Lemma 3.4 is given by Forsythe and Moler [431, 1967, p. 92]. Wilkinson made frequent use of a slightly different version of Lemma 3.4 in which the assumption is $nu < 0.1$ and the bound for $|\eta_n|$ is $1.06nu$ (see, e.g., [1233, 1965, p. 113]).

A straightforward notation for rounding errors that is subsumed by the notation described in this chapter is suggested by Scherer and Zeller [1017, 1980].

Ziv [1284, 1982] proposes the relative error measure

$$
d (x, y) = \| x - y \| / \max  (\| x \|, \| y \|)
$$

for vectors $x$ and $y$ and explains some of its favourable properties for error analysis.

Wilkinson [1233, 1965, p. 447] gives error bounds for complex arithmetic; Olver [904, 1983] does the same in the relative precision framework. Demmel [308, 1984] gives error bounds that extend those in Lemma 3.5 by taking into account the possibility of underflow.

Henrici [568, 1980] gives a brief, easy-to-read introduction to the use of the model (2.4) for analysing the propagation of rounding errors in a general algorithm. He uses a set notation that is another possible notation to add to those in §3.4.

The perspective on error analysis in §3.8 was suggested by J. W. Demmel.

# Problems

3.1. Prove Lemma 3.1.   
3.2. (Kiełbasinski and Schwetlick [734, 1988], [735, 1992]) Show that if $\rho_{i} \equiv 1$ in Lemma 3.1 then the stronger bound $|\theta_{n}| \leq nu / (1 - \frac{1}{2} nu)$ holds for $nu < 2$ .   
3.3. One algorithm for evaluating a continued fraction

$$
a _ {0} + \frac {b _ {0}}{a _ {1} + \frac {b _ {1}}{a _ {2} + \cdots + \frac {b _ {n}}{a _ {n + 1}}}}
$$

is

$$
q _ {n + 1} = a _ {n + 1}
$$

for $k = n: -1:0$

$$
q _ {k} = a _ {k} + b _ {k} / q _ {k + 1}
$$

end

Derive a running error bound for this algorithm.

3.4. Prove Lemma 3.3.

3.5. (Backward error result for matrix multiplication.) Let $A \in \mathbb{R}^{n \times n}$ and $B \in \mathbb{R}^{n \times n}$ both be nonsingular. Show that $fl(AB) = (A + \Delta A)B$ , where $|\Delta A| \leq \gamma_n |A||B||B^{-1}|$ , and derive a corresponding bound in which $B$ is perturbed.

3.6. (Backward error definition for matrix multiplication.) Let $A \in \mathbb{R}^{m \times n}$ and $B \in \mathbb{R}^{n \times p}$ be of full rank and suppose $C \approx AB$ . Define the componentwise backward error

$$
\omega = \min  \left\{\epsilon : C = (A + \Delta A) (B + \Delta B), \quad | \Delta A | \leq \epsilon E,   | \Delta B | \leq \epsilon F \right\},
$$

where $E$ and $F$ have nonnegative entries. Show that

$$
\omega \geq \max  _ {i, j} \left(\sqrt {1 + \frac {\left| r _ {i j} \right|}{g _ {i j}}} - 1\right),
$$

where $R = C - AB$ and $G = EF$ . Explain why the definition of $\omega$ makes sense only when $A$ and $B$ have full rank. Define a mixed backward/forward error applicable to the general case.

3.7. Give analogues of the backward error results (3.4) and (3.11) for complex $x$ , $y$ , and $A$ .   
3.8. Which is the more accurate way to compute $x^{2} - y^{2}$ : as $x^{2} - y^{2}$ or as $(x + y)(x - y)$ ? (Note that this computation arises when squaring a complex number.)   
3.9. Prove Lemma 3.6.   
3.10. Let $A_{1},\ldots ,A_{k}\in \mathbb{R}^{n\times n}$ . Show that

$$
\left\| A _ {1} \dots A _ {k} - f l (A _ {1} \dots A _ {k}) \right\| _ {F} \leq \left(k n ^ {2} u + O (u ^ {2})\right) \left\| A _ {1} \right\| _ {2} \dots \left\| A _ {k} \right\| _ {2}.
$$

3.11. (Kahan [690, 1980]) Consider this MATLAB function, which returns the absolute value of its first argument $x \in \mathbb{R}^n$ :

$$
f u n c t i o n \mathbf {z} = \text {a b s o l u t e} (\mathbf {x}, \mathbf {m})
$$

$$
\begin{array}{l} \mathbf {y} = \mathbf {x}. \hat {\mathbf {\Gamma}} 2; \\ f o r \quad i = 1: m \\ y = \operatorname {s q r t} (y); \\ e n d \\ z = y; \\ f o r \quad i = 1: m - 1 \\ z = z. \hat {\cdot} 2; \\ \mathbf {\Pi} _ {\mathrm {e n d}} \\ \end{array}
$$

Here is some output from a Pentium III workstation (which uses IEEE standard double precision arithmetic):

$$
\begin{array}{l} \gg x = [. 2 5. 5. 7 5 1. 2 5 1. 5 2 ]; z = \text {a b s o l u t e} (x, 5 0); [ x; z ] \\ \text {a n s} = \\ 0. 2 5 0 0 \quad 0. 5 0 0 0 \quad 0. 7 5 0 0 \quad 1. 2 5 0 0 \quad 1. 5 0 0 0 \quad 2. 0 0 0 0 \\ 0. 2 3 7 5 \quad 0. 4 7 2 4 \quad 0. 7 3 1 6 \quad 1. 1 3 3 1 \quad 1. 4 5 5 0 \quad 1. 8 6 8 2 \\ \end{array}
$$

Give an error analysis to explain the results.

3.12. Consider the quadrature rule

$$
I (f) := \int_ {a} ^ {b} f (x) d x \approx \sum_ {i = 1} ^ {n} w _ {i} f \left(x _ {i}\right) =: J (f),
$$

where the weights $w_{i}$ and nodes $x_{i}$ are assumed to be floating point numbers. Assuming that the sum is evaluated in left-to-right order and that

$$
f l \left(f \left(x _ {i}\right)\right) = f \left(x _ {i}\right) \left(1 + \eta_ {i}\right), \quad | \eta_ {i} | \leq \eta ,
$$

obtain and interpret a bound for $|I(f) - \widehat{J}(f)|$ , where $\widehat{J}(f) = fl(J(f))$ .
