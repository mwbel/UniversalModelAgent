The associated weights are $c _ { 3 , 2 } = 0 . { \overset {  } { 8 } }$ and $\begin{array} { r } { c _ { 3 , 1 } = c _ { 3 , 3 } = 0 . \overline { { 5 } } . } \end{array}$ (See Table 4.11.) Thus,

$$
\int _ { 1 . 4 } ^ { 2 . 0 } \int _ { 1 . 0 } ^ { 1 . 5 } \ln ( x + 2 y ) d y d x \approx 0 . 0 7 5 \sum _ { i = 1 } ^ { 3 } \sum _ { j = 1 } ^ { 3 } c _ { 3 , i } c _ { 3 , j } \ln ( 0 . 3 r _ { 3 , i } + 0 . 5 r _ { 3 , j } + 4 . 2 )
$$

Although this result requires only 9 functional evaluations compared to 15 for the Com-posite Simpson's rule considered in Example 1, this result is accurate to within $4 . 8 \times 1 0 ^ { - 9 }$ ， compared to $2 . 1 \times 1 0 ^ { - 6 }$ accuracy in Example 1. □

The use of approximation methods for double integrals is not limited to integrals with rectangular regions of integration. The techniques previously discussed can be modified to approximate double integrals of the form

$$
\int _ { a } ^ { b } \int _ { c ( x ) } ^ { d ( x ) } f ( x , y ) d y d x
$$

or

$$
\int _ { c } ^ { d } \int _ { a ( y ) } ^ { b ( y ) } f ( x , y ) d x d y .
$$

In fact, integrals on regions not of this type can also be approximated by performing appropriate partitions of the region. (See Exercise 10.)

To describe the technique involved with approximating an integral in the form

$$
\int _ { a } ^ { b } \int _ { c ( x ) } ^ { d ( x ) } f ( x , y ) d y d x ,
$$

we will use the basic Simpson's rule to integrate with respect to both variables. The step size for the variable $x$ is $h = ( b - a ) / 2$ , but the step size for $y$ varies with $x$ (see Figure 4.19)and is written

$$
k ( x ) = { \frac { d ( x ) - c ( x ) } { 2 } } .
$$

Consequently,

$$
\begin{array} { l } { \displaystyle \int _ { a } ^ { b } \int _ { c ( x ) } ^ { d ( s ) } f ( x , y ) d y d x \approx \int _ { a } ^ { b } \frac { k ( x ) } { 3 } [ f ( x , c ( x ) ) + 4 f ( x , c ( x ) + k ( x ) ) + f ( x , d ( x ) ) } \\ { \displaystyle \approx \frac { h } { 3 } \Big \lbrace \frac { k ( a ) } { 3 } [ f ( a , c ( a ) ) + 4 f ( a , c ( a ) + k ( a ) ) + f ( a , d ( a ) ) ] } \\ { \displaystyle \quad + \frac { 4 k ( a + h ) } { 3 } [ f ( a + h , c ( a + h ) ) + 4 f ( a + h , c ( a + h ) } \\ { \displaystyle \quad + k ( a + h ) ) + f ( a + h , d ( a + h ) ) ] } \\ { \displaystyle \quad + \frac { k ( b ) } { 3 } [ f ( b , c ( b ) ) + 4 f ( b , c ( b ) + k ( b ) ) + f ( b , d ( b ) ) ] \Big \rbrace } \end{array}
$$

![](images/145526bc6e4938c3c00f9249c0593248de7cedbe31cae2eed1bc382c75a21587.jpg)  
Figure 4.19

Algorithm 4.4 applies the Composite Simpson's rule to an integral in the form (4.43).   
Integrals in the form (4.44) can, of course,be handled similarly.

# Simpson's Double Integral

To appoximae he intgal $\begin{array} { r } { I = \int _ { a } ^ { b } \int _ { c ( x ) } ^ { d ( x ) } f ( x , y ) d y d x ; } \end{array}$

INPUT endpoints $a , b$ : even positive integers $m , n$

OUTPUT approximation $J$ to $I$ ，

Step 1 Set $\begin{array} { r l } & { \mathrm { ~ : ~ } h = ( b - a ) / n ; } \\ & { \quad J _ { 1 } = 0 ; \quad ( E n d t e r m s . ) } \\ & { \quad J _ { 2 } = 0 ; \quad ( E \nu e n t e r m s . ) } \\ & { \quad J _ { 3 } = 0 . \quad ( O d d t e r m s . ) } \end{array}$

Step 2 For $i = 0 , 1 , \ldots , n$ do Steps 3-8.

Step 3 Set $x = a + i h$ ;(Composite Simpson's method for $x$ ） $\begin{array} { l l } { { H X = ( d ( x ) - c ( x ) ) / m ; } } & { { } } \\ { { K _ { 1 } = f ( x , c ( x ) ) + f ( x , d ( x ) ) ; } } & { { ( E n d t e r m s . ) } } \\ { { K _ { 2 } = 0 ; } } & { { ( E \nu e n t e r m s . ) } } \\ { { K _ { 3 } = 0 . } } & { { ( O d d t e r m s . ) } } \end{array}$

Step 4 For $j = 1 , 2 , \dots , m - 1$ do Step 5 and 6.

Step 5 Set $\begin{array} { l } { { y = c ( x ) + j H X ; } } \\ { { Q = f ( x , y ) . } } \end{array}$

Step $6$ If $j$ is even then set $K _ { 2 } = K _ { 2 } + Q$ else set $K _ { 3 } = K _ { 3 } + Q$

Step 7 Set $L = ( K _ { 1 } + 2 K _ { 2 } + 4 K _ { 3 } ) H X / 3 .$

$$
\left( L \approx \int _ { c ( x _ { i } ) } ^ { d ( x _ { i } ) } f ( x _ { i } , y ) d y \quad b y t h e C o m p o s i t e S i m p s o n ^ { \prime } s m e t h o d . \right)
$$

Step $8$ If $i = 0$ or $i = n$ then set $J _ { 1 } = J _ { 1 } + L$ else if $i$ is even then set $J _ { 2 } = J _ { 2 } + L$ else set $J _ { 3 } = J _ { 3 } + L$

Step 9 Set $J = h ( J _ { 1 } + 2 J _ { 2 } + 4 J _ { 3 } ) / 3$

Step 10OUTPUT $( J )$ ：STOP.

To apply Gaussian quadrature to

$$
\int _ { a } ^ { b } \int _ { c ( x ) } ^ { d ( x ) } f ( x , y ) d y d x ,
$$

first requires transforming, for each $x$ in $[ a , b ]$ , the interval $[ c ( x ) , d ( x ) ]$ to $\{ - 1 , 1 \}$ and then applying Gaussian quadrature. This results in the formula

$$
\begin{array} { l } { \displaystyle \int _ { a } ^ { b } \int _ { c ( x ) } ^ { d ( x ) } f ( x , y ) d y d x } \\ { \displaystyle \approx \int _ { a } ^ { b } \frac { d ( x ) - c ( x ) } { 2 } \sum _ { j = 1 } ^ { n } c _ { n , j } f \left( x , \frac { ( d ( x ) - c ( x ) ) r _ { n , j } + d ( x ) + c ( x ) } { 2 } \right) d x , } \end{array}
$$

where,as before, the roots $r _ { n , j }$ and coefficients $c _ { n , j }$ come from Table 4.11. Now the interval $[ a , b ]$ is tranformed to $[ - 1 , 1 ]$ ， and Gaussian quadrature is applied to approximate the integral on the right side of this equation. The details are given in Algorithm 4.5.

# Gaussian Double Integral

To aproximate te integral $\textstyle \int _ { a } ^ { b } \int _ { c ( x ) } ^ { d ( x ) } f ( x , y ) d y d x ;$

INPUTendpoints $a , b$ ; positive integers $m , n$ · (The roots $r _ { i , j }$ and coefficients $c _ { i , j }$ need to be available for $i = \operatorname* { m a x } \{ m , n \}$ and for $1 \leq j \leq i .$ ）

OUTPUT approximation $J$ to $I$

Step1 Se $\begin{array} { c } { { \mathrm { t } h _ { 1 } = ( b - a ) / 2 ; } } \\ { { h _ { 2 } = ( b + a ) / 2 ; } } \\ { { J = 0 . } } \end{array}$

Step 2 For $i = 1 , 2 , \dots , m$ do Steps 3-5.

Step 3 Set $J X = 0$ ；$\begin{array} { l } { x = h _ { 1 } r _ { m , i } + h _ { 2 } ; } \\ { d _ { 1 } = d ( x ) ; } \\ { c _ { 1 } = c ( x ) ; } \\ { k _ { 1 } = ( d _ { 1 } - c _ { 1 } ) / 2 ; } \\ { k _ { 2 } = ( d _ { 1 } + c _ { 1 } ) / 2 . } \end{array}$

Step 4 For $j = 1 , 2 , \dots , n$ do set $\begin{array} { l } { { y = \kappa _ { 1 } r _ { n . j } + \kappa _ { 2 } ; } } \\ { { Q = f ( x , y ) ; } } \\ { { J X = J X + c _ { n , j } Q . } } \end{array}$

Step 5Set $J = J + c _ { m , i } k _ { 1 } J X$

Step $\sigma$ Set $J = h _ { 1 } J$

Step 7 OUTPUT $( J )$ STOP.

# EXAMPLE 3

The volume of the solid in Figure 4.20 is approximated by applying Simpson's Double Integral Algorithm with $n = m = 1 0$ to

Figure 4.20

![](images/114556b8d30bec1489f077f8383af5f3800ac3ff7abbcdaba2e72aa00cccaaca.jpg)

$$
\int _ { 0 . 1 } ^ { 0 . 5 } \int _ { x ^ { 3 } } ^ { x ^ { 2 } } e ^ { y / x } d y d x .
$$

This requires 121 evaluations of the function $f ( x , y ) = e ^ { y / x }$ and produces the 0.0333054, which approximates the volume of the solid shown in Figure 4.2O to nearly seven decimal places. Applying the Gaussian Quadrature Algorithm with $n = m = 5$ requires only 25 function evaluations and, gives the approximation, 0.03330556611, which is accurate to 11 decimal places.

Triple integrals of the form

$$
\int _ { a } ^ { b } \int _ { c ( x ) } ^ { d ( x ) } \int _ { \alpha ( x , y ) } ^ { \beta ( x , y ) } f ( x , y , z ) d z d y d x
$$

(see Figure 4.21) are approximated in a similar manner. Because of the number of calculations involved, Gaussian quadrature is the method of choice. Algorithm 4.6 implements this procedure.

# Gaussian Triple Integral

To appoximte he itgral $\begin{array} { r } { \int _ { a } ^ { b } \int _ { c ( x ) } ^ { d ( x ) } \int _ { \alpha ( x , y ) } ^ { \beta ( x , y ) } f ( x , y , z ) d z d y d x ; } \end{array}$

INPUT endpoints $a , b$ ; positive integers $m , n , p$ (The roots $r _ { i , j }$ and coefficients $c _ { i , j }$ need to be available for $i = \operatorname* { m a x } \{ n , m , p \}$ and for $1 \leq j \leq i . ,$ ）

OUTPUT approximation $J$ to $I$ ，

Step 1 Set $\begin{array} { c } { { ; h _ { 1 } = ( b - a ) / 2 ; } } \\ { { h _ { 2 } = ( b + a ) / 2 ; } } \\ { { J = 0 . } } \end{array}$

Step 2 For $i = 1 , 2 , \dots , m$ do Steps 3-8.

$$
\begin{array} { l } { { \mathrm {  ~ \psi ~ } _ { x } = 0 ; } } \\ { { \mathrm {  ~ \psi ~ } _ { x } = h _ { 1 } r _ { m , i } + h _ { 2 } ; } } \\ { { d _ { 1 } = d ( x ) ; } } \\ { { \mathrm {  ~ \psi ~ } _ { c 1 } = c ( x ) ; } } \\ { { \mathrm {  ~ \psi ~ } _ { k 1 } = ( d _ { 1 } - c _ { 1 } ) / 2 ; } } \\ { { k _ { 2 } = ( d _ { 1 } + c _ { 1 } ) / 2 . } } \end{array}
$$

Step 4 For $j = 1 , 2 , \dots , n$ do Steps 5-7.

Step 5Set

$$
\begin{array} { c } { { \mathrm { t } J Y = 0 ; } } \\ { { y = k _ { 1 } r _ { n , j } + k _ { 2 } ; } } \\ { { \beta _ { \boldsymbol { \imath } } = \beta ( \boldsymbol { x } , \boldsymbol { y } ) ; } } \\ { { \alpha _ { \boldsymbol { \imath } } = \alpha ( \boldsymbol { x } , \boldsymbol { y } ) ; } } \\ { { l _ { 1 } = ( \beta _ { \boldsymbol { 1 } } - \alpha _ { 1 } ) / 2 ; } } \\ { { l _ { 2 } = ( \beta _ { \boldsymbol { 1 } } + \alpha _ { 1 } ) / 2 . } } \end{array}
$$

$$
\begin{array} { r l } { s t e p \ 6 } & { \mathrm { F o r } \ k = 1 , 2 , \ldots , p \ \mathrm { d o } } \\ & { \qquad \mathrm { s e t } \ z = l _ { 1 } r _ { p , k } + l _ { 2 } ; } \\ & { \qquad Q = f ( x , y , z ) ; } \\ & { \qquad J Y = J Y + c _ { p , k } Q . } \end{array}
$$

![](images/3f7cf4d5bc556520d7da6f3c44ad32e065777e3e15a68fd3a6a81fd1b7827a23.jpg)  
Figure 4.21

Step 7 Set $J X = J X + c _ { n , j } l _ { 1 } J Y .$ Step 8 Set $J = J + c _ { m , i } k _ { 1 } J X$   
Step 9 Set $J = h _ { 1 } J$   
Step 10 OUTPUT $( J )$ ； STOP.

![](images/f5300df148a6ffff48724136d19f9dae9c8224836581a006a5ae891421779fd4.jpg)

The following example requires the evaluation of four triple integrals.

# EXAMPLE 4

The center of a mass of a solid region D with density function o occurs at

$$
( \overline { { x } } , \overline { { y } } , \overline { { z } } ) = \left( \frac { M _ { y z } } { M } , \frac { M _ { x z } } { M } , \frac { M _ { x y } } { M } \right) ,
$$

where

$$
M _ { y z } = \iiint _ { D } x \sigma ( x , y , z ) d V , \quad M _ { x z } = \iiint _ { D } y \sigma ( x , y , z ) d V
$$

and

$$
M _ { x y } = \iiint _ { D } z \sigma ( x , y , z ) d V
$$

are the moments about the coordinate planes and

$$
M = \int \iint _ { D } \sigma ( x , y , z ) d V
$$

is the mass.The solid shown in Figure 4.22 is bounded by the upper nappe of the cone $z ^ { 2 } = x ^ { 2 } + y ^ { 2 }$ and the plane $z = 2$ Supposethatthissolidhasdensityfunctongivenby

$$
\sigma ( x , y , z ) = { \sqrt { x ^ { 2 } + y ^ { 2 } } } .
$$

![](images/24f9110cf5df2f153f3ff512e033e99ddcdf7f8d854e871fc7d5061019bb5364.jpg)  
Figure 4.22

Applying the Gaussian Triple Integral Algorithm 4.6 with $n = m = p = 5$ requires 125 function evaluations per integral and gives the following approximations:

$$
\begin{array} { l } { { \displaystyle M = \int _ { - 2 } ^ { 2 } \int _ { - \sqrt { 4 - x ^ { 2 } } } ^ { \sqrt { 4 - x ^ { 2 } } } \int _ { \sqrt { x ^ { 2 } + y ^ { 2 } } } ^ { 2 } \sqrt { x ^ { 2 } + y ^ { 2 } } d z d y d x } } \\ { { \displaystyle = 4 \int _ { 0 } ^ { 2 } \int _ { 0 } ^ { \sqrt { 4 - x ^ { 2 } } } \int _ { \sqrt { x ^ { 2 } + y ^ { 2 } } } ^ { 2 } \sqrt { x ^ { 2 } + y ^ { 2 } } d z d y d x \approx 8 . 3 7 5 0 4 4 7 6 , } } \end{array}
$$

$$
M _ { y z } = \int _ { - 2 } ^ { 2 } \int _ { - \sqrt { 4 - x ^ { 2 } } } ^ { \sqrt { 4 - x ^ { 2 } } } \int _ { \sqrt { x ^ { 2 } + y ^ { 2 } } } ^ { 2 } x \sqrt { x ^ { 2 } + y ^ { 2 } } d z d y d x \approx - 5 . 5 5 1 1 1 5 1 2 \times 1 0 ^ { - 1 7 } ,
$$

$$
M _ { x z } = \int _ { - 2 } ^ { 2 } \int _ { - \sqrt { 4 - x ^ { 2 } } } ^ { \sqrt { 4 - x ^ { 2 } } } \int _ { \sqrt { x ^ { 2 } + y ^ { 2 } } } ^ { 2 } y \sqrt { x ^ { 2 } + y ^ { 2 } } d z d y d x \approx - 8 . 0 1 5 1 3 6 7 5 \times 1 0 ^ { - 1 7 } ,
$$

$$
M _ { x y } = \int _ { - 2 } ^ { 2 } \int _ { - \sqrt { 4 - x ^ { 2 } } } ^ { \sqrt { 4 - x ^ { 2 } } } \int _ { \sqrt { x ^ { 2 } + y ^ { 2 } } } ^ { 2 } z \sqrt { x ^ { 2 } + y ^ { 2 } } d z d y d x \approx 1 3 . 4 0 0 3 8 1 5 6 .
$$

This implies that the approximate location of the center of mass is

$$
( \overline { { x } } , \overline { { y } } , \overline { { z } } ) = ( 0 , 0 , 1 . 6 0 0 0 3 7 0 1 ) .
$$

These integrals are quite easy to evaluate directly. If you do this,you wil find that the exact center of mass occurs at (O, 0, 1.6). ■

# ExERCisE SEt 4.8

1. Use Algorithm 4.4 with $n ~ = ~ m ~ = ~ 4$ to approximate the following double integrals，and compare the results to the exact answers.

$$
{ \begin{array} { r l } { \displaystyle \int _ { 2 . 1 } ^ { 2 . 5 } \int _ { 1 . 2 } ^ { 1 . 4 } x y ^ { 2 } d y d x \qquad } & { \mathbf { b . } \quad \displaystyle \int _ { 0 } ^ { 0 . 5 } \int _ { 0 } ^ { 0 . 5 } e ^ { x - x } d y d x } \\ { \displaystyle \int _ { 2 } ^ { 2 . 2 } \int _ { x } ^ { 2 x } ( x ^ { 2 } + y ^ { 3 } ) d y d x \qquad } & { \mathbf { d . } \quad \displaystyle \int _ { 1 } ^ { 1 . 5 } \int _ { 0 } ^ { x } ( x ^ { 2 } + { \sqrt { y } } ) d y d x } \end{array} }
$$

2. Find the smallest values for $n \ = \ m$ so that Algorithm 4.4 can be used to approximate the integrals in Exercise 1 to within $1 0 ^ { - 6 }$ of the actual value.

3.Use Algorithm 4.4 with (i) $n = 4$ ， $m = 8$ ，(ii) $n = 8 , m = 4$ ,and (iii) $n = m = 6$ t0 approximate the following double integrals, and compare the results to the exact answers.

$$
\begin{array} { l l l } { { \displaystyle \int _ { 0 } ^ { \pi / 4 } \int _ { \sin x } ^ { \cos x } \left( 2 y \sin x + \cos ^ { 2 } x \right) d y d x } } & { { ~ { \bf b } . } } & { { \displaystyle \int _ { 1 } ^ { e } \int _ { 1 } ^ { x } \ln x y d y d x } } \\ { { \displaystyle \int _ { 0 } ^ { 1 } \int _ { x } ^ { 2 x } \left( x ^ { 2 } + y ^ { 3 } \right) d y d x } } & { { } } & { { \bf d . } } & { { \displaystyle \int _ { 0 } ^ { 1 } \int _ { x } ^ { 2 x } \left( y ^ { 2 } + x ^ { 3 } \right) d y d x } } \\ { { \displaystyle \int _ { 0 } ^ { \pi } \int _ { 0 } ^ { x } \cos x d y d x } } & { { } } & { { \bf f . } } & { { \displaystyle \int _ { 0 } ^ { \pi } \int _ { 0 } ^ { x } \cos y d y d x } } \\ { { \displaystyle \int _ { 0 } ^ { \pi / 4 } \int _ { 0 } ^ { \sin x } \frac { 1 } { \sqrt { 1 - y ^ { 2 } } } d y d x } } & { { } } & { { \bf h . } } & { { \displaystyle \int _ { - \pi } ^ { 3 \pi / 2 } \int _ { 0 } ^ { 2 \pi } \left( y \sin x + x \cos y \right) d y d x } } \end{array}
$$

4. Find the smallest values for $n \ = \ m$ so that Algorithm 4.4 can be used to approximate the integrals in Exercise 3 to within $1 0 ^ { - 6 }$ of the actual value.

5.Use Algorithm 4.5 with $n = m = 2$ to approximate the integrals in Exercise 1,and compare the results to those obtained in Exercise 1.

6. Find the smallest values of $n = m$ so that Algorithm 4.5 can be used to approximate the integrals in Exercise 1 to within $1 0 ^ { - 6 }$ . Do not continue beyond $n ~ = ~ m ~ = ~ 5$ . Compare the number of functional evaluations required to the number required in Exercise 2.

7.Use Algorithm 4.5 with (i) $n = m = 3$ ，(ii) $n = 3$ ， $m \ : = \ : 4$ ，(imi) $n = 4$ ， $m = 3$ ,and (iv)$n = m = 4$ to approximate the integrals in Exercise 3.

8.Use Algorithm 4.5 with $n = m = 5$ to approximate the integrals in Exercise 3. Compare the number of functional evaluations required to the number required in Exercise 4.

9.Use Algorithm 4.4 with $n = m = 1 4$ and Algorithm 4.5 with $n = m = 4$ to approximate

$$
\int _ { R } \int _ { } ^ { } e ^ { - ( x + y ) } d A ,
$$

for the region $R$ in the plane bounded by the curves $y = x ^ { 2 }$ and $y = { \sqrt { x } }$

10.Use Algorithm 4.4 to approximate

$$
\iint _ { R } \sqrt { x y + y ^ { 2 } } d A ,
$$

where $R$ is the region in the plane bounded by the lines $x + y = 6 , 3 y - x = 2$ ,and $3 x - y = 2$ First partition $R$ into two regions $R _ { 1 }$ and $\pmb { R } _ { 2 }$ on which Algorithm 4.4 can be applied. Use $n = m = 6$ on both $R _ { 1 }$ and $R _ { 2 }$

11.A plane lamina is a thin sheet of continuously distributed mass. If $\sigma$ is a function describing the density of a lamina having the shape of a region $R$ in the $x y$ -plane, then the center of the mass of the lamina $( { \bar { x } } , { \bar { y } } )$ is

$$
{ \bar { x } } = { \frac { \iint x \sigma ( x , y ) d A } { \iint \sigma ( x , y ) d A } } , \quad { \bar { y } } = { \frac { \iint y \sigma ( x , y ) d A } { \iint \sigma ( x , y ) d A } } .
$$

Use Algorithm 4.4 with $n = m = 1 4$ to find the center of mass of the lamina described by R={(x,y)10≤x≤1,0≤y ≤√1-x²} with the density functiong(x,y）=e-(x²+y2). Compare the approximation to the exact result.

12.Repeat Exercise 11 using Algorithm 4.5 with $n = m = 5$

13.The area of the surface described by $z = f ( x , y )$ for $( x , y )$ in $R$ is given by

$$
\iint _ { R } \sqrt { [ f _ { x } ( x , y ) ] ^ { 2 } + [ f _ { y } ( x , y ) ] ^ { 2 } + 1 } \ d A .
$$

Use Algorithm 4.4 with $n = m = 8$ to find an approximation to the area of the surface on the hemisphere $x ^ { 2 } + y ^ { 2 } + z ^ { 2 } = 9 , z \geq 0$ that lies above the region in the plane described by $R = \{ ( x , y ) \mid 0 \leq x \leq 1 , 0 \leq y \leq 1 \}$

14.Repeat Exercise 13 using Algorithm 4.5 with $n = m = 4$

15. Use Algorithm 4.6 with $n = m = p = 2$ to approximate the following triple integrals,and compare the results to the exact answers.

$$
\begin{array} { r l } { { \bf \partial } \cdot } & { { } \displaystyle \int _ { 0 } ^ { 1 } \int _ { 1 } ^ { 2 } \int _ { 0 } ^ { 0 . 5 } e ^ { x + y + z } d z d y d x } \\ { { \bf \partial } \cdot } & { { } \displaystyle \int _ { 0 } ^ { 1 } \int _ { x ^ { 2 } } ^ { x } \int _ { x - y } ^ { x + y } y d z d y d x } \\ { { \bf \partial } \cdot } & { { } \displaystyle \int _ { 0 } ^ { 1 } \int _ { 0 } ^ { x } \int _ { 0 } ^ { x } \frac { 1 } { y } \sin \frac { z } { y } d z d y d x } \\ { { \bf \partial } \cdot } & { { } \displaystyle \int _ { 0 } ^ { \pi } \int _ { 0 } ^ { x } \int _ { 0 } ^ { x } \frac { 1 } { y } \sin \frac { z } { y } d z d y d x } \end{array} \qquad { \bf d } { \bf _ { \tau } } \textstyle \int _ { 0 } ^ { 1 } \int _ { 0 } ^ { 1 } \int _ { x ^ { 2 } y } ^ { x ^ { 2 } + y ^ { 2 } } d z d y d x
$$

16.Repeat Exercise 15 using $n = m = p = 3$

17.Repeat Exercise 15 using $n = m = p = 4$ and $n = m = p = 5$

18.Use Algorithm 4.6 with $n = m = p = 4$ to approximate

$$
\iiint _ { S } x y \sin ( y z ) d V ,
$$

where $s$ is the solid bounded by the coordinate planes and the planes $x = \pi , \{ \ : \mathrm { y } = \pi / 2$ $z = \pi / 3$ . Compare this approximation to the exact result.

19.Use Algorithm 4.6 with $n = m = p = 5$ to approximate

$$
\int \limits _ { s } \iint \sqrt { x y z } d V ,
$$

where $s$ is the region in the first octant bounded by the cylinder $x ^ { 2 } + y ^ { 2 } = 4$ ，the sphere $x ^ { 2 } + y ^ { 2 } + z ^ { 2 } = 4$ , and the plane $x + y + z = 8$ . How many functional evaluations are required for the approximation?

# 4.9 Improper Integrals

Improper integrals result when the notion of integration is extended either to an interval of integration on which the function is unbounded or to an interval with one or more infnite endpoints. In either circumstance, the normal rules of integral approximation must be modified.

We willfirst consider the situation when the integrand is unbounded at the left endpoint of the interval of integration,as shown in Figure 4.23.We will then show that the other improper integrals can be reduced to problems of this form.

![](images/8b057debde3a1fe37e9d22a21b77388d6d94f8452cf8b56d0531f40a00fb76f2.jpg)  
Figure 4.23

It is shown in calculus that the improper integral with a singularity at the left endpoint,

$$
\int _ { a } ^ { b } { \frac { d x } { ( x - a ) ^ { p } } } ,
$$

converges if and only if $0 < p < 1$ , and in this case, we define

$$
\int _ { a } ^ { b } { \frac { d x } { ( x - a ) ^ { p } } } = { \frac { ( b - a ) ^ { 1 - p } } { 1 - p } } .
$$

If $f$ is a function that can be written in the form

$$
f ( x ) = { \frac { g ( x ) } { ( x - a ) ^ { p } } } ,
$$

where $0 < p < 1$ and $g$ is continuous on $[ a , b ]$ , then the improper integral

$$
\int _ { a } ^ { b } f ( x ) d x
$$

also exists. We willapproximate this integral using the Composite Simpson's rule, provided that $g \in C ^ { 5 } [ a , b ]$ . In that case, we can construct the fourth Taylor polynomial, $P _ { 4 } ( \mathfrak { x } )$ ,for $g$ about $a$ ，

$$
\mathsf { \Pi } _ { 4 } ^ { p } ( x ) = g ( a ) + g ^ { \prime } ( a ) ( x - a ) + \frac { g ^ { \prime \prime } ( a ) } { 2 ! } ( x - a ) ^ { 2 } + \frac { g ^ { \prime \prime \prime } ( a ) } { 3 ! } ( x - a ) ^ { 3 } + \frac { g ^ { ( 4 ) } ( a ) } { 4 ! } ( x - a ) ^ { 4 }
$$

and write

$$
\int _ { a } ^ { b } f ( x ) d x = \int _ { a } ^ { b } { \frac { g ( x ) - P _ { 4 } ( x ) } { ( x - a ) ^ { p } } } d x + \int _ { a } ^ { b } { \frac { P _ { 4 } ( x ) } { ( x - a ) ^ { p } } } d x .
$$

Since $P ( x )$ is a polynomial, we can exactly determine the value of

$$
\int _ { a } ^ { b } { \frac { P _ { 4 } ( x ) } { ( x - a ) ^ { p } } } d x = \sum _ { k = 0 } ^ { 4 } \int _ { a } ^ { b } { \frac { g ^ { ( k ) } ( a ) } { k ! } } ( x - a ) ^ { k - p } d x = \sum _ { k = 0 } ^ { 4 } { \frac { g ^ { ( k ) } ( a ) } { k ! ( k + 1 - p ) } } ( b - a ) ^ { k + 1 - p }
$$

This is generally the dominant portion of the approximation, especially when the Taylo1 polynomial $P _ { 4 } ( x )$ agrees closely with $g ( x )$ throughout the interval $[ a , b ]$

To approximate the integral of $f$ , we need to add this value to the approximation of

$$
\int _ { a } ^ { b } { \frac { g ( x ) - P _ { 4 } ( x ) } { ( x - a ) ^ { p } } } d x .
$$

To determine this, we first define

$$
G ( x ) = { \left\{ \begin{array} { l l } { { \frac { g ( x ) \cdots P _ { 4 } ( x ) } { ( x - a ) ^ { p } } } , } & { { \mathrm { ~ i f ~ } } a < x \leq b , } \\ { 0 , } & { { \mathrm { ~ i f ~ } } x = a . } \end{array} \right. }
$$

Since $0 < p < 1$ and $P _ { 4 } ^ { ( k ) } ( a )$ agrees with $g ^ { ( k ) } ( a )$ for each $k = 0$ ,1, 2. 3,4, we have $G \in$ $C ^ { 4 } \{ a , b \}$ . This implies that the Composite Simpson's rule can be applied to approximate the integral of $G$ on $\{ a , b \}$ . Adding this approximation to the value in Eq. (4.46) gives an approximation to the improper integral of $f$ on $[ a , b ]$ , within the accuracy of the Composite Simpson's rule approximation.

We will use the Composite Simpson's rule with $h = 0 . 2 5$ to approximate the value of the improper integral

$$
\int _ { 0 } ^ { 1 } { \frac { e ^ { x } } { \sqrt { x } } } d x .
$$

Since the fourth Taylor polynomial for $e ^ { x }$ about $x = 0$ is

$$
P _ { 4 } ( x ) = 1 + x + { \frac { x ^ { 2 } } { 2 } } + { \frac { x ^ { 3 } } { 6 } } + { \frac { x ^ { 4 } } { 2 4 } } ,
$$

we have

$$
\begin{array} { l } { \displaystyle { \int _ { 0 } ^ { 1 } \frac { P _ { 4 } ( x ) } { \sqrt { x } } d x = \int _ { 0 } ^ { 1 } ( x ^ { - 1 / 2 } + x ^ { 1 / 2 } + \frac { 1 } { 2 } x ^ { 3 / 2 } + \frac { 1 } { 6 } x ^ { 5 / 2 } + \frac { 1 } { 2 4 } x ^ { 7 / 2 } ) d x } } \\ { \displaystyle { = \operatorname* { l i m } _ { M  0 ^ { + } } [ 2 x ^ { 1 / 2 } + \frac { 2 } { 3 } x ^ { 3 / 2 } + \frac { 1 } { 5 } x ^ { 5 / 2 } + \frac { 1 } { 2 1 } x ^ { 7 / 2 } + \frac { 1 } { 1 0 8 } x ^ { 9 / 2 } ] _ { M } ^ { 1 } } } \\ { \displaystyle { = 2 + \frac { 2 } { 3 } + \frac { 1 } { 5 } + \frac { 1 } { 2 1 } + \frac { 1 } { 1 0 8 } \approx 2 . 9 2 3 5 4 5 0 . } } \end{array}
$$

Table 4.14 lists the approximate values of

$$
G ( x ) = \left\{ \begin{array} { l l } { \frac { 1 } { \sqrt { x } } \left( e ^ { x } - P _ { 4 } ( x ) \right) , } & { \mathrm { w h e n ~ } 0 < x \leq 1 , } \\ { 0 , } & { \mathrm { w h e n ~ } x = 0 . } \end{array} \right.
$$

# Table 4.14

<table><tr><td></td></tr><tr><td>G(x) X</td></tr><tr><td>0.00 0</td></tr><tr><td>0.25 0.0000170</td></tr><tr><td>0.50 0.0004013</td></tr><tr><td>0.75 0.0026026</td></tr><tr><td>1.00 0.0099485</td></tr></table>

Applying the Composite Simpson's rule using these data gives

$$
\begin{array} { l } { \displaystyle \int _ { 0 } ^ { 1 } G ( x ) d x \approx \frac { 0 . 2 5 } { 3 } [ 0 + 4 ( 0 . 0 0 0 0 1 7 0 ) + 2 ( 0 . 0 0 0 4 0 1 3 ) } \\ { + \left. 4 ( 0 . 0 0 2 6 0 2 6 ) + 0 . 0 0 9 9 4 8 5 \right] = 0 . 0 0 1 7 6 9 1 . } \end{array}
$$

Hence,

$$
\int _ { 0 } ^ { 1 } { \frac { e ^ { x } } { \sqrt { x } } } d x \approx 2 . 9 2 3 5 4 5 0 + 0 . 0 0 1 7 6 9 1 = 2 . 9 2 5 3 1 4 1 .
$$

Thisresult isaccurate within the accuracy oftheComposite Simpson's rule approximation for the function $G$ . Since $| G ^ { ( 4 ) } ( x ) | < 1$ on[0,1], the errorisbounded by

$$
{ \frac { 1 - 0 } { 1 8 0 } } ( 0 . 2 5 ) ^ { 4 } = 0 . 0 0 0 0 2 1 7 .
$$

To approximatethe improper integral with a singularity atthe right endpoint, we could apply the technique we used above but expand in terms of the right endpoint $b$ instead of the left endpoint $\pmb { a }$ . Alternatively, we can make the substitution

$$
z = - x , \quad d z = - d x
$$

to change the improper integral into one of the form

$$
\int _ { a } ^ { b } f ( x ) d x = \int _ { - b } ^ { - a } f ( - z ) d z ,
$$

which has its singularity at the left endpoint. (See Figure 4.24.)

![](images/27c8a31f7dd6d25daaaf9e319903b6a6a70de46da34fa9a768fd8765400c9416.jpg)  
Figure 4.24

An improper integral with a singularity at $\pmb { c }$ ,where $a < c < b$ , is treated as the sum of improper integrals with endpoint singularities since

$$
\int _ { a } ^ { b } f ( x ) d x = \int _ { a } ^ { c } f ( x ) d x + \int _ { c } ^ { b } f ( x ) d x .
$$

The other type of improper integral involves infinite limits of integration. The basic integral of this type has the form

$$
\int _ { a } ^ { \infty } { \frac { 1 } { x ^ { p } } } d x ,
$$

for $p > 1$ . This is converted to an integral with left endpoint singularity at Oby making the integration substitution

$$
t = x ^ { - 1 } , d t = - x ^ { - 2 } d x , \mathrm { s o } d x = - x ^ { 2 } d t = - t ^ { - 2 } d t .
$$

Then

$$
\int _ { a } ^ { \infty } { \frac { 1 } { x ^ { p } } } d x = \int _ { 1 / a } ^ { 0 } - { \frac { t ^ { p } } { t ^ { 2 } } } d t = \int _ { 0 } ^ { 1 / a } { \frac { 1 } { t ^ { 2 - p } } } d t .
$$

In a similar manner, the variable change $\textit { \textbf { t } } = \textit { x } ^ { - 1 }$ converts the improper integral $\textstyle { \int _ { a } ^ { \infty } f ( x ) d x }$ into one that has a left endpoint singularity at zero:

$$
\int _ { a } ^ { \infty } f ( x ) d x = \int _ { 0 } ^ { 1 / a } t ^ { - 2 } f \left( { \frac { 1 } { t } } \right) d t .
$$

It can now be approximated using a quadrature formula of the type described earlier.

# EXAMPLE 2

To approximate the value of the improper integral

$$
I = \int _ { 1 } ^ { \infty } x ^ { - 3 / 2 } \sin \frac { 1 } { x } d x ,
$$

we make the change of variable $t = x ^ { - 1 }$ to obtain

$$
I = \int _ { 0 } ^ { 1 } t ^ { - 1 / 2 } \sin t d t .
$$

The fourth Taylor polynomial, $P _ { 4 } ( t )$ ,for sin $t$ about 0 is

$$
P _ { 4 } ( t ) = t - \frac { 1 } { 6 } t ^ { 3 } ,
$$

so

$$
G ( t ) = \left\{ { \begin{array} { l l } { \displaystyle \sin t - t + { \frac { 1 } { 6 } } t ^ { 3 } } , & { { \mathrm { ~ i f ~ } } 0 < t \leq 1 } \\ { 0 , } & { { \mathrm { ~ i f ~ } } t = 0 } \end{array} } \right.
$$

is in $c ^ { 4 } \{ 0 , 1 \}$ , and we have

$$
{ \begin{array} { r l } & { I = \displaystyle \int _ { 0 } ^ { 1 } t ^ { 1 / 2 } - \frac { 1 } { 6 } t ^ { 5 / 2 } d t + \displaystyle \int _ { 0 } ^ { 1 } \frac { \sin t - t + \frac { 1 } { 6 } t ^ { 3 } } { t ^ { 1 / 2 } } d t } \\ & { \quad = \displaystyle \left[ \frac { 2 } { 3 } t ^ { 3 / 2 } - \frac { 1 } { 2 1 } t ^ { 7 / 2 } \right] _ { 0 } ^ { 1 } + \displaystyle \int _ { 0 } ^ { 1 } \frac { \sin t - t + \frac { 1 } { 6 } t ^ { 3 } } { t ^ { 1 / 2 } } d t } \\ & { \quad = 0 . 6 1 9 0 4 7 6 1 + \displaystyle \int _ { 0 } ^ { 1 } \frac { \sin t - t + \frac { 1 } { 6 } t ^ { 3 } } { t ^ { 1 / 2 } } d t . } \end{array} }
$$

Applying the Composite Simpson's rule with $n = 1 6$ to the remaining integral gives

$$
I = 0 . 0 0 1 4 8 9 0 0 9 7 + 0 . 6 1 9 0 4 7 6 1 = 0 . 6 2 0 5 3 6 6 1 ,
$$

which is accurate to within $4 . 0 \times 1 0 ^ { - 8 }$

# ExErcise Set 4.9

1.Use Simpson's Composite rule and the given values of $\pmb { n }$ to approximate the following im-proper integrals.

$$
\begin{array} { l l l } { { \displaystyle \int _ { 0 } ^ { 1 } x ^ { - 1 / 4 } \sin x d x , \quad n = 4 \quad } } & { { \mathrm { ~ } } } & { { \mathrm { ~ b } . \quad \displaystyle \int _ { 0 } ^ { 1 } \frac { e ^ { 2 x } } { \sqrt [ 5 ] { x ^ { 2 } } } d x , \quad n = 6 } } \\ { { \displaystyle \int _ { 1 } ^ { 2 } \frac { \ln x } { ( x - 1 ) ^ { 1 / 5 } } d x , \quad n = 8 \quad } } & { { \mathrm { ~ } } } & { { \mathrm { ~ d } . \quad \displaystyle \int _ { 0 } ^ { 1 } \frac { \cos 2 x } { x ^ { 1 / 3 } } d x , \quad n = 6 } } \end{array}
$$

2. Use the Composite Simpson's rule and the given values of $n$ to approximate the following improper integrals.

$$
\int _ { 0 } ^ { 1 } { \frac { e ^ { - x } } { \sqrt { 1 - x } } } d x , \quad n = 6 \qquad { \bf b . } \quad \int _ { 0 } ^ { 2 } { \frac { x e ^ { x } } { \sqrt [ 3 ] { ( x - 1 ) ^ { 2 } } } } d x , \quad n = 8
$$

3. Use the transformation $t = x ^ { - 1 }$ and then the Composite Simpson's rule and the given values of $n$ to approximate the following improper integrals.

$$
{ \begin{array} { r l } { \int _ { 1 } ^ { \infty } { \frac { 1 } { x ^ { 2 } + 9 } } d x , \quad n = 4 \quad \quad \quad } & { { \mathrm { \bf ~ b . } } \quad \int _ { 1 } ^ { \infty } { \frac { 1 } { 1 + x ^ { 4 } } } d x , \quad n = 4 } \\ { \int _ { 1 } ^ { \infty } { \frac { \cos x } { x ^ { 3 } } } d x , \quad n = 6 \quad \quad \quad } & { { \mathrm { \bf ~ d . } } \quad \int _ { 1 } ^ { \infty } x ^ { - 4 } \sin x d x , \quad n = 6 } \end{array} }
$$

4. The improper integral $\textstyle { \int _ { 0 } ^ { \infty } f ( x ) d x }$ cannot be converted into an integral with finite limits using the substitution $t = 1 / x$ because the limit at zero becomes infinite. The problem is resolved by first writing $\begin{array} { r } { \int _ { 0 } ^ { \infty } f ( x ) \ d x = \int _ { 0 } ^ { 1 } f ( x ) \ d x + \int _ { 1 } ^ { \infty } f ( x ) \ d x } \end{array}$ . Apply this technique to approximate the following improper integrals to within $\operatorname { i } \dot { 0 } ^ { - 6 }$

$$
\int _ { 0 } ^ { \infty } { \frac { 1 } { 1 + x ^ { 4 } } } d x
$$

$$
{ \textbf { b } } \int _ { 0 } ^ { \infty } { \frac { 1 } { ( 1 + x ^ { 2 } ) ^ { 3 } } } d x
$$

5. Suppose a body of mass $m$ is traveling vertically upward starting at the surface of the earth. If allresistance except gravity is neglected,the escape velocity $\pmb { \nu }$ is given by

$$
v ^ { 2 } = 2 g R \int _ { 1 } ^ { \infty } z ^ { - 2 } \ d z , \quad { \mathrm { w h e r e ~ } } z = { \frac { x } { R } } ,
$$

$R = 3 9 6 0 \mathrm { m i }$ is the radius ofthe earth and $g = 0 . 0 0 6 0 9 \mathrm { \ m i } / \mathrm { s } ^ { 2 }$ is the force of gravity at the earth's surface. Approximate the escape velocity $v$

6. The Laguerre polynomials $\{ L _ { 0 } ( x ) , L _ { 1 } ( x ) \ldots \}$ form an orthogonal set on $\left[ 0 , \infty \right)$ and satisfy $\begin{array} { r } { \int _ { 0 } ^ { \infty } e ^ { - x } L _ { i } ( x ) L _ { j } ( x ) d x = 0 } \end{array}$ for $i \neq j$ (SeeSection8.2.)Thepolyomial $L _ { n } ( x )$ has $n$ distinct zeros $x _ { 1 } , x _ { 2 } , \ldots , x _ { n }$ in $[ 0 , \infty )$ . Let

$$
c _ { n , i } = \int _ { 0 } ^ { \infty } e ^ { - x } \prod _ { j = 1 \atop j \neq i } ^ { n } { \frac { x - x _ { j } } { x _ { i } - x _ { j } } } d x .
$$

Show that the quadrature formula

$$
\int _ { 0 } ^ { \infty } f ( x ) e ^ { - x } d x = \sum _ { i = 1 } ^ { n } c _ { n , i } f ( x _ { i } )
$$

has degree of precision $2 n - 1$ . (Hint: Follow the steps in the proof of Theorem 4.7.)

7．The Laguerre polynomials $L _ { 0 } ( x ) = 1 , L _ { 1 } ( x ) = 1 - x , L _ { 2 } ( x ) = x ^ { 2 } - 4 x + 2 ,$ and $L _ { 3 } ( x ) =$ $- x ^ { 3 } + 9 x ^ { 2 } - 1 8 x + 6$ are derived in Exercise 11 of Section 8.2. As shown in Exercise 6, these polynomials are useful in approximating integrals of the form

$$
\int _ { 0 } ^ { \infty } e ^ { - x } f ( x ) d x = 0 .
$$

a.Derive the quadrature formula using $n = 2$ and the zeros of $L _ { 2 } ( x )$ b.Derive the quadrature formula using $n = 3$ and the zeros of $L _ { 3 } ( x )$ ·

8.Use the quadrature formulas derived in Exercise 7 to approximate the integral

$$
\int _ { 0 } ^ { \infty } { \sqrt { x } } e ^ { - x } d x .
$$

9.Use the quadrature formuals derived in Exercise 7 to approximate the integral

$$
\int _ { - \infty } ^ { \infty } { \frac { 1 } { 1 + x ^ { 2 } } } d x .
$$

# 4.10 Survey of Methods and Software

In this chapter we considered approximating integrals of functions of one,two, or three variables and approximating the derivatives of a function of a single real variable.

The Midpoint rule,Trapezoidal rule, and Simpson's rule were studied to introduce the techniques and error analysis of quadrature methods. Composite Simpson's rule is easy to use and produces accurate approximations unless the function oscillates in a subinterval of the interval of integration. Adaptive quadrature can be used if the function is suspected of oscillatory behavior. To minimize the number of nodes while maintaining accuracy, we studied Gaussian quadrature. Romberg integration was introduced to take advantage of the easily applied Composite Trapezoidal rule and extrapolation.

Most software for integrating a function of a single real variable is based on the adaptive approach or extremely accurate Gaussian formulas. Cautious Romberg integration is an adaptive technique that includes a check to make sure that the integrand is smoothly behaved over subintervals of the integral of integration. This method has been successfully used in software libraries. Multiple integrals are generally approximated by extending good adaptive methods to higher dimensions. Gaussian-type quadrature is also recommended to decrease the number of function evaluations.

The main routines in both the IMSL and NAG Libraries are based on QUADPACK: A Subroutine Package for Automatic Integration by R. Piessens,E. de Doncker-Kapenga, C. W. Uberhuber,and D.K. Kahaner published by Springer-Verlag in 1983 [PDUK]. The routines are also available as public domain software, at http://www.netlib.org/quadpack.

The IMSL Library contains the function QDAG,which is an adaptive integration scheme based on the 21-point Gaussian-Kronrod rule using the 1O-point Gaussian rule for error estimation. The Gaussian rule uses the ten points $x _ { 1 } , \ldots , x _ { 1 0 }$ and weights $x _ { 1 1 } , \ldots , x _ { 2 1 }$ $\boldsymbol { v } _ { 1 } , \ldots , \boldsymbol { v } _ { 2 1 }$ $\scriptstyle \sum _ { i = 1 } ^ { 2 1 } v _ { i } f ( x _ { i } )$ $x _ { 1 } , \ldots , x _ { 1 0 }$ $f$ only at 21 points. If independent 10- and 21-point Gaussian rules were used,31 function evaluations would be needed. This procedure permits endpoint singularities in the integrand.

Other IMSL subroutines are QDAGS, which alows for end point singularities; QDAGP, which allows user-specified singularities; QDAGI, which allows infinite intervals of integration; and QDNG,which is a nonadaptive procedure for smooth functions. The subroutine TWODQ uses the Gauss-Kronrod rules to integrate a function of two variables. There is also a subroutine QAND to use Gaussian quadrature to integrate a function of $\pmb { n }$ variables over $\pmb { n }$ intervals of the form $[ a _ { i } , b _ { i } ]$

The NAG Library includes the subroutine D01AJF to compute the integral of $f$ over the interval $[ a , b ]$ using an adaptive method based on Gaussian Quadrature using Gauss 10-point and Kronrod 21-point rules. The subroutine DO1AHF is used to approximate ${ \textstyle \int _ { a } ^ { b } } f ( x ) \ d x$ using a family of Gaussian-type formulas based on 1,3,5,7,15, 31, 63, 127,and 255 nodes. These interlacing high-precision rules are due to Patterson [Pat] and are used in an adaptive manner. The subroutine DO1GBF is for multiple integrals and D01GAF approximates an integral given only data points instead of the function. NAG includes many other subroutines for approximating integrals.

The Maple function call

computes the definite integral $\textstyle \int _ { a } ^ { b } f ( x ) d x$ . The numerical method applies singularity handling routines and then uses Clenshaw-Curtis quadrature,which is described in [CC]. If this fails,due to singularities in or near the interval, then an adaptive double-exponential quadrature method is applied. The adaptive Newton-Cotes formula can be applied by specifying the option _NCrule in the Maple function call

>int(f, ${ \pmb x } = _ { \mathbf { a } }$ ..b,digits,_NCrule);

The method attempts to achieve a relative eror tolerance $0 . 5 \times 1 0 ^ { ( 1 - \mathfrak { D i g i t s } ) }$ , where Digits is a variable in Maple that specifies the number of digits of rounding Maple uses for numer-ical calculation. The default value for Digits is 1O,but it can be changed to any positive integer n by the command Digits : $\mathbf { \mu } = \mathbf { n }$ ; The MATLAB command QUAD approximates the definite integral $\textstyle \int _ { a } ^ { b } f ( x ) d x$ using an adaptive Simpson's rule, and QUAD8 approximates the definite integral using an adaptive eight-panel Newton-Cotes rule.

Although numerical differentiation is unstable,derivative approximation formulas are needed for solving differential equations. The NAG Library includes the subroutine DO4AAF for the numerical differentiation of a function of one real variable with differentiation to the fourteenth derivative being possible. The IMSL function DERIV uses an adaptive change in step size for finite differences to approximate the first, second,or third, derivative of $f$ at $x$ to within a given tolerance. IMSL also includes the subroutine QDDER to compute the derivatives of a function defined on a set of points using quadratic inter-polation. Both packages allow the differentiation and integration of interpolatory cubic splines constructed by the subroutines mentioned in Section 3.4.

For further reading on numerical integration we recommend the books by Engels [E] and by Davis and Rabinowitz [DR]. For more information on Gaussian quadrature see Stroud and Secrest [StS]. Books on multiple integrals include those by Stroud [Stro] and the recent book by Sloan and Joe [SJ].

CHAPTER

# 5

# Initial-Value Problems for Ordinary Differential Equations

tions is described by the second-order differential equation

$$
\frac { d ^ { 2 } \theta } { d t ^ { 2 } } + \frac { g } { L } \sin \theta = 0 ,
$$

![](images/b496dc37979d08be74ee03f57b4df23329d1193a4baaad9cd02d05c4f54fc915.jpg)

where $\pmb { L }$ is the length of the pendulum, $g \approx 3 2 . 1 7 ~ \mathrm { f t } / s ^ { 2 }$ is the gravitational constant of the earth, and $\pmb { \theta }$ is the angle the pendulum makes with the vertical. If, in addition, we specify the position of the pendulum when the motion begins, $\pmb { \theta } ( t _ { 0 } ) = \pmb { \theta } _ { 0 } ,$ , and its velocity at that point, $\theta ^ { \prime } ( t _ { 0 } ) = \theta _ { 0 } ^ { \prime }$ ,we have what is called an initial-value problem.

![](images/badf11d577de4f6686b665c9c6aa28d58b9ca8e2ac10cd91adedab08d1189d52.jpg)

For small values of $\pmb \theta$ , the approximation $\theta \approx$ sin $\pmb \theta$ can be used to simplify this problem to the linear initial-value problem

$$
\frac { d ^ { 2 } \theta } { d t ^ { 2 } } + \frac { g } { L } \theta = 0 , \quad \theta ( t _ { 0 } ) = \theta _ { 0 } , \quad \theta ^ { \prime } ( t _ { 0 } ) = \theta _ { 0 } ^ { \prime } .
$$

This problem can be solved by a standard differential-equation technique. For larger values of $\pmb \theta$ , approximation methods must be used. A problem of this type is considered in Exercise 6 of Section 5.9.

Any textbook on ordinary differential equations details a number of methods for explicitly finding solutions to first-order initial-value problems. In practice,however, few of the problems originating from the study of physical phenomena can be solved exactly.

The first part of this chapter is concerned with approximating the solution $y ( t )$ to a problem of the form

$$
{ \frac { d y } { d t } } = f ( t , y ) , \quad \mathrm { f o r } a \leq t \leq b ,
$$

subject to an initial condition

$$
y ( a ) = \alpha .
$$

Later in the chapter we deal with the extension of these methods to a system of first-order differential equations in the form

$$
{ \begin{array} { l } { { \frac { d y _ { 1 } } { d t } } = f _ { 1 } ( t , y _ { 1 } , y _ { 2 } , \dots , y _ { n } ) , } \\ { { \frac { d y _ { 2 } } { d t } } = f _ { 2 } ( t , y _ { 1 } , y _ { 2 } , \dots , y _ { n } ) , } \\ { ~ \vdots } \\ { { \frac { d y _ { n } } { d t } } = f _ { n } ( t , y _ { 1 } , y _ { 2 } , \dots , y _ { n } ) , } \end{array} }
$$

for $a \leq t \leq b$ , subject to the initial conditions

$$
y _ { 1 } ( a ) = \alpha _ { 1 } , \quad y _ { 2 } ( a ) = \alpha _ { 2 } , \quad \ldots , \quad y _ { n } ( a ) = \alpha _ { n } .
$$

We also examine the relationship of a system of this type to the general $\pmb { n }$ th-order initialvalue problem of the form

$$
y ^ { ( n ) } = f ( t , y , y ^ { \prime } , y ^ { \prime \prime } , \ldots , y ^ { ( n - 1 ) } ) ,
$$

for $a \leq t \leq b$ , subject to the initial conditions

$$
y ( a ) = \alpha _ { 1 } , \quad y ^ { \prime } ( a ) = \alpha _ { 2 } , \quad \ldots , \quad y ^ { n - 1 } ( a ) = \alpha _ { n } .
$$

# 5.1 The Elementary Theory of Initial-Value Problems

Differential equations are used to model problems in science and engineering that involve the change of some variable with respect to another. Most of these problems require the solution to an initial-value problem, that is,the solution to a differential equation that satisfies a given initial condition.

In most real-life situations,the differential equation that models the problem is too complicated to solve exactly,and one of two approaches is taken to approximate the solution.The first approach is to simplify the differential equation to one that can be solved exactly and then use the solution of the simplified equation to approximate the solution to the original equation. The other approach, which we will examine in this chapter, uses methods for approximating the solution of the original problem. This is the approach that is most commonly taken since the approximation methods give more accurate results and realistic error information.

The methods that we consider in this chapter do not produce a continuous approximation to the solution of the initial-value problem. Rather, approximations are found at certain specified, and often equally spaced, points. Some method of interpolation, commonly Hermite, is used if intermediate values are needed.

We need some definitions and results from the theory of ordinary differential equations before considering methods for approximating the solutions to initial-value problems. Initial-value problems obtained by observing physical phenomena generally only approximate the true situation, so we need to know whether smallchanges in the statement of the problem introduce correspondingly small changes in the solution. This is also important because of the introduction of roundoff error when numerical methods are used.

# Definition 5.1

A function $f ( t , y )$ is said to satisfy a Lipschitz condition in the variable y on a set $D \subset \mathbb { R } ^ { 2 }$ if a constant $L > 0$ exists with

$$
| f ( t , y _ { 1 } ) - f ( t , y _ { 2 } , ) | \leq L | y _ { 1 } - y _ { 2 } | ,
$$

whenever $( t , y _ { 1 } ) , ( t , y _ { 2 } ) \in D$ . The constant $L$ is called a Lipschitz constant for $f$

# EXAMPLE 1

If $D = \{ ( t , y ) \mid 1 \leq t \leq 2 , - 3 \leq y \leq 4 \}$ and $f ( t , y ) = t | y |$ , then for each pair of points $( t , y _ { 1 } )$ and $( t , y _ { 2 } )$ in $D$ , we have

$$
| f ( t , y _ { 1 } ) - f ( t , y _ { 2 } ) | = | t | y _ { 1 } | - t | y _ { 2 } | | = | t | | | y _ { 1 } | - | y _ { 2 } | | \leq 2 | y _ { 1 } - y _ { 2 } | .
$$

Thus, $f$ satisfies a Lipschitz condition on $D$ in the variable $y$ with Lipschitz constant 2. The smallest value possible for the Lipschitz constant for this problem is $L = 2$ , since, for example,

$$
| f ( 2 , 1 ) - f ( 2 , 0 ) | = | 2 - 0 | = 2 | 1 - 0 | .
$$

# Definition 5.2

A set $D \subset \mathbb { R } ^ { 2 }$ is said to be convex if whenever $( t _ { 1 } , y _ { 1 } )$ and $( t _ { 2 } , y _ { 2 } )$ belong to $D$ and $\lambda$ is in [0, 1], the point $( ( 1 - \lambda ) t _ { 1 } + \lambda t _ { 2 }$ ， $( 1 - \lambda ) y _ { 1 } + \lambda y _ { 2 } )$ also belongs to $D$

In geometric terms, Definition 5.2 states that a set is convex provided that whenever two points belong to the set, the entire straight-line segment between the points also belongs to the set. (See Figure 5.1.) The sets we consider in this chapter are generally of the

form D = {(t,y)| a ≤ t ≤ b,-o < y < oo} for some constants a and b. It is easy to verify (see Exercise 5) that these sets are convex.

![](images/12d417167bd09a02a903bfaf1121d7516b8755152428b96ed7c9ba6d3bb2f928.jpg)  
Figure 5.1

Suppose $f ( t , y )$ is defined on a convex set $D \subset \mathbb { R } ^ { 2 }$ . If a constant $L > 0$ exists with

$$
\left| { \frac { \partial f } { \partial y } } ( t , y ) \right| \leq L , \quad { \mathrm { f o r ~ a l l ~ } } ( t , y ) \in D ,
$$

then f satisfies a Lipschitz condition on D in the variable y with Lipschitz constant L.

The proof ofTeorem5.3isdisussd inExercise4; tissimilartothe profof the corresponding result for functions of one variable discussed in Exercise 25 of Section 1.1.

As the next theorem willshow, it is often of significant interest to determine whether the function involved in an initial-value problem satisfies a Lipschitz condition in its second variable,and condition (5.1) is'generally easier to apply than the definition. We should note, however, that Theorem 5.3 gives only sufficient conditions for a Lipschitz condition to hold.The function in Example 1, for instance,satisfies a Lipschitz condition, but the partial derivative with respect to y does not exist when $y = 0$

The following theorem is a version of the fundamental existence and uniquenes theorem for first-order ordinary diferential equations. Although the theorem can be proved with the hypothesis reduced somewhat, this form of the theorem is sufficient for our purposes.(The proof of the theorem, in approximately this form, can be found in [BiR, pp. 142-155].)

# Theorem 5.4

Suppose that $D = \{ ( t , y ) | a \leq t \leq b , - \infty < y < \infty \}$ and that $f ( t , y )$ is continuous on $D$ .If $f$ satisfies a Lipschitz condition on $D$ in the variable $y$ ,thentheinitial-valueproblem

$$
y ^ { \prime } ( t ) = f ( t , y ) , \quad a \leq t \leq b , \quad y ( a ) = \alpha ,
$$

has a unique solution $y ( t )$ for $a \leq t \leq b$

EXAMPLE 2 Consider the initial-value problem

$$
y ^ { \prime } = 1 + t \sin ( t y ) , \quad 0 \leq t \leq 2 , \quad y ( 0 ) = 0 .
$$

Holding $t$ constant and applying the Mean Value Theorem to the function

$$
f ( t , y ) = 1 + t \sin ( t y ) ,
$$

we find that when $y _ { 1 } < y _ { 2 }$ ,a number $\xi$ in $( y _ { 1 } , y _ { 2 } )$ exists with

$$
{ \frac { f ( t , y _ { 2 } ) - f ( t , y _ { 1 } ) } { y _ { 2 } - y _ { 1 } } } = { \frac { \partial } { \partial y } } f ( t , \xi ) = t ^ { 2 } \cos ( \xi t ) .
$$

Thus,

$$
| f ( t , y _ { 2 } ) - f ( t , y _ { 1 } ) | = | y _ { 2 } - y _ { 1 } | | t ^ { 2 } \cos ( \xi t ) | \leq 4 | y _ { 2 } - y _ { 1 } | ,
$$

and $f$ satisfes a Lipschitz condition in the variable $y$ with Lipschitz constant $L \ = \ 4$ Since,additionally, $f ( t , y )$ is continuous when $0 \leq t \leq 2$ and $- \infty < y < \infty$ ,Theorem 5.4 implies that a unique solution exists to this initial-value problem.

If you havecompleted a course in differential equations you might try to find the exact solution to this problem.

Now that we have,to some extent, taken care of the question of when initial-value problems have unique solutions,we can move to the other question posed earlier in the section:

How do we determine whether a particular problem has the property that small changes,or perturbations,in the statement of the problem introduce correspondingly small changes in the solution?

As usual, we first need to give a workable definition to express this concept.

# Definition 5.5

The initial-value problem

$$
\frac { d y } { d t } = f ( t , y ) , \quad a \leq t \leq b , \quad y ( a ) = \alpha ,
$$

is said to be a well-posed problem if:

1. A unique solution, $y ( t )$ , to the problem exists;

2.For any $\varepsilon > 0$ , there exists a positive constant $k ( \varepsilon )$ , such that whenever $| \varepsilon _ { 0 } | < \varepsilon$ and $\delta ( t )$ is continuous with $| \delta ( t ) | < \varepsilon$ on $[ a , b ]$ ,a unique solution, $z ( t )$ 、to

$$
\frac { d z } { d t } = f ( t , z ) + \delta ( t ) , \quad a \leq t \leq b , \quad z ( a ) = \alpha + \varepsilon _ { 0 } ,
$$

exists with

$$
| z ( t ) - y ( t ) | < k ( \varepsilon ) \varepsilon , \quad { \mathrm { f o r ~ a l l ~ } } a \leq t \leq b .
$$

The problem specified by Eq. (5.3) is called a perturbed problem associated with the original problem (5.2). It assumes the possibility of an error $\delta ( t )$ being introduced in the statement of the differential equation,as well as an error $\varepsilon _ { 0 }$ being present in the initial condition.

Numerical methods will always be concerned with solving a perturbed problem since any roundoff error introduced in the representation perturbs the original problem. Unless the original problem is well-posed, there is little reason to expect that the numerical solution to a perturbed problem will accurately approximate the solution to the original problem.

The following theorem specifies conditions that ensure that an initial-value problem is well-posed. The proof of this theorem can be found in [BiR, pp. 142-147].

# Theorem 5.6

Suppose $D = \{ ( t , y ) \mid a \leq t \leq b$ and $- \infty < y < \infty \}$ .If $f$ is continuous and satisfies a Lipschitz condition in the variable $y$ on the set $D$ , then the initial-value problem

$$
\frac { d y } { d t } = f ( t , y ) , \quad a \leq t \leq b , \quad y ( a ) = \alpha
$$

is well-posed.

# EXAMPlE 3

Let $D = \{ ( t , y ) \mid 0 \leq t \leq 1 , - \infty < y < \infty \}$ ,and consider the initial-value problem

$$
\frac { d y } { d t } = y - t ^ { 2 } + 1 , \quad 0 \leq t \leq 2 , \quad y ( 0 ) = 0 . 5 .
$$

Since

$$
\left| \frac { \partial ( y - t ^ { 2 } + 1 ) } { \partial y } \right| = | 1 | = 1 ,
$$

Theorem 5.3 implies that $f ( t , y ) = y - t ^ { 2 } + 1$ satisfies a Lipschitz condition in $y$ on $D$ with Lipschitz constant 1. Since $f$ is continuous on $D$ ,Theorem 5.6 implies that the problem is well-posed.

To verify this directly, consider the perturbed problem

$$
\frac { d z } { d t } = z - t ^ { 2 } + 1 + \delta , \quad 0 \leq t \leq 2 , \quad z ( 0 ) = 0 . 5 + \varepsilon _ { 0 } ,
$$

where $\pmb { \delta }$ and $\pmb { \varepsilon _ { 0 } }$ are constants. The solutions to Eqs. (5.4) and (5.5) are

$$
y ( t ) = ( t + 1 ) ^ { 2 } - 0 . 5 e ^ { t } \quad \mathrm { a n d } \quad z ( t ) = ( t + 1 ) ^ { 2 } + ( \delta + \varepsilon _ { 0 } - 0 . 5 ) e ^ { t } - \delta ,
$$

respectively. If $| \delta | < \varepsilon$ and $| \varepsilon _ { 0 } | < \varepsilon$ ,then

$$
| y ( t ) - z ( t ) | = | ( \delta + \varepsilon _ { 0 } ) e ^ { t } - \delta | \leq | \delta + \varepsilon _ { 0 } | e ^ { 2 } + | \delta | \leq ( 2 e ^ { 2 } + 1 ) \varepsilon ,
$$

for all $t$ . Thus, the problem (5.4) is well-posed with $k ( \varepsilon ) = 2 e ^ { 2 } + 1$ for all $\varepsilon > 0$

Maple can be used to solve many initial-value problems. Consider the problem

$$
\frac { d y } { d t } = y - t ^ { 2 } + 1 , \quad 0 \leq t \leq 2 , \quad y ( 0 ) = 0 . 5 .
$$

To define the differential equation, enter

$$
\scriptstyle \mathtt { > d e q : = D ( y ) ( t ) = y ( t ) - t * t + 1 } ;
$$

and the initial condition

$$
> \mathrm { i n i t : } = \mathrm { y } \left( 0 \right) = 0 \ : . 5 ;
$$

The names deq and init are chosen by the user. The command to solve the initial-value problems is

$$
> \mathrm { d e q s o l : = d s o l v e \left( \left\{ d e q , i n i t \right\} , y ( t ) \right) ; }
$$

The response is

$$
{ \mathrm { d e q s o l : } } = y ( t ) = 1 + t ^ { 2 } + 2 t - { \frac { 1 } { 2 } } e ^ { t }
$$

To use the solution to obtain y(1.5), we enter

>q:=rhs(deqsol); evalf(subs(t=1.5,q));

with the result 4.009155465.

The function rhs is used to assign the solution of the initial-value problem to the function $\pmb q$ , which we then evaluate at $t = 1 . 5$ . The function dsolve can fail if an explicit solution to the initial-value problem cannot be found. For example, the command

$$
{ \bf \gamma } \mathsf { d e q s o l 2 : } = \mathbf { d s o l v e } \left( \left. \mathbb { D } \left( \mathbf { y } \right) \left( \mathbf { t } \right) = \mathbf { 1 } + \mathbf { t } \ast \mathbf { s i n } \left( \mathbf { t } \ast \mathbf { y } \left( \mathbf { t } \right) \right) , \mathbf { y } \left( 0 \right) = 0 \right\} , \mathbf { y } \left( \mathbf { t } \right) \right) ;
$$

does not succeed because an explicit solution cannot be found. In this case a numerical method must be used.

# EXERCIsE SEt 5.1

1.Use Theorem 5.4 to show that each of the following initial-value problems has a unique solution,and find the solution.

$$
\begin{array} { r l } & { y ^ { \prime } = y \cos t , \quad 0 \leq t \leq 1 , \quad y ( 0 ) = 1 . } \\ & { y ^ { \prime } = \displaystyle \frac { 2 } { t } y + t ^ { 2 } e ^ { t } , \quad 1 \leq t \leq 2 , \quad y ( 1 ) = 0 . } \\ & { } \\ & { y ^ { \prime } = - \displaystyle \frac { 2 } { t } y + t ^ { 2 } e ^ { t } , \quad 1 \leq t \leq 2 , \quad y ( 1 ) = \sqrt { 2 } e . } \\ & { y ^ { \prime } = \displaystyle \frac { 4 t ^ { 3 } y } { 1 + t ^ { 4 } } , \quad 0 \leq t \leq 1 , \quad y ( 0 ) = 1 . } \end{array}
$$

2.For each choice of $f ( t , y )$ given in parts (a) (d):

i.Does $f$ satisfy a Lipschitz condition on $D = \{ ( t , y ) | 0 \leq t \leq 1 , - \infty < y < \infty \}$ ？ ii.Can Theorem 5.6 be used to show that the initial-value problem

$$
y ^ { \prime } = f ( t , y ) , \quad 0 \leq t \leq 1 , \quad y ( 0 ) = 1 ,
$$

is well-posed?

a. $f ( t , y ) = t ^ { 2 } y + 1$ $\begin{array} { l l } { { \mathbf { b } , } } & { { f ( t , y ) = t y } } \\ { { \mathbf { d } . } } & { { f ( t , y ) = - t y + \displaystyle \frac { 4 t } { y } } } \end{array}$   
c. $f ( t , y ) = 1 - y$

3.For the following initial-value problems,show that the given equation implicitly defines a solution.Approximate $y ( 2 )$ using Newton's method.

$$
\begin{array} { l } { { y ^ { \prime } = - { \frac { y ^ { 3 } + y } { ( 3 y ^ { 2 } + 1 ) t } } , 1 \le t \le 2 , y ( 1 ) = 1 ; \ y ^ { 3 } t + y t = 2 } } \\ { { \qquad \quad } } \\ { { y ^ { \prime } = - { \frac { y \cos t + 2 t e ^ { y } } { \sin t + t ^ { 2 } e ^ { y } + 2 } } , 1 \le t \le 2 , y ( 1 ) = 0 ; \ y \sin t + t ^ { 2 } e ^ { y } + 2 y = 1 } } \end{array}
$$

4.Prove Theorem 5.3 by applying the Mean Value Theorem to $f ( t , y )$ , holding $t$ fixed.

5.Show that, for any constants $^ { a }$ and $b$ , the set $D = \{ ( t , y ) \mid a \leq t \leq b , - \infty < y < \infty \}$ is convex.

6. Suppose the perturbation $\delta ( t )$ is proportional to $t$ ,that is, $\delta ( t ) = \delta t$ for some constant $\delta$ . Show directly that the following initial-value problems are well-posed.

$$
\begin{array} { r l } & { y ^ { \prime } = 1 - y , \quad 0 \leq t \leq 2 , \quad y ( 0 ) = 0 } \\ & { y ^ { \prime } = t + y , \quad 0 \leq t \leq 2 , \quad y ( 0 ) = - 1 } \\ & { } \\ & { y ^ { \prime } = \frac { 2 } { t } y + t ^ { 2 } e ^ { t } , \quad 1 \leq t \leq 2 , \quad y ( 1 ) = 0 } \\ & { } \\ & { y ^ { \prime } = - \frac { 2 } { t } y + t ^ { 2 } e ^ { t } , \quad 1 \leq t \leq 2 , \quad y ( 1 ) = \sqrt { 2 } e } \end{array}
$$

7.Picard's method for solving the initial-value problem

$$
y ^ { \prime } = f ( t , y ) , \quad a \leq t \leq b , \quad y ( a ) = \alpha ,
$$

is described as follows: Let $y _ { 0 } ( t ) = \alpha$ for each $t$ in $[ a , b ]$ . Define a sequence $\{ y _ { k } ( t ) \}$ of func-tions by

$$
y _ { k } ( t ) = \alpha + \int _ { a } ^ { t } f ( \tau , y _ { k - 1 } ( \dot { \tau } ) ) d \tau , \quad k = 1 , 2 , \dots .
$$

a.Integrate y' = f(t,y(t)),and use the initial condition to derive Picard's method.

b.Generate $y _ { 0 } ( t ) , y _ { 1 } ( t ) , y _ { 2 } ( t )$ 、and $y _ { 3 } ( t )$ for the initial-value problem

$$
y ^ { \prime } = - y + t + 1 , \quad 0 \leq t \leq 1 , \quad y ( 0 ) = 1 .
$$

c.Compare the result in part (b) to the Maclaurin series of the actual solution y(t)= t+e-'.

# 5.2 Euler's Method

Although Euler's method is seldom used in practice,the simplicity of its derivation can be used to illustrate the techniques involved in the construction of some of the more advanced techniques, without the cumbersome algebra that accompanies these constructions.

The object of the method is to obtain an approximation to the well-posed initial-value problem

$$
\frac { d y } { d t } = f ( t , y ) , \quad a \leq t \leq b , \quad y ( a ) = \alpha .
$$

In actuality, a continuous approximation to the solution $y ( t )$ will not be obtained; instead, approximations to $y$ will be generated at various values, called mesh points, in the interval $[ a , b ]$ . Once the approximate solution is obtained at the points, the approximate solution at other points in the interval are found by interpolation.

We first make the stipulation that the mesh points are equally distributed throughout the interval $[ a , b ]$ Thiscoditionisensuredbychoosingapositiveinteger $N$ and selecting the mesh points

$$
t _ { i } = a + i h , \quad \mathrm { f o r } \operatorname { e a c h } i = 0 , 1 , 2 , \ldots , N .
$$

The common distance between the points $h = ( b - a ) / N$ is called the step size.

We will use Taylor's Theorem to derive Euler's method. Suppose that $y ( t )$ ，the unique solution to (5.6), has two continuous derivatives on $[ a , b ]$ ，so that for each $i = 0 , 1 , 2 , \ldots , N - 1 ,$

$$
y ( t _ { i + 1 } ) = y ( t _ { i } ) + ( t _ { i + 1 } - t _ { i } ) y ^ { \prime } ( t _ { i } ) + { \frac { ( t _ { i + 1 } - t _ { i } ) ^ { 2 } } { 2 } } y ^ { \prime \prime } ( \xi _ { i } ) ,
$$

for some number $\xi _ { i }$ in $( t _ { i } , t _ { i + 1 } )$ . Since $h = t _ { i + 1 } - t _ { i }$ ,we have

$$
y ( t _ { i + 1 } ) = y ( t _ { i } ) + h y ^ { \prime } ( t _ { i } ) + { \frac { h ^ { 2 } } { 2 } } y ^ { \prime \prime } ( \xi _ { i } ) ,
$$

and, since $y ( t )$ satisfies the differential equation (5.6),

$$
y ( t _ { i + 1 } ) = y ( t _ { i } ) + h f ( t _ { i } , y ( t _ { i } ) ) + { \frac { h ^ { 2 } } { 2 } } y ^ { \prime \prime } ( \xi _ { i } ) .
$$

Euler's method constructs $w _ { i } ~ \approx ~ y ( t _ { i } )$ ， for each $i = 1 , 2 , \dots , N$ ,by deleting the remainder term. Thus,Euler's method is

$$
\begin{array} { r l r } & { \boldsymbol { w } _ { 0 } = \alpha , } & \\ & { \boldsymbol { w } _ { i + 1 } = \boldsymbol { w } _ { i } + h f ( t _ { i } , \boldsymbol { w } _ { i } ) , } & { \mathrm { f o r } \operatorname { e a c h } i = 0 , 1 , \ldots , N - 1 . } \end{array}
$$

Equation (5.8) is called the difference equation associated with Euler's method. As we will see later in this chapter, the theory and solution of difference equations parallel, in many ways, the theory and solution of differential equations. Algorithm 5.1 implements Euler's method.

# Euler's

To approximate the solution of the initial-value problem

$$
y ^ { \prime } = f ( t , y ) , \quad a \leq t \leq b , \quad y ( a ) = \alpha ,
$$

at $( N + 1 )$ equally spaced numbers in the interval $[ a , b ]$ ：

INPUTendpoints $a , b ;$ integer $N$ ; initial condition $\pmb { \alpha }$

OUTPUTapproximation $w$ t0 $y$ at the $( N + 1 )$ values of $t$

Step 1 Set $h = ( b - a ) / N$ t=a; $w = \alpha ;$ OUTPUT $( t , w )$

Step 2 For $i = 1 , 2 , \dots , N$ do Steps 3, 4.

Step 3 Set $\begin{array} { l } { w = w + h f ( t , w ) ; \quad ( C o m p u t e w _ { i } . ) } \\ { t = a + i h . \quad ( C o m p u t e t _ { i } . ) } \end{array}$

Step 4 OUTPUT $( t , w )$

Step 5STOP.

To interpret Euler's method geometrically, note that when ${ \pmb w } _ { i }$ is a close approximation to $y ( t _ { i } )$ , the assumption that the problem is well-posed implies that

$$
f ( t _ { i } , w _ { i } ) \approx y ^ { \prime } ( t _ { i } ) = f ( t _ { i } , y ( t _ { i } ) ) .
$$

The graph of the function highlighting $y ( t _ { i } )$ is shown in Figure 5.2(a). One step in Euler's method appears in Figure 5.2(b), and a series of steps appears in Figure 5.3.

Suppose Euler's method is used to approximate the solution to the initial-value problem

$$
y ^ { \prime } = y - t ^ { 2 } + 1 , \quad 0 \leq t \leq 2 , \quad y ( 0 ) = 0 . 5 ,
$$

with $N = 1 0$ . Then $h = 0 . 2 , t _ { i } = 0 . 2 i$ ， $w _ { 0 } = 0 . 5$ ,and

$$
v _ { i + 1 } = w _ { i } + h ( w _ { i } - t _ { i } ^ { 2 } + 1 ) = w _ { i } + 0 . 2 [ w _ { i } - 0 . 0 4 i ^ { 2 } + 1 ] = 1 . 2 w _ { i } - 0 . 0 0 8 i ^ { 2 } + 0 . 2
$$

for $i = 0 , 1 , \ldots , 9$ . The exact solution is $y ( t ) = ( t + 1 ) ^ { 2 } - 0 . 5 e ^ { t }$ . Table 5.1 shows the comparison between the approximate values at $t _ { i }$ and the actual values. ■

![](images/7579b969aa9db91e084f46e1816760aec380f43e0500e8f0fcd58bce480c7662.jpg)  
Figure 5.2

![](images/c4ba218cff8938beb16eacf6bb5c0a9b8746e29fd0fecaa9972c49e3d963333f.jpg)  
Figure 5.3

# Table 5.1

<table><tr><td>t</td><td>Wi</td><td>yi=y(t）</td><td>lyi -wil</td></tr><tr><td>0.0</td><td>0.5000000</td><td>0.5000000</td><td>0.0000000</td></tr><tr><td>0.2</td><td>0.8000000</td><td>0.8292986</td><td>0.0292986</td></tr><tr><td>0.4</td><td>1.1520000</td><td>1.2140877</td><td>0.0620877</td></tr><tr><td>0.6</td><td>1.5504000</td><td>1.6489406</td><td>0.0985406</td></tr><tr><td>0.8</td><td>1.9884800</td><td>2.1272295</td><td>0.1387495</td></tr><tr><td>1.0</td><td>2.4581760</td><td>2.6408591</td><td>0.1826831</td></tr><tr><td>1.2</td><td>2.9498112</td><td>3.1799415</td><td>0.2301303</td></tr><tr><td>1.4</td><td>3.4517734</td><td>3.7324000</td><td>0.2806266</td></tr><tr><td>1.6</td><td>3.9501281</td><td>4.2834838</td><td>0.3333557</td></tr><tr><td>1.8</td><td>4.4281538</td><td>4.8151763</td><td>0.3870225</td></tr><tr><td>2.0</td><td>4.8657845</td><td>5.3054720</td><td>0.4396874</td></tr></table>

Note that the error grows slightly as the value of $t$ increases. This controlled error growth is a consequence of the stability of Euler's method, which implies that the error is expected to grow in no worse than a linear manner.

Although Euler's method is not accurate enough to warrant its use in practice, it is sufficiently elementary to analyze the error that is produced from its application. The error analysis for the more accurate methods that we consider in subsequent sections follows the same pattern but is more complicated.

To derive an error bound for Euler's method, we need two computational lemmas.

For all $x \ge - 1$ and any positive $m$ , we have $0 \leq ( 1 + x ) ^ { m } \leq e ^ { m x }$

ProofApplying Taylor's Theorem with $f ( x ) = e ^ { x }$ ， $x _ { 0 } = 0$ ,and $n = 1$ gives

$$
e ^ { x } = 1 + x + { \frac { 1 } { 2 } } x ^ { 2 } e ^ { \xi } ,
$$

where $\pmb { \xi }$ is between $x$ and zero. Thus,

$$
0 \leq 1 + x \leq 1 + x + { \frac { 1 } { 2 } } x ^ { 2 } e ^ { \xi } = e ^ { x } ,
$$

and, since $1 + x \ge 0$ ，

$$
0 \leq ( 1 + x ) ^ { m } \leq ( e ^ { x } ) ^ { m } = e ^ { m x } .
$$

# Lemma 5.8

If $\pmb { \mathscr { s } }$ and $t$ are positive real numbers, $\{ a _ { i } \} _ { i = 0 } ^ { k }$ is a sequence satisfying $a _ { 0 } \geq - t / s$ , and

$$
a _ { i + 1 } \leq ( 1 + s ) a _ { i } + t , \quad { \mathrm { f o r ~ e a c h ~ } } i = 0 , 1 , 2 , \ldots , k ,
$$

then

$$
a _ { i + 1 } \leq e ^ { ( i + 1 ) s } \left( a _ { 0 } + \frac { t } { s } \right) - \frac { t } { s } .
$$

Proof For a fixed integer $i$ ,Inequality (5.9) implies that

$$
\begin{array} { r l } & { a _ { i + 1 } \leq ( 1 + s ) a _ { i } + t } \\ & { \qquad \leq ( 1 + s ) [ ( 1 + s ) a _ { i - 1 } + t ] + t } \\ & { \qquad \leq ( 1 + s ) \{ ( 1 + s ) \{ ( 1 + s ) a _ { i - 2 } + t \} + t \} + t } \\ & { \qquad \vdots } \\ & { \qquad \leq ( 1 + s ) ^ { i + 1 } a _ { 0 } + [ 1 + ( 1 + s ) + ( 1 + s ) ^ { 2 } + \cdots + ( 1 + s ) ^ { i } ] t . } \end{array}
$$

But

$$
1 + ( 1 + s ) + ( 1 + s ) ^ { 2 } + \cdots + ( 1 + s ) ^ { i } = \sum _ { j = 0 } ^ { i } ( 1 + s ) ^ { j }
$$

is a geometric series with ratio $( 1 + s )$ that sums to

$$
{ \frac { 1 - ( 1 + s ) ^ { i + 1 } } { 1 - ( 1 + s ) } } = { \frac { 1 } { s } } [ ( 1 + s ) ^ { i + 1 } - 1 ] .
$$

Thus,

$$
a _ { i + 1 } \leq ( 1 + s ) ^ { i + 1 } a _ { 0 } + \frac { ( 1 + s ) ^ { i + 1 } - 1 } { s } t = ( 1 + s ) ^ { i + 1 } \left( a _ { 0 } + \frac { t } { s } \right) - \frac { t } { s } ,
$$

and using Lemma 5.7 with $x = 1 + s$ gives

$$
a _ { i + 1 } \leq e ^ { ( i + 1 ) s } \left( a _ { 0 } + { \frac { t } { s } } \right) - { \frac { t } { s } } .
$$

Theorem 5.9 Suppose $f$ is continuous and satisfies a Lipschitz condition with constant $L$ on

$$
D = \{ ( t , y ) | a \leq t \leq b , - \infty < y < \infty \}
$$

and that a constant $M$ exists with

$$
| y ^ { \prime \prime } ( t ) | \leq M , \quad { \mathrm { f o r ~ a l l ~ } } t \in [ a , b ] .
$$

Let $y ( t )$ denote the unique solution to the initial-value problem

$$
y ^ { \prime } = f ( t , y ) , \quad a \leq t \leq b , \quad y ( a ) = \alpha ,
$$

and $w _ { 0 } , w _ { 1 } , \ldots , w _ { N }$ be the approximations generated by Euler's method for some positive integer $N$ . Then, for each $i = 0 , 1 , 2 , \dots , N ,$

$$
| y ( t _ { i } ) - w _ { i } | \leq \frac { h M } { 2 L } \left[ e ^ { L ( t _ { i } - a ) } - 1 \right] .
$$

Proof When $i = 0$ the result is clearly true, since $y ( t _ { 0 } ) = w _ { 0 } = \alpha$

From Eq. (5.7), we have for $i = 0 , 1 , \dots , N - 1$

$$
y ( t _ { i + 1 } ) = y ( t _ { i } ) + h f ( t _ { i } , y ( t _ { i } ) ) + { \frac { h ^ { 2 } } { 2 } } y ^ { \prime \prime } ( \xi _ { i } ) ,
$$

and from the equations in (5.8),

$$
w _ { i + 1 } = w _ { i } + h f ( t _ { i } , w _ { i } ) .
$$

Consequently,using the notation $y _ { i } = y ( t _ { i } )$ and $y _ { i + 1 } = y ( t _ { i + 1 } )$ , we have

$$
y _ { i + 1 } - w _ { i + 1 } = y _ { i } - w _ { i } + h [ f ( t _ { i } , y _ { i } ) - f ( t _ { i } , w _ { i } ) ] + { \frac { h ^ { 2 } } { 2 } } y ^ { \prime \prime } ( \xi _ { i } )
$$

and

$$
| y _ { i + 1 } - w _ { i + 1 } | \leq | y _ { i } - w _ { i } | + h | f ( t _ { i } , y _ { i } ) - f ( t _ { i } , w _ { i } ) | + \frac { h ^ { 2 } } { 2 } | y ^ { \prime \prime } ( \xi _ { i } ) | .
$$

Since $f$ satisfies a Lipschitz condition in the second variable with constant $L$ and $| y ^ { \prime \prime } ( t ) | \leq M$ , we have

$$
| y _ { i + 1 } - w _ { i + 1 } | \leq ( 1 + h L ) | y _ { i } - w _ { i } | + \frac { h ^ { 2 } M } { 2 } .
$$

Referring to Lemma 5.8 and letting $s = h L , t = h ^ { 2 } M / 2$ ,and $a _ { j } = | y _ { j } - w _ { j } |$ ,for each $j = 0 , 1 , \ldots , N$ , we see that

$$
| y _ { i + 1 } - w _ { i + 1 } | \leq e ^ { ( i + 1 ) h L } \left( | y _ { 0 } - w _ { 0 } | + { \frac { h ^ { 2 } M } { 2 h L } } \right) - { \frac { h ^ { 2 } M } { 2 h L } } .
$$

Since $| y _ { 0 } - w _ { 0 } | = 0$ and $( i + 1 ) h = t _ { i + 1 } - t _ { 0 } = t _ { i + 1 } - a$ ,we have

$$
| y _ { i + 1 } - w _ { i + 1 } | \leq \frac { h M } { 2 L } ( e ^ { ( t _ { i + 1 } - a ) L } - 1 ) ,
$$

for each $i = 0 , 1 , \ldots , N - 1$

The weakness of Theorem 5.9 lies in the requirement that a bound be known for the second derivative of the solution. Although this condition often prohibits us from obtaining

a realistic error bound, it should be noted that if $\partial f / \partial t$ and $\partial f / \partial y$ both exist, the chain rule for partial differentiation implies that

$$
y ^ { \prime \prime } ( t ) = { \frac { d y ^ { \prime } } { d t } } ( t ) = { \frac { d f } { d t } } ( t , y ( t ) ) = { \frac { \partial f } { \partial t } } ( t , y ( t ) ) + { \frac { \partial f } { \partial y } } ( t , y ( t ) ) \cdot f ( t , y ( t ) ) .
$$

So it is at times possible to obtain an error bound for $y ^ { \prime \prime } ( t )$ without explicitly knowing $y ( t )$ ·

# EXAMPLE 2

Returning to the initial-value problem

$$
y ^ { \prime } = y - t ^ { 2 } + 1 , \quad 0 \leq t \leq 2 , \quad y ( 0 ) = 0 . 5 ,
$$

considered in Example 1, we see that since $f ( t , y ) = y - t ^ { 2 } + 1$ , we have $\partial f ( t , y ) / \partial y = 1$ for all $y$ ，s0 $L = 1$ . For this problem, the exact solution is $y ( t ) = ( t + 1 ) ^ { 2 } - { \textstyle \frac { 1 } { 2 } } e ^ { t }$ ，s0 $y ^ { \prime \prime } ( t ) = 2 - 0 . 5 e ^ { t }$ and

$$
| y ^ { \prime \prime } ( t ) | \leq 0 . 5 e ^ { 2 } - 2 , \quad \mathrm { f o r ~ a l l } \ t \in [ 0 , 2 ] .
$$

Using the inequality in the error bound for Euler's method with $h = 0 . 2 , L = 1$ ，and $M = \overline { { 0 . 5 e ^ { 2 } - 2 } }$ gives

$$
| y _ { i } - w _ { i } | \leq 0 . 1 ( 0 . 5 e ^ { 2 } - 2 ) ( e ^ { t _ { i } } - 1 ) .
$$

Table 5.2 lists the actual error found in Example 1, together with this error bound. Note that even though the true bound for the second derivative of the solution was used, the error bound is considerably larger than the actual error. □

Table 5.2   

<table><tr><td>i</td><td>0.2</td><td>0.4</td><td>0.6</td><td>0.8</td><td>1.0</td><td>1.2</td><td>1.4</td><td>1.6</td><td>1.8</td><td>2.0</td></tr><tr><td>Actual Error</td><td>0.02930</td><td>0.06209</td><td>0.09854</td><td>0.13875</td><td>0.18268</td><td>0.23013</td><td>0.28063</td><td>0.33336</td><td>0.38702</td><td>0.43969</td></tr><tr><td>Error Bound</td><td>0.03752</td><td>0.08334</td><td>0.13931</td><td>0.20767</td><td>0.29117</td><td>0.39315</td><td>0.51771</td><td>0.66985</td><td>0.85568</td><td>1.08264</td></tr></table>

The principal importance of the error-bound formula given in Theorem 5.9 is that the bound depends linearly on the step size h. Consequently, diminishing the step size should give correspondingly greater accuracy to the approximations.

Neglected in the result of Theorem 5.9 is the effect that roundoff error plays in the choice of step size. As $h$ becomes smaller, more calculations are necessary and more roundoff error is expected. In actuality then, the difference-equation form

$$
\begin{array} { r l r } & { \boldsymbol { w } _ { 0 } = \alpha , } & \\ & { \boldsymbol { w } _ { i + 1 } = \boldsymbol { w } _ { i } + h f ( t _ { i } , \boldsymbol { w } _ { i } ) , \quad \mathrm { f o r } \mathrm { e a c h } i = 0 , 1 , \ldots , N - 1 , } & \end{array}
$$

is not used to calculate the approximation to the solution $y _ { i }$ at a mesh point $t _ { i }$ . We use instead an equation of the form

$$
\begin{array} { r } { \begin{array} { r } { u _ { 0 } = \alpha + \delta _ { 0 } , \qquad } \\ { u _ { i + 1 } = u _ { i } + h f ( t _ { i } , u _ { i } ) + \delta _ { i + 1 } , \quad \mathrm { f o r } \mathrm { e a c h } i = 0 , 1 , \dots , N - 1 , } \end{array} } \end{array}
$$

where $\delta _ { i }$ denotes the roundoff error associated with $u _ { i }$ . Using methods similar to those in the proof of Theorem 5.9, we can produce an error bound for the finite-digit approximations to $y _ { i }$ given by Euler's method.

Let $y ( t )$ denote the unique solution to the initial-value problem

$$
y ^ { \prime } = f ( t , y ) , \quad a \leq t \leq b , \quad y ( a ) = \alpha
$$

and $u _ { 0 } , u _ { 1 } , \dotsc , u _ { N }$ be the approximations obtained using (5.11). If $| \delta _ { i } | < \delta$ for each $i =$ $0 , 1 , \ldots , N$ and the hypotheses of Theorem 5.9 hold for (5.12),then

$$
| y ( t _ { i } ) - u _ { i } | \leq \frac { 1 } { L } \left( \frac { h M } { 2 } + \frac { \delta } { h } \right) [ e ^ { L ( t _ { i } - a ) } - 1 ] + | \delta _ { 0 } | e ^ { L ( t _ { i } - a ) } ,
$$

for each $i = 0 , 1 , \ldots , N$

The error bound (5.13) is no longer linear in $h$ . In fact, since

$$
\operatorname* { l i m } _ { h \to 0 } \left( { \frac { h M } { 2 } } + { \frac { \delta } { h } } \right) = \infty ,
$$

the error would be expected to become large for sufficiently small values of $\pmb { h }$ . Calculus can be used to determine a lower bound for the step size $h$ . Letting $E ( h ) = ( h M / 2 ) + ( \delta / h )$ implies that $E ^ { \prime } ( h ) = ( M / 2 ) - ( \delta / h ^ { 2 } )$

The minimal value of $E ( h )$ occurs when

$$
h = \sqrt { \frac { 2 \delta } { M } } .
$$

Decreasing $h$ beyond this value tends to increase the total error in the approximation. Normally, however, the value of $\delta$ is sufficiently small that this lower bound for $h$ does not affect the operation of Euler's method.

# Exercise SEt 5.2

1.Use Euler's method to approximate the solutions for each of the following initial-value problems.

a. $y ^ { \prime } = t e ^ { 3 t } - 2 y , \quad 0 \leq t \leq 1 , \quad y ( 0 ) = 0 , { \mathrm { ~ w i t h ~ } } h = 0 . 5$ b. $y ^ { \prime } = 1 + ( t - y ) ^ { 2 } , \quad \dot { 2 } \leq t \leq 3 , \quad y ( 2 ) = 1 , \mathrm { w i t h } h =$ $h = 0 . 5$ c. $y ^ { \prime } = 1 + y / t , \quad 1 \leq t \leq 2 , \quad y ( 1 ) = 2 , \mathrm { w i t h } h = 0 . 2 5$ d. $y ^ { \prime } = \cos 2 t + \sin 3 t$ ， $0 \leq t \leq 1 , \quad y ( 0 ) = 1 , \mathrm { w i t h } h = 0 . 2 5$

2.The actual solutions to the initial-value problems in Exercise l are given here. Compare the actual error at each step to the error bound.

$$
\begin{array} { c c l } { { { \bf a . } } } & { { { \displaystyle y ( t ) = { \frac { 1 } { 5 } } t e ^ { 3 t } - { \frac { 1 } { 2 5 } } e ^ { 3 t } + { \frac { 1 } { 2 5 } } e ^ { - 2 t } } } } & { { { \bf b . } } } & { { { \displaystyle y ( t ) = t + { \frac { 1 } { 1 - t } } } } } \\ { { { \bf c . } } } & { { { \displaystyle y ( t ) = t \ln t + 2 t } } } & { { { \bf d . } } } & { { { \displaystyle y ( t ) = { \frac { 1 } { 2 } } \sin 2 t - { \frac { 1 } { 3 } } \cos 3 t + { \frac { 4 } { 3 } } } } } \end{array}
$$

3.Use Euler's method to approximate the solutions for each of the folowing initial-value problems.

$$
\begin{array} { r l } & { y ^ { \prime } = y / t - ( y / t ) ^ { 2 } , \quad 1 \leq t \leq 2 , \quad y ( 1 ) = 1 , \mathrm { ~ w i t h ~ } h = 0 . 1 } \\ & { y ^ { \prime } = 1 + y / t + ( y / t ) ^ { 2 } , \quad 1 \leq t \leq 3 , \quad y ( 1 ) = 0 , \mathrm { ~ w i t h ~ } h = 0 . 2 } \\ & { y ^ { \prime } = - ( y + 1 ) ( y + 3 ) , \quad 0 \leq t \leq 2 , \quad y ( 0 ) = - 2 , \mathrm { ~ w i t h ~ } h = 0 . 2 } \\ & { y ^ { \prime } = - 5 y + 5 t ^ { 2 } + 2 t , \quad 0 \leq t \leq 1 , \quad y ( 0 ) = \frac { 1 } { 3 } , \mathrm { ~ w i t h ~ } h = 0 . 1 } \end{array}
$$

4. The actual solutions to the initial-value problems in Exercise 3 are given here. Compute the actual error in the approximations of Exercise 3.

$$
\begin{array} { l } { { y ( t ) = \displaystyle \frac { t } { 1 + \ln t } } } \\ { { \displaystyle y ( t ) = - 3 + \frac { 2 } { 1 + e ^ { - 2 t } } } } \end{array} \qquad \begin{array} { l } { { \mathbf b . \quad y ( t ) = t \tan ( \ln t ) } } \\ { { \displaystyle \mathbf d . \quad y ( t ) = t ^ { 2 } + \frac { 1 } { 3 } e ^ { - 5 t } } } \end{array}
$$

5. Given the initial-value problem

$$
y ^ { \prime } = { \frac { 2 } { t } } y + t ^ { 2 } e ^ { t } , \quad 1 \leq t \leq 2 , \quad y ( 1 ) = 0 ,
$$

with exact solution $y ( t ) = t ^ { 2 } ( e ^ { t } - e )$ ：

a. Use Euler's method with $h = 0 . 1$ to approximate the solution,and compare it with the actual values of $y$   
b. Use the answers generated in part (a) and linear interpolation to approximate the following values of $y$ , and compare them to the actual values. i.y(1.04) ii.y(1.55) iii.y(1.97)

c.Compute.the value of $h$ necessary for $| y ( t _ { i } ) - w _ { i } | \leq 0 . 1$ ,using Eq. (5.10).

6. Given the initial-value problem

$$
y ^ { \prime } = { \frac { 1 } { t ^ { 2 } } } - { \frac { y } { t } } - y ^ { 2 } , \quad 1 \leq t \leq 2 , \quad y ( 1 ) = - 1 ,
$$

with exact solution $y ( t ) = - 1 / t$ ：

a. Use Euler's method with $h = 0 . 0 5$ to approximate the solution, and compare it with the actual values of $y$   
b. Use the answers generated in part (a) and linear interpolation to approximate the following values of $y$ , and compare them to the actual values. i.y(1.052) ii.y(1.555) ili.y(1.978)

c.Compute the value of $h$ necessary for $| y ( t _ { i } ) - w _ { i } | \leq 0 . 0 5$ using eq. (5.10).

7. Given the initial-value problem

$$
y ^ { \prime } = - y + t + 1 , \quad 0 \leq t \leq 5 , \quad y ( 0 ) = 1 ,
$$

with exact solution $y ( t ) = e ^ { - t } + t$ ：

a. Approximate $y ( 5 )$ using Euler's method with $h = 0 . 2 , h = 0 . 1$ , and $h = 0 . 0 5$ b. Determine the optimal value of $h$ to use in computing y(5),assuming $\delta = 1 0 ^ { - 6 }$ and that Eq. (5.14) is valid.

8. Use the results of Exercise 3 and linear interpolation to approximate the following values of $y ( t )$ .Compare the approximations obtained to the actual values obtained using the functions given in Exercise 4.

a.y(1.25)andy(1.93) $\begin{array} { r l } { \mathbf { b . } } & { { } ~ y ( 2 . 1 ) \mathrm { ~ a n d ~ } y ( 2 . 7 5 ) } \\ { \mathbf { d . } } & { { } ~ y ( 0 . 5 4 ) \mathrm { ~ a n d ~ } y ( 0 . 9 4 ) } \end{array}$ c. $y ( 1 . 4 )$ and y(1.93)

9.Let $E ( h ) = \frac { h M } { 2 } + \frac { \delta } { h }$

a. For the initial-value problem

$$
y ^ { \prime } = - y + 1 , \quad 0 \leq t \leq 1 , \quad y ( 0 ) = 0 ,
$$

compute the vaue of $h$ to minimize $E ( h )$ . Assume $\delta = 5 \times 1 0 ^ { - ( n + 1 ) }$ if you will be using $\pmb { n }$ -digit arithmetic in part (c).

b.For the optimal $h$ computed in part (a),use Eq.(5.13)to compute the minimal error obtainable.

Compare the actual error obtained using $h = 0 . 1$ and $h = 0 . 0 1$ to the minimal error in part (b). Can you explain the results?

10.Consider the initial-value problem

$$
y ^ { \prime } = - 1 0 y , \quad 0 \leq t \leq 2 , \quad y ( 0 ) = 1 ,
$$

which has solution $y ( t ) = e ^ { - 1 0 t }$ . What happens when Euler's methodis appliedto this probler with $h = 0 . 1 ?$ Does this behavior violate Theorem 5.9?

11. In a book entitled Looking at History Through Mathematics,Rashevsky [Ra, pp. 103-110] considers a model for a problem involving the production of nonconformists in society. Sup-pose that a society has a population of $x ( t )$ individuals at time $\pmb { t }$ ,in years,and that all nonconformists who mate with other nonconformists have ofspring who are also nonconformists, while a fixed proportion $r$ of all other offspring are also nonconformist. If the birth and death rates for all individuals are assumed to be the constants $b$ and $d$ ,respectively，and if conformists and nonconformists mate at random, the problem can be expressed by the differential equations

$$
\frac { d x ( t ) } { d t } = ( b - d ) x ( t ) \quad \mathrm { a n d } \quad \frac { d x _ { n } ( t ) } { d t } = ( b - d ) x _ { n } ( t ) + r b ( x ( t ) - x _ { n } ( t ) ) ,
$$

where $x _ { n } ( t )$ denotes the number of nonconformists in the population at time $t$

a. Suppose the variable $p ( t ) = x _ { n } ( t ) / x ( t )$ is introduced to represent the proportion of nonconformists in the society at time $t$ . Show that these equations can be combined and simplified to the single differential equation

$$
\frac { d p ( t ) } { d t } = r b ( 1 - p ( t ) ) .
$$

b. Assuming that $p ( 0 ) = 0 . 0 1 , b = 0 . 0 2 , d = 0 . 0 1 5$ ,and $r = 0 . 1$ , approximate the solution $p ( t )$ from $\ell = 0$ t0 $t = 5 0$ when the step size is $h = 1$ year.   
c. Solve the differential equation for $p ( t )$ exactly, and compare your result in part (b) when $t = 5 0$ with the exact value at that time.

12.In a circuit with impressed voltage $\pmb { \mathcal { E } }$ having resistance $R$ , inductance $L$ , and capacitance $C$ in parallel, the current $i$ satisfies the differential equation

$$
\frac { d i } { d t } = C \frac { d ^ { 2 } \mathcal { E } } { d t ^ { 2 } } + \frac { 1 } { R } \frac { d \mathcal { E } } { d t } + \frac { 1 } { L } \mathcal { E } .
$$

Suppose $C = 0 . 3$ farads, $R = 1 . 4$ ohms, $L = 1 . 7$ henries,and the voltage is given by

$$
\mathcal { E } ( t ) = e ^ { - 0 . 0 6 \pi t } \sin ( 2 t - \pi ) .
$$

If $i ( 0 ) = 0$ , find the current $i$ for the values $t = 0 . 1 j$ ，where $j = 0 , 1 , \ldots , 1 0 0 .$

# 5.3 Higher-Order Taylor Methods

Since the object of numerical techniques is to determine accurate approximations with minimal effort, we need a means for comparing the efficiency of various approximation methods. The first device we consider is called the local truncation error of the method. The local truncation error at a specified step measures the amount by which the exact solution to the differential equation fails to satisfy the difference equation being used for the approximation.

# Definition 5.11 The difference method

$$
\begin{array} { r }  \begin{array} { r } { \begin{array} { c } { w _ { 0 } = \alpha } \\ { \qquad } \\ { w _ { i + 1 } = w _ { i } + h \phi ( t _ { i } , w _ { i } ) , \quad \mathrm { f o r } \mathrm { e a c h } i = 0 , 1 , \ldots , N - 1 , } \end{array} } \end{array} \end{array}
$$

has local truncation error

$$
\tau _ { i + 1 } ( h ) = \frac { y _ { i + 1 } - ( y _ { i } + h \phi ( t _ { i } , y _ { i } ) ) } { h } = \frac { y _ { i + 1 } - y _ { i } } { h } - \phi ( t _ { i } , y _ { i } ) ,
$$

for each $i = 0 , 1 , \ldots , N - 1$

For Euler's method, the local truncation error at the ith step for the problem

$$
y ^ { \prime } = f ( t , y ) , \quad a \leq t \leq b , \quad y ( a ) = \alpha ,
$$

is

$$
\tau _ { i + 1 } ( h ) = \frac { y _ { i + 1 } - y _ { i } } { h } - f ( t _ { i } , y _ { i } ) , \quad \mathrm { f o r } \mathrm { e a c h } i = 0 , 1 , \dots , N - 1 ,
$$

where, as usual, $y _ { i } = y ( t _ { i } )$ denotes the exact value of the solution at $t _ { i }$ . This error is a local error because it measures the accuracy of the method at a specific step, assuming that the method was exact at the previous step.As such, it depends on the differential equation, the step size, and the particular step in the approximation.

By considering Eq. (5.7) in the previous section, we see that Euler's method has

$$
\tau _ { i + 1 } ( h ) = { \frac { h } { 2 } } y ^ { \prime \prime } ( \xi _ { i } ) , \quad { \mathrm { f o r ~ s o m e ~ } } \xi _ { i } { \mathrm { ~ i n ~ } } ( t _ { i } , t _ { i + 1 } ) .
$$

When $y ^ { \prime \prime } ( t )$ is known to be bounded by a constant $M$ on $[ a , b ]$ , this implies

$$
| \tau _ { i + 1 } ( h ) | \leq \frac { h } { 2 } M ,
$$

so the local truncation error in Euler's method is $O ( h )$

One way to select diference-equation methods for solving ordinary diferential equations is in such a manner that their local truncation errors are $O ( h ^ { p } )$ for as large a value of $p$ as possible, while keeping the number and complexity of calculations of the methods within a reasonable bound.

Since Euler's method was derived by using Taylor's Theorem with $n = 1$ to approximate the solution of the differential equation,our first attempt to find methods for improving the convergence properties of difference methods is to extend this technique of derivation to larger values of $\pmb { n }$

Suppose the solution $y ( t )$ to the initial-value problem

$$
y ^ { \prime } = f ( t , y ) , \quad a \leq t \leq b , \quad y ( a ) = \alpha ,
$$

has $( n + 1 )$ continuous derivatives. If we expand the solution, $y ( t )$ , in terms of its nth Taylor polynomial about $t _ { i }$ and evaluate at $t _ { i + 1 }$ , we obtain

$$
y ( t _ { i + 1 } ) = y ( t _ { i } ) + h y ^ { \prime } ( t _ { i } ) + { \frac { h ^ { 2 } } { 2 } } y ^ { \prime \prime } ( t _ { i } ) + \cdot \cdot \cdot + { \frac { h ^ { n } } { n ! } } y ^ { ( n ) } ( t _ { i } ) + { \frac { h ^ { n + 1 } } { ( n + 1 ) ! } } y ^ { ( n + 1 ) } ( \xi _ { i } ) ,
$$

for some $\xi _ { i }$ in $( t _ { i } , t _ { i + 1 } )$

Successive differentiation of the solution, $y ( t )$ , gives

$$
\begin{array} { r } { y ^ { \prime } ( t ) = f ( t , y ( t ) ) , } \\ { y ^ { \prime \prime } ( t ) = f ^ { \prime } ( t , y ( t ) ) , } \end{array}
$$

and, in general,

$$
y ^ { ( k ) } ( t ) = f ^ { ( k - 1 ) } ( t , y ( t ) ) .
$$

Substituting these results into Eq. (5.15) gives

$$
\begin{array} { l } { { \displaystyle y ( t _ { i + 1 } ) = y ( t _ { i } ) + h f ( t _ { i } , y ( t _ { i } ) ) + \frac { h ^ { 2 } } { 2 } f ^ { \prime } ( t _ { i } , y ( t _ { i } ) ) + \cdots } } \\ { { \displaystyle ~ + \frac { h ^ { n } } { n ! } f ^ { ( n - 1 ) } ( t _ { i } , y ( t _ { i } ) ) + \frac { h ^ { n + 1 } } { ( n + 1 ) ! } f ^ { ( n ) } ( \xi _ { i } , y ( \xi _ { i } ) ) . } } \end{array}
$$

The diference-equation method corresponding to Eq. (5.16) is obtained by deleting the remainder term involving $\xi _ { i }$ . This method is called the

# Taylor method of order n:

$$
\begin{array} { r l } & { \boldsymbol { w } _ { 0 } = \boldsymbol { \alpha } , } \\ & { \boldsymbol { w } _ { i + 1 } = \boldsymbol { w } _ { i } + h T ^ { ( n ) } ( t _ { i } , \boldsymbol { w } _ { i } ) , \quad \mathrm { f o r } \mathrm { e a c h } i = 0 , 1 , \ldots , N - 1 , } \end{array}
$$

where

$$
T ^ { ( n ) } ( t _ { i } , w _ { i } ) = f ( t _ { i } , w _ { i } ) + { \frac { h } { 2 } } f ^ { \prime } ( t _ { i } , w _ { i } ) + \cdots + { \frac { h ^ { n - 1 } } { n ! } } f ^ { ( n - 1 ) } ( t _ { i } , w _ { i } ) .
$$

Note that Euler's method is Taylor's method of order one.

Suppose that we want to apply Taylor's method of orders two and four to the initial-value problem

$$
y ^ { \prime } = y - t ^ { 2 } + 1 , \quad 0 \leq t \leq 2 , \quad y ( 0 ) = 0 . 5 ,
$$

which was studied in the previous sections. We must find the first three derivatives of $f ( t , y ( t ) ) = y ( t ) - t ^ { 2 } + 1$ with respect to the variable $t$ ：

$$
f ^ { \prime } ( t , y ( t ) ) = { \frac { d } { d t } } ( y - t ^ { 2 } + 1 ) = y ^ { \prime } - 2 t = y - t ^ { 2 } + 1 - 2 t ,
$$

$$
\begin{array} { l } { { f ^ { \prime \prime } ( t , y ( t ) ) = \displaystyle \frac { d } { d t } ( y - t ^ { 2 } + 1 - 2 t ) = y ^ { \prime } - 2 t - 2 } } \\ { { \qquad = y - t ^ { 2 } + 1 - 2 t - 2 = y - t ^ { 2 } - 2 t - 1 , } } \end{array}
$$

and

$$
f ^ { \prime \prime \prime } ( t , y ( t ) ) = \frac { d } { d t } ( y - t ^ { 2 } - 2 t - 1 ) = y ^ { \prime } - 2 t - 2 = y - t ^ { 2 } - 2 t - 1 .
$$

So

$$
\begin{array} { l } { { \displaystyle T ^ { ( 2 ) } ( t _ { i } , w _ { i } ) = f ( t _ { i } , w _ { i } ) + \frac { h } { 2 } f ^ { \prime } ( t _ { i } , w _ { i } ) = w _ { i } - t _ { i } ^ { 2 } + 1 + \frac { h } { 2 } ( w _ { i } - t _ { i } ^ { 2 } - 2 t _ { i } + 1 ) } } \\ { { \displaystyle \qquad = \left( 1 + \frac { h } { 2 } \right) ( w _ { i } - t _ { i } ^ { 2 } + 1 ) - h t _ { i } } } \end{array}
$$

and

$$
\begin{array} { l } { { { \cal T } ^ { ( 4 ) } ( t _ { i } , w _ { i } ) = f ( t _ { i } , w _ { i } ) + { \displaystyle \frac { h } { 2 } } f ^ { \prime } ( t _ { i } , w _ { i } ) + { \displaystyle \frac { h ^ { 2 } } { 6 } } f ^ { \prime \prime } ( t _ { i } , w _ { i } ) + { \displaystyle \frac { h ^ { 3 } } { 2 4 } } f ^ { \prime \prime } ( t _ { i } , w _ { i } ) } } \\ { { \mathrm { } } } \\ { { = w _ { i } - \displaystyle { \varepsilon _ { i } ^ { 2 } + 1 + \frac { h } { 2 } } \left( w _ { i } - \displaystyle { t _ { i } ^ { 2 } - 2 t _ { i } + 1 } \right) + { \displaystyle \frac { h ^ { 2 } } { 6 } } ( w _ { i } - \displaystyle { t _ { i } ^ { 2 } - 2 t _ { i } - 1 } ) } } \\ { { \mathrm { } } } \\ { { \mathrm { } } } \\ { { \displaystyle \mathrm { } + { \displaystyle \frac { h ^ { 3 } } { 2 4 } } ( w _ { i } - \displaystyle { t _ { i } ^ { 2 } - 2 t _ { i } - 1 } ) } } \\ { { \mathrm { } } } \\ { { \displaystyle = \left( 1 + { \displaystyle \frac { h } { 2 } + \frac { h ^ { 2 } } { 6 } + \frac { h ^ { 3 } } { 2 4 } } \right) ( w _ { i } - \displaystyle { t _ { i } ^ { 2 } } ) - \left( 1 + { \displaystyle \frac { h } { 3 } + \frac { h ^ { 2 } } { 1 2 } } \right) ( h _ { i } ) } } \\ { { \mathrm { } } } \\ { { \displaystyle \mathrm { } + 1 + { \displaystyle \frac { h } { 2 } - \frac { h ^ { 2 } } { 6 } - \frac { h ^ { 3 } } { 2 4 } } . } } \end{array}
$$

The Taylor methods of orders two and four are, consequently

$$
\begin{array} { r c l } { { w _ { 0 } = 0 . 5 , } } \\ { { \ldots } } \\ { { w _ { i + 1 } = w _ { i } + h \left[ \left( 1 + \displaystyle \frac { h } { 2 } \right) ( w _ { i } - t _ { i } ^ { 2 } + 1 ) - h t _ { i } \right] } } \end{array}
$$

and

$$
\begin{array} { c l } { { w _ { 0 } = 0 . 5 , } } \\ { { w _ { i + 1 } = w _ { i } + h \bigg [ \left( 1 + \displaystyle \frac { h } { 2 } + \displaystyle \frac { h ^ { 2 } } { 6 } + \displaystyle \frac { h ^ { 3 } } { 2 4 } \right) ( w _ { i } - t _ { i } ^ { 2 } ) - \left( 1 + \displaystyle \frac { h } { 3 } + \displaystyle \frac { h ^ { 2 } } { 1 2 } \right) h t _ { i } } } \\ { { + 1 + \displaystyle \frac { h } { 2 } - \displaystyle \frac { h ^ { 2 } } { 6 } - \displaystyle \frac { h ^ { 3 } } { 2 4 } \bigg ] , } } \end{array}
$$

for $i = 0 , 1 , \ldots , N - 1$

If $h = 0 . 2$ ,then $N = 1 0$ and $t _ { i } = 0 . 2 i$ for each i = 1,2,...,10. Thus,the secondorder method becomes

$$
\begin{array} { r l r } {  { w _ { 0 } = 0 . 5 , } } \\ & { } & \\ & { } & { w _ { i + 1 } = w _ { i } + 0 . 2 [ ( 1 + \frac { 0 . 2 } { 2 } ) ( w _ { i } - 0 . 0 4 i ^ { 2 } + 1 ) - 0 . 0 4 i ] } \\ & { } & \\ & { } & { = 1 . 2 2 w _ { i } - 0 . 0 0 8 8 i ^ { 2 } - 0 . 0 0 8 i + 0 . 2 2 , } \end{array}
$$

and the fourth-order method becomes

$$
\begin{array} { r l r } {  { w _ { i + 1 } = w _ { i } + 0 . 2 \bigg [ ( 1 + \frac { 0 . 2 } { 2 } + \frac { 0 . 0 4 } { 6 } + \frac { 0 . 0 0 8 } { 2 4 } ) ( w _ { i } - 0 . 0 4 i ^ { 2 } ) } } \\ & { } & \\ & { } & { \qquad - ( 1 + \frac { 0 . 2 } { 3 } + \frac { 0 . 0 4 } { 1 2 } ) ( . 0 4 i ) + 1 + \frac { 0 . 2 } { 2 } - \frac { 0 . 0 4 } { 6 } - \frac { 0 . 0 0 8 } { 2 4 } \bigg ] } \\ & { } & \\ & { } & { = 1 . 2 2 1 4 w _ { i } - 0 . 0 0 8 8 5 6 i ^ { 2 } - 0 . 0 0 8 5 6 i + 0 . 2 1 8 6 , } \end{array}
$$

for each $i = 0 , 1 , \ldots , 9$

Table 5.3 lists the actual values of the solution $y ( t ) = ( t + 1 ) ^ { 2 } - 0 . 5 e ^ { t }$ , the results from the Taylor methods of orders two and four,and the actual errors involved with these methods.

# Table 5.3

<table><tr><td></td><td>Exact</td><td>Taylor Order 2</td><td>Error ly(ti）-wil</td><td>Taylor Order 4</td><td>Error ly(ti）-wil</td></tr><tr><td>ti</td><td>y(ti)</td><td>Wi</td><td></td><td>wi 0.5000000</td><td></td></tr><tr><td>0.0</td><td>0.5000000</td><td>0.5000000 0.8300000</td><td>0 0.0007014</td><td>0.8293000</td><td>0 0.0000014</td></tr><tr><td>0.2 0.4</td><td>0.8292986 1.2140877</td><td>1.2158000</td><td>0.0017123</td><td>1.2140910</td><td>0.0000034</td></tr><tr><td>0.6</td><td>1.6489406</td><td>1.6520760</td><td>0.0031354</td><td>1.6489468</td><td>0.0000062</td></tr><tr><td>0.8</td><td>2.1272295</td><td>2.1323327</td><td>0.0051032</td><td>2.1272396</td><td>0.0000101</td></tr><tr><td>1.0</td><td>2.6408591</td><td>2.6486459</td><td>0.0077868</td><td>2.6408744</td><td>0.0000153</td></tr><tr><td>1.2</td><td>3.1799415</td><td>3.1913480</td><td>0.0114065</td><td>3.1799640</td><td>0.0000225</td></tr><tr><td>1.4</td><td>3.7324000</td><td>3.7486446</td><td>0.0162446</td><td>3.7324321</td><td>0.0000321</td></tr><tr><td>1.6</td><td>4.2834838</td><td>4.3061464</td><td>0.0226626</td><td>4.2835285</td><td>0.0000447</td></tr><tr><td>1.8</td><td>4.8151763</td><td>4.8462986</td><td>0.0311223</td><td>4.8152377</td><td>0.0000615</td></tr><tr><td>2.0</td><td>5.3054720</td><td>5.3476843</td><td>0.0422123</td><td>5.3055554</td><td>0.0000834</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Suppose we need to determine an approximation to an intermediate point in the table, for example, at $t = 1 . 2 5$ . If we use linear interpolation on the Taylor method of order four approximations at $t = 1 . 2$ and $t = 1 . 4$ ， we have

$$
y ( 1 . 2 5 ) \approx \left( { \frac { 1 . 2 5 - 1 . 4 } { 1 . 2 - 1 . 4 } } \right) 3 . 1 7 9 9 6 4 0 + \left( { \frac { 1 . 2 5 - 1 . 2 } { 1 . 4 - 1 . 2 } } \right) 3 . 7 3 2 4 3 2 1 = 3 . 3 1 8 0 8 1 0 .
$$

Since the true value is $y ( 1 . 2 5 ) = 3 . 3 1 7 3 2 8 5$ ,this approximation has an error of 0.0007525, which is nearly 30 times the average of the approximation errors at 1.2 and 1.4.

To improve the approximation to y(1.25),we use cubic Hermite interpolation. This requires approximations to $y ^ { \prime } ( 1 . 2 )$ and $y ^ { \prime } ( 1 . 4 )$ as well as approximations to y(1.2） and $y ( 1 . 4 )$ . But the derivative approximations are available from the differential equation since $y ^ { \prime } ( t ) = f ( t , y ( t ) )$ . In our example $y ^ { \prime } ( t ) = y ( t ) - t ^ { 2 } + 1$ ,s0

$$
y ^ { \prime } ( 1 . 2 ) = y ( 1 . 2 ) - ( 1 . 2 ) ^ { 2 } + 1 \approx 3 . 1 7 9 9 6 4 0 - 1 . 4 4 + 1 = 2 . 7 3 9 9 6 4 0
$$

and

$$
y ^ { \prime } ( 1 . 4 ) = y ( 1 . 4 ) - ( 1 . 4 ) ^ { 2 } + 1 \approx 3 . 7 3 2 4 3 2 7 - 1 . 9 6 + 1 = 2 . 7 7 2 4 3 2 1 .
$$

The divided-difference procedure in Section 3.3 gives the information in Table 5.4. The underlined entries come from the data,and the other entries use the divided-difference formulas.

# Table 5.4

<table><tr><td>1.2</td><td>3.1799640</td><td></td><td></td><td rowspan="3"></td></tr><tr><td></td><td></td><td>2.7399640</td><td>0.1118825 -0.3071225</td></tr><tr><td rowspan="2">1.2</td><td rowspan="2">3.1799640</td><td>2.7623405</td><td></td></tr><tr><td></td><td></td></tr><tr><td>1.4</td><td>3.7324321</td><td>2.7724321</td><td>0.0504580</td><td></td></tr><tr><td>1.4</td><td>3.7324321</td><td></td><td></td><td></td></tr></table>

The cubic Hermite polynomial is

$$
\begin{array} { r l } & { y ( t ) \approx 3 . 1 7 9 9 6 4 0 + ( t - 1 . 2 ) 2 . 7 3 9 9 6 4 0 + ( t - 1 . 2 ) ^ { 2 } 0 . 1 1 1 8 8 2 5 } \\ & { \qquad + ( t - 1 . 2 ) ^ { 2 } ( t - 1 . 4 ) ( - 0 . 3 0 7 1 2 2 5 ) , } \end{array}
$$

so

$$
y ( 1 . 2 5 ) \approx 3 . 1 7 9 9 6 4 0 + 0 . 1 3 6 9 9 8 2 + 0 . 0 0 0 2 7 9 7 + 0 . 0 0 0 1 1 5 2 = 3 . 3 1 7 3 5 7 1 ,
$$

a result that is accurate to within O.0o00286. This is about the average of the erors at 1.2 and at 1.4, or about $4 \%$ of the error obtained using linear interpolation.

# Theorem 5.12

If Taylor's method of order $\pmb { n }$ is used to approximate the solution to

$$
y ^ { \prime } ( t ) = f ( t , y ( t ) ) , \quad a \leq t \leq b , \quad y ( a ) = \alpha ,
$$

with step size $h$ and if $y \in C ^ { n + 1 } [ a , b ]$ , then the local truncation error is $O ( h ^ { n } )$

Proof Note that Eq.(5.16) can be rewritten

$$
- y _ { i } - h f ( t _ { i } , y _ { i } ) - { \frac { h ^ { 2 } } { 2 } } f ^ { \prime } ( t _ { i } , y _ { i } ) - \cdot \cdot \cdot - { \frac { h ^ { n } } { n ! } } f ^ { ( n - 1 ) } ( t _ { i } , y _ { i } ) = { \frac { h ^ { n + 1 } } { ( n + 1 ) ! } } f ^ { ( n ) } ( \xi _ { i } , y ( \xi _ { i } ) ) ,
$$

for some $\xi _ { i }$ in $( t _ { i } , t _ { i + 1 } )$ . So the local truncation error is

$$
\tau _ { i + 1 } ( h ) = \frac { y _ { i + 1 } - y _ { i } } { h } - T ^ { ( n ) } ( t _ { i } , y _ { i } ) = \frac { h ^ { n } } { ( n + 1 ) ! } f ^ { ( n ) } ( \xi _ { i } , y ( \xi _ { i } ) ) ,
$$

for each $i = 0 , 1 , \dots , N - 1$ Since $y \in C ^ { n + 1 } [ a , b ]$ , we have $y ^ { ( n + 1 ) } ( t ) = f ^ { ( n ) } ( t , y ( t ) )$ bounded on $[ a , b ]$ and $\tau _ { i } = O ( h ^ { n } )$ , for each $i = 1 , 2 , \dots , N$ ■ ■

1. Use Taylor's method of order two to approximate the solutions for each of the following initialvalue problems.

a. $y ^ { \prime } = t e ^ { 3 t } - 2 y , \quad 0 \leq t \leq 1 , \quad y ( 0 ) = 0 , { \mathrm { ~ w i t h ~ } } h = 0 . 5$ b. $y ^ { \prime } = 1 + ( t - y ) ^ { 2 } , \quad 2 \leq t \leq 3 , \quad y ( 2 ) = 1 ,$ $2 \leq t \leq 3 , \quad y ( 2 ) = 1 , \mathrm { w i t h } h = 0 . 5$ c. $y ^ { \prime } = 1 + y / t , \quad 1 \leq t \leq 2 , \quad y ( 1 ) = 2 , \mathrm { ~ w i ~ }$ th $h = 0 . 2 5$ d. $y ^ { \prime } = \cos 2 t + \sin 3 t , \quad 0 \leq t \leq 1 , \quad y ( 0 ) = 1 , \mathrm { w i t h } h = 0 . 2 5$

2.Repeat Exercise 1 using Taylor's method of order four.

3.Use Taylor's method of order two and four to approximate the solution for each of the following initial-value problems.

a. $y ^ { \prime } = y / t - ( y / t ) ^ { 2 } , \quad 1 \leq t \leq 1 . 2 , \quad y ( 1 ) = 1 , \mathrm { w i t h } h = 0 . 1$   
b. $y ^ { \prime } = \sin t + e ^ { - t } , \quad 0 \leq t \leq 1 , \quad y ( 0 ) = 0 , \ \mathrm { w i t h } \ h = 0 . 5$   
c. $y ^ { \prime } = 1 / t ( y ^ { 2 } + y ) , \quad 1 \leq t \leq 3 , \quad y ( 1 ) = - 2 , \mathrm { w i t h } h = 0 . 5$   
d. $y ^ { \prime } = - t y + 4 t / y , \quad 0 \leq t \leq 1 , \quad y ( 0 ) = 1 , \mathrm { w i t h } h = 0 . 2 5$

4.Use the Taylor method of order two with $h = 0 . 1$ to approximate the solution to

$$
y ^ { \prime } = 1 + t \sin ( t y ) , \quad 0 \leq t \leq 2 , \quad y ( 0 ) = 0 .
$$

5. Given the initial-value problem

$$
y ^ { \prime } = \frac { 2 } { t } y + t ^ { 2 } e ^ { t } , \quad 1 \leq t \leq 2 , \quad y ( 1 ) = 0 ,
$$

with exact solution $y ( t ) = t ^ { 2 } ( e ^ { t } - e )$ ：

a. Use Taylor's method of order two with $h = 0 . 1$ to approximate the solution, and compare it with the actual values of $y$   
b. Use the answers generated in part (a) and linear interpolation to approximate $y$ at the following values,and compare them to the actual values of $\pmb { y }$

iy(1.04) i. ' y(1.55) i.y(1.97)