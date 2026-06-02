The proof that the method presented in Algorithm 5.6 converges involves results from summability theory; it can be found in the original paper of Gragg [Gr]. A number of other extrapolation procedures are available, some of which use the variable step-size techniques. For additional procedures based on the extrapolation process, see the Bulirsch and Stoer papers [BS1],[BS2],[BS3] or the text by Steter [Stet]. The methods used by Bulirsch and Stoer involve interpolation with rational functions instead of the polynomial interpolation used in the Gragg procedure.

# Exercise Set 5.8

1.Use the Extrapolation Algorithm with tolerance $T O L = 1 0 ^ { - 4 }$ ， $h m a x \ : = \ : 0 . 2 5$ ,and hmin $\backsimeq$ 0.05 to approximate the solutions to the following initial-value problems. Compare the results to the actual values.

a. $y ^ { \prime } = t e ^ { 3 t } - 2 y , \quad 0 \leq t \leq 1 , \quad y ( 0 ) = 0 ;$ actual solution $\begin{array} { r } { y ( t ) = \frac { 1 } { 5 } t e ^ { 3 t } - \frac { 1 } { 2 5 } e ^ { 3 t } + \frac { 1 } { 2 5 } e ^ { - 2 t } } \end{array}$ b. $y ^ { \prime } = 1 + ( t - y ) ^ { 2 } , \quad 2 \leq t \leq 3 , \quad y ( 2 ) = 1$ ；actual solution $y ( t ) = t + 1 / ( 1 - t )$ c. $y ^ { \prime } = 1 + y / t , \quad 1 \leq t \leq 2 , \quad y ( 1 ) = 2 ;$ actual solution $y ( t ) = t \ln t + 2 t$ d. $y ^ { \prime } = \cos 2 t + \sin 3 t$ ， $0 \leq t \leq 1$ $y ( 0 ) = 1$ ；actual solution $y ( t ) = { \textstyle { \frac { 1 } { 2 } } } \sin 2 t -$ $\begin{array} { r } { \frac { 1 } { 3 } \cos 3 t + \frac { 4 } { 3 } } \end{array}$

2. Use the Extrapolation Algorithm with $T O L = 1 0 ^ { - 4 }$ to approximate the solutions to the following initial-value problems:

a. $y ^ { \prime } = ( y / t ) ^ { 2 } + y / t , \quad 1 \leq t \leq 1 . 2 , \quad y ( 1 ) = 1$ ,with $h m a x = 0 . 0 5$ and hmi $n = 0 . 0 2$ b. $y ^ { \prime } = \sin t + e ^ { - t } , \quad 0 \leq t \leq 1 , \quad y ( 0 ) = 0 ,$ with $h m a x = 0 . 2 5$ and hmi $n = 0 . 0 2$ c. $y ^ { \prime } = ( 1 / t ) ( y ^ { 2 } + y ) , \quad 1 \leq t \leq 3 , \quad y ( 1 ) = - 2$ ，with $h m a x = 0 . 5$ and hm ${ \bf \nabla } ; i n = 0 . 0 2$ d. $y ^ { \prime } = - t y + 4 t / y , \quad 0 \leq t \leq 1 , \quad y ( 0 ) = 1$ ，with $h m a x = 0 . 2 5$ and $h m i n = 0 . 0 2$

3.Use the Extrapolation Algorithm with tolerance $T O L = 1 0 ^ { - 6 }$ ， $h m a x = 0 . 5$ ,and $h m i n = 0 . 0 5$ to approximate the solutions to the following initial-value problems.Compare the results to the actual values.

a. $y ^ { \prime } = y / t - ( y / t ) ^ { 2 } , \quad 1 \leq t \leq 4 , \quad y ( 1 ) = 1 ;$ actual solution $y ( t ) = t / ( 1 + \ln t )$   
b. $y ^ { \prime } = 1 + y / t + ( y / t ) ^ { 2 } , \quad 1 \leq t \leq 3 , \quad y ( 1 ) = 0 .$ actual solution $y ( t ) = t \tan ( \ln t )$   
c. $y ^ { \prime } = - ( y + 1 ) ( y + 3 ) , \quad 0 \leq t \leq 3 , \quad y ( 0 ) = - 2$ ； actual solution $y ( t ) = - 3 + 2 ( 1 +$ e-21)-1.   
d. y=(t +2t³）y³-ty， $0 \leq t \leq 2$ $\begin{array} { r } { y ( 0 ) = \frac { 1 } { 3 } } \end{array}$ ； actual solution $y ( t ) = ( 3 + 2 t ^ { 2 } +$ 6e²2)-1/2.

4.Let $P ( t )$ be the number of individuals in a population at time $t$ ，measured in years. If the average birth rate $b$ is constant and the average death rate $d$ is proportional to the size of the population (due to overcrowding),then the growth rate of the population is given by the logistic equation

$$
\frac { d P ( t ) } { d t } = b P ( t ) - k [ P ( t ) ] ^ { 2 } ,
$$

where $d = k P ( t )$ . Suppose $P ( 0 ) = 5 0 , 9 7 6 , b = 2 . 9 \times 1 0 ^ { - 2 }$ ,and $k = 1 . 4 \times 1 0 ^ { - 7 }$ . Find the population after 5 years.

# 5.9 Higher-Order Equations and Systems of Differential Equations

This section contains an introduction to the numerical solution of higher-order initial-value problems.The techniques discussed are limited to those that transform a higher-order equation into a system of first-order differential equations. Before discussing the transformation procedure,some remarks are needed concerning systems that involve first-order differential equations.

An mth-order system of first-order initial-value problems has the form

$$
\frac { d u _ { 1 } } { d t } = f _ { 1 } ( t , u _ { 1 } , u _ { 2 } , . . . , u _ { m } ) ,
$$

$$
\frac { d u _ { 2 } } { d t } = f _ { 2 } ( t , u _ { 1 } , u _ { 2 } , . . . , u _ { m } ) ,
$$

$$
\frac { d u _ { m } } { d t } = f _ { m } ( t , u _ { 1 } , u _ { 2 } , \ldots , u _ { m } ) ,
$$

for $a \leq t \leq b$ , with the initial conditions

$$
u _ { 1 } ( a ) = \alpha _ { 1 } , u _ { 2 } ( a ) = \alpha _ { 2 } , . . . , u _ { m } ( a ) = \alpha _ { m } .
$$

The object is to find $m$ functions $u _ { 1 } , u _ { 2 } , \ldots , u _ { m }$ that satisfy each of the differential equations together with all the initial conditions.

To discuss existence and uniqueness of solutions to systems of equations, we need to extend the definition of the Lipschitz condition to functions of several variables.

# Definition 5.16

The function $f ( t , y _ { 1 } , \dots , y _ { m } )$ , defined on the set

$$
D = \{ \ ( t , u _ { 1 } , \ldots , u _ { m } ) \mid a \leq t \leq b , - \infty < u _ { i } < \infty ,
$$

is said to satisfy a Lipschitz condition on $D$ in the variables $u _ { 1 } , u _ { 2 } , \ldots , u _ { m }$ if a constant $L > 0$ exists with

$$
| f ( t , u _ { 1 } , \ldots , u _ { m } ) - f ( t , z _ { 1 } , \ldots , z _ { m } ) | \leq L \sum _ { j = 1 } ^ { m } | u _ { j } - z _ { j } | ,
$$

for all $( t , u _ { 1 } , \ldots , u _ { m } )$ and $( t , z _ { 1 } , \ldots , z _ { m } )$ in $D$

By using the Mean Value Theorem, it can be shown that if $f$ and its first partial derivatives are continuous on $D$ and if

$$
\left| \frac { \partial f ( t , u _ { 1 } , \ldots , u _ { m } ) } { \partial u _ { i } } \right| \leq L ,
$$

for each $i = 1 , 2 , \dots , m$ and all $( t , u _ { 1 } , \ldots , u _ { m } )$ in $D$ ,then $f$ satisfies a Lipschitz condition on $D$ with Lipschitz constant $L$ (see [BiR,p. 141]). A basic existence and uniqueness theorem follows. Its proof can be found in [BiR, pp. 152-154].

Theorem 5.17

$D = \{ ( t , u _ { 1 } , u _ { 2 } , \ldots , u _ { m } ) \mid a \leq t \leq b , - \infty < u _ { i } < \infty ,$ for each $i = 1 , 2 , \dots , m \}$ ，

and let $f _ { i } ( t , u _ { 1 } , \dots , u _ { m } )$ , for each $i = 1 , 2 , \dots , m$ , be continuous on $D$ and satisfy a Lipschitz condition there. The system of first-order differential equations (5.44), subject to the initial conditions (5.45),has a unique solution $u _ { 1 } ( t ) , \ldots , u _ { m } ( t )$ ,for $a \leq t \leq b$

Methods to solve systems of first-order differential equations are generalizations of the methods for a single first-order equation presented earlier in this chapter. For example, the classical Runge-Kutta method of order four given by

$$
\begin{array} { l } { w _ { 0 } = \alpha , } \\ { k _ { 1 } = h f ( t _ { i } , w _ { i } ) , } \\ { k _ { 2 } = h f \displaystyle \biggl ( t _ { i } + \frac { h } { 2 } , w _ { i } + \frac { 1 } { 2 } k _ { 1 } \biggr ) , } \\ { k _ { 3 } = h f \displaystyle \biggl ( t _ { i } + \frac { h } { 2 } , w _ { i } + \frac { 1 } { 2 } k _ { 2 } \biggr ) , } \\ { k _ { 4 } = h f ( t _ { i + 1 } , w _ { i } + k _ { 3 } ) , } \end{array}
$$

and

$$
w _ { i + 1 } = w _ { i } + \frac { 1 } { 6 } ( k _ { 1 } + 2 k _ { 2 } + 2 k _ { 3 } + k _ { 4 } ) , \quad \mathrm { f o r } \mathrm { e a c h } i = 0 , 1 , \dots , N - 1 ,
$$

used to solve the first-order initial-value problem

$$
y ^ { \prime } = f ( t , y ) , \quad a \leq t \leq b , \quad y ( a ) = \alpha ,
$$

is generalized as follows.

Let an integer $N > 0$ be chosen and set $h = ( b - a ) / N$ . Partition the interval $[ a , b ]$ into $N$ subintervals with the mesh points

$$
t _ { j } = a + j h , \quad \mathrm { f o r } \operatorname { e a c h } j = 0 , 1 , \dots , N .
$$

Use the notation $w _ { i j }$ , for each $j = 0 , 1 , . . . , N$ and $i = 1 , 2 , \dots , m$ , to denote an approximation to $u _ { i } \left( t _ { j } \right)$ . That is, $w _ { i j }$ approximates the ith solution $u _ { i } \left( t \right)$ of (5.44) at the $j$ th mesh point $t _ { j }$ . For the initial conditions, set (see Figure 5.5)

$$
w _ { 1 , 0 } = \alpha _ { 1 } , \ w _ { 2 , 0 } = \alpha _ { 2 } , \ \dotsc , \ w _ { m , 0 } = \alpha _ { m } .
$$

Suppose that the values $w _ { 1 , j } , w _ { 2 , j } , \dotsc , w _ { m , j }$ have been computed. We obtain $w _ { 1 , j + 1 }$ $w _ { 2 , j + 1 } , \dotsc , w _ { m , j + 1 }$ by first calculating

$$
k _ { 1 , i } = h f _ { i } ( t _ { j } , w _ { 1 , j } , w _ { 2 , j } , . . . , w _ { m , j } ) , \quad \mathrm { f o r e a c h } i = 1 , 2 , . . . , m ;
$$

$$
k _ { 2 , i } = h f _ { i } \left( t _ { j } + \frac { h } { 2 } , w _ { 1 , j } + \frac { 1 } { 2 } k _ { 1 , 1 } , w _ { 2 , j } + \frac { 1 } { 2 } k _ { 1 , 2 } , \ldots , w _ { m , j } + \frac { 1 } { 2 } k _ { 1 , m } \right) ,
$$

![](images/05a94265d0f3e0731f68fcfbf61deba52ca2d608386af0c254c5496bae1d6171.jpg)  
Figure 5.5

for each $i = 1 , 2 , \dots , m ;$

$$
k _ { 3 , i } = h f _ { i } \left( t _ { j } + \frac { h } { 2 } , w _ { 1 , j } + \frac { 1 } { 2 } k _ { 2 , 1 } , w _ { 2 , j } + \frac { 1 } { 2 } k _ { 2 , 2 } , \ldots , w _ { m , j } + \frac { 1 } { 2 } k _ { 2 , m } \right) ,
$$

for each $i = 1 , 2 , \dots , m$

$$
k _ { 4 , i } = h f _ { i } ( t _ { j } + h , w _ { 1 , j } + k _ { 3 , 1 } , w _ { 2 , j } + k _ { 3 , 2 } , \ldots , w _ { m , j } + k _ { 3 , m } ) ,
$$

for each $i = 1 , 2 , \dots , m$ ; and then

$$
w _ { i , j + 1 } = w _ { i , j } + \frac { 1 } { 6 } ( k _ { 1 , i } + 2 k _ { 2 , i } + 2 k _ { 3 , i } + k _ { 4 , i } ) ,
$$

for each $i = 1 , 2 , \dots , m$ . Note that all the values $k _ { 1 , 1 } , k _ { 1 , 2 } , \ldots , k _ { 1 , m }$ must be computed be-fore any of the terms of the form $k _ { 2 , i }$ can be determined. In general, each $k _ { l , 1 } , k _ { l , 2 } , \ldots , k _ { l , m }$ must be computed before any of the expressions $k _ { l + 1 , i }$ . Algorithm 5.7 implements the Runge-Kutta fourth-order method for systems of initial-value problems.

# Runge-Kutta Method for Systems of Differential Equations

To approximate the solution of the $m$ th-order system of first-order initial-value problems

$$
\begin{array} { r } { u _ { j } ^ { \prime } = f _ { j } ( t , u _ { 1 } , u _ { 2 } , \ldots , u _ { m } ) , \quad a \leq t \leq b , \quad \mathrm { w i t h } \quad u _ { j } ( a ) = \alpha _ { j } , } \end{array}
$$

for $j = 1 , 2 , \dots , m$ at $( N + 1 )$ equally spaced numbers in the interval $[ a , b ]$ ：

INPUTendpoints $a , b$ ; number of equations $m$ ; integer $N$ ; initial conditions $\alpha _ { 1 } , \ldots , \alpha _ { m }$ OUTPUTapproximations $w _ { j }$ to $u _ { j } ( t )$ at the $( N + 1 )$ values of $t$

Step 1 $\begin{array} { c } { \mathrm { S e t } h = ( b - a ) / N ; } \\ { t = a . } \end{array}$

Step 2 For $j = 1 , 2 , \dots , m$ set $w _ { j } = \alpha _ { j }$

Step 3OUTPUT $( t , w _ { 1 } , w _ { 2 } , \ldots , w _ { m } )$ ·

Step 4 For $i = 1 , 2 , \dots , N$ do steps 5-11.

Step 5For $j = 1$ ,2,...,.m set

$$
k _ { 1 , j } = h f _ { j } ( t , w _ { 1 } , w _ { 2 } , \ldots , w _ { m } ) .
$$

Step 6For $j = 1 , 2 , \dots , m$ set

$$
\begin{array} { r } { k _ { 2 , j } = h f _ { j } \big ( t + \frac { h } { 2 } , w _ { \mathrm { i } } + \frac { 1 } { 2 } k _ { 1 , \mathrm { t } } , w _ { 2 } + \frac { 1 } { 2 } k _ { 1 , 2 } , \ldots , w _ { m } + \frac { 1 } { 2 } k _ { 1 , m } \big ) . } \end{array}
$$

Step 7 For $j = 1 , 2 , \dots , m$ set

$$
\begin{array} { r } { k _ { 3 , j } = h f _ { j } \big ( t + \frac { h } { 2 } , w _ { 1 } + \frac { 1 } { 2 } k _ { 2 , 1 } , w _ { 2 } + \frac { 1 } { 2 } k _ { 2 , 2 } , \ldots , w _ { m } + \frac { 1 } { 2 } k _ { 2 , m } \big ) . } \end{array}
$$

Step 8 For j = 1,2,...,.m set

$$
k _ { 4 , j } = h f _ { j } ( t + h , w _ { 1 } + k _ { 3 , 1 } , w _ { 2 } + k _ { 3 , 2 } , \ldots , w _ { m } + k _ { 3 , m } ) .
$$

Step 9 For $j = 1 , 2 , \dots , m$ set

$$
w _ { j } = w _ { j } + ( k _ { 1 , j } + 2 k _ { 2 , j } + 2 k _ { 3 , j } + k _ { 4 , j } ) / 6 .
$$

Step 10 Set $t = a + i h$

Step 11 OUTPUT $( t , w _ { 1 } , w _ { 2 } , \ldots , w _ { m } )$

Step 12 STOP.

Kirchhoff's Law states that the sum of all instantaneous voltage changes around a closed circuit is zero. This law implies that the current $I ( t )$ in a closed circuit containing a re-sistance of $R$ ohms, a capacitance of $C$ farads, an inductance of $L$ henries, and a voltage source of $E ( t )$ volts satisfies the equation

$$
L I ^ { \prime } ( t ) + R I ( t ) + { \frac { 1 } { C } } \int I ( t ) d t = E ( t ) .
$$

The currents $I _ { 1 } ( t )$ and $I _ { 2 } ( t )$ in the left and right Ioops,respectively,of the circuit shown in Figure 5.6 are the solutions to the system of equations

$$
2 I _ { 1 } ( t ) + 6 [ I _ { 1 } ( t ) - I _ { 2 } ( t ) ] + 2 I _ { 1 } ^ { \prime } ( t ) = 1 2 ,
$$

$$
\frac { 1 } { 0 . 5 } \int I _ { 2 } ( t ) d t + 4 I _ { 2 } ( t ) + 6 [ I _ { 2 } ( t ) - I _ { 1 } ( t ) ] = 0 .
$$

![](images/6ab07e2a44c81f3ec20cf6822a6c8da3b6921ffabd5d901acd07a916769a4876.jpg)  
Figure 5.6

Suppose that the switch in the circuit is closed at time $t = 0$ . Then $I _ { 1 } ( 0 ) = 0$ and $I _ { 2 } ( 0 ) \ = \ 0$ Solve for $I _ { 1 } ^ { \prime } ( t )$ in the first equation, differentiate the second equation, and substitute for $I _ { 1 } ^ { \prime } ( t )$ to get

$$
\begin{array} { l } { { I _ { 1 } ^ { \prime } = f _ { 1 } ( t , I _ { 1 } , I _ { 2 } ) = - 4 I _ { 1 } + 3 I _ { 2 } + 6 , \quad I _ { 1 } ( 0 ) = 0 , } } \\ { { I _ { 2 } ^ { \prime } = f _ { 2 } ( t , I _ { 1 } , I _ { 2 } ) = 0 . 6 I _ { 1 } ^ { \prime } - 0 . 2 I _ { 2 } = - 2 . 4 I _ { 1 } + 1 . 6 I _ { 2 } + 3 . 6 , \quad I _ { 2 } ( 0 ) = 0 . } } \end{array}
$$

The exact solution to this system is

$$
\begin{array} { r l } & { I _ { 1 } ( t ) = - 3 . 3 7 5 e ^ { - 2 t } + 1 . 8 7 5 e ^ { - 0 . 4 t } + 1 . 5 , } \\ & { I _ { 2 } ( t ) = - 2 . 2 5 e ^ { - 2 t } + 2 . 2 5 e ^ { - 0 . 4 t } . } \end{array}
$$

We will apply the Runge-Kutta method of order four to this system with $h = 0 . 1$ Since $w _ { 1 , 0 } = I _ { 1 } ( 0 ) = 0$ and $w _ { 2 , 0 } = I _ { 2 } ( 0 ) = 0$ ，

$$
\begin{array} { r l } & { k _ { 1 , 1 } = h f _ { 1 } ( t _ { 0 } , w _ { 1 , 0 } , w _ { 2 , 0 } ) = 0 . 1 f _ { 1 } ( 0 , 0 , 0 ) = 0 . 1 [ - 4 ( 0 ) + 3 ( 0 ) + 6 ] = 0 . 6 , } \\ & { k _ { 1 , 2 } = h f _ { 2 } ( t _ { 0 } , w _ { 1 , 0 } , w _ { 2 , 0 } ) = 0 . 1 f _ { 2 } ( 0 , 0 , 0 ) = 0 . 1 [ - 2 . 4 ( 0 ) + 1 . 6 ( 0 ) + 3 . 6 ] = } \\ & { k _ { 2 , 1 } = h f _ { 1 } \left( t _ { 0 } + \displaystyle \frac { 1 } { 2 } h , w _ { 1 , 0 } + \displaystyle \frac { 1 } { 2 } k _ { 1 , 1 } , w _ { 2 , 0 } + \displaystyle \frac { 1 } { 2 } k _ { 1 , 2 } \right) = 0 . 1 f _ { 1 } ( 0 . 0 5 , 0 . 3 , 0 . 1 8 ) } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & & { \quad \quad = 0 . 1 [ - 4 ( 0 . 3 ) + 3 ( 0 . 1 8 ) + 6 ] = 0 . 5 3 4 , } \\ & { k _ { 2 , 2 } = h f _ { 2 } \left( t _ { 0 } + \displaystyle \frac { 1 } { 2 } h , w _ { 1 , 0 } + \displaystyle \frac { 1 } { 2 } k _ { 1 , 1 } , w _ { 2 , 0 } + \displaystyle \frac { 1 } { 2 } k _ { 1 , 2 } \right) = 0 . 1 f _ { 2 } ( 0 . 0 5 , 0 . 3 , 0 . 1 8 ) } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad = 0 . 1 [ - 2 . 4 ( 0 . 3 ) + 1 . 6 ( 0 . 1 8 ) + 3 . 6 ] = 0 . 3 1 6 8 . } \end{array}
$$

Generating the remaining entries in a similar manner produces

$$
\begin{array} { r l } & { k _ { 3 , 1 } = ( 0 . 1 ) f _ { 1 } ( 0 . 0 5 , 0 . 2 6 7 , 0 . 1 5 8 4 ) = 0 . 5 4 0 7 2 , } \\ & { k _ { 3 , 2 } = ( 0 . 1 ) f _ { 2 } ( 0 . 0 5 , 0 . 2 6 7 , 0 . 1 5 8 4 ) = 0 . 3 2 1 2 6 4 , } \\ & { k _ { 4 , 1 } = ( 0 . 1 ) f _ { 1 } ( 0 . 1 , 0 . 5 4 0 7 2 , 0 . 3 2 1 2 6 4 ) = 0 . 4 8 0 0 9 1 2 } \end{array}
$$

and

$$
k _ { 4 , 2 } = ( 0 . 1 ) f _ { 2 } ( 0 . 1 , 0 . 5 4 0 7 2 , 0 . 3 2 1 2 6 4 ) = 0 . 2 8 1 6 2 9 4 4 .
$$

As a consequence,

$$
\begin{array} { r l r } {  { I _ { 1 } ( 0 . 1 ) \approx w _ { 1 , l } = w _ { 1 , 0 } + \frac { 1 } { 6 } ( k _ { 1 , l } + 2 k _ { 2 , 1 } + 2 k _ { 3 , 1 } + k _ { 4 , 1 } ) } } \\ & { } & \\ & { } & { = 0 + \frac { 1 } { 6 } [ 0 . 6 + 2 ( 0 . 5 3 4 ) + 2 ( 0 . 5 4 0 7 2 ) + 0 . 4 8 0 0 9 1 2 ] = 0 . 5 3 8 2 5 5 2 } \end{array}
$$

and

$$
I _ { 2 } ( 0 . 1 ) \approx w _ { 2 , 1 } = w _ { 2 , 0 } + \frac { 1 } { 6 } ( k _ { 1 , 2 } + 2 k _ { 2 , 2 } + 2 k _ { 3 , 2 } + k _ { 4 , 2 } ) = 0 . 3 1 9 6 2 6 3 .
$$

The remaining entries in Table 5.17 are generated in a similar manner.

Table 5.17   

<table><tr><td>i</td><td>W1.j</td><td>W2.j</td><td>11(tj）-w1.jl</td><td>/(tj）-w2.jl</td></tr><tr><td>0.0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0.1</td><td>0.5382550</td><td>0.3196263</td><td>0.8285×10-5</td><td>0.5803 × 10-5</td></tr><tr><td>0.2</td><td>0.9684983</td><td>0.5687817</td><td>0.1514× 10-4</td><td>0.9596 × 10-5</td></tr><tr><td>0.3</td><td>1.310717</td><td>0.7607328</td><td>0.1907× 10-4</td><td>0.1216 × 10-4</td></tr><tr><td>0.4</td><td>1.581263</td><td>0.9063208</td><td>0.2098×10-4</td><td>0.1311 × 10-4</td></tr><tr><td>0.5</td><td>1.793505</td><td>1.014402</td><td>0.2193×10-4</td><td>0.1240 × 10-4</td></tr></table>

Maple's command dsolve can be used to solve systems of first-order differential equations.The system in Example 1 is defined with

$> \mathbf { s } \mathbf { y } \mathbf { s } \ \mathbf { 2 } : = \operatorname { D } ( \mathbf { u } \ \mathbf { 1 } ) \ ( \mathbf { t } ) = - 4 \ast \mathbf { u } \ \mathbf { 1 } \left( \mathbf { t } \right) + 3 \ast \mathbf { u } \ \mathbf { 2 } \left( \mathbf { t } \right) + 6 \ , \operatorname { D } ( \mathbf { u } \ \mathbf { 2 } ) \ ( \mathbf { t } ) = - 2 \ . 4 \ast \mathbf { u } \ \mathbf { 1 } \left( \mathbf { t } \right) + \mathbf { 1 } \ . 6 \ast \mathbf { u } \ \mathbf { 2 } \left( \mathbf { t } \right) = 0 \ .$ )+3.6; and the initial conditions with

$$
{ \bf \gamma } > \mathrm { i n i t } 2 : = { \bf u } 1 \left( 0 \right) = 0 , { \bf u } 2 \left( 0 \right) = 0 ;
$$

The system is solved with the command

$$
> { \bf s } { \mathrm { o l } } 2 : = { \tt d s o l v e } \left( \left\{ { \bf s } { \bf y } { \bf s } 2 , \mathrm { i n i t } 2 \right\} , \left\{ { \bf u } 1 \left( { \bf t } \right) , { \bf u } 2 \left( { \bf t } \right) \right\} \right) ;
$$

to obtain

$$
{ \mathrm { s o l } } 2 : = \left\{ u 1 ( t ) = { \frac { 3 } { 2 } } - { \frac { 2 7 } { 8 } } e ^ { ( - 2 t ) } + { \frac { 1 5 } { 8 } } e ^ { ( - 2 / 5 t ) } , u 2 ( t ) = - { \frac { 9 } { 4 } } e ^ { ( - 2 t ) } + { \frac { 9 } { 4 } } e ^ { ( - 2 / 5 t ) } \right\}
$$

To isolate the solution in function form, use

>r1:=rhs(sol2[2]);

$$
r 1 : = \frac 3 2 - \frac { 2 7 } { 8 } e ^ { ( - 2 t ) } + \frac { 1 5 } { 8 } e ^ { ( - 2 / 5 t ) }
$$

and

>r2:=rhs(sol2[1]);

which gives a similar response.

To evaluate $u _ { 1 } ( 0 . 5 )$ and $u _ { 2 } ( 0 . 5 )$ ,use

>evalf(subs $( \mathtt { t } { = } 0 . 5 , \mathtt { r } { 1 } )$ );evalf(subs(t=0.5,r2);

to get 1.793527048 and 1.014415451.

The command dsolve will fail if an explicit solution cannot be found. In that case we can use the numeric option in dsolve, which applies the Runge-Kutta-Fehlberg technique. For example,

$$
{ \bf \gamma } > { \bf g } : = { \bf d s o l v e } \left( \left\{ { \bf s y s } 2 , \mathrm { i n i t } 2 \right\} , \left\{ { \bf u } 1 \left( { \bf t } \right) , { \bf u } 2 \left( { \bf t } \right) \right\} , { \bf n u m e r i c } \right) ; 0 . 1 1 \mathrm { { \bf s h a n d e r } } 1 0 > { \bf d } , { \bf s } _ { 0 } = { \bf d } .
$$

returns the procedure

$$
g : = \operatorname { p r o c } ( r k f 4 5 \lrcorner x ) \ldots \operatorname { e n d } \operatorname { p r o c }
$$

To approximate the solutions at $t = 0 . 5$ ,enter

to obtain

$$
[ t = { \AA } , { \AA } , { \mathrm { ~ } } u 2 ( t ) = 1 . 0 1 4 4 1 5 4 5 4 7 0 2 9 1 7 6 1 , { \mathrm { ~ } } u 1 ( t ) = 1 . 7 9 3 5 2 7 0 5 2 4 3 7 6 6 5 8 6 ]
$$

Many important physical problems-for example, electrical circuits and vibrating systems--involve initial-value problems whose equations have orders higher than one. New techniques are not required for solving these problems; by relabeling the variables, we can reduce a higher-order differential equation into a system of first-order differential equations and then apply one of the methods we have already discussed. A general $m$ th-order initial-value problem

$$
y ^ { ( m ) } ( t ) = f ( t , y , y ^ { \prime } , \ldots , y ^ { ( m - 1 ) } ) , \ \quad a \leq t \leq b ,
$$

with initial conditions $y ( a ) = \alpha _ { 1 }$ ， $y ^ { \prime } ( a ) = \alpha _ { 2 } , \ldots , y ^ { ( m - 1 ) } ( a ) = \alpha _ { m }$ can be converted into a system of equations in the form (5.44) and (5.45).

Let $u _ { 1 } ( t ) = y ( t ) , u _ { 2 } ( t ) = y ^ { \prime } ( t ) , . . .$ and $u _ { m } ( t ) = y ^ { ( m - 1 ) } ( t )$ . This produces the frstorder system

$$
\frac { d u _ { 1 } } { d t } = \frac { d y } { d t } = u _ { 2 } ,
$$

$$
\frac { d u _ { 2 } } { d t } = \frac { d y ^ { \prime } } { d t } = u _ { 3 } ,
$$

$$
\frac { d u _ { m - 1 } } { d t } = \frac { d y ^ { ( m - 2 ) } } { d t } = u _ { m } ,
$$

and

$$
\frac { d u _ { m } } { d t } = \frac { d y ^ { ( m - 1 ) } } { d t } = y ^ { ( m ) } = f ( t , y , y ^ { \prime } , \ldots , y ^ { ( m - 1 ) } ) = f ( t , u _ { 1 } , u _ { 2 } , \ldots , u _ { m } ) ,
$$

with initial conditions

$$
u _ { 1 } ( a ) = y ( a ) = \alpha _ { 1 } , \quad u _ { 2 } ( a ) = y ^ { \prime } ( a ) = \alpha _ { 2 } , \quad \ldots , \quad u _ { m } ( a ) = y ^ { ( m - 1 ) } ( a ) = \alpha _ { m } .
$$

# EXAMPLE 2

Consider the second-order initial-value problem

$$
y ^ { \prime \prime } \ldots 2 y ^ { \prime } + 2 y = e ^ { 2 t } \sin t , \qquad \mathrm { f o r ~ } 0 \leq t \leq 1 , \quad \mathrm { ~ w i t h ~ } y ( 0 ) = - 0 . 4 , \ y ^ { \prime } ( 0 ) = - 0 . 6 .
$$

Let $u _ { 1 } ( t ) = y ( t )$ and $u _ { 2 } ( t ) = y ^ { \prime } ( t )$ . This transforms the equation into the system

$$
\begin{array} { l } { { u _ { 1 } ^ { \prime } ( t ) = u _ { 2 } ( t ) , } } \\ { { u _ { 2 } ^ { \prime } ( t ) = e ^ { 2 t } \sin t - 2 u _ { 1 } ( t ) + 2 u _ { 2 } ( t ) , } } \end{array}
$$

with initial conditions

$$
\begin{array} { r } { u _ { 1 } ( 0 ) = - 0 . 4 , ~ u _ { 2 } ( 0 ) = - 0 . 6 . } \end{array}
$$

The Runge-Kutta fourth-order method will be used to approximate the solution to this problem using $h = 0 . 1$ . The initial conditions give $w _ { 1 , 0 } = - 0 . 4$ and $w _ { 2 , 0 } = - 0 . 6$ Eqs. (5.48) through (5.51) with $j = 0$ give

$$
\begin{array} { r l } & { k _ { 1 , 1 } = \hbar { f _ { 1 } } ( { t _ { 0 } } , \boldsymbol { w } _ { 1 , 0 } , \boldsymbol { w } _ { 2 , 0 } ) = \hbar { w _ { 2 , 0 } } = - 0 . 0 6 , } \\ & { k _ { 1 , 2 } = \hbar { f _ { 2 } } ( { t _ { 0 } } , \boldsymbol { w } _ { 1 , 0 } , \boldsymbol { w } _ { 2 , 0 } ) = \hbar [ e ^ { 2 { t _ { 0 } } } \sin { t _ { 0 } } - 2 { w _ { 1 , 0 } } + 2 { w _ { 2 , 0 } } ] = - 0 . 0 4 , } \\ & { k _ { 2 , 1 } = \hbar { f _ { 1 } } \left( { t _ { 0 } } + \displaystyle \frac { { \hbar } } { 2 } , \boldsymbol { w } _ { 1 , 0 } + \displaystyle \frac { 1 } { 2 } { k _ { 1 , 1 } } , \boldsymbol { w } _ { 2 , 0 } + \displaystyle \frac { 1 } { 2 } { k _ { 1 , 2 } } \right) = \hbar [ \boldsymbol { w } _ { 2 , 0 } + \displaystyle \frac { 1 } { 2 } { k _ { 1 , 2 } } ] = - 0 . 0 6 ; } \\ & { k _ { 2 , 2 } = \hbar { f _ { 2 } } \left( { t _ { 0 } } + \displaystyle \frac { { \hbar } } { 2 } , \boldsymbol { w } _ { 1 , 0 } + \displaystyle \frac { 1 } { 2 } { k _ { 1 , 1 } } , \boldsymbol { w } _ { 2 , 0 } + \displaystyle \frac { 1 } { 2 } { k _ { 1 , 2 } } \right) } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \end{array}
$$

$$
\begin{array} { l } { { k _ { 3 , 1 } = h \left[ w _ { 2 , 0 } + \displaystyle \frac 1 2 k _ { 2 , 2 } \right] = - 0 . 0 6 1 6 2 8 3 2 2 3 8 , } } \\ { { k _ { 3 , 2 } = h \left[ e ^ { 2 ( t _ { 0 } + 0 . 0 5 ) } \sin ( t _ { 0 } + 0 . 0 5 ) - 2 \left( w _ { 1 , 0 } + \displaystyle \frac 1 2 k _ { 2 , 1 } \right) + 2 \left( w _ { 2 , 0 } + \displaystyle \frac 1 2 k _ { 2 , 2 } \right) \right] } } \\ { { ~ = - 0 . 0 3 1 5 2 4 0 9 2 3 7 , } } \\ { { k _ { 4 , 1 } = h \left[ w _ { 2 , 0 } + k _ { 3 , 2 } \right] = - 0 . 0 6 3 1 5 2 4 0 9 2 4 , } } \end{array}
$$

and

$$
k _ { 4 , 2 } = h \left[ e ^ { 2 ( t _ { 0 } + 0 . 1 ) } \sin ( t _ { 0 } + 0 . 1 ) - 2 ( w _ { 1 , 0 } + k _ { 3 , 1 } ) + 2 ( w _ { 2 , 0 } + k _ { 3 , 2 } ) \right] = - 0 . 0 2 1 7 8 6 3 7 2
$$

So

$$
\begin{array} { l } { { w _ { 1 , 1 } = w _ { 1 , 0 } + \displaystyle \frac { 1 } { 6 } ( k _ { 1 , 1 } + 2 k _ { 2 , 1 } + 2 k _ { 3 , 1 } + k _ { 4 , 1 } ) = - 0 . 4 6 1 7 3 3 4 2 3 } } \\ { { \displaystyle } } \\ { { w _ { 2 , 1 } = w _ { 2 , 0 } + \displaystyle \frac { 1 } { 6 } ( k _ { 1 , 2 } + 2 k _ { 2 , 2 } + 2 k _ { 3 , 2 } + k _ { 4 , 2 } ) = - 0 . 6 3 1 6 3 1 2 4 2 1 . } } \end{array}
$$

The value $w _ { 1 , 1 }$ approximates $u _ { 1 } ( 0 . 1 ) = y ( 0 . 1 ) = 0 . 2 e ^ { 2 ( 0 . 1 ) }$ (sin 0.1 - 2cos 0.1), and $w _ { 2 , 1 }$ approximates $u _ { 2 } ( 0 . 1 ) = y ^ { \prime } ( 0 . 1 ) = 0 . 2 e ^ { 2 ( 0 . 1 ) }$ (4 sin 0.1 - 3cos 0.1).

The set of values $w _ { 1 , j }$ and $w _ { 2 , j }$ ,for $j = 0 , 1 , \ldots , 1 0$ , obtained using the Runge-Kutta method of order four, are presented in Table 5.18 and are compared to the actual values of $u _ { 1 } ( t ) = 0 . 2 e ^ { 2 t } ( \sin t - 2 \cos t )$ and $u _ { 2 } ( t ) = u _ { 1 } ^ { \prime } ( t ) = 0 . 2 e ^ { 2 t } ( 4 \sin t - 3 \cos t )$ ·

Table 5.18   

<table><tr><td></td><td>y(tj）=u1(tj)</td><td>W1,j</td><td>y&#x27;(t）= u2(tj)</td><td>w2.j</td><td>ly(tj）-w1.jl</td><td>ly&#x27;(tj）-w2.jl</td></tr><tr><td>0.0</td><td>-0.40000000</td><td>-0.40000000</td><td>-6.0000000</td><td>-0.60000000</td><td>0</td><td>0</td></tr><tr><td>0.1</td><td>-0.46173297</td><td>-0.46173334</td><td>-0.6316304</td><td>-0.63163124</td><td>3.7× 10-7</td><td>7.75 × 10-7</td></tr><tr><td>0.2</td><td>-0.52555905</td><td>-0.52555988</td><td>-0.6401478</td><td>-0.64014895</td><td>8.3×10-7</td><td>1.01 × 10-6</td></tr><tr><td>0.3</td><td>-0.58860005</td><td>-0.58860144</td><td>-0.6136630</td><td>-0.61366381</td><td>1.39 ×10-6</td><td>8.34 × 10-7</td></tr><tr><td>0.4</td><td>-0.64661028</td><td>-0.64661231</td><td>-0.5365821</td><td>-0.53658203</td><td>2.03 × 10-6</td><td>1.79 ×10-7</td></tr><tr><td>0.5</td><td>-0.69356395</td><td>-0.69356666</td><td>-0.3887395</td><td>-0.38873810</td><td>2.71×10-6</td><td>5.96×10-7</td></tr><tr><td>0.6</td><td>-0.72114849</td><td>-0.72115190</td><td>-0.1443834</td><td>-0.14438087</td><td>3.41 × 10-6</td><td>7.75 × 10-7</td></tr><tr><td>0.7</td><td>-0.71814890</td><td>-0.71815295</td><td>0.2289917</td><td>0.22899702</td><td>4.05 × 10-6</td><td>2.03×10-6</td></tr><tr><td>0.8</td><td>-0.66970677</td><td>-0.66971133</td><td>0.7719815</td><td>0.77199180</td><td>4.56 × 10-6</td><td>5.30×10-6</td></tr><tr><td>0.9</td><td>-0.55643814</td><td>-0.55644290</td><td>1.534764</td><td>0.15347815</td><td>4.76 × 10-6</td><td>9.54× 10-6</td></tr><tr><td>1.0</td><td>--0.35339436</td><td>-0.35339886</td><td>2.578741</td><td>0.25787663</td><td>4.50 × 10-6</td><td>1.34 × 10-5</td></tr></table>

We can also use dsolve from Maple on higher-order equations. Note that the nth derivative $y ^ { ( n ) } ( t )$ is specified by $\left( \mathbb { D } \pmb { \mathfrak { Q } } \pmb { \mathfrak { Q } } \mathbf { \mathfrak { n } } \right) \left( \mathbf { y } \right) \left( \mathbf { t } \right)$ . To define the differential equation in Example 2, use

$$
{ \bf \gamma } \mathsf { d e f } 2 : = \left( \mathrm { D } \oplus \mathbb { Q } 2 \right) \left( \mathbf { y } \right) \left( \mathbf { t } \right) - 2 * \mathrm { D } \left( \mathbf { y } \right) \left( \mathbf { t } \right) + 2 * \mathbf { y } \left( \mathbf { t } \right) = \exp \left( 2 * \mathbf { t } \right) * \mathsf { s i n } \left( \mathbf { t } \right) ;
$$

and to specify the initial conditions use

$$
{ \bf >  i n i t 2 : = y \left( 0 \right) = - 0 \ . 4 , D \left( y \right) \left( 0 \right) = - 0 \ . 6 \ ; }
$$

The solution is obtained by the command

$$
> { \bf s } _ { 0 } 1 2 : = \mathrm { d } { \bf s } _ { 0 } { \bf l } \mathrm { v e } \left( \left\{ \tt d e f 2 , i n i t 2 \right\} , \mathrm { y ( t ) } \right) ;
$$

to obtain

$$
{ \mathsf { s o l } } 2 : = y ( t ) = - { \frac { 2 } { 5 } } e ^ { ( 2 t ) } \cos ( t ) + { \frac { 1 } { 5 } } e ^ { ( 2 t ) } \sin ( t )
$$

We isolate the solution in function form using

>g:=rhs(sol2);

To obtain $y ( 1 . 0 ) = g ( 1 . 0 )$ ,enter

>evalf(subs $\scriptstyle ( \mathtt { t } = 1 . 0 , \mathtt { g } ) ,$ ；

which gives the result -.3533943558.

Runge-Kutta-Fehlberg is also available for higher-order equations via the dsolve command with the numeric option. We enter the command

$$
{ \bf \gamma } > _ { \mathrm { g } } : = \mathtt { d } s \circ \mathrm { 2 } \mathrm { v e } \left( \left\{ \mathtt { d e f } 2 , \mathtt { i n i t } 2 \right\} , \mathrm { y ( t ) , n u m e r i c } \right) ;
$$

with the Maple response

$$
g : = \operatorname { p r o c } ( r k f 4 5 - x ) \dots \operatorname { e n d } \operatorname { p r o c }
$$

We can approximate y(1.O) using the command

${ \tt > } \tt { g } ( 1 . 0 ) ;$

to give

$$
\biggl [ t = 1 . 0 , y ( t ) = - . 3 5 3 3 9 4 3 4 6 8 0 7 5 3 4 6 7 6 , { \frac { \partial } { \partial t } } y ( t ) = 2 . 5 7 8 7 4 6 6 5 9 4 0 4 8 2 0 7 2 \biggr ]
$$

The other one-step methods can be extended to systems in a similar way. When error control methods like the Runge-Kutt-Fehlberg method are extended,each com-ponent of the numerical solution $( w _ { 1 j } , w _ { 2 j } , \dots , w _ { m j } )$ ）must be examined for accuracy. If any of the components fail to be sufficiently accurate, the entire numerical solution $( w _ { 1 j } , w _ { 2 j } , \dots , w _ { m j } )$ must be recomputed.

The multistep methods and predictor-corrector techniques can also be extended to systems. Again, if error control is used, each component must be accurate. The extension of the extrapolation technique to systems can also be done, but the notation becomes quite involved. If this topic is of interest,see [HNW1].

Convergence theorems and error estimates for systems are similar to those considered in Section 5.10 for the single equations, except that the bounds are given in terms of vector norms,a topic considered in Chapter 7. (A good reference for these theorems is [Ge1, pp. 45-72].)

1. Use the Runge-Kutta method for systems to approximate the solutions of the following systems of first-order differential equations,and compare the results to the actual solutions.

a. $u _ { 1 } ^ { \prime } = 3 u _ { 1 } + 2 u _ { 2 } - ( 2 t ^ { 2 } + 1 ) e ^ { 2 t } , \quad 0 \leq t \leq 1 , \quad u _ { 1 } ( 0 ) = 1 ;$ u=4u1+u2+(t²+2t-4)e²，0≤t≤1， $u _ { 2 } ( 0 ) = 1$ ： $h = 0 . 2$ ；actual solutions $\begin{array} { r } { u _ { 1 } ( t ) = \frac { 1 } { 3 } e ^ { 5 t } - \frac { 1 } { 3 } e ^ { - t } + e ^ { 2 t } } \end{array}$ and u2(t）=}e5+²e¹+t²e²1.   
b. $\begin{array} { r l } & { u _ { 1 } ^ { \prime } = - 4 u _ { 1 } - 2 u _ { 2 } + \cos { t } + 4 \sin { t } , \quad 0 \leq t \leq 2 , \quad u _ { 1 } ( 0 ) = 0 ; } \\ & { u _ { 2 } ^ { \prime } = 3 u _ { 1 } + u _ { 2 } - 3 \sin { t } , \quad 0 \leq t \leq 2 , \quad u _ { 2 } ( 0 ) = - 1 ; } \end{array}$ h = 0.1； actual solutions u1(t) = 2e-'-2e-2t +sint and u2(t)= -3e-'+2e-21.   
c. $\begin{array} { r l } & { u _ { 1 } ^ { \prime } = u _ { 2 } , \quad 0 \leq t \leq 2 , \quad u _ { 1 } ( 0 ) = 1 ; } \\ & { u _ { 2 } ^ { \prime } = - u _ { 1 } - 2 e ^ { t } + 1 , \quad 0 \leq t \leq 2 , \quad u _ { 2 } ( 0 ) = 0 ; } \\ & { u _ { 3 } ^ { \prime } = - u _ { 1 } - e ^ { t } + 1 , \quad 0 \leq t \leq 2 , \quad u _ { 3 } ( 0 ) = 1 ; } \end{array}$ $h = 0 . 5$ ；actual solutions $: u _ { 1 } ( t ) = \cos t + \sin t - e ^ { t } + 1 , \quad u _ { 2 } ( t ) = - \sin t + \cos t - e ^ { t } ,$ and $u _ { 3 } ( t ) = - \sin t + \cos t$   
d. $u _ { 1 } ^ { \prime } = u _ { 2 } - u _ { 3 } + t , \quad 0 \leq t \leq 1 , \quad u _ { 1 } ( 0 ) = 1 ;$ $u _ { 2 } ^ { \prime } = 3 t ^ { 2 } , \quad 0 \leq t \leq 1 , \quad u _ { 2 } ( 0 ) = 1 ;$ $u _ { 3 } ^ { \prime } = u _ { 2 } + e ^ { - t } , \quad 0 \le t \le 1 , \quad u _ { 3 } ( 0 ) = - 1 ;$ $h = 0 . 1$ ；actual solutions $u _ { 1 } ( t ) = - 0 . 0 5 t ^ { 5 } + 0 . 2 5 t ^ { 4 } + t + 2 - e ^ { - t } , \quad u _ { 2 } ( t ) = t ^ { 3 } + 1 ,$ and $u _ { 3 } ( t ) = 0 . 2 5 t ^ { 4 } + t - e ^ { - t }$ ，

2. Use the Runge-Kutta for Systems Algorithm to approximate the solutions of the following higher-order differential equations,and compare the results to the actual solutions.

a. $y ^ { \prime \prime } - 2 y ^ { \prime } + y = t e ^ { t } - t , \quad 0 \leq t \leq 1 , \quad y ( 0 ) = y ^ { \prime } ( 0 ) = 0 ,$ with $h = 0 . 1$ ；actual solution $y ( t ) = { \textstyle { \frac { 1 } { 6 } } } t ^ { 3 } e ^ { t } - t e ^ { t } + 2 e ^ { t } - t - 2$

b $t ^ { 2 } y ^ { \prime \prime } - 2 t y ^ { \prime } + 2 y = t ^ { 3 } \ln t$ $1 \leq t \leq 2$ ， $y ( 1 ) = 1$ ， $y ^ { \prime } ( 1 ) = 0$ ，with $h = 0 . 1$ ；actual solution $y ( t ) = { \textstyle { \frac { 7 } { 4 } } } t + { \textstyle { \frac { 1 } { 2 } } } t ^ { 3 } \ln t - { \textstyle { \frac { 3 } { 4 } } } t ^ { 3 }$   
c. $y ^ { \prime \prime \prime } + 2 y ^ { \prime \prime } - y ^ { \prime } - 2 y = e ^ { t }$ ， $0 \leq t \leq 3$ ， $y ( 0 ) = 1$ ， $y ^ { \prime } ( 0 ) = 2$ ， $y ^ { \prime \prime } ( 0 ) = 0$ ，with$h = 0 . 2$ actual solution $\begin{array} { r } { y ( t ) = \frac { 4 3 } { 3 6 } e ^ { t } + \frac { 1 } { 4 } e ^ { - t } - \frac { 4 } { 9 } e ^ { - 2 t } + \frac { 1 } { 6 } t e ^ { t } } \end{array}$   
d. $t ^ { 3 } y ^ { \prime \prime \prime } - t ^ { 2 } y ^ { \prime \prime } + 3 t y ^ { \prime } - 4 y = 5 t ^ { 3 } \ln t + 9 t ^ { 3 }$ ， $1 \ \leq \ t \ \leq \ 2 , \quad y ( 1 ) \ = \ 0 , \quad y ^ { \prime } ( 1 )$ 1， $y ^ { \prime \prime } ( 1 ) = 3$ ，with $h = 0 . 1$ ；actual solution $y ( t ) = - t ^ { 2 } + t \cos ( \ln t ) + t \sin ( \ln t ) +$ $t ^ { 3 } \ln t$

3. Change the Adams Fourth-Order Predictor-Corrector Algorithm to obtain approximate solutions to systems of first-order equations.

4.Repeat Exercise 1 using the algorithm developed in Exercise 3.

5.Repeat Exercise 2 using the algorithm developed in Exercise 3.

6. Suppose the swinging pendulum described in the lead example of this chapter is 2 ft long and that $g = 3 2 . 1 7$ ft $/ s ^ { 2 }$ .With $h = 0 . 1 \ \mathrm { s } ,$ compare the angle $\theta$ obtained for the following two initial-value problems:

$$
\begin{array} { l } { { \displaystyle { \frac { d ^ { 2 } \theta } { d t ^ { 2 } } + \frac { g } { L } \sin \theta = 0 , \quad \theta ( 0 ) = \frac { \pi } { 6 } , \quad \theta ^ { \prime } ( 0 ) = 0 , } } } \\ { { \displaystyle { \frac { d ^ { 2 } \theta } { d t ^ { 2 } } + \frac { g } { L } \theta = 0 , \quad \theta ( 0 ) = \frac { \pi } { 6 } , \quad \theta ^ { \prime } ( 0 ) = 0 , } } } \end{array}
$$

at $t = 0 , 1$ ,and $\textsf { 2 s }$

1. The study of mathematical models for predicting the population dynamics of competing species has its origin in independent works published in the early part of this century by A. J. Lotka and V. Volterra. Consider the problem of predicting the population of two species, one of which is a predator,whose population at time $t$ is $x _ { 2 } ( t )$ ,feeding on the other,which is the prey,whose population is $x _ { 1 } ( t )$ . We will assume that the prey always has an adequate food supply and that its birth rate at any time is proportional to the number of prey alive at that time; that is, birth rate (prey) is $k _ { 1 } x _ { 1 } ( t )$ . The death rate of the prey depends on both the number of prey and predators alive at that time.For simplicity,we assume death rate (prey) $= k _ { 2 } x _ { 1 } ( t ) x _ { 2 } ( t )$ .The birth rate of the predator, on the other hand, depends on its food supply, $x _ { 1 } ( t )$ ，as well as on the number of predators available for reproduction purposes. For this reason, we assume that the birth rate (predator) is $k _ { 3 } x _ { 1 } ( t ) x _ { 2 } ( t )$ . The death rate of the predator will be taken as simply proportional to the number of predators alive at the time; that is, death rate (predator) $) = k _ { 4 } x _ { 2 } ( t )$ ·

Since $x _ { 1 } ^ { \prime } ( t )$ and $x _ { 2 } ^ { \prime } ( t )$ represent the change in the prey and predator populations, respectively; with respect to time, the problem is expressed by the system of nonlinear diferential equations

$$
x _ { 1 } ^ { \prime } ( t ) = k _ { 1 } x _ { 1 } ( t ) - k _ { 2 } x _ { 1 } ( t ) x _ { 2 } ( t ) \quad \mathrm { a n d } \quad x _ { 2 } ^ { \prime } ( t ) = k _ { 3 } x _ { 1 } ( t ) x _ { 2 } ( t ) - k _ { 4 } x _ { 2 } ( t ) .
$$

Solve this system for $0 \leq t \leq 4$ ,assuming that the initial population of the prey is 1000 and of the predators is 5Oo and that the constants are $k _ { 1 } = 3$ ， $k _ { 2 } = 0 . 0 0 2$ ， $k _ { 3 } = 0 . 0 0 0 6$ ,and $k _ { 4 } = 0 . 5$ .Sketch a graph of the solutions to this problem, ploting both populations with time, and describe the physical phenomena represented. Is there a stable solution to this population model? If so, for what values $x _ { 1 }$ and $\pmb { x } _ { 2 }$ is the solution stable?

8. In Exercise 7 we considered the problem of predicting the population in a predator-prey model. Another problem of this type is concerned with two species competing for the same food supply. If the numbers of species alive at time $t$ are denoted by $x _ { 1 } ( t )$ and $x _ { 2 } ( t )$ , it is often assumed that, although the birth rate of each of the species is simply proportional to the number of species alive at that time,the death rate of each species depends on the population of both species. We will assume that the population of a particular pair of species is described by the

equations

$$
\frac { d x _ { 1 } ( t ) } { d t } = x _ { 1 } ( t ) \{ 4 - 0 . 0 0 0 3 x _ { 1 } ( t ) - 0 . 0 0 0 4 x _ { 2 } ( t ) \}
$$

and

$$
\frac { d x _ { 2 } ( t ) } { d t } = x _ { 2 } ( t ) [ 2 - 0 . 0 0 0 2 x _ { 1 } ( t ) - 0 . 0 0 0 1 x _ { 2 } ( t ) ] .
$$

If it is known that the initial population of each species is 1O,ooo,find the solution to this system for $0 \leq t \leq 4$ . Is there a stable solution to this population model? If so, for what values of $x _ { 1 }$ and $\pmb { x _ { 2 } }$ is the solution stable?

# 5.10 Stability

A number of methods have been presented in this chapter for approximating the solution to an initial-value problem. Although numerous other techniques are available,we have chosen the methods described here because they generally satisfied three criteria:

1. Their development is clear enough so that you can understand how and why they work.   
2. One or more of the methods will give satisfactory results for most of the problems that are encountered by students in science and engineering.   
3. Most of the more advanced and complex techniques are based on one or a combination of the procedures described here.

In this section, we discuss why these methods give satisfactory results when some similar methods do not. Before we begin this discussion, we need to present two definitions concerned with the convergence of one-step difference-equation methods to the solution of the differential equation as the step size decreases.

# Definition 5.18

A one-step difference-equation method with local truncation error $\tau _ { i } ( h )$ at the ith step is said to be consistent with the differential equation it approximates if

$$
\operatorname* { l i m } _ { h \to 0 } \operatorname* { m a x } _ { 1 \leq i \leq N } \left. \tau _ { i } ( h ) \right. = 0 .
$$

Note that this definition is a local definition since, for each of the values $\tau _ { i } ( h )$ ，we are assuming that the approximation wi-1 and the exact solution y(ti-1） are the same. A more realistic means of analyzing the effects of making $h$ small is to determine the global effect of the method. This is the maximum error of the method over the entire range of the approximation,assuming only that the method gives the exact result at the initial value.

# Definition 5.19

9A one-step difference-equation method is said to be convergent with respect to the differential equation it approximates if

$$
\operatorname* { l i m } _ { h \to 0 } \operatorname* { m a x } _ { 1 \le i \le N } | w _ { i } - y ( t _ { i } ) | = 0 ,
$$

where $y _ { i } = y ( t _ { i } )$ denotes the exact valueof the solution of the diferential equation and $w _ { i }$ is the approximation obtained from the diffrence method at the ith step.

Examining Inequality (5.1O) of Section 5.2 in the error-bound formula for Euler's method, it can be said that under the hypotheses of Theorem 5.9,

$$
\operatorname* { m a x } _ { 1 \leq i \leq N } | w _ { i } - y ( t _ { i } ) | \leq \frac { M h } { 2 L } | e ^ { L ( b \sim a ) } - 1 | .
$$

So Euler's method isconvergent with respect to a differential equationsatisfying the conditions of this definition, and the rate of convergence is $O ( h )$

A one-step method is consistent precisely when the difference equation for the method approaches the differential equation when the step size goes to zero; that is, the local truncation error approaches zero as the step size approaches zero. The definition of convergence has a similar connotation. A method is convergent precisely when the solution to the difference equation approaches the solution to the differential equation as the step size goes to zero.

The other error-bound type of problem that exists when using difference methods to approximate solutions to differential equations is a consequence of not using exact results. In practice, neither the initial conditions nor the arithmetic that is subsequently performed is represented exactly because of the roundoff error associated with finite-digit arithmetic. In Section 5.2 we saw that this consideration can lead to diffculties even for the convergent Euler's method. To analyze this situation, at least partially, we will try to determine which methods are stable,in the sense that smallchanges or perturbations in the initial conditions produce correspondingly small changes in the subsequent approximations; that is,a stable method is one whose results depend continuously on the initial data.

Since the concept of stability of a one-step difference equation is somewhat analogous to the condition of a differential equation being well-posed, it is not surprising that the Lipschitz condition appears here,as it did in the corresponding theorem for differential equations, Theorem 5.6.

Part (i) of the following theorem concerns the stability of a one-step method. The proof of this result is not difficult and is considered in Exercise 1. Part (ii) of Theorem 5.20 concerns sufficient conditions for a consistent method to be convergent. Part (iii) justifies the remark made in Section 5.5 about controlling the global error of a method by controlling its local truncation error and implies that when the local truncation error has the rate of convergence $O ( h ^ { n } )$ , the global error will have the same rate of convergence. The proofs of parts (ii) and (ii) are more difficult than that of part (i),and can be found within the material presented in [Gel, pp.57-58].

Theorem 5.20 Suppose the initial-value problem

$$
y ^ { \prime } = f ( t , y ) , \quad a \leq t \leq b , \quad y ( a ) = \alpha ,
$$

is approximated by a one-step difference method in the form

$$
\begin{array} { r c l } { { } } & { { } } & { { w _ { 0 } = \alpha , } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { w _ { i + 1 } = w _ { i } + h \phi ( t _ { i } , w _ { i } , h ) . } } \end{array}
$$

Suppose also that a number $h _ { 0 } > 0$ exists and that $\phi ( t , w , h )$ is continuous and satisfies a Lipschitz condition in the variable $w$ with Lipschitz constant $L$ on the set

$$
D = \{ ( t , w , h ) \mid a \leq t \leq b , - \infty < w < \infty , 0 \leq h \leq h _ { 0 } \} .
$$

Then

(i) The method is stable;   
(ii) The diference method is convergent if and only if it is consistent, which is equivalent to

$$
\phi ( t , y , 0 ) = f ( t , y ) , \quad \mathrm { f o r \ a l l } \ a \leq t \leq b ;
$$

(ii)If a function $\tau$ exists and, for each $i = 1 , 2 , \dots , N$ , the local truncation error $\tau _ { i } ( h )$ satisfies $| \tau _ { i } ( h ) | \leq \tau ( h )$ whenever $0 \leq h \leq h _ { 0 } .$ then

$$
| y ( t _ { i } ) - w _ { i } | \leq \frac { \tau ( h ) } { L } e ^ { L ( t _ { i } - a ) } .
$$

Consider the Modified Euler method given by

$$
w _ { i + 1 } = w _ { i } + { \frac { h } { 2 } } \left[ f ( t _ { i } , w _ { i } ) + f ( t _ { i + 1 } , w _ { i } + h f ( t _ { i } , w _ { i } ) ) \right] , \quad { \mathrm { f o r ~ } } i = 0 , 1 , \dots , N - 1 .
$$

We will verify that this method satisfies the hypothesis of Theorem 5.2O.For this method,

$$
\phi ( t , w , h ) = \frac { 1 } { 2 } f ( t , w ) + \frac { 1 } { 2 } f ( t + h , w + h f ( t , w ) ) .
$$

f $f$ satisfies a Lipschitz condition on $\{ ( t , w ) \mid a \leq t \leq b , - \infty < w < \infty \}$ in the variable $w$ with constant $L$ , then, since

$$
\begin{array} { l } { \displaystyle { \phi ( t , w , h ) - \phi ( t , \overline { { { w } } } , h ) = \frac { 1 } { 2 } f ( t , w ) + \frac { 1 } { 2 } f ( t + h , w + h f ( t , w ) ) } } \\ { \displaystyle { \qquad - \frac { 1 } { 2 } f ( t , \overline { { { w } } } ) - \frac { 1 } { 2 } f ( t + h , \overline { { { w } } } + h f ( t , \overline { { { w } } } ) ) , } } \end{array}
$$

the Lipschitz condition on $f$ leads to

$$
\begin{array} { l } { \displaystyle | \phi ( t , w , h ) - \phi ( t , \overline { { w } } , h ) | \leq \frac 1 2 L | w - \overline { { w } } | + \frac 1 2 L | w + h f ( t , w ) - \overline { { w } } - h f ( t , \overline { { w } } ) | } \\ { \displaystyle \qquad \leq L | w - \overline { { w } } | + \frac 1 2 L | h f ( t , w ) - h f ( t , \overline { { w } } ) | } \\ { \displaystyle \qquad \leq L | w - \overline { { w } } | + \frac 1 2 h L ^ { 2 } | w - \overline { { w } } | } \\ { \displaystyle \qquad = \bigg ( L + \frac 1 2 h L ^ { 2 } \bigg ) | w - \overline { { w } } | . } \end{array}
$$

Therefore, $\phi$ satisfies a Lipschitz condition in $\pmb { w }$ on the set

$$
\{ ( t , w , h ) \mid a \leq t \leq b , - \infty < w < \infty , 0 \leq h \leq h _ { 0 } \} ,
$$

for any $h _ { 0 } > 0$ with constant

$$
L ^ { \prime } = L + { \frac { 1 } { 2 } } h _ { 0 } L ^ { 2 } .
$$

Finally, if $f$ is continuous on $\{ ( t , w ) \ | \ a \ \leq \ t \ \leq \ b , - \infty \ < \ w \ < \ \infty \}$ ,then $\phi$ is continuous on

$$
\{ ( t , w , h ) \mid a \leq t \leq b , - \infty < w < \infty , 0 \leq h \leq h _ { 0 } \} ;
$$

so Theorem 5.20 implies that the Modified Euler method is stable.Letting $h = 0$ , we have

$$
\phi ( t , w , 0 ) = \frac { 1 } { 2 } f ( t , w ) + \frac { 1 } { 2 } f ( t + 0 , w + 0 \cdot f ( t , w ) ) = f ( t , w ) ,
$$

so the consistency condition expressed in Theorem 5.20,part (ii), holds.Thus,the method is convergent. Moreover, we have seen that for this method the local truncation error is $O ( h ^ { 2 } )$ , so the convergence of the Modified Euler method is also $O ( h ^ { 2 } )$

For multistep methods, the problems involved with consistency,convergence,and stability are compounded because of the number of approximations involved at each step. In the one-step methods, the approximation $w _ { i + 1 }$ depends directly only on the previous approximation ${ \boldsymbol { w } } _ { i }$ , whereas the multistep methods use at least two of the previous approximations,and the usual methods that are employed involve more.

The general multistep method for approximating the solution to the initial-value problem

$$
y ^ { \prime } = f ( t , y ) , \quad a \leq t \leq b , \quad y ( a ) = \alpha ,
$$

can be written in the form

$$
\begin{array} { r l } & { w _ { 0 } = \alpha , \quad w _ { 1 } = \alpha _ { 1 } , \quad \ldots , w _ { m - 1 } = \alpha _ { m - 1 } , } \\ & { } \\ & { v _ { i + 1 } = a _ { m - 1 } w _ { i } + a _ { m - 2 } w _ { i - 1 } + \ldots + a _ { 0 } w _ { i + 1 - m } + h F ( t _ { i } , h , w _ { i + 1 } , w _ { i } , \ldots , w _ { i + 1 - m } ) , } \end{array}
$$

for each $i = m - 1 , m , \dots , N - 1$ , where $a _ { 0 } , a _ { 1 } , \ldots , a _ { m + 1 }$ are constants and, as usual, $h = ( b - a ) / N$ and $t _ { i } = a + i h$

The local truncation error for a multistep method expressed in this form is

$$
\begin{array} { r } { \tau _ { i + 1 } ( h ) = \frac { y ( t _ { i + 1 } ) - a _ { m - 1 } y ( t _ { i } ) - \dots - a _ { 0 } y ( t _ { i + 1 - m } ) } { h } } \\ { - F ( t _ { i } , h , y ( t _ { i + 1 } ) , y ( t _ { i } ) , \dots , y ( t _ { i + 1 - m } ) ) , } \end{array}
$$

for each $i \ = \ m - 1 , m , \ldots , N - 1$ . As in the one-step methods,the local truncation error measures how the solution $y$ to the differential equation fails to satisfy the difference equation.

For the four-step Adams-Bashforth method, we have seen that

$$
\tau _ { i + 1 } ( h ) = \frac { 2 5 1 } { 7 2 0 } y ^ { ( 5 ) } ( \mu _ { i } ) h ^ { 4 } , \quad \mathrm { f o r ~ s o m e } \ \mu _ { i } \in ( t _ { i - 3 } , t _ { i + 1 } ) ,
$$

whereas the three-step Adams-Moulton method has

$$
\tau _ { i + 1 } ( h ) = - \frac { 1 9 } { 7 2 0 } y ^ { ( 5 ) } ( \mu _ { i } ) h ^ { 4 } , \quad \mathrm { f o r ~ s o m e } \ \mu _ { i } \in ( t _ { i - 2 } , t _ { i + 1 } ) ,
$$

provided,of course, that $y \in C ^ { 5 } [ a , b ]$

Throughout the analysis, two assumptions willbe made concerning the function $F$

1.If $f \equiv 0$ (that is,if the differential equation is homogeneous), then ${ \pmb F } \equiv { \bf 0 }$ also.

2. $F$ satisfies a Lipschitz condition with respect to $\{ w _ { j } \}$ , in the sense that a constant $L$ exists and, for every pair of sequences $\{ v _ { j } \} _ { j = 0 } ^ { N }$ and $\{ \tilde { v } _ { j } \} _ { j = 0 } ^ { N }$ and for $i = m - 1$ ， $m , \ldots , N - 1$ , we have

$$
| F ( t _ { i } , h , v _ { i + 1 } , \ldots , v _ { i + 1 - m } ) - F ( t _ { i } , h , \tilde { v } _ { i + 1 } , \ldots , \tilde { v } _ { i + 1 - m } ) | \leq L \sum _ { j = 0 } ^ { m } | v _ { i + 1 - j } - \tilde { v } _ { i + 1 - j } | .
$$

The explicit Adams-Bashforth and implicit Adams-Moulton methods satisfy both of these conditions, provided $f$ satisfies a Lipschitz condition. (See Exercise 2.)

The concept of convergence for multistep methods is the same as that for one-step methods; a multistep method is convergent if the solution to the difference equation approaches the solution to the differential equation as the step size approaches zero. This means that $\begin{array} { r } { \operatorname* { l i m } _ { h  0 } \operatorname* { m a x } _ { 0 \leq i \leq N } \mid w _ { i } - y ( t _ { i } ) \mid = 0 . } \end{array}$

For consistency, however, a slightly different situation occurs. Again, we want a multistep method to be consistent provided that the difference equation approaches the differential equation as the step size approaches zero; that is,the local truncation error approaches zero at each step as the step size approaches zero.The additional condition occurs because of the number of starting values required for multistep methods. Since usually only the first starting value, $w _ { 0 } = \alpha$ , is exact, we need to require that the errors in all the starting values $\left\{ \alpha _ { i } \right\}$ approach zero as the step size approaches zero. So, both

$$
\begin{array} { r l l } { \underset { h  0 } { \operatorname* { l i m } } | \tau _ { i } ( h ) | = 0 , } & { \mathrm { ~ f o r ~ a l l ~ } i = m , m + 1 , \ldots , N } & { \mathrm { ~ a n d ~ } } \\ { \underset { h  0 } { \operatorname* { l i m } } | \alpha _ { i } - y ( t _ { i } ) | = 0 , } & { \mathrm { ~ f o r ~ a l l ~ } i = 1 , 2 , \ldots , m - 1 , } \end{array}
$$

must be true for a multistep method in the form (5.54) to be consistent. Note that (5.56) im-plies that a multistep method will not be consistent unless the one-step method generating the starting values is also consistent.

The following theorem for multistep methods is similar to Theorem 5.20, part (iii), and gives a relationship between the local truncation error and global error of a multistep method. It provides the theoretical justification for attempting to control global error by controlling local truncation error. The proof of a slightly more general form of this theorem can be found in [IK, pp. 387-388].

Suppose the initial-value problem

$$
y ^ { \prime } = f ( t , y ) , \quad a \leq t \leq b , \quad y ( a ) = \alpha ,
$$

is approximated by an explicit Adams predictor-corrector method with an m-step Adams-Bashforth predictor equation

$$
w _ { i + 1 } = w _ { i } + h [ b _ { m - 1 } f ( t _ { i } , w _ { i } ) + \cdot \cdot \cdot + b _ { 0 } f ( t _ { i + 1 - m } , w _ { i + 1 - m } ) ] ,
$$

with local truncation error $\tau _ { i + 1 } ( h )$ ,and an $( m - 1 )$ -step implicit Adams-Moulton corrector equation

$$
w _ { i + 1 } = w _ { i } + h \left\{ \tilde { b } _ { m - 1 } f ( t _ { i } , w _ { i + 1 } ) + \tilde { b } _ { m - 2 } f ( t _ { i } , w _ { i } ) + \cdots + \tilde { b } _ { 0 } f ( t _ { i + 2 - m } , w _ { i + 2 - m } ) \right\} ,
$$

with local truncation error $\widetilde { \tau } _ { i + 1 } \left( h \right)$ . In addition, suppose that $f ( t , y )$ and $f _ { y } ( t , y )$ are continuous on $D = \{ ( t , y ) \mid a \leq t \leq b$ and $- \infty < y < \infty \}$ and that $f _ { y }$ is bounded. Then the local truncation error $\sigma _ { i + 1 } ( h )$ of the predictor-corrector method is

$$
\sigma _ { i + 1 } ( h ) = \tilde { \tau } _ { i + 1 } ( h ) + \tau _ { i + 1 } \tilde { b } _ { m - 1 } \frac { \partial f } { \partial y } ( t _ { i + 1 } , \theta _ { i + 1 } ) ,
$$

where $\theta _ { i + 1 }$ is a number between zero and $h \tau _ { i + 1 } ( h )$

Moreover, there exist constants $k _ { 1 }$ and $k _ { 2 }$ such that

$$
| w _ { i } - y ( t _ { i } ) | \leq \left[ \operatorname* { m a x } _ { 0 \leq j \leq m - 1 } \left| w _ { j } - y ( t _ { j } ) \right| + k _ { 1 } \sigma ( h ) \right] e ^ { k _ { 2 } ( t _ { i } - a ) } ,
$$

where $\sigma ( h ) = \operatorname* { m a x } _ { m \leq j \leq N } | \sigma _ { j } ( h ) |$

Before discussing connections between consistency, convergence, and stability for multistep methods, we need to consider in more detail the difference equation for a multistep method. In doing so, we will discover the reason for choosing the Adams methods as our standard multistep methods.

Associated with the difference equation (5.54) given at the beginning of this discussion,

$$
\begin{array} { r l } & { w _ { 0 } = \alpha , \ w _ { 1 } = \alpha _ { 1 } , \ \ldots , \ w _ { m - 1 } = \alpha _ { m - 1 } , } \\ & { w _ { i + 1 } = a _ { m - 1 } w _ { i } + a _ { m - 2 } w _ { i - 1 } + \cdot \cdot \cdot + a _ { 0 } w _ { i + 1 - m } + h F ( t _ { i } , h , w _ { i + 1 } , w _ { i } , \ldots , w _ { i + 1 - m } ) , } \end{array}
$$

is a polynomial, called the characteristic polynomial of the method, given by

$$
P ( \lambda ) = \lambda ^ { m } - a _ { m - 1 } \lambda ^ { m - 1 } - a _ { m - 2 } \lambda ^ { m - 2 } - \cdots - a _ { 1 } \lambda - a _ { 0 } .
$$

The stability of a multistep method with respect to roundoff error is dictated the by magnitudes of the zeros of the characteristic polynomial. To see this,consider applying the standard multistep method (5.54) to the trivial initial-value problem

$$
y ^ { \prime } \equiv 0 , \quad y ( a ) = \alpha , \quad \mathrm { w h e r e } \ : \alpha \neq 0 .
$$

This problem has exact solution $y ( t ) \equiv \alpha$ . By examining Eqs. (5.26) and (5.27) in Section 5.6, we can see that any multistep method will, in theory, produce the exact solution $w _ { n } =$

$\pmb { \alpha }$ for all $n$ . The only deviation from the exact solution is due to the roundoff error of the method.

The right side of the differential equation in (5.58) has $f ( t , y ) \equiv 0$ ,so by assumption (1), we have $F ( t _ { i } , h , w _ { i + 1 } , w _ { i + 2 } , \dots , w _ { i + 1 - m } ) = 0$ in the difference equation (5.54). As a consequence,the standard form.of the difference equation becomes

$$
w _ { i + 1 } = a _ { m - 1 } w _ { i } + a _ { m - 2 } w _ { i - 1 } + \cdot \cdot \cdot + a _ { 0 } w _ { i + 1 - m } .
$$

Suppose $\lambda$ is one of the zeros of the characteristic polynomial associated with (5.54). Then $w _ { n } = \lambda ^ { n }$ for each $\pmb { n }$ is a solution to (5.59) since

$$
\iota ^ { i + 1 } - a _ { m - 1 } \lambda ^ { i } - a _ { m - 2 } \lambda ^ { i - 1 } - \cdot \cdot \cdot - a _ { 0 } \lambda ^ { i + 1 - m } = \lambda ^ { i + 1 - m } \{ \lambda ^ { m } - a _ { m - 1 } \lambda ^ { m - 1 } - \cdot \cdot \cdot - a _ { 0 } \}
$$

In fact, if $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { m }$ are distinct zeros of the characteristic polynomial for (5.54), it can be shown that every solution to (5.59) can be expressed in the form

$$
w _ { n } = \sum _ { i = 1 } ^ { m } c _ { i } \lambda _ { i } ^ { n } ,
$$

for some unique collection of constants $c _ { 1 } , c _ { 2 } , \ldots , c _ { m }$

Since the exact solution to (5.58） is $y ( t ) = \alpha$ ，the choice $w _ { n } \ = \alpha$ , for all $\pmb { n }$ ,is a solution to (5.59). Using this fact in (5.59) gives

$$
0 = \alpha - \alpha a _ { m - 1 } - \alpha a _ { m - 2 } - \cdot \cdot \cdot - \alpha a _ { 0 } = \alpha [ 1 - a _ { m - 1 } - a _ { m - 2 } - \cdot \cdot \cdot - a _ { 0 } ] .
$$

This implies that $\lambda = 1$ is one of the zeros of the characteristic polynomial (5.57). We will assume that in the representation (5.6O) this solution is described by $\lambda _ { 1 } = 1$ and $c _ { 1 } = \alpha$ ， so all solutions to (5.59) are expressed as

$$
w _ { n } = \alpha + \sum _ { i = 2 } ^ { m } c _ { i } \lambda _ { i } ^ { n } .
$$

If all the calculations were exact, allthe constants $c _ { 2 } , c _ { 3 } , \ldots , c _ { m }$ would be zero. In practice, the constants $c _ { 2 } , c _ { 3 } , \ldots , c _ { m }$ are not zero due to roundoff error. In fact, the roundoff error grows exponentially unless $| \lambda _ { i } | \leq 1$ for each of the roots $\lambda _ { 2 } , \lambda _ { 3 } , \ldots , \lambda _ { m }$ . The smaller the magnitude of these roots,the more stable the method with respect to the growth of roundoff error.

In deriving (5.61),we made the simplifying assumption that the zeros of the characteristic polynomial are distinct. The situation is similar when multiple zeros occur. For example, if $\lambda _ { k } = \lambda _ { k + 1 } = \cdot \cdot \cdot = \lambda _ { k + p }$ for some $k$ and $p$ , it simply requires replacing the sum

$$
c _ { k } \lambda _ { k } ^ { n } + c _ { k + 1 } \lambda _ { k + 1 } ^ { n } + \cdot \cdot \cdot + c _ { k + p } \lambda _ { k + p } ^ { n }
$$

in (5.61) with

$$
c _ { k } \lambda _ { k } ^ { n } + c _ { k + 1 } n \lambda _ { k } ^ { n - 1 } + c _ { k + 2 } n ( n - 1 ) \lambda _ { k } ^ { n - 2 } + \cdot \cdot \cdot + c _ { k + p } [ n ( n - 1 ) \cdot \cdot \cdot ( n - p + 1 ) ] \lambda _ { k } ^ { n - p }
$$

(See [He2,pp.119-145].) Although the form of the solution is modified,the roundoff error if $| \lambda _ { k } | > 1$ still grows exponentially.

Although we have considered only the special case of approximating initial-value problems of the form (5.58),the stability characteristics for this equation determine the stability for the situation when $f ( t , y )$ is not identically zero. This is because the solution to the homogeneous equation (5.58) is embedded in the solution to any equation. The following definitions are motivated by this discussion.

Definition 5.22 Let $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { m }$ denote the (not necessarily distinct) roots of the characteristic equation

$$
P ( \lambda ) = \lambda ^ { m } - a _ { m - 1 } \lambda ^ { m - 1 } - \cdot \cdot \cdot - a _ { 1 } \lambda - a _ { 0 } = 0
$$

associated with the multistep difference method

$$
w _ { 0 } = \alpha , \quad w _ { 1 } = \alpha _ { 1 } , \quad \ldots , \quad w _ { m - 1 } = \alpha _ { m - 1 }
$$

and

$$
w _ { i + 1 } = a _ { m - 1 } w _ { i } + a _ { m - 2 } w _ { i - 1 } + \cdot \cdot \cdot + a _ { 0 } w _ { i + 1 - m } + h F ( t _ { i } , h , w _ { i + 1 } , w _ { i } , \ldots , w _ { i + 1 - m } ) .
$$

If $| \lambda _ { i } | \leq 1$ ,for each $i = 1 , 2 , \dots , m$ ,and all roots with absolute value 1 are simple roots, then the difference method is said to satisfy the root condition.

# Definition 5.23

(i) Methods that satisfy the root condition and have $\lambda = 1$ as the only root of the characteristic equation of magnitude one are called strongly stable.   
(ii) Methods that satisfy the root condition and have more than one distinct root with magnitude one are called weakly stable.   
(iii) Methods that do not satisfy the root condition are called unstable.

Consistency and convergence of a multistep method are closely related to the roundoff stability of the method. The next theorem details these connections. For the proof of this result and the theory on which it is based, see [IK, pp. 410-417].

# Theorem 5.24

A multistep method of the form

$$
w _ { 0 } = \alpha , \quad w _ { 1 } = \alpha _ { 1 } , \quad \textrm { . . . , } \quad w _ { m - 1 } = \alpha _ { m - 1 } ,
$$

where

$$
w _ { i + 1 } = a _ { m - 1 } w _ { i } + a _ { m - 2 } w _ { i - 1 } + \cdot \cdot \cdot + a _ { 0 } w _ { i + 1 - m } + h F ( t _ { i } , h , w _ { i + 1 } , w _ { i } , \ldots , w _ { i + 1 - m } )
$$

is stable if and only if it satisfies the root condition. Moreover, if the difference method is consistent with the differential equation,then the method is stable if and only if it is convergent.

# EXAMPLE 2

We have seen that the fourth-order Adams-Bashforth method can be expressed as

$$
w _ { i + 1 } = w _ { i } + h F ( t _ { i } , h , w _ { i + 1 } , w _ { i } , \dots , w _ { i - 3 } ) ,
$$

where

$$
\begin{array} { r l } & { F ( t _ { i } , h , w _ { i + 1 } , w _ { i } , \dotsc , w _ { i - 3 } ) = \displaystyle \frac { h } { 2 4 } [ 5 5 f ( t _ { i } , w _ { i } ) - 5 9 f ( t _ { i - 1 } , w _ { i - 1 } ) } \\ & { \qquad + 3 7 f ( t _ { i - 2 } , w _ { i - 2 } ) - 9 f ( t _ { i - 3 } , w _ { i - 3 } ) ] ; } \end{array}
$$

s0 $m = 4 , a _ { 0 } = 0 , a _ { 1 } = 0 , a _ { 2 } = 0 ,$ and $a _ { 3 } = 1$

The characteristic equation for this Adams-Bashforth method is,consequently,

$$
0 = P ( \lambda ) = \lambda ^ { 4 } - \lambda ^ { 3 } = \lambda ^ { 3 } ( \lambda - 1 ) ,
$$

which has roots $\lambda _ { 1 } = 1 , \lambda _ { 2 } = 0 , \lambda _ { 3 } = 0$ and $\lambda _ { 4 } = 0$ . It satisfies the root condition and is strongly stable.

The Adams-Moulton method has a similar characteristic polynomial, $P ( \lambda ) = \lambda ^ { 3 } - \lambda ^ { 2 } .$ with zeros $\lambda _ { 1 } = 1 , \lambda _ { 2 } = 0$ ,and $\lambda _ { 3 } = 0$ ,and is also strongly stable. ■

The explicit multistep method given by

$$
w _ { i + 1 } = w _ { i - 3 } + { \frac { 4 h } { 3 } } \left[ 2 f ( t _ { i } , w _ { i } ) - f ( t _ { i - 1 } , w _ { i - 1 } ) + 2 f ( t _ { i - 2 } , w _ { i - 2 } ) \right]
$$

was introduced in Section 5.6 as the fourth-order Milne's method. Since the characteristic equation for this method, $0 = P ( \lambda ) = \lambda ^ { 4 } - 1$ ,has four roots with magnitude one: $\lambda _ { 1 } = 1$ ， $\lambda _ { 2 } = - 1 , \lambda _ { 3 } = i$ ，and $\lambda _ { 4 } = - i$ , the method satisfies the root condition, but it is only weakly stable.

Consider the initial-value problem

$$
y ^ { \prime } = - 6 y + 6 , \quad 0 \leq t \leq 1 , \quad y ( 0 ) = 2 ,
$$

which has the exact solution $y ( t ) = 1 + e ^ { - 6 t }$ . For comparison purposes, the strongly stable fourth-order Adams-Bashforth method and the weakly stable Milne's method are used to approximate the solution to this problem with $h = 0 . 1$ , with exact values for the starting values. The results in Table 5.19 show the effects of a weakly stable method versus a strongly stable method for this problem.

Table 5.19   

<table><tr><td></td><td>Exact y(ti）</td><td>Adams-Bashforth Method</td><td>Error lyi-wi</td><td>Milne&#x27;s Method Wi</td><td>Error lyi-wil</td></tr><tr><td>t 0.10000000</td><td></td><td>Wi 1.5488116</td><td></td><td>1.5488116</td><td></td></tr><tr><td>0.20000000</td><td></td><td>1.3011942</td><td></td><td>1.3011942</td><td></td></tr><tr><td>0.30000000</td><td></td><td>1.1652989</td><td></td><td>1.1652989</td><td></td></tr><tr><td>0.40000000</td><td>1.0907180</td><td>1.0996236</td><td>8.906× 10-3</td><td>1.0983785</td><td>7.661 × 10-3</td></tr><tr><td>0.50000000</td><td>1.0497871</td><td>1.0513350</td><td>1.548 × 10-3</td><td>1.0417344</td><td>8.053×10-3</td></tr><tr><td>0.60000000</td><td>1.0273237</td><td>1.0425614</td><td>1.524 × 10-2</td><td>1.0486438</td><td>2.132 ×10-2</td></tr><tr><td>0.70000000</td><td>1.0149956</td><td>1.0047990</td><td>1.020 × 10-2</td><td>0.9634506</td><td>5.154 ×10-2</td></tr><tr><td>0.80000000</td><td>1.0082297</td><td>1.0359090</td><td>2.768 × 10-2</td><td>1.1289977</td><td>1.208× 10-1</td></tr><tr><td>0.90000000</td><td>1.0045166</td><td>0.9657936</td><td>3.872 ×10-2</td><td>0.7282684</td><td>2.762 × 10-1</td></tr><tr><td>1.00000000</td><td>1.0024788</td><td>1.0709304</td><td>6.845 × 10-2</td><td>1.6450917</td><td>6.426 × 10-1</td></tr></table>

The reason for choosing the Adams-Bashforth-Moulton as our standard fourth-order predictor-corrector technique in Section 5.6 over the Milne-Simpson method of the same order is that both the Adams-Bashforth and Adams-Moulton methods are strongly stable. They are more likely to give accurate approximations to a wider class of problems than is the predictor-corrector based on the Milne and Simpson techniques, both of which are weakly stable. □

# ExeRcise SEt 5.10

1.To prove Theorem 5.20,part (i),show that the hypotheses imply that there exists a constant $K > 0$ such that

$$
| u _ { i } - v _ { i } | \leq K | u _ { 0 } - v _ { 0 } | , \quad \mathrm { f o r e a c h } \ 1 \leq i \leq N ,
$$

whenever $\{ u _ { i } \} _ { i = 1 } ^ { N }$ and $\{ v _ { i } \} _ { i = 1 } ^ { N }$ satisfy the difference equation $w _ { i + 1 } = w _ { i } + h \phi ( t _ { i } , w _ { i } , h )$

2.For the Adams-Bashforth and Adams-Moulton methods of order four,

a. Show that if $f = 0$ ,then

$$
F ( t _ { i } , h , w _ { i + 1 } , \ldots , w _ { i + 1 - m } ) = 0 .
$$

b.Show that if $f$ satisfies a Lipschitz condition with constant $L$ , then a constant $C$ exists with

$$
| F ( t _ { i } , h , w _ { i + 1 } , \ldots , w _ { i + 1 - m } ) - F ( t _ { i } , h , v _ { i + 1 } , \ldots , v _ { i + 1 - m } ) | \leq C \sum _ { j = 0 } ^ { m } | w _ { i + 1 - j } - \nu _ { i + 1 - j } | .
$$

3.Use the results of Exercise 17 in Section 5.4 to show that the Runge-Kuta method of order four is consistent.

4. Consider the differential equation

$$
y ^ { \prime } = f ( t , y ) , \quad a \leq t \leq b , \quad y ( a ) = \alpha .
$$

a. Show that

$$
y ^ { \prime } ( t _ { i } ) = { \frac { - 3 y ( t _ { i } ) + 4 y ( t _ { i + 1 } ) - y ( t _ { i + 2 } ) } { 2 h } } + { \frac { h ^ { 2 } } { 3 } } y ^ { \prime \prime \prime } ( \xi _ { 1 } ) ,
$$

for some $\pmb { \xi }$ ， where $t _ { i } < \xi _ { i } < t _ { i + 2 }$

b.Part (a) suggests the difference method

$$
w _ { i + 2 } = 4 w _ { i + 1 } - 3 w _ { i } - 2 h f ( t _ { i } , w _ { i } ) , \quad \mathrm { f o r } i = 0 , 1 , \ldots , N - 2 ,
$$

Use this method to solve

$$
y ^ { \prime } = 1 - y , \quad 0 \leq t \leq 1 , \quad y ( 0 ) = 0 ,
$$

with $h = 0 . 1$ . Use the starting values ${ w _ { 0 } } = 0$ and $w _ { 1 } = y ( t _ { 1 } ) = 1 - e ^ { - 0 . 1 }$

c.Repeat part (b) with $\pmb { h } = \mathbf { 0 . 0 1 }$ and $w _ { 1 } = 1 - e ^ { - 0 . 0 1 }$ ，

d.Analyze this method for consistency,stability,and convergence.

5. Given the multistep method

$$
w _ { i + 1 } = - \frac { 3 } { 2 } w _ { i } + 3 w _ { i - 1 } - \frac { 1 } { 2 } w _ { i - 2 } + 3 h f ( t _ { i } , w _ { i } ) , \quad \mathrm { f o r ~ } i = 2 , \dots , N - 1 ,
$$

with starting values $w _ { 0 } , w _ { 1 } , w _ { 2 }$ ：

a. Find the local truncation error.   
b. Comment on consistency,stability,and convergence.

6.Obtain an approximate solution to the differential equation

$$
y ^ { \prime } = - y , \quad 0 \leq t \leq 1 0 , \quad y ( 0 ) = 1
$$

using Milne's method with $h = 0 . 1$ and then $h \ = \ 0 . 0 1$ ， with starting values $w _ { 0 } = 1$ and $w _ { 1 } = e ^ { - h }$ in both cases. How does decreasing $h$ from $h = 0 . 1$ to $h = 0 . 0 1$ affect the number of correct digits in the approximate solutions at $t = 1$ and $t = 1 0 ?$

7.Investigate stability for the difference method

$$
w _ { i + 1 } = - 4 w _ { i } + 5 w _ { i - 1 } + 2 h [ f ( t _ { i } , w _ { i } ) + 2 h f ( t _ { i - 1 } , w _ { i - 1 } ) ] ,
$$

for $i = 1 , 2 , \dots , N - 1$ ， with starting values $w _ { 0 } , w _ { 1 }$ ·

8. Consider the problem $y ^ { \prime } = 0 , 0 \leq t \leq 1 0 , y ( 0 ) = 0$ ，which has the solution $y \equiv 0$ . If the difference method of Exercise 4 is applied to the problem, then

$$
\begin{array} { c } { { w _ { i + 1 } = 4 w _ { i } - 3 w _ { i - 1 } , \quad \mathrm { f o r } i = 1 , 2 , \dots , N - 1 . } } \\ { { } } \\ { { w _ { 0 } = 0 , \quad \mathrm { a n d } \quad w _ { 1 } = \alpha _ { 1 } . } } \end{array}
$$

Suppose $w _ { 1 } = \alpha _ { 1 } = \varepsilon$ ，where $\pmb { \varepsilon }$ is a small rounding error. Compute $w _ { i }$ exactly for $i \ =$ 2,3,...,6 to find how the error $\pmb \varepsilon$ is propagated.

# 5.11 Stiff Differential Equations

All the methods for approximating the solution to initial-value problems have error terms that involve a higher derivative of the solution of the equation. If the derivative can be reasonably bounded, then the method will have a predictable error bound that can be used to estimate the accuracy of the approximation. Even if the derivative grows as the steps increase, the error can be kept in relative control, provided that the solution also grows in magnitude.Problems frequently arise, however, when the magnitude of the derivative increases but the solution does not. In this situation, the error can grow so large that it dominates the calculations.Initial-value problems for which this is likely to occur are called stiff equations and are quite common, particularly in the study of vibrations,chemical reactions,and electrical circuits. Stiff systems derive their name from the motion of spring and mass systems that have large spring constants.

Stiff differential equations are characterized as those whose exact solution has a term of the form $e ^ { - c t }$ ，where $c$ is a large positive constant. This is usually only a part of the solution, called the transient solution. The more important portion of the solution is called the steady-state solution. The transient portion of a stiff equation wil rapidly decay to zero as $\pmb { t }$ increases, but since the nth derivative of this term has magnitude $c ^ { n } e ^ { - c t }$ , the derivative does not decay as quickly. In fact, since the derivative in the error term is evaluated not at $t$ ,but at a number between zero and t, the derivative terms can increase as t increasesand very rapidly indeed. Fortunately, stiff equations generally can be predicted from the physical problem from which the equation is derived and, with care,the error can be kept under control. The manner in which this is done is considered in this section.

# EXAMPLE 1

The system of initial-value problems

$$
\begin{array} { l } { { u _ { 1 } ^ { \prime } = 9 u _ { 1 } + 2 4 u _ { 2 } + 5 \cos t - \displaystyle \frac 1 3 \sin t , \quad u _ { 1 } ( 0 ) = \displaystyle \frac 4 3 } } \\ { { } } \\ { { u _ { 2 } ^ { \prime } = - 2 4 u _ { 1 } - 5 1 u _ { 2 } - 9 \cos t + \displaystyle \frac 1 3 \sin t , \quad u _ { 2 } ( 0 ) = \displaystyle \frac 2 3 } } \end{array}
$$

has the unique solution

$$
\begin{array} { l } { { u _ { 1 } ( t ) = 2 e ^ { - 3 t } - e ^ { - 3 9 t } + \displaystyle \frac { 1 } { 3 } \cos t , } } \\ { { \displaystyle u _ { 2 } ( t ) = - e ^ { - 3 t } + 2 e ^ { - 3 9 t } - \displaystyle \frac { 1 } { 3 } \cos t . } } \end{array}
$$

The transient term $e ^ { - 3 9 t }$ in the solutioncauses this system to be stif.Applying Algorithm 5.7, the Runge-Kutta Fourth-Order Method for Systems, gives results listed in Table 5.20. When $h = 0 . 0 5$ , stability results and the approximations are accurate. Increasing the step size to $h = 0 . 1$ ,however,leads to the disastrous results shown in the table.

Table 5.20   

<table><tr><td>t</td><td>u1(t）</td><td>w1(t） h = 0.05</td><td>w1(t) h = 0.1</td><td>u2(t)</td><td>W2(t) h = 0.05</td><td>w2(t) h = 0.1</td></tr><tr><td>0.1</td><td>1.793061</td><td>1.712219</td><td>-2.645169</td><td>-1.032001</td><td>-0.8703152</td><td>7.844527</td></tr><tr><td>0.2</td><td>1.423901</td><td>1.414070</td><td>-18.45158</td><td>-0.8746809</td><td>-0.8550148</td><td>38.87631</td></tr><tr><td>0.3</td><td>1.131575</td><td>1.130523</td><td>-87.47221</td><td>-0.7249984</td><td>-0.7228910</td><td>176.4828</td></tr><tr><td>0.4</td><td>0.9094086</td><td>0.9092763</td><td>-934.0722</td><td>-0.6082141</td><td>-0.6079475</td><td>789.3540</td></tr><tr><td>0.5</td><td>0.7387877</td><td>9.7387506</td><td>-1760.016</td><td>-0.5156575</td><td>-0.5155810</td><td>3520.00</td></tr><tr><td>0.6</td><td>0.6057094</td><td>0.6056833</td><td>-7848.550</td><td>-0.4404108</td><td>-0.4403558</td><td>15697.84</td></tr><tr><td>0.7</td><td>0.4998603</td><td>0.4998361</td><td>-34989.63</td><td>-0.3774038</td><td>-0.3773540</td><td>69979.87</td></tr><tr><td>0.8</td><td>0.4136714</td><td>0.4136490</td><td>-155979.4</td><td>-0.3229535</td><td>-0.3229078</td><td>311959.5</td></tr><tr><td>0.9</td><td>0.3416143</td><td>0.3415939</td><td>-695332.0</td><td>-0.2744088</td><td>-0.2743673</td><td>1390664.</td></tr><tr><td>1.0</td><td>0.2796748</td><td>0.2796568</td><td>-3099671.</td><td>-0.2298877</td><td>-0.2298511</td><td>6199352.</td></tr></table>

Although stiffness is usually associated with systems of differential equations, the approximation characteristics of a particular numerical method applied to a stiff system can be predicted by examining the error produced when the method is applied to a simple test equation,

$$
y ^ { \prime } = \lambda y , \quad y ( 0 ) = \alpha , \quad \mathrm { w h e r e } \lambda < 0 .
$$

The solution to this equation is $y ( t ) = \alpha e ^ { \lambda t }$ , which contains the transient solution $e ^ { \lambda t }$ . The steady-state solution is zero, so the approximation characteristics of a method are easy to

determine. (A more complete discussion of the roundoff error associated with stiff systems requires examining the test equation when $\lambda$ is a complex number with negative imaginary part; see [Ge1, p. 222].)

First consider Euler's method applied to the test equation. Letting $h = ( b - a ) / N$ and $t _ { j } = j h$ ,for $j = 0 , 1 , 2 , \ldots , N$ ,Eq.(5.8) implies that

$$
w _ { 0 } = \alpha ,
$$

and

$$
w _ { j + 1 } = w _ { j } + h ( \lambda w _ { j } ) = ( 1 + h \lambda ) w _ { j } ,
$$

So

$$
w _ { j + 1 } = ( 1 + h \lambda ) ^ { j + 1 } w _ { 0 } = ( 1 + h \lambda ) ^ { j + 1 } \alpha , \quad \mathrm { f o r ~ } j = 0 , 1 , \dots , N - 1 .
$$

Since the exact solution is $y ( t ) = \alpha e ^ { \lambda t }$ , the absolute error is

$$
| y ( t _ { j } ) - w _ { j } | = \left| e ^ { j h \lambda } - ( 1 + h \lambda ) ^ { j } \right| | \alpha | = \left| ( e ^ { h \lambda } ) ^ { j } - ( 1 + h \lambda ) ^ { j } \right| | \alpha | ,
$$

and the accuracy is determined by how well the term $1 + h \lambda$ approximates $e ^ { h \lambda }$ . When $\lambda < 0$ ， the exact solution $( e ^ { h \lambda } ) ^ { j }$ decays to zero as $j$ increases, but by (5.64),the approximation will have this property only if $| 1 + h \lambda | < 1$ . This effectively restricts the step size $h$ for Euler's method to satisfy $h < 2 / \vert \lambda \vert$

Suppose now that a roundoff error $\delta _ { 0 }$ is introduced in the initial condition for Euler's method,

$$
\begin{array} { r } { w _ { 0 } = \alpha + \delta _ { 0 } . } \end{array}
$$

At the $j$ th step the roundoff error is

$$
\delta _ { j } = ( 1 + h \lambda ) ^ { j } \delta _ { 0 } .
$$

Since $\lambda < 0$ ,the condition for the control of the growth of roundoff error is the same as the condition for controlling the absolute error, $| 1 + h \lambda | < 1$ , which implies that $h < 2 / | \lambda |$

The situation is similar for other one-step methods.In general, a function $Q$ exists with the property that the difference method, when applied to the test equation, gives

$$
w _ { i + 1 } = Q ( h \lambda ) w _ { i } .
$$

The accuracy of the method depends upon how well $Q ( h \lambda )$ approximates $e ^ { h \lambda }$ , and the error will grow without bound if $| Q ( h \lambda ) | > 1$ .An $\pmb { n }$ th-order Taylor method, for example,will have stability with regard to both the growth of roundoff error and absolute error, provided $\hbar$ is chosen to satisfy

$$
\left| 1 + h \lambda + { \frac { 1 } { 2 } } h ^ { 2 } \lambda ^ { 2 } + \cdots + { \frac { 1 } { n ! } } h ^ { n } \lambda ^ { n } \right| < 1 .
$$

Exercise 6 examines the specific case when the method is the classical fourth-order Runge-Kutta method, a Taylor method of order four.

When a multistep method of the form (5.54) is applied to the test equation, the result is

$$
w _ { j + 1 } = a _ { m - 1 } w _ { j } + \cdot \cdot \cdot + a _ { 0 } w _ { j + 1 - m } + h \lambda ( b _ { m } w _ { j + 1 } + b _ { m - 1 } w _ { j } + \cdot \cdot \cdot + b _ { 0 } w _ { j + 1 - m } ) ,
$$

for $j = m - 1 , \ldots , N - 1$ ,0r

$$
( 1 - h \lambda b _ { m } ) w _ { j + 1 } - ( a _ { m - 1 } + h \lambda b _ { m - 1 } ) w _ { j } - \cdot \cdot \cdot - ( a _ { 0 } + h \lambda b _ { 0 } ) w _ { j + 1 - m } = 0 .
$$

Associated with this homogeneous difference equation is a characteristic polynomial

$$
Q ( z , h \lambda ) = ( 1 - h \lambda b _ { m } ) z ^ { m } - ( a _ { m - 1 } + h \lambda b _ { m - 1 } ) z ^ { m - 1 } - \cdot \cdot \cdot - ( a _ { 0 } + h \dot { \lambda } b _ { 0 } ) .
$$

This polynomial is similar to the characteristic polynomial (5.57),but it also incorporates the test equation. The theory here parallels the stability discussion in Section 5.10.

Suppose $w _ { 0 } , \ldots , w _ { m - 1 }$ are given, and, for fixed $h \lambda$ ,let $\beta _ { 1 } , \ldots , \beta _ { m }$ be the zeros of the polynomial $Q ( z , h \lambda )$ .If $\beta _ { 1 } , \ldots , \beta _ { m }$ are distinct, then $c _ { 1 } , \ldots , c _ { m }$ exist with

$$
w _ { j } = \sum _ { k = 1 } ^ { m } c _ { k } ( \beta _ { k } ) ^ { j } , \quad \mathrm { f o r } \ j = 0 , \dots , N .
$$

f $Q ( z , h \lambda )$ has multiple zeros, $w _ { j }$ is similarly defined. (See Eq. (5.62) in Section 5.10.) f $w _ { j }$ is to accurately approximate $y ( t _ { j } ) = e ^ { j h \lambda } = ( e ^ { h \lambda } ) ^ { j }$ , then all zeros $\beta _ { k }$ must satisfy $| \beta _ { k } | < 1$ ; otherwise, certain choices of $\pmb { \alpha }$ will result in $c _ { k } \neq 0$ , and the term $c _ { k } ( \beta _ { k } ) ^ { j }$ will not decay to zero.

EXAMPLE 2 The test differential equation

$$
y ^ { \prime } = - 3 0 y , \quad 0 \leq t \leq 1 . 5 , \quad y ( 0 ) = { \frac { 1 } { 3 } }
$$

has exact solution $\begin{array} { r } { y = \frac { 1 } { 3 } e ^ { - 3 0 t } } \end{array}$ .Using $h = 0 . 1$ for Euler's Algorithm 5.1, Runge-Kutta Fourth-Order Algorithm 5.2,and the Adams Predictor-Corrector Algorithm 5.4, gives the results at $t = 1 . 5$ in Table 5.21.

Table 5.21   

<table><tr><td>Exact solution Euler&#x27;s method Runge-Kutta method</td><td>9.54173 × 10-21 -1.09225 ×104 3.95730 ×101</td></tr></table>

The inaccuracies in Example 2 are due to the fact that $| Q ( h \lambda ) | > 1$ for Euler's method and the Runge-Kutta method and that $Q ( z , h \lambda )$ has zeros with modulus exceeding 1 for the predictor-corrector method. To apply these methods to this problem, the step size must be reduced. The following definition is used to describe the amount of step-size reduction that is required.

# Definition 5.25

The region R of absolute stability for aone-step method is $R = \{ h \lambda \in \mathcal { C } \mid | Q ( h \lambda ) | < 1 \}$ ， and for a multistep method, it is $R = \{ h \lambda \in \mathcal { C } \mid \{ \beta _ { k } | < 1 \}$ , for all zeros $\beta _ { k }$ of $Q ( z , h \lambda ) \}$

Equations (5.65) and (5.66) imply that a method can be applied effectively to a stiff equation only if hλ is in the region of absolute stability of the method,which for a given problem places a restriction on the size of h.Even though the exponential term in the exact solution decays quickly to zero,λh must remain within the region of absolute stability throughout the interval of $t$ values for the approximation to decay to zero and the growth of error to be under control. This means that, although $h$ could normally be increased because of truncation error considerations, the absolute stability criterion forces $h$ to remain small. Variable step-size methods are especially vulnerable to this problem since an examination of the local truncation error might indicate that the step size could increase,which could inadvertently result in λh being outside the region of absolute stability.

Since the region of absolute stability of a method is generally the critical factor in producing accurate approximations for stiff systems, numerical methods are sought with as large a region of absolute stability as possible.A numerical method is said to be $\pmb { A }$ -stable if its region $R$ of absolute stability contains the entire left half-plane.

The Implicit Trapezoidal method, given by

$$
\begin{array} { l } { { \displaystyle w _ { 0 } = \alpha , } } \\ { { \displaystyle w _ { j + 1 } = w _ { j } + \frac { h } { 2 } \left[ f ( t _ { j + 1 } , w _ { j + 1 } ) + f ( t _ { j } , w _ { j } ) \right] , \quad 0 \le j \le N - 1 , } } \end{array}
$$

is an $A$ -stable method (see Exercise 9) and is the only $A$ -stable multistep method. Although the Trapezoidal method does not give accurate approximations for large step sizes, its errol will not grow exponentially.

The techniques commonly used for stiff systems are implicit multistep methods. Generally, $w _ { i + 1 }$ is obtained by solving a nonlinear equation or nonlinear system iteratively, often by Newton's method. Consider, for example,the Implicit Trapezoidal method

$$
w _ { j + 1 } = w _ { j } + { \frac { h } { 2 } } [ f ( t _ { j + 1 } , w _ { j + 1 } ) + f ( t _ { j } , w _ { j } ) ] .
$$

Having computed $t _ { j } , t _ { j + 1 }$ ,and $w _ { j }$ , we need to determine $w _ { j + 1 }$ , the solution to

$$
F ( w ) = w - w _ { j } - \frac { h } { 2 } [ f ( t _ { j + 1 } , w ) + f ( t _ { j } , w _ { j } ) ] = 0 .
$$

To approximate this solution, select $\boldsymbol { w } _ { j + 1 } ^ { ( 0 ) }$ , usually as $w _ { j }$ , and generate $\boldsymbol { w } _ { j + 1 } ^ { ( k ) }$ by applying Newton's method to (5.68),

$$
\begin{array} { r l } & { w _ { j + 1 } ^ { ( k ) } = w _ { j + 1 } ^ { ( k - 1 ) } - \frac { F ( w _ { j + 1 } ^ { ( k - 1 ) } ) } { F ^ { \prime } ( w _ { j + 1 } ^ { ( k - 1 ) } ) } } \\ & { \qquad = w _ { j + 1 } ^ { ( k - 1 ) } - \frac { w _ { j + 1 } ^ { ( k - 1 ) } - w _ { j } - \frac { h } { 2 } [ f ( t _ { j } , w _ { j } ) + f ( t _ { j + 1 } , w _ { j + 1 } ^ { ( k - 1 ) } ) ] } { 1 - \frac { h } { 2 } f _ { y } ( t _ { j + 1 } , w _ { j + 1 } ^ { ( k - 1 ) } ) } } \end{array}
$$

until|wj+1 $| \boldsymbol { w } _ { j + 1 } ^ { ( k ) } - \boldsymbol { w } _ { j + 1 } ^ { ( k - 1 ) } |$ islse 5.8.Normally only three or four iterations per step are required.

The Secant method can be used as an alternative to Newton's method in Eq. (5.68), but then two distinct initial approximations to $w _ { j + 1 }$ are required. To employ the Secant method,

the usual practice is to let w(1 $w _ { j + 1 } ^ { ( 0 ) } = w _ { j }$ and obtain $\boldsymbol { w } _ { j + 1 } ^ { ( 1 ) }$ from some explicit multistep method. When a system of stiff equations is involved,a generalization is required for either Newton's or the Secant method. These topics are considered in Chapter 10.

# Trapezoidal with Newton Iteration

To approximate the solution of the initial-value problem

$$
y ^ { \prime } = f ( t , y ) , \quad \mathrm { f o r } a \leq t \leq b , \quad \mathrm { w i t h } y ( a ) = \alpha
$$

at $( N + 1 )$ equally spaced numbers in the interval $\{ a , b \}$ ：

INPUTendpoints $a , b$ ; integer $N$ ; initial condition $\pmb { \alpha }$ ; tolerance TOL; maximum number of iterations $M$ at any one step.

OUTPUTapproximation $w$ to $y$ at the $( N + 1 )$ values of $t$ or a messge of failure.

$$
\begin{array} { r l } { S t e p \ 1 } & { \mathrm { S e t } \ h = ( b - a ) / N ; } \\ & { \qquad t = a ; } \\ & { \qquad w = \alpha ; } \\ & { \qquad \mathrm { O U T P U T } \ ( t , w ) . } \end{array}
$$

Step 2 For $i = 1 , 2 , \dots , N$ do Steps 3-7.

$$
\begin{array} { c c } { { S t e p 3 } } & { { S e t k _ { 1 } = w + \frac { h } { 2 } f ( t , w ) ; } } \\ { { } } & { { w _ { 0 } = k _ { 1 } ; } } \\ { { } } & { { j = 1 ; } } \\ { { } } & { { { \cal F L A G } = 0 . } } \end{array}
$$

Step 4 While $F L A G = 0$ do Steps 5-6.

Step 5 Set $\mathrm { ~ } : w = w _ { 0 } - \frac { w _ { 0 } - \displaystyle \frac { h } { 2 } f ( t + h , w _ { 0 } ) - k _ { 1 } } { 1 - \displaystyle \frac { h } { 2 } f _ { y } ( t + h , w _ { 0 } ) } .$

Step 6If $| w - w _ { 0 } | < T O L$ then set $F L A G = 1$ else set $j = j + 1$ ； $w _ { 0 } = w ;$ if $j > M$ then OUTPUT('The maximum number of iterations exceeded'); STOP.

Step 7 Set $t = a + i h$ ； OUTPUT $( t , w )$

Step 8 STOP.

The stiff initial-value problem

$$
y ^ { \prime } = 5 e ^ { 5 t } ( y - t ) ^ { 2 } + 1 , \quad 0 \leq t \leq 1 , \quad y ( 0 ) = - 1
$$

has solution $y ( t ) = t - e ^ { - 5 t }$ . To show the effects of stiffness,the Implicit Trapezoidal method and the Runge-Kutta fourth-order method are applied both with $N = 4$ ，giving $h = 0 . 2 5$ , and with $N = 5$ , giving $h = 0 . 2 0$ . The Trapezoidal method performs well in both cases using $M = 1 0$ and $T O L = 1 0 ^ { - 6 }$ , as does Runge-Kutta with $h = 0 . 2$ However, $h = 0 . 2 5$ is outside the region of absolute stability of the Runge-Kutta method, which is evident from the results in Table 5.22. ■

Table 5.22   

<table><tr><td></td><td colspan="2">Runge-Kutta Method</td><td colspan="2">Trapezoidal Method</td></tr><tr><td></td><td>h = 0.2</td><td></td><td>h = 0.2</td><td>ly(ti）-wil</td></tr><tr><td>t</td><td>W</td><td>ly(ti）-wil</td><td>Wi</td><td></td></tr><tr><td>0.0</td><td>-1.0000000</td><td>0 1.9027 × 10-2</td><td>-1.0000000 -0.1414969</td><td>0 2.6383 × 10-2</td></tr><tr><td>0.2</td><td>-0.1488521</td><td>3.8237× 10-3</td><td></td><td>1.0197 × 10-2</td></tr><tr><td>0.4</td><td>0.2684884</td><td>1.7798 × 10-3</td><td>0.2748614</td><td>3.7700 × 10-3</td></tr><tr><td>0.6</td><td>0.5519927</td><td>6.0131 × 10-4</td><td>0.5539828 0.7830720</td><td>1.3876× 10-3</td></tr><tr><td>0.8 1.0</td><td>0.7822857</td><td>2.2845 × 10-4</td><td>0.9937726</td><td>5.1050 × 10-4</td></tr><tr><td></td><td>0.9934905</td><td></td><td></td><td>h = 0.25</td></tr><tr><td colspan="5">h = 0.25</td></tr><tr><td>ti</td><td>Wi</td><td>ly(ti）-wil</td><td>Wi</td><td>ly(ti）-wil</td></tr><tr><td>0.0</td><td>-1.0000000</td><td>0</td><td>-1.0000000</td><td>0</td></tr><tr><td>0.25</td><td>0.4014315</td><td>4.37936 × 10-l</td><td>0.0054557</td><td>4.1961 × 10-2</td></tr><tr><td>0.5</td><td>3.4374753</td><td>3.01956×100</td><td>0.4267572</td><td>8.8422 × 10-3</td></tr><tr><td>0.75</td><td>1.44639 × 1023</td><td>1.44639 × 1023</td><td>0.7291528</td><td>2.6706 × 10-3</td></tr><tr><td>1.0</td><td>Overflow</td><td></td><td>0.9940199</td><td>7.5790 × 10-4</td></tr></table>

We have presented here only a small amount of what the reader frequently encountering stiff differential equations should know. For further details, consult $[ G e 2 ]$ ,[Lam], or [SGe].

# EXERCISE SET 5.11

1.Solve the follwing stif initial-value problems using Euler's method, and compare the results with the actual solution.

a.y= -9y，0≤t ≤1， y(O)= e,with h =0.1; actual solution y(t)=el-9.   
b. $y ^ { \prime } = - 2 0 ( y - t ^ { 2 } ) + 2 t$ ， $0 \leq t \leq 1$ ， $\begin{array} { r } { y ( 0 ) = \frac { 1 } { 3 } } \end{array}$ ，with $h = 0 . 1$ ; actual solution $\begin{array} { r } { y ( t ) = t ^ { 2 } + \frac { 1 } { 3 } e ^ { - 2 0 t } } \end{array}$   
c. $y ^ { \prime } = - 2 0 y + 2 0 \sin { t } + \cos { t }$ ， $0 \leq t \leq 2$ ， $y ( 0 ) = 1$ ，with $h = 0 . 2 5$ ； actual solution y(t)= sint +e-20t.

d. $\begin{array} { r } { y ^ { \prime } = \frac { 5 0 } { y } - 5 0 y } \end{array}$ ， $0 \leq t \leq 1$ ， $y ( 0 ) = { \sqrt { 2 } } .$ with $h = 0 . 1$ ； actual solution $y ( t ) =$ $( 1 + e ^ { - 1 0 0 t } ) ^ { 1 / 2 }$

2.Repeat Exercise 1 using the Runge-Kutta fourth-order method.

3.Repeat Exercise 1 using the Adams fourth-order predictor-corrector method.

4.Repeat Exercise 1 using the Trapezoidal Algorithm. Use $T O L = 1 0 ^ { - 5 }$ · 5.Solve the following stiff initial-value problem using the Runge-Kutta fourth-order method with (a） $h = 0 . 1$ and (b) $\mid h = 0 . 0 2 5$

$$
\begin{array} { l } { { u _ { 1 } ^ { \prime } = { 3 2 u _ { 1 } + 6 6 u _ { 2 } + \displaystyle \frac { 2 } { 3 } t + \displaystyle \frac { 2 } { 3 } , \quad 0 \le t \le 0 . 5 , \quad u _ { 1 } ( 0 ) = \displaystyle \frac { 1 } { 3 } ; } } } \\ { { { } } } \\ { { u _ { 2 } ^ { \prime } = - 6 6 u _ { 1 } - 1 3 3 u _ { 2 } - \displaystyle \frac { 1 } { 3 } t - \displaystyle \frac { 1 } { 3 } , \quad 0 \le t \le 0 . 5 , \quad u _ { 2 } ( 0 ) = \displaystyle \frac { 1 } { 3 } . } } \end{array}
$$

Compare the results to the actual solution,

$$
u _ { 1 } ( t ) = { \frac { 2 } { 3 } } t + { \frac { 2 } { 3 } } e ^ { - t } - { \frac { 1 } { 3 } } e ^ { - 1 0 0 t } \quad { \mathrm { a n d } } \quad u _ { 2 } ( t ) = - { \frac { 1 } { 3 } } t - { \frac { 1 } { 3 } } e ^ { - t } + { \frac { 2 } { 3 } } e ^ { - 1 0 0 t } .
$$

6.Show that the fourth-order Runge-Kutta method,

$$
\begin{array} { r l } & { k _ { 1 } = h f ( t _ { i } , w _ { i } ) , } \\ & { k _ { 2 } = h f ( t _ { i } + h / 2 , w _ { i } + k _ { 1 } / 2 ) , } \\ & { k _ { 3 } = h f ( t _ { i } + h / 2 , w _ { i } + k _ { 2 } / 2 ) , } \\ & { k _ { 4 } = h f ( t _ { i } + h , w _ { i } + k _ { 3 } ) , } \\ & { w _ { i + 1 } = w _ { i } + \displaystyle \frac { 1 } { 6 } ( k _ { 1 } + 2 k _ { 2 } + 2 k _ { 3 } + k _ { 4 } ) , } \end{array}
$$

when applied to the differential equation $y ^ { \prime } = \lambda y$ , can be written in the form

$$
w _ { i + 1 } = \left( 1 + h \lambda + \frac { 1 } { 2 } ( h \lambda ) ^ { 2 } + \frac { 1 } { 6 } ( h \lambda ) ^ { 3 } + \frac { 1 } { 2 4 } ( h \lambda ) ^ { 4 } \right) w _ { i } .
$$

7.Discuss consistency,stability,and convergence for the Implicit Trapezoidal method

$$
w _ { i + 1 } = w _ { i } + { \frac { h } { 2 } } [ f ( t _ { i + 1 } , w _ { i + 1 } ) + f ( t _ { i } , w _ { i } ) ] , \quad { \mathrm { f o r ~ } } i = 0 , 1 , \dots , N - 1 ,
$$

with $w _ { 0 } = \alpha$ applied to the differential equation

$$
y ^ { \prime } = f ( t , y ) , \quad a \leq t \leq b , \quad y ( a ) = \alpha .
$$

8.The Backward Euler one-step method is defined by

$$
w _ { i + 1 } = w _ { i } + h f ( t _ { i + 1 } , w _ { i + 1 } ) , \quad \mathrm { f o r ~ } i = 0 , \dots , N - 1 .
$$

a.Show that $Q ( h \lambda ) = 1 / ( 1 - h \lambda )$ for the Backward Euler method.

b. Apply the Backward Euler method to the differential equations given in Exercise 1. Use Newton's method to solve for ${ \pmb w } _ { i + 1 }$

9.a.Show that the Implicit Trapezoidal method (5.67) is $\pmb { A }$ -stable. b.Show that the Backward Euler method described in Exercise 8 is A-stable.

# 5.12 Survey of Methods and Software

In this chapter we have considered methods to approximate the solutions to initial-value problems for ordinary differential equations. We began with a discussion of the most elementary numerical technique, Euler's method. This procedure is not sufficiently accurate to be of use in applications,but it illustrates the general behavior of the more powerful techniques,without the accompanying algebraic difficulties. The Taylor methods were then considered as generalizations of Euler's method. They were found to be accurate but cumbersome because of the need to determine extensive partial derivatives of the defining function of the diferential equation. The Runge-Kuta formulas simplified the Taylor methods, while not significantly increasing the error. To this point we had considered only one-step methods, techniques that use only data at the most recently computed point.

Multistep methods are discussed in Section 5.6, where Explicit methods of Adams-Bashforth type and implicit methods of Adams-Moulton type were considered. These culminate in predictor-corrector methods,which use an explicit method,such as an Adams-Bashforth, to predict the solution and then apply a corresponding implicit method, like an Adams-Moulton, to correct the approximation.

Section 5.9 illustrated how these techniques can be used to solve higher-order initialvalue problems and systems of initial-value problems.

The more accurate adaptive methods are based on the relatively uncomplicated one-step and multistep techniques. In particular, we saw in Section 5.5 that the Runge-Kutta-Fehlberg method is a one-step procedure that seeks to select mesh spacing to keep the local error of the approximation under control. The Variable Step-Size Predictor-Corrector method presented in Section 5.7 is based on the four-step Adams-Bashforth method and three-step Adams-Moulton method. It also changes the step size to keep the local error within a given tolerance.The Extrapolation method discussed in Section 5.8 is based on a modification of the Midpoint method and incorporates extrapolation to maintain a desired accuracy of approximation.

The final topic in the chapter concerned the difculty that is inherent in the approximation of the solution to a stiff equation, a differential equation whose exact solution contains a portion of the form $e ^ { - \lambda t }$ ， where $\lambda$ is a positive constant. Special caution must be taken with problems of this type, or the results can be overwhelmed by roundoff error.

Methods of the Runge-Kutta-Fehlberg type are generally sufficient for nonstiff problems when moderate accuracy is required. The extrapolation procedures are recommended for nonstiff problems where high accuracy is required. Extensions of the Implicit Trapezoidal method to variable-order and variable step-size implicit Adams-type methods are used for stiff initial-value problems.

The IMSL Library includes two subroutines for approximating the solutions of initialvalue problems. Each of the methods solves a system of m first-order equations in $m$ variables. The equations are of the form

$$
\frac { d u _ { i } } { d t } = f _ { i } ( t , u _ { 1 } , u _ { 2 } , \ldots , u _ { m } ) , \quad \mathrm { f o r } i = 1 , 2 , \ldots , m ,
$$

where $u _ { i } \left( t _ { 0 } \right)$ is given for each $i$ . The variable step-size subroutine IVPRK is based on the Runge-Kutta-Verner fifth- and sixth-order methods described in Exercise 4 of Section 5.5. A subroutine of Adams type to be used for stiff equations is due to C. William Gear and is given by IVPAG. This method uses implicit multistep methods of order up to 12 and backward differentiation formulas of order up to 5.

The Runge-Kutta-type procedures contained in the NAG Library are called D02BGF, D02BHF,D02PCF,and D02PDF.D02BGF and D02BHF are based on the Merson form of the Runge-Kutta method. A variable-order and variable step-size Adams method is contained in the procedure DO2CJF. Variable-order, variable step-size backward-difference methods for stiff systems are contained in the procedure DO2EJF. Other routines incorporate the same methods but iterate until a component of the solution attains a given value or until a function of the solution is zero.

The netlib Library includes several subroutines for approximating the solutions of initial-value problems in the package ODE,located at http://www.netlib.org/ode. The subroutine dverk.f is based on the Runge-Kutta-Verner fth- and sixth-order methods. The subroutine rkf45.f is based on the Runge-Kutta-Fehlberg fourth- and fifth-order methods as described on pages 284-285 of Section 5.5. For stiff ordinary differential equation initialvalue problems, the subroutine epsode.f based on variable coefficient backward differentiation formula can be used.

Many books specialize in the numerical solution of initial-value problems. Two clas-sics are by Henrici [He1] and Gear [Ge1]. Other books that survey the field are by Botha and Pinder [BP],Ortega and Poole [OP], Golub and Ortega [GO], Shampine [Sh],and Dormand [Dol. Two books by Hairer, Norsett, and Warner provide comprehensive discussions on nonstiff [HNW1] and stiff [HNW2] problems. The book by Burrage [Bur] describes parallel and sequential methods.

CHAPTER

6

# Direct Methods for Solving Linear Systems

■

rent through each junction and the net voltage drop around each closed loop of a circuit are zero. Suppose that a potential of $\pmb { V }$ volts is applied between the points A and $\pmb { G }$ in the circuit and that $i _ { 1 } , i _ { 2 } , i _ { 3 } , i _ { 4 } ,$ ,and $i _ { 5 }$ represent current flow as shown in the diagram. Using $\pmb { G }$ as a reference point, Kirchhoff's laws imply that the currents satisfy the following system of linear equations:

$$
\begin{array} { r } { 5 i _ { 1 } + 5 i _ { 2 } = V , } \\ { i _ { 3 } - i _ { 4 } - i _ { 5 } = 0 , } \\ { 2 i _ { 4 } - 3 i _ { 5 } = 0 , } \\ { i _ { 1 } - i _ { 2 } - i _ { 3 } = 0 , } \\ { . - 7 i _ { 3 } - 2 i _ { 4 } = 0 . } \end{array}
$$

![](images/31151153d3cf99b4d751bc58b0dbb4896898823ab3d106c8165bf6d2d5147b79.jpg)

The solution of systems of this type will be considered in this chapter. This application is discussed in Exercise 23 of Section 6.6.

Linear systems of equations are associated with many problems in engineering and science,as well as with applications of mathematics to the social sciences and the quantitative study of business and economic problems.

In this chapter, direct techniques are considered to solve the linear system

$$
\begin{array} { r l } { E _ { 1 } : } & { a _ { 1 1 } x _ { 1 } + a _ { 1 2 } x _ { 2 } + \cdot \cdot \cdot + a _ { 1 n } x _ { n } = b _ { 1 } , } \\ { E _ { 2 } : } & { a _ { 2 1 } x _ { 1 } + a _ { 2 2 } x _ { 2 } + \cdot \cdot \cdot + a _ { 2 n } x _ { n } = b _ { 2 } , } \\ & { \vdots } \\ { E _ { n } : } & { a _ { n 1 } x _ { 1 } + a _ { n 2 } x _ { 2 } + \cdot \cdot \cdot + a _ { n n } x _ { n } = b _ { n } , } \end{array}
$$

for $x _ { 1 } , \ldots , x _ { n }$ ， given the constants $a _ { i j }$ , for each i, $j = 1 , 2 , \dots , n$ ，and $b _ { i }$ ,for each $i =$ $1 , 2 , \ldots , n$ . Direct techniques are methods that give an answer in a fixed number of steps, subject only to roundoff errors. In the presentation we shall also introduce some elementary notions from the subject of linear algebra.

Methods of approximating the solution to linear systems by iterative methods are discussed in Chapter 7.

# 6.1 Linear Systems of Equations

We use three operations to simplify the linear system given in (6.1):

1.Equation $E _ { i }$ can be multiplied by any nonzero constant $\lambda$ with the resulting equation used in place of $E _ { i }$ . This operation is denoted $( \lambda E _ { i } ) \to ( E _ { i } )$   
2. Equation $E _ { j }$ can be multiplied by any constant $\lambda$ and added to equation $E _ { i }$ with the resulting equation used in place of $E _ { i }$ . This operation is denoted $( E _ { i } + \lambda E _ { j } ) $ $( E _ { i } )$   
3.Equations $E _ { i }$ and $E _ { j }$ can be transposed in order. This operation is denoted $( E _ { i } ) $ $( E _ { j } )$

By a sequence of these operations, a linear system can be transformed to a more easily solved linear system that has the same solutions.The sequence of operations is illustrated in the next example.

# EXAMPLE 1 The four equations

$$
\begin{array} { r } { E _ { 1 } : \quad \quad x _ { 1 } + \ x _ { 2 } \quad \quad + 3 x _ { 4 } = \quad 4 , } \\ { E _ { 2 } : \quad 2 x _ { 1 } + \ x _ { 2 } - \ x _ { 3 } + \ x _ { 4 } = \quad 1 , } \\ { E _ { 3 } : \quad 3 x _ { 1 } - \ x _ { 2 } - \ x _ { 3 } + 2 x _ { 4 } = - 3 , } \\ { E _ { 4 } : \quad - x _ { 1 } + 2 x _ { 2 } + 3 x _ { 3 } - \ x _ { 4 } = \quad 4 , } \end{array}
$$

will be solved for $x _ { 1 } , x _ { 2 } , x _ { 3 }$ ,and $\pmb { x _ { 4 } }$ . We frst use equation $E _ { 1 }$ to eliminate the unknown $x _ { 1 }$ from $E _ { 2 } , E _ { 3 }$ ,and $E _ { 4 }$ by performing $( E _ { 2 } - 2 E _ { 1 } )  ( E _ { 2 } )$ ， $( E _ { 3 } - 3 E _ { 1 } )  ( E _ { 3 } )$ ， and $( E _ { 4 } + E _ { 1 } )  ( E _ { 4 } )$ . The resulting system is

$$
\begin{array} { r l r } { E _ { 1 } : } & { { } x _ { 1 } + } & { x _ { 2 } \qquad } & { + 3 x _ { 4 } = \quad 4 , } \\ { E _ { 2 } : } & { { } - } & { x _ { 2 } - } & { x _ { 3 } - 5 x _ { 4 } = \quad - 7 , } \\ { E _ { 3 } : } & { { } - 4 x _ { 2 } - } & { x _ { 3 } - 7 x _ { 4 } = - 1 5 , } \\ { E _ { 4 } : } & { { } } & { 3 x _ { 2 } + 3 x _ { 3 } + 2 x _ { 4 } = \quad 8 , } \end{array}
$$

where,for simplicity, the new equations are again labeled $E _ { 1 } , E _ { 2 } , E _ { 3 }$ ,and $E _ { 4 }$

In the new system, $\pmb { { \cal E } } _ { 2 }$ is used to eliminate $x _ { 2 }$ from $E _ { 3 }$ and $E _ { 4 }$ by performing $( E _ { 3 } -$ $4 E _ { 2 } )  ( E _ { 3 } )$ and $( E _ { 4 } + 3 E _ { 2 } )  ( E _ { 4 } )$ , resulting in

$$
\begin{array} { r l r } { E _ { 1 } : } & { { } x _ { 1 } + x _ { 2 } } & { + \ 3 x _ { 4 } = \ \begin{array} { c } { 4 , } \\ { E _ { 2 } : } \end{array} } \\ { E _ { 3 } : } & { { } \begin{array} { r r r r } { - x _ { 2 } - } & { x _ { 3 } - } & { 5 x _ { 4 } = \ - 7 , } \\ { 3 x _ { 3 } + 1 3 x _ { 4 } = } & { { } 1 3 , } \\ { E _ { 4 } : } & { { } \ - 1 3 x _ { 4 } = - 1 3 . } \end{array} } \end{array}
$$

The system of equations (6.3) is now in triangular (or reduced) form and can be solved for the unknowns by a backward-substitution process. Since $E _ { 4 }$ implies $x _ { 4 } = 1$ we can solve $E _ { 3 }$ for $x _ { 3 }$ to give

$$
x _ { 3 } = { \frac { 1 } { 3 } } ( 1 3 - 1 3 x _ { 4 } ) = { \frac { 1 } { 3 } } ( 1 3 - 1 3 ) = 0 .
$$

Continuing, $E _ { 2 }$ gives

$$
x _ { 2 } = - ( - 7 + 5 x _ { 4 } + x _ { 3 } ) = - ( - 7 + 5 + 0 ) = 2 ,
$$

and $E _ { 1 }$ gives

$$
x _ { 1 } = 4 - 3 x _ { 4 } - x _ { 2 } = 4 - 3 - 2 = - 1 .
$$

The solution to (6.3),and consequently to (6.2), is therefore, $x _ { 1 } = - 1 , x _ { 2 } = 2 , x _ { 3 } = 0$ ， and $x _ { 4 } = 1$

When performing the calculations of Example 1, we did not need to write out the full equations at each step or to carry the variables $x _ { 1 } , x _ { 2 } , x _ { 3 }$ , and $x _ { 4 }$ through the calculations, since they always remained in the same column. The only variation from system to system occurred in the coeffcients of the unknowns and in the values on the right side of the equations.For this reason,a linear system is often replaced by a matrix, which contains all the information about the system that is necessary to determine its solution, but in a compact form.

An n x m ( $\mathbf { \hat { \Pi } } _ { \mathbf { \pmb { n } } }$ by m) matrix is a rectangular array of elements with n rows and m columns in which notonly is the value of an element important,but also its position in the aay.

The notation for an $n \times m$ matrix will be a capital letter such as $A$ for the matrix and lowercase letters with double subscripts, such as $a _ { i j }$ , to refer to the entry at the intersection of the $i$ th row and $j$ th column; that is,

$$
A = ( a _ { i j } ) = \left[ { \begin{array} { c c c c } { a _ { 1 1 } } & { a _ { 1 2 } } & { \cdot \cdot \cdot } & { a _ { 1 m } } \\ { a _ { 2 1 } } & { a _ { 2 2 } } & { \cdot \cdot \cdot } & { a _ { 2 m } } \\ { \vdots } & { \vdots } & & { \vdots } \\ { a _ { n 1 } } & { a _ { n 2 } } & { \cdot \cdot \cdot } & { a _ { n m } } \end{array} } \right] .
$$

# EXAMPlE 2

The matrix

$$
A = { \left[ \begin{array} { l l l } { 2 } & { - 1 } & { 7 } \\ { 3 } & { 1 } & { 0 } \end{array} \right] }
$$

is a $2 \times 3$ matrix with $\boldsymbol { a } _ { 1 1 } = 2 , \boldsymbol { a } _ { 1 2 } = - 1 , \boldsymbol { a } _ { 1 3 } = 7 , \boldsymbol { a } _ { 2 1 } = 3 , \boldsymbol { a } _ { 2 2 } = 1$ ,and $a _ { 2 3 } = 0$

The $1 \times n$ matrix

$$
A = [ a _ { 1 1 } ~ a _ { 1 2 } ~ \cdot ~ \cdot ~ \cdot ~ a _ { 1 n } ]
$$

is called an $\pmb { n }$ -dimensional row vector, and an $n \times 1$ matrix

$$
A = { \left[ \begin{array} { l } { a _ { 1 1 } } \\ { a _ { 2 1 } } \\ { \vdots } \\ { a _ { n 1 } } \end{array} \right] }
$$

is called an $\pmb { n }$ -dimensional column vector. Usually the unecessary subscripts are omitted for vectors, and a boldface lowercase leter is used for notation. Thus,

$$
\mathbf { x } = { \left[ \begin{array} { l } { x _ { 1 } } \\ { x _ { 2 } } \\ { \vdots } \\ { x _ { n } } \end{array} \right] }
$$

denotes a column vector, and

$$
\mathbf { y } = [ y _ { 1 } y _ { 2 } \dotsm y _ { n } ]
$$

a row vector.

An $n \times ( n + 1 )$ matrix can be used to represent the linear system

$$
\begin{array} { r l r } & { } & { a _ { 1 1 } x _ { 1 } + a _ { 1 2 } x _ { 2 } + \cdot \cdot \cdot + a _ { 1 n } x _ { n } = b _ { 1 } , } \\ & { } & \\ & { } & { a _ { 2 1 } x _ { 1 } + a _ { 2 2 } x _ { 2 } + \cdot \cdot \cdot + a _ { 2 n } x _ { n } = b _ { 2 } , } \\ & { } & \\ & { } & { \vdots \ } \end{array}
$$

$$
a _ { n 1 } x _ { 1 } + a _ { n 2 } x _ { 2 } + \cdot \cdot \cdot + a _ { n n } x _ { n } = b _ { n } ,
$$

by first constructing

$$
A = { \left[ \begin{array} { l l l l } { a _ { 1 1 } } & { a _ { 1 2 } } & { \cdots } & { a _ { 1 n } } \\ { a _ { 2 1 } } & { a _ { 2 2 } } & { \cdots } & { a _ { 2 n } } \\ { \vdots } & { \vdots } & & { \vdots } \\ { a _ { n 1 } } & { a _ { n 2 } } & { \cdots } & { a _ { n n } } \end{array} \right] } \quad { \mathrm { a n d } } \quad \mathbf { b } = { \left[ \begin{array} { l } { b _ { 1 } } \\ { b _ { 2 } } \\ { \vdots } \\ { b _ { n } } \end{array} \right] }
$$

and then combining these matrices to form the augmented matrix

$$
[ A , \mathbf { b } ] = \left[ { \begin{array} { c c c c c } { a _ { 1 1 } } & { a _ { 1 2 } } & { \cdot \cdot \cdot } & { a _ { 1 n } } & { \colon } & { b _ { 1 } } \\ { a _ { 2 1 } } & { a _ { 2 2 } } & { \cdot \cdot \cdot } & { a _ { 2 n } } & { \vdots } & { b _ { 2 } } \\ { \vdots } & { \vdots } & & { \vdots } & { \vdots } & { \vdots } \\ { a _ { n 1 } } & { a _ { n 2 } } & { \cdot \cdot \cdot } & { a _ { n n } } & { \vdots } & { b _ { n } } \end{array} } \right] ,
$$

where the vertical dotted line is used to separate the coeficients of the unknowns from the values on the right-hand side of the equations.

Repeating the operations involved in Example 1 with the matrix notation results in first considering the augmented matrix:

$$
\left[ { \begin{array} { r r r r r r } { 1 } & { 1 } & { 0 } & { 3 } & { \vdots } & { 4 } \\ { 2 } & { 1 } & { - 1 } & { 1 } & { \vdots } & { 1 } \\ { 3 } & { - 1 } & { - 1 } & { 2 } & { \vdots } & { - 3 } \\ { - 1 } & { 2 } & { 3 } & { - 1 } & { \vdots } & { 4 } \end{array} } \right] .
$$

Performing the operations as described in that example produces the matrices

$$
\left[ { \begin{array} { r r r r r r } { 1 } & { 1 } & { 0 } & { 3 } & { \vdots } \\ { 0 } & { - 1 } & { - 1 } & { - 5 } & { \vdots } & { - 7 } \\ { 0 } & { - 4 } & { - 1 } & { - 7 } & { \vdots } & { - 1 5 } \\ { 0 } & { 3 } & { 3 } & { 2 } & { \vdots } & { 8 } \end{array} } \right] \quad { \mathrm { a n d } } \quad \left[ { \begin{array} { r r r r r r } { 1 } & { 1 } & { 0 } & { 3 } & { \vdots } & { 4 } \\ { 0 } & { - 1 } & { - 1 } & { - 5 } & { \vdots } & { - 7 } \\ { 0 } & { 0 } & { 3 } & { 1 3 } & { \vdots } & { 1 3 } \\ { 0 } & { 0 } & { 0 } & { - 1 3 } & { \vdots } & { - 1 3 } \end{array} } \right] .
$$

The final matrix can now be transformed into its corresponding linear system, and solutions for $x _ { 1 } , x _ { 2 } , x _ { 3 }$ ,and $x _ { 4 }$ ,can be obtained. The procedure involved in this process is called Gaussian elimination with backward substitution.

The general Gaussian elimination procedure applied to the linear system

$$
\begin{array} { r l } { E _ { 1 } : } & { a _ { 1 1 } x _ { 1 } + a _ { 1 2 } x _ { 2 } + \cdot \cdot \cdot + a _ { 1 n } x _ { n } = b _ { 1 } , } \\ { E _ { 2 } : } & { a _ { 2 1 } x _ { 1 } + a _ { 2 2 } x _ { 2 } + \cdot \cdot \cdot + a _ { 2 n } x _ { n } = b _ { 2 } , } \\ & { \qquad \vdots } \\ { E _ { n } : } & { a _ { n 1 } x _ { 1 } + a _ { n 2 } x _ { 2 } + \cdot \cdot \cdot + a _ { n n } x _ { n } = b _ { n } , } \end{array}
$$

is handled in a similar manner. First form the augmented matrix $\tilde { A }$ ：

$$
\tilde { A } = [ A , \mathbf { b } ] = \left[ \begin{array} { c c c c c c } { a _ { 1 1 } } & { a _ { 1 2 } } & { \cdot \cdot \cdot } & { a _ { 1 n } } & { \vdots } & { a _ { 1 , n + 1 } } \\ { a _ { 2 1 } } & { a _ { 2 2 } } & { \cdot \cdot \cdot } & { a _ { 2 n } } & { \vdots } & { a _ { 2 , n + 1 } } \\ { \vdots } & { \vdots } & & { \vdots } & { \vdots } & { \vdots } \\ { a _ { n 1 } } & { a _ { n 2 } } & { \cdot \cdot \cdot } & { a _ { n n } } & { \vdots } & { a _ { n , n + 1 } } \end{array} \right] ,
$$

where $A$ denotes the matrix formed by the coeficients.The entries in the $( n + 1 )$ st column are the values of b; that is, $a _ { i , n + 1 } = b _ { i }$ for each $i = 1 , 2 , \dots , n$

Provided $a _ { 1 1 } \neq 0$ ,the operations corresponding to $( E _ { j } - ( a _ { j 1 } / a _ { 1 \downarrow } ) E _ { 1 } )  ( E _ { j } )$ are performed for each $j = 2 , 3 , \dots , n$ to eliminate the coefficient of $x _ { 1 }$ in each of these rows.Although the entries in rows $2 , 3 , \ldots , n$ are expected to change, for ease of notation we again denote the entry in the $i$ th row and the $j$ th column by $a _ { i j }$ . With this in mind, we follow a sequential procedure for $i = 2 , 3 , \ldots , n - 1$ and perform the operation $( E _ { j } - ( a _ { j i } / a _ { i i } ) E _ { i } )  ( E _ { j } )$ for each $j = i + 1 , i + 2 , . . . , n$ ， provided $a _ { i i } \neq 0$ .This eliminates (changes the coefficient to zero) $x _ { i }$ in each row below the ith for all values of $i = 1 , 2 , \dots , n - 1 .$ The resulting matrix has the form:

$$
\tilde { \tilde { A } } = \left[ \begin{array} { c c c c c } { a _ { 1 1 } } & { a _ { 1 2 } } & { \cdots } & { a _ { 1 n } } & { \vdots } & { a _ { 1 , n + 1 } } \\ { 0 . } & { a _ { 2 2 } } & { \cdots } & { a _ { 2 n } } & { \vdots } & { a _ { 2 , n + 1 } } \\ { \vdots } & { \ddots } & { \ddots } & { \vdots } & { \vdots } & { \vdots } \\ { 0 . } & { \cdots } & { \cdots } & { \vdots } & { \vdots } & { a _ { n , n } } \end{array} \right] ,
$$

where,except in the first row, the values of $a _ { i j }$ are not expected to agree with those in the original matrix $\tilde { A }$ . The matrix $\tilde { \tilde { A } }$ represents a linear system with the same solution set as the original system (6.4). Since the new linear system is triangular,

$$
\begin{array} { r } { a _ { 1 1 } x _ { 1 } + a _ { 1 2 } x _ { 2 } + \cdot \cdot \cdot + a _ { 1 n } x _ { n } = a _ { 1 , n + 1 } , } \\ { a _ { 2 2 } x _ { 2 } + \cdot \cdot \cdot + a _ { 2 n } x _ { n } = a _ { 2 , n + 1 } , } \\ { \cdot \cdot \cdot \cdot \cdot \quad \vdots \qquad \vdots \qquad \vdots } \\ { a _ { n n } x _ { n } = a _ { n , n + 1 } , } \end{array}
$$

backward substitution can be performed. Solving the $\pmb { n }$ th equation for $x _ { n }$ gives

$$
x _ { n } = { \frac { a _ { n , n + 1 } } { a _ { n n } } } .
$$

Solving the $( n - 1 )$ st equation for $x _ { n - 1 }$ and using $x _ { n }$ yields

$$
x _ { n - 1 } = { \frac { a _ { n - 1 , n + 1 } - a _ { n - 1 , n } x _ { n } } { a _ { n - 1 , n - 1 } } } .
$$

Continuing this process, we obtain

$$
x _ { i } = { \frac { a _ { i , n + 1 } - a _ { i , n } x _ { n } - a _ { i , n - 1 } x _ { n - 1 } - \cdot \cdot \cdot - a _ { i , i + 1 } x _ { i + 1 } } { a _ { i i } } } = { \frac { a _ { i , n + 1 } - \sum _ { j = i + 1 } ^ { n } a _ { i j } x _ { j } } { a _ { i i } } } ,
$$

for each $i = n - 1 , n - 2 , \ldots , 2 , 1$

The Gaussian elimination procedure can be presented more precisely,_although more intricately, by forming a sequence of augmented matrices A(), A2),..., A(n), where A(1) is the matrix $\tilde { A }$ given in (6.5) and $\tilde { A } ^ { ( k ) }$ , for each $k = 2 , 3 , \ldots , n$ , has entries $a _ { i j } ^ { ( k ) }$ , where:

$$
\mathbf { \Phi } _ { i j } ^ { ( k ) } = \left\{ \begin{array} { l l } { a _ { i j } ^ { ( k - 1 ) } , } & { \mathrm { w h e n } i = 1 , 2 , \dots , k - 1 \mathrm { ~ a n d ~ } j = 1 , 2 , \dots , n + 2 , } \\ { 0 , } & { \mathrm { w h e n } i = k , k + 1 , \dots , n \mathrm { ~ a n d ~ } j = 1 , 2 , \dots , k - 1 \mathrm { ~ a n d ~ } } \\ { a _ { i j } ^ { ( k - 1 ) } - \frac { a _ { i , k - 1 } ^ { ( k - 1 ) } } { a _ { k - 1 , k - 1 } ^ { ( k - 1 ) } } a _ { k - 1 , j } ^ { ( k - 1 ) } , } & { \mathrm { w h e n } i = k , k + 1 , \dots , n \mathrm { ~ a n d ~ } j = k , k + 1 , \dots , } \end{array} \right.
$$

Thus,

$$
\tilde { A } ^ { ( k ) } = \left[ \begin{array} { l l l l l l l l l } { a _ { 1 1 } ^ { ( 1 ) } } & { a _ { 1 2 } ^ { ( 1 ) } } & { a _ { 1 3 } ^ { ( 1 ) } } & { \cdots } & { a _ { 1 , k - 1 } ^ { ( 1 ) } } & { a _ { 1 k } ^ { ( 1 ) } } & { \cdots } & { a _ { 1 n } ^ { ( 1 ) } } & { \vdots } & { a _ { 1 , n + 1 } ^ { ( 1 ) } } \\ { 0 } & { \ldots } & { a _ { 2 2 } ^ { ( 2 ) } } & { \ldots } & { a _ { 2 , k - 1 } ^ { ( 2 ) } } & { a _ { 2 k } ^ { ( 2 ) } } & { \ldots } & { a _ { 2 n } ^ { ( 2 ) } } & { \vdots } & { a _ { 2 n + 1 } ^ { ( 2 ) } } \\ { \vdots } & { \ddots } & { \ddots } & { \vdots } & { \vdots } & { \vdots } & { } & { \vdots } & { \vdots } \\ { \vdots } & { \ddots } & { \ddots } & { \ddots } & { \vdots } & { \vdots } & { \vdots } & { \vdots } & { \vdots } \\ { \vdots } & { \ddots } & { \ddots } & { \ddots } & { \vdots } & { a _ { k - 1 , k - 1 } ^ { ( k - 1 ) } } & { a _ { k - 1 , k } ^ { ( k - 1 ) } } & { \ldots } & { a _ { k - 1 , n } ^ { ( k - 1 ) } } & { \vdots } & { a _ { k - 1 , n + 1 } ^ { ( k - 1 ) } } \\ { \vdots } & { \ddots } & { \vdots } & { a _ { k k } ^ { ( k ) } } & { \cdots } & { a _ { k n } ^ { ( k ) } } & { \vdots } & { a _ { k , n + 1 } ^ { ( k ) } } \\ { \vdots } & { \vdots } & { \vdots } & { \vdots } & { \vdots } & { \vdots } & { \vdots } \\ { \vdots } & { \vdots } & { \vdots } & { \vdots } & { \vdots } & { \vdots } & { \vdots } \\ { 0 } & { \ldots } & { \ldots } & { \ldots } & { \ldots } & { \ldots } & { 0 } & { a _ { n } ^ { ( k ) } } & { \vdots } & { a _ { n , n + 1 } ^ { ( k ) } } \end{array} \right]
$$

represents the equivalent linear system for which the variable $x _ { k - 1 }$ has just been eliminated from equations $E _ { k } , E _ { k + 1 } , \ldots , E _ { n }$

Theprocedure willfailfoneoftheelents $a _ { 1 1 } ^ { ( 1 ) } , a _ { 2 2 } ^ { ( 2 ) } , a _ { 3 3 } ^ { ( 3 ) } , \dots , a _ { n - 1 , n - 1 } ^ { ( n - 1 ) } , a _ { n n } ^ { ( n ) }$ is zero because the step

$$
\left( E _ { i } - \frac { a _ { i , k } ^ { ( k ) } } { a _ { k k } ^ { ( k ) } } E _ { k } \right) \to E _ { i }
$$

$a _ { 1 1 } ^ { ( 1 ) } , \ldots , a _ { n - 1 , n - 1 } ^ { ( n - 1 ) }$ $a _ { n n } ^ { ( n ) } = 0 )$   
solution,but the technique for finding the solution must be altered.An illustration is given   
in the following example.

# EXAMPLE 3 Consider the linear system

$$
\begin{array} { c c c } { { E _ { 1 } : } } & { { x _ { 1 } - \ x _ { 2 } + 2 x _ { 3 } - \ x _ { 4 } = \ - 8 , } } \\ { { E _ { 2 } : } } & { { 2 x _ { 1 } - 2 x _ { 2 } + 3 x _ { 3 } - 3 x _ { 4 } = - 2 0 , } } \\ { { E _ { 3 } : } } & { { x _ { 1 } + \ x _ { 2 } + \ x _ { 3 } } } & { { = \ - 2 , } } \\ { { E _ { 4 } : } } & { { x _ { 1 } - \ x _ { 2 } + 4 x _ { 3 } + 3 x _ { 4 } = \ 4 . } } \end{array}
$$

The augmented matrix is

$$
\tilde { A } = \tilde { A } ^ { ( 1 ) } = \left[ \begin{array} { r r r r r } { 1 } & { - 1 } & { 2 } & { - 1 } & { \vdots } & { - 8 } \\ { 2 } & { - 2 } & { 3 } & { - 3 } & { \vdots } & { - 2 0 } \\ { 1 } & { 1 } & { 1 } & { 0 } & { \vdots } & { - 2 } \\ { 1 } & { - 1 } & { 4 } & { 3 } & { \vdots } & { 4 } \end{array} \right] ,
$$

and performing the operations

$$
( E _ { 2 } \to 2 E _ { 1 } ) \to ( E _ { 2 } ) , ( E _ { 3 } - E _ { 1 } ) \to ( E _ { 3 } ) , \mathrm { a n d } ( E _ { 4 } - E _ { 1 } ) \to ( E _ { 4 } ) ,
$$

gives

$$
\tilde { A } ^ { ( 2 ) } = \left[ \begin{array} { r r r r r } { { 1 } } & { { - 1 } } & { { 2 } } & { { - 1 } } & { { \vdots } } & { { - 8 } } \\ { { 0 } } & { { 0 } } & { { - 1 } } & { { - 1 } } & { { \vdots } } & { { - 4 } } \\ { { 0 } } & { { 2 } } & { { - 1 } } & { { 1 } } & { { \vdots } } & { { 6 } } \\ { { 0 } } & { { 0 } } & { { 2 } } & { { 4 } } & { { \vdots } } & { { 1 2 } } \end{array} \right] .
$$

Since $a _ { 2 2 } ^ { ( 2 ) }$ ,called the pivot element,iszrothe procedurecannotcontiueitsresent form. But the operation $( E _ { i } )  ( E _ { j } )$ is permited, so a search is made of the elements $a _ { 3 2 } ^ { ( 2 ) }$ and $a _ { 4 2 } ^ { ( 2 ) }$ forthe first nonzeroelementSince $a _ { 3 2 } ^ { ( 2 ) } \neq 0$ the operation $( E _ { 2 } )  ( E _ { 3 } )$ is performed to obtain a new matrix,

$$
\tilde { A } ^ { ( 2 ) ^ { \prime } } = \left[ \begin{array} { r r r r r } { { 1 } } & { { - 1 } } & { { 2 } } & { { - 1 } } & { { \vdots } } & { { - 8 } } \\ { { 0 } } & { { 2 } } & { { - 1 } } & { { 1 } } & { { \vdots } } & { { 6 } } \\ { { 0 } } & { { 0 } } & { { - 1 } } & { { - 1 } } & { { \vdots } } & { { - 4 } } \\ { { 0 } } & { { 0 } } & { { 2 } } & { { 4 } } & { { \vdots } } & { { 1 2 } } \end{array} \right] .
$$

Since $x _ { 2 }$ is already eliminated from $E _ { 3 }$ and $E _ { 4 }$ ， $\tilde { A } ^ { ( 3 ) }$ will be $\tilde { A } ^ { ( 2 ) ^ { \prime } }$ , and the computations continue with the operation $( E _ { 4 } + 2 E _ { 3 } )  ( E _ { 4 } )$ ,giving

$$
\tilde { A } ^ { ( 4 ) } = \left[ \begin{array} { r r r r r } { { 1 } } & { { - 1 } } & { { 2 } } & { { - 1 } } & { { \vdots } } & { { - 8 } } \\ { { 0 } } & { { 2 } } & { { - 1 } } & { { 1 } } & { { \vdots } } & { { 6 } } \\ { { 0 } } & { { 0 } } & { { - 1 } } & { { - 1 } } & { { \vdots } } & { { - 4 } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { 2 } } & { { \vdots } } & { { 4 } } \end{array} \right] .
$$

Finally, the backward substitution is applied:

$$
\begin{array} { l } { \displaystyle x _ { 4 } = \frac 4 2 = 2 , } \\ { \displaystyle x _ { 3 } = \frac { [ - 4 - ( - 1 ) x _ { 4 } ] } { - 1 } = 2 , } \\ { \displaystyle x _ { 2 } = \frac { [ 6 - x _ { 4 } - ( - 1 ) x _ { 3 } ] } { 2 } = 3 , } \\ { \displaystyle x _ { 1 } = \frac { [ - 8 - ( - 1 ) x _ { 4 } - 2 x _ { 3 } - ( - 1 ) x _ { 2 } ] } { 1 } = - 7 . } \end{array}
$$

Example 2 illustrates what is done if ak $a _ { k k } ^ { ( k ) } = 0$ for some $k = 1 , 2 , \dots , n - 1$ .The $k$ th column of $\tilde { A } ^ { ( k - 1 ) }$ from the $k$ th row to the nth row is searched for the first nonzero entry. If $a _ { p k } ^ { ( k ) } \neq 0$ for some $p$ with $k + 1 \leq p \leq n$ , then the operation $( \vec { E } _ { k } )  ( \vec { E } _ { p } )$ is performed to obtain $\tilde { A } ^ { ( k - 1 ) ^ { \prime } }$ . The procedure can then be continued to form $\tilde { A } ^ { ( k ) }$ , and so on. fap $a _ { p k } ^ { ( k ) } = 0$ for each $p$ , it can be shown (see Theorem 6.16 in Section 6.4) that the linear system does not have a unique solution and the procedure stops.Finally, if $a _ { n n } ^ { ( n ) } = 0$ ,the linear system does not have a unique solution,and again the procedure stops. Algorithm 6.1 summarizes Gaussian elimination with backward substitution. The algorithm incorporates pivoting when one of the pivots $a _ { k k } ^ { ( k ) }$ is Oby interchanging the $k$ th row with the $p$ th row, wherepis tesmallstinteger greartankforwhichaa is nonzero.