Hence,

$$
[ E _ { k , - 1 } ( f ) ] ^ { 1 / ( k _ { j } - 1 ) } \geq \left( { \frac { \pi } { k _ { j } + 1 } } \right) ^ { 1 / [ 2 ( k _ { j } - 1 ) ] } ( 1 / \rho - \varepsilon ) ^ { k , / ( k _ { j } - 1 ) } .
$$

Now,

$$
\operatorname* { l i m } _ { j \to \infty } \frac { k _ { j } } { k _ { j } - 1 } = 1 \mathrm { ~ a n d ~ } \operatorname* { l i m } _ { j \to \infty } \bigg ( \frac { \pi } { k _ { j } + 1 } \bigg ) ^ { 1 / [ 2 ( k , - 1 ) ] } = 1 .
$$

Therefore

$$
\operatorname* { l i m } _ { n \to \infty } \operatorname* { s u p } _ { } [ E _ { n } ( f ) ] ^ { 1 / n } \geq ( 1 / \rho - \varepsilon ) .
$$

Since ε is arbitrary,

$$
\operatorname* { l i m } _ { n \to \infty } \operatorname* { s u p } _ { } [ E _ { n } ( f ) ] ^ { 1 / n } > 1 / \rho .
$$

Consequently (13.2.1) holds.

A similar theorem can be proved for least square approximation of analytic functions on[-1,1] by polynomials.The same technique of proof is used and is based on Corollary l0.3.6 and Theorem 12.4.7.

THEOREM 13.2.2．Let

$$
{ E _ { n } } ^ { 2 } ( f ) = \operatorname* { m i n } _ { a _ { 1 } } ^ { } \int _ { - 1 } ^ { + 1 } | f ( x ) - a _ { 0 } - a _ { 1 } x - \cdot \cdot \cdot - a _ { n } x ^ { n } | ^ { 2 } d x .
$$

1f $f$ is analytic in $\mathbf { \boldsymbol { \mathcal { E } } } _ { \rho }$ , but not in any $\boldsymbol { \mathcal { E } } _ { \rho } ^ { \rho }$ with $\pmb { \rho } ^ { \prime } > \pmb { \rho }$ then

$$
\operatorname* { l i m } _ { n \to \infty } \operatorname* { s u p } _ { } { [ E _ { n } ( f ) ] ^ { 1 / n } } = 1 / \rho .
$$

Note that the larger $\mathbf { \delta } _ { \mathcal { E } _ { \rho } } ^ { \mathcal { E } }$ is assumed to be,the more rapid is the approximation.

Ex.1. If $f$ is an entire function and $E _ { n } ( f )$ is defined either by (l3.2.1) or (13.2.3), then $\operatorname* { l i m } _ { n \to \infty } { [ E _ { n } ( f ) ] ^ { 1 / n } } = 0$

13.3 Degree of Approximation with Uniform Norm. We begin with an easily established theorem that shows the relationship between smoothness and degree of approximation.

THEOREM 13.3.1. $L e t f ( x ) \in C ^ { p } [ - \pi , \pi ]$ for some $\pmb { \mathscr { p } } \geq 1$ and have period $\mathbf { 2 \pi }$

$$
( f ( - \pi ) = f ( \pi ) , f ^ { \prime } ( - \pi ) = f ^ { \prime } ( \pi ) , \ldots , f ^ { ( p ) } ( - \pi ) = f ^ { ( p ) } ( \pi ) . )
$$

Suppose that $f ^ { ( { p } ) } ( x )$ satisfies a Lipschitz condition of order $\alpha , 0 < \alpha \leq 1$ If $E _ { n } ( f ) = \operatorname* { m i n } _ { { c _ { k } , d _ { k } \ - \pi \le x \le \pi } } \ \left| f ( x ) - \sum _ { k = 0 } ^ { n } c _ { k } \cos k x + d _ { k } \sin k x \right| , t h e n$ $E _ { n } ( f ) \leq { \frac { \mathrm { c o n s t } } { n ^ { p - 1 + \alpha } } } .$ (13.3.1)

Proof: Let $\smash {  { S _ { n } } ( x ) }$ be the nth partial sum of the Fourier expansion of $f$ and $a _ { k } , b _ { k }$ its Fourier coefficients. Then,

$$
E _ { n } ( f ) \leq \operatorname* { m a x } _ { - \pi \leq x \leq \pi } | f ( x ) - S _ { n } ( x ) | = \operatorname* { m a x } _ { - \pi \leq x \leq \pi } \left| \sum _ { k = 1 } ^ { \infty } \cdot \cdot \cdot \right| \leq \sum _ { k = n + 1 } ^ { \infty } \cdot \cdot \cdot \cdot
$$

By Theorem 12.1.4, $| a _ { k } | , | b _ { k } | \leq { \frac { c } { k ^ { p + \alpha } } } \quad k = 1 , 2 , . . . .$

Hence

$$
E _ { n } ( f ) \leq 2 c \sum _ { k = n + 1 } ^ { \infty } { \frac { 1 } { k ^ { p + \alpha } } } < 2 c { \int _ { n } ^ { \infty } { \frac { d x } { x ^ { p + x } } } } < { \frac { \mathrm { c o n s t } } { n ^ { p - 1 + \alpha } } } .
$$

The estimate in (l3.3.l) was obtained by using the partial sums of the Fourier series of $f$ as a comparison function.There is no reason to suppose that these are the most effcient trigonometric polynomials of order $\pmb { n }$ to use,and, indeed,D.Jackson has found that other polynomials lead to a better estimate.

LEMMA 13.3.2． Let $f ( x )$ be periodic on $[ - \pi , \pi ]$ and let $ { \boldsymbol { a } } _ { k } ,  { \boldsymbol { b } } _ { k }$ be its Fourier coefficients. Then, for arbitrary constants $\rho _ { n , k } ,$ ，the linear combination

$$
\sigma _ { n } ( f ; x ) = { \frac { a _ { 0 } } { 2 } } + \sum _ { k = 1 } ^ { n } \rho _ { n , k } ( a _ { k } \cos k x + b _ { k } \sin k x ) ,
$$

can be expressed as

$$
\sigma _ { n } ( f ; x ) = { \frac { 1 } { \pi } } \int _ { - \pi } ^ { \pi } f ( x + t ) K _ { n } ( t ) ~ d t
$$

where the kernel ${ \cal K } _ { n } ( t )$ is given by

$$
K _ { n } ( t ) = \frac { \imath } { 2 } + \sum _ { k = 1 } ^ { n } \rho _ { n , k } \cos k t .
$$

Proof: See the proof of Lemma 12.1.9.

Ex. 1.If $\rho _ { n , k } \equiv 1$ ，then $\sigma _ { n } ( f ; x ) = S _ { n } ( f ; x ) ,$ and

$$
K _ { n } ( t ) = { \frac { 1 } { 2 } } \ + \ \sum _ { k = 1 } ^ { n } \cos k t = { \frac { \sin ( n + { \frac { 1 } { 2 } } ) t } { 2 \sin { \frac { t } { 2 } } } } = \mathrm { t h e \ D i r i c h l e t \ k e r n e l } .
$$

Ex. 2.If pn,k = $\rho _ { n , k } = { \frac { n - k } { n } }$ ，then $\sigma _ { n } ( f ; x )$ are the Fejer sums (Lemma 12.2.2) and ${ \cal K } _ { n } ( t )$ is the Fejer kernel.

LEMMA 13.3.3．If $K _ { n } ( t ) \geq 0$ for $- \pi \leq t \leq \pi$ then

$$
I = \frac { 1 } { \pi } \int _ { - \pi } ^ { \pi } \lvert t \rvert K _ { n } ( t ) d t \le \frac { \pi } { \sqrt { 2 } } \sqrt { 1 - \rho _ { n 1 } } .
$$

Prof: Since ${ \frac { 2 t } { \pi } } \leq \sin t , 0 \leq t \leq { \frac { \pi } { 2 } }$ (draw a graph),

$$
\begin{array} { l } { { \displaystyle I = \frac { 2 } { \pi } \int _ { - \pi } ^ { \pi } \left. \frac { t } { 2 } \right. K _ { n } ( t ) d t \le \int _ { - \pi } ^ { \pi } \sin \left. \frac { t } { 2 } \right. K _ { n } ( t ) d t } } \\ { { \displaystyle \quad \le \left( \int _ { - \pi } ^ { \pi } \sin ^ { 2 } \frac { t } { 2 } K _ { n } ( t ) d t ) \right) ^ { \frac { 1 } { 2 } } \left( \int _ { - \pi } ^ { \pi } K _ { n } ( t ) d t \right) ^ { \frac { 1 } { 2 } } . } } \end{array}
$$

Now,

$$
\int _ { - \pi } ^ { \pi } K _ { n } ( t ) d t = \pi ,
$$

and

$$
\begin{array} { r l r } & { } & { \displaystyle { \int _ { - \pi } ^ { \pi } \sin ^ { 2 } \frac { t } { 2 } K _ { n } ( t ) d t } = \frac { 1 } { 2 } { \int _ { - \pi } ^ { \pi } ( 1 - \cos t ) \bigg ( \frac { 1 } { 2 } + \sum _ { k = 1 } ^ { n } \rho _ { n k } \cos k t \bigg ) } d t } \\ & { } & { \quad \quad = \displaystyle { \frac { 1 } { 2 } \int _ { - \pi } ^ { \pi } \bigg ( \frac { 1 } { 2 } - \rho _ { n 1 } \cos ^ { 2 } t \bigg ) } d t = \frac { \pi } { 2 } ( 1 - \rho _ { n 1 } ) . } \end{array}
$$

Combining this information,we obtain (13.3.5).

LEMMA 13.3.4 (Korovkin).If $K _ { n } ( t ) \geq 0$ and if $f \in C [ - \pi , \pi ]$ and is periodic, then

$$
| \sigma _ { n } ( f ; x ) - f ( x ) | \leq w \bigg ( \frac { 1 } { m } \bigg ) \bigg ( 1 + m \frac { \pi } { \sqrt { \frac { \pi } { 2 } } } \sqrt { 1 - \rho _ { n 1 } } \bigg ) ,
$$

for any integer $m > 0 , w ( \delta )$ is the modulus of continuity of $\pmb { f } ( \pmb { x } )$

$$
\sigma _ { n } ( f ; x ) - f ( x ) = { \frac { 1 } { \pi } } \int _ { - \pi } ^ { \pi } \left\{ f ( x + t ) - f ( x ) \right\} K _ { n } ( t ) d t .
$$

$$
\left| \sigma _ { n } ( f ; x ) - f ( x ) \right| \leq { \frac { 1 } { \pi } } \int _ { - \pi } ^ { \pi } \left| f ( x + t ) - f ( x ) \right| K _ { n } ( t ) d t \leq { \frac { 1 } { \pi } } \int _ { - \pi } ^ { \pi } w ( | t | ) K _ { n } ( t ) d t .
$$

Notice that if $\lambda > 0$ ，

$$
w ( \lambda \delta ) \leq ( \lambda + 1 ) w ( \delta ) .
$$

For set $\pmb { \lambda } = \pmb { n } + \pmb { \theta }$ ，where $\pmb { n }$ is an appropriate integer and $0 \leq \theta < 1$ . Then

$$
\begin{array} { c } { { w ( \lambda \delta ) = w ( n \delta + \theta \delta ) \leq w ( n \delta ) + w ( \theta \delta ) \leq n w ( \delta ) + w ( \delta ) } } \\ { { = ( n + 1 ) w ( \delta ) \leq ( \lambda + 1 ) w ( \delta ) . } } \end{array}
$$

These inequalities follow from (1.4.8)-(1.4.10). Let $\delta = \frac { 1 } { m }$ and $\lambda = m \left| t \right|$ ： then $w ( | t | ) \leq ( m | t | + 1 ) w \biggl ( \frac { 1 } { m } \biggr )$ . Hence,

$$
| \sigma _ { n } ( f ; x ) - f ( x ) | \leq { \frac { 1 } { \pi } } w \left( { \frac { 1 } { m } } \right) \int _ { - \pi } ^ { \pi } ( m | t | + 1 ) K _ { n } ( t ) d t .
$$

Applying (13.3.5), and $\frac { 1 } { \pi } \int _ { - \pi } ^ { \pi } K _ { n } ( t ) d t = 1$ , we obtain (13.3.6).

LEMMA 13.3.5. For ${ \pmb n = 1 , 2 , \dots }$ , we can find kernels ${ \tilde { K } } _ { n } ( t )$ such that

$$
\begin{array} { c } { { \displaystyle \tilde { \cal K } _ { n } ( t ) = \frac 1 2 + \sum _ { k = 1 } ^ { n } \rho _ { n k } \cos k t , } } \\ { { \displaystyle \tilde { \cal K } _ { n } ( t ) \geq 0 ~ - \pi \le t \le \pi , } } \\ { { \displaystyle \rho _ { n 1 } = \cos \frac { \pi } { n + 2 } . } } \end{array}
$$

Proof: For every fixed $\pmb { n } \geq 1$ ,set

where

$$
\tilde { K } _ { n } ( t ) = A _ { n } \ : | a _ { 0 } + a _ { 1 } z + \cdot \cdot \cdot + a _ { n } z ^ { n } | ^ { 2 }
$$

$$
a _ { k } = \sin \frac { ( k + 1 ) \pi } { n + 2 } \qquad k = 0 , 1 , \dots , n ,
$$

$$
A _ { n } = [ 2 ( { a _ { 0 } } ^ { 2 } + { a _ { 1 } } ^ { 2 } + \cdot \cdot \cdot + { a _ { n } } ^ { 2 } ) ] ^ { - 1 } ,
$$

and $z = e ^ { i \theta }$

Property (13.3.9) is obvious.

$$
\begin{array} { l } { { \displaystyle { \xi } _ { n } ( t ) = A _ { n } \sum _ { j = 0 } ^ { n } a _ { j } z ^ { j } \sum _ { j = 0 } ^ { n } a _ { j } z ^ { j } = A _ { n } \sum _ { j , k = 0 } ^ { n } a _ { j } a _ { k } e ^ { i ( j - k ) t } } } \\ { { \displaystyle = A _ { n } \bigg ( \sum _ { j = 0 } ^ { n } a _ { j } a _ { j } + 2 \bigg ( \sum _ { j = 0 } ^ { n - 1 } a _ { j } a _ { j + 1 } \bigg ) \cos { t } + 2 \bigg ( \sum _ { j = 0 } ^ { n - 2 } a _ { j } a _ { j + 2 } \bigg ) \cos { 2 t } + \dots + 2 ( a _ { 0 } a _ { n } ) \cos { n t } \bigg ) } } \end{array}
$$

Hence (l3.3.8) follows by inspection. Finally,observe that

$$
\cos { \frac { \pi } { n + 2 } } \sin { \frac { k \pi } { n + 2 } } = { \frac { 1 } { 2 } } { \Big ( } \sin { \frac { k + 1 } { n + 2 } } \pi + \sin { \frac { k - 1 } { n + 2 } } \pi { \Big ) } ,
$$

or,

$$
a _ { k - 1 } \cos { \frac { \pi } { n + 2 } } = \sharp ( a _ { k - 2 } + a _ { k } ) .
$$

Hence,

$$
\cos \frac { \pi } { n + 2 } a _ { k - 1 } ^ { 2 } = \sharp ( a _ { k - 2 } a _ { k - 1 } + a _ { k - 1 } a _ { k } ) .
$$

Therefore, cos $\frac { \pi } { n + 2 } \sum _ { k = 0 } ^ { n + 1 } a _ { k - 1 } ^ { 2 } = \frac { \imath } { 2 } \sum _ { k = 0 } ^ { n + 1 } \left( a _ { k - 2 } a _ { k - 1 } + a _ { k - 1 } a _ { k } \right)$ . Since

$$
a _ { - 1 } = \sin 0 = a _ { n + 1 } = \sin \frac { n + 2 } { n + 2 } \pi = 0 ,
$$

cos ${ \frac { \pi } { n + 2 } } ( { a _ { 0 } } ^ { 2 } + { a _ { 1 } } ^ { 2 } + \cdot \cdot \cdot + { a _ { n } } ^ { 2 } ) = a _ { 0 } a _ { 1 } + a _ { 1 } a _ { 2 } + \cdot \cdot \cdot + a _ { n - 1 } a _ { n } .$ Now the   
coefficient of cos $\pmb { t }$ in $\tilde { K } _ { n } ( t )$ is $2 A _ { n } ( a _ { 0 } a _ { 1 } + \cdots + a _ { n - 1 } a _ { n } )$ ，and therefore   
(13.3.13) implies (13.3.10).

THEOREM 13.3.6 (Jackson). Let $f ( x ) \in C [ - \pi , \pi ]$ and be periodic. If

$$
E _ { n } ( f ) = \operatorname* { m i n } _ { a _ { k } , b _ { k } } \ \operatorname* { m a x } _ { - \pi \leq x \leq \pi } \lvert f ( x ) - \sum _ { k = 0 } ^ { n } a _ { k } \cos k x + b _ { k } \sin k x \rvert ,
$$

then

$$
E _ { n } ( f ) \leq \left( 1 + { \frac { \pi ^ { 2 } } { 2 } } \right) w \left( { \frac { 1 } { n } } \right) .
$$

$w ( \delta )$ is the modulus of continuity of $f$

Proof: Use the kernels $\smash { \widetilde { K } } _ { n } ( t )$ to form ${ \pmb { \sigma } } _ { n } ( f ; { \pmb x } )$ . Then,

$$
E _ { n } ( f ) \leq \operatorname* { m a x } _ { - \pi \leq x \leq \pi } \left| f ( x ) - \sigma _ { n } ( f ; x ) \right| \leq w { \binom { 1 } { n } } \left( 1 + { \frac { n \pi } { { \sqrt { 2 } } } } { \sqrt { 1 - \cos { \frac { \pi } { n + 2 } } } } \right) .
$$

Now, ${ \sqrt { 1 - \cos { \frac { \pi } { n + 2 } } } } = { \sqrt { 2 } } \sin { \frac { \pi } { 2 ( n + 2 ) } }$ . Since sinx ≤x for0≤𝑥 ≤,

$$
1 + \frac { n \pi } { \sqrt { 2 } } \sqrt { 1 - \cos \frac { \pi } { n + 2 } } \le 1 + \frac { n \pi ^ { 2 } } { 2 n + 4 } \le 1 + \frac { \pi ^ { 2 } } { 2 } .
$$

The study of the degree of approximation to continuous functions by polynomials can be referred to Theorem l3.3.6 by a change of variable.

THEOREM 13.3.7 (Jackson).Let $f ( x ) \in C [ - 1 , 1 ]$ and set

$$
{ E } _ { n } ( f ) = \operatorname* { m i n } _ { a _ { i } } \ \operatorname* { m a x } _ { - 1 \leq x \leq 1 } | f ( x ) - \sum _ { i = 0 } ^ { n } a _ { i } x ^ { i } | .
$$

Then,

$$
E _ { n } ( f ) \leq \left( 1 + { \frac { \pi ^ { 2 } } { 2 } } \right) w \left( { \frac { 1 } { n } } \right)
$$

where $w ( \delta )$ is the modulus of continuity of $f$

Proof:Set $g ( x ) = f ( \cos x )$ . Then $\pmb { g }$ is continuous,periodic,and even in $[ - \pi , \pi ]$ Using $\smash { \widetilde { K } } _ { n } ( t )$ ,form ${ \pmb { \sigma } } _ { n } ( f ; { \pmb x } )$ . By (13.3.4),

$$
\sigma _ { n } ( g ; x ) = { \frac { a _ { 0 } } { 2 } } + \sum _ { k = 1 } ^ { n } \rho _ { n , k } a _ { k } \cos k x ,
$$

where $\pmb { a } _ { k }$ are the Fourier coefficients of ${ \pmb g } ( { \pmb x } )$ .From the proof of Theorem 13.3.6,

$$
\operatorname* { m a x } _ { - \pi \leq x \leq \pi } | g ( x ) - \sigma _ { n } ( g ; x ) | \leq { \biggl ( } 1 + { \frac { \pi ^ { 2 } } { 2 } } { \biggr ) } w { \biggl ( } { \frac { 1 } { n } } ; g { \biggr ) } .
$$

Now,

$$
w ( \delta ; g ) = \operatorname* { m a x } _ { | x - x _ { 2 } | \leq \delta } | g ( x _ { 1 } ) - g ( x _ { 2 } ) | = \operatorname* { m a x } _ { | x _ { 1 } - x _ { 2 } | \leq \delta } | f ( \cos x _ { 1 } ) - f ( \cos x _ { 2 } ) | .
$$

Since

$$
\left| { \frac { d } { d x } } \cos x \right| \leq 1 , | \cos x _ { 1 } - \cos x _ { 2 } | \leq | x _ { 1 } - x _ { 2 } | .
$$

Hence,

$$
\operatorname* { m a x } _ { | x _ { 1 } - x _ { 2 } | \leq \delta } \bigl | f ( \cos x _ { 1 } ) - f ( \cos x _ { 2 } ) \bigr | \leq \operatorname* { m a x } _ { | x _ { 1 } - x _ { 2 } | \leq \delta } \bigl | f ( x _ { 1 } ) - f ( x _ { 2 } ) \bigr | = w ( \delta ; f ) .
$$

Therefore,

$$
\operatorname* { m a x } _ { - \pi \leq x \leq \pi } \left| f ( \cos x ) - { \frac { a _ { 0 } } { 2 } } - \sum _ { k = 1 } ^ { n } \rho _ { n k } \cos k x \right| \leq { \biggl ( } 1 + { \frac { \pi ^ { 2 } } { 2 } } { \biggr ) } w { \biggl ( } { \frac { 1 } { n } } ; f { \biggr ) } .
$$

Setting $y = \cos x ,$

$$
\operatorname* { m a x } _ { - 1 \leq y \leq 1 } \left. f ( y ) - \frac { a _ { 0 } } { 2 } - \sum _ { k = 1 } ^ { n } \rho _ { n k } \cos \left( k \mathrm { a r c } \cos y \right) \right. \leq \bigg ( 1 + \frac { \pi ^ { 2 } } { 2 } \bigg ) w \bigg ( \frac { 1 } { n } ; f \bigg ) .
$$

Since cos $( k \operatorname { a r c } \cos y ) = T _ { k } ( y )$

$$
p _ { n } ( y ) = \frac { a _ { 0 } } { 2 } + \sum _ { k = 1 } ^ { n } \rho _ { n k } \cos { ( k \operatorname { a r c } \cos y ) } \in \mathcal { P } _ { n } .
$$

Hence,

$$
E _ { n } ( f ) \leq \operatorname* { m a x } _ { - 1 \leq y \leq 1 } \lvert f ( y ) - p _ { n } ( y ) \rvert \leq \left( 1 + { \frac { \pi ^ { 2 } } { 2 } } \right) w \left( { \frac { 1 } { n } } \right) .
$$

# NOTES ON CHAPTER XIII

13.1 Tieman [1] pp.50-55.

13.2-13.3 Much is known about the degree of approximation. For analytic functions,consult Walsh [2],[3]. For real functions,Jackson [1],Bernstein [1],Natanson [l],Tieman [1],Korovkin [2],Alexits[1], Zygmund[1], vol. I.

# PROBLEMS

1. Let theradius of convergence of $f ( z ) = \sum _ { n = 0 } ^ { \infty } a _ { n } z ^ { n }$ be $\scriptstyle { \mathcal { R } }$ .Set $S _ { n } ( z ) = \sum _ { k = 0 } ^ { n } a _ { k } z ^ { k } ,$ Show that

$$
\operatorname* { l i m } _ { n \to \infty } \operatorname* { s u p } _ { \bf { \sigma } } \left[ \operatorname* { m a x } _ { | z | \leq r } \left| f ( z ) - S _ { n } ( z ) \right| \right] ^ { 1 / n } = \frac { r } { R } , \mathrm { ~ f o r ~ } r < R
$$

and

$$
\operatorname* { l i m } _ { n \to \infty } \operatorname* { s u p } _ { \mathbf { \alpha } | z | \leq r } \big | \operatorname* { s u p } _ { z } | z | \big | ^ { 1 / n } = \frac { r } { R } , \mathrm { f o r } r \geq R .
$$

2.Let $\pmb { \rho }$ be a fixed number ${ > } 1$ ,and let $x$ be the space of functions that are analytic in $| z | < \pmb { \rho }$ For $f \in X$ set $\| f \| ^ { 2 } = \iint _ { | z | \leq 1 } \left| f ( z ) \right| ^ { 2 } d x d y$ Show that $x$ is not complete.

3. Discuss the degree of approximation of a periodic analytic function by its Fourier series.

4. Discuss the rapidity of convergence in $L ^ { 2 } ( \mathcal { E } _ { \rho } )$ of the best polynomial approximants to functions that are analytic in $\theta _ { \rho ^ { ' } } \quad \rho ^ { \prime } > \rho$

5.The kernel

$$
K _ { n } ( t ) = { \frac { 3 } { 2 n ( 2 n ^ { 2 } + 1 ) } } { \left( { \frac { \sin { \frac { n t } { 2 } } } { \sin { \frac { t } { 2 } } } } \right) } ^ { 4 }
$$

is known as Jackson's kernel. Show that

$$
\left( { \frac { \sin { \frac { n t } { 2 } } } { \sin { \frac { t } { 2 } } } } \right) ^ { 2 } = n + 2 [ ( n - 1 ) \cos t + ( n - 2 ) \cos 2 t + \cdot \cdot \cdot + \cos ( n - 1 ) t ]
$$

and hence that

$$
K _ { n } ( t ) = { \frac { 1 } { 2 } } + \sum _ { k = 1 } ^ { 2 n - 2 } \rho _ { 2 n - 2 , k } \cos k t \quad { \mathrm { w h e r e } } \quad \rho _ { 2 n - 2 , 1 } = 1 - { \frac { 3 } { 2 n ^ { 2 } } } .
$$

6. Show that Jackson's kernel is of Fejér's type on $\left[ - \pi , \pi \right]$ . (See 12.2.)

# CHAPTER XIV

# Approximation of Linear Functionals

14.1 Rules and Their Determination. Numerical analysis has given rise to many approximate formulas for interpolation,extrapolation,differentiation,and integration.These formulas,frequently called“rules,”are not only of practical importance,but very frequently have an unusual interest in their own right.Integrals,derivatives at a point,etc.,are linear functionals defined over appropriate linear spaces of functions,and the problem of rule formation is equivalent to the approximation of these functionals by linear combinations of prescribed linear functionals.

$$
\int _ { a } ^ { a + 2 h } f ( x ) d x \approx { \frac { h } { 3 } } \left[ f ( a ) + 4 f ( a + h ) + f ( a + 2 h ) \right]
$$

Ex. 2. $f ( a ) \approx \frac { 1 } { 2 } [ f ( a - h ) + f ( a + h ) ]$ (Linear Interpolation).

Ex. 3. $f ( a \mathrm { ~ + ~ } h ) \approx f ( a ) + \frac { h } { 2 } [ f ^ { \prime } ( a ) + f ^ { \prime } ( a \mathrm { ~ + ~ } h ) ]$ (Trapezoidal Rule for Diferential Equations).

In general, the prescribed linear functionals are values of a function at a point.Occasionally,as in Ex. 3,derivatives are employed. Integrals over subintervals have not been used to any extent as approximating linear functionals,but they，too,are possible,and might conceivably become important.

Two roads may be taken to develop rules:(a) The method of interpolation and (b) The method of approximation.Let $L _ { 1 } , L _ { 2 } , \ldots , L _ { n }$ be $\pmb { n }$ prescribed “elementary” linear functionals.It is desired to approximate a given linear functional $\pmb { L }$ by linear combinations of the $\pmb { L _ { i } }$ ：

$$
L \approx a _ { 1 } L _ { 1 } + a _ { 2 } L _ { 2 } + \cdots + a _ { n } L _ { n } .
$$

The remainder or error

$$
E = L - ( a _ { 1 } L _ { 1 } + \cdot \cdot \cdot + a _ { n } L _ { n } )
$$

is itself a linear functional. (Note that in this chapter,the symbols ${ \cal E } , { \cal E } _ { n }$ will be used with a different meaning than in Chapters 7,l3.) The method of interpolation selects constants $\pmb { a _ { i } }$ in such a way that $\pmb { \cal E }$ vanishes on $\pmb { n }$

prescribed elements ${ \pmb x } _ { 1 } , \ldots , { \pmb x } _ { n }$

$$
E ( x _ { i } ) = 0 \qquad i = 1 , 2 , \ldots , n .
$$

We may say that the constants $\pmb { a } _ { i }$ are determined so that $\pmb { \cal E }$ is orthogonal to $x _ { 1 } , \ldots , x _ { n }$ ，The theory of this method has been discussed extensively in 2.2.

Ex.4. The rules of Ex.1, Ex. 2, Ex. 3 are exact for $\mathcal { P } _ { 3 } , \mathcal { P } _ { 1 } ,$ and $\mathcal { P } _ { \mathfrak { Z } }$ respectively.

Method (a) has had a long history and by far the bulk of the approximate formulas of numerical analysis are of this type.The method of approximation (b) is a recent one and has certain advantages and disadvantages over (a).Here we assume that we are dealing with a normed linear space $\pmb { X }$ of functions and that the functionals in question $L , L _ { i } .$ ，belong to the normed conjugate space $x ^ { * }$ .We wish then to determine constants $\pmb { a } _ { i }$ such that

$$
\| L - ( a _ { 1 } L _ { 1 } + a _ { 2 } L _ { 2 } + \cdot \cdot \cdot + a _ { n } L _ { n } ) \| = \mathrm { m i n i m u m } .
$$

In the case where $\pmb { X }$ is a Hilbert space so that $\pmb { X }$ and $X ^ { * }$ are essentially the same (Theorem 9.3.9) the problem of approximation of functionals can be handled by orthogonalization methods.We therefore note:

THEOREM 14.1.1. The problem (14.1.4) possesses a solution.

Proof:Apply Theorem 7.4.1 to $x ^ { * }$

THEOREM 14.1.2． Let $\pmb { H }$ be a Hilbert space and $L , L _ { 1 } , \ldots , L _ { n }$ be bounded linear functionals， the last $\pmb { n }$ assumed independent. Let be their representers

14.2 The Gauss-Jacobi Theory of Approximate Integration. One of the finest examples of rules of interpolatory type is that of Gauss-Jacobi. Here the approximating linear functionals are not prescribed in advance, but the problem is to determiine them so that the rule will be exact for polynomials of maximal degree.Let $w ( x ) > 0$ be a weight function defined on $[ a , b ]$ .If $\pmb { n }$ distinct points $x _ { 1 } , \ldots , x _ { n }$ are specified in advance, then we know that we can find coefficients $w _ { 1 } , \ldots , w _ { n }$ such that the rule

$$
L ( f ) = \int _ { a } ^ { b } w ( x ) f ( x ) d x \approx \sum _ { k = 1 } ^ { n } w _ { k } f ( x _ { k } )
$$

will be exact for $\mathcal { P } _ { n - 1 }$ . If we treat both the $\pmb { x } _ { k }$ and the $w _ { k }$ as ${ \bf 2 } n$ unknowns, then,perhaps,we can arrange matters in such a way that the rule will be exact for $\mathscr { P } _ { 2 n - 1 }$ ,(i.e.,linear combinations of the ${ \bf 2 } n$ powers $1 , x , x ^ { 2 } , \dotsc , x ^ { 2 n - 1 } )$ For such a rule to have practical importance,the points $\pmb { x _ { i } }$ must lie in the interval $[ a , b ]$ ，although for analytic functions,this condition could be waived.

This is indeed possible as was found by Gauss and generalized by Jacobi. The solution exhibits a surprising relation to the orthogonal polynomials generated by the weight ${ w } ( { \pmb x } )$

THEOREM 14.2.1 (Gauss-Jacobi)． Let ${ \boldsymbol { w } } ( { \boldsymbol { x } } ) > 0$ be $\pmb { a }$ weight function defined on $[ a , b ]$ with corresponding orthogonal polynomials ${ \pmb p } _ { \pmb n } ( { \pmb x } )$ ， $\pmb { n } \geq 1$ Let the zeros of ${ \pmb p } _ { \pmb n } ( \pmb x )$ be $a < x _ { 1 } < x _ { 2 } < \cdot \cdot \cdot < x _ { n } < b$ .Then,we can find positive constants $w _ { 1 } , w _ { 2 } , \ldots , w _ { n }$ such that

$$
\int _ { a } ^ { b } w ( x ) p ( x ) d x = \sum _ { k = 1 } ^ { n } w _ { k } p ( x _ { k } )
$$

whenever $\pmb { p } ( x ) \in \mathcal { P } _ { 2 n - 1 }$

Proof: Given a $p ( x )$ as above. Let $q ( x ) \in \mathcal P _ { n - 1 }$ take on the values of ${ \pmb p } ( { \pmb x } )$ at $x _ { 1 } , \ldots , x _ { n }$ .We can write it in the Lagrange form

$$
q ( x ) = \sum _ { k = 1 } ^ { n } p ( x _ { k } ) \ell _ { k } ( x ) , \ell _ { k } ( x ) = { \frac { w ( x ) } { ( x - x _ { k } ) w ^ { \prime } ( x _ { k } ) } } , w ( x ) = \prod _ { k = 1 } ^ { n } ( x - x _ { k } ) .
$$

The polynomial $p ( x ) - q ( x )$ therefore has zeros at $x _ { 1 } , \ldots , x _ { n }$ and consequently $p ( x ) - q ( x ) = p _ { n } ( x ) r _ { n - 1 } ( x )$ for some polynomial $r _ { n - 1 } ( x ) \in \mathcal { P } _ { n - 1 }$ Therefore,in view of the orthogonality of ${ \pmb p } _ { n } ( { \pmb x } )$ to polynomials of lower degree,

$$
\begin{array} { r l r } {  { \int _ { a } ^ { b } w ( x ) p ( x ) d x = \int _ { a } ^ { b } w ( x ) [ q ( x ) + p _ { n } ( x ) r _ { n - 1 } ( x ) ] d x = \int _ { a } ^ { b } w ( x ) q ( x ) d x } } \\ & { } & { = \int _ { a } ^ { b } w ( x ) \sum _ { k = 1 } ^ { n } p ( x _ { k } ) \ell _ { k } ( x ) d x = \displaystyle \sum _ { k = 1 } ^ { n } \{ \int _ { a } ^ { b } w ( x ) \ell _ { k } ( x ) d x \} p ( x _ { k } ) . } \end{array}
$$

If we set

$$
w _ { k } = \int _ { a } ^ { b } w ( x ) \ell _ { k } ( x ) d x
$$

then the identity (14.2.2) holds. Now $\ell _ { k } ( x ) \in \mathcal P _ { n - 1 }$ and vanishes at $x _ { 1 } , \ldots ,$ $x _ { k - 1 } , x _ { k + 1 } , \ldots , x _ { n }$ .Therefore $( \ell _ { k } ( x ) ) ^ { 2 } \in \mathcal P _ { 2 n - 2 }$ and vanishes at these same points.Moreover $\ell _ { k } ( x _ { k } ) = 1$ .Hence,

$$
w _ { k } = \sum _ { j = 1 } ^ { n } w _ { j } ( \ell _ { k } ( x _ { j } ) ) ^ { 2 } = \int _ { a } ^ { b } w ( x ) [ \ell _ { k } ( x ) ] ^ { 2 } d x > 0 .
$$

The abscissas $x _ { i }$ are the zeros of certain polynomials,and are generally irrational numbers.If computing is done by hand,it is a nuisance to deal with many digits, and so in years gone by the Gauss rule was not popular. High speed digital computers,on the other hand,do not distinguish between “simple”numbers such as .50ooooooo and more“complicated’ones such as .577350269. The Gauss rules，which are excellent for large classes of functions arising in practise,have therefore been rehabilitated in the eyes of computers and are much employed.

The following remainder theorem holds for the Gauss-Jacobi rule.

THEOREM 14.2.2 (A． Markoff).Let ${ w } ( { \pmb x } )$ and $x _ { 1 } , \ldots , x _ { n }$ be as in the previous theorem. Let $f ( x ) \in C ^ { 2 n } [ a , b ]$ . Then,

$$
E _ { n } ( f ) = \int _ { a } ^ { b } w ( x ) f ( x ) d x - \sum _ { k = 1 } ^ { n } w _ { k } f ( x _ { k } ) = { \frac { f ^ { ( 2 n ) } ( \eta ) } { ( 2 n ) ! { k _ { n } } ^ { 2 } } } ,
$$

where $k _ { n }$ is the leading coefficient of the orthonormal polynomial ${ p _ { n } } ^ { * } ( x )$ associated with ${ w } ( { \pmb x } )$ ,and where $a < \eta < b$

Proof:The device here is to employ Hermite interpolation with each abscissa repeated once. Let $h _ { 2 n - 1 } ( x )$ be that polynomial of $\mathscr { P } _ { 2 n - 1 }$ for which $h _ { 2 n - 1 } ( x _ { k } ) = f ( x _ { k } ) , h _ { 2 n - 1 } ^ { \prime } ( x _ { k } ) = f ^ { \prime } ( x _ { k } ) , k = 1 , 2 , . . . , n _ { \mathrm { + } }$ Then according to Theorem 3.5.1,we have

$$
f ( x ) = h _ { 2 n - 1 } ( x ) + { \frac { f ^ { ( 2 n ) } ( \xi ( x ) ) } { ( 2 n ) ! } } ( x - x _ { 1 } ) ^ { 2 } ( x - x _ { 2 } ) ^ { 2 } \cdot \cdot \cdot ( x - x _ { n } ) ^ { 2 }
$$

for $a \leq x \leq b$ and $a < \xi ( x ) < b$ .Notice that by Theorem l.6.6 applied to $f ( x ) - h _ { 2 n - 1 } ( x ) , { \frac { f ( x ) - h _ { 2 n - 1 } ( x ) } { ( x - x _ { 1 } ) ^ { 2 } \cdot \cdot \cdot ( x - x _ { n } ) ^ { 2 } } } \in C [ a , b ]$ and hence $f ^ { ( 2 n ) } ( { \pmb \xi } ( { \pmb x } ) )$ is also continuous.Multiply (l4.2.5) by ${ w } ( { \pmb x } )$ ：

$$
w ( x ) f ( x ) = w ( x ) h _ { 2 n - 1 } ( x ) + { \frac { f ^ { ( 2 n ) } ( \xi ( x ) ) } { ( 2 n ) ! } } w ( x ) { \frac { [ { n _ { n } } ^ { * } ( x ) ] ^ { 2 } } { { k _ { n } } ^ { 2 } } }
$$

where ${ p _ { n } } ^ { * } ( x )$ is the orthonormal polynomial of degree $\pmb { n }$ associated with $w ( x )$ . Integrate (l4.2.6),and employ the mean value theorem for integrals:

$$
\begin{array} { l } { { \displaystyle \int _ { a } ^ { b } w ( x ) f ( x ) d x = \int _ { a } ^ { b } w ( x ) h _ { 2 n - 1 } ( x ) d x + \frac { 1 } { ( 2 n ) ! ~ k _ { n } ^ { ~ 2 } } \int _ { a } ^ { b } f ^ { ( 2 n ) } ( \xi ( x ) ) w ( x ) [ p _ { n } { } ^ { * } ( x ) ] ^ { 2 } d x } } \\ { { \displaystyle \qquad = \int _ { a } ^ { b } w ( x ) h _ { 2 n - 1 } ( x ) d x + \frac { f ^ { ( 2 n ) } ( \eta ) } { ( 2 n ) ! ~ k _ { n } ^ { ~ 2 } } \int _ { a } ^ { b } w ( x ) [ p _ { n } { } ^ { * } ( x ) ] ^ { 2 } d x } } \\ { { \displaystyle \qquad = \sum _ { k = 1 } ^ { n } w _ { k } f ( x _ { k } ) + \frac { f ^ { ( 2 n ) } ( \eta ) } { ( 2 n ) ! ~ k _ { n } ^ { ~ 2 } } . } } \end{array}
$$

COROLLARY 14.2.3. For the Jacobi weight $w ( x ) = ( 1 - x ) ^ { \alpha } ( 1 + x ) ^ { \beta }$ ， $\alpha > - 1 , \beta > - 1$ ,and for $f ( x ) \in C ^ { 2 n } [ - 1 , 1 ]$ ,then

$$
\Sigma _ { n } ( f ) = \frac { 2 ^ { 2 n + \alpha + \beta + 1 } \Gamma ( n + \alpha + 1 ) \Gamma ( n + \beta + 1 ) \Gamma ( n + \alpha + \beta + 1 ) n ! f ^ { ( 2 n ) } ( \eta ) } { \Gamma ( 2 n + \alpha + \beta + 1 ) \Gamma ( 2 n + \alpha + \beta + 2 ) ( 2 n ) ! }
$$

For $\alpha = \beta = 0$ ,this reduces to

$$
E _ { n } ( f ) = \frac { 2 ^ { 2 n + 1 } ( n ! ) ^ { 4 } } { ( 2 n + 1 ) [ ( 2 n ) ! ] ^ { 3 } } f ^ { ( 2 n ) } ( \eta ) .
$$

14.3 Norms of Functionals as Error Estimates. Let $\pmb { X }$ bea normed linear space and $\pmb { L }$ a bounded linear functional defined on $\pmb { X }$ . Then, as in (9.3.2),

$$
| L ( x ) | \leq \| L \| \ \| x \| , x \in X .
$$

$\| \pmb { L } \|$ is independent of $_ { x }$ .This fundamental inequality may be made the basis of error estimates for the linear rules of numerical analysis.Let $L$ be a given functional and let a rule $\pmb { R }$ be an approximation to $\pmb { L }$ Then construct the error

$$
{ \pmb E } = { \pmb L } - { \pmb R } .
$$

The smaller the norm $\| E \| = \| L - R \|$ ,the better the approximation of $\pmb { R }$ to $L$

Ex.1.Let $x$ be the linear space of continuous functions on $[ a , b ]$ that have a bounded， piecewise continuous derivative.Let $\| f \| = \operatorname* { s u p } _ { a \leq x \leq b } | f ^ { \prime } ( x ) | + | f ( a ) |$ Then $\boldsymbol { x }$ is a normed linear space. If $\pmb { K } ( \pmb { x } )$ is a bounded,piecewise continuous function on $[ a , b ]$ ，then $L ( f ) = \int _ { a } ^ { b } f ^ { \prime } ( x ) K ( x ) d x$ is a bounded linear functional b cm $x$ ${ \big | } L ( f ) { \big | } \leq \operatorname* { s u p } _ { a \leq x \leq b } { \big | } { \sqrt { f ^ { \prime } ( x ) } } { \big | } \int _ { a } ^ { \upsilon } { \big | } K ( x ) { \big | } d x \leq \| f \| \int _ { a } ^ { \upsilon } { \big | } K ( x ) { \big | } d x ,$ $\| L \| \leq \int _ { a } ^ { b } { \bigl | } K ( x ) { \bigr | } d x$ $\kappa ( x )$ and piecewise continuous in $[ a , b ]$ .Hence the function $g ( x ) \ = \int _ { a } ^ { x } \operatorname { s g n } K ( t ) \ d t$ is in $x$ and $g ( a ) = 0$ Also $L ( g ) \ = \int _ { a } ^ { b } ( \operatorname { s g n } K ( x ) ) K ( x ) \ d x \ = \int _ { a } ^ { b } { \bigl | } K ( x ) { \bigr | } \ d x$ If $\pmb { K } ( \pmb { x } ) \neq \pmb { 0 }$ $\| g \| _ { \ r { \hat { \mathbf { \Gamma } } } ^ { h } } = \operatorname* { s u p } _ { a \leq x \leq b } { \big | } \operatorname { s g n } K ( x ) { \big | } = 1$ ${ \big | } L ( g ) { \big | } = \| g \| \int _ { a } ^ { b } { \big | } K ( x ) { \big | } d x$ Threoe $\| L \| \geq \int _ { a } ^ { b } { \bigl | } K ( x ) { \bigr | } d x$ $\| L \| = \int _ { a } ^ { b } { \bigl | } K ( x ) { \bigr | } d x$

As a specific instance,the error in the trapezoidal rule (cf.Ex.4,3.7) is given by

$$
\begin{array} { l } { \displaystyle { E ( f ) = \int _ { a } ^ { b } f ( x ) d x - \frac { b - a } { n } \biggl [ \frac { f ( a ) } { 2 } + f ( a + \sigma ) + f ( a + 2 \sigma ) + \cdots } } \\ { { \mathrm { } + f ( a + ( n - 1 ) \sigma ) + \frac { f ( b ) } { 2 } \biggr ] , \sigma = \frac { b - a } { n } . } } \end{array}
$$

Therefore (cf.(3.7.21)),

$$
E ( f ) \ = \ - \sum _ { k = 0 } ^ { n - 1 } \int _ { a + k \sigma } ^ { a + ( k + 1 ) \sigma } ( t - ( a + ( k + \textstyle \frac { 1 } { 2 } ) \sigma ) ) f ^ { \prime } ( t ) \ d t .
$$

Hence,by the above work,

$$
\left\| E \right\| \ = \sum _ { k = 0 } ^ { n - 1 } \int _ { a + k \sigma } ^ { a + ( k + 1 ) \sigma } \left| t - ( a + ( k + \textstyle { \frac { 1 } { 2 } } ) \sigma ) \right| d t = \frac { n \sigma ^ { 2 } } { 4 } = \frac { ( b - a ) ^ { 2 } } { 4 n } .
$$

Therefore, $\left| E ( f ) \right| \leq { \frac { \left\| f \right\| ( b - a ) ^ { 2 } } { 4 n } } ,$

Ex.2.In the space $L ^ { 2 } ( B )$ where $\pmb { B }$ is the unit circle,consider the interpolation formula $f ( 0 ) \approx \frac { } { 2 } ( f ( h ) + f ( - h ) )$ ，where $0 < h < 1$ .Set

$$
E ( f ) = f ( 0 ) - { \textstyle \frac { 1 } { 2 } } ( f ( h ) + f ( - h ) ) .
$$

By Corollary 12.5.5, $\pmb { { \cal E } }$ is bounded over $L ^ { 2 } ( B )$ .From Corollary 12.6.7,

and from (12.6.17),

$$
\| E \| ^ { 2 } = E _ { w } \overline { { E _ { z } K ( z , w ) } } ,
$$

$$
K ( z , w ) = \frac { 1 } { \pi ( 1 - z \bar { w } ) ^ { 2 } } .
$$

Hence,

$$
E _ { z } K ( z , w ) = \frac { 1 } { \pi } - \frac { 1 } { 2 \pi } \biggl [ \frac { 1 } { ( 1 - h \bar { w } ) ^ { 2 } } + \frac { 1 } { ( 1 + h \bar { w } ) ^ { 2 } } \biggr ] = \frac { 1 } { \pi } \biggl [ \frac { - 3 h ^ { 2 } \bar { w } ^ { 2 } + h ^ { 4 } \bar { w } ^ { 4 } } { ( 1 - h ^ { 2 } \bar { w } ^ { 2 } ) ^ { 2 } } \biggr ] ,
$$

and

$$
\| E \| ^ { 2 } = \frac { 1 } { \pi } \biggl [ \frac { 3 h ^ { 4 } - h ^ { 8 } } { ( 1 - h ^ { 4 } ) ^ { 2 } } \biggr ] .
$$

Therefore,

$$
\| E \| = \frac { h ^ { 2 } } { \mathcal { V } _ { \pi } ^ { 2 } } \frac { \sqrt { 3 - h ^ { 4 } } } { ( 1 - h ^ { 4 } ) } .
$$

Hence,

$$
\left| E ( f ) \right| \leq { \frac { h ^ { 2 } } { \surd \frac { 2 } { \pi } } } { \frac { \sqrt { 3 - h ^ { 4 } } } { ( 1 - h ^ { 4 } ) } } { \Biggl [ } \iint \left| f ( z ) \right| ^ { 2 } d x d y { \Biggr ] } ^ { \frac { 1 } { 2 } } .
$$

Note that as $h  0$ ， $\| E \| \sim \sqrt { \frac { 3 } { \pi } } h ^ { 2 }$ As $h  1 ^ { - }$ $\| E \| \to \infty$ . This retg he fat that $f ( 0 ) \ - \ { \textstyle { \frac { 1 } { 2 } } } ( f ( 1 ) + f ( - 1 ) )$ is not bounded over $L ^ { 2 } ( B )$

Ex.3.Let $\boldsymbol { \mathcal { E } } _ { \rho }$ be the ellipse of Def.1.13.1.Let $E$ be a bounded linear functional over $L ^ { 2 } ( \hat { \mathcal { E } } _ { \rho } )$ and suppose that $E ( 1 ) = E ( z ) = { \textrm { \cdot } } \cdot \cdot = E ( z ^ { n } ) = 0$ From (12.6.18),

$$
\| E \| ^ { 2 } = \frac { 4 } { \pi } \sum _ { k = n + 1 } ^ { \infty } ( k + 1 ) \frac { | E ( U _ { k } ) | ^ { 2 } } { \rho ^ { 2 k + 2 } - \rho ^ { - 2 k - 2 } } .
$$

As concrete examples,the following values may be cited. Select the ellipse ${ \mathcal { E } } _ { \rho }$ with $a = 2 , b = \sqrt { 3 } , \rho = 3 . 7 3 2$ Approximate integration over[--1,1] is considered.

$$
\begin{array} { c c } { { R u l e } } & { { n } } \\ { { \mathrm { T r a p e z o i d a l } } } & { { 1 } } \\ { { \mathrm { S i m p s o n } } } & { { 3 } } \\ { { \mathrm { G a u s s ~ 7 ~ p o i n t } } } & { { 1 3 } } \\ { { \mathrm { G a u s s ~ 1 0 ~ p o i n t } } } & { { 1 9 } } \\ { { \mathrm { G a u s s ~ 1 6 ~ p o i n t } } } & { { 3 1 } } & { { 6 . 7 0 ~ \times ~ 1 0 ^ { - 1 2 } } } \end{array}
$$

14.4 Weak\* Convergence. Numerous modes of convergence have been defined and studied for normed linear spaces.One mode,known as weak\* convergence,is particularly relevant to the problem of approximation of linear functionals.In order to see how it fits into the scheme of things, it is convenient to make several preliminary definitions,some of which have been met before.

DEFINITioN l4.4.1． (Strong or ordinary convergence in $\pmb { X }$ .）A sequence of elements $\left\{ x _ { n } \right\}$ is said to converge strongly to $\pmb { x }$ if $\operatorname* { l i m } _ { n \to \infty } \| { \pmb x } - { \pmb x } _ { n } \| = 0$ (cf. 7.2).

Ex. 1.If $\pmb { H }$ is a Hilbert space and $\{ \boldsymbol { x } _ { k } ^ { \ * } \}$ is a complete orthonormal sequence, then for arbitrary $\pmb { x } \in \pmb { H }$ ，the Fourier segments $\sum _ { i \mathop { = } 1 } ^ { n } ( x , x _ { k } { ^ \ast } ) x _ { k } { ^ \ast }$ converge strongly to $_ { \pmb { x } }$ (Theorem 8.9.1,B). 1

DEFINITION l4.4.2. (Weak convergence in $\pmb { X }$ .）A sequence of elements $\left\{ x _ { n } \right\}$ is said to converge weakly to $_ { \pmb { x } }$ if $\operatorname* { l i m } _ { n \to \infty } | L ( x ) - L ( x _ { n } ) | = 0$ for all $\pmb { L } \in \pmb { X } ^ { * }$ ( $X ^ { * }$ is the normed conjugate space of $\pmb { X }$ ）

Ex.2.Let $\pmb { H }$ be a Hilbert space.Then，any orthonormal sequence $\{ x _ { k } ^ { \star } \}$ converges weakly to O.For by Theorem 9.3.3, $L ( x _ { k } { } ^ { * } ) = ( x _ { k } { } ^ { * } , x )$ for an appropriate $x \in H$ .By Theorem 8.9.1,C, $\operatorname* { l i m } _ { k \to \infty } \ \big | { L ( x _ { k } * ) - L ( 0 ) } \big | = 0$ On the other hand, $\{ \boldsymbol { x } _ { k } ^ { \ * } \}$ does not converge strongly to O,for $\| x _ { k } ^ { \star } - 0 \| = 1$

In the normed linear space $X ^ { * }$ ,there are also several modes of convergence.

DEFINITION l4.4.3. Strong convergence in $X ^ { * }$ . A sequence of elements $\{ \underline { { L } } _ { n } \}$ of $X ^ { * }$ is said to converge strongly to $\pmb { L }$ if $\operatorname* { l i m } _ { n \to \infty } \| { \cal L } - { \cal L } _ { n } \| = 0$ .This parallels Definition 14.4.1.

Ex.3. $X = { \cal C } [ a , b ]$ with $\| f \| = \operatorname* { m a x } _ { a \leq x \leq b } | f ( x ) |$ .Let $L _ { n } ( f ) = \sum _ { k = 1 } ^ { n } a _ { k n } f ( x _ { k n } )$ where $a \leq x _ { k n } \leq b$ and $\operatorname* { l i m } _ { n  \infty } \sum _ { k = 1 } ^ { n } | a _ { k n } | = 0$ Then,in view of Ex.5,9.3, $L _ { n } \to 0$ strongly.

Less useful is

DEFINITION l4.4.4. Weak convergence in $X ^ { * }$ . A sequence of elements $\{ \underline { { L } } _ { n } \}$ of $X ^ { * }$ is said to converge weakly in $X ^ { * }$ to $\pmb { L }$ if $\operatorname* { l i m } _ { n \to \infty } | L ^ { * } ( L _ { n } ) - L ^ { * } ( L ) | = 0$ for every element $L ^ { * } \in ( X ^ { * } ) ^ { * }$

An intermediate mode is

DEFINITIoN l4.4.5. Weak\* convergence: A sequence of elements $\{ \underline { { L } } _ { n } \}$ of $X ^ { * }$ has a weak\* limit $\pmb { L }$ if

$$
\operatorname* { l i m } _ { n  \infty } | L _ { n } ( x ) - L ( x ) | = 0
$$

for all ${ \pmb x } \in { \pmb X }$

Weak\* convergence is precisely what is required for the convergence of approximate rules, for we would like the approximate answers obtained, $\scriptstyle { \cal L } _ { n } ( x )$ ,to approach the true answer $\pmb { L } ( \pmb { x } )$ , for any element $_ { \pmb { x } }$

Ex. 4. $X = C [ a , b ] , \| f \| = \operatorname* { m a x } _ { a \leq x \leq b } \left| f ( x ) \right| . .$ Let be a triangular sequence of points of $[ a , b ]$ such that

Set $L _ { n } ( f ) = \sum _ { k = 1 } ^ { n } f ( x _ { n k } ) ( x _ { n , k } - x _ { n , k - 1 } )$ f $L ( f ) = \int _ { a } ^ { b } f ( x ) d x$ then by the properties of the Riemann integral, $L _ { n } ( f ) \to { \cal L } ( f )$ for every $f \in X$ $\scriptstyle { \cal L }$ is the weak\* limit of $\{ L _ { n } \}$

Ex.5.X = C[-1,1], $\| f \| = \operatorname* { m a x } _ { - 1 \leq x \leq 1 } \left| f ( x ) \right|$ . Let the functions $\textstyle K _ { n } ( x )$ satisfy Fejer's conditions (cf. 12.2.10-.12): $\scriptstyle K _ { n } ( x )$ integrable and $\geq 0 , \int _ { - 1 } ^ { + 1 } K _ { n } ( x ) d x = 1 ,$ and if $M _ { n } ( \delta ) \ = \ \operatorname* { m a x } \ K _ { n } ( x )$ ，then lim Mn(δ)=0 for all $0 < \delta < 1$ Set +1 ≤x≤1 n→8 $L _ { n } ( f ) = \int _ { - 1 } f ( x ) K _ { n } ( x ) d x , L ( f ) = f ( 0 )$ . Then, $L _ { n }$ converges weakly to $\pmb { L }$ .For,

$$
L ( f ) ~ - ~ L _ { n } ( f ) ~ = \int _ { - 1 } ^ { + 1 } ( f ( 0 ) ~ - f ( x ) ) K _ { n } ( x ) ~ d x ~ = \int _ { - \delta } ^ { + \delta } ( f ( 0 ) ~ - f ( x ) ) K _ { n } ( x ) ~ d x ~
$$

$$
+ \int _ { \delta } ^ { 1 } ( f ( 0 ) - f ( x ) ) K _ { n } ( x ) d x \ + \int _ { - 1 } ^ { - \delta } ( f ( 0 ) - f ( x ) ) K _ { n } ( x ) d x .
$$

Hence

$$
\begin{array} { r l } & { \displaystyle  L ( f ) - L _ { n } ( f )  \le \displaystyle  f ( 0 ) - f ( \xi )  \displaystyle \int _ { - \delta } ^ { + \delta } K _ { n } ( x ) d x } \\ & { \qquad \displaystyle +  M _ { n } ( \delta ) \Biggl [ \int _ { \delta } ^ { 1 } \bigl \lvert f ( 0 ) - f ( x ) \bigr \rvert d x + \int _ { - 1 } ^ { - \delta } \bigl \lvert f ( 0 ) - f ( x ) \bigr \rvert d x \Biggr ] } \end{array}
$$

$\leq \left| f ( 0 ) - f ( \xi ) \right| \int _ { - 1 } ^ { + 1 } K _ { n } ( x ) d x + M _ { n } ( \delta ) \int _ { - 1 } ^ { + 1 } \left| f ( 0 ) - f ( x ) \right| d x ,$ where $- \delta \leq \xi \leq \delta$

Allow $\textstyle n \to \infty$ ; then lim sup $\left| L ( f ) - L _ { n } ( f ) \right| \leq \left| f ( 0 ) - f ( \xi ) \right| .$

Since $\delta$ is arbitrary and $f$ is continuous, we conclude that $\operatorname* { l i m } _ { n \to \infty } L _ { n } ( f ) = L ( f )$ Employing the Dirac $\delta$ function: $f ( 0 ) = \int _ { - 1 } ^ { + 1 } f ( x ) \delta ( x ) d x ;$ ，we may speak of the Fejer kernels $\scriptstyle K _ { n } ( x )$ as“converging” to $\delta ( x )$ in the above sense.

A sequence of functionals can have only one weak\* limit.For suppose that $\pmb { L }$ and $M$ are both weak\* limits of $\{ L _ { n } \}$ .Then,for all $x \in X$ ， $L _ { n } ( x ) \to L ( x )$ and $L _ { n } ( x ) \to M ( x )$ .Hence $L ( x ) = M ( x )$ for all $x \in \mathbf { X }$ ,and this means that $L = M$

Strong convergence in $X ^ { * }$ implies weak\* convergence.For,assume that $\operatorname* { l i m } _ { n \to \infty } \| L - L _ { n } \| = 0 .$ Then, for any ${ \boldsymbol { x } } \in X$ ， $| L ( x ) - L _ { n } ( x ) | = | ( L - L _ { n } ) ( x ) | \leq$ $\| L - L _ { n } \| \ \| x \| \to 0$

On the other hand, weak\* convergence does not necessrily imply strong convergence.As in Ex.2,this is most easily seen in a Hilbert space.If $\{ x _ { n } * \}$ is an orthonormal system,set ${ L } _ { n } ( x ) = ( x , { x _ { n } } ^ { * } )$ . Then, $L _ { n } ( x ) \to 0$ for all $\boldsymbol { x } \in H$ so that O is the weak $^ *$ limit of $\{ L _ { n } \}$ . On the other hand, $\| 0 - L _ { n } \| =$ $\| x _ { n } ^ { * } \| = 1$

However,in a Hilbert space,if $\pmb { L }$ is the weak\* limit of $\{ L _ { n } \}$ and if $\| L _ { n } \| \to$ $\| \pmb { L } \|$ ，then $\| L - L _ { n } \| \to 0$ For let $L _ { n } ( y ) = ( y , x _ { n } )$ and $L ( y ) = ( y , x )$ Then $( y , x _ { n } ) \to ( y , x )$ for all $y \in H$ .In particular, $( x , x _ { n } ) \to ( x , x )$ .Moreover $( x _ { n } , x _ { n } ) \to ( x , x )$ . Now,

$$
\begin{array} { r l } & { \| L - L _ { n } \| ^ { 2 } = \| x - x _ { n } \| ^ { 2 } } \\ & { \qquad = ( x , x ) - ( x , x _ { n } ) - ( x _ { n } , x ) + ( x _ { n } , x _ { n } ) \to ( x , x ) - ( x , x ) - ( x , x ) } \\ & { \qquad + ( x , x ) = 0 . } \end{array}
$$

LEMMA 14.4.1．Let $X$ be $\pmb { a }$ complete metric space (cf.7.2). Suppose that $U _ { n } = U ( x _ { n } , \varepsilon _ { n } )$ is a sequence of closed balls such that $U _ { \mathbf { 1 } } \supseteq U _ { \mathbf { 2 } } \supseteq \cdots$ ，and lim $\varepsilon _ { n } = 0$ . Then,there is an $x \in X$ with $x \in U _ { n }$ ， $n = 1$ ,2,.... $\pmb { n }  \infty$

Proof: Given ε, we can find $\pmb { N }$ such that $\varepsilon _ { n } < \varepsilon$ for all $\pmb { n } \geq N$ .If $m \geq n$ ， then $U _ { m } \subseteq U _ { n }$ and hence ${ \boldsymbol { x } } _ { m } \in U _ { n }$ . Therefore $d ( x _ { m } , x _ { n } ) < \varepsilon$ for all $_ m$ ， $\pmb { n } \geq \pmb { N }$ ,and $\{ x _ { m } \}$ is a Cauchy sequence. Now $X$ is a complete space and so there is an $x \in \mathbf { X }$ with lim $d ( x , x _ { n } ) = 0$ .Let $U _ { j }$ be one of the balls. The $\pmb { n }  \infty$ elements $x _ { j } , x _ { j + 1 } , \ldots .$ ， all belong to $U _ { j }$ . Since $U _ { j }$ is closed, the limit ${ \boldsymbol { x } } \in U _ { j }$ and lience belongs to all the balls.

THEOREM 14.4.2．Let $X$ be a complete normed linear space. Suppose that $\{ L _ { n } \}$ is $^ { \pmb { a } }$ sequence of bounded linear functionals such that for all $x \in X$ ,the sequence of constants $\{ L _ { n } ( x ) \}$ is convergent. Then,we can find an $M$ such that

$$
\| L _ { n } \| \leq M \qquad n = 1 , 2 , . . . .
$$

Proof: Suppose that (14.4.2) were not true. Then, lim sup $\| L _ { n } \| = \infty$ $\pmb { \mathscr { n } }  \infty$ For a given $x _ { \mathbf { 0 } } \in X$ ，consider the closed ball $U ( x _ { 0 } , \varepsilon )$ consisting of those

elements $_ { \pmb { x } }$ for which $\| { \pmb x } - { \pmb x } _ { \mathbf 0 } \| \le \varepsilon$ It is now claimed that

$$
| L _ { n } ( x ) | \leq K \qquad n = 1 , 2 , \ldots ; x \in U ( x _ { 0 } , \varepsilon )
$$

is impossible. For take any $y \in X , y \neq 0$ Then

$$
z = \frac { \varepsilon y } { \| y \| } + x _ { 0 }
$$

is clearly in $U ( { \pmb x } _ { \mathbf { 0 } } , \pmb \varepsilon )$ .Now, $L _ { n } ( z ) = \frac { \varepsilon } { \| y \| } L _ { n } ( y ) + L _ { n } ( x _ { 0 } )$ Hence,

$$
\frac { \varepsilon } { \| y \| } \left| L _ { n } ( y ) \right| - | L _ { n } ( x _ { 0 } ) | \leq \left| \frac { \varepsilon } { \| y \| } L _ { n } ( y ) + L _ { n } ( x _ { 0 } ) \right| = | L _ { n } ( z ) | \leq K .
$$

This implies that $\begin{array} { r } { | L _ { n } ( y ) | \leq ( K + | L _ { n } ( x _ { 0 } ) | ) \frac { \| y \| } { \varepsilon } } \end{array}$ Since {Ln(xo)} converges, the sequence $| L _ { n } ( x _ { 0 } ) |$ is bounded.For some constant $K _ { 1 }$ ,therefore, $| L _ { n } ( y ) | \leq$ $\pmb { K } _ { 1 } \parallel y \parallel$ for all $y \in X$ .This tells us that $\| L _ { n } \| \leq K _ { 1 }$ , contrary to our assumption.

Take a $U ( \pmb { x } _ { 0 } , \pmb { \varepsilon } )$ . As has just been established,we can find an index $\pmb { n _ { 1 } }$ and an element $\pmb { x } _ { 1 } \in U ( \pmb { x } _ { 0 } , \pmb { \varepsilon } )$ for which

$$
| L _ { n _ { 1 } } ( x _ { 1 } ) | > 1 .
$$

Since $L _ { n _ { 1 } }$ is continuous,we can assume that $\pmb { x _ { 1 } }$ is in the interior of $U ( \pmb { x } _ { \mathbf { 0 } } , \pmb { \varepsilon } )$ and can therefore find a second ball centered at $\pmb { x _ { 1 } }$ ， $U ( x _ { 1 } , \varepsilon _ { 1 } )$ ,with $U ( \pmb { x } _ { 1 } , \pmb { \varepsilon } _ { 1 } ) \subset$ $U ( \pmb { x } _ { 0 } , \pmb { \varepsilon } )$ such that $| L _ { n _ { 1 } } ( x ) | > 1$ for all ${ \pmb x } \in { \pmb U } ( { \pmb x } _ { 1 } , { \pmb \varepsilon } _ { 1 } )$ .But again,the quantities $| L _ { n } ( x ) |$ cannot be bounded for ${ \pmb x } \in { \pmb U } ( { \pmb x } _ { 1 } , { \pmb \varepsilon } _ { 1 } )$ .Hence,we can find an $n _ { \mathbf { 2 } } > n _ { \mathbf { 1 } }$ for which $| L _ { n _ { 2 } } ( x _ { 2 } ) | > 2$ .We proceed in this way. A sequence of balls $\boldsymbol { U } ( \boldsymbol { x } _ { n } , \varepsilon _ { n } )$ ，each contained in the previous one,can be found for which $| L _ { n _ { j } } ( x ) | > j$ ${ \pmb x } \in { U } ( { \pmb x } _ { j } , { \pmb \varepsilon } _ { j } )$ .Moreover we may choose $\varepsilon _ { n } \to 0$ Since $\pmb { X }$ is complete,we can by Lemma l4.4.1 find an element $\pmb { x } ^ { \prime }$ lying in each of the nested sequence of balls. Then $| L _ { n _ { j } } ( x ^ { \prime } ) | > j , j = 1 , 2 , . . .$ . This contradicts the hypothesis that $\{ L _ { n } ( x ) \}$ is convergent for all $_ { \pmb { x } }$ .The assumption that

$$
\operatorname* { l i m } _ { n \to \infty } \| { \cal L } _ { n } \| = \infty
$$

must have been fallacious.

CoROLLARY l4.4.3. Under the hypothesis of the last theorem,we can find a boundedlinear functional $\pmb { L }$ for which

$$
\operatorname* { l i m } _ { n \to \infty } L _ { n } ( x ) = L ( x ) , x \in X .
$$

Proof: For a given $\pmb { x } \in \pmb { X }$ ,define $\scriptstyle { \cal L } ( { \pmb x } )$ by means of

$$
L ( x ) = \operatorname* { l i m } _ { n  \infty } L _ { n } ( x ) .
$$

$$
\begin{array} { l } { { \displaystyle { \cal L } ( a x + b y ) = \operatorname* { l i m } _ { n \to \infty } { \cal L } _ { n } ( a x + b y ) = \operatorname* { l i m } _ { n \to \infty } \left\{ a { \cal L } _ { n } ( x ) + b { \cal L } _ { n } ( y ) \right\} } } \\ { { \displaystyle ~ = a \operatorname* { l i m } _ { n \to \infty } { \cal L } _ { n } ( x ) + b \operatorname* { l i m } _ { n \to \infty } { \cal L } _ { n } ( y ) = a { \cal L } ( x ) + b { \cal L } ( y ) . } } \end{array}
$$

The functional $\scriptstyle { \cal L }$ is therefore linear.

By the theorem, there is an $M$ such that $\| L _ { n } \| \leq M$ ， $n = 1$ ,2,....Take an $x \in X$ .Then, $\lvert L _ { n } ( x ) \rvert \leq \lvert \lvert L _ { n } \rvert \rvert \lvert x \rvert \rvert \leq M \lvert \lvert x \rvert \rvert$ . From (14.4.7), $| L ( x ) | \leq M \ \| x \|$ Accordingly, $\pmb { L }$ is bounded and $\| { \mathbf { } } L \| \leq M$

A similar theorem holds when the $L _ { n }$ are linear operators which send the elements of one complete normed linear space $\pmb { X }$ into a second such space $\pmb { Y }$

We now come to the fundamental theorem of weak\* convergence. Many men have made contributions toward the final statement.Among them are Osgood,Vitali,Lebesgue,Polya,and Banach.

THEOREM 14.4.4. Let $\pmb { X }$ be a complete normed linear space, and let $L , L _ { 1 } $ $\ L _ { 2 } , \ldots .$ ，be bounded linear functionals defined on $\pmb { X }$ .In order that $L$ be the weak\* limit of the sequence $\left\{ L _ { k } \right\}$ ,it is necessary and sufficient that

$$
\| L _ { k } \| \leq M \qquad k = 1 , 2 , \ldots ,
$$

for some constant $M$ ,and that

$$
\operatorname * { l i m } _ { k  \infty } { \cal L } _ { k } ( x _ { j } ) = { \cal L } ( x _ { j } ) \qquad j = 1 , 2 , . . . ,
$$

for some sequence of elements $\{ x _ { j } \}$ that is closed in $\pmb { X }$

In this connection,the constants $\| L _ { k } \|$ are known as the Lebesgue Constants.

Proof:Sufficiency.We shall show that (14.4.8-9) implies that

$$
\operatorname* { l i m } _ { n \to \infty } { \cal L } _ { n } ( x ) = { \cal L } ( x )
$$

for all $x \in X$ .Take an $x \in X$ . Given an $\pmb \varepsilon$ ,we can,in view of the closure of $\left\{ x _ { j } \right\}$ ,find constants $a _ { 1 } , \ldots , a _ { k }$ such that $\| x - y _ { k } \| \le \varepsilon$ where

$$
y _ { k } = a _ { 1 } x _ { 1 } + \cdot \cdot \cdot + a _ { k } x _ { k } .
$$

Now $L ( x ) - L _ { n } ( x ) = L ( x ) - L ( y _ { k } ) + L ( y _ { k } ) - L _ { n } ( y _ { k } ) + L _ { n } ( y _ { k } ) - L _ { n } ( x )$ so that

$$
\begin{array} { r l } & { | L ( x ) - L _ { n } ( x ) | \leq | L ( x ) - L ( y _ { k } ) | + | L ( y _ { k } ) - L _ { n } ( y _ { k } ) | + | L _ { n } ( y _ { k } ) - L _ { n } ( x ) | } \\ & { \qquad \leq \| L \| ~ \| x - y _ { k } \| + | L ( y _ { k } ) - L _ { n } ( y _ { k } ) | + \| L _ { n } \| ~ \| x - y _ { k } \| . } \end{array}
$$

Keep $\pmb { k }$ fixed and allow $n \to \infty$ . By (14.4.9)， we have $\operatorname* { l i m } _ { n \to \infty } \ : L _ { n } ( y _ { k } ) = L ( y _ { k } )$ Using this and (l4.4.8),we have lim sup $| L ( x ) - L _ { n } ( x ) | \leq \| L \| \ \varepsilon + M \varepsilon$ n-Since $\pmb \varepsilon$ is arbitrary,this implies that $\operatorname* { l i m } _ { n  \infty } { \cal L } _ { n } ( x ) = { \cal L } ( x ) ,$

Necessity. (14.4.9) is trivial. (14.4.8) follows from Theorem 14.4.2.

The fundamental theorem of weak\* convergence can be applied usefully in two ways. Since conditions (l4.4.8-9) are sufficient, they can be used to demonstrate the convergence of a sequence of functionals.Since they are also necessary,they can also be used to demonstrate the impossibility of convergence.Examples of both types of application follow.Some of the results have been obtained previously.

Ex.6． Convergence of Bernstein Polynomials.

Let $X = C [ 0 ;$ 1], $\| f \| = \operatorname* { m a x } _ { 0 \leq x \leq 1 } \left| f ( x ) \right|$ . Let $_ { \pmb { x } }$ be a fixed point in [O,1] and set

$$
L _ { n } ( f ) = \sum _ { k = 0 } ^ { n } f \left( { \frac { k } { n } } \right) \binom { n } { k } x ^ { k } ( 1 - x ) ^ { n - k } \equiv B _ { n } ( f ; x )
$$

and

$$
L ( f ) = f ( { \boldsymbol { x } } ) .
$$

Now,from 9.3, Ex.5, $\| L _ { n } \| = \sum _ { k = 0 } ^ { n } { \binom { n } { k } } x ^ { k } ( 1 - x ) ^ { n - k } = 1 .$ Furthermore (.2,Ex.5) $L _ { n } ( e ^ { \lambda x } ) = ( 1 - x + x e ^ { \lambda / n } ) ^ { n }$ s0 that lir $\begin{array} { r } { \underset { \infty } { \mathrm { ~ n ~ } } L _ { n } ( e ^ { \lambda x } ) = e ^ { \lambda x } = L ( e ^ { \lambda x } ) } \end{array}$ . The system of exponentials $1 , e ^ { x } , e ^ { 2 x } , \ldots$ ，is closed in $C [ 0 , 1 ]$ .This follows from Weierstrass' Theorem (on the interval[1,e]） by a change of variable.Applying Theorem 14.4.4,we learn that $B _ { n } ( f ; x ) \to f ( x )$

Ex.7.Fejer Summability of Fourier Series.

Let $x$ be the set of functions that are continuous and periodic on $[ - \pi , \pi ]$ ， $\| f \| = \operatorname* { m a x } _ { - \pi \leq x \leq \pi } \left| f ( x ) \right|$ . Let $_ { x }$ be a fixed point in the interval and set $L ( f ) = f ( x ) ,$ $L _ { n } ( f ) = \sigma _ { n } ( f ; x ) =$ the Fejer sums for $f$ (cf.Lemma 12.2.2).For an integer $\mathcal { p }$ ， sin $_ { p x }$ has the Fourier expansion $0 + 0 + \cdot \cdot \cdot + \sin p x + 0 + 0 + \cdot \cdot \cdot$ ，and hence, for $\pmb { n }$ sufficiently large, its Fejér sums (the averages of the partial sums of the series)must be ${ \frac { ( n - p ) \sin p x } { n } } \to \sin p x$ A similar remark holds for cos $\mathbf { \nabla } _ { \mathbf { \mathcal { P } } } \mathbf { x }$ Thus, $L _ { n } { \binom { \sin p x } { \cos p x } } \to L { \binom { \sin p x } { \cos p x } }$ Now, $L _ { n } ( f ) = { \frac { 1 } { 2 \pi n } } \int _ { - \pi } ^ { \pi } f ( x + t ) { \frac { \sin ^ { 2 } n t / 2 } { ( \sin t / 2 ) ^ { 2 } } } d t .$ Since the kernelis positive,|/Lnll= $\| L _ { n } \| = { \frac { 1 } { 2 \pi n } } \int _ { - \pi } ^ { \pi } { \frac { \sin ^ { 2 } n t / 2 } { ( \sin t / 2 ) ^ { 2 } } } d t = 1 .$ An application of the Theorem 14.4.4 yields $\sigma _ { n } ( f ; x ) \to f ( x )$

Ex.8. Convergence of Quadrature Processes.

Let $X = C [ a , b ] , \| f \| = \operatorname* { m a x } _ { a \leq x \leq b } \left| f ( x ) \right|$ . Suppose that we have been given a triangular system of abscissas and weights

$$
\begin{array} { r l r l } & { x _ { 1 1 } } & & { a _ { 1 1 } } \\ & { x _ { 2 1 } x _ { 2 2 } } & & { a _ { 2 1 } a _ { 2 2 } } \\ & { x _ { 3 1 } x _ { 3 2 } x _ { 3 3 } } & & { a _ { 3 1 } a _ { 3 2 } a _ { 3 3 } } \\ & { . } & & { . } \\ & { . } & & { . } \\ & { . } & & { . } \end{array}
$$

and we construct a sequence of quadrature rules from them:

$$
L _ { n } ( f ) = \sum _ { k = 1 } ^ { n } a _ { n k } f ( x _ { n k } ) \qquad n = 1 , 2 , \ldots .
$$

Under what circumstances can we assert that

$$
\operatorname* { l i m } _ { n \to \infty } \ L _ { n } ( f ) \ = \int _ { a } ^ { b } f ( x ) \ d x , f \in C [ a , b ] \uparrow
$$

Inasmuch as $\| L _ { n } \| = \sum _ { k = 1 } ^ { n } \left| a _ { n k } \right|$ , an application of Theorem 14.4.4 yields:

THEOREM l4.4.5 (Polya). Let there be given a sequence of quadrature rules $\{ L _ { n } \}$ We have

$$
\operatorname* { l i m } _ { n \to \infty } L _ { n } ( f ) = \int _ { a } ^ { b } f ( x ) d x \quad { \mathrm { f o r ~ a l l ~ } } f \in C [ a , b ]
$$

if and only if

$$
\operatorname* { l i m } _ { n \to \infty } { \cal L } _ { n } ( x ^ { k } ) = \int _ { a } ^ { b } x ^ { k } d x \qquad k = 0 , 1 , \ldots ,
$$

and

$$
\sum _ { k = 1 } ^ { n } | a _ { n k } | \leq M \qquad n = 1 , 2 , \ldots .
$$

for some constant $M$

COROLLARY 14.4.6 (Stekloff).Let $a _ { n k } > 0$ .Then (14.4.14) holds if and only if (14.4.15) holds.

Proof: $\sum _ { k = 1 } ^ { n } \left| a _ { n k } \right| = \sum _ { k = 1 } ^ { n } a _ { n k } = L _ { n } ( 1 )$ Now if (14.4.15) holds then $L _ { n } ( 1 )$ is bounded.Hence (l4.4.16) holds and (14.4.14) follows.Conversely if (14.4.14) holds,(14.4.15) holds trivially.

COROLLARY 14.4.7 (Stieltjes).Let ${ w } ( { \pmb x } )$ be $^ { \pmb { a } }$ weight function on $[ a , b ]$ Let ${ \pmb x _ { n i } }$ be the abscissas and $w _ { n i }$ be the weights in the Gauss-Jacobi quadrature formula. Then,

$$
\int _ { a } ^ { b } w ( x ) f ( x ) d x = \operatorname* { l i m } _ { n \to \infty } \sum _ { i = 1 } ^ { n } w _ { n i } f ( x _ { n i } )
$$

for all $f ( x ) \in C [ a , b ]$

$L _ { n } ( x ^ { k } ) = \int _ { a } ^ { b } x ^ { k } d x$ $0 \leq k \leq 2 n - 1$ $L ( f ) = \int _ { a } ^ { b } w ( x ) f ( x ) d x$ r $L _ { n } ( f ) = \sum _ { i = 1 } ^ { n } w _ { n i } f ( x _ { n i } )$ $w _ { n i }$ then positive. Hence $\sum _ { i = 1 } ^ { n } | w _ { n i } | = b - a .$

Actully, more y prove $L _ { n } ( f ) \to \int _ { a } ^ { b } w ( x ) f ( x ) d x$ for any bounded $f ( x )$ for which the Riemann integral $\int _ { a } ^ { b } w ( x ) f ( x ) d x$ exists.

Ex.9．Equidistributed Sequences. A particular instance of the scheme (l4.4.12) is

$$
\begin{array} { l l l } { x _ { 1 } } & { h } & { } \\ { } & { } & { } \\ { x _ { 1 } x _ { 2 } } & { \frac { h } { 2 } \frac { h } { 2 } } \\ { } & { } & { } \\ { x _ { 1 } x _ { 2 } x _ { 3 } } & { \frac { h } { 3 } \frac { h } { 3 } \frac { h } { 3 } } \\ { } & { } & { } \\ { . } & { } & { . } \\ { . } & { } & { . } \\ { } & { } & { . } \\ { } & { } & { h = b - } \end{array}
$$

leading to the equation

$$
\operatorname* { l i m } _ { n \to \infty } { \frac { 1 } { n } } \sum _ { k = 1 } ^ { n } f ( x _ { k } ) = { \frac { 1 } { b \ - \ a } } \int _ { a } ^ { b } f ( x ) \ d x , f \in C [ a , b ] .
$$

The theory of this equation will now be developed.

LEMMA 14.4.8． Let $\pmb { F }$ and $G$ be two families of bounded,Riemann integrable functions on $[ \pmb { a } , \pmb { b } ]$ .If (14.4.19) holds for all $f \in F$ ,andifforeach $g \in G$ and $\varepsilon > 0$ ,we can find $f _ { 1 } , f _ { 2 } \in F$ such that

$$
\begin{array} { c } { { f _ { 1 } \leq g \leq f _ { 2 } \qquad a \leq x \leq b } } \\ { { \displaystyle \int _ { a } ^ { b } ( f _ { 2 } - f _ { 1 } ) d x \leq \varepsilon , } } \end{array}
$$

then (14.4.19) holds for all $g \in G$

$$
\begin{array} { r c l } { \displaystyle { \frac { 1 } { n } \left[ f _ { 1 } ( x _ { 1 } ) + f _ { 1 } ( x _ { 2 } ) + \cdots + f _ { 1 } ( x _ { n } ) \right] \le \frac { 1 } { n } \left[ g ( x _ { 1 } ) + \cdots + g ( x _ { n } ) \right] } } \\ { \displaystyle { \phantom { \frac { 1 } { n } \left[ f _ { 1 } ( x _ { 1 } ) + f _ { 1 } ( x _ { 2 } ) + \cdots + f _ { n } ( x _ { n } ) \right] } \le \frac { 1 } { n } \left[ f _ { 2 } ( x _ { 1 } ) + \cdots + f _ { 2 } ( x _ { n } ) \right] } . } \end{array}
$$

Hence,

$$
\begin{array} { l } { \displaystyle \int _ { a } ^ { b } f _ { 1 } ( x ) d x \leq \displaystyle \operatorname* { l i m } _ { n \to \infty } \operatorname* { i n f } _ { n } \frac 1 n \left[ g ( x _ { 1 } ) + \cdots \cdot + g ( x _ { n } ) \right] } \\ { \leq \displaystyle \operatorname* { l i m } _ { n \to \infty } \operatorname* { s u p } \frac 1 n \left[ g ( x _ { 1 } ) + \cdots \cdot + g ( x _ { n } ) \right] \leq \int _ { a } ^ { b } f _ { 2 } ( x ) d x . } \end{array}
$$

In view of (14.4.2O),the lim inf and the lim sup can be made arbitrarily close, and hence Call it $\boldsymbol { \mathit { I } }$ Then,

$$
\begin{array} { r l r } & { } & { \underset { n  \infty } { \operatorname* { l i m } } \frac { 1 } { n } [ g ( x _ { 1 } ) + \cdot \cdot \cdot + g ( x _ { n } ) ] \mathrm { e x i s t s . } } \\ & { } & { \displaystyle \int _ { a } ^ { b } f _ { 1 } ( x ) d x \leq I \leq \int _ { a } ^ { b } f _ { 2 } ( x ) d x . } \end{array}
$$

Then,

$$
0 \leq { \Biggl | } I - \int _ { a } ^ { b } g ( x ) d x { \Biggr | } \leq \int _ { a } ^ { b } f _ { 2 } ( x ) d x - \int _ { a } ^ { b } f _ { 1 } ( x ) d x \leq \varepsilon .
$$

Since $\pmb \varepsilon$ is arbitrary, $I = \int _ { a } ^ { b } g ( x ) \ d x$

COROLLARY 14.4.9．Let $R [ { \pmb a } , { \pmb b } ]$ designate the space of bounded，Riemann integrable functions on $[ a , b ]$ . The limit (14.4.19) holds for all $f \in C [ a , b ]$ f and only if it holds for all $f \in R [ a , b ]$

Proof: Since $C [ { a } , { b } ] \subset \mathbb { R } [ { a } , { b } ]$ ,it remains to prove the“only if”part. Let $\pmb { F } = C [ \pmb { a } , \pmb { b } ]$ and $G = R [ a , b ]$ .Take a ${ \pmb g } \in { \pmb R } [ { \pmb a } , { \pmb b } ]$ .We can obviously assume that $\pmb { g }$ is nonnegative.(For otherwise add a sufficiently large constant.) Observe first that we can find piecewise constant functions $f _ { 1 }$ and $f _ { 2 }$ such that (l4.4.2O) holds.For,by an elementary property of the Riemann integral，we can find a sub-division $a = \xi _ { 0 } < \xi _ { 1 } < \cdot \cdot \cdot < \xi _ { n - 1 } < \xi _ { n } = b$ such that the upper sum $U = \sum _ { k = 1 } ^ { n } M _ { k } ( \xi _ { k } - \xi _ { k - 1 } )$ and the lower sum $L =$ $\sum _ { k = 1 } ^ { n } m _ { k } ( \xi _ { k } - \xi _ { k - 1 } )$ differ by less than $\varepsilon \colon U - L < \varepsilon$ .Here we have written $\begin{array} { r l } { M _ { k } = } & { { } \operatorname* { s u p } } \end{array}$ $f ( x )$ ， $m _ { k } =$ inf $f ( x )$ . Now set $f _ { \mathbf { 2 } } ( x ) = M _ { k }$ on $\xi _ { k - 1 } \leq x < \xi _ { k } ,$ $\xi _ { k - 1 } \leq x \leq \xi _ { k } \qquad \xi _ { k - 1 } \leq x \leq \xi _ { k }$ $k = 1 , 2 , \ldots , n - 1$ and $f _ { \mathbf { 2 } } ( x ) = M _ { n }$ on $\xi _ { n - 1 } \leq x \leq \xi _ { n }$ Use a similar definition for $f _ { 1 }$

We wish to show next that we can find two functions $f _ { 1 }$ and $f _ { 2 } \in F =$ $C [ \pmb { a } , \pmb { b } ]$ such that the approximation (l4.4.20) holds. This type of approximation has a transitivity property,so that by what we have just proved, it suffices to take $\pmb { g }$ as positive and piecewise constant. Such functions $\pmb { g }$ are linear combinations with positive coefficients of functions of the type $\pmb { h } ( x ) = 1$ for $c \leq x \leq d$ ， $\pmb { h } ( \pmb { x } ) = \mathbf { 0 }$ elsewhere in $[ a , b ]$ $( a \leq c < d \leq b )$ .For sufficiently small $\delta$ ，define a continuous function $\pmb { h } _ { \delta }$ by means of $h _ { \delta } ( x ) =$ $1 + \delta$ for $c \leq x \leq d$ ， $\pmb { h } _ { \delta } ( \pmb { x } ) = \delta$ for $a \leq x \leq c - \delta$ and $d + \delta \leq ^ { \cdot } x \leq b$ ， $h _ { \delta } ( x ) =$ linear for $c - \delta \leq x \leq c ,$ ， $d \leq x \leq d + \delta$ .Then itiseasily verified that $h _ { \delta } ( x ) \geq h ( x ) + \delta$ and $0 < \int _ { a } ^ { b } ( h _ { \delta } ( x ) - h ( x ) ) \ d x$ can be made arbitrarily small for $\delta$ sufficiently small.A similar process can be carried out on the under side of $\pmb { h }$

DEFINITIoN 14.4.6. A sequence of points $\{ x _ { k } \}$ lying in $[ a , b ]$ is called equidistributed in $[ a , b ]$ if (14.4.19) holds for all $f \in C \left[ a , b \right]$

The word “equidistributed”arises from the following property of such sequences. Let $[ \sigma _ { 1 } , \sigma _ { 2 } ]$ be any interval contained in $[ a , b ]$ and let $N _ { n } [ \sigma _ { 1 } , \sigma _ { 2 } ]$ designate the number of points among the $x _ { 1 } , x _ { 2 } , \ldots , x _ { n }$ that lie in

$$
\sigma _ { 1 } \leq x \leq \sigma _ { 2 } .
$$

Then,

$$
\operatorname* { l i m } _ { n  \infty } \frac { 1 } { n } N _ { n } [ \sigma _ { 1 } , \sigma _ { 2 } ] = \frac { \sigma _ { 2 } - \sigma _ { 1 } } { b - a } .
$$

In other words,each interval contains,asymptotically,a fraction of the terms of the sequence in direct proportion to its length. This is a simple consequence of Corollary l4.4.9 by selecting $f = 1$ on ${ \pmb { \sigma } } _ { 1 } \leq { \pmb { x } } \leq { \pmb { \sigma } } _ { 2 }$ and $f = 0$ elsewhere.

COROLLARY 14.4.10．Let $\mathbf { \mathit { C } _ { \mathit { p } } [ \mathit { a } , \delta ] }$ designate the space of continuous and periodic (i.e., $f ( a ) = f ( b ) )$ functions on $[ a , b ]$ .The limit (14.4.19) holds for all $f \in C _ { p } [ a , b ]$ if and only if it holds for all $f \in C [ a , b ]$

Proof: Since $C _ { p } [ a , b ] \subset C [ a , b ]$ ,it remains to prove the“only if”part. Let $\boldsymbol { F } = \boldsymbol { C } _ { p } [ \boldsymbol { a } , \boldsymbol { b } ]$ and $G = C [ \boldsymbol { a } , \boldsymbol { b } ]$ . Take ${ \pmb g } \in C [ { \pmb a } , { \pmb b } ]$ .We may evidently suppose it to be positive. Let $M = \operatorname* { m a x } _ { a \leq x \leq b } g ( x )$ Select $\pmb { K }$ so that $\frac { { \cal K } } { g ( a ) } > 1 ,$ $\frac { \kappa } { g ( b ) } > 1$ . Pick an $\eta$ so that $0 < \eta < \operatorname* { m i n } \Big [ b - a , \varepsilon M ^ { - 1 } K ^ { - 1 } \Big ( \frac { 1 } { g ( a ) } + \frac { 1 } { g ( b ) } \Big ) ^ { - 1 } \Big ] .$ Define a continuous function $\Phi ( { \pmb x } )$ by means of $\Phi ( a ) = \frac { K } { g ( a ) } , \Phi ( b ) = \frac { K } { g ( b ) } ,$ $\Phi ( { \pmb x } ) = 1$ for $\pmb { a } + \eta \le \pmb { x } \le \pmb { b } - \eta$ ,and $\Phi ( x ) =$ linear elsewhere.Then $\Phi ( x ) \geq 1$ Set $f _ { 2 } ( x ) = \Phi ( x ) g ( x )$ Then $f _ { 2 } ( x ) \geq g ( x )$ and $f _ { 2 } ( x )$ is continuous.Moreover, $f _ { 2 } ( a ) = \Phi ( a ) g ( a ) = K = \Phi ( b ) g ( b ) = f _ { 2 } ( b )$ ,so that $f _ { 2 } \in C _ { p } [ a , b ]$ . Finally,

$$
\int _ { a } ^ { b } ( f _ { 2 } ( x ) - g ( x ) ) d x \leq \int _ { a } ^ { a + \eta } { \frac { K M } { g ( a ) } } d x + \int _ { b - \eta } ^ { b } { \frac { K M } { g ( b ) } } d x = \eta K M \left( { \frac { 1 } { g ( a ) } } + { \frac { 1 } { g ( b ) } } \right) +
$$

A similar process can be carried out on the under side of $\pmb { g }$ to yield an $f _ { 1 }$

THEOREM 14.4.11. The sequence $\left\{ x _ { k } \right\}$ is equidistributed in $[ a , b ]$ if and only if (14.4.19) holds for a sequence of functions $\left\{ f _ { k } ( x ) \right\}$ that is closed in $C [ \alpha , b ]$ or $ { C } _ { p } [ a , b ]$ with $\| f \| = \operatorname* { m a x } _ { a \leq x \leq b } | f ( x ) |$

Prof: Set $L ( f ) = \int _ { a } ^ { b } f ( x ) d x , L _ { n } ( f ) = { \frac { 1 } { n } } \sum _ { k = 1 } ^ { n } f ( x _ { k } )$ Then, $\| L _ { n } \| = 1$ Apply Theorem l4.4.4 and Corollary 14.4.10.

As yet,we have not exhibited an equidistributed sequence.The simplest one is provided by

THEOREM 14.4.12 (Bohl-Sierpinski-Weyl)． Let $\theta$ be an irrational number, and set ${ \pmb x _ { n } } =$ the fractional part of $\mathbf { \Omega } _ { n \theta }$ i.e., ${ x _ { n } = n \theta - [ n \theta ] }$ ,where $[ n \theta ]$ is the largest integer $< n \theta$ .Then $\left\{ x _ { n } \right\}$ is equidistributed in [0,1].

Proof: The functions $e ^ { 2 \pi i k x }$ ， $k = 0$ ，±1，±2....， are closed in $C _ { p } [ 0 , 1 ]$ with $\| f \| = \operatorname* { m a x } _ { 0 \leq x \leq 1 } | f ( x ) |$ . Hence by Theorem 14.4.11, it suffices to show that $\operatorname* { l i m } _ { n \to \infty } { \frac { 1 } { n } } \left[ e ^ { 2 \pi i k x _ { 1 } } + \cdot \cdot \cdot + e ^ { 2 \pi i k x _ { n } } \right] = \int _ { 0 } ^ { 1 } e ^ { 2 \pi i k x } d x , \ k = 0 , \pm 1 , \pm 2 , \ldots . . . { \mathrm { \bf ~ F o r } }$ $k = 0$ ,the limit holds trivially. For $k \neq 0 , \int _ { 0 } ^ { 1 } e ^ { 2 \pi i k x } d x = 0$ Since $e ^ { 2 \pi i k x _ { 3 } } =$ $e ^ { 2 \pi i k ( j \theta - [ j \theta ] ) } = e ^ { 2 \pi i k j \theta }$ ，

$$
{ \begin{array} { l } { { \frac { 1 } { n } } \left[ e ^ { 2 \pi i k x _ { 1 } } + \cdot \cdot \cdot + e ^ { 2 \pi i k x _ { n } } \right] = { \frac { 1 } { n } } \left[ e ^ { 2 \pi i k } + ( e ^ { 2 \pi i k \theta } ) ^ { 2 } + \cdot \cdot \cdot + ( e ^ { 2 \pi i k \theta } ) ^ { n } \right] } \\ { \quad \ } \\ { \displaystyle = { \frac { 1 } { n } } \left( e ^ { 2 \pi i k \theta } \right) { \frac { e ^ { 2 \pi i k n \theta } - 1 } { e ^ { 2 \pi i k \theta } - 1 } } . } \end{array} }
$$

Since $\theta$ is irrational, $e ^ { 2 \pi i k \theta } \neq 1$ .For $\pm 1 , \pm 2 , . . .$ ，the exponential expression is bounded as $n \to \infty$ and the limit O is obtained.

Ex.l0. A nonexistence theorem for quadratures. We have seen that it is indeed possible to have

$$
\sum _ { k = 1 } ^ { n } a _ { n k } f \left( x _ { k } \right) \to \int _ { a } ^ { b } f \left( x \right) d x \quad { \mathrm { f o r } } \quad f \in C [ a , b ] .
$$

Notice that the left-hand member involves a double array of weights.Would it be possible to replace it with a single array and have

$$
\sum _ { k = 1 } ^ { \infty } a _ { k } f ( x _ { k } ) = \int _ { a } ^ { b } f ( x ) d x
$$

for all $f \in C [ a , b ] \colon$ Such a formula would obviously be much simpler.In (14.4.22) we assume that $a _ { k } \neq 0 , a \leq x _ { k } \leq b$ ,the $x _ { k }$ are distinct,and both the $a _ { k }$ and the $\pmb { x } _ { k }$ are independent of $f$ ，An application of Theorem 14.4.4 will show this is impossible:

THEOREM 14.4.13. It is impossible to have $\int _ { a } ^ { b } f ( x ) d x = \sum _ { k = 1 } ^ { \infty } a _ { k } f ( x _ { k } )$ for all $f \in C [ \alpha , b ]$ under the above conditions on $\pmb { a } _ { k }$ and $\pmb { x } _ { k }$

Proof:Note first that if (l4.4.22) holds,then the $\pmb { x } _ { k }$ must be dense in $[ a , b ]$ .For,suppose there were an interval $\pmb { I }$ contained in $[ a , b ]$ which is free of abscissas $\pmb { x } _ { k }$ Let $\scriptstyle { I ^ { \prime } }$ be an interval interior to $\pmb { I }$ .Then it is clear that we may find a continuous function $\pmb { f } ( \pmb { x } )$ which is zero exterior to $\boldsymbol { \mathit { I } }$ and is positive interior to $\scriptstyle { I ^ { \prime } }$ . Then, $f ( x _ { k } ) = 0$ ， $k = 1 , 2 , \ldots$ ,since all the $\pmb { x } _ { \pmb { k } }$ lie outside

1. Thug, $0 < \int _ { a } ^ { b } f ( x ) d x = \sum _ { k = 1 } ^ { \infty } a _ { k } f ( x _ { k } ) = 0 .$

Work in $\boldsymbol { X } = \boldsymbol { C } [ \boldsymbol { a } , \boldsymbol { b } ]$ $\| f \| = \operatorname* { m a x } _ { a \leq x \leq b } | f ( x ) |$ Set $L ( f ) = \int _ { a } ^ { b } f ( x ) d x$ and $L _ { n } ( f ) = \sum _ { k = 1 } ^ { n } a _ { k } f ( x _ { k } )$ Then, $\| L \| = b - a , \| L _ { n } \| = \sum _ { k = 1 } ^ { n } | a _ { k } |$ . By Theorem 14.4.4,

i $L _ { n } ( f ) \to L ( f )$ $f \in X$ $M$ Such hae $\sum _ { k = 1 } ^ { n } \left| a _ { k } \right| < M$ for   
$\pmb { n }$ $\sum _ { i = 1 } ^ { \infty } a _ { k }$ must converge absolutely. 1

Select a $\boldsymbol { k }$ for which $a < x _ { k } < b$ Designate by $I _ { \varepsilon }$ the interval

$$
x _ { k } - \varepsilon \leq x \leq x _ { k } + \varepsilon .
$$

We can choose $\pmb \varepsilon$ sufficiently small so that $I _ { \epsilon }$ will be contained in $a < x < b$ The abscissas $x _ { i }$ lying in $I _ { \epsilon }$ will form a subset of all abscissas,and of the former,by choosing ε small enough,we can also guarantee that $x _ { k }$ will be the one which possesses the minimum subscript. In order of increasig subscripts the abscissas lying in Ie will be designated by xx = Xn1(e), Xnz(e)., where,moreover, $\operatorname* { l i m } _ { \varepsilon \to 0 } n _ { 2 } ( \varepsilon ) = \infty$

For each ε construct the following continuous triangular shaped function:

$$
\begin{array} { r l r l } & { f _ { \varepsilon } ( x ) = 0 } & & { \mathrm { f o r ~ } x \mathrm { ~ e x t e r i o r ~ t o ~ } I _ { \varepsilon } } \\ & { f _ { \varepsilon } ( x ) = \mathrm { l i n e a r } } & & { x _ { k } - \varepsilon \leq x \leq x _ { k } + \varepsilon } \\ & { f _ { \varepsilon } ( x _ { k } ) = 1 } \\ & { f _ { \varepsilon } ( x ) = \mathrm { l i n e a r } } & & { x _ { k } \leq x \leq x _ { k } + \varepsilon . } \end{array}
$$

Then $| f _ { \varepsilon } ( x ) | \le 1$ and $\int _ { a } ^ { b } f _ { \varepsilon } ( x ) d x = \varepsilon$ Aso，

$$
\varepsilon = \sum _ { j = 0 } ^ { \infty } a _ { j } f _ { \varepsilon } ( x _ { j } ) = a _ { k } f _ { \varepsilon } ( x _ { k } ) + \sum _ { j = 2 } ^ { \infty } a _ { n _ { j } ( \varepsilon ) } f _ { \varepsilon } ( x _ { n _ { j } ( \varepsilon ) } ) .
$$

Therefore, $| \pmb { \varepsilon } - \pmb { a } _ { k } | \leq \sum _ { j = 2 } ^ { \infty } | \pmb { a } _ { n _ { j } ( \pmb { \varepsilon } ) } |$ Now let $\varepsilon \to 0$ . The left side approaches $ { \boldsymbol { a } } _ { k } \neq 0$ Since $n _ { \mathrm { 2 } } ( \varepsilon ) \to \infty$ ，the right side approaches zero.This isa contradiction and (14.4.22) is impossible.

Ex.1l. Divergence of Fourier Series of a Continuous Function.This is developed in the final two theorems.

THEOREM 14.4.14 (Fejér)． Let

$$
\rho _ { n } = { \frac { 1 } { 2 \pi } } \int _ { - \pi } ^ { \pi } \left| \left. { \frac { \sin { ( n + { \frac { 1 } { 2 } } ) t } } { \sin { \frac { t } { 2 } } } } \right| d t . \right.
$$

Then,

$$
\operatorname* { l i m } _ { n \to \infty } \frac { \rho _ { n } } { \log n } = \frac { 4 } { \pi ^ { 2 } } .
$$

Proof:We have

$$
\rho _ { n } = \frac { 1 } { \pi } \int _ { - \pi / 2 } ^ { \pi / 2 } \left| \frac { \sin { ( 2 n + 1 ) t } } { \sin { t } } \right| d t = \frac { 2 } { \pi } \int _ { 0 } ^ { \pi / 2 } \frac { | \sin { ( 2 n + 1 ) t } | } { \sin { t } } d t .
$$

Hence,

$$
\begin{array} { l } { { \displaystyle \rho _ { n } = \frac { 2 } { n } \int _ { 0 } ^ { \pi / 2 } \frac { \left| \sin { ( 2 n + 1 ) t } \right| } { t } d t + \frac { 2 } { \pi } \int _ { 0 } ^ { \pi / 2 } \left( \frac { 1 } { \sin { t } } - \frac { 1 } { t } \right) \left| \sin { ( 2 n + 1 ) t } \right| d t } } \\ { { \displaystyle \quad = { \bf I } _ { n } + { \bf I I } _ { n } } } \end{array}
$$

$$
{ \mathrm { ; f u n c t i o n } } { \frac { 1 } { \sin t } } - { \frac { 1 } { t } } { \mathrm { i s ~ n o n n e g a t i v e ~ o n } } { \bigg [ } 0 , { \frac { \pi } { 2 } } { \bigg ] } { \mathrm { a n d ~ } } 0 \leq { \big | } \sin { ( 2 n + 1 ) t } { \big | } \leq 1 .
$$

Therefore, $0 \leq \operatorname { I I } _ { n } \leq { \frac { 2 } { \pi } } \int _ { 0 } ^ { \pi / 2 } \left( { \frac { 1 } { \sin t } } - { \frac { 1 } { t } } \right) d t$ ，and the integrals $\mathbf { I I } _ { n }$ are bounded. Again,

$$
\mathsf { I } _ { n } = \frac { 2 } { \pi } \int _ { 0 } ^ { ( n + 1 ) \pi / ( 2 n + 1 ) } \frac { | \sin { ( 2 n + 1 ) } t | } { t } d t - \frac { 2 } { \pi } \int _ { \pi / 2 } ^ { ( n + 1 ) \pi / ( 2 n + 1 ) } \frac { | \sin { ( 2 n + 1 ) } t | } { t } d t
$$

$$
\mathbf { \Delta } = \operatorname { I I I } _ { n } - \operatorname { I V } _ { n } .
$$

But,

$$
0 \leq \mathbf { I } \mathbf { V } _ { n } = { \frac { 2 } { \pi } } \int _ { \pi / 2 } ^ { ( n + 1 ) \pi / ( 2 n + 1 ) } { \frac { | \sin { ( 2 n + 1 ) t } | } { t } } d t \leq { \frac { 2 } { \pi } } \int _ { \pi / 2 } ^ { ( n + 1 ) \pi / ( 2 n + 1 ) } { \frac { d t } { t } } .
$$

Since $\operatorname* { l i m } _ { n \to \infty } { \frac { ( n + 1 ) \pi } { 2 n + 1 } } = { \frac { \pi } { 2 } } , \operatorname* { l i m } _ { n \to \infty } \operatorname { I V } _ { n } = 0$ Changing variables,

$$
{ \begin{array} { r l } & { { \mathrm { I I I } } _ { n } = { \cfrac { 2 } { \pi } } \int _ { 0 } ^ { ( n + 1 ) \pi / ( 2 n + 1 ) } \underbrace { \left| \sin { ( 2 n + 1 ) t } \right| } _ { t } d t = { \cfrac { 2 } { \pi } } \int _ { 0 } ^ { ( n + 1 ) \pi } \underbrace { \left| \sin { t } \right| } _ { t } d t } \\ & { \quad \quad = { \cfrac { 2 } { \pi } } \int _ { 0 } ^ { \pi } \underbrace { \left| \sin { t } \right| } _ { t } d t + { \cfrac { 2 } { \pi } } \int _ { \pi } ^ { ( n + 1 ) \pi } \underbrace { \left| \sin { t } \right| } _ { t } d t } \\ & { \quad \quad = \nabla + { \mathrm { V I } } _ { n } . } \end{array} }
$$

Now,

$$
\begin{array} { l } { { \displaystyle \operatorname { V I } _ { n } = \frac 2 \pi \int _ { 0 } ^ { \pi } \left( \frac 1 { t + \pi } + \frac 1 { t + 2 \pi } + \cdot \cdot \cdot + \frac 1 { t + n \pi } \right) \sin t d t } } \\ { { \displaystyle ~ = \frac 2 \pi \int _ { 0 } ^ { \pi } S _ { n } ( t ) \sin t d t , } } \end{array}
$$

where $S _ { n } ( t ) = { \frac { 1 } { t + \pi } } + { \frac { 1 } { t + 2 \pi } } + \cdots + { \frac { 1 } { t + n \pi } }$ .0n $0 \leq t \leq \pi$ we have, ${ \frac { 1 } { 2 \pi } } + { \frac { 1 } { 3 \pi } } + \cdots + { \frac { 1 } { ( n + 1 ) \pi } } \leq S _ { n } ( t ) \leq { \frac { 1 } { \pi } } + { \frac { 1 } { 2 \pi } } + \cdots + { \frac { 1 } { n \pi } }$ We now employ the well known property of the harmonic series:

$$
1 + { \frac { 1 } { 2 } } + { \frac { 1 } { 3 } } + \cdots + { \frac { 1 } { n } } - \log n = \gamma _ { n } , \operatorname* { l i m } _ { n \to \infty } \gamma _ { n } = \gamma = . 5 7 7 \cdots .
$$

Thus,

$$
\frac { 1 } { \pi } \left( \log \left( n + 1 \right) + \gamma _ { n + 1 } - 1 \right) \leq S _ { n } ( t ) \leq \frac { 1 } { \pi } \left( \log n + \gamma _ { n } \right) ,
$$

and

$$
\frac { 2 } { \pi ^ { 2 } } \left( \log \left( n + 1 \right) + \gamma _ { n + 1 } - 1 \right) \int _ { 0 } ^ { \pi } \sin t d t \leq \mathrm { V I } _ { n } \leq \frac { 2 } { \pi ^ { 2 } } \left( \log n + \gamma _ { n } \right) \int _ { 0 } ^ { \pi } \sin t d t .
$$

Therefore, $\operatorname* { l i m } _ { n \to \infty } { \frac { \nabla \mathbf { I } _ { n } } { \log n } } = { \frac { 4 } { \pi ^ { 2 } } }$ Now $\rho _ { n } = \mathrm { V } + \mathrm { V I } _ { n } - \mathrm { I V } _ { n } + \mathrm { I I } _ { n }$ and the theorem follows from the individual limiting behaviors.

THEOREm l4.4.15 (du Bois-Reymond). There exists a continuous function whose Fourier series diverges at ${ \boldsymbol { x } } = 0$

Proof:From (l2.l.5),the partial sum of the Fourier series evaluated at $x = 0$ is $L _ { n } ( f ) = { \frac { 1 } { 2 \pi } } \int _ { - \pi } ^ { \pi } { \frac { \sin { ( n + { \frac { 1 } { 2 } } ) t } } { \sin { \frac { t } { 2 } } } } f ( t ) d t$ Work in the space $X \colon C [ - \pi , \pi ]$ $f ( - \pi ) = f ( \pi ) , \parallel f \parallel = \operatorname* { m a x } _ { - \pi \leq x \leq \pi } | f ( x ) |$ Since, $\| L _ { n } \| = \rho _ { n } \to \infty$ ，the theorem follows from Theorem 14.4.4.

# NOTES ON CHAPTER XIV

14.1For a glance at the integration rules available,see Stroud []. 14.2Markof[1], Chapters V-VII, Szego [1], pp. 47-48,Hobson [1] pp. 76-83. 14.3Sard [1],Nikolsky[1],Davis [2],[3],Davis and Rabinowitz [1], Golomb and Weinberger [l],Krilov [l] Chapter 8. 14.4Ljusternik and Sobolew [l] pp.131-136.Feldheim [1],Krilov [1], Chapter l2.For equidistributed sequences,see Polya and Szego [l] vol. I, pp.67-77.Theorem l4.4.13,Davis [1]. On the other hand,if duplications in the abscissas are allowed,(14.4.22) is possible. See John [1].

# PROBLEMS

1. Can constants $a _ { \bf 1 } , a _ { \bf 2 } , x _ { \bf 1 } , x _ { \bf 2 }$ be determined so that the differentiation rule   
of“Gauss type" $f ^ { \prime } ( 0 ) = a _ { 1 } f ( x _ { 1 } ) + a _ { 2 } f ( x _ { 2 } )$ is valid for $f = 1 , x , x ^ { 2 } , x ^ { 3 } \colon$ 2.Integrate the Bernstein polynomial $\textstyle B _ { n } ( f ; x )$ over [0,1] and interpret what   
is obtained. 3. Let $\{ { p _ { n } } ^ { * } ( x ) \}$ be orthonormal polynomials with respect to the inner product   
$( f , g ) \ = \int _ { - 1 } ^ { + 1 } w ( x ) f ( x ) g ( x ) \ d x$ Let $x _ { 1 } , \ldots , x _ { n }$ and $w _ { 1 } , \ldots , w _ { n }$ be the abscissas

and weights of the corresponding Gauss-Jacobi integration rule.The polynomials $p _ { 0 } { } ^ { * } , \ldots , p _ { n - 1 } ^ { * }$ are also orthonormal with respect to the inner product

$$
( f , g ) = \sum _ { k = 1 } ^ { n } w _ { k } f ( x _ { k } ) g ( x _ { k } ) .
$$

4. The error in the Gauss rule of order $\pmb { n }$ over $[ a , b ]$ is

$$
\frac { ( b - a ) ^ { 2 n + 1 } 2 ^ { 2 n + 1 } ( n ! ) ^ { 4 } f ^ { ( 2 n ) } ( \xi ) } { ( 2 n + 1 ) [ ( 2 n ) ! ] ^ { 3 } } .
$$

5.In problems 5,6,7,and 8, $E _ { n } ( f )$ designates the error in the Gauss rule of order $_ n$ over $[ - 1 , 1 ]$ .Determine $E _ { n } ( x ^ { 2 n } )$

6.If $f$ is analyte then $E _ { n } ( f ) = { \frac { 1 } { \pi i } } \int _ { C } { \frac { f ( z ) Q _ { n } ( z ) } { P _ { n } ( z ) } } d z . \ ( \mathrm { C }$ f. (24.13,)

on 7. Prove that $[ - 1 , 1 ]$ · $\operatorname* { l i m } _ { n \to \infty } E _ { n } ( f ) = 0 { \mathrm { ~ i f ~ } } f$ is a bounded Riemann integrable function

8. Study the rapidity of convergence to O of $E _ { n } ( f )$ where $f$ is analytic on $[ - 1 , 1 ]$

9. Let $Q _ { n } ( f ) = \sum _ { k = 1 } ^ { n } w _ { n k } f ( x _ { n k } ) , n = 1 , \cdot \cdot \cdot ,$ ，be a sequence of quadrature rules for $\int _ { a } ^ { b } f ( x ) d x$ .Suppose that $Q _ { n }$ is exact for ${ \mathcal { P } } _ { \pmb { n } }$ . If for some $\varepsilon$ ，the abscissas satisfy $a + \varepsilon \leq x _ { n k } \leq b - \varepsilon$ ，then for sufficiently large $n , w _ { n 1 } , \ldots , w _ { n n }$ must have a change in sign.

10.Derive Landau's Theorem (Lemma 9.3.7) as a consequence of Theorem

14.4.4.

11. Study the behavior as $n  \infty$ of the sequence

$$
\sigma _ { n } = | \sin 1 \sin 2 \sin 3 \cdot \cdot \cdot \sin n | .
$$

12. Study the behavior as $n  \infty$ of the sequence

$$
\sigma _ { n } = [ \theta ] + [ 2 \theta ] + \cdot \cdot \cdot + [ n \theta ]
$$

for $\theta$ rational and irrational.

13.A triangular sequence $x _ { n 1 } , x _ { n 2 } , . ~ . ~ . ~ , x _ { n n } ( n = 1 , 2 , . ~ . ~ . )$ is called equidistributed on $[ a , b ]$ if $\operatorname* { l i m } _ { n \to \infty } { \frac { 1 } { n } } \sum _ { k = 1 } ^ { n } f ( x _ { n k } ) \ = \int _ { a } ^ { b } f ( x ) d x \operatorname { f o r } \operatorname { a l l } f \in C [ a , b ] .$ Give simple examples of equidistributed triangular sequences.

14.Find necessary and suffcient conditions that a triangular sequence be equidistributed.

# This page intentionally left blank

# Appendix

# This page intentionally left blank

# Short Guide to the Orthogonal Polynomials

I Name: Legendre $S y m b o l \colon { \cal P } _ { n } ( x ) \qquad I n t e r v a l ; [ - 1 , 1 ]$ Weight: 1 Standardization: $P _ { n } ( 1 ) = 1$ Norm: $\int _ { - 1 } ^ { + 1 } ( P _ { n } ( x ) ) ^ { 2 } d x = { \frac { 2 } { 2 n + 1 } }$ Exrplit Expresion: $P _ { n } ( x ) = \frac { 1 } { 2 ^ { n } } \sum _ { m = 0 } ^ { [ n / 2 ] } ( - 1 ) ^ { m } { \binom { n } { m } } \binom { 2 n - 2 m } { n } x ^ { n - 2 m }$ Recurrence Relation: $( n + 1 ) P _ { n + 1 } ( x ) = ( 2 n + 1 ) x P _ { n } ( x ) - n P _ { n - 1 } ( x )$ Differential Equation: $( 1 - x ^ { 2 } ) y ^ { \prime \prime } - 2 x y ^ { \prime } + n ( n + 1 ) y = 0$ $y = P _ { n } ( x )$ Rodrigues’Formula: $P _ { n } ( x ) = \frac { ( - 1 ) ^ { n } } { 2 ^ { n } n ! } \frac { d ^ { n } } { d x ^ { n } } \left\{ ( 1 - x ^ { 2 } ) ^ { n } \right\}$ Generating Function: ${ \cal R } ^ { - 1 } = \sum _ { n = 0 } ^ { \infty } P _ { n } ( x ) z ^ { n } ; ~ - 1 < x < 1 , | z | < 1 ,$ $R = { \sqrt { 1 - 2 x z + z ^ { 2 } } } .$ Inequality: $| P _ { n } ( x ) | \leq 1 , - 1 \leq x \leq 1$

# II

Name: Tschebysheff, First KindSymbol: $\boldsymbol { T } _ { \boldsymbol { n } } ( \boldsymbol { x } )$ Interval: [-1,1]   
Weight: $( 1 - x ^ { 2 } ) ^ { - \frac { 1 } { 2 } }$ Standardization: $T _ { n } ( 1 ) = 1$   
Norm: $\int _ { - 1 } ^ { + 1 } ( 1 - x ^ { 2 } ) ^ { - { \frac { 1 } { 2 } } } ( T _ { n } ( x ) ) ^ { 2 } d x = { \left\{ \begin{array} { l l } { \pi / 2 , } & { n \neq 0 } \\ { \pi , } & { n = 0 } \end{array} \right. }$   
Explicit E $x p r e s s i o n \colon { \frac { n } { 2 } } \sum _ { m = 0 } ^ { [ n / 2 ] } ( - 1 ) ^ { m } { \frac { ( n - m - 1 ) ! } { m ! ( n - 2 m ) ! } } ( 2 x ) ^ { n - 2 m } = \cos { ( n \operatorname { a r c c o s } { x } ) }$ $\mathbf { \Phi } = \mathbf { \mathcal { T } } _ { n } ( \pmb { x } )$   
Recurrence Relation: $T _ { n + 1 } ( x ) = 2 x T _ { n } ( x ) - T _ { n - 1 } ( x )$   
Differential Equation: $( 1 - x ^ { 2 } ) y ^ { \prime \prime } - x y ^ { \prime } + n ^ { 2 } y = 0$ $y = T _ { n } ( x )$   
Rodrigues'Formula: ${ \frac { ( - 1 ) ^ { n } ( 1 - x ^ { 2 } ) ^ { \frac { 1 } { 2 } } { \sqrt { \pi } } } { 2 ^ { n + 1 } \Gamma ( n + \frac { 1 } { 2 } ) } } { \frac { d ^ { n } } { d x ^ { n } } } \left\{ ( 1 - x ^ { 2 } ) ^ { n - \frac { 1 } { 2 } } \right\} = T _ { n } ( x )$   
Genertin unction: $\frac { 1 - x z } { 1 - 2 x z + z ^ { 2 } } = \sum _ { n = 0 } ^ { \infty } T _ { n } ( x ) z ^ { n } , - 1 < x < 1 , | z | < 1 .$   
Inequality: $| T _ { n } ( x ) | \leq 1 , - 1 \leq x \leq 1$

# III

Name: Tschebysheff,Second KindSymbol: $U _ { n } ( x )$ Interval: [-1,1]

Weight : $( 1 - x ^ { 2 } ) ^ { \frac { 1 } { 2 } }$ Standardization: $U _ { n } ( 1 ) = n + 1$

Norm: $\int _ { - 1 } ^ { + 1 } ( 1 - x ^ { 2 } ) ^ { \frac { 1 } { 2 } } [ U _ { n } ( x ) ] ^ { 2 } d x = { \frac { \pi } { 2 } }$

Explicit Expression: $U _ { n } ( x ) = \sum _ { m = 0 } ^ { [ n / 2 ] } ( - 1 ) ^ { m } { \frac { ( m - n ) ! } { m ! ( n - 2 m ) ! } } ( 2 x ) ^ { n - 2 m }$

$$
U _ { n } ( \cos \theta ) = { \frac { \sin { ( n + 1 ) } \theta } { \sin \theta } }
$$

Recurrence Relation : $U _ { n + 1 } ( x ) = 2 x U _ { n } ( x ) - U _ { n - 1 } ( x )$

Differential Equation: $( 1 - x ^ { 2 } ) y ^ { \prime \prime } - 3 x y ^ { \prime } + n ( n + 2 ) y = 0$ $y = U _ { n } ( x )$

Rodrigues'Fol:Un()=nd $U _ { n } ( x ) = { \frac { ( - 1 ) ^ { n } ( n + 1 ) { \sqrt { \pi } } } { ( 1 - x ^ { 2 } ) ^ { \frac { 1 } { 2 } } 2 ^ { n + 1 } \Gamma ( n + { \frac { 3 } { 2 } } ) } } { \frac { d ^ { n } } { d x ^ { n } } } \left\{ ( 1 - x ^ { 2 } ) ^ { n + { \frac { 1 } { 2 } } } \right\}$

Generating Function: $\frac { 1 } { 1 - 2 x z + z ^ { 2 } } = \sum _ { n = 0 } ^ { \infty } U _ { n } ( x ) z ^ { n } , - 1 < x < 1 , | z | < 1 .$

Inequality: $| U _ { n } ( x ) | \leq n + 1 , - 1 \leq x \leq 1 ,$

IV

Name: JacobiSymbol: $P _ { n } ^ { ( \alpha , \beta ) } ( x )$ Interval: [-1,1]

Weight: $( \mathbf { 1 } - x ) ^ { \alpha } ( \mathbf { 1 } + x ) ^ { \beta } ; \alpha , \beta > - 1$

$P _ { n } ^ { ( \alpha , \beta ) } ( x ) = { \binom { n + \alpha } { n } }$

$$
\begin{array} { l } { \displaystyle \int _ { - 1 } ^ { + 1 } ( 1 - x ) ^ { \alpha } ( 1 + x ) ^ { \beta } [ P _ { n } ^ { ( \alpha , \beta ) } ( x ) ] ^ { 2 } d x } \\ { \displaystyle = \frac { 2 ^ { \alpha + \beta + 1 } \Gamma ( n + \alpha + 1 ) \Gamma ( n + \beta + 1 ) } { ( 2 n + \alpha + \beta + 1 ) n ! \Gamma ( n + \alpha + \beta + 1 ) } } \end{array}
$$

Explicit Expression:

$$
P _ { n } ^ { ( \alpha , \beta ) } ( x ) = \frac { 1 } { 2 ^ { n } } \sum _ { m = 0 } ^ { n } \binom { n + \alpha } { m } \binom { n + \beta } { n - m } ( x - 1 ) ^ { n - m } ( x + 1 ) ^ { m }
$$

$$
= ( 2 n + \alpha + \beta + 1 ) [ ( \alpha ^ { 2 } - \beta ^ { 2 } ) + ( 2 n + \alpha + \beta + 2 )
$$

Differential Equation:

$$
\begin{array} { c } { { ( 1 - x ^ { 2 } ) y ^ { \prime \prime } + ( \beta - \alpha - ( \alpha + \beta + 2 ) x ) y ^ { \prime } + n ( n + \alpha + \beta + 1 ) y = 0 } } \\ { { y = P _ { n } ^ { ( \alpha , \beta ) } ( x ) } } \end{array}
$$

Rodrigues’ Formula:

$$
P _ { n } ^ { ( \alpha , \beta ) } ( x ) = \frac { ( - 1 ) ^ { n } } { 2 ^ { n } n ! ( 1 - x ) ^ { \alpha } ( 1 + x ) ^ { \beta } } \frac { d ^ { n } } { d x ^ { n } } \left\{ ( 1 - x ) ^ { n + \alpha } ( 1 + x ) ^ { n + \beta } \right\}
$$

Generating Function:

$$
\begin{array} { r l r } {  { R ^ { - 1 } ( 1 - z + R ) ^ { - \alpha } ( 1 + z + R ) ^ { - \beta } = \sum _ { n = 0 } ^ { \infty } 2 ^ { - \alpha - \beta } P _ { n } ^ { ( \alpha , \beta ) } ( x ) z ^ { n } ; } } \\ & { } & { R = \sqrt { 1 - 2 x z + z ^ { 2 } } , \ | z | \ < 1 } \\ & { } & { \tan { \beta } } \\ & { } & { \tan { \beta } : \operatorname* { m a x } \ ( \alpha , \beta ) = \{ \begin{array} { l l } { ( \begin{array} { l } { n + q } \\ { n } \end{array} ) \sim n ^ { \alpha } \operatorname { i f } q = \operatorname* { m a x } \ ( \alpha , \beta ) \geq - \frac { 1 } { 2 } } \\ { | P _ { n } ^ { ( \alpha , \beta ) } ( x ^ { \prime } ) | \sim n ^ { - 1 } \operatorname { i f } q < - \frac { 1 } { 2 } . } \\ { | x ^ { ' } \sin { \alpha } \ \mathrm { o f ~ t h e ~ t w o ~ m a x i m u m ~ p o i n t s ~ n e a r ~ } } \\ { [ \frac { \beta - \alpha } { \alpha + \beta + 1 }  } \end{array}  } \end{array}
$$

V

Name: Generalized LaguerreSymbol: $L _ { n } ^ { ( \alpha ) } ( x )$ Interval: $[ 0 , \infty ]$

Weight : $\pmb { x } ^ { \alpha } e ^ { - \pmb { x } }$ ， ${ \mathfrak { a } } > - 1$ Standardization: $L _ { n } ^ { ( \alpha ) } ( x ) = \frac { ( - 1 ) ^ { n } } { n ! } x ^ { n } + \cdot \cdot \cdot$

$$
\int _ { 0 } ^ { \infty } x ^ { \alpha } e ^ { - x } ( L _ { n } ^ { ( \alpha ) } ( x ) ) ^ { 2 } d x = { \frac { \Gamma ( n + \alpha + 1 ) } { n ! } }
$$

ExpicitExpreso=(- xm

Recurrence Relation:

$$
( n + 1 ) L _ { n + 1 } ^ { ( \alpha ) } ( x ) = [ ( 2 n + \alpha + 1 ) - x ] L _ { n } ^ { ( \alpha ) } ( x ) - ( n + \alpha ) L _ { n - 1 } ^ { ( \alpha ) } ( x )
$$

$$
y = L _ { n } ^ { ( \alpha ) } ( x )
$$

Rodrigues' Formula: $L _ { n } ^ { ( \alpha ) } ( x ) = \frac { 1 } { n ! \ x ^ { \alpha } e ^ { - x } } \frac { d ^ { n } } { d x ^ { n } } \left\{ x ^ { n + \alpha } e ^ { - x } \right\}$

Generating Function: $( 1 - z ) ^ { - \alpha - 1 } \exp \left( { \frac { x z } { z - 1 } } \right) = \sum _ { n = 0 } ^ { \infty } L _ { n } ^ { ( \alpha ) } ( x ) z ^ { n }$

$$
| L _ { n } ^ { ( \alpha ) } ( x ) | \leq \left[ 2 - \frac { \Gamma ( \alpha + n + 1 ) } { n ! \Gamma ( \alpha + 1 ) } \right] e ^ { x / 2 } ; \quad \frac { x \geq 0 } { - 1 < \alpha < 0 }
$$

VI

Name: HermiteSymbol: $H _ { n } ( x )$ Interval: $[ - \infty , \infty ]$   
Weight: $e ^ { - x ^ { 2 } }$ Standardization: $H _ { n } ( x ) = 2 ^ { n } x ^ { n } + \cdots$   
$\begin{array}{c} \begin{array} { l l } { { } } & { { } } \\ { { } } & { { } } \\ { { } } & { { } } \\ { { } } & { { } } \\ { { } } & { { } } \end{array} et { } { ' } { \int } _ { - \infty } ^ { + \infty } e ^ { - x ^ { 2 } } [ H _ { n } ( x ) ] ^ { 2 } d x = \sqrt { \pi } ~ 2 ^ { n } n !  \\ { { } } & { { } } \\ { { } } & { { } E x p l i c i t ~ E x p r e s s i o n { : } ~ H _ { n } ( x ) = n ! \sum _ { m = 0 } ^ { [ n / 2 ] } ( - 1 ) ^ { m } \frac { ( 2 x ) ^ { n - 2 m } } { m ! ~ ( n - 2 m ) ! } } \end{array}$   
Recurrence Relation: $H _ { n + 1 } ( x ) = 2 x H _ { n } ( x ) - 2 n H _ { n - 1 } ( x )$   
Differential Equation: $y ^ { \prime \prime } - 2 x y ^ { \prime } + 2 n y = 0$ $y = H _ { n } ( x )$   
Rodrigues'Formulz: Hn(x)=(-1)e2² dn （e-2   
Generating Function: $e ^ { 2 x z - z ^ { 2 } } = \sum _ { n = 0 } ^ { \infty } { \frac { H _ { n } ( x ) z ^ { n } } { n ! } }$   
Inequality: $| H _ { 2 m } ( x ) | \leq e ^ { x ^ { 2 } / 2 } 2 ^ { 2 m } m ! \biggl [ 2 - \frac { 1 } { 2 ^ { 2 m } } \binom { 2 m } { m } \biggr ] , \quad x \geq 0$ $| H _ { 2 m + 1 } ( x ) | \leq x e ^ { x ^ { 2 } / 2 } \frac { ( 2 m + 2 ) ! } { ( m + 1 ) ! } , ~ x \geq 0$

# Table of the Tschebyscheff Polynomials

T(x）=1 ${ \begin{array} { r l } & { | \mathcal { A } _ { \theta } ( \theta ) | = 1 } \\ & { T _ { 1 } ( \theta ) = x } \\ & { T _ { 2 } ( x ) = 0 } \\ & { T _ { 3 } ( x ) = 2 \sin ^ { 6 } - 1 8 \theta } \\ & { T _ { 4 } ( x ) = 8 4 ^ { 6 } - 3 x ^ { 2 } } \\ & { T _ { 4 } ( x ) = 8 4 ^ { 4 } - 8 x ^ { 4 } + 1 8 \theta } \\ & { T _ { 5 } ( \theta ) = 1 8 \theta \sin ^ { 6 } + 3 8 \theta } \\ & { T _ { 6 } ( \theta ) = 9 4 \theta \sin ^ { 6 } - 1 1 2 \theta \sin ^ { 6 } + 1 8 \theta } \\ & { T _ { 7 } ( \theta ) = 9 8 2 ^ { 6 } - 1 8 \theta + 6 8 \theta ^ { 3 } - 7 \theta } \\ & { T _ { 1 } ( x ) = 1 2 8 \theta \sin ^ { 6 } - 5 5 6 0 \theta + 6 1 6 0 ^ { 6 } - 3 2 \theta ^ { 2 } + 1 } \\ & { T _ { 1 } ( x ) = 1 2 8 8 \theta - 5 5 6 0 \theta + 1 6 0 2 ^ { 6 } - 1 2 0 \theta ^ { 3 } + 9 6 } \\ & { T _ { 8 } ( x ) = 2 8 1 2 \theta - 1 2 8 \theta \sin ^ { 6 } + 1 2 1 2 0 \theta ^ { 3 } - 4 0 0 \theta ^ { 4 } + 5 6 0 \theta ^ { 5 } - 1 } \\ & { T _ { 1 0 } ( x ) = 1 0 2 4 6 8 \theta - 2 8 1 6 \theta \sin ^ { 6 } + 2 1 8 \theta ^ { 2 } - 1 1 2 3 2 \theta ^ { 5 } + 2 0 2 9 \theta ^ { 5 } + 2 5 9 2 \theta ^ { 5 } } \\ & { T _ { 1 0 } ( x ) = 2 0 4 8 \theta - 6 1 1 4 \theta ^ { 1 0 } + 6 8 0 1 2 \theta ^ { 3 } - 3 8 6 4 \theta ^ { 4 } + 3 4 0 4 \theta ^ { 4 } } \end{array} }$

# Table of Powers as Combinations of the Tschebyscheff Polynomials

$$
\begin{array} { r l } & { \quad 1 - \eta _ { s } } \\ & { \quad _ { x } = - 2 } \\ & { \quad _ { x } = - 2 } \\ & { \quad _ { d } - \frac { 1 } { 2 } ( \theta _ { 1 } + \eta _ { s } ) } \\ & { \quad _ { x } = - \frac { 1 } { 4 } \frac { \mathcal { B } \eta _ { s } } { \mathcal { B } \eta _ { s } } + 2 \eta _ { s } } \\ & { \quad _ { d } - \frac { 1 } { 2 } \frac { \mathcal { B } \eta _ { s } } { \mathcal { B } \eta _ { s } } - 4 \eta _ { s } ^ { \prime } \frac { 1 } { 2 } } \\ & { \quad _ { x } = - \frac { 1 } { 8 } ( \Pi \tau _ { s } - \mathcal { B } \tau _ { s } - \mathcal { T } _ { s } ) } \\ & { \quad _ { y } = - \frac { 1 } { 8 } \frac { 1 } { 4 } \mathcal { B } \eta _ { s } \left( 1 + \Pi \tau _ { s } + \Pi \tau _ { s } + \Pi \tau _ { s } \right) } \\ & { \quad _ { x } = - \frac { 1 } { 8 } ( 1 + 2 \tau _ { 1 } + 3 \tau _ { 1 } + 7 \tau _ { 1 } + \Pi \tau _ { s } ) } \\ & { \quad _ { x } = - \frac { 1 } { 1 0 } ( 5 \pi _ { s } + 3 \tau _ { 1 } + 3 \tau _ { 2 } + \Pi \tau _ { s } ) } \\ & { \quad _ { x } = - \frac { 1 } { 1 0 } 1 3 \pi \alpha _ { s } + 3 \tau _ { 2 } + \Pi \tau _ { s } + \mathcal { B } \tau _ { s } + \frac { 1 } { 2 } } \\ & { \quad _ { x } = - \frac { 1 } { 1 0 } 1 3 \pi \alpha _ { s } + 3 \tau _ { 3 } - 8 \tau _ { 3 } + \frac { 1 } { 2 } } \end{array}
$$

$$
\begin{array} { r l } & { x ^ { * } - \frac { 1 } { 1 6 } ! 0 C _ { 1 } + 6 \mathcal { D } _ { 1 } + 4 \mathcal { D } _ { 3 } \mathcal { T } _ { 4 } } \\ & { x ^ { * } - \frac { 1 } { 1 6 } ( 1 0 C _ { 2 } + 1 5 \mathcal { T } _ { 4 } - 6 \mathcal { T } _ { 4 } + 7 \varphi _ { 3 } ) } \\ & { x ^ { 2 } - \frac { 1 } { 1 6 4 } ( 3 6 \mathcal { D } _ { 1 } - 1 5 \mathcal { T } _ { 2 } - 6 4 \mathcal { T } _ { 4 } + 7 \varphi _ { 1 } + 7 \varphi _ { 2 } ) } \\ & { x ^ { 2 } - \frac { 1 } { 1 6 4 } ( 3 6 \mathcal { D } _ { 1 } + 2 1 \mathcal { T } _ { 1 } + 7 \varphi _ { 1 } + 7 \varphi _ { 1 } + 7 \varphi _ { 1 } ) } \\ & { x ^ { 3 } - \frac { 1 } { 1 2 } | 3 5 \mathcal { D } _ { 1 } ^ { ( 3 ) } \mathcal { T } _ { 4 } + 1 6 \mathcal { D } _ { 2 } + 2 9 \mathcal { T } _ { 4 } + 8 \mathcal { T } _ { 4 } + 7 \varphi _ { 3 } \mathcal { T } _ { 4 } } \\ & { x ^ { 3 } - \frac { 1 } { 1 6 4 } ( 1 2 C _ { 1 } + 3 4 C _ { 3 } + 3 6 \mathcal { T } _ { 4 } + 4 7 \varphi _ { 2 } + 7 \varphi _ { 3 } ) } \\ & { x ^ { 3 } - \frac { 1 } { 1 6 4 } ( 1 2 \mathcal { D } _ { 1 } + 1 2 0 C _ { 2 } + 1 2 0 \mathcal { T } _ { 4 } + 4 3 \mathcal { T } _ { 5 } + 1 0 2 \varphi _ { 2 } + 7 \varphi _ { 3 } ) } \\ & { x ^ { 2 } - \frac { 1 } { 1 6 4 } ( 1 6 2 C _ { 1 } + 3 3 0 \mathcal { D } _ { 2 } + 1 8 4 \mathcal { D } _ { 3 } + 4 5 \mathcal { D } _ { 2 } + 1 1 7 \varphi _ { 2 } + 7 \varphi _ { 1 } ) } \\ & { x ^ { 3 } - \frac { 1 } { 1 6 4 } ( 1 6 2 C _ { 1 } + 3 3 0 \mathcal { D } _ { 2 } + 1 8 4 \mathcal { D } _ { 3 } + 5 5 \mathcal { D } _ { 4 } + 1 7 \varphi _ { 2 } + 1 8 \mathcal { T } _ { 5 } + 7 \varphi _ { 1 } ) } \\ &  x ^ { 4 } - \frac { 1 } { 3 2 } ( 5 6 2 C _   \end{array}
$$

# Table of the Legendre Polynomials

$$
\begin{array} { r l } & { P _ { 3 } = 1 } \\ & { P _ { 1 } = 1 } \\ & { P _ { 2 } = \frac { 1 } { 2 } ( 3 ^ { ( 3 ) / 2 } - 1 ) } \\ & { P _ { 3 } = \frac { 1 } { 2 } ( 3 ^ { ( 3 ) / 2 } - 3 6 ) } \\ & { P _ { 4 } = \frac { 1 } { 3 } ( 3 ^ { ( 3 ) / 2 } - 3 6 0 ^ { ( 3 ) / 2 } + 3 ) } \\ & { P _ { 5 } = \frac { 1 } { 6 } ( 3 ^ { ( 3 ) / 2 } - 3 6 0 ^ { ( 3 ) / 2 } + 3 ) } \\ & { P _ { 6 } = \frac { 1 } { 6 } ( 3 ^ { ( 3 ) / 2 } - 7 0 ^ { ( 3 ) / 2 } - 1 5 6 ) } \\ & { P _ { 6 } = \frac { 1 } { 1 6 } ( 3 ^ { ( 3 ) / 2 } - 3 1 8 ^ { ( 4 ) / 4 } + 1 0 1 6 ^ { ( 3 ) / 6 } - 6 3 ) } \\ & { P _ { 7 } = \frac { 1 } { 1 6 } ( 3 ^ { ( 3 ) / 2 } - 6 1 0 ^ { ( 3 ) / 2 } - 6 3 1 8 ^ { ( 3 ) / 2 } - 2 1 2 8 ^ { ( 3 ) } } \\ & { P _ { 8 } = \frac { 1 } { 1 5 } ( 3 ^ { ( 3 ) / 2 } - 1 5 6 ) } \end{array}
$$

Table of Powers as Linear Combinations of the Legendre Polynomials

$$
\begin{array} { r l } & { \mathcal { R } ^ { \nu } = \Gamma _ { \nu \downarrow } ^ { \nu } } \\ & { \quad _ { s } = \Gamma _ { 1 } ^ { \nu } } \\ & { \quad _ { s } = \frac { 1 } { s ^ { 2 } } ( \Gamma _ { 2 } ^ { \nu } + \Gamma _ { 3 } ^ { \nu } ) } \\ & { \quad _ { s } = \frac { 1 } { s ^ { 2 } } ( \Gamma _ { 3 } ^ { \nu } + 3 \Gamma _ { 3 } ^ { \nu } ) } \\ & { \quad _ { s } = \frac { 1 } { s ^ { 3 } } ( \Gamma _ { 3 } ^ { \nu } + 3 \Gamma _ { 3 } ^ { \nu } ) } \\ & { \quad _ { s } = \frac { 1 } { s ^ { 3 } } ( 8 P _ { 1 } + 2 0 P _ { 3 }  } \\ & { \quad _ { s } = \frac { 1 } { s ^ { 3 } } ( 8 P _ { 3 } - 2 8 P _ { 3 } + 2 7 P _ { 3 }  } \\ & { \quad  _ { s } = \frac { 1 } { s ^ { 3 } } ( 1 0 P _ { 4 } ^ { \nu } + 1 2 P _ { 2 } ^ { \nu } + 1 1 0 P _ { 4 } + 3 8 P _ { 6 } )  } \\ & { \quad _ { s } = \frac { 1 } { s ^ { 3 } } ( 1 0 P _ { 3 } + 6 8 P _ { 3 } + 1 8 P _ { 2 } 8 + 1 4 P _ { 3 }   } \\ & { \quad  _ { s } = \frac { 1 } { s ^ { 4 } } ( 8 P _ { 4 } + 3 P _ { 3 } + 8 P _ { 4 } + 2 0 P _ { 3 } + 1 4 P _ { 4 }    } \\ & { \quad   _ { s } = \frac { 1 } { s ^ { 3 } } ( 1 2 P _ { 3 } + 8 P _ { 2 } + 8 P _ { 3 } + 1 4 P _ { 3 }    } \\ & { \quad   _ { s } = \frac { 1 } { s ^ { 4 } } ( \Gamma _ { 4 } ^ { \nu } + 3 P _ { 4 }   } \end{array}
$$

# Bibliography

# This page intentionally left blank

Achieser, N.I.

1. Theory of Approximation,New York,1956.

Alexits, G. 1.Konvergenzprobleme der Orthogonalreihen,Budapest,1960.   
Aronszajn,N. 1.Introduction to the Theory of Hilbert Spaces,Stillwater,Oklahoma,1950. 2.Theory of Reproducing Kernels,Trans.Amer.Math.Soc.,vol.68 (1950), pp. 337-404.   
Banach, S. 1.Théorie des Opérations Linéaires,New York,1932.   
Behnke,H.and Sommer,F. 1.Theorie der Analytischen Funktionen einer Komplexen Veränderlichen, Berlin,1955.   
Bergman,S. 1.Sur les Fonctions Orthogonales,New York,1941. 2.The Kernel Function and Conformal Mapping,New York,1950.   
Bergman,S.and Schiffer,M. 1.Kernel Functions and Elliptic Differential Equations in Mathematical Physics,New York,1953.   
Bernstein,S. 1.Lecons sur les Proprietés Extremales,Paris,1926.   
Birkhoff,G.and Rota,G.C. 1. On the Completeness of Sturm-Liouville Expansions,Amer. Math. Mon., vol.67 (1960),pp.835-841.   
Boas,R. P., Jr. 1.Expansions of Analytic Functions, Trans. Amer. Math. Soc., vol.48 (1940), pp. 467-487. 2.Representation of Functions by Lidstone Series,Duke Math.J.,vol.10 (1943),pp.239-245. 3.Entire Functions,New York,1954. 4.A Primer of Real Functions,Rahway,New Jersey,1960.   
Boas,R.P.,Jr.and Buck,R.C. 1.Polynomial Expansions of Analytic Functions,Berlin,1958.   
Buck,R. C. 1.Interpolation Series,Trans.Amer.Math.Soc.,vol.64(1948)，pp.283-298. 2.Linear Spaces and Approximation Theory，pp.l1-23 of“On Numerical Approximation,”R.E.Langer,ed.,Madison,1959. 3.Survey of Recent Russian Literature on Approximation,in“On Numerical Approximation,”R.E.Langer,ed.,Madison,1959. 4.Bounded Continuous Functions on a Locally Compact Space,Michigan Math.Journal,vol.5(1958)pp.95-104. 5. Zero Sets for Continuous Functions,Proc．Amer.Math．Soc.，vol.1l, (1960),pp.630-633. 6.Studies in Modern Analysis,Vol．1,The Mathematical Association of America,1962.   
Clenshaw, C.W. 1.Chebyshev Series for Mathematical Functions,Math.Tables Series No.5, National Physical Laboratories, Her Majesty's Stationery Ofice, London, 1962.   
Cooke,R. G. 1.Infinite Matrices and Sequence Spaces,London,1950.   
Curry, H. B. 1.Abstract Differential Operators and Interpolation Formulas,Portugaliae Mathematica,vol.10 (195l),pp.135-162.   
Davis, P. J. 1. On Simple Quadratures,Pro.Amer.Math. Soc., vol.4 (1953),pp.127-136. 2.Errors of Numerical Approximation for Analytic Functions,Journal of Rational Mechanics and Analysis,vol.2 (1953),pp. 303-313. 3.On a Problem in the Theory of Mechanical Quadratures,Pac.J.Math., vol.5 (1955),pp.669-674.   
Davis,P.J.and Fan,K. 1.Complete Sequences and Approximations in Normed Linear Spaces,Duke Math. J.,vol. 24 (1957), pp.183-192.   
Davis,P.J.and Rabinowitz, P. 1.On the Estimation of Quadrature Errors for Analytic Functions,Math. Tables and Other Aids to Computation,vol.VIII (1954),pp.193-203. 2.Advances in Orthonormalizing Computation,Advances in Computers,vol. II,F.L.Alt,ed.,New York,1961.   
Day,M.M. 1.Normed Linear Spaces,Berlin,1958.   
Dickinson,D.J.,Pollak,H. O.,and Wannier,G.H. 1.On a Class of Polynomials Orthogonal Over a Denumerable Set,Pac.J. Math., vol.6 (1956),pp. 234-247.   
Dieudonn6, J. 1.Foundations of Modern Analysis,New York,1960.   
Dunford, N.and Schwartz,J. T. 1.Linear Operators,New York,1958.   
Eggleston,H.G. 1.Convexity,Cambridge,1958.   
Favard, J. 1． Sur les Polynomes de Tschebicheff,C.R. Acad. Sci. Paris,vol. 200 (1935), pp.2052-2053.   
Fejer,L. i. Uber die Lage der Nulltellen von Polynomen,die aus Minimumforderungen gewisser Art entspringen,Math.Ann., vol.85 (1922),pp.41-48.   
Fekete,M. 1. Uber den Transfiniten Durchmesser ebener Punktmengen, 3te Miteilung Math.Zeitschrift,vol. 37 (1933),pp.635-646.

Feldheim,M.E.

1. Théorie de la Convergence des Procédes d'interpolation et de Quadrature Mécanique,Paris,1939.

Franklin, P. 1.Functions ofa Complex Variable with Assigned Derivatives at an Infinite Number of Points...,Acta Mathematica,vol.47 (l926),pp.371-385.   
Gantmacher,F.R. 1.The Theory of Matrices,New York,1959.   
Gelfond, A. O. 1. Calculus of Finite Diferences, Moscow-Leningrad,l952. (In Russian)   
Golomb,M.and Weinberger,H.F. 1. Optimal Approximation and Error Bounds,pp.1l7-190 of “On Numerical Approximation,’R.E.Langer,ed.,Madison,1959.   
Gontscharoff,V.L. 1. Theory of Interpolation and Approximation of Functions,Moscow,1954. (In Russian)   
Halmos,P.R. 1.Introduction to Hilbert Space,New York,1951. 2．Naive Set Theory,New York,1960.   
Hardy,G.H.,Littlewood,J.E.,and P6lya,G. 1.Inequalities, Cambridge,1934.   
Hirschfeld,R.A. 1.On Best Approximations in Normed Vector Spaces,I,Nieuw Archief voor Wiskunde,vol. 3 (1958),pp.41-51. 2.On Best Approximations in Normed Vector Spaces,II,Nieuw Archief voor Wiskunde,vol.3 (1958),pp. 99-107.   
Hobson,E.W. 1. The Theory of Spherical and Ellipsoidal Harmonics,Cambridge,1931.   
Jackson, D. 1.The Theory of Approximation,New York,1930. 2.Fourier Series and Orthogonal Polynomials,Menasha,Wisconsin,1941.   
John, F. 1. A representation of Stieltjes integrals by conditionally convergent series, Amer.J.Math., vol. 59 (1937),pp.379-384.   
Kaczmarz,S.and Steinhaus,H. 1. Theorie der Orthogonalreihen,New York,1951.   
Knopp, K. 1. Theory and Application of Infinite Series,New York,1948.   
Kolmogorov,A.N.and Fomin,S.V. 1. Elements of the Theory of Functions and Functional Analysis, Rochester, New York,1957.

# Korovkin, P.

1.Sur une généralization de la série de Taylor,C.R.(Doklady) de l'Ac.des Sciences de l'URSS,vol. 14 (1937). 2.Linear Operators and Approximation Theory,Delhi,1960.

Kowalewski, G.

1.Interpolation und Genäherte Quadratur,Berlin,1932.   
2.Einfuhrung in die Determinantentheorie,New York,1948

# Krilov, V. I.

1.Approximate computation of Integrals,Moscow,1959.(In Russian)

Kuntzmann, J.

1.Méthodes Numériques,Paris,1959.

Landau,E.

1. Differential and Integral Calculus,New York,1951.

Langer,R.E.,ed. 1. On Numerical Approximation,Madison,1959.

Ljusternik,L.A.and Sobolew,W.I. 1.Elemente der Funktionalanalysis,Berlin,1955.

Lorentz, G. G. 1．Bernstein Polynomials,Toronto,1953.

Maehly,H.and Witzgall,C. 1.Tschebyscheff—Approximationen in Kleinen Intervallen I,Numerische Mathematik,vol.2(1960),pp.142-150. 2.Tschebyscheff—Approximationen in Kleinen Intervallen II,Numerische Mathematik,vol.2(1960),pp.293-307.

Markoff,A. A.

1.Differenzenrechnung,Leipzig,1896.

Mathematics Tables Project 1. Tables of Lagrangian Coefficients,New York,1944.

McShane,E.J.and Botts,T. 1.Real Analysis,Princeton,1959.

Milne,W. E.

1.The Remainder in Linear Methods of Approximation,N.B.S.Jour.of Research,vol.43 (1949),pp.501-511.

Motzkin,T. S.

1.Approximation by Curves of a Unisolvent Family,Bull.Amer. Math. Soc., vol. 55 (1949),pp.789-793.

Motzkin,T.S.and Walsh,J.L. 1.Least pth power polynomials on a real finite point set,Trans.Amer.Math. Soc.,vol. 78 (1955),pp.67-81.

Murnaghan,F.D.and Wrench,J.W., Jr.

1.The Approximation of Differentiable Functions by Polynomials,David Taylor Model Basin:Report 1175,1958,pp.1-52.

2.The Determination of the Chebyshev Approximating Polynomial for & Differentiable Function,Math.Tables and Other Aids to Comp.,vol.XIII (1959),pp.185-193.

Natanson, I. P.

1.Konstruktive Funktionentheorie,Berlin,1955.

National Bureau of Standards 1． Tables of Chebyshev Polynomials,Washington,1952.

Nehari, Zeev.

1. Conformal Mapping, New York, 1952.

Nikolsky, S. M.

1. On the problem of estimating the remainder in approximate quadrature formulas,Uspechi Mat.Nauk,vol.5 (1950),pp.165-177.

Norlund, N.E. 1.Vorlesungen über Differenzenrechnung,Berlin,1924.

Olmsted,J.M.H.

1.Completeness and Parseval's Equation，Amer.Math．Mon.，vol． LXV (1958),pp.343-345.

Paley,R.E.A.C.and Wiener,N. 1.Fourier Transforms in the Complex Domain,New York,1934.

Peano, G.

1.Resto Nelle Formule di Quadratura Espresso con un integrale Definito, Atti Della Reale Accademia Dei Lincei, Rendiconti (5),vol. 22 (1913),pp. 562-569.

2. Residuo In Formulas de Quadratura,Mathesis (4), vol. 34 (1914), pp. 5-10. P6lya, G.

1.Eine einfache,mit funktionentheoretischen Aufgaben verknüpfte,hinreichende Bedingung fur die Auflosbarkeit eines Systems unendlich vieler linearer Gleichungen. Commentarii Math. Helv.，vol.1l (1938-39)，pp. 234-252.

2.Sur l'existence de fonctions entieres satisfaisant & certaines conditions linéaires,Trans.Amer.Math.Soc.,vol.50 (194l),pp.129-139.

P6lya,G.and Szego,G. 1.Aufgaben und Lehrsätze aus der Analysis,New York,1945.

Rainville, E. D.

1. Special Functions,New York,1960.

Remez, E. Y.

1.Computational Methods for Tschebyscheff Approximation，Kiev，1957. (In Russian)

Trans.Amer. Math. Soc.,vol.96 (1960),pp.322-340. 2.Chebyshev Approximation by $a b ^ { x } + c , \mathbf { J }$ .Soc.Indust.Appl. Math., vol.8 (1960),pp.691-702. 3. Tchebycheff Approximations by Functions Unisolvent of Variable Degree, Trans. Amer.Math.Soc.,vol.99 (196l),pp.298-302.   
Riesz, F.and Sz.-Nagy,B. 1.Functional Analysis,New York,1955.   
Ritt, J. F. 1.On the Derivatives of a Function at a Point,Annals of Math.,vol.18 (1916), p. 18.   
Rivlin, T. J. 1.A Note on Smooth Interpolation,Siam Review,vol.2 (1960)，pp.27-30.   
Rivlin,T.J.and Shapiro,H.S. 1.A Unified Approach to Certain Problems of Approximation and Minimization, Journal of Soc.for Industrial and Applied Math., vol. 9, (1961), pp.670-699.   
Robin, L. 1.Fonctions Sphériques de Legendre et Fonctions Sphéroidales,vol. I-II, Paris,1957-1959.   
Rosenbloom,P.C.and Warschawski, S.E. 1.Approximation by Polynomials,in “Lectures on Functions of a Complex Variable,”W. Kaplan,ed.,Ann Arbor,1955.   
Rudin,W. 1.Principles of Mathematical Analysis,New York,1953.   
Salzer,H.E. 1. Some New Divided Difference Algorithms for Two Variables,in“On Numerical Approximation,”R.E.Langer,ed.,Madison,1959.   
Sansone, G. 1.Orthogonal Functions,New York,1959.   
Sard, A. 1.Integral Representations of Remainders,Duke Math. J.,vol. 15 (1948), pp.333-345. 2. Best Approximate Integration formulas； best approximation formulas, Amer.J. Math.,vol.71 (1949),pp.80-91.   
Schoenberg,I.J. 1. On Variation Diminishing Approximation Methods,pp.249-274 of“On Numerical Approximation,”R.E.Langer,ed.,Madison,1959.   
Schreier,O.and Sperner,E. 1. Modern Algebra and Matrix Theory.New York,1951.   
Sheffer, I. M. 1.Concerning some methods of best Approximation and the theorem of Birkhoff, Amer. J. Math., vol. 57 (1935),pp. 587-614.

1. On the Accuracy of Approximation to Given Functions By Certain Interpolatory Polynomials of Given Degree,Riveon Lematimatika,vol.8 (1954), pp.59-64.

Shohat,J.A. 1. Théorie Générale des Polynomes Orthogonaux de Tchebichef,Mémorial des Sciences Mathématiques,Fasc.66,Paris,1934.   
Shohat,J.A.,Hille,E.,and Walsh,J.L. 1.A Bibliography on Orthogonal Polynomials,Bull.Natl.Research Council (U.S.),vol. 103 (1940).   
Sommerville,D.M.Y. 1.An Introduction to the Geometry of $_ n$ -dimensions,New York,1958.   
Steffensen,J.F. 1.Interpolation,New York,1950.   
Stiefel,E. L. 1. Numerical Methods of Tchebycheff Approximation，pp. 217-232 of“On Numerical Approximation,”R.E.Langer,ed.,Madison,1959.   
Stroud,A. H. 1.A Bibliography on Approximate Integration,Math.of Computation,vol. 15 (1961),pp.52-80.   
Synge, J. L. 1.The Hypercircle in Mathematical Physics,Cambridge,1957.   
Szego, G. 1. Orthogonal Polynomials,New York,1959.   
Taylor,A. E. 1.Banach Spaces of Functions Analytic in the Unit Circle,I,Studia Mathematica,T.XI (1949),pp.145-170. 2.Banach Spaces of Functions Analytic in the Unit Circle,II, Studia Mathematica,T.XII (195l),pp.25-50. 3.Introduction to Functional Analysis,New York,1958.   
Thacher, H. C., Jr. 1.Numerical Properties of Functions of More than one Independent Variable, Annals of the New York Academy of Sciences,vol. 86 (1960),pp. 677-874.   
Tieman,A.F. 1. Theory of Approximation of Functions of a Real Variable, Moscow,1960. (In Russian)   
Titchmarsh,E.C. 1.The Theory of Functions,London,1939.   
Todd, J.,ed., 1.A Survey of Numerical Analysis,New York,1962.   
Tornheim, L. 1. On $\pmb { n }$ -parameter families of Functions and Associated Convex Functions, Trans.Amer.Math.Soc.,vol.69 (1950),pp.457-467.

Tricomi, F. G.

1.Vorlesungen über Orthogonalreihen,Berlin,1955.   
de la Vallee Poussin,G. 1.Lecons sur l'approximation des Fonctions d'une variable réelle,Paris,1919.   
Walsh, J. L. 1.Interpolation and Functions Analytic Interior to the Unit Circle,Trans. Amer.Math.Soc.,vol.34 (1932),pp.523-556. 2.Interpolation and Approximation by Rational Functions in the Complex Domain,Providence,Rhode Island,1956. 3.Approximation by Bounded Analytic Functions,Mémorial des Sciences Math.,vol. 144,Paris,1960.   
Walsh,J.L.and Davis,P.J. 1. Interpolation and Orthonormal Systems,J.d'Analyse Mathématique,vol. 2 (1952), pp. 1-28.   
Walsh,J.L.and Motzkin,T.S. 1.Best Approximations within a Linear Family on an Interval,Proc.Natl. Acad. Sci.,vol.46 (1960),pp.1225-1233.   
Ward,L.E.,Jr. 1.Linear Programming and Approximation Problems,Amer.Math.Mon., vol. 68 (1961), pp.46-52.   
Watson, G. N. 1.Theory of Bessel Functions, 2nd ed.,Cambridge,1958.   
Whittaker,J.M. 1.Interpolatory Function Theory,Cambridge,1935.   
Widder, D. V. 1．A Generalization of Taylor's Series,Trans.Amer.Math. Soc.,vol.30 (1927), pp. 126-154. 2.On the Expansion of Analytic Functions of the Complex Variable in Generalized Taylor's Series, Trans. Amer. Math. Soc., vol. 31 (1928), pp. 43-52. 3. Completely convex functions and Lidstone series, Trans. Amer. Math. Soc., vol. 51 (1942),pp.387-398.   
Young, J. W. 1.General Theory of Approximation by functions involving a given number of arbitrary parameters, Trans.Amer. Math. Soc., vol. 8 (l907),pp. 331- 344.   
Zaanen, A. C. 1.Linear Analysis,New York,1953.   
Zygmund,A. 1.Trigonometric Series,Cambridge,1959.

# Index

# This page intentionally left blank

Abel-Gontscharoff interpolation,28,52   
Abel-Gontscharoff polynomials,46   
Abel's theorem,104   
Abel-Dini, 220   
Achieser,52,155   
Alexits,255,339   
algebra,124   
algebraic conjugate space,16,18,22   
alternative theorem,2   
analytic configuration,69   
analytic functions, 12   
analytic functions,closure theorems, 273   
angle geometry,161   
Appel polynomials,48,53   
applications of Pólya's theorem,102   
approximants,Padé,53   
approximate integration,Gauss-Jacobi theory of,342   
approximation,78   
approximation, best,128,137 closeness of,128 degree of,328,333,334 least square, 158 simultaneous,112 Tschebyscheff, 146 uniform,107   
approximation by interpolation,118   
approximation of linear functionals, 341   
approximation theorem，Weierstrass, 24,107   
approximation under side conditions, 228   
Aronszajn,198,317,326   
average,moving,22   
axiom of choice,21

ball,open,189   
Banach,155,198,259,263,351   
Banach space,190   
basis,4   
Behnke,232,286,326   
Bergman,232,240,326   
Bergman kernel,319   
Bernoulli polynomials,47,48,53   
Bernstein,78,79,109,332,339   
Bernstein polynomials,108,126   
Bernstein polynomial,generalized,122   
Bessel inequality,172   
best approximation,128,137   
best approximation,   
measure of,328   
uniqueness of,140   
best approximation by nonlinear   
families,152   
best iniform approximation,146   
bilinear form,177   
biorthogonal expansion,44   
biorthonormal functionals,34   
biorthonormality theorem,41   
Birkhoff,G.,286   
Birkhoff,G.D.,283,286   
Boas,22,52,53,75,106,155,284,286   
Bohl, 356   
Bohnenblust,261   
Borel,104   
Botts,126   
bounded,function,5   
bounded linear functionals,214   
bounded triangular schemes,81   
Buck,52,53,126,286   
cardinal series,54   
Carleman,240,279   
Cauchy,268   
Cauchy-Hadamard theorem,15,90   
Cauchy integral formula,14   
Cauchy remainder,56   
Cauchy's theorem,13   
Cauchy sequence,190   
Cesaro summability,84,300   
Christoffel, 238   
Clenshaw,198   
closed sequence,257   
closed subspace,257   
closeness of approximation,128   
closure,188,190,257   
closure theorem,Mintz,267   
closure theorems for classes of analytic   
functions,273   
closure theorems of normed linear   
spaces,281   
co-dimension,225   
cofactor, 2   
coincident points,interpolation at,66   
complete inner product space,195,202   
complete normed linear space,202   
complete orthonormal sequence,202   
complete sequence,257   
complete set,194   
complete space,190,257   
completeness,257   
completeness of powers,265   
completeness of trigonometric systems,   
265   
complex Cartesian space,4   
complex orthogonal expansions,314   
complex orthogonal polynomials，239   
complex orthogonal polynomials,zeros   
of,245   
confocal ellipses,20   
confocal lemniscates,86   
conformal maps,19   
conjugate space,35   
conjugate space,   
algebraic,16,18,22   
normed,217   
continuity,modulus of,7   
continuous function,6   
continuous functional, 216   
convergence,   
strong,347   
weak,347   
convergence in norm,189   
convergence in the mean,189   
convergence of Legendre series,308   
convergence of quadrature processes,   
352   
convergence theorems,78   
convex,strictly,141   
convex functions,58   
convex hull,135   
convex hull theorem,Fejér's,244   
convex sets,134   
convex-functional,259   
Cooke,104   
Cramer's rule, 2   
Curry,53   
Narhouv 938   
Davis,198,232,286,360   
de La Vallée Poussin,155   
degree of approximation,328,333,334   
delta function,Dirac,323   
determinant,Vandermonde,24   
determinants,1   
Dickinson,255   
Dieudonné,126   
differences,successive,50   
differentiable functions,8   
dimension,4   
Dini's criterion,298   
Dirac delta function, 323   
Dirichlet kernel,295   
discrepancy,137   
divided differences,40,64   
divided differences,generalized,66   
du Bois-Reymond,300,360   
Duffin, 285   
Dunford,126,155

Eachus,285   
economization,Lanczos,174   
Eggleston,155   
element,minimal,197   
ellipses,confocal,20   
ellipses of convergence,90   
entire functions,15,22   
equations,normal,I75,176   
equidistributed sequences,354   
equioscillation theorem,Tschebyscheff, 149   
error,137   
error estimates,60,345   
error in linear interpolation,57,66   
errors,relative,199   
Euclidean geometry of $_ { n }$ dimensions, 198   
Euclidean space,202   
Euler-Lagrange differential equation, 323   
Euler-MacLaurin summation formula, 73   
expansion,biorthogonal,44   
expansion theorems,orthogonal functions,290   
expansions, complex orthogonal,314 Fourier,169 Tschebyscheff,198   
expansions in Legendre polynomials, 90   
extended Parseval identity,192   
extension,257   
Faber,78   
factorization theorem,16   
Fan,286   
Farrell, 279   
Fatou's lemma, 232   
Favard, 255   
Fejer,79,118,243,255,300,358   
Fejér kernel, 302   
Fejer norm,243   
Fejér's convex hull theorem, 244   
Fejer's principle,243,255   
Fejer's theory of Fourier series,299   
Fejer scheme,126   
Fejer sums,302   
Fekete,93   
Feldheim,360   
finite interpolation,26,226   
finite Newton series,41   
foci,86   
Fomin,155   
Fort,53   
forward difference formulas,Newton's, 52   
Fourier coefficients,169   
Fourier expansions,169   
Fourier expansions,minimum properties of,171   
Fourier series,29,169,170,290   
Fourier series,Fejer's theory of,299   
Fourier series of periodic analytic functions,305   
Franklin,104   
Frechet-Riesz theorem,218   
function,generating,48   
function bounded,5   
function continuous,6   
function,uniformly continuous,6   
functional, 17   
functional, continuous,216 linear,17 positive,71   
functionals, biorthonormal,34 linear,16 norms of,345   
functions, ohnvav 58 differentiable,8 entire,15,22 infinitely differentiable,11,22 linear spaces of,4 regular,12 weight,49   
functions,analytic,12   
fundamental polynomials,34   
fundamental problem of linear approximation,136   
fundamental theorem of algebra,16   
fundamental theorem of orthonormal expansions,191

Gantmacher,198   
Gauss,343   
gauge curve,136   
Gauss formula of trigonometric inter  
polation,38   
Gauss-Jacobi theory of approximate   
integration, 342   
Gauss 10 point rule,346   
Gauss 16 point rule,346   
Gauss 7 point rule,346   
Gelfand,53   
general Fejér kernels,303   
general polynomials,series of,108   
general remainder theorem,75   
generalizations of Weierstrass theorem,   
122   
generalized Bernstein polynomial,122   
generalized divided differences,66   
generalized Gram determinant,27   
generalized Newton representation,41   
generalized Rolle's theorem,9   
generalized Taylor interpolation,28,52   
generating function,48,253   
Golomb,232,326,360   
Gontscharoff,52,93,126   
Gram determinant,generalized,27   
Gram determinant,geometrical inter  
pretation,186   
Gram determinant properties,184   
Gram determinants,176   
Gram matrices,176   
Gram's criterion,180   
Gram-Schmidt orthonormalizing pro  
cess,165   
Grassman outer product,200   
Green's function,72,322   
Guage curve,136   
Guichard's theorem,96   
Haar,32   
Haar's theorem,52   
Hadamard's determinant inequality,   
180   
Hahn,259   
Hahn-Banach extension theorem,257   
Halmos,22,198   
Hardy,75   
Heine,310   
Hermite,68   
Hermite interpolation,28   
Hermite polynomials,168   
Hermite's interpolation,52   
Hermitian symmetry,158   
Hilbert,93   
Hilbert matrix,288   
Hilbert space,201,202.   
Hilbert space,   
separable,203   
sequential,204   
Hille,255   
Hirschfeld,155   
Hobson,326,360   
Holder's inequality,131   
hypercircle,229   
hypercircle inequality,230   
hyperplane,normal form,229   
hyperplanes,225   
indefinite inner product space,200   
infinite dimensional space,4   
infinite interpolation,95   
infinite systems of linear equations,97   
infinitely differentiable functions,11,   
22   
inner product,158   
inner product space,l58,202   
inner product space,indefinite,200   
inner product spaces,complete,195   
integral remainder for linear interpola  
tion,72   
integrals,mean value theorem for,7   
interior,189

interpolation,24   
interpolation, Abel-Gontscharoff,28,52 finite,26,226 Gauss formula of trigonometric,38 generalized Taylor,28,52 Hermite,28,52 infinite,95 Lidstone,28,52 osculatory,28,36 polynomial, 24 Taylor,28,36 trigonometric,29,52 two point Taylor,37   
interpolation at coincident points,66   
interpolation at discrete points,28   
interpolation formula,Lagrange,33   
interpolation in linear spaces,75   
interpolation property,27   
interpolation schemes,triangular,79   
interpolation series,80   
interpolatory processes,78   
isometric spaces,222   
isometric transformation,233   
isomorphic spaces,222

Jackson,255,326,335,338,339   
Jackson's kernel,340   
Jacobi,343   
Jacobi polynomials,168,246,251   
John,360   
Jordan curve,273

Kaczmarz,198,286   
Keldysch,278   
kernel, Bergman,319 Dirichlet,295 Fejer,302 Jackson,340 Peano,70,323 Poisson,308 reproducing,316   
kernel for Simpson's rule,74   
kernel function unit circle,321   
kernel polynomial,237,251,252   
kernels,general Fejér,303   
Kolmogorov, 155

Korovkin,93,126,336,339   
Kowalewski,198   
Kowalewski's exact remainder,71   
Kowalewski's remainder,76   
Krilov,360   
Kuntzmann,76   
Lagrange identity,199   
Lagrange interpolation formula,33   
Laguerre polynomials,168   
Lanczos,76   
Lanczos economization, 174   
Landau,220   
Laplace,310   
lattice hull, 124   
Lauricella,264   
Lavrentieff, 278   
law of cosines,162   
least square approximation, 158   
least square methods,198   
least square problems,171   
least squares data fitting,140   
Lebesgue,123,351   
Lebesgue constants,351   
Legendre function of the second kind,   
311   
Legendre polynomials,83,168,184,   
246   
Legendre polynomials,   
expansions in, 90   
table of,369   
Legendre series,convergence of, 308   
lemniscate of Bernoulli, 86   
lemniscates,83,86   
lemniscates,confocal,86   
Lemoine point,199   
Lidstone interpolation,28,52   
limit,189   
linear approximation,fundamental   
problem of,136   
linear combination,3   
linear differential equation,251   
linear equations,infinite systems of,97   
linear functional,16,17   
linear functionals,   
approximation of,341   
bounded, 214   
linear interpolation,   
error in,57,66   
integral remainder for,72   
linear manifold,176   
linear operators,351   
linear space,202   
linear spaces,interpolation in,75   
linear spaces of functions,4   
linear systems of equations,2   
linear varieties,225   
linear vector space,3   
linearly dependent,3   
Lipschitz condition,8   
Littlewood,75   
Ljusternik,155,360   
Lorentz,126   
LU-decomposition,44   
Maehly,155   
Marcinkiewicz,79   
Markoff,52,344,360   
maximum principle,15   
McShane,126   
mean value theorem,9,65   
mean value theorem for integrals,7   
mean values,64   
measure of best approkimation，328   
Méray,78   
Mergelyan,278   
metric space,130   
Milne,53,76   
minimal element,197   
minimum properties ofFourier   
expansions,171   
minimum property of orthogonal   
elements,172   
Minkowski inequality,l30,132   
Minkowski plane,135   
minor,2   
Mittag-Leffler's theorem,96   
modulus of continuity,7,22   
moment problem,227   
moments,48   
monotonic norm,243   
Motzkin,52,155   
moving average,22   
Mintz,270,272   
Mintz closure theorem,267   
Murnaghan,155,198   
NataIl3on,1zo,1əə,zəə,z80,3əy   
National Bureau of Standards,76,255   
Nehari,232,255,326   
neighborhood,93   
Neumann,312   
Newton formula,39   
Newton polynomials,46   
Newton representation,generalized,41   
Newton's forward difference formulas,   
52   
Newton series,52,53   
Newton series,finite,41   
Nikolsky,360   
nonharmonic oscillations,285   
nonlinear families,best approximation   
by,152   
Norlund,53   
norm,129   
norm,   
square,130   
uniform,133   
weighted square,134   
normal equations,175,176   
normal form,hyperplane,229   
normed conjugate space,217   
normed linear space,202   
normed linear spaces,129   
normed linear spaces,closure theorems,   
281   
norms of functionals,345   
orthonormal systems,163   
orthonormalizing process,Gram-  
Schmidt,165   
osculatory interpolation,28,36   
Osgood,351   
ovals of Cassini,86   
over-determined system,l40,199

Padé approximants, 53   
Paley,284   
parallel elements,161   
parallelogram theorem,161   
parallelotope,volume of,187   
Parseval identity,191,267   
Parseval identity,extended,192   
Peano,70,76   
Peano kernel,70,323   
Peano's theorem,69,76   
periodic analytic functions,Fourier series of,305   
permanence property,41,173   
perpendicular elements,162   
Poincaré,105   
Poisson kernel, 308   
Pollak,255   
P6lya,52,75,104,351,353,360   
P6lya's theorem,98   
Polya's theorem,applications of,102   
polynomial, kernel,237,251,252 trigonometric,29   
polynomial interpolation,24   
polynomial interpolation,remainder for,67   
polynomials,15   
polynomials, Abel-Gontscharoff,46 Appel,48,53 Bernoulli,47,48,53 Bernstein,108,126 fundamental, 34 Hermite,168 Jacobi,168,246 Laguerre,168 Legendre,83,168,184,246 Newton, 46 orthogonal,48,234 Tschebyscheff,60,63,163,240,24   
Olmstead,198   
open ball, 189   
orthogonal complement,223   
orthogonal elements,162   
orthogonal elements,minimum property of,172   
orthogonal functions,expansion theorems,290   
orthogonal polynomials,48,234   
orthogonal polynomials, complex,239 short guide to,364 zeros of,236   
orthogonal set,163   
orthonormal expansions,fundamental theorem of,191   
orthonormal set,35

Rota,286   
Rudin,232   
Runge,78,273,275,278

polynomials,(contd.) ultraspherical,246   
Positive functional,71   
powers,completeness of,265   
powers as combinations of Legendre polynomials,369   
powers as combinations of Tschebyscheff polynomials,368   
principle of localization,Riemann,298   
Pringsheim,14   
projection,162,223   
Pythagorean theorem,162,164

quadrature processes,convergence of, 352

Salzer,52   
Sansone,255   
Sard,76,360   
scalar product, 3   
Schafke, 285   
Schiffer,232,326   
Schoenberg,126   
Schreier,22,187   
Schwartz,126,155   
Schwarz inequality,134,159   
seminormed space,156   
separable metric space,190   
separable Hilbert space,203   
separable space,203   
separation of the plane, 278   
sequence,complete,257   
sequence,closed,257   
sequences,equidistributed,354   
sequential Hilbert space,204   
series, cardinal,54 Fourier,29,169,170,290 interpolation,80 Newton,52,53 Tschebyscheff-Fourier,170   
Series of general polynomials,108   
set, complete,194 convex,134 orthonormal,35   
Shapiro,155   
Sheffer,52,53   
Shisha,126,256   
Shohat,255   
short guide to orthogonal polynomials 364   
Sierpinski, 356   
Simpson's rule,341,346   
Simpson's rule, kernel for,74 remainder in,74   
simultaneous approximation,112   
simultaneous interpolation and approximation,121

Rabinowitz,198,360   
Rainville,53,326   
ramification point,32   
real Cartesian space,4   
recurrencerelation,6l,253   
recurrence relationship,234   
regular functions,12   
regularlyarranged,44   
relative errors,199   
remainder,   
Cauchy,56,   
Kowalewski's,76   
remainder for polynomial interpola  
tion,67   
remainder in Simpson's rule,74   
remainder theorem，Young's form,10   
remainder theory,56   
Remez,155   
representer,218   
reproducing kernel,316   
reproducing property,237,317   
Rice,155   
Riemann derivative,23   
Riemann-Lebesgue theorem,296   
Riemann principle of localization,298   
Riemann's theorem,173   
Riesz,155,194   
Ritt,104   
Rivlin,155   
Rodrigues'formula,246   
Rolle's theorem,9   
Rolle's theorem,generalized,9

DUvUzyK, zU1   
Sobolew,155,360   
Sommer,232,286,326   
Sommerville,198   
space, complete,190,257 complex Cartesian,4 Hilbert,201 infinite dimensional,4 metric,130 real Cartesian,4 seminormed,156 separable,203   
spaces, complete inner product,195 inner product,158 isometric,222 isomorphic,222 normed linear,129   
special function theory,246   
Sperner,22,187   
square norm,130   
Steinhaus,198,286   
Stekloff, 353   
Stiefel, 155   
Stieltjes,353   
Stone,126   
Stone-Weierstrass theorem，l23,125, 126   
strictly convex,141   
strong convergence,347   
Stroud,360   
subspace,closed,257   
successive differences,50   
Suchomlinoff, 261   
summability,Cesaro,84,300   
symmetry,Hermitian,158   
Synge,198,232   
systems of equations,linear, 2   
Sz.Nagy,155   
Szasz,282   
Szego,52,198,240,255,326,360   
table of Legendre polynomials,369   
table of Tschebyscheff polynomials,

367 Takenaka,255 Taylor,22,155

uy IvI μIvvI pUIWvIUI U,v   
Taylor interpolation,two point,37   
Taylor's theorem,10   
Tieman,22,339   
Tonelli, 143   
transformation,isometric,233   
trapezoidal rule,73,346   
trapezoidal rule for differential equations,341   
triangular interpolation schemes,79   
triangular schemes,bounded,81   
Tricomi,255,326   
trigonometric interpolation,29,52   
trigonometric interpolation; Gauss formula,38   
trigonometric polynomial,29   
trigonometric systems,completeness of,265   
Tschebyscheff,62   
Tschebyscheff approximation,139,146   
Tschebyscheff equioscillation theorem, 149   
Tschebyscheff expansions,198   
Tschebyscheff-Fourier series,170   
Tschebyscheff polynomial for S,146   
Tschebyscheff polynomials,60,63,76, 78,163,240,246   
Tschebyscheff polynomials, powers as combinations of,368 table of,367   
Tschebyscheff polynomials,first kind, 168   
Tschebyscheff polynomials,second kind,164,168,241   
Tschebyscheff zeros,79   
two point Taylor interpolation,37

ultraspherical polynomials,246   
uniform approximation,107   
uniform approximation,best,146   
uniform norm, 133   
uniformly continuous function,6   
uniqueness of best approximation,140   
uniqueness theorem,16   
unisolvence,31   
unisolvent systems,52   
unit circle,kernel function,321   
unit vectors,4   
Vandermonde determinant,24   
Vitali,324,351   
volume of parallelotope,187   
Voronovsky,117

Walsh,76,92,93,121,126,155,232 255,277,278,279,286,339   
Wannier, 255   
Ward,155   
weak convergence,347   
weak\*convergence,346   
Weierstrass approximation theorem, 24,107   
Weierstrass product theorem,96   
Weierstrass theorem,generalizations of,122,188   
weight functions,49   
weighted square norm,134   
Weinberger,232,326,360

Weyl, 356   
Whittaker, 52,53   
Widder, 52, 53   
Wiener, 284   
Witzgall, 155   
Wrench,155,198   
Wronskian,30   
Young, 155   
Young's criterion,156   
Young's form,remainder theorem,10   
Zaanen,155   
zeros of complex orthogonal   
polynomials,245   
zeros of orthogonal polynomials,236   
Zorn's lemma,21,22   
Zygmund,52,326,339