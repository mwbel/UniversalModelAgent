# Chapter 9

# LU Factorization and Linear Equations

It appears that Gauss and Doolittle applied the method only to symmetric equations.

More recent authors, for example, Aitken, Banachiewicz, Dwyer, and Crout ...

have emphasized the use of the method, or variations of it,

in connection with non-symmetric problems ...

Banachiewicz ... saw the point ...

that the basic problem is really one of matrix factorization,

or "decomposition" as he called it.

— PAUL S. DWYER, Linear Computations (1951)

Intolerable pivot-growth [with partial pivoting] is a phenomenon that happens

only to numerical analysts who are looking for that phenomenon.

— WILLIAM M. KAHAN, Numerical Linear Algebra (1966)

By 1949 the major components of the

Pilot ACE were complete and undergoing trials ...

During 1951 a programme for solving simultaneous

linear algebraic equations was used for the first time.

26th June, 1951 was a landmark in the history of the machine,

for on that day it first rivalled alternative computing methods

by yielding by 3 p.m. the solution to

a set of 17 equations submitted the same morning.

— MICHAEL WOODGER, The History and Present Use of

Digital Computers at the National Physical Laboratory (1958).

The closer one looks,

the more subtle and remarkable Gaussian elimination appears.

— LLOYD N. TREFETHEN, Three Mysteries of Gaussian Elimination (1985)

# 9.1. Gaussian Elimination and Pivoting Strategies

We begin by giving a traditional description of Gaussian elimination (GE) for solving a linear system $Ax = b$ , where $A \in \mathbb{R}^{n \times n}$ is nonsingular.

The strategy of GE is to reduce a problem we can't solve (a full linear system) to one that we can (a triangular system), using elementary row operations. There are $n - 1$ stages, beginning with $A^{(1)} \coloneqq A$ , $b^{(1)} \coloneqq b$ , and finishing with the upper triangular system $A^{(n)}x = b^{(n)}$ .

At the $k$ th stage we have converted the original system to $A^{(k)}x = b^{(k)}$ , where

$$
A ^ {(k)} = \left[ \begin{array}{c c} A _ {1 1} ^ {(k)} & A _ {1 2} ^ {(k)} \\ 0 & A _ {2 2} ^ {(k)} \end{array} \right],
$$

with $A_{11}^{(k)} \in \mathbb{R}^{(k-1) \times (k-1)}$ upper triangular. The purpose of the $k$ th stage of the elimination is to zero the elements below the diagonal in the $k$ th column of $A^{(k)}$ . This is accomplished by the operations

$$
a _ {i j} ^ {(k + 1)} = a _ {i j} ^ {(k)} - m _ {i k} a _ {k j} ^ {(k)}, \qquad i = k + 1: n, j = k + 1: n,
$$

$$
b _ {i} ^ {(k + 1)} = b _ {i} ^ {(k)} - m _ {i k} b _ {k} ^ {(k)}, \quad i = k + 1: n,
$$

where the multipliers $m_{ik} = a_{ik}^{(k)} / a_{kk}^{(k)}$ , $i = k + 1:n$ . At the end of the $(n - 1)$ st stage we have the upper triangular system $A^{(n)}x = b^{(n)}$ , which is solved by back substitution. For an $n\times n$ matrix, GE requires $2n^3 /3$ flops.

There are two problems with the method as described. First, there is a breakdown with division by zero if $a_{kk}^{(k)} = 0$ . Second, if we are working in finite precision and some multiplier $m_{ik}$ is large, then there is a possible loss of significance: in the subtraction $a_{ij}^{(k)} - m_{ik}a_{kj}^{(k)}$ , low-order digits of $a_{ij}^{(k)}$ could be lost. Losing these digits could correspond to making a relatively large change to the original matrix $A$ . The simplest example of this phenomenon is for the matrix $\left[ \begin{array}{cc}\epsilon & 1\\ 1 & 1 \end{array} \right]$ ; here, $a_{22}^{(2)} = 1 - 1 / \epsilon$ , and $fl(a_{22}^{(2)}) = -1 / \epsilon$ if $\epsilon < u$ , which would be the exact answer if we changed $a_{22}$ from 1 to 0.

These observations motivate the strategy of partial pivoting. At the start of the $k$ th stage, the $k$ th and $r$ th rows are interchanged, where

$$
| a _ {r k} ^ {(k)} | := \max _ {k \leq i \leq n} | a _ {i k} ^ {(k)} |.
$$

Partial pivoting ensures that the multipliers are nicely bounded:

$$
\left| m _ {i k} \right| \leq 1, \quad i = k + 1: n.
$$

A more expensive pivoting strategy, which interchanges both rows and columns, is complete pivoting.

At the start of the $k$ th stage, rows $k$ and $r$ and columns $k$ and $s$ are interchanged, where

$$
|a_{rs}^{(k)}|:= \max_{k\leq i,j\leq n}|a_{ij}^{(k)}|.
$$

Note that this requires $O(n^{3})$ comparisons in total, compared with $O(n^{2})$ for partial pivoting. Because of the searching overhead, and because partial pivoting

![](images/420f9e9f74405f9d93b67b7687f9017a51e2233aff51c306107c73972564d231.jpg)  
Figure 9.1. Illustration of how rook pivoting searches for the first pivot for a particular $6 \times 6$ matrix (with the positive integer entries shown). Each dot denotes a putative pivot that is tested to see if it is the largest in magnitude in both its row and its column.

works so well, complete pivoting is used only in special situations (see the Notes and References).

Also of interest, but much less well known, is the rook pivoting strategy, which chooses at each stage a pivot intermediate in size between the pivots that would be chosen by partial pivoting and complete pivoting. At the start of the $k$ th stage, rows $k$ and $r$ and columns $k$ and $s$ are interchanged, where

$$
| a _ {r s} ^ {(k)} | = \operatorname * {m a x} _ {k \leq i \leq n} | a _ {i s} ^ {(k)} | = \operatorname * {m a x} _ {k \leq j \leq n} | a _ {r j} ^ {(k)} |;
$$

in other words, a pivot is chosen that is the largest in magnitude in both its column (as for partial pivoting) and its row. The pivot search can be coded as follows:

$s_0 = k$ for $p = 1,2,\ldots$ $\begin{array}{l}r_p = \mathrm{row~index~of~first~element~of~max.~modulus~among}\{a_{i,s_{p - 1}}\}_{i = \\ \mathrm{take} a_{r_{p - 1},s_{p - 1}}\mathrm{as~pivot,~quit}\\ \mathrm{end}\\ s_p = \mathrm{col.~index~of~first~element~of~max.~modulus~among}\{a_{r_p,j}\}_{j = k}\\ \mathrm{if}\left|a_{r_p,s_p}\right| = \left|a_{r_p,s_{p - 1}}\right|\mathrm{take}a_{r_p,s_{p - 1}}\mathrm{as~pivot,~quit,~end}\\ \mathrm{end} \end{array}$

The rook pivoting strategy takes its name from the fact that the search for a pivot corresponds to the moves of a rook in chess; see Figure 9.1. Note that in the pivot search, elements previously considered can be skipped; in the following discussion we will assume that this refinement is incorporated, though it may not be worthwhile in practice.

Clearly, the search for a pivot in rook pivoting involves at least twice as many comparisons as for partial pivoting, and if the whole submatrix has to be searched then the number of comparisons is the same as for complete pivoting. Foster [435, 1997, Thm. 5] shows that if the elements $\{a_{ij}^{(k)}\}_{i,j = k}^n$ are independent identically

distributed random variables from any continuous probability distribution then the expected number of comparisons in the pivot search for rook pivoting at stage $k$ is at most $(n - k)e$ (where $e = \exp(1)$ ). If this statistical assumption is satisfied for each $k$ then the overall number of comparisons is bounded by $(n - 1)ne / 2$ , which is of the same order as for partial pivoting $((n - 1)n / 2$ comparisons) and an order of magnitude less than for complete pivoting $(n^3 / 3 + O(n / 2)$ comparisons). Numerical experiments show that the cost of rook pivoting is indeed usually a small multiple of the cost of partial pivoting and significantly less than the cost of complete pivoting (see Figure 9.3). However, rook pivoting can require $O(n^3)$ comparisons, as illustrated by any matrix of the form, illustrated for $n = 4$ ,

$$
\left[ \begin{array}{cccc} \theta_ {1} & \theta_ {2} &  &  \\  & \theta_ {3} & \theta_ {4} &  \\  &  & \theta_ {5} & \theta_ {6} \\  &  &  & \theta_ {7} \end{array} \right], \qquad | \theta_ {1} | <   | \theta_ {2} | <   \dots <   | \theta_ {7} |,
$$

for which $n^3 / 4 + O(n^2)$ comparisons are required.

# 9.2. LU Factorization

Much insight into GE is obtained by expressing it in matrix notation. We can write

$$
A ^ {(k + 1)} = M _ {k} A ^ {(k)} := \left[ \begin{array}{c c c c c c} I _ {k - 1} & & & & & \\ & 1 & & & & \\ & - m _ {k + 1, k} & 1 & & & \\ & - m _ {k + 2, k} & & \ddots & & \\ & \vdots & & & \ddots & \\ & - m _ {n, k} & & & & 1 \end{array} \right] A ^ {(k)}.
$$

The matrix $M_{k}$ can be expressed compactly as $M_{k} = I - m_{k}e_{k}^{T}$ , where $e_{k}$ is the $k$ th unit vector and $e_i^T m_k = 0$ for $i \leq k$ . To invert $M_{k}$ , just flip the signs of the multipliers: $M_{k}^{-1} = I + m_{k}e_{k}^{T}$ . Overall,

$$
M _ {n - 1} M _ {n - 2} \dots M _ {1} A = A ^ {(n)} =: U,
$$

and so

$$
\begin{array}{l} A = M _ {1} ^ {- 1} M _ {2} ^ {- 1} \dots M _ {n - 1} ^ {- 1} U \\ = \left(I + m _ {1} e _ {1} ^ {T}\right) \left(I + m _ {2} e _ {2} ^ {T}\right) \dots \left(I + m _ {n - 1} e _ {n - 1} ^ {T}\right) U \\ = \left(I + \sum_ {i = 1} ^ {n - 1} m _ {i} e _ {i} ^ {T}\right) U \\ = \left[ \begin{array}{c c c c c} 1 & & & & \\ m _ {2 1} & 1 & & & \\ \vdots & m _ {3 2} & \ddots & & \\ \vdots & \vdots & & \ddots & \\ m _ {n 1} & m _ {n 2} & \dots & m _ {n, n - 1} & 1 \end{array} \right] U =: L U. \\ \end{array}
$$

The conclusion is that GE computes an LU factorization of $A$ : $A = LU$ , where $L$ is unit lower triangular and $U$ is upper triangular.

We introduce the shorthand notation $A_{k} \coloneqq A(1:k,1:k)$ .

Theorem 9.1. There exists a unique LU factorization of $A \in \mathbb{R}^{n \times n}$ if and only if $A_k$ is nonsingular for $k = 1:n-1$ . If $A_k$ is singular for some $1 \leq k \leq n-1$ then the factorization may exist, but if so it is not unique.

Proof. Suppose $A_{k}$ is nonsingular for $k = 1:n - 1$ . The existence of an LU factorization can be proved by examining the steps of GE, but a more elegant proof, which also gives uniqueness, can be obtained by an inductive bordering construction. Suppose $A_{k - 1}$ has the unique LU factorization $A_{k - 1} = L_{k - 1}U_{k - 1}$ (this supposition clearly holds for $k - 1 = 1$ ). We look for a factorization

$$
A _ {k} = \left[ \begin{array}{c c} A _ {k - 1} & b \\ c ^ {T} & a _ {k k} \end{array} \right] = \left[ \begin{array}{c c} L _ {k - 1} & 0 \\ l ^ {T} & 1 \end{array} \right] \left[ \begin{array}{c c} U _ {k - 1} & u \\ 0 & u _ {k k} \end{array} \right] =: L _ {k} U _ {k}.
$$

The equations to be satisfied are $L_{k-1}u = b$ , $U_{k-1}^T l = c$ , and $a_{kk} = l^T u + u_{kk}$ . The matrices $L_{k-1}$ and $U_{k-1}$ are nonsingular, since $0 \neq \det(A_{k-1}) = \det(L_{k-1})\det(U_{k-1})$ , so the equations have a unique solution, completing the induction.

We prove the converse, under the assumption that $A$ is nonsingular; for the case $A$ singular see Problem 9.1. Suppose an LU factorization exists. Then $A_{k} = L_{k}U_{k}$ for $k = 1:n$ , which gives

$$
\det  \left(A _ {k}\right) = \det  \left(U _ {k}\right) = u _ {1 1} \dots u _ {k k}. \tag {9.1}
$$

Setting $k = n$ we find that $0 \neq \operatorname{det}(A) = u_{11} \ldots u_{nn}$ , and hence $\operatorname{det}(A_k) = u_{11} \ldots u_{kk} \neq 0, k = 1:n - 1$ .

Examples that illustrate the last part of the theorem are $\left[ \begin{array}{cc}0 & 0\\ 0 & 0 \end{array} \right] = \left[ \begin{array}{cc}1 & 0\\ l & 1 \end{array} \right]\left[ \begin{array}{cc}0 & 0\\ 0 & 0 \end{array} \right]$ , which holds for any $l$ , and $\left[ \begin{array}{cc}0 & 1\\ 1 & 1 \end{array} \right]$ , which does not have an LU factorization.

Visually, the condition of Theorem 9.1 is (for $n = 5$ ) that the indicated submatrices must be nonsingular:

$$
\left[ \begin{array}{c c c c c} \underline {{\times}} & \times & \times & \times & \times \\ \underline {{\times}} & \times & \times & \times & \times \\ \underline {{\times}} & \times & \times & \times & \times \\ \underline {{\times}} & \times & \times & \times & \times \\ \underline {{\times}} & \times & \times & \times & \times \end{array} \right].
$$

From (9.1) follows the expression $u_{kk} = \operatorname*{det}(A_k) / \operatorname*{det}(A_{k-1})$ . In fact, all the elements of $L$ and $U$ can be expressed by determinantal formulae (see, e.g., Gant-macher [453, 1959, p. 35] or Householder [644, 1964, p. 11]):

$$
\begin{array}{l} l _ {i j} = \frac {\det  \left(A ([ 1 : j - 1 , i ] , 1 : j)\right)}{\det  \left(A _ {j}\right)}, \quad i \geq j, (9.2a) \\ u _ {i j} = \frac {\det  \left(A (1 : i , [ 1 : i - 1 , j ])\right)}{\det  \left(A _ {i - 1}\right)}, \quad i \leq j. (9.2b) \\ \end{array}
$$

The effect of partial pivoting is easily seen by considering the case $n = 4$ . We have

$$
\begin{array}{l} U = M _ {3} P _ {3} M _ {2} P _ {2} M _ {1} P _ {1} A, \quad \text {w h e r e} P _ {k} \text {s w a p s r o w s} k, r (r \geq k), \\ = M _ {3} \cdot \underbrace {P _ {3} M _ {2} P _ {3}} \cdot \underbrace {P _ {3} P _ {2} M _ {1} P _ {2} P _ {3}} \cdot \underbrace {P _ {3} P _ {2} P _ {1} A} \\ =: M _ {3} ^ {\prime} M _ {2} ^ {\prime} M _ {1} ^ {\prime} P A, \\ \end{array}
$$

where, for example, $M_1' = P_3P_2(I - m_1e_1^T)P_2P_3 = I - (P_3P_2m_1)e_1^T$ . For $k = 1,2,3$ , $M_k'$ is the same as $M_k$ except the multipliers are interchanged. Hence, for $n = 4$ , GE with partial pivoting (GEPP) applied to $A$ is equivalent to GE without pivoting applied to the row-permutated matrix $PA$ . This conclusion is true for any $n$ : GEPP computes a factorization $PA = LU$ . Similarly, GE with rook pivoting or complete pivoting computes a factorization $PAQ = LU$ , where $P$ and $Q$ are permutation matrices.

Exploitation of the LU factorization streamlines both the error analysis and the practical solution of linear systems. Solution of $Ax = b$ breaks into a factorization phase, $PA = LU$ for partial pivoting ( $O(n^3)$ flops), and a substitution phase, where the triangular systems $Ly = Pb$ , $Ux = y$ are solved ( $O(n^2)$ flops). If more than one system is to be solved with the same coefficient matrix but different right-hand sides, the factorization can be reused, with a consequent saving in work.

Computing an LU factorization $A = LU$ is equivalent to solving the equations

$$
a _ {i j} = \sum_ {r = 1} ^ {\min  (i, j)} l _ {i r} u _ {r j}.
$$

If these nonlinear equations are examined in the right order, they are easily solved. For added generality let $A \in \mathbb{R}^{m \times n}$ ( $m \geq n$ ) and consider an LU factorization with $L \in \mathbb{R}^{m \times n}$ and $U \in \mathbb{R}^{n \times n}$ ( $L$ is lower trapezoidal: $l_{ij} = 0$ for $i < j$ ). Suppose we know the first $k - 1$ columns of $L$ and the first $k - 1$ rows of $U$ . Setting $l_{kk} = 1$ ,

$$
a _ {k j} = l _ {k 1} u _ {1 j} + \dots + l _ {k, k - 1} u _ {k - 1, j} + \boxed {u _ {k j}}, \quad j = k: n, \tag {9.3}
$$

$$
a _ {i k} = l _ {i 1} u _ {1 k} + \dots + \boxed {l _ {i k}} u _ {k k}, \quad i = k + 1: m. \tag {9.4}
$$

We can solve for the boxed elements in the $k$ th row of $U$ and then the $k$ th column of $L$ . This process is called Doolittle's method.

Algorithm 9.2 (Doolittle's method). This algorithm computes an LU factorization $A = LU \in \mathbb{R}^{m \times n}$ , where $m \geq n$ (assuming the factorization exists), by Doolittle's method.

for $k = 1:n$

for $j = k:n$

$(*)$ （20 $u_{kj} = a_{kj} - \sum_{i = 1}^{k - 1}l_{ki}u_{ij}$

end

for $i = k + 1$ : $m$

$(**)$ $l_{ik} = (a_{ik} - \sum_{j = 1}^{k - 1}l_{ij}u_{jk}) / u_{kk}$

end

end

Cost: $n^2 (m - n / 3)$ flops.

Doolittle's method is mathematically equivalent to GE without pivoting, for we have, in (9.3),

$$
a _ {k j} - l _ {k 1} u _ {1 j} - \dots - l _ {k s} u _ {s j} \equiv a _ {k j} ^ {(s + 1)} \quad (j > k), \tag {9.5}
$$

and similarly for (9.4). Had we chosen the normalization $u_{ii} \equiv 1$ , we would have obtained the Crout method. The Crout and Doolittle methods are well suited to calculations by hand or with a desk calculator, because they obviate the need to store the intermediate quantities $a_{ij}^{(k)}$ . They are also attractive when we can accumulate inner products in extended precision.

It is straightforward to incorporate partial pivoting into Doolittle's method (see, e.g., Stewart [1065, 1973, p. 138]). However, rook pivoting and complete pivoting cannot be incorporated without changing the method.

# 9.3. Error Analysis

The error analysis of GE is a combination of the error analyses of inner products and substitution. When this fact is realized, the analysis becomes straightforward. The key observation leading to this viewpoint is that all mathematically equivalent variants of GE satisfy a common error bound. To see why, first note the connection between standard GE, as we have described it, and the Doolittle method, as shown in (9.5). Whether the inner product in (9.5) is calculated as one operation, or whether its terms are calculated many operations apart, precisely the same rounding errors are sustained (assuming that extended precision accumulation of inner products is not used); all that changes is the moment when those rounding errors are committed. If we allow inner products to be reordered, so that, for example, the summation $(\ast)$ in Algorithm 9.2 is calculated with the index $i$ decreasing from $k - 1$ to 1, instead of increasing from 1 to $k - 1$ , then the actual rounding errors are different, but a common bound holds for all orderings.

It suffices, then, to analyse the Doolittle method. It also suffices to analyse the method without pivoting, because GE with partial, rook, or complete pivoting is equivalent to GE without pivoting applied to a permuted matrix.

The assignments $(\ast)$ and $(\ast \ast)$ in Algorithm 9.2 are of the form $y = (c - \sum_{i=1}^{k-1} a_i b_i) / b_k$ , which is analysed in Lemma 8.4. Applying the lemma, we deduce that, no matter what the ordering of the inner products, the computed matrices $\widehat{L}$ and $\widehat{U}$ satisfy (with $\widehat{l}_{kk} := 1$ )

$$
\begin{array}{l} \left| a _ {k j} - \sum_ {i = 1} ^ {k - 1} \widehat {l} _ {k i} \widehat {u} _ {i j} - \widehat {u} _ {k j} \right| \leq \gamma_ {k} \sum_ {i = 1} ^ {k} | \widehat {l} _ {k i} | | \widehat {u} _ {i j} |, \quad j \geq k, \\ \left| a _ {i k} - \sum_ {j = 1} ^ {k} \widehat {l} _ {i j} \widehat {u} _ {j k} \right| \leq \gamma_ {k} \sum_ {j = 1} ^ {k} | \widehat {l} _ {i j} | | \widehat {u} _ {j k} |, \quad i > k. \\ \end{array}
$$

These inequalities constitute a backward error result for LU factorization.

Theorem 9.3. If $GE$ applied to $A \in \mathbb{R}^{m \times n}$ ( $m \geq n$ ) runs to completion then the computed LU factors $\widehat{L} \in \mathbb{R}^{m \times n}$ and $\widehat{U} \in \mathbb{R}^{n \times n}$ satisfy

$$
\widehat {L} \widehat {U} = A + \Delta A, \quad | \Delta A | \leq \gamma_ {n} | \widehat {L} | | \widehat {U} |. \quad \square \tag {9.6}
$$

With only a little more effort, a backward error result can be obtained for the solution of $Ax = b$ .

Theorem 9.4. Let $A \in \mathbb{R}^{n \times n}$ and suppose GE produces computed LU factors $\widehat{L}, \widehat{U}$ , and a computed solution $\widehat{x}$ to $Ax = b$ . Then

$$
(A + \Delta A) \widehat {x} = b, \quad | \Delta A | \leq \gamma_ {3 n} | \widehat {L} | | \widehat {U} |. \tag {9.7}
$$

Proof. From Theorem 9.3, $\widehat{L}\widehat{U} = A + \Delta A_1$ , $|\Delta A_1| \leq \gamma_n |\widehat{L}| |\widehat{U}|$ . By Theorem 8.5, substitution produces $\widehat{y}$ and $\widehat{x}$ satisfying

$$
\begin{array}{l} (\widehat {L} + \Delta L) \widehat {y} = b, \quad | \Delta L | \leq \gamma_ {n} | \widehat {L} |, \\ (\widehat {U} + \Delta U) \widehat {x} = \widehat {y}, \quad | \Delta U | \leq \gamma_ {n} | \widehat {U} |. \\ \end{array}
$$

Thus

$$
\begin{array}{l} b = (\widehat {L} + \Delta L) (\widehat {U} + \Delta U) \widehat {x} \\ = (A + \Delta A _ {1} + \widehat {L} \Delta U + \Delta L \widehat {U} + \Delta L \Delta U) \widehat {x} \\ = (A + \Delta A) \widehat {x}, \\ \end{array}
$$

where

$$
\left| \Delta A \right| \leq \left(3 \gamma_ {n} + \gamma_ {n} ^ {2}\right) \left| \widehat {L} \right| \left| \widehat {U} \right| \leq \gamma_ {3 n} \left| \widehat {L} \right| \left| \widehat {U} \right|,
$$

using Lemma 3.3.

How do we interpret Theorem 9.4? Ideally, we would like $|\Delta A| \leq u |A|$ , which corresponds to the uncertainty introduced by rounding the elements of $A$ , but because each element of $A$ undergoes up to $n$ arithmetic operations we cannot expect better than a bound $|\Delta A| \leq c_n u |A|$ , where $c_n$ is a constant of order $n$ . Such a bound holds if $\widehat{L}$ and $\widehat{U}$ satisfy $|\widehat{L}| |\widehat{U}| = |\widehat{L} \widehat{U}|$ , which certainly holds if $\widehat{L}$ and $\widehat{U}$ are nonnegative, because then (9.6) gives

$$
\begin{array}{l} | \widehat {L} | | \widehat {U} | = | \widehat {L} \widehat {U} | = | A + \Delta A | \leq | A | + \gamma_ {n} | \widehat {L} | | \widehat {U} | \\ \Rightarrow | \widehat {L} | | \widehat {U} | \leq \frac {1}{1 - \gamma_ {n}} | A |. \tag {9.8} \\ \end{array}
$$

Substituting into (9.7), we obtain

$$
(A + \Delta A) \widehat {x} = b, \quad | \Delta A | \leq \frac {\gamma_ {3 n}}{1 - \gamma_ {n}} | A | \quad (\widehat {L}, \widehat {U} \geq 0). \tag {9.9}
$$

This result says that $\widehat{x}$ has a small componentwise relative backward error.

One class of matrices that has nonnegative LU factors is defined as follows. $A \in \mathbb{R}^{n \times n}$ is totally positive (nonnegative) if the determinant of every square submatrix is positive (nonnegative). In particular, this definition requires that

$a_{ij}$ and $\operatorname{det}(A)$ be positive or nonnegative. Some examples of totally nonnegative matrices are given in Chapter 28. If $A$ is totally nonnegative then it has an LU factorization $A = LU$ in which $L$ and $U$ are totally nonnegative, so that $L \geq 0$ and $U \geq 0$ (see Problem 9.6); moreover, the computed factors $\widehat{L}$ and $\widehat{U}$ from GE are nonnegative for sufficiently small values of the unit roundoff $u$ [300, 1977]. Inverses of totally nonnegative matrices also have the property that $|A| = |L||U|$ (see Problem 9.8). Note that the property of a matrix or its inverse being totally nonnegative is generally destroyed under row permutations. Hence for totally nonnegative matrices and their inverses it is best to use Gaussian elimination without pivoting.

One important fact that follows from (9.6) and (9.7) is that the stability of GE is determined not by the size of the multipliers $\widehat{l}_{ij}$ but by the size of the matrix $|\widehat{L}||\widehat{U}|$ . This matrix can be small when the multipliers are large, and large when the multipliers are of order 1 (as we will see in the next section).

To understand the stability of GE further we turn to norms. For GE without pivoting, the ratio $\| |\widehat{L} ||\widehat{U} || / ||A||$ can be arbitrarily large. For example, for the matrix $\left[ \begin{array}{cc}\epsilon & 1\\ 1 & 1 \end{array} \right]$ the ratio is of order $\epsilon^{-1}$ . Assume then that partial pivoting is used. Then $|l_{ij}|\leq 1$ for all $i\geq j$ , since the $l_{ij}$ are the multipliers. And it is easy to show by induction that $|u_{ij}|\leq 2^{i - 1}\max_{k\leq i}|a_{kj}|$ . Hence, for partial pivoting, $L$ is small and $U$ is bounded relative to $A$ .

Traditionally, backward error analysis for GE is expressed in terms of the growth factor

$$
\rho_ {n} = \frac {\operatorname * {m a x} _ {i , j , k} | a _ {i j} ^ {(k)} |}{\operatorname * {m a x} _ {i , j} | a _ {i j} |},
$$

which involves all the elements $a_{ij}^{(k)}$ ( $k = 1:n$ ) that occur during the elimination. Using the bound $|u_{ij}| = |a_{ij}^{(i)}| \leq \rho_n \max_{i,j} |a_{ij}|$ we obtain the following classic theorem.

Theorem 9.5 (Wilkinson). Let $A \in \mathbb{R}^{n \times n}$ and suppose $GE$ with partial pivoting produces a computed solution $\widehat{x}$ to $Ax = b$ . Then

$$
(A + \Delta A) \widehat {x} = b, \quad \| \Delta A \| _ {\infty} \leq n ^ {2} \gamma_ {3 n} \rho_ {n} \| A \| _ {\infty}. \quad \square \tag {9.10}
$$

We hasten to admit to using an illicit manoeuvre in the derivation of this theorem: we have used bounds for $\widehat{L}$ and $\widehat{U}$ that strictly are valid only for the exact $L$ and $U$ . We could instead have defined the growth factor in terms of the computed $\widehat{a}_{ij}^{(k)}$ , but then any bounds for the growth factor would involve the unit roundoff (similarly, we can only guarantee that $|\widehat{l}_{ij}| \leq 1 + u$ ). Our breach of correctness is harmless for the purposes to which we will put the theorem.

The assumption in Theorem 9.5 that partial pivoting is used is not necessary: $\| |L||U| \|_{\infty}$ can also be bounded in terms of the growth factor for GE without pivoting, as the next result shows.

Lemma 9.6. If $A = LU \in \mathbb{R}^{n \times n}$ is an LU factorization produced by GE without pivoting then

$$
\| | L | | U | \| _ {\infty} \leq (1 + 2 (n ^ {2} - n) \rho_ {n}) \| A \| _ {\infty}.
$$

Table 9.1. Classes of matrices for which $\rho_{n} = O(1)$ for GE without pivoting.   

<table><tr><td>Matrix property</td><td>Reference</td></tr><tr><td>Totally nonnegative</td><td>§9.3</td></tr><tr><td>Row or column diagonally dominant</td><td>§9.5</td></tr><tr><td>Symmetric positive definite</td><td>§10.1.1</td></tr><tr><td>Complex symmetric with positive definite Hermitian and skew-Hermitian parts</td><td>§10.4</td></tr></table>

Proof. Let $l_j$ denote the $j$ th column of $L$ and $u_i^T$ denote the $i$ th row of $U$ . Then

$$
\widetilde {A} ^ {(k + 1)} = \widetilde {A} ^ {(k)} - l _ {k} u _ {k} ^ {T}, \qquad k = 1: n - 1,
$$

where $\widetilde{A}^{(k)}$ denotes $A^{(k)}$ with the elements in rows $1: k - 1$ set to zero. Thus

$$
\left| l _ {k} \right| \left| u _ {k} ^ {T} \right| = \left| l _ {k} u _ {k} ^ {T} \right| \leq \left| \widetilde {A} ^ {(k)} \right| + \left| \widetilde {A} ^ {(k + 1)} \right|
$$

and hence

$$
| L | | U | = \sum_ {k = 1} ^ {n} \left| l _ {k} \right| \left| u _ {k} ^ {T} \right| \leq | A | + 2 \sum_ {k = 2} ^ {n} \left| \widetilde {A} ^ {(k)} \right|.
$$

Taking norms and using $|a_{ij}^{(k)}| \leq \rho_n \max_{i,j} |a_{ij}|$ gives

$$
\parallel | L | | U | \parallel_ {\infty} \leq \| A \| _ {\infty} + 2 (n - 1) n \rho_ {n} \| A \| _ {\infty} = (1 + 2 (n - 1) n \rho_ {n}) \| A \| _ {\infty}.
$$

It is also possible to bound the growth factor above in terms of $\| |L||U| \|_{\infty}$ ; see Problem 9.9.

Since the normwise backward stability of GE with or without pivoting is governed by the growth factor, we next turn our attention to analysis of the growth factor. As a prelude, Table 9.1 summarizes classes of matrices for which the growth factor for GE without pivoting is small, and for which it is therefore safe not to pivot.

# 9.4. The Growth Factor

It is easy to show that $\rho_{n} \leq 2^{n - 1}$ for partial pivoting. Wilkinson notes that this upper bound is achieved for matrices of the form illustrated for $n = 4$ by

$$
\left[ \begin{array}{c c c c} 1 & 0 & 0 & 1 \\ - 1 & 1 & 0 & 1 \\ - 1 & - 1 & 1 & 1 \\ - 1 & - 1 & - 1 & 1 \end{array} \right].
$$

For these matrices, no interchanges are required by partial pivoting, and there is exponential growth of elements in the last column of the reduced matrices. In fact, this is just one of a nontrivial class of matrices for which partial pivoting achieves maximal growth. When necessary in the rest of this chapter, we denote the growth factor for partial pivoting by $\rho_n^p$ and that for complete pivoting by $\rho_n^c$ .

Theorem 9.7 (Higham and Higham). All real $n \times n$ matrices $A$ for which $\rho_n^p(A) = 2^{n-1}$ are of the form

$$
A = D M \left[ \begin{array}{l l l} T & \vdots & \alpha d \\ 0 & \vdots \end{array} \right],
$$

where $D = \mathrm{diag}(\pm 1)$ , $M$ is unit lower triangular with $m_{ij} = -1$ for $i > j$ , $T$ is an arbitrary nonsingular upper triangular matrix of order $n - 1$ , $d = (1,2,4,\ldots ,2^{n - 1})^T$ , and $\alpha$ is a scalar such that $\alpha := |a_{1n}| = \max_{i,j}|a_{ij}|$ .

Proof. GEPP applied to a matrix $A$ gives a factorization $B := PA = LU$ , where $P$ is a permutation matrix. It is easy to show that $|u_{ij}| \leq 2^{i-1} \max_{r \leq i} |b_{rj}|$ , with equality for $i = s$ only if there is equality for $i = 1: s - 1$ . Thus $\rho_n = 2^{n-1}$ implies that the last column of $U$ has the form $\alpha Dd$ , and also that $|b_{1n}| = \max_{i,j} |b_{ij}|$ . By considering the final column of $B$ , and imposing the requirement that $|l_{ij}| \leq 1$ , it is easy to show that the unit lower triangular matrix $L$ must have the form $L = DMD$ . It follows that at each stage of the reduction every multiplier is $\pm 1$ ; hence no interchanges are performed, that is, $P = I$ . The only requirement on $T$ is that it be nonsingular, for if $t_{ii} = 0$ then the $i$ th elimination stage would be skipped because of a zero pivot column and no growth would be produced on that stage.

Note that by varying the elements $m_{ij}$ ( $i > j$ ) and the vector $d$ in Theorem 9.7 we can construct matrices for which $\rho_n^p$ achieves any desired value between 1 and $2^{n-1}$ .

Despite the existence of matrices for which $\rho_{n}$ is large with partial pivoting, the growth factor is almost invariably small in practice. For example, Wilkinson says "It is our experience that any substantial increase in size of elements of successive $A_{r}$ is extremely uncommon even with partial pivoting ... No example which has arisen naturally has in my experience given an increase by a factor as large as 16" [1233, 1965, pp. 213-214].

Matrices that yield large growth factors and that arise, or could arise, in practical applications, are rare. Wright [1261, 1993] has found a class of two-point boundary value problems that, when solved by the multiple shooting method, yield a linear system for which partial pivoting suffers exponential growth. The matrix is block lower bidiagonal, except for a nonzero block in the top right-hand corner. Furthermore, Foster [434, 1994] shows that a quadrature method for solving a practically occurring Volterra integral equation gives rise to linear systems for which partial pivoting again gives large growth factors.

There exist some well-known matrices that give unusually large, but not exponential, growth. They can be found using the following theorem, which is applicable whatever the strategy for interchanging rows and columns in GE.

Theorem 9.8 (Higham and Higham). Let $A \in \mathbb{C}^{n \times n}$ be nonsingular and set $\alpha = \max_{i,j} |a_{ij}|$ , $\beta = \max_{i,j} \left| (A^{-1})_{ij} \right|$ , and $\theta = (\alpha \beta)^{-1}$ . Then $\theta \leq n$ , and for any permutation matrices $P$ and $Q$ such that $PAQ$ has an LU factorization, the growth factor $\rho_n$ for $GE$ without pivoting on $PAQ$ satisfies $\rho_n \geq \theta$ .

Proof. The inequality $\theta \leq n$ follows from $\sum_{j=1}^{n} a_{ij} (A^{-1})_{ji} = 1$ . Consider an LU factorization $PAQ = LU$ computed by GE. We have

$$
\begin{array}{l} \left| u _ {n n} ^ {- 1} \right| = \left| e _ {n} ^ {T} U ^ {- 1} e _ {n} \right| = \left| e _ {n} ^ {T} U ^ {- 1} L ^ {- 1} e _ {n} \right| = \left| e _ {n} ^ {T} Q ^ {T} A ^ {- 1} P ^ {T} e _ {n} \right| \\ = \left| \left(A ^ {- 1}\right) _ {i j} \right| \quad \text {f o r s o m e} i, j \tag {9.11} \\ \leq \beta . \\ \end{array}
$$

Hence $\max_{i,j,k} |a_{ij}^{(k)}| \geq |u_{nn}| \geq \beta^{-1}$ , and the result follows.

![](images/32a86f5954bd3a071468b2546b7d8ee5f9c237485e1a36af9d715af0988fa749.jpg)

Note that $\theta^{-1} = \alpha \beta$ satisfies $\kappa_{\infty}(A)^{-1} \leq \theta^{-1} \leq n^{2}\kappa_{\infty}(A)^{-1}$ . Clearly, $A$ has to be very well conditioned for the theorem to provide a lower bound $\theta$ near the maximum of $n$ .

We apply the theorem to three noncontrived matrices that appear in practical applications.

(1) The matrix

$$
S _ {n} = \sqrt {\frac {2}{n + 1}} \left(\sin \left(\frac {i j \pi}{n + 1}\right)\right) _ {i, j = 1} ^ {n} \tag {9.12}
$$

is the symmetric, orthogonal eigenvector matrix for the second difference matrix (the tridiagonal matrix with typical row $(-1, 2, -1)$ —see §28.5); it arises, for example, in the analysis of time series [24, 1971, §6.5]. Theorem 9.8 gives $\rho_n(S_n) \geq (n + 1)/2$ .

(2) A Hadamard matrix $H_{n}$ is an $n \times n$ matrix with elements $h_{ij} = \pm 1$ and for which the rows of $H_{n}$ are mutually orthogonal. Hadamard matrices exist only for certain $n$ ; a necessary condition for their existence if $n > 2$ is that $n$ is a multiple of 4. For more about Hadamard matrices see Hall [538, 1967, Chap. 14], Hedayat, Sloane, and Stufken [557, 1999, Chap. 7], Wallis [1205, 1993], and Wallis, Street, and Wallis [1206, 1972]. We have $H_{n}H_{n}^{T} = nI$ , and so $H_{n}^{-1} = n^{-1}H_{n}^{T}$ . Theorem 9.8 gives $\rho_{n} \geq n$ .

(3) The next matrix is a complex Vandermonde matrix based on the roots of unity, which occurs in the evaluation of Fourier transforms (see §24.1):

$$
V _ {n} = \left(\exp \left(- 2 \pi i (r - 1) (s - 1) / n\right)\right) _ {r, s = 1} ^ {n}. \tag {9.13}
$$

Since $V_{n}^{-1} = n^{-1}V_{n}^{H}$ , Theorem 9.8 gives $\rho_n(V_n)\geq n$

Note that each of these matrices is orthogonal or unitary (to within a row scaling in the case of the Hadamard matrix), so it is not necessary to apply GE to them! This may explain why growth factors of order $n$ for these matrices have not been reported in the literature as occurring in practice.

To summarize, although there are practically occurring matrices for which partial pivoting yields a moderately large, or even exponentially large, growth factor, the growth factor is almost invariably found to be small. Explaining this fact remains one of the major unsolved problems in numerical analysis. The best attempt to date is by Trefethen and Schreiber [1157, 1990], who develop a statistical model of the average growth factor for partial pivoting and complete pivoting. Their model supports their empirical findings that for various distributions of random matrices the average growth factor (normalized by the standard deviation of the

![](images/f22cd5929019376669f19958ee48a39fc510b62bb62946402f4a3754b98f93b2.jpg)  
Figure 9.2. Upper bounds for growth factors $\rho_{n}$ for partial pivoting, rook pivoting, and complete pivoting.

initial matrix elements) is close to $n^{2/3}$ for partial pivoting and $n^{1/2}$ for complete pivoting (for $n \leq 1024$ ). Extensive experiments by Edelman suggest that for random matrices from the normal $N(0,1)$ distribution the unnormalized growth factor for partial pivoting grows like $n^{1/2}$ [382, 1995]. Trefethen and Bau [1156, 1997, Lecture 22] outline a possible strategy for explaining the growth factor behaviour: their idea is to show that for a matrix to produce a large growth factor with partial pivoting its column spaces must possess a certain skewness property and then to prove that this property holds with low probability for random matrices.

We turn now to complete pivoting. Wilkinson [1229, 1961, pp. 282-285] showed that

$$
\rho_ {n} ^ {c} \leq n ^ {1 / 2} \left(2 \cdot 3 ^ {1 / 2} \dots n ^ {1 / (n - 1)}\right) ^ {1 / 2} \sim c n ^ {1 / 2} n ^ {\frac {1}{4} \log n}, \tag {9.14}
$$

and that this bound is not attainable. As Figure 9.2 illustrates, the bound is a much more slowly growing function than $2^{n-1}$ , but it can still be quite large (e.g., it is 3570 for $n = 100$ ). As for partial pivoting, in practice the growth factor is usually small. Wilkinson stated that "no matrix has been encountered in practice for which $p_1 / p_n$ was as large as 8" [1229, 1961, p. 285] and that "no matrix has yet been discovered for which $f(r) > r$ " [1233, 1965, p. 213] (here, $p_i$ is the $(n - i + 1)$ st pivot and $f(r) \coloneqq \rho_r^c$ ).

Cryer [282, 1968] defined

$$
g (n) = \sup  _ {A \in \mathbb {R} ^ {n \times n}} \rho_ {n} ^ {c} (A). \tag {9.15}
$$

The following results are known:

$g(2) = 2$ (trivial).   
$g(3) = 2\frac{1}{4}$ ; Tornheim [1149, 1965] and Cohen [257, 1974].

$g(4) = 4$ ;Cryer [282,1968] and Cohen [257,1974].   
$g(5) <   5.005$ ; Cohen [257, 1974].

Tornheim [1149, 1965] (see also Cryer [282, 1968]) showed that $\rho_n^c (H_n)\geq n$ for any $n\times n$ Hadamard matrix $H_{n}$ (a bound which, as we saw above, holds for any form of pivoting). For $n$ such that a Hadamard matrix does not exist, the best known lower bound is $g(n)\geq \rho_n^c (S_n) = (n + 1) / 2$ (see (9.12)).

Cryer [282, 1968] conjectured that for real matrices $\rho_n^c (A)\leq n$ , with equality if and only if $A$ is a Hadamard matrix. The conjecture $\rho_{n}^{c}(A)\leq n$ became one of the most famous open problems in numerical analysis, and has been investigated by many mathematicians. The conjecture was finally shown to be false in 1991. Using a package LANCELOT [263, 1992] designed for large-scale nonlinear optimization, Gould [513, 1991] discovered a $13\times 13$ matrix for which the growth factor is 13.0205 in IEEE double precision floating point arithmetic. Edelman subsequently showed, using the symbolic manipulation packages Mathematica and Maple, that a growth factor 13.02 can be achieved in exact arithmetic by making a small perturbation (of relative size $10^{-7}$ ) to one element of Gould's matrix [374, 1992], [385, 1991]. A more striking counterexample to the conjecture is a matrix of order 25 for which $\rho_{25}^{c} = 32.986341$ [374, 1992]. Interesting problems remain, such as determining $\lim_{n\to \infty}g(n) / n$ and evaluating $\rho_{n}^{c}$ for Hadamard matrices (see Problem 9.17).

For complex matrices the maximum growth factor is at least $n$ for any $n$ , since $\rho_n^c (V_n)\geq n$ (see (9.13)). The growth can exceed $n$ , even for $n = 3$ : Tornheim [1149, 1965] constructed the example

$$
A = \left[ \begin{array}{ccc} 1 & 1 & 1 \\ 1 & z & z ^ {- 1} \\ 1 & z ^ {- 1} & z \end{array} \right], \qquad z = (- 1 + i \sqrt {8}) / 3,
$$

for which $\rho_3^c (A) = 3.079$

Finally, we turn to rook pivoting. Foster [435, 1997] has shown that the growth factor for rook pivoting satisfies

$$
\rho_ {n} \leq 1. 5 n ^ {\frac {3}{4} \log n}. \tag {9.16}
$$

This bound grows only slightly faster than that in (9.14) for complete pivoting and is much slower growing than that for partial pivoting; see Figure 9.2. Nothing is known about the largest attainable growth factor for rook pivoting (see Problem 9.18).

Figure 9.3 shows the results of an experiment in which, for each dimension $n = 100:100:1500$ , 10 random matrices from the normal $N(0,1)$ distribution and 10 from the uniform [0,1] distribution were factorized by LU factorization with partial pivoting, rook pivoting, and complete pivoting. The maximum growth factors and the number of comparisons (averaged in the case of rook pivoting) are plotted against $n$ .

# 9.5. Diagonally Dominant and Banded Matrices

For matrices with certain special properties, more can be said about the behaviour of GE and, in particular, the size of the growth factor.

![](images/9c3d052347d2c0c37af5e79ece8df44ee8ea8573ccc1f65d47b9119eeb819ee5.jpg)

![](images/930e8b03c5e4e262bc574e906c8f779e27a1d1dcac8535cb0b1e13e31ed1276d.jpg)

![](images/4884fc26e75c35fef8d3559a28d21617735fd2be120e0aebd8ee285b2feb0e31.jpg)

![](images/f3ee91f8ac119262c206dcc00013c7fe175e9e2d81774a32642b3a7328d723f8.jpg)

![](images/df257058443dd1d4f0fa8c27ddf3d4a44e73f5494a41a9e54be74081a3e44c8c.jpg)  
Figure 9.3. Maximum growth factors $\rho_{n}$ (top) and average number of comparisons (bottom) for 15000 random matrices of dimension $n = 100:100:1500$ .

As a first example, suppose $A \in \mathbb{C}^{n \times n}$ is diagonally dominant by rows,

$$
\sum_ {j \neq i} | a _ {i j} | \leq | a _ {i i} |, \quad i = 1: n,
$$

or diagonally dominant by columns, that is, $A^{*}$ is diagonally dominant by rows. Then GE without pivoting is perfectly stable.

Theorem 9.9 (Wilkinson). Let $A \in \mathbb{C}^{n \times n}$ be nonsingular. If $A$ is diagonally dominant by rows or columns then $A$ has an LU factorization without pivoting and the growth factor $\rho_n \leq 2$ . If $A$ is diagonally dominant by columns then $|l_{ij}| \leq 1$ for all $i$ and $j$ in the LU factorization without pivoting (hence GEPP does not require any row interchanges).

Proof. The result follows immediately from the more general Theorems 13.7 and 13.8 for block diagonally dominant matrices. (Note that the diagonal elements of $A$ are nonzero, since otherwise the diagonal dominance would imply that $A$ has a zero row or column, contradicting the nonsingularity of $A$ . Therefore (13.17) holds.)

Note that for a matrix diagonally dominant by rows the multipliers can be arbitrarily large but, nevertheless, $\rho_{n} \leq 2$ , so GE is perfectly stable. In fact, by writing $|L||U| = |AU^{-1}||U| \leq |A||U^{-1}||U|$ and invoking Lemma 8.8 we find that

$$
\left\| \left| L \right| \right| U | \| _ {\infty} \leq (2 n - 1) \| A \| _ {\infty}. \tag {9.17}
$$

This bound shows clearly that any large multipliers in $L$ must be cancelled by correspondingly small elements of $U$ .

A smaller bound for the growth factor also holds for an upper Hessenberg matrix: a matrix $H \in \mathbb{C}^{n \times n}$ for which $h_{ij} = 0$ for $i > j + 1$ .

Theorem 9.10 (Wilkinson). If $A \in \mathbb{C}^{n \times n}$ is upper Hessenberg then $\rho_n^p \leq n$ .

Proof. The structure of an upper Hessenberg $H$ means that at each stage of GEPP we just add a multiple of the pivot row to the next row (after possibly swapping these two rows). That $\rho_n^p \leq n$ is a consequence of the following claim, which is easily proved by induction: at the start of stage $k$ , row $k + 1$ of the reduced matrix is the same as row $k + 1$ of the original matrix, and the pivot row has elements of modulus at most $k$ times the largest element of $H$ . $\square$

A matrix $A \in \mathbb{C}^{n \times n}$ has lower bandwidth $p$ and upper bandwidth $q$ if $a_{ij} = 0$ for $i > j + p$ and $j > i + q$ ; see Figure 9.4. It is well known that in an LU factorization of a banded matrix the factors inherit $A$ 's band structure: $L$ has lower bandwidth $p$ and $U$ has upper bandwidth $q$ . If partial pivoting is used then, in $PA = LU$ , $L$ has at most $p + 1$ nonzeros per column and $U$ has upper bandwidth $p + q$ . (For proofs of these properties see Golub and Van Loan [509, 1996, §4.3].) It is not hard to see that for a banded matrix, $\gamma_n$ in Theorem 9.3 can be replaced by $\gamma_{\max(p + 1, q + 1)}$ and $\gamma_{3n}$ in Theorem 9.4 can be replaced by $\gamma_{\max(p + 1, q + 1)} + \gamma_{p + q + 1}$ .

![](images/dda45dab794657dabb3a6125772f22b1900b813815fab4ebe416f1034b5cc4ba.jpg)  
Figure 9.4. A banded matrix.

The following result bounds the growth factor for partial pivoting on a banded matrix.

Theorem 9.11 (Bohte). If $A \in \mathbb{C}^{n \times n}$ has upper and lower bandwidths $p$ then $\rho_n^p \leq 2^{2p - 1} - (p - 1)2^{p - 2}$ , and this bound is almost attainable when $n = 2p + 1$ .

Proof. See Bohte [146, 1975]. An example with $n = 9$ and $p = 4$ in which equality is almost attained is the matrix

$$
A = \left[ \begin{array}{c c c c c c c c c} - 1 & - 1 & - 1 & - 1 & 1 & 0 & 0 & 0 & 0 \\ - 1 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ - 1 & - 1 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\ - 1 & - 1 & - 1 & 1 & 0 & 0 & 0 & 0 & 0 \\ 1 + \epsilon & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 \\ 0 & - 1 & - 1 & - 1 & - 1 & 1 & 0 & 0 & 1 \\ 0 & 0 & - 1 & - 1 & - 1 & - 1 & 1 & 0 & 1 \\ 0 & 0 & 0 & - 1 & - 1 & - 1 & - 1 & 1 & 1 \\ 0 & 0 & 0 & 0 & - 1 & - 1 & - 1 & - 1 & 1 \end{array} \right],
$$

where $\epsilon$ is an arbitrarily small positive number that ensures that rows 1 and 5 are interchanged on the first stage of the elimination, this being the only row interchange required. Ignoring terms in $\epsilon$ , the last column of $U$ in $PA = LU$ is

$$
[ 1,   1,   2,   4,   8,   1 6,   3 1,   6 0,   1 1 6 ] ^ {T}
$$

and the growth factor is 116.

A special case of Theorem 9.11 is the easily verified result that for a tridiagonal matrix, $\rho_{n}^{p}\leq 2$ . Hence GEPP achieves a small normwise backward error for tridiagonal matrices. In the next section we show that for several types of tridiagonal matrix GE without pivoting achieves a small componentwise backward error.

# 9.6. Tridiagonal Matrices

Consider the nonsingular tridiagonal matrix

$$
A = \left[ \begin{array}{c c c c c} d _ {1} & e _ {1} &  &  &  \\ c _ {2} & d _ {2} & e _ {2} &  &  \\  & \ddots & \ddots & \ddots &  \\  &  & \ddots & \ddots & e _ {n - 1} \\  &  &  & c _ {n} & d _ {n} \end{array} \right] \in \mathbb {R} ^ {n \times n},
$$

and assume that $A$ has an LU factorization $A = LU$ , where

$$
L = \left[ \begin{array}{c c c c c} 1 & & & & \\ l _ {2} & 1 & & & \\ & l _ {3} & 1 & & \\ & & \ddots & \ddots & \\ & & & l _ {n} & 1 \end{array} \right], \quad U = \left[ \begin{array}{c c c c c} u _ {1} & e _ {1} & & & \\ & u _ {2} & e _ {2} & & \\ & & \ddots & \ddots & \\ & & & \ddots & e _ {n - 1} \\ & & & & u _ {n} \end{array} \right]. \tag {9.18}
$$

GE for computing $L$ and $U$ is described by the recurrence relations

$$
u _ {1} = d _ {1}; \quad \left. \begin{array}{c} l _ {i} = c _ {i} / u _ {i - 1} \\ u _ {i} = d _ {i} - l _ {i} e _ {i - 1} \end{array} \right\} i = 2: n. \tag {9.19}
$$

For the computed quantities, we have

$$
(1 + \epsilon_ {i}) \widehat {l _ {i}} = \frac {c _ {i}}{\widehat {u} _ {i - 1}}, \quad | \epsilon_ {i} | \leq u,
$$

$$
(1 + \theta_ {i}) \widehat {u} _ {i} = d _ {i} - \widehat {l} _ {i} e _ {i - 1} (1 + \delta_ {i}), \quad | \theta_ {i} |, | \delta_ {i} | \leq u.
$$

Hence

$$
\left| c _ {i} - \widehat {l} _ {i} \widehat {u} _ {i - 1} \right| \leq u \left| \widehat {l} _ {i} \widehat {u} _ {i - 1} \right|,
$$

$$
\left| d _ {i} - \widehat {l} _ {i} e _ {i - 1} - \widehat {u} _ {i} \right| \leq u \big (\left| \widehat {l} _ {i} e _ {i - 1} \right| + \left| \widehat {u} _ {i} \right| \big).
$$

In matrix terms these bounds may be written as

$$
A = \widehat {L} \widehat {U} + \Delta A, \quad | \Delta A | \leq u | \widehat {L} | | \widehat {U} |. \tag {9.20}
$$

If the LU factorization is used to solve a system $Ax = b$ by forward and back substitution then it is straightforward to show that the computed solution $\hat{x}$ satisfies

$$
(\widehat {L} + \varDelta L) (\widehat {U} + \varDelta U) \widehat {x} = b, | \varDelta L | \leq u | \widehat {L} |, | \varDelta U | \leq (2 u + u ^ {2}) | \widehat {U} |. (9. 2 1)
$$

Combining (9.20) and (9.21) we have, overall,

$$
(A + \Delta A) \widehat {x} = b, \quad | \Delta A | \leq f (u) | \widehat {L} | | \widehat {U} |, \quad f (u) = 4 u + 3 u ^ {2} + u ^ {3}. \tag {9.22}
$$

The backward error result (9.22) applies to arbitrary nonsingular tridiagonal $A$ having an LU factorization. We are interested in determining classes of tridiagonal $A$ for which a bound of the form $|\Delta A| \leq g(u)|A|$ holds. Such a bound will hold if $|\widehat{L}||\widehat{U}| = |\widehat{L}\widehat{U}|$ , as noted in §9.3 (see (9.8)).

Three classes of matrices for which $|\widehat{L}||\widehat{U}| = |\widehat{L}\widehat{U}|$ holds for the exact $L$ and $U$ are identified in the following theorem.

Theorem 9.12. Let $A \in \mathbb{R}^{n \times n}$ be nonsingular and tridiagonal. If any of the following conditions hold then $A$ has an LU factorization and $|L||U| = |LU|$ :

(a) $A$ is symmetric positive definite;   
(b) $A$ is totally nonnegative, or equivalently, $L\geq 0$ and $U\geq 0$   
(c) $A$ is an $M$ -matrix, or equivalently, $L$ and $U$ have positive diagonal elements and nonpositive off-diagonal elements;   
(d) $A$ is sign equivalent to a matrix $B$ of type (a)-(c), that is, $A = D_{1}BD_{2}$ , where $|D_1| = |D_2| = I$ .

Proof. For (a), it is well known that a symmetric positive definite $A$ has an LU factorization in which $U = DL^{T}$ , where $D$ is diagonal with positive diagonal elements. Hence $|L||U| = |L||D||L^{T}| = |LDL^{T}| = |LU|$ , where the middle equality requires a little thought. In (b) and (c) the equivalences, and the existence of an LU factorization, follow from known results on totally nonnegative matrices [284, 1976] and $M$ -matrices [106, 1994]; $|L||U| = |LU|$ is immediate from the sign properties of $L$ and $U$ . (d) is trivial. $\square$

For diagonally dominant tridiagonal matrices, $|L||U|$ is not equal to $|LU| = |A|$ , but it cannot be much bigger.

Theorem 9.13. Suppose $A \in \mathbb{R}^{n \times n}$ is nonsingular, tridiagonal, and diagonally dominant by rows or columns, and let $A$ have the LU factorization $A = LU$ . Then $|L||U| \leq 3|A|$ .

Proof. If $|i - j| = 1$ then $\big(|L||U|\big)_{ij} = |a_{ij}|$ , so it suffices to consider the diagonal elements and show that (using the notation of (9.18))

$$
\left| l _ {i} e _ {i - 1} \right| + \left| u _ {i} \right| \leq 3 \left| d _ {i} \right|.
$$

The rest of the proof is for the case where $A$ is diagonally dominant by rows; the proof for diagonal dominance by columns is similar.

First, we claim that $|e_i| \leq |u_i|$ for all $i$ . The proof is by induction. For $i = 1$ the result is immediate, and if it is true for $i - 1$ then, from (9.19),

$$
\begin{array}{l} \left| u _ {i} \right| \geq \left| d _ {i} \right| - \left| l _ {i} \right| \left| e _ {i - 1} \right| = \left| d _ {i} \right| - \frac {\left| c _ {i} \right|}{\left| u _ {i - 1} \right|} \left| e _ {i - 1} \right| \\ \geq \left| d _ {i} \right| - \left| c _ {i} \right| \geq \left| e _ {i} \right|, \\ \end{array}
$$

as required. Note that, similarly, $|u_i| \leq |d_i| + |c_i|$ . Finally,

$$
\begin{array}{l} \left| l _ {i} e _ {i - 1} \right| + \left| u _ {i} \right| = \left| \frac {c _ {i}}{u _ {i - 1}} e _ {i - 1} \right| + \left| u _ {i} \right| \leq \left| c _ {i} \right| + \left| u _ {i} \right| \\ \leq \left| c _ {i} \right| + \left(\left| d _ {i} \right| + \left| c _ {i} \right|\right) \\ \leq 3 \left| d _ {i} \right|. \quad \square \\ \end{array}
$$

Theorem 9.14. If the nonsingular tridiagonal matrix $A$ is of type (a)-(d) in Theorem 9.12, and if the unit roundoff $u$ is sufficiently small, then $GE$ for solving $Ax = b$ succeeds and the computed solution $\widehat{x}$ satisfies

$$
(A + \varDelta A) \widehat {\boldsymbol {x}} = b, \qquad | \varDelta A | \le h (u) | A |, \qquad h (u) = \frac {4 u + 3 u ^ {2} + u ^ {3}}{1 - u}.
$$

The same conclusion is true if $A$ is diagonally dominant by rows or columns, with no restriction on $u$ , provided the bound is multiplied by 3.

Proof. If $u$ is sufficiently small then for types (a)-(c) the diagonal elements of $\widehat{U}$ will be positive, since $\widehat{u}_i \to u_i > 0$ as $u \to 0$ . It is easy to see that $\widehat{u}_i > 0$ for all $i$ ensures that $|\widehat{L}||\widehat{U}| = |\widehat{L}\widehat{U}|$ . The argument is similar for type (d). The result therefore follows from (9.22) and (9.8). The last part is trivial.

A corollary of Theorem 9.14 is that it is not necessary to pivot for the matrices specified in the theorem (and, indeed, pivoting could vitiate the result of the theorem). Note that large multipliers may occur under the conditions of the theorem, but they do not affect the stability. For example, consider the $M$ -matrix

$$
A = \left[ \begin{array}{c c c} 2 & - 2 & 0 \\ \epsilon - 2 & 2 & 0 \\ 0 & - 1 & 3 \end{array} \right] = \left[ \begin{array}{c c c} 1 & 0 & 0 \\ (\epsilon - 2) / 2 & 1 & 0 \\ 0 & - 1 / \epsilon & 1 \end{array} \right] \left[ \begin{array}{c c c} 2 & - 2 & 0 \\ 0 & \epsilon & 0 \\ 0 & 0 & 3 \end{array} \right] = L U,
$$

where $0 \leq \epsilon < 2$ . The multiplier $l_{32}$ is unbounded as $\epsilon \to 0$ , but $|L||U| = |A|$ and GE performs very stably, as Theorem 9.14 shows it must.

# 9.7. More Error Bounds

From Theorem 9.4 it follows that the computed solution $\widehat{x}$ from GE satisfies

$$
\frac {\| \boldsymbol {x} - \widehat {\boldsymbol {x}} \| _ {\infty}}{\| \boldsymbol {x} \| _ {\infty}} \leq \gamma_ {3 n} \frac {\| | \boldsymbol {A} ^ {- 1} | | \widehat {\boldsymbol {L}} | | \widehat {\boldsymbol {U}} | | \widehat {\boldsymbol {x}} | \| _ {\infty}}{\| \boldsymbol {x} \| _ {\infty}},
$$

and this bound can be simplified to, for example,

$$
\frac {\| \boldsymbol {x} - \widehat {\boldsymbol {x}} \| _ {\infty}}{\| \boldsymbol {x} \| _ {\infty}} \leq \gamma_ {3 n} \kappa_ {\infty} (A) \frac {\| | \widehat {L} | | \widehat {U} | \| _ {\infty}}{\| A \| _ {\infty}}.
$$

Given particular information about $A$ it is often possible to obtain much stronger bounds. For example, if $A$ is totally nonnegative then we know that GE produces a small componentwise relative backward error, as shown by (9.9), and hence $\| x - \widehat{x} \|_{\infty} / \| x \|_{\infty}$ is bounded by a multiple of $\operatorname{cond}(A, x) u$ .

Here is a line of attack that is fruitful in several situations. By Theorem 9.3 the computed LU factors satisfy $\widehat{L}\widehat{U} = A + \Delta A_0$ , with $|\Delta A_0| \leq \gamma_n |\widehat{L}| |\widehat{U}|$ . Hence $\widehat{L} = (A + \Delta A_0) \widehat{U}^{-1}$ and

$$
| \widehat {L} | | \widehat {U} | \leq | A + \varDelta A _ {0} | | \widehat {U} ^ {- 1} | | \widehat {U} | \leq (| A | + \gamma_ {n} | \widehat {L} | | \widehat {U} |) | | \widehat {U} ^ {- 1} | | \widehat {U} |,
$$

which gives, since $1 - \gamma_{n}|\widehat{U}^{-1}||\widehat{U}|$ is an $M$ -matrix for $\gamma_{n} < 1$

$$
| \widehat {L} | | \widehat {U} | \leq | A | | \widehat {U} ^ {- 1} | | \widehat {U} | (1 - \gamma_ {n} | \widehat {U} ^ {- 1} | | \widehat {U} |) ^ {- 1}.
$$

From Theorem 9.4, $(A + \Delta A)\widehat{x} = b$ , with

$$
\left| \varDelta A \right| \leq \gamma_ {3 n} | \widehat {L} | | \widehat {U} | \leq \gamma_ {3 n} | A | | \widehat {U} ^ {- 1} | | \widehat {U} | (1 - \gamma_ {n} | \widehat {U} ^ {- 1} | | \widehat {U} |) ^ {- 1}.
$$

It follows that GE has a row-wise backward error bounded by a multiple of $\operatorname{cond}(U)u$ (see Table 7.1). Correspondingly, the forward error is easily seen to satisfy

$$
\begin{array}{l} \frac {\| x - \widehat {x} \| _ {\infty}}{\| x \| _ {\infty}} \leq 3 n u \frac {\| | A ^ {- 1} | | A | \| \widehat {U} ^ {- 1} | | \widehat {U} | | \widehat {x} | \| _ {\infty}}{\| x \| _ {\infty}} + O (u ^ {2}) \\ \leq 3 n u \operatorname {c o n d} (A) \operatorname {c o n d} (U) + O \left(u ^ {2}\right). \tag {9.23} \\ \end{array}
$$

In general, $\operatorname{cond}(U)$ is unbounded, but from results in Chapter 8 we know that

- $\operatorname{cond}(U) \leq 2^n - 1$ for rook pivoting and complete pivoting for general $A$ (see Lemma 8.6),   
- $\operatorname{cond}(U) \leq 2n - 1$ for GE without pivoting applied to row diagonally dominant matrices (see Lemma 8.8).

An interesting conclusion is that a small row-wise backward error and (hence) a forward error bounded by a multiple of $\operatorname{cond}(A)$ are guaranteed for row diagonally dominant matrices.

We continue the discussion of row-wise error bounds in the next section.

# 9.8. Scaling and Choice of Pivoting Strategy

Prior to solving a linear system $Ax = b$ by GE we are at liberty to scale the rows and the columns:

$$
A x = b \rightarrow D _ {1} A D _ {2} \cdot D _ {2} ^ {- 1} x = D _ {1} b, \quad \text {o r} \quad A ^ {\prime} y = c, \tag {9.24}
$$

where $D_{1}$ and $D_{2}$ are nonsingular diagonal matrices. We apply GE to the scaled system $A'y = c$ and then recover $x$ from $x = D_{2}y$ . Although scaling was used in some of the earliest published programs for GE [431, 1967], [836, 1962], how best to choose a scaling is still not well understood, and no single scaling algorithm can be guaranteed always to perform satisfactorily. Wilkinson's remark "We cannot decide whether equations are ill-conditioned without examining the way in which the coefficients were derived" [1233, 1965, p. 198] sums up the problem of scaling rather well.

The effect of scaling in GE without pivoting is easy to describe. If the elements of $D_{1}$ and $D_{2}$ are powers of the machine base $\beta$ (so that the scaling is done without error) and GE produces $\widehat{L}$ and $\widehat{U}$ satisfying $A + \Delta A = \widehat{L}\widehat{U}$ , then GE on $A' = D_{1}AD_{2}$ produces $D_{1}\widehat{L}D_{1}^{-1}$ and $D_{1}\widehat{U}D_{2}$ satisfying $A' + D_{1}\Delta AD_{2} = D_{1}\widehat{L}D_{1}^{-1}$ . $D_{1}\widehat{U}D_{2}$ . In other words, the rounding errors in GE scale in the same way as $A$ . This is a result of Bauer [89, 1963] (see [431, 1967, Chap. 11] for a clear proof and discussion). With partial pivoting, however, the choice of pivots is affected by the row scaling (though not the column scaling), and in a way that is difficult to predict.

We can take a method-independent approach to scaling, by considering any method for solving $Ax = b$ that yields a solution satisfying

$$
\frac {\| x - \widehat {x} \| _ {\infty}}{\| x \| _ {\infty}} \leq c _ {n} \kappa_ {\infty} (A) u,
$$

with $c_{n}$ a constant. For the scaled system (9.24) we have

$$
\frac {\left\| D _ {2} ^ {- 1} (x - \widehat {x}) \right\| _ {\infty}}{\left\| D _ {2} ^ {- 1} x \right\| _ {\infty}} \leq c _ {n} \kappa_ {\infty} \left(D _ {1} A D _ {2}\right) u,
$$

so it is natural to choose $D_{1}$ and $D_{2}$ to minimize $\kappa_{\infty}(D_1AD_2)$ . As we saw in §7.3 (Theorem 7.8) the minimum possible value is $\rho(|A||A^{-1}|)$ . However, a column scaling has the (usually) undesirable effect of changing the norm in which the error is measured. With row scaling only, the minimum value of $\kappa_{\infty}(D_1A)$ is $\mathrm{cond}(A) = \| |A^{-1}||A| \|_{\infty}$ , achieved when $D_{1}A$ has rows of unit 1-norm (see (7.15)). Thus row equilibration yields a cond-bounded forward error.

Specializing to GE, we can say more. If $A$ is row-equilibrated in the 1-norm then $|A|e = e$ and hence, from Theorem 9.4, the backward error matrix $\Delta A$ satisfies

$$
\left| \varDelta A \right| \leq \gamma_ {3 n} | \widehat {L} | | \widehat {U} | \leq \gamma_ {3 n} \| \left| \widehat {L} \right| | \widehat {U} | \| _ {\infty} e e ^ {T} = \gamma_ {3 n} \| \left| \widehat {L} \right| | \widehat {U} | \| _ {\infty} | A | e e ^ {T}.
$$

In other words, if GE is normwise backward stable then it is row-wise backward stable (cf. Table 7.1), as noted by Skeel [1042, 1981].

We have already seen in §9.7 that a cond-bounded forward error is guaranteed for GE without pivoting on a row diagonally dominant matrix and for GE with rook pivoting or complete pivoting on an arbitrary matrix, provided that $\operatorname{cond}(U)$ is of order 1. Further possibilities exist: if we LU factorize $A^T$ instead of $A$ (thus effectively carrying out column operations rather than row operations on $A$ ) then from (9.23) with the roles of $L$ and $U$ interchanged it follows that GEPP has a cond-bounded forward error if $\operatorname{cond}(L^T)$ is of order 1. With a suitable scaling it is possible to do even better. Skeel [1040, 1979] shows that for $D_1 = \mathrm{diag}(|A||x|)^{-1}$ , GEPP on $A$ is backward stable in the componentwise relative sense, and hence a forward error bound proportional to $\operatorname{cond}(A,x) = \| |A^{-1}||A||x||_{\infty} / ||x||_{\infty}$ holds; the catch is, of course, that the scaling depends on the unknown solution $x!$ Row equilibration can be regarded as approximating $x$ by $e$ in this "optimal" scaling.

Despite the variety of possible scalings and pivoting strategies and the catalogue of situations in which a particular pivoting strategy may have a smaller error bound than the usual theory predicts, in practice general linear systems are virtually always solved by unscaled GEPP. There are three main reasons:

1. Most users of GEPP feel that it performs well in practice.

2. GEPP has a long history of use in software libraries and packages (see page 188), and inertia makes it difficult to replace it. (For example, the LINPACK and LAPACK LU factorization routines use partial pivoting. LINPACK does not include scaling, while LAPACK's GEPP driver routine xGESVX offers an initial scaling as an option.)

3. A $\operatorname{cond}(A, x)$ -bounded forward error and a small componentwise relative backward error are both achieved by following GEPP with fixed precision iterative refinement (under mild assumptions); see §12.2.

This last point explains why scaling, rook pivoting, and complete pivoting are not popular with numerical analysts for general linear systems. None of these techniques, with the exception of Skeel's optimal but implicitly defined scaling, guarantees a small componentwise relative backward error. Yet fixed precision refinement as a supplement to GEPP yields this ideal form of stability whenever it can reasonably be expected to and at negligible cost.

Some programs for GEPP incorporate row scaling implicitly. They compute row scale factors $d_{1}, \ldots, d_{n}$ , but, instead of applying GEPP to $\mathrm{diag}(d_{i})^{-1} \times A$ , they apply it to $A$ and choose as pivot row at the $k$ th stage a row $r$ for which $d_{r}|a_{rk}^{(k)}|$ is maximal. This type of scaling has the sole effect of influencing the choice of pivots. There is little justification for using it, and the best bound for the growth factor is $2^{n-1}$ multiplied by a product of terms $d_{i_{1}} / d_{i_{2}}$ that can be large.

There is, however, one situation in which a form of implicit row scaling is beneficial. Consider the pivoting strategy that selects as the $k$ th pivot an element $a_{rk}^{(k)}$ for which

$$
\frac {\left| a _ {r k} ^ {(k)} \right|}{\left\| A ^ {(k)} (r , k : n) \right\| _ {\infty}} = \max  _ {i \geq k} \frac {\left| a _ {i k} ^ {(k)} \right|}{\left\| A ^ {(k)} (i , k : n) \right\| _ {\infty}}. \tag {9.25}
$$

A result of Peña [932, 1996] shows that if there exists a permutation matrix $P$ such that $PA$ has an LU factorization $PA = LU$ with $|PA| = |L||U|$ , then such a factorization will be produced by the pivoting scheme (9.25). This means that, unlike for partial pivoting, we can use the pivoting scheme (9.25) with impunity on totally nonnegative matrices and their inverses, row permutations of such matrices, and any matrix for which some row permutation has the “ $|PA| = |L||U|$ ” property. However, this pivoting strategy is as expensive as complete pivoting to implement, and for general $A$ it is not guaranteed to produce a factorization as stable as that produced by partial pivoting.

# 9.9. Variants of Gaussian Elimination

Some variants of GE and partial pivoting have been proposed, mainly motivated by parallel computing and the aim of avoiding the sequential search down a column required by partial pivoting.

One idea is, at each element-zeroing step of GE, to interchange (if necessary) the pivot row and the row whose first element is to be zeroed to ensure that the multiplier is bounded by 1. In one particular algorithm, the first stage introduces zeros into elements $(2,1)$ , $(3,1)$ , ..., $(n,1)$ , in this order, and the potential row interchanges are $1 \leftrightarrow 2$ , $1 \leftrightarrow 3$ , ..., $1 \leftrightarrow n$ , instead of just one row interchange as for partial pivoting. As well as saving on the pivot searching, this method has the advantage of permitting eliminations to be performed in parallel. For a $6 \times 6$ matrix we can represent the elimination as follows, where an integer $k$ denotes

elements that can be eliminated in parallel on the $k$ th stage:

$$
\left[ \begin{array}{c c c c c c} x & x & x & x & x & x \\ 1 & x & x & x & x & x \\ 2 & 3 & x & x & x & x \\ 3 & 4 & 5 & x & x & x \\ 4 & 5 & 6 & 7 & x & x \\ 5 & 6 & 7 & 8 & 9 & x \end{array} \right].
$$

In general, there are $2n - 3$ stages in each of which up to $n / 2$ elements are eliminated in parallel. This algorithm is discussed by Wilkinson [1233, 1965, pp. 236-237] and Gallivan, Plemmons, and Sameh [452, 1990]. Sorensen [1057, 1985] derives a backward error bound for the factorization that is proportional to $4^n$ which, roughly, comprises a factor $2^{n - 1}$ bounding the growth factor and a factor $2^{n - 1}$ bounding “ $L$ ”.

Another variant of GE is pairwise elimination, in which all row operations and row interchanges are between pairs of adjacent rows only. This method is discussed by Trefethen and Schreiber [1157, 1990] and is called Neville elimination by Gasca and Peña [461, 1992], who apply it to totally positive matrices. An error analysis of the method is given in [13, 1997].

Yet another idea is to avoid row interchanges altogether by adding plus or minus the row chosen by partial pivoting to the natural pivot row, thus ensuring that the multipliers are all bounded by 1. Mead, Renault, and Welfert [838, 2001] show that the growth factor for this modified form of GEPP is bounded by $3^{n-1}$ , and that this bound is nearly attainable.

# 9.10. A Posteriori Stability Tests

Having solved a linear system by LU factorization we can compute the componentwise or normwise backward error at the cost of evaluating one or two matrix-vector products (see Theorems 7.1 and 7.3). In some situations, though, we may wish to assess the stability of a computed LU factorization before using it to solve one or more linear systems. One possibility is to compute the growth factor by monitoring the size of elements during the elimination, at a cost of $O(n^3)$ comparisons. This has been regarded as rather expensive, and more efficient ways to estimate $\rho_n$ have been sought.

Businger [188, 1971] describes a way to obtain an upper bound for $\rho_{n}$ in $O(n^{2})$ operations. This approach is generalized by Erisman and Reid [393, 1974], who apply the Hölder inequality to the equation

$$
a _ {i j} ^ {(k + 1)} = a _ {i j} - \sum_ {r = 1} ^ {k} l _ {i r} u _ {r j}, \quad i, j > k,
$$

to obtain the bound

$$
\begin{array}{l} \left| a _ {i j} ^ {(k + 1)} \right| \leq \left| a _ {i j} \right| + \left\| \left(l _ {i 1}, \dots , l _ {i k}\right) \right\| _ {p} \left\| \left(u _ {1 j}, \dots , u _ {k j}\right) \right\| _ {q} \\ \leq \max  _ {i, j} | a _ {i j} | + \max  _ {i} \| (l _ {i 1}, \dots , l _ {i, i - 1}) \| _ {p} \max  _ {j} \| (u _ {1 j}, \dots , u _ {j - 1, j}) \| _ {q}, \tag {9.26} \\ \end{array}
$$

where $p^{-1} + q^{-1} = 1$ . In practice, $p = 1,2,\infty$ are the values of interest. Barlow [69, 1986] notes that application of the Hölder inequality instead to

$$
a _ {i j} ^ {(k + 1)} = \sum_ {r = k + 1} ^ {\min  (i, j)} l _ {i r} u _ {r j}
$$

yields a sometimes sharper bound.

It is interesting to note that in light of experience with the bound (9.26), Reid [980, 1987] recommends computing the growth factor explicitly in the context of sparse matrices, arguing that the expense is justified because (9.26) can be a very weak bound. See Erisman et al. [392, 1987] for some empirical results on the quality of the bound.

Chu and George [235, 1985] observe that the $\infty$ -norm of the matrix $|\widehat{L}||\widehat{U}|$ can be computed in $O(n^{2})$ operations without forming the matrix explicitly, since

$$
\parallel | \widehat {L} | | \widehat {U} | \parallel_ {\infty} = \parallel | \widehat {L} | | \widehat {U} | e \parallel_ {\infty} = \parallel | \widehat {L} | (| \widehat {U} | e) \parallel_ {\infty}.
$$

Thus one can cheaply compute a bound on $\| \varDelta A\|_{\infty}$ from the componentwise backward error bounds in (9.6) and (9.7).

All the methods discussed in this section make use of an a priori error analysis to compute bounds on the backward error. Because the bounds do not take into account the statistical distribution of rounding errors, and because they involve somewhat pessimistic constant terms, they cannot be expected to be very sharp. Thus it is important not to forget that it is straightforward to compute the backward error itself: $A - \widehat{L}\widehat{U}$ . Exact computation costs a prohibitively expensive $O(n^{3})$ operations, but $\| A - \widehat{L}\widehat{U}\|_{1}$ can be estimated in $O(n^{2})$ operations using the matrix norm estimator in Algorithm 15.4. Another possibility is to use a running error analysis, in which an error bound is computed concurrently with the factors (see §3.3).

# 9.11. Sensitivity of the LU Factorization

Although Theorem 9.3 bounds the backward error of the computed LU factors $\widehat{L}$ and $\widehat{U}$ , it does not give any indication about the size of the forward errors $L - \widehat{L}$ and $U - \widehat{U}$ . For most applications of the LU factorization it is the backward error and not the forward errors that matters, but it is still of some interest to know how big the forward errors can be. This is a question of perturbation theory and is answered by the next result.

Theorem 9.15 (Barrlund, Sun). Let the nonsingular matrices $A \in \mathbb{R}^{n \times n}$ and $A + \Delta A$ have LU factorizations $A = LU$ and $A + \Delta A = (L + \Delta L)(U + \Delta U)$ , and assume that $\| G \|_2 < 1$ , where $G = L^{-1} \Delta AU^{-1}$ . Then

$$
\max  \left\{\frac {\| \Delta L \| _ {F}}{\| L \| _ {2}}, \frac {\| \Delta U \| _ {F}}{\| U \| _ {2}} \right\} \leq \frac {\| G \| _ {F}}{1 - \| G \| _ {2}} \leq \frac {\| L ^ {- 1} \| _ {2} \| U ^ {- 1} \| _ {2} \| A \| _ {2}}{1 - \| L ^ {- 1} \| _ {2} \| U ^ {- 1} \| _ {2} \| \Delta A \| _ {2}} \frac {\| \Delta A \| _ {F}}{\| A \| _ {F}}. \tag {9.27}
$$

Moreover, if $\rho(|\widetilde{G}|) < 1$ , where $\widetilde{G} = (L + \Delta L)^{-1}\Delta A(U + \Delta U)^{-1}$ , then

$$
\begin{array}{l} \left| \Delta L \right| \leq \left| L + \Delta L \right| \operatorname {s t r i l} \left(\left(I - | \widetilde {G} |\right) ^ {- 1} | \widetilde {G} |\right), \\ \left| \Delta U \right| \leq \operatorname {t r i u} \left(\left| \widetilde {G} \right| \left(I - \left| \widetilde {G} \right|\right) ^ {- 1}\right) \left| U + \Delta U \right|, \\ \end{array}
$$

where $\operatorname{stril}(\cdot)$ and $\operatorname{triu}(\cdot)$ denote, respectively, the strictly lower triangular part and the upper triangular part of their matrix arguments.

The normwise bounds (9.27) imply that $\chi(A) \coloneqq \|L^{-1}\|_2\|U^{-1}\|_2\|A\|_2$ is an upper bound for the condition numbers of $L$ and $U$ under normwise perturbations. We have

$$
\kappa_ {2} (A) \leq \chi (A) \leq \min  \left\{\kappa_ {2} (L), \kappa_ {2} (U) \right\} \kappa_ {2} (A),
$$

and the ratio $\chi(A) / \kappa_2(A)$ can be arbitrarily large (though if partial pivoting is used then $\kappa_2(L) \leq n 2^{n-1}$ ).

The componentwise bounds in Theorem 9.15 are a little unsatisfactory in that they involve the unknown matrices $\Delta L$ and $\Delta U$ , but we can set these terms to zero and obtain a bound correct to first order.

# 9.12. Rank-Revealing LU Factorizations

In many applications it is useful to have a factorization of a matrix that "reveals the rank". In exact arithmetic, a factorization produced by GE with pivoting is certainly rank-revealing if it has the form

$$
P A Q = \mathbf {\Pi} _ {n - r} ^ {r} \left[ \begin{array}{c c} L _ {1 1} & n - r \\ L _ {2 1} ^ {T} & I \end{array} \right] \left[ \begin{array}{c c} R & n - r \\ U _ {1 1} & U _ {1 2} \\ 0 & 0 \end{array} \right] \mathbf {\Pi} _ {n - r} ^ {r},
$$

with $L_{11}$ and $U_{11}$ nonsingular. It is easy to see that GE without pivoting or with partial pivoting does not in general produce such a factorization, but GE with rook pivoting or complete pivoting does. Formulating a definition of rank-revealing LU factorization for matrices that are not exactly rank-deficient is nontrivial, and there are several possible approaches. We will use the general definition of Demmel et al. [323, 1999] that a rank-revealing decomposition (RRD) of $A \in \mathbb{R}^{m \times n}$ is a factorization $A = X D Y^T$ , where $X \in \mathbb{R}^{m \times r}$ , $D \in \mathbb{R}^{r \times r}$ , and $Y \in \mathbb{R}^{n \times r}$ , with $r \leq \min(m, n)$ , $D$ diagonal and nonsingular, and $X$ and $Y$ well conditioned. An RRD therefore concentrates the rank deficiency and ill condition of $A$ into the diagonal matrix $D$ . The existence of an RRD is clear, because the SVD is one (see §6.4).

Our interest here is in to what extent LU factorization with pivoting produces an RRD. If $PAQ = LU$ is an LU factorization with pivoting and $A$ is nonsingular (but possibly ill conditioned) then we can take $X = L$ , $D = \mathrm{diag}(U)$ and $Y^T = D^{-1}U$ . With no pivoting or with partial pivoting, $Y^T$ can be an arbitrary upper triangular matrix and so an RRD is not obtained in general. With rook pivoting or complete pivoting $X$ and $Y^T$ are both unit triangular with off-diagonal elements bounded by 1 and hence

$$
\kappa_ {\infty} (X), \kappa_ {\infty} (Y) \leq n 2 ^ {n - 1}.
$$

Moreover, in practice $X$ and $Y$ tend to be much better conditioned than these bounds suggest. Therefore GE with rook pivoting or complete pivoting is a means of computing an RRD, but with the remote possibility of failing to satisfy the definition by factors of order $2^n$ . This worst case is achievable. For the matrix $A(\theta) = U_n(\theta)^T U_n(\theta)$ , where $U_n(\theta)$ is the Kahan matrix in (8.11), for small $\theta > 0$ we have $r = n$ and $\kappa_2(X) = \kappa_2(Y) \approx 2^{n-1}$ .

Pan [914, 2000] shows the existence of a (guaranteed) RRD based on LU factorization and gives an algorithm for computing one that begins by computing an LU factorization with complete pivoting.

# 9.13. Historical Perspective

GE was the first numerical algorithm to be subjected to rounding error analysis, so it is instructive to follow the development of the error analysis from its beginnings in the 1940s.

In the 1940s there were three major papers giving error analyses of GE. Hotelling [639, 1943] presented a short forward error analysis of the LU factorization stage of GE. Under the assumptions that $|a_{ij}| \leq 1$ and $|b_i| \leq 1$ for all $i$ and $j$ and that the pivots are all of modulus unity, Hotelling derives a bound containing a factor $4^{n-1}$ for the error in the elements of the reduced upper triangular system. Hotelling's work was quoted approvingly by Bargmann, Montgomery, and von Neumann [64, 1946], who dismiss elimination methods for the solution of a linear system $Ax = b$ as being numerically unstable. Instead, they recommend computation of $A^{-1}$ via the Newton-Schulz iteration described in §14.5 (which was also discussed by Hotelling). In one paragraph they outline the alleged shortcomings of elimination methods as follows:

In the elimination method a series of $n$ compound operations is performed each of which depends on the preceding. An error at any stage affects all succeeding results and may become greatly magnified; this explains roughly why instability should be expected. It should be noticed that at each step a division is performed by a number whose size cannot be estimated in advance and which might be so small that any error in it would be greatly magnified by division. In fact such small divisors must occur if the determinant of the matrix is small and may occur even if it is not ... Another reason to expect instability is that once the variable $x_{n}$ is obtained all the other variables are expressed in terms of it.

As Wilkinson [1242, 1974, p. 354] notes of this paragraph, "almost every statement in it is either wrong or misleading".

Hotelling's result led to general pessimism about the practical effectiveness of GE for solving large systems of equations. Three papers published later in the same decade, as well as growing practical experience with the method, helped to restore confidence in GE.

Goldstine [499, 1972, p. 290] says of his discussions with von Neumann:

We did not feel it reasonable that so skilled a computer as Gauss would have fallen into the trap that Hotelling thought he had noted ... Von

Neumann remarked one day that even though errors may build up during one part of the computation, it was only relevant to ask how effective is the numerically obtained solution, not how close were some of the auxiliary numbers, calculated on the way to their correct counterparts. We sensed that at least for positive definite matrices the Gaussian procedure could be shown to be quite stable.

von Neumann and Goldstine [1200, 1947] subsequently gave a long and difficult rigorous fixed-point error analysis for the inversion of a symmetric positive definite matrix $A$ via GE. They showed that the computed inverse $\widehat{X}$ satisfies $\| A\widehat{X} - I \|_2 \leq 14.2n^2 u\kappa_2(A)$ . Parlett [925, 1990] explains that "the joy of this result was getting a polynomial in $n$ , and the pain was obtaining 14.2, a number that reflects little more than the exigencies of the analysis." Wilkinson [1239, 1971] gives an interesting critique of von Neumann and Goldstine's paper and points out that the residual bound could hardly be improved using modern error analysis techniques. In a later paper [501, 1951], Goldstine and von Neumann gave a probabilistic analysis, which Goldstine summarizes as showing that "under reasonable probabilistic assumptions the error estimates of the previous paper could be reduced from a proportionality of $n^2$ to $n$ " [499, 1972, p. 291].

In his 1970 Turing Award Lecture [1240, 1971], Wilkinson recounts how in the early 1940s he solved a system of 12 linear equations on a desk calculator, obtaining a small residual. He goes on to describe a later experience:

It happened that some time after my arrival [at the National Physical Laboratory in 1946], a system of 18 equations arrived in Mathematics Division and after talking around it for some time we finally decided to abandon theorizing and to solve it ... The operation was manned by Fox, Goodwin, Turing, and me, and we decided on Gaussian elimination with complete pivoting ... Again the system was mildly ill-conditioned, the last equation had a coefficient of order $10^{-4}$ (the original coefficients being of order unity) and the residuals were again of order $10^{-10}$ , that is of the size corresponding to the exact solution rounded to ten decimals. It is interesting that in connection with this example we subsequently performed one or two steps of what would now be called "iterative refinement," and this convinced us that the first solution had had almost six correct figures.

(Fox [439, 1987] notes that the computation referred to in this quotation took about two weeks using desk computing equipment!) In a subsequent paper, Fox, Huskey, and Wilkinson [440, 1948] presented empirical evidence in support of GE, commenting that "in our practical experience on matrices of orders up to the twentieth, some of them very ill-conditioned, the errors were in fact quite small".

The experiences of Fox, Huskey, and Wilkinson prompted Turing to write a remarkable paper "Rounding-off errors in matrix processes" [1166, 1948]. In this paper, Turing made several important contributions. He formulated the LU (actually, the LDU) factorization of a matrix, proving the "if" part of Theorem 9.1 and showing that GE computes an LDU factorization. He introduced the term "condition number" and defined two matrix condition numbers, one of which is $n^{-1}N(A)N(A^{-1})$ , where $N(A) = \| A\|_F$ , the " $N$ -condition number of $A$ " . He used

Table 9.2. Times for solution of a linear system of order $n$ .   

<table><tr><td>Machine</td><td>Year</td><td>n</td><td>Time</td><td>Reference</td></tr><tr><td>Logarithm tables</td><td>c. 1884</td><td>29a</td><td>7 weeks</td><td>[1076, 1995]</td></tr><tr><td>Desk computing equipment</td><td>c. 1946</td><td>18</td><td>2 weeks</td><td>[439, 1987]</td></tr><tr><td>Harvard Mark 1</td><td>1947</td><td>10</td><td>45 minutes</td><td>b</td></tr><tr><td>IBM 602 Calculating Punch</td><td>1949</td><td>10</td><td>4 hours</td><td>[1195, 1949]</td></tr><tr><td>Pilot ACE</td><td>1951</td><td>17</td><td>over 3 hours</td><td>[1254, 1958]</td></tr><tr><td>Pilot ACEc</td><td>1954</td><td>30</td><td>11/2mins</td><td>[1254, 1958]</td></tr><tr><td>ACE</td><td>1958</td><td>30</td><td>5 seconds</td><td>[1254, 1958]</td></tr><tr><td>EDSAC 2</td><td>1960</td><td>31</td><td>4 seconds</td><td>[83, 1960]</td></tr><tr><td>EDSAC 2d</td><td>1960</td><td>100</td><td>7 minutes</td><td>[83, 1960]</td></tr></table>

${}^{a}$ Symmetric positive definite system.   
$^b$ [142, 1948, p. 27], [552, 1948, p. 336].   
cWith magnetic drum store.   
${}^{d}$ Using magnetic tape for auxiliary storage.

the word "preconditioning" to mean improving the condition of a system of linear equations (a term that did not come into popular use until the 1970s). He described iterative refinement for linear systems. He exploited backward error ideas, for example by noting that "the triangular resolution obtained is an exact resolution of a matrix $A - S$ , where $M(S) < \epsilon$ " ( $M(S) \coloneqq \max_{i,j} |s_{ij}|$ ). Finally, and perhaps most importantly, he analysed GEPP for general matrices and obtained a bound for $\| x - \widehat{x} \|_{\infty}$ that contains a term proportional to $\| A^{-1} \|_{\infty}^2$ . (By making a trivial change in the analysis, namely replacing $A^{-1} b$ by $x$ , Turing's bound can be made proportional only to $\| A^{-1} \|_{\infty}$ .) Turing also showed that the factor $4^{n-1}$ in Hotelling's bound can be improved to $2^{n-1}$ and that still the bound is attained only in exceptional cases.

In a review of Turing's paper, Bodewig [144, 1949] described the error bounds as "impractical" and advocated computing the residual of the computed solution and then determining "the exact correction by solving a new system." That another researcher could miss the point of Turing's analysis emphasizes how new the concept of rounding error analysis was in the 1940s.

Table 9.2 shows the time for solution of linear systems by GE on some early computing devices. The performance of modern computers on two linear system benchmarks is summarized by Dongarra [346, 2001] in a report that is regularly updated.

Douglas [353, 1959] presented a forward error analysis for GE applied to diagonally dominant tridiagonal systems arising in the solution of the heat equation by finite differences. He concluded that the whole procedure of solving this partial differential equation "is stable against round-off error". It is surprising that Douglas' paper is little known, because irrespective of the fact that his analysis can be simplified and clarified using modern techniques, his is one of the first truly positive rounding error results to be published.

A major breakthrough in the error analysis of GE came with Wilkinson's pioneering backward error analysis, in which he proved Theorem 9.5 [1229, 1961],

[1232, 1963]. Apart from its simplicity and elegance and the realistic nature of the bounds, the main feature that distinguishes Wilkinson's analysis from the earlier error analyses of GE is that it bounds the normwise backward error rather than the forward error.

Wilkinson had been aware of the properties of the growth factor for partial pivoting long before developing his backward error analysis. In a 1954 paper [1225, 1954] he noted that

After $m$ reductions the largest element is at most $2^m$ times as large as the largest original coefficient. It is possible to construct sets in which this factor is achieved but in practice an increase seldom takes place; more frequently the coefficients become progressively smaller, particularly if the equations are ill-conditioned.

This quote summarizes most of what we know today!

Four of the first textbooks to incorporate Wilkinson's analysis were those of Fox [436, 1964, pp. 161-174], Isaacson and Keller [667, 1966], Wendroff [1215, 1966], and Forsythe and Moler [431, 1967, Chap. 21]. Fox gives a simplified analysis for fixed-point arithmetic under the assumption that the growth factor is of order 1. Forsythe and Moler give a particularly readable backward error analysis that has been widely quoted.

Wilkinson's 1961 result is essentially the best that can be obtained by a normwise analysis. Subsequent work in error analysis for GE has mainly been concerned with bounding the backward error componentwise, as in Theorems 9.3 and 9.4. We note that Wilkinson could have given a componentwise bound for the backward perturbation $\Delta A$ , since most of his analysis is at the element level.

Chartres and Geuder [223, 1967] analyse the Doolittle version of GE. They derive a backward error result $(A + \Delta A)\widehat{x} = b$ , with a componentwise bound on $\Delta A$ ; although they do not recognize it, their bound can be written in the form $|\Delta A| \leq c_n u |\widehat{L}| |\widehat{U}|$ .

Reid [979, 1971] shows that the assumption in Wilkinson's analysis that partial pivoting or complete pivoting is used is unnecessary. Without making any assumptions on the pivoting strategy, he derives for LU factorization the result $\widehat{L}\widehat{U} = A + \varDelta A$ , $|\varDelta a_{ij}|\leq 3.01\min (i - 1,j)u\max_k|a_{ij}^{(k)}|$ . Again, this is a componentwise bound. Erisman and Reid [393, 1974] note that for a sparse matrix, the term $\min (i - 1,j)$ in Reid's bound can be replaced by $m_{ij}$ , where $m_{ij}$ is the number of multiplications required in the calculation of $l_{ij}$ ( $i > j$ ) or $u_{ij}$ ( $i\leq j$ ).

de Boor and Pinkus [300, 1977] give the result stated in Theorem 9.4. They refer to the original German edition [1085, 1972] of [1086, 1980] for a proof of the result and explain several advantages to be gained by working with a componentwise bound for $\Delta A$ , one of which is the strong result that ensues for totally nonnegative matrices. A result very similar to Theorem 9.4 is proved by Sautter [1012, 1978].

Skeel [1040, 1979] carried out a detailed componentwise error analysis of GE with a different flavour to the analysis given in this chapter. His aim was to understand the numerical stability of GE (in a precisely defined sense) and to determine the proper way to scale a system by examining the behaviour of the backward and forward errors under scaling (see §9.8). He later used this analysis to de

rive important results about fixed precision iterative refinement (see Chapter 12). Skeel's work popularized the use of componentwise backward error analysis and componentwise perturbation theory.

The “ $|\widehat{L}||\widehat{U}''$ ” componentwise style of backward error analysis for GE has been well known for some time, as evidenced by its presence in the textbooks of Conte and de Boor [264, 1980], Golub and Van Loan [509, 1996] (also the 1983 first edition), and Stoer and Bulirsch [1086, 1980].

Forward error analyses have also been done for GE. The analyses are more complicated and more difficult to interpret than the backward error analyses. Olver and Wilkinson [906, 1982] derive a posteriori forward error bounds that require the computation of $A^{-1}$ . Further results are given in a series of papers by Stummel [1096, 1982], [1097, 1985], [1098, 1985], [1099, 1985].

# 9.14. Notes and References

A variant of GE was used by the Chinese around the first century AD; the Jiu Zhang Suanshu (Nine Chapters of the Mathematical Art) contains a worked example for a system of five equations in five unknowns [680, 1991, pp. 156-177], [776, 1989].

Gauss, who was a great statistician and numerical analyst, developed his elimination method as a tool to help him prove results in linear regression theory. The first published appearance of GE is in his Theoria Motus (1809). Stewart [1076, 1995] gives a survey of Gauss's work on solving linear systems; see also the afterword in [463, 1995].

The traditional form of GE, as given at the start of this chapter, can be expressed algorithmically as

for $k = 1$ : $n$ for $j = k + 1$ : $n$ for $i = k + 1$ : $n$ $a_{ij} = a_{ij} - (a_{ik} / a_{kk})a_{kj}$ end  
end

This is identified as the $kji$ form of GE. Altogether there are six possible orderings of the three loops. Doolittle's method (Algorithm 9.2) is the $ijk$ or $jik$ variant of Gaussian elimination. The choice of loop ordering does not affect the stability of the computation, but can greatly affect the efficiency of GE on a high-performance computer. For more on the different loop orderings of GE see Chapter 13; Dongarra, Gustavson, and Karp [344, 1984]; and the books by Dongarra, Duff, Sorensen, and van der Vorst [349, 1998] and Golub and Van Loan [509, 1996].

This chapter draws on the survey paper by Higham [593, 1990]. Theorems 9.7 and 9.8 are from Higham and Higham [616, 1989].

Myrick Hascall Doolittle (1830-1913) was a "computer of the United States coast and geodetic survey" [402, 1987]. Crout's method was published in an engineering journal in 1941 [281, 1941].

GE and its variants were known by various descriptive names in the early days of computing. These include the bordering method, the escalator method (for matrix inversion), the square root method (Cholesky factorization), and pivotal condensation. A good source for details of these methods is Faddeeva [399, 1959].

In a confidential 1948 report that "covers the general principles of both the design of the [Automatic Computing Engine] and the method of programming adopted for it", Wilkinson gives a program implementing GE with partial pivoting and iterative refinement [1224, 1948, p. 111]. This was probably the first such program to be written—and for a machine that had not yet been built!

The terms "partial pivoting" and "complete pivoting" were introduced by Wilkinson in [1229, 1961]. The pivoting techniques themselves were in use in the 1940s and it is not clear who, if anyone, can be said to have invented them; indeed, von Neumann and Goldstine [1200, 1947, §4.2] refer to complete pivoting as the "customary procedure".

Complete pivoting is currently used in several situations where the benefits it brings clearly outweigh the extra cost. It is used in LAPACK routine xLASY2 for solving Sylvester equations of dimensions 1 or 2 (see §16.6.1 and the solution to Problem 16.4) and in certain computations involving the generalized Schur decomposition. It is also used for computing a rank-revealing decomposition (see §9.12), for example as a first step in computing an accurate singular value decomposition; see Demmel et al. [323, 1999].

Rook pivoting for nonsymmetric matrices was introduced by Neal and Poole in [880, 1992]; see also [947, 2000]. Related pivoting strategies for symmetric indefinite matrices were introduced earlier by Fletcher [415, 1976] and subsequently by Ashcraft, Grimes, and Lewis [38, 1998]; see §11.1.3. Given the practical effectiveness of partial pivoting it is unlikely that rook pivoting will ever gain popular use for nonsymmetric matrices, and when the strongest possible guarantee of stability is required complete pivoting will always be preferred. Rook pivoting may find a niche for computing rank-revealing decompositions, since it is clearly better than partial pivoting for this purpose and no worse than complete pivoting in the worst case. For symmetric matrices rook pivoting-like strategies have additional advantages that make them of great practical interest; see §11.1.3.

There is a long history of published programs for GE, beginning with Crout routines of Forsythe [425, 1960], Thacher [1134, 1961], McKeeman [836, 1962], and Bowdler, Martin, Peters, and Wilkinson [154, 1966], all written in Algol 60 (which was the "official" language for publishing mathematical software in the 1960s and a strong competitor to Fortran for practical use at that time). The GE routines in LAPACK are the latest in a lineage beginning with the Fortran routines decomp and solve in Forsythe and Moler's book [431, 1967], and continuing with routines by Moler [860, 1972], [861, 1972] (which achieve improved efficiency in Fortran by accessing arrays by column rather than by row), Forsythe, Malcolm, and Moler [430, 1977] (these routines incorporate condition estimation—see Chapter 15), and LINPACK [341, 1979].

LU factorization of totally nonnegative matrices has been investigated by Cryer [283, 1973], [284, 1976], Ando [26, 1987], and de Boor and Pinkus [300, 1977]. It is natural to ask whether we can test for total nonnegativity without computing all the minors. The answer is yes: for an $n \times n$ matrix total nonnegativity can be

tested in $O(n^{3})$ operations, by testing the signs of the pivots in suitable elimination schemes, as shown by Cryer [284, 1976] and Gasca and Peña [461, 1992]. The latter paper employs Neville (pairwise) elimination (see §9.9). Note the analogy with positive definiteness, which holds for a symmetric matrix if and only if all the pivots in GE are positive. For an insightful survey of totally nonnegative matrices see Fallat [400, 2001].

The dilemma of whether to define the growth factor in terms of exact or computed quantities is faced by all authors; most make one choice or the other, and go on to derive, without comment, bounds that are strictly incorrect. Theorem 9.9, for example, bounds the exact growth factor; the computed one could conceivably violate the bound, but only by a tiny relative amount. van Veldhuizen [1184, 1977] shows that for a variation of partial pivoting that allows either a row or column interchange at each stage, the growth factor defined in terms of computed quantities is at most about $(1 + 3nu)2^{n - 1}$ , compared with the bound $2^{n - 1}$ for the exact growth factor.

The idea of deriving error bounds for GE by analysing the equations obtained by solving $A = LU$ is exploited by Wilkinson [1241, 1974], who gives a general analysis that includes Cholesky factorization. This paper gives a concise summary of error analysis of factorization methods for linear equations and least squares problems.

Various authors have tabulated growth factors in extensive tests with random matrices. In tests during the development of LINPACK, the largest value observed was $\rho_{40}^{p} = 23$ , occurring for a random matrix of 1s, 0s, and -1s [341, 1979, p. 1.21]. Macleod [803, 1989] recorded a value $\rho_{100}^{p} = 35.1$ , which occurred for a symmetric matrix with elements from the uniform distribution on $[-1,1]$ . In one MATLAB test of 100,000 matrices of dimension 100 from the normal $N(0,1)$ distribution, I found the largest growth factor to be $\rho_{n}^{p} = 20.12$ .

Gould [513, 1991] used the optimization LANCELOT [263, 1992] to maximize the $n$ th pivot for complete pivoting as a function of about $n^3 / 3$ variables comprising the intermediate elements $a_{ij}^{(k)}$ of the elimination; constraints were included that normalize the matrix $A$ , describe the elimination equations, and impose the complete pivoting conditions. Gould's package found many local maxima, and many different starting values had to be tried in order to locate the matrix for which $\rho_{13}^{c} > 13$ . In an earlier attempt at maximizing the growth factor, Day and Peterson [299, 1988] used a problem formulation in which the variables are the $n^2$ elements of $A$ , which makes the constraints and objective function substantially more nonlinear than in Gould's formulation. Using the package NPSOL [484, 1986], they obtained "largest known" growth factors for $5 \leq n \leq 7$ .

Theoretical progress into understanding the behaviour of the growth factor for complete pivoting has been made by Day and Peterson [299, 1988], Puschmann and Cortes [960, 1983], Puschmann and Nordio [961, 1985], and Edelman and Mascarenhas [382, 1995].

Probabilistic error analysis for GE is given by Barlow and Bareiss [73, 1985]. Yeung and Chan [1265, 1997] give a probabilistic analysis of GE without pivoting, obtaining the distributions of the entries of $L$ and $U$ for matrices from the normal $N(0,1)$ distribution.

Barlow and Zha [77, 1998] consider an alternative definition of growth factor,

$\rho_{n} = \max_{k}\| A^{(k)}\|_{2} / \| A\|_{2}$ . They show that the maximum value of this growth factor for partial pivoting is about $2^{n} / 3$ and that the maximum is attained at an orthogonal matrix.

A novel alternative to partial pivoting for stabilizing GE is proposed by Stewart [1066, 1974]. The idea is to modify the pivot element to make it suitably large, and undo this rank one change later using the Sherman-Morrison formula. Stewart gives error analysis that bounds the backward error for this modified form of GE.

Wilkinson proved Theorem 9.9 for matrices diagonally dominant by columns [1229, 1961, pp. 288-289]. Theorem 9.10 is proved in the same paper. That $\rho_{n} \leq 2$ for matrices diagonally dominant by rows does not appear to be well known, but it is proved by Wendroff [1215, 1966, pp. 122-123], for example.

In Theorem 9.9 it is assumed that $A$ is nonsingular. It has long been known (and frequently rediscovered) that diagonal dominance provides sufficient conditions for nonsingularity: if a matrix is diagonally dominant with strict inequalities in all the defining inequalities, or if it is irreducible and at least one of the inequalities is strict, then the matrix is nonsingular [908, 1972, Thm. 6.2.6], [1190, 1976].

The results in §9.6 for tridiagonal matrices are taken from Higham [589, 1990]. Another method for solving tridiagonal systems is cyclic reduction, which was developed in the 1960s [190, 1970]. Error analysis given by Amodio and Mazzia [18, 1994] shows that cyclic reduction is normwise backward stable for diagonally dominant tridiagonal matrices.

The chapter "Scaling Equations and Unknowns" of Forsythe and Moler [431, 1967] is a perceptive, easy-to-understand treatment that is still well worth reading. Early efforts at matrix scaling for GE were directed to equilibrating either just the rows or the rows and columns simultaneously (so that all the rows and columns have similar norms). An algorithm with the latter aim is described by Curtis and Reid [286, 1972]. Other important references on scaling are the papers by van der Sluis [1177, 1970] and Stewart [1069, 1977], which employ normwise analysis, and those by Skeel [1040, 1979], [1042, 1981], which use componentwise analysis.

Much is known about the existence and stability of LU factorizations of $M$ -matrices and related matrices. $A$ is an $H$ -matrix if the comparison matrix $M(A)$ (defined in (8.7)) is an $M$ -matrix. Funderlic, Neumann, and Plemmons [449, 1982] prove the existence of an LU factorization for an $H$ -matrix $A$ that is generalized diagonally dominant, that is, $DA$ is diagonally dominant by columns for some nonsingular diagonal matrix $D$ ; they show that the growth factor satisfies $\rho_n \leq 2\max_i |d_{ii}| / \min_i |d_{ii}|$ . Neumann and Plemmons [886, 1984] obtain a growth factor bound for an inverse of an $H$ -matrix. Ahac, Buoni, and Olesky [8, 1988] describe a novel column-pivoting scheme for which the growth factor can be bounded by $n$ when $A$ is an $H$ -matrix; for more general related work see Peña [933, 1998].

The normwise bounds in Theorem 9.15 are due to Barrlund [81, 1991] and the componentwise ones to Sun [1103, 1992]. Similar bounds are given by Stewart [1075, 1993] and Sun [1104, 1992]. Perturbation bounds that can be much smaller than the normwise one in Theorem 9.15 are obtained by Chang and Paige [218, 1998] and Stewart [1078, 1997].

Interval arithmetic techniques (see §26.4) are worth considering if high accuracy

Table 9.3. Records for largest dense linear systems solved (dimension $n$ ).   

<table><tr><td>Year</td><td>n</td><td>Computer</td><td>Time</td></tr><tr><td>1991</td><td>55,296</td><td>Connection Machine CM-2</td><td>4.4 days</td></tr><tr><td>1992/3</td><td>75,264</td><td>Intel iPSC/860</td><td>2 2/3 days</td></tr><tr><td>1994</td><td>76,800</td><td>Connection Machine CM-5</td><td>4.1 days</td></tr><tr><td>1995</td><td>128,600</td><td>Intel Paragon</td><td>≈1 hour</td></tr><tr><td>1996</td><td>138,240</td><td>Hitachi SR2201/1024</td><td>2.2 hours</td></tr><tr><td>1997</td><td>235,000</td><td>Intel ASCI Red</td><td>1.8 hours</td></tr><tr><td>1998</td><td>259,200</td><td>SGI T3E1200</td><td>3.6 hours</td></tr><tr><td>1999</td><td>431,344</td><td>IBM ASCI Blue</td><td>6.9 hours</td></tr><tr><td>2000</td><td>518,096</td><td>IBM ASCI White</td><td>3.6 hours</td></tr><tr><td>2001</td><td>525,000</td><td>Compaq AlphaServer SC ES45</td><td>6.6 hours</td></tr></table>

or guaranteed accuracy is required when solving a linear system. We mention just two papers, those by Demmel and Krückeberg [330, 1985] and Rump [1001, 2001], which provide very readable introductions to the subject and contain further references.

Edelman [373, 1991], [377, 1993], [378, 1994] presents statistics and details of applications in which large dense linear algebra problems arise. He also discusses relevant issues such as what users expect of the computed solutions and how best to make use of parallel computers. Table 9.3 contains "world records" for linear systems from Edelman's surveys and based on statistics from the TOP500 Supercomputer Sites Web site (http://www.top500.org/ or http://www.netlib.org/benchmark/top500.html). A practical application in which very large systems arise is the solution of boundary integral equations, a major application being the analysis of radar cross sections; the resulting systems have coefficient matrices that are complex symmetric (but not Hermitian).

# 9.14.1. LAPACK

Driver routines xGESV (simple) and xGESVX (expert) use LU factorization with partial pivoting to solve a general system of linear equations with multiple right-hand sides. The expert driver incorporates iterative refinement, condition estimation, and backward and forward error estimation and has an option to scale the system $AX = B$ to $(D_R^{-1}AD_C^{-1})D_CX = D_R^{-1}B$ before solution, where $D_{R} = \mathrm{diag}(r_{i}) = \mathrm{diag}(\max_{j}|a_{ij}|)$ and $D_{C} = \mathrm{diag}(\max_{i}r_{i}|a_{ij}|)$ ; the scaling is done by the routine xGEEQU. The LU factorization is computed by the routine xGETRF, which uses a partitioned outer product algorithm. The expert driver also returns the quantity $\| A\| /\| U\|$ , where $\| A\| \coloneqq \max_{i,j}|a_{ij}|$ , which is an estimate of the reciprocal of the growth factor, $1 / \rho_n^p$ . A value much less than 1 signals that the condition estimate and forward error bound could be unreliable.

The auxiliary routine xGETC2 implements LU factorization with complete pivoting.

For band matrices, the driver routines are xGBSV and xGBSVX, and for tridiagonal matrices, xGTSV and xGTSVX; they all use LU factorization with partial pivoting.

# Problems

9.1. (Completion of proof of Theorem 9.1.) Show that if a singular matrix $A \in \mathbb{R}^{n \times n}$ has a unique LU factorization then $A_{k}$ is nonsingular for $k = 1:n - 1$ .   
9.2. Define $A(\sigma) = A - \sigma I$ , where $\sigma \in \mathbb{R}$ and $A \in \mathbb{R}^{n \times n}$ . For how many values of $\sigma$ , at most, does $A(\sigma)$ fail to have an LU factorization without pivoting?   
9.3. Show that $A \in \mathbb{R}^{n \times n}$ has a unique LU factorization if 0 does not belong to the field of values $F(A) = \{z^* Az / (z^* z) : 0 \neq z \in \mathbb{C}^n\}$ .   
9.4. State analogues of Theorems 9.3 and 9.4 for LU factorization with row and column interchanges: $PAQ = LU$ .   
9.5. Give a $2 \times 2$ matrix $A$ having an LU factorization $A = LU$ such that $|L||U| \leq c|A|$ does not hold for any $c$ , yet $\| |L||U| \|_{\infty} / \| A \|_{\infty}$ is of order 1.   
9.6. Show that if $A \in \mathbb{R}^{n \times n}$ is nonsingular and totally nonnegative it has an LU factorization $A = LU$ with $L \geq 0$ and $U \geq 0$ . (Hint: use the inequality

$$
\det  (A) \leq \det  \left(A (1: p, 1: p)\right) \det  \left(A (p + 1: n, p + 1: n)\right), \quad p = 1: n - 1,
$$

which holds for any totally nonnegative $A$ [454, 1959, p. 100].) Deduce that the growth factor for GE without pivoting $\rho_{n} \equiv 1$ .

9.7. How many square submatrices, and how many rectangular submatrices, does an $n \times n$ matrix have?

9.8. Show that if $A \in \mathbb{R}^{n \times n}$ is nonsingular and its inverse is totally nonnegative then it has an LU factorization $A = LU$ with $|A| = |L||U|$ . (Use the fact that if $C$ is totally nonnegative and nonsingular then $JC^{-1}J$ is totally nonnegative, where $J = \mathrm{diag}((-1)^{i+1})$ (this can be proved using determinantal identities; see [26, 1987, Thm. 3.3].))

9.9. Show that for GE without pivoting $\rho_{n}\leq 1 + n\| |L||U|\|_{\infty} / \| A\|_{\infty}$

9.10. Suppose that GE without pivoting is applied to a linear system $Ax = b$ , where $A \in \mathbb{R}^{n \times n}$ is nonsingular, and that all operations are performed exactly except for the division determining a single multiplier $l_{ij}$ (where $i > j$ and $A = LU$ ), which is computed with relative error $\epsilon$ : $l_{ij} = \widehat{l}_{ij}(1 + \epsilon)$ . Evaluate the difference $x - \widehat{x}$ between the exact and computed solutions. (The answer allows us to see clearly the effect of a computational blunder, which could, for example, be the result of the malfunction of a computer's divide operation.)

9.11. Show that $\theta$ in Theorem 9.8 satisfies

$$
\theta (B) := \theta \left(\left[ \begin{array}{c c} A & A \\ A & - A \end{array} \right]\right) = 2 \theta (A).
$$

Hence, for $g(n)$ defined in (9.15) and $S_{n}$ in (9.12), deduce a larger lower bound than $g(2n) \geq \rho_n^c(S_{2n}) = (2n + 1)/2$ .

9.12. Explain the errors in the following criticism of GE with complete pivoting.

Gaussian elimination with complete pivoting maximizes the pivot at each stage of the elimination. Since the product of the pivots is the determinant (up to sign), which is fixed, making early pivots large forces later ones to be small. These small pivots will have large relative errors due to the accumulation of rounding errors during the algorithm, and dividing by them therefore introduces larger errors.

9.13. In sparse matrix computations the choice of pivot in GE has to be made with the aim of preserving sparsity as well as maintaining stability. In threshold pivoting, a pivot element is chosen from among those elements in column $k$ that satisfy $|a_{ik}^{(k)}| \geq \tau \max_{m \geq k} |a_{mk}^{(k)}|$ , where $\tau \in (0, 1]$ is a parameter (see, for example, Duff, Erisman, and Reid [360, 1986, §5.4]). Show that for threshold pivoting

$$
\operatorname * {m a x} _ {i} | a _ {i j} ^ {(k)} | \leq (1 + \tau^ {- 1}) _ {\max} ^ {\mu_ {j}} \operatorname * {m a x} _ {i} | a _ {i j} |,
$$

where $\mu_{j}$ is the number of nonzero entries in the $j$ th column of $U$ . Hence obtain a bound for $\rho_{n}$ .

9.14. Let $A \in \mathbb{R}^{n \times n}$ be pre-pivoted for GEPP, that is, GEPP requires no row interchanges when applied to $A$ . Show that GEPP computes the same LU factorization as (a) the first method described in §9.9 and (b) pairwise pivoting, with the natural pivoting strategy that ensures the multipliers are bounded by 1, applied to $\Pi A$ , where $\Pi = I(n: -1: 1,:)$ is the row reversal permutation matrix.

9.15. (RESEARCH PROBLEM) Obtain sharp bounds for the growth factor for GEPP applied to (a) a matrix with lower bandwidth $p$ and upper bandwidth $q$ (thus generalizing Theorem 9.11), and (b) a quasi-tridiagonal matrix (an $n \times n$ matrix that is tridiagonal except for nonzero $(1, n)$ and $(n, 1)$ elements).

9.16. (RESEARCH PROBLEM) Explain why the growth factor for GEPP is almost always small in practice.

9.17. (RESEARCH PROBLEM) For GE with complete pivoting what is the value of $\lim_{n\to \infty}g(n) / n$ (see (9.15))? Is $\rho_n^c$ equal to $n$ for Hadamard matrices?

9.18. (RESEARCH PROBLEM) Let $g(n)$ be defined for GE with rook pivoting analogously to (9.15). Try to obtain the exact value of $g(n)$ for $n \leq 4$ , say (cf. the bounds for complete pivoting on page 169), and to obtain lower bounds valid for all $n$ . All that is currently known is the bound (9.16) and a slightly smaller implicitly defined bound from which it is derived in [435, 1997], together with the following lower bounds found by direct search (as in §26.1):

<table><tr><td>n</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>lower bound</td><td>2 (exact)</td><td>2.9</td><td>4.16</td><td>5.36</td></tr></table>
