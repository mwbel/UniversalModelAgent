Thus for $\pmb { n } > N ( \pmb { \varepsilon } )$

$$
\left| \int _ { - 1 } ^ { 1 } \cdot { \cal L } _ { n - 1 } ( f , T ; x ) d x - \int _ { - 1 } ^ { 1 } f ( x ) d x \right| < 4 \varepsilon .
$$

The theorem is proved.

Remark. Fejér [4] proves this theorem in the more general case that $f$ is Riemann integrable on I.

Although the sequence of interpolating polynomials in the zeros of the Chebyshev polynomial does not converge uniformly to every continuous function, we conclude this chapter on a positive note by showing that this sequence does converge in the mean. As a by-product we thus obtain another proof of Theorem 1.6.

Theorem 1.7. If $f$ is continuous on $I _ { : }$ then

$$
\operatorname * { l i m } _ { n \to \infty } \int _ { - 1 } ^ { 1 } \left[ f ( x ) - L _ { n } ( f , T ; x ) \right] ^ { 2 } \frac { d x } { \sqrt { 1 - x ^ { 2 } } } = 0 .
$$

Proof. As in the proof of Theorem 1.6,given $\pmb { \varepsilon }$ satisfying $0 < \varepsilon < 1$ ,let $\pmb { p } ( \pmb { x } ) \in \mathcal { P } _ { \pmb { N } }$ be a polynomial satisfying

$$
| f ( x ) - p ( x ) | < \varepsilon , \qquad x \in I ;
$$

then

$$
\int _ { - 1 } ^ { 1 } [ f ( x ) - p ( x ) ] ^ { 2 } { \frac { d x } { \sqrt { 1 - x ^ { 2 } } } } < \varepsilon ^ { 2 } \pi .
$$

If $\pmb { n } > N$ , then $L _ { n } ( p , T ; x ) = p ( x ) ;$ hence

$$
\begin{array} { r l r } {  { \int _ { - 1 } ^ { 1 } [ L _ { n } ( f , T ; x ) - p ( x ) ] ^ { 2 } \frac { d x } { \sqrt { 1 - x ^ { 2 } } } = \int _ { - 1 } ^ { 1 } [ L _ { n } ( f - p , T ; x ) ] ^ { 2 } \frac { d x } { \sqrt { 1 - x ^ { 2 } } } } } \\ & { } & { = \int _ { - 1 } ^ { 1 } [ \overset { n + 1 } { \underset { i = 1 } { \sum } } \{ f ( \xi _ { i } ^ { ( n + 1 ) } ) - p ( \xi _ { i } ^ { ( n + 1 ) } ) \} l _ { i , n + 1 } ( T ; x ) ] ^ { 2 } \frac { d x } { \sqrt { 1 - x ^ { 2 } } } } \\ & { } & { = \underset { i = 1 } { \overset { n + 1 } { \sum } } \frac { \pi } { n + 1 } \{ f ( \xi _ { i } ^ { ( n + 1 ) } ) - p ( \xi _ { i } ^ { ( n + 1 ) } ) \} ^ { 2 } < \pi \varepsilon ^ { 2 } , \qquad ( 1 } \end{array}
$$

where we have used Exercises 1.5.20 and 1.5.21. The theorem now follows from (1.138) and (1.139), in view of the inequality $( A - B ) ^ { 2 } \leqslant 2 ( A ^ { 2 } + B ^ { 2 } ) ;$ which, in turn, is a consequence of the identity $( A - B ) ^ { 2 } + ( A + B ) ^ { 2 }$ $= 2 ( A ^ { 2 } + B ^ { 2 } )$

Remark 1. Since $( 1 - x ^ { 2 } ) ^ { 1 / 2 } \leqslant 1$ on $I _ { \ast }$ , Theorem 1.7 implies that

$$
\operatorname* { l i m } _ { n \to \infty } \int _ { - 1 } ^ { 1 } [ f ( x ) - L _ { n } ( f , T ; x ) ] ^ { 2 } d x = 0 ,
$$

and Theorem 1.6 follows by Schwarz's inequality. An application of the same inequality shows that (1.131) is also a consequence of Theorem 1.7.

Remark 2. Much more than Theorem 1.7 is known to be true. Erdos and Feldheim (cf. Feldheim [1]) have shown that

$$
\operatorname * { l i m } _ { n  \infty } \int _ { - 1 } ^ { 1 } | f ( x ) - L _ { n } ( f , T ; x ) | ^ { p } \frac { d x } { \sqrt { 1 - x ^ { 2 } } } = 0
$$

for all $\pmb { p } > \mathbf { 0 } .$ .The theory of mean convergence with respect to other sets of nodes and weight function is discussed in Askey [2].

# EXERCISES 1.5.26-1.5.67

1.5.26.The Chebyshev polynomials also enjoy orthogonality properties on finite point sets in $I ;$ for example, show that if $\xi _ { 1 } , \ldots , \xi _ { n }$ are the zeros of $T _ { n } ( x )$ then

$$
\sum _ { j = 1 } ^ { n } T _ { k } ( \xi _ { j } ) T _ { m } ( \xi _ { j } ) = \left\{ \begin{array} { l l } { ( - 1 ) ^ { p } + ( - 1 ) ^ { q } } & { \quad \mathrm { i f ~ } \left\{ k + m = 2 p n \right. } \\ { \qquad \mathrm { a n d } \qquad \quad } \\ { \qquad \left\{ k - m \right\} = 2 q n , } \\ { \qquad \mathrm { i f ~ } \left\{ k + m = 2 \sin n \right. } \\ { \qquad \mathrm { a n d } \qquad \quad } \\ { \qquad \left\{ k - m \right\} \neq 2 m n } \\ { \qquad \quad } \\ { \qquad \mathrm { o r ~ } \left\{ \begin{array} { l l } { [ k - m ] = 2 s n } \\ { \mathrm { a n d } \qquad \quad } \\ { k + m \neq 2 r n , } \\ { \qquad \mathrm { o t h e r w i s e } . } \end{array} \right. } \end{array} \right.
$$

1.5.27. Showthat thecoeffcients inthe Chebyshev expansionof $\pmb { p } \in \mathcal { P } _ { { \pmb n } - 1 }$

$$
p ( x ) = { \frac { A _ { 0 } } { 2 } } + A _ { 1 } T _ { 1 } ( x ) + \cdots + A _ { n - 1 } T _ { n - 1 } ( x ) ,
$$

can be obtained by the formula

$$
A _ { m } = \frac { 2 } { n } \sum _ { j = 1 } ^ { n } p ( \xi _ { j } ) T _ { m } ( \xi _ { j } ) , ~ m = 0 , 1 , \ldots , n - 1 .
$$

Note that (1.130) implies that

$$
\frac { 2 } { n } \sum _ { m = 0 } ^ { n - 1 } T _ { m } ( \xi _ { k } ) T _ { m } ( \xi _ { j } ) = \left\{ \begin{array} { l l } { 0 , } & { \quad j \ne k , } \\ { 1 , } & { \quad j = k . } \end{array} \right.
$$

# 1.5.28. Show that

$$
\int _ { - \infty } ^ { \infty } \mathbf { r } _ { t } ( \eta _ { t } ) r _ { t } ( \eta _ { t } ) \ d r _ { t } ^ { * } = \overbrace { 2 } ^ { ( 0 , 0 ) } = \overbrace { 2 } ^ { ( 0 , 0 ) } = \overbrace { ( ( \frac { \Omega _ { 0 } } { \Omega _ { t } } ) ^ { 2 } + ( \frac { \Omega _ { 0 } } { \Omega _ { t } } ) ^ { 2 } + ( \frac { \Omega _ { 0 } } { \Omega _ { t } } ) ^ { 2 } } ^ { ( 0 , 1 ) } = \overbrace { 2 } ^ { ( 0 , 0 ) }
$$

$$
\left( { \begin{array} { l l l } { 0 , } & & { k + m \neq 2 p n } \\ & & { { \mathrm { a n d } } } \\ & & { | k - m | \neq 2 q n , } \\ { n , } & & { k + m = 2 p n } \end{array} } \right)
$$

$$
\begin{array} { l } { { \left| k - m \right| = 2 q n , } } \\ { { \left| k + m = 2 p n \right. } } \end{array}
$$

$$
| k - m | \neq 2 q n
$$

$$
\pmb { k } + \pmb { m } \neq 2 p \pmb { n }
$$

$$
| k - m | = 2 q n ,
$$

where $\pmb { \eta } _ { 0 } , \dots , \pmb { \eta } _ { n }$ are the extrema of $T _ { n } ( x ) . \dagger$

Formula (1.144) is another “orthogonality” property of the Chebyshev polynomials.

Hint. cos ${ \pmb n } \pmb { \theta } = { \bf R } { \bf e } ( e ^ { i n \theta } ) ,$

1.5.29. Show that

$$
\int _ { - 1 } ^ { 1 } f ( x ) \frac { d x } { \sqrt { 1 - x ^ { 2 } } } = \frac { \pi } { n } \sum _ { i = 0 } ^ { n } f ( \eta _ { i } ^ { ( n ) } ) , \qquad f \in \mathcal { P } _ { 2 n - 1 } .
$$

Hint.Verify (1.145) for $T _ { 0 } , T _ { 1 } , . . . , T _ { 2 n - 1 }$ .The formula is variously named after Lobatto and Markov.

1.5.30. Show that there is no quadrature formula

$$
\int _ { - 1 } ^ { 1 } f ( x ) { \frac { d x } { \sqrt { 1 - x ^ { 2 } } } } = c _ { 0 } f ( - 1 ) + \sum _ { i = 1 } ^ { n - 1 } c _ { i } f ( x _ { i } ) + c _ { n } f ( 1 )
$$

exact for $f \in \mathcal { P } _ { m }$ with $m \geqslant 2 n ,$ ,and (1.145) is the only formula of this type exact for $f \in \mathscr { P } _ { 2 n - 1 }$

Hint. Show that (1.145) cannot hold for $f \in \mathcal { P } _ { 2 n }$ ,and then show that if(1.146) holds it must coincide with (1.145).

# 1.5.31. If

$$
x ^ { n } = \sum _ { j = 0 } ^ { n } B _ { j } ^ { ( n ) } T _ { j } ( x ) ,
$$

†The notation $\pmb { \Sigma ^ { \prime \prime } }$ is defined in (1.99).

show that

$$
B _ { n - 2 k } ^ { ( n ) } = 2 ^ { 1 - n } { \binom { n } { k } } , \qquad k = 0 , \ldots , { \binom { n } { 2 } } ,
$$

and that

$$
B _ { j } ^ { ( n ) } = 0 , ~ j \neq n - 2 k .
$$

1.5.32. If

$$
\sum _ { k = 0 } ^ { n } a _ { k } x ^ { k } = \sum _ { k = 0 } ^ { n } A _ { k } T _ { k } ( x ) ,
$$

then

$$
A _ { k } = { \frac { 1 } { 2 ^ { k - 1 } } } \left[ a _ { k } + \sum _ { j = 1 } ^ { [ ( n - k ) / 2 ] } { \frac { { \binom { k + 2 j } { j } } a _ { k + 2 j } } { 2 ^ { 2 j } } } \right] .
$$

1.5.33. If

$$
T _ { n } ^ { \prime } ( x ) = \sum _ { j = 0 } ^ { n - 1 } A _ { j } T _ { j } ( x ) ,
$$

show that $A _ { j } \geqslant 0 .$ For which $j$ is $A _ { j } = 0 ?$

Hint. See Exercise 1.2.13.

# 1.5.34. If

$$
T _ { n } ^ { ( k ) } ( x ) = \sum _ { j = 0 } ^ { n - k } A _ { j k } T _ { j } ( x ) , \qquad k = 0 , 1 , 2 , . . . , n ,
$$

show that

$$
A _ { j k } \geqslant 0 , \qquad k = 0 , 1 , \ldots , n , \qquad j = 0 , 1 , \ldots , n - k .
$$

For which $j$ is $A _ { j k } = 0 ?$

Hint.Use mathematical induction on $\pmb { k }$ and Exercise 1.5.33.

# 1.5.35. Show that

$$
| T _ { n } ^ { ( k ) } ( x ) | \leqslant T _ { n } ^ { ( k ) } ( 1 ) , \qquad x \in I , \qquad k = 0 , 1 , \ldots , n ,
$$

with equality only for $x = \pm 1 , k \geqslant 1$ ，thus generalizing Exercise 1.2.4,in view of Exercise 1.5.6.

Hint.This result follows immediately from Exercise 1.5.34.

# 1.5.36. (Feldheim [1]) Show that

$$
[ l _ { k , n } ( T ; \cos \theta ) ] ^ { 2 } = { \frac { 2 } { n } } \sum _ { m = 0 } ^ { 2 n - 2 } \cos m \theta _ { k } \cos m \theta + { \frac { 1 } { n ^ { 2 } } } \sum _ { m = 2 } ^ { 2 n - 2 } c _ { m , k } \cos m \theta ,
$$

where

$$
c _ { m , k } = { \frac { \sin m \theta _ { k } \cos \theta _ { k } - m \cos m \theta _ { k } \sin \theta _ { k } } { \sin \theta _ { k } } } , ~ k = 1 , \ldots , n .
$$

Hint. Use (1.130).

1.5.37. Show that

$$
\sum _ { k = 1 } ^ { n } [ l _ { k , n } ( T ; \cos { \theta } ) ] ^ { 2 } = \left\{ \begin{array} { l l } { \displaystyle 1 - \frac { 1 } { 2 n } + \frac { \sin { ( 2 n - 1 ) \theta } } { 2 n \sin { \theta } } , } & { \quad 0 < \theta < \pi , } \\ { \displaystyle 2 - \frac { 1 } { n } , } & { \quad \theta = 0 , \pi . } \end{array} \right.
$$

Hint. Sum (1.149) and recall Exercises 1.2.13 and 1.5.26.

# 1.5.38. Show that

$$
\operatorname* { l i m } _ { n \to \infty } \sum _ { k = 1 } ^ { n } [ l _ { k , n } ( T ; x ) ] ^ { 2 } = { \binom { 1 , } { 2 , } } \quad \quad x = \pm 1 .
$$

[Compare this result with Exercise 1.4.9.It is interesting to remark here, that although the problem of finding an array of nodes $\pmb { X }$ ,such that

$$
\operatorname* { m a x } _ { - 1 \leqslant x \leqslant 1 } \sum _ { k = 1 } ^ { n } | l _ { k , n } ( X ; x ) |
$$

is minimum is unsolved,the analogous problem of finding an array of nodes such that

$$
\operatorname* { m a x } _ { - 1 \leqslant x \leqslant 1 } \sum _ { k = 1 } ^ { n } { [ l _ { k , n } ( X ; x ) ] ^ { 2 } }
$$

is minimum has been solved (Fejer [3]). The array of nodes that produces the minimum of (1.150) consists of the zeros of

$$
F _ { n } ( x ) = \int _ { x } ^ { 1 } P _ { n - 1 } ( t ) d t ,
$$

where $\{ P _ { n } ( x ) \}$ are the Legendre polynomials,i.e., the ultraspherical polynomials with $\begin{array} { r } { \lambda = \frac { 1 } { 2 } . } \end{array}$ Remarkably enough the value of the minimum of (1.150) is i.]

1.5.39. Show that for each integer $m \geqslant 2$ and xeI

$$
\left( \sum _ { k = 1 } ^ { n } | l _ { k , n } ( T ; x ) | ^ { m } \right) ^ { 1 / m } \leqslant { \sqrt { 2 } } .
$$

Hint. First consider $m = 2 r$ and observe that, in notation suggested by Exercise 1.4.2,

$$
1 = \left[ \sum _ { k = 1 } ^ { n } v _ { k } ( T ) l _ { k } ^ { 2 } \right] ^ { r } \geqslant \sum _ { k = 1 } ^ { n } v _ { k } ^ { r } l _ { k } ^ { 2 r } .
$$

Then use Schwarz's inequality for the odd m. Compare with Exercise 1.4.9.

# 1.5.40. Show that

$$
\operatorname* { m a x } _ { - 1 \leqslant x \leqslant 1 } \vert l _ { 1 , n } ( T ; x ) \vert = \vert l _ { 1 , n } ( T ; 1 ) \vert
$$

and the sequence $\vert l _ { 1 , n } ( T ; 1 ) \vert$ is monotone increasing, with $\pmb { n } _ { : }$ to $4 / \pi$

# 1.5.41. If $n \geqslant 3$ and

$$
\operatorname* { m a x } _ { - 1 \leqslant x \leqslant 1 } | l _ { j , n } ( T ; x ) | = | l _ { j , n } ( T ; u _ { j } ) | , \qquad j = 2 , \ldots , n - 1 ,
$$

then, if $\begin{array} { r } { u _ { j } = \cos \alpha _ { j } , } \end{array}$ ，we have [recalling the notation of (1.16)]

$$
\vert \alpha _ { j } - \theta _ { j } ^ { ( n ) } \vert < \frac { \pi } { 2 n } .
$$

Hint. Apply the M. Riesz theorem (Exercise1.3.20)to $l _ { j , n } ( T ; \cos \theta ) { \in } \mathcal { T } _ { n - 1 }$

1.5.42. With the same hypothesis and notation as in Exercise 1.5.41 show that for $j = 2 , . . . , n - 1$ ，

$$
\frac { 1 - \xi _ { j } u _ { j } } { 1 - \xi _ { j } ^ { 2 } } \geqslant \frac { 1 3 } { 1 8 } .
$$

Hint. If $\theta _ { j } ^ { ( n ) } = 3 \mu ,$ then $\theta _ { j } ^ { ( n ) } - \pi / ( 2 n ) \geqslant 2 \mu ;$ hence

$$
A = \frac { \cos { ( \theta _ { j } ^ { ( n ) } - \pi / 2 n ) } - \cos { \theta _ { j } ^ { ( n ) } } } { 1 - \cos { \theta _ { j } ^ { ( n ) } } } \leqslant \frac { \cos { 2 \mu } - \cos { 3 \mu } } { 1 - \cos { 3 \mu } } \leqslant \frac { 5 } { 9 } ,
$$

so that

$$
A \frac { \cos \theta _ { j } ^ { ( n ) } } { 1 + \cos \theta _ { j } ^ { ( n ) } } \leqslant \frac { 5 } { 1 8 } .
$$

1.5.43. Show that for $j = 2 , . . . , n - 1$ ,and ${ \pmb n } \geqslant 3$

$$
( l _ { j , n } ( T ; u _ { j } ) ) ^ { 2 } < \frac { 1 8 } { 1 3 } < \left( \frac { 1 + \sqrt { 2 } } { 2 } \right) = ( l _ { 1 , 2 } ( T ; 1 ) ) ^ { 2 } .
$$

Hint. Recall Exercise 1.4.1.

1.5.44. (Erdos and Grunwald [1]) Show that for $\pmb { n } \geqslant 1$

$$
\operatorname* { s u p } _ { n } \operatorname* { m a x } _ { j } \ \operatorname* { m a x } _ { - 1 \leqslant x \leqslant 1 } | l _ { j , n } ( T ; x ) | = \frac { 4 } { \pi } .
$$

Hint. Put together the four preceding exercises. Compare with Exercise 1.4.10.

# 1.5.45. Prove that

$$
T _ { n } ( x ) = \left| \begin{array} { l l l l l l l } { 2 x } & { - 1 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { - 1 } & { 2 x } & { - 1 } & { \cdots } & { } & { 0 } & { 0 } \\ { 0 } & { - 1 } & { 2 x } & { - 1 } & { \cdots } & { 0 } & { 0 } \\ { \vdots } & { \vdots } & { \vdots } & { \vdots } & { } & { \vdots } & { \vdots } \\ { 0 } & { 0 } & { 0 } & { \cdots } & { - 1 } & { 2 x } & { - 1 } \\ { 0 } & { 0 } & { 0 } & { \cdots } & { 0 } & { - 1 } & { x } \end{array} \right| ,
$$

where the determinant is $n \times n .$ 、Also show that the corner elements $\pmb { x }$ and ${ \mathfrak { z } } { \mathfrak { x } }$ can be interchanged.

Hint. Expand in terms of elements of the first column and use (1.101).

# 1.5.46. (Korsak and Schubert [1]) Prove that

$$
D = { \left| \begin{array} { l l l l l l l l } { 1 } & { - 2 x } & { 1 } & { \cdots } & & & { 0 } & { 0 } \\ { 0 } & { 1 } & { - 2 x } & { 1 } & { \cdots } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } & { - 2 x } & { 1 } & { \cdots } & { 0 } & { 0 } \\ { \vdots } & { \vdots } & { \vdots } & { \vdots } & { \vdots } & { \vdots } & { \vdots } \\ { 0 } & { 0 } & { 0 } & { \cdots } & & { 1 } & { - 2 x } & { 1 } \\ { 1 } & { 0 } & { 0 } & { \cdots } & & { 0 } & { 1 } & { - 2 x } \\ { - 2 x } & { 1 } & { 0 } & { \cdots } & & & { 0 } & { 1 } \end{array} \right| } = 2 ( 1 - T ^ { n } ( x ) ) ,
$$

where $\pmb { D }$ is $\pmb { n } \times \pmb { n }$

Hint. Show that $\pmb { D }$ is zero at $x = \eta _ { k } , k = 0 , 2 , 4 , . . .$ , by establishing that

$$
T _ { 0 } ( \eta _ { k } ) C _ { 1 } + \cdots + T _ { n - 1 } ( \eta _ { k } ) C _ { n } = 0 ,
$$

where $C _ { j }$ is the $j$ th column vector of the matrix of $\pmb { D }$ .Then show that if $\boldsymbol { x } \in \boldsymbol { I }$ and

$$
E = { \left| \begin{array} { l l l l l l l } { 1 } & { - \tau } & { 0 } & { \cdots } & { } & { 0 } \\ { 0 } & { 1 } & { - \tau } & { \cdots } & { } & { 0 } \\ { 0 } & { 0 } & { 1 } & { - \tau } & { \cdots } & { 0 } \\ { \vdots } & { \vdots } & { \vdots } & { \vdots } & { \vdots } & { \vdots } \\ { 0 } & { \cdots } & { } & { } & { 0 } & { 1 } & { - \tau } \\ { - \tau } & { \cdots } & { } & { } & { } & { 0 } & { 1 } \end{array} \right| } ,
$$

where $\tau = x - \sqrt { x ^ { 2 } - 1 }$ ,then

$$
\pmb { D } = \pmb { \bar { E } } \cdot \pmb { E } \geqslant \pmb { 0 } ,
$$

where $\bar { E }$ is the complex conjugate of $\pmb { { \cal E } }$

1.5.47. If $x , y \geqslant 1$ then

$$
T _ { n } ( x y ) \leqslant T _ { n } ( x ) T _ { n } ( y ) .
$$

Hint. Fix $y \geqslant 1$ and apply Exercise 1.5.11 to $p ( x ) = T _ { n } ( x y ) / T _ { n } ( x ) T _ { n } ( y ) .$

1.5.48. If $\mathbf { 0 } \leqslant j , k$ and $j + k \leqslant n$ then

$$
y ^ { k } T _ { n } ^ { ( j + k ) } ( x y ) \leqslant T _ { n - j } ^ { ( k ) } ( x ) T _ { n } ^ { ( j ) } ( y )
$$

for $x , y \geqslant 1$

Hint. Fix $y \geqslant 1$ and put $\begin{array} { r } { p ( x ) = T _ { n } ^ { ( j ) } ( x y ) / T _ { n } ^ { ( j ) } ( y ) , } \end{array}$ so that $\pmb { p } \in \mathcal { P } _ { { \pmb { n } } - j }$ Exercise 1.5.34 implies that $| p ( x ) | \leqslant 1$ for $\boldsymbol { x } \in \boldsymbol { I }$ and we can then invoke Exercise 1.5.11 again to show that $| p ^ { ( k ) } ( x ) | \leqslant T _ { n - j } ^ { ( k ) } ( x ) .$ Exercise 1.5.47 is the case $\pmb { k } = j = 0$

1.5.49. Upon putting $x = y = 1$ in Exercise 1.5.48 we obtain

$$
T _ { n } ^ { ( j + k ) } ( 1 ) \leqslant T _ { n - j } ^ { ( k ) } ( 1 ) T _ { n } ^ { ( j ) } ( 1 ) ,
$$

a result which is not exactly obvious from (1.97).

1.5.50. Suppose that $\pmb { u } \geqslant \pmb 0$ and $v = \log T _ { n } ( e ^ { u } )$ . Show that

$$
\frac { d ^ { 2 } v } { d u ^ { 2 } } \leqslant 0 , \qquad u \geqslant 0 ,
$$

i.e., the curve in the ${ \pmb u } - { \pmb v }$ plane described by $v = \log T _ { n } ( e ^ { u } )$ is concave for nonnegative $\pmb { u }$

Hint.The desired inequality is equivalent to

$$
\left[ { \frac { x T _ { n } ^ { \prime } ( x ) } { T _ { n } ( x ) } } \right] ^ { \prime } = \left( \sum _ { j = 1 } ^ { n } { \frac { x } { x - \xi _ { j } } } \right) ^ { \prime } \leqslant 0 , \qquad x \geqslant 1 ,
$$

(use Exercise 1.3.2c), which, in turn, is the same as

$$
\sum _ { j = 1 } ^ { n } { \frac { \xi _ { j } } { ( x - \xi _ { j } ) ^ { 2 } } } \geqslant 0 , \qquad x \geqslant 1 .
$$

Now utilize the symmetry of the $\xi _ { j }$

# 1.5.51. Show that

$$
T _ { n } ( r ) T _ { n } ( s ) \leqslant T _ { n } ( x ) T _ { n } ( y ) , \qquad 1 \leqslant r \leqslant x \leqslant y \leqslant s , \qquad r s = x y .
$$

Hint.Fix r and s.Observe that the curve ${ \pmb v } = { \pmb v } ( { \pmb u } )$ described in Exercise 1.5.50 is concave and hence does not lie below the line segment joining the points $( a , v ( a ) )$ and $( b , v ( b ) )$ where $\pmb { a } = \pmb { \mathrm { l o g } } r$ and $\pmb { b } = \pmb { 1 0 } \pmb { \mathrm { g } } s$ for $a \leqslant u \leqslant b$ In particular consider $\pmb { u } = \mathbf { l o g } , \pmb { x } ,$ log y.

Note that the argument can be reversed so that the inequalities in this and the preceding exercise are equivalent. Also if $r = 1$ we recover the result of Exercise 1.5.47. Exercises 1.5.47-1.5.51 come from Askey,Gasper and Harris [1] where generalizations can also be found.

1.5.52. Verify that for any constant, $\pmb { c } ,$

$$
Q _ { n } ( x ) = T _ { n } ( x ) + ( 1 - c ) U _ { n - 2 } ( x )
$$

satisfies $Q _ { 0 } ( x ) = c , Q _ { 1 } ( x ) = x$ and

$$
Q _ { n } ( x ) = 2 x Q _ { n - 1 } ( x ) - Q _ { n - 2 } ( x ) , ~ n = 2 , 3 , \ldots .
$$

Hint.Exercise 1.5.19 and (1:101).

# 1.5.53. Show that

$$
U _ { n - 1 } ( y ) = { \frac { 1 } { \pi } } \int _ { - 1 } ^ { 1 } { \frac { T _ { n } ( x ) - T _ { n } ( y ) } { x - y } } { \frac { d x } { \sqrt { 1 - x ^ { 2 } } } } , \qquad n = 0 , 1 , 2 , \ldots .
$$

Another normalization of the Chebyshev polynomials is sometimes useful. We put

$$
C _ { n } ( x ) = 2 T _ { n } { \bigg ( } { \frac { x } { 2 } } { \bigg ) } , \qquad S _ { n } ( x ) = U _ { n } { \bigg ( } { \frac { x } { 2 } } { \bigg ) } , \qquad n = 0 , 1 , 2 , \ldots .
$$

In view of (1.96) and Exercise 1.5.13 we have

$$
C _ { n } ( x ) = \sum _ { k = 0 } ^ { [ n / 2 ] } ( - 1 ) ^ { k } { \frac { n } { n - k } } { \binom { n - k } { k } } x ^ { n - 2 k } ,
$$

and

$$
S _ { n } ( x ) = \sum _ { k = 0 } ^ { [ n / 2 ] } ( - 1 ) ^ { k } { \binom { n - k } { k } } x ^ { n - 2 k } .
$$

Note that the renormalized Chebyshev polynomials are monic,i.e., have leading coefficient 1,and have integer coefficients. They are useful in revealing algebraic and number theoretic aspects of the Chebyshev polynomials, as we shall see.

# 1.5.54. Show that

(a) $C _ { n } ( x ) = x C _ { n - 1 } ( x ) - C _ { n - 2 } , n \geqslant 2 ,$ with ${ \cal C } _ { \mathfrak { o } } ( { \pmb x } ) = 2$ and $C _ { 1 } ( x ) = x$ (b) $S _ { n } ( x ) = x S _ { n - 1 } ( x ) - S _ { n - 2 } , n \geqslant 2 ,$ with $\pmb { S } _ { 0 } ( \pmb { x } ) = 1$ and $\pmb { S } _ { 1 } ( \pmb { x } ) = \pmb { x }$

1.5.55. Verify that

$$
\int _ { - 2 } ^ { 2 } C _ { k } ( x ) C _ { m } ( x ) \frac { d x } { \sqrt { 1 - \frac { x ^ { 2 } } { 4 } } } = \left\{ \begin{array} { l l } { 0 , } & { m \neq k , } \\ { 4 \pi , } & { m = k \neq 0 , } \\ { 8 \pi , } & { m = k = 0 . } \end{array} \right.
$$

$$
\int _ { - 2 } ^ { 2 } S _ { k } ( x ) S _ { m } ( x ) \sqrt { 1 - \frac { x ^ { 2 } } { 4 } } d x = \left\{ 0 , \qquad m \ne k , \right.
$$

Thus the renormalized Chebyshev polynomials are sequences of orthogonal polynomials on the interval [-2,2].

1.5.56. Show that the positive integers defined by

$$
F _ { n + 1 } = \frac { S _ { n } ( i ) } { i ^ { n } } , \qquad n = 0 , 1 , 2 , \ldots , ( i ^ { 2 } = - 1 ) ,
$$

$\displaystyle F _ { 0 } = 0$ satisfy

$$
F _ { n + 1 } = F _ { n } + F _ { n - 1 } , \qquad n = 0 , 1 , 2 , \ldots .
$$

Therefore, $\left\{ F _ { n } \right\}$ is the sequence of Fibonacci numbers,0,1,1,2,3,5,.... There is a vast literature and a journal, The Fibonacci Quarterly, devoted to this sequence. The interested reader should consult Knuth [1] and the references given there.

1.5.57. Use the definition of the Fibonacci numbers given in Exercise 1.5.56 to show that:

$$
F _ { n + 1 } = \sum _ { k = 0 } ^ { [ n / 2 ] } { \binom { n - k } { k } } .
$$

$$
F _ { n + 1 } F _ { n - 1 } - F _ { n } ^ { 2 } = ( - 1 ) \sp n .
$$

Hint. See Exercise 1.5.19.

(c) (Binet's Formula)

$$
\begin{array} { l } { { \displaystyle F _ { n } \dot { = } \frac { 1 } { \sqrt { 5 } } \left[ \left( \frac { 1 + \sqrt { 5 } } { 2 } \right) ^ { n } - \left( \frac { 1 - \sqrt { 5 } } { 2 } \right) ^ { n } \right] } } \\ { { \displaystyle ~ = \frac { 1 } { \sqrt { 5 } } \left( \varphi ^ { n } - ( 1 - \varphi ) ^ { n } \right) , \quad \varphi = ( 1 + \sqrt { 5 } ) / 2 . } } \end{array}
$$

Hint.Exercise 1.2.20.

$$
F _ { 2 n } = S _ { n - 1 } ( 3 ) , \qquad n = 0 , 1 , 2 , \ldots .
$$

Hint. Use Binet's formula, the fact that $( 1 \pm { \sqrt { 5 } } ) ^ { 2 } = 2 ( 3 \pm { \sqrt { 5 } } )$ and Exercise 1.2.20.

Note that we now have

$$
{ \frac { S _ { 2 n - 1 } ( i ) } { i } } = ( - 1 ) ^ { n - 1 } S _ { n - 1 } ( 3 ) .
$$

Similarly, show that $F _ { 2 n - 1 } = S _ { n - 1 } ( 3 ) - S _ { n - 2 } ( 3 ) .$

1.5.58. Show that the positive integers defied by

$$
L _ { n } = \frac { C _ { n } ( i ) } { i ^ { n } } , \qquad n = 0 , 1 , 2 , \ldots ,
$$

satisfy

$$
L _ { n + 1 } = L _ { n } + L _ { n + 1 } , \qquad n = 1 , 2 , \ldots .
$$

$\left\{ L _ { n } \right\}$ is the sequence of Lucas numbers, 2,1,3,4, 7...

1.5.59.Use the definition of Lucas numbers given in Exercise 1.5.58 to show that:

$$
L _ { n } = \sum _ { k = 0 } ^ { [ n / 2 ] } { \frac { n } { n - k } } { \binom { n - k } { k } } .
$$

$$
L _ { n + 1 } L _ { n - 1 } - L _ { n } ^ { 2 } = ( - 1 ) ^ { n - 1 } 5 .
$$

# Hint. See Exercise 1.5.18.

$$
\begin{array} { c } { { L _ { n } = \left( \displaystyle \frac { 1 + \sqrt { 5 } } { 2 } \right) ^ { n } + \left( \displaystyle \frac { 1 - \sqrt { 5 } } { 2 } \right) ^ { n } } } \\ { { = \varphi ^ { n } + ( 1 - \varphi ) ^ { n } . } } \end{array}
$$

Hint.Exercise 1.1.1

$$
L _ { n } = F _ { n + 1 } + F _ { n - 1 } , n = 1 , 2 , \ldots .
$$

Hint. Exercise 1.2.15a.

It is clear that we are now in a position to generate many identities satisfied by the Fibonacci and Lucas numbers from identities involving the Chebyshev polynomials, such as those given in Exercises 1.2.13 and 1.2.15.We leave this task to the interested reader.

We turn next to some properties of the Chebyshev polynomials of complex arguments.

1.5.60. If $\pmb { z }$ is a complex number satisfying $| z | \geqslant 1$ then

$$
| T _ { n } ( z ) | \geqslant | T _ { n - 1 } ( z ) | , \qquad n \geqslant 1 .
$$

Equality holds if,and only if, $z = \pm 1$ for ${ \pmb n } > 1$ ,or $| z | = 1$ for $\pmb { n = 1 }$

Hint. Use the three-term recurrence formula.

1.5.61. If ${ \bf 0 } < { \bf R }$ then

$$
\operatorname* { m a x } _ { 0 \leqslant \theta < 2 \pi } | T _ { n } ( R e ^ { i \theta } ) | = | T _ { n } ( i R ) | ,
$$

and

$$
\operatorname* { m a x } _ { 0 \leqslant \theta < 2 \pi } | U _ { n } ( \dot { R } e ^ { i \theta } ) | = | U _ { n } ( i R ) | .
$$

Hint. Use (1.96) and Exercise 1.5.13.

# 1.5.62. Show that

$$
\operatorname* { m a x } _ { 0 \leqslant \theta < 2 \pi } | C _ { n } ( e ^ { i \theta } ) | = L _ { n } ,
$$

and

$$
\operatorname* { m a x } _ { 0 \leqslant \theta < 2 \pi } | U _ { n } ( e ^ { i \theta } ) | = F _ { n + 1 } .
$$

# 1.5.63. Show that

$$
{ \frac { T _ { n } ( i ) } { i ^ { n } } } = { \frac { 1 } { 2 } } \left( ( 1 + { \sqrt { 2 } } ) ^ { n } + ( 1 - { \sqrt { 2 } } ) ^ { n } \right) = \sum _ { j = 0 } ^ { [ n / 2 ] } { \binom { n } { 2 j } } \ 2 ^ { j } , \qquad n = 0 , 1 , \ldots .
$$

The next group of exercises in this chapter presents a result of Erdos which generalizes Exercise 1.5.11 to complex $\pmb { t }$ in the case $\pmb { k } = \pmb { 0 }$

1.5.64. Suppose $- 1 \leqslant t _ { i } \leqslant 1 , i = 1 , \ldots , k , z _ { 1 } , \ldots , z _ { k }$ are given complex numbers and

$$
G _ { k } ( t _ { 1 } , \dots , t _ { k } ) = t _ { 1 } z _ { 1 } + \cdots + t _ { k } z _ { k } .
$$

Show that

$$
\operatorname* { m a x } _ { t _ { 1 } , \dots , t _ { k } } | G _ { k } | = | G _ { k } ( \varepsilon _ { 1 } , \dots , \varepsilon _ { k } ) |
$$

if, and only if, $\varepsilon _ { i } , \mathrm { i } = 1 , . . . , k$ are appropriately chosen elements of $\{ - 1 , 1 \}$ ·

Hint. Suppose the result were false and the maximum in question to be attained when $t _ { k }$ ,say, satisfies $- 1 < t _ { k } < 1$ (and $\pmb { z } _ { k } \neq 0 .$ 0. Then if $G _ { k - 1 } = t _ { 1 } z _ { 1 } + \cdots + t _ { k - 1 } z _ { k - 1 } ,$ we have

$$
| G _ { k - 1 } + t _ { k } z _ { k } | ^ { 2 } = | G _ { k - 1 } | ^ { 2 } + t _ { k } ^ { 2 } | z _ { k } | ^ { 2 } + 2 t _ { k } \operatorname { R e } { \bar { z } } _ { k } < | G _ { k - 1 } + \varepsilon z _ { k } | ^ { 2 }
$$

for an $\mathfrak { E } \in \{ - 1 , 1 \}$

1.5.65. Suppose $\mathfrak { z } _ { i } \in \{ - 1 , 1 \} , \ i = 1 , \ldots , k , \ z _ { j } = \rho _ { j } e ^ { i \varphi _ { j } } , \ j = 1 , \ldots , k ,$ are given distinct nonzero complex numbers having the property that

$$
| \varphi _ { j } - \varphi _ { i } | \leqslant \frac { \pi } { 2 } , \qquad i , j = 1 , \ldots , k
$$

and

$$
H _ { k } ( \varepsilon _ { 1 } , \dots , \varepsilon _ { k } ) = \varepsilon _ { 1 } z _ { 1 } + \dots + \varepsilon _ { k } z _ { k } .
$$

Show that

$$
\operatorname* { m a x } _ { \varepsilon _ { 1 } , \ldots , \varepsilon _ { k } } | H _ { k } | = | z _ { 1 } + \cdots + z _ { k } | ,
$$

Hint. Let $z _ { j } = x _ { j } + i y _ { j } , x _ { j } \geqslant 0 , y _ { j } \geqslant 0 , j = 1 , . . . , k .$ Then

$$
| H _ { k } | ^ { 2 } = { \bigg ( } \sum _ { j = 1 } ^ { k } \varepsilon _ { j } x _ { j } { \bigg ) } ^ { 2 } + { \bigg ( } \sum _ { j = 1 } ^ { k } \varepsilon _ { j } y _ { j } { \bigg ) } ^ { 2 } .
$$

1.5.66. (Erdos [2]) If $\pmb { p } \in \mathcal { P } _ { \pmb { n } }$ (and the coefficients of $\pmb { p }$ are real) and

$$
| p ( \eta _ { j } ^ { ( n ) } ) | \leqslant 1 , \qquad j = 0 , \ldots , n ,
$$

then for any complex number $\zeta$ satisfying $| \zeta | \geqslant 1$

$$
| p ( \zeta ) | \leqslant | T _ { n } ( \zeta ) | .
$$

Equality hold only for $p = \pm T _ { n }$

Hint.

$$
p ( \zeta ) = \sum _ { j = 0 } ^ { n } t _ { j } l _ { j } ( U ; \zeta )
$$

where $t _ { j } = p ( \eta _ { j } ^ { ( n ) } )$ satisfies $- 1 \leqslant t _ { j } \leqslant 1$ , and (Exercise 1.5.7)

$$
l _ { j } ( U ; \zeta ) = \frac { ( \zeta ^ { 2 } - 1 ) T _ { n } ^ { \prime } ( \zeta ) } { n ^ { 2 } } \frac { ( - 1 ) ^ { j } } { \zeta - \eta _ { j } } , ~ j = 1 , \dots , n - 1
$$

(and half that quantity for $j = 0 , n \}$ .In view of Exercise 1.5.64, $| p ( \zeta ) |$ will be maximal if $t _ { j } = \pm 1$ .But then the hypotheses of Exercise 1.5.65 are in effect if we observe that the angle subtended at $\zeta \left( \left| \zeta \right| \geqslant 1 \right)$ exceeds ${ \pmb { \pi } } / 2 .$ .This leads to the conclusion that $| p ( \zeta ) |$ is maximal if

$$
p ( \zeta ) = \pm \sum _ { j = 0 } ^ { n } ( - 1 ) ^ { j } l _ { j } ( \zeta ) = \pm T _ { n } ( \zeta ) .
$$

1.5.67. If $\pmb { p } \in \pmb { \mathcal { P } _ { n } }$ has real coefficients and

$$
| p ( \eta _ { j } ^ { ( n ) } ) | \leqslant 1 , \qquad j = 0 , \ldots , n ,
$$

then

$$
\operatorname* { m a x } _ { | z | \leqslant 1 } | p ( z ) | \leqslant | T _ { n } ( i ) | , \qquad n = 0 , 1 , 2 , \ldots
$$

with equality only if $p = \pm T _ { n }$ . See also Exercise 1.5.6.

Hint.The maximum principle for analytic functions and Exercises 1.5.66 and 1.5.61.

There is an extension, due to Kemperman [1], of the Erdos inequality, given in Exercise 1.5.66, to derivatives of polynomials. Namely, if $\pmb { p } \in \mathcal { P } _ { \pmb { n } }$ is real-valued and

$$
| p ( \eta _ { j } ^ { ( n ) } ) | \leqslant 1 , \qquad j = 0 , \ldots , n ,
$$

then for any complex number $\zeta$ satisfying $| \zeta | \geqslant u _ { n , k }$ ,where ${ u } _ { n , k }$ is the largest zero of $T _ { n } ^ { ( k - 1 ) } ( x ) ;$ we- have

$$
| p ^ { ( k ) } ( \zeta ) | \leqslant | T _ { n } ^ { ( k ) } ( \zeta ) | , \qquad k = 1 , \ldots , n .
$$

The proof uses the following generalization of the observation made in Exercise 1.5.66.

Proposition. Let the zeros of real-valued $\pmb q \in \mathcal { P } _ { m }$ be $y _ { 1 } < y _ { 2 } < \cdots < y _ { m }$ Let $\pmb { p } \in \mathscr { P } _ { m }$ satisfy

$$
| p ( x _ { j } ) | \leqslant | q ( x _ { j } ) | , \qquad j = 0 , 1 , \ldots , m
$$

where $x _ { 0 } < y _ { 1 } < x _ { 1 } < \cdots < y _ { m } < x _ { m }$ .Then

$$
| p ( \zeta ) | \leqslant | q ( \zeta ) |
$$

holds for each complex number $\zeta$ outside the open disc with diameter $[ x _ { 0 } , x _ { m } ]$ .The equality in (1.152) can hold only on the boundary of that disc unless $p = \pm q$

Proof. Let $r ( x ) = ( x - x _ { 0 } ) \cdots ( x - x _ { m } ) ,$ then

$$
p ( \zeta ) = r ( \zeta ) \sum _ { j = 0 } ^ { n } \frac { p ( x _ { j } ) } { r ^ { \prime } ( x _ { j } ) ( \zeta - x _ { j } ) } .
$$

Since $p ( x _ { j } ) = t _ { j } q ( x _ { j } )$ where $- 1 \leqslant t _ { j } \leqslant 1 , j = 0 , . . . , n$ we obtain

$$
p ( \zeta ) = r ( \zeta ) \sum _ { j = 0 } ^ { n } t _ { j } \frac { q ( x _ { j } ) } { r ^ { \prime } ( x _ { j } ) ( \zeta - x _ { j } ) } .
$$

Now $q ( x _ { j } ) / r ^ { \prime } ( x _ { j } )$ are nonzero and of the same sign, $j = 0 , \ldots , n ,$ and if $\zeta$ is outside the above-mentioned open disc then the complex numbers $( \zeta - x _ { j } ) ^ { - 1 }$ all lie in a sector whose angle does not exceed $\pmb { \pi } / 2$ Hence $| p ( \zeta ) |$ attains its maximum when either $t _ { j } = 1$ or $t _ { j } = - 1 , j = 0 , \ldots , n ,$ thus establishing (1.152). The statement about equality is now easily verifed, and the Proposition is established.

According to Exercise 1.5.9, $T _ { n } ^ { ( k - 1 ) } ( z ) = 0$ implies

$$
| p ^ { ( k ) } ( z ) | \leqslant | T _ { n } ^ { ( k ) } ( z ) | , \qquad k = 1 , \ldots , n .
$$

But now if we invoke the Proposition with $\pmb { p } , \pmb { q }$ and m replaced by $\pmb { p } ^ { ( k ) }$ ， $T _ { n } ^ { ( k ) }$ and $n - k ,$ respectively, (the $\boldsymbol { x } _ { j }$ being the zeros of $T _ { n } ^ { ( k - 1 ) }$ and the $y _ { j }$ the zeros of $T _ { n } ^ { ( k ) }$ then (1.152) implies (1.151).

#

# EXTREMAL PROPERTIES

One of the most remarkable properties of the Chebyshev polynomial, $T _ { n } ( x ) ,$ is that $\widetilde { T } _ { n } ( x )$ (the Chebyshev polynomial normalized so that its leading coeffcient is 1) has the smallest maximum absolute value on $I \colon [ - 1 , 1 ]$ among all $p ( x ) = x ^ { n } + a _ { n - 1 } x ^ { n - 1 } + \cdots + a _ { 0 }$ [cf. (1.109)] (This property is one basis for the wide utility of the Chebyshev polynomials in numerical analysis,a topic to which we turn in Chapter 3.) Let us begin by proving this fact. We recall that if $g ( x )$ is continuous on $\pmb { I }$

$$
\| g \| = \operatorname* { m a x } _ { - 1 \leqslant x \leqslant 1 } | g ( x ) | .
$$

Theorem 2.1. If $p ( x ) = x ^ { n } + a _ { n - 1 } x ^ { n - 1 } + \cdots + a _ { 0 } ,$ then

$$
\| p \| \geqslant \| \widetilde { T } _ { n } \| = \left\{ 2 ^ { 1 - n } , \qquad n > 0 , \right.
$$

with equality only if $p = \widetilde { T } _ { n }$

Proof. Suppose that $\pmb { n } > \mathbf { 0 }$ and $\Vert \boldsymbol { p } \Vert \leqslant \Vert \widetilde { T } _ { n } \Vert = 2 ^ { 1 - n } ;$ then $| p ( x ) | \leqslant 2 ^ { 1 - n }$ throughout $\pmb { I }$ and $\tilde { T } _ { n } ( \eta _ { k } ) = ( - 1 ) ^ { k } 2 ^ { 1 - \bar { n } } ,$ $k = 0 ,$ ...， $\textbf { \em n } [ \eta _ { k }$ are as defined in (1.19)]. Suppose that $p \neq { \tilde { T } } _ { n }$ ，then $q = \tilde { T } _ { n } - p \in \mathcal { P } _ { n - 1 }$ and is not identically zero. Suppose that $q ( \eta _ { 0 } ) = \cdots = q ( \eta _ { k - 1 } ) = 0 ,$ $q ( \eta _ { k } ) \neq 0$ and $q ( \pmb { \eta } _ { m } ) \neq 0$ but $q ( \eta _ { m + 1 } ) = \cdots = q ( \eta _ { n } ) = 0$ Since $\pmb q$ is not the zero polynomial, $k \leqslant n$ and $\pmb { m } \geqslant \mathbf { 0 } .$ Note now that if $q ( \eta _ { i } ) \neq 0 ,$ ，then sg $\mathrm { n } q ( \bar { \eta } _ { i } ) = \mathrm { s g n } \ \tilde { T } _ { n } ( \eta _ { i } ) = ( - 1 ) ^ { i }$ Supposethat $q ( \eta _ { i } ) \neq 0 ,$ $q ( \eta _ { i + 1 } ) = \cdots = q ( \eta _ { i + ( j - 1 ) } ) = 0 ,$ $q ( \eta _ { i + j } ) \neq 0$ Then certainly $\pmb q$ has at least $j - 1$ zeros in $[ \eta _ { i } , \eta _ { i + j } ] ;$ but if $j$ is even sgn $q ( \eta _ { i } ) = \mathrm { s g n } q ( \eta _ { i + j } )$ and so $\pmb q$ has an even number of zeros (counting multiple zeros as many times as their multiplicity) in $[ \eta _ { i } , \eta _ { i + j } ]$ ,hence at least $j$ zeros. Ifj is odd,sgn $q ( \eta _ { i } ) = - \operatorname { s g n } q ( \eta _ { i + j } )$ and so $\pmb q$ has an odd number of zeros (counting multiple zeros as many times as their multiplicity) in $[ \eta _ { i } , \eta _ { i + j } ] ,$ hence at least $j$ zeros. Thus $\pmb q$ has at least $j$ zeros in $[ \eta _ { i } , \eta _ { i + j } ] ,$ hence at least $m - k$ zeros in $[ \pmb { \eta } _ { k } , \pmb { \eta } _ { m } ]$ .But $\pmb q$ also has $\pmb { k }$ zeros in $[ \eta _ { 0 } , \eta _ { k } ]$ and $n - m$ zeros in $[ \eta _ { m } , \eta _ { n } ] ,$ ，making a total of $( m - k ) + k + ( n - m ) = n$ zeros in I. Since $q \in { \mathcal { P } } _ { n - 1 } , q = 0$ . Thus either $\| \pmb { p } \| > \| \widetilde { T } _ { \pmb { n } } \|$ or $p = \widetilde { T } _ { n }$

Corollary 2.1.1. If $p ( { \boldsymbol { x } } ) = a _ { 0 } + a _ { 1 } { \boldsymbol { x } } + \cdots + a _ { k } x ^ { k } , a _ { k } \neq 0 ,$ and $p \neq a _ { k } \widetilde T _ { k }$ ,then there exist $\boldsymbol { x } _ { 0 } \in I$ such that

$$
| p ( x _ { 0 } ) | > { \frac { | a _ { k } | } { 2 ^ { k - 1 } } } .
$$

Theorem 2.1 has two interesting reinterpretations:

A.The polynomial in $\mathcal { P } _ { n - 1 }$ closest to the function $f ( x ) = x ^ { n } ;$ ，where closeness is measured by $\| f - p \| , p \in { \mathcal { P } } _ { n - 1 } .$ is

$$
p ^ { * } = x ^ { n } - \tilde { T } _ { n } .
$$

B. Among all $\pmb { p } \in \pmb { \mathcal { P } _ { n } }$ satisfying $\| \pmb { p } \| = 1$ the largest value of

$$
| F p | = \left| \frac { p ^ { ( n ) } ( 0 ) } { n ! } \right|
$$

is $2 ^ { n - 1 }$ and this value is assumed only for $p = \pm T _ { n }$

(A) is an example of a rich mathematical area, the uniform approximation of functions by polynomials,and (B) is an example of the problem of maximizing a linear functional on the space $\mathcal { P } _ { \pmb { n } }$ . To see how the Chebyshev polynomials fit into these larger schemes we next explore both areas in some detail.

# A. UNIFORM APPROXIMATION OF CONTINUOUS FUNCTIONS

# 2.1. Convex Sets in n-Space

Our investigation of uniform approximation wil be quite wide-ranging on its circuitous route back to the Chebyshev polynomials. For this purpose we need some preliminary material about convex sets in real and complex ndimensional spaces, $\mathbb { R } ^ { n }$ and $\mathbb { C } ^ { n }$ , respectively.

Definition 2.1. A set, S, in $\mathbb { R } ^ { n }$ or $\mathbb { C } ^ { n }$ is convex if $s _ { 1 } , ~ s _ { 2 } , ~ \in S$ implies $\lambda s _ { 1 } + ( 1 - \lambda ) s _ { 2 } \in S$ for $0 \leqslant \lambda \leqslant 1$ ；that is, together with any two points $\pmb { s }$ contains the line segment joining them.

Definition 2.2. If nonnegative numbers $\lambda _ { 1 } , \ldots , \lambda _ { m }$ satisfy

$$
\sum _ { i = 1 } ^ { m } \lambda _ { i } = 1
$$

and $y _ { 1 } , \ldots , y _ { m } \in \mathbb { R } ^ { n } , \mathbb { C } ^ { n } ,$

$$
\sum _ { i = 1 } ^ { m } \lambda _ { i } y _ { i }
$$

is called a convex combination of $y _ { 1 } , \ldots , y _ { m }$

Definition 2.3. Given a set S,form the set $\hat { s } ,$ of all convex combinations of points of S. $\hat { s }$ is called the convex hull of S.

Theorem 2.2(Carathéodory). Let S be a subset of $\mathbb { R } ^ { n }$ and $\boldsymbol { y }$ a point of S. Then there exists a subset ${ \pmb S } _ { 1 }$ of S, containing at most ${ \pm 1 }$ points, such that $y \in \hat { S } _ { 1 }$ Indeed, given any $z \in \mathbb { R } ^ { n }$ ，we may choose $\pmb { S _ { 1 } }$ to consist of $\pmb { z }$ and at most $\pmb { n }$ points of S.

Proof. If we can prove this result for ${ \pmb z } = { \bf 0 }$ ,namely,for any subset of $\mathbb { R } ^ { n } , B ,$ and $w \in \widehat { B } .$

$$
w = \sum _ { i = 1 } ^ { r } \mu _ { i } b _ { i } , \qquad \mu _ { i } \geqslant 0 , \qquad \sum _ { i = 1 } ^ { r } \mu _ { i } \leqslant 1 ,
$$

where $r \leqslant n$ and $\boldsymbol { b } _ { i } \in \boldsymbol { B } ,$ ,then it is true for arbitrary $\pmb { z }$ in $\pmb { n }$ -space. For given S and $y \in \hat { S }$ let $B = \left\{ x \in \mathbb { R } ^ { n } | x = s - z , s \in S \right\}$ . Then $\boldsymbol { w } = \boldsymbol { y } - \boldsymbol { z } \in \hat { B }$ ;hence

$$
y - z = \sum _ { i = 1 } ^ { r } \mu _ { i } b _ { i } = \sum _ { i = 1 } ^ { r } \mu _ { i } ( s _ { i } - z ) , \qquad s _ { i } \in S .
$$

Thus

$$
y = \left( 1 - \sum _ { i = 1 } ^ { r } \mu _ { i } \right) z + \sum _ { i = 1 } ^ { r } \mu _ { i } s _ { i } .
$$

Suppose then that $z = 0 .$ If $y = 0 , \ y = z$ and the theorem is proved. Suppose that $y \neq 0 .$ Since $y \in { \hat { S } } ,$ there exist $\begin{array} { r } { s _ { 1 } , \dotsc , s _ { r } \in S } \end{array}$ and positive $\lambda _ { 1 } , \ldots , \lambda _ { r }$ which satisfy

$$
\sum _ { i = 1 } ^ { r } \lambda _ { i } \leqslant 1
$$

such that

$$
y = \sum _ { i = 1 } ^ { r } \lambda _ { i } s _ { i } .
$$

We show that if $r$ is chosen to be the least integer such that (2.1) and (2.2) hold, then $r \leqslant n .$ Suppose that $r > n ;$ then the ${ \pmb s } _ { \pmb i }$ are linearly dependent and we can find real numbers $c _ { i }$ such that

$$
\sum _ { i = 1 } ^ { r } c _ { i } \geqslant 0
$$

(in particular, at least one $c _ { i }$ is positive) and

$$
\sum _ { i = 1 } ^ { r } c _ { i } s _ { i } = 0 .
$$

If $\pmb { t }$ is any real number, we have

$$
y = \sum _ { i = 1 } ^ { r } \ ( \lambda _ { i } - t c _ { i } ) s _ { i } .
$$

The numbers $t _ { i } ( t ) = \lambda _ { i } - t c _ { i }$ are all positive for $\pmb { t = 0 }$ ,hence for positive and sufficiently small $t .$ .Since at least one $c _ { i }$ is positive, there is a smallest positive value of $\pmb { t } ,$ say $\pmb { t } ^ { \prime }$ ,such that at least one of the $t _ { i } ( t )$ vanishes. [Note that none of the $t _ { i } ( t ^ { \prime } )$ is negative and at least one of them is positive, since $y \neq 0 . ]$ Thus

$$
y = \sum _ { i = 1 } ^ { r } ~ t _ { i } ( t ^ { \prime } ) s _ { i }
$$

and at least one of $t _ { i } ( t ^ { \prime } ) = 0$ ,but

$$
\sum _ { i = 1 } ^ { r } \ t _ { i } ( t ^ { \prime } ) = \sum _ { i = 1 } ^ { r } \ \lambda _ { i } - t ^ { \prime } \sum _ { i = 1 } ^ { r } c _ { i } \leqslant 1 ,
$$

which contradicts the assumed minimal property of $r$

Remark. Since $\mathbb { C } ^ { n }$ is isomorphic to $\mathbb { R } ^ { 2 n }$ Theorem 2.2 remains valid when S is a subset of $\mathbb { C } ^ { n }$ with ${ \pmb S } _ { 1 }$ containing at most $2 n + 1$ points,and similar appropriate changes are made in the final sentence of the statement of Theorem 2.2 as well.

Definition 2.4. If $\pmb { x } \colon ( \pmb { x _ { 1 } } , \ldots , \pmb { x _ { n } } )$ and y: $( y _ { 1 } \ldots , y _ { n } )$ are two points of $\mathbb { C } ^ { n }$ $( x , y ) = x _ { 1 } { \bar { y } } _ { 1 } + \cdots + x _ { n } { \bar { y } } _ { n }$ is called the inner product of $\pmb { x }$ and y; $d ( x , y ) = ( x - y , x - y ) ^ { 1 / 2 }$ is the distance between $\pmb { x }$ and $y$

Theorem 2.3 (Separating Hyperplane Theorem). Let $c$ be a closed convex set not containing the origin in $\mathbb { R } ^ { n }$ .Then there exists a hyperplane, $\pmb { H }$ , defined by $h ( x ) = ( x , a ) + b = 0$ such that $h ( 0 ) < 0$ and $h ( x ) > 0$ for all $\ b { x } \in { C }$ ; that is, $\pmb { H }$ strictly separates $c$ from 0.

Proof. Since $c$ is closed, there exists a point of $C , x ^ { * }$ which is closest to the origin. Take

$$
h ( x ) = { \bigg ( } x - { \frac { x ^ { * } } { 2 } } , x ^ { * } { \bigg ) } .
$$

Then $h ( 0 ) = - \frac { 1 } { 2 } ( x ^ { * } , x ^ { * } ) < 0$ and $\begin{array} { r } { h ( x ^ { * } ) = \frac { 1 } { 2 } ( x ^ { * } , x ^ { * } ) > 0 . } \end{array}$

We claim that $h ( x ) > 0$ for all $\ b { x } \in { C }$ 、Suppose it is not, that $\pmb { x } ^ { \prime } \in \pmb { C }$ and $h ( x ^ { \prime } ) \leqslant 0$ Then

$$
( x ^ { \prime } , x ^ { * } ) \leqslant { \frac { 1 } { 2 } } ( x ^ { * } , x ^ { * } ) .
$$

Since $\pmb { x } ^ { \prime }$ and ${ \pmb x } ^ { \ast } \in { \pmb C }$ ,every point $\lambda x ^ { \prime } + ( 1 - \lambda ) x ^ { * }$ ， $0 \leqslant \lambda \leqslant 1$ ,is in $c$ ,but if

$$
\begin{array} { r l } & { f ( \lambda ) = ( \lambda x ^ { \prime } + ( 1 - \lambda ) x ^ { * } , \lambda x ^ { \prime } + ( 1 - \lambda ) x ^ { * } ) } \\ & { \qquad = \lambda ^ { 2 } ( x ^ { \prime } , x ^ { \prime } ) + 2 \lambda ( 1 - \lambda ) ( x ^ { \prime } , x ^ { * } ) + ( 1 - \lambda ) ^ { 2 } ( x ^ { * } , x ^ { * } ) , } \end{array}
$$

we have $f ( 0 ) = ( x ^ { * } , x ^ { * } )$ and $f ^ { \prime } ( 0 ) = 2 ( x ^ { \prime } , x ^ { * } ) - 2 ( x ^ { * } , x ^ { * } ) < 0 ,$ in view of (2.3). Thus there is a point of $c$ closer to O than $x ^ { * }$ ,contradicting the definition of $x ^ { * }$ 、

Remark. Theorem 2.3 remains valid for $C \in \mathbb { C } ^ { n }$ if we put $h ( x ) =$ $\mathbb { R e } ( ( x , a ) + b ) .$

# EXERCISES 2.1.1-2.1.5

2.1.1. Show that $c$ is convex if,and only if, every convex combination of points of $c$ is contained in $c$

2.1.2. If $S \subset \mathbb { R } ^ { n } ( \mathbb { C } ^ { n } )$ , show that $\hat { s }$ is convex.

2.1.3. Show that $\pmb { S } \subset \widehat { \pmb { S } } .$

2.1.4. Show that $\hat { s }$ is the smallst convex set containing S.

2.1.5. Show that if $\pmb { s }$ is compact then $\hat { s }$ is also.

# 2.2. Characterization of Best Approximations

We are now in a position to discuss a quite general problem of uniform approximation. The setting is as follows. Let $\pmb { B }$ be a compact set in m-space and let $C ( B )$ be the set of (real or complex-valued) continuous functions on $\pmb { B } _ { : }$

equipped with the uniform (or Chebyshev) norm; that is,if ${ \pmb { g } } \in C ( { \pmb { B } } ) ,$

$$
\| g \| = \operatorname* { m a x } _ { y \in B } | g ( y ) | .
$$

Associated with each ${ \pmb g } \in C ( { \pmb B } )$ is its (nonempty) set of critical points,

$$
E ( g ; B ) = \{ y \in B / | g ( y ) | = \| g \| \} .
$$

Note that $E ( g ; B )$ is closed, hence compact.

Given $V ,$ a $\pmb { k }$ -dimensional subspace of $C ( B ) ,$ our objective is to characterize the elements of $V$ that are closest to a given $f \in C ( B ) ,$ closeness being measured by the uniform norm. The entire theoretical foundation of our endeavors is contained in the following result.

Theorem 2.4. Suppose ${ \pmb g } \in C ( { \pmb B } )$ and $\varphi _ { 1 } , \ldots , \varphi _ { k }$ is any basis for $V .$ Let $\pmb { K }$ be the set in $\pmb { k }$ -space described by $\langle \overline { { g ( y ) } } \varphi _ { 1 } ( y ) ,$ …， $\overline { { g ( y ) } } \varphi _ { k } ( y ) )$ as $\pmb { y }$ runs through $E ( g ; B )$ .Then

$$
\| g + v \| \geqslant \| g \| , \qquad \mathrm { a l l } \ v \in V
$$

if, and only if, the origin in $k$ -space is in the convex hull of some subset of $r$ points of $\pmb { K }$ ,where $r \leqslant k + 1$ in the real case (i.e., when $C ( B )$ consists of realvalued functions) and $r \leqslant 2 k + 1$ points in the complex case.

Proof. (i) Suppose that $y _ { 1 } , \ldots , y _ { r }$ are points of $E ( g ; B )$ such that

$$
0 = \sum _ { i = 1 } ^ { r } \lambda _ { i } \overline { { ( g ( y _ { i } ) } } \varphi _ { 1 } ( y _ { i } ) , \ldots , \overline { { g ( y _ { i } ) } } \varphi _ { k } ( y _ { i } ) ) ,
$$

where $\lambda _ { i } \geqslant 0$ and $\Sigma _ { i = 1 } ^ { r } \lambda _ { i } = 1$ Then

$$
0 = \sum _ { i = 1 } ^ { r } \lambda _ { i } { \overline { { g ( y _ { i } } } ) } \varphi _ { j } ( y _ { i } ) , \qquad j = 1 , \ldots , k ;
$$

hence, for any $v \in V ,$

$$
0 = \sum _ { i = 1 } ^ { r } \lambda _ { i } \overline { { g ( y _ { i } ) } } v ( y _ { i } )
$$

and

$$
0 = { \bf R e } \sum _ { i = 1 } ^ { r } \lambda _ { i } \overline { { g ( y _ { i } ) } } v ( y _ { i } ) = \sum _ { i = 1 } ^ { r } \lambda _ { i } { \bf R e } \overline { { g ( y _ { i } ) } } v ( y _ { i } ) ,
$$

so that for each ${ \boldsymbol { v } } \in V$ there exists $i ( v )$ such that

$$
\mathbb { R } \mathrm { e } \overline { { g ( y _ { i } ) } } v ( y _ { i } ) \geqslant 0 .
$$

Given any $v _ { \mathrm { { : } } }$ fix $_ i$ so that (2.5) holds; then

$$
\begin{array} { c } { \| g + v \| ^ { 2 } \geqslant | g ( y _ { i } ) + v ( y _ { i } ) | ^ { 2 } = [ g ( y _ { i } ) + v ( y _ { i } ) ] \cdot [ \overline { { g ( y _ { i } ) } } + \overline { { v ( y _ { i } ) } } ] } \\ { \geqslant \| g \| ^ { 2 } + | v ( y _ { i } ) | ^ { 2 } + 2 \operatorname { R e } \overline { { g ( y _ { i } ) } } v ( y _ { i } ) \geqslant \| g \| ^ { 2 } , } \end{array}
$$

thus establishing (2.4).

(ii) Suppose that (2.4) holds and $\| g \| = 1 . ( \mathbf { I f } \| g \| = 0$ ,the theorem is trivial. If $0 < \| g \| \neq 1$ ，continue the proof with $g _ { 0 } = g / \| g \|$ ，with no loss in generality.)

If $\hat { K }$ is the convex hull of $\pmb { K }$ , we show that $\mathbf { 0 } \in { \hat { K } }$ . Suppose that $0 \notin \hat { K }$ . Since $\pmb { K }$ is compact, so is $\hat { K }$ and there exists a hyperplane that separates O from $\hat { K }$ according to Theorem 2.3; that is, there exist complex numbers $c _ { 0 } , \ldots , c _ { k }$ $( c _ { 0 } \neq 0 )$ such that the half-space

$$
\operatorname { R e } ( c _ { 0 } + c _ { 1 } z _ { 1 } + \cdots + c _ { k } z _ { k } ) \geqslant 0
$$

contains $\hat { K }$ but $- \tau = \mathbb { R e } c _ { 0 } < 0 ;$ that is, for all $y \in E ( g ; B )$

$$
\mathrm { R e } \left( \sum _ { j = 1 } ^ { k } c _ { j } \overline { { g ( y ) } } \varphi _ { j } ( y ) \right) \geqslant \tau > 0 ,
$$

or, putting $v _ { 0 } = \Sigma _ { j = 1 } ^ { k } c _ { j } \varphi _ { j } ,$

$$
\mathbf { R e } ~ \overline { { g ( y ) } } v _ { 0 } ( y ) \geqslant \tau > 0 , \qquad y \in E ( g ; ~ B ) .
$$

Let $U _ { \mathbf { 1 } }$ be an open set of m-space such that $E ( g ; B ) \subset U _ { 1 } \cap B = U _ { : }$ $\mathbb { R } \mathrm { e } \bar { g } v _ { 0 } \geqslant \tau / 2$ on $\pmb { U }$ and $| g ( y ) | \leqslant 1 - \delta ( \delta > 0 )$ on $B \backslash U$ ，which isclosed.Now choose $\pmb \varepsilon > \mathbf 0$ so that $\begin{array} { r } { \pmb { \varepsilon } \| \pmb { v } _ { 0 } \| < \delta ; } \end{array}$ then

$$
\operatorname* { m a x } _ { y \in B \setminus U } | g ( y ) - \varepsilon v _ { 0 } ( y ) | < 1 ,
$$

but on $\pmb { U }$

$$
\begin{array} { c l c r } { { | g ( y ) - \varepsilon v _ { 0 } ( y ) | ^ { 2 } = | g ( y ) | ^ { 2 } + \varepsilon ^ { 2 } | v _ { 0 } ( y ) | ^ { 2 } - 2 \varepsilon \mathrm { R e } \overline { { { g ( y ) } } } v _ { 0 } ( y ) } } \\ { { } } & { { } } \\ { { } } & { { \leqslant 1 + \varepsilon ^ { 2 } \| v _ { 0 } \| ^ { 2 } - \varepsilon \tau . } } \end{array}
$$

Since $\varepsilon ^ { 2 } \| v _ { 0 } \| ^ { 2 } - \varepsilon \tau < 0$ for $\pmb \varepsilon$ sufficiently small,

$$
| g ( y ) - \varepsilon v _ { 0 } ( y ) | < 1 , \qquad y \in U ,
$$

and putting $v = - \varepsilon v _ { 0 } , \| g + v \| < 1 = \| g \|$ ,contradicting (2.4). Thus $\boldsymbol 0 \in \hat { K }$ and an application of Caratheodory's theorem (Theorem 2.2) now proves our result.

Definition 2.5. $\mathbf { I f } f \in C ( B )$ is given and $\| f - v ^ { * } \| \leqslant \| f - v \|$ ,all $v \in V ,$ we call ${ \pmb v } ^ { * }$ a best approximation to $f$ (on $\pmb { B }$ ）out of $V ,$ and put

$$
\| f - v ^ { * } \| = E _ { V } ( f ) .
$$

(In case $V = \mathcal { P } _ { \pmb { n } }$ we write $E _ { n } ( f )$ for $E _ { \mathcal { P } _ { n } } ( f ) . )$

Theorem 2.5. $v ^ { * }$ is a best approximation to $f \in C ( B )$ out of $V ,$ if, and only if, there exist distinct points $y _ { 1 } , \ldots , y _ { r } \in E ( f - v ^ { * } ; B ) .$ ,and positive numbers $\lambda _ { 1 }$ ， $\cdots , \lambda _ { r }$ such that

$$
\sum _ { i = 1 } ^ { r } \lambda _ { i } { \overline { { [ f ( y _ { i } ) - v ^ { * } ( y _ { i } ) ] } } } v ( y _ { i } ) = 0 , \qquad { \mathrm { a l l ~ } } v \in V ,
$$

where $r \leqslant k + 1$ in the real case and $r \leqslant 2 k + 1$ in the complex case.

Proof. Replace $\pmb { g }$ by $f - v ^ { * }$ in Theorem 2.4.

Remark. Theorem 2.5 remains valid if $\pmb { v }$ in (2.6) is replaced by $\varphi _ { j } \operatorname { f o r } j = 1 ;$ ， $\cdots , k .$

A useful variant of the characterization of best approximations given in theorem 2.5 is based on the following considerations.

Definition 2.6. A signature in $B , \Sigma$ , is a continuous function whose domain is a closed subset of $\pmb { B }$ and whose range is in the unit circle in the complex plane. We call the domain of $\pmb { \Sigma }$ the base of the signature and denote it by $\sigma ( \Sigma ) ; \Sigma ^ { \prime }$ is a subsignature of $\pmb { \Sigma }$ if $\pmb { \Sigma ^ { \prime } }$ is the restriction of $\pmb { \Sigma }$ to a subset of $\pmb { \sigma } ( \pmb { \Sigma } )$

Definition 2.7. A signature, $\Sigma [ g ]$ ,is said to be associated with ${ \pmb g } \in C ( { \pmb B } )$ if $\sigma \subseteq E ( g ; B )$ and $\Sigma ( y ) = \operatorname { s g n } g ( y ) . \dag$ (Note that $g = 0$ can have no signature associated with it.)

Definition 2.8. A signature, $\pmb { \Sigma }$ ,is said to be extremal for $V$ if there exist (complex) numbers $\zeta _ { 1 } , \ldots , \zeta _ { s }$ and distinct points $y _ { 1 } , \ldots , y _ { s }$ of $\pmb { \sigma }$ such that

$$
\mathtt { s g n } \zeta _ { i } = { \overline { { \Sigma ( y _ { i } ) } } } , \qquad i = 1 , . . . , s
$$

and

$$
\sum _ { i = 1 } ^ { s } \ \zeta _ { i } v ( y _ { i } ) = 0 , \qquad \mathrm { a l l } \ v \in V ;
$$

tFor a complex number $z \neq 0 , \thinspace \mathbf { s g n } z = z / | z |$ and $\mathbf { s g n 0 } = \mathbf { 0 }$ (cf. Exercise 1.3.6).

$\zeta _ { 1 } , \ldots , \zeta _ { s }$ are called weights for $\pmb { \Sigma }$ . An extremal signature, $\pmb { \Sigma } _ { i }$ , is called primitive if it has no proper extremal subsignature.

We now obtain an immediate equivalent to Theorem 2.5 in terms of extremal signatures.

Theorem 2.6. A best approximation out of $V \uparrow \circ f \notin V$ is $v ^ { * }$ if, and only if, there exists an extremal signature for $V$ associated with $f - v ^ { * }$ based on $r$ points, where $r \leqslant k + 1$ in the real case and $r \leqslant 2 k + 1$ in the complex case.

Corollary 2.6.1 (Skeleton Theorem). If ${ \pmb v } ^ { * }$ is a best approximation to $f \notin V$ on $B ,$ it is also a best approximation to $f$ on the base of an extremal signature for $V$ consisting of r points, where $r \leqslant k + 1$ in the real case and $r \leqslant 2 k + 1$ in the complex case.

Proof. The base $\pmb { \sigma }$ of the extremal signature described in Theorem 2.6 works by applying Theorem 2.6, with $\pmb { B }$ replaced by ${ \pmb \sigma } .$

Corollary 2.6.2. Let $y _ { 1 } , \ldots , y _ { r }$ be the base of the extremal signature $\pmb { \Sigma }$ .Then, if $v ^ { * }$ is a best approximation to $f$ out of $\pmb { B }$ and $v \in V ,$

$$
\| f - v ^ { * } \| = E _ { V } ( f ) \geqslant \operatorname* { m i n } _ { 1 \leqslant i \leqslant r } \mathrm { R e } \overline { { \Sigma ( y _ { i } ) } } [ f ( y _ { i } ) - v ( y _ { i } ) ] .
$$

Proof. Choose weights for $\Sigma , \zeta _ { 1 } , \ldots , \zeta _ { r }$ , to satisfy

$$
\sum _ { i = 1 } ^ { r } | \zeta _ { i } | = 1
$$

(this can always be done). Then

$$
\begin{array} { r l } { E _ { \nu } ( f ) = \displaystyle \sum _ { i = 1 } ^ { \nu } | \xi _ { i } | | f ( \nu ) - \nu ^ { * } | | \geqslant \displaystyle \sum _ { i = 1 } ^ { \nu } | \xi _ { i } | | f ( y _ { i } ) - \nu ^ { * } ( y _ { i } ) | } \\ { \geqslant \displaystyle \left| \sum _ { i = 1 } ^ { \nu } \xi _ { i } | \int ( y _ { i } ) - \nu ^ { * } ( y _ { i } ) | \right| = \displaystyle \left| \sum _ { i = 1 } ^ { \nu } \zeta _ { i } | f ( y _ { i } ) - \nu ( y _ { i } ) | \right| } \\ { = \displaystyle \left| \sum _ { i = 1 } ^ { \nu } \xi _ { i } | \overline { { 2 ( y _ { i } ) } } \big [ f ( y _ { i } ) - \nu ( y _ { i } ) \big ] \right| } \\ { \geqslant \displaystyle \mathbb { R } \in \sum _ { i = 1 } ^ { \nu } | \xi _ { i } | \overline { { 2 ( y _ { i } ) } } \big [ f ( y _ { i } ) - \nu ( y _ { i } ) | \big ] } \\ { = \displaystyle \sum _ { i = 1 } ^ { \nu } | \xi _ { i } | \operatorname { R e } \frac { \overline { { \kappa } } } { 2 ( y _ { i } ) } \big [ f ( y _ { i } ) - \nu ( y _ { i } ) \big ] } \\ { \geqslant \displaystyle \operatorname* { s u p } _ { i \in \nu } \mathbb { R } \oplus \frac { \overline { { \kappa } } } { 2 ( y _ { i } ) } \big [ f ( y _ { i } ) - \nu ( y _ { i } ) \big ] } \\ { \geqslant \displaystyle \operatorname* { s u p } _ { i \in \nu } \mathbb { R } \oplus \frac { \overline { { \kappa } } } { 2 ( y _ { i } ) } \big [ f ( y _ { i } ) - \nu ( y _ { i } ) \big ] . } \end{array}
$$

# EXERCISES 2.2.1-2.2.15

2.2.1. (Kolmogorov Criterion) Show that ${ \pmb v } ^ { * }$ is a best approximation to $f$ if, and only if,

$$
\operatorname* { m i n } _ { y \in E ( f - v ^ { * } ; B ) } \mathrm { s g n } \overline { { [ f ( y ) - v ^ { * } ( y ) ] } } \cdot v ( y ) \leqslant 0 , \quad \mathrm { ~ e a c h ~ } v \in V .
$$

[Thus (2.6) and (2.9) are equivalent.]

Hint.Formula (2.6) implies (2.9). Then show that (2.9) implies that

$$
\| f - v \| ^ { 2 } \geqslant \| f - v ^ { * } \| ^ { 2 } .
$$

2.2.2. Any signature with an extremal subsignature is itself extremal.

2.2.3. Every extremal signature has a finitely based extremal subsignature.

2.2.4. If $\pmb { \Sigma }$ is an extremal signature for $V ,$ then for each ${ \pmb v } \in { \pmb V }$

$$
\operatorname* { m i n } _ { y \in \sigma ( \Sigma ) } { \mathrm { R e } } ( v ( y ) { \overline { { \Sigma ( y ) ) } } } \leqslant 0 .
$$

2.2.5. If (2.10) holds, there is an extremal subsignature of $\pmb { \Sigma }$ based on $r$ points, where $r \leqslant k + 1$ in the real case and $r \leqslant 2 k + 1$ in the complex case.

Hint. Formula (2.10) implies that O is a best approximation to $\pmb { \Sigma }$ on $\pmb { \sigma }$ out of $V .$

2.2.6. Every extremal signature has an extremal subsignature based on r points, where $r \leqslant k + 1$ in the real case and $r \leqslant 2 k + 1$ in the complex case.

Exercises 2.2.7-2.2.10 deal with the real case.

2.2.7. Points $y _ { 1 } , \ldots , y _ { r }$ of $\pmb { B }$ are the base of a primitive extremal signature for $V$ if, and only if, every set of $\boldsymbol { r } - 1$ columns of the $k \times r$ matrix

$$
\Phi _ { r } = \left( \begin{array} { l l l } { \varphi _ { 1 } ( y _ { 1 } ) } & { \ldots } & { \varphi _ { 1 } ( y _ { r } ) } \\ { \vdots } \\ { \varphi _ { k } ( y _ { 1 } ) } & { \ldots } & { \varphi _ { k } ( y _ { r } ) } \end{array} \right)
$$

is linearly independent and the rank of $\Phi _ { r }$ is $r - 1$

Hint. (i) If,say,the first $r - 1$ columns are linearly dependent, an argument similar to that used in the proof of Theorem 2.2 contradicts the primitivity of the extremal signature. (ii) If the rank is $r - 1$ ,the columns are linearly dependent.

2.2.8. No proper subset of the base of a primitive extremal signature is the base of an extremal signature.

2.2.9. If $\pmb { \Sigma }$ is a primitive extremal signature, the only extremal signatures based on $\pmb { \sigma } ( \pmb { \Sigma } )$ are $\pm \Sigma$

2.2.10. If $y _ { 1 } , \ldots , y _ { r }$ are the base of a primitive extremal signature for $V$ and $\pmb { J }$ is any set of $\boldsymbol { r } - 1$ distinct indices among $1 , \ldots , r ,$ then, given arbitrary $ { b _ { i } } ,  { j } \in J$ , there exists $v \in V$ such that

$$
v ( y _ { j } ) = b _ { j } , \qquad j \in J .
$$

2.2.11. We have avoided the question of whether a best approximation out of $V$ to a given $f \in C ( B )$ exists.The answer is that it always does.Fill in the details in the following sketch of a proof of this fact. Show that $\| f - \Sigma _ { i = 1 } ^ { k } a _ { i } \varphi _ { i } \|$ ，a continuous function of a: $( a _ { 1 } , \ldots , a _ { k } ) .$ , assumes its minimum by noting that, since O is a possible value of a, we need only consider a such that $\| \Sigma _ { i = 1 } ^ { k } a _ { i } \varphi _ { i } \| \leqslant 2 \| f \|$ ,and the set of such a is compact.

2.2.12. Show that $\Sigma ( \eta _ { i } ) = ( - 1 ) ^ { i } ;$ $i = 0 , \ldots , n ,$ is an extremal signature for $V = \mathcal { P } _ { n - 1 }$ based on the extrema of $T _ { n } ( x )$

Hint.The weights needed to establish (2.7) and (2.8) can be deduced from (1.144) with $0 \leqslant k \leqslant n - 1$ and ${ \pmb m } = { \pmb n }$

2.2.13.Show that Theorem 2.6 implies,in view of Exercise 2.2.12, that a best approximation on $I$ to $2 ^ { n - 1 } z ^ { n }$ by polynomials of degree at most $n - 1$ with complex coeffcients is $2 ^ { n - 1 } z ^ { n } - T _ { n } ( z )$

2.2.14. (Ehlich and Zeler [3]) Show that a best approximation on the square B: $- 1 \leqslant x \leqslant 1$ ， $- 1 \leqslant y \leqslant 1$ to $x ^ { n } y ^ { m }$ out of the space

$$
V { = } \left\{ p ( x , y ) = \sum _ { \stackrel { i = 0 } { i + j < n + m } } ^ { n } a _ { i j } x ^ { i } y ^ { j } \right\}
$$

is $x ^ { n } y ^ { m } - \tilde { T } _ { n } ( x ) \tilde { T } _ { m } ( y ) .$

Hint. $( \eta _ { k } ^ { ( n ) } , \eta _ { l } ^ { ( m ) } ) ^ { \perp }  ( - 1 ) ^ { k + l } , k = 0 , \dots , n , l = 0 , \dots , m ,$ is an extremal signature for $V .$

2.2.15. Let $V$ be the set of linear polynomials in two variables; i.e.,

$$
V = \{ a x + b y + c \} \ \mathrm { s h o w \ t h a t }
$$

(i) every primitive extremal signature for $V$ in $\textstyle \mathbb { R } ^ { 2 }$ is based on at least 3 points and at most 4 points;

(ii) if an extremal signature for Vis based on 3 points, they are collinear and the signs alternate;

(ii) if an extremal signature for $V$ is based on 4 points, then either

(a) they are the vertices of a triangle, all with one sign,and a point inside the triangle with the opposite sign, or

(b) they are the vertices of a convex quadrilateral with opposite vertices of like sign and adjacent vertices of opposite sign.

# 2.3. Chebyshev Systems and Uniqueness

Since our ultimate concern is with polynomial approximation, we now further restrict our $k$ -dimensional space of approximators $V$ by requiring that it satisfy the Chebyshev condition.

Definition 2.9. Vsatisfies the Chebyshev condition with respect to $\pmb { B }$ if, and only if, each $v \in V$ has at most $k - 1$ distinct zeros in $\pmb { B }$ ,unless ${ \pmb v } = { \bf 0 } .$ Any basis of $V$ is said to be a Chebyshev system on $\pmb { B }$

The simplest example of a Chebyshev system is $1 , z , \ldots , z ^ { k - 1 }$ ,on any set of the complex plane. A detailed study of the properties of Chebyshev systems is to be found in Karlin and Studden [1].

It is clear that $V$ satisfies the Chebyshev condition (with respect to $\pmb { B }$ if, and only if, for each set of $k$ distinct points of $B , y _ { 1 } , \ldots , y _ { k } $ we have

$$
\Delta = \left[ \begin{array} { c c c } { \varphi _ { 1 } ( y _ { 1 } ) } & { \ldots } & { \varphi _ { 1 } ( y _ { k } ) } \\ { \vdots } & { } & { } \\ { \varphi _ { k } ( y _ { 1 } ) } & { \ldots } & { \varphi _ { k } ( y _ { k } ) } \end{array} \right] \neq 0 .
$$

Thus,given arbitrary $b _ { 1 } , \ldots , b _ { k }$ ，there exists a unique $v \in V$ that satisfies $v ( y _ { i } ) = b _ { i } , i = 1 , . . . , k .$

Theorem 2.7. Every extremal signature for a $V$ which satisfies the Chebyshev condition is based on at least $k + 1$ points.

Proof. Suppose $\pmb { \Sigma }$ based on $y _ { 1 } , \ldots , y _ { r }$ is an extremal signature for $V$ and $r \leqslant k .$ Then there exists $v \in V$ such that $v ( y _ { 1 } ) = 1 , \ v ( y _ { i } ) = 0 , \ i = 2 , \ . . . , r .$ Hence, if $\zeta _ { 1 } , \ldots , \zeta _ { r }$ are weights associated with $\pmb { \Sigma }$ , we have $\zeta _ { 1 } v ( y _ { 1 } ) = 0$ which is impossible. Thus $r \geqslant k + 1$

In view of Exercise 2.2.6, then, every primitive extremal signature for a $V$ that satisfies the Chebyshev condition is based on precisely $k + 1$ points in the real case and $r$ points in the complex case, where $k + 1 \leqslant r \leqslant 2 k + 1$ The Chebyshev condition is intimately connected with the uniqueness of best approximations,as our next result shows.

Theorem 2.8 (Haar). Every $f \in C ( B )$ has a unique best approximation out of $V$ if, and only if, $V$ satisfies the Chebyshev condition with respect to $\pmb { B }$

Proof. (i) If $f \in V$ there is nothing to prove. Suppose that $f \notin V .$ Let $v _ { 1 }$ and ${ \mathfrak { v } } _ { 2 }$ be best approximations to $f$ out of $V .$ Let $\Sigma [ f - v _ { 1 } ] .$ based on $y _ { 1 } , \ldots , y _ { r }$ ,be an extremal signature for $V$ whose existence is affrmed by Theorem 2.6, with associated weights $\zeta _ { 1 } , \ldots , \zeta _ { r }$ satisfying

$$
\sum _ { i = 1 } ^ { r } | \zeta _ { i } | = 1 .
$$

Then

$$
\begin{array} { l } { \| f - v _ { 1 } \| = \displaystyle \sum _ { i = 1 } ^ { r } \zeta _ { i } [ f ( y _ { i } ) - v _ { 1 } ( y _ { i } ) ] = \displaystyle \sum _ { i = 1 } ^ { r } \zeta _ { i } [ f ( y _ { i } ) - v _ { 2 } ( y _ { i } ) ] } \\ { \leqslant \displaystyle \sum _ { i = 1 } ^ { r } | \zeta _ { i } | | f ( y _ { i } ) - v _ { 2 } ( y _ { i } ) | \leqslant \| f - v _ { 2 } \| , } \end{array}
$$

and, since $\left\| { f - v _ { 2 } } \right\| = \left\| { f - v _ { 1 } } \right\|$ ,the inequalities in (2.12) are both equalities, which is possible only if $| f ( y _ { i } ) - v _ { 2 } ( y _ { i } ) | = \| f - v _ { 2 } \|$ ， $i = 1$ 。...， $r$ and sgr $\begin{array} { r } { \mathfrak { \ i } \left[ f ( y _ { i } ) - v _ { 2 } ( y _ { i } ) \right] = \mathtt { s g n } \overline { { \zeta } } _ { i } , i = 1 , . . . , r . } \end{array}$ But then

$$
f ( y _ { i } ) - v _ { 2 } ( y _ { i } ) = f ( y _ { i } ) - v _ { 1 } ( y _ { i } ) , \qquad i = 1 , \ldots , r
$$

or $v _ { 2 } ( y _ { i } ) = v _ { 1 } ( y _ { i } ) = 0 , i = 1 , \ldots , r ,$ and $v _ { 2 } - v _ { 1 }$ has $r \geqslant k + 1$ zeros in $\pmb { B }$ . Since $V$ satisfies the Chebyshev condition $v _ { 2 } - v _ { 1 } = 0$ or $\pmb { v } _ { 2 } = \pmb { v } _ { 1 }$ . The best approximation is unique.

(ii) Suppose that $V$ does not satisfy the Chebyshev condition; i.e., there exists $v _ { 0 } \in V , v _ { 0 } \neq 0 .$ ，and distinct points $y _ { 1 } , \dotsc , y _ { k } \in B$ such that $v _ { 0 } ( y _ { i } ) = 0 ;$ $i = 1 , \ldots , k .$ Hence $\pmb { \Delta } = \pmb { 0 }$ [cf. (2.11)] and

$$
\sum _ { j = 1 } ^ { k } a _ { j } \varphi _ { i } ( y _ { j } ) = 0 , \qquad i = 1 , \ldots , k ,
$$

has a nontrivial solution. Suppose that, after renumbering if necessary, $a _ { j } \neq 0$ ， $j = 1 , \ldots , r ,$ where $1 \leqslant r \leqslant k ;$ then

$$
\sum _ { j = 1 } ^ { r } a _ { j } v ( y _ { j } ) = 0 , \qquad \mathrm { a l l } \ v \in V .
$$

Suppose that $g \in C ( B ) , \ \| g \| = 1$ and $g ( y _ { j } ) = \mathfrak { s g n } \bar { a } _ { j } ,$ ， $j = 1$ ，...,r. Consider $f ( y ) = g ( y ) ( 1 - \lvert \lambda v _ { 0 } ( y ) \rvert ) + v _ { 1 } ( y ) ,$ where $v _ { 1 }$ is any element of $V$ and $\| \lambda v _ { 0 } \| < 1$ Then $f \in C ( B ) ;$ ， $\| f - v _ { 1 } \| \leqslant 1$ ，and indeed $\| f - v _ { 1 } \| = 1$ and $[ f ( y _ { j } ) -$ $v _ { 1 } ( y _ { j } ) ] = { \mathrm { s g n } } \bar { a } _ { j } , j = 1 , \ldots , r .$ Put $\Sigma ( y _ { j } ) = \mathrm { s g n } \bar { a } _ { j } , j = 1 , . . . , r .$ Then, in view of (2.13), $\pmb { \Sigma }$ is an extremal signature for $V ,$ hence by Theorem $2 . 6 \ v _ { 1 }$ is a best approximation to $f .$ Put $v _ { 2 } = v _ { 1 } - \lambda v _ { 0 }$ Then $\pmb { v _ { 2 } } \in V$ and $f - v _ { 2 } = g ( 1 -$ $| \lambda v _ { 0 } | ) + \lambda v _ { 0 } ;$ hence $| f ( y ) - v _ { 2 } ( y ) | \leqslant 1$ and $\| f - v _ { 2 } \| = 1$ .Thus ${ \mathfrak { v } } _ { 2 }$ is another best approximation to $f .$ Uniqueness fails.

Remark. Note that although the $f$ we constructed is continuous, it is not differentiable. -

Newman and Shapiro [1] introduced a quantitative strengthening of uniqueness which has become known as strong uniqueness. $\mathbf { I f } f \in C ( B )$ and $V$ is a $k \mathrm { . }$ -dimensional subspace of $C ( B )$ then $v ^ { * } \in V$ is called a strongly unique best approximation out of $V$ to $f$ on $\pmb { B }$ if, for all $v \in V$

$$
\lVert f - v \rVert \geqslant \lVert f - v ^ { * } \rVert + \gamma \lVert v - v ^ { * } \rVert
$$

for some $\gamma ( f , B , V ) > 0 . \gamma$ is then called a strong uniqueness constant. We denote the supremum of all positive $\gamma$ for which (2.13.1) holds by $\gamma ^ { * }$ , and call it the best strong uniqueness constant.

Let $v ^ { * }$ be a best approximation out of $V$ to $f ( \notin V )$ on $\pmb { B } .$ . Suppose that $\pmb { s }$ is a closed subset of $E ( f - v ^ { * } ; B )$ Put

$$
\varepsilon ( y ) = \operatorname { s g n } { \bigl ( } f ( y ) - v ^ { * } ( y ) { \bigr ) } , \qquad y \in S .
$$

Suppose that

$$
\operatorname* { m i n } _ { \| v \| = 1 } \operatorname* { m a x } _ { y \in S } \operatorname { R e } \overline { { ( \varepsilon ( y ) } } v ( y ) ) = \gamma _ { s } > 0 .
$$

f $v \not = v ^ { * }$ then $w = ( v ^ { * } - v ) / \| v - v ^ { * } \| \in V$ satisfies $\| \boldsymbol { w } \| = 1$ . Hence in view of (2.13.2) there exists $y _ { 0 } \in \mathbf { S }$ such that $\begin{array} { r } { \operatorname { R e } \left( \overline { { \varepsilon ( \ y _ { 0 } ) } } w ( y _ { 0 } ) \right) \geqslant \gamma _ { s } > 0 . } \end{array}$ But

$$
\begin{array} { r l } & { \| f - v \| \geqslant | \overline { { \varepsilon ( y _ { 0 } ) } } ( f ( y _ { 0 } ) - v ( y _ { 0 } ) ) | \geqslant \mathrm { R e } \widehat { \varepsilon ( y _ { 0 } ) } ( f ( y _ { 0 } ) - v ( y _ { 0 } ) ) } \\ & { \qquad \geqslant \mathrm { R e } \overline { { \varepsilon ( y _ { 0 } ) } } ( f ( y _ { 0 } ) - v ^ { * } ( y _ { 0 } ) ) + \mathrm { R e } \overline { { \varepsilon ( y _ { 0 } ) } } ( v ^ { * } ( y _ { 0 } ) - v ( y _ { 0 } ) ) , } \end{array}
$$

or,recalling the definitions of $\varepsilon ( y _ { 0 } )$ and w we have (what is trivially true if $v = v ^ { * }$ ）

$$
\lVert f - v \rVert \geqslant \lVert f - v ^ { * } \rVert + \gamma _ { s } \lVert v - v ^ { * } \rVert .
$$

Thus we have shown that (2.13.2) implies (2.13.1) with $\gamma = \gamma _ { s }$

There are two interesting choices for S. Suppose first that $S _ { 0 } = \{ y _ { 1 } , . . . , y _ { r } \}$ is the base of an extremal signature $\Sigma [ f - v ^ { * } ]$ (Definitions 2.6-2.8), and strong uniqueness fails to hold. Then (2.13.2) must not be valid and so there exists $v _ { 0 } \in V$ satisfying $\| v _ { 0 } \| = 1$ and $\begin{array} { r } { \mathbf { R e } \overline { { ( \varepsilon ( y _ { j } ) } } v _ { 0 } ( y _ { j } ) ) \leqslant 0 , j = 1 , } \end{array}$ $\cdots , r .$ But we know,(2.8), that there exist positive numbers, $\lambda _ { 1 } , \ldots , \lambda _ { r }$ such that

$$
\sum _ { j = 1 } ^ { r } \lambda _ { j } \operatorname { R e } \overline { { ( \varepsilon ( y _ { j } ) } } v _ { 0 } ( y _ { j } ) ) = 0 ,
$$

which yields

$$
\begin{array} { r } { \mathbf { R e } \overline { { ( \varepsilon ( y _ { j } ) } } v _ { 0 } ( y _ { j } ) ) = 0 , j = 1 , \ldots , r . } \end{array}
$$

Thus, in the real case, $v _ { 0 } ( y _ { j } ) = 0 , j = 1 , \ldots , r .$ But if $V$ satisfies the Chebyshev condition, then according to Theorem 2.7 we must have $r \geqslant k + 1$ and hence $v _ { 0 } = 0 ;$ ,contradicting our assumption that $\| v _ { 0 } \| = 1$ .We conclude then that in a real best approximation problem, in which $V$ satisfies the Chebyshev condition, strong uniqueness holds (cf. Theorem 2.8).

If $S ^ { * } = E ( f - v ^ { * } B )$ it is obvious that $\gamma _ { s } \leqslant \gamma _ { s ^ { * } }$ for all S. We show next that (2.13.1) implies

$$
\begin{array} { r l } & { \operatorname* { m i n } \quad \operatorname* { m a x } \mathrm { R e } \overline { { ( \varepsilon ( y ) } } v ( y ) ) \geqslant \gamma > 0 . } \\ & { \| v \| = 1 \quad y \in S ^ { * } } \end{array}
$$

If(2.13.3) were false then there would exist $w \in V , \| w \| = 1$ and $\pmb { \tau } > \mathbf { 0 }$ such that $\begin{array} { r } { \mathrm { R e } \overline { { ( \varepsilon ( y ) } } w ( y ) ) < \tau < \gamma , } \end{array}$ for $y \in S ^ { * }$ . Let $\| f - \nu ^ { * } \| = M$ and

$$
U = \{ y \in B ; \operatorname { R e } { \overline { { ( \varepsilon ( y ) } } } w ( y ) ) < \tau { \mathrm { ~ a n d ~ } } | f ( y ) - v ^ { * } ( y ) | > M / 2 \} .
$$

Then $s ^ { * } \subset U$ ,and if $y$ is in the closed set ${ \pmb { B } } \backslash { \pmb { U } }$ we have $| f ( y ) - v ^ { * } ( y ) |$ $\leqslant M - \delta$ (for some $\delta > 0$ ), and for any $\lambda$ satisfying $0 < \lambda \leqslant \delta / 2$

$$
\operatorname* { m a x } _ { y \in B \setminus U } | f ( y ) - v ^ { * } ( y ) + \lambda w | \leqslant M - \frac { \delta } { 2 } .
$$

$\| f - v ^ { * } + \lambda w \| _ { B } = | f ( y _ { 0 } ) - v ^ { * } ( y _ { 0 } ) + \lambda w ( y _ { 0 } ) |$ then $y _ { 0 } \in U$ and a simple calculation yields

$$
\begin{array} { c } { { \| f - v ^ { * } + \lambda w \| ^ { 2 } \leqslant M ^ { 2 } + 2 \lambda M \tau + \lambda } } \\ { { \leqslant \| f - v ^ { * } + \lambda w \| ^ { 2 } - 2 \lambda ( \gamma - \tau ) \| f - v ^ { * } + \lambda w \| } } \\ { { \qquad + \lambda ^ { 2 } ( \gamma ^ { 2 } - 2 \gamma \tau + \lambda ) \tau } } \end{array}
$$

(the second inequality being a consequence of (2.13.1) with $v = v ^ { * } - \lambda w )$ ， which is impossible under our assumption that $\tau < \gamma$ for $\lambda$ sufficiently small.

We have now established the equivalence of (2.13.3) and (2.13.1). This allows us to conclude that the best strong uniqueness constant is given by

$$
0 < \gamma ^ { * } = \operatorname* { m i n } _ { \| v \| = 1 } \ \operatorname* { m a x } _ { y \in E ( f - v ^ { * } ; B ) } \operatorname { R e } \overline { { ( \varepsilon ( y ) } } v ( y ) ) .
$$

The best strong uniqueness constant is not known explicitly for many concrete examples.Fortunately for us, it is known for the best approximation of $T _ { n } ( x )$ out of $\mathcal { P } _ { n - 1 }$ on $\pmb { I }$ , and our next task is to evaluate $\gamma ^ { \ast } ( T _ { n } , I , \mathcal { P } _ { n - 1 } )$ by solving the extremal problem in (2.13.4) in this case.

We begin with the observation that in the problem under consideration $v ^ { * } = 0 ,$ $= 0 , E ( T _ { n } ; I ) = \left\{ \eta _ { 0 } ^ { ( n ) } , \dots , \eta _ { n } ^ { ( n ) } \right\}$ and $\varepsilon ( \eta _ { j } ^ { ( n ) } ) = ( - 1 ) ^ { j }$ ， $j = 0 ;$ 。...,n. Suppose,

$\pmb { p } \in \mathcal { P } _ { \pmb { n } - 1 }$ . We claim that

$$
\operatorname* { m i n } _ { \| p \| = 1 } \operatorname* { m a x } _ { j = 0 , \ldots , n } ( - 1 ) ^ { j } p ( \eta _ { j } ) \geqslant \frac { 1 } { 2 n - 1 } .
$$

For suppose otherwise, then there exists $p \in { \mathcal { P } } _ { n - 1 } , \| p \| = 1 _ {  }$ and

$$
{ \frac { 1 } { 2 n - 1 } } - ( - 1 ) ^ { j } p ( \eta _ { j } ) > 0 , \qquad j = 0 , \ldots , n .
$$

Suppose $p ( x ) = A _ { 0 } + A _ { 1 } T _ { 1 } ( x ) + \cdots + A _ { n - 1 } T _ { n - 1 } ( x ) ,$ then

$$
T _ { n } ( x ) p ( x ) = \sum _ { j = 1 } ^ { 2 n - 1 } B _ { j } T _ { j } ( x )
$$

where

$$
B _ { j } = B _ { 2 n - j } = { \frac { A _ { n - j } } { 2 } } , \qquad j = 1 , \ldots , n - 1 , \qquad B _ { n } = A _ { 0 } .
$$

Consider the Chebyshev expansion of $q ( x ) = ( 2 n - 1 ) ^ { - 1 } - T _ { n } ( x ) p ( x ) .$ The finite orthogonality formula, (1.144), yields

$$
\sum _ { j = 0 } ^ { n } T _ { k } ( \eta _ { j } ) q ( \eta _ { j } ) = \left\{ \begin{array} { l l } { { - n A _ { 0 } , } } & { { \quad k = n , } } \\ { { - \frac { n } { 2 } A _ { n - k } , } } & { { \quad k = 1 , \ldots , n - 1 , } } \end{array} \right.
$$

and since $q ( \eta _ { j } ) > 0 , j = 0 , \ldots , n ,$ we obtain

$$
\frac { n } { 2 } \left| A _ { n - k } \right| \leqslant \sum _ { j = 0 } ^ { n } \prime \prime \ q ( \eta _ { j } ) = \frac { n } { 2 n - 1 } ,
$$

or

$$
| A _ { n - k } | \leqslant { \frac { 2 } { 2 n - 1 } } , \qquad k = 1 , \ldots , n - 1 .
$$

Also, since $T _ { n } ( \eta _ { j } ) = ( - 1 ) ^ { j }$ ，

$$
n | A _ { 0 } | < \sum _ { j = 0 } ^ { n } { } ^ { \prime \prime } q ( \eta _ { j } ) = { \frac { n } { 2 n - 1 } } ,
$$

or

$$
\left| { \cal A } _ { 0 } \right| < \frac { 1 } { 2 n - 1 } .
$$

Thus

$$
\| p \| \leqslant \sum _ { j = 0 } ^ { n - 1 } | A _ { j } | < 1 ,
$$

contrary to our assumption that $\| \pmb { p } \| = 1$ Equation (2.13.5) must hold. Itis easy to see (Exercise 1.2.15d) that if $s ( x ) = - ( 1 / 2 + T _ { 1 } ( x ) + \cdots + T _ { n - 1 } ( x ) )$ then

$$
s ( \eta _ { j } ) = \left\{ \begin{array} { l l } { { - \bigg ( n - \frac 1 2 \bigg ) , } } & { { j = 0 , } } \\ { { } } & { { } } \\ { { \displaystyle \frac { ( - 1 ) ^ { j } } 2 , } } & { { . } } \end{array} \right.
$$

so that

$$
p ( x ) = \frac { 2 s ( x ) } { 2 n - 1 }
$$

satisfies $\| { \pmb p } \| = 1$ and $( - 1 ) ^ { j } p ( \eta _ { j } ) \leqslant ( 2 n - 1 ) ^ { - 1 }$ ， $j = 0 ;$ ，..., n. We have thus proved, in view of (2.13.5), that

$$
\gamma ^ { * } ( T _ { n } , I , \mathcal { P } _ { n - 1 } ) = \frac { 1 } { 2 n - 1 }
$$

(see also Cline [1]).

# EXERCISES 2.3.1-2.3.4

# 2.3.1. Show that

$$
\gamma ^ { * } = \operatorname* { i n f } _ { v \neq v ^ { * } } { \frac { \| f - v \| - \| f - v ^ { * } \| } { \| v - v ^ { * } \| } } .
$$

This suggests that the best strong uniqueness constant is worth examining in the error analysis of computations of approximations to best approximations.

2.3.2. Suppose that $V$ satisfies the Chebyshev condition. Let $\mathscr { P }$ be the operator which transforms $f ( \in C ( B ) )$ into ${ \pmb v } ^ { * }$ ,the (unique) best approximation to $f$ out of $V .$ That is, $\mathcal { P } f = v ^ { \ast }$ .Show that for a given $f \in C ( B ) ;$ ,there exists $c > 0$ such that

$$
\| { \mathcal { P } } f - { \mathcal { P } } g \| \leqslant C \| f - g \| , \qquad g \in C ( B ) .
$$

Hint. Recall that ${ \pmb v } ^ { * }$ is strongly unique and put $\ v = \mathcal { P } g$ in (2.13.1) to obtain

$$
\gamma \| \mathcal { P } f - \mathcal { P } g \| \leqslant \| f - \mathcal { P } g \| - \| f - \mathcal { P } f \| .
$$

Judicious consecutive application of the triangle inequality to $\| f - \pmb { \mathscr { P } } \pmb { \mathscr { g } } \|$ in (2.13.8) leads to $\gamma \| \mathcal { P } f - \mathcal { P } g \| \leqslant 2 \| f - g \|$ ,and the required result follows.

Thus under the conditions of this exercise the best approximation operator (which is nonlinear) is continuous,and, indeed,satisfies a Lipschitz condition at each $f .$ This result is due to Freud [1].

2.3.3. Show that the constant $\gamma$ in (2.13.1) must satisfy $\gamma \leqslant 1$

2.3.4. Show that if $\pmb { p } \in \mathcal { P } _ { { \pmb { n } } - 1 }$

$$
\Vert T _ { n } - p \Vert _ { I } \geqslant 1 + \frac { \Vert p \Vert _ { I } } { 2 n - 1 } .
$$

# 2.4. Approximation on an Interval

We now further restrict our attention to the real case in which $V$ satisfies the Chebyshev condition. In view of Theorem 2.7 and Exercises 2.2.7 and 2.2.9, we see that any distinct points $y _ { 1 } , \dotsc , y _ { k + 1 }$ of $\pmb { B }$ are the base of a unique extremal signature up to multiplication by $^ { - 1 }$ .Moreover, if $B = [ a , b ] .$ an interval of the real axis, the primitive extremal signatures are further restricted.

Theorem 2.9. Suppose that $a \leqslant x _ { 1 } < x _ { 2 } < \cdots < x _ { k + 1 } \leqslant b ;$ $V$ satisfies the Chebyshev condition with respect to $[ a , b ]$ and consists of real-valued functions. Then the values $\Sigma ( x _ { i } ) , i = 1 , \ldots , k + 1 ,$ ,of the“unique” extremal signature based on $x _ { 1 } , \ldots , x _ { k + 1 }$ alternate in sign.

Proof. It is enough to show that any weights $\zeta _ { 1 } , \ldots , \zeta _ { k + 1 }$ associated with $\pmb { \Sigma }$ alternate in sign.

First we dispose of the case $k = 1$ .If $k = 1$ ， $v \neq 0$ has no zero in $[ x _ { 1 } , x _ { 2 } ]$ and $\zeta _ { 1 } v ( x _ { 1 } ) + \zeta _ { 2 } v ( x _ { 2 } ) = 0$ then implies that $\zeta _ { 1 } \zeta _ { 2 } < 0 .$ .Suppose that $k > 1$ and there exists $j ,$ $1 \leqslant j < k + 1 ,$ such that $\zeta _ { j } \zeta _ { j + 1 } > 0$ and, say, $\zeta _ { j } , \zeta _ { j + 1 } > 0$ Then there exists $\pmb q$ $, 1 < q < k + 1 ;$ ,such that either $\zeta _ { q - 1 }$ or $\zeta _ { q + 1 }$ is of the same sign as $\zeta _ { q }$ ,namely positive. $( \mathbb { I } { \boldsymbol { \mathrm { f } } } j > 1$ ,take $q = j , \operatorname { I f } j = 1$ ,take $\pmb q = 2 .$ ) Now choose two positive numbers, $\pmb { \alpha _ { q - 1 } }$ and $\alpha _ { q + 1 }$ ，such that $\alpha _ { q - 1 } \zeta _ { q - 1 } + \alpha _ { q + 1 } \zeta _ { q + 1 } > 0 ,$ and let ${ \pmb v _ { 0 } }$ be the unique element of $V$ that satisfies

$$
\begin{array} { c } { { v _ { 0 } ( x _ { q - 1 } ) = \alpha _ { q - 1 } , \qquad v _ { 0 } ( x _ { q + 1 } ) = \alpha _ { q + 1 } , } } \\ { { \qquad v _ { 0 } ( x _ { i } ) = 0 , \qquad i = 1 , \ldots , k + 1 , \qquad i \neq q - 1 , q , q + 1 . } } \end{array}
$$

Then by the definition of weights we have

$$
\begin{array} { r } { \alpha _ { q - 1 } \zeta _ { q - 1 } + \zeta _ { q } v _ { 0 } ( x _ { q } ) + \alpha _ { q + 1 } \zeta _ { q + 1 } = 0 . } \end{array}
$$

Thus $v _ { 0 } ( x _ { q } ) < 0 ;$ while $v _ { 0 } ( x _ { q \pm 1 } ) > 0 ;$ hence ${ \pmb v _ { 0 } }$ has two zeros in $( x _ { q - 1 } , x _ { q + 1 } )$ for a total of at least $\pmb { k }$ zeros in $[ x _ { 1 } , x _ { k + 1 } ]$ .This contradicts the assumption that $V$ satisfies the Chebyshev condition with respect to $[ a , b ]$

We next obtain, quite easily, the classical characterization theorem of best approximation on a closed subset of a real interval in the presence of the Chebyshev condition.

Theorem 2.10. Let $\pmb { B }$ denote the interval $[ a , b ]$ and suppose that $V$ satisfies the Chebyshev condition with respect to $\pmb { B }$ Let S be any closed subset of $\pmb { B }$ (e.g., $B _ { i }$ ,finitely many points of $\pmb { B }$ ). Then ${ \pmb v _ { 0 } }$ is the best approximation on S to $f \in C ( S ) \left( f \notin V \right)$ if,and only if, there exist $x _ { i } \in E ( f - v _ { 0 } ; S ) .$ $i = 1 ,$ ….， $k + 1$ ， such that $x _ { 1 } < x _ { 2 } < \cdots < x _ { k + 1 }$ ,and

$$
f ( x _ { i } ) - v _ { 0 } ( x _ { i } ) , \qquad i = 1 , \ldots , k + 1 ,
$$

alternate in sign.

Proof. Theorem 2.10 follows immediately from Theorems 2.6 and 2.9.

Remark. Under the assumptions of Theorem 2.10 and in view of Corollary 2.6.1, the best approximation ${ \pmb v _ { 0 } }$ to $f$ on S is also the best approximation to $f$ on some set of $k + 1$ points of S. Moreover, if Y: $\left\{ y _ { 1 } , \ldots , y _ { k + 1 } \right\}$ consists of distinct points of $\pmb { s }$ and ${ \pmb v } _ { { \pmb r } }$ is the best approximation to $f$ on $\pmb { Y } ,$ then $\| f - v _ { Y } \| _ { Y } \leqslant \| f - v _ { 0 } \|$ ； that is to say,if we find the best approximation to $f$ on a subset of $k + 1$ points of S which has the largest error (in norm) among all subsets of $k + 1$ points of S, that approximation is also best on all of S. This observation is the foundation of some frequently used algorithms for finding best approximations numerically.In the case that S is a finite set of points our search is reduced to examining the best approximations on the finite number of subsets of $k + 1$ points of S. This problem turns out to be tractable,as we shall see next.

Let $\pmb { X }$ denote the distinct points $x _ { 1 } , \ldots , x _ { k + 1 }$ of $[ a , b ]$ ，numbered (for future convenience) this time as follows: $a \leqslant x _ { k + 1 } < x _ { k } < \cdots < x _ { 1 } \leqslant b .$ Suppose that $V$ satisfies the Chebyshev condition with respect to $[ a , b ]$ Consider the matrix

$$
\Phi = \left( \begin{array} { l l l } { \varphi _ { 1 } ( x _ { 1 } ) } & { \ldots } & { \varphi _ { k } ( x _ { 1 } ) } \\ { \vdots } \\ { \varphi _ { 1 } ( x _ { k + 1 } ) } & { \ldots } & { \varphi _ { k } ( x _ { k + 1 } ) } \end{array} \right)
$$

and the determinant $\Delta _ { i } ( i = 1 , . . . , k + 1 )$ of the square matrix obtained by deleting the ith row of $\Phi$ .No $\Delta _ { i }$ is zero because of the Chebyshev condition

and, indeed, they all have the same sign,for the determinant

$$
\delta _ { i } ( t ) = \left[ \begin{array} { l l l } { \varphi _ { 1 } ( x _ { 1 } ) } & { \cdots } & { \varphi _ { k } ( x _ { 1 } ) } \\ { \vdots } \\ { \varphi _ { 1 } ( x _ { i - 1 } ) } & { \cdots } & { \varphi _ { k } ( x _ { i - 1 } ) } \\ { \varphi _ { 1 } ( t ) } & { \cdots } & { \varphi _ { k } ( t ) } \end{array} \right] .
$$

is a continuous function of $\pmb { t }$ which is not zero for $x _ { i + 2 } < t < x _ { i - 1 }$ ；hence $\Delta _ { i } = \delta _ { i } ( x _ { i + 1 } )$ and $\Delta _ { i + 1 } = \delta _ { i } ( x _ { i } )$ must have the same sign,and this holds for $i = 1 , \ldots , k + 1$ (with trivial modification of the argument for $i = 1 , k + 1 )$ .If we adjoin an arbitrary $( k + 1 ) { \mathsf { s t } }$ column to $\Phi$ ,the cofactors of the elements of this column are $( - 1 ) ^ { k + 1 } \Delta _ { i }$ ， $i = 1 , . . . , k + 1 .$ Moreover, these cofactors are orthogonal to each of the columns of $\Phi$ [because the dot product involved is merely the value of the determinant, with the particular column repeated as the $( k + 1 ) \mathsf { s t }$ column, obtained by expanding by elements of the $( k + 1 ) { \mathsf { s t } }$ column]; i.e.,

$$
\sum _ { i = 1 } ^ { k + 1 } ( - 1 ) ^ { i } \Delta _ { i } \varphi _ { j } ( x _ { i } ) = 0 , \qquad j = 1 , \ldots , k .
$$

Equations (2.14) imply that

$$
\Theta _ { i } = \frac { ( - 1 ) ^ { i } \Delta _ { i } } { \Sigma _ { j = 1 } ^ { k + 1 } | \Delta _ { j } | } , \qquad i = 1 , . . . , k + 1 ,
$$

are weights associated with the extremal signature $\Sigma ( x _ { i } ) = ( - 1 ) ^ { i }$ ，which satisfy

$$
\sum _ { i = 1 } ^ { k + 1 } | \Theta _ { i } | = 1 .
$$

If $v ^ { * }$ is the unique best approximation to $f \notin V$ on $\pmb { X }$ ,then in view of Theorem 2.10

$$
\| f - v ^ { * } \| _ { X } = \lambda \sum _ { i = 1 } ^ { k + 1 } \Theta _ { i } [ f ( x _ { i } ) - v ^ { * } ( x _ { i } ) ] = \lambda \sum _ { i = 1 } ^ { k + 1 } \Theta _ { i } f ( x _ { i } ) ,
$$

where

$$
\lambda = { \tt s g n } \sum _ { i = 1 } ^ { k + 1 } \Theta _ { i } f ( x _ { i } ) .
$$

Thus we have proved the following.

Theorem 2.11. For any $f$ defined on $\pmb { X }$ we have

$$
\rho ( f ; X ) = \rho = \| f - v ^ { * } \| _ { X } = \left| \sum _ { i = 1 } ^ { k + 1 } \Theta _ { i } f ( x _ { i } ) \right|
$$

and $v ^ { * }$ is determined by any $k$ of the equations

$$
v ^ { * } ( x _ { i } ) = f ( x _ { i } ) - \lambda \ \mathrm { s g n } \ \Delta _ { i } ( - 1 ) ^ { i } \rho , \ i = 1 , \ldots , k + 1 .
$$

We now further specialize by taking $V$ to be $\mathcal { P } _ { k - 1 }$ ,real polynomials of degree at most $k - 1$ ，and $\pmb { B }$ to be the interval $I \colon [ - 1 , 1 ]$ . (There is no loss in generality in restricting our attention to $I _ { : }$ ，since results obtained are easily translated to any finite interval by means of a linear change of variables that leaves $\mathcal { P } _ { k - 1 }$ invariant.) It is not easy to find explicitly the polynomial of best approximation to a given continuous $f ( x ) .$ .Of particular interest to us is the case $f ( x ) = x ^ { k } ;$ ， $( k \geqslant 1 )$

Let $p ( x ) \in \mathcal { P } _ { k - 1 }$ be the best approximation to $x ^ { k }$ on $\pmb { I }$ out of $\mathcal { P } _ { k - 1 }$ . Then $r ( x ) = x ^ { k } - p ( x ) \in \mathcal { P } _ { k }$ ,and $r ( x )$ attains its maximum absolute value, $M > 0$ at $k + 1$ points satisfying $- 1 \leqslant x _ { k + 1 } < x _ { k } < \cdots < x _ { 1 } \leqslant 1 ,$ ， with alternating signs (though the latter fact is superfluous in determining $\pmb { p }$ ,according to Theorem 2.10.We claim that $\mathbf { \boldsymbol { x } _ { 1 } } = 1$ and $x _ { k + 1 } = - 1$ , for otherwise $r ( x )$ has a relative extremum at $\pmb { k }$ interior points of $\pmb { I }$ ，which means that $\pmb { r } ^ { \prime }$ has $\pmb { k }$ zeros, hence is identically zero,an impossibility [since the leading coefficient of $r ( x )$ is 1]. Consider $M ^ { 2 } - r ^ { 2 } ( x ) \in \mathcal { P } _ { 2 k }$ $M ^ { 2 } - r ^ { 2 } ( x ) \geqslant 0$ in $\pmb { I }$ ,hence has $x _ { 2 } , \ldots , x _ { k }$ as zeros of order, at least 2, and $\pm 1$ as simple zeros, thus accounting for all its zeros; but $( 1 - x ^ { 2 } ) [ r ^ { \prime } ( x ) ] ^ { 2 } \in \mathcal { P } _ { 2 k }$ has precisely the same zeros,hence is a constant multiple of $M ^ { 2 } - r ^ { 2 } ( x ) .$ ， The constant is determined by equating leading coefficients and we obtain the (Chebyshev) differential equation

$$
( 1 - x ^ { 2 } ) ( r ^ { \prime } ( x ) ) ^ { 2 } = k ^ { 2 } ( M ^ { 2 } - r ^ { 2 } ( x ) ) .
$$

We know that $r ( - 1 ) = \pm M$ . Suppose that $r ( - 1 ) = - M .$ . Then we know that $r ^ { \prime } ( x ) > 0$ in $[ - 1 , x _ { k } )$ and the differential equation becomes

$$
\frac { r ^ { \prime } ( x ) } { \sqrt { M ^ { 2 } - r ^ { 2 } ( x ) } } = \frac { k } { \sqrt { 1 - x ^ { 2 } } } ,
$$

which has the solution arccos $( r / M ) = k$ arc cos $\mathbf { \sigma } _ { 3 } x + c = k \theta + c .$ ，where $0 \leqslant \theta \leqslant \pi ,$ and cos $\pmb \theta = \pmb x .$ Thus

$$
r ( x ) = M \cos { ( k \theta + c ) } .
$$

Now $r ( - 1 ) = - M$ implies that $c = [ ( 2 j - 1 ) - k ] \pi$ for some integer $j ,$ hence

$$
r ( x ) = ( - 1 ) ^ { k + 1 } M \cos k \theta , \qquad 0 \leqslant \theta < \theta _ { k } = \operatorname { a r c c o s } x _ { k } , x = \cos \theta ;
$$

that is, $r ( x ) = ( - 1 ) ^ { k + 1 } M T _ { k } ( x )$ in $[ - 1 , x _ { k } )$ .This is possible only if $\pmb { k }$ is odd and $M = 2 ^ { 1 - k }$ ， since the leading coefficient of $\boldsymbol { r }$ is 1.Also it must be that $x _ { k } = \eta _ { k - 1 } ^ { ( k ) }$ ,and it is clear that the solution

$$
r ( x ) = \widetilde { T } _ { k } ( x )
$$

can be continued in similar fashion to the whole interval $I .$ An analogous examination of the case $r ( - 1 ) = M$ leads to the conclusion that $\pmb { k }$ is even and that (2.1) remains valid. Thus the unique best approximation to $x ^ { k }$ out of $\mathcal { P } _ { k - 1 }$ on $I$ is $x ^ { k } - \widetilde { T } _ { k } ( x )$

Note that we have arrived at another proof of Theorem 2.1. It has been a long voyage with some interest of its own, bringing us back to our starting point, but we observe that our second approach creates the Chebyshev polynomials out of the void while they are pulled out of a hat in Theorem 2.1.

In the course of the discussion just concluded we have established the following important characterization of the Chebyshev polynomials.

Theorem 2.12. If $\pmb { p } \in \mathcal { P } _ { \pmb { n } }$ and $| p |$ assumes its maximum in $[ - 1 , 1 ] , \ \| p \|$ at $n + 1$ distinct points,then either $\pmb { p }$ is a constant $( \pm \| p \| )$ or $p = \pm \| p \| T _ { n }$ ,and the points are $\eta _ { j } ^ { ( n ) } , j = 0 , . . . , n .$

Remark. If the interval [-1,1] is replaced by $[ a , b ]$ ,then $T _ { n } ( x )$ must be replaced by

$$
T _ { n } \left( { \frac { 2 x - ( a + b ) } { b - a } } \right)
$$

in Theorem 2.12.In particular,when $a = 0 , b = 1$ ，we have the Chebyshev polynomial for the interval [0,1], $T _ { n } ( 2 x - 1 ) ,$ which arises frequently enough in applications to warrant the special notation $T _ { n } ^ { * } ( x )$ .Observe that in view of Exercise 1.1.6, $T _ { n } ^ { * } ( x ^ { 2 } ) = T _ { 2 n } ( x ) .$

# EXERCISES 2.4.1-2.4.50

2.4.1. If $f ( x )$ is an even (odd) function on $[ - a , a ]$ ,it has a best approximation out of $\mathcal { P } _ { \pmb { n } }$ that is also even (odd).

Hint. If $p ( { \boldsymbol { x } } )$ and $\pmb { p } ( - \pmb { x } )$ are both best approximations, so is $[ p ( x ) + p ( - x ) ] / 2$

2.4.2. What is the best approximation to $x ^ { n + 2 }$ on [-1,1] out of $\mathcal { P } _ { n } \mathrm { ? }$

2.4.3. If $v ^ { * }$ is a best approximation tofout of $V ,$ then $v ^ { * } - v$ is a best approximation to $f - v$ out of $V .$ Hence $E _ { V } ( f ) = E _ { V } ( f - v ) ,$ all $v \in V .$

2.4.4. If $f ^ { \prime \prime } ( x ) > 0$ on $[ a , b ]$ ,the best approximation to $f$ out of $\mathcal { P } _ { 1 }$ is

$$
{ \frac { f ( a ) ( b - c ) + f ( b ) ( c - a ) + f ( c ) ( b - a ) } { 2 ( b - a ) } } + { \frac { f ( b ) - f ( a ) } { b - a } } ( x - c )
$$

and

$$
E _ { 1 } ( f ) = \frac { f ( a ) ( b - c ) + f ( b ) ( c - a ) - f ( c ) ( b - a ) } { 2 ( b - a ) } ,
$$

where $^ { c }$ is the unique solution in $[ a , b ]$ of

$$
f ^ { \prime } ( c ) = { \frac { f ( b ) - f ( a ) } { b - a } } .
$$

2.4.5. (Turan [1]) If

$$
p ( { \boldsymbol { x } } ) = { \boldsymbol { x } } ^ { n } + a _ { n - 1 } { \boldsymbol { x } } ^ { n - 1 } + \cdots + a _ { 0 } = ( { \boldsymbol { x } } - { \boldsymbol { z } } _ { 1 } ) \cdots ( { \boldsymbol { x } } - { \boldsymbol { z } } _ { n } ) ,
$$

then

$$
\| p \| \geqslant 2 ^ { - n + 1 } \prod _ { | z _ { j } | > 1 } | z _ { j } | ,
$$

where an empty product is taken equal to 1.

Hint. Apply Corollary 2.1.1 to

$$
p ( x ) \prod _ { | z _ { j } | > 1 } ( x - z _ { j } ) ^ { - 1 } ( 1 - \bar { z } _ { j } x ) .
$$

2.4.6. According to (2.18), the differential equation

$$
( 1 - x ^ { 2 } ) ( y ^ { \prime } ) ^ { 2 } = n ^ { 2 } ( 1 - y ^ { 2 } )
$$

has $y = \pm T _ { n } ( x )$ as solutions. Show that (2.20) has no other polynomial solution for $\pmb { n } > \mathbf { 0 }$

Hint. If polynomial $\pmb { p }$ satisfies (2.20), it satisfies $( 1 - x ^ { 2 } ) p ^ { \prime \prime } - x p ^ { \prime } + n ^ { 2 } p = 0$ and $p ( 1 ) = \pm 1$ Now recall Exercise 1.5.4.

Problems 2.4.7-2.4.17 are set in the complex plane.

2.4.7. For any ${ \pmb \rho } > { \bf 0 }$

$$
\sum \left[ \rho e ^ { 2 \pi i j / ( k + 1 ) } \right] = e ^ { - 2 \pi i j / ( k + 1 ) } , \qquad j = 0 , 1 , \ldots , k
$$

is a primitive extremal signature for $\mathcal { P } _ { \pmb { k } - 1 }$ (complex-valued polynomials).

Hint. Associated weights are $e ^ { 2 \pi i j / ( k + \textbf { 1 } ) }$

2.4.8. Let $c _ { \rho }$ be the ellipse defined in the $z$ -plane by

$$
z = \textstyle { \frac { 1 } { 2 } } \biggl ( w + \frac { 1 } { w } \biggr ) , \qquad | w | = \rho , \qquad \rho \geqslant 1 .
$$

It has its foci at $( \pm 1 , 0 )$ and the sum of its major and minor axes is $2 \rho$ Let $w _ { j } = \rho e ^ { j \pi i / k }$ and $z _ { j } = ( w _ { j } + w _ { j } ^ { - 1 } ) / 2 , j = 0 , \ldots , 2 k - 1 ,$ ,be the corresponding points of $c _ { \rho }$ . Then

$$
\sum { ( z _ { j } ) } = ( - 1 ) ^ { j } , \qquad j = 0 , \ldots , 2 k - 1 ,
$$

is an extremal signature of $\mathcal { P } _ { k - 1 }$

Hint. Associated weights are $( - 1 ) ^ { j }$

# 2.4.9. What happens when $\pmb { \rho } = 1$ in Exercise 2.4.8?

On each compact set $\pmb { B }$ in the complex plane (consisting of $k + 1$ or more points) there exists a unique $\pmb { p } ^ { * } \in \mathcal { P } _ { \pmb { k } }$ with leading coefficient one and minimum maximum modulus. We put $p ^ { * } = T _ { k } ( z ; B )$ and call it the Chebyshev polynomial of degree $\pmb { k }$ of $\pmb { B }$ We know that $T _ { k } ( x ; I ) = \tilde { T } _ { k } ( x )$

2.4.10. If $\pmb { D }$ denotes $| z | \leqslant 1$ ， $T _ { k } ( z ; D ) = z ^ { k }$ .(The best strong uniqueness constant (see (2.13.1)) associated with the best approximation to $z ^ { k }$ out of $\mathcal { P } _ { k - 1 }$ on $\pmb { D }$ is known to be $1 / n .$ The details are in Rivlin [2].)

2.4.11. $T _ { k } ( z ; C _ { \rho } ) = \widetilde { T } _ { k } ( z ) , \rho \geqslant 1 .$

Hint.Use Exercise 2.4.8 and,recalling Exercise 1.1.1, note that $T _ { k } ( z ) = ( w ^ { k } +$ $w ^ { - k } ) / 2$ where $z$ is given by (2.21).

2.4.12.

$$
\operatorname* { m a x } _ { z \in C _ { \rho } } | T _ { k } ( z ; C _ { \rho } ) | = \frac { \rho ^ { k } + \rho ^ { - k } } { 2 ^ { k } } .
$$

2.4.13. Show that all the zeros of $T _ { k } ( z ; B )$ lie in $\begin{array} { r } { \widehat { B } , } \end{array}$ the convex hull of $\pmb { B }$ If we put

$$
\operatorname* { m a x } _ { z \in B } | T _ { k } ( z ; B ) | = m _ { k } ,
$$

then, if $\pmb { B }$ contains infinitely many points,

$$
\delta ( B ) = \operatorname* { l i m } _ { k  \infty } m _ { k } ^ { 1 / k }
$$

exists and is called the transfinite diameter of $\pmb { B } ,$ .Generalizations of the Chebyshev polynomial of $\pmb { B } ,$ ,based on the factorization $| T _ { k } ( z ; B ) | = | z - z _ { 1 } | \cdots | z - z _ { k } | ,$ have been made to other metric spaces (see Hille [1] and Friedman [1]).

2.4.14. $\delta ( I ) = { \textstyle \frac { 1 } { 2 } } ; \delta ( D ) = 1 ; \delta ( C _ { \rho } ) = \rho / 2 .$

2.4.15. If $0 < t < 1$ , the function

$$
w ( z ) = { \frac { z - t } { 1 - t z } }
$$

maps the circle $c \colon | z | = 1$ onto $| w | = 1$ so that, if $e ^ { i \varphi }$ is the image of $e ^ { i \theta }$ ， $\varphi ( \theta )$ increases continuously and monotonically from O to $2 \pi$ as $\pmb \theta$ increases from O to $\pmb { 2 \pi }$

$\begin{array} { r l r } & { 2 . 4 . 1 6 , \ \mathrm { L e t } f ( z ) = 1 / ( 1 - t z ) , } & { 0 < t < 1 , \mathrm { a n d } p ^ { * } ( z ) = 1 + t z + \cdots + t ^ { n - 1 } z ^ { t } } \\ & { ( 1 - t ^ { 2 } ) ^ { - 1 } t ^ { n } z ^ { n } ; } & { \mathrm { t h e n } r ( z ) = f ( z ) - p ^ { * } ( z ) = ( t ^ { n + 1 } ) ( 1 - t ^ { 2 } ) ^ { - 1 } z ^ { n } ( z - t ) / ( 1 - t z ) } \end{array}$ and $E ( r ; D ) = C$

2.4.17. With the notation of Exercise $2 . 4 . 1 6 , p ^ { * }$ is the best approximation to fon $\pmb { D }$ out of $\mathcal { P } _ { \pmb { n } }$ and $E _ { n } ( f ) = t ^ { n + 1 } / ( 1 - t ^ { 2 } )$

Hint.Use the Kolmogorov criterion (Exercise 2.2.1). Note that ${ \pmb n } \pmb { \theta } + \pmb { \varphi } ( \pmb { \theta } )$ increases from 0 to $( 2 n + 2 ) \pi$ as $\pmb \theta$ increases from O to $2 \pi$ ；hence there exist $\theta _ { j } , j = 0 , 1 , . . . , 2 n + 1$ such that $e ^ { i ( n \theta _ { j } + \varphi ( \theta _ { j } ) ) } = ( - 1 ) ^ { j }$ .Consider only the points $e ^ { i \theta _ { j } }$ of $E ( r ; D )$ in (2.9) and observe that $R e p ( e ^ { i \theta } )$ is a trigonometric polynomial of order $\pmb { n }$

2.4.18. If $0 < t < 1$ ，the best approximation to

$$
g ( x ) = { \frac { 1 - t x } { 1 + t ^ { 2 } - 2 t x } }
$$

on $I \colon [ - 1 , 1 ]$ out of $\mathcal { P } _ { \pmb { \pi } }$ is

$$
p ( x ) = 1 + t T _ { 1 } ( x ) + t ^ { 2 } T _ { 2 } ( x ) + \cdots + t ^ { n - 1 } T _ { n - 1 } ( x ) + { \frac { 1 } { 1 - t ^ { 2 } } } t ^ { n } T _ { n } ( x ) ,
$$

and $E _ { n } ( g ; I ) = t ^ { n + 1 } / ( 1 - t ^ { 2 } )$ .The same result holds for $- 1 < t < 1$

Hint. In Exercise 2.4.17, $\operatorname { R e } r ( e ^ { i \theta } ) = [ t ^ { n + 1 } / ( 1 - t ^ { 2 } ) ] \cos { ( n \theta + \varphi ) } .$ ， which assumes its maximum absolute value with alternating signs at $\theta _ { j } , j = 0 , . . . , n + 1$

2.4.19. Find the best approximation out of $\mathcal { P } _ { \pmb { \mathscr { n } } }$ on $\pmb { I }$ to $( x - \lambda ) ^ { - 1 }$ , where $\lambda > 1$

2.4.20. If $q \in \mathcal { P } _ { n + 1 }$ and $\lambda > 1$ ,find the best approximation to $q ( x ) / ( x - \lambda )$ out of $\mathcal { P } _ { \pmb { n } }$ on [-1,1].

Hint.Recall Exercise 2.4.3.

2.4.21. If real $V$ satisfies the Chebyshev condition with respect to $[ a , b ] ,$ ，there exists $\pmb { v } \in { V }$ satisfying ${ \pmb v } ( { \pmb x } ) > { \pmb 0 }$ ， $a \leqslant x \leqslant b$

Hint. If such a $\pmb { v }$ does not exist, consider the best approximation to 1 out of V.

2.4.22. Let $\pmb { X }$ be the $k + 1$ points defined on p. 85 but suppose that $\pmb { V }$ satisfies the Chebyshev condition only with respect to $\pmb { X }$ 、By appropriate modification of the discussion on p. 85 show that (2.17) still holds. How can ${ \pmb v } ^ { * }$ be determined now?

2.4.23. The linear system

$$
\sum _ { j = 1 } ^ { k } a _ { i j } t _ { j } = f _ { i } , \qquad i = 1 , . . . , k + 1
$$

generally has no solution; it is overdetermined. However,we can ask for a best approximate solution, $t ^ { * }$ ，satisfying

$$
\operatorname* { m a x } _ { 1 \leqslant i \leqslant k + 1 } \left. \sum _ { j = 1 } ^ { k } a _ { i j } t _ { j } ^ { \ast } - f _ { i } \right. \leqslant \operatorname* { m a x } _ { 1 \leqslant i \leqslant k + 1 } \left. \sum _ { j = 1 } ^ { k } a _ { i j } t _ { j } - f _ { i } \right.
$$

for all t.If every $k \times k$ submatrix of $A = ( a _ { i j } )$ is nonsingular,show that this problem is a special case of Exercise 2.4.22.

In problems 2.4.24-2.4.32 we are concerned with best approximation to given fon $X = \left\{ x _ { 1 } , \ldots , x _ { k + 1 } / x _ { 1 } > x _ { 2 } > \cdots > x _ { k + 1 } \right\}$ out of $V = \mathcal { P } _ { k - 1 }$

2.4.24. If $\omega ( x ) = ( x - x _ { 1 } ) \cdots ( x - x _ { k + 1 } ) ,$ then (2.17) holds with

$$
\Theta _ { i } = \frac { ( - 1 ) ^ { i } / | \omega ^ { \prime } ( x _ { i } ) | } { \Sigma _ { i = 1 } ^ { k + 1 } \ : 1 / | \omega ^ { \prime } ( x _ { i } ) | } , \qquad i = 1 , \ldots , k + 1 .
$$

2.4.25. Let

$$
\tau = { \frac { f ( x _ { 1 } , \ldots , x _ { k + 1 } ) } { g ( x _ { 1 } , \ldots , x _ { k + 1 } ) } }
$$

(recall the definitionof divided diferences in Exercise 1.3.7), where $\pmb { g }$ is any function satisfying $g ( x _ { i } ) = ( - 1 ) ^ { i } , i = 1 , \ldots , k + 1 .$ Show that $g ( x _ { 1 } , . . . , x _ { k + 1 } ) < 0 ,$ $\rho = | \tau | ( \rho$ is defined in (2.17)), and if $| f ( x _ { 1 } , \dots , x _ { k + 1 } ) | \leqslant h ( x _ { 1 } , \dots , x _ { k + 1 } )$ then $\rho ( f ; X ) \leqslant \rho ( h ; X ) .$

2.4.26. The best approximation tofon $\pmb { X }$ out of $\mathcal { P } _ { k - 1 }$ is given in terms of interpolating polynomials by

$$
p ^ { * } = p - \tau q ,
$$

where $\pmb { p } = \pmb { L } _ { \pmb { k } } ( f , \pmb { X } )$ and $\pmb { q } = L _ { \pmb { k } } ( \pmb { g } , \pmb { X } )$ with $\pmb { \tau }$ and $\pmb { g }$ as defined in Exercise 2.4.25.

2.4.27. The operator $\pi { : } f {  } p ^ { * }$ is linear and satisfies ${ \pmb { \pi } } ^ { 2 } = { \pmb { \pi } } .$

2.4.28. Let $p _ { i } \in \mathcal { P } _ { k - 1 } , i = 1 , . . . , k + 1$ satisfy $p _ { i } ( x _ { j } ) = f ( x _ { j } ) , j = 1 , . . . , k + 1 , j \neq i .$ Then

$$
p ^ { * } = \sum _ { i = 1 } ^ { k + 1 } | \Theta _ { i } | p _ { i } ,
$$

where $\Theta _ { i }$ is given by (2.22).

2.4.29. If $a = - 1$ and $\pmb { b = 1 }$

$$
\rho ( x ^ { k } ; X ) \leqslant { \frac { 1 } { 2 ^ { k - 1 } } } .
$$

Thus

$$
\sum _ { j = 1 } ^ { k + 1 } \frac { 1 } { | \omega ^ { \prime } ( x _ { j } ) | } \geqslant 2 ^ { k - 1 } ,
$$

with equality in both cases if,and only if, $x _ { j } = \eta _ { j - 1 } ^ { ( k ) } , j = 1 , . . . , k + 1$

2.4.30. If $a = - 1$ and $\pmb { b } = 1$ ，

$$
\rho ( x ^ { k + 1 } ; X ) \leqslant \frac { 1 } { 2 ^ { k } } ,
$$

and

$$
\sum _ { j = 1 } ^ { k + 1 } { \frac { 1 } { | \omega ^ { \prime } ( x _ { j } ) | } } \geqslant | x _ { 1 } + \cdots + x _ { k + 1 } | 2 ^ { k } .
$$

Equality holds in both cases only if $x _ { j } = \eta _ { j - 1 } ^ { ( k + 1 ) } , j = 1 , \ldots , k + 1 ;$ or $\begin{array} { r } { x _ { j } = \eta _ { j } ^ { ( k + 1 ) } , j = 1 , } \end{array}$ $\ldots , k + 1$

Hint. If $f ( x ) = x ^ { k + 1 }$ , then $f ( x _ { 1 } , \dots , x _ { k + 1 } ) = x _ { 1 } + \cdots + x _ { k + 1 } .$

# 2.4.31. Show that if

$$
U = \{ \eta _ { 0 } ^ { ( k ) } , \dots , \eta _ { k } ^ { ( k ) } \}
$$

and

$$
T = \{ \xi _ { 1 } ^ { ( k + 1 ) } , . . . , \xi _ { k + 1 } ^ { ( k + 1 ) } \}
$$

we have

$$
\rho ( f ; U ) = \frac { 1 } { k } \left| \sum _ { j = 0 } ^ { k } \prime \prime ( - 1 ) ^ { j } f ( \eta _ { j } ^ { ( k ) } ) \right|
$$

and

$$
\rho ( f ; T ) = \sin \frac { \pi } { 2 ( k + 1 ) } \left| \sum _ { j = 1 } ^ { k + 1 } ( - 1 ) ^ { j } \sin \frac { ( 2 j - 1 ) \pi } { 2 ( k + 1 ) } f ( \xi _ { j } ^ { ( k + 1 ) } ) \right| .
$$

2.4.32. If $X \subset I \colon [ - 1 , 1 ]$ and $f , h \in C ^ { k } ( I ) ,$ then $| f ( x _ { 1 } , \dots , x _ { k + 1 } ) | \leqslant h ( x _ { 1 } , \dots , x _ { k + 1 } )$ for every $\pmb { X }$ if, and only if $| f ^ { ( k ) } ( x ) | \leqslant h ^ { ( k ) } ( x ) ,$ all $\boldsymbol { x } \in \boldsymbol { I }$

Hint.Recall Exercise 1.3.12.

2.4.33. If $| f ^ { ( k ) } ( x ) | \leqslant h ^ { ( k ) } ( x ) .$ all $\boldsymbol { x } \in \boldsymbol { I } ,$ Then

$$
E _ { k - 1 } ( f ) \leqslant E _ { k - 1 } ( h )
$$

on I.

Hint. Exercises 2.4.32 and 2.4.25 plus the remark following Theorem 2.10.

2.4.34. On [-1, 1]

$$
{ \frac { e ^ { - 1 } } { k ! 2 ^ { k - 1 } } } \leqslant E _ { k - 1 } ( e ^ { x } ) \leqslant { \frac { e } { k ! 2 ^ { k - 1 } } } .
$$

(Compare the best approximation to the partial sum of the Taylor series!)

Another consequence of Exercise 2.4.33 is a generalization, due to E. B. Saff (private communication), of the first inequality in Exercise 2.4.34. Namely,let

$$
F _ { k } = \operatorname* { i n f } \left\{ \| f \| _ { I } ; f ^ { ( k ) } ( x ) \geqslant 1 , x \in I \right\}
$$

(where $\| f \| _ { I }$ is the uniform norm on $\pmb { I }$ ), then

$$
F _ { k } = { \frac { 1 } { k ! 2 ^ { k - 1 } } } = \left\| { \frac { T _ { k } } { k ! 2 ^ { k - 1 } } } \right\| _ { I } , \qquad k = 1 , 2 , \ldots .
$$

For if we put $p ( x ) = T _ { k } ( x ) / k ! 2 ^ { k - 1 }$ and suppose that $f ( x )$ satisfies $f ^ { ( k ) } ( x ) \geqslant 1$ ,x∈land $\| f \| _ { I } = F _ { k }$ ,then $\pmb { p } ^ { ( k ) } = 1$ and Exercise 2.4.33 yields $E _ { k - 1 } ( p ) \leqslant E _ { k - 1 } ( f )$ But it is not dificult to see that O is the best approximation to $f$ out of $P _ { k - 1 }$ on $\pmb { I }$ and so $E _ { k - 1 } ( f ) = \| f \| _ { I }$ . Since $E _ { k - 1 } ( p ) = \| p \| _ { I }$ we obtain the desired result.

2.4.35. A trigonometric polynomial of degree $\pmb { n } ,$

$$
t ( \theta ) = \sum _ { j = 0 } ^ { n } { \bigl ( } a _ { j } \cos j \theta + b _ { j } \sin j \theta { \bigr ) } ,
$$

which assumes its maximum $\| \pmb { t } \|$ at $_ { 2 n }$ distinct values of $[ 0 , 2 \pi )$ , is either a constant $( \pm \| t \| )$ or $\| t \| \cos { ( n ( \theta - \theta _ { 0 } ) ) }$ for some $\pmb { \theta _ { 0 } }$

Hint. Analog of Theorem 2.12.

Encouraged by our success in finding the polynomial with leading coefficient 1 that deviates least from zero on $\pmb { I }$ (Theorem 2.1), let us consider fixing the next highest coefficient as well. Suppose ${ \pmb s } \geqslant { \pmb 0 }$ and $\pmb { p } ^ { \ast }$ is the best approximation to $\pmb { x } ^ { k + 1 } - s \pmb { x } ^ { k }$ out of $\mathcal { P } _ { \pmb { k } - 1 }$ on $I .$ The polynomial

$$
Z _ { s , k } ( x ) = x ^ { k + 1 } - s x ^ { k } - p ^ { * }
$$

is called a Zolotarev polynomial of order $\pmb { k }$ and is a generalization of the (monic) Chebyshev polynomial (of order $k + 1 )$ ）to which it reduces when ${ \pmb s } = { \bf 0 }$

# 2.4.36. Show that

$$
Z _ { s , k } ( x ) = { \frac { [ 1 + s / ( k + 1 ) ] ^ { k + 1 } } { 2 ^ { k } } } \ : T _ { k + 1 } \left[ { \frac { ( k + 1 ) x - s } { ( k + 1 ) + s } } \right]
$$

if

$$
0 \leqslant s \leqslant ( k + 1 ) \tan ^ { 2 } \frac { \pi } { 2 ( k + 1 ) } .
$$

2.4.37. $Z _ { - s , k } ( x ) = ( - 1 ) ^ { k + 1 } Z _ { s , k } ( - x ) .$

2.4.38. Discuss $Z _ { s , 1 }$ for all real $\pmb { S } .$

2.4.39. Discuss $Z _ { s , 2 }$ , for all real s.

Hint. Represent the parameter $\pmb { s }$ in terms of a new parameter $\pmb { u }$ by

$$
s = { \frac { 3 u } { 2 } } - { \frac { 1 } { 2 u } } .
$$

More information about the Zolotarev polynomials may be found in Achieser [1], Carlson and Todd [1],and Voronovskaja [1]. The reader interested in numerical approximation of the Zolotarev polynomials,for values of the parameter not covered by Exercise 2.4.36, should consult Paszkowski [1] and Haussmann and Zeller [1].

Theorem 2.1 suggests the problem of finding polynomials with leading coefficient 1 which deviate least from zero on $\pmb { I }$ ,where the deviation is measured in norms other than the uniform one. In the case_of least squares,with respect to the weight $( 1 - x ^ { 2 } ) ^ { - 1 / 2 }$ , we saw in (1.109) that $\tilde { T } _ { n }$ was once again the minimum deviator. More generally,as Szego [1,p.39] shows,for the least-squares norm with respect to a broad class of weight functions the appropriate orthogonal polynomial is the minimum deviator. The next set of exercises is concerned with the same problem in least first powers. If $| g |$ is integrable on $I ,$ we put

$$
\| g \| _ { 1 } = \int _ { 1 } ^ { 1 } | g | d x .
$$

2.4.40. If $\pmb { p } \in \mathcal { P } _ { \pmb { n } - 1 }$ satisfies

$$
\int _ { - 1 } ^ { 1 } \operatorname { s g n } { [ f ( x ) - p ( x ) ] { q ( x ) } d x } = 0
$$

for all $\pmb q \in \mathcal P _ { n - 1 }$ then $\left\| f - p \right\| _ { 1 } \leqslant \left\| f - q \right\| _ { 1 }$ for all $\pmb q \in \mathcal P _ { n - 1 }$

# 2.4.41. Show that

$$
\int _ { - \pi } ^ { \pi } \operatorname { s g n } \left[ \sin \left( n + 1 \right) \theta \right] \sin { k \theta } d \theta = 0 , \qquad k = 1 , \dots , n .
$$

2.4.42. If $r ( x ) = x ^ { n } + c _ { n - 1 } x ^ { n - 1 } + \cdots + c _ { 0 } ,$ then

$$
2 ^ { 1 - n } = \| { \tilde { U } } _ { n } \| _ { 1 } \leqslant \| r \| _ { 1 } .
$$

Hint. $\smash { \tilde { U } _ { p } }$ is the Chebyshev polynomial of the second kind [see (1.23)] normalized so that its leading coefficient is 1. Use Exercises 2.4.40 and 2.4.41 and note that every $q \in \mathcal { P } _ { n - 1 }$ can be written $q = a _ { 0 } U _ { 0 } + \cdots + a _ { n - 1 } U _ { n - 1 }$

2.4.43. If $\pmb { p } \in \mathcal { P } _ { n - 1 }$ satisfies (2.24) and is thus a least-first-power approximation to $f ,$ then

$$
\| f - p \| _ { 1 } = \int _ { - 1 } ^ { 1 } f \operatorname { s g n } \left[ f - p \right] d x .
$$

2.4.44.Equality holds in (.25) only if $\pmb { r } = \tilde { U } _ { \pmb { n } }$

Hint. If $\pmb { r } = \pmb { x } ^ { n } - \pmb { p } _ { 1 }$ and equality holds in (2.25), then

$$
\int _ { - 1 } ^ { 1 } r ( x ) \operatorname { s g n } U _ { n } ( x ) d x = \int _ { - 1 } ^ { 1 } | r ( x ) | d x ,
$$

which implies that $r ( x )$ changes sign precisely as $U _ { \pmb { n } } ( \pmb { x } )$ does at $\eta _ { 1 } ^ { ( n + 1 ) } , \ldots , \eta _ { n } ^ { ( n + 1 ) }$

2.4.45. $\mathbf { I f } f - { \pmb { p } }$ changes sign only at $\eta _ { 1 } ^ { ( n + 1 ) } , \ldots , \eta _ { n } ^ { ( n + 1 ) }$ and $\pmb { p } \in \mathcal { P } _ { n - 1 }$ then $\pmb { p }$ is a leastfirst-power approximation to $f$ on $\pmb { I }$

2.4.46. If ${ \pmb w } ( { \pmb x } )$ is a weight function and $t \geqslant 1$ ,then if $p \in \mathcal { P } _ { n - 1 }$ satisfies

$$
\int _ { - 1 } ^ { 1 } { \mathrm { s g n } } ( f - p ) | f - p | ^ { t - 1 } q ( x ) w ( x ) d x = 0
$$

for all $\pmb q \in \mathcal { P } _ { n - 1 }$

$$
\int _ { - 1 } ^ { 1 } | f - p | ^ { t } w d x \leqslant \int _ { - 1 } ^ { 1 } | f - q | ^ { t } w d x
$$

for all $\pmb q \in \mathcal { P } _ { n - 1 }$

2.4.47. If $q ( x ) = x ^ { n } + a _ { n - 1 } x ^ { n - 1 } + \cdots + a _ { 0 } ,$ then

$$
\int _ { - 1 } ^ { 1 } | \widetilde { T } _ { n } ( x ) | ^ { t } \frac { d x } { \sqrt { 1 - x ^ { 2 } } } \leqslant \int _ { - 1 } ^ { 1 } | q ( x ) | ^ { t } \frac { d x } { \sqrt { 1 - x ^ { 2 } } }
$$

for all $t \geqslant 1$

Another generalization of Theorem 2.1 is to minimize

$$
\operatorname* { m a x } _ { - 1 \leqslant x \leqslant 1 } s ( x ) | x ^ { n } + a _ { n - 1 } x ^ { n - 1 } + \cdots + a _ { 0 } | ,
$$

where $s ( x )$ is a positive continuous function on $I ,$ (Our general theory informs us that $s ( x ) x ^ { n }$ has a unique best approximation out of the space spanned by $s ( \boldsymbol { x } ) , \boldsymbol { x } s ( \boldsymbol { x } ) , \ldots ,$ $x ^ { n - 1 } s ( x )$ on $\pmb { I } .$ ) Such problems have been solved for special choices of $\pmb { s }$ .We put

$$
v _ { k } ( x ) = \sum _ { j = 1 } ^ { k } \bigg ( 1 - { \frac { x } { c _ { j } } } \bigg ) , \qquad k \geqslant 1 , \qquad v _ { 0 } = 1 ,
$$

where the $c _ { j }$ are any points of the complex plane such that $v _ { k } ( x )$ is positive on I. Now consider the case that $\pmb { S } = \pmb { v _ { k } ^ { - 1 } }$ .By means of the mapping (2.21)

$$
c _ { j } = \frac { 1 } { 2 } \bigg ( w _ { j } + \frac { 1 } { w _ { j } } \bigg ) , j = 1 , . . . , k ,
$$

where $| w _ { j } | < 1$ . Suppose that $q _ { k } ( w ) = ( w - w _ { 1 } ) \cdot \cdot \cdot ( w - w _ { k } ) .$

2.4.48. If $w = e ^ { i \varphi }$ ， $0 \leqslant \varphi \leqslant \pi$ , then if ${ x = ( w + w ^ { - 1 } ) / 2 }$

$$
q _ { k } ( w ) q _ { k } ( w ^ { - 1 } ) = \left[ \sum _ { j = 1 } ^ { k } \left( 1 + w _ { j } ^ { 2 } \right) \right] v _ { k } ( x ) = W _ { k } v _ { k } ( x ) .
$$

Hint. Equation (2.27) implies $w _ { j } ^ { 2 } - 2 c _ { j } w _ { j } + 1 = 0$ and the product on the left is therefore a polynomial in $_ { x }$ whose zeros are $c _ { 1 } , \ldots , c _ { k }$

2.4.49. If $\pmb { n } > \pmb { k }$ ， $w = e ^ { i \varphi }$ ， $0 \leqslant \varphi \leqslant \pi$ and $\begin{array} { r } { x = ( w + w ^ { - 1 } ) / 2 , } \end{array}$

$$
\begin{array} { c l } { \displaystyle T _ { n } ( x ; v _ { k } ) = \frac { W _ { k } } { 2 ^ { n } } \left[ w ^ { n - 2 k } \frac { q _ { k } ( w ) } { q _ { k } ( w ^ { - 1 } ) } + w ^ { 2 k - n } \frac { q _ { k } ( w ^ { - 1 } ) } { q _ { k } ( w ) } \right] v _ { k } ( x ) } \\ { \displaystyle = x ^ { n } + b _ { n - 1 } x ^ { n - 1 } + \cdots + b _ { 0 } . } \end{array}
$$

Hint. Use Exercise 2.4.48 and $T _ { j } ( x ) = ( w ^ { j } + w ^ { - j } ) / 2 .$

2.4.50. When $\pmb { S } = \pmb { v _ { k } ^ { - 1 } }$ ,the unique minimum of (2.26) is assumed for $a _ { j } = b _ { j }$ (defined in Exercise 2.4.49), $j = 0 , . . . , n - 1 ;$ i.e., if $\pmb { p } \in \mathcal { P } _ { { n } - 1 }$ is the best approximation to $\pmb { x } ^ { \pmb { n } }$ with respect to weight $[ v _ { k } ( x ) ] ^ { - 1 }$ , then $x ^ { n } - p ( x ) = T _ { n } ( x ; v _ { k } ) .$

# B. MAXIMIZING LINEAR FUNCTIONALS ON $\mathcal { P } _ { \pmb { \pi } }$

# 2.5. An Interpolation Formula for Linear Functionals

We shall continue to use the notation of Section 2.2 throughout this section; however, let $\pmb { B }$ be a compact set in real m-space and $V$ a $k$ -dimensional subspace of the real-valued continuous functions on $B , C ( B )$

Definition 2.9. A (real) linear functional on $V$ is a function, $\pmb { F }$ ,with domain $V$ and range in the real numbers which satisfies $F ( a u + b v ) = a F ( u ) + b F ( v )$ for every ${ \pmb u } , { \pmb v } , \in { \pmb V }$ and any real numbers $a , b$

Examples of linear functionals are $F v = v ( y _ { 0 } ) .$ where ${ \pmb y _ { 0 } }$ is a given point of $\pmb { B }$ (point evaluation functional) or

$$
F v = \int _ { B } v .
$$

If $\varphi _ { 1 } , . . . , \varphi _ { k }$ is a basis for $V ,$ then a linear functional $\pmb { F }$ is completely specified by its values at $\varphi _ { 1 } , ~ \ldots , ~ \varphi _ { k } ;$ for,if $F \varphi _ { j } = c _ { j } , \ j = 1 , \ . . . , k ,$ and $v = a _ { 1 } \varphi _ { 1 } + \cdots + a _ { k } \varphi _ { k }$ ,then $F v = a _ { 1 } c _ { 1 } + \cdots + a _ { k } c _ { k }$ .Furthermore, the set of $\pmb { a }$ such that $v = a _ { 1 } \varphi _ { 1 } + \cdots + a _ { k } \varphi _ { k }$ satisfies $\| \boldsymbol { v } \| \leqslant 1$ is compact; thus $| F v |$ is a continuous function on $\| \boldsymbol { v } \| \leqslant 1$ and assumes its maximum there.

Definition 2.10. If $\pmb { F }$ is a linear functional on $V$ and

$$
\operatorname* { m a x } _ { \| v \| \leqslant 1 } | F v | = M ,
$$

$\pmb { M }$ is called the norm of $\pmb { F }$ ,written $\| \pmb { F } \|$ ,and there exists ${ \pmb v } ^ { * }$ satisfying $\| v ^ { * } \| = 1$ such that $F v ^ { * } = \| F \|$ . Such $v ^ { * }$ are called extremal elements, or extremal, for $\pmb { F }$

When $V$ is $\mathcal { P } _ { \pmb { n } }$ ,Theorem 2.1 says that if

$$
F v = \frac { v ^ { ( n ) } ( 0 ) } { n ! }
$$

then $\| { \boldsymbol { F } } \| = 2 ^ { n - 1 }$ and $T _ { n }$ is the only extremal element for $\pmb { F } .$ Our goal now is to examine a large class of linear functionals on ${ \mathcal { P } } _ { \pmb { n } }$ for which the Chebyshev polynomials are extremal elements. Our main tool in this program is an “interpolation formula” for linear functionals on $V$ which is itself another consequence of Theorem 2.4. Before stating the formula we need a little more information about linear functionals.

The set of $v \in V$ such that $\boldsymbol { F } \boldsymbol { v } = 0$ is called the null-space of $\pmb { F }$ . The nullspace of $\pmb { F }$ is a $( k - 1 )$ dimensional subspace of $V$ (see Exercise 2.5.2).

Theorem 2.13. Let $F ( \neq 0 )$ be a real linear functional on $V .$ Then there exist points $y _ { 1 } , \ldots , y _ { r }$ of $\pmb { B }$ and nonzero real numbers $\alpha _ { 1 } , \ldots , \alpha _ { r } $ with $r \leqslant k ,$ such that for every ${ \mathfrak { v } } \in V$

$$
F v = \sum _ { j \mathop { = } 1 } ^ { r } \alpha _ { j } v ( y _ { j } )
$$

and

$$
\| F \| = \sum _ { j = 1 } ^ { r } | \alpha _ { j } | .
$$

Proof. Let ${ \pmb v } ^ { * }$ be an extremal element for ${ \pmb F }$ If $k = 1$ , then any $\pmb { v } \in \pmb { V }$ can be writen $c v ^ { * }$ ；hence $F v = c F v ^ { * } = c \| F \|$ . Let $y _ { 1 }$ be a point of $\pmb { B }$ such that $v ^ { * } ( y _ { 1 } ) = \varepsilon ,$ ，where $\varepsilon = \pm 1$ ；then $v ( y _ { 1 } ) = c \varepsilon$ and $c = \varepsilon v ( y _ { 1 } )$ Thus ${ \pmb { F } } { \pmb { v } } =$ $\pmb { \varepsilon } \| F \| \pmb { v } ( y _ { 1 } )$ and Theorem 2.13 is proved by choosing $\alpha _ { 1 } = \varepsilon \lVert F \rVert$

Suppose, then,that $k > 1$ Let $V _ { 0 }$ denote the null space of $\pmb { F }$ ，which has dimension $k - 1$ and thus contains nonzero elements.If $v _ { 0 } \in V _ { 0 } ,$ then, since $| F ( v ^ { * } + v _ { 0 } ) | \leqslant \| v ^ { * } + v _ { 0 } \| \| F \|$ and $F ( v ^ { * } + v _ { 0 } ) = \| F \|$ ,we have $\| v ^ { * } + v _ { 0 } \|$ $\geqslant 1 = \| v ^ { * } \|$ . Invoking Theorem 2.4,with $V _ { 0 }$ playing the role of $V$ and $\pmb { g }$ replaced by $v ^ { * }$ , we obtain the existence of $r \leqslant k$ points $y _ { 1 } , \ldots , y _ { r }$ of $E ( v ^ { * } ; B )$ and positive numbers $\lambda _ { 1 } , \ldots , \lambda _ { r }$ such that

$$
\sum _ { i = 1 } ^ { r } \lambda _ { i } v ^ { * } ( y _ { i } ) v _ { 0 } ( y _ { i } ) = 0 ,
$$

all $\pmb { v _ { 0 } } \in V _ { 0 }$

Suppose that $v \in V ;$ then $v _ { 0 } = ( F v ) v ^ { * } - ( F v ^ { * } ) v \in V _ { 0 } ,$ and by substituting this ${ \pmb v _ { 0 } }$ in (2.30) we obtain

$$
( F v ) \sum _ { i = 1 } ^ { r } \lambda _ { i } [ v ^ { * } ( y _ { i } ) ] ^ { 2 } = F v ^ { * } \sum _ { i = 1 } ^ { r } \lambda _ { i } v ^ { * } ( y _ { i } ) v ( y _ { i } )
$$

or, since $| v ^ { * } ( y _ { i } ) | = \| v ^ { * } \| = 1$ and $F v ^ { * } = \| F \|$ ，

$$
( F v ) \sum _ { i = 1 } ^ { r } \lambda _ { i } = \| F \| \sum _ { i = 1 } ^ { r } [ \lambda _ { i } \mathrm { s g n } v ^ { * } ( y _ { i } ) ] v ( y _ { i } ) .
$$

The theorem is now proved by puting

$$
\alpha _ { i } = \frac { \lambda _ { i } \operatorname { s g n } v ^ { * } ( y _ { i } ) } { \Sigma _ { i = 1 } ^ { r } \lambda _ { i } } \parallel F \parallel .
$$

A representation of $\pmb { F }$ of the form (2.29) we callcanonical. An important observation for us is the following:

Theorem 2.14. If $v ^ { * }$ is extremal for $\pmb { F }$ , then for any canonical representation (2.29)

$$
v ^ { * } ( y _ { j } ) = \operatorname { s g n } \alpha _ { j } , \qquad j = 1 , \ldots , r .
$$

Proof.

$$
\sum _ { j = 1 } ^ { r } | \alpha _ { j } | = \| F \| = F v ^ { * } = \sum _ { j = 1 } ^ { r } \alpha _ { j } v ^ { * } ( y _ { j } ) ,
$$

and the theorem follows, since $\| \pmb { v } ^ { * } \| = 1$

# EXERCISES 2.5.1-2.5.12

2.5.1. Show that the set of linear functionals on $V$ is itself a $\pmb { k }$ dimensional normed linear space, the norm being that given in Definition 2.10.

2.5.2. If $F _ { 1 } , \ldots , F _ { s } ( s < k )$ are linearly independent linear functionals on Vand $\pmb { N _ { i } }$ is the null space of $F _ { i } , i = 1 , \ldots , s ,$ then

$$
\bigcap _ { i = 1 } ^ { s } N _ { i }
$$

is a $( k - s )$ -dimensional subspace of $V .$

2.5.3. If $F , F _ { 1 } , \dots , F _ { s }$ are linear functionals on $V$ with respective null spaces $N , N _ { 1 } , \ldots ,$ $N _ { s }$ and

$$
\bigcap _ { i = 1 } ^ { s } N _ { i } \subset N ,
$$

then $\pmb { F }$ is a linear combination of $F _ { 1 } , \ldots , F _ { s }$

2.5.4. Show that no $y _ { i }$ in (2.29a) is a common zero of all elements of $V .$

2.5.5. If $1 \in V ,$ then 1 is extremal for $\pmb { F }$ if, and only if, $\pmb { F }$ has a canonical representation with $\alpha _ { j } > 0 , j = 1 , . . . , r .$

2.5.6. If $1 \in V ,$ then 1 is extremal for $\pmb { F }$ if and only if $\pmb { F }$ is a positive linear functional (i.e., if $v ( y ) \geqslant 0$ ,all $y \in B ,$ ,then $\pmb { F v } \geqslant \mathbf { 0 } .$

2.5.7. Let $\pmb { x } = ( \pmb { x } _ { 1 } , \dots , \pmb { x } _ { m } )$ denote a point in real $\pmb { m }$ space and let $V = P ( m , n )$ be the space of polynomials in $\pmb { x }$ of degree at most ${ \pmb n } ,$ i.e., all $x _ { 1 } ^ { j _ { 1 } } \cdots x _ { m } ^ { j _ { m } }$ with nonnegative integers $j _ { 1 } , \dots , j _ { m }$ satisfying $j _ { 1 } + \cdots + j _ { m } \leqslant n$ form a basis for $P ( m , n )$ It is not hard to see that the dimension of $P ( m , n )$ is $\pmb { k } = \binom { m + n } { m } .$ (The dimension is the number of ways of putting n balls in $m + 1$ bins.To obtain this number we need only calculate the number of ways of choosing $\pmb { m }$ "partitions”( $\mathbf { \lambda } =$ interior bin walls) among $\pmb { n } + \pmb { m }$ objects arranged on a line). Show that if $\pmb { B }$ is a compact set in $\pmb { m }$ space there is a numerical integration formula

$$
\int _ { B } f d x = \sum _ { i = 1 } ^ { r } a _ { i } f ( x ^ { ( i ) } ) , \qquad r \leqslant k ,
$$

with $\mathbf { \boldsymbol { x } } ^ { ( 0 ) } \in \mathbf { \mathit { B } }$ and $a _ { i } > 0 , i = 1 , . . . , r ,$ valid for $f \in P ( m , n )$

Hint. $F f = \int f$ is a positive linear functional.

2.5.8. Let $_ { x }$ denote a point in real $\pmb { m }$ space, let $\pmb { B }$ be a compact set in m space, and $\pmb { V }$ a $\pmb { k }$ dimensional subset of $C ( B )$ spanned by $\varphi _ { 1 } ( x ) , \ldots , \varphi _ { k } ( x )$ with ${ \varphi _ { 1 } } ( x ) > 0$ throughout $\pmb { B }$ Then,if ${ \pmb F }$ is a positive linear functional on $V ,$

$$
F v = \sum _ { i = 1 } ^ { r } a _ { i } v ( x ^ { ( i ) } ) , \qquad r \leqslant k ,
$$

with $\boldsymbol { x } ^ { ( i ) } \in B$ and $a _ { i } > 0 , i = 1 , . . . , r ,$ holds for all ${ \mathfrak { v } } \in V .$ (This result, which implies the result of Exercise 2.5.7,is due to Tchakaloff [1].)

Hint. ${ G f } = F ( \varphi _ { 1 } f )$ is a positive linear functional on the span of 1, $\varphi _ { 2 } / \varphi _ { 1 } , \ldots ,$ $\varphi _ { k } / \varphi _ { 1 }$

2.5.9. If $\pmb { F }$ is a strictly positive linear functional on $\mathcal { P } _ { n } \left( \mathrm { i . e . , i f } p \geqslant 0 , p \neq 0 , \right.$ then $\pmb { F } \pmb { p } > \pmb { 0 } )$ then

$$
\left[ { \frac { n } { 2 } } \right] < r \leqslant n + 1
$$

in any canonical representation of $\pmb { F }$

2.5.10. Put

$$
m = \left[ { \frac { n } { 2 } } \right] + 1 .
$$

Let $\pmb { x } _ { 1 } , \ldots , \pmb { x } _ { m }$ be the distinct zeros of the Legendre polynomial $\pmb { P _ { m } } ( \pmb { x } )$ (cf. p. 56) in $( - 1 , 1 )$ 、Show that there is a numerical integration formula (Gaussian quadrature formula)

$$
\int _ { - 1 } ^ { 1 } f ( x ) d x = \sum _ { i = 1 } ^ { m } a _ { i } f ( x _ { i } )
$$

with $a _ { i } > 0 , i = 1 , \ldots , m ,$ valid for $f \in \mathcal { P } _ { n }$

Hint.The integral in question is a strictly positive linear functional on ${ \mathcal { P } } _ { \pmb { n } }$ .If $\pmb { p } \in \mathcal { P } _ { \pmb { n } }$ is zero at each $\pmb { x _ { i } }$ then $\int p d x = 0$ in view of the orthogonality of the Legendre polynomials.Now apply Exercise 2.5.3.

In the trigonometric case it is easy to see that if

$$
t ( \theta ) = \sum _ { j = 0 } ^ { n } { \bigl ( } a _ { j } \cos j \theta + b _ { j } \sin j \theta { \bigr ) }
$$

then

$$
{ \frac { 1 } { 2 \pi } } \int _ { 0 } ^ { 2 \pi } t ( \theta ) d \theta = { \frac { 1 } { n + 1 } } \sum _ { k = 0 } ^ { n } t \left( { \frac { 2 \pi k } { n + 1 } } \right) .
$$

To verify this it suffices to show that equality holds for $t ( \theta ) = e ^ { i j \theta } , j = 0 , \pm 1 , . . . , \pm n .$ Thus the trapezoidal rule is the analog of Gaussan quadrature for trigonometric polynomials. General trigonometric quadrature formulae of highest degree of accuracy are described by Mysovskikh [1].

2.5.11. Let $V ( F ) = \left\{ v \in V / F v = 1 \right\}$ . Show that (i) if $v ^ { * }$ is extremal for $\pmb { F }$ then $\bar { v } = v ^ { * } / \| F \|$ satisfies

$$
\rho _ { F } ( V ) = \operatorname* { m i n } _ { v \in V ( F ) } \| v \| = \| \bar { v } \| .
$$

(ii) If ${ \bar { v } } \in V ( F )$ satisfies (2.33), then $\bar { v } / \| \bar { v } \|$ is extremal for F. Thus $\| F \| \rho _ { F } ( V ) = 1 ; v ^ { * }$ is unique if, and only if, $\bar { \pmb { v } }$ is unique.

2.5.12. Suppose that $J = [ \alpha , \beta ]$ and $\mathbf { 0 } \not \in J$ If $V _ { 0 } = \left\{ p \in \mathcal { P } _ { n } / p ( 0 ) = 1 \right\}$ show that

$$
\begin{array} { r l } & { \operatorname* { m i n } \parallel p \parallel _ { J } = \parallel \bar { p } \parallel _ { J } } \\ & { p \in V _ { 0 } } \end{array}
$$

where

$$
\bar { p } ( x ) = \frac { T _ { n } \left( \displaystyle \frac { 2 x - ( \alpha + \beta ) } { \beta - \alpha } \right) } { T _ { n } \left( \displaystyle \frac { \alpha + \beta } { \alpha - \beta } \right) } ,
$$

uniquely. Thus

$$
\| \bar { p } \| _ { J } = \frac { 1 } { \left| T _ { n } \left( \frac { \alpha + \beta } { \alpha - \beta } \right) \right| } .
$$

Hint. Use Exercise 2.5.11 with $V = { \mathcal { P } } _ { n } , \ F p = p ( 0 ) , \ V ( F ) = V _ { 0 }$ and recall the Remark following Theorem 2.12.

# 2.6. Linear Functionals on $\mathcal { P } _ { \pmb { n } }$

Henceforth we take $V = \mathcal { P } _ { \pmb { n } }$ and $B = [ - 1 , 1 ]$ . We can now say something about the uniqueness of a canonical representation of $\pmb { F }$

Theorem 2.15. If $\pm 1$ is not the unique extremal for $\pmb { F }$ ,then $\pmb { F }$ has a unique canonical representation.

Proof. Suppose that $\pmb { F }$ has two canonical representations

$$
F p = \sum _ { j = 1 } ^ { r } \alpha _ { j } p ( x _ { j } ) = \sum _ { j = 1 } ^ { s } \beta _ { j } p ( y _ { j } ) , \qquad p \in \mathcal { P } _ { n }
$$

with

$$
\sum _ { j = 1 } ^ { r } | \alpha _ { j } | = \sum _ { j = 1 } ^ { s } | \beta _ { j } | = \left\| F \right\|
$$

and say $\pmb { r } \geqslant \pmb { s } .$

Let $p ^ { * } \neq \pm 1$ be extremal for $\pmb { F }$ ；then，in view of Theorem 2.14, $| p ^ { * } ( x _ { j } ) | = | p ^ { * } ( y _ { i } ) | = 1 , j = 1 , \ldots , r , i = 1 , \ldots , s .$ . Hence the set $\{ x _ { 1 } , \ldots , x _ { r } ,$ $y _ { 1 } , \ldots , y _ { s } \}$ contains $k \leqslant n + 1$ distinct points, $z _ { 1 } , \ldots , z _ { k }$

We claim that $\left\{ x _ { 1 } , \ldots , x _ { r } \right\} = \left\{ y _ { 1 } , \ldots , y _ { s } \right\}$ . Suppose not, say, $x _ { l } \neq y _ { i } , i = 1 ;$ ..., s. Let $z _ { k } = x _ { l }$ .Then

$$
q ( x ) = \prod _ { i = 1 } ^ { k - 1 } \left( x - z _ { i } \right) \in \mathcal { P } _ { n } ,
$$

$q ( x _ { l } ) \neq 0$ and $q ( y _ { i } ) = 0 , \ i = 1 , \ . . . , s .$ Thus $F q = \alpha _ { \iota } q ( x _ { \iota } ) = 0 _ { : }$ ，according to (2.34), a contradiction. Hence $r = s$ and, after renumbering if necessary, $x _ { j } = y _ { j } , j = 1 , \ldots , r .$ Now consider

$$
p _ { j } ( { \boldsymbol x } ) = \prod _ { \stackrel { i = 1 } { i \neq j } } ^ { r } ( { \boldsymbol x } - { \boldsymbol x } _ { i } ) , \qquad j = 1 , \ldots , r ,
$$

$p _ { j } ( x ) \in \mathcal { P } _ { n }$ ,and $p _ { j } ( x _ { i } ) \neq 0 ; F p _ { j } = \alpha _ { j } p _ { j } ( x _ { j } ) = \beta _ { j } p _ { j } ( x _ { j } )$ implies that $\alpha _ { j } = \beta _ { j } , j = 1 _ { \mathrm { { ; } } }$ ..,r.

Remark 1. The requirement that neither 1 nor $^ { - 1 }$ be a unique extremal for $\pmb { F }$ is essential for a canonical representation to be unique, as the following example shows. Consider $\mathcal { P } _ { 2 }$ and the functional $F ( a _ { 0 } + a _ { 1 } x +$ $a _ { 2 } x ^ { 2 } ) = 3 a _ { 0 } + 2 a _ { 2 }$ .Then

$$
F p = p ( - 1 ) + p ( 0 ) + p ( 1 ) = { \frac { 3 } { 2 } } p \left( - { \frac { \sqrt { 6 } } { 3 } } \right) + { \frac { 3 } { 2 } } p \left( { \frac { \sqrt { 6 } } { 3 } } \right) ,
$$

are both canonical representations,and clearly 1 is the unique extremal for $\pmb { F }$

Remark 2. If 1 is an extremal for $\pmb { F }$ , then $\pmb { F }$ has a canonical representation containing a preassigned point, $t ,$ of $\pmb { B }$ ,if, and only if,

$$
\displaystyle \operatorname* { m i n } _ { p \in { \mathcal { Q } } _ { n } } F p = b > 0 ,
$$

where $\mathcal { Q } _ { n } = \{ p \in \mathcal { P } _ { n } / p ( t ) = 1$ and $p ( x ) \geqslant 0 , \ x \in B \}$ . To see this we apply Tchakaloff's theorem (Exercise 2.5.8) to the linear functional $F q - b q ( t ) ,$ which is positive in view of the definition of $\pmb { b }$ and the positivity of $\pmb { F }$ (Exercise 2.5.6), and obtain

$$
F p = b q ( t ) + \sum _ { i = 1 } ^ { r } a _ { i } q ( x _ { i } ) , \qquad r \leqslant n + 1 ,
$$

with $a _ { i } > 0 , i = 1 , . . . , r .$ f $F p ^ { * } = b , p ^ { * } \in \mathcal { Q } _ { n } ,$ ，

$$
b = F p ^ { * } = b + \sum _ { i = 1 } ^ { r } a _ { i } p ^ { * } ( x _ { i } ) ,
$$

and therefore $p ^ { * } ( x _ { i } ) = 0 , i = 1 , \ldots , r ,$ which implies that $r \leqslant n$ (indeed, since $p ^ { * } \geqslant 0 , 2 r \leqslant n )$ ，and we have the required canonical representation. Conversely, if $\pmb { b = 0 }$ and

$$
F q = c q ( t ) + \sum _ { i = 1 } ^ { r } c _ { i } q ( x _ { i } ) , \qquad r \leqslant n ,
$$

with $c , c _ { i }$ positive and $x _ { i } \neq t$ , putting $q = p ^ { * }$ (where $p ^ { * }$ is defined above), yields a contradiction.

Remark 3. Theorem 2.15 remains valid if $\pmb { B }$ is a finite set of $k \leqslant n + 1$ points (as examination of the proof reveals). However, if the finite set $\pmb { B }$ consists of $k > n + 1$ points Theorem 2.15 may be false. For example, take $= 2 , B = \{ - 1 , - { \textstyle \frac { 1 } { 2 } } , { \textstyle \frac { 1 } { 2 } } , 1 \}$ and $F p = p ( 0 )$ Then $\| \pmb { F } \| = 5 / 3$ ， $p ^ { * } ( x ) =$ $( 8 x ^ { 2 } - 5 ) / 3$ is extremal for $\pmb { F }$ and $\pmb { F }$ has two canonical representations,

$$
F p = - { \textstyle \frac { 1 } { 3 } } p ( - 1 ) + p ( - { \textstyle \frac { 1 } { 2 } } ) + { \textstyle \frac { 1 } { 3 } } p ( { \textstyle \frac { 1 } { 2 } } ) = { \textstyle \frac { 1 } { 3 } } p ( - { \textstyle \frac { 1 } { 2 } } ) + p ( { \textstyle \frac { 1 } { 2 } } ) - { \textstyle \frac { 1 } { 3 } } p ( 1 ) .
$$

A result of which we shall make major use provides sufficient conditions for the Chebyshev polynomial to be an extremal of a linear functional.

Theorem 2.16. If $r = n + 1$ in a canonical representation of $\pmb { F }$ ，then the extremals for $\pmb { F }$ are either $\pm T _ { n }$ or $\pm 1$ 、In the former case we may take $y _ { j } = \eta _ { j - 1 } ^ { ( n ) } , j = 1 , \ldots , n + 1 ,$ and $\alpha _ { 1 } , \ldots , \alpha _ { n + 1 }$ alternate in sign.

Proof. Immediate consequence of Theorems 2.14 and 2.12.

Remark. However, $\pmb { r } = \pmb { n } + 1$ is not a necessary condition for $T _ { n }$ to be an extremal, for, consider

$$
F p = \sum _ { j \in J } ( - 1 ) ^ { j } p ( \eta _ { j } ^ { ( n ) } ) ,
$$

where $J$ is some subset of $\{ 0 , 1 , \ldots , n \}$ . Clearly, if $\| { \pmb p } \| = 1$ ,then $| F p | \leqslant | J | \dagger$ ， whereas

$$
F T _ { n } = \sum _ { j \in J } 1 = | J | .
$$

Hence $T _ { n }$ can be an extremal of a linear functional with $1 \leqslant r \leqslant n + 1$ in its canonical representation.

Next, we turn to the question of the uniqueness of extremals for a given linear functional. We define a function on $I , e ( x )$ by

$$
e ( x ) = \left\{ \begin{array} { l l } { 2 , \quad } & { - 1 < x < 1 , } \\ { 1 , \quad } & { x = \pm 1 . } \end{array} \right.
$$

Theorem 2.17. If

$$
\sum _ { j = 1 } ^ { r } e ( y _ { j } ) > n
$$

for some canonical representation of ${ \pmb F }$ , then $\pmb { F }$ has a unique extremal.

Proof. If $p , q$ are both extremals for $\pmb { F }$ ,then s $\mathbf { g n } \alpha _ { j } = p ( y _ { j } ) = q ( y _ { j } )$ so that $p ( y _ { j } ) - q ( y _ { j } ) = 0 _ { ! }$ $j = 1$ $r$ and $p ^ { \prime } ( y _ { j } ) - q ^ { \prime } ( y _ { j } ) = 0$ if $- 1 < y _ { j } < 1 .$ Thus $\pmb { p } - \pmb { q }$ has zeros of total multiplicity greater than in $\pmb { n } ,$ ,in view of (2.35),and $\boldsymbol { p } = \boldsymbol { q }$

Results of a converse nature are not so neat. However, we have the following.

tIf $\pmb { s }$ is a finite set, $| \pmb { S } |$ denotes its cardinality.

Theorem 2.18. If 1 is extremal for $\pmb { F }$ and

$$
\sum _ { j = 1 } ^ { r } \ e ( y _ { j } ) \leqslant n
$$

for some canonical representation, then 1 is not the unique extremal for $\pmb { F }$

Proof. Suppose that $y _ { 1 } < y _ { 2 } < \cdots < y _ { r } \leqslant 1 \leqslant$ If $y _ { r } = 1$ set

$$
q ( x ) = ( 1 - x ) \prod _ { j = 1 } ^ { r - 1 } ( x - y _ { j } ) ^ { e ( y _ { j } ) } ,
$$

while if $y _ { r } < 1$ take

$$
q ( x ) = \sum _ { j = 1 } ^ { r } ~ ( x - y _ { j } ) ^ { e ( y _ { j } ) } .
$$

In either case $\ b { q } \in \mathcal { P } _ { n }$ and $q ( x ) \geqslant 0$ in $I ,$ Choose $A > 0$ and so small that $\| A q \| < 1$ ，then $p = 1 - A q \in \mathcal { P } _ { n }$ and $\| { \pmb p } \| = 1$ ，but $p ( y _ { j } ) = 1 , j = 1 , . . . , r ;$ hence

$$
F { \pmb { p } } = \sum _ { j = 1 } ^ { r } \alpha _ { j } = \| { \pmb { F } } \| .
$$

Since $q \neq 0 , p \neq 1$

Remark. The same result holds if $^ { - 1 }$ is extremal for $\pmb { F }$ .If neither $\pm 1$ is extremal for $\pmb { F }$ ， then (2.35) is not necessary for uniqueness. Consider the remark following Theorem 2.16 with ${ n = 4 }$ and $J = \{ 2 , 3 \}$ . Clearly, $\pmb { T _ { 4 } }$ is extremal and $\pm 1$ is not. Suppose that $\pmb { p } \in \mathcal { P } _ { 4 }$ is also extremal so that $\| { \pmb { p } } \| = 1 ,$ $p ( \eta _ { 2 } ) = 1$ ，and $p ( \eta _ { 3 } ) = - 1$ Then $q = p - T _ { 4 }$ satisfies ${ \mathfrak { q } } ( { \mathfrak { \eta } } _ { j } ) = 0 ;$ ${ q ^ { \prime } } ( \eta _ { j } ) = 0 ;$ $j = 2 , 3$ ，hence

$$
\begin{array} { r } { q = c ( { x } - \eta _ { 2 } ) ^ { 2 } ( { x } - \eta _ { 3 } ) ^ { 2 } , } \end{array}
$$

but $| p ( 1 ) | = | 1 - q | \leqslant 1$ requires $c \geqslant 0 ,$ ，whereas $| p ( \eta _ { 1 } ) | = | - 1 - q | \leqslant 1$ requires $c \leqslant 0$ Hence $c = 0$ and $\begin{array} { r } { p = T _ { 4 } } \end{array}$

To obtain a necessry condition for uniqueness we proceed as follows. If $\pmb { p } \in \mathcal { P } _ { \pmb { n } }$ ,let $N ( p )$ denote the total multiplicity with which the values 1 and -1 are assumed by $\pmb { p }$ in $\pmb { I }$ (Thus $N ( T _ { n } ) = 2 n .$ ）

Theorem 2.19. If $\pmb { F }$ has a unique extremal, $\pmb { p }$ ,then $N ( p ) > n .$

Proof. We show that if $N ( p ) \leqslant n$ then $\pmb { F }$ has an extremal other than $\pmb { p }$ Suppose that $N ( p ) \leqslant n$

Let $x _ { 1 } , \ldots , x _ { s }$ satisfying $- 1 \leqslant x _ { 1 } < \cdots < x _ { s } \leqslant 1$ be all the points of $\pmb { I }$ at which $p ( x ) = 1$ and let ${ \pmb m } _ { i }$ be the multiplicity of the zero of $1 - p ( x )$ at $\boldsymbol { x } _ { i }$ .Let $z _ { 1 } , \ldots , z _ { t }$ satisfying $- 1 \leqslant z _ { 1 } < \cdots < z _ { t } \leqslant 1$ be all the points of $\pmb { I }$ at which $p ( x ) = - 1$ and let ${ \pmb n } _ { i }$ be the multiplicity of the zero of $1 + p ( x )$ at $z _ { i }$ .(We need only consider the case $s \geqslant 1 , t \geqslant 1$ ,for if $p ( { \boldsymbol { x } } )$ omits the value $^ { - 1 }$ ,say,on $\pmb { I }$ ， then either $p = 1$ and nonuniqueness follows from Theorem 2.18 or $p \neq 1$ and 1 is another extremal for $\pmb { F }$ Similarly, if $\pmb { p }$ omits the value 1.)

Put

$$
q _ { 1 } ( x ) = c _ { 1 } \prod _ { i = 1 } ^ { s } ( x - x _ { i } ) ^ { m _ { i } }
$$

and

$$
q _ { 2 } ( x ) = c _ { 2 } \prod _ { i = 1 } ^ { t } ( x - z _ { i } ) ^ { n _ { i } } ,
$$

where $c _ { 1 }$ and $\boldsymbol { c } _ { 2 }$ are chosen so that there is some subinterval of $\pmb { I }$ in which $q _ { 1 } ( x ) > 0$ and another in which $q _ { 2 } ( x ) > 0$ Thus $1 - p ( x ) = q _ { 1 } ( x ) p _ { 1 } ( x )$ where $p _ { 1 } ( x ) > 0$ throughout $\pmb { I }$ and $1 + p ( x ) = q _ { 2 } ( x ) p _ { 2 } ( x )$ where $p _ { 2 } ( x ) > 0$ throughout $I .$ Note,also， that, since $0 \leqslant 1 - p ( x )$ and $0 \leqslant 1 + p ( x ) .$ $q _ { 1 } ( x ) \geqslant 0$ and $q _ { 2 } ( x ) > 0$ for all $\mathbf { { \boldsymbol { x } } } \in I , $ ，whereas $q = q _ { 1 } q _ { 2 } \in \mathcal { P } _ { n }$ in view of our assumption that $N ( p ) \leqslant n .$ Let

$$
b = \operatorname* { m i n } _ { { \boldsymbol { x } } \in I } { \frac { p _ { 1 } ( { \boldsymbol { x } } ) } { q _ { 2 } ( { \boldsymbol { x } } ) } } ;
$$

then $b > 0 ;$ and if $0 < a \leqslant b$ we assert that $p ( x ) + a q ( x ) = r ( x )$ satisfies $\| r \| = 1$ ,for $a \leqslant b$ implies that $a q ( x ) \leqslant q _ { 1 } ( x ) p _ { 1 } ( x ) ,$ hence $r ( x ) \leqslant 1$ for all $\boldsymbol { x } \in \boldsymbol { I }$ ， whereas ${ \pmb a } > { \bf 0 }$ implies $a q ( x ) \geqslant - q _ { 2 } ( x ) p _ { 2 } ( x )$ and $r ( x ) \geq - 1$ . Since $r ( x _ { i } ) = p ( x _ { i } )$ and $r ( z _ { i } ) = p ( z _ { i } ) , r$ is another extremal.

# EXERCISES 2.6.1-2.6.13

2.6.1.The remark following Theorem 2.16 is not convincing unless we know that the $\pmb { F }$ defined there does not have another canonical representation involving $\pm 1$ points. Show that this is the case.

2.6.2. If $\pmb { F } \pmb { x } ^ { i } = \pmb 0$ for all odd i, $0 \leqslant i \leqslant n ,$ show that ${ \pmb F }$ has an even extremal. If $\pmb { F } \pmb { x } ^ { i } = \pmb 0$ for all even i, $0 \leqslant i \leqslant n ,$ show that $\pmb { F }$ has an odd extremal.

2.6.3. If $\pmb { F } \pmb { x ^ { i } } = \pmb 0$ ,either for all odd ior for all even i, $0 \leqslant i \leqslant n ,$ and neither of $\pm 1$ is an extremal for ${ \pmb F } _ { \pmb { \bot } }$ ，show that ${ \pmb F }$ has a canonical representation in which the points are symmetric about zero.In the second case zero is not one of the points. Also, the coefficients [the $\alpha _ { j }$ in (2.29a)] of symmetric points are equal.

Hint. Put ${ \boldsymbol { x } } ^ { 2 } = t$ and consider either polynomials of degree at most $[ n / 2 ]$ or linear combinations of $t ^ { 1 / 2 } , t ^ { 3 / 2 } , \dotsc , t ^ { [ ( n + 1 ) / 2 ] - 1 / 2 }$ on [0,1].

2.6.4. If the null space of ${ \pmb F }$ satisfies the Chebyshev condition, the only extremals of $\pmb { F }$ are either $\pm T _ { n }$ or $\pm 1$

2.6.5. Consider the linear functional on $\mathcal { P } _ { 2 } , F p = p ( - 1 ) - p ( 0 ) .$ Show that $\| \pmb { F } \| = 2$ and $\boldsymbol { T _ { 2 } }$ is the unique extremal for ${ \pmb F }$

2.6.6. Show that the null space $V _ { 0 }$ of the functional ${ \pmb F }$ defined in Exercise 2.6.5 does not satisfy the Chebyshev condition.

2.6.7. Let $V _ { 0 }$ be as in Exercise 2.6.6. Show that there is a unique best approximation to $x ^ { 2 }$ out of $V _ { 0 }$ on [-1,1].

The set of $\pmb { p } \in \mathcal { P } _ { n }$ satisfying $\| p \| \leqslant 1 ( \| \cdot \|$ is the maximum norm on $\pmb { I }$ )is a compact convex set, $B _ { n }$ ，the unit ball in ${ \mathcal { P } } _ { n }$ . A point $\pmb { p } \in \pmb { B } _ { \pmb { n } }$ is an extreme point of $\pmb { { \cal B } } _ { \pmb { \eta } }$ if $p = ( p _ { 1 } + p _ { 2 } ) / 2$ with $\pmb { p _ { 1 } } , \pmb { p _ { 2 } } \in \pmb { B _ { n } }$ implies $\pmb { p } = \pmb { p _ { 1 } } = \pmb { p _ { 2 } }$ . Let us denote the set of extreme points of $B _ { n }$ by $E ( B _ { n } )$

2.6.8. $1 \in E ( B _ { n } )$ for $\pmb { n = 0 } , 1 , 2 , \ldots .$

2.6.9. If $\pmb { p } \in \pmb { B } _ { n }$ and $p ( \mathbf { \boldsymbol { x } _ { 0 } } ) = 1$ ,where $- 1 < x _ { 0 } < 1$ , then there exists a positive integer m such that $p ( x ) = 1 - ( x - x _ { 0 } ) ^ { 2 m } r ( x ) ,$ where $r ( x ) \geqslant 0$ in $\pmb { I }$ and ${ r } ( x _ { 0 } ) > 0$

2.6.10. If $\pmb { p } = ( p _ { 1 } \cdot + p _ { 2 } ) / 2$ ，where $p _ { 1 } , p _ { 2 } \in B _ { n } , p ( x _ { 0 } ) = \varepsilon ,$ and ${ p ^ { ( k ) } ( x _ { 0 } ) = 0 }$ ， $k = 1$ $k _ { 0 } - 1 , p ^ { ( k _ { 0 } ) } ( x _ { 0 } ) \neq 0 ,$ where $\boldsymbol { x } _ { 0 } \in I$ and $\pm 1$ Then, for $j = 1$ 2, $\pmb { p } _ { j } ( \pmb { x } _ { 0 } ) = \pmb { \varepsilon }$ and $p _ { j } ^ { ( k ) } ( x _ { 0 } ) = 0 , k = 1 , 2 , . . . , k _ { 0 } - 1 .$

2.6.11. If $\pmb { p } \in \pmb { B } _ { n }$ then $\pmb { \mathnormal { p } } \in \pmb { \cal { E } } ( \pmb { \cal { B } } _ { n } )$ if, and only if, $N ( p ) > n .$ (Notation as in Theorem 2.19.)

Hint. (i) The “if" part follows from Exercise 2.6.9,10;(ii)“only if" by construction following that given in the proof of Theorem 2.19.

$$
T _ { n } \in E ( B _ { k } ) , n \leqslant k \leqslant 2 n - 1 \mathrm { ~ b u t ~ } T _ { n } \notin E ( B _ { 2 n } ) .
$$

2.6.13. Suppose 1 is an extremal for $\pmb { F }$ (hence $\pmb { F }$ is a positive linear functional); then the following are equivalent:

(i) $\Sigma _ { i = 1 } ^ { r } e ( y _ { i } ) \leqslant n$ for some canonical representation of $\pmb { F }$ (ii) 1 is not the unique extremal for $\pmb { F }$ (iii) $\pmb { F }$ is not strictly positive (see Exercise 2.5.9). (iv) ${ \pmb F }$ has a unique canonical representation.

Hint. Remark 2 following Theorem 2.15 can be used to show that (iv) implies(ii).

# 2.7. Some Examples in which the Chebyshev Polynomials Are Extremal

We want next to use Theorem 2.16 in order to conclude that the Chebyshev polynomial is the extremal for certain specific functionals. Indeed, we shall examine a series of functionals that exemplify the following general scheme. Let $C _ { n }$ denote the (convex) subset of $\mathcal { P } _ { \pmb { n } }$ consisting of $\pmb { p }$ satisfying

$$
\operatorname* { m a x } _ { j = 0 , \dots , n } | p ( \eta _ { j } ^ { ( n ) } ) | \leqslant 1 .
$$

Theorem 2.20. Let $\pmb { F }$ be a linear functional on $\mathcal { P } _ { \pmb { n } }$ such that (i) neither $\pm 1$ is an extremal for $\pmb { F }$ (ii) $\pmb { p } \in \mathcal { P } _ { \pmb { n } }$ ， $p \neq 0 ,$ having $\pmb { n }$ distinct zeros in $I _ { : }$ ，implies $F p \neq 0 .$ Then

$$
| F p | \leqslant | F T _ { n } | , \qquad p \in C _ { n } ,
$$

with equality holding if,and only if, $p = \pm T _ { n }$

Proof. Let

$$
F p = \sum _ { j \mathop { = } 1 } ^ { r } \alpha _ { j } p ( y _ { j } )
$$

be a canonical representation of $\pmb { F }$ If $r \leqslant n ,$ ，there exists $\begin{array} { r } { p _ { 0 } \in \mathcal { P } _ { n } , ~ p _ { 0 } \not = 0 , } \end{array}$ satisfying $p _ { 0 } ( y _ { j } ) = 0 , j = 1 , . . . , r ,$ ;hence $F p _ { 0 } = 0$ ,contradicting the hypothesis (if $r < n ,$ choose $\pmb { p _ { 0 } }$ to have zeros at any $n - r$ points of $\pmb { I }$ other than the $y _ { j } .$ Thus $r = n + 1$ and, in view of Theorem 2.16, $y _ { j } = \eta _ { j - 1 } ^ { ( n ) } , j = 1 , \dots , n + 1$ ,and $\| F \| = \| F T _ { n } | .$ but if ${ \pmb { p } } \in C _ { \pmb { n } }$

$$
| F p | \leqslant \sum _ { j = 1 } ^ { n + 1 } | \alpha _ { j } | | p ( \eta _ { j - 1 } ^ { ( n ) } ) | \leqslant \sum _ { j = 1 } ^ { n + 1 } | \alpha _ { j } | = \| F \| = | F T _ { n } | . \quad =
$$

Remark. The theorem remains true, of course, with the condition, $\pmb { p } \in \pmb { C } _ { \pmb { n } }$ strengthened to $\pmb { p } \in \pmb { B _ { n } }$ (i.e., $\| p \| \leqslant 1 )$ . It is in this weaker form that results of the kind we are about to give occur most frequently in the literature. In some of the examples we rely directly on Theorem 2.13 with $V$ other than $\mathcal { P } _ { \pmb { n } }$ ,but the line of argument is analogous to an application of Theorem 2.20.

1. Growth Outside the Interval. If $\pmb { p } \in \pmb { C } _ { \pmb { n } }$ ,then

$$
| p ^ { ( j ) } ( t ) | \leqslant | T _ { n } ^ { ( j ) } ( t ) |
$$

for $| t | \geqslant 1$ and $j = 0 , 1 , \ldots , n .$ Equality is possible in (2.37) for $j \geqslant 1$ or $| t | > 1$ only if $p = \pm T _ { n }$ (cf. Exercise 1.5.11).

To establish (2.37) we put $F p = p ^ { ( j ) } ( t ) . \operatorname { I f } j = 0$ and $t = \pm 1 , ( 2 . 3 7 )$ is trivially true (with equality holding for all ${ \pmb { p } } \in { \pmb { C } } _ { \pmb { n } }$ satisfying $| p ( t ) | = 1 \}$ . Suppose that $j \geqslant 1$ or $| t | > 1$ ; then neither of $\pm 1$ is extremal for $\pmb { F }$ ,since $| F 1 | < | F T _ { n } |$ Also, if $p \neq 0$ has $\pmb { n }$ distinct zeros in $I _ { : }$ ，it has no zero in $| t | > 1$ and, by Rolle's Theorem, $\pmb { p } ^ { ( j ) }$ has no zero in $| t | \geqslant 1$ ; that is, $F p \neq 0 .$ (i) and (ii) in the hypotheses of Theorem 2.20 are thus in force and our result follows from Theorem 2.20.

Remark. In particular, taking $j = n ,$ ，we see that if $\pmb { p } \in C _ { \pmb { n } }$ has leading coefficient ${ \pmb a } _ { \pmb { n } }$ then $| a _ { n } | \leqslant 2 ^ { n - 1 }$ ，with equality only for $p = \pm T _ { n }$ . One consequence of this observation is the following generalization of Theorem 2.1 $( n > 0 )$ .If

$$
p ( x ) = x ^ { n } + a _ { n - 1 } x ^ { n - 1 } + \cdots + a _ { 0 } ,
$$

then

$$
\operatorname* { m a x } _ { j = 0 , \dots , n } | p ( \eta _ { j } ^ { ( n ) } ) | \geqslant \operatorname* { m a x } _ { j = 0 , \dots , n } | \widetilde { T } _ { n } ( \eta _ { j } ^ { ( n ) } ) | = 2 ^ { 1 - n } ,
$$

with equality only for ${ p } = \pm \tilde { T } ,$ for if $p \neq \pm \widetilde { T } _ { n }$ and

$$
\operatorname* { m a x } _ { j = 0 , \dots , n } | p ( \eta _ { j } ^ { ( n ) } ) | \leqslant 2 ^ { 1 - n }
$$

then

$$
2 ^ { n - 1 } p \in C _ { n } .
$$

Another consequence of the same observation is an interesting characterization of the Chebyshev polynomials due to DeVore [1].

f $p ( { \boldsymbol { x } } ) = c ( { \boldsymbol { x } } - { \boldsymbol { x } } _ { 1 } ) \cdots ( { \boldsymbol { x } } - { \boldsymbol { x } } _ { n } )$ has all its zeros in [-1,1] and satisfies

$$
| p ( \eta _ { j } ^ { ( n ) } ) | = 1 , \qquad j = 0 , \ldots , n ,
$$

then $p = \pm T _ { n }$ . To see this note that

$$
\begin{array} { l } { { 1 = | p ( \eta _ { 0 } ) p ^ { 2 } ( \eta _ { 1 } ) \cdots p ^ { 2 } ( \eta _ { n - 1 } ) p ( \eta _ { n } ) | } } \\ { { \displaystyle \quad = | p ( \eta _ { 0 } ) \cdots p ( \eta _ { n } ) | | p ( \eta _ { 1 } ) \cdots p ( \eta _ { n - 1 } ) | } } \\ { { \displaystyle \quad = | c | ^ { n + 1 } \prod _ { j = 1 } ^ { n } \left| \sum _ { i = 0 } ^ { n } \left( \eta _ { i } - x _ { j } \right) \right| \cdot | c | ^ { n - 1 } \sum _ { j = 1 } ^ { n } \left| \prod _ { i = 1 } ^ { n - 1 } ( \eta _ { i } - x _ { j } ) \right| } } \\ { { \displaystyle \qquad \quad = \frac { | c | ^ { 2 n } } { [ n ^ { 2 } 2 ^ { 2 ( n - 1 ) } ] ^ { n } } \sum _ { j = 1 } ^ { n } \left( 1 - x _ { j } ^ { 2 } \right) [ T _ { n } ^ { \prime } ( x _ { j } ) ] ^ { 2 } . } } \end{array}
$$

But in view of the Chebyshev differential equation (2.18)

$$
( 1 - x _ { j } ^ { 2 } ) [ T _ { n } ^ { \prime } ( x _ { j } ) ] ^ { 2 } = n ^ { 2 } ( 1 - T _ { n } ^ { 2 } ( x _ { j } ) ) \leqslant n ^ { 2 } ;
$$

hence

$$
1 \leqslant \left( { \frac { | c | } { 2 ^ { n - 1 } } } \right) ^ { 2 n }
$$

or

$$
| c | \geqslant 2 ^ { n - 1 } .
$$

Since ${ \pmb { p } } \in C _ { \pmb { n } }$ we know that $| c | \leqslant 2 ^ { n - 1 }$ ; hence $| c | = 2 ^ { n - 1 }$ and $p = \pm T _ { n }$

2. Size of Coefficients. If $p = a _ { 0 } + \cdots + a _ { n } x ^ { n }$ and $\pmb { p } \in \pmb { C } _ { \pmb { n } }$ ， then

$$
{ \left| \sum _ { j = i } ^ { \lfloor n / 2 \rfloor } a _ { n - 2 j } \right| \leqslant \left| \sum _ { j = i } ^ { \lfloor n / 2 \rfloor } t _ { n - 2 j } ^ { ( n ) } \right| } , \qquad i = 0 , 1 , \ldots , { \left[ \frac { n } { 2 } \right] } .
$$

Let us put

$$
F _ { i , n } p = \sum _ { j = i } ^ { [ n / 2 ] } a _ { n - 2 j } , \qquad i = 0 , . . . , \biggl [ \frac { n } { 2 } \biggr ] .
$$

Our aim is to show that $\pm T _ { n }$ is extremal for $F _ { i , n }$ .If $\pmb { i } = \pmb { 0 }$ or $[ n / 2 ]$ ,(2.38) holds trivially with equality for any $p \in C _ { n }$ satisfying $p ( 1 ) = \pm 1$ or $p ( 0 ) = \pm 1 _ { : }$ ， respectively. This disposes of the cases $\pmb { n = 1 }$ ，2 and we need only establish (2.38) if $\pmb { n } \geqslant 3$ and $0 < i < [ n / 2 ]$

Suppose that $a _ { n } = 1 , p \in \mathcal { P } _ { n }$ is even for even n or odd for odd $\pmb { n } ,$ and either (i) $\pmb { p }$ has $\pmb { n }$ distinct zeros in $\pmb { I }$ or (ii) $\pmb { p }$ has a zero of order 2 at zero and $\pmb { n } - 2$ other distinct zeros in $I .$ Then $F _ { 0 , n } p = p ( 1 ) \geqslant 0 ;$ since ${ a } _ { n } = 1$ ,and we claim that if $n \geqslant 4$ is even

$$
( - 1 ) ^ { n - 1 } F _ { i , n } p > 0 , \qquad i = 1 , . . . , \frac { n } { 2 } - 1 ,
$$

and

$$
( - 1 ) ^ { n / 2 } F _ { n / 2 , n } p \geqslant 0 ,
$$

with equality if, and only if, $p ( 0 ) = 0$ ，whereas if $n \geqslant 3$ is odd

$$
( - 1 ) ^ { n - i } F _ { i , n } p < 0 , \qquad i = 1 , . . . , \frac { n - 1 } { 2 } .
$$

We verify this claim by mathematical induction on n. Consider first even n. Suppose that $n = 4 .$ Let $^ { c }$ be the smallest nonnegative zero of $\pmb { p }$ Then $p = ( x ^ { 2 } - c ^ { 2 } ) ( x ^ { 2 } - a ^ { 2 } ) .$ where $0 < | a | \leqslant 1 , F _ { 2 , 4 } p = a ^ { 2 } c ^ { 2 } \geqslant 0 ,$ ，with equality if, and only if, $\begin{array} { r } { \pmb { c } = \pmb { 0 } ; } \end{array}$ and $F _ { 1 , 4 } p = a ^ { 2 } c ^ { 2 } - ( a ^ { 2 } + c ^ { 2 } ) = c ^ { 2 } ( a ^ { 2 } - 1 ) - a ^ { 2 } < 0$ verifying (2.39a,b). Suppose that (2.39a,b) hold for $n \geqslant 4$ and suppose even $\pmb { p } \in \mathscr { P } _ { n + 2 }$ has $a _ { n + 2 } = 1$ and satisfies (i) or (ii) above. Let $^ { c }$ be the smallest nonnegative zero of $\pmb { p }$ Then $p = ( x ^ { 2 } - c ^ { 2 } ) r$ where $\boldsymbol { r } \in \mathcal { P } _ { n }$ is even, has leading coefficient 1, satisfies (i), and

$$
( - 1 ) ^ { n + 2 - i } F _ { i , n + 2 } p = ( - 1 ) ^ { n - i } F _ { i , n } r + c ^ { 2 } ( - 1 ) ^ { n - ( i - 1 ) } F _ { i - 1 , n } r
$$

so that (2.39a,b) hold and (2.39a,b) are therefore valid for all even $\pmb { n } .$ In the case that $n ( \geqslant 3 )$ is odd a similar argument establishes (2.40).

Now let a canonical representation of $F _ { i , n } ( n \geqslant 3 , i = 1 , . . . , [ ( n - 1 ) / 2 ] )$ with points symmetric about the origin be

$$
F _ { i , n } q = \sum _ { j = 1 } ^ { r } \alpha _ { j } q ( y _ { j } ) , \qquad q \in \mathcal { P } _ { n } ,
$$

the existence of such a canonical representation being assured by Exercise 2.6.3, provided that $\pm 1$ is not an extremal of $F _ { i , n }$ ；but they are clearly not extremals for odd $\pmb { n } _ { \pmb { \imath } }$ ,and for even $\pmb { n }$

$$
F _ { i , n } 1 = 1 < | F _ { i , n } T _ { n - 2 ( i + 1 ) } | = 2 ^ { n - 2 i + 3 } - 1 .
$$

$\mathbf { I f } \ r \leqslant n ,$ ,there exists $\pmb { p } \in \mathcal { P } _ { \pmb { n } }$ ,even for even n or odd for odd $\pmb { n }$ ,satisfying (i) or (ii) and taking the value zero at $y _ { 1 } , \ldots , y _ { r }$ such that, according to (2.39) or (2.40), $F _ { i , n } p \neq 0$ Thus $\pmb { r } = \pmb { n } + 1$ and either $\pm T _ { n }$ or $\pm 1$ is extremal for $F _ { i , n }$ ; but we have just seen that $\pm 1$ is not an extremal for $F _ { i , n }$ ,hence $y _ { j } = \eta _ { j - 1 } ^ { ( n ) } , j = 1 , \ldots ,$ $n + 1$ and (2.38) is established, with equality only for $p = \pm T _ { n }$ ,if $\pmb { n } \geqslant 3$ and $0 < i < [ n / 2 ]$

Remark 1. If $p = a _ { 0 } + a _ { 1 } x + \cdots + a _ { n } x ^ { n } , p \in B _ { n }$ , and we put

$$
A _ { i } ( x ) = \sum _ { j = 1 } ^ { [ n / 2 ] } a _ { n - 2 j } x ^ { n - 2 j }
$$

for each $i = 0 , . . . , [ n / 2 ]$ Then, if, for some $i ,$

$$
\operatorname* { m a x } _ { { \boldsymbol x } \in I } | A _ { i } ( { \boldsymbol x } ) | = | A _ { i } ( { \boldsymbol x } _ { 0 } ) | ,
$$

the polynomial $q = p ( x _ { 0 } x ) \in C _ { n }$ and so, in view of (2.38) applied to $\pmb q .$

$$
\| A _ { i } ( x ) \| = \left| \sum _ { j = i } ^ { [ n / 2 ] } a _ { n - 2 j } x _ { 0 } ^ { n - 2 j } \right| \leqslant \left| \sum _ { j = i } ^ { [ n / 2 ] } t _ { n - 2 j } ^ { ( n ) } \right| , \qquad i = 0 , \ldots , [ n / 2 ] .
$$

In partcular, we have, taking $a _ { n - 2 j } = t _ { n - 2 j } ^ { ( n ) }$

$$
| t _ { 0 } ^ { ( n ) } + \cdots + t _ { i } ^ { ( n ) } | = \| t _ { 0 } ^ { ( n ) } + \cdots + t _ { i } ^ { ( n ) } x ^ { i } \| , \qquad i = 0 , \ldots , n .
$$

In a similar vein, if we know that

$$
| a _ { i } + \cdots + a _ { n } | \leqslant | b _ { i } + \cdots + b _ { n } |
$$

for all $p = a _ { 0 } + \cdots + a _ { n } x ^ { n } \epsilon B _ { n }$ ，which are even for even $\pmb { n }$ or odd for odd ${ \pmb n } _ { \pmb { \imath } }$ then $\| a _ { i } x ^ { i } + \cdots + a _ { n } x ^ { n } \| \leqslant | b _ { i } + \cdots + b _ { n } |$ 、Moreover, we note that

$$
a _ { i } + \cdots + a _ { n } = p ( 1 ) - ( a _ { 0 } + \cdots + a _ { i - 1 } ) ,
$$

so that $| a _ { i } + \cdots + a _ { n } | \leqslant 1 + | t _ { 0 } ^ { ( n ) } + \cdots + t _ { i - 1 } ^ { ( n ) } | ;$ but we observed in Exercise 1.2.19 that the numbers $t _ { 0 } ^ { ( n ) } + \cdots + t _ { n - 2 j } ^ { ( n ) } , j = 0 , . . . , [ n / 2 ]$ alternate in sign. Therefore, since $t _ { 0 } ^ { ( n ) } + \cdots + t _ { i - 1 } ^ { ( n ) } = 1 - ( t _ { i } ^ { ( n ) } + \cdots + t _ { n } ^ { ( n ) } )$ is negative for $[ n / 2 ]$ of the indices $i = 1$ ，.， $n + 1$ ，and when that is the case $1 + | t _ { 0 } ^ { ( n ) } + \cdots$ $+ t _ { i - 1 } ^ { ( n ) } | = | t _ { i } ^ { ( n ) } + \cdots + t _ { n } ^ { ( n ) } |$ ，we conclude that at least “half” the time

$$
| a _ { i } + \cdots + a _ { n } | \leqslant | t _ { i } ^ { ( n ) } + \cdots + t _ { n } ^ { ( n ) } | ,
$$

hence $\| a _ { i } x ^ { i } + \cdots + a _ { n } x ^ { n } \| \leqslant | t _ { i } ^ { ( n ) } + \cdots + t _ { n } ^ { ( n ) } |$ . Indeed,Reimer [1] describes the relatively few cases in which (2.43) fails to hold.

Note that (2.42) is no longer true if we require only ${ \pmb { p } } \in C _ { \pmb { n } }$ . Consider, for example, $\pmb { n }$ an even integer greater than 2 and

$$
p ( x ) = 1 - \prod _ { j = 0 } ^ { ( n / 2 - 1 ) } ( [ \eta _ { j } ^ { ( n ) } ] ^ { 2 } - x ^ { 2 } ) ;
$$

$p \in C _ { n }$ ,but since $p ( \eta _ { j } ) = 1$ and $p ^ { \prime } ( \eta _ { j } ) \neq 0$ for some $j \neq 0 , \| p \| > 1$ and $p \notin B _ { n }$ Also $\| p \| = \| A _ { n / 2 } ( x ) \| > | t _ { 0 } ^ { ( n ) } + \dots + t _ { n } ^ { ( n ) } |$

Remark 2. Suppose $p = a _ { 0 } + a _ { 1 } x + \cdots + a _ { n } x ^ { n }$ If $\pmb { n } - j$ is even (or zero) and $\pmb { p } \in C _ { \pmb { n } }$ ,then

$$
\begin{array} { r } { | a _ { j } | \leqslant | t _ { j } ^ { ( n ) } | . } \end{array}
$$

f ${ \pmb n } - j$ is odd and $p \in C _ { n - 1 }$ ,then

$$
| a _ { j } | \leqslant | t _ { j } ^ { ( n - 1 ) } | .
$$

Equality in (2.44) occurs only if $p = \pm T _ { n }$ for $j > 0$ and equality in (2.45) occurs only if $p = \pm T _ { n - 1 }$ for $j > 0$ and $n > 2$

Proof. If $j = 0$ , (2.44)and (2.45)are triviallytrue, with equality for any $\pmb { p }$ satisfying $p ( 0 ) = \pm 1$ Suppose $j > 0$ Let $\pmb { F } _ { j } \pmb { p } = \pmb { a } _ { j }$ .We treat several cases.

(a) $n - j$ even (or zero).

(1) n even.

$$
a _ { j } = F _ { j } p = F _ { i , n } p - F _ { i + 1 , n } p , \qquad i = { \frac { n - j } { 2 } } ,
$$

hence

$$
( - 1 ) ^ { n - 1 } F _ { j } p = ( - 1 ) ^ { n - 1 } F _ { i , n } p + ( - 1 ) ^ { n - ( i + 1 ) } F _ { i + 1 , n } p .
$$

Since $F _ { j } x ^ { k } = 0$ for all odd $k , F _ { j }$ has an even extremal according to Exercise 2.6.2. With $F _ { j }$ restricted to even polynomials (2.39a,b) together

with (2.46) imply that

$$
( - 1 ) ^ { ( n + j ) / 2 } F _ { j } p > 0 , \qquad j = 2 , 4 , \ldots , n ,
$$

provided that ${ a } _ { n } = 1$ and either (i)or (ii)(p.110) holds. Thus we conclude, as before, that $\pm T _ { n }$ is a unique extremal, as $\pm 1$ cannot be extremals, and (2.44) is established.

(2) n odd. An analogous treatment based on (2.40) establishes (2.44).

(b) $\pmb { n } - j$ odd. $F _ { j }$ has an even extremal, if $j$ is even,an odd extremal if $j$ is odd.In either case it has an extremal in $\mathcal { P } _ { n - 1 }$ ,but $F _ { j }$ restricted to $\mathcal { P } _ { n - 1 }$ takes us back to $( a ) _ { : }$ since $\pmb { n } - \pmb { 1 } - j$ is even (or zero), and $\pm T _ { n - 1 }$ are the only possible extremals of $F _ { j }$ in $\mathcal { P } _ { n - 1 }$ .Moreover, in view of Exercise 2.6.3, $\boldsymbol { F } _ { j }$ has a symmetric canonical representation, namely,

$$
F _ { j } p = \sum _ { j = 1 } ^ { n } \alpha _ { j } p ( \eta _ { j - 1 } ^ { ( n - 1 ) } ) ,
$$

and it is unique for $\pmb { p } \in \mathcal { P } _ { { \pmb n } - 1 }$ .Equation (2.47) is also canonical for $\pmb { p } \in \mathcal { P } _ { \pmb { n } }$ ,for, since $x ^ { n }$ is odd for odd $\pmb { n }$ and even for even ${ \pmb n }$ ,the right-hand side of (2.47) is zero when $p = x ^ { n } .$ .In view of Theorems 2.17 and $2 . 1 9 , \pm T _ { n - 1 }$ is the unique extremal if $\pmb { n } > 2$ , whereas for ${ \pmb n } = 2$ one of $\pm T _ { n - 1 }$ is an extremal but there are others.

# 3. The Tau Method.

Let $Q _ { n } = \left\{ p \in \mathcal { P } _ { n } / p ( 0 ) = 1 \right\}$ . We wish to consider the problem of minimizing

$$
\| \pmb { p } - \pmb { p } ^ { \prime } \|
$$

for all $\pmb { p } \in \pmb { Q } _ { \pmb { n } }$ .If we put $\pmb { p } - \pmb { p } ^ { \prime } = \pmb { q } .$ with $q ( x ) = b _ { 0 } + \cdots + b _ { n } x ^ { n }$ and $p ( x ) = a _ { 0 } + \cdots + a _ { n } x ^ { n }$ ,then

$$
a _ { j } = \frac { 1 } { j ! } \sum _ { i = j } ^ { n } i ! b _ { i } , \qquad j = 0 , \ldots , n ,
$$

and the condition $p ( \mathbf { 0 } ) = 1$ ,i.e., $a _ { 0 } = 1$ , is equivalent to

$$
G q = \sum _ { i = 0 } ^ { n } i ! b _ { i } = 1 .
$$

Thus our problem is to minimize $\| q \|$ among all $\pmb q \in \mathcal { P } _ { n }$ that satisfy (2.50). In view of Exercise 2.5.11 it suffces to find an extremal for the linear functional $\pmb { G }$ ,defined in (2.50). Suppose that $n > 1$ (If ${ \pmb n } = { \bf 0 } ;$ ，the original problem is trivial. If $n = 1$ ， $p ( x ) = 1 + \lambda x .$ hence $q ( x ) = 1 + \lambda x - \lambda$ so that $q ( 1 ) = 1$ and $\| q \| \geqslant 1$ ,but,if $0 \leqslant \lambda \leqslant 1$ ， $\| q \| = 1 .$ .Thus any $p ( x ) = 1 + \lambda x , 0 \leqslant \lambda \leqslant 1 _ { \mathrm { ~ \scriptsize ~ . ~ } }$ solves our problem.) We wish to apply Theorem 2.20 to $\pmb { G }$ Neither of $\pm 1$ is extremal for $G _ { : }$ since $G x ^ { n } = n ! > 1$ “We claim that (ii) in Theorem 2.20 also holds. Indeed, we show more. If (for $n \geqslant 1 ) p \in \mathcal { P } _ { n }$ has leading coefficient 1, $\pmb { n }$ real zeros $x _ { 1 } \leqslant x _ { 2 } \leqslant \cdots \leqslant x _ { n } \leqslant 1 _ { \mathrm { : } }$ and $p \neq ( x - 1 ) ^ { n }$ ，then, if $p ( x ) = c _ { 0 } + c _ { 1 } x +$ $\cdots + c _ { n } x ^ { n } $ ，

$$
G _ { j } p = \sum _ { i = j } ^ { n } i ! c _ { i } > 0 , \qquad j = 0 , \dots , n - 1 .
$$

We establish (2.51) by mathematical induction on $\pmb { n } .$ If $n = 1 , p = c _ { 0 } + x$ and $- c _ { 0 } < 1$ , so that $G _ { 0 } p = c _ { 0 } + 1 > 0 ;$ ,and (2.51) is proved. Suppose that (2.51) holds for $\pmb { n }$ and $r _ { n + 1 } \in \mathcal { P } _ { n + 1 }$ satisfies

$$
r _ { n + 1 } ( x ) = ( x - a ) r _ { n } ( x ) ,
$$

where ${ a \leqslant 1 }$ and $r _ { n }$ satisfies the inductive hypothesis.Let $B _ { i } = r _ { n } ^ { ( i ) } ( 0 )$ and $B _ { i } ^ { \prime } = r _ { n + 1 } ^ { ( i ) } ( 0 ) ;$ then

$$
B _ { i } ^ { \prime } = { } - a B _ { i } + i B _ { i - 1 } , \qquad i = 0 , \ldots , n + 1 ,
$$

and if $0 \leqslant j \leqslant n$

$$
G _ { j } r _ { n + 1 } = \sum _ { i = j } ^ { n + 1 } B _ { i } ^ { \prime } = \sum _ { i = j + 1 } ^ { n } S _ { i } + ( 1 - a ) S _ { j } + j S _ { j - 1 } ,
$$

where

$$
S _ { k } = \sum _ { i = k } ^ { n } B _ { i } , \qquad S _ { n + 1 } = 0 .
$$

By the inductive hypothesis $S _ { k } > 0 , k = 0 , . . . , n - 1 ,$ ,and $B _ { n } > 0 ;$ ， since the leading coefficient of $\boldsymbol { r } _ { \pmb { n } }$ is 1; hence $G _ { j } p _ { n + 1 } > 0$ and all is shown.

According to Theorem 2.20, therefore,the unique extremal for $\pmb { G }$ is $\pm T _ { n }$ .If we put

$$
{ \frac { 1 } { \tau _ { n } } } = G T _ { n } = \sum _ { i = 0 } ^ { n } T _ { n } ^ { ( i ) } ( 0 ) ,
$$

then, since $T _ { n }$ has a positive leading coefficient, $G T _ { n } = G _ { 0 } T _ { n } > 0 ;$ ，and the unique extremal for $\pmb { G }$ is $T _ { n }$ . Now Exercise 2.5.11 reveals that the unique solution of our minimum problem is

$$
q _ { n } ( x ) = \tau _ { n } T _ { n } ( x ) ,
$$

or the unique $\pmb { p _ { n } } \in \pmb { Q _ { n } }$ that minimizes (2.48) is obtained from

$$
p _ { n } ( x ) - p _ { n } ^ { \prime } ( x ) = \tau _ { n } T _ { n } ( x ) .
$$

Also

$$
\operatorname* { m i n } _ { p \in Q _ { n } } \| p - p ^ { \prime } \| = \| p _ { n } - p _ { n } ^ { \prime } \| = \tau _ { n } .
$$

Note that in view of(2.51) and (2.49) all the coeffcients of ${ \pmb p } _ { \pmb n }$ are positive. If we put

$$
s _ { k } ( x ) = \sum _ { j = 0 } ^ { k } { \frac { x ^ { j } } { j ! } } ,
$$

i.e., ${ \pmb S } _ { { \pmb k } }$ is the $\pmb { k }$ th partial sum of $e ^ { x }$ ,then $s _ { k } ( x ) - s _ { k } ^ { \prime } ( x ) = x ^ { k } / k !$ and therefore

$$
p _ { n } ( x ) = \frac { \sum _ { k = 0 } ^ { n } T _ { n } ^ { ( k ) } ( 0 ) s _ { k } ( x ) } { \sum _ { k = 0 } ^ { n } T _ { n } ^ { ( k ) } ( 0 ) } = \frac { \sum _ { k = 0 } ^ { n } k ! t _ { k } ^ { ( n ) } s _ { k } ( x ) } { \sum _ { k = 0 } ^ { n } k ! t _ { k } ^ { ( n ) } } .
$$

To see this,observe that the polynomial defined in (2.54) is in $Q _ { n }$ and satisfies (2.53). Thus the solution of our problem turns out to be an “average” of the partial sums of $e ^ { \pmb { x } }$

$y = e ^ { x }$ is the unique solution of $y - y ^ { \prime } = 0 $ $y ( 0 ) = 1$ ，hence minimizing (2.48) seems a reasonable way of obtaining a polynomial approximation to $e ^ { \pmb { x } }$ on I. Indeed, the idea of choosing $\pmb { p }$ to satisfy (2.53) and then choosing $\tau _ { n }$ s0 that $p ( 0 ) = 1$ exemplifies the tau method of Lanczos [1].

Let us go a little further and see how good ${ p } _ { n } ( x )$ is as an approximation of $e ^ { x }$ Consider $\pmb { p _ { n + 1 } ^ { \prime } } = \pmb { u } \in \mathcal { P } _ { n }$ . We shall show that $\pmb { u }$ is “nearly” a best approximation out of $\mathcal { P } _ { \pmb { n } }$ to $e ^ { x }$ ，not only on $\pmb { I }$ but in the closed elliptical domain $\scriptstyle D _ { \rho }$ consisting of the points of the ellipse $c _ { \rho }$ (see Exercise 2.4.8) and the points inside $c _ { \rho }$ ， $\pmb { \rho } \geqslant \pmb { 1 }$ .The reason we approximate by $\pmb { u } = \pmb { p _ { n + 1 } ^ { \prime } }$ rather than ${ \pmb p } _ { \pmb n }$ is that ${ \pmb p } _ { { \pmb n } + 1 } ^ { \prime }$ is close to $\pmb { p _ { n + 1 } }$ ， and so we get the advantage of a polynomial of degree $n + 1$ with a polynomial of degree $\pmb { n }$

If $z \in C _ { \rho } ,$ we solve the linear differential equation (2.53) subject to $p _ { n + 1 } ( 0 ) = 1$ and obtain

$$
e ^ { z } - p _ { n + 1 } ( z ) = \tau _ { n + 1 } e ^ { z } \int _ { 0 } ^ { z } e ^ { - t } T _ { n + 1 } ( t ) d t ,
$$

the path of integration being the line segment joining O and $\pmb { z }$ .Differentiating (2.55) yields

$$
e ^ { z } - u ( z ) = \tau _ { n + 1 } \bigg ( T _ { n + 1 } ( z ) + e ^ { z } \int _ { 0 } ^ { z } e ^ { - t } T _ { n + 1 } ( t ) d t \bigg ) .
$$

Now if $z \in C _ { \rho }$ ,then

$$
| z | \leqslant \frac { \rho + \rho ^ { - 1 } } { 2 } = \lambda
$$

and (cf. Exercise 2.4.11)

$$
| T _ { n + 1 } ( z ) | \leqslant { \frac { \rho ^ { n + 1 } + \rho ^ { - ( n + 1 ) } } { 2 } } .
$$

Also, since $\pmb { \rho } ^ { t } + \pmb { \rho } ^ { - t }$ is a concave increasing function of $\pmb { t }$ for $t > 0 ,$ ,it is not hard to see that, recalling Exercise 1.1.4,

$$
W _ { n + 1 } ( z ) = \int _ { 0 } ^ { z } T _ { n + 1 } ( t ) d t = { \frac { 1 } { 2 } } \left[ { \frac { T _ { n + 2 } ( z ) } { n + 2 } } - { \frac { T _ { n } ( z ) } { n } } \right] + \cos { \frac { n \pi } { 2 } } { \frac { n + 1 } { n ( n + 2 ) } }
$$

satisfies

$$
| W _ { n + 1 } ( z ) | \leqslant \frac { 2 } { n } \frac { \rho ^ { n + 1 } + \rho ^ { - ( n + 1 ) } } { 2 } .
$$

Integrating by parts now yields

$$
\left| e ^ { z } \int _ { 0 } ^ { z } e ^ { - t } T _ { n + 1 } ( t ) d t \right| \leqslant \frac { \beta } { n } \frac { \rho ^ { n + 1 } + \rho ^ { - ( n + 1 ) } } { 2 } ,
$$

where

$$
\beta = 2 ( 1 + \lambda e ^ { 2 \lambda } ) ,
$$

and $\lambda$ is defined in (2.57). Thus for every $z \in D _ { \rho }$

$$
| e ^ { z } - u ( z ) | \leqslant \tau _ { n + 1 } \left( 1 + \frac { \beta } { n } \right) \frac { \rho ^ { n + 1 } + \rho ^ { - ( n + 1 ) } } { 2 } ,
$$

according to the maximum modulus principle.

In Exercise 2.4.8, with $k = n + 1$ ,an extremal signature based on points of $C _ { \rho } , z _ { 0 } , \ldots , z _ { 2 n + 1 } ,$ , is described. Putting $\ z = z _ { i }$ in (2.56) yields

$$
e ^ { z _ { i } } - u ( z _ { i } ) = \tau _ { n + 1 } \Biggl [ ( - 1 ) ^ { i } \frac { \rho ^ { n + 1 } + \rho ^ { - ( n + 1 ) } } { 2 } + e ^ { z _ { i } } \int _ { 0 } ^ { z _ { i } } e ^ { - t } T _ { n + 1 } ( t ) d t \Biggr ] ,
$$

and therefore

$$
; ( e ^ { z _ { i } } - u ( z _ { i } ) ) ( - 1 ) ^ { i } = \tau _ { n + 1 } \Bigg [ \frac { \rho ^ { n + 1 } + \rho ^ { - ( n + 1 ) } } { 2 } + ( - 1 ) ^ { i } \operatorname { R e } e ^ { z _ { i } } \int _ { 0 } ^ { z _ { i } } e ^ { - \tau } T _ { n + 1 } ( t ) d t \Bigg ] ,
$$

but for each $i = 0 , \ldots , 2 n + 1 ,$

$$
\mathbf { R e } e ^ { z _ { i } } \int _ { 0 } ^ { z _ { i } } e ^ { - t } T _ { n + 1 } ( t ) d t \leqslant \left| e ^ { z _ { i } } \int _ { 0 } ^ { z _ { i } } e ^ { - t } T _ { n + 1 } ( t ) d t \right| \leqslant \frac { \beta } { n } \frac { \rho ^ { n + 1 } + \rho ^ { - ( n + 1 ) } } { 2 } ,
$$

in view of (2.58), hence

$$
\operatorname* { m i n } _ { i } \mathrm { \normalfont ~ R e } ( e ^ { z _ { i } } - u ( z _ { i } ) ) ( - 1 ) ^ { i } \geqslant \tau _ { n + 1 } \left( 1 - \frac { \beta } { n } \right) \frac { \rho ^ { n + 1 } + \rho ^ { - ( n + 1 ) } } { 2 } .
$$

Corollary 2.6.2 now implies that

$$
E _ { n } ( e ^ { x } ; D _ { \rho } ) = E _ { n } ( e ^ { x } ; C _ { \rho } ) \geqslant \tau _ { n + 1 } \left( 1 - \frac { \beta } { n } \right) \frac { \rho ^ { n + 1 } + \rho ^ { - ( n + 1 ) } } { 2 } .
$$

Formulae (2.59) and (2.60) reveal that ${ \pmb u } ( z )$ is arbitrarily close to a best approximation for $\pmb { n }$ sufficiently large.

Since

$$
\frac { 1 } { \tau _ { n } } = \sum _ { j = 0 } ^ { [ n / 2 ] } ( n - 2 j ) ! t _ { n - 2 j } ^ { ( n ) }
$$

and the explicit formula for the $t _ { n - 2 j }$ [see (1.96)] yields

$$
( n - 2 j ) ! t _ { n - 2 j } + ( n - 2 ( j + 1 ) ) ! t _ { n - 2 ( j + 1 ) } { \left\{ \begin{array} { l l } { > 0 , } & { \quad j = 0 , 2 , 4 , \dots , } \\ { < 0 , } & { \quad j = 1 , 3 , 5 , \dots , } \end{array} \right. }
$$

we obtain

$$
{ \frac { 1 } { \tau _ { n } } } > n ! t _ { n } + ( n - 2 ) ! t _ { n - 2 } = n ! 2 ^ { n - 3 } \left( 4 - { \frac { 1 } { n - 1 } } \right)
$$

and

$$
{ \frac { 1 } { \tau _ { n } } } < n ! t _ { n } = n ! 2 ^ { n - 1 } .
$$

Thus

$$
\frac { 1 } { ( n + 1 ) ! 2 ^ { n } } < \tau _ { n + 1 } < \frac { 1 } { ( n + 1 ) ! 2 ^ { n } ( 1 - 4 / n ) } .
$$

If the inequality (2.61) is used in (2.59) and (2.60) and we consider the interval $I _ { : }$ ,i.e., $\pmb { \rho } = 1$ ，we obtain

$$
\begin{array} { l } { \displaystyle \frac { 1 } { 2 ^ { n } ( n + 1 ) ! } \bigg [ 1 - \frac { 2 ( 1 + e ^ { 2 } ) } { n } \bigg ] < E _ { n } ( e ^ { x } ; I ) < \displaystyle \frac { 1 } { 2 ^ { n } ( n + 1 ) ! } } \\ { \displaystyle \qquad \times \bigg [ 1 + \frac { 2 ( 1 + e ^ { 2 } ) } { n } \bigg ] \bigg ( \frac { 1 } { 1 - 4 / n + 1 } \bigg ) . } \end{array}
$$

which, for $\pmb { n }$ large enough, is significantly better than Exercise 2.4.34.

# 4. Size of the Derivative. Suppose that

$$
t ( \theta ) = \sum _ { j = 0 } ^ { n } { \bigl ( } a _ { j } \cos j \theta + b _ { j } \sin j \theta { \bigr ) } ,
$$

a trigonometric polynomial of degree ${ \pmb n } _ { \pmb { \imath } }$ satisfies

$$
| t ( \theta _ { j } ) | \leqslant 1 , \qquad j = 1 , \ldots , 2 n ,
$$

where $\theta _ { j } = ( 2 j - 1 ) \pi / 2 n , j = 1 , \ldots , 2 n ,$ then

$$
| t ^ { \prime } ( 0 ) | \leqslant n ,
$$

with equality only if $t = \pm \sin n \theta$

To see this we apply Theorem 2.13 with $V = \mathcal { T } _ { n }$ ,the $( 2 n + 1 )$ -dimensional space consisting of all trigonometric polynomials of degree, at most, $\pmb { n }$ and $F t = t ^ { \prime } ( 0 )$ Let a canonical representation of $\pmb { F }$ be

$$
t ^ { \prime } ( 0 ) = \sum _ { j = 1 } ^ { r } \alpha _ { j } t ( y _ { j } ) ,
$$

$0 \leqslant y _ { j } < 2 \pi .$ ， $r \leqslant 2 n + 1$ If $r < 2 n$ ，then, since there exists (nonzero) $\mathbf { \Delta } t _ { 0 } \in \mathcal { T } _ { n }$ vanishing at $_ { 2 n }$ distinct points of $[ 0 , 2 \pi ) ;$ ,including zero, we have $t _ { 0 } ^ { \prime } ( 0 ) = 0$ and $t _ { 0 }$ has a total of $2 n + 1$ zeros in $[ 0 , 2 \pi ]$ ，a contradiction.Therefore $r \geqslant 2 n$ Thus (see Exercise 2.4.35)， the only possible extremals of $\pmb { F }$ are $\pm 1 _ { ; }$ ， cos $n ( \theta - \theta _ { 0 } )$ But $\pm 1$ are not extremals, since their derivative is zero (hence, incidentally, $r = 2 n ,$ for,if $r = 2 n + 1 , \pm 1$ are the only possible extremals since for no nonconstant $\mathbf { \Delta } _ { t \in \mathcal { T } _ { n } }$ does $| t |$ assume its maximum at $2 n + 1$ distinct points of $[ 0 , 2 \pi ) .$ .If $t = \cos n ( \theta - \theta _ { 0 } ) ;$ then $t ^ { \prime } ( 0 ) = n$ sin ${ \pmb n } \theta _ { 0 } { \dagger }$ hence the only possible extremals are $t = \cos n ( \theta - [ ( 2 i - 1 ) \pi / 2 n ] ) = \pm \sin n \theta .$ Thus in (2.64), $= 2 n , y _ { j } = ( 2 j - 1 ) \pi / 2 n = \theta _ { j }$ ,and (2.63) follows at once.

Next, suppose we fix $\rho , 0 \leqslant \varphi \leqslant 2 \pi$ and put

$$
t _ { \varphi } ( \theta ) = t ( \theta + \varphi ) .
$$

Clearly, $\pmb { t _ { \varphi } \in \mathscr { T } _ { n } }$ ,and if we assume that

$$
| t ( \theta _ { j } + \varphi ) | \leqslant 1 , \qquad j = 1 , \ldots , 2 n ,
$$

then, according to (2.63), we have $| t _ { \varphi } ^ { \prime } ( 0 ) | \leqslant n ,$ i.e.,

$$
| t ^ { \prime } ( \varphi ) | \leqslant n ,
$$

with equality only if $t ( \theta ) = \pm \sin n ( \theta - \varphi )$ . Thus we have shown in particular

that if $\mathbf { \Delta } _ { t \in \mathcal { T } _ { n } }$ and

$$
\| t \| = \operatorname* { m a x } _ { 0 \leqslant \theta \leqslant 2 \pi } | t ( \theta ) | \leqslant 1
$$

then

$$
\| t ^ { \prime } \| \leqslant n ,
$$

with equality only for polynomials of the form $t ( \theta ) = \sin n ( \theta - \varphi ) .$ [The hypothesis (2.67) cannot be replaced by the less stringent (2.62),as the example $t ( \theta ) = \sin n \theta + 2 \cos n \theta$ shows.] This result is known as Bernstein's inequality.

Remark 1. If we consider the linear functional on $\mathcal { T } _ { \pmb { n } }$ ，

$$
G _ { \lambda } t = t ( \theta ) \cos { \lambda } + { \frac { 1 } { n } } t ^ { \prime } ( \theta ) \sin { \lambda } , 0 \leqslant \lambda < 2 \pi ,
$$

and we replace $\pmb { F }$ by $G _ { \lambda }$ in the preceding discussion, mindful of the elementary fact that

$$
\operatorname* { m a x } _ { \lambda } { ( a \cos { \lambda } + b \sin { \lambda } ) } = ( a ^ { 2 } + b ^ { 2 } ) ^ { 1 / 2 } ,
$$

we obtain the following generalization of the Bernstein inequality: if $\| t \| \leqslant 1$ then $n ^ { 2 } t ^ { 2 } ( \theta ) + [ t ^ { \prime } ( \theta ) ] ^ { 2 } \leqslant n ^ { 2 }$ ， $0 \leqslant \theta < 2 \pi$ 、This result was established in van der Corput and Schaake [1], but, as the authors remark in a subsequent correction (see the reference just given), it is a simple consequence of an even more general result of Szego [2].

f $\pmb { p } \in \pmb { B } _ { n }$ then $p ( \cos \theta ) = t ( \theta ) \in \mathcal { T } _ { n } , \| t \| \leqslant$ , it is easy to see that the van der Corput-Schaake result yields

$$
n ^ { 2 } p ^ { 2 } ( x ) + ( 1 - x ^ { 2 } ) ( p ^ { \prime } ( x ) ) ^ { 2 } \leqslant n ^ { 2 } .
$$

In view of (2.18) equality holds only for $p = \pm T _ { n }$

Remark 2. Bernstein's inequality remains valid if the trigonometric polynomial, $t ,$ 、has complex coefficients. For if $\| t \| \leqslant 1$ then $\| e ^ { i \tau } t \| \leqslant 1$ and if $R e e ^ { i \tau } t = t _ { 0 } ,$ then $\| t _ { 0 } \| \leqslant 1$ and $\pmb { t _ { 0 } } \in \mathcal { T } _ { n }$ has real coefficients. Given any $\pmb { \theta _ { 0 } } ,$ $0 \leqslant \theta _ { 0 } < 2 \pi$ ， $\boldsymbol { \tau }$ may be chosen so that $e ^ { i \tau } t ^ { \prime } ( \theta _ { 0 } )$ is real,and hence $| t ^ { \prime } ( \theta _ { 0 } ) |$ $= | t _ { 0 } ^ { \prime } ( \theta _ { 0 } ) | \leqslant n ,$ i.e., $\| t ^ { \prime } \| \leqslant n$

It now follows that if $\pmb { p } \in \mathcal { P } _ { \pmb { n } }$ (with complex coefficients） satisfies, for complex $\pmb { z }$

$$
| p ( z ) | \leqslant 1 , \qquad | z | \leqslant 1 ,
$$

then

$$
| p ^ { \prime } ( z ) | \leqslant n , \qquad | z | \leqslant 1 .
$$

To verify this we need only note that $p ( e ^ { i \theta } )$ is a trigonometric polynomial of degree at most $\pmb { n }$ ,and invoke the maximum modulus principle for the analytic functions $\pmb { p }$ and $\pmb { p } ^ { \prime }$ .Indeed, it suffces to assume only that $| \mathsf { R e } p ( z ) | \leqslant 1$ in $| z | \leqslant 1 ,$ ,to conclude that $\begin{array} { r } { | p ^ { \prime } ( z ) | \leqslant n , | z | \leqslant 1 ; } \end{array}$ ,as we shall see later.

Remark 3. Still another generalization of Bernstein's inequality, due to Zygmund [2], yields

$$
\int _ { 0 } ^ { 2 \pi } \left| \frac { t ^ { \prime } ( \theta ) } { n } \right| ^ { p } d \theta \leqslant \int _ { 0 } ^ { 2 \pi } | t ( \theta ) | ^ { p } d \theta , \qquad t \in \mathcal { T } _ { n } , \qquad p \geqslant 1 ,
$$

with equality only for $t ( \theta ) = A \cos n \theta + B \sin n \theta$ .When $\pmb { p }$ becomes infinite we obtain Bernstein's inequality. Zygmund's inequality has recently been extended to $\pmb { p }$ satisfying $0 \leqslant p < 1 .$ .Details may be found in v. Golitschek and Lorentz [1].

This extension of the range of $\pmb { p }$ was used by Kroó and Saff [1] to extend the result of Exercise 2.4.7. They showed that (using the present notation) for $0 < p < 1$ ，

$$
\int _ { - 1 } ^ { 1 } | \widetilde { T } _ { n } ( x ) | ^ { p } \frac { d x } { \sqrt { 1 - x ^ { 2 } } } \leqslant \int _ { - 1 } ^ { 1 } | q ( x ) | ^ { p } \frac { d x } { \sqrt { 1 - x ^ { 2 } } } ,
$$

for every $q ( x ) = x ^ { n } + a _ { n - 1 } x ^ { n - 1 } + \cdots + a _ { 0 } ,$ with equality only for $q = \widetilde { T } _ { n }$

Proof. Suppose $q \not = \tilde { T } _ { n }$ and $\pmb { p } > \mathbf { 0 } .$ Then

$$
\int _ { - 1 } ^ { 1 } | q ( x ) | ^ { p } { \frac { d x } { \sqrt { 1 - x ^ { 2 } } } } = 2 ^ { ( 1 - n ) p - 1 } \int _ { 0 } ^ { 2 \pi } | \cos n \theta + t _ { n - 1 } ( \theta ) | ^ { p } d \theta ,
$$

where $t _ { n - 1 } ( \theta ) = b _ { 0 } + b _ { 1 } \cos \theta + \cdots + b _ { n - 1 } \cos ( n - 1 ) \theta \not = 0 .$ Repeated application of the extended Zygmund inequality now implies that if

$$
c _ { k } = 2 ^ { ( 1 - n ) p - 1 } \int _ { 0 } ^ { 2 \pi } | { \cos n \theta } + n ^ { - 4 k } t _ { n - 1 } ^ { ( 4 k ) } ( \theta ) | ^ { p } d \theta , \qquad k = 0 , 1 , \ldots ,
$$

then $c _ { 0 } > c _ { 1 }$ and $c _ { k } \geqslant c _ { k + 1 }$ for $k \geqslant 1$ But it is easy to see that $n ^ { - 4 k } t _ { n - 1 } ^ { ( 4 k ) } ( \theta )$ tends to zero uniformly on $[ 0 , 2 \pi ]$ as $k \to \infty$ . Thus the $c _ { k }$ decrease monotonically to

$$
2 ^ { ( 1 - n ) p - 1 } \int _ { 0 } ^ { 2 \pi } | \cos n \theta | ^ { p } d \theta = \int _ { - 1 } ^ { 1 } | \widetilde { T } _ { n } ( x ) | ^ { p } \frac { d x } { \sqrt { 1 - x ^ { 2 } } } ,
$$

and our proof is complete.

Remark 4. If $p ( x ) = a _ { 0 } + \cdots + a _ { n } x ^ { n }$ ，then $t ( \theta ) = p ( \cos \theta ) \in \mathcal { T } _ { n }$ . Thus, if $\pmb { p } \in \pmb { B _ { n } }$ ，then $\| t \| \leqslant 1$ and

$$
| t ^ { \prime } ( \theta ) | = | p ^ { \prime } ( x ) \sin \theta | = | p ^ { \prime } ( x ) ( 1 - x ^ { 2 } ) ^ { 1 / 2 } | \leqslant n
$$

or

$$
| p ^ { \prime } ( x ) | \leqslant { \frac { n } { ( 1 - x ^ { 2 } ) ^ { 1 / 2 } } } , \qquad - 1 < x < 1 .
$$

f $t \in \mathcal { T } _ { n }$ and

$$
\left| t { \binom { i \pi } { n } } \right| \leqslant 1 , \qquad i = 0 , \ldots , 2 n - 1 ,
$$

$t ( \theta + \theta _ { k } )$ satisfies (2.62) and we conclude that

$$
| t ^ { \prime } ( \theta _ { k } ) | \leqslant n , \qquad k = 1 , \ldots , 2 n ,
$$

with equality for any $\pmb { k }$ only if $t = \pm \cos n \theta .$ Thus, if ${ \pmb { p } } \in C _ { \pmb { n } }$ ，

$$
| p ^ { \prime } ( \xi _ { i } ^ { ( n ) } ) | \leqslant \frac { n } { \sqrt { 1 - ( \xi _ { i } ^ { ( n ) } ) ^ { 2 } } } = | T _ { n } ^ { \prime } ( \xi _ { i } ^ { ( n ) } ) | , \qquad i = 1 , \dots , n ,
$$

and equality is possible for any ionly for $p = \pm T _ { n }$ . Hence, we have obtained another proof of Exercise 1.5.8.

Also

$$
\begin{array} { r } { | p ^ { ( k ) } ( u _ { i } ) | \leqslant | T _ { n } ^ { ( k ) } ( u _ { i } ) | , } \end{array}
$$

for $1 \leqslant k < n ,$ where $u _ { 1 } , \ldots , u _ { n - ( k - 1 ) }$ are the zeros of $T _ { n } ^ { ( k - 1 ) }$ ， with equality possible for any i only if $p = \pm T _ { n }$ .(This is Exercise 1.5.9.) We establish this by mathematical induction on $\pmb { k } .$ The case $k = 1$ is just (2.70). Suppose that (2.71) holds. The Lagrange interpolation formula gives

$$
p ^ { ( k ) } ( x ) = \sum _ { i = 1 } ^ { n - ( k - 1 ) } \frac { p ^ { ( k ) } ( u _ { i } ) } { T _ { n } ^ { ( k ) } ( u _ { i } ) } \frac { T _ { n } ^ { ( k - 1 ) } ( x ) } { x - u _ { i } } ;
$$

hence, if $v$ is any zero of $T _ { n } ^ { ( k ) }$

$$
p ^ { ( k + 1 ) } ( v ) = - T _ { n } ^ { ( k - 1 ) } ( v ) \sum _ { i = 1 } ^ { n - ( k - 1 ) } \frac { p ^ { ( k ) } ( u _ { i } ) } { T _ { n } ^ { ( k ) } ( u _ { i } ) } \frac { 1 } { ( v - u _ { i } ) ^ { 2 } } ,
$$