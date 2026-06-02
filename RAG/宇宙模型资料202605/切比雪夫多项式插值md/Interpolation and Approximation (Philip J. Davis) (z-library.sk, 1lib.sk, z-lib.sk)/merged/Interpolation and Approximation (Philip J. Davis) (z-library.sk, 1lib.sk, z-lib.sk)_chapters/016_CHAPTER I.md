# CHAPTER I

# Introduction

This chapter contains material from algebra and analysis that will be of use in the later portions of the book.It is presented here for ready reference and for review.The reader is assumed to be familiar with some of the theorems.Other theorems may be less familiar and their proofs have been given.Though $L ^ { p }$ spaces are mentioned in Theorem l.4.0,they do not reappear until Chapter VII,and only the elementary portions of measure and integration theory are used.

1.1 Determinants. Let $\boldsymbol { v } _ { i }$ designate the $\pmb { n }$ -tuple of numbers $( a _ { i 1 } , a _ { i 2 } ,$ $\cdots , a _ { i n } )$ . For a constant $\pmb { \alpha }$ , we shall mean by $\alpha v _ { i }$ the $\pmb { n }$ -tuple $( \alpha a _ { i 1 } , \alpha a _ { i 2 } , \ldots ,$ ${ \alpha } a _ { i n } )$ ，while by $\pmb { v } _ { i } + \pmb { v } _ { j }$ ，we shall mean the $\pmb { n }$ -tuple $( a _ { i 1 } + a _ { j 1 }$ ， ${ a _ { i } } _ { 2 } + { a _ { j } } _ { 2 } ,$ ：, ${ a } _ { i n } + { a } _ { j n } )$ .The letters $e _ { 1 } , \ldots , e _ { n }$ will designate the unit $\pmb { n }$ -tuples (1,0,0, $\ldots , 0 )$ ， $( 0 , 1 , 0 , \ldots , 0 ) , \ldots , ( 0 , 0 , 0 , \ldots , 1 ) .$ ，The function of the $\pmb { n } ^ { 2 }$ variables $\pmb { a } _ { i j }$ $( i , j = 1 , 2 , \ldots , n )$ , known as the determinant of those quantities, is generally written

$$
D = { \left| \begin{array} { l l l l } { a _ { 1 1 } } & { a _ { 1 2 } } & { \cdots } & { a _ { 1 n } } \\ { a _ { 2 1 } } & { a _ { 2 2 } } & { \cdots } & { a _ { 2 n } } \\ { \cdot } & { } & { } & { \cdot } \\ { \cdot } & { } & { \cdot } \\ { \cdot } & { } & { \cdot } \\ { a _ { n 1 } } & { a _ { n 2 } } & { \cdots } & { a _ { n n } } \end{array} \right| } = | a _ { i j } | = D ( v _ { 1 } , v _ { 2 } , \ldots , v _ { n } ) .
$$

The determinant is completely characterized by the following three properties

$$
\begin{array} { l } { { D ( v _ { 1 } , v _ { 2 } , \ldots , v _ { i } , \ldots , v _ { n } ) = D ( v _ { 1 } , v _ { 2 } , \ldots , v _ { i } + v _ { j } , \ldots , v _ { n } ) } } \\ { { ( i \neq j ) \ ( \mathrm { I n v a r i a n c e } ) . } } \\ { { D ( v _ { 1 } , v _ { 2 } , \ldots , \alpha v _ { i } , \ldots , v _ { n } ) = \alpha D ( v _ { 1 } , v _ { 2 } , \ldots , v _ { i } , \ldots , v _ { n } ) } } \end{array}
$$

$$
D ( e _ { 1 } , e _ { 2 } , \ldots , e _ { n } ) = 1 { \mathrm { ( N o r m a l i z a t i o n ) } } .
$$

The whole of determinant theory can be built up from this starting point and is related to the theory of the volume of an $\pmb { n }$ -dimensional parallelotope.

Given an $\pmb { n }$ by $\pmb { n }$ matrix $A = ( a _ { i j } )$ ，the determinant associated with this matrix is designated by $| A |$ or det $\pmb { A }$ .If from the array $\pmb { A }$ we delete the ith row and the jth column,a certain $( n - 1 )$ by $( n - 1 )$ submatrix $A _ { i j }$ will remain.The determinant associated with this submatrix is known as the minor of the element $\pmb { a } _ { i j }$ .The quantity $( - 1 ) ^ { i + j } \left| A _ { i j } \right|$ is the cofactor of $\boldsymbol { a } _ { i j } .$ For the cofactor we write $A _ { i j } { } ^ { * }$ .The following rules of computation for determinants are fundamental.

(a) $| { \cal A } | = | { \cal A } ^ { \prime } |$ ， $A ^ { \prime } =$ transpose of $A = ( a _ { j i } )$   
(b) If two rows (or columns) of $\pmb { A }$ are interchanged, producing a matrix $\scriptstyle A _ { 1 }$ ，then $| A | = - | A _ { 1 } |$   
（c） If two rows (or columns) of $\pmb { A }$ are identical,then $| { \cal A } | = 0$   
(d) If a row (or column), $\pmb { v }$ of $\pmb { A }$ is replaced by kv producing a matrix $\scriptstyle A _ { 1 }$ ,then $| A _ { 1 } | = k \left| A \right|$   
(e) If a scalar multiple $k v _ { i }$ of the ith row (or column) is added to the jth row (or column) $\boldsymbol { v } _ { j }$ ， $( i \neq j )$ and （ the matrix $A _ { 1 }$ results, then $| { \cal A } | = | { \cal A } _ { 1 } |$

(f) A determinant may be evaluated in terms of cofactors :

$$
\begin{array} { r l } { { | { \cal A } | = \displaystyle \sum _ { i = 1 } ^ { n } a _ { i j } A _ { i j } { } ^ { * } } } & { { \quad 1 \le j \le n } } \\ { { } } & { { } } \\ { { = \displaystyle \sum _ { j = 1 } ^ { n } a _ { i j } A _ { i j } { } ^ { * } } } & { { \quad 1 \le i \le n . } } \end{array}
$$

The expansion (f) is of considerable utility for it reduces an $\textit { \textbf { n } } \times \textit { \textbf { n } }$ determinant to a sum of $\pmb { n }$ determinants of order $\pmb { n } - \pmb { 1 }$ . Coupled with the elementary equation $| a _ { \mathbf { 1 1 } } | = a _ { \mathbf { 1 1 } }$ ,it contains within it a recursive definition of a determinant.The complete expansion of a determinant in terms of the matrix elements is less useful theoretically and hardly at all numerically.

1.2 Solution of Linear Systems of Equations. Consider the system of $\pmb { n }$ linear equations in $\pmb { n }$ unknowns $x _ { 1 } , x _ { 2 } , \ldots , x _ { n }$

$$
\sum _ { j = 1 } ^ { n } a _ { i j } x _ { j } = b _ { i } \qquad ( i = 1 , 2 , . . . , n ) .
$$

THEOREM 1.2.1 (Cramer's Rule).If $| A | = | a _ { i j } | \neq 0$ ,then (1.2.1) possesses a unique solution given by

$$
x _ { r } = { \frac { \displaystyle \sum _ { i = 1 } ^ { n } A _ { i r } { } ^ { * } b _ { i } } { | A | } } \qquad r = 1 , 2 , \ldots , n .
$$

THEOREM 1.2.2 (The Alternative Theorem). The homogeneous system

$$
\sum _ { j = 1 } ^ { n } a _ { i j } x _ { j } = 0 \qquad ( i = 1 , 2 , . . . , n )
$$

possesses a non-trivial solution (i.e., $\pmb { a }$ solution other than $x _ { 1 } = x _ { 2 } = \cdots =$ $\begin{array} { r } { x _ { n } = 0 \quad } { } \end{array}$ if and only if $| { \cal A } | = 0$ If for $\pmb { a }$ fixed $A = ( a _ { i j } )$ there are solutions to the non-homogeneous system (1.2.i) for every selection of the quantities $\boldsymbol { b } _ { i }$ then $| A | \neq 0$ and the homogeneous system has only the trivial solution.

1.3 Linear Vector Spaces. It will be useful to formulate many questions of interpolation and approximation theory within an abstract framework.The notion of a linear vector space over a field $\pmb { F }$ is therefore a basic one.

DEFINITioN l.3.l. A linear vector space (or a linear space) $\pmb { X }$ is a set of elements (or vectors) $\boldsymbol { \mathscr { x } } , \boldsymbol { \mathscr { y } } , \ldots$ ,for which two types of operation are possible. Any two elementsx, $y \in X$ determine a unique element $\pmb { x } + \pmb { y } \in \pmb { X }$ as their sum.Each element $\pmb { x } \in \pmb { X }$ and each scalar $\pmb { \alpha }$ ofa given field $\pmb { F }$ determine a unique element $\pmb { \alpha } \pmb { x } \in \pmb { X }$ as a scalar product.Vector sums and scalar products are required to obey the following laws.

(a) ${ \pmb x } + { \pmb y } = { \pmb y } + { \pmb x } .$   
(b) ${ \pmb x } + ( { \pmb y } + { \pmb z } ) = ( { \pmb x } + { \pmb y } ) + { \pmb z } .$   
(c） There exists a unique element $\mathbf { 0 } \in X$ such that $\pmb { x } + \pmb { 0 } = \pmb { x }$ for all $\pmb { x } \in \pmb { X }$   
(d) To each ${ \pmb x } \in { \pmb X }$ there exists a unique inverse - $_ { \pmb { x } }$ such that ${ \pmb x } + ( - { \pmb x } ) = 0$   
(e) $\alpha ( \beta x ) = ( \alpha \beta ) x$ for all $\alpha , \beta \in F , x \in X$   
(f) $\alpha ( { \pmb x } + { \pmb y } ) = \alpha { \pmb x } + \alpha { \pmb y } .$   
（g） $( \alpha + \beta ) x = \alpha x + \beta x$   
(h) $\mathbf { l } ( { \pmb x } ) = { \pmb x }$

Couditions (a)-(d) are frequently summed up by saying that the elements of $\pmb { X }$ form an Abelian group under addition.The element O is called the zero vector.

In this book,the underlying field $\pmb { F }$ of scalars will be either (l) the feld of real numbers,or (2) the feld of complex numbers.We can,therefore, speak either of a real or a.complex linear vector space.

DEFINITIoN 1.3.2. An expression of the form

$$
\alpha _ { 1 } x _ { 1 } + \alpha _ { 2 } x _ { 2 } + \cdots + \alpha _ { n } x _ { n } ; \alpha _ { i } \in I , x _ { i } \in X
$$

is called a linear combination of the $_ { \ast }$ s.

DEFINITioN 1.3.3. A finite set of vectors $x _ { 1 } , \ldots , x _ { n }$ is linearlydependent if we can find constants (i.e., scalars) $\alpha _ { 1 } , \alpha _ { 2 } , \ldots , \alpha _ { n } ;$ ，not all zero such that $\alpha _ { 1 } x _ { 1 } + \alpha _ { 2 } x _ { 2 } + \cdot \cdot \cdot + \alpha _ { n } x _ { n } = 0$ .If such is not the case,the vectors are calledindependent.

DEFINITION 1.3.4． Let $\pmb { n }$ be a positive integer. Suppose that we can find $\pmb { n }$ vectors $x _ { 1 } , x _ { 2 } , \ldots .$ ， $x _ { n } \in X$ which are independent while every $n + 1$ vectors are dependent.Then $\pmb { X }$ is said to be a linear space of dimension $\pmb { n }$ If no such $_ { n }$ exists,then $\pmb { X }$ is called an infinite dimensional space.

DEFINITIoN l.3.5. A set of elements $x _ { 1 } , x _ { 2 } , \ldots$ , is said to be a basis for $\pmb { X }$ if the $x _ { i }$ are independent and if every $x \in X$ can be expressed (uniquely) as a linear combination of the $x _ { i }$

THEOREM 1.3.1． $\pmb { X }$ has finite dimensionnif and only if it has a basis of $\pmb { n }$ elements.If $\pmb { X }$ has dimension n any $\mathscr { n }$ independent elementsconstitute $\pmb { a }$ basis.

Ex.1．The Real, $_ n$ -dimensional,Cartesianpace $\scriptstyle { R _ { n } }$ .This consists of vectors $_ x$ which are $_ n$ -tuples of real numbers: ${ \boldsymbol { x } } = ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } )$ . Let $y = ( y _ { 1 } , y _ { 2 } , \dotsc , y _ { n } )$ be a second vector.( $x$ and $_ y$ are considered equal if and only if $x _ { i } = y _ { i } , i =$ $1 , 2 , \ldots , n .$ ）Vector addition is defined by

$$
x + y = ( x _ { 1 } + y _ { 1 } , x _ { 2 } + y _ { 2 } , . . . , x _ { n } + y _ { n } ) .
$$

Scalar multiplication is defined by $\alpha x = ( \alpha x _ { 1 } , \alpha x _ { 2 } , \ldots , \alpha x _ { n } )$ .We set $0 \ \simeq$ $( \mathbf { 0 } , 0 , \ldots , \mathbf { 0 } )$ and $- x = ( - x _ { 1 } , - x _ { 2 } , . ~ . ~ . ~ , - x _ { n } )$ .The $_ n$ vectors, $\boldsymbol { e } _ { 1 } = ( 1 , 0 , \dots , 0 )$ ， $e _ { 2 } = ( 0 , 1 , . ~ . ~ . ~ , 0 ) , . ~ . ~ . ~ , e _ { n } = ( 0 , 0 , . ~ . ~ . ~ , 1 )$ ,known as unit vectors,are independent.

Ex.2. The Complex, $_ n$ -dimensional,Cartesian pace $C _ { n }$ .This consists of $_ { n }$ tuples of complex numbers: $( z _ { 1 } , z _ { 2 } , \ldots , z _ { n } )$ .The laws of combination are as in Ex. 1.

Ex.3.Linear Spaces of Functions.In this example,a function,considered asa whole,is thought of as constituting an element ofa space.Let $\pmb { S }$ designate a point set lying on the real axis.Consider the totality of real-valued functions with domain $\boldsymbol { s }$ .Call this totality $_ { T }$ $\Gamma . { \bf F o r } f , g \in T$ ,define their sum $f + g$ by means of

$$
( f + g ) ( x ) = f ( x ) + g ( x ) , x \in S .
$$

Define a scalar product by means of

$$
( \alpha f ) ( x ) \ = \alpha f ( x ) , x \in S .
$$

Let the zero vector be the function of $\pmb { T }$ that vanishes identically.Let $- f$ designate the function defined by

$$
( - f ) ( x ) \ = \ - f ( x ) , x \in S .
$$

With these definitions, $\pmb { T }$ is a linear vector space.If $\boldsymbol { s }$ contains more than a finite number of points, $\pmb { T }$ is of infinite dimension.

1.4 The Hierarchy of Functions. Our dealings will be almost exclusively with functions of a single real or complex variable.We shall work with finite intervals in the real case and bounded sets in the complex case. The deeper analytical properties of interpolation and approximation depend to a great extent on what may be called “the degree of smoothness”of the function approximated.In order of increasing smoothness,we shall deal with: $L ^ { p }$ functions,bounded functions,continuous functions,functions satisfying a Lipschitz condition,differentiable functions, $\pmb { n }$ -times differentiable functions,infinitely differentiable functions,analytic functions,entire functions,polynomials of restricted degree,constants.It will become apparent in subsequent chapters that the processes of interpolation and approximation become stronger when applied to functions further down this list.We shall now define these classes of functions and recall some basic facts about them.

DEFINITION 1.4.0. Let $\pmb { p } > 0$ .The class of functions $f ( x )$ which are measurable and for which $| f ( x ) | ^ { p }$ is integrable over $[ a , b ]$ is known as $L ^ { p } [ \pmb { a } , \pmb { b } ]$ If $\pmb { p } = 1$ , the class is designated by $L [ \boldsymbol { a } , \boldsymbol { b } ]$

THEOREM 1.4.0. (a) $L ^ { p } [ { \pmb { a } } , { \pmb { b } } ]$ is $^ { \pmb { a } }$ linear space. (b) If $f \in L [ a , b ]$ ，then $f \geq 0$ and $\int _ { a } ^ { b } f ( x ) d x = 0$ imply $f = 0$ almost everywhere. (c) If $f \in L [ a , b ]$ ， then $g ( x ) = \int _ { a } ^ { x } f ( x ) d x$ is continuous. (d) $1 f - \infty < a < b < \infty$ ，then $f \in L ^ { p } [ a , b ] , p ^ { \prime } < p$ ,implies $f \in L ^ { p \prime } [ a , b ]$ (e) $I f f \in L ^ { p } [ a , b ]$ with $\pmb { \mathscr { p } } \geq 1$ , we can find an absolutely continuous function $g ( x )$ such that $\int _ { a } ^ { b } | f ( x ) - g ( x ) | ^ { p } d x \leq \varepsilon$ for arbitrary $\varepsilon > 0$

For these results,the reader is referred to standard texts on integration theory.

Let $s$ denote a point set in $\scriptstyle { R _ { n } }$ or in the complex plane and $P$ a point in that set. Though Definitions 1.4.l-l.9.l are meaningful for complex valued functions of a real variable,we shall generally deal with real valued functions whenever $\boldsymbol { s }$ is in $\scriptstyle { R _ { n } }$

DEFINITION l.4.1． A function $f$ is bounded on $\boldsymbol { s }$ if there exists a constant $M$ such that

$$
| f ( P ) | \leq M { \mathrm { ~ f o r ~ a l l ~ } } P \in S .
$$

If no such constant exists,the function is said to be unbounded on $s$ .The class of functions which are bounded on $\boldsymbol { s }$ will be designated by $B ( S ) . ~ B ( S )$ is a lincar space.

Ex.1．The function $y = \sin x ^ { 2 }$ is bounded on $- \infty < x < \infty$

Ex.2．The Gamma function $y = \Gamma ( x )$ is unbounded on the interval $0 < x \le 1$ ， and on the interval $1 \leq x < \infty$ ·

Ex.3.If $[ a , b ]$ is a finite interval, $f \in B [ a , b ]$ and measurable there implies $f \in L ^ { p } [ a , b ]$ for all $\pmb { \mathscr { p } } > \pmb { 0 }$

DEFINITION 1.4.2． Let the function $f$ be defined on the set $\pmb { S }$ It is continuous at a point $P _ { 0 }$ of $\pmb { S }$ if

$$
\operatorname* { l i m } _ { n \to \infty } f ( P _ { n } ) = f ( P _ { 0 } )
$$

whenever $P _ { n } \to P _ { 0 }$ ， $P _ { n } \in { \mathcal { S } }$ If $f$ is defined on an interval $[ \pmb { a } , \pmb { b } ]$ and is continuous at ${ \pmb x } _ { \pmb 0 } \in [ { \pmb a } , { \pmb b } ]$ ,then given an $\varepsilon > 0$ ,we can find a $\pmb { \delta }$ such that

$$
| f ( x ) - f ( x _ { 0 } ) | \leq \varepsilon
$$

for all $| x - x _ { 0 } | \leq \delta$ in $[ a , b ]$ .The $\pmb { \delta }$ will depend upon $f , \pmb { x _ { 0 } } ,$ and $\varepsilon$ The class of functions continuous on $I \colon [ a , b ]$ will be designated by $C [ \pmb { a } , \pmb { b } ]$ .It is a linear space.

It may occur that for a given $f$ and ε we can find a $\pmb { \delta }$ for which (1.4.3) holds independently of $\pmb { x _ { 0 } }$ 、This leads to the notion of uniform continuity.

DEFINITION 1.4.3． A function $f$ is uniformly continuous over a set $\pmb { S }$ if given an $\varepsilon > 0$ ,we can find a $\pmb { \delta }$ such that

$$
| f ( x _ { 1 } ) - f ( x _ { 2 } ) | \leq \varepsilon
$$

for all $| x _ { 1 } - x _ { 2 } | \leq \delta ; x _ { 1 } , x _ { 2 } \in S$

I one important case,the lotions of continuity and uniform continuity coincide:

THEOREM l.4.1. A function which is continuous on a compact (i.e.,closed and bounded) point set is uniformly continuous there.

Ex.1．The function $A ( x ) = \left| x \right|$ is continuous on $- \infty < x < \infty$

Ex.2．The function $f ( x ) = ( 1 + e ^ { 1 / x } ) ^ { - 1 }$ is discontinuous at $\pmb { x } = \pmb { 0 }$ however ${ f ( 0 ) }$ may be defined,for $\operatorname* { l i m } _ { x \to 0 ^ { + } } f ( x ) = 0$ while $\operatorname* { l i m } _ { x \to 0 ^ { - } } f ( x ) \ = \ 1$ .It is continuous elsewhere.

Ex.3．The function $f ( x ) = { \frac { 1 } { x } }$ is continuous on the open interval $( \mathbf { 0 } , \textstyle { \frac { 1 } { 2 } } )$ but is not uniformly continuous there.

Ex.4. The function $f ( x ) = { \frac { 1 } { 1 + x ^ { 2 } } }$ is uniformly continuous over the whole   
line $- \infty < x < \infty$ ,for we have

$$
\left| \frac { 1 } { 1 + { x _ { 1 } } ^ { 2 } } - \frac { 1 } { 1 + { x _ { 2 } } ^ { 2 } } \right| = \frac { | { x _ { 2 } } ^ { 2 } - { x _ { 1 } } ^ { 2 } | } { ( 1 + { x _ { 1 } } ^ { 2 } ) ( 1 + { x _ { 2 } } ^ { 2 } ) } \le | { x _ { 2 } } - { x _ { 1 } } | \frac { ( | { x _ { 1 } } | + | { x _ { 2 } } | ) } { ( 1 + { x _ { 1 } } ^ { 2 } ) ( 1 + { x _ { 2 } } ^ { 2 } ) } .
$$

Inasmuch as

$$
{ \frac { | x _ { 1 } | } { 1 + { x _ { 1 } } ^ { 2 } } } \leq { \frac { 1 } { 2 } } , { \frac { | x _ { 1 } | + | x _ { 2 } | } { ( 1 + { x _ { 1 } } ^ { 2 } ) ( 1 + { x _ { 2 } } ^ { 2 } ) } } \leq 1 .
$$

Thus,

THEOREM 1.4.2 (First Mean Value Theorem for Integrals).

$L e t f , g \in C [ a , b ]$ . Suppose moreover that ${ \pmb g } \ge { \pmb 0 }$ there. Then,

$$
\int _ { a } ^ { b } f ( x ) g ( x ) \ d x = f ( \xi ) { \int _ { a } ^ { b } g ( x ) \ d x }
$$

for some ${ \pmb \xi }$ with $a \le \xi \le b$ The theorem is also true if ${ \pmb g } \in { \pmb L } [ { \pmb a } , { \pmb b } ]$ ， $g \geq 0$ a.e. It is occasionally useful to have inforination about the best $\pmb { \varepsilon }$ which goes with a given $\pmb { \delta }$ in the definition of uniform continuity.

DEFINITION 1.4.4． Let $f ( x )$ be defined on an interval $\pmb { I }$ Set

$$
w ( \delta ; f ) = w ( \delta ) = \operatorname* { s u p } | f ( x _ { 1 } ) - f ( x _ { 2 } ) |
$$

where the sup is taken over all pairs ${ \pmb x _ { 1 } } , { \pmb x _ { 2 } } \in I$ for which $| x _ { 1 } - x _ { 2 } | \leq \delta$ The function $w ( \delta )$ (which depends on $f$ )is called the modulus of continuity of $f$ on $\pmb { I }$

$$
f ( x ) = x ^ { 2 } , I = ( 0 , 1 ) , w ( \delta ) = 2 \delta - \delta ^ { 2 } .
$$

Ex. 6. $f ( x ) = \frac { 1 } { x } , I = ( 0 , 1 ) , w ( \delta ) = + \infty .$

Ex. 7. $f ( x ) = \sin \frac { 1 } { x } , I = ( 0 , 1 ) , w ( \delta ) \equiv 2 .$

THEOREM 1.4.3．Let $f ( x ) \in C [ a , b ]$ The modulus of continuity has the following properties

$$
{ \pmb w } ( { \bf 0 } ) = { \bf 0 }
$$

$$
w ( \delta _ { 1 } + \delta _ { 2 } ) \leq w ( \delta _ { 1 } ) + w ( \delta _ { 2 } ) \ ( S u b a d d i t i v i t y )
$$

$$
w ( n \delta ) \leq n w ( \delta ) .
$$

Moreover, $w ( \delta ) \in C [ 0 , b - a ]$ ·

Proof:(l.4.7) is obvious. Since $| x _ { 1 } - x _ { 2 } | \le \delta _ { 1 }$ implies $| x _ { 1 } - x _ { 2 } | \leq \delta _ { 2 } ,$ the corresponding sup cannot decrease,and (1.4.8) follows. To prove (l.4.9),observe that if $0 \le x _ { 2 } - x _ { 1 } \le \delta _ { 1 }$ ,then $| f ( x _ { 1 } ) - f ( x _ { 2 } ) | \leq w ( \delta _ { 1 } ) \leq w ( \delta _ { 1 } ) + w ( \delta _ { 2 } )$ On the other hand,if $\delta _ { 1 } < x _ { 2 } - x _ { 1 } \le \delta _ { 1 } + \delta _ { 2 } ,$ then $\pmb { x _ { 1 } } + \pmb { \delta _ { 1 } } < \pmb { x _ { 2 } }$ and $x _ { 2 } - ( x _ { 1 } + \delta _ { 1 } ) < \delta _ { 2 }$ But,

$$
\begin{array} { r } { | f ( x _ { 1 } ) - f ( x _ { 2 } ) | \leq | f ( x _ { 1 } ) - f ( x _ { 1 } + \delta _ { 1 } ) | + | f ( x _ { 1 } + \delta _ { 1 } ) - f ( x _ { 2 } ) | } \\ { \leq w ( \delta _ { 1 } ) + w ( x _ { 2 } - ( x _ { 1 } + \delta _ { 1 } ) ) \leq w ( \delta _ { 1 } ) + w ( \delta _ { 2 } ) . } \end{array}
$$

Therefore, $w ( \delta _ { 1 } + \delta _ { 2 } ) = \operatorname* { s u p } _ { \substack { 0 \leq x _ { 2 } - x _ { 1 } \leq \delta _ { 1 } + \delta _ { 2 } } } | f ( x _ { 1 } ) - f ( x _ { 2 } ) | \leq w ( \delta _ { 1 } ) + w ( \delta _ { 2 } ) .$ (1.4.10) follows immediately from (1.4.9)by induction. From (l.4.8 and 9), $0 \le w ( \delta + \delta _ { 1 } ) - w ( \delta ) \le w ( \delta _ { 1 } )$ Now， by Theorem 1.4.1, $\operatorname* { l i m } _ { \delta _ { 1 } \to 0 } \ w ( \delta _ { 1 } ) = 0$ and hence $\pmb { w }$ is continuous at $\delta$

# 1.5 Functions Satisfying a Lipschitz Condition

DEFINITION 1.5.1． Let $f ( x )$ be defined on an interval $\boldsymbol { \mathit { I } }$ and suppose we can find two positive constants $M$ and $\pmb { \alpha }$ such that

$$
| f ( x _ { 1 } ) - f ( x _ { 2 } ) | \leq M | x _ { 1 } - x _ { 2 } | ^ { \alpha } { \mathrm { ~ f o r ~ a l l ~ } } x _ { 1 } , x _ { 2 } \in I .
$$

Then $f$ is said to satisfy a Lipschitz Condition of order $\pmb { \alpha }$ .The class of such functions will be designated by Lip $\pmb { \alpha }$ .When it is useful to put the constant $\pmb { M }$ in evidence, one writes $\operatorname { L i p } _ { M } \alpha$ ·

THEOREM 1.5.1． Lip $\pmb { \alpha }$ is a linear space. If $f \in \operatorname { L i p } \alpha$ on $\boldsymbol { \mathit { I } }$ ，then $f$ is continuous；indeed，uniformly continuous on $\pmb { I }$ If $f \in \operatorname { L i p } \alpha$ with $\alpha > 1$ then $f = c o n s t a _ { i }$ nt.If $f \in \operatorname { L i p } \alpha$ ,it may fail to be differentiable,but if it possesses $^ { \pmb { a } }$ derivative satisfying $| f ^ { \prime } ( x ) | \leq M$ then $f \in \operatorname { L i p } _ { M } 1$ .If $\alpha < \beta$ then Lip ${ \pmb { \alpha } } = \mathbf { L i p } \beta$ The conditions $f \in \operatorname { L i p } _ { M } \alpha$ and $w ( \delta ) \leq M \delta ^ { \alpha }$ are equivalent.

Ex.1.Let $0 ~ < \alpha < 1$ Let $x > 0 , h > 0$ .Then ${ \frac { d } { d x } } \left[ ( x + h ) ^ { \alpha } - x ^ { \alpha } \right] =$ $\alpha [ ( x + h ) ^ { \alpha - 1 } - x ^ { \alpha - 1 } ] < 0$ Therefore $( x + h ) ^ { \alpha } - x ^ { \alpha }$ is decreasing for all $x \ge 0$ and hence $( x + h ) ^ { \alpha } - x ^ { \alpha } \leq h ^ { \alpha }$ ，This means that $x ^ { \alpha } \in$ Lip $\pmb { \alpha }$ on any positive interval.

# 1.6 Differentiable Functions

DEFINITION 1.6.1．Let $f ( x )$ be defined on an interval $\boldsymbol { \mathit { I } }$ It is said to be differentiableat a point $x _ { 0 } \in I$ if the following limit exists

$$
\operatorname* { l i m } _ { x \to x _ { 0 } } { \frac { f ( x ) - f ( x _ { 0 } ) } { x - x _ { 0 } } } = f ^ { \prime } ( x _ { 0 } ) .
$$

If $x _ { \mathbf { 0 } }$ is an end point of $\boldsymbol { \mathit { I } }$ then the limit in (1.6.l) is replaced by an appropriate one-sided limit.The function $f ( x )$ is differentiable on $\boldsymbol { \mathit { I } }$ if it is differentiable at each point of $\boldsymbol { I }$

Ex.1. $A ( x ) = \left| x \right|$ is differentiable at all $x \neq 0$ At $x = 0$ it possesses right and left hand derivatives $\operatorname* { l i m } _ { x \to 0 ^ { + } } , \operatorname* { l i m } _ { x \to 0 ^ { - } } \frac { A ( x ) - A ( 0 ) } { x - 0 }$

Ex. 2. $S ( x ) = \left\{ { \begin{array} { l l } { 0 \quad } & { x \leq 0 } \\ { 1 \quad } & { x > 0 } \end{array} } \right.$ is discontinuous at $x = 0$ and is not differentiable there.Elsewhere it is differentiable.

Ex. 3. $f ( x ) = x ^ { \frac { 1 } { 3 } }$ .Though continuous at ${ \pmb x } = { \bf 0 } , { \pmb f } ( { \pmb x } )$ fails to be differentiable there.It is sometimes convenient to write $f ^ { \prime } ( 0 ) = + \infty$

For differentiable functions,we have Rolle's Theorem and the Mean Value Theorem :

THEOREM 1.6.1 (Rolle). $L e t f ( x ) \in C [ a , b ]$ and be differentiable at each point of $( a , b )$ .If $f ( a ) = f ( b )$ then thereisa point ${ \pmb x } = { \pmb \xi }$ with $a < \xi < b$ for which $f ^ { \prime } ( \pmb { \xi } ) = 0$

THEOREM 1.6.2． Let $f ( x ) \in C [ a , b ]$ be differentiable at each point of $( a , b )$ Then we can find a ${ \pmb \xi }$ with $a < \xi < b$ such that

$$
f ( b ) = f ( a ) + ( b - a ) f ^ { \prime } ( \xi ) .
$$

If $f$ is differentiable at each point of $\pmb { I }$ ,its derivative $f ^ { \prime } ( x )$ may exhibit a wide variety of smoothness properties.A particularly noteworthy case is where $f ^ { \prime } ( x )$ is itself continuous on $\boldsymbol { \mathit { I } }$ .The class of functions that have a continuous derivative on $[ a , b ]$ is designated by $\scriptstyle C ^ { 1 } [ a , b ]$ .More generally,

DEFINITION 1.6.2. If $f ( x )$ is $\pmb { n }$ times differentiable on $[ \pmb { a } , \pmb { b } ]$ and if $f ^ { ( n ) } ( x )$ is itself continuous on $[ \pmb { a } , \pmb { b } ]$ ，we shall write $f ( x ) \in C ^ { n } [ a , b ]$

$C ^ { n } [ \pmb { a } , \pmb { b } ]$ is a linear space of functions.

Ex.4.Let

$$
f ( x ) = { \left\{ \begin{array} { l l } { x ^ { k } \quad } & { x \geq 0 } \\ { 0 \quad } & { x < 0 . } \end{array} \right. }
$$

Then, $f \in C ^ { k - 1 }$ on $- \infty < x < \infty$ .But $f \notin C ^ { k }$ on any interval containing the origin.

Ex.5.Let $f ( x ) = | x | ^ { \frac { 5 } { 2 } }$ .Then $f \in C ^ { 2 }$ ，but $f \not \in C ^ { 3 }$ on any interval containing the origin.

For functions having higher derivatives we have the following generalized Rolle's Theorem.

THEOREM 1.6.3． Let $n \geq 2$ Suppose that $\pmb { f } \in C [ \pmb { a } , \pmb { b } ]$ and let $f ^ { ( n - 1 ) } ( x )$ exist at each point of $( a , b )$ . Suppose that $f ( x _ { 1 } ) = f ( x _ { 2 } ) = \cdot \cdot \cdot = f ( x _ { n } ) = 0$ for $a \leq x _ { 1 } < x _ { 2 } < \cdot \cdot \cdot < x _ { n } \leq b $ Then there is $\pmb { a }$ point ${ \pmb \xi }$ ， $x _ { 1 } < \xi < x _ { n }$ such that $j ^ { ( n - 1 ) } ( \xi ) = 0$

Proof: We give the proof for $n = 3$ .The general case is similar. Let $f ( x _ { 1 } ) = f ( x _ { 2 } ) = f ( x _ { 3 } ) = 0$ Since $f$ is differentiable in $x _ { 1 } < x < x _ { 3 }$ we can find $\pmb { \xi _ { 1 } }$ and ${ \pmb { \xi _ { 2 } } }$ such that $x _ { 1 } < \xi _ { 1 } < x _ { 2 } < \xi _ { 2 } < x _ { 3 }$ and $f ^ { \prime } ( \pmb { \xi } _ { 1 } ) = 0$ ， $f ^ { \prime } ( \pmb { \xi } _ { 2 } ) = \mathbf { 0 }$

Since $f ^ { \prime \prime }$ also exists,a second application of Rolle's Theorem yields a $\pmb { \xi } ,$ $\xi _ { 1 } < \xi < \xi _ { 2 }$ with $f ^ { ( 2 ) } ( \xi ) = 0$

Taylor's Theorem with the exact remainder and the various expressions for the remainder involving higher derivatives constitute generalizations of the Mean Value Theorem.

THEOREM 1.6.4. Let $f ( x ) \in C ^ { n + 1 } [ a , b ]$ and let ${ \pmb x } _ { \pmb 0 } \in [ { \pmb a } , { \pmb b } ]$ . Then for all

$$
\begin{array} { c } { { a \leq x \leq b , f ( x ) = f ( x _ { 0 } ) + f ^ { \prime } ( x _ { 0 } ) ( x - x _ { 0 } ) + { \displaystyle \frac { f ^ { \prime \prime } ( x _ { 0 } ) } { 2 ! } } ( x - x _ { 0 } ) ^ { 2 } + \cdot \cdot \cdot } } \\ { { + { \displaystyle \frac { f ^ { ( n ) } ( x _ { 0 } ) } { n ! } } ( x - x _ { 0 } ) ^ { n } + { \displaystyle \frac { 1 } { n ! } } { \displaystyle \int _ { x _ { 0 } } ^ { x } } f ^ { ( n + 1 ) } ( t ) ( x - t ) ^ { n } d t . } } \end{array}
$$

THEOREM 1.6.5．Let $f ( x ) \in C ^ { n } [ a , b ]$ and let $f ^ { ( n + 1 ) } ( x )$ exist in $( a , b )$ . Then there isa ${ \pmb \xi }$ with $a < \xi < b$ such that

$$
\begin{array} { c } { { f ( b ) = f ( a ) + f ^ { \prime } ( a ) ( b - a ) + \displaystyle { \frac { f ^ { \prime } ( a ) } { 2 ! } } ( b - a ) ^ { 2 } + \cdots } } \\ { { + \displaystyle { \frac { f ^ { ( n ) } ( a ) } { n ! } } ( b - a ) ^ { n } + \displaystyle { \frac { f ^ { ( n + 1 ) } ( \xi ) } { ( n + 1 ) ! } } ( b - a ) ^ { n + 1 } . } } \end{array}
$$

A form of the remainder theorem (sometimes referred to as Young's form) is useful on occasion.

THEOREM 1.6.6． Let $f ( x )$ be $\pm 1$ times differentiable at ${ \pmb x } = { \pmb x } _ { \pmb 0 }$ Then,

$$
\begin{array} { c } { { f ( x ) = f ( x _ { 0 } ) + f ^ { \prime } ( x _ { 0 } ) ( x - x _ { 0 } ) + \displaystyle \cdots + \frac { f ^ { ( n ) } ( x _ { 0 } ) } { n ! } ~ ( x - x _ { 0 } ) ^ { n } } } \\ { { + \displaystyle \frac { ( x - x _ { 0 } ) ^ { n + 1 } } { ( n + 1 ) ! } \left[ f ^ { ( n + 1 ) } ( x _ { 0 } ) + \varepsilon ( x ) \right] } } \end{array}
$$

where

$$
\operatorname* { l i m } _ { x \to x _ { 0 } } \varepsilon ( x ) = 0 .
$$

Proof: Set

$$
R ( x ) = f ( x ) - f ( x _ { 0 } ) - f ^ { \prime } ( x _ { 0 } ) ( x - x _ { 0 } ) - \cdot \cdot \cdot - { \frac { ( x - x _ { 0 } ) ^ { n + 1 } } { ( n + 1 ) ! } } f ^ { ( n + 1 ) } ( x _ { 0 } ) .
$$

Then (l.6.5) is equivalent to showing that $\operatorname* { l i m } _ { x \to x _ { 0 } } { \frac { R ( x ) } { ( x - x _ { 0 } ) ^ { n + 1 } } } = 0$ = 0.By differentiating,we find that

$$
R ( x _ { 0 } ) = R ^ { \prime } ( x _ { 0 } ) = \cdot \cdot \cdot = R ^ { ( n + 1 ) } ( x _ { 0 } ) = 0 .
$$

Let $\varepsilon > 0$ . The functions

$$
P ( x ) = R ( x ) + \varepsilon ( x - x _ { 0 } ) ^ { n + 1 } , Q ( x ) = R ( x ) - \varepsilon ( x - x _ { 0 } ) ^ { n + 1 }
$$

are $\pmb { n } + \pmb { 1 }$ times differentiable at ${ x } = { x } _ { 0 }$ .Moreover, $P ^ { ( k ) } ( x _ { 0 } ) = 0 , Q ^ { ( k ) } ( x _ { 0 } ) = 0$ $k = 0 , 1 , \ldots , n$ ,while $P ^ { ( n + 1 ) } ( x _ { 0 } ) = \varepsilon ( n + 1 ) ! > 0$ ，

$$
Q ^ { ( n + 1 ) } ( x _ { 0 } ) = - ( n + 1 ) ! \varepsilon < 0 .
$$

This implies that $P ( { \pmb x } )$ increases monotonically in some interval $( \pmb { x _ { 0 } } , \pmb { x _ { 0 } } + \delta )$ while $Q ( x )$ decreases monotonically in $( x _ { 0 } , \ x _ { 0 } + \delta )$ Therefore，for $_ { \pmb { x } }$ in $( x _ { 0 } , x _ { 0 } + \delta )$ ，

$$
\begin{array} { l l l l l l } { R ( x ) + \varepsilon ( x - x _ { 0 } ) ^ { n + 1 } > 0 } \\ { R ( x ) - \varepsilon ( x - x _ { 0 } ) ^ { n + 1 } < 0 . } \end{array}
$$

Therefore,

$$
- \varepsilon < \frac { R ( x ) } { ( x - x _ { 0 } ) ^ { n + 1 } } < \varepsilon .
$$

Since ε is arbitrary,(l.6.8) implies that $\operatorname* { l i m } _ { x \to x _ { 0 } + } { \frac { R ( x ) } { ( x - x _ { 0 } ) ^ { n + 1 } } } = 0$ =0.A similar argument shows that $\operatorname* { l i m } _ { x \to x _ { 0 } - } { \frac { R ( x ) } { ( x - x _ { 0 } ) ^ { n + 1 } } } = 0$ ,and the proof is complete.

# 1.7Infinitely Differentiable Functions

DEFINITION 1.7.1．If $f ( x ) \in C ^ { n } [ a , b ]$ for $n = 0 , 1 , 2 , \ldots$ ,then $f$ is called infinitelydifferentiablein $[ a , b ]$ . We shall write $C ^ { \infty } [ \pmb { a } , \pmb { b } ]$ for the class of such functions.

Ex. 1. $f ( x ) = x ^ { 2 }$ is infinitely differentiable on $- \infty < x < \infty$

Ex. 2. $f ( x ) = { \frac { 1 } { 1 + x ^ { 2 } } }$ is infinitely differentiable on $- \infty < x < \infty$

Ex. 3. $f ( x ) = \sum _ { n = 1 } ^ { \infty } { \frac { \cos n x } { n ^ { \log n } } }$ is infitly diferetiable on $- \infty < x < \infty$ For since $| \cos n x | \le 1$ and $\sum _ { n = 1 } ^ { \infty } { \frac { 1 } { n ^ { \log n } } } < \infty$ ,the original series converges absolutely and uniformly. Since moreover,for any integer ： $p \ge 0 \sum _ { n = 1 } ^ { \infty } \frac { n ^ { p } } { n ^ { \mathrm { l o g } n } } < \infty$ ，the differentiated series of all orders converge uniformly and hence represent the respective derivatives of $f ( x )$

The functions of class $C ^ { \infty } [ { \pmb { a } } , { \pmb { b } } ]$ form a linear space.

If $f \in C ^ { \infty } [ a , b ]$ and ${ \pmb x } _ { \pmb 0 } \in [ { \pmb a } , { \pmb b } ]$ we may form the Taylor expansion

$$
f ( x ) \sim \sum _ { k = 0 } ^ { \infty } { \frac { f ^ { ( n ) } ( x _ { 0 } ) } { n ! } } ( x - x _ { 0 } ) ^ { n } .
$$

For a given $_ { \pmb { x } }$ this series may or may not converge. If it converges, it may or may not converge to $f ( x )$ . The famous function that displays this

behavior is

$$
f ( x ) = e ^ { - x ^ { - 2 } } , \quad x \neq 0 ; \quad f ( 0 ) = 0 .
$$

This function is in $C ^ { \infty } ( - \infty , \infty )$ and

$$
f ^ { ( n ) } ( 0 ) = 0 \qquad n = 0 , 1 , 2 , . . . .
$$

With $x _ { \mathbf { 0 } } = 0$ ，(1.7.1） converges to O for every $_ x$ .There are an infinity of functions of class $C ^ { \infty }$ for which (1.7,3) holds.If (1.7.1) converges to $f ( x )$ over an interval,we are led to the notion of an analytic function.

# 1.8 Functions Analytic on the Line

DEFINITION 1.8.1． Let $f ( x )$ be defined on $[ a , b ]$ and assume that at each point $x _ { \pmb 0 } \in [ \pmb { a } , \pmb { b } ]$ there is a power series expression of $f ( x )$ valid in some interval:

$$
f ( x ) = a _ { 0 } + a _ { 1 } ( x - x _ { 0 } ) + a _ { 2 } ( x - x _ { 0 } ) ^ { 2 } + \cdots , | x - x _ { 0 } | < p ( x _ { 0 } ) .
$$

Then $f ( x )$ is said to be analytic on the interval. We write $f ( x ) \in A [ a , b ] .$

$$
f ( x ) = [ ( x ) ( x - 1 ) ] ^ { - \frac { 1 } { 2 } } \in A [ \varepsilon , 1 - \varepsilon ] , 0 < \varepsilon < 1 - \varepsilon .
$$

Ex. 2. $f ( x ) = \int _ { 0 } ^ { x } e ^ { t ^ { 2 } } d t$ is analytic over theentire line $- \infty < x < \infty$

Ex.3. $A ( x ) = \left| x \right|$ is not analytic over an interval containing $x = 0$ inits interior.But it is“piece-wise”analytic.

THEOREM 1.8.1. $A [ { \pmb a } , { \pmb b } ]$ is $\pmb { a }$ linear space. If $f ( x ) \in A [ a , b ]$ then

$$
f ( x ) \in C ^ { \infty } [ a , b ] .
$$

The constants ${ \pmb a } _ { \pmb n }$ of (1.8.1) are

$$
a _ { n } = { \frac { 1 } { n ! } } f ^ { ( n ) } ( x _ { 0 } ) \qquad n = 0 , 1 , . . . .
$$

It does not follow conversely that if $f \in C ^ { \infty } [ a , b ]$ then $f \in A [ a , b ]$ This is demonstrated by the example (1.7.2).Another example is $f ( x ) = \sum _ { k = 1 } ^ { \infty } { \frac { \cos n x } { n ^ { \log n } } }$ which,as we have seen,is infinitely differentiable on $- \infty < x < \infty$ and of period $2 \pi$ .The ideas of Theorem l2.3.2 will show that $f ( x ) \not \in A [ - \pi , \pi ]$

# 1.9 Functions Analytic in a Region

DEFINITION 1.9.1． Let $\boldsymbol { R }$ be a region of the complex plane and let $f ( z )$ be a single valued function of the complex variable $\boldsymbol { z }$ defined in $\pmb { R }$ If $z _ { 0 } \in R , f ( z )$ is said to be analytic at ${ \boldsymbol { z } } _ { \mathbf { 0 } }$ (or regular at ${ z _ { \mathbf { 0 } } }$ ）if it has a representation of

the form

$$
f ( z ) = \sum _ { n = 0 } ^ { \infty } a _ { n } ( z - z _ { 0 } ) ^ { n }
$$

valid in some neighborhood of $z _ { 0 } \colon | z - z _ { 0 } | < p ( z _ { 0 } )$ .If $z _ { \mathbf { 0 } } = \infty$ , we require an expansion of the form

$$
f ( z ) = \sum _ { n = 0 } ^ { \infty } a _ { n } z ^ { - n } , | z | > p .
$$

A function is analytic (or regular) in $\pmb { R }$ if it is analytic at each point of $\pmb { R }$ We shall write $A ( R )$ for the class of such functions. $A ( R )$ is a linear space.

Ex.1.The function f(z) = $f ( z ) = { \frac { 1 } { 1 + z ^ { 2 } } }$ is analytic in any region not containing the points $z ~ = ~ \pm i$

Ex.2.The function $f ( z ) \ = \int _ { 0 } ^ { z } e ^ { t ^ { 2 } } \ d t$ is analytic inanyregionnot cotaining $z = \infty$ ·

Ex.3.A branch of the function $f ( z ) = ( z ( z \ : - \ : 1 ) ) ^ { \frac { 1 } { 2 } }$ may be selected that is regular in any rectangle $0 < \varepsilon \le x \le 1 - \varepsilon$ ， $- R \leq y \leq R$

The relationship between functions analytic on a line and functions analytic in a region is given by the following theorem.

THEOREM 1.9.1． Let $f ( x ) \in A [ a , b ]$ . Then we can fnd a region $\pmb { R }$ containing $[ a , b ]$ into which $f ( x )$ can be continued analytically such that $f ( z ) \in A ( R )$

Proof: For each point $x _ { \mathbf { 0 } } \in [ a , b ]$ there is a quantity $\pmb { \mathscr { p } } ( \pmb { x _ { 0 } } )$ and an expansion

$$
f ( x ) = \sum _ { n = 0 } ^ { \infty } a _ { n } ( x - x _ { 0 } ) ^ { n } { \mathrm { ~ v a l i d ~ i n ~ } } | x - x _ { 0 } | < p ( x _ { 0 } ) .
$$

When $_ { x }$ is replaced by $z = x + i y$ ，(1.9.3)defines an analytic continuation of $f ( x )$ into the circle $| z - x _ { 0 } | < p ( x _ { 0 } )$ Let $\pmb { x _ { 0 } }$ run through the interval $[ a , b ]$ .The circles $| z - x _ { 0 } | < p ( x _ { 0 } )$ cover $[ a , b ]$ .Let $\pmb { R }$ be the union of these circles. $\pmb { R }$ is an open set and is arcwise connected. For if p, $q \in R$ ，join $\pmb { p }$ to $x _ { 1 }$ and $\pmb q$ to ${ \pmb x } _ { \mathbf { 2 } } ^ { }$ ,the centers of their respective circles.Then the arc $p x _ { 1 } x _ { 2 } q$ lies in $\boldsymbol { R } , \boldsymbol { R }$ is therefore a region and $f ( x )$ can be continued analytically into it.

![](../chunks/Interpolation and Approximation (Philip J. Davis) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0070/auto/images/9956dcce49eec34f1a2b804e6707edc66dce61f94316b987947dce8994726e14.jpg)  
Figure 1.9.1.

Cauchy's Theorem is a basic tool in complex analysis.

THEOREM 1.9.2． Let $\pmb { R }$ be $^ { \pmb { a } }$ simply connected region and let $f ( z ) \in A ( R )$ Let $z _ { \mathbf { 0 } }$ lie in $\pmb { R }$ and suppose that $c$ is $^ { \pmb { a } }$ simple,closed,rectifiable curve which lies in $\pmb { R }$ and which goes around ${ z _ { 0 } }$ in the positive sense. Then

$$
f ^ { ( n ) } ( z _ { 0 } ) = { \frac { n ! } { 2 \pi i } } \int _ { C } { \frac { f ( z ) } { ( z - z _ { 0 } ) ^ { n + 1 } } } d z .
$$

Whenever the Cauchy integral formula is employed,it will be understood that $c$ satisfies the above conditions.

Analytic functions may be completely characterized by the growth of their derivatives,and this provides a second approach independent of power series.

THEOREM 1.9.3 (Pringsheim).Let $f ( x ) \in C ^ { \infty } [ a , b ]$ $\pmb { A }$ necessary and suffcient condition that $f \in A [ a , b ]$ is that there exist $\pmb { a }$ constant $r > 0$ such that

$$
| f ^ { ( n ) } ( x ) | \leq r ^ { n } n ! \quad a \leq x \leq b , \quad n = 0 , 1 , . . . .
$$

Proof: Sufficiency. Let $\pmb { x _ { 0 } }$ be a fixed point in $[ a , b ]$ and suppose that (1.9.5) holds. By Theorem 1.6.5 we have for ${ \pmb x } \in [ { \pmb a } , { \pmb b } ]$ ，

$$
f ( x ) = \sum _ { k = 0 } ^ { n - 1 } { \frac { f ^ { ( k ) } ( x _ { 0 } ) } { k ! } } ( x - x _ { 0 } ) ^ { k } + { \frac { f ^ { ( n ) } ( \xi ) } { n ! } } ( x - x _ { 0 } ) ^ { n } .
$$

This holds for all $\pmb { n }$ ,and $\xi = \xi ( n , x )$ is between $_ { \pmb { x } }$ and $\pmb { x _ { 0 } }$ In view of (1.9.5),

$$
\left| { \frac { f ^ { ( n ) } ( \xi ) } { n ! } } ( x - x _ { 0 } ) ^ { n } \right| \leq r ^ { n } | x - x _ { 0 } | ^ { n } ,
$$

so that if $| x - x _ { 0 } | < \frac { 1 } { r }$ ,the remainder in (1.9.6)willconverge to 0.The function $f$ possesses a power series expansion valid in a neighborhood of $\pmb { x _ { 0 } }$ This means that $f \in A [ a , b ]$ . Necessity. If $f \in A [ a , b ]$ ，then by Theorem 1.9.1,we can find a simply connected region $\pmb { R }$ containing $[ a , b ]$ in which $f$ is analytic. Let $\boldsymbol { c }$ be a curve surrounding $[ \pmb { a } , \pmb { b } ]$ and lying in $\pmb { R }$ .Then,for ${ \pmb x } _ { \pmb 0 } \in [ { \pmb a } , { \pmb b } ]$ ,we have from (1.9.4),

$$
\vert f ^ { ( n ) } ( x _ { 0 } ) \vert \leq { \frac { n ! } { 2 \pi } } \int _ { C } { \frac { \vert f ( z ) \vert } { \vert z - x _ { 0 } \vert ^ { n + 1 } } } d s .
$$

If $L ( C )$ denotes the length of $c$ and $\pmb { \delta }$ is the minimum distance from $c$ to $[ a , b ]$ ，then

$$
| f ^ { ( n ) } ( x ) | \leq { \frac { \operatorname* { m a x } _ { z \in C } \left| f ( z ) \right| L ( C ) n ! } { 2 \pi \delta ^ { n + 1 } } } = { \frac { M n ! } { \delta ^ { n } } } , a \leq x \leq b
$$

where $M$ is a constant independent of $\pmb { n }$ . It is now clear that we can find an $\boldsymbol { r }$ that makes (1.9.5) true.

Ex.4.Suppose $f \in A [ - 1 , 1 ]$ .It is impossible to have $f ^ { ( n ) } ( 0 ) = ( n ! ) ^ { 2 }$ For then, $\begin{array} { r } { ( n ! ) ^ { 2 } \leq r ^ { n } n ! } \end{array}$ ， $\textbf { \em n } = \textbf { 0 }$ ,1,....But,by Stirling's Theorem, $\tilde { \mathcal { V } } _ { n !  \mathrm { ~ \infty ~ } } ^ { - }$ so that we cannot find such an $\boldsymbol { r }$

On the other hand,if $f$ is analytic only in the semi-open interval $0 < x \le 1$ but is in $C ^ { \infty } [ 0 , 1 ]$ ，we may very well have $f ^ { ( n ) } ( 0 ) = ( n ! ) ^ { 2 }$ A theorem to this effect is developed in Chapter $\mathbf { v }$

Of great importance is the class of functions that are analytic in a circle $C _ { r } \colon | z | < r$ ，Here we have the fundamental theorem of Cauchy-Hadamard.

THEOREM 1.9.4．Let $f ( z ) \in A ( C _ { r } )$ but $\not \in A ( C _ { r ^ { \prime } } )$ if $r ^ { \prime } > r$ This holds if and only if

$$
r ^ { - 1 } = \operatorname* { l i m } _ { n \to \infty } \operatorname* { s u p } _ { \infty } \left| { \frac { f ^ { ( n ) } ( 0 ) } { n ! } } \right| ^ { 1 / n }
$$

THEOREM 1.9.5 (Maximum Principle). Let $f ( z )$ be analytic in a region $\pmb { R }$ and not be constant there.Let $z _ { \mathbf { 0 } }$ lie in $\boldsymbol { R }$ .Then in any neighborhood of $z _ { \mathbf { 0 } }$ there exists $^ { \pmb { a } }$ point $z _ { 1 }$ where $| f ( z _ { 1 } ) | > | f ( z _ { 0 } ) |$ If $f ( z _ { 0 } ) \neq 0$ ,then in any neighborhood of $z _ { \mathbf { 0 } }$ there is $\pmb { a }$ point $z _ { 2 }$ where $| f ( z _ { 2 } ) | < | f ( z _ { 0 } ) |$

# 1.10 Entire Functions

DEFINITION 1.10.l． A function $f ( x )$ is called entire ifit has a representation of the form

$$
f ( z ) = \sum _ { k = 0 } ^ { \infty } a _ { k } z ^ { k } \quad \mathrm { \ v a l i d ~ f o r ~ } | z | < \infty .
$$

We shall designate this class of functions by $\pmb { \cal E } , \pmb { \cal E }$ is a linear space.

Ex.1. Some examples of entire functions are

THEOREM 1.10.1． The function $f ( z ) = \sum _ { k = 0 } ^ { \infty } a _ { k } z ^ { k }$ is entire if and only if

$$
\operatorname* { l i m } _ { n  \infty } | a _ { n } | ^ { 1 / n } = 0 .
$$

Proof: This follows from (1.9.9).

# 1.11 Polynomials

DEFINITIoN 1.1l.1． By a polynomial of degree $\pmb { n }$ is meant a function of the form

$$
p _ { n } ( z ) = a _ { 0 } z ^ { n } + a _ { 1 } z ^ { n - 1 } + \cdots + a _ { n } , a _ { 0 } \neq 0 .
$$

The class of polynomials of degree $\leq n$ will be designated by $\mathcal { P } _ { n }$

One might distinguish between the classes of polynomials with real coeffcients and with complex coefficients.It will usually be clear from the context which class we are dealing with and separate notations will not be introduced.

$\mathcal { P } _ { n }$ is a linear space.

The following basic facts about polynomials should be recaled.

THEOREM 1.l1.l (Fundamental Theorem of Algebra).If $\pmb { n } \geq 1$ , a polynomial of degree n possesses a complex root.

THEOREm l.l1.2 (Factorization Theorem).If $\scriptstyle { \pmb { p } } _ { \pmb { n } } ( z )$ is a polynomial of degree $\pmb { n }$ then we may find $\pmb { n }$ complex numbers $z _ { 1 } , z _ { 2 } , \ldots , z _ { n }$ such that

$$
\begin{array} { c } { \qquad \nu _ { n } ( z ) = a _ { 0 } z ^ { n } + a _ { 1 } z ^ { n - 1 } + \cdot \cdot \cdot + a _ { n } } \\ { \qquad \equiv a _ { 0 } ( z - z _ { 1 } ) ( z - z _ { 2 } ) \cdot \cdot \cdot ( z - z _ { n } ) \quad ( a _ { 0 } \ne 0 } \end{array}
$$

The quantities $z _ { i }$ need not be distinct.If there are $r \leq n$ distinct roots $z _ { 1 } , z _ { 2 } , \ldots , z _ { r } ;$ ，then for appropriate positive integers $\alpha _ { 1 } , \alpha _ { 2 } , \ldots , \alpha _ { r } ,$ satisfying $\alpha _ { 1 } + \alpha _ { 2 } + \cdots + \alpha _ { r } = n$ ,we have

$$
p _ { n } ( z ) = a _ { 0 } ( z - z _ { 1 } ) ^ { \alpha _ { 1 } } ( z - z _ { 2 } ) ^ { \alpha _ { 2 } } \cdot \cdot \cdot ( z - z _ { r } ) ^ { \alpha _ { r } } .
$$

The ${ \pmb { \alpha } } _ { i }$ are uniquely determined and the zero $z _ { i }$ is known as an ${ \pmb { \alpha } } _ { i }$ fold zero. We have

$$
p _ { n } ( z _ { i } ) = { p _ { n } } ^ { \prime } ( z _ { i } ) = \dots = p _ { n } ^ { ( \alpha _ { i } - 1 ) } ( z _ { i } ) = 0 , p _ { n } ^ { ( \alpha _ { i } ) } ( z _ { i } ) \neq 0 .
$$

Conversely,these derivative conditions imply the above factorization.

THEOREM 1.11.3 (Uniqueness).If $f ( z ) \in \mathcal { P } _ { n }$ and $f$ vanishes at more than n distinct points then it vanishes identically.

Proof: Let the degree of $f$ be $k \leq n$ .By Theorem 1.11.2,

$$
f ( z ) = a _ { 0 } ( z - z _ { 1 } ) \cdot \cdot \cdot ( z - z _ { k } ) .
$$

By hypothesis,we can find a point $z ^ { * } \neq z _ { 1 } , z _ { 2 } , \ldots , z _ { k }$ such that $f ( z ^ { * } ) = 0$ Then, $0 = a _ { 0 } ( z ^ { * } - z _ { 1 } ) \cdot \cdot \cdot ( z ^ { * } - z _ { k } )$ so that ${ a _ { \mathbf { 0 } } } = 0$ .This implies that

$$
f ( z ) \equiv 0 .
$$

1.12 Linear Functionals and the Algebraic Conjugate Space. In many problems,we must associate a number with a function extracted from a given class of functions.For instance,to each function $f ( x )$ that has a continuous derivative on $[ a , b ]$ ，we may want to associate the number $\int _ { a } ^ { b } ( 1 + [ f ^ { \prime } ( x ) ] ^ { 2 } ) ^ { \frac { 1 } { 2 } } d x$ .To each function $\pmb { f } ( \pmb { x } , y )$ that is twice continuously differentiable over a closed bounded region $\pmb { B }$ ，we may have to form the number $\iint _ { B } { \left( \frac { \partial f } { \partial x } \right) ^ { 2 } } + \left( \frac { \partial f } { \partial y } \right) ^ { 2 } d x d y$ or even more simply, $f ( x _ { 0 } , y _ { 0 } )$ where $( x _ { 0 } , y _ { 0 } ) \in B$ .Such an association is known as a functional.An important restriction is that the association behave linearly,and this leads to the following definition.

DEFINITION 1.12.1． Let $X$ be a linear vector space and to each $_ x$ let there be associated a unique real (or complex) number designated by $\scriptstyle { L ( x ) }$ If for : $\mathfrak { e } , \mathfrak { y } \in X$ and for all real (or complex) $\alpha , \beta$ we have

$$
L ( \alpha x + \beta y ) = \alpha L ( x ) + \beta L ( y ) ,
$$

then $L$ is called a linear functional over $X$

Ex. 1. $X = C [ a , b ]$ . The elements of $x$ are functions $f ( x )$

$$
L ( f ) = \int _ { a } ^ { b } f ( x ) d x \quad { \mathrm { o r } } \quad L ( f ) = \int _ { a } ^ { b } x ^ { 2 } f ( x ) d x .
$$

$$
\begin{array} { r l } & { X = C ^ { 2 } [ a , b ] . \ L ( f ) \ = f ^ { \prime \prime } ( a ) + f ^ { \prime } ( b ) \ - f \bigg ( \frac { a \ + \ b } { 2 } \bigg ) . } \\ & { X \ = A [ a , b ] . \ L ( f ) \ = \displaystyle \int _ { a } ^ { b } f ( x ) \ d x \ - \sum _ { i = 1 } ^ { n } a _ { i } f ( x _ { i } ) , a \ \leq x _ { i } \ \leq b . } \end{array}
$$

Ex. 4. $X = A ( R )$ where $\scriptstyle { R }$ is a region of the complex plane. Let $C$ bea rectifiable curve lying in $\scriptstyle { R }$

$$
L ( f ) = \int _ { C } f ( z ) d z .
$$

Ex.5. ${ \ X = R _ { n } . \ x = ( x _ { 1 } , x _ { 2 } , . . . , x _ { n } ) }$ .Let $a _ { 1 } , \ldots , a _ { n }$ be fixed constants and set

$$
L ( x ) = \sum _ { i = 1 } ^ { n } a _ { i } x _ { i } .
$$

Interpolation theory is concerned with reconstructing functions on the basis of certain functional information assumed known.In many cases,the functionals are linear.

Functionals can be added to one another and scalar products can be formed. If,for instance, $f \in C ^ { 1 } [ a , b ]$ and

$$
L _ { 1 } ( f ) = \int _ { a } ^ { b } f ( x ) d x \quad { \mathrm { a n d } } \quad L _ { 2 } ( f ) = f ^ { \prime } \left( { \frac { a + b } { 2 } } \right) ,
$$

we can identify the functional

$$
L ( f ) = \alpha { \int _ { a } ^ { b } } f ( x ) d x + \beta f ^ { \prime } { \left( \frac { a + b } { 2 } \right) }
$$

with the expression $\alpha L _ { 1 } + \beta L _ { 2 } . L$ is itself a linear functional. These observations form the basis for the following definition.

DEFINITION 1.12.2． Let $\pmb { X }$ be a given linear space and let $L _ { 1 }$ and $L _ { 2 }$ be two linear functionals defined on $X$ . The sum of $L _ { 1 }$ and $L _ { 2 }$ and the scalar product of $\pmb { \alpha }$ and $L _ { 1 }$ are defined by

$$
\begin{array} { c } { { ( L _ { 1 } + L _ { 2 } ) ( x ) = L _ { 1 } ( x ) + L _ { 2 } ( x ) , x \in X } } \\ { { ( \alpha L _ { 1 } ) ( x ) = \alpha L _ { 1 } ( x ) . } } \end{array}
$$

It is a simple matter to show that the set of all linear functionals defined on $\pmb { X }$ combined by the above rules constitute a second linear space.

DEFINITION 1.12.3． Let $\pmb { X }$ be a given linear space.The set of linear functionals defined on $\pmb { X }$ and combined by (l.l2.2) forms a linear space called the algebraic conjugate space of $\pmb { X }$ and denoted by $x ^ { * }$

$x ^ { * }$ ，then，has elements that are linear functionals.We can speak of linear combinations, linear inderendence,dimension,bases,etc.,for linear functionals.

Ex.6. $X = C [ a , b ]$ .Let $x _ { 1 } , x _ { 2 } , \ldots , x _ { n }$ be $_ n$ distinct points lying in $[ a , b ]$ · Let $L _ { k } ( f ) = f ( x _ { k } )$ for $f \in X$ .Then $L _ { 1 } , L _ { 2 } , \ldots , L _ { n }$ are independent in $x ^ { * }$ .For otherwise,for constants $a _ { \mathbf { 1 } } , \ldots , a _ { n }$ not all zero, $a _ { 1 } L _ { 1 } + a _ { 2 } L _ { 2 } + \cdot \cdot \cdot + a _ { n } L _ { n } = 0$ (the O functional).Thus,for all $f \in C [ a , b ]$ $a _ { 1 } f ( x _ { 1 } ) + a _ { 2 } f ( x _ { 2 } ) + \cdot \cdot \cdot + a _ { n } f ( x _ { n } ) = 0$ . This is impossible.For if $a _ { k } \neq 0$ ，we may find a continuous function for which $f ( x _ { k } ) = 1 , f ( x _ { i } ) = 0 , i \neq k$ .This leads to the contradiction $a _ { k } = 0$

Ex. 7. $X = { \pmb { \mathscr P } } _ { n - 2 } [ a , b ]$ . The above $_ n$ functionals are linearly dependent.This isa consequence of the Lagrange interpolation formula in Chapter II.

THEOREM 1.12.1．If $\pmb { X }$ has dimension $\pmb { n }$ then $X ^ { * }$ has dimension n also.

Proof: Let $x _ { 1 } , x _ { 2 } , \ldots , x _ { n }$ be a basis ( $\mathbf { \lambda } _ { n }$ independent elements).Then for any ${ \pmb x } \in { \pmb X }$ ， $x = a _ { 1 } x _ { 1 } + a _ { 2 } x _ { 2 } + \cdot \cdot \cdot + a _ { n } x _ { n }$ in a unique way. Therefore, $L ( x ) = a _ { 1 } L ( x _ { 1 } ) + \cdot \cdot \cdot + a _ { n } L ( x _ { n } )$ .For any $\pmb { x } \in \pmb { X }$ set

$$
\begin{array} { l } { { L _ { 1 } ( x ) = a _ { 1 } } } \\ { { \ } } \\ { { L _ { 2 } ( x ) = a _ { 2 } } } \\ { { \ } } \\ { { . } } \\ { { \ . } } \\ { { L _ { n } ( x ) = a _ { n } . } } \end{array}
$$

$L _ { i }$ are linear functionals defned on $\pmb { X }$ ，They are independent,for,if not, we would have $\beta _ { 1 } L _ { 1 } + \beta _ { 2 } L _ { 2 } + \cdots + \beta _ { n } L _ { n } = 0$ with some $\beta _ { j } \neq 0$ .Then,

$$
\beta _ { 1 } L _ { 1 } ( x _ { j } ) + \beta _ { 2 } L _ { 2 } ( x _ { j } ) + \cdot \cdot \cdot + \beta _ { j } L _ { j } ( x _ { j } ) + \cdot \cdot \cdot + \beta _ { n } L _ { n } ( x _ { j } ) = 0 ( x _ { j } ) = 0 .
$$

But $L _ { i } ( x _ { j } ) = \delta _ { i j } = { \Big \{ } _ { 0 { \mathrm { ~ i f ~ } } i \neq j } ^ { 1 { \mathrm { ~ i f ~ } } i = j } { \Big . }$ so that we obtain $\beta _ { j } = 0$ ，a contradiction.

This shows that the dimension of $X ^ { * }$ is at least $\mathscr { n }$ .We next show it is at most $\pmb { n }$

Suppose we have $n + 1$ functionals, $L _ { 1 } , L _ { 2 } , \dots , L _ { n + 1 }$ .Consider the $n + 1$ $\pmb { n }$ -tuples

$$
[ L _ { i } ( x _ { 1 } ) , L _ { i } ( x _ { 2 } ) , \ldots , L _ { i } ( x _ { n } ) ] , \qquad i = 1 , 2 , \ldots , n + 1 .
$$

Since $\scriptstyle { R _ { n } }$ (or $C _ { n } )$ is of dimension $\pmb { n }$ ，these $\pmb { n }$ -tuples cannot be independent. Hence we can find numbers $\alpha _ { 1 } , \ldots , \alpha _ { n + 1 }$ not all zero such that

$$
\begin{array} { r l } & { \alpha _ { 1 } [ L _ { 1 } ( x _ { 1 } ) , \textrm { . . . , } L _ { 1 } ( x _ { n } ) ] + \cdot \cdot \cdot + \alpha _ { n + 1 } [ L _ { n + 1 } ( x _ { 1 } ) , \textrm { . . . , } L _ { n + 1 } ( x _ { n } ) ] } \\ & { \phantom { = } \quad \quad \quad \quad \quad \quad \quad \quad \quad = 0 = [ 0 , 0 , \textrm { . . . , } 0 ] . } \end{array}
$$

Therefore

$$
( \alpha _ { 1 } L _ { 1 } + \cdot \cdot \cdot + \alpha _ { n + 1 } L _ { n + 1 } ) ( x _ { i } ) = 0 , ~ \mathrm { f o r } ~ i = 1 , 2 , \ldots , n .
$$

By taking linear combinations,

$$
( \alpha _ { 1 } L _ { 1 } + \cdot \cdot \cdot + \alpha _ { n + 1 } L _ { n + 1 } ) ( x ) = 0 \quad \mathrm { f o r } \quad x \in X .
$$

Therefore $L _ { 1 } , \ldots , L _ { n + 1 }$ must be dependent and the dimension of $X ^ { * }$ is at most,and hence,precisely $\pmb { n }$

This theorem tells us that over a space $\pmb { X }$ of dimension $\pmb { n }$ any linear functional can be expressed as a linear combination of $\pmb { n }$ fixed independent linear functionals.

1.13 Some Assorted Facts. Two special conformal maps.

A.

$$
w = \textstyle \frac { 1 } { 2 } ( z + z ^ { - 1 } ) .
$$

Set $w = u + i v$ and $z = \rho e ^ { i \theta }$ . The exterior of the unit circle, $| z | > 1$ ,is mapped conformally onto the $\pmb { w }$ -plane with the interval $- 1 \leq u \leq 1$ deleted. The image of the point $( \rho \cos \theta , \rho \sin \theta )$ is the point

$$
( \ddagger ( \rho + \rho ^ { - 1 } ) \cos \theta , \ddagger ( \rho - \rho ^ { - 1 } ) \sin \theta ) .
$$

The circle $| z | = \rho > 1$ maps onto the ellipse

$$
\begin{array} { r } { u = \frac { 1 } { 2 } ( \rho + \rho ^ { - 1 } ) \cos \theta , v = \frac { 1 } { 2 } ( \rho - \rho ^ { - 1 } ) \sin \theta , 0 \leq \theta \leq 2 \pi . } \end{array}
$$

![](../chunks/Interpolation and Approximation (Philip J. Davis) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0070/auto/images/5b8220bf9fd249008fb2fad681ffd0c5ca92f29d92d82e932c0a515423a44738.jpg)  
Figure 1.13.1.

DEFINITIoN 1.13.1.The ellipse (1.13.2) will be designated by $\mathcal { E } _ { \rho }$ ， $( \pmb { \rho } > 1 )$ The semi-axes of $\mathcal { E } _ { \rho }$ are, respectively

$$
\begin{array} { c } { { { \pmb a } = \frac { 1 } { 2 } ( { \pmb \rho } + { \pmb \rho } ^ { - 1 } ) } } \\ { { { \pmb b } = \frac { 1 } { 2 } ( { \pmb \rho } - { \pmb \rho } ^ { - 1 } ) } } \end{array}
$$

and hence

The foci of $\mathcal { E } _ { \rho }$ are at $u = \pm 1$ so that $\mathcal { E } _ { \rho } ^ { \mathcal { ( } { ) } } , \rho > 1$ ,forms a confocal family of ellipses. The image of the unit circle under (l.l3.l） is the interval $- 1 \leq u \leq 1$ traced from l to $^ { - 1 }$ ,thence back to l.

When $z$ is solved for $\pmb { w }$ ，we obtain

$$
z = w + \sqrt { w ^ { 2 } - 1 } .
$$

For values of $z$ outside the unit circle,that branch of the root must be taken which leads to $z ( \infty ) = \infty$

![](../chunks/Interpolation and Approximation (Philip J. Davis) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0070/auto/images/821f5db0deaccd0d5c99059a8c981d56037a6c6d7a24e3ee264397dc23e11256.jpg)  
Figure 1.13.2 The Family $\mathbf { \boldsymbol { \mathcal { E } } } _ { \rho } ^ { \varphi }$ of Confocal Ellipses.

B.

$$
z = \cos w = \cos ( u + i v ) = \cos u \cosh v - i \sin u \sinh v .
$$

Let $\pmb { R }$ be the rectangle in the $\pmb { w }$ plane with vertices at $w = \sigma { i }$ ， $\sigma i + \pi ,$ $- \sigma i + \pi , - \sigma i . \ R$ is mapped onto the ellipse d ${ \mathfrak { s } } _ { \mathfrak { p } } , \ \pmb { \rho } = { \mathfrak { e } } ^ { \pmb { \sigma } }$ ，with the two intervals $[ 1 , { \pmb a } ] , [ - { \pmb a } , - 1 ]$ ， $a = \cosh \sigma$ ，deleted.As a point w traces out the vertical sides of $\pmb { R }$ ，the image point $\boldsymbol { z }$ traces each of these two intervals twice.

![](../chunks/Interpolation and Approximation (Philip J. Davis) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0070/auto/images/7762de965342e8b7605ea108b5b95b4c77982ee5608e43634d5dc7a903280ac6.jpg)  
Figure 1.13.3.

Zorn's Lemma. Today,a mathematics book without this lemma would be like an l8th century gentleman without his sword.

DEFINITION 1.13.2. A partial ordering of a set $X$ is a binary relation between elements designated by $^ { \ast } \leq ^ { \ast }$ and such that

$$
\begin{array} { l l l } { x \leq y , } & { y \leq z } & { \mathrm { i m p l i e s } } & { x \leq z } \\ { } & { } & { x \leq x } \\ { x \leq y , } & { y \leq x } & { \mathrm { i m p l i e s } } & { x = y . } \end{array}
$$

If in addition for auy $x , y \in X$ it is true that either

$$
x \leq y \quad { \mathrm { o r } } \quad y \leq x ,
$$

the set is called totally ordered (or,simply ordered).

If $\pmb { A }$ is a subset of a partially ordered set,and if an element $z$ satisfies

$$
x \leq z \quad { \mathrm { f o r ~ a l l } } \quad x \in A ,
$$

then $_ z$ is called an upper bound for $\pmb { A }$

If $z$ is an element of a partially ordered set $X$ such that no element $x \in X$ ， $x \neq z$ satisfies

$$
z \leq x
$$

then $\boldsymbol { z }$ is called a maximal element of $X$

THEOREM 1.13.1 (ZORN's LEMMA). Let $X$ be $^ { a }$ partially ordered set and suppose that every totally ordered subset of $X$ has an upper bound in X.Then $X$ has a maximal element.

Zorn's Lemma is known to be equivalent to the Axiom of Choice.

# NOTES ON CHAPTER I

1.1Determinant theory developed from the point of view of $\mathscr { n }$ -dimensional volume can be found in Schreier and Sperner [1], Chapter II.

1.4 For a discussion of when a function $w ( \delta )$ can be a modulus of continuity see Tieman [l],p.109.

1.7For more on infinitely differentiable functions,see Boas [4], pp.   
150-156.

1.10 An up-to-date account of the theory of entire functions is given in Boas [3].

1.12 For the algebraic conjugate space, see, e.g.，Taylor [3], pp.34-35.

1.13 Zorn's Lemma is discussed in Halmos [2],p. 62.

# PROBLEMS

1. For what values of $^ { a }$ and $^ { b }$ are the curves $y = a x ^ { b }$ bounded on [0,1]?

2.For what values of a andbare the curves y =x² +ax +b bounded on[-1,1]？

3.Show that $\frac { 1 } { x }$ sin x and $x \sin { \frac { 1 } { x } }$ (properly defined at $x = 0$ ）are continuous over any finite interval.

4.Show that $\begin{array} { r } { y = e ^ { - x } } \end{array}$ is uniformly continuous over the infinite interval

$$
0 \leq x < \infty .
$$

5.Let $f \in C [ a , b ]$ .Use the first mean value theorem to show that

$$
\operatorname* { l i m } _ { n \to \infty } \int _ { a } ^ { b } f \left( x \right) \left| \sin n x \right| d x = \operatorname* { l i m } _ { n \to \infty } \int _ { a } ^ { b } f \left( x \right) \left| \cos n x \right| d x = { \frac { 2 } { \pi } } \int _ { a } ^ { b } f \left( x \right) d x . \ \mathrm { ( F e ] } \dot { \epsilon } \mathrm { r } ) .
$$

6. Compute $w ( f ; \delta )$ for $f ( x ) = \sin { x }$ on $- \infty < x < \infty$ ·

7. Compute $w ( f ; \delta )$ for $f ( x ) = x ^ { 2 } - 3 x + 1$ on $- 1 \leq x \leq 1$

8.Let $f ( x ) \in C ^ { 1 } [ a , b ]$ and let $f ^ { \prime } ( x )$ be increasing and positive.Find $w ( \delta )$

9.Let $f ( z )$ be analytic in $| z | \leq 1$ .Show that $w ( f ; \delta ) \leq M \delta$ for some $\pmb { M }$ Generalize.

10.Let $f ( x )$ be periodic and integrable. Define the moving average of $f$ by means of

$$
f _ { h } ( x ) = { \frac { 1 } { 2 h } } \int _ { x - h } ^ { x + h } f \left( t \right) d t .
$$

Prove: 1. $f _ { h } ( x )$ is periodic. 2.If $f \left( x \right) \in C ^ { n }$ then $f _ { h } ( x ) \in C ^ { n + 1 }$ 3. $w ( f _ { h } ; \delta ) \le w ( f ; \delta )$ and hence $f _ { h }$ is“smoother”than $f$ 4. If $f$ is sufficiently smooth, $( f _ { h } ( x ) ) ^ { \prime } = ( f ^ { \prime } ) _ { h }$

11. Let $f ( x )$ ， $g ( x ) \in \operatorname { L i p } \alpha$ on $[ a , b ]$ . Then the same is true of $f ( x ) \ g ( x )$

12. Does $x ^ { \alpha } \log x , \alpha > 0$ ，satisfy a Lipschitz condition on [0,1]?

13. If

$$
f ( x ) \in C ^ { 2 } [ a , b ] ,
$$

then

$$
( a ~ - b ) { f ^ { \prime } ( x ) } ~ = f ( a ) ~ - ~ f ( b ) ~ + ~ { \textstyle { \frac { 1 } { 2 } } } ( b ~ - x ) ^ { 2 } f ^ { \prime \prime } ( \xi _ { 1 } ) ~ - ~ { \textstyle { \frac { 1 } { 2 } } } ( a ~ - x ) ^ { 2 } f ^ { \prime \prime } ( \xi _ { 2 } )
$$

for $x \in ( a , b ) , a \mathit { \Theta } < \xi _ { 2 } < x , x \mathit { \Theta } < \xi _ { 1 } < b$

14.Use the last result to show that

$$
M _ { 1 } \leq \frac { 2 M _ { 0 } } { h } + \frac { 1 } { 2 } M _ { 2 } h
$$

where $M _ { i } = \operatorname* { m a x } _ { a \leq x \leq b } | f ^ { ( i ) } ( x ) |$ and $h = b - a$ . (Hadamard)

15. $\operatorname { I f } \operatorname* { l i m } _ { h \to 0 } { \frac { f ( x + h ) - 2 f ( x ) + f ( x - h ) } { h ^ { 2 } } }$ exists, $f ( x )$ is said to have a second Riemann derivative at $_ { x }$ .Use Theorem 1.6.6 to show that if $f ^ { \prime \prime } ( x )$ exists then the above limit exists and equals it. Show,however,that there are many functions that do not have a second derivative at $_ { x }$ but have a second Riemann derivative.

16. Let $f \in C ^ { 1 } [ a , b ]$ and let $f ^ { \prime \prime } ( x )$ exist at each point of $( a , b )$ . Suppose $f ( a ) =$ $f ^ { \prime } ( a ) = 0$ and $f ( b ) = 0$ ．Then there isa point ${ \pmb \xi }$ ， $a < \xi < b$ with $f ^ { \prime \prime } ( \pmb { \xi } ) = \mathbf { 0 }$ Generalize to functions having higher order zeros at $\pmb { k }$ points.

17. If $\operatorname* { l i m } _ { x \to \infty } f ( x ) = a$ and $\operatorname* { l i m } _ { x \to \infty } f ^ { \prime \prime \prime } ( x ) = 0$ prove that $\operatorname* { l i m } _ { x \to \infty } f ^ { \prime } ( x ) = 0$ and $\operatorname* { l i m } _ { x \to \infty } f ^ { \prime \prime } ( x ) = 0$

18.Let $f ( x ) , g ( x ) \in C ^ { \infty } [ a , b ]$ and $a \leq x _ { 0 } \leq b$ If $f ^ { ( n ) } ( x _ { 0 } ) = 0$ ,n = 0,1,2,..., then ${ \frac { d ^ { n } } { d x ^ { n } } } ( f ( x ) g ( x ) ) | _ { x _ { 0 } } = 0 , n = 0 , 1 , . . . . .$

19.1 $\sum \limits _ { n = 0 } ^ { \infty } a _ { n } z ^ { n } , \sum \limits _ { n = 0 } ^ { \infty } b _ { n } z ^ { n }$ are algin $| z | < 1$ soi $\sum _ { n = 0 } ^ { \infty } a _ { n } b _ { n } z ^ { n }$

20.Use Theorem 1.9.3 to show that is in $A [ a , b ]$ for any $0 < a < b < \infty$

21. Show directly that $e ^ { e ^ { \pmb { x } } }$ satisfies the conditions of Theorem 1.9.3 on [0,1].

22. Make use of Theorem 1.10.l to show that $f ( z ) = \int _ { 0 } ^ { z } e ^ { t ^ { 2 } } d t$ is entire.

23.If $f ( z )$ is entire and satisfies $| f ( z ) | \geq m | z | ^ { n }$ for all $| z | > r$ ，then $\pmb { f }$ is a polynomial and its degree is at least $_ { n }$

24. Let $f \in \mathcal { P } _ { 2 }$ and suppose that $\pmb { f } ( a ) = \pmb { f } ^ { \prime } ( a ) = 0 , \pmb { f } ( b ) = 0 \textnormal { \pmb { b } } \neq a$ . Then $\pmb { f } \equiv \mathbf { 0 }$ In general, if $f \in \mathcal { P } _ { n }$ and has roots of total multiplicity $> n$ ,then $\pmb { f } \equiv 0$

25. Prove that $\mathbf { 2 } ^ { x }$ can coincide with a polynomial at only a finite number of points.Is this true when $_ { x }$ is replaced by $z ?$

26.Let $f \in A ( - \infty , \infty )$ and f(𝑘)(x)>0k=0,1,....Then $f ( x )$ cannot coincide with a polynomial infinitely often. Generalize.

27. If $f ( x )$ is a polynomial, then lim $f ^ { ( n ) } ( x ) = 0$ for all $_ { \pmb { x } }$ .Is the converse true? n→8

28.The spaces $C ^ { n } [ a , b ] , C ^ { \infty } [ a , b ] , A [ a , b ] , A ( R ) , .$ $\pmb { \cal E }$ are all infinite dimensional.

29. ${ \mathcal { P } } _ { n }$ defined on $[ a , b ]$ has dimension $n + 1$ .What about $\mathcal { P } _ { n }$ defined on a set $\pmb { S }$ consisting of $\pmb { k }$ points?

30.Let $A _ { r }$ designate the set of functions that are analytic in $| z | < r$ but in no disc $| z | < r ^ { \prime }$ with $r ^ { \prime } > r$ Is $A _ { r }$ a linear space?

31. Let $_ { x }$ be the space of all functions that are analytic in $| z | < R$ and have $| z | = R$ as a natural boundary. Is $\pmb { N }$ a linear space?
