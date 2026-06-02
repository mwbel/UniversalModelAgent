# CHAPTER II

# Interpolation

2.1 Polynomial Interpolation. This whole book can be regarded as a theme and variation on two theorems:an interpolation theorem of great antiquity and Weierstrass’approximation theorem of l885.The simple theorem of polynomial interpolation upon which much practical numerical analysis rests says,in effect,that a straight line can be passed through two points,a parabola through three,a cubic through four,and so on.

![](../chunks/Interpolation and Approximation (Philip J. Davis) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0070/auto/images/da8587d3ab9a4eeab60c56ef4567b8491dbfefcb7dce108ec54e6e30e8b058dd.jpg)  
Figure 2.1.1. Polynomial Interpolation.

THEOREM 2.1.1. Given $n + 1$ distinct (real or complex) points $z _ { 0 } , z _ { 1 } , \ldots , z _ { n }$ and $n + 1$ (real or complex) values $w _ { 0 } , w _ { 1 } , \ldots , w _ { n }$ There exists $^ { a }$ unique polynomial $\pmb { p } _ { n } ( z ) \in \mathcal { P } _ { n }$ for which

$$
p _ { n } ( z _ { i } ) = w _ { i } \qquad i = 0 , 1 , . . . , n .
$$

Proof:Set up a polynomial $a _ { 0 } + a _ { 1 } z + \cdots + a _ { n } z ^ { n }$ with $n + 1$ undetermined coefficients $a _ { i }$ ，The conditions (2.1.l) lead to the system of $n + 1$ linear equations in the ${ \bf { \em a } } _ { \imath }$ ：

$$
a _ { \pm } + a _ { 1 } z _ { i } + \cdot \cdot \cdot + a _ { n } z _ { \iota } { } ^ { n } = w _ { i } \qquad i = 0 , \ldots , n .
$$

The determinant of the system is the Vandermonde determinant formed

from $z _ { 0 } , \ldots , z _ { n }$ ：

$$
V ( z _ { 0 } , z _ { 1 } , \ldots , z _ { n } ) = \left| \begin{array} { c c c c c } { { 1 } } & { { z _ { 0 } } } & { { z _ { 0 } ^ { \ 2 } \cdot \cdot \cdot z _ { 0 } ^ { \ n } } } \\ { { } } & { { } } & { { } } & { { } } \\ { { 1 } } & { { z _ { 1 } } } & { { z _ { 1 } ^ { \ 2 } \cdot \cdot \cdot z _ { 1 } ^ { \ n } } } \\ { { } } & { { } } & { { } } & { { } } \\ { { \cdot } } & { { \cdot } } & { { \cdot } } & { { \cdot } } \\ { { 1 } } & { { z _ { n } } } & { { z _ { n } ^ { \ 2 } \cdot \cdot \cdot z _ { n } ^ { \ n } } } \end{array} \right| .
$$

To evaluate $V$ ,we may proceed as follows. Consider the function

$$
V ( z ) = V ( z _ { 0 } , z _ { 1 } , . . . , z _ { n - 1 } , z ) = \left| \begin{array} { c c } { { 1 } } & { { z _ { 0 } ~ ^ { . . . ~ } z _ { 0 } ^ { n } } } \\ { { . } } & { { . } } \\ { { . } } & { { . } } \\ { { . } } & { { . } } \\ { { 1 } } & { { z _ { n - 1 } ~ ^ { . . . ~ } z _ { n - 1 } ^ { n } } } \\ { { 1 } } & { { z ~ ^ { . . . ~ } z ^ { n } } } \end{array} \right| .
$$

$V ( z )$ is obviously in $\mathcal { P } _ { n }$ Furthermore it vanishes at $z _ { 0 } , z _ { 1 } , . . . , z _ { n - 1 }$ for inserting these values in place of $_ z$ yields two identical rows in the determinant. Thus,

$$
V ( z _ { 0 } , z _ { 1 } , . . . , z _ { n - 1 } , z ) = A ( z - z _ { 0 } ) ( z - z _ { 1 } ) \cdot \cdot \cdot ( z - z _ { n - 1 } )
$$

where $\pmb { A }$ depends only on $z _ { 0 } , z _ { 1 } , \dotsc , z _ { n - 1 }$ . To evaluate $\pmb { A }$ ,expand the determinant in (2.1.4) by minors of its last row.We then see that the coefficient of $z ^ { n }$ is $V ( z _ { 0 } , \dots , z _ { n - 1 } )$ . Thus, we have

$$
V ( z _ { 0 } , z _ { 1 } , . . . , z _ { n - 1 } , z ) = V ( z _ { 0 } , . . . , z _ { n - 1 } ) ( z - z _ { 0 } ) ( z - z _ { 1 } ) \cdot \cdot \cdot ( z - z _ { n - 1 } )
$$

and hence we have the recursion formula

$$
V ( z _ { 0 } , z _ { 1 } , . . . , z _ { n - 1 } , z _ { n } ) = V ( z _ { 0 } , . . . , z _ { n - 1 } ) ( z _ { n } - z _ { 0 } ) ( z _ { n } - z _ { 1 } ) \cdot \cdot \cdot ( z _ { n } - z _ { n - 1 } ) .
$$

Since $V ( z _ { 0 } , z _ { 1 } ) = z _ { 1 } - z _ { 0 }$ ,we have from (2.1.7),

$$
V ( z _ { 0 } , z _ { 1 } , z _ { 2 } ) = ( z _ { 1 } - z _ { 0 } ) ( z _ { 2 } - z _ { 0 } ) ( z _ { 2 } - z _ { 1 } )
$$

and by multiple applications of (2.1.7),

$$
V ( z _ { 0 } , z _ { 1 } , . . . , z _ { n } ) = \prod _ { i > j } ^ { n } ( z _ { i } - z _ { j } ) .
$$

By assumption, the points $z _ { 0 } , z _ { 1 } , \ldots , z _ { n }$ are distinct.Therefore $V \neq 0$ There is consequently a unique solution to the system (2.1.2).

Here is a second proof that contains a useful line of reasoning.Consider the system (2.1.2).If,when the right-hand side is O $( w _ { i } = 0 )$ ，the system possesses only the trivial zero solution，Theorem 1.2.2 tells us that its determinant does not vanish.Hence for an arbitrary right-hand side there is one and only one solution.Now a zero right-hand side to (2.l.2) means that $\scriptstyle { \pmb { p } } _ { \pmb { n } } ( z )$ vanishes at $n + 1$ distinct points. By Theorem 1.11.3, $a _ { k } = 0 , k =$ $0 , 1 , \ldots , n$ 、The homogeneous equation possesses only the trivial solution and the rest follows.

2.2 The General Problem of Finite Interpolation. In Theorem 2.1.1 we have reconstructed a polynomial $\in \mathcal { P } _ { \pmb { n } }$ on the basis of $\pm 1$ values. Can we do it on the basis of $n + 1$ arbitrary pieces of linear information? Can we do it for functions other than polynomials? These questions lead to the following general problem.

Let $\pmb { X }$ be a linear space of dimension $\pmb { n }$ and let $L _ { 1 } , L _ { 2 } , \ldots , L _ { n }$ be $\pmb { n }$ given linear functionals defined on $\pmb { X }$ .For a given set of values $w _ { 1 } , w _ { 2 } , \ldots , w _ { n } ,$ can we find an element of $\pmb { X }$ ,say $_ { \pmb { x } }$ ，such that

$$
L _ { i } ( x ) = w _ { i } \qquad i = 1 , 2 , \ldots , n !
$$

The answer is yes if the $\scriptstyle { L _ { i } }$ are independent in $X ^ { * }$ ·

LEMMA 2.2.1. Let $\pmb { X }$ have dimension $\pmb { n }$ .If $x _ { 1 } , \ldots , x _ { n }$ are independent in $\pmb { X }$ and $L _ { 1 } , \ldots , L _ { n }$ are independent in $X ^ { * }$ then

$$
| L _ { i } ( x _ { j } ) | \neq 0 .
$$

Conversely， if either $x _ { 1 } , \ldots , x _ { n }$ or $L _ { 1 } , \ldots , L _ { n }$ are independent and (2.2.2) holds then the other set is also independent.

Proof: Suppose that $| L _ { i } ( x _ { j } ) | = 0$ .Then also $| L _ { j } ( x _ { i } ) | = 0$ The system

$$
\begin{array} { l } { { a _ { 1 } L _ { 1 } ( x _ { 1 } ) + a _ { 2 } L _ { 2 } ( x _ { 1 } ) + \cdots + a _ { n } L _ { n } ( x _ { 1 } ) = 0 } } \\ { { \ . } } \\ { { . } } \\ { { . } } \\ { { . } } \\ { { a , L _ { 1 } ( x _ { \infty } ) + a , L _ { 2 } ( x _ { \infty } ) + \cdots + a , L _ { \mathit { \Pi } } ( x _ { \infty } ) = 0 } } \end{array}
$$

would have a nontrivial solution $a _ { 1 } , \ldots , a _ { n }$

Then,

$$
( a _ { 1 } L _ { 1 } + a _ { 2 } L _ { 2 } + \cdot \cdot \cdot + a _ { n } L _ { n } ) ( x _ { i } ) = 0 \qquad i = 1 , 2 , \ldots , n .
$$

Since ${ \pmb x _ { 1 } , \dotsb \cdot \dotsb , \pmb x _ { n } }$ form a basis for $\pmb { X }$ ，

$$
( a _ { 1 } L _ { 1 } + a _ { 2 } L _ { 2 } + \cdots + a _ { n } L _ { n } ) ( x ) = 0 \qquad x \in X
$$

and hence $a _ { 1 } L _ { 1 } + \cdots + a _ { n } L _ { n } = 0$

Therefore, $L _ { 1 } , \ldots , L _ { n }$ are dependent contrary to our assumption.

To show the converse,we may trace the argument backwards.

THEOREM 2.2.2. Let a linear space $\pmb { X }$ have dimension n and let $L _ { 1 } , L _ { 2 } , \ldots$ ， $L _ { n }$ be $\pmb { n }$ elements of $x ^ { * }$ .The interpolation problem (2.2.l) possesses a solution for arbitrary values $w _ { 1 } , w _ { 2 } , \ldots , w _ { n }$ if and only if the $L _ { i }$ are independent in $X ^ { * }$ The solution will be unique.

Proof:In this generality，the theorem is nothing but a rewording of Theorem 1.2.2. If the $\mathbf { } L _ { i }$ are independent and if $x _ { 1 } , \ldots , x _ { n }$ are independent, then $| L _ { i } ( x _ { j } ) | \neq 0$ by Lemma 2.2.1.Hence the system

$$
L _ { i } ( a _ { 1 } x _ { 1 } + a _ { 2 } x _ { 2 } + \cdot \cdot \cdot + a _ { n } x _ { n } ) = w _ { i } ~ i = 1 , 2 , \ldots , n
$$

Qr

$$
a _ { 1 } L _ { i } ( x _ { 1 } ) + a _ { 2 } L _ { i } ( x _ { 2 } ) + \cdot \cdot \cdot + a _ { n } L _ { i } ( x _ { n } ) = w _ { i }
$$

possesses a solution $a _ { 1 } , \ldots , a _ { n }$ and the element $\sum _ { i = 1 } ^ { n } a _ { i } x _ { i }$ solves the inter-  
polation problem.Conversely，if the problem (2.2.l） has a solution for arbitrary $w _ { i }$ ,then (2.2.3) has a solution for arbitrary $w _ { i }$ .By Theorem 1.2.2, this implies that $| L _ { \ i } ( x _ { j } ) | \neq 0$ and hence by Lemma 2.2.1, the $L _ { i }$ are independent.

The determinant $| L _ { i } ( x _ { j } ) |$ is a generalized Gram determinant (cf. Chapter 8.7)and its nonvanishing is synonomous with the possibility of solution of the interpolation problem.We may speak of independent systems of functionals as having the“interpolation property.’In the next section,we shall study some spaces and functionals for which the interpolation problem can be solved.But before passing to it,we should rid ourselves of the naive hope that an interpolation problem can always be solved providing the number of parameters equals the number of conditions.

Ex.1.Let $x$ designate the set of functions of the form $a _ { 0 } + a _ { 2 } x ^ { 2 }$ defined on [-1,1]. $x$ has dimension 2. If $L _ { 1 } ( f ) = f ( x _ { 1 } )$ and $L _ { 2 } ( f ) = f ( x _ { 2 } ) , - 1 \leq x _ { 1 } , x _ { 2 } \leq 1$ then the generalized Gram determinant for the independent elements 1, $x ^ { 2 }$ is

$$
\left| \begin{array} { c c } { { 1 } } & { { { x _ { 1 } } ^ { 2 } } } \\ { { } } & { { } } \\ { { 1 } } & { { { x _ { 2 } } ^ { 2 } } } \end{array} \right| = ( x _ { 2 } - x _ { 1 } ) ( x _ { 2 } + x _ { 1 } ) .
$$

This vanishes if $x _ { 1 } = x _ { 2 }$ or $x _ { 1 } = - x _ { 2 }$ In these cases $L _ { 1 }$ and $\scriptstyle L _ { 2 }$ are not independent.The frst case would be excluded trivially,but the second tells us that we cannot force the even functions $a _ { 0 } + a _ { 2 } x ^ { 2 }$ to take on arbitrary values at distinct points.

Ex.2. The strength of Theorem 2.1.1 is brought out by noting that it cannot be extended as it stands to polynomial interpolation in several variables.Let the powers in two real variables be listed as follows: $p _ { \mathbf { 0 } } ( x , y ) = 1$ ， $p _ { 1 } ( x , y ) = x$ ， $p _ { 2 } ( x , y ) = y ;$ $p _ { 3 } ( x , y ) = x ^ { 2 }$ ， $p _ { 4 } ( x , y ) = x y$ ， $p _ { 5 } ( x , y ) = y ^ { 2 }$ ， $p _ { 6 } ( x , y ) = x ^ { 3 }$ .... It is not always possible,having been given $_ n$ arbitrary distinct points $( x _ { i } , y _ { i } )$ ，to find a linear combination of $p _ { 0 } , \ldots , p _ { n - 1 }$ that takes on preassigned values at these points.

2.3 Systems Possessing the Interpolation Property. Many spaces offunctions and related systems of independent functionals are known and have been studied in detail. We shall list some of the more common ones.

Ex.1. (Interpolation at discrete points)

$$
X = { \mathcal { P } } _ { n } . \quad L _ { 0 } ( f ) = f ( z _ { 0 } ) , L _ { 1 } ( f ) = f ( z _ { 1 } ) , . . . , L _ { n } ( f ) = f ( z _ { n } ) .
$$

We assume that $z _ { i } \neq z _ { j } , i \neq j$

Ex.2． (Taylor interpolation)

$$
X = { \mathcal { P } } _ { n } . \quad L _ { 0 } ( f ) = f ( z _ { 0 } ) , L _ { 1 } ( f ) = f ^ { \prime } ( z _ { 0 } ) , . . . , L _ { n } ( f ) = f ^ { ( n ) } ( z _ { 0 } ) .
$$

Ex.3. (Abel-Gontscharoff Interpolation)

$$
X = \mathcal { P } _ { n } . \quad L _ { 0 } ( { f } ) = f ( z _ { 0 } ) , L _ { 1 } ( { f } ) = f ^ { \prime } ( z _ { 1 } ) , L _ { 2 } ( { f } ) = f ^ { \prime \prime } ( z _ { 2 } ) , \dots , L _ { n } ( { f } ) = f ^ { ( n ) } ( z _ { n } ) .
$$

Ex.4.(Lidstone Interpolation)

$$
\begin{array} { r l } { X = \mathcal { P } _ { 2 n + 1 } . } & { L _ { 1 } ( f ) = f ( z _ { 0 } ) , L _ { 2 } ( f ) = f ( z _ { 1 } ) } \\ & { L _ { 3 } ( f ) = f ^ { \prime \prime } ( z _ { 0 } ) , L _ { 4 } ( f ) = f ^ { \prime \prime } ( z _ { 1 } ) } \\ & { . } \\ & { . } \end{array}
$$

$$
L _ { 2 n + 1 } ( f ) = f ^ { ( 2 n ) } ( z _ { 0 } ) , L _ { 2 n + 2 } ( f ) = f ^ { ( 2 n ) } ( z _ { 1 } ) , ( z _ { 0 } \ne z _ { 1 } ) .
$$

Ex.5. (Simple Hermite or Osculatory Interpolation)

$$
\begin{array} { r l r } { X = \mathcal { P } _ { 2 n - 1 } . } & { } & { L _ { 1 } ( f ) = f ( z _ { 1 } ) , L _ { 2 } ( f ) = f ^ { \prime } ( z _ { 1 } ) } \\ & { } & { L _ { 3 } ( f ) = f ( z _ { 2 } ) , L _ { 4 } ( f ) = f ^ { \prime } ( z _ { 2 } ) } \\ & { } & { . } \\ & { } & { . } \end{array}
$$

$$
L _ { 2 n - 1 } ( f ) = f ( z _ { n } ) , L _ { 2 n } ( f ) = f ^ { \prime } ( z _ { n } ) , ( z _ { i } \ne z _ { j } , i \ne j ) .
$$

Ex.6． (Full Hermite Interpolation) $\boldsymbol { X } = \mathcal { P } _ { N }$ ，To avoid indexing difficulties,we list the functional information employed without using the symbol $L$ ·

$$
\begin{array} { l } { f ( z _ { n } ) , f ^ { \prime } ( z _ { n } ) , \ldots , f ^ { ( m _ { n } ) } ( z _ { n } ) } \\ { \quad ( z _ { i } \ne z _ { j } , N = m _ { 0 } + m _ { 1 } + \cdot \cdot \cdot + m _ { n } + n ) . } \end{array}
$$

Ex.7． (Generalized Taylor Interpolation) $x$ consists of the linear combinations of the $n + 1$ linearly independent functions $\varphi _ { \bf 0 } ( z ) , \varphi _ { \bf 1 } ( z ) , \ldots , \varphi _ { n } ( z )$ that are analytic at $z _ { \mathbf { 0 } }$

$$
\begin{array} { r l } & { L _ { \bf 0 } ( f ) = f ( z _ { \bf 0 } ) , L _ { \bf 1 } ( f ) = f ^ { \prime } ( z _ { \bf 0 } ) , \ldots , } \\ & { } \\ & { L _ { \bf n } ( f ) = f ^ { ( n ) } ( z _ { \bf 0 } ) . } \end{array}
$$

$$
\vert \varphi _ { i } ^ { ( j ) } ( z _ { 0 } ) \vert \neq 0 .
$$

Ex.8． (Trigonometric Interpolation)

A linear combination of 1,cos $_ x$ ...,cos $_ { n x }$ ，sin $_ x$ sin $\mathbf { 2 } x$ ....,sin nx is known as a trigonometric polynomial of degree $\leq n$ . The corresponding linear space will be designated by $\mathcal { T } _ { n }$ .It has dimension $2 n \mathrm { ~ + ~ } 1$

$$
\begin{array} { r l } { X = \mathcal { T } _ { n } . \ } & { L _ { 0 } ( f ) = f ( x _ { 0 } ) , L _ { 1 } ( f ) = f ( x _ { 1 } ) , . . . , L _ { 2 n } ( f ) = f ( x _ { 2 n } ) , } \\ & { - \pi \leq x _ { 0 } < x _ { 1 } < \cdot \cdot \cdot < x _ { 2 n } < \pi . } \end{array}
$$

Ex.9． (Fourier Series)

$$
\begin{array} { r l } { X = \mathcal { T } _ { n } . \quad L _ { 2 k } ( f ) = \displaystyle \int _ { - \pi } ^ { \pi } f ( x ) \cos k x d x , k = 0 , 1 , \ldots , n . } & { } \\ { L _ { 2 k - 1 } ( f ) = \displaystyle \int _ { - \pi } ^ { \pi } f ( x ) \sin k x d x , k = 1 , 2 , \ldots , n . } & { } \end{array}
$$

Before demonstrating that these functionals are independent over the respective spaces,a few remarks are in order.Ex.1 is,of course,Theorem 2.1.1.Exs.1,2,5 are special cases of Ex. 6. Ex.2 is a special case of Ex.7 if we select $\varphi _ { k } ( z ) = z ^ { k }$ .Ex.9 is not generally thought of as an interpolation process since the usual interpolatory processes make use of point data.But it—and indeed all orthogonal expansions-fit into the present pattern,and so we have listed it here.

The most direct way to show that the interpolation problem formed from these examples has a solution is to exhibit the solution explicitly.For some of the examples,we shall do this in subsequent sections.But it suffces to show that the generalized Gram determinant does not vanish,(2.2.2),or to apply the Alternative Theorem 1.2.2 directly.

Ex.6.We shall show that if $\mathcal { P } \in \mathcal { P } _ { N }$ and satisfies

$$
\begin{array} { r l r } { \ } & { } & { p ( z _ { 0 } ) = 0 , p ^ { \prime } ( z _ { 0 } ) = 0 , \ldots , p ^ { m _ { 0 } } ( z _ { 0 } ) = 0 } \\ { \ } & { } & { p ( z _ { 1 } ) = 0 , p ^ { \prime } ( z _ { 1 } ) = 0 , \ldots , p ^ { m _ { 1 } } ( z _ { 1 } ) = 0 } \\ { \ } & { } & { \cdot } \\ { \ } & { } & { \cdot } \\ { \cdot } & { } & { \cdot } \\ { \ } & { } & { p ( z _ { , n } ) = 0 , p ^ { \prime } ( z _ { n } ) = 0 , \ldots , p ^ { m _ { n } } ( z _ { n } ) = 0 } \end{array}
$$

where $N = m _ { 0 } + m _ { 1 } + \cdot \cdot \cdot + m _ { n } + n$ ，then $\mathscr { p }$ must vanish identically.By the Factorization Theorem,if $\pmb { p }$ satisfies all conditions of (2.3.1) with the exception of the last, i.e., $p ^ { m _ { n } } ( z _ { n } ) = 0$ ,then we must have

$$
p ( z ) = A ( z ) ( z - z _ { 0 } ) ^ { m _ { 0 } + 1 } ( z - z _ { 1 } ) ^ { m _ { 1 } + 1 } \cdot \cdot \cdot ( z - z _ { n - 1 } ) ^ { m _ { n - 1 } + 1 } ( z - z _ { n } ) ^ { m _ { n } } ,
$$

A(z) = polynomial.

By examining the degree of this product, it appears that $A =$ constant. Since, moreover,

$$
p ^ { ( m _ { n } ) } ( z _ { n } ) = A ( m _ { n } ) ! ( z _ { n } - z _ { 0 } ) ^ { m _ { 0 } + 1 } \cdot \cdot \cdot ( z _ { n } - z _ { n - 1 } ) ^ { m _ { n - 1 } + 1 } = 0
$$

and ${ \pmb z } _ { i } \neq { \pmb z } _ { j } , \ i \neq j ,$ ，we have $ { \textbf { A } } = 0$ and therefore ${ \boldsymbol { \mathscr { p } } } \equiv 0$ ．The homogeneous interpolation problem has the zero solution only and hence the nonhomogeneous problem possesses a unique solution.

Ex.3. The generalized Gram determinant is

$$
\scriptstyle { \begin{array} { l } { { \begin{array} { l l l l l } { \scriptstyle 1 } & { \ z _ { 0 } } & { \ z _ { 0 } ^ { \ 2 } \cdot \cdot \cdot \ z _ { 0 } ^ { n } } \\ { \scriptstyle 0 } & { \ 1 } & { \ 2 z _ { 1 } \cdot \cdot \cdot n z _ { 1 } ^ { n - 1 } } \\ { \scriptstyle 0 } & { \ 0 } & { \ 2 \ \cdot \cdot \cdot \ n ( n - 1 ) z _ { 2 } ^ { n - 2 } } \\ { \scriptstyle \cdot } & { \ } & { \ \cdot } \\ { \scriptstyle \cdot } & { \ } & { \ \cdot } \\ { \scriptstyle \cdot } & { \ } & { \ \cdot } \\ { \scriptstyle 0 } & { \ 0 } & { \ 0 } & { \ \cdot \cdot \ n ! } \end{array} } } \end{array} } = 1 ! \ \ 2 ! \cdot \cdot \cdot n ! \ \neq 0 .
$$

Ex.4.Let $\boldsymbol { p } \in \mathscr { P } _ { 2 n + 1 }$ .If $p ^ { ( 2 j ) } ( z _ { 0 } ) = 0$ for $j = 0 , 1 , \ldots , n$ ，then by Theorem 1.6.4， $p ( z ) = a _ { 1 } ( z - z _ { 0 } ) + a _ { 3 } ( z - z _ { 0 } ) ^ { 3 } + \cdot \cdot \cdot + a _ { 2 n + 1 } ( z - z _ { 0 } ) ^ { 2 n + 1 }$ Ifnow, $p ^ { ( 2 n ) } ( z _ { 1 } ) = 0$ then $a _ { 2 n + 1 } = 0$ and $p ^ { ( 2 j ) } ( z _ { 1 } ) = 0 , j = n \ - 1 , n \ - \ 2 , . \ . \ . \ , 0$ implies, by recurrence,that the remaining coefficients are O.The homogeneous problem possesses the O solution only,and so the nonhomogeneous problem has a solution and it is unique.

As far as Ex.7 is concerned,no proof is required,for condition (2.2.2) has been built into the hypothesis.In this example,the crucial determinant reduces to the Wronskian of the functions $\phi _ { 0 } , \ldots , \phi _ { n }$ and we postulate that it does not vanish at ${ \pmb z _ { 0 } }$

Ex.8. The crucial determinant here is

$$
\begin{array} { r } { G = \left[ \begin{array} { l l l l l l l } { 1 . \cos x _ { 0 } } & { \sin x _ { 0 } } & { \cos 2 x _ { 0 } } & { \sin 2 x _ { 0 } } & { \cdot \cdot \cdot \cos n x _ { 0 } } & { \sin n x _ { 0 } } \\ { 1 } & { \cos x _ { 1 } } & { \sin x _ { 1 } } & { \cos 2 x _ { 1 } } & { \sin 2 x _ { 1 } } & { \cdot \cdot \cdot } & { \cos n x _ { 1 } } & { \sin n x _ { 1 } } \\ { . } & { } & { } & { } & { \cdot } & { } \\ { . } & { } & { } & { } & { \cdot } & { } \\ { . } & { } & { } & { } & { } & { \cdot } \\ { 1 } & { \cos x _ { 2 n } } & { \sin x _ { 2 n } } & { \cos 2 x _ { 2 n } } & { \sin 2 x _ { 2 n } } & { \cdot \cdot \cdot } & { \cos n x _ { 2 n } } & { \sin n x _ { 2 n } } \end{array} \right] . } \end{array}
$$

To evaluate $G$ we reduce its elements to complex form. Multiply the 3rd, 5th,... columns by $\mathbf { \chi } _ { i } ^ { \star }$ and add them respectively to the 2nd,4th,...columns.We obtain

$$
G \ = \ | 1 e ^ { i x _ { j } } \sin x _ { j } e ^ { 2 i x _ { j } } \sin 2 x _ { j } . . . e ^ { n i x _ { j } } \sin n x _ { j } | .
$$

Multiply the 3rd, 5th,...columns by $- 2 i$ and to them add the 2nd, 4th,...

columns respectively:

$$
( - 2 i ) ^ { n } G = | 1 e ^ { i x _ { j } } e ^ { - i x _ { j } } e ^ { 2 i x _ { j } } e ^ { - 2 i x _ { j } } . \cdot \cdot \cdot e ^ { n i x _ { j } } e ^ { - n i x _ { j } } | .
$$

Interchange the columns:

$$
( - 1 ) ^ { n ( n + 1 ) } ( - 2 i ) ^ { n } G = \big | e ^ { - n i x _ { j } } e ^ { - ( n - 1 ) i x _ { j } } \cdot \cdot \cdot 1 \cdot \cdot e ^ { ( n - 1 ) i x _ { j } } e ^ { n i x _ { j } } \big | .
$$

Multiply the jth row by $e ^ { n i x _ { j } } , j = 0 , . . . , 2 n$ ：

$$
e ^ { n i ( x _ { o } + x _ { 1 } + \cdots + x _ { 2 n } ) } ( - 1 ) ^ { n ( n + 1 ) } ( - 2 i ) ^ { n } { \cal G } = | 1 e ^ { i x _ { j } } e ^ { 2 i x _ { j } } \cdots e ^ { 2 n i x _ { j } } | .
$$

The determinant in the last line is a Vandermonde. Hence from (2.1.8),

$$
e ^ { n i ( x _ { 0 } + x _ { 1 } + \cdots + x _ { 2 n } ) } ( - 1 ) ^ { n ( n + 1 ) } ( - 2 i ) ^ { n } { \cal G } \ = \ \prod _ { j > k } ^ { 2 n } \ ( e ^ { i x _ { j } } - e ^ { i x _ { k } } ) .
$$

In view of the conditions on the $x _ { j } , e ^ { i x _ { j } } \neq e ^ { i x _ { k } } , j \neq k _ { \mathrm { ; } }$ and so $G \neq 0$

Ex.9.In view of the orthogonality of the sines and cosines (Chap. 8.3, Ex.3),the crucial determinant has positive quantities on the main diagonal and O's elsewhere and hence does not vanish.

2.4 Unisolvence. Let the functions $f _ { 1 } ( x ) , f _ { 2 } ( x ) , \ldots , f _ { n } ( x )$ be defined on an interval $\pmb { I }$ Given $\pmb { n }$ distinct points $x _ { 1 } , \dotsc , x _ { n } \in I$ and $\pmb { n }$ values $w _ { 1 } , . . . ,$ $w _ { n }$ ,we will be able to solve uniquely the interpolation problem

$$
\sum _ { i = 0 } ^ { n } a _ { i } f _ { i } ( x _ { j } ) = w _ { j } \qquad j = 1 , 2 , \ldots , n
$$

if and only if

$$
| f _ { i } ( x _ { j } ) | \neq 0 .
$$

DEFINITION 2.4.1． A system of $\pmb { n }$ functions $f _ { 1 } , \ldots , f _ { n }$ defined on a point set $s$ is called unisolvent on $\pmb { S }$ if (2.4.2) holds for every selection of $\pmb { n }$ distinct points lying in $\pmb { S }$

Pointwise interpolation can always be carried out uniquely with a unisolvent system.

It follows that $f _ { 1 } , \ldots , f _ { n }$ is unisolvent on $\pmb { S }$ if and only if the only linear combination of the $f ^ { ; }$ sthat vanishes on $\pmb { n }$ distinct points of $\pmb { S }$ vanishes identically.

Ex.1．The system 1, $\pmb { x ^ { 2 } }$ is unisolvent on [0,1] but not on[-1,1].

Ex. 2. The system $1 , x , x ^ { 2 } , \ldots , x ^ { n }$ is unisolvent over any interval $[ a , b ]$ ·

Ex.3.Suppose that ${ \pmb w } ( { \pmb x } )$ does not vanish on $[ a , b ]$ . Then

$$
w ( x ) , x w ( x ) , x ^ { 2 } w ( x ) , \textrm { . . . , } x ^ { n } w ( x )
$$

is unisolvent on $[ a , b ]$

Ex. 4. The system of complex powers $1 , z , z ^ { 2 } , \ldots , z ^ { n }$ is unisolvent over any region.

Ex.5. The trigonometric system

1, cos $_ { \pmb { x } }$ cos $\mathbf { 2 } x$ ...,cos $_ { n x }$ ,sin $_ x$ sin $\pmb { 2 x }$ ....,sin nx

is unisolvent on $- \pi \leq x < \pi$

Ex.6.Let $\pmb { a } _ { i }$ be distinct values not in $[ \pmb { a } , \pmb { b } ]$ .Then the system

$$
{ \frac { 1 } { x \ + a _ { 1 } } } , { \frac { 1 } { x \ + a _ { 2 } } } , \ \ldots \ , { \frac { 1 } { x \ + a _ { n } } }
$$

is unisolvent in $[ a , b ]$ .For we shall prove in Chap.I1.3 that

$$
\left| { \frac { 1 } { x _ { i } + a _ { j } } } \right| = \prod _ { i > j } ^ { n } ( x _ { i } - x _ { j } ) ( a _ { i } - a _ { j } ) \left/ \prod _ { i , j = 1 } ^ { n } ( x _ { i } + a _ { j } ) . \right.
$$

As far as functions of one variable are concerned,unisolvent systems are reasonably plentiful.In several dimensions,the situation is vastly different. We have already had a hint of this in 2.2,Ex.2 where we noticed that the fundamental theorem of polynomial interpolation does not go over directly to several variables.

THEOREM 2.4.1 (Haar).Let $s$ be a point set in a Euclidean space of $\pmb { n }$ dimension, $\scriptstyle { R _ { n } }$ ， $\mathscr { n } \geq 2$ Suppose that $s$ contains an interior point $\pmb { p }$ Let $f _ { 1 } , f _ { 2 } , \ldots , f _ { n } ( n > 1 )$ be defined on $\pmb { S }$ and continuous in $^ { \pmb { a } }$ neighborhood of $\pmb { p }$ Then this set of functions cannot be unisolvent on $\pmb { S }$

Proof: Let $\boldsymbol { U }$ be a ball with center at $\pmb { p }$ and contained in $\pmb { S }$ and sufficiently small so that the $f _ { i }$ are continuous in $\boldsymbol { U }$ .Select $\pmb { n }$ distinct points $p _ { 1 } , p _ { 2 } , \ldots ,$ ${ \pmb { p } } _ { \pmb { n } } \in U$ .We may assume that $| f _ { i } ( p _ { j } ) | \neq 0$ ,for otherwise the system is surely not unisolvent.Hold the points $p _ { 3 } , p _ { 4 } , \ldots , p _ { n }$ fixed. Now move the points ${ \pmb p _ { 1 } }$ and ${ \pmb p _ { \mathbf { 2 } } }$ continuously through $\boldsymbol { U }$ in such a manner that the positions of $\pmb { p _ { 1 } }$ and ${ \pmb p _ { 2 } }$ are interchanged. Since $\boldsymbol { U }$ has dimension $\geq 2$ ,it is clear that this can be carried out in such a manner that $\pmb { p _ { 1 } }$ and ${ \pmb p _ { \mathbf { 2 } } }$ coincide neither with one another nor with the remaining points.In this way we induce an interchange of two columns of the determinant $| f _ { i } ( \pmb { p } _ { j } ) |$ .Its sign therefore changes. Since the functions are continuous,there must be some intermediate position of ${ \pmb p _ { 1 } }$ and ${ \pmb p _ { 2 } }$ for which the value of the determinant is zero.

In order to carry out this argument,it is not necessary to have an interior point.It suffices if the set $\pmb { S }$ contains a “ramification point;” that is to say, a point $\pmb { p }$ at which three arcs meet.Then by a process of“train switching" we may carry out the same argument.It is surprising that unisolvence has this topological aspect.

![](../chunks/Interpolation and Approximation (Philip J. Davis) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0070/auto/images/30f2974ac4d256836f919bd8c0932cff177349e83a8c57d6b1be990b79bc06e2.jpg)  
Figure 2.4.1.

2.5 Representation Theorems: The Lagrange Formula. Let $z _ { \mathbf { 0 } } ,$ $z _ { 1 } , \ldots , z _ { n }$ be distinct and introduce the following polynomials of degree $\pmb { n }$

$$
l _ { k } ( z ) = { \frac { ( z - z _ { 0 } ) ( z - z _ { 1 } ) \cdot \cdot \cdot ( z - z _ { k - 1 } ) ( z - z _ { k + 1 } ) \cdot \cdot \cdot ( z - z _ { n } ) } { ( z _ { k } - z _ { 0 } ) ( z _ { k } - z _ { 1 } ) \cdot \cdot \cdot ( z _ { k } - z _ { k - 1 } ) ( z _ { k } - z _ { k + 1 } ) \cdot \cdot \cdot ( z _ { k } - z _ { n } ) } } ,
$$

It is clear that

$$
l _ { k } ( z _ { j } ) = \delta _ { k j } = { \binom { 0 { \mathrm { ~ i f ~ } } k \neq j } { 1 { \mathrm { ~ i f ~ } } k = j } } .
$$

For given values $w _ { 0 } , w _ { 1 } , \ldots , w _ { n }$ ，the polynomial

$$
p _ { n } ( z ) = \sum _ { k = 0 } ^ { n } w _ { k } l _ { k } ( z )
$$

is in $\mathcal { P } _ { \pmb { n } }$ and takes on these values at the points $z _ { i }$

$$
p _ { n } ( z _ { k } ) = w _ { k } \qquad k = 0 , 1 , \ldots , n .
$$

Formula (2.5.3) is the Lagrange Interpolation Formula. Since the interpolation problem (2.5.4) has a unique solution,all other representations of the solution must, upon rearrangement of terms, coincide with the Lagrange polynomial.

An alternate form is useful.Introduce

$$
w ( z ) = ( z - z _ { 0 } ) ( z - z _ { 1 } ) \cdot \cdot \cdot ( z - z _ { n } ) .
$$

Then,

$$
w ^ { \prime } ( z _ { k } ) = ( z _ { k } - z _ { 0 } ) ( z _ { k } - z _ { 1 } ) \cdot \cdot \cdot ( z _ { k } - z _ { k - 1 } ) ( z _ { k } - z _ { k + 1 } ) \cdot \cdot \cdot ( z _ { k } - z _ { n } )
$$

and hence from (2.5.1),

$$
l _ { k } ( z ) = \frac { w ( z ) } { ( z - z _ { k } ) w ^ { \prime } ( z _ { k } ) } .
$$

The formula (2.5.3) becomes

$$
p _ { n } ( z ) = \sum _ { k = 0 } ^ { n } w _ { k } \frac { w ( z ) } { ( z - z _ { k } ) w ^ { \prime } ( z _ { k } ) } .
$$

The polynomials $l _ { k } ( z )$ are called the fundamental polynomials for pointwise interpolation.

The numbers $w _ { i }$ are frequently the values of some function $f ( z )$ at the points $z _ { i }$ ： $w _ { i } = f ( z _ { i } )$ . The polynomial $\scriptstyle { \pmb { p } } _ { \pmb { n } } ( z )$ given by (2.5.8) and formed with these w's coincides with the function $f ( z )$ at the points $z _ { 0 } , z _ { 1 } , \ldots , z _ { n } .$ That is,if

$$
p _ { n } ( z ) = \sum _ { k = 0 } ^ { n } f ( z _ { k } ) l _ { k } ( z ) = \sum _ { k = 0 } ^ { n } f ( z _ { k } ) { \frac { w ( z ) } { ( z - z _ { k } ) w ^ { \prime } ( z _ { k } ) } } ,
$$

then

$$
p _ { n } ( z _ { k } ) = f ( z _ { k } ) \qquad k = 0 , 1 , \ldots , n .
$$

DEFINITIon 2.5.1. We shall designate the unique polynomial of class $\mathcal { P } _ { n }$ that coincides with $f$ at $z _ { 0 } , \ldots , z _ { n }$ by $p _ { n } ( f ; z )$

Suppose that $q ( z ) \in \mathcal { P } _ { n }$ .Then $\pmb q$ is uniquely determined by the $n + 1$ values $q ( z _ { i } ) , i = 0 , \ldots , n$ .Hence we must have

$$
p _ { n } ( q ; z ) \equiv q ( z ) .
$$

Now take $q ( z ) = ( z - u ) ^ { j }$ ， $j = 0 , 1 , \ldots , n$ and regard $\textbf { \em u }$ as an independent variable.From (2.5.1l) and (2.5.9),

$$
( z - u ) ^ { j } = \sum _ { k = 0 } ^ { n } ( z _ { k } - u ) ^ { j } l _ { k } ( z ) \qquad j = 0 , 1 , \ldots , n
$$

holding identically in $\textit { \textbf { z } }$ and $\textbf { \em u }$

By selecting $u = z$ we obtain

$$
\begin{array} { c } { { \displaystyle \sum _ { k = 0 } ^ { n } l _ { k } ( z ) \equiv 1 } } \\ { { \sum _ { k = 0 } ^ { n } ( z _ { k } - z ) ^ { j } l _ { k } ( z ) \equiv 0 , j = 1 , 2 , . . . , n . } } \end{array}
$$

The $\pm 1$ identities (2.5.l3) are the Cauchy relations for the fundamental polynomials $l _ { k } ( z )$

The importance of the fundamental polynomials lies in the identity (2.5.2) and the resulting simple explicit solution (2.5.9) of the interpolation problem.If we set

$$
L _ { 0 } ( f ) = f ( z _ { 0 } ) , \ L _ { 1 } ( f ) = f ( z _ { 1 } ) , \ldots , L _ { n } ( f ) = f ( z _ { n } ) ,
$$

then (2.5.2) can be written as

$$
\begin{array} { r } { L _ { i } ( l _ { j } ) = \delta _ { i j } . } \end{array}
$$

In anticipation of certain geometric developments in Chapter VII, we willsay that the polynomials $l _ { i } ( z )$ and the functionals $L _ { i }$ are biorthonormal. For a given set of independent functionals,we can always find a related biorthonormal set of polynomials.Indeed,we have the following generalization of Lagrange's formula.

THEOREM 2.5.1. Let $\pmb { X }$ be $^ { \pmb { a } }$ linear space of dimension $\pmb { n }$ Let $L _ { 1 } , L _ { 2 } , \dots ,$ $L _ { n }$ be $\pmb { n }$ independent functionals in $X ^ { * }$ .Then,there are determined uniquely $\pmb { n }$ independent elements of $X , x _ { 1 } { ^ * } , x _ { 2 } { ^ * } , \dotsb , x _ { n } { ^ * }$ such that

$$
L _ { i } ( x _ { j } { } ^ { * } ) = \delta _ { i j } .
$$

For any ${ \boldsymbol { x } } \in X$ we have

$$
{ \pmb x } = \sum _ { i = 1 } ^ { n } L _ { i } ( { \pmb x } ) x _ { i } ^ { \ast } .
$$

For every choice of $w _ { 1 } , \ldots , w _ { n } $ the element

$$
{ \pmb x } = \sum _ { i = 1 } ^ { n } w _ { i } { x _ { i } } ^ { * }
$$

is the unique solution of the interpolation problem

$$
L _ { i } ( x ) = w _ { i } , \qquad i = 1 , 2 , \ldots , n .
$$

Pro0f: Let $x _ { 1 } , \ldots , x _ { n }$ be a basis for $\pmb { X }$ .By Lemma 2.2.1, $| L _ { i } ( x _ { j } ) | \neq 0$ If we set ${ x _ { j } } ^ { * } = a _ { j 1 } x _ { 1 } + \cdot \cdot \cdot + a _ { j n } x _ { n }$ ，then this determinant condition guarantees that the system (2.5.15) can be solved for $\pmb { a } _ { j _ { i } }$ to produce a set of elements ${ x _ { 1 } } ^ { * } , \ldots , { x _ { n } } ^ { * }$ .By Theorem 2.2.2,the solution to the interpolation problem (2.5.15) is unique,for each $j$ ，and by Lemma 2.2.1,the ${ \pmb x } _ { i } ^ { * }$ are independent.

Denote $\stackrel { \mathrm { \scriptsize ~ . ~ . ~ } } { y } = \sum _ { i = 1 } ^ { n } { L _ { i } ( x ) { x _ { i } } ^ { * } }$ . Then $L _ { j } ( y ) = \sum _ { i = 1 } ^ { n } L _ { i } ( x ) L _ { j } ( x _ { i } { ^ { * } } )$ . Hence,by (2.5.15), $L _ { j } ( y ) = L _ { j } ( x ) , j = 1 , 2 , . . . , n$ 、Again,since interpolation with the $\pmb { n }$ conditions $L _ { i }$ is unique, $y = x$ and this establishes (2.5.16). Equation (2.5.18) is established similarly.

In this theorem and throughout the remainder of the book an asterisk $( ^ { * } )$ will be applied to the symbol of an element whenever the element is one of a biorthonormal or an orthonormal set. (Cf.Def. 8.3.1.) An asterisk on the symbol of a space will be used to denote the conjugate space. (Cf.Def.1.12.3.)

The solution to the interpolation problem (2.5.lS)can be given in determinantal form.

THEOREM 2.5.2. Let the hypotheses of Theorem 2.5.1 hold and let $\pmb { x } _ { 1 } , \ldots , .$ ${ \pmb x } _ { \pmb n }$ be $^ { \pmb { a } }$ basis for $\pmb { X }$ .If $w _ { 1 } , \ldots , w _ { n }$ are arbitrary numbers then the element

$$
x = - { \frac { 1 } { G } } { \left| \begin{array} { l l l l l } { 0 } & { x _ { 1 } } & { x _ { 2 } } & { \cdots } & { x _ { n } } \\ { w _ { 1 } } & { L _ { 1 } ( x _ { 1 } ) } & { L _ { 1 } ( x _ { 2 } ) \cdots L _ { 1 } ( x _ { n } ) } \\ { . } & { . } & { . } & { . } \\ { . } & { . } & { . } & { . } \\ { . } & { . } & { . } & { . } \\ { w _ { n } } & { L _ { n } ( x _ { 1 } ) } & { L _ { n } ( x _ { 2 } ) \ldots L _ { n } ( x _ { n } ) } \end{array} \right| }
$$

satisfies $L _ { i } ( x ) = w _ { i } , i = 1 , 2 , \ldots , n .$

Proof:It is clear that $_ { \pmb { x } }$ is a linear combination of $x _ { 1 } , \ldots , x _ { n }$ and hence is in $X$ .Furthermore,we have

$$
\begin{array} { r } { L _ { j } ( x ) = - \frac { 1 } { G } \left| \begin{array} { c c c c } { 0 } & { L _ { j } ( x _ { 1 } ) } & { L _ { j } ( x _ { 2 } ) } & { \cdots \cdot L _ { j } ( x _ { n } ) } \\ { w _ { 1 } } & { L _ { 1 } ( x _ { 1 } ) } & { L _ { 1 } ( x _ { 2 } ) \cdots L _ { 1 } ( x _ { n } ) } \\ { \cdot } & { \cdot } & { \cdot } & { \cdot } \\ { \cdot } & { \cdot } & { \cdot } & { \cdot } \\ { \cdot } & { \cdot } & { \cdot } & { \cdot } \\ { w _ { j } } & { L _ { j } ( x _ { 1 } ) } & { L _ { j } ( x _ { 2 } ) } & { \cdots \cdot L _ { j } ( x _ { n } ) } \\ { \cdot } & { \cdot } & { \cdot } & { \cdot } \\ { \cdot } & { \cdot } & { \cdot } & { \cdot } \\ { \cdot } & { \cdot } & { \cdot } & { \cdot } \\ { w _ { n } } & { L _ { n } ( x _ { 1 } ) } & { L _ { n } ( x _ { 2 } ) \cdots L _ { n } ( x _ { n } ) } \end{array} \right| . } \end{array}
$$

Expand this determinant by minors of the lst column. The minor of each nonzero element,with the exception of $w _ { j }$ ,is O,for it contains two identical rows. The cofactor of $w _ { j }$ is $- G$ Hence, $L _ { j } ( x ) = w _ { j } , j = 1 , 2 , . . . , n .$

Ex.1． (Taylor Interpolation)

The polynomials ${ \frac { z ^ { n } } { n ! } } , n = 0 , 1 , \ldots$ ，and the functionals $L _ { n } ( f ) = f ^ { ( n ) } ( 0 ) , n =$ $0 , 1 , \ldots$ ,are biorthonormal.

![](../chunks/Interpolation and Approximation (Philip J. Davis) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0070/auto/images/82f1acd77e80c7445a6cd1a4048876ea493678f965acec9286c4173030da73d9.jpg)  
Figure 2.5.1 Osculatory Interpolation at Two Points

$$
p ( x ) = \textstyle { \frac { 3 } { 4 } } - \frac { 1 } { 4 } x ^ { 2 } , \qquad f ( x ) = \frac { 1 } { 1 + x ^ { 2 } }
$$

$$
\begin{array} { r l } { p ( + 1 ) = f ( + 1 ) , \quad } & { { } p ^ { \prime } ( + 1 ) = f ^ { \prime } ( + 1 ) } \\ { p ( - 1 ) = f ( - 1 ) , \quad } & { { } p ^ { \prime } ( - 1 ) = f ^ { \prime } ( - 1 ) . } \end{array}
$$

Ex.2. (Osculatory Interpolation)

$$
w ( z ) = ( z - z _ { 1 } ) ( z - z _ { 2 } ) \cdot \cdot \cdot ( z - z _ { n } ) , l _ { k } ( z ) = \frac { w ( z ) } { ( z - z _ { k } ) w ^ { \prime } ( z _ { k } ) } .
$$

The polynomials $\left[ 1 - \frac { w ^ { \prime \prime } ( z _ { k } ) } { w ^ { \prime } ( z _ { k } ) } ( z - z _ { k } ) \right] { l _ { k } } ^ { 2 } ( z ) , ( z - z _ { k } ) { l _ { k } } ^ { 2 } ( z )$ of degree $2 n \mathrm { ~ - ~ } 1$ and the functionals

$$
L _ { k } ( f ) = f ( z _ { k } ) , M _ { k } ( f ) = f ^ { \prime } ( z _ { k } ) , \qquad k = 1 , 2 , \ldots , n
$$

are biorthonormal.

The resulting expansion of type (2.5.17) is, therefore,

$$
p _ { 2 n - 1 } ( z ) = \sum _ { k = 1 } ^ { n } w _ { k } \left[ 1 - \frac { w ^ { \prime \prime } ( z _ { k } ) } { w ^ { \prime } ( z _ { k } ) } ( z - z _ { k } ) \right] { l _ { k } } ^ { 2 } ( z ) + \sum _ { k = 1 } ^ { n } { w _ { k } } ^ { \prime } ( z - z _ { k } ) { l _ { k } } ^ { 2 } ( z ) ,
$$

and produces the unique element of $\mathscr { P } _ { 2 n - 1 }$ which solves the “osculatory” interpolation problem

$$
\begin{array} { c c } { { p ( z _ { k } ) = w _ { k } } } & { { } } \\ { { { } } } & { { { } } } \\ { { p ^ { \prime } ( z _ { k } ) = w _ { k } { } ^ { \prime } } } & { { { } } } \end{array} \quad k = 1 , 2 , . . . , n .
$$

Ex.3． (Two Point Taylor Interpolation) Let $^ { a }$ and $^ { b }$ be distinct points.The polynomial

$$
\begin{array} { c } { { \displaystyle p _ { 2 n - 1 } ( z ) ~ = ~ ( z ~ - ~ a ) ^ { n } \sum _ { k = 0 } ^ { 1 } \frac { B _ { k } ( z ~ - ~ b ) ^ { k } } { k ! } ~ + ~ ( z ~ - ~ b ) ^ { n } \sum _ { k = 0 } ^ { n - 1 } \frac { A _ { k } ( z ~ - ~ a ) ^ { k } } { k ! } ~ } } \\ { { { } ~ } } \\ { { { \cal A } _ { k } ~ { = } ~ { \displaystyle \frac { d ^ { k } } { d z ^ { k } } } \biggl [ \frac { f ( z ) } { ( z ~ - ~ b ) ^ { n } } \biggr ] _ { z = a } } } \\ { { { } ~ } } \\ { { { \cal B } _ { k } ~ { = } ~ { \displaystyle \frac { d ^ { k } } { d z ^ { k } } } \biggl [ \frac { f ( z ) } { ( z ~ - ~ a ) ^ { n } } \biggr ] _ { z = b } } } \end{array}
$$

is the unique solution in $\mathscr { P } _ { 2 n - 1 }$ of the interpolation problem

$$
\begin{array} { r l } & { p _ { 2 n - 1 } ( a ) = f ( a ) , p _ { 2 n - 1 } ^ { \prime } ( a ) = f ^ { \prime } ( a ) , \ldots , p _ { 2 n - 1 } ^ { ( n - 1 ) } ( a ) = f ^ { ( n - 1 ) } ( a ) \ } \\ & { p _ { 2 n - 1 } ( b ) = f ( b ) , p _ { 2 n - 1 } ^ { \prime } ( b ) = f ^ { \prime } ( b ) , \ldots , p _ { 2 n - 1 } ^ { ( n - 1 ) } ( b ) = f ^ { ( n - 1 ) } ( b ) . } \end{array}
$$

Ex.4． Exs.1,2,3 are,of course,special cases of the general Hermite interpolation problem. (Cf.Ex.6, 2.3.) Let $z _ { 1 } , z _ { 2 } , \ldots , z _ { n }$ be $\pmb { n }$ distinct points, $\alpha _ { 1 } , \ldots , \alpha _ { n }$ be $\pmb { n }$ integers $\geq 1$ and $N = \alpha _ { 1 } + \alpha _ { 2 } + \cdot \cdot \cdot + \alpha _ { n } - 1$ Set $w ( z ) = \prod _ { i = 1 } ^ { n } ( z - z _ { i } ) ^ { \alpha _ { i } }$ and

$$
l _ { i k } ( z ) \ : = \ : w ( z ) \ : \frac { ( z \ : - \ : z _ { i } ) ^ { k - \alpha _ { i } } } { k ! } \ : \frac { d ^ { ( \alpha _ { i } - k - 1 ) } } { d z ^ { ( \alpha _ { i } - k - 1 ) } } \biggl [ \frac { ( z \ : - \ : z _ { i } ) ^ { \alpha _ { i } } } { w ( z ) } \biggr ] _ { z = z _ { i } } ,
$$

$$
p _ { N } ( z ) = \sum _ { i = 1 } ^ { n } r _ { i } l _ { i { \bf 0 } } ( z ) + \sum _ { i = 1 } ^ { n } r _ { i } \cdot l _ { i { \bf 1 } } ( z ) + \cdot \cdot \cdot + \sum _ { i = 1 } ^ { n } r _ { i } ^ { ( \alpha _ { i } - 1 ) } l _ { i { \alpha _ { i } } - 1 } ( z )
$$

is the unique member of ${ \mathcal P } _ { N }$ for which

$$
\begin{array} { l l } { { p _ { N } ( z _ { 1 } ) = r _ { 1 } , p ^ { \prime } { } _ { N } ( z _ { 1 } ) = r _ { 1 } { } ^ { \prime } , \cdot \cdot \cdot , p _ { N } ^ { ( \alpha _ { 1 } - 1 ) } ( z _ { 1 } ) = r _ { 1 } ^ { ( \alpha _ { 1 } - 1 ) } } } \\ { { . } } \\ { { . } } \\ { { . } } \end{array}
$$

$$
p _ { N } ( z _ { n } ) = r _ { n } , p ^ { \prime } N ( z _ { n } ) = r _ { n } { ' } , . . . , p _ { N } ^ { ( \alpha _ { n } - 1 ) } ( z _ { n } ) = r _ { n } ^ { ( \alpha _ { n } - 1 ) } .
$$

Ex.5.Given the $2 n \mathrm { ~ + ~ } 1$ points

$$
- \pi \leq x _ { 0 } < x _ { 1 } < \cdot \cdot \cdot < x _ { 2 n } < \pi .
$$

Construct the functions $t _ { j } ( x ) = \prod _ { { k = 0 } \atop { k \ne j } } ^ { 2 n } \sin { \frac { 1 } { 2 } } ( x - x _ { k } ) \left/ \prod _ { { k = 0 } \atop { k \ne j } } ^ { 2 n } \sin { \frac { 1 } { 2 } } ( x _ { j } - x _ { k } ) , \right. \  j = 0 ,$ $1 , \ldots , 2 n$ .If $L _ { j } ( f ) = f ( x _ { j } )$ ,then $t _ { j }$ and $L _ { j }$ are biorthonormal.

Each function $t _ { j } ( x )$ is a linear combination of l, cos $_ { x }$ ....,cos $_ { n x }$ ,sin $x , \ldots$ ， sin nx and hence is an element of $\mathcal { T } _ { \pmb { n } }$

To show this,observe that the numerator of $t _ { j }$ is the product of ${ \bf 2 } n$ factors of the form sin ${ \mathfrak { z } } ( x - x _ { k } ) = \alpha e ^ { i x / 2 } + \beta e ^ { - i x / 2 }$ for appropriate constants $\pmb { \alpha }$ and $\beta$ The product is therefore of the form $\sum _ { \mathrm { ~ : ~ } = \mathrm { ~ - ~ } n } ^ { n } c _ { k } e ^ { i k x }$ ，and is a combination of the required form.The function

$$
T ( x ) = \sum _ { k = 0 } ^ { 2 n } w _ { k } t _ { k } ( x )
$$

is therefore an element of $\mathcal { T } _ { n }$ and is the unique solution of the interpolation problem $T ( x _ { k } ) = w _ { k } , k = 0 , 1 , \ldots , 2 n$ Formula (2.5.28) is known as the Gauss formula of trigonometric interpolation.

Ex.6.Given $\textbf { \em n } + \textbf { 1 }$ distinct points

$$
0 \leq x _ { 0 } < x _ { 1 } < \cdot \cdot \cdot < x _ { n } < \pi .
$$

$$
C _ { j } ( x ) = \prod _ { { k = 0 } \atop { k \neq j } } ^ { n } ( \cos x - \cos x _ { k } ) \left/ \prod _ { { k = 0 } \atop { k \neq j } } ^ { n } ( \cos x _ { j } - \cos x _ { k } ) \right. .
$$

Then $\boldsymbol { C } _ { j }$ is a cosine polynomial of order $\leq n$ (i.e.,a function of the form $\sum _ { k = 0 } ^ { n } a _ { k } \cos k x )$ for which $C _ { j } ( x _ { k } ) = \delta _ { j k }$ Given $n + 1$ distinct values $w _ { 0 } , w _ { 1 } , \ldots , w _ { n }$ there is a unique cosine polynomial of order $\leq n , C ( x )$ ,for which $C ( x _ { k } ) = w _ { k } , k = 0 ;$ $1 , \ldots , n$ .It is

$$
C ( x ) = \sum _ { k = 0 } ^ { n } w _ { k } C _ { k } ( x ) .
$$

Ex. 7. Given $^ { \pmb { \mathscr { n } } }$ distinct points $0 < x _ { 1 } < \cdot \cdot \cdot < x _ { n } < \pi ,$ Set

$$
\displaystyle { S _ { j } ( x ) = \sin x \prod _ { \stackrel { k = 1 } { k \neq j } } ^ { n } ( \cos x - \cos x _ { k } ) \left/ \prod _ { \stackrel { k = 1 } { k \neq j } } ^ { n } ( \cos x _ { j } - \cos x _ { k } ) \right. } 
$$

Then ${ \pmb S } _ { j } ( { \pmb x } )$ is a sine polynomial of order $\leq n$ for which $S _ { j } ( x _ { k } ) = \delta _ { j k }$ Given $\pmb { n }$ distinct values $w _ { 1 } , w _ { 2 } , \ldots , w _ { n }$ ，there is a unique sine polynomial of order $\leq n , S ( x )$ ,for which $S ( x _ { k } ) = w _ { k }$ and it is

$$
S ( x ) = \sum _ { k = 1 } ^ { n } w _ { k } S _ { k } ( x ) .
$$

Ex.8.Let $z _ { 0 } , z _ { 1 } , \ldots , z _ { n }$ be $\boldsymbol { n } + \boldsymbol { 1 }$ distinct real (or complex） points. Let $w _ { 0 } , w _ { 1 } , \ldots , w _ { m }$ be a second such set of $m + 1$ points.Set

$$
\begin{array} { r } { P ( z ) = ( z - z _ { 0 } ) \cdot \cdot \cdot ( z - z _ { n } ) , \phantom { . . . } } \\ { Q ( w ) = ( w - w _ { 0 } ) \cdot \cdot \cdot ( w - w _ { m } ) , } \\ { P _ { j } ( z ) = P ( z ) / ( z - z _ { j } ) , \phantom { . . . } } \\ { Q _ { k } ( w ) = Q ( w ) / ( w - w _ { k } ) . \phantom { . . } } \end{array}
$$

The $( m \mathrm { ~ + ~ } 1 ) ( n \mathrm { ~ + ~ } 1 )$ polynomials

$$
l _ { j k } ( z , w ) = \frac { P _ { j } ( z ) Q _ { k } ( w ) } { P _ { j } ( z _ { j } ) Q _ { k } ( w _ { k } ) }
$$

satisfy

$$
l _ { j k } ( z _ { r } , w _ { s } ) = \delta _ { j r } \delta _ { k s } .
$$

Hence

$$
p ( z , w ) = \sum _ { j = 0 } ^ { n } \sum _ { k = 0 } ^ { m } \mu _ { j k } l _ { j k } ( z , w )
$$

is a polynomial of degree $\leq m n$ which satisfies the $( m + 1 ) ( n + 1 )$ interpolation conditions

$$
\begin{array} { l l } { { } } & { { j = 0 , 1 , . . . , n } } \\ { { p ( z _ { j } , w _ { k } ) = \mu _ { j k } } } & { { } } \\ { { } } & { { k = 0 , 1 , . . . , m . } } \end{array}
$$

Formula (2.5.35) may be regarded as the generalization of the Lagrange formula to two dimensions.Extensions to any number of variables willfollow ina similar fashion.It shows that by taking a suffciently large number of powers of several variables polynomial interpolation can be achieved.

2.6 Representation Theorems: The Newton Formula. The Lagrange formula (2.5.3) or (2.5.l7) has one drawback. If we desire to pass from a space of dimension $\pmb { n }$ to a space of one higher dimension,we must determine an entirely new set of elements $y _ { 1 } { ^ { * } } , y _ { 2 } { ^ { * } } , \dots , y _ { n + 1 } { ^ { * } }$ that are not related in a simple fashion to the old set $x _ { 1 } { } ^ { * } , x _ { 2 } { } ^ { * } , \ldots , x _ { n } { } ^ { * }$ .A representation of Newton gets around this diffculty by taking linear combinations of both the basis elements ${ \pmb x _ { 1 } } , { \pmb x _ { 2 } } , \ldots .$ ，and the prescribed functionalg $L _ { 1 } , L _ { 2 } , \dotsb .$ We shall first study this representation in the case of polynomial interpolation.

Let $z _ { 0 } , \ldots , z _ { n }$ be $n + 1$ distinct points and form the $n + 1$ independent Newton polynomials

$$
1 , \ z - z _ { 0 } , \ ( z - z _ { 0 } ) ( z - z _ { 1 } ) , \ \ldots , ( z - z _ { 0 } ) ( z - z _ { 1 } ) \cdot \cdot \cdot ( z - z _ { n - 1 } ) .
$$

For given values $w _ { 0 } , w _ { 1 } , \ldots , w _ { n }$ there is a unique member of $\mathcal { P } _ { n }$ for which $p ( z _ { i } ) = w _ { i } , i = 0 , 1 , . ~ . ~ . ~ , n$ .Let us see if we can represent it in the form

$$
\begin{array} { c } { p ( z ) = a _ { 0 } + a _ { 1 } ( z - z _ { 0 } ) + a _ { 2 } ( z - z _ { 0 } ) ( z - z _ { 1 } ) + \cdots } \\ { + a _ { n } ( z - z _ { 0 } ) ( z - z _ { 1 } ) \cdot \cdot \cdot ( z - z _ { n - 1 } ) . } \end{array}
$$

To determine the constants ${ \pmb a } _ { i }$ set $z = z _ { 0 } , \ z = z _ { 1 } , \ . \ . \ .$ ， successively， and solve the resulting linear equations:

$$
\begin{array} { r l } & { a _ { 0 } = w _ { 0 } } \\ & { a _ { 1 } = \displaystyle \frac { w _ { 1 } - w _ { 0 } } { z _ { 1 } - z _ { 0 } } } \\ & { a _ { 2 } = \displaystyle \frac { 1 } { z _ { 2 } - z _ { 1 } } \Big ( \displaystyle \frac { w _ { 2 } - w _ { 0 } } { z _ { 2 } - z _ { 0 } } - \displaystyle \frac { w _ { 1 } - w _ { 0 } } { z _ { 1 } - z _ { 0 } } \Big ) . } \\ & { . } \\ & { . } \end{array}
$$

Note that for a fixed set of points $z _ { 0 } , \ldots , z _ { n }$ ，each $\pmb { a } _ { i }$ is a certain linear combination of the ${ \boldsymbol { w } } _ { i }$ ,and that,furthermore, ${ \pmb { a } } _ { \mathbf { 0 } }$ involves only ${ \pmb w } _ { \mathbf 0 }$ and ${ z _ { 0 } } ; { a _ { 1 } }$ involves only $w _ { 0 } , w _ { 1 } , z _ { 0 } , z _ { 1 } ; a _ { 2 }$ involves only $w _ { 0 } , w _ { 1 } , w _ { 2 } , z _ { 0 } , z _ { 1 } , z _ { 2 }$ etc.

DEFINITION 2.6.1. The constant $\pmb { a _ { j } }$ is called the divided difference of the jth order of $w _ { 0 } , w _ { 1 } , \dotsc , w _ { j }$ with respect to $z _ { 0 } , z _ { 1 } , \dots , z _ { j } . \ i$ $\mathit { \Pi } _ { I t }$ is designated by

$$
a _ { j } = [ w _ { 0 } , w _ { 1 } , \ldots , w _ { j } ] .
$$

A compact formula for ${ \pmb a } _ { j }$ can be found by comparing (2.6.l) with the Lagrange formula (2.5.8) with which it must coincide.The coefficient of $z ^ { n }$ in (2.6.1) is fore, ${ \pmb a } _ { \pmb n }$ . The coefficient of $z ^ { n }$ in (2.5.8) is seen to be $\sum _ { k = 0 } ^ { n } { \frac { w _ { k } } { w ^ { \prime } ( z _ { k } ) } }$ . There-

$$
a _ { n } = [ w _ { 0 } , w _ { 1 } , \ldots , w _ { n } ] = \sum _ { k = 0 } ^ { n } \frac { w _ { k } } { w ^ { \prime } ( z _ { k } ) }
$$

where $w ( z ) = w _ { n } ( z ) = ( z - z _ { 0 } ) ( z - z _ { 1 } ) \cdot \cdot \cdot ( z - z _ { n } ) .$ Thus, again, from (2.6.4),

$$
\begin{array} { l } { \displaystyle a _ { 1 } = \frac { w _ { 0 } } { z _ { 0 } - z _ { 1 } } + \frac { w _ { 1 } } { z _ { 1 } - z _ { 0 } } } \\ { \displaystyle a _ { 2 } = \frac { w _ { 0 } } { ( z _ { 0 } - z _ { 1 } ) ( z _ { 0 } - z _ { 2 } ) } + \frac { w _ { 1 } } { ( z _ { 1 } - z _ { 0 } ) ( z _ { 1 } - z _ { 2 } ) } + \frac { w _ { 2 } } { ( z _ { 2 } - z _ { 0 } ) ( z _ { 2 } - z _ { 1 } ) } } \end{array}
$$

If the $w _ { i }$ are taken as the value of a function $f$ at $z _ { i } \colon f ( z _ { i } ) = w _ { i } ,$ ，then we may combine (2.6.l) and (2.6.3) to obtain

$$
p _ { n } ( f ; z ) = \sum _ { k = 0 } ^ { n } [ f ( z _ { 0 } ) , f ( z _ { 1 } ) , \ldots , f ( z _ { k } ) ] ( z - z _ { 0 } ) ( z - z _ { 1 } ) \cdot \cdot \cdot ( z - z _ { k - 1 } ) .
$$

$$
{ \pmb w } _ { - { \bf 1 } } ( { \pmb z } ) \equiv { \bf 1 } .
$$

This form of the interpolating polynomial is the fnite Newton series for a function $f ( z )$

With $z _ { 0 } , z _ { 1 } , \ldots , z _ { n }$ fixed, introduce the linear functionals

$$
L _ { 0 } ( f ) = f ( z _ { 0 } )
$$

$$
\begin{array} { c } { { L _ { 1 } ( f ) = \displaystyle { \frac { f ( z _ { 0 } ) } { z _ { 0 } - z _ { 1 } } } + \displaystyle { \frac { f ( z _ { 1 } ) } { z _ { 1 } - z _ { 0 } } } } } \\ { { . } } \\ { { . } } \\ { { . } } \end{array}
$$

according to the scheme in (2.6.5). Then (2.6.6) becomes

$$
p _ { n } ( f ; z ) = \sum _ { k = 0 } ^ { n } L _ { k } ( f ) w _ { k - 1 } ( z ) .
$$

Since $w _ { j } ( z ) \in \mathcal { P } _ { n }$ if $0 \leq j \leq n - 1$ it follows that $w _ { j } ( z ) = p _ { n } ( w _ { j } ( z ) ; z )$ and hence

$$
w _ { j } ( z ) \equiv \sum _ { k = 0 } ^ { n } L _ { k } ( w _ { j } ( z ) ) w _ { k - 1 } ( z )
$$

By setting $j = 0 , 1 , 2 , \ldots ,$ in (2.6.9) successively we obtain

$$
L _ { k } ( w _ { j - 1 } ( z ) ) = \delta _ { k j } .
$$

Comparing the biorthogonality relationships (2.6.l0) and (2.5.l4) our introductory remarks become clear.Whereas $w _ { \boldsymbol { k } } ( z )$ depends only on the points $z _ { 0 } , \dotsc , z _ { k } , l _ { k } ( z ) = l _ { k , n } ( z )$ depends upon all the points $z _ { 0 } , \ldots , z _ { k } , \ldots , z _ { n }$ In the Lagrange representation，we add an additional point and increase the degree of the interpolating polynomial at the cost of changing all the fundamental polynomials.In the Newton representation,this can be accomplished by adding one more term. The Newton representation has a permanence property,and this is characteristic of Fourier series and other orthogonal and biorthogonal expansions.(See 8.5.) The price that is paid for the convenience of the permanence property is that the multipliers of the individual polynomials are no longer simple values at a point,but certain linear combinations of these values.

This type of biorthonormality and permanence can be obtained in a general setting.

THEOREM 2.6.1 (Biorthonormality Theorem or Generalized Newton Representation). Let $X$ be a linear space of infinite dimension. Let $x _ { 1 }$ ， $\pmb { x _ { 2 } } .$ be a sequence of elements of $X$ such that for each $n , x _ { 1 } , \ldots , x _ { n }$ are independent, Suppose,further,that $L _ { 1 } , L _ { 2 } , \ldots$ ，is $^ { a }$ sequence of linear functionals in $X ^ { * }$ such that for each $\pmb { n }$ the $\textit { \textbf { n } } \times \textit { \textbf { n } }$ determinant

$$
\vert L _ { i } ( x _ { j } ) \vert _ { i , j = 1 } ^ { n } \neq 0 .
$$

Then there is determined uniquely two triangular systems of constants $\pmb { a } _ { i j }$ $\boldsymbol { b } _ { i j }$ with $\pmb { a } _ { i i } \neq 0$ such that if

$$
\begin{array} { l l } { { { { L } _ { 1 } } ^ { * } = a _ { 1 1 } { L } _ { 1 } } } & { { { { x } _ { 1 } } ^ { * } = x _ { 1 } } } \\ { { { { L } _ { 2 } } ^ { * } = a _ { 2 1 } { L } _ { 1 } + a _ { 2 2 } { L } _ { 2 } } } & { { { { x } _ { 2 } } ^ { * } = b _ { 2 1 } { x } _ { 1 } + x _ { 2 } } } \\ { { { { L } _ { 3 } } ^ { * } = a _ { 3 1 } { L } _ { 1 } + a _ { 3 2 } { L } _ { 2 } + a _ { 3 3 } { L } _ { 3 } } } & { { { { x } _ { 3 } } ^ { * } = b _ { 3 1 } { x } _ { 1 } + b _ { 3 2 } { x } _ { 2 } + x _ { 3 } } } \\ { . } & { . } \\ { . } & { . } \\ { . } \end{array}
$$

we have

$$
{ L _ { i } } ^ { * } ( { x _ { j } } ^ { * } ) = { \delta } _ { i j } , ~ i , j = 1 , 2 , \cdots .
$$

Pro0f: We want $L _ { 1 } { } ^ { * } ( x _ { 1 } { } ^ { * } ) = 1$ . Therefore, $a _ { 1 1 } L _ { 1 } ( x _ { 1 } ) = 1$ or

$$
a _ { 1 1 } = ( L _ { 1 } ( x _ { 1 } ) ) ^ { - 1 } \neq 0 .
$$

The denominator does not vanish by (2.6.ll). We shall now carry out an inductive proof.Assume that we have already determined

$$
\begin{array} { c c c c c c c c c c c c c c c c c c c c c c c } { a _ { 1 1 } } & & & & & & & & & & & & & & & & & & & & & & & & & & & & & \\ { a _ { 2 1 } } & { a _ { 2 2 } } & & & & & & { b _ { 2 1 } } & { 1 } & & & & & & & & & & & & \\ { \cdot } & { \cdot } & & & & & { \cdot } & { \cdot } & & & & & & & & & & & \\ { \cdot } & { \cdot } & & & & & { \cdot } & { \cdot } & & & & & & & & & \\ { \cdot } & { \cdot } & & & & & { \cdot } & { \cdot } & & & & & & & & & \\ { \cdot } & { \cdot } & & & & & & { \cdot } & { \cdot } & & & & & & & & & \\ { a _ { n 1 } } & { a _ { n 2 } } & { \cdot \cdot \cdot \cdot } & { a _ { n n } } & & & & & { b _ { n 1 } } & { b _ { n 2 } } & { \cdot \cdot \cdot } & { b _ { n , n - 1 } } & { 1 } & & & & \end{array}
$$

with $a _ { 1 1 } a _ { 2 2 } \cdots a _ { n n } \neq 0$ and such that

$$
{ L _ { i } } ^ { * } ( x _ { j } { * } ) = { \delta } _ { i j } , ~ i , j = 1 , 2 , . ~ . ~ . ~ , n .
$$

We will show that we can obtain first $b _ { n + 1 , 1 } , b _ { n + 1 , 2 } , \dotsc , b _ { n + 1 , n } , 1$ and from a knowledge of these values can then obtain ${ \pmb { a } } _ { n + 1 , 1 }$ ， $a _ { n + 1 , 2 } , \ldots , a _ { n + 1 , n + 1 }$ with $a _ { n + 1 , n + 1 } \neq 0$ and such that

$$
{ L _ { i } } ^ { * } ( x _ { j } { } ^ { * } ) = \delta _ { i j } , \qquad i , j = 1 , 2 , \ldots , n + 1 .
$$

The conditions included in (2.6.l5) that are not already contained in (2.6.14) are

$$
\begin{array} { r l } { L _ { i } { * ( x _ { n + 1 } ^ { * } ) } = 0 } & { i = 1 , 2 , \ldots , n \quad \mathrm { a n d } } \\ { L _ { n + 1 } ^ { * } ( x _ { i } { * } ) = 0 } & { i = 1 , 2 , \ldots , n , } \\ { L _ { n + 1 } ^ { * } ( x _ { n + 1 } ^ { * } ) = 1 . } \end{array}
$$

The first $\pmb { n }$ equations in (2.6.l6) yield the system

$$
b _ { n + 1 , 1 } L _ { 1 } { } ^ { * } ( x _ { 1 } ) + b _ { n + 1 , 2 } L _ { 1 } { } ^ { * } ( x _ { 2 } ) + \cdot \cdot \cdot + b _ { n + 1 , n } L _ { 1 } { } ^ { * } ( x _ { n } ) = - L _ { 1 } { } ^ { * } ( x _ { n + 1 } )
$$

$$
b _ { n + 1 , 1 } L _ { n } { } ^ { * } ( x _ { 1 } ) + b _ { n + 1 , 2 } L _ { n } { } ^ { * } ( x _ { 2 } ) + \cdot \cdot \cdot + b _ { n + 1 , n } L _ { n } { } ^ { * } ( x _ { n } ) = - L _ { n } { } ^ { * } ( x _ { n + 1 } ) .
$$

This system has a unique solution providing $\vert { L } _ { i } { ^ { * } ( x _ { j } ) } \vert _ { i , j = 1 } ^ { n } \neq 0$ . But from Problem 19,Chapter II,

$$
| L _ { i } { ^ * } ( x _ { j } ) | = \left| { \begin{array} { l l l l } { a _ { 1 1 } } & { 0 } & { \cdots } & { 0 } \\ { a _ { 2 1 } } & { a _ { 2 2 } } & { \cdots } & { 0 } \\ { \cdot } & { } & { \cdot } \\ { \cdot } & { } & { \cdot } \\ { \cdot } & { } & { \cdot } \\ { a _ { n 1 } } & { a _ { n 2 } } & { \cdots } & { a _ { n n } } \end{array} } \right| \cdot | L _ { i } ( x _ { j } ) | _ { i , j = 1 } ^ { n }
$$

$$
= a _ { 1 1 } a _ { 2 2 } \cdot \cdot \cdot a _ { n n } | L _ { i } ( x _ { j } ) | _ { i , j = 1 } ^ { n } \neq 0 .
$$

Having determined the b's, or equivalently ${ \boldsymbol x } _ { n + 1 } ^ { * }$ , consider the second group of $\pm 1$ equations in (2.6.16). This yields

$$
\begin{array} { l } { { a _ { n + 1 , 1 } L _ { 1 } ( x _ { 1 } { * } ) + \dots + a _ { n + 1 , n + 1 } L _ { n + 1 } ( x _ { 1 } { * } ) = 0 } } \\ { { \mathrm { . } } } \\ { { \mathrm { . } } } \end{array}
$$

$$
\begin{array} { r } { a _ { n + 1 , 1 } L _ { 1 } ( x _ { n } { } ^ { * } ) + \cdots + a _ { n + 1 , n + 1 } L _ { n + 1 } ( x _ { n } { } ^ { * } ) = 0 } \\ { a _ { n + 1 , 1 } L _ { 1 } ( x _ { n + 1 } ^ { * } ) + \cdots + a _ { n + 1 , n + 1 } L _ { n + 1 } ( x _ { n + 1 } ^ { * } ) = 1 } \end{array}
$$

This system has a unique solution providing that

$$
| L _ { i } ( { x _ { j } } ^ { * } ) | _ { i , j = 1 } ^ { n + 1 } \neq 0 .
$$

But,again by Problem 19,

$$
| L _ { i } ( x _ { j } ^ { * } ) | _ { i , j = 1 } ^ { n + 1 } = \left| \begin{array} { l l l l } { 1 } & { 0 } & { \cdots } & { 0 } \\ { b _ { 2 1 } } & { 1 } & { \cdots } & { 0 } \\ { \cdot } & { } & { } & { \cdot } \\ { \cdot } & { } & { \cdot } \\ { \cdot } & { } & { \cdot } \\ { b _ { n + 1 , 1 } } & { b _ { n + 2 , 1 } } & { \cdots } & { 1 } \end{array} \right| \cdot | L _ { i } ( x _ { j } ) | _ { i , j = 1 } ^ { n + 1 }
$$

$$
= | L _ { i } ( x _ { j } ) | _ { i , j = 1 } ^ { n + 1 } \neq 0 .
$$

Furthermore, $a _ { n + 1 , n + 1 } = a _ { 1 1 } a _ { 2 2 } \cdot \cdot \cdot a _ { n n } | L _ { i } ( x _ { j } ) | _ { i , j = 1 } ^ { n } / | L _ { i } ( x _ { j } ) | _ { i , j = 1 } ^ { n + 1 } \neq 0 .$ We observe finally that at no stage is there any arbitrariness in our determination of the constants and hence the solution is unique.

COROLLARY 2.6.2. Let $X _ { n }$ designate the subspace of $\pmb { X }$ spanned by $x _ { 1 } , \ldots ,$ $x _ { n }$ (i.e., the set of all linear combinations $a _ { 1 } x _ { 1 } + \cdots + a _ { n } x _ { n } )$ .If $x \in X _ { n }$ then

$$
\begin{array} { c } { { \displaystyle x = \sum _ { k = 1 } ^ { n } L _ { k } { } ^ { * } ( x ) x _ { k } { } ^ { * } . } } \\ { { \displaystyle = \sum _ { k = 1 } ^ { n } { L _ { k } { } ^ { * } ( x ) x _ { k } { } ^ { * } \mathrm { ~ t h e n ~ } L _ { j } { } ^ { * } ( y ) } = \sum _ { k = 1 } ^ { n } { L _ { k } { } ^ { * } ( x ) L _ { j } { } ^ { * } ( x _ { k } { } ^ { * } ) } = L _ { j } { } ^ { * } ( x ) } } \end{array}
$$

Proof: If by (2.6.13). Since $x _ { 1 } , \ldots , x _ { n }$ are independent,it follows from (2.6.l2） that ${ x _ { 1 } } ^ { * } , \ldots , { x _ { n } } ^ { * }$ are independent.Hence from (2.6.l3) and Lemma 2.2.l it follows that $L _ { 1 } , \ldots , L _ { n }$ and consequently $L _ { 1 } { } ^ { * } , \ldots , L _ { n } { } ^ { * }$ are independent. In view of this, $L _ { j } { * } ( y - x ) = 0 , j = 1 , 2 , \ldots , n$ implies $y = x$

For a given $x \in X$ ,the formal series

$$
x \sim \sum _ { k = 1 } ^ { \infty } L _ { k } { * ( x ) } { x _ { k } } ^ { * }
$$

is a biorthogonal expansion of the element $_ x$ .In particular cases,the relation of the series to $_ { x }$ has been the object of vast investigations.

It will help to grasp the difference between the biorthonormality of Lagrange type (2.5.l5) and that of Newton type (2.6.15) if each is expressed in the language of matrices.Let $G$ designate the matrix $( L _ { i } ( x _ { j } ) )$ . Let $\pmb { A }$ designate the matrix $( a _ { i j } )$ where the $\boldsymbol { a } _ { i j }$ are the quantities appearing in the proof of Theorem 2.5.1. $\boldsymbol { \mathit { I } }$ is the unit matrix. Then,(2.5.l5) may be expressed as

$$
G A ^ { \prime } = I , ~ A ^ { \prime } = \mathrm { t r a n s p o s e ~ o f } ~ A .
$$

On the other hand,if $\pmb { A }$ and $\pmb { B }$ designate the lower triangular matrices taken from the coefficient scheme of (2.6.l2) then

$$
A G B ^ { \prime } = I .
$$

Note that (2.6.19) is equivalent to

$$
\begin{array} { r } { G = A ^ { - 1 } ( B ^ { \prime } ) ^ { - 1 } . } \end{array}
$$

Now, $A ^ { - 1 }$ is a lower triangular matrix with non-zero elements on its·principal diagonal and $( B ^ { \prime } ) ^ { - 1 }$ is an upper triangular matrix with l's on its principal diagonal.(2.6.20) has a matrix formulation.A matrix ${ \cal { G } } = ( g _ { i j } )$ is said to be regularly arranged if none of its principal minors $\left( \mathrm { i . e . , } g _ { 1 1 } , \begin{array} { l } { { \left| \begin{array} { l l } { { g _ { 1 1 } } } & { { g _ { 1 2 } } } \\ { { g _ { 2 1 } } } & { { g _ { 2 2 } } } \end{array} \right| , . . . . } } \end{array} \right)$ vanishes. If $G$ is regularly arranged,then it can be expressed as the product of a lower triangular matrix by an upper triangular matrix with l's on its principal diagonal. This is known as an $_ { L U }$ -decomposition of $G$

The result of biorthogonalization can be expressed by means of determinants.

THEOREM 2.6.3. With the notation of the previous theorem,let

$$
G _ { r } = \vert L _ { \imath } ( x _ { j } ) \vert _ { i , j = 1 } ^ { r } .
$$

Then,

$$
x _ { j } \ast = { \frac { 1 } { G _ { j - 1 } } } { \left| \begin{array} { l l l l } { L _ { 1 } ( x _ { 1 } ) } & { L _ { 1 } ( x _ { 2 } ) } & { \cdots } & { L _ { 1 } ( x _ { j } ) } \\ { \cdot } & { \cdot } & { \cdot } \\ { \cdot } & { \cdot } & { \cdot } \\ { \cdot } & { \cdot } & { \cdot } \\ { L _ { j - 1 } ( x _ { 1 } ) } & { L _ { j - 1 } ( x _ { 2 } ) } & { \cdots } & { L _ { j - 1 } ( x _ { j } ) } \\ { \quad x _ { 1 } } & { x _ { 2 } } & { \cdot \cdot \cdot } & { x _ { j } } \end{array} \right| }
$$

$$
L _ { j } * = \frac { 1 } { G _ { j } } \left| \begin{array} { c c c c c } { L _ { 1 } ( x _ { 1 } ) } & { L _ { 2 } ( x _ { 1 } ) } & { \cdots } & { L _ { j } ( x _ { 1 } ) } \\ { \cdot } & { \cdot } & { \cdot } & { \cdot } \\ { \cdot } & { \cdot } & { \cdot } \\ { \cdot } & { \cdot } & { \cdot } \\ { L _ { 1 } ( x _ { j - 1 } ) } & { L _ { 2 } ( x _ { j - 1 } ) } & { \cdots } & { L _ { j } ( x _ { j - 1 } ) } \\ { L _ { 1 } } & { L _ { 2 } } & { \cdot \cdot } & { L _ { j } } \end{array} \right| .
$$

Proof:Expand these determinants according to the minors of the last row. We see that ${ x _ { j } } ^ { * }$ is a linear combination of $x _ { 1 } , x _ { 2 } , \dotsc , x _ { j }$ and $\boldsymbol { L _ { j } } ^ { * }$ is a linear combination of $L _ { 1 } , L _ { 2 } , \ldots , L _ { j }$ .Moreover the coefficient of $\boldsymbol { x } _ { j }$ in ${ x _ { j } } ^ { * }$ is 1. Fix a $j > 1$ .We shall show that ${ \cal L } _ { i } { } ^ { * } ( x _ { j } { } ^ { * } ) = 0$ for $i < j$ It suffices to show that $L _ { i } ( x _ { j } ^ { * } ) = 0$ for $i < j$ But

$$
L _ { i } ( x _ { j } * ) = { \frac { 1 } { G _ { j - 1 } } } { \left| \begin{array} { l l l l } { L _ { 1 } ( x _ { 1 } ) } & { L _ { 1 } ( x _ { 2 } ) } & { \cdot \cdot } & { L _ { 1 } ( x _ { j } ) } \\ { \cdot } & { \cdot } & { \cdot } \\ { \cdot } & { \cdot } & { \cdot } \\ { \cdot } & { \cdot } & { \cdot } \\ { L _ { j - 1 } ( x _ { 1 } ) } & { L _ { j - 1 } ( x _ { 2 } ) } & { \cdot \cdot } & { L _ { j - 1 } ( x _ { j } ) } \\ { L _ { i } ( x _ { 1 } ) } & { L _ { i } ( x _ { 2 } ) } & { \cdot \cdot } & { L _ { i } ( x _ { j } ) } \end{array} \right| } = 0
$$

inasmuch as two rows are identical. Similarly,we can show that for fixed $i > 1$ ， ${ \cal L } _ { i } { } ^ { * } ( x _ { j } { } ^ { * } ) = 0$ for $j < i$ .It remains to show that ${ \cal L } _ { i } { } ^ { * } ( x _ { i } { } ^ { * } ) = 1$ Since $x _ { i } { ^ * } = b _ { i 1 } x _ { 1 } + b _ { i 2 } x _ { 2 } + \cdot \cdot \cdot + b _ { i , i - 1 } x _ { i - 1 } + x _ { i }$ it suffices to show that $L _ { i } { * ( x _ { i } ) } =$ 1.Now,from the second equation of (2.6.21), ${ L _ { i } } ^ { * } ( x _ { i } ) = { G _ { i } } / { G _ { i } } = 1$ The above biorthogonal representation is unique and the theorem follows.

We now give some examples of biorthogonal systems of the Newton type.

Ex.1． (Newton Polynomials). $x$ is the space of all polynomials in $\pmb { z }$ ，

$$
x _ { 1 } = 1 , x _ { 2 } = z , x _ { 3 } = z ^ { 2 } , \ldots , L _ { 1 } ( f ) = f ( z _ { 0 } ) , L _ { 2 } ( f ) = f ( z _ { 1 } ) , \ldots ,
$$

where ${ \pmb z } _ { i }$ are distinct points.Then,

$$
G _ { r } = \left| \begin{array} { c c c c c c } { 1 } & { z _ { 0 } } & { z _ { 0 } ^ { 2 } } & { \cdots } & { z _ { 0 } ^ { r - 1 } } \\ { \vdots } & { z _ { 1 } } & { z _ { 1 } ^ { 2 } } & { \ddots } & { z _ { 1 } ^ { r - 1 } } \\ { \cdot } & { \cdot } & { \cdot } & & { \cdot } \\ { \cdot } & { \cdot } & { \cdot } & & { \cdot } \\ { \cdot } & { \cdot } & { \cdot } & & { \cdot } \\ { 1 } & { z _ { r - 1 } } & { z _ { r - 1 } ^ { 2 } } & { \cdot \cdot } & { z _ { r - 1 } ^ { r - 1 } } \end{array} \right| = \prod _ { i > j } ^ { r - 1 } ( z _ { i } - z _ { j } )
$$

$$
x _ { j } \sp * = { \frac { 1 } { G _ { j - 1 } } } \left| \begin{array} { c c c c c c } { { 1 } } & { { z _ { 0 } } } & { { z _ { 0 } \sp 2 } } & { { \cdots } } & { { z _ { 0 } \sp { j - 1 } } } \\ { { \cdot } } & { { \cdot } } & { { \cdot } } & { { \cdot } } & { { \cdot } } \\ { { \cdot } } & { { \cdot } } & { { \cdot } } & { { \cdot } } & { { \cdot } } \\ { { \cdot } } & { { \cdot } } & { { \cdot } } & { { \cdot } } & { { \cdot } } \\ { { \cdot } } & { { \cdot } } & { { \cdot } } & { { \cdot } } & { { \cdot } } \\ { { 1 } } & { { z _ { j - 2 } } } & { { z _ { j - 2 } ^ { 2 } } } & { { \cdot \cdot \cdot } } & { { z _ { j - 2 } ^ { j - 1 } } } \\ { { 1 } } & { { z } } & { { z \sp 2 } } & { { \cdot \cdot \cdot } } & { { z ^ { j - 1 } } } \end{array} \right|
$$

This is a polynomial $q ( z )$ of degree $j - 1$ in $\pmb { z }$ .Now $q ( z _ { 0 } ) = q ( z _ { 1 } ) = \cdot \cdot \cdot = q ( z _ { j - 2 } ) = 0$ inasmuch as two rows are identical. Hence $x _ { j } { * } \ : = \ : ( z \ : - \ : z _ { 0 } ) ( z \ : - \ : z _ { 1 } ) \ : \cdot \ : \cdot ( z \ : - \ : z _ { j - 1 } )$ ， Corresponding to $\boldsymbol { L _ { j } } ^ { * }$ we have the divided differences of $f$ at the points $z _ { 0 } , z _ { 1 } , \dots z _ { \mathrm { ~ \tiny ~ ( ~ \cdot ~ ) ~ } }$ Formula (2.6.21) yields the representation

$$
\pmb { a _ { n } } = [ f ( z _ { 0 } ) , f ( z _ { 1 } ) , . . . , f ( z _ { n } ) ]
$$

$$
\begin{array} { r l } & { \mathbf { \Phi } _ { , J } : \langle \mathbf { \Phi } _ { 1 } | \boldsymbol { \cdot } , \boldsymbol { \cdot } , \boldsymbol { \cdot } , \boldsymbol { \cdot } , \boldsymbol { } , \boldsymbol { \cdot } , \boldsymbol { } , \boldsymbol { \cdot } , \boldsymbol { } \rangle } \\ & { = \left| \begin{array} { l l l l } { \mathbf { \Phi } _ { 1 } } & { \mathbf { \Phi } _ { 1 } } & { \dots } & { \mathbf { \Phi } _ { 1 } } \\ { \mathbf { \Phi } _ { z _ { 0 } } } & { \mathbf { \Phi } _ { z _ { 1 } } } & { \dots } & { \mathbf { \Phi } _ { z _ { n } } } \\ { \cdot } & { \cdot } & { \cdot } & { \cdot } \\ { \cdot } & { \cdot } & { \cdot } & { \cdot } \\ { \cdot } & { \cdot } & { \cdot } & { \cdot } \\ { z _ { 0 } ^ { n - 1 } } & { z _ { 1 } ^ { n - 1 } } & { \dots } & { z _ { n } ^ { n - 1 } } \\ { \mathbf { \Phi } _ { 2 } ^ { n } } & { \mathbf { \Phi } _ { 2 } ^ { n } } & { \dots } & { \mathbf { \Phi } _ { \tilde { n } } } \end{array} \right| \left| \begin{array} { l l l l l } { \mathbf { \Phi } _ { 1 } } & { \mathbf { \Phi } _ { 1 } } & { \dots } & { \mathbf { \Phi } _ { 1 } } \\ { \mathbf { \Phi } _ { z _ { 0 } } } & { \mathbf { \Phi } _ { z _ { 1 } } } & { \dots } & { \mathbf { \Phi } _ { z _ { n } } } \\ { \cdot } & { \cdot } & { \cdot } & { \cdot } \\ { \cdot } & { \cdot } & { \cdot } & { \cdot } \\ { \cdot } & { \cdot } & { \cdot } & { \cdot } \\ { z _ { 0 } ^ { n - 1 } } & { z _ { 1 } ^ { n - 1 } } & { \dots } & { z _ { n } ^ { n - 1 } } \\ { \mathbf { \Phi } _ { 2 } ^ { n } } & { \mathbf { \Phi } _ { z _ { 1 } } ^ { n } } & { \dots } & { z _ { n } ^ { n } } \end{array} \right| } \end{array}
$$

for divided differences.

Ex.2 (Abel-Gontscharoff Polynomials)． These polynomials, $Q _ { n } ( z )$ ,arise from biorthogonalizing the powers $1 , z , z ^ { 2 } , \ldots$ ，against the functionals $\pmb { L _ { 0 } } ( f ) =$ $f ( z _ { 0 } ) , L _ { 1 } ( f ) = f ^ { \prime } ( z _ { 1 } ) , L _ { 2 } ( f ) = f ^ { \prime } ( z _ { 2 } ) ,$ .... We have

$$
\scriptstyle G _ { \tau } = { \left| \begin{array} { l l l l l l } { 1 } & { z _ { 0 } } & { z _ { 0 } ^ { 0 } } & { \cdots } & & { z _ { 0 } ^ { \tau - 1 } } \\ { 0 } & { 1 } & { 2 z _ { 1 } } & { \cdots } & & { ( r - 1 ) z _ { 1 } ^ { \tau - 2 } } \\ { 0 } & { 0 } & { 2 } & { \cdots } & { ( r - 1 ) ( r - 2 ) z _ { 2 } ^ { \tau - 3 } } \\ { \cdot } & { \cdot } & & & { \cdot } \\ { \cdot } & { \cdot } & & & { \cdot } \\ { \cdot } & { \cdot } & & & { \cdot } \\ { 0 } & { 0 } & { \cdots } & { \cdot } & & { ( r - 1 ) ! } \end{array} \right| } = 1 ! \ 2 ! \ 3 ! \ \cdot \ \cdot \ \cdot ( r - 1 ) !
$$

$$
L _ { n } \mathbf { * } ( f ) = \frac { 1 } { G _ { n + 1 } } \left| \begin{array} { l l l l l l } { ~ 1 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { z _ { 0 } } & { ~ 1 } & { 0 } & { 0 } & { 0 } \\ { z _ { 0 } ^ { 2 } } & { ~ 2 z _ { 1 } } & { ~ 2 } & { ~ 0 } \\ { ~ \cdot } & { ~ \cdot } & { ~ \cdot } & { ~ \cdot } & { ~ \cdot } \\ { ~ \cdot } & { ~ \cdot } & { ~ \cdot } & { ~ \cdot } & { ~ \cdot } \\ { ~ \cdot } & { ~ \cdot } & { ~ \cdot } & { ~ \cdot } & { ~ \cdot } \\ { z _ { 0 } ^ { n - 1 } } & { ( n - 1 ) z _ { 1 } ^ { n - 2 } } & { ~ ( n - 1 ) ! } & { ~ 0 } \\ { ~ f ( z _ { 0 } ) } & { ~ f ^ { \prime } ( z _ { 1 } ) } & { ~ f ^ { ( n - 1 ) } ( z _ { n - 1 } ) } & { f ^ { ( n ) } ( z _ { n } ) } \end{array} \right| = \frac { f ^ { ( n ) } ( z _ { n } ) } { n ! }
$$

$$
\begin{array} { r } { Q _ { n } ( z ) \ = \frac { 1 } { G _ { n } } \left| \begin{array} { l l l l l l } { 1 } & { z _ { 0 } } & { z _ { 0 } ^ { 2 } } & { \cdots } & { z _ { 0 } ^ { n } } \\ { 0 } & { 1 } & { 2 z _ { 1 } } & { \cdots } & { n z _ { 1 } ^ { n - 1 } } \\ { 0 } & { 0 } & { 2 } & { \cdots } & { n ( n - 1 ) z _ { 2 } ^ { n - 2 } } \\ { \cdot } & { \cdot } & { \cdot } & & { \cdot } \\ { \cdot } & { \cdot } & { \cdot } & & & { \cdot } \\ { 1 } & { \cdot } & { \cdot } & & & { \cdot } \\ { 1 } & { z } & { z ^ { 2 } } & { \cdots } & { z ^ { n } } & \end{array} \right| } \end{array}
$$

Thus,in particular,we have

$$
\begin{array} { r l } & { Q _ { \bf 0 } ( z ) = 1 } \\ & { Q _ { \bf 1 } ( z ) = z - z _ { 0 } } \\ & { Q _ { \bf 2 } ( z ) = z ^ { 2 } - 2 z _ { 1 } z + z _ { 0 } ( 2 z _ { 1 } - z _ { 0 } ) . } \\ & { . } \\ & { . } \\ & { . } \end{array}
$$

The polynomials $Q _ { n } ( z )$ are the Abel-Gontscharoff polynomials. A more tractable representation can be found for $Q _ { n } ( z )$ in terms of iterated integration. Consider the $\pmb { n }$ -fold iterated integral

$$
T _ { n } ( z ) \ = n ! \int _ { z _ { 0 } } ^ { z } d z ^ { \prime } \int _ { z _ { 1 } } ^ { z ^ { \prime } } d z ^ { \prime \prime } \int _ { z _ { 2 } } ^ { z ^ { \prime } } d z ^ { \prime \prime \prime } \ \cdot \cdot \cdot \int _ { z _ { n - 1 } } ^ { z ^ { ( n - 1 ) } } d z ^ { ( n ) } , n \geq 1 .
$$

It is clear that $\scriptstyle { \pmb { T } } _ { \pmb { n } }$ is a polynomial of degree $\pmb { n }$ with leading coefficient 1.Furthermore, $T _ { n } ( z _ { 0 } ) = 0$ ,and by successive differentiation,

$$
\begin{array} { l } { { T _ { n } ^ { \prime } ( z _ { 1 } ) = 0 , \dots , \frac { T _ { n } ^ { ( n ) } ( z _ { n } ) } { n ! } = 1 , } } \\ { { \frac { T _ { n } ^ { ( r ) } ( z _ { r } ) } { r ! } = 0 \quad \mathrm { f o r } \quad r > n . } } \end{array}
$$

Thus,the biorthogonalityconditions hold for $\scriptstyle { T _ { n } }$ , and hence $T _ { n } \equiv Q _ { n }$

Ex.3 (Bernoulli Polynomials)．Let $\pmb { f } ( \pmb { z } )$ be analytic at ${ \boldsymbol { z } } = \mathbf { 0 }$ and assume that $f ( 0 ) \neq 0$ .ByLeibnitz'rule

$$
{ \frac { d ^ { n } } { d z ^ { n } } } \left( f ( z ) e ^ { s z } \right) = \sum _ { k = 0 } ^ { n } { \binom { n } { k } } s ^ { k } e ^ { s z } f ^ { ( n - k ) } ( z ) .
$$

Hence,

$$
{ \frac { d ^ { n } } { d z ^ { n } } } \left( f \left( z \right) e ^ { s z } \right) \left| _ { z = 0 } = \sum _ { k = 0 } ^ { n } { \binom { n } { k } } s ^ { k } f ^ { ( n - k ) } ( 0 ) \right.
$$

is a polynomial of degree $_ n$ in $\pmb { \mathscr { s } }$ In particular, select $f ( z ) = { \frac { z } { e ^ { z } - 1 } }$ 1，a function that is analytic in $| z | < 2 \pi$ and $f ( 0 ) \neq 0$ .Hence,we may write

$$
\frac { z e ^ { s z } } { e ^ { z } - 1 } = \sum _ { n = 0 } ^ { \infty } \frac { 1 } { n ! } \left( \frac { z e ^ { s z } } { e ^ { z } - 1 } \right) _ { 0 } ^ { ( n ) } z ^ { n } = \sum _ { n = 0 } ^ { \infty } \frac { 1 } { n ! } B _ { n } ( s ) z ^ { n }
$$

for certain polynomials $B _ { n } ( s )$ of degree $_ n$ .(2.6.31) is valid for $| z | < 2 \pi$ and can be shown to hold uniformly in $\pmb { \mathscr { s } }$ and $\pmb { z }$ provided $\pmb { \mathscr { s } }$ is confined to a closed bounded region and $_ z$ to a closed subset of $| z | < 2 \pi$ The polynomials $B _ { n } ( z )$ are the Bernoulli Polynomials. The generating function (2.6.3l） provides a convenient way to define them.Fora general $f ( z )$ ,the resulting polynomials $p _ { n } ( s )$ defined by

$$
f ( z ) e ^ { s z } \ : = \ : \sum _ { n = 0 } ^ { \infty } p _ { n } ( s ) z ^ { n }
$$

are known as Appel Polynomials.

Differentiating (2.6.31) $j$ times with respect to $s$ we obtain

$$
\frac { z ^ { j + 1 } e ^ { s z } } { e ^ { z } - 1 } = \sum _ { n = 0 } ^ { \infty } \frac { B _ { n } ^ { ( j ) } ( s ) z ^ { n } } { n ! } , \quad | z | < 2 \pi .
$$

Set $s = 0 , 1$ in (2.6.33),and subtract,

$$
z ^ { j + 1 } \Bigg ( \frac { e ^ { z } - 1 } { e ^ { z } - 1 } \Bigg ) \ = \sum _ { n = 0 } ^ { \infty } \frac { B _ { n } ^ { ( j ) } ( 1 ) - B _ { n } ^ { ( j ) } ( 0 ) } { n ! } z ^ { n } , | z | < 2 \pi , j = 0 , 1 , . . .
$$

By the uniqueness theorem for power series we must have

$$
\frac { B _ { j + 1 } ^ { ( j ) } ( 1 ) - B _ { j + 1 } ^ { ( j ) } ( 0 ) } { ( j + 1 ) ! } = 1 \quad \mathrm { w h i l e } \quad B _ { r } ^ { ( j ) } ( 1 ) - B _ { r } ^ { ( j ) } ( 0 ) = 0 , r \ne j + 1 .
$$

We see now that the polynomials ${ \cal B } _ { \bf 0 } ( x ) , { \cal B } _ { \bf 1 } ( x ) , \dots .$ and the functionals

$$
L _ { 0 } ( f ) = f ( 0 ) , L _ { 1 } ( f ) = f ( 1 ) - f ( 0 ) ,
$$

$$
L _ { 2 } ( f ) = \frac { f ( 1 ) - f ^ { \prime } ( 0 ) } { 2 ! } , L _ { 3 } ( f ) = \frac { f ^ { \prime \prime } ( 1 ) - f ^ { \prime \prime } ( 0 ) } { 3 ! } , \ldots ,
$$

form a biorthogonal set.

Ex.4 (Orthogonal Polynomials)． Though these polynomials will be treated in detail in Chapter $\mathbf { x }$ ,it is interesting to note how they fit in with Theorem 2.6.1 and Corollary 2.6.2.Let $X = C [ a , b ]$ .Let $w ( x )$ be a fixed positive weight function for which the integrals $\int _ { a } ^ { b } w ( x ) x ^ { n } d x , n = 0 , 1 , 2 , . . .$ ,all exist. Introduce the functionals $L _ { n } ( f ) \ = \int _ { a } ^ { b } w ( x ) x ^ { n } f ( x ) d x , n \ = \ 0 , 1 , 2 , . . . . .$ These are the weighted moments of $f$ .It will then be possible to biorthonormalize the powers $1 , x , x ^ { 2 } , \ldots ,$ against these functionals. (In Chapter VIII it will be shown that the determinant condition for this is fulfilled.)We then obtain $^ { \pmb { a } }$ sand $^ { b }$ s such that

$$
\begin{array} { c l c r } { { } } & { { } } & { { L _ { n } { } ^ { * } ( f ) = \displaystyle \int _ { a } ^ { b } w ( x ) ( a _ { n 0 } + a _ { n 1 } x + \cdot \cdot \cdot + a _ { n n } x ^ { n } ) f ( x ) d x } } \\ { { } } & { { } } & { { } } \\ { { \displaystyle p _ { n } ( x ) = b _ { n 0 } + b _ { n 1 } x + \cdot \cdot \cdot + b _ { n n - 1 } x ^ { n - 1 } + x ^ { n } } } \\ { { } } & { { } } & { { L _ { n } { } ^ { * } ( p _ { j } ( x ) ) = \delta _ { n j } . } } \end{array}
$$

A glance at the determinants (2.6.21) shows that the a's and ó's in (2.6.35) are proportional. Indeed,since $L _ { i } ( x ^ { j } ) = \int _ { a } ^ { b } w ( x ) x ^ { i } x ^ { j } d x = L _ { j } ( x ^ { i } )$ ，the minors corre-sponding to elements $\boldsymbol { x } _ { i }$ and $\pmb { L _ { i } }$ are equal. After accounting for the factors $\scriptstyle Q _ { n - 1 }$ and $\scriptstyle { \pmb { G } } _ { n }$ infront of these determinants,we find

$$
L _ { n } { } ^ { * } ( f ) \ = \int _ { a } ^ { b } w ( x ) \ { \frac { G _ { n - 1 } } { G _ { n } } } p _ { n } ( x ) f ( x ) \ d x .
$$

If we now set

$$
p _ { n } { * } ( x ) = \sqrt { \frac { G _ { n - 1 } } { G _ { n } } } p _ { n } ( x )
$$

we shall have

$$
\begin{array} { l } { \displaystyle \sqrt { \frac { G _ { j - 1 } } { G _ { j } } } \sqrt { \frac { G _ { n } } { G _ { n - 1 } } } L _ { n } { } ^ { * } ( p _ { j } ) = \delta _ { n j } } \\ { \displaystyle = \int _ { a } ^ { b } w ( x ) \sqrt { \frac { G _ { n - 1 } } { G _ { n } } } p _ { n } ( x ) \sqrt { \frac { G _ { j - 1 } } { G _ { j } } } p _ { j } ( x ) d x } \\ { \displaystyle = \int _ { a } ^ { b } w ( x ) p _ { n } { } ^ { * } ( x ) p _ { j } { } ^ { * } ( x ) d x . } \end{array}
$$

The polynomials ${ { p } _ { n } } ^ { * }$ are called orthonormal over $[ a , b ]$ with respect to the weight $w ( x )$ .They are determined up to a factor of $\pm 1$ .(2.6.21) and (2.6.37) now give us the following determinant representation for the orthonormal polynomials

$$
\begin{array} { r } { p _ { n } \pmb { * } ( x ) = C _ { n } \left| \begin{array} { c c c c } { ( 1 , 1 ) } & { ( 1 , x ) } & { \cdots \cdot } & { ( 1 , x ^ { n } ) } \\ { ( x , 1 ) } & { ( x , x ) } & { \cdots \cdot } & { ( x , x ^ { n } ) } \\ { \cdot } & { } & { } & { \cdot } \\ { \cdot } & { } & { } & { \cdot } \\ { \cdot } & { } & { \cdot } \\ { ( x ^ { n - 1 } , 1 ) } & { ( x ^ { n - 1 } , x ) } & { \cdots \cdot } & { ( x ^ { n - 1 } , x ^ { n } ) } \\ { \phantom { \cdot } } & { } & { \cdot \cdot } & { x ^ { n } } \end{array} \right| } \end{array}
$$

where

$$
( x ^ { i } , x ^ { j } ) = \int _ { a } ^ { b } w ( x ) x ^ { i + j } d x
$$

and

with

$$
\begin{array} { l } { { C _ { n } = ( G _ { n } G _ { n - 1 } ) ^ { - \frac { 1 } { 2 } } \nonumber } } \\ { { G _ { n } = \left| ( x ^ { i } , x ^ { j } ) \right| _ { i , j = 0 } ^ { n } . } } \end{array}
$$

# 2.7Successive Differences

DEFINITIoN 2.7.1. Let there be given a sequence of values yo, Y1, .\*.. The differences of adjacent values are designated by

$$
\Delta y _ { k } = y _ { k + 1 } - y _ { k } , ~ k = 0 , 1 , \cdots .
$$

Higher diferences are defined similarly

$$
\Delta ^ { 2 } y _ { k } = \Delta ( \Delta y _ { k } ) = \Delta y _ { k + 1 } - \Delta y _ { k } = ( y _ { k + 2 } - y _ { k + 1 } ) - ( y _ { k + 1 } - y _ { k } ) .
$$

In general,

$$
\Delta ^ { n + 1 } y _ { k } = \Delta ( \Delta ^ { n } y _ { k } ) = \Delta ^ { n } y _ { k + 1 } - \Delta ^ { n } y _ { k } .
$$

We define $\Delta ^ { 0 } y _ { k } = y _ { k }$

THEOREM 2.7.1. We have

$$
\begin{array} { r l } & { \Delta ^ { 0 } y _ { k } = y _ { k } } \\ & { \Delta ^ { 1 } y _ { k } = y _ { k + 1 } - y _ { k } } \\ & { \Delta ^ { 2 } y _ { k } = y _ { k + 2 } - 2 y _ { k + 1 } + y _ { k } } \\ & { \Delta ^ { 3 } y _ { k } = y _ { k + 3 } - 3 y _ { k + 2 } + 3 y _ { k + 1 } - y _ { k } } \end{array}
$$

In general,

$$
\Delta ^ { n } y _ { k } = \sum _ { r = 0 } ^ { n } ( - 1 ) ^ { n - r } { \binom { n } { r } } y _ { k + r } , \quad { \binom { n } { r } } = { \frac { n ! } { r ! ( n - r ) ! } } .
$$

Proof: Formula (2.7.4) holds trivially for ${ \pmb n } = { \bf 0 }$ ，and this begins an inductive proof. Assume (2.7.4) true for $\pmb { n }$ Then,

$$
\begin{array} { r l } & { \Delta ^ { n + 1 } y _ { k } = \Delta ( \Delta ^ { n } y _ { k } ) = \Delta \Big ( \underset { r = 0 } { \overset { n } { \sum } } ( - 1 ) ^ { n - r } \Big ( \underset { r } { \overset { n } { \sum } } y _ { k + r } \Big ) } \\ & { \qquad = \underset { r = 0 } { \overset { n } { \sum } } ( - 1 ) ^ { n - r } \Big ( \underset { r } { \overset { n } { \sum } } \Big ) \Delta y _ { k + r } = \underset { r = 0 } { \overset { n } { \sum } } ( - 1 ) ^ { n - r } \binom { n } { r } ( y _ { k + 1 + r } - y _ { k + r } ) } \\ & { \qquad = \underset { r = 1 } { \overset { n + 1 } { \sum } } ( - 1 ) ^ { n + 1 - r } \Big ( \underset { r = 1 } { \overset { n } { \binom { n } { r } } } y _ { k + r } - \underset { r = 0 } { \overset { n } { \sum } } ( - 1 ) ^ { n - r } \Big ( \underset { r } { \overset { n } { \sum } } \Big ) y _ { k + r } } \\ & { \qquad = \underset { r = 1 } { \overset { n } { \sum } } ( - 1 ) ^ { n + 1 - r } y _ { k + r } \Big [ \Big ( \underset { r = 1 } { \overset { n } { \sum } } \Big ) + \binom { n } { r } \Big ] + \binom { n } { n } y _ { k + n + 1 } - ( - 1 ) ^ { n } \binom { n } { 0 } y } \\ & { \qquad = \underset { r = 0 } { \overset { n + 1 } { \sum } } ( - 1 ) ^ { n + 1 - r } y _ { k + r } \Big ( \underset { r } { \overset { n } { \sum } } + 1 \Big ) . } \end{array}
$$

Thus,if the formula is true for $\pmb { n }$ ,it must be true for $n + 1$ ,and the induction is complete.

COROLLARY 2.7.2. For $\pmb { k } = \mathbf { 0 }$ we have

$$
\Delta ^ { n } y _ { 0 } = \sum _ { r = 0 } ^ { n } ( - 1 ) ^ { n - r } { \binom { n } { r } } y _ { r } .
$$

In the case of interpolation at abscissas $z _ { 0 } , z _ { 1 } , . . .$ , that are spaced evenly:

$$
z _ { 0 } = a , z _ { 1 } = a + h , z _ { 2 } = a + 2 h , . . . , z _ { n } = a + n h ,
$$

the divided differences may be given an elegant expression in terms of successive differences.If $w ( z ) = ( z - z _ { 0 } ) ( z - z _ { 1 } ) \cdot \cdot \cdot ( z - z _ { n } )$ ,then

$$
w ^ { \prime } ( z _ { k } ) = ( z _ { k } - z _ { 0 } ) ( z _ { k } - z _ { 1 } ) \cdot \cdot \cdot ( z _ { k } - z _ { k - 1 } ) ( z _ { k } - z _ { k + 1 } ) \cdot \cdot \cdot ( z _ { k } - z _ { n } ) .
$$

Since $z _ { i } - z _ { j } = ( i - j ) h$ ，

$$
\begin{array} { c } { { w ^ { \prime } ( z _ { k } ) = ( k h ) ( k - 1 ) h \cdot \cdot \cdot ( h ) ( - h ) ( - 2 h ) \cdot \cdot \cdot ( - ( n - k ) h ) } } \\ { { = h ^ { n } k ! ( n - k ) ! ( - 1 ) ^ { n - k } . } } \end{array}
$$

Therefore from (2.6.4),

$$
{ \begin{array} { r l } & { a _ { n } = [ y _ { 0 } , y _ { 1 } , \dots , y _ { n } ] = \displaystyle \sum _ { k = 0 } ^ { n } { \frac { y _ { k } } { w ^ { \prime } ( z _ { k } ) } } } \\ & { \quad = \displaystyle \sum _ { k = 0 } ^ { n } { \frac { ( - 1 ) ^ { n - k } y _ { k } } { h ^ { n } k ! ( n - k ) ! } } = { \frac { 1 } { n ! h ^ { n } } } \sum _ { k = 0 } ^ { n } ( - 1 ) ^ { n - k } { \binom { n } { k } } y _ { k } } \\ & { \quad = \displaystyle { \frac { \Delta ^ { n } y _ { 0 } } { n ! h ^ { n } } } . } \end{array} }
$$

We can therefore prove the following theorem.

THEOREM 2.7.3. Let $\pmb { p } ( z )$ be the unique polynomial of $\mathcal { P } _ { n }$ that takes on the values $y _ { 0 } , y _ { 1 } , \ldots , y _ { n }$ at the $n + 1$ points $a , a + h , \ldots , a + n h$ . Then

$$
{ \begin{array} { r l } & { p _ { n } ( z ) = y _ { 0 } + { \cfrac { \Delta y _ { 0 } } { h } } ( z - a ) + { \cfrac { \Delta ^ { 2 } y _ { 0 } } { 2 ! h ^ { 2 } } } ( z - a ) ( z - a - h ) + \cdots } \\ & { \qquad + { \cfrac { 1 } { n ! h ^ { n } } } \Delta ^ { n } y _ { 0 } ( z - a ) ( z - a - h ) \cdot \cdot \cdot ( z - a - ( n - 1 ) h ) . } \end{array} }
$$

If $p _ { n } ( f ; z )$ interpolates to $f$ at $a , a + h , \ldots , a + n h$ then

$$
\begin{array} { l } { { p _ { n } ( f ; z ) = f ( a ) + \displaystyle \frac { \Delta f ( a ) } { h } ( z - a ) + \displaystyle \frac { 1 } { 2 ! h ^ { 2 } } \Delta ^ { 2 } f ( a ) ( z - a ) ( z - a - h ) + \cdots } } \\ { { \mathrm { } + \displaystyle \frac { 1 } { n ! h ^ { n } } \Delta ^ { n } f ( a ) ( z - a ) ( z - a - h ) \cdot \cdot \cdot ( z - a - ( n - 1 ) h ) . \quad ( 2 . 7 . 1 } } \end{array}
$$

We have written

$$
\begin{array} { l } { \Delta f ( a ) = f ( a + h ) - f ( a ) } \\ { \Delta ^ { 2 } f ( a ) = f ( a + 2 h ) - 2 f ( a + h ) + f ( a ) , \mathrm { { e t c . } } } \end{array}
$$

Formulas (2.7.9) and (2.7.10) are known as Newton's forward diffrence formulas.

If $f ( x )$ is defined at ${ \pmb a } , { \pmb a } + \hbar , { \pmb a } + 2 \hbar , . . . .$ ,the formal series

$$
f ( x ) \sim \sum _ { k = 0 } ^ { \infty } { \frac { \Delta ^ { k } f ( a ) } { k ! h ^ { k } } } ( z - a ) ( z - a - h ) \cdot \cdot \cdot ( z - a - ( k - 1 ) h )
$$

is called a Newton series for $f$

Ex.1. $\mathbf { I f } f ( x ) = x ^ { n }$ ,then $\Delta f ( x ) = n h x ^ { n - 1 } + \cdot \cdot \cdot .$ The first difference is therefore a polynomial of degree $n \mathrm { ~ - ~ } 1$ .Similarly,we find $\Delta ^ { n } x ^ { n } \ = n ! \ h ^ { n }$ and $\Delta ^ { p } x ^ { n } = 0$ for $\textit { \textbf { p } } > n$

Ex.2.If $f \left( x \right) = e ^ { \sigma x }$ then $\Delta f ( x ) = ( e ^ { \sigma h } - 1 ) \epsilon ^ { \sigma x }$ Iterating this, $\Delta ^ { n } f ( x ) =$ $( e ^ { \sigma h } - 1 ) ^ { n } e ^ { \sigma x }$

Ex.3.If $f \left( x \right) \in \mathcal { P } _ { n }$ then the series (2.7.12） converges to $f ( x )$ .From Ex. 1, the series reduces to a sum of $n + 1$ terms and,by Theorem 2.7.3,is that member of ${ \mathcal { P } } _ { n }$ which interpolates to $f$ at $a , a \ + \ h , \ . \ . \ . \ , a \ + \ n h$ By uniqueness,it must coincide with $f$

Ex.4．On the other hand,the function $f ( x ) = \sin \pi x$ has zeros at ${ \bf 0 } , { \bf \pm 1 }$ ， $\pm 2 , . . .$ ,so thatwith $a = 0 , h = 1 , \Delta ^ { k } f ( 0 ) \equiv 0$ .The series (2.7.12) is identically zero and does not represent $f ( x )$ over any interval.An entire function may still not be sufficiently restricted in its behavior to be represented by its Newton series.

# NOTES ON CHAPTER II

2.1The discussion of polynomial interpolation in Chapters II and II can be amplified by related material in any text on numerical analysis.Mention should be made also of the numerous practical articles of H.E.Salzer related to interpolation.

2.3Abel-Gontscharoff Interpolation:J.M.Whittaker [l],p.38；V.L. Gontscharoff [1]，pp.84-86.Lidstone Interpolation:D. V. Widder [3], R.P.Boas,Jr.[2].Hermite's Interpolation:A.A.Markoff[l]; Gontscharoff [l],p.64.Hermite's formulas are rediscovered and republished every few years.Generalized Taylor Interpolation:D.V.Widder[l],[2],I.M. Sheffer [l].Trigonometric Interpolation,A. Zygmund [l],Vol.II.

2.4For additional examples of unisolvent systems,see Polya and Szego [1],vol.II,pp.45-52.Further theory is presented in Achieser [l],p.67 et seq.and in Motzkin [l].References to recent work related to Haar's Theorem can be found in Buck [2].

2.5-2.6 General formulae of Lagrange and Newton type have been given implicitly and explicitly by many authors.For instance,see the articles by Widder and Shefer cited in 2.3. Also: W. E. Milne [1]. H. B. Curry [1] develops these notions and contains some further references.

Bernoulli Polynomials: N.E. Norlund [1].

Appel Polynomials: Boas and Buck [1], E. D. Rainville [1].

2.7For the algebraic side of differences,consult books on difference calculus such as Fort [l]. There are extensive studies of the convergence of interpolation series some of which are found in books:Norlund [1],Whittaker[l].A.O.Gelfand [1] has a noteworthy treatment of Newton series and allied questions.See also Buck[1].

# PROBLEMS

1. If $V ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } )$ designates the Vandermonde determinant, show that $V ( 1 , 2 , 3 , . . . , n ) = 1 ! 2 ! 3 ! \cdot \cdot \cdot ( n - 1 ) !$

2. Can a parabola $\pmb { p }$ be found for which $\mathcal { p } ( 0 ) , \mathcal { p } ^ { \prime \prime } ( 0 ) , \mathcal { p } ^ { \prime \prime \prime } ( 0 )$ have preassigned values? For which $\int _ { - 1 } ^ { 1 } p ( x ) \ : d x , p ( 0 ) , p ^ { \prime } ( 0 ) \ :$ have preassigned values?

3.Construct a polynomial in $\mathscr { P } _ { 3 }$ for which $\begin{array} { r } { p ( 0 ) = 1 , p ( 1 ) = 3 , p ^ { \prime } ( - 1 ) = 4 , } \end{array}$ $p ^ { \prime \prime } ( 0 ) = 0$ .Is the answer unique?

4.Three points lie on a nonvertical line.What happens when you try to fit a parabola to them?A cubic?Formulate a general statement.

5.Show that wecan not alwaysfindafunctionoftheformf(x)= that passes through three points with distinct abscissas.

6.Is it possible to fit a curve of the form $f ( x ) = A + B e ^ { C x }$ to the data $f ( 0 ) = 0 , f ( 1 ) = 1 , f ( 2 ) = \frac { 1 } { 2 } ?$

7. $x$ consists of all functions of the form $a _ { 0 } + a _ { 1 } x + a _ { 2 } y + a _ { 3 } x ^ { 2 } + a _ { 4 } x y + a _ { 5 } y ^ { 2 }$ defined on $- 1 \leq x \leq 1$ ， $- 1 \le y \le 1$ .Find a basis for $x ^ { * }$ ·

8. Let $X = \mathcal { P } _ { n }$ considered on $0 \leq x \leq 1$ Let $0 < x _ { 0 } < \cdots < x _ { n } \leq 1$ Prove that $L _ { j } ( f ) = \int _ { 0 } ^ { x _ { j } } f ( t ) d t , j = 0 , 1 , . . . , n ,$ ，are independent over $x *$ ·

9.Select the constants $A , \ldots , E$ so that $\frac { A + B x + C x ^ { 2 } } { 1 + D x + E x ^ { 2 } }$ ：agrees with the Maclaurin series expansion of $e ^ { \mathfrak { X } }$ as far as $x ^ { 4 }$ .How close is the resulting rational function to $e ^ { \ast }$ over the interval $| x | \leq { \frac { 1 } { 1 0 } }$ ？

10. If $R ( x ) = { \frac { A + B x } { 1 + C x } }$ ， can the interpolation problem $R ( 0 ) = f ( 0 ) , R ^ { \prime } ( 0 ) =$ $f ^ { \prime } ( 0 ) , R ^ { \prime \prime } ( 0 ) = f ^ { \prime \prime } ( 0 )$ always be solved?What about a similar problem for rational functions of higher degree? The resulting rational functions are called the Padé Approximants to $f ( x )$

11. Let $x _ { 0 } , x _ { 1 } , \ldots , x _ { n }$ be fixed．Let $p ( x ) = a _ { 0 } + a _ { 1 } x + \cdot \cdot \cdot + a _ { n } x ^ { n }$ and $p ( x _ { i } ) = y _ { i }$ Given an $\varepsilon > 0$ , we can find a $\pmb { \delta }$ such that $\left| y _ { i } \right| \le \delta$ implies $\left. a _ { i } \right. \leq \varepsilon$

12.Discuss the possibility of trigonometric interpolation with Taylor conditions.

13.Discuss the possibility of osculatory trigonometric interpolation.

14. Let $T ( x ) = a _ { 0 } + a _ { 1 } \cos x + b _ { 1 }$ sin $x + \cdots + a _ { n }$ cos ${ \pmb n } { \pmb x } + { \pmb b } _ { \pmb n }$ sin $_ { n x }$ Consider $e ^ { i n x } T ( x ) = P _ { 2 n } ( e ^ { i x } )$ and show that the number of real roots modulo $\pmb { 2 \pi }$ of $\pmb { T } ( \pmb { x } )$ ,each root counted with its multiplicity,is $\leq 2 n$ ·


<!-- chunk 0002: pages 71-140 -->
15. If $a _ { 0 } + a _ { 1 } \cos x + \cdot \cdot \cdot + a _ { n }$ cos nx vanishes at $n + 1$ points,

$$
0 \leq x _ { 0 } < x _ { 1 } \cdot \cdot \cdot < x _ { n } < \pi ,
$$

it vanishes identically.

16. If b sin x + ..: + bn sin nx vanishes at n points,0 <x1 <·. < xn <π, it vanishes identically.

17. Let $s _ { 1 } , s _ { 2 } , \ldots , s _ { n }$ be distinct. Then the set $e ^ { \pmb { \mathscr { s } } _ { 1 } \pmb { x } } , \ldots , e ^ { \pmb { \mathscr { s } } _ { n } \pmb { x } }$ is unisolvent over any interval.

$$
p _ { n } ( x ^ { n + 1 } ; x ) = x ^ { n + 1 } - ( x - x _ { 0 } ) ( x - x _ { 1 } ) \cdot \cdot \cdot ( x - x _ { n } ) .
$$

19.Let $G ( x _ { 1 } , \dots , x _ { n } ) = ( L _ { i } ( x _ { j } ) )$ Set $y _ { k } = \sum _ { i = 1 } ^ { n } a _ { k i } x _ { i }$ and $T = ( a _ { i j } )$ Then, $G ( y _ { 1 } , \cdot \cdot \cdot , y _ { n } ) = G ( x _ { 1 } , \cdot \cdot \cdot , x _ { n } ) T ^ { \prime }$ ， $\mathbf { \delta } _ { \mathbf { \mathcal { T } } ^ { \prime } } =$ transpose of $\pmb { T }$ .Prove a corresponding result for a linear transformation of the ${ \pmb { L } } ^ { * } { \pmb { \ 8 } }$

20.In Theorem 2.5.1,determine the ${ \boldsymbol { x } } _ { i } { } ^ { * }$ explicitly in terms of determinants.

21.Prove the following‘dual”of Theorem 2.5.1.Let $x$ be a linear space of dimension $\pmb { n }$ and let $x _ { 1 } , x _ { 2 } , \ldots , x _ { n }$ be $\pmb { n }$ independent elements. Then,there are determined uniquely $\pmb { n }$ independent elements of $X ^ { * } , L _ { 1 } { } ^ { * } , \ldots , L _ { n } { } ^ { * }$ ，such that ${ { L } _ { i } } ^ { * } ( x _ { j } ) = { { \delta } _ { i j } }$

22. Show that if the abscissas $x _ { 1 } \neq x _ { 2 } ,$ then ${ L _ { 1 } } ^ { * } ( f ) = \frac { { x _ { 2 } } f ( x _ { 1 } ) - { x _ { 1 } } f ( x _ { 2 } ) } { x _ { 2 } - x _ { 1 } }$ and ${ L _ { 2 } } ^ { * } ( f ) = \frac { f ( x _ { 2 } ) - f ( x _ { 1 } ) } { x _ { 2 } - x _ { 1 } }$ are biorthonormal to the functions ${ \mathbf { 1 } } , { \boldsymbol { x } }$ Interpret in $\mathbf { \boldsymbol { X } } = \mathcal { P } _ { \mathbf { 1 } }$

$\frac { ( - 1 ) ^ { n } \sin z } { z - n \pi }$ 23.The functions and the functionals

$$
L _ { n } ( f ) = f ( n \pi ) n = 0 , \pm 1 , \pm 2 , . . . ,
$$

are biorthonormal. The infinite expansion of form (2.6.17) is

$$
f ( z ) \sim \sin z \sum _ { n = - \infty } ^ { \infty } { \frac { ( - 1 ) ^ { n } f \left( n \pi \right) } { z - n \pi } } .
$$

It is called the Cardinal Series for $f$

24.Biorthogonalize 1, $x , x ^ { 2 }$ ....,against

$$
L _ { 0 } ( f ) = \int _ { 0 } ^ { 1 } f ( x ) d x , L _ { 1 } ( f ) = \int _ { 0 } ^ { 2 } f ( x ) d x , . . . .
$$

Compute the first three polynomials.

25. Let $\vert L _ { i } ( x _ { j } ) \vert _ { i , j = 1 } ^ { n } \neq 0$ . Then there is a permutation of the elements

$$
x _ { 1 } , x _ { 2 } , \ldots , x _ { n } { \mathrm { : ~ } } x _ { 1 } { \mathrm { ' ~ } } , x _ { 2 } { \mathrm { ' ~ } } , \ldots , x _ { n } { \mathrm { ' ~ } }
$$

such that $| L _ { i } ( \boldsymbol { x _ { j } } ^ { \prime } ) | _ { i , j = 1 } ^ { k } \neq 0 , k = 1 , 2 , \ldots , n .$ ，(Cf.the hypotheses of Theorem 2.6.1.)

26. Compute the first four Bernoulli polynomials from (2.6.30) or (2.6.31).

27. Calculate the nth divided diference for $f ( x ) = { \frac { 1 } { x } }$

28. Prove that $f ( n ) = \sum _ { k = 0 } ^ { n } { \binom { n } { k } } \Delta ^ { k } f ( 0 ) .$

29.Express $x ^ { 2 }$ ， $x ^ { 3 }$ ， $x ^ { 4 }$ as linear combinations of l $\mathbf { \sigma } _ { \cdot } , \mathbf { \vec { x } } , \mathbf { \vec { x } } ( \mathbf { \vec { x } } - \mathbf { \vec { l } } )$ ， $x ( x \textrm { -- } 1 ) ( x \textrm { -- } 2 )$ ， $x ( x \mathrm { ~ - ~ } 1 ) ( x \mathrm { ~ - ~ } 2 ) ( x \mathrm { ~ - ~ } 3 )$ ·

30.Verify the formal Newton Series

$$
\begin{array} { c } { { e ^ { \sigma z } \sim 1 + ( e ^ { \sigma } - 1 ) z + \displaystyle \frac { ( e ^ { \sigma } - 1 ) ^ { 2 } } { 2 ! } z ( z - 1 ) + \cdots , } } \\ { { \displaystyle \frac { 1 } { t - z } \sim \frac { 1 } { t } + \displaystyle \frac { z } { t ( t - 1 ) } + \displaystyle \frac { z ( z - 1 ) } { t ( t - 1 ) ( t - 2 ) } + \cdots . } } \end{array}
$$

31.Verify the formal Newton series

$\log \ \Gamma ( 1 + z ) \sim { \frac { \log 2 } { 2 ! } } z ( z - 1 ) + { \frac { ( \log 3 - 2 \log 2 ) } { 3 ! } } z ( z - 1 ) ( z - 2 ) + \cdot \cdot \cdot z$
