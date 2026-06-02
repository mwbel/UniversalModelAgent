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

![](images/0f430966813b6d854a223d8c826537346f5e32d3135094c387e287c0ff1a52a9.jpg)  
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

![](images/494618cabf8729ba894489ed31ca80cdd70258a73373c03a0f151fd7863fcd1f.jpg)  
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

![](images/34952666b46ead1774376cf245c776e95cffec98617a820f6b03668361e50b1d.jpg)  
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

![](images/5bbbc8926acfbdddfc5eb6f5849c290dbc73059e97344f72465cecd67f474cfa.jpg)  
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

![](images/5a9c99361672df4c163ff7c7c050e19a4e03be798e3df4a810416a06ad43326e.jpg)  
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

![](images/16602d633a1ebf535072688f8703bf0c811684c87c3989421a98f2163f39c943.jpg)  
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

![](images/969f7b7117c9d685ba273278d8648ffad001c01bdf8d3b509018948a3508fb7e.jpg)  
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

# CHAPTER XI

# The Theory of Closure and Completeness

11.1 The Fundamental Theorem of Closure and Completeness. Theorem 8.9.l related the concepts of closure and completeness for inner product spaces.In the present section，we shall do this for normed linear spaces.

DEFINITIoN ll.1.1． The sequence of elements $\left\{ x _ { k } \right\}$ is complete in a normed linear space $\pmb { X }$ if $L ( x _ { k } ) = 0$ ， $k = 1$ ,2,..., $\ b { L } \in \ b { X } ^ { * }$ ,implies $\mathbf { L } = \mathbf { 0 }$ $X ^ { * }$ is the normed conjugate space of $\pmb { X }$

(In an inner product space,there are now two definitions of complete sequences,Definition 8.9.4 and Defnition l1.1.1. If the space is complete, these definitions are equivalent.)

<table><tr><td rowspan="2">Space</td><td>Closed</td><td>Complete</td></tr><tr><td>A subspace is closed if it contains all its limit points.</td><td>A space is complete if every Cauchy sequence has a limit in the space.</td></tr><tr><td>Sequence</td><td>A sequence is closed if every element of the space can be approximated ar- bitrarilycloselyby finite linear combinations of the elements of the sequence.</td><td>A sequence {xn} is complete if L(xn)=0,n=0,1,..., L ∈X*,implies L=0.</td></tr></table>

The fundamental theorem is that closure and completeness are equivalent concepts.This emerges as a consequence of the Hahn-Banach Extension Theorem,and it is to this that we now turn.

DEFINITION 11.1.2．Let $\pmb { X }$ be a linear space and $\pmb { Y }$ a linear subspace. Let $L$ be a linear functional defined on $\pmb { Y }$ .A linear functional $L _ { 1 }$ is called an extension of $\pmb { L }$ to $\pmb { X }$ if $L _ { 1 } ( x )$ is defined for all ${ \pmb x } \in { \pmb X }$ and if $L _ { 1 } ( x ) = L ( x )$ for $\pmb { x } \in \pmb { Y }$

Ex.1. $\pmb { X }$ is the space of all functions defined on $[ a , b ]$ .Let $\pmb { Y }$ be the subspace $C [ \pmb { a } , \pmb { b } ]$ Let $a < x _ { 1 } < b$ and set $L ( f ) = \operatorname* { l i m } f ( x )$ .Let $L _ { 1 } ( f ) = f ( x _ { 1 } )$ Then $\mathbf { L _ { 1 } }$ is an extension of $\pmb { L }$ from $\pmb { Y }$ to $x$ $\pmb { x } \mathrm {  } \pmb { x } _ { 1 }$ -

THEOREM 11.1.1．Let $\pmb { X }$ be $^ { \pmb { a } }$ real normed linear space and $\pmb { Y }$ a linear subspace. ( $Y \neq X .$ .Let ${ \pmb p } ( { \pmb x } )$ be a real valued functional defined on the elements of $\pmb { X }$ and possessing the following normlike properties

$$
\begin{array} { r l } { p ( x ) \geq 0 ; } & { \quad x \in X } \\ { p ( x + y ) \leq p ( x ) + p ( y ) ; } & { \quad x , y \in X } \\ { p ( \lambda x ) = \lambda p ( x ) ; } & { \quad x \in X , \lambda \geq 0 . } \end{array}
$$

Let $L$ be $^ { \pmb { a } }$ real linear functional defined on $Y$ that satisfies

$$
L ( x ) \leq p ( x ) , \qquad x \in Y .
$$

Then $L$ can be extended to be $^ { \pmb { a } }$ linear functional $L _ { 1 }$ defined on $\pmb { X }$ and such that

$$
L _ { 1 } ( x ) \leq p ( x ) , \qquad x \in X .
$$

Proof: 1. Select an $\pmb { x _ { 0 } } \in X$ but $\notin Y$ Take $\textstyle { \pmb { x } } , y \in { \pmb { Y } }$ Then

$$
L ( y ) - L ( x ) = L ( y - x ) \leq p ( y - x ) .
$$

Now $p ( y - x ) \leq p ( y + x _ { 0 } ) + p ( - x - x _ { 0 } )$ so that

$$
- p ( - x - x _ { 0 } ) - L ( x ) \leq p ( y + x _ { 0 } ) - L ( y ) ; \qquad x , y \in Y .
$$

Think of $_ y$ as fixed in $\pmb { Y }$ and $_ { \pmb { x } }$ as varying in $\pmb { Y }$ .Then the last inequality shows that $- p ( - x - x _ { 0 } ) - L ( x )$ is bounded above. Similarly,for varying $y , p ( y + x _ { 0 } ) - L ( y )$ is bounded below.If we set

$$
\begin{array} { l } { r _ { 1 } = \underset { x \in Y } { \operatorname* { s u p } } \left[ - p ( - x - x _ { 0 } ) - L ( x ) \right] } \\ { r _ { 2 } = \underset { y \in Y } { \operatorname* { i n f } } \left[ p ( y + x _ { 0 } ) - L ( y ) \right] } \end{array}
$$

then we must have $- \infty < r _ { 1 } \le r _ { 2 } < \infty$ .Select a number $\pmb { r }$ such that $r _ { 1 } \leq r \leq r _ { 2 } .$ Then,

$$
- p ( - x - x _ { 0 } ) - L ( x ) \leq r \leq p ( y + x _ { 0 } ) - L ( y )
$$

for any $\textstyle { \boldsymbol { \mathfrak { x } } } , { \boldsymbol { \mathfrak { y } } } \in Y$

2.Consider the linear subspace $Y _ { 0 }$ consisting of all elements $_ y$ of the form $y = x + \lambda x _ { 0 }$ ， $\pmb { x } \in \pmb { Y }$ .Each element in $\mathbf { { \mathit { Y } } _ { 0 } }$ has a unique representation in this form. For suppose, $y \in Y _ { \mathbf { \pmb { \theta } } }$ and $y = x _ { 1 } + \lambda _ { 1 } x _ { 0 } = x _ { 2 } + \lambda _ { 2 } x _ { 0 }$ Then $x _ { 1 } - x _ { 2 } = ( \lambda _ { 1 } - \lambda _ { 2 } ) x _ { 0 }$ If $\lambda _ { 1 } \neq \lambda _ { 2 }$ then $\pmb { x _ { 0 } }$ would be a linear combination of ${ \pmb x _ { 1 } } , { \pmb x _ { 2 } }$ and hence in $\pmb { Y }$ .This contradicts our selection of $\pmb { x _ { 0 } }$ . Therefore $\lambda _ { 1 } = \lambda _ { 2 }$ and hence also 𝑥1 = x2.

Define $L _ { 1 }$ on $\boldsymbol { Y } _ { \boldsymbol { \mathfrak { o } } }$ by means of

$$
L _ { 1 } ( y ) = L ( x ) + \lambda r .
$$

Now if $y \in Y , \lambda = 0$ and hence $L _ { 1 } ( y ) = L ( y )$ ， $y \in Y$ Since $\pmb { L }$ is linear,it follows easily that $L _ { 1 }$ is linear.

We wish to prove next that

$$
L _ { 1 } ( y ) \leq p ( y ) \qquad { \mathrm { f o r ~ a l l } } \quad y \in Y _ { 0 } .
$$

Decompose $_ y$ into the form $y = x _ { 1 } + \lambda x _ { 0 }$ .We need only deal with the case when $\lambda \neq 0$ .From (11.1.4) we have

$$
- p \Big ( - \frac { x _ { 1 } } { \lambda } - x _ { 0 } \Big ) - L \Big ( \frac { x _ { 1 } } { \lambda } \Big ) \leq r \leq p \Big ( \frac { x _ { 1 } } { \lambda } + x _ { 0 } \Big ) - L \Big ( \frac { x _ { 1 } } { \lambda } \Big ) .
$$

Now if $\lambda > 0 , p \Big ( \frac { x _ { 1 } } { \lambda } + x _ { 0 } \Big ) = \frac { 1 } { \lambda } p ( x _ { 1 } + \lambda x _ { 0 } )$ and the second inequality reduces to

$$
r \leq { \frac { 1 } { \lambda } } p ( x _ { 1 } + \lambda x _ { 0 } ) - { \frac { 1 } { \lambda } } L ( x _ { 1 } )
$$

or

$$
L _ { 1 } ( y ) = L ( x _ { 1 } ) + \lambda r \leq p ( x _ { 1 } + \lambda x _ { 0 } ) .
$$

If $\lambda < 0$ ,the first inequality may be employed:

$- p \left( - { \frac { x _ { 1 } } { \lambda } } - x _ { 0 } \right) = { \frac { 1 } { \lambda } } p ( x _ { 1 } + \lambda x _ { 0 } ) ; { \mathrm { h e n c e } } , p ( x _ { 1 } + \lambda x _ { 0 } ) - L ( x _ { 1 } ) \geq \lambda r$ and the conclusion is as before.

3.Consider,finally,all the linear functionals that extend $L$ to some linear subspace containing $\pmb { Y }$ and which satisfy the condition (ll.1.5).A partial ordering $L ^ { \prime } \leq L ^ { \prime }$ is defined amongst these functionals by agreeing that $L ^ { \prime } \leq L ^ { \prime \prime }$ means that $L ^ { \prime \prime }$ is an extension of $L ^ { \prime }$ .With this ordering, every totally ordered subset is seen to have an upper bound,i.e., the functional which is defined over the union of the domains of definition of the individual functionals and which takes on the values assgned by them. Zorn's Lemma (Theorem l.l3.l) tells us that there exists a maximal extension $L _ { 1 }$ .This linear functional is defined over the entire space $\pmb { X }$ ,for if not, it could have been further extended by the process described under 2.

If the space $\pmb { X }$ is separable,the use of Zorn's Lemma (and hence the axiom of choice) can be avoided.

A functional ${ \pmb p } ( { \pmb x } )$ satisfying ll.1.1 is known as $^ { \pmb { a } }$ convex functional.

THEOREM 11.l.2 (Hahn-Banach). Let $\pmb { X }$ be $^ { \pmb { a } }$ real normed linear space and $\pmb { Y }$ a subspace. Let $L$ be defined on $\pmb { Y }$ and have norm $\| L \| _ { \mathcal { F } }$ there. Then there is $^ { \pmb { a } }$ linear functional $L _ { 1 }$ which extends $\scriptstyle { \cal L }$ to $\pmb { X }$ and such that $\| L _ { 1 } \| _ { X } =$ $\| L \| _ { Y }$

Proof: Set $p ( { \pmb x } ) = \| { \pmb L } \| _ { V } \| { \pmb x } \|$ . The functional ${ \pmb p } ( { \pmb x } )$ is readily seen to fulfll the requirements (li.l.l). Therefore, by the previous theorem，we may extend $\pmb { L }$ to $L _ { 1 }$ so that

$$
L _ { 1 } ( x ) \leq \| L \| _ { Y } \| x \| , \qquad x \in X .
$$

Since also

$$
- L _ { 1 } ( x ) = L _ { 1 } ( - x ) \leq \| L \| _ { Y } \| - x \| = \| L \| _ { Y } \| x \| ,
$$

it follows that

$$
\left| L _ { 1 } ( x ) \right| \leq \left\| L _ { 1 } ^ { \prime } \right\| _ { Y } \left\| x \right\| .
$$

Hence,

$$
\operatorname* { s u p } _ { x \in X } { \frac { | L _ { 1 } ( x ) | } { \| x \| } } \leq \| L \| _ { Y }
$$

so that

$$
\| L _ { 1 } \| \leq \| L \| _ { Y } .
$$

But $\| L \| _ { Y } = \operatorname* { s u p } _ { x \in Y } { \frac { | L ( x ) | } { \| x \| } } = \operatorname* { s u p } _ { x \in Y } { \frac { | L _ { 1 } ( x ) | } { \| x \| } } \leq \operatorname* { s u p } _ { x \in X } { \frac { | L _ { 1 } ( x ) | } { \| x \| } } = \| L _ { 1 } \| _ { X }$ and therefore $\| L \| _ { Y } \leq \| L _ { 1 } \| _ { X }$ Thus,finally $\| L _ { 1 } \| _ { X } = \| L \| _ { Y }$

This extension theorem also holds in complex normed linear spaces.To establish this,we make use of a simple device which associates a unique real normed linear space $X _ { R }$ to each complex normed linear space $\pmb { X }$ In this way,the burden of the proof is thrown back to the real situation.

DEFINITION 11.1.3． Let $\pmb { X }$ be a complex normed linear space.The space $X _ { R }$ will consist of the same elements as $\pmb { X }$ .Addition in $\scriptstyle { X _ { R } }$ will be identical with addition in $\pmb { X }$ If $\pmb { a }$ is real and ${ \boldsymbol { x } } \in { \boldsymbol { X } } _ { R }$ then $\pmb { a x }$ will be the element $( a + i 0 ) x = a x$ of $\pmb { X }$ $\| x \|$ in $X _ { R }$ will equal $\| x \|$ in $\pmb { X }$ .If $L$ is a bounded (and complex) linear functional defined on $\pmb { X }$ ,then by $L _ { R }$ we shall mean the real valued functional defined on $X _ { R }$ by means of

$$
L _ { R } ( x ) = { \mathrm { R e a l ~ p a r t ~ o f ~ } } L ( x ) .
$$

The $_ { \pmb { x } }$ in the left-hand member is considered to lie in $X _ { R }$ while in the right it is considered to lie in $\pmb { X }$

LEMMA 11.1.3．If $\scriptstyle { \cal L }$ is $^ { \pmb { a } }$ bounded linear functional on $\pmb { X }$ then $L _ { R }$ is $^ { \pmb { a } }$ bounded linear functional on $X _ { R }$

Proof: Let $_ { \pmb { x } }$ $\mathfrak { e } , \mathfrak { y } \in  {  { \cal X } } _ { R }$ and $a , b$ be real.

$$
{ \begin{array} { r l } & { L _ { R } ( a x + b y ) = \operatorname { R e } L ( a x + b y ) } \\ & { \qquad = \operatorname { R e } { \big \{ } a L ( x ) + b L ( y ) { \big \} } = a \operatorname { R e } L ( x ) + b \operatorname { R e } L ( y ) } \\ & { \qquad = a L _ { R } ( x ) + b L _ { R } ( y ) . } \end{array} }
$$

Therefore $L _ { R }$ is linear on $X _ { R }$ Also

$$
| L _ { R } ( x ) | = | { \mathrm { R e } } L ( x ) | \leq | L ( x ) | \leq \| L \| \ \| x \| _ { x } = \| L \| \ \| x \| _ { X _ { R } } .
$$

Therefore $L _ { R }$ is bounded on $X _ { R }$ ,and $\| L _ { R } \| \leq \| L \|$

LEMMA 11.1.4.If $L$ is a linear functional on $\pmb { X }$ then

$$
L ( x ) = L _ { R } ( x ) - i L _ { R } ( i x ) .
$$

Conversely if $\Lambda$ is $\pmb { a }$ linear functional on $X _ { R }$ , then the equation

$$
L ( x ) = \Lambda ( x ) - i \Lambda ( i x )
$$

defines a linear functional on $\pmb { X }$

Proof: If $L ( x ) = \operatorname { R e } L ( x ) + i \operatorname { I m } L ( x ) , x \in X$ ，then

$$
\begin{array} { r } { L ( i x ) =  { \mathrm { R e } } L ( i x ) + i  { \mathrm { I m } } L ( i x ) } \\ { = i  { \mathrm { R e } } L ( x ) -  { \mathrm { I m } } L ( x ) . } \end{array}
$$

Therefore Im $L ( x ) = - \mathrm { R e } L ( i x ) = - L _ { R } ( i x )$ ,so (11.1.8) follows.Conversely, given $\textstyle { \boldsymbol { \mathscr { x } } } , y \in X$ ,from (ll.l.9) we see that

$$
\begin{array} { r l } & { L ( { \pmb x } + { \pmb y } ) = \Lambda ( { \pmb x } + { \pmb y } ) - i \Lambda ( i { \pmb x } + i { \pmb y } ) } \\ & { \qquad = \Lambda ( { \pmb x } ) + \Lambda ( { \pmb y } ) - i \Lambda ( i { \pmb x } ) - i \Lambda ( i { \pmb y } ) } \\ & { \qquad = L ( { \pmb x } ) + L ( { \pmb y } ) . } \end{array}
$$

Moreover, if $\pmb { a }$ is real,

$$
\begin{array} { c } { { L ( a x ) = \Lambda ( a x ) - i \Lambda ( i a x ) } } \\ { { = a \Lambda ( x ) - i a \Lambda ( i x ) = a L ( x ) . } } \end{array}
$$

Finally,

$$
\begin{array} { c } { { L ( i x ) = \Lambda ( i x ) - i \Lambda ( - x ) } } \\ { { = i [ \Lambda ( x ) - i \Lambda ( i x ) ] = i L ( x ) . } } \end{array}
$$

Thus, $\pmb { L }$ is linear over $\pmb { X }$

THEOREm 1l.1.5 (Bohnenblust-Sobczyk-Suchomlinoff). Let $\pmb { X }$ be a complex normed linear space and $\pmb { Y }$ a subspace. Let $\scriptstyle { \cal L }$ be a complex linear functional defined on $\boldsymbol { Y }$ and have norm $\| L \| _ { Y }$ there.Then there is $^ { \pmb { a } }$ linear functional $L _ { 1 }$ that extends $L$ to $\pmb { X }$ and such that $\| L _ { 1 } \| _ { X } = \| L \| _ { Y }$

Proof: Write $L ( x ) = L _ { R } ( x ) + i L _ { I } ( x )$ ， ${ \pmb x } \in { \pmb Y }$ where $L _ { R }$ and $L _ { I }$ are real valued. By Lemma l1.1.3, $L _ { R }$ is a bounded real valued linear functional defined on $Y _ { R }$ ，the real normed linear space associated with $\boldsymbol { Y }$ .Extend $L _ { R }$ to $X _ { R }$ by Theorem ll.l.2,and obtain a real,bounded, linear functional $L _ { 1 , R }$ for which ${ \cal L } _ { 1 , R } ( x ) = { \cal L } _ { R } ( x ) ;$ ${ \pmb x } \in { \pmb Y } _ { \pmb R }$ and for which $\| L _ { 1 , R } \| = \| L _ { R } \|$ Define

$$
L _ { 1 } ( x ) = L _ { 1 , R } ( x ) - i L _ { 1 , R } ( i x ) .
$$

By Lemma 11.1.4, $L _ { 1 }$ is a linear functional defined on the whole of $\pmb { X }$ It is an extension of $\scriptstyle { \cal L }$ For let ${ \pmb x } \in { \pmb Y }$ .Then,by (ll.1.8)(taking the $\pmb { X }$ as the present $\boldsymbol { Y }$ ，

$$
L ( x ) = L _ { R } ( x ) - i L _ { R } ( i x ) = L _ { 1 , R } ( x ) - i L _ { 1 , R } ( i x ) = L _ { 1 } ( x ) .
$$

We must finally prove that $\| L _ { 1 } \| = \| L \|$ . Since $L _ { 1 }$ is an extension of $\pmb { L }$ ,it is clear that $\| L \| \leq \| L _ { 1 } \|$ . On the other hand,suppose that $L _ { 1 } ( x ) = r e ^ { i \theta }$ $\pmb { x } \in \pmb { X }$ . Then,

$$
\begin{array} { r l } & { | L _ { 1 } ( x ) | = r = \mathrm { R e } L _ { 1 } ( e ^ { - i \theta } x ) = L _ { 1 , R } ( e ^ { - i \theta } x ) \leq \| L _ { 1 , R } \| \| e ^ { - i \theta } x \| } \\ & { \qquad = \| L _ { 1 , R } \| \| x \| = \| L _ { R } \| \| x \| \leq \| L \| \| x \| . } \end{array}
$$

The last inequality was observed after (ll.1.7).Therefore,for all ${ \pmb x } \in { \pmb X }$ ， $\frac { | L _ { 1 } ( x ) | } { \| x \| } \leq \| L \|$ ,so that $\| L _ { 1 } \| \leq \| L \|$ . Thus, $\| L _ { 1 } \| = \| L \|$

THEOREM 11.1.6．Let $\pmb { X }$ be $^ { \pmb { a } }$ normed linear space and $\pmb { Y }$ a linear subspace. Let $\pmb { x _ { 0 } } \in X$ ,but ${ \pmb x _ { 0 } } \notin Y$ and suppose that $d = \operatorname* { i n f } _ { y \in Y } \| y - x _ { 0 } \| > 0$ . Then we can find $^ { \pmb { a } }$ bounded linear functional, $\scriptstyle { \cal L }$ ,on $\pmb { X }$ such that

$$
\begin{array} { c c } { { L ( x ) = 0 } } & { { \quad x \in Y } } \\ { { } } & { { } } \\ { { L ( x _ { 0 } ) = 1 } } & { { } } \\ { { \| L \| = d ^ { - 1 } . } } & { { } } \end{array}
$$

Proof:As in Theorem l1.1.1, let $\mathbf { { \mathit { Y } } _ { 0 } }$ be the linear subspace of elements of the form $\pmb { \mathscr { x } } + \lambda \pmb { \mathscr { x } } _ { \mathbf { 0 } }$ ， $\pmb { x } \in \pmb { Y }$ .This decomposition is unique.Construct an $L$ over $\mathbf { { \mathit { Y } } _ { 0 } }$ as follows :

$$
L ( y ) = \lambda \quad { \mathrm { f o r } } \quad y = x + \lambda x _ { 0 } .
$$

In particular, $L ( { \pmb x } ) = \mathbf { 0 }$ whenever $\pmb { x } \in \pmb { Y }$ ，and $L ( x _ { 0 } ) = L ( 0 + 1 \cdot x _ { 0 } ) = 1$ Now

$$
{ \begin{array} { r l } & { \quad \displaystyle { \frac { | L ( y ) | } { \| y \| } } = \displaystyle { \frac { | \lambda | } { \| y \| } } = \displaystyle { \frac { | \lambda | } { \| x + \lambda x _ { 0 } \| } } = \displaystyle { \frac { 1 } { \left\| { \frac { x } { \lambda } } + x _ { 0 } \right\| } } = \displaystyle { \frac { 1 } { \left\| x _ { 0 } - \left( - { \frac { x } { \lambda } } \right) \right\| } } . } \\ & { \quad \mathrm { S i n c e } - \displaystyle { \frac { x } { \lambda } } \in Y , { \bigg \| } x _ { 0 } - \left( - { \frac { x } { \lambda } } \right) { \bigg \| } \geq d . } \end{array} }
$$

Hence

$$
\| L \| _ { Y _ { 0 } } = \operatorname* { s u p } _ { y \in Y _ { 0 } } \frac { | L ( y ) | } { \| y \| } \leq \frac { 1 } { d } .
$$

On the other hand,we can find a sequence of elements $\{ x _ { n } \} \in Y$ such that $\operatorname* { l i m } _ { n \to \infty } \| x _ { n } - x _ { 0 } \| = d$ Now ${ \pmb x _ { n } } - { \pmb x _ { 0 } } \in { \pmb Y _ { 0 } }$ so that

$$
| L ( x _ { n } - x _ { 0 } ) | \leq \| L \| _ { Y _ { 0 } } \| x _ { n } - x _ { 0 } \| .
$$

But $L ( x _ { n } ) = 0$ ， ${ \pmb n = 1 , 2 , \dots }$ ,and $L ( x _ { 0 } ) = 1$

Hence,

so that

$$
\begin{array} { l } { 1 \leq \| L \| _ { { Y _ { 0 } } } \| x _ { n } - x _ { 0 } \| , } \\ { 1 \leq \| L \| _ { { Y _ { 0 } } } d . } \end{array}
$$

Thefore $\Vert L \Vert _ { \textbf { \tiny { F _ { 0 } } } } \geq \frac { 1 } { d }$ and we must have

$$
\Vert L \Vert _ { Y _ { 0 } } = \frac { 1 } { d } .
$$

We now apply Theorem l1.1.5 to extend $L$ from $Y _ { \mathbf { 0 } }$ to $\pmb { X }$ with preservation of norm.

THEOREM 11.1.7 (Banach).Let $\pmb { X }$ be a normed linear space (real or complex). $\pmb { A }$ sequence of elements $\left\{ x _ { k } \right\}$ is closed if and only if it is complete.

Proof: Suppose $\left\{ x _ { k } \right\}$ is closed. Let $L \in X ^ { * }$ and suppose that $L ( x _ { k } ) = 0$ $k = 1$ ,2,.... Given any ${ \pmb x } \in { \pmb X }$ ，we may approximate $_ { x }$ arbitrarily closely by finite combinations of $x _ { k } \colon \| x - a _ { 1 } x _ { 1 } - a _ { 2 } x _ { 2 } - \cdot \cdot \cdot - a _ { n } x _ { n } \| \leq \varepsilon$ for some coefficients $\pmb { a } _ { \pmb { k } }$ Then,

$$
\begin{array} { r } { | L ( x ) | = | L ( x - a _ { 1 } x _ { 1 } - \cdot \cdot \cdot - a _ { n } x _ { n } ) | \medskip \qquad } \\ { \leq \| L \| \| x - a _ { 1 } x _ { 1 } - \cdot \cdot \cdot - a _ { n } x _ { n } \| \leq \| L \| \varepsilon . } \end{array}
$$

Allow $\varepsilon \to 0$ and obtain $L ( x ) = 0$ Since $\pmb { x }$ is arbitrary, $\mathbf { \nabla } L = \mathbf { 0 }$

Conversely, suppose that $L ( x _ { k } ) = 0 , k = 1 , 2 , . . . ,$ implies $\mathbf { \nabla } L = \mathbf { 0 }$ Let $\pmb { x _ { 0 } }$ be an element of $\pmb { X }$ and let $\boldsymbol { Y }$ be the linear subspace comprised of all finite linear combinations of $x _ { 1 } , x _ { 2 } , \ldots .$ We wish to prove $d = \operatorname* { i n f } _ { y \in Y } \| x _ { 0 } - y \| = 0$ Suppose the contrary.Then by the previous theorem，we can find an $\pmb { L }$ such that $\boldsymbol { L } ( y ) = \boldsymbol { 0 }$ ， $y \in Y$ and $L ( x _ { 0 } ) = 1$ . In particular, $L ( x _ { k } ) = 0$ ， $k =$ 1,2,....But by completeness,this implies $\mathbf { \nabla } L = 0$ and contradicts $L ( x _ { 0 } )$ $= 1$

Ex. 2. Let $\pmb { X }$ be a complete inner product space.Any $\pmb { L } \in \pmb { X } ^ { \ast }$ has the representation $\pmb { L } ( \pmb { x } ) = ( \pmb { x } , \pmb { x _ { 0 } } )$ for some ${ \pmb x } _ { \pmb 0 } \in { \pmb X }$ .Hence,the definition of completeness of $\{ x _ { k } \}$ is that $( x _ { k } , x ) = 0 , k = 1 , 2 , \ldots ,$ implies $\pmb { x } = \pmb { 0 }$ .In this case,the present theorem gives us the equivalence of $\pmb { A }$ and $\pmb { \cal E }$ of Theorem 8.9.1.

Ex. 3.Select $X = C [ a , b ] , \| f \| = \operatorname* { m a x } _ { a \leq x \leq b } \left| f ( x ) \right|$ .By Weierstrass’ Theorem, the powers $1 , x , x ^ { 2 } , \ldots$ ，are closed.For a given ${ \pmb g } ( { \pmb x } ) \in C$ the linear functional $L ( f ) ~ { \stackrel { \cdot } { = } } ~ \int _ { a } ^ { b } f ( x ) g ( x ) ~ d x \operatorname { i s } \operatorname { i n } X ^ { * } . \operatorname { H e n c e } \int _ { a } ^ { b } x ^ { n } g ( x ) ~ d x ~ = 0 , n ~ = 0 , 1 , 2 , \ldots , n - 1 .$ implies 、

Ex.4. Let $\{ \pmb { r _ { i } } \}$ be the set of all rational numbers lying in $a \leq x \leq b$ Let $\mathbf { \mathcal { S } } _ { i } ( x )$ be the step function defined by

$$
\begin{array} { r l r l } & { S _ { i } ( x ) = 1 } & & { a \le x \le r _ { i } } \\ & { S _ { i } ( x ) = 0 } & & { r _ { i } < x \le b . } \end{array}
$$

Then the system $\{  { \boldsymbol } S _ { i } (  { \boldsymbol } x ) \}$ is closed in $L ^ { 2 } [ a , b ]$ ·