# Chapter 27. Pad´e Approximation

Suppose $f$ is a function with a Taylor series

$$
f ( z ) = c _ { 0 } + c _ { 1 } z + c _ { 2 } z ^ { 2 } + \cdot \cdot \cdot
$$

at $z = 0$ .14 Whether or not the series converges doesn’t matter in this chapter (it is enough for $f$ to be a formal power series). For any integer $m \geq 0$ , the degree $m$ Taylor approximant to $f$ is the unique polynomial $p _ { m } \in \mathcal { P } _ { m }$ that matches the series as far as possible, which will be at least through degree $m$ ,

$$
( f - p _ { m } ) ( z ) = O ( z ^ { m + 1 } ) .
$$

Pad´e approximation is the generalization of this idea to rational approximation. For any integers $m , n \geq 0$ , $r \in \mathcal { R } _ { m n }$ is the type $( m , n )$ Pad´e approximant to $f$ if their Taylor series at $z = 0$ agree as far as possible:

$$
( f - r _ { m n } ) ( z ) = O ( z ^ { \mathrm { m a x i m u m } } ) .
$$

In these conditions the “big O” notation has its usual precise meaning. Equation (27.2) asserts, for example, that the first nonzero term in the Taylor series for $f - p _ { m }$ is of order $z ^ { k }$ for some $k \geq m + 1$ , but not necessarily $k = m + 1$ .

Pad´e approximation can be viewed as the special case of rational interpolation in which the interpolation points coalesce at a single point. Thus there is a close analogy between the mathematics of the last chapter and this one, thoughsome significant differences too that spring from the fact that the powers $z ^ { 0 } , z ^ { 1 } , \dots$ are ordered whereas the roots of unity are all equal in status. We shall see that a key property is that $r _ { m n }$ exists and is unique. Generically, it matches $f$ through term $m + n$ ,

$$
( f - r _ { m n } ) ( z ) = O ( z ^ { m + n + 1 } ) ,
$$

but in some cases, the matching will be to lower or higher order.

For example, the type $( 1 , 1 )$ Pad´e approximant to $e ^ { z }$ is $( 1 + \textstyle { \frac { 1 } { 2 } } z ) / ( 1 - \textstyle { \frac { 1 } { 2 } } z )$ , as we can verify numerically with the Chebfun command padeapprox:

[r,a,b] $=$ padeapprox(@exp,1,1); fprintf(' Numerator coeffs: %19.15f %19.15f\n',a) fprintf(' Denominator coeffs: %19.15f %19.15f\n',b)

Numerator coeffs: 1.000000000000000 0.500000000000000   
Denominator coeffs: 1.000000000000000 -0.500000000000000

The algorithm used by padeapprox will be discussed in the second half of this chapter.

The early history of Pad´e approximation is hard to disentangle because every continued fraction can be regarded as a Pad´e approximant (Exercise 27.7), and continued fractions got a lot of attention in past centuries. For example, Gauss derived the idea of Gauss quadrature from a continued fraction that amounts to a Pad´e approximant to the function $\log ( ( z + 1 ) / ( z - 1 ) )$ at the point $z = \infty$ [Gauss 1814, Takahasi & Mori 1971, Trefethen 2008]. Ideas related to Pad´e approximation have been credited to Anderson (1740), Lambert (1758), and Lagrange (1776), and contributions were certainly made by Cauchy [1826] and Jacobi [1846]. The study of Pad´e approximants began to come closer to the current form with the papers of Frobenius [1881] and Pad´e himself [1892], who was a student of Hermite and published many articles after his initial thesis on the subject. Throughout the early literature, and also in the more recent era, much of the discussion of Pad´e approximation is connected with continued fractions, determinants, and recurrence relations, but here we shall follow a more robust matrix formulation.

We begin with a theorem about existence, uniqueness, and characterization, analogous to Theorem 24.1 for rational best approximation on an interval. There, the key idea was to count points of equioscillation of the error function $f - r$ . Here, we count how many initial terms of the Taylor series of $f - r$ are zero. The arguments are similar, and again, everything depends on the integer known as the defect. Recall that if $r \in \mathcal { R } _ { m n }$ is of exact type $( \mu , \nu )$ for some $\mu \leq m$ , $\nu \leq n$ , then the defect of $r$ with respect to $\mathcal { R } _ { m n }$ is $d = \operatorname* { m i n } \{ m - \mu , n - \nu \} \geq 0$ , with $\mu = - \infty$ and $d = n$ in the special case $r = 0$ .

Theorem 27.1. Characterization of Pad´e approximants. For each $m , n \geq$ 0, a function $f$ has a unique Pad´e approximant $r _ { m n } \in \mathcal { R } _ { m n }$ as defined by the condition (27.3), and a function $r \in \mathcal { R } _ { m n }$ is equal to $r _ { m n }$ if and only if $( f - r ) ( z ) =$ $O ( z ^ { m + n + 1 - d } )$ , where $d$ is the defect of $r$ in $\mathcal { R } _ { m n }$ .

Proof. The first part of the argument is analogous to parts 2 and 4 of the proof of Theorem 24.1: we show that if $r$ satisfies $( f - r ) ( z ) = O ( z ^ { m + n + 1 - d } )$ , then $r$ is the unique type $( m , n )$ Pad´e approximant to $f$ as defined by the condition (27.3). Suppose then that $( f - r ) ( z ) = O ( z ^ { m + n + 1 - d } )$ and that $( f - \tilde { r } ) ( z ) = O ( z ^ { m + n + 1 - d } )$ also for some possibly different function $\tilde { r } \in \mathcal { R } _ { m n }$ . Then $( r - { \tilde { r } } ) ( z ) = O ( z ^ { m + n + 1 - d } )$ . However, $r - \tilde { r }$ is of type $( m + n - d , 2 n - d )$ , so it can only have $m + n - d$ zeros at $z = 0$ unless it is identically zero. This implies $\tilde { r } = r$ .

The other half of the proof is to show that there exists a function $r$ with $( f - r ) ( z ) = O ( z ^ { m + n + 1 - d } )$ . This part of the argument makes use of linear algebra and is given in the two paragraphs following (27.8).

Let us consider some examples to illustrate the characterization of Theorem 27.1. First, a generic case: We noted above that the type (1,1) Pad´e approximant to $e ^ { z }$ is $r _ { 1 1 } ( z ) = ( 1 + \textstyle \frac { 1 } { 2 } z ) / ( 1 - \textstyle \frac { 1 } { 2 } z )$ . The defect of $r _ { 1 1 }$ in $\mathcal { R } _ { 1 1 }$ is $d = 0$ , and we have

$$
r _ { 1 1 } ( z ) - e ^ { z } = \textstyle { \frac { 1 } { 1 2 } } z ^ { 3 } + \textstyle { \frac { 1 } { 1 2 } } z ^ { 4 } + \cdot \cdot \cdot = O ( z ^ { 3 } ) .
$$

Since $m + n + 1 - d = 3$ , this confirms that $r _ { 1 1 }$ is the Pad´e approximant.

On the other hand, if $f$ is even or odd, we soon find ourselves in the nongeneric case. Suppose we consider

$$
\begin{array} { r } { f ( z ) = \cos ( z ) = 1 - \frac { 1 } { 2 } z ^ { 2 } + \frac { 1 } { 2 4 } z ^ { 4 } - \cdot \cdot \cdot } \end{array}
$$

and the rational approximation

$$
\begin{array} { r } { r ( z ) = 1 - \frac { 1 } { 2 } z ^ { 2 } } \end{array}
$$

of exact type $( 2 , 0 )$ . This gives

$$
( f - r ) ( z ) = O ( z ^ { 4 } ) , \ \ne O ( z ^ { 5 } ) .
$$

By Theorem 27.1, this implies that $r$ is the Pad´e approximation to $f$ for four different choices of $( m , n )$ : $( 2 , 0 )$ , $( 3 , 0 )$ , $( 2 , 1 )$ , and $( 3 , 1 )$ . With $( m , n ) = ( 2 , 0 )$ , for example, the defect is $d = 0$ and we need $( f - r ) ( z ) = O ( z ^ { 2 + 0 + 1 - 0 } ) = O ( z ^ { 3 } )$ , and with $( m , n ) = ( 3 , 1 )$ , the defect is $d = 1$ and we need $( f - r ) ( z ) = O ( z ^ { 3 + 1 + 1 - 1 } ) = O ( z ^ { 4 } )$ . Both matching conditions are satisfied, so $r$ is the Pad´e approximant of both types $( 2 , 0 )$ and $( 3 , 1 )$ . Similarly it is also the Pad´e approximant of types $( 3 , 0 )$ and $( 2 , 1 )$ , but for no other values of $( m , n )$ .

This example involving an even function suggests the general situation. In analogy to the Walsh table of Chapter 24, the Pad´e table of a function $f$ consists of the set of its Pad´e approximants for various $m , n \geq 0$ laid out in an array, with $m$ along the horizontal and $n$ along the vertical:

$$
\left( { \begin{array} { c c c c } { r _ { 0 0 } } & { r _ { 1 0 } } & { r _ { 2 0 } } & { . . . } \\ { r _ { 0 1 } } & { r _ { 1 1 } } & { r _ { 2 1 } } & { . . . } \\ { r _ { 0 2 } } & { r _ { 1 2 } } & { r _ { 2 2 } } & { . . . } \\ { \vdots } & { \vdots } & { \vdots } & { \ddots } \\ { \vdots } & { \vdots } & { \vdots } & { \ddots } \end{array} } \right) .
$$

The idea of the Pad´e table was proposed by Pad´e [1892], who called it “a table of approximate rational fractions. . . analogous to the multiplication table, unbounded to the right and below.” Like the Walsh table for real rational approximation on an interval, the Pad´e table breaks into square blocks of degenerate entries, again as a consequence of the equioscillation-type characterization [Trefethen 1984].

Theorem 27.2. Square blocks in the Pad´e table. The Pad´e table for any function $f$ breaks into precisely square blocks containing identical entries. (If $f$ is rational, one of these will be infinite in extent.) The only exception is that if an entry $r = 0$ appears in the table, then it fills all of the columns to the left of some fixed index $m = m _ { 0 }$ .

Proof. The proof is essentially the same as the proof of Theorem 24.2.

As in the case of best real approximation on an interval discussed in Chapter 24, square blocks and defects have a variety of consequences for Pad´e approximants. In particular, the Pad´e approximation operator, which maps Taylor series $f$ to their Pad´e approximants $r _ { m n }$ , is continuous at $f$ with respect to a norm based on Taylor coefficients if and only if $r _ { m n }$ has defect $d = 0$ . Another related result is that best supremum-norm approximations on intervals $[ - \varepsilon , \varepsilon ]$ converge to the Pad´e approximant as $\varepsilon  0$ if $d = 0$ , but not, in general, if $d > 0$ . These results come from [Trefethen $\&$ Gutknecht 1985], with earlier partial results due to Walsh; Werner and Wuytak; and Chui, Shisha, and Smith.

At this point we have come a good way into the theory of Pad´e approximation without doing any algebra. To finish the job, and to lead into algorithms, it is time to introduce vectors and matrices, closely analogous to those of the last chapter.

Given a function $f$ with Taylor coefficients $\{ c _ { j } \}$ , suppose we look for a representation of the Pad´e approximant $r _ { m n }$ as a quotient $r = p / q$ with $p \in \mathcal { P } _ { m }$ and $q \in \mathcal { P } _ { n }$ . Equation (27.4) is nonlinear, but multiplying through by the denominator suggests the linear condition

$$
p ( z ) = f ( z ) q ( z ) + O ( z ^ { m + n + 1 } ) ,
$$

just as (26.4) led to (26.5). To express this equation in matrix form, suppose that $p$ and $q$ are represented by coefficient vectors $\mathbf { a }$ and $\mathbf { b }$ :

$$
\mathbf { a } = \left( \begin{array} { c } { a _ { 0 } } \\ { a _ { 1 } } \\ { \vdots } \\ { a _ { m } } \end{array} \right) , \qquad \mathbf { b } = \left( \begin{array} { c } { b _ { 0 } } \\ { b _ { 1 } } \\ { \vdots } \\ { b _ { n } } \end{array} \right) ,
$$

$$
p ( z ) = \sum _ { k = 0 } ^ { m } a _ { k } z ^ { k } , \qquad q ( z ) = \sum _ { k = 0 } ^ { n } b _ { k } z ^ { k } .
$$

Then (27.5) can be written as an equation involving a Toeplitz matrix of Taylor coefficients of $f$ , that is, a matrix with constant entries along each diagonal. For $m \geq n$ , the equation looks like this:

$$
\left( \begin{array} { c } { a _ { 0 } } \\ { a _ { 1 } } \\ { \vdots } \\ { a _ { n } } \\ { \vdots } \\ { \vdots } \\ { a _ { m + 1 } } \\ { a _ { m + 1 } } \\ { \vdots } \\ { a _ { m + n } } \end{array} \right) = \left( \begin{array} { c c c c c } { c _ { 0 } } & & & & \\ { c _ { 1 } } & & { c _ { 0 } } & & \\ { \vdots } & { \vdots } & { \ddots } & & \\ { c _ { n } } & { c _ { m - 1 } } & { \ddots } & & { c _ { 0 } } \\ { \vdots } & { \vdots } & & & { \vdots } \\ { c _ { m } } & { c _ { m - 1 } } & { \hdots } & { c _ { m - n } } \\ { c _ { m + 1 } } & { c _ { m } } & { \hdots } & { c _ { m + 1 - n } } \\ { \vdots } & { \vdots } & { \ddots } & { \vdots } \\ { c _ { m + n } } & { c _ { m + n - 1 } } & { \hdots } & { c _ { m } } \end{array} \right) \left( \begin{array} { c } { b _ { 0 } } \\ { b _ { 1 } } \\ { \vdots } \\ { b _ { n } } \end{array} \right)
$$

coupled with the condition

$$
a _ { m + 1 } = \cdots = a _ { m + n } = 0 .
$$

In other words, $\mathbf { b }$ must be a null vector of the $n \times ( n + 1 )$ matrix displayed below the horizontal line. If $m < n$ , the equation looks like this:

$$
\left( \begin{array} { c } { a _ { 0 } } \\ { a _ { 1 } } \\ { \vdots } \\ { a _ { m + 1 } } \\ { a _ { m + 1 } } \\ { \vdots } \\ { a _ { n } } \\ { a _ { m } } \end{array} \right) = \left( \begin{array} { c c c c c c c } { c _ { 0 } } \\ { c _ { 1 } } \\ { c _ { 1 } } & { c _ { 0 } } \\ { \vdots } & { \vdots } & { \ddots } \\ { c _ { m } } & { c _ { m - 1 } } & { \ldots } & { c _ { 0 } } \\ { c _ { m + 1 } } & { c _ { m } } & { \ldots } & { c _ { 1 } } & { c _ { 0 } } \\ { c _ { m + 1 } } & { c _ { m } } & { \ldots } & { c _ { 1 } } & { c _ { 0 } } \\ { \vdots } & { \vdots } & { \vdots } & { \ddots } & { \ddots } \\ { c _ { n } } & { c _ { n - 1 } } & { \ddots } & { c _ { 1 } } & { c _ { 0 } } \\ { \vdots } & { \vdots } & { \vdots } & { \vdots } \\ { c _ { m + n } } & { c _ { m + n - 1 } } & { \ldots } & { c _ { m } } \end{array} \right) \left( \begin{array} { c } { b _ { 0 } } \\ { b _ { 1 } } \\ { \vdots } \\ { b _ { n } } \end{array} \right) .
$$

For simplicity we shall use the label (27.6) to refer to both cases, writing the $n ~ \times$ $( n + 1 )$ matrix always as

$$
C = \left( \begin{array} { c c c c } { { c _ { m + 1 } } } & { { c _ { m } } } & { { \ldots } } & { { c _ { m + 1 - n } } } \\ { { \vdots } } & { { \vdots } } & { { \ddots } } & { { \vdots } } \\ { { c _ { m + n } } } & { { c _ { m + n - 1 } } } & { { \ldots } } & { { c _ { m } } } \end{array} \right)
$$

with the convention that $c _ { k } = 0$ for $k < 0$ .

One solution to (27.6)–(27.7) would be $\mathbf { a } = \mathbf { 0 }$ and $\mathbf { b } = \mathbf { 0 }$ , corresponding to the useless candidate $r = 0 / 0$ . However, an $n \times ( n + 1 )$ matrix always has a nonzero null vector,

$$
C \mathbf { b } = \mathbf { 0 } , \quad \mathbf { b } \neq \mathbf { 0 } ,
$$

and once $\mathbf { b }$ is chosen, the coefficients $a _ { 0 } , \ldots , a _ { m }$ of $p$ can be obtained by multiplying out the matrix-vector product above the line. Thus there is always a solution to (27.5) with $q \neq 0$ .

If $b _ { 0 } \neq 0$ , then dividing (27.5) by $q$ shows that $p / q$ is a solution to (27.4). Some nonzero null vectors $\mathbf { b }$ , however, may begin with one or more zero components. Suppose that $\mathbf { b }$ is a nonzero null vector with $b _ { 0 } = b _ { 1 } = \cdot \cdot \cdot = b _ { \sigma - 1 } = 0$ and $b _ { \sigma } \neq 0$ for some $\sigma \geq 1$ . Then the corresponding vector $\mathbf { a }$ will also have $u _ { 0 } = u _ { 1 } = \cdot \cdot \cdot =$ $a _ { \sigma - 1 } = 0$ (and $a _ { \sigma }$ might be zero or nonzero). It follows from the Toeplitz structure of (27.6) that we can shift both $\mathbf { a }$ and $\mathbf { b }$ upward by $\sigma$ positions to obtain new vectors $\tilde { \mathbf { a } } = ( a _ { \sigma } , \ldots , a _ { m } , 0 , \ldots , 0 ) ^ { T }$ and $\bar { \mathbf { b } } = ( b _ { \sigma } , \ldots , b _ { n } , 0 , \ldots , 0 ) ^ { T }$ while preserving the quotient $r = \tilde { p } / \tilde { q } = p / q$ . Thus $r$ has defect $d \geq \sigma$ , and (27.6)–(27.7) are still satisfied except that $\tilde { a } _ { m + n - \sigma + 1 } , \dots , \tilde { a } _ { m + n }$ may no longer be zero, implying $( f - r ) ( z ) = O ( z ^ { m + n + 1 - \sigma } )$ . Thus $( f - r ) ( z ) = O ( z ^ { m + n + 1 - d } )$ , and this completes the proof of Theorem 27.1.

We have just shown that any nonzero null vector of the matrix $C$ of (27.8) gives a function $r$ that satisfies the condition for a Pad´e approximation and hence must be the unique approximant provided by Theorem 27.1. So we have proved the following theorem.

Theorem 27.3. Linear algebra solution of Pad´e problem. Given a function $f$ with Taylor coefficients $\{ c _ { j } \}$ , let b be any nonzero null vector of the matrix

$C$ of (27.8), let a be the corresponding vector obtained from (27.6), and let $p \in \mathcal { P } _ { m }$ and $q \in \mathcal { P } _ { n }$ be the corresponding polynomials. Then $r _ { m n } = p / q$ is the unique type $( m , n )$ Pad´e approximant to $f$ .

We emphasize that the vectors $\mathbf { a }$ and $\mathbf { b }$ are not unique in general: a function in $\mathcal { R } _ { m n }$ may have many representations $p / q$ . Nevertheless, all choices of $\mathbf { a }$ and $\mathbf { b }$ lead to the same rmn.

From Theorems 27.1–27.3 one can derive a precise characterization of the algebraic structure of the Pad´e approximants to a function $f$ , as follows. Let $\hat { r }$ b e a rational function of exact type $( \mu , \nu )$ that is the Pad´e approximant to $f$ in a $( k + 1 ) \times ( k + 1 )$ square block for some $k \geq 0$ :

$$
\left( \begin{array} { c c c } { { r _ { \mu \nu } } } & { { . . . } } & { { r _ { \mu + k , \nu } } } \\ { { } } & { { } } & { { } } \\ { { \vdots } } & { { } } & { { \vdots } } \\ { { } } & { { } } & { { } } \\ { { r _ { \mu , \nu + k } } } & { { . . . } } & { { r _ { \mu + k , \nu + k } } } \end{array} \right) .
$$

Write $\hat { r } = \hat { p } / \hat { q }$ with $\hat { p }$ and $\hat { q }$ of exact degrees $\mu$ and $\nu$ . From Theorem 27.1 we know that the defect $d$ must be distributed within the square block according to this pattern illustrated for $k = 5$ :

$$
\begin{array} { r l } { { \operatorname* { d e f e c t } \ d : } } & { { } \left( \begin{array} { l l l l l l } { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 1 } & { 1 } & { 1 } & { 1 } \\ { 0 } & { 1 } & { 2 } & { 2 } & { 2 } & { 2 } \\ { 0 } & { 1 } & { 2 } & { 3 } & { 3 } & { 3 } \\ { 0 } & { 1 } & { 2 } & { 3 } & { 4 } & { 4 } \\ { 0 } & { 1 } & { 2 } & { 3 } & { 4 } & { 5 } \end{array} \right) \ . } \end{array}
$$

According to Theorem 27.3, the polynomials $p$ and $q$ that result from solving the matrix problem (27.6)–(27.7) must be related to $\hat { p }$ and $\hat { q }$ by

$$
p ( z ) = \pi ( z ) \hat { p } ( z ) , \quad q ( z ) = \pi ( z ) \hat { q } ( z )
$$

for some polynomial $\pi$ of degree at most $d$ . Now let us define the deficiency $\lambda$ of $r$ as the distance below the cross-diagonal in the square block, with the following pattern:

$$
\mathrm { d e f f c i e n c y ~ } \lambda : \quad \left( \begin{array} { c c c c c c c } { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } & { { 1 } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } & { { 1 } } & { { 2 } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { 1 } } & { { 2 } } & { { 3 } } \\ { { 0 } } & { { 0 } } & { { 1 } } & { { 2 } } & { { 3 } } & { { 4 } } \\ { { 0 } } & { { 1 } } & { { 2 } } & { { 3 } } & { { 4 } } & { { 5 } } \end{array} \right) ~ . \nonumber
$$

From Theorem 27.1, we know that in the positions of the block with $\lambda ~ > ~ 0$ , $( f - r ) ( z ) = O ( z ^ { m + n + 1 - \lambda } ) , \neq O ( z ^ { m + n + 2 - \lambda } )$ , for otherwise, the block would be bigger. For this to happen, $\pi ( z )$ must be divisible by $z ^ { \lambda }$ , so that at least $\lambda$ powers of $z$ are lost when solutions $p$ and $q$ from (27.6) are normalized to $\hat { p }$ and $\hat { q }$ . Since may have degree up to $d$ , the number of degrees of freedom remaining in and $\pi$ $p$ $q$ is $d - \lambda$ , an integer we denote by $\chi$ , distributed within the block according to this

pattern:

$$
\mathrm { r a n k ~ d e f i c i e n c y ~ } \chi ; \quad \left( \begin{array} { c c c c c c c } { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 1 } } & { { 1 } } & { { 1 } } & { { 1 } } & { { 0 } } \\ { { 0 } } & { { 1 } } & { { 2 } } & { { 2 } } & { { 1 } } & { { 0 } } \\ { { 0 } } & { { 1 } } & { { 2 } } & { { 2 } } & { { 1 } } & { { 0 } } \\ { { 0 } } & { { 1 } } & { { 1 } } & { { 1 } } & { { 1 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } \end{array} \right) \ .
$$

Thus the dimensionality of the space of vectors $q$ is $\chi + 1$ , and the same for $p$ . We call $\chi$ the rank deficiency of $r$ because of a fact of linear algebra: the rank of the $n \times ( n + 1 )$ matrix $C$ of (27.8) must be equal to $n - \chi$ , so that its space of null vectors will have the required dimension $\chi + 1$ . Some ideas related to these developments can be found in [Heinig & Rost 1984].

We have just outlined a proof of the following theorem, which can be found in Section 3 of [Gragg 1972].

Theorem 27.4. Structure of a Pad´e approximant. Let $f$ and $m , n \geq 0$ be given, let the type $( m , n )$ Pad´e approximant $r _ { m n }$ of $f$ have exact type $( \mu , \nu )$ , and let $\hat { p }$ and $\hat { q } \neq 0$ be polynomials of exact degrees $\mu$ and $\nu$ with $r _ { m n } = \hat { p } / \hat { q }$ . Let the defect $d$ , deficiency $\lambda$ , and rank deficiency $\chi = d - \lambda$ be defined as above. Then the matrix $C$ of (27.8) has rank $n - \chi$ , and two polynomials $p \in P _ { m }$ and $q \in P _ { n }$ satisfy (27.5) if and only if

$$
p ( z ) = \pi ( z ) \hat { p } ( z ) , \quad q ( z ) = \pi ( z ) \hat { q } ( z )
$$

for some $\pi \in \mathcal { P } _ { d }$ divisible by $z ^ { \lambda }$ .

Although we did not state it in the last chapter, there is an analogue of this theorem for rational interpolation in distinct points, proved by Maehly and Witzgall [1960] and discussed also in [Gutknecht 1990] and [Pach´on, Gonnet & Van Deun 2012].

With the results of the past few pages to guide us, we are now prepared to talk about algorithms.

At one level, the computation of Pad´e approximants is trivial, just a matter of implementing the linear algebra of (27.6)–(27.7). In particular, in the generic case, the matrix $C$ of (27.8) will have full rank, and so will its $n \times n$ submatrix obtained by deleting the first column. One computational approach to Pad´e approximation is accordingly to normalize $\mathbf { b }$ by setting $b _ { 0 } = 1$ and then determine the rest of the entries of $\mathbf { b }$ by solving a system of equations involving this square matrix.

This approach will fail, however, when the square matrix is singular, and it is nonrobust with respect to rounding errors even when the matrix is nonsingular. To work with (27.8) robustly, it is a better idea to normalize by the condition

$$
\| \mathbf { b } \| = 1 ,
$$

where $\| \cdot \|$ is the vector 2-norm, as in (26.6) of the last chapter. We then again consider the SVD (singular value decomposition) of $C$ , a factorization

$$
\boldsymbol { C } = \boldsymbol { U \Sigma V } ^ { * } ,
$$

where $U$ is $n \times n$ and unitary, $V$ is $( n + 1 ) \times ( n + 1 )$ and unitary, and $\Sigma$ is an $n \times ( n + 1 )$ real diagonal matrix with diagonal entries $\sigma _ { 1 } \geq \sigma _ { 2 } \geq \cdot \cdot \cdot \geq \sigma _ { n } \geq 0$ .

Suppose $\sigma _ { n } ~ > ~ 0$ . Then $C$ has rank $n$ , and the final column of $V$ provides a unique nonzero null vector $\mathbf { b }$ of $C$ up to a scale factor. This null vector defines a polynomial $q \in \mathcal { P } _ { n }$ . Moreover, from (27.11), we know that $( m , n )$ must lie on the outer boundary of its square block in the Pad´e table. If $q$ is divisible by $z ^ { \lambda }$ for some $\lambda \geq 1$ , then $( m , n )$ must lie in the bottom row or right column, and dividing $p$ and $q$ by $z ^ { \lambda }$ brings it to the left column or top row, respectively. A final trimming of any trailing zeros in $p$ or $q$ brings them to the minimal forms $\hat { p }$ and $\hat { q }$ with exact degrees $\mu$ and $\nu$ .

On the other hand, suppose $\sigma _ { n } = 0$ , so that the number of zero singular values of $C$ is $\chi \geq 1$ . In this case (27.11) tells us that $( m , n )$ must lie in the interior of its square block at a distance $\chi$ from the boundary. Both $m$ and $n$ can accordingly be reduced by $\chi$ and the process repeated with a new matrix and a new SVD, $\chi$ steps closer to the upper-left $( \mu , \nu )$ corner. After a small number of such steps (never more than $2 + \log _ { 2 } ( d + 1 )$ , where $d$ is the defect), convergence is guaranteed.

These observations suggest the following SVD-based algorithm, introduced in [Gonnet, G¨uttel $\&$ Trefethen 2013].

Algorithm 27.1. Pure Pad´e approximation in exact arithmetic

Input: $m \geq 0$ , $n \geq 0$ , and a vector c of Taylor coefficients $c _ { 0 } , \ldots , c _ { m + n }$ of $a$ function $f$ .

Output: Polynomials $p ( z ) = a _ { 0 } + \cdot \cdot \cdot + a _ { \mu } z ^ { \mu }$ and $q ( z ) = b _ { 0 } + \cdot \cdot \cdot + b _ { \nu } z ^ { \nu }$ , $b _ { 0 } = 1$ , of the minimal degree type $( m , n )$ Pad´e approximation of $f$ .

1. If $c _ { 0 } = \cdots = c _ { m } = 0$ , set $p = 0$ and $q = 1$ and stop.

2. If $n = 0$ , set $p ( z ) = c _ { 0 } + \cdot \cdot \cdot + c _ { m } z ^ { m }$ and $q = 1$ and go to Step 8.

3. Compute the $S V D$ (27.13) of the $n \times ( n + 1 )$ matrix $C$ . Let $\rho \leq n$ be the number of nonzero singular values.

4. If $\rho < n$ , reduce $n$ to $\rho$ and $m$ to $m - ( n - \rho )$ and return to Step 2.

5. Get $q$ from the null right singular vector b of $C$ and then $p$ from the upper part of (27.6).

6. If $b _ { 0 } = \cdot \cdot \cdot = b _ { \lambda - 1 } = 0$ for some $\lambda \geq 1$ , which also implies $a _ { 0 } = \cdot \cdot \cdot = a _ { \lambda - 1 } = 0$ , cancel the common factor of $z ^ { \lambda }$ in $p$ and $q$ .

7. Divide $p$ and $q$ by $b _ { 0 }$ to obtain a representation with $b _ { 0 } = 1$ .

8. Remove trailing zero coefficients, if any, from $p ( z )$ or $q ( z )$ .

In exact arithmetic, this algorithm produces the unique Pad´e approximant $r _ { m n }$ in a minimal-degree representation of type $( \mu , \nu )$ with $b _ { 0 } = 1$ . The greatest importance of Algorithm 27.1, however, is that it generalizes readily to numerical computation with rounding errors, or with noisy Taylor coefficients $\{ c _ { j } \}$ . All one needs to do is modify the tests for zero singular values or zero coefficients so as to incorporate a suitable tolerance, such as $1 0 ^ { - 1 4 }$ for computations in standard 16-digit arithmetic. The following modified algorithm also comes from [Gonnet, G¨uttel $\&$ Trefethen 2013].

Algorithm 27.2. Robust Pad´e approximation for noisy data or floating point arithmetic

Input: $m \geq 0$ , $n \geq 0$ , a vector c of Taylor coefficients $c _ { 0 } , \ldots , c _ { m + n }$ of a function $f$ , and a relative tolerance $\mathbf { t o l } \geq 0$ .

Output: Polynomials $p ( z ) = a _ { 0 } + \cdot \cdot \cdot + a _ { \mu } z ^ { \mu }$ and $q ( z ) = b _ { 0 } + \cdot \cdot \cdot + b _ { \nu } z ^ { \nu }$ , $b _ { 0 } = 1$ , of the minimal degree type $( m , n )$ Pad´e approximation of a function close to $f$ .

1. Rescale $f ( z )$ to $f ( z / \gamma )$ for some $\gamma > 0$ if desired to get a function whose Taylor coefficients $c _ { 0 } , \ldots , c _ { m + n }$ do not vary too widely.

2. Define $\tau = \pm \circ 1 \cdot \| \mathbf { c } \| _ { 2 }$ . If $| c _ { 0 } | = \cdot \cdot \cdot = | c _ { m } | \leq \tau$ , set $p = 0$ and $q = 1$ and stop.

3. If $n = 0$ , set $p ( z ) = c _ { 0 } + \cdot \cdot \cdot + c _ { m } z ^ { m }$ and $q = 1$ and go to Step 7.

4. Compute the $S V D$ (27.13) of the $n \times ( n + 1 )$ matrix $C$ . Let $\rho \leq n$ be the number of singular values of $C$ that are greater than $\gamma$ .

5. If $\rho < n$ , reduce n to $\rho$ and m to $m - ( n - \rho )$ and return to Step 3.

6. Get $q$ from the null right singular vector b of $C$ and then p from the upper part of (27.6).

7. If $| b _ { 0 } | , \ldots , | b _ { \lambda - 1 } | \leq \mathrm { t o l }$ for some $\lambda \geq 1$ , zero the first $\lambda$ coefficients of $p$ and $q$ and cancel the common factor $z ^ { \lambda }$ .

8. If $| b _ { n + 1 - \lambda } | , \ldots , | b _ { n } | \leq \mathtt { t o l }$ for some $\lambda \geq 1$ , remove the last $\lambda$ coefficients of $q$ . If $| a _ { m + 1 - \lambda } | , \ldots , | a _ { m } | \leq \tau$ for some $\lambda \geq 1$ , remove the last $\lambda$ coefficients of $p$ .

9. Divide $p$ and $q$ by $b _ { 0 }$ to obtain a representation with $b _ { 0 } = 1$ .

10. Undo the scaling of Step 1 by redefining $\gamma ^ { j } a _ { j }$ as $a _ { j }$ and $\gamma ^ { j } b _ { j }$ as $b _ { j }$ for each $j$

Algorithm 27.2 has been implemented in a MATLAB code called padeapprox that is included in the Chebfun distribution, though it does not involve chebfuns. In its basic usage, padeapprox takes as input a vector $\mathbf { c }$ of Taylor coefficients together with a specification of $m$ and $n$ , with $\mathtt { t o l } = 1 0 ^ { - 1 4 }$ by default. For example, following [Gragg 1972], suppose

$$
f ( z ) = { \frac { 1 - z + z ^ { 3 } } { 1 - 2 z + z ^ { 2 } } } = 1 + z + z ^ { 2 } + 2 z ^ { 3 } + 3 z ^ { 4 } + 4 z ^ { 5 } + \cdots .
$$

Then the type $( 2 , 5 )$ Pad´e approximation of $f$ comes out with the theoretically correct exact type $( 0 , 3 )$ :

c = [1 1 (1:50)]; [r,a,b] $=$ padeapprox(c,2,5); disp(a.'), disp(b.')

Coefficients of numerator: 1.0000 Coefficients of denominator:

1.0000 -1.0000 0.0000 -1.0000

To illustrate the vital role of the SVD in such a calculation, here is what happens if robustness is turned off by setting $\tt t o l = 0$ :

[r,a,b] $=$ padeapprox(c,2,5,0); disp(a.'), disp(b.')

Coefficients of numerator:

1.0e+15 \*  
0.0000 -0.0000 3.4166

Coefficients of denominator:

0.0000 -0.0000 3.4166 -3.4166 0.0000 -3.4166

We now see longer vectors with enormous entries, on the order of the inverse of machine precision. The type appears to be $( 2 , 5 )$ , but the zeros and poles reveal that this is spurious:

disp(roots(a(end:-1:1))), disp(roots(b(end:-1:1)))

Zeros:

1.44015621657119e-16 + 1.71080672699754e-08i1.44015621657119e-16 - 1.71080672699754e-08iPoles:-0.341163901914009 + 1.16154139999725i-0.341163901914009 - 1.16154139999725i0.6823278038280191.44015621642544e-16 + 1.71080672699754e-08i1.44015621642544e-16 - 1.71080672699754e-08i

We see that the two zeros are virtually canceled by two poles that differ from them by only about $1 0 ^ { - 2 4 }$ . Thus this approximant has two spurious pole-zero pairs, or Froissart doublets, introduced by rounding errors. Many Pad´e computations over the years have been contaminated by such effects, and in an attempt to combat them, many authors have asserted that it is necessary to compute Pad´e approximations in high-precision arithmetic.

If padeapprox is called with a MATLAB function handle $f$ rather than a vector as its first argument, then it assumes $f$ is a function analytic in a neighborhood of the closed unit disk and computes Taylor coefficients by the FFT. For example, here is the type $( 2 , 2 )$ Pad´e approximant of $f ( z ) = \cos ( z )$ :

[r,a,b] = padeapprox(@cos,2,2); disp(a.'), disp(b.')

Coefficients of numerator: 1.000000000000000 0 -0.416666666666667   
Coefficients of denominator: 1.000000000000000 0 0.083333333333333

One appealing application of padeapprox is the numerical computation of block structure in the Pad´e table for a given function $f$ . For example, here is a table of the computed pair $( \mu , \nu )$ for each $( m , n )$ in the upper-left portion of the Pad´e table of $\cos ( z )$ with $0 \leq m , n \leq 8$ . One sees the $2 \times 2$ block structure resulting from the evenness of $\cos ( z )$ .

nmax $= ~ 8$ ; for $\mathtt { n } \ = \ 0 : \mathtt { n m a x }$

for $\mathtt { m } \ = \ 0$ :nmax [r,a,b,mu,nu] $=$ padeapprox(@cos,m,n); fprintf(' (%1d,%1d)',mu,nu) end fprintf $( " \setminus " )$ end

(0,0) (0,0) (2,0) (2,0) (4,0) (4,0) (6,0) (6,0) (8,0) (0,0) (0,0) (2,0) (2,0) (4,0) (4,0) (6,0) (6,0) (8,0) (0,2) (0,2) (2,2) (2,2) (4,2) (4,2) (6,2) (6,2) (8,2) (0,2) (0,2) (2,2) (2,2) (4,2) (4,2) (6,2) (6,2) (8,2) (0,4) (0,4) (2,4) (2,4) (4,4) (4,4) (6,4) (6,4) (8,4) (0,4) (0,4) (2,4) (2,4) (4,4) (4,4) (6,4) (6,4) (8,4) (0,6) (0,6) (2,6) (2,6) (4,6) (4,6) (6,6) (6,6) (8,6) (0,6) (0,6) (2,6) (2,6) (4,6) (4,6) (6,6) (6,6) (8,6) (0,8) (0,8) (2,8) (2,8) (4,8) (4,8) (6,8) (6,8) (8,8)

We can also show the block structure with a color plot, like this:

d = zeros(nmax $^ { + 2 }$ );   
rand('state',7); h = tan(2\*rand(50)-1); h(8,1) = 1;   
for $\mathtt { n } \ = \ 0 : \mathtt { n m a x }$ , for m = 0:nmax $[ \mathbf { r } , \mathbf { a } , \mathbf { b } , \mathtt { m u } , \mathtt { n u } ] \ = \ \mathtt { p a d e a p p r o x } ( \mathtt { q c o s } , \mathtt { m } , \mathtt { n } ) ; \ \mathtt { d } ( \mathtt { n } + 1 , \mathtt { m } + 1 ) \ = \ \mathtt { h } ( \mathtt { m u } + 1 , \mathtt { n u } + 1 )$ ;   
end, end, pcolor(d), axis ij square off

Pad´e table of cos(z)

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0004_pages_0211-0280/auto/images/d1bcc5e47359d73544afa6fe38d9c72ede3bff9a0a46350c613c3fd463d7de52.jpg)

The pattern of $2 \times 2$ blocks is broken if we compute a larger segment of the table, such as $0 \leq m , n \leq 1 6$ :

nmax $\textstyle { \begin{array} { r l } \end{array} } = { \begin{array} { r l } { 1 6 } \end{array} }$ ; d = zeros(nmax+2);   
for $\mathtt { n } \ = \ 0 : \mathtt { n m a x }$ , for $\mathtt { m } \ = \ 0$ :nmax [r,a,b,mu,nu] $=$ padeapprox(@cos,m,n); d( $\mathtt { n } { + } 1$ ,m+1) = h(mu+1,nu+1);   
end, end, pcolor(d), axis ij square off

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0004_pages_0211-0280/auto/images/1f5924d667f3826fa7628b5e5879ac29b445e6eb79057f4275c3ed0ef985e38b.jpg)

What is going on here is that for $m + n$ greater than about 16, $\cos ( z )$ is resolved to machine precision, and the diagonal stripes of the plot show that padeapprox has automatically cut $m$ and $n$ down to this level.

For an “arbitrary” function $f$ with gaps in its Taylor series, the block structure can be quite intriguing, as illustrated by this example with $f ( z ) = 1 + z + z ^ { 4 } + z ^ { 7 } +$ $z ^ { 1 0 } + z ^ { 1 3 } + z ^ { 1 6 } + z ^ { 1 7 }$ :

$$
\begin{array} { r l } & { \mathrm { ~ \beta = ~ \Theta ( z ) ~ \gamma _ 1 + z + z _ { \perp } \cdot \gamma _ 4 + z _ { \perp } \cdot \hat { \mathrm {  ~ \gamma ~ } } \mathrm { \hat { \mathrm {  ~ \gamma ~ } } \mathrm { \hat { \mathrm {  ~ \psi ~ } } \mathrm {  ~ \psi ~ } } } } } \\ & { \mathrm { ~ \beta r ~ \mathrm { ~ n ~ \beta ~ = ~ 0 : n m a x , ~ \hat { \mathrm { ~ f ~ o r ~ ~ m ~ \psi ~ } } = ~ 0 : n m a x } ~ } } \\ & { \mathrm { ~ [ \hat { \mathrm { ~  ~ r ~ } } , \mathrm { ~ a ~ } , \mathrm { b ~ } , m u , n u ] ~ \mathrm { ~ \beta ~ = ~ \ p a d e a p p r o x ( \mathrm { ~ f ~ , ~ m ~ } , n ) ~ ; ~ \mathrm { ~ d ~ } ( n + 1 , m + 1 ) ~ \mathrm { ~ \beta ~ = ~ h ~ ( m u + 1 , n u + 1 ) ~ ; ~ \hat { \mathrm { ~ o r ~ } ~ } \mathrm { ~ \hat { \delta ~ } ~ } } ~ } } } \end{array}
$$

end, end, pcolor(d), axis ij square off

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0004_pages_0211-0280/auto/images/08a9b6677bb826de065fa36fe7c1499a670bc0e4d892b4dd93100a577ea21ee7.jpg)

Apart from $z ^ { 1 7 }$ , these are the initial terms of the Taylor series of

$$
f ( z ) = { \frac { 1 + z - z ^ { 3 } } { 1 - z ^ { 3 } } } ,
$$

an example for which Pad´e worked out the block structure for $0 \leq m \leq 7$ , $0 \leq n \leq 5$ [Pad´e 1892], showing vividly a $2 \times 2$ block, two $3 \times 3$ blocks, and the beginning of the infinite block at position $( 3 , 3 )$ .

In this chapter we have discussed how to compute Pad´e approximants, but not what they are useful for. As outlined in Chapter 23, applications of these approximations typically involve situations where we know a function in one region of the $z$ -plane and wish to evaluate it in another region that lies near or beyond certain singularities. The next chapter is devoted to practical exploration of such problems.

From a theoretical perspective, a central question for more than a century has been, what sort of convergence of Pad´e approximants of a function $f$ can we expect as $m$ and/or $n$ increase to $\infty$ ? In the simplest case, suppose that $f$ is an entire function, that is, analytic for all $z$ . Then for any compact set $K$ in the complex plane, we know that the type $( m , 0 )$ Pad´e approximants converge uniformly on $K$ as $m \to \infty$ , since these are just the Taylor approximants. One might hope that the same would be true of type $( m , n _ { 0 } )$ approximants for fixed $n _ { 0 } \geq 1$ as $m \to \infty$ , or of type $( n , n )$ approximants as $n \to \infty$ , but in fact, pointwise convergence need not occur in either of these situations. The problem is that spurious pole-zero pairs, Froissart doublets, may appear at seemingly arbitrary locations in the plane. As $m$ and/or $n$ increases, the doublets get weaker and their effects more localized, but they can never be guaranteed to go away. (In fact, there exist functions $f$ whose Pad´e approximants have so many spurious poles that the sequence of $( n , n )$ approximants is unbounded for every $z \neq 0$ [Perron 1929, Wallin 1972].) The same applies if $f$ is meromorphic, i.e., analytic apart from poles, or if it has more complicated singularities such as branch points. All this is true in exact mathematics, and when there are rounding errors on a computer, the doublets become ubiquitous.

Despite these complexities, important theorems have been proved. The theorem of de Montessus de Ballore [1902] concerns the case of $m \to \infty$ with fixed $n$ , guaranteeing convergence in a disk about $z = 0$ if $f$ has exactly $n$ poles there. The Nuttall– Pommerenke theorem [Nuttall 1970, Pommerenke 1973] concerns $m = \pi \to \infty$ and ensures convergence for meromorphic $f$ not pointwise but in measure or in capacity, these being precise notions that require accuracy over most of a region as $m , n \to \infty$ while allowing for localized anomalies. This result was powerfully generalized for functions with branch points by Stahl [1997], who showed that as $n  \infty$ , almost all the poles of type $( n , n )$ Pad´e approximants line up along branch cuts that have a property of minimal capacity in the $z ^ { - 1 }$ -plane. For discussion of these results see [Baker & Graves-Morris 1996]. There are also analogous results for multipoint Pad´e approximation and other forms of rational interpolation. For example, an analogue of the de Montessus de Ballore theorem for interpolation as in the last chapter was proved by Saff [1972].

As a practical matter, these complexities of convergence are well combated by the SVD approach we have described, which can be regarded as a method of regularization of the Pad´e problem.

For reasons explained in the last chapter, the whole discussion of this chapter has been based on the behavior of a function $f ( z )$ at $z = 0$ rather than this book’s usual context of a function $f ( x )$ on an interval such as $[ - 1 , 1 ]$ . There is an analogue of Pad´e approximation for $[ - 1 , 1 ]$ called Chebyshev–Pad´e approximation, developed by Hornecker [1956], Maehly [1963], Frankel and Gragg [1973], Clenshaw and Lord [1974], and Geddes [1981]. The idea is to consider the analogue of (27.3) for Chebyshev series rather than Taylor series:

$$
( f - r _ { m n } ) ( x ) = O ( T _ { \mathrm { m a x i m u m } } ( x ) ) .
$$

(The Maehly version starts from the analogue of the linearized form (27.5).) In analogy to Theorem 27.1, it turns out that any $r \in \mathcal { R } _ { m n }$ satisfying $( f - r ) ( x ) =$ $O ( T _ { m + n + 1 - d } ( x ) )$ is the unique Chebyshev–Pad´e approximant according to this definition, but now, there is no guarantee that such a function $T$ exists. For theoretical details, see [Trefethen & Gutknecht 1987], and for computations in Chebfun, there is a code chebpade. As of today, there has not yet been a study of Chebyshev–Pad´e approximation employing the SVD-based robustness ideas described in this chapter for Pad´e approximation.

For extensive information about Pad´e approximation, see the book by Baker and Graves-Morris [1996]. However, that monograph uses an alternative definition according to which a Pad´e approximant exists only if (27.4) can be satisfied, and in fact the present treatment is mathematically closer to the landmark review of Gragg [1972], which uses the definition (27.3).

Summary of Chapter 27. Pad´e approximation is the generalization of Taylor polynomials to rational approximation, that is, rational interpolation at a single point. Pad´e approximants are characterized by a kind of equioscillation condition and can be computed robustly by an algorithm based on the SVD. The analogue on the interval $[ - 1 , 1 ]$ is known as Chebyshev–Pad´e approximation.

Exercise 27.1. Pad´e approximation of a logarithm. Show from Theorem 27.1 that the function $f ( z ) = \log ( 1 + z )$ has Pad´e approximants $r _ { 0 0 } = 0$ , $r _ { 1 , 0 } ( z ) = z$ , $r _ { 0 1 } ( z ) = 0$ , and $r _ { 1 1 } = z / ( 1 + \textstyle { \frac { 1 } { 2 } } z )$ .

Exercise 27.2. Reciprocals and exponentials. (a) Suppose $r _ { m n }$ is the type $( m , n )$ Pad´e approximant to a function $f$ with $f ( 0 ) \neq 0$ . Show that $1 / r _ { m n }$ is the type $( n , m )$ Pad´e approximant to $1 / f$ . (b) As a corollary, state a theorem relating the $( m , n )$ and $( n , m )$ Pad´e approximants of $e ^ { z }$ .

Exercise 27.3. Prescribed block structures. Devise functions $f$ with the following structures in their Pad´e tables, and verify your claims numerically by color plots for $0 \leq$ $m , n \leq 2 0$ . (a) $3 \times 3$ blocks everywhere. (b) $1 \times 1$ blocks everywhere, except that $r _ { 1 1 } =$ $r _ { 2 1 } = r _ { 1 2 } = r _ { 2 2 }$ . (c) $1 \times 1$ blocks everywhere, except that all $r _ { m n }$ with $n \leq 2$ are the same.

Exercise 27.4. Order stars. The order star of a function $f$ and its approximation $r$ is the set of points $z$ in the complex plane for which $| f ( z ) | = | r ( z ) |$ . Use the MATLAB contour command to plot the order stars of the Pad´e approximations $r _ { 1 1 }$ , $r _ { 2 2 }$ , $r _ { 3 2 }$ , and $r _ { 2 3 }$ to $e ^ { z }$ . Comment on the behavior near the origin.

Exercise 27.5. Nonsingularity and normality. Show that for a given $f$ and $( m , n )$ , the Pad´e approximation $r _ { m n }$ has defect $d = 0$ if and only if the square matrix obtained by deleting the first column of (27.8) is nonsingular. (If all such matrices are nonsingular, the Pad´e table of $f$ is accordingly normal, with all its entries distinct.)

Exercise 27.6. Arbitrary patterns of square blocks? Knowing that degeneracies in the Pad´e table always occupy square blocks, one might conjecture that, given any tiling of the quarter-plane $m \geq 0$ , $n \geq 0$ by square blocks, there exists a function $f$ with this pattern in its Pad´e table. Prove that this conjecture is false. (Hint: Consider the case where the first two rows of the table are filled with $2 \times 2$ blocks [Trefethen 1984].)

Exercise 27.7. Continued fractions and the Pad´e table. If $d _ { 0 } , d _ { 1 } , \ldots$ is a sequence of numbers, the continued fraction

$$
d _ { 0 } + \frac { d _ { 1 } z } { 1 + \displaystyle \frac { d _ { 2 } z } { 1 + \cdot \cdot \cdot } }
$$

is shorthand for the sequence of rational functions

$$
d _ { 0 } , \ d _ { 0 } + d _ { 1 } z , \ d _ { 0 } + { \frac { d _ { 1 } z } { 1 + d _ { 2 } z } } , \ldots ,
$$

known as convergents of the continued fraction. (a) Show that if $d \sb { 0 } , \ldots , d \sb { k - 1 } \neq 0$ and $d _ { k } = 0$ , then (27.15) defines a rational function $r ( z )$ , and determine its exact type. (b) Assuming $d _ { k } \neq 0$ for all $k$ , show that the convergents are the Pad´e approximants of types $( 0 , 0 ) , ( 1 , 0 ) , ( 1 , 1 ) , ( 2 , 1 ) , ( 2 , 2 ) , \ldots$ of a certain formal power series.
