# 359 The $V$ and $W$ transformations

We refer to the transformation of $M$ using the Vandermonde matrix $V$ to form $V ^ { \prime } M V$ , as the $V$ transformation’. We now introduce the more sophisticated $W$ transformation.

We recall Corollary 356D, which enables us to confine our attention to irreducible methods in which $b ^ { \intercal }$ has only positive elements. Construct a sequence of polynomials $P _ { 0 }$ , $P _ { 1 }$ , $\cdot \cdot \cdot$ , $P _ { s - 1 }$ with degrees 0, 1, . . . , $s \mathrm { ~ - ~ } 1$ , respectively, which are orthonormal in the sense that

$$
\sum _ { i = 1 } ^ { s } b _ { i } P _ { k - 1 } ( c _ { i } ) P _ { l - 1 } ( c _ { i } ) = \delta _ { k l } , \qquad k , l = 1 , 2 , \ldots , s .
$$

We can assume that the leading coefficients are all positive. Define $W$ as the generalized Vandermonde matrix

$$
\begin{array} { r l } { W = [ P _ { 0 } ( c ) \quad P _ { 1 } ( c ) \quad \cdots \quad P _ { s - 1 } ( c ) ] } \\ & { \qquad = \left[ \begin{array} { c c c c } { P _ { 0 } ( c _ { 1 } ) } & { P _ { 1 } ( c _ { 1 } ) } & { \cdots } & { P _ { s - 1 } ( c _ { 1 } ) } \\ { P _ { 0 } ( c _ { 2 } ) } & { P _ { 1 } ( c _ { 2 } ) } & { \cdots } & { P _ { s - 1 } ( c _ { 2 } ) } \\ { \vdots } & { \vdots } & { \vdots } \\ { P _ { 0 } ( c _ { s } ) } & { P _ { 1 } ( c _ { s } ) } & { \cdots } & { P _ { s - 1 } ( c _ { s } ) } \end{array} \right] . } \end{array}
$$

This matrix can be constructed using the Gram–Schmidt process, or what is algebraically equivalent, from a QR factorization

$$
B ^ { 1 / 2 } V = ( B ^ { 1 / 2 } W ) R ,
$$

where $B ^ { 1 / 2 } = \mathrm { d i a g } ( \sqrt { b _ { 1 } } , \sqrt { b _ { 2 } } , \cdot \cdot \cdot , \sqrt { b _ { s } } )$ and $R$ is upper triangular with positive elements on the diagonal. Note that the coefficients in $P _ { 0 }$ , $P _ { 1 }$ , $\cdot \cdot \cdot$ , $P _ { s - 1 }$ can be read off from the columns of $R$ .

If $b ^ { \prime }$ and $c$ are weight and abscissa vectors for a Runge–Kutta method of order $p$ , then as long as $k + l \le p + 1$ , (359a) implies that

$$
\int _ { 0 } ^ { 1 } P _ { k - 1 } ( x ) P _ { l - 1 } ( x ) d x = \sum _ { i = 1 } ^ { s } b _ { i } P _ { k - 1 } ( c _ { i } ) P _ { l - 1 } ( c _ { i } ) = \delta _ { k l } ,
$$

implying that $P _ { 0 }$ , $P _ { 1 }$ , . . . , $P _ { \left[ \left( p - 1 \right) / 2 \right] }$ are orthonormal with respect to integration on $[ 0 , 1 ]$ . This means that they are necessarily the normalized Legendre polynomials on this interval, given by

$$
P _ { k } ( z ) = \sqrt { 2 k + 1 } \sum _ { i = 0 } ^ { k } ( - 1 ) ^ { k - i } { \binom { k } { i } } { \binom { k + i } { i } } z ^ { i } .
$$

In particular, $P _ { 0 } ( x ) \ = \ 1$ and the first column of $W$ is $\mathbf { 1 }$ . Because of orthonormality, it follows that $\mathbf { 1 } ^ { \prime } B W = e _ { 1 } ^ { \mathsf { T } }$ .

We now focus our attention on the matrix $X = W ^ { \prime } B A W$ . This is significant because

$$
\begin{array} { r } { W ^ { \mathsf { T } } M W = X + X ^ { \mathsf { T } } - ( W ^ { \mathsf { T } } B \mathbf { 1 } ) ( \mathbf { 1 } ^ { \mathsf { T } } B W ) = ( X - \frac { 1 } { 2 } e _ { 1 } e _ { 1 } ^ { \mathsf { T } } ) + ( X - \frac { 1 } { 2 } e _ { 1 } e _ { 1 } ^ { \mathsf { T } } ) ^ { \mathsf { T } } . } \end{array}
$$

Because $M$ , and therefore $W ^ { \prime } M W$ , is the zero matrix for the Gauss method, it follows that $\begin{array} { r } { X - \frac { 1 } { 2 } e _ { 1 } e _ { 1 } ^ { \top } } \end{array}$ is skew-symmetric. Denote $X$ by $X _ { \mathrm { G } }$ in this special case. We now evaluate $X _ { \mathrm { G } }$ in full.

# Lemma 359A Let

$$
\begin{array} { r } { X _ { G } = W ^ { \top } B A W , } \end{array}
$$

where $A$ and $B = \mathrm { d i a g } ( b )$ are as for the Gauss method of order 2s. Also let

$$
\xi _ { k } = \frac { 1 } { 2 \sqrt { 4 k ^ { 2 } - 1 } } , \qquad k = 1 , 2 , \ldots , s - 1 .
$$

Then

$$
\begin{array} { r } { { \cal X } _ { G } = \left[ \begin{array} { c c c c c c c c } { \frac 1 2 } & { - \xi _ { 1 } } & { 0 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { \xi _ { 1 } } & { 0 } & { - \xi _ { 2 } } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { 0 } & { \xi _ { 2 } } & { 0 } & { - \xi _ { 3 } } & { \cdots } & { 0 } & { 0 } \\ { \vdots } & { \vdots } & { \vdots } & { \vdots } & & { \vdots } & { \vdots } \\ { 0 } & { 0 } & { 0 } & { 0 } & { \cdots } & { 0 } & { - \xi _ { s - 1 } } \\ { 0 } & { 0 } & { 0 } & { 0 } & { \cdots } & { \xi _ { s - 1 } } & { 0 } \end{array} \right] . } \end{array}
$$

Proof. From linear combinations of identities included in the condition $E ( s , s )$ , given by (321c), we have

$$
\sum _ { i = 1 } ^ { s } \sum _ { j = 1 } ^ { s } b _ { i } \phi ( c _ { i } ) a _ { i j } \psi ( c _ { j } ) = \int _ { 0 } ^ { 1 } \phi ( u ) \int _ { 0 } ^ { u } \psi ( v ) d v d u ,
$$

for polynomials $\phi$ and $\psi$ each with degree less than $s$ . Use the polynomials $\phi = P _ { k - 1 }$ , $\psi = P _ { l - 1 }$ and we have a formula for the $( k , l )$ element of $X _ { \mathrm { G } }$ . Add to this the result for $k$ and $\it l$ interchanged and use integration by parts. We have

$$
( X _ { \mathrm { G } } ) _ { k l } + ( X _ { \mathrm { G } } ) _ { l k } = \int _ { 0 } ^ { 1 } P _ { k - 1 } ( u ) d u \int _ { 0 } ^ { 1 } P _ { l - 1 } ( v ) d v = \delta _ { k 1 } \delta _ { l 1 } .
$$

This result determines the diagonal elements of $X _ { \mathrm { G } }$ , and also implies the skew-symmetric form of $X _ { \mathrm { G } } ~ - ~ \frac { 1 } { 2 } e _ { 1 } e _ { 1 } ^ { \top }$ . We now determine the form of the lower triangular elements. If $k > l + 1$ , the integral $\int _ { 0 } ^ { u } P _ { l - 1 } ( v ) d v$ has lower degree than $P _ { k - 1 }$ and is therefore orthogonal to it. Thus, in this case, $( X _ { \mathrm { G } } ) _ { k l } = 0$ . It remains to evaluate $( X _ { \mathrm { G } } ) _ { k , k - 1 }$ for $k = 1 , 2 , \ldots , s - 1$ . The integral $\int _ { 0 } ^ { u } P _ { k - 1 } ( v ) d v$ is a polynomial in $u$ of degree $k$ and can be written in the form $\theta P _ { k } ( u )$ added to a polynomial of degree less than $k$ . The integral of $P _ { k } ( u )$ multiplied by the polynomial of degree less than $k$ is zero, by orthogonality, and the integral reduces to

$$
\int _ { 0 } ^ { 1 } \theta P _ { k } ( u ) ^ { 2 } d u = \theta .
$$

is The value of $\sqrt { 2 k - 1 } \binom { 2 k - 2 } { k - 1 }$ $\theta$ can be found by noting that the coefficient of , with a similar formula for the leading coefficient of in $P _ { k - 1 } ( v )$ $P _ { k } ( u )$

Hence,

$$
( X _ { \mathrm { G } } ) _ { k , k - 1 } = \theta = { \frac { { \frac { 1 } { k } } { \sqrt { 2 k - 1 } } { \binom { 2 k - 2 } { k - 1 } } } { { \sqrt { 2 k + 1 } } { \binom { 2 k } { k } } } } = { \frac { 1 } { 2 { \sqrt { 4 k ^ { 2 } - 1 } } } } .
$$

The computation of elements of $X ~ = ~ W ^ { \top } B A W$ for any Runge–Kutta method, for which $W$ makes sense, will lead to the same $( k , l )$ elements as in $X _ { \mathrm { G } }$ as long as $k + l \le p + 1$ . We state this formally.

Corollary 359B Let $( A , b , c )$ denote a Runge–Kutta method for which $B =$ $\mathrm { d i a g } ( b )$ is positive definite and for which the abscissae are distinct. Define $W$ by (359b) and $X$ by $X = W ^ { \prime } B A W$ . Then $X _ { k l } ~ = ~ ( X _ { G } ) _ { k l }$ , as long as $k + l \le p + 1$ .

The $W$ transformation is related in an interesting way to the $C ( m )$ and $D ( m )$ conditions, which can be written in the equivalent forms

$$
\begin{array} { c c } { { C ( m ) : } } & { { \displaystyle \sum _ { j = 1 } ^ { s } a _ { i j } P _ { k - 1 } ( c _ { j } ) = \int _ { 0 } ^ { c _ { i } } P _ { k - 1 } ( x ) d x , } } & { { k \le m , \ i = 1 , 2 , \ldots , s , } } \\ { { D ( m ) : } } & { { \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } P _ { k - 1 } ( c _ { i } ) a _ { i j } = b _ { j } \int _ { c _ { j } } ^ { 1 } P _ { k - 1 } ( x ) d x , } } & { { k \le m , \ j = 1 , 2 , \ldots , s . } } \end{array}
$$

It follows from these observations that, if $B ( m )$ and $C ( m )$ are true, then the first $m$ columns of $X$ will be the same as for $X _ { \mathrm { G } }$ . Similarly, if $B ( m )$ and $D ( m )$ , then the first $m$ rows of $X$ and $X _ { \mathrm { G } }$ will agree.

Amongst the methods known to be algebraically stable, we have already encountered the Gauss and Radau IIA methods. We can extend this list to include further methods.

Theorem 359C The Gauss, Radau IA, Radau IIA and Lobatto IIIC methods are algebraically stable.

Proof. We have already settled the Gauss and Radau IIA cases, using the $V$ transformation, making use of the $C ( s )$ and $B ( p )$ conditions, as in Theorem 358A.

To prove the result for Radau IA methods, use the $D ( s )$ and $B ( 2 s - 1 )$ conditions:

$$
\begin{array} { r l } { \displaystyle \sum _ { j = 1 } ^ { s } c _ { i } ^ { k - 1 } b _ { i } a _ { i j } c _ { j } ^ { l - 1 } + \displaystyle \sum _ { i , j = 1 } ^ { s } c _ { i } ^ { k - 1 } b _ { j } a _ { j i } c _ { j } ^ { l - 1 } } & { } \\ { = \displaystyle \frac { 1 } { k } \displaystyle \sum _ { j = 1 } ^ { s } b _ { j } ( 1 - c _ { j } ^ { k } ) c _ { j } ^ { l - 1 } + \displaystyle \frac { 1 } { l } \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } ( 1 - c _ { i } ^ { l } ) c _ { i } ^ { k - 1 } - \displaystyle \frac { 1 } { k l } } & { } \\ { \displaystyle } & { = \displaystyle \frac { 1 } { k l } - \frac { k + l } { k l } \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } c _ { i } ^ { k + l - 1 } . } \end{array}
$$

The value of this expression is zero if $k + l \le 2 s - 1$ . Although it can be verified directly that the value is positive in the remaining case $k = l = s$ , it is enough to show that the $( 1 , 1 )$ element of $M$ is positive, because this will have the same sign as the only non-zero eigenvalue of the rank 1 matrix $V ^ { \prime } M V$ . We note that all values in the first column of $A$ are equal to $b _ { 1 }$ because these give the unique solution to the $D ( s )$ condition applied to the first column. Hence, we calculate the $( 1 , 1 )$ element of $M$ to be

$$
2 b _ { 1 } a _ { 1 1 } - b _ { 1 } ^ { 2 } = b _ { 1 } ^ { 2 } > 0 .
$$

In the case of the Lobatto IIIC methods, we can use a combination of the $C ( s - 1 )$ and $D ( s - 1 )$ conditions to evaluate the $( k , l )$ and $( l , k )$ elements of $M$ , where $k \le s - 1$ and $l \leq s$ . The value of these elements is

$$
\begin{array} { r c l } { { } } & { { } } & { { \displaystyle \sum _ { i , j = 1 } ^ { s } c _ { i } ^ { k - 1 } b _ { i } a _ { i j } c _ { j } ^ { l - 1 } + \sum _ { i , j = 1 } ^ { s } c _ { i } ^ { k - 1 } b _ { j } a _ { j i } c _ { j } ^ { l - 1 } } } \\ { { } } & { { } } & { { = \displaystyle \frac { 1 } { k } \sum _ { j = 1 } ^ { s } ( 1 - c _ { j } ^ { k } ) c _ { j } ^ { l - 1 } + \frac { 1 } { k } \sum _ { i = 1 } ^ { s } b _ { i } c _ { i } ^ { k + l - 1 } - \frac { 1 } { k l } } } \\ { { } } & { { } } & { { = \displaystyle \frac { 1 } { k } \sum _ { j = 1 } ^ { s } b _ { j } c _ { j } ^ { l - 1 } - \frac { 1 } { k l } } } \\ { { } } & { { } } & { { = 0 . } } \end{array}
$$

The final step of the proof is the same as for the Radau IA case, because again $a _ { i 1 } = b _ { 1 }$ , for $i = 1 , 2 , \dots , s$ . 

The $V$ transformation was used to simplify questions concerning algebraic stability in Butcher (1975) and Burrage (1978). The $W$ transformation was introduced in Hairer and Wanner (1981, 1982). Recent results on the $W$ transformation, and especially application to symplectic methods, were presented in Hairer and Leone (2000) .

# Exercises 35

35.1 Show that a Runge–Kutta method with $R ( z ) ~ = ~ N ( z ) / D ( z )$ , where $N$ and $D$ have no common factors, cannot be A-stable unless the coefficients in $D ( z )$ alternate in sign.

35.2 Show that the error constant for the $( s - d , s )$ Pad´e approximation to the exponential function has sign $( - 1 ) ^ { s }$ . Deduce that, if $d > 0$ and $d = 3$ (mod 4) or $d = 0$ (mod 4), then $| R ( i y ) | > 0$ , for sufficiently small real $y$ .

35.3 Show that the implicit Runge–Kutta method with tableau

<table><tr><td>#云</td><td>A 2</td></tr><tr><td>1</td><td></td></tr><tr><td>1</td><td></td></tr><tr><td></td><td>1</td></tr></table>

is A-stable but not AN-stable.

35.4 For the $( 0 , m )$ Pad´e approximation $N ( z ) / D ( z )$ , show that the denominator $D$ has zeros with negative real part, for $m \geq 5$ .

35.5 For the $( 1 , m )$ Pad´e approximation $N ( z ) / D ( z )$ , show that the denominator $D$ has zeros with negative real part, for $m \geq 7$ .
