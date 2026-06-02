assumes the form

$$
\int _ { a } ^ { b } { \dot { \gamma } } ( x ) d x \approx \sum _ { i = 0 } ^ { n } a _ { i } f ( x _ { i } ) ,
$$

where

$$
a _ { i } = \int _ { x _ { 0 } } ^ { x _ { n } } L _ { i } ( x ) d x = \int _ { x _ { 0 } } ^ { x _ { n } } \prod _ { j = 0 } ^ { n } { \frac { ( x - x _ { j } ) } { ( x _ { i } - x _ { j } ) } } d x .
$$

The following theorem details the error analysis associated with the closed Newton-Cotes formulas. For a proof of this theorem, see $[ \mathbf { I K }$ ,p. 313].

# Theorem 4.2

Suppose that $\scriptstyle \sum _ { i = 0 } ^ { n } a _ { i } f ( x _ { i } )$ denotes the $( n + 1 )$ -point closed Newton-Cotes formula with $x _ { 0 } = a , x _ { n } = b$ and $h = ( b - a ) / n$ . There exists $\xi \in ( a , b )$ for which

$$
\int _ { a } ^ { b } f ( x ) d x = \sum _ { i = 0 } ^ { n } a _ { i } f ( x _ { i } ) + { \frac { h ^ { n + 3 } f ^ { ( n + 2 ) } ( \xi ) } { ( n + 2 ) ! } } \int _ { 0 } ^ { n } t ^ { 2 } ( t - 1 ) \cdots ( t - n ) d t ,
$$

if $\pmb { n }$ is even and $f \in C ^ { n + 2 } [ a , b ]$ ,and

$$
\int _ { a } ^ { b } f ( x ) d x = \sum _ { i = 0 } ^ { n } a _ { i } f ( x _ { i } ) + { \frac { h ^ { n + 2 } f ^ { ( n + 1 ) } ( \xi ) } { ( n + 1 ) ! } } \int _ { 0 } ^ { n } t ( t - 1 ) \cdot \cdot \cdot ( t - n ) d t ,
$$

if $\pmb { n }$ is odd and $f \in C ^ { n + 1 } [ a , b ]$

Note that when $\pmb { n }$ is an even integer, the degree of precision is $n + 1$ ， although the interpolation polynomial is of degree at most $\pmb { n }$ . In the case where $\pmb { n }$ is odd, the degree of precision is only $\pmb { n }$ ·

Some of the common closed Newton-Cotes formulas with their error terms are as follows:

# ${ \pmb n } = 1 :$ :Trapezoidal rule

$$
\int _ { x _ { 0 } } ^ { x _ { 1 } } f ( x ) d x = { \frac { h } { 2 } } [ f ( x _ { 0 } ) + f ( x _ { 1 } ) ] - { \frac { h ^ { 3 } } { 1 2 } } f ^ { \prime \prime } ( \xi ) , \quad { \mathrm { w h e r e } } \quad x _ { 0 } < \xi < x _ { 1 } .
$$

$\pmb { n } = 2$ : Simpson's rule

$$
\int _ { x _ { 0 } } ^ { x _ { 2 } } f ( x ) d x = { \frac { h } { 3 } } [ f ( x _ { 0 } ) + 4 f ( x _ { 1 } ) + f ( x _ { 2 } ) ] - { \frac { h ^ { 5 } } { 9 0 } } f ^ { ( 4 ) } ( \xi ) , \quad { \mathrm { w h e r e } } \quad x _ { 0 } < \xi < x _ { 2 }
$$

# $n = 3 \colon$ Simpson's Three-Eighths rule

$$
\int _ { x _ { 0 } } ^ { x _ { 3 } } f ( x ) d x = { \frac { 3 h } { 8 } } [ f ( x _ { 0 } ) + 3 f ( x _ { 1 } ) + 3 f ( x _ { 2 } ) + f ( x _ { 3 } ) ] - { \frac { 3 h ^ { 5 } } { 8 0 } } f ^ { ( 4 ) } ( \xi ) ,
$$

n = 4:

$$
\int _ { x _ { 0 } } ^ { x _ { 4 } } f ( x ) d x = { \frac { 2 h } { 4 5 } } [ 7 f ( x _ { 0 } ) + 3 2 f ( x _ { 1 } ) + 1 2 f ( x _ { 2 } ) + 3 2 f ( x _ { 3 } ) + 7 f ( x _ { 4 } ) ] - { \frac { 8 h ^ { 7 } } { 9 4 5 } } f ^ { ( 6 ) } ( x _ { 0 } ) .
$$

$$
x _ { 0 } < \xi < x _ { 4 }
$$

The open Newton-Cotes formulas use the nodes $x _ { i } = x _ { 0 } + i h$ ,for each $i = 0 , 1 , \ldots , n ,$ where h = (b -a)/(n+2) and xo = a +h. This implies that xn = b-h,so we label the endpoints by seting x-1 = a and xn+1 = b,as shown in Figure 4.6. Open formulas contain all the nodes used for the approximation within the open interval (a,b). The formulas become

$$
\int _ { a } ^ { b } f ( x ) d x = \int _ { x _ { - 1 } } ^ { x _ { n + 1 } } f ( x ) d x \approx \sum _ { i = 0 } ^ { n } a _ { i } f ( x _ { i } ) ,
$$

where again

$$
a _ { i } = \int _ { a } ^ { b } L _ { i } ( x ) d x .
$$

![](images/cb84c86df475fdea3d3782a2082914d21f39b492e1c8034783efccec1b5ec2b1.jpg)  
Figure 4.6

The following theorem is analogous to Theorem 4.2; its proof is contained in [IK, p. 314].

Theorem 4.3 Suppose that ∑i=0ai f(xi) denotes the (n +1)-point open Newton-Cotes formula with x-1=a,xn+1 = b,and h = (b -a)/(n +2). There exists § ∈ (a,b) for which

$$
\int _ { a } ^ { b } f ( x ) d x = \sum _ { i = 0 } ^ { n } a _ { i } f ( x _ { i } ) + { \frac { h ^ { n + 3 } f ^ { ( n + 2 ) } ( \xi ) } { ( n + 2 ) ! } } \int _ { - 1 } ^ { n + 1 } t ^ { 2 } ( t - 1 ) \cdot \cdot \cdot ( t - n ) d t ,
$$

if $n$ is even and $f \in C ^ { n + 2 } [ a , b ]$ ,and

$$
\int _ { a } ^ { b } f ( x ) d x = \sum _ { i = 0 } ^ { n } a _ { i } f ( x _ { i } ) + { \frac { h ^ { n + 2 } f ^ { ( n + 1 ) } ( \xi ) } { ( n + 1 ) ! } } \int _ { - 1 } ^ { n + 1 } t ( t - 1 ) \cdot \cdot \cdot ( t - n ) d t ,
$$

if $n$ is odd and $f \in C ^ { n + 1 } \{ a , b \}$

Some of the common open Newton-Cotes formulas with their error terms are as follows:

# $\pmb { n } = \pmb { 0 }$ : Midpoint rule

$$
\int _ { x _ { - 1 } } ^ { x _ { 1 } } f ( x ) d x = 2 h f ( x _ { 0 } ) + { \frac { h ^ { 3 } } { 3 } } f ^ { \prime \prime } ( \xi ) , \quad { \mathrm { w h e r e } } \quad x _ { - 1 } < \xi < x _ { 1 } .
$$

${ n = 1 }$ ：

$$
\int _ { x _ { - 1 } } ^ { x _ { 2 } } f ( x ) d x = { \frac { 3 h } { 2 } } [ f ( x _ { 0 } ) + f ( x _ { 1 } ) ] + { \frac { 3 h ^ { 3 } } { 4 } } f ^ { \prime \prime } ( \xi ) , \quad \mathrm { w h e r e } \quad x _ { - 1 } < \xi < x _ { 2 } .
$$

$n = 2 \colon$

$$
\int _ { x - 1 } ^ { x _ { 3 } } f ( x ) d x = { \frac { 4 h } { 3 } } [ 2 f ( x _ { 0 } ) - f ( x _ { 1 } ) + 2 f ( x _ { 2 } ) ] + { \frac { 1 4 h ^ { 5 } } { 4 5 } } f ^ { ( 4 ) } ( \xi ) ,
$$

n = 3:

$$
\int _ { x _ { - 1 } } ^ { x _ { 4 } } f ( x ) d x = { \frac { 5 h } { 2 4 } } \lbrack 1 1 f ( x _ { 0 } ) + f ( x _ { 1 } ) + f ( x _ { 2 } ) + 1 1 f ( x _ { 3 } ) \rbrack + { \frac { 9 5 } { 1 4 4 } } h ^ { 5 } f ^ { ( 4 ) } ( \xi ) ,
$$

# EXAMPLE 2

Using the closed and open Newton-Cotes formulas listed as (4.23)-(4.26) and (4.27)- （4.30) to approximate $\begin{array} { r } { \int _ { 0 } ^ { \pi / 4 } \sin x \ d x \ = \ 1 - \sqrt { 2 } / 2 \approx \ 0 . 2 9 2 8 9 3 2 2 } \end{array}$ gives the results in Table 4.8.

# Table 4.8

<table><tr><td>n</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td>Closed formulas</td><td></td><td>0.27768018</td><td>0.29293264</td><td>0.29291070</td><td>0.29289318</td></tr><tr><td>Error</td><td></td><td>0.01521303</td><td>0.00003942</td><td>0.00001748</td><td>0.00000004</td></tr><tr><td>Open formulas</td><td>0.30055887</td><td>0.29798754</td><td>0.29285866</td><td>0.29286923</td><td></td></tr><tr><td>Error</td><td>0.00766565</td><td>0.00509432</td><td>0.00003456</td><td>0.00002399</td><td></td></tr></table>

# EXERCISE SET 4.3

1.Approximate the following integrals using the Trapezoidal rule.

a. $\begin{array} { r l } & { \displaystyle \int _ { 0 . 5 } ^ { 1 } x ^ { 4 } d x } \\ & { \displaystyle \int _ { 1 } ^ { 1 . 5 } x ^ { 2 } \ln { x } d x } \\ & { \displaystyle \int _ { 1 } ^ { 1 . 6 } \frac { 2 x } { x ^ { 2 } - 4 } d x } \\ & { \displaystyle \int _ { 0 } ^ { \pi / 4 } x \sin { x } d x } \end{array}$ $\begin{array} { r l } { \mathbf { b } . } & { { } \displaystyle \int _ { 0 } ^ { 0 . 5 } \frac { 2 } { x - 4 } d x } \\ { \mathbf { d } . } & { { } \displaystyle \int _ { 0 } ^ { 1 } x ^ { 2 } e ^ { - x } d x } \\ { \mathbf { f } . } & { { } \displaystyle \int _ { 0 } ^ { 0 . 5 } \frac { 2 } { x ^ { 2 } - 4 } d x } \\ { \mathbf { h } . } & { { } \displaystyle \int _ { 0 } ^ { \pi / 4 } e ^ { 3 x } \sin 2 x d , } \end{array}$ c.   
e.   
g

2.Find abound for the error in Exercise 1 using the error formula,and compare this to the actual error.

3. Repeat Exercise 1 using Simpson's rule.

4.Repeat Exercise 2 using Simpson's rule and the results of Exercise 3.

5.Repeat Exercise 1 using the Midpoint rule.

6.Repeat Exercise 2 using the Midpoint rule and the results of Exercise 5.

7.The Trapezoidal rule applied to $\textstyle { \int _ { 0 } ^ { 2 } f ( x ) \ d x }$ gives the value 4, and Simpson's rule gives the value 2. What is $f ( 1 ) ?$

3The Trapezoidal rule applied to $\textstyle { \int _ { 0 } ^ { 2 } f ( x ) d x }$ gives the value 5,and the Midpointrule gives the value 4. What value does Simpson's rule give?

9.Find the degree of precision of the quadrature formula

$$
\int _ { - 1 } ^ { 1 } f ( x ) d x = f \left( - { \frac { \sqrt { 3 } } { 3 } } \right) + f \left( { \frac { \sqrt { 3 } } { 3 } } \right) .
$$

10.Let $h \neq ( b - a ) / 3 , x _ { 0 } = a , x _ { 1 } = a + h$ ,and $x _ { 2 } = b$ . Find the degree of precision of the quadrature formula

$$
\int _ { a } ^ { b } f ( x ) d x = { \frac { 9 } { 4 } } h f ( x _ { 1 } ) + { \frac { 3 } { 4 } } h f ( x _ { 2 } ) .
$$

11. The quadrature formula $\textstyle { \int _ { - 1 } ^ { 1 } f ( x ) d x } = c _ { 0 } f ( - 1 ) + c _ { 1 } f ( 0 ) + c _ { 2 } f ( 1 )$ is exact for all polynomials of degree lessthan or equal to2. Determine $c _ { 0 } , c _ { 1 }$ ,and $c _ { 2 }$ ，

12. The quadrature formula $\begin{array} { r } { \int _ { 0 } ^ { 2 } f ( x ) d x = c _ { 0 } f ( 0 ) + c _ { 1 } f ( 1 ) + c _ { 2 } f ( 2 ) } \end{array}$ is exact for all polynomials of degree lessthan an equal to 2. Determine $c _ { 0 } , c _ { 1 }$ ,and $c _ { 2 }$

13. Find the constants $c _ { 0 } , c _ { 1 }$ ,and $x _ { 1 }$ so that the quadrature formula

$$
\int _ { 0 } ^ { 1 } f ( x ) d x = c _ { 0 } f ( 0 ) + c _ { 1 } f ( x _ { 1 } )
$$

has the highest possible degree of precision.

14.Find the constants $x _ { 0 } , x _ { 1 }$ ,and $c _ { 1 }$ so that the quadrature formula

$$
\int _ { 0 } ^ { 1 } f ( x ) d x = { \frac { 1 } { 2 } } f ( x _ { 0 } ) + c _ { 1 } f ( x _ { 1 } )
$$

has the highest possible degree of precision.

15. Approximate the following integrals using formulas (4.23) through (4.30). Are the accuracies of the approximations consistent withthe error formulas? Which of parts (d)and (e)give the better approximation?

a. $\begin{array} { l } { \displaystyle \int _ { 0 } ^ { 0 . 1 } \sqrt { 1 + x } \ d x } \\ { \displaystyle \int _ { 1 . 1 } ^ { 1 . 5 } e ^ { x } \ d x } \\ { \displaystyle \int _ { 1 } ^ { 5 . 5 } \frac { 1 } { x } \ d x + \int _ { 5 . 5 } ^ { 1 0 } \frac { 1 } { x } \ d x } \end{array}$ $\begin{array} { r l } { \mathbf { b } . \ } & { \displaystyle \int _ { 0 } ^ { \pi / 2 } ( \sin x ) ^ { 2 } d x } \\ { \mathbf { d } . \ } & { \displaystyle \int _ { 1 } ^ { 1 0 } \frac { 1 } { x } \ d x } \\ { \mathbf { f } . \ } & { \displaystyle \int _ { 0 } ^ { 1 } x ^ { 1 / 3 } d x } \end{array}$   
c.   
e.

16.Given the function $f$ at the following values,

<table><tr><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>1.8</td><td rowspan=1 colspan=1>2.0</td><td rowspan=1 colspan=1>2.2</td><td rowspan=1 colspan=1>2.4</td><td rowspan=1 colspan=1>2.6</td></tr><tr><td rowspan=1 colspan=1>f(x）</td><td rowspan=1 colspan=1>3.12014</td><td rowspan=1 colspan=1>4.42569</td><td rowspan=1 colspan=1>6.04241</td><td rowspan=1 colspan=1>8.03014</td><td rowspan=1 colspan=1>10.46675</td></tr></table>

approximate $\textstyle \int _ { 1 . 8 } ^ { 2 . 6 } f ( x ) d x$ using alltheappropriate quadrature formulasof tissection.

17.Suppose the data of Exercise 16 have roundoff errors given by the following table.

$$
\frac { x } { \mathrm { E r r o r } i n f ( x ) }  \begin{array} { l } { 1 . 8 } \\ { 2 \times 1 0 ^ { - 6 } } \end{array}  \begin{array} { l } { 2 . 0 } \\ { - 2 \times 1 0 ^ { - 6 } } \end{array}  \begin{array} { l } { 2 . 2 } \\ { - 0 . 9 \times 1 0 ^ { - 6 } } \end{array}  \begin{array} { l } { 2 . 4 } \\ { - 0 . 9 \times 1 0 ^ { - 6 } } \end{array}  \begin{array} { l } { 2 . 6 } \\ { 2 \times 1 0 ^ { - 6 } } \end{array}
$$

Calculate the errors due to roundoff in Exercise 16.

18.Derive Simpson's rule with error term by using

$$
\int _ { x _ { 0 } } ^ { x _ { 2 } } f ( x ) d x = a _ { 0 } f ( x _ { 0 } ) + a _ { 1 } f ( x _ { 1 } ) + a _ { 2 } f ( x _ { 2 } ) + k f ^ { ( 4 ) } ( \xi ) .
$$

Find $a _ { 0 } , a _ { 1 }$ , and ${ \pmb a } _ { 2 }$ from the fact that Simpson's rule is exact for $f ( x ) = x ^ { n }$ when $n = 1 , 2$ and 3. Then find $k$ by applying the integration formula with $f ( x ) = x ^ { 4 }$

19.Prove the statement folowing Definition4.1: that is,show that aquadrature formula has degree of precision $\pmb { n }$ if and only if the error $E ( P ( x ) ) = 0$ for all polynomials $P ( x )$ of degree $k =$ $0 , 1 , \ldots , n$ ,but $E ( P ( x ) ) \neq 0$ for some polynomial $P ( x )$ of degree $n + 1$

20.Derive Simpson's three-eighths rule,Eq. (4.25), with error term bythe use of Theorem 4.2.

21.Derive Eq. (4.28) with error term by the use of Theorem 4.3.

# 4.4 Composite Numerical Integration

The Newton-Cotes formulas are generally unsuitable for use over large integration intervals.High-degree formulas would be required, and the values of the coefficients in these formulas are difficult to obtain. Also,the Newton-Cotes formulas are based on interpola-tory polynomials that use equally spaced nodes, a procedure that is inaccurate over large intervals because of the oscillatory nature of high-degree polynomials. In this section, we discuss a piecewise approach to numerical integration that uses the low-order Newton-Cotes formulas. These are the techniques most often applied.

Consider finding an approximation to $\int _ { 0 } ^ { 4 } e ^ { x } d x$ . Simpson's rule with $h = 2$ gives

$$
\int _ { 0 } ^ { 4 } e ^ { x } \ d x \approx { \frac { 2 } { 3 } } ( e ^ { 0 } + 4 e ^ { 2 } + e ^ { 4 } ) = 5 6 . 7 6 9 5 8 .
$$

Since the exact answer in this case is $e ^ { 4 } - e ^ { 0 } = 5 3 . 5 9 8 1 5$ ,the error-3.17143 isfar larger than we would normally accept.

To apply a piecewise technique to this problem, divide [0,4] into [O,2] and [2,4]and use Simpson's rule twice with $h = 1$ . This gives

$$
{ \begin{array} { r l } & { \displaystyle \int _ { 0 } ^ { 4 } e ^ { x } \ d x = \int _ { 0 } ^ { 2 } e ^ { x } \ d x + \int _ { 2 } ^ { 4 } e ^ { x } \ d x } \\ & { \qquad \approx { \frac { 1 } { 3 } } [ e ^ { 0 } + 4 e + e ^ { 2 } ] + { \frac { 1 } { 3 } } [ e ^ { 2 } + 4 e ^ { 3 } + e ^ { 4 } ] } \\ & { \qquad = { \frac { 1 } { 3 } } [ e ^ { 0 } + 4 e + 2 e ^ { 2 } + 4 e ^ { 3 } + e ^ { 4 } ] } \\ & { \qquad = 5 3 . 8 6 3 8 5 . } \end{array} }
$$

The error has been reduced to -0.26570. Encouraged by our results, we subdivide the intervals [0,2]and[2,4]and use Simpson’s rule with $\begin{array} { r } { h = \frac { 1 } { 2 } } \end{array}$ ,giving

$$
\begin{array} { r l } & { \displaystyle \int _ { 0 } ^ { 4 } e ^ { x } \ d x = \int _ { 0 } ^ { 1 } e ^ { x } \ d x + \int _ { 1 } ^ { 2 } e ^ { x } \ d x + \int _ { 2 } ^ { 3 } e ^ { x } \ d x + \int _ { 3 } ^ { 4 } e ^ { x } \ d x } \\ & { \qquad \approx \displaystyle \frac { 1 } { 6 } [ e _ { 0 } + 4 e ^ { 1 / 2 } + e ] + \frac { 1 } { 6 } [ e + 4 e ^ { 3 / 2 } + e ^ { 2 } ] } \\ & { \qquad + \frac { 1 } { 6 } [ e ^ { 2 } + 4 e ^ { 5 / 2 } + e ^ { 3 } ] + \frac { 1 } { 6 } [ e ^ { 3 } + 4 e ^ { 7 / 2 } + e ^ { 4 } ] } \\ & { \qquad = \displaystyle \frac { 1 } { 6 } [ e ^ { 0 } + 4 e ^ { 1 / 2 } + 2 e + 4 e ^ { 3 / 2 } + 2 e ^ { 2 } + 4 e ^ { 5 / 2 } + 2 e ^ { 3 } + 4 e ^ { 7 / 2 } + e ^ { 4 } ] } \\ & { \qquad = 5 3 6 1 6 2 2 . } \end{array}
$$

The error for this approximation is -0.01807.

To generalize this procedure, choose an even integer n. Subdivide the interval $[ a , b ]$ into $n$ subintervals,and apply Simpson's rule on each consecutive pair of subintervals. (See Figure 4.7 on page 198.) With $h = ( b - a ) / n$ and $x _ { j } = a + j h$ , for each $j = 0 , 1 , \ldots , n ,$ we have

$$
\begin{array} { l } { \displaystyle \int _ { a } ^ { b } f ( x ) d x = \sum _ { j = 1 } ^ { n / 2 } \int _ { x _ { 2 j - 2 } } ^ { x _ { 2 j } } f ( x ) d x } \\ { \displaystyle = \sum _ { j = 1 } ^ { n / 2 } \left\{ \frac { h } { 3 } [ f ( x _ { 2 j - 2 } ) + 4 f ( x _ { 2 j - 1 } ) + f ( x _ { 2 j } ) ] - \frac { h ^ { 5 } } { 9 0 } f ^ { ( 4 ) } ( \xi _ { j } ) \right\} , } \end{array}
$$

for some $\xi _ { j }$ with $x _ { 2 j - 2 } < \xi _ { j } < x _ { 2 j }$ , provided that $f \in C ^ { 4 } [ a , b ]$ . Using the fact that, for each $j = 1$ ,2.，...,， $( n / 2 ) - 1$ , we have $f ( x _ { 2 j } )$ appearing in the term corresponding to the

![](images/91ce7d7a1bb79c1be6f308f313c7ccd7063b4d6ec2763acd17f58e861137c954.jpg)  
Figure 4.7

interval $[ x _ { 2 j - 2 } , x _ { 2 j } ]$ and also in the term corresponding to the interval $[ x _ { 2 j } , x _ { 2 j + 2 } ]$ , we can reduce this sum to

$$
f ( x ) d x = { \frac { h } { 3 } } \left[ f ( x _ { 0 } ) + 2 \sum _ { j = 1 } ^ { ( n / 2 ) - 1 } f ( x _ { 2 j } ) + 4 \sum _ { j = 1 } ^ { n / 2 } f ( x _ { 2 j - 1 } ) + f ( x _ { n } ) \right] - { \frac { h ^ { 5 } } { 9 0 } } \sum _ { j = 1 } ^ { n / 2 } f ^ { ( 4 ) } ( \xi _ { j } ) ,
$$

The error associated with this approximation is

$$
E ( f ) = - { \frac { h ^ { 5 } } { 9 0 } } \sum _ { j = 1 } ^ { n / 2 } f ^ { ( 4 ) } ( \xi _ { j } ) ,
$$

where $x _ { 2 j - 2 } < \xi _ { j } < x _ { 2 j }$ , for each $j = 1 , 2 , \dots , n / 2$

f $f \in C ^ { 4 } [ a , b ]$ , the Extreme Value Theorem implies that $f ^ { ( 4 ) }$ assumes its maximum and minimum in $[ a , b ]$ . Since

$$
\operatorname* { m i n } _ { x \in [ a , b ] } f ^ { ( 4 ) } ( x ) \leq f ^ { ( 4 ) } ( \xi _ { j } ) \leq \operatorname* { m a x } _ { x \in [ a , b ] } f ^ { ( 4 ) } ( x ) ,
$$

we have

$$
{ \frac { n } { 2 } } \operatorname* { m i n } _ { x \in [ a , b ] } f ^ { ( 4 ) } ( x ) \leq \sum _ { j = 1 } ^ { n / 2 } f ^ { ( 4 ) } ( \xi _ { j } ) \leq { \frac { n } { 2 } } \operatorname* { m a x } _ { x \in [ a , b ] } f ^ { ( 4 ) } ( x )
$$

and

$$
\operatorname* { m i n } _ { x \in [ a , b ] } f ^ { ( 4 ) } ( x ) \leq \frac { 2 } { n } \sum _ { j = 1 } ^ { n / 2 } f ^ { ( 4 ) } ( \xi _ { j } ) \leq \operatorname* { m a x } _ { x \in [ a , b ] } f ^ { ( 4 ) } ( x ) .
$$

By the Intermediate Value Theorem, there is a $\mu \in ( a , b )$ such that

$$
f ^ { ( 4 ) } ( \mu ) = \frac { 2 } { n } \sum _ { j = 1 } ^ { n / 2 } f ^ { ( 4 ) } ( \xi _ { j } ) .
$$

Thus,

$$
E ( f ) = - { \frac { h ^ { 5 } } { 9 0 } } \sum _ { j = 1 } ^ { n / 2 } f ^ { ( 4 ) } ( \xi _ { j } ) = - { \frac { h ^ { 5 } } { 1 8 0 } } n f ^ { ( 4 ) } ( \mu ) ,
$$

or, since $h = ( b - a ) / n$ ，

$$
E ( f ) = - \frac { ( b - a ) } { 1 8 0 } h ^ { 4 } f ^ { ( 4 ) } ( \mu ) .
$$

These observations produce the following result.

# Theorem 4.4

Let $f \in C ^ { 4 } [ a , b ]$ ， $n$ be even, $h = ( b - a ) / n$ , and $x _ { j } = a + j h$ , for each $j = 0 , 1 , \ldots , n$ There exists a $\mu \in ( a , b )$ for which the Composite Simpson's rule for $\pmb { n }$ subintervals can be written with its error term as

$$
{ \bf \Sigma } _ { \textit { t } } ^ { \star \star } ( x ) ~ d x = \frac { h } { 3 } \left[ f ( a ) + 2 \ \sum _ { j = 1 } ^ { ( n / 2 ) - 1 } f ( x _ { 2 j } ) + 4 \sum _ { j = 1 } ^ { n / 2 } f ( x _ { 2 j - 1 } ) + f ( b ) \right] - \frac { b - a } { 1 8 0 } h ^ { 4 } f ^ { ( 4 ) } ( 1 ) ,
$$

Algorithm 4.1 uses the Composite Simpson's rule on $n$ subintervals. This is the most frequently used general-purpose quadrature algorithm.

# Composite Simpson's Rule

To approximate the integral $\textstyle I = \int _ { a } ^ { b } f ( x ) d x$ ：

INPUTendpoints $a , b$ ; even positive integer $n$

OUTPUT approximation $X I$ to $I$ ·

Step 1 Set $h = ( b - a ) / n$

Step 2 Set $\begin{array} { l } { { X I 0 = f ( a ) + f ( b ) ; } } \\ { { X I 1 = 0 ; \quad ( S u m m a t i o n \ o f f ( x _ { 2 i - 1 } ) . ) } } \\ { { X I 2 = 0 . \quad ( S u m m a t i o n \ o f f ( x _ { 2 i } ) . ) } } \end{array}$

Step 3For $i = 1$ ,... , n - 1 do Steps 4 and 5.

Step 4 Set $X = a + i h$

Step 5If $\Dot { \iota }$ is even then set $X I 2 = X I 2 + f ( X )$ else set $X I 1 = X I 1 + f ( X )$ .

Step 6Set $X I = h ( X I 0 + 2 \cdot X I 2 + 4 \cdot X I 1 ) / 3 .$

Step 7 OUTPUT $( X I )$ ；STOP.

The subdivision approach can be applied to any of the Newton-Cotes formulas. The extensions of the Trapezoidal (see Figure 4.8) and Midpoint rules are given without proof. Since the Trapezoidal rule requires only one interval for each application, the integer n can be either odd or even.

![](images/0e0d130088b30fee461f37792e48deded73639d8f9948f4fd48e7173f51ed8d2.jpg)  
Figure 4.8

# Theorem 4.5

Let $f \in C ^ { 2 } [ a , b ]$ ， $h = ( b - a ) / n$ , and $x _ { j } = a + j h$ , for each $j = 0 , 1 , \ldots , n$ . There exists a $\mu \in ( a , b )$ for which the Composite Trapezoidal rule for $\pmb { n }$ subintervals can be written with its error term as

$$
\int _ { a } ^ { b } f ( x ) d x = { \frac { h } { 2 } } \left[ f ( a ) + 2 \sum _ { j = 1 } ^ { n - 1 } f ( x _ { j } ) + f ( b ) \right] - { \frac { b - a } { 1 2 } } h ^ { 2 } f ^ { \prime \prime } ( \mu ) .
$$

For the Composite Midpoint rule, $\pmb { n }$ must again be even. (See Figure 4.9.)

![](images/35f72fb9fd5d18e26132c6f2f56a237268e90742dfc17154b3c465c46911a865.jpg)  
Figure 4.9

# Theorem 4.6

Let $f \in C ^ { 2 } [ a , b ]$ ， $\pmb { n }$ be even, $h = ( b - a ) / ( n + 2 )$ ，and $x _ { j } = a + ( j + 1 ) h$ for each $j = - 1 , 0 , \dots , n + 1$ . There exists a $\mu \in ( a , b )$ for which the Composite Midpoint rule for $n + 2$ subintervals can be written with its error term as

$$
\int _ { a } ^ { b } f ( x ) d x = 2 h \sum _ { j = 0 } ^ { n / 2 } f ( x _ { 2 j } ) + { \frac { b - a } { 6 } } h ^ { 2 } f ^ { \prime \prime } ( \mu ) .
$$

Consider approximating $\textstyle { \int _ { 0 } ^ { \pi } \sin x \ d x }$ with an absolute error less than O.00002, using the Composite Simpson's rule. The Composite Simpson's rule gives, for some $\mu$ in $( 0 , \pi )$ ，

$$
\int _ { 0 } ^ { \pi } \sin { x } d x = { \frac { h } { 3 } } \left[ 2 \sum _ { j = 1 } ^ { ( n / 2 ) - 1 } \sin { x _ { 2 j } } + 4 \sum _ { j = 1 } ^ { n / 2 } \sin { x _ { 2 j - 1 } } \right] - { \frac { \pi h ^ { 4 } } { 1 8 0 } } \sin { \mu } .
$$

Since the absolute error is to be less than O.0oo02,the inequality

$$
\left| { \frac { \pi h ^ { 4 } } { 1 8 0 } } \sin \mu \right| \leq { \frac { \pi h ^ { 4 } } { 1 8 0 } } = { \frac { \pi ^ { 5 } } { 1 8 0 n ^ { 4 } } } < 0 . 0 0 0 0 2
$$

is used to determine $\pmb { n }$ and $h$ . Completing these calculations gives $n \geq 1 8$ .If $n = 2 0$ ,then $h = \pi / 2 0$ , and the formula gives

$$
\int _ { 0 } ^ { \pi } \sin x d x \approx { \frac { \pi } { 6 0 } } \left[ 2 \sum _ { j = 1 } ^ { 9 } \sin \left( { \frac { j \pi } { 1 0 } } \right) + 4 \sum _ { j = 1 } ^ { 1 0 } \sin \left( { \frac { ( 2 j - 1 ) \pi } { 2 0 } } \right) \right] = 2 . 0 0 0 0 0 6 .
$$

To be assured of this degree of accuracy using the Composite Trapezoidal rule requires that

$$
\left| \frac { \pi h ^ { 2 } } { 1 2 } \sin \mu \right| \leq \frac { \pi h ^ { 2 } } { 1 2 } = \frac { \pi ^ { 3 } } { 1 2 n ^ { 2 } } < 0 . 0 0 0 0 2 ,
$$

or that $n \geq 3 6 0$ . Since this is many more calculations than are needed for the Composite Simpson's rule, we would not want to use the Composite Trapezoidal rule on this problem. For comparison purposes,the Composite Trapezoidal rule with $n = 2 0$ and $h = \pi / 2 0$ gives

$$
\int _ { 0 } ^ { \pi } \sin x d x \approx { \frac { \pi } { 4 0 } } \left[ 2 \sum _ { j = 1 } ^ { 1 9 } \sin \left( { \frac { j \pi } { 2 0 } } \right) + \sin 0 + \sin \pi \right] = { \frac { \pi } { 4 0 } } \left[ 2 \sum _ { j = 1 } ^ { 1 9 } \sin \left( { \frac { j \pi } { 2 0 } } \right) \right]
$$

The exact answer is 2, so Simpson's rule with $n = 2 0$ gave an answer well within the required error bound, whereas the Trapezoidal rule with $n = 2 0$ clearly did not. □

Most CAS incorporate both the Composite Simpson's rule and the Composite Trape-Zoidal Rule. In Maple,you first accessto the library where they are defined by entering

>with(student);

The calls for the methods are trapezoid(f , $x = a \cdot ( b , n )$ and simpson(f $x = a , \cdot b , n )$ For our example,

>f:=sin(x);

$$
f : = \sin ( x )
$$

>trapezoid(f, $\mathbf { \Delta x } { = } 0$ ..Pi,20);

$$
{ \frac { 1 } { 2 0 } } \pi \left( \sum _ { i = 1 } ^ { 1 9 } s \mathrm { i n } \left( { \frac { 1 } { 2 0 } } i \pi \right) \right)
$$

>evalf(%) ;

1.995885974

>evalf(simpson(f, $x = 0$ ..Pi,20));

2.000006785

The Composite Midpoint rule is also in the Maple library and can be accessed with the command

>evalf(middlesum(f, $\mathbf { x } { = } 0$ ...Pi,10));

which gives the approximation 2.0o8248408.

To demonstrate Maple code for the midpoint method, we define $f ( x ) , a , b , n$ and $h$ with the commands

$$
\begin{array} { r l } & { \mathrm { > \mathbf { f } : = \mathbf { x } \mathrm { - } > \mathbf { s } i n \left( \mathbf { x } \right) ~ ; } } \\ & { \mathrm { > \mathbf { a } : = 0 ~ ; ~ \mathbf { b } : = \mathrm { P i } ~ ; ~ \mathbf { n } : = 1 8 ; ~ \mathbf { h } : = \left( b \mathrm { - } \mathbf { a } \right) / \left( n + 2 \right) ; } } \end{array}
$$

We also need a variable to calculate the running sum, which we initialize to 0.

>Tot : $\mathtt { \Omega } = 0$ ；

In Maple the counter-controlled loop is defined by

for loop control variable from initial-value to terminal value do statement; statement; ： statement;   
od;

We set the loop control variable $j$ , which begins at O and goes to $n / 2 = 9$ in steps of 1. For each value of $j = 0 , 1 , \ldots , 9$ the loop is traversed and each calculation inside the loop is performed until the word od is encountered. The reserved words involved are for,from, to,do,and od.Note that no semicolon $( ; )$ follows the do statement.

$>$ for j from O to n/2 do $> \mathbf { \Delta x } \mathbf { j } : = \mathbf { a } + ( 2 * \mathbf { j } + 1 ) * \mathbf { h }$ ； $>$ Tot:=evalf(Tot+f(xj)) >od;

This produces a series of results culminating in the final summation

$$
T o t = \sum _ { j = 0 } ^ { n / 2 } f ( x _ { 2 j } ) = \sum _ { j = 0 } ^ { 9 } f ( x _ { 2 j } ) = 6 . 3 9 2 4 5 3 2 2 2 .
$$

We then multiply by $2 h$ to finish the Composite Midpoint method:

>Tot: evalf(2\*h\*Tot);

$$
T o t : = 2 . 0 0 8 2 4 8 4 0 8
$$

An important property shared by all the composite integration techniques is a stabil-ity with respect to roundoff error. To demonstrate this, suppose we apply the Composite Simpson's rule with $\pmb { n }$ subintervals to a function $f$ on $[ a , b ]$ and determine the maximum bound for the roundoff error. Assume that $f ( x _ { i } )$ is approximated by $\tilde { f } ( x _ { i } )$ and that

$$
f ( x _ { i } ) = \tilde { f } ( x _ { i } ) + e _ { i } , \quad \mathrm { f o r e a c h } i = 0 , 1 , \ldots , n ,
$$

where $e _ { i }$ denotes the roundoff error associated with using $\tilde { f } ( x _ { i } )$ to approximate $f ( x _ { i } )$ Then the accumulated error, $e ( h )$ , in the Composite Simpson's rule is

$$
\begin{array} { r l r } {  { e ( h ) = | \frac { h } { 3 } [ e _ { 0 } + 2 \sum _ { j = 1 } ^ { ( n / 2 ) - 1 } e _ { 2 j } + 4 \sum _ { j = 1 } ^ { n / 2 } e _ { 2 j - 1 } + e _ { n } ] | } } \\ & { } & { \leq \frac { h } { 3 } [ | e _ { 0 } | + 2 \sum _ { j = 1 } ^ { ( n / 2 ) - 1 } | e _ { 2 j } | + 4 \sum _ { j = 1 } ^ { n / 2 } | e _ { 2 j - 1 } | + | e _ { n } | ] . } \end{array}
$$

If the roundoff errors are uniformly bounded by $\pmb \varepsilon$ ,then

$$
e ( h ) \leq { \frac { h } { 3 } } \left[ \varepsilon + 2 \left( { \frac { n } { 2 } } - 1 \right) \varepsilon + 4 \left( { \frac { n } { 2 } } \right) \varepsilon + \varepsilon \right] = { \frac { h } { 3 } } 3 n \varepsilon = n h \varepsilon .
$$

But $n h = b \sim a$ ,so

$$
e ( h ) \leq ( b - a ) \varepsilon ,
$$

a bound independent of $h$ (and $\pmb { n }$ ). This means that, even though we may need to divide an interval into more parts to ensure accuracy, the increased computation that is required does not increase the roundoff error. This result implies that the procedure is stable as $h$ approaches zero. Recallthat this was not true of the numerical differentiation procedures considered at the beginning of this chapter.

# Exercise Set 4.4

1. Use the Composite Trapezoidal rule with the indicated values of $\pmb { n }$ to approximate the follow. ing integrals.

$$
\begin{array} { l l l l l } { { { \displaystyle \int _ { 1 } ^ { 2 } x \ln x d x , } } } & { { n = 4 } } & { { \mathrm { ~ } } } & { { { \mathrm { ~  ~ { ~ \cal ~ h . ~ } ~ } } } } & { { \int _ { - 2 } ^ { 2 } x ^ { 3 } e ^ { x } d x , } } & { { n = 4 } } \\ { { \displaystyle \int _ { 0 } ^ { 2 } { \frac { 2 } { x ^ { 2 } + 4 } d x } , } } & { { n = 6 } } & { { \mathrm { ~  ~ { ~ \cal ~ d . ~ } ~ } } } & { { \int _ { 0 } ^ { \pi } x ^ { 2 } \cos x d x , } } & { { n = 6 } } \\ { { \displaystyle \int _ { 0 } ^ { 2 } e ^ { 2 x } \sin 3 x d x , } } & { { n = 8 } } & { { \mathrm { ~  ~ { ~ \cal ~ L ~ } ~ } } } & { { \int _ { 1 } ^ { 3 } { \frac { x } { x ^ { 2 } + 4 } d x } , } } & { { n = 8 } } \\ { { \displaystyle \int _ { 3 } ^ { 5 } { \frac { 1 } { \sqrt { x ^ { 2 } - 4 } } d x } , } } & { { n = 8 } } & { { \mathrm { ~  ~ { ~ \cal ~ h . ~ } ~ } } } & { { \int _ { 0 } ^ { 3 \pi / 8 } \mathrm { t a n } x d x , } } & { { n = 8 } } \end{array}
$$

2.Use the Composite Simpson's rule to approximate the integrals in Exercise 1.

3.Use the Composite Midpoint rule with $n + 2$ subintervals to approximate the integrals ir Exercise 1.

4.Approximate $\textstyle \int _ { 0 } ^ { 2 } x ^ { 2 } e ^ { - x ^ { 2 } } d x$ using $h = 0 . 2 5$

a. Use the Composite Trapezoidal rule.   
b. Use the Composite Simpson's rule.   
c. Use the Composite Midpoint rule.

5. Suppose that $f ( 0 ) = 1 , f ( 0 . 5 ) = 2 . 5 , f ( 1 ) = 2 ,$ and $f ( 0 . 2 5 ) = f ( 0 . 7 5 ) = \alpha$ . Find $\pmb { \alpha }$ if the Composite Trapezoidal rule with $n = 4$ gives the value 1.75 for $\textstyle \int _ { 0 } ^ { 1 } f ( x ) d x$

6. The Midpoint rule for approximating $\textstyle \int _ { - 1 } ^ { 1 } f ( x ) d x$ gives the value 12,the Composite Midpoint rule with $n = 2$ gives 5,and Composite Simpson's rule gives 6. Use the fact that $f ( - 1 ) =$ $f ( 1 )$ and $f ( - 0 . 5 ) = f ( 0 . 5 ) - 1$ to determine $f ( - 1 ) , f ( - 0 . 5 ) , f ( 0 ) , f ( 0 . 5 ) ,$ and $f ( 1 )$

7.Determine the values of $\pmb { n }$ and $h$ required to approximate

$$
\int _ { 0 } ^ { 2 } e ^ { 2 x } \sin 3 x d x
$$

to within $1 0 ^ { - 4 }$

a. Use the Composite Trapezoidal rule.   
b. Use the Composite Simpson's rule.   
c. Use the Composite Midpoint rule.

8.Repeat Exercise 7 for the integral $\textstyle { \int _ { 0 } ^ { \pi } x ^ { 2 } \cos x d x }$

9.Determine the values of $\pmb { n }$ and $h$ required to approximate

$$
\int _ { 0 } ^ { 2 } { \frac { 1 } { x + 4 } } d x
$$

to within $1 0 ^ { - 5 }$ and compute the approximation.

a. Use the Composite Trapezoidal rule.   
$\mathbf { b } _ { \bullet }$ Use the Composite Simpson's rule.   
c. Use the Composite Midpoint rule.

10.Repeat Exercise 9 for the integral $\textstyle \int _ { 1 } ^ { 2 } x \ln x d x$

11.Let $f$ be defined by

$$
f ( x ) = \left\{ \begin{array} { l l } { x ^ { 3 } + 1 , } & { 0 \leq x \leq 0 . 1 , } \\ { 1 . 0 0 1 + 0 . 0 3 ( x - 0 . 1 ) + 0 . 3 ( x - 0 . 1 ) ^ { 2 } + 2 ( x - 0 . 1 ) ^ { 3 } , } & { 0 . 1 \leq x \leq 0 . 2 , } \\ { 1 . 0 0 9 + 0 . 1 5 ( x - 0 . 2 ) + 0 . 9 ( x - 0 . 2 ) ^ { 2 } + 2 ( x - 0 . 2 ) ^ { 3 } , } & { 0 . 2 \leq x \leq 0 . 3 . } \end{array} \right.
$$

a. Investigate the continuity of the derivatives of $f$   
$\mathbf { b } .$ Use the Composite Trapezoidal rule with $n = 6$ to approximate $\begin{array} { r } { \int _ { 0 } ^ { 0 . 3 } f ( x ) d x } \end{array}$ , and esti-mate the error using the error bound.   
c. Use the Composite Simpson's rule with $n = 6$ to approximate $\textstyle { \int _ { 0 } ^ { 0 . 3 } f ( x ) \ d x }$ . Are the results more accurate than in part (b)?

12.Show that the error $E ( f )$ for Composite Simpson's rule can be approximated by

$$
- { \frac { h ^ { 4 } } { 1 8 0 } } [ f ^ { \prime \prime \prime } ( b ) - f ^ { \prime \prime \prime } ( a ) ] .
$$

[Hint: $\textstyle \sum _ { j = 1 } ^ { n / 2 } f ^ { ( 4 ) } ( \xi _ { j } ) ( 2 h )$ is a Riemann Sum for $\textstyle \int _ { a } ^ { b } f ^ { ( 4 ) } ( x ) d x . ]$

13.a.Derive an estimate for $E ( f )$ in the Composite Trapezoidal rule using the method in Exercise 12. b. Repeat part (a) for the Composite Midpoint rule.

l4.Use the error estimates of Exercises 12 and 13 to estimate the errors in Exercise 8.

15.Use the error estimates of Exercises 12 and 13 to estimate the errors in Exercise 10.

16.In multivariable calculus and in statistics courses it is shown that

$$
\int _ { - \infty } ^ { \infty } \frac { 1 } { \sigma \sqrt { 2 \pi } } e ^ { - ( 1 / 2 ) ( x / \sigma ) ^ { 2 } } d x = 1 ,
$$

for any positive $\pmb { \sigma }$ . The function

$$
f ( x ) = { \frac { 1 } { \sigma { \sqrt { 2 \pi } } } } e ^ { - ( 1 / 2 ) ( x / \sigma ) ^ { 2 } }
$$

is the normal density function with mean $\mu = 0$ and standard deviation $\pmb { \sigma }$ . The probability that a randomly chosen value described by this distribution lies in $[ a , b ]$ is given by $\textstyle { \int _ { a } ^ { b } f ( x ) } d x$ Approximate to within $1 0 ^ { - 5 }$ the probability that a randomly chosen value described by this distribution will lie in

a. $[ - \sigma , \sigma ]$ $\begin{array} { r l } { \mathbf { b } . \ } & { { } [ - 2 \sigma , 2 \sigma ] } \end{array}$ $\mathrm { ~ \texttt ~ { ~ c ~ } ~ } [ - 3 \sigma , 3 \sigma ]$

17.Determine to within $1 0 ^ { - 6 }$ the length of the graph of the elipse with equation $4 x ^ { 2 } + 9 y ^ { 2 } = 3 6$

18.A car laps a race track in 84 seconds. The speed of the car at each 6-second interval is determined using a radar gun and is given from the beginning of the lap,in feet/second, by the entries in the following table.

$$
\begin{array}{c} \begin{array}{c} \frac { \mathrm { T i m e } } { \mathbf { S p e c d } } \ \left| \begin{array} { l } { 0 } \\ { 1 2 4 } \end{array} \right| \ 1 2 \ \left| \begin{array} { l } { 1 8 } \\ { 1 4 8 } \end{array} \right| \ 1 4 7 \ \left| \begin{array} { l } { 3 4 } \\ { 1 3 3 } \end{array} \right| \ 3 0  \end{array} \ \left| \begin{array} { l } { 3 6 } \\ { 1 2 1 } \end{array} \right| \ 4 2 \ \left| \begin{array} { l } { 4 8 } \\ { 8 } \end{array} \right| \ 5 4 \ \left| \begin{array} { l } { 6 0 } \\ { 6 8 } \end{array} \right| \ 6 6 \ \left| \begin{array} { l } { 7 2 } \\ { 7 8 } \end{array} \right| \ 7 8  \end{array} \right| \ 8 4 \ \left| \begin{array} { l } { 8 4 } \\ { 1 2 3 } \end{array}
$$

How long is the track?

19.A particle of mass $m$ moving through a fluid is subjected to a viscous resistance $R$ , which is a function of the velocity $\pmb { v }$ . The relationship between the resistance $R$ , velocity $\pmb { \nu }$ , and time $t$ is given by the equation

$$
t = \int _ { v ( t _ { 0 } ) } ^ { v ( t ) } { \frac { m } { R ( u ) } } d u .
$$

Suppose that $R ( v ) = - v \sqrt { v }$ for a particular fuid, where $R$ is in newtons and $\pmb { \nu }$ is in meters/second. If $m = 1 0 \mathrm { k g }$ and $v ( 0 ) = 1 0 \mathrm { m } / s$ , approximate the time required for the particle to slow to $\nu = 5 ~ \mathrm { m } / \mathrm { s }$

20.To simulate the thermal characteristics of disk brakes (see the following figure), D.A. Secrist and R. W. Hombeck [SH] needed to approximate numerically the “area averaged lining temperature," $T$ ,of the brake pad from the equation

$$
T = \frac { \displaystyle \int _ { r _ { e } } ^ { r _ { 0 } } T ( r ) r \theta _ { p } d r } { \displaystyle \int _ { r _ { e } } ^ { r _ { 0 } } r \theta _ { p } d r } ,
$$

where $r _ { e }$ represents the radius at which the pad-disk contact begins, $r _ { 0 }$ represents the outside radius of the pad-disk contact, $\theta _ { p }$ represents the angle subtended by the sector brake pads, and $T ( r )$ is the temperature at each point of the pad, obtained numerically from analyzing the heat

equation (see Section 12.2). Suppose $r _ { e } = 0 . 3 0 8$ ft, $r _ { 0 } = 0 . 4 7 8$ ft, $\theta _ { p } = 0 . 7 0 5 1$ radians, and the temperatures given in the following table have been calculated at the various points on the disk. Approximate $\pmb { T }$

<table><tr><td>r (ft)</td><td>T(r)(F)</td><td>r (ft)</td><td>T(r)(F)</td><td>r(ft)</td><td>T(r) (oF)</td></tr><tr><td>0.308</td><td>640</td><td>0.376</td><td>1034</td><td>0.444</td><td>1204</td></tr><tr><td>0.325</td><td>794</td><td>0.393</td><td>1064</td><td>0.461</td><td>1222</td></tr><tr><td>0.342</td><td>885</td><td>0.410</td><td>1114</td><td>0.478</td><td>1239</td></tr><tr><td>0.359</td><td>943</td><td>0.427</td><td>1152</td><td></td><td></td></tr></table>

![](images/6afdd0d9465178e7ab434368e8990533d54e522e4ea97672adc74ef4658c8d08.jpg)

21.Find an approximation to within $1 0 ^ { - 4 }$ of the value of the integral considered in the application opening this chapter:

$$
\int _ { 0 } ^ { 4 8 } \sqrt { 1 + ( \cos x ) ^ { 2 } } d x .
$$

22. The equation

$$
\int _ { 0 } ^ { x } { \frac { 1 } { \sqrt { 2 \pi } } } e ^ { - t ^ { 2 } / 2 } d t = 0 . 4 5
$$

can be solved for $\pmb { x }$ by using Newton's method with

$$
f ( x ) = \int _ { 0 } ^ { x } { \frac { 1 } { \sqrt { 2 \pi } } } e ^ { - t ^ { 2 } / 2 } d t - 0 . 4 5
$$

and

$$
f ^ { \prime } ( x ) = { \frac { 1 } { \sqrt { 2 \pi } } } e ^ { - x ^ { 2 } / 2 } .
$$

To evaluate $f$ at the approximation $p _ { k }$ , we need a quadrature formula to approximate

$$
\int _ { 0 } ^ { p _ { k } } { \frac { 1 } { \sqrt { 2 \pi } } } e ^ { - t ^ { 2 } / 2 } d t .
$$

a. Find a solution to $f ( x ) = 0$ accurate to within $1 0 ^ { - 5 }$ using Newton's method with $p _ { 0 } =$ 0.5 and the Composite Simpson's rule.   
b. Repeat (a) using the Composite Trapezoidal rule in place of the Composite Simpson's rule.

# 4.5 Romberg Integration

Romberg integration uses the Composite Trapezoidal rule to give preliminary approximations and then applies the Richardson extrapolation process to improve the approximations. Recall from Section 4.2 that Richardson extrapolation can be performed on any approximation procedure of the form

$$
M - N ( h ) = K _ { 1 } h + K _ { 2 } h ^ { 2 } + \cdot \cdot \cdot + K _ { n } h ^ { n } ,
$$

where the $K _ { 1 } , K _ { 2 } , \ldots , K _ { n }$ are constants and $N ( h )$ is an approximation to the unknown value $M$ . The truncation error in this formula is dominated by $K _ { 1 } h$ when $h$ is small, so this formula gives $O ( h )$ approximations. Richardson's extrapolation uses an averaging technique to produce formulas with higher-order truncation error. In Section 4.2 we saw how this could be used to produce derivative approximations. In this section we will use extrapolation to approximate definite integrals.

To begin the presentation of the Romberg integration scheme, recall that the Composite Trapezoidal rule for approximating the integral of a function $f$ on an interval $[ a , b ]$ using $m$ subintervals is

$$
\int _ { a } ^ { b } f ( x ) d x = { \frac { h } { 2 } } \left[ f ( a ) + f ( b ) + 2 \sum _ { j = 1 } ^ { m - 1 } f ( x _ { j } ) \right] - { \frac { ( b - a ) } { 1 2 } } h ^ { 2 } f ^ { \prime \prime } ( \mu ) ,
$$

where $a < \mu < b , h = ( b - a ) / m$ and $x _ { j } = a + j h$ ,for each $j = 0 , 1 , \ldots , m$

We first obtain Composite Trapezoidal rule approximations with $m _ { 1 } = 1$ ， $m _ { 2 } = 2$ ， $m _ { 3 } = 4 , \dots$ ，and $m _ { n } = 2 ^ { n - 1 }$ , where $\pmb { n }$ is a positive integer. The step size $h _ { k }$ corresponding to $m _ { k }$ is $h _ { k } = ( b - a ) / m _ { k } = ( b - a ) / 2 ^ { k - 1 }$ .With this notation the Trapezoidal rule becomes

$$
\int _ { a } ^ { b } f ( x ) d x = { \frac { h _ { k } } { 2 } } \left[ f ( a ) + f ( b ) + 2 \left( \sum _ { i = 1 } ^ { 2 ^ { k - 1 } - 1 } f ( a + i h _ { k } ) \right) \right] - { \frac { ( b - a ) } { 1 2 } } h _ { k } ^ { 2 } f ^ { \prime \prime } ( \mu _ { k } ) ,
$$

where $\mu _ { k }$ is a number in $( a , b )$

If the notation $R _ { k , 1 }$ is introduced to denote the portion of Eq.(4.31) used for the trapezoidal approximation, then

$$
\begin{array} { l } { \displaystyle { R _ { 1 , 1 } = \frac { h _ { 1 } } { 2 } [ f ( a ) + f ( b ) ] = \frac { ( b - a ) } { 2 } [ f ( a ) + f ( b ) ] ; } } \\ { \displaystyle { R _ { 2 , 1 } = \frac { h _ { 2 } } { 2 } [ f ( a ) + f ( b ) + 2 f ( a + h _ { 2 } ) ] } } \end{array}
$$

$$
\begin{array} { c } { { \displaystyle = \frac { ( b - a ) } { 4 } \left[ f ( a ) + f ( b ) + 2 f \left( a + \frac { ( b - a ) } { 2 } \right) \right] } } \\ { { \displaystyle } } \\ { { \displaystyle = \frac { 1 } { 2 } [ R _ { 1 , 1 } + h _ { 1 } f ( a + h _ { 2 } ) ] ; } } \\ { { \displaystyle } } \\ { { R _ { 3 , 1 } = \frac { 1 } { 2 } \{ R _ { 2 , 1 } + h _ { 2 } [ f ( a + h _ { 3 } ) + f ( a + 3 h _ { 3 } ) ] \} ; } } \end{array}
$$

and, in general (see Figure 4.10),

$$
R _ { k , 1 } = \frac { 1 } { 2 } \left[ \mathcal { R } _ { k - 1 , 1 } + h _ { k - 1 } \sum _ { i = 1 } ^ { 2 ^ { k - 2 } } f \left( a + ( 2 i - 1 ) h _ { k } \right) \right] ,
$$

for each $k = 2 , 3 , \ldots , n$ .(See Exercises 12 and 13.)

![](images/4df924a481d71054241e45582df160e6044cbe706fe65676f71adcdf277df2a9.jpg)  
Figure 4.10

# EXAMPLE 1

Using Eq. (4.32) to perform the first step of the Romberg integration scheme for approximating $\int _ { 0 } ^ { \pi } \sin x \ d x$ with $\hbar = 6$ leads to the equations

$$
\begin{array} { l } { { R _ { 1 , 1 } = { \displaystyle \frac { \pi } { 2 } } [ \sin 0 + \sin \pi ] = 0 ; } } \\ { { R _ { 2 , 1 } = { \displaystyle \frac { 1 } { 2 } } \left[ R _ { 1 , 1 } + \pi \sin { \displaystyle \frac { \pi } { 2 } } \right] = 1 . 5 7 0 7 9 6 3 3 ; } } \\ { { R _ { 3 , 1 } = { \displaystyle \frac { 1 } { 2 } } \left[ R _ { 2 , 1 } + { \displaystyle \frac { \pi } { 2 } } \left( \sin { \displaystyle \frac { \pi } { 4 } } + \sin { \displaystyle \frac { 3 \pi } { 4 } } \right) \right] = 1 . 8 9 6 1 1 8 9 0 ; } } \\ { { R _ { 4 , 1 } = { \displaystyle \frac { 1 } { 2 } } \left[ R _ { 3 , 1 } + { \displaystyle \frac { \pi } { 4 } } \left( \sin { \displaystyle \frac { \pi } { 8 } } + \sin { \displaystyle \frac { 3 \pi } { 8 } } + \sin { \displaystyle \frac { 5 \pi } { 8 } } + \sin { \displaystyle \frac { 7 \pi } { 8 } } \right) \right] = 1 . 9 7 4 2 3 1 6 0 . } } \\ { { R _ { 5 , 1 } = 1 . 9 9 3 5 7 0 3 4 . \quad \mathrm { a n d } \quad R _ { 6 , 1 } = 1 . 9 9 8 3 9 3 3 6 , } } \end{array}
$$

Since the correct value for the integral in Example 1 is 2, the convergence is quite slow. Richardson extrapolation will be used to speed the convergence.

It can be shown,although not easily (see [RR, pp.136-138), that if $f \in C ^ { \cdot \infty } \{ a , b \} .$ the Composite Trapezoidal rule can be writen with an alternative error term in the form

$$
\int _ { a } ^ { b } f ( x ) d x - R _ { k , 1 } = \sum _ { i = 1 } ^ { \infty } K _ { i } h _ { k } ^ { 2 i } = K _ { 1 } h _ { k } ^ { 2 } + \sum _ { i = 2 } ^ { \infty } K _ { i } h _ { k } ^ { 2 i } ,
$$

where each $K _ { i }$ is independent of $h _ { k }$ and depends only on $f ^ { ( 2 i - 1 ) } ( a )$ and $f ^ { ( 2 i - 1 ) } ( b )$

With theComposite Trapezoidal rule in this form, we can eliminate the term involving $h _ { k } ^ { 2 }$ by combining this equation with its counterpart with $h _ { k }$ replaced by $h _ { k + 1 } = h _ { k } / 2$ ,giving

$$
\int _ { a } ^ { b } f ( x ) d x - R _ { k + 1 , 1 } = \sum _ { i = 1 } ^ { \infty } K _ { i } h _ { k + 1 } ^ { 2 i } = \sum _ { i = 1 } ^ { \infty } { \frac { K _ { i } h _ { k } ^ { 2 i } } { 2 ^ { 2 i } } } = { \frac { K _ { 1 } h _ { k } ^ { 2 } } { 4 } } + \sum _ { i = 2 } ^ { \infty } { \frac { K _ { i } h _ { k } ^ { 2 i } } { 4 ^ { i } } } .
$$

Subtracting Eq. (4.33) from 4 times (4.34) and simplifying gives the $O ( h _ { k } ^ { 4 } )$ formula

$$
\begin{array} { r } { \int _ { a } ^ { b } f ( x ) d x - \left[ R _ { k + 1 , 1 } + \frac { R _ { k + 1 , 1 } - R _ { k , 1 } } { 3 } \right] = \displaystyle \sum _ { i = 2 } ^ { \infty } \frac { K _ { i } } { 3 } \left( \frac { h _ { k } ^ { 2 i } } { 4 ^ { i - 1 } } - h _ { k } ^ { 2 i } \right) } \\ { = \displaystyle \sum _ { i = 2 } ^ { \infty } \frac { K _ { i } } { 3 } \left( \frac { 1 - 4 ^ { i - 1 } } { 4 ^ { i - 1 } } \right) h _ { k } ^ { 2 i } . } \end{array}
$$

Extrapolation can then be applied to this formula to obtain an $O ( h _ { k } ^ { 6 } )$ result, and so on. To simplify the notation we define

$$
R _ { k , 2 } = R _ { k , 1 } + { \frac { R _ { k , 1 } - R _ { k - 1 , 1 } } { 3 } } ,
$$

for each $k = 2 , 3 , \ldots , n$ ,and apply the Richardson extrapolation procedure to these values. Continuing this notation, we have, for each $k = 2 , 3 , 4 , \dots , n$ and $j = 2 , \ldots , k$ an $O ( h _ { k } ^ { 2 j } )$ approximation formula defined by

$$
R _ { k , j } = R _ { k , j - 1 } + \frac { R _ { k , j - 1 } - R _ { k - 1 , j - 1 } } { 4 ^ { j - 1 } - 1 } .
$$

The results that are generated from these formulas are shown in Table 4.9.

# Table 4.9

<table><tr><td>R1.1 R2.！</td><td>R2.2</td><td></td><td></td><td></td></tr><tr><td>R3.1 R4.1</td><td>R3.2 R4.2</td><td>R3.3 R4.3</td><td>R4.4</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Rn.1</td><td></td><td></td><td>Rn.4</td><td></td></tr><tr><td></td><td>Rn.2</td><td>Rn.3</td><td></td><td></td></tr></table>

The Romberg technique has tho additional desirable feature that it allows an entire new row in the table to be calculated by doing one additional application of the Composite Trapezoidal rule. Then it uses an averaging of the previously calculated values to obtain the

succeeding entries in the row. The method used to construct a table of this type calculates the entries row by row, that is,in the order $R _ { 1 , 1 } , R _ { 2 , 1 } , R _ { 2 , 2 } , R _ { 3 , 1 } , R _ { 3 , 2 } , R _ { 3 , 3 }$ ,etc. Algorithm 4.2 describes this technique in detail.

# Romberg

To approximate the integral $\begin{array} { r } { I = \int _ { a } ^ { b } f ( x ) d x } \end{array}$ , select an integer $n > 0$

INPUT endpoints $a , b ;$ integer $\pmb { n }$

OUTPUTan array $R$ (Compute $R$ by rows: onlythe last2rows are saved.in storge.)

Step 1 Set $h = b - a$ ；$\begin{array} { r } { R _ { 1 . 1 } = \frac { h } { 2 } ( f ( a ) + f ( b ) ) . } \end{array}$

Step 2 OUTPUT $( R _ { 1 , 1 } )$

Step 3For $i = 2 , \ldots , n$ do Steps 4-8.

$S t e p ~ 4 ~ \mathrm { { S e t } } ~ R _ { 2 , 1 } = \frac { 1 } { 2 } \left[ R _ { 1 , 1 } + h \sum _ { k = 1 } ^ { 2 ^ { i - 2 } } f ( a + ( k - 0 . 5 ) h ) \right] .$ (Approximation from Trapezoidal method.)

Step 5 For j =2,...,i s $\mathrm { e t } \ R _ { 2 , j } = R _ { 2 , j - 1 } + { \frac { R _ { 2 , j - 1 } - R _ { 1 , j - 1 } } { 4 ^ { j - 1 } - 1 } }$ (Extrapolation.)

Step 6OUTPUT $( R _ { 2 , j }$ for $j = 1 , 2 , \dots , i )$

Step 7 Set $h = h / 2$

Step 8 For  =1,2....,i set $R _ { 1 , j } = R _ { 2 , j }$ (Update row 1 of R.) Step 9 STOP.

In Example 1, the values for $R _ { 1 , 1 }$ through $R _ { 6 , 1 }$ were obtained for approximating $\int _ { 0 } ^ { \pi } \sin x d x$ With Algorithm 4.2, the Romberg table is shown in Table 4.10. ■

Although there are 2l entries in the table,only the six in the first column require function evaluations since these are the only entries generated by the integration technique. The other entries are obtained by an averaging process.

Table 4.10   

<table><tr><td>0</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>1,57079633</td><td>2.09439511</td><td></td><td></td><td></td><td></td></tr><tr><td>1.89611890</td><td>2.00455976</td><td>1.99857073</td><td></td><td></td><td></td></tr><tr><td>1.97423160</td><td>2.00026917</td><td>1.99998313</td><td>2.00000555</td><td></td><td></td></tr><tr><td>1.99357034</td><td>2.00001659</td><td>1.99999975</td><td>2.00000001</td><td>1.99999999</td><td></td></tr><tr><td>1.99839336</td><td>2.00000103</td><td>2.00000000</td><td>2.00000000</td><td>2.00000000</td><td>2.00000000</td></tr></table>

Algorithm 4.2 requires a preset integer $n$ to determine the number of rows to be gen-erated. We could also set an error tolerance for the approximation and generate $n$ .within some upper bound, until consecutive diagonal entries $R _ { \cdots 1 , n - 1 }$ and $R _ { n , \mu }$ agree to within the tolerance. To guard against the possibility that two consecutive row clements agree with each other but not with the value of the integral being approximated, it is common to generate approximations until not only $R _ { n - 1 , n - 1 } \ - \ R _ { n , n } \}$ is within the tolerance. but also $\mid R _ { n - 2 , n - 2 } - R _ { n - 1 , n - 1 } \mid$ . Although not a universal safeguard, this will ensure that two differ-ently generated sets of approximations agree within the specified tolerance before $R _ { \mathit { t i } , \mathit { t i } }$ is accepted as sufficiently accurate.

Romberg integration applied to $f$ on $\{ a , b \}$ relies on the assumption that the Composite Trapezoidal rule has an error term that can be expressed in the form of Eq. (4.33): that is. we must have $f \in C ^ { 2 k + 2 } [ a , b ]$ for the $k$ th row to be generated. General-purpose algorithms using Romberg integration include a check at each stage to ensure that this assumption is fulfilled. These methods are known as cautious Romberg algorithms and are described in [Johl. This reference also describes methods for using the Romberg technique as an adaptive procedure, similar to the adaptive Simpson's rule that will be discussed in Section 4.6.

# EXERCisE SEt 4.5

1.Use Romberg integration to compute $R _ { \mathrm { : : } }$ for the following integrals.

a $\begin{array} { r l } { * } & { { } \int _ { 1 } ^ { 1 5 } x ^ { 2 } \ln x d x } \\ { * } & { { } \int _ { 0 } ^ { 2 3 5 } \displaystyle { \frac { 2 } { x ^ { 2 } - 4 } } d x } \\ { * } & { { } \int _ { 0 } ^ { \pi / 4 } e ^ { 3 x } \sin 2 x d x } \\ { * } & { { } \int _ { 3 } ^ { 3 . 5 } \displaystyle { \frac { x } { \sqrt { x ^ { 2 } - 4 } } } d x } \end{array}$ $\begin{array} { r l } { { \bf b . \ } } & { { } \displaystyle \int _ { 0 } ^ { 1 6 } x ^ { \frac { 3 } { 2 } } e ^ { - \nu } \ d x } \\ { { \bf d . \ } } & { { } \displaystyle \int _ { 0 } ^ { \pi / 4 } x ^ { \frac { 3 } { 2 } } \sin x \ d x } \\ { { \bf f . \ } } & { { } \displaystyle \int _ { 1 } ^ { 1 6 } \frac { 2 x } { x ^ { \frac { 3 } { 2 } } - 4 } \ d x } \\ { { \bf h . \ } } & { { } \displaystyle \int _ { 0 } ^ { \pi / 4 } \ c \cos x ^ { 2 } d x } \end{array}$   
0   
6   
g

2.Calculate $R _ { 4 , 4 }$ for the integrals in Exercise 1.

3.Use Romberg integration to approximate the integrals in Exercise 1 to within $1 ( ) ^ { \cdot \cdot \ell }$ . Compute the Romberg table until either $\mid R _ { n \mathrm { ~ \tiny ~ \cdot ~ } \mid , n - 1 } \ : - \ : R _ { n , n } \mid < 1 0 ^ { - 6 }$ ，or $n = 1 0$ . Compare your results to the exact values of the integrals.

4.Apply Rombcrg integration to the following integrals until $R _ { n - 1 \cdots 1 }$ and $R , \mu _ { 1 , \mu }$ agree to within $1 0 ^ { \cdot 4 }$

d. $\begin{array} { l } { \displaystyle \int _ { 0 } ^ { 1 } x ^ { 1 / 3 } d x } \\ { \displaystyle \int _ { 0 } ^ { 0 . > } f ( x ) d x , \quad \mathrm { \ w h e r c } } \end{array}$   
b.

$$
f ( x ) = \left\{ \begin{array} { l l } { x ^ { 3 } + 1 . } & { 0 \leq x \leq 0 . 1 } \\ { 1 . 0 0 1 + 0 . 0 3 ( x - 0 . 1 ) + 0 . 3 ( x - 0 . 1 ) ^ { 2 } + 2 ( x - 0 . 1 ) ^ { 3 } , } & { 0 . 1 < x \leq 0 . 2 . } \\ { 1 . 0 0 9 + 0 . 1 5 ( x - 0 . 2 ) + 0 . 9 ( x - 0 . 2 ) ^ { 2 } + 2 ( x - 0 . 2 ) ^ { 3 } , } & { 0 . 2 < \mathscr { s } \leq 0 . 3 } \end{array} \right.
$$

5.Use the following data to approximate $\textstyle { \int _ { 1 } ^ { 5 } f ( x ) d x }$ as accurately as possiblc.

$$
\frac { x } { f ( x ) } \quad \left| { \begin{array} { l } { 1 } \\ { 2 . 4 1 4 2 } \end{array} } - \left| { \begin{array} { l } { 2 } \\ { 2 . 6 7 3 4 } \end{array} } \right| { \begin{array} { l } { 3 } \\ { 2 . 8 9 7 4 } \end{array} } \right| { \begin{array} { l } { 4 } \\ { 3 . 0 9 7 6 } \end{array} } \quad \left| { \begin{array} { l } { 5 } \\ { 3 . 2 8 0 4 } \end{array} } \right| { \begin{array} { l } { 0 } \\ { 2 . 8 9 4 } \end{array} } .
$$

6.Romberg intcgration is used to cpproximate

$$
\int _ { 0 } ^ { 1 } { \frac { x ^ { 2 } } { 1 + x ^ { 3 } } } d x .
$$

$R _ { \textrm { l i } } = 0 . 2 5 0$ and $R _ { 2 2 } = \left( \right) . 2 3 \left\uparrow 5 \right.$ ，what is $R _ { 2 1 }$ ？

7.Romberg integration is used to approximate

$$
\int _ { ? } ^ { ? } f ( x ) d x .
$$

If $f ( 2 ) = 0 . 5 1 3 4 2$ 、 $f ( 3 ) = 0 . 3 6 7 8 8 , R _ { 3 \mathord { \uparrow } } = 0 . 4 3 6 8 \tau$ ,and $R _ { 3 3 } = 0 . 4 3 6 6 3$ find $1 : 2 . 5$ ·

3.Romberg integration for approximating $\textstyle { \int _ { t \colon } ^ { 1 } f ( x ) d x }$ gives $R _ { \textrm { i j } } = 4$ and $R \sb { \textnormal { a } } = \bar { \varphi }$ .Find 1t9.

9. Romberg integrationforappoximating $\int _ { i } ^ { \cdot h } f ( x ) d x$ gives $R _ { \textrm { l l } } = 8$ $R _ { 2 2 } = \frac { 1 1 } { 3 }$ 、and $R : \quad  . \quad  . \quad $ Find $R _ { 3 1 }$

10.Use Romberg integration to compute the following approximations to

$$
\int _ { ( ) } ^ { \therefore \cdot { \mathbb { R } } } { \sqrt { 1 + ( \cos x ) ^ { 2 } } } d x .
$$

[Note: The results in this exercisc are most interesting if you are using a device with betw eep seven- and nine-digit arithmetic.1

a. Determine $R _ { \mathrm { ~ l ~ } , \mathrm { ~ l ~ } } , R _ { \mathrm { ~ 2 ~ } , \mathrm { ~ l ~ } } , R _ { \mathrm { ~ 3 ~ } , \mathrm { ~ l ~ } } , R _ { \mathrm { 4 ~ } , \mathrm { ~ l ~ } }$ 、and $R _ { 5 , 1 }$ , and use these approximations to predict the value of the integral.   
b. Determine $R _ { ? ? } , R _ { ? , ? } , R _ { 4 . 4 }$ ,and $R _ { 5 , 5 }$ , and modify your prediction.   
c. Determine $R _ { 6 , 1 } , R _ { 6 , 2 } , R _ { 6 , 3 } , R _ { 6 , 4 } , R _ { 6 , 5 }$ . and $R _ { \dot { \Theta } , \dot { \Theta } }$ ,and modify your prediction.   
d. Determine $R _ { 7 . 7 } , R _ { 8 . 8 } , R _ { 9 , 9 }$ ,and $R _ { 1 0 , 1 6 }$ , and make a final prediction.   
e. Explain why this integral causes difficulty with Romberg integration and hov 1 can be reformulated to more easily determine an accurate approximation.

11. Show that thc approximation obtained from $R _ { k , 2 }$ is the same as that given by the Compositc Simpson's rule described in Theorem 4.4 with $h = h _ { k }$

12.Show that, for any $k$

$$
\sum _ { i = 1 } ^ { 2 ^ { k - 1 } } f \left( a + { \frac { i } { 2 } } h _ { k - 1 } \right) = \sum _ { i = 1 } ^ { 2 ^ { k - 2 } } f \left( a + \left( i - { \frac { 1 } { 2 } } \right) h _ { k - 1 } \right) + \sum _ { i = 4 } ^ { 2 ^ { k } } f ( u + i h . \quad \forall i = 4 , \quad
$$

13.Use the result of Exercise 12 to vcrify Eq.(4.32): that is,show that for all $k$ 、

$$
R _ { k \cdot } : = \frac { 1 } { 2 } \left[ R _ { k - 1 , 1 } + h _ { k } ~ _ { 1 } \sum _ { i = 1 } ^ { 2 ^ { k - 2 } } f \left( a + \left( i - \frac { 1 } { 2 } \right) h _ { k } ~ _ { 1 } \right) \right] .
$$

14. In Exercise 24 of Section 1.1. a Maclaurin series was integrated to approximate erfil:. wnere erf $( . 1 )$ is the normal distribution error function defined by

$$
\operatorname { e r f } ( x ) = { \frac { 2 } { \sqrt { \pi } } } \int _ { 0 } ^ { x } e ^ { - t ^ { 2 } } d t .
$$

Approximate erf(1) to within $1 0 ^ { - 7 }$

# 4.6 Adaptive Quadrature Methods

The composite formulas require the use of equally spaced nodes. This is inappropriate when integrating a function on an interval that contains both regions with large functional variation and regions with small functional variation. If the approximation error is to be evenly distributed, a smaller step size is needed for the large-variation regions than for those with less variation. An efficient technique for this type of problem should predict the amount of functional variation and adapt the step size to the varying requirements. These methods are called Adaptive quadrature methods. The method we discuss is based on the Composite Simpson's rule, but the technique is easily modified to use other composite procedures.

Suppose that we want to approximate $\textstyle { \int _ { a } ^ { b } f ( x ) d x }$ to within a specified tolerance $\varepsilon > 0$ The first step in the procedure is to apply Simpson's rule with step size $h = ( b - a ) / 2$ This produces (see Figure 4.11)

$$
\int _ { a } ^ { b } f ( x ) d x = S ( a , b ) - { \frac { h ^ { 5 } } { 9 0 } } f ^ { ( 4 ) } ( \mu ) , \quad { \mathrm { f o r ~ s o m e ~ } } \mu { \mathrm { ~ i n ~ } } ( a , b ) ,
$$

where

$$
S ( a , b ) = \frac { h } { 3 } [ f ( a ) + 4 f ( a + h ) + f ( b ) ] .
$$

![](images/374c93b3e6e81e883ebdcf609d46ad0015e83522b7a5c79d84a4caee7a4e0d56.jpg)  
Figure 4.11

The next step is to determine an accuracy approximation that does not equire $f ^ { ( 4 ) } ( \mu )$ To do this, we apply the Composite Simpson's rule with $n = 4$ and step size $( b - a ) / 4 =$ $h / 2$ , giving

$$
\begin{array} { r l r } {  { \int _ { a } ^ { b } f ( x ) d x = \frac { h } { 6 } [ f ( a ) + 4 f ( a + \frac { h } { 2 } ) + 2 f ( a + h ) + 4 f ( a + \frac { 3 h } { 2 } ) + f ( b ) ] } } \\ & { } & { \quad \quad - ( \frac { h } { 2 } ) ^ { 4 } \frac { ( b - a ) } { 1 8 0 } f ^ { ( 4 ) } ( \tilde { \mu } ) , \ } & { ( 4 ) } \end{array}
$$

for some $\tilde { \mu }$ in $( a , b )$ . To simplify notation, let

$$
S \left( a , { \frac { a + b } { 2 } } \right) = { \frac { h } { 6 } } \left[ f ( a ) + 4 f \left( a + { \frac { h } { 2 } } \right) + f ( a + h ) \right]
$$

and

$$
S \left( { \frac { a + b } { 2 } } , b \right) = { \frac { h } { 6 } } \left[ f ( a + h ) + 4 f \left( a + { \frac { 3 h } { 2 } } \right) + f ( b ) \right] .
$$

Then Eq. (4.37) can be rewritten (see Figure 4.12)as

$$
\int _ { a } ^ { b } f ( x ) d x = S \left( a , { \frac { a + b } { 2 } } \right) + S \left( { \frac { a + b } { 2 } } , b \right) - { \frac { 1 } { 1 6 } } \left( { \frac { h ^ { 5 } } { 9 0 } } \right) f ^ { ( 4 ) } ( \tilde { \mu } ) .
$$

The error estimation is derived by assuming that $\mu \approx \tilde { \mu }$ or, more precisely, that $f ^ { ( 4 ) } ( \mu ) \approx$ $f ^ { ( 4 ) } ( \tilde { \mu } )$ ,and the success of the technique depends on the accuracy of this assumption. If it is accurate,then equating the integrals in Eqs. (4.36) and (4.38) implies that

![](images/c028556c65606dfe8aaa627c22ff1115c105fc6bcf56dc86a9171a9cd43da62b.jpg)  
Figure 4.12

$$
S \left( a , \frac { a + b } { 2 } \right) + S \left( \frac { a + b } { 2 } , b \right) - \frac { 1 } { 1 6 } \left( \frac { h ^ { 5 } } { 9 0 } \right) f ^ { ( 4 ) } ( \tilde { \mu } ) \approx S ( a , b ) - \frac { h ^ { 5 } } { 9 0 } f ^ { ( 4 ) } ( \mu ) ,
$$

so

$$
{ \frac { h ^ { 5 } } { 9 0 } } f ^ { ( 4 ) } ( \mu ) \approx { \frac { 1 6 } { 1 5 } } \left[ S ( a , b ) - S \left( a , { \frac { a + b } { 2 } } \right) - S \left( { \frac { a + b } { 2 } } , b \right) \right] .
$$

Using this estimate in Eq. (4.38) produces the error estimation

$$
{ \begin{array} { r l } & { \left| { \int _ { a } ^ { b } f ( x ) d x - S \left( a , \frac { a + b } { 2 } \right) - S \left( \frac { a + b } { 2 } , b \right) } \right| } \\ & { \qquad \approx { \frac { 1 } { 1 5 } } \left| S ( a , b ) - S \left( a , { \frac { a + b } { 2 } } \right) - S \left( { \frac { a + b } { 2 } } , b \right) \right| . } \end{array} }
$$

This result means that $S ( a , ( a + b ) / 2 ) + S ( ( a + b ) / 2 , b )$ approximates $\textstyle { \int _ { a } ^ { b } f ( x ) d x }$ about 15 times better than it agrees with the known value $S ( a , b )$ . Thus, if

$$
\left| S ( a , b ) - S \left( a , \frac { a + b } { 2 } \right) - S \left( \frac { a + b } { 2 } , b \right) \right| < 1 5 \varepsilon ,
$$

we expect to have

$$
\left| \int _ { a } ^ { b } f ( x ) d x - S \left( a , { \frac { a + b } { 2 } } \right) - S \left( { \frac { a + b } { 2 } } , b \right) \right| < \varepsilon ,
$$

and

$$
S \left( a , { \frac { a + b } { 2 } } \right) + S \left( { \frac { a + b } { 2 } } , b \right)
$$

is assumed to be a suffciently accurate approximation to $\textstyle \int _ { a } ^ { b } f ( x ) d x$

To check the accuracy of the error estimate given in (4.39)and (4.40),considerits applica. tion to the integral

$$
\int _ { 0 } ^ { \pi / 2 } \sin x d x = 1 .
$$

In this case,

$$
S \left( 0 , { \frac { \pi } { 2 } } \right) = { \frac { \pi / 4 } { 3 } } \left[ \sin 0 + 4 \sin { \frac { \pi } { 4 } } + \sin { \frac { \pi } { 2 } } \right] = { \frac { \pi } { 1 2 } } ( 2 { \sqrt { 2 } } + 1 ) = 1 . 0 0 2 2 7 9 8 7 8
$$

and

$$
{ \begin{array} { r l } & { S \left( 0 , { \frac { \pi } { 4 } } \right) + S \left( { \frac { \pi } { 4 } } , { \frac { \pi } { 2 } } \right) = { \frac { \pi / 8 } { 3 } } \left[ \sin 0 + 4 \sin { \frac { \pi } { 8 } } + 2 \sin { \frac { \pi } { 4 } } + 4 \sin { \frac { 3 \pi } { 8 } } + \sin { \frac { \pi } { 2 } } \right] } \\ & { \qquad = 1 . 0 0 0 1 3 4 5 8 5 , } \end{array} }
$$

S0

$$
\frac { 1 } { 1 5 } \left| S \left( 0 , \frac { \pi } { 2 } \right) - S \left( 0 , \frac { \pi } { 4 } \right) - S \left( \frac { \pi } { 4 } , \frac { \pi } { 2 } \right) \right| = 0 . 0 0 0 1 4 3 0 2 0 .
$$

This closely approximates the actual error,

$$
\left| \int _ { 0 } ^ { \pi / 2 } \sin { x } d x - 1 . 0 0 0 1 3 4 5 8 5 \right| = 0 . 0 0 0 1 3 4 5 8 5 ,
$$

even though $D _ { x } ^ { 4 } \sin x = \sin x$ varies significantly in the interval $( 0 , \pi / 2 )$ ·

When the approximations in (4.39) differ by more than $1 5 \varepsilon$ , we apply the Simpson's rule technique individually to the subintervals $[ a , ( a + b ) / 2 ]$ and $[ ( a + b ) / 2 , b ]$ . Then we use the error estimation procedure to determine if the approximation to the integral on each subinterval is within a tolerance of $\varepsilon / 2$ . If so,we sum the approximations to produce an approximation to $\textstyle { \int _ { a } ^ { b } f ( x ) d x }$ within the tolerance $\varepsilon$

If the approximation on one of the subintervals fails to be within the tolerance $\varepsilon / 2$ ,that subinterval is itself subdivided,and the procedure is reapplied to the two subintervals to determine if the approximation on each subinterval is accurate to within $\varepsilon / 4$ . This halving procedure is continued until each portion is within the required tolerance.Although problems can be constructed for which this tolerance will never be met, the technique is usually successful, because each subdivision typically increases the accuracy of the approximation by a factor of 16 while requiring an increased accuracy factor of only 2.

Algorithm 4.3 details this Adaptive quadrature procedure for Simpson's rule,although some technical difficulties arise that require the implementation to differ slightly from the preceding discussion.For example, in Step 1 the tolerance has been set at $1 0 \varepsilon$ rather than the $1 5 \varepsilon$ figure in Inequality (4.39). This bound is chosen conservatively to compensate for error in the assumption $f ^ { ( 4 ) } ( \mu ) \approx f ^ { ( 4 ) } ( { \tilde { \mu } } )$ . In problems where $f ^ { ( 4 ) }$ is known to be widely varying, you should lower this bound even further.

The procedure listed in the algorithm first approximates the integral on the leftmost subinterval in a subdivision. This requires the efficient storing and recalling of previously computed functional evaluations for the nodes in the right half subintervals. Steps 3,4, and 5 contain a stacking procedure with an indicator to keep track of the data that will be required for calculating the approximation on the subinterval immediately adjacent and to the right of the subinterval on which the approximation is being generated. The method is easier to implement on a computer using a recursive programming language.

# Adaptive Quadrature

To approximate the integral $\textstyle I = \int _ { a } ^ { b } f ( x ) d x$ to within a given tolerance:

INPUT endpoints $a , b$ ；tolerance TOL; limit $N$ to number of levels.

OUTPUTapproximation $A P P$ or message that $N$ is exceeded.

Step 1 Set $A P P = 0$ ；$\begin{array} { r c l } { { } } & { { } } & { { \dot { \iota } = 1 ; } } \\ { { } } & { { } } & { { T O L _ { i } = 1 0 T O L ; } } \end{array}$

$\begin{array} { r l } & { a _ { i } = a ; } \\ & { h _ { i } = ( b - a ) / 2 ; } \\ & { F A _ { i } = f ( a ) ; } \\ & { F C _ { i } = f ( a + h _ { i } ) ; } \\ & { F B _ { i } = f ( b ) ; } \\ & { S _ { i } = h _ { i } ( F A _ { i } + 4 F C _ { i } + F B _ { i } ) / 3 ; } \\ & { L _ { i } = 1 . } \end{array}$ (Approximation from Simpson's method for entire interval.)

Step 2 While $i > 0$ do Steps 3-5.

Step 3Set $\begin{array} { r l } & { F D = f ( a _ { i } + h _ { i } / 2 ) ; } \\ & { F E = f ( a _ { i } + 3 h _ { i } / 2 ) ; } \\ & { S 1 = h _ { i } ( F A _ { i } + 4 F D + F C _ { i } ) / 6 . } \end{array}$ (Approximations from Simpson's method for halves of subintervals.) $\begin{array} { r l } & { S 2 = h _ { i } ( F C _ { i } + 4 F E + F B _ { i } ) / 6 ; } \\ & { v _ { 1 } = a _ { i } ; \quad ( S a v e d a t a t h i s l e v e l . ) } \\ & { v _ { 2 } = F A _ { i } ; } \\ & { v _ { 3 } = F C _ { i } ; } \\ & { v _ { 4 } = F B _ { i } ; } \\ & { v _ { 5 } = h _ { i } ; } \\ & { v _ { 6 } = T O L _ { i } ; } \\ & { v _ { 7 } = S _ { i } ; } \\ & { v _ { 8 } = L _ { i } . } \end{array}$

Step 4 Set $i = i - 1$ .(Delete the level.)

If $| S 1 + S 2 - v _ { 7 } | < v _ { 6 }$ then set $A P P = A P P + ( S 1 + S 2 )$ else i $\dot { \mathbf { \eta } } ( v _ { 8 } \geq N )$ then OUTPUT(LEVEL EXCEEDED')；(Procedure fails.) STOP. else(Add one level.) set $i = i + 1$ ；(Data for right half subinterval.) $a _ { i } = v _ { 1 } + v _ { 5 } .$ ； $F A _ { i } = v _ { 3 }$ ； $F C _ { i } = F E ;$ $F B _ { i } = v _ { 4 } ;$ hi = v5/2; $T O L _ { i } = { v _ { \mathrm { { 6 } } } } / { 2 } ;$ $S _ { i } = S 2$ ： $L _ { i } = v _ { 8 } + 1 $ set $i = i + 1$ ；(Data for left half subinterval.) $\begin{array} { r l } & { a _ { i } = v _ { 1 } ; } \\ & { F A _ { i } = v _ { 2 } ; } \\ & { F C _ { i } = F D ; } \\ & { F B _ { i } = v _ { 3 } ; } \\ & { h _ { i } = h _ { i - 1 } ; } \end{array}$

$$
\begin{array} { l } { T O L _ { i } = T O L _ { i - 1 } ; } \\ { S _ { i } = S 1 ; } \\ { L _ { i } = L _ { i - 1 } . } \end{array}
$$

Step 6OUTPUT $( A P P )$ ；(APP approximates I to within TOL.) STOP.

# EXAMPLE 2

The graph of the function $f ( x ) = ( 1 0 0 / x ^ { 2 } ) \sin ( 1 0 / x )$ for $x$ in [1,3] is shown in Figure 4.13. Using the Adaptive Quadrature Algorithm 4.3 with tolerance $1 0 ^ { - 4 }$ to approximate $\textstyle { \int _ { 1 } ^ { 3 } f ( x ) d x }$ produces -1.426014, a result that is accurate to within $1 . 1 \times 1 0 ^ { - 5 }$ . The approximation required that Simpson's rule with $n = 4$ be performed on the 23 subintervals whose endpoints are shown on the horizontal axis in Figure 4.13. The total number of functional evaluations required for this approximation is 93.

![](images/7ff1cccc111648907a91751ec20a3f1fad3346227315f007c384078734c8f800.jpg)  
Figure 4.13

The largest value of $h$ for which the standard Composite Simpson's rule gives $1 0 ^ { - 4 }$ accuracy is $\begin{array} { r } { h \ = \ \frac { 1 } { 8 8 } } \end{array}$ . This application requires 177 function evaluations, nearly twice as many as Adaptive quadrature.

# Exercise sEt 4.6

1. Compute the Simpson's rule approximations $S ( a , b ) , S ( a , ( a + b ) / 2 )$ ,and $S ( ( a + b ) / 2 , b )$ for the following integrals,and verify the estimate given in the approximation formula.

a. ${ \begin{array} { r l } & { \int _ { 1 } ^ { 1 . 5 } x ^ { 2 } \ln x d x } \\ & { \int _ { 0 } ^ { 0 . 3 5 } { \frac { 2 } { x ^ { 2 } - 4 } } d x } \\ & { \int _ { 0 } ^ { \pi / 4 } e ^ { 3 x } \sin 2 x d x } \\ & { \int _ { 3 } ^ { 3 . 5 } { \frac { x } { { \sqrt { x ^ { 2 } - 4 } } } } d x } \end{array} }$ $\begin{array} { r l } { { \bf b . } } & { { } { \displaystyle \int _ { 0 } ^ { 1 } x ^ { 2 } e ^ { - x } d x } } \\ { { \bf d . } } & { { } { \displaystyle \int _ { 0 } ^ { \pi / 4 } x ^ { 2 } \sin x d x } } \\ { { \bf f . } } & { { } { \displaystyle \int _ { 1 } ^ { 1 . 6 } \frac { 2 x } { x ^ { 2 } - 4 } d x } } \\ { { \bf h . } } & { { } { \displaystyle \int _ { 0 } ^ { \pi / 4 } ( \cos x ) ^ { 2 } d x } } \end{array}$ c.   
e.   
g

2. Use Adaptive quadrature to find approximations to within $1 0 ^ { - 3 }$ for the integrals in Exercise 1. Do not use a computer program to generate these results.

3.Use Adaptive quadrature to approximate the following integrals to within $1 0 ^ { - 5 }$

$$
\begin{array} { l l } { { \displaystyle \int _ { 1 } ^ { 3 } e ^ { 2 x } \sin 3 x d x \qquad } } & { { \mathrm { ~ b . ~ } \displaystyle \int _ { 1 } ^ { 3 } e ^ { 3 x } \sin 2 x d x } } \\ { { \displaystyle \int _ { 0 } ^ { 5 } \left[ 2 x \cos ( 2 x ) - ( x - 2 ) ^ { 2 } \right] d x \qquad } } & { { \mathrm { ~ d . ~ } \displaystyle \int _ { 0 } ^ { 5 } \left[ 4 x \cos ( 2 x ) - ( x - 2 ) ^ { 2 } \right] d x } } \end{array}
$$

4. Use Simpson's Composite rule with $n = 4 , 6 , 8 , \ldots$ ，until successive approximations to the following integrals agree to within $1 0 ^ { - 6 }$ . Determine the number of nodes required. Use the Adaptive Quadrature Algorithm to approximate the integral to within $1 0 ^ { - 6 }$ , and count the number of nodes. Did Adaptive quadrature produce any improvement?

a.. $\begin{array} { l } { \displaystyle \int _ { 0 } ^ { \pi } { x \cos x ^ { 2 } d x } } \\ { \displaystyle \int _ { 0 } ^ { \pi } { x ^ { 2 } \cos x d x } } \end{array}$ $\begin{array} { c } { { \displaystyle { \bf b . } \int _ { 0 } ^ { \pi } x \sin x ^ { 2 } d x } } \\ { { { \bf d . } \int _ { 0 } ^ { \pi } x ^ { 2 } \sin x d x } } \end{array}$   
c.

5. Sketch the graphs of sin $( 1 / x )$ and $\cos ( 1 / x )$ on [0.1,2]. Use Adaptive quadrature to approximate the integrals

$$
\int _ { 0 . 1 } ^ { 2 } \sin { \frac { 1 } { x } } \ d x \quad { \mathrm { a n d } } \quad \int _ { 0 . 1 } ^ { 2 } \cos { \frac { 1 } { x } } \ d x
$$

to within $1 0 ^ { - 3 }$

6.Let $T ( a , b )$ and $\begin{array} { r } { T ( a , \frac { a + b } { 2 } ) + T ( \frac { a + b } { 2 } , b ) } \end{array}$ be the single and double applications of the Trapezoidal rule to $\textstyle \int _ { a } ^ { b } f ( x ) d x$ . Derive the relationship between

$$
\left| T ( a , b ) - T \left( a , { \frac { a + b } { 2 } } \right) - T \left( { \frac { a + b } { 2 } } , b \right) \right| ^ { . }
$$

and

$$
\left| \int _ { a } ^ { b } f ( x ) d x - T \left( a , { \frac { a + b } { 2 } } \right) - T \left( { \frac { a + b } { 2 } } , b \right) \right| .
$$

7. The differential equation

$$
m u ^ { \prime \prime } ( t ) + k u ( t ) = F _ { 0 } \cos { \omega t }
$$

describes a spring-mass system with mass $m$ , spring constant $k$ ,and no applied damping. The term $F _ { 0 }$ cos ωt describes a periodic external force applied to the system. The solution to the equation when the system is initially at rest $( u ^ { \prime } ( 0 ) = u ( 0 ) = 0 )$ is

$$
u ( t ) = \frac { F _ { 0 } } { m ( \omega _ { 0 } ^ { 2 } - \omega ^ { 2 } ) } \left[ \cos \omega t - \cos \omega _ { 0 } t \right] , \quad \mathrm { w h e r e } \quad \omega _ { 0 } = \sqrt { \frac { k } { m } } \neq \omega .
$$

Sketch the graph of $\pmb { u }$ when $m = 1 , k = 9 , F _ { 0 } = 1 , \omega = 2$ and $t \in [ 0 , 2 \pi ]$ . Approximate $\textstyle \int _ { 0 } ^ { 2 \pi } u ( t ) d t$ to witin $1 0 ^ { - 4 }$

8. If the term $c u ^ { \prime } ( t )$ is added to the left sideof the motion equation in Exercise 7,theresulting differential equation describes a spring-mass system that is damped with damping constant $c \neq 0$ . The solution to this equation when the system is initially at rest is

$$
u ( t ) = c _ { 1 } e ^ { r _ { 1 } t } + c _ { 2 } e ^ { r _ { 2 } t } + \frac { F _ { 0 } } { c ^ { 2 } \omega ^ { 2 } + m ^ { 2 } ( \omega _ { 0 } ^ { 2 } - \omega ^ { 2 } ) ^ { 2 } } \left[ c \omega \sin \omega t + m \left( \omega _ { 0 } ^ { 2 } - \omega ^ { 2 } \right) \cos \omega t \right] ,
$$

where

$$
r _ { 1 } = \frac { - c + \sqrt { c ^ { 2 } - 4 \omega _ { 0 } ^ { 2 } m ^ { 2 } } } { 2 m } \quad \mathrm { a n d } \quad r _ { 2 } = \frac { - c - \sqrt { c ^ { 2 } - 4 \omega _ { 0 } ^ { 2 } m ^ { 2 } } } { 2 m } .
$$

a. Let $m = 1 , k = 9 , F _ { 0 } = 1 , c = 1 0$ ,and $\omega = 2$ .Find the values of $c _ { 1 }$ and $c _ { 2 }$ so that $u ( 0 ) = u ( 1 ) = 0$ b. Sketch the graph of $u ( t )$ for $t \in [ 0 , 2 \pi ]$ and approximate $\textstyle \int _ { 0 } ^ { 2 \pi } u ( t ) d t$ to within $1 0 ^ { - 4 }$

9.The study of light diffraction at a rectangular aperture involves the Fresnel integrals

$$
c ( t ) = \int _ { 0 } ^ { t } \cos { \frac { \pi } { 2 } } w ^ { 2 } d w \quad { \mathrm { ~ a n d ~ } } \quad s ( t ) = \int _ { 0 } ^ { t } \sin { \frac { \pi } { 2 } } w ^ { 2 } d w .
$$

Construct a table of values for $c ( t )$ and $s ( t )$ that is accurate to within $1 0 ^ { - 4 }$ for values of $t = 0 . 1 , 0 . 2 , \ldots , 1 . 0 .$

# 4.7 Gaussian Quadrature

The Newton-Cotes formulas in Section 4.3 were derived by integrating interpolating poly-nomials. Since the error term in the interpolating polynomial of degree $\pmb { n }$ involves the $( n + 1 ) \mathsf { s t }$ derivative of the function being approximated, a formula of this type is exact when approximating any polynomial of degree less than or equal to $\pmb { n }$

All the Newton-Cotes formulas use values of the function at equally-spaced points. This restriction is convenient when the formulas are combined to form the composite rules we considered in Section 4.4,but it can significantly decrease the accuracy of the approximation. Consider, for example, the Trapezoidal rule applied to determine the integrals of the functions shown in Figure 4.14.

![](images/8c937f7cb3620c26f90815a42eb0cf6a0e67e472bacdb36a5eed22bf7b46e832.jpg)  
Figure 4.14

The Trapezoidal rule approximates the integral of the function by integrating the linear function that joins the endpoints of the graph of the function.But this is not likely the best line for approximating the integral. Lines such as those shown in Figure 4.15 would likely give much better approximations in most cases.

![](images/4043d9d82250cdbd7dbe332c1e2560131eacdcb917e022d6cf21f6dfb4043c83.jpg)  
Figure 4.15

Gaussian quadrature chooses the points for evaluation in an optimal, rather than equally spaced, way. The nodes x1, x2,..., xn in the interval [a,b] and coefficients $c _ { 1 } , c _ { 2 } , \ldots , c _ { n }$ ,are chosen to minimize the expected error obtained in the approximation

$$
\int _ { a } ^ { b } f ( x ) d x \approx \sum _ { i = 1 } ^ { n } c _ { i } f ( x _ { i } ) .
$$

To measure this accuracy， we assume that the best choice of these values is that which produces the exact result for the largest class of polynomials, that is,the choice that gives the greatest degree of precision.

The coefficients $c _ { 1 } , c _ { 2 } , \ldots , c _ { n }$ in the approximation formula are arbitrary,and the nodes $x _ { 1 } , x _ { 2 } , \ldots , x _ { n }$ are restricted only by the fact that they must lie in $[ a , b ]$ , the interval of integration. This gives us $2 n$ parameters to choose.If the coefficients of a polynomial are considered parameters, the class of polynomials of degree at most $2 n - 1$ also contains $2 n$ parameters.This,then, is the largest class of polynomials for which it is reasonable to expect the formula to be exact. With the proper choice of the values and constants, exactness on this set can be obtained.

To illustrate the procedure for choosing the appropriate parameters, we willshow how to select the coefficients and nodes when $n = 2$ and the interval of integration is $\{ - 1 , 1 \}$ We willthen discuss the more general situation for an arbitrary choice of nodes and coefficients and show how the technique is modified when integrating over an arbitrary interval.

Suppose we want to determine $c _ { 1 } , c _ { 2 } , x _ { 1 }$ ,and $x _ { 2 }$ so that the integration formula

$$
\int _ { - 1 } ^ { 1 } f ( x ) d x \approx c _ { 1 } f ( x _ { 1 } ) + c _ { 2 } f ( x _ { 2 } )
$$

gives the exact result whenever $f ( x )$ is a polynomial of degree $2 ( 2 ) - 1 = 3$ or less, that is, when

$$
f ( x ) = a _ { 0 } + a _ { 1 } x + a _ { 2 } x ^ { 2 } + a _ { 3 } x ^ { 3 } ,
$$

for some collection of constants, $a _ { 0 } , a _ { 1 } , a _ { 2 }$ ,and $a _ { 3 }$ . Because

$$
\int ( a _ { 0 } + a _ { 1 } x + a _ { 2 } x ^ { 2 } + a _ { 3 } x ^ { 3 } ) d x = a _ { 0 } \int 1 d x + a _ { 1 } \int x d x + a _ { 2 } \int x ^ { 2 } d x + a _ { 3 } \int x ^ { 2 } d x .
$$

this is equivalent to showing that the formula gives exact results when $f ( x ) { \mathrm { ~ i s ~ } } 1 , x , x ^ { 2 }$ ， and $x ^ { 3 }$ . Hence, we need $c _ { 1 } , c _ { 2 } , x _ { 1 }$ ,and $x _ { 2 }$ ,so that

$$
c _ { 1 } \cdot 1 + c _ { 2 } \cdot 1 = \int _ { - 1 } ^ { 1 } 1 d x = 2 , \qquad c _ { 1 } \cdot x _ { 1 } + c _ { 2 } \cdot x _ { 2 } = \int _ { - 1 } ^ { 1 } x \ d x = 0 ,
$$

$$
c _ { 1 } \cdot x _ { 1 } ^ { 2 } + c _ { 2 } \cdot x _ { 2 } ^ { 2 } = \int _ { - 1 } ^ { 1 } x ^ { 2 } d x = { \frac { 2 } { 3 } } , \quad { \mathrm { a n d } } \quad c _ { 1 } \cdot x _ { 1 } ^ { 3 } + c _ { 2 } \cdot x _ { 2 } ^ { 3 } = \int _ { - 1 } ^ { 1 } x ^ { 3 } d x = 0 .
$$

A little algebra shows that this system of equations has the unique solution

$$
c _ { 1 } = 1 , \quad c _ { 2 } = 1 , \quad x _ { 1 } = - { \frac { \sqrt { 3 } } { 3 } } , \quad { \mathrm { ~ a n d ~ } } \quad x _ { 2 } = { \frac { \sqrt { 3 } } { 3 } } ,
$$

which gives the approximation formula

$$
\int _ { - 1 } ^ { 1 } f ( x ) d x \approx f \left( { \frac { - { \sqrt { 3 } } } { 3 } } \right) + f \left( { \frac { \sqrt { 3 } } { 3 } } \right) .
$$

This formula has degreeof precision 3, thatis,it produces the exact result for every polynomial of degree 3 or less.

This technique could be used to determine the nodes and coefficients for formulas that give exact results for higher-degree polynomials, but an alternative method obtains them more easily.In Sections 8.2 and 8.3 we will consider various collections of orthogonal polynomials, functions that have the property that a particular definite integral of the product of any two of them is O. The set that is relevant to our problem is the set of Legendre polynomials,a collection $\{ P _ { 0 } ( x ) , P _ { 1 } ( x ) , \ldots , P _ { n } ( x ) , \ldots , \}$ with properties:

1．For each $\pmb { n }$ ， $P _ { n } \{ x \}$ is a polynomial of degree $n$

2. $\begin{array} { r } { \int _ { - 1 } ^ { 1 } P ( x ) P _ { n } ( x ) d x = 0 } \end{array}$ whenever $P ( x )$ is a polynomial of degree less than $n$

The first few Legendre polynomials are

$$
P _ { 0 } ( x ) = 1 , \quad P _ { 1 } ( x ) = x , \quad P _ { 2 } ( x ) = x ^ { 2 } - \frac { 1 } { 3 } ,
$$

$$
P _ { 3 } ( x ) = x ^ { 3 } - { \frac { 3 } { 5 } } x , \quad { \mathrm { a n d } } \quad P _ { 4 } ( x ) = x ^ { 4 } - { \frac { 6 } { 7 } } x ^ { 2 } + { \frac { 3 } { 3 5 } } .
$$

The roots of these polynomials are distinct, lie in the interval $( - 1 , 1 )$ , have a symmetry with respect to the origin,and, most importantly,are the correct choice for determining the parameters that solve our problem.

The nodes $x _ { 1 } , x _ { 2 } , \ldots , x _ { n }$ needed to produce an integral approximation formula that gives exact results for any polynomial of degree less than $2 n$ are the roots of the $n$ th-degree Legendre polynomial. This is established by the following result.

Suppose that $x _ { 1 } , x _ { 2 } , \ldots , x _ { n }$ are the roots of the $\pmb { n }$ th Legendre polynomial $P _ { n } ( x )$ and that for each $i = 1 , 2 , \dots , n .$ , the numbers $c _ { i }$ are defined by

$$
c _ { i } = \int _ { - 1 } ^ { 1 } \prod _ { j = 1 } ^ { n } { \frac { x - x _ { j } } { x _ { i } - x _ { j } } } d x .
$$

If $P ( x )$ is any polynomial of degree less than $2 n$ ,then

$$
\int _ { - 1 } ^ { 1 } P ( x ) d x = \sum _ { i = 1 } ^ { n } c _ { i } P ( x _ { i } ) .
$$

Proof Let us first consider the situation for a polynomial $P ( x )$ of degree less than $n$ Rewrite $P ( x )$ as an $( n - 1 ) \mathsf { s t }$ Lagrange polynomial with nodes at the roots of the nth Legendre polynomial $P _ { n } ( x )$ . This representation of $P ( x )$ is exact, since the error term involves the $\pmb { n }$ th derivative of $P$ and the nth derivative of $P$ is 0. Hence,

$$
\int _ { - 1 } ^ { 1 } P ( x ) d x = \int _ { - 1 } ^ { 1 } \left[ \sum _ { i = 1 } ^ { n } \prod _ { j = 1 } ^ { n } { \frac { x - x _ { j } } { x _ { i } - x _ { j } } } P ( x _ { i } ) \right] d x
$$

$$
= \sum _ { i = 1 } ^ { n } \left[ \int _ { - 1 } ^ { 1 } \prod _ { j = 1 } ^ { n } { \frac { x - x _ { j } } { x _ { i } - x _ { j } } } d x \right] P ( x _ { i } ) = \sum _ { i = 1 } ^ { n } c _ { i } P ( x _ { i } ) ,
$$

which verifies the result for polynomials of degree less than $\pmb { n }$

If the polynomial $P ( x )$ of degree at least $\pmb { n }$ but less than $2 n$ is divided by the $\pmb { n }$ th Legendre polynomial $P _ { n } ( x )$ , we get two polynomials $Q ( x )$ and $R ( x )$ of degree less than $\pmb { n }$ ：

$$
\begin{array} { r } { P ( x ) = Q ( x ) P _ { n } ( x ) + R ( x ) . } \end{array}
$$

We now invoke the unique power of the Legendre polynomials.First,the degree of the polynomial $Q ( x )$ is less than $\pmb { n }$ , so (by Legendre property 2),

$$
\int _ { - 1 } ^ { 1 } Q ( x ) P _ { n } ( x ) d x = 0 .
$$

Next, since $x _ { i }$ is a root of $P _ { n } ( x )$ for each $i = 1 , 2 , \dots , n$ ,we have

$$
P ( x _ { i } ) = Q ( x _ { i } ) P _ { n } ( x _ { i } ) + R ( x _ { i } ) = R ( x _ { i } ) .
$$

Finally, since $R ( x )$ is a polynomial of degree less than $\pmb { n }$ , the opening argument implies that

$$
\int _ { - 1 } ^ { 1 } R ( x ) d x = \sum _ { i = 1 } ^ { n } c _ { i } R ( x _ { i } ) .
$$

Putting these facts together verifies that the formula is exact for the polynomial $P ( x )$ ：

$$
P ( x ) d x = \int _ { - 1 } ^ { 1 } [ Q ( x ) P _ { n } ( x ) + R ( x ) ] d x = \int _ { - 1 } ^ { 1 } R ( x ) d x = \sum _ { i = 1 } ^ { n } c _ { i } R ( x _ { i } ) = \sum _ { i = 1 } ^ { n } c _ { i } P ( x _ { i } ) .
$$

The constants $c _ { i }$ needed for the quadrature rule can be generated from the equation in Theorem 4.7, but both these constants and the roots of the Legendre polynomials are extensively tabulated. Table 4.11 lists these values for $n = 2 , 3 , 4$ ,and 5. Others can be found in [StS].

An integral $\textstyle \int _ { a } ^ { b } f ( x ) d x$ over an arbitrary $[ a , b ]$ can be transformed into an integral over $[ - 1 , 1 ]$ by using the change of variables (see Figure 4.16 on page 225):

$$
t = { \frac { 2 x - a - b } { b - a } } \Longleftrightarrow x = { \frac { 1 } { 2 } } [ ( b - a ) t + a + b ] .
$$

This permits Gaussian quadrature to be applied to any interval $[ a , b ]$ , since

$$
\int _ { a } ^ { b } f ( x ) d x = \int _ { - 1 } ^ { 1 } f \left( { \frac { ( b - a ) t + ( b + a ) } { 2 } } \right) { \frac { ( b - a ) } { 2 } } d t .
$$

Table 4.11   

<table><tr><td rowspan=1 colspan=3>n                  Roots rn,i                  Coefficients Cn.i</td></tr><tr><td rowspan=1 colspan=3>2               0.5773502692             1.0000000000-0.5773502692             1.00000000003               0.7745966692             0.55555555560.0000000000             0.8888888889-0.7745966692             0.55555555564               0.8611363116             0.3478548451</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2>0.3399810436             0.6521451549</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2>-0.3399810436             0.6521451549</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-0.8611363116</td><td rowspan=1 colspan=1>0.3478548451</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=2>0.9061798459             0.2369268850</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2>0.5384693101             0.4786286705</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2>0.0000000000             0.5688888889</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-0.5384693101</td><td rowspan=1 colspan=1>0.4786286705</td></tr><tr><td rowspan=1 colspan=3>-0.9061798459             0.2369268850</td></tr></table>

![](images/9242f01d9685898e94a389c12555aca38fe3c72fceafce54be4ea412f71d61f9.jpg)  
Figure 4.16

Consider the problem of finding approximations to $\textstyle { \int _ { 1 } ^ { 1 . 5 } e ^ { - x ^ { 2 } } d x }$ . Table 4.12 lists the values for the Newton-Cotes formulas given in Section 4.3. The exact value of the integral to seven decimal places is O.1093643.

# Table 4.12

<table><tr><td>n</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td>Closed formulas</td><td></td><td>0.1183197</td><td>0.1093104</td><td>0.1093404</td><td>0.1093643</td></tr><tr><td>Open formulas</td><td>0.1048057</td><td>0.1063473</td><td>0.1094116</td><td>0.1093971</td><td></td></tr></table>

The Gaussian quadrature procedure applied to this problem requires that the integral first be transformed into a problem whose interval of integration is [-1,1]. Using Eq. (4.42), we have

$$
\int _ { 1 } ^ { 1 . 5 } e ^ { - x ^ { 2 } } d x = { \frac { 1 } { 4 } } \int _ { - 1 } ^ { 1 } e ^ { ( - ( t + 5 ) ^ { 2 } / 1 6 ) } d t .
$$

The values in Table 4.11 give the following Gaussian quadrature approximations for this problem:

$$
\int _ { 1 } ^ { 1 . 5 } e ^ { - x ^ { 2 } } d x \approx { \frac { 1 } { 4 } } [ e ^ { - ( 5 + 0 . 5 7 7 3 5 0 2 6 9 2 ) ^ { 2 } / 1 6 } + e ^ { - ( 5 - 0 . 5 7 7 3 5 0 2 6 9 2 ) ^ { 2 } / 1 6 } ] = 0 . 1 0 9 4 0 0 3 ;
$$

n = 3:

$$
\begin{array} { r l r }   { \int _ { 1 } ^ { 1 . 5 } e ^ { - x ^ { 2 } } d x \approx \frac { 1 } { 4 } \{ ( 0 . 5 5 5 5 5 5 5 5 5 5 6 ) e ^ { - ( 5 + 0 . 7 7 4 5 9 6 6 6 9 2 ) ^ { 2 } / 1 6 } + ( 0 . 8 8 8 8 8 8 8 8 8 8 9 ) e ^ { - ( 5 ) ^ { 2 } / 1 6 } } \\ & { } & \\ & { } & { \qquad + ( 0 . 5 5 5 5 5 5 5 5 5 5 6 ) e ^ { - ( 5 - 0 . 7 7 4 5 9 6 6 6 9 2 ) ^ { 2 } / 1 6 } ] } \end{array}
$$

For further comparison, the values obtained using the Romberg procedure with $n = 4$ are listed in Table 4.13.

# Table 4.13

<table><tr><td>0.1183197</td><td></td><td></td><td></td></tr><tr><td>0.1115627</td><td>0.1093104</td><td></td><td></td></tr><tr><td>0.1099114</td><td>0.1093610</td><td>0.1093643</td><td></td></tr><tr><td>0.1095009</td><td>0.1093641</td><td>0.1093643</td><td>0.1093643</td></tr></table>

# Exercise Set 4.7

1. Approximate the following integrals using Gaussian quadrature with $n = 2$ , and compare your results to the exact values of the integrals.

a. $\begin{array} { l } { \displaystyle \int _ { 1 } ^ { 1 . 5 } x ^ { 2 } \ln { x } d x } \\ { \displaystyle \int _ { 0 } ^ { 0 . 3 5 } \frac { 2 } { x ^ { 2 } - 4 } d x } \\ { \displaystyle \int _ { 0 } ^ { \pi / 4 } e ^ { 3 x } \sin { 2 x } d x } \\ { \displaystyle \int _ { 3 } ^ { 3 . 5 } \frac { x } { \sqrt { x ^ { 2 } - 4 } } d x } \end{array}$ $\begin{array} { r l } { { \mathbf b } . } & { { } \displaystyle \int _ { 0 } ^ { 1 } x ^ { 2 } e ^ { - x } d x } \\ { { \mathbf d } . } & { { } \displaystyle \int _ { 0 } ^ { \pi / 4 } x ^ { 2 } \sin x d x } \\ { { \mathbf f } . } & { { } \displaystyle \int _ { 1 } ^ { 1 . 6 } \frac { 2 x } { x ^ { 2 } - 4 } d x } \\ { { \mathbf h } . } & { { } \displaystyle \int _ { 0 } ^ { \pi / 4 } ( \cos x ) ^ { 2 } d x } \end{array}$   
c.   
e.   
g.

2. Repeat Exercise 1 with $n = 3$

3.Repeat Exercise 1 with $n = 4$

4. Repeat Exercise 1 with $n = 5$

5.Determine constants $a , b , c$ ,and $\pmb { d }$ that will produce a quadrature formula

$$
\int _ { - 1 } ^ { 1 } f ( x ) d x = a f ( - 1 ) + b f ( 1 ) + c f ^ { \prime } ( - 1 ) + d f ^ { \prime } ( 1 )
$$

that has degree of precision 3.

Determine constants $a , b , c ,$ and $d$ that will produce a quadrature formula

$$
\int _ { - 1 } ^ { 1 } f ( x ) d x = a f ( - 1 ) + b f ( 0 ) + c f ( 1 ) + d f ^ { \prime } ( - 1 ) + e f ^ { \prime } ( 1 )
$$

that has degree of precision 4.

6.Verify the entries for the values of $n = 2$ and 3 in Table 4.11 by finding the roots of the respective Legendre polynomials,and use the equations preceding this table to find the coefficients associated with the values.

7.Show that the formula $\begin{array} { r } { Q ( P ) = \sum _ { i = 1 } ^ { n } c _ { i } P ( x _ { i } ) } \end{array}$ cannot have degree of precision greater than $2 n - 1$ ,regardless of the choice of $c _ { 1 } , \ldots , c _ { n }$ and $x _ { 1 } , \ldots , x _ { n }$ . [Hint: Construct a polynomial that has a double root at each of the $x _ { i } ^ { \prime } \mathbf { s . } ]$

# 4.8 Multiple Integrals

The techniques discussed in the previous sections can be modified in a straightforward manner for use in the approximation of multiple integrals. Consider the double integral

$$
\int _ { R } f ( x , y ) d A ,
$$

where $R \ = \ \{ \ ( x , y ) \mid a \ \leq \ x \ \leq \ b , c \ \leq \ y \ \leq \ d \}$ ， for some constants $a , b , c ,$ and $d$ ， is a rectangular region in the plane. (See Figure 4.17.） We will employ the Composite

![](images/5bb726da748ba84121d51f50ea22588f4650c77cd96e218522f39794f4ed2039.jpg)  
Figure 4.17

Simpson's rule to ilustrate the approximation technique,although any other composite formula could be used in its place.

To apply the Composite Simpson's rule, we divide the region $R$ by partitioning both $[ a , b ]$ and $[ c , d ]$ into an even number of subintervals. To simplify the notation, we choose even integers $n$ and $m$ and partition $[ a , b ]$ and $[ c , d ]$ with the evenly spaced mesh points $x _ { 0 } , x _ { 1 } , \ldots , x _ { n }$ and $y _ { 0 } , y _ { 1 } , \ldots , y _ { m }$ , respectively. These subdivisions determine step sizes $h = ( b - a ) / n$ and $k = ( d - c ) / m$ . Writing the double integral as the iterated integral

$$
\iint _ { R } f ( x , y ) d A = \int _ { a } ^ { b } \left( \int _ { c } ^ { d } f ( x , y ) d y \right) d x ,
$$

we firstuse the Composite Simpson's rule to approximate

$$
\int _ { c } ^ { d } f ( x , y ) d y ,
$$

treating $x$ as a constant. Let $y _ { j } = c + j k$ , for each $j = 0 , 1 , \ldots , m$ . Then

$$
\begin{array} { c } { { { \displaystyle f ^ { d } } f ( x , y ) d y = \frac { k } { 3 } \left[ f ( x , y _ { 0 } ) + 2 \sum _ { j = 1 } ^ { ( m / 2 ) - 1 } f ( x , y _ { 2 j } ) + 4 \sum _ { j = 1 } ^ { m / 2 } f ( x , y _ { 2 j - 1 } ) + f ( x , y _ { m } ) \right] } } \\ { { { } } } \\ { { - \frac { ( d - c ) k ^ { 4 } } { 1 8 0 } \frac { \partial ^ { 4 } f ( x , \mu ) } { \partial y ^ { 4 } } , } } \end{array}
$$

for some $\mu$ in $( c , d )$ . Thus,

$$
 \begin{array} { r l } { \displaystyle \int _ { a } ^ { b } \int _ { c } ^ { d } f ( x , y ) d y d x = \frac { k } { 3 } { \biggl [ } \int _ { a } ^ { b } f ( x , y _ { 0 } ) d x + 2 { \begin{array} { c } { \displaystyle \sum _ { j = 1 } ^ { ( m / 2 ) - 1 } \int _ { a } ^ { b } f ( x , y _ { 2 j } ) d x } \\ { \displaystyle + \ 4 \sum _ { j = 1 } ^ { m / 2 } \int _ { a } ^ { b } f ( x , y _ { 2 j - 1 } ) d x + \int _ { a } ^ { b } f ( x , y _ { m } ) d x { \biggl ] } } \\ { \displaystyle - \ \frac { ( d - c ) k ^ { 4 } } { 1 8 0 } } \int _ { a } ^ { b } \frac { \partial ^ { 4 } f ( x , \mu ) } { \partial y ^ { 4 } } d x . } \end{array} } \end{array}
$$

The Composite Simpson's rule is now employed on the integrals in this equation. Let $x _ { i } = a + i h$ , for each $i = 0 , 1 , \ldots , n$ . Then for each $j = 0 , 1 , \ldots , m$ , we have

$$
\begin{array} { l } { { \displaystyle \int _ { a } ^ { b } f ( x , y _ { j } ) d x = \frac { h } { 3 } \left[ f ( x _ { 0 } , y _ { j } ) + 2 \sum _ { i = 1 } ^ { ( n / 2 ) - 1 } f ( x _ { 2 i } , y _ { j } ) + 4 \sum _ { i = 1 } ^ { n / 2 } f ( x _ { 2 i - 1 } , y _ { j } ) + f ( x _ { n } , y _ { i } ) \right] } } \\ { { - \displaystyle \frac { ( b - a ) h ^ { 4 } } { 1 8 0 } \frac { \partial ^ { 4 } f } { \partial x ^ { 4 } } ( \xi _ { j } , y _ { j } ) , } } \end{array}
$$

for some $\xi _ { j }$ in $( a , b )$ . The resulting approximation has the form

$$
\begin{array} { r l } { \displaystyle \int _ { 0 } ^ { \infty } \int _ { - \infty } ^ { \infty } \int _ { 0 } ^ { \infty } \int _ { 0 } ^ { \infty } ( \int _ { 0 } ^ { \infty } ( x _ { \infty } , x _ { \infty } ) ( E ( x _ { \infty } , x _ { \infty } ) + 2 \sum _ { j = 1 } ^ { \infty } \int _ { 0 } ^ { x _ { \infty } }  i ( x _ { \infty } , x _ { j } )    } \\ { \displaystyle } & { +   \frac { \partial _ { x } ^ { 2 } } { \partial x _ { \infty } ^ { 2 } } \int _ { 0 } ^ { x _ { \infty } } ( x _ { \infty - 1 , \infty , j } ) + i ( E ( x _ { \infty } , x _ { \infty } ) )   } \\ { \displaystyle } & { - 2 ( \sum _ { j = 1 } ^ { \infty } \int _ { 0 } ^ { x _ { \infty } }  i ( x _ { \infty - 1 , j + 1 } ) + 2 \sum _ { j = 1 } ^ { \infty } \sum _ { j = 1 } ^ { \infty } \frac { i \partial _ { x } ^ { 2 } } { \partial x _ { \infty } ^ { 2 } }   } \\ { \displaystyle } & {   +  \sum _ { j = 1 } ^ { \infty } \sum _ { j = 1 } ^ { \infty } \int _ { 0 } ^ { x _ { \infty } }  i ( x _ { \infty - 1 , j - 1 } ) + 2 \sum _ { j = 1 } ^ { \infty } \int _ { 0 } ^ { x _ { \infty } }  i ( x _ { \infty - 1 , j - 1 } )     } \\ { \displaystyle } & {   +   \frac { \partial _ { x } ^ { 2 } } { \partial x _ { \infty } ^ { 2 } } \int _ { 0 } ^ { x _ { \infty } }  i ( x _ { \infty - 1 , j - 1 } ) + 2 \sum _ { j = 1 } ^ { \infty } \int _ { 0 } ^ { x _ { \infty } }  i ( x _ { \infty - 1 , j - 1 } )     } \\ { \displaystyle } &    +  \frac { \partial _ { x } ^ { 2 } } { \partial x _ { \infty } ^ { 2 } } \int _ { 0 } ^ { x _ { \infty } }  i ( x _ { \infty - 1 , j - 1 } ) + 2 \sum _ { j = 1 } ^ { \infty } \int _ { 0 } ^  x _  \infty - 1 , \end{array}
$$

The error term $E$ is given by

$$
\begin{array} { l } { { \displaystyle { E = \frac { - k ( b - a ) h ^ { 4 } } { 5 4 0 } \bigg [ \frac { \partial ^ { 4 } f ( \xi _ { 0 } , y _ { 0 } ) } { \partial x ^ { 4 } } + 2 \sum _ { j = 1 } ^ { ( m / 2 ) - 1 } \frac { \partial ^ { 4 } f ( \xi _ { 2 j } , y _ { 2 j } ) } { \partial x ^ { 4 } } + 4 \sum _ { j = 1 } ^ { m / 2 } \frac { \partial ^ { 4 } f ( \xi _ { 2 j - 1 } , y _ { 2 j - 1 } ) } { \partial x ^ { 4 } } } } } \\ { { \displaystyle { + \frac { \partial ^ { 4 } f ( \xi _ { m } , y _ { m } ) } { \partial x ^ { 4 } } \bigg ] - \frac { ( d - c ) k ^ { 4 } } { 1 8 0 } \int _ { a } ^ { b } \frac { \partial ^ { 4 } f ( x , \mu ) } { \partial y ^ { 4 } } d x . } } } \end{array}
$$

If $\partial ^ { 4 } f / \partial x ^ { 4 }$ is continuous, the Intermediate Value Theorem can be repeatedly applied to show that the evaluation of the partial derivatives with respect to $x$ can be replaced by a common value and that

$$
E = \frac { - k ( b - a ) h ^ { 4 } } { 5 4 0 } \left[ 3 m \frac { \partial ^ { 4 } f } { \partial x ^ { 4 } } ( \vec { \eta } , \overline { { { \mu } } } ) \right] - \frac { ( d - c ) k ^ { 4 } } { 1 8 0 } \int _ { a } ^ { b } \frac { \partial ^ { 4 } f ( x , \mu ) } { \partial y ^ { 4 } } d x ,
$$

for some $( \overline { { \eta } } , \overline { { \mu } } )$ in $R$ .If $\partial ^ { 4 } f / \partial y ^ { 4 }$ is also continuous, the Weighted Mean Value Theorem for Integrals implies that

$$
\int _ { a } ^ { b } { \frac { \partial ^ { 4 } f ( x , \mu ) } { \partial y ^ { 4 } } } d x = ( b - a ) { \frac { \partial ^ { 4 } f } { \partial y ^ { 4 } } } ( { \hat { \eta } } , { \hat { \mu } } ) ,
$$

for some $( \hat { \eta } , \hat { \mu } )$ in $R$ . Since $m = ( d - c ) / k$ , the error term has the form

$$
E = \frac { - k ( b - a ) h ^ { 4 } } { 5 4 0 } \left[ 3 m \frac { \partial ^ { 4 } f } { \partial x ^ { 4 } } ( \overline { { { \eta } } } , \overline { { { \mu } } } ) \right] - \frac { ( d - c ) ( b - a ) } { 1 8 0 } k ^ { 4 } \frac { \partial ^ { 4 } f } { \partial y ^ { 4 } } ( \hat { \eta } , \hat { \mu } )
$$

or

$$
E = - \frac { ( d - c ) ( b - a ) } { 1 8 0 } \left[ h ^ { 4 } \frac { \partial ^ { 4 } f } { \partial x ^ { 4 } } ( \overline { { \eta } } , \overline { { \mu } } ) + k ^ { 4 } \frac { \partial ^ { 4 } f } { \partial y ^ { 4 } } ( \hat { \eta } , \hat { \mu } ) \right] ,
$$

# EXAMPLE 1

for some $( \overline { { \eta } } , \overline { { \mu } } )$ and $( \hat { \eta } , \hat { \mu } )$ in $R$

The Composite Simpson's rule applied to approximate

$$
\int _ { 1 . 4 } ^ { 2 . 0 } \int _ { 1 . 0 } ^ { 1 . 5 } \ln ( x + 2 y ) d y d x ,
$$

with $n = 4$ and $m = 2$ uses the step sizes $h = 0 . 1 5$ and $k = 0 . 2 5$ . The region of integration $R$ is shown in Figure 4.18, together with the nodes $( x _ { i } , y _ { j } )$ ， where $i \ = 0$ ,1,2,3,4 and $j = 0$ , 1, 2 and, the coeficients $w _ { i , j }$ ,of $f ( x _ { i } , y _ { j } ) = \ln ( x _ { i } + 2 y _ { j } )$ in the sum.

![](images/97022ba8013a164394a1cd8e807043b9d86cc51f435bf36674d75e91b37a9290.jpg)  
Figure 4.18

The approximation is

$$
\int _ { 1 . 4 } ^ { 2 . 0 } \int _ { 1 . 0 } ^ { 1 . 5 } \ln ( x + 2 y ) d y d x \approx { \frac { ( 0 . 1 5 ) ( 0 . 2 5 ) } { 9 } } \sum _ { i = 0 } ^ { 4 } \sum _ { j = 0 } ^ { 2 } w _ { i , j } \ln ( x _ { i } + 2 y _ { j } )
$$

Since

$$
{ \frac { \partial ^ { 4 } f } { \partial x ^ { 4 } } } ( x , y ) = { \frac { - 6 } { ( x + 2 y ) ^ { 4 } } } \quad { \mathrm { ~ a n d ~ } } \quad { \frac { \partial ^ { 4 } f } { \partial y ^ { 4 } } } ( x , y ) = { \frac { - 9 6 } { ( x + 2 y ) ^ { 4 } } } ,
$$

and the maximum value of $\frac { 1 } { ( x + 2 y ) ^ { 4 } }$ on $R$ occurs at (1.4,1.0), the error is bounded by

$$
\begin{array} { r l r } {  { | E | \le \frac { ( 0 . 5 ) ( 0 . 6 ) } { 1 8 0 } [ ( 0 . 1 5 ) ^ { 4 } \operatorname* { m a x } _ { ( x , y ) \mathrm { i n } R } \frac { 6 } { ( x + 2 y ) ^ { 4 } } + ( 0 . 2 5 ) ^ { 4 } \operatorname* { m a x } _ { ( x , y ) \mathrm { i n } R } \frac { 9 6 } { ( x + 2 y ) ^ { 4 } } ] } } \\ & { } & { \le 4 . 7 2 \times 1 0 ^ { - 6 } . } \end{array}
$$

The actual value of the integral to ten decimal places is

$$
\int _ { 1 . 4 } ^ { 2 . 0 } \int _ { 1 . 0 } ^ { 1 . 5 } \ln ( x + 2 y ) d y d x = 0 . 4 2 9 5 5 4 5 2 6 5 ,
$$

so the approximation is accurate to within $2 . 1 \times 1 0 ^ { - 6 }$ .

The same techniques can be applied for the approximation of triple integrals as well as higher integrals for functions of more than three variables. The number of functional evaluations required for the approximation is the product of the number of functional evaluations required when the method is applied to each variable.

To reduce the number of functional evaluations, more efcient methods such as Gaussian quadrature, Romberg integration, or Adaptive quadrature can be incorporated in place of the Newton-Cotes formulas. The following example illustrates the use of Gaussian quadrature for the integral considered in Example 1.

Consider the double integral given in Example 1. Before employing a Gaussian quadrature technique to approximate this integral, we transform the region of integration

$$
R = \{ ( x , y ) \mid 1 . 4 \leq x \leq 2 . 0 , 1 . 0 \leq y \leq 1 . 5 \}
$$

into

$$
\hat { R } = \{ ( u , v ) | - 1 \leq u \leq 1 , - 1 \leq v \leq 1 \} .
$$

The linear transformations that accomplish this are

$$
u = \frac { 1 } { 2 . 0 - 1 . 4 } ( 2 x - 1 . 4 - 2 . 0 ) \quad \mathrm { a n d } \quad v = \frac { 1 } { 1 . 5 - 1 . 0 } ( 2 y - 1 . 0 - 1 . 5 ) .
$$

or, equivalently, $x = 0 . 3 u + 1 . 7$ and $y = 0 . 2 5 \upsilon + 1 . 2 5$ . Employing this change of variables gives an integral on which Gaussian quadrature can be applied:

$$
\int _ { 1 . 4 } ^ { 2 . 0 } \int _ { 1 . 0 } ^ { 1 . 5 } \ln ( x + 2 y ) d y d x = 0 . 0 7 5 \int _ { - 1 } ^ { 1 } \int _ { - 1 } ^ { 1 } \ln ( 0 . 3 u + 0 . 5 \nu + 4 . 2 ) d v d u .
$$

The Gaussian quadrature formula for $n = 3$ in both $\pmb { u }$ and $\boldsymbol { \mathcal { V } }$ requires that we use the nodes

$$
u _ { 1 } = v _ { 1 } = r _ { 3 , 2 } = 0 , \quad u _ { 0 } = v _ { 0 } = r _ { 3 , 1 } = - 0 . 7 7 4 5 9 6 6 6 9 2 ,
$$

and

$$
u _ { 2 } = v _ { 2 } = r _ { 3 , 3 } = 0 . 7 7 4 5 9 6 6 6 9 2 .
$$