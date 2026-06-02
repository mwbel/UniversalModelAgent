So

$$
) = g ^ { ( n + 1 ) } ( \xi ) = f ^ { ( n + 1 ) } ( \xi ) - P ^ { ( n + 1 ) } ( \xi ) - [ f ( x ) - P ( x ) ] \frac { d ^ { n + 1 } } { d \imath ^ { n + 1 } } \left[ \prod _ { i = 0 } ^ { n } \frac { ( t - x _ { i } ) } { ( x - x _ { i } ) } \right] _ { t = \xi } .
$$

Since $P ( x )$ is apolynomial of degree at most $\pmb { n }$ ,the $( n + 1 )$ st derivative, $P ^ { ( n + 1 ) } ( x )$ ,is identically zero. Also, $\scriptstyle \prod _ { i = 0 } ^ { n } [ ( t - x _ { i } ) / ( x - x _ { i } ) ]$ is a polynomial of degree $( n + 1 )$ ,s0

$$
\prod _ { i = 0 } ^ { n } { \frac { ( t - x _ { i } ) } { ( x - x _ { i } ) } } = \left[ { \frac { 1 } { \prod _ { i = 0 } ^ { n } ( x - x _ { i } ) } } \right] t ^ { n + 1 } + ( \mathrm { l o w e r \mathrm { - } d e g r e e \ t e r m s \ i n \ } t ) ,
$$

and

$$
{ \frac { d ^ { n + 1 } } { d t ^ { n + 1 } } } \prod _ { i = 0 } ^ { n } { \frac { ( t - x _ { i } ) } { ( x - x _ { i } ) } } = { \frac { ( n + 1 ) ! } { \prod _ { i = 0 } ^ { n } ( x - x _ { i } ) } } .
$$

Equation (3.4) now becomes

$$
0 = f ^ { ( n + 1 ) } ( \xi ) - 0 - [ f ( x ) - P ( x ) ] \frac { ( n + 1 ) ! } { \prod _ { i = 0 } ^ { n } ( x - x _ { i } ) } ,
$$

and, upon solving for $f ( x )$ , we have

$$
f ( x ) = P ( x ) + { \frac { f ^ { ( n + 1 ) } ( \xi ) } { ( n + 1 ) ! } } \prod _ { i = 0 } ^ { n } ( x - x _ { i } ) .
$$

The error formula in Theorem 3.3 is an important theoretical result because Lagrange polynomials are used extensively for deriving numerical differentiation and integration methods. Error bounds for these techniques are obtained from the Lagrange error formula.

Note that the error form for the Lagrange polynomial is quite similar to that for the Taylor polynomial. The $\pmb { n }$ th Taylor polynomial about $x _ { 0 }$ concentrates all the known information at $x _ { 0 }$ and has an error term of the form

$$
{ \frac { f ^ { ( n + 1 ) } ( \xi ( x ) ) } { ( n + 1 ) ! } } ( x - x _ { 0 } ) ^ { n + 1 } .
$$

The Lagrange polynomial of degree $\pmb { n }$ uses information at the distinct numbers $x _ { 0 } , x _ { 1 }$ $\cdots , x _ { n }$ and, in place of $( x - x _ { 0 } ) ^ { n }$ , its error formula uses a product of the $n + 1$ terms $( x - x _ { 0 } ) , ( x - x _ { 1 } ) , \ldots , ( x - x _ { n } )$ ：

$$
\frac { f ^ { ( n + 1 ) } ( \xi ( x ) ) } { ( n + 1 ) ! } ( x - x _ { 0 } ) ( x - x _ { 1 } ) \cdot \cdot \cdot ( x - x _ { n } ) .
$$

The specific use of this error formula is restricted to those functions whose derivatives have known bounds.

Suppose a table is to be prepared for the function $f ( x ) = e ^ { x }$ ,for $x$ in [0,1]. Assume the number of decimal places to be given per entry is $d \geq 8$ and that the difference between adjacent $\pmb { x }$ -values, the step size, is h. What should $\pmb { h }$ be for linear interpolation (that is, the Lagrange polynomial of degree 1) to give an absolute error of at most $1 0 ^ { - 6 } ?$

Let $x _ { 0 } , x _ { 1 } , \ldots$ . be the numbers at which $f$ is evaluated, $\pmb { x }$ be in [0,1],and suppose $j$ satisfies $x _ { j } \leq x \leq x _ { j + 1 }$ . Eq. (3.3) implies that the error in linear interpolation is

$$
| f ( x ) - P ( x ) | = \left| \frac { f ^ { ( 2 ) } ( \xi ) } { 2 ! } ( x - x _ { j } ) ( x - x _ { j + 1 } ) \right| = \frac { | f ^ { ( 2 ) } ( \xi ) | } { 2 } | ( x - x _ { j } ) | | ( x - x _ { j + 1 } ) | ,
$$

Since the step size is $\pmb { h }$ , it follows that $x _ { j } = j h , x _ { j + 1 } = ( j + 1 ) h$ and

$$
| f ( x ) - P ( x ) | \leq { \frac { | f ^ { ( 2 ) } ( \xi ) | } { 2 ! } } | ( x - j h ) ( x - ( j + 1 ) h ) | .
$$

Hence,

$$
\begin{array} { l } { \displaystyle { | f ( x ) - P ( x ) | \le \frac { 1 } { 2 } \operatorname* { m a x } _ { \xi \in [ 0 , 1 ] } e ^ { \xi } \operatorname* { m a x } _ { x _ { j } \le x \le x _ { j + 1 } } | ( x - j h ) ( x - ( j + 1 ) h ) | } } \\ { \displaystyle { \le \frac { 1 } { 2 } e \operatorname* { m a x } _ { x _ { j } \le x \le x _ { j + 1 } } | ( x - j h ) ( x - ( j + 1 ) h ) | . } } \end{array}
$$

By considering $g ( x ) = ( x - j h ) ( x - ( j + 1 ) h )$ ,for $j h \leq x \leq ( j + 1 ) h$ , and using the Extreme Value Theorem (see Exercise 28), we find that

$$
\operatorname* { m a x } _ { \substack { x _ { j } \leq x \leq x _ { j + 1 } } } \vert ( x - j h ) ( x - ( j + 1 ) h ) \vert = \operatorname* { m a x } _ { \substack { x _ { j } \leq x \leq x _ { j + 1 } } } \vert g ( x ) \vert = \left. g \left( \left( j + \frac { 1 } { 2 } \right) h \right) \right. = \frac { h ^ { 2 } } { 4 } .
$$

Consequently, the error in linear interpolation is bounded by

$$
| f ( x ) - P ( x ) | \leq { \frac { e h ^ { 2 } } { 8 } } ,
$$

and it is sufficient for $h$ to be chosen so that

$$
\frac { e h ^ { 2 } } { 8 } \leq 1 0 ^ { - 6 } , \quad \mathrm { w h i c h i m p l i e s t h a t } \quad h < 1 . 7 2 \times 1 0 ^ { - 3 } .
$$

Since $n = ( 1 - 0 ) / h$ must be an integer, one logical choice for the step size is $h = 0 . 0 0 1$

The next example illustrates interpolation for a situation when the eror portion of Eq. (3.3) cannot be used.

# EXAMPLE 3

Table 3.2 lists values of a function at various points. The approximations to $f ( 1 . 5 )$ obtained by various Lagrange polynomials will be compared.

Table 3.2   

<table><tr><td></td></tr><tr><td>f(x) x</td></tr><tr><td>1.0 0.7651977</td></tr><tr><td></td></tr><tr><td>1.3 0.6200860</td></tr><tr><td>1.6 0.4554022</td></tr><tr><td>1.9 0.2818186 2.2 0.1103623</td></tr></table>

Since 1.5 is between 1.3 and 1.6, the most appropriate linear polynomial uses $x _ { 0 } = 1 . 3$ and $x _ { 1 } = 1 . 6$ . The value of the interpolating polynomial at 1.5 is

$$
P _ { 1 } ( 1 . 5 ) = { \frac { ( 1 . 5 - 1 . 6 ) } { ( 1 . 3 - 1 . 6 ) } } ( 0 . 6 2 0 0 8 6 0 ) + { \frac { ( 1 . 5 - 1 . 3 ) } { ( 1 . 6 - 1 . 3 ) } } ( 0 . 4 5 5 4 0 2 2 ) = 0 . 5 1 0 2 9 6 8 .
$$

Two polynomials of degree 2 can reasonably be used, one by letting $x _ { 0 } = 1 . 3 , x _ { 1 } = 1 . 6$ ， and $x _ { 2 } = 1 . 9$ , which gives

$$
\begin{array} { l } { P _ { 2 } ( 1 . 5 ) = \displaystyle \frac { ( 1 . 5 - 1 . 6 ) ( 1 . 5 - 1 . 9 ) } { ( 1 . 3 - 1 . 6 ) ( 1 . 3 - 1 . 9 ) } ( 0 . 6 2 0 0 8 6 0 ) + \displaystyle \frac { ( 1 . 5 - 1 . 3 ) ( 1 . 5 - 1 . 9 ) } { ( 1 . 6 - 1 . 3 ) ( 1 . 6 - 1 . 9 ) } ( } \\ { + \displaystyle \frac { ( 1 . 5 - 1 . 3 ) ( 1 . 5 - 1 . 6 ) } { ( 1 . 9 - 1 . 3 ) ( 1 . 9 - 1 . 6 ) } ( 0 . 2 8 1 8 1 8 6 ) } \\ { = 0 . 5 1 1 2 8 5 7 , } \end{array}
$$

and the other by letting $x _ { 0 } = 1 . 0 , x _ { 1 } = 1 . 3$ ,and $x _ { 2 } = 1 . 6$ ,which gives

$$
{ \hat { P } } _ { 2 } ( 1 . 5 ) = 0 . 5 1 2 4 7 1 5 .
$$

In the third-degree case, there are also two reasonable choices for the polynomial. One is with $x _ { 0 } = 1 . 3 , x _ { 1 } = 1 . 6 , x _ { 2 } = 1 . 9$ ,and $x _ { 3 } = 2 . 2$ , which gives

$$
P _ { 3 } ( 1 . 5 ) = 0 . 5 1 1 8 3 0 2 .
$$

The other is obtained by letting $x _ { 0 } = 1 . 0 , x _ { 1 } = 1 . 3 , x _ { 2 } = 1 . 6 ,$ and $x _ { 3 } = 1 . 9$ , which gives

$$
\hat { P } _ { 3 } ( 1 . 5 ) = 0 . 5 1 1 8 1 2 7 .
$$

The fourth-degree Lagrange polynomial uses allthe entries in the table. With $x _ { 0 } = 1 . 0$ ， $x _ { 1 } = 1 . 3 , x _ { 2 } = 1 . 6 , x _ { 3 } = 1 . 9$ ,and $x _ { 4 } = 2 . 2$ ,the approximation is

$$
P _ { 4 } ( 1 . 5 ) = 0 . 5 1 1 8 2 0 0 .
$$

Since $P _ { 3 } ( 1 . 5 )$ ， $\hat { P } _ { 3 } ( 1 . 5 )$ ,and $P _ { 4 } ( 1 . 5 )$ all agree to within $2 \times 1 0 ^ { - 5 }$ units, we expect this degree of accuracy for these approximations. We also expect $P _ { 4 } ( 1 . 5 )$ to be the most accurate approximation, since it uses more of the given data.

The function we are approximating is the Bessel function of the first kind of order zero,whose value at 1.5 is known to be 0.5118277. Therefore, the true accuracies of the approximations are as follows:

$$
\begin{array} { r l } & { | P _ { 1 } ( 1 . 5 ) - f ( 1 . 5 ) | \approx 1 . 5 3 \times 1 0 ^ { - 3 } , } \\ & { | P _ { 2 } ( 1 . 5 ) - f ( 1 . 5 ) | \approx 5 . 4 2 \times 1 0 ^ { - 4 } , } \\ & { | \hat { P } _ { 2 } ( 1 . 5 ) - f ( 1 . 5 ) | \approx 6 . 4 4 \times 1 0 ^ { - 4 } , } \\ & { | P _ { 3 } ( 1 . 5 ) - f ( 1 . 5 ) | \approx 2 . 5 \times 1 0 ^ { - 6 } , } \\ & { | \hat { P } _ { 3 } ( 1 . 5 ) - f ( 1 . 5 ) | \approx 1 . 5 0 \times 1 0 ^ { - 5 } , } \\ & { | P _ { 4 } ( 1 . 5 ) - f ( 1 . 5 ) | \approx 7 . 7 \times 1 0 ^ { - 6 } . } \end{array}
$$

Although $P _ { 3 } ( 1 . 5 )$ is the most accurate approximation, if we had no knowledge of the actual value of $f ( 1 . 5 )$ , we would accept $P _ { 4 } ( 1 . 5 )$ as the best approximation since it includes the most data about the function. The Lagrange error term derived in Theorem 3.3 cannot be applied here since no knowledge of the fourth derivative of $f$ is available. Unfortunately, this is generally the case.

A practical difficulty with Lagrange interpolation is that since the error term is difficult to apply, the degree of the polynomial needed for the desired accuracy is generally not known until computations are determined. The usual practice is to compute the results given from various polynomials until appropriate agreement is obtained, as was done in the previous example. However, the work done in calculating the approximation by the second polynomial does not lessen the work needed to calculate the third approximation; nor is the fourth approximation easier to obtain once the third approximation is known, and so on. We will now derive these approximating polynomials in a manner that uses the previous calculations to greater advantage.

# Definition 3.4

Let $f$ be a function defined at $x _ { 0 } , x _ { 1 } , x _ { 2 } , \ldots , x _ { n }$ , and suppose that $m _ { 1 } , m _ { 2 } , \ldots , m _ { k }$ are $k$ distinct integers, with $0 \leq m _ { i } \leq n$ for each $i$ . The Lagrange polynomial that agrees with $f ( x )$ at the $k$ points $x _ { m _ { 1 } } , x _ { m _ { 2 } } , \ldots , x _ { m _ { k } }$ is denoted $P _ { m _ { 1 } , m _ { 2 } , \ldots , m _ { k } } ( x )$

# EXAMPLE 4

If $x _ { 0 } = 1$ ， $x _ { 1 } = 2$ ， $x _ { 2 } = 3$ ， $x _ { 3 } = 4$ ， $x _ { 4 } = 6$ and $f ( x ) = e ^ { x }$ ,then $P _ { 1 , 2 , 4 } ( x )$ is the polynomial that agrees with $f ( x )$ at $x _ { 1 } = 2$ ， $x _ { 2 } = 3$ ,and $x _ { 4 } = 6$ ; that is.

$$
P _ { 1 , 2 , 4 } ( x ) = \frac { ( x - 3 ) ( x - 6 ) } { ( 2 - 3 ) ( 2 - 6 ) } e ^ { 2 } + \frac { ( x - 2 ) ( x - 6 ) } { ( 3 - 2 ) ( 3 - 6 ) } e ^ { 3 } + \frac { ( x - 2 ) ( x - 3 ) } { ( 6 - 2 ) ( 6 - 3 ) } e ^ { 6 } .
$$

The next result describes a method for recursively generating Lagrange polynomial approximations.

# Theorem 3.5

Let $f$ be defined at $x _ { 0 } , x _ { 1 } , \ldots , x _ { k }$ ,and let $x _ { j }$ and $x _ { i }$ be two distinct numbers in this set. Then

$$
P ( x ) = { \frac { ( x - x _ { j } ) P _ { 0 , 1 , \ldots , j - 1 , j + 1 , \ldots , k } ( x ) - ( x - x _ { i } ) P _ { 0 , 1 , \ldots , i - 1 , i + 1 , \ldots , k } ( x ) } { ( x _ { i } - x _ { j } ) } }
$$

describes the $k$ th Lagrange polynomial that interpolates $f$ at the $k + 1$ points $x _ { 0 } , x _ { 1 } , \ldots , x _ { k }$

Proof For ease of notation, let $Q \equiv P _ { 0 , 1 , \dots , i - 1 , i + 1 , \dots , k }$ and $\hat { Q } \equiv P _ { 0 , 1 , \dots , j - 1 , j + 1 , \dots , k }$ Since $Q ( x )$ and ${ \hat { Q } } ( x )$ are polynomials of degree $k - 1$ or less, $P ( x )$ is of degree at most $k$ .If $0 \leq r \leq k$ and $r \neq i , j$ ,then $Q ( x _ { r } ) = { \mathbf { \bar { Q } } } ( x _ { r } ) = f ( x _ { r } )$ ,so

$$
P ( x _ { r } ) = { \frac { ( x _ { r } - x _ { j } ) { \hat { Q } } ( x _ { r } ) - ( x _ { r } - x _ { i } ) Q ( x _ { r } ) } { x _ { i } - x _ { j } } } = { \frac { ( x _ { i } - x _ { j } ) } { ( x _ { i } - x _ { j } ) } } f ( x _ { r } ) = f ( x _ { r } ) .
$$

Moreover, since ${ \hat { Q } } ( x _ { i } ) = f ( x _ { i } )$ , we have

$$
P ( x _ { i } ) = { \frac { ( x _ { i } - x _ { j } ) { \hat { Q } } ( x _ { i } ) - ( x _ { i } - x _ { i } ) Q ( x _ { i } ) } { x _ { i } - x _ { j } } } = { \frac { ( x _ { i } - x _ { j } ) } { ( x _ { i } - x _ { j } ) } } f ( x _ { i } ) = f ( x _ { i } ) .
$$

Similarly， since $Q ( x _ { j } ) ~ = ~ f ( x _ { j } )$ ， we have $P ( x _ { j } ) ~ = ~ f ( x _ { j } )$ . But, by definition, $P _ { 0 , 1 , \dots , k } ( x )$ is the unique polynomial of degree at most $k$ that agrees with $f$ at $x _ { 0 } , x _ { 1 } , \ldots , x _ { k }$ Thus, $\pmb { P } \equiv P _ { 0 , 1 , \dots , k }$ ...

Theorem 3.5 implies that the interpolating polynomials can be generated recursively. For example,they can be generated in the manner shown in Table 3.3, where each row is completed before the succeeding rows are begun.

Table 3.3

<table><tr><td>x0 X1</td><td>P= Q0.0 P= Q10</td><td>P0.1 = Q1.1 P1.2 = Q2,1</td><td>P0,1.2 = Q2,2</td><td></td><td></td></tr><tr><td>x2 x3</td><td>P= Q2.0 P=Q3.0</td><td>P2.3 = Q3,1</td><td>P1,2.3 = Q3,2</td><td>P0,1,2.3 = Q3,3</td><td></td></tr><tr><td>x4</td><td>P4 = Q4.0</td><td>P3.4 = Q4.1</td><td>P2,3.4 = Q4.2</td><td>P1,2.3.4 = Q4.3</td><td>P0,1,2.3.4 = Q4.4</td></tr></table>

This procedure is called Neville's method.The $P$ notation used in Table 3.3 is cumbersome because of the number of subscripts used to represent the entries. Note, however, that as an array is being constructed,only two subscripts are needed. Proceeding down the table corresponds to using consecutive points $x _ { i }$ with larger $i$ ,and proceeding to the right corresponds to increasing the degree of the interpolating polynomial. Since the points appear consecutively in each entry, we need to describe only a starting point and the number of additional points used in constructing the approximation.

To avoid the multiple subscripts, let $Q _ { i , j } ( x )$ ,for $0 \le j \le i$ ,denote the interpolating polynomial of degree $j$ on the $( j + 1 )$ numbers $x _ { i - j } , x _ { i - j + 1 } , \dotsc , x _ { i - 1 } , x _ { i }$ ; that is,

$$
Q _ { i , j } = P _ { i - j , i - j + 1 , \dots , i - 1 , i } .
$$

Using this notation for Neville's method provides the $Q$ notation array in Table 3.3.

Values of various interpolating polynomials at $x = 1 . 5$ were obtained in Example 3 using the data shown in the first two columns of Table 3.4. In this example,we approximate $f ( 1 . 5 )$ using the result in Theorem 3.5. If $x _ { 0 } = 1 . 0 , x _ { 1 } = 1 . 3 , x _ { 2 } = 1 . 6 , x _ { 3 } = 1 . 9$ ,and $x _ { 4 } = 2 . 2$ ，then $Q _ { 0 , 0 } \ = \ f ( 1 . 0 ) , \ Q _ { 1 , 0 } \ = \ f ( 1 . 3 ) , \ Q _ { 2 , 0 } \ = \ f ( 1 . 6 ) , \ Q _ { 3 , 0 } \ = \ f ( 1 . 9 )$ , and $Q _ { 4 , 0 } = f ( 2 . 2 )$ . These are the five polynomials of degree zero (constants) that approximate $f ( 1 . 5 )$

Calculating the first-degree approximation $Q _ { 1 , 1 } ( 1 . 5 )$ gives

$$
\begin{array} { r l } & { \mathcal { Q } _ { 1 , 1 } ( 1 . 5 ) = \frac { \left( x - x _ { 0 } \right) Q _ { 1 , 0 } - \left( x - x _ { 1 } \right) Q _ { 0 , 0 } } { x _ { 1 } - x _ { 0 } } } \\ & { \quad \quad \quad \quad = \frac { ( 1 . 5 - 1 . 0 ) Q _ { 1 , 0 } - \left( 1 . 5 - 1 . 3 \right) Q _ { 0 , 0 } } { 1 . 3 - 1 . 0 } } \\ & { \quad \quad \quad = \frac { 0 . 5 ( 0 . 6 2 0 0 8 6 0 ) - 0 . 2 ( 0 . 7 6 5 1 9 7 7 ) } { 0 . 3 } = 0 . 5 2 3 3 4 4 9 . } \end{array}
$$

Similarly,

$$
Q _ { 2 , 1 } ( 1 . 5 ) = { \frac { ( 1 . 5 - 1 . 3 ) ( 0 . 4 5 5 4 0 2 2 ) - ( 1 . 5 - 1 . 6 ) ( 0 . 6 0 0 8 6 0 ) } { 1 . 6 - 1 . 3 } } = 0 . 5 1 0 2 9 6 8 ,
$$

The best linear approximation is expected to be $Q _ { 2 , 1 }$ since 1.5 is between $x _ { 1 } = 1 . 3$ and $x _ { 2 } = 1 . 6$

In a similar manner, approximations using higher-degree polynomials are given by

$$
Q _ { 2 , 2 } ( 1 . 5 ) = \frac { ( 1 . 5 - 1 . 0 ) ( 0 . 5 1 0 2 9 6 8 ) - ( 1 . 5 - 1 . 6 ) ( 0 . 5 2 3 3 4 4 9 ) } { 1 . 6 - 1 . 0 } = 0 . 5 1 2 4 7 1 5 ,
$$

The higher-degree approximations are generated in a similar manner and are shown in Table 3.4.

# Table 3.4

<table><tr><td>1.0</td><td>0.7651977</td><td></td><td></td><td></td><td></td></tr><tr><td>1.3</td><td>0.6200860</td><td>0.5233449</td><td></td><td></td><td></td></tr><tr><td>1.6</td><td>0.4554022</td><td>0.5102968</td><td>0.5124715</td><td></td><td></td></tr><tr><td>1.9</td><td>0.2818186</td><td>0.5132634</td><td>0.5112857</td><td>0.5118127</td><td></td></tr><tr><td>2.2</td><td>0.1103623</td><td>0.5104270</td><td>0.5137361</td><td>0.5118302</td><td>0.5118200</td></tr></table>

If the latest approximation, $Q _ { 4 , 4 }$ ,is not sufficiently accurate,another node, $x _ { 5 }$ ,can be selected,and another row added to the table:

$$
x _ { 5 } \quad Q _ { 5 , 0 } \quad Q _ { 5 , 1 } \quad Q _ { 5 , 2 } \quad Q _ { 5 , 3 } \quad Q _ { 5 , 4 } \quad Q _ { 5 , 5 } .
$$

Then $Q _ { 4 , 4 } , Q _ { 5 , 4 }$ ,and $Q { \mathfrak { s } } , { \mathfrak { s } }$ can be compared to determine further accuracy.

In our example, the function is the Bessel function of the first kind of order zero, whose value at 2.5 is -0.0483838, and a new row of approximations to $f ( 1 . 5 )$ is

2.5- 0.04838380.48076990.5301984 0.5119070 0.51184300.5118277.

The final new entry, 0.5118277,is correct to seven decimal places.

# EXAMPlE 6

Table 3.5 lists the values of $f ( x ) = \ln x$ accurate to the places given.

Table 3.5   

<table><tr><td>i Xi</td><td>ln xi</td></tr><tr><td>0</td><td>2.0 0.6931</td></tr><tr><td>1</td><td>2.2 0.7885</td></tr><tr><td>2</td><td>2.3 0.8329</td></tr></table>

We will use Neville's method to approximate $f ( 2 . 1 ) = \ln 2 . 1$ . Completing the table gives the entries in Table 3.6.

Table 3.6   

<table><tr><td>i</td><td>Xi</td><td>x-xi</td><td>Qi0</td><td>Qi1</td><td>Qi2</td></tr><tr><td>0</td><td>2.0</td><td>0.1</td><td>0.6931</td><td></td><td></td></tr><tr><td>1</td><td>2.2</td><td>-0.1</td><td>0.7885</td><td>0.7410</td><td></td></tr><tr><td>2</td><td>2.3</td><td>-0.2</td><td>0.8329</td><td>0.7441</td><td>0.7420</td></tr></table>

Thus, $P _ { 2 } ( 2 . 1 ) = Q _ { 2 2 } = 0 . 7 4 2 0$ . Since $f ( 2 . 1 ) = \ln 2 . 1 = 0 . 7 4 1 9$ to four decimal places,the absolute error is

$$
\begin{array} { r l } { | f ( 2 . 1 ) - P _ { 2 } ( 2 . 1 ) | = | 0 . 7 4 1 9 - 0 . 7 4 2 0 | } & { { } } \\ { = 1 0 ^ { - 4 } . } \end{array}
$$

However, $f ^ { \prime } ( x ) = 1 / x , f ^ { \prime \prime } ( x ) = - 1 / x ^ { 2 }$ ，and $f ^ { \prime \prime \prime } ( x ) \ = \ 2 / x ^ { 3 }$ ， so the Lagrange error formula (3.3) gives an error bound

$$
\begin{array} { r l r } {  { | f ( 2 , 1 ) - P _ { 2 } ( 2 , 1 ) | = | \frac { f ^ { \prime \prime \prime } ( \xi ) } { 3 ! } ( x - x _ { 0 } ) ( x - x _ { 1 } ) ( x - x _ { 2 } ) | } } \\ & { } & { = | \frac { 1 } { 3 \xi ^ { 3 } } ( 0 . 1 ) ( - 0 . 1 ) ( - 0 . 2 ) | \le 8 . { \overline { { 3 } } } \times 1 0 ^ { - 5 } . } \end{array}
$$

Notice that the actual error, $1 0 ^ { - 4 }$ , exceeds the error bound, $8 . \mathcal { \overline { { 3 } } } \times 1 0 ^ { - 5 }$ . This apparent contradiction is a consequence of finite-digit computations. We used four-digit approximations,and the Lagrange error formula (3.3) assumes infinite-digit arithmetic. This caused our actual errors to exceed the theoretical error estimate.

Algorithm 3.1 constructs the entries in Neville's method by rows.

# Neville's Iterated Interpolation

To evaluate the interpolating polynomial $P$ on the $n + 1$ distinct numbers $x _ { 0 } , \ldots , x _ { n }$ at the number $x$ for the function $f$ ：

INPUTnumbers $x , x _ { 0 } , x _ { 1 } , \ldots , x _ { n }$ ; values $f ( { \boldsymbol { x } } _ { 0 } ) , f ( { \boldsymbol { x } } _ { 1 } ) , \ldots , f ( { \boldsymbol { x } } _ { n } )$ as the first column $Q _ { 0 , 0 } , Q _ { 1 , 0 } , \ldots , Q _ { n , 0 } \circ$ f $Q$ ：

OUTPUT the table $Q$ with $P ( x ) = Q _ { n , n }$

Step 1 For i = 1,2,...,n for $j = 1 , 2 , \dots , i$ $\sec Q _ { i , j } = { \frac { ( x - x _ { i - j } ) Q _ { i , j - 1 } - ( x - x _ { i } ) Q _ { i - 1 , j - 1 } } { x _ { i } - x _ { i - j } } } .$

Step 2 OUTPUT $( Q )$ ； STOP.

The algorithm can be modified to allow for the addition of new interpolating nodes. For example, the inequality

$$
| Q _ { i , i } - Q _ { i - 1 , i - 1 } | < \varepsilon
$$

can be used as a stopping criterion, where $\pmb { \varepsilon }$ is a prescribed error tolerance. If the inequal-ity is true, $Q _ { i , i }$ is a reasonable approximation to $f ( x )$ . If the inequality is false, a new interpolation point, $x _ { i + 1 }$ , is added.

# ExERCIsE SEt 3.1

1.For the given functions $f ( x )$ ,let $x _ { 0 } = 0$ ， $x _ { 1 } = 0 . 6$ and $x _ { 2 } = 0 . 9$ . Construct interpolation polynomials of degree at most one and at most two to approximate $f ( 0 . 4 5 )$ , and find the actual error.

a. $f ( x ) = \cos x$ $\begin{array} { r l } { \mathbf { b } . \quad } & { { } f ( x ) = { \sqrt { 1 + x } } } \\ { \mathbf { d } . \quad } & { { } f ( x ) = \tan x } \end{array}$   
c. $f ( x ) = \ln ( x + 1 )$

2.Use Theorem 3.3 to find an error bound for the approximations in Exercise 1.

3.Use appropriate Lagrange interpolating polynomials of degrees one, two, and thre to approximate each of the following:

a. $f ( 8 . 4 )$ if $\begin{array} { r c l } { { f ( 8 . 1 ) ~ = ~ 1 6 . 9 4 4 1 0 , ~ f ( 8 . 3 ) ~ = ~ 1 7 . 5 6 4 9 2 , ~ f ( 8 . 6 ) ~ = ~ 1 8 . 5 0 5 1 5 , ~ f ( 8 . 7 ) ~ = ~ 1 8 . 8 0 9 2 , } } \\ { { } } & { { } } & { { } } \\ { { f ( - 0 . 7 5 ) ~ = ~ - 0 . 0 7 1 8 1 2 5 0 , ~ f ( - 0 . 5 ) ~ = ~ - 0 . 0 2 4 7 5 0 0 0 , ~ f ( - 0 . 2 5 ) ~ = ~ - 0 . 0 2 4 7 5 0 . } } \end{array}$ 18.82091   
b. $f ( - \frac { 1 } { 3 } )$ if 0.33493750, $f ( 0 ) = 1 . 1 0 1 0 0 0 0 0$   
c. $f ( 0 . 2 5 )$ if $f ( 0 . 1 ) ~ = ~ 0 . 6 2 0 4 9 9 5 8$ ， $f ( 0 . 2 ) ~ = ~ - 0 . 2 8 3 9 8 6 6 8$ ， $f ( 0 . 3 ) ~ = ~ 0 . 0 0 6 6 0 0 9 5 ,$ $f ( 0 . 4 ) = 0 . 2 4 8 4 2 4 4 0$   
d. $f ( 0 . 9 )$ if $f ( 0 . 6 ) ~ = ~ - 0 . 1 7 6 9 4 4 6 0$ ，f(0.7)= 0.01375227, $f ( 0 . 8 ) ~ = ~ 0 . 2 2 3 6 3 3 6 2 .$ $f ( 1 . 0 ) = 0 . 6 5 8 0 9 1 9 7$

4.Use Neville's method to obtain the approximations for Exercise 3.

5.Use Nevile's method to approximate $\sqrt { 3 }$ with the function $f ( x ) = 3 ^ { x }$ and the values $x _ { 0 } = - 2$ $x _ { 1 } = - 1 , x _ { 2 } = 0 , x _ { 3 } = 1$ ,and $x _ { 4 } = 2$

6.Use Nevile's method to approximate $\sqrt { 3 }$ with the function $f ( x ) = { \sqrt { x } }$ and the values $x _ { 0 } = 0$ $x _ { 1 } = 1 , x _ { 2 } = 2 , x _ { 3 } = 4$ ,and $x _ { 4 } = 5$ . Compare the accuracy with that of Exercise 5.

7.The data for Exercise 3 were generated using the following functions. Use the error formula to find a bound for the error, and compare the bound to the actual error for the cases $n \stackrel { } { \mathop { \mathbf { \Gamma } } } = 1$ and $n = 2$

a. $\begin{array} { l } { f ( x ) = x \ln x } \\ { f ( x ) = x ^ { 3 } + 4 . 0 0 1 x ^ { 2 } + 4 . 0 0 2 x + 1 . 1 0 1 } \\ { f ( x ) = x \cos x - 2 x ^ { 2 } + 3 x - 1 } \\ { . } \end{array}$   
b.   
c.   
d. $f ( x ) = \sin ( e ^ { x } - 2 )$

8. Let $f ( x ) = { \sqrt { x - x ^ { 2 } } }$ and $P _ { 2 } ( x )$ be the interpolation polynomial on $x _ { 0 } = 0 , x _ { 1 }$ and $x _ { 2 } = 1$ Find the largest value of $x _ { 1 }$ in $( 0 , 1 )$ for which $f ( 0 . 5 ) - P _ { 2 } ( 0 . 5 ) = - 0 . 2 5$

9.Let $P _ { 3 } ( x )$ be the interpolating polynomial for the data $( 0 , 0 )$ ,(0.5,y), (1,3),and (2,2). Find $y$ if the coefficient of $x ^ { 3 }$ in $P _ { 3 } ( x )$ is 6.

10.Use the Lagrange interpolating polynomial of degree three or less and four-digit chopping arithmetic to approximate cos O.75O using the following values. Find an error bound for the approximation.

$$
\cos 0 . 6 9 8 = 0 . 7 6 6 1 \quad \cos 0 . 7 3 3 = 0 . 7 4 3 2 \quad \cos 0 . 7 6 8 = 0 . 7 1 9 3 \quad \cos 0 . 8 0 3 = 0 . 6 9 4 6
$$

The actual value of cos 0.75Ois 0.7317(to four decimal places). Explain the discrepancy between the actual error and the error bound.

11. Usethe following values and four-digit rounding arithmetic toconstruct a third Lagrange poly-nomial approximation to $f ( 1 . 0 9 )$ . The function being approximated is $f ( x ) = \log _ { 1 0 } ( \tan x )$ Use this knowledge to find a bound for the error in the approximation.

$$
f ( 1 . 0 0 ) = 0 . 1 9 2 4 \quad f ( 1 . 0 5 ) = 0 . 2 4 1 4 \quad f ( 1 . 1 0 ) = 0 . 2 9 3 3 \quad f ( 1 . 1 5 ) = 0 . 3 4 9 2
$$

12.Repeat Exercise 11 using Maple and ten-digit rounding arithmetic.

13.Neville's method is used to approximate $f ( 0 . 5 )$ ，giving the following table.

$$
\begin{array} { l l l } { \overline { { x _ { 0 } = 0 } } } & { P _ { 0 } = 0 } \\ { \overline { { x _ { 1 } = 0 . 4 } } } & { P _ { 1 } = 2 . 8 } & { P _ { 0 1 } = 3 . 5 } \\ { \overline { { x _ { 2 } = 0 . 7 } } } & { P _ { 2 } } & { P _ { 1 2 } } & { P _ { 0 1 2 } = \overline { { 7 } } } \end{array}
$$

Determine $P _ { 2 } = f ( 0 . 7 )$

14.Neville's method is used to approximate $f ( 0 . 4 )$ , giving the following table.

$$
\begin{array} { l l l l } { { } } & { { x _ { 0 } = 0 } } & { { P _ { 0 } = 1 } } & { { } } \\ { { x _ { 1 } = 0 . 2 5 } } & { { P _ { 1 } = 2 } } & { { P _ { 0 1 } = 2 . 6 } } & { { } } \\ { { x _ { 2 } = 0 . 5 } } & { { P _ { 2 } } } & { { P _ { 1 2 } } } & { { P _ { 0 1 2 } } } \\ { { x _ { 3 } = 0 . 7 5 } } & { { P _ { 3 } = 8 } } & { { P _ { 2 3 } = 2 . 4 } } & { { P _ { 1 2 3 } = 2 . 9 6 \quad P _ { 0 1 2 3 } = 3 . 0 1 6 } } \end{array}
$$

Determine $P _ { 2 } = f ( 0 . 5 )$ ·

15.Construct the Lagrange interpolating polynomials for the following functions,and find a bound for the absolute error on the interval $[ x _ { 0 } , x _ { n } ]$ ·

a. $f ( x ) = e ^ { 2 x } \cos 3 x , \quad x _ { 0 } = 0 , x _ { 1 } = 0 . 3 , x _ { 2 } = 0 . 6 , n = 2$ $\mathbf { b } .$ $f ( x ) = \sin ( \ln x ) , \quad x _ { 0 } = 2 . 0 , x _ { 1 } = 2 . 4 , x _ { 2 } = 2 . 6 , n = 2$ c. f(x)= In x, $x _ { 0 } = 1 , x _ { 1 } = 1 . 1 , x _ { 2 } = 1 . 3 , x _ { 3 } = 1 . 4 , n = 3$ d. $f ( x ) = \cos x + \sin x , \quad x _ { 0 } = 0 , x _ { 1 } = 0 . 2 5 , x _ { 2 } = 0 . 5 , x _ { 3 } = 1 . 0 , n = 3$

16.Let $f ( x ) = e ^ { x }$ ,for $0 \leq x \leq 2$

a. Approximate $f ( 0 . 2 5 )$ using linear interpolation with ${ \pmb x } _ { 0 } = { \pmb 0 }$ and $x _ { 1 } = 0 . 5$   
${ \bf { b } } .$ Approximate ${ \bf { f } } ( 0 . 7 5 )$ using linear interpolation with ${ x _ { 0 } } = 0 . 5$ and $x _ { 1 } = 1$   
c. Approximate $f ( 0 . 2 5 )$ and $f ( 0 . 7 5 )$ by using the second interpolating polynomial with ${ \mathfrak { x } } _ { 0 } = 0$ ， $x _ { 1 } = 1$ , and $x _ { 2 } = 2$   
d. Which approximations are better and why?

17.Suppose you need to construct eight-decimal-place tables for the common, or base-10, logarithm function from $x = 1$ to $x = 1 0$ in such a way that linear interpolation is accurate to within $1 0 ^ { - 6 }$ . Determine a bound for the step size for this table.What choice of step size would you make to ensure that $x = 1 0$ is included in the table?

18.Suppose $x _ { j } = j$ ,for $j = 0 , 1 , 2 , 3$ and it is known that

$$
P _ { 0 , 1 } ( x ) = x + 1 , \quad P _ { 1 , 2 } ( x ) = 3 x - 1 , \quad \mathrm { a n d } \quad P _ { 1 , 2 , 3 } ( 1 . 5 ) = 4 .
$$

Find $P _ { 0 , 1 , 2 , 3 }$ (1.5).

19.Suppose $x _ { j } = j$ ,for $j = 0 , 1 , 2 , 3$ and it is known that

$$
P _ { 0 , 1 } ( x ) = 2 x + 1 , \quad P _ { 0 , 2 } ( x ) = x + 1 , \quad \mathrm { a n d } \quad P _ { 1 , 2 , 3 } ( 2 . 5 ) = 3 .
$$

Find $P _ { 0 , 1 , 2 , 3 } ( 2 . 5 )$

20.Neville's Algorithm is used to approximate $f ( 0 )$ using $f ( - 2 ) , f ( - 1 ) , f ( 1 )$ ,and $f ( 2 )$ . Sup-pose $f ( - 1 )$ was overstated by 2 and $f ( 1 )$ was understated by 3. Determine the error in the original calculation of the value of the interpolating polynomial to approximate $f ( 0 )$

21. Construct a sequence of interpolating values $y _ { n }$ to $f ( 1 + { \sqrt { 1 0 } } )$ ， where $f ( x ) = ( 1 + x ^ { 2 } ) ^ { - 1 }$ for $- 5 \leq x \leq 5$ , as follows: For each $n = 1 , 2 , \ldots ,$ 10, let $h = 1 0 / n$ and $y _ { n } = P _ { n } ( 1 + { \sqrt { 1 0 } } )$ ， where ${ \cal P } _ { n } ( x )$ istheiterpotilfo $f ( x )$ at the odes $x _ { 0 } ^ { ( n ) } , x _ { 1 } ^ { ( n ) } , \ldots , x _ { n } ^ { ( n ) }$ and

$x _ { j } ^ { ( n ) } = - 5 + j h$ , for each $j = 0 , 1 , 2 , \ldots , n$ . Does the sequence $\{ y _ { n } \}$ appear to converge to $f ( 1 + { \sqrt { 1 0 } } ) \ ?$

Inverse Interpolation Suppose $f \in C ^ { 1 } [ a , b ] , f ^ { \prime } ( x ) \neq 0$ on $[ a , b ]$ and $f$ has one zero $p$ in $[ a , b ]$ . Let $x _ { 0 } , \ldots , x _ { n }$ ，be $n + 1$ distinct numbers in $[ a , b ]$ with $f ( x _ { k } ) = y _ { k }$ , for each $k = 0 , 1 , \ldots , n$ To approximate $p$ construct the interpolating polynomial of degree $\pmb { n }$ on the nodes $y _ { 0 } , \ldots , y _ { n }$ for $f ^ { - 1 }$ . Since $y _ { k } = f ( x _ { k } )$ and $0 = f ( p )$ , it follows that $f ^ { - 1 } ( y _ { k } ) = x _ { k }$ and $p = f ^ { - 1 } ( 0 )$ . Using iterated interpolation to approximate $f ^ { - 1 } ( 0 )$ is called iterated inverse interpolation.

22.Use iterated inverse interpolation to find an approximation to the solution of $x - e ^ { - x } = 0$ ， using the data

<table><tr><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>0.3</td><td rowspan=1 colspan=1>0.4</td><td rowspan=1 colspan=1>0.5</td><td rowspan=1 colspan=1>0.6</td></tr><tr><td rowspan=1 colspan=1>e-x</td><td rowspan=1 colspan=1>0.740818</td><td rowspan=1 colspan=1>0.6703200.606531</td><td rowspan=1 colspan=1>0.6703200.606531</td><td rowspan=1 colspan=1>0.548812</td></tr></table>

23.Construct an algorithm that can be used for inverse interpolation.

24.a.The introduction to this chapter included a table listing the population of the United States from 1940 to 1990. Use Lagrange interpolation to approximate the population in the years 1930,1965,and 2010.. b. The population in 1930 was approximately 123,203,000. How accurate do you think your 1965 and 2010 figures are?

25.It is suspected that the high amounts of tannin in mature oak leaves inhibit the growth of the winter moth (Operophtera bromata $L .$ , Geometridae) larvae that extensively damage these trees in certain years. The following table lists the average weight of two samples of larvae at times in the first 28 days after birth. The first sample was reared on young oak leaves, whereas the second sample was reared on mature leaves from the same tree.

a.Use Lagrange interpolation to approximate the average weight curve for each sample.

b. Find an approximate maximum average weight for each sample by determining the maximum of the interpolating polynomial.

$$
\operatorname  \begin{array} { l } { \operatorname { D a y } } \\ { \mathrm { S a m p l e ~ 1 ~ a v e r a g e ~ w e i g h t ~ ( m g ) } } \\ { \mathrm { S a m p l e ~ 2 ~ a v e r a g e ~ w e i g h t ~ ( m g ) } } \end{array} | \begin{array} { l } { 0 } \\ { 0 . 6 7 } \\ { 6 . 6 7 } \\ { 6 . 7 } \end{array} | \begin{array} { l } { 6 } \\ { 1 7 . 3 3 } \\ { 1 6 . 1 1 } \end{array} | \begin{array} { l } { 1 0 } \\ { 4 2 . 6 7 } \\ { 1 8 . 8 9 } \end{array} | \begin{array} { l } { 1 3 } \\ { 3 7 . 3 3 } \\ { 1 5 . 0 0 } \end{array} | \begin{array} { l } { 1 7 } \\ { 3 0 . 1 0 } \\ { 0 . 5 6 } \end{array} | \begin{array} { l } { 2 0 } \\ { 2 9 . 3 1 } \\ { 9 . 4 4 } \end{array} | \begin{array} { l } { 2 8 } \\ { 2 8 . 7 4 } \end{array}
$$

26.In Exercise 24 of Section 1.1 a Maclaurin series was integrated to approximate erf(1), where $\textstyle \operatorname { e r f } ( x )$ is the normal distribution error function defined by

$$
\operatorname { e r f } ( x ) = { \frac { 2 } { \sqrt { \pi } } } \int _ { 0 } ^ { x } e ^ { - t ^ { 2 } } d t .
$$

a. Use the Maclaurin series to construct a table for $\operatorname { e r f } ( x )$ that is accurate to within $1 0 ^ { - 4 }$ for $\textstyle \operatorname { e r f } ( x _ { i } )$ , where $x _ { i } = 0 . 2 i$ ,for $i = 0 , 1 , \ldots , 5 ,$   
${ \bf { b } } .$ Use both linear interpolation and quadratic interpolation to obtain an approximation to $\operatorname { e r f } ( { \frac { 1 } { 3 } } )$ . Which approach seems most feasible?

27.Prove Theorem 1.14 by following the procedure in the proof of Theorem 3.3. [Hint: Let

$$
g ( t ) = f ( t ) - P ( t ) - \left[ f ( x ) - P ( x ) \right] \cdot { \frac { ( t - x _ { 0 } ) ^ { n + 1 } } { ( x - x _ { 0 } ) ^ { n + 1 } } } ,
$$

where $P$ is the nth Taylor polynomial, and use Theorem 1.12.]

28.Show that $\operatorname* { m a x } _ { x _ { j } \le x \le x _ { j + 1 } } | g ( x ) | = h ^ { 2 } / 4$ ,where $g ( x ) = ( x - j h ) ( x - ( j + 1 ) h )$

29.The Bernstein polynomial of degree $n$ for $f \in C [ 0 , 1 ]$ is given by

$$
B _ { n } ( x ) = \sum _ { k = 0 } ^ { n } { \binom { n } { k } } f \left( { \frac { k } { n } } \right) x ^ { k } ( 1 - x ) ^ { n - k } ,
$$

where $\binom { n } { k }$ denotes $n ! / k ! ( n - k ) !$ . These polynomials can be used in a constructive proof of the Weierstrass Approximation Theorem 3.1 (see [Bartl) since $\operatorname* { l i m } _ { n  \infty } B _ { n } ( x ) = f ( x )$ , for each $x \in \left[ 0 , 1 \right]$

a. Find $B _ { 3 } ( x )$ for the functions

i $f ( x ) = x$ ii.f(x）=1

b.Show that for each $k \leq n$ ，

$$
{ \binom { n - 1 } { k - 1 } } = { \binom { k } { n } } { \binom { n } { k } } .
$$

c. Use part (b) and the fact, from (ii) in part (a), that

$$
1 = \sum _ { k = 0 } ^ { n } { \binom { n } { k } } x ^ { k } ( 1 - x ) ^ { n - k } , \quad { \mathrm { f o r ~ e a c h } } \ n ,
$$

to show that, for $f ( x ) = x ^ { 2 }$ ，

$$
B _ { n } ( x ) = \left( { \frac { n - 1 } { n } } \right) x ^ { 2 } + { \frac { 1 } { n } } x .
$$

d.Use part (c) to estimate the value of $\pmb { n }$ necessary for $\left| B _ { n } ( x ) - x ^ { 2 } \right| \leq 1 0 ^ { - 6 }$ to hold for all $x$ in [0,1].

# 3.2 Divided Differences

Iterated interpolation was used in the previous section to generate successively higherdegree polynomial approximations at a specific point. Divided-difference methods introduced in this section are used to successively generate the polynomials themselves. Our treatment of divided-difference methods will be brief since the results in this section will not be used extensively in subsequent material. Most older texts on numerical analysis have extensive treatments of divided-difference methods. If a more comprehensive treatment is needed, the book by Hildebrand [Hild] is a particularly good reference.

Suppose that $P _ { n } ( x )$ is the $n$ th Lagrange polynomial that agrees with the function $f$ at the distinct numbers $x _ { 0 } , x _ { 1 } , \ldots , x _ { n }$ . The divided differences of $f$ with respect to $x _ { 0 } , x _ { 1 } , \ldots , x _ { n }$ are used to express $P _ { n } ( x )$ in the form

$$
\begin{array} { c } { { P _ { n } ( x ) = a _ { 0 } + a _ { 1 } ( x - x _ { 0 } ) + a _ { 2 } ( x - x _ { 0 } ) ( x - x _ { 1 } ) + \cdot \cdot \cdot } } \\ { { { } } } \\ { { + a _ { n } ( x - x _ { 0 } ) ( x - x _ { 1 } ) \cdot \cdot \cdot ( x - x _ { n - 1 } ) , } } \end{array}
$$

for appropriate constants $a _ { 0 } , a _ { 1 } , \ldots , a _ { n }$

To determine the first of these constants, $a _ { 0 }$ , note that if $P _ { n } ( x )$ is written in the form of Eq. (3.5), then evaluating $P _ { n } ( x )$ at $x _ { 0 }$ leaves only the constant term $a _ { 0 }$ ; that is,

$$
a _ { 0 } = P _ { n } ( x _ { 0 } ) = f ( x _ { 0 } ) .
$$

Similarly, when $P ( x )$ is evaluated at $x _ { 1 }$ ,the only nonzero terms in the evaluation of $P _ { n } ( x _ { 1 } )$ are the constant and linear terms,

$$
f ( x _ { 0 } ) + a _ { 1 } ( x _ { 1 } - x _ { 0 } ) = P _ { n } ( x _ { 1 } ) = f ( x _ { 1 } ) ;
$$

so

$$
a _ { 1 } = { \frac { f ( x _ { 1 } ) - f ( x _ { 0 } ) } { x _ { 1 } - x _ { 0 } } } .
$$

We now introduce the divided-difference notation, which is related to Aitken's $\Delta ^ { 2 }$ notation used in Section 2.5. The zeroth divided difference of the function $f$ with respect to $x _ { i }$ ， denoted $f \{ x _ { i } \}$ , is simply the value of $f$ at $x _ { i }$ ：

$$
f [ x _ { i } ] = f ( x _ { i } ) .
$$

The remaining divided differences are defined inductively; the first divided difference of $f$ with respect to $x _ { i }$ and $x _ { i + 1 }$ is denoted $f [ x _ { i } , x _ { i + 1 } ]$ and is defined as

$$
f [ x _ { i } , x _ { i + 1 } ] = { \frac { f [ x _ { i + 1 } ] - f [ x _ { i } ] } { x _ { i + 1 } - x _ { i } } } .
$$

The second divided difference, $f [ x _ { i } , x _ { i + 1 } , x _ { i + 2 } ]$ , is defined as

$$
f [ x _ { i } , x _ { i + 1 } , x _ { x + 2 } ] = { \frac { f [ x _ { i + 1 } , x _ { i + 2 } ] - f [ x _ { i } , x _ { i + 1 } ] } { x _ { i + 2 } - x _ { i } } } .
$$

Similarly, after the $( k - 1 )$ st divided differences,

$$
f [ x _ { i } , x _ { i + 1 } , x _ { i + 2 } , \ldots , x _ { i + k - 1 } ] \quad { \mathrm { a n d } } \quad f [ x _ { i + 1 } , x _ { i + 2 } , \ldots , x _ { i + k - 1 } , x _ { i + k } ] ,
$$

have been determined, the kth divided difference relative to $x _ { i } , x _ { i + 1 } , x _ { i + 2 } , \ldots , x _ { i + k }$ is given by

$$
f [ x _ { i } , x _ { i + 1 } , \dots , x _ { i + k - 1 } , x _ { i + k } ] = { \frac { f [ x _ { i + 1 } , x _ { i + 2 } , \dots , x _ { i + k } ] - f [ x _ { i } , x _ { i + 1 } , \dots , x _ { i + k - 1 } ] } { x _ { i + k } - x _ { i } } } .
$$

With this notation, Eq. (3.6) can be reexpressed as $a _ { 1 } = f [ x _ { 0 } , x _ { 1 } ] .$ ，and the interpolating polynomial in Eq. (3.5) is

$$
\begin{array} { l } { { P _ { n } ( x ) = f [ x _ { 0 } ] + f [ x _ { 0 } , x _ { 1 } ] ( x - x _ { 0 } ) + a _ { 2 } ( x - x _ { 0 } ) ( x - x _ { 1 } ) } } \\ { { \ ~ + \cdot \cdot \cdot + a _ { n } ( x - x _ { 0 } ) ( x - x _ { 1 } ) \cdot \cdot \cdot ( x - x _ { n - 1 } ) . } } \end{array}
$$

As might be expected from the evaluation of ${ a } _ { 0 }$ and $a _ { 1 }$ , the required constants are

$$
a _ { k } = f [ x _ { 0 } , x _ { 1 } , x _ { 2 } , \ldots , x _ { k } ] ,
$$

for each $k = 0 , 1 , \ldots , n$ .So $P _ { n } ( x )$ can be rewritten as (see [Hild, pp. 43-47])

$$
P _ { n } ( x ) = f [ x _ { 0 } ] + \sum _ { k = 1 } ^ { n } f [ x _ { 0 } , x _ { 1 } , \ldots , x _ { k } ] ( x - x _ { 0 } ) \cdot \cdot \cdot ( x - x _ { k - 1 } ) .
$$

The value of $f [ x _ { 0 } , x _ { 1 } , \dots , x _ { k } ]$ is independent of the order of the numbers $x _ { 0 } , x _ { 1 } , \ldots , x _ { k }$ ， as is shown in Exercise 17. This equation is known as Newton's interpolatory divideddifference formula. The generation of the divided differences is outlined in Table 3.7.Two fourth and one fifth difference could also be determined from these data.

Table 3.7   

<table><tr><td>xf(x）</td><td>First divided differences</td><td>Second divided differences</td><td></td><td>Third divided differences</td></tr><tr><td colspan="5">xo f[xo] flx1]-flxo] flxo，x1]=</td></tr><tr><td colspan="3">x1-x0</td><td colspan="2">f[x,x2]-f[xo，x1]</td></tr><tr><td colspan="3">x1f[x1] fxo，x1,x2]</td><td colspan="2">x2-x0</td></tr><tr><td colspan="3">f[x2]-f[x1] f[x,x2]=</td><td>f[xo,x1,x2,x3] =</td><td>f[x1,x2,x3]-f[xo,x1,x2]</td></tr><tr><td colspan="3">x2-x1 x2 f[x2] flx1,x2,x]=:</td><td>fx,x3]-f[x,x2]</td><td>x3-x0</td></tr><tr><td colspan="3">f[x3]-f[x2] f[x,x]=</td><td>x3-x1</td><td>f[x2,x3,x4]-f[x1,x,x]</td></tr><tr><td colspan="3">x-x2</td><td>f[x1,x2,x3,x4] = fx,x4]-f[x2,x]</td><td>X4-X1</td></tr><tr><td colspan="3">x f[x3] f[x2,x,x4]=</td><td>X4-X2</td><td></td></tr><tr><td colspan="3">f[x4]-f[x3] f[x,x4]=</td><td>f[x2,x3,x4,x5]=</td><td>f[x3,x4,xs]-flx2,x,x4]</td></tr><tr><td colspan="3">X4-X3</td><td>f[x4,xs]-f[x,x4]</td><td>x5-x2</td></tr><tr><td colspan="3">x4 f[x4] f[x3,x4,xs]= xs-x3</td><td></td><td></td></tr><tr><td colspan="3">f[xsl-f[x4]</td><td></td><td></td></tr><tr><td colspan="3">f[x4,xs]= X5-X4</td><td></td><td></td></tr><tr><td colspan="3"></td><td></td><td></td></tr><tr><td colspan="3">xs f[xs]</td><td></td><td></td></tr></table>

Newton's interpolatory divided-difference formula can be implemented using Algorithm 3.2. The form of the output can be modified to produce all the divided differences, as done in Example 1.

# Newton's Interpolatory Divided-Difference Formula

To obtain the divided-difference coeffcients of the interpolatory polynomial $P$ on the $( n +$ 1） distinct numbers $x _ { 0 } , x _ { 1 } , \ldots , x _ { n }$ for the function $f$ ：

INPUTnumbers $x _ { 0 } , x _ { 1 } , \ldots , x _ { n }$ ; val ${ \mathrm { u e s ~ } } f ( x _ { 0 } ) , f ( x _ { 1 } ) , \ldots , f ( x _ { n } ) { \mathrm { ~ a s ~ } } F _ { 0 , 0 } , F _ { 1 , 0 } , \ldots , F _ { n , 0 } .$ OUTPUT the numbers $F _ { 0 , 0 } , F _ { 1 , 1 } , \ldots , F _ { n , n }$ where

$$
P ( x ) = \sum _ { i = 0 } ^ { n } F _ { i , i } \prod _ { j = 0 } ^ { i - 1 } ( x - x _ { j } ) .
$$

Step 1 For $i = 1 , 2 , \dots , n$ For $j = 1 , 2 , \dots , i$ set $F _ { i , j } = \frac { F _ { i , j - 1 } - F _ { i - 1 , j - 1 } } { x _ { i } - x _ { i - j } } .$

Step 2 OUTPUT $( F _ { 0 , 0 } , F _ { 1 , 1 } , \ldots , F _ { n , n } )$ ；(F,i is f[xo,x1,..., x].)） STOP.

# EXAMPLE 1

In Example 3 of Section 3.1, various interpolating polynomials were used to approximate $f ( 1 . 5 )$ ，using the data in the first three columns of Table 3.8. The remaining entries of Table 3.8 contain divided differences computed using Algorithm 3.2.

The coefficients of the Newton forward divided-difference form of the interpolatory polynomial are along the diagonal in the table. The polynomial is

$$
\begin{array} { l } { { P _ { 4 } ( x ) = 0 . 7 6 5 1 9 7 7 - 0 . 4 8 3 7 0 5 7 ( x - 1 . 0 ) - 0 . 1 0 8 7 3 3 9 ( x - 1 . 0 ) ( x - 1 . 3 ) } } \\ { { \nonumber } } \\ { { \qquad + 0 . 0 6 5 8 7 8 4 ( x - 1 . 0 ) ( x - 1 . 3 ) ( x - 1 . 6 ) } } \\ { { \nonumber } } \\ { { \qquad + 0 . 0 0 1 8 2 5 1 ( x - 1 . 0 ) ( x - 1 . 3 ) ( x - 1 . 6 ) ( x - 1 . 9 ) . } } \end{array}
$$

Notice that the value $P _ { 4 } ( 1 . 5 ) ~ = ~ 0 . 5 1 1 8 2 0 0$ agrees with the result in Section 3.1, Example 3,as it must because the polynomials are the same.

Table 3.8   

<table><tr><td>i</td><td>X</td><td>f[xi]</td><td>f[xi-1,xi]</td><td>f[xi-2,xi-1,xi]</td><td>f[xi-3,..., xi]</td><td>f[xi-4，...,xi]</td></tr><tr><td>0</td><td>1.0</td><td>0.7651977</td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="3">1</td><td rowspan="3">1.3</td><td></td><td>-0.4837057</td><td></td><td></td><td></td></tr><tr><td>0.6200860</td><td></td><td>-0.1087339</td><td></td><td></td></tr><tr><td></td><td>-0.5489460</td><td></td><td>0.0658784</td><td></td></tr><tr><td>2</td><td>1.6</td><td>0.4554022</td><td></td><td>-0.0494433</td><td></td><td>0.0018251</td></tr><tr><td rowspan="2">3</td><td></td><td></td><td>-0.5786120</td><td></td><td>0.0680685</td><td></td></tr><tr><td>1.9</td><td>0.2818186</td><td></td><td>0.0118183</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>-0.5715210</td><td></td><td></td><td></td></tr><tr><td>4</td><td>2.2</td><td>0.1103623</td><td></td><td></td><td></td><td></td></tr></table>

The Mean Value Theorem applied to Eq.(3.8) when $i = 0$ ，

$$
f [ x _ { 0 } , x _ { 1 } ] = { \frac { f ( x _ { 1 } ) - f ( x _ { 0 } ) } { x _ { 1 } - x _ { 0 } } } ,
$$

implies that when $f ^ { \prime }$ exists, $f [ x _ { 0 } , x _ { 1 } ] = f ^ { \prime } ( \pmb { \xi } )$ for some number $\xi$ between $x _ { 0 }$ and $x _ { 1 }$ . The following theorem generalizes this result.

# Theorem 3.6

Suppose that $f \in C ^ { n } [ a , b ]$ and $x _ { 0 } , x _ { 1 } , \ldots , x _ { n }$ are distinct numbers in $[ a , b ]$ . Then a number $\xi$ exists in $( a , b )$ with

$$
f [ x _ { 0 } , x _ { 1 } , \dots , x _ { n } ] = { \frac { f ^ { ( n ) } ( \xi ) } { n ! } } .
$$

Proof Let

$$
g ( x ) = f ( x ) - P _ { n } ( x ) .
$$

Since $f ( x _ { i } ) = P _ { n } ( x _ { i } )$ , for each $i = 0 , 1 , \ldots , n$ , the function $g$ has $n + 1$ distinct zeros in $[ a , b ]$ .The Generalized Rolle's Theorem implies that a number $\xi$ in $( a , b )$ exists with $g ^ { ( n ) } ( \xi ) = 0$ ,s0

$$
0 = f ^ { ( n ) } ( \xi ) - P _ { n } ^ { ( n ) } ( \xi ) .
$$

Since $P _ { n } ( x )$ is a polynomial of degree $\pmb { n }$ whose leading coefficient is $f [ x _ { 0 } , x _ { 1 } , \ldots , x _ { n } ] ,$

$$
P _ { n } ^ { ( n ) } ( x ) = n ! f [ x _ { 0 } , x _ { 1 } , \dots , x _ { n } ] ,
$$

for all values of $\pmb { x }$ . As a consequence,

$$
f [ x _ { 0 } , x _ { 1 } , \dots , x _ { n } ] = { \frac { f ^ { ( n ) } ( \xi ) } { n ! } } .
$$

Newton's interpolatory divided-diference formula can be expressed in a simplified form when $x _ { 0 } , x _ { 1 } , \ldots , x _ { n }$ are arranged consecutively with equal spacing. In this case, we introduce the notation $h = x _ { i + 1 } - x _ { i }$ , for each $i = 0 , 1 , \ldots , n - 1$ and let $x = x _ { 0 } + s h$ Then the difference $\boldsymbol { x } - \boldsymbol { x } _ { i }$ can be written ${ \mathrm { a s ~ } } x - x _ { i } = ( s - i ) h$ .So Eq. (3.10) becomes

$$
{ \begin{array} { l } { P _ { n } ( x ) = P _ { n } ( x _ { 0 } + s h ) = f [ x _ { 0 } ] + s h f [ x _ { 0 } , x _ { 1 } ] + s ( s - 1 ) h ^ { 2 } f [ x _ { 0 } , x _ { 1 } , x _ { 2 } ] } \\ { \qquad + \cdots + s ( s - 1 ) ( s - n + 1 ) h ^ { n } f [ x _ { 0 } , x _ { 1 } , \dots , x _ { n } ] } \\ { \qquad = \displaystyle \sum _ { k = 0 } ^ { n } s ( s - 1 ) \cdot \cdot \cdot ( s - k + 1 ) h ^ { k } f [ x _ { 0 } , x _ { 1 } , \dots , x _ { k } ] . } \end{array} }
$$

Using binomial-coefficient notation,

$$
{ \binom { s } { k } } = { \frac { s ( s - 1 ) \cdots ( s - k + 1 ) } { k ! } } ,
$$

we can express $P _ { n } ( x )$ compactly as

$$
P _ { n } ( x ) = P _ { n } ( x _ { 0 } + s h ) = f [ x _ { 0 } ] + \sum _ { k = 1 } ^ { n } { \binom { s } { k } } k ! h ^ { k } f [ x _ { 0 } , x _ { i } , \dots , x _ { k } ] .
$$

This formula is called the Newton forward divided-difference formula. Another form, called the Newton forward-difference formula, is constructed by making use of the forward difference notation $\Delta$ introduced in Aitken's $\Delta ^ { 2 }$ method. With this notation,

$$
f [ x _ { 0 } , x _ { 1 } ] = { \frac { f ( x _ { 1 } ) - f ( x _ { 0 } ) } { x _ { 1 } - x _ { 0 } } } = { \frac { 1 } { h } } \Delta f ( x _ { 0 } )
$$

$$
f [ x _ { 0 } , x _ { 1 } , x _ { 2 } ] = \frac { 1 } { 2 h } \left[ \frac { \Delta f ( x _ { 1 } ) - \Delta f ( x _ { 0 } ) } { h } \right] = \frac { 1 } { 2 h ^ { 2 } } \Delta ^ { 2 } f ( x _ { 0 } ) ,
$$

and,in general,

$$
f [ x _ { 0 } , x _ { 1 } , \dots , x _ { k } ] = { \frac { 1 } { k ! h ^ { k } } } \Delta ^ { k } f ( x _ { 0 } ) .
$$

Then,Eq. (3.11) has the following formula.

# Newton Forward-Difference Formula

$$
P _ { n } ( x ) = f [ x _ { 0 } ] + \sum _ { k = 1 } ^ { n } { \binom { s } { k } } \Delta ^ { k } f ( x _ { 0 } )
$$

If the interpolating nodes are reordered as $x _ { n } , x _ { n - 1 } , \ldots , x _ { 0 }$ ,a formula similar to Eq. (3.10) results:

$$
{ \begin{array} { r l } & { P _ { n } ( x ) = f [ x _ { n } ] + f [ x _ { n } , x _ { n - 1 } ] ( x - x _ { n } ) + f [ x _ { n } , x _ { n - 1 } , x _ { n - 2 } ] ( x - x _ { n } ) ( x - x _ { n - 1 } ) } \\ & { \qquad + \cdots + f [ x _ { n } , \ldots , x _ { 0 } ] ( x - x _ { n } ) ( x - x _ { n - 1 } ) \cdot \cdot \cdot ( x - x _ { 1 } ) . } \end{array} }
$$

If the nodes are equally spaced with $x = x _ { n } + s h$ and $x = x _ { i } + ( s + n - i ) h$ ,then

$$
\begin{array} { r l } & { P _ { n } ( x ) = P _ { n } ( x _ { n } + s h ) } \\ & { \qquad = f [ x _ { n } ] + s h f [ x _ { n } , x _ { n - 1 } ] + s ( s + 1 ) h ^ { 2 } f [ x _ { n } , x _ { n - 1 } , x _ { n - 2 } ] + \cdot \cdot \cdot } \\ & { \qquad + s ( s + 1 ) \cdot \cdot \cdot ( s + n - 1 ) h ^ { n } f [ x _ { n } , \ldots , x _ { 0 } ] . } \end{array}
$$

This form is called the Newton backward divided-difference formula. It is used to derive a more commonly applied formula known as the Newton backward-difference formula. To discuss this formula, we need the following definition.

# Definition 3.7

Given the sequence $\{ p _ { n } \} _ { n = 0 } ^ { \infty }$ , define the backward diference $\nabla p _ { n }$ (read nabla $p _ { n }$ )by

$$
\nabla p _ { n } = p _ { n } - p _ { n - 1 } , \quad { \mathrm { f o r } } n \geq 1 .
$$

Higher powers are defined recursively by

$$
\nabla ^ { k } p _ { n } = \nabla ( \nabla ^ { k - 1 } p _ { n } ) , \quad { \mathrm { f o r ~ } } k \geq 2 .
$$

Definition 3.7 implies that

$$
f [ x _ { n } , x _ { n - 1 } ] = { \frac { 1 } { h } } \nabla f ( x _ { n } ) , \quad f [ x _ { n } , x _ { n - 1 } , x _ { n - 2 } ] = { \frac { 1 } { 2 h ^ { 2 } } } \nabla ^ { 2 } f ( x _ { n } ) ,
$$

and, in general,

$$
f [ x _ { n } , x _ { n - 1 } , \ldots , x _ { n - k } ] = { \frac { 1 } { k ! h ^ { k } } } \nabla ^ { k } f ( x _ { n } ) .
$$

Consequently,

$$
P _ { n } ( x ) = f [ x _ { n } ] + s \nabla f ( x _ { n } ) + { \frac { s ( s + 1 ) } { 2 } } \nabla ^ { 2 } f ( x _ { n } ) + \cdot \cdot \cdot + { \frac { s ( s + 1 ) \cdot \cdot \cdot ( s + n - 1 ) } { n ! } } \nabla ^ { n } f ( x _ { n } ) + \cdot \cdot \cdot + \cdot
$$

If we extend the binomial coeficient notation to include allreal values of $\pmb { S }$ by letting

$$
{ \binom { - s } { k } } = { \frac { - s ( - s - 1 ) \cdot \cdot \cdot ( - s - k + 1 ) } { k ! } } = ( - 1 ) ^ { k } { \frac { s ( s + 1 ) \cdot \cdot \cdot ( s + k - 1 ) } { k ! } } ,
$$

then

$$
\mathfrak { z } _ { n } ( x ) = f [ x _ { n } ] + ( - 1 ) ^ { 1 } { \binom { - s } { 1 } } \nabla f ( x _ { n } ) + ( - 1 ) ^ { 2 } { \binom { - s } { 2 } } \nabla ^ { 2 } f ( x _ { n } ) + \cdot \cdot \cdot + ( - 1 ) ^ { n } { \binom { - s } { n } } \nabla ^ { n } f ( x _ { n } ) + \cdot \cdot \cdot + ( - 1 ) ^ { n } { \binom { - s } { n } } \nabla ^ { n } f ( x _ { n } ) + \cdot \cdot \cdot + ( - 1 ) ^ { n } { \binom { - s } { n } } \nabla ^ { n } f ( x _ { n } ) + \cdot \cdot \cdot \cdot + ( - 1 ) ^ { n } { \binom { - s } { n } } \nabla ^ { n } f ( x _ { n } )
$$

which gives the following result.

# Newton Backward-Difference Formula

$$
P _ { n } ( x ) = f [ x _ { n } ] + \sum _ { k = 1 } ^ { n } ( - 1 ) ^ { k } { \binom { - s } { k } } \nabla ^ { k } f ( x _ { n } )
$$

# EXAMPlE 2

The divided-difference Table 3.9 corresponds to the data in Example 1.   
Table 3.9   

<table><tr><td></td><td></td><td>First divided differences</td><td>Second divided differences</td><td>Third divided. differences</td><td>Fourth divided differences</td></tr><tr><td>1.0</td><td>0.7651977</td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="2">1.3</td><td></td><td>-0.4837057</td><td></td><td></td><td></td></tr><tr><td>0.6200860</td><td></td><td>-0.1087339</td><td></td><td></td></tr><tr><td rowspan="2">1.6</td><td></td><td>-0.5489460</td><td></td><td>0.0658784</td><td></td></tr><tr><td>0.4554022</td><td></td><td>-0.0494433</td><td></td><td>0.0018251</td></tr><tr><td rowspan="2">1.9</td><td></td><td>-0.5786120</td><td></td><td>0.0680685</td><td></td></tr><tr><td>0.2818186</td><td>-0.5715210</td><td>0.0118183</td><td></td><td></td></tr><tr><td>2.2</td><td>0.1103623</td><td></td><td></td><td></td><td></td></tr></table>

Only one interpolating polynomial of degree at most 4 uses these five data points, but we will organize the data points to obtain the best interpolation approximations of degrees 1, 2,and 3. This will give us a sense of accuracy of the fourth-degree approximation for the given value of $x$ ·

If an approximation to $f ( 1 . 1 )$ is required, the reasonable choice for the nodes would be $x _ { 0 } = 1 . 0 , x _ { 1 } = 1 . 3 , x _ { 2 } = 1 . 6 , x _ { 3 } = 1 . 9 ,$ ,and $x _ { 4 } = 2 . 2$ since this choice makes the earliest possible use of the data points closest to $x = 1 . 1$ , and also makes use of the fourth divided difference. This implies that $h = 0 . 3$ and $\begin{array} { r } { s = \frac { 1 } { 3 } } \end{array}$ , so the Newton forward divided-difference formula is used with the divided differences that have a solid underscore in Table 3.9:

$$
\begin{array} { l } { { P _ { 4 } ( 1 . 1 ) = P _ { 4 } ( 1 . 0 + { \displaystyle { \frac { 1 } { 3 } } } ( 0 . 3 ) ) } } \\ { { \mathrm { } } } \\ { { = 0 . 7 6 5 1 9 9 7 + { \displaystyle { \frac { 1 } { 3 } } } ( 0 . 3 ) ( - 0 . 4 8 3 7 0 5 7 ) + { \displaystyle { \frac { 1 } { 3 } } } \left( - { \displaystyle { \frac { 2 } { 3 } } } \right) ( 0 . 3 ) ^ { 2 } ( - 0 . 1 0 8 7 3 3 9 ) } } \end{array}
$$

$$
\begin{array} { l } { { \displaystyle  \begin{array} { l } { { \displaystyle + \frac { 1 } { 3 } ( - \frac { 2 } { 3 } ) ( - \frac { 5 } { 3 } ) ( 0 . 3 ) ^ { 3 } ( 0 . 0 6 5 8 7 8 4 ) } } \\ { { \displaystyle \vphantom { \displaystyle ( - \frac { 1 } { 3 } ) ^ { 4 } ( - \frac { 2 } { 3 } ) ( - \frac { 5 } { 3 } ) ( - \frac { 8 } { 3 } ) ( 0 . 3 ) ^ { 4 } ( 0 . 0 0 1 8 2 5 1 ) } } } \end{array}  } } \\ { { \displaystyle  \begin{array} { r l } { { \displaystyle + \frac { 1 } { 3 } ( - \frac { 2 } { 3 } ) ( - \frac { 5 } { 3 } ) ( - \frac { 8 } { 3 } ) ( 0 . 3 ) ^ { 4 } ( 0 . 0 0 1 8 2 5 1 ) } } \end{array}  } } \\ { { \displaystyle  = 0 . 7 1 9 6 4 8 0 . } } \end{array}
$$

To approximate a value when $x$ is close to the end of the tabulated values,say, $x = 2 . 0$ ， we would again like to make the earliest use of the data points closest to $x$ . This requires using the Newton backward divided-diference formula with $s = - \textstyle { \frac { 2 } { 3 } }$ and the divided differences in Table 3.9 that have a dashed underscore:

$$
P _ { 4 } ( 2 . 0 ) = P _ { 4 } \left( 2 . 2 - { \frac { 2 } { 3 } } ( 0 . 3 ) \right)
$$

The Newton formulas are not appropriate for approximating $f ( x )$ when $x$ lies near the center of the table since employing either the backward or forward method in such a way that the highest-order difference is involved will not allow $x _ { 0 }$ to be close to $x$ . A number of divided-difference formulas are available for this case,each of which has situations when it can be used to maximum advantage. These methods are known as centered-difference formulas. There are a number of such methods, but we will present only one, Stirling's method, and again refer the interested reader to [Hild] for a more complete presentation.

For the centered-difference formulas,we choose $x _ { 0 }$ near the point being approximated and label the nodes directly below $x _ { 0 }$ as $x _ { 1 } , x _ { 2 } , \ldots$ and those directly above as $x _ { - 1 } , x _ { - 2 } , \ldots$ . With this convention, Stirling's formula is given by

$$
P _ { n } ( x ) = P _ { 2 m + 1 } ( x ) = f [ x _ { 0 } ] + \frac { s h } { 2 } ( f [ x _ { - 1 } , x _ { 0 } ] + f [ x _ { 0 } , x _ { 1 } ] ) + s ^ { 2 } h ^ { 2 } f [ x _ { - 1 } , x _ { 0 } , x _ { 1 } ]
$$

$$
\begin{array} { l } { \displaystyle + \frac { s ( s ^ { 2 } - 1 ) h ^ { 3 } } { 2 } f [ x _ { - 2 } , x _ { - 1 } , x _ { 0 } , x _ { 1 } ] + f [ x _ { - 1 } , x _ { 0 } , x _ { 1 } , x _ { 2 } ] ) } \\ { + \cdots + s ^ { 2 } ( s ^ { 2 } - 1 ) ( s ^ { 2 } - 4 ) \cdots ( s ^ { 2 } - ( m - 1 ) ^ { 2 } ) h ^ { 2 m } f [ x _ { - m } , \ldots , x _ { m } ] } \\ { + \frac { s ( s ^ { 2 } - 1 ) \cdots ( s ^ { 2 } - m ^ { 2 } ) h ^ { 2 m + 1 } } { 2 } ( f [ x _ { - m - 1 } , \ldots , x _ { m } ] + f [ x _ { - m } , \ldots , x _ { m + 1 } ] ) , } \end{array}
$$

if $n = 2 m + 1$ is odd. If $n = 2 m$ is even, we use the same formula but delete the last line The entries used for this formula are underlined in Table 3.1O on page 130.

EXAMPLE 3 Consider the table of data that was given in the previous examples.To use Stirling's formula to approximate $f ( 1 . 5 )$ with $x _ { 0 } = 1 . 6$ ,we use the underlined entries in the difference Table 3.11.

Table 3.10   

<table><tr><td>x</td><td>f(x）</td><td>First divided differences</td><td>Second divided differences</td><td>Third divided differences</td><td>Fourth divided differences</td></tr><tr><td>x-2</td><td>f[x-2]</td><td>f[x-2,x-1]</td><td></td><td></td><td></td></tr><tr><td>x-1</td><td>f[x_1]</td><td>f[x-1,xo]</td><td>f[x-2,x-1,xo]</td><td>f[x-2,x-1,x0,x]</td><td></td></tr><tr><td>x0</td><td>f[xo]</td><td>f[xo，x1]</td><td>f[x-1,xo,x1]</td><td>f[x-1,xo,x1,x2]</td><td>f[x-2,x-1,x0,x1,x2]</td></tr><tr><td>X1</td><td>f[x1]</td><td>f[x1,x2]</td><td>f[xo,x1,x2]</td><td></td><td></td></tr><tr><td>x2</td><td>f[x2]</td><td></td><td></td><td></td><td></td></tr></table>

Table 3.11   

<table><tr><td>X</td><td>f(x)</td><td>First divided differences</td><td>Second divided differences</td><td>Third divided differences</td><td>Fourth divided differences</td></tr><tr><td>1.0</td><td>0.7651977</td><td>-0.4837057</td><td></td><td></td><td></td></tr><tr><td>1.3</td><td>0.6200860</td><td>-0.5489460</td><td>-0.1087339</td><td>0.0658784</td><td></td></tr><tr><td>1.6</td><td>0.4554022</td><td>-0.5786120</td><td>-0.0494433</td><td>0.0680685</td><td>0.0018251</td></tr><tr><td>1.9</td><td>0.2818186</td><td>-0.5715210</td><td>0.0118183</td><td></td><td></td></tr><tr><td>2.2</td><td>0.1103623</td><td></td><td></td><td></td><td></td></tr></table>

The formula, with $h = 0 . 3$ ， $x _ { 0 } = 1 . 6$ ,and $\begin{array} { r } { s = - \frac { 1 } { 3 } } \end{array}$ , becomes

$$
\begin{array} { r l } & { f ( 1 . 5 ) \approx F _ { 4 } \left( 1 . 6 + \left( \frac { - 1 } { 3 } \right) ( 0 . 3 ) \right) } \\ & { \qquad = 0 . 4 5 5 4 0 2 2 + \left( - \frac { 1 } { 3 } \right) \left( \frac { 0 . 3 } { 2 } \right) ( ( - 0 . 5 4 8 9 4 6 0 ) + ( - 0 . 5 7 8 6 1 2 0 ) ) } \\ & { \qquad + \left( - \frac { 1 } { 3 } \right) ^ { 2 } ( 0 . 3 ) ^ { 2 } ( - 0 . 0 4 9 4 4 3 3 ) } \\ & { \qquad + \frac { 1 } { 2 } \left( - \frac { 1 } { 3 } \right) \left( \left( - \frac { 1 } { 3 } \right) ^ { 2 } - 1 \right) ( 0 . 3 ) ^ { 3 } ( 0 . 0 6 5 8 7 8 4 + 0 . 0 6 3 6 6 5 ) } \\ & { \qquad + \left( - \frac { 1 } { 3 } \right) ^ { 2 } \left( \left( - \frac { 1 } { 3 } \right) ^ { 2 } - 1 \right) ( 0 . 3 ) ^ { 4 } ( 0 . 0 0 1 8 2 5 1 ) } \end{array}
$$

# ExErcise SEt 3.2

1.Use Newton's interpolatory divided-difference formula or Algorithm 3.2 to construct inter-polating polynomials of degree one,two, and three for the following data. Approximate the specified value using each of the polynomials.

a. $f ( 8 . 4 )$ if $f ( 8 . 1 ) ~ = ~ 1 6 . 9 4 4 1 0 $ ， $f ( 8 . 3 ) ~ = ~ 1 7 . 5 6 4 9 2$ $f ( 8 . 6 ) ~ = ~ 1 8 . 5 0 5 1 5$ ， $f ( 8 . 7 ) =$ 18.82091  
b. $f ( 0 . 9 )$ if $f ( 0 . 6 ) ~ = ~ - 0 . 1 7 6 9 4 4 6 0$ ， $f ( 0 . 7 ) ~ = ~ 0 . 0 1 3 7 5 2 2 7$ ， $f ( 0 . 8 ) \ = \ 0 . 2 2 3 6 3 3 6 2 ,$ $f ( 1 . 0 ) = 0 . 6 5 8 0 9 1 9 7$

2.Use Newton's forward-diffrence formula to construct interpolating polynomials of degree one, two,and three for the following data. Approximate the specified value using each of the polynomials.

a. $f ( - \frac { 1 } { 3 } )$ if $\begin{array} { r l r } { f ( - 0 . 7 5 ) } & { { } = } & { - 0 . 0 7 1 8 1 2 5 0 , \ f ( - 0 . 5 ) \ = \ - 0 . 0 2 4 7 5 0 0 0 , \ f ( - 0 . 8 ) \ = \ - 0 . 0 3 4 7 5 0 0 0 , } \end{array}$ $f ( - 0 . 2 5 ) ~ =$ 0.33493750, $f ( 0 ) = 1 . 1 0 1 0 0 0 0 0$   
b. $f ( 0 . 2 5 )$ if $ \} ^ { \epsilon } ( 0 . 1 ) = - 0 . 6 2 0 4 9 9 5 8 , f ( 0 . 2 ) = - 0 . 2 8 3 9 8 6 6 8 , f ( 0 . 3 ) = 0 . 0 0 6 6 0 0 9 5 ,$ $f ( 0 . 4 ) = 0 . 2 4 8 4 2 4 4 0$

3.Use Newton's backward-diference formula to construct interpolating polynomials of degree one, two,and three for the following data. Approximate the specified value using each of the polynomials.

a. $f ( - \frac { 1 } { 3 } )$ if f(-0.75)= -0.07181250,f(-0.5)= -0.02475000, $f ( - 0 . 2 5 ) ~ =$ 0.33493750, $f ( 0 ) = 1 . 1 0 1 0 0 0 0 0$   
b. $f ( 0 . 2 5 )$ if $f ( 0 . 1 ) ~ = ~ - 0 . 6 2 0 4 9 9 5 8$ ， $f ( 0 . 2 ) ~ = ~ - 0 . 2 8 3 9 8 6 6 8$ ， $f ( 0 . 3 ) \ : = \ : 0 . 0 0 6 6 0 0 9 5 _ { ! }$ $f ( 0 . 4 ) = 0 . 2 4 8 4 2 4 4 0$

4.a.Use Algorithm 3.2 to construct the interpolating polynomial of degree four for the unequally spaced points given in the following table:

<table><tr><td>x</td><td>f(x)</td></tr><tr><td>0.0</td><td>-6.00000</td></tr><tr><td>0.1</td><td>-5.89483</td></tr><tr><td>0.3</td><td>-5.65014</td></tr><tr><td>0.6 1.0</td><td>-5.17788 -4.28172</td></tr></table>

b.Add $f ( \mathbf { l . l } ) ~ = ~ - 3 . 9 9 5 8 3$ to the table,and construct the interpolating polynomial of degree five.

5.a.Approximate $f ( 0 . 0 5 )$ using the following data and the Newton forward divideddifference formula:

$$
\frac { x } { f ( x ) \ \left. \begin{array} { l } { { 0 . 0 } } \end{array} \right. \ 0 . 2 } \ \left. \begin{array} { l } { { 0 . 4 } } \end{array} \right. \ 0 . 4 \qquad \left. \begin{array} { l } { { 0 . 6 } } \end{array} \right. \ 0 . 8 \qquad 
$$

b.Use the Newton backward divided-difference formula to approximate $f ( 0 . 6 5 )$

c. Use Stirling's formula to approximate $f ( \mathbf { 0 . 4 3 } )$

6.Show that the polynomial interpolating the following data has degree 3.

$$
\frac { x } { f ( x ) } \left. { \begin{array} { c } { { - 2 \left. \begin{array} { c } { { - 1 } } \end{array} \right. { - 1 } } } \end{array} } { 1 } \right. { \begin{array} { c } { { - 1 } } \end{array} } \left. { \begin{array} { c } { { 0 } } \end{array} } \right. { 1 } \left. { 2 } \right. { 3 }
$$

7.a.Show that the Newton forward divided-difference polynomials

$$
P ( x ) = 3 - 2 ( x + 1 ) + 0 ( x + 1 ) ( x ) + ( x + 1 ) ( x ) ( x - 1 )
$$

and

$$
Q ( x ) = - 1 + 4 ( x + 2 ) - 3 ( x + 2 ) ( x + 1 ) + ( x + 2 ) ( x + 1 ) ( x )
$$

both interpolate the data

$$
\frac { x } { f ( x ) \ \left. \begin{array} { l } { - 2 } \end{array} \right. \left. \begin{array} { l } { - 1 } \end{array} \right. \ 0 \ \left. \begin{array} { l } { \ 1 } \end{array} \right. \ 2 }
$$

b.Why does part (a) not violate the uniqueness property of interpolating polynomials?

8.A fourth-degree polynomial $P ( x )$ satisfies $\Delta ^ { 4 } P ( 0 ) = 2 4 $ ， $\Delta ^ { 3 } P ( 0 ) = 6$ ,and $\Delta ^ { 2 } P ( 0 ) = 0$ ， where $\Delta P ( x ) = P ( x + 1 ) - P ( x )$ . .Compute $\Delta ^ { 2 } P$ (10).

9.The following data are given for a polynomial $P ( x )$ of unknown degree.

$$
\frac { x } { P ( x ) } \frac { 0 } { 2 } \frac { 1 \Big | \ 2 } { - 1 \Big | \ 4 }
$$

Determine the coefficient of $x ^ { 2 }$ in $P ( x )$ if all third-order forward differences are 1.

10.The following data are given for a polynomial $P ( x )$ of unknown degree.

$$
\frac { x } { P ( x ) \ | \ 4 | \ 9 | \ 1 5 \ | \ 1 8 }
$$

Determine the coefficient of $x ^ { 3 }$ in $P ( x )$ if all fourth-order forward differences are 1.

11. The Newton forward divided-difference formula is used to approximate $\pmb { f ( 0 . 3 ) }$ given the following data.

$$
\frac { x } { f ( x ) \ \left| \begin{array} { c c } { 0 . 0 } \end{array} \right| \ 0 . 2 \ \left| \begin{array} { c c } { 0 . 4 } \end{array} \right| \ 0 . 6 }
$$

Suppose it is discovered that $f ( 0 . 4 )$ was understated by 10 and $f ( 0 . 6 )$ was overstated by 5. By what amount should the approximation to $f ( 0 . 3 )$ be changed?

12.For a function $f$ ,the Newton's interpolatory divided-diffrence formula gives the interpolating polynomial

$$
P _ { 3 } ( x ) = 1 + 4 x + 4 x ( x - 0 . 2 5 ) + { \frac { 1 6 } { 3 } } x ( x - 0 . 2 5 ) ( x - 0 . 5 ) ,
$$

on the nodes $x _ { 0 } = 0 , x _ { 1 } = 0 . 2 5 , x _ { 2 } = 0 . 5$ and $x _ { 3 } = 0 . 7 5$ . Find $f ( 0 . 7 5 )$

13.For a function $f$ , the forward divided differences are given by

<table><tr><td>x = 0.0</td><td>f[xo]</td><td>fxo,x1]</td></tr><tr><td rowspan="2">x = 0.4</td><td rowspan="2">f[x1]</td><td rowspan="2">flx0，x1,x2]=5</td></tr><tr><td>f[x1,x2]= 10</td></tr><tr><td>x = 0.7</td><td>f[x2]=6</td><td></td><td></td></tr></table>

Determine the missing entries in the table.

14.a.The introduction to this chapter included a table listing the population of the United States from 1940 to 1990. Use appropriate divided diferences to approximate the population in the years 1930,1965,and 2010. b. The population in 1930 was approximately 123,203,000. How accurate do you think your 1965 and 2010 figures are?

15. Given

$$
\begin{array} { l } { { P _ { n } ( x ) = f [ x _ { 0 } ] + f [ x _ { 0 } , x _ { 1 } ] ( x - x _ { 0 } ) + a _ { 2 } ( x - x _ { 0 } ) ( x - x _ { 1 } ) } } \\ { { \ } } \\ { { \ } } \\ { { \qquad + a _ { 3 } ( x - x _ { 0 } ) ( x - x _ { 1 } ) ( x - x _ { 2 } ) + \cdots } } \\ { { \ } } \\ { { \ } } \\ { { \qquad + a _ { n } ( x - x _ { 0 } ) ( x - x _ { 1 } ) \cdots ( x - x _ { n - 1 } ) , } } \end{array}
$$

use $P _ { n } ( x _ { 2 } )$ to show that $a _ { 2 } = f [ x _ { 0 } , x _ { 1 } , x _ { 2 } ]$

16.Show that

$$
f [ x _ { 0 } , x _ { 1 } , \dots , x _ { n } , x ] = { \frac { f ^ { ( n + 1 ) } ( \xi ( x ) ) } { ( n + 1 ) ! } } ,
$$

for some $\xi ( x )$ .[Hint: From Eq. (3.3),

$$
f ( x ) = P _ { n } ( x ) + { \frac { f ^ { ( n + 1 ) } ( \xi ( x ) ) } { ( n + 1 ) ! } } ( x - x _ { 0 } ) \cdot \cdot \cdot ( x - x _ { n } ) .
$$

Considering the interpolation polynomial of degree $n + 1$ on $x _ { 0 } , x _ { 1 } , \dotsc , x _ { n } , x$ ,we have

$$
f ( x ) = P _ { n + 1 } ( x ) = P _ { n } ( x ) + f [ x _ { 0 } , x _ { 1 } , \ldots , x _ { n } , x ] ( x - x _ { 0 } ) \cdot \cdot \cdot ( x - x _ { n } ) . \nonumber
$$

17.Let $i _ { 0 } , i _ { 1 } , \ldots , i _ { n }$ be a rearrangement of the integers $0 , 1 , \ldots , n$ . Show that $f [ x _ { i _ { 0 } } , x _ { i _ { 1 } } , \dots , x _ { i _ { n } } ]$ $= f [ x _ { 0 } , x _ { 1 } , . . . , x _ { n } ]$ . [Hint: Consider the leading coeficient of the $\pmb { n }$ th Lagrange polynomial on the data $\{ x _ { 0 } , x _ { 1 } , \ldots , x _ { n } \} = \{ x _ { i _ { 0 } } , x _ { i _ { 1 } } , \ldots , x _ { i _ { n } } \} . \}$

# 3.3 Hermite Interpolation

Osculating polynomials generalize both the Taylor polynomials and the Lagrange polynomials. Suppose that we are given $n + 1$ distinct numbers $x _ { 0 } , x _ { 1 } , \ldots , x _ { n }$ in $[ a , b ]$ -and nonnegative integers $m _ { 0 } , m _ { 1 } , \ldots , m _ { n }$ ，and $m \ : = \ : \operatorname* { m a x } \{ m _ { 0 } , m _ { 1 } , . . . , m _ { n } \}$ .The osculating polynomial approximating a function $f \in C ^ { m } [ a , b ]$ at $x _ { i }$ , for each $i = 0 , \ldots , n$ ,is the polynomial of least degree with the property that it agrees with the function $f$ and all its derivatives of order less than or equal to $m _ { i }$ at $x _ { i }$ . The degree of this osculating polynomial is at most

$$
M = \sum _ { i = 0 } ^ { n } m _ { i } + n
$$

because the number of conditions to be satisfid is $\textstyle \sum _ { i = 0 } ^ { n } m _ { i } + ( n + 1 )$ , and a polynomial of degree $M$ has $M + 1$ coefficients that can be used to satisfy these conditions.

# Definition 3.8

Let $x _ { 0 } , x _ { 1 } , \ldots , x _ { n }$ be $n + 1$ distinct numbers in $[ a , b ]$ and $\dot { m } _ { i }$ be a nonnegative integer associated with $x _ { i }$ ,for $i = 0$ ,1,..., $\pmb { n }$ . Suppose that $f \in { \dot { C } } ^ { m } [ a , b ]$ ,where $m = \mathfrak { m a x } _ { 0 \leq i \leq n } m _ { i }$ The osculating polynomial approximating $f$ is the polynomial $P ( x )$ of least degree such that

$$
{ \frac { d ^ { k } P ( x _ { i } ) } { d x ^ { k } } } = { \frac { d ^ { k } f ( x _ { i } ) } { d x ^ { k } } } , \quad { \mathrm { f o r ~ e a c h ~ } } i = 0 , 1 , \dots , n ^ { \prime } \quad { \mathrm { a n d } } \quad k = 0 , 1 , \dots , m _ { i } .
$$

Note that when $n = 0$ ,the osculating polynomial.approximating $f$ is the $m _ { 0 }$ th Taylor polynomial for $f$ at $x _ { 0 }$ . When $m _ { i } ~ = ~ 0$ for each $i$ , the osculating polynomial is the nth Lagrange polynomial interpolating $f$ on $x _ { 0 } , x _ { 1 } , \ldots , x _ { n }$

The case when $m _ { i } = 1$ ,for each $i = 0$ ， $1 , \ldots , n$ , gives the Hermite polynomials. For a given function $f$ , these polynomials agree with $f$ at $x _ { 0 } , x _ { 1 } , \ldots , x _ { n }$ . In addition,since their first derivatives agree with those of $f$ , they: have the same “shape” as the function at $( x _ { i } , f ( x _ { i } ) )$ in the sense that the tangent lines'to.the polynomial and to the function agree. We will restrict our study of osculating polynomials to this situation and consider first a theorem that describes precisely the form of the Hermite polynomials.

If $f \in C ^ { 1 } [ a , b ]$ and $x _ { 0 } , \ldots , x _ { n } \in [ a , b ]$ are distinct, the unique polynomial of least degree agreeing with $f$ and $f ^ { \prime }$ at $x _ { 0 } , \ldots , x _ { n }$ is the Hermite polynomial of degree at most $2 n + 1$ given by

$$
H _ { 2 n + 1 } ( x ) = \sum _ { j = 0 } ^ { n } f ( x _ { j } ) H _ { n , j } ( x ) + \sum _ { j = 0 } ^ { n } f ^ { \prime } ( x _ { j } ) { \hat { H } } _ { n , j } ( x ) ,
$$

where

$$
H _ { n , j } ( x ) = [ 1 - 2 ( x - x _ { j } ) L _ { n , j } ^ { \prime } ( x _ { j } ) ] L _ { n , j } ^ { 2 } ( x )
$$

and

$$
\hat { H } _ { n , j } ( x ) = ( x - x _ { j } ) L _ { n , j } ^ { 2 } ( x ) .
$$

In this context, $L _ { n , j } \left( x \right)$ denotes the $j$ th Lagrange coeficient polynomial of degree $_ n$ defined in Eq (3.2).

Moreover, if $f \in C ^ { 2 n + 2 } [ a , b ]$ ,then

$$
f ( x ) = H _ { 2 n + 1 } ( x ) + \frac { ( x - x _ { 0 } ) ^ { 2 } \ldots ( x - x _ { n } ) ^ { 2 } } { ( 2 n + 2 ) ! } f ^ { ( 2 n + 2 ) } ( \xi ) ,
$$

for some $\xi$ with $a < \xi < b$

Proof First recall that

$$
L _ { n , j } ( x _ { i } ) = { \left\{ \begin{array} { l l } { 0 , } & { { \mathrm { i f ~ } } i \neq j , } \\ { 1 , } & { { \mathrm { i f ~ } } i = j . } \end{array} \right. }
$$

Hence, when $i \neq j$ ，

$$
H _ { n , j } ( x _ { i } ) = 0 \quad \mathrm { a n d } \quad \hat { H } _ { n , j } ( x _ { i } ) = 0 ,
$$

whereas

$$
H _ { n , i } ( x _ { i } ) = \{ 1 - 2 ( x _ { i } - x _ { i } ) L _ { n , i } ^ { \prime } ( x _ { i } ) ] \cdot 1 = 1
$$

and

$$
{ \hat { H } } _ { n , i } ( x _ { i } ) = ( x _ { i } - x _ { i } ) \cdot 1 ^ { 2 } = 0 .
$$

As a consequence,

$$
H _ { 2 n + 1 } ( x _ { i } ) = \sum _ { \stackrel { j = 0 } { j \neq i } } ^ { n } f ( x _ { j } ) \cdot 0 + f ( x _ { i } ) \cdot 1 + . \underset { j = 0 } { \overset { n } { \sum } } f ^ { \prime } ( x _ { j } ) \cdot 0 = f ( x _ { i } ) ,
$$

s0 $H _ { 2 n + 1 }$ agrees with $f$ at $x _ { 0 } , x _ { 1 } , \ldots , x _ { n }$

To show the agreement of $H _ { 2 n + 1 } ^ { \prime }$ with $f ^ { \prime }$ at the nodes,first note that $L _ { n , j } ( x )$ is a factor of $H _ { n , j } ^ { \prime } ( x )$ ，s0 $H _ { n , j } ^ { \prime } ( x _ { i } ) = 0$ when $i \neq j$ . In addition, when $i = j$ and $L _ { n , i } ( x _ { i } ) = 1$ ,we have

$$
\begin{array} { r l } & { H _ { n , i } ^ { \prime } ( x _ { i } ) = - 2 L _ { n , i } ^ { \prime } ( x _ { i } ) \cdot L _ { n , i } ^ { 2 } ( x _ { i } ) + [ 1 - 2 ( x _ { i } - x _ { i } ) L _ { n , i } ^ { \prime } ( x _ { i } ) ] 2 L _ { n , i } ( x _ { i } ) L _ { n , i } ^ { \prime } ( x _ { i } ) } \\ & { \qquad = - 2 L _ { n , i } ^ { \prime } ( x _ { i } ) + 2 L _ { n , i } ^ { \prime } ( x _ { i } ) = 0 . } \end{array}
$$

Hence, $H _ { n , j } ^ { \prime } ( x _ { i } ) = 0$ for all $i$ and $j$

Finally,

$$
\begin{array} { r l } & { \hat { H } _ { n , j } ^ { \prime } ( x _ { i } ) = L _ { n , j } ^ { 2 } ( x _ { i } ) + ( x _ { i } - x _ { j } ) 2 L _ { n , j } ( x _ { i } ) L _ { n , j } ^ { \prime } ( x _ { i } ) } \\ & { \qquad = L _ { n , j } ( x _ { i } ) [ L _ { n , j } ( x _ { i } ) + 2 ( x _ { i } - x _ { j } ) L _ { n , j } ^ { \prime } ( x _ { i } ) ] , } \end{array}
$$

s0 $\hat { H } _ { n , j } ^ { \prime } ( x _ { i } ) = 0$ if $i \neq j$ and $\hat { H } _ { n , i } ^ { \prime } ( x _ { i } ) = 1$ . Combining these facts, we have

$$
H _ { 2 n + 1 } ^ { \prime } ( x _ { i } ) = \sum _ { j = 0 } ^ { n } f ( x _ { j } ) \cdot 0 + \sum _ { j = 0 \atop j \ne i } ^ { n } f ^ { \prime } ( x _ { j } ) \cdot 0 + f ^ { \prime } ( x _ { i } ) \cdot 1 = f ^ { \prime } ( x _ { i } ) .
$$

"herefore, $H _ { 2 n + 1 }$ agrees with $f$ and $H _ { 2 n + 1 } ^ { \prime }$ with $f ^ { \prime }$ at $x _ { 0 } , x _ { 1 } , \ldots , x _ { n }$

The uniqueness of this polynomial and the error formula are considered in Exercise 8.

Use the Hermite polynomial that agres with the data listed in Table 3.12 to find an approximation of $f ( 1 . 5 )$

# Table 3.12

<table><tr><td>k</td><td>Xk f(xx)</td><td>f&#x27;(xk)</td></tr><tr><td>0 1.3</td><td>0.6200860</td><td>-0.5220232</td></tr><tr><td>1</td><td>1.6 0.4554022</td><td>-0.5698959</td></tr><tr><td>2</td><td>1.9 0.2818186</td><td>-0.5811571</td></tr></table>

We first compute the Lagrange polynomials and their derivatives. This gives

$$
\begin{array} { l l l } { { \tiny \begin{array} { c } { { \displaystyle \mathrm { ~ } _ { \cdot 2 , 0 } ( x ) = \displaystyle \frac { ( x - x _ { 1 } ) ( x - x _ { 2 } ) } { ( x _ { 0 } - x _ { 1 } ) ( x _ { 0 } - x _ { 2 } ) } = \displaystyle \frac { 5 0 } { 9 } x ^ { 2 } - \frac { 1 7 5 } { 9 } x + \frac { 1 5 2 } { 9 } , } } \end{array} } } & { { \begin{array} { c } { { \displaystyle L _ { 2 , 0 } ^ { \prime } ( x ) = \displaystyle \frac { 1 0 0 } { 9 } x - \frac { 1 } { 9 } } } \end{array} } } \\ { { \tiny \begin{array} { c } { { \displaystyle \mathrm { ~ } _ { \cdot 2 , 1 } ( x ) = \displaystyle \frac { ( x - x _ { 0 } ) ( x - x _ { 2 } ) } { ( x _ { 1 } - x _ { 0 } ) ( x _ { 1 } - x _ { 2 } ) } = \displaystyle \frac { - 1 0 0 } { 9 } x ^ { 2 } + \frac { 3 2 0 } { 9 } x - \frac { 2 4 7 } { 9 } , } } \end{array} } } & { { \begin{array} { c } { { \displaystyle L _ { 2 , 1 } ^ { \prime } ( x ) = \displaystyle \frac { - 2 0 0 } { 9 } x + \frac { 1 } { 9 } } } \end{array} } } \end{array}
$$

and

$$
\therefore _ { 2 , 2 } = { \frac { ( x - x _ { 0 } ) ( x - x _ { 1 } ) } { ( x _ { 2 } - x _ { 0 } ) ( x _ { 2 } - x _ { 1 } ) } } = { \frac { 5 0 } { 9 } } x ^ { 2 } - { \frac { 1 4 5 } { 9 } } x + { \frac { 1 0 4 } { 9 } } , \qquad L _ { 2 , 2 } ^ { \prime } ( x ) = { \frac { 1 0 0 } { 9 } } x - { \frac { 1 4 5 } { 9 } } .
$$

The polynomials $H _ { 2 , j } ( x )$ and $\hat { H } _ { 2 , j } ( x )$ are then

$$
\begin{array} { r l } & { H _ { 2 , 0 , 1 } ( x ) = [ 1 - 2 ( \iota - 1 . 3 ) \iota ) ( \frac { 5 \mathrm { i } \mathrm { i } } { 9 } x ^ { 2 } - \frac { 1 7 5 } { 9 } x + \frac { 1 5 2 } { 9 } ] } \\ & { \phantom { h s p a c e } = ( \mathrm { I } \mathfrak { g } - 1 2 ) ( \frac { 5 0 } { 9 } x ^ { 2 } - \frac { 1 7 5 } { 9 } x + \frac { 1 5 2 } { 9 } ) ^ { 2 } , } \\ & { \phantom { h s p a c e } H _ { 2 , \vert \lambda \vert } ( x ) = \mathrm { I } \cdot ( \frac { - 1 0 0 } { 9 } x ^ { 2 } + \frac { 3 2 0 } { 9 } x - \frac { 2 4 7 } { 9 } ) ^ { 2 } , } \\ & { \phantom { h s p a c e } H _ { 2 , 2 , ( x ) = } \mathrm { I I R } _ { 2 } ( x ) = \mathrm { I I R } _ { 2 } ( x ) - \frac { 1 6 0 } { 9 } x ^ { 2 } - \frac { 1 4 5 } { 9 } x + \frac { 1 0 4 } { 9 } ) ^ { 2 } , } \\ & { \phantom { h s p a c e } H _ { 2 , 0 , ( x ) = } ( x - 1 . 3 ) ( \frac { 5 0 } { 9 } x ^ { 2 } - \frac { 1 7 5 } { 9 } x + \frac { 1 5 2 } { 9 } ) ^ { 2 } , } \\ & { \phantom { h s p a c e } H _ { 2 , 1 } ( x ) = ( x - 1 . 6 ) ( \frac { - 1 0 0 } { 9 } x ^ { 2 } + \frac { 3 2 0 } { 9 } x - \frac { 2 4 7 } { 9 } ) ^ { 2 } . } \end{array}
$$

and

$$
\hat { H } _ { 2 , 2 } ( x ) = ( x - 1 . 9 ) \left( \frac { 5 0 } { 9 } x ^ { 2 } - \frac { 1 4 5 } { 9 } x + \frac { 1 0 4 } { 9 } \right) ^ { 2 } .
$$

Finally,

$$
\begin{array} { r l } & { H _ { 5 } ( x ) = 0 . 6 2 0 0 8 6 0 H _ { 2 , 0 } ( x ) + 0 . 4 5 5 4 0 2 2 H _ { 2 , 1 } ( x ) + 0 . 2 8 1 8 1 8 6 H _ { 2 , 2 } ( x ) } \\ & { \qquad - 0 . 5 2 2 0 2 3 2 \hat { H } _ { 2 , 0 } ( x ) - 0 . 5 6 9 8 9 5 9 \hat { H } _ { 2 , 1 } ( x ) - 0 . 5 8 1 1 5 7 1 \hat { H } _ { 2 , 2 } ( x ) } \end{array}
$$

and

$$
H _ { 5 } ( 1 . 5 ) = 0 . 6 2 0 0 8 6 0 \left( { \frac { 4 } { 2 7 } } \right) + 0 . 4 5 5 4 0 2 2 \left( { \frac { 6 4 } { 8 1 } } \right) + 0 . 2 8 1 8 1 8 6 \left( { \frac { 5 } { 8 1 } } \right)
$$

$$
- 0 . 5 2 2 0 2 3 2 \left( \frac { 4 } { 4 0 5 } \right) - 0 . 5 6 9 8 9 5 9 \left( \frac { - 3 2 } { 4 0 5 } \right) - 0 . 5 8 1 1 5 7 1 \left( \frac { - 2 } { 4 0 5 } \right)
$$

a result that is accurate to the places listed.

Although Theorem 3.9 provides a complete description of the Hermite polynomials, it is clear from Example 1 that the need to determine and evaluate the Lagrange polynomials and their derivatives makes the procedure tedious even for small values of $n$ . An alternative method for generating Hermite approximations has as its basis the Newton interpolatory divided-difference formula (3.10) for the Lagrange polynomial at $x _ { 0 } , x _ { 1 } , \ldots , x _ { n }$ ，

$$
P _ { n } ( x ) = f [ x _ { 0 } ] + \sum _ { k = 1 } ^ { n } f [ x _ { 0 } , x _ { 1 } , \ldots , x _ { k } ] ( x - x _ { 0 } ) \cdot \cdot \cdot ( x - x _ { k - 1 } ) ,
$$

and the connection between the $\pmb { n }$ th divided difference and the $n$ th derivative of $f$ ，as outlined in Theorem 3.6 in Section 3.2.

Suppose that the distinct numbers $x _ { 0 } , x _ { 1 } , \ldots , x _ { n }$ are given together with the values of $f$ and $f ^ { \prime }$ at these numbers. Define a new sequence $z _ { 0 } , z _ { 1 } , \dots , z _ { 2 n + 1 }$ by

$$
z _ { 2 i } = z _ { 2 i + 1 } = x _ { i } , \quad { \mathrm { f o r ~ e a c h } } i = 0 , 1 , \dots , n ,
$$

and construct the divided diference table in the form of Table 3.7thatuses Zo, $z _ { 2 n + 1 }$ ·

Since $z _ { 2 i } \ = \ z _ { 2 i + 1 } \ = \ x _ { i }$ for each $i$ ，we cannot define $f [ z _ { 2 i } , z _ { 2 i + 1 } ]$ by the divided difference formula.If we assume,based on Theorem 3.6, that the reasonable substitution in this situation is $f [ z _ { 2 i } , z _ { 2 i + 1 } ] = f ^ { \prime } ( \dot { z } _ { 2 i } ) = f ^ { \prime } ( x _ { i } )$ , we can use the entries

$$
f ^ { \prime } ( x _ { 0 } ) , f ^ { \prime } ( x _ { 1 } ) , \ldots , f ^ { \prime } ( x _ { n } )
$$

in place of the undefined first divided differences

$$
f [ z _ { 0 } , z _ { 1 } ] , f [ z _ { 2 } , z _ { 3 } ] , \dots , f [ z _ { 2 n } , z _ { 2 n + 1 } ] .
$$

The remaining divided differences are produced as usual, and the appropriate divided differences are employed in Newton's interpolatory divided-difference formula. Table 3.13 shows the entries that are used for the first three divided-difference columns when determining the Hermite polynomial $H _ { 5 } ( x )$ for $x _ { 0 } , \ x _ { 1 }$ ,and $x _ { 2 }$ . The remaining entries are generated in the same manner as in Table 3.7. The Hermite polynomial is given by

$$
H _ { 2 n + 1 } ( x ) = f [ z _ { 0 } ] + \sum _ { k = 1 } ^ { 2 n + 1 } f [ z _ { 0 } , \ldots , z _ { k } ] ( x - z _ { 0 } ) ( x - z _ { 1 } ) \cdot \cdot \cdot ( x - z _ { k - 1 } ) .
$$

A proof of this fact can be found in $[ \mathrm { P o } , \mathfrak { p } . 5 6 ]$

Table 3.13   

<table><tr><td>7</td><td>f(2)</td><td>First divided differences</td><td colspan="2">Second divided differences</td></tr><tr><td>Z0 = x0</td><td>f[zo]= f(xo）</td><td>f[zo,z1]= f(xo）</td><td></td><td>f[zt, z2]- f[zo,21]</td></tr><tr><td>Z1= x0</td><td>flz1= f(xo）</td><td>f[22]-f[z1] f[z1,22] =</td><td>f[z0,21, 22] =</td><td>Z2-Z0</td></tr><tr><td>Z2 = X1</td><td>f[z2]= f(x1）</td><td>Z2 - z1</td><td>f[z1,22,23]=</td><td>f[22,z3]- f[21, 22]</td></tr><tr><td></td><td></td><td>f[z2,z3]= f&#x27;(x1)</td><td></td><td>Z3-Z1</td></tr><tr><td>Z3 =x1</td><td>f[z3]=f(x1）</td><td></td><td>f[22,23,24] =</td><td>f[z3,24]-f[2,23] 24- 22</td></tr><tr><td></td><td></td><td>f[z4]-f[z3] f[z3,24] = Z4-Z3</td><td></td><td></td></tr><tr><td>Z4 = X2</td><td>f[z4]= f(x2)</td><td></td><td>f[23,Z4,25] =</td><td>f[z4,25]- f[z3,24]</td></tr><tr><td></td><td></td><td></td><td></td><td>25-23</td></tr><tr><td></td><td></td><td>f[z4,zs]= f&#x27;(x2）</td><td></td><td></td></tr><tr><td>Zs = X2</td><td>f[zs]=f（x2）</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr></table>

# EXAMPLE 2

The entries in Table 3.14 use the data given in Example 1. The underlined entries are the given data;the remainder are generated by the standard divided-diference formula (3.9):

$$
H _ { 5 } ( 1 . 5 ) = 0 . 6 2 0 0 8 6 0 + ( 1 . 5 - 1 . 3 ) ( - 0 . 5 2 2 0 2 3 2 ) + ( 1 . 5 - 1 . 3 ) ^ { 2 } ( - 0 . 0 8 9 7 4 2 7 )
$$

$$
+ ( 1 . 5 - 1 . 3 ) ^ { 2 } ( 1 . 5 - 1 . 6 ) ( 0 . 0 6 6 3 6 5 7 ) + ( 1 . 5 - 1 . 3 ) ^ { 2 } ( 1 . 5 - 1 . 6 ) ^ { 2 } ( 0 . 0 0 2 6 6 6 3 )
$$

Table 3.14   

<table><tr><td>1.3</td><td>0.6200860</td><td></td><td></td><td></td><td></td></tr><tr><td>1.3</td><td>0.6200860</td><td>-0.5220232</td><td>-0.0897427</td><td></td><td></td></tr><tr><td></td><td></td><td>-0.5489460</td><td></td><td>0.0663657</td><td></td></tr><tr><td>1.6</td><td>0.4554022</td><td></td><td>-0.0698330</td><td></td><td>0.0026663</td></tr><tr><td></td><td></td><td>-0.5698959</td><td></td><td>0.0679655</td><td></td></tr><tr><td></td><td>0.4554022</td><td></td><td>-0.0290537</td><td></td><td></td></tr><tr><td>1.6</td><td></td><td>-0.5786120</td><td></td><td></td><td>0.0010020</td></tr><tr><td>1.9</td><td>0.2818186</td><td></td><td></td><td>0.0685667</td><td></td></tr><tr><td></td><td></td><td></td><td>-0.0084837</td><td></td><td></td></tr><tr><td>1.9</td><td>0.2818186</td><td>-0.5811571</td><td></td><td></td><td></td></tr></table>

The technique used in Algorithm 3.3 can be extended for use in determining other Osculating polynomials.A concise discussion of the procedures can be found in $\{ \mathbf { P o } ,$ pp. 53-57].

# Hermite Interpolation

To obtain the coeficients of the Hermite interpolating polynomial $H ( x )$ on the $( n + 1 )$ distinct numbers $x _ { 0 } , \ldots , x _ { n }$ for the function $f$ ：

INPUTnumbers $x _ { 0 } , x _ { 1 } , \ldots , x _ { n }$ ; values $f ( x _ { 0 } ) , \ldots , f ( x _ { n } )$ and $f ^ { \prime } ( x _ { 0 } ) , \ldots , f ^ { \prime } ( x _ { n } )$

OUTPUT the numbers $Q _ { 0 , 0 } , Q _ { 1 , 1 } , \dots , Q _ { 2 n + 1 , 2 n + 1 }$ where

$$
\begin{array} { l } { { H ( x ) = \mathcal { Q } _ { 0 , 0 } + Q _ { 1 , 1 } ( x - x _ { 0 } ) + Q _ { 2 , 2 } ( x - x _ { 0 } ) ^ { 2 } + Q _ { 3 , 3 } ( x - x _ { 0 } ) ^ { 2 } ( x - x _ { 1 } ) } } \\ { { \ ~ + Q _ { 4 , 4 } ( x - x _ { 0 } ) ^ { 2 } ( x - x _ { 1 } ) ^ { 2 } + \cdot \cdot \cdot } } \\ { { \ ~ + Q _ { 2 n + 1 , 2 n + 1 } ( x - x _ { 0 } ) ^ { 2 } ( x - x _ { 1 } ) ^ { 2 } \cdot \cdot \cdot ( x - x _ { n - 1 } ) ^ { 2 } ( x - x _ { n } ) . } } \end{array}
$$

Step 1 For $i = 0 , 1 , \ldots , n$ do Steps 2 and 3.

Step 2 Set $z _ { 2 j } = x _ { i }$ ；$\begin{array} { r l } & { z _ { 2 i + 1 } = x _ { i } ; } \\ & { Q _ { 2 i , 0 } = f ( x _ { i } ) ; } \\ & { Q _ { 2 i + 1 , 0 } = f ( x _ { i } ) ; } \\ & { Q _ { 2 i + 1 , 1 } = f ^ { \prime } ( x _ { i } ) . } \end{array}$

Step 3If $i \neq 0$ then set

$$
Q _ { 2 i , 1 } = \frac { Q _ { 2 i , 0 } - Q _ { 2 i - 1 , 0 } } { z _ { 2 i } - z _ { 2 i - 1 } } .
$$

![](images/605489421f56fb7ea421d86cf110f8fce35b90d0b1c57da734f14d6adc309976.jpg)

Step $^ { \prime 4 } \mathrm { F o r } i = 2 , 3 , \ldots , 2 n + 1$ $\mathrm { f o r } \ j = 2 , 3 , \ldots , i \ \mathrm { s e t } \ Q _ { i , j } = { \frac { Q _ { i , j - 1 } - Q _ { i - 1 , j - 1 } } { z _ { i } - z _ { i - j } } } .$

Step 5OUTPUT $( Q _ { 0 , 0 } , Q _ { 1 , 1 } , \dots , Q _ { 2 n + 1 , 2 n + 1 } )$ ； STOP

# ExERCIsE SEt 3.3

1.Use Theorem 3.9or Algorithm 3.3 toconstruct an approximating polynomial forthe following data.

<table><tr><td rowspan="3">a.</td><td>X</td><td>f(x)</td><td>f&#x27;(x)</td></tr><tr><td>8.3</td><td>17.56492</td><td>3.116256</td></tr><tr><td>8.6</td><td>18.50515</td><td>3.151762</td></tr></table>

<table><tr><td>b.</td><td>X</td><td>f(x）</td><td>f&#x27;(x)</td></tr><tr><td>0.8 1.0</td><td></td><td>0.22363362 0.65809197</td><td>2.1691753 2.0466965</td></tr></table>

<table><tr><td>c.</td><td>X</td><td>f(x)</td><td>f&#x27;(x)</td></tr><tr><td rowspan="3">-0.5 -0.25 0</td><td rowspan="3"></td><td>-0.0247500</td><td>0.7510000</td></tr><tr><td>0.3349375</td><td>2.1890000</td></tr><tr><td>1.1010000</td><td>4.0020000</td></tr></table>

<table><tr><td>d.</td><td>X</td><td>f(x）</td><td>f&#x27;(x)</td></tr><tr><td></td><td>0.1</td><td>-0.62049958</td><td>3.58502082</td></tr><tr><td></td><td>0.2</td><td>-0.28398668</td><td>3.14033271</td></tr><tr><td></td><td>0.3</td><td>0.00660095</td><td>2.66668043</td></tr><tr><td></td><td>0.4</td><td>0.24842440</td><td>2.16529366</td></tr></table>

2.The data in Exercise 1 were generated using the following functions. Use the polynomials constructed in Exercise 1 for the given value of $x$ to approximate $f ( x )$ ， and calculate the actual error.

a. $f ( x ) = x \ln x$ ；approximate $f ( 8 . 4 )$ . $\mathbf { b } .$ $f ( x ) = \sin ( e ^ { x } - 2 )$ ；approximate $f ( 0 . 9 )$ c. $f ( x ) = x ^ { 3 } + 4 . 0 0 1 x ^ { 2 } + 4 . 0 0 2 x + 1 . 1 0 1$ ；approximate $f ( - \frac { 1 } { 3 } )$ d. $f ( x ) = x \cos x - 2 x ^ { 2 } + 3 x - 1$ ；approximate $f ( 0 . 2 5 )$

3.a.Use the following values and five-digit rounding arithmetic to construct the Hermite interpolating polynomial to approximate sin 0.34.

<table><tr><td>X</td><td>sin x</td><td>Dx sin x = cos x</td></tr><tr><td>0.30</td><td>0.29552</td><td>0.95534</td></tr><tr><td>0.32</td><td>0.31457</td><td>0.94924</td></tr><tr><td>0.35</td><td>0.34290</td><td>0.93937</td></tr></table>

b.Determine an eror bound for the approximation in part (a),and compare it to the actual error. c. Add sin $0 . 3 3 = 0 . 3 2 4 0 4$ and cos $0 . 3 3 = 0 . 9 4 6 0 4$ to the data,andredo thecalculations.

4.Let $f ( x ) = 3 x e ^ { x } - e ^ { 2 x }$

a. Approximate $f ( 1 . 0 3 )$ by the Hermite interpolating polynomial of degree at most three using ${ \pmb x } _ { 0 } = { \pmb 1 }$ and $x _ { 1 } = 1 . 0 5$ . Compare the actual error to the error bound.   
$\mathbf { b } _ { \bullet }$ Repeat (a) with the Hermite interpolating polynomial of degree at most five, using $x _ { 0 } = 1$ ， $x _ { 1 } = 1 . 0 5$ , and $x _ { 2 } = 1 . 0 7$

5. Usethe error formula and Maple to find a bound for the errors in the approximations of $f ( x )$ in parts (a) and (c) of Exercise 2.

6.The following table lists data for the function described by $f ( x ) \ = \ e ^ { 0 . 1 x ^ { 2 } }$ . Approximate $f ( 1 . 2 5 )$ by using $H _ { 5 } ( 1 . 2 5 )$ and $H _ { 3 } ( 1 . 2 5 )$ ， where $H _ { 5 }$ uses the nodes $x _ { 0 } = 1$ ， $x _ { 1 } = 2$ ,and $x _ { 2 } = 3$ ; and $H _ { 3 }$ uses the nodes $\bar { x } _ { 0 } = 1$ and $\bar { x } _ { 1 } = 1 . 5$ Find error bounds for these approximations.

$$
\begin{array}{c} { \begin{array} { l } { x } \\ { { \overline { { x _ { 0 } = { \overline { { x } } } _ { 0 } = 1 } } } } \\ { { \bar { x } } _ { 1 } = 1 . 5 } \\ { x _ { 1 } = 2 } \\ { x _ { 2 } = 3 } \end{array} } { \overset { } { \mid } } { \overbrace { f ( x ) = e ^ { 0 . 1 x ^ { 2 } } \ \downarrow { \begin{array} { l } { f ^ { \prime } ( x ) = 0 . 2 x e ^ { 0 . 1 x ^ { 2 } } } \\ { 1 . 1 0 5 1 7 0 9 1 8 } \\ { 1 . 2 5 2 3 2 2 7 1 6 } \\ { 1 . 4 9 1 8 2 4 6 9 8 } \\ { 2 . 4 5 9 6 0 3 1 1 1 } \end{array} } } } { \overbrace { 0 . 2 2 1 0 3 4 1 8 3 6 } ^ { 0 . 2 2 1 8 2 } }  \end{array} 
$$

7.A car traveling along a straight road is clocked at a number of points. The data from the observations are given in the following table,where the time is in seconds,the distance is in feet, and the speed is in feet per second.

<table><tr><td rowspan=1 colspan=1>Time</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>13</td></tr><tr><td rowspan=1 colspan=1>Distance</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>225</td><td rowspan=1 colspan=1>383</td><td rowspan=1 colspan=1>623</td><td rowspan=1 colspan=1>993</td></tr><tr><td rowspan=1 colspan=1>Speed</td><td rowspan=1 colspan=1>—75</td><td rowspan=1 colspan=1>77</td><td rowspan=1 colspan=1>80</td><td rowspan=1 colspan=1>74</td><td rowspan=1 colspan=1>72</td></tr></table>

a.Use a Hermite polynomial to predict the position of the car and its speed when $t = 1 0 s$

${ \bf b } .$ Use the derivative of the Hermite polynomial to determine whether the car ever exceeds a $5 5 \mathrm { m i } / \hbar$ speed limit on the road. If so, what is the first time the car exceeds this speed?

c. What is the predicted maximum speed for the car?

8.a. Show that $H _ { 2 n + 1 } ( x )$ is the unique polynomial of least degree agreeing with $f$ and $f ^ { \prime }$ at $x _ { 0 } , \ldots , x _ { n }$ . [Hint: Assume that $P ( x )$ is another such polynomial and consider $D =$ $H _ { 2 n + 1 } - P$ and $\pmb { D } ^ { \prime }$ at $x _ { 0 } , x _ { 1 } , \ldots , x _ { n } .$

b. Derive the error term in Theorem 3.9.[Hint: Use the same method as in the Lagrange error derivation, Theorem 3.3,defining

$$
g ( t ) = f ( t ) - H _ { 2 n + 1 } ( t ) - { \frac { ( t - x _ { 0 } ) ^ { 2 } \cdot \cdot \cdot ( t - x _ { n } ) ^ { 2 } } { ( x - x _ { 0 } ) ^ { 2 } \cdot \cdot \cdot ( x - x _ { n } ) ^ { 2 } } } [ f ( x ) - H _ { 2 n + 1 } ( x ) ]
$$

and using the fact that $g ^ { \prime } ( t )$ has $( 2 n + 2 )$ distinct zeros in $\{ a , b \} . ]$

9.Let $z _ { 0 } = x _ { 0 } , z _ { 1 } = x _ { 0 } , z _ { 2 } = x _ { 1 }$ ,and $z _ { 3 } = x _ { 1 }$ . Form the following divided-difference tabl

$$
\begin{array}{c} \begin{array}{c} \begin{array} { l l l } { z _ { 0 } = x _ { 0 } } & { f [ z _ { 0 } ] = f ( x _ { 0 } ) } \\ { z _ { 1 } = x _ { 0 } } & { f [ z _ { 1 } ] = f ( x _ { 0 } ) } & { f [ z _ { 0 } , z _ { 1 } ] = f ^ { \prime } ( x _ { 0 } ) } \\ & & { f [ z _ { 1 } , z _ { 2 } ] } \\ { z _ { 2 } = x _ { 1 } } & { f [ z _ { 2 } ] = f ( x _ { 1 } ) } & { f [ z _ { 2 } , z _ { 3 } ] = f ^ { \prime } ( x _ { 1 } ) } \\ & & { f [ z _ { 3 } , z _ { 1 } ] = f ( x _ { 1 } ) } \end{array} \begin{array} { l l } { f [ z _ { 0 } , z _ { 1 } , z _ { 2 } ] } \\ & { f [ z _ { 0 } , z _ { 1 } , z _ { 2 } ] } \\ & { f [ z _ { 1 } , z _ { 2 } , z _ { 3 } ] } \end{array}  \end{array} f [ z _ { 0 } , z _ { 1 } , z _ { 2 } ]  \\ { z _ { 3 } = x _ { 1 } \quad f [ z _ { 3 } ] = f ( x _ { 1 } ) } \end{array}
$$

Show that the cubic Hermite polynomial $H _ { 3 } ( x )$ can also be written as $f [ z _ { 0 } ] + f [ z _ { 0 } , z _ { 1 } ] ( x -$ $x _ { 0 } ) + f [ z _ { 0 } , z _ { 1 } , z _ { 2 } ] ( x - x _ { 0 } ) ^ { 2 } + f [ z _ { 0 } , z _ { 1 } , z _ { 2 } , z _ { 3 } ] ( x - x _ { 0 } ) ^ { 2 } ( x - x _ { 1 } ) .$

# 3.4 Cubic Spline Interpolation\*

The previous sections concermed the approximation of arbitrary functions on closed intervals by the use of polynomials.However, the oscillatory nature of high-degree polynomials and the property that a fluctuation over a small portion of the interval can induce large fluctuations over the entire range restricts their use. We will see a good example of this in Figure 3.12 at the end of this section.

An alternative approach is to divide the interval into a collection of subintervals and construct a (generally) different approximating polynomial on each subinterval. Approximation by functions of this type is called piecewise-polynomial approximation.

The simplest piecewise-polynomial approximation is piecewise-linear interpolation, which consists of joining a set of data points

$$
\{ ( x _ { 0 } , f ( x _ { 0 } ) ) , ( x _ { 1 } , f ( x _ { 1 } ) ) , \ldots , ( x _ { n } , f ( x _ { n } ) ) \}
$$

by a series of straight lines, as shown in Figure 3.7 on page 142.

A disadvantage of linear function approximation is that there is likely no diferentiability at the endpoints of the subintervals,which,in a geometrical context, means that the interpolating function is not “smooth.” Often it is clear from physical conditions that smoothness is required, so the approximating function must be continuously differentiable.

An alternative procedure is to use a piecewise polynomial of Hermite type. For exam-ple, if the values of $f$ and of $f ^ { \prime }$ are known at each of the points $x _ { 0 } < x _ { 1 } < \cdots < x _ { n }$ ,a cubic Hermite polynomial can be used on each of the subintervals $[ x _ { 0 } , x _ { 1 } ] , [ x _ { 1 } , x _ { 2 } ] , \dots ,$ $[ x _ { n - 1 } , x _ { n } ]$ to obtain a function that has a continuous derivative on the interval $[ x _ { 0 } , x _ { n } ]$ .To \*The proofs of the theorems in this section rely on results in Chapter 6.

![](images/03e849c5616c8bed041c372c1528b35e10c980b05017ee4885a011d152ecee90.jpg)  
Figure 3.7

determine the appropriate Hermite cubic polynomial on a given interval is simply a mater of computing $H _ { 3 } ( x )$ for that interval. Since the Lagrange interpolating polynomials needed to determine $H _ { 3 }$ are of first degree, this can be accomplished without great difficulty. How-ever, to use Hermite piecewise polynomials for general interpolation, we need to know the derivative of.the function being approximated, which is frequently unavailable.

The remainder of this section considers approximation using piecewise polynomials that require no derivative information, except perhaps at the endpoints of the interval on which the function is being approximated.

The simplest type of differentiable piecewise-polynomial function on an entire interval $[ x _ { 0 } , x _ { n } ]$ is the function obtained by fitting one quadratic polynomial between each succes-sive pair of nodes. This is done by constructing one quadratic on $[ x _ { 0 } , x _ { 1 } ]$ agreeing with the function at $x _ { 0 }$ and $x _ { 1 }$ , another quadratic on $[ x _ { 1 } , x _ { 2 } ]$ agreeing with the function at $x _ { 1 }$ and $x _ { 2 }$ ,and so on. Since a general quadratic polynomial has three arbitrary constants-the constant term, the coefficient of $x$ ,and the coefficient of $x ^ { 2 }$ --and only two conditions are required to fit the data at the endpoints of each subinterval, flexibility exists that permits the quadratic to be chosen so that the interpolant has a continuous derivative on $[ x _ { 0 } , x _ { n } ]$ The difficulty arises when there is a need to specify conditions about the derivative of the interpolant at the endpoints $x _ { 0 }$ and $x _ { n }$ . There is not a sufficient number of constants to ensure that the conditions will be satisfied. (See Exercise 22.)

The most common piecewise-polynomial approximation uses cubic polynomials be-tween each successive pair of nodes and is called cubic spline interpolation. A general cubic polynomial involves four constants,so there is sufcient flexibility in the cubic spline procedure to ensure that the interpolant is not only continuously differentiable on the interval, but also has a continuous second derivative. The construction of the cubic spline does not, however,assume that the derivatives of the interpolant agree with those of the function it is approximating,even at the nodes. (See Figure 3.8.)

![](images/031231c53ee83f88e25a76f59962e51742a19e08de3e5fee9ab06cd85c5b35a0.jpg)  
Figure 3.8

# Definition 3.10

Given a function f defined on [a,b] and a set of nodes a = xo < x1 < .. < xn = b,a cubic spline interpolant $S$ for $f$ is a function that satisfies the following conditions:

a. $S ( x )$ is a cubic polynomial, denoted $S _ { j } ( x )$ , on the subinterval $[ x _ { j } , x _ { j + 1 } ]$ for each $j = 0 , 1 , \ldots , n - 1$ ；   
b. $S ( x _ { j } ) = f ( x _ { j } )$ for each $j = 0 , 1 , \dotsc , n _ { \scriptscriptstyle \mathscr { n } }$   
c. $S _ { j + 1 } ( x _ { j + 1 } ) = S _ { j } ( x _ { j + 1 } )$ for each $j = 0 , 1 , \ldots , n - 2 ;$   
d. $S _ { j + 1 } ^ { \prime } ( x _ { j + 1 } ) = S _ { j } ^ { \prime } ( x _ { j + 1 } )$ for each $j = 0 , 1 , \ldots , n - 2$   
e. $S _ { j + 1 } ^ { \prime \prime } ( x _ { j + 1 } ) = S _ { j } ^ { \prime \prime } ( x _ { j + 1 } )$ for each $j = 0 , 1 , \ldots , n - 2$   
f. One of the following sets of boundary conditions is satisfied: i $S ^ { \prime \prime } ( x _ { 0 } ) = S ^ { \prime \prime } ( x _ { n } ) = 0$ (free or natural boundary); (ii) $S ^ { \prime } ( x _ { 0 } ) = f ^ { \prime } ( x _ { 0 } )$ and $S ^ { \prime } ( x _ { n } ) = f ^ { \prime } ( x _ { n } )$ (clamped boundary).

Although cubic splines are defined with other boundary conditions,the conditions given in (f) are suficient for our purposes. When the free boundary conditions occur, the spline is caled a natural spline,and its graph approximates the shape that a long flexible rod would assume if forced to go through the data points {(xo,f(xo)),(x1, f(xi))..., $( x _ { n } , f ( x _ { n } ) ) \}$

In general, clamped boundary conditions lead to more accurate approximations since they include more information about the function. However, for this type of boundary condition to hold, it is necessary to have either the values of the derivative at the endpoints or an accurate approximation to those values.

To construct the cubic spline interpolant for a given function $f$ , the conditions in the definition are applied to the cubic polynomials

$$
S _ { j } ( x ) = a _ { j } + b _ { j } ( x - x _ { j } ) + c _ { j } ( x - x _ { j } ) ^ { 2 } + d _ { j } ( x - x _ { j } ) ^ { 3 } ,
$$

for each $j = 0 , 1 , \ldots , n - 1$

Since

$$
S _ { j } ( x _ { j } ) = a _ { j } = f ( x _ { j } ) ,
$$

condition (c) can be applied to obtain

$$
\iota _ { j + 1 } = S _ { j + 1 } ( x _ { j + 1 } ) = S _ { j } ( x _ { j + 1 } ) = a _ { j } + b _ { j } ( x _ { j + 1 } - x _ { j } ) + c _ { j } ( x _ { j + 1 } - x _ { j } ) ^ { 2 } + d _ { j } ( x _ { j + 1 } - x _ { j } ) + d _ { j + 1 } .
$$

for each $j = 0 , 1 , \ldots , n - 2$

Since the terms $x _ { j + 1 } - x _ { j }$ are used repeatedly in this development, it is convenient to introduce the simpler notation

$$
h _ { j } = x _ { j + 1 } - x _ { j } ,
$$

for each $j = 0 , 1 , \ldots , n - 1$ . If we also define $a _ { n } = f ( x _ { n } )$ , then the equation

$$
a _ { j + 1 } = a _ { j } + b _ { j } h _ { j } + c _ { j } h _ { j } ^ { 2 } + d _ { j } h _ { j } ^ { 3 }
$$

holds for each $j = 0 , 1 , \ldots , n - 1$

In a similar manner, define $b _ { n } = S ^ { \prime } ( x _ { n } )$ and observe that

$$
S _ { j } ^ { \prime } ( x ) = b _ { j } + 2 c _ { j } ( x - x _ { j } ) + 3 d _ { j } ( x - x _ { j } ) ^ { 2 }
$$

implies $S _ { j } ^ { \prime } ( x _ { j } ) = b _ { j }$ ,for each $j = 0 , 1 , \ldots , n - 1$ .Applying condition (d) gives

$$
b _ { j + 1 } = b _ { j } + 2 c _ { j } h _ { j } + 3 d _ { j } h _ { j } ^ { 2 } ,
$$

for each $j = 0 , 1 , \ldots , n - 1$

Another relationship between the coefficients of $S _ { j }$ is obtained by defining $c _ { n } =$ $S ^ { \prime \prime } ( x _ { n } ) / 2$ and applying condition (e). Then, for each $j = 0 , 1 , \ldots , n - 1$ ，

$$
c _ { j + 1 } = c _ { j } + 3 d _ { j } h _ { j } .
$$

Solving for $d _ { j }$ in Eq. (3.17) and substituting this value into Eqs.(3.15)and (3.16) gives, for each $j = 0 , 1 , \ldots , n - 1$ , the new equations

$$
a _ { j + 1 } = a _ { j } + b _ { j } h _ { j } + \frac { h _ { j } ^ { 2 } } { 3 } ( 2 c _ { j } + c _ { j + 1 } )
$$

and

$$
b _ { j + 1 } = b _ { j } + h _ { j } ( c _ { j } + c _ { j + 1 } ) .
$$

Th final relationshipinvolvingthecofcients isotainedbysolving theappoate equation in the form of equation (3.18),frst for $b _ { j }$ ，

$$
b _ { j } = \frac { 1 } { h _ { j } } ( a _ { j + 1 } - a _ { j } ) - \frac { h _ { j } } { 3 } ( 2 c _ { j } + c _ { j + 1 } ) ,
$$

and then, with a reduction of the index, for $b _ { j - 1 }$ . This gives

$$
b _ { j - 1 } = \frac { 1 } { h _ { j - 1 } } ( a _ { j } - a _ { j - 1 } ) - \frac { h _ { j - 1 } } { 3 } ( 2 c _ { j - 1 } + c _ { j } ) .
$$

Substituting these values into the equation derived from Eq. (3.19), with the index reduced by one, gives the linear system of equations

$$
h _ { j - 1 } c _ { j - 1 } + 2 ( h _ { j - 1 } + h _ { j } ) c _ { j } + h _ { j } c _ { j + 1 } = \frac { 3 } { h _ { j } } ( a _ { j + 1 } - a _ { j } ) - \frac { 3 } { h _ { j - 1 } } ( a _ { j } - a _ { j - 1 } ) ,
$$

for each $j = 1 , 2 , \dots , n - 1$ . This system involves only the $\{ c _ { j } \} _ { j = 0 } ^ { n }$ as unknowns since the values of $\{ h _ { j } \} _ { j = 0 } ^ { n - 1 } \mathrm { a n d } \{ a _ { j } \} _ { j = 0 } ^ { n }$ are given,respectively,bythespacing of teodes $\{ x _ { j } \} _ { j = 0 } ^ { n }$ and the values of $f$ at the nodes.

Note that once the values of $\{ c _ { j } \} _ { j = 0 } ^ { n }$ are determined, it is a simple matter to find the remainder of the constants $\{ b _ { j } \} _ { j = 0 } ^ { n - 1 }$ from Eq. (3.20) and $\{ d _ { j } \} _ { j = 0 } ^ { n - 1 }$ from Eq. (3.17), and to construct the cubic polynomials $\stackrel { \cdot } { \{ S _ { j } ( x ) \} } _ { j = 0 } ^ { n - 1 }$

The major question that arises in connection with this construction is whether the values of $\{ c _ { j } \} _ { j = 0 } ^ { n }$ can be found using the system of equations given in (3.21) and, if so, whether these values are unique. The following theorems indicate that this is the case when either of the boundary conditions given in part (f) of the definition are imposed. The proofs of these theorems require material from linear algebra, which is discussed in Chapter 6.

# Theorem 3.11

$f$ is defined at $a = x _ { 0 } < x _ { 1 } < \cdots < x _ { n } = b$ ，then $f$ has a unique natural spline interpolant $s$ on the nodes $x _ { 0 } , x _ { 1 } , \ldots , x _ { n }$ ; that is,a spline interpolant that satisfies the boundary conditions $S ^ { \prime \prime } ( a ) = 0$ and $S ^ { \prime \prime } ( b ) = 0$

Proof The boundary conditions in this case imply that $c _ { n } = S ^ { \prime \prime } ( x _ { n } ) / 2 = 0$ and that

$$
0 = S ^ { \prime \prime } ( x _ { 0 } ) = 2 c _ { 0 } + 6 d _ { 0 } ( x _ { 0 } - x _ { 0 } ) ,
$$

so $c _ { 0 } = 0$

The two equations $c _ { 0 } = 0$ and $c _ { n } = 0$ together with the equations in (3.21) produce a linear system described by the vector equation $\pmb { A } \mathbf { x } = \mathbf { b }$ ,where $A$ is the $( n + 1 ) \times ( n + 1 )$ matrix

$$
A = \left[ \begin{array} { c c c c c c c c } { 1 } & { 0 } & { 0 } & { \ldots } & { \ldots } & { \ldots } & { \ldots } & { \ldots } & { \ldots } & { 0 } \\ { h _ { 0 } } & { 2 ( h _ { 0 } + h _ { 1 } ) } & { h _ { 1 } } & { \ddots } & { \ldots } & { \vdots } \\ { 0 } & { \ldots } & { h _ { 1 } } & { \ldots } & { h _ { 2 } } & { \ldots } & { \vdots } \\ { \vdots } & { \ddots } & { \ddots } & { \ddots } & { \ddots } & { \ddots } & { \ddots } & { \ddots } \\ { \vdots } & { \ddots } & { \ddots } & { \ddots } & { \ddots } & { \ddots } & { \ddots } & { \ddots } \\ { \vdots } & { \ddots } & { \ddots } & { \ddots } & { \ddots } & { \ddots } & { \ddots } & { \ddots } \\ { \vdots } & { \ddots } & { \ddots } & { \ddots } & { h _ { n - 2 } } & { 2 ( h _ { n - 2 } ^ { - } + h _ { n - 1 } ) ^ { \setminus } h _ { n - 1 } } \\ { \vdots } & { \ddots } & { \ddots } & { \ldots } & { \ldots } & { \ldots } & { \ddots } & { 0 } \end{array} \right] ,
$$

and $\mathbf { b }$ and $\mathbf { x }$ are the vectors

$$
\mathbf { b } = \left[ \begin{array} { c } { 0 } \\ { \frac { 3 } { h _ { 1 } } ( a _ { 2 } - a _ { 1 } ) - \frac { 3 } { h _ { 0 } } ( a _ { 1 } - a _ { 0 } ) } \\ { \vdots } \\ { \frac { 3 } { h _ { n - 1 } } ( a _ { n } - a _ { n - 1 } ) - \frac { 3 } { h _ { n - 2 } } ( a _ { n - 1 } - a _ { n - 2 } ) } \\ { 0 } \end{array} \right] \quad \mathrm { a n d } \quad \mathbf { x } = \left[ \begin{array} { c } { c _ { 0 } } \\ { c _ { 1 } } \\ { \vdots } \\ { c _ { n } } \\ { c _ { n } } \end{array} \right]
$$

The matrix $A$ is strictly diagonally dominant, so it satisfies the hypotheses of Theorem 6.19 in Section 6.6. Therefore, the linear system has a unique solution for $c _ { 0 } , c _ { 1 } , \ldots , c _ { n }$

The solution tothe cubic spline problem with the boundary conditions $S ^ { \prime \prime } ( x _ { 0 } ) \ =$ $S ^ { \prime \prime } ( x _ { n } ) = 0$ can be obtained by applying Algorithm 3.4.

# Natural Cubic Spline

To construct the cubic spline interpolant $s$ for the function $f$ ， defined at the numbers $x _ { 0 } < x _ { 1 } < \cdots < x _ { n }$ , satisfying $S ^ { \prime \prime } ( x _ { 0 } ) = S ^ { \prime \prime } ( x _ { n } ) = 0$

$$
n ; x _ { 0 } , x _ { 1 } , \ldots , x _ { n } ; a _ { 0 } = f ( x _ { 0 } ) , a _ { 1 } = f ( x _ { 1 } ) , \ldots , a _ { n } = f ( x _ { n } ) .
$$

OUTPUT $a _ { j } , b _ { j } , c _ { j } , d _ { j }$ for $j = 0 , 1 , \ldots , n - 1$ (Note: $S ( x ) \stackrel { \cdot } { = } \tilde { S _ { j } ( x ) } = \stackrel { \cdot } { a } _ { j } + b _ { j } ( x - x _ { j } ) + c _ { j } ( x - x _ { j } ) ^ { 2 } + d _ { j } ( x - x _ { j } ) ^ { 3 } f o r x _ { j } \leq x \leq x _ { j + 1 } . )$

Step 1 Fori=0,1,..,n-1 sethi = xi+1 - xi.

Step 2 $\operatorname { F o r } i = 1 , 2 , \dots , n - 1$ set

$$
\alpha _ { i } = \frac { 3 } { h _ { i } } ( a _ { i + 1 } - a _ { i } ) - \frac { 3 } { h _ { i - 1 } } ( a _ { i } - a _ { i - 1 } ) .
$$

Step 3 Set ${ { l } _ { 0 } } = 1$ ; (Steps 3,4,5, and part of Step 6 solve a tridiagonal linear system using $\pmb { a }$ method described in Algorithm 6.7.)

$$
\begin{array} { l } { { \mu _ { 0 } = 0 ; } } \\ { { z _ { 0 } = 0 . } } \end{array}
$$

Step 4 For $i = 1 , 2 , \ldots , n - 1$ set $\begin{array} { r l } & { \cdot l _ { i } = 2 ( x _ { i + 1 } - x _ { i - 1 } ) - h _ { i - 1 } \mu _ { i - 1 } ; } \\ & { \mu _ { i } = h _ { i } / l _ { i } ; } \\ & { z _ { i } = ( \alpha _ { i } - h _ { i - 1 } z _ { i - 1 } ) / l _ { i } . } \end{array}$

Step 5 Set ${ l } _ { n } = 1$ ；$\begin{array} { c } { { \dot { z } _ { n } = 0 ; } } \\ { { c _ { n } = 0 . } } \end{array}$

Step 6For $j = n - 1 , n - 2 , \dots , 0$

$$
\begin{array} { r l } & { \cdot \llcorner \llcorner - \rrangle \llcorner \rrangle , } \\ & { \theta _ { j } = ( a _ { j + 1 } - a _ { j } ) / h _ { j } - h _ { j } ( c _ { j + 1 } + 2 c _ { j } ) / 3 ; } \\ & { d _ { j } = ( c _ { j + 1 } - c _ { j } ) / ( 3 h _ { j } ) . } \end{array}
$$

A result similar to Theorem 3.11 holds in the case of clamped boundary conditions.

# Theorem 3.12

If $f$ is defined at $a = x _ { 0 } < x _ { 1 } < \cdots < x _ { n } = b$ and differentiable at $^ { a }$ and $b$ ,then $f$ has a unique clamped spline interpolant $S$ on the nodes $x _ { 0 } , x _ { 1 } , \ldots , x _ { n }$ ； that is, a spline interpolant that satisfies the boundary conditions $S ^ { \prime } ( a ) = f ^ { \prime } ( a )$ and $\mathbf { \nabla } \cdot S ^ { \prime } ( b ) = f ^ { \prime } ( b )$

Proof Since $f ^ { \prime } ( a ) = S ^ { \prime } ( a ) = S ^ { \prime } ( x _ { 0 } ) = b _ { 0 }$ ,Eq. (3.20) with $j = 0$ implies

$$
f ^ { \prime } ( a ) = \frac { 1 } { h _ { 0 } } ( a _ { 1 } - a _ { 0 } ) - \frac { h _ { 0 } } { 3 } ( 2 c _ { 0 } + c _ { 1 } ) .
$$

Consequently,

$$
2 h _ { 0 } c _ { 0 } + h _ { 0 } c _ { 1 } = \frac { 3 } { h _ { 0 } } ( a _ { 1 } - a _ { 0 } ) - 3 f ^ { \prime } ( a ) .
$$

Similarly,

$$
f ^ { \prime } ( b ) = b _ { n } = b _ { n - 1 } + h _ { n - 1 } ( c _ { n - 1 } + c _ { n } ) ,
$$

so Eq. (3.20) with $j = n - 1$ implies that

$$
\begin{array} { l } { f ^ { \prime } ( b ) = \displaystyle \frac { a _ { n } - a _ { n - 1 } } { h _ { n - 1 } } - \frac { h _ { n - 1 } } { 3 } ( 2 c _ { n - 1 } + c _ { n } ) + h _ { n - 1 } ( c _ { n - 1 } + c _ { n } ) \medskip } \\ { = \displaystyle \frac { a _ { n } - a _ { n - 1 } } { h _ { n - 1 } } + \frac { h _ { n - 1 } } { 3 } ( c _ { n - 1 } + 2 c _ { n } ) , } \end{array}
$$

and

$$
h _ { n - 1 } c _ { n - 1 } + 2 h _ { n - 1 } c _ { n } = 3 f ^ { \prime } ( b ) - \frac { 3 } { h _ { n - 1 } } ( a _ { n } - a _ { n - 1 } ) .
$$

Equations (3.21) together with the equations

$$
2 h _ { 0 } c _ { 0 } + h _ { 0 } c _ { 1 } = \frac { 3 } { h _ { 0 } } ( a _ { 1 } - a _ { 0 } ) - 3 f ^ { \prime } ( a )
$$

and

$$
h _ { n - 1 } c _ { n - 1 } + 2 h _ { n - 1 } c _ { n } = 3 f ^ { \prime } ( b ) - \frac { 3 } { h _ { n - 1 } } ( a _ { n } - a _ { n - 1 } )
$$

determine the linear system $\pmb { A } \mathbf { x } = \mathbf { b }$ , where

$$
\begin{array} { r l } &  \begin{array} { r l } & { [ 2 \hbar \boldsymbol { \hat { \mathbf { u } } } , \quad \hat { \mathbf { p } } _ { 1 }  } \\   \hbar \boldsymbol { \hat { \mathbf { u } } } , \quad  \frac { \hbar \hat { \mathbf { u } } } { 2 } , \quad  \frac { \hbar \boldsymbol { \hat { \mathbf { u } } } , \boldsymbol { \hat { \mathbf { v } } } , \boldsymbol { \hat { \mathbf { u } } } , \boldsymbol { \hat { \mathbf { v } } } , \boldsymbol { \hat { \mathbf { u } } } , \boldsymbol { \hat { \mathbf { v } } } , \boldsymbol { \hat { \mathbf { u } } } , \boldsymbol { \hat { \mathbf { v } } } , \boldsymbol { \hat { \mathbf { u } } } , \boldsymbol { \hat { \mathbf { u } } } , \boldsymbol { \hat { \mathbf { v } } } , \boldsymbol { \hat { \mathbf { u } } } , \boldsymbol { \hat { \mathbf { u } } } , \boldsymbol { \hat { \mathbf { v } } } , \boldsymbol { \hat { \mathbf { u } } } , \boldsymbol { \hat { \mathbf { u } } } , \boldsymbol { \hat { \mathbf { v } } }  } \\ {  \hbar \boldsymbol { \hat { \mathbf { u } } } , \quad 2 ( \hbar \boldsymbol { \hat { \mathbf { u } } } + \hbar \boldsymbol { \mathbf { l } } ) , \quad \hat { \mathbf { h } } _ { 1 }  } \\ {  \boldsymbol { \hat { \mathbf { u } } } , \quad - \hbar \boldsymbol { \hat { \mathbf { u } } } , \boldsymbol { \hat { \mathbf { v } } } , \boldsymbol { \hat { \mathbf { u } } } , \boldsymbol { \hat { \mathbf { v } } } , \boldsymbol { \hat { \mathbf { u } } } , \boldsymbol { \hat { \mathbf { v } } } , \boldsymbol { \hat { \mathbf { u } } } , \boldsymbol { \hat { \mathbf { v } } } , \boldsymbol { \hat { \mathbf { u } } } , \boldsymbol { \hat { \mathbf { v } } } , \boldsymbol { \hat { \mathbf { u } } } , \boldsymbol { \hat { \mathbf { u } } } , \boldsymbol { \hat { \mathbf { v } } } , \boldsymbol { \hat { \mathbf { u } } } , \boldsymbol { \hat { \mathbf { u } } } , \boldsymbol { \hat { \mathbf { u } } } , \boldsymbol { \hat { \mathbf { u } } } , \boldsymbol { \hat { \mathbf { u } } } , \boldsymbol { \hat { \mathbf { u } } } , \boldsymbol { \hat { \mathbf { u } } } ] } \\   \frac  \hbar \boldsymbol { \hat { \mathbf { v } } } \cdot \boldsymbol { \mathbf { u } } , \quad \boldsymbol { \hat { \mathbf { v } } } , \boldsymbol  \hat  \mathbf \end{array} \end{array}
$$

The matrix $A$ is strictly diagonally dominant, so it satisfies the conditions of Theorem 6.19. Therefore, the linear system has a unique solution for $c _ { 0 } , c _ { 1 } , \ldots , c _ { n }$

The solution to the cubic spline problem with the boundary conditions $S ^ { \prime } ( x _ { 0 } ) = f ^ { \prime } ( x _ { 0 } )$ and $S ^ { \prime } ( x _ { n } ) = f ^ { \prime } ( x _ { n } )$ can be obtained by applying Algorithm 3.5.

# Clamped Cubic Spline

To construct the cubic spline interpolant $s$ for the function $f$ defined at the numbers $x _ { 0 } <$ $x _ { 1 } < \cdots < x _ { n }$ ,satisfying $S ^ { \prime } ( x _ { 0 } ) = f ^ { \prime } ( x _ { 0 } )$ and $S ^ { \prime } ( x _ { n } ) = f ^ { \prime } ( x _ { n } )$

INPUT $n ; x _ { 0 } , x _ { 1 } , \ldots , x _ { n } ; a _ { 0 } = f ( x _ { 0 } ) , a _ { 1 } = f ( x _ { 1 } ) , \ldots , a _ { n } = f ( x _ { n } ) ; F P O = f ^ { \prime } ( x _ { 0 } ) ;$ $F P N = f ^ { \prime } ( x _ { n } )$ ，

OUTPUT $a _ { j } , b _ { j } , c _ { j } , d _ { j }$ for $j = 0 , 1 , \ldots , n - 1$ (Note $: S ( x ) \stackrel { \cdot } { = } S _ { j } ^ { \cdot } ( x ) \stackrel { \cdot } { = } a _ { j } + b _ { j } ( x - x _ { j } ) + c _ { j } ( x - x _ { j } ) ^ { 2 } + d _ { j } ( x - x _ { j } ) ^ { 3 } f o r x _ { j } \leq x \leq x _ { j + 1 } . \rangle$

Step 1 For $\cdot i = 0 , 1 , \ldots , n - 1$ set $h _ { i } = x _ { i + 1 } - x _ { i }$

Step 2 Set $\alpha _ { 0 } = 3 ( a _ { 1 } - a _ { 0 } ) / h _ { 0 } - 3 F P O ;$ $\alpha _ { n } = 3 F P N - 3 ( a _ { n } - a _ { n - 1 } ) / h _ { n - 1 } .$

Step 3 $\operatorname { F o r } i = 1 , 2 , \dots , n - 1$

$$
\sec \alpha _ { i } = { \frac { 3 } { h _ { i } } } ( a _ { i + 1 } - a _ { i } ) - { \frac { 3 } { h _ { i - 1 } } } ( a _ { i } - a _ { i - 1 } ) .
$$

Step 4 Set $l _ { 0 } = 2 h _ { 0 }$ ;(Steps 4,5,6,and partof Step 7solve atridiagonal linear sstem using $a$ method described in Algorithm 6.7.)

$$
\begin{array} { l } { { \mu _ { 0 } = 0 . 5 ; } } \\ { { z _ { 0 } = \alpha _ { 0 } / l _ { 0 } . } } \end{array}
$$

Step 5For $i = 1 , 2 , \dots , n - 1$ set $\begin{array} { r c l } { \cdot l _ { i } = 2 ( x _ { i + 1 } - x _ { i - 1 } ) - h _ { i - 1 } \mu _ { i - 1 } ; } \\ { \mu _ { i } = h _ { i } / l _ { i } ; } \\ { z _ { i } = ( \alpha _ { i } - h _ { i - 1 } z _ { i - 1 } ) / l _ { i } . } \end{array}$

![](images/2d6789c299428991a5e41cc1c8158548734b4e271f7dd7696b60e582458afeec.jpg)

Step 6 Set $\begin{array} { r c l } { { } } & { { } } & { { : l _ { n } = h _ { n - 1 } ( 2 - \mu _ { n - 1 } ) ; } } \\ { { } } & { { } } & { { z _ { n } = ( \alpha _ { n } - h _ { n - 1 } z _ { n - 1 } ) / l _ { n } ; } } \\ { { } } & { { } } & { { c _ { n } = z _ { n } . } } \end{array}$

Step 7 For $j = n - 1 , n - 2 , \dots , 0$

$$
\begin{array} { r l } & { \mathrm { \Lambda } ^ { [ } c _ { j } = z _ { j } - \mu _ { j } c _ { j + 1 } \mathrm { ; } } \\ & { \mathrm { \Lambda } b _ { j } = ( a _ { j + 1 } - a _ { j } ) / h _ { j } - h _ { j } ( c _ { j + 1 } + 2 c _ { j } ) / 3 \mathrm { ; } } \\ & { \mathrm { \Lambda } d _ { j } = ( c _ { j + 1 } - c _ { j } ) / ( 3 h _ { j } ) . } \end{array}
$$

Step 8OUTPUT $( a _ { j } , b _ { j } , c _ { j } , d _ { j }$ for $j = 0 , 1 , \ldots , n - 1 )$ ：STOP.

# EXAMPLE 1

Figure 3.9 shows a ruddy duck in flight.To approximate the top profile of the duck, we have chosen points along the curve through which we want the approximating curve to pass. Table 3.15 lists the coordinates of 21 data points relative to the superimposed coordinate system shown in Figure 3.10 on page 150. Notice that more points are used when the curve is changing rapidly than when it is changing more slowly.

![](images/3005b2893c4445134ca7a59f158361c41c9c4597eab1f441d34a0f65c668ff63.jpg)  
Figure 3.9

Table 3.15   

<table><tr><td rowspan=2 colspan=1>X</td><td rowspan=2 colspan=1>0.9</td><td rowspan=2 colspan=1>1.3</td><td rowspan=2 colspan=1>1.9</td><td rowspan=2 colspan=1>2.12</td><td rowspan=2 colspan=1>2.6</td><td rowspan=2 colspan=1>3.0</td><td rowspan=2 colspan=1>3.9</td><td rowspan=2 colspan=1>4.4</td><td rowspan=2 colspan=1>4.7</td><td rowspan=2 colspan=1>5.0</td><td rowspan=2 colspan=1>6.0</td><td rowspan=2 colspan=1>7.0</td><td rowspan=2 colspan=1>8.0</td><td rowspan=2 colspan=1>9.2</td><td rowspan=2 colspan=1>10.5</td><td rowspan=2 colspan=1>11.3</td><td rowspan=2 colspan=1>11.6</td><td></td><td></td><td></td><td></td></tr><tr><td rowspan=1 colspan=1>12.0</td><td rowspan=1 colspan=1>12.6</td><td rowspan=1 colspan=1>13.0</td><td rowspan=1 colspan=1>13.3</td></tr><tr><td rowspan=1 colspan=1>f(x）</td><td rowspan=1 colspan=1>1.3</td><td rowspan=1 colspan=1>1.5</td><td rowspan=1 colspan=1>1.85</td><td rowspan=1 colspan=1>2.1</td><td rowspan=1 colspan=1>2.6</td><td rowspan=1 colspan=1>2.7</td><td rowspan=1 colspan=1>2.4</td><td rowspan=1 colspan=1>2.15</td><td rowspan=1 colspan=1>2.05</td><td rowspan=1 colspan=1>2.1</td><td rowspan=1 colspan=1>2.25</td><td rowspan=1 colspan=1>2.3</td><td rowspan=1 colspan=1>2.25</td><td rowspan=1 colspan=1>1.95</td><td rowspan=1 colspan=1>1.4</td><td rowspan=1 colspan=1>0.9</td><td rowspan=1 colspan=1>0.7</td><td rowspan=1 colspan=1>0.6</td><td rowspan=1 colspan=1>0.5</td><td rowspan=1 colspan=1>0.4</td><td rowspan=1 colspan=1>0.25</td></tr></table>

Using Algorithm 3.4 to generate the free cubic spline for this data produces the coefficients shown in Table 3.16.This spline curve is nearly identical to the profile,as shown in Figure 3.11.

![](images/6f9922aad62c65d0feda997de8cc24c53e8471516595486d3ce575e90f10de9b.jpg)  
Figure 3.10

Table 3.16   

<table><tr><td>j</td><td>xj</td><td>aj</td><td>bj</td><td>Cj</td><td>dj</td></tr><tr><td>0</td><td>0.9</td><td>1.3</td><td>5.40</td><td>0.00</td><td>-0.25</td></tr><tr><td>1</td><td>1.3</td><td>1.5</td><td>0.42</td><td>-0.30</td><td>0.95</td></tr><tr><td>2</td><td>1.9</td><td>1.85</td><td>1.09</td><td>1.41</td><td>-2.96</td></tr><tr><td>3</td><td>2.1</td><td>2.1</td><td>1.29</td><td>-0.37</td><td>-0.45</td></tr><tr><td>4</td><td>2.6</td><td>2.6</td><td>0.59</td><td>--1.04</td><td>0.45</td></tr><tr><td>5</td><td>3.0</td><td>2.7</td><td>-0.02</td><td>-0.50</td><td>0.17</td></tr><tr><td>6</td><td>3.9</td><td>2.4</td><td>-0.50</td><td>-0.03</td><td>0.08</td></tr><tr><td>7</td><td>4.4</td><td>2.15</td><td>-0.48</td><td>0.08</td><td>1.31</td></tr><tr><td>8</td><td>4.7</td><td>2.05</td><td>-0.07</td><td>1.27</td><td>-1.58</td></tr><tr><td>9</td><td>5.0</td><td>2.1</td><td>0.26</td><td>-0.16</td><td>0.04</td></tr><tr><td>10</td><td>6.0</td><td>2.25</td><td>0.08</td><td>-0.03</td><td>0.00</td></tr><tr><td>11</td><td>7.0</td><td>2.3</td><td>0.01</td><td>-0.04</td><td>-0.02</td></tr><tr><td>12</td><td>8.0</td><td>2.25</td><td>-0.14</td><td>-0.11</td><td>0.02</td></tr><tr><td>13</td><td>9.2</td><td>1.95</td><td>-0.34</td><td>-0.05</td><td>-0.01</td></tr><tr><td>14</td><td>10.5</td><td>1.4</td><td>-0.53</td><td>-0.10</td><td>-0.02</td></tr><tr><td>15</td><td>11.3</td><td>0.9</td><td>-0.73</td><td>-0.15</td><td>1.21</td></tr><tr><td>16</td><td>11.6</td><td>0.7</td><td>-0.49</td><td>0.94</td><td>-0.84</td></tr><tr><td>17</td><td>12.0</td><td>0.6</td><td>-0.14</td><td>-0.06</td><td>0.04</td></tr><tr><td>18</td><td>12.6</td><td>0.5</td><td>--0.18</td><td>0.00</td><td>-0.45</td></tr><tr><td>19</td><td>13.0</td><td>0.4</td><td>-0.39</td><td>-0.54</td><td>0.60</td></tr><tr><td>20</td><td>13.3</td><td>0.25</td><td></td><td></td><td></td></tr></table>

![](images/7eda01c17c4c085e702c6e9c73b9f07b6f444acb7fe268394ca53689768e919b.jpg)  
Figure 3.11

For comparison purposes, Figure 3.12 gives an ilustration of the curve that is generated using a Lagrange interpolating polynomial to fit the data given in Table 3.15. This produces a very strange ilustration of the back of a duck, in flight or otherwise. The interpolating polynomial in this case is of degree 20 and oscillates wildly.

![](images/8374d9a2fd0b10f4458ceefc353423fea22cc8df1b6d4eed23990240398e12b4.jpg)  
Figure 3.12