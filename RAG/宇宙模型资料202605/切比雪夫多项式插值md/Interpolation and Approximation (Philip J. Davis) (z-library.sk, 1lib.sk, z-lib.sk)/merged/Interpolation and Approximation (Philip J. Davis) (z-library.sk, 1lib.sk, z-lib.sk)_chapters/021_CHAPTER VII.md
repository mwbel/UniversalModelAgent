# CHAPTER VII

# Best Approximation

7.1What is Best Approximation? In Chapter VI,we have studied several situations in which functions can be approximated arbitrarily closely by polynomials.It goes without saying that in order to achieve more and more accuracy in the approximations,the approxiniants will (in general) have to be of higher and higher degree. But it is of considerable importance both for theory as well as for numerical practice to accomplish as much as possible with polynomials of a fixed degree.For instance,how well can the function $x ^ { 4 }$ be approximated over $0 \le x \le 1$ bya straight line?In order to answer such a question,the notion of closeness of approximation must be defined.Frequently,we measure the closeness of approximation over the interval by taking the maximum deviation between the function and its approximant.At other times,we may wish to use alternate definitions. The maximum deviation considered over a finite set of points,or the integral of the square of the deviations are frequently employed.

Once a criterion of closeness of approximation has been decided upon, we may begin to answer specific questions.We may,for instance,look into the problem of whether,among the elements of $\mathcal { P } _ { n }$ ，there is one whose closeness to a given function $f ( x )$ is not exceeded by any other element of $\mathcal { P } _ { n }$ .If there is,it is known as a best approximation to $f ( x )$ . Change the criterion of closeness of approximation and the best approximation will change.

Ex.1．Approximate $\begin{array} { r } { \pmb { y } = x ^ { 4 } } \end{array}$ over [0,l] by a straight line $\boldsymbol { l } ( \boldsymbol { x } )$ so that

$$
\int _ { 0 } ^ { 1 } ( x ^ { 4 } - l ( x ) ) ^ { 2 } d x = \mathrm { { \ m i n i m u m } }
$$

$$
\int _ { 0 } ^ { 1 } ( x ^ { 4 } - l ( x ) ) ^ { 2 } d x + \int _ { 0 } ^ { 1 } ( d / d x ( x ^ { 4 } - l ( x ) ) ) ^ { 2 } d x = \mathrm { { m i n i m u m } }
$$

$$
\operatorname* { m a x } _ { 0 \leq x \leq 1 } \ \left| x ^ { 4 } - l ( x ) \right| = \mathrm { { m i n i m u m } }
$$

The answers are given by

$$
{ \begin{array} { r l } & { l ( x ) = { \frac { 4 } { 5 } } x - { \frac { 1 } { 5 } } } \\ & { l ( x ) = { \frac { 5 } { 5 } } { \frac { 4 } { 5 } } x - { \frac { 1 } { 5 } } { \frac { 6 } { 5 } } } \\ & { l ( x ) = x - { \frac { 3 } { 1 6 } } { \sqrt [ { 3 } ] { 2 } } = x - . 2 3 6 \ldots . } \end{array} }
$$

![](../chunks/Interpolation and Approximation (Philip J. Davis) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0141-0210/auto/images/9a3a6d4a2ad69e5ff1e64171e2c57891cb492f313b396f8fdadf5814c3a12db4.jpg)  
Figure 7.1.1 Least Square and Best Uniform Linear Approximations to $x ^ { 4 }$ on [0, 1].

The major investigations in the theory of best approximation concern themselves with (a) Under what circumstances is there a best approximation?If it exists,is it unique?(b) How can best approximations be characterized analytically or geometrically?(c) How can the best approximants be computed numerically? (d) What are the asymptotic properties of best approximation? We shall prove theorems in all these categories.

It would be good to have an abstract mathematical structure to describe properties of best approximation independently of the specific criterion of closeness of approximation. Such a structure is furnished by the theory of Normed Linear Spaces,and it is to this theory that we now turn.

# 7.2 Normed Linear Spaces

DEFINITioN 7.2.1. A linear space $X$ is called a normed linear space if for each element $_ { x }$ of the space there is defined a real number designated by $\| x \|$ with the following properties:

(a) $\| x \| \ge 0 ( \mathrm { p o s i t i v i t y } )$ (b) $\| x \| = 0$ if and only if $\pmb { x } = 0$ (definiteness) （c） $\| { \boldsymbol { \alpha } } { \boldsymbol { x } } \| = | { \boldsymbol { \alpha } } | \ \| { \boldsymbol { x } } \|$ for every scalar $\pmb { \alpha }$ (homogeneity) （d） $\| x + y \| \leq \| x \| + \| y \|$ (triangle inequality)

The quantity $\| \pmb { x } \|$ is known as the norm of $_ { \pmb { x } }$

DEFINITion 7.2.2. A metric space is a collection of elements and a measure of distance $d ( x , y )$ defined for every ordered pair of elements.The function $d ( x , y )$ is assumed to satisfy

$$
\begin{array} { l } { d ( x , y ) \geq 0 } \\ { d ( x , y ) = 0 \mathrm { ~ i f ~ a n d ~ o n l y ~ i f ~ } x = y } \\ { d ( x , y ) = d ( y , x ) } \\ { d ( x , y ) + d ( y , z ) \geq d ( x , z ) . } \end{array}
$$

Note that the concept of a metric space is the more primitive one since a normed linear space is a metric space under the definition

$$
d ( x , y ) = \| x - y \| .
$$

It is easily verified that (7.2.1) and (7.2.3) imply (7.2.2).

As an easy consequence of the norm postulates we have

$$
\begin{array} { c } { \displaystyle { \big | \| { \boldsymbol { x } } \| - \| { \boldsymbol { y } } \| \big | \leq \| { \boldsymbol { x } } - { \boldsymbol { y } } \| , } } \\ { \| { \boldsymbol { x } } \| = \| { \boldsymbol { x } } - { \boldsymbol { y } } + { \boldsymbol { y } } \| \leq \| { \boldsymbol { x } } - { \boldsymbol { y } } \| + \| { \boldsymbol { y } } \| . } \end{array}
$$

Therefore $\| x \| - \| y \| \leq \| x - y \|$

Similarly $\| y \| - \| x \| \leq \| y - x \| = \| x - y \|$

and (7.2.4) follows.

The following examples of normed linear spaces find frequent application.

Ex.1．The real line $- \infty < x < \infty$ with $\| x \| = | x |$

Ex.2.The real $_ n$ -dimensional Cartesian space $\scriptstyle { R _ { n } }$ of elements

$$
x = ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } )
$$

with the definition $\| x \| = ( { x _ { 1 } } ^ { 2 } + { x _ { 2 } } ^ { 2 } + \cdot \cdot \cdot + { x _ { n } } ^ { 2 } ) ^ { \frac { 1 } { 2 } }$ . This is known as the“square norm."

Ex.3. $\scriptstyle { R _ { n } }$ or $C _ { n }$ with the definition $\| x \| = ( | x _ { 1 } | ^ { p } + \cdot \cdot \cdot + | x _ { n } | ^ { p } ) ^ { 1 / p }$ ， $\textit { \textbf { p } } { \geq } 1$ · This is known as the $^ { \ast \mathfrak { s } } p$ norm.”Properties (7.2.1)(a)-(c) are easy to verify. Property (d) is the Minkowski Inequality and takes a number of steps to reach.

LEMMA 7.2.1.If $x , y \ge 0 , a , b > 0$ and $a + b = 1$ then

$$
x ^ { a } y ^ { b } \leq a x + b y .
$$

Equality holdsif and only if ${ \pmb x } = { \pmb y }$

Proof: Let $t > 1$ ， $m < 1$ .Let $f ( t ) = t ^ { m }$ ·

From Theorem 1.6.2,

$$
f ( t ) = f ( 1 ) + ( t - 1 ) f ^ { \prime } ( \xi ) \qquad 1 < \xi < t .
$$

Hence $t ^ { m } = 1 + ( t - 1 ) m \xi ^ { m - 1 } .$

Since $\xi ^ { m - 1 } < 1$

$$
t ^ { m } < 1 + m ( t - 1 ) .
$$

Assume,for the moment that $x > y > 0$ Set $t = x / y > 1$ ， $m = a$ ，so that $1 - m = b$ Then,from (7.2.6),

or

Hence

$$
\begin{array} { r l } & { ( x / y ) ^ { a } < 1 + a ( x / y - 1 ) } \\ & { } \\ & { x ^ { a } y ^ { 1 - a } < y + a ( x - y ) = a x + ( 1 - a ) y . } \\ & { } \\ & { x ^ { a } y ^ { b } < a x + b y . } \end{array}
$$

If $0 < x < y$ ，we may interchange the roles of $^ { a }$ and $^ { b }$ and arrive at the same inequality. If $x = y , x ^ { a } y ^ { b } = x ^ { a + b } = x = a x + b x$

LEMMA 7.2.2 (Holder's Inequality).Let $x _ { k }$ and $y _ { k }$ be complex. If $\pmb { p } > 1$ ，and $1 / p + 1 / q = 1$ ，

$$
\bigg | \sum _ { k = 1 } ^ { n } x _ { k } y _ { k } \bigg | \leq \bigg ( \sum _ { k = 1 } ^ { n } | x _ { k } | ^ { p } \bigg ) ^ { 1 / p } \bigg ( \sum _ { k = 1 } ^ { n } | y _ { k } | ^ { q } \bigg ) ^ { 1 / q } .
$$

Note that $1 / p , 1 / q > 0$

Proof:From Lemma 7.2.1,with $x = - \frac { | x _ { k } | ^ { p } } { \displaystyle \sum _ { k = 1 } ^ { n } | x _ { k } | ^ { p } } , y = \frac { | y _ { k } | ^ { q } } { \displaystyle \sum _ { k = 1 } ^ { n } | y _ { k } | ^ { q } } ,$

$a = 1 / p , b = 1 - 1 / p = 1 / q$ we have

$$
\left( \frac { | x _ { k } | ^ { p } } { \displaystyle \sum _ { k = 1 } ^ { n } | x _ { k } | ^ { p } } \right) ^ { 1 / p } \left( \frac { | y _ { k } | ^ { q } } { \displaystyle \sum _ { k = 1 } ^ { n } | y _ { k } | ^ { q } } \right) ^ { 1 / q } \leq 1 / p \frac { | x _ { k } | ^ { p } } { \displaystyle \sum _ { k = 1 } ^ { n } | x _ { k } | ^ { p } } + 1 / q \frac { | y _ { k } | ^ { q } } { \displaystyle \sum _ { k = 1 } ^ { n } | y _ { k } | ^ { q } } .
$$

Summing (7.2.8) from $k = 1$ to $k = n$ ， and multiplying by $\left( \sum _ { k = 1 } ^ { n } | x _ { k } | ^ { p } \right) ^ { 1 / p }$ $\times \left( \sum _ { k = 1 } ^ { n } | y _ { k } | ^ { q } \right) ^ { 1 / q }$ we obtain

$$
\sum _ { k = 1 } ^ { n } | x _ { k } y _ { k } | \leq { \biggl ( } \sum _ { k = 1 } ^ { n } | x _ { k } | ^ { p } { \biggr ) } ^ { 1 / p } { \biggl ( } \sum _ { k = 1 } ^ { n } | y _ { k } | ^ { q } { \biggr ) } ^ { 1 / q } .
$$

Since $\left| \sum _ { k = 1 } ^ { n } x _ { k } y _ { k } \right| \leq \sum _ { k = 1 } ^ { n } | x _ { k } y _ { k } |$ in (7.2.7) we must have

$$
{ \frac { | x _ { k } | ^ { p } } { \displaystyle \sum _ { k = 1 } ^ { n } | x _ { k } | ^ { p } } } = { \frac { | y _ { k } | ^ { q } } { \displaystyle \sum _ { k = 1 } ^ { n } | y _ { k } | ^ { q } } } k = 1 , 2 , \ldots , n
$$

i.e.,

$$
| x _ { k } | ^ { p } = \operatorname { c o n s t a n t } | y _ { k } | ^ { q } , k = 1 , 2 , . . . , n .
$$

Moreover,

$$
\left| \sum _ { k = 1 } ^ { n } x _ { k } y _ { k } \right| < \sum _ { k = 1 } ^ { n } \left| x _ { k } y _ { k } \right|
$$

unless

$$
x _ { k } y _ { k } = | x _ { k } y _ { k } | e ^ { i \theta } , \quad \theta = { \mathrm { c o n s t a n t } } , \quad k = 1 , 2 , \ldots , n .
$$

Hence (7.2.10) and (7.2.11) together are necessary and suffcient for equality in (7.2.7).

THEOREM 7.2.3 (Minkowski's Inequality). If $\pmb { \mathcal { p } } \geq \pmb { 1 }$ ，

$$
\left\{ \sum _ { i = 1 } ^ { n } | x _ { i } + y _ { i } | ^ { p } \right\} ^ { 1 / p } \leq \left( \sum _ { i = 1 } ^ { n } | x _ { i } | ^ { p } \right) ^ { 1 / p } + \left( \sum _ { i = 1 } ^ { n } | y _ { i } | ^ { p } \right) ^ { 1 / p }
$$

or, in the notation of $\ E x$ .3., $\| x + y \| \leq \| x \| + \| y \|$

Proof: If $\pmb { p } = 1$ ， (7.2.12)reduces to the triangle inequality. If $\pmb { p } > 1$ ，

$$
\begin{array} { r l r } {  { \sum _ { i = 1 } ^ { n } | x _ { i } + y _ { i } | ^ { p } = \sum _ { i = 1 } ^ { n } | x _ { i } + y _ { i } | | x _ { i } + y _ { i } | ^ { p - 1 } } } \\ & { } & { \leq \displaystyle \sum _ { i = 1 } ^ { n } | x _ { i } | | x _ { i } + y _ { i } | ^ { p - 1 } + \sum _ { i = 1 } ^ { n } | y _ { i } | | x _ { i } + y _ { i } | ^ { p - 1 } } \end{array}
$$

By Lemma 7.2.2,

$$
\begin{array} { r } { \displaystyle \sum _ { i = 1 } ^ { n } | x _ { i } | | x _ { i } + y _ { i } | ^ { p - 1 } \leq \bigg ( \sum _ { i = 1 } ^ { n } | x _ { i } | ^ { p } \bigg ) ^ { 1 / p } \bigg ( \sum _ { i = 1 } ^ { n } | x _ { i } + y _ { i } | ^ { ( p - 1 ) q } \bigg ) ^ { 1 / q } } \\ { = \bigg ( \displaystyle \sum _ { i = 1 } ^ { n } | x _ { i } | ^ { p } \bigg ) ^ { 1 / p } \bigg ( \displaystyle \sum _ { i = 1 } ^ { n } | x _ { i } + y _ { i } | ^ { p } \bigg ) ^ { 1 / q } . } \end{array}
$$

$$
\sum _ { i = 1 } ^ { n } | y _ { i } | | x _ { i } + y _ { i } | ^ { p - 1 } \leq \biggl ( \sum _ { i = 1 } ^ { n } | y _ { i } | ^ { p } \biggr ) ^ { 1 / p } \biggl ( \sum _ { i = 1 } ^ { n } | x _ { i } + y _ { i } | ^ { p } \biggr ) ^ { 1 / q } .
$$

$\mathbf { b y } \bigg ( \sum _ { i = 1 } ^ { n } | x _ { i } + y _ { i } | ^ { p } \bigg ) ^ { 1 / }$ (7.2.12).

Suppose that $\pmb { p } > 1$ . If there is equality in (7.2.12), we must have

$$
\begin{array} { r } { \displaystyle \sum _ { i = 1 } ^ { n } | x _ { i } | | x _ { i } + y _ { i } | ^ { p - 1 } = \biggr ( \sum _ { i = 1 } ^ { n } | x _ { i } | ^ { p } \biggr ) ^ { 1 / p } \biggr ( \sum _ { i = 1 } ^ { n } | x _ { i } + y _ { i } | ^ { p } \biggr ) ^ { 1 / q } } \\ { \displaystyle \sum _ { i = 1 } ^ { n } | y _ { i } | | x _ { i } + y _ { i } | ^ { p - 1 } = \biggr ( \sum _ { i = 1 } ^ { n } | y _ { i } | ^ { p } \biggr ) ^ { 1 / p } \biggr ( \sum _ { i = 1 } ^ { n } | x _ { i } + y _ { i } | ^ { p } \biggr ) ^ { 1 / q } } \end{array}
$$

and

$$
\sum _ { i = 1 } ^ { n } | x _ { i } + y _ { i } | | x _ { i } + y _ { i } | ^ { p - 1 } = \sum _ { i = 1 } ^ { n } | x _ { i } | | x _ { i } + y _ { i } | ^ { p - 1 } + \sum _ { i = 1 } ^ { n } | y _ { i } | | x _ { i } + y _ { i } | ^ { p - 1 } .
$$

By the remark following Lemma 7.2.2,(7.2.13) implies that

$$
| x _ { i } | ^ { p } = c _ { 1 } | x _ { i } + y _ { i } | ^ { p } , | y _ { i } | ^ { p } = c _ { 2 } | x _ { i } + y _ { i } | ^ { p } , i = 1 , 2 , . . . , n .
$$

Assuming that neither the $x _ { i }$ nor the $y _ { i }$ are all zero,

$$
| x _ { i } | = { \mathrm { c o n s t a n t } } | y _ { i } | , i = 1 , 2 , . . . , n .
$$

Since $| \alpha + \beta | < | \alpha | + | \beta |$ unless $\propto$ and $\beta$ have the same direction,we conclude from (7.2.14) that

$$
x _ { i } = | x _ { i } | \ e ^ { i \phi } , y _ { i } = | y _ { i } | \ e ^ { i \phi } , i = 1 , 2 , . . . , n .
$$

Hence,

$$
x _ { i } = c y _ { i } \quad i = 1 , 2 , . \dots , n ,
$$

with $c > 0$

Ex.4.ThesamelinearspaceasinEx.2,withthedefinition $\left\| x \right\| = \operatorname* { m a x } _ { 1 \leq j \leq n } \left| x _ { j } \right|$ This is known as the uniform norm.It is also called the $p \ : = \ : \infty$ norm in virtue of the identi sometimes ex $\begin{array} { r l } & { \underset { p \to \infty } { \mathrm { \operatorname { t y } } } \underset {  \infty } { \operatorname* { l i m } } ( | x _ { 1 } | ^ { \bar { p } } + | x _ { 2 } | ^ { p } + \cdot \cdot \cdot + | x _ { n } | ^ { p } ) ^ { 1 / p } = \underset { 1 \leq j \leq n } { \operatorname* { m a x } } | x _ { j } | . } \\ & { \mathrm { c p r e s s e s ~ t h i s ~ a s ~ } \underset { p \to \infty } { \operatorname { l i m } } \| x \| _ { p } = \| x \| _ { \infty } . } \end{array}$ (Prove.) One

Ex.5.If $\{ x _ { i } \}$ and $\{ y _ { i } \}$ are two sequences of real or complex numbers such that

$$
\begin{array} { r l r } {  { | x _ { i } | ^ { p } < \infty , \displaystyle \sum _ { i = 1 } ^ { \infty } | y _ { i } | ^ { p } < \infty , p \geq 1 , \mathrm { t h e n } } } \\ & { } & { \quad \bigg \{ \displaystyle \sum _ { i = 1 } ^ { \infty } | x _ { i } + y _ { i } | ^ { p } \bigg \} ^ { 1 / p } \leq \bigg ( \displaystyle \sum _ { i = 1 } ^ { \infty } | x _ { i } | ^ { p } \bigg ) ^ { 1 / p } + \bigg ( \displaystyle \sum _ { i = 1 } ^ { \infty } | y _ { i } | ^ { p } \bigg ) ^ { 1 / p } . } \end{array}
$$

This implies that the set of all infinite sequences $\{ x _ { i } \}$ with $\sum _ { i = 1 } ^ { \infty } | x _ { i } | ^ { p } < \infty$ and addition and scalar multiplication defined analogously to $\mathbf { E x }$ . 1,1.3, form a linear space with $\| \{ x _ { i } \} \| = \left( \sum _ { i = 1 } ^ { \infty } | x _ { i } | ^ { p } \right) ^ { 1 / \tau }$ .This space is called the $\ell ^ { p }$ space.

Ex.6.Let $B [ a , b ]$ be the set of all bounded functions defined in $[ a , b ]$ Define

$$
\| f \| = \operatorname* { s u p } _ { a \leq x \leq b } | f ( x ) | .
$$

Then we have a normed linear space.To prove (7.2.1)(d),observe that

$$
| f ( x ) | \leq \operatorname* { s u p } | f ( x ) | , | g ( x ) | \leq \operatorname* { s u p } | g ( x ) | .
$$

Hence,

$$
| f ( x ) + g ( x ) | \leq | f ( x ) | + | g ( x ) | \leq \operatorname* { s u p } | f ( x ) | + \operatorname* { s u p } | g ( x ) | .
$$

Since this is true for all $_ { x }$ ,it follows that

$$
\operatorname* { s u p } | f ( x ) + g ( x ) | \leq \operatorname* { s u p } | f ( x ) | + \operatorname* { s u p } | g ( x ) | .
$$

Ex. 7. $C [ \boldsymbol { a } , \boldsymbol { b } ]$ with the definition $\| f \| = \operatorname* { m a x } _ { a \leq x \leq b } \ | f ( x ) |$ is a normed linear space.

Ex.8.Let $\scriptstyle { \mathcal { R } }$ be a region of the complex plane. The set of functions analytic in $\scriptstyle { R }$ and bounded there forms a linear space $B ( R )$ .It may be normed by defining $\| f \| = \operatorname* { s u p } _ { z \in R } | f ( z ) |$ ·

Ex. 9.Let $w ( x ) \in C [ a , b ]$ and ${ \pmb w } ( { \pmb x } ) > { \pmb 0 }$ .We may norm $\mathit { C } [ a , b ]$ by defining $\| f \| = \left( \int _ { a } ^ { b } w ( x ) f ^ { 2 } ( x ) d x \right) ^ { \ddag }$ (wighte gar narmg

Ex. 10. $L ^ { p } [ a , b ]$ (Cf.Def. 1.4.o) is a normed linear space for $\textit { \textbf { p } } { \geq } 1$ We define $\| f \| = \left( \int _ { a } ^ { b } | f ( x ) | ^ { p } d x \right) ^ { 1 / \tau }$ . The triangle inequality is the Minkowski inequality for integrals.

$$
\left( \int _ { a } ^ { b } | f ( x ) ~ + ~ g ( x ) | ^ { p } ~ d x \right) ^ { 1 / p } \leq \left( \int _ { a } ^ { b } | f ( x ) | ^ { p } ~ d x \right) ^ { 1 / p } + ~ \left( \int _ { a } ^ { b } | g ( x ) | ^ { p } ~ d x \right) ^ { 1 / p } .
$$

For $\mathcal { p } > 1$ this may be defined from the Holder inequality for integrals.This states that if $f \in L ^ { p } [ a , b ]$ and $g \in L ^ { q } [ a , b ] , 1 / p \ + \ 1 / q = 1 , p > 1$ ,then $f g \in L [ a , b ]$ and

$$
{ \biggl | } \int _ { a } ^ { b } f \left( x \right) g ( x ) d x { \biggr | } \leq { \biggl ( } \int _ { a } ^ { b } | f \left( x \right) | ^ { p } d x { \biggr ) } ^ { 1 / p } { \biggl ( } \int _ { a } ^ { b } | g ( x ) | ^ { q } d x { \biggr ) } ^ { 1 / q } .
$$

The proof runs paralel to that of Lemma 7.2.2. The particular case, ${ \pmb { p } } = { \pmb { 2 } }$ ，

$$
\left| \int _ { a } ^ { b } f \left( x \right) g ( x ) d x \right| \leq \left( \int _ { a } ^ { b } | f \left( x \right) | ^ { 2 } d x \right) ^ { \frac { 1 } { 2 } } \left( \int _ { a } ^ { b } | g ( x ) | ^ { 2 } d x \right) ^ { \frac { 1 } { 2 } }
$$

is the very important Schwarz inequality.

Ex. 11. Let $a \leq x _ { 1 } < x _ { 2 } < \cdot \cdot \cdot < x _ { n } \leq b$ The linear space $\scriptstyle { \mathcal { P } } _ { n - 1 }$ may be normed as follows

$$
\| p \| = \operatorname* { m a x } _ { 1 \leq j \leq n } | p ( x _ { j } ) | .
$$

# 7.3 Convex Sets.

DEFINITION 7.3.1． Let $\pmb { X }$ be a linear space.If $\pmb { x _ { 1 } }$ and ${ \pmb x } _ { \mathbf { 2 } }$ are two distinct elements of $\pmb { X }$ ,the set of all elements of the form

$$
x = t x _ { 1 } + ( 1 - t ) x _ { 2 } , ~ 0 \leq t \leq 1
$$

is called the line segment joining $\pmb { x _ { 1 } }$ and ${ \pmb x } _ { \mathbf { 2 } }$

DEFINITION 7.3.2． Let $\pmb { X }$ be a linear space.A subset $c$ of $\pmb { X }$ is called convex if $\boldsymbol { c }$ contains all the elements on the line segment joining any two of its elements.That is,if $\pmb { x _ { 1 } }$ ${ \pmb { \mathscr { r } } } _ { 1 } , { \pmb { \mathscr { x } } } _ { 2 } \in C$ then so does $t x _ { 1 } + ( 1 - t ) x _ { 2 } ,$ $0 \leq t \leq 1$ ·

Ex.1.In $\scriptstyle { R _ { 2 } } ,$ a line segment, the quadrant $\pmb { x } \ge \mathbf { 0 } , y \ge \mathbf { 0 }$ ,the interior of an ellipse are all convex sets.(Proofs?)

Ex.2. The set of all polynomials with nonnegative coefficients is convex.

Ex.3.Let $x$ be a normed linear space.The ball $\| x \| \leq r$ is convex. For

suppose $\| x \| \leq r , \| y \| \leq r$ and $0 \leq t \leq 1$ . Then

$$
\left\| t x + ( 1 - t ) y \right\| \leq | t | \left\| x \right\| + | 1 - t | \left\| y \right\| \leq t r + ( 1 - t ) r = r .
$$

Hence $t x + ( 1 - t ) y$ belongs to the set.

![](../chunks/Interpolation and Approximation (Philip J. Davis) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0141-0210/auto/images/8c222413fd4d3181bedec24f4f195e9905bbe39f6e9c3e7ea05d326d66394a80.jpg)  
Figure 7.3.1 A Convex Set.

![](../chunks/Interpolation and Approximation (Philip J. Davis) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0141-0210/auto/images/2752b0ec1f8eedb8a46a26870ea999a27e997dc1689e11503cf935024ecc8f01.jpg)  
Figure 7.3.2 The Convex Hull.

![](../chunks/Interpolation and Approximation (Philip J. Davis) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0141-0210/auto/images/9dc2aa1f4a747e85f4f0ddef7061142c2a9420257328ea56f65c30505676cbe3.jpg)  
Figure 7.3.3.

DEFINITION 7.3.3. The convex hull of a given set $\pmb { S }$ is the intersection of all convex sets containing $\pmb { S }$

Ex.4.The convex hull of the point set $\frac { 1 } { 2 } \leq x ^ { 2 } + y ^ { 2 } \leq 1 , y \geq 0$ is the semicircle $x ^ { 2 } + y ^ { 2 } \leq 1 , y \geq 0$

Ex.5．The convex hull of the points $P _ { 1 } , P _ { 2 } , \ldots , P _ { n }$ lying in a plane may be“found’by driving nails in at $P _ { i }$ and wrapping a string around the configuration.

An elegant example of a normed linear space is furnished by the Minkowski plane.Let there be given in the $x , y$ plane a bounded,convex set $\pmb { S }$ with boundary $c$ 、We will suppose it contains the origin in its interior and that it is symmetric with respect to the origin;i.e.,if $( x , y ) \in S$ then $( - x , - y ) \in S$ If $P = ( x , y )$ is a point other than the origin,the directed line extending from (0,0） to $( x , y )$ can be shown to intersect $c$ in precisely one point $( x ^ { \prime } , y ^ { \prime } )$

Define

$$
\| P \| = \| ( x , y ) \| = \frac { \sqrt { x ^ { 2 } + y ^ { 2 } } } { \sqrt { x ^ { ' 2 } + y ^ { ' 2 } } } , \quad \| ( 0 , 0 ) \| = 0 .
$$

It should be clear that the points of the plane interior to $c$ have $\mathbf { n o r m } < 1$ ， those exterior to $\boldsymbol { c }$ have norm $> 1$ ,while those on $c$ have $\mathbf { n o r m } = 1$

THEOREM 7.3.1. $R _ { 2 }$ normed by (7.3.2) is $^ { \pmb { a } }$ normed linear space.

Proof:The requirements for a norm are (7.2.1)(a)-(d). The first three are easy to check. The triangle inequality requires some ingenuity. We wish to show that $\lVert P _ { 1 } + P _ { 2 } \rVert \leq \lVert P _ { 1 } \rVert + \lVert P _ { 2 } \rVert$ If either $\| \pmb { P _ { 1 } } \| = 0$ or $\| \pmb { P _ { 2 } } \| = 0$ ,the inequality is trivial.Assume that neither is O and set

$$
\| P _ { 1 } \| + \| P _ { 2 } \| = t .
$$

We can then write $\| P _ { 1 } \| = \theta t , \| P _ { 2 } \| = ( 1 - \theta ) t$ for some $0 < \theta < 1$

By homogeneity,

$$
\left\| { \frac { P _ { 1 } } { \theta t } } \right\| = \left\| { \frac { P _ { 2 } } { ( 1 - \theta ) t } } \right\| = 1 .
$$

This elsus ht he o points $\frac { P _ { 1 } } { \theta t } , \frac { P _ { 2 } } { ( 1 - \theta ) t }$ are loated on $c$ By the convexity of the closure of $\mathfrak { s }$ ，the point $\theta \left( \frac { P _ { 1 } } { \theta t } \right) + \left( 1 - \theta \right) \frac { P _ { 2 } } { \left( 1 - \theta \right) t } =$ $\frac { 1 } { t } \left( P _ { 1 } + P _ { 2 } \right)$ is also in the closure of $\boldsymbol { s }$ and hence

$$
\left\| { \frac { 1 } { t } } \left( P _ { 1 } + P _ { 2 } \right) \right\| = { \frac { 1 } { t } } \left\| P _ { 1 } + P _ { 2 } \right\| \leq 1 .
$$

Therefore,

$$
\lVert P _ { 1 } + P _ { 2 } \rVert \leq \lVert P _ { 1 } \rVert + \lVert P _ { 2 } \rVert .
$$

The same defnition can be introduced in spaces of higher dimension. $c$ is called the gauge curve of the normed plane.

Ex.6.If $c$ is the unit circle,then $\| P \| = ( x ^ { 2 } + y ^ { 2 } ) ^ { \frac { 1 } { 2 } }$ ，and we have the Euclidean norm.

Ex. 7.If $\boldsymbol { \sigma }$ is the square with sides $x = \pm 1 , y = \pm 1$ ,then

$$
\left\| P \right\| = \operatorname* { m a x } { ( | x | , | y | ) } .
$$

Ex.8. $\boldsymbol { \mathfrak { c } }$ is the square with sides $x \pm y = \pm 1$ Then $\| P \| = | x | + | y |$

7.4 The Fundamental Problem of Linear Approximation. Let $\pmb { X }$ be a normed linear space. Select $\mathscr { n }$ linearly independent elements $x _ { 1 } , \ldots , x _ { n }$ Let $_ y$ be an additional element.We wish to approximate $_ y$ by an appropriate

linear combination of the $x _ { 1 } , \ldots , x _ { n }$ 、The closeness of two elements will be defined as the norm of their difference.We therefore would like to make $\| y - ( a _ { 1 } x _ { 1 } + a _ { 2 } x _ { 2 } + \cdot \cdot \cdot + a _ { n } x _ { n } ) \|$ as small as possible. The element

$$
y - ( a _ { 1 } x _ { 1 } + \cdots + a _ { n } x _ { n } )
$$

is called the error or discrepancy.

DEFINITIoN 7.4.1. A best approximation to $_ y$ by linear combinations of $x _ { 1 } , \ldots , x _ { n }$ is an element $a _ { 1 } x _ { 1 } + \cdots + a _ { n } x _ { n }$ for which

$$
\| y - ( a _ { 1 } x _ { 1 } + \cdot \cdot \cdot + a _ { n } x _ { n } ) \| \leq \| y - ( b _ { 1 } x _ { 1 } + \cdot \cdot \cdot + b _ { n } x _ { n } ) \|
$$

for every choice of constants $\boldsymbol { b } _ { 1 } , \ldots , \boldsymbol { b } _ { n }$

A best approximation solves the problem of minimizing the error norm.

Ex.1.Let $x$ be $C [ 0 , 1 ]$ normed by $\| f \| = \operatorname* { m a x } _ { 0 \leq x \leq 1 } | f ( x ) |$ . Take $\pmb { n } = \pmb { 1 } , \pmb { x _ { 1 } }$ as the function l,and $_ y$ the function $e ^ { { \boldsymbol { x } } }$ .A best approximation to $e ^ { \mathfrak { x } }$ by constants is the constant $^ { a }$ that minimizes $\operatorname* { m a x } _ { 0 \leq x \leq 1 } | e ^ { x } - a |$ . The (unique) solution is ${ \textbf { \em a } } =$ $\textstyle { \frac { 1 } { 2 } } ( e \mathrm { ~ + ~ } 1 )$ and the error norm is $\textstyle { \frac { 1 } { 2 } } ( e \mathrm { ~ - ~ } 1 )$

Ex.2 Let $x$ be $C [ 0 , 1 ]$ normed by $\| f \| = \left( \int _ { 0 } ^ { 1 } f ^ { 2 } d x \right) ^ { \frac { 1 } { 2 } }$ Take $\textbf { \em n } = \textbf { 1 }$ $x _ { 1 }$ the function 1, and $y$ the function $e ^ { { \mathfrak { x } } }$ 、A best approximation to $e ^ { \alpha }$ by constants is the ongtant $^ { a }$ which minimizea $\left( \int _ { 0 } ^ { 1 } ( e ^ { x } - a ) ^ { 2 } d x \right) ^ { \frac { 1 } { 2 } }$ . The (uniguy solai i given by $\boldsymbol { e } \mathrm { ~ - ~ } \boldsymbol { 1 }$ and the error norm is $( \frac { 1 } { 2 } ( 4 e \mathrm { ~ - ~ } e ^ { 2 } \mathrm { ~ - ~ } 3 ) ) ^ { \frac { 1 } { 2 } }$

Ex.3.Let $x$ be $R _ { 3 }$ normed by $\| x \| = \operatorname* { m a x } _ { 1 \leq i \leq 3 } | x _ { i } |$ . Take $\textbf { \textit { n } } = \textbf { 2 }$ ， $x _ { 1 } = ( 1 , 0 , 0 )$ $x _ { 2 } = ( 0 , 1 , 0 )$ and $y = ( 3 , 5 , 2 )$ .The minimum error norm is 2 and can be achieved with any coefficients $a _ { \mathbf { 1 } } , a _ { \mathbf { 2 } }$ ,forwhich $| 3 - a _ { 1 } | \leq 2$ ， $| 5 - a _ { \bf 2 } | \leq { \bf 2 } .$ ，Though there is a best approximation,it is not unique.

Ex.4.Let $\boldsymbol { X } = \boldsymbol { \mathcal { P } _ { 1 } }$ normed by $\left\| f \right\| = \left| f ( 0 ) \right| + \left| f ( 1 ) \right|$ .What constant is a best approximant to the polynomial $x ?$ We have $\| x - a \| = | a | + | 1 - a |$ Hence, as $^ { a }$ varies,the minimum value is 1 and is assumed for every $0 \leq a \leq 1$

The problem of finding best approximations can be pictured geometrically.The set of all linear combinations $a _ { 1 } x _ { 1 } + \cdots + a _ { n } x _ { n }$ form a linear subspace of dimension $\pmb { n }$ .We can picture this as a plane.The element $_ y$ will not,in general, lie in this plane,and we would like to locate the point of the plane closest to $_ y$

THEOREM 7.4.1. Given y and n linearly independent elements $x _ { 1 } , \ldots , x _ { n }$ The problem of finding min $\| y - ( a _ { 1 } x _ { 1 } + \cdot \cdot \cdot + a _ { n } x _ { n } ) \|$ has $^ { \pmb { a } }$ solution. ai

Proof:Consider the error norm

$$
d ( a _ { 1 } , a _ { 2 } , . . . , a _ { n } ) = \| y - ( a _ { 1 } x _ { 1 } + a _ { 2 } x _ { 2 } + \dotsb + a _ { n } x _ { n } ) \|
$$

as a function of the $\pmb { n }$ real or complex variables $a _ { 1 } , \ldots , a _ { n }$ .This function is continuous in the variables ${ \pmb a } _ { i }$ ,for,the difference

$$
\begin{array} { r l } & { | d ( a _ { 1 } ^ { \prime } , a _ { 2 } ^ { \prime } , \ldots , a _ { n } ^ { \prime } ) - d ( a _ { 1 } , a _ { 2 } , \ldots , a _ { n } ) | } \\ & { \phantom { | d ( a _ { 1 } ^ { \prime } , a _ { 2 } ^ { \prime } , \ldots , a _ { n } ^ { \prime } ) - d ( a _ { 1 } , a _ { 2 } , \ldots , a _ { n } ) | } = | \| y - ( a _ { 1 } x _ { 1 } + \cdot \cdot \cdot + a _ { n } x _ { n } ) \| \cdot } \\ & { \phantom { | d ( a _ { 1 } ^ { \prime } , a _ { 2 } ^ { \prime } , \ldots , a _ { n } ) } \leq \| ( a _ { 1 } ^ { \prime } - a _ { 1 } ) x _ { 1 } + \cdot \cdot \cdot + ( a _ { n } ^ { \prime } - a _ { n } ) x _ { n } \| } \\ & { \phantom { | d ( a _ { 1 } ^ { \prime } , a _ { 2 } ^ { \prime } , \ldots , a _ { n } ) } \leq | a _ { 1 } ^ { \prime } - a _ { 1 } | \| x _ { 1 } \| + \cdot \cdot \cdot + | a _ { n } ^ { \prime } - a _ { n } | \| x _ { n } \| . } \end{array}
$$

![](../chunks/Interpolation and Approximation (Philip J. Davis) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0141-0210/auto/images/2483af4043f9bbf024da3f55e851c82f4fe63a4b2e39d01a3266cdfa4bebac97.jpg)  
Figure 7.4.1.

The first inequality follows from (7.2.4) and the second from (7.2.1)(d), (c). Since the $_ { \pmb { x } }$ s are fixed,(7.4.2) implies that the difference of the $^ d$ s must be small if the difference of the $^ { \pmb { a } }$ 's is small. In a similar way,the function

$$
h ( a _ { 1 } , . . . , a _ { n } ) = \| a _ { 1 } x _ { 1 } + \cdot \cdot \cdot + a _ { n } x _ { n } \|
$$

is a continuous function of the $^ { \pmb { a } }$ s.

Let $\pmb { S }$ designate the spherical surface

$$
S \colon | a _ { 1 } | ^ { 2 } + | a _ { 2 } | ^ { 2 } + \cdots + | a _ { n } | ^ { 2 } = 1
$$

in $\scriptstyle { R _ { n } }$ (or $C _ { n }$ ). $\pmb { S }$ is closed and bounded and hence $\pmb { h }$ must take on a minimum value $m > 0$ there.The possibility ${ \pmb m } = 0$ is ruled out for we should have for some nonidentically vanishing $\pmb { a } _ { i }$ ， $\| a _ { 1 } x _ { 1 } + \dotsb + a _ { n } x _ { n } \| = 0$ This implies that $a _ { 1 } x _ { 1 } + \dotsb + a _ { n } x _ { n } = 0$ and contradicts the assumption that the $_ { \pmb { x } }$ 's are linearly independent.Now,writing $\boldsymbol { r }$ for $( | a _ { 1 } | ^ { 2 } + | a _ { 2 } | ^ { 2 } + \cdot \cdot \cdot + | a _ { n } | ^ { 2 } ) ^ { \frac { 1 } { 2 } }$ ，

$$
h ( a _ { 1 } , \ldots , a _ { n } ) = r \left\| { \frac { a _ { 1 } } { r } } x _ { 1 } + \cdot \cdot \cdot + { \frac { a _ { n } } { r } } x _ { n } \right\|
$$

so that

$$
\begin{array} { r } { h ( a _ { 1 } , \ldots , a _ { n } ) \ge m r . } \end{array}
$$

Moreover,

$$
\begin{array} { r l } & { d = \| y - ( a _ { 1 } x _ { 1 } + \cdot \cdot \cdot + a _ { n } x _ { n } ) \| \ge \| a _ { 1 } x _ { 1 } + \cdot \cdot \cdot + a _ { n } x _ { n } \| - \| y \| } \\ & { \quad \ge m r - \| y \| . } \end{array}
$$

This inequality means that if we select coefficients that are very large, $\scriptstyle d$ must be very large for it increases without limit as $r \to \infty$ .This in turn means that in looking fora minimum value for $\pmb { d }$ ,we can confine our attentions to a certain sphere in the $^ { \pmb { a } }$ -space.More precisely,set

$$
\rho = \operatorname* { i n f } d ( a _ { 1 } , \ldots , a _ { n } ) \quad { \mathrm { a n d } } \quad R = { \frac { 1 + \rho + \| y \| } { m } } .
$$

If $| a _ { 1 } | ^ { 2 } + \cdots + | a _ { n } | ^ { 2 } > R ^ { 2 }$ (7.4.7) implies

$$
d > m R - \| y \| = 1 + \rho > \rho .
$$

Hence

$$
\operatorname* { i n f } _ { \mathrm { ~ I ~ } } d ( a _ { 1 } , \cdot \cdot \cdot , a _ { n } ) = \operatorname* { i n f } _ { \mathrm { ~ I ~ I ~ } } d ( a _ { 1 } , \cdot \cdot \cdot , a _ { n } )
$$

where I refers to the whole space of the $^ { a }$ 's and $\mathbf { I I }$ to the portion $| a _ { \mathbf { 1 } } | ^ { 2 } +$ $\cdots + \vert a _ { n } \vert ^ { 2 } \leq R ^ { 2 }$ Since $\pmb { d }$ is continuous,the value of the right hand of (7.4.10) is assumed in $| a _ { 1 } | ^ { 2 } + \cdots + | a _ { n } | ^ { 2 } \leq R ^ { 2 }$ ,and this completes the proof.

COROLLARY 7.4.2． Let $f ( x ) \in C [ a , b ]$ and $\pmb { n }$ be a fixed integer.The problem of finding $\operatorname* { m i n } _ { a _ { 0 } , \dots , a _ { n } } \operatorname* { m a x } _ { a \leq x \leq b } | f ( x ) - ( a _ { 0 } + a _ { 1 } x + \cdot \cdot \cdot + a _ { n } x ^ { n } ) |$ has $^ { a }$ solution. As we shall prove subsequently,the solution is unique.It is calld the Tschebyscheff approximation of degree $\leq n$ to $f ( x )$ .We shall designate it by $\pmb { T } _ { n } ( f ; \pmb { x } )$

COROLLARY 7.4.3. Let $f ( x ) \in C [ a , b ]$ and $\pmb { n }$ be a fixed integer. Let $\pmb { \mathscr { p } } \geq 1$ The problem of finding $\operatorname* { m i n } _ { a _ { 0 } , a _ { 1 } , \ldots , a _ { n } } \int _ { a } ^ { b } \lvert f ( x ) - ( a _ { 0 } + a _ { 1 } x + \cdot \cdot \cdot + a _ { n } x ^ { n } ) \rvert ^ { p } d x h a s d$ $^ { \pmb { a } }$ solution. Such a solution yields $^ { \pmb { a } }$ best approximation to $\pmb { f } ( \pmb { x } )$ in the sense of least pth powers. We need only assume that $f \in L ^ { p } [ a , b ]$

COROLLARY 7.4.4． Let $\pmb { B }$ be a bounded region in the complex $\textit { \textbf { z } }$ plane. Let $f ( z )$ be analytic in $\pmb { B }$ and remain continuous in $\pmb { \bar { B } }$ ,the closure of $\pmb { B }$ The problem of finding $\operatorname* { m i n } _ { a _ { 0 } , \ldots , a _ { n } } \ \operatorname* { m a x } _ { z \in \mathcal { B } } | f ( z ) - ( a _ { 0 } + a _ { 1 } z + \cdot \cdot \cdot + a _ { n } z ^ { n } ) |$ has $^ { \pmb { a } }$ solution. This polynomial will be proven unique in Theorem 7.5.6 and willbe designated by $T _ { n } ( f ( z ) ; z )$

COROLLARY 7.4.5. Let $x _ { 0 } , \ldots , x _ { k }$ be $k + 1$ distinct points. Let $k \geq n$ .The problem of determining $\operatorname* { m i n } _ { a _ { 0 } , \dots , a _ { n } } \operatorname* { m a x } _ { 0 \leq i \leq k } | f ( x _ { i } ) - ( a _ { 0 } + a _ { 1 } x _ { i } + \dots \cdot + a _ { n } x _ { i } ^ { \mathit { n } } ) |$ has a solution.

COROLLARY 7.4.6． Let $x _ { 0 } , \ldots , x _ { k }$ be $k + 1$ distinct points, $k \geq n$ The problem of determining $\operatorname* { m i n } _ { a _ { 0 } , \ldots , a _ { n } } \sum _ { i = 0 } ^ { k } ( f ( x _ { i } ) - ( a _ { 0 } + a _ { 1 } x _ { i } + \cdots + a _ { n } x _ { i } ^ { \phantom { - } n } ) ) ^ { 2 }$ possesses a solution.This is the common problem of least squares data fitting by polynomials.

COROLLARY 7.4.7. Let values $a _ { i j } , y _ { i }$ be given for $1 \leq i \leq p$ ， $1 \leq j \leq n$ ， $\mathbf { \nabla } _ { \pmb { p } } > \mathbf { \nabla } _ { \pmb { n } }$ . The problem of finding min maxp $| y _ { i } - ( a _ { i 1 } x _ { 1 } + a _ { i 2 } x _ { 2 } + \cdot \cdot \cdot + a _ { i n } x _ { n } ) |$ has a solution.

This is the“solution’of an over-determined system of linear equations, accepting as the answer those values that render minimum the maximum of the individual discrepancies. Other norms may be used. The most frequently used norm is the square norm.

COROLLARY 7.4.8. Let $C _ { p } [ - \pi , \pi ]$ designate the linear space of functions which are continuous on $[ - \pi , \pi ]$ and are periodic: $f ( \pi ) = f ( - \pi )$ Then, there is a trigonometric polynomial of order $\leq n$ ，

$$
T _ { n } ( x ) = \sum _ { k = 0 } ^ { n } a _ { k } \cos k x + \sum _ { k = 1 } ^ { n } b _ { k } \sin k x
$$

for which $\operatorname* { m a x } _ { - \pi \leq x \leq \pi } | f ( x ) - T _ { n } ( x ) |$ is minimum.

DEFINITION 7.4.2. For a given $y ; x _ { 1 } , \ldots , x _ { n }$ set

$$
\operatorname* { m i n } _ { a _ { i } } \| y - ( a _ { 1 } x _ { 1 } + \cdot \cdot \cdot + a _ { n } x _ { n } ) \| = E _ { n } ( y ; x _ { 1 } , \dots , x _ { n } ) = E _ { n } ( y ) .
$$

$E _ { n } ( y )$ is the measure of best approximation that can be achieved when $_ y$ is approximated by linear combinations of the $_ { x }$ s.Geometrically,it may be thought of as the distance from $_ y$ to the subspace spanned by $x _ { 1 } , \ldots , x _ { n }$

Evidently we have

$$
E _ { 1 } ( y ) \geq E _ { 2 } ( y ) \geq E _ { 3 } ( y ) \geq \cdot \cdot \cdot
$$

This is true since linear combinations of $x _ { 1 } , x _ { 2 } , \ldots , x _ { k }$ are also linear combinations of x1,x2,...,xx, Xk+1·

7.5Uniqueness of Best Approximation. We have observed that under the hypothesis of Theorem 7.4.l there is always one best approximant. But there may be more than one.In fact,the best approximants form a convex set.

THEOREM 7.5.l. Let S designate the set of best approximants to y in the situation of Theorem 7.4.1. Then S is convex.

Proof: Let $_ x$ and $\boldsymbol { w }$ be two best approximants to $\pmb { y }$ .Then, $\| y - x \| =$ $E _ { n } ( y ) , \| y - w \| = E _ { n } ( y )$ .Suppose that $\alpha \geq 0$ ， $\beta \geq 0$ and $\alpha + \beta = 1$ . Then

$$
\begin{array} { r l } & { \| y - \alpha x - \beta w \| = \| { \alpha } ( y - x ) + \beta ( y - w ) \| \leq \alpha \| y - x \| + \beta \| y - w \| } \\ & { \qquad = ( \alpha + \beta ) E _ { n } ( y ) = E _ { n } ( y ) . } \end{array}
$$

But $\alpha x + \beta w$ is also a linear combination of ${ \pmb x } _ { 1 } , { \pmb x } _ { 2 } , \ldots , { \pmb x } _ { n }$ and hence $\alpha x + \beta w$ must also be a best approximant.

CoROLLARy 7.5.2. The set of best approximants consists either of one element orof infinitely many elements.

Proof:For if it contains two distinct clements,it must contain the whole line of elements joining the two.

Ex.1. In Ex.3,7.4,the totality of best approximations is given by $| 3 - a _ { 1 } | \leq 2$ ， $| 5 \textrm { -- } a _ { 2 } | \leq 2$ The points $( a _ { \bf 1 } , a _ { \bf 2 } )$ lie in a square,a convex figure.

A fairly extensive sufficient condition can be given which assures the uniqueness of the best approximation.

DEFINITIoN 7.5.l． A normed linear space $\pmb { X }$ is called strictly convex if $\| x \| \leq r$ ， $\| y \| \leq r$ imply $\| x + y \| < 2 r$ unless $x = y$

Ex.2.The space $C _ { n }$ of complex sequences $x = ( x _ { 1 } , \ldots , x _ { n } )$ with

$$
\| x \| = { \biggl ( } \sum _ { i = 1 } ^ { n } | x _ { i } | ^ { p } { \biggr ) } ^ { 1 / p } , p > 1 ,
$$

is strictly convex.For if

$$
\| x \| \leq r , \| y \| \leq r \qquad \mathrm { a n d } \qquad \| x + y \| = 2 r ,
$$

then

$$
2 r = \| x + y \| \leq \| x \| + \| y \| \leq 2 r .
$$

Therefore,

$$
\| x + y \| = \| x \| + \| y \| .
$$

Hence

$$
\| x \| = \| y \| = r .
$$

$$
x _ { i } / y _ { i } = \lambda > 0 \quad i = 1 , 2 , . . . , n .
$$

Since $\| x \| = \| y \|$ ， $\lambda = 1$ ,and so $x \ : = y$

Ex.3． The normed linear spaces $\ell ^ { p }$ and $L ^ { p } [ a , b ] , \ 1 < p < \infty$ ，are strictly convex.

Ex.4.The space ${ \cal C } [ - 1 , 1 ]$ with $\| f \| = \operatorname* { m a x } _ { - 1 \leq x \leq 1 } | f ( x ) |$ is not strictly convex.

For if $f ( x ) = 1 - x ^ { 2 } , g ( x ) = 1 - x ^ { 4 } , \| f \| = \| g \| = 1 , \| f + g \| = 2$ but

$$
f ( x ) \not \equiv g ( x ) .
$$

Ex.5. $R _ { 2 }$ with $\| ( x _ { 1 } , x _ { 2 } ) \| = \operatorname* { m a x } { ( | x _ { 1 } | , | x _ { 2 } | ) }$ is not strictly convex for

$$
\lVert ( 1 , 0 ) + ( 1 , 1 ) \rVert \ = \lVert ( 1 , 0 ) \rVert \ + \ \lVert ( 1 , 1 ) \rVert .
$$

THEOREm 7.5.3. In a normed linear space $X$ with $^ { a }$ strictly convex norm, the problem of best approximation (posed in Theorem 7.4.l) has $^ { a }$ unique solution.

Proof: Suppose there are two distinct best approximants to $y , u _ { 1 }$ and $\mathbf { \mathscr { u } _ { 2 } }$ Then $\| y - u _ { 1 } \| = \| y - u _ { 2 } \| = E _ { n } ( y )$ Now $y - u _ { 1 }$ and $y - u _ { 2 }$ are also distinct.Hence by strict convexity,

$$
\| ( y - u _ { 1 } ) + ( y - u _ { 2 } ) \| < 2 E _ { n } ( y ) .
$$

This is equivalent to $\lVert y - \frac { 1 } { 2 } ( u _ { 1 } + u _ { 2 } ) \rVert < E _ { n } ( y )$ .But this would mean that the element $\frac { 1 } { 2 } ( u _ { 1 } + u _ { 2 } )$ ， which is also a linear combination of $x _ { 1 } , \ldots , x _ { n }$ ， is closer to $_ y$ than the minimum possible distance.This is a contradiction.

COROLLARY 7.5.4. Best approximation in the spaces $L ^ { p } [ a , b ] , \ell ^ { p } , 1 < p < \infty$ is unique.

The important case of best uniform approximation is,unfortunately,not covered by the general result of Theorcm 7.5.3 and must be trcated by its own methods.

We begin by establishing a geometric lemma whose utility will become clear during the course of the proof of Theorem 7.5.6.

![](../chunks/Interpolation and Approximation (Philip J. Davis) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0141-0210/auto/images/47725b094955b1407a0820951040d353f46c8ca237bb322b9ec8aee7a9d52a18.jpg)  
Figure 7.5.1.

LEMMA 7.5.5. Let $M$ and $\varepsilon < M / 2$ be fixed.Designate by I the set of points $| z - \eta M | \leq \eta \varepsilon$ and by II the set of points common to $| z | \leq M$ and $| z - M | \leq \varepsilon . \mathit { S e t } \rho ( \eta ) = \left. \operatorname* { m a x } _ { z _ { 1 } \in 1 , \atop z _ { 9 } \in \mathrm { I I } } \right| z _ { 1 } - z _ { 2 } |$ .Then,for any $0 < \eta < \frac { 1 } { 3 } , \rho ( \eta ) < M$ The same conclusion obviously holds if the whole figure is rotated about 0.

Pro0f: Sinceε<M/2,η<}< $\eta < \frac { 1 } { 3 } < \frac { M - \varepsilon } { M + \varepsilon }$ .The sets I and II have no common point and appear as drawn in the figure.If $\theta = \yen 10M$ ，then sin $\theta = \displaystyle \frac { \eta \varepsilon } { \eta M } < \frac { 1 } { 2 }$ Hence $0 < \theta < \pi / 6$

A moment's consideration leads one to the conclusion that $\begin{array} { r } { \pmb \rho = \overline { { P P ^ { \prime } } } } \end{array}$ Hence,

$$
\rho ( \eta ) = ( M ^ { 2 } + \eta ^ { 2 } M ^ { 2 } - 2 M ^ { 2 } \eta \cos \theta ^ { \prime } ) ^ { \frac { 1 } { 2 } } + \eta \varepsilon
$$

where $\pmb { \theta } ^ { \prime } = \pmb { \chi } \pmb { P } \pmb { O } \pmb { M }$ Since $\theta ^ { \prime } < \theta < \pi / 6 , - \cos \theta ^ { \prime } < - \frac { \sqrt { 3 } } { 2 }$ Hence,

$$
\rho ( \eta ) < M ( ( 1 + \eta ^ { 2 } - \sqrt { 3 } \eta ) ^ { \frac { 1 } { 2 } } + \eta / 2 ) .
$$

Let $f ( \eta ) = ( 1 + \eta ^ { 2 } - \sqrt { 3 } \eta ) ^ { \frac { 1 } { 2 } } + \eta / 2$ Then $f ( \eta ) = 1$ if and only if $\eta = 0$ or $\eta = \textstyle \frac { 4 } { 3 } ( \sqrt { 3 } - 1 ) = . 9 7 6$ Furthermore, $f ( { \textstyle { \frac { 1 } { 2 } } } ) = ( { \textstyle { \frac { 5 } { 4 } } } - { \textstyle { \frac { 1 } { 2 } } } { \textstyle \sqrt { 3 } } ) ^ { \frac { 1 } { 2 } } + { \textstyle { \frac { 1 } { 4 } } } = . 8 7 < 1$ Therefore when $0 < \eta < . 9 7 6$ $f ( \eta ) < 1$ .Consequently $\rho ( \eta ) < M$ for $0 < \eta < { \frac { 1 } { 3 } }$

THEOREM 7.5.6 (Tonelli)．Let $s$ be a closed and bounded set in the complex plane that contains more than $n + 1$ points.Let $f ( z )$ be continuous on $\pmb { S }$ and set

$$
M = \operatorname* { m i n } _ { p \in { \mathcal { P } } _ { n } } \operatorname* { m a x } _ { z \in S } | f ( z ) - p ( z ) | .
$$

Let $\scriptstyle { \pmb { \mathscr { p } } } _ { \pmb { \mathscr { n } } } ( z )$ be any polynomial that realizes this extreme value and set

$$
r ( z ) = f ( z ) - p _ { n } ( z ) .
$$

A. The number of distinct points of $\pmb { S }$ at which $| r ( z ) |$ takes on its maximum value is greater than $n + 1$

B. There is a unique solution to the problem (7.5.1).

Proof:There is first the trivial case in which $M = 0$ .Then

so that

$$
\begin{array} { r } { \underset { z \in S } { \operatorname* { m a x } } \left| f ( z ) - p _ { n } ( z ) \right| = 0 } \\ { p _ { n } ( z ) = f ( z ) \qquad } \end{array}
$$

throughout $\boldsymbol { s }$ .This implies A. Since a minimizing polynomial must agree with $f$ in more than $n + 1$ points,it is uniquelydetermined forit is in $\mathcal { P } _ { n }$

Assume next that $M > 0$ .We first show that A implies B. Suppose that ${ \pmb p } _ { n } , { \pmb q } _ { n } \in \mathcal { P } _ { n }$ are two distinct polynomials for which

$$
\operatorname* { m a x } _ { z \in S } | f ( z ) - p _ { n } ( z ) | = \operatorname* { m a x } _ { z \in S } | f ( z ) - q _ { n } ( z ) | = M .
$$

Now,

$$
\operatorname* { m a x } _ { z \in S } | f ( z ) - \frac { 1 } { 2 } ( p _ { n } ( z ) + q _ { n } ( z ) ) |
$$

$$
\begin{array} { r } { \leq \underset { z \in S } { \operatorname* { m a x } } \frac { 1 } { 2 } \left| f ( z ) - p _ { n } ( z ) \right| + \underset { z \in S } { \operatorname* { m a x } } \frac { 1 } { 2 } \left| f ( z ) - q _ { n } ( z ) \right| = M / 2 + M / 2 = M . } \end{array}
$$

Since $\smash { \frac { 1 } { 2 } ( p _ { n } + q _ { n } ) \in \mathcal { P } _ { n } }$ ,the definition of $M$ implies that

$$
\operatorname* { m a x } _ { z \in S } | f ( z ) - \frac { 1 } { 2 } ( p _ { n } ( z ) + q _ { n } ( z ) ) | = M .
$$

This means that $\smash { \frac { 3 } { 2 } ( p _ { n } + q _ { n } ) }$ is a minimizing polynomial.

Let $z ^ { \prime }$ be a point of $\pmb { S }$ for which the maximum in (7.5.3) is achieved. Then

$$
\begin{array} { r } { M = | f ( z ^ { \prime } ) - \frac 1 2 ( p _ { n } ( z ^ { \prime } ) + q _ { n } ( z ^ { \prime } ) ) | \le \frac 1 2 | f ( z ^ { \prime } ) - p _ { n } ( z ^ { \prime } ) | + \frac 1 2 | f ( z ^ { \prime } ) - q _ { n } ( z ^ { \prime } ) | } \\ { \le M / 2 + M / 2 = M . \qquad } \end{array}
$$

This implies that

$$
\begin{array} { r } { \begin{array} { r } { | f ( z ^ { \prime } ) - \frac { 1 } { 2 } ( p _ { n } ( z ^ { \prime } ) + q _ { n } ( z ^ { \prime } ) ) | = \frac { 1 } { 2 } | f ( z ^ { \prime } ) - p _ { n } ( z ^ { \prime } ) | + \frac { 1 } { 2 } | f ( z ^ { \prime } ) - q _ { n } ( z ^ { \prime } ) | } \\ { | f ( z ^ { \prime } ) - p _ { n } ( z ^ { \prime } ) | = M \quad \mathrm { a n d } \quad | f ( z ^ { \prime } ) - q _ { n } ( z ^ { \prime } ) | = M . } \end{array} } \end{array}
$$

and

Since, moreover, $| a + b | = | a | + | b |$ implies that arg $a = \arg b$ (or $a b = 0$ ）， it follows that

$$
f ( z ^ { \prime } ) - p _ { n } ( z ^ { \prime } ) = f ( z ^ { \prime } ) - q _ { n } ( z ^ { \prime } ) \quad \mathrm { o r } \quad p _ { n } ( z ^ { \prime } ) - q _ { n } ( z ^ { \prime } ) = 0 .
$$

According to A,there are at least $\mathbf { \omega } _ { n { \mathrm { ~ + ~ } } 2 }$ distinct points of type $z ^ { \prime }$ Since $p _ { n } - q _ { n } \in \mathcal { P } _ { n }$ , it follows that ${ \pmb { p } } _ { \pmb { n } } \equiv { \pmb q } _ { n }$

To prove A, suppose the contrary, that $| r ( z ) | = M$ only at $z _ { 1 } , z _ { 2 } , \ldots , z _ { m }$ and $m \leq \dot { \star } + 1$ Let $\pmb q ( \pmb z )$ be an element of $\mathcal { P } _ { n }$ for which

$$
q ( \boldsymbol { z } _ { i } ) = r ( \boldsymbol { z } _ { i } ) \qquad i = 1 , 2 , \ldots , m .
$$

We will show that for suffciently small $\eta$

$$
\operatorname* { m a x } _ { z \in S } | r ( z ) - \eta q ( z ) | < M .
$$

Thus,

$$
\operatorname* { m a x } _ { z \in S } | f ( z ) - p _ { n } ( z ) - \eta q ( z ) | < M .
$$

Since $\boldsymbol { p } _ { n } + \eta \boldsymbol { q } \in \mathcal { P } _ { n }$ ,this would contradict the definition of $M$ in (7.5.1). To prove (7.5.4),

(a） Select $\varepsilon < M / 2$ (b)In view of the uniform continuity of $r$ and $\pmb q$ over $\pmb { S }$ ，determine $\pmb { \delta }$ so that

for

$$
\begin{array} { c } { { | r ( z _ { 1 } ) - r ( z _ { 2 } ) | \leq \varepsilon , | q ( z _ { 1 } ) - q ( z _ { 2 } ) | \leq \varepsilon } } \\ { { | z _ { 1 } - z _ { 2 } | \leq \delta , z _ { 1 } , z _ { 2 } \in \mathcal S . } } \end{array}
$$

(c)Let $C _ { \delta }$ designate the set of points of $\pmb { S }$ lying in at least one of the cireles

$$
| z - z _ { k } | < \delta \qquad k = 1 , 2 , \ldots , m .
$$

Let $\begin{array} { r } { T _ { \delta } = { \cal S } - C _ { \delta } } \end{array}$ .Then $S = C _ { \delta } \cup T _ { \delta }$

(d) Let $M _ { \delta } = \operatorname* { m a x } _ { z \in T _ { \delta } } | r ( z ) |$ .(If $\pmb { T } _ { \delta }$ is empty，set $M _ { \delta } = 0$ Similarly below.) In view of the fact that $| r ( z ) | = M$ only at $z _ { 1 } , \ldots , z _ { m }$ ,we have $M _ { \delta } < M$

(e) Set $\operatorname* { m a x } _ { z \in S } | q ( z ) | = Q$ and select an $\eta$ ：

$$
0 < \eta < \operatorname * { m i n } \biggl ( { } _ { 3 } ^ { 1 } , \frac { M - M _ { \delta } } { 2 Q } \biggr ) .
$$

Then,

$$
\operatorname* { m a x } _ { z \in T _ { \delta } } | r ( z ) - \eta q ( z ) | \le \operatorname* { m a x } _ { z \in T _ { \delta } } | r ( z ) | + \eta \operatorname* { m a x } _ { z \in T _ { \delta } } | q ( z ) |
$$

$$
< M _ { \delta } + \frac { M - M _ { \delta } } { 2 Q } Q = \frac { M + M _ { \delta } } { 2 } < M .
$$

Now for $C _ { \delta }$ Let $C _ { \kappa }$ designate the set of points common to $\pmb { S }$ and to

$$
| z - z _ { k } | < \delta .
$$

Then, $C _ { \delta } = \bigcup _ { k = 1 } ^ { m } C _ { k } .$ If $z \in C _ { k }$ ,then $| r ( z ) | \leq M = | r ( z _ { k } ) |$ ,and by (b)

$$
| r ( z ) - r ( z _ { k } ) | \leq \varepsilon < M / 2 .
$$

Thus,the values of $r ( z )$ lie in a region $\mathbf { I I } _ { k }$ as explained in the lemma.If $z \in C _ { k } ,$ then by (b), $| q ( z ) - q ( \varepsilon _ { k } ) | \leq \varepsilon$ ；but since $q ( z _ { k } ) = r ( z _ { k } )$ ，we have $| \eta q ( z ) - \eta r ( z _ { k } ) | \leq \eta \varepsilon$ Thus,for $z \in C _ { k }$ ，the values of $\eta \pmb { q } ( \pmb { z } )$ lie in a region ${ \bf { I } } _ { k }$ · Under the assumption on $\eta$ ，

$$
| r ( z ) - \eta q ( z ) | \leq \rho ( \eta ) = \underset { z _ { 1 } \in \mathrm { I I } _ { k } } { \operatorname* { m a x } } | z _ { 1 } - z _ { 2 } | < M .
$$

This conclusion is independent of $\pmb { k }$ and hence

$$
\operatorname* { m a x } _ { z \in C _ { \delta } } | r ( z ) - \eta q ( z ) | < M .
$$

Combining (7.5.8) with (7.5.7) we obtain (7.5.4). This completes the proof of the Theorem.For further elaboration of a similar argument carried out in the real domain,see the proof of Theorem 7.6.2.

We remark that if $\boldsymbol { s }$ contains $n + 1$ points,then $M = 0$ and B holds but not A. If $s$ contains fewer than $n + 1$ points, $M = 0$ and the solution is not unique.

Ex.6.Let $s$ be a closed bounded point set in the complex plane containing more than $\textit { \textbf { n } } - 1$ points. The problem of finding

$$
\operatorname* { m i n } _ { a _ { i } } \ \operatorname* { m a x } _ { z \in S } \ \left| z ^ { n } - ( a _ { n - 1 } z ^ { n - 1 } + a _ { n - 2 } z ^ { n - 2 } + \cdot \cdot \cdot + a _ { 0 } ) \right|
$$

has a unique solution. The total expression above is a polynomial of degree $\pmb { n }$ with leading coefficient 1 whose maximum modulus over $\boldsymbol { s }$ is minimum.We

will designate it by $\pmb { T } _ { n } ( S ; z )$ .We note that it is frequently called the Tschebyscheff polynomial of degree $_ { n }$ for $s$ .This adds greatly to the ambiguity of the expression“Tschebyscheff polynomial.”

Ex. 7. Let $\pmb { S }$ consist of $^ { \pmb { n } }$ distinct points $z _ { 1 } , \ldots , z _ { n }$ .Then

$$
T _ { n } ( S ; z ) = ( z \ - \ z _ { 1 } ) ( z \ - \ z _ { 2 } ) \cdot \cdot \cdot ( z \ - \ z _ { n } ) .
$$

Ex.8.Let $S \colon [ - 1 , 1 ]$ . Then $T _ { n } ( S ; z ) \ : = \ : \tilde { T } _ { n } ( z )$ (Cf. Def. 3.3.2).

Ex. 9.If $c$ designates the unit circle, $T _ { n } ( C ; z ) = z ^ { n }$ .We shall prove that if $p _ { n } ( z ) = z ^ { n } + a _ { 1 } z ^ { n - 1 } + \cdot \cdot \cdot + a _ { n } \not \equiv z ^ { n }$ ,then max $\left| p _ { n } ( z ) \right| > 1$ Consider zEC

$$
q ( z ) = { \frac { p _ { n } ( z ) } { z ^ { n } } } = 1 + { \frac { a _ { 1 } } { z } } + \cdot \cdot \cdot + { \frac { a _ { n } } { z ^ { n } } } .
$$

The function $q ( z )$ is analytic in the closed exterior of $c$ (including $\infty$ )，and $q ( \infty ) = 1$ .By the Maximum Principle,since $\pmb q$ is not a constant,

$$
\operatorname* { m a x } _ { | z | = 1 } \left| q ( z ) \right| > \left| q ( \infty ) \right| = 1 .
$$

Therefore, $\operatorname* { m a x } _ { | z | = 1 } \ \left| p _ { n } ( z ) \right| \ = \ \operatorname* { m a x } _ { | z | \ = 1 } \ \left| z ^ { n } \right| \left| q ( z ) \right| > 1 .$

7.6 Best Uniform (Tschebyscheff) Approximation of Continuous Functions. Let $f \in C [ a , b ]$ .We know by Theorem 7.5.6 that the problem of finding min pEPn $\operatorname* { m a x } _ { a \leq x \leq b } | f ( x ) - p ( x ) |$ has a unique solution.Designate the solution by $\pmb { p _ { n } } ( x )$ and set ${ E } _ { n } ( f ) = \operatorname* { m a x } _ { a \leq x \leq b } | f ( x ) - p _ { n } ( x ) |$ (The polynomial ${ \pmb p } _ { \pmb n } ( { \pmb x } )$ is frequently called the Tschebyscheff approximation of degree $\leq n$ to $f ( x ) . )$

THEOREM 7.6.1．If $f \in C [ \pmb { a } , \pmb { b } ]$ ,then

$$
{ \cal E } _ { 0 } ( f ) \ge { \cal E } _ { 1 } ( f ) \ge \cdots a n d \operatorname* { l i m } _ { n \to \infty } { \cal E } _ { n } ( f ) = 0 .
$$

Proof: We have already noted the monotonicity in (7.4.12).

Let $\varepsilon > 0$ be given.By Weierstrass' theorem we can find a polynomial of degree $\pmb { m }$ ， ${ \pmb q } _ { m } ( { \pmb x } )$ ,such that $| f ( x ) - q _ { m } ( x ) | \leq \varepsilon ,$ ${ a \leq x \leq b }$ Hence,

$$
E _ { m } ( f ) = \operatorname* { m a x } _ { a \leq x \leq b } | f ( x ) - p _ { m } ( x ) | \leq \operatorname* { m a x } _ { a \leq x \leq b } | f ( x ) - q _ { m } ( x ) | \leq \varepsilon .
$$

Thus, ${ \pmb { { \cal E } } } _ { n } ( f ) \leq \varepsilon$ for all $\pmb { n } \geq m$ ,establishing the second assertion.

We shall now characterize the behavior of the best uniform approximants.An examination of the cases $\pmb { n = 0 }$ and ${ \pmb n } = { \bf 1 }$ will provide insight to the general theorem and will help us to understand a simple,but fussy, proof.

Let $f ( x ) \in C [ a , b ]$ .We are interested in solving the problem of finding $\operatorname* { m i n } _ { c } { \operatorname* { m a x } _ { a \leq x \leq b } | f ( x ) - c | }$ .A glance at Figure 7.6.1 leads us to the following answer. Let $m = \operatorname* { m i n } _ { a \leq x \leq b } f ( x ) , M = \operatorname* { m a x } _ { a \leq x \leq b } f ( x )$ Then the minimizing constant

$$
c = { \frac { 1 } { 2 } } ( m + M )
$$

and

$$
E _ { 0 } ( f ) = { \textstyle \frac { 1 } { 2 } } ( M - m ) .
$$

![](../chunks/Interpolation and Approximation (Philip J. Davis) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0141-0210/auto/images/34009bb01abd2fdb95e55d1635da660f03d75c632a633ded58b3e24791349794.jpg)  
Figure 7.6.1.

![](../chunks/Interpolation and Approximation (Philip J. Davis) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0141-0210/auto/images/1dc208a4644ba1087a953d9287de737d4ff4c9133956e032615da35d344aff3a.jpg)  
Figure 7.6.2.

![](../chunks/Interpolation and Approximation (Philip J. Davis) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0141-0210/auto/images/b1126b461ca6b6fd955117085bbea5cb86fbe0e537e69d99f09e6d2ad69a7486.jpg)  
Figure 7.6.3.

Notice that when the error curve $\varepsilon ( x ) = f ( x ) - c$ is drawn, the value $\pm \pmb { { \cal E } _ { 0 } }$ is assumed by it at least twice: once with a plus sign and once with a minus sign.Suppose next that $p _ { 1 } ( x ) = a _ { 0 } + a _ { 1 } x$ solves the problem of fnding $P \in \mathcal { P } _ { 1 } \ a \leq x \leq b$ $| f ( x ) - p ( x ) |$ . Consider the error curve $\pmb \varepsilon ( \pmb x ) = \pmb f ( \pmb x ) - p _ { 1 } ( \pmb x )$ Set $E _ { 1 } \dot { = } \operatorname* { m a x } _ { a \le x \le b } | f ( x ) - p _ { 1 } ( x ) |$ .Since $| \varepsilon ( x ) |$ is in $C [ \boldsymbol { a } , \boldsymbol { b } ]$ ,this maximum is assuined at least once.If it were taken on only once (Fig.7.6.3) then by the addition of an appropriate constant to ${ p } _ { 1 } ( { \pmb x } )$ we could lower $\pmb { { \cal E } } _ { 1 }$ .This would contradict the definition of ${ \pmb E _ { 1 } }$

Suppose $E _ { 1 }$ is taken on only two times.It must be taken on with opposite signs,otherwise we can argue as above and lower $\pmb { { \cal E } } _ { 1 }$ .But even if it were taken on with opposite signs,we could subtract from $\varepsilon ( x )$ ,and hence from the original $p _ { 1 } ( x )$ ，an appropriate linear function which would have the effect of reducing the size of the maximum values without raising other values in excess of this.This is more or less evident geometrically (look at the dashed line in Fig.7.6.4),but we can formalize the argument in this way.

![](../chunks/Interpolation and Approximation (Philip J. Davis) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0141-0210/auto/images/08a62f0d1c366022bd926f12cd2a6d73da749523b5b29dc3f6ee617974b743de.jpg)  
Figure 7.6.4.

Let $\pmb { \varepsilon } ( \pmb { x _ { 1 } } ) = + \pmb { E _ { 1 } }$ and $\varepsilon ( x _ { 2 } ) = - E _ { 1 }$ .By continuity,we can find two closed intervals, $I _ { 1 }$ containing $\pmb { x _ { 1 } }$ ,and $\boldsymbol { I } _ { 2 }$ containing $x _ { \pmb { 2 } }$ such that $\varepsilon ( x ) > E _ { 1 } / 2$ in $I _ { 1 }$ and $\varepsilon ( x ) < - E _ { 1 } / 2$ in $I _ { 2 } . I _ { 1 }$ and $I _ { 2 }$ are disjoint, for $\varepsilon ( x )$ is of opposite sign in them.Pick a point $\pmb { x _ { 0 } }$ between $x _ { 1 }$ and $x _ { \mathbf { 2 } }$ ，but exterior to these intervals, and let $\ell ( x )$ be a fixed linear function that passes through $\pmb { x _ { 0 } } .$ is positive in $\scriptstyle { I _ { 1 } }$ ,and negative in $I _ { 2 }$ (Fig. 7.6.5)

![](../chunks/Interpolation and Approximation (Philip J. Davis) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0141-0210/auto/images/6d6ce6a65725670557b60d6b3b817677b6a0a1b02edfce487904eba604820d76.jpg)  
Figure 7.6.5.

Let $\pmb { J }$ designate the closure of the set $[ a , b ] - I _ { 1 } - I _ { 2 }$ ，and write $E _ { 1 } ^ { \prime } =$ max $| \varepsilon ( x ) |$ . We can obviously arrange matters so that $\pmb { J }$ does not contain ${ \pmb x } _ { 1 }$ or ${ \pmb x } _ { \pmb { 2 } }$ .Since the maximum of $| \varepsilon ( x ) |$ is assumed only at $\pmb { x _ { 1 } }$ and ${ \pmb x } _ { \pmb { 2 } }$ we have $E _ { 1 } ^ { \prime } < E _ { 1 }$ .Finally,select a quantity $\eta$ that satisfies

$$
0 < \eta < ( E _ { 1 } - E _ { 1 } ^ { \prime } ) / 2 \operatorname* { m a x } _ { a \leq x \leq b } | { \ell ( x ) } | .
$$

The claim is now made that

$$
\operatorname* { m a x } _ { a \leq x \leq b } | f ( x ) - p _ { 1 } ( x ) - \eta \ell ( x ) | = \operatorname* { m a x } _ { a \leq x \leq b } | \varepsilon ( x ) - \eta \ell ( x ) | < E _ { 1 }
$$

and this contradicts the definition of ${ \pmb E } _ { 1 }$ . To show this: on $I _ { 1 }$ by (7.6.4)

$$
0 < \eta \ell ( x ) < \frac { \ell ( x ) ( E _ { 1 } - E _ { 1 } ^ { \prime } ) } { 2 \operatorname* { m a x } _ { a \leq x \leq b } | \ell ( x ) | } \leq \frac { E _ { 1 } } { 2 } < \varepsilon ( x ) .
$$

Hence $\varepsilon ( x ) > \eta \ell ( x )$ and

$$
\begin{array} { r l } & { | \varepsilon ( x ) - \eta \ell ( x ) | = \varepsilon ( x ) - \eta \ell ( x ) } \\ & { \qquad \le E _ { 1 } - \operatorname* { m i n } _ { x \in I _ { 1 } } \eta \ell ( x ) = E _ { 1 } - \mathrm { s o m e t h i n g ~ p o s i t i v e } < E _ { 1 } . } \end{array}
$$

A similar argument holds for $\scriptstyle I _ { 2 }$ .Now for $\pmb { J }$ Using (7.6.4),

$$
\operatorname* { m a x } _ { x \in J } | \varepsilon ( x ) - \eta \ell ( x ) | \leq \operatorname* { m a x } _ { x \in J } | \varepsilon ( x ) | + \eta \operatorname* { m a x } _ { x \in J } | \ell ( x ) |
$$

$$
< { E _ { 1 } } ^ { \prime } + \frac { \underset { x \in J } { \operatorname* { m a x } } \left| \ell ( x ) \right| } { \underset { a \leq x \leq b } { \operatorname* { m a x } } \left| \ell ( x ) \right| } \frac { ( E _ { 1 } - E _ { 1 } ^ { \prime } ) } { 2 } < { E _ { 1 } } ^ { \prime } + E _ { 1 } - { E _ { 1 } } ^ { \prime } = E _ { 1 } .
$$

Therefore (7.6.5) holds.

It follows that there must be at least thre points ${ x _ { 1 } < x _ { 2 } < x _ { 3 } }$ where $\pmb { \varepsilon } ( \pmb { x } _ { i } ) = \pmb { \pm } \pmb { E _ { 1 } }$ .The error must alternate in signs at these three points: ${ \pmb E _ { 1 } }$ ， $- { \pmb { { E } } _ { 1 } } , { \pmb { { E } } _ { 1 } }$ or $- E _ { 1 } , E _ { 1 } , - E _ { 1 }$ .For one alternation has already been established, and if we had, say, $E _ { 1 } , - E _ { 1 } , - E _ { 1 }$ ，the same argument could be used to show that ${ \pmb E } _ { 1 }$ could be lowered.

THEOREM 7.6.2 (The Tschebyscheff Equioscillation Theorem).

Let $f ( x ) \in C [ a , b ]$ and ${ \pmb p } ( { \pmb x } )$ be the best uniform approximant to $f$ of degree $_ { n }$ Let ${ E _ { n } = \operatorname* { m a x } _ { a \leq x \leq b } | f ( x ) - p ( x ) | }$ and $\pmb { \varepsilon } ( \pmb { x } ) = \pmb { f } ( \pmb { x } ) - \pmb { p } ( \pmb { x } )$ . There are at least $\mathscr { n } + 2$ points $a \leq x _ { 1 } < x _ { 2 } < \cdot \cdot \cdot < x _ { n + 2 } \leq b$ where $\varepsilon ( x )$ assumes the values $\pm \pmb { { E _ { n } } }$ and with alternating signs:

$$
\begin{array} { l l } { { \varepsilon ( x _ { i } ) = \pm E _ { n } ~ } } & { { i = 1 , 2 , . . . , n + 2 } } \\ { { \varepsilon ( x _ { i } ) = - \varepsilon ( x _ { i + 1 } ) ~ } } & { { i = 1 , 2 , . . . , n + 1 . } } \end{array}
$$

Proof: Select an $\pmb \varepsilon$ so small that $| x _ { 1 } - x _ { 2 } | < \varepsilon$ implies

$$
| \varepsilon ( x _ { 1 } ) - \varepsilon ( x _ { 2 } ) | \leq E _ { n } / 2 .
$$

This is possible by the uniform continuity of ${ \pmb \varepsilon } ( { \pmb x } )$ .Divide $[ \pmb { a } , \pmb { b } ]$ into consecutive closed intervals of width $\le \varepsilon$ . Call the intervals on which $| \varepsilon ( x ) |$ assumes its maximum value $\cal I _ { 1 } , \cal I _ { 2 } , \dots , \cal I _ { m }$ Since ${ \pmb \varepsilon } ( { \pmb x } )$ can vary at most $\textstyle { E _ { n } } / 2$ in any of these intervals,we must have

$$
\varepsilon ( x ) > E _ { n } / 2 \quad \mathrm { o r } \quad \varepsilon ( x ) < - E _ { n } / 2
$$

there. Let $u _ { 1 } , . . . , u _ { m } ( = \pm 1 )$ be the sign of ${ \pmb \varepsilon } ( { \pmb x } )$ over these intervals.We must prove that in this sequence there are at least $n + 1$ changes of sign.

We do this by showing that if there were fewer than $n + 1$ changes，we could find a polynomial whose ${ \pmb E } _ { n }$ is less than that of $p ( x )$

If all the u's were the same,by adding an appropriate constant to ${ \pmb p } ( { \pmb x } )$ we could get a better approximation. Suppose then，we go through the intervals $I _ { 1 } , \ldots , I _ { m }$ and group them into consecutive groups where the u's have the same sign:

$$
k \mathrm { t h ~ g r o u p ~ } T ^ { ( j _ { k - 1 } + 1 ) } , \qquad \cdot \cdot \cdot , I ^ { ( j _ { k } ) }
$$

(Here we have written $I ^ { ( 1 ) } = I _ { 1 } , \cdot \cdot \cdot , I ^ { ( j _ { k } ) } = I _ { m } ,$ etc.)

This scheme displays $k - 1$ changes of sign so let us assume that

$$
k - 1 < n + 1 \mathrm { o r } k < n + 2 .
$$

Consider the intervals $I ^ { ( j _ { 1 } ) } , ~ I ^ { ( j _ { 1 } + 1 ) }$ . These intervals cannot be adjacent for $\varepsilon ( x )$ is O in neither and yet it has opposite signs there.Hence (with an obvious notation) we can find an $x _ { 1 }$ ：

$$
\begin{array} { r } { I ^ { ( j _ { 1 } ) } < x _ { 1 } < I ^ { ( j _ { 1 } + 1 ) } } \\ { I ^ { ( j _ { 2 } ) } < x _ { 2 } < I ^ { ( j _ { 2 } + 1 ) } } \end{array}
$$

Similarly,

$$
I ^ { ( j _ { k - 1 } ) } < x _ { k - 1 } < I ^ { ( j _ { k - 1 } + 1 ) } .
$$

Form the polynomial $q ( x ) = ( x _ { 1 } - x ) ( x _ { 2 } - x ) \cdot \cdot \cdot ( x _ { k - 1 } - x )$

Since we have assumed $\pmb { k } < \pmb { n } + \pmb { 2 }$ ，it follows that $k - 1 \leq n$ ，so that $q ( x ) \in { \mathcal { P } } _ { n } .$ $q ( x )$ vanishes only at $x _ { i }$ .Since the $x _ { i }$ are between the intervals $I _ { 1 } , \ldots , I _ { m } , $ $\pmb q$ must have constant sign over each of these intervals.

![](../chunks/Interpolation and Approximation (Philip J. Davis) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0141-0210/auto/images/cbe9d333c65d6f99cc548e66e2f0ff8b2cfd1db174efe9c236875a8fbde631a1.jpg)  
Figure 7.6.6.

Over the first group of intervals $q ( x ) = ( x _ { 1 } - x ) \cdot \cdot \cdot ( x _ { k - 1 } - x )$ is positive, for all factors are positive.Over the second group $q ( x )$ is negative, for all but the first factor are positive,etc.By selecting $u = \pm 1$ appropriately, $u q ( x )$ will coincide with $\varepsilon ( x )$ in sign over all the intervals $I _ { 1 } , \ldots , I _ { m }$

We now claim that for $\eta$ sufficiently small, $p ( { \pmb x } ) + \eta u q ( { \pmb x } )$ will be a better approximant to $f$ than $\pmb { p }$ is.This would be a contradiction.Let $\pmb { J }$ be the closure of $[ a , b ] - I _ { 1 } - I _ { 2 } - \cdot \cdot \cdot - I _ { m }$ Write ${ E _ { n } } ^ { \prime } = \operatorname* { m a x } _ { x \in J } | \varepsilon ( x ) |$ . Since the maxima of $| \varepsilon ( x ) |$ are assumed only on the $\boldsymbol { { \cal I } }$ s we have ${ \mathbf Z _ { n } } ^ { \prime } < { \pmb E _ { n } }$ .Select an $\eta$ that satisfies

$$
0 < \eta < ( E _ { n } - E _ { n } ^ { \prime } ) / 2 \operatorname * { m a x } _ { a \leq x \leq b } | q ( x ) | .
$$

The rest of the argument parallels exactly the discussion following (7.6.5).

In one case it is possible to give an explicit construction of the best uniform approximant.

COROLLARY 7.6.3. Let $f ( x ) \in C ^ { 2 } \left[ a , b \right]$ and let $f ^ { \prime \prime } ( x ) > 0$ there. If ${ a _ { 0 } + a _ { 1 } x }$ is the best uniform linear approximant to $f _ { i }$ then

$$
\begin{array} { l } { \displaystyle a _ { 1 } = \frac { f ( b ) - f ( a ) } { b - a } } \\ { \displaystyle a _ { 0 } = \frac { 1 } { 2 } ( f ( a ) + f ( c ) ) - \frac { f ( b ) - f ( a ) } { b - a } \frac { a + c } { 2 } } \end{array}
$$

whereistheiqueoiof((.

Prof: One solutin to he quatio $f ^ { \prime } ( c ) = { \frac { f ( b ) - f ( a ) } { b - a } }$ is garanteed by the mean value theorem. Since $f ^ { \prime \prime } > 0 , f ^ { \prime }$ is increasing，and hence this solution is unique.

Now set

$$
\varepsilon ( x ) = f ( x ) - ( a _ { 0 } + a _ { 1 } x ) .
$$

By our theorem, there are at least 3 distinct points ${ x _ { 1 } < x _ { 2 } < x _ { 3 } }$ where $\varepsilon ( x )$ reaches its maximum absolute value. One point, ${ \pmb x } _ { \pmb { 2 } }$ ,is interior to the interval and hence $\pmb { \varepsilon } ^ { \prime } ( x _ { 2 } ) = 0$ Since ${ \varepsilon } ^ { \prime } ( x ) = f ^ { \prime } ( x ) - a _ { 1 } , \ { \varepsilon } ^ { \prime }$ is also strictly increasing. The other two extreme points of $\varepsilon ( x )$ must therefore be at $\pmb { a }$ and $\pmb { b }$ Now with $x _ { 1 } = a$ ， ${ \pmb x _ { 2 } } = { \pmb c }$ ， $\pmb { x _ { 3 } } = \pmb { b }$ ,it follows that

$$
f ( a ) - ( a _ { 0 } + a _ { 1 } a ) = - ( f ( c ) - ( a _ { 0 } + a _ { 1 } c ) ) = f ( b ) - ( a _ { 0 } + a _ { 1 } b )
$$

and

$$
\begin{array} { r } { \varepsilon ^ { \prime } ( c ) = f ^ { \prime } ( c ) - a _ { 1 } = 0 . } \end{array}
$$

These conditions,rearranged,lead to (7.6.8).

The best uniform (Tschebyscheff） approximant is completely characterized by the property of equioscillation at $\textstyle { n + 2 }$ points. This property is frequently the basis of numerical schemes for computing the approximant.

THEOREM 7.6.4. Let $f ( x ) \in C [ a , b ]$ . Given a $q ( x ) \in \mathcal { P } _ { n }$ with

$$
\operatorname* { m a x } _ { a \leq x \leq b } | f ( x ) - q ( x ) | = \delta .
$$

Let there be $n + 2$ points $a \leq x _ { 1 } < x _ { 2 } < \cdots < x _ { n + 2 } \leq b$ such that

$$
f ( x _ { i } ) - q ( x _ { i } ) = \pm \delta , \qquad i = 1 , 2 , \ldots , n + 2 ,
$$

in an alternating fashion. Then,

$$
\delta = E _ { n } ( f )
$$

and $\pmb q$ is the best uniform approximant to $f$ in $\mathcal { P } _ { n }$

Proof:By definition, ${ \pmb { { \cal E } } } _ { n } ( f ) \leq \delta$ Assume $E _ { n } ( f ) < \delta$ Let ${ \pmb p } ( { \pmb x } )$ be the best uniform approximant.Then

$$
q ( x _ { i } ) - p ( x _ { i } ) = q ( x _ { i } ) - f ( x _ { i } ) - ( p ( x _ { i } ) - f ( x _ { i } ) )
$$

Since $\operatorname* { m a x } _ { a \leq x \leq b } | f ( x ) - p ( x ) | = E _ { n } ( f ) < \delta$ ，then writing $\tau _ { i } = p ( x _ { i } ) - f ( x _ { i } )$ we   
have $| \tau _ { i } | < \delta$ ， $q ( x _ { i } ) - p ( x _ { i } ) = \pm \delta - \tau _ { i }$ The function $q ( x ) - p ( x ) \in \mathcal { P } _ { n }$ and has $\mathbf { \mathscr { n } } + \mathbf { \mathscr { 2 } }$ points of alternation.It therefore has $n + 1$ zeros and consequently must be identically zero by Theorem l.1l.3.Conclusion: $q ( x ) \equiv p ( x )$

![](../chunks/Interpolation and Approximation (Philip J. Davis) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0141-0210/auto/images/52b42685cb46d837292f528fdbfafa716a082a59262774746305c1d9b8110387.jpg)  
Figure 7.6.7 Tschebyscheff's Equioscillation Theorem.

The best uniform approximant to $\cos { \frac { \pi } { 2 } } x$ over[−1, 1] out of $\mathcal { P } _ { \mathfrak { s } }$ is

$$
p ( x ) = 0 . 9 9 9 4 0 3 2 - 1 . 2 2 2 7 9 6 7 x ^ { 2 } + 0 . 2 2 3 9 9 0 3 x ^ { 4 } .
$$

$\varepsilon ( x ) = \cos { \frac { \pi } { 2 } } x - p ( x )$ assumes its extreme values at $5 + 2$ points and with alternating sign.

7.7 Best Approximation by Nonlinear Families. The situation here is more complicated than in the case of linear families.A few examples will suffice to show what can happen.

Ex.1． Consider the problem min $\operatorname* { m a x } _ { 1 \leq x \leq 2 } \left| 0 - e ^ { a x } \right|$ .By selecting $^ { a }$ very large a and negative,the maximum can be made as small as desired.The problem is, so to speak,solved by $a = - \infty$

Ex. 2. Consider the problem min $\operatorname* { m a x } _ { 0 \leq x \leq 1 } | \frac { 1 } { 2 } - x ^ { a ^ { 2 } } |$ . For any value $^ { a }$ ， a

$$
\operatorname* { m a x } _ { 0 \le x \le 1 } | \frac { 1 } { 2 } - x ^ { a ^ { 2 } } | = \frac { 1 } { 2 } .
$$

Thus,while no proper value solves the first problem,any value at all solves the second.

One of the inost familiar nonlinear families is fortunate enough to contain best uniform approximations.

THEOREM 7.7.1. Let $f ( x ) \in C [ a , b ]$ and let m and n be fixed integers $\geq 0$ $\mathit { T h e \ p r o b l e m \ o f \ f i n d i n g \operatorname* { m i n } _ { a _ { i } , b _ { i } } \operatorname* { m a x } _ { a \le x \le b } } \left| f ( x ) - \frac { a _ { 0 } x ^ { n } + a _ { 1 } x ^ { n - 1 } + \cdot \cdot \cdot + a _ { n } } { b _ { 0 } x ^ { m } + b _ { 1 } x ^ { m - 1 } + \cdot \cdot \cdot + b _ { m } } \right|$ has $^ { \pmb { a } }$ solution.

Proof:There is some redundancy in the coeffcients of the rational function.We can adjust them so that $b _ { 0 } { } ^ { 2 } + b _ { 1 } { } ^ { 2 } + \cdot \cdot \cdot + b _ { m } { } ^ { 2 } = 1$ As the $^ { b }$ 's vary,we will certainly obtain some polynomials that do not vanish in $[ a , b ]$ If we set

$$
\Delta = \operatorname* { i n f } _ { a _ { i } , b _ { j } } \operatorname* { m a x } _ { a \leq x \leq b } \left| f ( x ) - \frac { a _ { 0 } x ^ { n } + \cdot \cdot \cdot } { b _ { 0 } x ^ { m } + \cdot \cdot \cdot } \right| ,
$$

then $0 \leq \Delta < \infty$ .By the definition of $\Delta$ , we can find a sequence of rational functions

$$
R _ { k } ( x ) = \frac { A _ { k } ( x ) } { B _ { k } ( x ) } , A _ { k } ( x ) = \sum _ { i = 0 } ^ { n } a _ { i } ^ { ( k ) } x ^ { n - i } , B _ { k } ( x ) = \sum _ { j = 0 } ^ { m } b _ { j } ^ { ( k ) } x ^ { m - j }
$$

so that if

then

$$
\Delta _ { k } = \operatorname* { m a x } _ { a \le x \le b } | f ( x ) - R _ { k } ( x ) | ,
$$

$$
\operatorname* { l i m } _ { k  \infty } \Delta _ { k } = \Delta .
$$

The coefficients ${ b } _ { j } ^ { ( k ) }$ are bounded due to the normalizing condition.The coefficients $a _ { i } ^ { ( k ) }$ are also bounded. This can be seen as follows.From (7.7.1),

Hence

$$
\begin{array} { r l } { \quad } & { { } \quad - \Delta _ { k } \leq f ( x ) - R _ { k } ( x ) \leq \Delta _ { k } . } \\ { \quad } & { { } } \\ { \quad } & { { } \quad | R _ { k } ( x ) | \leq \Delta _ { k } + \displaystyle \operatorname* { m a x } _ { a \leq x \leq b } | f ( x ) | \leq M } \end{array}
$$

for some constant $M$ .This means that

$$
\begin{array} { r } { | A _ { k } ( x ) | \le M | B _ { k } ( x ) | . } \end{array}
$$

Since the ${ b } _ { j } ^ { ( k ) }$ are bounded, the polynomials $B _ { \boldsymbol { k } } ( \boldsymbol { x } )$ are bounded on $[ a , b ]$ ， and therefore $A _ { k } ( x )$ are bounded.Now if a family of polynomials of bounded degrees are bounded,then its coeffcients are bounded. (See Problem 40.)

Consider the points $P _ { k }$ ： $( a _ { 0 } ^ { ( k ) } , a _ { 1 } ^ { ( k ) } , \ldots , a _ { n } ^ { ( k ) } , b _ { 0 } ^ { ( k ) } , b _ { 1 } ^ { ( k ) } , \ldots , b _ { m } ^ { ( k ) } )$ in the space $\scriptstyle R _ { m + n + 2 }$ .They lie in a bounded portion of that space.Hence,we may select a subsequence $P _ { k _ { l } }$ that converges to a point

$$
P ^ { \prime } = ( a _ { 0 } ^ { \prime } , a _ { 1 } ^ { \prime } , \ldots , a _ { n } ^ { \prime } , b _ { 0 } ^ { \prime } , b _ { 1 } ^ { \prime } , \ldots , b _ { m } ^ { \prime } ) .
$$

Consider the rational functions corresponding to this subsequence,and reindex the subsequence so that we have

Form

$$
\begin{array} { c c } { \displaystyle \operatorname* { l i m } _ { k \to \infty } a _ { i } ^ { ( k ) } = a _ { i } ^ { \prime } \qquad } & { i = 0 , 1 , \ldots , n } \\ { \displaystyle \operatorname* { l i m } _ { k \to \infty } b _ { j } ^ { ( k ) } = { b _ { j } } ^ { \prime } \qquad } & { j = 0 , 1 , \ldots , m . } \end{array}
$$

$$
R ^ { \prime } ( x ) = \frac { { a _ { 0 } } ^ { \prime } x ^ { n } + { a _ { 1 } } ^ { \prime } x ^ { n - 1 } + \dots + { a _ { n } } ^ { \prime } } { { b _ { 0 } } ^ { \prime } x ^ { m } + { b _ { 1 } } ^ { \prime } x ^ { m - 1 } + \dots + { b _ { m } } ^ { \prime } } .
$$

If we can show that

$$
\operatorname* { m a x } _ { a \leq x \leq b } | f ( x ) - R ^ { \prime } ( x ) | = \Delta
$$

then $\pmb { R } ^ { \prime }$ will be a best approximant and our proof is complete.

$\scriptstyle { R ^ { \prime } }$ ,being rational,can have at most a finite number of infinities.Let $D ( { \pmb x } )$ be the denominator of $R ^ { \prime } ( x )$ and select an $_ { \pmb { x } }$ in $[ a , b ]$ such that $D ( x ) \neq 0$ At such a point we must have $\operatorname* { l i m } _ { k  \infty } R _ { k } ( x ) = R ^ { \prime } ( x )$ . Since

hence

$$
\begin{array} { c } { { R ^ { \prime } ( x ) = f ( x ) + R _ { k } ( x ) - f ( x ) + R ^ { \prime } ( x ) - R _ { k } ( x ) , } } \\ { { \mid R ^ { \prime } ( x ) \mid \leq \mid f ( x ) \mid + \mid f ( x ) - R _ { k } ( x ) \mid + \mid R ^ { \prime } ( x ) - R _ { k } ( x ) \mid ; } } \end{array}
$$

$$
| R ^ { \prime } ( x ) | \leq \operatorname* { m a x } _ { a \leq x \leq b } | f ( x ) | + \Delta _ { k } + \varepsilon _ { k } , \varepsilon _ { k } \to 0 .
$$

Setting $\mu = \operatorname* { s u p } _ { k } \Delta _ { k } ,$ and allowing $k \to \infty$ ，

$$
| R ^ { \prime } ( x ) | \leq \operatorname* { m a x } _ { a \leq x \leq b } | f ( x ) | + \mu .
$$

The bound (7.7.7) holds uniformly for any $\pmb { x }$ in $[ a , b ]$ for which $D ( x ) \neq 0$ This,in turn,means that $\scriptstyle { R ^ { \prime } } ( x )$ cannot have any infinities on $[ a , b ]$ ,for if it did,there would be values of $_ { \pmb { x } }$ ina neighborhood of the infinity where the bound would be exceeded.

Let $\pmb { x }$ be any point of $[ a , b ]$ .Suppose first that $D ( x ) \neq 0$ .Then for $k =$ $\mathbf { 1 , 2 , . . . }$ ，

$$
\begin{array} { r } { \begin{array} { r } { | f ( x ) - R ^ { \prime } ( x ) | \leq | f ( x ) - R _ { k } ( x ) | + | R _ { k } ( x ) - R ^ { \prime } ( x ) | } \\ { \leq \Delta _ { k } + \eta _ { k } \mathrm { ~ w h e r e ~ } \eta _ { k } \to 0 . } \end{array} } \end{array}
$$

Thus,

$$
| f ( x ) - R ^ { \prime } ( x ) | \leq \Delta .
$$

Suppose that $D ( x ) = 0$ . Then we may find a sequence of points of $[ a , b ] , x _ { 1 } .$ $x _ { 2 } , . . .$ ,such that $x _ { i } \to x$ ， $D ( x _ { i } ) \neq 0$ .Then by (7.7.8), $| f ( x _ { i } ) - R ^ { \prime } ( x _ { i } ) | \leq \Delta .$ $i = 1$ ，2,...，and by continuity, $| f ( x ) - R ^ { \prime } ( x ) | \leq \Delta$ .We have therefore shown that $| f ( x ) - R ^ { \prime } ( x ) | \leq \Delta$ throughout $[ a , b ]$ .By the definition of $\Delta$ ， this implies (7.7.6).

# NOTES ON CHAPTER VII

Works on functional analysis that have been found useful include Banach [1],Riesz-Sz.Nagy [l],Ljusternik and Sobolew [1],Kolmogorov and Fomin [1], Taylor [3],Dunford and Schwartz [1], Zaanen [1].

7.2 The convexity of $x ^ { \star }$ ， $r > 1$ ,can be used to prove (7.2.5). See Boas [4], p. 148. 7.3Eggleston [l] is a fine presentation of the theory of convex bodies. 7.4 Achieser [1]. 7.5For further results on uniqueness,see Hirschfeld [1],[2].An extension of Theorem 7.5.6 to rational functions can be found in Walsh [2], p.363. 7.6de la Vallée Poussin [l],Natanson [l]. The numerical side of best uniform approximation by polynomials and rationals had to wait for the development of electronic computing equipment.For part of the vast literature that has developed around this problem,see Remez [l],Stiefel [l], Maehly and Witzgall [1], [2],Murnaghan and Wrench [1], [2].Ward [1] expounds the problem from the point of view of linear programming.

For a more abstract approach to problems of Tschebyscheff type see Rivlin and Shapiro [1].

7.7Approximation by nonlinear families is currently under investigation. See Motzkin [1],Rice [1],[2],[3]. See also Young [1].

# PROBLEMS

1. Let $_ n$ be fixed. $\pmb { S }$ consists of the $2 ^ { n } \ n$ -tuples $A , B , \ldots$ ，whose elements are either O or 1.If we set $d ( A , B ) =$ the number of places in which $\pmb { A }$ and $B$ differ,then $\pmb { S }$ becomes a metric space.This is the Hamming distance.

2.Let $\pmb { S }$ be a collection of sets $A , B , \ldots$ ，each of which contains a finite number of objects.If we set $d ( A , B ) =$ number of objects in $( A \cup B ) \ : - \ : ( A \cap B )$ then $\boldsymbol { s }$ isa metric space.This is the Silverman distance.

3.Is the following a norm in $R _ { 2 } \colon \| ( x , y ) \| = \operatorname* { m a x } { \big ( } 3 \left| x \right| + 2 \left| y \right| , 2 \left| x \right| + 3 \left| y \right| ) \mathclose { \mathfrak { T } }$   
4.In $\scriptstyle { \mathcal { R } } _ { n }$ ,define $\left\| ( a _ { 1 } , \cdot \cdot \cdot , a _ { n } ) \right\| = \operatorname* { m a x } _ { 0 \leq x \leq 1 } \left| \sum _ { k = 0 } ^ { n - 1 } a _ { k + 1 } x ^ { k } \right|$ . Is this a norm?   
5.Does the following expression define a norm in $C ^ { \mathbf { 1 } } [ a , b ]$ ：

$$
\| f \| = \operatorname* { m a x } _ { a \leq x \leq b } [ { \big | } f ( x ) { \big | } , { \big | } f ^ { \prime } ( x ) { \big | } ] \ P
$$

6. Show that $\scriptstyle { R _ { n } }$ can be normed as follows: Let $w _ { 1 } , w _ { 2 } , \ldots , w _ { n }$ be a fixed sequence of positive constants. Set $\| x \| = \operatorname* { m a x } _ { 1 \leq j \leq n } w _ { j } \left| x _ { j } \right|$

7. Prove that the postulate (7.2.1)(a) follows from (7.2.1)(c) and (7.2.1)(d).

8. Describe the gauge curve that gives rise to the norm $\left\| ( x , y ) \right\| = 3 { \big | } x { \big | } + 2 { \big | } y { \big | }$ in $R _ { 2 }$

9. In the space $C [ - 1 , 1 ]$ ,is the norm $\left\| f \right\| = \int _ { - 1 } ^ { + 1 } \left| f ( x ) \right| d x$ strictly convex? 10. Let the ellipse ${ \frac { x ^ { 2 } } { a ^ { 2 } } } + { \frac { y ^ { 2 } } { b ^ { 2 } } } = 1$ act as the gauge curve for a Minkowski plane. Find the equation of the“Minkowski circle’ of radius $\mathscr { r }$ and center $( x _ { \mathbf { 0 } } , y _ { \mathbf { 0 } } )$

11.Let $\boldsymbol { \mathfrak { c } }$ be a Minkowski gauge curve no part of which is a line segment. Prove that the resulting norm is strictly convex.

12. If $\boldsymbol { x }$ is strictly convex, then $\| x \| = \| y \| = r , x \neq y$ implies

$$
\| t x + ( 1 - t ) y \| < r \quad \mathrm { f o r } \quad 0 < t < 1 .
$$

Geometrically,the surface $\| { \boldsymbol { x } } \| = r$ does not contain a line segment.

13.If a linear space $\boldsymbol { x }$ satisfies (7.2.1)(a),(c),(d) but if $\| x \| = 0$ does not necessarily mean that $x = 0$ ，then $X$ is called a seminormed space.Show that $O ^ { 1 } [ a , b ]$ with $\| f \| ^ { 2 } = \int _ { a } ^ { b } | f ^ { \prime } ( x ) | ^ { 2 } d x$ is a seminormed space.

14.Prove that Theorem 7.4.1 holds in a seminormed linear space.Formulate several concrete examples.

15.Let $\boldsymbol { X }$ be a linear space and let $\mathcal { L }$ be a family of linear functionals taken from $X ^ { * }$ .Show that $\| x \| = \ \sup _ { L \in \mathcal { L } } \ \big | L ( x ) \big |$ defines a seminorm on $X$ When is it a norm？

16.Show that the fundamental theorem 7.4.1 holds if the $a _ { i }$ are allowed to vary only over a preassigned closed set.

17.Interpret Holder's inequality (7.2.7） for in the light of Ex.4,7.2.

$\textit { \textbf { p } } = 1$ 18.Prove Young's criterion:Let $_ y$ bea fixed element of a normed linear space and let the variable element $_ { x }$ be a function of $\pmb { n }$ real or complex parameters $a _ { 1 } , \ldots , a _ { n }$ defined for $| a _ { i } | < \infty : \ x = x ( a _ { 1 } , \ldots , a _ { n } )$ .Suppose that (a) $\| x ( a _ { 1 } , \ldots , a _ { n } ) \|$ is a continuous function of its parameters (b) $\| x ( a _ { 1 } , \cdot \cdot \cdot , a _ { n } ) \| \leq M$ implies there is an $\pmb { N }$ such that $\left| a _ { i } \right| \le N \ i = 1 , 2 , . . . , n$ ，Then the problem min $\| y \_ { \neg } x ( a _ { 1 } , \dotsc , a _ { n } ) \|$ has a solution.

19.Show that Young's criterion is not necessary for the existence of minimizing parameters.

20．Solve the problem   
21.Solve the probler

22.Solve the problem

$$
\begin{array} { r l } & { \underset { 0 \leq x \leq 1 } { \operatorname* { m a x } } \ \vert e ^ { x } - a x - b \vert = \mathrm { m i n i m u m } . } \\ & { \underset { 0 \leq x \leq 1 } { \operatorname* { m a x } } \ \vert e ^ { x } - a \vert \ d x = \mathrm { m i n i m u m } . } \\ & { \underset { a } { \operatorname* { m i n } } \ \underset { 0 \leq x \leq 1 } { \operatorname* { m a x } } \ \vert x ^ { 4 } - a x \vert . \ \mathrm { I s ~ t h e ~ s o l u t i o n ~ u n i q u e } ? } \\ & { \underset { 0 \leq x \leq 1 } { \operatorname* { m i n g } } \underset { c } { \operatorname* { m i n } } \underset { - 1 } { \overset { 1 } { \operatorname* { m } } } \vert x - c x ^ { 2 } \vert \ d x \ \mathrm { d o e s ~ n o t ~ h a v e ~ a ~ u n i q u e ~ s ~ } } \end{array}
$$

23. The problem of fi solution.

24. Let $\boldsymbol { \mathcal { P } _ { 2 } }$ be normed by $\| p \| = \left| p ( 0 ) \right| + \left| p ( 1 ) \right| + \left| p ( 2 ) \right|$ Determine the best approximation to $x ^ { 2 }$ by a constant.

25.Referring to Figure 7.6.7,compare the accuracy of the best uniform eprximant to cos ${ \frac { \pi } { 2 } } x$ withthatoftTylooant.

26.Let $f ( x ) = 0 , - 1 \leq x \leq 0 , f ( x ) = 1 , 0 <$ $0 < x \le 1$ . Compute

$$
\operatorname * { m i n } _ { g ( x ) \in C [ - 1 , 1 ] } \quad \operatorname * { m a x } _ { - 1 \leq x \leq 1 } \quad \big | f ( x ) - g ( x ) \big | .
$$

27. Given $\mathscr { n }$ points in the plane $P _ { i } \colon ( x _ { i } , y _ { i } ) i = 1 , 2 , . \textup { -- } , n . P _ { 0 }$ is one additional point.Show that there exists a straight line through $P _ { 0 } \colon y = a _ { 0 } x + a _ { 1 }$ such thatm $\begin{array} { l } { \underset { \leq n } { \bf x } \left| y _ { i } - ( a _ { 0 } x _ { i } + a _ { 1 } ) \right| = 1 } \end{array}$ minimum. Generalize.

28.Given $_ { n }$ points in the plane $P _ { 1 } , \ldots , P _ { n }$ Let $\scriptstyle d ( P _ { i } , \ell )$ designate the per  
pendicular distance from $P _ { i }$ to a straight line $\ell$ .Show that there is a line $\ell$ such   
that_max $d ( P _ { i } , \ell ) = \mathrm { { m i n i m u m } }$ $\mathbf { 1 } \leq i \leq n$

29.Let $f ( x ) \in C [ a , b ]$ and consist of two linear portions.Determine the best uniform linear approximant to $f ( x )$ over $[ a , b ]$ .Interpret geometrically.

30.Let $B [ { \boldsymbol { a } } , { \boldsymbol { b } } ]$ designate the space of functions that are bounded over $[ a , b ]$ The problem of finding $\operatorname* { m i n } _ { p \in \mathcal { P } _ { n } } \ \operatorname* { m a x } _ { a \leq x \leq b } \ \left| f ( x ) - p ( x ) \right|$ has a solution,but it is not necessarily unique.

31. Discuss the problem of minimizing $\operatorname* { m a x } _ { - 1 \le x \le 1 } \left| 1 \ - f ( x ) \right|$ ,where the approximants $f$ satisfy $f \in C [ - 1 , 1 ] { \mathrm { ~ a n d } } \int _ { - 1 } ^ { + 1 } f ( x ) d x = 0 .$

32.Let $f ( x ) \in C ^ { 2 } [ a , b ]$ and be concave. $_ { r }$ is a variable point on the curve and $\pmb { T } ( \pmb { x } )$ is linear between $( a , f ( a ) )$ and $\pmb { P }$ ，and between $\pmb { P }$ and $( b , f ( b ) )$ . Show that there is a position of $\pmb { P }$ that minimizes $\int _ { a } ^ { b } f ( x ) \ - \ T ( x ) \ d x$ Interpret the position geometrically.

33.Characterize $\boldsymbol { s }$ in Theorem 7.5.l as the intersection of two convex sets.

34. The best uniform approximation to $\sqrt { 1 + x ^ { 2 } }$ on [0,1] bya linear function is $\mathbf { 9 5 5 + . 4 1 4 } x$

35.Derive the approximation ${ \sqrt { x ^ { 2 } + y ^ { 2 } } } \approx . 9 5 5 x + . 4 1 4 y x \geq y > 0$ and determine the error incurred.

36.Find the best uniform approximation to $\sqrt { 1 + x ^ { 3 } }$ by a straight line over [0,1].

37. Let $w ( x ) , f ( x ) \in C [ - 1 , 1 ]$ . Prove there is one and only one polynomial in ${ \mathcal { P } } _ { \pmb { n } }$ for which $\operatorname* { m a x } _ { - 1 \le x \le 1 } w ( x ) \left| f ( x ) - p ( x ) \right| = 1$ minimum.

38.Let $p ( x ) = z ^ { k } + a _ { 1 } z ^ { k - 1 } + \cdot \cdot \cdot + a _ { n } .$ If $\Gamma$ is the lemniscate $\vert p ( z ) \vert = a$ ,the Tschebyscheff polynomial of degree nk for $\Gamma$ is $[ p ( z ) ] ^ { n }$

39.Discuss the problem of finding $\operatorname* { m i n } _ { a , b } \operatorname* { m a x } _ { 0 \leq x \leq 1 } \left| x - a \sin b x \right| .$

40.A family of polynomials of bounded degree whose values on $[ a , b ]$ are bounded must have bounded coefficients.

# CHAPTERVIII

# Least Square Approximation

8.1 Inner Product Spaces. We come now to the approximation process most commonly employed and most highly developed: least squares. An abstract vantage point from which it is convenient to survey the common features of various least square approximations is provided by the theory of inner product spaces. If the subjects of algebra, geometry,and analysis can be said to have a “center of gravity,”it surely lies in this theory.

DEFINITION 8.1.l. A real linear space $\pmb { X }$ with elements $_ { \pmb { x } }$ will be called an inner product space,if there has been defined for each two elements ${ \pmb x _ { 1 } } , { \pmb x _ { 2 } }$ a real number designated by $( x _ { 1 } , x _ { 2 } )$ with the following properties

(a） $( x _ { 1 } + x _ { 2 } , x _ { 3 } ) = ( x _ { 1 } , x _ { 3 } ) + ( x _ { 2 } , x _ { 3 } )$ (Linearity) （(b） $( x _ { 1 } , x _ { 2 } ) = ( x _ { 2 } , x _ { 1 } )$ (Symmetry) （c） $( \alpha x _ { 1 } , x _ { 2 } ) = \alpha ( x _ { 1 } , x _ { 2 } ) , ~ \alpha { \mathrm { ~ r e a l } }$ (Homogeneity) （d） $( { \pmb x } , { \pmb x } ) \ge 0 , ( { \pmb x } , { \pmb x } ) = 0$ if and only if $\pmb { x } = 0$ (Positivity)

The quantity $( x _ { 1 } , x _ { 2 } )$ is called the inner product of $\pmb { x _ { 1 } }$ and ${ \pmb x } _ { \mathbf { 2 } }$

A similar definition can be made for complex linear spaces.The inner product $( x _ { 1 } , x _ { 2 } )$ will be a complex number and (8.1.l)(b) must be replaced by the condition

$$
\mathrm { ( b ^ { \prime } ) } \quad ( x _ { 1 } , x _ { 2 } ) = { \overline { { { ( x _ { 2 } , x _ { 1 } ) } } } } \quad \mathrm { ( H e r m i t i a n ~ S y m m e t r y ) }
$$

The bar in the above line designates the complex conjugate.

Ex.1. $X = R _ { n } . \ x \ = ( x _ { 1 } , x _ { 2 } , . . . , x _ { n } ) , y \ = ( y _ { 1 } , y _ { 2 } , . . . , y _ { n } )$ .Let $w _ { i }$ be $_ n$ fixed postive numbers Define $( x , y ) = \sum _ { i = 1 } ^ { n } w _ { i } x _ { i } y _ { i }$

Ex. 2. $x$ is the complex Euclidean space, $C _ { n }$ with elements

$$
x = ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } ) , x _ { i } { \mathrm { ~ c o m p l e x . } }
$$

Define

$$
( x , y ) = \sum _ { i = 1 } ^ { n } w _ { i } x _ { i } { \overline { { y _ { i } } } } .
$$

Ex. 3. $X = C [ a , b ]$ .If $x = f ( t ) , y = g ( t )$ ，we define

$$
( x , y ) = ( f , g ) = \int _ { a } ^ { b } f ( t ) g ( t ) d t .
$$

Ex.4.Let $B$ designate a bounded two dimensional region.Let $X$ designate the space of functions $f ( x , y )$ that are continuous in the closure of $B , \ w ( x , y )$ is afixedosiveus whttio $( f , g ) \ = \int _ { B } \int _ { } f ( x , y ) g ( x , y ) w ( x , y ) d x d y .$

Ex.5.Let $B$ be a bounded simply connected region of the complex plane with a simple,rectifiable boundary $\boldsymbol { c }$ Let $x$ be the complex linear space composed of all functions analytic in $B$ and continuous in $\smash { B \cup C }$ The line integral $( f , g ) = \int _ { C } f ( z ) { \overline { { g ( z ) } } } \ d s , d s ^ { 2 } = d x ^ { 2 } \ + \ d y ^ { 2 }$ is an inner produt for $x$

Ex.6.Let $X = L ^ { 2 } [ a , b ]$ and write $( f , g ) \ = \int _ { a } ^ { b } f ( x ) g ( x ) \ d x .$ (Cf. 7.2,Ex. 10,with $p = 2 .$ ）

Note several simple consequences of (8.1.1). From (c), $( 0 , x ) = 0$ From (c) and $( \mathbf { b } ^ { \prime } )$ ， $( x _ { 1 } , \alpha x _ { 2 } ) = \bar { \alpha } ( x _ { 1 } , x _ { 2 } )$ .From(a)and (b）or $( \mathbf { b } ^ { \prime } )$ ， $( x _ { 1 } , x _ { 2 } + x _ { 3 } ) =$ $( x _ { 1 } , x _ { 2 } ) + ( x _ { 1 } , x _ { 3 } )$ ·

THEOREM 8.1.1 (The Schwarz Inequality).

In an inner product space,

$$
| ( x _ { 1 } , x _ { 2 } ) | ^ { 2 } \leq ( x _ { 1 } , x _ { 1 } ) ( x _ { 2 } , x _ { 2 } ) .
$$

The equality sign holds if and only if $x _ { 1 }$ and $x _ { \mathbf { 2 } }$ are dependent.

Proof: If $x _ { 2 } = 0$ ， the theorem reduces to the trivial inequality $0 \le 0$ Assume then that $x _ { 2 } \neq 0$ Let $\lambda$ be an arbitrary complex number.We have from (8.1.1)(d),

$$
( x _ { 1 } + \lambda x _ { 2 } , x _ { 1 } + \lambda x _ { 2 } ) \geq 0 .
$$

This is equivalent to

$$
( x _ { 1 } , x _ { 1 } ) + \lambda ( x _ { 2 } , x _ { 1 } ) + \bar { \lambda } ( x _ { 1 } , x _ { 2 } ) + \lambda \bar { \lambda } ( x _ { 2 } , x _ { 2 } ) \geq 0 .
$$

This is true,in particular,for the number

$$
\lambda = - ( x _ { 1 } , x _ { 2 } ) / ( x _ { 2 } , x _ { 2 } ) .
$$

Hence,

$$
( x _ { 1 } , x _ { 1 } ) \ : - \ : \frac { ( x _ { 1 } , x _ { 2 } ) ( x _ { 2 } , x _ { 1 } ) } { ( x _ { 2 } , x _ { 2 } ) } - \frac { ( x _ { 1 } , x _ { 2 } ) ( x _ { 2 } , x _ { 1 } ) } { ( x _ { 2 } , x _ { 2 } ) }
$$

$$
+ \frac { ( x _ { 1 } , x _ { 2 } ) ( x _ { 2 } , x _ { 1 } ) } { ( x _ { 2 } , x _ { 2 } ) ^ { 2 } } \cdot ( x _ { 2 } , x _ { 2 } ) \geq 0 .
$$

Then,

$$
( x _ { 1 } , x _ { 1 } ) - { \frac { ( x _ { 1 } , x _ { 2 } ) ( x _ { 2 } , x _ { 1 } ) } { ( x _ { 2 } , x _ { 2 } ) } } \geq 0 .
$$

Therefore

or by (8.1.1) $( \mathbf { b } ^ { \prime } )$ ，

$$
\begin{array} { r l r } & { } & { ( x _ { 1 } , x _ { 2 } ) ( x _ { 2 } , x _ { 1 } ) \le ( x _ { 1 } , x _ { 1 } ) ( x _ { 2 } , x _ { 2 } ) , ~ } \\ & { } & { ~ | ( x _ { 1 } , x _ { 2 } ) | ^ { 2 } \le ( x _ { 1 } , x _ { 1 } ) ( x _ { 2 } , x _ { 2 } ) . ~ } \end{array}
$$

Suppose that equality holds. The case $x _ { 2 } = 0$ is trivial, so take $x _ { 2 } \neq 0$ By the above work we have

$$
\begin{array} { r l } & { x _ { 1 } + \lambda x _ { 2 } , x _ { 1 } + \lambda x _ { 2 } ) = 0 \quad \mathrm { w i t h } \quad \lambda = - ( x _ { 1 } , x _ { 2 } ) / ( x _ { 2 } , x _ { 2 } ) . } \\ & { } \\ & { { \mathrm { } } \mathrm { } \mathrm { } 8 . 1 . 1 ) ( \mathrm { d } ) , \quad x _ { 1 } + \lambda x _ { 2 } = 0 \quad \mathrm { a n d } \quad x _ { 1 } = \frac { ( x _ { 1 } , x _ { 2 } ) } { ( x _ { 2 } , x _ { 2 } ) } x _ { 2 } . } \end{array}
$$

Conversely if ${ \boldsymbol x } _ { 1 } = \alpha { \boldsymbol x } _ { 2 }$ ，then $| ( x _ { 1 } , x _ { 2 } ) | ^ { 2 } = | \alpha | ^ { 2 } ( x _ { 2 } , x _ { 2 } ) ^ { 2 } = ( x _ { 1 } , x _ { 1 } ) ( x _ { 2 } , x _ { 2 } ) .$

THEOREM 8.1.2．If $\pmb { X }$ is an inner product space,the equation

$$
\| x \| = { \sqrt { ( x , x ) } }
$$

defines a norm in $\pmb { X }$ ,and $\pmb { X }$ becomes a normed linear space.

Proof: The quantity $\sqrt { ( x , x ) }$ satisfies the requirements for a norm given in (7.2.1).The only requirement that is not immediately evident is the triangle inequality

$$
\| x + y \| \leq \| x \| + \| y \| .
$$

This is equivalent to

$$
\| x + y \| ^ { 2 } \leq \| x \| ^ { 2 } + 2 \| x \| \ \| y \| + \| y \| ^ { 2 }
$$

or

$$
( x + y , x + y ) \leq ( x , x ) + 2 { \sqrt { ( x , x ) } } { \sqrt { ( y , y ) } } + ( y , y ) .
$$

Since

$$
( x + y , x + y ) = ( x , x ) + ( y , x ) + ( x , y ) + ( y , y ) ,
$$

$$
\begin{array} { r } { ( x , y ) + ( y , x ) \le 2 \sqrt { ( x , x ) } \sqrt { ( y , y ) } . } \end{array}
$$

But

$$
| ( x , y ) + ( y , x ) | \leq | ( x , y ) | + | ( y , x ) | \leq 2 | ( x , y ) | .
$$

Hence,it sufices to show $| ( x , y ) | \leq { \sqrt { ( x , x ) } } { \sqrt { ( y , y ) } }$ .But this is precisely the Schwarz Inequality.

In view of Theorem 8.l.2,we can make every inner product space into a normed linear space in a natural and automatic way.

Ex.7.For $\ell ^ { 2 }$ ，the Schwarz inequality (8.1.2） coincides with the Holder inequality for infinite sequences. (Cf.(7.2.7) with $p = 2$ ）The triangle inequality (8.1.4) coincides with the Minkowski inequality (7.2.16).

Ex.8．A similar observation holds for $L ^ { 2 } [ a , b ]$

THEOREM 8.1.3 (The Paralllogram Theorem). For any elements $_ x$ and $_ y$ in an inner product space $\pmb { X }$ we have

$$
\| x + y \| ^ { 2 } + \| x - y \| ^ { 2 } = 2 \| x \| ^ { 2 } + 2 \| y \| ^ { 2 } .
$$

Proof: Replace the norms by inner products and expand.

8.2 Angle Geometry for Inner Product Spaces. For two nonzero elements in a real inner product space,we have,from (8.1.2),

$$
- 1 \leq { \frac { ( x _ { 1 } , x _ { 2 } ) } { \| x _ { 1 } \| \ \| x _ { 2 } \| } } \leq 1 .
$$

There is consequently a unique value of $\theta$ in the range $0 \leq \theta \leq \pi$ that   
satisfies cos $\theta = { \frac { ( x _ { 1 } , x _ { 2 } ) } { \| x _ { 1 } \| \ \| x _ { 2 } \| } }$

DEFINITION 8.2.1． The angle $\theta$ between elements $x _ { 1 } , \ x _ { 2 }$ in a real inner product space is defined by

$$
\cos \theta = { \frac { ( x _ { 1 } , x _ { 2 } ) } { \left\| x _ { 1 } \right\| \left\| x _ { 2 } \right\| } } \qquad 0 \leq \theta \leq \pi .
$$

The justification of this definition lies in the fact that it extends the usual formulas of Euclidean geometry.

Ex.1.Let $X \phantom { } = R _ { 3 }$ .For two elements $\boldsymbol { x } = ( x _ { 1 } , x _ { 2 } , x _ { 3 } )$ ， $\boldsymbol { y } = ( y _ { 1 } , y _ { 2 } , y _ { 3 } )$ ，use the inner product $( x , y ) = \sum _ { i = 1 } ^ { 3 } x _ { i } y _ { i }$ . This leads to the norm (or distance from the origin) $\| x \| ^ { 2 } = x _ { 1 } ^ { 2 } + x _ { 2 } ^ { 2 } + x _ { 3 } ^ { 2 }$ Then

$$
\cos \theta = { \frac { x _ { 1 } y _ { 1 } + x _ { 2 } y _ { 2 } + x _ { 3 } y _ { 3 } } { ( { x _ { 1 } } ^ { 2 } + { x _ { 2 } } ^ { 2 } + { x _ { 3 } } ^ { 2 } ) ^ { \frac { 1 } { 2 } } ( { y _ { 1 } } ^ { 2 } + { y _ { 2 } } ^ { 2 } + { y _ { 3 } } ^ { 2 } ) ^ { \frac { 1 } { 2 } } } } .
$$

This is familiar from analytic geometry.

In the case of a complex inner product space,the definition

$$
\cos \theta = { \frac { | ( x , y ) | } { \| x \| \ \| y \| } } \qquad 0 \leq \theta \leq \pi ,
$$

is frequently employed, though this is not completely satisfactory.(See Problem 13.)

Two special cases are particularly noteworthy.

A. $\theta = 0$ .In this case，cos $\theta = 1$ and $| ( x , y ) | = \| x \| \ \| y \|$ . According to Theorem 8.1.1,the elements $x _ { 1 }$ and $x _ { 2 }$ are dependent: $\alpha x _ { 1 } = \beta x _ { 2 }$ We may say that $x _ { 1 }$ and $x _ { 2 }$ are parallel.

B. $\theta = \pi / 2$ .In this case,the elements are perpendicular or orthogonal. Since cos $\theta = 0$ ， $| ( x , y ) | / \| x \| \ \| y \| = 0$ ，and this implies that $( x , y ) = 0$ . We sometimes write $x \perp y$ to express orthogonality and make the following definition.

DEFINITION 8.2.2. $x \perp y$ if and only if $( x , y ) = 0$

Ex.2. O is the only self orthogonal element.

Ex. 3. $x \perp y$ implies $y \perp x$

Ex. 4. $y \perp x _ { 1 } , x _ { 2 } , \ldots , x _ { n } { \mathrm { ~ i m p l i e s ~ } } y \perp a _ { 1 } x _ { 1 } + a _ { 2 } x _ { 2 } + \cdot \cdot \cdot + a _ { n } x _ { n } .$

Ex.5.Pythagoras' Theorem. $x \_ { \downarrow } \ y$ implies

$$
\| x + y \| ^ { 2 } = \| x \| ^ { 2 } + \| y \| ^ { 2 }
$$

Ex.6. The Law of Cosines. In a real inner product space,

$$
\| x + y \| ^ { 2 } = \| x \| ^ { 2 } + \| y \| ^ { 2 } + 2 \| x \| \| y \| \cos \theta .
$$

The inner product has a geometric interpretation as a projection. This is suggested by the accompanying two dimensional figure.

![](../chunks/Interpolation and Approximation (Philip J. Davis) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0141-0210/auto/images/66b3c5df84e0f135f138329d20fb1d0b5f97f977b11728a7788ec24dd02fcd78.jpg)  
Figure 8.2.1.

Let $x _ { 1 }$ and $x _ { 2 }$ be nonzero elements. Select a scalar $\lambda$ so that $\lambda x _ { \mathbf { 2 } }$ is the projection of $x _ { 1 }$ on $x _ { \mathbf { 2 } }$ Then

$$
\lambda x _ { 2 } \perp x _ { 1 } - \lambda x _ { 2 } .
$$

This means

$$
( \lambda x _ { 2 } , x _ { 1 } - \lambda x _ { 2 } ) = 0 .
$$

Therefore $\lambda ( x _ { 2 } , x _ { 1 } ) - \ \lambda \bar { \lambda } ( x _ { 2 } , x _ { 2 } ) = 0$ and $\lambda = { \frac { ( x _ { 1 } , x _ { 2 } ) } { ( x _ { 2 } , x _ { 2 } ) } }$ This means that if $x _ { 2 } \neq 0$ ，

This equation serves to define projection in the abstract case.

When the element ${ \pmb x } _ { \pmb { 2 } }$ has unit length : $\| x _ { 2 } \| ^ { 2 } = ( x _ { 2 } , x _ { 2 } ) = 1$ ,then

# 8.3 Orthonormal Systems

DEFINITION 8.3.1． A set $\pmb { S }$ of elements of an inner product space is called orthonormal if

$$
( x , y ) = { \left\{ \begin{array} { l l } { 0 } & { x \neq y } \\ { 1 } & { x = y } \end{array} \right. } x , y \in S .
$$

If we have merely

$$
( x , y ) = 0 \quad { \mathrm { f o r } } \quad x \neq y ,
$$

the set is called orthogonal.

Ex.1.In $\scriptstyle { R _ { n } }$ with $( x , y ) = \sum _ { i = 1 } ^ { n } x _ { i } y _ { i } ,$ the unit vectors

$$
( 1 , 0 , \ldots , 0 ) , ( 0 , 1 , 0 , \ldots , 0 ) , \ldots , ( 0 , 0 , \ldots , 1 )
$$

form an orthonormal set.

Ex.2.Let the $\textbf { \textit { n } } \times \textbf { \textit { n } }$ matrix $Q$ be orthogonal,i.e., $Q Q ^ { \prime } = I$ where $Q ^ { \prime }$ is the transpose of $Q$ and $\pmb { I }$ is the unit matrix.The rows (or columns) of $Q$ form an orthonormal set in the space of $\mathbf { E x }$ .1.

$\begin{array} { r } { \mathrm { E x . ~ 3 . ~ } \mathrm { ~ I n ~ } C [ - \pi , \pi ] \mathrm { ~ o r ~ } L ^ { 2 } [ - \pi , \pi ] \mathrm { , ~ w i t h ~ } ( f , g ) = \displaystyle \int _ { - \pi } ^ { \pi } f ( x ) g ( x ) d x , \mathsf { t o r } ( g ) \mathrm { , ~ } } \\ { ( 2 \pi ) ^ { - \frac { 1 } { 2 } } , \pi ^ { - \frac { 1 } { 2 } } \mathrm { ~ c o s ~ } x , \pi ^ { - \frac { 1 } { 2 } } \mathrm { ~ s i n ~ } x , \pi ^ { - \frac { 1 } { 2 } } \mathrm { ~ c o s ~ } 2 x , \pi ^ { - \frac { 1 } { 2 } } \mathrm { ~ s i n ~ } 2 x , . . . , \mathrm { ~ f o r m ~ } ( g ) \ge \mathbb { E } \equiv \mathbb { E } \equiv \mathbb { E } \equiv \mathbb { E } \equiv \mathbb { E } \equiv \mathbb { E } \equiv \mathbb { E } \equiv \mathbb { E } \equiv \mathbb { E } \equiv \mathbb { E } \equiv \mathbb { E } \equiv \mathbb { E } \equiv \mathbb { E } \equiv \mathbb { E } \equiv \mathbb { E } \mathbb { E } \equiv \mathbb { E } \equiv \mathbb { E } \mathbb { E } \equiv \mathbb { E } \mathbb { E } . } \end{array}$ che functions an orthonormal set.

Ex4 ,the polynomials $( \pi ) ^ { - \frac { 1 } { 2 } } T _ { 0 } ,$ $\left( { \frac { \pi } { 2 } } \right) ^ { - { \frac { 1 } { 2 } } } T _ { n } ( x ) , n = 1 , 2 , \ldots , T _ { n } ( x ) = \cos { ( n { \mathrm { ~ a r c ~ } } \cos x ) } ,$ form an orhororma set These are the Tschebyscheff Polynomials (cf. Def.3.3.1).

Ex.5.In ${ \bf \Pi } _ { 1 } \thinspace C [ - 1 , 1 ]$ or $L ^ { 2 } [ - 1 , 1 ]$ ，with $( f , g ) \ = \int _ { - 1 } ^ { + 1 } { \sqrt { 1 \ - { x ^ { 2 } } } } f ( x ) g ( x ) \ d x$ the functions set. For $U _ { m } ( x ) = { \frac { \sin \left[ ( m + 1 ) \operatorname { a r c } \cos x \right] } { \sqrt { 1 - x ^ { 2 } } } } m = 0 , 1 , 2 , . . . .$ , form an orthogonal

$$
\int _ { - 1 } ^ { 1 } { \sqrt { 1 - x ^ { 2 } } } \ U _ { m } ( x ) U _ { n } ( x ) d x \ = \int _ { 0 } ^ { \pi } \sin { ( m + 1 ) } \theta \sin { ( n + 1 ) } \theta d \theta \ = \ 0 \ , m \neq n .
$$

The functions ${ \sqrt { \frac { 2 } { \pi } } } \ U _ { n } ( x )$ are orthonormal Actually, $U _ { m } ( x )$ is a polynomial f degree $\mathbf { \nabla } m _ { \mathbf { \nabla } }$ in $[ - 1 , 1 ]$ ; for,cos $n \theta = T _ { n } ( \cos \theta )$ . Now

sin $( n + 1 ) \theta = \sin { n \theta }$ cos $\theta +$ cos nθ sin θ = sin nθ cos $\theta \ + \ T _ { n } ( \cos \theta )$ sin $\theta$

Hence,

$$
{ \frac { \sin { ( n + 1 ) \theta } } { \sin { \theta } } } = { \frac { \sin { n \theta } } { \sin { \theta } } } \cos { \theta } + T _ { n } ( \cos { \theta } ) .
$$

By induction,therefore, $\frac { \sin { ( n + 1 ) \theta } } { \sin { \theta } }$ is a polynomial of degree $_ n$ in cos 0. $U _ { m } ( x )$   
are the Tschebyscheff polynomials of the second kind.

$\operatorname { E x . ~ 6 . } \quad \operatorname { I n } { \mathcal { C } } [ a , b ] \operatorname { w i t h } ( f , g ) = \int _ { a } ^ { b } A ( x ) f ( x ) g ( x ) d x , ( A ( x ) \in C [ a , b ] \operatorname { a n d } \geq 0 ) , \cdots ,$ the eigenfunctions of the self-adjoint differential problem

$$
\begin{array} { l } { { \left\{ y ^ { \prime \prime } + \lambda A ( x ) y \right. = 0 } }  \\ { { \left. y ( a ) = y ( b ) = 0 \right. } } \end{array}
$$

corresponding to distinct eigenvalues are orthogonal.

Let $y _ { j }$ and $y _ { k }$ be two solutions of this problem corresponding to distinct values $\lambda _ { j } , \lambda _ { k }$ . Then

$$
\begin{array} { c } { { ( \lambda _ { k } - \lambda _ { j } ) A ( x ) y _ { k } ( x ) y _ { j } ( x ) = y _ { j } y _ { k } { } ^ { \prime } - y _ { k } y _ { j } { } ^ { \prime } = \displaystyle \frac { d } { d x } [ y _ { j } y _ { k } { } ^ { \prime } - y _ { k } y _ { j } { } ^ { \prime } ] . } } \\ { { { } } } \\ { { ( \lambda _ { k } - \lambda _ { j } ) { \displaystyle \int _ { a } ^ { b } } A ( x ) y _ { k } ( x ) y _ { j } ( x ) d x = [ y _ { j } y _ { k } { } ^ { \prime } - y _ { k } y _ { j } { } ^ { \prime } ] _ { a } ^ { b } = 0 . } } \end{array}
$$

THEOREM 8.3.1 (Pythagorean Theorem).If $x _ { 1 } , \ldots , x _ { n }$ are orthogonal then

$$
\| x _ { 1 } + x _ { 2 } + \cdot \cdot \cdot + x _ { n } \| ^ { 2 } = \| x _ { 1 } \| ^ { 2 } + \| x _ { 2 } \| ^ { 2 } + \cdot \cdot \cdot + \| x _ { n } \| ^ { 2 } .
$$

Proof: The cross terms in the expanded inner product vanish.

THEOREM 8.3.2. Any fnite set of nonzero orthogonal elements x1, xz..., ${ \pmb x } _ { \pmb n }$ is linearly independent.

Proof: Suppose $a _ { 1 } x _ { 1 } + a _ { 2 } x _ { 2 } + \cdot \cdot \cdot + a _ { n } x _ { n } = 0$ where the $^ { a }$ 's are not all 0. Then,

$$
0 = ( 0 , \pmb { x } _ { k } ) = ( a _ { 1 } \pmb { x } _ { 1 } + \cdot \cdot \cdot + a _ { n } \pmb { x } _ { n } , \pmb { x } _ { k } ) = a _ { k } ( x _ { k } , x _ { k } ) .
$$

This implies that $a _ { k } = 0 , k = 1 , 2 , \ldots , n$ , a contradiction.

The previous theorem has a partial converse which is of great importance.An independent set,of course,is not necessarily orthogonal, but it can be orthogonalized. That is,we can find linear combinations which are

orthogonal.From among the many proofs,we select one that leads to the Gram-Schmidt orthonormalizing process.

THEOREM 8.3.3． Let $x _ { 1 }$ ， $x _ { 2 } ,$ ...., be a finite or infinite sequence of elements such that any finite number of elements $x _ { 1 } , x _ { 2 } , \ldots , x _ { k }$ are linearly independent. Then,ue can find constants

$$
\begin{array} { r l } & { a _ { 1 1 } } \\ & { a _ { 2 1 } \quad a _ { 2 2 } } \\ & { a _ { 3 1 } \quad a _ { 3 2 } \quad a _ { 3 3 } } \\ & { . } \\ & { . } \\ & { . } \end{array}
$$

such that the elements

$$
\begin{array} { l } { { { x _ { 1 } } ^ { * } = a _ { 1 1 } x _ { 1 } } } \\ { { { x _ { 2 } } ^ { * } = a _ { 2 1 } x _ { 1 } + a _ { 2 2 } x _ { 2 } } } \\ { { { x _ { 3 } } ^ { * } = a _ { 3 1 } x _ { 1 } + a _ { 3 2 } x _ { 2 } + a _ { 3 3 } x _ { 3 } } } \\ { { . } } \\ { { . } } \\ { { . } } \\ { { . } } \end{array}
$$

are orthonormal:

$$
( x _ { i } { ^ { * } } , x _ { j } { ^ { * } } ) = \delta _ { i j } \qquad i , j = 1 , 2 , . . . .
$$

Proof: Set, recursively,

$$
\begin{array} { r l } & { y _ { 1 } = x _ { 1 } \mathrm { a n d } x _ { 1 } { ^ { * } } = y _ { 1 } / \| y _ { 1 } \| } \\ & { y _ { 2 } = x _ { 2 } - ( x _ { 2 } , x _ { 1 } { ^ { * } } ) { x _ { 1 } } ^ { * } \mathrm { a n d } x _ { 2 } { ^ { * } } = y _ { 2 } / \| y _ { 2 } \| } \\ & { . } \end{array}
$$

$$
\begin{array} { r l } & { y _ { n + 1 } = x _ { n + 1 } - \displaystyle \sum _ { k = 1 } ^ { n } ( x _ { n + 1 } , x _ { k } ^ { * } ) { x _ { k } ^ { * } } \quad \mathrm { a n d } \quad x _ { n + 1 } ^ { * } = y _ { n + 1 } / \| y _ { n + 1 } \| } \\ & { \quad . } \end{array}
$$

It is clear from the structure of this recursion that $y _ { n + 1 }$ ,and hence, ${ \pmb x } _ { { \pmb n } + 1 }$ is a linear combination of $x _ { 1 } , x _ { 2 } , \ldots , x _ { n + 1 }$ $\| y _ { i } \|$ cannot vanish inasmuch as this would imply that $y _ { i } = 0$ .But $y _ { i } = x _ { i } +$ "lower" $\pmb { x } _ { \mathbf { \lambda } } ^ { * } \mathbf { s }$ ，and this would contradict the assumption that the $_ x$ 's are independent.The ${ x _ { i } } ^ { * }$ are normal:

$$
( x _ { i } ^ { * } , x _ { i } ^ { * } ) = \left( { \frac { y _ { i } } { \| y _ { i } \| } } , { \frac { y _ { i } } { \| y _ { i } \| } } \right) = { \frac { 1 } { \| y _ { i } \| ^ { 2 } } } ( y _ { i } , y _ { i } ) = 1 .
$$

Finally we must prove that $x _ { n + 1 } ^ { * }$ (or $y _ { n + 1 } )$ is orthogonal to ${ x _ { n } } ^ { * } , { x _ { n - 1 } ^ { * } } , \ldots ,$ ${ \pmb x _ { 1 } } ^ { * }$ .A simple computation verifies that $( y _ { 2 } , x _ { 1 } ^ { * } ) = 0$ .Assume that for $\ i \leq n , j < i$ we have proved $( y _ { i } , x _ { j } ^ { * } ) = 0$ .Then for $j \leq n$ ，

$$
\begin{array} { l } { ( y _ { n + 1 } , x _ { j } { } ^ { * } ) = ( x _ { n + 1 } - \displaystyle \sum _ { k = 1 } ^ { n } ( x _ { n + 1 } , x _ { k } { } ^ { * } ) x _ { k } { } ^ { * } , x _ { j } { } ^ { * } ) } \\ { = ( x _ { n + 1 } , x _ { j } { } ^ { * } ) - \displaystyle \sum _ { k = 1 } ^ { n } ( x _ { n + 1 } , x _ { k } { } ^ { * } ) ( x _ { k } { } ^ { * } , x _ { j } { } ^ { * } ) } \\ { = ( x _ { n + 1 } , x _ { j } { } ^ { * } ) - ( x _ { n + 1 } , x _ { j } { } ^ { * } ) = 0 . } \end{array}
$$

COROLLARY 8.3.4. The "leading coefficients" $\pmb { a } _ { i i }$ are positive. For $a _ { i i } = ( \| y _ { i } \| ) ^ { - 1 }$

COROLLARY 8.3.5. We can find constants

with $b _ { i i } > 0$ such that

$$
\begin{array} { c } { { x _ { 1 } = b _ { 1 1 } x _ { 1 } { } ^ { * } } } \\ { { x _ { 2 } = b _ { 2 1 } x _ { 1 } { } ^ { * } + b _ { 2 2 } x _ { 2 } { } ^ { * } } } \\ { { . } } \\ { { . } } \end{array}
$$

$$
x _ { n } = b _ { n 1 } x _ { 1 } { * } + b _ { n 2 } x _ { 2 } { * } + \cdot \cdot \cdot + b _ { n n } x _ { n } { * }
$$

Proof:

$$
x _ { 1 } = \frac { 1 } { a _ { 1 1 } } { x _ { 1 } } ^ { * } \qquad \mathrm { s o ~ t h a t } ~ b _ { 1 1 } = \frac { 1 } { a _ { 1 1 } } .
$$

$$
\begin{array} { c } { { { \displaystyle x _ { 2 } = \frac { - a _ { 2 1 } } { a _ { 2 2 } } x _ { 1 } + \frac { 1 } { a _ { 2 2 } } { x _ { 2 } } ^ { * } } } } \\ { { { } } } \\ { { { } = - \frac { a _ { 2 1 } } { a _ { 2 2 } a _ { 1 1 } } { x _ { 1 } } ^ { * } + \frac { 1 } { a _ { 2 2 } } { x _ { 2 } } ^ { * } } } \end{array}
$$

so that

$$
b _ { \mathbf 2 \mathbf 1 } = \frac { - a _ { \mathbf 2 1 } } { a _ { \mathbf 2 2 } a _ { \mathbf 1 1 } } , \quad b _ { \mathbf 2 2 } = \frac { 1 } { a _ { \mathbf 2 2 } } .
$$

It is clear that we may proceed step by step in this way, since $a _ { j j } > 0$ ， j= 1,2,.... Note that $b _ { i i } = \frac { 1 } { a _ { i i } } = \| y _ { i } \| > 0$

COROLLARY 8.3.6. $x _ { n } { } ^ { * } \perp x _ { 1 } , x _ { n } { } ^ { * } \perp x _ { 2 } , . ~ . ~ . ~ , x _ { n } { } ^ { * } \perp x _ { n - 1 } .$

Proof: $x _ { k } = b _ { k 1 } x _ { 1 } { * } + b _ { k 2 } x _ { 2 } { * } + \cdot \cdot \cdot + b _ { k k } x _ { k } { * }$ so that

$$
( x _ { n } ^ { * } , x _ { k } ) = \left( x _ { n } ^ { * } , \sum _ { i = 1 } ^ { k } b _ { k i } x _ { i } ^ { * } \right) = \sum _ { i = 1 } ^ { k } b _ { k i } ( x _ { n } ^ { * } , x _ { i } ^ { * } ) = 0 \quad { \mathrm { i f } } \quad k < n .
$$

Note:In the subsequent portions of this book,we shall use the asterisk \* on symbols of elements to designate orthonormal elements,and on symbols of spaces to designate conjugate spaces.

The following observation should be made. If $x _ { 1 } , \ldots , x _ { n }$ and ${ \pmb x _ { 1 } } ^ { * } , \ldots , { \pmb x _ { n } } ^ { * }$ are related by (8.3.4),and we require that the latter are orthonormal and $a _ { k k } > 0 , k = 1 , 2 , . . . , n$ ，then the constants $\pmb { a } _ { i j }$ are determined uniquely. (Prove!) The Gram-Schmidt process is merely one scheme for determining them.

On the other hand,if we allow

$$
{ x _ { k } } ^ { * } = \alpha _ { k 1 } x _ { 1 } + \alpha _ { k 2 } x _ { 2 } + \cdot \cdot \cdot + \alpha _ { k n } x _ { n } , \qquad k = 1 , 2 , \ldots , n ,
$$

then there is much more freedom in the choice of the constants $\alpha _ { i j }$ .Whenever we speak of orthogonalizing a sequence of elements $x _ { 1 } , \ldots , x _ { n }$ the reader should decide whether the statements made hold for the triangular schenie (8.3.4) only,or whether they are valid for the more general scheme.

Ex.7. The powers $1 , x , x ^ { 2 } , \ldots$ , are independent in $C [ \boldsymbol { a } , \boldsymbol { b } ]$ .For,if

$$
a _ { \mathbf { 0 } } + a _ { \mathbf { 1 } } x + \cdots + a _ { n } x ^ { n } \equiv 0 , \qquad a \leq x \leq b ,
$$

then $a _ { i } = 0 , i = 0 , 1 , \dotsc , n$ If $w ( x )$ is a fixed positive, integrable function defined on $[ a , b ]$ then the integral

$$
( f , g ) \ = \int _ { a } ^ { b } w ( x ) f ( x ) g ( x ) \ d x
$$

forms an inner product in $C [ \boldsymbol { a } , \boldsymbol { b } ]$ . The powers may therefore be orthogonalized with respect to this inner product and we obtain a set of polynomials

$$
p _ { n } \sp { * } ( x ) = k _ { n } x \sp { n } + \cdot \cdot \cdot , \qquad n = 0 , 1 , 2 , \ldots , \qquad k _ { n } > 0
$$

which are orthonormal in the sense that

$$
\int _ { a } ^ { b } w ( x ) { p _ { m } } ^ { * } ( x ) { p _ { n } } ^ { * } ( x ) d x = \delta _ { m n } , \qquad m , n = 0 , 1 , \dots .
$$

In the case of a semi-infinite or an infinite interval $[ a , b ]$ ，we must assume that the weight factor ${ \pmb w } ( { \pmb x } )$ is such that the integrals $\int _ { a } ^ { b } w ( x ) x ^ { n } d x , n = 0 , 1 , \ldots ,$ all exist.

The following special selections of $[ a , b ]$ and $w ( x )$ have been studied extensively,and the resulting orthonormal polynomials constitute the“classical" orthonormal polynomials.

$$
\begin{array} { r l } & { \mathrm { 1 . ~ } a \mathrm { ~ = ~ - 1 ~ } b = 1 \quad w ( x ) = 1 } \\ & { \mathrm { 2 . ~ } a \mathrm { ~ = ~ - 1 ~ } b = 1 \quad w ( x ) = ( 1 - x ^ { 2 } ) ^ { - \frac { 1 } { 2 } } } \\ & { } \\ & { \mathrm { 3 . ~ } a \mathrm { ~ = ~ - 1 ~ } b = 1 \quad w ( x ) = ( 1 - x ^ { 2 } ) ^ { \frac { 1 } { 2 } } } \\ & { } \\ & { \mathrm { 4 . ~ } a \mathrm { ~ = ~ - 1 ~ } b = 1 \quad w ( x ) = ( 1 - x ) ^ { \alpha } ( 1 + x ) ^ { \beta } ; } \\ & { } \\ & { \mathrm { 5 . ~ } a \mathrm { ~ = ~ 0 ~ } b \mathrm { ~ = ~ \infty ~ } w ( x ) = x ^ { \alpha } e ^ { - \alpha } , \mathrm { ~ \alpha > ~ - 1 ~ } , } \\ & { \mathrm { 6 . ~ } a \mathrm { ~ = ~ - \infty ~ } b = \infty \quad w ( x ) = e ^ { - x ^ { 2 } } } \end{array}
$$

Legendre Polynomials Tschebyscheff Polynomials (of the First Kind) Tschebyscheff Polynomials of the Second Kind.

Jacobi Polynomials Laguerre Polynomials Hermite Polynomials

Ex.8. We compute the first 3 Legendre polynomials using the scheme of Theorem 8.3.3.

$$
x _ { 1 } = 1 , x _ { 2 } = t , x _ { 3 } = t ^ { 2 } \cdot y _ { 1 } = 1 \cdot \quad \| y _ { 1 } \| = \left( \int _ { - 1 } ^ { + 1 } d t \right) ^ { \frac { 1 } { 2 } } = { \sqrt { 2 } } .
$$

$$
x _ { 1 } \ l ^ { * } = { \frac { 1 } { \surd 2 } } \cdot \quad y _ { 2 } = t - \left( t , { \frac { 1 } { \surd 2 } } \right) { \frac { 1 } { \surd 2 } } \cdot \quad \left( t , { \frac { 1 } { \large \sqrt { 2 } } } \right) = { \frac { 1 } { \surd 2 } } \int _ { - 1 } ^ { + 1 } t d t = 0
$$

$$
y _ { 2 } = t . \quad \| y _ { 2 } \| = \biggl ( \int _ { - 1 } ^ { + 1 } t ^ { 2 } d t \biggr ) ^ { \frac { 1 } { 2 } } = \sqrt { \frac { 2 } { 3 } } \cdot \quad { x _ { 2 } } ^ { * } = \sqrt { \frac { 3 } { 2 } } t .
$$

$$
y _ { 3 } = t ^ { 2 } - \left( t ^ { 2 } , \sqrt { { \frac { 3 } { 2 } } } t \right) \sqrt { { \frac { 3 } { 2 } } } t - \left( t ^ { 2 } , { \frac { 1 } { \sqrt { 2 } } } \right) { \frac { 1 } { \sqrt { 2 } } } = t ^ { 2 } - { \frac { 1 } { 3 } } .
$$

$$
\| y _ { 3 } \| ~ = ~ \biggl ( \int _ { - 1 } ^ { + 1 } \biggl ( t ^ { 2 } ~ - { \frac { 1 } { 3 } } \biggr ) ^ { 2 } d t \biggr ) ^ { \frac { 1 } { 2 } } { } = ~ { \frac { 2 } { 1 5 } } ~ \sqrt { 1 0 } ~ x _ { 3 } { } ^ { * } ~ = ~ { \frac { 3 } { 4 } } ~ \sqrt { 1 0 } \biggl ( t ^ { 2 } ~ - { \frac { 1 } { 3 } } \biggr ) .
$$

Though the Gram-Schmidt process may be employed, the Legendre polynomials of higher degree are more expeditiously computed via recurrence. (See Chapter X.）

Ex.9.Let $a \leq x _ { 1 } < x _ { 2 } < \cdot \cdot \cdot < x _ { n + 1 } \leq b$ be $n + 1$ distinct points and $w _ { 1 } ,$ $w _ { \mathbf { 2 } } , \ldots , w _ { n + 1 }$ be $n + 1$ positive weights. The expression

$$
( f , g ) = \sum _ { i = 1 } ^ { n + 1 } w _ { i } f ( x _ { i } ) g ( x _ { i } )
$$

is an inner product for ${ \mathcal { P } } _ { n }$ (but not for ${ \mathcal { P } } _ { m } , m > n$ or for $C [ \boldsymbol { a } , \boldsymbol { b } ] )$ . We may therefore orthonormalize the powers and arrive at a set of polynomials

$$
{ p _ { 0 } } ^ { * } ( x ) , { p _ { 1 } } ^ { * } ( x ) , \ldots , { p _ { n } } ^ { * } ( x )
$$

for which

$$
\sum _ { k = 1 } ^ { n + 1 } w _ { k } { p _ { i } } ^ { * } ( x _ { k } ) p _ { j } ( x _ { k } ) \ : = \ : \delta _ { i j } \qquad 0 \leq i , j \leq n .
$$

These orthonormal polynomials are important in least square approximations on discrete sets of points.

Ex.10.Consider the situation of $\mathbf { E x }$ . 5 of 8.1. The complex powers ${ \bf 1 } , z ,$ $z ^ { 2 } , \ldots .$ ，are independent elements of $X$ .Hence,they may be orthonormalized with respect to the inner product $( f , g ) = \int _ { C } f ( z ) { \overline { { g ( z ) } } } d s$ to arrive at a set of polynomials ${ p _ { 0 } } ^ { * } ( z ) , { p _ { 1 } } ^ { * } ( z ) , . . . .$ ，for which

$$
\int _ { C } p _ { n } { } ^ { * } ( z ) \overline { { p _ { m } { } ^ { * } ( z ) } } d s = \delta _ { m n } \qquad 0 \leq m , n < \infty .
$$

# 8.4 Fourier (or Orthogonal) Expansions

DEFINITION 8.4.1．Let ${ x _ { 1 } } ^ { * } , { x _ { 2 } } ^ { * } , \ldots .$ ，be a finite or infinite sequence of orthonormal elements. Let $_ y$ be an arbitrary element. The series $\sum _ { n = 1 } ^ { \infty } ( y , x _ { n } { ^ * } ) x _ { n } { ^ * }$ ： is the Fourier series for $_ y$ .(If the sequence is finite we use a finite sum.) The constants $( y , x _ { n } ^ { * } )$ are known as the Fourier coefficients of $_ y$

One frequently writes

$$
y \sim \sum _ { n = 1 } ^ { \infty } ( y , x _ { n } { ^ * } ) x _ { n } { ^ * }
$$

to indicate that the right-hand sum is associated in a formal way with the left-hand side.The relation between an element and its Fourier series has been the object of vast investigations and theories.

In view of (8.2.4) we may write (8.4.1) in the form

$$
y \sim \sum _ { n = 1 } ^ { \infty } ( { \mathrm { P r o j e c t i o n ~ o f ~ } } y \ { \mathrm { ~ o n ~ } } x _ { n } { } ^ { * } )
$$

and hence the Fourier series of an element is merely the sum of the projections of the element on a system of orthonormal elements.

If $x _ { 1 } , x _ { 2 } , \ldots , \neq 0$ are orthogonal, but not necessarily normal, then

$$
{ x _ { k } } ^ { * } = { x _ { k } } / \| { x _ { k } } \| \qquad k = 1 , 2 , . . . ,
$$

are orthonormal so that (8.4.1） becomes

$$
y \sim \sum _ { n = 1 } ^ { \infty } \left( y , { \frac { x _ { k } } { \| x _ { k } \| } } \right) { \frac { x _ { k } } { \| x _ { k } \| } } = \sum _ { k = 1 } ^ { \infty } { \frac { ( y , x _ { k } ) } { ( x _ { k } , x _ { k } ) } } x _ { k } .
$$

Again, by (8.2.3) this may be interpreted as

$$
y \sim \sum _ { n = 1 } ^ { \infty } ( { \mathrm { P r o j e c t i o n ~ o f ~ } } y { \mathrm { ~ o n ~ } } x _ { n } ) .
$$

Ex.1.In $R _ { 3 }$ with $( x , y ) = \sum _ { i = 1 } ^ { 3 } x _ { i } y _ { i }$ select

$$
{ x _ { 1 } } ^ { * } = ( 1 , 0 , 0 ) , { x _ { 2 } } ^ { * } = ( 0 , 1 , 0 ) , { x _ { 3 } } ^ { * } = ( 0 , 0 , 1 ) .
$$

For a given $y = ( a , b , c )$ we have $( y , x _ { 1 } { ^ { * } } ) = a , ( y , x _ { 2 } { ^ { * } } ) = b , ( y , x _ { 3 } { ^ { * } } ) = c$ The summation $( a , b , c ) = a ( 1 , 0 , 0 ) + b ( 0 , 1 , 0 ) + c ( 0 , 0 , 1 )$ is the Fourier expansion of $_ y$

Ex. $\begin{array} { r l } & { 2 . \quad \mathrm { T a k e } C [ - \pi , \pi ] \mathrm { o r } L ^ { 2 } [ - \pi , \pi ] \mathrm { w i t h } ( f , g ) = \displaystyle \int _ { - \pi } ^ { \pi } f ( x ) g ( x ) d x . } \\ & { : ( 2 \pi ) ^ { - \frac { 1 } { 2 } } , ( \pi ) ^ { - \frac { 1 } { 2 } } \sin x , ( \pi ) ^ { - \frac { 1 } { 2 } } \cos x , ( \pi ) ^ { - \frac { 1 } { 2 } } \sin 2 x , \ldots . } \end{array}$ Orthonormal system

$$
\begin{array} { r } { \mathrm {  ~ \psi ~ } ^ { { \scriptscriptstyle : } \{ } \{ } \alpha \pi \} \mathrm {  ~ \psi ~ } ^  { \scriptscriptstyle < } \mathrm {  ~ \nu ~ } \mathrm {  ~ \ s u n } \mathrm {  ~ \psi ~ } \mathrm {  ~ } \alpha , \varpi \mathrm {  ~ \psi ~ } \mathrm {  ~ \psi ~ } \mathrm {  ~ \psi ~ } ^ { \scriptscriptstyle : } \mathrm {  ~ \psi ~ } \mathrm {  ~ \psi ~ } ^ { \scriptscriptstyle : } \mathrm {  ~ \psi ~ } \mathrm {  ~ \psi ~ } ^ { \scriptscriptstyle } \mathrm {  ~ \psi ~ } \mathrm {  ~ \psi ~ } \mathrm {  ~ \psi ~ } ^ { \scriptscriptstyle } \mathrm {  ~ \psi ~ } \mathrm {  ~ \psi ~ } \mathrm {  ~ \psi ~ } ^ { \scriptscriptstyle } \mathrm {  ~ \psi ~ } \mathrm {  ~ \psi ~ } \mathrm {  ~ \psi ~ } \mathrm {  ~ \psi ~ } \mathrm {  ~ \psi ~ } \mathrm {  ~ \psi ~ } \mathrm {  ~ \psi ~ } \mathrm {  ~ \psi ~ } \mathrm {  ~ \psi ~ } \mathrm {  ~ \psi ~ } \mathrm {  ~ \psi ~ } \mathrm {  ~ \psi ~ } \mathrm {  ~ \psi ~ } \mathrm {  ~ \psi ~ } \mathrm {  ~ \psi ~ } \mathrm {  ~ \psi ~ } \mathrm {  ~ \psi ~ } \mathrm {  ~ \psi ~ } \mathrm {  ~ \psi ~ } \mathrm {  ~ \psi ~ } \mathrm {  ~ \psi ~ } \mathrm {  ~ \psi ~ } \mathrm {  ~ \psi ~ } \mathrm {  ~ \psi ~ } \mathrm {  ~ \psi ~ } \mathrm {  ~ \psi ~ } \mathrm {  ~ \psi ~ } \mathrm {  ~ \psi ~ } \mathrm {  ~ \psi ~ } \mathrm {  ~ \psi ~ } \mathrm {  ~ \psi ~ } \mathrm {  ~ \psi ~ } \mathrm {  ~ \psi ~ } \mathrm {  ~ \psi ~ } \mathrm {  ~ \psi ~ } \mathrm {  ~ \psi ~ } \mathrm {  ~ \psi ~ } \mathrm {  ~ \psi ~ } \mathrm {  ~ \psi ~ } \mathrm {  ~ \psi ~ } \mathrm {  ~ \psi ~ } \mathrm {  ~ \psi ~ } \mathrm {  ~ \psi ~ } \mathrm {  ~ \psi ~ } \mathrm {  ~ \psi ~ } \mathrm {  ~ \psi ~ } \mathrm {  ~ \psi ~ } \mathrm {  ~ \psi ~ } \mathrm {  ~ \psi ~ } \mathrm {  ~ \psi ~ } \mathrm {  ~ \psi ~ } \mathrm {  ~ \psi ~ } \mathrm {  ~ \psi ~ } \mathrm   ~ \end{array}
$$

This is the Fourier Series.

${ \bf E x . 3 . } \quad { \cal C } [ - 1 , 1 ] . \ ( f , g ) \ = \int _ { - 1 } ^ { 1 } { \frac { f ( x ) g ( x ) d x } { \sqrt { 1 - x ^ { 2 } } } }$ . Orthonormal system

$$
( \pi ) ^ { - \frac { 1 } { 2 } } T _ { 0 } ( x ) , \left( \frac { \pi } { 2 } \right) ^ { - \frac { 1 } { 2 } } T _ { 1 } ( x ) , \left( \frac { \pi } { 2 } \right) ^ { - \frac { 1 } { 2 } } T _ { 2 } ( x ) , \ldots ,
$$

$$
f ( x ) \sim \frac { a _ { 0 } } { 2 } + \sum _ { k = 1 } ^ { \infty } a _ { k } T _ { k } ( x ) , \quad a _ { k } = \frac { 2 } { \pi } \int _ { - 1 } ^ { + 1 } \frac { f ( x ) T _ { k } ( x ) d x } { \sqrt { 1 - x ^ { 2 } } } .
$$

This is the Tschebyscheff-Fourier Series.

In the simple case of finite dimensional spaces,the Fourier expansion of an element coincides with the element.More precisely,the following theorem holds.

THEOREM 8.4.1． Let $x _ { 1 } , \ldots , x _ { n }$ be independent and let ${ x _ { i } } ^ { * }$ be the x's orthonormalized.If $w = a _ { 1 } x _ { 1 } + \cdot \cdot \cdot + a _ { n } x _ { n }$ then

$$
w = \sum _ { k = 1 } ^ { n } ( w , x _ { k } * ) x _ { k } { } ^ { * } .
$$

Proof: From Corollary 8.3.5, we have,

$$
\begin{array} { l } { w = a _ { 1 } ( b _ { 1 1 } x _ { 1 } { * } ) + a _ { 2 } ( b _ { 2 1 } x _ { 1 } { * } + b _ { 2 2 } x _ { 2 } { * } ) + \cdot \cdot \cdot + a _ { n } ( b _ { n 1 } x _ { 1 } { * } + \cdot \cdot \cdot + b _ { n n } x _ { n } { * } ) } \\ { \quad = c _ { 1 } x _ { 1 } { * } + c _ { 2 } x _ { 2 } { * } + \cdot \cdot \cdot + c _ { n } x _ { n } { * } . } \end{array}
$$

Now, for $1 \leq k \leq n$

$$
\begin{array} { l } { ( w , x _ { k } ^ { * } ) = ( c _ { 1 } x _ { 1 } ^ { * } + \cdot \cdot \cdot + c _ { n } x _ { n } ^ { * } , x _ { k } ^ { * } ) } \\ { \qquad = c _ { 1 } ( x _ { 1 } ^ { * } , x _ { k } ^ { * } ) + \cdot \cdot \cdot + c _ { k } ( x _ { k } ^ { * } , x _ { k } ^ { * } ) + \cdot \cdot \cdot + c _ { n } ( x _ { n } ^ { * } , x _ { k } ^ { * } ) = c _ { k } , } \end{array}
$$

and (8.4.8) follows.

Ex. 4.If ${ p _ { n } } ^ { * } ( x ) = \sum _ { j = 0 } ^ { n } k _ { n j } x ^ { j } , k _ { n n } \ne 0$ ,are polynomials that are orthonormal with respect to the inner product $( f , g )$ then

$$
p ( x ) = \sum _ { k = 0 } ^ { n } ( p , { p _ { k } } ^ { * } ) { p _ { k } } ^ { * } ( x )
$$

for all $\boldsymbol { p } \in \mathcal { P } _ { n }$

Ex.5.Let $x _ { 1 } , \ldots , x _ { n } \mid \neq 0 )$ be an orthogonal set in $\scriptstyle { R _ { n } }$ or $C _ { n }$ . Any element in the space is equal to the sum of its projections on $x _ { 1 } , \ldots , x _ { n }$

8.5 Minimum Properties of Fourier Expansions. Truncated Fourier expansions have the following minimum property.

THEOREM 8.5.1． Let ${ x _ { 1 } } ^ { * } , { x _ { 2 } } ^ { * }$ ，...， be an orthonormal system and let $_ y$ be arbitrary. Then,

$$
\left\| y - \sum _ { i = 1 } ^ { N } ( y , { x _ { i } } ^ { * } ) { x _ { i } } ^ { * } \right\| \leq \left\| y - \sum _ { i = 1 } ^ { N } a _ { i } { x _ { i } } ^ { * } \right\|
$$

for any selectionof constants ${ \pmb a } _ { 1 } , { \pmb a } _ { 2 } , \dots , { \pmb a } _ { N }$

$$
\begin{array} { r l } & { \bigg \vert y - \displaystyle \sum _ { i = 1 } ^ { N } a _ { i } x _ { i } ^ { * } \bigg \vert ^ { 2 } = \bigg ( y - \displaystyle \sum _ { i = 1 } ^ { N } a _ { i } x _ { i } ^ { * } , y ) - \displaystyle \sum _ { i = 1 } ^ { N } a _ { i } x _ { i } ^ { * } \bigg ) } \\ & { \qquad = ( y , y ) - \displaystyle \sum _ { i = 1 } ^ { N } a _ { i } ( x _ { i } ^ { * } , y ) - \displaystyle \sum _ { i = 1 } ^ { N } a _ { i } ( y , x _ { i } ^ { * } ) + \displaystyle \sum _ { i , j = 1 } ^ { N } a _ { i } \tilde { a } _ { j } ( x _ { i } ^ { * } , x _ { j } ^ { * } ) } \\ & { \qquad = ( y , y ) - \displaystyle \sum _ { i = 1 } ^ { N } a _ { i } ( x _ { i } ^ { * } , y ) - \displaystyle \sum _ { i = 1 } ^ { N } \tilde { a } _ { i } ( y , x _ { i } ^ { * } ) + \displaystyle \sum _ { i = 1 } ^ { N } \vert a _ { i } \vert ^ { 2 } } \\ & { \qquad \quad + \displaystyle \sum _ { i = 1 } ^ { N } ( x _ { i } ^ { * } , y ) ( y , x _ { i } ^ { * } ) - \displaystyle \sum _ { i = 1 } ^ { N } ( x _ { i } ^ { * } , y ) ( y , x _ { i } ^ { * } ) } \\ & { \qquad = ( y , y ) - \displaystyle \sum _ { i = 1 } ^ { N } \vert ( y , x _ { i } ^ { * } ) \vert ^ { 2 } + \displaystyle \sum _ { i = 1 } ^ { N } \vert a _ { i } - ( y , x _ { i } ^ { * } ) \vert ^ { 2 } . } \end{array}
$$

Since the first two terms of the last member are independent of the $^ { \pmb { a } }$ 's,it is clear that the minimum of $\|  y - \sum _ { i = 1 } ^ { N } a _ { i } x _ { i } { } ^ { * } \| ^ { 2 }$ is achieved when and only when

$$
\begin{array} { r } { \pmb { a _ { i } } = ( y , x _ { i } ^ { * } ) \qquad i = 1 , 2 , \dots , N ; } \end{array}
$$

i.e., when the $^ { \pmb { a } }$ 's are the Fourier coefficients of $_ y$

Least square problems of numerical analysis can be formulated in terms of finding $\operatorname* { m i n } _ { \pmb { a } _ { i } } \left\| \pmb { y } - \sum _ { i = 1 } ^ { N } \pmb { a } _ { i } \pmb { x } _ { i } \right\|$ in an appropriate inner product space. (Cf., e.g.,Ex.3.) The next corollary gives the solution to such problems.

COROLLARY 8.5.2. Let $x _ { 1 } , \ldots , x _ { S }$ be an independent set of elements. The problem of finding that linear combination of $x _ { 1 } , \ldots , x _ { N }$ which minimizes

$$
\left\| { \boldsymbol { y } } - \sum _ { i = 1 } ^ { N } a _ { i } x _ { i } \right\| i s ~ s o l v e d ~ b { \boldsymbol { y } } \sum _ { i = 1 } ^ { N } ( { \boldsymbol { y } } , { \boldsymbol { x } } _ { i } ^ { * } ) { \boldsymbol { x } } _ { i } ^ { * } .
$$

The ${ \boldsymbol { x } _ { i } } ^ { * }$ 's are orthonormalized $_ x$ 's.The solution is unique.This tells us that every least square problem is solved by an appropriate truncated Fourier series.

$$
\displaystyle { \mathrm { ' } } 8 . 5 . 3 . \quad \operatorname* { m i n } _ { a _ { \iota } } \left\| y - \sum _ { i = 1 } ^ { N } a _ { \iota } \boldsymbol { x } _ { \iota } \right\| ^ { 2 } = \| y \| ^ { 2 } - \sum _ { i = 1 } ^ { N } | ( y , x _ { \iota } ^ { \ast } ) | ^ { 2 } .
$$

Proof: Insert $\boldsymbol { a } _ { \iota } = ( y , x _ { \iota } ^ { * } )$ in the last equality of the proof of Theorem 8.5.1.

Since this minimum value is $\geq 0$ we have

CoROLLARY 8.5.4 (Bessel Inequality).1f ${ \boldsymbol { x } _ { i } } ^ { * }$ are orthonormal, then

$$
\sum _ { i = 1 } ^ { N } | ( y , x _ { i } ^ { * } ) | ^ { 2 } \leq \| y \| ^ { 2 } .
$$

COROLLARY 8.5.5．If ${ \boldsymbol { x } _ { i } } ^ { * }$ are an infinite sequence of orthonormal elements then

$$
\sum _ { i = 1 } ^ { \infty } | ( y , x _ { i } ^ { \ast } ) | ^ { 2 } \leq \| y \| ^ { 2 } .
$$

COROLLARY 8.5.6. If ${ \boldsymbol { x } _ { i } } ^ { * }$ are an infinite sequence of orthonormal elements then

$$
\operatorname* { l i m } _ { i  \infty } ( y , x _ { \imath } ^ { \ast } ) = 0
$$

i.e., the Fourier coefficients of any element approach zero.

CoROLLARY 8.5.7 (Minimum Property of Orthogonal Elements).Let $x _ { 1 }$ ， $x _ { 2 } , \ldots , x _ { n }$ be independent. Let ${ x _ { 1 } } ^ { * } , { x _ { 2 } } ^ { * }$ ${ x _ { n } } ^ { * }$ be the $x _ { k }$ s orthonormalized according to the triangular scheme of Theorem 8.3.3.Then,for all selections of constants $a _ { 1 } , \ldots , a _ { n - 1 }$ ， we have

$$
\| y _ { n } \| = \left\| { \frac { { x _ { n } } ^ { * } } { a _ { n n } } } \right\| \leq \| a _ { 1 } x _ { 1 } + a _ { 2 } x _ { 2 } + \cdot \cdot \cdot + a _ { n - 1 } x _ { n - 1 } + x _ { n } \| .
$$

The notation of (8.3.6) is employed.

Proof:By Corollary 8.5.2,the problem

$$
\begin{array} { c } { { \mathrm { m i n ~ } \| x _ { n } - ( b _ { 1 } x _ { 1 } + \cdot \cdot \cdot + b _ { n - 1 } x _ { n - 1 } ) \| } } \\ { { b _ { i } } } \\ { { , x _ { k } ^ { * } ) x _ { k } ^ { * } . \ \mathrm { B u t ~ f r o m ~ } ( 8 . 3 . 6 ) \ \mathrm { t h i s ~ i s ~ p r e c i s } } } \end{array}
$$

is solved by $\sum _ { i = 1 } ^ { n - 1 } ( x _ { n } , x _ { k } { ^ \ast } ) x _ { k } { ^ \ast }$ sely $x _ { n } \mathrm { ~ - ~ } y _ { n }$ 1

Least square approximations (i.e.,best approximations in an inner product space) of an element $_ y$ by a combination of given independent elements $x _ { 1 } , x _ { 2 } , \ldots , x _ { n }$ can be expressed in several ways:(l) as a linear combination $a _ { 1 } x _ { 1 } + \cdots + a _ { n } x _ { n }$ of the given elements,(2）as a linear conibination $b _ { 1 } x _ { 1 } { * } + \dotsb + b _ { n } x _ { n } { * }$ of the orthonormalized $_ { x }$ 's.Although (l) may be more convenient, (2) possesses the advantage of permanance. That is to say, suppose we add an additional element $x _ { n + 1 }$ to our list and ask for best approximations to $_ y$ by linear combinations of $x _ { 1 } , \ldots , x _ { n } , x _ { n + 1 }$ Expressed in form (1),the answer will be some $a _ { 1 } { ' } x _ { 1 } + \cdot \cdot \cdot + a _ { n } { ' } x _ { n } + a _ { n + 1 } ^ { \prime } x _ { n + 1 }$ where the ${ a _ { k } } ^ { \prime }$ 's may bear no simple relation to the $a _ { k }$ .Expressed in form (2),the answer retains the frst $\pmb { n }$ coefficients and merely adds one more:

$$
b _ { 1 } x _ { 1 } { * } + b _ { 2 } x _ { 2 } { * } + \dotsb + b _ { n } x _ { n } { * } + b _ { n + 1 } x _ { n + 1 } ^ { * } .
$$

Ex.1.If $f \in C [ - \pi , \pi ]$ or even of $L ^ { 2 } [ - \pi , \pi ]$ ,then

$$
\operatorname* { l i m } _ { n \to \infty } \int _ { - \pi } ^ { \pi } f ( x ) \sin n x d x = \operatorname* { l i m } _ { n \to \infty } \int _ { - \pi } ^ { \pi } f ( x ) \cos n x d x = 0 .
$$

This is Riemann's Theorem and is a consequence of Corollary 8.5.5.It holds under more general circumstances than demonstrated here.

Ex. 2. Let ${ { p } _ { n } } ^ { * } ( x )$ be the Legendre polynomials. If

$$
f \in C [ - 1 , 1 ] \quad { \mathrm { t h e n } } \operatorname* { l i m } _ { n \to \infty } \int _ { - 1 } ^ { + 1 } f ( x ) p _ { n } { } ^ { * } ( x ) d x = 0 .
$$

Ex.3.If $\cdot f \in L ^ { 2 } [ a , b ]$ ,the problem of finding

$$
\operatorname* { m i n } _ { a _ { \imath } } \int _ { a } ^ { b } \left( f ( x ) { \bf \Phi } - \sum _ { i = 0 } ^ { n } a _ { i } x ^ { i } \right) ^ { 2 } d x
$$

has a unique solution.

Ex.4．Solve the problem

$$
\operatorname* { m i n } _ { a _ { 1 } } \int _ { - 1 } ^ { + 1 } ( e ^ { x } - a _ { 0 } - a _ { 1 } x - a _ { 2 } x ^ { 2 } ) ^ { 2 } d x .
$$

Use the Legendre polynomials

$$
x _ { 1 } { ^ \ast } = \sqrt { { \textstyle { \frac { 1 } { 2 } } } } , x _ { 2 } { ^ \ast } = \sqrt { { \textstyle { \frac { 3 } { 2 } } } } x , x _ { 3 } { ^ \ast } = { \textstyle { \frac { 3 } { 4 } } } \sqrt { 1 0 } ( x ^ { 2 } - { \textstyle { \frac { 1 } { 3 } } } ) .
$$

The Fourier coefficients of $e ^ { \pmb { x } }$ are

$$
\begin{array} { l } { { b _ { 0 } = \displaystyle { \int _ { - 1 } ^ { + 1 } } \sqrt { \frac { 1 } { 2 } } e ^ { x } d x ~ = ~ \sqrt { \frac { 1 } { 2 } } ( e ^ { \mathbf { \Theta } } - e ^ { - 1 } ) , } } \\ { { b _ { 1 } = \displaystyle { \int _ { - 1 } ^ { + 1 } } \sqrt { \frac { 3 } { 2 } } x e ^ { x } d x ~ = ~ \sqrt { \frac { 3 } { 2 } } ( 2 e ^ { - 1 } ) , } } \\ { { b _ { 2 } = \displaystyle { \int _ { - 1 } ^ { + 1 } } \frac { 3 } { 4 } \sqrt { \overline { { 1 0 } } } ( x ^ { 2 } ~ - \frac { 1 } { 3 } ) e ^ { x } d x ~ = \displaystyle { \frac { 3 \sqrt { 1 0 } } { 4 } } \left( \frac { 2 e ^ { \mathbf { \Theta } } - 1 4 e ^ { - 1 } } { 3 } \right) } } \end{array}
$$

The minimizing polynomial is therefore

$$
{ \begin{array} { r l } & { p ( x ) = { \frac { 1 } { 2 } } ( e - e ^ { - 1 } ) + 3 e ^ { - 1 } x + { \frac { 9 0 } { 1 6 } } { \bigg ( } { \frac { 2 e - 1 4 e ^ { - 1 } } { 3 } } { \bigg ) } ( x ^ { 2 } - { \frac { 1 } { 3 } } ) } \\ & { \qquad = { \frac { 1 5 } { 4 } } ( e - 7 e ^ { - 1 } ) x ^ { 2 } + 3 e ^ { - 1 } x + { \frac { 3 3 } { 4 } } e ^ { - 1 } - { \frac { 3 } { 4 } } e . } \\ & { \qquad \approx . 5 3 7 x ^ { 2 } + 1 . 1 0 4 x + . 9 9 6 . } \end{array} }
$$

![](../chunks/Interpolation and Approximation (Philip J. Davis) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0141-0210/auto/images/12e8c39025531ceed05a195f31f63ed7be163d958d7933efee4b751d12e1b51d.jpg)  
Figure 8.5.1 Error in Least Square Approximation of $e ^ { x }$ by a Parabola.

Ex.5. Let $p _ { n } ( x ) = k _ { n n } x ^ { n } + \cdot \cdot \cdot$ be the Legendre polynomials. Then,

$$
\int _ { - 1 } ^ { + 1 } \left( { \frac { p _ { n } ( x ) } { k _ { n n } } } \right) ^ { 2 } d x = { \frac { 2 ^ { 2 n + 1 } ( n ! ) ^ { 4 } } { ( 2 n ) ! ( 2 n + 1 ) ! } } \leq \int _ { - 1 } ^ { + 1 } ( x ^ { n } + a _ { 1 } x ^ { n - 1 } + \cdot \cdot \cdot + a _ { n } ) ^ { 2 } d x
$$

for all selections of $^ { a }$ s. (Use Theorem 10.3.5 and Theorem 10.3.4 for the equality.)

Ex.6.Let $T _ { n } ( x ) = 2 ^ { n - 1 } x ^ { n } + \cdot \cdot \cdot$ be the Tschebyscheff polynomial of the first kind. Then,

$$
{ \frac { 1 } { 2 ^ { 2 n - 2 } } } \int _ { - 1 } ^ { + 1 } { \frac { ( T _ { n } ( x ) ) ^ { 2 } } { \sqrt { 1 - x ^ { 2 } } } } d x = { \frac { \pi } { 2 ^ { 2 n - 1 } } } \leq \int _ { - 1 } ^ { + 1 } { \frac { ( x ^ { n } + a _ { 1 } x ^ { n - 1 } + \cdot \cdot \cdot + a _ { n } ) ^ { 2 } } { \sqrt { 1 - x ^ { 2 } } } } d x
$$

for all selections of $^ { a }$ s.Here $\textbf { \em n } \geq \textbf { 1 }$

Ex.7．Lanczos Economization.

If $\frac { a _ { 0 } } { 2 } + \sum _ { k = 1 } ^ { \infty } a _ { k } T _ { k } ( x )$ is the Tschebyschef-Fourier series of a continuous $f ( x )$ (cf.84.7)e $\frac { a _ { 0 } } { 2 } + \sum _ { k = 1 } ^ { n } a _ { k } T _ { k } ( x )$ solves the problem of finding $\operatorname* { m i n } _ { b _ { i } } \int _ { - 1 } ^ { + 1 } \left( f ( x ) - \sum _ { k = 0 } ^ { n } b _ { k } x ^ { k } \right) ^ { 2 } ( 1 - x ^ { 2 } ) ^ { - \frac { 1 } { 2 } } \mathop { d x } .$ But this partial sum is very nearly the

solution to the problem $\operatorname* { m i n } _ { b _ { i } } \operatorname* { m a x } _ { - 1 \leq x \leq 1 } { \left| f ( x ) - \sum _ { k = 0 } ^ { n } b _ { k } x ^ { k } \right| } .$ For suppose that we write $f ( x ) = { \frac { - \Re } { \mathrm { \Large ~ * ~ } } } + a _ { 1 } T _ { 1 } ( x ) ~ + ~ \cdot ~ \cdot ~ + ~ a _ { n } T _ { n } ( x ) ~ + ~ a _ { n + 1 } T _ { n + 1 } ( x )$ a plus a remainder which 2   
we neglect. Then, $f ( x ) \ - \ \left( { \frac { a _ { 0 } } { 2 } } + a _ { 1 } T _ { 1 } ( x ) \ + \ \cdot \ \cdot \ + \ a _ { n } T _ { n } ( x ) \right) = a _ { n + 1 } T _ { n + 1 } ( x )$ Since $a _ { n + 1 } T _ { n + 1 } ( x )$ has $\textit { \textbf { n } + 2 }$ equal maxima and minima alternating in sign,Theorem 7.6.4 tells us that the contents of the parenthesis is the best uniform approximation to $f ( x )$ from $\mathcal { P } _ { n }$ .For this reason，the partial Tschebyscheff-Fourier series are sometimes used as a starting point in determining best uniform approximations.

If $f$ isa polynomial,its Tschebyscheff-Fourier expansion can be obtained by using the table,given in the Appendix,of powers as combinations of Tschebyscheff polynomials.

Ex. 7A. Economize $f ( x ) = 1 + { \frac { x } { 2 } } + { \frac { x ^ { 2 } } { 3 } } + { \frac { x ^ { 3 } } { 4 } } + { \frac { x ^ { 4 } } { 5 } } + { \frac { x ^ { 5 } } { 6 } }$ on the interval $[ - 1 , 1 ]$ allowing a tolerance of $\varepsilon \ = \ . 0 5$ We have,

$$
{ \begin{array} { r l } & { f ( x ) \ = \ T _ { 0 } \ + \ { \frac { 1 } { 2 } } T _ { 1 } \ + \ { \frac { 1 } { 3 } } \cdot { \frac { 1 } { 2 } } ( T _ { 0 } \ + \ T _ { 1 } ) \ + \ { \frac { 1 } { 4 } } \cdot { \frac { 1 } { 4 } } ( 3 T _ { 1 } \ + \ T _ { 3 } ) } \\ & { \qquad + \ { \frac { 1 } { 5 } } \cdot { \frac { 1 } { 8 } } ( 3 T _ { 0 } \ + \ 4 T _ { 2 } \ + \ T _ { 4 } ) \ + \ { \frac { 1 } { 6 } } \cdot { \frac { 1 } { 1 6 } } ( 1 0 T _ { 1 } \ + \ 5 T _ { 3 } \ + \ T _ { 5 } ) } \\ & { \qquad = { \frac { 1 4 9 } { 1 2 0 } } T _ { 0 } \ + \ { \frac { 7 } { 8 } } 6 T _ { 1 } \ + \ { \frac { 3 2 } { 1 2 0 } } T _ { 2 } \ + \ { \frac { 1 1 } { 9 6 } } T _ { 3 } \ + \ { \frac { 3 } { 1 2 0 } } T _ { 4 } \ + \ { \frac { 1 } { 9 6 } } T _ { 5 } . } \end{array} }
$$

Since $\left| T _ { n } ( x ) \right| = \left| \cos { ( n \operatorname { a r c } \cos { x } ) } \right| \le 1$ ，we can delete the last two terms and we incur an error of at most $\frac { 3 } { 1 } \frac { } { 2 } \overline { { \mathbf { 0 } } } \ + \ \frac { 1 } { 9 8 } < . 0 5$ Hence

$$
\begin{array} { r } { \frac { 1 } { 1 } \frac { 4 } { 2 } \frac { 9 } { 0 } T _ { 0 } \ + \ \frac { 7 } { 9 } \frac { 6 } { 6 } T _ { 1 } \ + \ \frac { 3 2 } { 1 2 0 } T _ { 2 } \ + \ \frac { 1 1 } { 9 } \frac { 1 } { 6 } T _ { 3 } } \end{array}
$$

is in $\mathcal { P } _ { 3 }$ and approximates $f ( x )$ to within $. 0 5 \mathrm { ~ o n ~ } [ - 1 , 1 ] .$

Ex. 7B. The Tschebyscheff-Fourier coeffcients of cos $\frac { \pi x } { 2 }$ are

$$
{ \begin{array} { r l } & { { \cfrac { 1 } { \pi } } \displaystyle \int _ { - 1 } ^ { + 1 } { \frac { \cos { \frac { \pi x } { 2 } } \cos { ( n \arg x ) } } { \sqrt { 1 - x ^ { 2 } } } } d x } \\ & { \qquad = { \cfrac { 1 } { \pi } } \displaystyle \int _ { 0 } ^ { \pi } \cos \left( { \frac { \pi } { 2 } } \cos { y } \right) \cos { n y } d y \ = \left\{ { \begin{array} { l l } { ( - 1 ) ^ { k } 2 J _ { 2 k } ( \pi / 2 ) } & { \quad n = 2 k } \\ { 0 } & { \quad n = 2 k + 1 } \end{array} } \right. } \end{array} }
$$

where $J _ { n } ( x )$ is the Bessel Function of order $\pmb { n }$ .(See,for instance,G.N.Watson [1] p. 21.) Hence, $\cos { \frac { \pi x } { 2 } } \sim J _ { 0 } ( \pi / 2 ) - 2 J _ { 2 } ( \pi / 2 ) T _ { 2 } ( x ) + 2 J _ { 4 } ( \pi / 2 ) T _ { 4 } ( x ) - \cdot \cdot \cdot .$ The partial sum of order 4i $\textrm { s } = 0 . 9 9 9 3 9 6 6 \ - 1 . 2 2 2 7 4 3 2 x ^ { 2 } \ + \ 0 . 2 2 3 9 3 6 6 x ^ { 4 }$ ,and this may be compared with the best uniform approximation given in Fig.7.6.7.

# 8.6 The Normal Equations

THEOREM 8.6.1． Let $x _ { 1 } , x _ { 2 } , \ldots , x _ { n }$ be independent elements and let ${ x _ { 1 } } ^ { * }$ ， ${ x _ { 2 } } ^ { * } , \ldots , { x _ { n } } ^ { * }$ be the $_ x$ 's orthonormalized. Then,for any element $_ y$ ，

$$
\left( y - \sum _ { k = 1 } ^ { n } ( y , { x _ { k } } ^ { * } ) { x _ { k } } ^ { * } \right) \perp { x _ { j } } ^ { * } .
$$

Proof:

$$
\begin{array} { l } { \left( y - { \displaystyle \sum _ { k = 1 } ^ { n } } ( y , x _ { k } ^ { * } ) x _ { k } ^ { * } , x _ { j } ^ { * } \right) } \\ { = ( y , x _ { j } ^ { * } ) - { \displaystyle \sum _ { k = 1 } ^ { n } } ( y , x _ { k } ^ { * } ) ( x _ { k } ^ { * } , x _ { j } ^ { * } ) = ( y , x _ { j } ^ { * } ) - ( y , x _ { j } ^ { * } ) = 0 . } \end{array}
$$

COROLLARy 8.6.2. y minus its best approximation by linear combinations of $\pmb { x } _ { 1 } , \ldots , \pmb { x } _ { n }$ is orthogonal to each $x _ { j }$

![](../chunks/Interpolation and Approximation (Philip J. Davis) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0141-0210/auto/images/d1f446c4de5299d6cf2e849a362ead2de891e46cab18528300618f0da2766267.jpg)  
Figure 8.6.1

In geometric language，we speak of the set of all possible linear combinations $a _ { 1 } x _ { 1 } + a _ { 2 } x _ { 2 } + \cdot \cdot \cdot a _ { n } x _ { n }$ as constituting a linear manifold.A linear manifold is a natural generalization of the notion of a plane through the origin,and this corollary states that the shortest distance from a fixed element to a point of a linear manifold is the length of an element perpendicular to the manifold. (See also Def. 9.4.1.)

THEOREM 8.6.3． Let $a _ { 1 } x _ { 1 } + a _ { 2 } x _ { 2 } + \cdots + a _ { n } x _ { n }$ be the best approximation to y from among the linear combinations of $x _ { 1 } , \ldots , x _ { n }$ (assumed independent). Then, the coefficients $\boldsymbol { a } _ { i }$ are the solution of the following system of equations.

$$
\begin{array} { r l r } & { a _ { 1 } ( x _ { 1 } , x _ { 1 } ) + a _ { 2 } ( x _ { 2 } , x _ { 1 } ) + \dotsb + a _ { n } ( x _ { n } , x _ { 1 } ) = ( y , x _ { 1 } ) } & \\ & { \cdot } & { \cdot } \\ & { \cdot } & { \cdot } \end{array}
$$

$$
a _ { 1 } ( x _ { 1 } , x _ { n } ) + a _ { 2 } ( x _ { 2 } , x _ { n } ) + \dotsb + a _ { n } ( x _ { n } , x _ { n } ) = ( y , x _ { n } ) .
$$

These equations are known as the normal equations.

Proof: By the previous corollary, $( y - a _ { 1 } x _ { 1 } - \cdot \cdot \cdot - a _ { n } x _ { n } , x _ { j } ) = 0$ When expanded, this is the jth equation of system (8.6.1).

# 8.7 Gram Matrices and Determinants

DEFINITION 8.7.1. Given a sequence of elements ${ \pmb x } _ { 1 } , { \pmb x } _ { 2 } , \ldots , { \pmb x } _ { n }$ in an

inner product space. The $n \times n$ matrix

$$
\begin{array} { r } { G = ( ( x _ { i } , x _ { j } ) ) = \left[ { \begin{array} { c c } { ( x _ { 1 } , x _ { 1 } ) } & { ( x _ { 1 } , x _ { 2 } ) , \dots , ( x _ { 1 } , x _ { n } ) } \\ { \cdot } & { \cdot } \\ { \cdot } & { \cdot } \\ { \cdot } & { \cdot } \\ { ( x _ { n } , x _ { 1 } ) } & { ( x _ { n } , x _ { 2 } ) , \dots , ( x _ { n } , x _ { n } ) } \end{array} } \right] } \end{array}
$$

is known as the Gram matrix of ${ \pmb x _ { 1 } } , { \pmb x _ { 2 } } , \ldots , { \pmb x _ { n } }$ . Its determinant

$$
g = g ( x _ { 1 } , \ldots , x _ { n } ) = | ( x _ { i } , x _ { j } ) | = | ( x _ { j } , x _ { i } ) |
$$

is known as the Gram determinant of the elements.

The Gram matrix is the transpose of the coefficient matrix of the normal equations.It is also the matrix of the bilinear form

$$
( a _ { 1 } x _ { 1 } + a _ { 2 } x _ { 2 } + \cdot \cdot \cdot + a _ { n } x _ { n } , b _ { 1 } x _ { 1 } + b _ { 2 } x _ { 2 } + \cdot \cdot \cdot + b _ { n } x _ { n } ) = \sum _ { i , j = 1 } ^ { n } a _ { i } \bar { b } _ { j } ( x _ { i } , x _ { j } ) .
$$

Notice that $g ( x _ { 1 } , \ldots , x _ { n } )$ is a symmetric function of its arguments. For, consider $g ( x _ { 1 } , \ldots , x _ { i } , \ldots , x _ { j } , \ldots , x _ { n } )$ and suppose that $\pmb { x } _ { i }$ and $\pmb { x } _ { j }$ have been interchanged yielding $g ( x _ { 1 } , \ldots , x _ { j } , \ldots , x _ { i } , \ldots , x _ { n } )$ . In the determinant expression for the latter,interchange the ith and $j$ th columns and the ith and jth rows and obtain the determinant for the former.

LEMMA 8.7.1. Let $y _ { i } = \sum _ { j = 1 } ^ { n } a _ { i j } x _ { j } , i = 1 , 2 , . . . , n$ Let A designate the matrix $( a _ { i j } )$ and $\pmb { \cal { \check { A } } }$ be its conjugate transpose $( \bar { a } _ { j i } )$ . Then

$$
G ( y _ { 1 } , y _ { 2 } , . . . , y _ { n } ) = A G ( x _ { 1 } , x _ { 2 } , . . . , x _ { n } ) { \tilde { A } }
$$

and

$$
g ( y _ { 1 } , \dots , y _ { n } ) = | \operatorname* { d e t } A | ^ { 2 } \ g ( x _ { 1 } , . . . \ , x _ { n } . )
$$

Proof:

$$
\begin{array} { r } { \left[ \begin{array} { c c c c } { ( x _ { 1 } , y _ { 1 } ) } & { ( x _ { 1 } , y _ { 2 } ) } & { \cdot \cdot \cdot } & { ( x _ { 1 } , y _ { n } ) } \\ { \cdot } & { } & { } & { \cdot } \\ { \cdot } & { } & { } & { \cdot } \\ { \cdot } & { } & { } & { \cdot } \\ { \cdot } & { } & { } & { \cdot } \\ { ( x _ { n } , y _ { 1 } ) } & { ( x _ { n } , y _ { 2 } ) } & { \cdot \cdot \cdot } & { ( x _ { n } , y _ { n } ) } \end{array} \right] } \end{array}
$$

$$
\begin{array} { r l } & { = \left[ \begin{array} { c c c c c c } { ( x _ { 1 } , x _ { 1 } ) } & { ( x _ { 1 } , x _ { 2 } ) } & { \cdots } & { ( x _ { 1 } , x _ { n } ) } \\ { \cdot } & & & & { \cdot } \\ { \cdot } & & & & { \cdot } \\ { \cdot } & & & & { \cdot } \\ { \cdot } & & & & { \cdot } \\ { ( x _ { n } , x _ { 1 } ) } & { ( x _ { n } , x _ { 2 } ) } & { \cdots } & { ( x _ { n } , x _ { n } ) } \end{array} \right] \left[ \begin{array} { c c c c c } { \bar { a } _ { 1 1 } } & { \bar { a } _ { 2 1 } } & { \cdots } & { \bar { a } _ { n 1 } } \\ { \cdot } & & & { \cdot } \\ { \cdot } & & & { \cdot } \\ { \cdot } & & & { \cdot } \\ { \cdot } & & & { \cdot } \\ { \bar { a } _ { 1 n } } & { \bar { a } _ { 2 n } } & { \cdots } & { \bar { a } _ { n n } } \end{array} \right] } \\ & { = G ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } ) \bar { A } . } \end{array}
$$

Furthermore,

$$
{ \begin{array} { r l } { [ a _ { 1 1 } \quad a _ { 1 2 } \quad \cdots \quad a _ { 1 n } ] } & { { \ u { ' } } ( x _ { 1 } , y _ { 1 } ) \quad ( x _ { 1 } , y _ { 2 } ) \quad \cdots \quad ( x _ { 1 } , y _ { n } ) } \\ { \cdot \quad } & { \cdot \cdot } \\ { \cdot \quad } & { \cdot \cdot } \\ { \cdot \quad } & { \cdot \cdot } \\ { a _ { n 1 } \quad a _ { n 2 } \quad \cdots \quad a _ { n n } ] [ ( x _ { n } , y _ { 1 } ) \quad ( x _ { n } , y _ { 2 } ) \quad \cdots \quad ( x _ { n } , y _ { n } ) ] } \end{array} }
$$

$$
\begin{array} { r } { { \bf \Phi } = \left[ { \begin{array} { c c c c } { ( y _ { 1 } , y _ { 1 } ) } & { ( y _ { 1 } , y _ { 2 } ) } & { \cdots \cdots } & { ( y _ { 1 } , y _ { n } ) } \\ { \cdot } & { } & { \cdot } \\ { \cdot } & { } & { \cdot } \\ { \cdot } & { } & { \cdot } \\ { \cdot } & { } & { \cdot } \\ { ( y _ { n } , y _ { 1 } ) } & { ( y _ { n } , y _ { 2 } ) } & { \cdots \cdot } & { ( y _ { n } , y _ { n } ) } \end{array} } \right] = G ( y _ { 1 } , \ldots , y _ { n } ) . } \end{array}
$$

Combining these two equations we obtain the first identity of the lemna. The second comes from taking determinants and observing that $| { \tilde { A } } | = { \overline { { | A | } } }$ As a special case,

$$
g ( \sigma _ { 1 } x _ { 1 } , \sigma _ { 2 } x _ { 2 } , . . . , \sigma _ { n } x _ { n } ) = | \sigma _ { 1 } | ^ { 2 } | \sigma _ { 2 } | ^ { 2 } \cdot \cdot \cdot | \sigma _ { n } | ^ { 2 } g ( x _ { 1 } , x _ { 2 } , . . . , x _ { n } ) .
$$

THEOREM 8.7.2. Let $\pmb { x } _ { 1 } , \ldots , \pmb { x } _ { n } \neq 0$ Then,

$$
0 \leq g ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } ) \leq \| x _ { 1 } \| ^ { 2 } \| x _ { 2 } \| ^ { 2 } \cdot \cdot \cdot \| x _ { n } \| ^ { 2 } .
$$

The lower extreme $g = 0$ occurs if and only if the elements $x _ { i }$ are dependent.   
The upper extreme occurs if and only if the elements are orthogonal.

If the elements have been normalized: $\| { \pmb x } _ { i } \| = 1$ , then we have

$$
0 \leq g \leq 1 .
$$

Proof:Suppose first that the $\pmb { x }$ s are dependent. Then,we can find constants $a _ { 1 } , \ldots , a _ { n }$ not all zero such that $a _ { 1 } x _ { 1 } + a _ { 2 } x _ { 2 } + \cdot \cdot \cdot + a _ { n } x _ { n } = 0$ Suppose that $ { \boldsymbol { a } } _ { j } \neq 0$ ,and consider the transformation

$$
\begin{array} { l } { y _ { 1 } = x _ { 1 } } \\ { . } \\ { . } \end{array}
$$

$$
\begin{array} { r l r } {  { y _ { j - 1 } = x _ { j - 1 } } } \\ & { } & \\ & { } & { y _ { j } = a _ { 1 } x _ { 1 } + a _ { 2 } x _ { 2 } + \cdot \cdot \cdot + a _ { n } x _ { n } = 0 } \\ & { } & \\ { \mathscr { Y } _ { j + 1 } = } & { x _ { j + 1 } } \\ & { } & \\ { \cdot } & { } & \\ { \cdot } & { \cdot } & { \cdot } \\ { \mathscr { Y } _ { n } = } & { } & { x _ { n } . } \end{array}
$$

Since $( y _ { j } , y _ { i } ) = ( 0 , y _ { \imath } ) = 0 , g ( y _ { 1 } , . . . , y _ { n } ) = 0 .$ Now

$$
\scriptstyle 1 4 | = { \begin{array} { l } { 1 } \\ { 1 } \\ { \ldots } \\ { \ldots } \\ { \ldots } \\ { \ldots } \\ { \ldots } \\ { \ldots } \\ { \ldots } \\ { \ldots } \\ { \ldots } \\ { \ldots } \\ { \ldots } \\ { \ldots } \\ { \ldots } \\ { \ldots } \\ { \ldots } \\ { \ldots } \\ { \ldots } \\ { \ldots } \\ { \ldots } \\ { \ldots } \\ { \ldots } \\ { \ldots } \\ { \ldots } \\ { \ldots } \\ { \ldots } \\ { \ldots } \\ { \ldots } \end{array} } \ \ldots \ \ldots \ \ldots \ \ \ldots
$$

Expanding this according to minors of the jth row, we find

$$
| A | = 0 + 0 + \cdots + a _ { j } \cdot 1 + 0 + \cdots + 0 = a _ { j } \neq 0 .
$$

It follows from Lemma 8.7.1 that $g ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } ) = 0$

Next,suppose that the $\pmb { x }$ s are independent. Then by Theorem 8.3.3 we can find constants $\pmb { a } _ { i j }$ such that the elements

$$
{ x _ { k } } ^ { * } = a _ { k 1 } x _ { 1 } + a _ { k 2 } x _ { 2 } + \cdot \cdot \cdot + a _ { k k } x _ { k } , ~ a _ { k k } > 0
$$

are orthonormal. By our lemma,

$$
1 = | \delta _ { i j } | = g ( x _ { 1 } { } ^ { * } , x _ { 2 } { } ^ { * } , \ldots , x _ { n } { } ^ { * } ) = g ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } ) | A | ^ { 2 }
$$

where

$$
\begin{array} { r } { | A | = \left| \begin{array} { l l l l } { a _ { 1 1 } } & { 0 } & { \cdots } & { 0 } \\ { a _ { 2 1 } } & { a _ { 2 2 } } & { \cdots } & { 0 } \\ { \cdot } & { } & { } & { \cdot } \\ { \cdot } & { } & { } & { \cdot } \\ { \cdot } & { } & { } & { \cdot } \\ { a _ { n 1 } } & { a _ { n 2 } } & { \cdots } & { a _ { n n } } \end{array} \right| = a _ { 1 1 } a _ { 2 2 } \cdot \cdot \cdot a _ { n n } . } \end{array}
$$

Hence,

$$
g ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } ) = { \frac { 1 } { { a _ { 1 1 } } ^ { 2 } } } \cdot { \frac { 1 } { { a _ { 2 2 } } ^ { 2 } } } \cdot \cdot \cdot { \frac { 1 } { { a _ { n n } } ^ { 2 } } } > 0 .
$$

Hence ${ \pmb g } = { \bf 0 }$ occurs when and only when the $_ x$ 's are dependent.

We show next that

$$
{ \frac { 1 } { { a _ { k k } } ^ { 2 } } } \leq \| x _ { k } \| ^ { 2 } .
$$

From (8.3.6), ${ \frac { 1 } { { a _ { k k } } ^ { 2 } } } = \| y _ { k } \| ^ { 2 } = \left\| { x _ { k } } - \sum _ { j = 1 } ^ { k - 1 } { ( x _ { k } , x _ { j } ^ { * } ) x _ { j } ^ { * } } \right\| ^ { 2 } \leq \| x _ { k } \| ^ { 2 } { \mathrm { ( f r o m ~ T h e o r e m } }$ 8.5.1 with $a _ { i } = 0$ ）.

If the $x _ { i }$ are orthogonal, then $G$ is a matrix with $\| x _ { i } \| ^ { 2 }$ on the diagonal and O's elsewhere. In this case, $g ( x _ { 1 } , x _ { 2 } , . . . , x _ { n } ) = \| x _ { 1 } \| ^ { 2 } \| x _ { 2 } \| ^ { 2 } \cdot \cdot \cdot \| x _ { n } \| ^ { 2 }$ Suppose, conversely, $g ( x _ { 1 } , x _ { 2 } , . . . , x _ { n } ) = \| x _ { 1 } \| ^ { 2 } \| x _ { 2 } \| ^ { 2 } \cdot \cdot \cdot \| x _ { n } \| ^ { 2 }$ .We have from $\begin{array} { r l r } & { } & { ( 8 . 7 . 1 0 ) \ g ( x _ { 1 } , \dots , x _ { n } ) = \cfrac { 1 } { a _ { 1 1 } ^ { 2 } } \cdot \cdot \cdot \cdot \frac { 1 } { a _ { n n } ^ { 2 } } \cdot \ \cdot \mathrm { N o w ~ s i n c e } \ \cfrac { 1 } { a _ { k k } ^ { 2 } } \leq \| x _ { k } \| ^ { 2 } , \mathrm { i t ~ f o l l o w s ~ t } } \\ & { } & { \| y _ { k } \| ^ { 2 } = \cfrac { 1 } { a _ { k k } ^ { 2 } } = \| x _ { k } \| ^ { 2 } , \ k = 1 , 2 , \dots , n \cdot \mathrm { B u t ~ f r o m ~ } ( 8 . 3 . 6 ) \ \mathrm { a n d ~ C o r o l l a r y ~ 8 . } } \\ & { } & { \| y _ { k } \| ^ { 2 } = \| x _ { k } \| ^ { 2 } - \displaystyle \sum _ { i = 1 } ^ { k - 1 } | ( x _ { k } , x _ { i } ^ { * } ) | ^ { 2 } . \ \mathrm { H e n c e } \ \sum _ { i = 1 } ^ { k - 1 } | ( x _ { k } , x _ { i } ^ { * } ) | ^ { 2 } = 0 \ f \mathrm { o r } \ k = 1 , } \end{array}$ that 5.3, $2 , \ldots , n$ . This implies the orthogonality of the vectors $x _ { 1 } , x _ { 2 } , \ldots , x _ { n } .$

CoRoLLARY 8.7.3 (Hadamard's Determinant Inequality).Let $D = ( a _ { i j } )$ be an $\textit { \textbf { n } } \times \textit { \textbf { n } }$ matrix with complex elements. Then,

$$
| D | ^ { 2 } \leq \prod _ { k = 1 } ^ { n } ( | a _ { k 1 } | ^ { 2 } + | a _ { k 2 } | ^ { 2 } + \cdot \cdot \cdot + | a _ { k n } | ^ { 2 } ) .
$$

If the elements $a _ { i j }$ satisfy $| a _ { i j } | \le M , i , j = 1 , 2 , . . . , n$ then

$$
| D | \leq M ^ { n } n ^ { n / 2 } .
$$

Proof:Let $\pmb { x _ { i } }$ designate the vector $( a _ { i 1 } , a _ { i 2 } , \ldots , a _ { i n } )$ .Use the Hermitian inner product $( x _ { i } , x _ { j } ) = \sum _ { k = 1 } ^ { n } a _ { i k } \bar { a } _ { j k }$ in $C _ { n }$

If $\tilde { D }$ designates the conjugate transpose of $D , \vert \bar { a } _ { j i } \vert$ ,then

$$
\begin{array} { r } { D \tilde { D } = \left| \begin{array} { l } { a _ { 1 1 } \quad a _ { 1 2 } \quad \cdot \cdot \cdot \quad a _ { 1 n } } \\ { a _ { 2 1 } \quad a _ { 2 2 } \quad \cdot \cdot \cdot \quad a _ { 2 n } } \\ { \cdot } \\ { \cdot } \\ { \cdot } \\ { a _ { n 1 } \quad a _ { n 2 } \quad \cdot \cdot \cdot \quad a _ { n n } } \end{array} \right| \left| \begin{array} { l l l l l } { \bar { a } _ { 1 1 } \quad \bar { a } _ { 2 1 } \quad \cdot \cdot \cdot \quad \bar { a } _ { n 1 } } \\ { \bar { a } _ { 1 2 } \quad \bar { a } _ { 2 2 } \quad \cdot \cdot \cdot \quad \bar { a } _ { n 2 } } \\ { \cdot } \\ { \cdot } \\ { \cdot } \\ { \cdot } \\ { \bar { a } _ { 1 n } \quad \bar { a } _ { 2 n } \quad \cdot \cdot \cdot \quad \bar { a } _ { n n } } \end{array} \right| } \end{array}
$$

$$
= | ( x _ { i } , x _ { j } ) | = g ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } ) \leq \| x _ { 1 } \| ^ { 2 } \| x _ { 2 } \| ^ { 2 } \cdot \cdot \cdot \| x _ { n } \| ^ { 2 } .
$$

Now $\| x _ { i } \| ^ { 2 } = \sum _ { k = 1 } ^ { n } a _ { i k } { \bar { a } } _ { i k } = \sum _ { k = 1 } ^ { n } | a _ { i k } | ^ { 2 }$ And, since, $| \tilde { D } | = | \overline { { D | } }$ , (8.7.12) follows. If $| a _ { i j } | \leq M$ ，then $| a _ { k 1 } | ^ { 2 } + | a _ { k 2 } | ^ { 2 } + \cdot \cdot \cdot + | a _ { k n } | ^ { 2 } \leq n M ^ { 2 }$ so that $| D | ^ { 2 } \leq n ^ { n } M ^ { 2 n }$

Ex.1. (Gram's Criterion).Let $f _ { i } ( t ) \in C [ a , b ] i = 1 , 2 , . . . , n$ These functions

are linearly independent if and only if the Gram determinant

$$
\left| \int _ { a } ^ { b } f _ { i } ( t ) f _ { j } ( t ) d t \right| > 0 .
$$

A similar result holds for $f _ { i } ( t ) \in L ^ { 2 } [ a , b ]$

THEOREM 8.7.4. Let $x _ { 1 } , x _ { 2 } , \ldots , x _ { n }$ be independent. If

then,

$$
\delta = \operatorname* { m i n } _ { a _ { 1 } } \| y - ( a _ { 1 } x _ { 1 } + a _ { 2 } x _ { 2 } + \cdot \cdot \cdot + a _ { n } x _ { n } ) \| ,
$$

$$
\delta ^ { 2 } = \frac { g ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } , y ) } { g ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } ) } .
$$

Proof:Let the minimizing element $a _ { 1 } x _ { 1 } + a _ { 2 } x _ { 2 } + \cdots + a _ { n } x _ { n }$ be called $\pmb { \vartheta }$ Then

$$
\delta ^ { 2 } = \| y - s \| ^ { 2 } = ( y - s , y - s ) = ( y - s , y ) - ( y - s , s ) .
$$

By Theorem 8.6.1, $( { \pmb y } - { \pmb s } , { \pmb s } ) = { \pmb 0 }$ so that

$$
\delta ^ { 2 } = ( y - s , y ) = ( y , y ) - ( s , y )
$$

and

$$
( s , y ) = ( y , y ) - \delta ^ { 2 } .
$$

Write the normal equations in the following form and append to them the expanded version of (8.7.16):

$$
\begin{array} { r l } { a _ { 1 } ( x _ { 1 } , x _ { 1 } ) + a _ { 2 } ( x _ { 2 } , x _ { 1 } ) + \cdot \cdot \cdot + a _ { n } ( x _ { n } , x _ { 1 } ) - \quad } & { ( y , x _ { 1 } ) \quad { \scriptstyle = 0 } } \\ { \cdot \quad } & { \mathrm { : } } \\ { \cdot \quad } & { \mathrm { : } } \end{array}
$$

$$
\begin{array} { r l r } & { } & { a _ { 1 } ( x _ { n } , x _ { 1 } ) + a _ { 2 } ( x _ { n } , x _ { 2 } ) + \dots + a _ { n } ( x _ { n } , x _ { n } ) - \dots \quad ( y , x _ { n } ) \quad = 0 } \\ & { } & { a _ { 1 } ( x _ { 1 } , y ) + a _ { 2 } ( x _ { 2 } , y ) + \dots + a _ { n } ( x _ { n } , y ) + [ \delta ^ { 2 } - ( y , y ) ] = 0 } \end{array}
$$

If we introduce a dummy value $a _ { n + 1 } = 1$ as a coefficient of the elements of the last column, then (8.7.17) becomes a system of $n + 1$ homogeneous linear equation in $n + 1$ variables $a _ { 1 } , \ldots , a _ { n }$ ， $a _ { n + 1 } ( = 1 )$ ，which possesses a nontrivial solution.The determinant of this system must therefore vanish:

$$
\left| { \begin{array} { c c c c c } { ( x _ { 1 } , x _ { 1 } ) } & { ( x _ { 2 } , x _ { 1 } ) } & { \cdots } & { ( x _ { n } , x _ { 1 } ) } & { 0 - ( y , x _ { 1 } ) } \\ { \cdot } & { } & { } & { \cdot } & { } \\ { \cdot } & { } & { } & { \cdot } & { } \\ { \cdot } & { } & { \cdot } & { } & { \cdot } \\ { ( x _ { 1 } , x _ { n } ) } & { ( x _ { 2 } , x _ { n } ) } & { \cdots } & { ( x _ { n } , x _ { n } ) } & { 0 - ( y , x _ { n } ) } \\ { ( x _ { 1 } , y ) } & { ( x _ { 2 } , y ) } & { \cdots } & { ( x _ { n } , y ) } & { \delta ^ { 2 } - ( y , y ) } \end{array} } \right| = 0 .
$$

# Therefore

$$
\left| { \begin{array} { c c c c c } { ( x _ { 1 } , x _ { 1 } ) } & { ( x _ { 2 } , x _ { 1 } ) } & { \cdots } & { ( x _ { n } , x _ { 1 } ) } & { 0 } \\ { \cdot } & { } & { } & { \cdot } \\ { \cdot } & { } & { } & { \cdot } \\ { \cdot } & { } & { } & { \cdot } \\ { ( x _ { 1 } , x _ { n } ) } & { ( x _ { 2 } , x _ { n } ) } & { \cdots } & { ( x _ { n } , x _ { n } ) } & { 0 } \\ { } & { } & { } & { \cdots } & { ( x _ { n } , y ) } & { \delta ^ { 2 } } \end{array} } \right|
$$

$$
\begin{array} { r } { { \bf \Pi } = \left| \begin{array} { c c c c c } { ( x _ { 1 } , x _ { 1 } ) } & { ( x _ { 2 } , x _ { 1 } ) } & { \cdots } & { ( x _ { n } , x _ { 1 } ) } & { ( y , x _ { 1 } ) } \\ { \cdot } & { } & { } & { \cdot } \\ { \cdot } & { } & { } & { \cdot } \\ { \cdot } & { } & { \cdot } & { } \\ { ( x _ { 1 } , x _ { n } ) } & { ( x _ { 2 } , x _ { n } ) } & { \cdots } & { ( x _ { n } , x _ { n } ) } & { ( y , x ) } \\ { \cdot } & { } & { \cdot \cdot } & { \cdot } & { ( x _ { n } , y ) } & { ( y , y ) } \end{array} \right| } \end{array}
$$

and

$$
\delta ^ { 2 } g ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } ) = g ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } , y ) .
$$

THEOREM 8.7.5. Let $x _ { 1 } , \ldots , x _ { n }$ be independent. The solution s to the minimum problem

$$
\operatorname* { m i n } _ { \pmb { a _ { i } } } \| y - ( a _ { 1 } x + \cdot \cdot \cdot + a _ { n } x _ { n } ) \|
$$

is given by

$$
s = - \left| \begin{array} { c c c c c c } { { ( x _ { 1 } , x _ { 1 } ) } } & { { ( x _ { 2 } , x _ { 1 } ) } } & { { \cdots \cdot } } & { { ( x _ { n } , x _ { 1 } ) } } & { { ( y , x _ { 1 } ) } } \\ { { . } } & { { . } } & { { . } } & { { . } } \\ { { . } } & { { . } } & { { . } } & { { . } } \\ { { . } } & { { . } } & { { . } } & { { . } } \\ { { ( x _ { 1 } , x _ { n } ) } } & { { ( x _ { 2 } , x _ { n } ) } } & { { \cdots } } & { { ( x _ { n } , x _ { n } ) } } & { { ( y , x _ { n } ) } } \\ { { x _ { 1 } } } & { { x _ { 2 } } } & { { . . . } } & { { x _ { n } } } & { { 0 } } \end{array} \right| \ \stackrel { . } { : } \ g ( x _ { 1 } , . . . , x _ { n } ) .
$$

The remainder or error, $y - s$ , is given by

$$
y - s = \left| { \begin{array} { l l l l l } { ( x _ { 1 } , x _ { 1 } ) } & { ( x _ { 2 } , x _ { 1 } ) } & { \cdots \cdot } & { ( x _ { n } , x _ { 1 } ) } & { ( y , x _ { 1 } ) } \\ { \cdot } & { } & { } & { \cdot } \\ { \cdot } & { } & { } & { \cdot } \\ { \cdot } & { } & { } & { \cdot } \\ { ( x _ { 1 } , x _ { n } ) } & { ( x _ { 2 } , x _ { n } ) } & { \cdots \cdot } & { ( x _ { n } , x _ { n } ) } & { ( y , x _ { n } ) } \\ { \quad x _ { 1 } } & { x _ { 2 } } & { \cdots \cdot } & { x _ { n } } & { y } \end{array} } \right| \div \ g ( x _ { 1 } , \cdot \cdot \ , \ x _ { n } ) .
$$

Proof: Froin the normal equations (8.6.l) and Cramer's rule (1.2.2) we have

$$
a _ { 1 } = \left| \begin{array} { c c c c c } { { ( y , x _ { 1 } ) } } & { { ( x _ { 2 } , x _ { 1 } ) } } & { { \cdots } } & { { ( x _ { n } , x _ { 1 } ) } } \\ { { } } & { { } } & { { } } & { { } } \\ { { ( y , x _ { 2 } ) } } & { { ( x _ { 2 } , x _ { 2 } ) } } & { { \cdots } } & { { ( x _ { n } , x _ { 2 } ) } } \\ { { } } & { { } } & { { } } & { { } } & { { } } \\ { { \cdot } } & { { \cdot } } & { { } } & { { \cdot } } \\ { { \cdot } } & { { \cdot } } & { { } } & { { \cdot } } \\ { { } } & { { } } & { { } } & { { } } & { { } } \\ { { ( y , x _ { n } ) } } & { { ( x _ { 2 } , x _ { n } ) } } & { { \cdots } } & { { ( x _ { n } , x _ { n } ) } } \end{array} \right| \div g ( x _ { 1 } , \ldots , x _ { n } ) ,
$$

with similar formulas for the other a's.If we expand the determinant in (8.7.18) according to the minors of the last row we obtain expressions for the coefficients of the $_ { \pmb { x } }$ 's which coincide with those just mentioned.

Since

$$
y = { \left| \begin{array} { c c c c c c } { ( x _ { 1 } , x _ { 1 } ) } & { ( x _ { 2 } , x _ { 1 } ) } & { \cdots } & { ( x _ { n } , x _ { 1 } ) } & { 0 } \\ { \cdot } & { } & { \cdot } & { \cdot } & { \cdot } \\ { \cdot } & { } & { \cdot } & { \cdot } & { \cdot } \\ { \cdot } & { } & { \cdot } & { \cdot } & { \cdot } \\ { ( x _ { 1 } , x _ { n } ) } & { ( x _ { 2 } , x _ { n } ) } & { \cdots } & { ( x _ { n } , x _ { n } ) } & { 0 } \\ { x _ { 1 } } & { x _ { 2 } } & { \cdots } & { x _ { n } } & { y } \end{array} \right| } { \overset { } { _ { \ x { 1 } } } { \longrightarrow } } g ( x _ { 1 } , \ldots , x _ { n } ) ,
$$

adding (8.7.18) to (8.7.21) yields (8.7.19).

COROLLARY 8.7.6. Let the elements $x _ { 1 } , x _ { 2 } , \ldots .$ ，be linearly independent and be orthonormalized according to the Gram-Schmidt scheme yielding ${ \pmb x _ { 1 } } ^ { * }$ ， ${ x _ { 2 } } ^ { * }$ .. Then,

$$
\scriptstyle x _ { n } ^ { * } = { \frac { 1 } { \sqrt { g ( x _ { 1 } , \ . . . \ , x _ { n - 1 } ) g ( x _ { 1 } , \ . . . \ , x _ { n } ) } } } \left| { \begin{array} { c c c c c c } { ( x _ { 1 } , x _ { 1 } ) } & { ( x _ { 2 } , x _ { 1 } ) } & { \cdots } & { ( x _ { n } , x _ { n - 1 } ) } & & \\ { \cdot } & & & & { \cdot } & \\ { \cdot } & & & & & { \cdot } & \\ & & & & & { \cdot } & \\ { \cdot } & & & & & & { \cdot } \end{array} } \right. .
$$

$$
{ x _ { 1 } } ^ { * } = { x _ { 1 } } / { \sqrt { g ( x _ { 1 } ) } } .
$$

The“leading coefficient" in ${ x _ { n } } ^ { * } , a _ { n n }$ is given by

$$
a _ { n n } = { \sqrt { \frac { g ( x _ { 1 } , \ldots , x _ { n - 1 } ) } { g ( x _ { 1 } , \ldots , x _ { n } ) } } } , n > 1 .
$$

Proof: Consider the minimum problem

$$
\operatorname* { m i n } _ { a _ { i } } \| x _ { n } - ( a _ { 1 } x _ { 1 } + \cdot \cdot \cdot + a _ { n - 1 } x _ { n - 1 } ) \| .
$$

According to Corollary 8.5.7, the solution is given by

$$
{ \frac { { x _ { n } } ^ { * } } { a _ { n n } } } = x _ { n } - ( a _ { 1 } x _ { 1 } + \cdot \cdot \cdot + a _ { n - 1 } x _ { n - 1 } ) , ~ a _ { n n } > 0 .
$$

According to (8.7.19),

$$
\begin{array} { r l } {  { n - ( a _ { 1 } x _ { 1 } + \cdot \cdot \cdot + a _ { n - 1 } x _ { n - 1 } ) } } \\ & { = | { \begin{array} { c c c c c c } { ( x _ { 1 } , x _ { 1 } ) } & { ( x _ { 2 } , x _ { 1 } ) } & { \cdot \cdot \cdot } & { ( x _ { n - 1 } , x _ { 1 } ) } & { ( x _ { n } , x _ { 1 } ) } \\ { \cdot } & & & & { \cdot } \\ { \cdot } & & & & { \cdot } \\ { \cdot } & & & & & { \cdot } \\ { \cdot } & & & & & { \cdot } \\ { ( x _ { 1 } , x _ { n - 1 } ) } & { ( x _ { 2 } , x _ { n - 1 } ) } & { \cdot \cdot \cdot } & { ( x _ { n - 1 } , x _ { n - 1 } ) } & { ( x _ { n } , x _ { n - 1 } ) } \\ { x _ { 1 } } & { x _ { 2 } } & { \cdot \cdot \cdot } & { x _ { n - 1 } } & { x _ { n } } \end{array} } | \div \ g ( x _ { 1 } , \cdot . . . , x _ { n - 1 } ) } \end{array}
$$

From Corollary 8.5. $\begin{array} { r l } & { 7 , \displaystyle \frac { 1 } { a _ { n n } } = \left\| \frac { { x _ { n } } ^ { * } } { a _ { n n } } \right\| = \operatorname* { m i n } _ { a _ { i } } \| x _ { n } - ( a _ { 1 } x _ { 1 } + \cdot \cdot \cdot + a _ { n - 1 } x _ { n - 1 } ) \| , } \\ & { 3 . 7 . 4 , \mathrm { t h i s ~ m i n i m u m } = \sqrt { \displaystyle \frac { g ( x _ { 1 } , \cdot \cdot \cdot , x _ { n } ) } { g ( x _ { 1 } , \cdot \cdot \cdot , x _ { n - 1 } ) } } \cdot \mathrm { H e n c e ~ } ( 8 . 7 . 2 2 ) } \\ & { \mathrm { : ~ a n d ~ } ( 8 . 7 . 2 3 ) . } \end{array}$ and from Theorem 8.7.4,this minimum = follows from (8.7.24) and (8.7.23).

Ex. 2. The Legendre polynomials are given by

$$
{ p _ { 0 } } ^ { * } ( x ) = \frac { 1 } { \sqrt { 2 } } , \quad { p _ { 1 } } ^ { * } ( x ) = \frac { 1 } { \sqrt { 2 } \sqrt { \frac { 4 } { 3 } } } \biggr | _ { 1 } ^ { 2 } \quad 0 \biggr | ,
$$

$$
p _ { 2 } \ L ^ { * } ( x ) = \frac { 1 } { \sqrt { \frac { 4 } { 3 } } \sqrt { \frac { 3 2 } { 1 \ L ^ { 3 } 3 } } } \left| \begin{array} { l l l } { 2 } & { 0 } & { \frac { 2 } { 3 } } \\ { 0 } & { \frac { 2 } { 3 } } & { 0 } \\ { 1 } & { x } & { x ^ { 2 } } \end{array} \right| , \ L \ L \ L 
$$

# 8.8 Further Properties of the Gram Determinant

THEOREM 8.8.1. The Gram determinant $g ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } )$ has the followving properties.

(a) $\pmb { g }$ is a symmetric function of its arguments.

$$
g ( x _ { 1 } , \ldots , \sigma x _ { j } , \ldots , x _ { n } ) = | \sigma | ^ { 2 } g ( x _ { 1 } , \ldots , x _ { n } )
$$

$$
\begin{array} { r l } & { g ( x _ { 1 } , \dotsc , x _ { j } + \sigma x _ { k } , \dotsc , x _ { n } ) = g ( x _ { 1 } , \dotsc , x _ { n } ) , j \neq k } \\ & { g ^ { \frac { 1 } { 2 } } ( x _ { 1 } ^ { \prime } + x _ { 1 } ^ { \prime } , x _ { 2 } , \dotsc , x _ { n } ) \leq g ^ { \frac { 1 } { 2 } } ( x _ { 1 } ^ { \prime } , x _ { 2 } , \dotsc , x _ { n } ) } \\ & { \qquad + g ^ { \frac { 1 } { 2 } } ( x _ { 1 } ^ { \prime \prime } , x _ { 2 } , \dotsc , x _ { n } ) } \\ & { g ( x _ { 1 } , \dotsc , x _ { n } ) \leq g ( x _ { 1 } , \dotsc , x _ { p } ) g ( x _ { p + 1 } , \dotsc , x _ { n } ) , 1 \leq p < n . } \end{array}
$$

Equality in (e) holds if and only if

$$
\begin{array} { r } { ( x _ { i } , x _ { j } ) = 0 \quad 1 \leq i \leq p , \quad p + 1 \leq j \leq n . } \end{array}
$$

(Compare Theorem 13.1.2.)

Proof:Statements (a) and (b) have already been proved. (c).Write the left hand member of (8.8.1)(c) as a determinant of inner products. Expand the inner products in the $j ^ { \mathrm { t h } }$ row and use the elementary properties of determinants.Then expand the inner products in the jth column and do likewise. (d). We may assume that ${ \pmb x _ { 2 } } , \ldots , { \pmb x _ { n } }$ are independent. Otherwise both members of (8.8.1)(d) vanish and the inequality holds trivially. Orthonormalize ${ \pmb x _ { 2 } } , \ldots , { \pmb x _ { n } }$ and call the orthonormal vectors ${ x _ { 2 } } ^ { * } , \ldots , { x _ { n } } ^ { * }$ .Then, from Theorem 8.5.1 and (8.7.15),

$$
\begin{array} { r l } & { \frac { g ^ { \frac { 1 } { 4 } } ( x _ { 1 } ^ { ' } + x _ { 1 } ^ { ' } , x _ { 2 } , \dots , x _ { n } ) } { g ^ { \frac { 1 } { 4 } } ( x _ { 2 } , \dots , x _ { n } ) } = \bigg \| { x _ { 1 } ^ { ' } + x _ { 1 } ^ { ' } - \frac { \displaystyle n } { { k - 2 } } ( x _ { 1 } ^ { ' } + x _ { 1 } ^ { ' } , x _ { k } ^ { * } ) } \bigg \| } \\ & { ~ = \bigg \| { x _ { 1 } ^ { ' } - \frac { \displaystyle n } { { k - 2 } } ( x _ { 1 } ^ { ' } , x _ { k } ^ { * } ) x _ { k } ^ { * } + x _ { 1 } ^ { ' } - \frac { \displaystyle n } { { k - 2 } } ( x _ { 1 } ^ { ' } , x _ { k } ^ { * } ) x _ { k } ^ { * } } \bigg \| } \\ & { ~ \leq \bigg \| { x _ { 1 } ^ { ' } - \frac { \displaystyle n } { { k - 2 } } ( x _ { 1 } ^ { ' } , x _ { k } ^ { * } ) x _ { k } ^ { * } } \bigg \| + \bigg \| { x _ { 1 } ^ { ' } - \frac { \displaystyle n } { { k - 2 } } ( x _ { 1 } ^ { ' } , x _ { k } ^ { * } ) x _ { k } ^ { * } } \bigg \| } \\ & { ~ = \frac { g ^ { \frac { 1 } { 4 } } ( x _ { 1 } ^ { ' } , x _ { 2 } , \dots , x _ { n } ) } { g ^ { \frac { 1 } { 4 } } ( x _ { 2 } , \dots , \dots , x _ { n } ) } + \frac { g ^ { \frac { 1 } { 4 } } ( x _ { 1 } ^ { ' } , x _ { 2 } , \dots , x _ { n } ) } { g ^ { \frac { 1 } { 4 } } ( x _ { 2 } , \dots , x _ { n } ) } ~ . } \end{array}
$$

Multiplying this inequality by the denominator,we arrive at (d).

(e) Let $\pmb { k }$ satisfy $1 \leq k < p$ .Then,since there is more competition on the left-hand side,

$$
\operatorname* { m i n } _ { a _ { j } } \| x _ { k } - ( a _ { k + 1 } x _ { k + 1 } + \cdot \cdot \cdot + a _ { n } x _ { n } ) \| ^ { 2 } \leq \operatorname* { m i n } _ { b _ { j } } \| x _ { k } - ( b _ { k + 1 } x _ { k + 1 } + \cdot \cdot \cdot + b _ { p } x _ { p }
$$

Similarly,

$$
\operatorname* { m i n } _ { c _ { j } } \| x _ { p } - ( c _ { p + 1 } x _ { p + 1 } + \cdot \cdot \cdot + c _ { n } x _ { n } ) \| ^ { 2 } \leq \| x _ { p } \| ^ { 2 } .
$$

Therefore by Theorem 8.7.4,

$$
\frac { g ( x _ { k } , x _ { k + 1 } , x _ { k + 2 } , \ldots , x _ { n } ) } { g ( x _ { k + 1 } , \ldots , x _ { n } ) } \leq \frac { g ( x _ { k } , x _ { k + 1 } , \ldots , x _ { n } ) } { g ( x _ { k + 1 } , \ldots , x _ { p } ) }
$$

and

$$
\frac { g ( x _ { p } , x _ { p + 1 } , \ldots , x _ { n } ) } { g ( x _ { p + 1 } , \ldots , x _ { n } ) } \leq g ( x _ { p } ) .
$$

In particular,writing $k = 1$ ， $k = 2 , \ldots , p - 1$ in (8.8.2) we have

$$
{ \begin{array} { r l } & { { \frac { g ( x _ { 1 } , \ldots , x _ { n } ) } { g ( x _ { 2 } , \ldots , x _ { n } ) } } \leq { \frac { g ( x _ { 1 } , \ldots , x _ { n } ) } { g ( x _ { 2 } , \ldots , x _ { n } ) } } } \\ & { } \\ & { { \frac { g ( x _ { 2 } , \ldots , x _ { n } ) } { g ( x _ { 3 } , \ldots , x _ { n } ) } } \leq { \frac { g ( x _ { 2 } , \ldots , x _ { n } ) } { g ( x _ { 3 } , \ldots , x _ { n } ) } } } \\ & { } \\ & { \qquad \cdot } \\ & { \qquad \cdot } \\ & { { \frac { g ( x _ { p } , \ldots , x _ { n } ) } { g ( x _ { p + 1 } , \ldots , x _ { n } ) } } \leq g ( x _ { p } ) . } \end{array} }
$$

Multiplying these inequalities together,

$$
\frac { g ( x _ { 1 } , \ldots , x _ { n } ) } { g ( x _ { p + 1 } , \ldots , x _ { n } ) } \leq g ( x _ { 1 } , \ldots , x _ { p } ) ,
$$

or

$$
g ( x _ { 1 } , \ldots , x _ { n } ) \leq g ( x _ { 1 } , \ldots , x _ { p } ) g ( x _ { p + 1 } , \ldots , x _ { n } ) .
$$

Now,equality in (8.8.5) can hold if and only ifit holds in each of the relations (8.8.4); i.e.,if and only if

$$
\operatorname* { m i n } _ { { \boldsymbol { c } } _ { j } } \| { \boldsymbol { x } } _ { p } - ( c _ { p + 1 } x _ { p + 1 } + \cdot \cdot \cdot + c _ { n } x _ { n } ) \| ^ { 2 } = \| { \boldsymbol { x } } _ { p } \| ^ { 2 }
$$

and

$$
\begin{array} { r l r } & { } & { \underset { a _ { j } } { \mathrm { i n } } ~ \lVert x _ { k } - ( a _ { k + 1 } x _ { k + 1 } + \cdot \cdot \cdot + a _ { n } x _ { n } ) \rVert ^ { 2 } = \underset { b _ { j } } { \mathrm { m i n } } ~ \lVert x _ { k } - ( b _ { k + 1 } x _ { k + 1 } + \cdot \cdot \cdot + b _ { p } x _ { p } ) \rVert } \\ & { } & { k = 1 , 2 , \cdot \cdot \cdot , p - 1 . \quad ( 8 . 8 . 7 } \end{array}
$$

Now, by Corollary 8.5.3,(8.8.6) holds if and only if

$$
( x _ { p } , x _ { j } ) = 0 \quad j = p + 1 , . . . , n .
$$

Now (8.8.7) with $k = p - 1$ reads

$$
\operatorname* { m i n } _ { a _ { j } } \| x _ { p - 1 } - ( a _ { p } x _ { p } + \cdot \cdot \cdot + a _ { n } x _ { n } ) \| ^ { 2 } = \operatorname* { m i n } _ { b _ { p } } \| x _ { p - 1 } - b _ { p } x _ { p } \| ^ { 2 } .
$$

By the same principle,this holds if and only if $x _ { p - 1 } \perp x _ { p + 1 } , x _ { p + 2 } , . . . , x _ { n } .$ Considering $k = p - 2 , p - 3 , \ldots , 1$ successively，we arrive at the stated orthogonality conditions.

The Gram determinant has a very striking geometrical interpretation. Let there be given $\pmb { n }$ vectors in $R _ { n } \colon x _ { i } = ( x _ { i 1 } , x _ { i 2 } , \ldots , x _ { i n } )$ . These vectors are the edges of a certain $\pmb { n }$ -dimensional parallelotope (the generalization of a parallelogram) whose volume willbe designated by $V = V ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } )$

It can be shown that

$$
{ \left| \begin{array} { l l l l } { x _ { 1 1 } } & { x _ { 1 2 } } & { \cdots } & { x _ { 1 n } } \\ { x _ { 2 1 } } & { x _ { 2 2 } } & { \cdots } & { x _ { 2 n } } \\ { \cdot } & { \cdot } & & { \cdot } \\ { \cdot } & { \cdot } & & { \cdot } \\ { \cdot } & { \cdot } & & { \cdot } \\ { x _ { n 1 } } & { x _ { n 2 } } & { \cdots } & { x _ { n n } } \end{array} \right| } .
$$

![](../chunks/Interpolation and Approximation (Philip J. Davis) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0141-0210/auto/images/a9b79937081326fb611a34749e846bda844b973cf32d80e5921498c0f91478f9.jpg)  
Figure 8.8.1 Parallelotope in $\boldsymbol { R _ { 3 } }$

(Though elementary,the derivation of this formula is far from trivial.An axiomatic derivation can be found in Schreier and Sperner [l] Ch.II.)

Multiply the determinant in (8.8.8) by its transpose and obtain

$$
V ^ { 2 } = { \left| \begin{array} { l l l l } { ( x _ { 1 } , x _ { 1 } ) } & { ( x _ { 1 } , x _ { 2 } ) } & { \cdot \cdot \cdot } & { ( x _ { 1 } , x _ { n } ) } \\ { \cdot } & { \cdot } & { \cdot } & { \cdot } \\ { \cdot } & { \cdot } & { \cdot } & { \cdot } \\ { \cdot } & { \cdot } & { \cdot } & { \cdot } \\ { ( x _ { n } , x _ { 1 } ) } & { ( x _ { n } , x _ { 2 } ) } & { \cdot \cdot \cdot } & { ( x _ { n } , x _ { n } ) } \end{array} \right| } = g ( x _ { 1 } , \cdot \cdot \cdot , x _ { n } ) .
$$

Hence,

$$
V ( x _ { 1 } , \ldots , x _ { n } ) = { \sqrt { g ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } ) } } .
$$

A derivation of (8.8.8) can be given via Theorem 8.7.4 if we assume by way of analogy to the situation in 2 and 3 dimensions that the volume of the parallelotope can be found by multiplying altitudes.That is,assume

$$
V ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } ) = \| x _ { 1 } \| { \overset { } { d } } ( x _ { 2 } ; x _ { 1 } ) d ( x _ { 3 } ; x _ { 1 } , x _ { 2 } ) \cdot \cdot \cdot d ( x _ { n } ; x _ { 1 } , x _ { 2 } , \ldots , x _ { n - 1 } )
$$

where $d ( x _ { i } ; x _ { 1 } , x _ { 2 } , \dots , x _ { i - 1 } )$ designates the distance from $\pmb { x } _ { i }$ to the linear manifold spanned by $x _ { 1 } , \ldots , x _ { i - 1 }$ . Since

$$
d ( x _ { i } ; x _ { 1 } , x _ { 2 } , \ldots , x _ { i - 1 } ) = { \sqrt { \frac { g ( x _ { 1 } , x _ { 2 } , \ldots , x _ { i } ) } { g ( x _ { 1 } , x _ { 2 } , \ldots , x _ { i - 1 } ) } } } ,
$$

$$
V ^ { 2 } = g ( x _ { 1 } ) { \frac { g ( x _ { 1 } , x _ { 2 } ) } { g ( x _ { 1 } ) } } { \frac { g ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) } { g ( x _ { 1 } , x _ { 2 } ) } } \cdot \cdot \cdot { \frac { g ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } ) } { g ( x _ { 1 } , x _ { 2 } , \ldots , \ldots , x _ { n - 1 } ) } } = g ( x _ { 1 } , \ldots , x _ { n } ) .
$$

# 8.9 Closure and Its Consequences

DEFINITioN 8.9.1. A finite or infinite system of elements, $x _ { 1 } , x _ { 2 } , \cdots$ ,in a normed linear space $\pmb { X }$ is called closed if every element ${ \pmb x } \in { \pmb X }$ can be approximated arbitrarily closely by finite linear combinations of the $\boldsymbol { x } _ { i }$ That is, given ${ \pmb x } \in { \pmb X }$ and $\varepsilon > 0$ ,we can find constants $a _ { 1 } , \ldots , a _ { n }$ such that

$$
\| x - ( a _ { 1 } x _ { 1 } + a _ { 2 } x _ { 2 } + \cdot \cdot \cdot + a _ { n } x _ { n } ) \| \leq \varepsilon .
$$

Ex.1． Any set of $_ n$ independent vectors $x _ { 1 } , \ldots , x _ { n }$ in $\scriptstyle { R _ { n } }$ or $C _ { n }$ is closed. In this case,the approximation can be made perfect (Theorem 1.3.1).But one can also argue as follows. Since $x _ { i }$ are independent, $g ( x _ { 1 } , \ldots , x _ { n } ) > 0$ If

$$
x _ { i } = ( x _ { i 1 } , x _ { i 2 } , \ldots , x _ { i n } ) ,
$$

then

$$
g ( x _ { 1 } , \ldots , x _ { n } ) = \left| { \begin{array} { l l l } { x _ { 1 1 } } & { \cdot \cdot \cdot } & { x _ { 1 n } } \\ { \cdot } & { \cdot } & { \cdot } \\ { \cdot } & { \cdot } & { \cdot } \\ { \cdot } & { \cdot } & { \cdot } \\ { x _ { n 1 } } & { \cdot \cdot \cdot } & { x _ { n n } } \end{array} } \right| \left| { \begin{array} { l l l } { { \bar { x } } _ { 1 1 } } & { \cdot \cdot \cdot } & { { \bar { x } } _ { n 1 } } \\ { \cdot } & & { \cdot } \\ { \cdot } & & { \cdot } \\ { \cdot } & & { \cdot } \\ { { \bar { x } } _ { 1 n } } & { \cdot \cdot \cdot } & { { \bar { x } } _ { n n } } \end{array} } \right| > 0
$$

and therefore $| x _ { i j } | \neq 0$ . Given any $\pmb { y }$ , the system $a _ { 1 } x _ { 1 } + a _ { 2 } x _ { 2 } + \cdot \cdot \cdot + a _ { n } x _ { n } = y$ may be solved for the $\pmb { a } _ { i }$

Ex.2.Let $x$ be $C [ \pmb { a } , \pmb { b } ]$ with $\| f \| = \operatorname* { m a x } _ { a \leq x \leq b } | f ( x ) |$ . The powers $1 , x , x ^ { 2 } , \ldots$ ， are closed in $x$ .This is a reformulation of the Weierstrass Theorem 6.1.1.

Ex.3.Let $x$ be $\mathbf { \mathit { C } } [ \mathbf { \mathit { a } } , \mathbf { \mathit { b } } ]$ with $\| f \| ^ { 2 } = \int _ { a } ^ { b } | f ( x ) | ^ { 2 } d x$ .The powers $1 , x , x ^ { 2 } , \ldots$ ， are closed in $x$

Ex. 4.Let $\pmb { X }$ be $\mathbf { } L [ \boldsymbol { a } , \boldsymbol { b } ]$ with $\| f \| = \int _ { a } ^ { b } | f ( x ) | ~ d x$ .The powers $1 , x , x ^ { 2 } , \ldots$ ， are closed in $x$ . This is a generalization of the Weierstrass Theorem.

According to Theorem 1.4.0(e)，given an $\varepsilon > 0$ ，we can find an absolutely contir $\begin{array} { l l } { { \mathrm { ! u o u s ~ f u n c t i o n ~ } g ( x ) \mathrm { ~ s u c h ~ t h a t } { \displaystyle \int _ { a } ^ { b } } \vert f ( x ) - g ( x ) \vert d x \le \varepsilon / 2 . \mathrm { ~ S i n c e ~ } g \mathrm { ~ i s ~ c o n t i n t } } } \\ { { \mathrm { ~ n ~ f i n d ~ a ~ p o l y n o m i a l ~ } p \mathrm { ~ s u c h ~ t h a t ~ } \vert g ( x ) - p ( x ) \vert \le \displaystyle \frac { \varepsilon } { 2 ( b - a ) } , a \le x \le b } } \\ { { \displaystyle \int _ { a } ^ { b } \vert g ( x ) - p ( x ) \vert d x \le \varepsilon / 2 . \mathrm { ~ T h e r e f o r e ~ b y ~ } ( 7 . 2 . 1 7 ) } } \\ { { \displaystyle \int _ { a } ^ { b } \vert f ( x ) - g ( x ) + g ( x ) - p ( x ) \vert d x \le \varepsilon / 2 + \varepsilon / 2 = \varepsilon . } } \end{array}$ 1ous we ca and hence

Ex.5. Let $x$ be the set of analytic functions that are continuous in $| z | \leq 1$ Set

$$
\| f \| = \operatorname* { m a x } _ { | z | \leq 1 } | f ( z ) | .
$$

The powers $z , z ^ { 2 } , z ^ { 3 } , \ldots$ , are not closed in $x$ . If they were, given an $\varepsilon > 0$ we could find constants $a _ { 1 } , \ldots , a _ { n }$ such that

$$
\operatorname* { m a x } _ { | z | \leq 1 } | 1 - ( a _ { 1 } z + a _ { 2 } z ^ { 2 } + \cdot \cdot \cdot + a _ { n } z ^ { n } ) | \leq \varepsilon .
$$

Setting $z = 0$ ,we would have, in particular, $1 \ \leq \varepsilon$

Before studying the implications of closure,it will be important to recall a number of topological concepts.Let $\pmb { X }$ be a metric space with a distance function $d ( x , y )$ .(Definition 7.2.2.) If ${ \pmb x _ { 0 } } \in { \pmb X }$ ，the set $U ( x _ { 0 } , r )$ consisting of all elements $\pmb { x } \in \pmb { X }$ for which $d ( x , x _ { 0 } ) < r$ is called an open ball.An element $_ { x }$ of a subset $\pmb { S }$ is called an interior element of $\pmb { S }$ if there is an $r > 0$ such that $U ( x , r ) \subseteq S$ 、In a metric space and hence in a normed linear space,the notion of convergence can be defined:

DEFINITIoN 8.9.2. A sequence of elements $\left\{ x _ { n } \right\}$ of a metric space is said to converge to an element $x \in X$ if

$$
\operatorname* { l i m } _ { n \to \infty } d ( x , x _ { n } ) = 0 .
$$

In a normed linear space,(8.9.2) is equivalent to

$$
\operatorname* { l i m } _ { n \to \infty } \| x - x _ { n } \| = 0 .
$$

A convergent sequence cannot converge to two different elements；for suppose $\operatorname* { l i m } _ { n \to \infty } d ( x , x _ { n } ) = 0$ and $\operatorname* { l i m } _ { n \to \infty } d ( y , x _ { n } ) = 0 \quad$ By (7.2.2)(d), $0 \leq d ( x , y ) \leq$ $d ( x , x _ { n } ) + d ( y , x _ { n } )$ . Allowing $\pmb { \mathscr { n } }  \infty$ , we obtain $d ( x , y ) = 0$ and hence $x = y$ We may speak of $_ { \pmb { x } }$ as the limit of the sequence $\{ x _ { n } \}$ and write

$$
\operatorname* { l i m } _ { n \to \infty } x _ { n } = x .
$$

Convergence of type $( { \bf 8 . 9 . 2 ^ { \prime } } )$ is sometimes called convergence in norm or; if the norm happens to be given by an integral expression, convergence in the mean.In the case of normed linear spaces of functions,this serves to distinguish it from other types of convergence (pointwise,uniform,etc.). One must always make this distinction,for a sequence in a normed linear space of functions may converge in norm without converging in the pointwise sense.

$\operatorname { E x . 6 . } \ \operatorname { L e t } X \operatorname { b e } C [ - 1 , 1 ] \operatorname { w i t h } \| f \| ^ { 2 } = \int _ { - 1 } ^ { + 1 } ( f ( x ) ) ^ { 2 } d x . \operatorname { L e t } f _ { n } ( x ) = \left[ { \frac { n } { 1 + n ^ { 4 } x ^ { 2 } } } \right] \operatorname { w i t h } ( n ) \operatorname { f } _ { n } ( x ) .$ 2 Then,

$$
\| 0 - f _ { n } \| ^ { 2 } = \int _ { - 1 } ^ { + 1 } { \frac { n } { 1 + n ^ { 4 } x ^ { 2 } } } d x = { \frac { 2 } { n } } \arctan n ^ { 2 } \to 0 .
$$

However, $f _ { n } ( 0 ) \to \infty$

Let $\pmb { X }$ be a metric space and ${ \mathfrak { S } } \subseteq { \mathfrak { X } }$ .The closure $\bar { s }$ of $\pmb { S }$ is defined as the set of all limits of convergent sequences of $\pmb { S }$ Obviously ${ \mathfrak { s } } \subseteq { \bar { \mathfrak { s } } }$ If $\pmb { S } = \pmb { \bar { S } }$ ， $\pmb { S }$ is called closed.A set $\pmb { S }$ is dense in $\pmb { X }$ if ${ \bar { \boldsymbol { s } } } = { \boldsymbol { x } }$ $\pmb { X }$ is separable if there is in it a countable dense set.

If lim ${ \pmb x } _ { \pmb n } = { \pmb x }$ ，then from $d ( x _ { m } , x _ { n } ) \leq d ( x , x _ { m } ) + d ( x , x _ { n } )$ it follows that we can make $d ( x _ { m } , x _ { n } ) \leq \varepsilon$ for all $m , n > N ( \varepsilon )$ .But as in the case of the metric space of rational numbers (with $d ( x , y ) = | \pmb { x } - \pmb { y } | )$ ，the converse is not true.It is important to distinguish those spaces in which it is true.

DEFINITIoN 8.9.3. A sequence of elements of $\pmb { X }$ ， $\left\{ x _ { n } \right\}$ is called a Cauchy sequence,if for every $\varepsilon > 0$ ,there isan integer $\pmb { N } ( \pmb \varepsilon )$ such that $d ( x _ { m } , x _ { n } ) \leq \varepsilon$ for all $\pmb { m }$ ， $n \geq N ( \varepsilon )$ . A space $\pmb { X }$ is called complete if every Cauchy sequence has a limit in $\pmb { X }$

Specifically, if $\pmb { X }$ is a complete normed linear space,and if for any $\varepsilon > 0$ ， we can find $N ( \varepsilon )$ such that

$$
\begin{array} { r } { \| \boldsymbol { x } _ { m } - \boldsymbol { x } _ { n } \| \le \varepsilon , ~ m , n \ge N ( \varepsilon ) , } \end{array}
$$

then there is an $\pmb { x } \in \pmb { X }$ such that

$$
\operatorname* { l i m } _ { n \to \infty } \| { \pmb x } - { \pmb x } _ { n } \| = 0 .
$$

A complete normed linear space is often called a Banach Space.

Ex.7. The complex Euclidian space $C _ { n }$ is complete and hence is a Banach Space. Let $\pmb { x _ { m } } = ( x _ { 1 } ^ { ( m ) } , x _ { 2 } ^ { ( m ) } , \dots , x _ { n } ^ { ( m ) } )$ if $\{ x _ { m } \}$ is a Cauchy sequence, then

$$
\sum _ { i = 1 } ^ { n } | x _ { i } ^ { ( m ) } - x _ { i } ^ { ( p ) } | ^ { 2 } \leq \varepsilon \quad \mathrm { f o r } \quad m , p > N ( \varepsilon ) .
$$

Hence, for any particular $i , | x _ { i } ^ { ( m ) } - x _ { i } ^ { ( p ) } | ^ { 2 } \leq \varepsilon$ for $m , p \geq N ( \varepsilon )$ .Thus, for each $i , x _ { i } ^ { ( m ) }$ is a Cauchy sequence and has a limit $x _ { i }$ ： $\operatorname* { l i m } _ { \ i  \infty } | x _ { i } - x _ { i } ^ { ( m ) } | = 0$ If we set m→8

$$
x = ( x _ { 1 } , \ldots , x _ { n } ) { \mathrm { ~ t h e n ~ } } \| x - x _ { m } \| ^ { 2 } = \sum _ { i = 1 } ^ { n } | x _ { i } - x _ { i } ^ { ( m ) } | ^ { 2 } \leq \varepsilon ^ { 2 } { \mathrm { ~ f o r ~ } } m \geq N ^ { \prime } ( \varepsilon ) .
$$

Ex.8. Let $C [ \boldsymbol { a } , \boldsymbol { b } ]$ be normed by $\| f \| = \operatorname* { m a x } _ { a \leq x \leq b } | f ( x ) |$ . This space is complete. For if $\operatorname* { m a x } _ { a \leq x \leq b } | f _ { m } ( x ) - f _ { n } ( x ) | \leq \varepsilon , m , n > N ( \bar { \varepsilon } )$ then the sequence $f _ { m } ( x )$ is uniformly convergent on $[ a , b ]$ .Hence there isa function $f ( x ) \in C [ a , b ]$ for which

$$
| f ( x ) - f _ { n } ( x ) | \leq \varepsilon , a \leq x \leq b , n \geq N ^ { \prime } ( \varepsilon ) ,
$$

and this implies that $f _ { n }$ converges to $f$ in the norm considered.

Ex. 9. On the other hand,if $x$ is $C [ \boldsymbol { a } , \boldsymbol { b } ]$ normed by $\| f \| ^ { 2 } = \int _ { a } ^ { b } | f ( x ) | ^ { 2 } d x ,$ then $\pmb { X }$ is not complete.This can be shown by exhibiting a Cauchy sequence in $\pmb { X }$ which does not converge to an element of $x$

For simplicity take $a = - 1 , b = 1$ and let $f _ { n } ( x )$ be the continuous function

$$
f _ { n } ( x ) = { \left\{ \begin{array} { l l } { - 1 \quad } & { - 1 \leq x \leq - { \frac { 1 } { n } } } \\ { \qquad } \\ { n x \qquad } & { - { \frac { 1 } { n } } \leq x \leq { \frac { 1 } { n } } . } \\ { \qquad } \\ { 1 \quad } & { { \frac { 1 } { n } } \leq x \leq 1 } \end{array} \right. }
$$

Let $f ( x )$ be the discontinuous function

$$
f ( x ) = \left\{ { \begin{array} { l l } { - 1 \qquad - 1 \leq x \leq 0 . } \\ { 1 \qquad 0 < x \leq 1 } \end{array} } \right.
$$

Now

$$
\| f ( x ) - f _ { n } ( x ) \| ^ { 2 } = \int _ { - 1 / n } ^ { 0 } ( - 1 - n x ) ^ { 2 } d x + \int _ { 0 } ^ { 1 / n } ( 1 - n x ) ^ { 2 } d x = { \frac { 2 } { 3 n } } .
$$

And therefore $\operatorname* { l i m } _ { n \to \infty } \| f - f _ { n } \| ^ { 2 } = 0 . f _ { n }$ converges (in norm) to $f$ and is a fortiori a Cauchy sequence.But it cannot converge in norm to a continuous function $g ( x )$ ,for

$$
\left\| { f - g } \right\| = \left\| { f - f _ { n } + f _ { n } - g } \right\| \le \left\| { f - f _ { n } } \right\| + \left\| { g - f _ { n } } \right\| .
$$

If therefore $\| g - f _ { n } \| \to 0$ and $\| f - f _ { n } \| \to 0$ ，then allowing $n  \infty$ ， we obtain

$$
\| f - g \| = 0 . \operatorname { T h u s } , \int _ { - 1 } ^ { 0 } ( 1 + g ( x ) ) ^ { 2 } d x = 0 \quad \mathrm { { a n d } } \int _ { 0 } ^ { 1 } ( g ( x ) - 1 ) ^ { 2 } d x = 0 .
$$

This means that $g ( x ) = - 1$ for $- 1 < x < 0$ and $g ( x ) = 1$ for $0 < x < 1$

We now come to the fundamental theorem of orthonormal (Fourier) expansions.

THEOREM 8.9.1． Let ${ x _ { 1 } } ^ { * }$ ， ${ x _ { 2 } } ^ { * }$ ，...,be a sequence of orthonormal elements in an inner product space $\pmb { X }$ .The sequence may consist of only $^ { a }$ finite number of elements. Appropriate changes are then to be made below. Consider the following seven statements.

(A) The ${ \pmb x } _ { i } ^ { * }$ are closed in $\pmb { X }$ (B) The Fourier series of any element $y \in X$ converges in norm to $_ y$ ；i.e.,

$$
\operatorname* { l i m } _ { n \to \infty } \left\| y - \sum _ { k = 1 } ^ { n } ( y , { x _ { k } } ^ { * } ) { x _ { k } } ^ { * } \right\| = 0 .
$$

(C) Parseval's identity holds. That is,for any $y \in { \pmb X }$ ，

$$
\| y \| ^ { 2 } = ( y , y ) = \sum _ { n = 1 } ^ { \infty } | ( y , x _ { n } ^ { * } ) | ^ { 2 } .
$$

(C') The extended Parseval identity holds. That is,for any $\textstyle { \boldsymbol { \mathscr { x } } } , y \in X$ ，

$$
( x , y ) = \sum _ { n = 1 } ^ { \infty } ( x , x _ { n } { } ^ { * } ) ( x _ { n } { } ^ { * } , y ) .
$$

(D) There is no strictly larger orthonormal system containing ${ x _ { 1 } } ^ { * } , { x _ { 2 } } ^ { * } , \ldots .$ $( \mathbf { E } )$ The elements ${ \pmb x _ { 1 } } ^ { * } , { \pmb x _ { 2 } } ^ { * }$ ...， have the completeness property. That is, $y \in X$ and $( y , x _ { k } ^ { * } ) = 0$ ， $k = 1$ ,2,...,implies $y = 0$

(F) $\mathbf { \nabla } A n$ element of $\pmb { X }$ isdetermined uniquely by its Fourier coefficients.That is,if $( w , x _ { k } ^ { \ast } ) = ( y , x _ { k } ^ { \ast } ) \ k = 1 , 2 , . . . , t h e n \ w = y .$

Then

$$
\mathbf { A }  \mathbf { B }  \mathbf { C }  \mathbf { C } ^ { \prime }  \mathbf { D }  \mathbf { E }  \mathbf { F } .
$$

If $\pmb { X }$ is a complete inner produce space, $\pmb { D }  \pmb { C }$ and all seven statements are equivalent:

$$
\mathbf { A }  \mathbf { B }  \mathbf { C }  \mathbf { C ^ { \prime } }  \mathbf { D }  \mathbf { E }  \mathbf { F } .
$$

We have used $^ { \bullet }  ^ { \bullet \bullet }$ to mean “implies”and $\ "  \ "$ to mean “implies and is implied by.”

Proof:Assume A. Now

$$
\left\| { y - \sum _ { k = 1 } ^ { n } ( y , x _ { k } ^ { \ast } ) { x _ { k } ^ { \ast } } } \right\| \leq \left\| { y - \sum _ { k = 1 } ^ { n } a _ { k } { x _ { k } ^ { \ast } } } \right\|
$$

By A,the last expression can be made $\leq \varepsilon$ If $\mathbf { B }$ holds,we can approximate any element $_ y$ by its Fourier segments；hence ${ \pmb x } _ { k } ^ { * }$ is closed. Thus $\mathbf A  \mathbf B$

By orthogonality,

$$
\left( x - \sum _ { k = 1 } ^ { n } ( x , x _ { k } ^ { * } ) x _ { k } ^ { * } , y - \sum _ { k = 1 } ^ { n } ( y , x _ { k } ^ { * } ) x _ { k } ^ { * } \right) = ( x , y ) - \sum _ { k = 1 } ^ { n } ( x , x _ { k } ^ { * } ) ( x _ { k } ^ { * } , y ) .
$$

By the Schwarz inequality,

$$
( x , y ) - \sum _ { k = 1 } ^ { n } ( x , x _ { k } ^ { * } ) ( x _ { k } ^ { * } , y ) \Bigg | \leq \left\| x - \sum _ { k = 1 } ^ { n } ( x , x _ { k } ^ { * } ) x _ { k } ^ { * } \right\| \cdot \left\| y - \sum _ { k = 1 } ^ { n } ( y , x _ { k } ^ { * } ) x _ { k } ^ { * } \right\|
$$

If B holds,then the right-hand members both approach zero and hence $\mathbf { B } \to \mathbf { C ^ { \prime } }$ .

By selecting ${ \boldsymbol { x } } = { \boldsymbol { y } }$ in $\mathrm { { C ^ { \prime } } }$ it is clear that C holds.Hence $\mathrm { C } ^ { \prime } \to \mathrm { C }$

By Corollary 8.5.3,

$$
0 \leq \left\| y - \sum _ { k = 1 } ^ { n } ( y , x _ { k } ^ { * } ) { x _ { k } ^ { * } } \right\| ^ { 2 } = \| y \| ^ { 2 } - \sum _ { k = 1 } ^ { n } | ( y , x _ { k } ^ { * } ) | ^ { 2 } .
$$

Hence $\mathbf { C } \to \mathbf { B }$ ,and thus $\mathbf { A }  \mathbf { B }  \mathbf { C }  \mathbf { C ^ { \prime } }$

Assume A and suppose that ${ x _ { 1 } } ^ { * } , { x _ { 2 } } ^ { * } , \ldots , w , ( w \neq { x _ { i } } ^ { * } )$ , is also an orthonormal system.This augmented system is also closed in $\pmb { X }$ .Since $\mathbf { A } \to \mathbf { C ^ { \prime } }$ ，

we have both

$$
\begin{array} { l } { \displaystyle \| w \| ^ { 2 } = \sum _ { k = 1 } ^ { \infty } | ( w , x _ { k } ^ { * } ) | ^ { 2 } + ( w , w ) , } \\ { \| w \| ^ { 2 } = \displaystyle \sum _ { k = 1 } ^ { \infty } | ( w , x _ { k } ^ { * } ) | ^ { 2 } } \end{array}
$$

Hence $( w , w ) = 0$ and this is a contradiction since $\| \boldsymbol { w } \| = 1$ . This means :hat $\mathbf { A }  \mathbf { D }$

Suppose there is a $y \in X$ ， $y \neq 0$ such that $( y , x _ { k } ^ { * } ) = 0 , \ k = 1 , 2 , . \ . \ . \ .$ Then, $x _ { 1 } { * } , x _ { 2 } { * } , \ldots , y / \| y \|$ would be an orthonormal system strictly larger than ${ \pmb x } _ { 1 } ^ { \ * } , \ { \pmb x } _ { 2 } ^ { \ * }$ ，....Thus, $\mathbf D  \mathbf E$

Suppose $( w , x _ { k } { } ^ { * } ) = ( y , x _ { k } { } ^ { * } )$ k =1,2,.... Then $( w - y , \ x _ { k } ^ { \ast } ) = 0 \ k =$ 1,2,....Assuming $\mathbf { E }$ ， $w - y = 0$ .Therefore $\mathbf { E }  \mathbf { F }$

If $\mathbf { E }$ were false,we could find a $z \neq 0$ with $( z , x _ { k } { * } ) = 0 \ k = 1 , 2 , . \ . \ . \ .$ For any $_ y$ $( y , x _ { k } ^ { * } ) = ( y + z , x _ { k } ^ { * } ) \ k = 1 , 2 , . . . . \ \mathrm { S o } \ y$ and $y + z$ would be two distinct elements with the same Fourier coefficients. $\mathbf { F }$ would then be false.Therefore $\mathbf { F }  \mathbf { E }$ This completes the chain of implications (8.9.9).

Assume that $\pmb { X }$ is complete.We will show that $\mathbf { F }  \mathbf { B }$ and this will establish the implications (8.9.10).Let $w \in X$ and consider the elements

$$
s _ { n } = \sum _ { k = 1 } ^ { n } ( w , x _ { k } { ^ \ast } ) x _ { k } { ^ \ast } .
$$

ror $\pmb { n } > m$ ， we have $s _ { n } ^ { m , } - s _ { m } = \sum _ { k = m + 1 } ^ { n } ( w , { x _ { k } } ^ { * } ) { x _ { k } } ^ { * }$ so that

$$
\| s _ { n } - s _ { m } \| ^ { 2 } = \sum _ { k = m + 1 } ^ { n } | ( w , x _ { k } ^ { * } ) | ^ { 2 } .
$$

By (8.5.3), $\sum _ { k = 1 } ^ { \infty } | ( w , x _ { k } { ^ * } ) | ^ { 2 } < \infty$ Therefore given an $\pmb { \varepsilon }$ ， we can find an $N ( \varepsilon )$   
such that $\sum _ { = m + 1 } ^ { n } | ( w , x _ { k } { } ^ { * } ) | ^ { 2 } \leq \varepsilon$ for all m, $n \geq N ( \varepsilon )$ . Thus $\left\{ \pmb { s _ { n } } \right\}$ is a Cauchy k   
sequence,and by the assumed completeness of $\pmb { X }$ converges to an element   
$\pmb { \mathscr { s } } \in \pmb { X }$ ：

$$
\operatorname* { l i m } _ { n \to \infty } \| s - s _ { n } \| = 0 .
$$

Let $v$ be fixed and $\textit { \textbf { n } } { \geq } v$ .Then

$$
( s - s _ { n } , x _ { v } { } ^ { * } ) = ( s , x _ { v } { } ^ { * } ) - ( s _ { n } , x _ { v } { } ^ { * } ) = ( s , x _ { v } { } ^ { * } ) - ( w , x _ { v } { } ^ { * } ) .
$$

By the Schwarz inequality,

$$
| ( s , x _ { v } ^ { * } ) - ( w , x _ { v } ^ { * } ) | = | ( s - s _ { n } , x _ { v } ^ { * } ) | \leq \| s - s _ { n } \| \| x _ { v } ^ { * } \| = \| s - s _ { n } \| .
$$

In view of (8.9.l3),we find that

$$
( s , x _ { v } { } ^ { * } ) = ( w , x _ { v } { } ^ { * } ) \quad v = 1 , 2 , . . . .
$$


<!-- chunk 0004: pages 211-280 -->
By $\mathbf { F }$ ,this implies that $s = w$ ,so that (8.9.13) reads

$$
\operatorname* { l i m } _ { n \to \infty } \left\| v - \sum _ { k = 1 } ^ { n } ( w , { x _ { k } } ^ { * } ) { x _ { k } } ^ { * } \right\| = 0 .
$$

But this is precisely $\mathbf { B }$

We remark in passing that Parseval's identity is a generalization of the Theorem of Pythagoras 8.3.1.

The completeness property in (E) may be defined for any set of elements:

DEFINITION 8.9.4. A set of elements $\pmb { S }$ in an inner product space $\pmb { X }$ is complete if

$$
( y , x ) = 0 \quad { \mathrm { f o r ~ a l l ~ } } x \in S
$$

implies $y = 0$

As we have seen,in a complete inner product space,completeness and closure are equivalent concepts and some authors use these words with interchanged meaning.In Chapter XI, the lotion of complete sequence is extended to normed linear spaces and the relation between closure and completeness is probed further.

Ex.10.Let $x$ be $C [ \boldsymbol { a } , \boldsymbol { b } ]$ with $( f , g ) = \int _ { a } ^ { b } f ( x ) g ( x ) \ d x$ . Given an $f \in C [ a , b ]$ and $\varepsilon > 0$ ,we can find constants $a _ { k }$ such that

$$
| f ( x ) - ( a _ { 0 } + a _ { 1 } x + \cdot \cdot \cdot + a _ { n } x ^ { n } ) | \leq \varepsilon \qquad a \leq x \leq b .
$$

By integration,

$$
\int _ { a } ^ { b } ( f ( x ) - ( a _ { 0 } + \cdot \cdot \cdot + a _ { n } x ^ { n } ) ) ^ { 2 } d x \leq \varepsilon ^ { 2 } ( b - a ) .
$$

It follows that the powers $1 , x , x ^ { 2 } , \ldots$ ，are closed in $x$ All statements (A)- ${ \bf \nabla } \cdot ( { \bf F } )$ now follow with the elements ${ x _ { k } } ^ { * }$ interpreted as certain modified Legendre polynomials.In particular,if $f \in C [ a , b ]$ and if

$$
\int _ { a } ^ { b } f ( x ) x ^ { n } d x = 0 \qquad n = 0 , 1 , 2 , \ldots , \quad { \mathrm { t h e n } } \quad f ( x ) \equiv 0 .
$$

Ex. 11.If $x$ is $L ^ { 2 } [ a , b ]$ with the same inner product then the same conclusion holds (See Theorems 11.2.1 and 9.2.2).

Ex.l2. Fourier expansions of continuous functions in terms of Jacobi   
polynomials converge in norm. Parseval's identity holds for such expansions. If $w ( x ) \geq 0 { \mathrm { ~ a n d } } \int _ { a } ^ { b } w ( x ) \ d x < \infty$   
then these results may be extended to the class $L ^ { 2 } [ a , b ; w ]$ of measurable   
functions $\pmb { f }$ for which $\int _ { a } ^ { b } w ( x ) \mid f \mid ^ { 2 } d x < \infty$

THEOREM 8.9.2 (Riesz). Let $\pmb { X }$ be $\pmb { a }$ complete inner product space and let

${ \pmb a } _ { \pmb k }$ be constants such that $\sum _ { k = 1 } ^ { \infty } | a _ { k } | ^ { 2 } < \infty$ Let $\{ x _ { k } ^ { * } \}$ be $^ { \pmb { a } }$ complete orthonormal   
sequence.Then there isa $y \in X$ such that

$$
( y , x _ { k } ^ { * } ) = a _ { k } \quad k = 1 , 2 , . . . .
$$

Prof: Consider the lements $s _ { n } = \sum _ { k = 1 } ^ { n } { a _ { k } { x _ { k } } ^ { * } }$

Now $\| s _ { n } - s _ { m } \| ^ { 2 } = \sum _ { k = m + 1 } ^ { n } | a _ { k } | ^ { 2 }$ In view of $\sum _ { k = 1 } ^ { \infty } | a _ { k } | ^ { 2 } < \infty , \left\{ \mathscr { s } _ { n } \right\}$ is a Cauchy sequence,and there is a $_ y$ such that $\operatorname* { l i m } _ { n \to \infty } \| y - s _ { n } \| = 0$ .With $\pmb { k }$ fixed and $\pmb { n } \geq k$ ，

$$
\| y - s _ { n } \| = \| y - s _ { n } \| \| x _ { k } ^ { * } \| \geq | ( y - s _ { n } , x _ { k } ^ { * } ) | = | ( y , x _ { k } ^ { * } ) - a _ { k } | .
$$

Allowing $\pmb { n }  \infty$ ,we obtain (8.9.15).

8.10 Further Geometrical Properties of Complete Inner Product Spaces. We have seen in Theorem 8.5.l that there is a minimum distance from a given element to a linear manifold.How can this be extended to more general subsets ? Theorem 8.lo.1 provides a sufficient condition of great importance.

THEOREM 8.10.1． Let $\pmb { X }$ be $^ { \pmb { a } }$ complete inner product space. Let $M$ be $^ { \pmb { a } }$ closed (i.e., topologically),convex,and nonempty subset of $\pmb { X }$ Let $y \in X$ and set

$$
d = \operatorname* { i n f } _ { x \in M } \| y - x \| .
$$

Then there is a unique $\pmb { x _ { 0 } }$ in $M$ such that

$$
\lVert y - x _ { 0 } \rVert = d .
$$

![](../chunks/Interpolation and Approximation (Philip J. Davis) (z-library.sk, 1lib.sk, z-lib.sk)_part_0004_pages_0211-0280/auto/images/0f430966813b6d854a223d8c826537346f5e32d3135094c387e287c0ff1a52a9.jpg)  
Figure 8.10.1.

Proof:By (8.lo.l) we can find a sequence of elements ${ \pmb x } _ { \pmb n }$ in $M$ such that

$$
\operatorname* { l i m } _ { n \to \infty } \| y - x _ { n } \| = d .
$$

The parallelogram theorem (Theorem 8.1.3) tells us that

$$
\begin{array} { c } { \| x _ { m } - x _ { n } \| ^ { 2 } = 2 \| x _ { m } - y \| ^ { 2 } + 2 \| x _ { n } - y \| ^ { 2 } - \| 2 y - x _ { m } - x _ { n } \| ^ { 2 } } \\ { = 2 \| x _ { m } - y \| ^ { 2 } + 2 \| x _ { n } - y \| ^ { 2 } - 4 \| y - \frac { 1 } { 2 } ( x _ { m } + x _ { n } ) \| ^ { 2 } . } \end{array}
$$

$M$ is convex; hence $\pmb { \Sigma } ( \pmb { x } _ { m } + \pmb { x } _ { n } )$ is in $M$ and $\| y - \frac { 1 } { 2 } ( x _ { m } + x _ { n } ) \| ^ { 2 } \geq d ^ { 2 }$ Therefore,

$$
\| x _ { m } - x _ { n } \| ^ { 2 } \leq 2 \| y - x _ { m } \| ^ { 2 } + 2 \| y - x _ { n } \| ^ { 2 } - 4 d ^ { 2 } .
$$

In view of (8.10.3), $\| { \pmb x } _ { m } - { \pmb x } _ { n } \| ^ { 2 } \to 0$ as $\pmb { m }$ ， $n \to \infty$ . This means that $\{ x _ { m } \}$ is a Cauchy sequence.Since $\pmb { X }$ is complete,there is an $\pmb { x _ { 0 } }$ in $\pmb { X }$ such that $\| { \pmb x } _ { m } - { \pmb x } _ { 0 } \|  0$ .Since $M$ is closed, $\pmb { x _ { 0 } }$ isin $M$ . Now

$$
\| y - x _ { 0 } \| \leq \| y - x _ { n } \| + \| x _ { n } - x _ { 0 } \| \to d + 0 = d .
$$

On the other hand,from (8.10.1), $\| y - x _ { 0 } \| \geq d$ .Therefore $\| y - x _ { 0 } \| = d .$ Suppose we have $\pmb { x _ { 0 } }$ and $\pmb { x _ { 1 } }$ with $\| y - x _ { 0 } \| = \| y - x _ { 1 } \| = d$ Since $M$ is convex, $\frac { 1 } { 2 } ( x _ { 0 } + x _ { 1 } )$ is in $M$ Hence,

$$
\begin{array} { l } { d \leq \| y - \frac { 1 } { 2 } ( x _ { 0 } + x _ { 1 } ) \| = \| \frac { 1 } { 2 } y - \frac { 1 } { 2 } x _ { 0 } + \frac { 1 } { 2 } y - \frac { 1 } { 2 } x _ { 1 } \| } \\ { \quad \leq \frac { 1 } { 2 } \| y - x _ { 0 } \| + \frac { 1 } { 2 } \| y - x _ { 1 } \| = \displaystyle \frac { d } { 2 } + \frac { d } { 2 } = d . } \end{array}
$$

Therefore $\lVert y - \frac { 1 } { 2 } ( x _ { 0 } + x _ { 1 } ) \rVert = d$ By the parallelogram law,

$$
\begin{array} { c } { { \| x _ { 0 } - x _ { 1 } \| ^ { 2 } = 2 \ \| y - x _ { 0 } \| ^ { 2 } + 2 \ \| y - x _ { 1 } \| ^ { 2 } - 4 \ \| y - \frac { 1 } { 2 } ( x _ { 0 } + x _ { 1 } ) \| ^ { 2 } } } \\ { { { } } } \\ { { = 2 d ^ { 2 } + 2 d ^ { 2 } - 4 d ^ { 2 } = 0 . } } \end{array}
$$

Therefore ${ \pmb x _ { 0 } } = { \pmb x _ { 1 } }$

Ex.1．In the plane,let $\pmb { M }$ designate a nonempty，closed,convex set of points. If $\mathbfit { \Delta } _ { P }$ is a point not contained in $M$ ,there is a unique segment of minimum length connecting $\pmb { P }$ and $\pmb { M }$

THEOREM 8.10.2．Let $\pmb { X }$ be $^ { \pmb { a } }$ complete inner product space and let M be a closed linear subspace that is not the whole of $\pmb { X }$ .Then there exists $\pmb { a }$ nonzero element z ⊥ $M$ ,i.e., $( z , y ) = 0$ for all $y \in M$

Proof: Let w $\notin M$ Set $d = \operatorname* { i n f } _ { y \in M } \| w - y \|$ .By Theorem 8.10.l,we can find a ${ \pmb y _ { 0 } }$ in $\pmb { M }$ with $\| w - y _ { 0 } \| = d$ Let $z = w - y _ { 0 }$ . Now $z \neq 0$ ，otherwise ${ w = y _ { 0 } \in M }$ Since $\pmb { M }$ is linear, $y _ { 0 } + C y$ is in $M$ for all $y \in M$ and all $\boldsymbol { c }$ Hence, $d \leq \| w - y _ { 0 } - C y \| = \| z - C y \|$ .Then, $\| z - C y \| ^ { 2 } - \| z \| ^ { 2 } \geq 0 .$ This means that $| C | ^ { 2 } \ \| y \| ^ { 2 } - C ( y , z ) - { \bar { C } } ( z , y ) \geq 0$ ，In particular，select ${ \boldsymbol { C } } =$ ${ \pmb \sigma } ( z , y )$ where $\pmb { \sigma }$ is real. Then,

$$
| ( z , y ) | ^ { 2 } \left\{ \sigma ^ { 2 } \| y \| ^ { 2 } - 2 \sigma \right\} \geq 0 \quad { \mathrm { f o r ~ a l l ~ } } \sigma .
$$

But for $\pmb { \sigma } > 0$ and sufficiently small, $\sigma ^ { 2 } \parallel y \parallel ^ { 2 } - 2 \sigma$ is negative. Hence $( z , y ) = 0$

CoROLLARy 8.lO.3. The minimal element extending from a given element to a closed linear subspace is perpendicular to the subspace.

Here is a second application of Theorem 8.l0.l more directly related to questions of approximation theory.

THEOREM 8.10.4. Let $M$ designate the set of polynomials of degree $\leq n$ that are convex on $[ \pmb { a } , \pmb { b } ]$ . Let $f ( x ) \in L ^ { 2 } [ a , b ]$ .Then the problem

$$
\operatorname* { m i n } _ { p \in M } \| f - p \| , \quad \| f \| ^ { 2 } = \int _ { a } ^ { b } \lvert f \rvert ^ { 2 } d x ,
$$

possesses a unique solution.

Proof:A polynomial ${ \pmb p } ( { \pmb x } )$ is convex on $[ a , b ]$ if and only if $\pmb { p } ^ { \prime \prime } ( \pmb { x } ) \geq 0$ there. If $\pmb { p }$ and $\pmb q$ are convex on $[ a , b ]$ ，then $t p ( x ) + ( 1 - t ) q ( x )$ is also convex on $[ a , b ]$ for $0 \leq t \leq 1$ ,inasmuch as $t p ^ { \prime \prime } + ( 1 - t ) q ^ { \prime \prime } \geq 0$ The set $M$ is therefore convex.

We show next that $\pmb { M }$ is a closed subset of $L ^ { 2 } [ a , b ]$ . Let $\pmb { \mathscr { p } _ { k } } ( \pmb { \mathscr { x } } ) \in \pmb { M }$ converge to $f ( x ) \in L ^ { 2 } [ a , b ]$ ； i.e.,let $\operatorname* { l i m } _ { k \to \infty } \int _ { a } ^ { b } | f ( x ) - p _ { k } ( x ) | ^ { 2 } d x = 0$ Let ${ \pmb q } ( { \pmb x } )$ be the best approximation to $\pmb { f } ( \pmb { x } )$ in $\mathcal { P } _ { n }$ (Cf. Cor.8.5.2). Then,

$$
\begin{array} { l } { 0 \leq \displaystyle \int _ { a } ^ { b } | f ( x ) - q ( x ) | ^ { 2 } d x \leq \int _ { a } ^ { b } | f ( x ) - p _ { k } ( x ) | ^ { 2 } d x . } \\ { \infty \mathrm { ~ w e ~ h a v e } \displaystyle \int _ { a } ^ { b } | f ( x ) - q ( x ) | ^ { 2 } d x = 0 , \mathrm { ~ s o ~ t h a t ~ } . } \end{array}
$$

Allowing $k \to \infty$ $f ( { \pmb x } ) = { \pmb q } ( { \pmb x } )$ is in $\mathcal { P } _ { n }$ ·

Let ${ P _ { 0 } } ^ { * } ( x ) , \ { P _ { 1 } } ^ { * } ( x ) , \ . \ . \ . \ , \ { P _ { n } } ^ { * } ( x )$ designate the orthonormal polynomials for $[ a , b ]$ . Then,

$$
f ( x ) - { p _ { k } } ( x ) \equiv a _ { 0 k } { P _ { 0 } } ^ { * } ( x ) + \dots + a _ { n k } { P _ { n } } ^ { * } ( x ) , k = 1 , 2 , \dots ,
$$

for some constants $\pmb { a } _ { i k }$ and hence,

$$
\begin{array} { l } { \displaystyle \int _ { a } ^ { b } | f ( x ) - p _ { k } ( x ) | ^ { 2 } d x = \sum _ { i = 0 } ^ { n } | a _ { i k } | ^ { 2 } \to 0 . } \\ { \displaystyle \operatorname* { l i m } _ { k \to \infty } a _ { i k } = 0 , i = 0 , 1 , . . . , n . } \end{array}
$$

Thus,

Now $\left| f ( z ) - p _ { k } ( z ) \right| \leq \sum _ { i = 0 } ^ { n } \left| a _ { i k } \right| \left| P _ { i } { } ^ { * } ( z ) \right|$ ； hence over any bounded region in the complex plane $p _ { k } ( z ) \to f ( z )$ uniformly.Hence ${ p _ { k } } ^ { \prime \prime } ( z )  f ^ { \prime \prime } ( z )$ uniformly there and since ${ p _ { k } } ^ { \prime \prime } ( x ) \geq 0$ on $[ a , b ]$ ,it follows that $f ^ { \prime \prime } ( x ) \geq 0$ there.Thus $\pmb { M }$ is closed.The Theorem now follows by an application of Theorem 8.10.1. We refer to Theorem 9.2.2 for the completeness of $L ^ { 2 } [ a , b ]$

# NOTES ON CHAPTER VIII

General works that have been found useful include Halmos [l] and Aronszajn[l].Also the references cited in Chapter 7.

8.1 For spaces that do not satisfy the positivity requirement (8.1.1)(d), see Synge [l],Part III. 8.2The Euclidean geometry of $\pmb { n }$ dimensions is developed in Sommerville [1]. 8.5For additional examples of Tschebyscheff expansions,see Murnaghan and Wrench [2],Clenshaw [l].Davis and Rabinowitz [2] presents an extensive survey of the applications of least square methods to numerical analysis. 8.7-8.8 Kowalewski [2] pp.223-229.Gantmacher [l],Vol.I.Kaczmarz and Steinhaus [l] pp.73-78,Szego[1] pp.23-27. 8.9-8.10 Banach [l] Chap.IV,Kaczmarcz and Steinhaus [l], Chap. II. Further discussion of Theorem 8.9.1 is in Olmstead [1].

# PROBLEMS

$1 . \mathrm { ~ I f ~ } - \infty < \lambda , \mu < \infty , \mathrm { t h e n ~ } \operatorname* { l i m } _ { T \to \infty } \frac { 1 } { 2 T } \int _ { - T } ^ { T } \cos { \lambda x } \cos { \mu x } d x = 0 , \lambda \neq \mu .$ What is the value of the limit for $\lambda = \mu ?$

2.If $x$ is a real inner product space $\| x + y \| = \| x - y \|$ if and only if $( x , y ) = 0$ What if $x$ is a complex inner product space?

3. In a real inner product space $\| x \| = \| y \|$ implies that

$$
( x , x \ : - \ : y ) = ( y , y \ : - \ : x ) .
$$

Give a geometric interpretation.

4. If $x$ is a real inner product space, $( x , y ) = 0$ if and only if $\| a x + y \| \geq \| y \|$ for all real $^ { a }$

5.If $x _ { 1 }$ and $x _ { \mathbf { 2 } }$ are orthonormal, then ${ \boldsymbol { x } } _ { 1 } ~ + ~ { \boldsymbol { x } } _ { 2 }$ and $x _ { 1 } \ - \ x _ { 2 }$ are orthogonal. Geometrical interpretation?

6. Let $\| x _ { i } \| = 1 , i = 1 , 2 , \ldots , n . \left\| x _ { i } - x _ { j } \right\| = 1 , i \neq j .$ Determine the angle between $x _ { i }$ and $x _ { j } .$ Interpretation in $R _ { 2 }$ and $R _ { 3 }$ ？

7.Prove that an inner product space is strictly convex.

8.In a real inner product space $( x , y ) = { \textstyle { \frac { 1 } { 4 } } } [ \| x + y \| ^ { 2 } - \| x - y \| ^ { 2 } ]$ In a complex inner product space，Re $( x , y ) = \textstyle { \frac { 1 } { 4 } } [ \| x + y \| ^ { 2 } - \| x - y \| ^ { 2 } ]$ ${ \bf I m } ( x , y ) =$ $- { \frac { 1 } { 4 } } [ \| i x + y \| ^ { 2 } - \| i x - y \| ^ { 2 } ]$

9.Give an example of a normed linear space in which the parallelogram theorem fails.

10.In $O ^ { \mathbf { 1 } } [ a , b ]$ define

$$
\begin{array} { l } { \displaystyle ( f , g ) = \int _ { a } ^ { b } f ^ { \prime } ( x ) g ^ { \prime } ( x ) d x } \\ { \displaystyle ( f , g ) = \int _ { a } ^ { b } f ^ { \prime } ( x ) g ^ { \prime } ( x ) d x + f ( a ) g ( a ) . } \end{array}
$$

Which of these is an inner product?

11. Let $X$ be a real Minkowski plane with points $\pmb { P }$ .It is an inner product space if and only if the locus $\| \cal { P } \| = 1$ is an ellipse.

12.Estimate $\int _ { 0 } ^ { 1 } { \frac { x ^ { n } d x } { 1 + x } }$ from above by the Schwarz inequality.Estimate from   
below and above by using the mean value theorem for integrals.Compare with   
the exact answer for $\scriptstyle n \ = \ 6$

13.In the case of a complex inner product space two definitions of angle are possible: (1） cos $\phi = { \frac { | ( x , y ) | } { \left\| x \right\| \left\| y \right\| } }$ (2) $\cos \phi = { \frac { \mathbf { R e } \left( x , y \right) } { \left\| x \right\| \left\| y \right\| } }$ According to (1), $\phi = \pi / 2$ if and only if $( x , y ) = 0$ ，but the law of cosines does not hold.According to (2), the reverse is true.

14. Let $X$ be an inner product space and $x _ { 1 } , \ldots , x _ { n }$ be $\mathscr { n }$ independent elements. Introduce $L _ { k } ( x ) = ( x , x _ { k } )$ and use the $_ { L U }$ decomposition of $( ( x _ { i } , ~ x _ { j } ) )$ (2.6.19) to derive the orthonormalized $x _ { 1 } { * } , x _ { 2 } { * } , \ldots , x _ { n } { * }$

15. Let $\mathscr { n } > 2$ .“Solve” the overdetermined system of real equations in $x , \ y$

$$
\begin{array} { r } { a _ { 1 } x \ + \ b _ { 1 } y \ = \ c _ { 1 } } \\ { . } \\ { . } \\ { . } \end{array}
$$

$$
a _ { n } x + b _ { n } y = c _ { n }
$$

by minimizing $\sum _ { i = 1 } ^ { n } ( c _ { i } - a _ { i } x - b _ { i } y ) ^ { 2 }$

16.Find the least square polynomial approximations of degrees O,2,and 4 to $| x |$ over $[ - 1 , 1 ]$

17.Approximate $x ^ { 2 }$ in $L ^ { 2 } [ 0 , 1 ]$ by a combination of ${ \mathbf { 1 } } , x$ ，Bya combination of $x ^ { 1 0 0 }$ ， $x ^ { 1 0 1 }$ .Compare the answers.

18.In an inner product space,minimize

$$
\| x _ { 1 } - x \| ^ { 2 } + \| x _ { 2 } - x \| ^ { 2 } + \cdot \cdot \cdot + \| x _ { n } - x \| ^ { 2 }
$$

where $_ { \pmb { x } }$ is a linear combination of $x _ { 1 } , \ldots , x _ { n }$ Interpret geometrically.

$_ y$ “relative errors,” $\sum _ { j = 1 } ^ { n } \left[ { \frac { a _ { j } - y } { y } } \right] ^ { 2 }$ ,is $y = \sum _ { j = 1 } ^ { n } { a _ { j } } ^ { 2 } \left/ \sum _ { j = 1 } ^ { n } a _ { j } . \right.$

20.Let a triangle $\pmb { T }$ have sides $a , b , c$ .If $_ { P }$ is a point in the plane,denote by $x , y , z ,$ ,the distance from $\mathbfit { \Delta } \mathcal { P }$ to the sides.What position of $\pmb { P }$ minimizes $x + y + z ?$

21.With the notationof Problem 20,show that there isa point $P _ { L }$ such that ${ \frac { x } { a } } = { \frac { y } { b } } = { \frac { z } { c } }$ . This is known as the Lemoine Point of the triangle. Show that this point minimizes $x ^ { 2 } + y ^ { 2 } + z ^ { 2 }$ .Hint: Use the Lagrange identity

$$
\begin{array} { l } { { ( a ^ { 2 } + b ^ { 2 } + c ^ { 2 } ) ( x ^ { 2 } + y ^ { 2 } + z ^ { 2 } ) = ( a x + b y + c z ) ^ { 2 } \nonumber } } \\ { { \nonumber } } \\ { { \qquad + ( a y - b x ) ^ { 2 } + ( b z - c y ) ^ { 2 } + ( c x - a z ) ^ { 2 } . } } \end{array}
$$

22. In $\scriptstyle { R _ { n } }$ ， $\| y - A x \| ^ { 2 }$ is minimized for $x = x _ { 1 }$ if and only if $A ^ { \prime } A x _ { 1 } = A ^ { \prime } y$

23. Given $0 < x _ { 1 } < x _ { 2 } < \cdot \cdot \cdot < x _ { n } \leq 1 ;$ ： $f _ { k } ( x ) = 1 , 0 \leq x \leq x _ { k } ;$ ： $f _ { k } ( x ) = 0$ ， $x _ { k } < x \le 1$ ； $k = 1 , 2 , \ldots , n$ Compute $G ( f _ { 1 } , f _ { 2 } , \ldots , f _ { n } )$ ·

24. If $\boldsymbol { x } _ { i }$ are normal: $\| { \pmb x } _ { i } \| = { \bf 1 }$ ， prove that the sequence $\mu _ { n } = g ( x _ { 1 } , x _ { 2 } , . ~ . ~ . ~ , x _ { n } )$ is nonincreasing.

25.Let the matrix $G ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } )$ have rank $\pmb { r }$ Then $\pmb { r }$ of the elements $x _ { 1 } , \ldots , x _ { n }$ are linearly independent and $\textit { \textbf { n } } - \textit { \textbf { r } }$ elements are linear combinations of these.

26. Prove that Hadamard's determinant inequality is an equality if and only if the rows or columns of $_ D$ are orthogonal.

27.Prove that the $_ n$ -dimensional volume, $V _ { n }$ ，of the regular $\pmb { n }$ -simplex of side l (generalization to $\pmb { n }$ dimensions of the equilateral triangle) is given by

$$
V _ { n } = { \frac { 1 } { n ! } } { \sqrt { \frac { n + 1 } { 2 ^ { n } } } } .
$$

28.Let $x$ be an inner product space and $x _ { 1 } , \ldots , x _ { n }$ be $\pmb { n }$ independent elements. Then, $g ( y , x _ { 1 } , \dots , x _ { n } ) = | ( y , z ) | ^ { 2 }$ for all $_ y$ ,and where $\pmb { z }$ depends only on $x _ { 1 } , \ldots , x _ { n } ,$ if and only if the dimension of $X \leq n + 1$ The $\pmb { z }$ is unique.If the dimension of $\pmb { X } < \pmb { n } + \pmb { 1 } , \pmb { z } = \pmb { 0 }$ ，The element $\pmb { z }$ is known as the Grassman outer product of $x _ { 1 } , \ldots , x _ { n }$

29.Use the result of the last problem to generalize the formula of analytic geometry for the distance from a point to a line. In $R _ { n + 1 }$ ,let $x _ { 1 } , \ldots , x _ { n }$ be independent.Then,the distance $^ d$ from $_ y$ to the hyperplane spanned by $x _ { 1 } , \ldots , x _ { n }$ is given by $d = { \frac { \left| ( y , z ) \right| } { \left\| z \right\| } }$ .Check the case $\textbf { \em n } = \textbf { 2 }$

30.Suppose there is a real valued function of $\pmb { n }$ elements of an inner product space $V ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } )$ such that (1) $V ( x _ { 1 } , \ldots , x _ { n } ) = \| x _ { 1 } \| \ \| x _ { 2 } \| \cdot \cdot \cdot \| x _ { n } \|$ whenever $x _ { 1 } , \ldots , x _ { n }$ are orthogonal. (2) $V ( x _ { 1 } , \ldots , x _ { j } , \ldots , x _ { k } , \ldots , x _ { n } ) = V ( x _ { 1 } , \ldots , x _ { } , $ $x _ { j } + \sigma x _ { k } , . . . , x _ { k } , . . . , x _ { n } )$ for all constants $\pmb { \sigma }$ and all $j , k \left( j \neq k \right)$ .Prove that $V ( x _ { 1 } , \ldots , x _ { n } ) = g ^ { \frac { 1 } { 2 } } ( x _ { 1 } , \ldots , x _ { n } )$ ·

31.Give a geometric interpretation of Hadamard's Inequality and of inequality (8.8.1)(e).

32. Let $\pmb { g } ( \pmb { x } ) \in C ^ { \pmb { 2 } } [ \mathbf { 0 } , \mathbf { 1 } ]$ and suppose that $g ^ { \prime \prime } ( x ) < 0$ at some point $x \in [ 0 , 1 ]$ Suppose that a polynomial $p ( x )$ is such that $| g ( x ) - p ( x ) | \leq \varepsilon$ for $0 \leq x \leq 1$ Forεsufficiently small,there is a point $\eta$ in [0,1] where $p ^ { \prime } ( \eta ) < 0$ ·

33.What is the implication of the previous exercise about the possibility of uniform convex polynomial approximations?

34.Let ${ \mathcal P _ { \pmb { n } } }$ designate a normed linear space of polynomials of degree $\leq n$ .If $p _ { k } ( z )$ is a sequence of elements of ${ \mathcal { P } } _ { n }$ for which $\| p _ { k } \| \to 0$ ,then $p _ { \star } ( z )  0$ uniformly on any bounded set.

35.If $x$ satisfies all conditions for an inner product space,except that $( { \pmb x } , { \pmb x } ) = { \pmb 0 }$ does not necessarily imply ${ \boldsymbol { x } } = \mathbf { 0 } , { \boldsymbol { X } }$ is called an indefinite inner product space.Give examples of such a space.How much of the present chapter is valid for such spaces?

# CHAPTERIX

# Hilbert Space

9.1Introduction. Hilbert space is the natural generalization to an infinite number of dimensions of the real or complex Euclidean spaces $\scriptstyle { R _ { n } }$ and $C _ { n }$ .There are many advantages to be gained from working ina Hilbert space.In the first place,our spatial intuition acquired in 1,2,and 3 dimensions carries over to some extent,and theorems and processes can be“seen” geometrically as well as analytically.In the second place,the norm in the space is associated with a quadratic expression，so that the processes of minimization lead to linear problems.Finally,all (separable) Hilbert spaces are abstractly equivalent to one another.This means that the theorems established have wide application.

DEFINIrion 9.l.1. A complete inner product space will be called a Hilbert space, $\pmb { H }$ ,if the following additional requirements are fulfilled

(a) $\pmb { H }$ is infinite dimensional; that is,given any integer $\pmb { n }$ ，we can find $\pmb { n }$ independent elements. (b) There is a closed (or complete) sequence of elements in $\pmb { H }$

We have already observed in Chapter VIII that inner product spaces have a good bit of geometry associated with them.The requirement that $\pmb { H }$ be complete means that all the conditions $\mathbf { A } { - } \mathbf { F }$ of Theorem 8.9.l are equivalent.

Condition (9.1.1)(a) provides $\pmb { H }$ with more dimensions than any $\scriptstyle { R _ { n } }$ while condition (b) restricts the number of dimensions to being countably infinite. These conditions are largely a matter of convenience,and the practice of authors with respect to them varies.

A Hilbert space is,at the very first level,a linear space.This linear space may be either real or complex.Accordingly,the Hilbert Space is spoken of as real or complex.

If $\pmb { X }$ is an inner product space and the sequence $x _ { 1 } , x _ { 2 } , \ldots$ , is complete, we can find a subsequence $x _ { k _ { 1 } } , x _ { k _ { 2 } } , \ldots$ (possibly finite) that is both complete and independent.For,beginning with the first nonzero element,inspect the sequence and strike out the first element that depends upon the previous elements.Inspect the subsequence that remains and do the same.Proceeding in this way we obtain a subsequence $x _ { k _ { 1 } } , x _ { k _ { 2 } } , \dotsc .$ of independent elements. Moreover,any element $\pmb { x } _ { q }$ struck from the list is a linear combination of a certain number of elements of the subsequence: $x _ { q } = a _ { 1 } x _ { k _ { 1 } } + \cdot \cdot \cdot + a _ { p } x _ { k _ { p } }$

![](../chunks/Interpolation and Approximation (Philip J. Davis) (z-library.sk, 1lib.sk, z-lib.sk)_part_0004_pages_0211-0280/auto/images/494618cabf8729ba894489ed31ca80cdd70258a73373c03a0f151fd7863fcd1f.jpg)  
Figure 9.1.1 The Hierarchy of Linear Spaces.

Hence, $( y , x _ { k _ { i } } ) = 0 , i = 1 , 2 , . . .$ ,implies $( y , x _ { i } ) = 0$ ， $i = 1$ ,2,.... This means that the subsequence is itself complete.

If $\pmb { X }$ is an infinite dimensional complete inner product space,a finite sequence $x _ { 1 } , \ldots , x _ { n }$ cannot be complete.For,otherwise we may suppose it to be independent,as above,and orthonormalize it to obtain a complete orthonormal sequence $x _ { 1 } { } ^ { * } , \ldots , x _ { n } { } ^ { * }$ .In view of (8.9.6),any element $_ y$ equals $\sum _ { k = 1 } ^ { n } ( y , x _ { k } \ast ) x _ { k } \ast$ so that there cannot be $n + 1$ independent elements.

In view of this discussion and Theorem 8.3.3, condition (9.1.1) may be replaced by

There is a complete orthonormal infinite sequence of elements in $H$ ·

Recall that a metric space $\pmb { S }$ is separable if there is a denumerable dense set of elements.Condition (9.1.1)(b) implies that $H$ is separable.For let $\{ x _ { i } ^ { * } \}$ be a complete orthonormal sequence.The finite linear combinations of the $x _ { i } { } ^ { * }$ with rational (real or complex) coefficients is a denumerable set. Given $y \in H$ and $\varepsilon > 0$ ,then by Theorem 8.9.l(B),for sufficiently large $\pmb { n }$ ， $\left\| y - \sum _ { k = 1 } ^ { n } ( y , { x _ { k } } ^ { * } ) { x _ { k } } ^ { * } \right\| < \varepsilon / 2$ If rationals $r _ { k }$ are sletetsg ae

$$
\sum _ { k = 1 } ^ { n } | r _ { k } - ( y , { x _ { k } } ^ { * } ) | ^ { 2 } < \varepsilon ^ { 2 } / 4 ,
$$

then

$$
\left\| \sum _ { k = 1 } ^ { n } ( y , { x _ { k } } ^ { * } ) { x _ { k } } ^ { * } - \sum _ { k = 1 } ^ { n } { r _ { k } { x _ { k } } ^ { * } } \right\| ^ { 2 } < \varepsilon ^ { 2 } / 4 .
$$

Hence $\left\| { y - \sum _ { k = 1 } ^ { n } { r _ { k } } x _ { k } } ^ { * } \right\| < \varepsilon .$ Thi aproximat too $_ y$ is one f hederuherable set.

Hilbert spaces as defined here are sometimes called separable Hilbert spaces,but we shall omit the qualifying term.

The following lemma is of occasional use.

LEMMA 9.1.1． Let ${ x _ { 1 } } ^ { * } , \ldots , { x _ { n } } ^ { * }$ be $\pmb { n }$ orthonormal elements in a Hilbert space. Wecan augmentheseelementsby $x _ { n + 1 } ^ { * } , x _ { n + 2 } ^ { * } , . . .$ such that ${ x _ { 1 } } ^ { * }$ $^ { * } , x _ { 2 } ^ { * } , \ldots ,$ iscomplete and orthonormal.

Proof:The Hilbert space has a complete sequence $y _ { 1 } , y _ { 2 } , \ldots$ The sequence $x _ { 1 } { } ^ { * } , \ldots , x _ { n } { } ^ { * }$ ， $y _ { 1 } , y _ { 2 } , \ldots$ ， is obviously complete (since $( y , y _ { i } ) = 0$ ， $i = 1 , 2 , \dots .$ ，already implies $y = 0$ .By the process described above，we can extract a subsequence that is complete and independent.The subsequence will begin with ${ x _ { 1 } } ^ { * } , \ldots , { x _ { n } } ^ { * }$ since these elements are independent. Orthonormalizing this subsequence,we obtain ${ x _ { 1 } } ^ { * } , \ldots , { x _ { n } } ^ { * }$ over again, plus additional elements that we call $x _ { n + 1 } ^ { * } , x _ { n + 2 } ^ { * } , \ldots .$

9.2 Three Hilbert Spaces. There are many known examples of Hilbert spaces,but we limit our presentation to three.

THEOREM 9.2.1. The set of all infinite sequences $\{ a _ { i } \}$ for which

$$
\sum _ { i = 1 } ^ { \infty } | a _ { i } | ^ { 2 } < \infty ,
$$

augmented by the usual defnitions for adition and scalar products and by

$$
( \pmb { a } , \pmb { b } ) = \sum _ { i = 1 } ^ { \infty } a _ { i } \overline { { b _ { i } } } , \pmb { a } = \{ \pmb { a } _ { i } \} , \pmb { b } = \{ b _ { i } \} ,
$$

as the definition of an inner product,constitutes $\pmb { a }$ Hilbert space.

It is called the sequential Hilbert space and is designated by $\ell ^ { 2 }$

Proof:We have already observed in Ex. 5,7.2, that $\ell ^ { 2 }$ is a normed linear space. For any two elements $a , b$ of $\ell ^ { 2 }$ ,we have by (7.2.9)

$$
\sum _ { i = 1 } ^ { n } | a _ { i } \overline { { b } } _ { i } | \leq \bigg ( \sum _ { i = 1 } ^ { n } | a _ { i } | ^ { 2 } \bigg ) ^ { \frac { 1 } { 2 } } \bigg ( \sum _ { i = 1 } ^ { n } | b _ { i } | ^ { 2 } \bigg ) ^ { \frac { 1 } { 2 } } .
$$

Hence, $\sum _ { i = 1 } ^ { \infty } \vert a _ { i } \overline { { b } } _ { i } \vert < \infty$ and $\sum _ { i = 1 } ^ { \infty } a _ { i } \bar { b _ { i } }$ converges. The expression $( a , b )$ is therefore defined for all $a , b \in \ell ^ { 2 }$ ,and it is now a trivial computation to show that it satisfies the requirements (8.1.l) (a)-(d) for an inner product.

We prove next that the space is complete. Let $a ^ { ( n ) } = \{ a _ { i } ^ { ( n ) } \}$ be a Cauchy sequence.That is,let

$$
\operatorname * { l i m } _ { m , n \to \infty } \| a ^ { ( m ) } - a ^ { ( n ) } \| ^ { 2 } = \operatorname * { l i m } _ { m , n \to \infty } \sum _ { i = 1 } ^ { \infty } | a _ { i } ^ { ( m ) } - a _ { i } ^ { ( n ) } | ^ { 2 } = 0 .
$$

For each fixed subscript $\mathbf { \chi } _ { i }$ ， then, we have $\operatorname* { l i m } _ { m , n \to \infty } | a _ { i } ^ { ( m ) } - a _ { i } ^ { ( n ) } | = 0$ Each of the sequences ${ \pmb a } _ { i } ^ { ( 1 ) } , { \pmb a } _ { i } ^ { ( 2 ) } , \dots .$ ,is therefore a Cauchy sequence of real or coniplex numbers,and by the completeness of these spaces,possesses a limit:

$$
\operatorname * { l i m } _ { m  \infty } a _ { i } ^ { ( m ) } = a _ { i } , i = 1 , 2 , 3 \cdots .
$$

For each integer $\pmb { k }$ ,set

$$
\sigma _ { k } { } ^ { 2 } = \operatorname* { s u p } _ { m , n \geq k } \| a ^ { ( m ) } - a ^ { ( n ) } \| ^ { 2 } .
$$

By (9.2.3), we have

$$
\operatorname* { l i m } _ { k  \infty } \sigma _ { k } = 0 .
$$

Now for $\pmb { N }$ arbitrary and for all $m \geq n$ ,we have

$$
\sum _ { i = 1 } ^ { N } | a _ { i } ^ { ( m ) } - a _ { i } ^ { ( n ) } | ^ { 2 } \leq \sum _ { i = 1 } ^ { \infty } | a _ { i } ^ { ( m ) } - a _ { i } ^ { ( n ) } | ^ { 2 } = \| a ^ { ( m ) } - a ^ { ( n ) } \| ^ { 2 } \leq { \sigma _ { n } } ^ { 2 } .
$$

In (9.2.7) keep $\pmb { N }$ and $\pmb { n }$ fixed and let $m \to \infty$ . Since we are dealing with a finite sum,we have

$$
\sum _ { i = 1 } ^ { N } | a _ { i } - a _ { i } ^ { ( n ) } | ^ { 2 } \leq { \sigma _ { n } } ^ { 2 } .
$$

By Minkowski's inequality,

$$
\begin{array} { r l } & { \biggl ( \displaystyle \sum _ { i = 1 } ^ { N } | a _ { i } | ^ { 2 } \biggr ) ^ { \frac { 1 } { 2 } } \leq \biggl ( \displaystyle \sum _ { i = 1 } ^ { N } | a _ { i } ^ { ( n ) } | ^ { 2 } \biggr ) ^ { \frac { 1 } { 2 } } + \biggl ( \displaystyle \sum _ { i = 1 } ^ { N } | a _ { i } - a _ { i } ^ { ( n ) } | ^ { 2 } \biggr ) ^ { \frac { 1 } { 2 } } } \\ & { \qquad \leq \bigl \| a ^ { ( n ) } \bigr \| + \sigma _ { n } . } \end{array}
$$

This is true for all $\pmb { N }$ . Keeping $\pmb { n }$ fixed,allow $N \to \infty$ and obtain

$$
\biggl ( \sum _ { i = 1 } ^ { \infty } | a _ { i } | ^ { 2 } \biggr ) ^ { \frac { 1 } { 2 } } \leq \| a ^ { ( n ) } \| + \sigma _ { n } .
$$

This shows us that the sequence $\left\{ a _ { i } \right\}$ is an element of $\ell ^ { 2 }$

We next show that

$$
\operatorname* { l i m } _ { n \to \infty } \| a - a ^ { ( n ) } \| = 0
$$

where ${ \pmb a } = \{ { \pmb a } _ { i } \}$

In (9.2.8) allow $N \to \infty$ .This yields

$$
\sum _ { i = 1 } ^ { \infty } | a _ { i } - a _ { i } ^ { ( n ) } | ^ { 2 } \leq { \sigma _ { n } } ^ { 2 } .
$$

In view of (9.2.6), (9.2.1l) follows. The Cauchy sequence ${ \pmb a } ^ { ( n ) }$ approaches the element $\pmb { a }$ as a limit.

The unit elements $\boldsymbol { u } _ { 1 } = ( 1 , 0 , \dots { } )$ $u _ { 2 } = ( 0 , 1 , 0 , . ~ . ~ . ) , . ~ . ~ .$ ,are independent and orthonormal. They are complete, for if $\pmb { a } = ( a _ { 1 } , a _ { 2 } , \dots ) \in \ell ^ { 2 }$ then ${ \pmb a } _ { i } = ( { \pmb a } , { \pmb u } _ { i } ) = 0$ ， $i = 1 , 2 , \dots$ ,implies ${ \pmb a } = { \bf 0 }$ ·

#

The second Hilbert space is $L ^ { 2 } [ a , b ]$ ，consisting of all functions defined on $[ a , b ]$ which are measurable and for which $| f ( x ) | ^ { 2 }$ is integrable.The inner product is defined by

$$
( f , g ) = \int _ { a } ^ { b } f ( x ) { \overline { { g ( x ) } } } d x
$$

and the norm by

$$
\| f \| ^ { 2 } = ( f , f ) = \int _ { a } ^ { b } | f ( x ) | ^ { 2 } d x .
$$

We may consider functions that are real valued or that are complex valued.This leads to two separate spaces,but the proofs are the same for each.

It should be recalled that two functions differing only on a set of zero measure have the same Lebesgue integral.Hence,according to (9.2.l3), there are functions not identically zero with zero norm.In order to avoid this difficulty,we treat as identical any two functions whose values differ on a set of zero measure at most.This means that the elements of our space should not be the functions themselves but equivalence classes of functions. To set up the work in this form is a nicety,and we shall not insist upon it.

THEOREM 9.2.2. $L ^ { 2 } [ a , b ]$ with inner product (9.2.12) and the identification of functions discussed above is a Hilbert space.

Proof:We have seen (Ex.l0,7.2) that $L ^ { 2 } [ a , b ]$ is a normed linear space and that the inner product expression (9.2.l2) has meaning for $f , g \in L ^ { 2 } [ a , b ]$ By Theorem l.4.0,and simple properties of the integral, $L ^ { 2 } [ a , b ]$ is an inner product space as well.

We next show that $L ^ { 2 } [ a , b ]$ is complete. That is,we show that every

Cauchy sequence converges to an element of the space. In symbols,

$$
\operatorname* { l i m } _ { m , n \to \infty } \int _ { a } ^ { b } | f _ { m } ( x ) - f _ { n } ( x ) | ^ { 2 } d x = \operatorname* { l i m } _ { m , n \to \infty } \| f _ { m } - f _ { n } \| ^ { 2 } = 0
$$

implies the existence of an $f ( x ) \in L ^ { 2 } [ a , b ]$ for which

$$
\operatorname* { l i m } _ { n \to \infty } \int _ { a } ^ { b } | f ( x ) - f _ { n } ( x ) | ^ { 2 } d x = \operatorname* { l i m } _ { n \to \infty } \| f - f _ { n } \| ^ { 2 } = 0 .
$$

In view of (9.2.l4),we can find a strictly increasing sequence of positive integers $n _ { 1 } , n _ { 2 } , \ldots$ ,such that

$$
\| f _ { n _ { k } } - f _ { n _ { k + 1 } } \| \leq { \frac { 1 } { 2 ^ { k } } } , k = 1 , 2 , . . . .
$$

If $\pmb { g }$ is an arbitrary function of $L ^ { 2 } [ a , b ]$ ,then by the Schwarz inequality,

$$
\begin{array} { r } { \displaystyle \int _ { a } ^ { b } \lvert g ( x ) \rvert | f _ { n _ { k } } ( x ) - f _ { n _ { k + 1 } } ( x ) | d x \leq \| g \| \| f _ { n _ { k } } - f _ { n _ { k + 1 } } \| \leq \| g \| \| 2 ^ { - k } . \mathrm { H e n c e } } \\ { \displaystyle \sum _ { k = 1 } ^ { \infty } \displaystyle \int _ { a } ^ { b } \lvert g ( x ) \rvert | f _ { n _ { k } } ( x ) - f _ { n _ { k + 1 } } ( x ) | d x \leq \| g \| \langle \frac { 1 } { 2 } + \frac { 1 } { 4 } + \cdot \cdot \cdot \rangle = \| g \| . } \end{array}
$$

Thus, interchanging summation and integration,

$$
\int _ { a } ^ { b } | g ( x ) | \sum _ { k = 1 } ^ { \infty } | f _ { n _ { k } } ( x ) - f _ { n _ { k + 1 } } ( x ) | d x \leq \| g \| < \infty .
$$

This tells us that

$$
| g ( x ) | \sum _ { k = 1 } ^ { \infty } | f _ { n _ { k } } ( x ) - f _ { n _ { k + 1 } } ( x ) | < \infty
$$

almost everywhere on $[ a , b ]$ ，and hence that $\sum _ { k = 1 } ^ { \infty } | f _ { n _ { k } } ( x ) - f _ { n _ { k + 1 } } ( x ) | < \infty$ al.   
most everywhere.This last statement is true because if the series diverged   
on a set of positive measure,we could take a test function $\pmb { g }$ that was non  
zero on this set,and obtain a contradiction to (9.2.18).

Now $\sum _ { k = 1 } ^ { \infty } ( f _ { n _ { k + 1 } } ( x ) - f _ { n _ { k } } ( x ) )$ must also converge almost everywhere. Its partial sums are $f _ { n _ { k + 1 } } ( x ) - f _ { n _ { 1 } } ( x )$ 、Hence,for an appropriate function $f ( x )$ defined almost everywhere,

$$
\operatorname* { l i m } _ { k \to \infty } f _ { n _ { k } } ( x ) = f ( x ) .
$$

We next show that $f ( x ) \in L ^ { 2 } [ a , b ]$ .In view of (9.2.19),for fixed $j _ { ; }$ we have almost everywhere $\operatorname* { l i m } _ { k \to \infty } | f _ { n _ { k } } ( x ) - f _ { n _ { j } } ( x ) | ^ { 2 } = | f ( x ) - f _ { n _ { j } } ( x ) | ^ { 2 }$ . Hence by Fatou's lemma,

$$
\int _ { a } ^ { b } | f ( x ) - f _ { n _ { j } } ( x ) | ^ { 2 } d x \leq \operatorname* { l i m } _ { k \to \infty } \operatorname* { i n f } _ { 2 } \int _ { a } ^ { b } | f _ { n _ { k } } ( x ) - f _ { n _ { j } } ( x ) | ^ { 2 } d x .
$$

$$
\begin{array} { l } { \| f _ { n _ { k } } - f _ { n _ { j } } \| \le \| f _ { n _ { j } } - f _ { n _ { j + 1 } } \| + \| f _ { n _ { j + 1 } } - f _ { n _ { j + 2 } } \| + \cdot \cdot \cdot + \| f _ { n _ { k - 1 } } - f _ { n _ { k } } \| } \\ { \quad \le \displaystyle \frac 1 { 2 ^ { j } } + \displaystyle \frac 1 { 2 ^ { j + 1 } } + \cdot \cdot \cdot = \displaystyle \frac 1 { 2 ^ { j - 1 } } . } \end{array}
$$

Hence,

$$
\| f _ { n _ { k } } - f _ { n _ { j } } \| ^ { 2 } \leq { \frac { 1 } { 2 ^ { 2 j - 2 } } } , \ \mathrm { { s o } \ t h a t \operatorname* { l i m } _ { k \to \infty } \operatorname* { i n f } _ { 0 } } \int _ { a } ^ { b } | f _ { n _ { k } } ( x ) - f _ { n _ { j } } ( x ) | ^ { 2 } d x \leq { \frac { 1 } { 2 ^ { 2 j - 2 } } } < \infty .
$$

This means that $\int _ { a } ^ { b } | f ( x ) - f _ { n , } ( x ) | ^ { 2 } d x < \infty$ ， so that $f - f _ { n _ { j } } \in L ^ { 2 } [ a , b ]$ Since $f = ( f - f _ { n _ { \ i } } ) + f _ { n _ { j } } ,$ and each of these is in $L ^ { 2 } [ a , b ]$ ，their sum, $f _ { : }$ must be in $L ^ { 2 } ( a , b ]$ .From (9.2.2O) and the last inequality for the lim inf,

$$
\operatorname* { l i m } _ { j \to \infty } \| f - f _ { n _ { j } } \| = 0 .
$$

Now $\| f - f _ { n } \| \leq \| f - f _ { n _ { j } } \| + \| f _ { n _ { j } } - f _ { n } \|$ .The first term on the right can be made arbitrarily small,as we have seen.The second can also be made arbitrarily small in virtue of (9.2.l4). Hence (9.2.15) follows.

To wind up the proof of the theorem,we must show that $L ^ { 2 } [ a , b ]$ is infinite dimensional and contains a complete (or closed） sequence.The functions 1 $, x , x ^ { 2 }$ ...,are in $L ^ { 2 } [ a , b ]$ and are independent. Moreover, they are complete.This will be established in Theorem 11.2.1.

The proof of completeness is capable of wide generalization.In the first place，completeness holds with the norm, $\| f \| ^ { p } = \int _ { a } ^ { b } | f ( x ) | ^ { p } d x ,$ p ≥1. Secondly,positive weighting functions may be used.For $\pmb { p = 2 }$ ,each weight leads to a corresponding Hilbert space.

III

The third Hilbert space to be studied here is comprised of certain single valued analytic functions.It has a totally different flavor from the two previous spaces for the reason that convergence in norm now implies uniform convergence.A certain part of the discussion that follows could have been abridged by employing the Lebesgue integral,but it is of some interest to see the theory built up with only the Riemann integral.

Let $\pmb { B }$ designate a fixed region (open connected set) lying in the complex $\boldsymbol { z }$ plane.It is clear (intuitively at least for simple regions,and we shall not pursue the topological question further $^ \dagger$ ）that we can find a sequence of closed bounded regions $B _ { 1 } , B _ { 2 } , \ldots$ ，with the following properties

(a) $B _ { n }$ is contained in $\pmb { B }$ ， $n = 1 , 2 , \ldots .$   
(） $B _ { n }$ is contained in the interior of $B _ { n + 1 }$ ， $n = 1 , 2 , \ldots .$   
(c） The sequence $B _ { n }$ exhausts $\pmb { B }$ in the sense that any point of $\pmb { B }$ (with the exception of $z = \infty$ ,if it lies in $\pmb { B }$ ）ultimately belongs to some $B _ { n }$ and hence to all subsequent $\pmb { { \cal B } } \mathbf { \dot { s } }$

$^ { \dagger }$ See Walsh,[l], p. 10.

![](../chunks/Interpolation and Approximation (Philip J. Davis) (z-library.sk, 1lib.sk, z-lib.sk)_part_0004_pages_0211-0280/auto/images/34952666b46ead1774376cf245c776e95cffec98617a820f6b03668361e50b1d.jpg)  
Figure 9.2.1.

If $\pmb { S }$ in any closed bounded set in $\pmb { B }$ then $\pmb { \mathscr { s } }$ is contained in $B _ { n }$ for all $\pmb { n }$ sufficiently large.For suppose not.Then we shall be able to find a point ${ \pmb z _ { 1 } }$ in $\pmb { \mathscr { s } }$ but not in ${ \cal B } _ { 1 } , z _ { 2 }$ in $\pmb { \mathscr { s } }$ but not in $\mathbf { \delta } _ { B _ { 2 } } , \ldots .$ The points $z _ { 1 } , z _ { 2 } ,$ ... have a limit point $z ^ { * } \neq \infty$ which is in $\pmb { S }$ Now $z ^ { * }$ lies in some $B _ { m }$ by hypothesis (c) and hence is interior to $B _ { m + 1 }$ by (b).A whole neighborhood of $z ^ { * }$ therefore lies in $B _ { m + 1 }$ ， and this means that an infinity of points of the sequence $z _ { 1 } , z _ { 2 } , \ldots$ ,lie in $B _ { m + 1 } . \mathrm { L e t } q ( > m + 1 )$ be such that $z _ { q } \in B _ { m + 1 }$ . Then $z _ { q } \in B _ { q } .$ This is a contradiction.

We shall deal with functions $w ( z )$ defined on $\pmb { B }$ and possessing Riemann integrals over $B _ { n }$ ， $n = 1 , 2 , \ldots$ , for all sequences $B _ { n }$

If $\operatorname* { l i m } _ { n \to \infty } \iint _ { \pmb { B } _ { n } } w ( z ) d x d y$ exists for all sequences $B _ { n }$ and its value is independent of the particular sequence $B _ { n }$ assumed to satisfy (a)-(c),we shall write

$$
\iint _ { B } w ( z ) d x d y = \operatorname* { l i m } _ { n \to \infty \atop B _ { n } } \iint w ( z ) d x d y .
$$

If $w ( z ) \geq 0$ ， and if for some sequence $B _ { n }$ we set $I _ { n } = \int \limits _ { B _ { n } } \int w ( z ) d x d y$ ，then

$B _ { n } \subset B _ { n + 1 }$ implies that $\scriptstyle { I _ { n } }$ is nondecreasing. Hence, $\operatorname* { l i m } _ { n \to \infty } I _ { n }$ exists (or is $+ \infty )$ . Suppose that $\operatorname* { l i m } _ { n  \infty } I _ { n } = I < \infty$ Let $D _ { n }$ be a second sequence satisfying (a)-(c). A fixed $D _ { \pmb { n } }$ is contained in some $B _ { k }$ for $\pmb { k }$ sufficiently large. Hence

$$
\iint _ { D _ { n } } w ( z ) d x d y \leq \int _ { B _ { k } } w ( z ) d x d y \leq I .
$$

$$
\operatorname* { l i m } _ { n \to \infty } \int _ { D _ { n } } \int w ( z ) d x d y = L \leq I .
$$

We may reverse the roles of the $\pmb { D }$ 's and the B's and obtain $I \leq L$ Hence $I = L ,$ ,and this tells us that the limit is independent of the particular selection of regions $B _ { n }$

DEFINITION 9.2.1． Let $\pmb { B }$ be a region.The set of functions $f ( z )$ which are single valued and analytic in $\pmb { B }$ and for which

$$
\iint _ { B } { | f ( z ) | ^ { 2 } d x d y } < \infty .
$$

will be designated by $L ^ { 2 } ( B )$

Ex.1.If $\pmb { B }$ is bounded and $f ( z )$ remains analytic or even continuous in the closure of $\textbf {  { B } }$ then $f \in L ^ { 2 } ( B )$ ·

LEMMA 9.2.3. If $f ( z )$ and $g ( z ) \in L ^ { 2 } ( B )$ then the linear combination af $( z ) +$ $b g ( z ) \in L ^ { 2 } ( B )$ for all complex constants $a , b . L ^ { 2 } ( B )$ is therefore $\pmb { a }$ linear space.

Proof:First of all,the combination af $( z ) + b g ( z )$ is single valued and analytic in $\pmb { B }$ .Now,

$$
| a f ( z ) + b g ( z ) | ^ { 2 } + | a f ( z ) - b g ( z ) | ^ { 2 } \equiv 2 ( | a | ^ { 2 } | f ( z ) | ^ { 2 } + | b | ^ { 2 } | g ( z ) | ^ { 2 } ) .
$$

Hence $| a f ( z ) + b g ( z ) | ^ { 2 } \leq 2 ( | a | ^ { 2 } | f ( z ) | ^ { 2 } + | b | ^ { 2 } | g ( z ) | ^ { 2 } )$ . Therefore

$$
\int _ { B _ { n } } \int _ { } | a f ( z ) + b g ( z ) | ^ { 2 } d x d y \leq 2 | a | ^ { 2 } \int _ { B _ { n } } \int _ { } | f ( z ) | ^ { 2 } d x d y + 2 | b | ^ { 2 } \int _ { B _ { n } } \int _ { } | g ( z ) ^ { 2 } | d x d y .
$$

Allowing $\pmb { n }  \infty$ ,the last two integrals possess finite limits by hypothesis.

Therefore $\operatorname* { l i m } _ { n \to \infty } \iint _ { B _ { n } } | a f ( z ) + b g ( z ) | ^ { 2 } d x d y \mathrm { ~ e x i s t s ~ a n d ~ i s < \infty . }$

$$
\mathtt { E M M A } \ 9 . 2 . 4 . \ I f f a n d \ g \in L ^ { 2 } ( B ) \ t h e n \int _ { B } \int f \bar { g } \ d x \ d y \ e x i s t s .
$$

Proof: The following is an algebraic identity :

$$
f \bar { g } = \frac { 1 } { 2 } | f + g | ^ { 2 } + \frac { i } { 2 } | f + i g | ^ { 2 } - \frac { 1 + i } { 2 } | f | ^ { 2 } - \frac { 1 + i } { 2 } | g | ^ { 2 } .
$$

This expresses the function $f { \bar { g } }$ as a linear combination of nonnegative functions.

Integrating over $B _ { n }$

$$
\begin{array} { r l } & { \displaystyle \int _ { B _ { n } } \int _ { f } f \bar { g } d x d y = \frac { 1 } { 2 } \int _ { B _ { n } } \int _ { 1 } f + g | ^ { 2 } d x d y + \frac { i } { 2 } \int _ { B _ { n } } \int _ { | f | ^ { 2 } } { \not p } | f + i g | ^ { 2 } d x d y } \\ & { \quad \quad \quad \quad - \frac { 1 + i } { 2 } \displaystyle \iint _ { B _ { n } } | f | ^ { 2 } d x d y - \frac { 1 + i } { 2 } \displaystyle \iint _ { B _ { n } } | g | ^ { 2 } d x d y . } \end{array}
$$

Since $f$ and $\pmb { g }$ are in $L ^ { 2 } ( B )$ ,the previous lemma tells us that both $f + g$ and $f + i g$ are in $L ^ { 2 } ( B )$ . The limits of each of the four integrals on the right, as $\pmb { \mathscr { n } }  \infty$ exist independently of the sequence $B _ { n }$ and are $< \infty$ This must also be true of the integral on the left.

LEMMA 9.2.5. For J $\ell , g \in L ^ { 2 } ( B )$ ,write

$$
( f , g ) = \int _ { B } f { \bar { g } } d x d y .
$$

The expression $( f , g )$ is an inner product for $L ^ { 2 } ( B )$ With it, $L ^ { 2 } ( B )$ is an inner product space and therefore $\pmb { a }$ normed linear space wherein

$$
\| f \| ^ { 2 } = \iint _ { B } | f | ^ { 2 } d x d y .
$$

Proof: Since $( f + g ) \bar { h } = f \bar { h } + g \bar { h } , \ ( \alpha f ) \bar { g } = \alpha ( f \bar { g } ) , \ f \bar { g } = \overline { { { g \bar { f } } } } ,$ the algebraic properties required of an inner product are evident by integrating over $B _ { n }$ and passing to the limit. If $( f , f ) = \iint _ { B } | f | ^ { 2 } d x d y = 0$ the $\displaystyle \mathbf { \boldsymbol { n } } \iint _ { \mathbf { \boldsymbol { n } } _ { \boldsymbol { n } } } \mathbf { \lvert } f \mathbf { \rvert } ^ { 2 } d x d y =$ 0 for all $\pmb { n }$ . Since $| f | ^ { 2 }$ is continuous over $B _ { n }$ ,it follows that $f ( z ) \equiv 0$ on $B _ { n }$ ， and hence throughout $\pmb { B }$

LEMMA 9.2.6. Let $C _ { r }$ designate the closed circle $| z - z _ { 0 } | \leq r .$ Suppose that $f ( z )$ is analytic in $C _ { r }$ If

$$
f ( z ) = a _ { 0 } + a _ { 1 } ( z - z _ { 0 } ) + a _ { 2 } ( z - z _ { 0 } ) ^ { 2 } + . . . ,
$$

then

$$
\iint _ { C _ { \tau } } \lvert f ( z ) \rvert ^ { 2 } d x d y = \pi \sum _ { n = 0 } ^ { \infty } \lvert a _ { n } \rvert ^ { 2 } \frac { r ^ { 2 n + 2 } } { n + 1 } .
$$

Proof: The series (9.2.26) converges uniformly and absolutely in $C _ { r }$ For this reason,

$$
\begin{array} { c } { { \displaystyle { \displaystyle \iint _ { \cal C } | f ( z ) | ^ { 2 } d x d y = \displaystyle \iint _ { { \cal C } _ { \tau } } \biggl ( \sum _ { m = 0 } ^ { \infty } a _ { m } ( z - z _ { 0 } ) ^ { m } \biggr ) \biggl ( \sum _ { m = 0 } ^ { \infty } \bar { a } _ { m } ( \bar { z } - \bar { z } _ { 0 } ) ^ { m } \biggr ) d x d y } } } \\ { { = \displaystyle { \sum _ { m , n = 0 } ^ { \infty } a _ { m } \bar { a } _ { n } \displaystyle \iint _ { { \cal C } _ { \tau } } ( z - z _ { 0 } ) ^ { m } ( \bar { z } - \bar { z } _ { 0 } ) ^ { n } d x d y } . } } \end{array}
$$

Set $z - z _ { 0 } = \rho e ^ { i \theta }$ Then

$$
\int _ { \bar { c } _ { r } } ( z - z _ { 0 } ) ^ { m } ( \bar { z } - \bar { z } _ { 0 } ) ^ { n } d x d y = \int _ { 0 } ^ { 2 \pi } d \theta e ^ { ( m - n ) i \theta } \int _ { 0 } ^ { \tau } \rho ^ { m + n + 1 } d \rho .
$$

If $m \neq n$ ，the inner integral vanishes.When ${ \pmb m } = { \pmb n }$ ，we have $\pi { \frac { r ^ { 2 ( n + 1 ) } } { n + 1 } }$ Thus, $\iint _ { C _ { r } } \lvert f ( z ) \rvert ^ { 2 } d x d y = \pi \sum _ { n = 0 } ^ { \infty } \lvert a _ { n } \rvert ^ { 2 } \frac { r ^ { 2 n + 2 } } { n + 1 } \cdotp$

THEOREM 9.2.7. Let $f ( z ) = \sum _ { n = 0 } ^ { \infty } a _ { n } ( z - z _ { 0 } ) ^ { n }$ . Then $S = \pi \sum _ { n = 0 } ^ { \infty } | a _ { n } | ^ { 2 } \frac { r ^ { 2 n + 2 } } { n + 1 } < \infty$ if and only if $f \in L ^ { 2 } ( C _ { r } )$ .If $f \in L ^ { 2 } ( C _ { r } )$ then $S = \| f \| ^ { 2 }$

Proof: Assume $\quad { \mathfrak { S } } < \infty$ .Then,for some constant $M$ ，

$$
| a _ { n } | ^ { 2 } { \frac { r ^ { 2 n + 2 } } { n + 1 } } \leq M , n = 0 , 1 , . . . . .
$$

Hence,

$$
| a _ { n } | ^ { 1 / n } \leq \frac { M ^ { 1 / 2 n } ( n + 1 ) ^ { 1 / 2 n } } { r \cdot r ^ { 1 / n } } .
$$

If $\pmb { \rho }$ designates the radius of convergence of $\sum _ { \ i = 0 } ^ { \infty } a _ { n } ( z - z _ { 0 } ) ^ { n }$ ，then

$$
\frac { 1 } { \rho } = \operatorname* { l i m } _ { n \to \infty } \operatorname* { s u p } | a _ { n } | ^ { 1 / n } \leq \frac { 1 } { r } .
$$

Thus, $\pmb { \rho } \geq \pmb { r }$ and therefore $f ( z )$ is analytic in $| z - z _ { 0 } | < r$ Select an $\pmb { r } ^ { \prime }$ with $0 < r ^ { \prime } < r$ If $C _ { r ^ { \prime } }$ is $| z - z _ { 0 } | \leq r ^ { \prime }$ , then by Lemma 9.2.6,

$$
\int _ { C _ { r } } \int _ { } | f ( z ) | ^ { 2 } d x d y = \pi \sum _ { n = 0 } ^ { \infty } | a _ { n } | ^ { 2 } \frac { ( r ^ { \prime } ) ^ { 2 n + 2 } } { n + 1 } < S < \infty .
$$

Therefore $\operatorname* { l i m } _ { \tau ^ { \prime }  \tau } \iint _ { C _ { \tau ^ { \prime } } } | f ( z ) | ^ { 2 } d x d y < \infty$ and therefore $f \in L ^ { 2 } ( C _ { r } )$

Suppose,conversely,that $f \in L ^ { 2 } ( C _ { r } )$ .Then, for any $\pmb { r } ^ { \prime }$ ， $0 < r ^ { \prime } < r , f ( z )$ i analytic in the closed circle $| z - z _ { 0 } | \leq r ^ { \prime }$ .Hence by the lemma,

$$
\int _ { c _ { r } } \Bigl | f ( z ) | ^ { 2 } d x d y = \pi \sum _ { n = 0 } ^ { \infty } | a _ { n } | ^ { 2 } \frac { ( r ^ { \prime } ) ^ { 2 n + 2 } } { n + 1 } = S ( r ^ { \prime } ) < \infty .
$$

Moreover, $\operatorname* { l i m } _ { r ^ { \prime } \to r ^ { - } } { \cal S } ( r ^ { \prime } )$ exists and equals $\| f \| ^ { 2 } \left( < \infty \right)$ . For any $\pmb { N }$

$$
\pi \sum _ { n = 0 } ^ { N } | a _ { n } | ^ { 2 } { \frac { ( r ^ { \prime } ) ^ { 2 n + 2 } } { n + 1 } } \leq S ( r ^ { \prime } ) .
$$

Allowing $r ^ { \prime }  r ^ { - }$ ，

$$
\pi \sum _ { n = 0 } ^ { N } | a _ { n } | ^ { 2 } { \frac { r ^ { 2 n + 2 } } { n + 1 } } \leq \| f \| ^ { 2 } .
$$

This estimate is independent of $\pmb { N }$ . Allowing $N \to \infty$ ，we obtain

$$
S \leq \| f \| ^ { 2 } < \infty .
$$

Since $\begin{array} { r } { S ( r ^ { \prime } ) \le S } \end{array}$ by allowing $r ^ { \prime } \to r ^ { - }$ we have $\| f \| ^ { 2 } \leq S$ and therefore $\boldsymbol { \mathscr { S } } =$ $\| f \| ^ { 2 }$

LEMMA 9.2.8. Let $f ( z ) \in L ^ { 2 } ( B )$ Let $\pmb { r } ( z _ { 0 } )$ be the distance from a fixed point $\pmb { z _ { 0 } } \in \mathcal { B }$ to the boundary of $\pmb { B }$ Then,

$$
| f ( z _ { 0 } ) | ^ { 2 } \leq { \frac { \| f \| ^ { 2 } } { \pi r ^ { 2 } ( z _ { 0 } ) } } .
$$

Proof: Let $0 < r ^ { \prime } < r ( z _ { 0 } )$ .Then the circle $C _ { \pmb { r } ^ { \prime } } \colon | z - z _ { 0 } | \leq r ^ { \prime }$ is contained in $\pmb { B }$ This implies that $\iint _ { C _ { f } , \prime } | f ( z ) | ^ { 2 } d x d y \leq \iint _ { B } | f ( z ) | ^ { 2 } d x d y = \| f \| ^ { 2 }$ But from (9.2.27), ignoring all but the first term,

Then,

$$
\pi | f ( z _ { 0 } ) | ^ { 2 } r ^ { \prime 2 } = \pi | a _ { 0 } | ^ { 2 } r ^ { \prime 2 } \leq \int _ { \underline { { c } } _ { r ^ { \prime } } } \lvert f ( z ) \rvert ^ { 2 } d x d y \leq \| f \| ^ { 2 } .
$$

$$
\vert f ( z _ { 0 } ) \vert ^ { 2 } \leq { \frac { \Vert f \Vert ^ { 2 } } { \pi r ^ { \prime 2 } } } .
$$

This is true for all $0 < r ^ { \prime } < r$ and hence (9.2.28) follows.

LEMMA 9.2.9. $\scriptstyle { { \cal L } ^ { 2 } } ( B )$ is $^ { \pmb { a } }$ complete inner product space.

Proof: Let $\{ f _ { n } ( z ) \}$ be a Cauchy sequence of functions in $L ^ { 2 } ( B )$ . Given an $\varepsilon$ ,we can find an $\boldsymbol { N } ( \varepsilon )$ such that

$$
\| f _ { m } ( z ) - f _ { n } ( z ) \| \leq \varepsilon , m , n \geq N ( \varepsilon ) .
$$

We wish to show the existence of an analytic function $f ( z )$ which is in $L ^ { 2 } ( B )$ and for which $\operatorname* { l i m } _ { n \to \infty } \| f ( z ) - f _ { n } ( z ) \| = 0$ Select a fixed $B _ { k }$ .On $B _ { k }$ we have from the previous Lemma,

$$
| f _ { m } ( z ) - f _ { n } ( z ) | \leq \frac { \| f _ { m } - f _ { n } \| } { \pi ^ { \frac { 1 } { 2 } } r ( z ) } .
$$

If $\rho ( > 0 )$ designates the minimum distance from $B _ { k }$ to the boundary of $\pmb { B }$ ， then we have uniformly in $B _ { \kappa }$

$$
| f _ { m } ( z ) - f _ { n } ( z ) | \leq \frac { \| f _ { m } - f _ { n } \| } { \pi ^ { \frac { 1 } { 2 } } \rho } .
$$

In view of (9.2.31) and (9.2.29), $\{ f _ { m } ( z ) \}$ is a Cauchy sequence of functions with respect to the norm $\| \phi \| = \operatorname* { m a x } _ { z \in B _ { k } } | \phi ( z ) |$ 、(Cf.Ex.8,7.2.） The sequence therefore converges uniformly in $B _ { k }$ to a function $f ( z )$ which must be analytic in the interior of $B _ { k }$ Since $B _ { \kappa }$ is arbitrary, $f ( z )$ must be analytic in the whole of $\pmb { B }$ Now,for $\pmb { n }$ and $\pmb { k }$ fixed, $\operatorname* { l i m } _ { m \to \infty } \iint _ { \ v { D } _ { k } } | f _ { m } ( z ) - f _ { n } ( z ) | ^ { 2 } d x d y =$ $\iint _ { B _ { k } } | f ( z ) - f _ { n } ( z ) | ^ { 2 } d x d y$ .This is true because of the uniform convergence of $f _ { m }$ to $f$ on $B _ { \kappa }$ .For $m , n \geq N ( \varepsilon )$ we have for all $\pmb { k }$ ，

$$
\int _ { B _ { k } } \int _ { | f _ { m } ( z ) - f _ { n } ( z ) | ^ { 2 } } d x d y \leq \int _ { B } \int _ { } | f _ { m } ( z ) - f _ { n } ( z ) | ^ { 2 } d x d y \leq \varepsilon ^ { 2 } .
$$

Allowing ${ \pmb m }  \infty$

$$
\int _ { B _ { k } } \int _ { } | f ( z ) - f _ { n } ( z ) | ^ { 2 } d x d y \leq \varepsilon ^ { 2 } .
$$

This statement is independent of $\pmb { k }$ ; hence

$$
\operatorname* { l i m } _ { k \to \infty } \iint _ { \pmb { \mathscr { B } } _ { k } } | f ( z ) - f _ { n } ( z ) | ^ { 2 } d x d y \leq \varepsilon ^ { 2 } .
$$

This implies that $f ( z ) - f _ { n } ( z )$ is in $L ^ { 2 } ( B )$ . Since $f _ { n } ( z )$ is in $L ^ { 2 } ( B )$ , their sum   
$f ( z )$ is in $L ^ { 2 } ( B )$ Since $\int _ { B } \int _ { } | f ( z ) - f _ { n } ( z ) | ^ { 2 } d x d y \leq \varepsilon ^ { 2 }$ for $n \geq N ( \varepsilon )$ we have   
convergence in norm to $f ( z )$

Having established that $L ^ { 2 } ( B )$ is a complete inner product space, it remains only to show that $L ^ { 2 } ( B )$ is infinite dimensional, that it contains a closed sequence of elements,and we will have proved that $L ^ { 2 } ( B )$ is a Hilbert space. As with $L ^ { 2 } [ a , b ]$ ，we could refer to Theorem 11.4.8 telling us that the complex powers are closed in $L ^ { 2 } ( B )$ for certain types of region $\pmb { B }$ However,we shall prove a stronger result by means of the Fréchet-Riesz representation theorem whose proof will be given shortly.

THEOREM 9.2.10. $L ^ { 2 } ( B )$ contains a complete sequence of functions. If $\pmb { B }$ is bounded,or can be mapped l-l conformally onto $\pmb { a }$ bounded region， then $L ^ { 2 } ( B )$ is a Hilbert space.

Proof: Let $\pmb { t }$ be a fixed point of $\pmb { B }$ As is shown in 9.3, Ex.4, $L _ { n } ( f ) =$ $f ^ { ( n ) } ( t )$ ， $\pmb { n = 0 , 1 , 2 , . . . }$ ，are bounded linear functionals over $L ^ { 2 } ( B )$ By Theorem 9.3.3,there exists,for each $\pmb { n }$ ，an element $g _ { n } ( z ) \in L ^ { 2 } ( B )$ such that

$$
L _ { n } ( f ) = ( f , g _ { n } ) = f ^ { ( n ) } ( t ) , \qquad f \in L ^ { 2 } ( B ) .
$$

If now $( f , g _ { n } ) = 0$ ， $\pmb { n = 0 , 1 , \dots }$ ，then $f ^ { ( n ) } ( t ) = 0$ ， $\pmb { n = 0 , 1 , \dots }$ and this implies that $\scriptstyle f \equiv 0$ . Therefore ${ \pmb g } _ { \pmb n }$ is a complete sequence of functions.

If $\pmb { B }$ is bounded, then $1 , z , z ^ { 2 }$ 。...,are independent and are all in $L ^ { 2 } ( B )$ Hence $L ^ { 2 } ( B )$ is infinite dimensional.If $\pmb { B }$ can be mapped 1-l conformally onto a bounded region $\pmb { D }$ ， then we can find an infinite sequence of

independent functions in $L ^ { 2 } ( B )$ by a change of variable. For, let $\pmb { D }$ lie in the $\pmb { w }$ plane, $w = u + i v$ ,and suppose that

$$
w = M ( z ) , \qquad z = x + i y \in B ,
$$

maps $\textbf { \textit { B } } 1 . 1$ conformally onto $D$ Let $D _ { n }$ be a sequence for $\pmb { D }$ satisfying (a)-(c).Let $B _ { n }$ be the images of $D _ { n }$ under the inverse map of (9.2.33).The $B _ { n }$ will be a sequence for $\pmb { B }$ satisfying (a)-(c),If $f ( w ) \in L ^ { 2 } ( D )$ ,we have

$$
\iint _ { \boldsymbol { D } _ { n } } | f ( \boldsymbol { w } ) | ^ { 2 } d u d v = \iint _ { \boldsymbol { B } _ { n } } | f ( M ( z ) ) | ^ { 2 } \left| \overline { { \partial \boldsymbol { x } } } \quad \overline { { \partial \boldsymbol { y } } } \right| d x d y
$$

But by the Cauchy-Riemann equations,

$$
\frac { \partial u } { \partial x } = \frac { \partial v } { \partial y } , \frac { \partial u } { \partial y } = - \frac { \partial v } { \partial x } ,
$$

so that

$$
{ \left| \begin{array} { l l } { { \frac { \partial u } { \partial x } } } & { { \frac { \partial u } { \partial y } } } \\ { { \frac { \partial v } { \partial x } } } & { { \frac { \partial v } { \partial y } } } \end{array} \right| } = \left( { \frac { \partial u } { \partial x } } \right) ^ { 2 } + \left( { \frac { \partial u } { \partial y } } \right) ^ { 2 } = \left| { \frac { \partial u } { \partial x } } - i { \frac { \partial u } { \partial y } } \right| ^ { 2 } = | M ^ { \prime } ( z ) | ^ { 2 } .
$$

Thus,the rule for the transformation of our double integral under the conformal map is

$$
\iint _ { { D } _ { n } } \lvert f ( w ) \rvert ^ { 2 } d u d v = \iint _ { { D } _ { n } } \lvert f ( M ( z ) ) \rvert ^ { 2 } \lvert M ^ { \prime } ( z ) \rvert ^ { 2 } d x d y .
$$

The functions $f ( w ) = 1 , w , w ^ { 2 } , \cdot \cdot \cdot ,$ ，are clearly in $L ^ { 2 } ( D )$ .It follows from (9.2.35),by allowing $n \to \infty$ ,that their“images,”

$$
( M ( z ) ) ^ { n } M ^ { \prime } ( z ) \quad n = 0 , 1 , . . . ,
$$

will be an infinite independent set of functions in $L ^ { 2 } ( B )$

9.3 Bounded Linear Functionals in Normed Linear Spaces and in Hilbert Spaces. We may distinguish two types of linear functionals defined on normed linear spaces: the bounded and the unbounded.

DEFINITION 9.3.1． Let $\pmb { L }$ be a linear functional defined over the elements of a normed linear space $\boldsymbol { X } , \boldsymbol { L }$ is said to be bounded if there exists a constant $\pmb { M }$ such that

$$
| L ( x ) | \leq M \| x \| , \qquad { \mathrm { f o r ~ a l l ~ } } x \in X .
$$

If no such constant exists, the functional is called unbounded.

Ex. 1.Let $\begin{array} { l } { \displaystyle \boldsymbol { X } = C [ \boldsymbol { a } , \boldsymbol { b } ] , \| \boldsymbol { f } \| = \operatorname* { m a x } _ { \boldsymbol { a } < \boldsymbol { x } \le \boldsymbol { b } } \big | \boldsymbol { f } \left( \boldsymbol { x } \right) \big | } \end{array}$ Let $L \left( f \right) = \int _ { a } ^ { b } w ( x ) f ( x ) d x$ for a fixed $w ( x ) \in C [ a , b ]$ .Then,

$$
\left| L ( f ) \right| \leq \int _ { a } ^ { b } { \bigl | } w ( x ) { \bigr | } \operatorname* { m a x } _ { a \leq x \leq b } { \big | } f ( x ) { \big | } d x \leq \left\| f \right\| \int _ { a } ^ { b } { \bigl | } w ( x ) { \bigr | } d x .
$$

Inequality(9.3.1)isfed with $M = \int _ { a } ^ { b } { \left| w ( x ) \right| d x }$ and $L$ is bounded.

Ex.2.Let

$$
X = C [ a , b ] , \| f \| ^ { 2 } = \int _ { a } ^ { b } ( f ( x ) ) ^ { 2 } d x .
$$

Let $L ( f ) = f ( x _ { 0 } )$ where $a \le x _ { 0 } \le b . \ L$ is unbounded. For we may construct a sequence of functions $f _ { n } ( x ) , n = 1 , 2 , . . . ,$ with $f _ { n } ( x _ { 0 } ) = 1$ and

$$
\int _ { a } ^ { b } ( f _ { n } ( x ) ) ^ { 2 } d x = \varepsilon _ { n } { } ^ { 2 } \to 0 .
$$

This can be done in many ways. Now if $\pmb { L }$ were bounded we should have

$$
\begin{array} { r } { 1 = \left| L ( f _ { n } ) \right| \le M \varepsilon _ { n } , } \end{array}
$$

and this is impossible.

Ex.3.Let $x$ be an inner product space and $\pmb { x _ { 0 } }$ bea fixed element.Then $L ( x ) = ( x , x _ { 0 } )$ is a linear functional defined on $x$ .It is bounded,for

$$
\big | L ( x ) \big | = \big | ( x , x _ { 0 } ) \big | \leq \| x \| \| x _ { 0 } \| .
$$

Ex.4.Let $^ { n }$ be a fixed integer $\geq 0$ .If $\pmb { t }$ is a fixed point in a region $B$ ，then the functional

$$
L ( f ) = f ^ { ( n ) } ( t )
$$

is bounded over $L ^ { 2 } ( B )$

Proof:Since $\mathbf { \Delta } _ { t }$ is an interior point,we can find a circle $| C _ { r } \colon | z \mathrm { ~ - ~ } t | \leq r$ contained in $B$ Since

$$
f ( z ) = \sum _ { n = 0 } ^ { \infty } { \frac { f ^ { ( n ) } ( t ) } { n ! } } ( z \ - \ t ) ^ { n }
$$

in $\scriptstyle { C _ { r } , }$ then by (9.2.27),

$$
\pi \sum _ { n = 0 } ^ { \infty } { \frac { \left| f ^ { ( n ) } ( t ) \right| ^ { 2 } } { n ! ^ { 2 } ( n + 1 ) } } r ^ { 2 n + 2 } = \iint _ { C _ { r } } \left| f ( z ) \right| ^ { 2 } d x d y \ \leq \iint _ { B } \left| f ( z ) \right| ^ { 2 } d x d y .
$$

For a particular $_ n$

Therefore

$$
{ \frac { \pi | f ^ { ( n ) } ( t ) | ^ { 2 } } { n ! ^ { 2 } ( n + 1 ) } } r ^ { 2 n + 2 } \leq \int _ { B } \int _ { } | f ( z ) | ^ { 2 } d x d y = \| f \| ^ { 2 } .
$$

$$
\left| L ( f ) \right| = \left| f ^ { ( n ) } ( t ) \right| \leq { \frac { n ! { \sqrt { n + 1 } } } { { \sqrt { \pi } } r ^ { n + 1 } } } \left\| f \right\| .
$$

Some authors use the term“linear functional’to mean a bounded linear functional.But in interpolation theory,the same formal functional may be bounded or unbounded depending upon what space it is considered in,and it is therefore better to stress the fact of boundedness whenever it occurs.

DEFINITION 9.3.2．Let $\pmb { F }$ be a functional defined over a normed linear space. $\pmb { F }$ is said to be continuous if

$$
x _ { n }  x \mathrm { i m p l i e s } F ( x _ { n } )  F ( x ) .
$$

THEOREM 9.3.1. A linear functional $\scriptstyle { \cal L }$ defined on a normed linear space $\pmb { X }$ is boundedif and only if it is continuous.

Proof: Let $\scriptstyle { \cal L }$ be bounded.Then $| L ( x ) | \leq M \| x \|$ for all ${ \pmb x } \in { \pmb X }$ . If now $\| { \pmb x _ { n } } - { \pmb x } \|  0$ ，then $| L ( x _ { n } ) - L ( x ) | = | L ( x _ { n } - x ) | \leq M \| x _ { n } - x \|$ .Therefore $| L ( x _ { n } ) - L ( x ) |  0$

Conversely,suppose that $\boldsymbol { L }$ is continuous and unbounded. Then we can fnda ${ \pmb x } _ { \pmb n }$ $\lvert L ( x _ { n } ) \rvert > n \parallel x _ { n } \parallel$ $y _ { n } = { \frac { x _ { n } } { n \left\| x _ { n } \right\| } }$ $\| y _ { n } \| = { \frac { 1 } { n } }$ $\| y _ { n } - 0 \| \to 0$ $| L ( y _ { n } ) | = { \frac { L ( x _ { n } ) } { n \left\| x _ { n } \right\| } } > 1$ $\boldsymbol { L }$ is continuous, $L ( y _ { n } ) \to L ( 0 ) = 0$ ，and this is a contradiction.

A norm may be associated with each bounded linear functional.Let $\pmb { I }$ designate the set of values $\pmb { M }$ for which condition(9.3.1) holds.Let $M ^ { \prime }$ be the inf of the set $\boldsymbol { \mathit { I } }$ We can find $M _ { 1 } , M _ { 2 } , \ldots , \in I$ such that $M _ { n } \to M ^ { \prime }$ .We have $\lvert L ( x ) \rvert \leq M _ { n } \| x \|$ for all $_ { \pmb { x } }$ and for ${ \pmb n } = { \bf 1 }$ ,2,.... Keep $_ { \pmb { x } }$ fixed and allow $n \to \infty$ .Then, $| L ( x ) | \leq M ^ { \prime } \| x \|$ . This is true for all $\pmb { x } .$ Therefore (9.3.1) holds with $M = M ^ { \prime }$ ,and the set $\boldsymbol { \mathit { I } }$ has a minimum.

DEFINITION 9.3.3． Let $L$ be a bounded linear functional defined on a normed linear space $\pmb { X }$ .Then $\| L \|$ is defined as the minimum value $M$ for which (9.3.1) holds.We have,obviously,

$$
| L ( x ) | \leq \| L \| \ \| x \| , \qquad x \in X ,
$$

and for every $\varepsilon > 0$ , we can find an $\pmb { x _ { 0 } } \in X$ for which

$$
| L ( x _ { 0 } ) | > ( \| L \| - \varepsilon ) \ \| x _ { 0 } \| .
$$

An alternate formula for $\| L \|$ is given by

$$
\| L \| = \operatorname* { s u p } _ { x \in X } { \frac { | L ( x ) | } { \| x \| } } .
$$

For, $\lvert L ( x ) \rvert \leq \| L \| \ \| x \|$ so that ${ \frac { | L ( x ) | } { \| x \| } } \leq \| L \|$ and hence s $\underset { \pmb { x } } { \operatorname* { u p } } \frac { | L ( \pmb { x } ) | } { \| \pmb { x } \| } \leq \| L \|$

On the other hand,given an $\varepsilon > 0$ there is an $\pmb { x _ { 0 } }$ with (9.3.3) holding.Therefore sup ${ \frac { | L ( x ) | } { \| x \| } } \geq { \frac { | L ( x _ { 0 } ) | } { \| x _ { 0 } \| } } > \| L \| - \varepsilon .$ These two inequalities imply (9.3.4). x

Ex.5. $X = C [ a , b ] , \| f \| = \operatorname* { m a x } _ { a \leq x \leq b } \left| f ( x ) \right|$ .Let $L ( f ) = \sum _ { k = 1 } ^ { n } a _ { k } f ( x _ { k } )$ where $a \ \leq$ $x _ { k } \leq b$ Then, ${ \big | } L ( f ) { \big | } \leq \sum _ { k = 1 } ^ { n } { \big | } a _ { k } { \big | } \left| f ( x _ { k } ) \right| \leq \| f \| \sum _ { k = 1 } ^ { n } \left| a _ { k } \right|$ . This implies that $\| \mathbfcal { L } \| \leq$ $\sum _ { k = 1 } ^ { n } \left| a _ { k } \right|$ . On the other hand, construct an $f ( x ) \in C [ a , b ]$ such that $\left| f ( x ) \right| \leq 1$ ， $a \leq x \leq b$ ，and $f ( x _ { k } ) = \operatorname { s g n } a _ { k } , k = 1 , 2 , . . . , n$ .Then, $\| f \| = 1$ and $\left| L ( f ) \right| =$ $\sum _ { k = 1 } ^ { n } \left| a _ { k } \right| \leq \left\| L \right\| \left\| f \right\|$ . This implies hat $\| L \| \geq \sum _ { k = 1 } ^ { n } \left| a _ { k } \right|$ . Therefore $\| L \| = \sum _ { k = 1 } ^ { n } \left| a _ { k } \right|$

Ex.6. $X = C [ a , b ] , \| f \| = \operatorname* { m a x } _ { a \leq x \leq b } { \big | } f ( x ) { \big | } . { \mathrm { ~ L e t ~ } } L ( f ) = \int _ { a } ^ { b } f ( x ) w ( x ) d x$ where ${ \pmb w } ( { \pmb x } )$ is a fixed function of $C [ \pmb { a } , \pmb { b } ]$ .A similar argument shows that

$$
\| L \| = \int _ { a } ^ { b } { \bigl | } w ( x ) { \bigr | } d x .
$$

THEOREM 9.3.2. The set of all bounded linear functionals defined over $^ { \pmb { a } }$ normed linear space $\pmb { X }$ is $\pmb { a }$ linear space. Introducing the quantity $\Vert L \Vert$ by (9.3.4) makes this linear space into $\pmb { a }$ normed linear space.

Proof: Let $L _ { 1 }$ and $L _ { 2 }$ be bounded linear functionals over $\pmb { X }$ . Then, for any ${ \pmb x } \in { \pmb X }$ ，

$$
\begin{array} { r l } & { | ( a _ { 1 } L _ { 1 } + a _ { 2 } L _ { 2 } ) ( x ) | = | a _ { 1 } L _ { 1 } ( x ) + a _ { 2 } L _ { 2 } ( x ) | \leq | a _ { 1 } | \| L _ { 1 } \| \| x \| + | a _ { 2 } | \| L _ { 2 } \| \| x \| } \\ & { \qquad = ( | a _ { 1 } | \| L _ { 1 } \| + | a _ { 2 } | \| L _ { 2 } \| ) \| x \| . } \end{array}
$$

This implies that $a _ { \bf 1 } L _ { \bf 1 } + a _ { \bf 2 } L _ { \bf 2 }$ is a bounded linear functional.

Let $L \neq 0$ .Then there is a $y \neq 0$ such that $L ( y ) \neq 0$ Hence $\| \mathbfcal { L } \| =$ $\mathrm { p } { \frac { | L ( x ) | } { \| x \| } } \geq { \frac { | L ( y ) | } { \| y \| } } > 0$ Therefore $\| L \| = 0$ if and only if $L = 0$ Secondly,

$$
\| L _ { 1 } + L _ { 2 } \| = \operatorname* { s u p } _ { x } { \frac { | L _ { 1 } ( x ) + L _ { 2 } ( x ) | } { \| x \| } } \leq \operatorname* { s u p } _ { x } { \frac { | L _ { 1 } ( x ) | } { \| x \| } } + \operatorname* { s u p } _ { x } { \frac { | L _ { 2 } ( x ) | } { \| x \| } } = \| L _ { 1 } \| + \| L \|
$$

The postulates for a norm are therefore satisfied.

DEFINITion 9.3.4. The normed linear space of bounded linear functionals defined on a given normed linear space $\pmb { X }$ by means of (9.3.4) is known as the normed conjugate space of $\pmb { X }$ and is designated by $X ^ { * }$ ·

In a complete inner product space, bounded linear functionals possess a particularly simple representation.

THEOREM 9.3.3 (Fréchet-Riesz).If $\scriptstyle { \cal L }$ is a bounded linear functional over $\pmb { a }$ complete inner product space $\pmb { X }$ ， then there exists $\pmb { a }$ unique element $x _ { \mathbf { 0 } } \in X$ such that

$$
L ( x ) = ( x , x _ { 0 } ) , \qquad x \in X .
$$

Proof: Let $\pmb { M }$ designate the set of elements $_ x$ such that $L ( x ) = 0$ . Mis clearly a linear space. Moreover,it is closed. For suppose that $x _ { n } \in M$ and $\| x _ { n } - x \| \to 0$ Since $L$ is bounded,

$$
| L ( x - x _ { n } ) | \leq \| L \| \ \| x - x _ { n } \| \to 0 .
$$

Therefore $L ( x ) - L ( x _ { n } )  0$ But $L ( x _ { n } ) = 0$ Hence $L ( x ) = 0$ and $x \in M$

Now there are two possibilities. (a) $M$ is the whole space.In this case $L = 0$ and we may take ${ \pmb x _ { 0 } } = 0$ (b) $M$ is not the whole space.In this case, by Theorem 8.10.2,we can find an element $y _ { 0 } \neq 0$ which is $\perp M$ . If we set

$$
x _ { 0 } = \frac { \overline { { L ( y _ { 0 } ) } } y _ { 0 } } { \| y _ { 0 } \| ^ { 2 } } ,
$$

then we can show that

$$
( x , x _ { 0 } ) = \left( x , { \frac { \overline { { { \cal L } ( y _ { 0 } } } ) y _ { 0 } } { ( y _ { 0 } , y _ { 0 } ) } } \right) = { \cal L } ( x ) , \qquad x \in X .
$$

Now (9.3.7) is equivalent to

$$
L ( x ) ( y _ { 0 } , y _ { 0 } ) = L ( y _ { 0 } ) ( x , y _ { 0 } ) .
$$

Consider the elements $L ( x ) y _ { 0 } - L ( y _ { 0 } ) x .$ $x \in X$ .These elements are in $M$ ， for $L ( L ( x ) y _ { 0 } - L ( y _ { 0 } ) x ) = L ( x ) L ( y _ { 0 } ) - L ( y _ { 0 } ) L ( x ) = 0$ Hence ${ \pmb y _ { 0 } }$ is $\bot$ to these elements. This means that $( L ( x ) y _ { 0 } - L ( y _ { 0 } ) x , y _ { 0 } ) = 0$ and this is precisely (9.3.8).

The $\pmb { x _ { 0 } }$ is unique, for if

then

$$
\begin{array} { r l r l } { L ( x ) = ( x , x _ { 0 } ) = ( x , x _ { 1 } ) , } & { } & { x \in X , } \\ { \quad ( x , x _ { 0 } - x _ { 1 } ) = 0 , } & { } & { x \in X . } \end{array}
$$

If we select ${ \pmb x } = { \pmb x _ { 0 } } - { \pmb x _ { 1 } }$ ，this implies that $\| x _ { 0 } - x _ { 1 } \| ^ { 2 } = 0$ and hence ${ \pmb x _ { 0 } } = { \pmb x _ { 1 } }$

DEFINITION 9.3.5. The element $\pmb { x _ { 0 } }$ is known as the representer of the linear functional $L$

COROLLARY 9.3.4. Let $\pmb { L }$ be a bounded linear functional over a complete

inner product space. Let $\pmb { x _ { 0 } }$ be its representer. Then,

$$
\| \boldsymbol { L } \| = \| \boldsymbol { x } _ { 0 } \|
$$

and

$$
\begin{array} { r } { | L ( \pmb { x _ { 0 } } ) | = \| L \| \ \| \pmb { x _ { 0 } } \| . } \end{array}
$$

Proof: $L ( x ) = ( x , x _ { 0 } )$ Hence $| L ( x ) | \leq | ( x , x _ { 0 } ) | \leq \| x _ { 0 } \| \ \| x \|$ This implies that $\| L \| \leq \| \pmb { x _ { 0 } } \|$ . But $\| L \| = \operatorname* { s u p } _ { x } { \frac { | L ( x ) | } { \| x \| } } \geq { \frac { | L ( x _ { 0 } ) | } { \| x _ { 0 } \| } } = { \frac { | ( x _ { 0 } , x _ { 0 } ) | } { \| x _ { 0 } \| } } = \| x _ { 0 } \|$ Therefore $\| \mathbf { L } \| \geq \| \pmb { x _ { 0 } } \|$ and hence $\| L \| = \| x _ { 0 } \|$ Finally， $| L ( x _ { 0 } ) | = ( x _ { 0 } , x _ { 0 } ) =$ $\| x _ { 0 } \| ^ { 2 } = \| L \| \ \| x _ { 0 } \|$

Ex. 7.In $L ^ { 2 } [ a , b ]$ ,every bounded linear functional has the form

$$
L ( f ) = \int _ { a } ^ { b } f ( x ) g ( x ) d x
$$

with $g ( x ) \in L ^ { 2 } [ a , b ]$ In $L ^ { 2 } ( B )$ sucha fuctionalhas h fgrm $L ( f ) = \int _ { \mathbf { \overline { { B } } } } \int _ { } ^ { } f ( z ) { \overline { { g ( z ) } } } d x d y$

where $g ( z ) \in L ^ { 2 } ( B )$ . Moreover, $\| L \| ^ { 2 } = \int _ { a } ^ { b } ( g ( x ) ) ^ { 2 } d x { \mathrm { ~ o r ~ } } \int _ { B } \int _ { } ^ { } \left| g ( z ) \right| ^ { 2 } d x d y$

The representer of a functional has a simple formula in terms of a complete orthonormal sequence.

THEOREM 9.3.5. Let $\pmb { H }$ be a Hilbert space and ${ \pmb x } _ { 1 } ^ { \ * } , { \pmb x } _ { 2 } ^ { \ * }$ ，..., be a complete orthonormal sequence of elements.If $\pmb { L }$ isa bounded linear functional on $\pmb { H }$ then ${ \cal L } ( x ) = ( x , y )$ where $_ y$ has the Fourier expression

Moreover

$$
\begin{array} { c } { y \displaystyle \sim \sum _ { k = 1 } ^ { \infty } \overline { { L ( { x _ { k } } ^ { * } ) } } { x _ { k } } ^ { * } . } \\ { L ( x ) = \displaystyle \sum _ { k = 1 } ^ { \infty } ( x , { x _ { k } } ^ { * } ) L ( { x _ { k } } ^ { * } ) , \qquad x \in H } \\ { \| L \| ^ { 2 } = \displaystyle \sum _ { k = 1 } ^ { \infty } | L ( { x _ { k } } ^ { * } ) | ^ { 2 } . } \end{array}
$$

and

Proof: Let $_ y$ be the representer of $L$ . Then

$$
y \sim \sum _ { k = 1 } ^ { \infty } ( y , x _ { k } { ^ * } ) x _ { k } { ^ * } = \sum _ { k = 1 } ^ { \infty } { \overline { { ( x _ { k } { ^ * } , y } } ) } x _ { k } { ^ * } = \sum _ { k = 1 } ^ { \infty } { \overline { { L ( x _ { k } { ^ * } } } ) } x _ { k } { ^ * } .
$$

By (8.9.8),

$$
L ( x ) = ( x , y ) = \sum _ { k = 1 } ^ { \infty } ( x , x _ { k } { } ^ { * } ) ( x _ { k } { } ^ { * } , y ) = \sum _ { k = 1 } ^ { \infty } ( x , x _ { k } { } ^ { * } ) L ( x _ { k } { } ^ { * } ) .
$$

Finally, $\| L \| ^ { 2 } = \| y \| ^ { 2 }$ By (8.9.7),

$$
\| y \| ^ { 2 } = \sum _ { k = 1 } ^ { \infty } | ( y , x _ { k } ^ { \ast } ) | ^ { 2 } = \sum _ { k = 1 } ^ { \infty } | L ( x _ { k } ^ { \ast } ) | ^ { 2 } .
$$

LEMMA 9.3.6 (Abel-Dini)．Let $w _ { n } > 0$ and let $\sum _ { n = 1 } ^ { \infty } w _ { n } = \infty$ Then if ${ \cal W } _ { n } =$ $w _ { 1 } + w _ { 2 } + \cdots + w _ { n } ,$ 1

$$
\sum _ { n = 1 } ^ { \infty } { \frac { w _ { n } } { W _ { n } } } = \infty ,
$$

while

$$
\sum _ { n = 1 } ^ { \infty } { \frac { w _ { n } } { \boldsymbol { W _ { n } } ^ { 2 } } } < \infty .
$$

Proof: $\boldsymbol { W } _ { n }$ increases to $+ \infty$

$$
\begin{array} { r l r } {  { \frac { w _ { n + 1 } } { W _ { n + 1 } } + \frac { w _ { n + 2 } } { W _ { n + 2 } } + \cdot \cdot \cdot + \frac { w _ { n + p } } { W _ { n + p } } > \frac { w _ { n + 1 } + \cdot \cdot \cdot + w _ { n + p } } { W _ { n + p } } } } \\ & { } & { \quad = \frac { W _ { n + p } - W _ { n } } { W _ { n + p } } = 1 - \frac { W _ { n } } { W _ { n + p } } } \end{array}
$$

For every fixed $\pmb { n }$ , this last fraction approaches 1. Hence, from some $\pmb { p }$ on, the partial sums exceed, say, $\pmb { \frac { 1 } { 2 } }$ .The tails of a convergent series cannot all exceed a fixed amount,and hence (9.3.l4) diverges.We have

$$
\sum _ { n = 2 } ^ { N } \left( \frac { 1 } { W _ { n - 1 } } - \frac { 1 } { W _ { n } } \right) = \frac { 1 } { W _ { 1 } } - \frac { 1 } { W _ { N } } .
$$

Therefore the series

$$
\sum _ { n = 2 } ^ { \infty } \left( { \frac { 1 } { W _ { n - 1 } } } - { \frac { 1 } { W _ { n } } } \right) = \sum _ { n = 2 } ^ { \infty } { \frac { W _ { n } - W _ { n - 1 } } { W _ { n - 1 } W _ { n } } }
$$

is convergent. Thus,

$$
\sum _ { n = 2 } ^ { \infty } \frac { w _ { n } } { W _ { n - 1 } W _ { n } } < \infty
$$

and a fortiori

$$
\sum _ { n = 1 } ^ { \infty } { \frac { w _ { n } } { \boldsymbol { W _ { n } } ^ { 2 } } } < \infty .
$$

LEMMA 9.3.7 (Landau). Let $\left\{ a _ { n } \right\}$ be $\pmb { a }$ fixed sequence of complex numbers and suppose hat $\sum _ { n = 1 } ^ { \infty } a _ { n } b _ { n }$ covergesfor al eguenes $\left\{ b _ { n } \right\}$ for which

$$
\sum _ { n = 1 } ^ { \infty } | b _ { n } | ^ { 2 } < \infty .
$$

Then,

$$
\sum _ { n = 1 } ^ { \infty } | a _ { n } | ^ { 2 } < \infty .
$$

Proof: Suppose that $\sum _ { \ i = 1 } ^ { \infty } | a _ { n } | ^ { 2 } = \infty$ Set $b _ { n } = { \frac { { \overline { { a _ { n } } } } } { | a _ { 1 } | ^ { 2 } + \cdots + | a _ { n } | ^ { 2 } } }$ . Then by (9.3.15）with $w _ { n } = | a _ { n } | ^ { 2 } , \sum _ { n = 1 } ^ { \infty } | b _ { n } | ^ { 2 } < \infty$ 、On the other hand,by (9.3.14), $\sum _ { n = 1 } ^ { \infty } a _ { n } b _ { n } = \infty$ ,and this contradicts the hypothesis.

THEOREM 9.3.8．Let $\pmb { H }$ be $^ { \pmb { a } }$ Hilbert space and $\{ { x _ { n } } ^ { * } \}$ $^ { \pmb { a } }$ complete orthonormal sequence. Let $L$ be $^ { \pmb { a } }$ linear functional defined on $\pmb { H }$ and suppose that for all $\pmb { x } \in \pmb { H }$ we have

$$
L ( x ) = \sum _ { k = 1 } ^ { \infty } ( x , { x _ { k } } ^ { * } ) L ( { x _ { k } } ^ { * } ) .
$$

Then $\pmb { L }$ is bounded on $\pmb { H }$ and

$$
\| L \| ^ { 2 } = \sum _ { k = 1 } ^ { \infty } | L ( x _ { k } ^ { \ast } ) | ^ { 2 } .
$$

Proof: By_ Theorems 8.9.1(C) and 8.9.2, the set of all sequences $b _ { k } =$ $( x , x _ { k } ^ { * } )$ ， $\pmb { x } \in \pmb { H }$ ,is identical to the set of all sequences $\left\{ b _ { k } \right\}$ for which

$$
\sum _ { k = 1 } ^ { \infty } | b _ { k } | ^ { 2 } < \infty .
$$

By Lemma 9.3.7,

$$
\sum _ { k = 1 } ^ { \infty } | L ( x _ { k } ^ { } ^ { * } ) | ^ { 2 } < \infty .
$$

Applying the Schwarz inequality to (9.3.16),

$$
| L ( x ) | ^ { 2 } \leq \sum _ { k = 1 } ^ { \infty } | ( x , x _ { k } ^ { * } ) | ^ { 2 } \sum _ { k = 1 } ^ { \infty } | L ( x _ { k } ^ { * } ) | ^ { 2 } = \| x \| ^ { 2 } \sum _ { k = 1 } ^ { \infty } | L ( x _ { k } ^ { * } ) | ^ { 2 } .
$$

$\pmb { L }$ is therefore bounded,and (9.3.17) follows from (9.3.13).

For examples illustrating this theorem, see Corollary 12.5.5.

THEOREM 9.3.9． Let $\pmb { H }$ be a Hilbert space .Let $H ^ { * }$ be its normed conjugate space. Then $H ^ { * }$ can be made into $\pmb { a }$ Hilbert space in such $\pmb { a }$ way that $\pmb { H }$ and $H ^ { * }$ are essentially the same. More precisely, we can find $^ { \pmb { a } }$ one to one correspondence $(  )$ between $\pmb { H }$ and $H ^ { * }$ such that

(a) $\pmb { x _ { 1 } }  \pmb { L _ { 1 } }$ ， ${ \pmb x } _ { 2 }  { \pmb L } _ { 2 }$ implies $a _ { 1 } x _ { 1 } + a _ { 2 } x _ { 2 }  a _ { 1 } L _ { 1 } + a _ { 2 } L _ { 2 } .$   
(b) $x  L$ implies $\| { \pmb x } \| = \| { \pmb L } \|$   
(c)An inner product can be introduced in $H ^ { * }$ by writing $( L _ { 1 } , L _ { 2 } ) = ( x _ { 1 } , x _ { 2 } )$ where $\pmb { x _ { 1 } }  \pmb { L _ { 1 } }$ ， $x _ { 2 }  L _ { 2 }$   
(d）The norm arising from this inner product coincides with te originalnorn in $H ^ { * }$ (i., $\| L \| = \operatorname* { s u p } _ { \pmb { x } \in \pmb { H } } \frac { | L ( \pmb { x } ) | } { \| \pmb { x } \| } \bigg ) .$

Proof: Let $\{ { { x } _ { i } } ^ { * } \}$ be a complete orthonormal system in $\pmb { H }$ Let $L \in H ^ { * }$ By Theorem 9.3.3, we have ${ \cal L } ( y ) = ( y , w )$ for a unique $w \in H$ and for all $y \in H$ .The quantities $( w , x _ { i } ^ { * } )$ are the Fourier coefficients of $\pmb { w }$ and hence, $\| w \| ^ { 2 } = \sum _ { i = 1 } ^ { \infty } | ( w , x _ { i } { ^ { * } } ) | ^ { 2 } < \infty$ The quantities $( { x _ { i } } ^ { * } , w ) = \overline { { ( w , { x _ { i } } ^ { * } ) } }$ satisfy the same inequality $\sum _ { i = 1 } ^ { \infty } | ( x _ { i } ^ { \ast } , w ) | ^ { 2 } < \infty$ and hence by Theorems 8.9.2 and ${ \bf 8 . 9 . 1 ( F ) }$ ,they are the Fourier coeffcients of a unique element $\in H$ which will be designated by $\bar { \boldsymbol { w } }$ .Note that $\| \bar { \boldsymbol { w } } \| = \| \boldsymbol { w } \|$

Make the correspondence $L  \bar { w }$ 、This correspondence is one to one between the whole of $\pmb { H }$ and the whole of $H ^ { * }$ .For,each $\pmb { L } \in \pmb { H } ^ { * }$ determines a $w \in H$ and each w determines a $\bar { \boldsymbol { w } }$ If $L _ { 1 } \to w _ { 1 }$ and ${ \cal L } _ { 2 } \to w _ { 2 }$ then $\begin{array} { r } { L _ { 1 } \neq L _ { 2 } } \end{array}$ implies $w _ { 1 } \neq w _ { 2 }$ For we can find an ${ \pmb x } \in { \pmb H }$ such that $L _ { 1 } ( x ) \neq L _ { 2 } ( x )$ Therefore $0 \neq L _ { 1 } ( x ) - L _ { 2 } ( x ) = ( x , w _ { 1 } ) - ( x , w _ { 2 } )$ Hence $w _ { 1 } \neq w _ { 2 }$ Now $\overline { { w _ { 1 } } } \neq \overline { { w _ { 2 } } }$ For otherwise, $( \overline { { w _ { 1 } } } , x _ { i } { ^ { * } } ) = ( \overline { { w _ { 2 } } } , x _ { i } { ^ { * } } )$ ， $i = 1 , 2 ,$ ... . Then $\begin{array} { r } { \overline { { ( w _ { 1 } , x _ { i } { ^ * } ) } } = \overline { { ( w _ { 2 } , x _ { i } { ^ * } ) } } , } \end{array}$ $i = 1 , 2 , \dots { } _ { ; }$ implying $w _ { 1 } = w _ { 2 }$

Conversely, let ${ \pmb v } \in { \pmb H }$ Consider $\bar { v }$ as above and define $L$ by means of ${ \cal L } ( { \pmb x } ) = ( { \pmb x } , { \bar { \pmb v } } )$ .By the above,the element $\overline { { \overline { { v } } } }$ corresponds to $L$ But $\overline { { \overline { { v } } } } = v$ Thus $v$ corresponds to some $\pmb { L }$ in $H ^ { * }$

(a）Let $x _ { 1 }  L _ { 1 }$ ， $x _ { 2 }  L _ { 2 }$ . Then,

$$
L _ { 1 } ( x ) = ( x , { \overline { { x _ { 1 } } } } ) , L _ { 2 } ( x ) = ( x , { \overline { { x _ { 2 } } } } )
$$

so that

$$
( a _ { 1 } L _ { 1 } + a _ { 2 } L _ { 2 } ) ( x ) = a _ { 1 } L _ { 1 } ( x ) + a _ { 2 } L _ { 2 } ( x ) = ( x , \bar { a } _ { 1 } \bar { x } _ { 1 } + \bar { a } _ { 2 } \bar { x } _ { 2 } ) .
$$

Now

$$
\overline { { a _ { 1 } x _ { 1 } + a _ { 2 } x _ { 2 } } } = \bar { a } _ { 1 } \overline { { x } } _ { 1 } + \bar { a } _ { 2 } \overline { { x } } _ { 2 } .
$$

Hence

$$
( a _ { 1 } L _ { 1 } + a _ { 2 } L _ { 2 } ) ( x ) = ( x , \overline { { { a _ { 1 } x _ { 1 } + a _ { 2 } x _ { 2 } } } } )
$$

and therefore

$$
a _ { 1 } L _ { 1 } + a _ { 2 } L _ { 2 }  a _ { 1 } x _ { 1 } + a _ { 2 } x _ { 2 } .
$$

(b)If $w  L$ then ${ \cal L } ( x ) = ( x , \bar { w } )$ Hence by (9.3.9), $\| L \| = \| { \bar { \boldsymbol { w } } } \| = \| \pmb { w } \|$ (c) The inner product properties of $( L _ { 1 } , L _ { 2 } )$ follow from those in $\pmb { H }$ ：

$$
( L _ { 1 } + L _ { 2 } , L _ { 3 } ) = ( x _ { 1 } + x _ { 2 } , x _ { 3 } ) = ( x _ { 1 } , x _ { 3 } ) + ( x _ { 2 } , x _ { 3 } ) = ( L _ { 1 } , L _ { 3 } ) + ( L _ { 2 } , L _ { 3 } ) .
$$

$$
( L _ { 1 } , L _ { 2 } ) = ( x _ { 1 } , x _ { 2 } ) = \overline { { { ( x _ { 2 } , x _ { 1 } ) } } } = \overline { { { ( L _ { 2 } , L _ { 1 } ) } } } .
$$

$$
( \alpha L _ { 1 } , L _ { 2 } ) = ( \alpha x _ { 1 } , x _ { 2 } ) = \alpha ( x _ { 1 } , x _ { 2 } ) = \alpha ( L _ { 1 } , L _ { 2 } ) .
$$

$( L _ { 1 } , L _ { 1 } ) = ( x _ { 1 } , x _ { 1 } ) = \| x _ { 1 } \| ^ { 2 } > 0$ and ${ \bf \omega } = { \bf 0 }$ if and only if ${ \pmb x _ { 1 } } = { \bf 0 }$ e if and only if $L _ { 1 } = 0$

(d) $( L , L ) ^ { \frac { 1 } { 2 } } = ( x , x ) ^ { \frac { 1 } { 2 } } = \| { \pmb x } \| = \| { \overline { { { \pmb x } } } } \|$ . Since $L ( y ) = ( y , { \overline { { x } } } ) , y \in H , \| L \| = \| { \overline { { x } } } \| .$ Hence $\| L \| = ( L , L ) ^ { \frac { 1 } { 2 } }$

Thus, $H ^ { * }$ is an inner product space.To show completeness we need to prove that $\| L _ { m } - L _ { n } \| \leq \varepsilon , m , n \geq N _ { \varepsilon }$ implies the existence of an $\scriptstyle { \cal L }$ with $\| L - L _ { n } \| \to 0$ Let $L _ { n }  x _ { n }$ .Then $\| x _ { n } - x _ { m } \| = \| L _ { n } - L _ { m } \| \leq \varepsilon$ for $m , n \geq N _ { \varepsilon }$ . Thus, $\{ x _ { n } \}$ is a Cauchy sequence in $\pmb { H }$ .Hence there is an $\pmb { x } \colon \| \pmb { x } - \pmb { x _ { n } } \|  0 .$ If ${ \pmb x }  { \pmb L }$ then $\| L - L _ { n } \| = \| x - x _ { n } \| \to 0$

Finally,there is a complete orthonormal sequence in $H ^ { * }$ .For if $\{ x _ { k } * \}$ is complete and orthonormal in $\pmb { H }$ and ${ x _ { n } } ^ { * }  { L _ { n } } ^ { * }$ then $\{ L _ { n } { } ^ { * } \}$ is complete and orthonormal in $H ^ { * }$ $H ^ { * }$ is therefore a Hilbert space.

In virtue of (9.3.18), the spaces $\pmb { H }$ and $H ^ { * }$ are known as isomorphic and isometric.

DEFINITION 9.3.6． Let $\pmb { X }$ be an inner product space. $\pmb { Y }$ is an arbitrary subset of $\pmb { X }$ .The set of elements $_ { \pmb { x } }$ that are orthogonal to all elements of $\pmb { Y }$ is known as the orthogonal complement of $\boldsymbol { Y }$ and is designated by $\pmb { Y } ^ { \perp }$ .In symbols: $( x , y ) = 0$ for all $x \in Y ^ { \perp }$ and all $y \in Y$

Ex.8.In $R _ { 2 }$ ,the orthogonal complement of the $_ { \pmb { x } }$ axis is the $_ y$ axis.

Ex.9． Orthogonal complements are closed sets.

The following decomposition theorem holds.

THEOREM 9.3.10．Let $\pmb { X }$ be a complete inner product space. Let $M$ be $^ { a }$ closed linear subspace and $M ^ { \perp }$ its orthogonal complement. Then any $x \in X$ may be written uniquely as

$$
{ x = m + m ^ { \perp } }
$$

where $m \in M$ and $m ^ { \perp } \in M ^ { \perp }$

Proof:We show first that $M$ is complete. If $\{ m _ { k } \}$ is a Cauchy sequence of elements of $\boldsymbol { \mathcal { M } }$ ，then by the completeness of $\pmb { X }$ there is an element $x \in X$ such that $\operatorname* { l i m } _ { k \to \infty } \| x - m _ { k } \| = 0$ .But,by the closure of $M$ ， $_ { x }$ must be in $M$ Hence every Cauchy sequence of elements of $M$ has a limit in $M$

Let $x \in X$ be a fixed element and consider $( m , x )$ as $\mathbf { \nabla } m$ varies over $M$ By Theorem 9.3.3,there is an $m _ { 1 } \in M$ such that $( m , m _ { 1 } ) = ( m , x )$ for all $m \in M$ Write

$$
x = m _ { 1 } + ( x - m _ { 1 } ) .
$$

Now if $m ^ { \prime } \in M$ ， $( x - m _ { 1 } , m ^ { \prime } ) = ( x , m ^ { \prime } ) - ( m _ { 1 } , m ^ { \prime } ) = 0 .$ Hence ${ \pmb x } - m _ { 1 } \in { \pmb M } ^ { \bot }$ . The decomposition is unique.For suppose $m _ { 1 } + m _ { 1 } { } ^ { \perp } = m _ { 2 } + m _ { 2 } { } ^ { \perp }$ . Then $m _ { 1 } - m _ { 2 } = m _ { 2 } ^ { \perp } - m _ { 1 } ^ { \perp }$ .But $m _ { 1 } - m _ { 2 } \in M$ and $m _ { 2 } ^ { \perp } - m _ { 1 } ^ { \perp } \in { \bf { \cal M } } ^ { \perp }$ . Now the only element simultaneously in $M$ and $M ^ { \perp }$ is O and hence $m _ { 1 } = m _ { 2 }$ ， ${ m _ { 1 } } ^ { \perp } =$ $m _ { 2 } ^ { \mathrm { ~ \perp ~ } }$

DEFINITioN 9.3.7. The unique element m determined from $_ { x }$ is called the projection of $_ { x }$ on $M$ ： $m = \operatorname { p r o j } ( x )$

LEMMA 9.3.11． If $\pmb { X }$ is a separable metric space and $s$ is an arbitrary subset of $\pmb { X }$ ， $\pmb { S }$ is also separable.

Proof: Let $\left\{ x _ { k } \right\}$ be a sequence of elements that is dense in $\pmb { X }$ The set of points $\pmb { x }$ of $\pmb { X }$ satisfying $d ( x , x _ { k } ) < r$ is a ball of radius $\pmb { r }$ centered at $x _ { k }$ Designate it by $U ( x _ { k } , r )$ and consider all the balls $U ( \boldsymbol { x } _ { k } , \boldsymbol { r } )$ where $\pmb { r }$ runs through all the positive rational numbers.These form a denumerable set and hence can be listed as a sequence $U _ { \bf 1 } , U _ { \bf 2 } , \dots .$

If $_ { x }$ is an arbitrary element of $\pmb { X }$ ,and if $V ( x , \pmb { \rho } )$ is any ball with center at ${ \pmb x } _ { : }$ ,then we can find an m such that $x \in U _ { m } \subseteq V ( x , \rho )$ .For select an $\boldsymbol { x } _ { j }$ with $d ( x , x _ { j } ) < \rho / 2$ and a rational $\pmb { \rho _ { 1 } }$ with $d ( x , x _ { j } ) < \rho _ { 1 } < \rho / 2$ .If $z \in U ( x _ { j } , \rho _ { 1 } )$ ， then $d ( z , x _ { j } ) < \rho _ { 1 }$ But $d ( z , x ) \leq d ( z , x _ { j } ) + d ( x _ { j } , x ) < \rho / 2 + \rho / 2 = \rho$ and hence $z \in V ( { \pmb x } , { \pmb \rho } )$

Now consider the members of the sequence $U _ { \bf 1 } , U _ { \bf 2 } , . . . .$ ,that have points in common with $\pmb { S }$ .These are also denumerable,and hence can be listed in a sequence. Call them $\pmb { T _ { 1 } } , \pmb { T _ { 2 } } , \dots .$

For each $\pmb { k }$ select a $y _ { k } \in T _ { k } \cap { \mathcal { S } } .$ The sequence $\left\{ y _ { k } \right\}$ is dense in $\pmb { S } ,$ For let $z \in \mathcal S$ and $\varepsilon > 0$ be given. As we have seen,we can find a $U _ { m }$ such that $z \in U _ { m }$ and $U _ { m } \subset V ( z , \varepsilon ) . \ U _ { m }$ contains a point of $\pmb { S }$ and is therefore a $\pmb { T _ { n } }$ $\pmb { T _ { n } }$ contains $y _ { n }$ ,and hence $d ( y _ { n } , z ) < \varepsilon$

THEOREM 9.3.12．Let $\pmb { H }$ be a Hilbert space and $\{ { x _ { k } } ^ { * } \}$ be an orthonormal sequence that is not complete. Then we can find $\pmb { a }$ sequence of elements $\{ y _ { k } ^ { * } \}$ (finite or infinite) such that $\{ { x _ { k } } ^ { * } \}$ and $\left\{ y _ { k } ^ { * } \right\}$ together form $\pmb { a }$ complete orthonormal set (cf. Lemma 9.1.1).

Proof: Designate by $\pmb { M }$ the closed linear subspace generated by ${ \pmb x _ { 1 } } ^ { * }$ ， ${ \pmb x _ { 2 } } ^ { * }$ ,.... That is, $\pmb { M }$ consists of all finite linear combinations of ${ \pmb x } _ { \imath } ^ { * }$ plus the limits of sequences of such combinations. $M ^ { \perp }$ is the orthogonal complement of $M$ .Since $\pmb { H }$ is separable (cf. 9.1),Lemma 9.3.ll tells us that $M ^ { \perp }$ is also separable.Let $\left\{ z _ { k } \right\}$ be a sequence of elements of $M ^ { \perp }$ that is dense in $M ^ { \perp }$ . Go through the sequence $z _ { 1 } , z _ { 2 } , \ldots$ , and strike out any element that is dependent on its predecessors.Call the independent sequence that remains $\left\{ y _ { k } \right\}$ .Orthonormalize this sequence to yield $\{ { y _ { k } } ^ { * } \}$ ·

If $z \in M ^ { \perp }$ , and if $\varepsilon > 0$ isgiven,e $\sum _ { i = 1 } ^ { n } a _ { k } { y _ { k } } ^ { * }$ such that $\left\| z - \sum _ { k = 1 } ^ { n } a _ { k } y _ { k } { } ^ { * } \right\| \leq \varepsilon .$ For, we can find a $\pmb { k }$ such that $\| z - z _ { k } \| \leq \varepsilon$ Now $z _ { k }$ is either a $y _ { j }$ or a linear combination of $y _ { 1 } , y _ { 2 } , \ldots$ , and hence a linear combination of $y _ { 1 } { ^ { * } } , y _ { 2 } { ^ { * } }$ ：

Since ${ \boldsymbol { y _ { k } } ^ { * } } \in \pmb { M } ^ { \perp }$ ， $( { x _ { j } } ^ { * } , { y _ { k } } ^ { * } ) = 0$ and hence the combined set $\{ x _ { j } ^ { \ast } \} , \{ y _ { k } ^ { \ast } \}$ is   
orthonormal. This combined set is closed in $\pmb { H }$ For let ${ \pmb x } \in { \pmb H }$ By Theorem   
9.3.10 we can write ${ \pmb x } = m + m ^ { \perp }$ . Now by the definition of $M$ ,for appro-$_ { k } , \left\| \begin{array} { l l } { m - \sum _ { k = 1 } ^ { p } b _ { k } { x _ { k } } ^ { * } } \end{array} \right\| \le \varepsilon / 2$ $\|  m ^ { \perp } - \sum _ { k = 1 } ^ { q } b _ { k } ^ { \prime } y _ { k } ^ { \ast } \| \leq \varepsilon / 2$ Hone

$$
\left\| { x - \sum _ { k = 1 } ^ { p } b _ { k } { x _ { k } } ^ { * } - \sum _ { k = 1 } ^ { q } { b _ { k } } ^ { \prime } { y _ { k } } ^ { * } } \right\| \leq \varepsilon .
$$

This completes the proof.

THEOREM 9.3.13．Let $\pmb { H }$ and $\pmb { K }$ be two Hilbert spaces (either both real or both complex). Then $\pmb { H }$ and $\pmb { K }$ are isomorphic and isometric. That is, we can find $\pmb { a }$ one to one mapping $\pmb { T }$ of $\pmb { H }$ onto $\pmb { K }$ such that for all constants $\alpha , \beta$

$$
T ( \alpha x _ { 1 } + \beta x _ { 2 } ) = \alpha T ( x _ { 1 } ) + \beta T ( x _ { 2 } ) , \qquad x _ { 1 } , x _ { 2 } \in H
$$

and such that

$$
( T ( x _ { 1 } ) , T ( x _ { 2 } ) ) = ( x _ { 1 } , x _ { 2 } ) .
$$

Proof: It suffices to take $\pmb { K }$ as $\ell ^ { 2 }$ (real or complex as the case may be). For since isomorphisms and isometries are obviously transitive,the general case can be proved by going through $\ell ^ { 2 }$ as an intermediate space.

Let $x _ { 1 } ^ { * } , x _ { 2 } ^ { * }$ 。..， be a complete orthonormal sequence in $\pmb { H }$ Forany ${ \pmb x } \in { \pmb H }$ ，the sequence of constants $a _ { k } = ( x , x _ { k } { } ^ { * } )$ ， $k = 1 , 2 , \ldots$ isin $\ell ^ { 2 }$ by (8.9.7). Define $\pmb { T }$ by $\pmb { \mathcal { T } } ( \pmb { x } ) = \{ a _ { \pmb { k } } \}$ .Conversely，by Theorem 8.9.2， to any sequence $\left\{ a _ { k } \right\} \in \ell ^ { 2 }$ ,there is a unique element $\pmb { x } \in \pmb { H }$ such that $\pmb { T } ( \pmb { x } ) = \{ a _ { k } \}$

The linearity of $\pmb { T }$ is obvious. Property (9.3.22) follows from (8.9.8).

# 9.4 Linear Varieties and Hyperplanes; Interpolation and Approximation in Hilbert Space

DEFINITION 9.4.1． Let $x _ { 1 } , \ldots , x _ { n }$ be $\pmb { n }$ independent elements of a linear space.The set of all linear combinations

$$
x _ { 0 } + \sum _ { i = 1 } ^ { n } a _ { i } x _ { i }
$$

is known as a linear variety of dimension $\pmb { n }$

DEFINITION 9.4.2. Let ${ \pmb x _ { 1 } } , { \pmb x _ { 2 } } , \ldots , { \pmb x _ { n } }$ be $\pmb { n }$ independent elements of an inner product space and let $c _ { 1 } , c _ { 2 } , \ldots , c _ { n }$ be $\pmb { n }$ given constants. The set of elements $\pmb { y }$ that simultaneously satisfy the $\pmb { n }$ equations

$$
( y , x _ { i } ) = c _ { i } , \qquad i = 1 , 2 , \ldots , n ,
$$

is known as a hyperplane of co-dimension $\pmb { n }$

Ex.l． Linear varieties and hyperplanes are convex sets.

If $x _ { 1 } , \ldots , x _ { n }$ are orthonormalized to produce ${ x _ { 1 } } ^ { * } , \ldots , { x _ { n } } ^ { * }$ ，then by Corollary 8.3.5,we can write the variety in the form

$$
{ \pmb x _ { 0 } } + \sum _ { i = 1 } ^ { n } a _ { i } { x _ { i } } ^ { * }
$$

and the hyperplane in the form

$$
( y , x _ { i } { ^ { * } } ) = d _ { i } , \qquad i = 1 , 2 , \ldots , n .
$$

In an inner product space of finite dimension $\pmb { n }$ ,the concepts of linear variety and hyperplane are equivalent.More precisely,a linear variety of dimension $\pmb { \mathscr { p } }$ ， $1 \leq p < n$ ,is a hyperplane of co-dimension $\mathcal { n } - \mathcal { p }$ and vice versa. For let $y = x _ { 0 } + \sum _ { i = 1 } ^ { p } a _ { i } x _ { i } { } ^ { * }$ be a variety $\pmb { V }$ of dimension $\pmb { p }$ . Then $( y , x _ { k } { ^ * } ) = ( x _ { 0 } , x _ { k } { ^ * } )$ for $k = p + 1 , p + 2 , \ldots , n$ and hence $\pmb { y }$ lies on a hyperplane of co-dimension $\mathbf { \boldsymbol { n } } - \mathbf { \boldsymbol { p } }$ .Conversely, let $\pmb { y }$ satisfy $( y , x _ { k } { ^ * } ) = ( x _ { 0 } , x _ { k } { ^ * } )$ ， $k = p + 1 , \ldots , n$ $\pmb { z }$ $z = \sum _ { k = 1 } ^ { n } ( z , x _ { k } * ) x _ { k } *$ hare $\begin{array} { r } { \pmb { y } = } \end{array}$ $\sum _ { k = 1 } ^ { p } ( y , x _ { k } ^ { * } ) x _ { k } ^ { * } + \sum _ { k = p + 1 } ^ { n } ( x _ { 0 } , x _ { k } ^ { * } ) { x _ { k } ^ { * } } = x _ { 0 } + \sum _ { k = 1 } ^ { p } [ ( y , x _ { k } ^ { * } ) - ( x _ { 0 } , x _ { k } ^ { * } ) ] { x _ { k } } ^ { * } .$ $\pmb { y }$ lies on $V$ 、In the same way we can show that every hyperplane of co-dimension $\pmb { p }$ is a linear variety of dimension $\mathscr { n } - \mathscr { p }$

We begin with the problem of finite interpolation. This is essentially an instance of Theorem 2.2.2.

THEOREM 9.4.1. Let $\boldsymbol { \cal X }$ be an inner product space. Let $x _ { 1 } , \ldots , x _ { n }$ be $\pmb { n }$ independent elements. Then given any set of $\pmb { n }$ constants $c _ { 1 } , \ldots , c _ { n }$ we can find an element $_ y$ such that

$$
( y , x _ { i } ) = c _ { i } , \qquad i = 1 , 2 , \ldots , n .
$$

Proof: We can find a solution among the linear combinations of the $x _ { i }$ Set $y = a _ { 1 } x _ { 1 } + \cdots + a _ { n } x _ { n }$ Then (9.4.5） becomes

$$
a _ { 1 } ( x _ { 1 } , x _ { i } ) + \cdot \cdot \cdot + a _ { n } ( x _ { n } , x _ { i } ) = c _ { i } , \qquad i = 1 , 2 , \ldots , n .
$$

The system (9.4.6) has determinant $g ( x _ { 1 } , \ldots , x _ { n } ) \neq 0$ in view of the independence of the $\pmb { x } _ { i }$ .Hence there is a solution for any assignment of $\pmb { c } \mathbf { \acute { s } }$

When we consider an interpolation problem with infinitely many conditions,the situation is not so simple.

Ex.2. In the sequential Hilbert space ${ \pmb \ell } ^ { 2 }$ ,let $x _ { 1 } = ( 1 , 0 , 0 , \ldots )$ ， $x _ { 2 } = ( 0 , 1 , 0 ,$ $0 , \ldots . ) , \ldots .$ ,and consider the problem

$$
( y , x _ { i } ) = 1 , \qquad i = 1 , 2 , \ldots .
$$

These conditions obviously require a solution of the form $y = ( 1 , 1 , 1 , \ldots )$ . But this element is not in the Hilbert space.

THEOREM 9.4.2． Let $\left\{ x _ { i } \right\}$ be an infinite sequence of independent elements of a Hilbert space $\pmb { H }$ and let constants $\left\{ c _ { i } \right\}$ be given. $\pmb { A }$ necessary and sufficient condition that there exist an element $y \in H$ such that

$$
( y , x _ { i } ) = c _ { i } , \qquad i = 1 , 2 , \ldots ,
$$

is that

$$
\sum _ { k = 1 } ^ { \infty } | a _ { k } | ^ { 2 } < \infty
$$

where

$$
\bar { a } _ { 1 } = \bar { c } _ { 1 } / \sqrt { g ( x _ { 1 } ) } ,
$$

$$
\scriptstyle \mathbf { \Sigma } _ { n } = { \frac { 1 } { \sqrt { g ( x _ { 1 } , \ \dotsc \ , x _ { n - 1 } ) g ( x _ { 1 } , \ \dotsc \ , x _ { n } ) } } } \left| { \begin{array} { c c c c c } { ( x _ { 1 } , x _ { 1 } ) } & { ( x _ { 2 } , x _ { 1 } ) } & { \ \cdots } & { ( x _ { n } , x _ { 1 } ) } \\ { \cdot } & { \cdot } & { \cdot } \\ { \cdot } & { \cdot } & { \cdot } \\ { \cdot } & { \cdot } & { \cdot } \\ { ( x _ { 1 } , x _ { n - 1 } ) } & { ( x _ { 2 } , x _ { n - 1 } ) } & { \cdots } & { ( x _ { n } , x _ { n - 1 } ) } \\ { \bar { c } _ { 1 } } & { \bar { c } _ { 2 } } & { \cdot \cdot } & { \bar { c } _ { n } } \end{array} } \right| .
$$

$$
n > 1 .
$$

If there is a solution, it is unique if and only if $\{ x _ { i } \}$ is complete (or closed) in $\pmb { H }$

Proof:Orthonormalize the $\pmb { x } _ { k }$ using Theorem 8.3.3 and obtain ${ x _ { k } } ^ { * }$ In view of (8.7.22), the conditions (9.4.8) imply

$$
( y , x _ { i } ^ { * } ) = a _ { i } \qquad i = 1 , 2 , . . . .
$$

Conversely,it is easily shown through (8.3.7), that (9.4.1l) implies (9.4.8). Now if there is a $y \in H$ satisfying (9.4.11), then by Corollary 8.5.4,(9.4.9) follows.Conversely,if (9.4.9) holds,then by Theorem 8.9.2,there is an element $_ y$ for which (9.4.1l) and hence (9.4.8) holds.

Suppose that $( y _ { 1 } , x _ { i } ) = c _ { i } = ( y _ { 2 } , x _ { i } )$ .Then $( y _ { 1 } - y _ { 2 } , x _ { i } ) = 0$ ， $i = 1 , 2 , \dots .$ If $\left\{ x _ { i } \right\}$ is complete then $y _ { 1 } - y _ { 2 } = 0$ and $y _ { 1 } = y _ { 2 }$ If $\left\{ x _ { i } \right\}$ is incomplete, then we can find an element $z \neq 0$ such that $( z , x _ { i } ) = 0$ ， $i = 1$ ,2,....Hence, $( y , x _ { i } ) = c _ { i } = ( y + z , x _ { i } )$ so that the solution to (9.4.8) is not unique.

Ex.3. Under what circumstances can we have $\int _ { - 1 } ^ { + 1 } f ( x ) x ^ { n } d x = c _ { n } , \ n$ $\textbf { \em n } = \textbf { 0 }$ ， $1 , . . .$ ，for $f \in L ^ { 2 } [ - 1 , 1 ]$ ? This is the moment problem for the space $L ^ { 2 } [ - 1 , 1 ]$ · Let $p _ { n } { } ^ { * } ( x ) = a _ { n 0 } + a _ { n 1 } x + \cdot \cdot \cdot + a _ { n n } x ^ { n }$ be the Legendre polynomials.Then the moment conditions above are totally equivalent to

$$
\int _ { - 1 } ^ { + 1 } f ( x ) { p _ { n } } ^ { * } ( x ) d x = a _ { n 0 } c _ { 0 } + a _ { n 1 } c _ { 1 } + \cdot \cdot \cdot + a _ { n n } c _ { n } .
$$

Hence,the necessary and suffcient condition is that

$$
\sum _ { n = 0 } ^ { \infty } \lvert a _ { n 0 } c _ { 0 } + a _ { n 1 } c _ { 1 } + \cdot \cdot \cdot + a _ { n n } c _ { n } \rvert ^ { 2 } < \infty .
$$

Since the powers are complete in $L ^ { 2 } [ - 1 , 1 ]$ (Theorem l1.2.l),there can be at most one solution.

Let $\pmb { X }$ be an inner product space and $x _ { 1 } , \ldots , x _ { n }$ be $\pmb { n }$ independent elements.Let $\pmb { S }$ be the linear subspace spanned by the $\scriptstyle { \boldsymbol { x } } ^ { \prime } \mathbf { s }$ .That is, $\pmb { S }$ consists of all linear combinations $y = a _ { 1 } x _ { 1 } + a _ { 2 } x _ { 2 } + \cdot \cdot \cdot + a _ { n } x _ { n }$ ，or alternatively, of all combinations $y = a _ { 1 } x _ { 1 } { * } + \dotsb + a _ { n } x _ { n } { * }$ where"the ${ \boldsymbol { x } _ { i } } ^ { * }$ are the $\pmb { x } _ { i }$ orthonormalized (in any way).Take an element $z \in X$ which is not perpendicular to all the ${ x _ { i } } ^ { * }$ ，and let $V$ consist of all the elements $y \in \mathcal S$ for which $( y , z ) = 1$ $V$ is a linear variety of dimension $\leq n - 1$ .For suppose that $( x _ { 1 } ^ { \ * } , z ) \neq 0$ If $y = a _ { 1 } x _ { 1 } { * } + \dotsb + a _ { n } x _ { n } { * }$ and $( y , z ) = 1$ ,then

$$
a _ { 1 } ( { x _ { 1 } } ^ { * } , z ) + \dotsb + a _ { n } ( { x _ { n } } ^ { * } , z ) = 1
$$

and so

$$
y = { \frac { { x _ { 1 } } ^ { * } } { ( { x _ { 1 } } ^ { * } , z ) } } + a _ { 2 } { \left( - { \frac { ( { x _ { 2 } } ^ { * } , z ) } { ( { x _ { 1 } } ^ { * } , z ) } } { x _ { 1 } } ^ { * } + { x _ { 2 } } ^ { * } \right) } + \cdot \cdot \cdot + a _ { n } { \left( - { \frac { ( { x _ { n } } ^ { * } , z ) } { ( { x _ { 1 } } ^ { * } , z ) } } { x _ { 1 } } ^ { * } + { x _ { n } } ^ { * } \right) }
$$

Since ${ \pmb x } _ { 1 } ^ { * } , \dots , { \pmb x } _ { n } ^ { * }$ are independent, the elements $- \frac { ( { x _ { i } } ^ { * } , z ) } { ( { x _ { 1 } } ^ { * } , z ) } { x _ { 1 } } ^ { * } + { x _ { i } } ^ { * } , i$ $i =$ $2 , \ldots , n$ are easily seen to be independent.Hence (9.4.12) is of form (9.4.1) and the elements of $V$ lie on the variety (9.4.l2). Conversely,all the elements of this variety are in $\pmb { S }$ and satisfy $( y , z ) = 1$ .Hence they belong to $V$

It is desired to find the element of $V$ closest to the origin.That is,select $y \in V$ such that $\| y \| = \operatorname* { m i n i m u m }$

THEOREM 9.4.3. The unique solution to the above problem is given by

$$
y = \sum _ { i = 1 } ^ { n } ( z , { x _ { i } } ^ { * } ) { x _ { i } } ^ { * } / \sum _ { i = 1 } ^ { n } | ( z , { x _ { i } } ^ { * } ) | ^ { 2 } .
$$

The minimal distance is given by

$$
\| y \| ^ { 2 } = 1 / \sum _ { i = 1 } ^ { n } | ( z , x _ { i } { } ^ { * } ) | ^ { 2 } .
$$

Prof: Sst $\sum _ { i = 1 } ^ { n } | ( z , x _ { i } { ^ { * } } ) | ^ { 2 } = s \neq 0$ and write $a _ { i } = \frac { ( z , x _ { i } { } ^ { * } ) } { s } + b _ { i }$ where he

$b _ { i }$ are now to be determined. Now, $1 = ( y , z ) = 1 + \sum _ { i = 1 } ^ { n } b _ { i } ( { x _ { i } } ^ { * } , z ) ,$ so that $\sum _ { i = 1 } ^ { n } b _ { i } ( x _ { i } { ^ { * } } , z ) = 0$ But

$$
\begin{array} { c } { { \displaystyle | | y | | ^ { 2 } = \sum _ { i = 1 } ^ { n } | a _ { i } | ^ { 2 } = \sum _ { i = 1 } ^ { n } \biggl ( \frac { ( z , x _ { i } ^ { * } ) } { s } + b _ { i } \biggr ) \biggl ( \frac { ( x _ { i } ^ { * } , z ) } { s } + \overline { { { b _ { i } } } } \biggr ) } } \\ { { = \frac { s } { s ^ { 2 } } + \frac { 1 } { s } \sum _ { i = 1 } ^ { n } b _ { i } ( x _ { i } ^ { * } , z ) + \frac { 1 } { s } \sum _ { i = 1 } ^ { n } \overline { { { b _ { i } } } } ( z , x _ { i } ^ { * } ) + \sum _ { i = 1 } ^ { n } | b _ { i } | ^ { 2 } } } \\ { { = \displaystyle \frac { 1 } { s } + \sum _ { i = 1 } ^ { n } | b _ { i } | ^ { 2 } . } } \end{array}
$$

The selection leading to the minimum $\| y \| ^ { 2 }$ is uniquely given by $\boldsymbol { b } _ { i } \equiv 0$ and the minimum value is $\frac { 1 } { s }$

We turn to a second problem of approximation under side conditions. Let ${ \pmb x } _ { 1 } , { \pmb x } _ { 2 } , \ldots , { \pmb x } _ { n }$ be $\pmb { n }$ independent elements and $d _ { 1 } , \ldots , d _ { n }$ be $\pmb { n }$ given constants.

Find

$$
\operatorname* { m i n } _ { \pmb { y } } \| \pmb { x } - \pmb { y } \|
$$

subject to

$$
( y , x _ { i } ) = d _ { i } , ~ i = 1 , 2 , . ~ . ~ . ~ , n .
$$

Geometrically speaking,find the shortest distance from the element $_ { \pmb { x } }$ to the hyperplane (9.4.16).

If we set ${ \pmb w } = { \pmb x } - { \pmb y }$ ,our problem becomes that of finding

$$
\operatorname* { m i n } _ { \boldsymbol { w } } \parallel \boldsymbol { w } \parallel
$$

subject to

$$
( w , x _ { i } ) = c _ { i } = ( x , x _ { i } ) - d _ { i } , i = 1 , 2 , \ldots , n .
$$

If the x's are orthonormalized (by Theorem 8.3.3) yielding x𝑥1\*,xz\*,...,n\*, then (9.4.l8) is totally equivalent to

$$
( w , x _ { i } ^ { * } ) = a _ { i }
$$

where $\pmb { a _ { i } }$ are given by (9.4.10).

THEOREM 9.4.4. Let $\pmb { H }$ be a Hilbert space. Then

$$
w = \sum _ { i = 1 } ^ { n } a _ { i } { x _ { i } } ^ { * }
$$

solves the problem (9.4.17), (9.4.18). Moreover,

$$
\operatorname* { m i n } _ { w } \| w \| ^ { 2 } = \sum _ { i = 1 } ^ { n } | a _ { i } | ^ { 2 } .
$$

Proof: The ${ x _ { i } } ^ { * }$ may be augmented yielding a complete orthonormal sequence for $\pmb { H }$ (Lemma 9.1.1). Then, for any element $w \in H$ ，

$$
\| w \| ^ { 2 } = \sum _ { i = 1 } ^ { \infty } | ( w , x _ { i } { ^ { * } } ) | ^ { 2 } .
$$

Any element w that satisfes (9.4.19) must therefore satisfy

$$
\| w \| ^ { 2 } = \sum _ { i = 1 } ^ { n } | a _ { i } | ^ { 2 } + \sum _ { i = n + 1 } ^ { \infty } | ( w , x _ { i } ^ { * } ) | ^ { 2 } .
$$

This expression is minimized if $( w , x _ { i } ^ { * } ) = 0$ for $i = n + 1 , n + 2 , . . .$ ,and we are led to (9.4.20).

COROLLARY 9.4.5. In a Hilbert space let $\pmb { x _ { 1 } \neq 0 }$ The problem of finding min $\| \pmb { w } \|$ subject to $( w , x _ { 1 } ) = d _ { 1 }$ is solved by $w = { \frac { d _ { 1 } } { \| x _ { 1 } \| ^ { 2 } } } x _ { 1 }$ . Furthermore,

$$
\operatorname* { m i n } \ \| w \| = \frac { | d _ { 1 } | } { \| x _ { 1 } \| } .
$$

CoROLLARY 9.4.6. The equation of any hyperplane of co-dimension l can be written in the“normal” form

$$
( y , x ^ { * } ) = d
$$

where $\pmb { x } ^ { * }$ is an appropriate element of unit length and $\pmb { d }$ is the distance from the origin to the hyperplane.

DEFINITIoN 9.4.3. The portion of a Hilbert space common to the hyperplane $P \colon ( x , x _ { i } ) = c _ { i }$ ， $i = 1 , 2 , \ldots , n$ and to the ball $\| \ b { x } \| \leq r$ is called a hypercircle, $c _ { r }$

As before,orthonormalize $x _ { 1 } , \ldots , x _ { n }$ by the Gram-Schmidt process,and complete the sequence of orthonormal elements yielding ${ x _ { 1 } } ^ { * } , { x _ { 2 } } ^ { * } ;$ .... The conditions $( x , x _ { i } ) = c _ { i }$ are equivalent to $( x , x _ { i } ^ { * } ) = a _ { i }$ ， $i = 1 , 2 , \ldots , n$ ，where the $\pmb { a } _ { i }$ are given by (9.4.l0).Hence,any element $_ { \ast }$ of the hyperplane can be written as $x = \sum _ { k = 1 } ^ { n } a _ { k } x _ { k } { } ^ { * } + \sum _ { k = n + 1 } ^ { \infty } ( x , x _ { k } { } ^ { * } ) x _ { k } { } ^ { * } = w + \sum _ { k = n + 1 } ^ { \infty } ( x , x _ { k } { } ^ { * } ) x _ { k } { } ^ { * } .$ The last equality follows from (9.4.20).Now, $\| x \| ^ { 2 } = \| w \| ^ { 2 } + \sum _ { k = n + 1 } | ( x , x _ { k } \ast ) | ^ { 2 }$ If $x \in C _ { r }$ $r ^ { 2 } \geq \| x \| ^ { 2 } \geq \| w \| ^ { 2 }$ .The element $\pmb { w }$ is determined solely by $x _ { i }$ and $\pmb { c _ { i } }$ $i = 1 , 2 , \ldots , n$ ，and is independent of $\pmb { r }$ .If $r < \| w \|$ ,the hypercircle contains no elements.

THEOREM 9.4.7 (The Hypercircle Inequality). Let w be the element of the hyperplane $P$ nearest to the origin. Then,for any $x \in C _ { r }$ and any bounded linearfunctional $\pmb { L }$ we have

$$
| L ( x ) - L ( w ) | ^ { 2 } \leq ( r ^ { 2 } - \| w \| ^ { 2 } ) \sum _ { k = n + 1 } ^ { \infty } | L ( x _ { k } ^ { * } ) | ^ { 2 } .
$$

1f $\pmb { h }$ is the representer of $L$ ,this may be written as

$$
| L ( x ) - L ( w ) | ^ { 2 } \leq ( r ^ { 2 } - \| w \| ^ { 2 } ) \ ( \| h \| ^ { 2 } - \sum _ { k = 1 } ^ { n } | L ( x _ { k } ^ { * } ) | ^ { 2 } ) .
$$

Moreover, if $\| w \| \leq r$ ， there is an element in $C _ { r }$ for which this inequality becomes an equality.

Proof: From the above remarks, $x - w = \sum _ { k = n + 1 } ^ { \infty } ( x , { x _ { k } } ^ { * } ) { x _ { k } } ^ { * }$ and hence by (9.3.12), $L ( x - w ) = \mathrm { ~ \sum ~ } ^ { \infty } \mathrm { ~ } ( x , x _ { k } { } ^ { * } ) L ( x _ { k } { } ^ { * } )$ .By the Schwarz inequality and k=n+1 8 (8.9.7), $| L ( x - w ) | ^ { 2 } \leq \| x - w \| ^ { 2 } \sum _ { k = n + 1 } | L ( x _ { k } ^ { * } ) | ^ { 2 }$ Since $x - w \perp w$

$$
\| x - w \| ^ { 2 } = \| x \| ^ { 2 } - \| w \| ^ { 2 } \leq r ^ { 2 } - \| w \| ^ { 2 } .
$$

Combining,we obtain (9.4.23). By (9.3.5), $\sum _ { \ i = n + 1 } ^ { \infty } \lvert L ( { x _ { k } } ^ { * } ) \rvert ^ { 2 } = \sum _ { k = n + 1 } ^ { \infty } \lvert ( { x _ { k } } ^ { * } , h ) \rvert ^ { 2 } =$ $\sum _ { k = 1 } ^ { \infty } \vert ( h , { x _ { k } } ^ { * } ) \vert ^ { 2 } - \sum _ { k = 1 } ^ { n } \vert ( { x _ { k } } ^ { * } , h ) \vert ^ { 2 }$ Again by (8.9.7) and (9.3.5), this is 1 $\| \hbar \| ^ { 2 } -$   
$\sum _ { k = 1 } ^ { n } | L ( { x _ { k } } ^ { * } ) | ^ { 2 }$ giving us (9.4.24).

Assume now that $\| w \| \leq r$ .We shall exhibit an element in $C _ { r }$ for which the inequality (9.4.23) becomes an equality. Let $z = \sum _ { k = n + 1 } ^ { \infty } { \overline { { L ( { x _ { k } } ^ { * } ) } } } { x _ { k } } ^ { * }$ If $z = 0$ ， $L ( x _ { k } { } ^ { * } ) = 0$ ， $k = n + 1 ,$ ....In this case,the elemnt $x _ { 0 } = w$ isin $C _ { r }$ and equality in (9.4.23) holds trivially.

If $z \neq 0$ ，set

$$
x _ { 0 } = w + \lambda z
$$

where

$$
| \lambda | = ( r ^ { 2 } - \| w \| ^ { 2 } ) ^ { \frac { 1 } { 2 } } / \| z \| .
$$

Now $( x _ { 0 } , x _ { i } ^ { * } ) = ( w , x _ { i } ^ { * } ) = a _ { i } , \ i$ $i = 1$ ,2,...,n, and so $x _ { 0 } \in P$ Moreover, $\| x _ { 0 } \| ^ { 2 } = \| w \| ^ { 2 } + | \lambda | ^ { 2 } \| z \| ^ { 2 } = r ^ { 2 }$ so that $x _ { 0 } \in C _ { r }$ Furthermore,

$$
\begin{array} { l } { { \displaystyle | L ( x _ { 0 } - w ) | = | \lambda | | L ( z ) | = | \lambda | \sum _ { k = n + 1 } ^ { \infty } | L ( x _ { k } ^ { * } ) | ^ { 2 } = | \lambda | \| z \| ^ { 2 } } } \\ { { \displaystyle \quad = ( r ^ { 2 } - \| w \| ^ { 2 } ) ^ { \frac { 1 } { 2 } } \| z \| = ( r ^ { 2 } - \| w \| ^ { 2 } ) ^ { \frac { 1 } { 2 } } \biggr ( \sum _ { k = n + 1 } ^ { \infty } | L ( x _ { k } ^ { * } ) | ^ { 2 } \biggr ) ^ { \frac { 1 } { 2 } } . } } \end{array}
$$

Thus, equality holds in (9.4.23) for ${ \boldsymbol { x } } = { \boldsymbol { x } } _ { \mathbf { 0 } }$

It should be remarked that the element $_ z$ has the alternate representation

$$
z = h - \sum _ { k = 1 } ^ { n } ( h , { x _ { k } } ^ { * } ) { x _ { k } } ^ { * } = h - \sum _ { k = 1 } ^ { n } \overline { { L ( { x _ { k } } ^ { * } ) } } { x _ { k } } ^ { * } ;
$$

for it is readily verifed that the Fourier coeffcients (with respect to ${ x _ { k } } ^ { * }$ ） of $\boldsymbol { z }$ and of the middle member of (9.4.27) are identical.

The hypercircle inequality may be used to obtain bounds for $L ( x )$ having been given certain information about $_ x$ This is illustrated by the following example.

Ex.4.Estimate $\int _ { - \frac { 1 } { 2 } } ^ { \frac { 1 } { 2 } } x ( t ) \ d t$ on the basis of the following information:

$$
x ( t ) \in L ^ { 2 } [ - 1 , 1 ] , \qquad \left\| x ( t ) \right\| \leq r ,
$$

and

$$
\int _ { - 1 } ^ { 1 } x ( t ) d t = 1 , \qquad \int _ { - 1 } ^ { 1 } t ^ { 2 } x ( t ) d t = 1 .
$$

The relevant hyperplane is $( x ( t ) , x _ { i } ( t ) ) \ : = 1 , i \ : = 1 , 2 .$ where $x _ { 1 } ( t ) = 1$ and $x _ { 2 } ( t ) = t ^ { 2 }$ .Orthonormalizing we obtain

$$
\begin{array} { r } { x _ { 1 } { } ^ { * } ( t ) \ : = \frac { 1 } { 2 } \sqrt { 2 } , \qquad x _ { 2 } { } ^ { * } ( t ) \ : = \ : - \frac { 1 } { 4 } \sqrt { 1 0 } \ : + \ : \frac { 3 } { 4 } \sqrt { 1 0 } \ : t ^ { 2 } . } \end{array}
$$

The hyperplane equations can be written as

$$
( x ( t ) , x _ { 1 } { } ^ { * } ( t ) ) \ : = \ : { \frac { 1 } { 2 } } \sqrt { 2 } \ : = a _ { 1 } , \qquad ( x ( t ) , x _ { 2 } { } ^ { * } ( t ) ) \ : = \ : { \frac { 1 } { 2 } } \sqrt { 1 0 } \ : = a _ { 2 } .
$$

Therefore,

$$
\begin{array} { r } { w = w ( t ) = ( \frac { 1 } { 2 } \sqrt { 2 } ) ( \frac { 1 } { 2 } \sqrt { 2 } ) + \frac { 1 } { 2 } \sqrt { 1 0 } ( - \frac { 1 } { 4 } \sqrt { 1 0 } + \frac { 3 } { 4 } \sqrt { 1 0 } t ^ { 2 } ) = \frac { 3 } { 4 } ( 5 t ^ { 2 } - 1 ) , } \end{array}
$$

and

$$
\| w \| ^ { 2 } = { a _ { 1 } } ^ { 2 } + { a _ { 2 } } ^ { 2 } = 3 .
$$

Now,

$$
\begin{array} { r l } { L ( x _ { 1 } ^ { * } ) } & { = \displaystyle { \int _ { - \frac { 1 } { 2 } } ^ { \frac { 1 } { 2 } } } \sqrt { \frac { 1 } { 2 } } d t = \frac { 1 } { 2 } \sqrt { \frac { 1 } { 2 } } \mathrm { , } } \\ { L ( x _ { 2 } ^ { * } ) } & { = \displaystyle { \int _ { - \frac { 1 } { 2 } } ^ { \frac { 1 } { 2 } } } ( - \frac { 1 } { 4 } \sqrt { 1 0 } + \frac { 3 } { 4 } \sqrt { 1 0 } t ^ { 2 } ) d t = - \frac { 3 } { 1 6 } \sqrt { \overline { { 1 0 } } } \mathrm { , } } \\ { L ( w ) } & { = \displaystyle { \int _ { - \frac { 1 } { 2 } } ^ { \frac { 1 } { 4 } } } ( 5 t ^ { 2 } - 1 ) d t = - \frac { 7 } { 1 6 } . } \end{array}
$$

and

By inspection, $\pmb { h } = \pmb { h } ( t ) = \pmb { 1 }$ for $- \frac { 1 } { 2 } \leq t \leq \frac { 1 } { 2 }$ and $\mathbf { \boldsymbol { h } } ( t ) = \mathbf { \boldsymbol { 0 } }$ elsewhere.Hence, $\| h ( t ) \| = 1$ .Inequality(9.4.24) becomes

$$
\displaystyle \left( \int _ { - \frac { 1 } { 2 } } ^ { \frac { 1 } { 2 } } x ( t ) d t + \frac { 7 } { 1 6 } \right) ^ { 2 } \leq ( r ^ { 2 } - 3 ) ( 1 - \frac { 1 } { 2 } - \frac { 9 0 } { 2 5 6 } ) = \frac { 1 9 } { 1 2 8 } ( r ^ { 2 } - 3 ) .
$$

We may express this as

$$
- { \textstyle \frac { 7 } { 1 6 } } - \varepsilon \leq \int _ { - { \frac { 1 } { 2 } } } ^ { \frac { 1 } { 2 } } x ( t ) d t \leq - { \textstyle \frac { 7 } { 1 6 } } + \varepsilon
$$

with $\varepsilon = { \sqrt { \frac { 1 9 } { 1 2 8 } } } ~ { \sqrt { r ^ { 2 } - 3 } } .$ Inequality(9.4.30)holdsforallfunctions ${ \boldsymbol x } ( t )$ satisfying the hypercircle conditions (9.4.28)(a),(b).Moreover，since one equality in (9.4.30)occurs for some element in the hypercircle, the midpoint of the range, $- \frac { 7 } { 1 8 }$ , can be taken as a “best”value o $\cdot \int _ { - \frac { 1 } { 2 } } ^ { \frac { 1 } { 2 } } x ( t ) \ d t$ relative to the information available.

# NOTES ON CHAPTER IX

See the references on normed linear spaces and Hilbert spaces listed under Chapters VII and VIII.

9.2For interchange of summation and integration and Fatou's lemma used in the proof of Theorem 9.2.2,see,e.g.，Rudin [l],pp.209-217.The Hilbert space $L ^ { 2 } ( B )$ can be found in Bergman [2], Chapter I,Behnke and Sommer [l],pp.256-282,Nehari [1],pp.239-260.Related Hilbert spaces formed by using line integrals as inner products are described in Walsh [2], Chapter 6.Bergman and Schiffer [l] discuss Hilbert spaces of solutions of elliptic partial differential equations.

9.4For interpolation problems in $L ^ { 2 } ( B )$ see Bergman [2],pp. 47-49, Walsh and Davis [1]. The hypercircle inequality (Th. 9.4.7) is given in Synge[l],Chapter 2,and in Golomb and Weinberger [l],p. l33,where many applications to numerical analysis will be found.

# PROBLEMS

1. Let $w _ { i } > 0$ and let $\ell _ { w } ^ { \mathrm { ~ 2 ~ } }$ designate the set of all sequences $\{ a _ { i } \}$ such that $\sum _ { i = 1 } ^ { \infty } w _ { i } \vert a _ { i } \vert ^ { 2 } < \infty$ .Set $( a , b ) = \sum _ { i = 1 } ^ { \infty } w _ { i } a _ { i } \bar { b } _ { i }$ .Then $\ell _ { w } ^ { \mathrm { ~ \ 2 ~ } }$ is a Hilbert space.

2. Prove that all sequences of the form $( a _ { 1 } , 0 , a _ { 2 } , 0 , a _ { 3 } , 0 , . ~ . ~ . )$ with

$$
\sum _ { i = 1 } ^ { \infty } | a _ { i } | ^ { 2 } < \infty
$$

constitute a sub-Hilbert space of ${ \pmb \ell } ^ { 2 }$ . Generalize.

3. Let $M$ be a linear subspace of a Hilbert space $\pmb { H }$ .Show by an example that there may be a sequence ${ x _ { 1 } } ^ { * } , { x _ { 2 } } ^ { * } , \ldots ,$ ,of orthonormal elements that arecomplete for $M$ but not for $\pmb { H }$ ·

4. If $\boldsymbol { \mathfrak { c } }$ is the unit circle,there are functions that are analytic in $c$ but are not in 5.If $L ^ { 2 } ( C )$ $\pmb { f }$ is in $L ^ { 2 } ( B )$ ,is $f ^ { \prime }$ inL $^ { 2 } ( B ) \Im \mathrm { I s } \int ^ { z } f ( z ) d z \mathrm { i n } L ^ { 2 } ( B ) \Im \mathrm { I s }$

6.Let $\pmb { B }$ be a finite region and $z _ { 1 } , z _ { 2 } , \ldots , z _ { n }$ be $_ n$ fixed points in $\pmb { B }$ .Let $\pmb { H }$ designate the set of all functions $f ( z )$ in $L ^ { 2 } ( B )$ for which $f ( z _ { k } ) = 0 , k = 1 , 2 , . . . , n$ Show that $\pmb { H }$ is a sub-Hilbert space of $L ^ { 2 } ( B )$ . Generalize.

7. If $\boldsymbol { \mathfrak { c } }$ is the unit circle, find $\operatorname* { m i n } _ { f \in L ^ { 2 } ( C ) } \iint _ { C } \lvert 1 - z f ( z ) \rvert ^ { 2 } d x d y .$

8.If $X = C [ a , b ]$ with $\left\| f \right\| = \operatorname* { m a x } _ { a \leq x \leq b } \left| f ( x ) \right|$ ，are either $F ( f ) = \int _ { a } ^ { b } f ^ { 2 } ( x ) d x$ or $F ( f ) = f ^ { 2 } ( x _ { 1 } ) - f ^ { 2 } ( x _ { 2 } ) , a \leq x _ { 1 } , x _ { 2 } \leq b$ continuous functionals?

$X = C [ 0 , 1 ]$ with $\| f \| = \int _ { 0 } ^ { 1 } { \bigl | } f ( x ) { \bigr | } d x$ Let $F ( f ) = \int _ { 0 } ^ { 1 } f ^ { 2 } ( x ) d x$ Show that $\pmb { F }$ is not a continuous functional.

10. In $L ^ { 2 } [ - 1 , 1 ]$ set $L _ { h } ( f ) = { \frac { 1 } { 2 h } } \int _ { - h } ^ { h } f ( x ) d x , 0 < h \leq 1$ . Compute $\| L _ { h } \|$ and study $\operatorname* { l i m } _ { h \to 0 } \| L _ { h } \|$

$x$ is a real normed linear space.If $L$ is an additive and continuous functional,it must be homogeneous and hence is a bounded linear functional.

12.Let $x$ be a finite dimensional normed linear space.Then any linear functional $\scriptstyle { \cal L }$ is bounded on $x$

13.A linear transformation of one Hilbert space into another is a mapping $\pmb { T }$ for which $T ( a _ { 1 } x _ { 1 } + a _ { 2 } x _ { 2 } ) = a _ { 1 } T ( x _ { 1 } ) + a _ { 2 } T ( x _ { 2 } )$ . A linear transformation $U$ is called isometric if $\| U ( x ) \| = \| x \|$ for all ${ \pmb x } \in { \pmb H }$ Prove that if $\boldsymbol { \tau }$ is isometric, $( U x , U y ) = ( x , y )$ and hence an isometry sends orthogonal systems into orthogonal systems.

14. If $\boldsymbol { \tau }$ is an isometry that maps $\pmb { H }$ onto (the whole of) itself, then $\{ U ( x _ { n } ) \}$ is complete if and only if $\{ x _ { n } \}$ is complete.

15.Let $\{ x _ { i } ^ { * } \}$ and $\{ y _ { i } * \}$ be two complete orthonormal systems for a Hilbert space $\pmb { H }$ The trnsfsration $U \left( \sum _ { i = 1 } ^ { \infty } a _ { i } x _ { i } { } ^ { * } \right) \ = \sum _ { i = 1 } ^ { \infty } a _ { i } y _ { i } { } ^ { * }$ is isometrc.

16. Exhibit the isomorphism and isometry of $\scriptstyle { \pmb { R _ { n } } }$ and $\pmb { R _ { n } } ^ { * }$

17. If $x$ is an inner product space of infinite dimension,a hyperplane in $x$ is also of infinite dimension.

18.Formulate an interpolation problem in Hilbert space that has infinitely many conditions and has infinitely many independent solutions.

19.Discuss the interpolation problem $( y , x _ { 1 } ) = 1 , ( y , x _ { k } ) = 0 , k = 2 , 3 , \ldots ,$ in a Hilbert space.

20.Formulate Theorem 9.4.2 as a theorem about a system of infinitely many linear equations in infinitely many unknowns.

21.In $\ell ^ { 2 }$ ，what are necessary and sufficient conditions that the elements $x _ { 1 } = ( a _ { 1 1 } , 0 , 0 , . . . ) , x _ { 2 } = ( a _ { 2 1 } , a _ { 2 2 } , 0 , 0 , . . . ) , x _ { 3 } = ( a _ { 3 1 } , a _ { 3 2 } , a _ { 3 3 } , 0 , 0 , . . . )$ be independent?Be complete? Orthogonalize them.

22.Discuss the solution of the system

$$
\begin{array} { r l r } & { } & { \quad x _ { 1 } } \\ & { } & { \quad - x _ { 1 } + x _ { 2 } \quad \quad = a _ { 2 } } \\ & { } & { \quad - x _ { 2 } + x _ { 3 } = a _ { 3 } } \\ & { } & { \quad \quad \cdot \quad } \\ & { } & { \quad \cdot \quad } \\ & { } & { \quad \cdot \quad } \end{array}
$$

from the point of view of Theorem 9.4.2.

# CHAPTERX

# Orthogonal Polynomials

10.1 General Properties of Real Orthogonal Polynomials. Let $[ a , b ]$ be a finite or infinite interval and let $w ( x )$ be a positive weight function defined there. We assume that the integrals $\int _ { a } ^ { b } w ( x ) x ^ { n } d x , \ n = 0 , 1 , . . . \ . \ ,$ all exist.Employ an inner product

$$
( f , g ) { \overset { \cdot } { = } } ( g , f ) = \int _ { a } ^ { b } w ( x ) f ( x ) g ( x ) d x
$$

and orthonormalize (by means of Theorem 8.3.3) the sequence of powers $1 , x , x ^ { 2 } ;$ ，...,with respect to this inner product.Designate the polynomials obtained by

$$
{ p _ { n } } ^ { * } ( x ) = k _ { n } x ^ { n } + \cdot \cdot \cdot , k _ { n } > 0 .
$$

Polynomials that are merely orthogonal without being necessarily normal will be designated by ${ \pmb { p } } _ { n }$ throughout this chapter.

Observe that if $\pmb { p } \in \mathscr { P } _ { n - 1 }$ then

$$
( { \pmb { p } } , { \pmb { p } } _ { n } ) = 0 .
$$

This follows from Corollary 8.3.5 and the definition of orthogonality.

Though determinant expressions for orthogonal polynomials can be obtained from Corollary 8.7.6,they appear to be of limited importance. The following theorem, however, is of great utility.

THEOREM l0.l.1. Real orthonormal polynomials satisfy $^ { a }$ three term recurrence relationship.

$$
{ p _ { n } } ^ { * } ( x ) = ( a _ { n } x + b _ { n } ) p _ { n - 1 } ^ { * } ( x ) - c _ { n } p _ { n - 2 } ^ { * } ( x ) \quad n = 2 , 3 , . . . .
$$

The following form is particularly convenient for niachine computation

$$
\left. \begin{array} { l } { { p _ { - 1 } = 0 } } \\ { { p _ { 0 } = 1 } } \\ { { . } } \\ { { . } } \\ { { . } } \\ { { p _ { n + 1 } ( x ) = x p _ { n } { } ^ { * } ( x ) - ( x p _ { n } { } ^ { * } , p _ { n } { } ^ { * } ) { p _ { n } } ^ { * } ( x ) - ( p _ { n } , p _ { n } ) { } ^ { 1 } p _ { n - 1 } ^ { * } ( x ) } } \\ { { \quad } } \\ { { p _ { n } { } ^ { * } ( x ) = p _ { n } ( x ) / ( p _ { n } , p _ { n } ) ^ { \frac { 1 } { 2 } } . } } \\ { { \quad } } \end{array} \right\}
$$

Proof:It is clear that ${ p _ { n } } ^ { * } ( x )$ (defined by (lo.1.5)) is a polynomial of degree $\pmb { n }$ and is normal.We shall prove by induction that they are orthogonal. Assume that we have proved $( { p _ { m } } ^ { * } , { p _ { j } } ^ { * } ) = 0$ for $j = 0 , 1 , \ldots , m - 1$ and for $m = 0 , 1 , \ldots , n$ .We wish to show that $( { p _ { n + 1 } ^ { * } } , { p _ { j } } ^ { * } ) = 0$ for $j = 0$ ， $1 , \ldots , n$ Now,

$$
\begin{array} { r } { ( p _ { n + 1 } , p _ { j } { * } ) = ( x p _ { n } { * } - ( x p _ { n } { * } , p _ { n } { * } ) p _ { n } { * } - ( p _ { n } , p _ { n } ) ^ { \frac { 1 } { 2 } } p _ { n - 1 } ^ { * } , p _ { j } { * } ) \qquad } \\ { = ( x p _ { n } { * } , p _ { j } { * } ) - ( x p _ { n } { * } , p _ { n } { * } ) ( p _ { n } { * } , p _ { j } { * } ) - ( p _ { n } , p _ { n } ) ^ { \frac { 1 } { 2 } } ( p _ { n - 1 } ^ { * } , p _ { j } { * } ) . } \end{array}
$$

Also $( { x p _ { n } } ^ { * } , { p _ { j } } ^ { * } ) = ( { p _ { n } } ^ { * } , { x p _ { j } } ^ { * } )$ as can be seen by referring to (l0.1.1). For $j = 0 , 1 , 2 , \ldots , n - 2$ we have by our induction hypothesis

$$
( { p _ { n } } ^ { * } , { p _ { j } } ^ { * } ) = 0 , ( { p _ { n - 1 } ^ { * } } , { p _ { j } } ^ { * } ) = 0 , ( { p _ { n } } ^ { * } , x { p _ { j } } ^ { * } ) = 0
$$

since ${ x p } _ { j } ^ { * }$ is a polynoniial of degree $\leq n - 1$ Hence $( p _ { n + 1 } , p _ { j } ^ { * } ) = 0$ for $j = 0 , 1 , 2 , \ldots , n - 2$ .For $j = n - 1$ we have

$$
( p _ { n + 1 } , p _ { n - 1 } ^ { * } ) = ( { x p _ { n } } ^ { * } , p _ { n - 1 } ^ { * } ) - 0 - ( p _ { n } , p _ { n } ) ^ { \frac { 1 } { 2 } } \cdot 1 .
$$

Now, $( x p _ { n } , p _ { n - 1 } ^ { * } ) = ( p _ { n } , x p _ { n - 1 } ^ { * } )$ . By the recurrence,

$$
x p _ { n - 1 } ^ { * } = p _ { n } + \alpha { p _ { n - 1 } ^ { * } } + \beta p _ { n - 2 } ^ { * } .
$$

Hence, $( p _ { n } , x p _ { n - 1 } ^ { * } ) = ( p _ { n } , p _ { n } + \alpha p _ { n - 1 } ^ { * } + \beta p _ { n - 2 } ^ { * } ) = ( p _ { n } , p _ { n } )$ by our induction hypothesis.Hence $( x p _ { n } { } ^ { * } , p _ { n - 1 } ^ { * } ) = ( p _ { n } , p _ { n } ) ^ { \frac { 1 } { 2 } }$ and therefore $( p _ { n + 1 } , p _ { n - 1 } ^ { * } ) = 0$ Finally, $( p _ { n \div 1 } , p _ { n } { } ^ { * } ) = ( x p _ { n } { } ^ { * } , p _ { n } { } ^ { * } ) - ( x p _ { n } { } ^ { * } , p _ { n } { } ^ { * } ) - 0 = 0$ In this way, the induction is carried to $n + 1$ .Equation (10.1.4) follows from (10.1.5).

Further identification of the coefficients of the recursion is often useful.

THEOREM 10.1.2． Let ${ p _ { n } } ^ { * } ( x ) = k _ { n } x ^ { n } + s _ { n } x ^ { n - 1 } + \cdot \cdot \cdot b \epsilon$ orthonormal polynomials.Then the coefficients in the recurrence

$$
{ p _ { n } } ^ { * } = ( a _ { n } x + b _ { n } ) p _ { n - 1 } ^ { * } - c _ { n } p _ { n - 2 } ^ { * }
$$

are given by

$$
\left. \begin{array} { l } { { a _ { n } = \displaystyle \frac { k _ { n } } { k _ { n - 1 } } \ , b _ { n } = a _ { n } \biggl ( \frac { s _ { n } } { k _ { n } } - \frac { s _ { n - 1 } } { k _ { n - 1 } } \biggr ) } } \\ { { c _ { n } = a _ { n } \displaystyle \frac { k _ { n - 2 } } { k _ { n - 1 } } = \frac { k _ { n } k _ { n - 2 } } { k _ { n - 1 } ^ { 2 } } \ . } } \end{array} \right. \quad n = 2 , 3 , . . . . \ .
$$

Proof: The first two identities are obtained by inserting $k _ { n } x ^ { n } + \mathfrak { s } _ { n } x ^ { n - 1 } + \cdots$ into (10.1.4) and comparing the coefficients of $x ^ { n }$ and $x ^ { n - 1 }$ .The third identity can be proved in this way:

$$
\begin{array} { c } { { 0 = ( p _ { n } { } ^ { * } , p _ { n - 2 } ^ { * } ) = ( a _ { n } x p _ { n - 1 } ^ { * } + b _ { n } p _ { n - 1 } ^ { * } - c _ { n } p _ { n - 2 } ^ { * } , p _ { n - 2 } ^ { * } ) } } \\ { { { } } } \\ { { = a _ { n } ( x p _ { n - 1 } ^ { * } , p _ { n - 2 } ^ { * } ) - c _ { n } . } } \end{array}
$$

But

$$
\begin{array} { l } { \displaystyle ( x p _ { n - 1 } ^ { * } , p _ { n - 2 } ^ { * } ) = ( p _ { n - 1 } ^ { * } , x p _ { n - 2 } ^ { * } ) = ( p _ { n - 1 } ^ { * } , k _ { n - 2 } x ^ { n - 1 } ) } \\ { \displaystyle = \frac { k _ { n - 2 } } { k _ { n - 1 } } ( p _ { n - 1 } ^ { * } , k _ { n - 1 } x ^ { n - 1 } ) = \frac { k _ { n - 2 } } { k _ { n - 1 } } ( p _ { n - 1 } ^ { * } , p _ { n - 1 } ^ { * } ) = \frac { k _ { n - 2 } } { k _ { n - 1 } } . } \end{array}
$$

The formula for $\pmb { c _ { n } }$ is now apparent.

THEOREM lO.1.3. The zeros of real orthogonal polynomials are real, simple, and are located in the interior of $[ a , b ]$

Proof: Let $n \ ( \geq 1 )$ be fixed. If ${ \pmb p } _ { n } ( x )$ were of constant sign ill $[ \pmb { a } , \pmb { b } ]$ say positive,then $\int _ { a } ^ { b } w ( x ) p _ { n } ( x ) d x = ( p _ { n } , p _ { 0 } ) > 0$ .But this contradicts orthogonality. Hence $\pmb { p _ { n } } ( \pmb { x _ { 1 } } ) = 0$ for some ${ \pmb x } _ { 1 } \in ( a , b )$ .Suppose that there is a zero at $\pmb { x _ { 1 } }$ which is multiple. Then $\frac { p _ { n } ( x ) } { ( x - x _ { 1 } ) ^ { 2 } }$ would be a polynomial of degree $\mathbf { \mathscr { n } } - \mathbf { \mathscr { 2 } }$ Hence $0 = { \Big ( } p _ { n } ( x ) , { \frac { p _ { n } ( x ) } { ( x - x _ { 1 } ) ^ { 2 } } } { \Big ) } = { \Big ( } 1 , { \Big ( } { \frac { p _ { n } ( x ) } { ( x - x _ { 1 } ) } } { \Big ) } ^ { 2 } { \Big ) } > 0$ and this is impossible. Therefore every zero is simple. Suppose now that ${ \pmb p } _ { \pmb n } ( { \pmb x } )$ has $j$ zeros $x _ { 1 } , x _ { 2 } , \ldots , x _ { j }$ and no others lying in $( a , b )$ . Then,

Pn $( x ) ( x - x _ { 1 } ) ( x - x _ { 2 } ) \cdot \cdot \cdot ( x - x _ { j } ) = P _ { n - j } ( x ) ( x - x _ { 1 } ) ^ { 2 } ( x - x _ { 2 } ) ^ { 2 } \cdot \cdot \cdot ( x - x _ { j } ) ^ { 2 }$ where $P _ { n - j }$ isa polynomial of degree $\pmb { n } - j$ that does not change sign in $( a , b )$ . Hence, $( p _ { n } ( x ) , ( x - x _ { 1 } ) \cdot \cdot \cdot ( x - x _ { j } ) ) = ( P _ { n - j } , ( x - x _ { 1 } ) ^ { 2 } \cdot \cdot \cdot ( x - x _ { j } ) ^ { 2 } )$ The right-hand side cannot vanish.But the left vanishes if $j < n$ ，so that $j \geq n$ .But $j > n$ is impossible,and therefore $j = n$

THEOREM 10.1.4．Let $f ( x ) \in C [ a , b ]$ ; then the Fourier segment

$$
\sum _ { k = 0 } ^ { n } ( f , { p _ { k } } ^ { * } ) { p _ { k } } ^ { * } ( x )
$$

must coincide with $f ( x )$ in at least $\pm 1$ points of $( a , b )$

Proof: Let $R _ { n } ( x ) = f ( x ) - \sum _ { k = 0 } ^ { n } ( f , { p _ { k } } ^ { * } ) { p _ { k } } ^ { * } ( x )$ .Then from Theorem 8.6.1 we know that $( \boldsymbol R _ { n } ( x ) , \boldsymbol p _ { k } { } ^ { * } ( x ) ) = 0 , k = 0 , 1 , . . . , n .$ In particular,

$$
( R _ { n } ( x ) , p _ { 0 } { } ^ { * } ) = 0 = ( R _ { n } ( x ) , 1 ) .
$$

Hence $\boldsymbol { R } _ { n } ( \boldsymbol { x } )$ must vanish somewhere in $( a , b )$ .Suppose now that it changes sign at $a < x _ { 1 } < x _ { 2 } < \cdots < x _ { j } < b$ and at no other points of $( a , b )$ . Then, $\boldsymbol { R } _ { n } ( \boldsymbol { x } )$ is of constant and alternating sign in the segments

$$
( a , x _ { 1 } ) , ( x _ { 1 } , x _ { 2 } ) , \cdot \cdot \cdot , ( x _ { j } , b ) ,
$$

and this is true of the polynomial $( { \pmb x } - { \pmb x } _ { 1 } ) \cdot \cdot \cdot ( { \pmb x } - { \pmb x } _ { 3 } )$ .Thus, the product

$R _ { n } ( x ) ( x - x _ { 1 } ) \cdot \cdot \cdot ( x - x _ { j } )$ has constant sign in $( a , b )$ and

$$
( R _ { n } ( x ) ( x - x _ { 1 } ) \cdot \cdot \cdot ( x - x _ { j } ) , 1 ) = \cdot ( R _ { n } ( x ) , ( x - x _ { 1 } ) \cdot \cdot \cdot ( x - x _ { j } ) )
$$

cannot vanish.But by orthogonality it must vanish for $j \leq n$ . Hence $j > n$ and the theorem follows.

![](../chunks/Interpolation and Approximation (Philip J. Davis) (z-library.sk, 1lib.sk, z-lib.sk)_part_0004_pages_0211-0280/auto/images/5bbbc8926acfbdddfc5eb6f5849c290dbc73059e97344f72465cecd67f474cfa.jpg)  
Figure 10.1.1 Coincidence of a Function and its Fourier Approximants.

DEFINITION 10.1.1．Let ${ p _ { n } } ^ { * } ( x )$ ， $\pmb { n = 0 , 1 , \dots }$ ,be a system of real orthonormal polynomials.The symmetric function

$$
K _ { n } ( x , y ) = \sum _ { k = 0 } ^ { n } { p _ { k } } ^ { * } ( x ) { p _ { k } } ^ { * } ( y )
$$

is called the kernel polynomial of order $\pmb { n }$ of the orthonormal system.

The kernel polynomial has the following reproducing property.

THEOREM 10.1.5. For any polynomial $P \in \mathcal { P } _ { n }$

$$
( P ( x ) , K _ { n } ( x , y ) ) _ { x } = P ( y ) .
$$

Conversely, if $\pmb { K } ( \pmb { x } , \pmb { y } )$ is $^ { \pmb { a } }$ polynomial of degree n at most in $\pmb { x }$ and in y and if

$$
( P ( x ) , K ( x , y ) ) _ { x } = P ( y )
$$

holds for all $P ( \pmb { x } ) \in \mathcal { P } _ { n }$ then $K ( x , y ) = K _ { n } ( x , y )$

The subscript $\pmb { x }$ is placed outside the inner product to indicate the integration variable.

$$
\begin{array} { l } { { \displaystyle P r o o f \colon ~ P ( x ) = \sum _ { k = 0 } ^ { n } ( P , p _ { k } { } ^ { * } ) p _ { k } { } ^ { * } ( x ) ~ \mathrm { b y ~ T h e o r e m ~ 8 . 4 . 1 } \mathrm { . } \mathrm { ~ H e n c e } , } } \\ { { \displaystyle ( P ( x ) , K _ { n } ( x , y ) ) _ { x } = \left( \sum _ { k = 0 } ^ { n } ( P , p _ { k } { } ^ { * } ) p _ { k } { } ^ { * } ( x ) , \sum _ { k = 0 } ^ { n } p _ { k } { } ^ { * } ( x ) p _ { k } { } ^ { * } ( y ) \right) _ { x } } } \\ { { \displaystyle \quad \quad = \sum _ { m , k = 0 } ^ { n } ( P , p _ { k } { } ^ { * } ) p _ { m } { } ^ { * } ( y ) ( p _ { k } { } ^ { * } ( x ) , p _ { m } { } ^ { * } ( x ) ) = \sum _ { k = 0 } ^ { n } ( P , p _ { k } { } ^ { * } ) p _ { k } { } ^ { * } ( y ) = P ( y ) . } } \end{array}
$$

Suppose now, that $( P ( x ) , K ( x , y ) ) _ { x } = P ( y )$ for all $\boldsymbol { P } \in \mathcal { P } _ { n }$ Select $P ( { \pmb x } ) =$ ${ \pmb { K } } _ { n } ( { \pmb x } , { \pmb w } )$ .Then, $( K _ { n } ( x , w ) , \ K ( x , y ) ) _ { x } = K _ { n } ( y , w )$ .But,also,in view of (10.1.8), $( K _ { n } ( x , w ) , K ( x , y ) ) _ { x } = ( K ( x , y ) , K _ { n } ( x , w ) ) _ { x } = K ( w , y )$ . Hence,

$$
K _ { n } ( y , w ) = K _ { n } ( w , y ) = K ( w , y ) .
$$

An alternate expression may be given for the kernel polynomial.

THEOREM l0.1.6 (Christoffel-Darboux).Let ${ p _ { n } } ^ { * } ( x ) = k _ { n } x ^ { n } + \cdot \cdot \cdot , \ \prime$ $\pmb { n } =$ 0,1,...,be real orthonormal polynomials. Then,

$$
K _ { n } ( x , y ) = \sum _ { k = 0 } ^ { n } { p _ { k } } ^ { * } ( x ) p _ { k } { } ^ { * } ( y ) = { \frac { k _ { n } } { k _ { n + 1 } } } { \frac { p _ { n + 1 } ^ { * } ( x ) p _ { n } { } ^ { * } ( y ) - { p _ { n } } ^ { * } ( x ) p _ { n + 1 } ^ { * } ( y ) } { x - y } }
$$

Proof:Designate the right-hand member of (lo.1.10) by $K ( x , y )$ . Consider $\pmb { y }$ fixed.Then the numerator of $\pmb { K }$ is a polynomial of degree $\leq n + 1$ in $_ { \pmb { x } }$ Moreover it vanishes when ${ \boldsymbol { x } } = { \boldsymbol { y } }$ and hence is divisible by $x - y$ Thus, $K ( x , y )$ is a polynomial of degree ${ \leq n }$ in both $\pmb { x }$ and $_ y$ .We shall show that if $\pmb { p } ( \pmb { x } ) \in \mathcal { P } _ { \pmb { n } } ,$ ， $( p ( { \pmb x } ) , K ( { \pmb x } , { \pmb y } ) ) _ { \pmb { x } } = p ( { \pmb y } )$ and hence by the previous theorem we will have $K ( x , y ) = K _ { n } ( x , y )$ . Now,

$$
\begin{array} { l c l } { ( p ( x ) , K ( x , y ) ) _ { x } = \displaystyle \frac { k _ { n } } { k _ { n + 1 } } \Big ( [ p _ { n + 1 } ^ { * } ( x ) { p _ { n } } ^ { * } ( y ) - { p _ { n } } ^ { * } ( x ) { p _ { n + 1 } ^ { * } ( y ) } ] , \displaystyle \frac { p ( x ) - p ( y ) } { x - y } \Big ) _ { x } } \\ { + \displaystyle \frac { k _ { n } } { k _ { n + 1 } } p ( y ) \Big ( p _ { n } { } ^ { * } ( x ) , \displaystyle \frac { p _ { n + 1 } ^ { * } ( x ) - p _ { n + 1 } ^ { * } ( y ) } { x - y } \Big ) _ { x } } \\ { + \displaystyle \frac { k _ { n } } { k _ { n + 1 } } p ( y ) \Big ( p _ { n + 1 } ^ { * } ( x ) , \displaystyle \frac { p _ { n } { } ^ { * } ( y ) - p _ { n } { } ^ { * } ( x ) } { x - y } \Big ) _ { x } . } \end{array}
$$

Observe that $\frac { p ( x ) - p ( y ) } { x - y }$ and $\frac { p _ { n } * ( x ) - p _ { n } * ( y ) } { x - y }$ are polynomials of degree

$\leq n - 1$ in $_ x$ (or equal O if $\pmb { n = 0 }$ ).Hence by orthogonality,the first and third of the inner products on the right hand vanish. Then,

$$
( p ( x ) , K ( x , y ) ) _ { x } = \frac { k _ { n } } { k _ { n + 1 } } p ( y ) \bigg ( p _ { n } { } ^ { * } ( x ) , \frac { p _ { n + 1 } ^ { * } ( x ) - p _ { n + 1 } ^ { * } ( y ) } { x - y } \bigg ) _ { x } .
$$

But,

$$
{ \frac { k _ { n } } { k _ { n + 1 } } } { \frac { p _ { n + 1 } ^ { * } ( x ) - p _ { n + 1 } ^ { * } ( y ) } { x - y } } = k _ { n } { \biggr [ } { \frac { y ^ { n + 1 } - x ^ { n + 1 } } { x - y } } + \cdot \cdot \cdot { \biggr ] }
$$

Hence

$$
\frac { k _ { n } } { k _ { n + 1 } } \bigg ( p _ { n } { } ^ { * } ( x ) , \frac { p _ { n + 1 } ^ { * } ( y ) - p _ { n + 1 } ^ { * } ( x ) } { x - y } \bigg ) _ { x } = 1
$$

and the theorem follows.

COROLLARY 10.1.7.

$$
\sum _ { k = 0 } ^ { n } \{ p _ { n } { } ^ { * } ( x ) \} ^ { 2 } = \frac { k _ { n } } { k _ { n + 1 } } \left\{ p _ { n + 1 } ^ { * ^ { \prime } } ( x ) p _ { n } { } ^ { * } ( x ) - p _ { n } { } ^ { * } ( x ) p _ { n + 1 } ^ { * } ( x ) \right\}
$$

Proof: Allow $y  x$ in l0.1.1O and evaluate the right-hand limit by de l'Hospital's rule.

10.2 Complex Orthogonal Polynomials. Let $\boldsymbol { c }$ bea rectifiable curve or arc lying in the plane of the complex variable $z = x + i y$ .Consider the linear space of all polynomials with complex coefficients and for $_ z$ on $\boldsymbol { c }$ The complex powers $1 , z , z ^ { 2 } , \ldots$ ，are independent elements,for if we had $a _ { 0 } + a _ { 1 } z + a _ { 2 } z ^ { 2 } + \cdots + a _ { n } z ^ { n } \equiv 0$ on $c$ it would follow from the fundamental theorem of algebra that $\pmb { a _ { 0 } } = \pmb { a _ { 1 } } = \cdot \cdot \cdot = \pmb { a _ { n } } = 0$ . In this space,

$$
( f , g ) = \int _ { C } f ( z ) { \overline { { g ( z ) } } } d s
$$

$\left( \int _ { c } | f ( z ) | ^ { 2 } d \mathscr { s } = 0 \right.$ imples $f ( z ) \equiv 0 \Bigg )$ . Hece,.by

Theorem 8.3.3 we may orthogonalize the powers and arrive at a set of polynomials

$$
{ p _ { n } } ^ { * } ( z ) = k _ { n } z ^ { n } + \cdot \cdot \cdot \quad ; k _ { n } > 0 , n = 0 , 1 , \ldots ,
$$

that are orthonormal:

$$
\int _ { C } { p _ { n } } ^ { * } ( z ) { \overline { { { p _ { m } } ^ { * } ( z ) } } } d s = \delta _ { m n } .
$$

The ${ p _ { n } } ^ { * } ( z )$ are known as the complex orthonormal polynomials corresponding to $c$ .If $w ( z )$ is a positive function of the complex variable $\pmb { z }$ defined on $c$ ，

then, with appropriate integrability conditions,

$$
( f , g ) = \int _ { C } f ( z ) { \overline { { g ( z ) } } } w ( z ) \ d s
$$

also constitutes an inner product and gives rise to a set of orthonormal polynomials. The polynomials arising from (l0.2.3) or (l0.2.4) are associated with the name of G. Szego who first studied their properties extensively.

Complex orthogonal polynomials may also be constructed with double integrals.Let $\pmb { B }$ designate a bounded region (open connected set） lying in the complex plane.If we introduce the inner product

or

$$
( f , g ) = \int _ { \ B } \int _ { B } f ( z ) { \overline { { g ( z ) } } } d x d y
$$

$$
( f , g ) = \int _ { B } \int _ { } f ( z ) { \overline { { g ( z ) } } } w ( z ) d x d y
$$

for a suitable positive weight function $w ( z )$ ,then sets of orthonormal polynomials can be generated.These orthogonal polynomials are associated with the names of T.Carleman and S.Bergman. (Cf.9.2,III.)

Ex.1．The powers ${ \frac { 1 } { \sqrt { 2 \pi r ^ { 2 n + 1 } } } } \ z ^ { n } , \ n = 0 , 1 , 2 , \ldots ,$ ，are orthonormal on $| z | = r$ For   
$\int _ { | z | = r } { \frac { 1 } { \sqrt { 2 \pi r ^ { 2 n + 1 } } } } z ^ { n } { \frac { 1 } { \sqrt { 2 \pi r ^ { 2 n + 1 } } } } { \frac { \overline { { z ^ { m } } } } { z ^ { m } } } d s = { \frac { 1 } { 2 \pi r ^ { ( m + n + 1 ) } } } \int _ { | z | = r } z ^ { n } { \overline { { z ^ { m } } } } d s = { \frac { 1 } { 2 \pi } } \int _ { 0 } ^ { 2 \pi } e ^ { i ( m - n ) \theta } d s = | z | = | z | = | z | = | | z | = | | z | = | | { \frac { \overline { { z ^ { n } } } } { \sqrt { 2 \pi r ^ { 2 n + 1 } } } } | | \alpha | | | \quad \mathrm { a n d } | | | \quad \mathrm { a n d } | | | \quad \mathrm { a n d } | | | \quad \mathrm { a n d } | | | \quad \mathrm { a n d } | | | \quad \mathrm { a n d } | | | \quad \mathrm { a n d } | | | \quad \mathrm { a n d } | | | \quad \mathrm { a n d } | | | \quad \mathrm { a n d } | | | \quad \mathrm { a n d } | | | \quad \mathrm { a n d } | | | \quad \mathrm { a n d } | | | \quad \mathrm { a n d } | | | \quad \mathrm { a n d } | | | \quad \mathrm { a n d } | | | \quad \mathrm { a n d } | | | \quad \mathrm { a n d } | | | \quad \mathrm { a n d } | | | \quad \mathrm { a n d } | | | \quad \mathrm { a n d } | | | \quad \mathrm { a n d } | | | \quad \mathrm { a n d } | | | \quad \mathrm { a n d } | | | \quad \mathrm { a n d } | | | \quad \mathrm { a n d } | | | \quad \mathrm { a n d } | | | \quad \mathrm { a n d } | | | \quad \mathrm { a n d } | | | \quad | z | = | | \mathrm { a n d } | | | \quad | \mathrm { a n d } | | | \quad | \mathrm { a n d } | | | \quad | \mathrm { a n d } | | | \quad | \mathrm { a n d } | | | \quad | \mathrm { a n d } | | | | \quad | \mathrm { a n d } | | | | \quad | \mathrm { a n d } | | | | \quad | \mathrm { a n d } | | | | | \quad | \mathrm { a n d } | | | | | \quad | \quad | \mathrm { a n d } | | | | | | \quad | \quad | \quad | \quad | \mathrm  a n d | | | | | | | | \mathrm | | \quad | | \quad | | \quad | | \quad | \quad | | \quad | | | $ 10 ${ \bf \mu } = { \bf 0 }$ if $m \neq n$ and $\mathbf { 1 }$ if $\textbf { \textit { m } } = \pmb { \mathscr { n } }$

Ex. 2. The powers $\sqrt { \frac { n + 1 } { \pi } } \frac { z ^ { n } } { r ^ { n + 1 } } , n = 0 , 1 , 2 , . . . ,$ rn+1'n =0,1,2,..,are orthonormal over the region $| z | < r$

Ex.3．The Tschebyscheff polynomials of the first kind, $\pmb { T } _ { \pmb { n } } ( \pmb { w } )$ ,are orthogonal on every ellipse $\mathcal { E } _ { \rho }$ (see l.13) with respect to the weight function $| 1 - w ^ { 2 } | ^ { - \frac { 1 } { 2 } }$ That is,

$$
I _ { m , n } = \int _ { \pmb { \mathscr { E } } _ { \rho } } \frac { T _ { m } ( w ) \overline { { T _ { n } ( w ) } } } { \lvert 1 - w ^ { 2 } \rvert ^ { \frac { 1 } { 2 } } } \left. d w \right. = 0 , \mathscr { m } \neq n ; \quad \lvert d w \rvert = d s _ { w }
$$

$\Longapprox$ element of arc in the $\pmb { w }$ -plane.

Proof: Let

then by (4.4.2)

$$
\begin{array} { r } { w = \frac { 1 } { 2 } ( z + z ^ { - 1 } ) , ~ z = \rho e ^ { i \theta } ; } \\ { ~ } \\ { T _ { n } ( w ) = \frac { 1 } { 2 } ( \rho ^ { n } e ^ { i n \theta } + \rho ^ { - n } e ^ { - i n \theta } ) . } \end{array}
$$

Now

$$
d w / d z = { \textstyle \frac { 1 } { 2 } } ( 1 - z ^ { - 2 } ) \quad \mathrm { s o ~ t h a t } \quad | d w | = \frac { | z ^ { 2 } - 1 | } { | z ^ { 2 } | } \left| d z \right|
$$

and

$$
| 1 - w ^ { 2 } | ^ { \frac { 1 } { 2 } } = \frac { 1 } { 2 } \frac { | z ^ { 2 } - 1 | } { | z | } .
$$

Hence, by transforming to the $\pmb { z }$ plane,

$$
\begin{array} { r } { I _ { m , n } = \cfrac { 1 } { 4 } \int _ { | z | = \rho } \frac { ( \rho ^ { m } e ^ { i m \theta } + \rho ^ { - m } e ^ { - i m \theta } ) ( \rho ^ { n } e ^ { - i n \theta } + \rho ^ { - n } e ^ { i n \theta } ) } { | z | } \left. | d z \right| } \\ { = \cfrac { 1 } { 4 } \int _ { 0 } ^ { 2 \pi } ( \rho ^ { m } e ^ { i m \theta } + \rho ^ { - m } e ^ { - i m \theta } ) ( \rho ^ { n } e ^ { - i n \theta } + \rho ^ { - n } e ^ { i n \theta } ) d \theta = 0 } \end{array}
$$

Ex.4. The Tschebyscheff Polynomials of the Second Kind

$$
\begin{array} { l l l l } { { } } & { { p _ { n } { } ^ { * } ( z ) = 2 \displaystyle \sqrt { \frac { n + 1 } { \pi } } \left( \rho ^ { 2 n + 2 } - \rho ^ { - 2 n - 2 } \right) ^ { - \frac { 1 } { 2 } } U _ { n } ( z ) , } } \\ { { } } & { { } } \\ { { U _ { n } ( z ) = ( 1 - z ^ { 2 } ) ^ { - \frac { 1 } { 2 } } \sin { [ ( n + 1 ) \operatorname { a r c } \cos z ] } , } } \end{array}
$$

are orthonormal over the ellipse $\pmb { \mathscr { E } _ { \pmb { \rho } } }$ with respect to the inner product

$$
( f , g ) = \int _ { \mathcal { E } _ { \rho } } \int _ { } f ( z ) { \overline { { g ( z ) } } } d x d y .
$$

Proof:Under the conformal map $z = \cos w , z = x + i y , w = u + i v ,$ the interior of the rectangle $\pmb { R }$ with vertices at $\sigma i , \sigma i + \pi , - \sigma i + \pi , - \sigma i$ is mapped onto the ellipse $\pmb { \mathcal { E } _ { p } } ^ { \prime }$ consisting of the interior of $\mathcal { E } _ { \pmb { \rho } }$ with the two segments $[ - a , - 1 ] , [ 1 , a ]$ deleted. Now, $U _ { n } ( z ) = ( 1 - z ^ { 2 } ) ^ { - \frac { 1 } { 2 } } \sin \overline { { { [ ( n + 1 ) w ] } } }$ and

$$
d x d y \ = { \left| \begin{array} { l l } { { \overline { { \partial x } } } } & { { \frac { \partial y } { \partial u } } } \\ { { \overline { { \partial x } } } } & { { \frac { \partial y } { \partial v } } } \end{array} \right| } { d u d v \ } = \left| { \frac { d z } { d w } } \right| ^ { 2 } d w d v = \left| 1 \ - z ^ { 2 } \right| d u d v .
$$

Hence,

$$
\begin{array} { c l } { { \displaystyle I _ { m , n } = \iint _ { m } U _ { m } ( z ) \overline { { { U _ { n } ( z ) } } } d x d y ~ { = } \iint U _ { m } ( z ) \overline { { { U _ { n } ( z ) } } } d x d y ~ } } \\ { { \displaystyle \qquad } } \\ { { \displaystyle { = \iint _ { R } \exp \left( m + 1 \right) w \frac { 1 } { \sin { \big ( n + 1 \big ) w } } d u d y . } } } \end{array}
$$

With $p = m + 1 , r = n + 1$ ,and since

sin $\begin{array} { r } { p ( u \mathrm { ~ + ~ } i v ) \mathrm { ~ = ~ } \sin \mathcal { p u } \cosh \mathcal { p v } \mathrm { ~ + ~ } i \cos \mathcal { p u } \sinh \mathcal { p v } , } \end{array}$

$$
\begin{array} { r l r } { \displaystyle { I _ { m , n } } } & { { } \displaystyle { = \int _ { - \sigma } ^ { \sigma } \cosh p v \cosh r v d v \int _ { 0 } ^ { \tau } \sin p u \sin r u d u } } & { \displaystyle { + \int _ { - \sigma } ^ { \sigma } \sinh p v \sinh r v d v } } \\ { \displaystyle { } } & { { } } & { { \times \int _ { 0 } ^ { \tau } \cos p u \cos r u d u + i \int _ { - \sigma } ^ { \sigma } \sinh p v \cosh r v d v \int _ { 0 } ^ { \tau } \cos p u \sin r u d u - i \int _ { - \sigma } ^ { \sigma } \sinh p v \cosh r v d u } } \\ { \displaystyle { } } & { { } } & { { i \int _ { - \sigma } ^ { \sigma } \cosh p v \sinh r v d v \int _ { 0 } ^ { \tau } \sin p u \cos r u d u } } \end{array}
$$

Now sinh pv cosh $_ { r v }$ and cosh pv sinh $_ { r v }$ are odd functions of $v$ Their integral over $[ - \sigma , \sigma ]$ therefore vanishes.Furthermore,

$$
\int _ { 0 } ^ { \pi } \sin p u \sin r u d u \ = \int _ { 0 } ^ { \pi } \cos p u \cos r u d u \ = \frac { 0 , \quad p \neq r } { \pi }
$$

Hence, ${ \cal I } _ { m , n } = 0$ for $m \neq n$ . Now

$$
I _ { p , p } = { \frac { \pi } { 2 } } \int _ { - \sigma } ^ { \sigma } \cosh ^ { 2 } p v + \sinh ^ { 2 } p v d v = { \frac { \pi } { 2 } } \int _ { - \sigma } ^ { \sigma } \cosh 2 p v d v = { \frac { \pi \sinh 2 p \sigma } { 2 p } } .
$$

But p = e°. Hence, Ip,p $I _ { p , p } = \frac { \pi } { 4 p } ( \rho ^ { 2 p } - \rho ^ { - 2 p } )$

Ex.5.Let $\boldsymbol { S }$ designate the square with sides $x = \pm 1 , y = \pm 1$ ，and write

$$
( f , g ) = \int _ { S } f ( z ) { \overline { { g ( z ) } } } d s .
$$

The following polynomials are orthonormal with respect to this inner product.

$$
{ \begin{array} { r l } & { s _ { 0 } ( z ) = { \mathrm { . 3 5 3 5 5 } } } \\ & { s _ { 1 } ( z ) = { \mathrm { . 3 0 6 1 9 z } } } \\ & { s _ { 2 } ( z ) = { \mathrm { . 2 5 8 7 7 z ^ { 2 } } } } \\ & { s _ { 3 } ( z ) = { \mathrm { . 2 1 3 4 8 z ^ { 3 } } } } \\ & { s _ { 4 } ( z ) = { \mathrm { . 1 8 6 9 7 z ^ { 4 } } } + { \mathrm { . 1 4 9 5 7 } } } \\ & { s _ { 5 } ( z ) = { \mathrm { . 1 5 8 1 1 z ^ { 5 } } } + { \mathrm { . 1 8 0 7 0 z } } } \\ & { s _ { 6 } ( z ) = { \mathrm { . 1 3 3 9 6 z ^ { 6 } } } + { \mathrm { . 2 0 0 4 9 z ^ { 2 } } } } \\ & { s _ { 7 } ( z ) = { \mathrm { . 1 1 3 7 2 z ^ { 2 } } } + { \mathrm { . 2 0 0 0 5 z ^ { 3 } } } } \\ & { s _ { 8 } ( z ) = { \mathrm { . 0 9 6 5 6 z ^ { 8 } } } + { \mathrm { . 2 0 6 2 7 z ^ { 4 } } } } \end{array} }
$$

Though in isolated cases there are recurrence formulas relating successive complex orthogonal polynomials, there does not appear to be a general theorem of this sort.The identity used in the real case to establish the recurrence: $( x p _ { n } { } ^ { * } , p _ { m } { } ^ { * } ) = ( p _ { n } { } ^ { * } , x p _ { m } { } ^ { * } )$ does not carry over to the complex case where the inner product is Hermitian.

Theorem 10.1.3 tells us the location of the zeros of real orthogonal polynomials.L.Fejer found a remarkably simple proof of a theorem that covers a wide variety of cases,both real and complex.

LEMMA 10.2.1 (Fejér's Principle)．Let $\boldsymbol { s }$ designate a closed bounded convex set lying in the complex plane. $z _ { 1 }$ is $^ { \pmb { a } }$ point exterior to $\pmb { S }$ Then we may find $^ { \pmb { a } }$ point $z ^ { \prime }$ such that

$$
| z - z ^ { \prime } | < | z - z _ { 1 } | \qquad f o r \ a l l \ z \in S .
$$

![](../chunks/Interpolation and Approximation (Philip J. Davis) (z-library.sk, 1lib.sk, z-lib.sk)_part_0004_pages_0211-0280/auto/images/5a9c99361672df4c163ff7c7c050e19a4e03be798e3df4a810416a06ad43326e.jpg)  
Figure 10.2.1.

Proof:We can find a line $\ell$ that separates $z _ { 1 }$ and $\pmb { S }$ i.e., $z _ { 1 }$ and $\pmb { S }$ lie on opposite sides of $\ell .$ This geometrically evident fact can be established easily by the methods of the theory of convex bodies,but we shall not do so here (Cf.Prob.23).Drop a perpendicular from $z _ { 1 }$ to $\ell$ and call its foot $z ^ { \prime }$ Then if $_ z$ is any point on the $^ { \mathfrak { s o } }$ side of $\ell , \mathrm { , }$ it is no trouble to show that $| z - z ^ { \prime } | < | z - z _ { 1 } |$ In particular,(10.2.9) follows.

DEFINITION 10.2.1．Let $\pmb { S }$ be a set of points lying in the complex plane and $\pmb { F }$ a family of functions of a complex variable defined on $\pmb { S }$ Foreach $f \in F$ let there be defined a real, nonnegative quantity designated by $\| f \|$ satisfying the following property:for distinct $f$ and $\pmb { g }$ ，the condition

and

$$
\begin{array} { r l } & { | f ( z ) | < | g ( z ) | \mathrm { ~ w h e n e v e r ~ } g ( z ) \ne 0 } \\ & { } \\ & { | f ( z ) | = | g ( z ) | \mathrm { ~ w h e n e v e r ~ } g ( z ) = 0 } \end{array}
$$

implies

$$
\| f \| < \| g \| .
$$

The quantity $\| f \|$ will be known as a Fejér or monotonic norm for $\pmb { F }$ (It should be distinguished from the norms in a normed linear space.)

Here are some examples of monotonic norms.In each case $\pmb { F }$ is the class of polynomials $z ^ { n } + a _ { 1 } z ^ { n - 1 } + \cdots + a _ { n }$ with ${ \pmb a } _ { i }$ complex.

Ex.6.Let $s$ be a closed bounded point set.If finite,it should contain at least $\pmb { n }$ points. $\| f \| = \operatorname* { m a x } _ { z \in S } \left| f ( z ) \right|$ ·

Ex.7. Let $\pmb { S }$ be a rectifiable curve or arc.

$$
\| f \| = \int _ { S } \left| f ( z ) \right| ^ { p } d s . \qquad p > 0 .
$$

Ex.8. Let $\pmb { S }$ be a closed bounded region.

$$
\| f \| = \int _ { S } \int _ { S } \{ { f ( z ) } { | { \begin{array} { l } { { p } } \end{array} } \ d x d y ,  } \qquad p > 0 .
$$

Ex.9.Let $\pmb { S }$ be a rectifable arc,

$$
\| f \| = \int _ { S } e ^ { | f ( z ) | ^ { p } } d s , \qquad p > 0 .
$$

In Ex.6,there must be at least one point in $\pmb { S }$ where $\left| f \right| < \left| g \right|$ ，for otherwise $\left| f \right| = \left| g \right| = 0$ throughout $\pmb { S }$ and this is impossible since $\pmb { S }$ has at least $\pmb { n }$ points. In the other examples, $\left| f \right| \leq \left| g \right|$ certainly implies $\| f \| \leq \| g \| ,$ . But since $\vert f \vert < \vert g \vert$ in at least one point,the monotonic character of the integrals tells us that the inequality may be strengthened to $\| f \| < \| g \| ,$ ·

THEOREM lO.2.2 (Fejér's Convex Hull Theorem). Let $\pmb { F }$ designate the family of polynomials $z ^ { n } + a _ { 1 } z ^ { n - 1 } + \cdots \ + a _ { n }$ with ${ \pmb a } _ { i }$ complex. Let $\bigstar \bigstar \bigstar \bigstar | \bigstar | | \bigstar o |$ a monotonic norm on $\pmb { F }$ relative to $^ { \pmb { a } }$ point set $\pmb { S }$ Let the problem

$$
\operatorname* { m i n } _ { a _ { i } } \| z ^ { n } + a _ { 1 } z ^ { n - 1 } + \cdots + a _ { n } \|
$$

be solved by $^ { \pmb { a } }$ polynomial $\pmb { p } ( z )$ . Then the zeros of $\pmb { p } ( z )$ all lie in the closure of the convex hull of $\pmb { S }$ (Def. 7.3.3).

Proof: Let $p ( z ) = ( z - z _ { 1 } ) \cdot \cdot \cdot ( z - z _ { n } )$ Assume that a typical root, $z _ { 1 } ,$ lies exterior to the closure of the convex hull of $\pmb { S }$ This closure is also convex. By Fejér's principle,we can find a $z ^ { \prime }$ such that

$$
| z - z ^ { \prime } | < | z - z _ { 1 } | \qquad { \mathrm { f o r ~ a l l ~ } } z \in S .
$$

Hence, if we set

$$
q ( z ) = ( z - z ^ { \prime } ) ( z - z _ { 2 } ) \cdot \cdot \cdot ( z - z _ { n } ) \quad ( \not \equiv p ( z ) ) ,
$$

we have for $_ z$ in $\pmb { S }$

and

$$
\begin{array} { r l } & { | q ( z ) | < | p ( z ) | \mathrm { ~ w h e n e v e r ~ } p ( z ) \ne 0 } \\ & { } \\ & { | q ( z ) | = | p ( z ) | \mathrm { ~ w h e n e v e r ~ } p ( z ) = 0 . } \end{array}
$$

Hence, $\| q \| < \| p \|$ ，so that $\pmb { p }$ could not possibly have been a minimal polynomial as asserted.Therefore $z _ { 1 }$ must be in the closure of the convex hull of $\pmb { S }$

CoROLLARy l0.2.3. The zeros of complex orthogonal polynomials lie in the closure of the convex hull of the point sets over which the integration is performed.If ihe point set lies on the real axis and is contained in $[ a , b ]$ the orthogonal polynomials have real coefficients and the zeros lie in $[ a , b ]$

Proof:Cor.8.5.7,Ex.7,8 of 10.2 with $\pmb { p = 2 }$ ,and Theorem 10.2.2.

In contradistinction to the real case,no assertion can be made about the simplicity of the roots；indeed, $z ^ { n }$ are orthogonal over circles $| z | = r$ ，but have an $\pmb { n }$ -fold zero at $z = 0$ ·

The kernel polynomials of a real or complex system of orthogonal polynomials solve an important extremal problem. (Cf. Theorem 9.4.3.)

THEOREM 10.2.3．Let $z _ { \mathbf { 0 } }$ be an arbitrary point in the complex plane and $p ( z )$ an arbitrary element of $\mathcal { P } _ { n }$ . The problem of finding

subject to

$$
\operatorname* { m a x } _ { \pmb { p } \in \pmb { \mathcal { P } } _ { n } } | \pmb { p } ( \pmb { z } _ { 0 } ) |
$$

$$
\| \pmb { p } \| = 1
$$

is solved by

$$
q ( z ) = { \frac { e ^ { i \theta } K _ { n } ( z , z _ { 0 } ) } { \sqrt { K _ { n } ( z _ { 0 } , z _ { 0 } ) } } }
$$

where ${ \cal K } _ { n } ( z , z _ { 0 } )$ is the kernel polynomial

$$
K _ { n } ( z , z _ { 0 } ) = \sum _ { k = 0 } ^ { n } p _ { k } { ^ { * } } ( z ) { \overline { { p _ { k } { ^ { * } } ( z _ { 0 } ) } } }
$$

and $\ : \Theta \leq \theta < 2 \pi \ :$ ,is arbitrary. The maximum valueof (10.2.15) $\mathfrak { s } \sqrt { K _ { n } ( z _ { 0 } , z _ { 0 } ) }$

Proof: Let $\{ { p _ { n } } ^ { * } \}$ be the orthonormal polynomials appropriate to the norm $\parallel \parallel$ . Then an arbitrary $\pmb { \mathscr { p } } \in \mathscr { P } _ { \pmb { \mathscr { n } } }$ can be written as $p ( z ) = \sum _ { k = 0 } ^ { n } a _ { k } { p _ { k } } ^ { * } ( z )$ with $\| \mathcal { p } \| ^ { 2 } = \sum _ { k = 0 } ^ { n } | a _ { k } | ^ { 2 }$ (Theorem 8.4.1).Hence

$$
| p ( z _ { 0 } ) | ^ { 2 } = { \bigg | } \sum _ { k = 0 } ^ { n } a _ { k } p _ { k } { } ^ { * } ( z _ { 0 } ) { \bigg | } ^ { 2 } \leq \sum _ { k = 0 } ^ { n } | a _ { k } | ^ { 2 } \sum _ { k = 0 } ^ { n } | p _ { k } { } ^ { * } ( z _ { 0 } ) | ^ { 2 } .
$$

Hence $| p ( z _ { 0 } ) | ^ { 2 } \leq \sum _ { k = 0 } ^ { n } | p _ { k } ^ { * } ( z _ { 0 } ) | ^ { 2 } = K _ { n } ( z _ { 0 } , z _ { 0 } )$ whenever $\| \pmb { p } \| = 1$ . On the other hand, $q ( z ) \in \mathcal { P } _ { n } ;$ and

$$
\begin{array} { l } { { \displaystyle \| q \| ^ { 2 } = \left( \frac { e ^ { i \theta } K _ { n } ( z , z _ { 0 } ) } { \sqrt { K _ { n } ( z _ { 0 } , z _ { 0 } ) } } , \frac { e ^ { i \theta } K _ { n } ( z , z _ { 0 } ) } { \sqrt { K _ { n } ( z _ { 0 } , z _ { 0 } ) } } \right) } } \\ { { \displaystyle \quad = \frac { 1 } { K _ { n } ( z _ { 0 } , z _ { 0 } ) } \sum _ { j , k = 0 } ^ { n } ( p _ { k } { ^ { * } } ( z ) \overline { { p _ { k } { ^ { * } } ( z _ { 0 } ) } } , p _ { j } { ^ { * } } ( z ) \overline { { p _ { j } { ^ { * } } ( z _ { 0 } ) } } ) } } \\ { { \displaystyle \quad = \frac { 1 } { K _ { n } ( z _ { 0 } , z _ { 0 } ) } \sum _ { k = 0 } ^ { n } p _ { k } { ^ { * } } ( z _ { 0 } ) \overline { { p _ { k } { ^ { * } } ( z _ { 0 } ) } } = 1 . } } \end{array}
$$

Furthernore,

$$
| q ( z _ { 0 } ) | = { \sqrt { K _ { n } ( z _ { 0 } , z _ { 0 } ) } } .
$$

Ex.10.Let $\mathcal { P } _ { n }$ be an inner product space of real or complex polynomials of degree $\leq n$ .If ${ z _ { 0 } }$ is an arbitrary point in the complex plane, then $L ( f ) = f ( z _ { 0 } )$ is a bounded linear functional over ${ \mathcal P } _ { \pmb { n } }$ and $\| L \| ^ { 2 } = K _ { n } ( z _ { 0 } , z _ { 0 } )$

10.3 The Special Function Theory of the Jacobi Polynomials. There is an extensive literature that contains many identities and interrelationships between the real orthogonal polynomials generated by simple weighting functions.We shall content ourselves with presenting the most important identities for the class of polynomials known as the Jacobi polynomials.

For simplicity，the fundamental interval is selected as $[ - 1 , + 1 ]$ .The relevant weight function is

$$
w ( x ) = ( 1 - x ) ^ { \alpha } ( 1 + x ) ^ { \beta } , \alpha > - 1 , \beta > - 1 .
$$

If the exponents are between $- 1$ and O, then the weight has a singularity at the corresponding end point, but possesses a finite integral. Indeed,

$$
\int _ { - 1 } ^ { + 1 } ( 1 - x ) ^ { \alpha } ( 1 + x ) ^ { \beta } d x = 2 ^ { \alpha + \beta + 1 } \frac { \Gamma ( \alpha + 1 ) \Gamma ( \beta + 1 ) } { \Gamma ( \alpha + \beta + 2 ) } .
$$

This is readily established by setting $t = { \frac { 1 } { 2 } } ( 1 + x )$ and using the standard integral for the beta function.

The orthonormal polynomials that result from orthonormalizing ${ \displaystyle 1 , } \pmb { x } ,$ $x ^ { 2 } , \ldots .$ ，with respect to the inner product $( f , g ) = \int _ { - 1 } ^ { 1 } f ( x ) g ( x ) w ( x ) \ d x$ by means of the Gram-Schmidt process are called the Jacobi polynomials, and will be designated by ${ \pmb p } _ { n } ^ { ( \alpha , \beta ) } ( x )$

The following special selections of $\pmb { \alpha }$ and $\beta$ carry special names.

${ \pmb { \alpha } } = { \bf 0 }$ ， $\beta = 0$ :Legendre polynomials   
$\alpha = - \frac { 1 } { 2 }$ ， $\beta = - \textstyle { \frac { 1 } { 2 } }$ : Tschebyscheff polynomials (of the first kind). $\begin{array} { r } { \pmb { \alpha } = \frac { 1 } { 2 } } \end{array}$ ， $\beta = { \textstyle { \frac { 1 } { 2 } } }$ : Tschebyscheff polynomials of the second kind. ${ \pmb { \alpha } } = \beta$ :Ultraspherical polynomials.

We shall also employ orthogonal Jacobi polynomials, $P _ { n } ^ { ( \alpha , \beta ) } ( x )$ ，that have been standardized by requiring that

$$
P _ { n } ^ { ( \alpha , \beta ) } ( 1 ) = \frac { \Gamma ( n + \alpha + 1 ) } { \Gamma ( n + 1 ) \Gamma ( \alpha + 1 ) } .
$$

THEOREM 10.3.1 (Rodrigues' Formula).

$$
P _ { n } ^ { ( \alpha , \beta ) } ( x ) = \frac { ( - 1 ) ^ { n } } { 2 ^ { n } n ! } ( 1 - x ) ^ { - \alpha } ( 1 + x ) ^ { - \beta } \frac { d ^ { n } } { d x ^ { n } } \{ ( 1 - x ) ^ { n + \alpha } ( 1 + x ) ^ { n + \beta } \} .
$$

![](../chunks/Interpolation and Approximation (Philip J. Davis) (z-library.sk, 1lib.sk, z-lib.sk)_part_0004_pages_0211-0280/auto/images/16602d633a1ebf535072688f8703bf0c811684c87c3989421a98f2163f39c943.jpg)  
Figure 10.3.1 The Legendre Polynomials.

Proof: Consider first the expression

$$
Q _ { n } ( x ) = ( 1 - x ) ^ { - \alpha } ( 1 + x ) ^ { - \beta } \frac { d ^ { n } } { d x ^ { n } } \big \{ ( 1 - x ) ^ { n + \alpha } ( 1 + x ) ^ { n + \beta } \big \} .
$$

By Leibnitz’ Formula, we have,

$$
Q _ { n } ( x ) = ( 1 - x ) ^ { - \alpha } ( 1 + x ) ^ { - \beta } \sum _ { j = 0 } ^ { n } { \binom { n } { j } } ( - 1 ) ^ { j } ( n + \alpha ) ( n + \alpha - 1 ) \cdot \cdot \cdot
$$

$$
\begin{array} { c } { { \times ( n + \alpha - j + 1 ) ( 1 - x ) ^ { n + \alpha - j } ( n + \beta ) ( n + \beta - 1 ) \cdots } } \\ { { \times ( n + \beta - n + j + 1 ) ( 1 + x ) ^ { n + \beta - n + j } } } \end{array}
$$

$$
\begin{array} { l } { = \displaystyle \sum _ { j = 0 } ^ { n } \binom { n } { j } ( - 1 ) ^ { j } ( n + \alpha ) ( n + \alpha - 1 ) \cdots ( n + \alpha - j + 1 ) } \\ { \qquad \times ( 1 - x ) ^ { n - j } ( n + \beta ) ( n + \beta - 1 ) \cdots ( \beta + j + 1 ) ( 1 + x ) ^ { j } } \\ { = \displaystyle \sum _ { j = 0 } ^ { n } \binom { n } { j } ( - 1 ) ^ { j } \frac { \Gamma ( n + \alpha + 1 ) } { \Gamma ( n + \alpha - j + 1 ) } \frac { \Gamma ( n + \beta + 1 ) } { \Gamma ( \beta + j + 1 ) } ( 1 - x ) ^ { n - j } ( 1 + x ) ^ { j } . } \end{array}
$$

It is clear from this that $Q _ { n } ( x )$ is a polynomial of degree $\pmb { n }$ .Note also that $\frac { d ^ { j } } { d x ^ { j } } \left[ ( 1 - x ) ^ { n + \alpha } ( 1 + x ) ^ { n + \beta } \right] \mathrm { ~ v a n i s h e s ~ a t ~ } + 1 \mathrm { ~ a n d ~ } - 1 \mathrm { ~ i f ~ } 0 \leq j < n .$

We now show that $Q _ { n }$ is orthogonal to all polynomials in $\mathscr { P } _ { n - 1 }$ and hence is, up to a constant, equal to $P _ { \pmb { n } } ^ { ( \alpha , \beta ) } ( \pmb { x } )$

Let ${ \pmb s } ( { \pmb x } )$ be such a polynomial. Then,

$$
\begin{array} { l } { \displaystyle { I = \int _ { - 1 } ^ { + 1 } ( 1 - x ) ^ { \alpha } ( 1 + x ) ^ { \beta } Q _ { n } ( x ) s ( x ) d x } } \\ { \displaystyle { = \int _ { - 1 } ^ { + 1 } \frac { d ^ { n } } { d x ^ { n } } \left\{ ( 1 - x ) ^ { n + \alpha } ( 1 + x ) ^ { n + \beta } \right\} s ( x ) d x . } } \end{array}
$$

Integrating by parts,

$$
\begin{array} { l } { { I = \displaystyle \frac { d ^ { n - 1 } } { d x ^ { n - 1 } } \left. ( 1 - x ) ^ { n + \alpha } ( 1 + x ) ^ { n + \beta } \right. \Biggl \prod _ { - 1 } ^ { + 1 } } } \\ { { \phantom { \frac { d ^ { n - 1 } } { d x ^ { n - 1 } } \left. ( 1 - x ) ^ { n + \alpha } ( 1 + x ) ^ { n + \alpha } ( 1 + x ) ^ { n + \beta } \right. s ^ { \prime } ( x ) d x } \mathrm { ~ } } } \\ { { \phantom { \frac { d ^ { n - 1 } } { d x ^ { n - 1 } } \left. ( 1 - x ) ^ { n + \alpha } ( 1 + x ) ^ { n + \beta } \right. s ^ { \prime } ( x ) d x } \mathrm { ~ } } } \end{array}
$$

The first term vanishes. Integrate by parts $\pmb { n }$ times.

$$
I = ( - 1 ) ^ { n } { \int _ { - 1 } ^ { + 1 } ( 1 - x ) ^ { n + \alpha } ( 1 + x ) ^ { n + \beta } { s ^ { ( n ) } ( x ) d x } } = 0
$$

inasmuch as $\pmb { \mathscr { s } } ( \pmb { \mathscr { x } } ) \in \mathcal { P } _ { n - 1 }$ and $s ^ { ( n ) } ( x ) \equiv 0$ .We can therefore write $P _ { n } ( x ) =$ ${ \mathfrak { c } } Q _ { n } ( x )$ .From (10.3.6), $Q _ { n } ( 1 ) = ( - 1 ) ^ { n } { \frac { \Gamma ( n + \alpha + 1 ) } { \Gamma ( \alpha + 1 ) } } 2 ^ { n }$ 2n，and hence from (10.3.3), $c = { \frac { ( - 1 ) ^ { n } } { n ! 2 ^ { n } } } .$

COROLLARY 10.3.2.

$$
\begin{array} { l } { { P _ { n } ^ { ( \alpha , \beta ) } ( x ) = \displaystyle \sum _ { j = 0 } ^ { n } \frac { \Gamma ( n + \alpha + 1 ) } { j ! \Gamma ( n + \alpha - j + 1 ) } \frac { \Gamma ( n + \beta + 1 ) } { ( n - j ) ! \Gamma ( \beta + j + 1 ) } \hfill } } \\ { { \mathrm { } \times \left( \frac { x - 1 } { 2 } \right) ^ { n - j } \left( \frac { x + 1 } { 2 } \right) ^ { j } \hfill } } \\ { { \mathrm { } = \displaystyle \sum _ { j = 0 } ^ { n } \left( \begin{array} { l } { { n + \alpha } } \\ { { j } } \end{array} \right) \left( \begin{array} { l } { { n + \beta } } \\ { { n - j } } \end{array} \right) \left( \frac { x - 1 } { 2 } \right) ^ { n - j } \left( \frac { x + 1 } { 2 } \right) ^ { j } } } \end{array}
$$

where weextendthebinomialsymbol $\binom { y } { z }$ to noninteger values in an obvious way.

COROLLARY 10.3.3.

$$
\begin{array} { l } { { P _ { n } ^ { ( \alpha , \beta ) } ( - x ) = ( - 1 ) ^ { n } P _ { n } ^ { ( \beta , \alpha ) } ( x ) . } } \\ { { P _ { n } ^ { ( \alpha , \beta ) } ( - 1 ) = ( - 1 ) ^ { n } \displaystyle \frac { \Gamma ( n + \beta + 1 ) } { \Gamma ( n + 1 ) \Gamma ( \beta + 1 ) } . } } \end{array}
$$

THEOREM 10.3.4. $P _ { n } ^ { ( \alpha , \beta ) } ( x ) = K _ { n } x ^ { n } + S _ { n } x ^ { n - 1 } + \cdot \cdot \cdot$ where

$$
K _ { n } = { \frac { 1 } { 2 ^ { n } } } { \binom { 2 n + \alpha + \beta } { n } }
$$

and

$$
S _ { n } = \frac { \alpha - \beta } { 2 ^ { n } } \binom { 2 n + \alpha + \beta - 1 } { n - 1 } .
$$

Proof:We begin by establishing two identities for binomial coefficients. For $| x | < 1$ we have

Hence,

$$
{ \begin{array} { r l } & { ( 1 + x ) ^ { p } = \displaystyle \sum _ { n = 0 } ^ { \infty } { \binom { p } { n } } x ^ { n } , ~ ( 1 + x ) ^ { \sigma } = \displaystyle \sum _ { m = 0 } ^ { \infty } { \binom { \sigma } { m } } x ^ { m } } \\ & { ( 1 + x ) ^ { p + \sigma } = \displaystyle \sum _ { m , n = 0 } ^ { \infty } { \binom { p } { n } } ( { \binom { \sigma } { m } } x ^ { n + m }  } \\ & { \qquad = \displaystyle \sum _ { n = 0 } ^ { \infty } x ^ { n } \sum _ { j = 0 } ^ { n } { \binom { p } { j } } ( { \binom { \sigma } { n } } - j ) . } \end{array} }
$$

Therefore

$$
\sum _ { j = 0 } ^ { n } { \binom { p } { j } } { \binom { \sigma } { n - j } } = { \frac { 1 } { n ! } } { \frac { d ^ { n } } { d x ^ { n } } } ( 1 + x ) ^ { p + \sigma } { \binom { \sigma + \sigma } { x = 0 } } = { \binom { p + \sigma } { n } } .
$$

utheraee $p ( 1 + x ) ^ { p - 1 } = \sum _ { n = 1 } ^ { \infty } n { \binom { p } { n } } x ^ { n - 1 }$ Hane

$$
p x ( 1 + x ) ^ { p + \sigma - 1 } = \sum _ { n = 0 } ^ { \infty } x ^ { n } \sum _ { j = 1 } ^ { n } j { \binom { p } { j } } { \binom { \sigma } { n - j } } .
$$

# Therefore

$$
\begin{array} { r l } {  { \sum _ { j = 1 } ^ { n } j \binom { p } { j } \binom { \sigma } { n } \binom { \sigma } { n - j } = \frac { 1 } { n ! } \frac { d ^ { n } } { d x ^ { n } } p x ( 1 + x ) ^ { p + \sigma - 1 } \bigg | _ { x = 0 } } } \\ & { = \frac { p } { n ! } \bigg ( x \frac { d ^ { n } } { d x ^ { n } } ( 1 + x ) ^ { p + \sigma - 1 } + n \frac { d ^ { n - 1 } } { d x ^ { n - 1 } } ( 1 + x ) ^ { p + \sigma - 1 } \bigg | _ { x = 0 } } \\ & { = p \binom { p } { n - 1 } . } \end{array}
$$

To prove the theorem,we use Corollary l0.3.2. Notice that

$$
\begin{array} { c } { { ( x - 1 ) ^ { n - j } ( x + 1 ) ^ { j } = [ x ^ { n - j } - ( n - j ) x ^ { n - j - 1 } + \cdot \cdot \cdot ] [ x ^ { j } + j x ^ { j - 1 } + \cdot \cdot \cdot ] } } \\ { { = x ^ { n } + ( 2 j - n ) x ^ { n - 1 } + \cdot \cdot \cdot . } } \end{array}
$$

It is now clear that

$$
K _ { n } = { \frac { 1 } { 2 ^ { n } } } \sum _ { j = 0 } ^ { n } { \binom { n + \alpha } { j } } { \binom { n + \beta } { n - j } } = { \frac { 1 } { 2 ^ { n } } } { \binom { 2 n + \alpha + \beta } { n } } .
$$

The last equality follows from (10.3.9).

In the same way,

$$
\begin{array} { l } { { 2 ^ { n } S _ { n } = \displaystyle \sum _ { j = 0 } ^ { n } ( \begin{array} { l } { { ( n + \alpha ) ( n + \beta ) ( 2 j - n ) } } \\ { { j } } \end{array} ) ( \begin{array} { l } { { ( n - j ) ( 2 j - n ) } } \\ { { ( n - j ) ( 2 ) } } \end{array} ) } } \\ { { = \displaystyle 2 \sum _ { j = 0 } ^ { n } \sum _ { j } ^ { j } { ( \begin{array} { l } { { ( n + \alpha ) ( n + \beta ) } } \\ { { j } } \end{array} ) ( \begin{array} { l } { { ( n + \beta ) ( - n \atop j = 0 } ) - n \sum _ { j = 0 } ^ { n } { ( \begin{array} { l } { { n + \alpha } } \\ { { j } } \end{array} ) ( \begin{array} { l } { { ( n + \beta ) } } \\ { { ( n - j ) } } \end{array} ) } } } \\ { { = \displaystyle 2 ( n + \alpha ) { ( 2 n + \alpha + \beta - 1 ) } - n { ( 2 n + \alpha + \beta ) } } } \\ { { \displaystyle n - 1 } } \end{array} } } \\ { { = ( \alpha - \beta ) { ( \begin{array} { l } { { 2 n + \alpha + \beta - 1 } } \\ { { n - 1 } } \end{array} ) } . } } \end{array}
$$

THEOREM 10.3.5.

$$
\begin{array} { r l } {  { \int _ { - 1 } ^ { 1 } ( 1 - x ) ^ { \alpha } ( 1 + x ) ^ { \beta } ( P _ { n } ^ { ( \alpha , \beta ) } ( x ) ) ^ { 2 } d x } } \\ & { = \frac { 2 ^ { \alpha + \beta + 1 } } { ( 2 n + \alpha + \beta + 1 ) } \frac { \Gamma ( n + \alpha + 1 ) \Gamma ( n + \beta + 1 ) } { \Gamma ( n + 1 ) \Gamma ( n + \alpha + \beta + 1 ) } . } \end{array}
$$

Proof: Write $( 1 - x ) ^ { \alpha } ( 1 + x ) ^ { \beta } = w ( x )$ and $P _ { n } ^ { ( \alpha , \beta ) } = P _ { n }$

$$
I = \int _ { - 1 } ^ { 1 } w ( x ) [ P _ { n } ( x ) ] ^ { 2 } d x = \int _ { - 1 } ^ { 1 } w ( x ) P _ { n } ( x ) P _ { n } ( x ) d x .
$$

Now, $P _ { n } ( x ) = K _ { n } x ^ { n } +$ polynomial of lower degree; hence,

$$
= K _ { n } \int _ { - 1 } ^ { 1 } w ( x ) P _ { n } ( x ) x ^ { n } d x = { \frac { ( - 1 ) ^ { n } K _ { n } } { 2 ^ { n } n ! } } \int _ { - 1 } ^ { + 1 } x ^ { n } { \frac { d ^ { n } } { d x ^ { n } } } \{ ( 1 - x ) ^ { n + \alpha } ( 1 + x ) ^ { n + \beta } \} d x
$$

Integrate by parts $\pmb { n }$ times and obtain

$$
I = \frac { K _ { n } } { 2 ^ { n } } \int _ { - 1 } ^ { + 1 } ( 1 - x ) ^ { n + \alpha } ( 1 + x ) ^ { n + \beta } d x .
$$

By (10.3.2) we have

$$
I = \frac { K _ { n } } { 2 ^ { n } } \cdot 2 ^ { \mathbf { 2 } n + \alpha _ { + } \beta _ { + 1 } } \frac { \Gamma ( n + \alpha + 1 ) \Gamma ( n + \beta + 1 ) } { \Gamma ( 2 n + \alpha + \beta + 2 ) } ,
$$

and the theorem follows.

CoROLLARY 10.3.6. The orthonormal Jacobi polynomials are given by

$$
p _ { n } ^ { ( \alpha , \beta ) } ( x ) = \Big \{ \frac { ( 2 n + \alpha + \beta + 1 ) } { 2 ^ { \alpha + \beta + 1 } } \frac { \Gamma ( n + 1 ) \Gamma ( n + \alpha + \beta + 1 ) } { \Gamma ( n + \alpha + 1 ) \Gamma ( n + \beta + 1 ) } \Big \} ^ { \frac { 1 } { 2 } } P _ { n } ^ { ( \alpha , \beta ) } ( x ) .
$$

CoROLLARy l0.3.7. The kernel polynomial of the orthonormal system has the following expression:

$$
\begin{array} { r l } {  { K _ { n } ( x , y ) = \sum _ { j = 0 } ^ { n } ( x , \beta ) ( x ) p _ { j } ^ { ( \alpha , \beta ) } ( y ) } } \\ & { = \frac { 1 } { \| P _ { n } \| ^ { 2 } } \frac { K _ { n } } { K _ { n + 1 } } \frac { P _ { n + 1 } ^ { ( \alpha , \beta ) } ( x ) P _ { n } ^ { ( \alpha , \beta ) } ( y ) - P _ { n } ^ { ( \alpha , \beta ) } ( x ) P _ { n + 1 } ^ { ( \alpha , \beta ) } ( y ) } { x - y } } \\ & { = \frac { ( n + 1 ) ! \Gamma ( n + \alpha + \beta + 2 ) } { 2 ^ { \alpha + \beta } ( 2 n + \alpha + \beta + 2 ) \Gamma ( n + \alpha + \alpha + 1 ) \Gamma ( n + \beta + 1 ) } } \\ & { \cdot \frac { P _ { n + 1 } ^ { ( \alpha , \beta ) } ( x ) P _ { n } ^ { ( \alpha , \beta ) } ( y ) - P _ { n } ^ { ( \alpha , \beta ) } ( x ) P _ { n + 1 } ^ { ( \alpha , \beta ) } ( y ) } { x - y } . } \end{array}
$$

Proof: This is an application of (10.1.7),(10.3.7),(10.3.13),and Theorem 10.3.5.

THEOREM 10.3.8. The Jacobi polynomials $P _ { n } ^ { ( \alpha , \beta ) } ( x )$ satisfy the following second order linear differential equation.

$$
( 1 - x ^ { 2 } ) y ^ { \prime \prime } + [ ( \beta - \alpha ) - ( \alpha + \beta + 2 ) x ] y ^ { \prime } + n ( n + \alpha + \beta + 1 ) y = 0
$$

Proof: Note that for any $\pmb q$ ，

$$
\begin{array} { c } { { \displaystyle { \frac { d } { d x } } [ ( 1 - x ) ^ { \alpha + 1 } ( 1 + x ) ^ { \beta + 1 } q ^ { \prime } ] = ( 1 - x ) ^ { \alpha } ( 1 + x ) ^ { \beta } } } \\ { { \times [ ( 1 - x ^ { 2 } ) q ^ { \prime \prime } + \{ ( \beta - \alpha ) - ( \alpha + \beta + 2 ) x \} q ^ { \prime } ] . } } \end{array}
$$

![](../chunks/Interpolation and Approximation (Philip J. Davis) (z-library.sk, 1lib.sk, z-lib.sk)_part_0004_pages_0211-0280/auto/images/969f7b7117c9d685ba273278d8648ffad001c01bdf8d3b509018948a3508fb7e.jpg)  
Figure 10.3.2 The Kernel Polynomial for $\alpha = \beta = 0$

Hence we may write the differential equation (lo.3.14) in the alternate form

$$
( 1 - x ) ^ { - \alpha } ( 1 + x ) ^ { - \beta } { \frac { d } { d x } } \left[ ( 1 - x ) ^ { \alpha + 1 } ( 1 + x ) ^ { \beta + 1 } y ^ { \prime } \right] = - n ( n + \alpha + \beta + 1 ) y
$$

Let $y = P _ { \pmb { n } } ^ { ( \alpha , \beta ) } ( \pmb { x } )$ ， $w ( x ) = ( 1 - x ) ^ { \alpha } ( 1 + x ) ^ { \beta }$ and $q ( x ) \in \mathcal P _ { n - 1 }$ . We shall show that the expression occurring on the left side of (lo.3.l6) is orthogonal to $q ( { \pmb x } )$ .Hence the left-hand side must coincide with $_ y$ apart from a constant multiplier. Now,

$$
\begin{array} { l } { { \displaystyle I = \int _ { - 1 } ^ { + 1 } w ( x ) ( 1 - x ) ^ { - \alpha } ( 1 + x ) ^ { - \beta } \frac { d } { d x } [ ( 1 - x ) ^ { \alpha + 1 } ( 1 + x ) ^ { \beta + 1 } y ^ { \prime } ] q ( x ) d x } } \\ { { \displaystyle \quad = \int _ { - 1 } ^ { + 1 } \frac { d } { d x } [ ( 1 - x ) ^ { \alpha + 1 } ( 1 + x ) ^ { \beta + 1 } y ^ { \prime } ] q ( x ) d x . } } \end{array}
$$

Integrate by parts,

$$
I = - \int _ { - 1 } ^ { + 1 } ( 1 - x ) ^ { \alpha + 1 } ( 1 + x ) ^ { \beta + 1 } y ^ { \prime } q ^ { \prime } \ d x .
$$

Integrate by parts once again,

$$
I = \int _ { - 1 } ^ { + 1 } \frac { d } { d x } \left[ ( 1 - x ) ^ { \alpha + 1 } ( 1 + x ) ^ { \beta + 1 } q ^ { \prime } \right] y d x .
$$

Now from (l0.3.15) we observe that

$$
{ \frac { d } { d x } } [ ( 1 - x ) ^ { \alpha + 1 } ( 1 + x ) ^ { \beta + 1 } q ^ { \prime } ] = ( 1 - x ) ^ { \alpha } ( 1 + x ) ^ { \beta } p ( x ) \quad { \mathrm { w h e r e } } \quad p ( x ) \in { \mathcal { P } } _ { n - 1 } .
$$

Hence

$$
I = \int _ { - 1 } ^ { + 1 } ( 1 - x ) ^ { \alpha } ( 1 + x ) ^ { \beta } P _ { n } ^ { ( \alpha , \beta ) } ( x ) p ( x ) d x = 0 .
$$

Thus， certainly,

$( 1 - x ^ { 2 } ) y ^ { \prime \prime } + \{ ( \beta - \alpha ) - x ( \alpha + \beta + 2 ) \} y ^ { \prime } = c y$ for some constant c.

To determine $c$ set $P _ { n } ^ { ( \alpha , \beta ) } ( x ) = y = K _ { n } x ^ { n } + \cdot \cdot \cdot$ . Then dealing only with the highest powers, $- n ( n - 1 ) K _ { n } x ^ { n } - n ( \alpha + \beta + 2 ) K _ { n } x ^ { n } = c K _ { n } x ^ { n }$ Hence $c = - n ( n + \alpha + \beta + 1 )$ as required.

THEOREM 10.3.9. The Jacobi polynomials $P _ { \pmb { n } } ^ { ( \alpha , \beta ) } ( \pmb { x } )$ satisfy the following three-term linearrecurrencerelation

$$
P _ { n } ^ { ( \alpha , \beta ) } ( x ) = ( A _ { n } x + B _ { n } ) P _ { n - 1 } ^ { ( \alpha , \beta ) } ( x ) - C _ { n } P _ { n - 2 } ^ { ( \alpha , \beta ) } ( x )
$$

where

$$
\begin{array} { l } { A _ { n } = \displaystyle \frac { ( 2 n + \alpha + \beta - 1 ) ( 2 n + \alpha + \beta ) } { 2 n ( n + \alpha + \beta ) } } \\ { B _ { n } = \displaystyle \frac { ( \alpha ^ { 2 } - \beta ^ { 2 } ) ( 2 n + \alpha + \beta - 1 ) } { 2 n ( n + \alpha + \beta ) ( 2 n + \alpha + \beta - 2 ) } } \\ { C _ { n } = \displaystyle \frac { ( n + \alpha - 1 ) ( n + \beta - 1 ) ( 2 n + \alpha + \beta ) } { n ( n + \alpha + \beta ) ( 2 n + \alpha + \beta - 2 ) } . } \end{array}
$$

Proof: We combine (10.1.6),(10.3.7), (10.3.8),and (10.3.13). If $p _ { n } ^ { ( \alpha , \beta ) } ( x ) =$ $\lambda _ { n } { \cal P } _ { n } ^ { ( \alpha , \beta ) } ( x )$ ，then

$$
A _ { n } = \frac { K _ { n } } { K _ { n - 1 } } , \qquad B _ { n } = \frac { K _ { n } } { K _ { n - 1 } } \left( \frac { S _ { n } } { K _ { n } } - \frac { S _ { n - 1 } } { K _ { n - 1 } } \right) , \qquad C _ { n } = \left( \frac { \lambda _ { n - 2 } } { \lambda _ { n - 1 } } \right) ^ { 2 } \frac { K _ { n } K _ { n - 2 } } { K _ { n - 1 } ^ { 2 } } .
$$

The expressions above result from this.

THEOREM 10.3.10. In a neighborhood of $w = 0$ , we have

$$
\sum _ { n = 0 } ^ { \infty } P _ { n } ^ { ( \alpha , \beta ) } ( z ) w ^ { n } = \frac { 2 ^ { \alpha + \beta } } { R ( 1 - w + R ) ^ { \alpha } ( 1 + w + R ) ^ { \beta } } ,
$$

$$
R = + { \sqrt { 1 - 2 z w + w ^ { 2 } } } .
$$

The multivalued functions are taken positive for $w = 0$

Proof: Cauchy's Theorem tell us that for analytic functions,

$$
f ^ { ( n ) } ( z ) = { \frac { n ! } { 2 \pi i } } \int _ { C } { \frac { f ( t ) } { ( t - z ) ^ { n + 1 } } } d t
$$

where $\boldsymbol { c }$ is a closed curve containing $_ z$ in its interior.

Consider the function $( 1 - z ) ^ { n + \alpha } ( 1 + z ) ^ { n + \beta }$ In a simply connected region that does not contain $\pm 1$ in its interior,it is possible to define a single valued

analytic branch. Hence,

$$
\frac { d ^ { n } } { d z ^ { n } } ( 1 - z ) ^ { n + \alpha } ( 1 + z ) ^ { n + \beta } = \frac { n ! } { 2 \pi i } \int _ { C } \frac { ( 1 - t ) ^ { n + \alpha } ( 1 + t ) ^ { n + \beta } } { ( t - z ) ^ { n + 1 } } d t
$$

where $c$ is a closed curve that contains $_ z$ in its interior,but does not contain either $z = 1$ or $z = - 1$ .From Rodrigues' formula (10.3.4),

$$
\begin{array} { l } { { P _ { n } ^ { ( \alpha , \beta ) } ( z ) = \displaystyle { \frac { ( - 1 ) ^ { n } } { 2 ^ { n } n ! } \cdot \frac { n ! } { 2 \pi i } } \int _ { C } \displaystyle { \frac { ( 1 - z ) ^ { - \alpha } ( 1 + z ) ^ { - \beta } ( 1 - t ) ^ { n + \alpha } ( 1 + t ) ^ { n + \beta } } { ( t - z ) ^ { n + 1 } } } d t } } \\ { { \displaystyle ~ = \frac { 1 } { 2 \pi i } \int _ { C } \left( \displaystyle { \frac { 1 - t } { 1 - z } } \right) ^ { \alpha } \left( \displaystyle { \frac { 1 + t } { 1 + z } } \right) ^ { \beta } \left( \displaystyle { \frac { t ^ { 2 } - 1 } { 2 ( t - z ) } } \right) ^ { n } \displaystyle { \frac { d t } { t - z } } . } } \end{array}
$$

The points $z = \pm 1$ are excluded from consideration here.

In this integral,make the change of variable

$$
{ \frac { t ^ { 2 } - 1 } { 2 ( t - z ) } } = { \frac { 1 } { w } } ; \qquad t = { \frac { 1 } { w } } ( 1 - \sqrt { 1 - 2 w z + w ^ { 2 } } ) .
$$

Write

$$
t = { \frac { 1 } { w } } \left( 1 - R \right) \quad { \mathrm { w h e r e } } \quad R = { \sqrt { 1 - 2 z w + w ^ { 2 } } } .
$$

Now $t - z = \pm w ( z ^ { 2 } - 1 ) + \cdots$ and so a neighborhood of $t = z$ is mapped conformally onto a neighborhood of $w = 0$

$$
{ \frac { d t } { d w } } = { \frac { 1 } { w ^ { 2 } } } \left( R - 1 - w { \frac { d R } { d w } } \right) \quad { \mathrm { a n d } } \quad { \frac { d R } { d w } } = { \frac { w - z } { R } }
$$

so that

$$
\frac { d t } { d w } = \frac { t - z } { R w } .
$$

Moreover,

$$
{ \frac { 1 + t } { 1 + z } } = { \frac { 1 + 1 / w - R / w } { 1 + z } } = { \frac { 2 } { 1 + w + R } }
$$

and

$$
\frac { 1 - t } { 1 - z } = \frac { 1 - 1 / w + R / w } { 1 - z } = \frac { 2 } { 1 - w + R } .
$$

Hence,

$$
P _ { n } ^ { ( \alpha , \beta ) } ( z ) = \frac { 2 ^ { \alpha + \beta } } { 2 \pi i } \int _ { C _ { 1 } } \frac { d w } { ( 1 - w + R ) ^ { \alpha } ( 1 + w + R ) ^ { \beta } w ^ { n + 1 } R } .
$$

$C _ { 1 }$ is the image of $c$ under the conformal transformation and is a closed curve containing the origin $w = 0$ in its interior.

Applying Cauchy's formula in the $\pmb { w }$ -plane,we see that

$$
P _ { n } ^ { ( \alpha , \beta ) } ( z ) = \frac { 1 } { n ! } \frac { d ^ { n } } { d w ^ { n } } \frac { 2 ^ { \alpha + \beta } } { R ( 1 - w + R ) ^ { \alpha } ( 1 + w + R ) ^ { \beta } } \bigg | _ { w = 0 } .
$$

Now,considered as a function of $\pmb { w }$ $~ , ~ R ^ { - 1 } ( 1 - w + R ) ^ { - \alpha } ( 1 + w + R ) ^ { - \beta }$ is

analytic in a neighborhood of the origin,and we have (10.3.22). For $z = \pm 1$ ， the identity can be verified directly.

# NOTES ON CHAPTER X

General references on orthogonal polynomials include Szego [1], Tricomi [l],Sansone [1],Jackson [2],Alexits [1].The bibliography referred to in the Foreword is the publication of Shohat,Hille,and Walsh [1].

10.1 For an analog of Theorem lO.1.4 for trigonometric Fourier series, see Tricomi [l] pp.75-76.A converse of Theorem l0.1.l was found by Favard and independently by Natanson. See Favard [l].Also relevant is Dickinson,Pollak,and Wannier [].

10.2 Ex.3.,Walsh [2] Chap.VI.Ex.4.,Nehari[1].Ex.5.: these and more extensive values were computed on the IBM 704 at the National Bureau of Standards. For Fejer's Principle see Fejér [1].

# PROBLEMS

1. The powers $x ^ { m }$ cannot be orthogonal on $[ - 1 , 1 ]$ with respect to any weight function $w ( x )$

2. Let $w ( - x ) = w ( x )$ and suppose that $\scriptstyle { \mathcal { P } } _ { n } ( x )$ are orthogonal with respect to $( f , g ) = \int _ { - 1 } ^ { + 1 } f ( x ) g ( x ) w ( x ) d x . \mathrm { T h e n } p _ { n } ( - x ) = ( - 1 ) ^ { n } p _ { n } ( x ) .$

3.How do orthogonal polynomials change when the interval $[ - 1 , 1 ]$ is shifted linearly to $[ a , b ]$ and the weight function changed correspondingly?

4. Let $\begin{array} { r } { p _ { 0 } ( z ) = 1 , p _ { n } ( z ) = z ^ { n - 1 } ( z \ : - \ : z _ { 0 } ) } \end{array}$ $\pmb { n } = 1$ , 2,.... Prove that for $m \neq n$ $\int _ { c } { \frac { p _ { m } ( z ) { \overline { { p _ { n } ( z ) } } } d s } { | z \ - \ z _ { 0 } | ^ { 2 } } } = 0$ on all ircles $C \colon | z | = R > | z _ { 0 } |$

5. Let $\left| a _ { i } \right| < 1$ Prove that the functions

$$
\begin{array} { l } { \displaystyle r _ { 1 } ( z ) = \bigg ( \frac { 1 - \big | a _ { 1 } \big | ^ { 2 } } { 2 \pi } \bigg ) ^ { \frac { 1 } { 2 } } \frac { 1 } { 1 - \overline { { a _ { 1 } } } z } , } \\ { \displaystyle r _ { n } ( z ) = \bigg ( \frac { 1 - \big | a _ { n } \big | ^ { 2 } } { 2 \pi } \bigg ) ^ { \frac { 1 } { 2 } } \frac { ( z - a _ { 1 } ) \cdot \cdot \cdot ( z - a _ { n - 1 } ) } { ( 1 - \overline { { a _ { 1 } } } z ) ( 1 - \overline { { a _ { 2 } } } z ) \cdot \cdot \cdot ( 1 - \overline { { a _ { n } } } z ) } \qquad n = 2 , 3 , \ldots , } \end{array}
$$

are orthonormal in the sense that $\int _ { | z | = 1 } r _ { m } ( z ) \overline { { r _ { n } ( z ) } } d s = \delta _ { m , n }$ (Takenaka,Walsh).

6.Let ${ \mathfrak { p } } _ { n } ^ { * } ( x )$ be orthonormal with respect to the inner product $( f , g ) =$ $\int _ { a } ^ { b } f ( x ) g ( x ) w ( x ) \ d x$ If $K _ { n } ( x , y )$ is the kernel polynomial,and if $x _ { 0 } \leq a$ ,the polynomials $K _ { n } ( x _ { 0 } , x )$ are orthogonal with respect to the inner product $( f , g ) =$ $\int _ { a } ^ { b } f ( x ) g ( x ) w ( x ) ( x - x _ { 0 } ) d x .$

7. Let ${ \mathfrak { p } } _ { n } { } ^ { * } ( x )$ be orthonormal with respect to the inner product $( f , g ) =$ $\int _ { - 1 } ^ { + 1 } f ( x ) g ( x ) w ( x ) \ : d x , w ( x ) > 0 ,$ 、Prove that $\sum _ { k = 0 } ^ { \infty } ( p _ { k } { } ^ { * } ( x ) ) ^ { 2 } = \infty$ for $- 1 \leq x \leq 1$

Check this divergence directly for the Legendre polynomials at $\scriptstyle { \pmb x } = { \pmb 0 }$

8.Using polynomials of degree l and $\| f \| = \operatorname* { m a x } _ { z \in B } { \left| f ( z ) \right| }$ ，prove that if $\boldsymbol { \mathfrak { c } }$ is the circle of smallest radius that contains a closed bounded set $B$ ，then the center of $\boldsymbol { \mathfrak { C } }$ lies in the convex hull of $\pmb { B }$

9.In the previous problem,give an example to show that the center of $c$ may fall on the boundary of the convex hull of $B$ ·

10.Check explicitly for $\pmb { n } = \pmb { 1 }$ ,2,3,4 that the polynomials orthonormal over the square have their zeros in the square.(Cf.10.2,Ex.5.)

11.Prove that $P _ { n } ( 0 ) = 0 , n \det$ d，and that $P _ { n } ( 0 ) = ( - 1 ) ^ { n / 2 } { \frac { 1 \cdot 3 \cdot 5 \cdot \cdot \cdot ( n - 1 ) } { 2 \cdot 4 \cdot 6 \cdot \cdot \cdot n } } , n { \mathrm { ~ e v e n . } }$

$P _ { n } ( x )$ are the Legendre polynomials with normalization (10.3.3).

12.The polynomial $p ( x ) = \sum _ { k = 0 } ^ { n } \frac { 2 k + 1 } { 2 } P _ { k } ( x )$ satisfies $\int _ { - 1 } ^ { + 1 } x ^ { j } p ( x ) \ d x = 1$ for $j = 0 , 1 , \ldots , n$

$$
{ \begin{array} { r l } { \mathrm { 3 . ~ \ S h o w { } t h a t { \ t h e } p o l y n o m i a l { \textit { p } } } ( x ) = \displaystyle \sum _ { j = 0 } ^ { M } ( - 1 ) ^ { j } { \frac { 4 j + 1 } { 2 ^ { 2 j + 1 } } } { \frac { ( 2 j ) ! } { ( j ! ) ^ { 2 } } } P _ { 2 j } ( x ) } & { { \mathrm { s a t i s f i e s } } } \\ { p ( x ) d x = \mathrm { 1 } , \displaystyle \int _ { - 1 } ^ { 1 } p ( x ) x ^ { j } d x = 0 } & { j = \mathrm { 1 } , \mathrm { 2 } , \dots , \mathrm { 2 } M . } \end{array} }
$$

14. Let the $\pmb { n }$ zeros of $P _ { \textbf { \textit { n } } } ^ { ( \alpha , \beta ) }$ be $x _ { 1 } , \ldots , x _ { n }$ Then $x _ { 1 } + x _ { 2 } + \cdot \cdot \cdot + x _ { n } =$ ${ \frac { n ( \beta - { \boldsymbol { \alpha } } ) } { 2 n + \alpha + \beta } } .$

15.Verify (10.3.22) directly for $z = \pm 1$

16.Show that in $\mathcal { P } _ { n } [ - 1 , 1 ]$ with $( f , g ) \ = \int _ { - 1 } ^ { + 1 } f ( x ) g ( x ) \ d x , L ( p ) \ = p ^ { \prime } ( x _ { 0 } )$ isa bounded linear functional,and compute its norm.Generalize.

17. If

then

$$
f ( z ) = \sum _ { k = 0 } ^ { \infty } a _ { k } T _ { k } ( x ) , \left| x \right| \leq 1 \quad \mathrm { w i t h } \quad \sum _ { k = 0 } ^ { \infty } \left| a _ { k } \right| < \infty ,
$$

$$
\int _ { - 1 } ^ { x } f ( t ) d t = \mathrm { c o n s t } + \sum _ { k = 1 } ^ { \infty } \left( \frac { a _ { k - 1 } - a _ { k + 1 } } { 2 k } \right) T _ { k } ( x ) , | x | \leq 1 .
$$

18.The expansion of $f ( x )$ in Tschebyscheff polynomials of the first kind is identical to the development of $f \left( \cos \theta \right)$ in a cosine series.

$$
\begin{array} { l } { { \mathrm { A r c ~ c o s ~ } x \sim \displaystyle \frac { \pi } { 2 } - \frac { 4 } { \pi } { \cal T } _ { 1 } ( x ) - \displaystyle \frac { 1 6 } { 9 \pi } { \cal T } _ { 2 } ( x ) ~ - \cdot \cdot \cdot . } } \\ { { \displaystyle \frac { 1 } { 1 + x ^ { 2 } } \sim \sqrt { 2 } [ \frac { 1 } { 2 } - p ^ { 2 } { \cal T } _ { 2 } ( x ) + p ^ { 4 } { \cal T } _ { 4 } ( x ) ~ - \cdot \cdot \cdot ] , ~ p = \sqrt { 2 } ~ - 1 . } } \end{array}
$$

21.If curves $\boldsymbol { \mathfrak { c } }$ and $_ { D }$ are related by the transformation ${ \pmb w } = { \pmb a } { \pmb z } + { \pmb b }$ ，what is the relationship between the orthonormal polynomials over $\boldsymbol { \mathfrak { c } }$ and those over $\pmb { D } \pmb { \eta }$ What if the inner product is an area integral?

22.How do the symmetries of a curve influence the structure of its orthogonal polynomials (see Ex. 5, 10.2)?

23. Let $\pmb { S }$ be a closed,bounded,convex set in the plane.Let ${ \pmb z _ { 1 } }$ be a point exterior to $\pmb { S }$ 、Show:1. The problem of finding min $| z _ { 1 } - z |$ has a unique soluzES tion, $z ^ { \prime }$ . 2.At $z ^ { \prime }$ draw the line $\ell$ perpendicular to the segment $z _ { 1 } z ^ { \prime }$ Then $\boldsymbol { S }$ lies on one side of l.3.The point $z ^ { \prime }$ satisfies the condition (10.2.9) (O.Shisha).
