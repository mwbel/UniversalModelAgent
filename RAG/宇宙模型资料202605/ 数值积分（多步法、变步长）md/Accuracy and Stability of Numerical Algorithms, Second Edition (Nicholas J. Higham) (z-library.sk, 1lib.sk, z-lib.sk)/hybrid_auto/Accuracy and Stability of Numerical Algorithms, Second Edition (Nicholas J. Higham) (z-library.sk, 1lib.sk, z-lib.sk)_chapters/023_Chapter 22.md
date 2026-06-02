# Chapter 22

# Vandermonde Systems

We began, 25 years ago, to take up [the conditioning of]

the class of Vandermonde matrices.

The original motivation came from unpleasant experiences with the

computation of Gauss type quadrature rules from the

moments of the underlying weight function.

— WALTER GAUTsCHI, How (Un)stable Are Vandermonde Systems? (1990)

Extreme ill-conditioning of the [Vandermonde] linear systems

will eventually manifest itself as $n$ increases by yielding

an error curve which is not sufficiently levelled on the current reference ...

or more seriously fails to have the correct number of sign changes.

— M. ALMACANY, C. B. DUNHAM, and J. WILLIAMS,

Discrete Chebyshev Approximation by Interpolating Rationals (1984)

A Vandermonde matrix is defined in terms of scalars $\alpha_0, \alpha_1, \ldots, \alpha_n \in \mathbb{C}$ by

$$
V = V (\alpha_ {0}, \alpha_ {1}, \ldots , \alpha_ {n}) = \left[ \begin{array}{c c c c} 1 & 1 & \ldots & 1 \\ \alpha_ {0} & \alpha_ {1} & \ldots & \alpha_ {n} \\ \vdots & \vdots & & \vdots \\ \alpha_ {0} ^ {n} & \alpha_ {1} ^ {n} & \ldots & \alpha_ {n} ^ {n} \end{array} \right] \in \mathbb {C} ^ {(n + 1) \times (n + 1)}.
$$

Vandermonde matrices play an important role in various problems, such as in polynomial interpolation. Suppose we wish to find the polynomial $p_n(x) = a_n x^n + a_{n-1} x^{n-1} + \dots + a_0$ that interpolates to the data $(\alpha_i, f_i)_{i=0}^n$ , for distinct points $\alpha_i$ , that is, $p_n(\alpha_i) = f_i$ , $i = 0:n$ . Then the desired coefficient vector $a = [a_0, a_1, \ldots, a_n]^T$ is the solution of the dual Vandermonde system

$$
V ^ {T} a = f \quad (\text {d u a l}).
$$

The primal system

$$
V x = b \quad (\text {p r i m a l})
$$

represents a moment problem, which arises, for example, when determining the weights for a quadrature rule: given moments $b_{i}$ find weights $x_{i}$ such that $\sum_{j=0}^{n} x_{j} \alpha_{j}^{i} = b_{i}, i = 0:n$ .

Because a Vandermonde matrix depends on only $n + 1$ parameters and has a great deal of structure, it is possible to perform standard computations with reduced complexity. The easiest algorithm to derive is for matrix inversion.

# 22.1. Matrix Inversion

Assume that $V$ is nonsingular and let $V^{-1} = W = (w_{ij})_{i,j=0}^{n}$ . The $i$ th row of the equation $WV = I$ may be written

$$
\sum_ {j = 0} ^ {n} w _ {i j} \alpha_ {k} ^ {j} = \delta_ {i k}, \quad k = 0: n.
$$

These equations specify a fundamental interpolation problem that is solved by the Lagrange basis polynomial:

$$
\sum_ {j = 0} ^ {n} w _ {i j} x ^ {j} = \prod_ {\substack {k = 0 \\ k \neq i}} ^ {n} \left(\frac {x - \alpha_ {k}}{\alpha_ {i} - \alpha_ {k}}\right) =: l _ {i} (x). \tag{22.1}
$$

The inversion problem is now reduced to finding the coefficients of $l_{i}(x)$ . It is clear from (22.1) that $V$ is nonsingular iff the $\alpha_{i}$ are distinct. It also follows from (22.1) that $V^{-1}$ is given explicitly by

$$
w _ {i j} = \frac {\left(- 1\right) ^ {n - j} \sigma_ {n - j} \left(\alpha_ {0} , \dots , \alpha_ {i - 1} , \alpha_ {i + 1} , \dots , \alpha_ {n}\right)}{\prod_ {\substack {k = 0 \\ k \neq i}} ^ {n} \left(\alpha_ {i} - \alpha_ {k}\right)}, \tag{22.2}
$$

where $\sigma_{k}(y_{1},\ldots ,y_{n})$ denotes the sum of all distinct products of $k$ of the arguments $y_{1},\ldots ,y_{n}$ (that is, $\sigma_{k}$ is the $k$ th elementary symmetric function). An efficient way to find the $w_{ij}$ is first to form the master polynomial

$$
\phi (x) = \prod_ {k = 0} ^ {n} (x - \alpha_ {k}) =: \sum_ {i = 0} ^ {n + 1} a _ {i} x ^ {i},
$$

and then to recover each Lagrange polynomial by synthetic division:

$$
\begin{array}{l} q _ {i} (x) = \phi (x) / (x - \alpha_ {i}), \\ l _ {i} (x) = q _ {i} (x) / q _ {i} (\alpha_ {i}). \\ \end{array}
$$

The scalars $q_{i}(\alpha_{i})$ can be computed by Horner's rule as the coefficients of $q_{i}$ are formed.

Algorithm 22.1. Given distinct scalars $\alpha_0, \alpha_1, \ldots, \alpha_n \in \mathbb{C}$ this algorithm computes $W = (w_{ij})_{i,j=0}^{n} = V(\alpha_0, \alpha_1, \ldots, \alpha_n)^{-1}$ .

% Stage 1: Construct the master polynomial.

$a_0 = -\alpha_0$ . $a_1 = 1$

for $k = 1:n$

$$
a _ {k + 1} = 1
$$

$$
f o r j = k: - 1: 1
$$

$$
a _ {j} = a _ {j - 1} - \alpha_ {k} a _ {j}
$$

end

$$
a _ {0} = - \alpha_ {k} a _ {0}
$$

end

% Stage 2: Synthetic division.

for $i = 0:n$

$$
w _ {i n} = 1; s = 1
$$

$$
\text {f o r} j = n - 1: - 1: 0
$$

$$
w _ {i j} = a _ {j + 1} + \alpha_ {i} w _ {i, j + 1}
$$

$$
s = \alpha_ {i} s + w _ {i j}
$$

end

$$
w (i,:) = w (i,:) / s
$$

end

Cost: $6n^{2}$ flops.

The $O(n^{2})$ complexity is optimal, since the algorithm has $n^{2}$ output values, each of which must partake in at least one operation.

Vandermonde matrices have the deserved reputation of being ill conditioned. The ill conditioning is a consequence of the monomials being a poor basis for the polynomials on the real line. A variety of bounds for the condition number of a Vandermonde matrix have been derived. Let $V_{n} = V(\alpha_{0},\alpha_{1},\ldots ,\alpha_{n - 1}) \in \mathbb{C}^{n\times n}$ . For arbitrary distinct points $\alpha_{i}$ ,

$$
\max  _ {i} \prod_ {j \neq i} \frac {\operatorname* {m a x} (1 , | \alpha_ {j} |)}{| \alpha_ {i} - \alpha_ {j} |} \leq \| V _ {n} ^ {- 1} \| _ {\infty} \leq \max  _ {i} \prod_ {j \neq i} \frac {1 + | \alpha_ {j} |}{| \alpha_ {i} - \alpha_ {j} |}, \tag {22.3}
$$

Table 22.1. Bounds and estimates for $\kappa (V_n)$   

<table><tr><td colspan="2">αi</td><td>Bound or estimate</td><td>Reference</td></tr><tr><td>(V1):</td><td>1/i+1</td><td>κ∞(Vn) &gt; n^{n+1}</td><td>[468, 1990]</td></tr><tr><td>(V2):</td><td>arbitrary real</td><td>κ2(Vn) ≥ (2/n+1)1/2 (1 + √2)n-1</td><td>[98, 2000]</td></tr><tr><td>(V3):</td><td>αi≥ 0</td><td>κ2(Vn) ≥ 1/2√n+1[(1 + √2)2n+(1 + √2)−2n]</td><td>[98, 2000]</td></tr><tr><td>(V4):</td><td>equispaced [0,1]</td><td>κ∞(Vn) ~ (4π)-1√2 8n</td><td>[468, 1990]</td></tr><tr><td>(V5):</td><td>equispaced [-1,1]</td><td>κ∞(Vn) ~ π-1e-π/4(3.1)n</td><td>[465, 1975]</td></tr><tr><td>(V6):</td><td>Chebyshev nodes [-1,1]</td><td>κ∞(Vn) ~ 33/4(1 + √2)n</td><td>[465, 1975]</td></tr><tr><td>(V7):</td><td>roots of unity</td><td>κ2(Vn) = 1</td><td>well known</td></tr></table>

with equality on the right when $\alpha_{j} = |\alpha_{j}|e^{i\theta}$ for all $j$ with a fixed $\theta$ (in particular, when $\alpha_{j}\geq 0$ for all $j$ ) [464, 1962], [466, 1978]. Note that the upper and lower bounds differ by at most a factor $2^{n - 1}$ . More specific bounds are given in Table 22.1, on which we now comment.

Bound (V1) and estimate (V4) follow from (22.3). The condition number for the harmonic points $1 / (i + 1)$ grows faster than $n!$ ; by contrast, the condition numbers of the notoriously ill-conditioned Hilbert and Pascal matrices grow only exponentially (see §§28.1 and 28.4). For any choice of real points the rate of growth is at least exponential (V2), and this rate is achieved for points equally spaced on [0, 1]. For points equally spaced on $[-1, 1]$ the condition number grows at a slower exponential rate than that for [0, 1], and the growth rate is slower still for the zeros of the $n$ th degree Chebyshev polynomial (V6). For one set of points the Vandermonde matrix is perfectly conditioned: the roots of unity, for which $V_{n} / \sqrt{n}$ is unitary.

# 22.2. Primal and Dual Systems

The standard Vandermonde matrix can be generalized in at least two ways: by allowing confluency of the points $\alpha_{i}$ and by replacing the monomials by other polynomials. An example of a confluent Vandermonde matrix is

$$
\left[ \begin{array}{c c c c c} 1 & 0 & 0 & 1 & 0 \\ \alpha_ {0} & 1 & 0 & \alpha_ {1} & 1 \\ \alpha_ {0} ^ {2} & 2 \alpha_ {0} & 2 & \alpha_ {1} ^ {2} & 2 \alpha_ {1} \\ \alpha_ {0} ^ {3} & 3 \alpha_ {0} ^ {2} & 6 \alpha_ {0} & \alpha_ {1} ^ {3} & 3 \alpha_ {i} ^ {2} \\ \alpha_ {0} ^ {4} & 4 \alpha_ {0} ^ {3} & 1 2 \alpha_ {0} ^ {2} & \alpha_ {1} ^ {4} & 4 \alpha_ {i} ^ {3} \end{array} \right]. \tag {22.4}
$$

The second, third, and fifth columns are obtained by "differentiating" the previous column. The transpose of a confluent Vandermonde matrix arises in Hermite interpolation; it is nonsingular if the points corresponding to the "nonconfluent columns" are distinct.

A Vandermonde-like matrix is defined by $P = (p_i(\alpha_j))_{i,j=0}^n$ , where $p_i$ is a polynomial of degree $i$ . The case of practical interest is where the $p_i$ satisfy a three-

term recurrence relation. In the rest of this chapter we will assume that the $p_i$ do satisfy a three-term recurrence relation. A particular application is the solution of certain discrete Chebyshev approximation problems [12, 1984]. Incorporating confluency, we obtain a confluent Vandermonde-like matrix, defined by

$$
P = P \left(\alpha_ {0}, \alpha_ {1}, \dots , \alpha_ {n}\right) = \left[ q _ {0} \left(\alpha_ {0}\right), q _ {1} \left(\alpha_ {1}\right), \dots , q _ {n} \left(\alpha_ {n}\right) \right] \in \mathbb {C} ^ {(n + 1) \times (n + 1)},
$$

where the $\alpha_{i}$ are ordered so that equal points are contiguous, that is,

$$
\alpha_ {i} = \alpha_ {j} \quad (i <   j) \quad \Rightarrow \quad \alpha_ {i} = \alpha_ {i + 1} = \dots = \alpha_ {j}, \tag {22.5}
$$

and the vectors $q_{j}(x)$ are defined recursively by

$$
q _ {j} (x) = \left\{ \begin{array}{l l} {[ p _ {0} (x), p _ {1} (x), \dots , p _ {n} (x) ] ^ {T},} & {\mathrm {i f} j = 0 \mathrm {o r} \alpha_ {j} \neq \alpha_ {j - 1},} \\ {\frac {d}{d x} q _ {j - 1} (x),} & {\mathrm {o t h e r w i s e}.} \end{array} \right.
$$

For all polynomials and points, $P$ is nonsingular; this follows from the derivation of the algorithms below. One reason for the interest in Vandermonde-like matrices is that for certain polynomials they tend to be better conditioned than Vandermonde matrices (see, for example, Problem 22.5). Gautschi [467, 1983] derives bounds for the condition numbers of Vandermonde-like matrices.

Fast algorithms for solving the confluent Vandermonde-like primal and dual systems $Px = b$ and $P^T a = f$ can be derived under the assumption that the $p_j(x)$ satisfy the three-term recurrence relation

$$
p _ {j + 1} (x) = \theta_ {j} \left(x - \beta_ {j}\right) p _ {j} (x) - \gamma_ {j} p _ {j - 1} (x), \quad j \geq 1, \tag {22.6a}
$$

$$
p _ {0} (x) = 1, \quad p _ {1} (x) = \theta_ {0} (x - \beta_ {0}) p _ {0} (x), \tag {22.6b}
$$

where $\theta_{j} \neq 0$ for all $j$ . Note that in this chapter $\gamma_{i}$ denotes a constant in the recurrence relation and not $iu / (1 - iu)$ as elsewhere in the book. The latter notation is not used in this chapter.

The algorithms exploit the connection with interpolation. Denote by $r(i) \geq 0$ the smallest integer for which $\alpha_{r(i)} = \alpha_{r(i) + 1} = \dots = \alpha_i$ . Considering first the dual system $P^T a = f$ , we note that

$$
\psi (x) = \sum_ {i = 0} ^ {n} a _ {i} p _ {i} (x) \tag {22.7}
$$

satisfies

$$
\psi^ {(i - r (i))} (\alpha_ {i}) = f _ {i}, \quad i = 0: n.
$$

Thus $\psi$ is a Hermite interpolating polynomial for the data $\{\alpha_i, f_i\}$ , and our task is to obtain its representation in terms of the basis $\{p_i(x)\}_{i=0}^n$ . As a first step we construct the divided difference form of $\psi$ ,

$$
\psi (x) = \sum_ {i = 0} ^ {n} c _ {i} \prod_ {j = 0} ^ {i - 1} \left(x - \alpha_ {j}\right). \tag {22.8}
$$

The (confluent) divided differences $c_{i} = f[\alpha_{0},\alpha_{1},\ldots ,\alpha_{i}]$ may be generated using the recurrence relation

$$
f \left[ \alpha_ {j - k - 1}, \dots , \alpha_ {j} \right] = \left\{ \begin{array}{l l} \frac {f \left[ \alpha_ {j - k} , \dots , \alpha_ {j} \right] - f \left[ \alpha_ {j - k - 1} , \dots , \alpha_ {j - 1} \right]}{\alpha_ {j} - \alpha_ {j - k - 1}}, & \alpha_ {j} \neq \alpha_ {j - k - 1}, \\ \frac {f _ {r (j) + k + 1}}{(k + 1) !}, & \alpha_ {j} = \alpha_ {j - k - 1}. \end{array} \right. \tag {22.9}
$$

Now we need to generate the $a_{i}$ in (22.7) from the $c_{i}$ in (22.8). The idea is to expand (22.8) using nested multiplication and use the recurrence relations (22.6) to express the results as a linear combination of the $p_j$ . Define

$$
q _ {n} (x) = c _ {n}, \tag {22.10}
$$

$$
q _ {k} (x) = \left(x - \alpha_ {k}\right) q _ {k + 1} (x) + c _ {k}, \quad k = n - 1: - 1: 0, \tag {22.11}
$$

from which $q_0(x) = \psi (x)$ . Let

$$
q _ {k} (x) = \sum_ {j = 0} ^ {n - k} a _ {k + j} ^ {(k)} p _ {j} (x). \tag {22.12}
$$

To obtain recurrences for the coefficients $a_j^{(k)}$ we expand the right-hand side of (22.11), giving

$$
q _ {k} (x) = \left(x - \alpha_ {k}\right) \sum_ {j = 0} ^ {n - k - 1} a _ {k + j + 1} ^ {(k + 1)} p _ {j} (x) + c _ {k}.
$$

Using the relations, from (22.6),

$$
x p _ {0} (x) = \frac {1}{\theta_ {0}} p _ {1} (x) + \beta_ {0},
$$

$$
x p _ {j} (x) = \frac {1}{\theta_ {j}} \left(p _ {j + 1} (x) + \gamma_ {j} p _ {j - 1} (x)\right) + \beta_ {j} p _ {j} (x), \quad j \geq 1,
$$

we obtain, for $k = 0: n - 2$ ,

$$
\begin{array}{l} q _ {k} (x) = a _ {k + 1} ^ {(k + 1)} \left(\frac {1}{\theta_ {0}} p _ {1} (x) + \beta_ {0}\right) \\ + \sum_ {j = 1} ^ {n - k - 1} a _ {k + j + 1} ^ {(k + 1)} \left(\frac {1}{\theta_ {j}} \left(p _ {j + 1} (x) + \gamma_ {j} p _ {j - 1} (x)\right) + \beta_ {j} p _ {j} (x)\right) \\ - \alpha_ {k} \sum_ {j = 0} ^ {n - k - 1} a _ {k + j + 1} ^ {(k + 1)} p _ {j} (x) + c _ {k} \\ = c _ {k} + (\beta_ {0} - \alpha_ {k}) a _ {k + 1} ^ {(k + 1)} + \frac {\gamma_ {1}}{\theta_ {1}} a _ {k + 2} ^ {(k + 1)} \\ + \sum_ {j = 1} ^ {n - k - 2} \left(\frac {1}{\theta_ {j - 1}} a _ {k + j} ^ {(k + 1)} + (\beta_ {j} - \alpha_ {k}) a _ {k + j + 1} ^ {(k + 1)} + \frac {\gamma_ {j + 1}}{\theta_ {j + 1}} a _ {k + j + 2} ^ {(k + 1)}\right) p _ {j} (x) \\ \end{array}
$$

$$
\begin{array}{l} + \left(\frac {1}{\theta_ {n - k - 2}} a _ {n - 1} ^ {(k + 1)} + (\beta_ {n - k - 1} - \alpha_ {k}) a _ {n} ^ {(k + 1)}\right) p _ {n - k - 1} (x) \\ + \frac {1}{\theta_ {n - k - 1}} a _ {n} ^ {(k + 1)} p _ {n - k} (x), \tag {22.13} \\ \end{array}
$$

in which the empty summation is defined to be zero. For the special case $k = n - 1$ we have

$$
q _ {n - 1} (x) = c _ {n - 1} + \left(\beta_ {0} - \alpha_ {n - 1}\right) a _ {n} ^ {(n)} + \frac {1}{\theta_ {0}} a _ {n} ^ {(n)} p _ {1} (x). \tag {22.14}
$$

Recurrences for the coefficients $a_{j}^{(k)}$ , $j = k$ : $n$ , in terms of $a_{j}^{(k + 1)}$ , $j = k + 1$ : $n$ , follow immediately by comparing (22.12) with (22.13) and (22.14).

In the following algorithm, stage I computes the confluent divided differences and stage II implements the recurrences derived above.

Algorithm 22.2 (dual, $P^T a = f$ ). Given parameters $\{\theta_j, \beta_j, \gamma_j\}_{j=0}^{n-1}$ , a vector $f$ and points $\alpha(0:n) \in \mathbb{C}^{n+1}$ satisfying (22.5), this algorithm solves the dual confluent Vandermonde-like system $P^T a = f$ .

% Stage I:

Set $c = f$

for $k = 0$ : $n - 1$

$$
c l a s t = c _ {k}
$$

for $j = k + 1:n$

$$
\begin{array}{l} i f \alpha_ {j} = \alpha_ {j - k - 1} t h e n \\ c _ {j} = c _ {j} / (k + 1) \\ \end{array}
$$

else

$$
\begin{array}{l} t e m p = c _ {j} \\ c _ {j} = \left(c _ {j} - c l a s t\right) / \left(\alpha_ {j} - \alpha_ {j - k - 1}\right) \\ c l a s t = t e m p \\ \end{array}
$$

end

end

end

% Stage II:

Set $a = c$

$$
a _ {n - 1} = a _ {n - 1} + \left(\beta_ {0} - \alpha_ {n - 1}\right) a _ {n}
$$

$$
a _ {n} = a _ {n} / \theta_ {0}
$$

for $k = n - 2: -1:0$

$$
a _ {k} = a _ {k} + \left(\beta_ {0} - \alpha_ {k}\right) a _ {k + 1} + \left(\gamma_ {1} / \theta_ {1}\right) a _ {k + 2}
$$

for $j = 1$ : $n - k - 2$

$$
a _ {k + j} = a _ {k + j} / \theta_ {j - 1} + (\beta_ {j} - \alpha_ {k}) a _ {k + j + 1} + (\gamma_ {j + 1} / \theta_ {j + 1}) a _ {k + j + 2}
$$

end

$$
a _ {n - 1} = a _ {n - 1} / \theta_ {n - k - 2} + (\beta_ {n - k - 1} - \alpha_ {k}) a _ {n}
$$

$$
a _ {n} = a _ {n} / \theta_ {n - k - 1}
$$

end

Assuming that the values $\gamma_j / \theta_j$ are given (note that $\gamma_j$ appears only in the terms $\gamma_j / \theta_j$ ), the computational cost of Algorithm 22.2 is at most $9n^2 / 2$ flops.

Table 22.2. Parameters in the three-term recurrence (22.6).   

<table><tr><td>Polynomial</td><td>θj</td><td>βj</td><td>γj</td><td></td></tr><tr><td>Monomials</td><td>1</td><td>0</td><td>0</td><td></td></tr><tr><td>Chebyshev</td><td>2*</td><td>0</td><td>1</td><td>*θ0=1</td></tr><tr><td>Legendre*</td><td>2j+1/j+1</td><td>0</td><td>j/j+1</td><td>*pj(1) ≈ 1</td></tr><tr><td>Hermite</td><td>2</td><td>0</td><td>2j</td><td></td></tr><tr><td>Laguerre</td><td>-1/j+1</td><td>2j+1</td><td>j/j+1</td><td></td></tr></table>

The vectors $c$ and $a$ have been used for clarity; in fact both can be replaced by $f$ , so that the right-hand side is transformed into the solution without using any extra storage.

Values of $\theta_{j},\beta_{j},\gamma_{j}$ for some polynomials of interest are collected in Table 22.2.

The key to deriving a corresponding algorithm for solving the primal system is to recognize that Algorithm 22.2 implicitly computes a factorization of $P^{-T}$ into the product of $2n$ triangular matrices. In the rest of this chapter we adopt the convention that the subscripts of all vectors and matrices run from 0 to $n$ . In stage I, letting $c^{(k)}$ denote the vector $c$ at the start of the $k$ th iteration of the outer loop, we have

$$
c ^ {(0)} = f, \quad c ^ {(k + 1)} = L _ {k} c ^ {(k)}, \quad k = 0: n - 1. \tag {22.15}
$$

The matrix $L_{k}$ is lower triangular and agrees with the identity matrix in rows 0 to $k$ . The remaining rows can be described, for $k + 1 \leq j \leq n$ , by

$$
e _ {j} ^ {T} L _ {k} = \left\{ \begin{array}{l l} e _ {j} ^ {T} / (k + 1), & \text {i f} \alpha_ {j} = \alpha_ {j - k - 1}, \\ (e _ {j} ^ {T} - e _ {s} ^ {T}) / (\alpha_ {j} - \alpha_ {j - k - 1}), & \text {s o m e s <   j , o t h e r w i s e}, \end{array} \right.
$$

where $e_j$ is column $j$ of the identity matrix. Similarly, stage II can be expressed as

$$
a ^ {(n)} = c ^ {(n)}, \quad a ^ {(k)} = U _ {k} a ^ {(k + 1)}, \quad k = n - 1: - 1: 0. \tag {22.16}
$$

The matrix $U_{k}$ is upper triangular, it agrees with the identity matrix in rows 0 to $k - 1$ , and it has zeros everywhere above the first two superdiagonals.

From (22.15) and (22.16) we see that the overall effect of Algorithm 22.2 is to evaluate, step-by-step, the product

$$
a = U _ {0} \dots U _ {n - 1} L _ {n - 1} \dots L _ {0} f \equiv P ^ {- T} f. \tag {22.17}
$$

Taking the transpose of this product we obtain a representation of $P^{-1}$ , from which it is easy to write down an algorithm for computing $x = P^{-1}b$ .

Algorithm 22.3 (primal, $Px = b$ ). Given parameters $\{\theta_j,\beta_j,\gamma_j\}_{j = 0}^{n - 1}$ , a vector $b$ , and points $\alpha (0:n)\in \mathbb{C}^{n + 1}$ satisfying (22.5), this algorithm solves the primal confluent Vandermonde-like system $Px = b$ .

% Stage I:

Set $d = b$

for $k = 0:n - 2$

for $j = n - k: - 1:2$

$$
d _ {k + j} = \left(\gamma_ {j - 1} / \theta_ {j - 1}\right) d _ {k + j - 2} + \left(\beta_ {j - 1} - \alpha_ {k}\right) d _ {k + j - 1} + d _ {k + j} / \theta_ {j - 1}
$$

end

$$
d _ {k + 1} = \left(\beta_ {0} - \alpha_ {k}\right) d _ {k} + d _ {k + 1} / \theta_ {0}
$$

end

$$
d _ {n} = \left(\beta_ {0} - \alpha_ {n - 1}\right) d _ {n - 1} + d _ {n} / \theta_ {0}
$$

% Stage II:

Set $x = d$

for $k = n - 1: -1:0$

$xlast = 0$

for $j = n: -1: k + 1$

if $\alpha_{j} = \alpha_{j - k - 1}$ then

$$
x _ {j} = x _ {j} / (k + 1)
$$

else

$$
t e m p = x _ {j} / \left(\alpha_ {j} - \alpha_ {j - k - 1}\right)
$$

$x_{j} = \text{temp} - x\text{last}$

$xlast = temp$

end

end

$$
x _ {k} = x _ {k} - \text {x l a s t}
$$

end

Algorithm 22.3 has, by construction, the same operation count as Algorithm 22.2.

# 22.3. Stability

Algorithms 22.2 and 22.3 have interesting stability properties. Depending on the problem parameters, the algorithms can range from being very stable (in either a backward or forward sense) to very unstable.

When the $p_i$ are the monomials and the points $\alpha_i$ are distinct, the algorithms reduce to those of Björck and Pereyra [133, 1970]. Björck and Pereyra found that for the system $Vx = b$ with $\alpha_i = 1 / (i + 3)$ , $b_i = 2^{-i}$ , $n = 9$ , and on a computer with $u \approx 10^{-16}$ ,

$$
\kappa_ {\infty} (V) = 9 \times 1 0 ^ {1 3}, \quad \max  _ {i} \frac {| x _ {i} - \widehat {x} _ {i} |}{| x _ {i} |} = 5 u.
$$

Thus the computed solution has a tiny componentwise relative error, despite the extreme ill condition of $V$ . Björck and Pereyra comment "It seems as if at least some problems connected with Vandermonde systems, which traditionally have been considered too ill-conditioned to be attacked, actually can be solved with good precision." This high accuracy can be explained with the aid of the error analysis below.

The analysis can be kept quite short by exploiting the interpretation of the algorithms in terms of matrix-vector products. Because of the inherent duality between Algorithms 22.2 and 22.3, any result for one has an analogue for the other, so we will consider only Algorithm 22.2.

# 22.3.1. Forward Error

Theorem 22.4. If no underflows or overflows are encountered then Algorithm 22.2 runs to completion and the computed solution $\hat{a}$ satisfies

$$
\left| a - \widehat {a} \right| \leq c (n, u) \left| U _ {0} \right| \dots \left| U _ {n - 1} \right| \left| L _ {n - 1} \right| \dots \left| L _ {0} \right| | f |, \tag {22.18}
$$

where $c(n, u) \coloneqq (1 + u)^{7n} - 1 = 7nu + O(u^2)$ .

Proof. First, note that Algorithm 22.2 must succeed in the absence of underflow and overflow, because division by zero cannot occur.

The analysis of the computation of the $c^{(k)}$ vectors is exactly the same as that for the nonconfluent divided differences in §5.3 (see (5.9) and (5.10)). However, we obtain a slightly cleaner error bound by dropping the $\gamma_{k}$ notation and instead writing

$$
\widehat {c} ^ {(k + 1)} = \left(L _ {k} + \Delta L _ {k}\right) \widehat {c} ^ {(k)}, \quad | \Delta L _ {k} | \leq [ (1 + u) ^ {3} - 1 ] | L _ {k} |. \tag {22.19}
$$

Turning to the equations (22.16), we can regard the multiplication $a^{(k)} = U_k a^{(k+1)}$ as comprising a sequence of three-term inner products. Analysing these in standard fashion we arrive at the equation

$$
\widehat {a} ^ {(k)} = \left(U _ {k} + \Delta U _ {k}\right) \widehat {a} ^ {(k + 1)}, \quad | \Delta U _ {k} | \leq [ (1 + u) ^ {4} - 1 ] | U _ {k} |, \tag {22.20}
$$

where we have taken into account the rounding errors in forming $u_{i,i+1}^{(k)} = \beta_j - \alpha_k$ and $u_{i,i+2}^{(k)} = \gamma_{j+1} / \theta_{j+1}$ ( $i = k + j$ ).

Since $\widehat{c}^{(0)} = f$ , and $\widehat{a} = \widehat{a}^{(0)}$ , (22.19) and (22.20) imply that

$$
\widehat {a} = \left(U _ {0} + \Delta U _ {0}\right) \dots \left(U _ {n - 1} + \Delta U _ {n - 1}\right) \left(L _ {n - 1} + \Delta L _ {n - 1}\right) \dots \left(L _ {0} + \Delta L _ {0}\right) f. \tag {22.21}
$$

Applying Lemma 3.8 to (22.21) and using (22.17), we obtain the desired bound for the forward error. $\square$

The product $|U_0| \ldots |U_{n-1}| |L_{n-1}| \ldots |L_0|$ in (22.18) is an upper bound for $|U_0 \ldots U_{n-1} L_{n-1} \ldots L_0| = |P^{-T}|$ and is equal to it when there is no subtractive cancellation in the latter product. To gain insight, suppose the points are distinct and consider the case $n = 3$ . We have

$$
\begin{array}{l} P ^ {- T} = U _ {0} U _ {1} U _ {2} L _ {2} L _ {1} L _ {0} \\ \equiv \left[ \begin{array}{c c c c} 1 & \beta_ {0} - \alpha_ {0} & \gamma_ {1} / \theta_ {1} & 0 \\ & \theta_ {0} ^ {- 1} & \beta_ {1} - \alpha_ {0} & \gamma_ {2} / \theta_ {2} \\ & & \theta_ {1} ^ {- 1} & \beta_ {2} - \alpha_ {0} \\ & & & \theta_ {2} ^ {- 1} \end{array} \right] \left[ \begin{array}{c c c c} 1 & 0 & 0 & 0 \\ & 1 & \beta_ {0} - \alpha_ {1} & \gamma_ {1} / \theta_ {1} \\ & & \theta_ {0} ^ {- 1} & \beta_ {1} - \alpha_ {1} \\ & & & \theta_ {1} ^ {- 1} \end{array} \right] \\ \times \left[ \begin{array}{c c c c} 1 & 0 & 0 & 0 \\ & 1 & 0 & 0 \\ & & 1 & \beta_ {0} - \alpha_ {2} \\ & & & \theta_ {0} ^ {- 1} \end{array} \right] \left[ \begin{array}{c c c c} 1 & & & \\ 0 & 1 & & \\ 0 & 0 & 1 & \\ 0 & 0 & \frac {- 1}{\alpha_ {3} - \alpha_ {0}} & \frac {1}{\alpha_ {3} - \alpha_ {0}} \end{array} \right] \\ \times \left[ \begin{array}{c c c c} 1 & & & \\ 0 & 1 & & \\ 0 & \frac {- 1}{\alpha_ {2} - \alpha_ {0}} & \frac {1}{\alpha_ {2} - \alpha_ {0}} & \\ 0 & 0 & \frac {- 1}{\alpha_ {3} - \alpha_ {1}} & \frac {1}{\alpha_ {3} - \alpha_ {1}} \end{array} \right] \\ \end{array}
$$

$$
\times \left[ \begin{array}{c c c c} 1 & & & \\ \frac {- 1}{\alpha_ {1} - \alpha_ {0}} & \frac {1}{\alpha_ {1} - \alpha_ {0}} & & \\ 0 & \frac {- 1}{\alpha_ {2} - \alpha_ {1}} & \frac {1}{\alpha_ {2} - \alpha_ {1}} & \\ 0 & 0 & \frac {- 1}{\alpha_ {3} - \alpha_ {2}} & \frac {1}{\alpha_ {3} - \alpha_ {2}} \end{array} \right]. \tag {22.22}
$$

There is no subtractive cancellation in this product as long as each matrix has the alternating (checkerboard) sign pattern defined, for $A = (a_{ij})$ , by $(-1)^{i+j} a_{ij} \geq 0$ . This sign pattern holds for the matrices $L_i$ if the points $\alpha_i$ are arranged in increasing order. The matrices $U_i$ have the required sign pattern provided that (in general)

$$
\theta_ {i} > 0, \quad \gamma_ {i} \geq 0 \quad \text {f o r a l l} i, \quad \text {a n d} \quad \beta_ {i} - \alpha_ {k} \leq 0 \quad \text {f o r a l l} i + k \leq n - 1.
$$

In view of Table 22.2 we have the following result.

Corollary 22.5. If $0 \leq \alpha_0 < \alpha_1 < \dots < \alpha_n$ then for the monomials, or the Chebyshev, Legendre, or Hermite polynomials,

$$
| a - \widehat {a} | \leq c (n, u) | P ^ {- T} | | f |. \quad \square
$$

Corollary 22.5 explains the high accuracy observed by Björck and Pereyra. Note that if

$$
| P ^ {- T} | | f | \leq t _ {n} | P ^ {- T} f | = t _ {n} | a |
$$

then, under the conditions of the corollary, $|\widehat{a} - a| \leq c(n,u)t_n|a|$ , which shows that the componentwise relative error is bounded by $c(n,u)t_n$ . For the problem of Björck and Pereyra it can be shown that $t_n \approx n^4 / 24$ . Another factor contributing to the high accuracy in this problem is that many of the subtractions $\alpha_j - \alpha_{j-k-1} = 1/(j+3) - 1/(j-k+2)$ are performed exactly, in view of Theorem 2.5.

Note that under the conditions of the corollary $P^{-T}$ has the alternating sign pattern, since each of its factors does. Thus if $(-1)^{i}f_{i}\geq 0$ then $t_n = 1$ , and the corollary implies that $\widehat{a}$ is accurate essentially to full machine precision, independent of the condition number $\kappa_{\infty}(P)$ . In particular, taking $f$ to be a column of the identity matrix shows that we can compute the inverse of $P$ to high relative accuracy, independent of its condition number.

# 22.3.2. Residual

Next we look at the residual, $r = f - P^T\widehat{a}$ . Rewriting (22.21),

$$
f = \left(L _ {0} + \Delta L _ {0}\right) ^ {- 1} \dots \left(L _ {n - 1} + \Delta L _ {n - 1}\right) ^ {- 1} \left(U _ {n - 1} + \Delta U _ {n - 1}\right) ^ {- 1} \dots \left(U _ {0} + \Delta U _ {0}\right) ^ {- 1} \widehat {a}. \tag {22.23}
$$

From the proof of Theorem 22.4 and the relation (5.9) it is easy to show that

$$
\left(L _ {k} + \Delta L _ {k}\right) ^ {- 1} = L _ {k} ^ {- 1} + E _ {k}, \quad | E _ {k} | \leq \left[ (1 - u) ^ {- 3} - 1 \right] | L _ {k} ^ {- 1} |.
$$

Strictly, an analogous bound for $(U_k + \Delta U_k)^{-1}$ does not hold, since $\Delta U_k$ cannot be expressed in the form of a diagonal matrix times $U_k$ . However, it seems reasonable to make a simplifying assumption that such a bound is valid, say

$$
\left(U _ {k} + \Delta U _ {k}\right) ^ {- 1} = U _ {k} ^ {- 1} + F _ {k}, \quad | F _ {k} | \leq c (n, u) \left| U _ {k} ^ {- 1} \right|. \tag {22.24}
$$

Then, writing (22.23) as

$$
f = \left(L _ {0} ^ {- 1} + E _ {0}\right) \dots \left(L _ {n - 1} ^ {- 1} + E _ {n - 1}\right) \left(U _ {n - 1} ^ {- 1} + F _ {n - 1}\right) \dots \left(U _ {0} ^ {- 1} + F _ {0}\right) \widehat {a}
$$

and invoking Lemma 3.8, we obtain the following result.

Theorem 22.6. Under the assumption (22.24), the residual of the computed solution $\widehat{a}$ from Algorithm 22.2 is bounded by

$$
\left| f - P ^ {T} \widehat {a} \right| \leq d (n, u) \left| L _ {0} ^ {- 1} \right| \dots \left| L _ {n - 1} ^ {- 1} \right| \left| U _ {n - 1} ^ {- 1} \right| \dots \left| U _ {0} ^ {- 1} \right| | \widehat {a} |, \tag {22.25}
$$

where $d(n,u)\coloneqq (1 + c(n,u))^n (1 - u)^{-3n} - 1 = n(c(n,u) + 3u) + O(u^2)$

We now specialize to the monomials, for which $L_{i}$ and $U_{i}$ are bidiagonal. Assumption (22.24) can be shown to hold with $c(n,u) = (n + 1)u + O(u^2)$ ; see Problem 22.8. For distinct, nonnegative points arranged in increasing order the inverses of $L_{i}$ and $U_{i}$ have nonnegative elements and, since $P^{T} = L_{0}^{-1}\ldots L_{n - 1}^{-1}U_{n - 1}^{-1}\ldots U_{0}^{-1}$ , we obtain from (22.25) the following pleasing result, which guarantees a tiny componentwise relative backward error.

Corollary 22.7. Let $0 \leq \alpha_0 < \alpha_1 < \dots < \alpha_n$ , and consider Algorithm 22.2 for the monomials. The computed solution $\hat{a}$ satisfies

$$
\left| f - P ^ {T} \widehat {a} \right| \leq \left(n (n + 4) u + O \left(u ^ {2}\right)\right) \left| P ^ {T} | | \widehat {a} | \right.. \quad \square
$$

# 22.3.3. Dealing with Instability

The potential instability of Algorithm 22.2 is illustrated by the following example. Take the Chebyshev polynomials $T_{i}$ with the points $\alpha_{i} = \cos (i\pi /n)$ (the extrema of $T_{n}$ ), and define the right-hand side by $f_{i} = (-1)^{i}$ . The exact solution to $P^T a = f$ is the last column of the identity matrix. Relative errors and residuals are shown in Table 22.3 ( $u \approx 10^{-16}$ ). Even though $\kappa_{2}(P) \leq 2$ for all $n$ (see Problem 22.7), the forward errors and relative residuals are large and grow with $n$ . The reason for the instability is that there are large intermediate numbers in the algorithm (at the start of stage II for $n = 40$ , $\| c\|_{\infty}$ is of order $10^{15}$ ); hence severe cancellation is necessary to produce the final answer of order 1. Looked at another way, the factorization of $P^T$ used by the algorithm is unstable because it is very sensitive to perturbations in the factors.

How can we overcome this instability? There are two possibilities: prevention and cure. The only means at our disposal for preventing instability is to reorder the points $\alpha_{i}$ . The ordering is arbitrary subject to condition (22.5) being satisfied. Recall that the algorithms construct an $LU$ factorization of $P^T$ in factored form, and note that permuting the rows of $P^T$ is equivalent to reordering the points $\alpha_{i}$ . A reasonable approach is therefore to take whatever ordering of the points would be produced by GEPP applied to $P^T$ . Since the diagonal elements of $U$ in $P^T = LU$ have the form

$$
u _ {i i} = h _ {i} \prod_ {j = 0} ^ {i - 1} \left(\alpha_ {i} - \alpha_ {j}\right), \quad i = 0: n,
$$

Table 22.3. Results for dual Chebyshev-Vandermonde-like system.   

<table><tr><td>n</td><td>10</td><td>20</td><td>30</td><td>40</td></tr><tr><td>||a-ˆa||∞/||a||∞</td><td>2.5 × 10-12</td><td>6.3 × 10-7</td><td>4.7 × 10-2</td><td>1.8 × 103</td></tr><tr><td>||f-P^Tˆa||∞/||P||∞||ˆa||∞ + ||f||∞</td><td>6.0 × 10-13</td><td>1.1 × 10-7</td><td>5.3 × 10-3</td><td>8.3 × 10-2</td></tr></table>

where $h_i$ depends only on the $\theta_i$ , and since partial pivoting maximizes the pivot at each stage, this ordering of the $\alpha_i$ can be computed at the start of the algorithm in $n^2$ flops (see Problem 22.9). This ordering is essentially the Leja ordering (5.13) (the difference is that partial pivoting leaves $\alpha_0$ unchanged).

To attempt to cure observed instability we can use iterative refinement in fixed precision. Ordinarily, residual computation for linear equations is trivial, but in this context the coefficient matrix is not given explicitly and computing the residual turns out to be conceptually almost as difficult, and computationally as expensive, as solving the linear system!

To compute the residual for the dual system we need a means for evaluating $\psi(t)$ in (22.7) and its first $k \leq n$ derivatives, where $k = \max_{i} (i - r(i))$ is the order of fluency. Since the polynomials $p_j$ satisfy a three-term recurrence relation we can use an extension of the Clenshaw recurrence formula (which evaluates $\psi$ but not its derivatives). The following algorithm implements the appropriate recurrences, which are given by Smith [1050, 1965] (see Problem 22.10).

Algorithm 22.8 (extended Clenshaw recurrence). This algorithm computes the $k + 1$ values $y_{j} = \psi^{(j)}(x)$ , $0 \leq j \leq k$ , where $\psi$ is given by (22.7) and $k \leq n$ . It uses a work vector $z$ of order $k$ .

Set $y(0:k) = z(0:k) = 0$ $y_{0} = a_{n}$ for $j = n - 1: - 1:0$ $\begin{array}{l}temp = y_0\\ y_0 = \theta_j(x - \beta_j)y_0 - \gamma_{j + 1}z_0 + a_j\\ z_0 = temp\\ \mathrm{for~}i = 1:\min (k,n - j)\\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad z_i = temp\\ \mathrm{end}\\ \mathrm{end}\\ m = 1\\ \mathrm{for~}i = 2:k\\ m = m*i\\ y_i = m*y_i\\ \mathrm{end}\\ \end{array}$

Computing the residual using Algorithm 22.8 costs between $3n^2$ flops (for full confluency) and $6n^2$ flops (for the nonconfluent case); recall that Algorithm 22.2 costs at most $9n^2 / 2$ flops!

The use of iterative refinement can be justified with the aid of Theorem 12.3. For (confluent) Vandermonde matrices, the residuals are formed using Horner's rule and (12.9) holds in view of (5.3) and (5.7). Hence for standard Vandermonde matrices, Theorem 12.3 leads to an asymptotic componentwise backward stability result. A complete error analysis of Algorithm 22.8 is not available for (confluent) Vandermonde-like matrices, but it is easy to see that (12.9) will not always hold. Nevertheless it is clear that a normwise bound can be obtained (see Oliver [901, 1977] for the special case of the Chebyshev polynomials) and hence an asymptotic normwise stability result can be deduced from Theorem 12.3. Thus there is theoretical backing for the use of iterative refinement with Algorithm 22.8.

Numerical experiments using Algorithm 22.8 in conjunction with the partial pivoting reordering and fixed precision iterative refinement show that both techniques are effective means for stabilizing the algorithms, but that iterative refinement is likely to fail once the instability is sufficiently severe. Because of its lower cost, the reordering approach is preferable.

Two heuristics are worth noting. Consider a (confluent) Vandermonde-like system $P\mathbf{x} = \mathbf{b}$ . Heuristic 1: it is systems with a large normed solution $(\| x \| \approx \| P^{-1} \| \| b \|)$ that are solved to high accuracy by the fast algorithms. To produce a large solution the algorithms must sustain little cancellation, and the error analysis shows that cancellation is the main cause of instability. Heuristic 2: GEPP is unable to solve accurately Vandermonde systems with a very large normed solution $(\| x \| \gg u^{-1} \| b \| / \| P \|)$ . The pivots for GEPP will tend to satisfy $|u_{ii}| \gtrsim u \| P \|$ , so that the computed solution will tend to satisfy $\| \widehat{x} \| \leq u^{-1} \| b \| / \| P \|$ . A consequence of these two heuristics is that for Vandermonde(-like) systems with a very large-normed solution the fast algorithms will be much more accurate (but no more backward stable) than GEPP. However, we should be suspicious of any framework in which such systems arise; although the solution vector may be obtained accurately (barring overflow), subsequent computations with numbers of such a wide dynamic range will probably themselves be unstable.

# 22.4. Notes and References

The formulae (22.1) and (22.2), and inversion methods based on these formulae, have been discovered independently by many authors. Traub [1150, 1966, §14] gives a short historical survey, his earliest reference being a 1932 book by Kowalewski. There does not appear to be any published error analysis for Algorithm 22.1 (see Problem 22.3). There is little justification for using the output of the algorithm to solve the primal or dual linear system, as is done in [953, 1992, §2.8]; Algorithms 22.2 and 22.3 are more efficient and almost certainly at least as stable. Calvetti and Reichel [198, 1993] generalize Algorithm 22.1 to Vandermonde-like matrices, but they do not present any error analysis. Gohberg and Olshevsky [495, 1994] give another $O(n^{2})$ flops algorithm for inverting a Chebyshev-Vandermonde matrix.

The standard condition number $\kappa(V)$ is not an appropriate measure of sensi

tivity when only the points $\alpha_{i}$ are perturbed, because it does not reflect the special structure of the perturbations. Appropriate condition numbers were first derived by Higham [581, 1987] and are comprehensively investigated by Bartels and D. J. Higham [86, 1992]; see Problem 22.11.

Structured backward errors for Vandermonde systems are defined and investigated by Sun [1109, 1998], who obtains upper and lower bounds.

Methods for solving the dual and primal Vandermonde systems have an interesting history. The earliest algorithm was derived by Lyness and Moler [801, 1966] via Neville interpolation; it solves the dual system in $O(n^3)$ flops. The first $O(n^2)$ algorithm was obtained by Ballester and Pereyra [61, 1967]; it computes the LU factors of the Vandermonde matrix and requires $O(n^2)$ elements of storage. Björck and Pereyra [133, 1970] derived the specialization of Algorithms 22.2 and 22.3 to nonconfluent Vandermonde matrices; these algorithms require no storage other than that for the problem data. The algorithms of Björck and Pereyra were generalized by Björck and Elfving to confluent systems [129, 1973], and by Higham to Vandermonde-like systems [584, 1988] and confluent Vandermonde-like systems [595, 1990]. The error analysis in this chapter is based on [595, 1990]. Tang and Golub [1126, 1981] give a block algorithm that requires only real arithmetic to solve a Vandermonde system in which all the points appear in complex conjugate pairs.

Other $O(n^{2})$ algorithms for solving Chebyshev-Vandermonde systems are given by Reichel and Opfer [977, 1991] and Calvetti and Reichel [197, 1992]. The former algorithms are progressive, in that they allow the solution to be updated when a new point $\alpha_{i}$ is added; they generalize progressive algorithms of Björck and Pereyra [133, 1970]. Boros, Kailath, and Olshevsky [151, 1994] use the concept of displacement structure to derive further $O(n^{2})$ algorithms for solving Vandermonde and Chebyshev-Vandermonde systems. No error analysis is given in [151, 1994], [197, 1992], or [977, 1991].

The $O(n^{2})$ complexity of the algorithms mentioned above for solving Vandermonde-like systems is not optimal. Lu [797, 1994], [798, 1995], [799, 1996] derives $O(n\log n\log p)$ flops algorithms, where $p$ is the number of distinct points. The numerical stability and practical efficiency of the algorithms remain to be determined. Bini and Pan [111, 1994] give an $O(n\log^2 n)$ algorithm for solving a dual Vandermonde system that involves solving related Toeplitz and Hankel systems.

Since Vandermonde systems can be solved in less than $O(n^{3})$ flops it is natural to ask whether the $O(mn^{2})$ complexity of QR factorization of an $m \times n$ matrix can be bettered for a Vandermonde matrix. QR factorization algorithms with $O(mn)$ flop counts have been derived by Demeure [305, 1989], [306, 1990], and for Vandermonde-like matrices where the polynomials satisfy a three-term recurrence by Reichel [976, 1991]. No error analysis has been published for these algorithms. Demeure's algorithms are likely to be unstable, because they form the normal equations matrix $V^T V$ .

# Problems

22.1. Derive a modified version of Algorithm 22.1 in which the scale factor $s = q_i(\alpha_i)$ is computed directly as

$$
\prod_{\substack{k = 0\\ k\neq i}}^{n}(\alpha_{i} - \alpha_{k}).
$$

What is the flop count for this version?

22.2. (Calvetti and Reichel [198, 1993]) Generalize Algorithm 22.1 to the inversion of a Vandermonde-like matrix for polynomials that satisfy a three-term recurrence relation.   
22.3. Investigate the stability of Algorithm 22.1 and the modified version of Problem 22.1. (a) Evaluate the left and right residuals of the computed inverses; compare the results with those for GEPP. (b) Show that Algorithm 22.1 always performs subtractions of like-signed numbers and explain the implications for stability. (Does Algorithm 22.1 share the high accuracy properties discussed at the end of §22.3.1?) (c) (RESEARCH PROBLEM) Derive and explore forward error bounds and residual bounds for both algorithms. Extend the analysis to the algorithms of Calvetti and Reichel [198, 1993].   
22.4. By summing (22.1) for $i = 0$ : $n$ , show that $\sum_{i=0}^{n} w_{ij} = \delta_{j0}$ . What does this imply about the sign pattern of $V^{-1}$ ? What is the sum of all the elements of $V^{-1}$ ?   
22.5. Let $T = T(\alpha_0, \alpha_1, \ldots, \alpha_n) = (T_i(\alpha_j))_{i,j=0}^n$ be a Chebyshev-Vandermonde matrix ( $T_j$ is the Chebyshev polynomial of degree $j$ ), with $T^{-1} = (u_{ij})$ . Analogously to (22.1) we have $\sum_{j=0}^{n} u_{ij} T_j(x) = l_i(x)$ . Hence $\sum_{j=0}^{n} w_{ij} x^j = \sum_{j=0}^{n} u_{ij} T_j(x)$ , where $V^{-1} = V(\alpha_0, \alpha_1, \ldots, \alpha_n)^{-1} = (w_{ij})$ . Show that

$$
\sum_ {j = 0} ^ {n} \left| u _ {i j} \right| \leq \sum_ {j = 0} ^ {n} \left| w _ {i j} \right|,
$$

and hence that

$$
\| T ^ {- 1} \| _ {\infty} \leq \| V ^ {- 1} \| _ {\infty}.
$$

(Hint: show that $T = LV$ for a lower triangular matrix $L$ and use the fact that $x^n = \frac{1}{2^{n+1}} \sum_{k=0}^{\lceil n/2 \rceil} \binom{n}{k} T_{n-2k}(x)$ .)

22.6. Show that for a nonconfluent Vandermonde-like matrix $P = (P_{i}(\alpha_{j}))_{i,j=0}^{n}$ , where the $p_i$ satisfy (22.6),

$$
\det  (P) = \prod_ {i = 0} ^ {n - 1} \theta_ {i} ^ {n - i} \prod_ {i > j} (\alpha_ {i} - \alpha_ {j}).
$$

(Hint: study the structure of (22.22).)

22.7. Show that for the Chebyshev-Vandermonde-like matrix $T = T(\alpha_0, \alpha_1, \ldots, \alpha_n)$ ,

1. $\kappa_{2}(T) = \sqrt{2}$ , for $\alpha_{i} = \cos((i + \frac{1}{2})\pi / (n + 1))$ (zeros of $T_{n+1}$ ).   
2. $\kappa_{2}(T)\leq 2$ , for $\alpha_{i} = \cos (i\pi /n)$ (extrema of $T_{n}$

(Hint: use the discrete orthogonality properties of the Chebyshev polynomials; see, e.g., Hamming [545, 1973, pp. 472-473].)

22.8. Let $U \in \mathbb{R}^{n \times n}$ be upper bidiagonal and let $\Delta U$ be a perturbation such that $\Delta u_{ij} = \delta_{ij} u_{ij}$ . Show that

$$
\left((U + \Delta U) ^ {- 1} - U ^ {- 1}\right) _ {i j} = \frac {1}{1 + \delta_ {j j}} \left(\prod_ {p = i} ^ {j - 1} \frac {- (1 + \delta_ {p , p + 1})}{1 + \delta_ {p p}}\right) (U ^ {- 1}) _ {i j}.
$$

Interpret this equality. Deduce that for $U_{k} + \Delta U_{k}$ in (22.24) we have

$$
\left(U _ {k} + \varDelta U _ {k}\right) ^ {- 1} = U _ {k} ^ {- 1} + F _ {k}, \qquad | F _ {k} | \leq \frac {(n + 1) u}{1 - (n + 1) u} | U _ {k} ^ {- 1} |.
$$

22.9. Derive an $O(n^{2})$ flops algorithm that reorders the distinct points $\alpha_{0}, \alpha_{1}, \ldots, \alpha_{n} \in \mathbb{C}$ according to the same permutation that would be produced by GEPP applied to $P^{T}(\alpha_{0}, \alpha_{1}, \ldots, \alpha_{n})$ . (Cf. Problem 5.4.) Can your algorithm ever produce the increasing ordering?

22.10. Derive Algorithm 22.8 by differentiating repeatedly the original Clenshaw recurrence (which is Algorithm 22.8 with $k = 0$ ) and rescaling so as to consign factorial terms to a cleanup loop at the end. Derive an algorithm for computing the residual for the primal system in a similar way, using recurrences obtained by differentiating (22.6).

22.11. (Higham [581, 1987]) A structured condition number for the primal Vandermonde system $Vx = b$ , where $V = V(\alpha_0, \alpha_1, \ldots, \alpha_n)$ , can be defined by

$$
\begin{array}{l} \operatorname {c o n d} (V) := \lim  _ {\epsilon \rightarrow 0} \sup  \left\{\frac {\| \Delta x \| _ {\infty}}{\epsilon \| x \| _ {\infty}}: V (\alpha_ {0} + \Delta \alpha_ {0}, \dots , \alpha_ {n} + \Delta \alpha_ {n}) (x + \Delta x) = b, \right. \\ \left. \left| \Delta \alpha_ {i} \right| \leq \epsilon \mid \alpha_ {i} \right|, \quad i = 0: n \Big \}. \\ \end{array}
$$

Show that

$$
\operatorname {c o n d} (V) = \frac {\left\| \left| V ^ {- 1} \operatorname {d i a g} (0 , 1 , 2 , \dots , n) V \right| \right| _ {\infty}}{\left\| x \right| _ {\infty}},
$$

and derive a corresponding condition number for the dual system $V^T a = f$ .
