for sufficiently small $\tau$ and

$$
f _ { 1 } ( w , \tau ) = f _ { 1 } ( w _ { 1 , 0 } , w _ { 2 } , \cdot \cdot \cdot , w _ { n } , \tau ) + \int _ { w _ { 1 , 0 } } ^ { w _ { 1 } } \left| \frac { \partial \left( f _ { 2 } , \cdot \cdot \cdot , f _ { n } \right) } { \partial \left( w _ { 2 } , \cdot \cdot \cdot , w _ { n } \right) } \right| ( \xi , w _ { 2 } , \cdot \cdot \cdot , w _ { n } ) \mathrm { d } \xi ,
$$

we have from (8.31)

$$
\phi _ { 1 } ^ { ( m ) } ( w , \tau ) = f _ { 1 } ( w , \tau ) + { \cal O } ( \tau ^ { m + 1 } ) .
$$

So, $\phi ^ { ( m ) } ( w , \tau ) ~ = ~ ( \phi _ { 1 } ^ { ( m ) } ( w , \tau ) , \cdot \cdot \cdot , \phi _ { n } ^ { ( m ) } ( w , \tau ) )$ is an $m$ -th order approximant to $f ( w , \tau ) = ( f _ { 1 } ( w , \tau ) , \cdot \cdot \cdot , f _ { n } ( w , \tau ) )$ , the generating function of the type $\alpha _ { 1 , 1 }$ of $g _ { \alpha } ^ { t }$ and hence the volume-preserving scheme (8.33) is of $m$ -th order of accuracy. The proof is completed.

Remark 8.10. We note that the volume-preserving scheme $z = z ^ { k } \to z ^ { k + 1 }$ given by (8.33) is implicit for only one new variable $z _ { 1 } ^ { k + 1 }$ and explicit for all other new variables $z _ { i } ^ { k + 1 } ( i = 2 , \cdots , n )$ in terms of the old variables $z _ { i } ^ { k } ( i = 2 , \cdots , n )$ .

Remark 8.11. We can get volume-preserving scheme similar to the above one if we consider the types $\alpha = \alpha _ { ( s , s ) }$ $2 \leq s \leq n$ ), instead of $\alpha = \alpha _ { ( 1 , 1 ) }$ .

Example 8.12. First order scheme:

$$
\left\{ \begin{array} { l l } { z _ { 1 } ^ { k } = \phi _ { 1 } ^ { ( 1 ) } ( z _ { 1 } ^ { k + 1 } , z _ { 2 } ^ { k } , \cdot \cdot \cdot , z _ { n } ^ { k } , \tau ) , } \\ { z _ { i } ^ { k } = \phi _ { i } ^ { ( 1 ) } ( z _ { 1 } ^ { k + 1 } , z _ { 2 } ^ { k } , \cdot \cdot \cdot , z _ { n } ^ { k } , \tau ) , } \end{array} \right. \quad i = 2 , \cdot \cdot \cdot , n ,
$$

where

$$
\begin{array} { r c l } { { \phi _ { 1 } ^ { ( 1 ) } ( w , \tau ) } } & { { = } } & { { - \tau a _ { 1 } ( 0 , w _ { 2 } , \cdots , w _ { n } ) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { } } \\ { { + } } & { { \displaystyle \int _ { 0 } ^ { w _ { 1 } } \left[ \begin{array} { c c c c c } { { 1 + \tau \frac { \partial a _ { 2 } } { \partial w _ { 2 } } } } & { { \tau \frac { \partial a _ { 2 } } { \partial w _ { 3 } } } } & { { \cdots } } & { { \tau \frac { \partial a _ { 3 } } { \partial w _ { n } } } } \\ { { } } & { { } } & { { } } & { { } } \\ { { \tau \frac { \partial a _ { 3 } } { \partial w _ { 2 } } } } & { { 1 + \tau \frac { \partial a _ { 3 } } { \partial w _ { 3 } } } } & { { \cdots } } & { { \tau \frac { \partial a _ { 3 } } { \partial w _ { n } } } } \\ { { } } & { { } } & { { } } & { { } } \\ { { \vdots } } & { { \vdots } } & { { } } & { { } } & { { \vdots } } \\ { { \tau \frac { \partial a _ { n } } { \partial w _ { 2 } } } } & { { \tau \frac { \partial a _ { n } } { \partial w _ { 3 } } } } & { { \cdots } } & { { 1 + \tau \frac { \partial a _ { n } } { \partial w _ { n } } } } \end{array} \right] ( \xi , w _ { 2 } , \cdots , w _ { n } ) \mathrm { d } \xi } } \\ { { } } & { { } } & { { } } \\ { { \phi _ { i } ^ { ( 1 ) } ( w , \tau ) } } & { { = } } & { { w _ { i } + \tau a _ { i } ( w ) . } } \end{array}
$$

Second order scheme:

$$
\left\{ \begin{array} { l l } { z _ { 1 } ^ { k } = \phi _ { 1 } ^ { ( 2 ) } ( z _ { 1 } ^ { k + 1 } , z _ { 2 } ^ { k } , \cdots , z _ { n } ^ { k } , \tau ) , } \\ { z _ { i } ^ { k + 1 } = \phi _ { i } ^ { ( 2 ) } ( z _ { 1 } ^ { k + 1 } , z _ { 2 } ^ { k } , \cdots , z _ { n } ^ { k } , \tau ) , } & { i = 2 , \cdots , n , } \end{array} \right.
$$

where

$$
\begin{array} { l } { { \phi _ { 1 } ^ { ( 2 ) } ( w , \tau ) = \psi _ { 1 } ^ { ( 2 ) } ( 0 , w _ { 2 } , \cdot \cdot \cdot , w _ { n } , \tau ) + \displaystyle \int _ { 0 } ^ { w _ { 1 } } \left| \frac { \partial ( \psi _ { 2 } ^ { ( 2 ) } , \cdot \cdot \cdot , \psi _ { n } ^ { ( 2 ) } ) } { \partial ( w _ { 2 } , \cdot \cdot \cdot , w _ { n } ) } \right| ( \xi , w _ { 2 } , \cdot \cdot \cdot , w _ { n } ) \mathrm { d } \xi . } } \\ { { \phi _ { i } ^ { ( 2 ) } ( w , \tau ) = \psi _ { i } ^ { ( 2 ) } ( w , \tau ) , \quad i = 2 , \cdot \cdot \cdot , n , } } \end{array}
$$

and

$$
\begin{array} { l } { { \psi ^ { ( 2 ) } ( w , \tau ) = \bigl ( \psi _ { 1 } ^ { ( 2 ) } ( w , \tau ) , \cdots , \psi _ { n } ^ { ( 2 ) } ( w , \tau ) \bigr ) ^ { \mathrm { T } } = w + \tau \widetilde { a } ( w ) + \frac 1 2 \tau ^ { 2 } \frac { \partial \widetilde { a } ( w ) } { \partial w _ { 1 } } \widetilde { a } ( w ) } } \\ { { \mathrm { } } } \\ { { \widetilde { a } ( w ) = \bigl ( - a _ { 1 } ( w ) , a _ { 2 } ( w ) , \cdots , a _ { n } ( w ) \bigr ) ^ { \mathrm { T } } . } } \end{array}
$$

# 10.9 Some Volume-Preserving Algorithms

In this section, we analyze and study under conditions a source-free system that has volume-preserving R–K schemes.

# 10.9.1 Volume-Preserving R–K Methods

Consider the system

$$
\frac { \mathrm { d } \boldsymbol { z } } { \mathrm { d } t } = \boldsymbol { a } ( \boldsymbol { z } ) ,
$$

where

$$
\begin{array} { r l } & { z = \left[ \begin{array} { l } { x } \\ { y } \end{array} \right] , \quad x \in \mathbf { R } ^ { p } , \quad y \in \mathbf { R } ^ { q } , } \\ & { \quad a ( z ) = \left[ \begin{array} { l } { g ( y ) } \\ { f ( x ) } \end{array} \right] . } \end{array}
$$

Obviously, this is a source-free system. Its phase flow in $\mathbf { R } ^ { p + q }$ preserves the phase volume of $( p + q )$ form

$$
\operatorname { d } x _ { 1 } \wedge \operatorname { d } x _ { 2 } \wedge \cdots \wedge \operatorname { d } x _ { p } \wedge \operatorname { d } y _ { 1 } \wedge \operatorname { d } y _ { 2 } \wedge \cdots \wedge \operatorname { d } y _ { q } .
$$

Only R–K and P–R–K are to be discussed. We wish, some of the phase volume is preserved.

The formula of a general $m$ -th stage P–R–K method with time step $h$ applied to system (9.1) is read as

$$
\begin{array} { l } { \displaystyle \xi _ { i } = x _ { n } + h \sum _ { j = 1 } ^ { m } d _ { i j } g ( \eta _ { j } ) , \eta _ { i } = y _ { n } + h \sum _ { j = 1 } ^ { m } c _ { i j } f ( \xi _ { j } ) , \quad 1 \le i \le m , } \\ { \displaystyle x _ { n + 1 } = x _ { n } + h \sum _ { j = 1 } ^ { m } \delta _ { j } g ( \eta _ { j } ) , } \\ { \displaystyle y _ { n + 1 } = y _ { n } + h \sum _ { j = 1 } ^ { m } \gamma _ { j } f ( \xi _ { j } ) , } \end{array}
$$

here $\xi _ { i } \in \mathbf { R } ^ { p } , \eta _ { i } \in \mathbf { R } ^ { q }$ ( $1 \leq i \leq m$ ) are auxiliary vectors used to compute updates $( x _ { n + 1 } , y _ { n + 1 } )$ .

Suppose (9.2) is irreducible, that is, if $i \neq j$ , then $\xi _ { i } \neq \xi _ { j }$ or $\eta _ { i } \neq \eta _ { j } ^ { \mathrm { [ D V 8 4 ] } }$ . We have following Lemma of Y.B. Suris[Sur96] .

Lemma 9.1. Let $\delta = [ \delta _ { 1 } , \delta _ { 2 } , \cdots , \delta _ { m } ] ^ { \mathrm { T } }$ , $D = \left( d _ { i j } \right)$ , $C = \left( c _ { i j } \right)$ , $e = [ 1 , 1 , \cdots , 1 ] ^ { \mathrm { T } }$ be a $m$ -dimensional vector $D ^ { - } = e \delta ^ { \mathrm { T } } - D$ , $C ^ { - } = e \delta ^ { \mathrm { T } } - C$ . The P–R–K method preserves phase volume for system (9.1) in arbitrary dimensions, iff

$$
\begin{array} { r l } & { d _ { k _ { 1 } l _ { 1 } } c _ { l , k _ { 2 } } \cdot \cdot \cdot d _ { k _ { r - 1 } l _ { r - 1 } } c _ { l _ { r - 1 } k _ { r } } d _ { k _ { r } l _ { r } } c _ { l _ { r } k _ { 1 } } } \\ & { = d _ { k _ { 1 } l _ { 1 } } ^ { - } c _ { l _ { 1 } k _ { 2 } } ^ { - } \cdot \cdot \cdot d _ { k _ { r - 1 } l _ { r - 1 } } ^ { - } c _ { l _ { r - 1 } k _ { r } } ^ { - } d _ { k _ { r } l _ { r } } ^ { - } c _ { l _ { r } k _ { 1 } } ^ { - } . } \end{array}
$$

For arbitrary $1 \leq r \leq m$ and two arbitrary ordered sets $\left( k _ { 1 } , \cdots , k _ { r } \right)$ and $( l _ { 1 } , \cdots , l _ { r } )$ of different natural numbers from $( 1 , m )$ , $d _ { i j }$ and $c _ { i j }$ are elements $( i , j )$ with respect to matrix $D ^ { - }$ and $C ^ { - }$ .

Next, for system (9.1), we construct some volume-preserving method by P–R–K method, using the above criteria.

First we consider volume-preserving by $\mathbf { R - K }$ method for linear system.

Linear system of ODE is read as

$$
{ \dot { y } } = M y ,
$$

where $M$ is $n \times n$ matrix with trace $M = 0$ . If $\operatorname* { d e t } M = 0$ , the system (9.3) can degrade to a lower stage, so we assume $\operatorname* { d e t } M \neq 0$ . Now, we assume that $M$ is a constant matrix. As in R–K method, $( A . b . c )$ applied to system (9.3) takes the form

$$
\begin{array} { l } { { \displaystyle Y _ { i } = y _ { n } + h \sum _ { j = 1 } ^ { s } a _ { i j } M Y _ { j } } , } \\ { { \displaystyle y _ { n + 1 } = y _ { n } + h \sum _ { j = 1 } ^ { s } b _ { j } M Y _ { j } } , } \end{array}
$$

where $A = ( a _ { i j } ) _ { s \times s } , b = [ b _ { 1 } , b _ { 2 } , \cdot \cdot \cdot , b _ { s } ] ^ { \mathrm { T } }$ .

Here, we just talk about R–K method and according to Lemma 4.2, we cannot find a general volume-preserving $\mathbf { R - K }$ method. So, our hope is to distinguish $M$ into

different classes and find out whether there are volume-preserving R–K method in any class.

Now, we need the following notations:

$$
\begin{array} { l l } { { \overline { { { A } } } = A \otimes E _ { n } , } } & { { \overline { { { M } } } = \mathrm { d i a g } \left( M , M , \cdots , M \right) = E _ { s } \otimes M , } } \\ { { \overline { { { b } } } = b ^ { \mathrm { T } } \otimes E _ { n } , } } & { { Y = [ Y _ { 1 } , Y _ { 2 } , \cdots , Y _ { s } ] ^ { \mathrm { T } } } } \\ { { \overline { { { y } } } _ { n } = [ y _ { n } , y _ { n } , \cdots , y _ { n } ] ^ { \mathrm { T } } , } } & { { \overline { { { e } } } = e \otimes e _ { s } , } } \end{array}
$$

where $E _ { n }$ is an $n$ -stage identical matrix and $e = [ 1 , 1 , \cdots , 1 ] ^ { \mathrm { T } }$ is a $n$ -dimensional   
vector. For $\mathbf { R - K }$ method to be volume-preserving, we have equivalent condition:   
de t ∂ yn+1 ≡ 1. So, we need to calculate the matrix ∂ yn+1 1. In matrix notations, ∂ yn   
$\mathbf { R - K }$ method (9.4) reads

$$
\begin{array} { l } { { y _ { n + 1 } = y _ { n } + h M \overline { { { b } } } Y , } } \\ { { Y = ( 1 - h \overline { { { M } } } \overline { { { A } } } ) ^ { - 1 } \overline { { { y } } } _ { n } . } } \end{array}
$$

So,

$$
\begin{array} { r c l } { { y _ { n + 1 } } } & { { = } } & { { ( E _ { n } + ( h M \overline { { { b } } } ( I - h \overline { { { M } } } \overline { { { A } } } ) ^ { - 1 } \overline { { { e } } } ) y _ { n } } } \\ { { } } & { { \Longrightarrow } } & { { \displaystyle { \frac { \partial y _ { n + 1 } } { \partial y _ { n } } = E _ { n } + h M \overline { { { b } } } ( I - h \overline { { { M } } } \overline { { { A } } } ) ^ { - 1 } \overline { { { e } } } . } } } \end{array}
$$

Lemma 9.2. Let $A , D$ be non-degenerate $m \times m$ and $n \times n$ matrices respectively and $B$ an $m \times n$ and $C$ an $n \times m$ matrix, then

$$
\operatorname* { d e t } A \operatorname* { d e t } \left( D + C A ^ { - 1 } B \right) = \operatorname* { d e t } D \operatorname* { d e t } \left( A + B D ^ { - 1 } C \right) .
$$

The proof can be found in any textbook of linear algebra.

By Lemma 9.2, it is easy to get from (9.7)

$$
\operatorname* { d e t } \left( \frac { \partial y _ { n + 1 } } { \partial y _ { n } } \right) = \frac { \operatorname* { d e t } \left( I - h \overline { { M } } \overline { { A } } - \overline { { e } } M \overline { { b } } \right) } { \operatorname* { d e t } \left( I - h \overline { { M } } \overline { { A } } \right) } .
$$

Additionally, we define the notations

$$
\begin{array} { l l } { { A ^ { - } = ( a _ { i j } ^ { - } ) , ~ } } & { { a _ { i j } ^ { - } = a _ { i j } - b _ { j } , } } \\ { { { } } } & { { { } } } \\ { { N = A \otimes M , ~ N ^ { - } = A ^ { - } \otimes M . } } \end{array}
$$

In these notations, (9.7) reads as

$$
\operatorname* { d e t } \left( \frac { \partial y _ { n + 1 } } { \partial y _ { n } } \right) = \frac { \operatorname* { d e t } \left( I - h N ^ { - } \right) } { \operatorname* { d e t } \left( I - h N \right) } .
$$

Now, if (9.10) is identical to 1, we arrive at the criterion for $\mathbf { R - K }$ method (9.4) to be volume-preserving scheme as

$$
\operatorname* { d e t } \left( \lambda I - N ^ { - } \right) = \operatorname* { d e t } { \big ( } \lambda I - N { \big ) } , \quad \forall \lambda \in \mathbf { R } .
$$

Theorem 9.3. If dimension of $M$ is odd, then all the R–K methods based on high order quadrature formula such as Gauss–Legendre, Radau, and Lobatto are not volumepreserving.

Proof. Note that $N \ = \ A \otimes$ M and $N ^ { - } ~ = ~ A ^ { - } ~ \otimes ~ M$ . If the method is volumepreserving, then

$$
{ \begin{array} { r l } { \operatorname* { d e t } N = \operatorname* { d e t } ( N ^ { - } ) \iff \operatorname* { d e t } ( A \otimes M ) = \operatorname* { d e t } ( A ^ { - } \otimes M ) } \\ & { \iff ( \operatorname* { d e t } A ) ^ { n } ( \operatorname* { d e t } ( M ) ) ^ { s } = ( \operatorname* { d e t } ( A ^ { - } ) ) ^ { n } ( \operatorname* { d e t } M ) ^ { s } } \\ & { \iff ( \operatorname* { d e t } A ) ^ { n } = ( \operatorname* { d e t } ( A ^ { - } ) ) ^ { n } } \\ & { \iff \operatorname* { d e t } A = \operatorname* { d e t } ( A ^ { - } ) . } \end{array} }
$$

Now, we need the $W$ -transformation proposed by Hairer and Wanner $\mathrm { [ H W 8 1 ] }$ . They introduced a generalized square matrix $W$ defined by

$$
W = ( p _ { 0 } ( c ) , p _ { 1 } ( c ) , \cdot \cdot \cdot , p _ { n - 1 } ( c ) ) ,
$$

where the normalized shifted Legendre polynomials are defined by

$$
p _ { k } ( x ) = \sqrt { 2 k + 1 } \sum _ { i = 0 } ^ { k } ( - 1 ) ^ { k + i } \Big ( \begin{array} { c } { { k } } \\ { { i } } \end{array} \Big ) \Big ( \begin{array} { c } { { k + i } } \\ { { i } } \end{array} \Big ) x ^ { i } , \quad k = 0 , 1 , \cdots , s - 1 .
$$

For Gauss–Legendre, let $X = W ^ { - 1 } A W$ , then

$$
\begin{array} { r } { X = \left[ \begin{array} { c c c c c c } { \frac 1 2 } & { - \xi _ { 1 } } & & & & \\ { \xi _ { 1 } } & { 0 } & { - \xi _ { 2 } } & & & \\ & { \xi _ { 2 } } & & & & \\ & & { \ddots } & { \ddots } & { - \xi _ { s - 1 } } \\ & & & & { \xi _ { s - 1 } } & { 0 } \end{array} \right] , } \end{array}
$$

where $\xi _ { k } = \frac { 1 } { 2 \sqrt { 4 k ^ { 2 } - 1 } } \left( k = 0 , 1 , \cdots , s - 1 \right)$ .

However, $X ^ { - } = W ^ { - 1 } A ^ { - } W$ , then

$$
X ^ { - } = \left[ \begin{array} { c c c c c c } { { - \frac { 1 } { 2 } } } & { { - \xi _ { 1 } } } & { { } } & { { } } & { { } } & { { } } \\ { { \xi _ { 1 } } } & { { 0 } } & { { - \xi _ { 2 } } } & { { } } & { { } } & { { } } \\ { { } } & { { \xi _ { 2 } } } & { { } } & { { } } & { { } } & { { } } \\ { { } } & { { } } & { { \ddots } } & { { \ddots } } & { { - \xi _ { s - 1 } } } \\ { { } } & { { } } & { { } } & { { } } & { { \xi _ { s - 1 } } } & { { 0 } } \end{array} \right] .
$$

It is easy to verify that d $\operatorname { e t } X \neq \operatorname* { d e t } ( X ^ { - } ) \Rightarrow \operatorname* { d e t } A \neq \operatorname* { d e t } ( A ^ { - } ) .$ So, Gauss–Legendre method is not volume-preserving.

Using the Table 2.1 of Chapter 7, the remaining part of the proof is similar, where $\sigma \in \mathbf { R }$ and $u \sigma \neq 0$ .

Theorem 9.4. [QL00] If the dimension of $M$ is even, then the R–K methods based on high order quadrature formulas such as Gauss–Legendre, Lobatto III A, Lobatto III $B$ , Lobatto III $s$ , Radau $I B$ , and Radau IIB are volume-preserving, iff

$$
\lambda ( M ) = ( \lambda _ { 1 } , \lambda _ { 2 } , \cdot \cdot \cdot , \lambda _ { \frac { n } { 2 } } , - \lambda _ { 1 } , - \lambda _ { 2 } , \cdot \cdot \cdot , - \lambda _ { \frac { n } { 2 } } ) .
$$

Proof. Assume $A , B$ are $n \times n$ and $m \times m$ matrices respectively, and their eigenvalue are respectively $\{ \lambda _ { 1 } , \lambda _ { 2 } , \dotsb , \lambda _ { n } \}$ and $\{ \mu _ { 1 } , \mu _ { 2 } , \cdots , \mu _ { m } \}$ . Then according to the property of Kronecker product, we have $\lambda ( A \otimes B ) = \{ \lambda _ { i } \mu _ { j } , i = 1 , \cdot \cdot \cdot , n ; j = 1 , \cdot \cdot \cdot , m \}$ . For $\mathbf { R - K }$ methods to be volume-preserving schemes, according to (9.11), $N$ and $N ^ { - }$ must have same eigenvalue, that is to say, $A \otimes M$ and $A ^ { - } \otimes M$ must have the same eigenvalues. For example, for Gauss–Legendre method, $\lambda ( A ) ~ = ~ \lambda ( X )$ and $\lambda ( A ^ { - } ) = \lambda ( X ^ { - } )$ , however, it is obvious that $\lambda ( X ) = - \lambda ( X ^ { - } )$ , so according to the properties of Kronecker product, we can easily verify that $A \otimes M$ and $A ^ { - } \otimes M$ have the same eigenvalues. -

tem, that is to say, invertible matrix, th $M \ : = \ : J ^ { - 1 } S$ , where $J = \left[ \begin{array} { c c } { 0 } & { I _ { n } } \\ { - I _ { n } } & { 0 } \end{array} \right]$ $S ^ { \prime } = S$ $n \times n$

$$
\lambda ( M ) = \left( \lambda _ { 1 } , \lambda _ { 2 } , \cdot \cdot \cdot , \lambda _ { \frac { n } { 2 } } , - \lambda _ { 1 } , - \lambda _ { 2 } , \cdot \cdot \cdot , \lambda _ { \frac { n } { 2 } } \right) .
$$

So, the $\mathbf { R - K }$ method based on high order quadrature formula (Gauss–Legendre, Lobatto IIIA, Lobatto IIIB, Lobatto IIIS, Radau IB, and Radau IIB) are volumepreserving. The Theorem 9.4 says that for the methods to preserve volume, the system, in some sense, must be similar to a Hamiltonian system. If the matrix $M$ similar to an infinitesimally symplectic matrix, i.e., there is an invertible matrix $P$ , subjected to $P ^ { - 1 } M P = J S$ , $S ^ { \mathrm { T } } = S$ , then we can transform the system to a Hamiltonian system by a coordinate transformation. In this situation, the volume-preserving $\mathbf { R - K }$ methods and the symplectic $\mathbf { R - K }$ methods almost have no difference, that is, if $P$ is a symplectic matrix, then volume-preserving R–K methods are equivalent to symplectic $\mathbf { R - K }$ methods; and in this case, they can be transformed to one another by a linear transformation.

# 10.9.2 Volume-Preserving 2-Stage P–R–K Methods

In the case $r = 1$ , if the necessary and sufficient condition of Lemma 9.5 are satisfied, then a 2-stage P–R–K method is volume-preserving. This condition is the same condition of symplecity on the class of separable Hamiltonian system. Thus for system (9.3), all 2-stage P–R–K methods proposed $\mathrm { i n } ^ { [ \mathrm { S u n 9 5 } ] }$ are volume-preserving algorithms[QL00] .

Example 9.6. 3th order Radau IA-IA method

Example 9.7. 3th order Radau IIA-IIA method   

<table><tr><td>0</td><td>14</td><td>1</td><td>0</td><td>0</td><td>0</td></tr><tr><td></td><td>1</td><td>5</td><td></td><td></td><td></td></tr><tr><td>2</td><td>4</td><td>12</td><td>2</td><td>1</td><td>1</td></tr><tr><td></td><td>1</td><td>3-4</td><td></td><td>1</td><td>3-4</td></tr></table>

Example 9.8. 2nd order Lobatto IIIC-IIIC method   

<table><tr><td>1</td><td>5</td><td>1 12</td><td>1 1</td><td></td><td>0</td></tr><tr><td></td><td></td><td>1</td><td>1</td><td></td><td></td></tr><tr><td>1</td><td>4 4</td><td>4 1</td><td></td><td>1 4</td><td>0 1-4</td></tr></table>

Example 9.9. 4th order Gauss IA-IA method   

<table><tr><td>0</td><td>1</td><td>1-2</td><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td></tr><tr><td></td><td>1</td><td>1</td><td></td><td>1</td><td>1</td></tr></table>

<table><tr><td>1 V3 6</td><td>1+2g 4</td><td>1-2σ 4</td><td>V3 6</td></tr><tr><td>1 V3 + 6</td><td>1-2σ V 十 6</td><td>1+2g</td><td></td></tr><tr><td></td><td>4 1</td><td>4 1</td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td>1-2 V3 6</td><td>1-2σ</td><td>1+2σ</td><td>V3</td></tr><tr><td></td><td>4</td><td>4</td><td>6</td></tr><tr><td>V</td><td>1+2σ V</td><td></td><td></td></tr><tr><td>1 + 6</td><td>+ 6</td><td>1-2σ</td><td></td></tr><tr><td></td><td>4</td><td>4</td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>1</td><td></td></tr><tr><td></td><td>1</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>2</td></tr></table>

# 10.9.3 Some Generalizations

Method $\mathrm { i n } ^ { [ \mathrm { S u r 9 6 } ] }$ can be applied to the extension of following system:

$$
{ \dot { x } } = g ( y ) , \quad { \dot { y } } = h ( z ) , \quad { \dot { z } } = f ( x ) , \quad x , y , z \in \mathbf { R } ^ { P } .
$$

For this system, we consider multi-stage P–R–K method

$$
\xi _ { i } = x _ { n } + h \sum _ { j = 1 } ^ { m } d _ { i j } g ( \eta _ { j } ) , \ \eta _ { i } = y _ { n } + h \sum _ { j = 1 } ^ { m } c _ { i j } h ( w _ { j } ) , \ w _ { j } = z _ { n } + h \sum _ { j = 1 } ^ { m } e _ { i j } f ( \xi _ { j } ) ,
$$

$$
x _ { n + 1 } = x _ { n } + h \sum _ { j = 1 } ^ { m } \alpha _ { j } g ( \eta _ { j } ) , y _ { n + 1 } = y _ { n } + h \sum _ { j = 1 } ^ { m } \beta _ { j } h ( w _ { j } ) , z _ { n + 1 } = z _ { n } + h \sum _ { j = 1 } ^ { m } \gamma _ { j } ( \xi _ { j } ) .
$$

Theorem 9.10. A multi-stage P–R–K method is volume-preserving for a system type (9.17), iff

$$
\begin{array} { r l } & { d _ { k _ { 1 } l _ { 1 } } c _ { l _ { 1 } m _ { 1 } } e _ { m _ { 1 } k _ { 2 } } d _ { k _ { 2 } l _ { 2 } } c _ { l _ { 2 } m _ { 2 } } e _ { m _ { 2 } k _ { 3 } } \cdot \cdot \cdot d _ { k _ { r } l _ { r } } c _ { l _ { r } m _ { r } } e _ { m _ { r } k _ { r } } } \\ & { = d _ { k _ { 1 } l _ { 1 } } ^ { - } c _ { l _ { 1 } m _ { 1 } } ^ { - } e _ { m _ { 1 } k _ { 2 } } ^ { - } d _ { k _ { 2 } l _ { 2 } } ^ { - } c _ { l _ { 2 } m _ { 2 } } ^ { - } e _ { m _ { 2 } k _ { 3 } } ^ { - } \cdot \cdot \cdot d _ { k _ { r } l _ { r } } ^ { - } c _ { l _ { r } m _ { r } } ^ { - } e _ { m _ { r } k _ { r } } ^ { - } } \end{array}
$$

for arbitrary $1 \leq r \leq m$ and three arbitrary ordered sets $\left( k _ { 1 } , \cdots , k _ { r } \right)$ , $\left( l _ { 1 } , \cdots , l _ { r } \right)$ , and $( m _ { 1 } , \cdots , m _ { r } )$ of different natural number form $[ 1 , \cdots , m ]$ , here $d _ { i j } , c _ { i j } , e _ { i j } , d _ { i j } ^ { - }$ , c−ij, e−ij are defined by Lemma 9.5.

Example 9.11. A multi-stage P–R–K method   

<table><tr><td>0</td><td>1</td><td>1 0</td><td>0</td><td>0</td><td>a</td><td>a 0</td></tr><tr><td>1</td><td>1</td><td>1 2</td><td>1</td><td>0</td><td>b+c</td><td>b C</td></tr><tr><td></td><td>1</td><td>1</td><td>1</td><td>1</td><td></td><td>b 2c</td></tr></table>

Suitably choose $a , b , c ,$ , as method can get global truncation error with order $O ( h ^ { 2 } )$

Remark 9.12. Dimension of $x , y , z$ may be different.

Remark 9.13. Theorem 9.10 can be extended with no difficulty to the following system:

$$
{ \dot { x } } _ { 1 } = f _ { 2 } ( x _ { 2 } ) \quad { \dot { x } } _ { 2 } = f _ { 3 } ( x _ { 4 } ) , \quad \cdots , \quad { \dot { x } } _ { n } = f _ { 1 } ( x _ { 1 } ) .
$$

# 10.9.4 Some Explanations

We usually state that symplectic method is volume-preserving scheme. But this parlance is somewhat irrelevancy because symplectic scheme (satisfying symplectic condition), true only in this case, that it applied to Hamiltonian system. For P–R–K method $( d _ { i j } , \delta _ { i } , c _ { i j } , \gamma _ { j } )$ , if it satisfies

$$
\gamma _ { i } d _ { i j } + \delta _ { i } c _ { j i } - \gamma _ { i } \delta _ { j } = 0 ,
$$

we can say this integrator is symplectic. If system is not Hamiltonian, we cannot say that this $\mathrm { P - R - K }$ method is symplectic. The main problem is that we say a scheme is symplectic because it preserves symplectic structure for a given system. Therefore, only Hamiltonian system possesses symplectic structure. Consequently, we cannot say “volume-preserving P–R–K methods form a subset of symplectic ones”.

Until now, we gave some criteria for volume-preserving by $\mathbf { R - K }$ and P–R–K methods. In fact, it is almost impossible based on these criteria to construct volumepreserving algorithm with high order accuracy. Indeed, we even cannot predict that there exists schemes which satisfied those criteria. We are too far to resolve these problems.

It should be noted that in the above discussion, we always suppose system is not reducible. In other words, det $M \neq 0$ . But in practice, some systems are reducible, for example

$$
\begin{array} { r l } & { \dot { \boldsymbol { x } } = c \boldsymbol { y } - b \boldsymbol { z } , } \\ & { \dot { \boldsymbol { y } } = a \boldsymbol { z } - c \boldsymbol { x } , \quad a , b , c \in { \bf R } . } \\ & { \dot { \boldsymbol { z } } = b \boldsymbol { x } - a \boldsymbol { y } , } \end{array}
$$

In fact, for this system, centered Euler scheme is volume-preserving. Furthermore, LobattoIIIA, LobattoIIIB, LobattoIIIS, RadauIB, RadauIIB etc. are also volumepreserving. With detailed analysis of the process in Subsection 10.9.2, it is easy to get the following[QL00] .

Theorem 9.14. If the dimension of $M$ is odd, then the R–K methods based on high order quadrature formulae, such as LobattoIIIA, LobattoIIIB, LobattoIIIS, RadauI, RadauIIB etc., are volume-preserving, iff

$$
\lambda ( M ) = \left( \lambda _ { 1 } , \lambda _ { 2 } , \cdots , \lambda _ { \frac { n } { 2 } } , 0 , - \lambda _ { 1 } , - \lambda _ { 2 } , - \cdots , - \lambda _ { \frac { n } { 2 } } \right) .
$$

We also find that in Theorem 9.4, det $M \neq 0$ is not necessary.

As for nonlinear systems, we cannot give some satisfactory results. A nonlinear system

$$
\dot { y } = f ( y ) , \quad t \in \mathbf { R } , \ y \in \mathbf { R } ^ { n } ,
$$

is said to be source-free if $\mathrm { d i v } f = \sum _ { i = 1 } ^ { n } { \frac { \partial f _ { i } ( y ) } { \partial y _ { i } } } = 0 .$ . Such system preserves the phase volume on the phase $R ^ { n }$ . For these systems, we only point out the centered Euler

schemes is volume-preserving iff the Jacobian ∂ fi = M is, in some sense, similar to an infinitesimally symplectic matrix. That is, the eigenvalues of $M$ can be specified as

or

$$
\lambda ( M ) = \left( \lambda _ { 1 } , \lambda _ { 2 } , \cdot \cdot \cdot , \lambda _ { \frac { n } { 2 } } , - \lambda _ { 1 } , - \lambda _ { 2 } , - \cdot \cdot \cdot , - \lambda _ { \frac { n } { 2 } } \right) ,
$$

$$
\lambda ( M ) = \left( \lambda _ { 1 } , \lambda _ { 2 } , \cdots , \lambda _ { \frac { n } { 2 } } , 0 , - \lambda _ { 1 } , - \lambda _ { 2 } , - \cdots , - \lambda _ { \frac { n } { 2 } } \right) .
$$

# Bibliography

[DV84] K. Dekker and J.G. Verwer: Stability of Runge–Kutta Methods for Stiff Initial Value Problems. Elesevier Science Pub. B. V., North-Holland, Amsterdam, (1984).   
[FS95] K. Feng and Z. J. Shang: Volume-preserving algorithms for source-free dynamical systems. Numer. Math., 71:451–463, (1995).   
[FW94] K. Feng and D.L. Wang: Dynamical systems and geometric construction of algorithms. In Z. C. Shi and C. C. Yang, editors, Computational Mathematics in China, Contemporary Mathematics of AMS, Vol. 163, pages 1–32. AMS, (1994).   
[HW81] E. Hairer and G. Wanner: Algebraically stable and implementable Runge–Kutta methods of high order. SIAM J. Numer. Anal., 18:1098–1108, (1981).   
[MQ04] R.I. McLachlan and G.R.W. Quispel: Explicit geometric integration of polynomial vector fields. BIT, 44:513–538, (2004).   
[QD97] G. R. W. Quispel and C. P. Dyt: Solving ODE’s numerically while preserving symmetries, Hamiltonian structure, phase space volume, or first integrals. In A. Sydow, editor, Proceedings of the 15th IMACS World Congress, pages 601–607. Wissenschaft & Technik, Berlin, (1997).   
[QD98] G. R. W. Quispel and C. P. Dyt: Volume-preserving integrators have linear error growth. Physics Letters A, 202:25–30, (1998).   
[QL00] M. Z. Qin and H. W. Li: Volume preserving R–K methods for linear systems. Acta Applicandae Mathematicae, 16:430–434, (2000).   
[QM03] G. R. W. Quispel and D. I. McLaren: Explicit volume-preserving and symplectic integrators for trigonometric polynomial flows. J. of Comp. Phys., 186(1):308–316, (2003).   
[Qui95] G. R. W. Quispel: Volume-preserving integrators. Physics Letters A, 206:26–30, (1995).   
[QZ92] M. Z. Qin and W. J. Zhu: Construction of higher order symplectic schemes by composition. Computing, 47:309–321, (1992).   
[QZ93] M. Z. Qin and W. J. Zhu: Volume-preserving schemes and numerical experiments. Computers Math. Applic., 26:33–42, (1993).   
[Sco91] C. Scovel: Symplectic numerical integration of Hamiltonian systems. In T. Ratiu, editor, The Geometry of Hamiltonian Systems, pages 463–496. Springer, New York, (1991).   
[Sha94a] Z Shang: Construction of volume-preserving difference schemes for source-free systems via generating functions. J. Comput. Math., 12:265–272, (1994).   
[Sha94b] Z. Shang: Generating functions for volume-preserving mappings and Hamilton– Jacobi equations for source-free dynamical systems. Science in China (series A), 37:1172– 1188, (1994).   
[Sun95] G. Sun: Construction of high order symplectic Partitioned–Runge–Kutta methods. J. Comput. Math., 13(1):40–50, (1995).   
[Sur96] Y. B. Suris: Partitioned–Runge–Kutta methods a phase volume preserving integrators. Physics Letters A, 220:63–69, (1996).   
[TH85] A. Thyagaraja and F.A. Haas: Representation of volume-preserving maps induced by solenoidal vector fields. Phys. Fluids, 28:1005, (1985).   
[Wey40] H. Weyl: The method of orthogonal projection in potential theory. Duke Math. J., 7:411–444, (1940).

# Chapter 11. Contact Algorithms for Contact Dynamical Systems

An odd-dimensional manifold cannot admit a symplectic structure. The analogue of symplectic structure for odd-dimensional manifolds is a little less symmetric, but is also a very interesting structure – the contact structure. In this chapter, we apply the ideas of preserving Lie group and Lie algebra structure of dynamical systems in constructing symplectic algorithms for Hamiltonian systems to the study of numerical algorithms for contact dynamical systems and present so-called contact algorithms, i.e., algorithms preserving contact structure, for solving numerically contact systems.

# 11.1 Contact Structure

The source of contact structures are manifolds of contact element of configuration spaces. It is also of basic importance in physical and engineering sciences. Contact geometry has – as does symplectic geometry – broad applications in physics, e.g. geometrical optics, classical mechanics, thermodynamics, geometric quantization, and applied mathematics such as control theory.

# 11.1.1 Basic Concepts of Contact Geometry

Contact geometry $\mathbf { \left[ A r n 8 9 , A r n 8 8 \right]} $ is the study of a geometric structure on smooth manifolds given by a hyperplane distribution in the tangent bundle and specified by a one-form, both of which satisfy a “maximum non-degeneracy” condition called “complete nonintegrability”.

The integration of first-order partial differential equations is reduced to the integration of a system of ordinary differential equations, the so-called characteristic equations. The basic of this reduction is a simple geometric analysis of the formulation of curves. Let $M$ be a smooth manifold and let $V$ be a direction field on $M$ .

Definition 1.1. $N \subset M$ is called an integral surface of $V$ if the tangent plane of $N$ contains the direction of $V$ at every point (Fig. 1.1).

Let $\varGamma$ be a $k$ -dimensional submanifold in an $n$ -dimensional manifold $M$ (Fig. 1.2), $\varGamma$ is called a hypersurface if $k = n - 1$ .

The Cauchy problem for the direction field $v$ with initial manifold $\varGamma$ is the problem of finding a $( k + 1 )$ -dimensional integral submanifold of $v$ containing the initial submanifold $\varGamma$ .

![](images/8f31855523d579ac163c9f8c35685dc43f186abfb276853d05f9456d86bd6325.jpg)  
Fig. 1.1. Meaning of definition

![](images/edec02e4f19c9d194910bef438270694a057432d6e3786f4e04bca10ded95131.jpg)

![](images/e2d8ded28dfefe774219e91b3417026860e9986418771b0adda7d33f03c436ce.jpg)  
Fig. 1.2. Integral surface with initial manifold of $\varGamma$

Every point in $n$ -dimensional space existence an $( n - 1 )$ -dimensional hyperplane, $\operatorname { c o d i m } = 1$ field of hyperplane, this means field of tangent hyperplane can be locally described by 1-form, and

$$
\begin{array} { c } { { \displaystyle \alpha = \sum _ { i = 1 } ^ { n } \alpha _ { i } \mathbf { d } x _ { i } , \mathrm { a n d } } } \\ { { \displaystyle \sum _ { i = 1 } ^ { n } \alpha _ { i } ^ { 2 } ( x ) \neq 0 , \quad \forall x \in \mathbf { R } ^ { n } . } } \end{array}
$$

Hyperplane in Fig. 1.3 is null space of 1-form $\alpha$ . Relation between hyperplane and its 1-form is not 1- to $^ { - 1 }$ correspondence. They may be different up to multiplication by a non zero constant. This multiplicator is dependent of point.

We consider what a filed of hyperplane looks like in general in a neighborhood of a point in an $n$ -dimensional manifold. For example, let $n = 2$ . Then the manifold is a surface and field of hyperplane is a field of straight line. Such a field in a neighborhood of a point is always constructed very simply, namely, as a field of tangent to a family of parallel lines in a plane. More precisely, one of the basic results of the local theory of ODEs is that it is possible to change any smooth field of tangent lines on a manifold into a field of tangents to family of straight lines in Euclidean space by using a diffeomorphism in a sufficiently small neighborhood of any point of the manifold.

![](images/f784e8ac6b6cb0d09205e610cfd6d23629ce7914b40b9a0093d881c5edaeaf82.jpg)  
Fig. 1.3. Hyperplane

If $n > 2$ , then a hyperplane is not a line. For example, if $n = 3$ , most field of 2-dimensional tangent planes in ordinary 3-dimensional space cannot be diffeomorphically mapped onto a field of parallel planes. The reason is that there exists fields of tangent planes for which it is impossible to find integral surfaces, i.e., surface which have the prescribed tangent plane at each point.

A 1-form in 3-dimensional can be written in following standard form

$$
\alpha = x \mathbf { d } y + \mathbf { d } z .
$$

Every tangent hyperplane in point $x$ , which is denoted by $\Pi _ { x }$ , have:

$$
\left[ \eta _ { x } , \eta _ { y } , \eta _ { z } \right] \left[ \begin{array} { c } { { 0 } } \\ { { x } } \\ { { 1 } } \end{array} \right] = 0 ,
$$

and $[ 0 , x , 1 ]$ not all equal to zero, it is defined as a 2-dimensional field of hyperplane.

When $x = 0$ ,

$$
{ \left[ \begin{array} { l } { 0 } \\ { 0 } \\ { 1 } \end{array} \right] } ^ { \mathrm { T } } { \left[ \begin{array} { l } { \eta _ { x } } \\ { \eta _ { y } } \\ { 0 } \end{array} \right] } = 0 .
$$

Each point with a hyperplane intersecting wall defines a direction field, see Fig. 1.4 and 1.5.

Next, we prove that in $\mathbf { R } ^ { 3 }$ space, there does not exist an integral surface which can be given by the 1-form $\alpha = x \mathbf { d } y + \mathbf { d } z$ , where $x , y$ is horizontal coordinate, $z$ is vertical coordinate, see Fig. 1.6.

Consider a pair of vectors emanating from the origin (0,0,0) and lying in the horizontal plane of our coordinate systems; another integral curve from (0,0,0) to (0,1,0), and then from (0,1,0) to (1,1,0), and another integral curve from (0,0,0) to (1,0,0), and then from (1,0,0) to $( 1 , 1 , - 1 )$ . As a result, these two curves cannot close up. The difference in the heights of these points is 1, this difference can be considered as a measure of the nonintegrability of the field.

We have four direction fields from the origin point 0 to walls of east, south, west, and north, respectively, describing by Fig. 1.5.

![](images/02c4e835b0ed8d7e0408f9277b5d7e29499771841594a5f8b9fe52912f57ada5.jpg)  
Fig. 1.4. Defines the field of $2 n$ -dimensional plane $\alpha = 0$ in $\mathbf { R } ^ { 2 n + 1 }$

![](images/eb1f1f308ef40d897bb38dec4fee247d10b33367c102ff5f9651469334a769f2.jpg)  
Fig. 1.5. Direction fields in each wall

# 11.1.2 Contact Structure

A contact element to an $n$ -dimensional smooth manifold at some point is an $( n - 1 )$ - dimensional plane tangent to the manifold at that point, i.e., an $( n - 1 )$ -dimensional subspace of the $n$ -dimensional tangent space at that point. At the $n$ -dimensional space for each point there is a $n - 1$ dimensional hyperplane, dimensions of this hyperplane field is $n - 1$ . We note first that a field of hyperplanes can be given locally by a differential 1-form: a plane in the tangent space gives a 1-form up to multiplication by a non zero constant. We choose this constant so that the value of the form on vertical basic vector is equal to 1. The Hyperplanes of the field are null space of the 1-form[Arn89,Arn88] .

Definition 1.2. A field of hyperplanes is said to be nondegenerate at a point if the rank of the 2-form $\mathrm { d } \alpha | _ { \omega = 0 }$ in the plane of the field passing through this point is equal to the dimension of the plane.

Definition 1.3. A differential 1-form $\alpha$ which is nowhere equal to the zero form on a manifold $M$ is called a contact form if the exterior derivative $\mathrm { d } \alpha$ of $\alpha$ defines a nondegenerate exterior 2-form in every plane $\alpha = 0$ .

![](images/8035f0b8e4a31a2787b109921188b5181cd52a7bdb046bd939eb5b252ac46474.jpg)  
Fig. 1.6. Integral curves constructed for a non-integrable field of planes

Example 1.4. Consider the space $\mathbf { R } ^ { 2 n + 1 }$ with the contact structure by the 1-form $\alpha = \mathbf { d } u + p \mathbf { d } q$ . Where $q = ( q _ { 1 } , \cdots , q _ { n } ) , u , p = ( p _ { 1 } , \cdots , p _ { n } )$ , $\alpha$ is not equal to zero form at any point in $\mathbf { R } ^ { 2 n + 1 }$ , and consequently defines the field of $2 n$ -dimensional planes α = 0 in R2n+1.

Example 1.5. The form constructed in Example 1.4 is a contact form, the exterior derivatives of the form $\alpha$ is equal to

$$
\mathbf { d } \alpha | _ { \alpha = 0 } = \mathbf { d } q _ { 1 } \wedge \mathbf { d } p _ { 1 } + \cdot \cdot \cdot + \mathbf { d } q _ { n } \wedge \mathbf { d } p _ { n } .
$$

In the plane $\alpha = 0$ , $\left( q _ { 1 } , \cdot \cdot \cdot , q _ { n } ; p _ { 1 } , \cdot \cdot \cdot , p _ { n } \right)$ may serve as coordinate.

The matrix of the form $\omega = \mathrm { d } \alpha | _ { \alpha = 0 }$ has the form $\left[ \begin{array} { l l } { O } & { - I } \\ { I } & { O } \end{array} \right]$ , where $I$ is the identity matrix of order $n$ . The determinant of this matrix is equal to 1. Consequently, the 2-form $\omega$ is nondegenerate. In other words, the rank of this form is $2 n$ , so our field is nondegenerate at the origin and thus also in a neighborhood of the origin (in fact, this field of planes is nondegenerate at all points of the space).

Definition 1.6. A contact structure on the manifold $M$ is a field of tangent plane which are given locally as the set of zeros of a contact 1-form. The hyperplanes of the field are called contact hyperplanes. We can denote by $\Pi _ { x }$ the contact hyperplane at the point $x$ . Putting briefly, a contact structure on a manifold is a nondegenerate field of tangent hyperplane.

Definition 1.7. A field of planes is called nondegenerated on a manifold if it is nondegenerate at every point of the manifold.

It should be noted that on the even-dimensional manifold there cannot be a nondegenerate field of hyperplanes, on such a manifold a hyperplane is odd-dimensional, and the rank of every skew-symmetric bilinear form on an odd-dimensional space is less than the dimension of the space. Nondegenerate field of hyperplane do exist on odd-dimensional manifold.

Definition 1.8. A hyperplane (dimension $n - 1 \mathrm { \Delta }$ ) tangent to a manifold at some point is called a contact element, and this point is called the point of contact.

The set of all contact element of an $n$ -dimensional manifold has the structure of a smooth manifold of dimension $2 n - 1$ . The manifold of all contact elements of an $n$ -dimensional manifold is a fiber bundle whose base is our manifold and whose fiber is $( n - 1 )$ -dimensional projective space.

Theorem 1.9. The bundle of contact element is the projectivization of the cotangent bundle: it can be obtained from the cotangent bundle by changing every cotangent $n$ -dimensional vector space into on $( n - 1 )$ -dimensional projective space (a point of which is a line passing through the origin in the cotangent space).

Proof. A contact element is given by a 1-form on the tangent space, for which this element is not zero, and it is determined up to multiplication by a non zero number. But a form on the tangent space is a vector of the cotangent space. Therefore, a non zero vector of the cotangent space, determined up to a multiplication by a non zero number, is a non zero vector of the cotangent space, determined up to a multiplication by a non zero number, i.e., a point of the projectivized cotangent space. -

In this chapter, we simply consider the Euclidean space $\mathbf { R } ^ { 2 n + 1 }$ of $2 n { + 1 }$ dimensions as our basic manifold with the contact structure given by the normal form

$$
\alpha = \sum _ { i = 1 } ^ { n } x _ { i } \mathbf { d } y _ { i } + \mathbf { d } z = x \mathbf { d } y + \mathbf { d } z = ( 0 , x ^ { \mathrm { T } } , 1 ) \left[ \begin{array} { l } { \mathbf { d } x } \\ { \mathbf { d } y } \\ { \mathbf { d } z } \end{array} \right] ,
$$

here we have used 3-symbol notation to denote the coordinates and vectors on $\mathbf { R } ^ { 2 n + 1 }$

$$
x = ( x _ { 1 } , \cdots , x _ { n } ) ^ { \mathrm { T } } , \quad y = ( y _ { 1 } , \cdots , y _ { n } ) ^ { \mathrm { T } } , \quad z = ( z ) .
$$

A contact dynamical system on $\mathbf { R } ^ { 2 n + 1 }$ is governed by a contact vector field $f =$ $( a ^ { \mathrm { T } } , b ^ { \mathrm { T } } , c ) : \dot { \mathbf { R } ^ { 2 n + 1 } } \xrightarrow { } \dot { \mathbf { R } ^ { 2 n + 1 } }$ through equations

$$
\dot { x } = a ( x , y , z ) , \quad \dot { y } = b ( x , y , z ) , \quad \dot { z } = c ( x , y , z ) , \quad \cdot = : \frac { \mathrm { d } } { \mathrm { d } t } ,
$$

where the contactivity condition of the vector field $f$ is

$$
L _ { f } \alpha = \lambda _ { f } \alpha ,
$$

with some function $\begin{array} { r } { { \lambda } _ { f } : \begin{array} { r } { { \mathbf { R } } ^ { 2 n + 1 } \to { \mathbf { R } } } \end{array} } \end{array}$ , called the multiplier of $f$ . In (1.4), $L _ { f } \alpha$ denotes the Lie derivation of $\alpha$ with respect to $f$ and is usually calculated by the formula (see Chapter 1 of book)[Arn88]

$$
L _ { f } \alpha = i _ { f } { \bf d } \alpha + { \bf d } i _ { f } \alpha .
$$

It is easy to show from (1.4) and (1.5) that to any contact vector field $f$ on $\mathbf { R } ^ { 2 n + 1 }$ , there corresponds a function $K ( x , y , z )$ , called contact Hamiltonian, such that

$$
a = - K _ { y } + K _ { z } x , \quad b = K _ { x } , \quad c = K - x ^ { \operatorname { T } } K _ { x } = : K _ { e } .
$$

In fact, (1.6) represents the general form of a contact vector field. Its multiplier, denoted as $\lambda _ { f }$ from now, is equal to $K _ { z }$ .

Definition 1.10. A contact transformation $g$ is a diffeomorphism on $\mathbf { R } ^ { 2 n + 1 }$

$$
g : \quad { \left( \begin{array} { l } { x } \\ { y } \\ { z } \end{array} \right) } \quad \longrightarrow \quad { \left( \begin{array} { l } { { \widehat { x } } ( x , y , z ) } \\ { { \widehat { y } } ( x , y , z ) } \\ { { \widehat { z } } ( x , y , z ) } \end{array} \right) }
$$

conformally preserving the contact structure, i.e., $g ^ { * } \alpha = \mu _ { g } \alpha$ , that means

$$
\sum _ { i = 1 } ^ { n } { \widehat { x } } _ { i } \mathbf { d } { \widehat { y } } _ { i } + \mathbf { d } { \widehat { z } } = \mu _ { g } \left( \sum _ { i = 1 } ^ { n } x _ { i } \mathbf { d } y _ { i } + \mathbf { d } z \right) ,
$$

for some everywhere non-vanishing function $\mu _ { g } : \mathbf { R } ^ { 2 n + 1 } \to \mathbf { R }$ , called the multiplier of $g$ .

The explicit expression of (1.7) is

$$
( 0 , { \widehat x } ^ { \mathrm { T } } , 1 ) \left[ \begin{array} { l l l } { { \widehat x } _ { x } } & { { \widehat x } _ { y } } & { { \widehat x } _ { z } } \\ { { \widehat y } _ { x } } & { { \widehat y } _ { y } } & { { \widehat y } _ { z } } \\ { { \widehat z } _ { x } } & { { \widehat z } _ { y } } & { { \widehat z } _ { z } } \end{array} \right] = \mu _ { g } ( 0 , x ^ { \mathrm { T } } , 1 ) .
$$

A fundamental fact is that the phase flow $g _ { K } ^ { t }$ of a contact dynamical system associated with a contact Hamiltonian $K : \mathbf { R } ^ { 2 n + 1 } \stackrel { - } {  } \mathbf { R }$ is a one parameter (local) group of contact transformations on $\mathbf { R } ^ { 2 n + 1 }$ , i.e., $g _ { K } ^ { t }$ satisfies

$$
\begin{array} { r l } & { g _ { K } ^ { 0 } = \mathrm { i d e n t i t y ~ m a p ~ o n ~ } { \bf R } ^ { 2 n + 1 } ; } \\ & { g _ { K } ^ { t + s } = g _ { K } ^ { t } \circ g _ { K } ^ { s } , \quad \forall t , s \in { \bf R } ; } \\ & { ( g _ { K } ^ { t } ) ^ { * } \alpha = \mu _ { g _ { K } ^ { t } } \alpha , } \end{array}
$$

for some everywhere non-vanishing function $\mu _ { g _ { K } ^ { t } } : \mathbf { R } ^ { 2 n + 1 } \to \mathbf { R }$ . Moreover, we have the following relation between $\mu _ { G _ { k } ^ { * } }$ K and the Hamiltonian $K$ :

$$
\mu _ { g _ { K } ^ { t } } = \exp \int _ { 0 } ^ { t } ( K _ { z } \circ g _ { K } ^ { s } ) \mathrm { d } s .
$$

For general contact systems, condition (1.10) is stringent for algorithmic approximations to phase flows because only the phase flows themselves satisfy it. We will construct algorithms for contact systems such that the corresponding algorithmic approximations to the phase flows satisfy the condition (1.10), of course, probably, with different, but everywhere non-vanishing, multipliers from $\mu _ { g _ { K } ^ { t } }$ . We call such algorithms as contact ones.

# 11.2 Contactization and Symplectization

There is a well known correspondence between contact geometry on $\mathbf { R } ^ { 2 n + 1 }$ and conic (or homogeneous) symplectic geometry on $\mathbf { R } ^ { 2 n + 2 }$ . To establish this correspondence, we introduce two spaces $\mathbf { R } _ { + } ^ { 2 n + 2 }$ and ${ \bf R } _ { + } \times { \bf R } ^ { 2 n + 1 }$ .

a. We use the 4-symbol notation for the coordinates on $\mathbf { R } ^ { 2 n + 2 }$

$$
\left[ \begin{array} { c } { p _ { 0 } } \\ { p _ { 1 } } \\ { q _ { 0 } } \\ { q _ { 1 } } \end{array} \right] , \quad p _ { 0 } = ( p _ { 0 } ) , \quad q _ { 0 } = ( q _ { 0 } ) , \quad p _ { 1 } = \left[ \begin{array} { c } { p _ { 1 1 } } \\ { \vdots } \\ { p _ { 1 n } } \end{array} \right] , \quad q _ { 1 } = \left[ \begin{array} { c } { q _ { 1 1 } } \\ { \vdots } \\ { q _ { 1 n } } \end{array} \right] .
$$

Consider

$$
{ \bf R } _ { + } ^ { 2 n + 2 } = \left\{ ( p _ { 0 } , p _ { 1 } , q _ { 0 } , q _ { 1 } ) \in { \bf R } ^ { 2 n + 2 } \ | \ p _ { 0 } > 0 \right\}
$$

as a conic symplectic space with the standard symplectic form

$$
\omega = \mathrm { d } p _ { 0 } \wedge \mathrm { d } q _ { 0 } + \mathrm { d } p _ { 1 } \wedge \mathrm { d } q _ { 1 } .
$$

Definition 2.1. Function $\phi : \mathbf { R } _ { + } ^ { 2 n + 2 } \to \mathbf { R }$ is called a conic function if it satisfies

$$
\phi ( p _ { 0 } , p _ { 1 } , q _ { 0 } , q _ { 1 } ) = p _ { 0 } \phi \Bigl ( 1 , \frac { p _ { 1 } } { p _ { 0 } } , q _ { 0 } , q _ { 1 } \Bigr ) , \quad \forall p _ { 0 } > 0 .
$$

So, a conic function on $\mathbf { R } ^ { 2 n + 2 }$ depends essentially only $2 n + 1$ variables.

${ \cal F } : { \bf R } _ { + } ^ { 2 n + 2 }  { \bf R } _ { + } ^ { 2 n + 2 }$

$$
F \circ T _ { \lambda } = T _ { \lambda } \circ F , \quad \forall \lambda > 0 ,
$$

where $T _ { \lambda }$ is the linear transformation on $\mathbf { R } ^ { 2 n + 2 }$

$$
T _ { \lambda } \left[ \begin{array} { c } { { p } } \\ { { q } } \end{array} \right] = \left[ \begin{array} { c } { { \lambda p } } \\ { { q } } \end{array} \right] , \quad p = \left[ \begin{array} { c } { { p _ { 0 } } } \\ { { p _ { 1 } } } \end{array} \right] , \quad q = \left[ \begin{array} { c } { { q _ { 0 } } } \\ { { q _ { 1 } } } \end{array} \right] .
$$

The conic condition (2.5) for the mapping $F : ( p _ { 0 } , p _ { 1 } , q _ { 0 } , q _ { 1 } )  ( P _ { 0 } , P _ { 1 } , Q _ { 0 } , Q _ { 1 } )$ can be expressed as follows:

$$
\begin{array} { r l } & { P _ { 0 } ( p _ { 0 } , p _ { 1 } , q _ { 0 } , q _ { 1 } ) = p _ { 0 } P _ { 0 } \Big ( 1 , \frac { p _ { 1 } } { p _ { 0 } } , q _ { 0 } , q _ { 1 } \Big ) > 0 , } \\ & { P _ { 1 } ( p _ { 0 } , p _ { 1 } , q _ { 0 } , q _ { 1 } ) = p _ { 0 } P _ { 1 } \Big ( 1 , \frac { p _ { 1 } } { p _ { 0 } } , q _ { 0 } , q _ { 1 } \Big ) , } \\ & { Q _ { 0 } ( p _ { 0 } , p _ { 1 } , q _ { 0 } , q _ { 1 } ) = Q _ { 0 } \Big ( 1 , \frac { p _ { 1 } } { p _ { 0 } } , q _ { 0 } , q _ { 1 } \Big ) , } \\ & { Q _ { 1 } ( p _ { 0 } , p _ { 1 } , q _ { 0 } , q _ { 1 } ) = Q _ { 1 } \Big ( 1 , \frac { p _ { 1 } } { p _ { 0 } } , q _ { 0 } , q _ { 1 } \Big ) , } \end{array} \qquad \forall \ : p _ { 0 } > 0 .
$$

So, a conic map is essentially depending only on $2 n + 2$ functions in $2 n + 1$ variables.

It should be noted that, in some cases, we also consider conic functions and conic maps defined on the whole Eucildean space. The following lemma gives a criterion of a conic symplectic map.

Lemma 2.3. $F : ( p _ { 0 } , p _ { 1 } , q _ { 0 } , q _ { 1 } )  ( P _ { 0 } , P _ { 1 } , Q _ { 0 } , Q _ { 1 } )$ is a conic symplectic map if and only if $( 0 , 0 , P _ { 0 } ^ { \mathrm { T } } , P _ { 1 } ^ { \mathrm { T } } ) F _ { * } - ( 0 , 0 , p _ { 0 } ^ { T } , p _ { 1 } ^ { \mathrm { T } } ) = 0$ , where $F _ { * }$ is the Jacobi matrix of $F$ at the point $\left( p _ { 0 } , p _ { 1 } , q _ { 0 } , q _ { 1 } \right)$ .

Proof. For $F : ( p _ { 0 } , p _ { 1 } , q _ { 0 } , q _ { 1 } )  ( P _ { 0 } , P _ { 1 } , Q _ { 0 } , Q _ { 1 } )$ , the condition

$$
( 0 , 0 , P _ { 0 } ^ { \mathrm { T } } , P _ { 1 } ^ { \mathrm { T } } ) F _ { * } - ( 0 , 0 , p _ { 0 } ^ { \mathrm { T } } , p _ { 1 } ^ { \mathrm { T } } ) = 0 ,
$$

is equivalent to the condition

$$
P _ { 0 } \mathbf { d } Q _ { 0 } + P _ { 1 } \mathbf { d } Q _ { 1 } = p _ { 0 } \mathbf { d } q _ { 0 } + p _ { 1 } \mathbf { d } q _ { 1 } , \quad \mathrm { o r } \quad P \mathbf { d } Q = p \mathbf { d } q ,
$$

where $P = ( P _ { 0 } , P _ { 1 } ) , Q = ( Q _ { 0 } , Q _ { 1 } ) , p = ( p _ { 0 } , p _ { 1 } ) , q = ( q _ { 0 } , q _ { 1 } ) .$ Hence in matrix form, it can be written as

$$
\begin{array} { r } { Q _ { p } ^ { \mathrm { T } } \cdot P = 0 , \quad Q _ { q } ^ { \mathrm { T } } \cdot P = p . } \end{array}
$$

Notice that a function $f ( x _ { 1 } , x _ { 2 } , \cdots , x _ { n } )$ is homogeneous of degree $k$ , i.e.,

$$
f ( \lambda x _ { 1 } , \lambda x _ { 2 } , \cdots , \lambda x _ { n } ) = \lambda ^ { k } f ( x _ { 1 } , x _ { 2 } , \cdots , x _ { n } ) ,
$$

if and only if

$$
\sum x _ { i } f _ { x _ { i } } ( x _ { 1 } , x _ { 2 } , \cdots , x _ { n } ) = k f ( x _ { 1 } , x _ { 2 } , \cdots , x _ { n } ) .
$$

Therefore, the condition (2.7) is equivalent to

$$
P _ { p } ( p , q ) \cdot p = P ( p , q ) , \quad Q _ { p } ( p , q ) = 0 .
$$

If $F$ is conic symplectic, then

$$
\begin{array} { r } { Q _ { p } ^ { \mathrm { { T } } } P _ { p } - P _ { p } ^ { \mathrm { { T } } } Q _ { p } = O , \quad Q _ { q } ^ { \mathrm { { T } } } P _ { q } - P _ { q } ^ { \mathrm { { T } } } Q _ { q } = O , \quad Q _ { q } ^ { \mathrm { { T } } } P _ { p } - P _ { q } ^ { \mathrm { { T } } } Q _ { p } = I . } \end{array}
$$

Combining with (2.11), we get

$$
p = Q _ { q } ^ { \mathrm { T } } P _ { p } p - P _ { q } ^ { \mathrm { T } } Q _ { p } p = Q _ { q } ^ { \mathrm { T } } P , O = Q _ { p } ^ { \mathrm { T } } P _ { p } p - P _ { p } ^ { \mathrm { T } } Q _ { p } p = Q _ { p } ^ { \mathrm { T } } P .
$$

This proves the “only if” part.

Conversely, if $F$ satisfies the condition (2.8), then it satisfies (2.9), which means that it is symplectic. We know that if a matrix is symplectic, then its transpose is also symplectic. Therefore,

$$
P _ { q } P _ { p } ^ { \mathrm { T } } - P _ { p } P _ { q } ^ { \mathrm { T } } = O , \quad Q _ { q } Q _ { p } ^ { T } - Q _ { p } Q _ { q } ^ { \mathrm { T } } = O , \quad P _ { p } Q _ { q } ^ { \mathrm { T } } - P _ { q } Q _ { p } ^ { \mathrm { T } } = I .
$$

Combining with (2.10), we get

$$
\begin{array} { r } { P = P _ { p } Q _ { q } ^ { \mathrm { T } } P - P _ { q } Q _ { p } ^ { \mathrm { T } } P = P _ { p } p , } \\ { 0 = Q _ { q } Q _ { p } ^ { \mathrm { T } } P - Q _ { p } Q _ { q } ^ { \mathrm { T } } P = Q _ { q } p . } \end{array}
$$

This means that $F$ is conic. This finishes the proof.

b. Consider ${ \bf R } _ { + } \times { \bf R } ^ { 2 n + 1 }$ as the product of the positive real space $\mathbf { R } _ { + }$ and the contact space $\mathbf { R } ^ { 2 n + 1 }$ . We use $( w , x , y , z )$ to denote the coordinates of ${ \bf R } _ { + } \times { \bf R } ^ { 2 n + 1 }$ with $w > 0$ and with $x , y , z$ as before.

Definition 2.4. A map ${ \cal G } \colon { \mathbf { R } } _ { + } \times { \mathbf { R } } ^ { 2 n + 1 }  { \mathbf { R } } _ { + } \times { \mathbf { R } } ^ { 2 n + 1 }$ is called a positive product map if it is composed by a map $g : \mathbf { R } ^ { 2 n + 1 } \to \mathbf { R } ^ { 2 n + 1 }$ and a positive function $\gamma :$ ${ \bf R } ^ { 2 n + 1 }  { \bf R } _ { + }$ in the form

$$
\left[ \begin{array} { c } { { w } } \\ { { x } } \\ { { y } } \\ { { z } } \end{array} \right] \longrightarrow \left[ \begin{array} { c } { { W } } \\ { { X } } \\ { { Y } } \\ { { Z } } \end{array} \right] , \quad W = w \gamma ( x , y , z ) , \quad ( X , Y , Z ) = g ( x , y , z ) .
$$

We denote $\gamma \otimes g$ the positive product map composed of map $g$ and function $\gamma$ .

c. Define mapping $S : \mathbf { R } _ { + } \times \mathbf { R } ^ { 2 n + 1 } \to \mathbf { R } _ { + } ^ { 2 n + 2 }$

$$
\left[ \begin{array} { l } { w } \\ { x } \\ { y } \\ { z } \end{array} \right] \longrightarrow \left[ \begin{array} { l } { p _ { 0 } = w } \\ { p _ { 1 } = w x } \\ { q _ { 0 } = z } \\ { q _ { 1 } = y } \end{array} \right] .
$$

Then the inverse $S ^ { - 1 } : { \bf R } _ { + } ^ { 2 n + 2 }  { \bf R } _ { + } \times { \bf R } ^ { 2 n + 1 }$ is given by

$$
\left[ \begin{array} { c } { { p _ { 0 } } } \\ { { p _ { 1 } } } \\ { { q _ { 0 } } } \\ { { q _ { 1 } } } \end{array} \right] \longrightarrow \left[ \begin{array} { c } { { w = p _ { 0 } } } \\ { { x = \frac { p _ { 1 } } { p _ { 0 } } } } \\ { { y = q _ { 1 } } } \\ { { z = q _ { 0 } } } \end{array} \right] , \quad p _ { 0 } \neq 0 .
$$

Lemma 2.5. [Fen93b,Fen95] Given a transformation $F : ( p _ { 0 } , p _ { 1 } , q _ { 0 } , q _ { 1 } ) \to ( P _ { 0 } , P _ { 1 } , Q _ { 0 }$ , $Q _ { 1 } )$ on $\mathbf { R } _ { + } ^ { 2 n + 2 }$ and let $G = S ^ { - 1 } \circ F \circ S$ . Then we have:

$1 ^ { \circ }$ $F$ is a conic map on $\mathbf { R } _ { + } ^ { 2 n + 2 }$ if and only if $G$ is a positive product map on ${ \bf R } _ { + } \times { \bf R } ^ { 2 n + 1 }$ ; in this case, if we write $G = \gamma \otimes g$ , then

$$
\gamma ( x , y , z ) = P _ { 0 } ( 1 , x , z , y ) ,
$$

and $g : ( x , y , z ) \to ( X , Y , Z )$ is given by

$$
X = \frac { P _ { 1 } ( 1 , x , z , y ) } { P _ { 0 } ( 1 , x , z , y ) } , \quad Y = Q _ { 1 } ( 1 , x , z , y ) , \quad Z = Q _ { 0 } ( 1 , x , z , y ) .
$$

$2 ^ { \circ }$ $F$ is a conic symplectic map if and only if $G$ is a positive product map, say $\gamma \otimes g$ , on ${ \bf R } _ { + } \times { \bf R } ^ { 2 n + 1 }$ with $g$ also a contact map on $\mathbf { R } ^ { 2 n + 1 }$ . Moreover, in this case, the multiplier of the contact map $g$ is just equal to $\gamma ^ { - 1 } = P _ { 0 } ^ { - 1 } ( 1 , x , z , y )$ .

Proof. The conclusion $1 ^ { \circ }$ is easily proved by some simple calculations. Below we devote to the proof of $2 ^ { \circ }$ . Let $F$ send $( p _ { 0 } , \dot { p _ { 1 } } , q _ { 0 } , q _ { 1 } ) \stackrel { . } {  } ( P _ { 0 } , P _ { 1 } , Q _ { 0 } , Q _ { 1 } )$ , $G$ send $( w , x , y , z ) \to ^ { \bullet } ( W , X , Y , Z )$ . Then by using the conclusion $1 ^ { \circ }$ , we have

$$
\begin{array} { r } { P _ { 0 } \circ S = w P _ { 0 } ( 1 , x , z , y ) = w \gamma , P _ { 1 } \circ S = w P _ { 1 } ( 1 , x , z , y ) = w \gamma X ( x , y , z ) , } \end{array}
$$

$$
S _ { * } = \left[ \begin{array} { l l l l } { 1 } & { 0 } & { 0 } & { 0 } \\ { x } & { w I _ { n } } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 1 } \\ { 0 } & { 0 } & { I _ { n } } & { 0 } \end{array} \right] , \quad G _ { * } = \frac { \partial \left( W , X , Y , Z \right) } { \partial \left( w , x , y , z \right) } = \left[ \begin{array} { l l l l } { \gamma } & { w \gamma _ { x } } & { w \gamma _ { y } } & { w \gamma _ { z } } \\ { 0 } & { } & { } & { } \\ { 0 } & { } & { g _ { * } } & { } \\ { 0 } & { } & { } & { } \end{array} \right] ,
$$

$$
S _ { * } \circ G = \left[ \begin{array} { c c c c } { { 1 } } & { { 0 } } & { { 0 } } & { { 0 } } \\ { { X } } & { { W I _ { n } } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { 1 } } \\ { { 0 } } & { { 0 } } & { { I _ { n } } } & { { 0 } } \end{array} \right] ,
$$

and compute

$$
\begin{array} { r l } & { \big ( ( ( 0 , 0 , P _ { 0 } ^ { \mathrm { T } } , P _ { 1 } ^ { \mathrm { T } } ) F _ { * } - ( 0 , 0 , p _ { 0 } ^ { \mathrm { T } } , p _ { 1 } ^ { \mathrm { T } } ) ) \circ S \big ) S _ { * } } \\ & { = \big ( ( 0 , 0 , P _ { 0 } ^ { \mathrm { T } } , P _ { 1 } ^ { \mathrm { T } } ) \circ S \big ) \big ( F _ { * } \circ S \big ) S _ { * } - \big ( ( 0 , 0 , p _ { 0 } ^ { \mathrm { T } } , p _ { 1 } ^ { \mathrm { T } } ) \circ S \big ) S _ { * } } \\ & { = ( 0 , 0 , w \gamma , w \gamma X ^ { \mathrm { T } } ) \big ( F _ { * } \circ S \big ) S _ { * } - ( 0 , 0 , w , w x ^ { \mathrm { T } } ) S _ { * } } \\ & { = ( 0 , 0 , w \gamma , w \gamma X ^ { \mathrm { T } } ) \big ( S _ { * } \circ G \big ) G _ { * } - ( 0 , 0 , w , w x ^ { \mathrm { T } } ) S _ { * } } \\ & { = w \gamma \big ( 0 , ( 0 , X ^ { \mathrm { T } } , 1 ) g _ { * } \big ) - w \gamma \big ( 0 , \gamma ^ { - 1 } ( 0 , x ^ { \mathrm { T } } , 1 ) \big ) . } \end{array}
$$

Noting that $S$ is a diffeomorphism, $S _ { * }$ is non-singular, $w > 0 , \gamma > 0$ , we obtain

$$
( 0 , 0 , P _ { 0 } ^ { \mathrm { T } } , P _ { 1 } ^ { \mathrm { T } } ) F _ { * } - ( 0 , 0 , p _ { 0 } ^ { \mathrm { T } } , p _ { 1 } ^ { \mathrm { T } } ) \equiv 0 \Longleftrightarrow ( 0 , X ^ { \mathrm { T } } , 1 ) g _ { * } - \gamma ^ { - 1 } ( 0 , x ^ { \mathrm { T } } , 1 ) \equiv 0 ,
$$

which proves the conclusion $2 ^ { \circ }$

Lemma 2.5 establishes correspondences between conic symplectic space and contact space and between conic symplectic maps and contact maps. We call the transform from $F$ to $G = S ^ { - 1 } \circ F \circ S = \gamma \otimes g$ contactization of conic symplectic maps, the call the transform transform from $G = \gamma \otimes g$ $S : \mathbf { R } _ { + } \times \mathbf { R } ^ { 2 n + 1 } \to \mathbf { R } _ { + } ^ { 2 n + 1 }$ to $F = S \circ G S ^ { - 1 }$ symplectization of contact space, and symplectization of contact maps and the transform $C = S ^ { - 1 } : { \bf R } _ { + } ^ { 2 n + 2 }  { \bf R } _ { + } \times { \bf R } ^ { 2 n + 1 }$ contactization of conic symplectic space.

# 11.3 Contact Generating Functions for Contact Maps

With the preliminaries of the last section, it is natural to derive contact generating function theory for contact maps from the well known symplectic analog[Fen93b,Fen95,Shu93] .

The following two lemmas can be proved easily[Fen95] .

Lemma 3.1. Hamiltonian $\phi : \mathbf { R } ^ { 2 n + 2 } \to \mathbf { R }$ is a conic function if only if the associated Hamiltonian vector field $a _ { \phi } = J \nabla \phi$ is conic, i.e., $a ( T _ { \lambda } z ) = T _ { \lambda } a ( z ) , \quad \lambda \ne 0 , \ z \in$ $\mathbf { R } ^ { 2 n + 2 }$ , where $J = \left[ { \begin{array} { c c } { O } & { - I _ { n + 1 } } \\ { I _ { n + 1 } } & { O } \end{array} } \right] .$ .

Lemma 3.2. Linear map ${ \left[ \begin{array} { l } { p } \\ { q } \end{array} \right] } \to C { \left[ \begin{array} { l } { p } \\ { q } \end{array} \right] }$ is a conic transformation on $\mathbf { R } ^ { 2 n + 2 }$ , i.e., $C \circ T _ { \lambda } \ : = \ : T _ { \lambda } \circ C .$ , if and only if the matrix $C$ has the diagonal form $C =$ $\left[ \begin{array} { c c } { { C _ { 0 } } } & { { O } } \\ { { O } } & { { C _ { 1 } } } \end{array} \right] w i t h \left( n + 1 \right) \times \left( n + 1 \right)$ matrix $C _ { 0 }$ and $C _ { 1 }$ .

Noting that the matrix in $g l ( 2 n + 2 )$

$$
C = \frac 1 2 ( I + J B ) , \quad B = B ^ { \mathrm { T } } \in S m ( 2 n + 2 ) ,
$$

establishes a 1-1 correspondence between near-zero Hamiltonian vector fields $z $ $\boldsymbol { a } ( \boldsymbol { z } ) \equiv J \nabla \phi ( \boldsymbol { z } )$ and near-identity symplectic maps $z \to g ( z )$ via generating relation

$$
g ( z ) - z = J \nabla \phi ( C g ( z ) + ( I - C ) z ) ,
$$

and combining Lemma 3.1 and Lemma 3.2, we find that matrix

$$
\begin{array} { r } { C = \left[ \begin{array} { c c } { C _ { 0 } } & { O } \\ { O } & { I - C _ { 0 } ^ { \mathrm { T } } } \end{array} \right] , \quad C _ { 0 } \in g l ( n + 1 ) , } \end{array}
$$

establishes a 1-1 correspondence between near-zero conic Hamiltonian vector fields $z  a ( z ) = J \nabla \phi ( z )$ and near-identity conic symplectic maps $z \to g ( z )$ via generating relation (3.3).

Write $\begin{array} { r } { C _ { 0 } = \left[ \begin{array} { l l } { \alpha } & { \beta ^ { \mathrm { T } } } \\ { \gamma } & { \delta } \end{array} \right] } \end{array}$ with $\alpha \in \textbf { R }$ , $\beta , \gamma \in \mathbf { \Gamma } ^ { \mathbf { R } ^ { n } }$ and $\delta \in g l ( n )$ . Then the generating relation (3.2) with generating matrix $C$ given by (3.3) can be expressed as

$$
\left\{ \begin{array} { l l } { \widehat { p } _ { 0 } - p _ { 0 } = - \phi _ { q _ { 0 } } ( \overline { { p } } , \overline { { q } } ) , } \\ { \widehat { p } _ { 1 } - p _ { 1 } = - \phi _ { q _ { 1 } } ( \overline { { p } } , \overline { { q } } ) , } \\ { \widehat { q } _ { 0 } - q _ { 0 } = \phi _ { q _ { 0 } } ( \overline { { p } } , \overline { { q } } ) , } \\ { \widehat { q } _ { 1 } - q _ { 1 } = \phi _ { q _ { 1 } } ( \overline { { p } } , \overline { { q } } ) , } \end{array} \right.
$$

where ${ \overline { { p } } } = { \left[ \begin{array} { l } { { \overline { { p } } } _ { 0 } } \\ { { \overline { { p } } } _ { 1 } } \end{array} \right] }$ and ${ \overline { { q } } } = { \left[ \begin{array} { l } { { \overline { { q } } } _ { 0 } } \\ { { \overline { { q } } } _ { 1 } } \end{array} \right] }$ are given by

$$
\left\{ \begin{array} { l l } { \overline { { p } } _ { 0 } = \alpha \widehat { p } _ { 0 } + ( 1 - \alpha ) p _ { 0 } + \beta ^ { \mathrm { T } } ( \widehat { p } _ { 1 } - p _ { 1 } ) , } \\ { \overline { { p } } _ { 1 } = \delta \widehat { p } _ { 1 } + ( I - \delta ) p _ { 1 } + \gamma ( \widehat { p } _ { 0 } - p _ { 0 } ) , } \\ { \overline { { q } } _ { 0 } = ( 1 - \alpha ) \widehat { q } _ { 0 } + \alpha q _ { 0 } - \gamma ^ { \mathrm { T } } ( \widehat { q } _ { 1 } - q _ { 1 } ) , } \\ { \overline { { q } } _ { 1 } = ( I - \delta ^ { \mathrm { T } } ) \widehat { q } _ { 1 } + \delta ^ { \mathrm { T } } q _ { 1 } - \beta ( \widehat { q } _ { 0 } - q _ { 0 } ) . } \end{array} \right.
$$

Every conic function $\phi$ can be contactized as an arbitrary function $\psi ( x , y , z )$ as follows

$$
\psi ( x , y , z ) = \phi ( 1 , x , z , y ) ,
$$

i.e.,

$$
\phi ( p _ { 0 } , p _ { 1 } , q _ { 0 } , q _ { 1 } ) = p _ { 0 } \phi ( 1 , p _ { 1 } / p _ { 0 } , q _ { 0 } , q _ { 1 } ) = p _ { 0 } \psi ( p _ { 1 } / p _ { 0 } , q _ { 1 } , q _ { 0 } ) , \quad p _ { 0 } \neq 0 ,
$$

and we have the partial derivative relation:

$$
\left\{ \begin{array} { l l } { \phi _ { q _ { 0 } } ( p _ { 0 } , p _ { 1 } , q _ { 0 } , q _ { 1 } ) = p _ { 0 } \psi _ { z } ( x , y , z ) , } \\ { \phi _ { q _ { 1 } } ( p _ { 0 } , p _ { 1 } , q _ { 0 } , q _ { 1 } ) = p _ { 0 } \psi _ { y } ( x , y , z ) , } \\ { \phi _ { p _ { 0 } } ( p _ { 0 } , p _ { 1 } , q _ { 0 } , q _ { 1 } ) = \psi ( x , y , z ) - x ^ { \mathrm { T } } \psi _ { x } ( x , y , z ) = \psi _ { e } ( x , y , z ) , } \\ { \phi _ { p _ { 1 } } ( p _ { 0 } , p _ { 1 } , q _ { 0 } , q _ { 1 } ) = \psi _ { x } ( x , y , z ) , } \end{array} \right.
$$

where $\begin{array} { r } { x \ = \ \frac { p _ { 1 } } { p _ { 0 } } } \end{array}$ $y \ = \ q _ { 1 }$ , $z ~ = ~ q _ { 0 }$ on the right hand side. So, under contactizing transforms

$$
\begin{array} { r } { S : \left[ \begin{array} { c c c c c c c c c c } { w } \\ { x } \\ { x } \\ { y } \\ { z } \\ { z } \end{array} \right] \longrightarrow \left[ \begin{array} { c c c c c c c c c } { p _ { 0 } } \\ { p _ { 1 } } \\ { p _ { 1 } } \\ { q _ { 0 } } \\ { q _ { 1 } } \end{array} \right] = \left[ \begin{array} { c c c c c c c c c } { w } \\ { w x } \\ { w x } \\ { z } \\ { z } \\ { y } \end{array} \right] , \left[ \begin{array} { c c c c c c c c } { \hat { w } } \\ { \hat { x } } \\ { \hat { x } } \\ { \hat { y } } \\ { \hat { z } } \end{array} \right] \longrightarrow \left[ \begin{array} { c c c c c c c c } { \hat { p } _ { 0 } } \\ { \hat { p } _ { 1 } } \\ { \hat { p } _ { 1 } } \\ { \hat { q } _ { 0 } } \\ { \hat { q } _ { 1 } } \end{array} \right] = \left[ \begin{array} { c c c c c c c c c } { \hat { w } } \\ { \hat { w } } \\ { \hat { w } \hat { x } } \\ { \hat { x } } \\ { \hat { z } } \\ { \hat { y } } \end{array} \right] , } \\ { \left[ \begin{array} { c c c c c c c c c } { \overline { { w } } } \\ { \overline { { x } } } \\ { \overline { { y } } } \\ { \overline { { z } } } \end{array} \right] \longrightarrow \left[ \begin{array} { c c c c c c c c c } { \overline { { p } } _ { 0 } } \\ { \overline { { p } } _ { 1 } } \\ { \overline { { q } } _ { 0 } } \\ { \overline { { q } } _ { 1 } } \end{array} \right] = \left[ \begin{array} { c c c c c c c c c } { \overline { { w } } } \\ { \overline { { w } } } \\ { \overline { { z } } } \\ { \overline { { y } } } \\ { \overline { { y } } } \end{array} \right] , } \end{array}
$$

the generating relation (3.4) turns into

$$
\left\{ \begin{array} { l l } { \widehat { w } - w = - \overline { { w } } \psi _ { z } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) , } \\ { \widehat { w } \widehat { x } - w x = - \overline { { w } } \psi _ { y } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) , } \\ { \widehat { z } - z = \psi _ { e } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) , } \\ { \widehat { y } - y = \psi _ { x } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) , } \end{array} \right.
$$

and Equation (3.5) turns into

$$
\left\{ \begin{array} { l l } { \overline { { w } } = \alpha \widehat { w } + ( 1 - \alpha ) w + \beta ^ { \mathrm { T } } ( \widehat { w } \widehat { x } - w x ) , } \\ { \overline { { w } } \overline { { x } } = \delta \widehat { w } \widehat { x } + ( I - \delta ) w x + \gamma ( \widehat { w } - w ) , } \\ { \overline { { z } } = ( 1 - \alpha ) \widehat { z } + \alpha z - \gamma ^ { \mathrm { T } } ( \widehat { y } - y ) , } \\ { \overline { { y } } = ( I - \delta ^ { \mathrm { T } } ) \widehat { y } + \delta ^ { \mathrm { T } } y - \beta ( \widehat { z } - z ) . } \end{array} \right.
$$

Since the $p _ { 0 }$ -axis is distinguished for the contactization in which we should always take $p _ { 0 } \neq 0$ , it is natural to require $\beta = 0$ in (3.5). Let $\widehat { \mu } = \frac { w } { \widehat { w } } = \frac { p _ { 0 } } { \widehat { p } _ { 0 } }$ and $\overline { { \mu } } = \frac { w } { \overline { { w } } } = \frac { \tilde { p _ { 0 } } } { \overline { { p } } _ { 0 } }$ , we obtain from Equations (3.9) and (3.10)

$$
\widehat { \mu } = \frac { 1 + \alpha \psi _ { z } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) } { 1 - ( 1 - \alpha ) \psi _ { z } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) } , \quad \overline { { \mu } } = 1 + \alpha \psi _ { z } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) ,
$$

and the induced contact transformation on the contact $( x , y , z )$ space $\mathbf { R } ^ { 2 n + 1 }$ is

$$
\left\{ \begin{array} { l l } { \widehat { x } - x = - \psi _ { y } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) + \psi _ { z } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) \big ( ( 1 - \alpha ) \widehat { x } + \alpha x \big ) , } \\ { } \\ { \widehat { y } - y = \psi _ { x } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) , } \\ { } \\ { \widehat { z } - z = \psi _ { e } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) , } \end{array} \right.
$$

with the bar variables on the right hand side given by $\overline { { x } } , \overline { { y } } , \overline { { z } }$

$$
\left\{ \begin{array} { l } { \overline { { x } } = d _ { 1 } \widehat { x } + d _ { 2 } x + d _ { 0 } , } \\ { \overline { { y } } = ( I - \delta ^ { \mathrm { T } } ) \widehat { y } + \delta ^ { \mathrm { T } } y , } \\ { \overline { { z } } = ( 1 - \alpha ) \widehat { z } + \alpha z - \gamma ^ { \mathrm { T } } ( \widehat { y } - y ) , } \end{array} \right.
$$

where

$$
\left\{ \begin{array} { l l } { d _ { 1 } = \big ( I - ( 1 - \alpha ) \psi _ { z } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) \big ) \delta , } \\ { d _ { 2 } = \Big ( I + \alpha \psi _ { z } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) \big ) ( I - \delta ) , } \\ { d _ { 0 } = - \psi _ { z } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) \gamma . } \end{array} \right.
$$

Summarizing the above discussions, we have:

Theorem 3.3. Relations (3.12) – (3.14) give a contact map $( x , y , z ) \to ( { \widehat { x } } , { \widehat { y } } , { \widehat { z } } )$ via contact generating function $\psi ( x , y , z )$ under the type $C _ { 0 } = \left[ \begin{array} { l l } { \alpha } & { O } \\ { \gamma } & { \delta } \end{array} \right]$   . Vice versa.

However, the difficulty in the algorithmic implementation lies in the fact that, unlike $\bar { y }$ and $\overline { z }$ , which are linear combinations of ${ \widehat { y } } , y$ and ${ \widehat { z } } , z$ with constant matrix coefficients, since $\overline { { x } } = d _ { 1 } \widehat { x } + d _ { 2 } x + d _ { 0 }$ and $d _ { 1 } , d _ { 2 }$  are matrices with coefficients depending on $\bar { \psi } _ { z } = \psi _ { z } ( \overline { { x } } , \overline { { y } } , \overline { { z } } )$ which in turn depends on $( { \overline { { x } } } , { \overline { { y } } } , { \overline { { z } } } )$ the combination of $\textstyle { \overline { { x } } }$ from $\widehat { x }$ and $x$ is not explicitly given, the entire equations for solving $\widehat { x } , \widehat { y } , \widehat { z }$ in terms of $x , y , z$ are highly implicit. The exceptional cases are the following:

(E1) $\alpha = 0 , \ \delta = O _ { n } , \ \gamma = O ($ ,

$$
\begin{array} { c } { \widehat { \mu } = 1 - \psi _ { z } ( x , \widehat { y } , \widehat { z } ) , \quad \overline { { \mu } } = 1 , } \\ { \left\{ \begin{array} { l l } { \widehat { x } - x = - \psi _ { y } ( x , \widehat { y } , \widehat { z } ) + \widehat { x } \psi _ { z } ( x , \widehat { y } , \widehat { z } ) , } \\ { \widehat { y } - y = \psi _ { x } ( x , \widehat { y } , \widehat { z } ) , } \\ { \widehat { z } - z = \psi _ { e } ( x , \widehat { y } , \widehat { z } ) = \psi ( x , \widehat { y } , \widehat { z } ) - x ^ { \mathrm { T } } \psi _ { x } ( x , \widehat { y } , \widehat { z } ) . } \end{array} \right. } \end{array}
$$

(E2) α = 1, δ = In, γ = O,

$$
\begin{array} { c } { \widehat { \mu } = \overline { { \mu } } = 1 + \psi _ { z } ( \widehat { x } , y , z ) , } \\ { \left\{ \widehat { x } - x = - \psi _ { y } ( \widehat { x } , y , z ) + x \psi _ { z } ( \widehat { x } , y , z ) , \right. } \\ { \left. \widehat { y } - y = \psi _ { x } ( \widehat { x } , y , z ) , \right. } \\ { \left. \widehat { z } - z = \psi _ { e } ( \widehat { x } , y , z ) = \psi ( \widehat { x } , y , z ) - x ^ { \mathrm { T } } \psi _ { x } ( \widehat { x } , y , z ) . \right. } \end{array}
$$

$\alpha = \frac { 1 } { 2 } , \thinspace \thinspace \thinspace \delta = \frac { 1 } { 2 } I _ { n } , \thinspace \thinspace \gamma = O ,$

$$
\begin{array} { c } { { \displaystyle \widehat { \mu } = \frac { 1 + \frac { 1 } { 2 } \psi _ { z } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) } { 1 - \frac { 1 } { 2 } \psi _ { z } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) } , \quad \overline { { \mu } } = 1 + \frac { 1 } { 2 } \psi _ { z } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) , } } \\ { { \displaystyle } } \\ { { \left\{ \begin{array} { l } { { \hat { x } - x = - \psi _ { y } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) + \psi _ { z } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) \frac { \hat { x } + x } { 2 } , } } \\ { { \hat { y } - y = \psi _ { x } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) , } } \\ { { \hat { z } - z = \psi _ { e } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) = \psi ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) - \overline { { x } } ^ { \mathrm { T } } \psi _ { x } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) , } } \end{array} \right. } } \end{array}
$$

with

$$
\overline { { x } } = \frac { \widehat { x } + x } { 2 } - \frac { 1 } { 4 } \psi _ { z } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) ( \widehat { x } - x ) , \overline { { y } } = \frac { \widehat { y } + y } { 2 } , \overline { { z } } = \frac { \widehat { z } + z } { 2 } .
$$

For $\psi _ { z } = \lambda =$ constant, the case (E3) reduces to

$$
\begin{array} { l } { \displaystyle { \widehat { \mu } = \frac { 1 + \frac { 1 } { 2 } \lambda } { 1 - \frac { 1 } { 2 } \lambda } , \quad \overline { { \mu } } = 1 + \frac { 1 } { 2 } \lambda , } } \\ { \displaystyle { \left\{ \begin{array} { l l } { \displaystyle { \widehat { x } - x = - \psi _ { y } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) + \psi _ { z } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) \frac { \widehat { x } + x } { 2 } , } } \\ { \displaystyle { \widehat { y } - y = \psi _ { x } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) , } } \\ { \displaystyle { \widehat { z } - z = \psi _ { e } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) = \psi ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) - \overline { { x } } ^ { \mathrm { T } } \psi _ { x } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) , } } \end{array} \right. } } \end{array}
$$

with

$$
\overline { { x } } = \frac { \widehat { x } + x } { 2 } - \frac { 1 } { 4 } \lambda ( \widehat { x } - x ) , \quad \overline { { y } } = \frac { \widehat { y } + y } { 2 } , \quad \overline { { z } } = \frac { \widehat { z } + z } { 2 } .
$$

Note that the symplectic map induced by generating function $\phi$ from the relation (3.2) can be represented as the composition of the maps, non-symplectic generally, $z  { \overline { { z } } }$ and $\overline { { z } }  \widehat { z }$

$$
\begin{array} { l } { { \overline { { z } } = z + C J \nabla \phi ( \overline { { z } } ) , } } \\ { { \overline { { z } } = z + ( I - C ) J \nabla \phi ( \overline { { z } } ) . } } \end{array}
$$

Theorem 3.4. Contact map $( x , y , z ) \to ( { \widehat { x } } , { \widehat { y } } , { \widehat { z } } )$ induced by contact generating function $\psi$   from the relations (3.12)–(3.14) can be represented as the composition of the maps $( x , y , z ) \to ( { \overline { { x } } } , { \overline { { y } } } , { \overline { { z } } } )$ and $( \overline { { x } } , \overline { { y } } , \overline { { z } } )  ( \widehat { x } , \widehat { y } , \widehat { z } )$ which are not contact generally and given, respectively, as follows

$$
\left\{ \begin{array} { l l } { \overline { { x } } - x = - \delta \psi _ { y } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) + \alpha \psi _ { z } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) x - \gamma \psi _ { z } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) , } \\ { \overline { { y } } - y = ( I - \delta ^ { \mathrm { T } } ) \psi _ { x } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) , } \\ { \overline { { z } } - z = ( 1 - \alpha ) \psi _ { e } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) - \gamma ^ { \mathrm { T } } \psi _ { x } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) } \end{array} \right.
$$

and

$$
\left\{ \begin{array} { l l } { \widehat { x } - \overline { { x } } = - ( I - \delta ) \psi _ { y } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) + ( 1 - \alpha ) \psi _ { z } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) \widehat { x } + \gamma \psi _ { z } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) , } \\ { \widehat { y } - \overline { { y } } = \delta ^ { \mathrm { T } } \psi _ { x } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) , } \\ { \widehat { z } - \overline { { z } } = \alpha \psi _ { e } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) + \gamma ^ { \mathrm { T } } \psi _ { x } ( \overline { { x } } , \overline { { y } } , \overline { { z } } ) . } \end{array} \right.
$$

(3.25) and (3.26) are the 2-stage form of the generating relation (3.12) of the contact map induced by generating function $\psi$ under the type $C _ { 0 } = { \left[ \begin{array} { l l } { \alpha } & { O } \\ { \gamma } & { \delta } \end{array} \right] }$ . Corresponding to the exceptional cases (E1), (E2) and (E3), the above 2-stage representation has simpler forms, we no longer use them here.

# 11.4 Contact Algorithms for Contact Systems

Consider contact system (1.3) with the vector field $a$ defined by contact Hamiltonian $K$ according to Equation (1.6). Take $\psi ( x , y , z ) = s K ( x , y , z )$ in $( 3 . 1 2 ) - ( 3 . 1 4 )$ as the generating function, we then obtain contact difference schemes with 1st order of accuracy of the contact system (1.3) associated with all possible types $C _ { 0 } = { \left[ \begin{array} { l l } { \alpha } & { O } \\ { \gamma } & { \delta } \end{array} \right] }$ The simplest and important cases are (write $\overline { { K } } _ { x } = K _ { x } ( \overline { { x } } , \overline { { y } } , \overline { { z } } )$ , etc.) as follows[Fen95] .

# 11.4.1 $\overline { { Q } }$ Contact Algorithm

$\overline { { Q } }$ . Contact analog of symplectic method $( p , Q ) ^ { 1 } \ ( \alpha = 0 , \delta = 0 _ { n } , \gamma = 0 )$ .

2-stage form :

1-stage form : $\begin{array} { l } { \widehat { x } = x + s \big ( - K _ { y } ( x , \widehat { y } , \widehat { z } ) + \widehat { x } K _ { z } ( x , \widehat { y } , \widehat { z } ) \big ) , } \\ { \widehat { y } = y + s K _ { x } ( x , \widehat { y } , \widehat { z } ) , } \\ { \widehat { z } = z + s K _ { e } ( x , \widehat { y } , \widehat { z } ) ; } \\ { \overline { { x } } = x , \quad \overline { { y } } = y + s \overline { { K } } _ { x } , \quad \overline { { z } } = z + s \overline { { K } } _ { e } , } \\ { \widehat { x } = \overline { { x } } + s ( - \overline { { K } } _ { y } + \widehat { x } \overline { { K } } _ { x } ) , \quad \widehat { y } = \overline { { y } } , \quad \widehat { z } = \overline { { z } } . } \end{array}$

# 11.4.2 $\overline { { P } }$ Contact Algorithm

$\overline { { P } }$ . Contact analog of symplectic method $( P , q ) ( \alpha = 1 , \delta = I _ { n } , \gamma = O )$ .

1-stage form: $\begin{array} { r l } & { \hat { x } = x + s \big ( - K _ { y } ( \hat { x } , y , z ) + x K _ { z } ( \hat { x } , y , z ) \big ) , } \\ & { \hat { y } = y + s K _ { x } ( \hat { x } , y , z ) , } \\ & { \hat { z } = z + s K _ { e } ( \hat { x } , y , z ) ; } \\ & { \overline { { x } } = x + s ( - \overline { { K } } _ { y } + x \overline { { K } } _ { z } ) , \quad \overline { { y } } = y , \quad \overline { { z } } = z , } \\ & { \hat { x } = \overline { { x } } , \quad \hat { y } = \overline { { y } } + s \overline { { K } } _ { x } , \quad \hat { z } = \overline { { z } } + s \overline { { K } } _ { e } . } \end{array}$   
2-stage form:

# 11.4.3 $\overline { { C } }$ Contact Algorithm

case $\overline { { C } }$ . Contact version of Poincare generating function method similarly to symplectic ´ $\left( \alpha = \frac { 1 } { 2 } , \delta = \frac { 1 } { 2 } I _ { n } , \gamma = O \right)$ .

2-stage form:

$$
\begin{array} { r l } & { \overline { { x } } = x + \frac { s } { 2 } ( - \overline { { K } } _ { y } + x \overline { { K } } _ { z } ) , \quad \overline { { y } } = y + \frac { s } { 2 } \overline { { K } } _ { z } , \quad \overline { { z } } = z + \frac { s } { 2 } \overline { { K } } _ { e } , } \\ & { \widehat { x } = \overline { { x } } + \frac { s } { 2 } ( - \overline { { K } } _ { y } + \widehat x \overline { { K } } _ { x } ) = \left( \overline { { x } } - \frac { s } { 2 } \overline { { K } } _ { y } \right) \left( 1 - \frac { s } { 2 } \overline { { K } } _ { z } \right) ^ { - 1 } , } \\ & { \widehat { y } = \overline { { y } } + \frac { s } { 2 } \overline { { K } } _ { x } = 2 \overline { { y } } - y , \quad \widehat { z } = \overline { { z } } + \frac { s } { 2 } \overline { { K } } _ { e } = 2 \overline { { z } } - z . } \end{array}
$$

One might suggest, for example, the following scheme for (1.3):

$$
\widehat { x } = x + s a ( \widehat { x } , y , z ) , ~ \widehat { y } = y + s b ( \widehat { x } , y , z ) , ~ \widehat { z } = z + s c ( \widehat { x } , y , z ) .
$$

It differs from (4.2) only in one term for $\widehat { x }$ , i.e., $\widehat { x } K ( \widehat { x } , y , z )$ instead of $x K ( \widehat { x } , y , z )$    This minute, but delicate, difference makes (4.2) contact and the other non-contact!

It should be noted that the $\overline { { Q } }$ and $\overline { { P } }$ methods are of order one of accuracy and the $\overline { { C } }$ method is of order two. The proof is similar to that for symplectic case. In principle, one can construct the contact difference schemes of arbitrarily high order of accuracy for contact systems, as was done for Hamiltonian systems, by suitably composing the $\overline { { Q } } , \overline { { P } }$ or $\overline { { C } }$ method and the respective reversible counterpart[QZ92] . Another general method for the construction of contact difference schemes is based on the generating functions for phase flows of contact systems which will be developed in the next section.

# 11.5 Hamilton–Jacobi Equations for Contact Systems

We recall that a near identity contact map $g \ : \ ( x , y , z ) \ \to \ ( { \widehat { x } } , { \widehat { y } } , { \widehat { z } } )$ can be generated from the so-called generating function $\psi ( x , y , z )$   , associated with a matrix $C _ { 0 } = { \left[ \begin{array} { l l } { \alpha } & { O } \\ { \gamma } & { \delta } \end{array} \right] }$ , by the relations (3.12) – (3.14). Accordingly, to the phase flow $e _ { K } ^ { t }$ of a contact system with contact Hamiltonian $K$ , there corresponds a time-dependent generating function $\psi ^ { t } ( x , y , z )$ such that the map $e _ { K } ^ { t } : ( x , y , z ) \to ( \widehat { x } , \widehat { y } , \widehat { z } )$ is generated from $\psi ^ { t }$ by the relations $( 3 . 1 2 ) - ( 3 . 1 4 )$ , in which $\psi$  is replaced by $\psi ^ { t }$ and $C _ { 0 }$ is given in advance as above. The function $\psi ^ { t }$ should be determined by $K$ and $C _ { 0 }$ . Below we derive the relevant relations between them.

Let $H ( p _ { 0 } , p _ { 1 } , q _ { 0 } , q _ { 1 } ) = p _ { 0 } K \big ( \frac { p _ { 1 } } { p _ { 0 } } , q _ { 1 } , q _ { 0 } \big )$ , $p _ { 0 } \neq 0$ . With this conic Hamiltonian and with normal Darboux matrices $C = \left[ \begin{array} { c c } { C _ { 0 } } & { O } \\ { O } & { I - C _ { 0 } } \end{array} \right]$ , where ${ \cal C } _ { 0 } = \left[ \begin{array} { c c } { { \alpha } } & { { { \cal O } } } \\ { { \gamma } } & { { \delta } } \end{array} \right] ,$

$$
\frac { \partial } { \partial t } \phi ^ { t } ( u ) = H \big ( u + ( I - C ) J \nabla \phi ^ { t } ( u ) \big ) , \quad \mathrm { w i t h } \quad u = ( p _ { 0 } , p _ { 1 } , q _ { 0 } , q _ { 1 } ) ^ { \mathrm { T } } ,
$$

satisfied by the generating function $\phi ^ { t } ( u )$ of the phase flow $g _ { H } ^ { t }$ of the Hamiltonian system associated with the Hamiltonian $H$ while the phase flow $g _ { H } ^ { t }$ is generated from $\phi ^ { t }$ by the relation

$$
g _ { H } ^ { t } ( u ) - u = J \phi ^ { t } \bigl ( C g _ { H } ^ { t } ( u ) + ( I - C ) u \bigr ) .
$$

On the other hand, according to the discussion in Section 11.3, we have

$$
\phi ^ { t } ( p _ { 0 } , p _ { 1 } , q _ { 0 } , q _ { 1 } ) = p _ { 0 } \psi ^ { t } ( x , y , z ) , \quad \mathrm { w i t h } \quad x = \frac { p _ { 1 } } { p _ { 0 } } , \quad y = q _ { 1 } , \quad z = q _ { 0 } .
$$

So, by simple calculations, we have

$$
\begin{array} { r } { u + ( I - C ) J \nabla \phi ^ { t } ( u ) = \left[ \begin{array} { c } { p _ { 0 } - ( 1 - \alpha ) \phi _ { q _ { 0 } } } \\ { p _ { 1 } + \gamma \phi _ { q _ { 0 } } - ( I - \delta ) \phi _ { q _ { 1 } } } \\ { q _ { 0 } + \alpha \phi _ { p _ { 0 } } + \gamma ^ { \operatorname { T } } \phi _ { p _ { 1 } } } \\ { q _ { 1 } + \delta ^ { \operatorname { T } } \phi _ { p _ { 1 } } } \end{array} \right] = \left[ \begin{array} { c } { p _ { 0 } ( 1 - ( 1 - \alpha ) \psi _ { z } ) } \\ { p _ { 0 } ( x + \gamma \psi _ { z } - ( I - \delta ) \psi _ { y } ) } \\ { z + \alpha \psi _ { e } + \gamma ^ { \operatorname { T } } \psi _ { x } } \\ { y + \delta ^ { \operatorname { T } } \psi _ { x } } \end{array} \right] } \end{array}
$$

and

$$
\begin{array} { r l } & { H ( u + ( I - C ) J \nabla \phi ^ { t } ( u ) ) } \\ & { = p _ { 0 } \big ( 1 - ( 1 - \alpha ) \psi _ { z } \big ) K \left( \frac { x - ( I - \delta ) \psi _ { y } + \gamma \psi _ { z } } { 1 - ( 1 - \alpha ) \psi _ { z } } , y + \delta ^ { \mathrm { T } } \psi _ { x } , z + \alpha \psi _ { e } + \gamma ^ { \mathrm { T } } \psi _ { x } \right) . } \end{array}
$$

Therefore, from Equation (5.1), $\psi ^ { t } ( x , y , z )$ satisfies

$$
\frac { \partial } { \partial t } \psi ^ { t } = \left( 1 - ( 1 - \alpha ) \psi _ { z } \right) K \left( \frac { x - ( I - \delta ) \psi _ { y } + \gamma \psi _ { z } } { 1 - ( 1 - \alpha ) \psi _ { z } } , y + \delta ^ { \mathrm { T } } \psi _ { x } , z + \alpha \psi _ { e } + \gamma ^ { \mathrm { T } } \psi _ { x } \right) .
$$

Now we claim1. From (5.2), it follows that $\widehat { u } = g _ { H } ^ { t } ( \bar { u } )$ . The claim is then proved, since ${ \cal H } ( g _ { H } ^ { t } ( \bar { u } ) ) = { \cal H } ( \bar { u } )$ , for all $u$ . The following equality is valid

$$
H { \big ( } u + ( I - C ) J \nabla \phi ^ { t } ( u ) { \big ) } = H { \big ( } u - C J \nabla \phi ^ { t } ( u ) { \big ) } .
$$

So, replacing $C$ by $C - I$ in above discussions or, equivalently, replacing $\alpha$ and $\delta$ by $\alpha - 1$ and $\delta - 1$ with $\gamma$ unchanging in (5.3), we can derive equation satisfied by the $\psi ^ { t }$

$$
\frac { \partial } { \partial t } \psi ^ { t } = ( 1 + \alpha \psi _ { z } ) K \left( \frac { x + \delta \psi _ { y } + \gamma \psi _ { z } } { 1 + \alpha \psi _ { z } } , y + ( \delta ^ { \mathrm { T } } - I ) \psi _ { x } , z + ( \alpha - 1 ) \psi _ { e } + \gamma ^ { \mathrm { T } } \psi _ { x } \right) .
$$

(5.3) and (5.5) define the same function $\psi ^ { t }$ . When $t = 0 , e _ { K } ^ { t } = I$ , so we should impose the initial condition

$$
\psi ^ { 0 } ( x , y , z ) = 0 ,
$$

for solving the first order partial differential equation (5.3) or (5.5). We call both equations the Hamilton–Jacobi equations of the contact system associated with the contact Hamiltonian $K$ and the matrix $C _ { 0 } = { \left[ \begin{array} { l l } { \alpha } & { O } \\ { \gamma } & { \delta } \end{array} \right] }$

Specifically, we have Hamilton–Jacobi equations for particular cases:

(E1) $\alpha = 0 , \delta = O , \gamma = O$

$$
\frac { \partial } { \partial t } \psi ^ { t } = ( 1 - \psi _ { z } ^ { t } ) K \left( \frac { x - \psi _ { y } ^ { t } } { 1 - \psi _ { z } ^ { t } } , y , z \right) = K ( x , y - \psi _ { x } ^ { t } , z - \psi _ { e } ^ { t } ) .
$$

(E2) $\alpha = 1 , \delta = I _ { n } , \gamma = O .$

$$
\frac { \partial } { \partial { t } } \psi ^ { t } = K ( x , y + \psi _ { x } ^ { t } , z + \psi _ { e } ^ { t } ) = ( 1 + \psi _ { z } ^ { t } ) K \left( \frac { x + \psi _ { y } ^ { t } } { 1 + \psi _ { z } ^ { t } } , y , z \right) .
$$

(E3) α = 12 , δ = 12 In, γ = O.

$$
\begin{array} { r c l } { { \displaystyle { \frac { \partial } { \partial t } } \psi ^ { t } ~ = ~ \left( 1 - \frac { 1 } { 2 } \psi _ { z } ^ { t } \right) K \left( \frac { x - \displaystyle { \frac { 1 } { 2 } } \psi _ { y } ^ { t } } { 1 - \displaystyle { \frac { 1 } { 2 } } \psi _ { z } ^ { t } } , y + \displaystyle { \frac { 1 } { 2 } } \psi _ { x } ^ { t } , z + \displaystyle { \frac { 1 } { 2 } } \psi _ { e } ^ { t } \right) } } \\ { { ~ } } & { { ~ } } & { { ~ } } \\ { { ~ = ~ \left( 1 + \displaystyle { \frac { 1 } { 2 } } \psi _ { z } ^ { t } \right) K \left( \frac { x + \displaystyle { \frac { 1 } { 2 } } \psi _ { y } ^ { t } } { 1 + \displaystyle { \frac { 1 } { 2 } } \psi _ { z } ^ { t } } , y - \displaystyle { \frac { 1 } { 2 } } \psi _ { x } ^ { t } , z - \displaystyle { \frac { 1 } { 2 } } \psi _ { e } ^ { t } \right) . } } \end{array}
$$

Remark 5.1. On the construction of high order contact difference schemes.

If $K$ is analytic, then one can solve $\psi ^ { t } ( x , y , z )$ from the above Hamilton–Jacobi equations in the forms of power series in time $t$ . Its coefficients are recursively determined by the $K$ and the related matrix $C _ { 0 }$ . The power series are simply given from the corresponding conic Hamiltonian generating functions $\phi ^ { t } ( p _ { 0 } , p _ { 1 } , q _ { 0 } , q _ { 1 } )$ by $\psi ^ { t } ( x , y , z ) = \psi ^ { t } ( 1 , x , z , y )$ , since the power series expressions of $\phi ^ { t }$ with respect to $t$ from the conic Hamiltonian $H ( p _ { 0 } , p _ { 1 } , q _ { 0 } , q _ { 1 } ) = p _ { 0 } K \Big ( \frac { p _ { 1 } } { p _ { 0 } } , q _ { 1 } , q _ { 0 } \Big )$ have been well given $\mathrm { i n } ^ { [ \mathrm { F W 9 4 } ] }$ . Taking a finite truncation of the power series up to order $m$ , an arbitrary integer, with respect to the time $t$ and replacing by the truncation the generating function $\psi$ in (3.12)–(3.14), then one obtains a contact difference scheme of order $m$ for the contact system defined by the contact Hamiltonian $K$ . The proofs of these assertions are similar to those in the Hamiltonian system case, hence are omitted here.

# Bibliography

[Arn78] V. I. Arnold: Ordinary Differential Equations. The MIT Press, New York, (1978).   
[Arn88] V. I. Arnold: Geometrical Methods In The Theory of Ordinary Differential Equations. Springer-Verlag, Berlin, (1988).   
[Arn89] V. I. Arnold: Mathematical Methods of Classical Mechanics. Springer-Verlag, GTM 60, Berlin Heidelberg, Second edition, (1989).   
[Etn03] J. Etnyre: Introductory lectures on contact geometry. In Proc. Sympos. Pure Math, volume 71, page 81C107. SG/0111118, (2003).   
[Fen93b] K. Feng: Symplectic, contact and volume preserving algorithms. In Z.C. Shi and T. Ushijima, editors, Proc.1st China-Japan conf. on computation of differential equationsand dynamical systems, pages 1–28. World Scientific, Singapore, (1993).   
[Fen95] K. Feng: Collected works of Feng Kang. volume I,II. National Defence Industry Press, Beijing, (1995).   
[FW94] K. Feng and D.L. Wang: Dynamical systems and geometric construction of algorithms. In Z. C. Shi and C. C. Yang, editors, Computational Mathematics in China, Contemporary Mathematics of AMS, Vol 163, pages 1–32. AMS, (1994).   
[Gei03] H. Geiges: Contact geometry. Math.SG/0307242, (2003).   
[MNSS91] R. Mrugała, J.D. Nulton, J.C. Schon, and P. Salamon: Contact structure in thermodynamic theory. Reports on Mathematical Physics, 29:109C121, (1991).   
[QZ92] M. Z. Qin and W. J. Zhu: Construction of higher order symplectic schemes by composition. Computing, 47:309–321, (1992).   
[Shu93] H.B. Shu: A new approach to generating functions for contact systems. Computers Math. Applic., 25:101–106, (1993).

# Chapter 12. Poisson Bracket and Lie–Poisson Schemes

In this chapter, a clear Lie–Poisson Hamilton–Jacobi theory is presented. It is also shown how to construct a Lie–Poisson scheme integrator by generating function, which is different from the Ge–Marsden[GM88] method.

# 12.1 Poisson Bracket and Lie–Poisson Systems

Before introducing the Lie–Poisson system, let us first review more general about the Poisson system.

# 12.1.1 Poisson Bracket

Take a system with finite dimensions as an example. Give a manifold $M$ and two smooth functions $F , G$ on $M$ , i.e., $F , G \in C ^ { \infty } ( M )$ . If an operation $\{ \cdot , \cdot \}$ defined on $C ^ { \infty } ( M )$ satisfies the following 4 properties, then $\{ \cdot , \cdot \}$ is called Poisson bracket, and $( M , \{ \cdot , \cdot \} )$ is called Poisson manifold $\left[ \mathrm { O l v } 9 3 \right]$ .

# 1. Bilinearity

$$
\begin{array} { r } { \{ a F _ { 1 } + b F _ { 2 } , H \} = a \{ F _ { 1 } , H \} + b \{ F _ { 2 } , H \} , } \\ { \{ } \\ { F , a H _ { 1 } + b H _ { 2 } \} = a \{ F , H _ { 1 } \} + b \{ F , H _ { 2 } \} . } \end{array}
$$

2. Skew-Symmetry

$$
\{ F , H \} = - \{ H , F \} .
$$

3. Jacobi Identity

$$
\{ \{ F , H \} , G \} + \{ \{ H , G \} , F \} + \{ \{ G , F \} , H \} = 0 .
$$

# 4. Leibniz Rule

$$
\{ F _ { 1 } \cdot F _ { 2 } , H \} = F _ { 1 } \{ F _ { 2 } , H \} + F _ { 2 } \{ F _ { 1 } , H \} .
$$

Given a Hamiltonian function $H \in C ^ { \infty } ( M )$ , the induced equation

$$
\dot { F } = \{ F , H \} , \quad \forall F \in C ^ { \infty } ( M )
$$

is called the generalized Hamiltonian equation. The most general case of Hamiltonian system is the one with symplectic structure, whose equations have the form:

$$
{ \dot { z } } = J H _ { z } , \quad J = { \left[ \begin{array} { l l } { O } & { I } \\ { I } & { O } \end{array} \right] } , \quad z = { \left[ \begin{array} { l } { p } \\ { q } \end{array} \right] } .
$$

According to Darboux theorem, a general Poisson system with finite dimensions can be transformed into a local coordinate form, whose equations may be written as

$$
\begin{array} { r } { \dot { z } = K ( z ) H _ { z } , } \end{array}
$$

the corresponding Poisson bracket is

$$
\{ F , H \} = ( \nabla _ { z } F ( z ) ) ^ { \mathrm { T } } K ( z ) \nabla _ { z } H ( z ) , \quad \forall F , H \in C ^ { \infty } ( M ) .
$$

$K ( z )$ satisfies 4 properties the above , if and only if $K ( z ) = ( k _ { i j } ( z ) )$ satisfies

$$
k _ { i j } ( z ) \frac { \partial k _ { l m } ( z ) } { \partial z _ { i } } + k _ { i l } ( z ) \frac { \partial k _ { m j } } { \partial z _ { i } } + k _ { i m } ( z ) \frac { \partial k _ { j l } } { \partial z _ { i } } = 0 , \quad j , l , m = 1 , 2 , \cdot \cdot , n .
$$

We remark that any antisymmetry constant matrix satisfies (1.2) and hence is a Hamiltonian operator, and the bracket defined by it is a Poisson bracket. We will discuss its algorithm in more detail in the next section.

Definition 1.1. A diffeomorphism $z  { \widehat { z } } = g ( z ) : M  M$ is called a Poisson mapping, if it preserves the Poisson bracket, i.e.,

$$
\{ F \circ g , H \circ g \} = \{ F , H \} \circ g , \quad \forall F , H \in C ^ { \infty } ( M ) .
$$

Theorem 1.2. For a Poisson manifold with structure matrix $K ( z )$ , Equation (1.3) is equivalent to

$$
g _ { z } K ( z ) g _ { z } ^ { \mathrm { T } } = K ( \widehat { z } ) ,
$$

where $g _ { z }$ is the Jacobian matrix of $g$ with respect to $z$ .

Proof.

$$
\begin{array} { l } { \{ F \circ g , H \circ g \} } \\ { = \ ( F \circ g ) _ { z } K ( z ) ( H \circ g ) _ { z } ^ { \mathrm { T } } } \\ { = \ F _ { z } ( g ( z ) ) \frac { \partial g } { \partial z } K ( z ) \left( \frac { \partial g } { \partial z } \right) ^ { \mathrm { T } } \left( H _ { z } ( g ( z ) \right) ^ { \mathrm { T } } } \\ { = \ F _ { z } ( g ( z ) ) \frac { \partial \mathbf { \Psi } } { \partial z } K ( z ) \left( \frac { \partial g } { \partial z } \right) ^ { \mathrm { T } } \left( \nabla H \circ g \right) , } \end{array}
$$

and

$$
\{ F , H \} \circ g = \nabla F ^ { \mathrm { T } } K \nabla H ( g ( z ) ) = ( \nabla F \circ g ) ^ { \mathrm { T } } K ( g ( z ) ) ( \nabla H \circ g ) .
$$

By comparison, we get

$$
g _ { z } ( z ) K ( z ) ( g _ { z } ( z ) ) ^ { \mathrm { T } } = K ( g ( z ) ) = K ( \widehat { z } ) .
$$

The theorem is proved.

A Hamiltonian system on a Poisson manifold usually refers to the following ODEs

$$
\frac { \mathrm { d } \boldsymbol { z } } { \mathrm { d } t } = \boldsymbol { K } ( \boldsymbol { z } ) \nabla \boldsymbol { H } ( \boldsymbol { z } ) ,
$$

where $H ( z )$ is a Hamiltonian function.

The phase flow of the Equation (1.4), which is expressed as $g ^ { t } ( z ) = g ( t , z ) =$ $g _ { H } ( t , z )$ , is a one parameter diffeomorphism group (at least locally), i.e.,

$$
g ^ { 0 } = \mathrm { i d e n t i t y } , \quad g ^ { t _ { 1 } + t _ { 2 } } = g ^ { t _ { 1 } } \circ g ^ { t _ { 2 } } .
$$

Theorem 1.3. The phase flow $g _ { H } ( z , t )$ of the Hamiltonian system (1.4) is a one parameter group of Poisson maps, i.e.,

$$
\{ F \circ g ( z , t ) , G \circ g ( z , t ) \} = \{ F , G \} \circ g ( z , t ) .
$$

Proof. $\mathrm { S e e } ^ { \mathrm { [ O l v 9 3 ] } }$ .

By Theorem 1.2, we get

$$
g _ { z } ( z , t ) K ( z ) ( g _ { z } ( z , t ) ) ^ { \mathrm { T } } = K ( g ( z ) ) .
$$

Definition 1.4. A smooth function $C ( z )$ is called a Casimir function, if

$$
\{ C ( z ) , F ( z ) \} = 0 , \quad \forall F \in C ^ { \infty } ( M ) .
$$

Definition 1.5. $F ( z ) \in C ^ { \infty } ( M )$ is a first integral of Hamiltonian system, iff $\{ F , H \} =$ 0. Obviously, every Casimir function is a first integral.

# 12.1.2 Lie–Poisson Systems

The Lie–Poisson system is a $\mathrm { t y p e ^ { [ M W 8 3 , M R 9 9 ] } }$ of common Poisson systems. Its structure space is the dual space of any Lie algebra, and its bracket is called Lie–Poisson bracket. There are two types of definition for the Lie–Poisson bracket: one relies on the coordinate definition, and the other does not rely on the coordinate definition.

Lie–Poisson bracket. Let $\mathbf { g }$ be a $r$ -dimensional Lie algebra, $C _ { i j } ^ { k } \left( i , j , k = 1 , 2 , \cdot \cdot \cdot , r \right)$ be the configuration constants of $\mathbf { g }$ w.r.t. basis $v _ { 1 } , v _ { 2 } , \cdots , v _ { r }$ . Let $V$ be another $r$ - dimensional linear space, with coordinate $x = ( x _ { 1 } , x _ { 2 } , \cdot \cdot \cdot , x _ { r } )$ . Then Lie–Poisson bracket is defined by:

$$
\{ F , H \} = \sum _ { i , j , k = 1 } ^ { r } C _ { i j } ^ { k } x ^ { k } \frac { \partial F } { \partial x _ { i } } \frac { \partial H } { \partial x _ { j } } , \quad \forall F , H \in C ^ { \infty } ( \mathbf { R } ) .
$$

According to the notation of the Poisson system

$$
k ^ { i j } ( x ) = \sum _ { l = 1 } ^ { r } C _ { i j } ^ { l } x ^ { l } .
$$

It is easy to verify that $\{ F , H \}$ satisfies the 4 properties of a Poisson bracket. For the infinite dimensional evolution equations, there exists a corresponding coordinate definition; see the literatures[Arn89,MR99] .

Lie group action and momentum mapping. The Lie–Poisson system is closely related to the Hamiltonian system with symmetry.

Definition 1.6. The invariant property of a Hamiltonian system under one parameter differomorphism group is called symmetry of the Hamiltonian system. Under certain circumstance, this invariant property is called momentum. The corresponding mapping is called momentum mapping.

The Lie group, action on manifold $M , \forall g \in G$ , and corresponds to a self-homeomorphism $\phi _ { g }$ on $M$ . Below, we consider only the translation action of $G$ on itself and the induced action on $_ { T G }$ and $T ^ { * } G$ .

Definition 1.7. Infinitesimal generator vector field: let $\mathbf { g }$ be a Lie algebra of $G , \xi \in \mathbf { g }$ , then exp $t \xi \in G$ ,

$$
\xi _ { M } = \frac { \mathrm { d } } { \mathrm { d } t } \bigg \vert _ { t = 0 } \phi _ { \exp { t } \xi } ( x ) , \quad x \in M
$$

is called infinitesimal generator vector field of the flow $F _ { t } = \phi _ { \mathrm { e x p } ~ t \xi }$

Definition 1.8 (Lifted action). Action $\phi _ { g } \ : \ M \to \ M$ may induce action $\widetilde { \phi } _ { g }$ : $T ^ { * } M \to T ^ { * } M$ , which is defined as follows:

$$
\begin{array} { r } { \widetilde { \phi } _ { g } ( \alpha ) = T ^ { * } \phi _ { g ^ { - 1 } } = ( T ^ { * } \phi _ { g } ) ^ { - 1 } ( \alpha ) , \quad \alpha \in T _ { \phi ( g ) } ^ { * } ( x ) . } \end{array}
$$

Thus, we can prove that the lifted mapping of a diffeomorphism is symplectic.

Definition 1.9 (Momentum mapping). Let $( P , \omega )$ be a connected symplectic manifold. Let $G$ be a Lie group, $\phi _ { g } : P \to P$ a symplectic action. We call $\mathcal { I } : P \to { \bf g } ^ { * } ( { \bf g } ^ { * }$ is the dual space of $\mathrm { g }$ ) a momentum mapping, if $\mathcal { I }$ satisfies

$$
\forall \xi \in \mathbf { g } , \quad \mathrm { d } \widehat { \mathcal { I } } ( \xi ) = i _ { \xi _ { p } } \omega ,
$$

where $\widehat { \mathcal { I } } ( \xi )$ is defined by $\widehat { \mathcal { I } } ( \xi ) ( x ) = \langle \mathcal { I } ( x ) , \xi \rangle , \langle \cdot , \cdot \rangle$ denotes a scalar product, and $\xi _ { p }$ is the infinitesimal generator of the action to $\xi$ .

Theorem 1.10 (Generalized Noether theorem). Let $\phi$ be a symplectic action of $G$ on $( P , \omega )$ with a momentum mapping $\mathcal { I }$ . Suppose $H : P \to \mathbf { R }$ is $G$ -invariant, i.e.,

$$
H ( x ) = H ( \phi _ { g } ( x ) ) , \quad \forall x \in P , \quad g \in G ,
$$

then $\widehat { \mathcal { I } }$ is a first integral of $X _ { H }$ , i.e., if $F _ { t }$ is the phase flow of $X _ { H }$ , then

$$
\mathcal { I } ( F _ { t } ( x ) ) = \mathcal { I } ( x ) .
$$

Proof. See[MW83] .

Definition 1.11. A momentum mapping $\mathcal { I }$ is called $A d ^ { * }$ -equivariant, if

$$
\mathcal { I } ( \phi _ { g } ( x ) ) = A d _ { g ^ { - 1 } } ^ { * } \mathcal { I } ( x ) , \quad \forall g \in G ,
$$

that is, the following diagram commutes

$$
\begin{array} { r } { \begin{array} { r l r } & { P } & { \xrightarrow { \phi _ { g } } } \\ & { \mathcal { I } \Big \downarrow } \\ & { \mathcal { I } \Big \downarrow } \\ & { \mathbf { g } ^ { * } } & { \xrightarrow { A d _ { g ^ { - 1 } } ^ { * } } \mathbf { g } ^ { * } } \end{array} } \end{array}
$$

and we call such a group action as a Poisson action[AN90] .

Theorem 1.12. [MR99] $\mathcal { I }$ is $A d ^ { * }$ -equivariant momentum mapping, iff

$$
\{ \widehat { \mathcal { I } } ( \xi ) , \widehat { \mathcal { I } } ( \eta ) \} = \widehat { \mathcal { I } } ( [ \xi , \eta ] ) ,
$$

i.e., $\widehat { \mathcal { I } }$ is a Lie homomorphism.

Corollary 1.13. Let $\phi$ be a Poisson action of $G$ on the manifold $M$ , and $\widetilde { \phi }$ be the lifted action on $T ^ { * } ( M ) = P$ . Then this action $\widetilde { \phi }$ is symplectic and has an $A d ^ { * }$ -equivariant momentum mapping given by

$$
\mathcal { I } : \ : P \longrightarrow g ^ { * } , \quad \widehat { \mathcal { I } } ( \xi ) ( \alpha ( q ) ) = \alpha ( q ) \cdot \xi _ { M } ( q ) , \quad q \in M , \quad \alpha ( q ) \in T ^ { * } M .
$$

$\xi _ { M }$ is the infinitesimal generator of $\phi$ on $M$

Below, we will discuss the translation action of a Lie group on itself using the above theorem and deduction.

Let $G$ be a Lie group, $\phi : G \times G \to G$ be a left translation action $( g , h ) \to g h$ . Then its infinitesimal generator is

$$
\xi _ { G } ( g ) = T _ { e } R _ { g } \xi = R _ { g } ^ { * } \xi .
$$

Because lifted action is symplectic, by Corollary 1.13, we can obtain the momentum mapping:

$$
\mathcal { I } ( \alpha _ { q } ) ( \xi ) = \alpha _ { q } T _ { e } R _ { g } \xi = \alpha _ { q } R _ { g } ^ { * } \xi \Longrightarrow \mathcal { I } ( \alpha _ { q } ) = T _ { e } R _ { g } ^ { * } \alpha _ { q } = R _ { g } ^ { * } \alpha _ { q } ,
$$

or can rewrite it as

$$
\begin{array} { r } { \mathcal { I } _ { L } ( \alpha _ { q } ) = R _ { g } ^ { * } \alpha _ { q } . } \end{array}
$$

Likewise, we can obtain the similar result for the right translation

$$
\begin{array} { r } { \mathcal { I } _ { R } ( \alpha _ { q } ) = L _ { g } ^ { * } \alpha _ { q } . } \end{array}
$$

Lie–Poisson bracket and motion equation. In the previous sections, we have introduced the Lie–Poisson bracket and equations which are expressed by the local coordinates. Below, we will introduce an intrinsic definition of Lie–Poisson bracket and its induced equation of motion.

Let $\langle \cdot , \cdot \rangle$ be the pairing between $\mathbf { g } ^ { * }$ and $\mathbf { g } , \forall F \colon \mathbf { g } ^ { * } \to \mathbf { R } , { \frac { \delta F } { \delta \mu } } \in \mathbf { g } , \mu \in \mathbf { g } ^ { * } ,$ is defined by

$$
\mathrm { { D } } F ( \mu ) \gamma = \Big \langle \gamma , \frac { \delta F } { \delta \mu } \Big \rangle , \quad \gamma \in \mathbf { g } ^ { * } .
$$

If we regard $\mathbf { g } ^ { * * } \simeq \mathbf { g }$ , then $\mathsf { D } F ( \mu ) \in \mathsf { g } ^ { * * }$ becomes an element of $\mathbf { g }$ ,

$$
\{ F , G \} ( \mu ) = - \bigg \langle \mu , \Big [ \frac { \delta F } { \delta \mu } , \frac { \delta G } { \delta \mu } \Big ] \bigg \rangle ,
$$

where $[ \cdot , \cdot ]$ is the Lie bracket on g. The above equation is usually denoted as $\{ F , G \}$ . It is easy to verify that $\{ \cdot , \cdot \}$ satisfies the 4 properties of Poisson bracket, and are often called as $( \langle \langle - \rangle \rangle )$ Lie–Poisson bracket. They are first proposed by $\mathrm { L i e ^ { \left[ \mathrm { L i e 8 8 } \right] } }$ and are redefined by Berezin and others thereafter. We can prove that $\{ \cdot , \cdot \}$ can be derived from the left translation reduction of a typical Poisson bracket on $T ^ { * } G$ . If the right translation reduction is used, we have the Lie–Poisson bracket $\langle \langle + \rangle \rangle )$ :

$$
\{ F , G \} ( \mu ) = \Big \langle \mu , \Big [ \frac { \delta F } { \delta \mu } , \frac { \delta G } { \delta \mu } \Big ] \Big \rangle = \{ F , G \} _ { + } .
$$

Given a Lie–Poisson bracket, we can define the Lie–Poisson equation. Take $\{ \cdot , \cdot \}$ as an example.

Proposition 1.14. If $H _ { - } \in C ^ { \infty } ( \mathbf { g } ^ { * } )$ is a Hamiltonian function, then the evolutionary equation on $\mathbf { g } ^ { * }$ is:

$$
\dot { F } = \{ F , H \} _ { - } ,
$$

i.e.,

$$
\dot { \mu } = X _ { H _ { - } } ( \mu ) = a d _ { \frac { \delta H } { \delta \mu } } ^ { * } \mu .
$$

Proof. Because

$$
{ \dot { F } } ( \mu ) = D F ( \mu ) \cdot { \dot { \mu } } = \Big \langle { \dot { \mu } } , \frac { \delta F } { \delta \mu } \Big \rangle ,
$$

and

$$
\{ F , H _ { - } \} _ { - } ( \mu ) = - \Big \langle \mu , \Big [ \frac { \delta F } { \delta \mu } , \frac { \delta H } { \delta \mu } \Big ] \Big \rangle = \Big \langle \mu , a d _ { \frac { \delta H } { \delta \mu } } \frac { \delta F } { \delta \mu } \Big \rangle = \Big \langle a d _ { \frac { \delta H } { \delta \mu } } ^ { * } \mu , \frac { \delta F } { \delta \mu } \Big \rangle .
$$

Since $F$ is arbitrary, we obtain

$$
\begin{array} { r } { \dot { \mu } = a d _ { \frac { \delta H } { \delta \mu } } ^ { \ast } \mu . } \end{array}
$$

Likewise, for the right invariant system, the equation is

$$
\begin{array} { r } { \dot { \mu } = - a d _ { \frac { \delta H } { \delta \mu } } ^ { \ast } \mu . } \end{array}
$$

Henceforth, we will denote the system of left translation reduction as $\mathbf { g } _ { + } ^ { * }$ , and the right translation reduction as $\mathrm { g } _ { - } ^ { * }$ . Generally speaking, the rigid body and Heavy top system belongs to the left invariant system $\mathbf { g } _ { - } ^ { * }$ , and the continuous systems, such as plasma and the incompressible flow, are right invariant system $\mathbf { g } _ { + } ^ { * }$ . -

Lemma 1.15. $\mathcal { I } _ { L }$ , $\mathcal { I } _ { R }$ are Poisson mapping.

Proof. $\mathrm { S e e } ^ { \mathrm { [ M W 8 3 ] } }$ .

From this lemma, we can obtain the following reduction theorem (it will be used in the generating function theory later).

Theorem 1.16. $1 ^ { \circ }$ For the left invariant system $\mathrm { g _ { - } ^ { \ast } }$ , we have the following diagram commutes:

$$
\begin{array} { r l } { T ^ { * } G } & { { } \xrightarrow { G _ { H \circ \mathcal { I } _ { R } } ^ { t } } \ T ^ { * } G } \\ { \mathcal { I } _ { R } \Big \downarrow } & { { } \mathcal { I } _ { R } \Big \downarrow } \\ { \mathrm { g } _ { - } ^ { * } } & { { } \xrightarrow { G _ { H } ^ { t } } \quad \mathrm { g } _ { - } ^ { * } } \end{array}
$$

where ${ \cal H } : g ^ { * }  { \bf R }$ is a Hamiltonian function on $\mathbf { g } _ { - } ^ { * }$ , $G _ { H } ^ { t }$ is a phase flow of Hamiltonian function $H$ on $\mathbf { g } _ { - } ^ { * }$ , and $G _ { H \circ \mathcal { I } _ { R } } ^ { t }$ − is phase flow of Hamiltonian function $H \circ \mathcal { I } _ { R }$ on $T ^ { * } G$ .

$2 ^ { \circ }$ Similarly for right invariant system $\mathbf { g } _ { + } ^ { * }$ , we have

$$
\begin{array} { r l } { T ^ { * } G } & { { } \xrightarrow { G _ { H \circ \mathcal { I } _ { L } } ^ { t } } \ T ^ { * } G } \\ { \mathcal { I } _ { L } \Big \downarrow } & { { } \qquad \mathcal { I } _ { L } \Big \downarrow } \\ { g _ { + } ^ { * } } & { { } \xrightarrow { G _ { H } ^ { t } } \quad g _ { + } ^ { * } } \end{array}
$$

Theorem 1.17. The solutions of a Lie–Poisson system are a bundle of coadjoint orbits. Each coadjoint orbit is a symplectic manifold and is called symplectic leave of the Lie–Poisson system.

This theorem is from literature[AM78] . For Lie–Poisson system such as Heavy Top and the compressible flows, similar set of theories can be established. The readers can refer to literature[MRW90] for more details.

# 12.1.3 Introduction of the Generalized Rigid Body Motion

Let $G$ be a Lie group (finite dimensional), $g ( t )$ be a movement on $G$ . We define:

Velocity: $V ( t ) = \dot { g } ( t ) \in T _ { g ( t ) } G$ ;

Angular velocity in body description: $W _ { B } ( t ) = T L _ { g ( t ) ^ { - 1 } } ( \dot { g } ( t ) ) \in \mathfrak { g } ;$

Angular velocity in space description: $W _ { S } ( t ) = T R _ { g ( t ) ^ { - 1 } } ( \dot { g } ( t ) ) \in \mathfrak { g } ;$

Momentum : $\begin{array} { r } { M ( t ) = A _ { g } \dot { g } } \end{array}$ , where $A _ { g } : T _ { g } G \to T _ { g } ^ { * } G$ is called a moment of inertia operator, it relates to the kinetic energy by

$$
T = \frac 1 2 ( \dot { g } , \dot { g } ) _ { g } = \frac 1 2 ( W _ { B } , W _ { B } ) = \frac 1 2 \langle A W _ { B } , W _ { B } \rangle = \frac 1 2 \langle A _ { g } \dot { g } , \dot { g } \rangle ,
$$

where $A \colon \mathbf { g } \to \mathbf { g } ^ { * }$ is a value of $A _ { g }$ at $g = e$ ;

Angular momentum in body description: $M _ { B } ( t ) = T ^ { * } R _ { g ( t ) } ( M ( t ) ) \in \mathbf { g } ^ { * }$ ;   
Angular momentum in space description: $M _ { S } ( t ) = T ^ { * } L _ { g ( t ) } ( M ( t ) ) \in \mathfrak { g } ^ { * }$ .

From the above definition, we can obtain the following conclusions:

$$
W _ { S } ( t ) = A d _ { g ( t ) } W _ { B } ( t ) , \quad M _ { S } ( t ) = A d _ { g ( t ) ^ { - 1 } } ^ { * } M _ { B } ( t ) , \quad M _ { B } ( t ) = A W _ { B } ( t ) .
$$

By Theorem 1.10, we get:

Theorem 1.18. Conservation of spatial angular momentum theorem

$$
\frac { \mathrm { d } } { \mathrm { d } t } M _ { S } ( t ) = 0 .
$$

Because the system that takes kinetic energy $T$ as the Hamiltonian function is left invariant, $M _ { S } ( t )$ is the momentum mapping exactly.

# Corollary 1.19. Euler equation

$$
\frac { \mathrm { d } } { \mathrm { d } t } M _ { B } ( t ) = \{ W _ { B } ( t ) , M _ { B } ( t ) \} = \{ A ^ { - 1 } M _ { B } ( t ) , M _ { B } ( t ) \} ,
$$

where $\{ \cdot , \cdot \}$ is defined by:

$$
\{ \xi , a \} = a d _ { \xi } ^ { * } a , \quad \forall \xi \in g , a \in g ^ { * } .
$$

Given below are two different proofs of the Euler equation.

Proof. $1 ^ { \circ }$ From the Lie–Poisson equation of the motion $\dot { \mu } = a d _ { \frac { \partial H } { \partial \mu } } ^ { * } \mu$ , we can obtain directly

$$
H = \frac { 1 } { 2 } ( W _ { B } ( t ) , M _ { B } ( t ) ) = \frac { 1 } { 2 } \big ( A ^ { - 1 } M _ { B } ( t ) , M _ { B } ( t ) \big ) ,
$$

$$
{ \frac { \delta H } { \delta M _ { B } } } = A ^ { - 1 } M _ { B } ( t ) = W _ { B } ( t ) .
$$

$2 ^ { \circ }$ By the definition of spatial angular momentum, we have

$$
M _ { B } ( t ) = A d _ { g ( t ) } ^ { * } A d _ { g ( 0 ) ^ { - 1 } } ^ { * } M _ { B } ( 0 ) = A d _ { g ( t ) } ^ { * } \eta .
$$

Since

$$
M _ { S } ( t ) = M _ { S } ( 0 ) \Longrightarrow A d _ { g ( t ) ^ { - 1 } } ^ { * } M _ { B } ( t ) = A d _ { g ( 0 ) ^ { - 1 } } ^ { * } M _ { B } ( 0 ) = \eta .
$$

This also indicates that the trajectory of Lie–Poisson equation lies in some coadjoint orbit. From

$$
\langle M _ { B } ( t ) , \xi \rangle = \langle A d _ { g ( t ) } ^ { * } \eta , \xi \rangle = \langle \eta , A d _ { g ( t ) } \xi \rangle , \quad \forall \xi \in { \bf g } ,
$$

taking time derivatives on two sides, we get

$$
\left. \frac { \mathrm { d } M _ { B } ( t ) } { \mathrm { d } t } , \xi \right. = \left. \eta , [ T R _ { g ( t ) ^ { - 1 } } ( \dot { g } ( t ) ) , A d _ { g ( t ) } \xi ] \right. ,
$$

since

$$
\frac { \textrm { d } } { \textrm { d } t } A d _ { g ( t ) } \xi = [ T R _ { g ( t ) ^ { - 1 } } \dot { g } ( t ) , A d _ { g ( t ) } \xi ]
$$

$( \mathrm { s e e } ^ { \mathrm { [ A M 7 8 ] } } )$ , then

$$
\begin{array} { l l l } { \left. \frac { { \mathrm { d } } M _ { B } ( t ) } { { \mathrm { d } } t } , \xi \right. } & { = } & { \left. \eta , \left[ T R _ { g ( t ) } - \dot { y } ( t ) , A d _ { g ( t ) } \xi \right] \right. } \\ & { = } & { \left. \eta , A d _ { g ( t ) } [ T L _ { g ( t ) } - \dot { y } ( t ) , \xi ] \right. } \\ & { = } & { \left. A d _ { g ( t ) } ^ { * } \eta , a d _ { T L _ { g ( t ) } - 1 } \dot { y } ( t ) \xi \right. } \\ & { = } & { \left. M _ { B } ( t ) , a d _ { T L _ { g ( t ) } - 1 } \dot { y } ( t ) \xi \right. } \\ & { = } & { \left. a d _ { T L _ { g ( t ) } - 1 } ^ { * } \dot { y } ( t ) ^ { M } B ( t ) , \xi \right. } \\ & { \implies \frac { { \mathrm { d } } M _ { B } ( t ) } { { \mathrm { d } } t } = a d _ { T L _ { g ( t ) } - 1 } ^ { * } \dot { y } ( t ) ^ { M } B ( t ) = \left\{ W _ { B } ( t ) , { M } _ { B } ( t ) \right\} . } \end{array}
$$

The proof can be obtained.

Generally speaking, an equation of motion on $T ^ { * } G$ , if it has Hamiltonian function $H = T$ , it can be expressed by

$$
\begin{array} { r c l } { { \dot { g } ( t ) ~ = ~ T L _ { g ( t ) } \frac { \partial H } { \partial \mu } = L _ { g ( t ) ^ { * } } \frac { \partial H } { \partial \mu } , } } \\ { { \dot { \mu } ( t ) ~ = ~ a d _ { \frac { \partial H } { \partial \mu } } ^ { * } \mu ( t ) . } } \end{array}
$$

Its solution is $\mu ( t ) = A d _ { g ( t ) } ^ { * } A d _ { g ( 0 ) ^ { - 1 } } ^ { * } \mu ( 0 )$ . The Equation (1.14) is called as the Lie– Poisson equation.

# 12.2 Constructing Difference Schemes for Linear Poisson Systems

Since the phase flow of Hamiltonian system is Poisson phase flow, which preserves the Poisson structure, it is important to construct difference schemes for system (1.4) that preserve the same property. Difference scheme that preserves the Poisson bracket is called as the Poisson difference scheme.

One special case of the Poisson phase flow is the symplectic phase flow. How to construct the symplectic difference schemes has already been described in the previous chapters. The reader can also refer to literatures[Fen85,FWQW89,FQ87,CS90] for more details. However, the numerical algorithm for a general Poisson phase flow is still in its infancy. So far the results are limited to cases where structure matrix $K$ is constant $[ \mathrm { W a n } \dot { 9 } 1 , Z \mathrm { Q } 9 4 , \mathrm { A K W } 9 3 , \mathrm { K a r } 0 4 ]$ and $K ( z )$ is linear (Lie–Poisson) only. We will discuss the results for the Lie–Poisson case in the next section. In this section, we will discuss the results when $K$ is a constant matrix.

# 12.2.1 Constructing Difference Schemes for Linear Poisson Systems

Without loss of generality, we assume that $K$ is an odd-dimensional matrix. Because odd dimensional antisymmetric matrix is definitely degenerated, there exists a coordinate transformation $P \in G L ( n )$ such that $P K P ^ { \mathrm { { T } } } = \left[ \begin{array} { c c } { J _ { 2 r } } & { O } \\ { O } & { O _ { s } } \end{array} \right] .$ .

Definition 2.1. A difference scheme $\widehat z = g _ { H } ^ { \tau } ( z )$ is called a Poisson scheme, if and only if $g _ { z } K g _ { z } ^ { \mathrm { T } } = K$ .

Next, we have:

Definition 2.2. $S _ { K } ( n ) = \{ A \in G L ( n ) \mid A K A ^ { \mathrm { T } } = K \}$ , then the set $S _ { K } ( n )$ has the following properties:

$1 ^ { \circ }$ When the rank of $K$ is an even number and non-singular, then $K$ has all the properties of a symplectic matrix.

$2 ^ { \circ }$ When the rank of $K$ is an odd number, it must be degenerated. It is easy to verify that $S _ { K } ( n )$ is a group and we call it as $K$ -symplectic group. Its Lie algebra is

$$
s _ { K } ( n ) = \{ a \in g l ( n ) \mid a K + K a ^ { \operatorname { T } } = 0 \} .
$$

According to Feng et al. $[ \mathrm { F W Q 9 0 } ]$ , we can establish the relationship between $S _ { K } ( n )$ and $s _ { K } ( n )$ via Cayley transformation. If $A \in S _ { K } ( n )$ , namely if $A K A ^ { \mathrm { T } } = K$ , then

$$
B = ( I - A ) ( I + A ) ^ { - 1 } = ( I + A ) ^ { - 1 } ( I - A )
$$

is an element of $s _ { K } ( n )$ . However, if $B \in s _ { K } ( n )$ , then

$$
A = ( I - B ) ( I + B ) ^ { - 1 } = ( I + B ) ^ { - 1 } ( I - B )
$$

is an element of $S _ { K } ( n )$

For a generalized Cayley transformation, we have the following result similarly:

Theorem 2.3. Given $\begin{array} { r } { \phi ( \Lambda ) = \frac { p ( \Lambda ) } { p ( - \Lambda ) } } \end{array}$ , $p ( \Lambda )$ is a polynomial that satisfies $p ( 0 ) = 1$ $\dot { p } ( 0 ) \neq 0$ , if $B \in s _ { K } ( n )$ , then

$$
A = \phi ( B ) \in S _ { K } ( n ) .
$$

Therefore, we may use Pade approximation and pseudo-spectral method (the ´ Chebyshev spectral method) to construct the Poisson schemes for the linear Poisson system. The Pade approximation has been described in the literatures ´ [Qin89,ZQ94,FWQ90] in detail. Below, we will briefly describe the Chebyshev spectral method to construct the Poisson scheme. The Chebyshev spectral method is a highly effective method to approximate $\mathrm { e } ^ { A }$ . The detailed explanation of this is described in literature[TF85] . Here, we give only the result.

The Chebyshev spectral method is an approach based on series expansion by Chebyshev polynomial, i.e.,

$$
\mathbf { e } ^ { x } = \sum _ { k = 0 } ^ { \infty } C _ { k } J _ { k } ( R ) Q _ { k } \Big ( \frac { x } { R } \Big ) , \quad | x | < R ,
$$

where $x$ is a real number and $Q _ { k }$ is the Chebyshev complex orthogonal multinomial. $Q _ { k }$ satisfies the following recurrence relation:

$$
\begin{array} { l } { { Q _ { 0 } ( x ) = 1 , } } \\ { { \ } } \\ { { Q _ { 1 } ( x ) = x , } } \\ { { \ } } \\ { { Q _ { k + 1 } ( x ) = Q _ { k - 1 } ( x ) + 2 x Q _ { k } ( x ) , } } \end{array}
$$

where $C _ { 0 } = 1$ , and $C _ { k } = 2$ for $k > 0 , J _ { k }$ denotes the $k$ -order Bessel function. $Q _ { k }$ denotes the Chebyshev polynomial. $R$ is chosen arbitrarily. During computing, we calculate $J _ { k } ( R )$ first, and then calculate $Q _ { k }$ using the above recursive procedure.

Using the generalized Cayley transformation, and

$$
\mathrm { e } ^ { A } = { \frac { \mathrm { e } ^ { \frac { A } { 2 } } } { \mathrm { e } ^ { \frac { - A } { 2 } } } } ,
$$

and applying the Chebyshev spectral method to the numerator and denominator respectively, we can obtain the Poisson algorithm.

It was pointed out in literature $\left[ \mathrm { T F 8 5 } \right] ^ { - }$ that when $k > R$ , the series converges exponentially. Therefore, the summation in (2.1) is always finite. Where to truncate the series is determined by the size of $J _ { k } ( R )$ . Since $J _ { k } ( R )$ converges exponentially too, only a few steps of iteration is enough. Numerical tests show that this method has high accuracy and efficiency, especially when $A$ is a dense matrix. The above method can be applied only to the linear dynamic system, where $H$ is a quadratic form of $z$ ,

$$
\dot { z } = K B z .
$$

# 12.2.2 Construction of Difference Schemes for General Poisson Manifold

For a general $H$ , there are other methods to construct Poisson integrator such as method of generating function. The reader can refer to literatures[Fen85,FWQW89,FQ87] for more details. For a low-order scheme, we can construct directly using the implicit Euler scheme and verify it by criterion (1.3).

$$
\dot { z } = K \frac { \partial H } { \partial z } ,
$$

construct

$$
z ^ { k + 1 } = z ^ { k } + \tau K \nabla H \Big ( \frac { 1 } { 2 } ( I + B ) z ^ { k + 1 } + \frac { 1 } { 2 } ( I - B ) z ^ { k } \Big ) .
$$

Take derivative of (2.2) w.r.t. $z ^ { k }$ ,

$$
\widehat { z } _ { z } = I + \tau K H _ { z z } \Big ( \frac { 1 } { 2 } ( I + B ) \widehat { z } _ { z } + \frac { 1 } { 2 } ( I - B ) \Big ) ,
$$

i.e.,

$$
\Big ( I - \frac { 1 } { 2 } \tau K H _ { z z } ( I + B ) \Big ) \widehat { z } _ { z } = I + \frac { 1 } { 2 } \tau K H _ { z z } ( I - B ) ,
$$

where $z ^ { k + 1 } = { \widehat { z } } , z ^ { k } = z , x _ { y } = { \frac { \partial x } { \partial y } } ,$ , therefore,

$$
\widehat { z } _ { z } = \Big ( I - \frac { 1 } { 2 } \tau K H _ { z z } ( I + B ) \Big ) ^ { - 1 } \Big ( I + \frac { 1 } { 2 } \tau K H _ { z z } ( I - B ) \Big ) .
$$

To become a Poisson scheme, it should satisfy

$$
\begin{array} { r } { \widehat { z } _ { z } K \widehat { z } _ { z } ^ { \mathrm { T } } = K , } \end{array}
$$

i.e.,

$$
\begin{array} { r l } & { \left( I - \frac { 1 } { 2 } \tau K H _ { z z } ( I + B ) \right) ^ { - 1 } \left( I + \frac { 1 } { 2 } \tau K H _ { z z } ( I - B ) \right) K } \\ & { \cdot \left( I + \frac { 1 } { 2 } \tau K H _ { z } z ( I - B ) \right) ^ { \mathrm { T } } \left( I - \frac { 1 } { 2 } \tau K H _ { z } z ( I + B ) \right) ^ { - 1 } = K . } \end{array}
$$

After manipulation, we obtain

$$
K H _ { z z } ( K B ^ { \mathrm { T } } + B K ) H _ { z z } K = O .
$$

Therefore, if $K B ^ { \mathrm { T } } + B K = O$ , i.e., $B ^ { \mathrm { T } } \in { \mathfrak { s } } _ { K } ( n )$ , this scheme is a Poisson scheme.   
When $B = O$ , then the scheme becomes Euler midpoint scheme.

Denote

$$
z ^ { k + 1 } = G _ { H , B } ^ { \tau } z ^ { k } ,
$$

then for $B = O$ , the scheme is of second-order, for $B \neq O$ , it is only of first order. Using

$$
z ^ { k + 1 } = G _ { H , \pm B } ^ { \tau } z ^ { k } ,
$$

we can construct a composite scheme,

$$
\begin{array} { l } { { G _ { H , \pm B } ^ { \tau } = G _ { H , B } ^ { \frac { \tau } { 2 } } \circ G _ { H , - B } ^ { \frac { \tau } { 2 } } , } } \\ { { \ } } \\ { { G _ { H , \mp B } ^ { \tau } = G _ { H , - B } ^ { \frac { \tau } { 2 } } \circ G _ { H , B . } ^ { \frac { \tau } { 2 } } } } \end{array}
$$

Proposition 2.4. The above scheme has the second-order accuracy and the following proposition can be easily derived.

If $\phi _ { A } ( z ) = \frac { 1 } { 2 } z ^ { \mathrm { T } } A z$ , where $A ^ { \mathrm { T } } = A$ , is a conservative quantity of Hamiltonian systemconserv $\frac { \mathrm { d } \boldsymbol { z } } { \mathrm { d } t } \ : = \ : K \frac { \partial \boldsymbol { H } } { \partial \boldsymbol { z } }$ , and if of differe $A$ satisfies ce scheme $B ^ { \mathrm { T } } A + A B ^ { \mathrm { T } } = 0$ , then $\phi _ { A } ( z )$ is also $a$ $G _ { H , - B } ^ { \tau }$

Proof. Because $\phi _ { A } ( z )$ is a conservative quantity of Hamiltonian system,

$$
\frac { 1 } { 2 } \widehat { z } ^ { \mathrm { T } } A \widehat { z } = \frac { 1 } { 2 } z ^ { \mathrm { T } } A z ,
$$

then

$$
\frac { 1 } { 2 } ( \widehat { z } + z ) ^ { \mathrm { T } } A ( \widehat { z } + z ) = 0 .
$$

From $B ^ { \mathrm { T } } A + A B ^ { \mathrm { T } } = 0$ , we obtain

$$
\begin{array} { r l } { \frac { 1 } { 2 } ( B ( \widehat z - z ) ) ^ { \mathrm T } A ( \widehat z - z ) } & { = \frac { 1 } { 2 } ( \widehat z - z ) B ^ { \mathrm T } A ( \widehat z - z ) } \\ & { = \frac { 1 } { 4 } ( \widehat z - z ) ^ { \mathrm T } ( B ^ { \mathrm T } A + A B ) ( \widehat z - z ) = 0 , } \\ { \left( \frac { 1 } { 2 } ( \widehat z + z ) + \frac { 1 } { 2 } B ( \widehat z - z ) \right) ^ { \mathrm T } A ( \widehat z - z ) } & { = 0 } \\ & { \Longrightarrow \tau w ^ { \mathrm T } A K H _ { z } ( w ) = 0 , \quad \forall ~ w \in \mathbb { R } ^ { n } . } \end{array}
$$

Let

$$
w = \frac { 1 } { 2 } ( z ^ { k + 1 } + z ^ { k } ) + \frac { 1 } { 2 } B ( z ^ { k + 1 } - z ^ { k } ) ,
$$

we obtain

$$
{ \frac { 1 } { 2 } } ( z ^ { k + 1 } ) ^ { \mathrm { T } } A z ^ { k + 1 } = { \frac { 1 } { 2 } } ( z ^ { k } ) ^ { \mathrm { T } } A z ^ { k } .
$$

The proof can be obtained.

# 12.2.3 Answers of Some Questions

# 1. Euler explicit scheme[LQ95a]

For a separable Hamiltonian $H$ in a standard Hamiltonian system, there exists an Euler explicit symplectic scheme. Similar question is raised for the Poisson system: does there exist an Euler explicit Poisson scheme for a separable $H ?$ The answer is “may not be”. We take $n = 3$ as an example to explain this point. Let

$$
K = \left[ \begin{array} { c c c } { { 0 } } & { { - c } } & { { b } } \\ { { } } & { { } } & { { } } \\ { { c } } & { { 0 } } & { { - a } } \\ { { - b } } & { { a } } & { { 0 } } \end{array} \right] ,
$$

$$
H = { \frac { 1 } { 2 } } ( z _ { 1 } ^ { 2 } + z _ { 2 } ^ { 2 } + z _ { 3 } ^ { 2 } ) ,
$$

then

$$
\dot { z } = K \frac { \partial H } { \partial z } = K z .
$$

To make scheme

$$
z ^ { k + 1 } = z ^ { k } + \tau K \nabla H \Big ( \frac { 1 } { 2 } ( I + B ) z ^ { k + 1 } + \frac { 1 } { 2 } ( I - B ) z ^ { k } \Big )
$$

a Poisson scheme, we should have

$$
K H _ { z z } ( K B ^ { \mathrm { T } } + B K ) H _ { z z } K = K ^ { 2 } B ^ { \mathrm { T } } K + K B K ^ { 2 } = O ,
$$

i.e., $K ^ { 2 } B ^ { \mathrm { T } } K \in S m ( n )$ (symmetrical matrix), here $K B ^ { \mathrm { T } } \in S m ( n )$ , i.e., $B K \in$ $S m ( n )$ . Expand scheme

$$
z ^ { k + 1 } = z ^ { k } + \tau K \nabla H ( w ) , \quad w = \frac { 1 } { 2 } ( I + B ) z ^ { k + 1 } + \frac { 1 } { 2 } ( I - B ) z ^ { k }
$$

into

$$
\left\{ \begin{array} { l l } { z _ { 1 } ^ { k + 1 } = z _ { 1 } ^ { k } - c \tau w _ { 2 } + b \tau w _ { 3 } , } \\ { \qquad \quad } \\ { z _ { 2 } ^ { k + 1 } = z _ { 2 } ^ { k } + c \tau w _ { 1 } - a \tau w _ { 3 } , } \\ { \qquad \quad } \\ { z _ { 3 } ^ { k + 1 } = z _ { 3 } ^ { k } - b \tau w _ { 1 } + a \tau w _ { 2 } . } \end{array} \right.
$$

To make sure the scheme is explicit, $w _ { 2 } , w _ { 3 }$ have to be a function of $z ^ { k }$ only. From

$$
w _ { 2 } = \frac { 1 } { 2 } ( z _ { 2 } ^ { k + 1 } + z _ { 2 } ^ { k } ) + \frac { 1 } { 2 } b _ { 2 1 } ( z _ { 1 } ^ { k + 1 } - z _ { 1 } ^ { k } ) + \frac { 1 } { 2 } b _ { 2 3 } ( z _ { 3 } ^ { k + 1 } - z _ { 3 } ^ { k } ) + \frac { 1 } { 2 } b _ { 2 2 } ( z _ { 2 } ^ { k + 1 } - z _ { 2 } ^ { k } ) ,
$$

we obtain $b _ { 2 1 } = 0 = b _ { 2 3 } , \ b _ { 2 2 } = - 1$ . Likewise, $b _ { 3 1 } = b _ { 3 2 } = 0 , b _ { 3 3 } = - 1 .$ Then $B$ has the form

$$
\left[ { \begin{array} { c c c } { b _ { 1 } } & { b _ { 2 } } & { b _ { 3 } } \\ { 0 } & { - 1 } & { 0 } \\ { 0 } & { 0 } & { - 1 } \end{array} } \right] ,
$$

substituting it into $B K ( \in S m ( n ) )$ , we know only when $a = 0$ , the scheme becomes an explicit scheme. Note that when $a = 0$ , $K$ is degenerated to the symplectic case. Therefore, in many situations, the separable system does not have an explicit scheme. Here the explicit scheme refers to the low-order finite-difference scheme, not the explicit analytic solution.

# 2. Midpoint scheme and Euler scheme

Below, we will answer the questions whether the midpoint scheme is a Lie–Poisson scheme of Euler equation, and whether there exists a Lie–Poisson scheme in a generalized Euler scheme[LQ95a,LQ95b] .

We already know that the answer for the first question is “no”. Now, we turn to the second question. The Euler equation has the form

$$
\dot { z } = J ( z ) H _ { z } = f ( z ) .
$$

For the case $n = 3$ ,

$$
J ( z ) = \left[ { \begin{array} { c c c } { 0 } & { - z _ { 3 } } & { z _ { 2 } } \\ { z _ { 3 } } & { 0 } & { - z _ { 1 } } \\ { - z _ { 2 } } & { z _ { 1 } } & { 0 } \end{array} } \right] ,
$$

$$
H = \frac { 1 } { 2 } \left( \frac { z _ { 1 } ^ { 2 } } { I _ { 1 } } + \frac { z _ { 2 } ^ { 2 } } { I _ { 2 } } + \frac { z _ { 3 } ^ { 2 } } { I _ { 3 } } \right) .
$$

We construct a generalized Euler scheme:

$$
\widehat { z } = z + \tau J ( w ) H _ { z } ( w ) = z + \tau f ( w ) ,
$$

where

$$
w = \frac { 1 } { 2 } ( \widehat { z } + z ) + \frac { 1 } { 2 } B ( \widehat { z } - z ) = \frac { 1 } { 2 } ( I + B ) \widehat { z } + \frac { 1 } { 2 } ( I - B ) z .
$$

The Jacobian matrix of map $z  { \widehat { z } }$ is

$$
A = \frac { \partial \widehat { z } } { \partial z } = I + \tau D _ { * } f ( w ) \left( \frac { \partial w } { \partial z } \right) ,
$$

where

$$
\begin{array} { r } { D _ { * } f ( z ) = D _ { * } J ( z ) H _ { z } = \left[ \begin{array} { c c c } { 0 } & { \frac { I _ { 2 } - I _ { 3 } } { I _ { 2 } I _ { 3 } } z _ { 3 } } & { \frac { I _ { 2 } - I _ { 3 } } { I _ { 2 } I _ { 3 } } z _ { 2 } } \\ { \frac { I _ { 3 } - I _ { 1 } } { I _ { 1 } I _ { 3 } } z _ { 3 } } & { 0 } & { \frac { I _ { 3 } - I _ { 1 } } { I _ { 1 } I _ { 3 } } z _ { 1 } } \\ { \frac { I _ { 1 } - I _ { 2 } } { I _ { 1 } I _ { 2 } } z _ { 2 } } & { \frac { I _ { 1 } - I _ { 2 } } { I _ { 1 } I _ { 2 } } z _ { 1 } } & { 0 } \end{array} \right] , } \\ { \frac { \partial w } { \partial z } = \frac { 1 } { 2 } ( I + B ) A + \frac { 1 } { 2 } ( I - B ) , } \end{array}
$$

therefore

$$
A = ( I - \tau D _ { * } f ( w ) ( I + B ) ) ^ { - 1 } ( I + \tau D _ { * } f ( w ) ( I - B ) ) .
$$

For the Euler scheme to be a Poisson scheme, it has to be $A J ( z ) A ^ { \mathrm { T } } = J ( \widehat { z } )$ , therefore:

$$
\begin{array} { r c l } { { } } & { { } } & { { A J ( z ) A ^ { \mathrm { T } } = ~ ( I - \tau D _ { * } f ( w ) ( I + B ) ) ^ { - 1 } ( I + \tau D _ { * } f ( w ) ( I - B ) ) J ( z ) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { \cdot ~ ( I + \tau ( I - B ^ { \mathrm { T } } ) ( D _ { * } f ( w ) ) ^ { \mathrm { T } } ) ( I - \tau ( I + B ) ( D _ { * } f ( w ) ) ^ { \mathrm { T } } ) ^ { - 1 } } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = ~ J ( \widehat z ) , } } \end{array}
$$

$$
\begin{array} { r l } & { ( I + \tau D _ { * } f ( w ) ( I - B ) ) J ( z ) ( I + \tau ( I - B ^ { \mathrm { T } } ) ( D _ { * } f ( w ) ) ^ { \mathrm { T } } ) } \\ & { } \\ & { = ( I - \tau D _ { * } f ( w ) ( I + B ) ) J ( \widehat { z } ) ( I - \tau ( I + B ^ { \mathrm { T } } ) ( D _ { * } f ( w ) ) ^ { \mathrm { T } } ) , } \end{array}
$$

after manipulation,

$$
\begin{array} { r l } & { J ( \hat { z } ) - J ( z ) + \tau ^ { 2 } D _ { * } f ( w ) [ ( I + B ) J ( \hat { z } ) ( I + B ^ { \mathrm { T } } ) - ( I - B ) J ( z ) ( I - B ^ { \mathrm { T } } ) ] ( D _ { * } f ( w ) ) ^ { \mathrm { T } } } \\ & { = \tau [ J ( z ) ( I - B ^ { \mathrm { T } } ) + J ( \hat { z } ) ( I + B ^ { \mathrm { T } } ) ] ( D _ { * } f ( w ) ) ^ { \mathrm { T } } + \tau D _ { * } f ( w ) [ ( I - B ) J ( z ) + ( I + B ) J ( \hat { z } ) ] } \\ & { = J ( \hat { z } - z ) + \tau ^ { 2 } D _ { * } f ( w ) [ J ( \hat { z } - z ) + B J ( \hat { z } + z ) + J ( \hat { z } + z ) B ^ { \mathrm { T } } + B J ( \hat { z } - z ) B ^ { \mathrm { T } } ] ( D _ { * } f ( w ) ) ^ { \mathrm { T } } . } \end{array}
$$

Because $\tau$ is arbitrary, and $\widehat { z } - z = { O } ( \tau )$ , we can have

$$
\left\{ \begin{array} { l l } { \begin{array} { r l } & { J ( \widehat { z } - z ) = \tau J ( \widehat { z } + z ) ( D _ { * } f ( w ) ) ^ { \mathrm { T } } + \tau D _ { * } f ( w ) J ( \widehat { z } + z ) , } \\ & { \tau ^ { 2 } D _ { * } f ( w ) [ B J ( \widehat { z } + z ) + J ( \widehat { z } + z ) B ^ { \mathrm { T } } ] ( D _ { * } f ( w ) ) ^ { \mathrm { T } } } \end{array} } \\ { \begin{array} { r l } & { = \tau J ( \widehat { z } - z ) B ^ { \mathrm { T } } ( D _ { * } f ( w ) ) ^ { \mathrm { T } } + \tau D _ { * } f ( w ) B J ( \widehat { z } - z ) , } \\ & { D _ { * } f ( w ) [ J ( \widehat { z } - z ) + B J ( \widehat { z } - z ) B ^ { \mathrm { T } } ] ( D _ { * } f ( w ) ) ^ { \mathrm { T } } = O . } \end{array} } \end{array} \right.
$$

When $B = O$ , the above equation is the midpoint scheme, $w = \frac { 1 } { 2 } ( \widehat { z } + z )$ . It is easy to verify that the last equality in the above equations is dissatisfied. Hence the midpoint scheme is not a Poisson scheme. When $B \neq O$ , after complex computation, we can obtain similarly that there does not exist any $B \in g l ( n )$ to satisfy the above 3 formulas. Therefore, there does not exist a Poisson scheme in a generalized Euler form.

# 12.3 Generating Function and Lie–Poisson Scheme

The generating function method plays a crucial role in constructing the symplectic scheme (see the literatures[FWQW89,CS90,CG93] for details). Therefore, how to use the generating function method to construct the Lie–Poisson scheme becomes a research hot spot. The literatures in this aspect include[GM88,Ge91,CS91] . We have also investigated the generating function for Lie–Poisson system in details, and discovered that the Ge–Marsden method needs further improvement. Below is our understanding and derivation on the generating function and the Hamilton–Jacobi theory[LQ95b] .

# 12.3.1 Lie–Poisson–Hamilton–Jacobi (LPHJ) Equation and Generating Function

According to the diagram in Section 12.1 (for the left invariant system),

$$
\begin{array} { r l } { T ^ { * } G } & { { } \xrightarrow { G _ { H \circ \mathcal { T } _ { R } } ^ { t } = S } \ T ^ { * } G } \\ { \mathcal { T } _ { R } \bigg \downarrow } & { { } \mathcal { T } _ { R } \bigg \downarrow } \\ { \mathbf { g } ^ { * } } & { { } \xrightarrow { G _ { H } ^ { t } = P } \quad \mathbf { g } ^ { * } } \end{array}
$$

the phase flow determined by $H$ on $\mathbf { g } ^ { * }$ can induce a phase flow on $T ^ { * } G$ determined by $H \circ \mathcal { I } _ { R }$ . Let $u ^ { t } ( q , q _ { 0 } )$ be a first kind generating function of the symplectic map $S$ . Then we have the following properties.

Property 3.1. If $u : G \times G \to \mathbf { R }$ is invariant under the left action of $G$ , i.e.,

$$
u ^ { t } ( g q , g q _ { 0 } ) = u ^ { t } ( q , q _ { 0 } ) ,
$$

then the symplectic mapping generated by $u , S : \ ( q _ { 0 } , p _ { 0 } ) \to ( p , q )$ , where:

$$
p _ { 0 } = - \frac { \partial u ^ { t } ( q , q _ { 0 } ) } { \partial q _ { 0 } } , \quad p = \frac { \partial u ^ { t } ( q , q _ { 0 } ) } { \partial q } ,
$$

preserves momentum mapping $\mathcal { I } _ { L }$ . That is to say,

$$
{ \mathcal { I } } _ { L } \circ S = { \mathcal { I } } _ { L } .
$$

For the right-invariant translation on $G$ ,

$$
{ \mathcal { I } } _ { R } \circ S = { \mathcal { I } } _ { R } .
$$

Definition 3.2. If $G$ acts on the configuration space without fixed point, then we say $G$ acts on $G$ freely.

Property 3.3. If $G$ acts on $G$ freely, and its induced symplectic mapping $S$ preserves the momentum mapping $\mathcal { T } _ { L }$ , then the first-kind generating function of $S$ is left invariant.

Proof. See[GM88] .

For a left-invariant system, such as a generalized rigid body, the Hamiltonian function is left invariant, the phase flow isa first integral for this dynamics, i.e., left invariant, the momentum mappiis invariant under the phase flow of $\mathcal { T } _ { L }$ $\mathcal { I } _ { L }$ $G _ { H \circ { \mathcal { I } } _ { R } } ^ { t }$ RTherefore, if the action is free (generally speaking, the action is locally free), the firstkind generating function is left invariant.

Let $u ^ { t } ( q , q _ { 0 } )$ be the first-kind generating function of $S$ , then by the left invariance

$$
u ^ { t } ( q , q _ { 0 } ) = u ^ { t } ( e , q ^ { - 1 } q _ { 0 } ) = \widetilde { u } ^ { t } ( g ) , \quad g = q ^ { - 1 } q _ { 0 } .
$$

By Equation (3.2), we have

$$
\begin{array} { r l } & { p _ { 0 } = - \frac { \partial u ^ { t } ( q , q _ { 0 } ) } { \partial q _ { 0 } } = - \frac { \partial \widetilde { u } ^ { t } ( q ^ { - 1 } q _ { 0 } ) } { \partial q _ { 0 } } = - \frac { \partial \widetilde { u } ^ { t } ( L _ { q ^ { - 1 } } q _ { 0 } ) } { \partial q _ { 0 } } = - L _ { q ^ { - 1 } } ^ { * } \frac { \partial \widetilde { u } } { \partial g } \Bigr | _ { g = q ^ { - 1 } } } \\ & { p = \frac { \partial u ^ { t } ( q , q _ { 0 } ) } { \partial q } = \frac { \partial \widetilde { u } ( q ^ { - 1 } q _ { 0 } ) } { \partial q } = \frac { \partial \widetilde { u } ( R _ { q _ { 0 } } V ( q ) ) } { \partial \widetilde { q } } = V ^ { * } R _ { q _ { 0 } } ^ { * } \frac { \partial \widetilde { u } } { \partial g } \Bigr | _ { g = q ^ { - 1 } q _ { 0 } } , } \\ & { V ( q ) = q ^ { - 1 } , } \\ & { V ^ { * } = - L _ { q ^ { - 1 } } ^ { * } R _ { q ^ { - 1 } } ^ { * } , } \end{array}
$$

then

$$
p = - L _ { q ^ { - 1 } } ^ { * } R _ { q ^ { - 1 } } ^ { * } R _ { q _ { 0 } } ^ { * } \frac { \partial \widetilde { u } } { \partial g } \Big | _ { g = q ^ { - 1 } q _ { 0 } } ,
$$

therefore,

$$
\begin{array} { r c l } { { \mu _ { 0 } ~ = ~ { \cal L } _ { q _ { 0 } } ^ { * } p _ { 0 } = - { \cal L } _ { q _ { 0 } } ^ { * } { \cal L } _ { q ^ { - 1 } } ^ { * } \frac { \partial \widetilde { u } } { \partial g } \Big | _ { g = q ^ { - 1 } q _ { 0 } } } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = ~ - { \cal L } _ { q ^ { - 1 } q _ { 0 } } ^ { * } \frac { \partial \widetilde { u } } { \partial g } \Big | _ { g = q ^ { - 1 } q _ { 0 } } = - { \cal L } _ { g } ^ { * } \frac { \partial \widetilde { u } } { \partial g } \Big | _ { g = q ^ { - 1 } q _ { 0 } } , } } \end{array}
$$

and

$$
\begin{array} { r c l } { { \mu } } & { { = } } & { { L _ { q } ^ { * } p = - L _ { q } ^ { * } L _ { q ^ { - 1 } } ^ { * } R _ { q ^ { - 1 } } ^ { * } R _ { q _ { 0 } } ^ { * } \frac { \partial \widetilde { u } } { \partial g } \Big | _ { g = q ^ { - 1 } q _ { 0 } } } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = } } & { { - R _ { q ^ { - 1 } q _ { 0 } } ^ { * } \frac { \partial \widetilde { u } } { \partial g } \Big | _ { g = q ^ { - 1 } q _ { 0 } } = - R _ { g } ^ { * } \frac { \partial \widetilde { u } } { \partial g } \Big | _ { g = q ^ { - 1 } q _ { 0 } } . } } \end{array}
$$

Through the above derivation, it is easy to prove (3.1)

$$
\begin{array} { r c l } { { { \cal M } _ { 0 } ~ = ~ R _ { q _ { 0 } } ^ { * } p _ { 0 } = - R _ { q _ { 0 } } ^ { * } L _ { q ^ { - 1 } } ^ { * } \frac { \partial \stackrel { \wedge } { u } } { \partial g } \Big | _ { g = q ^ { - 1 } q _ { 0 } } , } } \\ { { } } & { { } } & { { } } \\ { { { \cal M } ~ = ~ R _ { q } ^ { * } p = - R _ { q } ^ { * } L _ { q ^ { - 1 } } ^ { * } R _ { q ^ { - 1 } } ^ { * } R _ { q _ { 0 } } ^ { * } \frac { \partial \stackrel { \wedge } { u } } { \partial g } \Big | _ { g = q ^ { - 1 } q _ { 0 } } } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = ~ - L _ { q ^ { - 1 } } ^ { * } R _ { q _ { 0 } } ^ { * } \frac { \partial \stackrel { \wedge } { u } } { \partial g } \Big | _ { g = q ^ { - 1 } q _ { 0 } } } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = ~ - R _ { q _ { 0 } } ^ { * } L _ { q ^ { - 1 } } ^ { * } \frac { \partial \stackrel { \wedge } { u } } { \partial g } \Big | _ { q = q ^ { - 1 } q _ { 0 } } = { \cal M } _ { 0 } , } } \end{array}
$$

i.e.,

$$
{ \mathcal { T } } _ { L } \circ S = { \mathcal { T } } _ { L } .
$$

Take $g = q ^ { - 1 } q _ { 0 }$ , then

$$
\left\{ \begin{array} { l } { \displaystyle \mu _ { 0 } = - L _ { q } ^ { * } \frac { \partial \widetilde { u } ( \boldsymbol { g } ) } { \partial \boldsymbol { g } } , } \\ { \displaystyle \mu = - R _ { g } ^ { * } \frac { \partial \widetilde { u } ( \boldsymbol { g } ) } { \partial \boldsymbol { g } } = A d _ { g ^ { - 1 } } ^ { * } \mu _ { 0 } , } \end{array} \right.
$$

therefore $u ^ { t } ( q , q _ { 0 } ) = \widetilde { u } ^ { t } ( q ^ { - 1 } q _ { 0 } ) = \widetilde { u } ^ { t } ( g )$ defines a Poisson mapping:

$$
\mu _ { 0 }  \mu = A d _ { g ^ { - 1 } } ^ { * } \mu _ { 0 } .
$$

We now derive the conditions that $u ^ { t } ( q , q _ { 0 } )$ must meet.

$u ^ { t } ( q , q _ { 0 } )$ generates a symplectic map $S = G _ { H \circ J } ^ { t } = G _ { \overline { { H } } } ^ { t } .$ , where $\overline { { H } } = H \circ \mathcal { I }$ , and

$$
\begin{array} { l } { { S : ( p _ { 0 } , q _ { 0 } ) \longrightarrow ( p , q ) , } } \\ { { \ } } \\ { { p _ { 0 } = - \displaystyle { \frac { \partial u } { \partial q _ { 0 } } } , \quad p = \displaystyle { \frac { \partial u } { \partial q } } . } } \end{array}
$$

Because

$$
\begin{array} { l } { p \mathbf { d } q - p _ { 0 } \mathbf { d } q _ { 0 } = \displaystyle \frac { \partial u } { \partial q } \mathbf { d } q + \frac { \partial u } { \partial q _ { 0 } } \mathbf { d } q _ { 0 } , } \\ { \displaystyle \mathbf { d } u = \frac { \partial u } { \partial q } \mathbf { d } q + \frac { \partial u } { \partial q _ { 0 } } \mathbf { d } q _ { 0 } + \frac { \partial u } { \partial t } \mathbf { d } t = p \mathbf { d } q - p _ { 0 } \mathbf { d } q _ { 0 } + \frac { \partial u } { \partial t } \mathbf { d } t , } \end{array}
$$

we have

$$
\mathbf { d } \left( p \mathbf { d } q - p _ { 0 } \mathbf { d } q _ { 0 } + { \frac { \partial u } { \partial t } } \mathbf { d } t \right) = 0 .
$$

Note that

$$
{ \begin{array} { r l } & { \ d \left( p { \mathrm { d } } q - p _ { 0 } { \mathrm { d } } q _ { 0 } \right) = { \mathrm { d } } p \wedge { \mathrm { d } } q - { \mathrm { d } } p _ { 0 } \wedge { \mathrm { d } } q _ { 0 } } \\ { = } & { \left( { \frac { \partial p } { \partial p _ { 0 } } } { \mathrm { d } } p _ { 0 } + { \frac { \partial p } { \partial q _ { 0 } } } { \mathrm { d } } q _ { 0 } + { \frac { \partial p } { \partial t } } { \mathrm { d } } t \right) \wedge \left( { \frac { \partial q } { \partial p _ { 0 } } } { \mathrm { d } } p _ { 0 } + { \frac { \partial q } { \partial q _ { 0 } } } { \mathrm { d } } q _ { 0 } + { \frac { \partial q } { \partial t } } { \mathrm { d } } t \right) - { \mathrm { d } } p _ { 0 } \wedge { \mathrm { d } } q _ { 0 } } \\ { = } & { \left( { \frac { \partial p } { \partial p _ { 0 } } } { \frac { \partial q } { \partial q _ { 0 } } } - { \frac { \partial p } { \partial q _ { 0 } } } { \frac { \partial q } { \partial p _ { 0 } } } \right) { \mathrm { d } } p _ { 0 } \wedge { \mathrm { d } } q _ { 0 } - { \mathrm { d } } p _ { 0 } \wedge { \mathrm { d } } q _ { 0 } } \\ & { \ + { \frac { \partial q } { \partial t } } { \frac { \partial p } { \partial p _ { 0 } } } { \mathrm { d } } p _ { 0 } \wedge { \mathrm { d } } t + { \frac { \partial q } { \partial t } } { \frac { \partial p _ { 0 } } { \partial q _ { 0 } } } { \mathrm { d } } q _ { 0 } \wedge { \mathrm { d } } t } \\ & { \ - { \frac { \partial p } { \partial t } } { \frac { \partial q } { \partial p _ { 0 } } } { \mathrm { d } } p _ { 0 } \wedge { \mathrm { d } } t - { \frac { \partial p } { \partial t } } { \frac { \partial p } { \partial q _ { 0 } } } { \mathrm { d } } q _ { 0 } \wedge { \mathrm { d } } t } \end{array} }
$$

Since $( p _ { 0 } , q _ { 0 } ) \to ( p , q )$ is symplectic, we have

$$
g _ { z } J g _ { z } ^ { \mathrm { T } } = J \Longrightarrow f _ { 1 } = 0 .
$$

Because

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { \partial q } { \partial t } = \frac { \partial \overline { { H } } } { \partial p } } \\ { \displaystyle \frac { \partial p } { \partial t } = - \frac { \partial \overline { { H } } } { \partial q } } \end{array} \right. \Longrightarrow \left\{ \begin{array} { l l } { \displaystyle f _ { 2 } = \frac { \partial \overline { { H } } } { \partial p } \mathbf { d } p \wedge \mathbf { d } t } \\ { \displaystyle f _ { 3 } = \frac { \partial \overline { { H } } } { \partial q } \mathbf { d } q \wedge \mathbf { d } t } \end{array} \right. ,
$$

therefore,

$$
{ \begin{array} { r l } & { \mathbf { d } p \wedge \mathbf { d } q - d p _ { 0 } \wedge \mathbf { d } q _ { 0 } } \\ & { = { \frac { \partial { \overline { { H } } } } { \partial p } } \mathbf { d } p \wedge \mathbf { d } t + { \frac { \partial { \overline { { H } } } } { \partial q } } \mathbf { d } q \wedge \mathbf { d } t = \mathbf { d } { \overline { { H } } } \wedge \mathbf { d } t } \\ & { \Longrightarrow \mathbf { d } { \overline { { H } } } \wedge \mathbf { d } t + \mathbf { d } \left( { \frac { \partial { \overline { { H } } } } { \partial t } } \right) \wedge \mathbf { d } t = 0 . } \end{array} }
$$

We have

$$
\textrm { d } \left( \overline { { H } } + \frac { \partial \overline { { H } } } { \partial t } \right) \wedge \mathbf { d } t = 0 .
$$

Therefore,

$$
\frac { \partial u } { \partial t } + \overline { { H } } ( p , q , t ) = c .
$$

Taking a proper initial value, we can obtain:

$$
\frac { \partial u } { \partial t } + \overline { { H } } ( p , q , t ) = 0 ,
$$

i.e.,

$$
\frac { \partial u ^ { t } ( p , q ) } { \partial t } + H \circ \mathcal { T } _ { R } ( p , q , t ) = 0 .
$$

Therefore we obtain the LPHJ equations

$$
\frac { \partial \overline { { u } } ( g ) } { \partial t } + H \bigg ( - R _ { g } ^ { * } \frac { \partial \overline { { u } } ( g ) } { \partial g } \bigg ) = 0 ,
$$

$$
g = q ^ { - 1 } q _ { 0 } .
$$

Remark 3.4. If we can construct a generating function $u ( g )$ , we then have $u ( q _ { 0 } , q )$ . This function can generate a symplectic mapping on $T ^ { * } G$ . By the commutative diagram, a Poisson mapping on ${ \bf g } ^ { * }$ can also be induced. This is a key point of constructing a Lie–Poisson integrator by generating function.

Remark 3.5. In order that the induced phase flow is a Poisson phase flow, the phase flow on $T ^ { * } G$ should be symplectic. Therefore, the condition of $g = q ^ { - 1 } q _ { 0 }$ cannot be discarded. Namely, when $t \to 0$ , $g = q ^ { - 1 } q _ { 0 }$ (unit element).

Remark 3.6. Only when $g = q ^ { - 1 } q _ { 0 }$ is satisfied, the momentum mapping is invariant. This is because the momentum mapping is

$$
\begin{array} { r } { \mathcal { I } _ { L } ( p , q ) = R _ { q } ^ { * } p = A d _ { q ^ { - 1 } } ^ { * } \mathcal { I } _ { R } ( p , q ) . } \end{array}
$$

To make sure

$$
\begin{array} { r c l } { { \mathcal { I } _ { L } ( p _ { 0 } , q _ { 0 } ) = \mathcal { I } _ { L } ( p , q ) \implies A d _ { q _ { 0 } ^ { - 1 } } ^ { * } \mathcal { I } _ { R } ( p _ { 0 } , q _ { 0 } ) = A d _ { q ^ { - 1 } } ^ { * } \mathcal { I } _ { R } ( p , q ) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { \implies \mathcal { I } _ { R } ( p , q ) = A d _ { q } ^ { * } A d _ { q _ { 0 } ^ { - 1 } } ^ { * } \mathcal { I } _ { R } ( p _ { 0 } , q _ { 0 } ) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = } } & { { A d _ { ( q ^ { - 1 } q _ { 0 } ) ^ { - 1 } } ^ { * } \mathcal { I } _ { R } ( p _ { 0 } , q _ { 0 } ) = A d _ { g ^ { - 1 } } ^ { * } \mathcal { I } _ { R } ( p _ { 0 } , q _ { 0 } ) . } } \end{array}
$$

If $g = q ^ { - 1 } q _ { 0 }$ , deriving back, we obtain the momentum mapping is invariant.

Remark 3.7. The above generating function theory can be transformed into the generating function theory on $\mathbf { g }$ (for details see literature[CS90] ). That is to say, the above generating function theory on $T ^ { * } G$ can be reformulated by the exponential mapping in terms of algebra variables, which has been done by Channell and Scovel[CS90] . Below, we list only some of their results.

For $g \in G$ , choose $\xi \in \{ \mathrm { g } \}$ , so that $g = \exp { ( \xi ) }$ . Then the LPHJ equation can be transformed into

$$
\left\{ \begin{array} { l l } { \frac { \partial s } { \partial t } + H ( - \mathbf { d } s \cdot \psi ( a d _ { \xi } ) ) = 0 , } \\ { M _ { 0 } = - \mathbf { d } s \cdot \chi ( a d _ { \xi } ) , } \\ { M = - \mathbf { d } s \cdot \psi ( a d _ { \xi } ) , } \end{array} \right.
$$

where

$$
\left\{ \begin{array} { l } { \displaystyle \chi ( a d _ { \xi } ) = \mathrm { i d } + \frac 1 2 a d _ { \xi } + \frac { 1 } { 1 2 } a d _ { \xi } ^ { 2 } + \cdots , } \\ { \displaystyle \psi ( a d _ { \xi } ) = \chi ( a d _ { \xi } ) \cdot e ^ { - a d _ { \xi } } \backsim \chi ( a d _ { \xi } ) - a d _ { \xi } , } \end{array} \right.
$$

and the condition $g = q ^ { - 1 } q _ { 0 }$ is transformed into

$$
s ( \xi , 0 ) = s _ { 0 } ( \xi ) = s _ { 0 } ( I ) ,
$$

i.e.,

$$
\xi | _ { t = 0 } = \operatorname { i d } .
$$

# 12.3.2 Construction of Lie–Poisson Schemes via Generating Function

The generating function theory to construct the symplectic scheme has been described in detail in the literatures[LQ95a,Fen86,FWQW89] . The next step is to use the generating function theory to construct the Lie–Poisson schemes. As we know, the generating function must generate identity transformation at time zero. From the previous section, the generating function should satisfy the condition (3.8), i.e., the group element becomes a unit element at $t = 0$ . We are not able to find a generating function universally applicable to a general Lie–Poisson system after a long time pursuit. Scovel[MS96] once suggested a possible solution using the Morse bundle theory. However, for the Hamilton function of quadratic form, we can find the low-order generating function. Below, we will give a brief description:

The Hamiltonian for $s o ( 3 ) ^ { * }$ is $H ( M ) = { \frac { 1 } { 2 } } M I ^ { - 1 } M .$ . From (3.6) and (3.7), using $u$ as the generating function, we have:

$$
\begin{array} { r c l } { { { \cal M } } } & { { = } } & { { - \mathrm { \bf d } u \cdot \psi ( a d _ { \xi } ) = - \mathrm { \bf d } u \left( 1 - \frac { 1 } { 2 } a d _ { \xi } + \frac { 1 } { 1 2 } a d _ { \xi } ^ { 2 } + { \cal O } ( a d _ { \xi } ^ { 3 } ) \right) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = } } & { { - \mathrm { \bf d } u + \frac { 1 } { 2 } \mathrm { \bf d } u \cdot a d _ { \xi } + { \cal O } ( a d _ { \xi } ^ { 2 } ) . } } \end{array}
$$

After substituting $H$ into Equation (3.6) and using expansion of $\psi$ , we have

$$
\begin{array} { r l } & { \displaystyle \frac { \partial u } { \partial t } + H \left( - \mathbf { d } u + \frac { 1 } { 2 } \mathbf { d } u \cdot a d _ { \xi } - O ( a d _ { x i } ^ { 2 } ) \right) } \\ & { = \displaystyle \frac { \partial u } { \partial t } + \frac { 1 } { 2 } \left( - \mathbf { d } u + \frac { 1 } { 2 } \mathbf { d } u \cdot a d _ { \xi } + O ( a d _ { \xi } ^ { 2 } ) \right) I ^ { - 1 } \left( - \mathbf { d } u + \frac { 1 } { 2 } \mathbf { d } u \cdot a d _ { \xi } + O ( a d _ { \xi } ^ { 2 } ) \right) } \\ & { = \displaystyle \frac { \partial u } { \partial t } + \frac { 1 } { 2 } I ^ { - 1 } \mathbf { d } u \mathbf { d } u - \frac { 1 } { 2 } I ^ { - 1 } \mathbf { d } u \mathbf { d } u ( a d _ { \xi } ) + O ( a d _ { \xi } ^ { 2 } ) . } \end{array}
$$

Because $\xi$ and time $\tau$ have the same order of magnitude, the Equation (3.10) can be simplified as

$$
\begin{array} { r c l } { { \displaystyle { \frac { \partial u } { \partial t } } + H ( M ) \ = \ \frac { \partial u } { \partial t } + \frac { 1 } { 2 } I ^ { - 1 } \frac { \partial u } { \partial \xi } \frac { \partial u } { \partial \xi } - \frac { 1 } { 2 } I ^ { - 1 } \frac { \partial u } { \partial \xi } \left( \frac { \partial u } { \partial \xi } a d _ { \xi } \right) + O ( \tau ^ { 2 } ) } } \\ { { \displaystyle { } } } & { { \displaystyle { } } } & { { } } \\ { { \displaystyle { } } } &  { \displaystyle { = \ \frac { \partial u } { \partial t } + \frac { 1 } { 2 } I ^ { - 1 } \frac { \partial u } { \partial \xi } \frac { \partial u } { \partial \xi } + O ( \tau ^ { 2 } ) } } \\ { { \displaystyle { } } } & { { \displaystyle { } } } & { { } } \\ { { \displaystyle { } } } & { { \displaystyle { = \ 0 . } } } \end{array}
$$

From this, we can obtain a first-order generating function. Taking

$$
u = \frac { I \xi \cdot \xi } { 2 \tau } .
$$

It can be easily verified that the Equation (3.11) satisfies (3.10) to the approximate order. Therefore, we can use $u$ to construct the Lie–Poisson scheme.

We first calculate $\xi$ by solving

$$
M _ { 0 } = - I \boldsymbol { \xi } \cdot \boldsymbol { \chi } ( \boldsymbol { \xi } ) ,
$$

and then substitute it into Equation (3.6). Next, we calculate $M = \exp { ( \xi ) } M _ { 0 }$ . On repeating this procedure, we can obtain a Lie–Poisson algorithm.

Below, we will apply this algorithm to free rigid body. For motion of the rigid body, $\chi ( \xi )$ has a closed expression (see Subsection 12.5.2). Solving nonlinear (3.12) for $\xi$ becomes a key point. It is necessary to linearize (3.12). The iterative formula for $\xi$ is

$$
\bigl ( 1 + \tau \bigl ( c _ { 1 } \widehat { \xi } - \bigl ( c _ { 3 } \xi ( \xi + c _ { 4 } ) \bigr ) ( I ^ { - 1 } \widehat { M _ { 0 } \times \xi } ) + c _ { 2 } ( \widehat { I ^ { - 1 } p _ { 0 } } ) \bigr ) \bigr ) \delta \xi = \xi _ { k + 1 } - \xi _ { k } ,
$$

where

$$
\begin{array} { l l } { { c _ { 1 } = \displaystyle \frac { 2 - | \xi | \sin | \xi | - 2 \cos | \xi | } { | \xi | ^ { 4 } } , } } & { { c _ { 2 } = \displaystyle \frac { \cos | \xi | - 1 } { | \xi | ^ { 2 } } , \nonumber } } \\ { { c _ { 3 } = \displaystyle \frac { - 2 | \xi | - | \xi | \cos | \xi | + 3 \sin | \xi | } { | \xi | ^ { 5 } } , } } & { { c _ { 4 } = \displaystyle \frac { 2 | \xi | - \sin | \xi | } { | \xi | ^ { 3 } } . } } \end{array}
$$

In fact, the above algorithm is applicable even when $H$ is a polynomial.

Ge–Marsden[GM88] have proposed an algorithm, which neglects the generating function condition (3.8). Therefore, it has certain flaw. Below, we will explain it from the theoretical point of view.

First, we should point out that the Ge–Marsden algorithm can only give the firstorder scheme for simple system such as the free rigid body. Its second-order scheme, however, is not a second-order approximation to the original system, as we will prove it below.

Generally speaking, a generating function can be given as the following equation

$$
u = u _ { 0 } + \sum _ { n = 1 } ^ { \infty } \frac { ( \delta t ) ^ { n } } { n ! } u _ { n } ,
$$

where $u _ { 0 } = { \frac { ( \xi , \xi ) } { 2 } }$ generates the identical transformation at time $t = 0$ . Substituting (3.13) into the LPHJ equation, we have

$$
u _ { 1 } = - H ( V ) , \quad u _ { 2 } = \frac { \partial H } { \partial V } \cdot \mathrm { d } u _ { 1 } \cdot \psi ( a d _ { \xi } ) , \cdot \cdot \cdot .
$$

Below, we will take $s o ( 3 ) ^ { * }$ as an example to explain the flaw of this algorithm.

For $s o ( 3 ) ^ { * }$ , $u _ { 0 } = \frac { \xi ^ { 2 } } { 2 }$ , and hence $V = \xi$ . The first-order scheme is

$$
S _ { 1 } = u _ { 0 } + \tau u _ { 1 } = \frac { \xi ^ { 2 } } { 2 } - \tau H ( \xi ) = \frac { \xi ^ { 2 } } { 2 } - \frac { \tau } { 2 } \xi I ^ { - 1 } \xi .
$$

The generating function for the second-order scheme is

$$
\begin{array} { r c l } { { } } & { { } } & { { S _ { 2 } ~ = ~ S _ { 1 } + \displaystyle \frac { \tau ^ { 2 } } { 2 } u _ { 2 } = \displaystyle \frac { \xi ^ { 2 } } { 2 } - \tau H ( \xi ) + \displaystyle \frac { \tau ^ { 2 } } { 2 } \frac { \partial H } { \partial V } \cdot \mathrm { d } u _ { 1 } \cdot \psi ( a d _ { \xi } ) } } \\ { { } } & { { } } & { { ~ = ~ \displaystyle \frac { \xi ^ { 2 } } { 2 } - \displaystyle \frac { \tau } { 2 } \xi I ^ { - 1 } \xi - \displaystyle \frac { \tau ^ { 2 } } { 2 } I ^ { - 1 } \xi \big ( I ^ { - 1 } \xi \cdot \psi ( \xi ) \big ) . } } \end{array}
$$

Using the system of Equation (3.6) (for $S O ( 3 ) \ M , M _ { 0 }$ denote angular momentum), we get:

$$
M - M _ { 0 } = - \mathrm { d } u \cdot a d _ { \xi } .
$$

Next, we will prove that $S _ { 1 }$ indeed generates a first-order Lie–Poisson scheme to the Euler equation. However, $S _ { 2 }$ actually is not a second-order approximation to the Euler equation. Furthermore, we will find that with this algorithm, it is impossible to construct difference scheme that preserves the momentum mapping.

Because

$$
\mathbf { d } S _ { 1 } = \mathbf { d } \left( \frac { \xi ^ { 2 } } { 2 } - \frac { \tau } { 2 } \xi \cdot I ^ { - 1 } \xi \right) = \xi - \tau I ^ { - 1 } \xi
$$

and $M _ { 0 } = - \mathrm { d } S _ { 1 } \cdot \chi ( a d _ { \xi } ) = ( - \xi + \tau I ^ { - 1 } \xi ) \cdot \chi ( \xi )$ , we have $\xi = - M _ { 0 } + O ( \tau )$ . By Equation (3.15) and applying $\xi \cdot a d _ { \xi } = 0$ , we obtain

$$
\begin{array} { l } { M - M _ { 0 } ~ = ~ ( \xi - \tau I ^ { - 1 } \xi ) \cdot a d _ { \xi } = - \tau I ^ { - 1 } \xi \cdot a d _ { \xi } } \\ { ~ = ~ \tau [ \xi , I ^ { - 1 } \xi ] = \tau [ - M _ { 0 } + O ( \tau ) , I ^ { - 1 } ( - M _ { 0 } + O ( \tau ) ) ] } \\ { ~ = ~ \tau [ M _ { 0 } , I ^ { - 1 } M _ { 0 } ] + O ( \tau ^ { 2 } ) . } \end{array}
$$

This is a first-order approximation to the Euler equation

$$
\begin{array} { r } { \dot { M } = [ M , I ^ { - 1 } M ] . } \end{array}
$$

For the second-order generating function $S _ { 2 }$ , we first calculate $\chi ( \xi )$ . Let $\chi ( \xi ) =$ $1 + a _ { 1 } \xi + a _ { 2 } \xi ^ { 2 }$ , where $a _ { 1 } , a _ { 2 }$ have closed analytical expression (see Subsection 12.5.2) as follows

$$
\begin{array} { l } { \displaystyle a _ { 1 } = \frac { 1 - \cos | \xi | } { \sin ^ { 2 } | \xi | + ( 1 - \cos | \xi | ) ^ { 2 } } , } \\ { \displaystyle a _ { 2 } = \frac { \frac { ( \cos | \xi | - 1 ) ^ { 2 } } { | \xi | ^ { 2 } } + \frac { \sin | \xi | - | \xi | } { | \xi | } + ( \sin | \xi | - | \xi | ) | \xi | } { \sin ^ { 2 } | \xi | + ( 1 - \cos | \xi | ) ^ { 2 } } , } \end{array}
$$

therefore,

$$
\begin{array} { l } { { u _ { 2 } ~ = ~ - I ^ { - 1 } \xi ( I ^ { - 1 } \xi \cdot \psi ( \xi ) ) } } \\ { { { } } } \\ { { { } } } \\ { { { } = ~ - \langle I ^ { - 1 } \xi , I ^ { - 1 } \xi \rangle - a _ { 2 } I ^ { - 1 } \xi ( I ^ { - 1 } \xi \cdot \xi ^ { 2 } ) , } } \end{array}
$$

then

$$
\begin{array} { r } { \textrm { d } S _ { 2 } = \xi - \tau I ^ { - 1 } \xi - \tau ^ { 2 } ( I ^ { - 1 } ) ^ { 2 } \xi - \frac { \tau ^ { 2 } } { 2 } \textrm { d } \big ( a _ { 2 } I ^ { - 1 } \xi \cdot ( I ^ { - 1 } \xi \cdot \xi ^ { 2 } ) \big ) , } \end{array}
$$

by

$$
M _ { 0 } = - \mathbf { d } S _ { 2 } \cdot \chi ( \xi ) = - \xi + \tau \xi \cdot \chi ( \xi ) + O ( \tau ^ { 2 } ) ,
$$

we have

$$
\xi = - M _ { 0 } + \tau \xi \cdot \chi ( \xi ) + O ( \tau ^ { 2 } ) .
$$

From Equation (3.15), we get

$$
\begin{array} { r l } { M - M _ { 0 } \ = \ - { \mathrm { d } } S _ { 2 } \cdot a d _ { \xi } } \\ { \ } & { \ - ( \xi - { \tau } { I ^ { - 1 } } \xi - { \tau } ^ { 2 } ( \ \widehat { I ^ { - 1 } \xi } ) ^ { 2 } - \frac { { \tau } ^ { 2 } } { 2 } { \mathrm { d } } ( a _ { 2 } { I ^ { - 1 } } \xi \cdot ( { I ^ { - 1 } } \xi \cdot \widehat { \xi ^ { 2 } } ) ) ) \cdot \widehat { \xi } } \\ { \ } & { \ = \ \tau [ M _ { 0 } , I ^ { - 1 } M _ { 0 } ] + a _ { 1 } \tau ^ { 2 } \big ( [ [ M _ { 0 } , I ^ { - 1 } M _ { 0 } ] , I ^ { - 1 } M _ { 0 } ] } \\ & { \ + [ M _ { 0 } , I ^ { - 1 } [ M _ { 0 } , I ^ { - 1 } M _ { 0 } ] ] \big ) } \\ & { \ + a _ { 2 } \big ( I ^ { - 1 } M _ { 0 } ( I ^ { - 1 } M _ { 0 } \cdot \widehat { M _ { 0 } ^ { 2 } } ) + I ^ { - 1 } ( I ^ { - 1 } M _ { 0 } \cdot \widehat { M _ { 0 } ^ { 2 } } ) M _ { 0 } \big ) } \\ & { \ - \frac { \tau ^ { 2 } } { 2 } { \mathrm { d } } \big ( a _ { 2 } \cdot I ^ { - 1 } \xi ( I ^ { - 1 } \xi \cdot \widehat { \xi ^ { 2 } } ) \big ) \cdot \widehat { \xi } + O ( \tau ^ { 3 } ) . } \end{array}
$$

According to the Euler equation (3.16), its second-order approximation should be

$$
\begin{array} { r l } { M - M _ { 0 } = } & { \tau [ M _ { 0 } , I ^ { - 1 } M _ { 0 } ] + \frac { \tau ^ { 2 } } { 2 } ( [ [ M _ { 0 } , I ^ { - 1 } M _ { 0 } ] , I ^ { - 1 } M _ { 0 } ] } \\ & { + [ M _ { 0 } , I ^ { - 1 } [ I ^ { - 1 } M _ { 0 } , M _ { 0 } ] ] ) + O ( \tau ^ { 3 } ) . } \end{array}
$$

As $t  0 , \xi  M _ { 0 }$ , by comparison, we found that the Equation (3.17) is not an approximation to the Equation (3.18). Therefore, the generating function $S _ { 2 }$ cannot generate the second-order approximation to the Euler equation.

We have shown that $S _ { 1 }$ generates a first-order Lie–Poisson scheme. However, a momentum mapping preserving scheme should satisfy $J _ { L } ( q , M ) = J _ { L } ( q _ { 0 } , M _ { 0 } )$ . For $T ^ { * } S O ( 3 )$ , this becomes $q M = q _ { 0 } M _ { 0 }$ , and hence $M = q ^ { - 1 } q _ { 0 } M _ { 0 }$ . Therefore, it is necessary to estimate $q \in G$ . If we had formula $M = g M _ { 0 }$ , a very natural idea is to make $g = q ^ { - 1 } q _ { 0 }$ , which leads to $q = q _ { 0 } g ^ { - 1 }$ . An algorithm well constructed on $s o ( 3 ) ^ { * }$ should lead to a good approximation of $q \in S O ( 3 )$ to equation of motion. The scheme that satisfies Equations (3.6) and the condition (3.8) and is generated by our generating function theory that belongs to this type. However, the scheme constructed via algorithm[GM88] does not belong to this type. Because the condition (3.8) is neglected, it is impossible to construct the algorithm on $G$ using algorithm[GM88] . This can be illustrated as follows.

Using another representation of (3.6)

$$
M _ { 0 } = - \mathsf { d } u \cdot \chi ( a d _ { \xi } ) , \quad M = \exp { ( a d _ { \xi } ) } M _ { 0 } ,
$$

and $\xi = ( - M _ { 0 } + \tau I ^ { - 1 } \xi ) \cdot \chi ( \xi )$ , if we let $q = q _ { 0 } g ^ { - 1 } = q _ { 0 } \exp \left( - \xi \right) = q _ { 0 } \exp \left( \left( M _ { 0 } - \right. \right.$ $\tau I ^ { - 1 } \xi ) \cdot \chi ( \xi ) )$ , then $q$ is not a first-order approximation to the equation of motion ${ \dot { q } } =$ $q I ^ { - 1 } \widehat { M }$ . In fact, the algorithm[GM88] cannot produce the form of $q$ alone to construct momentum mapping preserving scheme.

# 12.4 Construction of Structure Preserving Schemes for Rigid Body

We have already introduced the equation of motion for generalized rigid body in previous section. In this section, we will take $S O ( 3 )$ as an example to explain how to construct structure-preserving schemes.

# 12.4.1 Rigid Body in Euclidean Space

Let $\Lambda ( t ) \in S O ( 3 )$ , such that $\Lambda ( t ) \Lambda ( t ) ^ { \mathrm { T } } = I$ , $| \Lambda ( t ) | = 1$ . Then the equation of motion for the free rigid body can be formulated as

$$
\dot { \Lambda } ( t ) = \Lambda ( t ) \widehat { W } ( t ) ,
$$

where $\widehat { W } ( t ) \in s o ( 3 )$ , $s o ( 3 )$ is the Lie algebra of $S O ( 3 )$ . The isomorphism relation, $s o ( 3 ) \simeq \mathbf { R } ^ { 3 }$ , can be realized through the following equations:

$$
\begin{array} { r l } & { \widehat { W } ( t ) \simeq W ( t ) \in { \bf R } ^ { 3 } , } \\ & { \left[ \begin{array} { c c c } { 0 } & { - w _ { 3 } } & { w _ { 2 } } \\ { w _ { 3 } } & { 0 } & { - w _ { 1 } } \\ { - w _ { 2 } } & { w _ { 1 } } & { 0 } \end{array} \right] \simeq \left[ \begin{array} { c } { w _ { 1 } } \\ { w _ { 2 } } \\ { w _ { 3 } } \\ { w _ { 3 } } \end{array} \right] , } \end{array}
$$

$$
\widehat W ( t ) \cdot a = W \times a , \quad a \in { \bf R } ^ { 3 } .
$$

The $\widehat W ( t )$ in Equation (4.1) is called angular velocity in the body description. $\widehat { W } ( t ) =$ $\Lambda ( t ) ^ { - 1 } \dot { \Lambda } ( t )$ is consistent with the definition of generalized rigid body. The corresponding Euler equation is

$$
\dot { M } = [ M , W ] , \quad M = J W ,
$$

where $J$ is called inertia operator, $M$ the body angular momentum. The body variables and the spatial variables have the following relations:

$$
\left\{ \begin{array} { l } { \omega = A W , } \\ { m = \Lambda M , \quad \widehat { \omega } = \Lambda \widehat { W } \Lambda ^ { \mathrm { T } } \Longrightarrow \omega = \Lambda W , } \\ { a = \Lambda A , } \end{array} \right.
$$

here $A$ is an acceleration.

Operator “  ” has the following equalities:

$$
\begin{array} { r c l } { \widehat { \boldsymbol { u } \times \boldsymbol { v } } } & { = } & { [ \widehat { \boldsymbol { u } } , \widehat { \boldsymbol { v } } ] , } \\ { \widehat { \boldsymbol { u } } \cdot \boldsymbol { v } } & { = } & { \boldsymbol { u } \times \boldsymbol { v } , } \\ { \widehat { \boldsymbol { \left[ u , \widehat { \boldsymbol { v } } \right] } \cdot \boldsymbol { w } } } & { = } & { \left( \boldsymbol { u } \times \boldsymbol { v } \right) \times \boldsymbol { w } , } \\ { \boldsymbol { u } \cdot \boldsymbol { v } } & { = } & { \frac { 1 } { 2 } \mathrm { t r } \left( \widehat { u } \widehat { \boldsymbol { v } } \right) . } \end{array}
$$

The equation of motion of the rigid body may be expressed on space $S U ( 2 )$ or $S H _ { 1 }$ (unit quaternion). Applying their equivalence (their Lie algebra is isomorphism), we may obtain different forms of the Equation (4.1) under $S U ( 2 )$ and $S H _ { 1 }$ .

$S U ( 2 )$ : $U \in S U ( 2 )$ , satisfies

$$
\begin{array} { r } { \begin{array} { r } { U U ^ { * } = I , \quad | U | = 1 . } \end{array} } \end{array}
$$

The equation of motion becomes

$$
\dot { U } = U \Omega _ { u } ,
$$

where $\Omega _ { u } = U ^ { * } U \in s u ( 2 )$ , satisfies $\Omega _ { u } + \Omega _ { u } ^ { * } = 0$ , tr $\Omega _ { u } = 0$ . In $s u ( 2 )$ , we choose

$$
\{ ( - \mathrm { i } \sigma _ { 1 } ) , ( - \mathrm { i } \sigma _ { 2 } ) , ( - \mathrm { i } \sigma _ { 3 } ) \}
$$

as a basis, where

$$
\begin{array} { r l } & { \sigma _ { 1 } = \left[ \begin{array} { l l } { 0 } & { 1 } \\ { } & { } \\ { 1 } & { 0 } \end{array} \right] , \quad \sigma _ { 2 } = \left[ \begin{array} { l l } { 0 } & { - \mathbf { i } } \\ { } & { } \\ { \mathbf { i } } & { 0 } \end{array} \right] } \\ & { \sigma _ { 3 } = \left[ \begin{array} { l l } { 1 } & { 0 } \\ { } & { } \\ { 0 } & { - 1 } \end{array} \right] , \quad \sigma _ { 0 } = \left[ \begin{array} { l l } { 1 } & { 0 } \\ { } & { } \\ { 0 } & { 1 } \end{array} \right] } \end{array}
$$

are 4 Pauli matrices.

It is easy to see that

$$
\sum _ { i = 1 } ^ { 3 } \omega _ { i } \sigma _ { i } = \left[ \begin{array} { c c } { - \mathrm { i } \omega _ { 3 } } & { - \omega _ { 2 } - \mathrm { i } \omega _ { 1 } } \\ { } & { } \\ { \omega _ { 2 } - \mathrm { i } \omega _ { 1 } } & { \mathrm { i } \omega _ { 3 } } \end{array} \right] \in S U ( 2 ) .
$$

Hence

$$
\Omega _ { u } = ( \omega _ { 1 } , \omega _ { 2 } , \omega _ { 3 } ) \in s u ( 2 ) \simeq \mathbf { R } ^ { 3 } \simeq s o ( 3 ) ,
$$

using the matrix notation, rewrite the equation:

$$
\left[ \begin{array} { c c } { \dot { \sigma } } & { \dot { \beta } } \\ { \dot { \gamma } } & { \dot { \delta } } \end{array} \right] = \left[ \begin{array} { c c } { \sigma } & { \beta } \\ { \gamma } & { \delta } \end{array} \right] \left[ \begin{array} { c c } { - \mathrm { i } \omega _ { 3 } } & { - \omega _ { 2 } - \mathrm { i } \omega _ { 1 } } \\ { \omega _ { 2 } - \mathrm { i } \omega _ { 1 } } & { \mathrm { i } \omega _ { 3 } } \end{array} \right] .
$$

$\forall Q \in S H _ { 1 }$ , $\| Q \| = 1$ , $Q = ( q _ { 0 } , q _ { 1 } , q _ { 2 } , q _ { 3 } ) \in H$ (set of all quaternion). The equation of motion becomes $\dot { Q } = Q \Omega _ { h }$ , where $\ddot { \Omega _ { h } } = \overline { { Q } } \dot { Q } = Q ^ { - 1 } \dot { Q } \in s h _ { 1 }$ (quaternion with zero real part). Let

$$
\begin{array} { r } { \Omega _ { h } = \omega _ { 1 } i + \omega _ { 2 } j + \omega _ { 3 } k = ( 0 , \omega _ { 1 } , \omega _ { 2 } , \omega _ { 3 } ) , \quad \omega _ { h } = ( \omega _ { 1 } , \omega _ { 2 } , \omega _ { 3 } ) . } \end{array}
$$

Rewrite the equation of motion into the quaternion form

$$
\begin{array} { r c l } { ( \dot { q } _ { 0 } , \dot { q } _ { 1 } , \dot { q } _ { 2 } , \dot { q } _ { 3 } ) } & { = } & { ( q _ { 0 } , q _ { 1 } , q _ { 2 } , q _ { 3 } ) \cdot ( 0 , \omega _ { 1 } , \omega _ { 2 } , \omega _ { 3 } ) } \\ & & { \implies \left\{ \begin{array} { l } { \dot { q } _ { 0 } = - q \omega = - ( q , \omega ) , } \\ { \dot { q } = q _ { 0 } \omega ^ { \mathrm { T } } + q \widehat { \omega } , } \end{array} \right. \quad q = ( q _ { 1 } , q _ { 2 } , q _ { 3 } ) . } \end{array}
$$

The Euler equation of motion becomes

$$
\begin{array} { l l l } { { s o _ { 3 } ^ { * } : } } & { { \cfrac { \mathrm { d } M } { \mathrm { d } t } = [ M , W ] ; } } & { { } } \\ { { } } & { { } } & { { } } \\ { { s u _ { 2 } ^ { * } : } } & { { \cfrac { \mathrm { d } M _ { u } } { \mathrm { d } t } = \cfrac 1 2 [ M _ { u } , W _ { u } ] = [ M _ { u } , W ] , } } & { { M _ { u } = 2 M , \quad \omega _ { u } = \cfrac 1 2 W ; } } \\ { { } } & { { } } & { { } } \\ { { s h _ { 1 } ^ { * } : } } & { { \cfrac { \mathrm { d } M _ { h } } { \mathrm { d } t } = \cfrac 1 2 [ M _ { h } , W _ { h } ] = [ M _ { h } , W ] , } } & { { M _ { h } = 2 M , \quad \omega _ { h } = \cfrac 1 2 W . } } \end{array}
$$

If the unified Euler equation of motion is used, we have

$$
{ \frac { \mathrm { d } { \cal M } } { \mathrm { d } t } } = [ { \cal M } , { \cal W } ] .
$$

If $\omega$ is assigned using the values of $S O ( 3 )$ , then the corresponding equation of motion becomes:

$$
\begin{array} { r l } & { \dot { \Lambda } = \Lambda \widehat { W } ( t ) , ~ W ( t ) = ( \omega _ { 1 } , \omega _ { 2 } , \omega _ { 3 } ) , } \\ & { \dot { Q } = Q \Omega _ { h } , ~ \Omega _ { h } = \left( 0 , \frac { \omega _ { 1 } } { 2 } , \frac { \omega _ { 2 } } { 2 } , \frac { \omega _ { 3 } } { 2 } \right) , } \\ & { \dot { U } = U \Omega _ { u } , ~ \Omega _ { u } = \left( \frac { \omega _ { 1 } } { 2 } , \frac { \omega _ { 2 } } { 2 } , \frac { \omega _ { 3 } } { 2 } \right) . } \end{array}
$$

After the above transformation, the equation of motion becomes more simpler. The number of unknowns become fewer from the original 9 $( S O ( 3 ) )$ to 4 complex variables $( S U ( 2 ) )$ ), and then reduced to 4 real variables $( S H _ { 1 } )$ . The computation storage and operation may be sharply reduced for large-scale scientific computations.

More details about the relations among $S O ( 3 )$ , $S U ( 2 )$ and $S H _ { 1 }$ will be given in Section 12.5.

# 12.4.2 Energy-Preserving and Angular Momentum-Preserving Schemes for Rigid Body

With the equation of motion of rigid body, we may construct the corresponding difference scheme[LQ95a] . One type of important schemes is the structure-preserving scheme. Structure-preserving may have some different meaning for different systems. For example, it could mean to preserve the original system’s physical structure, the symmetry, or invariant physical quantities.

The total energy and the angular momentum, especially the angular momentum, are important invariants for the rigid motion. Many experiments indicated that the energy and the angular momentum can be well maintained, which is essential for computer simulation to have a good approximation to the real motion.

The equation of motion for the rigid body is

$$
\left\{ \begin{array} { l } { \dot { \Lambda } ( t ) = \Lambda ( t ) \widehat { W } ( t ) , } \\ { \dot { M } ( t ) = M ( t ) \times W ( t ) } \\ { M ( t ) = I \cdot W ( t ) } \end{array} \right\} \Longrightarrow I \cdot \dot { W } ( t ) = I W ( t ) \times W ( t ) ,
$$

where $I$ is the inertia operator.

Note that the energy function $H = \frac { 1 } { 2 } ( M ( t ) , W ( t ) ) = \frac { 1 } { 2 } \widehat { W } ( t ) J \widehat { W } ( t )$ is a Hamiltonian function and the spatial angular momentum $M ( t ) { \overline { { \ } } } = \Lambda M ( t ) \Leftrightarrow { \widehat { M } } ( t ) =$ $\Lambda \widehat { M } ( t ) \Lambda ( t ) ^ { \mathrm { T } }$ becomes momentum mapping. To maintain the energy and the angular momentum invariant is just to maintain the Hamilton function and the momentum mapping of the Lie–Poisson system invariant.

The energy invariance is mainly manifested in solving Euler equations, and the angular momentum invariance concerns more with equations of motion on $S O ( 3 )$ . Using relation $\Lambda _ { n + 1 } M _ { n + 1 } \ = \ \Lambda _ { n } M _ { n }$ , we can derive the formula for which $\Lambda _ { n + 1 }$ should satisfy. For Euler equation $\dot { M } ( t ) = M ( t ) \times W ( t ) = M ( t ) \times I ^ { - 1 } M ( t )$ , the midpoint scheme preserves the Hamiltonian function, i.e., it is energy-preserving (in fact midpoint scheme preserves all functions of quadratic form).

The midpoint scheme for Euler equation is

$$
\frac { M _ { n + 1 } - M _ { n } } { \delta t } = \frac { M _ { n + 1 } + M _ { n } } { 2 } \times I \frac { M _ { n + 1 } + M _ { n } } { 2 } ,
$$

multiply $I ^ { - 1 } { \frac { M _ { n + 1 } + M _ { n } } { 2 } }$ via inner product on both sides,

$$
\left( M _ { n + 1 } - M _ { n } \right) \cdot ( I ^ { - 1 } ( M _ { n + 1 } + M _ { n } ) ) = 0 \Longrightarrow I ^ { - 1 } M _ { n + 1 } \cdot M _ { n + 1 } = I ^ { - 1 } M _ { n } \cdot M _ { n } ,
$$

i.e., $H _ { n + 1 } = H _ { n }$ . Since $I ^ { - 1 }$ is a symmetric operator, we have

$$
M _ { n } \cdot I ^ { - 1 } M _ { n + 1 } = M _ { n + 1 } \cdot I ^ { - 1 } M _ { n } .
$$

Rewrite scheme (4.3) into

$$
\begin{array} { l c l } { { M _ { n + 1 } } } & { { = } } & { { M _ { n } + \displaystyle \frac { \delta t } { 4 } ( M _ { n + 1 } + M _ { n } ) \times I ^ { - 1 } ( M _ { n + 1 } + M _ { n } ) } } \\ { { } } & { { \Longrightarrow } } & { { \left( I + \displaystyle \frac { \delta t } { 4 } I ^ { - 1 } ( M _ { n + 1 } + M _ { n } ) \right) M _ { n + 1 } = \left( I - \displaystyle \frac { \delta t } { 4 } I ^ { - 1 } ( \displaystyle \widehat { M _ { n + 1 } + M _ { n } } ) \right) M _ { n } } } \\ { { } } & { { \Longrightarrow } } & { { M _ { n + 1 } = \left( I + \displaystyle \frac { \delta t } { 4 } I ^ { - 1 } ( \displaystyle \widehat { M _ { n + 1 } + M _ { n } } ) \right) ^ { - 1 } \left( I - \displaystyle \frac { \delta t } { 4 } I ^ { - 1 } ( \displaystyle \widehat { M _ { n + 1 } + M _ { n } } ) \right) M _ { n } , } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = } } & { { \Lambda _ { n + 1 } ^ { - 1 } \Lambda _ { n } M _ { n } . } } \end{array}
$$

By conservation of angular momentum:

$$
\Lambda _ { n + 1 } M _ { n + 1 } = \Lambda _ { n } M _ { n } .
$$

By comparison, we obtain

$$
\Lambda _ { n + 1 } = \Lambda _ { n } \bigg ( I - \frac { \delta t } { 4 } I ^ { - 1 } \big ( \widehat { M _ { n + 1 } + M _ { n } } \big ) \bigg ) ^ { - 1 } \bigg ( I + \frac { \delta t } { 4 } I ^ { - 1 } \big ( \widehat { M _ { n + 1 } + M _ { n } } \big ) \bigg ) .
$$

Since

$$
\frac { \delta t } { 4 } I ^ { - 1 } ( M _ { n + 1 } + M _ { n } ) = \frac { \delta t } { 2 } W _ { n } + O ( \delta t ^ { 2 } ) ,
$$

from Cayley transformation, we know this is a second-order approximation to equation $\dot { \Lambda } = \Lambda \widehat { W }$ .

In brief, if we construct an energy-preserving scheme on $s o ( 3 ) ^ { * }$ , we may obtain a scheme approximate to the equation of motion by using the conservation of an angular momentum. We remark that this highly depends on the schemes constructed on $s o ( 3 ) ^ { * }$ . Not every scheme on $s o ( 3 ) ^ { * }$ corresponds to a good approximation scheme to the equation of motion on $S O ( 3 )$ . Ge–Marsden algorithm for Lie–Poisson system is a typical example.

# 12.4.3 Orbit-Preserving and Angular-Momentum-Preserving Explicit Scheme

The orbit-preserving $\mathrm { [ L O 9 5 a ] }$ here means the motion trajectory remains at coadjoint orbit. For rigid body this means in every time step

$$
M _ { n + 1 } = \Lambda _ { n } M _ { n } , \exists \Lambda _ { n } \in S O ( 3 ) .
$$

The midpoint scheme constructed in (4.2) is a kind of implicit orbit-preserving scheme. Below, we will derive explicit orbit-preserving schemes.

The equation is

$$
\dot { M } = M \times W = - W \times M = - \widehat { W } \cdot M , \quad \widehat { W } \in S O ( 3 ) , \quad \widehat { W } = I ^ { - 1 } M .
$$

Assume the difference scheme to be constructed has the form

$$
M _ { n + 1 } = \exp { ( b ( \delta t ) ) } M _ { n } .
$$

It is easy to see when $b ( \delta t ) = - \delta t W _ { n } = - \delta t ( I ^ { - 1 } M _ { n } )$ , (4.4) is a first-order scheme. Expanding the scheme (4.4), we obtain

$$
M _ { n + 1 } = M _ { n } + b ( \delta t ) M _ { n } + \frac { 1 } { 2 } \big ( b ( \delta t ) \big ) ^ { 2 } M _ { n } + \frac { 1 } { 3 ! } \big ( b ( \delta t ) \big ) ^ { 3 } M _ { n } + \cdots .
$$

Using Taylor expansion, we have

$$
\begin{array} { r c l } { { } } & { { } } & { { M _ { n + 1 } ~ = ~ M _ { n } - \delta t \widehat W _ { n } M _ { n } + \Big ( \frac { \ddot { M } } { 2 } \Big ) \delta t ^ { 2 } + \Big ( \frac { M ^ { ( 3 ) } } { 3 ! } \Big ) \delta t ^ { 3 } + \cdots } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = ~ M _ { n } - \delta t \widehat W _ { n } M _ { n } + \frac { \delta t ^ { 2 } } { 2 } ( M _ { n } \times W _ { n } \times W _ { n } ) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { + \frac { \delta t ^ { 2 } } { 2 } \big ( M _ { n } \times I ^ { - 1 } ( M _ { n } \times W _ { n } ) \big ) + \cdots . } } \end{array}
$$

Let

$$
b ( \delta t ) = \delta t B _ { 1 } + \delta t ^ { 2 } B _ { 2 } + \delta t ^ { 3 } B _ { 3 } + \cdots ,
$$

substitute it into (4.5), and retain only the first two terms

$$
\begin{array} { r c l } { { { \cal M } _ { n + 1 } } } & { { = } } & { { { \cal M } _ { n } + \delta t B _ { 1 } { \cal M } _ { n } + \delta t ^ { 2 } B _ { 2 } { \cal M } _ { n } + \displaystyle \frac { 1 } { 2 } ( \delta t B _ { 1 } + \delta t ^ { 2 } B _ { 2 } ) ^ { 2 } { \cal M } _ { n } + o ( \delta t ^ { 3 } ) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = } } & { { { \cal M } _ { n } + \delta t B _ { 1 } { \cal M } _ { n } + \delta t ^ { 2 } B _ { 2 } { \cal M } _ { n } + \displaystyle \frac { 1 } { 2 } \delta t ^ { 2 } B _ { 1 } ^ { 2 } { \cal M } _ { n } + o ( \delta t ^ { 3 } ) . } } \end{array}
$$

Comparing the coefficients of Equation (4.6) with those of (4.7), we have

$$
\begin{array} { r c l } { { } } & { { B _ { 1 } } } & { { = } } & { { - \widehat { W } _ { n } , } } \\ { { } } & { { } } & { { } } \\ { { ( B _ { 1 } ^ { 2 } + 2 B _ { 2 } ) M _ { n } } } & { { = } } & { { ( M _ { n } \times W _ { n } \times W _ { n } ) + ( M _ { n } \times I ^ { - 1 } ( M _ { n } \times W _ { n } ) ) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = } } & { { \widehat { W } _ { n } ^ { 2 } M _ { n } - \left( I ^ { - 1 } ( \widehat { M _ { n } \times W _ { n } } ) \right) M _ { n } , } } \end{array}
$$

then

$$
\begin{array} { l } { { \displaystyle B _ { 1 } = - \widehat { W } _ { n } , } } \\ { { \displaystyle B _ { 2 } = - \frac { 1 } { 2 } \big ( I ^ { - 1 } ( \widehat { M _ { n } \times W _ { n } } ) \big ) . } } \end{array}
$$

Likewise, we can construct third or fourth order schemes. Here we give only the result

$$
\begin{array} { r c l } { { { \cal B } _ { 3 } } } & { { = } } &  { \frac 1 6 \widehat { \displaystyle ( W \big ( I ^ { - 1 } ( { \widehat { \cal M } } \times { \hat { \cal W } } ) \big ) \big ) + 2 I ^ { - 1 } ( { \widehat { \cal M } } \times { \hat { \cal W } } ) { \widehat { \cal W } } + I ^ { - 1 } ( { \cal M } \widehat { \times { \hat { \cal W } } \times { \cal W } } ) } } \\ { { } } & { { } } & { { { } } } \\ { { } } & { { } } & { { + \big ( I ^ { - 1 } \big ( { \cal M } \times { \widehat { \ I ^ { - 1 } ( { \cal M } } \times { \cal W } ) } \big ) \big ) - \frac 1 2 B _ { 1 } B _ { 2 } - \frac 1 2 B _ { 2 } B _ { 1 } . } } \end{array}
$$

Another way to construct the orbit-preserving scheme is the modified R–K method, which can be described as follows.

If the initial value $M _ { 0 }$ is known, let:

$$
\begin{array} { r l } & { \mu _ { 0 } = M _ { 0 } , } \\ & { \mu _ { 1 } = \mathrm { { e } } ^ { \tau c _ { 1 0 } ( - \widehat { I ^ { - 1 } \mu _ { 0 } } ) } M _ { 0 } , } \\ & { \mu _ { 2 } = \mathrm { { e } } ^ { \tau c _ { 2 1 } ( - \widehat { I ^ { - 1 } \mu _ { 1 } } ) } \mathrm { { e } } ^ { \tau c _ { 2 0 } ( - \widehat { I ^ { - 1 } \mu _ { 0 } } ) } M _ { 0 } , } \\ & { \qquad \cdots } \\ & { \mu _ { r } = \mathrm { { e } } ^ { \tau c _ { r , r - 1 } ( - \widehat { I ^ { - 1 } \mu _ { r - 1 } } ) } \mathrm { { e } } ^ { \tau c _ { r , r - 2 } ( - \widehat { I ^ { - 1 } \mu _ { r - 2 } } ) } \cdots \mathrm { { e } } ^ { \tau c _ { r , 0 } ( - \widehat { I ^ { - 1 } \mu _ { 0 } } ) } M _ { 0 } , } \end{array}
$$

the $( r + 1 )$ -th order approximation of the equation is

$$
M = \mathrm { e } ^ { \tau c _ { r } ( - \widehat { I ^ { - 1 } \mu _ { r } } ) } \mathrm { e } ^ { \tau c _ { r - 1 } ( - \widehat { I ^ { - 1 } \mu _ { r - 1 } } ) } \cdot \cdot \cdot \mathrm { e } ^ { \tau c _ { 0 } ( - \widehat { I ^ { - 1 } \mu _ { 0 } } ) } M _ { 0 } .
$$

Comparing the coefficients between the above equation and the Taylor expansion (4.6), we obtain $c _ { i j }$ and $c _ { s }$ . Take $r = 1$ as an example.

$$
\begin{array} { r l } & { \mathrm { ( s u r e ) } } \\ & { \mathrm { ( a s u r e ) } } \\ & { = \left( \begin{array} { c c } { 1 } & { r _ { 1 } } \\ { - r _ { 2 } } \\ { 0 } & { 1 } \end{array} \right) \left( \begin{array} { c c } { 0 } & { 0 } \\ { r _ { 2 } } \end{array} \right) \mathrm { ( } A r _ { 1 } - r _ { 1 } } \\ { 0 } & { 0 } \\ { 0 } & { 0 } \end{array} \right)  \\ & { \quad = \left( \begin{array} { c c } { 0 } & { 1 } \\ { 1 } & { - r _ { 2 } A _ { 1 } ^ { - 1 } r _ { 2 } } \end{array} \right) \left( \begin{array} { c c } { 0 } & { 0 } \\ { \overline { { A } } _ { 2 1 } ^ { - 1 } } & { 0 } \\ { 0 } & { 1 } \end{array} \right) \left( \begin{array} { c c } { 0 } & { 0 } \\ { 0 } & { 1 } \end{array} \right) } \\ & { \quad = \left( \begin{array} { c c } { 0 } & { 0 } \\ { 1 } & { - r _ { 2 } A _ { 1 } ^ { - 1 } r _ { 1 } } \end{array} \right) \left( \begin{array} { c c } { 0 } & { 0 } \\ { 0 } & { 1 } \end{array} \right) \left( \begin{array} { c c } { 1 } & { 0 } \\ { 0 } & { 1 } \end{array} \right) } \\ & { \quad = \left( \begin{array} { c c } { 0 } & { 0 } \\ { 1 } & { 0 } \end{array} \right) \left( \begin{array} { c c } { 1 } & { 0 } \\ { 0 } & { 1 } \end{array} \right) \left( \begin{array} { c c } { 0 } & { 0 } \\ { 0 } & { 1 } \end{array} \right) } \\ & { \quad = \left( \begin{array} { c c } { 0 } & { 0 } \\ { 0 } & { 1 } \end{array} \right) \left( \begin{array} { c c } { 1 } & { 0 } \\ { 0 } & { 0 } \end{array} \right) \left( \begin{array} { c c } { 1 } & { 0 } \\ { 0 } & { 0 } \end{array} \right) \left( \begin{array} { c c } { 0 } & { 0 } \\ { 1 } & { 0 } \end{array} \right) } \\ &  \quad = \left( \begin{array} { c c } { 0 } & { 0 } \\ { 0 } & { 0 } \end{array} \right) \left( \begin{array} { c c } { 0 } & { 0 } \\ { 0 } & { 0 } \end{array} \right) \left( \begin{array} { c c } { 0 } & { 0 } \\ { 0 } &  0  \end{array}
$$

By the Taylor expansion, we have

$$
\left\{ \begin{array} { l l } { c _ { 0 } + c _ { 1 } = 1 , } \\ { \displaystyle { c _ { 1 } c _ { 1 0 } = \frac { 1 } { 2 } } , } \\ { c _ { 0 } ^ { 2 } + c _ { 1 } ^ { 2 } + 2 c _ { 0 } c _ { 1 } = ( c _ { 0 } + c _ { 1 } ) ^ { 2 } = 1 , } \end{array} \right. \Longrightarrow \left\{ \begin{array} { l l } { c _ { 0 } + c _ { 1 } = 1 , } \\ { \displaystyle c _ { 1 } c _ { 1 0 } = \frac { 1 } { 2 } . } \end{array} \right.
$$

Set $c _ { 0 } = c _ { 1 } = \frac { 1 } { 2 } , c _ { 1 0 } = 1$ 12 , c10 = 1 or c0 = 0, c1 = 1, c10 = 2 , we obtain a second-order modified $\mathbf { R - K }$ method.

Literature[CG93] gives the modified R–K methods for general dynamic system. The scheme on $s o ( 3 ) ^ { * }$ constructed via the above methods can be written as $M _ { n + 1 } = \Lambda M _ { n }$ . Take $\Lambda _ { n + 1 } ^ { - 1 } \Lambda _ { n } = \Lambda$ , we obtain $\Lambda _ { n + 1 } = \Lambda _ { n } \Lambda ^ { - 1 }$ . It is easy to verify that the $\Lambda _ { n + 1 } =$ $\Lambda _ { n } \Lambda ^ { - 1 }$ approximates $\dot { \Lambda } = \Lambda W$ in the same order of accuracy as scheme $M _ { n + 1 } =$ $\Lambda M _ { n }$ .

# 12.4.4 Lie–Poisson Schemes for Free Rigid Body

We have mentioned how to construct a scheme to preserve the angular momentum and the Lie–Poisson structure. The free rigid motion is a simple Lie–Poisson system. Among existing methods, Ge–Marsden algorithm is a first-order method to preserve the Lie–Poisson structure (we thus prove that this method is unable to maintain angular momentum). In Section 12.3, we introduced a generating-function method which is slow. We will introduce a fast method in this section. It is a split Lie–Poisson method[LQ95a] . It is also an angular momentum preserving method.

Because the free rigid motion’s Hamiltonian function is separable, we can use the composite method to construct Lie–Poisson scheme according to separable system’s procedure. MacLachlan introduced an explicit method[McL93] which requires analytic solution for each split subsystem at every step. The midpoint method proposed below is also an explicit Lie–Poisson method but with few computations.

The rigid motion’s Lie–Poisson equation is

$$
\left[ \begin{array} { c } { \dot { x } _ { 1 } } \\ { \dot { x } _ { 2 } } \\ { \dot { x } _ { 3 } } \end{array} \right] = \left[ \begin{array} { c c c } { 0 } & { - x _ { 3 } } & { x _ { 2 } } \\ { x _ { 3 } } & { 0 } & { - x _ { 1 } } \\ { - x _ { 2 } } & { x _ { 1 } } & { 0 } \end{array} \right] \left[ \begin{array} { c } { \frac { \partial H } { \partial x _ { 1 } } } \\ { \frac { \partial H } { \partial x _ { 2 } } } \\ { \frac { \partial H } { \partial x _ { 3 } } } \end{array} \right] ,
$$

where $x \ = \ ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) ^ { \mathrm { T } } \ \in \ \mathbf { R } ^ { 3 }$ is an angular momentum, $H = \frac { 1 } { 2 } \langle I ^ { - 1 } x , x \rangle$ is a Hamiltonian function and energy function of system.

For a separable system, $I$ is usually a diagonal matrix. Without loss of generality, let $H = \frac { 1 } { 2 } \bar { ( a _ { 1 } x _ { 1 } ^ { 2 } + a _ { 2 } x _ { 2 } ^ { 2 } + a _ { 3 } x _ { 3 } ^ { 2 } ) }$ . According to the decomposition rule, the fewer the split steps the better. We can use Casimir function of the Lie–Poisson equation to rewrite the system’s Hamilton function, and obtain an equivalent system. Note that $| x | ^ { 2 } = \sum _ { i = 1 } ^ { n } x _ { i } ^ { 2 }$ is a first integral of the system. Let

$$
\overline { { { H } } } = H - \frac { 1 } { 2 } a _ { 1 } | x | ^ { 2 } = \frac { 1 } { 2 } ( a _ { 2 } - a _ { 1 } ) x _ { 2 } ^ { 2 } + \frac { 1 } { 2 } ( a _ { 3 } - a _ { 1 } ) x _ { 3 } ^ { 2 } = H _ { 1 } + H _ { 2 } ,
$$

where $H _ { 1 } = \frac { 1 } { 2 } ( a _ { 2 } - a _ { 1 } ) x _ { 2 } ^ { 2 } , H _ { 2 } = \frac { 1 } { 2 } ( a _ { 3 } - a _ { 1 } ) x _ { 3 } ^ { 2 } .$

Substituting $H _ { 1 }$ into the Lie–Poisson equation (1.1), we have

$$
\dot { x } = J ( x ) \frac { \partial H _ { 1 } } { \partial x } = \left[ \begin{array} { c } { - ( a _ { 2 } - a _ { 1 } ) x _ { 2 } x _ { 3 } } \\ { 0 } \\ { 0 } \\ { ( a _ { 2 } - a _ { 1 } ) x _ { 1 } x _ { 2 } } \end{array} \right] ,
$$

where

$$
J ( x ) = \left[ \begin{array} { c c c } { { 0 } } & { { - x _ { 3 } } } & { { x _ { 2 } } } \\ { { } } & { { } } & { { } } \\ { { x _ { 3 } } } & { { 0 } } & { { - x _ { 1 } } } \\ { { } } & { { } } & { { } } \\ { { - x _ { 2 } } } & { { x _ { 1 } } } & { { 0 } } \end{array} \right] .
$$

This equation can be simplified as a standard symplectic system

$$
\left\{ \begin{array} { l l } { \dot { x } _ { 1 } = - ( a _ { 2 } - a _ { 1 } ) x _ { 2 } x _ { 3 } , } \\ { ~ } \\ { \dot { x } _ { 3 } = ( a _ { 2 } - a _ { 1 } ) x _ { 1 } x _ { 2 } , } \end{array} \right.
$$

where $x _ { 2 }$ is a constant.

Among symplectic difference schemes for the standard symplectic system (4.10), only a few of them can preserve the Lie-Poisson structure of the original system (4.9).

Theorem 4.1. For the system (4.9), the midpoint scheme is a Lie–Poisson scheme[LQ95a] .

In order to prove the Theorem 4.1, we need the following lemma first.

Lemma 4.2. For the system (4.9), a symplectic algorithm for the standard symplectic system (4.10) preserves Poisson structure, if and only if the following three conditions are satisfied

$$
\left\{ \begin{array} { l l } { - x _ { 1 1 } x _ { 3 } + x _ { 1 3 } x _ { 1 } = - \widehat { x } _ { 3 } , } \\ { \qquad } \\ { x _ { 3 1 } x _ { 3 } - x _ { 3 3 } x _ { 1 } = - \widehat { x } _ { 1 } , } \\ { \qquad } \\ { x _ { 1 2 } \widehat { x } _ { 1 } + x _ { 3 2 } \widehat { x } _ { 3 } = 0 , } \end{array} \right.
$$

where $x _ { i } = x _ { i } ^ { n } , \widehat { x _ { i } } = x _ { i } ^ { n + 1 } , x _ { i j } = \frac { \partial \widehat { x _ { i } } } { \partial x _ { j } } .$

Proof. By the Theorem 1.2, a scheme is of Poisson if and only if

$$
\left( \frac { \partial \widehat { x } } { \partial x } \right) J ( x ) \left( \frac { \partial \widehat { x } } { \partial x } \right) ^ { \mathrm { T } } = J ( \widehat { x } ) .
$$

Expanding the above equation, we get

$$
{ \begin{array} { r l } & { \left[ { \begin{array} { c c c } { x _ { 1 1 } } & { x _ { 1 2 } } & { x _ { 1 3 } } \\ { 0 } & { 1 } & { 0 } \\ { x _ { 3 1 } } & { x _ { 3 2 } } & { x _ { 3 3 } } \end{array} } \right] \left[ { \begin{array} { c c c } { 0 } & { - x _ { 3 } } & { x _ { 2 } } \\ { x _ { 3 } } & { 0 } & { - x _ { 1 } } \\ { - x _ { 2 } } & { x _ { 1 } } & { 0 } \end{array} } \right] \left[ { \begin{array} { c c c } { x _ { 1 1 } } & { 0 } & { x _ { 3 1 } } \\ { x _ { 1 2 } } & { 1 } & { x _ { 3 2 } } \\ { x _ { 1 3 } } & { 0 } & { x _ { 3 3 } } \end{array} } \right] } \\ { = } & { \left[ { \begin{array} { c c c } { 0 } & { - { \hat { x } } _ { 3 } } & { { \hat { x } } _ { 2 } } \\ { { \hat { x } } _ { 3 } } & { 0 } & { - { \hat { x } } _ { 1 } } \\ { - { \hat { x } } _ { 2 } } & { { \hat { x } } _ { 1 } } & { 0 } \end{array} } \right] , } \end{array} }
$$

i.e.,

$$
\left[ \begin{array} { c c c } { { 0 } } & { { - x _ { 1 1 } x _ { 3 } + x _ { 1 3 } x _ { 1 } } } & { { a _ { 1 3 } } } \\ { { x _ { 1 1 } x _ { 3 } - x _ { 1 3 } x _ { 1 } } } & { { 0 } } & { { x _ { 3 1 } x _ { 3 } - x _ { 3 3 } x _ { 1 } } } \\ { { - a _ { 1 3 } } } & { { x _ { 3 3 } x _ { 1 } - x _ { 3 1 } x _ { 3 } } } & { { 0 } } \end{array} \right] = \left[ \begin{array} { c c c } { { 0 } } & { { - \widehat { x } _ { 3 } } } & { { \widehat { x } _ { 2 } } } & { { - \widehat { x } _ { 3 } } } \\ { { \widehat { x } _ { 3 } } } & { { 0 } } & { { - \widehat { x } _ { 1 } } } \\ { { - \widehat { x } _ { 2 } } } & { { \widehat { x } _ { 1 } } } & { { 0 } } \end{array} \right] .
$$

where $a _ { 1 3 } = ( x _ { 1 2 } x _ { 3 } - x _ { 1 3 } x _ { 2 } ) x _ { 3 1 } + ( x _ { 1 3 } x _ { 1 } - x _ { 1 1 } x _ { 3 } ) x _ { 3 2 } + ( x _ { 1 1 } x _ { 2 } - x _ { 1 2 } x _ { 1 } ) x _ { 3 3 }$

Since the scheme is symplectic for (4.10), we have

$$
- x _ { 1 3 } x _ { 3 1 } + x _ { 1 1 } x _ { 3 3 } = 1 .
$$

So $a _ { 1 3 }$ can be simplified as:

$$
a _ { 1 3 } = ( x _ { 3 } x _ { 3 1 } - x _ { 1 } x _ { 3 3 } ) x _ { 1 2 } + ( x _ { 1 3 } x _ { 1 } - x _ { 1 1 } x _ { 3 } ) x _ { 3 2 } + x _ { 2 } .
$$

Comparing the corresponding elements of the matrix on both sides and using the condition $\widehat { x } _ { 2 } = x _ { 2 }$ , we have

$$
\left\{ \begin{array} { l l } { x _ { 1 1 } x _ { 3 } - x _ { 1 3 } x _ { 1 } = \widehat { x } _ { 3 } , } \\ { \qquad } \\ { x _ { 3 1 } x _ { 3 } - x _ { 3 3 } x _ { 1 } = - \widehat { x } _ { 1 } , } \\ { \qquad } \\ { x _ { 1 2 } \widehat { x } _ { 1 } + x _ { 3 2 } \widehat { x } _ { 3 } = 0 . } \end{array} \right.
$$

Thus before the lemma is proved.

Now we will prove the Theorem 4.1.

Proof. The midpoint scheme for system (4.9) is (here, $I = \left( I _ { 1 } , I _ { 2 } , I _ { 3 } \right) = \left( a _ { 1 } , a _ { 2 } , a _ { 3 } \right) )$

$$
\left\{ \begin{array} { l l } { \widehat { x } _ { 1 } = x _ { 1 } + \tau ( I _ { 1 } - I _ { 2 } ) \frac { \widehat { x } _ { 3 } + x _ { 3 } } { 2 } x _ { 2 } , } \\ { \widehat { x } _ { 2 } = x _ { 2 } , } \\ { \widehat { x } _ { 3 } = x _ { 3 } + \tau ( I _ { 2 } - I _ { 1 } ) \frac { \widehat { x } _ { 1 } + x _ { 1 } } { 2 } x _ { 2 } . } \end{array} \right.
$$

Its Jacobian matrix is $\left[ { \begin{array} { c c c } { x _ { 1 1 } } & { x _ { 1 2 } } & { x _ { 1 3 } } \\ { 0 } & { 1 } & { 0 } \\ { x _ { 3 1 } } & { x _ { 3 2 } } & { x _ { 3 3 } } \end{array} } \right] , { \mathrm { w h e r } }$ e

$$
\left\{ \begin{array} { l l } { \displaystyle x _ { 1 1 } = 1 + \frac { T } { 2 } ( I _ { 1 } - I _ { 2 } ) x _ { 2 } x _ { 3 1 } , } \\ { \displaystyle x _ { 1 2 } = \frac { T } { 2 } ( I _ { 1 } - I _ { 2 } ) ( \widehat { x } _ { 3 } + x _ { 3 } ) + \frac { T } { 2 } ( I _ { 1 } - I _ { 2 } ) x _ { 2 } x _ { 3 2 } , } \\ { \displaystyle x _ { 1 3 } = \frac { T } { 2 } ( I _ { 1 } - I _ { 2 } ) x _ { 3 3 } x _ { 2 } + \frac { T } { 2 } ( I _ { 1 } - I _ { 2 } ) x _ { 2 } , } \\ { \displaystyle x _ { 3 1 } = \frac { T } { 2 } ( I _ { 2 } - I _ { 1 } ) x _ { 1 1 } x _ { 2 } + \frac { T } { 2 } ( I _ { 2 } - I _ { 1 } ) x _ { 2 } , } \\ { \displaystyle x _ { 3 2 } = \frac { T } { 2 } ( I _ { 2 } - I _ { 1 } ) ( \widehat { x } _ { 1 } + x _ { 1 } ) + \frac { T } { 2 } ( I _ { 2 } - I _ { 1 } ) x _ { 2 } , } \\ { \displaystyle x _ { 3 3 } = 1 + \frac { T } { 2 } ( I _ { 2 } - I _ { 1 } ) x _ { 2 } x _ { 1 3 } . } \end{array} \right.
$$

Solving the above equations, we get

$$
\left\{ \begin{array} { l l } { \displaystyle x _ { 1 1 } = x _ { 3 3 } = \frac { 1 - a ^ { 2 } } { 1 + a ^ { 2 } } , } \\ { \displaystyle x _ { 1 2 } = \frac { \frac { 7 } { 2 } \left( I _ { 1 } - I _ { 2 } \right) \widehat x _ { 3 } } { 1 + a ^ { 2 } } , } \\ { \displaystyle x _ { 1 3 } = - x _ { 3 1 } = - \frac { 2 a } { 1 + a ^ { 2 } } , } \\ { \displaystyle x _ { 3 2 } = \frac { \frac { 7 } { 2 } \left( I _ { 2 } - I _ { 1 } \right) \widehat x _ { 1 } } { 1 + a ^ { 2 } } , } \end{array} \right.
$$

where

$$
a = \frac { \tau } { 2 } ( I _ { 2 } - I _ { 1 } ) x _ { 2 } .
$$

Substituting the system of Equations (4.12) into condition (4.11), we find that all conditions are satisfied. Therefore, by Lemma 4.2, the scheme is of Poisson. $\blacktriangle$

Lemma 4.3. [FQ91] Consider dynamic system ${ \dot { x } } = a ( x )$ . If $a$ can be split into $a =$ $a _ { 1 } + a _ { 2 } + \cdots + a _ { k }$ , and $\boldsymbol { g } ^ { s } \sim \boldsymbol { e } _ { a } ^ { s }$ is phase flow of a dynamic system, then

$$
g _ { i } ^ { s } \sim e _ { a _ { i } } ^ { s } , \quad 2 n d - o r d e r , \quad \forall i \implies g _ { 1 } ^ { \frac { s } { 2 } } \circ \cdot \cdot \cdot g _ { k } ^ { \frac { s } { 2 } } \circ g _ { k } ^ { \frac { s } { 2 } } \circ \cdot \cdot \cdot g _ { 1 } ^ { \frac { s } { 2 } } \smile e _ { a } ^ { s } , \quad 2 n d - o r d e r .
$$

Proof. For the standard symplectic system (4.10), the generalized Euler scheme

$$
\widehat { \boldsymbol { x } } = \boldsymbol { x } + \tau J \nabla H ( B \widehat { \boldsymbol { x } } + ( I - B ) \boldsymbol { x } )
$$

is symplectic, iff

$$
B = \frac 1 2 ( I + C ) , \quad J C + C ^ { \mathrm { T } } J = O .
$$

It is natural to ask what kind of symplectic difference scheme for the system (4.10) is also a Poisson scheme for the system (4.9). Below we restrict our discussion to the generalized Euler scheme (4.14).

Let C = c1 c2 ! , then the symplectic condition (4.14) turns into $c _ { 4 } = - c _ { 1 }$ Therefore,

$$
B = \frac { 1 } { 2 } \left[ \begin{array} { c c } { 1 + c _ { 1 } } & { c _ { 2 } } \\ { c _ { 3 } } & { 1 - c _ { 1 } } \end{array} \right] ,
$$

then

$$
\begin{array} { r l r } {  { B \widehat { x } + ( I - B ) x \ = \ \frac { 1 } { 2 } [ \begin{array} { l } { ( 1 + c _ { 1 } ) \widehat { x } _ { 1 } + ( 1 - c _ { 1 } ) x _ { 1 } + c _ { 2 } ( \widehat { x } _ { 3 } - x _ { 3 } ) } \\ { c _ { 3 } ( \widehat { x } _ { 1 } - x _ { 1 } ) + ( 1 - c _ { 1 } ) \widehat { x } _ { 3 } + ( 1 - c _ { 1 } ) x _ { 3 } } \end{array} ] } } \\ & { } & { \ = \ \frac { 1 } { 2 } [ \begin{array} { l } { z _ { 1 } } \\ { z _ { 3 } } \end{array} ] , } \end{array}
$$

then Euler scheme becomes

$$
\left\{ \begin{array} { l l } { \widehat { x } _ { 1 } = x _ { 1 } - a z _ { 3 } , } \\ { \qquad } \\ { \widehat { x } _ { 3 } = x _ { 3 } - a z _ { 1 } , } \end{array} \right.
$$

where $a$ is defined by Equation (4.13), $z _ { 1 } , z _ { 3 }$ are defined by Equation (4.15).

After complex computations, the elements of Jacobian matrix of the solution are

$$
\begin{array} { r l } & { x _ { 1 1 } = \cfrac { ( 1 + a c _ { 3 } ) ( 1 - a c _ { 2 } ) - a ^ { 2 } ( 1 - c _ { 1 } ) ^ { 2 } } { ( 1 + a c _ { 3 } ) ( 1 - a c _ { 2 } ) + a ^ { 2 } ( 1 - c _ { 1 } ^ { 2 } ) } , } \\ & { x _ { 1 3 } = \cfrac { - 2 a ( 1 - a c _ { 2 } ) } { ( 1 + a c _ { 3 } ) ( 1 - a c _ { 2 } ) + a ^ { 2 } ( 1 - c _ { 1 } ^ { 2 } ) } , } \\ & { \widehat { x } _ { 3 } = \cfrac { ( ( 1 + a c _ { 3 } ) ( 1 - a c _ { 2 } ) - a ^ { 2 } ( 1 - c _ { 1 } ) ^ { 2 } ) x _ { 3 } + 2 a ( 1 + a c _ { 3 } ) x _ { 1 } } { ( 1 + a c _ { 3 } ) ( 1 - a c _ { 2 } ) + a ^ { 2 } ( 1 - c _ { 1 } ^ { 2 } ) } , } \\ & { x _ { 1 1 } x _ { 3 } - x _ { 1 3 } x _ { 1 } = \widehat { x } _ { 3 } \quad ( \sec { ( 4 . 1 1 ) } ) . } \end{array}
$$

Since $x _ { 1 } , x _ { 3 }$ are arbitrary real number, we can get

$$
c _ { 1 } = 0 , \quad c _ { 2 } = - c _ { 3 } .
$$

Substituting Equation (4.17) into (4.16), and recalculating the Jacobian matrix, we have

$$
\begin{array} { l } { { x _ { 3 1 } = \displaystyle \frac { 2 a ( 1 - a c _ { 2 } ) } { a ^ { 2 } + ( 1 - a c _ { 2 } ) ^ { 2 } } , ~ x _ { 3 3 } = \displaystyle \frac { ( 1 - a c _ { 2 } ) ^ { 2 } - a ^ { 2 } } { a ^ { 2 } + ( 1 - a c _ { 2 } ) ^ { 2 } } , } } \\ { { { } } } \\  { { \widehat x _ { 1 } = \displaystyle \frac { ( ( 1 - a c _ { 2 } ) ^ { 2 } - a ^ { 2 } ) x _ { 1 } } { a ^ { 2 } + ( 1 - a c _ { 2 } ) ^ { 2 } } . } } \end{array}
$$

It is easy to see that one of the conditions (4.11)

$$
x _ { 3 1 } x _ { 3 } - x _ { 3 3 } x _ { 1 } = - \widehat { x } _ { 1 }
$$

is satisfied. Likewise, we can prove that another condition of (4.11) is also satisfied.

From (4.17), we have $C = c J$ , where $c$ is an arbitrary constant and

$$
J = \left[ \begin{array} { c c } { { 0 } } & { { 1 } } \\ { { } } & { { } } \\ { { - 1 } } & { { 0 } } \end{array} \right] .
$$

Therefore, the lemma is completed.

# 12.4.5 Lie–Poisson Scheme on Heavy Top

The Lie–Poisson algorithm as we discussed in the previous sections are based on the dual space of semi-simple Lie algebra. In practice, we often have some Lie-Poisson system whose configuration space is not based on semi-simple Lie algebra, but on the dual space of the semi-product of Lie algebra and linear space. Such systems include but not limited to heavy top and compressible hydrodynamics flows. The reader can refer to literature[MRW90] for a more detailed discussion. In such configuration space, there exists no momentum mapping as we discussed in previous sections. The angular momentum is preserved only along a specific direction. Therefore, the generating function theory is no longer valid. However, using Lie–Poisson equations under local coordinates, we can construct the Lie–Poisson algorithm and the angular momentum preserving scheme. We will illustrate this by heavy top as an example.

Heavy top is a gravity body under the action of gravity with a fixed point. The free rigid body is a heavy top with the fixed point in center of mass. Its configuration space is 3 dimensional Euclid space $E ( 3 )$ . Its Lie algebra is no longer semisimple. Its phase space $e ^ { * } ( 3 )$ has 6 coordinates $\{ x _ { 1 } , x _ { 2 } , x _ { 3 } , p _ { 1 } , p _ { 2 } , p _ { 3 } \}$ . The Poisson bracket operation on $e ^ { * } ( 3 )$ is

$$
\{ x _ { i } , x _ { j } \} = \varepsilon _ { i j k } x _ { k } , ~ \{ x _ { i } , p _ { i } \} = \varepsilon _ { i j k } p _ { k } , ~ \{ p _ { i } , p _ { j } \} = 0 ,
$$

where

$$
\varepsilon _ { i j k } = { \left\{ \begin{array} { l l } { ( i , j , k ) , } & { i , j , k { \mathrm { ~ i s ~ n o t ~ t h e ~ s a m e } } , } \\ { 0 , } & { i , j , k { \mathrm { ~ i s ~ t h e ~ s a m e } } . } \end{array} \right. }
$$

There are two independent Casimir functions for bracket (4.18)

$$
f _ { 1 } = \sum _ { i = 1 } ^ { 3 } p _ { i } ^ { 2 } , \quad f _ { 2 } = \sum _ { i = 1 } ^ { 3 } p _ { i } x _ { i } .
$$

Let $H ( x , p )$ be the Hamiltonian function of system. Introducing notation $u _ { i } =$ ${ \frac { \partial H } { \partial p _ { i } } } , \Omega _ { i } = { \frac { \partial { \bar { H } } } { \partial x _ { i } } }$ . Then the Lie–Poisson equation has the form of Kirchhoff equation

$$
\dot { p } = [ p , \Omega ] , \quad \dot { x } = [ x , \omega ] + [ p , u ] ,
$$

where square bracket denotes cross product. $H$ is the system’s energy, $x$ and $p$ are angular momentum, and momentum under momentum coordinate. For a general case, energy $H$ is of quadratic form about $x , p$ , and positive definite, which can be given as follows