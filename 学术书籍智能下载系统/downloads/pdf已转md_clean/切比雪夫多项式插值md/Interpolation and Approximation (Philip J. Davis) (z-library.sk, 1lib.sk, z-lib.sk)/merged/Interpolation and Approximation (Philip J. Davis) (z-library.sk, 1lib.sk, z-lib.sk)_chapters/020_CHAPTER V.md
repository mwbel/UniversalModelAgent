# CHAPTER V

# Some Problems of Infinite Interpolation

5.1 Characteristics of Such Problems. In Chapters 2 and 3，we considered interpolation problems with a finite number of conditions.In Chapter 4,we allowed the number of conditions to grow and,under certain favorable circumstances,we obtained solutions in the form of infinite series of polynomials.Not all problems involving an infinity of interpolating conditions can be treated in this manner,and the present chapter explores several alternate approaches.

In passing from a problem with a finite number of conditions to one with an infinity of conditions,analytic as well as algebraic difficulties arise to complicate the situation.If we look for a solution within a given class of functions,we may be unsuccessful,or we may be too successful, for the solution may not be unique.The following examples illustrate these possibilities.

Ex.1.Find a function analytic in $| z | < r$ ，for which $\begin{array} { r } { f ^ { ( n ) } ( 0 ) = ( n ! ) ^ { 2 } \quad n = } \end{array}$ 0,1,....We must have

$$
f ( z ) = \sum _ { n = 0 } ^ { \infty } \frac { 1 } { n ! } ( n ! ) ^ { 2 } z ^ { n } = \sum _ { n = 0 } ^ { \infty } n ! z ^ { n } .
$$

This series has a zero radius of convergence and so the problem has no solution. From (1.9.9),the interpolation problem $f ^ { ( n ) } ( 0 ) = a _ { n }$ has a solution analytic in $| z | < r$ if and only if $\operatorname* { l i m } _ { n \to \infty } \operatorname* { s u p } _ { n } { \frac { 1 } { n } } | a _ { n } | ^ { 1 / n } \leq { \frac { 1 } { r e } }$ .If it has a solution,the solution is unique.

Ex.2.Given a set of points $0 \leq x _ { 1 } < x _ { 2 } < \cdot \cdot \cdot < 1$ with $\operatorname* { l i m } _ { n \to \infty } x _ { n } = 1$ and a set of values $y _ { 1 } , y _ { 2 } , \ldots$ , find a function of class $C [ 0 , 1 ]$ for which $f ( x _ { i } ) = y _ { i }$ It should be clear that a necessary and sufficient condition that this interpolation problem have a solution is that $\operatorname* { l i m } _ { n \to \infty } y _ { n }$ exists. Assuming this, we may then solve the problem in an infinity of ways.

Ex.3．Find a function of class ${ \cal C } [ 0 , 1 ]$ for which

$$
\int _ { 0 } ^ { 1 } x ^ { n } f \left( x \right) d x \ = n , n \ = 0 , 1 , \ldots . . .
$$

By Theorem 1.4.2,

$$
\left| \int _ { 0 } ^ { 1 } x ^ { n } f \left( x \right) d x \right| = \left| f \left( \xi \right) \int _ { 0 } ^ { 1 } x ^ { n } d x \right| = \frac { \left| f \left( \xi \right) \right| } { n + 1 } \leq \frac { \operatorname* { m a x } _ { 0 \leq x \leq 1 } \left| f \left( x \right) \right| } { n + 1 }
$$

The sequence of moments $\int _ { 0 } ^ { 1 } x ^ { n } f \left( x \right) d x$ therefore approaches O as a limit and the interpolation problem has no solution.

5.2 Guichard's Theorem. A natural generalization of the fundamental theorem for polynomial interpolation (Theorem 2.1.1) is the following theorem of Guichard.

THEOREM 5.2.1． Let $z _ { \mathbf { 0 } } , z _ { \mathbf { 1 } } ,$ ...,be $^ { \pmb { a } }$ sequence of distinct complex numbers such that $\operatorname* { l i m } _ { n \to \infty } z _ { n } = \infty$ Let $w _ { 0 } , w _ { 1 } , \ldots$ ，be $\pmb { a }$ completely arbitrary sequence of complex values.Then there exists an entire function $f ( z )$ such that

$$
f ( z _ { n } ) = w _ { n } \qquad n = 0 , 1 , \ldots .
$$

We shall give two proofs of this theorem.The first is function-theoretic in nature and is based upon theorems of Weierstrass and Mittag-Leffer that have an interpolatory character.We shall state these theorems,but refer to standard texts on complex variable for their proofs.

THEOREM 5.2.2 (The Weierstrass Product Theorem).Let $z _ { 0 } = 0$ ， $z _ { 1 } , . . . ,$ be $\pmb { a }$ sequence of distinct complex numbers for which $\operatorname* { l i m } _ { n \to \infty } z _ { n } = \infty$ Let $\begin{array} { r } { n _ { 0 } , n _ { 1 } , \ldots . } \end{array}$ ， be a sequence of integers $\geq 1$ . Then, for an appropriate selection of integers $\pmb { p _ { k } }$ the product

$$
f ( z ) = z ^ { n _ { 0 } } \prod _ { k = 1 } ^ { \infty } \Big ( 1 - \frac { z } { z _ { k } } \Big ) ^ { n _ { k } } \Big [ \exp \Big ( \frac { z } { z _ { k } } + \frac { 1 } { 2 } \Big ( \frac { z } { z _ { k } } \Big ) ^ { 2 } + \cdot \cdot \cdot + \frac { 1 } { p _ { k } } \Big ( \frac { z } { z _ { k } } \Big ) ^ { p _ { k } } \Big ) \Big ] ^ { n _ { k } }
$$

converges for $| z | < \infty$ to an entire function that has $\pmb { a }$ zero of order $n _ { k } \mathrm { ~ } a t \mathrm { ~ } z _ { k } ,$ $k = 0 , 1 , \ldots$

THEOREM 5.2.3 (Mittag-Leffer's Partial Fraction Theorem)._Let $z _ { \mathbf { 0 } } ,$ $z _ { 1 } , . . .$ ，be $^ { \pmb { a } }$ sequence of distinct points， and let lim $z _ { n } = \infty$ For $i =$ $0 , 1 , \ldots$ ， let ${ a _ { i 1 } }$ ai2,..., $a _ { i n _ { i } }$ be given complex numbers. Then there exists $^ { \pmb { a } }$ meromorphic function having at each ${ \boldsymbol { z } } _ { i } \mathbf { \delta } \mathbf { a }$ principal part

$$
{ \frac { a _ { i , 1 } } { ( z - z _ { i } ) } } + { \frac { a _ { i , 2 } } { ( z - z _ { i } ) ^ { 2 } } } + \cdots + { \frac { a _ { i , n _ { i } } } { ( z - z _ { i } ) ^ { n _ { i } } } }
$$

and analytic everywhere else.

Proof of Theorem 5.2.1:By Theorem 5.2.2,construct a function $g ( z )$ that is entire and has simple zeros at $z _ { i } \colon g ( z _ { i } ) = 0$ and $g ^ { \prime } ( z _ { i } ) \neq 0 , i = 0 , 1 , 2 \cdots .$ By Theorem 5.2.3,construct a meromorphic function $h ( z )$ whose principal part at $z _ { i }$ is $\frac { w _ { i } } { g ^ { \prime } ( z _ { i } ) ( z - z _ { i } ) }$ and which is analytic everywhere else.Then the function $f ( z ) = g ( z ) \hbar ( z )$ solves the interpolation problem,for the zeros of $\pmb { g }$ cancel the poles of $\pmb { h }$ so that $f$ is an entire function.Moreover,in a neighborhood of $\boldsymbol { z } = \boldsymbol { z } _ { i }$ we have

$$
\begin{array} { c } { { f ( z ) = g ( z ) h ( z ) = [ g ^ { \prime } ( z _ { i } ) ( z - z _ { i } ) + \mathrm { h i g h e r ~ p o w e r s ~ o f ~ } ( z - z _ { i } ) ] } } \\ { { \qquad \times \left[ \displaystyle \frac { w _ { i } } { g ^ { \prime } ( z _ { i } ) ( z - z _ { i } ) } + r ( z ) \right] } } \end{array}
$$

where $r ( z )$ is analytic in a neighborhood of $z _ { i }$ .Hence $f ( z _ { i } ) = w _ { i }$ as required.

5.3 A Second Approach: Infinite Systems of Linear Equations in Infinitely Many Unknowns. A simple-minded approach to the problem in Theorem 5.2.1 is the following.We are looking for an entire function

for which

$$
\begin{array} { c } { { f ( z ) = a _ { 0 } + a _ { 1 } z + a _ { 2 } z ^ { 2 } + \cdots } } \\ { { \ } } \\ { { f ( z _ { i } ) = w _ { i } , \qquad i = 1 , 2 , \ldots . } } \end{array}
$$

Regard the a's of (5.3.l） as unknowns and determine them so that the conditions (5.3.2) hold. These conditions lead to

$$
\begin{array} { r } { a _ { 0 } + a _ { 1 } z _ { 1 } + a _ { 2 } z _ { 1 } { } ^ { 2 } + \dots = w _ { 1 } } \\ { a _ { 0 } + a _ { 1 } z _ { 2 } + a _ { 2 } z _ { 2 } { } ^ { 2 } + \dots = w _ { 2 } } \\ { a _ { 0 } + a _ { 1 } z _ { 3 } + a _ { 2 } z _ { 3 } { } ^ { 3 } + \dots = w _ { 3 } } \\ { . } \\ { . } \\ { . } \end{array}
$$

an infinite system of linear equations in the unknowns $a _ { 0 } , a _ { 1 } , \ldots .$ Assuming, for the moment, that we have succeeded in producing numbers ${ \pmb { a } } _ { \mathbf { 0 } } ,$ $a _ { 1 } , . . .$ ，which make the left hand of (5.3.3) converge to the right hand,it folows from the properties of power series that the series (5.3.1) converges absolutely for $| z | < | z _ { 1 } |$ ，for $| z | < | z _ { 2 } |$ ，etc.Since lim $z _ { n } = \infty$ ， $f ( z )$ will be entire and $f ( z _ { i } ) = w _ { i }$ ，The matter therefore hinges upon our ability to solve the system (5.3.3).It should be clear that infinite problems of linear interpolation theory can always be reduced to such systems.

Questions relating to the existence and uniqueness of solutions of finite systems of linear equations have been completely resolved.Not so for infinite systems.While much is known,much remains unknown.There is no all-encompassing theory,but rather many different theories that have their origins in the variety of assumptions that can be made about the growth properties of the coefficients and of the solution.We shall prove a theorem of Polya which gives a suffcient condition for the existence of a solution of an infinite system.Polya's Theorem is interesting because it has numerous applications to interpolation problems,and also because it is one of the few theorems about infinite systems in which nothing is assumed about the right-hand side.

THEOREM 5.3.l (Polya). Let there be given an infinite set of linear equations in infinitely many unknowns $x _ { 1 } , x _ { 2 } , \ldots$ ：

$$
\begin{array} { r } { a _ { 1 1 } x _ { 1 } + a _ { 1 2 } x _ { 2 } + \cdot \cdot \cdot = b _ { 1 } } \\ { a _ { 2 1 } x _ { 1 } + a _ { 2 2 } x _ { 2 } + \cdot \cdot \cdot = b _ { 2 } } \\ { \cdot \qquad \cdot \qquad \cdot } \\ { \cdot \qquad \cdot } \end{array}
$$

No assumptions are made about the b's, but as far as the a's are concerned we assume

(A)Let $\pmb q \geq 0$ and $\pmb { n } \geq 1$ be arbitrary integers. From the infinite array of coefficients

$$
\begin{array} { l } { a _ { 1 , q + 1 } = a _ { 1 , q + 2 \dots } } \\ { \cdot } \\ { \cdot } \\ { \cdot } \\ { a _ { n , q + 1 } = a _ { n , q + 2 \dots } . . . } \end{array}
$$

we may select $\pmb { n }$ columns such that the determinant formed by these columns does not vanish.

(B)For $j = 2 , 3 , \dots$ we have

$$
\operatorname* { l i m } _ { k \to \infty } { \frac { a _ { j - 1 , k } } { a _ { j k } } } = 0
$$

Under assumptions (A) and (B),we may find $^ { a }$ solution $\pmb { x } _ { i }$ to (5.3.4) with all the infinite series absolutely convergent.

A solution will be constructed in a “blockwise” fashion. This will require a preliminary description and a lemma. The first block of unknowns will be

$$
x _ { 1 } , x _ { 2 } , \ldots , x _ { q _ { 1 } } .
$$

The second block will be

$$
x _ { q _ { 1 } + 1 } , x _ { q _ { 1 } + 2 } , \ldots , x _ { q _ { 2 } } .
$$

In general, the nth block of unknowns will be

$$
x _ { a _ { n - 1 } + 1 } , x _ { q _ { n - 1 } + 2 } , \ldots , x _ { q _ { n } } .
$$

The numbers $\pmb { q } _ { i }$ are certain integers satisfying $1 \leq q _ { 1 } < q _ { 2 } < \cdots$ ,and will be specified precisely in the proof below.

The first block of unknowns will be assumed to satisfy

$$
a _ { 1 1 } x _ { 1 } + a _ { 1 2 } x _ { 2 } + \cdot \cdot \cdot + a _ { 1 , q _ { 1 } } x _ { q _ { 1 } } = b _ { 1 }
$$

The second block will be assumed to satisfy

$$
\begin{array} { c } { a _ { 1 , q _ { 1 } + 1 } x _ { q _ { 1 } + 1 } + a _ { 1 , q _ { 1 } + 2 } x _ { q _ { 1 } + 2 } + \cdot \cdot \cdot + a _ { 1 , q _ { 2 } } x _ { q _ { 2 } } = 0 } \\ { a _ { 2 , q _ { 1 } + 1 } x _ { q _ { 1 } + 1 } + a _ { 2 , q _ { 1 } + 2 } x _ { q _ { 1 } + 2 } + \cdot \cdot \cdot + a _ { 2 , q _ { 2 } } x _ { q _ { 2 } } } \\ { = b _ { 2 } - ( a _ { 2 1 } x _ { 1 } + a _ { 2 2 } x _ { 2 } + \cdot \cdot \cdot + a _ { 2 , q _ { 1 } } x _ { q _ { 1 } } ) } \end{array}
$$

By adding (5.3.10)to (5.3.l1), we see that the first two blocks satisfy

$$
\begin{array} { r } { a _ { 1 1 } x _ { 1 } + \cdots + a _ { 1 , q _ { 2 } } x _ { q _ { 2 } } = b _ { 1 } } \\ { a _ { 2 1 } x _ { 1 } + \cdots + a _ { 2 , q _ { 2 } } x _ { q _ { 2 } } = b _ { 2 } } \end{array}
$$

In general, the nth block will be assumed to satisfy

$$
\begin{array} { r l r } {  { a _ { n - 1 , q _ { n - 1 } + 1 } x _ { q _ { n - 1 } + 1 } + \dots + a _ { n - 1 , q _ { n } } x _ { q _ { n } } = 0 } } \\ & { } & \\ & { } & { a _ { n , q _ { n - 1 } + 1 } x _ { q _ { n - 1 } + 1 } + \dots + a _ { n , q _ { n } } x _ { q _ { n } } \qquad } \\ & { } & \\ & { } & { = b _ { n } - ( a _ { n , 1 } x _ { 1 } + a _ { n , 2 } x _ { 2 } + \dots + a _ { n , q _ { n - 1 } } x _ { q _ { n - 1 } } ) = b _ { n } , } \end{array}
$$

By addition, the frst $\pmb { n }$ blocks of unknowns will satisfy the $\pmb { n }$ conditions

$$
\begin{array} { r } { a _ { 1 1 } x _ { 1 } + a _ { 1 2 } x _ { 2 } + \cdots + a _ { 1 , a _ { n } } x _ { a _ { n } } = b _ { 1 } } \\ { ~ \cdot } \\ { ~ \cdot } \\ { ~ \cdot } \end{array}
$$

$$
a _ { n 1 } x _ { 1 } + a _ { n 2 } x _ { 2 } + \cdot \cdot \cdot + a _ { n , q _ { n } } x _ { q _ { n } } = b _ { n }
$$

But,in order to provide absolute convergence，we need more.We shall require that (5.3.l3) be solved subject to the condition that the terms of the first ${ \pmb n } - { \bf l }$ of its left-hand members be uniformly small in absolute value.

LEMMA 5.3.2. Let $\pmb { n }$ and $\pmb q$ be positive integers. Let b be arbitrary and $\varepsilon > 0$ .Under conditions (A) and (B) of Theorem 5.3.l,we can find an integer $q ^ { \prime } > q$ and values $x _ { q + 1 } , x _ { q + 2 } , \ldots , x _ { q ^ { \prime } }$ such that

$$
\begin{array} { r l r l } { a _ { 1 , q + 1 } x _ { q + 1 } } & { { } + a _ { 1 , q + 2 } x _ { q + 2 } } & { + \cdot \cdot \cdot + a _ { 1 , q } . x _ { q ^ { \prime } } } & { = 0 } \end{array}
$$

$$
\begin{array} { r } { a _ { n - 1 , q + 1 } x _ { q + 1 } + a _ { n - 1 , q + 2 } x _ { q + 2 } + \cdot \cdot \cdot + a _ { n - 1 , q } , x _ { q ^ { \prime } } = 0 } \\ { \qquad \quad a _ { n , q + 1 } x _ { q + 1 } + a _ { n , q + 2 } x _ { q + 2 } \quad + \cdot \cdot \cdot + a _ { n , q ^ { \prime } } x _ { q ^ { \prime } } = b } \end{array}
$$

and such that

$$
\begin{array} { r l r } { | a _ { 1 , q + 1 } x _ { q + 1 } | } & { + \cdot \cdot \cdot + | a _ { 1 , q } , x _ { q ^ { \prime } } | } & { < \varepsilon } \\ { \cdot } & { \cdot } & \\ { \cdot } & { \cdot } & \\ { \cdot } & { \cdot } & \\ { | a _ { n - 1 , q + 1 } x _ { q + 1 } | + \cdot \cdot \cdot + | a _ { n - 1 , q ^ { \prime } } x _ { q ^ { \prime } } | < \varepsilon . } \end{array}
$$

Proof: Let $t _ { 1 } , \ldots , t _ { n }$ be $\pmb { n }$ independent variables.In view of condition (A),we can select $\pmb { n }$ integers $k _ { 1 } , k _ { 2 } , \ldots , k _ { n }$ with $q < k _ { 1 } < k _ { 2 } < \cdots < k _ { n }$ in such a fashion that the determinant of the system

$$
\begin{array} { r } { a _ { 1 k _ { 1 } } x _ { k _ { 1 } } + a _ { 1 k _ { 2 } } x _ { k _ { 2 } } + \cdot \cdot \cdot + a _ { 1 k _ { n } } x _ { k _ { n } } = t _ { 1 } } \\ { . } \\ { . } \end{array}
$$

$$
a _ { n k _ { 1 } } x _ { k _ { 1 } } + a _ { n k _ { 2 } } x _ { k _ { 2 } } + \cdot \cdot \cdot + a _ { n k _ { n } } x _ { k _ { n } } = t _ { n }
$$

does not vanish.The $\pmb { x } ^ { \mathrm { i } }$ s may therefore be solved as certain linear combinations of the t's.Hence,for the t's sufficiently small, the $\pmb { x }$ s will also be small. More than this,we may find a $\delta > 0$ such that $| t _ { i } | < \delta , i = 1 , 2 , \ldots , n$ implies

$$
| a _ { j k _ { 1 } } x _ { k _ { 1 } } | + | a _ { j k _ { 2 } } x _ { k _ { 2 } } | + \cdot \cdot \cdot + | a _ { j k _ { n } } x _ { k _ { n } } | < \frac { \varepsilon } { 2 } \ ; j = 1 , 2 , \ldots , n .
$$

Now in view of condition (B),we can determine an integer $q ^ { \prime } > k _ { n }$ such that

$$
| b | \left| \frac { a _ { j q ^ { \prime } } } { a _ { n q ^ { \prime } } } \right| < \operatorname* { m i n } \left( \delta , \varepsilon / 2 \right) \mathrm { f o r } j = 1 , 2 , \ldots , n - 1 .
$$

Now, set $\boldsymbol { x } _ { k } = 0$ if $q < k < q ^ { \prime }$ and $k \neq k _ { 1 } , ~ k _ { 2 } , \ldots , k _ { n }$ Determine $\boldsymbol { x } _ { k _ { 1 } } ,$ Xkz,..., xxn from the system (5.3.17) wherein we have set

$$
\begin{array} { r l } { \bigg \{ t _ { j } = - \frac { b a _ { j q ^ { \prime } } } { a _ { n q ^ { \prime } } } \qquad } & { { } j = 1 , 2 , \dots , n - 1 } \\ { t _ { n } = 0 . } \end{array}
$$

In view of (5.3.19) and (5.3.20), we have $| t _ { j } | < \delta$ for $j = 1 , 2 , \dots , n$ and hence (5.3.18) holds.If we set

$$
x _ { q ^ { \prime } } = \frac { b } { a _ { n q ^ { \prime } } } \mathrm { t h e n } | a _ { j q ^ { \prime } } x _ { q ^ { \prime } } | = \left| \frac { a _ { j q ^ { \prime } } } { a _ { n q ^ { \prime } } } \right| | b | < \frac { \varepsilon } { 2 }
$$

by (5.3.19).

Finally,

a

$$
\begin{array} { r l } & { a _ { j , a + 1 } x _ { a + 1 } + a _ { j , a + 2 } x _ { a + 2 } + \cdot \cdot \cdot + a _ { j , a } x _ { a } } \\ & { \qquad = a _ { j k _ { 1 } } x _ { k _ { 1 } } + a _ { j k _ { 2 } } x _ { k _ { 2 } } + \cdot \cdot \cdot + a _ { j k _ { 1 } } x _ { k _ { 1 } } + a _ { j \cdot } \frac { b } { a _ { j \cdot } } = t _ { j } - t _ { j } = 0 } \\ & { \qquad j = 1 , 2 , \ldots , n - 1 } \\ & { \qquad \mathrm { ~ a d } } \\ & { a _ { n , a + 1 } x _ { a + 1 } + a _ { n , a + 2 } x _ { a + 2 } + \cdot \cdot \cdot + a _ { n \cdot 2 } x _ { a ^ { \prime } } = a _ { n k _ { 1 } } x _ { k _ { 1 } } + a _ { n k _ { 2 } } x _ { k _ { 2 } } + \cdot \cdot \cdot } \\ & { \qquad \quad \quad + a _ { n k _ { 1 } } x _ { k _ { 1 } } + a _ { n \cdot 2 } \frac { b } { a _ { \cdot \cdot \cdot } } = t _ { n } + b = b } \end{array}
$$

Thus, if $\pmb { x } _ { q + 1 } , \ldots , \pmb { x } _ { q ^ { \prime } }$ have been selected in the above manner,all the required conditions are fulfilled.

Proof of Theorem 5.3.1:We begin by dividing the unknowns into blocks in an inductive fashion.In view of condition (A),the sequence $a _ { 1 1 } , a _ { 1 2 } , \ldots ,$ must contain infinitely many nonzero elements.Determine ${ \pmb q _ { 1 } }$ such that $a _ { 1 q _ { 1 } } \neq 0$ Now set ${ \pmb x _ { 1 } } = { \bf 0 }$ ， $x _ { 2 } = 0 , \ldots , x _ { q _ { 1 } - 1 } = 0 , x _ { q _ { 1 } } = b _ { 1 } / a _ { 1 q _ { 1 } }$ . Conditions (5.3.10) imposed on the first block are satisfied. Suppose now that we have obtained integers

where $\mathscr { n } \geq 2$ .We take the next step as follows.Use Lemma 5.3.2 with $q = q _ { n - 1 } , \ b = b _ { n } ^ { \prime }$ (Cf.(5.3.13)） and determine $q ^ { \prime } = q _ { n }$ and the values of the $\pmb { n }$ th block of unknowns, $x _ { q _ { n - 1 } + 1 } , \ldots , x _ { q _ { n } }$ so that (5.3.15) is satisfed and so that

$$
| a _ { j q _ { n - 1 } + 1 } x _ { q _ { n - 1 } + 1 } | + \cdot \cdot \cdot + | a _ { j q _ { n } } x _ { q _ { n } } | \leq { \frac { 1 } { 2 ^ { n } } } , 1 \leq j < n
$$

.., (5.3.16) with $\varepsilon = { \frac { 1 } { 2 ^ { n } } }$ . Note that ${ b _ { n } } ^ { \prime }$ involves only the values $x _ { 1 } , \ldots ,$ xan-1 so that this step may be taken.This completes the inductive definition.

In view of (5.3.l3), it is easy to see that $x _ { 1 } , x _ { 2 } , \ldots .$ ,satisfy the original system (5.3.4)-at least in a blockwise fashion.Let $j$ be fixed,i.e.,consider a fixed row. As soon as $\pmb { n } > j$ ，(5.3.21) holds,and this tellsus that the jth row must be absolutely convergent.From (5.3.l4),we see that when $\pmb { n } \geq j$ ， the jth row has partial sums $a _ { j 1 } x _ { 1 } + \cdots + a _ { j q _ { n } } x _ { q _ { n } } = b _ { j } ,$ for the infinite sequence of indices $q _ { n } , q _ { n + 1 } , \ldots$ Since $\sum _ { i = 1 } ^ { \infty } a _ { j k } x _ { k }$ converges, it follows that $\sum _ { k = 1 } ^ { \infty } a _ { j k } x _ { k } = b _ { j }$ This completes the proof.

It should be emphasized that nothing has been said about the uniqueness of the solution.Quite the contrary.Under these conditions,there must be an infinity of solutions. (See Prob.7.)

5.4 Applications of P6lya's Theorem. Theorem 5.3.l will now be applied to give a proof of a theorem similar to Theorem 5.2.1.

THEOREM 5.4.1. Let 21, 2,... , satisfy $0 < | z _ { 1 } | < | z _ { 2 } | < \cdots , \operatorname* { l i m } _ { n \to \infty } | z _ { n } | =$ $\rho \leq \infty$ . To each point $z _ { j }$ associate $^ { \pmb { a } }$ nonnegative integer $\mathbf { \nabla } m _ { j }$ and $m _ { j } + 1$ arbitrary values $w _ { j } ^ { 0 } , w _ { j } ^ { 1 } , \ldots , w _ { j } ^ { m _ { j } }$ . Then we can find $\pmb { a }$ function $f ( z )$ that is analytic in $| z | < \rho$ and satisfies the interpolation conditions:

$$
f ( z _ { j } ) = w _ { j } ^ { 0 } , f ^ { \prime } ( z _ { j } ) = w _ { j } ^ { 1 } , . . . , f ^ { ( m _ { j } ) } ( z _ { j } ) = w _ { j } ^ { m _ { j } } \quad j = 1 , 2 , . . . . ,
$$

Proof: Assuming we have $f ( z ) = \sum _ { k = 0 } ^ { \infty } a _ { k } z ^ { k }$ ，with ${ \pmb a } _ { \pmb k }$ to be determined，we have for $\pmb { \mathscr { s } } \geq 1$ ，

$$
f ^ { ( s ) } ( z ) = \sum _ { k = 0 } ^ { \infty } a _ { k } k ( k - 1 ) \cdot \cdot \cdot ( k - s + 1 ) z ^ { k - s } .
$$

The conditions (5.4.1) therefore lead to the infinite system

$$
\begin{array} { r l r } & { } & { a _ { 0 } + z _ { 1 } a _ { 1 } + z _ { 1 } { } ^ { 2 } a _ { 2 } + z _ { 1 } { } ^ { 3 } a _ { 3 } + \cdot \cdot \cdot = w _ { 1 } { } ^ { 0 } } \\ & { } & { a _ { 1 } + 2 z _ { 1 } a _ { 2 } + 3 z _ { 1 } { } ^ { 2 } a _ { 3 } + \cdot \cdot \cdot = w _ { 1 } { } ^ { 1 } } \\ & { } & { 2 a _ { 2 } + 6 z _ { 1 } a _ { 3 } + \cdot \cdot \cdot = w _ { 1 } { } ^ { 2 } } \end{array}
$$

$$
\begin{array} { r l r } & { } & { ( m _ { j } ) ! a _ { m _ { j } } + \cdot \cdot \cdot = w _ { 1 } ^ { \textrm { \tiny { m } } _ { j } } } \\ & { } & { a _ { 0 } + z _ { 2 } a _ { 1 } + z _ { 2 } { } ^ { 2 } a _ { 2 } + z _ { 2 } { } ^ { 3 } a _ { 3 } + \cdot \cdot \cdot = w _ { 2 } { } ^ { 0 } } \\ & { } & { a _ { 1 } + 2 z _ { 2 } + 3 z _ { 2 } { } ^ { 2 } a _ { 3 } + \cdot \cdot \cdot = w _ { 2 } { } ^ { 1 } } \\ & { } & { . } \\ & { } & { . } & { . } \\ & { } & { . } & { . } \end{array}
$$

Now condition (B),(5.3.6) is satisfied.For if the jth row refers to an sth derivative at $z _ { p } , s \geq 1$ ,we have from (5.4.2)

$$
{ \frac { a _ { j - 1 , k + 1 } } { a _ { j , k + 1 } } } = { \frac { z _ { p } k ( k - 1 ) \cdot \cdot \cdot ( k - s + 2 ) } { k ( k - 1 ) \cdot \cdot \cdot ( k - s + 1 ) } } = { \frac { z _ { p } } { k - s + 1 } } \to 0 .
$$

However,if the jth row relates to a value of $f$ at a point,then the condition $| z _ { p - 1 } | < | z _ { p } |$ assures that the limit of $a _ { j - 1 , k } / a _ { j , k }$ is zero.Consider the coeffcients arising from the system (5.4.3).We shall prove that the determinant formed from the first $\pmb { n }$ rows and any $\pmb { n }$ adjacent columns cannot vanish. This will tell us that condition (A) is fulfilled.These determinants may be thought of as generalized Vandermonde determinants.To avoid losing the thread of the argument in a welter of indices,look at the specific case $\textbf { \em n } =$ 4, $m _ { 1 } = 2$ The $4 \times 4$ determinant formed from the first 4 rows and 4 adjacent columns is

$$
) = | \begin{array} { c c c c c } { { z _ { 1 } ^ { k } } } & { { z _ { 1 } ^ { k + 1 } } } & { { z _ { 1 } ^ { k + 2 } } } & { { z _ { 1 } ^ { k + 3 } } } & { { z _ { 1 } ^ { k + 3 } } } \\ { { k z _ { 1 } ^ { k - 1 } } } & { { ( k + 1 ) z _ { 1 } ^ { k } } } & { { ( k + 2 ) z _ { 1 } ^ { k + 1 } } } & { { ( k + 3 ) z _ { 1 } ^ { k + 2 } } } & { { } } \\ { { k ( k - 1 ) z _ { 1 } ^ { k - 2 } } } & { { ( k + 1 ) k z _ { 1 } ^ { k - 1 } } } & { { ( k + 2 ) ( k + 1 ) z _ { 1 } ^ { k } } } & { { ( k + 3 ) ( k + 2 ) z _ { 1 } ^ { k + 1 } } } & { {  } } \\ { { z _ { 2 } ^ { k } } } & { { z _ { 2 } ^ { k + 1 } } } & { { z _ { 2 } ^ { k + 2 } } } & { { z _ { 2 } ^ { k + 3 } } } & { { z _ { 2 } ^ { k + 3 } } } \end{array} |
$$

Form the related system of linear homogeneous equations in 4 unknowns $v _ { 1 } , \ldots , v _ { 4 }$ ：

$$
\begin{array} { r l r } & { } & { z _ { 1 } { ^ { k } } v _ { 1 } + z _ { 1 } ^ { k + 1 } v _ { 2 } + z _ { 1 } ^ { k + 2 } v _ { 3 } + z _ { 1 } ^ { k + 3 } v _ { 4 } = 0 } \\ & { } & { k z _ { 1 } ^ { k - 1 } v _ { 1 } + ( k + 1 ) z _ { 1 } { ^ { k } } v _ { 2 } + ( k + 2 ) z _ { 1 } ^ { k + 1 } v _ { 3 } + ( k + 3 ) z _ { 1 } ^ { k + 2 } v _ { 4 } = 0 } \\ & { } & { k ( k - 1 ) z _ { 1 } ^ { k - 2 } v _ { 1 } + ( k + 1 ) k z _ { 1 } ^ { k - 1 } v _ { 2 } \qquad } \\ & { } & { + ( k + 2 ) ( k + 1 ) z _ { 1 } { ^ { k } } v _ { 3 } + ( k + 3 ) ( k + 2 ) z _ { 1 } ^ { k + 1 } v _ { 4 } = 0 } \\ & { } & { z _ { 2 } { ^ { k } } v _ { 1 } + z _ { 2 } ^ { k + 1 } v _ { 2 } + z _ { 2 } ^ { k + 2 } v _ { 3 } + z _ { 2 } ^ { k + 3 } v _ { 4 } = 0 } \end{array}
$$

If $\pmb { D } = 0$ ,then by Theorem 1.2.2,we can find $v _ { 1 } , \ldots , v _ { 4 }$ , not all zero, satisfying (5.4.5).With these values,form the polynomial

$$
P ( z ) = v _ { 1 } z ^ { k } + v _ { 2 } z ^ { k + 1 } + v _ { 3 } z ^ { k + 2 } + v _ { 4 } z ^ { k + 3 } .
$$

$P$ is of degree $\leq k + 3$ and does not vanish identically. It has a $\pmb { k }$ -fold zero at $z = 0$ and in view of (5.4.5),a 3-fold zero at $z _ { 1 }$ and a zero at $z _ { 2 }$ That is, it has zeros of total multiplicity $k + 4$ .This is impossible,and hence $\boldsymbol { D } \neq$ O.(Cf.the argument used in 2.3,Ex. 6.)

We now employ Theorem 5.3.l and obtain values ${ a _ { 0 } } , { a _ { 1 } } , \ldots$ ,for which (5.4.3) holds,all series being absolutely convergent.Since,in particular, $\sum _ { k = 0 } ^ { \infty } a _ { k } | z _ { j } | ^ { k } < \infty , f ( z ) = \sum _ { k = 0 } ^ { \infty } a _ { k } z ^ { k }$ is convergent in $| z | < \rho$ and the formal work of (5.4.3) is valid.

Can one construct an analytic function whose derivatives at a point have been prescribed in advance? Ex.1 of 5.l shows that this is not always possible if the point is interior to the region of analyticity.But,by moving the point to the boundary of this region,it becomes possible.

THEOREM 5.4.2 (Borel). Given an arbitrary sequence of real numbers $\begin{array} { r } { m _ { 0 } , m _ { 1 } , \ldots . } \end{array}$ , we can find $\pmb { a }$ function which is analytic in (-l,1) and for which

Proof: Write, te $\begin{array} { r l } & { \underset { x  1 } { \operatorname* { l i m } } f ^ { ( n ) } ( x ) = m _ { n } , n = 0 , 1 , . . . . } \\ & { \mathrm { , n t a t i v e l y , } f ( x ) = \displaystyle \sum _ { n = 0 } ^ { \infty } a _ { n } x ^ { n } , f ^ { \prime } ( x ) = \displaystyle \sum _ { n = 0 } ^ { \infty } n a _ { n } x ^ { n - 1 } } \end{array}$ ,etc. On the basis of these assumed expansions,set up the following infinite system of linear equations for $a _ { 0 } , a _ { 1 } , \ldots .$

$$
\begin{array} { r l r } & { } & { a _ { 0 } + a _ { 1 } + a _ { 2 } + \cdot \cdot \cdot = m _ { 0 } } \\ & { } & { a _ { 1 } + 2 a _ { 2 } + 3 a _ { 3 } + \cdot \cdot \cdot = m _ { 1 } } \\ & { } & { 2 a _ { 2 } + 6 a _ { 3 } + \cdot \cdot \cdot = m _ { 2 } } \\ & { } & { . } \\ & { } & { . } \end{array}
$$

A typical column of coefficients of this system is $1 , k , k ( k - 1 ) , k ( k - 1 ) \times$ $( k - 2 ) , \ldots$ ,so that condition (B) of Theorem 5.3.1 is immediate.Consider, next,any $\textit { \textbf { n } } \times \textit { \textbf { n } }$ determinant formed from the first $\pmb { n }$ rows of the coefficient matrix of (5.4.7).By the addition of appropriate linear combinations of the rows,it may be converted into a determinant whose typical column is $1 , k , \dotsc , k ^ { n - 1 }$ . This is a Vandermonde and does not vanish. Condition (A) of Theorem 5.3.l is satisfied,and we can find numbers $a _ { 0 } , a _ { 1 } , \ldots$ , for which all the series in (5.4.7) converge to the right-hand side.

Form $f ( x ) = \sum _ { n = 0 } ^ { \infty } a _ { n } x ^ { n }$ . By the first equation of (5.4.7), $f ( x )$ is analytic in $| x | < 1$ .By Abel's Theorem (see e.g., Titchmarsh,[1]p. 229) $\operatorname* { l i m } _ { x  1 } f ( x ) = m _ { 0 } .$ Moreover, $f ^ { \prime } ( x ) = \sum _ { n = 0 } ^ { \infty } n a _ { n } x ^ { n - 1 }$ ， $| x | < 1$ . In view of the second equation of (5.4.7) and Abel's Theorem, $\operatorname* { l i m } _ { x  1 } f ^ { \prime } ( x ) = m _ { 1 }$ .In this way,we can establish that (5.4.6) holds generally.

# NOTES ON CHAPTER V

5.3-5.4 G.P6lya [1]. R.G. Cooke [l]. Theorems 5.4.l and 5.4.2 have attracted wide attention and many proofs and generalizations can be found. See,e.g.,P6lya [2],Ritt [1],Franklin [1].

# PROBLEMS

1. Given $0 \leq x _ { 1 } < x _ { 2 } < \cdot \cdot \cdot < 1 , \operatorname* { l i m } _ { n \to \infty } x _ { n } = 1$ Find necessary and sufficient conditions on ${ a } _ { n }$ in order that the problem $f ( { \pmb x } _ { n } ) = { \pmb a } _ { n }$ ${ \pmb n = 1 , 2 , \dots }$ ,have a solution $f ( x )$ that is differentiable in $0 \leq x \leq 1$

2.Construct a function ${ f } \left( x \right)$ that satisfies

$$
x f ( x ) ^ { \cdot } = f ( x + 1 ) , \quad 0 < x < \infty , \quad f ( n ) = \Gamma ( n ) , \ : \ : \ : n = 1 , 2 , \ldots ,
$$

is convex for $0 < x < \infty$ ,but is not $\Gamma ( x )$

3. The function $f ( z ) = e ^ { 1 / ( z + i ) } - 1$ has an infinity of zeros in $| z | < 1$ .Does this contradict the uniqueness principle for analytic functions?

4.Prove the following generalization of the Lagrange interpolation formula. Let $z _ { 0 } , z _ { 1 } , \dots , ( \neq 0 )$ be distinct points with lim $z _ { n } ~ = ~ \infty$ . Let $w ( z )$ be an entire function with simple zeros at $z _ { 0 } , z _ { 1 } , \dots .$ If n→8

$$
\sum _ { k = 0 } ^ { \infty } \left| \frac { a _ { k } } { z _ { k } w ^ { \prime } ( z _ { k } ) } \right| < \infty ,
$$

then

$$
\sum _ { k = 0 } ^ { \infty } { \frac { a _ { k } w ( z ) } { w ^ { \prime } ( z _ { k } ) ( z \ - \ z _ { k } ) } }
$$

converges absolutely and uniformly in every $| z | \leq R$ to an entire function $f ( z )$ for which $f ( z _ { k } ) = a _ { k } , k = 0 , 1 , . . .$

5.Specialize the result of the previous exercise by writing ${ \pmb w } ( { \pmb z } ) = { \sin { \pmb z } }$ and obtain a theorem for the cardinal series.

6. Let $M ( r )$ be an arbitrary positive function $0 \leq r < \infty$ . We can find an entire function $f ( z )$ such that $\operatorname* { m a x } _ { 0 \le \theta \le 2 \pi } \left| f ( r e ^ { i \theta } ) \right| \ge M ( r ) , 0 \le r < \infty$ In other words,we can find an entire function whose growth is uniformly arbitrarily rapid. Hint: write $f ( z ) = a _ { 0 } + \sum _ { k = 1 } ^ { \infty } a _ { k } \left( \frac { z } { k } \right) ^ { \lambda _ { k } }$ and select ${ \pmb a } _ { { \pmb k } }$ and $\lambda _ { k }$ sufficiently large. (Poincaré.)

7. Lt thgayseo $\sum _ { i = 1 } ^ { \infty } a _ { j k } x _ { k } = b _ { j } , j = 1 , 2 , . . .$

5.3.1. For any $\textbf { \textit { m } } > 0$ , show that we may obtain a solution with $x _ { 1 } , x _ { 2 } , \ldots , x _ { m }$ prescribed arbitrarily,and hence there is an infinity of solutions.

8. Suppose that $f ( z ) = \sum _ { n = 0 } ^ { \infty } a _ { n } z ^ { n }$ converges at $z = 1$ . Show that $f ( 1 ) = 1$ ， $f \left( { \frac { 1 } { 2 } } \right) = f \left( { \frac { 2 } { 3 } } \right) = \cdots = f \left( { \frac { n } { n + 1 } } \right) = \cdot \cdot \cdot = 0$ is impossible.Hence in Theorem 5.3.1 condition (A) cannot itself guarantee the existence of a solution.

9.Let $m _ { 0 } , m _ { 1 } , \ldots$ ，be an arbitrary sequence of real numbers. Show there exists a function $\pmb { f }$ of class $C ^ { \infty } [ - 1 , 1 ]$ for which $f ^ { ( n ) } ( 0 ) = m _ { n } \quad n = 0 , 1 , \ldots .$

10. Let $z _ { n }$ be distinct complex numbers with $\operatorname* { l i m } _ { n \to \infty } z _ { n } = \infty$ .If $\pmb { c _ { n } }$ is completely arbitrary,we can find an entire function $f ( z )$ such that

$$
\int _ { z _ { n } } ^ { z _ { n + 1 } } f ( z ) d z = c _ { n } \qquad n = 0 , 1 , \ldots .
$$

11.Use a theorem on infinite interpolation to construct a function that is analytic in $| z | < 1$ and has $| z | = 1$ as a natural boundary.

12. Let $x _ { 1 } , x _ { 2 } , \ldots$ ， be distinct real numbers that satisfy lim $x _ { n } = \infty$ .If $m _ { 0 } , m _ { 1 } , \ldots$ are completely arbitrary real numbers, we can find $u _ { 0 } , u _ { 1 } , \dotsc ,$ such that $\sum _ { i = 1 } ^ { \infty } u _ { i } x _ { i } { } ^ { n } = m _ { n }$ $n = 0 , 1 , \ldots$ ，eacherescovergingbutely.

(R. P. Boas, $\mathbf { J r }$ ）

13. The problems of Theorems 5.4.1 and 5.4.2 have an infinity of solutions.

14.There is no entire function that satisfies

$$
f ( 1 ) = 1 , f ( - 1 ) = 0 , f ^ { ( 2 n + 1 ) } ( 0 ) = 0 n = 0 , 1 , \ldots .
$$

15.Construct a function of class $C ^ { \infty }$ that satisfies the conditions of Prob.14.

# CHAPTERVI

# Uniform Approximation

6.1 The Weierstrass Approximation Theorem. We come now to the 2nd fundamental theorem of this book,the Weierstrass approximation theorem of1885.

![](../chunks/Interpolation and Approximation (Philip J. Davis) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/84e87fa420c7435637a8e1528f4860d7a07a56a43b5bb2e2a7134200727fa57e.jpg)  
Figure 6.1.1.

THEOREM 6.1.1. $L e t f ( x ) \in C [ a , b ]$ . Given an $\varepsilon > 0$ we can find a polynomial $\scriptstyle { \pmb { p } } _ { \pmb { n } } ( x )$ (of sufficiently high degree) for which

$$
| f ( x ) - p _ { n } ( x ) | \leq \varepsilon , \ a \leq x \leq b .
$$

Weierstrass theorem asserts the possibility of uniform approximation by polynomials to continuous functions over a closed interval.

It is instructive to contrast this theorem with Taylor's theorem for analytic functions for the two are often confounded. Suppose that $f ( z )$ is analytic in the cirele $| z | \leq R$ . Then we have $f ( z ) = \sum _ { k = 0 } ^ { \infty } a _ { k } z ^ { k }$ , convergent uniformly in $| z | \leq R$ .Hence it is clear that given an $\varepsilon > 0$ ，we can take sufficiently many terms of this power series and arrive at a polynomial $p _ { n } ( z ) = \sum _ { k = 0 } ^ { n } a _ { k } z ^ { k }$ for which $| f ( z ) - p _ { n } ( z ) | \leq \varepsilon$ for $| z | \leq R$ ．A fortiori,on the real segment $- R \leq x \leq R$ we have $| f ( x ) - p _ { n } ( x ) | \leq \varepsilon$ 、But for functions that are not analytic,there is no expansion in power series.Yet Weierstrass’ theorem assures us we can approximate uniformly functions which are merely continuous. Given a sequence $\varepsilon _ { 1 } , \varepsilon _ { 2 } , . . . . 0$ , we can find polynomials

$$
\begin{array} { c } { { p _ { n _ { 1 } } ( x ) = a _ { 0 n _ { 1 } } + a _ { 1 n _ { 1 } } x + \cdot \cdot \cdot + a _ { n _ { 1 } n _ { 1 } } x ^ { n _ { 1 } } } } \\ { { p _ { n _ { 2 } } ( x ) = a _ { 0 n _ { 2 } } + a _ { 1 n _ { 2 } } x + \cdot \cdot \cdot + a _ { n _ { 2 } n _ { 2 } } x ^ { n _ { 2 } } } } \\ { { . } } \\ { { . } } \\ { { . } } \end{array}
$$

for which $| f ( x ) - p _ { n _ { k } } ( x ) | \leq \varepsilon _ { k } , - R \leq x \leq R _ { \mathrm { \varepsilon } }$ $k = 1$ ,2,.... Consequently $\operatorname* { l i m } _ { k \to \infty } p _ { n _ { k } } ( x ) = f ( x )$ uniformly in $- R \leq x \leq R$

From approximations, it is simple enough to go to expansions,for we can write the‘collapsing”series

$$
f ( x ) = p _ { n _ { 1 } } ( x ) + ( p _ { n _ { 2 } } ( x ) - p _ { n _ { 1 } } ( x ) ) + ( p _ { n _ { 3 } } ( x ) - p _ { n _ { 2 } } ( x ) ) + \cdot \cdot \cdot
$$

which，evidently，converges to $f ( x )$ uniformly on $- R \leq x \leq R$ Thus, briefly,an analytic function can be expanded in a uniformly convergent power series,and a continuous but nonanalytic function can be expanded in a uniformly convergent series of general polynomials,with no possibility of rearranging its terms so as to produce a convergent power series.

6.2 The Bernstein Polynomials. There are many proofs of the Weierstrass theorem,and we shall present S.Bernstein's proof.While it is not the simplest conceptually,it is easily the most elegant.

DEFINITION 6.2.1． Let $\pmb { f } ( \pmb { x } )$ be defined on [0,1].The nth $( n \geq 1 )$ Bernstein polynomial for $f ( x )$ is given by

$$
B _ { n } ( f ; x ) = \sum _ { k = 0 } ^ { n } f \left( { \frac { k } { n } } \right) { \binom { n } { k } } x ^ { k } ( 1 - x ) ^ { n - k } .
$$

Notice that

$$
B _ { n } ( f ; 0 ) = f ( 0 ) \quad B _ { n } ( f ; 1 ) = f ( 1 ) .
$$

It is clear that $B _ { n } \in \mathcal { P } _ { n }$ .In certain cases,it may degenerate and become a polynomial of degree lower than $\pmb { n }$

THEOREM 6.2.1.

$$
B _ { n } ( f ; x ) = \sum _ { t = 0 } ^ { n } \Delta ^ { t } f ( 0 ) { \binom { n } { t } } x ^ { t }
$$

where the differences have been computed from the functional values at $0 / n , 1 / n , \ldots , ( n - 1 ) / n , n / n .$

$$
\begin{array} { l } { { P r o o f : B _ { n } ( f ; x ) = \displaystyle \sum _ { k = 0 } ^ { n } f \left( \frac { k } { n } \right) \binom { n } { k } x ^ { k } ( 1 - x ) ^ { n - k } } } \\ { { = \displaystyle \sum _ { k = 0 } ^ { n } f \left( \frac { k } { n } \right) \binom { n } { k } x ^ { k } \sum _ { j = 0 } ^ { n - k } \binom { n - k } { j } ( - 1 ) ^ { n - k - j } x ^ { n - k - j } } } \\ { { = \displaystyle \sum _ { k = 0 } ^ { n } \sum _ { j = 0 } ^ { n - k } f \left( \frac { k } { n } \right) \binom { n } { k } \binom { n } { j } \binom { n - k } { j } ( - 1 ) ^ { n - k - j } x ^ { n - j } . } } \end{array}
$$

Rearranging the summation, we obtain

$$
\begin{array} { r l } & { \displaystyle \sum _ { t = 0 } ^ { n } x ^ { t } \sum _ { k = 0 } ^ { t } f \left( \frac { k } { n } \right) \binom { n } { k } \binom { n } { n } \binom { n - k } { n - t } ( - 1 ) ^ { t - k } = \displaystyle \sum _ { t = 0 } ^ { n } x ^ { t } \binom { n } { t } \sum _ { k = 0 } ^ { t } f \left( \frac { k } { n } \right) \binom { t } { k } \binom { t } { k } ( - 1 ) ^ { t - k } } \\ & { \qquad = \displaystyle \sum _ { t = 0 } ^ { n } \Delta ^ { t } f ( 0 ) \binom { n } { t } x ^ { t } . } \end{array}
$$

The last equality follows from (2.7.5).

Ex.1.If $f \in \mathcal { P } _ { m }$ then $\Delta ^ { t } f \left( 0 \right) = 0$ for $\smash { t > m }$ ：(6.2.3) then implies that $B _ { n } ( f ; x ) \in \mathcal P _ { m }$ for all $\pmb { n }$

Ex.2. Useful identities may be derived by applying (6.2.3) to the functions $1 , x , x ^ { 2 }$ .For $\pmb { f } ( \pmb { x } ) = \pmb { 1 }$ ，we have $\Delta ^ { 0 } f ( 0 ) = 1 , \Delta ^ { 1 } f ( 0 ) = 0 , \Delta ^ { 2 } f ( 0 ) = 0 ,$ etc.Hence

$$
B _ { n } ( 1 ; x ) = \sum _ { k = 0 } ^ { n } { \binom { n } { k } } x ^ { k } ( 1 - x ) ^ { n - k } = 1 .
$$

This,of course,is the binomial expansion for $\mathbf { l } ^ { n } = ( { \pmb x } + ( { \pmb 1 } - { \pmb x } ) ) ^ { n }$

Hx ${ \bf 3 . \mathrm {  ~ \ F o r ~ } } \ f ( x ) = x , \ \mathrm { \tiny { w e } } \ \mathrm {  ~ \ h a v e ~ } \ \Delta ^ { 0 } f ( 0 ) = 0 , \Delta ^ { 1 } f ( 0 ) = { \frac { 1 } { n } } , \Delta ^ { 2 } f ( 0 ) = 0 , \dots .$

$$
B _ { n } ( x ; x ) = \sum _ { k = 0 } ^ { n } { \frac { k } { n } } { \binom { n } { k } } x ^ { k } ( 1 - x ) ^ { n - k } = { \frac { 1 } { n } } { \binom { n } { 1 } } x = x .
$$

Ex.4. For $f ( x ) = x ^ { 2 }$ ,we have

$$
\Delta ^ { 0 } f ( 0 ) = 0 , \quad \Delta ^ { 1 } f ( 0 ) = \frac 1 { n ^ { 2 } } , \quad \Delta ^ { 2 } f ( 0 ) = \frac 2 { n ^ { 2 } } , \quad \Delta ^ { 3 } f ( 0 ) = 0 , \ldots . . .
$$

Hence

$$
B _ { n } ( x ^ { 2 } ; x ) = \sum _ { k = 0 } ^ { n } { \binom { k } { n } } ^ { 2 } { \binom { n } { k } } x ^ { k } ( 1 - x ) ^ { n - k } = { \frac { 1 } { n ^ { 2 } } } { \binom { n } { 1 } } x + { \frac { 2 } { n ^ { 2 } } } { \binom { n } { 2 } } x ^ { 2 } .
$$

Ex.5. $B _ { n } ( e ^ { \alpha x } ; x ) = ( x e ^ { \alpha / n } + ( 1 - x ) ) ^ { n } .$

THEOREM 6.2.2 (Bernstein).Let $f ( x )$ be bounded on [0,1]. Then

$$
\operatorname* { l i m } _ { n \to \infty } B _ { n } ( f ; x ) = f ( x )
$$

at any point ${ \pmb x } \in [ 0 , 1 ]$ at which $\pmb { f }$ is continuous. If $f \in C [ 0 , 1 ]$ , the limit (6.2.7) holds uniformly in [0,1].

Proof: A. Note the identity

$$
\sum _ { k = 0 } ^ { n } ( k - n x ) ^ { 2 } \binom { n } { k } x ^ { k } ( 1 - x ) ^ { n - k } \equiv n x ( 1 - x ) .
$$

To prove this, expand this sum into

$$
\begin{array} { l } { { \displaystyle \sum _ { k = 0 } ^ { n } k ^ { 2 } \binom { n } { k } x ^ { k } ( 1 - x ) ^ { n - k } - 2 n x \sum _ { k = 0 } ^ { n } k \binom { n } { k } x ^ { k } ( 1 - x ) ^ { n - k } } } \\ { { + n ^ { 2 } x ^ { 2 } \sum _ { k = 0 } ^ { n } \binom { n } { k } x ^ { k } ( 1 - x ) ^ { n - k } , } } \end{array}
$$

and combine this with identities (6.2.4),(6.2.5),and (6.2.6)

B. For a given $\delta > 0$ and for $0 \leq x \leq 1$ ，we have

$$
\sum _ { | k / n - x | \geq \delta } { \binom { n } { k } } x ^ { k } ( 1 - x ) ^ { n - k } \leq \frac { 1 } { 4 n \delta ^ { 2 } } .
$$

$k = 0 , 1 , \ldots , n$ $\left| { \frac { k } { n } } - x \right| \geq \delta$ $\left| { \frac { k } { n } } - x \right| \geq \delta$ $\frac { 1 } { \delta ^ { 2 } } \left( \frac { k } { n } - x \right) ^ { 2 } \geq 1$ Heno

$$
\begin{array} { r l } & { \underset { | k / n - x | \geq \delta } { \sum } \binom { n } { k } x ^ { k } ( 1 - x ) ^ { n - k } \leq \frac { 1 } { \delta ^ { 2 } } \underset { | k / n - x | \geq \delta } { \sum } \bigg ( \frac { k } { n } - x \bigg ) ^ { 2 } \binom { n } { k } x ^ { k } ( 1 - x ) ^ { n - k } } \\ & { \qquad \leq \frac { 1 } { \delta ^ { 2 } } \underset { k = 0 } { \sum } \bigg ( \frac { k } { n } - x \bigg ) ^ { 2 } \binom { n } { k } x ^ { k } ( 1 - x ) ^ { n - k } = \frac { n x ( 1 - x ) } { \delta ^ { 2 } n ^ { 2 } } \leq \frac { 1 } { 4 n \delta ^ { 2 } } . } \end{array}
$$

The last inequality follows since $x ( 1 - x ) \leq \pmb { \underline { { \mathtt { i } } } }$ for all $_ { \pmb { x } }$

C. We hae

$$
\begin{array} { c } { { 1 = \displaystyle \sum _ { k = 0 } ^ { n } { \binom { n } { k } } x ^ { k } ( 1 - x ) ^ { n - k } \mathrm { f r o m ~ } ( 6 . 2 . 4 ) . \mathrm { H e n c e } , } } \\ { { f ( x ) = \displaystyle \sum _ { k = 0 } ^ { n } f ( x ) { \binom { n } { k } } x ^ { k } ( 1 - x ) ^ { n - k } } } \end{array}
$$

so that

$$
\begin{array} { l } { { f ( x ) - B _ { n } ( f ; x ) = \displaystyle \sum _ { k = 0 } ^ { n } \left\{ f ( x ) - f \Big ( \frac k n \Big ) \right\} \Big ( \displaystyle n \Big ) x ^ { k } ( 1 - x ) ^ { n - k } } } \\ { { = \displaystyle \sum _ { | k / n - x | < \delta } \left\{ f ( x ) - f \Big ( \frac k n \Big ) \right\} \Big ( \displaystyle n \Big ) x ^ { k } ( 1 - x ) ^ { n - k } } } \\ { { + \displaystyle \sum _ { | k / n - x | \geq \delta } \left\{ f ( x ) - f \Big ( \frac k n \Big ) \right\} \Big ( \displaystyle n \Big ) x ^ { k } ( 1 - x ) ^ { n - k } . } } \end{array}
$$

The function $f ( x )$ is assumed bounded in [O,1]. Hence for some $M > 0$ ， $| f ( { \pmb x } ) | \leq { \pmb M }$ and for any two values $\pmb { \alpha }$ ， $\beta \in [ 0 , 1 ]$ ， $| f ( \alpha ) - f ( \beta ) | \leq 2 M$ Let $_ { \pmb { x } }$ be a point of continuity of $f .$ Given an $\varepsilon > 0$ ，we can find a $\pmb { \delta }$ such that

$| f ( x ) - f ( y ) | < \varepsilon$ whenever $| y - x | < \delta$ 、Thus,using these estimates and using this $\pmb { \delta }$ in (6.2.9), we have

$$
\begin{array} { r l } & { | f ( x ) - B _ { n } ( f ; x ) | \le \displaystyle \sum _ { | k / n - x | < \delta } | f ( x ) - f \Big ( \displaystyle \frac { k } { n } \Big ) \bigg | \bigg ( \displaystyle \frac { n } { k } \bigg ) x ^ { k } ( 1 - x ) ^ { n - k }  } \\ & { \qquad +  \displaystyle \sum _ { | k / n - x | \ge \delta } \bigg | f ( x ) - f \Big ( \displaystyle \frac { k } { n } \bigg ) \bigg | \bigg ( \displaystyle \frac { n } { k } \bigg ) x ^ { k } ( 1 - x ) ^ { n - k } \qquad } \\ & { \qquad \le  \varepsilon \sum _ { | k / n - x | < \delta } \binom { n } { k } x ^ { k } ( 1 - x ) ^ { n - k } + \displaystyle \frac { 2 M } { | k / n - x | \ge \delta } \binom { n } { k } x ^ { k } ( 1 - x ) ^ { n - k }  } \\ & { \qquad \le  \varepsilon \sum _ { k = 0 } ^ { \displaystyle \frac { N } { \delta } } \binom { n } { k } x ^ { k } ( 1 - x ) ^ { n - k } + \displaystyle \frac { 2 M } { 4 n \delta ^ { 2 } } = \varepsilon + \displaystyle \frac { M } { 2 n \delta ^ { 2 } } . } \end{array}
$$

From this inequality，we see that $| f ( x ) - B _ { n } ( f ; x ) | \le 2 \varepsilon$ for $\pmb { n }$ sufficiently large.Sinceεis arbitrary,(6.2.7) follows.

Suppose now that $f \in C [ 0 , 1 ]$ ；then $f$ is uniformly continuous there. Given an $\varepsilon > 0$ ,we can find a $\pmb { \delta }$ such that $| f ( x ) - f ( y ) | < \varepsilon$ for all $x , y$ in [0,1] satisfying $| x - y | < \delta$ ，The above inequality holds independently of the $_ { \pmb { x } }$ selected and the convergence to $\pmb { f } ( \pmb { x } )$ is uniform in [0,1].We express this as a corollary.

COROLLARY 6.2.3．If $f ( x ) \in C [ 0 , 1 ]$ ， then given an $\varepsilon > 0$ ， we have for all sufficiently large $\pmb { n }$ ，

$$
| f ( x ) - B _ { n } ( f ; x ) | \leq \varepsilon , 0 \leq x \leq 1 .
$$

Bernstein's Theorem not only proves the existence of polynomials of uniform approximation,but provides a simple explicit representation for them.

The results for [0,1] are easily transferred to $[ a , b ]$ by means of the linear transformation

$$
y = \frac { x - a } { b - a }
$$

that converts $[ a , b ]$ into [0, 1].

COROLLARY 6.2.4 (Theorem 6.1.1)．Let $f ( x ) \in C [ a , b ]$ . Then given $\varepsilon > 0$ ， we can find a polynomial ${ \pmb p } ( { \pmb x } )$ such that $| f ( x ) - p ( x ) | \leq \varepsilon$ for ${ a \leq x \leq b }$ ·

Proof:Consider $\begin{array} { r } { g ( y ) = f ( a + ( b - a ) y ) } \end{array}$ $g \in C [ 0 , 1 ]$ .Hence given an $\varepsilon > 0$ we can find a polynomial $r ( y )$ such that $| g ( y ) - r ( y ) | \leq \varepsilon$ ， $0 \leq y \leq 1$ Set $p ( x ) = r { \biggl ( } { \frac { x - a } { b - a } } { \biggr ) }$ ,which is a polynomial in $_ { \pmb { x } }$ ,and the required inequality follows.

6.3 Simultaneous Approximation of Functions and Derivatives. In contrast to other modes of approximation-in particular to Tschebyscheff or best uniform approximation which will be studied subsequentlythe Bernstein polynomials yield smooth approximants.If the approximated function is differentiable,not only do we have $B _ { n } ( f ; x ) \to f ( x )$ but ${ B _ { n } } ^ { \prime } ( f ; x )  f ^ { \prime } ( x )$ .A corresponding statement is true for higher derivatives. The Bernstein polynomials therefore provide simultaneous approximation of the function and its derivatives.

In order to make the force of this result felt,we call attention to the following examples from real and complex analysis.

Ex.1.Uniform approximation does not automatically carry with it approximation of the derivatives.Considerfn(x) = nsin nx on[0,2π].Since|fn(x) ≤n the sequence $f _ { n }$ converges to O uniformly on $[ 0 , 2 \pi ]$ .On the other hand, ${ f _ { n } } ^ { \prime } ( x ) =$ cos $\pmb { n x }$ ，so that ${ f _ { n } } ^ { \prime }$ does not approach $\mathbf { 0 } ^ { \prime } = \mathbf { 0 }$ ·

This phenomenon may be present in sequences of polynomials.Let $f _ { n } ( x ) = { \frac { 1 } { n } } T _ { n } ( x )$ ，Cf. (3.3.2). Since $| T _ { n } ( x ) | \leq 1$ on[-1,1], it follows that $f _ { n } \to 0$ uniformly there.Now, ${ f _ { n } } ^ { \prime } ( x ) = ( 1 - x ^ { 2 } ) ^ { - 1 }$ sin ( $\mathbf { \lambda } _ { n }$ arc cos x),and if we set $x _ { n } = \cos { \frac { \pi } { 2 n } }$ ，then ${ f _ { n } } ^ { \prime } ( x _ { n } ) = \csc { \frac { \pi } { 2 n } }$ . The sequence of derivatives of $f _ { n }$ cannot approach any function of $C [ - 1 , 1 ]$ uniformly.

Ex. 2. Uniform approximation of analytic functions by analytic functions is totally different.Let $\pmb { R }$ be a region bounded by a simple closed curve $\boldsymbol { \sigma }$ . Let $f ( z )$ and $p ( z )$ be two functions analytic in $\pmb { R }$ and on $c$ .Suppose that $\left| f ( z ) - p ( z ) \right| \leq \varepsilon$ on $\boldsymbol { \mathfrak { c } }$ .By the Maximum Principle,this inequality,and hence uniform approximation，persists throughout $\scriptstyle { \mathcal { R } }$ .Moreover，by Cauchy's Inequality (1.9.8） we have

$$
| f ^ { ( n ) } ( z ) - p ^ { ( n ) } ( z ) | \ \leq { \frac { n ! \ L ( C ) } { 2 \pi \delta ^ { n + 1 } } } \ \varepsilon
$$

for $\pmb { z }$ confined to a point set $\pmb { S }$ in $\scriptstyle { R }$ the distance of whose points from $\boldsymbol { c }$ is no less than δ.For fixed $\pmb { S }$ and $\mathscr { n }$ ，allow $\epsilon  0$ and (6.3.1) tells us that the nth derivative of the approximant is also a uniform approximation to the nth derivative of the approximee.In the complex analytic case,uniform approximation over regions carries with it the simultaneous uniform approximation,in the above sense,of all the derivatives.

LEMMA 6.3.1． Let $\pmb { p } \geq \mathbf { 0 }$ be an integer. Then

$$
B _ { n + p } ^ { ( p ) } ( f ; x ) = \frac { ( n + p ) ! } { n ! } \sum _ { t = 0 } ^ { n } \Delta ^ { p } f \left( \frac { t } { n + p } \right) \binom { n } { t } x ^ { t } ( 1 - x ) ^ { n - t } .
$$

Proof:Apply Leibnitz' formula

$$
( u v ) ^ { ( p ) } = \sum _ { j = 0 } ^ { p } { \binom { p } { j } } u ^ { ( j ) } v ^ { ( p - j ) }
$$

to (6.2.1) and obtain

$$
B _ { n + p } ^ { ( p ) } ( f ; x ) = \sum _ { k = 0 } ^ { n + p } f { \biggl ( } { \frac { k } { n + p } } { \biggr ) } \left( { n + p } \right) \sum _ { j = 0 } ^ { p } { \binom { p } { j } } ( x ^ { k } ) ^ { ( j ) } [ ( 1 - x ) ^ { n + p - k } ] ^ { ( p - j ) } .
$$

Now, we have $( x ^ { k } ) ^ { ( j ) } = k ! x ^ { k - j } / ( k - j ) ! , k - j \ge 0$ and

$$
\begin{array} { c } { { [ ( 1 - x ) ^ { n + p - k } ] ^ { ( p - j ) } = ( - 1 ) ^ { p - j } ( n + p - k ) ! } } \\ { { \times ( 1 - x ) ^ { n + j - k } / ( n + j - k ) ! , k - j \leq n . } } \end{array}
$$

Therefore (6.3.4) becomes

$$
\begin{array} { l } { { \displaystyle B _ { n + p } ^ { ( p ) } ( f ; x ) = } } \\ { { \displaystyle \sum _ { \ell = 0 } ^ { n + p } \sum _ { j = 0 \atop 0 \leq k - j \leq n } ^ { p } f \left( \frac { k } { n + p } \right) \frac { ( n + p ) ! } { ( k - j ) ! ( n + j - k ) ! } \binom { p } { j } ( - 1 ) ^ { p - j } x ^ { k - j } ( 1 - x ) ^ { n + j - k } . } } \end{array}
$$

If we set $k - j = t , \ k = t + j$ ，we see that $0 \leq t \leq n , \ j = 0 , 1 , . . . , p ,$ corresponds to the range of the sum in (6.3.5). We may write (6.3.5) as

$$
B _ { n + p } ^ { ( p ) } ( f ; x ) = ( n + p ) ! \sum _ { t = 0 } ^ { n } { \frac { x ^ { t } ( 1 - x ) ^ { n - t } } { t ! ( n - t ) ! } } \sum _ { j = 0 } ^ { p } ( - 1 ) ^ { p - j } \biggl ( { \frac { p } { j } } \biggr ) f \left( { \frac { t + j } { n + p } } \right)
$$

(6.3.2) now follows from (2.7.4).

THEOREM 6.3.2. Let $f ( x ) \in C ^ { p } [ 0 , 1 ]$ . Then

Proof: y (3.4.5) we have $\Delta ^ { o } f \left( \frac { t } { n + p } \right) = \frac { 1 } { ( n + p ) ^ { p } } f ^ { ( p ) } ( \xi _ { t } )$ for some $\pmb { \xi } _ { t }$ satisfying $\frac { t } { n + p } < \xi _ { t } < \frac { t + p } { n + p } , t = 0 , 1 , \dots , n .$ Hence from Lemma 6.3.1,

$$
B _ { n + p } ^ { ( p ) } ( f ; x ) = { \frac { ( n + p ) ! } { n ! ( n + p ) ^ { p } } } \sum _ { t = 0 } ^ { n } f ^ { ( p ) } ( \xi _ { t } ) { \binom { n } { t } } x ^ { t } ( 1 - x ) ^ { n - t } .
$$

It follows that

$$
\begin{array} { l } { \displaystyle \frac { n ! ( n + p ) ^ { p } } { ( n + p ) ! } B _ { n + p } ^ { ( p ) } ( f ; x ) = \sum _ { t = 0 } ^ { n } f ^ { ( p ) } \bigg ( \frac { t } { n } \bigg ) \binom { n } { t } x ^ { t } ( 1 - x ) ^ { n - t } } \\ { \displaystyle \qquad + \sum _ { t = 0 } ^ { n } \bigg \{ f ^ { ( p ) } ( \xi _ { t } ) - f ^ { ( p ) } \bigg ( \frac { t } { n } \bigg ) \bigg \} \bigg ( _ { t } ^ { n } \bigg ) x ^ { t } ( 1 - x ) ^ { n - t } . } \end{array}
$$

Since $\frac { t } { n + p } \le \frac { t } { n } \le \frac { t + p } { n + p } , t = 0 , 1 , \dots , n ,$ $\pmb { \xi } _ { t }$ tbat $\left| \xi _ { t } - { \frac { t } { n } } \right| < { \frac { t + p } { n + p } } - { \frac { t } { n + p } } = { \frac { p } { n + p } } .$

From the uniform continuity of $f ^ { ( { \pmb { \mathscr { p } } } ) } ( { \pmb x } )$ ， given an $\varepsilon > 0$ ，we can find an $\pmb { n _ { 0 } }$ such that for all $n \geq n _ { \mathfrak { d } }$ and all $\pmb { t }$ $| f ^ { ( p ) } ( \xi _ { t } ) - f ^ { ( p ) } ( t / n ) | < \varepsilon .$ As in the proof of Theorem 6.2.2,the second sum in (6.3.8) is less than $\pmb \varepsilon$ in absolute value for $\pmb { n } \geq \pmb { n _ { 0 } }$ and for all ${ \pmb x } \in [ 0 , 1 ]$ Furtermore, $\operatorname* { l i m } _ { n \to \infty } { \frac { n ! ( n + p ) ^ { p } } { ( n + p ) ! } } = 1$ ，and by Theorem 6.2.2, the frst sum approaches $f ^ { ( { \pmb { \mathscr { p } } } ) } ( { \pmb { \mathscr { x } } } )$ uniformly.The theorem follows from this.

More general results may be established on the assumption that $\pmb { f } ^ { ( \pmb { p } ) } ( \pmb { x } )$ exists at individual points of the interval.

THEOREM 6.3.3. Let $\pmb { p }$ be $\pmb { a }$ fxed integer with $0 \leq p \leq n$ 1f

$$
m \le f ^ { ( p ) } ( x ) \le M , 0 \le x \le 1
$$

then

$$
m \leq { \frac { n ^ { p } } { n ( n - 1 ) \cdot \cdot \cdot ( n - p + 1 ) } } B _ { n } ^ { ( p ) } ( f ; x ) \leq M , 0 \leq x \leq 1 .
$$

For $\pmb { p } = \mathbf { 0 }$ , the multiplier of $B _ { n } ^ { ( p ) }$ is to be interpreted as 1. If

$$
f ^ { ( p ) } ( x ) \geq 0 , 0 \leq x \leq 1
$$

then

$$
B _ { n } ^ { ( p ) } ( f ; x ) \geq 0 , 0 \leq x \leq 1 .
$$

1f $f ( x )$ is nondecreasing on $0 \leq x \leq 1$ ，then $\textstyle B _ { n } ( f ; x )$ is nondecreasing there.   
$H f f ( x )$ is convex on $0 \leq x \leq 1$ then $\textstyle B _ { n } ( f ; x )$ is convex there.

Proof: From (6.3.2) and (6.2.3) we have for $p = 1 , 2 , \ldots , n _ { : }$

$$
B _ { n } ^ { ( p ) } ( f ; x ) = n ( n - 1 ) \cdot \cdot \cdot ( n - p + 1 ) \sum _ { t = 0 } ^ { n - p } \Delta ^ { p } f \left( { \frac { t } { n } } \right) { \binom { n - p } { t } } x ^ { t } ( 1 - x ) ^ { n - p - t }
$$

By the extended mean value theorem, Cor. 3.4.4,

$$
\Delta ^ { p } f \left( \frac { t } { n } \right) = \frac { 1 } { n ^ { p } } f ^ { ( p ) } ( \xi _ { t } ) , \frac { t } { n } < \xi _ { t } < \frac { t + p } { n } .
$$

For $\pmb { p } = \mathbf { 0 }$ ,this equality obviously holds with $\xi _ { t } = t / n$ . Hence,

$$
\begin{array} { c } { { Q = \displaystyle \frac { n ^ { p } } { n ( n - 1 ) \cdot \cdot \cdot ( n - p + 1 ) } B _ { n } ^ { ( p ) } ( f ; x ) } } \\ { { = \displaystyle \sum _ { t = 0 } ^ { n - p } f ^ { ( p ) } ( \xi _ { t } ) \binom { n - p } { t } x ^ { t } ( 1 - x ) ^ { n - p - t } . } } \end{array}
$$

In view of (6.3.9) and the fact that $x ^ { t } ( 1 - x ) ^ { n - p - t } \geq 0$ on [0,1], it follows

that

$$
n = m \sum _ { t = 0 } ^ { n - p } { \binom { n - p } { t } } x ^ { t } ( 1 - x ) ^ { n - p - t } \leq Q \leq M \sum _ { t = 0 } ^ { n - p } { \binom { n - p } { t } } x ^ { t } ( 1 - x ) ^ { { \boldsymbol { \circ } } \cdot { \boldsymbol { \sigma } } \cdot { \boldsymbol { t } } } = M
$$

This demonstrates (6.3.10). (6.3.11) follows by setting ${ \pmb m } = { \bf 0 }$

If $f ( x )$ is nondecreasing, $\Delta f ( t / n ) \geq 0$ and hence from (6.3.13) with $p = 1$ ， $B _ { n } ^ { \prime } ( f ; x ) \geq 0$ on [0,1] and this implies that $B _ { n } ( f ; x )$ is nondecreasing. Finally,if $f$ is convex,then by (3.2.2), $\Delta ^ { 2 } f ( t / n ) \geq 0$ .From (6.3.13） with $\pmb { p = 2 }$ ，this implies that ${ B _ { n } } ^ { \prime \prime } ( f ; x ) \ge 0$ By Theorem 3.2.1, this, in turn, implies that $B _ { n }$ is convex in every closed subinterval of (O,1). Since $B _ { n }$ is continuous,it is convex in [0,1].

THEOREM 6.3.4. Let $f ( x )$ be convex in [0,1]. Then,for $n = 2 , 3 , \ldots ,$

$$
B _ { n - 1 } ( f ; x ) \geq B _ { n } ( f ; x ) , \quad 0 < x < 1 .
$$

$I f f \in C [ 0 , 1 ]$ ,the strict inequality holds unless $f$ is linear in each of the intervals $\Big [ \frac { j - 1 } { n - 1 } , \frac { j } { n - 1 } \Big ] , j = 1 , 2 , \dots , n - 1 . \ I n \ t h i s \ c a s e , \ B _ { n - 1 } ( f ; \ x ) = I$

Proof:In (6.2.1) set $t = { \frac { x } { 1 - x } }$ and obtain

$$
\begin{array} { l } { { ( 1 - x ) ^ { - n } ( B _ { n - 1 } ( f ; x ) - B _ { n } ( f ; x ) ) } } \\ { { \ = ( 1 + t ) \displaystyle \sum _ { k = 0 } ^ { n - 1 } f \left( \frac { k } { n - 1 } \right) \binom { n - 1 } { k } t ^ { k } - \displaystyle \sum _ { k = 0 } ^ { n } f \left( \frac { k } { n } \right) \binom { n } { k } t ^ { k } } } \\ { { \ = \displaystyle \sum _ { k = 1 } ^ { n - 1 } f \left( \frac { k } { n - 1 } \right) \binom { n - 1 } { k } t ^ { k } + f ( 0 ) + \displaystyle \sum _ { k = 1 } ^ { n - 1 } f \left( \frac { k - 1 } { n - 1 } \right) \binom { n - 1 } { k - 1 } t ^ { k } + f ( 1 ) } } \end{array}
$$

$$
\begin{array} { c } { { c _ { k } = \displaystyle \frac { ( n - 1 ) ! } { ( k - 1 ) ! ( n - k - 1 ) ! } \left\{ \frac { 1 } { k } f \left( \frac { k } { n - 1 } \right) \right. } } \\ { { \displaystyle \left. + \frac { 1 } { n - k } f \left( \frac { k - 1 } { n - 1 } \right) - \frac { n } { k ( n - k ) } f \left( \frac { k } { n } \right) \right\} . } } \end{array}
$$

Now $\frac { k - 1 } { n - 1 } < \frac { k } { n } < \frac { k } { n - 1 }$ ,and since $f$ is convex,the bracketed quantity in (6.3.15) is $\geq 0$ by Definition 3.2.1. Therefore $\sum _ { k = 1 } ^ { n - 1 } c _ { k } t ^ { k } \geq 0$ and (6.3.14) follows. If $f$ is linear in each of the intervals $\left[ { \frac { j - 1 } { n - 1 } } , { \frac { j } { n - 1 } } \right]$ then all the $\pmb { c } _ { j }$ are 0 and hence $B _ { n - 1 } \equiv B _ { n }$ .Conversely,if $B _ { n - 1 } \equiv B _ { n }$ ,then all the $c _ { j }$ are 0,and since $f \in C [ 0 , 1 ]$ and is convex,(6.3.15) implies that $f$ is linear in each interval.

The geometric interpretation of these theorems is this.The Bernstein approximant of a continuous function lies between the extreme values of the function itself,and its higher derivatives are bounded by (6.3.10). Monotonic and convex functions yield monotonic and convex approximants respectively.Ina word—and this is reflected in Figure 6.3.l—the Bernstein approximants mimic the behavior of the function to a remarkable degree.

There is a price that must be paid for these beautiful approximation properties: the convergence of the Bernstein polynomials is very slow.

Ex. 3. From (6.2.6) we have $B _ { n } ( x ^ { 2 } ; x ) \ : - \ : x ^ { 2 } = \frac { x ( 1 - x ) } { n }$ . The convergence is like $1 / n$

It is far slower than what can be achieved by other means.If $f$ is bounded, then at a point where $f ^ { \prime \prime } ( x )$ exists and does not vanish, $\textstyle B _ { n } ( f ; x )$ converges to $f ( x )$ precisely like $C / n$ .(See Theorem 6.3.6.) This fact seems to have precluded any numerical application of Bernstein polynomials from having been made. Perhaps they will find application when the properties of the approximant in the large are of more importance than the closeness of the approximation.

![](../chunks/Interpolation and Approximation (Philip J. Davis) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/0b602ec06e4cc8af3ed44296305b17464f2cf9c41384f0434793a9cd80de0396.jpg)  
Figure 6.3.1 Illustrating the Approximation Properties of the Bernstein Polynomials of a Concave Function.

$\begin{array} { l } { B _ { 2 } ( f ; x ) = \frac { 3 } { 2 } ( x - x ^ { 2 } ) } \\ { B _ { 4 } ( f ; x ) = \frac { 5 } { 2 } x - 3 x ^ { 2 } + \frac { 3 } { 2 } x ^ { 3 } - x ^ { 4 } } \\ { B _ { 1 0 } ( f ; x ) = 3 x - 3 0 x ^ { 3 } + 1 0 5 x ^ { 4 } - 1 8 9 x ^ { 5 } + 2 1 0 x ^ { 6 } - 1 6 0 x ^ { 7 } + 9 0 x ^ { 8 } - 3 5 x ^ { 9 } + 6 . } \end{array}$ x10.   
The graph of $\pmb { f }$ is polygonal and joins (0,0), (.2,6),(.6,.8),(.9,.7), (1,0).

LEMMA 6.3.5. There is $^ { \pmb { a } }$ constant c independent of $\pmb { n }$ such that for all $_ { \pmb { x } }$ in [0,1],

$$
\sum _ { | k / n - x | \geq n ^ { - \frac 1 4 } } { \binom { n } { k } } x ^ { k } ( 1 - x ) ^ { n - k } \leq \frac { c } { n ^ { \frac 3 2 } } .
$$

Proof: Consider the sums

$$
\mathcal { S } _ { m } ( x ) = \sum _ { k = 0 } ^ { n } ( k - n x ) ^ { m } \binom { n } { k } x ^ { k } ( 1 - x ) ^ { n - k } .
$$

We have already established by (6.2.4),(6.2.5),and (6.2.8), that $S _ { \bf 0 } ( x ) = 1$ ， $S _ { 1 } ( x ) = 0$ ， $S _ { 2 } ( x ) = n x ( 1 - x )$ .Differentiating (6.3.17) we have

$$
\begin{array} { l } { { S _ { m } } ^ { \prime } ( x ) = \displaystyle \sum _ { k = 0 } ^ { n } \binom { n } { k } ( k - n x ) ^ { m - 1 } x ^ { k - 1 } ( 1 - x ) ^ { n - k - 1 } [ - m n x ( 1 - x ) + ( k - n x ) ^ { 2 } ] } \\ { ~ = - m n S _ { m - 1 } ( x ) + \displaystyle \frac { S _ { m + 1 } ( x ) } { x ( 1 - x ) } . ~ } \end{array}
$$

Hence,

$$
\begin{array} { r } { S _ { m + 1 } ( x ) = x ( 1 - x ) [ { S _ { m } } ^ { \prime } ( x ) + m n S _ { m - 1 } ( x ) ] . } \end{array}
$$

We may conclude from this recurrence that each sum $\boldsymbol { \mathcal { S } } _ { m } ( \boldsymbol { x } )$ isa polynomial in $_ { \pmb { x } }$ and $\pmb { n }$ . In particular, $\mathbb { S } _ { 3 }$ is of lst, $\mathcal { S } _ { 4 }$ is of 2nd, ${ \mathfrak { S } } _ { 5 }$ is of 2nd,and ${ \cal { S } } _ { 8 }$ is of 3rd degree in $\pmb { n }$ .Hence,for some constant $\pmb { c }$ ， $| S _ { 6 } ( x ) | \le c n ^ { 3 }$ for $_ { \pmb { x } }$ in [0,1].

$$
\left| { \frac { k } { n } } - x \right| \geq n ^ { - \frac { 1 } { 4 } } \operatorname { i m p l i e s } { \frac { ( k - n x ) ^ { 6 } } { n ^ { \frac { 9 } { 2 } } } } \geq 1 ,
$$

$$
\begin{array} { r l r } & { } & { \displaystyle \sum _ { | k / n - x | \geq n ^ { - \frac { n } { k } } } \binom { n } { k } x ^ { k } ( 1 - x ) ^ { n - k } \leq \frac { 1 } { n ^ { \frac { n } { 2 } } } \displaystyle \sum _ { k = 0 } ^ { n } ( k - n x ) ^ { \ast } \binom { n } { k } x ^ { k } ( 1 - x ) ^ { n - k } } \\ & { } & { \qquad = n ^ { - \frac { n } { 2 } } S _ { 6 } ( x ) \leq \displaystyle \frac { c } { n ^ { \frac { n } { 2 } } } . } \end{array}
$$

THEOREM 6.3.6 (Voronovsky). Let $\pmb { f } ( \pmb { x } )$ be bounded in [0,1] and let $\pmb { x _ { 0 } }$ be a point of [0,1] at which $f ^ { \prime \prime } ( x _ { 0 } )$ exists. Then,

$$
\operatorname* { l i m } _ { n \to \infty } n [ B _ { n } ( f ; x _ { 0 } ) - f ( x _ { 0 } ) ] = \frac { 1 } { 2 } x _ { 0 } ( 1 - x _ { 0 } ) f ^ { \prime \prime } ( x _ { 0 } ) .
$$

Proof:From Theorem 1.6.6 we have

$$
f ( x ) = f ( x _ { 0 } ) + f ^ { \prime } ( x _ { 0 } ) ( x - x _ { 0 } ) + { \frac { f ^ { \prime \prime } ( x _ { 0 } ) ( x - x _ { 0 } ) ^ { 2 } } { 2 } } + s ( x ) ( x - x _ { 0 } ) ^ { 2 }
$$

where $\operatorname* { l i m } _ { x \to x _ { 0 } } s ( x ) = 0$ Set $\ x = { \frac { k } { n } }$

$$
f { \biggl ( } { \frac { k } { n } } { \biggr ) } = f ( x _ { 0 } ) + f ^ { \prime } ( x _ { 0 } ) { \biggl ( } { \frac { k } { n } } - x _ { 0 } { \biggr ) } + { \frac { f ^ { \prime \prime } ( x _ { 0 } ) } { 2 } } { \biggl ( } { \frac { k } { n } } - x _ { 0 } { \biggr ) } ^ { 2 } + s { \biggl ( } { \frac { k } { n } } { \biggr ) } { \biggl ( } { \frac { k } { n } } - x _ { 0 } { \biggr ) } ^ { 2 }
$$

Multiply both sidesof (6.3.21) $\mathrm { b y } \binom { n } { k } x _ { 0 } { } ^ { k } ( 1 - x _ { 0 } ) ^ { n - k }$ and sum from $k = 0$ to $k = n$ . In view of identities (6.2.4-6),we obtain

$$
3 _ { n } ( f ; x _ { 0 } ) = f ( x _ { 0 } ) + { \frac { x _ { 0 } ( 1 - x _ { 0 } ) f ^ { \prime \prime } ( x _ { 0 } ) } { 2 n } } + \sum _ { k = 0 } ^ { n } s \left( { \frac { k } { n } } \right) \left( { \frac { k } { n } } - x _ { 0 } \right) ^ { 2 } { \binom { n } { k } } x _ { 0 } ^ { k } ( 1 - x _ { 0 } ) ^ { n - k }
$$

Designate the third term in (6.3.22) by $\pmb { S }$ Let $\varepsilon > 0$ be given.We can find $\pmb { n }$ suffcently large that $| x - x _ { 0 } | < { \frac { 1 } { n ^ { \ddag } } }$ implies $| \cdot s ( x ) | \leq \varepsilon$ Hence,

$$
| S | \le \sum _ { | k / n - x _ { 0 } | < n ^ { - \frac { 1 } { 4 } } } \bigg | s \bigg ( \frac { k } { n } \bigg ) \bigg | \bigg ( \frac { k } { n } - x _ { 0 } \bigg ) ^ { 2 } \bigg ( \frac { n } { k } \bigg ) x _ { 0 } \ l ^ { k } ( 1 - x _ { 0 } ) \ l ^ { n - k }
$$

Thus,

$$
| S | \leq \varepsilon \sum _ { k = 0 } ^ { n } \binom { k } { n } x _ { 0 } ^ { k } ( 1 - x _ { 0 } ) ^ { 2 } \binom { n } { k } x _ { 0 } ^ { k } ( 1 - x _ { 0 } ) ^ { n - k } + M \sum _ { | k | { n - x _ { 0 } } | \geq n - \frac { 1 } { k } } \binom { n } { k } x _ { 0 } ^ { k } ( 1 - x _ { 0 } ) ^ { n - k }
$$

where $M = { \begin{array} { c c c } { \mathbf { s u p } } & { s ( x ) ( x - x _ { 0 } ) ^ { 2 } } \end{array} }$ .By (6.2.8) and Lemma 6.3.5, $\mathbf { 0 } \le \pmb { x } \le \mathbf { 1 }$

$$
| S | \leq \frac { \varepsilon x _ { 0 } ( 1 - x _ { 0 } ) } { n } + \frac { M C } { n ^ { \frac { 3 } { 2 } } } .
$$

It follows from (6.3.22) that

$$
\left| n [ B _ { n } ( f ; x _ { 0 } ) - f ( x _ { 0 } ) ] - \frac { x _ { 0 } ( 1 - x _ { 0 } ) } { 2 } f ^ { \prime \prime } ( x _ { 0 } ) \right| = | n S | \leq \varepsilon x _ { 0 } ( 1 - x _ { 0 } ) + \frac { M C } { n ^ { \frac { 1 } { 2 } } } .
$$

Since $\pmb \varepsilon$ is arbitrary,(6.3.20) follows.

# 6.4 Approximation by Interpolation: Fejer's Proof.

THEOREM 6.4.1． Let $x _ { 1 } , x _ { 2 } , \ldots , x _ { n }$ be the zeros of the Tschebyscheff polynomial $T _ { n } ( x ) , \left( x _ { j } = \cos \frac { 2 j - 1 } { 2 n } \pi \right)$ Let $f ( x ) \in C [ - 1 , 1 ]$ and suppose that $H _ { 2 n - 1 } ( f ; x )$ is that element of $\mathscr { P } _ { 2 n - 1 }$ for which

$$
\begin{array} { l l } { { H _ { 2 n - 1 } ( f ; x _ { k } ) = f ( x _ { k } ) } } & { { } } \\ { { \nonumber } } & { { } } \\ { { H _ { 2 n - 1 } ^ { \prime } ( f ; x _ { k } ) = 0 } } & { { } } \end{array} \ z = 1 , 2 , . . . \ , n .
$$

Then $, \operatorname* { l i m } _ { n  \infty } H _ { 2 n - 1 } ( f ; x ) = f ( x )$ uniformly in [-1,1].

Proof:We are confronted here with a problem of Hermite interpolation.

As already observed in (2.5.20), the general solution is given by

where

$$
\begin{array} { c } { { H _ { 2 n - 1 } ( f ; x ) = \displaystyle \sum _ { k = 1 } ^ { n } y _ { k } A _ { k } ( x ) + \sum _ { k = 1 } ^ { n } y _ { k } { } ^ { \prime } B _ { k } ( x ) } } \\ { { { } } } \\ { { A _ { k } ( x ) = \displaystyle \left[ 1 - \frac { w ^ { \prime } ( x _ { k } ) } { w ^ { \prime } ( x _ { k } ) } ( x - x _ { k } ) \right] l _ { k } { } ^ { 2 } ( x ) } } \\ { { B _ { k } ( x ) = ( x - x _ { k } ) l _ { k } { } ^ { 2 } ( x ) } } \\ { { l _ { k } ( x ) = \displaystyle \frac { w ( x ) } { w ^ { \prime } ( x _ { k } ) ( x - x _ { k } ) } , w ( x ) = ( x - x _ { 1 } ) \cdots ( x - x _ { n } ) . } } \end{array}
$$

In the present construction，we select $y _ { k } ^ { \prime } = 0 , k = 1 , \ldots , n$ so that our interpolation polynomial reduces to

$$
H _ { 2 n - 1 } ( f ; x ) = \sum _ { k = 1 } ^ { n } f ( x _ { k } ) A _ { k } ( x ) .
$$

We next compute $l _ { \pmb { k } } ( \pmb { x } ) , \pmb { w } ^ { \prime } ( \pmb { x } _ { \pmb { k } } ) , \pmb { w } _ { \pmb { k } } ^ { \prime \prime } ( \pmb { x } )$ .Now

$$
w ( x ) = c _ { n } T _ { n } ( x ) = c _ { n } \cos { ( n \operatorname { a r c } \cos { x } ) } , c _ { n } = { \frac { 1 } { 2 ^ { n - 1 } } } ,
$$

and hence,

$$
{ \frac { w ^ { \prime } ( x ) } { c _ { n } } } = { \frac { n \sin { ( n \operatorname { a r c } \cos { x } ) } } { \sqrt { 1 - x ^ { 2 } } } } , \mathrm { a n d }
$$

$$
{ \frac { w ^ { \prime \prime } ( x ) } { c _ { n } } } = n \biggl [ { \frac { x \sin { ( n \arg { \cos { x } } ) } } { ( 1 - x ^ { 2 } ) ^ { \frac { 3 } { 2 } } } } - { \frac { n ( 1 - x ^ { 2 } ) ^ { \frac { 1 } { 2 } } \cos { ( n \arg { \cos { x } } ) } } { ( 1 - x ^ { 2 } ) ^ { \frac { 3 } { 2 } } } } \biggr ] .
$$

At $\scriptstyle \cdot x = x _ { k } , \cos \left( n \operatorname { a r c } \cos x \right) = 0$ ,and sin $( n \operatorname { a r c } \cos x ) = \sin \left( ( k - { \frac { 1 } { 2 } } ) \pi \right) = ( - 1 ) ^ { k - 1 } .$

$$
{ \frac { w ^ { \prime } ( x _ { k } ) } { c _ { n } } } = { \frac { ( - 1 ) ^ { k - 1 } n } { \sqrt { 1 - { x _ { k } } ^ { 2 } } } } , { \frac { w ^ { \prime \prime } ( x _ { k } ) } { c _ { n } } } = { \frac { n x _ { k } ( - 1 ) ^ { k - 1 } } { ( 1 - { x _ { k } } ^ { 2 } ) ^ { \frac { 3 } { 2 } } } } ,
$$

$$
l _ { k } ( x ) = { \frac { ( - 1 ) ^ { k - 1 } { \sqrt { 1 - x _ { k } ^ { 2 } } } T _ { n } ( x ) } { n ( x - x _ { k } ) } } , 1 - { \frac { w ^ { \prime } ( x _ { k } ) } { w ^ { \prime } ( x _ { k } ) } } ( x - x _ { k } ) = { \frac { 1 - x x _ { k } } { 1 - { x _ { k } } ^ { 2 } } }
$$

$$
\begin{array} { l } { { A _ { k } ( x ) = \displaystyle \bigg [ 1 - \frac { w ^ { \prime } ( x _ { k } ) } { w ^ { \prime } ( x _ { k } ) } ( x - x _ { k } ) \bigg ] l _ { k } { } ^ { 2 } ( x ) = \displaystyle \frac { 1 - x x _ { k } } { 1 - x _ { k } ^ { 2 } } \frac { T _ { n } { } ^ { 2 } ( x ) ( 1 - x _ { k } ^ { 2 } ) } { n ^ { 2 } ( x - x _ { k } ) ^ { 2 } } } } \\ { { = ( 1 - x x _ { k } ) \bigg ( \frac { T _ { n } ( x ) } { n ( x - x _ { k } ) } \bigg ) ^ { 2 } . } } \end{array}
$$

Formula (6.4.4) can be rewriten as

$$
H _ { 2 n - 1 } ( f ; x ) = \sum _ { k = 1 } ^ { n } f ( x _ { k } ) ( 1 - x x _ { k } ) { \bigg ( } { \frac { T _ { n } ( x ) } { n ( x - x _ { k } ) } } { \bigg ) } ^ { 2 } { \stackrel { } { = } } \sum _ { k = 1 } ^ { n } f ( x _ { k } ) A _ { k } ( x )
$$

where

$$
A _ { k } ( x ) = ( 1 - x x _ { k } ) \bigg ( \frac { T _ { n } ( x ) } { n ( x - x _ { k } ) } \bigg ) ^ { 2 } .
$$

Observe that since $| x _ { k } | < 1$ ， $A _ { \boldsymbol { k } } ( \boldsymbol { x } ) \geq 0$ for $- 1 \leq x \leq 1$ . Observe further that

$$
H _ { \mathbf { 2 } n - 1 } ( 1 ; x ) = \sum _ { k = 1 } ^ { n } A _ { k } ( x )
$$

is that unique polynomial $P _ { 2 n - 1 } ( x )$ of degree $\leq 2 n - 1$ ,for which

$$
P _ { 2 n - 1 } ( x _ { k } ) = 1 , \quad P _ { 2 n - 1 } ^ { \prime } ( x _ { k } ) = 0 , \quad k = 1 , 2 , \ldots , n .
$$

The polynomial 1 fts these requirements and hence

$$
H _ { 2 n - 1 } ( 1 ; x ) = \sum _ { k = 1 } ^ { n } A _ { k } ( x ) \equiv 1 .
$$

After these algebraic preliminaries we can turn to the proof of conver-gence. Since $\sum _ { i \mathop { = } 1 } ^ { n } A _ { k } ( x ) \equiv 1$ , it follows that $f ( x ) = \sum _ { k = 1 } ^ { n } f ( x ) A _ { k } ( x )$ so that

$$
f ( x ) - H _ { 2 n - 1 } ( f ; x ) = \sum _ { k = 1 } ^ { n } ( f ( x ) - f ( x _ { k } ) ) A _ { k } ( x )
$$

and

$$
| f ( x ) - H _ { 2 n - 1 } ( f ; x ) | \leq \sum _ { k = 1 } ^ { n } | f ( x ) - f ( x _ { k } ) | A _ { k } ( x ) .
$$

Since $f ( x ) \in C [ - 1 , 1 ]$ ,it is uniformly continuous there. This means that if $\varepsilon > 0$ is given,we can find a $\delta > 0$ such that

$$
| x _ { 1 } - x _ { 2 } | \leq \delta { \mathrm { ~ i m p l i e s ~ } } | f ( x _ { 1 } ) - f ( x _ { 2 } ) | \leq \varepsilon , - 1 \leq x _ { 1 } , x _ { 2 } \leq 1 .
$$

For a given $_ { \pmb { x } }$ in $[ - 1 , 1 ]$ ，split the indices $k = 1 , 2 , \ldots , n$ into two sets: $\mathbf { I } \colon | x - x _ { k } | < \delta$ II: $| x - x _ { k } | \geq \delta$ Then,

$$
| f ( x ) - H _ { 2 n - 1 } ( f ; x ) | \leq \sum _ { k \in \mathrm { I } } | f ( x ) - f ( x _ { k } ) | \ A _ { k } ( x ) + \sum _ { k \in \mathrm { I I } } | f ( x ) - f ( x _ { k } ) | \ A _ { k } ( x ) .
$$

We now estimate each of these sums. In view of (6.4.10) and (6.4.8),

$$
\sum _ { k \in \mathrm { I } } \left| f ( x ) - f ( x _ { k } ) \right| A _ { k } ( x ) \le \varepsilon \sum _ { k \in \mathrm { I } } A _ { k } ( x ) \le \varepsilon \sum _ { k = 1 } ^ { n } A _ { k } ( x ) = \varepsilon .
$$

Consider next $\boldsymbol { A } _ { \boldsymbol { k } } ( \boldsymbol { x } )$ for $| x - x _ { k } | \geq \delta , - 1 \leq x \leq 1 .$

$$
A _ { k } ( x ) = ( 1 - x x _ { k } ) \biggl [ \frac { T _ { n } ( x ) } { n ( x - x _ { k } ) } \biggr ] ^ { 2 } .
$$

Now, $0 < 1 - x x _ { k } < 2 , | T _ { n } ( x ) | \leq 1 , | x - x _ { k } | \geq \delta .$ Hence $A _ { k } ( x ) \leq \frac { 2 } { n ^ { 2 } \delta ^ { 2 } }$ Since $f \in C [ - 1 , 1 ]$ ,it is bounded on[-l,l] by some constant $M$ ：

$$
| f ( x ) | \leq M , - 1 \leq x \leq 1 .
$$

Thus, $| f ( x ) - f ( x _ { k } ) | \leq 2 M$ ，

$$
\sum _ { k \in \mathrm { I I } } \vert f ( x ) - f ( x _ { k } ) \vert \ A _ { k } ( x ) \le \sum _ { k \in \mathrm { I I } } 2 M \cdot \frac { 2 } { n ^ { 2 } \delta ^ { 2 } } \le \frac { 4 M } { n ^ { 2 } \delta ^ { 2 } } \sum _ { k = 1 } ^ { n } 1 = \frac { 4 M } { n \delta ^ { 2 } } .
$$

Combining these estimates, $| f ( x ) - H _ { 2 n - 1 } ( f ; x ) | \leq \varepsilon + { \frac { 4 M } { n \delta ^ { 2 } } }$ Having been given an $\varepsilon , \ \delta$ is determined.Select $\pmb { n }$ so large that $\frac { 4 M } { n \delta ^ { 2 } } \leq \varepsilon$ Thus,for $\pmb { n }$ sufficiently large and for all $- 1 \leq x \leq 1 , | f ( x ) - H _ { 2 n - 1 } ( f ; x ) | \leq 2 \varepsilon .$

6.5 Simultaneous Interpolation and Approximation. $\mathbf { I f } f \in C [ a , b ]$ it may be approximated uniformly by a polynomial.We know also that we may interpolate to $f$ at a set of points in $[ a , b ]$ .Can these processes be combined ? Given $\pmb { n }$ points $x _ { 1 } , x _ { 2 } , \ldots , x _ { n }$ in $[ a , b ]$ and given $\varepsilon > 0$ can we find a polynomial ${ \pmb p } ( { \pmb x } )$ such that $| f ( x ) - p ( x ) | \leq \varepsilon .$ ${ \pmb x } \in [ { \pmb a } , { \pmb b } ]$ and $p ( \pmb { x } _ { i } ) =$ $f ( x _ { i } ) , i = 1 , 2 , . ~ . ~ . ~ , n ?$ Such approximations may be very desirable.

![](../chunks/Interpolation and Approximation (Philip J. Davis) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/4f0fc94b079d1e2e3d80b4324e64d7332e14db0067f8f3e62fbbf1c4553aff27.jpg)  
Figure 6.5.1.

THEOREM 6.5.1 (Walsh). Let S be a closed bounded point set in the complex plane. Let $z _ { 1 } , \ldots , z _ { n }$ be $\pmb { n }$ distinct points of $\pmb { S }$ Suppose that $f ( z )$ is defined on $\pmb { S }$ and is uniformly approximable by polynomials there. Then it is uniformly approximable by polynomials $\pmb { p }$ that satisfy the auxiliary conditions

$$
p ( z _ { i } ) = f ( z _ { i } ) , i = 1 , 2 , . . . , n .
$$

Proof: Given an $\varepsilon > 0$ ,select a polynomial $\pmb { p } ( z )$ such that

$$
| f ( z ) - p ( z ) | \leq \varepsilon , z \in S .
$$

Set

$$
\begin{array} { l } { \displaystyle q ( z ) = \sum _ { k = 1 } ^ { n } \left( f ( z _ { k } ) - p ( z _ { k } ) \right) l _ { k } ( z ) } \\ { \displaystyle l _ { k } ( z ) = \frac { w ( z ) } { ( z - z _ { k } ) w ^ { \prime } ( z _ { k } ) } } \\ { \displaystyle w ( z ) = \prod _ { k = 1 } ^ { n } ( z - z _ { k } ) . } \end{array}
$$

Then $\pmb q ( \pmb z )$ is the unique element of $\mathscr { P } _ { n - 1 }$ with $q ( z _ { k } ) = f ( z _ { k } ) - p ( z _ { k } ) , k =$ $1 , 2 , \ldots , n$ Now

where

$$
\begin{array} { c } { { \displaystyle \operatorname* { m a x } _ { z \in S } | q ( z ) | \leq \sum _ { k = 1 } ^ { n } | f ( z _ { k } ) - p ( z _ { k } ) | \operatorname* { m a x } _ { z \in S } | l _ { k } ( z ) | \leq \varepsilon M } } \\ { { M = \displaystyle \sum _ { k = 1 } ^ { n } \operatorname* { m a x } _ { z \in S } | l _ { k } ( z ) | . } } \end{array}
$$

Note that $M$ depends only upon $\pmb { S }$ and $z _ { 1 } , \ldots , z _ { n }$ Set

$$
\begin{array} { r } { p _ { 1 } ( z ) = p ( z ) + q ( z ) . } \end{array}
$$

Then

$$
p _ { 1 } ( z _ { k } ) \ : = \ : p ( z _ { k } ) \ : + \ : q ( z _ { k } ) = f ( z _ { k } ) , k = 1 , 2 , . . . , n .
$$

Moreover,

$$
| f ( z ) - p _ { 1 } ( z ) | \leq | f ( z ) - p ( z ) | + | q ( z ) | \leq \varepsilon + M \varepsilon , ~ z \in \mathcal S .
$$

This inequality proves the theorem.

Ex.1．By Weierstrass'Theorem,any $f ( x ) \in C [ a , b ]$ is uniformly approximable by polynomials.Hence the answer to the question in the introductory paragraph of 6.5is“yes.”

Ex.2.Let $f ( z )$ be analytic in $| z | \leq R$ Since $f ( z )$ may be expanded in a power series which is uniformly convergent there,it is uniformly approximable there by polynomials.Let $z _ { 1 } , . . . , z _ { n }$ be distinct points in $| z | \leq R$ .Then we can find a polynomial $\pmb { \mathcal { P } } ^ { ( z ) }$ with $| f ( z ) - p ( z ) | \leq \varepsilon$ ， $| z | \leq R$ and $\begin{array} { r } { p ( z _ { k } ) = f ( z _ { k } ) , k = } \end{array}$ $1 , 2 , \ldots , n$

6.6 Generalizations of the Weierstrass Theorem. The Weierstrass Theorem has been generalized in many different directions.We shall meet some of the results in Chapter XI where closure and completeness are studied.Here,we shall look at generalizations to functions of $\pmb { N }$ real variables.Ifa real function of $\pmb { N }$ real variables is continuous on a closed bounded set of $R _ { N }$ ,it may be approximated uniformly by polynomials in the $\pmb { N }$ variables. There are many proofs of this fact.One proof-an extension of Theorem 6.2.2-makes use of generalized Bernstein polynomials: if $f ( x _ { 1 } ,$ $\pmb { x } _ { 2 } , \ldots , \pmb { x } _ { N } )$ is continuous on the hypercube $C \colon 0 \le x _ { j } \le 1 , j = 1 , 2 , . \ldots , N$ ， then the generalized Bernstein polynomial

$$
\begin{array} { l } { { \mathrm {  ~ \tilde { \rho } ~ } _ { ; } ^ , x _ { 1 } , x _ { 2 } , \dots , x _ { N } \rangle = \displaystyle \sum _ { k _ { 1 } = 0 } ^ { n _ { 1 } } \cdots \sum _ { k _ { N } = 0 } ^ { n _ { N } } \binom { n _ { 1 } } { k _ { 1 } } \binom { n _ { 2 } } { k _ { 2 } } \cdots \binom { n _ { N } } { k _ { N } } } } \\ { { \mathrm {  ~ \tilde { \rho } ~ } _ { \times } f \left( \frac { k _ { 1 } } { n _ { 1 } } , \frac { k _ { 2 } } { n _ { 2 } } , \dots , \frac { k _ { N } } { n _ { N } } \right) x _ { 1 } ^ { k _ { 1 } } ( 1 - x _ { 1 } ) ^ { n _ { 1 } - k _ { 1 } } \cdots x _ { N } ^ { k _ { N } } ( 1 - x _ { N } ) ^ { n _ { N } - k _ { N } } , } } \end{array}
$$

converges uniformly in $c$ to $f$ as $\operatorname* { m i n } _ { j } n _ { j } \to \infty$

In order to provide an alternate approach,and to present a result with a more contemporary flavor,we shall prove the Stone-Weierstrass Theorem and derive the $\pmb { N }$ -dimensional Weierstrass Theorem as a consequence. Stone's Theorem was inspired,in part,by an elementary proof of Weierstrass'Theorem given by Lebesgue in 1908.

We shall limit our discusson to real functions that are defined on a finite interval $\boldsymbol { \mathit { I } }$ of $R _ { n } \colon - \infty < a _ { i } \leq x _ { i } \leq b _ { i } < \infty$ .We designate points of $\pmb { I }$ by $P , Q$ etc.

LEMMA 6.6.1．Let $\pmb { F }$ be a family of functions that are real and continuous on $\boldsymbol { \mathit { I } }$ and such that

$$
f _ { 1 } , f _ { 2 } \in F \ i m p l i e s \ m a x \ [ f _ { 1 } , f _ { 2 } ] \in F \ a n d \operatorname* { m i n } \ [ f _ { 1 } , f _ { 2 } ] \in F .
$$

In order for $^ { \pmb { a } }$ function $f$ that is continuous on $\boldsymbol { \mathit { I } }$ to be uniformly approximable by members of $\pmb { F }$ ,it is necessary and suffcient that for any two points $P _ { 1 }$ and $P _ { 2 }$ of $\pmb { I }$ and for any $\varepsilon > 0$ ,there be $^ { \pmb { a } }$ function $t ( P ) \in F$ such that

$$
| f ( P _ { i } ) - t ( P _ { i } ) | < \varepsilon , i = 1 , 2 .
$$

Proof:If uniform approximation is possible, then given $\varepsilon > 0$ we can find a $t ( P ) \in F$ such that

$$
| f ( P ) - t ( P ) | < \varepsilon , \quad P \in { \cal I }
$$

and so (6.6.3) follows trivially.

Conversely，suppose that (6.6.3) holds.Select a fixed $Q \in I$ and a fixed $\varepsilon > 0$ ，Then,for any point $\boldsymbol { R }$ ，we can find a function $t ( P ) ( = t ( P ; Q , R , \varepsilon ) )$ such that $| f ( Q ) - t ( Q ) | < \varepsilon$ and $| f ( R ) - t ( R ) | < \varepsilon$ In particular,

$$
t ( R ) < f ( R ) + \varepsilon .
$$

By continuity of $\pmb { t }$ and $f _ { i }$ ，this inequality must persist in a certain neighborhood ${ \cal N } _ { R }$ of $\pmb { R }$ As $\pmb { R }$ runs over all the points of $\boldsymbol { \mathit { I } }$ ,the corresponding neighborhoods must cover $\boldsymbol { \mathit { I } }$ .Hence by the Heine-Borel Theorem,we can find a finite number of them $N _ { R _ { 1 } } , N _ { R _ { 2 } } , \ldots , N _ { R _ { k } }$ that cover $\pmb { I }$ . The corresponding functions $t ( P ; Q , R _ { i } )$ satisfy

$$
t ( P ; Q , R _ { i } ) < f ( P ) + \varepsilon , ~ P \in N _ { i } , ~ i = 1 , 2 , \ldots , k .
$$

Define

$$
t ^ { - } ( P ; Q ) = \operatorname * { m i n } { \big \{ } t ( P ; Q , R _ { 1 } ) , t ( P ; Q , R _ { 2 } ) , \ldots , t ( P ; Q , R _ { k } ) { \big \} } .
$$

By (6.6.2), iterated, $\pmb { t } ^ { - } \in \pmb { F }$ and by (6.6.5),

$$
t ^ { - } ( P , Q ) < f ( P ) + \varepsilon , \quad P \in { \cal Z } .
$$

Again, for each $_ i$ we have

$$
| f ( Q ) - t ( Q ; Q , R _ { i } ) | < \varepsilon
$$

so that

$$
t ( Q ; Q , R _ { i } ) > f ( Q ) - \varepsilon .
$$


<!-- chunk 0003: pages 141-210 -->
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
