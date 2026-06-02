It follows from (6.6.6) that

$$
t ^ { - } ( Q ; Q ) > f ( Q ) - \varepsilon .
$$

By continuity, (6.6.9) must persist in a neighborhood $o$ of $Q$ ：

$$
t ^ { - } ( P ; Q ) > f ( P ) - \varepsilon .
$$

Now let $Q$ run over $\pmb { I }$ ，These neighborhoods cover $\boldsymbol { \mathit { I } }$ ，and we may find a finite number of them $O _ { 1 } , O _ { 2 } , \ldots , O _ { r }$ corresponding to $Q _ { 1 } , \ldots , Q _ { r }$ that cover $\boldsymbol { \mathit { I } }$ Since

$$
t ^ { - } ( P ; Q _ { i } ) > f ( P ) - \varepsilon , \quad P \in O _ { i } , \quad i = 1 , 2 , \ldots , r ,
$$

and since the $O _ { i }$ cover $\boldsymbol { \mathit { I } }$ for every $P \in I$ , the inequality

$$
t ^ { - } ( P ; Q _ { i } ) > f ( P ) - \varepsilon
$$

must hold for some $_ i$

If we set

$$
s ( P ) = \operatorname* { m a x } \left\{ t ^ { - } ( P , Q _ { 1 } ) , \dots , t ^ { - } ( P , Q _ { r } ) \right\}
$$

then by what we have just said,

$$
s ( P ) > f ( P ) - \varepsilon , \mathrm { f o r ~ a l l } \ P \in I .
$$

On the other hand,by (6.6.7), $t ^ { - } ( P ; Q ) < f ( P ) + \varepsilon , P \in { \cal I }$ for all $Q$ Hence, $\begin{array} { r } { s ( P ) < f ( P ) + \varepsilon , P \in I } \end{array}$ .Combining this with (6.6.14),

$$
| f ( P ) - s ( P ) | < \varepsilon , \quad P \in { \cal I } .
$$

Finally,by (6.6.2) iterated, $s ( P ) \in { \pmb { F } }$

Ex.1.Let $\pmb { I }$ be $- \infty < a \le x \le b < \infty$ and ${ \pmb F }$ be the set of all piecewise linear functions defined on $\pmb { I }$ .It iseasy to verify that $\pmb { F }$ satisfies (6.6.2). Condition (6.6.3) can be satisfied with $\varepsilon = 0$ by means of a linear function.Conclusion: Every continuous function can be approximated uniformly on $\pmb { I }$ by continuous piecewise linear functions.

DEFINITION 6.6.1． Let $\pmb { F }$ be a family of real valued functions.By the lattice hull $\pmb { L }$ of $\pmb { F }$ is meant the intersection of all families of functions that contain $\pmb { F }$ and contain the functions max $( f _ { 1 } , f _ { 2 } )$ and min $( f _ { 1 } , f _ { 2 } )$ whenever they contain $f _ { 1 }$ and $f _ { 2 }$

Note that $\mathbf { \mathcal { F } } \subseteq L$ .If all the functions of $\pmb { F }$ are continuous,then the functions of $\scriptstyle { \cal L }$ must also be continuous.

DEFINITION 6.6.2． An algebra $\mathcal { A }$ of real valued continuous functions defined on $\boldsymbol { \mathit { I } }$ is a set of such functions that possesses the following property.

$$
\begin{array} { r } { f _ { 1 } , f _ { 2 } \in \mathcal { A } , \mathrm { c } \mathrm { r e a l } , \mathrm { i m p l i e s } f _ { 1 } + f _ { 2 } \in \mathcal { A } , \mathrm { } c f _ { 1 } \in \mathcal { A } , f _ { 1 } f _ { 2 } \in \mathcal { A } . } \end{array}
$$

Note that (6.6.l6) implies that any polynomial in $f _ { 1 }$ with real coefficients and of the form $a _ { 1 } f _ { 1 } + a _ { 2 } f _ { 1 } { ^ 2 } + \cdots + a _ { n } f _ { 1 } { ^ n } \in { \mathcal { A } }$

LEMMA 6.6.2． Let $\mathcal { A }$ be an algebra of continuous real valued functions defined on I.Let $L$ designate its lattice hull.Then,the elements of $L$ are uniformly approximable by elements of $\mathcal { A }$

Proof:Designate by $\mathcal { B }$ the set of functions that are uniformly approximable by elements of $\mathcal { A }$ .We shall show: (l) $\mathcal { B }$ is an algebra and (2)if $f \in { \mathcal { B } }$ then $| f | \in \mathcal { B }$

Since we have

$$
\operatorname* { m a x } { ( f _ { 1 } , f _ { 2 } ) } = { \textstyle { \frac { 1 } { 2 } } } [ ( f _ { 1 } + f _ { 2 } ) + | f _ { 1 } - f _ { 2 } | ]
$$

$$
\operatorname* { m i n } { ( f _ { 1 } , f _ { 2 } ) } = { \textstyle { \frac { 1 } { 2 } } } [ ( f _ { 1 } + f _ { 2 } ) - | f _ { 1 } - f _ { 2 } | ] ,
$$

it follows from (1） and (2) that if $f _ { 1 }$ ， $f _ { 2 } \in \mathcal { B }$ then max $( f _ { 1 } , f _ { 2 } ) \in \mathcal { B }$ ，and min $( f _ { 1 } , f _ { 2 } ) \in \mathcal { B }$ Since obviously ${ \mathcal { A } } \subseteq { \mathcal { B } }$ ，it will follow from Definition 6.6.1 that $L \subseteq { \mathcal { B } }$ .This will establish the lemma.

As far as (l) is concerned,we need only imitate the familiar proofs of the elementary theorems on limits of sums and products. To prove (2), observe that since the elements of $\mathcal { A }$ are continuous on $\boldsymbol { \mathit { I } }$ ,they are bounded there. Since an $f \in { \mathcal { B } }$ is uniformly approximable by elements of $\mathcal { A }$ ,it,too, must be bounded there. Set $M = \operatorname* { s u p } _ { p \in I } | f ( P ) |$ .By Theorem 6.5.1, let $P ( t )$ be a polynomial with $P ( 0 ) = 0$ and with $\left| P _ { 1 } ^ { \prime } t \right. - \left| t \right| \big | \leq \varepsilon$ for $| t | \leq M$ Since the values of $f$ lie in $[ - M , M ]$ ，we have $\left| P ( f ) - { \dot { | f | } } \right| \leq \varepsilon$ But from (l) and the remark following Definition 6.6.2, $P ( f ) \in { \mathcal { B } }$ .Hence we can find a $g \in \mathcal A$ such that $| P ( f ) - g | \leq \varepsilon .$ .Combining these inequalities, $| | f | - g | \le 2 \varepsilon$ on $\boldsymbol { \mathit { I } }$ Therefore $| f | \in \mathcal { B }$

THEOREM 6.6.3 (Stone-Weierstrass). Let $\mathcal { A }$ be an algebra of real valued continuous functions defined on $\pmb { I }$ In order that an arbitrary continuous real valued function $\pmb { f }$ be uniformly approximable on $\boldsymbol { \mathit { I } }$ by elements of $\mathcal { A }$ itis necessary and sufficient that for any two points $P _ { 1 }$ ， $P _ { \mathfrak { z } } \in I$ and any $\varepsilon > 0$ ，we can find a $g \in \mathcal A$ such that $| f ( P _ { i } ) - g ( P _ { i } ) | \leq \varepsilon$ ， $i = 1$ ，2.

Proof: If $f$ is uniformly approximable on $\pmb { I }$ by elements in $\mathcal { A }$ ，then this condition obviously holds.Suppose,conversely，that the condition holds. Let $L ( { \mathcal { A } } )$ denote the lattice hull of $\mathcal { A }$ and let $f$ be continuous on $\boldsymbol { I }$ For any two points $P _ { 1 } , P _ { 2 } \in I$ ,and any $\varepsilon > 0$ ,we can find a $g \in \mathcal A$ (and a fortiori $\in L ( \mathcal { A } ) )$ such that $| f ( P _ { i } ) - g ( P _ { i } ) | \leq \varepsilon$ ， $i = 1$ ,2.Hence,by Lemma 6.6.1 with ${ \pmb F } = { \pmb L } ( { \pmb \mathcal { A } } )$ ,we can approximate $f$ uniformly on $\pmb { I }$ by elements of $L ( \mathcal { A } )$ .On the other hand,the elements of $\pmb { L } ( \mathcal { A } )$ can，by Lemma 6.6.2, be uniformly approximated by the elements of $\mathcal { A }$ itself.Combining these two approximations,we can approximate $f$ by elements of $\mathcal { A }$

COROLLARY 6.6.4．Let $f ( x _ { 1 } , \dots , x _ { s } )$ be real and continuous on $\pmb { I }$ Then it can be approximated uniformly on $\boldsymbol { I }$ by polynomials in $x _ { 1 } , x _ { 2 } , \dotsc , x _ { S }$

Proof: For the algebra $\mathcal { A }$ take the set of polynomials in $x _ { 1 } , x _ { 2 } , \dotsc , x _ { S }$

Let $P _ { i } \colon ( x _ { 1 } ^ { ( i ) } , x _ { 2 } ^ { ( i ) } , \ldots , x _ { N } ^ { ( i ) } )$ ， $i = 1 , 2$ , be distinct points and consider

$$
g ( x _ { 1 } , x _ { 2 } , \ldots , x _ { N } ) = f ( P _ { 1 } ) + \frac { f ( P _ { 2 } ) - f ( P _ { 1 } ) } { \underset { i = 1 } { N } ( x _ { 1 } ^ { ( 2 ) } - x _ { i } ^ { ( 1 ) } ) ^ { 2 } } \underset { i = 1 } { \overset { N } { \sum } } ( x _ { i } - x _ { i } ^ { ( 1 ) } ) ( x _ { i } ^ { ( 2 ) } - x _ { i } ^ { ( 1 ) } ) .
$$

This is a polynomial in ${ \pmb x } _ { 1 } , \ldots , { \pmb x } _ { N }$ and $g ( P _ { i } ) = f ( P _ { i } ) , i = 1 , 2$ The conditions of Theorem 6.6.3 are satisfied with $\varepsilon = 0$

# NOTES ON CHAPTER VI

6.2-6.3 Bernstein polynomials are described in Gontscharoff [1],Natanson [l]，pp.1-7,174-l82.Lorentz [1] is a penetrating study of these interesting polynomials and includes a discussion of their behavior in the complex plane,applications to moment problems,and generalizations.

For Theorem 6.3.4 and for applications of the Bernstein polynomials to variation reducing approximations, see Schoenberg [1].

For a deeper study of the rate of convergence of the Fejér scheme in Theorem 6.4.1,see Shisha et al.[1].

An interesting and unifying approach to Theorems 6.2.2, 6.4.1,and 12.2.8 (Bernstein and Fejér) is provided by the theory of positive linear functionals as developed by Korovkin in [2].

6.5Walsh [2],p.310.

6.6The Stone-Weierstrass theorem can be found in McShane and Botts [1],Dieudonné [1],pp.l31-l34.Dunford and Schwartz [1],pp.272,383- 385.The chapter by Stone in Buck [6] is highly recommended.

# PROBLEMS

1. Let $f ( x ) \in C ^ { 1 } [ a , b ]$ .If $p ( x )$ is a polynomial that approximates $f ^ { \prime }$ to within εon $[ a , b ]$ then $q ( x ) = \int _ { a } ^ { x } p ( x ) d x + f ( a )$ isa polynomial that approximates $\pmb { f }$ to within $( b ~ - ~ a ) \varepsilon$ on $[ a , b ]$ .Extend to higher derivatives.

2. Let $f ( x ) \in C ^ { \infty } [ a , b ]$ . Show (without using Bernstein polynomials) that we can find a sequence of polynomials $\textstyle p _ { n } ( x )$ such that $\operatorname * { l i m } _ { n  \infty } ~ \mathcal { P } _ { n } ^ { ( j ) } ( x ) ~ = f ^ { ( j ) } ( x )$ uniformly on $[ a , b ] \quad j = 0 , 1 , \ldots .$

3. Let $p _ { n k } ( x ) = { \binom { n } { k } } x ^ { k } ( 1 - x ) ^ { n - k } , 0 \leq x \leq 1$ ，Prove that the maximum value ocurset $x = { \frac { k } { n } }$ .If ${ \frac { k } { n } } \to x$ $n  \infty , p _ { n k } \bigg ( \frac { k } { n } \bigg )$ is asymptotically equal to n

4. Bernstein polynomials over the interval $[ a , b ]$ may be defined by

$$
B _ { n } ( f , a , b ; x ) = { \frac { 1 } { h ^ { n } } } \sum _ { k = 0 } ^ { n } f \left( a + { \frac { k } { n } } h \right) { \binom { n } { k } } ( x - a ) ^ { k } ( b - x ) ^ { n - k } , \qquad h = b - a .
$$

Prove a theorem analogous to Theorem 6.2.2.

5. Compare $B _ { 4 } ( \sqrt { x } ; \frac { 1 } { 2 } )$ with $\boldsymbol { \sqrt { \frac { 1 } { 2 } } }$

6. Let $S ( x ) = \left| 2 x \mathrm { ~ - ~ } 1 \right|$ ， $0 \leq x \leq 1$ . Compute $B _ { 4 } ( S ( x ) ; x ) , B _ { 6 } ( S ( x ) ; x )$ . Show $B _ { 2 n } \biggl ( S ( x ) ; \frac { 1 } { 2 } \biggr ) \ = \frac { 1 } { 2 ^ { 2 n } } \binom { 2 n } { n }$ and study the rapidity of the approach to O of $S ( \Sigma ) \ - \ B _ { 2 n } ( S ( x ) ; \Sigma )$

7. Let $f ( x ) = 0$ for $0 \leq x \leq \frac { 1 } { 2 } , f ( x ) = x - \frac { 1 } { 2 }$ for $\textstyle { \frac { 1 } { 2 } } \leq x \leq 1$ .Show that $B _ { 2 n } ( f ; x )$ has nth order contact with $f$ at both O and 1.

8. Verify Voronovsky's Theorem for $f ( x ) = e ^ { x }$ by a direct computation.

9.Obtain an explicit expression for $B _ { n } ( x ^ { 3 } ; x )$ and show directly that

$$
\operatorname * { l i m } _ { n  \infty } n [ B _ { n } ( x ^ { 3 } ; x ) - x ^ { 3 } ] = 3 x ^ { 2 } ( 1 - x ) .
$$

10.Let $f ( x ) \in C [ a , b ]$ .It is uniformly approximable on $[ a , b ]$ by polynomials with rational coefficients.

11. If $f ( x ) \in C [ a , b ] ,$ ， uniform approximation by polynomials with integer coeffcients is not necessarily possible.

12. Prove Ex. 1,6.6 directly.

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

![](images/9a3a6d4a2ad69e5ff1e64171e2c57891cb492f313b396f8fdadf5814c3a12db4.jpg)  
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

![](images/8c222413fd4d3181bedec24f4f195e9905bbe39f6e9c3e7ea05d326d66394a80.jpg)  
Figure 7.3.1 A Convex Set.

![](images/2752b0ec1f8eedb8a46a26870ea999a27e997dc1689e11503cf935024ecc8f01.jpg)  
Figure 7.3.2 The Convex Hull.

![](images/9dc2aa1f4a747e85f4f0ddef7061142c2a9420257328ea56f65c30505676cbe3.jpg)  
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

![](images/2483af4043f9bbf024da3f55e851c82f4fe63a4b2e39d01a3266cdfa4bebac97.jpg)  
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

![](images/47725b094955b1407a0820951040d353f46c8ca237bb322b9ec8aee7a9d52a18.jpg)  
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

![](images/34009bb01abd2fdb95e55d1635da660f03d75c632a633ded58b3e24791349794.jpg)  
Figure 7.6.1.

![](images/1dc208a4644ba1087a953d9287de737d4ff4c9133956e032615da35d344aff3a.jpg)  
Figure 7.6.2.

![](images/b1126b461ca6b6fd955117085bbea5cb86fbe0e537e69d99f09e6d2ad69a7486.jpg)  
Figure 7.6.3.

Notice that when the error curve $\varepsilon ( x ) = f ( x ) - c$ is drawn, the value $\pm \pmb { { \cal E } _ { 0 } }$ is assumed by it at least twice: once with a plus sign and once with a minus sign.Suppose next that $p _ { 1 } ( x ) = a _ { 0 } + a _ { 1 } x$ solves the problem of fnding $P \in \mathcal { P } _ { 1 } \ a \leq x \leq b$ $| f ( x ) - p ( x ) |$ . Consider the error curve $\pmb \varepsilon ( \pmb x ) = \pmb f ( \pmb x ) - p _ { 1 } ( \pmb x )$ Set $E _ { 1 } \dot { = } \operatorname* { m a x } _ { a \le x \le b } | f ( x ) - p _ { 1 } ( x ) |$ .Since $| \varepsilon ( x ) |$ is in $C [ \boldsymbol { a } , \boldsymbol { b } ]$ ,this maximum is assuined at least once.If it were taken on only once (Fig.7.6.3) then by the addition of an appropriate constant to ${ p } _ { 1 } ( { \pmb x } )$ we could lower $\pmb { { \cal E } } _ { 1 }$ .This would contradict the definition of ${ \pmb E _ { 1 } }$

Suppose $E _ { 1 }$ is taken on only two times.It must be taken on with opposite signs,otherwise we can argue as above and lower $\pmb { { \cal E } } _ { 1 }$ .But even if it were taken on with opposite signs,we could subtract from $\varepsilon ( x )$ ,and hence from the original $p _ { 1 } ( x )$ ，an appropriate linear function which would have the effect of reducing the size of the maximum values without raising other values in excess of this.This is more or less evident geometrically (look at the dashed line in Fig.7.6.4),but we can formalize the argument in this way.

![](images/08a62f0d1c366022bd926f12cd2a6d73da749523b5b29dc3f6ee617974b743de.jpg)  
Figure 7.6.4.

Let $\pmb { \varepsilon } ( \pmb { x _ { 1 } } ) = + \pmb { E _ { 1 } }$ and $\varepsilon ( x _ { 2 } ) = - E _ { 1 }$ .By continuity,we can find two closed intervals, $I _ { 1 }$ containing $\pmb { x _ { 1 } }$ ,and $\boldsymbol { I } _ { 2 }$ containing $x _ { \pmb { 2 } }$ such that $\varepsilon ( x ) > E _ { 1 } / 2$ in $I _ { 1 }$ and $\varepsilon ( x ) < - E _ { 1 } / 2$ in $I _ { 2 } . I _ { 1 }$ and $I _ { 2 }$ are disjoint, for $\varepsilon ( x )$ is of opposite sign in them.Pick a point $\pmb { x _ { 0 } }$ between $x _ { 1 }$ and $x _ { \mathbf { 2 } }$ ，but exterior to these intervals, and let $\ell ( x )$ be a fixed linear function that passes through $\pmb { x _ { 0 } } .$ is positive in $\scriptstyle { I _ { 1 } }$ ,and negative in $I _ { 2 }$ (Fig. 7.6.5)

![](images/6d6ce6a65725670557b60d6b3b817677b6a0a1b02edfce487904eba604820d76.jpg)  
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

![](images/cbe9d333c65d6f99cc548e66e2f0ff8b2cfd1db174efe9c236875a8fbde631a1.jpg)  
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

![](images/52b42685cb46d837292f528fdbfafa716a082a59262774746305c1d9b8110387.jpg)  
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

![](images/66b3c5df84e0f135f138329d20fb1d0b5f97f977b11728a7788ec24dd02fcd78.jpg)  
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

![](images/12e8c39025531ceed05a195f31f63ed7be163d958d7933efee4b751d12e1b51d.jpg)  
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

![](images/d1f446c4de5299d6cf2e849a362ead2de891e46cab18528300618f0da2766267.jpg)  
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

![](images/a9b79937081326fb611a34749e846bda844b973cf32d80e5921498c0f91478f9.jpg)  
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