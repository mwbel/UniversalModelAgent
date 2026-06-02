# ExERcisE Set 11.4

1.Use the Nonlinear Finite-Difference Algorithm with $h = 0 . 5$ to approximate the solution to the boundary-value problem

$$
y ^ { \prime \prime } = - ( y ^ { \prime } ) ^ { 2 } - y + \ln x , \quad 1 \leq x \leq 2 , \quad y ( 1 ) = 0 , \quad y ( 2 ) = \ln 2 ,
$$

Compare your results to the actual solution $y = \ln x$ ·

2. Use the Nonlinear Finite-Difference Algorithm with $h = 0 . 2 5$ to approximate the solution to the boundary-value problem

$$
y ^ { \prime \prime } = 2 y ^ { 3 } , \quad - 1 \leq x \leq 0 , \quad y ( - 1 ) = { \frac { 1 } { 2 } } , \quad y ( 0 ) = { \frac { 1 } { 3 } }
$$

Compare your results to the actual solution $y ( x ) = 1 / ( x + 3 )$

3.Use the Nonlinear Finite-Difference Algorithm with $T O L = 1 0 ^ { - 4 }$ to approximate the solution to the following boundary-value problems. The actual solution is given for comparison to your results.

a. y"= y³- yy'， $1 \leq x \leq 2$ ， $\begin{array} { r } { y ( 1 ) = ~ \frac { 1 } { 2 } } \end{array}$ ， $y ( 2 ) = \textstyle { \frac { 1 } { 3 } }$ ; use $h \ = \ 0 . 1$ ； actual solution $y ( x ) = ( x + 1 ) ^ { - 1 }$   
b. $\begin{array} { r } { y ^ { \prime \prime } = 2 y ^ { 3 } - 6 y , - 2 x ^ { 3 } , \quad 1 \leq x \leq 2 , \ y ( 1 ) = 2 , \ y ( 2 ) = \frac { 5 } { 2 } ; } \end{array}$ use $h = 0 . 1$ ; actual solution $y ( x ) = x + x ^ { - 1 }$   
c. $y ^ { \prime \prime } = y ^ { \prime } + 2 ( y - \ln x ) ^ { 3 } - x ^ { - 1 } , \quad 2 \leq x \leq 3 , \ y ( 2 ) = { \textstyle { \frac { 1 } { 2 } } } + \ln 2 , \ y ( 3 ) = { \textstyle { \frac { 1 } { 3 } } } + \ln 3 ;$ use $h = 0 . 1$ ; actual solution $y ( x ) = x ^ { - 1 } + \ln x$   
d $y ^ { \prime \prime } = \left( x ^ { 2 } ( y ^ { \prime } ) ^ { 2 } - 9 y ^ { 2 } + 4 x ^ { 6 } \right) / x ^ { 5 } , \quad 1 \leq x \leq 2 , \ y ( 1 ) = 0 , \ y ( 2 ) = \ln 2 5 6 ;$ use $h = 0 . 0 5$ ； actual solution $y ( x ) = x ^ { 3 } \ln x$

4.Repeat Exercise 3(a) and (b) using extrapolation.

5. Show that the hypotheses listed at the beginning of the section ensure the nonsingularity of the Jacobian matrix $J$ for $h < 2 / L$ ·

6.In Exercise 7 of Section 11.3,the deflection of a beam with supported ends subject to uniform loading was approximated. Using a more appropriate representation of curvature gives the differential equation

$$
[ 1 + ( w ^ { \prime } ( x ) ) ^ { 2 } ] ^ { - 3 / 2 } w ^ { \prime \prime } ( x ) = \frac { S } { E I } w ( x ) + \frac { q x } { 2 E I } ( x - l ) , \quad \mathrm { f o r } 0 < x < l .
$$

Approximate the deflection $w ( x )$ of the beam every 6 in. and compare the results to those of Exercise 7 of Section 11.3.

# 11.5 The Rayleigh-Ritz Method

The Shooting method for approximating the solution to a boundary-value problem replaced the boundary-value problem with pair of initial-value problems. The finite-difference ap-proach replaces the continuous operation of differentiation with the discrete operation of finite differences. The Rayleigh-Ritz method is a variational technique that attacks the problem from a third approach. The boundary-value problem is first reformulated as a problem of choosing,from the set of allsufficiently differentiable functions satisfying the boundary conditions,the function to minimize a certain integral. Then the set of feasible functions is reduced in size, to result in an approximation to the solution of the minimization problem and (as a consequence) an approximation to the solution of the boundary-value problem.

To describe the Rayleigh-Ritz method, we consider approximating the solution to a linear two-point boundary-value problem from beam-stress analysis. This boundary-value problem is described by the differential equation

$$
- { \frac { d } { d x } } \left( p ( x ) { \frac { d y } { d x } } \right) + q ( x ) y = f ( x ) , \quad { \mathrm { f o r ~ } } 0 \leq x \leq 1 ,
$$

with the boundary conditions

$$
y ( 0 ) = y ( 1 ) = 0 .
$$

This differential equation describes the deflection $y ( x )$ of a beam of length 1 with variable cross section represented by $q ( x )$ .The deflection is due to the added stresses $p ( x )$ and $f ( x )$

In the discussion that follows, we assume that $p \in C ^ { 1 } [ 0 , 1 ]$ and $q , f \in C [ 0 , 1 ]$ Further, we assume that there exists a constant $\delta > 0$ such that

$$
p ( x ) \geq \delta , \quad \mathrm { a n d \ t h a t } \quad q ( x ) \geq 0 , \quad \mathrm { f o r \ e a c h \ x \ i n \ \Gamma } [ 0 , 1 ] .
$$

Theseassumptionsare sufficient to guaranteethat the boundary-value problem given in (11.22) and (11.23) has a unique solution (see [BSW]).

As is the case in many boundary-value problems that describe physical phenomena, the solution to the beam equation satisfies a variational property. The variational principle for the beam equation is fundamental to the development of the Rayleigh-Ritz method and characterizes the solution to the beam equation as the function that minimizes a certain integral over all functions in $C _ { 0 } ^ { 2 } [ 0 , 1 ]$ ,the set of those functions $\pmb { u }$ in $C ^ { 2 } [ 0 , 1 ]$ with the property that $u ( 0 ) = u ( 1 ) = 0$ . The following theorem gives the characterization.

Theorem 11.4

Let $p \in C ^ { 1 } [ 0 , 1 ] , q , f \in C [ 0 , 1 ]$ and

$$
p ( x ) \geq \delta > 0 , \quad q ( x ) \geq 0 , \quad { \mathrm { f o r ~ } } 0 \leq x \leq 1 .
$$

The function $y \in C _ { 0 } ^ { 2 } [ 0 , 1 ]$ is the unique solution to the differential equation

$$
- { \frac { d } { d x } } \left( p ( x ) { \frac { d y } { d x } } \right) + q ( x ) y = f ( x ) , \quad { \mathrm { f o r ~ } } 0 \leq x \leq 1 ,
$$

if and only if $y$ is the unique function in $C _ { 0 } ^ { 2 } [ 0 , 1 ]$ that minimizes the integral

$$
I [ u ] = \int _ { 0 } ^ { 1 } \{ p ( x ) [ u ^ { \prime } ( x ) ] ^ { 2 } + q ( x ) [ u ( x ) ] ^ { 2 } - 2 f ( x ) u ( x ) \} d x .
$$

Details of the proof of this theorem can be found in [Shul, pp. 88-89]. It proceeds in three steps. First it is shown that any solution $y$ to (11.24) also satisfes the equation

$$
\int _ { 0 } ^ { 1 } f ( x ) u ( x ) d x = \int _ { 0 } ^ { 1 } p ( x ) { \frac { d y } { d x } } ( x ) { \frac { d u } { d x } } ( x ) + q ( x ) y ( x ) u ( x ) d x ,
$$

for all $u \in C _ { 0 } ^ { 2 } \{ 0 . 1 \}$

The second step shows that $y \in C _ { 0 } ^ { 2 } [ 0 , 1 ]$ is a solution to (11.25) if and only if (1 holds for all $u \in C _ { 0 } ^ { 2 } [ 0 , 1 ]$

The final step shows that (11.26) has a unique solution. This unique solution will also be a solution to (11.25) and to (11.24), so the solutions to (11.24) and (11.25) are identical.

The Rayleigh-Ritz method approximates the solution $y$ by minimizing the integral, not over all the functions in $C _ { 0 } ^ { 2 } [ 0 , 1 ]$ ,but over a smaller set of functions consisting of linear combinations of certain basis functions $\phi _ { 1 } , \phi _ { 2 } , \ldots , \phi _ { n }$ . The basis functions are linearly independent and satisfy

$$
\phi _ { i } ( 0 ) = \phi _ { i } ( 1 ) = 0 , \qquad \mathrm { f o r ~ e a c h } \ : i = 1 , 2 , \ldots , n .
$$

An approximation $\begin{array} { r } { \phi ( x ) = \sum _ { i = 1 } ^ { n } c _ { i } \phi _ { i } ( x ) } \end{array}$ to the solution $y ( x )$ of Eq. (11.24) is then obtained by finding constants $c _ { 1 } , c _ { 2 } , \ldots , c _ { n }$ to minimize $I \left[ \textstyle \sum _ { i = 1 } ^ { n } c _ { i } \phi _ { i } \right]$

From Eq. (11.25),

$$
\begin{array} { l } { { I [ \phi ] = I \displaystyle \left[ \sum _ { i = 1 } ^ { n } c _ { \mathrm { i } } \phi _ { i } \right] \qquad } } \\ { { \qquad = \displaystyle \int _ { 0 } ^ { 1 } \left\{ p ( x ) \left[ \sum _ { i = 1 } ^ { n } c _ { i } \phi _ { i } ^ { \prime } ( x ) \right] ^ { 2 } + q ( x ) \biggl [ \sum _ { i = 1 } ^ { n } c _ { i } \phi _ { i } ( x ) \biggr ] ^ { 2 } - 2 f ( x ) \sum _ { i = 1 } ^ { n } c _ { i } \phi _ { i } ( x ) \right\} d x } } \end{array}
$$

and,for a minimum to occur, it is necessary, when considering $I$ as a function of $c _ { 1 } , c _ { 2 }$ $\cdots , c _ { n }$ ,to have

$$
{ \frac { \partial I } { \partial c _ { j } } } = 0 , \qquad { \mathrm { f o r } } \operatorname { e a c h } j = 1 , 2 , \ldots , n .
$$

Differentiating （11.27) gives

$$
\frac { \partial I } { \partial c _ { j } } = \int _ { 0 } ^ { 1 } \left\{ 2 p ( x ) \sum _ { i = 1 } ^ { n } c _ { i } \phi _ { i } ^ { \prime } ( x ) \phi _ { j } ^ { \prime } ( x ) + 2 q ( x ) \sum _ { i = 1 } ^ { n } c _ { i } \phi _ { i } ( x ) \phi _ { j } ( x ) - 2 f ( x ) \phi _ { j } ( x ) \right\} d x ,
$$

and substituting into Eq.(11.28) yields

$$
0 = \sum _ { i = 1 } ^ { n } \biggl [ \int _ { 0 } ^ { 1 } \{ p ( x ) \phi _ { i } ^ { \prime } ( x ) \phi _ { j } ^ { \prime } ( x ) + q ( x ) \phi _ { i } ( x ) \phi _ { j } ( x ) \} d x \biggr ] c _ { i } - \int _ { 0 } ^ { 1 } f ( x ) \phi _ { j } ( x ) d x ,
$$

for each $j = 1 , 2 , \ldots , n$

The normal equations described in Eq.(11.29) produce an $n \times n$ linear system $A \mathbf { c } = \mathbf { b }$ in the variables $c _ { 1 } , c _ { 2 } , \ldots , c _ { n }$ , where the symmetric matrix $A$ is given by

$$
a _ { i j } = \int _ { 0 } ^ { 1 } [ p ( x ) \phi _ { i } ^ { \prime } ( x ) \phi _ { j } ^ { \prime } ( x ) + q ( x ) \phi _ { i } ( x ) \phi _ { j } ( x ) ] d x ,
$$

and b is defined by

$$
b _ { i } = \int _ { 0 } ^ { 1 } f ( x ) \phi _ { i } ( x ) d x .
$$

The simplest choice of basis functions involves piecewise-linear polynomials.The first step is to form a partition of [O,1] by choosing points $x _ { 0 } , x _ { 1 } , \ldots , x _ { n + 1 }$ with

$$
0 = x _ { 0 } < x _ { 1 } < \cdot \cdot \cdot < x _ { n } < x _ { n + 1 } = 1 .
$$

Letting $h _ { i } = x _ { i + 1 } - x _ { i }$ ,for each $i = 0 , 1 , \ldots , n$ ， we define the basis functions $\phi _ { 1 } ( x )$ $\phi _ { 2 } ( x ) , \ldots , \phi _ { n } ( x )$ by

$$
\phi _ { i } ( x ) = \left\{ \begin{array} { l l } { 0 , } & { \mathrm { i f } \quad 0 \leq x \leq x _ { i - 1 } , } \\ { \displaystyle { \frac { 1 } { h _ { i - 1 } } } ( x - x _ { i - 1 } ) , } & { \mathrm { i f } \quad x _ { i - 1 } < x \leq x _ { i } , } \\ { \displaystyle { \frac { 1 } { h _ { i } } } ( x _ { i + 1 } - x ) , } & { \mathrm { i f } \quad x _ { i } < x \leq x _ { i + 1 } , } \\ { 0 , } & { \mathrm { i f } \quad x _ { i + 1 } < x \leq 1 , } \end{array} \right.
$$

for each $i = 1 , 2 , \ldots , n$ . (See Figure 11.4.)

![](images/75315208d5ab52418d7425ef477f502ff20752a9f6ccc33a19f944f1e02002a8.jpg)  
Figure 11.4

Since the functions $\phi _ { i }$ are piecewise-linear, the derivatives $\phi _ { i } ^ { \prime }$ ， while not continuous, are constant on $( x _ { j } , x _ { j + 1 } )$ ,for each $j = 0 , 1 , \ldots , n$ ,and

$$
\phi _ { i } ^ { \prime } ( x ) = \left\{ \begin{array} { l l } { 0 , } & { \mathrm { i f } \quad 0 < x < x _ { i - 1 } , } \\ { \displaystyle \frac { 1 } { h _ { i - 1 } } , } & { \mathrm { i f } \quad x _ { i - 1 } < x < x _ { i } , } \\ { - \displaystyle \frac { 1 } { h _ { i } } , } & { \mathrm { i f } \quad x _ { i } < x < x _ { i + 1 } , } \\ { 0 , } & { \mathrm { i f } \quad x _ { i + 1 } < x < 1 , } \end{array} \right.
$$

for each $i = 1 , 2 , \ldots , n$

Because $\phi _ { i }$ and $\phi _ { i } ^ { \prime }$ are nonzero only on $( x _ { i - 1 } , x _ { i + 1 } )$ ，

$$
\phi _ { i } ( x ) \phi _ { j } ( x ) \equiv 0 \qquad \mathrm { a n d } \qquad \phi _ { i } ^ { \prime } ( x ) \phi _ { j } ^ { \prime } ( x ) \equiv 0 ,
$$

except when $j \ i \ s \ i - 1 , i$ or $i + 1$ . As a consequence, the linear system given by (11.29) reduces to an $n \times n$ tridiagonal linear system. The nonzero entries in $A$ are

$$
\begin{array} { l } { \displaystyle { a _ { i i } = \int _ { 0 } ^ { 1 } \left\{ p ( x ) [ \phi _ { i } ^ { \prime } ( x ) ] ^ { 2 } + q ( x ) [ \phi _ { i } ( x ) ] ^ { 2 } \right\} d x } } \\ { \displaystyle { \quad = \left( \frac { 1 } { h _ { i - 1 } } \right) ^ { 2 } \int _ { x _ { i - 1 } } ^ { x _ { i } } p ( x ) d x + \left( \frac { - 1 } { h _ { i } } \right) ^ { 2 } \int _ { x _ { i } } ^ { x _ { i + 1 } } p ( x ) d x } } \\ { \displaystyle { \quad + \left( \frac { 1 } { h _ { i - 1 } } \right) ^ { 2 } \int _ { x _ { i - 1 } } ^ { x _ { i } } ( x - x _ { i - 1 } ) ^ { 2 } q ( x ) d x + \left( \frac { 1 } { h _ { i } } \right) ^ { 2 } \int _ { x _ { i } } ^ { x _ { i + 1 } } ( x _ { i + 1 } - x ) ^ { 2 } q ( x ) d x } . }  \end{array}
$$

for each $i = 1 , 2 , \dots , n ;$

$$
\begin{array} { l } { \displaystyle a _ { i , i + 1 } = \int _ { 0 } ^ { 1 } \{ p ( x ) \phi _ { i } ^ { \prime } ( x ) \phi _ { i + 1 } ^ { \prime } ( x ) + q ( x ) \phi _ { i } ( x ) \phi _ { i + 1 } ( x ) \} d x } \\ { \displaystyle \quad = - \left( \frac { 1 } { h _ { i } } \right) ^ { 2 } \int _ { x _ { i } } ^ { x _ { i + 1 } } p ( x ) d x + \left( \frac { 1 } { h _ { i } } \right) ^ { 2 } \int _ { x _ { i } } ^ { x _ { i + 1 } } ( x _ { i + 1 } - x ) ( x - x _ { i } ) q ( x ) d x , } \end{array}
$$

for each $i = 1 , 2 , \ldots , n - 1$ ; and

$$
\begin{array} { l } { \displaystyle a _ { i , i - 1 } = \int _ { 0 } ^ { 1 } \{ p ( x ) \phi _ { i } ^ { \prime } ( x ) \phi _ { i - 1 } ^ { \prime } ( x ) + q ( x ) \phi _ { i } ( x ) \phi _ { i - 1 } ( x ) \} d x } \\ { \displaystyle \ = - \biggl ( \frac { 1 } { h _ { i - 1 } } \biggr ) ^ { 2 } \int _ { x _ { i - 1 } } ^ { x _ { i } } p ( x ) d x + \biggl ( \frac { 1 } { h _ { i - 1 } } \biggr ) ^ { 2 } \int _ { x _ { i - 1 } } ^ { x _ { i } } ( x _ { i } - x ) ( x - x _ { i - 1 } ) q ( x ) d x , } \end{array}
$$

for each $i = 2 , \ldots , n$ . The entries in b are

$$
b _ { i } = \int _ { 0 } ^ { 1 } f ( x ) \phi _ { i } ( x ) d x = { \frac { 1 } { h _ { i - 1 } } } \int _ { x _ { i - 1 } } ^ { x _ { i } } ( x - x _ { i - 1 } ) f ( x ) d x + { \frac { 1 } { h _ { i } } } \int _ { x _ { i } } ^ { x _ { i + 1 } } ( x _ { i + 1 } - x ) f ( x ) d x .
$$

for each $i = 1 , 2 , \ldots , n$

There are six types of integrals to be evaluated:

$$
\begin{array} { l } { \displaystyle Q _ { 1 , i } = \left( \frac 1 { h _ { i } } \right) ^ { 2 } \int _ { x _ { i } } ^ { x _ { i + 1 } } ( x _ { i + 1 } - x ) ( x - x _ { i } ) q ( x ) d x , \quad \mathrm { ~ f o r ~ e a c h ~ } i = 1 , 2 , . . } \\ { \displaystyle Q _ { 2 , i } = \left( \frac 1 { h _ { i - 1 } } \right) ^ { 2 } \int _ { x _ { i - 1 } } ^ { x _ { i } } ( x - x _ { i - 1 } ) ^ { 2 } q ( x ) d x , \quad \mathrm { ~ f o r ~ e a c h ~ } i = 1 , 2 , . . . , n , } \\ { \displaystyle Q _ { 3 , i } = \left( \frac 1 { h _ { i } } \right) ^ { 2 } \int _ { x _ { i } } ^ { x _ { i + 1 } } ( x _ { i + 1 } - x ) ^ { 2 } q ( x ) d x , \quad \mathrm { ~ f o r ~ e a c h ~ } i = 1 , 2 , . . . , n , } \end{array}
$$

$$
\begin{array} { l l l } { \displaystyle { Q _ { 4 , i } = \left( \frac { 1 } { h _ { i - 1 } } \right) ^ { 2 } \int _ { x _ { i - 1 } } ^ { x _ { i } } p ( x ) d x , \quad \mathrm { f o r e a c h } i = 1 , 2 , \dots , n + 1 , } } \\ { \displaystyle { Q _ { 5 , i } = \frac { 1 } { h _ { i - 1 } } \int _ { x _ { i - 1 } } ^ { x _ { i } } ( x - x _ { i - 1 } ) f ( x ) d x , \quad \mathrm { f o r e a c h } i = 1 , 2 , \dots , n , } } \end{array}
$$

and

$$
Q _ { 6 , i } = { \frac { 1 } { h _ { i } } } \int _ { x _ { i } } ^ { x _ { i + 1 } } ( x _ { i + 1 } - x ) f ( x ) d x , \quad { \mathrm { f o r ~ e a c h ~ } } i = 1 , 2 , \dots , n .
$$

The matrix $A$ and the vector $\mathbf { b }$ in the linear system $\pmb { A } \mathbf { c } = \mathbf { b }$ have the entries

$$
\begin{array} { r l } & { \quad a _ { i , i } = Q _ { 4 , i } + Q _ { 4 , i + 1 } + Q _ { 2 , i } + Q _ { 3 , i } , \quad \mathrm { f o r ~ e a c h } \ i = 1 , 2 , \ldots , n , } \\ & { \quad a _ { i , i + 1 } = - Q _ { 4 , i + 1 } + Q _ { 1 , i } , \quad \mathrm { f o r ~ e a c h } \ i = 1 , 2 , \ldots , n - 1 , } \\ & { \quad a _ { i , i - 1 } = - Q _ { 4 , i } + Q _ { 1 , i - 1 } , \quad \mathrm { f o r ~ e a c h } \ i = 2 , 3 , \ldots , n , } \end{array}
$$

and

$$
b _ { i } = Q _ { 5 , i } + Q _ { 6 , i } , \quad \mathrm { f o r e a c h } i = 1 , 2 , \dots , n .
$$

The entries in c are the unknown coefficients $c _ { 1 } , c _ { 2 } , \ldots , c _ { n }$ , from which the Rayleigh-Ritz approximation $\phi$ , given by $\phi ( x ) = \sum _ { i = 1 } ^ { n } c _ { i } \phi _ { i } ( x )$ , is constructed.

A practical difficulty with this method is the necessity of evaluating 6n integrals. The integrals can be evaluated either directly or by a quadrature formula such as Composite Simpson's rule. An alternative approach for the integral evaluation is to approximate each of the functions $p , q$ ,and $f$ with its piecewise-linear interpolating polynomial and then integrate the approximation. Consider,for example, the integral $Q _ { 1 , i }$ . The piecewise-linear interpolation of $q$ is

$$
P _ { q } ( x ) = \sum _ { i = 0 } ^ { n + 1 } q ( x _ { i } ) \phi _ { i } ( x ) ,
$$

where $\phi _ { 1 } , \ldots , \phi _ { n }$ are defined in (11.30) and

$$
b _ { 0 } ( x ) = \left\{ \begin{array} { l l } { \displaystyle \frac { x _ { 1 } - x } { x _ { 1 } } , \quad i \mathbf { f } \quad 0 \leq x \leq x _ { 1 } } \\ { \displaystyle 0 , \quad \mathrm { e l s e w h e r e } } \end{array} \right. \quad \quad \mathrm { a n d } \quad \quad \phi _ { n + 1 } ( x ) = \left\{ \begin{array} { l l } { \displaystyle \frac { x - x _ { n } } { 1 - x _ { n } } , \quad \mathrm { i f } \quad x _ { n } \leq x \leq x _ { 1 } } \\ { \displaystyle 0 , \quad \mathrm { e l s e w h e r e . } } \end{array} \right.
$$

Since the interval of integration is $[ x _ { i } , x _ { i + 1 } ]$ ,the piecewise polynomial $P _ { q } ( x )$ reduces to

$$
P _ { q } ( x ) = q ( x _ { i } ) \phi _ { i } ( x ) + q ( x _ { i + 1 } ) \phi _ { i + 1 } ( x ) .
$$

This is the first-degree interpolating polynomial studied in Section 3.1.By Theorem 3.3,

$$
| q ( x ) - P _ { q } ( x ) | = O ( h _ { i } ^ { 2 } ) , \quad \mathrm { f o r } x _ { i } \leq x \leq x _ { i + 1 } ,
$$

if $q \in C ^ { 2 } [ x _ { i } , x _ { i + 1 } ]$ .For $i = 1 , 2 , \dots , n - 1$ , the approximation to $Q _ { 1 , i }$ is obtained by integrating the approximation to the integrand

$$
\begin{array} { l } { \displaystyle Q _ { 1 , i } = \left( \frac { 1 } { h _ { i } } \right) ^ { 2 } \int _ { x _ { i } } ^ { x _ { i + 1 } } ( x _ { i + 1 } - x ) ( x - x _ { i } ) q ( x ) d x } \\ { \displaystyle \approx \left( \frac { 1 } { h _ { i } } \right) ^ { 2 } \int _ { x _ { i } } ^ { x _ { i + 1 } } ( x _ { i + 1 } - x ) ( x - x _ { i } ) \biggl [ \frac { q ( x _ { i } ) ( x _ { i + 1 } - x ) } { h _ { i } } + \frac { q ( x _ { i + 1 } ) ( x - x _ { i } ) } { h _ { i } } \biggr ] d x } \\ { \displaystyle = \frac { h _ { i } } { 1 2 } [ q ( x _ { i } ) + q ( x _ { i + 1 } ) ] . } \end{array}
$$

Further, if $q \in C ^ { 2 } [ x _ { i } , x _ { i + 1 } ]$ ,then

$$
\left| Q _ { 1 , i } - \frac { h _ { i } } { 1 2 } [ q ( x _ { i } ) + q ( x _ { i + 1 } ) ] \right| = O ( h _ { i } ^ { 3 } ) .
$$

Approximations to the other integrals are derived in a similar manner and are given by

$$
\begin{array} { l } { { \displaystyle Q _ { 2 , i } \approx \frac { h _ { i - 1 } } { 1 2 } [ 3 q ( x _ { i } ) + q ( x _ { i - 1 } ) ] , \qquad Q _ { 3 , i } \approx \frac { h _ { i } } { 1 2 } [ 3 q ( x _ { i } ) + q ( x _ { i + 1 } ) ] , } } \\ { { \displaystyle Q _ { 4 , i } \approx \frac { h _ { i - 1 } } { 2 } [ p ( x _ { i } ) + p ( x _ { i - 1 } ) ] , \qquad Q _ { 5 , i } \approx \frac { h _ { i - 1 } } { 6 } [ 2 f ( x _ { i } ) + f ( x _ { i - 1 } ) ] , } } \end{array}
$$

and

$$
Q _ { 6 , i } \approx \frac { h _ { i } } { 6 } [ 2 f ( x _ { i } ) + f ( x _ { i + 1 } ) ] .
$$

Algorithm 115 sets up the tridiagonal linear system and incorporates the Crout Factorization Algorithm 6.7 to solve the system. The integrals $Q _ { 1 , i } , \ldots , Q _ { 6 , i }$ can be computed by one of the methods mentioned previously.

# Piecewise Linear Rayleigh-Ritz

To approximate the solution to the boundary-value problem

$$
- { \frac { d } { d x } } \left( p ( x ) { \frac { d y } { d x } } \right) + q ( x ) y = f ( x ) , \quad 0 \leq x \leq 1 , \quad y ( 0 ) = y ( 1 ) = 0 ,
$$

with the piecewise linear function

$$
\phi ( x ) = \sum _ { i = 1 } ^ { n } c _ { i } \phi _ { i } ( x ) :
$$

INPUT integer $n \geq 1$ ; points $x _ { 0 } = 0 < x _ { 1 } < \cdot \cdot \cdot < x _ { n } < x _ { n + 1 } = 1$

OUTPUT coefficients $c _ { 1 } , \ldots , c _ { n }$

Step 1 For $i = 0 , \ldots , n$ set $h _ { i } = x _ { i + 1 } - x _ { i }$

Step 2For $i = 1 , \ldots , n$ define the piecewise linear basis $\phi _ { i }$ by

$$
\phi _ { i } ( x ) = \left\{ \begin{array} { l l } { 0 , } & { 0 \leq x \leq x _ { i - 1 } , } \\ { \frac { x - x _ { i - 1 } } { h _ { i - 1 } } , } & { x _ { i - 1 } < x \leq x _ { i } , } \\ { \frac { x _ { i + 1 } - x } { h _ { i } } , } & { x _ { i } < x \leq x _ { i + 1 } , } \\ { 0 , } & { x _ { i + 1 } < x \leq 1 . } \end{array} \right.
$$

Step 3 For each $i = 1 , 2 , \ldots , n - 1$ compute $Q _ { 1 , i } , Q _ { 2 , i } , Q _ { 3 , i } , Q _ { 4 , i } , Q _ { 5 , i } , Q _ { 6 , i } ;$ Compute $Q _ { 2 , n } , Q _ { 3 , n } , Q _ { 4 , n } , Q _ { 4 , n + 1 } , Q _ { 5 , n } , Q _ { 6 , n }$

Step 4 For each $i = 1 , 2 , \ldots , n - 1$ ,set $\alpha _ { i } = Q _ { 4 , i } + Q _ { 4 , i + 1 } + Q _ { 2 , i } + Q _ { 3 , i } ;$ $\beta _ { i } = Q _ { 1 , i } - Q _ { 4 , i + 1 } $ $b _ { i } = Q _ { 5 , i } + Q _ { 6 , i }$

Step 5Set $\alpha _ { n } = Q _ { 4 , n } + Q _ { 4 , n + 1 } + Q _ { 2 , n } + Q _ { 3 , n } ;$ $b _ { n } = Q _ { 5 , n } + Q _ { 6 , n } .$

Step 6 Set $a _ { 1 } = \alpha _ { 1 }$ ; (Steps 6-10 solve $a$ symmetric tridiagonal linear system using Algorithm 6.7.)

$$
\begin{array} { l } { { \zeta _ { 1 } = \beta _ { 1 } / \alpha _ { 1 } ; } } \\ { { z _ { 1 } = b _ { 1 } / a _ { 1 } . } } \end{array}
$$

$$
\begin{array} { r l r } & { } & { p 7 \quad \mathrm { F o r } i = 2 , \ldots , n - 1 \mathrm { s e t } a _ { i } = \alpha _ { i } - \beta _ { i - 1 } \zeta _ { i - 1 } ; } \\ & { } & { \zeta _ { i } = \beta _ { i } / a _ { i } ; } \\ & { } & { z _ { i } = ( b _ { i } - \beta _ { i - 1 } z _ { i - 1 } ) / a _ { i } . } \end{array}
$$

Step 8 Set $a _ { n } = \alpha _ { n } - \beta _ { n - 1 } \zeta _ { n - 1 }$ ；$z _ { n } = ( b _ { n } - \beta _ { n - 1 } z _ { n - 1 } ) / a _ { n } .$

Step 9 Set $c _ { n } = z _ { n }$ ； OUTPUT $\left( c _ { n } \right)$

Step 10 For $i = n  1$ ,...,1 set $c _ { i } = z _ { i } - \zeta _ { i } c _ { i + 1 } ;$ OUTPUT $\left( c _ { i } \right)$

Step 11 STOP.(The procedure is complete.)

The following example uses Algorithm 11.5. Because of the elementary nature of this example, the integrals in Steps 3,4,and 5 were found directly.

Consider the boundary-value problem

$$
- y ^ { \prime \prime } + \pi ^ { 2 } y = 2 \pi ^ { 2 } \sin ( \pi x ) , \quad 0 \leq x \leq 1 , \quad y ( 0 ) = y ( 1 ) = 0 ,
$$

Let $h _ { i } = h = 0 . 1$ ,so that $x _ { i } = 0 . 1 i$ , for each $i = 0 , 1 , \ldots , 9$ . The integrals are

$$
Q _ { 1 , i } = 1 0 0 \int _ { 0 . 1 i } ^ { 0 . 1 i + 0 . 1 } ( 0 . 1 i + 0 . 1 - x ) ( x - 0 . 1 i ) \pi ^ { 2 } d x = \frac { \pi ^ { 2 } } { 6 0 } ,
$$

$$
\begin{array} { l } { { Q _ { 2 , i } = 1 0 0 \int _ { 0 , 1 i - 0 , 1 } ^ { 0 . 1 i } \left( x - 0 . 1 i + 0 . 1 \right) ^ { 2 } \pi ^ { 2 } d x = \displaystyle \frac { \pi ^ { 2 } } { 3 0 } , } } \\ { { \ } } \\ { { Q _ { 3 , i } = 1 0 0 \int _ { 0 , 1 i } ^ { 0 . 1 i + 0 . 1 } \left( 0 . 1 i + 0 . 1 - x \right) ^ { 2 } \pi ^ { 2 } d x = \displaystyle \frac { \pi ^ { 2 } } { 3 0 } , } } \\ { { \ } } \\ { { Q _ { 4 , i } = 1 0 0 \int _ { 0 , 1 i - 0 , 1 } ^ { 0 . 1 i } d x = 1 0 , } } \\ { { \ } } \\ { { Q _ { 5 , i } = 1 0 \int _ { 0 , 1 i - 0 . 1 } ^ { 0 . 1 i } \left( x - 0 . 1 i + 0 . 1 \right) 2 \pi ^ { 2 } \sin \pi x d x } } \\ { { \ } } \\ { { \ } } \\ { { = - 2 \pi \cos \Theta . \mathrm { 1 r } i + 2 0 5 \sin ( 0 . 1 i - 0 . 1 \pi i ) - \sin ( ( 0 . 1 i - 0 . 1 ) \pi ) ) } } \end{array}
$$

and

$$
\begin{array} { l } { { \displaystyle Q _ { 6 , i } = 1 0 \int _ { 0 . 1 i } ^ { 0 . 1 i + 0 . 1 } ( 0 . 1 i + 0 . 1 - x ) 2 \pi ^ { 2 } \sin \pi x ~ d x } } \\ { { \displaystyle ~ = 2 \pi \cos 0 . 1 \pi i - 2 0 [ \sin ( ( 0 . 1 i + 0 . 1 ) \pi ) - \sin ( 0 . 1 \pi i ) ] . } } \end{array}
$$

The linear system $\pmb { A } \pmb { c } = \pmb { b }$ has

$$
\begin{array} { c } { { a _ { i , i } = 2 0 + { \displaystyle \frac { \pi ^ { 2 } } { 1 5 } } , \qquad \mathrm { f o r ~ e a c h } \ i = 1 , 2 , \dots , 9 , } } \\ { { \nonumber } } \\ { { a _ { i , i + 1 } = - 1 0 + { \displaystyle \frac { \pi ^ { 2 } } { 6 0 } } , \qquad \mathrm { f o r ~ e a c h } \ i = 1 , 2 , \dots , 8 , } } \\ { { \nonumber } } \\ { { a _ { i , i - 1 } = - 1 0 + { \displaystyle \frac { \pi ^ { 2 } } { 6 0 } } , \qquad \mathrm { f o r ~ e a c h } \ i = 2 , 3 , \dots , 9 , } } \end{array}
$$

and

$$
b _ { i } = 4 0 \sin ( 0 . 1 \pi i ) [ 1 - \cos 0 . 1 \pi ] ,
$$

The solution to the tridiagonal linear system is

$$
\begin{array} { r l } & { c _ { 9 } = 0 . 3 1 0 2 8 6 6 7 4 2 , ~ c _ { 8 } = 0 . 5 9 0 2 0 0 3 2 7 1 , ~ c _ { 7 } = 0 . 8 1 2 3 4 1 0 5 9 8 , } \\ & { c _ { 6 } = 0 . 9 5 4 9 6 4 1 8 9 3 , ~ c _ { 5 } = 1 . 0 0 4 1 0 8 7 7 1 , ~ c _ { 4 } = 0 . 9 5 4 9 6 4 1 8 9 3 , } \\ & { c _ { 3 } = 0 . 8 1 2 3 4 1 0 5 9 8 , ~ c _ { 2 } = 0 . 5 9 0 2 0 0 3 2 7 1 , ~ c _ { 1 } = 0 . 3 1 0 2 8 6 6 7 4 2 . } \end{array}
$$

The piecewise-linear approximation is

$$
\phi ( x ) = \sum _ { i = 1 } ^ { 9 } c _ { i } \phi _ { i } ( x ) ,
$$

and the actual solution to the boundary-value problem is

$$
y ( x ) = \sin \pi x .
$$

Table 11.7 lists the error in the approximation at $x _ { i }$ , for each $i = 1 , \ldots , 9$

Table 11.7   

<table><tr><td>i</td><td>Xi</td><td>(xi）</td><td>y(xi)</td><td>(x）-y(xi）l</td></tr><tr><td>1</td><td>0.1</td><td>0.3102866742</td><td>0.3090169943</td><td>0.00127</td></tr><tr><td>2</td><td>0.2</td><td>0.5902003271</td><td>0.5877852522</td><td>0.00241</td></tr><tr><td>3</td><td>0.3</td><td>0.8123410598</td><td>0.8090169943</td><td>0.00332</td></tr><tr><td>4</td><td>0.4</td><td>0.9549641896</td><td>0.9510565162</td><td>0.00390</td></tr><tr><td>5</td><td>0.5</td><td>1.0041087710</td><td>1.0000000000</td><td>0.00411</td></tr><tr><td>6</td><td>0.6</td><td>0.9549641893</td><td>0.9510565162</td><td>0.00390</td></tr><tr><td>7</td><td>0.7</td><td>0.8123410598</td><td>0.8090169943</td><td>0.00332</td></tr><tr><td>8</td><td>0.8</td><td>0.5902003271</td><td>0.5877852522</td><td>0.00241</td></tr><tr><td>9</td><td>0.9</td><td>0.3102866742</td><td>0.3090169943</td><td>0.00127</td></tr></table>

It can be shown that the tridiagonal matrix $\pmb { A }$ given by the piecewise-linear basis functions is positive definite (see Exercise 12),so,by Theorem 6.24, the linear system is stable with respect to roundoff error. Under the hypotheses presented at the beginning of this section, we have

$$
| \phi ( x ) - y ( x ) | = O ( h ^ { 2 } ) , \quad \mathrm { f o r } \operatorname { e a c h } x \operatorname { i n } [ 0 , 1 ] .
$$

A proof of this result can be found in [Schul, pp.103-104].

The use of piecewise-linear basis functions results in an approximate solution to Eqs.(11.22) and (11.23) that is continuous but not differentiable on [0,1].A more complicated set of basis functions is required to construct an approximation that belongs to $C _ { 0 } ^ { 2 } [ 0 , 1 ]$ .These basis functions are similar to the cubic interpolatory splines discussed in Section 3.4.

Recall that the cubic interpolatory spline $s$ on the five nodes $x _ { 0 } , x _ { 1 } , x _ { 2 } , x _ { 3 }$ ,and $x _ { 4 }$ for a function $f$ is defined by:

a. $s$ is a cubic polynomial, denoted by $S _ { j }$ ，on $[ x _ { j } , x _ { j + 1 } ]$ ,for $j = 0 , 1 , 2 , 3$ . (This gives 16 selectable constants for $s$ ,4 for each cubic.)   
b. $S ( x _ { j } ) = f ( x _ { j } )$ ，for $j = 0$ ,1,2,3,4 (5 specifed conditions).   
c. $S _ { j + 1 } ( x _ { j + 1 } ) = S _ { j } ( x _ { j + 1 } )$ ,for $j = 0$ ,1,2 (3 specified conditions).   
d. $S _ { j + 1 } ^ { \prime } ( x _ { j + 1 } ) = S _ { j } ^ { \prime } ( x _ { j + 1 } )$ ,for $j = 0$ ,1,2 (3 specified conditions).   
e. $S _ { j + 1 } ^ { \prime \prime } ( x _ { j + 1 } ) = S _ { j } ^ { \prime \prime } ( x _ { j + 1 } ) , \mathrm { f o r } j = 0 , 1 , 2 ( 3 s p e c i f i e d c o n d i t i o n s ) .$   
f. One of the following boundary conditions is satisfied: (i)Free: $S ^ { \prime \prime } ( x _ { 0 } ) = S ^ { \prime \prime } ( x _ { 4 } ) = 0$ (2 specifed conditions). (ii) Clamped: $S ^ { \prime } ( x _ { 0 } ) = f ^ { \prime } ( x _ { 0 } )$ and $S ^ { \prime } ( x _ { 4 } ) = f ^ { \prime } ( x _ { 4 } )$ (2 specified conditions).

Since uniquenessof solution requires the number of constants in (a),16, to equal the number of conditions in (b) through (f),only one of the boundary conditions in (f) can be specified for the interpolatory cubic splines.

The cubic spline functions we willuse for our basis functions are called B-splines, or bell-shaped splines. These differ from interpolatory splines in that both sets of boundary conditions in (f) are satisfied. This requires the relaxation of two of the conditions in (b) through (e). Since the spline must have two continuous derivatives on $[ x _ { 0 } , x _ { 4 } ]$ , we delete two of the interpolation conditions from the description of the interpolatory splines. In

particular, we modify condition (b) to

The basic $B$ -spline $s$ defined next and shown in Figure 11.5 uses the equally spaced nodes $x _ { 0 } = - 2 , x _ { 1 } = - 1 , x _ { 2 } = 0 , x _ { 3 } = 1$ ,and $x _ { 4 } = 2$ . It satisfies the interpolatory conditions

$$
\mathfrak { b . } \quad S ( x _ { 0 } ) = 0 , \quad S ( x _ { 2 } ) = 1 , \quad S ( x _ { 4 } ) = 0 ;
$$

as well as both sets of conditions

$$
\mathrm { ( i ) } \ S ^ { \prime \prime } ( x _ { 0 } ) = S ^ { \prime \prime } ( x _ { 4 } ) = 0 \quad \mathrm { a n d } \quad \mathrm { ( i i ) } \ S ^ { \prime } ( x _ { 0 } ) = S ^ { \prime } ( x _ { 4 } ) = 0 .
$$

![](images/ba1065a9f6a1bc1fd4dafe4b625843e703ca02d9ea220c6a75e196810461caf9.jpg)  
Figure 11.5

As a consequence, $S \in C _ { 0 } ^ { 2 } ( - \infty , \infty )$ ,and

$$
S ( x ) = \left\{ \begin{array} { l l } { 0 , } & { \mathrm { i f } \quad x \leq - 2 , } \\ { \frac { 1 } { 4 } ( 2 + x ) ^ { 3 } , } & { \mathrm { i f } \quad - 2 \leq x \leq - 1 , } \\ { \frac { 1 } { 4 } \left[ ( 2 + x ) ^ { 3 } - 4 ( 1 + x ) ^ { 3 } \right] , } & { \mathrm { i f } \quad - 1 < x \leq 0 , } \\ { \frac { 1 } { 4 } \left[ ( 2 - x ) ^ { 3 } - 4 ( 1 - x ) ^ { 3 } \right] , } & { \mathrm { i f } \quad 0 < x \leq 1 , } \\ { \frac { 1 } { 4 } ( 2 - x ) ^ { 3 } , } & { \mathrm { i f } \quad 1 < x \leq 2 , } \\ { 0 , } & { \mathrm { i f } \quad 2 < x . } \end{array} \right.
$$

To construct the basis functions $\phi _ { i }$ in $C _ { 0 } ^ { 2 } [ 0 , 1 ]$ ,we first partition [0,1]by choosing a positive integer $x _ { i } = i h$ freach $\pmb { n }$ $i = 0 , 1 , \ldots , n + 1$ and defining $h = 1 / ( n + 1 )$ Wethendefine thesisfunctions . This produces the equally-spaced nodes $\{ \phi _ { i } \} _ { i = 0 } ^ { n + 1 }$ as

$$
{ \textsf { f } } \quad i = 0 ,
$$

$$
\phi _ { i } ( x ) = \left\{ \begin{array} { l l } { S \left( \frac { x } { h } \right) - 4 S \left( \frac { x + h } { h } \right) , } & \\ { S \left( \frac { x - h } { h } \right) - S \left( \frac { x + h } { h } \right) , } & \\ { S \left( \frac { x - i h } { h } \right) , } & \\ { S \left( \frac { x - n h } { h } \right) - S \left( \frac { x - ( n + 2 ) h } { h } \right) , } & \\ { S \left( \frac { x - ( n + 1 ) h } { h } \right) - 4 S \left( \frac { x - ( n + 2 ) h } { h } \right) . } & \end{array} \right.
$$

Itis notdifficuto show that $\{ \phi _ { i } \} _ { i = 0 } ^ { n + 1 }$ isealeptsii $\phi _ { i } ( 0 ) = \phi _ { i } ( 1 ) = 0 .$ ,for each $i \ : = 0$ ,1,...,n, $n + 1$ (see Exercise 11). The graphs of $\phi _ { i }$ ， for $2 \leq i \leq n - 1$ , are shown in Figure 11.6,and the graphs of $\phi _ { 0 } , \phi _ { 1 } , \phi _ { n }$ ,and $\phi _ { n + 1 }$ are in Figure 11.7.

![](images/ba237cadbda62ad3786e56d33a59ef54797b2277fccfa2356b9c60f4159b2c1a.jpg)  
Figure 11.6

![](images/2da485d9cb381d080906fc3cff720990b2afeba88095f5356d39ab845d51b9eb.jpg)  
Figure 11.7

Since $\phi _ { i } ( x )$ and $\phi _ { i } ^ { \prime } ( x )$ are nonzero only for $x \in [ x _ { i - 2 } , x _ { i + 2 } ] .$ ，the matrix in the Rayleigh-Ritz approximation is a band matrix with bandwidth at most seven:

$$
\begin{array} { r }  A = [ \begin{array} { l l l l l l l l } { a _ { 0 0 } } & { a _ { 0 1 } } & { a _ { 0 2 } } & { a _ { 0 3 } } & { 0 : \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots } & { 0 } \\ { a _ { 1 0 } } & { a _ { 1 1 } } & { a _ { 1 2 } } & { a _ { 1 3 } } & { a _ { 1 4 } } & { \ddots } & { \dots } & { \vdots } \\ { a _ { 2 0 } } & { a _ { 2 1 } } & { a _ { 2 2 } } & { a _ { 2 3 } } & { a _ { 2 4 } } & { a _ { 2 5 } } & { \dots } & { \vdots } \\ { a _ { 3 0 } } & { a _ { 3 1 } } & { a _ { 3 2 } } & { a _ { 3 3 } } & { a _ { 3 4 } } & { a _ { 5 } } & { \dots } & { \ddots } \\ { 0 } & { \dots } & { \dots } & { \dots } & { a _ { 3 3 } } & { \dots } & { a _ { 3 5 } } & { \dots } & { a _ { 5 } } \\ { 0 } & { \dots } & { \dots } & { \dots } & { \dots } & { \dots } & { \dots } & { \dots } & { \dots } \\ { \vdots } & { \dots } & { \dots } & { \dots } & { \dots } & { \dots } & { \dots } & { \dots } & { \dots } & { \dots } \\ { \vdots } & { \dots } & { \dots } & { \dots } & { \dots } & { \dots } & { \dots } & { \dots } & { \dots } & { \dots } \\ { \vdots } & { \dots } & { \dots } & { \dots } & { \dots } & { \dots } & { \dots } & { \dots } & { \dots } & { \dots } \\ { \vdots } & { \dots } & { \dots } & { \dots } & { \dots } & { \dots } & { \dots } & { \dots } & { \dots } & { \dots } \\ { \vdots } & { \dots } & { \dots } & { \dots } & { \dots } & { \dots } & { \dots } & { \dots } & { \dots } \\ { 0 } & { \dots } & { \dots } & { \dots } & { \dots } & { \dots } & { \dots } & { \dots } \\ { 0 } & { \dots } & { \dots } & { \dots } & { \dots } & { \dots } & { \dots } & { \dots } \\ { 0 } & { \dots } & { \dots } & { \dots } & { \dots } & { \dots } & { \dots } \\ { 0 }  \end{array} \end{array}
$$

where

$$
a _ { i j } = \int _ { 0 } ^ { 1 } \{ p ( x ) \phi _ { i } ^ { \prime } ( x ) \phi _ { j } ^ { \prime } ( x ) + q ( x ) \phi _ { i } ( x ) \phi _ { j } ( x ) \} d x ,
$$

for each $i$ ， $j = 0 , 1 , \ldots , n + 1$ . The vector b has the entries

$$
b _ { i } = \int _ { 0 } ^ { 1 } f ( x ) \phi _ { i } ( x ) d x .
$$

The matrix $A$ is positive definite (see Exercise 13),so the linear system $A \mathfrak { c } = \mathfrak { b }$ can be solved by Choleski's Algorithm 6.6 or by Gaussian elimination. Algorithm 11.6 details the construction of the cubic spline approximation $\phi ( x )$ by the Rayleigh-Ritz method for the boundary-value problem (11.22) and (11.23) given at the beginning of this section.

# Cubic Spline Rayleigh-Ritz

To approximate the solution to the boundary-value problem

$$
- { \frac { d } { d x } } \left( p ( x ) { \frac { d y } { d x } } \right) + q ( x ) y = f ( x ) , \quad 0 \leq x \leq 1 , \quad y ( 0 ) = y ( 1 ) = 0
$$

with the sum of cubic splines

$$
\phi ( x ) = \sum _ { i = 0 } ^ { n + 1 } c _ { i } \phi _ { i } ( x ) :
$$

INPUT integer $n \geq 1$

OUTPUT coefficients $c _ { 0 } , \ldots , c _ { n + 1 }$

Step 1 Set $h = 1 / ( n + 1 )$

Step 2 For $i = 0 , \ldots , n + 1$ set $x _ { i } = i h$ Set $x _ { - 2 } = x _ { - 1 } = 0$ $x _ { n + 2 } = x _ { n + 3 } = 1$

Step 3 Define the function $\pmb { S }$ by

$$
S ( x ) = \left\{ \begin{array} { l l } { 0 , } & { x \leq - 2 , } \\ { \frac { 1 } { 4 } ( 2 + x ) ^ { 3 } , } & { - 2 < x \leq - 1 , } \\ { \frac { 1 } { 4 } \left[ ( 2 + x ) ^ { 3 } - 4 ( 1 + x ) ^ { 3 } \right] , } & { - 1 < x \leq 0 , } \\ { \frac { 1 } { 4 } \left[ ( 2 - x ) ^ { 3 } - 4 ( 1 - x ) ^ { 3 } \right] , } & { 0 < x \leq 1 , } \\ { \frac { 1 } { 4 } ( 2 - x ) ^ { 3 } , } & { 1 < x \leq 2 , } \\ { 0 , } & { 2 < x } \end{array} \right.
$$

Step 4 Define thecubic spline basis $\{ \phi _ { i } \} _ { i = 0 } ^ { n + 1 }$ by

$$
\begin{array} { r l } & { \phi _ { 0 } ( x ) = S ( \frac { x } { h } ) - 4 S ( \frac { x + h } { h } ) , } \\ & { \phi _ { 1 } ^ { * } ( x ) = S ( \frac { x - x _ { 1 } } { h } ) - S ( \frac { x + h } { h } ) , } \\ & { \phi _ { i } ( x ) = S ( \frac { x - x _ { i } } { h } ) , \mathrm { f o r } i = 2 , \dots , n - 1 , } \\ & { \phi _ { n } ( x ) = S ( \frac { x - x _ { n } } { h } ) - S ( \frac { x - ( n + 2 ) h } { h } ) , } \\ & { \phi _ { n + 1 } ( x ) = S ( \frac { x - x _ { n + 1 } } { h } ) - 4 S ( \frac { x - ( n + 2 ) } { h } , } \end{array}
$$

Step 5 For $i , = 0 , \ldots , n + 1$ do Steps 6-9. (Note: The integrals in Steps 6 and 9 can be evaluated using a numerical integration procedure.)

$$
j = i , i + 1 , \ldots , \operatorname* { m i n } \{ i + 3 , n + 1 \}
$$

$$
U = \operatorname* { m i n } \{ x _ { i + 2 } , 1 \}
$$

$$
\begin{array} { r } { a _ { i j } = \int _ { L } ^ { U } \left[ p ( x ) \phi _ { i } ^ { \prime } ( x ) \phi _ { j } ^ { \prime } ( x ) + q ( x ) \phi _ { i } ( x ) \phi _ { j } ( x ) \right] d x ; } \end{array}
$$

Step 7If $i \geq 4$ then for $j = 0 , \ldots , i - 4 \mathrm { s e t } a _ { i j } = 0 .$

Step 8If $i \leq n - 3$ then for $j = i + 4 , \dots , n + 1$ set $a _ { i j } = 0$ ·

Step 9 Set $\begin{array} { l } { L = \operatorname* { m a x } \{ x _ { i - 2 } , 0 \} ; } \\ { U = \operatorname* { m i n } \{ x _ { i + 2 } , 1 \} ; } \\ { b _ { i } = \int _ { L } ^ { U } f ( x ) \phi _ { i } ( x ) d x . } \end{array}$

Step 10 Solve the linear system $A c = b$ ,where $A = ( a _ { i j } ) , \mathbf { b } = ( b _ { 0 } , \ldots , b _ { n + 1 } ) ^ { t }$ and $\mathbf { c } = ( c _ { 0 } , \dots , c _ { n + 1 } ) ^ { t }$

Step 11 For $i = 0 , \ldots , n + 1$ OUTPUT $( c _ { i } )$

Step 12 STOP.(The procedure is complete.)

Consider the boundary-value problem

$$
- y ^ { \prime \prime } + \pi ^ { 2 } y = 2 \pi ^ { 2 } \sin ( \pi x ) , \quad 0 \leq x \leq 1 , \quad y ( 0 ) = y ( 1 ) = 0 .
$$

In Example 1 we let $h = 0 . 1$ and generated approximations using piecewise-linear basis functions. Table 11.8 lists the results obtained by applying the $B$ -splines as detailed in Algorithm 11.6 with this same choice of nodes. ■

# Table 11.8

<table><tr><td>i</td><td>Ci</td><td>X</td><td>(xi）</td><td>y(xi）</td><td>ly(xi）-(xi）</td></tr><tr><td>0</td><td>0.50964361 × 10-5</td><td>0</td><td>0.00000000</td><td>0.00000000</td><td>0.00000000</td></tr><tr><td>1</td><td>0.20942608</td><td>0.1</td><td>0.30901644</td><td>0.30901699</td><td>0.00000055</td></tr><tr><td>2</td><td>0.39835678</td><td>0.2</td><td>0.58778549</td><td>0.58778525</td><td>0.00000024</td></tr><tr><td>3</td><td>0.54828946</td><td>0.3</td><td>0.80901687</td><td>0.80901699</td><td>0.00000012</td></tr><tr><td>4</td><td>0.64455358</td><td>0.4</td><td>0.95105667</td><td>0.95105652</td><td>0.00000015</td></tr><tr><td>5</td><td>0.67772340</td><td>0.5</td><td>1.00000002</td><td>1.00000000</td><td>0.00000020</td></tr><tr><td>6</td><td>0.64455370</td><td>0.6</td><td>0.95105713</td><td>0.95105652</td><td>0.00000061</td></tr><tr><td>7</td><td>0.54828951</td><td>0.7</td><td>0.80901773</td><td>0.80901699</td><td>0.00000074</td></tr><tr><td>8</td><td>0.39835730</td><td>0.8</td><td>0.58778690</td><td>0.58778525</td><td>0.00000165</td></tr><tr><td>9</td><td>0.20942593</td><td>0.9</td><td>0.30901810</td><td>0.30901699</td><td>0.00000111</td></tr><tr><td>10</td><td>0.74931285 × 10-5</td><td>1.0</td><td>0.00000000</td><td>0.00000000</td><td>0.00000000</td></tr></table>

We recommend that the integrations in Steps 6 and 9 be performed in two steps.First, construct cubic spline interpolatory polynomials for $p , q$ ,and $f$ using the methods presented in Section 3.4. Then approximate the integrands by products of cubic splines or derivatives of cubic splines. The integrands are now piecewise polynomials and can be integrated exactly on each subinterval, and then summed. This leads to accurate approximations of the integrals.

The hypotheses assumed at the beginning of this section are sufficient to guarantee that

$$
\left\{ \int _ { 0 } ^ { 1 } \left| y ( x ) - \phi ( x ) \right| ^ { 2 } d x \right\} ^ { 1 / 2 } = O ( h ^ { 4 } ) , \quad { \mathrm { i f } } \quad 0 \leq x \leq 1 .
$$

For a proof of this result, see [Schul, pp. 107-108].

$B$ -splines can also be defined for unequally-spaced nodes,but the details are more complicated. A presentation of the technique can be found in [Schul, p. 73]. Another commonly used basis is the piecewise cubic Hermite polynomials.For an excellent presentation of this method, again see [Schul, pp. 24ff].

Other methods that receive considerable attention are Galerkin,or “weak form," methods. For the boundary-value problem we have been considering,

$$
- \frac { d } { d x } \left( p ( x ) \frac { d y } { d x } \right) + q ( x ) y = f ( x ) , \quad y ( 0 ) = y ( 1 ) = 0 , \quad 0 \leq x \leq 1 ,
$$

under the assumptions listed at the beginning of this section, the Galerkin and Rayleigh-Ritz methods are both determined by Eq.(11.29). However, this is not the case for an arbitrary boundary-value problem. A treatment of the similarities and differences in the

two methods and a discussion of the wide application of the Galerkin method can be found in [Schul] and in [SF].

Another popular technique for solving boundary-value problems is the method of collocation. This procedure begins by selecting a set of basis functions $\{ \phi _ { 1 } , \ldots , \phi _ { N } \}$ ,a set of numbers $\{ x _ { i } , \ldots , x _ { n } \}$ in [0,1],and requiring that anapproximation

$$
\sum _ { i = 1 } ^ { N } c _ { i } \phi _ { i } ( x )
$$

satisfy the differential equation at each of the numbers $x _ { j }$ ,for $1 \leq j \leq n$ . If, in addition, it is required that $\phi _ { i } ( 0 ) = \phi _ { i } ( 1 ) = 0$ ,for $1 ~ \leq ~ i ~ \leq ~ N$ ,the boundary conditions are automatically satisfied. Much attention in the literature has been given to the choice of the numbers $\{ x _ { j } \}$ and the basis functions $\{ \phi _ { i } \}$ . One popular choice is to let the $\phi _ { i }$ be the basis functions for spline functions relative to a partition of [O,1],and to let the nodes $\{ x _ { j } \}$ be the Gaussian points or roots of certain orthogonal polynomials,transformed to the proper subinterval. A comparison of various collocation methods and finite difference methods is contained in $[ \tt R u ]$ .The conclusion is that the collcation methods using higherdegree splines are competitive with finite-difference techniques using extrapolation. Other references for collocation methods are [DebS] and [LR].

# ExERcisE SEt 11.5

1.Use the Piecewise Linear Algorithm to approximate the solution to the boundary-vaiue problem

$$
y ^ { \prime \prime } + { \frac { \pi ^ { 2 } } { 4 } } y = { \frac { \pi ^ { 2 } } { 1 6 } } \cos { \frac { \pi } { 4 } } x , \quad 0 \leq x \leq 1 , \quad y ( 0 ) = y ( 1 ) = 0
$$

using $x _ { 0 } ~ = ~ 0 , x _ { 1 } ~ = ~ 0 . 3 , x _ { 2 } ~ = ~ 0 . 7 , x _ { 3 } ~ = ~ 1 .$ .Compare your results to the actual solution $\begin{array} { r } { y ( x ) = - \frac { 1 } { 3 } \cos \frac { \pi } { 2 } x - \frac { \sqrt { 2 } } { 6 } } \end{array}$ sin $\begin{array} { r } { { \frac { \pi } { 2 } } x + { \frac { 1 } { 3 } } \cos { \frac { \pi } { 4 } } x } \end{array}$

2.Use the Piecewise Linear Algorithm toapproximate the solution to the boundary-value prob. lem

$$
- { \frac { d } { d x } } ( x y ^ { \prime } ) + 4 y = 4 x ^ { 2 } - 8 x + 1 , \quad 0 \leq x \leq 1 , \quad y ( 0 ) = y ( 1 ) = 0
$$

using $x _ { 0 } ~ = ~ 0 , x _ { 1 } ~ = ~ 0 . 4 , x _ { 2 } ~ = ~ 0 . 8 , x _ { 3 } ~ = ~ 1$ .Compare your results to the actual solution $y ( x ) = x ^ { 2 } - x$

3.Use the Piecewise Linear Algorithm to approximate the solutions to the following boundary. value problems,and compare the results to the actual solution:

a. $- x ^ { 2 } y ^ { \prime \prime } - 2 x y ^ { \prime } + 2 y = - 4 x ^ { 2 } , \quad 0 \leq x \leq 1 , \ y ( 0 ) = y ( 1 ) = 0 ;$ use $h = 0 . 1$ ; actual solution $y ( x ) = x ^ { 2 } - x$   
b. $\begin{array} { r } { - \frac { d } { d x } ( e ^ { x } y ^ { \prime } ) + e ^ { x } y = x + ( 2 - x ) e ^ { x } , \quad 0 \leq x \leq 1 , \ y ( 0 ) = y ( 1 ) = 0 ; \ v } \end{array}$ use $h = 0 . 1$ : actual solution $y ( x ) = ( x - 1 ) ( e ^ { - x } - 1 )$ .   
c. $\begin{array} { r } { - \frac { d } { d x } ( e ^ { - x } y ^ { \prime } ) + e ^ { - x } y = ( x - 1 ) - ( x + 1 ) e ^ { - ( x - 1 ) } , \quad 0 \leq x \leq 1 , \ y ( 0 ) = y ( 1 ) = 0 ; } \end{array}$ use $h = 0 . 0 5$ ; actual solution $y ( x ) = x ( e ^ { x } - e )$   
d. $- ( x + 1 ) y ^ { \prime \prime } - y ^ { \prime } + ( x + 2 ) y = [ 2 - ( x + 1 ) ^ { 2 } ] e \ln { 2 } - 2 e ^ { x }$ ， $0 \leq x \leq 1$ ， $y ( 0 ) = y ( \boldsymbol { \textbf { l } } ) = 0 \mathrm { { ; } }$ use $h = 0 . 0 5$ ; actual solution $y ( x ) = e ^ { x } \ln ( x + 1 ) - ( e \ln 2 ) x$

4. Use the Cubic Spline Algorithm with $n = 3$ to approximate the solution to each of the following boundary-value problems,and compare the results to the actual solutions given in Exercises 1 and 2:

$$
\begin{array} { r } { y ^ { \prime \prime } + \frac { \pi ^ { 2 } } { 4 } y = \frac { \pi ^ { 2 } } { 1 6 } \cos \frac { \pi } { 4 } x , \quad 0 \leq x \leq 1 , \ y ( 0 ) = 0 , \ y ( 1 ) = 0 } \end{array}
$$

$$
\begin{array} { r } { - \frac { d } { d x } ( x y ^ { \prime } ) + 4 y = 4 x ^ { 2 } - 8 x + 1 , \quad 0 \leq x \leq 1 , \ y ( 0 ) = 0 , \ y ( 1 ) = 0 } \end{array}
$$

5.Repeat Exercise 3 using the Cubic Spline Algorithm.

6. Show that the boundary-value problem

$$
- \frac { d } { d x } ( p ( x ) y ^ { \prime } ) + q ( x ) y = f ( x ) , \quad 0 \leq x \leq 1 , \quad y ( 0 ) = \alpha , \quad y ( 1 ) = \beta ,
$$

can be transformed by the change of variable

$$
z = y - \beta x - ( 1 - x ) \alpha
$$

into the form

$$
- \frac { d } { d x } ( p ( x ) z ^ { \prime } ) + q ( x ) z = F ( x ) , \quad 0 \leq x \leq 1 , \quad z ( 0 ) = 0 , \quad z ( 1 ) = 0 .
$$

7. Use Exercise 6 and the Piecewise Linear Algorithm with $n = 9$ to approximate the solution to the boundary-value problem

$$
- y ^ { \prime \prime } + y = x , \quad 0 \leq x \leq 1 , \quad y ( 0 ) = 1 , \quad y ( 1 ) = 1 + e ^ { - 1 } .
$$

8.Repeat Exercise 7 using the Cubic Spline Algorithm.

9. Show that the boundary-value problem

$$
- { \frac { d } { d x } } ( p ( x ) y ^ { \prime } ) + q ( x ) y = f ( x ) , \quad a \leq x \leq b , \quad y ( a ) = \alpha , \quad y ( b ) = \beta ,
$$

can be transformed into the form

$$
- \frac { d } { d w } ( p ( w ) z ^ { \prime } ) + q ( w ) z = F ( w ) , \quad 0 \leq w \leq 1 , \quad z ( 0 ) = 0 , \quad z ( 1 ) = 0 ,
$$

by a method similar to that given in Exercise 6.

10.Show that the piecewise-linear basis functions $\{ \phi _ { i } \} _ { i = 1 } ^ { n }$ are linearly independent.

11．Show that the cubic spline basis functions $\{ \phi _ { i } \} _ { i = 0 } ^ { n + 1 }$ are linearly independent.

12. Show that the matrix given by the piecewise linear basis functions is positive definite.[Hint: Use the definition.]

13.Show that the matrix given by the cubic spline basis functions is positive definite.

# 11.6 Survey of Methods and Software

In this chapter we discussed methods for approximating solutions to boundary-value problems. For the linear boundary-value problem

$$
y ^ { \prime \prime } = p ( x ) y ^ { \prime } + q ( x ) y + r ( x ) , \quad a \leq x \leq b , \quad y ( a ) = \alpha , \quad y ( b ) = \beta ,
$$

we considered both a linear shooting method and a finite-difference method to approximate the solution. The shooting method uses an initial-value technique to solve the problems

$$
y ^ { \prime \prime } = p ( x ) y ^ { \prime } + q ( x ) y + r ( x ) , \quad a \leq x \leq b , \quad y ( a ) = \alpha , \quad y ^ { \prime } ( a ) = 0 ,
$$

and

$$
y ^ { \prime \prime } = p ( x ) y ^ { \prime } + q ( x ) y , \quad a \leq x \leq b , \quad y ( a ) = 0 , \quad y ^ { \prime } ( a ) = 1 .
$$

A weighted average of these solutions produces a solution to the linear boundary-value problem.

In the finite-difference method, we replaced $y ^ { \prime \prime }$ and $\mathbf { y } _ { \mathrm { . } } ^ { \prime }$ with difference approximations and solved a linear system. Although the approximations may not be as accurate as the shooting method, there is less sensitivity to roundoff error. Higher-order difference methods are available,or extrapolation can be used to improve accuracy.

For the nonlinear boundary problem

$$
y ^ { \prime \prime } = f ( x , y , y ^ { \prime } ) , \quad a \leq x \leq b , \quad y ( a ) = \alpha , \quad y ( b ) = \beta ,
$$

we also presented two methods. The nonlinear shooting method requires the solution of the initial-value problem

$$
y ^ { \prime \prime } = f ( x , y , y ^ { \prime } ) , \quad a \leq x \leq b , \quad y ( a ) = \alpha , \quad y ^ { \prime } ( a ) = t ,
$$

for an initial choice of $t$ . We improved the choice by using Newton's method to approximate the solution, $t$ ,to $y ( b , t ) = \beta$ . This method required solving two initial-value problems at each iteration. The accuracy is dependent on the choice of method for solving the initial-value problems.

The finite-difference method for the nonlinear equation requires the replacement of $y ^ { \prime \prime }$ and $y ^ { \prime }$ by difference quotients,which results in a nonlinear system. This system is solved using Newton's method. Higher-order differences or extrapolation can be used to improve accuracy. Finite-difference methods tend to be less sensitive to roundoff error than shooting methods.

The Rayleigh-Ritz-Galerkin method was ilustrated by approximating the solution to the boundary-value problem

$$
- { \frac { d } { d x } } \left( p ( x ) { \frac { d y } { d x } } \right) + q ( x ) y = f ( x ) , \quad 0 \leq x \leq 1 , \quad y ( 0 ) = y ( 1 ) = 0 .
$$

A piecewise-linear approximation or a cubic spline approximation can be obtained.

Most of the material concerning second-order boundary-value problems can be extended to problems with boundary conditions of the form

$$
\alpha _ { 1 } y ( a ) + \beta _ { 1 } y ^ { \prime } ( a ) = \alpha \quad \mathrm { a n d } \quad \alpha _ { 2 } y ( b ) + \beta _ { 2 } y ^ { \prime } ( b ) = \beta ,
$$

where $| \alpha _ { 1 } | + | \beta _ { 1 } | \ne 0$ and $| \alpha _ { 2 } | + | \beta _ { 2 } | \ne 0$ ， but some of the techniques become quite complicated. The reader who is interested in problems of this type is advised to consider a book specializing in boundary-value problems, such as $[ \mathbf { K } , \mathbf { H } ]$

We mention only two of the many methods in the IMSL Library for solving boundaryvalue problems.The subroutine BVPFD is based on finite differences,and BVPMS is based on multiple shooting using IVPRK, a Runge-Kutta-Verner method for initial-value problems.Both methods can be used for systems of parameterized boundary-value problems.

The NAG Library also has a multitude of subroutines for solving boundary-value problems.The subroutine DO2HAF is a shooting method using the Runge-Kutta-Merson initialvalue method in conjunction with Newton's method. The subroutine D02GAF uses the finite-difference method with Newton's method to solve the nonlinear system. The subroutine D02GBF is a linear finite-difference method,and D02JAF is a method based on collocation.

The subroutines MUSL and MUSN in the ODE package contained in the Netlib library solve the linear and nonlinear two-point boundary-value problems,respectively. Both routines are based on multiple shooting methods.

Further information on the general problems involved with the numerical solution to two-point boundary-value problems can be found in Keller [Keller, H] and Bailey, Shampine and Waltman [BSW]. Roberts and Shipman [RS] focuses on the shooting methods for the two-point boundary-value problem, and Pryce $\{ \bf P r \}$ restricts attention to Sturm-Liouville problems. The book by Ascher, Mattheij, and Russell[AMR] has a comprehen-sive presentation of multiple shooting and parallel shooting methods.

CHAPTER

2

# Numerical Solutions to Partial Differential Equations

# ■

Ab body is isotropic if the thermal conductivity at each point in the body is independent of the direction of heat flow through the point. The temperature, $u \equiv u ( x , y , z , t )$ ,in an isotropic body can be found by solving the partial differential equation

$$
\frac { \partial } { \partial x } \left( k \frac { \partial u } { \partial x } \right) + \frac { \partial } { \partial y } \left( k \frac { \partial u } { \partial y } \right) + \frac { \partial } { \partial z } \left( k \frac { \partial u } { \partial z } \right) = c \rho \frac { \partial u } { \partial t } ,
$$

where $k , c ,$ and $\pmb { \rho }$ are functions of $( x , y , z )$ and represent, respectively, the thermal conductivity, specific heat, and density of the body at the point $( x , y , z )$ ：

When $k , c ,$ and $\pmb { \rho }$ are constants, this equation is known as the simple three-dimensional heat equation and is expressed as

$$
\frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } + \frac { \partial ^ { 2 } u } { \partial y ^ { 2 } } + \frac { \partial ^ { 2 } u } { \partial z ^ { 2 } } = \frac { c \rho } { k } \frac { \partial u } { \partial t } .
$$

If the boundary of the body is relatively simple, the solution to this equation can be found using Fourier series. In most situations where $k , c ,$ and $\pmb { \rho }$ are not constant or when the boundary is irregular, the solution to the partial differential equation must be obtained by approximation techniques. An introduction to techniques of this type is presented in this chapter.

The partial differential equation we will consider in Section 12.1 is an elliptic equation known as the Poisson equation:

$$
{ \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } } ( x , y ) + { \frac { \partial ^ { 2 } u } { \partial y ^ { 2 } } } ( x , y ) = f ( x , y ) .
$$

In this equation we assume that $f$ describes the input to the problem on a plane region $R$ with boundary S. Equations of this type arise in the study of various time-independent physical problems such as the steady-state distribution of heat in a plane region,the potential energy of a point in a plane acted on by gravitational forces in the plane, and twodimensional steady-state problems involving incompressible fuids.

Additional constraints must be imposed to obtain a unique solution to the Poisson equation. For example,the study of the steady-state distribution of heat in a plane region requires that $f ( x , y ) \equiv 0$ ,resulting in a simplification to

$$
{ \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } } ( x , y ) + { \frac { \partial ^ { 2 } u } { \partial y ^ { 2 } } } ( x , y ) = 0 ,
$$

which is called Laplace's equation. If the temperature within the region is determined by the temperature distribution on the boundary of the region,the constraints are caled the Dirichlet boundary conditions, given by

$$
u ( x , y ) = g ( x , y ) ,
$$

for all $( x , y )$ on $s$ ,the boundary of the region $R$ . (See Figure 12.1.)

![](images/ccd6ad9e9df936bb2aadf7c394c6115b99388ebdeac05a38726529acb6de7b5a.jpg)  
Figure 12.1

In Section 12.2 we consider the numerical solution to a problem involving a parabolic partial differential equation of the form

$$
{ \frac { \partial u } { \partial t } } ( x , t ) - \alpha ^ { 2 } { \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } } ( x , t ) = 0 .
$$

The physical problem considered here concerns the flow of heat along a rod of length $l$ (see Figure 12.2),which has a uniform temperature within each cross-sectional element. This requires the rod to be perfectly insulated on its lateral surface. The constant $\pmb { \alpha }$ is independent of the position in the rod and is determined by the heat-conductive properties of the material of which the rod is composed.

![](images/9c6f2d67a92c37d5007ee60b6fc673025385638d9dcd50657daf880728a68f6e.jpg)  
Figure 12.2

One of the typical sets of constraints for a heat-flow problem of this type is to specify the initial heat distribution in the rod,

$$
u ( x , 0 ) = f ( x ) ,
$$

and to describe the behavior at the ends of the rod. For example, if the ends are held at constant temperatures $U _ { 1 }$ and $U _ { 2 }$ , the boundary conditions have the form

$$
u ( 0 , t ) = U _ { 1 } \quad \mathrm { a n d } \quad u ( l , t ) = U _ { 2 } ,
$$

and the heat distribution approaches the limiting temperature distribution

$$
\operatorname * { l i m } _ { t  \infty } u ( x , t ) = U _ { 1 } + \frac { U _ { 2 , - } U _ { 1 } } { l } x .
$$

If, instead, the rod is insulated so that no heat flows through the ends,the boundary conditions are

$$
\frac { \partial u } { \partial x } ( 0 , t ) = 0 \quad \mathrm { a n d } \quad \frac { \partial u } { \partial x } ( l , t ) = 0 ,
$$

resulting in a constant temperature in the rod as the limiting case.The parabolic partial differential equation is also of importance in the study of gas diffusion; in fact, it is known in some circles as the diffusion equation.

The problem studied in Section 12.3 is the one-dimensional wave equation and is an example of a hyperbolic partial differential equation. Suppose an elastic string of length $l$ is stretched between two supports at the same horizontal level (see Figure 12.3).

![](images/4a1ae8cd3b498eef1f7a5729be21c2e34670a5aefae9a4aa8a303675a59b173b.jpg)  
Figure 12.3

If the string is set to vibrate in a vertical plane, the vertical displacement $u ( x , t )$ of a point $x$ at time $t$ satisfies the partial differential equation

$$
\alpha ^ { 2 } \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } ( x , t ) = \frac { \partial ^ { 2 } u } { \partial t ^ { 2 } } ( x , t ) , \quad \mathrm { f o r } \ 0 < x < l \quad \mathrm { a n d } \quad 0 < t ,
$$

provided that damping effects are neglected and the amplitude is not too large. To impose constraints on this problem, assume that the initial position and velocity of the string are given by

$$
u ( x , 0 ) = f ( x ) \quad { \mathrm { a n d } } \quad { \frac { \partial u } { \partial t } } ( x , 0 ) = g ( x ) , \quad { \mathrm { f o r ~ } } 0 \leq x \leq l .
$$

If the endpoints are fixed, we also have $u ( 0 , t ) = 0$ and $u ( l , t ) = 0$

Other physical problems involving the hyperbolic partial differential equation occur in the study of vibrating beams with one or both ends clamped and in the transmission of electricity on a long line where there is some leakage of current to the ground.

# 12.1Elliptic Partial Differential Equations

The elliptic partial differential equation we consider is the Poisson equation,

$$
\nabla ^ { 2 } u ( x , y ) \equiv \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } ( x , y ) + \frac { \partial ^ { 2 } u } { \partial y ^ { 2 } } ( x , y ) = f ( x , y )
$$

on $R = \{ ( x , y ) \mid a < x < b , c < y < d \}$ ，with

$$
u ( x , y ) = g ( x , y ) \quad { \mathrm { f o r } } ( x , y ) \in S ,
$$

where $s$ denotes the boundary of $R$ .If $f$ and $\pmb { g }$ are continuous on their domains, then there is a unique solution to this equation.

The method used is an adaptation of the Finite-Difference method for linear boundaryvalue problems,which was discussed in Section 11.3. The first step is to choose integers $\pmb { n }$ and $m$ and define step sizes $h = ( b - a ) / n$ and $k = ( d - c ) / m$ . Partition the interval $[ a , b ]$ into $\pmb { n }$ equal parts of width $h$ and the interval $[ c , d ]$ into $m$ equal parts of width $k$ (see Figure 12.4). Place a grid on the rectangle $R$ by drawing vertical and horizontal lines through the points with coordinates $( x _ { i } , y _ { j } )$ ，where

![](images/b8bbf0aeb20dc9cef142e612ded17e2c55ac0918c591e843bbc5296a6d3673a0.jpg)  
Figure 12.4

$$
x _ { i } = a + i h , \quad { \mathrm { f o r ~ e a c h ~ } } i = 0 , 1 , \dots , n ,
$$

and

$$
y _ { j } = c + j k , \quad { \mathrm { f o r ~ e a c h ~ } } j = 0 , 1 , \ldots , m .
$$

The lines $x = x _ { i }$ and $y = y _ { j }$ are grid lines, and their intersections are the mesh points of the grid. For each mesh point in the interior of the grid, $( x _ { i } , y _ { j } )$ ,for $i = 1 , 2 , \ldots , n - 1$ and $j = 1 , 2 , . . . , m - 1$ , we use the Taylor series in the variable $x$ about $x _ { i }$ to generate the centered-difference formula

$$
\frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } ( x _ { i } , y _ { j } ) = \frac { u ( x _ { i + 1 } , y _ { j } ) - 2 u ( x _ { i } , y _ { j } ) + u ( x _ { i - 1 } , y _ { j } ) } { h ^ { 2 } } - \frac { h ^ { 2 } } { 1 2 } \frac { \partial ^ { 4 } u } { \partial x ^ { 4 } } ( \xi _ { i } , y _ { j } ) ,
$$

where $\xi _ { i } \in ( x _ { i - 1 } , x _ { i + 1 } )$ . We also use the Taylor series in the variable $y$ about $y _ { j }$ to generate the centered-difference formula

$$
\frac { \partial ^ { 2 } u } { \partial y ^ { 2 } } ( x _ { i } , y _ { j } ) = \frac { u ( x _ { i } , y _ { j + 1 } ) - 2 u ( x _ { i } , y _ { j } ) + u ( x _ { i } , y _ { j - 1 } ) } { k ^ { 2 } } - \frac { k ^ { 2 } } { 1 2 } \frac { \partial ^ { 4 } u } { \partial y ^ { 4 } } ( x _ { i } , \eta _ { j } ) ,
$$

where $\eta _ { j } \in ( y _ { j - 1 } , y _ { j + 1 } )$

Using these formulas in Eq. (12.1) allows us to express the Poisson equation at the points $( x _ { i } , y _ { j } )$ as

$$
\begin{array} { l } { \frac { u ( x _ { i + 1 } , y _ { j } ) - 2 u ( x _ { i } , y _ { j } ) + u ( x _ { i - 1 } , y _ { j } ) } { h ^ { 2 } } + \frac { u ( x _ { i } , y _ { j + 1 } ) - 2 u ( x _ { i } , y _ { j } ) + u ( x _ { i } , y _ { j - 1 } ) } { k ^ { 2 } } } \\ { = f ( x _ { i } , y _ { j } ) + \displaystyle \frac { h ^ { 2 } } { 1 2 } \frac { \partial ^ { 4 } u } { \partial x ^ { 4 } } ( \xi _ { i } , y _ { j } ) + \frac { k ^ { 2 } } { 1 2 } \frac { \partial ^ { 4 } u } { \partial y ^ { 4 } } ( x _ { i } , \eta _ { j } ) , } \end{array}
$$

for each $i = 1 , 2 , \ldots , n - 1$ and $j = 1 , 2 , \dots , m - 1$ , and the boundary conditions as

$$
\begin{array} { l l l l } { { u ( x _ { 0 } , y _ { j } ) = g ( x _ { 0 } , y _ { j } ) } } & { { \mathrm { a n d } } } & { { u ( x _ { n } , y _ { j } ) = g ( x _ { n } , y _ { j } ) , } } & { { \mathrm { f o r ~ e a c h ~ } j = 0 , 1 , \ldots , m ; } } \\ { { u ( x _ { i } , y _ { 0 } ) = g ( x _ { i } , y _ { 0 } ) } } & { { \mathrm { a n d } } } & { { u ( x _ { i } , y _ { m } ) = g ( x _ { i } , y _ { m } ) , } } & { { \mathrm { f o r ~ e a c h ~ } i = 1 , 2 , \ldots , n - 1 . } } \end{array}
$$

In difference-equation form, this results in the Finite-Difference method, with local truncation error of order $O ( h ^ { 2 } + k ^ { 2 } )$ ：

$$
2 \biggl [ \left( \frac { h } { k } \right) ^ { 2 } + 1 \biggr ] w _ { i j } - ( w _ { i + 1 , j } + w _ { i - 1 , j } ) - \biggl ( \frac { h } { k } \biggr ) ^ { 2 } ( w _ { i , j + 1 } + w _ { i , j - 1 } ) = - h ^ { 2 } f ( x _ { i } , y _ { j } )
$$

for each $i = 1 , 2 , \ldots , n - 1$ and $j = 1 , 2 , \dots , m - 1$ ,and

$$
\begin{array} { c l l l } { { w _ { 0 j } = g ( x _ { 0 } , y _ { j } ) } } & { { \mathrm { a n d } } } & { { w _ { n j } = g ( x _ { n } , y _ { j } ) , } } & { { \mathrm { f o r ~ e a c h ~ } j = 0 , 1 , \ldots , m ; } } \\ { { w _ { i 0 } = g ( x _ { i } , y _ { 0 } ) } } & { { \mathrm { a n d } } } & { { w _ { i m } = g ( x _ { i } , y _ { m } ) , } } & { { \mathrm { f o r ~ e a c h ~ } i = 1 , 2 , \ldots , n - 1 } } \end{array}
$$

where $w _ { i j }$ approximates $u ( x _ { i } , y _ { j } )$

The typical equation in (12.4) involves approximations to $u ( x , y )$ at the points

$$
( x _ { i - 1 } , y _ { j } ) , \quad ( x _ { i } , y _ { j } ) , \quad ( x _ { i + 1 } , y _ { j } ) , \quad ( x _ { i } , y _ { j - 1 } ) , \quad \mathrm { a n d } \quad ( x _ { i } , y _ { j + 1 } ) .
$$

![](images/cad27fb4b89da543d91bbbe5237709fdee43bc23b538a589bc87461330f80685.jpg)  
Figure 12.5

Reproducing the portion of the grid where these points are located (see Figure 12.5) shows that each equation involves approximations in a star-shaped region about $( x _ { i } , y _ { j } )$

If we use the information from the boundary conditions (12.5) whenever appropriate in the system given by (12.4); that is, at all points $( x _ { i } , y _ { j } )$ adjacent to a boundary mesh point, we have an $( n - 1 ) ( m - 1 ) \times ( n - 1 ) ( m - 1 )$ linear system with the unknowns being the approximations $w _ { i , j }$ to $u ( x _ { i } , y _ { j } )$ at the interior mesh points.

The linear system involving these unknowns is expressed for matrix calculations more efficiently if a relabeling of the interior mesh points is introduced. A recommended labeling of these points (see [Var, p. 210]) is to let

$$
P _ { l } = ( x _ { i } , y _ { j } ) \quad \mathrm { a n d } \quad w _ { l } = w _ { i , j } ,
$$

![](images/291669b7279df4e9e2cdb40609a4bbe5044122fe1496f0e77a97f7f88f64291f.jpg)  
Figure 12.6

where $l = i + ( m - 1 - j ) ( n - 1 )$ , for each $i = 1 , 2 , \ldots , n - 1$ and $j = 1 , 2 , \dots , m - 1$ This labels the mesh points consecutively from left to right and top to bottom.For example, with $n = 4$ and $m = 5$ ,the relabeling results in a grid whose points are shown in Figure 12.6.Labeling the points in this manner ensures that the system needed to determine the $w _ { i , j }$ is a banded matrix with band width at most $2 n - 1$

Consider the problem of determining the steady-state heat distribution in a thin square metal plate with dimensions $0 . 5 \mathrm { m }$ by $0 . 5 ~ \mathrm { \mathfrak { m } }$ .Two adjacent boundaries are held at $0 ^ { \circ } C$ ,and the heat on the other boundaries increases linearly from $0 \%$ at one corner to $1 0 0 ^ { \circ } \mathrm { C }$ where the sides meet. If we place the sides with the zero boundary conditions along the $x$ and $y$ -axes, the problem is expressed as

$$
{ \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } } ( x , y ) + { \frac { \partial ^ { 2 } u } { \partial y ^ { 2 } } } ( x , y ) = 0 ,
$$

for $( x , y )$ in the set $R = \{ ( x , y ) \mid 0 < x < 0 . 5 , 0 < y < 0 . 5 \}$ ， with the boundary conditions

$$
u ( 0 , y ) = 0 , u ( x , 0 ) = 0 , u ( x , 0 . 5 ) = 2 0 0 x , u ( 0 . 5 , y ) = 2 0 0 y .
$$

f $n = m = 4$ ， the problem has the grid given in Figure 12.7,and the difference equation (12.4) is

$$
4 w _ { i , j } - w _ { i + 1 , j } - w _ { i - 1 , j } - w _ { i , j - 1 } - w _ { i , j + 1 } = 0 ,
$$

for each $i = 1 , 2 , 3$ and $j = 1 , 2 , 3$

Expressing this in terms of the relabeled interior grid points $w _ { i } = u ( P _ { i } )$ implies that the equations at the points $P _ { i }$ are:

![](images/0b59da57334ce1b358c0b12cc4ce53f0f93e35a0282e29dfaabc67f594b66a03.jpg)  
Figure 12.7

$$
\begin{array} { r l } & { P _ { 1 } : \qquad 4 u _ { 1 } - w _ { 2 } - w _ { 4 } = w _ { 4 , 3 } + w _ { 1 , 4 } , } \\ & { P _ { 2 } : \qquad 4 w _ { 2 } - w _ { 3 } - w _ { 1 } - w _ { 5 } = w _ { 2 , 4 } , } \\ & { P _ { 3 } : \qquad 4 w _ { 3 } - w _ { 2 } - w _ { 6 } = w _ { 4 , 3 } + w _ { 3 , 4 } , } \\ & { P _ { 4 } : \qquad 4 w _ { 4 } - w _ { 5 } - w _ { 1 } \cdot w _ { 7 } = w _ { 0 , 2 } , } \\ & { P _ { 5 } : \qquad 4 w _ { 5 } - w _ { 6 } - w _ { 4 } - w _ { 2 } - w _ { 8 } = 0 , } \\ & { P _ { 6 } : \qquad 4 w _ { 6 } - w _ { 5 } - w _ { 3 } - w _ { 9 } = w _ { 4 , 2 } , } \\ & { P _ { 7 } : \qquad 4 w _ { 7 } - w _ { 8 } - w _ { 4 } = w _ { 0 , 1 } + w _ { 1 , 0 } , } \\ & { P _ { 8 } : \qquad 4 w _ { 8 } - w _ { 7 } - w _ { 5 } = w _ { 2 , 0 } , } \\ & { P _ { 9 } : \qquad 4 w _ { 8 } - w _ { 1 0 } - w _ { 1 0 } = w _ { 3 , 0 } - w _ { 4 , 1 } , } \\ & { P _ { 8 } : \qquad 4 w _ { 9 } - w _ { 8 } - w _ { 1 0 } , } \end{array}
$$

vhere the right sides of the equations are obtained from the boundary conditions. In fact, the boundary conditions imply that

$$
\begin{array} { r l } & { w _ { 1 , 0 } = w _ { 2 , 0 } = w _ { 3 , 0 } = w _ { 0 , 1 } = w _ { 0 , 2 } = w _ { 0 , 3 } = 0 , } \\ & { w _ { 1 , 4 } = w _ { 4 , 1 } = 2 5 , \quad w _ { 2 , 4 } = w _ { 4 , 2 } = 5 0 , \quad \mathrm { a n d } \quad w _ { 3 , 4 } = w _ { 4 , 3 } = 7 5 . } \end{array}
$$

The linear system associated with this problem has the form

$$
\left[ \begin{array} { r r r r r r r r r } { 4 } & { - 1 } & { 0 } & { - 1 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { - 1 } & { 4 } & { - 1 } & { 0 } & { - 1 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { - 1 } & { 4 } & { 0 } & { 0 } & { - 1 } & { 0 } & { 0 } & { 0 } \\ { - 1 } & { 0 } & { 0 } & { 4 } & { - 1 } & { 0 } & { - 1 } & { 0 } & { 0 } \\ { 0 } & { - 1 } & { 0 } & { - 1 } & { 4 } & { - 1 } & { 0 } & { - 1 } & { 0 } \\ { 0 } & { 0 } & { - 1 } & { 0 } & { - 1 } & { 4 } & { 0 } & { 0 } & { 0 } & { - 1 } \\ { 0 } & { 0 } & { 0 } & { - 1 } & { 0 } & { 0 } & { 4 } & { - 1 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { - 1 } & { 0 } & { - 1 } & { 4 } & { - 1 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { - 1 } & { 0 } & { - 1 } & { 4 } \end{array} \right] \left[ \begin{array} { r } { w _ { 1 } } \\ { w _ { 2 } } \\ { w _ { 3 } } \\ { w _ { 4 } } \\ { w _ { 5 } } \\ { w _ { 6 } } \\ { w _ { 7 } } \\ { w _ { 8 } } \\ { w _ { 8 } } \\ { w _ { 9 } } \end{array} \right] = \left[ \begin{array} { r } { 2 5 } \\ { 5 0 } \\ { 1 5 0 } \\ { 0 } \\ { 0 } \\ { 5 0 } \\ { 0 } \\ { 0 } \\ { 0 } \end{array} \right] .
$$

The values of $w _ { 1 } , w _ { 2 } , \ldots , w _ { 9 }$ , found by applying the Gauss-Seidel method to this matrix,are given in Table 12.1.

# Table 12.1

$$
\frac { i } { w _ { i } } \ | \begin{array} { c } { { 1 } } \\ { { 1 8 . 7 5 } } \end{array} | \begin{array} { c } { { 2 } } \\ { { 3 7 . 5 0 } } \end{array} \ | \begin{array} { c } { { 3 } } \\ { { 5 6 . 2 5 } } \end{array} | \begin{array} { c } { { 4 } } \\ { { 1 2 . 5 0 } } \end{array} | \begin{array} { c } { { 5 } } \\ { { 2 5 . 0 0 } } \end{array} \ | \begin{array} { c } { { 6 } } \\ { { 3 7 . 5 0 } } \end{array} | \begin{array} { c } { { 7 } } \\ { { 6 . 2 5 } } \end{array} | \begin{array} { c } { { 8 } } \\ { { 1 2 . 5 0 } } \end{array} \ | \begin{array} { c } { { 9 } } \\ { { 1 8 . 7 5 } } \end{array} | \begin{array} { c } { { 8 } } \\ { { 1 8 . 7 5 } } \end{array}
$$

These answers are exact, since the true solution, $u ( x , y ) = 4 0 0 x y$ , has

$$
{ \frac { \partial ^ { 4 } u } { \partial x ^ { 4 } } } = { \frac { \partial ^ { 4 } u } { \partial y ^ { 4 } } } \equiv 0 ,
$$

so the truncation error is zero at each step.

The problem we considered in Example 1 has the same mesh size, O.125,on each axis and requires solving only a $9 \times 9$ linear system. This simplifies the situation and does not introduce the computational problems that are present when the system is larger. Algorithm

12.1 uses the Gauss-Seidel iterative method for solving the linear system that is produced and permits unequal mesh sizes on the axes.

# Poisson Equation Finite-Difference

To approximate the solution to the Poisson equation

$$
{ \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } } ( x , y ) + { \frac { \partial ^ { 2 } u } { \partial y ^ { 2 } } } ( x , y ) = f ( x , y ) , \quad a \leq x \leq b , \quad c \leq y \leq d ,
$$

subject to the boundary conditions

$$
u ( x , y ) = g ( x , y ) \quad { \mathrm { i f ~ } } x = a { \mathrm { ~ o r ~ } } x = b \quad { \mathrm { a n d } } \quad c \leq y \leq d
$$

and

$$
u ( x , y ) = g ( x , y ) \quad { \mathrm { i f ~ } } y = c { \mathrm { ~ o r ~ } } y = d \quad { \mathrm { a n d } } \quad a \leq x \leq b \ ;
$$

INPUTendpoints $a , b , c , d$ ; integers $m \geq 3 , n \geq 3$ ; tolerance TOL; maximum number of iterations $N$ ·

OUTPUTapproximations $w _ { i , j }$ to $u ( x _ { i } , y _ { j } )$ for each $i = 1 , \ldots , n - 1$ and for each $j =$ $1 , \ldots , m - 1$ or a message that the maximum number of iterations was exceeded.

Step 1 Set $\begin{array} { l } { h = ( b - a ) / n ; } \\ { k = ( d - c ) / m . } \end{array}$

Step 2 For $i = 1 , \ldots , n - 1$ set $x _ { i } = a + i h$ (Steps 2 and 3 construct mesh points.)

Step 3For $j = 1 , \ldots , m - 1$ set $y _ { j } = c + j k$

Step 4 For $i = 1 , \ldots , n - 1$ for $j = 1 , \ldots , m - 1 \mathrm { ~ s e t ~ } w _ { i , j } = 0 .$

Step 5 Se $\begin{array} { c } { { \mathrm { \bf ~ t } \lambda = h ^ { 2 } / k ^ { 2 } ; } } \\ { { \mu = 2 ( 1 + \lambda ) ; } } \\ { { l = 1 . } } \end{array}$

Step $\pmb { \delta }$ While $l \leq N$ do Steps 7-20. (Steps 7-20 perform Gauss-Seidel iterations.)

$$
\begin{array} { r l } & { \mathsf { e t } z = \left( - h ^ { 2 } f ( x _ { 1 } , y _ { m - 1 } ) + g ( a , y _ { m - 1 } ) + \lambda g ( x _ { 1 } , d ) + \lambda w _ { 1 , m - 2 } + w _ { 2 , m - 1 } \right) / \mu ; } \\ & { \quad N O R M = | z - w _ { 1 , m - 1 } | ; } \\ & { \quad w _ { 1 , m - 1 } = z . } \end{array}
$$

Step 8 Fori=2,...,n -2 s6 if $\begin{array} { r l } &  \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm  \end{array}$ set $w _ { i , m - 1 } = z$

$$
\begin{array} { r l } & { \textsf { e t } z = \big ( - h ^ { 2 } f ( x _ { n - 1 } , y _ { m - 1 } ) + g ( b , y _ { m - 1 } ) + \lambda g ( x _ { n - 1 } , d ) } \\ & { \qquad + w _ { n - 2 , m - 1 } + \lambda w _ { n - 1 , m - 2 } \big ) / \mu ; } \end{array}
$$

if $| w _ { n - 1 , m - 1 } - z | > N O R M$ then set $N O R M = | w _ { n - 1 , m - 1 } - z |$ set $w _ { n - 1 , m - 1 } = z$

Step 10 For $j = m - 2 , \ldots , 2$ do Steps 11,12,and 13.

Step 11 Set $z = \left( - h ^ { 2 } f ( x _ { 1 } , y _ { j } ) + g ( a , y _ { j } ) + \lambda w _ { 1 , j + 1 } + \lambda w _ { 1 , j - 1 } + w _ { 2 , j } \right) / \mu ;$ if $| w _ { 1 , j } - z | > N O R M$ then set $N O R M = | w _ { 1 , j } - z |$ ； set $w _ { 1 , j } = z$

Step 12 $\operatorname { F o r } i = 2 , \dots , n - 2$ set $z = \left( - h ^ { 2 } f ( x _ { i } , y _ { j } ) + w _ { i - 1 , j } + \lambda w _ { i , j + 1 } + w _ { i + 1 , j } + \lambda w _ { i , j - 1 } \right) / \mu ;$ if $| w _ { i , j } - z | > N O R M$ then set $N O R M = | w _ { i , j } - z |$ ； set $w _ { i , j } = z$ ·

Step 13 Se if $\begin{array} { r l } & { \mathfrak { t } z = \big ( - h ^ { 2 } f ( x _ { n - 1 } , y _ { j } ) + g ( b , y _ { j } ) + w _ { n - 2 , j } } \\ & { \qquad + \lambda w _ { n - 1 , j + 1 } + \lambda w _ { n - 1 , j - 1 } \big ) / \mu ; } \\ & { w _ { n - 1 , j } - z | > N O R M \mathrm { t h e n ~ s e t } N O R M = | w _ { n - 1 , j } - z | ; } \end{array}$ set $w _ { n - 1 , j } = z$

Step 14 Set $: z = \left( - h ^ { 2 } f ( x _ { 1 } , y _ { 1 } ) + g ( a , y _ { 1 } ) + \lambda g ( x _ { 1 } , c ) + \lambda w _ { 1 , 2 } + w _ { 2 , 1 } \right) / \mu ;$ if $\lvert w _ { 1 , 1 } - z \rvert > N O R M$ then set $N O R M = | w _ { 1 , 1 } - z |$ ； set $w _ { 1 , 1 } = z$

Step 15For $i = 2 , \ldots , n - 2$ set $\begin{array} { r l } & { z = \left( - h ^ { 2 } f ( x _ { i } , y _ { 1 } ) + \lambda g ( x _ { i } , c ) + w _ { i - 1 , 1 } + \lambda w _ { i , 2 } + w _ { i + 1 , 1 } \right) / \mu ; } \\ & { w _ { i , 1 } - z | > N O R M \mathrm { t h e n ~ s e t } N O R M = | w _ { i , 1 } - z | ; } \end{array}$ if set $w _ { i , 1 } = z$

Step 16 Se if $\begin{array} { r l } & { \mathrm { \bf ~ t } z = \left( - h ^ { 2 } f ( x _ { n - 1 } , y _ { 1 } ) + g ( b , y _ { 1 } ) + \lambda g ( x _ { n - 1 } , c ) + w _ { n - 2 , 1 } + \lambda w _ { n - 1 , 2 } \right) / \mu ; } \\ & { | w _ { n - 1 , 1 } - z | > N O R M \mathrm { t h e n ~ s e t } N O R M = | w _ { n - 1 , 1 } - z | ; } \end{array}$ set $w _ { n - 1 , 1 } = z$

Step 17If $N O R M \leq T O L$ then do Steps 18 and 19.

Step 18 For $i = 1 , \ldots , n - 1$ for $j = 1 , \ldots , m - 1$ OUTPUT $( x _ { i } , y _ { j } , w _ { i , j } )$

Step 19 STOP. (The procedure was successful.)

Step 20 Set $l = l + 1$

Step 21 OUTPUT('Maximum number of iterations exceeded'); (The procedure was unsuccessful.) STOP.

Although the Gauss-Seidel iterative procedure is incorporated into Algorithm 12.1 for simplicity, it is advisable to use a direct technique such as Gaussian elimination when the system is small,on the order of 1OO or lesssince the positive definiteness ensures stability with respect to roundoff errors. In particular, a generalization of the Crout Factorization Algorithm 6.7 (see [Var, p. 221]),is effcient for solving this system since the matrix is in symmetric-block tridiagonal form

$$
\begin{array} { r } { \left[ \begin{array} { l l l l l l } { A _ { 1 } } & { C _ { 1 } } & { 0 { : } \cdots } & { \cdots } & { \cdots } & { 0 } \\ { C _ { 1 } } & { A _ { 2 } } & { C _ { 2 } } & & & { \vdots } \\ { 0 . } & { C _ { 2 } } & { . . . } & { . . } & { . } & { \vdots } \\ { \vdots } & { . . . } & { . . . } & { . . . } & { . . } & { . } \\ { \vdots } & { . . . } & { . . . } & { . . . } & { . . } & { . } \\ { \vdots } & { . . . } & { . . . } & { . . . } & { . . } & { . } \\ { \vdots } & { . . . } & { . . . } & { . . . } & { . } & { . } \\ { \dot { 0 } } & { . . . . } & { . . . } & { . . . } & { . } & { . } \end{array} \right] , } \end{array}
$$

with square blocks of size $( n - 1 ) \times ( n - 1 )$

For large systems,an iterative method should be used-specifically, the SOR method discussed in Algorithm 7.3. The choice of $\omega$ that is optimal in this situation comes from the fact that when $A$ is decomposed into its diagonal $D$ and upper- and lower-triangular parts $U$ and $L$ ，

$$
A = D - L - U ,
$$

and $B$ is the matrix for the Jacobi method,

$$
B = D ^ { - 1 } ( L + U ) ,
$$

then the spectral radius of $B$ is (see [Var])

$$
\rho ( B ) = \frac { 1 } { 2 } \biggl [ \cos { \left( \frac { \pi } { m } \right) } + \cos { \left( \frac { \pi } { n } \right) } \biggr ] .
$$

The value of $\omega$ to be used is, consequently,

$$
\omega = \frac { 2 } { 1 + \sqrt { 1 - [ \rho ( B ) ] ^ { 2 } } } = \frac { 4 } { 2 + \sqrt { 4 - \left[ \cos \left( \frac { \pi } { m } \right) + \cos \left( \frac { \pi } { n } \right) \right] ^ { 2 } } } .
$$

A block technique can be incorporated into the algorithm for faster convergence of the SOR procedure.For a presentation of this technique, see [Var, pp. 219-223].

# EXAMPLE 2 Consider Poisson's equation

$$
\frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } ( x , y ) + \frac { \partial ^ { 2 } u } { \partial y ^ { 2 } } ( x , y ) = x e ^ { y } , \quad 0 < x < 2 , \quad 0 < y < 1 ,
$$

with the boundary conditions

$$
\begin{array} { r l } & { u ( 0 , y ) = 0 , \quad u ( 2 , y ) = 2 e ^ { y } , \quad 0 \leq y \leq 1 , } \\ & { u ( x , 0 ) = x , \quad u ( x , 1 ) = e x , \quad 0 \leq x \leq 2 . } \end{array}
$$

We will use Algorithm 12.1 to approximate the exact solution $u ( x , y ) = x e ^ { y }$ with $n = 6$ and $m = 5$ .The stopping criterion for the Gauss-Seidel method in Step 17requires that

$$
\left| w _ { i j } ^ { ( l ) } - w _ { i j } ^ { ( l - 1 ) } \right| \leq 1 0 ^ { - 1 0 } ,
$$

for each $i = 1 , \dots , 5$ and $j = 1 , \ldots , 4$ . So the solution to the diference equation was accurately obtained, and the procedure stopped at $l = 6 1$ . The results, along with the correct values, are presented in Table 12.2.

Table 12.2   

<table><tr><td>i</td><td>j</td><td>X</td><td>yi</td><td>(61) wj</td><td>u(xi,yj)</td><td>u(xi，yj）- (61) Wij</td></tr><tr><td>1</td><td>1</td><td>0.3333</td><td>0.2000</td><td>0.40726</td><td>0.40713</td><td>1.30 × 10-4</td></tr><tr><td>1</td><td>2</td><td>0.3333</td><td>0.4000</td><td>0.49748</td><td>0.49727</td><td>2.08 × 10-4</td></tr><tr><td>1</td><td>3</td><td>0.3333</td><td>0.6000</td><td>0.60760</td><td>0.60737</td><td>2.23×10-4</td></tr><tr><td>1</td><td>4</td><td>0.3333</td><td>0.8000</td><td>0.74201</td><td>0.74185</td><td>1.60 × 10-4</td></tr><tr><td>2</td><td>1</td><td>0.6667</td><td>0.2000</td><td>0.81452</td><td>0.81427</td><td>2.55 ×10-4</td></tr><tr><td>2</td><td>2</td><td>0.6667</td><td>0.4000</td><td>0.99496</td><td>0.99455</td><td>4.08 × 10-4</td></tr><tr><td>2</td><td>3</td><td>0.6667</td><td>0.6000</td><td>1.2152</td><td>1.2147</td><td>4.37 ×10-4</td></tr><tr><td>2</td><td>4</td><td>0.6667</td><td>0.8000</td><td>1.4840</td><td>1.4837</td><td>3.15×10-4</td></tr><tr><td>3</td><td>1</td><td>1.0000</td><td>0.2000</td><td>1.2218</td><td>1.2214</td><td>3.64 × 10-4</td></tr><tr><td>3</td><td>2</td><td>1.0000</td><td>0.4000</td><td>1.4924</td><td>1.4918</td><td>5.80 ×10-4</td></tr><tr><td>3</td><td>3</td><td>1.0000</td><td>0.6000</td><td>1.8227</td><td>1.8221</td><td>6.24 × 10-4</td></tr><tr><td>3</td><td>4</td><td>1.0000</td><td>0.8000</td><td>2.2260</td><td>2.2255</td><td>4.51 × 10-4</td></tr><tr><td>4</td><td>1</td><td>1.3333</td><td>0.2000</td><td>1.6290</td><td>1.6285</td><td>4.27 × 10-4</td></tr><tr><td>4</td><td>2</td><td>1.3333</td><td>0.4000</td><td>1.9898</td><td>1.9891</td><td>6.79 × 10-4</td></tr><tr><td>4</td><td>3</td><td>1.3333</td><td>0.6000</td><td>2.4302</td><td>2.4295</td><td>7.35 × 10-4</td></tr><tr><td>4</td><td>4</td><td>1.3333</td><td>0.8000</td><td>2.9679</td><td>2.9674</td><td>5.40 ×10-4</td></tr><tr><td>5</td><td>1</td><td>1.6667</td><td>0.2000</td><td>2.0360</td><td>2.0357</td><td>3.71 ×10-4</td></tr><tr><td>5</td><td>2</td><td>1.6667</td><td>0.4000</td><td>2.4870</td><td>2.4864</td><td>5.84 ×10-4</td></tr><tr><td>5</td><td>3</td><td>1.6667</td><td>0.6000</td><td>3.0375</td><td>3.0369</td><td>6.41 × 10-4</td></tr><tr><td>5</td><td>4</td><td>1.6667</td><td>0.8000</td><td>3.7097</td><td>3.7092</td><td>4.89 ×10-4</td></tr></table>

1.Use Algorithm 12.1 to approximate the solution to the elliptic partial differential equation

$$
\frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } + \frac { \partial ^ { 2 } u } { \partial y ^ { 2 } } = 4 , \qquad 0 < x < 1 , \quad 0 < y < 2 ;
$$

$$
\begin{array} { l l } { { u ( x , 0 ) = x ^ { 2 } , } } & { { u ( x , 2 ) = ( x - 2 ) ^ { 2 } , \quad 0 \leq x \leq 1 ; } } \\ { { } } & { { } } \\ { { u ( 0 , y ) = y ^ { 2 } , } } & { { u ( 1 , y ) = ( y - 1 ) ^ { 2 } , \quad 0 \leq y \leq 2 . } } \end{array}
$$

Use $\begin{array} { r } { h = k = \frac { 1 } { 2 } } \end{array}$ , and compare the results to the actual solution $u ( x , y ) = ( x - y ) ^ { 2 }$ ·

2.Use Algorithm 12.1 to approximate the solution to the elliptic partial differential equation

$$
\frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } + \frac { \partial ^ { 2 } u } { \partial y ^ { 2 } } = 0 , \qquad 1 < x < 2 , \quad 0 < y < 1 ;
$$

$$
\begin{array} { r l r } & { u ( x , 0 ) = 2 \ln x , \quad } & { u ( x , 1 ) = \ln ( x ^ { 2 } + 1 ) , \quad 1 \leq x \leq 2 ; } \\ & { u ( 1 , y ) = \ln ( y ^ { 2 } + 1 ) , \quad } & { u ( 2 , y ) = \ln ( y ^ { 2 } + 4 ) , \quad 0 \leq y \leq 1 . } \end{array}
$$

Use $\begin{array} { r } { h = k = \frac { 1 } { 3 } } \end{array}$ ,and compare the results to the actual solution $u ( x , y ) = \ln ( x ^ { 2 } + y ^ { 2 } )$ 、

3.Approximate the solutions to the following elliptic partial differential equations,using Algorithm 12.1:

$$
\begin{array} { l l l } { \displaystyle { \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } + \frac { \partial ^ { 2 } u } { \partial y ^ { 2 } } = 0 , \quad } } & { 0 < x < 1 , } & { 0 < y < 1 ; } \\ { \displaystyle { \vphantom { \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } + \frac { \partial ^ { 2 } u } { \partial y ^ { 2 } } = 0 , } } } & { } & { } \\ { \displaystyle { u ( x , 0 ) = 0 , \quad u ( x , 1 ) = x , \quad } } & { 0 \leq x \leq 1 ; } \\ { \displaystyle { u ( 0 , y ) = 0 , \quad u ( 1 , y ) = y , \quad } } & { 0 \leq y \leq 1 . } \end{array}
$$

Use $h = k = 0 . 2$ ,and compare the results to the actual solution $u ( x , y ) = x y$

$$
{ \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } } + { \frac { \partial ^ { 2 } u } { \partial y ^ { 2 } } } = - ( \cos { ( x + y ) } + \cos { ( x - y ) } ) , \qquad 0 < x < \pi , \quad 0 < y < \frac { \pi } { 2 } ;
$$

$$
\begin{array} { r l r } & { u ( 0 , y ) = \cos y , \quad u ( \pi , y ) = - \cos y , } & { 0 \leq y \leq \displaystyle \frac { \pi } { 2 } , \medskip } \\ & { u ( x , 0 ) = \cos x , \quad u \left( x , \displaystyle \frac { \pi } { 2 } \right) = 0 , } & { 0 \leq x \leq \pi . } \end{array}
$$

Use $h = \pi / 5$ and $k = \pi / 1 0$ , and compare the results to the actual solution $u ( x , y ) =$ cos $x$ cos y.

$$
\begin{array} { c c } { { \displaystyle { \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } + \frac { \partial ^ { 2 } u } { \partial y ^ { 2 } } = ( x ^ { 2 } + y ^ { 2 } ) e ^ { x y } , } } } & { { ~ 0 < x < 2 , ~ 0 < y < 1 ; } } \\ { { } } & { { } } \\ { { u ( 0 , y ) = 1 , } } & { { u ( 2 , y ) = e ^ { 2 y } , } } \\ { { } } & { { } } \\ { { u ( x , 0 ) = 1 , } } & { { u ( x , 1 ) = e ^ { x } , } } \end{array} \quad \begin{array} { c c } { { 0 \leq y \leq 1 ; } } \\ { { 0 \leq x \leq 2 . } } \end{array}
$$

Use $h = 0 . 2$ and $k = 0 . 1$ , and compare the results to the actual solution $u ( x , y ) = e ^ { x y }$

d. + X X 1<𝑥<2，1<y<2;

$$
\begin{array} { r l r l r l } & { u ( x , 1 ) = x \ln x , } & { u ( x , 2 ) = x \ln ( 4 x ^ { 2 } ) , } & & { 1 \leq x \leq 2 ; } \\ & { u ( 1 , y ) = y \ln y , } & { u ( 2 , y ) = 2 y \ln ( 2 y ) , } & & { 1 \leq y \leq 2 . } \end{array}
$$

Use $h = k = 0 . 1$ ,and compare the results to the actual solution $u ( x , y ) = x y \ln x y$

4.Repeat Exercise 3(a) using extrapolation with $h _ { 0 } = 0 . 2 , h _ { 1 } = h _ { 0 } / 2$ ,and $h _ { 2 } = h _ { 0 } / 4$

5. Construct an algorithm similar to Algorithm 12.1, except use the SOR method with optimal $\omega$ instead of the Gauss-Seidel method for solving the linear system.

6.Repeat Exercise 3 using the algorithm constructed in Exercise 5.

7.A coaxial cable is made of a O.1-in.-square inner conductor and a 0.5-in.-square outer conductor.The potential at a point in the cross section of the cable is described by Laplace's equation. Suppose the inner conductor is kept at O volts and the outer conductor is kept at 11O volts. Find the potential between the two conductors by placing a grid with horizontal mesh spacing $h = 0 . 1$ in. and vertical mesh spacing $k = 0 . 1$ in. on the region

$$
D = \{ ( x , y ) \mid 0 \leq x , y \leq 0 . 5 \} .
$$

Approximate the solution to Laplace's equation at each grid point, and use the two sets of boundary conditions to derive a linear system to be solved by the Gauss-Seidel method.

8.A 6-cm by 5-cm rectangular silver plate has heat being uniformly generated at each point at the rate $q = 1 . 5 \mathrm { c a l } / \mathrm { c m } ^ { 3 } \cdot \varsigma$ .Let $x$ represent the distance along the edge of the plate of length 6 cm and $y$ be the distance along the edge of the plate of length $5 \mathtt { c m }$ . Suppose the temperature $\pmb { u }$ along the edges is kept at the following temperatures:

$$
\begin{array} { r l } & { u ( x , 0 ) = x ( 6 - x ) , \ u ( x , 5 ) = 0 , \quad 0 \leq x \leq 6 , } \\ & { } \\ & { u ( 0 , y ) = y ( 5 - y ) , \ u ( 6 , y ) = 0 , \quad 0 \leq y \leq 5 , } \end{array}
$$

where the origin lies at a corner of the plate with coordinates $( \mathbf { 0 } , \mathbf { 0 } )$ and the edges lie along the positive $x \cdot$ and $\boldsymbol { y }$ -axes. The steady-state temperature $\pmb { u } = \pmb { u } ( \pmb { x } , \pmb { y } )$ satisfies Poisson's equation:

$$
\frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } ( x , y ) + \frac { \partial ^ { 2 } u } { \partial y ^ { 2 } } ( x , y ) = - \frac { q } { K } , \quad 0 < x < 6 , 0 < y < 5 ,
$$

where $\pmb { K }$ , the thermal conductivity, is 1.04 cal/cm·deg·s. Approximate the temperature $u ( x , y )$ using Algorithm 12.1 with $h = 0 . 4$ and $\begin{array} { r } { \pmb { k } = \frac { 1 } { 3 } } \end{array}$

# 12.2 Parabolic Partial Differential Equations

The parabolic partial differential equation we study is the heat, or diffusion, equation

$$
\frac { \partial u } { \partial t } ( x , t ) = \alpha ^ { 2 } \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } ( x , t ) , \quad 0 < x < l , \quad t > 0 ,
$$

subject to the conditions

$$
u ( 0 , t ) = u ( l , t ) = 0 , \quad t > 0 ,
$$

and

$$
u ( x , 0 ) = f ( x ) , \quad 0 \leq x \leq l .
$$

The approach we use to approximate the solution to this problem involves finite differences and is similar to the method used in Section 12.1.

First select an integer $m > 0$ and define $h = l / m$ . Then select a time-step size $k$ . The grid points for this situation are $( x _ { i } , t _ { j } )$ ,where $x _ { i } = i h$ ,for $i = 0 , 1 , \ldots , m$ ,and $t _ { j } = j k$ ， for $j = 0 , 1 , \ldots$

We obtain the difference method using the Taylor series in $t$ to form the difference quotient

$$
\frac { \partial u } { \partial t } ( x _ { i } , t _ { j } ) = \frac { u ( x _ { i } , t _ { j } + k ) - u ( x _ { i } , t _ { j } ) } { k } - \frac { k } { 2 } \frac { \partial ^ { 2 } u } { \partial t ^ { 2 } } ( x _ { i } , \mu _ { j } ) ,
$$

for some $\mu _ { j } \in ( t _ { j } , t _ { j + 1 } )$ , and the Taylor series in $x$ to form the difference quotient

$$
\frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } ( x _ { i } , t _ { j } ) = \frac { u ( x _ { i } + h , t _ { j } ) - 2 u ( x _ { i } , t _ { j } ) + u ( x _ { i } - h , t _ { j } ) } { h ^ { 2 } } - \frac { h ^ { 2 } } { 1 2 } \frac { \partial ^ { 4 } u } { \partial x ^ { 4 } } ( \xi _ { i } , t _ { j } ) ,
$$

where $\xi _ { i } \in ( x _ { i - 1 } , x _ { i + 1 } )$

The parabolic partial differential equation (12.6) implies that at the interior gridpoint $( x _ { i } , t _ { j } )$ ,for each $i = 1 , 2 , \ldots , m - 1$ and $j = 1 , 2 , \dots ,$ we have

$$
\frac { \partial u } { \partial t } ( x _ { i } , t _ { j } ) - \alpha ^ { 2 } \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } ( x _ { i } , t _ { j } ) = 0 ,
$$

so the diference method using the difference quotients (12.7) and (12.8) is

$$
{ \frac { \ l } { \ l } } \quad \quad { \frac { w _ { i , j + 1 } - w _ { i j } } { k } } - \alpha ^ { 2 } { \frac { w _ { i + 1 , j } - 2 w _ { i j } + w _ { i - 1 , j } } { h ^ { 2 } } } = 0 ,
$$

where $w _ { i j }$ approximates $u ( x _ { i } , t _ { j } )$

The local truncation error for this difference equation is

$$
\tau _ { i j } = \frac { k } { 2 } \frac { \partial ^ { 2 } u } { \partial t ^ { 2 } } ( x _ { i } , \mu _ { j } ) - \alpha ^ { 2 } \frac { h ^ { 2 } } { 1 2 } \frac { \partial ^ { 4 } u } { \partial x ^ { 4 } } ( \xi _ { i } , t _ { j } ) .
$$

Solving Eq. (12.9) for $w _ { i , j + 1 }$ gives

$$
w _ { i , j + 1 } = \bigg ( 1 - \frac { 2 \alpha ^ { 2 } k } { h ^ { 2 } } \bigg ) w _ { i j } + \alpha ^ { 2 } \frac { k } { h ^ { 2 } } ( w _ { i + 1 , j } + w _ { i - 1 , j } ) ,
$$

for each $i = 1 , 2 , \dots , m - 1$ and $j = 1 , 2$ ,.... Since the initial condition $u ( x , 0 ) = f ( x ) .$ for each $0 \leq x \leq l$ , implies that $w _ { i , 0 } = f ( x _ { i } )$ ,for each $i = 0 , 1 , \ldots , m$ , these values can be used in Eq. (12.11) to find the value of $w _ { i , 1 }$ , for each $i = 1 , 2 , \ldots , m - 1$ . The additional conditions $u ( 0 , t ) = 0$ and $u ( l , t ) = 0$ imply that $w _ { 0 , 1 } = w _ { m , 1 } = 0$ ， so all the entries of the form $w _ { i , 1 }$ can be determined. If the procedure is reapplied once all the approximations $w _ { i , 1 }$ are known, the values of $w _ { i , 2 } , w _ { i , 3 } , \ldots .$ ,can be obtained in a similar manner.

The explicit nature of the diference method implies that the $( m - 1 ) \times ( m - 1 )$ matrix associated with this system can be written in the tridiagonal form

$$
A = \left[ \begin{array} { l } { ( 1 - 2 \lambda ) \qquad \lambda \qquad 0 \div \dots \dots \dots \dots } \\ { \lambda \cdot \underbrace { \quad ( 1 - 2 \lambda ) \quad \lambda \cdot \dots \dots } _ { \ddots \dots \dots \dots } \cdot \underbrace { \quad \cdot } _ { \ddots \dots \dots \dots } } \\ { \qquad 0 \cdot \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots } \\ { \vdots \qquad \ddots \dots \dots \dots \dots \dots \dots \dots \dots \dots } \\ { \vdots \qquad \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots } \\ { \qquad 0 \cdot \dots \dots \dots \dots \dots \dots \dots \dots \dots \enspace ( 1 - 2 \lambda ) } \end{array} \right] ,
$$

where $\lambda = \alpha ^ { 2 } ( k / h ^ { 2 } )$ . If we let

$$
\mathbf { w } ^ { ( 0 ) } = ( f ( x _ { 1 } ) , f ( x _ { 2 } ) , \ldots , f ( x _ { m - 1 } ) ) ^ { t }
$$

and

$$
\mathbf w ^ { ( j ) } = ( w _ { 1 j } , w _ { 2 j } , \ldots , w _ { m - 1 , j } ) ^ { t } , \quad \mathrm { f o r } \operatorname { e a c h } j = 1 , 2 , \ldots ,
$$

then the approximate solution is given by

$$
\mathbf { w } ^ { ( j ) } = A \mathbf { w } ^ { ( j - 1 ) } , \quad \mathrm { f o r } \operatorname { e a c h } j = 1 , 2 , \ldots ,
$$

s0 $\mathbf { w } ^ { ( j ) }$ is obtained from ${ \bf w } ^ { ( j - 1 ) }$ by a simple matrix multiplication. This is known as the Forward-Diffrence method. If the solution to the partial differential equation has four continuous partial derivatives in $x$ and two in $t$ ,then Eq.(12.10) implies that the method is of order $O ( k + h ^ { 2 } )$

# EXAMPLE 1

Consider the heat equation

$$
\frac { \partial u } { \partial t } ( x , t ) - \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } ( x , t ) = 0 , \quad 0 < x < 1 , \quad 0 \leq t ,
$$

with boundary conditions

$$
u ( 0 , t ) = u ( 1 , t ) = 0 , \quad 0 < t ,
$$

and initial conditions

$$
u ( x , 0 ) = \sin ( \pi x ) , \quad 0 \leq x \leq 1 .
$$

The solution to this problem is

$$
u ( x , t ) = e ^ { - \pi ^ { 2 } t } \sin ( \pi x ) .
$$

The solution at $t = 0 . 5$ will be approximated using the Forward-Difference method, first with $h = 0 . 1$ ， $k = 0 . 0 0 0 5$ ,and $\lambda = 0 . 0 5$ ,and then with $h = 0 . 1 , k = 0 . 0 1$ ,and $\lambda = 1$ The results are presented in Table 12.3. ■

Table 12.3   

<table><tr><td></td><td>u(xi,0.5)</td><td>Wi,1000 k = 0.0005</td><td>lu(xi,0.5)- Wi.1000l</td><td>Wi,50 k=0.01</td><td>lu(xi,0.5)- Wi.50l</td><td></td></tr><tr><td>Xi 0.0</td><td>0</td><td>0</td><td></td><td>0</td><td></td><td></td></tr><tr><td>0.1</td><td>0.00222241</td><td>0.00228652</td><td>6.411 × 10-5</td><td>8.19876 ×107</td><td>8.199×107</td><td></td></tr><tr><td>0.2</td><td>0.00422728</td><td>0.00434922</td><td>1.219 × 10-4</td><td>-1.55719 × 108</td><td>1.557 × 108</td><td></td></tr><tr><td>0.3</td><td>0.00581836</td><td>0.00598619</td><td>1.678 × 10-4</td><td>2.13833×108</td><td>2.138×108</td><td></td></tr><tr><td>0.4</td><td>0.00683989</td><td>0.00703719</td><td>1.973 × 10-4</td><td>-2.50642 × 108</td><td>2.506 ×108</td><td></td></tr><tr><td>0.5</td><td>0.00719188</td><td>0.00739934</td><td>2.075×10-4</td><td>2.62685×108</td><td>2.627 ×108</td><td></td></tr><tr><td>0.6</td><td>0.00683989</td><td>0.00703719</td><td>1.973 × 10-4</td><td>-2.49015 × 108</td><td>2.490×108</td><td></td></tr><tr><td>0.7</td><td>0.00581836</td><td>0.00598619</td><td>1.678 × 10-4</td><td>2.11200×108</td><td>2.112 ×108</td><td></td></tr><tr><td>0.8</td><td>0.00422728</td><td>0.00434922</td><td>1.219 × 10-4</td><td>-1.53086 × 108</td><td>1.531 × 108</td><td></td></tr><tr><td>0.9</td><td>0.00222241</td><td>0.00228652</td><td>6.511 ×10-5</td><td>8.03604×107</td><td></td><td>8.036×107</td></tr><tr><td>1.0</td><td>0</td><td>0</td><td></td><td>0</td><td></td><td></td></tr></table>

A truncation error of order $O ( k + h ^ { 2 } )$ is expected in Example 1. Although this is obtained with $h = 0 . 1$ and $k = 0 . 0 0 0 5$ , it certainly is not with $h = 0 . 1$ and $k = 0 . 0 1$ . To explain the difficulty, we must look at the stability of the Forward-Difference method.

If an error $\mathbf { e } ^ { ( 0 ) } = \left( e _ { 1 } ^ { ( 0 ) } , e _ { 2 } ^ { ( 0 ) } , \ldots , e _ { m - 1 } ^ { ( 0 ) } \right) ^ { t }$ is made inrepresenting the initial data

$$
\mathbf { w } ^ { ( 0 ) } = \left( f ( x _ { 1 } ) , f ( x _ { 2 } ) , \ldots , f ( x _ { m - 1 } ) \right) ^ { t }
$$

(or in any particular step,the choice of the initial step is simply for convenience),an error of $A e ^ { ( 0 ) }$ propagates in $\mathbf { w } ^ { ( \mathrm { I } ) }$ ,since

$$
\mathbf { w } ^ { ( 1 ) } = A \big ( \mathbf { w } ^ { ( 0 ) } + \mathbf { e } ^ { ( 0 ) } \big ) = A \mathbf { w } ^ { ( 0 ) } + A \mathbf { e } ^ { ( 0 ) } .
$$

This process continues.At the nth time step, the error in $\mathbf { w } ^ { ( n ) }$ due to $\mathbf { e } ^ { ( 0 ) }$ is $A ^ { n } \mathbf { e } ^ { ( 0 ) }$ .The method is consequently stable precisely when these errors do not grow as $n$ increases. But

this is true if and only iffor any initial error $\mathbf { e } ^ { ( 0 ) }$ ， we have $\left\| A ^ { n } \mathbf { e } ^ { ( 0 ) } \right\| \leq \left\| \mathbf { e } ^ { ( 0 ) } \right\|$ for all $n$ Hence, we must have $| | A ^ { n } | | \leq 1$ ,a condition that, by Theorem 7.15,requires that $\rho ( A ^ { n } ) =$ $( \rho ( A ) ) ^ { n } \leq 1$ . The Forward-Difference method is therefore stable only if $\rho ( A ) \leq 1$

The eigenvalues of $A$ can be shown (see Exercise 7) to be

$$
\mu _ { i } = 1 - 4 \lambda \bigg ( \sin \bigg ( \frac { i \pi } { 2 m } \bigg ) \bigg ) ^ { 2 } , \quad \mathrm { f o r } \operatorname { e a c h } i = 1 , 2 , \ldots , m - 1 .
$$

The condition for stability consequently reduces to determining whether

$$
\rho ( A ) = \operatorname* { m a x } _ { 1 \leq i \leq m - 1 } \left. 1 - 4 \lambda \left( \sin \left( \frac { i \pi } { 2 m } \right) \right) ^ { 2 } \right. \leq 1 ,
$$

which simplifies to

$$
0 \leq \lambda \bigg ( \sin \bigg ( \frac { i \pi } { 2 m } \bigg ) \bigg ) ^ { 2 } \leq \frac { 1 } { 2 } , \quad \mathrm { f o r e a c h } i = 1 , 2 , \ldots , m - 1 .
$$

Since stability requires that this inequality condition hold as $h  0$ , or, equivalently, as $m  \infty$ , the fact that

$$
\operatorname* { l i m } _ { m \to \infty } \left[ \sin \left( { \frac { ( m - 1 ) \pi } { 2 m } } \right) \right] ^ { 2 } = 1
$$

means that stability will occur only if $0 \leq \lambda \leq \frac { 1 } { 2 }$ . Since $\lambda = \alpha ^ { 2 } ( k / h ^ { 2 } )$ , this inequality requires that $h$ and $k$ be chosen so that

$$
\alpha ^ { 2 } \frac { k } { h ^ { 2 } } \leq \frac { 1 } { 2 } .
$$

In Example 1 we have $\alpha = 1$ , so this condition is satisfied when $h = 0 . 1$ and $k = 0 . 0 0 0 5$ But when $k$ was increased to O.01 with no corresponding increase in $h$ , the ratio was

$$
\frac { 0 . 0 1 } { ( 0 . 1 ) ^ { 2 } } = 1 > \frac { 1 } { 2 } ,
$$

and stability problems became apparent.

Consistent with the terminology of Chapter 5,we call the Forward-Difference method conditionally stable and remark that the method converges to the solution of Eq. (12.6) with rate of convergence $O ( k + h ^ { 2 } )$ , provided

$$
\alpha ^ { 2 } \frac { k } { h ^ { 2 } } \leq \frac { 1 } { 2 }
$$

and the required continuity conditions on the solution are met. (For a detailed proof of this fact, see [IK, pp. 502-505].)

To obtain a method that is unconditionally stable, we consider an implicit-difference method that results from using the backward-difference quotient for $( { \partial u } / { \partial t } ) ( x _ { i } , t _ { j } )$ in the form

$$
\frac { \partial u } { \partial t } ( x _ { i } , t _ { j } ) = \frac { u ( x _ { i } , t _ { j } ) - u ( x _ { i } , t _ { j - 1 } ) } { k } + \frac { k } { 2 } \frac { \partial ^ { 2 } u } { \partial t ^ { 2 } } ( x _ { i } , \mu _ { j } ) ,
$$

where $\mu _ { j }$ is in $( t _ { j - 1 } , t _ { j } )$ . Substituting this equation, together with Eq. (12.8) for $\partial ^ { 2 } u / \partial x ^ { 2 }$ ， into the partial differential equation gives

$$
\begin{array} { l } { \displaystyle \frac { u ( x _ { i } , t _ { j } ) - u ( x _ { i } , t _ { j - 1 } ) } { k } - \dot { \alpha } ^ { 2 } \frac { u ( x _ { i + 1 } , t _ { j } ) - 2 u ( x _ { i } , t _ { j } ) + u ( x _ { i - 1 } , t _ { j } ) } { h ^ { 2 } } } \\ { \displaystyle \qquad = - \frac { k } { 2 } \frac { \partial ^ { 2 } u } { \partial t ^ { 2 } } ( x _ { i } , \mu _ { j } ) - \alpha ^ { 2 } \frac { h ^ { 2 } } { 1 2 } \frac { \partial ^ { 4 } u } { \partial x ^ { 4 } } ( \xi _ { i } , t _ { j } ) , } \end{array}
$$

for some $\xi _ { i } \in ( x _ { i - 1 } , x _ { i + 1 } )$ . The Backward-Difference method that results is

$$
{ \frac { w _ { i j } - w _ { i , j - 1 } } { k } } - \alpha ^ { 2 } { \frac { w _ { i + 1 , j } - 2 w _ { i j } + w _ { i - 1 , j } } { h ^ { 2 } } } = 0 ,
$$

for each $i = 1 , 2 , \dots , m - 1$ and $j = 1 , 2 , \ldots$

The Backward-Difference method involves,at a typical step, the mesh points

$$
( x _ { i } , t _ { j } ) , \quad ( x _ { i } , t _ { j - 1 } ) , \quad ( x _ { i - 1 } , t _ { j } ) , \quad \mathrm { a n d } \quad ( x _ { i + 1 } , t _ { j } ) ,
$$

and involves approximations at the points marked with $\times 3$ in Figure 12.8.

![](images/2cdfd6345f581f58e592c5a5cdd89989a80d9727342f72d468108606b4fd9098.jpg)  
Figure 12.8

Since the boundary and initial conditions associated with the problem give information at the circled mesh points,the figure shows that no explicit procedures can be used to solve Eq.(12.12). Recall that in the Forward-Difference method (see Figure 12.9), approximations at

$$
( x _ { i - 1 } , t _ { j } ) , \quad ( x _ { i } , t _ { j } ) , \quad ( x _ { i } , t _ { j + 1 } ) , \quad \mathrm { a n d } \quad ( x _ { i + 1 } , t _ { j } )
$$

were used, so an explicit method for finding the approximations, based on the information from the initial and boundary conditions, was available.

If we again let $\lambda$ denote the quantity $\alpha ^ { 2 } ( k / h ^ { 2 } )$ , the Backward-Difference method becomes

$$
( 1 + 2 \lambda ) w _ { i j } - \lambda w _ { i + 1 , j } - \lambda w _ { i - 1 , j } = w _ { i , j - 1 } ,
$$

![](images/eb55e768da65061423d403390ccbe5636730c1320469deacdb787792ac8122de.jpg)  
Figure 12.9

for each $i = 1 , 2 , \ldots , m - 1$ and $j = 1 , 2$ ，... Using the knowledge that $w _ { i , 0 } = f ( x _ { i } )$ ， for each $i = 1 , 2 , \dots , m - 1$ and $w _ { m , j } = w _ { 0 , j } = 0$ for each $j = 1 , 2 , \dots ,$ this difference method has the matrix representation:

$$
\left[ \begin{array} { c c c c c c c } { \left( 1 + 2 \lambda \right) } & { - \lambda _ { \cdot } } & { 0 } & { \vdots \ddots } & { \cdots } & { \cdots } & { 0 } \\ { - \lambda _ { \cdot } } & { \cdot } & { \cdot } & { \cdot } & { \cdot } & { \vdots } \\ { \cdot } & { \cdot } & { \cdot } & { \cdot } & { \cdot } & { \cdot } & { \cdot } \\ { \vdots } & { \cdot } & { \cdot } & { \cdot } & { \cdot } & { \ddots } & { \vdots } \\ { \vdots } & { \cdot } & { \cdot } & { \cdot } & { \ddots } & { \cdot } & { \vdots } \\ { \vdots } & { \cdot } & { \cdot } & { \cdot } & { \ddots } & { \cdot } & { \vdots } \end{array} \right] \left[ \begin{array} { c } { w _ { 1 , j } } \\ { w _ { 2 , j } } \\ { \vdots } \\ { w _ { m - 1 , j } } \end{array} \right] = \left[ \begin{array} { c } { w _ { 1 , j - 1 } } \\ { w _ { 2 , j - 1 } } \\ { \vdots } \\ { w _ { m - 1 , j - 1 } } \end{array} \right] ,
$$

or $A \mathbf { w } ^ { ( j ) } = \mathbf { w } ^ { ( j - 1 ) }$ , for each $i = 1 , 2 , \dots$

Hence, we must now solve a linear system to obtain $\pmb { w } ^ { ( j ) }$ from $\mathbf { w } ^ { ( j - 1 ) }$ . Since $\lambda > 0$ ,the matrix A is positive definite and strictly diagonally dominant, as well as being tridiagonal. We can use either the Crout Factorization Algorithm 6.7 or the SOR Algorithm 7.3 to solve this system.Algorithm 12.2 solves (12.13) using Crout factorization, which is acceptable unless m is large. In this algorithm we assume,for stopping purposes, that a bound is given for $t$

# Heat Equation Backward-Difference

To approximate the solution to the parabolic partial differential equation

$$
\frac { \partial u } { \partial t } ( x , t ) - \alpha ^ { 2 } \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } ( x , t ) = 0 , \quad 0 < x < l , \quad 0 < t < T ,
$$

subject to the boundary conditions

$$
u ( 0 , t ) = u ( l , t ) = 0 , \quad 0 < t < T ,
$$

and the initial conditions

$$
u ( x , 0 ) = f ( x ) , \quad 0 \leq x \leq l :
$$

INPUTendpoint $l$ ; maximum time $T$ ; constant $\pmb { \alpha }$ ; integers $m \ge 3 , N \ge 1$

OUTPUTapproximations $w _ { i , j }$ t0 $u ( x _ { i } , t _ { j } )$ for each $i = 1 , \ldots , m - 1$ and $j = 1 , \dots , N$

Step 1 Set $\begin{array} { c } { \dot { \boldsymbol { h } } = \boldsymbol { l } / m ; } \\ { \boldsymbol { k } = \boldsymbol { T } / N ; } \\ { \lambda = \alpha ^ { 2 } \boldsymbol { k } / h ^ { 2 } . } \end{array}$

Step 2 For $i = 1 , \ldots , m - 1$ set $w _ { i } = f ( i h )$ . (Initial values.) (Steps 3-11 solve a tridiagonal linear system using Algorithm 6.7.)

Step3 Set $\begin{array} { r } { l _ { 1 } = 1 + 2 \lambda ; } \\ { u _ { 1 } = - \lambda / l _ { 1 } . } \end{array}$

Step 4For $i = 2$ ，..， $m \to 2$ set $l _ { i } = 1 + 2 \lambda + \lambda u _ { i - 1 } ;$ $u _ { i } = - \lambda / l _ { i }$

Step 5 Set $l _ { m - 1 } = 1 + 2 \lambda + \lambda u _ { m - 2 }$

Step 6For $j = 1 , \dots , N$ do Steps 7-11.

$$
\begin{array} { c c } { { S t e p 7 } } & { { \mathrm { S e t } t = j k ; ( C u r r e n t t _ { j } . ) } } \\ { { } } & { { \ z _ { 1 } = w _ { 1 } / l _ { 1 } . } } \end{array}
$$

Step 8 $\mathrm { F o r } i = 2 , \ldots , m - 1 \mathrm { s e t } z _ { i } = ( w _ { i } + \lambda z _ { i - 1 } ) / l _ { i }$

Step 9 Set $w _ { m - 1 } = z _ { m - 1 }$

Step 10 Fori = m - 2,...,1 set $w _ { i } = z _ { i } - u _ { i } w _ { i + 1 }$

Step 11OUTPUT $( t )$ ； $( N o t e \colon t = t _ { j } .$ ） For i = 1,.., $m - 1$ set $x = i h$ ； OUTPUT $( x , w _ { i } )$ . (Note: Wi = Wi,j.)

Step 12 STOP. (The procedure is complete.)

The Backward-Difference method (Algorithm 12.2） with $h = 0 . 1$ and $k = 0 . 0 1$ will be used to approximate the solution to the heat equation

$$
\frac { \partial u } { \partial t } ( x , t ) - \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } ( x , t ) = 0 , \quad 0 < x < 1 , \quad 0 < t ,
$$

subject to the constraints

$$
u ( 0 , t ) = u ( 1 , t ) = 0 , \quad 0 < t , \quad u ( x , 0 ) = \sin \pi x , \quad 0 \leq x \leq 1 ,
$$

which was considered in Example 1. To demonstrate the unconditional stability of the Backward-Difference method,we again compare $w _ { i , 5 0 }$ to $u ( x _ { i } , 0 . 5 )$ ，where $i ~ = ~ 0 , 1$ ， ...,10.

The results listed in Table 12.4 have the same values of $h$ and $k$ as those in the fifth and sixth columns of Table 12.3,which illustrates the stability of this method.

# Table 12.4

<table><tr><td>Xi</td><td>Wi,50</td><td>u(xi,0.5)</td><td>|wi,50 - u(xi, 0.5)l</td></tr><tr><td>0.0</td><td>0</td><td>0</td><td></td></tr><tr><td>0.1</td><td>0.00289802</td><td>0.00222241</td><td>6.756 × 10-4</td></tr><tr><td>0.2</td><td>0.00551236</td><td>0.00422728</td><td>1.285 × 10-3</td></tr><tr><td>0.3</td><td>0.00758711</td><td>0.00581836</td><td>1.769 ×10-3</td></tr><tr><td>0.4</td><td>0.00891918</td><td>0.00683989</td><td>2.079 × 10-3</td></tr><tr><td>0.5</td><td>0.00937818</td><td>0.00719188</td><td>2.186 × 10-3</td></tr><tr><td>0.6</td><td>0.00891918</td><td>0.00683989</td><td>2.079 × 10-3</td></tr><tr><td>0.7</td><td>0.00758711</td><td>0.00581836</td><td>1.769 × 10-3</td></tr><tr><td>0.8</td><td>0.00551236</td><td>0.00422728</td><td>1.285 ×10-3</td></tr><tr><td>0.9</td><td>0.00289802</td><td>0.00222241</td><td>6.756 × 10-4</td></tr><tr><td>1.0</td><td>0</td><td>0</td><td></td></tr></table>

The reason that the Backward-Difference method does not have the stability problems of the Forward-Difference method can be seen by analyzing the eigenvalues of the matrix A.For the Backward-Difference method (see Exercise 8), the eigenvalues are

$$
\mu _ { i } = 1 + 4 \lambda \Biggl [ \sin { \biggl ( \frac { i \pi } { 2 m } \biggr ) } \Biggr ] ^ { 2 } , \quad \mathrm { f o r e a c h } i = 1 , 2 , \ldots , m - 1 ,
$$

and since $\lambda > 0$ ，we have $\mu _ { i } ~ > ~ 1$ ,for all $i = 1 , 2 , \dotsc , m - 1$ . This implies that $A ^ { - 1 }$ exists since zero is not an eigenvalue of $A$ . An error ${ \bf e } ^ { ( 0 ) }$ in the initial data produces an error $( A ^ { - 1 } ) ^ { n } \mathbf { e } ^ { ( 0 ) }$ at the $\pmb { n }$ th step. Since the eigenvalues of $A ^ { - 1 }$ are the reciprocals of the eigenvalues of A,the spectral radius of A-1 is bounded above by 1,and the method is stable,independent of the choice of $\lambda = \alpha ^ { 2 } ( k / h ^ { 2 } )$ . In the terminology of Chapter 5,we call the Backward-Difference method an unconditionally stable method. The local truncation error for the method is of order $O ( k + h ^ { 2 } )$ , provided the solution of the differential equation satisfies the usual differentiability conditions.In this case, the method converges to the solution of the partial differential equation with this same rate of convergence (see [IK, p. 508]).

The weakness in the Backward-Difference method results from the fact that the local truncation error has a portion with order $O ( k )$ , requiring that time intervals be made much smaller than spatial intervals. It would clearly be desirable to have a procedure with local truncation error of order $O ( k ^ { 2 } + h ^ { 2 } )$ . The first step in this direction is to use a difference equation that has $O ( k ^ { 2 } )$ error for $u _ { t } ( x , t )$ instead of those we have used previously, whose error was $O ( k )$ . This can be done by using the Taylor series in $t$ for the function $u ( x , t )$ at the point $( x _ { i } , t _ { j } )$ and evaluating at $( x _ { i } , t _ { j + 1 } )$ and $( x _ { i } , t _ { j - 1 } )$ to obtain the Centered-Difference formula

$$
\frac { \partial u } { \partial t } ( x _ { i } , t _ { j } ) = \frac { u ( x _ { i } , t _ { j + 1 } ) - u ( x _ { i } , t _ { j - 1 } ) } { 2 k } + \frac { k ^ { 2 } } { 6 } \frac { \partial ^ { 3 } u } { \partial t ^ { 3 } } ( x _ { i } , \mu _ { j } ) ,
$$

where $\mu _ { j } \in ( t _ { j - 1 } , t _ { j + 1 } )$ . The difference method that results from substituting this and the usual difference quotient for $( \partial ^ { 2 } u / \partial x ^ { 2 } )$ ,Eq. (12.8),into the differential equation is called Richardson's method and is given by

$$
{ \frac { w _ { i , j + 1 } - w _ { i , j - 1 } } { 2 k } } - \alpha ^ { 2 } { \frac { w _ { i + 1 , j } - 2 w _ { i j } + w _ { i - 1 , j } } { h ^ { 2 } } } = 0 .
$$