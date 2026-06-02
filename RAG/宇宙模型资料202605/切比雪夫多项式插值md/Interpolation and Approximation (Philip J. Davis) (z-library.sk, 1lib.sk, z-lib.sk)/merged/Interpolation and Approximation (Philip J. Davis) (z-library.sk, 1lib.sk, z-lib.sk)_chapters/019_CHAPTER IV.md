CHAPTER IV

# Convergence Theorems for Interpolatory Processes

4.1 Approximation by Means of Interpolation. Suppose that we have been given certain information about a function.Perhaps we know its values,or the values of its derivatives at certain points.Perhaps we know its moments.How can we use this information to construct other functions that will approximate it? This is the practical problem of numerical analysis. Theoretical analysis can go beyond. Having been given an infinite number of facts about our function,how can we reconstruct the function completely? Borrowing some terms from harmonic analysis,we may say that the process of extracting functional information constitutes an analysis of the function,while the process of reconstructing the function from given functional information is a synthesis of the function.

One of the most surprising facts in the theory of interpolation and approximation is that the simplest and most natural approach to synthesis leads to failure,or rather,to an impossibility.Given a function of class $C [ \pmb { a } , \pmb { b } ]$ ,what is more natural than to think that if a sequence of polynomials $p _ { n } ( f ; x )$ is set up that duplicates the function at $\pm 1$ points of the interval,then as $n \to \infty$ ， $p _ { n } ( f ; x )$ will converge to $f ( { \pmb x } ) \ ? \ : \ : \mathrm { \bf Y } \mathrm { \bf e t }$ ，this may not be the case.One of the first indications of this came around the turn of the century when Méray and later Runge,investigated interpolation to certain meromorphic functions. Runge looked at the function $f ( x ) = { \frac { 1 } { 1 + x ^ { 2 } } }$ and found the following to be true:if $p _ { n } ( f ; x )$ interpolates to $f$ at $n + 1$ equidistant points of the interval $\vert x \vert \le 5$ ， ${ \pmb p _ { \pmb n } }$ converges to $f$ only in the interval $| x | \leq 3 . 6 3 \cdot \cdot \cdot$ and diverges outside this interval. Although $f$ is analytic on the whole real axis,its singularities at $\pm i$ induce,so to speak,this divergence.In l9l2,Bernstein proved that equidistant interpolation over $| x | \leq 1$ to the function $y = | { \boldsymbol { x } } |$ diverges for $0 < | x | < 1$

These results relate to equidistant points of interpolation. The possibility was still open that a more felicitous choice of points would give rise to a convergent interpolation process.Some indications of this are contained in (3.3.10) where interpolation on the zeros of the Tschebyscheff polynomials minimizes certain error estimates.The hopes for this idea vanished when Bernstein and Faber simultaneously discovered in l914 that ifany triangular system of interpolation points is prescribed in advance，we can construct a continuous function for which the interpolation process carried out on these points cannot converge uniformly to this function.Even the Tschebyscheff zeros as interpolation points fare badly,for in l937,Marcinkiewicz gave an example of a continuous function for which interpolation at these zeros diverges at every point of(-1,1).

Yet,the damage is not as great as one might think and can be repaired in several ways.The first is to change the way the interpolation is carried out by not insisting that for $n + 1$ points a polynomial of class $\mathcal { P } _ { n }$ be employed.Fejer proved a remarkable theorem showing hov an interpolation process with controlled derivative values can converge properly for all continuous functions.The second way is not to insist on working with the class of continuous functions,but to assume some smoothness properties. The Tschebyscheff zeros (and the zeros of other orthogonal polynomials) actually are a remarkable system of interpolating points.Bernstein showed in 1916 that if $f$ is a continuous function for which $\operatorname * { l i m } _ { \delta  0 } \ w ( \delta ; f ) \log \ \delta = 0 \ /$ interpolation at these points produces a properly convergent sequence of polynomials.If interpolation is carried out on bounded sets,it suffces to assume that our functions are analytic in certain regions.If interpolation is carried out on unbounded sets,say the integers,then for convergence，we shall have to assume that our functions are entire and of severely restricted growth. Thus,if we are to have convergence,there must be a subtle interplay between the distribution of points of interpolation and the smoothness or growth properties of the interpolated function.Though much is known about this interplay,we shall be able to develop in this chapter only a few of its broader features.

4.2 Triangular Interpolation Schemes. We frst describe an interpolation scheme of great generality. Let there be given a triangular sequence of real or complex points

$$
\begin{array} { c c c c c } & { z _ { 0 0 } } & & & \\ { T \colon } & { z _ { 1 0 } } & { z _ { 1 1 } } & & \\ & { z _ { 2 0 } } & { z _ { 2 1 } } & { z _ { 2 2 } } \\ & { \cdot } & & & \\ & { \cdot } & & & \\ & { \cdot } & & & \end{array}
$$

Suppose that a function $f ( z )$ has been defined on a region containing the points of $\pmb { T }$ and let $p _ { n } ( f ; z )$ be that element of $\mathcal { P } _ { n }$ for which

$$
\begin{array} { l c r } { { p _ { n } ( f ; z _ { n i } ) = f ( z _ { n i } ) ~ } } & { { ~ i = 0 , 1 , . . . , n } } \\ { { { } } } & { { { } } } & { { } } \\ { { p _ { n } ( f ; z _ { n i } ) = f ( z _ { n i } ) ~ } } & { { ~ n = 0 , 1 , . . . . } } \end{array}
$$

In other words, $p _ { n } ( f ; z )$ interpolates to $f$ at the points of the $( n + 1 ) { \mathsf { s t } }$ row of $\pmb { T }$ .The numbers in the rows of $\pmb { T }$ may or may not be distinct. If they are

not distinct,then the interpolation polynomial is to be formed in accordance with the convention explained in 3.5.

We now ask the question, does

$$
\operatorname* { l i m } _ { n \to \infty } \ p _ { n } ( f ; z ) = f ( z ) !
$$

In such generality,the answer is a resounding no,but the problem is to delineate those circumstances under which the answer is yes.

In many cases of interest, the matrix $\pmb { T }$ degenerates by having its elements not depend upon the row, but only upon the column. In such a case,we can drop the double indexing,and write the scheme as follows

$$
\begin{array} { r l r } & { z _ { 0 } } & \\ & { \textit { S : } } & { z _ { 0 } \quad z _ { 1 } } \\ & { z _ { 0 } \quad z _ { 1 } \quad z _ { 2 } } \\ & { \cdot } & \\ & { \cdot } & \\ & { \cdot } & \end{array}
$$

For a scheme of this type, we have

$$
p _ { n } ( f ; z ) = \sum _ { k = 0 } ^ { n } [ f ( z _ { 0 } ) , f ( z _ { 1 } ) , \ldots , f ( z _ { k } ) ] ( z - z _ { 0 } ) , \ldots , ( z - z _ { k - 1 } )
$$

and so the existence of $\operatorname* { l i m } _ { n \to \infty } p _ { n } ( f ; z )$ is identical with the convergence of the interpolation series

$$
f ( z ) \sim \sum _ { k = 0 } ^ { \infty } [ f ( z _ { 0 } ) , f ( z _ { 1 } ) , \ldots , f ( z _ { k } ) ] ( z - z _ { 0 } ) \cdot \cdot \cdot ( z - z _ { k - 1 } ) .
$$

In order to appreciate the kinds of things that may occur with triangular interpolation schemes,we shall consider a few examples.

Ex. 1． A scheme $\pmb { S }$ i8 used with $z _ { 0 } = 1 , z _ { 1 } = \frac { 1 } { 2 } , \cdot \cdot \cdot , z _ { n } = \frac { 1 } { n + 1 } \cdot \cdot \cdot$ The interpolated function is $f ( x ) = x \sin { \frac { \pi } { x } }$ which is continuous in $- \infty < x < \infty$ Since $f ( z _ { k } ) = 0$ ，the interpolation polynomials $p _ { n } ( f ; x )$ are all identically zero. The sequence $p _ { n } ( f ; x )$ converges,but not to $\pmb { f }$

Ex.2.On the other hand if $f \in \mathcal P _ { n }$ ，then no matter how the matrix $\pmb { T }$ is Constituted,we shall always have $p _ { m } ( f ; z ) \equiv f ( z )$ for $m \geq n$ .Hence convergence takes place to the proper value.In other words,if the class of interpolated functions is suffciently small (the class of all polynomials) a triangular scheme is always convergent.

Ex.3.A degenerate case of $\pmb { S }$ is where all the points have a common value ${ \pmb z } _ { \pmb 0 }$ .By our convention,the interpolating polynomials are the partial sums of the Taylor expansion of $f \colon f ( z _ { 0 } ) + f ^ { \prime } ( z _ { 0 } ) ( z - z _ { 0 } ) + \cdots + { \frac { f ^ { ( n ) } ( z _ { 0 } ) } { n ! } } ( z - z _ { 0 } ) ^ { n } .$ .We have convergence to $\pmb { f } \left( \pmb { z } \right)$ if and only if $\pmb { f }$ is analytic at ${ \pmb z _ { 0 } }$ and the convergence holds throughout the largest circle $| z - z _ { 0 } | < \rho$ in which $f ( z )$ is analytic.On the other hand,if $\pmb { f }$ is merely of class $\ b { C } ^ { \infty }$ ,we may have divergence or convergence to a wrong value.

Ex.4.For $z _ { n 0 } , \ldots , z _ { n n }$ select the $( n \mathrm { ~ + ~ } 1 ) { \bf s t }$ roots of 1. Call them ${ \boldsymbol { w } } _ { j }$ Choose $f ( z ) = { \frac { 1 } { z } }$ .Then, $p _ { n } ( f ; z ) \equiv z ^ { n }$ inasmuch as ${ w _ { j } } ^ { n } = \frac { 1 } { w _ { j } } = f ( z _ { n j } )$ Notice that $p _ { n } ( f ; x )$ converges to 0 in $| z | < 1$ ，diverges for $| z | > 1$ . The sequence converges to $f$ only at $z = 1$

Ex.5.A scheme $s$ is used with $z _ { 0 } = 0 , z _ { 1 } = 1 , z _ { 2 } = 2 , . ~ . ~ .$ Select $f ( z ) =$ $( 1 + \sigma ) ^ { z }$ ,fora fixed $\pmb { \sigma }$ ，with $\sigma \neq - 1$ .It is easily verified through(2.7.lO) that

$$
p _ { n } ( f ; z ) = 1 + \sigma z + \sigma ^ { 2 } \frac { z ( z - 1 ) } { 2 ! } + \cdot \cdot \cdot + \sigma ^ { n } \frac { z ( z - 1 ) \cdot \cdot \cdot ( z - n + 1 ) } { n ! } .
$$

The convergence of the scheme is equivalent to the convergence of the series $\sum _ { n = 0 } ^ { \infty } \sigma ^ { n } { \frac { z ( z - 1 ) \cdot \cdot \cdot ( z - n + 1 ) } { n ! } }$ For fixed $\pmb { z }$ ，this is the power series expansion of $( 1 + \sigma ) ^ { z }$ about $\sigma = 0$ .Nowif $z \neq 0 , 1 , 2 , \ldots , ( 1 + \sigma ) ^ { z }$ is analytic in $| \sigma | < 1$ and hasa singularity at $\sigma = - 1$ .The series,and therefore $p _ { n } ( f ; z )$ ,isconvergent for $| \sigma | < 1$ and divergent for $| \sigma | > 1$

4.3 A Convergence Theorem for Bounded Triangular Schemes. If the points of interpolation are all confined to a bounded region of the plane and if the function we are interpolating is analytic in a sufficiently large region,then we shall have uniform convergence in a sub-region.This theorem is of interest in itself and also because it illustrates the use of the complex remainder (3.6.5) in estimating errors.This is a technique that can be put to practical use in numerical analysis.

THEOREM 4.3.1． Let $\textstyle R , \ S$ and $\pmb { T }$ be bounded simply connected regions, $\textstyle R \subset { \mathcal { S } } \subset T$ ， whose boundaries are $C _ { R } , ~ C _ { S }$ and $c _ { \pmb { x } }$ ,respectively. $c _ { \pmb { x } }$ is $\pmb { a }$ simple,closed,rectifiable curve,and $c _ { s }$ and $c _ { \pmb { x } }$ are assumed to be disjoint.

Let $\delta =$ minimum distance from $c _ { \pmb { x } }$ to $C _ { R }$ $\Delta =$ maximum distance from $c _ { s }$ to $C _ { R }$ and assume that $\frac { \Delta } { \delta } < 1$

Let the points of $^ { \pmb { a } }$ triangular system lie in $\pmb { R }$ and let $f ( z )$ be analytic in and on $c _ { \pmb { x } }$ Then $p _ { n } ( f ; z )$ converges to $f$ uniformly in $\boldsymbol { s }$

Proof: From (3.6.5),

$$
\begin{array} { l } { f ( z ) - { p _ { n } } ( f ; z ) = R _ { n } ( f ; z ) } \\ { \displaystyle = \frac { 1 } { 2 \pi i } \int _ { C _ { T } } \frac { ( z - z _ { n 0 } ) ( z - z _ { n 1 } ) \cdot \cdot \cdot ( z - z _ { n n } ) f ( t ) d t } { ( t - z _ { n 0 } ) ( t - z _ { n 1 } ) \cdot \cdot \cdot ( t - z _ { n n } ) ( t - z ) } . } \end{array}
$$

Hence,

$$
| R _ { n } ( f ; z ) | \leq \frac { 1 } { 2 \pi } \int _ { C _ { T } } \frac { | z - z _ { n 0 } | \cdot \cdot \cdot | z - z _ { n n } | \mid f ( t ) | d s } { | t - z _ { n 0 } | \cdot \cdot \cdot | t - z _ { n n } | \mid t - z | } .
$$

For $z _ { i k } \in R$ and $z \in { \mathcal { C } } _ { s }$ ， $| z - z _ { i k } | < \Delta$ .For $z _ { i k } \in R$ and $t \in C _ { T }$ ， $| t - z _ { i k } | > \delta$ If we set $M = \operatorname* { m a x } | f ( t ) | , d = \operatorname* { m i n } | t - z |$ ,then,

$$
| R _ { n } ( f ; z ) | \leq \frac { 1 } { 2 \pi } \int _ { C _ { T } } \frac { \Delta ^ { n + 1 } } { \delta ^ { n + 1 } } \frac M d d \boldsymbol { \mathscr { s } } = \frac { M L ( C _ { T } ) } { 2 \pi d } \bigg ( \frac { \Delta } { \delta } \bigg ) ^ { n + 1 } ,
$$

where $L ( C _ { T } ) = \mathrm { l e n g t h }$ of $c _ { \tau }$ .This estimate holds uniformly for $z \in \mathcal S$ . Since $\frac { \Delta } { \delta } < 1$ ， $\operatorname* { l i m } _ { n  \infty } R _ { n } ( f ; z ) = 0$ uniformly in $\boldsymbol { S }$

![](../chunks/Interpolation and Approximation (Philip J. Davis) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/227e128570039bef72650c5cb55ae496aec587219b891abe361ad49623f1aa77.jpg)  
Figure 4.3.1.

Ex.l．Let the points of the interpolation scheme all lie on the real segment $I = [ - a , a ]$ . Select a $\delta > 2 a$ and let $\pmb { T }$ be the set of points whose distance from $\pmb { I }$ is ${ \le } \delta$ .If $f ( z ) \in A ( T )$ ,the interpolatory scheme converges uniformly to $f$ on $\pmb { I }$ .This is independent of the distribution of the interpolating points.

![](../chunks/Interpolation and Approximation (Philip J. Davis) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/e6a42306c8bfbadc327384b915b973a2a90206983dda8c2c68bdb9deeaa112ed.jpg)  
Figure 4.3.2.

4.4 Lemniscates and Interpolation. More penetrating theorems can be obtained by postulating a more regular distribution of the points in the triangular scheme.An examination of equations (4.3.2) and (4.3.3) reveals that the asymptotic behavior of the expression

$$
| ( z - z _ { n 0 } ) ( z - z _ { n 1 } ) \cdot \cdot \cdot ( z - z _ { n n } ) | ^ { 1 / ( n + 1 ) }
$$

contains the key to convergence. We will therefore investigate convergence under the hypothesis that the following limit exists on certain sets of the complex plane:

$$
\operatorname* { l i m } _ { n \to \infty } | ( z - z _ { n 0 } ) ( z - z _ { n 1 } ) \cdot \cdot \cdot ( z - z _ { n n } ) | ^ { 1 / ( n + 1 ) } = \sigma ( z ) .
$$

Here are some examples of triangular distributions of points with this property.

Ex.1. Let al the points $z _ { i j }$ Consist of & single point ${ z _ { 0 } }$ . Then $\sigma ( z ) = | z - z _ { 0 } |$

Ex.2. Let $z _ { n 0 } , z _ { n 1 } , \ldots , z _ { n n }$ be the $\pm \ : 1$ zeros of the $( n + 1 ) { \mathsf { s t } }$ Tschebyscheff polynomial $\pmb { T } _ { n + 1 } ( z )$ . Then, $( z - z _ { n 0 } ) ( z - z _ { n 1 } ) \cdot \cdot \cdot ( z - z _ { n n } ) = \tilde { \cal T } _ { n + 1 } ( z )$ (Def. 3.3.2). Let $z = \rho e ^ { i \theta }$ ， $w = \textstyle { \frac { 1 } { 2 } } ( z + z ^ { - 1 } ) = \textstyle { \frac { 1 } { 2 } } ( \rho e ^ { i \theta } + \rho ^ { - 1 } e ^ { - i \theta } )$ .Then,

$$
T _ { n } ( w ) = \frac { } { } ^ { 1 } ( \rho ^ { n } e ^ { i n \theta } + \rho ^ { - n } e ^ { - i n \theta } ) .
$$

This may be proved by induction. It is true for $\textbf { \em n } = \textbf { 0 }$ by (3.3.3). Assume it is true for $\mathbf { 0 } , \mathbf { 1 } , \mathbf { 2 } , \ldots , \mathfrak { n }$ By (3.3.4),

$$
\begin{array} { r l } & { T _ { n + 1 } ( w ) = ( \rho e ^ { i \theta } + \rho ^ { - 1 } e ^ { - i \theta } ) \frac { 1 } { 2 } ( \rho ^ { n } e ^ { i n \theta } + \rho ^ { - n } e ^ { - i n \theta } ) } \\ & { \phantom { x x x x x x x x x x x x x x x x x x x x x x x x x } - \frac { 1 } { 2 } ( \rho ^ { n - 1 } e ^ { i ( n - 1 ) \theta } + \rho ^ { - n + 1 } e ^ { - i ( n - 1 ) \theta } ) } \\ & { \phantom { x x x x x x x x x x x x } = \frac { 1 } { 2 } ( \rho ^ { n + 1 } e ^ { ( n + 1 ) i \theta } + \rho ^ { - ( n + 1 ) } e ^ { - ( n + 1 ) i \theta } ) . } \end{array}
$$

This proves the identity for $\textbf { \em n } + \textbf { 1 }$

From (4.4.2)

$$
\begin{array} { l } { \mathrm { R e } T _ { n } ( w ) = \frac { 1 } { 2 } ( \rho ^ { n } + \rho ^ { - n } ) \cos n \theta } \\ { \mathrm { I m } T _ { n } ( w ) = \frac { 1 } { 2 } ( \rho ^ { n } - \rho ^ { - n } ) \sin n \theta } \end{array}
$$

and so

$$
\left| T _ { n } ( w ) \right| = \frac { _ 1 } { ^ 2 } ( \rho ^ { 2 n } + 2 \cos 2 n \theta + \rho ^ { - 2 n } ) ^ { \frac { 1 } { 2 } } . \ .
$$

Therefore, for $\pmb { w }$ on $\pmb { \delta _ { \pmb { \rho } } }$ (cf. Def. (1.13.1)) we have

$$
\operatorname* { l i m } _ { n \to \infty } | T _ { n } ( w ) | ^ { 1 / n } = \rho , { \mathrm { u n i f o r m l y } } .
$$

Since ${ \tilde { T } } _ { n } = { \frac { 1 } { 2 ^ { n - 1 } } } T _ { n } ,$

$$
\sigma ( z ) = \operatorname* { l i m } _ { n  \infty } | \tilde { T } _ { n } ( z ) | ^ { 1 / n } = \rho / 2 , z \in \mathcal { E } _ { p } .
$$

Ex.3．A similar limit holds on $\pmb { \mathscr { E } _ { \pmb { \mathscr { p } } } }$ for the Legendre polynomials (cf. Theorem 12.4.5).

Ex.4.The points $z _ { n 0 } , \ldots , z _ { n n }$ are evenly distributed on $[ - 1 , 1 ] \colon z _ { n k } =$ $- 1 + { \frac { 2 k } { n } }$ Here we have

$$
\begin{array} { l } { \displaystyle \sigma _ { n } ( z ) = \big | ( z - z _ { n 0 } ) \cdot \cdot \cdot \cdot ( z - z _ { n n } ) \big | ^ { 1 / ( n + 1 ) } = \bigg | ( z + 1 ) \bigg ( z + 1 - \frac { 2 } { n } \bigg ) \cdot \cdot \cdot ( z + 1 - 2 ) \bigg | ^ { 1 / ( n + 1 ) } } \\ { \displaystyle \qquad = 2 \left| \left( \frac { z + 1 } { 2 } - \frac { 0 } { n } \right) \left( \frac { z + 1 } { 2 } - \frac { 1 } { n } \right) \cdot \cdot \cdot \left( \frac { z + 1 } { 2 } - \frac { n } { n } \right) \right| ^ { 1 / ( n + 1 ) } } \end{array}
$$

Therefore $\log \frac { 1 } { 2 } \sigma _ { n } ( z ) = \frac { 1 } { n + 1 } \sum _ { k = 0 } ^ { n } \log \Bigg | \frac { z + 1 } { 2 } - \frac { k } { n } \Bigg | .$ By the definition of the inte-$\begin{array} { l l l } { { \mathrm { g r a l , } \displaystyle \operatorname* { l i m } _ { n \to \infty } \log \frac { 1 } { 2 } \sigma _ { n } ( z ) \ = \displaystyle \int _ { 0 } ^ { 1 } \log \left| \frac { z + 1 } { 2 } - t \right| d t = \frac { 1 } { 2 } \int _ { - 1 } ^ { + 1 } \log \left| z - u \right| d u \ - \log 2 . } } \\ { { \mathrm { H e n c e , } \ \mathrm { f o r \ a l l } \ z \ \mathrm { o u t s i d e } \left[ - 1 , 1 \right] , \sigma ( z ) \ = \exp \frac { 1 } { 2 } \displaystyle \int _ { - 1 } ^ { + 1 } \log \left| z - u \right| d u . } } \end{array}$

Ex.5．A wide generalization of Ex.1 is contained in the next theorem.

THEOREM 4.4.1． Let $z _ { 1 } , z _ { 2 } , \ldots$ ，be $^ { \pmb { a } }$ sequence that has $\pmb { k }$ limit points $\pmb { \zeta _ { 1 } }$ $\zeta _ { 2 } , \ldots , \zeta _ { k }$ approached cyclically. That is,

$$
\begin{array} { r } { \underset { n  \infty } { \operatorname* { l i m } } z _ { n k + 1 } = \zeta _ { 1 } } \\ { \underset { n  \infty } { \operatorname* { l i m } } z _ { n k + 2 } = \zeta _ { 2 } } \end{array}
$$

$$
\operatorname* { l i m } _ { n \to \infty } z _ { n k + k } = \zeta _ { k } .
$$

Then

$$
\sigma ( z ) = \operatorname* { l i m } _ { n \to \infty } | ( z - z _ { 1 } ) \cdot \cdot \cdot ( z - z _ { n } ) | ^ { 1 / n } = | ( z - \zeta _ { 1 } ) \cdot \cdot \cdot ( z - \zeta _ { k } ) | ^ { 1 / k }
$$

uniformly on any set $\pmb { \mathscr { s } }$ that is bounded and such that

$$
\operatorname* { i n f } _ { t \in S } | z _ { i } - t | > \delta > 0 \qquad i = 1 , 2 , \ldots . . .
$$

Proof: We begin with the following observation which is really a slight modification of the“consistency of Cesaro summability."

Let $\phi _ { \kappa } ( z )$ be a sequence of functions defined on a point set $\pmb { \mathscr { s } }$ and which converges uniformly on $\pmb { \mathscr { s } }$ to a function $\phi ( z )$ . Assume that $\phi _ { k } ( z )$ and $\phi ( z )$ are all bounded on $\pmb { \mathscr { s } }$ .Then,the sequence of arithmetic means

$$
( 1 / n ) [ \phi _ { 1 } ( z ) + \cdots + \phi _ { n } ( z ) ]
$$

also converges uniformly to $\phi ( z )$ on $\pmb { \mathscr { s } }$ For, given an $\pmb \varepsilon > 0$ ， we can find an

$m = m ( \pmb { \varepsilon } )$ such that $| \phi ( z ) - \phi _ { n } ( z ) | \leq \varepsilon$ for all $z \in \mathcal { S }$ and all $\pmb { n } \geq m$ .Now, for $\pmb { n } \geq m$ ，

$$
\begin{array} { l } { { \displaystyle { D _ { n } ( z ) = ( 1 / n ) [ \phi _ { 1 } ( z ) + \cdots + \phi _ { n } ( z ) ] - \phi ( z ) } } } \\ { { \displaystyle { \qquad = ( 1 / n ) [ \phi _ { 1 } ( z ) + \cdots + \phi _ { m } ( z ) ] + \frac { n - m } { n } \cdot \frac { 1 } { n - m } [ ( \phi _ { m + 1 } ( z ) - \phi ( z ) ) } } } \\ { { \displaystyle { \qquad + \cdots + ( \phi _ { n } ( z ) - \phi ( z ) ) ] - ( m / n ) \phi ( z ) . } } } \end{array}
$$

Let $M _ { m } = \operatorname* { m a x } _ { z \in S } \displaystyle \left( | \phi _ { 1 } ( z ) | + \cdots + | \phi _ { m } ( z ) | \right) , M = \operatorname* { m a x } _ { z \in S } | \phi ( z ) | .$ Hence,

$$
| D _ { n } ( z ) | \leq \frac { M _ { m } } { n } + \frac { n - m } { n } \cdot \frac { 1 } { n - m } \left( n - m \right) \varepsilon + \frac { m M } { n } , ~ z \in \cal { S } .
$$

Keep $\pmb { m }$ fixed and let $n \to \infty$ . We obtain, for $\pmb { n }$ suffciently large, i.e., for

$$
\left( n \geq \operatorname* { m a x } \left( { \frac { M _ { m } } { \varepsilon } } , { \frac { m M } { \varepsilon } } \right) \right) ,
$$

$$
| D _ { n } ( z ) | \leq \varepsilon + \varepsilon + \varepsilon = 3 \varepsilon , \qquad z \in \mathcal { S } .
$$

This inequality implies the uniform convergence stated.

We now turn to the proof of the theorem.

Let $\phi _ { i } ( z ) = \log | z - z _ { i } |$ For $z \in S , \log | z - z _ { i } | \geq \log \delta , i = 1 , 2 , . . . .$ In view of the cyclic limit conditions,the $z _ { i }$ are bounded. Since $\pmb { \mathscr { s } }$ is bounded, $\log | z - z _ { i } | \leq B$ for $z \in \pmb { S }$ ， $i = 1$ ,2,....Thus, $\phi _ { i } ( z )$ are uniformly bounded in $\pmb { \mathscr { s } }$ ； that is,we can find an $\pmb { M }$ such that $| \phi _ { i } ( z ) | \leq M , z \in S$ ， $i = 1$ ,2,....

The function $\log | z - \zeta _ { i } |$ is also bounded in $\pmb { \mathscr { s } }$ since the $\boldsymbol { \zeta } _ { i }$ are limit points of the $z _ { k }$ and the latter are bounded away from $\pmb { \mathscr { s } }$

Let $N = n k + p$ ， $0 \leq p < k$ and consider $\pmb { n }$ and $\pmb { p }$ as functions of $\pmb { x }$ Then

$$
\begin{array} { l } { { \displaystyle \log | ( z - z _ { 1 } ) \cdot \cdot \cdot ( z - z _ { N } ) | ^ { 1 / N } = \frac { 1 } { N } \sum _ { i = 1 } ^ { N } \phi _ { i } ( z ) } } \\ { { \displaystyle \quad \quad = \frac { n } { N } \frac { 1 } { n } \sum _ { j = 0 } ^ { n - 1 } \phi _ { j k + 1 } + \cdot \cdot \cdot + \frac { n } { N } \frac { 1 } { n } \sum _ { j = 0 } ^ { n - 1 } \phi _ { j k + k } + \frac { n } { N } \frac { 1 } { n } \sum _ { j = 1 } ^ { n } \phi _ { n k + j } } . }  \end{array}
$$

(If $\pmb { p } = \mathbf { 0 }$ , the last sum is taken to be O.） In view of (4.4.7), $\operatorname* { l i m } _ { n  \infty } \phi _ { n k + i } =$ $\log | z - \zeta _ { i } | ~ i = 1 , 2 , \ldots , k ,$ uniformly on $\pmb { S }$ 、Hence,their mean values $\frac { 1 } { n } \sum _ { j = 0 } ^ { n - 1 } \phi _ { j k + i }$ also approach this limit uniformly. Furthermore,

$$
\left| \frac { 1 } { n } \sum _ { j = 1 } ^ { p } \phi _ { n k + j } \right| \leq \frac { 1 } { n } \sum _ { j = 1 } ^ { p } | \phi _ { n k + j } | \leq \frac { p M } { n } \leq \frac { k M } { n } .
$$

$n  \infty , \frac { 1 } { n } \sum _ { j = 1 } ^ { p } \phi _ { n k + j }$ $\pmb { S }$ $\operatorname* { l i m } _ { N  \infty } { \frac { n } { N } } =$ $\frac { 1 } { k }$ we have $\operatorname* { l i m } _ { N  \infty } \log | ( z - z _ { 1 } ) \cdot \cdot \cdot ( z - z _ { N } ) | ^ { 1 / N } = \frac { 1 } { k } \sum _ { i = 1 } ^ { k } \log | z - \zeta _ { i } |$ uniformly in $s$ .The proof is completed by exponentiation.

Actually,(4.4.8) holds uniformly on any set $\pmb { S }$ that is bounded and such that inf $| \zeta _ { i } - t | > \delta > 0 , i = 1 , \ldots , k$

Motivated by (4.4.8), we shall next study the loci given by

$$
| ( z - z _ { 1 } ) ( z - z _ { 2 } ) \cdot \cdot \cdot ( z - z _ { n } ) | = \mathrm { c o n s t a n t } .
$$

DEFINITION 4.4.1． Let $z _ { 1 } , \ldots , z _ { n }$ be $\pmb { n }$ complex numbers not necessarily distinct. For $r > 0$ ,the set of points satisfying

$$
| ( z - z _ { 1 } ) ( z - z _ { 2 } ) \cdot \cdot \cdot ( z - z _ { n } ) | = r ^ { n }
$$

is called a lemniscate and will be designated by $\Gamma _ { r }$ The points $z _ { i }$ are called the foci of the lemniscate and $\pmb { r }$ its radius. The set of points satisfying the inequality

$$
| ( z - z _ { 1 } ) ( z - z _ { 2 } ) \cdot \cdot \cdot ( z - z _ { n } ) | < r ^ { n }
$$

will be designated by $\mathcal { L } _ { r }$

With $z _ { i }$ fixed and $\boldsymbol { r }$ varying, we may speak of a family of confocal lemni-scates. Note that if $r _ { 1 } < r _ { 2 }$ then $\mathcal { L } _ { r _ { 1 } } \subset \mathcal { L } _ { r _ { 2 } }$

Ex. 6. $k = 1 . \left| z \mathrm { ~ - ~ } z _ { 1 } \right| = r$ is a family of concentric circles centered at $z _ { 1 }$

Ex.7.Let $\ k = \pmb { 2 }$ and $z _ { 1 } , z _ { 2 }$ be distinct.Then, $| z - z _ { 1 } | | z - z _ { 2 } | = r ^ { 2 }$ is the locus of points which move in such a way that the product of their distances to $z _ { 1 }$ and to $z _ { 2 }$ is constant. If $\begin{array} { r } { 0 < r < \frac { 1 } { 2 } \left| z _ { 2 } - z _ { 1 } \right| } \end{array}$ ,then the locus consists of two mutually exterior ovals,one surrounding $z _ { 1 }$ and the other ${ z _ { \mathbf { 2 } } }$ 、These are the Ovals of Cassini.When $r = \frac { 1 } { 2 } \left| z _ { 2 } - z _ { 1 } \right|$ ，we obtain the Lemniscate of Bernoulli, a figure 8 with a double point at $\frac { 1 } { 2 } ( z _ { 1 } \ + \ z _ { 2 } )$ . When $r > \frac { 1 } { 2 } \left| z _ { 2 } - z _ { 1 } \right|$ ，the locus consists of one closed contour containing ${ z } _ { 1 }$ and ${ z _ { \mathbf { 2 } } }$ in its interior.

![](../chunks/Interpolation and Approximation (Philip J. Davis) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/1a886c69c835726558a684b53481ceea3aa0ac4d9c66baa8395285099259d188.jpg)  
Figure 4.4.1 Confocal Lemniscates with Two Foci.

The behavior of confocal families of lemniscates follows the pattern of Example 7. If $z _ { 1 } , \ldots , z _ { n }$ are $\pmb { n }$ distinct points and if $\pmb { r }$ is sufficiently small, the locus $\Gamma _ { r }$ consists of $\mathscr { n }$ closed contours surrounding precisely one of the foci. As $\pmb { r }$ increases,the contours increase in size until two or more of them touch and then coalesce,reducing the number of contours.This coalescence continues until for sufficiently large $\pmb { r }$ there is but one contour surrounding all the foci.As $r \to \infty$ ,the single contour becomes more and more circular in its shape.If the $z _ { i }$ are not all distinct,this picture can be modified in an appropriate way.

![](../chunks/Interpolation and Approximation (Philip J. Davis) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/764ec0bff42aad91b8547a992afaf1cc414049622956ef034f1aa4b74119a58d.jpg)  
Figure 4.4.2 Confocal Lemniscates with 3 Foci

We shall now sketch the proofs of these facts. Consider the set $\mathcal { L } _ { r }$ It is nonempty,for it contains the foci $z _ { 1 } , \ldots , z _ { n }$ .It is open,for suppose $z \in \mathcal { L } _ { r }$ That is, $| z - z _ { 1 } | \cdot \cdot \cdot | z - z _ { n } | < r ^ { n }$ By the continuity of the absolute value, this inequality must hold in a neighborhood of $z , \mathcal { L } _ { r }$ is bounded.For let a circle $C _ { 1 }$ contain the foci.Draw a second circle $C _ { 2 }$ ，concentric with $C _ { 1 }$ ,and such that the difference of the radii of $C _ { 2 }$ and $C _ { 1 }$ is greater than $\boldsymbol { r }$ For any point $_ z$ exterior to $C _ { 2 } , | z - z _ { i } | > r$ Hence $| z - z _ { 1 } | \cdot \cdot \cdot | z - z _ { n } | > r ^ { n }$ Therefore no point exterior to $C _ { 2 }$ can be in $\mathcal { L } _ { r }$

Let $\Delta _ { r }$ designate the set of points for which $| z - z _ { 1 } | \cdot \cdot \cdot | z - z _ { n } | > r ^ { n }$ Again,by continuity,if $z \in \Delta _ { r }$ ,there is a whole neighborhood of $\textit { \textbf { z } }$ in $\Delta _ { r }$

Hence every point of $\Delta _ { r }$ is an exterior point of $\mathcal { L } _ { r }$ The exterior of $\mathcal { L } _ { r }$ is precisely $\Delta _ { r }$ .For suppose $_ z$ is in the exterior of $\mathcal { L } _ { r }$ and that

$$
| ( z - z _ { 1 } ) \cdot \cdot \cdot ( z - z _ { n } ) | \equiv | p ( z ) | = r ^ { n } .
$$

Since $\pmb { \mathscr { p } } ( z ) \neq 0$ ,there isa whole neighborhood $\pmb { N }$ of $_ z$ whose closure lies in the exterior of $\mathcal { L } _ { r }$ and in which $\pmb { p } ( z )$ has no zero.By the Maximum Principle (Theorem 1.9.5) $\pmb { p } ( z )$ cannot have a maximum or a minimum in the interior of $\pmb { N }$ .Therefore there is a point $z ^ { \prime }$ on the boundary of $\pmb { N }$ at which

$$
| p ( z ^ { \prime } ) | < | p ( z ) | = r ^ { n } .
$$

This means that $z ^ { \prime } \in \mathcal { L } _ { r }$ and this is a contradiction since $z ^ { \prime }$ is exterior to $\mathcal { L } _ { r }$ It follows that if $| z - z _ { 1 } | \cdot \cdot \cdot | z - z _ { n } | = r ^ { n }$ ， $z$ cannot be exterior to $\mathcal { L } _ { r }$ Thus, finally, $\Delta _ { r }$ is the complete exterior of $\mathcal { L } _ { r }$ and $\Gamma _ { r }$ is its complete boundary.

Since $\mathcal { L } _ { r }$ is an open set,it consists of a certain number (finite or infinite) of connected components.Each component must contain at least one of the points $z _ { i }$ For,suppose $c$ is a component which does not.On the boundary of $c$ we have $| p ( z ) | = r$ ，and by assumption, $\pmb { p } ( z )$ does not vanish in $c$ Hence,by the Maximum Principle,both the maximum and the minimum of $| p ( z ) |$ in $\bar { c }$ ,the closure of $c$ ,occur on the boundary of $c$ 、This means that $\displaystyle \operatorname* { m a x } _ { z \in \mathcal { C } } | p ( z ) | = \displaystyle \operatorname* { m i n } _ { z \in \mathcal { C } } | p ( z ) | = r$ Therefore $| p ( z ) |$ is constant over $c$ and this implies that $\pmb { p } ( z )$ is constant over $c$ ，This is impossible.Thus,each of the connected components of $\mathcal { L } _ { r }$ must contain at least one of the points $z _ { i }$ in its interior,and so there are at most $\pmb { n }$ such components.

Each of the components of $\mathcal { L } _ { r }$ must be simply connected.For, let $\pmb { C }$ be a component and let $\mathbf { r }$ be a simple closed curve lying in $c$ .On $\mathbf { \varGamma }$ we have $| p ( z ) | < r$ Hence by the Maximum Principle,we have $| p ( z ) | < r$ throughout the interior of $\mathbf { \Gamma } \mathbf { \Gamma } \mathbf { \Gamma } \mathbf { \Gamma } \mathbf { \Gamma } \mathbf { \Gamma } \mathbf { \Gamma } \mathbf { \Gamma }$ .Thus,the whole interior of $\mathbf { \Gamma } ^ { \Gamma }$ belongs to $\mathcal { L } _ { r }$ It follows that $c$ must be simply connected.For suppose not.Then there would be a point $^ { \pmb { a } }$ interior to $\mathbf { \Gamma } ^ { \Gamma }$ with $\pmb { a } \in \mathcal { L } _ { r }$ and $a \not \in C$ Let $\pmb { I }$ be the closure of the interior of $\Gamma$ Then $A = I \cup C$ is a connected set that is in $\mathcal { L } _ { r }$ and contains $\boldsymbol { c }$ properly.This is impossible since $c$ is a maximal connected subset. $\mathcal { L } _ { r }$ therefore consists of a number (not exceeding $\pmb { n }$ )of simply connected regions and the boundary of $\mathcal { L } _ { r }$ consists of a number of contours each of which is the complete boundary of a simply connected region.

At a point of $\Gamma _ { r }$ where the derivative of $\prod _ { i = 1 } ^ { n } ~ ( z - z _ { i } )$ does not vanish, one can show,using the implicit function theorem for analytic functions, that the lemniscate is an analytic curve.

What is the situation when $\pmb { r }$ is sufficiently small? Assume that the points $z _ { 1 } , \ldots , z _ { n }$ are distinct.For $\pmb { r }$ sufficiently small, the $\pmb { n }$ circles $| z - z _ { i } | < r$ have no common points.Then if $\rho < r , \mathcal { L } _ { \rho }$ must be contained in the union of these circles.For otherwise, $| z - z _ { i } | \geq r$ and hence $\prod _ { i = 1 } ^ { n } | z - z _ { i } | \geq r ^ { n } > \rho ^ { n } ,$

Moreover,since the points $z _ { i }$ are interior to the components of $\mathcal { L } _ { \mathfrak { p } } ,$ it follows that $\mathcal { L } _ { \mathfrak { p } }$ consists of exactly $\pmb { n }$ components with precisely one component lying in each one of these circles. The lemniscate $\Gamma _ { \pmb { \rho } }$ consists of precisely $\pmb { n }$ ovals,one in each circle.

What happens when $\pmb { r }$ is sufficiently large? Let a circle $c$ of diameter $\pmb { D }$ contain all the points $z _ { i }$ If $_ z$ is in $c$ then $| z - z _ { i } | < D$ so that

$$
\prod _ { i = 1 } ^ { n } | z - z _ { i } | < D ^ { n } .
$$

Therefore $c$ is contained in any $\mathcal { L } _ { \mathfrak { p } }$ with $\rho > D$ 、Since we know that each component of $\mathcal { L } _ { \mathfrak { p } }$ must contain at least one of the $z _ { i }$ in it,it follows that $\mathcal { L } _ { \mathfrak { p } }$ must consist of a single region containing this circle. The corresponding leinniscate $\Gamma _ { \pmb { \rho } }$ consists of a single contour.

As $\pmb { r }$ becomes very large, so also must $| z |$ .With $\boldsymbol { z }$ far removed from ${ z } _ { i } ,$ the points $z _ { i }$ may be regarded as a single iterated point and the lemniscate is“almost”a circle.

The multiple points of lemniscates occur at the solutions of $\pmb { \mathcal { p } } ^ { \prime } ( z ) = \mathbf { 0 }$ ， $p ( z ) \equiv \prod _ { i = 1 } ^ { n } ( z - z _ { i } )$ . But it would take us out of our way to discuss the interesting geometrical facts related to them.

LEMMA 4.4.2. Let $\phi _ { n } ( z ) , \phi ( z )$ be functions of $\pmb { a }$ complex variable and suppose that

$$
\operatorname * { l i m } _ { n  \infty } | \phi _ { n } ( z ) | ^ { 1 / n } = | \phi ( z ) |
$$

on $^ { \pmb { a } }$ set $\pmb { S }$ and uniformly on $\pmb { a }$ subset $S ^ { \prime } \subseteq S$ Let $\left\{ a _ { n } \right\}$ be $^ { \pmb { a } }$ sequence of complex numbers for which

$$
\operatorname* { l i m } _ { n \to \infty } \operatorname* { s u p } | a _ { n } | ^ { 1 / n } = 1 / r , \qquad 0 \leq r < \infty .
$$

Then the series $\sum _ { n = 0 } ^ { \infty } a _ { n } \phi _ { n } ( z )$ converges at all points of $\pmb { S }$ where $| \phi ( z ) | < r$ and ：   
diverges at all points of $\pmb { S }$ where $| \phi ( z ) | > r$ It converges uniformly at all points   
of $\mathbf { \nabla } _ { \mathbf { \lambda } } ^ { g \prime }$ where $| \phi ( z ) | \leq s < r$

Proof: Given a $z \in S \cap \left\{ z \colon | \phi ( z ) | < r \right\}$ For all $\pmb { n }$ sufficiently large，we have from (4.4.11), $| \phi _ { n } ( z ) | ^ { 1 / n } \leq r ^ { \prime }$ for some $0 < r ^ { \prime } < r$ Select an $\pmb { r } ^ { \prime \prime }$ with $r ^ { \prime } < r ^ { \prime \prime } < r$ Then for all $\pmb { n }$ sufficiently large,we have from (4.4.12),

$$
| a _ { n } | ^ { 1 / n } \leq { \frac { 1 } { r ^ { \prime \prime } } } .
$$

Thus,

$$
| a _ { n } \phi _ { n } ( z ) | \leq { \biggl ( } { \frac { r ^ { \prime } } { r ^ { n } } } { \biggr ) } ^ { n } .
$$

Our infinite series is majorized by a convergent geometric series and must itself be convergent.

If

$$
z \in S ^ { \prime } \cap \{ z : | \phi ( z ) | \le s \} , \qquad s < r ,
$$

then the estimate $| \phi _ { n } ( z ) | ^ { 1 / n } \leq r ^ { \prime }$ ， $\vartheta < r ^ { \prime } < r$ holds uniformly in this set and the same reasoning allows us to conclude uniform convergence there.

Let $z \in \pmb { S }$ be such that $| \phi ( z ) | > r$ Then for all $\pmb { n }$ sufficiently large and for some $r ^ { \prime } > r _ { \mathrm { { ; } } }$ $| \phi _ { n } ( z ) | ^ { 1 / n } > r ^ { \prime }$ .Select an $\pmb { r } ^ { \prime \prime }$ with $r ^ { \prime } > r ^ { \prime \prime } > r .$ Since

$$
\operatorname* { l i m } _ { n  \infty } \operatorname* { s u p } | a _ { n } | ^ { 1 / n } = { \frac { 1 } { r } } ,
$$

$n _ { 1 } , n _ { 2 } , . . .  \infty$ with $| a _ { n _ { k } } | ^ { 1 / n _ { k } } \geq \frac { 1 } { r ^ { \prime \prime } }$ Hence $| a _ { n _ { k } } \phi _ { n _ { k } } ( z ) | \geq \left( { \frac { r ^ { \prime } } { r ^ { \prime \prime } } } \right) ^ { n _ { k } }$ for all $\pmb { k }$ sufficiently large. Since $r ^ { \prime } / r ^ { \prime \prime } > 1$ ， the general term of the series does not approach O and the series is divergent.

Ex.8.Let $\phi _ { n } ( z ) = z ^ { n }$ Then $\operatorname* { l i m } _ { n  \infty } | \phi _ { n } ( z ) | ^ { 1 / n } = | z |$ for all $| z | < \infty$ and the limit isuniformon any st If im sup $\left. a _ { n } \right. ^ { 1 / n } = \frac { 1 } { r }$ , we have convergence of $\sum _ { \ l = 0 } ^ { \infty } a _ { n } z ^ { n }$ for $| z | < r$ and divergence for $| z | > r$ .Our lemma is therefore a simple modification of the Cauchy-Hadamard Theorem for the radius of convergence of a power series (Theorem 1.9.4).

Ex.9. $\phi _ { n } ( z ) = T _ { n } ( z ) = $ the nth Tschebyscheff polynomial. From (4.4.5), $\big | \phi ( z ) \big | = \operatorname* { l i m } _ { n \to \infty } _ { } ^ { } | T _ { n } ( z ) | ^ { 1 / n } = \rho \mathrm { f o r } z \mathrm { o n } \mathscr { C } _ { \rho } , \mathrm { I f } \operatorname* { l i m } _ { n \to \infty } \mathrm { s u p } | a _ { n } | ^ { 1 / n } = \frac { 1 } { r } , 1 < r \leq \infty ,$ we conclude that the series $\sum _ { i = 0 } ^ { \infty } a _ { n } T _ { n } ( z )$ converges in the interior of $\mathcal { E } _ { r } ,$ diverges in its exterior and converges uniformly if any $\mathcal { E } _ { r ^ { \prime } } , r ^ { \prime } < r$ 、In the case of expansions in Tschebyscheff polynomials,we have confocal ellipses of convergence as the analog of circles of convergence for power series.

Ex.10. Expansions in Legendre polynomials have ellipses of convergence.   
f. Theorem 12.4.7.

THEOREM 4.4.3．Let $\mathcal { L } _ { \mathfrak { p } }$ designate the lemniscate interior

$$
| ( z - \zeta _ { 1 } ) ( z - \zeta _ { 2 } ) \cdot \cdot \cdot ( z - \zeta _ { k } ) | < \rho ^ { k } .
$$

Let $z _ { 0 } , z _ { 1 } , \ldots , l$ ie in $\mathcal { L } _ { \mathfrak { p } }$ and approach $\zeta _ { 1 } , \ldots , \zeta _ { k }$ cyclically； i.e., (4.4.7) holds. Let $f ( z )$ be analytic in $\mathcal { L } _ { \mathfrak { p } }$ but not in any $\mathcal { L } _ { \mathfrak { p } _ { 1 } }$ with $\pmb { \rho _ { 1 } } > \pmb { \rho _ { } }$ If $\mathcal { L } _ { \mathfrak { p } }$

consists of several mutually exterior regions, then $f ( z )$ is assumed to be a general analytic configuration (cf. 3.6). If

$$
p _ { n } ( f ; z ) = a _ { 0 } + a _ { 1 } ( z - z _ { 0 } ) + \cdot \cdot \cdot + a _ { n } ( z - z _ { 0 } ) ( z - z _ { 1 } ) \cdot \cdot \cdot ( z - z _ { n - 1 } )
$$

interpolates to $f a t z _ { 0 } , \ldots , z _ { n } ,$ we have

$$
\operatorname* { l i m } _ { n \to \infty } p _ { n } ( f ; z ) = f ( z ) \qquad z \in \mathcal { L } _ { \rho }
$$

and uniformly in any closed set lying in $\mathcal { L } _ { \mathfrak { p } }$ Exterior to $\mathcal { L } _ { \mathfrak { p } }$ the limit does not exist.More precisely,we have

$$
| f ( z ) - p _ { n } ( f ; z ) | \leq M ( \rho ^ { \prime } / \rho ) ^ { n } \quad \mathrm { f o r } \quad z \in \mathcal { L } _ { \rho ^ { \prime } } , \ \rho ^ { \prime } < \rho .
$$

Furthermore

$$
\operatorname* { l i m } _ { n \to \infty } \operatorname* { s u p } | a _ { n } | ^ { 1 / n } = { \frac { 1 } { \rho } } .
$$

Proof: A closed set $\pmb { S }$ lying in $\mathcal { L } _ { \mathfrak { p } }$ must also lie in some $\mathcal { L } _ { \rho ^ { \prime } }$ with $\pmb { \rho } ^ { \prime } < \pmb { \rho }$ Hence (4.4.15) implies (4.4.14),uniformly in $\pmb { S }$ We therefore prove (4.4.15). Select a $\pmb { \rho } ^ { \prime }$ sufficiently close to $\pmb { \rho }$ so that all the points $z _ { 0 } , z _ { 1 } , \ldots$ , lie in $\mathcal { L } _ { \rho ^ { \prime } }$ Select $\pmb { \rho ^ { \prime } }$ with $\rho ^ { \prime } < \rho ^ { \prime \prime } < \rho . \ \Gamma ,$ $\Gamma _ { \rho ^ { \ast } }$ consists of one or at most a finite number of mutually exterior curves which may,possibly,meet at a finite number of points.From the remarks at the end of 3.6,we have

$$
f ( z ) - p _ { n } ( f ; z ) = { \frac { 1 } { 2 \pi i } } \int _ { \Gamma _ { \rho ^ { * } } } { \frac { ( z - z _ { 0 } ) ( z - z _ { 1 } ) \cdot \cdot \cdot ( z - z _ { n } ) f ( t ) d t } { ( t - z _ { 0 } ) ( t - z _ { 1 } ) \cdot \cdot \cdot ( t - z _ { n } ) ( t - z ) } } .
$$

For $z \in \hat { \mathbf { i } } _ { \pmb { \rho } ^ { \prime } } ^ { \prime }$ we have by (4.4.8),

$$
\operatorname* { l i m } _ { n \to \infty } | ( z - z _ { 0 } ) \cdot \cdot \cdot ( z - z _ { n } ) | ^ { 1 / ( n + 1 ) } = | ( z - \zeta _ { 1 } ) \cdot \cdot \cdot ( z - \zeta _ { k } ) | ^ { 1 / k } = \rho ^ { \prime }
$$

uniformly. Hence, for some $\pmb { \rho } ^ { \prime \prime }$ with $\rho ^ { \prime } < \rho ^ { \prime \prime } < \rho ^ { \prime \prime }$ ，and for $\pmb { n }$ sufficiently large, we have

$$
| ( z - z _ { 0 } ) ( z - z _ { 1 } ) \cdot \cdot \cdot ( z - z _ { n } ) | \leq ( \rho ^ { \prime \prime \prime } ) ^ { n + 1 } , \qquad z \in \Gamma _ { \rho ^ { \prime } } .
$$

By the Maximum Principle,this inequality holds throughout $\mathcal { L } _ { \mathfrak { p ^ { \prime } } }$

Similarly we have

$$
\operatorname* { l i m } _ { n \to \infty } | ( t - z _ { 0 } ) \cdot \cdot \cdot ( t - z _ { n } ) | ^ { 1 / ( n + 1 ) } = \rho ^ { \prime \prime } , \qquad t \in \Gamma _ { \rho ^ { \star } }
$$

uniformly. Hence,for some $\rho ^ { \mathbf { i v } }$ with $\rho ^ { \prime \prime } < \rho ^ { \mathrm { i v } } < \rho ^ { \prime \prime }$ and $\pmb { n }$ suffciently large,

$$
| ( t - z _ { 0 } ) \cdot \cdot \cdot ( t - z _ { n } ) | \geq ( \rho ^ { \mathrm { i v } } ) ^ { n + 1 } , \qquad t \in \Gamma _ { \rho ^ { * } } ^ { } .
$$

We now use (4.4.18) and (4.4.19) to estimate (4.4.17):

$$
| f ( z ) - p _ { n } ( f ; z ) | \leq { \frac { 1 } { 2 \pi } } \int _ { \Gamma _ { \rho ^ { * } } } \left( { \frac { \rho ^ { \prime \prime \prime } } { \rho ^ { \mathrm { i v } } } } \right) ^ { n + 1 } { \frac { | f ( t ) | \ d s } { | t - z | } } , \qquad z \in { \mathcal { L } } _ { \rho ^ { * } } .
$$

Let $L ( \Gamma _ { \rho ^ { \circ } } ) = \mathrm { l e n g t h }$ of I $\mathbf { \phi } _ { p ^ { \prime } } ^ { \ast } , m = \operatorname* { m a x } _ { t \in \Gamma _ { \rho } } | f ( t ) |$ ， $\delta =$ minimum distance from $\Gamma _ { \rho ^ { \prime } }$ to $\Gamma _ { \rho ^ { \ast } }$ and we have

$$
| f ( z ) - p _ { n } ( f ; z ) | \leq { \frac { m L ( \Gamma _ { \rho ^ { * } } ) } { 2 \pi \delta } } \left( { \frac { \rho ^ { \prime \prime \prime } } { \rho ^ { \mathrm { i v } } } } \right) ^ { n + 1 } \leq M { \left( { \frac { \rho ^ { \prime } } { \rho } } \right) } ^ { n }
$$

for an appropriate constant $M$ independent of $\pmb { n }$

Consider next the number $\pmb { \mu }$ defined by

$$
\operatorname* { l i m } _ { n \to \infty } \operatorname* { s u p } | a _ { n } | ^ { 1 / n } = { \frac { 1 } { \mu } } .
$$

We shall prove ${ \pmb \mu } = { \pmb \rho }$ and establish (4.4.16). Suppose, first, that $\mu < \rho$ By the above work, $\operatorname* { l i m } _ { n \to \infty } p _ { n } ( f ; z )$ exists in $\mathcal { L } _ { \mathfrak { p } }$ .But by Lemma 4.4.2 and Theorem 4.4.l,this limit does not exist at a point $\textit { \textbf { z } }$ exterior to $\mathcal { L } _ { \mu }$ and distinct from $\zeta _ { 1 } , \ldots , \zeta _ { k } .$ Hence,at a point $z \left( { \ne } \left. _ { 1 } , \ldots , \right. _ { k } \right)$ belonging to $\mathcal { L } _ { \mathfrak { p } }$ but exterior to $\mathcal { L } _ { \mu }$ ,the limit both exists and does not exist.This is impossible.Suppose，secondly，that $\mu > \rho$ By Lemma 4.4.2, $p _ { n } ( f ; z )$ converges uniformly in closed subregions of $\mathcal { L } _ { \mu }$ to a function that is analytic. This is impossible,since by hypothesis $\mathcal { L } _ { \mu }$ is the largest lemniscate of analyticity.Hence ${ \pmb { \mu } } = { \pmb { \rho } }$ .This establishes (4.4.16)and the fact that we have divergence exterior to $\mathcal { L } _ { \mathfrak { p } }$

This theorem has a long history，going back,in various amounts of generality,about a century.In the form stated,it is due to Walsh.More general assumptions as to the“strength’of the limit points can and have been made.

Interpolation processes may be found that yield expansions of analytic functions in quite general regions. We shall, however, approach such approximations by other methods.

Ex.11. Let $z _ { 2 n } = 0 , z _ { 2 n + 1 } = 1 n = 0 , 1 , . . . ,$ Then $\ k = \pmb { 2 }$ and $\zeta _ { 1 } = 0$ $\zeta _ { 2 } = 1$ . Define $f ( z )$ asO in a neighborhood of $\pmb { \zeta _ { 1 } }$ and l in a neighborhood of $\pmb { \zeta _ { 2 } }$ We then have

$$
\begin{array} { r l } & { p _ { 2 n - 1 } ( f ; z ) = a _ { 0 } + a _ { 1 } z + a _ { 2 } z ( z - 1 ) + a _ { 3 } z ^ { 2 } ( z - 1 ) } \\ & { \qquad + a _ { 4 } z ^ { 2 } ( z - 1 ) ^ { 2 } + \cdot \cdot \cdot + a _ { 2 n - 1 } z ^ { n } ( z - 1 ) ^ { n - 1 } } \\ & { p _ { 2 n } ( f ; z ) = p _ { 2 n - 1 } ( f ; z ) + a _ { 2 n } z ^ { n } ( z - 1 ) ^ { n } . } \end{array}
$$

In view of (2.6.6),(3.6.1), (3.6.3),we have

$$
a _ { 2 n - 1 } = \frac { 1 } { 2 \pi i } \int _ { C } \frac { d z } { z ^ { n } ( z - 1 ) ^ { n } } , a _ { 2 n } = \frac { 1 } { 2 \pi i } \int _ { C } \frac { d z } { z ^ { n + 1 } ( z - 1 ) ^ { n } }
$$

where $\boldsymbol { \mathfrak { c } }$ is any contour containing $\boldsymbol { \zeta _ { 2 } }$ in its interior and $\pmb { \zeta _ { 1 } }$ in its exterior. Hence,

$$
\begin{array} { l } { { a _ { 2 n - 1 } = \displaystyle \frac { 1 } { ( n \mathrm { ~ - ~ } 1 ) ! } \left. \frac { d ^ { n - 1 } } { d z ^ { n - 1 } } \binom { 1 } { z ^ { n } } \right| _ { z = 1 } = ( - 1 ) ^ { n - 1 } \binom { 2 n - 2 } { n - 1 } } } \\ { { a _ { 2 n } = \displaystyle \frac { 1 } { ( n \mathrm { ~ - ~ } 1 ) ! } \left. \frac { d ^ { n - 1 } } { d z ^ { n - 1 } } \binom { 1 } { z ^ { n + 1 } } \right| _ { z = 1 } = ( - 1 ) ^ { n - 1 } \binom { 2 n - 1 } { n } \quad n = 1 , 2 , \cdot \cdot \cdot } } \\ { { a _ { 0 } = 0 . } } \end{array}
$$

The interpolation series is therefore

$$
0 + z + z ( z - 1 ) - 2 z ^ { 2 } ( z - 1 ) - 3 z ^ { 2 } ( z - 1 ) ^ { 2 } + 6 z ^ { 3 } ( z - 1 ) ^ { 2 } + \cdot \cdot \cdot .
$$

In view of the fact that lim sup $| a _ { n } | ^ { 1 / n } = 2 = 1 / \frac { 1 } { 2 }$ ，the series converges in the interior of the leminiscate $| z ( z \textrm { -- } 1 ) | \textrm { = } \frac { 1 } { 4 }$ and diverges in its exterior. The sum of the series is O in the left lobe and 1 in the right lobe.

The fairly “arbitrary” shape of lemniscates displayed in Figure 4.4.2 leads one to suspect that quite general curves can be approximated by them.This is indeed the case.

DEFINITION 4.4.2． Let $\pmb { \cal E }$ be a closed,bounded,and nonempty set in the complex plane.By the closed $\pmb { \rho }$ neighborhood of $\mathbfit { \mathbf { E } } , \mathbfit { \mathbf { E } } ( \rho )$ ,is meant the set of all points whose distance from $\pmb { \cal E }$ is $\leq \rho$ That is,

$$
E ( \rho ) = \bigcup _ { w \in E } \{ z \colon | z - w | \le \rho \} .
$$

THEOREM 4.4.4. Let $\pmb { \cal E }$ be a closed and bounded set in the complex plane. For any $\rho > 0$ ，we can find a lemniscate $\mathbf { r }$ such that $\Gamma \subseteq E ( \rho )$ $- \pmb { \cal E }$ and each component of $\pmb { \cal E }$ is separated from the exterior component of the complement of $\pmb { { \cal E } } ( \pmb { \rho } )$ by a component of $\mathbf { \Gamma } \mathbf { \Gamma } \mathbf { \Gamma } \mathbf { \Gamma } \mathbf { \Gamma } \mathbf { \Gamma } \mathbf { \Gamma }$

This theorem (which we shall not use in the sequel and whose proof we shall not give) goes back to Hilbert,and early proofs make use of potential theory.In the generality stated, the theorem is due to Fekete.His methods are somewhat more elementary.This theorem can be made the basis of interpolation processes that yield expansions in general regions.

# NOTES ON CHAPTER IV

4.2,4.4.Walsh[2],Chap.III,IV.Gontscharoff[1],Chap.V.For the “strength'’of limit points, see Korovkin[1].Fekete's proof will be found in Fekete[1].

# PROBLEMS

1. Cosh $\pmb { z }$ is approximated by a cubic polynomial found by interpolating at the points $\pm \frac { 1 } { 2 } , \pm \frac { 1 } { 2 } i$ .Estimate the error over the unit circle.

2. Let $z _ { n k }$ be the $^ { n + }$ lst roots of unity. Compute $\sigma ( z )$ . (Cf. (4.4.1))   
3.Sketch the family ${ \bf { { r } } } _ { r }$ whose foci are at $\pm 1 , \pm i$   
4.Expand $( 1 + u ) ^ { \frac { 1 } { 2 } }$ and set ${ \pmb u } = { \pmb z } ^ { 2 } - { \bf l }$ to obtain

$$
( z ^ { 2 } ) ^ { \frac { 1 } { 2 } } = 1 + { \frac { z ^ { 2 } - 1 } { 2 } } + \cdot \cdot \cdot + ( - 1 ) ^ { n - 1 } { \frac { 1 \cdot 3 \cdot 5 \cdot \cdot \cdot ( 2 n - 3 ) } { 2 \cdot 4 \cdot 6 \cdot \cdot \cdot ( 2 n ) } } ( z ^ { 2 } - 1 ) ^ { n } + \cdot \cdot \cdot \cdot .
$$

Show that the series converges to $\pmb { z }$ in the right open lobe of $| z ^ { 2 } - 1 | = 1$ and to $- z$ in the left open lobe.What are the interpolation properties of the series?

5. Following $\mathbf { E x }$ .11, let $z _ { 3 n } = 0 , z _ { 3 n + 1 } = 1 , z _ { 3 n + 2 } = - 1 . \operatorname { D e f i n e } f ( z ) { \mathrm { a s } }$ $- 1 , 0 , 1$ in the neighborhood of -1,0,1 respectively.Discuss.

6.Interpret the mode of interpolation and the statement of Theorem 4.4.3 when $z _ { 0 } , z _ { 1 } , \dotsc ,$ ,consists of the $\pmb { k }$ points $\boldsymbol { \zeta } _ { 1 } , \boldsymbol { \zeta } _ { 2 } , \ldots , \boldsymbol { \zeta } _ { k }$ repeated cyclically.

7.Discuss the convergence of series of the form

$$
a _ { 0 } + a _ { 1 } ( z - 1 ) + a _ { 2 } ( z - 1 ) ( 2 z - 1 ) + a _ { 3 } ( z - 1 ) ( 2 z - 1 ) ( 3 z - 1 ) + \cdots .
$$

8.Let $m ( z )$ map a simply connected region $B$ conformally onto the unit circle. Discuss the convergence of series of the form $\sum _ { n = 0 } ^ { \infty } a _ { n } ( m ( z ) ) ^ { n }$
