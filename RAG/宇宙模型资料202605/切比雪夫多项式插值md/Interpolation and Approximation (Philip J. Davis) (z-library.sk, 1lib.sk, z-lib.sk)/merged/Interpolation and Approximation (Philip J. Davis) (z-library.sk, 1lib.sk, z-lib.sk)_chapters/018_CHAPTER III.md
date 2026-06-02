# CHAPTER III

# Remainder Theory

The results of the previous chapter are purely algebraic.They relate to the possibility of carrying out interpolatory processes.But once these processes have been carried out,how good are the approximations that result? Remainder theory deals with this question and is consequently of great importance to numerical analysis as well as to various parts of pure analysis.

# 3.1 The Cauchy Remainder for Polynomial Interpolation

THEOREM 3.1.1． Let $f ( x ) \in C ^ { n } [ a , b ]$ and suppose that $f ^ { ( n + 1 ) } ( x )$ exists at each point of $( a , b )$ ·

If, $a \leq x _ { 0 } < x _ { 1 } < \cdot \cdot \cdot < x _ { n } \leq b$ then

$$
f ( x ) - p _ { n } ( f ; x ) = { \frac { ( x - x _ { 0 } ) ( x - x _ { 1 } ) \cdot \cdot \cdot ( x - x _ { n } ) } { ( n + 1 ) ! } } f ^ { ( n + 1 ) } ( \xi )
$$

where min $( x , x _ { 0 } , x _ { 1 } , . . . , x _ { n } ) < \xi < \operatorname* { m a x } \ ( x , x _ { 0 } , x _ { 1 } , . . . , x _ { n } )$ . The point ${ \pmb \xi }$ depends upon $x , x _ { 0 } , x _ { 1 } , \ldots , x _ { n }$ and $f$

Proof: Since $p _ { n } ( f ; x _ { k } ) = f ( x _ { k } )$ ，the function $f ( x ) - p _ { n } ( f ; x )$ vanishes at $\mathbf { \Phi } = x _ { 0 } , x = x _ { 1 } , \dots , x = x _ { n }$ Let $_ { \pmb { x } }$ be fixed and $\neq \pmb { x _ { 0 } }$ ， $x _ { 1 } , \ldots , x _ { n }$ .Set

$$
K ( x ) = { \frac { f ( x ) - p _ { n } ( f ; x ) } { ( x - x _ { 0 } ) ( x - x _ { 1 } ) \cdot \cdot \cdot ( x - x _ { n } ) } }
$$

and consider the following function of $\pmb { t }$ ：

$$
W ( t ) = f ( t ) - p _ { n } ( f ; t ) - ( t - x _ { 0 } ) ( t - x _ { 1 } ) \cdot \cdot \cdot ( t - x _ { n } ) K ( x ) .
$$

The function $W ( t )$ vanishes at $t = x _ { 0 } , t = x _ { 1 } , . . . , t = x _ { n }$ ，In addition,in virtue of (3.1.2),it vanishes at the additional point $t = x$ By the generalized Rolle's Theorem l.6.3, the function $W ^ { ( n + 1 ) } ( t )$ must vanish at a point ${ \pmb \xi }$ with min $( x , x _ { 0 } , \ldots , x _ { n } ) < \xi < \operatorname* { m a x } \left( x , x _ { 0 } , \ldots , x _ { n } \right)$ But from (3.1.3)

$$
W ^ { ( n + 1 ) } ( t ) = f ^ { ( n + 1 ) } ( t ) - ( n + 1 ) ! K ( x )
$$

so that

$$
0 = W ^ { ( n + 1 ) } ( \xi ) = f ^ { ( n + 1 ) } ( \xi ) - ( n + 1 ) ! K ( x )
$$

and therefore

$$
K ( x ) = { \frac { 1 } { ( n + 1 ) ! } } f ^ { ( n + 1 ) } ( \xi ) .
$$

Inserting this in (3.1.2) we obtain (3.1.1). If ${ \boldsymbol { x } } = { \boldsymbol { x } } _ { k }$ ，（3.1.1） holds trivially with any ${ \pmb \xi }$

COROLLARY 3.1.2. (Error in Linear Interpolation).Let $f ( x ) \in C ^ { \prime } [ a , b ]$ and suppose that $f ^ { \prime \prime } ( x )$ exists at each point of $( a , b )$ . Then, for $a \leq x \leq b$ ，

$$
f ( x ) - \left( { \frac { b - x } { b - a } } f ( a ) + { \frac { x - a } { b - a } } f ( b ) \right) = { \frac { ( x - a ) ( x - b ) } { 2 } } f ^ { \prime \prime } ( \xi ) , a < \xi < b .
$$

In most instances, the value of ${ \pmb \xi }$ is not known exactly,and the following estimate becomes of importance.

COROLLARY 3.1.3．Let

$$
R _ { n } ( f ; x ) = f ( x ) - p _ { n } ( f ; x ) .
$$

Then if

$$
f ( x ) \in C ^ { n + 1 } [ a , b ] ,
$$

$$
\left| R _ { n } ( f ; x ) \right| \leq \left\{ \operatorname* { m a x } _ { a \leq t \leq b } \left| f ^ { ( n + 1 ) } ( t ) \right| \right\} { \frac { | x - x _ { 0 } | | x - x _ { 1 } | \cdot \cdot \cdot | x - x _ { n } | } { ( n + 1 ) ! } } .
$$

Ex.l．A value for arcsin (.5335) is obtained by interpolating linearly between the values for $\mathbf {  { x } } = . 5 3 3 0$ and $x = . 5 3 4 0$ .Estimate the error committed.We have (arcsi $\mathbf { n } \ x ) ^ { \prime \prime } = x ( 1 \ - \ x ^ { 2 } ) ^ { - \frac 3 2 }$ and (arcsin $x ) ^ { \pmb { \sigma } } = ( 1 + 2 x ^ { 2 } ) ( 1 - x ^ { 2 } ) ^ { - \frac { 5 } { 2 } }$ .Since the 3rd derivative is positive over $\mathbf { 5 3 3 } \leq x \leq . 5 3 4$ ，the maximum value of the 2nd derivative occurs at $x = . 5 3 4$ .From (3.1.8),

$$
\left| R _ { 1 } \right| \le \frac { . 5 3 4 } { ( 1 - ( . 5 3 4 ) ^ { 2 } ) ^ { \frac 3 2 } } \frac { ( . 0 0 0 5 ) ^ { 2 } } 2 \le 1 . 2 \times 1 0 ^ { - 7 } .
$$

A direct computation shows that the true error is $1 . 1 0 1 \times 1 0 ^ { - 7 }$

This example points out the following facts.In order to use the estimate (3.1.8)in practical work,it is necessary to have an expression for a higher derivative of the function interpolated,and it is necessary to obtain an upper bound for the value of this high derivative over a certain interval. This might be a formidable task even for quite elementary functions.Think of obtaining the 8th derivative of arcsin $\pmb { x }$ or,worse still,of

$$
( 1 + ( x + 2 ) ^ { \frac { 1 } { 2 } } + ( x + 3 ) ^ { \frac { 1 } { 2 } } ) ^ { \frac { 1 } { 3 } } !
$$

There are several ways in which this difficulty can be overcome. This applies not only to the error estimate for interpolation，but to all error estimates of mean value type,i.e.,those involving higher derivatives.If we are working with a tabulated function,we can estimate derivatives by means of differences.The justification for this procedure is found in Corollary 3.4.4.Secondly,if we are working with analytic functions and if we are in a position to obtain an upper bound for the values of the function in the complex plane,then we can use (1.9.8) to estimate the derivative.This process is summed up by the following result..

COROLLARY 3.1.4． Let $f ( x ) \in A ( R )$ where $\pmb { R }$ is $\pmb { a }$ region that contains $[ a , b ]$ · Let $\boldsymbol { c }$ be $\pmb { a }$ closed curve that contains $[ a , b ]$ in its interior and set $L ( C ) =$ length of $C , M _ { C } = \operatorname* { m a x } _ { z \in C } | f ( z ) |$ ， $\delta =$ minimum distance from $\boldsymbol { C }$ to $[ a , b ]$ . Then,

$$
| R _ { n } ( f ; x ) | = | f ( x ) - p _ { n } ( f ; x ) | \leq { \frac { L ( C ) M _ { C } } { 2 \pi \delta ^ { n + 2 } } } | x - x _ { 0 } | | x - x _ { 1 } | \cdot \cdot \cdot | x - x _ { n } | .
$$

Ex. 2. Let $f ( x ) = [ e ^ { x ^ { 2 } - 4 } - 1 ] ^ { \frac { 1 } { 3 } }$ $[ a , b ] = [ - 1 , 1 ]$ ， $\textbf { \em n } = \textbf { 4 }$ ， $x _ { 0 } = - 1$ ， $\textstyle x _ { 1 } = - { \frac { 1 } { 2 } }$ ， $x _ { 2 } = 0 , x _ { 3 } = \frac { 1 } { 2 } , x _ { 4 } = 1 .$ Estimate the error committed at $\begin{array} { r } { x = \frac { 1 } { 4 } } \end{array}$ by interpolation at these points.Now $f ( z )$ is analytic in $| z | < 2$ ,and

$$
{ \begin{array} { r l } & { { \big | } f ( z ) { \big | } = { \big | } e ^ { z ^ { 2 } - 4 } - 1 { \big | } ^ { \frac { 1 } { 3 } } } \\ & { \qquad \leq ( { \big | } e ^ { z ^ { 2 } - 4 } { \big | } + 1 ) ^ { \frac { 1 } { 3 } } = ( e ^ { R e ( z ^ { 2 } - 4 ) } + 1 ) ^ { \frac { 1 } { 3 } } } \\ & { \qquad = ( e ^ { x ^ { 2 } - y ^ { 2 } - 4 } + 1 ) ^ { \frac { 1 } { 3 } } . } \end{array} }
$$

If $C \colon | z | = \rho , 1 < \rho < 2 ,$

$$
M _ { C } = \operatorname* { m a x } _ { z \in C } \left| f ( z ) \right| \le ( e ^ { \rho ^ { 2 } - 4 } + 1 ) ^ { \frac { 1 } { 3 } } \le 2 ^ { \frac { 1 } { 3 } } . L ( C ) = 2 \pi \rho ,
$$

and $\delta = \rho - 1$ .Write ${ \pmb \rho } = { \bf 2 } - { \pmb \varepsilon }$ Then

$$
\frac { L ( C ) M _ { C } } { 2 \pi \delta ^ { n + 2 } } \leq \frac { ( 2 \pi ) ( 2 - \varepsilon ) 2 ^ { \frac { 1 } { 3 } } } { 2 \pi ( 1 - \varepsilon ) ^ { 6 } } .
$$

Since (3.1.9) is valid for any $0 < \varepsilon < 2$ ，we may select $\varepsilon = 0$ ,leading to

$$
\begin{array} { r } { \left| R _ { 4 } ( f ; \frac { 1 } { 4 } ) \right| \le 2 ^ { \frac { 4 } { 3 } } ( \frac { 5 } { 4 } ) ( \frac { 3 } { 4 } ) ( \frac { 1 } { 4 } ) ( \frac { 1 } { 4 } ) ( \frac { 3 } { 4 } ) \approx . 1 1 . } \end{array}
$$

3.2 Convex Functions. Here we make a different sort of application of the remainder theorem.

DEFINITION 3.2.1．Let $f ( x )$ be defined on $[ a , b ]$ Then $\pmb { f }$ is said to be convex on this interval if an arbitrary chord joining two points of the curve is never below the curve.

![](../chunks/Interpolation and Approximation (Philip J. Davis) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/8c7b98737c68aeb9011e961bbac1ac880aef4cd3a37fd17e48f5944142424b7f.jpg)  
Figure 3.2.1.

Ex.1．The parabola $y = x ^ { 2 }$ is convex on any interval $[ a , b ]$

This definition can be recast in the language of interpolation. Let ${ \pmb a } \le$ $x _ { 1 } < x _ { 2 } < x _ { 3 } \leq b$ and let $p _ { 1 } ( f ; x )$ be that element of $\mathcal { P } _ { \mathbf { 1 } }$ which coincides with $f$ at $\pmb { x _ { 1 } }$ and ${ \pmb x } _ { \mathbf { 3 } }$ ；then

$$
f ( x _ { 2 } ) - p _ { 1 } ( f ; x _ { 2 } ) \leq 0 , x _ { 1 } < x _ { 2 } < x _ { 3 } .
$$

THEOREM 3.2.1. Let $f ^ { \prime \prime } ( x )$ exist on $( a , b )$ . Then $f ( x )$ is convex in every closed subinterval if and only if $f ^ { \prime \prime } ( x ) \geq 0$ on $( a , b )$

Proof: By (3.1.6),

$$
\begin{array} { r } { f ( x _ { 2 } ) - p _ { 1 } ( f ; x _ { 2 } ) = \frac 1 2 ( x _ { 2 } - x _ { 1 } ) ( x _ { 2 } - x _ { 3 } ) f ^ { \prime \prime } ( \xi ) , x _ { 1 } < \xi < x _ { 3 } , } \end{array}
$$

Since $( x _ { 2 } - x _ { 1 } ) ( x _ { 2 } - x _ { 3 } ) < 0 , f ^ { \prime } ( x ) \geq 0$ implies that the left hand side is nonpositive and hence $f$ is convex.

Suppose,conversely that $f$ is convex but that $f ^ { \prime \prime } ( x ) = k < 0$ for some ${ a < x < b }$ .Then,by definition of the second derivative,

$$
\operatorname* { l i m } _ { h \to 0 ^ { + } } { \frac { f ^ { \prime } ( x + h ) - f ^ { \prime } ( x ) } { h } } = k
$$

$$
\operatorname* { l i m } _ { h \to 0 ^ { + } } { \frac { f ^ { \prime } ( x - h ) - f ^ { \prime } ( x ) } { - h } } = k .
$$

Hence,

$$
\operatorname* { l i m } _ { h \to 0 ^ { + } } { \frac { f ^ { \prime } ( x + h ) - f ^ { \prime } ( x - h ) } { h } } = 2 k
$$

Since $k < 0$ ，for sufficiently small $\pmb { h }$ ，say for $0 < h \leq h _ { 1 }$ ，we must have $f ^ { \prime } ( x + h ) - f ^ { \prime } ( x - h ) < k _ { 1 } h , k _ { 1 } < 0 .$

$$
\int _ { 0 } ^ { h _ { 1 } } [ f ^ { \prime } ( x + h ) - f ^ { \prime } ( x - h ) ] d h < \int _ { 0 } ^ { h _ { 1 } } k _ { 1 } h d h = \frac { k _ { 1 } { h _ { 1 } } ^ { 2 } } { 2 } .
$$

Therefore

$$
f ( x + h _ { 1 } ) - 2 f ( x ) + f ( x - h _ { 1 } ) < 0 .
$$

This tells us that the chord extended from ${ \pmb x } - { \pmb h } _ { 1 }$ to $\pmb { x } + \pmb { h } _ { 1 }$ lies below the curve at $\pmb { x }$ and this contradicts the assumption of convexity.

If $f$ lacks a second derivative,we can at least say that second differences are nonnegative.

THEOREM 3.2.2． Let $f ( x )$ be convex in $[ a , b ]$

$$
\begin{array} { r } { I f \ a \leq x _ { 0 } < x _ { 0 } + h < x _ { 0 } + 2 h \leq b , } \end{array}
$$

then

$$
\Delta ^ { 2 } f ( x _ { 0 } ) = f ( x _ { 0 } + 2 h ) - 2 f ( x _ { 0 } + h ) + f ( x _ { 0 } ) \geq 0 .
$$

Proof: This inequality asserts that the midpoint of any chord lies above or on the curve.

3.3 Best Real Error Estimates;The Tschebyscheff Polynomials. The error estimate (3.1.8) for polynomial interpolation splits into two parts.The first part, $\operatorname* { m a x } _ { a \leq x \leq b } \ | f ^ { ( n + 1 ) } ( x ) |$ ，depends upon the function interpolated,but is independent of the manner in which the interpolation is carried out. The second part, ${ \frac { 1 } { ( n + 1 ) ! } } \left| x - x _ { 0 } \right| \left| x - x _ { 1 } \right| \cdot \cdot \cdot \left| x - x _ { n } \right|$ , is independent of the function，but depends upon the points.The estimate (3.1.8) was obtained by replacing $\vert f ^ { ( n + 1 ) } ( \pmb { \xi } ) \vert$ by $\operatorname* { m a x } _ { a \leq x \leq b } | f ^ { ( n + 1 ) } ( x ) |$ . This was a pure expedient,and in many cases,of course,the error predicted by (3.1.8) will be far greater than the actual error.

But since the frst part is,so to speak,beyond our control,let us look at the second part.A small error estimate will also result from a small second part. Consider the quantity $\operatorname* { m a x } _ { a \leq x \leq b } | ( x - x _ { 0 } ) ( x - x _ { 1 } ) \cdot \cdot \cdot ( x - x _ { n } ) |$ It depends upon ${ \pmb x } _ { 0 } , { \pmb x } _ { 1 } , \ldots , { \pmb x } _ { n }$ ，and this leads us to the following important and interesting question: how can we select points ${ \pmb x } _ { 0 } , { \pmb x } _ { 1 } , \ldots , { \pmb x } _ { n }$ in $[ \pmb { a } , \pmb { b } ]$ so that the maximum is as small as possible? As far as the estimate (3.1.8) is concerned, this selection of points will be the best possible selection. Indeed, it turns out that this choice of points is a happy choice as far as a number of questions in interpolation theory are concerned.The answer to the problem just posed is given by the zeros of the Tschebyscheff Polynomials,and we now turn to their theory.

In deMoivre's formula (cos $\theta + i \sin \theta ) ^ { n } = \cos n \theta + i \sin n \theta$ set cos $\pmb \theta = \pmb x$ If $0 \leq \theta \leq \pi$ sin $\theta = \sqrt { 1 - x ^ { 2 } } \geq 0$ Then,

$$
\cos n \theta + i \sin n \theta = ( x + i { \sqrt { 1 - x ^ { 2 } } } ) ^ { n } .
$$

If we expand this expression by the Binomial Theorem,and take the real parts of the resulting equation,we obtain

$$
\begin{array} { c } { { \cos n ( \operatorname { a r c c o s } x ) = \cos n \theta = x ^ { n } + { \binom { n } { 2 } } x ^ { n - 2 } ( x ^ { 2 } - 1 ) } } \\ { { + \left( { \binom { n } { 4 } } x ^ { n - 4 } ( x ^ { 2 } - 1 ) ^ { 2 } + \dots { } ^ { . } \right) } } \end{array}
$$

Thus, cos $\mathbf { \Omega } _ { n \theta }$ is a certain polynomial of degree $\pmb { n }$ in cos $\theta$

DEFINITIoN 3.3.1． The Tschebyscheff polynomial of degree $\pmb { n }$ is defined by

$$
T _ { n } ( x ) = \cos { ( n \operatorname { a r c c o s } { x } ) } = x ^ { n } + { \binom { n } { 2 } } x ^ { n - 2 } ( x ^ { 2 } - 1 ) + \cdots ( n = 0 , 1 , \ldots ) .
$$

There are a number of distinct families (in fact,infinitely many) of polynomials that go by the name of “Tschebyscheff Polynomials.” The polynomials defined by (3.3.2) are the Tschebyscheff Polynomials,par excellence.

When we have occasion to deal with other types of Tschebyscheff Polynomials,we shall include some qualifying expression.

It is easy to compute the frst few Tschebyscheff polynomials explicitly using (3.3.2). We find

$$
\begin{array} { r l } & { T _ { 0 } ( x ) = 1 } \\ & { T _ { 1 } ( x ) = x } \\ & { T _ { 2 } ( x ) = 2 x ^ { 2 } - 1 } \\ & { T _ { 3 } ( x ) = 4 x ^ { 3 } - 3 x } \\ & { T _ { 4 } ( x ) = 8 x ^ { 4 } - 8 x ^ { 2 } + 1 } \\ & { T _ { 5 } ( x ) = 1 6 x ^ { 5 } - 2 0 x ^ { 3 } + 5 x } \\ & { T _ { 6 } ( x ) = 3 2 x ^ { 6 } - 4 8 x ^ { 4 } + 1 8 x ^ { 2 } - 1 } \end{array}
$$

The Tschebyscheff polynomials satisfy a three term recurrence relation.

THEOREM 3.3.1.

$$
T _ { n + 1 } ( x ) = 2 x T _ { n } ( x ) - T _ { n - 1 } ( x ) \quad n = 1 , 2 , \ldots .
$$

Proof:

$$
( n + 1 ) \theta = \cos n \theta \cos \theta - \sin n \theta \sin \theta
$$

$$
( n - 1 ) \theta = \cos { n \theta } \cos { \theta } + \sin { n \theta } \sin { \theta }
$$

Adding and rearranging,

$$
( n + 1 ) \theta = 2 \cos n \theta \cos \theta - \cos ( n - 1 ) \theta
$$

Now set cos $\theta = \pmb { x }$ cos ${ \pmb n } \theta = { \pmb T } _ { \pmb n } ( { \pmb x } )$ ,and (3.3.4) is obtained.

COROLLARY 3.3.2.

$$
T _ { n } ( x ) = 2 ^ { n - 1 } x ^ { n } + t e r m s ~ o f ~ l o w e r ~ d e g r e e .
$$

THEOREM 3.3.3. $\pmb { T } _ { \pmb { n } } ( \pmb { x } )$ has simple zeros at the n points

$$
x _ { k } = \cos \frac { 2 k - 1 } { 2 n } \pi \quad k = 1 , 2 , \ldots , n .
$$

On the closed interval $- 1 \leq x \leq 1$ ， $\pmb { T } _ { \pmb { n } } ( \pmb { x } )$ has extreme values at the $n + 1$ points

$$
{ x _ { k } } ^ { \prime } = \cos \frac { 2 k } { 2 n } \pi \quad k = 0 , 1 , \ldots , n
$$

where it assumes the alternating values $( - 1 ) ^ { k }$

$T _ { n } ( x _ { k } ) = \cos \left( n \operatorname { a r c } \cos \left( \cos { \frac { 2 k - 1 } { 2 n } } \pi \right) \right) = \cos \left( { \frac { 2 k - 1 } { 2 } } \pi \right) = 0 ,$ $k = 1 , 2 , \ldots , n$

$$
{ T _ { n } } ^ { \prime } ( x ) = { \frac { n } { \sqrt { 1 - x ^ { 2 } } } } \sin { ( n \operatorname { a r c } \cos x ) } .
$$

Hence，Tn'(αk) = ${ T _ { n } } ^ { \prime } ( x _ { k } ) = { \frac { n } { \sqrt { 1 - { x _ { k } } ^ { 2 } } } } \sin \left( { \frac { 2 k - 1 } { 2 } } \pi \right) \ne 0$ and the zeros must be simple. Moreover,

$$
{ T _ { n } } ^ { \prime } ( x _ { k } ^ { \prime } ) = n \bigg ( 1 - \cos ^ { 2 } \frac { k \pi } { n } \bigg ) ^ { - \frac { 1 } { 2 } } \mathrm { s i n } \left( k \pi \right) = 0
$$

for $k = 1 , 2 , \ldots , n - 1 . \mathrm { N o v }$ v，

$$
T _ { n } ( x _ { k } ^ { \prime } ) = \cos \left( n \operatorname { a r c } \cos \left( \cos { \frac { k \pi } { n } } \right) \right) = \cos ( k \pi ) = ( - 1 ) ^ { k } .
$$

This is valid for $k = 0 , 1 , \ldots , n$ But for $- 1 \leq x \leq 1$ ，

$$
T _ { n } ( x ) = \cos { ( n \operatorname { a r c } \cos { x } ) }
$$

and hence $| T _ { n } ( x ) | \leq 1$ . This shows that the points ${ x _ { k } } ^ { \prime }$ are extreme points.

It is easily shown that ${ x _ { k } } ^ { \prime }$ are the only extreme points in $- 1 \leq x \leq 1$

DEFINITION 3.3.2. $\tilde { T } _ { n } ( x ) = \frac { 1 } { 2 ^ { n - 1 } } \ : T _ { n } ( x ) .$

Note that $\widetilde { T } _ { n } ( x ) = x ^ { n } +$ terms of lower degree.

THEOREM 3.3.4 (Tschebyscheff). Let $\smash { \widetilde { \mathcal { P } } } _ { n }$ designate the class of all poly-nomials of degree $\pmb { n }$ with leading coeffcient 1. Thenfor any $\pmb { \mathscr { p } } \in \widetilde { \pmb { \mathscr { P } } } _ { \pmb { \mathscr { n } } }$ ，

$$
\operatorname* { m a x } _ { - 1 \leq x \leq 1 } | \tilde { T } _ { n } ( x ) | \leq \operatorname* { m a x } _ { - 1 \leq x \leq 1 } | p ( x ) | .
$$

Proof: On $- 1 \leq x \leq 1$ ， $| \widetilde { T } _ { n } |$ assumes its maximum value, ${ \frac { 1 } { 2 ^ { n - 1 } } } , n + 1$ times at the points ${ x _ { k } } ^ { \prime } = \cos \left( { \frac { k \pi } { n } } \right) \quad k = 0 , 1 , \ldots , n .$

Suppose there were a $\pmb { p } \in \tilde { \mathcal { P } } _ { n }$ ，with $\operatorname* { m a x } _ { - 1 \leq x \leq 1 } | p ( x ) | < { \frac { 1 } { 2 ^ { n - 1 } } }$ 2n-1·Form the dif. ference $Q ( x ) = { \tilde { T } } _ { n } ( x ) - p ( x )$ .Clearly $Q ( x ) \in { \mathcal { P } } _ { n - 1 }$ .Now

$$
Q ( x _ { k } ^ { \prime } ) = \tilde { \mathcal { T } } _ { n } ( x _ { k } ^ { \prime } ) - p ( x _ { k } ^ { \prime } ) = \frac { ( - 1 ) ^ { k } } { 2 ^ { n - 1 } } - p ( x _ { k } ^ { \prime } ) , k = 0 , 1 , \dots , n .
$$

These quantities are alternatively $^ +$ and - inasmuch as $| p ( x _ { k } ^ { \prime } ) | < \frac { 1 } { 2 ^ { n - 1 } } .$ Therefore,there are $n + 1$ points where $Q ( x )$ takes values with alternating signs. $Q ( x )$ therefore has $\pmb { n }$ zeros. Since $Q \in \mathcal { P } _ { n - 1 }$ ,it must vanish identically. Thus, ${ \pmb p } ( { \pmb x } ) \equiv \tilde { { \pmb T } } _ { \pmb n } ( { \pmb x } )$ This yields

$$
\frac { 1 } { 2 ^ { n - 1 } } = \operatorname* { m a x } _ { - 1 \leq x \leq 1 } | \widetilde { T } _ { n } ( x ) | = \operatorname* { m a x } _ { - 1 \leq x \leq 1 } | p ( x ) | < \frac { 1 } { 2 ^ { n - 1 } } .
$$

This is a contradiction.

![](../chunks/Interpolation and Approximation (Philip J. Davis) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/e5b7482802ae3fb9f49e8dbb770a21f84b2f18e29df56c86e4828e753c629962.jpg)  
Figure 3.3.1 The Tschebyscheff Polynomials.

COROLLARY 3.3.5. $\operatorname* { m a x } _ { - 1 \leq x \leq 1 } | x ^ { n } + a _ { 1 } x ^ { n - 1 } + \cdot \cdot \cdot + a _ { n } | \geq { \frac { 1 } { 2 ^ { n - 1 } } } .$

COROLLARY 3.3.6. $\operatorname* { m a x } _ { a \leq x \leq b } \ | a _ { 0 } x ^ { n } + a _ { 1 } x ^ { n - 1 } + \cdot \cdot \cdot + a _ { n } | \geq | a _ { 0 } | { \frac { ( b - a ) ^ { n } } { 2 ^ { 2 n - 1 } } } .$

irf:aeterai $x = \frac { b + a } { 2 } + \frac { b - a } { 2 } t$ converting $[ \pmb { a } , \pmb { b } ]$

When polynomial interpolation is carried out on the zeros of $\boldsymbol { T } _ { n + 1 } ( \boldsymbol { x } )$ ： ${ \pmb x _ { 0 } } , { \pmb x _ { 1 } } , \ldots , { \pmb x _ { n } }$ ,then $\tilde { T } _ { n + 1 } ( x ) = ( x - x _ { 0 } ) \cdot \cdot \cdot ( x - x _ { n } )$ and we have

$$
R _ { n } ( f ; x ) = { \frac { \tilde { T } _ { n + 1 } ( x ) } { ( n + 1 ) ! } } f ^ { ( n + 1 ) } ( \xi ) , - 1 < \xi < 1 ,
$$

and

$$
| R _ { n } ( f ; x ) | \leq { \frac { 1 } { 2 ^ { n } ( n + 1 ) ! } } \operatorname* { m a x } _ { - 1 \leq x \leq 1 } | f ^ { ( n + 1 ) } ( x ) | , - 1 \leq x \leq 1 .
$$

3.4 Divided Differences and Mean Values. We begin with a formal identity for the remainder in polynomial interpolation.

THEOREM 3.4.1.

$$
\begin{array} { r l r } & { } & { R _ { n } ( f ; z ) = f ( z ) - p _ { n } ( f ; z ) ~ } \\ & { } & { ~ = [ f ( z ) , f ( z _ { 0 } ) , \ldots , f ( z _ { n } ) ] ( z - z _ { 0 } ) ( z - z _ { 1 } ) \cdot \cdot \cdot ( z - z _ { n } ) . } \end{array}
$$

Proof: According to (2.6.23),

$$
\begin{array}{c} f ( z ) , f ( z _ { 0 } ) , \dots , f ( z _ { n } ) ] = | \begin{array} { l l l l l l l } { 1 } & { 1 } & { 1 } & { 1 } & { 1 } & { 1 } & { 1 } \\ { z } & { z _ { 0 } } & { \dots } & { z _ { n } } \\ { z ^ { 2 } } & { z _ { 0 } ^ { 2 } } & { \dots } & { z _ { n } ^ { 2 } } \\ { \dots } & { \dots } & { \dots } & { \dots } & { z _ { \ast } ^ { 2 } } \\ { \dots } & { \dots } & { \dots } & { \dots } \\ { \dots } & { \dots } & { \dots } & { \dots } \\ { z ^ { n } } & { z _ { 0 } ^ { n } } & { \dots } & { z _ { n } ^ { n } } \\ { f ( z ) } & { f ( z _ { 0 } ) } & { \dots } & { f ( z _ { n } ) } \end{array} | \overset { 1 } { z } \cdot \frac { z _ { 0 } } { \dots }  & { \dots } & { z _ { n } } \end{array} | .
$$

Note that the denominator $\pmb { D }$ is in $\mathscr { P } _ { n + 1 }$ , and that it vanishes for $z _ { 0 } , z _ { 1 } , \dots ,$ $z _ { n }$ (identical columns).Hence we have

$$
D = ( - 1 ) ^ { n + 1 } ( z - z _ { 0 } ) ( z - z _ { 1 } ) \cdot \cdot \cdot ( z - z _ { n } ) { \left| \begin{array} { l l l } { 1 } & { \cdots } & { 1 } \\ { z _ { 0 } } & { \cdots } & { z _ { n } } \\ { \cdot } & { \cdot } & { \cdot } \\ { \cdot } & { \cdot } & { \cdot } \\ { z _ { 0 } ^ { n } } & { \cdots } & { z _ { n } ^ { n } } \end{array} \right| } .
$$

It follows from this and by expanding the numerator of (3.4.2) in minors of

the first column that the function

$$
\Phi ( z ) = [ f ( z ) , f ( z _ { 0 } ) , \ldots , f ( z _ { n } ) ] ( z - z _ { 0 } ) ( z - z _ { 1 } ) \cdot \cdot \cdot ( z - z _ { n } )
$$

equals $f ( z ) + q ( z )$ ，where $q ( z ) \in \mathcal { P } _ { n }$ Moreover, $\Phi ( z _ { i } ) = 0 \ i = 0 , 1 , . . . , n ,$ Hence $- q ( \boldsymbol { z } _ { i } ) = f ( \boldsymbol { z } _ { i } )$ .By the uniqueness of interpolation, $q ( z ) = - p _ { n } ( f ; z )$ and (3.4.1) follows.

COROLLARY 3.4.2． Let $f ( \pmb { x } ) \in C \left[ \pmb { a } , \pmb { b } \right]$ and suppose that $f ^ { ( n + 1 ) } ( x )$ exists at each point of $( a , b )$ .If $a \leq x _ { 0 } < x _ { 1 } < \cdot \cdot \cdot < x _ { n } \leq b _ { \mathrm { ~ ~ } }$ and ${ \pmb x } \in [ { \pmb a } , { \pmb b } ]$ then

$$
[ f ( x ) , f ( x _ { 0 } ) , \ldots , f ( x _ { n } ) ] = { \frac { f ^ { ( n + 1 ) } ( \xi ) } { ( n + 1 ) ! } }
$$

$$
( x , x _ { 0 } , \ldots , x _ { n } ) < \xi < \operatorname* { m a x } { ( x , x _ { 0 } , \ldots , x _ { n } ) } .
$$

Proof:Combine Theorem 3.4.l with Theorem 3.1.1.

Divided differences may be regarded as generalizations of derivatives. More precisely,

COROLLARY 3.4.3. Let $f ( x ) \in C ^ { n + 1 } [ a , b ]$ . Then if ${ \pmb x } \in [ { \pmb a } , { \pmb b } ]$ ，

$$
\operatorname* { l i m } _ { \substack { i = 0 , 1 , 2 , \ldots , n } } \left[ f ( x ) , f ( x _ { 0 } ) , \ldots , f ( x _ { n } ) \right] = \frac { f ^ { ( n + 1 ) } ( x ) } { ( n + 1 ) ! }
$$

In the case of equally spaced points,we obtain a mean value theorem for successive differences. Let ${ \pmb x _ { 0 } } = { \pmb a }$ ， $x _ { 1 } = a + h , . ~ . ~ . , x _ { n } = a + n h$ Then, $[ f ( x _ { 0 } ) , f ( x _ { 1 } ) , \ldots , f ( x _ { n } ) ] = { \frac { \Delta ^ { n } f ( x _ { 0 } ) } { n ! h ^ { n } } }$ Combining thiswith

COROLLARY 3.4.4. Let $f ( x ) \in C [ a , b ]$ and suppose that $f ^ { ( n ) } ( x )$ exists at each point of $( a , b )$ ; then

$$
\Delta ^ { n } f ( x _ { 0 } ) = h ^ { n } f ^ { ( n ) } ( \xi ) \qquad x _ { 0 } < \xi < x _ { n } , \quad F o r ~ n = 1 ,
$$

this is the simple mean value theorem.

Ex.1. Tables of functions frequently list the first few differences.Suppose that $f$ has been tabulated at an interval of $\pmb { h }$ and suppose that we obtain the value of $f$ at a point $\pmb { x }$ between successive abscissas $\pmb { a }$ and $\mathbf { \omega } _ { a { \mathrm { ~ + ~ } } h }$ by linear interpolation.By Cor.3.1.2,the error committed, $\scriptstyle R _ { 1 }$ is

$$
{ \frac { ( x - a ) ( x - a - h ) } { 2 } } f ^ { \prime } ( \xi ) , ~ a < \xi < a + h .
$$

By (3.4.5) $\Delta ^ { 2 } f ( a ) = h ^ { 2 } f ^ { \prime \prime } ( \xi _ { 1 } )$ so that if $^ { 6 } h$ is suffciently small" $f ^ { \prime \prime } ( \xi ) \approx \frac { 1 } { h ^ { 2 } } \Delta ^ { 2 } f ( a ) .$

Since $\operatorname* { m a x } _ { a \leq x \leq a + h } \left| ( x - a ) ( x - a - h ) \right| = \frac { h ^ { 2 } } { 4 }$ , it follows that

$$
\begin{array} { r } { | R _ { 1 } | \leq \frac { 1 } { 8 } | \Delta ^ { 2 } f ( a ) | . } \end{array}
$$

This leads to a rule of thumb long employed by computers: the error in linear interpolation does not exceed $\bigstar$ of the 2nd difference.

3.5 Interpolation at Coincident Points. In formulating the fundamental problem of polynomial interpolation，we have assumed that the interpolating points are distinct.With a proper convention as to what interpolation at coincident points means,this restriction can be overcome. The convention arises from considerations of the following sort. Suppose we interpolate to $\pmb { f } ( \pmb { x } )$ at the distinct points ${ \pmb x _ { 0 } } , { \pmb x _ { 1 } } , \ldots , { \pmb x _ { n } }$ Then,

$$
p _ { n } ( f ; x ) = \sum _ { k = 0 } ^ { n } [ f ( x _ { 0 } ) , f ( x _ { 1 } ) , \ldots , f ( x _ { k } ) ] ( x - x _ { 0 } ) \cdot \cdot \cdot ( x - x _ { k - 1 } ) .
$$

If we make ${ \pmb x _ { 1 } } , \ldots , { \pmb x _ { n } }$ “coincide” at $\pmb { x _ { 0 } }$ by allowing $x _ { 1 } , x _ { 2 } , \ldots , x _ { n } \to x _ { 0 } ,$ then,by (3.4.4),the limiting expression on the right hand side will be

$$
p _ { n } ( f ; x ) = \sum _ { k = 0 } ^ { n } { \frac { f ^ { ( k ) } ( x _ { 0 } ) } { k ! } } ( x - x _ { 0 } ) ^ { k } .
$$

The interpolation polynomial approaches the truncated Taylor expansion for $\pmb { f } ( \pmb { x } )$ at $\pmb { x _ { 0 } }$ 、This is an interpolation in which the values $f ( x _ { 0 } ) , \dots , f ^ { ( n ) } ( x _ { 0 } )$ have been prescribed. This provides an interpretation for interpolation at $\pm 1$ coincident points.

In an analogous way，the following convention is introduced. Suppose that among the $n + 1$ points ${ \pmb x _ { 0 } } , { \pmb x _ { 1 } } , \ldots , { \pmb x _ { n } }$ only $j + 1$ of them, ${ \pmb x } _ { 0 } , { \pmb x } _ { 1 } , \ldots , { \pmb x } _ { j } ,$ are distinct.Suppose that in the list of points $\pmb { x _ { 0 } }$ occurs $\pmb { n _ { 0 } }$ times, $\mathbf { \cdots } \cdot \mathbf { \cdot } \cdot \mathbf { \sigma } ^ { x _ { j } }$ occurs $\pmb { n } _ { j }$ times so that $n _ { 0 } + n _ { 1 } + \cdots + n _ { j } = n + 1$ .Then，by interpolation to $\pmb { f } ( \pmb { x } )$ at ${ \pmb x _ { 0 } } , { \pmb x _ { 1 } } , \ldots , { \pmb x _ { n } }$ we shall understand the determination of the unique polynomial of degree $\leq n$ ， ${ \pmb p } _ { \pmb n } ( \pmb x )$ ,for which

$$
p _ { n } ( x _ { 0 } ) = f ( x _ { 0 } ) , { p _ { n } } ^ { \prime } ( x _ { 0 } ) = f ^ { \prime } ( x _ { 0 } ) , \ldots , p _ { n } ^ { ( n _ { 0 } - 1 ) } ( x _ { 0 } ) = f ^ { ( n _ { 0 } - 1 ) } ( x _ { 0 } )
$$

$$
p _ { n } ( x _ { j } ) = f ( x _ { j } ) , { p _ { n } } ^ { \prime } ( x _ { j } ) = f ^ { \prime } ( x _ { j } ) , \ldots , p _ { n } ^ { ( n _ { j - 1 } ) } ( x _ { j } ) = f ^ { ( n _ { j - 1 } ) } ( x _ { j } ) .
$$

This is a problem of Hermite interpolation and the existence and uniqueness of this polynomial is guaranteed by Ex.4, Ch.2.5.

To justify this convention from the point of view of a limiting process, in the way in which (3.5.2) was derived from (3.5.l),we should have to study the limiting expressions of the divided differences when each of several groups of arguments approach distinct limits.This would lead to the notion of generalized divided differences and is a topic that will not be pursued in this book.

Having identified “coincident point”interpolation with Hermite interpolation,we point out that a remainder formula analogous to (3.l.l） is easily obtained.

THEOREM 3.5.1． Let ${ \pmb x _ { 0 } } , { \pmb x _ { 1 } } , \ldots , { \pmb x _ { n } }$ be $\pm 1$ distinct points in $[ \pmb { a } , \pmb { b } ]$ .Let $n _ { 0 } , n _ { 1 } , \ldots , n _ { n _ { n } }$ be $\pm 1$ integers $\geq 0$ Let $N = ( n _ { 0 } + n _ { 1 } + \cdots + n _ { n } ) + n$ · Designate by $H _ { N } ( f ; x )$ the unique element of $\mathcal { P } _ { N }$ for which

$$
\begin{array} { r } { H _ { N } ^ { ( k ) } ( f ; x _ { i } ) = f ^ { ( k ) } ( x _ { i } ) \quad k = 0 , 1 , \ldots , n _ { i } , \ i = 0 , 1 , \ldots , n . } \end{array}
$$

Let $f ( x ) \in C [ a , b ]$ and suppose that $f ^ { ( N + 1 ) } ( x )$ exists in $( a , b )$ ; then

$$
f ( x ) - H _ { N } ( f ; x ) = { \frac { f ^ { ( N + 1 ) } ( \xi ) } { ( N + 1 ) ! } } ( x - x _ { 0 } ) ^ { n _ { 0 } + 1 } ( x - x _ { 1 } ) ^ { n _ { 1 } + 1 } \cdot \cdot \cdot ( x - x _ { n } ) ^ { n _ { n } + 1 }
$$

where

$$
\operatorname* { m i n } \ ( x , x _ { 0 } , \ldots , x _ { n } ) < \xi < \operatorname* { m a x } \ ( x , x _ { 0 } , \ldots , x _ { n } ) .
$$

Proof: Consider $( f ( x ) - H _ { N } ( f ; x ) ) / ( x - x _ { 0 } ) ^ { n _ { 0 } + 1 } \cdot \cdot \cdot ( x - x _ { n } ) ^ { n _ { n } + 1 }$ and proceed as in the proof of Theorem 3.1.1.

3.6 Analytic Functions: Remainder for Polynomial Interpolation. Let $f ( z )$ be analytic in a closed simply connected region $\pmb { R }$ Let $c$ bea simple,closed,rectifiable curve that lies in $\pmb { R }$ and contains the distinct points $z _ { 0 } , z _ { 1 } , \ldots , z _ { n }$ in its interior. Consider the integral

$$
I = { \frac { 1 } { 2 \pi i } } \int _ { C } { \frac { f ( z ) } { ( z - z _ { 0 } ) ( z - z _ { 1 } ) \cdot \cdot \cdot ( z - z _ { n } ) } } d z .
$$

The integrand is analytic or has simple poles at $z _ { 0 } , z _ { 1 } , \ldots , z _ { n }$ Hence,by the residue theorem,

$$
I = \sum _ { k = 0 } ^ { n } { \frac { f ( z _ { k } ) } { ( z _ { k } - z _ { 0 } ) \cdot \cdot \cdot \cdot ( z _ { k } - z _ { k - 1 } ) ( z _ { k } - z _ { k + 1 } ) \cdot \cdot \cdot \cdot ( z _ { k } - z _ { n } ) } }
$$

Compare this with (2.6.4),(2.5.6) and obtain

$$
[ f ( z _ { 0 } ) , f ( z _ { 1 } ) , \cdot \cdot \cdot , f ( z _ { n } ) ] = I .
$$

By the same token,

$$
[ f ( z ) , f ( z _ { 0 } ) , \dots , f ( z _ { n } ) ] = { \frac { 1 } { 2 \pi i } } \int _ { C } { \frac { f ( t ) } { ( t - z ) ( t - z _ { 0 } ) , \dots , ( t - z _ { n } ) } } d t , \quad z \in R .
$$

From (3.4.1),

$$
\begin{array} { l } { { R _ { n } ( f ; z ) = f ( z ) - p _ { n } ( f ; z ) \ } } \\ { { \ = [ f ( z ) , f ( z _ { 0 } ) , \dots , f ( z _ { n } ) ] ( z - z _ { 0 } ) ( z - z _ { 1 } ) \cdot \cdot \cdot ( z - z _ { n } ) } } \\ { { \ = \displaystyle \frac { ( z - z _ { 0 } ) ( z - z _ { 1 } ) \cdot \cdot \cdot ( z - z _ { n } ) } { 2 \pi i } \int _ { c } \frac { f ( t ) d t } { ( t - z ) ( t - z _ { 0 } ) \cdot \cdot \cdot ( t - z _ { n } ) } . } } \end{array}
$$

We have therefore proved

THEOREM 3.6.l (Hermite). Under the above regularity conditions,

$$
\begin{array} { l } { f ( z ) - { p _ { n } } ( f ; z ) = { R _ { n } } ( f ; z ) } \\ { \displaystyle = \frac { 1 } { 2 \pi i } \int _ { C } \frac { ( z - z _ { 0 } ) ( z - z _ { 1 } ) \cdot \cdot \cdot ( z - z _ { n } ) f ( t ) d t } { ( t - z _ { 0 } ) ( t - z _ { 1 } ) \cdot \cdot \cdot ( t - z _ { n } ) ( t - z ) } } \end{array}
$$

COROLLARY 3.6.2.

$$
p _ { n } ( f ; z ) = { \frac { 1 } { 2 \pi i } } \int _ { C } { \frac { w ( t ) - w ( z ) } { w ( t ) ( t - z ) } } f ( t ) d t
$$

where $w ( z ) = ( z - z _ { 0 } ) ( z - z _ { 1 } ) \cdot \cdot \cdot ( z - z _ { n } ) .$

Proof: $f ( z ) = { \frac { 1 } { 2 \pi i } } \int _ { c } { \frac { f ( t ) } { t - z } } d t$ Subtract (3.6.5)from this.

COROLLARY 3.6.3. Formula (3.6.6) has meaning if the points $z _ { 0 } , z _ { 1 } , \ldots , z _ { n }$ are not distinct and yields the polynomial that interpolates to $f$ in the generalized sense explained in 3.5.

Proof:We shall give only a brief indication of how this goes.For simplicity,suppose that $z _ { \mathbf { 0 } }$ and $z _ { 1 }$ are coincident and the other z's are distinct. Then, $w ( z ) = ( z - z _ { 0 } ) ^ { 2 } ( z - z _ { 2 } ) \cdot \cdot \cdot ( z - z _ { n } )$ and so, $w ( z _ { 0 } ) = 0$ ， $w ^ { \prime } ( z _ { 0 } ) = 0$ From (3.6.6),

$$
p _ { n } ( f ; z _ { 0 } ) = \frac { 1 } { 2 \pi i } \int _ { C } \frac { w ( t ) f ( t ) } { w ( t ) ( t - z _ { 0 } ) } d t = f ( z _ { 0 } )
$$

and

$$
\begin{array} { c l l } { { \displaystyle p _ { n } { ' } ( f ; z _ { 0 } ) = \frac { 1 } { 2 \pi i } \int _ { C } \frac { \partial } { \partial z } \biggl ( \frac { w ( t ) - w ( z ) } { ( t - z ) } \biggr ) _ { z = z _ { 0 } } \frac { f ( t ) d t } { w ( t ) } } } \\ { { \displaystyle = \frac { 1 } { 2 \pi i } \int _ { C } \frac { f ( t ) } { ( t - z _ { 0 } ) ^ { 2 } } d t = f { ' } ( z _ { 0 } ) . } } \end{array}
$$

Now $p _ { n } ( f ; z _ { i } ) ~ i = 2 , . . . , n$ is easily computed to be $f ( z _ { i } )$ and therefore $p _ { n } ( f ; z )$ takes on interpolatory values as required.

COROLLARY 3.6.4．If $f$ is analytic at $z _ { \mathbf { 0 } }$ then

$$
\operatorname* { l i m } _ { z _ { 1 } , z _ { 2 } , \ldots , z _ { n }  z _ { 0 } } [ f ( z _ { 0 } ) , f ( z _ { 1 } ) , \ldots , f ( z _ { n } ) ] = { \frac { 1 } { n ! } } f ^ { ( n ) } ( z _ { 0 } )
$$

Proof: In the limt, $\pmb { I }$ beoomes ${ \frac { 1 } { 2 \pi i } } \int _ { C } { \frac { f ( z ) } { ( z - z _ { 0 } ) ^ { n + 1 } } } = { \frac { 1 } { n ! } } f ^ { ( n ) } ( z _ { 0 } ) .$ This is the complex analog of (3.4.4).

Ex.1． The limiting form of (3.6.5) as $z _ { 1 } , . . . , z _ { n }  z _ { 0 }$ is the Taylor Series with the exact complex remainder

$$
f ( z ) \ - \sum _ { k = 0 } ^ { n } \frac { f ^ { ( k ) } ( z _ { 0 } ) } { k ! } ( z \ - z _ { 0 } ) ^ { k } = \frac { 1 } { 2 \pi i } \int _ { C } \left( \frac { z \ - \ z _ { 0 } } { t \ - \ z _ { 0 } } \right) ^ { n + 1 } \frac { f ( t ) } { t \ - \ z } d t .
$$

![](../chunks/Interpolation and Approximation (Philip J. Davis) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/8472dd4c8ea05d9ad86c6fc6e097e52947d8b372c99f1060baedb0000e0495e0.jpg)  
Figure 3.6.1.

A moment's consideration of the residue theorem should convince the reader of the validity of the following generalization of formulas (3.6.5) and (3.6.6). Let $c$ consist of a finite number of mutually exterior curves ${ \cal C } _ { 1 } , \dots ,$ $ { C _ { r } } .  { \mathrm { L e t } } f _ { i } ( z )$ be a single valued analytic function in and on ${ C _ { i } } i = 1 , 2 , \ldots , r .$ The functions $f _ { i }$ need not be analytic continuations of one another. The total configuration of functions $f _ { i } ( z )$ will be designated by $f ( z )$ ，and $f$ will be thought of as a certain analytic configuration.If,now,each of the points $z _ { 0 } , \ldots , z _ { n }$ is contained in the interior of some $c _ { i } ,$ and if interpolation to $f ( z )$ is carried out at these points,then formulas (3.6.3),(3.6.5),and (3.6.6) are still valid.

Ex.2.Formula (3.6.5) provides a complex analog of the estimate (3.1.8). If $\delta _ { i } =$ minimum distance from ${ \boldsymbol { z } } _ { i }$ to $\pmb { c }$ and $\delta =$ minimum distance from $\pmb { z }$ to $\pmb { c }$ then,

$$
\big | R _ { n } ( f ; z ) \big | \leq \frac { L ( C ) M _ { C } \big | z - z _ { 0 } \big | \big | z - z _ { 1 } \big | \cdot \cdot \cdot \big | z - z _ { n } \big | } { 2 \pi \delta \delta _ { 0 } \delta _ { 1 } \cdot \cdot \cdot \cdot \delta _ { n } } .
$$

3.7 Peano's Theorem and Its Consequences. If we examine, once again,the Cauchy remainder for polynomial interpolation (3.1.1),we may note the prominent role played by the portion $f ^ { ( n + 1 ) } ( \xi )$ .If, for instance, $f \in \mathcal { P } _ { n }$ ，then $f ^ { ( n + 1 ) } \equiv 0$ ,and the remainder vanishes identically as it should. For a fixed $_ { \pmb { x } }$ ，we may consider the remainder $R _ { n } ( f ; x ) = f ( x ) - p _ { n } ( f ; x )$ as a linear functional which operates on $f$ and which annihilates all elements of $\mathcal { P } _ { n }$ .Peano Qbserved that if a linear functional has this property, then it must also have a simple representation in terms of $f ^ { ( n + 1 ) }$

Without striving for full generality, consider functions of class $O ^ { n + 1 } [ a , b ]$ ， and let linear functionals of the following type be defined over this class.

$$
\begin{array} { l } { { \displaystyle { \cal L } ( f ) = \int _ { a } ^ { b } [ a _ { 0 } ( x ) f ( x ) + a _ { 1 } ( x ) f ^ { \prime } ( x ) + \cdots + a _ { n } ( x ) f ^ { ( n ) } ( x ) ] d x } } \\ { { \displaystyle ~ + ~ \sum _ { i = 1 } ^ { j _ { 0 } } b _ { i 0 } f ( x _ { i 0 } ) + \sum _ { i = 1 } ^ { j _ { 1 } } b _ { i 1 } f ^ { \prime } ( x _ { i 1 } ) + \cdots + \sum _ { i = 1 } ^ { j _ { n } } b _ { i n } f ^ { ( n ) } ( x _ { i n } ) . } } \end{array}
$$

The functions ${ a } _ { i } ( \pmb { x } )$ are assumed to be piecewise continuous over $[ a , b ]$ and the points $\boldsymbol { x } _ { i j }$ to lie in $[ a , b ]$

THEOREM 3.7.1 (Peano).Let $\begin{array} { r } { { \pmb { L } } ( { \pmb { p } } ) = { \bf 0 } } \end{array}$ for all $\pmb { \mathscr { p } } \in \mathscr { P } _ { \pmb { \mathscr { n } } }$ .Then， for all$f \in C ^ { n + 1 } [ a , b ] .$

$$
L ( f ) = \int _ { a } ^ { b } f ^ { ( n + 1 ) } ( t ) K ( t ) ~ d t
$$

where

$$
K ( t ) = \frac { 1 } { n ! } L _ { x } [ ( x - t ) _ { + } ^ { n } ]
$$

and

$$
\begin{array} { l l l } { ( x - t ) _ { + } ^ { n } = ( x - t ) ^ { n } } & { } & { { x \geq t } } \\ { ( x - t ) _ { + } ^ { n } = 0 } & { } & { { x < t } . } \end{array}
$$

The notation $L _ { x } [ ( x - t ) _ { + } ^ { n } ]$ means that the functional $\pmb { L }$ is applied to $( x - t ) _ { + } ^ { n }$ considered as $^ { \pmb { a } }$ function of $\pmb { x }$

Proof:Taylor's Theorem with the exact remainder tels us that

$$
\begin{array} { l } { f ( x ) = f ( a ) + f ^ { \prime } ( a ) ( x - a ) + \cdots } \\ { \qquad + \displaystyle \frac { f ^ { ( n ) } ( a ) ( x - a ) ^ { n } } { n ! } + \displaystyle \frac { 1 } { n ! } \int _ { a } ^ { x } f ^ { ( n + 1 ) } ( t ) ( x - t ) ^ { n } d t . } \end{array}
$$

Wemayevidentlywitht $\frac { 1 } { n ! } \int _ { a } ^ { b } f ^ { ( n + 1 ) } ( t ) ( x - t ) _ { + } ^ { n }$ dt. Now apply $\pmb { L }$ to both sides of this expansion and recall that $\pmb { L }$ vanishes for all elements of $\mathcal { P } _ { n }$ .This yields

$$
L ( f ) = { \frac { 1 } { n ! } } L { \int } _ { a } ^ { b } f ^ { ( n + 1 ) } ( t ) ( x - t ) _ { + } ^ { n } d t .
$$

Since we have assumed a form (3.7.1) for $\pmb { L }$ ，we are working under hypotheses which allow an interchange of the functional $\pmb { L }$ with the integral in (3.7.5). Hence,

$$
L ( f ) = \frac { 1 } { n ! } \int _ { a } ^ { b } f ^ { ( n + 1 ) } ( t ) L _ { \alpha } [ ( x - t ) _ { + } ^ { n } ] \ d t .
$$

The function $\pmb { K } ( t )$ is called the Peano Kernel associated with the functional $\pmb { L }$

COROLLARY 3.7.2. If, in addition to the above hypotheses, the kernel $\pmb { K } ( t )$ does not change its sign on $[ \pmb { a } , \pmb { b } ]$ then for all $f \in C ^ { n + 1 } [ a , b ] .$

$$
L ( f ) = { \frac { f ^ { ( n + 1 ) } ( \xi ) } { ( n + 1 ) ! } } L ( x ^ { n + 1 } ) , \qquad a \leq \xi \leq b
$$

Proof: From (3.7.2) and (1.4.5),

$$
L ( f ) = f ^ { ( n + 1 ) } ( \xi ) { \int } _ { a } ^ { b } K ( t ) d t \qquad a \leq \xi \leq b
$$

Insert $f = x ^ { n + 1 }$ in (3.7.8) and obtain

$$
L ( x ^ { n + 1 } ) = ( n + 1 ) ! \int _ { a } ^ { b } K ( t ) d t
$$

Combining these yields (3.7.7).

A functional that satisfies the conditions $K ( t ) \geq 0$ (or $K ( t ) \leq 0 )$ on $[ a , b ]$ is known as a positive (or negative) functional of order $\pmb { n }$ . Many of the error functionals that occur in numerical analysis are of this type.

Ex.l. Kowalewski's Exact Remainder for Polynomial Interpolation. Let $x , x _ { 0 } , \ldots , x _ { n }$ be fixed in $[ a , b ]$ Let $L ( f ) = R _ { n } ( f ; x ) = f ( x ) - \sum _ { k = 0 } ^ { n } f ( x _ { k } ) \ell _ { k } ( x ) .$ (See (2.5.9)).

Then,

$$
\begin{array} { l } { n ! K ( t ) = L _ { x } ( x - t ) _ { + } ^ { n } = ( x - t ) _ { + } ^ { n } - \displaystyle \sum _ { k = 0 } ^ { n } ( x _ { k } - t ) _ { + } ^ { n } \ell _ { k } ( x ) } \\ { = \displaystyle \sum _ { k = 0 } ^ { n } [ ( x - t ) _ { + } ^ { n } - ( x _ { k } - t ) _ { + } ^ { n } ] \ell _ { k } ( x ) . } \end{array}
$$

The last equality follows from (2.5.13).We now put this in a more convenient form. For fixed $\pmb { k }$ we have by (3.7.4),

$$
\begin{array} { l } { { \displaystyle { \mathrm {  ~ \psi ~ } _ { a } ^ { * b } } [ ( x - t ) _ { + } ^ { n } ~ - ( x _ { k } - t ) _ { + } ^ { n } ] f ^ { ( n + 1 ) } ( t ) ~ d t } \ ~ } \\ { { \displaystyle ~ = \int _ { a } ^ { x } [ ( x - t ) ^ { n } ~ - ( x _ { k } - t ) ^ { n } ] f ^ { ( n + 1 ) } ( t ) ~ d t ~ + \int _ { x _ { k } } ^ { x } ( x _ { k } - t ) ^ { n } f ^ { ( n + 1 ) } ( t ) ~ d t } \ ~ } \end{array}
$$

Hence,

$$
\begin{array} { l } { { \displaystyle \imath ! \int _ { a } ^ { b } K ( t ) f ^ { ( n + 1 ) } ( t ) ~ d t } } \\ { { \displaystyle = \int _ { a } ^ { \imath } { \hat { f } ^ { ( n + 1 ) } ( t ) \sum _ { k = 0 } ^ { n } [ ( x - t ) ^ { n } - ( x _ { k } - t ) ^ { n } ] \ell _ { k } ( x ) ~ d t } + \sum _ { k = 0 } ^ { n } \ell _ { k } ( x ) \int _ { x _ { k } } ^ { x } ( x _ { k } - t ) ^ { n } f ^ { ( n + 1 ) } ( t ) ~ d t } } \end{array}
$$

The inner sum in the second integral may be transformed by (2.5.13):

$$
\sum _ { k = 0 } ^ { n } [ ( x - t ) ^ { n } - ( x _ { k } - t ) ^ { n } ] \ell _ { k } ( x ) = ( x - t ) ^ { n } - \sum _ { k = 0 } ^ { n } ( x _ { k } - t ) ^ { n } \ell _ { k } ( x ) .
$$

Since $\sum _ { k = 0 } ^ { n } ( x _ { k } - t ) ^ { n } \ell _ { k } ( x ) = p _ { n } ( ( x - t ) ^ { n } ; x ) = ( x - t ) ^ { n }$ ，the inner sum vanishes   
identically.Thus,finally,

$$
L ( f ) = f ( x ) - p _ { n } ( f ; x ) - \frac { 1 } { n ! } \sum _ { k = 0 } ^ { n } \ell _ { k } ( x ) { \int _ { x _ { k } } ^ { x } ( x _ { k } - t ) ^ { n } f ^ { ( n + 1 ) } ( t ) d t } , \quad f \in C ^ { n + 1 } [ a , b ] .
$$

Ex.2. (Integral remainder for linear interpolation.) The cage $\pmb { n } = 1$ ， $x _ { 0 } = a _ { : }$ $\pmb { x _ { 1 } } = \pmb { b }$ is ailaltet() $\ell _ { 0 } ( x ) = { \frac { x - b } { a - b } } , \ell _ { 1 } ( x ) = { \frac { x - a } { b - a } }$ From

$$
\begin{array} { l } { \displaystyle f ( x ) - \frac { x - b } { a - b } f ( a ) - \frac { x - a } { b - a } f ( b ) } \\ { \displaystyle \qquad = \frac { x - b } { b - a } \int _ { a } ^ { x } ( t - a ) f ^ { \prime } ( t ) d t + \frac { x - a } { b - a } \int _ { x } ^ { b } ( t - b ) f ^ { \prime } ( t ) d t . } \end{array}
$$

Introduce the following function defined over the square $a \leq x \leq b , a \leq t \leq b$

$$
G ( x , t ) = \left\{ { \begin{array} { l l } { \displaystyle ( t - a ) ( x - b ) } & { \quad t \leq x } \\ { \displaystyle b - a } & { \quad t \leq x } \\ { \displaystyle ( \frac { x - a ) ( t - b ) } { b - a } } & { \quad x \leq t . } \end{array} } \right.
$$

Then we may write (3.7.1) in the form

$$
R _ { 1 } ( f ; x ) = \int _ { a } ^ { b } G ( x , t ) f ^ { \prime \prime } ( t ) d t
$$

The function $ { \boldsymbol { G } } (  { \boldsymbol { { x } } } , t )$ is, for fixed $_ { \pmb { x } }$ ,the Peano kernel for $R _ { 1 } ( f )$

Let $\pmb { h } ( \pmb { x } ) \in C [ \pmb { a } , \pmb { b } ]$ and $H ^ { \prime \prime } ( x ) = h ( x )$ .Set

$$
\phi ( x ) = \int _ { a } ^ { b } G ( x , t ) h ( t ) ~ d t .
$$

Then, by (3.7.13),

$$
\phi ( x ) = H ( x ) - p _ { 1 } ( H ; x ) \quad \mathrm { { s o \ t h a t } } \quad \phi ^ { \prime \prime } ( x ) = H ^ { \prime \prime } ( x ) = h ( x ) .
$$

Furthermore, $\phi ( a ) = R _ { 1 } ( H ; a ) = 0 , \phi ( b ) = R _ { 1 } ( H ; b ) = 0 ,$

Therefore the integral (3.7.14) solves the differential problem

$$
\begin{array} { c } { { \phi ^ { \prime \prime } ( x ) = h } } \\ { { \phi ( a ) = \phi ( b ) = 0 . } } \end{array}
$$

The function $ { \boldsymbol { G } } (  { \boldsymbol { { x } } } , t )$ is known as the Green's function for the diferential system (3.7.15).These remarks indicate the close relationship between Peano's kernels and Green's functions,and hence between interpolation theory and the theory of linear differential equations.Unfortunately，we shall not be able to pursue this relationship.

Ex. 3. Let ${ \pmb x } _ { 1 } = { \pmb x } _ { 0 } + { \pmb h } ,$ $x _ { 2 } = x _ { 0 } + 2 h$ ， ${ x _ { 3 } = x _ { 0 } + 3 h }$ and set

$$
L ( f ) = - f ( x _ { 0 } ) + 3 f ( x _ { 1 } ) - 3 f ( x _ { 2 } ) + f ( x _ { 3 } ) = \Delta ^ { 3 } f ( x _ { 0 } ) .
$$

$\pmb { L }$ annihilates all elements of $\mathscr { P } _ { \mathbf { 2 } }$ Hence, $\textbf { \em n } = \textbf { 2 }$ and

$$
K ( t ) = \frac { 1 } { 2 ! } L ( x - t ) _ { + } ^ { 2 } .
$$

If we write this out explicity we find

$$
\begin{array} { r l r } { 2 K ( t ) } & { = ( x _ { 3 } - t ) ^ { 2 } - 3 ( x _ { 2 } - t ) ^ { 2 } + 3 ( x _ { 1 } - t ) ^ { 2 } = ( t - x _ { 0 } ) ^ { 2 } , } & { x _ { 0 } \leq t \leq x _ { 1 } } \\ & { = ( x _ { 3 } - t ) ^ { 2 } - 3 ( x _ { 2 } - t ) ^ { 2 } } & { x _ { 1 } \leq t \leq x _ { 2 } } \\ & { = ( x _ { 3 } - t ) ^ { 2 } } & { x _ { 2 } \leq t \leq x _ { 3 } } \end{array}
$$

The kernel $\pmb { K } ( t )$ consists of 3 parabolic arches and is of class $O ^ { 1 } [ x _ { 0 } , x _ { 3 } ]$ Thus,for $f \in C ^ { 3 } [ x _ { 0 } , x _ { 3 } ] ,$ 、

$$
L ( f ) = \Delta ^ { 3 } f ( x _ { 0 } ) = \int _ { x _ { 0 } } ^ { x _ { 3 } } K ( t ) f ^ { \prime \prime \prime } ( t ) d t .
$$

Note that $\pmb { K } ( t ) \geq \mathbf { 0 }$ .We may apply (3.7.7) yielding

$$
\Delta ^ { 3 } f ( x _ { 0 } ) = \frac { f ^ { ( 3 ) } ( \xi ) } { 3 ! } \Delta ^ { 3 } ( x ^ { 3 } ) = h ^ { 3 } f ^ { ( 3 ) } ( \xi ) . \mathrm { C f . } ( 3 . 4 . 5 ) .
$$

Similar formulas hold for differences of all orders.

![](../chunks/Interpolation and Approximation (Philip J. Davis) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/520b7eefdabe94fd612b164bbc4328fd6cc057482339a00846dec7ae78886098.jpg)  
Figure 3.7.1 Peano Kernel for 3rd Difference, ${ \pmb x _ { 0 } } = { \bf 0 }$ ， $\pmb { h } = \pmb { 1 }$

Ex.4. The Trapezoidal Rule and the Euler-MacLaurin Summation Formula. Let

$$
L ( f ) = \int _ { a } ^ { b } f ( x ) d x - { \frac { b - a } { 2 } } [ f ( a ) + f ( b ) ]
$$

be the error in estimating the definite integral $\int _ { a } ^ { b } f ( x ) d x$ by the trapezoidal rule $\frac { 1 } { 2 } ( b - a ) [ f ( a ) + f ( b ) ]$ .The rule is exact for linear functions,and,in particular, for constants.If we select $\pmb { n } = \pmb { 0 }$ ,we have

$$
( x \ - t ) _ { + } ^ { 0 } = S ( x , t ) \ = \left\{ { \begin{array} { l l l } { { 1 } } & { { \mathrm { f o r } } } & { { x \geq t } } \\ { { } } & { { } } & { { } } \\ { { 0 } } & { { \mathrm { f o r } } } & { { x < t . } } \end{array} } \right.
$$

Then

$$
\begin{array} { l } { \displaystyle L _ { x } ( S ( x , t ) ) = \int _ { a } ^ { b } { S ( x , t ) d x - \frac { b - a } { 2 } [ S ( a , t ) + S ( b , t ) ] } } \\ { \displaystyle = = \int _ { t } ^ { b } { d x - \frac { b - a } { 2 } [ 0 + 1 ] = \frac { 1 } { 2 } ( a + b ) - t } , ~ { t > a } . } \end{array}
$$

# Therefore

$$
L ( f ) = - \int _ { a } ^ { b } ( t - { \frac { 1 } { 2 } } ( a + b ) ) f ^ { \prime } ( t ) d t .
$$

Consider, next, the extended trapezoidal rule,

$$
\begin{array}{c} { \begin{array} { r l } { L ( f ) \ = \displaystyle \int _ { a } ^ { b } f ( x ) \ d x \ - \frac { b \ - a } { n } [ \frac { f ( a ) } { 2 } + f ( a \ + \sigma ) \ + f ( a \ + \ 2 \sigma ) \ + \ \cdot \ \cdot \ \cdot } \end{array}  } & { } \\ { \ + \ f ( a \ + \ ( n \ - 1 ) \sigma ) \ + \ \frac { f ( b ) } { 2 } ] , \quad \sigma \ = \frac { 1 } { n } \ ( b \ - a ) . } \end{array} 
$$

An expression analogous to (3.7.19） is most conveniently obtained by adding expressions of this form for each subinterval.

$$
L ( f ) \ = \ - \sum _ { k = 0 } ^ { n - 1 } \int _ { a + k \sigma } ^ { a + ( k + 1 ) \sigma } ( t \ - \ ( a \ + \ ( k \ + \ \frac 1 2 ) \sigma ) ) f ^ { \prime } ( t ) \ d t .
$$

In particular,if we select $\textstyle a = 0 , b = n , \sigma = 1$ ,then over $k \leq t \leq k + 1 , t - k - \frac { 1 } { 2 }$ becomes $t - [ t ] - \frac { 1 } { 2 }$ ，where $[ t ]$ is the largest integer contained in $\pmb { t }$ ，and we rewrite (3.7.21) as

$$
\begin{array} { l } { \displaystyle { \int _ { 0 } ^ { n } f ( x ) d x + \frac { f ( 0 ) + f ( n ) } { 2 } - [ f ( 0 ) + f ( 1 ) + \cdots + f ( n ) ] } } \\ { \displaystyle { \qquad = \int _ { 0 } ^ { n } ( [ t ] - t + \frac { 1 } { 2 } ) f ^ { \prime } ( t ) d t } . } \end{array}
$$

This is the simplest version of the Euler-MacLaurin summation formula.

Ex.5.Remainder in Simpson's Rule.Let

$$
\begin{array} { r } { L ( f ) = \displaystyle \int _ { - 1 } ^ { + 1 } f ( x ) d x - \frac { 1 } { 3 } f ( - 1 ) - \frac { 4 } { 3 } f ( 0 ) - \frac { 1 } { 3 } f ( 1 ) . \quad L ( p ) = 0 \quad \mathrm { i f } \quad p \in \mathscr { P } _ { 3 } . } \end{array}
$$

![](../chunks/Interpolation and Approximation (Philip J. Davis) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/cda9e12c2bd606b84eb201edf23f4c3fd0e96cf360c12b82fa5ed30a62b132bd.jpg)  
Figure 3.7.2 Kernel for Simpson's Rule.

Applying (3.7.3) we find $6 K ( t ) = L _ { \alpha } [ ( x - t ) _ { + } ^ { 3 } ]$ or,

$$
\begin{array} { l c r } { { K ( t ) = - \frac { 1 } { 7 2 } ( 1 - t ) ^ { 3 } ( 3 t + 1 ) \qquad } } & { { 0 \leq t \leq 1 } } \\ { { K ( t ) = K ( - t ) \qquad } } & { { - 1 \leq t \leq 0 } } \end{array}
$$

Note that ${ \mathbf { } } K ( t ) \leq 0$ so that Corollary 3.7.2 is applicable:

$$
L ( f ) = \frac { 1 } { 4 ! } f ^ { ( 4 ) } ( \xi ) L ( x ^ { 4 } ) = \frac { f ^ { ( 4 ) } ( \xi ) } { 4 ! } \left( - \frac { 4 } { 1 5 } \right) = - \frac { f ^ { ( 4 ) } ( \xi ) } { 9 0 } .
$$

This leads to the following error for Simpson's rule:

$$
\int _ { - 1 } ^ { 1 } f ( x ) d x = \textstyle { \frac { 1 } { 3 } } f ( - 1 ) + \frac { 4 } { 3 } f ( 0 ) + \frac { 1 } { 3 } f ( 1 ) - \frac { f ^ { ( 4 ) } ( \xi ) } { 9 0 } , - 1 \le \xi \le 1 .
$$

3.8 . Interpolation in Linear Spaces;General Remainder Theorem. We cannot say too much in the general case,for the underlying structure is too meagre.But it is instructive to derive what result we can,and this will round off the formal algebraic work of 2.5,2.6.

Given an element $_ { \pmb { x } }$ in a linear space $\pmb { X }$ ， we interpolate to $\pmb { x }$ by an appro-priate linear combination of $x _ { 1 } , \ldots , x _ { n }$ ， $a _ { 1 } x _ { 1 } + \cdots + a _ { n } x _ { n }$ ，such that $L _ { i } ( a _ { 1 } x _ { 1 } + \cdot \cdot \cdot + a _ { n } x _ { n } ) = L _ { i } ( x ) \quad i = 1 , 2 , \ldots ,$ $\pmb { n }$ .Let

$$
\pmb { x } _ { R } = \pmb { x } - ( \pmb { a _ { 1 } } \pmb { x _ { 1 } } + \cdot \cdot \cdot + \pmb { a _ { n } } \pmb { x _ { n } } ) .
$$

Then, $L _ { i } ( x _ { R } ) = 0 \quad i = 1 , 2 , \ldots , n .$

THEOREM 3.8.1. Under the assumption that $| L _ { i } ( x _ { j } ) | \neq 0$ , we have

$$
\begin{array} { r } { x _ { R } = \left| { \begin{array} { c c c c c } { x } & { x _ { 1 } } & { \cdot \cdot \cdot } & { x _ { n } } \\ { L _ { 1 } ( x ) } & { L _ { 1 } ( x _ { 1 } ) } & { \cdot \cdot \cdot } & { L _ { 1 } ( x _ { n } ) } \\ { \cdot } & & & { \cdot } \\ { \cdot } & & & { \cdot } \\ { \cdot } & & & & { \cdot } \\ { L _ { n } ( x ) } & { L _ { n } ( x _ { 1 } ) } & { \cdot \cdot \cdot } & { L _ { n } ( x _ { n } ) } \end{array} } \right| \div \left| { \begin{array} { c c c c c } { L _ { 1 } ( x _ { 1 } ) } & { L _ { 1 } ( x _ { 2 } ) } & { \cdot \cdot \cdot } & { L _ { 1 } ( x _ { n } ) } \\ { \cdot } & { \cdot } & & { \cdot } \\ { \cdot } & { \cdot } & & { \cdot } \\ { \cdot } & { \cdot } & & { \cdot } \\ { L _ { n } ( x _ { 1 } ) } & { L _ { n } ( x _ { 2 } ) } & { \cdot \cdot \cdot } & { L _ { n } ( x _ { n } ) } \end{array} } \right| } \end{array}
$$

Proof:It is clear by expanding the numerator of (3.8.l) by the minors of its first row that the right hand side of(3.8.l) is a linear combination of ${ \pmb x } , { \pmb x } _ { 1 } , \dots , { \pmb x } _ { n }$ ，and that the coefficient of $_ { \pmb { x } }$ is precisely l． Applying $L _ { i }$ to the right hand side(which we may do by letting it operate on each element of the first row),we see that this row is identical with the $( i + 1 ) { \bf s } t$ rowand hence $L _ { i } ( x _ { R } ) = 0 , i = 1 , 2 , . . . , n$ 、Thus,the expression (3.8.l) has all the properties the remainder element ${ \pmb x } _ { R }$ should have.

# NOTES ON CHAPTER III

3.2 Hardy,Littlewood,and Polya [1],pp.70-75.R.P.Boas,Jr. [4] pp. 142-150.

3.3The Tschebyscheff polynomials are everywhere dense in the literature of numerical analysis,approximation theory，and special function theory.The National Bureau of Standards,Table of Chebyshev Polynomials [l] has an introduction by C.Lanczos that summarizes the properties of these famous polynomials and indicates their use in numerical analysis.

3.6J.L.Walsh [2] p.50. For coincident points of interpolation,p.53. 3.7G.Peano [l],[2]. In recent years,Arthur Sard has called attention to the utility of Peano's Theorem.A.Sard [l],[2].Kowalewski's Remainder: G.Kowalewski [1] pp.21-24.For some of the kernels see Sard [l],Milne [1],Kuntzmann [1] pp.44-49,152-157.

3.8See references to 2.5,2.6.

# PROBLEMS

1. $\bf { L o g _ { 1 0 } }$ 12.7 has been computed by looking up $\bf { l o g } _ { 1 0 }$ 12 and $\bf { l o g } _ { 1 0 }$ 13 and interpolating linearly between these values.Show that the error incurred is $\leq . 0 0 4$

2.Formulate rules of thumb for the accuracy of quadratic,cubic,and quartic interpolation on equidistant points.

3.A polynomial of degree $\pmb { n }$ ， $\scriptstyle { \pmb { \mathscr { p } } } _ { \pmb { \mathscr { n } } } ( { \pmb { \mathscr { x } } } )$ ,coincides with $e ^ { \mathfrak { X } }$ at the points ${ \frac { 0 } { n } } , { \frac { 1 } { n } } , \ldots ,$ $\frac { n - 1 } { n } , \frac { n } { n }$ .How large shall $\pmb { n }$ be taken so as to insure that $\left| e ^ { x } - p _ { n } ( x ) \right| \leq 1 0 ^ { - 6 }$ over $0 \leq x \leq 1 \eta$ .

4.Let $f ( z ) = e ^ { z ^ { 2 } }$ $\scriptstyle R _ { 1 0 } ( f ; { \frac { 1 } { 2 0 } } )$

5. Same problem with $f ( z ) = { \sqrt { 9 + { \sqrt { z } } } }$

6. Write explicitly the remainder for simple osculatory interpolation at the $\textbf { \em n } + \textbf { 1 }$ points $x _ { 0 } , x _ { 1 } , \ldots , x _ { n }$ If $f ^ { ( 2 n + 2 ) } ( x ) \geq 0$ ,the interpolant never exceeds the function over the range of interest.

7. If $\pmb { \mathcal { P } } \geq \pmb { 1 }$ ， $\scriptstyle y \ = x ^ { p }$ is convex on $[ \mathbf { 0 } , \pmb { a } ]$ for any $\textbf { \em a } > \mathbf { 0 }$

8.A monotone increasing function of a convex function is itself convex. True or false?

9. Find necessary and sufficient conditions on the a's in order that $\sum _ { n = 0 } ^ { 4 } a _ { n } x ^ { n }$ be convex on $- 1 \leq x \leq 1$

10. In particular,

$$
T _ { m } ( T _ { n } ( x ) ) = T _ { n } ( T _ { m } ( x ) ) = T _ { m n } ( x ) .
$$

$$
T _ { n } ( 2 x ^ { 2 } \ : - \ : 1 ) = 2 T _ { n } { } ^ { 2 } ( x ) \ : - \ : 1 .
$$

11.

$$
T _ { m } ( x ) T _ { n } ( x ) = \frac { } { } [ T _ { m + n } ( x ) + T _ { m - n } ( x ) ] .
$$

12. Prv he

$$
\begin{array} { l l } { \displaystyle \mathrm { i d e n t i t i e s } \int T _ { 0 } ( x ) d x = T _ { 1 } ( x ) , \int T _ { 1 } ( x ) d x = \frac { 1 } { 4 } T _ { 2 } ( x ) , } \\ { \displaystyle \int T _ { n } ( x ) d x = \frac { 1 } { 2 } \bigg ( \frac { T _ { n + 1 } ( x ) } { n + 1 } - \frac { T _ { n - 1 } ( x ) } { n - 1 } \bigg ) \quad n > 1 . } \end{array}
$$

$$
\mathrm { ~ : ~ } f ^ { \prime } ( 0 ) \ - \frac { 1 } { 2 h } \left[ f ( h ) \ - f ( - h ) \right] \ = \int _ { - 1 } ^ { 1 } f ^ { ( 3 ) } ( x ) K ( x ) \ d x \quad 0 \ < h < 1
$$

$$
K ( x ) = \left\{ \begin{array} { l l } { \displaystyle - \frac { ( x + h ) ^ { 2 } } { 4 h } } & { - h \leq x \leq 0 } \\ { \displaystyle - \frac { ( x - h ) ^ { 2 } } { 4 h } } & { \quad 0 \leq x \leq h } \\ { \quad 0 } & { \quad \mathrm { o t h e r w i s e } } \end{array} \right.
$$

14.Derive this formula directly by integration by parts.

15. Show that $f ( - 1 ) = f ( 0 ) - f ^ { \prime } ( 0 ) + { \textstyle \frac { 1 } { 2 } } f ^ { \prime } ( 0 ) + \int _ { - 1 } ^ { 1 } f ^ { \prime \prime } ( t ) K ( t ) d t$

where

$$
K ( t ) = \left\{ \begin{array} { c c } { { - \frac { 1 } { 4 } ( 1 - t ) ^ { 2 } } } & { { 0 < t \le 1 } } \\ { { - \frac { 1 } { 4 } ( 1 + t ) ^ { 2 } } } & { { - 1 \le t \le 0 } } \end{array} \right.
$$

16.Show that $- { \textstyle \frac { 1 } { 4 } } f ( - 1 ) - { \textstyle \frac { 1 } { 2 } } f ( 0 ) + { \textstyle \frac { 3 } { 4 } } f ( 1 ) - f ^ { \prime } ( { \textstyle \frac { 1 } { 4 } } ) = \int _ { - 1 } ^ { 1 } f ^ { ( 3 ) } ( x ) K ( x ) d x$

where

$$
K ( x ) = \left\{ \begin{array} { l l } { \mathfrak { k } ( 1 + x ) ^ { 2 } \quad \quad } & { - 1 \leq x < 0 } \\ { \mathfrak { k } ( 1 + 2 x + 3 x ^ { 2 } ) \quad \quad } & { 0 \leq x < \frac { 1 } { 4 } } \\ { \mathfrak { z } ( 1 - x ) ^ { 2 } \quad } & { \frac { 1 } { 4 } \leq x \leq 1 } \end{array} \right.
$$

17.Find the Peano kernel for $\Delta ^ { 4 } f ( x _ { 0 } ) , h = 1$ ·

18. Derive the following formula of Euler-MacLaurin type

$$
\begin{array} { l } { { \displaystyle { \int _ { a } ^ { b } f ( x ) d x = \frac { 1 } { 2 } ( b - a ) ( f ( a ) + f ( b ) ) + \frac { 1 } { 1 2 } ( b - a ) ^ { 2 } ( f ^ { \prime } ( a ) - f ^ { \prime } ( b ) ) } } } \\ { { \mathrm { ~ + ~ } \displaystyle { \frac { 1 } { 4 ! } \int _ { a } ^ { b } ( x - a ) ^ { 2 } ( x - b ) ^ { 2 } f ^ { ( 4 ) } ( x ) d x } . } } \end{array}
$$

19.Study the continuity class of $\pmb { K } ( t )$ for various functionals.
