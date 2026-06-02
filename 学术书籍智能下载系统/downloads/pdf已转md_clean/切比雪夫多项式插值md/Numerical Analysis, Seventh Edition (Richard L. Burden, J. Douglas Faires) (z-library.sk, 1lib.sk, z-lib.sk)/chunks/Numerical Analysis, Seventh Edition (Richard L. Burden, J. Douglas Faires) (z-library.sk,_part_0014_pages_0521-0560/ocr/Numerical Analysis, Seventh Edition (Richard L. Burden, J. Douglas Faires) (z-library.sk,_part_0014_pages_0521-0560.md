Since

$$
| P _ { n } ( \bar { x } _ { k } ^ { \prime } ) | \leq \frac { 1 } { 2 ^ { n - 1 } } , \quad \mathrm { f o r e a c h } \ k = 0 , 1 , \ldots , n ,
$$

we have

$$
Q ( \bar { x } _ { k } ^ { \prime } ) \leq 0 , \quad \mathrm { w h e n ~ } k \mathrm { ~ i s ~ o d d ~ } \quad \mathrm { a n d } \quad Q ( \bar { x } _ { k } ^ { \prime } ) \geq 0 , \quad \mathrm { w h e n ~ } k \mathrm { ~ i s ~ e v e n } .
$$

Since $Q$ is continuous,the Intermediate Value Theorem implies that the polynomial $Q ( x )$ has at least one zero between $\bar { \bar { x } } _ { j } ^ { \prime }$ and $\bar { \bar { x } } _ { j + 1 } ^ { \prime }$ , for each $j = 0 , 1 , \ldots , n - 1$ . Thus, $Q$ has at least $\pmb { n }$ zeros in the interval [-1,1]. But the degree of $Q ( x )$ is less than $\pmb { n }$ ，so $Q \equiv 0$ . This implies that $P _ { n } \equiv \tilde { T } _ { n }$ · ■

This theorem can be used to answer the question of where to place interpolating nodes to minimize the error in Lagrange interpolation. Theorem 3.3 applied to the interval $[ - 1 , 1 ]$ states that, if $x _ { 0 } , \ldots , x _ { n }$ are distinct numbers in the interval $[ - 1 , 1 ]$ and if $f \in C ^ { n + 1 } [ - 1 ,$ 1], then, for each $x \in [ - 1 , 1 ]$ , a number $\xi ( x )$ exists in $( - 1 , 1 )$ with

$$
f ( x ) - P ( x ) = { \frac { f ^ { ( n + 1 ) } ( \xi ( x ) ) } { ( n + 1 ) ! } } ( x - x _ { 0 } ) ( x - x _ { 1 } ) \cdots ( x - x _ { n } ) ,
$$

where $P ( x )$ is the Lagrange interpolating polynomial. Generally, there is no control over $\xi ( x )$ ， so to minimize the error by shrewd placement of the nodes $x _ { 0 } , \ldots , x _ { n }$ ，we find $x _ { 0 } , \ldots , x _ { n }$ to minimize the quantity

$$
| ( x - x _ { 0 } ) ( x - x _ { 1 } ) \cdot \cdot \cdot ( x - x _ { n } ) |
$$

throughout the interval [-1,1].

Since $( x - x _ { 0 } ) ( x - x _ { 1 } ) \cdot \cdot \cdot ( x - x _ { n } )$ is a monic polynomial of degree $( n + 1 )$ , we have just seen that the minimum is obtained when

$$
( x - x _ { 0 } ) ( x - x _ { 1 } ) \cdots ( x - x _ { n } ) = { \tilde { T } } _ { n + 1 } ( x ) .
$$

The maximum value of $| ( x - x _ { 0 } ) ( x - x _ { 1 } ) \cdot \cdot \cdot ( x - x _ { n } ) |$ is smallest when $x _ { k }$ is chosen to be the $( k + 1 )$ st zero of $\tilde { T } _ { n + 1 }$ , for each $k = 0 , 1 , \ldots , n ;$ that is, when $x _ { k }$ is

$$
\bar { x } _ { k + 1 } = \cos \frac { 2 k + 1 } { 2 ( n + 1 ) } \pi .
$$

Since $\begin{array} { r } { \operatorname* { m a x } _ { x \in [ - 1 , 1 ] } | \tilde { T } _ { n + 1 } ( x ) | = 2 ^ { - n } } \end{array}$ , this also implies that

$$
\frac { 1 } { 2 ^ { n } } = \operatorname* { m a x } _ { x \in [ - 1 , 1 ] } | ( x - \tilde { x } _ { 1 } ) \cdot \cdot \cdot ( x - \tilde { x } _ { n + 1 } ) | \leq \operatorname* { m a x } _ { x \in [ - 1 , 1 ] } | ( x - x _ { 0 } ) \cdot \cdot \cdot ( x - x _ { n } ) | ,
$$

for any choice of $x _ { 0 } , x _ { 1 } , \ldots , x _ { n }$ in the interval [-1,1]. The next corollary follows from this discussion.

Corollary 8.11If $P ( x )$ is the interpolating polynomial of degree at most $\pmb { n }$ with nodes at the roots of $T _ { n + 1 } ( x )$ ,then

$$
\operatorname* { m a x } _ { x \in [ - 1 , 1 ] } | f ( x ) - P ( x ) | \leq \frac { 1 } { 2 ^ { n } ( n + 1 ) ! } \operatorname* { m a x } _ { x \in [ - 1 , 1 ] } | f ^ { ( n + 1 ) } ( x ) | , \quad \mathrm { f o r ~ e a c h ~ } f \in C ^ { n + 1 } [ - 1 , 1 ] .
$$

This technique for choosing points to minimize the interpolating error is extended to a general closed interval $\{ a , b \}$ by using the change of variables

$$
\tilde { x } = \frac { 1 } { 2 } [ ( b - a ) x + a + b ]
$$

to transform the numbers $\bar { x } _ { k }$ in the interval [-1,1] into the corresponding number $\tilde { x } _ { k }$ in the interval $[ a , b ]$ , as shown in the next example.

Let $f ( x ) = x e ^ { x }$ on [0,1.5]. Two interpolation polynomials of degree at most three will be constructed. First, the equally spaced nodes $x _ { 0 } = 0 , x _ { 1 } = 0 . 5 , x _ { 2 } = 1$ , and $x _ { 3 } = 1 . 5$ are used to give

$$
\begin{array} { r l } & { L _ { 0 } ( x ) = - 1 . 3 3 3 3 x ^ { 3 } + 4 . 0 0 0 0 x ^ { 2 } - 3 . 6 6 6 7 x + 1 , } \\ & { L _ { 1 } ( x ) = 4 . 0 0 0 0 x ^ { 3 } - 1 0 . 0 0 0 x ^ { 2 } + 6 . 0 0 0 0 x , } \\ & { L _ { 2 } ( x ) = - 4 . 0 0 0 0 x ^ { 3 } + 8 . 0 0 0 0 x ^ { 2 } - 3 . 0 0 0 0 x , } \\ & { L _ { 3 } ( x ) = 1 . 3 3 3 3 x ^ { 3 } - 2 . 0 0 0 x ^ { 2 } + 0 . 6 6 6 7 x . } \end{array}
$$

For the values listed in the first two columns of Table 8.7,the first polynomial is given by

$$
P _ { 3 } ( x ) = 1 . 3 8 7 5 x ^ { 3 } + 0 . 0 5 7 5 7 0 x ^ { 2 } + 1 . 2 7 3 0 x .
$$

# Table 8.7

<table><tr><td>x</td><td>f(x)= xex</td><td>x</td><td>f(x）= xex</td></tr><tr><td>xo = 0.0</td><td>0.00000</td><td>x = 1.44291</td><td>6.10783</td></tr><tr><td>x1 = 0.5</td><td>0.824361</td><td>x= 1.03701</td><td>2.92517</td></tr><tr><td>x2 = 1.0</td><td>2.71828</td><td>x = 0.46299</td><td>0.73560</td></tr><tr><td>x = 1.5</td><td>6.72253</td><td>x= 0.05709</td><td>0.060444</td></tr></table>

For the second interpolating polynomial, shift the zeros $\bar { x } _ { k } = \cos ( ( 2 k + 1 ) / 8 ) \pi$ ,for $k = 0$ ,1,2,3,of $\tilde { T } _ { 4 }$ from[-1,1] to [0,1.5],using the linear transformation

$$
\tilde { x } _ { k } = \frac { 1 } { 2 } \left[ ( 1 . 5 - 0 ) \bar { x } _ { k } + ( 1 . 5 + 0 ) \right] = 0 . 7 5 + 0 . 7 5 \bar { x } _ { k }
$$

to obtain

$$
\tilde { x } _ { 0 } = 1 . 4 4 2 9 1 , \quad \tilde { x } _ { 1 } = 1 . 0 3 7 0 1 , \quad \tilde { x } _ { 2 } = 0 . 4 6 2 9 9 , \quad \mathrm { a n d } \quad \tilde { x } _ { 3 } = 0 . 0 5 7 0 9 .
$$

The Lagrange coefcient polynomials for this set of nodes are then computed as:

$$
\begin{array} { r l } & { \tilde { L } _ { 0 } ( x ) = 1 . 8 1 4 2 x ^ { 3 } - 2 . 8 2 4 9 x ^ { 2 } + 1 . 0 2 6 4 x - 0 . 0 4 9 7 2 8 , } \\ & { \tilde { L } _ { 1 } ( x ) = - 4 . 3 7 9 9 x ^ { 3 } + 8 . 5 9 7 7 x ^ { 2 } - 3 . 4 0 2 6 x + 0 . 1 6 7 0 5 , } \\ & { \tilde { L } _ { 2 } ( x ) = 4 . 3 7 9 9 x ^ { 3 } - 1 1 . 1 1 2 x ^ { 2 } + 7 . 1 7 3 8 x - 0 . 3 7 4 1 5 , } \\ & { \tilde { L } _ { 3 } ( x ) = - 1 . 8 1 4 2 x ^ { 3 } + 5 . 3 3 9 0 x ^ { 2 } - 4 . 7 9 7 6 x + 1 . 2 5 6 8 . } \end{array}
$$

The functional values required for these polynomials are given in the last two columns of Table 8.7. The interpolation polynomial of degree at most 3 is

$$
\tilde { P } _ { 3 } ( x ) = 1 . 3 8 1 1 x ^ { 3 } + 0 . 0 4 4 6 5 2 x ^ { 2 } + 1 . 3 0 3 1 x - 0 . 0 1 4 3 5 2 .
$$

For comparison, Table 8.8 lists various values of $\pmb { x }$ ， together with the values of $f ( x ) , P _ { 3 } ( x )$ ,and $\tilde { P } _ { 3 } ( x )$ . It can be seen from this table that, although the error using $P _ { 3 } ( x )$ is less than using $\tilde { P } _ { 3 } ( x )$ near the middle of the table, the maximum error involved with using $\tilde { P } _ { 3 } ( x )$ , 0.0180, is considerably less than when using $P _ { 3 } ( x )$ ， which gives the error 0.0290. (See Figure 8.12.) ■

# Table 8.8

<table><tr><td>X</td><td>f(x）=xex</td><td>P(x)</td><td>1xex-P(x)1</td><td>P(x）</td><td>xex-P(x)1</td></tr><tr><td>0.15</td><td>0.1743</td><td>0.1969</td><td>0.0226</td><td>0.1868</td><td>0.0125</td></tr><tr><td>0.25</td><td>0.3210</td><td>0.3435</td><td>0.0225</td><td>0.3358</td><td>0.0148</td></tr><tr><td>0.35</td><td>0.4967</td><td>0.5121</td><td>0.0154</td><td>0.5064</td><td>0.0097</td></tr><tr><td>0.65</td><td>1.245</td><td>1.233</td><td>0.012</td><td>1.231</td><td>0.014</td></tr><tr><td>0.75</td><td>1.588</td><td>1.572</td><td>0.016</td><td>1.571</td><td>0.017</td></tr><tr><td>0.85</td><td>1.989</td><td>1.976</td><td>0.013</td><td>1.974</td><td>0.015</td></tr><tr><td>1.15</td><td>3.632</td><td>3.650</td><td>0.018</td><td>3.644</td><td>0.012</td></tr><tr><td>1.25</td><td>4.363</td><td>4.391</td><td>0.028</td><td>4.382</td><td>0.019</td></tr><tr><td>1.35</td><td>5.208</td><td>5.237</td><td>0.029</td><td>5.224</td><td>0.016</td></tr></table>

![](images/68d29642cf7ed3a8a9beb395ab879b9f026bac6c4d178fbcdafd25c716454a93.jpg)  
Figure 8.12

Chebyshev polynomials can also be used to reduce the degree of an approximating polynomial with a minimal loss of accuracy. Because the Chebyshev polynomials have a minimum maximum-absolute value that is spread uniformly on an interval, they can be

used to reduce the degree of an approximation polynomial without exceeding the error tolerance.

Consider approximating an arbitrary $\pmb { n }$ th-degree polynomial

$$
P _ { n } ( x ) = a _ { n } x ^ { n } + a _ { n - 1 } x ^ { n - 1 } + \cdots + a _ { 1 } x + a _ { 0 }
$$

on $[ - 1 , 1 ]$ with a polynomial of degree at most $n - 1$ . The object is to choose $P _ { n - 1 } ( x )$ in $\prod _ { n - 1 }$ so that

$$
\operatorname* { m a x } _ { x \in [ - 1 , 1 ] } | P _ { n } ( x ) - P _ { n - 1 } ( x ) |
$$

is as small as possible.

We first note that $( P _ { n } ( x ) - P _ { n - 1 } ( x ) ) / a _ { n }$ is a monic polynomialof degree $\pmb { n }$ , so applying Theorem 8.10 gives

$$
\operatorname* { m a x } _ { x \in [ - 1 , 1 ] } \left| { \frac { 1 } { a _ { n } } } ( P _ { n } ( x ) - P _ { n - 1 } ( x ) ) \right| \geq { \frac { 1 } { 2 ^ { n - 1 } } } .
$$

Equality occurs precisely when

$$
{ \frac { 1 } { a _ { n } } } ( P _ { n } ( x ) - P _ { n - 1 } ( x ) ) = { \tilde { T } } _ { n } ( x ) .
$$

This means that we should choose

$$
P _ { n - 1 } ( x ) = P _ { n } ( x ) - a _ { n } \tilde { T } _ { n } ( x ) ,
$$

and with this choice we have the minimum value of

$$
\operatorname* { m a x } _ { x \in \{ - 1 , 1 \} } | P _ { n } ( x ) - P _ { n - 1 } ( x ) | = | a _ { n } | \operatorname* { m a x } _ { x \in \{ - 1 , 1 \} } \left| { \frac { 1 } { a _ { n } } } ( P _ { n } ( x ) - P _ { n - 1 } ( x ) ) \right| = { \frac { | a _ { n } | } { 2 ^ { n - 1 } } } .
$$

# EXAMPLE 2

The function $f ( x ) = e ^ { x }$ is approximated on the interval [-1,1]by the fourth Maclaurin polynomial

$$
P _ { 4 } ( x ) = 1 + x + { \frac { x ^ { 2 } } { 2 } } + { \frac { x ^ { 3 } } { 6 } } + { \frac { x ^ { 4 } } { 2 4 } } ,
$$

which has truncation error

$$
| R _ { 4 } ( x ) | = \frac { | f ^ { ( 5 ) } ( \xi ( x ) ) | | x ^ { 5 } | } { 1 2 0 } \leq \frac { e } { 1 2 0 } \approx 0 . 0 2 3 , \mathrm { ~ f o r ~ } - 1 \leq x \leq 1 .
$$

Suppose that an error of O.O5 is tolerable and that we would like to reduce the degree of the approximating polynomial while staying within this bound.

The polynomial of degree 3 or less that best uniformly approximates $P _ { 4 } ( x ) \mathrm { o n } [ - 1 , 1 ]$ is

$$
\begin{array} { c } { { P _ { 3 } ( x ) = P _ { 4 } ( x ) - a _ { 4 } \tilde { T } _ { 4 } ( x ) = 1 + x + { \frac { x ^ { 2 } } { 2 } } + { \frac { x ^ { 3 } } { 6 } } + { \frac { x ^ { 4 } } { 2 4 } } - { \frac { 1 } { 2 4 } } \left( x ^ { 4 } - x ^ { 2 } + { \frac { 1 } { 8 } } \right) } } \\ { { = { \frac { 1 9 1 } { 1 9 2 } } + x + { \frac { 1 3 } { 2 4 } } x ^ { 2 } + { \frac { 1 } { 6 } } x ^ { 3 } . } } \end{array}
$$

With this choice, we have

$$
\vert P _ { 4 } ( x ) - P _ { 3 } ( x ) \vert = \vert a _ { 4 } \tilde { T } _ { 4 } ( x ) \vert \le \frac { 1 } { 2 4 } \cdot \frac { 1 } { 2 ^ { 3 } } = \frac { 1 } { 1 9 2 } \le 0 . 0 0 5 3 .
$$

Adding this error bound to the bound for the Maclaurin truncation error gives

$$
0 . 0 2 3 + 0 . 0 0 5 3 = 0 . 0 2 8 3 ,
$$

which is still within the permissible error of 0.05.

The polynomial of degree 2 or less that best uniformly approximates $P _ { 3 } ( x )$ on [-1,1] is

$$
{ \begin{array} { r l } & { P _ { 2 } ( x ) = P _ { 3 } ( x ) - { \cfrac { 1 } { 6 } } { \tilde { T } } _ { 3 } ( x ) } \\ & { \qquad = { \cfrac { 1 9 1 } { 1 9 2 } } + x + { \cfrac { 1 3 } { 2 4 } } x ^ { 2 } + { \cfrac { 1 } { 6 } } x ^ { 3 } - { \cfrac { 1 } { 6 } } ( x ^ { 3 } - { \cfrac { 3 } { 4 } } x ) = { \cfrac { 1 9 1 } { 1 9 2 } } + { \cfrac { 9 } { 8 } } x + { \cfrac { 1 3 } { 2 4 } } x ^ { 2 } . } \end{array} }
$$

However,

$$
| P _ { 3 } ( x ) - P _ { 2 } ( x ) | = | \frac { 1 } { 6 } \tilde { T } _ { 3 } ( x ) | = \frac { 1 } { 6 } \left( \frac { 1 } { 2 } \right) ^ { 2 } = \frac { 1 } { 2 4 } \approx 0 . 0 4 2 ,
$$

which—when added to the already accumulated error bound of O.0283-exceeds the tolerance of O.05. Consequently, the polynomial of least degree that best approximates $e ^ { x }$ on $[ - 1 , 1 ]$ with an error bound of less than 0.05 is

$$
P _ { 3 } ( x ) = \frac { 1 9 1 } { 1 9 2 } + x + \frac { 1 3 } { 2 4 } x ^ { 2 } + \frac { 1 } { 6 } x ^ { 3 } .
$$

Table 8.9 lists the function and the approximating polynomials at various points in $[ - 1 , 1 ]$ Note that the tabulated entries for $P _ { 2 }$ are well within the tolerance of O.O5,even though the error bound for $P _ { 2 } ( x )$ exceeded the tolerance.

# Table 8.9

<table><tr><td>x</td><td>er</td><td>P4(x)</td><td>P(x)</td><td>P(x)</td><td>lex- P(x)1</td></tr><tr><td>-0.75</td><td>0.47237</td><td>0.47412</td><td>0.47917</td><td>0.45573</td><td>0.01664</td></tr><tr><td>-0.25</td><td>0.77880</td><td>0.77881</td><td>0.77604</td><td>0.74740</td><td>0.03140</td></tr><tr><td>0.00</td><td>1.00000</td><td>1.00000</td><td>0.99479</td><td>0.99479</td><td>0.00521</td></tr><tr><td>0.25</td><td>1.28403</td><td>1.28402</td><td>1.28125</td><td>1.30990</td><td>0.02587</td></tr><tr><td>0.75</td><td>2.11700</td><td>2.11475</td><td>2.11979</td><td>2.14323</td><td>0.02623</td></tr></table>

# ExERcIse SEt 8.3

1.Use the zeros of $\tilde { T } _ { 3 }$ to construct an interpolating polynomial of degree 2 for the following functions on the interval [-1, 1].

a. $\begin{array} { l } { f ( x ) = e ^ { x } } \\ { f ( x ) = \ln ( x + 2 ) } \end{array}$ $\begin{array} { r l } { \mathbf { b } . \quad f ( x ) = \sin { x } } \\ { \mathbf { d } . \quad f ( x ) = x ^ { 4 } } \end{array}$   
c.

2.Find a bound for the maximum error of the approximation in Exercise 1 on the interval $\{ - 1 , 1 \}$ ·

3.Use the zeros of $\tilde { T } _ { 4 }$ to construct an interpolating polynomial of degree 3 for the functions in Exercise 1.

4.Repeat Exercise 2 for the approximations computed in Exercise 3.

5.Use the zeros of $\tilde { T } _ { 3 }$ and transformations of the given interval to construct an interpolating polynomial of degree 2 for the following functions.

$$
\begin{array} { l l l } { { f ( x ) = \displaystyle \frac { 1 } { x } , \quad [ 1 , 3 ] } } & { { \quad \mathrm { ~ b } . \quad f ( x ) = e ^ { - x } , \quad [ 0 , 2 ] } } \\ { { \displaystyle f ( x ) = \displaystyle \frac { 1 } { 2 } \cos x + \displaystyle \frac { 1 } { 3 } \sin 2 x , \quad [ 0 , 1 ] } } & { { \quad \mathrm { ~ d } . \quad f ( x ) = x \ln x , \quad [ 1 , 3 ] } } \end{array}
$$

6. Find the sixth Maclaurin polynomial for $x e ^ { x }$ , and use Chebyshev economization to obtain a lesser-degree polynomial approximation while keeping the error less than 0.01 on $\{ - 1 , 1 \}$ ·

7．Find the sixth Maclaurin polynomial for sin $\pmb { x }$ ,and use Chebyshev economization to obtain a lesser-degree polynomial approximation while keeping the error Iess than 0.01 on $[ - 1 , 1 ]$

8.Show that for any positive integers $i$ and $j$ with $i > j$ ， we have $\begin{array} { r } { T _ { i } ( x ) T _ { j } ( x ) = \frac { 1 } { 2 } [ T _ { i + j } ( x ) + } \end{array}$ $T _ { i - j } ( { \pmb x } ) ]$

9.Show that for each Chebyshev polynomial $T _ { n } ( x )$ , we have

$$
\quad \int _ { - 1 } ^ { 1 } { \frac { [ T _ { n } ( x ) ] ^ { 2 } } { \sqrt { 1 - x ^ { 2 } } } } d x = { \frac { \pi } { 2 } } .
$$

# 8.4 Rational Function Approximation

The class of algebraic polynomials has some distinct advantages for use in approximation:

1.there are a suficient number of polynomials to approximate any continuous function on a closed interval to within an arbitrary tolerance;   
2.polynomials are easily evaluated at arbitrary values; and   
3.the derivatives and integrals of polynomials exist and are easily determined.

The disadvantage of using polynomials for approximation is their tendency for oscillation. This often causes error bounds in polynomial approximation to significantly exceed the average approximation error, since error bounds are determined by the maximum approximation error. We now consider methods that spread the approximation error more evenly over the approximation interval. These techniques involve rational functions.

A rational function $r$ of degree $N$ has the form

$$
r ( x ) = \frac { p ( x ) } { q ( x ) } ,
$$

where $p ( x )$ and $q ( x )$ are polynomials whose degrees sum to $N$

Since every polynomial is a rational function (simply let $q ( x ) \equiv 1 )$ ， approximation by rational functions gives results that are no worse than approximation by polynomials. However, rational functions whose numerator and denominator have the same or nearly the same degree generally produce approximation results superior to polynomial methods for the same amount of computation effort. (This statement is based on the assumption that the amount of computation effort required for division is approximately the same as for multiplication.） Rational functions have the added advantage of permitting efficient approximation of functions with infinite discontinuities near, but outside,the interval of approximation. Polynomial approximation is generally unacceptable in this situation.

Suppose $r$ is a rational function of degree $N = n + m$ of the form

$$
r ( x ) = { \frac { p ( x ) } { q ( x ) } } = { \frac { p _ { 0 } + p _ { 1 } x + \cdots + p _ { n } x ^ { n } } { q _ { 0 } + q _ { 1 } x + \cdots + q _ { m } x ^ { m } } } ,
$$

that is used to approximate a function $f$ on a closed interval $I$ containing zero. For $r$ t0 be defined at zero requires that $q _ { 0 } \neq 0$ . In fact, we can assume that $q _ { 0 } = 1$ , for if this is not the case we simply replace $p ( x )$ by $p ( x ) / q _ { 0 }$ and $q ( x )$ by $q ( x ) / q _ { 0 }$ . Consequently, there are $N + 1$ parameters $q _ { 1 } , q _ { 2 } , \ldots , q _ { m } , p _ { 0 } , p _ { 1 } , \ldots , p _ { n }$ available for the approximation of $f$ by $r$

The Padé approximation technique,which is the extension of Taylor poiynomial approximation to rational functions, chooses the $N { + 1 }$ parameters so that $f ^ { ( k ) } ( 0 ) = r ^ { ( k ) } ( 0 )$ ， for each $k = 0 , 1 , \ldots , N$ When $n = N$ and $m = 0$ ,the Padé approximation is just the $N$ th Maclaurin polynomial.

Consider the difference

$$
\dot { \mathbf { \Psi } } ( x ) - r ( x ) = f ( x ) - \frac { p ( x ) } { q ( x ) } = \frac { f ( x ) q ( x ) - p ( x ) } { q ( x ) } = \frac { f ( x ) \sum _ { i = 0 } ^ { m } q _ { i } x ^ { i } - \sum _ { i = 0 } ^ { n } p _ { i } x ^ { i } } { q ( x ) } ,
$$

and suppose $f$ has the Maclaurin series expansion $\textstyle f ( x ) = \sum _ { i = 0 } ^ { \infty } a _ { i } x ^ { i }$ . Then

$$
f ( x ) - r ( x ) = { \frac { \sum _ { i = 0 } ^ { \infty } a _ { i } x ^ { i } \sum _ { i = 0 } ^ { m } q _ { i } x ^ { i } - \sum _ { i = 0 } ^ { n } p _ { i } x ^ { i } } { q ( x ) } } .
$$

The object is to choose the constants $q _ { 1 } , q _ { 2 } , \ldots , q _ { m }$ and $p _ { 0 } , p _ { 1 } , \ldots , p _ { n }$ so that

$$
f ^ { ( k ) } ( 0 ) - r ^ { ( k ) } ( 0 ) = 0 , \quad \mathrm { f o r } \operatorname { e a c h } k = 0 , 1 , \dots , N .
$$

In Section 2.4 (see,in particular, Exercise 10) we found that this is equivalent to $f \sim r$ having a zero of multiplicity $N + 1$ at $x = 0$ . As a consequence, we choose $q _ { 1 } , q _ { 2 } , \ldots , q _ { m }$ and $p _ { 0 } , p _ { 1 } , \ldots , p _ { n }$ so that the numerator on the right side of Eq. (8.14),

$$
( a _ { 0 } + a _ { 1 } x + \cdot \cdot \cdot ) ( 1 + q _ { 1 } x + \cdot \cdot \cdot + q _ { m } x ^ { m } ) - ( p _ { 0 } + p _ { 1 } x + \cdot \cdot \cdot + p _ { n } x ^ { n } ) ,
$$

has no terms of degree less than or equal to $N$ ·

To simplify notation, we define $p _ { n + 1 } = p _ { n + 2 } = \cdot \cdot \cdot = p _ { N } = 0$ and $q _ { m + 1 } = q _ { m + 2 } =$ $\dots { } = q _ { N } = 0$ . We can then express the coefficient of $x ^ { k }$ in expression (8.15) as

$$
\left( \sum _ { i = 0 } ^ { k } a _ { i } q _ { k - i } \right) - p _ { k } .
$$

So,the rational function for Padé approximation results from the solution of the $N + 1$ linear equations

$$
\sum _ { i = 0 } ^ { k } a _ { i } q _ { k - i } = p _ { k } , \quad k = 0 , 1 , \dots , N
$$

in the $N + 1$ unknowns $q _ { 1 } , q _ { 2 } , \ldots , q _ { m } , p _ { 0 } , p _ { 1 } , \ldots , p _ { n } .$

# EXAMPLE 1

The Maclaurin series expansion for $e ^ { - x }$ is

$$
\sum _ { i = 0 } ^ { \infty } { \frac { ( - 1 ) ^ { i } } { i ! } } x ^ { i } .
$$

To find the Padé approximation to $e ^ { - x }$ of degree 5 with $n = 3$ and $m = 2$ requires choosing Po, P1,P2, P3,q1,and q2 so that the coefcients of xk for k = O,1,..,5 are zero in the expression

$$
\biggl ( 1 - x + { \frac { x ^ { 2 } } { 2 } } - { \frac { x ^ { 3 } } { 6 } } + \cdot \cdot \cdot \biggr ) ( 1 + q _ { 1 } x + q _ { 2 } x ^ { 2 } ) - ( p _ { 0 } + p _ { 1 } x + p _ { 2 } x ^ { 2 } + p _ { 3 } x ^ { 3 } ) .
$$

Expanding and collecting terms produces

$$
\begin{array} { c c c c c c } { { x ^ { 5 } : } } & { { - \displaystyle \frac { 1 } { 1 2 0 } + \frac { 1 } { 2 4 } q _ { 1 } - \frac { 1 } { 6 } q _ { 2 } = 0 ; } } & { { } } & { { x ^ { 2 } : } } & { { \displaystyle \frac { 1 } { 2 } - q _ { 1 } + q _ { 2 } = p _ { 2 } ; } } \\ { { } } & { { } } & { { \displaystyle { x ^ { 4 } : } } } & { { \displaystyle \frac { 1 } { 2 4 } - \mathrm { ~ } \frac { 1 } { 6 } q _ { 1 } + \frac { 1 } { 2 } q _ { 2 } = 0 ; } } & { { } } & { { x ^ { 1 } : } } & { { - 1 + q _ { 1 } } } \\ { { } } & { { } } & { { \displaystyle { x ^ { 3 } : } } } & { { - \displaystyle \frac { 1 } { 6 } + \mathrm { ~ } \frac { 1 } { 2 } q _ { 1 } - q _ { 2 } = p _ { 3 } ; } } & { { } } & { { x ^ { 0 } : } } & { { 1 } } \end{array} = p _ { 1 } ;
$$

To solve the system in Maple, we use the following commands:

>eq1 $: = - 1 + { \tt q } 1 { \tt = p } 1$ ；  
>eq2: 1/2-q1+q2=p2;  
$\mathtt { \mathtt { e q 3 : = - 1 / 6 + 1 / 2 * q 1 - q 2 = p 3 } }$ ；  
>eq4: $\mathbf { = }$ 1/24-1/6\*q1+1/2\*q2=0;  
>eq5:=-1/120+1/24\*q1-1/6\*q2=0;  
>solve({eq1,eq2,eq3,eq4,eq5},{q1,q2,p1,p2,p3});

giving

$$
p _ { 0 } = 1 , \ p _ { 1 } = - { \frac { 3 } { 5 } } , \ p _ { 2 } = { \frac { 3 } { 2 0 } } , \ p _ { 3 } = - { \frac { 1 } { 6 0 } } , \ q _ { 1 } = { \frac { 2 } { 5 } } , \ \mathrm { a n d } \ q _ { 2 } = { \frac { 1 } { 2 0 } } .
$$

Table 8.10   

<table><tr><td>X</td><td>e-x</td><td>Ps(x)</td><td>le-x-Ps(x）</td><td>r(x)</td><td>le-x-r(x）1</td></tr><tr><td>0.2</td><td>0.81873075</td><td>0.81873067</td><td>8.64×10-8</td><td>0.81873075</td><td>7.55×10-9</td></tr><tr><td>0.4</td><td>0.67032005</td><td>0.67031467</td><td>5.38 × 10-6</td><td>0.67031963</td><td>4.11 × 10-7</td></tr><tr><td>0.6</td><td>0.54881164</td><td>0.54875200</td><td>5.96 × 10-5</td><td>0.54880763</td><td>4.00 × 10-6</td></tr><tr><td>0.8</td><td>0.44932896</td><td>0.44900267</td><td>3.26× 10-4</td><td>0.44930966</td><td>1.93 × 10-5</td></tr><tr><td>1.0</td><td>0.36787944</td><td>0.36666667</td><td>1.21×10-3</td><td>0.36781609</td><td>6.33 × 10-5</td></tr></table>

So the Padé approximation is

$$
r ( x ) = \frac { 1 - \frac { 3 } { 5 } x + \frac { 3 } { 2 0 } x ^ { 2 } - \frac { 1 } { 6 0 } x ^ { 3 } } { 1 + \frac { 2 } { 5 } x + \frac { 1 } { 2 0 } x ^ { 2 } } .
$$

Table 8.10 lists values of $r ( x )$ and $P _ { 5 } ( x )$ ,the fifth Maclaurin polynomial. The Padé approximation is clearly superior in this example.

Maple can also be used directly to compute a Padé approximation. We first compute the Maclaurin series with the call

>series $( \exp \left( - \mathbf { x } \right) , \mathbf { x } )$ ；

to obtain

$$
1 - x + \frac { 1 } { 2 } x ^ { 2 } - \frac { 1 } { 6 } x ^ { 3 } + \frac { 1 } { 2 4 } x ^ { 4 } - \frac { 1 } { 1 2 0 } x ^ { 5 } + { \cal { O } } ( x ^ { 6 } )
$$

The Padé approximation with $n = 3$ and $m = 2$ is computed using the command

>g:=convert(%,ratpoly,3,2);

where the % refers to the result of the preceding calculation, namely, the series. The result is

$$
g : = \frac { 1 - \frac 3 5 x + \frac 3 { 2 0 } x ^ { 2 } - \frac 1 { 6 0 } x ^ { 3 } } { 1 + \frac 2 5 x + \frac 1 { 2 0 } x ^ { 2 } } .
$$

We can then compute, for example, $g ( 0 . 8 )$ by entering

>evalf(subs $( \mathbf { x } { = } 0 , 8 , \mathbf { g } )$ ；

to get .4493096647.

Algorithm 8.1 implements the Padé approximation technique.

# Padé Rational Approximation

To obtain the rational approximation

$$
r ( x ) = { \frac { p ( x ) } { q ( x ) } } = { \frac { \sum _ { i = 0 } ^ { n } p _ { i } x ^ { i } } { \sum _ { j = 0 } ^ { m } q _ { j } x ^ { j } } }
$$

for a given function $f ( x )$ ：

INPUT nonnegative integers m and $\pmb { n }$

OUTPUT coefficients $q _ { 0 } , q _ { 1 } , \ldots , q _ { m }$ and $p _ { 0 } , p _ { 1 } , \ldots , p _ { n } .$

Step 1 Set $N = m + n$

Step 2 For $i = 0 , 1 , \ldots , N$ set $a _ { i } = \frac { f ^ { ( i ) } ( 0 ) } { i ! }$ -

(The coefficients of the Maclaurin polynomial are $a _ { 0 } , \ldots , a _ { N }$ , which could be input instead of calculated.)

Step 3 Set $q _ { 0 } = 1$ ；$p _ { 0 } = a _ { 0 } .$

Step 4 For $i = 1 , 2 , \dots , N$ do Steps 5-10.(Set up a linear system with matrix B.)

$$
\begin{array} { r l } { \stackrel { , } { \boldsymbol { \Sigma } } } & { \operatorname { F o r } j = 1 , 2 , \ldots , i - 1 } \\ & { \qquad \mathrm { i f } j \leq n \mathrm { t h e n ~ s e t } b _ { i , j } = 0 . } \end{array}
$$

Step $\sigma$ $i \leq n$ then set $b _ { i , i } = 1$

Step 7For $j = i + 1 , i + 2 , . . . , N \mathrm { s e t } b _ { i , j } = 0 .$

Step 8 For $j = 1 , 2 , \dots , i$ if $j \leq m$ then set $b _ { i , n + j } = - a _ { i - j }$

Step 9 For $\dot { \cdot } j = n + i + 1 , n + i + 2 , \ldots , N \operatorname { s e t } b _ { i , j } = 0 .$

Step 10 Set $b _ { i , N + 1 } = a _ { i }$

(Steps 11-22 solve the linear system using partial pivoting.)

Step 11For $i = n + 1 , n + 2 , \ldots , N - 1$ do Steps 12-18.

Step 12 Let $k$ be the smallest integer with $i \le k \le N$ and $\vert b _ { k , i } \vert = \mathbf { m a x } _ { i \leq j \leq N } \vert b _ { j , i } \vert$ (Find pivot element.)

Step 13 If $b _ { k , i } = 0$ then OUTPUT ("The system is singular "); STOP.

Step 14 If $k \neq i$ then(Interchange row i and row $k$ ） for $j = i , i + 1 , \dots , N + 1$ set

$$
\begin{array} { c } { b _ { C O P Y } = b _ { i , j } ; } \\ { b _ { i , j } = b _ { k , j } ; } \\ { b _ { k , j } = b _ { C O P Y } . } \end{array}
$$

Step 15 For $j = i + 1 , i + 2 , \dots , N$ do Steps 16-18. (Perform elimination.)

Step 16 Set $x m = \frac { b _ { j , i } } { b _ { i , i } }$

$\mathit { S t e p 1 7 } \quad \mathrm { F o r } \ : k = i + 1 , i + 2 , \ldots , N + 1$ set $b _ { j , k } = b _ { j , k } - x m \cdot b _ { i , k }$

Step 18 Set $b _ { j , i } = 0$

Step 19 If $b _ { N , N } = 0$ then OUTPUT("The system is singular"); STOP.

Step 20 If $m > 0$ then set $q _ { m } = { \frac { b _ { N , N + 1 } } { b _ { N , N } } }$ (Start backward substitution.)

$$
\mathrm { F o r } i = N - 1 , N - 2 , \ldots , n + 1 \mathrm { s e t } q _ { i - n } = \frac { b _ { i , N + 1 } - \sum _ { j = i + 1 } ^ { N } b _ { i , j } q _ { j - n } } { b _ { i , i } } .
$$

$$
\begin{array} { r } { \cdot \ i = n , n - 1 , \dots , 1 \mathrm { ~ s e t ~ } p _ { i } = b _ { i , N + 1 } - \sum _ { j = n + 1 } ^ { N } b _ { i , j } q _ { j - n } . } \end{array}
$$

Step 23OUTPUT $( q _ { 0 } , q _ { 1 } , . . . , q _ { m } , p _ { 0 } , p _ { 1 } , . . . , p _ { n } )$ STOP. (The procedure was successful.)

It is interesting to compare the number of arithmetic operations required for calculations of $P _ { 5 } ( x )$ and $r ( x )$ in Example 1. Using nested multiplication, $P _ { 5 } ( x )$ can be expressed as

$$
P _ { 5 } ( x ) = \left( \left( \left( \left( - { \frac { 1 } { 1 2 0 } } x + { \frac { 1 } { 2 4 } } \right) x - { \frac { 1 } { 6 } } \right) x + { \frac { 1 } { 2 } } \right) x - 1 \right) x + 1 .
$$

Assuming that the coefficients of $1 , x , x ^ { 2 } , x ^ { 3 } , x ^ { 4 }$ ，and $x ^ { 5 }$ are represented as decimals, a single calculation of $P _ { 5 } ( x )$ in nested form requires five multiplications and five additions/subtractions.

Using nested multiplication, $r ( x )$ is expressed as

$$
r ( x ) = \frac { \left( \left( - \frac { 1 } { 6 0 } x + \frac { 3 } { 2 0 } \right) x - \frac { 3 } { 5 } \right) x + 1 } { \left( \frac { 1 } { 2 0 } x + \frac { 2 } { 5 } \right) x + 1 } ,
$$

so a single calculation of $r ( x )$ requires five multiplications, five additions/subtractions, and one division. Hence, computational effort appears to favor the polynomial approximation. However, by reexpressing $r ( x )$ by continued division, we can write

$$
\begin{array} { c } { { r ( x ) = \displaystyle \frac { 1 - \frac { 3 } { 3 } x + \frac { 3 } { 2 0 } x ^ { 2 } - \frac { 1 8 } { 6 0 } x ^ { 3 } } { 1 + \frac { 2 } { 3 } x + \frac { 2 } { 2 0 } x ^ { 2 } } } } \\ { { = \displaystyle \frac { - \frac { 1 } { 3 } x ^ { 3 } + 3 x ^ { 2 } - 1 2 x + 2 0 } { x ^ { 2 } + 8 x + 2 0 } } } \\ { { = - \frac { 1 } { 3 } x + \frac { 1 7 } { 3 } + \frac { ( - \frac { 1 5 2 x } { 3 } x - \frac { 2 8 0 } { 3 } ) } { x ^ { 2 } + 8 x + 2 0 } } } \\ { { = - \frac { 1 } { 3 } x + \frac { 1 7 } { 3 } + \frac { - \frac { 1 5 2 } { 3 } } { \left( \frac { x ^ { 2 } + 8 x + 2 0 } { x + 3 ( 3 5 + 2 0 ) } \right) } } } \end{array}
$$

or

$$
r ( x ) = - { \frac { 1 } { 3 } } x + { \frac { 1 7 } { 3 } } + { \frac { - { \frac { 1 5 2 } { 3 } } } { \left( x + { \frac { 1 1 7 } { 1 9 } } + { \frac { 3 1 2 5 / 3 6 1 } { ( x + ( 3 5 / 1 9 ) ) } } \right) } } .
$$

Writen in this form, a single calculation of $r ( x )$ requires one multiplication, five additions/subtractions, and two divisions. If the amount of computation required for division is approximately the same as for multiplication, the computational effort required for an evaluation of $P _ { 5 } ( x )$ significantly exceeds that required for an evaluation of $r ( x )$

Expressing a rational function approximation in a form such as Eq. (8.16) is called continued-fraction approximation. This is a classical approximation technique of current interest because of the computational efficiency of this representation. It is, however, a specialized technique that we will not discuss further. A rather extensive treatment of this subject and of rational approximation in general can be found in [RR, pp.285-322].

Although the rational-function approximation in Example 1 gave results superior to the polynomial approximation of the same degree, the approximation has a wide variation in accuracy. The approximation at O.2 is accurate to within $8 \times 1 0 ^ { - 9 }$ ，while at 1.0 the approximation and the function agree only to within $7 \times 1 0 ^ { - 5 }$ . This accuracy variation is expected because the Padé approximation is based on a Taylor polynomial representation of $e ^ { - x }$ , and the Taylor representation has a wide variation of accuracy in [0.2,1.0].

To obtain more uniformly accurate rational-function approximations we use Cheby-shev polynomials,a class that exhibits more uniform behavior. The general Chebyshev rational-function approximation method proceeds in the same manner as Padé approximation, except that each $x ^ { k }$ term in the Padé approximation is replaced by the $k$ th-degree Chebyshev polynomial $T _ { k } ( x )$

Suppose we want to approximate the function $f$ by an $N$ th-degree rational function $r$ written in the form

$$
r ( x ) = { \frac { \sum _ { k = 0 } ^ { n } p _ { k } T _ { k } ( x ) } { \sum _ { k = 0 } ^ { m } q _ { k } T _ { k } ( x ) } } , \quad { \mathrm { w h e r e ~ } } N = n + m { \mathrm { ~ a n d ~ } } q _ { 0 } = 1
$$

Writing $f ( x )$ in a series involving Chebyshev polynomials as

$$
f ( x ) = \sum _ { k = 0 } ^ { \infty } a _ { k } T _ { k } ( x )
$$

gives

$$
f ( x ) - r ( x ) = \sum _ { k = 0 } ^ { \infty } a _ { k } T _ { k } ( x ) - { \frac { \sum _ { k = 0 } ^ { n } p _ { k } T _ { k } ( x ) } { \sum _ { k = 0 } ^ { m } q _ { k } T _ { k } ( x ) } }
$$

or

$$
f ( x ) - r ( x ) = { \frac { \sum _ { k = 0 } ^ { \infty } a _ { k } T _ { k } ( x ) \sum _ { k = 0 } ^ { m } q _ { k } T _ { k } ( x ) - \sum _ { k = 0 } ^ { n } p _ { k } T _ { k } ( x ) } { \sum _ { k = 0 } ^ { m } q _ { k } T _ { k } ( x ) } } .
$$

The coefficients $q _ { 1 } , q _ { 2 } , \ldots , q _ { m }$ and $p _ { 0 } , p _ { 1 } , \ldots , p _ { n }$ are chosen so that the numerator on the right-hand side of this equation has zero coefficients for $T _ { k } ( x )$ when $k = 0 , 1 , \ldots , N$ .This implies that the series

$$
\begin{array} { c } { { ( a _ { 0 } T _ { 0 } ( x ) + a _ { 1 } T _ { 1 } ( x ) + \cdot \cdot \cdot ) ( T _ { 0 } ( x ) + q _ { 1 } T _ { 1 } ( x ) + \cdot \cdot \cdot + q _ { m } T _ { m } ( x ) ) } } \\ { { { } } } \\ { { - ( p _ { 0 } T _ { 0 } ( x ) + p _ { 1 } T _ { 1 } ( x ) + \cdot \cdot \cdot + p _ { n } T _ { n } ( x ) ) } } \end{array}
$$

has no terms of degree less than or equal to $N$ .

Two problems arise with the Chebyshev procedure that make it more difficult to im-plement than the Padé method. One occurs because the product of the polynomial $q ( x )$ and the series for $f ( x )$ involves products of Chebyshev polynomials.This problem is resolved by making use of the relationship

$$
T _ { i } ( x ) T _ { j } ( x ) = \frac { 1 } { 2 } \left[ T _ { i + j } ( x ) + T _ { \mid i - j \mid } ( x ) \right] .
$$

(See Exercise 8 of Section 8.3.) The other problem is more diffcult to resolve and involves the computation of the Chebyshev series for $f ( x )$ . In theory, this is not difficult for if

$$
f ( x ) = \sum _ { k = 0 } ^ { \infty } a _ { k } T _ { k } ( x ) ,
$$

then the orthogonality of the Chebyshev polynomials implies that

$$
a _ { 0 } = \frac { 1 } { \pi } \int _ { - 1 } ^ { 1 } \frac { f ( x ) } { \sqrt { 1 - x ^ { 2 } } } ~ d x \quad \mathrm { a n d } \quad a _ { k } = \frac { 2 } { \pi } \int _ { - 1 } ^ { 1 } \frac { f ( x ) T _ { k } ( x ) } { \sqrt { 1 - x ^ { 2 } } } ~ d x , \quad \mathrm { w h e r e } ~ k \geq
$$

Practically, however, these integrals can seldom be evaluated in closed form,and a numerical integration technique is required for each evaluation.

# EXAMPLE 2

The first five terms of the Chebyshev expansion for $e ^ { - x }$ are

$$
\begin{array} { r l } & { \tilde { P } _ { 5 } ( x ) = 1 . 2 6 6 0 6 6 T _ { 0 } ( x ) - 1 . 1 3 0 3 1 8 T _ { 1 } ( x ) + 0 . 2 7 1 4 9 5 T _ { 2 } ( x ) - 0 . 0 4 4 3 3 7 T _ { 3 } ( x ) } \\ & { \qquad + \ 0 . 0 0 5 4 7 4 T _ { 4 } ( x ) - 0 . 0 0 0 5 4 3 T _ { 5 } ( x ) . } \end{array}
$$

To determine the Chebyshev rational approximation of degree 5 with $n = 3$ and $m \ : = \ : 2$ requires choosing $p _ { 0 } , \ p _ { 1 } , \ p _ { 2 } , \ p _ { 3 } , \ q _ { 1 }$ ，and $q _ { 2 }$ so that for $k = 0 , 1 , 2 , 3 , 4 ,$ and 5, the coefficients of $T _ { k } ( x )$ are zero in the expansion

$$
\tilde { P } _ { 5 } ( x ) [ { \cal T } _ { 0 } ( x ) + q _ { 1 } { \cal T } _ { 1 } ( x ) + q _ { 2 } { \cal T } _ { 2 } ( x ) ] - [ p _ { 0 } { \cal T } _ { 0 } ( x ) + p _ { 1 } { \cal T } _ { 1 } ( x ) + p _ { 2 } { \cal T } _ { 2 } ( x ) + p _ { 3 } { \cal T } _ { 3 } ( x ) ] .
$$

Using the relation (8.18) and collecting terms gives the equations

$$
\begin{array} { r l } & { T _ { 0 } : \quad 1 . 2 6 6 0 6 6 - 0 . 5 6 5 1 5 9 q _ { 1 } + 0 . 1 3 5 7 4 8 5 q _ { 2 } = p _ { 0 } , } \\ & { T _ { 1 } : \quad - 1 . 1 3 0 3 1 8 + 1 . 4 0 1 8 1 4 q _ { 1 } - \quad 0 . 5 8 7 3 2 8 q _ { 2 } = p _ { 1 } , } \\ & { T _ { 2 } : \quad 0 . 2 7 1 4 9 5 - 0 . 5 8 7 3 2 8 q _ { 1 } + \quad 1 . 2 6 8 8 0 3 q _ { 2 } = p _ { 2 } , } \\ & { T _ { 3 } : \quad - 0 . 0 4 4 3 3 7 + 0 . 1 3 8 4 8 5 q _ { 1 } - \quad 0 . 5 6 5 4 3 1 q _ { 2 } = p _ { 3 } , } \\ & { T _ { 4 } : \quad 0 . 0 0 5 4 7 4 - 0 . 0 2 2 4 4 0 q _ { 1 } + \quad 0 . 1 3 5 7 4 8 q _ { 2 } = 0 , } \\ & { T _ { 5 } : \quad - 0 . 0 0 0 5 4 3 + 0 . 0 0 2 7 3 7 q _ { 1 } - \quad 0 . 0 2 2 1 6 9 q _ { 2 } = 0 . } \end{array}
$$

The solution to this system produces the rational function

$$
r _ { T } ( x ) = \frac { 1 . 0 5 5 2 6 5 T _ { 0 } ( x ) - 0 . 6 1 3 0 1 6 T _ { 1 } ( x ) + 0 . 0 7 7 4 7 8 T _ { 2 } ( x ) - 0 . 0 0 4 5 0 6 T _ { 3 } ( x ) } { T _ { 0 } ( x ) + 0 . 3 7 8 3 3 1 T _ { 1 } ( x ) + 0 . 0 2 2 2 1 6 T _ { 2 } ( x ) } .
$$

We found at the beginning of Section 8.3 that

$$
T _ { 0 } ( x ) = 1 , T _ { 1 } ( x ) = x , T _ { 2 } ( x ) = 2 x ^ { 2 } - 1 , T _ { 3 } ( x ) = 4 x ^ { 3 } - 3 x .
$$

Using these to convert to an expression involving powers of $x$ gives

$$
r _ { T } ( x ) = \frac { 0 . 9 7 7 7 8 7 - 0 . 5 9 9 4 9 9 x + 0 . 1 5 4 9 5 6 x ^ { 2 } - 0 . 0 1 8 0 2 2 x ^ { 3 } } { 0 . 9 7 7 7 8 4 + 0 . 3 7 8 3 3 1 x + 0 . 0 4 4 4 3 2 x ^ { 2 } } .
$$

Table 8.11 lists values of $r _ { T } ( x )$ and, for comparison purposes,the values of $r ( x )$ obtained in Example 1. Note thatthe approximation given by r(x) is superior to that ofrr(x) for x = 0.2 and O.4,but that the maximum error for $r ( x )$ is $6 . 3 3 \times 1 0 ^ { - 5 }$ compared to $9 . 1 3 \times 1 0 ^ { - 6 }$ for $r _ { T } ( x )$

# Table 8.11

<table><tr><td>X</td><td>e-x</td><td>r(x）</td><td>le-x-r(x）</td><td>rr(x）</td><td>le-x-rr(x)l</td></tr><tr><td>0.2</td><td>0.81873075</td><td>0.81873075</td><td>7.55 × 10-9</td><td>0.81872510</td><td>5.66 × 10-6</td></tr><tr><td>0.4</td><td>0.67032005</td><td>0.67031963</td><td>4.11 × 10-7</td><td>0.67031310</td><td>6.95 ×10-6</td></tr><tr><td>0.6</td><td>0.54881164</td><td>0.54880763</td><td>4.00 × 10-6</td><td>0.54881292</td><td>1.28 × 10-6</td></tr><tr><td>0.8</td><td>0.44932896</td><td>0.44930966</td><td>1.93 × 10-5</td><td>0.44933809</td><td>9.13 × 10-6</td></tr><tr><td>1.0</td><td>0.36787944</td><td>0.36781609</td><td>6.33 × 10-5</td><td>0.36787155</td><td>7.89 × 10-6</td></tr></table>

The Chebyshev approximation can be generated using Algorithm 8.2.

# Chebyshev Rational Approximation

To obtain the rational approximation

$$
r _ { T } ( x ) = \frac { \sum _ { k = 0 } ^ { n } p _ { k } T _ { k } ( x ) } { \sum _ { k = 0 } ^ { m } q _ { k } T _ { k } ( x ) }
$$

for a given function $f ( x )$ ：

INPUT nonnegative integers $m$ and $\pmb { n }$

OUTPUT coefficients qo,q1,...,qm and po, P1,..., Pn:

Step 1 Set $N = m + n$

Step 2 Set $a _ { 0 } = \frac { 2 } { \pi } \int _ { 0 } ^ { \pi } f ( \cos \theta ) d \theta ;$ (The coefficient $a _ { 0 }$ is doubled for computational efficiency.) $\operatorname { F o r } k = 1 , 2 , \dots , N + m$ set

$$
a _ { k } = { \frac { 2 } { \pi } } \int _ { 0 } ^ { \pi } f ( \cos \theta ) \cos k \theta d \theta .
$$

(The integrals can be evaluated using a numerical integration procedure or the coefficients can be input directly.)

Step 3 Set $q _ { 0 } = 1$

Step 4 For $i = 0 , 1 , \ldots , N$ do Steps 5-9. (Set up a linear system with matrix B.)

$$
\begin{array} { r l } { S t e p 5 } & { \mathrm { F o r ~ } j = 0 , 1 , \dotsc , i } \\ & { \qquad \mathrm { i f ~ } j \leq n \mathrm { : t h e n ~ s e t ~ } b _ { i , j } = 0 . } \end{array}
$$

Step 6 If $i \leq n$ then set $b _ { i , i } = 1$

Step 7Fo $\begin{array} { r } { \mathbf { r } j = i + 1 , i + 2 , \ldots , n \operatorname { s e t } b _ { i , j } = 0 . } \end{array}$

Step 8For $j = n + 1 , n + 2 , . . . , N$

$$
\begin{array} { c } { { \mathrm { i f } i \neq 0 \mathrm { t h e n } \mathrm { s e t } b _ { i , j } = - \frac 1 2 ( a _ { i + j - n } + a _ { | i - j + n | } ) } } \\ { { \mathrm { e l s e s e t } b _ { i , j } = - \frac 1 2 a _ { j - n } . } } \end{array}
$$

Step 9If $i \neq 0$ then set $b _ { i , N + 1 } = a _ { i }$ else set $\begin{array} { r } { b _ { i , N + 1 } = \frac { 1 } { 2 } a _ { i } } \end{array}$

(Steps 10-2l solve the linear system using partial pivoting.)

Step 10 For $i = n + 1 , n + 2 , \dots , N - 1$ do Steps 11-17.

Step 11 Let $k$ be the smallest integer with $i \le k \le N$ and $| b _ { k , i } | = \operatorname* { m a x } _ { i \leq j \leq N } | b _ { j , i } |$ .(Find pivot element.)

Step 12 If $b _ { k , i } = 0$ then OUTPUT ("The system is singular"); STOP.

Step 13 If $k \neq i$ then (Interchange row $i$ and row $k$ ） for $j = i , i + 1 , \dots , N + 1$ set

$$
\begin{array} { c } { b _ { C O P Y } = b _ { i , j } ; } \\ { b _ { i , j } = b _ { k , j } ; } \\ { b _ { k , j } = b _ { C O P Y } . } \end{array}
$$

Step 14 For $j = i + 1 , i + 2 , \dots , N$ do Steps 15-17. (Perform elimination.)

Step 15 Set $x m = \frac { b _ { j , i } } { b _ { i , i } }$

$$
\begin{array} { r l } { { 5 t e p \ 1 6 } } & { { } { \mathrm { F o r \ } k = i + 1 , i + 2 , \ldots , N + 1 } } \\ { { } } & { { } { \mathrm { s e t } \ b _ { j , k } = b _ { j , k } - x m \cdot b _ { i , k } . } } \end{array}
$$

Step 17 Set $b _ { j , i } = 0$

Step 18 If $b _ { N , N } = 0$ then OUTPUT("The system is singular"); STOP.

Step 19If $m > 0$ then set $q _ { m } = { \frac { b _ { N , N + 1 } } { b _ { N , N } } }$ (Start backward substitution.)

$$
{ \mathrm { } ? } p 2 O \quad { \mathrm { F o r } } i = N - 1 , N - 2 , \ldots , n + 1 { \mathrm { ~ s e t ~ } } q _ { i - n } = { \frac { b _ { i , N + 1 } - \sum _ { j = i + 1 } ^ { N } b _ { i , j } q _ { j - n } } { b _ { i , i } } } .
$$

Step 21 For $\begin{array} { r } { i = n , n - 1 , \ldots , 0 \mathrm { ~ s e t ~ } p _ { i } = b _ { i , N + 1 } - \sum _ { j = n + 1 } ^ { N } b _ { i , j } q _ { j - n } . } \end{array}$

Step 22OUTPUT $( q _ { 0 } , q _ { 1 } , . . . , q _ { m } , p _ { 0 } , p _ { 1 } , . . . , p _ { n } )$ STOP.(The procedure was successful.)

We can obtain both the Chebyshev series expansion and the Chebyshev rational ap-proximation using a CAS. For example, to make the Chebyshev polynomials accessible to Maple, we enter the command

>with(orthopoly,T);

The procedure to compute the Chebyshev series as an approximation is >g:=numapprox[chebyshev](exp(-x),x,O.Oo0001）;

where the third parameter specifies the required accuracy. The result is $g : = 1 . 2 6 6 0 6 5 8 7 8 T ( 0 , x ) - 1 . 1 3 0 3 1 8 2 0 8 T ( 1 , x ) + . 2 7 1 4 9 5 3 3 9 6 T ( 2 , x )$ $- . 0 4 4 3 3 6 8 4 9 8 5 T ( 3 , x ) + . 0 0 5 4 7 4 2 4 0 4 4 2 T ( 4 , x )$ $- . 0 0 0 5 4 2 9 2 6 3 1 1 9 T ( 5 , x ) + . 0 0 0 0 4 4 9 7 7 3 2 2 9 6 T ( 6 , x )$ - .3198436462 10-5 T(7,x)

and we can evaluate $g ( 0 . 8 )$ using >evalf(subs $( \mathbf { x } { = } 0 . 8 , \mathbf { g } ) .$ ； to obtain .4493288893.

To get the Chebyshev rational approximation we start again with the Chebyshev series

>restart;   
>numapprox[chebyshev](exp(-x),x,O.Oo0001);

as before and then enter

resulting in

$$
\begin{array} { r } { g : = ( 1 . 0 5 0 5 3 1 1 6 6 T ( 0 , x ) - . 6 0 1 6 3 6 2 1 2 2 T ( 1 , x ) + . 0 7 4 1 7 8 9 7 1 4 9 T ( 2 , x ) } \end{array}
$$

Since we have cleared Maple's memory, we need to reenter the command

>with(orthopoly,T);

so we can evaluate $g ( 0 . 8 )$ by >evalf(subs $( \mathbf { x } { = } 0 . 8 , \mathbf { g } )$ ）；

to get .4493317579.

The Chebyshev method does not produce the best rational function approximation in the sense of the approximation whose maximum approximation error is minimal. The method can, however, be used as a starting point for an interative method known as the second Remes' algorithm that converges to the best approximation.A discussion of the techniques involved with this procedure and an improvement on this algorithm can be found in [RR,pp.292-305],or in [Po,pp. 90-92].

# ExercIse Set 8.4

1.Determine all degre 2 Padé approximations for $f ( x ) = e ^ { 2 x }$ . Compare the results at $x _ { i } = 0 . 2 i$ ， for $i = 1$ ,2,3,4,5, with the actual values $f ( { \pmb x } _ { i } )$

2.Determine all degree 3 Padé approximations for $f ( x ) = x \ln ( x + 1 )$ . Compare the results at $x _ { i } = 0 . 2 i$ ,for $i = 1 , 2 , 3 , 4 , 5$ , with the actual values $f ( x _ { i } )$

3.Determine the Padé approximation of degree 5 with $n = 2$ and $m = 3$ for $f ( x ) = e ^ { x }$ . Compare the results at $x _ { i } = 0 . 2 i$ ,for $i = 1$ ,2,3,4,5,with those from the fifth Maclaurin polynomial.

4. Repeat Exercise 3 using instead the Padé approximation of degree 5 with $n = 3$ and $m = 2$ Compare the results at each $x _ { i }$ with those computed in Exercise 3.

5.Determine the Padé approximation of degree 6 with $n = m = 3$ for $f ( x ) = \sin { x }$ . Compare the results at $x _ { i } = 0 . 1 i$ ,for $i = 0 , 1 , . . . , 5 ,$ ,with the exact results and with the results of the sixth Maclaurin polynomial.

6. Determine the Padé approximations of degree 6 with (a) $n = 2 , m = 4$ and (b) $n = 4$ ， $m = 2$ for $f ( x ) = \sin { x }$ . Compare the results at each $x _ { i }$ to those obtained in Exercise 5.

7.Table 8.1O lists results of the Padé approximation of degree 5 with $n = 3$ and $m = 2$ , the fifth Maclaurin polynomial,and the exact values of $f ( x ) = e ^ { - x }$ when ${ x } _ { i } = 0 . 2 i$ ,for $i = 1$ ,2,3, 4,and 5. Compare these results with those produced from the other Padé approximations of degree five.

a $\begin{array} { r } { n = 0 , m = 5 } \\ { n = 3 , m = 2 } \end{array}$ $\begin{array} { r } { \pmb { \mathrm { b . } } \quad n = 1 , m = 4 } \\ { \pmb { \mathrm { d . } } \quad n = 4 , m = 1 } \end{array}$

8.Express the following rational functions in continued-fraction form:

$$
\begin{array} { l l } { { \displaystyle \frac { x ^ { 2 } + 3 x + 2 } { x ^ { 2 } - x + 1 } } } & { { \mathrm { ~ b . ~ } \quad \displaystyle \frac { 4 x ^ { 2 } + 3 x - 7 } { 2 x ^ { 3 } + x ^ { 2 } - x + 5 } } } \\ { { \displaystyle \frac { 2 x ^ { 3 } - 3 x ^ { 2 } + 4 x - 5 } { x ^ { 2 } + 2 x + 4 } } } & { { \mathrm { ~ d . ~ } \quad \displaystyle \frac { 2 x ^ { 3 } + x ^ { 2 } - x + 3 } { 3 x ^ { 3 } + 2 x ^ { 2 } - x + 1 } } } \end{array}
$$

9. Find all the Chebyshev rational approximations of degree 2 for $f ( x ) = e ^ { - x }$ . Which give the best approximations to $f ( x ) = e ^ { - x }$ at ${ x = 0 . 2 5 }$ , 0.5, and 1?

10. Find all the Chebyshev rational approximations of degree 3 for $f ( x ) = \cos x$ . Which give the best approximations to $f ( x ) = \cos x$ at $x = \pi / 4$ and $\pi / 3 ?$

11. Find the Chebyshev rational approximation of degree 4 with $n = m = 2$ for $f ( x ) = \sin { x }$ Compare the results at ${ x _ { i } } = 0 . 1 i$ ,for $i = 0$ ,1,2, 3,4,5,from this approximation with those obtained in Exercise 5 using a sixth-degree Padé approximation.

12.Find all Chebyshev rational approximations of degree 5 for $f ( x ) = e ^ { x }$ .Compare the results at $x _ { i } = 0 . 2 i$ ,for $i = \cdot 1$ ,2, 3,4,5, with those obtained in Exercises 3 and 4.

13. To accurately approximate $f ( x ) = e ^ { x }$ for inclusion in a mathematical library,we first restrict the domain of $f$ . Given a real number $\pmb { x }$ , divide by $\ln { \sqrt { 1 0 } }$ to obtain the relation

$$
x = M \cdot \ln { \sqrt { 1 0 } } + s ,
$$

where $M$ is an integer and $\pmb { \mathscr { s } }$ is a real number satisfying $\textstyle | s | \leq { \frac { 1 } { 2 } } \ln { \sqrt { 1 0 } }$

a.Show that $e ^ { x } = e ^ { s } \cdot 1 0 ^ { M / 2 }$ .

b. Construct a rational function approximation for $e ^ { s }$ using $n = m = 3$ . Estimate the error when $\begin{array} { r } { \mathbf { 0 } \leq | s | \leq { \frac { 1 } { 2 } } \ln { \sqrt { 1 0 } } } \end{array}$   
c. Design an implemcntation of $e ^ { x }$ using the results of part (a) and ${ ( \mathsf { b } ) }$ and the approximations

$$
{ \frac { 1 } { \ln { \sqrt { 1 0 } } } } = 0 . 8 6 8 5 8 8 9 6 3 8 \quad { \mathrm { a n d } } \quad { \sqrt { 1 0 } } = 3 . 1 6 2 2 7 7 6 6 0 .
$$

14.To accurately approximate sin $x$ and cos $x$ for inclusion in a mathematical library,we first restrict their domains. Given a real number $x$ ,divide by $\pi$ to obtain the relation

$$
| x | = M \pi + s , \quad { \mathrm { w h e r e ~ } } M { \mathrm { ~ i s ~ a n ~ i n t e g e r ~ a n d ~ } } | s | \leq { \frac { \pi } { 2 } } .
$$

a. Show that sir $\mathsf { \Pi } ^ { \mathsf { \Pi } } \cdot \mathsf { \Pi } = \mathsf { s g n } ( x ) \cdot ( - 1 ) ^ { M } \cdot \mathsf { s i n } s$   
b. Construct a rational approximation to sin $\pmb { S }$ using $n = m = 4$ .Estimate the error when $0 \le | s | \le \pi / 2$   
c. Design an implementation of sin $x$ using parts (a) and (b).   
d. Repeat part (c) for $\mathtt { c o s } x$ using the fact that cos $\pmb { x } = \sin ( \pmb { x } + \pi / 2 )$

# 8.5Trigonometric Polynomial Approximation

The use of series of sine and cosine functions to represent arbitrary functions had its be-ginnings in the 175Os with the study of the motion of a vibrating string. This problem was considered by Jean d'Alembert and then taken up by the foremost mathematician of the time,Leonhard Euler. But it was Daniel Bernoulli who first advocated the use of the infinite sums of sine and cosines as a solution to the problem, sums that we now know as Fourier series. In the early part of the 19th century, Jean Baptiste Joseph Fourier used these series to study the flow of heat and developed quite a complete theory of the subject.

The first observation in the development of Fourier series is that, for each positive integer $n$ , the set of functions $\{ \phi _ { 0 } , \phi _ { 1 } , \ldots , \phi _ { 2 n - 1 } \}$ , where

$$
\begin{array} { l l l } { \displaystyle \phi _ { 0 } ( \boldsymbol { x } ) = \frac { 1 } { 2 } , } \\ { \displaystyle \phi _ { k } ( \boldsymbol { x } ) = \cos k x , \quad \mathrm { f o r } \mathrm { e a c h } k = 1 , 2 , \ldots , n , } \end{array}
$$

and

$$
\phi _ { n + k } ( x ) = \sin k x , \quad { \mathrm { f o r } } \operatorname { e a c h } k = 1 , 2 , \ldots , n - 1 ,
$$

is an orthogonal set on $[ - \pi , \pi ]$ with respect to $w ( x ) \equiv 1$ . This orthogonality follows from the fact that, for every integer $j$ , the integrals of sin $j x$ and cos $j x$ over $[ - \pi , \pi ]$ are O,and we can rewrite products of sine and cosine functions as sums by using the three trigonometric identities

$$
\begin{array} { c } { \sin t _ { 1 } \sin t _ { 2 } = \displaystyle \frac { 1 } { 2 } [ \cos ( t _ { 1 } - t _ { 2 } ) - \cos ( t _ { 1 } + t _ { 2 } ) ] , } \\ { \cos t _ { 1 } \cos t _ { 2 } = \displaystyle \frac { 1 } { 2 } [ \cos ( t _ { 1 } - t _ { 2 } ) + \cos ( t _ { 1 } + t _ { 2 } ) ] , } \\ { \sin t _ { 1 } \cos t _ { 2 } = \displaystyle \frac { 1 } { 2 } [ \sin ( t _ { 1 } - t _ { 2 } ) + \sin ( t _ { 1 } + t _ { 2 } ) ] . } \end{array}
$$

Let $\mathcal { T } _ { n }$ denote the set of allinear combinations of the functions $\phi _ { 0 } , \phi _ { 1 } , \ldots , \phi _ { 2 n - 1 }$ This set is called the set of trigonometric polynomials of degree less than or equal to $n$ (Some sources also include an additional function in the set, $\phi _ { 2 n } ( x ) = \sin n x .$ ）

For a function $f \in C [ - \pi , \pi ]$ , we want to find the continuous least squares approximation by functions in $\mathcal { T } _ { n }$ in the form

$$
S _ { n } ( x ) = { \frac { a _ { 0 } } { 2 } } + a _ { n } \cos n x + \sum _ { k = 1 } ^ { n - 1 } ( a _ { k } \cos k x + b _ { k } \sin k x ) .
$$

Since the set of functions $\{ \phi _ { 0 } , \phi _ { 1 } , \ldots , \phi _ { 2 n - 1 } \}$ is orthogonal on $[ - \pi , \pi ]$ with respect to $w ( x ) \equiv 1$ , it follows from Theorem 8.6 that the appropriate selection of coefficients is

$$
a _ { k } = { \frac { 1 } { \pi } } \int _ { - \pi } ^ { \pi } f ( x ) \cos k x \ d x , \quad { \mathrm { f o r ~ e a c h ~ } } k = 0 , 1 , 2 , \ldots , n ,
$$

and

$$
b _ { k } = { \frac { 1 } { \pi } } \int _ { - \pi } ^ { \pi } f ( x ) \sin k x d x , \quad { \mathrm { f o r } } \operatorname { e a c h } k = 1 , 2 , \dots , n - 1 .
$$

The limit of $S _ { n } ( x )$ when $n  \infty$ is called the Fourier series of $f$ . Fourier series are used to describe the solution of various ordinary and partial-diferential equations that occur in physical situations.

To determine the trigonometric polynomial from $\mathcal { T } _ { n }$ that approximates

$$
f ( x ) = | x | , \quad { \mathrm { f o r ~ } } - \pi < x < \pi ,
$$

requires finding

$$
\begin{array} { l } { { \displaystyle a _ { 0 } = \frac { 1 } { \pi } \int _ { - \pi } ^ { \pi } \left| x \right| d x = - \frac { 1 } { \pi } \int _ { - \pi } ^ { 0 } x d x + \frac { 1 } { \pi } \int _ { 0 } ^ { \pi } x d x = \frac { 2 } { \pi } \int _ { 0 } ^ { \pi } x d x = \pi , } } \\ { { \displaystyle a _ { k } = \frac { 1 } { \pi } \int _ { - \pi } ^ { \pi } \left| x \right| \cos k x d x = \frac { 2 } { \pi } \int _ { 0 } ^ { \pi } x \cos k x d x = \frac { 2 } { \pi k ^ { 2 } } \left[ ( - 1 ) ^ { k } - 1 \right] , } } \end{array}
$$

for each $k = 1 , 2 , \ldots , n$ ,and

$$
b _ { k } = { \frac { 1 } { \pi } } \int _ { - \pi } ^ { \pi } | x | \sin k x d x = 0 , \quad { \mathrm { f o r } } \operatorname { e a c h } k = 1 , 2 , \dots , n - 1 .
$$

That the $b _ { k } \mathbf { ' s }$ are all O follows from the fact that $g ( x ) = | x | \sin { k x }$ is an odd function for each $k$ ， and the integral of any odd function over any interval of the form $[ \neg a , a ]$ is 0. (See Exercises 13 and 14.） The trigonometric polynomial from $\mathcal { T } _ { n }$ approximating $f$ is,

therefore,

$$
S _ { n } ( x ) = { \frac { \pi } { 2 } } + { \frac { 2 } { \pi } } \sum _ { k = 1 } ^ { n } { \frac { ( - 1 ) ^ { k } - 1 } { k ^ { 2 } } } \cos k x .
$$

The first few trigonometric polynomials for $f ( x ) = | x |$ are shown in Figure 8.13.

![](images/2e7a1d05417b3c03a589e069c9f97d2d6a591d05291369b1bdd0a605117c176e.jpg)  
Figure 8.13

The Fourier series for $f$ is

$$
S ( x ) = \operatorname* { l i m } _ { n \to \infty } S _ { n } ( x ) = { \frac { \pi } { 2 } } + { \frac { 2 } { \pi } } \sum _ { k = 1 } ^ { \infty } { \frac { ( - 1 ) ^ { k } - 1 } { k ^ { 2 } } } \cos k x .
$$

Since $| \cos k x | \le 1$ , for every $k$ and $x$ , the series converges, and $S ( x )$ exists for all real numbers $x$ ·

There is a discrete analog that is useful for the discrete least squares approximation and the interpolation of large amounts of data.

Suppose that a collection of $2 m$ paired data points $\{ ( x _ { j } , y _ { j } ) \} _ { j = 0 } ^ { 2 m - 1 }$ is given, with the first elements in the pairs equally partitioning a closed interval. For convenience,we assume that the interval is $[ - \pi , \pi ]$ ,so, as shown in Figure 8.14,

$$
x _ { j } = - \pi + \bigg ( \frac { j } { m } \bigg ) \pi , \quad \mathrm { f o r } \operatorname { e a c h } j = 0 , 1 , \ldots , 2 m - 1 .
$$

If it is not $[ - \pi , \pi ]$ ,a simple linear transformation could be used to translate the data into this form.

![](images/066fe9336c51a61dd197556859bba3db79c264c0b04c535b8a439d51bcb525e3.jpg)  
Figure 8.14

The goal in the discrete case is to determine the trigonometric polynomial $S _ { n } ( x )$ in $\mathcal { T } _ { n }$ that will minimize

$$
E ( S _ { n } ) = \sum _ { j = 0 } ^ { 2 m - 1 } [ y _ { j } - S _ { n } ( x _ { j } ) ] ^ { 2 } .
$$

To do this we need to choose the constants $a _ { 0 } , a _ { 1 } , \dots , a _ { n } , b _ { 1 } , b _ { 2 } , \dots , b _ { n - 1 }$ so that

$$
E ( S _ { n } ) = \sum _ { j = 0 } ^ { 2 m - 1 } \left\{ y _ { j } - \left[ { \frac { a _ { 0 } } { 2 } } + a _ { n } \cos n x _ { j } + \sum _ { k = 1 } ^ { n - 1 } ( a _ { k } \cos k x _ { j } + b _ { k } \sin k x _ { j } ) \right] \right\} ^ { 2 }
$$

is a minimum.

The determination of the constants is simplified by the fact that the set $\{ \phi _ { 0 } , \phi _ { 1 } , . . . \ ,$ $\phi _ { 2 n - 1 } \}$ is orthogonal withrespect tosummation over theequallyspaced points $\{ x _ { j } \} _ { j = 0 } ^ { 2 m - 1 }$ in $[ - \pi , \pi ]$ . By this we mean that for each $k \neq l$ ，

$$
\sum _ { j = 0 } ^ { 2 m - 1 } \phi _ { k } ( x _ { j } ) \phi _ { l } ( x _ { j } ) = 0 .
$$

To show this orthogonality, we use the following lemma.

If the integer $r$ is not a multiple of $2 m$ ,then

$$
\sum _ { j = 0 } ^ { 2 m - 1 } \cos r x _ { j } = 0 \quad { \mathrm { a n d } } \quad \sum _ { j = 0 } ^ { 2 m - 1 } \sin r x _ { j } = 0 .
$$

Moreover, if $\boldsymbol { r }$ is not a multiple of $_ { m }$ , then

$$
\sum _ { j = 0 } ^ { 2 m - 1 } ( \cos r x _ { j } ) ^ { 2 } = m \quad { \mathrm { a n d } } \quad \sum _ { j = 0 } ^ { 2 m - 1 } ( \sin r x _ { j } ) ^ { 2 } = m .
$$

Proof Euler's Formula states that if $i ^ { 2 } = - 1$ , then for every real number $z$ , we have

$$
e ^ { i z } = \cos z + i \sin z .
$$

Applying this result gives

$$
\sum _ { j = 0 } ^ { 2 m - 1 } \cos r x _ { j } + i \sum _ { j = 0 } ^ { 2 m - 1 } \sin r x _ { j } = \sum _ { j = 0 } ^ { 2 m - 1 } \left( \cos r x _ { j } + i \sin r x _ { j } \right) = \sum _ { j = 0 } ^ { 2 m - 1 } e ^ { i r x _ { j } } .
$$

But

$$
e ^ { i r x _ { j } } = e ^ { i r ( - \pi + j \pi / m ) } = e ^ { - i r \pi } \cdot e ^ { i r j \pi / m } ,
$$

so

$$
\sum _ { j = 0 } ^ { 2 m - 1 } \cos r x _ { j } + i \sum _ { j = 0 } ^ { 2 m - 1 } \sin r x _ { j } = e ^ { - i r \pi } \sum _ { j = 0 } ^ { 2 m - 1 } e ^ { i r j \pi / m } .
$$

Since $\sum _ { j = 0 } ^ { 2 m - 1 } e ^ { i r j \pi / m }$ i $e ^ { i r \pi / m } \neq 1$ we have

$$
\sum _ { j = 0 } ^ { 2 m - 1 } e ^ { i r j \pi / m } = \frac { 1 - ( e ^ { i r \pi / m } ) ^ { 2 m } } { 1 - e ^ { i r \pi / m } } = \frac { 1 - e ^ { 2 i r \pi } } { 1 - e ^ { i r \pi / m } } .
$$

But $e ^ { 2 i r \pi } = \cos 2 r \pi + i \sin 2 r \pi = 1$ ， $\mathsf { i } 0 \ 1 - e ^ { 2 i r \pi } = 0$ and

$$
\sum _ { j = 0 } ^ { 2 m - 1 } \cos r x _ { j } + i \sum _ { j = 0 } ^ { 2 m - 1 } \sin r x _ { j } = e ^ { - i r \pi } \sum _ { j = 0 } ^ { 2 m - 1 } e ^ { i r j \pi / m } = 0 .
$$

This implies that both

$$
\sum _ { j = 0 } ^ { 2 m - 1 } \cos r x _ { j } = 0 \quad { \mathrm { a n d } } \quad \sum _ { j = 0 } ^ { 2 m - 1 } \sin r x _ { j } = 0 .
$$

f $r$ is not a multiple of $m$ , these sums imply that

$$
\begin{array} { l } { { \displaystyle \sum _ { j = 0 } ^ { 2 m - 1 } ( \cos r x _ { j } ) ^ { 2 } = \sum _ { j = 0 } ^ { 2 m - 1 } \frac { 1 } { 2 } \left( 1 + \cos 2 r x _ { j } \right) } } \\ { { \displaystyle \qquad = \frac { 1 } { 2 } \left[ \sum _ { j = 0 } ^ { 2 m - 1 } 1 + \sum _ { j = 0 } ^ { 2 m - 1 } \cos 2 r x _ { j } \right] = \frac { 1 } { 2 } ( 2 m + 0 ) = m } } \end{array}
$$

and, similarly, that

$$
\sum _ { j = 0 } ^ { 2 m - 1 } ( \sin r x _ { j } ) ^ { 2 } = m .
$$

We can now show the orthogonality stated in (8.22). Consider, for example, the case

$$
\sum _ { j = 0 } ^ { 2 m - 1 } \phi _ { k } ( x _ { j } ) \phi _ { n + l } ( x _ { j } ) = \sum _ { j = 0 } ^ { 2 m - 1 } ( \cos k x _ { j } ) ( \sin l x _ { j } ) .
$$

Since

$$
\cos k x _ { j } \sin l x _ { j } = { \frac { 1 } { 2 } } [ \sin ( l + k ) x _ { j } + \sin ( l - k ) x _ { j } ]
$$

and $( l + k )$ and $( l - k )$ are both integers that are not multiples of $2 m$ , Lemma 8.12 implies that

$$
\sum _ { j = 0 } ^ { 2 m - 1 } ( \cos k x _ { j } ) ( \sin l x _ { j } ) = \frac { 1 } { 2 } \left[ \sum _ { j = 0 } ^ { 2 m - 1 } \sin ( l + k ) x _ { j } + \sum _ { j = 0 } ^ { 2 m - 1 } \sin ( l - k ) x _ { j } \right] = \frac { 1 } { 2 } \left( 0 + 0 \right) =
$$

This technique is used to show that the orthogonality condition is satisfied for any pair of the functions and is used to produce the following result.

# Theorem 8.13

The constants in the summation

$$
S _ { n } ( x ) = { \frac { a _ { 0 } } { 2 } } + a _ { n } \cos n x + \sum _ { k = 1 } ^ { n - 1 } ( a _ { k } \cos k x + b _ { k } \sin k x )
$$

that minimize the least squares sum

$$
E ( a _ { 0 } , \dots , a _ { n } , b _ { 1 } , \dots , b _ { n - 1 } ) = \sum _ { j = 0 } ^ { 2 m - 1 } ( y _ { j } - S _ { n } ( x _ { j } ) ) ^ { 2 }
$$

are

$$
a _ { k } = \frac { 1 } { m } \sum _ { j = 0 } ^ { 2 m - 1 } y _ { j } \cos k x _ { j } , \quad \mathrm { f o r } \operatorname { e a c h } k = 0 , 1 , \dots , n ,
$$

and

$$
b _ { k } = \frac { 1 } { m } \sum _ { j = 0 } ^ { 2 m - 1 } y _ { j } \sin k x _ { j } , \quad \mathrm { f o r } \operatorname { e a c h } k = 1 , 2 , \dots , n - 1 .
$$

The theorem is proved by setting the partial derivatives of $E$ with respect to the $\boldsymbol { a } _ { k } { \mathbf { \bar { s } } }$ and the $b _ { k } \mathbf { ' s }$ to zero,as was done in Sections 8.1 and 8.2,and applying the orthogonality to simplify the equations. For example,

$$
0 = \frac { \partial E } { \partial b _ { k } } = 2 \sum _ { j = 0 } ^ { 2 m - 1 } [ y _ { j } - S _ { n } ( x _ { j } ) ] ( - \sin k x _ { j } ) ,
$$

So

$$
\begin{array} { l } { { \displaystyle 0 = \sum _ { j = 0 } ^ { \infty n - 1 } y _ { j } \sin k x _ { j } - \sum _ { j = 0 } ^ { \infty n } S _ { n } ( x _ { j } ) \sin k x _ { j } } } \\ { { \displaystyle ~ = \sum _ { j = 0 } ^ { 2 m - 1 } y _ { j } \sin k x _ { j } - \frac { a _ { 0 } } { 2 } \sum _ { j = 0 } ^ { 2 m - 1 } \sin k x _ { j } - a _ { n } \sum _ { j = 0 } ^ { 2 m - 1 } \sin k x _ { j } \cos n x _ { j } } } \\ { { \displaystyle ~ - \sum _ { l = 1 } ^ { n - 1 } a _ { l } \sum _ { j = 0 } ^ { 2 m - 1 } \sin k x _ { j } \cos l x _ { j } - \sum _ { l = 1 } ^ { n - 1 } b _ { l } \sum _ { j = 0 } ^ { 2 m - 1 } \sin k x _ { j } \sin l x _ { j } - b _ { k } \sum _ { j = 0 } ^ { 2 m - 1 } ( \sin k x _ { j } ) ^ { 2 } } . } \end{array}
$$

The orthogonality implies that all butthe first and last sums on the right side are zero, and Lemma 8.12 states the final sum is $m$ . Hence

$$
b _ { k } = \frac { 1 } { m } \sum _ { j = 0 } ^ { 2 m - 1 } y _ { j } \sin k x _ { j } .
$$

# EXAMPLE 2

Let $f ( x ) = x ^ { 4 } - 3 x ^ { 3 } + 2 x ^ { 2 } - \tan { x ( x - 2 ) }$ . To find the discrete least squares approximation $S _ { 3 } ( x )$ for the data $\{ ( x _ { j } , y _ { j } ) \} _ { j = 0 } ^ { 9 }$ , where $x _ { j } = j / 5$ and $y _ { j } = f ( \pmb { x } _ { j } )$ ,requires a transformation from [0, 2] to $[ - \pi , \pi ]$ . This linear transformation is

$$
z _ { j } = \pi ( x _ { j } - 1 ) ,
$$

and the transformed data is of the form

$$
\left\{ \left( z _ { j } , f \left( 1 + \frac { z _ { j } } { \pi } \right) \right) \right\} _ { j = 0 } ^ { 9 } .
$$

The least squares trigonometric polynomial is, consequently,

$$
S _ { 3 } ( z ) = \left[ { \frac { a _ { 0 } } { 2 } } + a _ { 3 } \cos 3 z + \sum _ { k = 1 } ^ { 2 } ( a _ { k } \cos k z + b _ { k } \sin k z ) \right] ,
$$

where

$$
a _ { k } = \frac { 1 } { 5 } \sum _ { j = 0 } ^ { 9 } f \left( 1 + \frac { z _ { j } } { \pi } \right) \cos k z _ { j } , \quad \mathrm { f o r } \ k = 0 , 1 , 2 , 3 ,
$$

and

$$
b _ { k } = \frac { 1 } { 5 } \sum _ { j = 0 } ^ { 9 } f \left( 1 + \frac { z _ { j } } { \pi } \right) \sin k z _ { j } , \quad \mathrm { f o r } \ k = 1 , 2 .
$$

Evaluating these sums produces the approximation

$$
S _ { 3 } ( z ) = 0 . 7 6 2 0 1 + 0 . 7 7 1 7 7 \cos z + 0 . 0 1 7 4 2 3 \cos 2 z + 0 . 0 0 6 5 6 7 3 \cos 3 z
$$

$$
- 0 . 3 8 6 7 6 \sin z + 0 . 0 4 7 8 0 6 \sin 2 z ,
$$

Table 8.12

<table><tr><td>X</td><td>f(x）</td><td>S(x) If(x)-S(x)1</td></tr><tr><td>0.125</td><td>0.26440</td><td>0.24060 2.38 × 10-2</td></tr><tr><td>0.375</td><td>0.84081</td><td>0.85154 1.07 × 10-2</td></tr><tr><td>0.625</td><td>1.36150</td><td>1.36248 9.74 × 10-4</td></tr><tr><td>0.875</td><td>1.61282</td><td>1.60406 8.75 × 10-3</td></tr><tr><td>1.125</td><td>1.36672</td><td>1.37566 8.94 × 10-3</td></tr><tr><td>1.375</td><td>0.71697</td><td>0.71545 1.52 × 10-3</td></tr><tr><td>1.625</td><td>0.07909</td><td>0.06929 9.80 × 10-3</td></tr><tr><td>1.875</td><td>-0.14576</td><td>-0.12302 2.27 ×10-2</td></tr></table>

and converting back to the variable $\pmb { x }$ gives

$S _ { 3 } ( x ) = 0 . 7 6 2 0 1 + 0 . 7 7 1 7 7 \cos \pi ( x - 1 ) + 0 . 0 1 7 4 2 3 \cos 2 \pi ( x - 1 )$ $+ 0 . 0 0 6 5 6 7 3 \cos 3 \pi ( x - 1 ) - 0 . 3 8 6 7 6 \sin \pi ( x - 1 ) + 0 . 0 4 7 8 0 6 \sin 2 \pi ( x - 1 ) .$

Table 8.12 lists values of $f ( x )$ and $S _ { 3 } ( x )$

# Exercise set 8.5

1.Find the continuous least squares trigonometric polynomial $\mathcal { S } _ { 2 } ( x )$ for $f ( x ) = x ^ { 2 }$ on $[ - \pi , \pi ]$

2.Find the continuous least squares trigonometric polynomial $S _ { n } ( x )$ for $f ( x ) = x$ on $[ - \pi , \pi ]$ ·

3.Find the continuous least squares trigonometric polynomial $\mathbb { S } _ { 3 } ( x )$ for $f ( x ) = e ^ { x }$ on $[ - \pi , \pi ]$

4.Find the general continuous least squares trigonometric polynomial $S _ { n } ( x )$ for $f ( x ) = e ^ { x }$ on $[ - \pi , \pi ]$

5.Find the general continuous least squares trigonometric polynomial $S _ { n } ( x )$ for

$$
f ( x ) = { \left\{ \begin{array} { l l } { 0 , } & { { \mathrm { i f } } - \pi < x \leq 0 , } \\ { 1 , } & { { \mathrm { i f } } \ 0 < x < \pi . } \end{array} \right. }
$$

6.Find the general continuous least squares trigonometric polynomial $S _ { n } ( x )$ in for

$$
f ( x ) = { \left\{ \begin{array} { l l } { - 1 , } & { { \mathrm { i f ~ } } - \pi < x < 0 . } \\ { 1 , } & { { \mathrm { i f ~ } } 0 \leq x \leq \pi . } \end{array} \right. }
$$

7.Determine the discrete least squares trigonometric polynomial $S _ { n } ( x )$ on the interval $[ - \pi , \pi ]$ for the following functions, using the given values of $m$ and $\pmb { n }$ ：

$$
\begin{array} { l } { f ( x ) = \cos 2 x , \quad m = 4 , n = 2 } \\ { f ( x ) = \cos 3 x , \quad m = 4 , n = 2 } \\ { f ( x ) = \sin \frac 1 2 x + 2 \cos \frac 1 3 x , \quad m = 6 , n = 3 } \\ { f ( x ) = x ^ { 2 } \cos x , \quad m = 6 , n = 3 } \end{array}
$$

8.Compute the error $E ( S _ { n } )$ for each of the functions in Exercise 7.

9.Determine the discrete least squares trigonometric polynomial ${ \pmb S } _ { 3 } ( { \pmb x } )$ ,using $m = 4$ for $f ( x ) =$ $e ^ { x }$ cos $\pmb { 2 x }$ on the interval $[ - \pi , \pi ]$ . Compute the error $E ( S _ { 3 } )$

10. Repeat Exercise 9 using $m = 8$ . Compare the values of the approximating polynomials with the values of $f$ at the points $\xi _ { j } = - \pi + 0 . 2 j \pi$ ,for $0 \leq j \leq 1 0$ .Which approximation is better?

11. Let $f ( x ) = 2$ tan $\scriptstyle x - s e c 2 x$ ,for $2 \leq x \leq 4$ . Determine the discrete least squares trigonometric polynomials ${ \pmb S } _ { n } ( x )$ , using the values of $\pmb { n }$ and $\pmb { m }$ as follows,and compute the error in each case.

a. $n = 3 , \quad m = 6$ $\ b _ { \bullet } \quad n = 4 , \quad m = 6$

12. a.Determine the discrete least squares trigonometric polynomial $\pmb { S _ { 4 } } ( \pmb { x } )$ ,using $m = 1 6$ ,for $f ( x ) = x ^ { 2 }$ sin x on the interval [0, 1]. $\mathbf { b } _ { \bullet }$ Compute $\int _ { 0 } ^ { 1 } S _ { 4 } ( x ) d x$ c. Compare the integral in part (b) to $\textstyle \int _ { 0 } ^ { 1 } x ^ { 2 } \sin x d x$

13.Show that for any continuous odd function $f$ defined on the interval $[ - a , a ]$ ，we have $\textstyle { \int _ { - a } ^ { a } f ( x ) d x = 0 }$

14. Show that for any continuous even function $f$ defined on the interval $[ - a , a ]$ ，we have $\textstyle { \int _ { - a } ^ { a } f ( x ) d x = 2 \int _ { 0 } ^ { a } f ( x ) d x }$

15.Show that the functions $\phi _ { 0 } ( x ) = 1 / 2 , \phi _ { 1 } ( x ) = \cos x , \ldots , \phi _ { n } ( x ) = \cos n x , \phi _ { n + 1 } ( x ) = \sin x ,$ … $\phi _ { 2 n - 1 } ( x ) = \sin ( n - 1 ) x$ are orthogonal on $[ - \pi , \pi ]$ with respect to $w ( x ) \equiv 1$

16. In Example 1 the Fourier series was determined for $f ( x ) = | x |$ . Use this series and the assumption that it represents $f$ at zero to find the value of the convergent infinite series $\textstyle \sum _ { k = 0 } ^ { \infty } ( 1 / ( 2 k + 1 ) ^ { 2 } )$ ·

# 8.6 Fast Fourier Transforms

In the second half of Section 8.5, we determined the form of the discrete least squares polynomialof degree n on he $_ { 2 m - 1 }$ data points $\{ ( x _ { j } , y _ { j } ) \} _ { j = 0 } ^ { 2 m - 1 }$ ， where $x _ { j } = - \pi + ( j / m ) \pi ,$ for each $j = 0 , 1 , \ldots , 2 m - 1$

The interpolatory rigonometric polynomial in $\mathcal { T } _ { m }$ on these $2 m$ data points is almost the same as the least squares polynomial. This is because the least squares trigonometric polynomial minimizes the error term

$$
E ( S _ { m } ) = \sum _ { j = 0 } ^ { 2 m - 1 } \left( y _ { j } - S _ { m } ( x _ { j } ) \right) ^ { 2 } ,
$$

and for the interpolatory trigonometric polynomial,this error is O, hence minimized, when the $S _ { m } ( x _ { j } ) = y _ { j }$ , for each $j = 0 , 1 , \ldots , 2 m - 1 .$ A modification is needed to the form of the polynomial, however, if we want the coefficients to assume the same form as in the least squares case. In Lemma 8.12 we found that if $r$ is not a multiple of $m$ ,then

$$
\sum _ { j = 0 } ^ { 2 m - 1 } ( \cos r x _ { j } ) ^ { 2 } = m .
$$

Interpolation requires computing instead

$$
\sum _ { j = 0 } ^ { 2 m - 1 } ( \cos m x _ { j } ) ^ { 2 } ,
$$

which (see Exercise 8) has the value $2 m$ . This requires the interpolatory polynomial to be written as

$$
S _ { m } ( x ) = { \frac { a _ { 0 } + a _ { m } \cos { m x } } { 2 } } + \sum _ { k = 1 } ^ { m - 1 } ( a _ { k } \cos { k x } + b _ { k } \sin { k x } ) ,
$$

if we want the form of the constants $a _ { k }$ and $b _ { k }$ to agree with those of the discrete least squares polynomial; that is, where

$$
a _ { k } = { \frac { 1 } { m } } \sum _ { j = 0 } ^ { 2 m - 1 } y _ { j } \cos k x _ { j } , \quad { \mathrm { f o r } } \operatorname { e a c h } k = 0 , 1 , \dots , m ,
$$

and

$$
b _ { k } = \frac { 1 } { m } \sum _ { j = 0 } ^ { 2 m - 1 } y _ { j } \sin k x _ { j } \quad \mathrm { f o r } \operatorname { e a c h } k = 1 , 2 , \dots , m - 1 .
$$

The interpolation of large amounts of equally spaced data by trigonometric polynomials can produce very accurate results. It is the appropriate approximation technique in areas involving digital filters,antenna field patterns,quantum mechanics, optics,and in numerous simulation problems.Until the middle of the 1960s,however, the method had not been extensively applied due to the number of arithmetic calculations required for the determination of the constants in the approximation. The interpolation of $2 m$ data points by the direct-calculation technique requires approximately $( 2 m ) ^ { 2 }$ multiplications and $( 2 m ) ^ { 2 }$ additions. The approximation of many thousands of data points is not unusual in areas requiring trigonometric interpolation, so the direct methods for evaluating the constants require multiplication and addition operations numbering in the millions.The roundoff error associated with this number of calculations generally dominates the approximation.

In 1965 a paper by J. W Cooley and J. W Tukey in the journal Mathematics of Com-putation [CT] described a diferent method of calculating the constants in the interpolating trigonometric polynomial. This method requires only $O ( m \log _ { 2 } m )$ multiplications and $O ( m \log _ { 2 } m )$ additions,provided m is chosen in an appropriate manner. For a problem with thousands of data points, this reduces the number of calculations from millions to thousands. The method had actually been discovered a number of years before the Cooley-Tukey paper appeared but had gone largely unnoticed. ([Brigh, pp. 8-9], contains a short, but interesting,historical summary of the method.)

The method described by Cooley and Tukey is known either as the Cooley-Tukey algorithm or the fast Fourier transform (FFT) algorithm and has led to a revolution in the use of interpolatory trigonometric polynomials. The method consists of organizing the problem so that the number of data points being used can be easily factored, particularly into powers of two.

Instead of directly evaluating the constants $a _ { k }$ and $b _ { k }$ , the fast Fourier transform procedure computes the complex coefficients $c _ { k }$ in

$$
\frac { 1 } { m } \sum _ { k = 0 } ^ { 2 m - 1 } c _ { k } e ^ { i k x } ,
$$

where

$$
c _ { k } = \sum _ { j = 0 } ^ { 2 m - 1 } y _ { j } e ^ { i k \pi j / m } , \quad { \mathrm { f o r } } \operatorname { e a c h } k = 0 , 1 , \dots , 2 m - 1 .
$$

Once the constants $c _ { k }$ have been determined, $a _ { k }$ and $b _ { k }$ can be recovered. To do this we use Euler's Formula,

$$
e ^ { i z } = \cos z + i \sin z .
$$

For each $k = 0 , 1 , \ldots , m .$

$$
\begin{array} { r l } { \displaystyle \frac { 1 } { m } c _ { k } ( - 1 ) ^ { k } = \frac { 1 } { m } c _ { k } e ^ { - i \pi k } = \frac { 1 } { m } \sum _ { j = 0 } ^ { 2 m - 1 } y _ { j } e ^ { i k \pi j / m } e ^ { - i \pi k } = \frac { 1 } { m } \sum _ { j = 0 } ^ { 2 m - 1 } y _ { j } e ^ { i k ( - \pi + ( \pi j / m ) ) } } & { } \\ { = \displaystyle \frac { 1 } { m } \sum _ { j = 0 } ^ { 2 m - 1 } y _ { j } \left( \cos k \left( - \pi + \frac { \pi j } { m } \right) + i \sin k \left( - \pi + \frac { \pi j } { m } \right) \right) } & { } \\ { = \displaystyle \frac { 1 } { m } \sum _ { j = 0 } ^ { 2 m - 1 } y _ { j } ( \cos k x _ { j } + i \sin k x _ { j } ) , } & { } \end{array}
$$

so

$$
a _ { k } + i b _ { k } = { \frac { ( - 1 ) ^ { k } } { m } } c _ { k } .
$$

For notational convenience, $b _ { 0 }$ and $b _ { m }$ are added to the collection,but both are O and do not contribute to the resulting sum.

The operation-reduction feature of the fast Fourier transform results from calculating the coefficients $c _ { k }$ in clusters and uses as a basic relation the fact that for any integer $n$ ，

$$
e ^ { n \pi i } = \cos n \pi + i \sin n \pi = ( - 1 ) ^ { n } .
$$

Suppose $m = 2 ^ { p }$ for some positive integer $p$ .For each $k = 0 , 1 , \ldots , m - 1$ ，

$$
c _ { k } + c _ { m + k } = \sum _ { j = 0 } ^ { 2 m - 1 } y _ { j } e ^ { i k \pi j / m } + \sum _ { j = 0 } ^ { 2 m - 1 } y _ { j } e ^ { i ( m + k ) \pi j / m } = \sum _ { j = 0 } ^ { 2 m - 1 } y _ { j } e ^ { i k \pi j / m } ( 1 + e ^ { \pi i j } ) .
$$

But

$$
1 + e ^ { i \pi j } = { \left\{ \begin{array} { l l } { 2 , } & { { \mathrm { i f ~ } } j { \mathrm { ~ i s ~ e v e n } } , } \\ { 0 , } & { { \mathrm { i f ~ } } j { \mathrm { ~ i s ~ o d d } } , } \end{array} \right. }
$$

so there are only m nonzero terms to be summed. If $j$ is replaced by $2 j$ in the index of the sum, we can write the sum as

$$
c _ { k } + c _ { m + k } = 2 \sum _ { j = 0 } ^ { m - 1 } y _ { 2 j } e ^ { i k \pi ( 2 j ) / m } ;
$$

that is,

$$
c _ { k } + c _ { m + k } = 2 \sum _ { j = 0 } ^ { m - 1 } y _ { 2 j } e ^ { \mathrm { i } k \pi j / ( m / 2 ) } .
$$

In a similar manner,

$$
c _ { k } - c _ { m + k } = 2 e ^ { i k \pi / m } \sum _ { j = 0 } ^ { m - 1 } y _ { 2 j + 1 } e ^ { i k \pi j / ( m / 2 ) } .
$$

Since $c _ { k }$ and $c _ { m + k }$ can both be recovered from Eqs. (8.30) and (8.31), these relations determine all the coefficients $c _ { k }$ .Note also that the sums in Eqs.(8.30) and (8.31) are of the same form as the sum in Eq. (8.28), except that the index m has ben replaced by $m / 2$

There are $2 m$ coefficients $c _ { 0 } , c _ { 1 } , \dots , c _ { 2 m - 1 }$ to be calculated. Using the basic formula (8.28) requires 2m complex multiplications per coefcient, for a total of $( 2 m ) ^ { 2 }$ operations. Equation (8.30) requires m complex multiplications for each $k = 0 , 1 , \ldots , m - 1$ ，and (8.31) requires $m + 1$ complex multiplications for each $k = 0$ ,1,..., $m - 1$ . Using these equations to compute $c _ { 0 } , c _ { 1 } , \dots , c _ { 2 m - 1 }$ reduces the number of complex multiplications from $( 2 m ) ^ { 2 } = 4 m ^ { 2 }$ to

$$
m \cdot m + m ( m + 1 ) = 2 m ^ { 2 } + m .
$$

Since the sums in (8.30) and (8.31) have the same form as the original and $m$ is a power of 2, the reduction technique can be reapplied to the sums in (8.30) and (8.31). Each of these is replaced by two sums from $j = 0$ to $j = ( m / 2 ) - 1$ . This reduces the $2 m ^ { 2 }$ portion of the sum to

$$
2 \left[ { \frac { m } { 2 } } \cdot { \frac { m } { 2 } } + { \frac { m } { 2 } } \cdot \left( { \frac { m } { 2 } } + 1 \right) \right] = m ^ { 2 } + m .
$$

So a total of

$$
( m ^ { 2 } + m ) + m = m ^ { 2 } + 2 m
$$

complex multiplications are now needed.

Applying the technique one more time gives us 4 sums each with $m / 4$ terms and reduces the $m ^ { 2 }$ portion of this total to

$$
4 \left[ \left( { \frac { m } { 4 } } \right) ^ { 2 } + { \frac { m } { 4 } } \left( { \frac { m } { 4 } } \stackrel { , } { + } 1 \right) \right] = { \frac { m ^ { 2 } } { 2 } } + m ,
$$

for a new total of $( m ^ { 2 } / 2 ) + 3 m$ complex multiplications. Repeating the process $r$ times reduces the total number of required complex multiplications to

$$
{ \frac { m ^ { 2 } } { 2 ^ { r - 2 } } } + m r .
$$

The process is complete when $r = p + 1$ ， since $m = 2 ^ { p }$ and $2 m = 2 ^ { p + 1 }$ . As a consequence, after $r = p { + } 1$ reductions of this type,the number of complex multiplications is reduced to

$$
\frac { ( 2 ^ { p } ) ^ { 2 } } { 2 ^ { p - 1 } } + m ( p + 1 ) = 2 m + p m + m = 3 m + m \log _ { 2 } m = { \cal O } ( m \log _ { 2 } m ) .
$$

Because of the way the calculations are arranged, the number of required complex additions is comparable. To illustrate the significance of this reduction, suppose we have $m = 2 ^ { 1 0 } = 1 0 \bar { 2 } 4$ . The direct calculation would require

$$
( 2 m ) ^ { 2 } = ( 2 0 4 8 ) ^ { 2 } \approx 4 , 2 0 0 , 0 0 0
$$

calculations. The fast Fourier transform procedure reduces the number of calculations to

$$
3 ( 1 0 2 4 ) + 1 0 2 4 \log _ { 2 } { 1 0 2 4 } \approx 1 3 , 3 0 0 .
$$

Consider the fast Fourier transform techique apid to $8 = 2 ^ { 3 }$ data points $\{ ( x _ { j } , y _ { j } ) \} _ { j = 0 } ^ { 7 } ,$ where $x _ { j } = - \pi + j \pi / 4$ ,for each $j = 0 , 1 , \ldots , 7$ . In this case $2 m = 8$ ，S $) m = 4 = 2 ^ { 2 }$ and $p = 2$

From (8.24) we have

$$
S _ { 4 } ( x ) = \frac { a _ { 0 } + a _ { 4 } \cos { 4 x } } { 2 } + \sum _ { k = 1 } ^ { 3 } ( a _ { k } \cos { k x } + b _ { k } \sin { k x } ) ,
$$

where

$$
a _ { k } = \frac { 1 } { 4 } \sum _ { j = 0 } ^ { 7 } y _ { j } \cos k x _ { j } \quad \mathrm { a n d } \quad b _ { k } = \frac { 1 } { 4 } \sum _ { j = 0 } ^ { 7 } y _ { j } \sin k x _ { j } , \quad k = 0 , 1 , 2 , 3 , 4 .
$$

Define

$$
F ( x ) = { \frac { 1 } { 4 } } \sum _ { j = 0 } ^ { 7 } c _ { k } e ^ { i k x } ,
$$

where

$$
c _ { k } = \sum _ { j = 0 } ^ { 7 } y _ { j } e ^ { i k \pi j / 4 } , \quad \mathrm { f o r } \ k = 0 , 1 , \dots , 7 .
$$

Then by (8.29), for $k = 0 , 1 , 2 , 3 , 4 ,$

$$
{ \frac { 1 } { 4 } } c _ { k } e ^ { - i k \pi } = a _ { k } + i b _ { k } .
$$

By direct calculation, the complex constants $c _ { k }$ are given by

$$
\begin{array} { r l } & { C _ { 0 } \sim \mathcal { P } + \mathcal { D } + \mathcal { T } \cdot \Phi ^ { 2 } = \mathcal { P } + \mathcal { P } + \mathcal { P } + \mathcal { P } + \mathcal { P } + \mathcal { P } + \mathcal { P } \cdot \Phi } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ &  \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \end{array}
$$

Because of the small size of the collection of data points,many of the coefficients of the $y _ { j }$ in these equations are 1 or $- 1$ . This frequency will decrease in a larger application,so to count the computational operations accurately,multiplication by 1 or -l will be included, even though it would not be necessary in this example. With this understanding,64 multiplications/divisions and 56 additions/subtractions are required for the direct computation of $c _ { 0 } , c _ { 1 } , \ldots , c _ { 7 }$

To apply the fast Fourier transform procedure with $r = 1$ ， we first define

$$
\begin{array} { r l } & { d _ { 4 } - \frac { 1 } { 2 } ( \langle \partial _ { t } - c \rangle - \mathcal { H } + \mathcal { H } - \mathcal { H } ) } \\ & { d _ { 4 } } \\ & { d _ { 5 } = \frac { 1 } { 2 } ( \langle c \rangle - c \rangle - 3 ( \mathcal { H } - \mathcal { P } + \mathcal { P } ) \cdot \mathcal { Q } ) } \\ & { d _ { 6 } = \frac { 1 } { 2 } ( c \rangle + \mathcal { P } - \mathcal { H } - \langle \partial _ { t } - c \rangle + \mathcal { P } - \langle \partial _ { t } + \mathcal { P } \rangle } \\ & { d _ { 7 } } \\ & { d _ { 8 } = \frac { 1 } { 2 } ( c \rangle - \mathcal { P } ) - 3 ( \mathcal { H } + \mathcal { P } ) \cdot \mathcal { P } + \langle \partial _ { t } + \mathcal { P } \rangle - \mathcal { P } - i \mathcal { P } ) \cdot \mathcal { Q } } \\ & { d _ { 8 } = \frac { 1 } { 2 } ( c \cdot \mathcal { Q } - \mathcal { P } ) - 3 ( \mathcal { P } - \mathcal { P } + \mathcal { P } \cdot \mathcal { P } ) } \\ & { d _ { 9 } - \frac { 1 } { 2 } ( c \cdot \mathcal { P } - \mathcal { P } ) - \mathcal { P } \cdot \mathcal { P } - \mathcal { P } \mathcal { P } ) \cdot \mathcal { Q } } \\ & { d _ { 9 } - \frac { 1 } { 2 } ( c \cdot \mathcal { P } + \mathcal { P } ) - 3 ( \mathcal { P } - \mathcal { P } - \mathcal { P } \cdot \mathcal { P } ) \cdot \mathcal { P } } \\ & { d _ { 9 } - \frac { 1 } { 2 } ( c \cdot \mathcal { P } + \mathcal { P } ) - 3 ( \mathcal { P } - \mathcal { P } - \mathcal { P } ) \cdot \mathcal { P } - i \mathcal { P } ) } \\ & { d _ { 4 } - \frac { 1 } { 2 } ( c \cdot \mathcal { P } - \mathcal { P } ) - \mathcal { Q } ( i \cdot \mathcal { P } ) \cdot \mathcal { P } - i \mathcal { P } ) \cdot \mathcal { P } - i \mathcal { P } \cdot \mathcal { P } - i \mathcal { P } . } \end{array}
$$

We then define, for $r = 2$ ，

$$
\begin{array} { r l } & { x _ { 5 } - \frac { 1 } { 2 } ( \theta _ { 6 } + \theta _ { 6 } ) = \mathcal { N } + \theta _ { 4 } , } \\ & { x _ { 5 } - \frac { 1 } { 2 } ( \theta _ { 6 } - \theta _ { 6 } ) = \mathcal { N } + \theta _ { 5 } , } \\ & { x _ { 6 } = \frac { 1 } { 2 } ( \theta _ { 6 } + \theta _ { 6 } ) = \mathcal { N } + \theta _ { 5 } , \quad | \mathcal { N } | ^ { 2 } , } \\ & { x _ { 7 } = \frac { 1 } { 2 } ( \theta _ { 6 } + \theta _ { 6 } ) = \mathcal { N } + \theta _ { 7 } , \quad | \mathcal { N } | ^ { 3 } , } \\ & { x _ { 1 } = \frac { 1 } { 2 } ( \theta _ { 6 } - \theta _ { 3 } ) = - i \phi _ { 1 } , \quad | \mathcal { N } | ^ { 3 } , } \\ & { x _ { 9 } = \frac { 1 } { 2 } ( \theta _ { 6 } - \theta _ { 4 } ) = \mathcal { N } - \mathcal { N } + \theta _ { 8 } , } \\ & { x _ { 9 } = \frac { 1 } { 2 } ( \theta _ { 6 } - \theta _ { 6 } ) = \mathcal { N } + \{ x _ { 9 } , - w _ { 9 } \} , } \\ & { x _ { 6 } = \frac { 1 } { 2 } ( \theta _ { 6 } - \theta _ { 6 } ) = \mathcal { N } + \{ x _ { 1 } , \forall \} \partial \Omega ( \theta _ { 6 } - w _ { 9 } ) = \mathcal { N } + \theta _ { 1 } , } \\ & { x _ { 7 } = \frac { 1 } { 2 } ( \partial \Omega - i \omega _ { 1 } ) = \mathcal { N } + \theta _ { 1 } , } \\ & { x _ { 9 } = \frac { 1 } { 2 } ( \partial \Omega - i \omega _ { 2 } ) = \mathcal { N } + \theta _ { 1 } - i \phi _ { 1 } , } \\ & { x _ { 1 } = \frac { 1 } { 2 } ( \partial \Omega - i \omega _ { 1 } ) = \mathcal { N } + \theta _ { 1 } - i \phi _ { 2 } , } \\ & { x _ { 9 } = \frac { 1 } { 2 } ( \partial \Omega - i \omega _ { 2 } ) = \mathcal { N } + \theta _ { 1 } - i \phi _ { 2 } , } \end{array}
$$

Finally, for $r = p + 1 = 3$ , we define

$$
\begin{array} { r l } & { \hat { \lambda } _ { 0 } - \frac { 1 } { 2 } ( \epsilon \epsilon ) \cdot ( s \epsilon ) - \mathcal { D } ( s - \epsilon ) } \\ & { \hat { \mathcal { L } } = \frac { 1 } { 2 } ( \epsilon s ) - \mathcal { D } ( s - \epsilon s ) - \mathcal { D } ( s - \epsilon s ) } \\ & { \hat { \mathcal { L } } = \frac { 1 } { 2 } ( \epsilon s ) - \frac { 1 } { 2 } ( \epsilon s ) - \mathcal { D } ( s - \epsilon s ) } \\ & { \hat { \mathcal { L } } = \frac { 1 } { 2 } ( \epsilon s ) - \epsilon \epsilon s _ { 0 } = 0 , } \\ & { \hat { \mathcal { L } } = \frac { 1 } { 2 } ( \epsilon s ) - \epsilon \epsilon s _ { 0 } = 0 , } \\ & { \hat { \mathcal { L } } = \frac { 1 } { 2 } ( \epsilon s + 1 ) / \sqrt { 2 } \epsilon s _ { 0 } + \epsilon s _ { 0 } ) - ( \epsilon s - 1 ) / \sqrt { 2 } \eta s _ { 0 } } \\ & { \hat { \mathcal { L } } = \frac { 1 } { 2 } ( \epsilon ( - s ) / \sqrt { \lambda } \phi _ { 0 } - \epsilon s _ { 0 } ) = ( \epsilon s - 1 ) / \sqrt { 2 } \eta s _ { 0 } } \\ & { \hat { \mathcal { L } } = - \frac { 1 } { 2 } ( \epsilon s - 1 ) / \sqrt { \lambda } \phi _ { 0 } - \epsilon s _ { 0 } ) = ( - \epsilon s - 1 ) / \sqrt { 2 } \eta s _ { 0 } } \\ & { \hat { \mathcal { L } } = \frac { 1 } { 2 } ( \epsilon s ( - 1 ) / \sqrt { 2 } \eta s _ { 0 } + 1 ) / \sqrt { 2 } \eta s _ { 0 } } \\ & { \hat { \mathcal { L } } = \frac { 1 } { 2 } \frac { 1 } { 2 } ( \epsilon s ( - 1 ) / \sqrt { 2 } \eta s _ { 0 } - \epsilon s _ { 0 } ) - ( - \epsilon s + 1 ) / \sqrt { 2 } \eta s _ { 0 } } \end{array}
$$

The $c _ { 0 } , \ldots , c _ { 7 } , d _ { 0 } , \ldots , d _ { 7 } , e _ { 0 } , \ldots , e _ { 7 }$ and $f _ { 0 } , \ldots , f _ { 7 }$ are independent of the particular $m \ : = \ : 4$ $m$ $\{ c _ { k } \} _ { k = 0 } ^ { 2 m - 1 } , \{ d _ { k } \} _ { k = 0 } ^ { 2 m - 1 } , \{ e _ { k } \} _ { k = 0 } ^ { 2 m - 1 }$ $\{ f _ { k } \} _ { k = 0 } ^ { 2 m - 1 }$

1. fo= yo;f1=y4;f=iy2；f= iy6;   
$\begin{array} { r l } & { f _ { 4 } = \{ ( i - 1 ) / \sqrt { 2 } \} \times \{ \zeta \} , } \\ & { f _ { 1 } = \{ - ( i + 1 ) / \sqrt { 2 } \} \times . } \\ & { e _ { 0 } = f _ { 1 } + f _ { 1 } , \quad e _ { 1 } = - i ( f _ { 2 } + f _ { 2 } ) ; \quad e _ { 2 } = ( ( - i + 1 ) / \sqrt { 2 } ) ( f _ { 4 } + f _ { 5 } ) ; } \\ & { e _ { 3 } = ( ( - i - 1 ) / \sqrt { 2 } ) ( f _ { 6 } + f _ { 7 } ) ; \quad e _ { 4 } = f _ { 6 } - f _ { 1 } , \quad e _ { 5 } = f _ { 2 } - f _ { 3 } ; } \\ & { e _ { 6 } = f _ { 4 } - f _ { 5 } , \quad e _ { 5 } = f _ { 6 } - f _ { 7 } , } \\ & { d _ { 0 } = e _ { 6 } + e _ { 1 } ; \quad d _ { 1 } = - i ( e _ { 2 } + e _ { 3 } ) ; \quad d _ { 2 } = e _ { 4 } + e _ { 5 } ; \quad d _ { 3 } = - i ( e _ { 6 } + e _ { 7 } ) } \\ & { d _ { 4 } = e _ { 0 } - e _ { 1 } ; \quad d _ { 5 } = e _ { 2 } - e _ { 3 } ; \quad d _ { 6 } = e _ { 4 } - e _ { 5 } ; \quad d _ { 7 } = e _ { 6 } - e _ { 7 } , } \\ & { e _ { 1 } = d _ { 0 } + d _ { 1 } ; \quad c _ { 1 } = d _ { 2 } + d _ { 3 } ; \quad c _ { 2 } = d _ { 4 } + d _ { 5 } ; \quad c _ { 3 } = d _ { 6 } + d _ { 4 } ; } \\ & { e _ { 4 } = d _ { 6 } - d _ { 1 } ; \quad c _ { 5 } = d _ { 2 } - d _ { 3 } ; \quad c _ { 6 } = d _ { 4 } - d _ { 5 } ; \quad c _ { 7 } = d _ { 6 } - d _ { 7 } . } \end{array}$ y3；   
2.   
3.   
4.

Computing the constants $c _ { 0 } , c _ { 1 } , \ldots , c _ { 7 }$ in this manner requires the number of operations shown in Table 8.13. Note again that multiplication by 1 or $- 1$ has been included in the count, even though this does not require computational effort.

coefcients The lack of multiplications/divisions in Step 4 reflects the fact that for any $\left\{ c _ { k } \right\} _ { k = 0 } ^ { 2 m - 1 }$ are computed from $\{ d _ { k } \} _ { k = 0 } ^ { 2 m - 1 }$ in the same manner: $_ { m }$ ，the

$$
c _ { k } = d _ { 2 k } + d _ { 2 k + 1 }
$$

Table 8.13   

<table><tr><td>Step</td><td>Multiplications/divisions</td><td>Additions/subtractions</td></tr><tr><td>(1)</td><td>8</td><td>0</td></tr><tr><td>(2)</td><td>8</td><td>8</td></tr><tr><td>(3)</td><td>8</td><td>8</td></tr><tr><td>(4)</td><td>0</td><td>8</td></tr><tr><td>Total</td><td>24</td><td>24</td></tr></table>

and

$$
c _ { k + m } = d _ { 2 k } - d _ { 2 k + 1 } , \quad \mathrm { f o r } \ k = 0 , 1 , \ldots , m - 1 ,
$$

so no complex multiplication is involved.

In summary, the direct computation of the coefficients $c _ { 0 } , c _ { 1 } , \ldots , c _ { 7 }$ requires $6 4 \mathrm { \ m u l } .$ tiplications/divisions and 56 additions/subtractions.The fast Fourier transform technique reduces the computations to 24 multiplications/divisions and 24 additions/subtractions.

Algorithm 8.3 performs the fast Fourier transform when $m = 2 ^ { p }$ for some positive integer $p$ . Modifications of the technique can be made when $m$ takes other forms.

# Fast Fourier Transform

To compute the coefficients in the summation

$$
{ \frac { 1 } { m } } \sum _ { k = 0 } ^ { 2 m - 1 } c _ { k } e ^ { i k x } = { \frac { 1 } { m } } \sum _ { k = 0 } ^ { 2 m - 1 } c _ { k } ( \cos k x + i \sin k x ) , \quad { \mathrm { w h e r e ~ } } i = { \sqrt { - 1 } } ,
$$

for the data $\{ ( x _ { j } , y _ { j } ) \} _ { j = 0 } ^ { 2 m - 1 }$ where $m = 2 ^ { p }$ and $x _ { j } = - \pi + j \pi / m$ for $j = 0 , 1 , \ldots , 2 m - 1$

INPUT $m , p ; y _ { 0 } , y _ { 1 } , . . . , y _ { 2 m - 1 } .$

OUTPUT complex numbers $c _ { 0 } , \ldots , c _ { 2 m - 1 }$ ; real numbers $a _ { 0 } , \dots , a _ { m } ; b _ { 1 } , \dots , b _ { m - 1 }$

Step 1 Set $M = m$

$$
\begin{array} { l } { q = p ; } \\ { \zeta = e ^ { \pi i / m } . } \end{array}
$$

Step 2 For $j = 0 , 1 , \ldots , 2 m - 1 \mathrm { s e t } c _ { j } = y _ { . }$

$$
\begin{array} { r l r l } { { 3 } } & { { } \mathrm { F o r } j = 1 , 2 , \dotsc , M } & { } & { { } \sec \xi _ { j } = \xi ^ { j } ; } \\ { \quad } & { { } } & { \xi _ { j + M } \doteq - \xi _ { j } . } \end{array}
$$

Step 4 Set $K = 0 ;$ $\xi _ { 0 } = 1 .$

Step 5For $L = 1 , 2 , \dots , p + 1$ do Steps 6--12.

Step $\sigma$ While $K < 2 m - 1$ do Steps 7-11.

Step 8 Let $K = k _ { p } \cdot 2 ^ { p } + k _ { p - 1 } \cdot 2 ^ { p - 1 } + \cdot \cdot \cdot + k _ { 1 } \cdot 2 + k _ { 0 } ;$ (Decompose k.) set $\begin{array} { r c l } { { } } & { { } } & { { K _ { 1 } = K / 2 ^ { q } = k _ { p } \cdot 2 ^ { p - q } + \cdot \cdot \cdot + k _ { q + 1 } \cdot 2 + k _ { q } ; } } \\ { { } } & { { } } & { { K _ { 2 } = k _ { q } \cdot 2 ^ { p } + k _ { q + 1 } \cdot 2 ^ { p - 1 } + \cdot \cdot \cdot + k _ { p } \cdot 2 ^ { q } . } } \end{array}$

Step 9 Set $\eta = c _ { K + M } \xi _ { K _ { 2 } }$ ；

$$
\begin{array} { l } { { c _ { K + M } = c _ { K } - \eta ; } } \\ { { c _ { K } = c _ { K } + \eta . } } \end{array}
$$

Step 10 Set $K = K + 1$

Step 11 Set $K = K + M$

Step 12 Set $K = 0$ $\begin{array} { c } { { M = M / 2 ; } } \\ { { q = q - 1 . } } \end{array}$

Step 13 While $K < 2 m - 1$ do Steps 14-16.

Step 14 Let set ${ \begin{array} { r l } & { \cdot K = k _ { p } \cdot 2 ^ { p } + k _ { p - 1 } \cdot 2 ^ { p - 1 } + \cdot \cdot \cdot + k _ { 1 } \cdot 2 + k _ { 0 } ; \quad ( D e c o m p o s e k . ) } \\ & { j = k _ { 0 } \cdot 2 ^ { p } + k _ { 1 } \cdot 2 ^ { p - 1 } + \cdot \cdot \cdot + k _ { p - 1 } \cdot 2 + k _ { p } . } \end{array} }$

Step 15 If $j > K$ then interchange $c _ { j }$ and $c _ { k }$

Step 16 Set $K = K + 1$

Step 17 Set $a _ { 0 } = c _ { 0 } / m$ ；$a _ { m } = \mathrm { R e } ( e ^ { - i \pi m } c _ { m } / m ) .$

Step 18 For $\begin{array} { r } { j = 1 , \dots , m - 1 \mathrm { ~ s e t } a _ { j } = \mathrm { R e } ( e ^ { - i \pi j } c _ { j } / m ) ; } \\ { b _ { j } = \mathrm { I m } ( e ^ { - i \pi j } c _ { j } / m ) . } \end{array}$

Step 19OUTPUT $( c _ { 0 } , \ldots , c _ { 2 m - 1 } ; a _ { 0 } , \ldots , a _ { m } ; b _ { 1 } , \ldots , b _ { m - 1 } ) ;$ STOP.

Let $f ( x ) = x ^ { 4 } - 3 x ^ { 3 } + 2 x ^ { 2 } - \tan { x ( x - 2 ) }$ . To determine the trigonometricinterpolating polynomial of degree 4 for the data $\{ ( x _ { j } , y _ { j } ) \} _ { j = 0 } ^ { 7 }$ where $x _ { j } = j / 4$ and $y _ { j } ~ = ~ f ( x _ { j } )$ ， requires a transformation of the interval[0,2] to $[ - \pi , \pi ]$ . This is given by

$$
z _ { j } = \pi ( x _ { j } - 1 ) ,
$$

so that the input data to Algorithm 8.3 are

$$
\left\{ z _ { j } , f \left( 1 + \frac { z _ { j } } { \pi } \right) \right\} _ { j = 0 } ^ { 7 } .
$$

The interpolating polynomial in $z$ is

$$
S _ { 4 } ( z ) = 0 . 7 6 1 9 7 9 + 0 . 7 7 1 8 4 1 \cos z + 0 . 0 1 7 3 0 3 7 \cos 2 z + 0 . 0 0 6 8 6 3 0 4 \cos 3 z
$$

$$
- 0 . 0 0 0 5 7 8 5 4 5 \cos { 4 z } - 0 . 3 8 6 3 7 4 \sin { z } + 0 . 0 4 6 8 7 5 0 \sin { 2 z } - 0 . 0 1 1 3 7 3 8 \sin { 3 z } .
$$

The trigonometric polynomial $S _ { 4 } ( x )$ on[0,2]isbaedbysii $z = \pi ( x - 1 )$ into $\mathbb { S } _ { 4 } ( z )$ . The graphs of $y = f ( x )$ and $y = S _ { 4 } ( x )$ are shown in Figure 8.15. Values of $f ( x )$ and $S _ { 4 } ( x )$ are given in Table 8.14. ■

![](images/4f7508c907c8603092c118bc8e53312c0812d71dae61e321acb94937d03e3f34.jpg)  
Figure 8.15   
Table 8.14

<table><tr><td>f(x) x</td><td>S4(x) If(x)-S4(x)l</td></tr><tr><td>0.125 0.26440</td><td>0.25001 1.44 × 10-2</td></tr><tr><td>0.375 0.84081</td><td>0.84647 5.66×10-3</td></tr><tr><td>0.625 1.36150</td><td>1.35824 3.27× 10-3</td></tr><tr><td>0.875 1.61282</td><td>1.61515 2.33 ×</td></tr><tr><td>1.125 1.36672</td><td>10-3 1.36471 2.02 × 10-3</td></tr><tr><td>1.375 0.71697</td><td>0.71931 2.33 × 10-3</td></tr><tr><td>1.625 0.07909</td><td>0.07496 4.14 × 10-3</td></tr><tr><td>1.875 -0.14576 -0.13301</td><td>1.27 × 10-2</td></tr></table>

More details on the verification of the validity of the fast Fourier transform procedure can be found in $\left[ \mathbf { H a m } \right]$ ,which presents the method from a mathematical approach, or in [Brac], where the presentation is based on methods more likely to be familiar to engineers. [AHU, pp. 252-269], is a good reference for a discussion of the computational aspects of the method. Modification of the procedure for the case when m is not a power of 2 can be found in [Win]. A presentation of the techniques and related material from the point of view of applied abstract algebra is given in [Lau, pp. 438-465].

# ExERCIsE SET 8.6

1.Determine the trigonometric interpolating polynomial $\pmb { S } _ { 2 } ( \pmb { x } )$ of degree 2 on $[ - \pi , \pi ]$ for the following functions,and graph $f ( x ) - S _ { 2 } ( x )$ ：

a. $f ( x ) = \pi ( x - \pi )$ $\begin{array} { r l } { \mathbf { b } , \ } & { f ( x ) = x ( \pi - x ) } \\ { \mathbf { d } . \ } & { f ( x ) = \left\{ { \begin{array} { l l } { - 1 , } & { - \pi \leq x \leq 0 } \\ { 1 , } & { 0 < x \leq \pi } \end{array} } \right. } \end{array}$   
c. $f ( x ) = \left| x \right|$

2.Determine the trigonometric interpolating polynomial of degre 4 for $f ( x ) = x ( \pi - x )$ on the interval $[ - \pi , \pi ]$ using:

a. Direct calculation;   
b. The Fast Fourier Transform Algorithm.

3.Usethe Fast Fourier Transform Algorithm tocompute the trigonometric interpolating polynomial of degree 4 on $[ - \pi , \pi ]$ for the following functions.

$$
\begin{array} { r l } & { f ( x ) = \pi ( x - \pi ) } \\ & { f ( x ) = \cos \pi x - 2 \sin \pi x } \end{array} \qquad \begin{array} { r l } & { \mathbf { b } _ { \cdot } \quad f ( x ) = | x | } \\ & { \mathbf { d } _ { \cdot } \quad f ( x ) = x \cos x ^ { 2 } + e ^ { x } \cos e ^ { x } } \end{array}
$$

4.a.Determine the trigonometric interpolating polynomial $S _ { 4 } ( x )$ of degree 4 for $f ( x ) =$ $x ^ { 2 }$ sin $\pmb { x }$ on the interval [0,1]. b.Compute $\begin{array} { r } { \int _ { 0 } ^ { 1 } S _ { 4 } ( x ) d x } \end{array}$ c. Compare the integral in part (b) to $\textstyle \int _ { 0 } ^ { 1 } x ^ { 2 } \sin x d x$

5. Use the approximations obtained in Exercise 3 to approximate the following integrals, and compare your results to the actual values.

$$
\begin{array} { l l } { { \displaystyle \int _ { - \pi } ^ { \pi } \pi ( x - \pi ) d x } } & { { \mathrm { ~ \qquad ~ b . ~ } \displaystyle \int _ { - \pi } ^ { \pi } | x | d x } } \\ { { \displaystyle \int _ { - \pi } ^ { \pi } ( \cos \pi x - 2 \sin \pi x ) d x } } & { { \mathrm { ~ \qquad ~ d . ~ } \displaystyle \int _ { - \pi } ^ { \pi } ( x \cos x ^ { 2 } + e ^ { x } \cos e ^ { x } ) d x } } \end{array} 
$$

6.Use the Fast Fourier Transform Algorithm to determine the trigonometric interpolating polynomial of degree 16 for $f ( x ) = x ^ { 2 } \cos x$ on $[ - \pi , \pi ]$

7.Usethe Fast Fourier Transform Algorithm todetermine the trigonometric interpolating polynomial of degree 64 for $f ( x ) = x ^ { 2 } \cos x$ on $[ - \pi , \pi ]$

8.Useatrgooetricidentityotat $\begin{array} { r } { \sum _ { j = 0 } ^ { 2 m - 1 } ( \cos m x _ { j } ) ^ { 2 } = 2 m } \end{array}$

9.Show that $c _ { 0 } , \ldots , c _ { 2 m - 1 }$ in Algorithm 8.3 are given by

$$
\begin{array} { r } { \left[ \begin{array} { c } { c _ { 0 } } \\ { c _ { 1 } } \\ { c _ { 2 } } \\ { \vdots } \\ { c _ { 2 m - 1 } } \end{array} \right] = \left[ \begin{array} { c c c c c c } { 1 } & { 1 } & { 1 } & { \cdots } & { 1 } \\ { 1 } & { \zeta } & { \zeta ^ { 2 } } & { \cdots } & { \zeta ^ { 2 m - 1 } } \\ { 1 } & { \zeta ^ { 2 } } & { \zeta ^ { 4 } } & { \cdots } & { \zeta ^ { 4 m - 2 } } \\ { \vdots } & { \vdots } & { \vdots } & & { \vdots } \\ { 1 } & { \zeta ^ { 2 m - 1 } } & { \zeta ^ { 4 m - 2 } } & { \cdots } & { \zeta ^ { ( 2 m - 1 ) ^ { 2 } } } \end{array} \right] \left[ \begin{array} { c } { y _ { 0 } } \\ { y _ { 1 } } \\ { y _ { 2 } } \\ { \vdots } \\ { y _ { 2 m - 1 } } \end{array} \right] , } \end{array}
$$

where $\zeta = e ^ { \pi i / m }$ ，

10.In the discussion preceding Algorithm 8.3, an example for $m \ = \ 4$ was explained. Define vectors c, $\mathbf { d } , \mathbf { e } , \mathbf { f } ,$ and $\pmb { y }$ as

$$
\begin{array} { r } { \mathbf { c } = ( c _ { 0 } , c _ { 1 } , \ldots , c _ { 7 } ) ^ { t } , } \\ { \mathbf { d } = ( d _ { 0 } , d _ { 1 } , \ldots , d _ { 7 } ) ^ { t } , } \\ { \mathbf { e } = ( e _ { 0 } , e _ { 1 } , \ldots , e _ { 7 } ) ^ { t } , } \end{array}
$$

$$
\begin{array} { r } { \mathbf { f } = ( f _ { 0 } , f _ { 1 } , \ldots , f _ { 7 } ) ^ { t } , } \\ { \mathbf { y } = ( y _ { 0 } , y _ { 1 } , \ldots , y _ { 7 } ) ^ { t } . } \end{array}
$$

Find matrices $A , B , C$ ,and $D$ so that $\mathfrak { c } = A \mathbf { d }$ ， $\mathbf { d } = B \mathbf { e }$ ， $\mathfrak { e } = C \mathfrak { f }$ ,and $\mathbf { f } = D \mathbf { y }$

# 8.7 Survey of Methods and Software

In this chapter we have considered approximating data and functions with elementary func-tions. The elementary functions used were polynomials, rational functions, and trigonometric polynomials. We considered two types of approximations, discrete and continuous. Discrete approximations arise when approximating a finite set of data with an elementary function. Continuous approximations are used when the function to be approximated is known.

Discrete Ieast squares techniques are recommended when the function is specified by giving a set of data that may not exactly represent the function. Least squares fit of data can take the form of a linear or other polynomial approximation or even an exponential form. These approximations are computed by solving sets of normal equations,as given in Section 8.1.

If the data are periodic, a trigonometric least squares fit may be appropriate. Because of the orthonormality of the trigonometric basis functions, the least squares trigonometric approximation does not require the solution of a linear system. For large amounts of periodic data, interpolation by trigonometric polynomials is also recommended.An efficient method of computing the trigonometric interpolating polynomial is given by the fast Fourier transform.

When the function to be approximated can be evaluated at any required argument, the approximations seek to minimize an integral instead of a sum. The continuous least squares polynomial approximations were considered in Section 8.2. Efficient computation of least squares polynomials lead to orthonormal sets of polynomials,such as the Legendre and Chebyshev polynomials. Approximation by rational functions was studied in Section 8.4, where Padé approximation as a generalization of the Maclaurin polynomial and its extension to Chebyshev rational approximation were presented. Both methods allow a more uniform method of approximation than polynomials. Continuous least squares approximation by trigonometric functions was discussed in Section 8.5, especially as it relates to Fourier series.

The IMSL Library provides a number of routines for approximation. The subroutine RLINE gives the least squares line for a set of data points,and returns statistics such as means and variances. The subroutine FNLSQ computes the discrete least squares approximation for a user's choice of basis functions,and BSLSQ computes a least squares cubic spline approximation. The subroutine RATCH computes the rational weighted Chebyshev approximation to a continuous functions on an interval $[ a , b ]$ ，and FFTCB computes the fast Fourier transform for a given set of data in a manner similar to Algorithm 8.3.

The NAG Library has many subroutines for function approximation. Least squares polynomial approximation is given in the subroutine EO2ADF. This subroutine is quite versatile in that it computes least squares polynomials for varying degrees and gives their least squares errors.It uses Chebyshev polynomials to minimize roundoff error and enhance accuracy.

The routine EO2AEF can be used to evaluate the approximation obtained by E02ADF. NAG also supplies the routine EO2BAF to compute least squares cubic spline fits,E02GAF to compute the best $L _ { 1 }$ linear fit, and E02GCF to compute the best $L _ { \infty }$ fit. The routine E02RAF computes the Padé approximation. The NAG Library also includes many routines for fast Fourier transforms, one of which is CO6ECF.

The netlib library contains the subroutine polfit.f under the package slatec to com-pute the polynomial least squares approximation to a discrete set of points. The subroutine pvalue.f can be used to evaluate the polynomial from polfit.f and any of its derivatives at a given point.

For further information on the general theory of approximation theory see Powell $\{ { \bf P o } \}$ ， Davis [Da], or Cheney [Ch].A good reference for methods of least squares is Lawson and Hanson [LH],and information about Fourier transforms can be found in Van Loan [Van] and in Briggs and Hanson [BH].

CHAPTER

9

# Approximating Eigenvalues

■ ■

density $\rho ( x )$ are described by the partial differential equation

$$
\rho ( x ) \frac { \partial ^ { 2 } \nu } { \partial t ^ { 2 } } ( x , t ) = \frac { \partial } { \partial x } \left[ p ( x ) \frac { \partial \nu } { \partial x } ( x , t ) \right] ,
$$

where ${ \pmb \nu } ( { \pmb x } , t )$ is the mean longitudinal displacement of a section of the bar from its equilibrium position $\pmb { x }$ at time $t$ ，The vibrations can be written as a sum of simple harmonic vibrations:

$$
\nu ( x , t ) = \sum _ { k = 0 } ^ { \infty } c _ { k } u _ { k } ( x ) \cos \sqrt { \lambda _ { k } } ( t - t _ { 0 } ) ,
$$

where

$$
\frac { d } { d x } \left[ p ( x ) \frac { d u _ { k } } { d x } ( x ) \right] + \lambda _ { k } \rho ( x ) u _ { k } ( x ) = 0 .
$$

If the bar has length $l$ and is fixed at its ends, then this differential equation holds for $0 < x < l$ and $\nu ( 0 ) = \nu ( l ) = 0$ . A system of these differential equations is called a Sturm-Liouville system, and the numbers $\lambda _ { k }$ are eigenvalues with corresponding eigenfunctions $u _ { k } ( x )$ ·

Suppose the bar is $1 \textbf { m }$ long with uniform stiffness $p ( { \pmb x } ) = { \pmb p }$ and uniform density $\rho ( { \pmb x } ) = \rho$ . To approximate $\pmb { u }$ and $\pmb { \lambda }$ ,let $h = 0 . 2$ Then xj = 0.2j, for 0 ≤ j ≤ 5,and we can use the centered-difference formula (4.5) in Section 4.1 to approximate the first derivatives. This gives the linear system

$$
A \mathbf { w } = { \left[ \begin{array} { l l l l } { 2 } & { - 1 } & { 0 } & { 0 } \\ { - 1 } & { 2 } & { - 1 } & { 0 } \\ { 0 } & { - 1 } & { 2 } & { - 1 } \\ { 0 } & { 0 } & { - 1 } & { 2 } \end{array} \right] } { \left[ \begin{array} { l } { w _ { 1 } } \\ { w _ { 2 } } \\ { w _ { 3 } } \\ { w _ { 4 } } \end{array} \right] } = - 0 . 0 4 { \frac { \rho } { p } } \lambda { \left[ \begin{array} { l } { w _ { 1 } } \\ { w _ { 2 } } \\ { w _ { 3 } } \\ { w _ { 4 } } \end{array} \right] } = - 0 . 0 4 { \frac { \rho } { p } } \lambda \mathbf { w } .
$$

![](images/c61d7688fbdf0b7cc8e303c3494d6e15953ec9f8d3d8e546efc77d980d3c4907.jpg)

In this system, $w _ { j } \approx u ( x _ { j } )$ ，for $1 \leq j \leq 4$ ，and $w _ { 0 } ~ = ~ w _ { 5 } ~ = ~ 0$ .The four eigenvalues of A approximate the eigenvalues of the Sturm-Liouville system. It is the approximation of eigenvalues that we will consider in this chapter. A Sturm-Liouville application is discussed in Exercise 11 of Section 9.4.

# 9.1 Linear Algebra and Eigenvalues

Eigenvalues and eigenvectors were introduced in Chapter 7 in connection with the conver-gence of iterative methods for approximating the solution to a linear system. To determine the eigenvalues of an $n \times n$ matrix $A$ ,we construct the characteristic polynomial

$$
p ( \lambda ) = \det ( A - \lambda I )
$$

and then determine its zeros.Finding the determinant of an $n \times n$ matrix is computationally expensive,and finding good approximations to the roots of $p ( \lambda )$ is also difficult. In this chapter we willexplore other means for approximating the eigenvalues of a matrix.

In chapter 7 we found that an iterative technique for solving a linear system will converge if all the eigenvalues associated with the problem have magnitude less than 1. The exact values of the eigenvalues in this case are not of primary importance-only the region of the complex plane in which they lie.

Even when we need to know the eigenvalues,the fact that many of the techniques for their approximation are iterative implies that determining regions in which they lie is a first step in the direction of determining the approximation, since it provides us with the initial approximation that iterative methods need.

Before considering further results concerning eigenvalues and eigenvectors,we need some definitions and results from linear algebra. All the general results that will be needed in the remainder of this chapter are listed here for ease of reference. The proofs of the results that are not given can be found in most standard texts on linear algebra (see,for example, $[ \mathrm { N D } ] ,$ . The first definition parallels the definition for the linear independence of functions described in Section 8.2.

# Definition 9.1

Let $\{ \mathbf { v } ^ { ( 1 ) } , \mathbf { v } ^ { ( 2 ) } , \mathbf { v } ^ { ( 3 ) } , \dots , \mathbf { v } ^ { ( k ) } \}$ be a set of vectors.The set is linearly independent if whenever

$$
\begin{array} { r } { \mathbf { 0 } = \alpha _ { 1 } \mathbf { v } ^ { ( 1 ) } + \alpha _ { 2 } \mathbf { v } ^ { ( 2 ) } + \alpha _ { 3 } \mathbf { v } ^ { ( 3 ) } + \cdot \cdot \cdot + \alpha _ { k } \mathbf { v } ^ { ( k ) } , } \end{array}
$$

then $\alpha _ { 1 } = \alpha _ { 2 } = \alpha _ { 3 } = \cdot \cdot \cdot = \alpha _ { k } = 0$ . Otherwise the set of vectors is linearly dependent.

Note that any set of vectors containing the zero vector is linearly dependent.