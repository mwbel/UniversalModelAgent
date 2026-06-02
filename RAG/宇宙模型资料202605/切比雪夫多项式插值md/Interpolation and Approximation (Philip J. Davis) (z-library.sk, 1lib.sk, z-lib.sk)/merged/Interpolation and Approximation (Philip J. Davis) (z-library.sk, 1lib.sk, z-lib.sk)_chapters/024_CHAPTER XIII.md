# CHAPTER XIII

# Degree of Approximation

13.1 The Measure of Best Approximation. Let $\pmb { X }$ be a normed linear space and $\left\{ x _ { i } \right\}$ a sequence of independent elements. For an arbitrary $y \in X$ ,there is a best approximation to $_ y$ from among the linear combinations of $x _ { 1 } , x _ { 2 } , \ldots , x _ { n }$ ，and we have already defined the measure of best approximation by means of

$$
{ E } _ { n } ( y ) = \operatorname* { m i n } _ { a _ { i } } \left\| y - \sum _ { i = 1 } ^ { n } a _ { i } x _ { i } \right\| .
$$

(See (7:4.1l).) We know that $E _ { 1 } \geq E _ { 2 } \geq \cdots \geq 0$ 、The limit is O if and only if $_ y$ can be approximated arbitrarily closely by combinations of ${ \pmb x _ { 1 } } ,$ $\pmb { x } _ { 2 } , \ldots .$ Hence we have (cf.Theorem 7.6.1)

cTeon 1 13.1.1. $\operatorname* { l i m } _ { n \to \infty } ~ E _ { n } ( y ) = 0$ for all $y \in X$ if and omly if $\left\{ x _ { i } \right\}$ i8 $\pmb { X }$

In the present chapter, the rapidity with which $ { { \cal E } } _ { n } ( y )$ approaches zero will be studied.

Ex.1．The quantities $E _ { n } ( y )$ are computed easily when $x$ is an inner product space.Assuming,as we may,that we have orthonormalized the $\{ x _ { i } \}$ to yield $\{ x _ { i } ^ { * } \}$ ,then by Corollary 8.5.3,

$$
{ E _ { n } } ^ { 2 } ( y ) = \| y \| ^ { 2 } - \sum _ { k = 1 } ^ { n } { \big | } ( y , { x _ { k } } ^ { * } ) { \big | } ^ { 2 } .
$$

If $x$ is a Hilbert space and $\{ x _ { i } ^ { * } \}$ is complete and orthonormal, then by Theorem 8.9.1 (C),

$$
{ E _ { n } } ^ { 2 } ( y ) = \sum _ { k = n + 1 } ^ { \infty } \big | ( y , x _ { k } * ) \big | ^ { 2 } .
$$

Note that in the Hilbert space situation, $ { \boldsymbol { E } } _ { n } ( y )$ may approach zero with arbitrary rapidity. For let $\pmb { \varepsilon _ { 1 } } , \pmb { \varepsilon _ { 2 } }$ be an arbitrary nonincreasing sequence of nonnegative numbers with $\operatorname* { l i m } _ { n \to \infty } \varepsilon _ { n } = 0$ . Set

$$
a _ { 1 } = { \sqrt { { \varepsilon _ { 1 } } ^ { 2 } - { \varepsilon _ { 2 } } ^ { 2 } } } , a _ { 2 } = { \sqrt { { \varepsilon _ { 2 } } ^ { 2 } - { \varepsilon _ { 3 } } ^ { 2 } } } , . . . . .
$$

Then,

$$
\sum _ { i = 1 } ^ { \infty } a _ { i } { } ^ { 2 } = ( \varepsilon _ { 1 } { } ^ { 2 } - \varepsilon _ { 2 } { } ^ { 2 } ) + ( \varepsilon _ { 2 } { } ^ { 2 } - \varepsilon _ { 3 } { } ^ { 2 } ) + \cdot \cdot \cdot = \varepsilon _ { 1 } { } ^ { 2 } < \infty .
$$

Hence, there is an element $_ y$ with Fourier coefficients $\left\{ a _ { i } \right\}$ .Now,

$$
{ E _ { n } } ^ { 2 } ( y ) = \sum _ { k = n + 1 } ^ { \infty } ( { \varepsilon _ { k } } ^ { 2 } - \varepsilon _ { k + 1 } ^ { 2 } ) = \varepsilon _ { n + 1 } ^ { 2 } .
$$

The arbitrary approach to zero holds in a Banach space as well. The proof is somewhat more involved and preliminary work is necessary.

THEOREM 13.1.2. The quantities ${ \pmb { { \cal E } } } _ { n } ( y )$ have the following properties

$$
\begin{array} { l } { \displaystyle E _ { n } ( y + \sum _ { i = 1 } ^ { n } b _ { i } x _ { i } ) = E _ { n } ( y ) . } \\ { \displaystyle E _ { n } ( y + z ) \leq E _ { n } ( y ) + E _ { n } ( z ) } \\ { \displaystyle E _ { n } ( \sigma y ) = | \sigma | E _ { n } ( y ) . } \\ { \displaystyle E _ { n } ( y - z ) \geq | E _ { n } ( y ) - E _ { n } ( z ) | } \end{array}
$$

${ E } _ { n } ( y + \sigma z )$ is $^ { \pmb { a } }$ continuous function of $\pmb { \sigma }$ 1f $\pmb { \sigma }$ is real, it is a convex function. If $\bar { E } _ { n } ( z ) > 0$ ， $\operatorname* { l i m } _ { | \sigma |  \infty } E _ { n } ( y + \sigma z ) = \infty .$ （

$\operatorname * { d } \ E _ { n } ( y ) = \ \left\| y - \sum _ { i = 1 } ^ { n } a _ { i } x _ { i } \right\| .$

$$
\begin{array} { l } { { \displaystyle { \cal E } _ { n } \bigg ( y + \sum _ { i = 1 } ^ { n } b _ { i } x _ { i } \bigg ) = \operatorname* { m i n } _ { c _ { i } } \bigg \| y + \sum _ { i = 1 } ^ { n } b _ { i } x _ { i } - \sum _ { i = 1 } ^ { n } c _ { i } x _ { i } \bigg \| } } \\ { { \displaystyle ~ = \operatorname* { m i n } _ { c _ { i } } \bigg \| y - \sum _ { i = 1 } ^ { n } ( c _ { i } - b _ { i } ) x _ { i } \bigg \| = { \cal E } _ { n } ( y ) } . } \end{array}
$$

(3). If $E _ { n } ( y ) = \left\| y - \sum _ { i = 1 } ^ { n } b _ { i } x _ { i } \right\|$ and $\displaystyle { E _ { n } ( z ) = \bigg \| z - \sum _ { i = 1 } ^ { n } c _ { i } x _ { i } \bigg \| } ,$ then by he $\begin{array} { r l } & { \mathrm { n g l e ~ i n e q u a l i t y ~ f o r ~ n o r m s , \left\| ~ ( \it y + z ) - \sum _ { i = 1 } ^ { n } ( b _ { i } + c _ { i } ) x _ { i } \right\| \leq { E _ { n } } ( y ) + { E _ { n } } ( z ) . } } \\ & { ; { E _ { n } } ( y + z ) = \displaystyle \operatorname* { m i n } _ { a _ { i } } \left\| ~ ( y + z ) - \sum _ { i = 1 } ^ { n } a _ { i } x _ { i } \right\| \leq \left\| ~ ( y + z ) - \sum _ { i = 1 } ^ { n } ( b _ { i } + c _ { i } ) x _ { i } \right\| . } \end{array}$ (4). $\operatorname { L e t } E _ { n } ( y ) = \left\| y - \sum _ { i = 1 \ldots } ^ { n } a _ { i } x _ { i } \right\| ,$ Then, $\left| \sigma \right| E _ { n } ( y ) = \left\| \ \sigma y - \sum _ { i = 1 } ^ { n } \sigma a _ { i } x _ { i } \right\| \geq E _ { n } ( \sigma y ) .$

It follows that if $\sigma \neq 0 , \ E _ { n } ( y ) = E _ { n } \left( { \frac { \sigma y } { \sigma } } \right) \leq { \frac { 1 } { | \sigma | } } \ E _ { n } ( \sigma y )$ .Hence $E _ { n } ( \sigma y ) \geq$ $| \sigma | \ B _ { n } ( y )$ . Combining these yields (l3.1.4).If ${ \pmb \sigma } = { \bf 0 }$ the statement is trivial. (5). $E _ { n } ( y ) = E _ { n } ( z + y - z ) \leq E _ { n } ( z ) + E _ { n } ( y - z )$ .Hence, $\bar { E } _ { n } ( y - z ) \geq$ ${ \pmb E _ { n } } ( y ) - { \pmb E _ { n } } ( z )$ .Similarly, ${ \cal E } _ { n } ( y - z ) = { \cal E } _ { n } ( z - y ) \geq { \cal E } _ { n } ( z ) - { \cal E } _ { n } ( y )$

(6).By (13.1.5),

$$
| E _ { n } ( y + \sigma _ { 1 } z ) - E _ { n } ( y + \sigma _ { 2 } z ) | \leq E _ { n } ( ( \sigma _ { 1 } - \sigma _ { 2 } ) z ) = | \sigma _ { 1 } - \sigma _ { 2 } | E _ { n } ( z ) .
$$

Continuity follows from this.Let $0 \leq t \leq 1$ . Then

$$
\begin{array} { r l } & { E _ { n } ( y + ( t \sigma _ { 1 } + ( 1 - t ) \sigma _ { 2 } ) z ) = E _ { n } ( t ( y + \sigma _ { 1 } z ) + ( 1 - t ) ( y + \sigma _ { 2 } z ) ) } \\ & { \qquad \leq t E _ { n } ( y + \sigma _ { 1 } z ) + ( 1 - t ) E _ { n } ( y + \sigma _ { 2 } z ) , } \end{array}
$$

and this implies convexity. Finally,

$$
{ E } _ { n } ( y + \sigma z ) \geq { E } _ { n } ( \sigma z ) - { E } _ { n } ( y ) = | \sigma | { E } _ { n } ( z ) - { E } _ { n } ( y ) .
$$

If

$$
E _ { n } ( z ) \neq 0 , \operatorname* { l i m } _ { | \sigma |  \infty } E _ { n } ( y + \sigma z ) = \infty .
$$

LEMMA 13.1.3． Let $\pmb { X }$ be $^ { \pmb { a } }$ normed linear space and $x _ { 1 } , x _ { 2 } , \dotsc , a$ sequence ofindependent elements.For arbitrary $\pmb { x } \in \pmb { X }$ write

$$
E _ { j } ( { \boldsymbol { x } } ) = \operatorname* { m i n } _ { \boldsymbol { a _ { i } } } \left\| { \boldsymbol { x } } - \sum _ { i = 1 } ^ { j } a _ { i } x _ { i } \right\| .
$$

If e is a number that satisfes $e \geq E _ { j + 1 } ( x )$ , we can find a o such that

$$
E _ { j } ( x + \sigma x _ { j + 1 } ) = e .
$$

Prof:Suposetate ${ \cal E } _ { j + 1 } ( x ) = \left\| \ x - \sum _ { i = 1 } ^ { j + 1 } a _ { i } x _ { i } \right\| .$ Then,

$$
\begin{array} { c l } { { } } & { { { \stackrel { , } { _ { j } } } ( x - a _ { j + 1 } x _ { j + 1 } ) = \displaystyle \operatorname* { m i n } _ { b _ { i } } \left\| x - a _ { j + 1 } x _ { j + 1 } - \sum _ { i = 1 } ^ { j } b _ { i } x _ { i } \right\| \leq \left\| x - \sum _ { i = 1 } ^ { j + 1 } a _ { i } x _ { i } \right\| = E _ { j + 1 } ( x ) } } \\ { { } } & { { { } } } \\ { { } } & { { = E _ { j + 1 } ( x - a _ { j + 1 } x _ { j + 1 } ) \leq \left( \mathrm { b y } \left( 7 . 4 . 1 2 \right) \right) E _ { j } ( x - a _ { j + 1 } x _ { j + 1 } ) . } } \end{array}
$$

Henee $; E _ { j } ( x - a _ { j + 1 } x _ { j + 1 } ) = E _ { j + 1 } ( x ) . \mathrm { N o w } E _ { j } ( x _ { j + 1 } ) = \operatorname* { m i n } _ { a _ { i } } \left\| x _ { j + 1 } - \sum _ { i = 1 } ^ { j } a _ { i } x _ { i } \right\| > 0 ,$ otherwise the $_ { \pmb { x } }$ s would be dependent.Hence,by (l3.1.6) we can find a ${ \pmb \sigma } ^ { \prime }$ such that $E _ { j } ( x + \sigma ^ { \prime } x _ { j + 1 } ) > e$ Thus, $E _ { j } ( x - a _ { j + 1 } x _ { j + 1 } ) \leq e < E _ { j } ( x + \sigma ^ { \prime } x _ { j + 1 } ) .$ By the continuity property (l3.l.6), the proper $\pmb { \sigma }$ can be found.

THEOREM 13.1.4. Let X be a normed linear space and x1, xz,..,xn, Xn+1 a sequence of independent elements.If $e _ { 1 } \geq e _ { 2 } \geq \cdot \cdot \cdot \geq e _ { n } \geq 0$ are prescribed, we can find a linear combination

$$
y = b _ { 1 } x _ { 1 } + b _ { 2 } x _ { 2 } + \cdot \cdot \cdot + b _ { n } x _ { n } + b _ { n + 1 } x _ { n + 1 }
$$

such that

$$
E _ { k } ( y ) = e _ { k } \qquad k = 1 , 2 , \ldots , n
$$

and

$$
\| y \| = e _ { 1 } .
$$

Proof: Since $E _ { n + 1 } ( 0 ) = 0$ ，there is,by Lemma l3.1.3,aconstant $b _ { n + 1 }$ such that

$$
E _ { n } ( 0 + b _ { n + 1 } x _ { n + 1 } ) = e _ { n } .
$$

Since $e _ { n - 1 } \geq e _ { n }$ ,there is,by the Lemma,a $b _ { n }$ such that

$$
\begin{array} { r } { E _ { n - 1 } ( b _ { n } x _ { n } + b _ { n + 1 } x _ { n + 1 } ) = e _ { n - 1 } . } \end{array}
$$

By (13.1.2), $E _ { n } ( b _ { n } x _ { n } + b _ { n + 1 } x _ { n + 1 } ) = E _ { n } ( b _ { n + 1 } x _ { n + 1 } ) = e _ { n } .$ Since $e _ { n - 2 } \geq e _ { n - 1 }$ there is a $\pmb { b _ { n - 1 } }$ such that

$$
E _ { n - 2 } ( b _ { n - 1 } x _ { n - 1 } + b _ { n } x _ { n } + b _ { n + 1 } x _ { n + 1 } ) = e _ { n - 2 } .
$$

$$
\begin{array} { r } { E _ { n - 1 } ( b _ { n - 1 } x _ { n - 1 } + b _ { n } x _ { n } + b _ { n + 1 } x _ { n + 1 } ) = E _ { n - 1 } ( b _ { n } x _ { n } + b _ { n + 1 } x _ { n + 1 } ) = e _ { n - 1 } , } \end{array}
$$

$$
E _ { n } ( b _ { n - 1 } x _ { n - 1 } + b _ { n } x _ { n } + b _ { n + 1 } x _ { n + 1 } ) = E _ { n } ( b _ { n + 1 } x _ { n + 1 } ) = e _ { n } .
$$

Continuing in this way, we can find an element $z = b _ { 2 } x _ { 2 } + \cdot \cdot \cdot + b _ { n + 1 } x _ { n + 1 }$ such that

$$
E _ { n } ( z ) = e _ { n } , E _ { n - 1 } ( z ) = e _ { n - 1 } , . . . , E _ { 1 } ( z ) = e _ { 1 } .
$$

Now $e _ { 1 } = E _ { 1 } ( z ) = \operatorname* { m i n } _ { b } \ \| b _ { 2 } x _ { 2 } + \cdot \cdot \cdot + b _ { n + 1 } x _ { n + 1 } - b x _ { 1 } \|$ . Select a $^ { b }$ that yields the minimum value. Call it $- b _ { \mathbf { 1 } }$ . Then if $y = b _ { 1 } x _ { 1 } + b _ { 2 } x _ { 2 } + \cdot \cdot \cdot + b _ { n + 1 } x _ { n + 1 } ,$ conditions (13.1.9-10) hold.

LEMMA 13.1.5. Let $\pmb { K }$ be a bounded subset of $\pmb { a }$ normed linear space $\pmb { X }$ Suppose that $\pmb { X }$ has finite dimension $\pmb { N }$ .If $\left\{ y _ { k } \right\}$ is an arbitrary sequence of elements of $\pmb { K }$ ， we may find $^ { \pmb { a } }$ subsequence $y _ { k _ { 1 } } , y _ { k _ { 2 } } , \dotsc .$ , that converges to an element $y \in X \colon \operatorname* { l i m } _ { n \to \infty } \| y - y _ { k _ { n } } \| = 0$ 1f $\pmb { K }$ isclosed, $y \in K$ ，and $\pmb { \kappa }$ is said to be sequentially compact.

Proof: Let ${ \pmb x } _ { 1 } , { \pmb x } _ { 2 } , \ldots , { \pmb x } _ { N }$ be a set of independent elements of $\pmb { X }$ Then the elements $\pmb { x }$ of $\pmb { K }$ satisfy $\| x \| = \| a _ { 1 } x _ { 1 } + \cdot \cdot \cdot + a _ { N } x _ { N } \| \le M$ for some $M$ Employing the notation of the proof of Theorem 7.4.l,we have from (7.4.6), $M \geq \| x \| \geq m r , r = ( | a _ { 1 } | ^ { 2 } + \cdot \cdot \cdot + | a _ { N } | ^ { 2 } ) ^ { \frac { 1 } { 2 } }$ ,for every ${ \pmb x } \in { \pmb K }$ .The coefficients of elements of $\pmb { K }$ satisfy $( | a _ { 1 } | ^ { 2 } + \cdot \cdot \cdot + | a _ { N } | ^ { 2 } ) ^ { \frac { 1 } { 2 } } \leq M / m$ ，and in particular, $| a _ { j } | \leq M / m$ I $y _ { k } = \sum _ { i = 1 } ^ { N } a _ { i } ^ { ( k ) } x _ { i } .$ then $| a _ { j } ^ { ( k ) } | \leq M / m , j = 1 , \ldots , N$ and th points $P _ { k } \colon ( a _ { 1 } ^ { ( k ) } , a _ { 2 } ^ { ( k ) } , \ldots , a _ { N } ^ { ( k ) } )$ lie in a bounded portion of $R _ { N }$ or $ { { \mathcal { C } } } _ { N }$ By the Bolzano-Weierstrass Theorem, we can find a convergent subsequence $\{ P _ { k _ { n } } \}$ of $\{ P _ { k } \}$ with $\operatorname* { l i m } _ { n \to \infty } P _ { k _ { n } } = P$ Let $P \colon ( b _ { 1 } , \ldots , b _ { N } ) $ .We have $\operatorname* { l i m } _ { n  \infty } a _ { j } ^ { ( k _ { n } ) } = \dot { b _ { j } }$ for $j = 1 , \dots , N$ Set $y = b _ { 1 } x _ { 1 } + \cdot \cdot \cdot + b _ { N } x _ { N }$ Then,

$$
\| y - y _ { k _ { n } } \| \leq \sum _ { j = 1 } ^ { N } | b _ { j } - a _ { j } ^ { ( k _ { n } ) } | \ \| x _ { j } \| \quad { \mathrm { a n d ~ s o } } \quad \operatorname* { l i m } _ { n \to \infty } \ \| y - y _ { k _ { n } } \| = 0 .
$$

If $\pmb { K }$ is closed,it contains all its limit points and hence $y \in K$

THEOREM 13.1.6 (Bernstein)． Let $\pmb { X }$ be $^ { \pmb { a } }$ complete normed linear space. Let $\left\{ x _ { i } \right\}$ be $^ { \pmb { a } }$ sequence of independent elements. Given an arbitrary sequence $e _ { 1 } \geq e _ { 2 } \geq \cdots > 0$ ， $\operatorname* { l i m } _ { n \to \infty } e _ { n } = 0$ ,we can find a $y \in X$ such that

$$
E _ { n } ( y ) = e _ { n } , \qquad n = 1 , 2 , \ldots .
$$

Proof:For each $\pmb { n }$ ,use Theorem l3.l.4 to determine a linear combination $y _ { n } = \sum _ { j = 1 } ^ { n + 1 } b _ { j } ^ { ( n ) } x _ { j }$ such that $E _ { k } ( y _ { n } ) = e _ { k } , k = 1 , 2 , . . . , n$ and $\| y _ { n } \| = e _ { 1 }$ We will show that a suitable subsequence of $\left\{ y _ { n } \right\}$ converges to the required $_ y$

For each $k , k = 1 , 2 , \ldots$ ，let $z _ { n , k } = \sum _ { j = 1 } ^ { k } b _ { j } { } ^ { ( n , k ) } x _ { j }$ be a linear ombination of $x _ { 1 } , \ldots , x _ { k }$ yielding a best approximation to ${ \pmb y } _ { \pmb n }$ . Then, $\| y _ { n } - z _ { n , k } \| \leq \| y _ { n } \|$ · Hence, $\| z _ { n , k } \| \leq \| y _ { n } \| + \| z _ { n , k } - y _ { n } \| \leq \| y _ { n } \| + \| y _ { n } \| = 2 e _ { 1 }$ Let $\pmb { k }$ be fixed. The set of elements $z _ { n , k }$ is bounded. By Lemma 13.1.5,we can find a subsequence $z _ { n _ { p } , k }$ converging to an element

$$
w _ { k } = \sum _ { j = 1 } ^ { k } c _ { j , k } x _ { j } { \mathrm { ~ i . e . , ~ } } \operatorname* { l i m } _ { p \to \infty } \| w _ { k } - z _ { n _ { \iota } , k } \| = 0 .
$$

For sufficiently large $\pmb { p }$ (depending upon $\pmb { k }$ ）， $\| w _ { k } - z _ { n _ { p } , k } \| < e _ { k }$ Consequently,

$$
\| w _ { k } - y _ { n _ { p } } \| \leq \| w _ { k } - z _ { n _ { p } , k } \| + \| z _ { n _ { p } , k } - y _ { n _ { p } } \| < e _ { k } + e _ { k } = 2 e _ { k } .
$$

Again, for suffcientl large $\pmb { p }$ and $\pmb q$

$$
\begin{array} { r } { \| y _ { n _ { p } } - y _ { n _ { q } } \| \leq \| w _ { k } - y _ { n _ { p } } \| + \| w _ { k } - y _ { n _ { q } } \| \leq 2 e _ { k } + 2 e _ { k } = 4 e _ { k } . } \end{array}
$$

Now $\operatorname* { l i m } _ { k \to \infty } e _ { k } = 0$ ； hence $\left\{ y _ { n _ { p } } \right\}$ is a Cauchy sequence. Since $\pmb { X }$ is complete, $\left\{ y _ { n _ { p } } \right\}$ converges to an element $y \in X$ . For sufficiently large $\pmb { p }$ ，

$$
e _ { k } = E _ { k } ( y _ { n _ { p } } ) = \| y _ { n _ { p } } - z _ { n _ { p } , k } \| .
$$

Bythe continuity f h hom $e _ { k } = \| y - w _ { k } \| = \left\| y - \sum _ { j = 1 } ^ { k } c _ { j , k } x _ { j } \right\| .$ Thus, for each $\pmb { k }$ $\dot { c } , E _ { k } ( y ) \le e _ { k }$ Nowiftherewerealineabation $\sum _ { j = 1 } ^ { k } d _ { j } x _ { j }$ for which $\left\| y - \sum _ { j = 1 } ^ { k } d _ { j } x _ { j } \right\| < e _ { k } ,$ $\left\| y _ { n _ { p } } - \sum _ { j = 1 } ^ { k } d _ { j } x _ { j } \right\| < e _ { k } .$ However for $n _ { p } > k , E _ { k } ( y _ { n _ { p } } ) = e _ { k }$ and this is a contradiction.Therefore, $\begin{array} { r } { \boldsymbol { E } _ { k } ( y ) = \boldsymbol { e } _ { k } , k = 1 , 2 , . . . } \end{array}$ ·

COROLLARY 13.1.7. Let $E _ { n } ( f ) = \operatorname* { m i n } _ { a _ { i } } \ \operatorname* { m a x } _ { a \leq x \leq b } { \bigg | } f ( x ) - \sum _ { i = 0 } ^ { n } a _ { i } x ^ { i } { \bigg | } .$ Then given $e _ { 0 } \geq e _ { 1 } \geq \cdots > 0$ lim $e _ { n } = 0$ we can find an $f \in C [ a , b ]$ with $\textstyle E _ { n } ( f ) = e _ { n }$ $n = 0 , 1 , \ldots ,$ n→8

This theorem tells us that in order to obtain nontrivial asymptotic theorems for ${ \pmb { { \cal E } } } _ { n } ( { \pmb { x } } )$ ，we must operate in a normed linear space that is not complete.As an example,when $f \in C [ a , b ]$ and polynomial approximation is considered, ${ \pmb { { \cal E } } } _ { \pmb { { n } } } ( f )$ can go to zero with arbitrary rapidity. This is not the case for $f \in { \cal C } ^ { 1 } [ a , b ]$ . As subspaces of smoother and smoother functions are considered, ${ \pmb { { \cal E } } } _ { n } ( f )$ goes to zero more and more rapidly. This is a phenomenon that pervades the theory of the asymptotics of approximation.

# 13.2 Degree of Approximation with Some Square Norms

THEOREM 13.2.1． Let $\pmb { B }$ be the unit circle,and set

$$
\begin{array} { r } { E _ { n } { ^ { 2 } } ( f ) = \underset { a _ { i } } { \operatorname* { m i n } } \iint | f ( z ) - a _ { 0 } - a _ { 1 } z - \cdots - a _ { n } z ^ { n } | ^ { 2 } d x d y , } \\ { \overset { } { B } \cong C \varepsilon ^ { 2 } ( B ) . \qquad } \end{array}
$$

If $f$ is analytic in $| z | < \rho , \rho \geq 1 ;$ but not in $| z | < \rho ^ { \prime }$ with $\pmb { \rho } ^ { \prime } > \pmb { \rho }$ ,then

$$
\operatorname* { l i m } _ { n \to \infty } \mathrm { ~ s u p ~ } [ E _ { n } ( f ) ] ^ { 1 / n } = 1 / \rho .
$$

Proof: Let $f ( z )$ have the Taylor expansion $f ( z ) = \sum _ { k = 0 } ^ { \infty } a _ { k } z ^ { k }$ where

$$
\operatorname* { l i m } _ { n \to \infty } \operatorname* { s u p } | a _ { k } | ^ { 1 / k } = 1 / \rho .
$$

$\left\{ { \sqrt { \frac { n + 1 } { \pi } } } z ^ { n } \right\}$ $L ^ { 2 } ( B )$

$$
f ( z ) = \sum _ { k = 0 } ^ { \infty } \left( \sqrt { \frac { \pi } { k + 1 } } a _ { k } \right) \sqrt { \frac { k + 1 } { \pi } } z ^ { k }
$$

is the Fourier expansion of $\pmb { f }$ By Ex. 1,13.1,

$$
| E _ { n } ( f ) | ^ { 2 } = \sum _ { k = n + 1 } ^ { \infty } { \frac { \pi } { k + 1 } } | a _ { k } | ^ { 2 } .
$$

Given $\varepsilon > 0$ ，we have for $k \geq N ( \varepsilon )$ ， $| a _ { k } | ^ { 1 / k } \leq 1 / \rho + \varepsilon ,$ so that $| a _ { k } | ^ { 2 } \leq$ $( 1 / \rho + \varepsilon ) ^ { 2 k }$ .Therefore, for $n \geq N ( \varepsilon )$ ，

$$
E _ { n } ( f ) | ^ { 2 } \leq \sum _ { k = n + 1 } ^ { \infty } { \frac { \pi } { k + 1 } } ( 1 / \rho + \varepsilon ) ^ { 2 k } \leq \pi \sum _ { k = n + 1 } ^ { \infty } ( 1 / \rho + \varepsilon ) ^ { 2 k } = { \frac { \pi ( 1 / \rho + \varepsilon ) ^ { 2 n + 2 } } { 1 - ( 1 / \rho + \varepsilon ) ^ { 2 } } }
$$

It follows from this that

$$
\operatorname* { l i m } _ { n \to \infty } \mathrm { s u p } [ E _ { n } ( f ) ] ^ { 1 / n } \leq 1 / \rho + \varepsilon .
$$

Since ε is arbitrary, lim sup $[ E _ { n } ( f ) ] ^ { 1 / n } \leq 1 / \rho .$

On the other hand,to an arbitrarily given $\varepsilon > 0$ , we have $| a _ { k } | ^ { 1 / k } \geq \frac 1 \rho - \varepsilon$ for an increasing sequence of integers $\pmb { k } = \pmb { k _ { 1 } }$ ， $\pmb { k _ { 2 } } ,$ .... Hence,

$$
\frac { \pi } { k _ { j } + 1 } | a _ { k _ { j } } | ^ { 2 } \geq \frac { \pi } { k _ { j } + 1 } ( 1 / \rho - \varepsilon ) ^ { 2 k _ { j } } .
$$

But,

$$
[ E _ { k _ { j } - 1 } ( f ) ] ^ { 2 } \geq \frac { \pi } { k _ { j } + 1 } | a _ { k _ { j } } | ^ { 2 } \geq \frac { \pi } { k _ { j } + 1 } ( 1 / \rho - \varepsilon ) ^ { 2 k _ { j } } .
$$


<!-- chunk 0006: pages 351-410 -->
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
