This method has local truncation error of order $O ( k ^ { 2 } + h ^ { 2 } )$ , but unfortunately it also has serious stability problems (see Exercise 6).

A more rewarding method is derived by averaging the Forward-Difference method at the $j$ th step in $t$ ，

$$
{ \frac { w _ { i , j + 1 } - w _ { i , j } } { k } } - \alpha ^ { 2 } { \frac { w _ { i + 1 , j } - 2 w _ { i , j } + w _ { i - 1 , j } } { h ^ { 2 } } } = 0 ,
$$

which has local truncation error

$$
\tau _ { F } = \frac { k } { 2 } \frac { \partial ^ { 2 } u } { \partial t ^ { 2 } } ( x _ { i } , \mu _ { j } ) + { \cal O } ( h ^ { 2 } ) ,
$$

and the Backward-Difference method at the $( j + 1 )$ st step in $t$ ，

$$
{ \frac { w _ { i , j + 1 } - w _ { i , j } } { k } } - \alpha ^ { 2 } { \frac { w _ { i + 1 , j + 1 } - 2 w _ { i , j + 1 } + w _ { i - 1 , j + 1 } } { h ^ { 2 } } } = 0 ,
$$

which has local truncation error

$$
\tau _ { B } = - \frac { k } { 2 } \frac { \partial ^ { 2 } u } { \partial t ^ { 2 } } ( x _ { i } , \hat { u } _ { j } ) + { \cal O } ( h ^ { 2 } ) .
$$

If we assume that

$$
\frac { \partial ^ { 2 } u } { \partial t ^ { 2 } } ( x _ { i } , \hat { \mu } _ { j } ) \approx \frac { \partial ^ { 2 } u } { \partial t ^ { 2 } } ( x _ { i } , \mu _ { j } ) ,
$$

then the averaged-difference method,

$$
\frac { w _ { i , j + 1 } - w _ { i j } } { k } - \frac { \alpha ^ { 2 } } { 2 } \Bigg [ \frac { w _ { i + 1 , j } - 2 w _ { i , j } + w _ { i - 1 , j } } { h ^ { 2 } } + \frac { w _ { i + 1 , j + 1 } - 2 w _ { i , j + 1 } + w _ { i - 1 , j + 1 } } { h ^ { 2 } } \Bigg ] =
$$

has local truncation error of order $O ( k ^ { 2 } + h ^ { 2 } )$ ，provided, of course, that the usual differentiability conditions are satisfied. This is known as the Crank-Nicolson method and is represented in the matrix form

$$
A \mathbf { w } ^ { ( j + 1 ) } = B \mathbf { w } ^ { ( j ) } , \quad \mathrm { f o r } \operatorname { e a c h } j = 0 , 1 , 2 , \ldots ,
$$

where

$$
\boldsymbol { \lambda } = \alpha ^ { 2 } \frac { k } { h ^ { 2 } } , \quad \mathbf { w } ^ { ( j ) } = ( w _ { 1 , j } , w _ { 2 , j } , \dots , w _ { m - 1 , j } ) ^ { t } ,
$$

and the matrices $A$ and $B$ are given by:

$$
A = \left[ \begin{array} { c c c c c c c } { \left( 1 + \lambda \right) } & { - \frac { \lambda } { 2 } . } & { 0 } & { \dots } & { \dots } & { 0 } \\ { - \frac { \lambda } { 2 } . } & { . } & { . } & { . } & { . } & { . } \\ { 0 } & { . } & { . } & { . } & { . } & { . } \\ { \vdots } & { . } & { . } & { . } & { . } & { . } \\ { . } & { . } & { . } & { . } & { . } & { - \frac { \lambda } { 2 } } \\ { 0 } & { . } & { . } & { . } & { . } & { \vdots } & { \vdots } \\ { 0 } & { . } & { . } & { . } & { . } & { \vdots } & { \vdots } \end{array} \right]
$$

and

$$
B = [ \begin{array} { l } { ( 1 - \lambda ) ^ { \underline { { { \lambda } } } } _ { \ddots } \underset { \ddots } { \underline { { { \lambda } } } } _ { \ddots } 0 ^ { : \underline { { { \lambda } } } \dots \dots \dots \ddots } 0 } \\ { \frac { \lambda } { 2 } \underset { \ddots } { \underline { { { \lambda } } } } _ { \ddots } \underset { \ddots } { \underline { { { \lambda } } } } _ { \ddots } \underset { \ddots } { \underline { { { \lambda } } } } _ { \ddots } \underset { \ddots } { \underline { { { \lambda } } } } _ { \ddots } \underset { \ddots } { \underline { { { \lambda } } } } } \\ { 0 \underset { \vdots } { \underline { { { \lambda } } } } _ { \ddots } \underset { \ddots } { \underline { { { \lambda } } } } _ { \ddots } \underset { \ddots } { \underline { { { \lambda } } } } _ { \ddots } \underset { \ddots } { \underline { { { \lambda } } } } _ { \ddots } \underset { \vdots } { \underline { { { \lambda } } } } } \\ { \vdots } & { \vdots } \\ { 0 \underset { \ddots } { \underline { { { \lambda } } } } _ {  \dots \dots \dots \dots \dots } 0 \overset { \lambda } { \underset { \ddots } { \underline { { { \lambda } } } } } _ { \texttt { ( 1 - \lambda ) } } } \end{array} ] .
$$

Since $A$ is a positive definite, strictly diagonally dominant, and tridiagonal matrix, it is nonsingular. Either the Crout Factorization 6.7 or the SOR Algorithm 7.3 can be used to obtain $\mathbf { w } ^ { ( j + 1 ) }$ from $\pmb { w } ^ { ( j ) }$ , for each $j = 0$ ,1,2,.... Algorithm 12.3 incorporates Crout factorization into the Crank-Nicolson technique.As in Algorithm 12.2,a finite length for the time interval must be specified to determine a stopping procedure. The verification that the Crank-Nicolson method is unconditionally stable and has order of convergence $O ( k ^ { 2 } + h ^ { 2 } )$ can be found in [IK, pp.508-512].

# Crank-Nicolson

To approximate the solution to the parabolic partial differential equation

![](images/9711151849e79d5a7945accb75685abd7213b7e08c1a80aa6de6e4cbc317efcc.jpg)

$$
\frac { \partial u } { \partial t } ( x , t ) - \alpha ^ { 2 } \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } ( x , t ) = 0 , \quad 0 < x < l , \quad 0 < t < T ,
$$

subject to the boundary conditions

$$
u ( 0 , t ) = u ( l , t ) = 0 , \quad 0 < t < T ,
$$

and the initial conditions

$$
u ( x , 0 ) = f ( x ) , \quad 0 \leq x \leq l { \mathrm { : } }
$$

INPUT endpoint $l$ ; maximum time $T$ ; constant $\pmb { \alpha }$ ; integers $m \ge 3 , N \ge 1$

OUTPUTapproximations $w _ { i , j }$ to $u ( x _ { i } , t _ { j } )$ for each $i = 1 , \ldots , m - 1$ and $j = 1 , \dots , N$

Step 1 Set $\begin{array} { c } { \mathrm { t } h = l / m ; } \\ { k = T / N ; } \\ { \lambda = \alpha ^ { 2 } k / h ^ { 2 } ; } \\ { w _ { m } = 0 . } \end{array}$

Step 2 For $i = 1 , \ldots , m - 1$ set $w _ { i } = f ( i h )$ .(Initial values.) (Steps 3-11 solve a tridiagonal linear system using Algorithm 6.7.)

$$
\begin{array} { r l } { s t e p 3 } & { { } \mathrm { S e t } l _ { 1 } = 1 + \lambda ; } \\ { \quad } & { { } \quad u _ { 1 } = - \lambda / ( 2 l _ { 1 } ) . } \end{array}
$$

Step 4 For $i = 2 , \ldots , m - 2$ set $l _ { i } = 1 + \lambda + \lambda u _ { i - 1 } / 2 ;$ $u _ { i } = - \lambda / ( 2 l _ { i } )$ ：

Step 5 Set $l _ { m - 1 } = 1 + \lambda + \lambda u _ { m - 2 } / 2$

Step 6 For $j = 1 , \dots , N$ do Steps 7-11.

Step 7 Set $t = j k$ ： (Current tj.)

$$
z _ { 1 } = \biggl [ ( 1 - \lambda ) w _ { 1 } + \frac { \lambda } { 2 } w _ { 2 } \biggr ] \bigg / l _ { 1 } .
$$

Step 8For $i = 2 , \ldots , m - 1$ set

$$
z _ { i } = \Biggl [ ( 1 - \lambda ) w _ { i } + \frac { \lambda } { 2 } ( w _ { i + 1 } + w _ { i - 1 } + z _ { i - 1 } ) \Biggr ] \Biggl / l _ { i } .
$$

Step9 Set $w _ { m - 1 } = z _ { m - 1 }$

Step 10Fo1 $\div i = m - 2 , \ldots , 1$ set $w _ { i } = z _ { i } - u _ { i } w _ { i + 1 }$

Step 11 OUTPUT (t)； $( N o t e . i \ t = t _ { j } .$ ）For $i = 1$ ，., $m - 1$ set $x = i h$ ；OUTPUT $( x , w _ { i } )$ (Note: $w _ { i } = w _ { i , j } .$ ）

Step 12 STOP. (The procedure is complete.)

The Crank-Nicolson method willbe used to approximate the solution to the problem in Examples 1 and 2,consisting of the equation

$$
\frac { \partial u } { \partial t } ( x , t ) - \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } ( x , t ) = 0 , \quad 0 < x < 1 \quad 0 < t ,
$$

subject to the conditions

$$
u ( 0 , t ) = u ( 1 , t ) = 0 , \quad 0 < t ,
$$

and

$$
u ( x , 0 ) = \sin ( \pi x ) , \quad 0 \leq x \leq 1 .
$$

The choices $m = 1 0 , h = 0 . 1 , N = 5 0 , k = 0 . 0 1$ ,and $\lambda = 1$ are used in Algorithm 12.3, as they were in the previous examples. The results in Table 12.5 indicate the increase in

# Table 12.5

<table><tr><td>Xi</td><td>Wi,50</td><td>u(x;,0.5)</td><td>lwi,so - u(xi,0.5)1</td></tr><tr><td>0.0</td><td>0</td><td>0</td><td></td></tr><tr><td>0.1</td><td>0.00230512</td><td>0.00222241</td><td>8.271 × 10-5</td></tr><tr><td>0.2</td><td>0.00438461</td><td>0.00422728</td><td>1.573 × 10-4</td></tr><tr><td>0.3</td><td>0.00603489</td><td>0.00581836</td><td>2.165 × 10-4</td></tr><tr><td>0.4</td><td>0.00709444</td><td>0.00683989</td><td>2.546× 10-4</td></tr><tr><td>0.5</td><td>0.00745954</td><td>0.00719188</td><td>2.677 × 10-4</td></tr><tr><td>0.6</td><td>0.00709444</td><td>0.00683989</td><td>2.546 × 10-4</td></tr><tr><td>0.7</td><td>0.00603489</td><td>0.00581836</td><td>2.165×1 10-4</td></tr><tr><td>0.8</td><td>0.00438461</td><td>0.00422728</td><td>1.573 × 10-4</td></tr><tr><td>0.9</td><td>0.00230512</td><td>0.00222241</td><td>8.271 × 10-5</td></tr><tr><td>1.0</td><td>0</td><td>0</td><td></td></tr></table>

accuracy of the Crank-Nicolson method over the Backward-Difference method,the best of the two previously discussed techniques. ■

# ExERCIse SEt 12.2

1. Approximate the solution to the following partial differential equations using the Backward-Difference Algorithm.

$$
\begin{array} { c c c } { { \bf a . } } & { { \displaystyle \frac { \partial u } { \partial t } - \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } = 0 , } } & { { 0 < x < 2 , 0 < t ; } } \\ { { } } & { { } } & { { u ( 0 , t ) = u ( 2 , t ) = 0 , 0 < t , } } \\ { { } } & { { } } & { { u ( x , 0 ) = \displaystyle \sin \frac { \pi } { 2 } x , 0 \leq x \leq 2 . } } \end{array}
$$

Use $m = 4 , T = 0 . 1$ ，and $N \ = \ 2$ , and compare your results to the actual solution $u ( x , t ) = e ^ { - ( \pi ^ { 2 } / 4 ) t } \sin { \frac { \pi } { 2 } } x$

$$
\begin{array} { c c } { { \bf b . ~ } } & { { \displaystyle \frac { \partial u } { \partial t } - \frac { 1 } { 1 6 } \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } = 0 , } } & { { 0 < x < 1 , ~ 0 < t ; } } \\ { { } } & { { } } & { { u ( 0 , t ) = u ( 1 , t ) = 0 , \quad 0 < t , } } \\ { { } } & { { } } & { { u ( x , 0 ) = 2 \sin { 2 \pi x } , \quad 0 \leq x \leq 1 . } } \end{array}
$$

Us $\textsf { e m } = 3 , T \ = \ 0 . 1$ and $N \simeq 2$ , and compare your results to the actual solution $u ( x , t ) = 2 e ^ { - ( \pi ^ { 2 } / 4 ) t } \sin 2 \pi x$

2.Repeat Exercise 1 using the Crank-Nicolson Algorithm.

3.Use the Forward-Difference method to approximate the solution to the following parabolic partial differential equations.

$$
\begin{array} { c } { { \displaystyle { \frac { \partial u } { \partial t } } - \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } = 0 , \quad 0 < x < 2 , 0 < t ; } } \\ { { u ( 0 , t ) = u ( 2 , t ) = 0 , \quad 0 < t , } } \\ { { u ( x , 0 ) = \sin 2 \pi x , \quad 0 \leq x \leq 2 . } } \end{array}
$$

Use $h = 0 . 4$ and $k = 0 . 1$ ,and compare your results at $t = 0 . 5$ to the actual solution $u ( x , t ) = e ^ { - 4 \pi ^ { 2 } t } \sin { 2 \pi x }$ . Then use $h = 0 . 4$ and $k = 0 . 0 5$ , and compare the answers.

$$
\begin{array} { c } { { \displaystyle { \frac { \partial u } { \partial t } } - \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } = 0 , \quad 0 < x < \pi , 0 < t ; } } \\ { { u ( 0 , t ) = u ( \pi , t ) = 0 , \quad 0 < t , } } \\ { { u ( x , 0 ) = \sin x , \quad 0 \leq x \leq \pi . } } \end{array}
$$

Use $h = \pi / 1 0$ and $k = 0 . 0 5$ , and compare your results at $t = 0 . 5$ to the actual solution $u ( x , t ) = e ^ { - t } \sin x$ ，

$$
\begin{array} { l } { \displaystyle - \frac { _ 4 } { \pi ^ { 2 } } \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } = 0 , \quad 0 < x < 4 , 0 < t ; } \\ { \displaystyle u ( 0 , t ) = u ( 4 , t ) = 0 , \quad 0 < t , } \\ { \displaystyle u ( x , 0 ) = \sin \frac { \pi } { 4 } x \left( 1 + 2 \cos \frac { \pi } { 4 } x \right) , \quad 0 \leq x \leq 4 . } \end{array}
$$

Use $h = 0 . 2$ and $k = 0 . 0 4$ , and compare your results at $t = 0 . 4$ to the actual solution $u ( x , t ) = e ^ { - t }$ sin $\frac { \pi } { 2 } x + e ^ { - t / 4 } \sin \frac { \pi } { 4 } x$

$$
\frac { \partial u } { \partial t } - \frac { 1 } { \pi ^ { 2 } } \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } = 0 , \quad 0 < x < 1 , \ 0 < t ;
$$

$$
u ( 0 , t ) = u ( 1 , t ) = 0 , \quad 0 < t ,
$$

$$
\begin{array} { r } { u ( x , 0 ) = \cos \pi \left( x - \frac { 1 } { 2 } \right) , \quad 0 \leq x \leq 1 . } \end{array}
$$

Use $h = 0 . 1$ and $k = 0 . 0 4$ , and compare your results at $t = 0 . 4$ to the actual solution $u ( x , t ) = e ^ { - t } \cos \pi ( x - { \textstyle \frac { 1 } { 2 } } )$

4.Repeat Exercise 3 using the Backward-Diference Algorithm.

5.Repeat Exercise 3 using the Crank-Nicolson Algorithm.

6. Repeat Exercise 3 using Richardson's method.

7.Show that the eigenvalues for the $( m - 1 )$ by $( m - 1 )$ tridiagonal method matrix $\pmb { A }$ given by

$$
a _ { i j } = \left\{ \begin{array} { l l } { \lambda , } & { j = i - 1 \mathrm { o r } j = i + 1 , } \\ { 1 - 2 \lambda , } & { j = i , } \\ { 0 , } & { \mathrm { o t h e r w i s e } } \end{array} \right.
$$

are

$$
\mu _ { i } = 1 - 4 \lambda \left( \sin \frac { i \pi } { 2 m } \right) ^ { 2 } , \quad \mathrm { f o r e a c h } i = 1 , 2 , \ldots , m - 1 ,
$$

with corresponding eigenvectors $\mathbf { v } ^ { ( i ) }$ ,where $\begin{array} { r } { v _ { j } ^ { ( i ) } = \sin { \frac { i j \pi } { m } } } \end{array}$

8.Show that the $( m - 1 )$ by $( m - 1 )$ tridiagonal method matrix $\pmb { A }$ given by

$$
a _ { i j } = { \left\{ \begin{array} { l l } { - \lambda , } & { j = i - 1 { \mathrm { ~ o r ~ } } j = i + 1 , } \\ { 1 + 2 \lambda , } & { j = i , } \\ { 0 , } & { { \mathrm { o t h e r w i s e } } , } \end{array} \right. }
$$

where $\lambda > 0$ ,is positive definite and diagonally dominant and has eigenvalues

$$
\mu _ { i } = 1 + 4 \lambda \left( \sin \frac { i \pi } { 2 m } \right) ^ { 2 } , \quad \mathrm { f o r } \operatorname { e a c h } i = 1 , 2 , \dots , m - 1 ,
$$

with corresponding eigenvectors $\mathbf { v } ^ { ( i ) }$ , where $\begin{array} { r } { v _ { j } ^ { ( i ) } = \sin { \frac { i j \pi } { m } } } \end{array}$

9.Modify Algorithms 12.2 and 12.3 to include the parabolic partial differential equation

$$
\begin{array} { c } { { \displaystyle { \frac { \partial u } { \partial t } } - \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } = F ( x ) , \quad 0 < x < l , 0 < t ; } } \\ { { { } } } \\ { { u ( 0 , t ) = u ( l , t ) = 0 , \quad 0 < t ; } } \\ { { { } } } \\ { { u ( x , 0 ) = f ( x ) , \quad 0 \leq x \leq l . } } \end{array}
$$

10.Use the results of Exercise 9 to approximate the solution to

$$
\begin{array} { c } { { \displaystyle { \frac { \partial u } { \partial t } } - \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } = 2 , \quad 0 < x < 1 , 0 < t ; } } \\ { { u ( 0 , t ) = u ( 1 , t ) = 0 , \quad 0 < t ; } } \\ { { u ( x , 0 ) = \sin \pi x + x ( 1 - x ) , } } \end{array}
$$

with $h = 0 . 1$ and ${ k = 0 . 0 1 }$ . Compare your answer at $t = 0 . 2 5$ to the actual solution $u ( x , t ) =$ $e ^ { - \pi ^ { 2 } t } \sin \pi x + x ( 1 - x )$

11.Change Algorithms 12.2 and 12.3 to accommodate the partial differential equation

$$
\begin{array} { c } { { \displaystyle { \frac { \partial u } { \partial t } } - \alpha ^ { 2 } \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } = 0 , \quad 0 < x < l , 0 < t ; } } \\ { { u ( 0 , t ) = \phi ( t ) , \ : u ( l , t ) = \Psi ( t ) , \quad 0 < t ; } } \\ { { u ( x , 0 ) = f ( x ) , \quad 0 \leq x \leq l , } } \end{array}
$$

where $f ( 0 ) = \phi ( 0 )$ and $f ( l ) = \Psi ( 0 )$

12. The temperature $u ( x , t )$ of along, thin rod of constant cross section and homogeneous conducting material is governed by the one-dimensional heat equation. If heat is generated in the material, for example, by resistance to current or nuclear reaction, the heat equation becomes

$$
\frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } + \frac { K r } { \rho C } = K \frac { \partial u } { \partial t } , \quad 0 < x < l , \quad 0 < t ,
$$

where $l$ is the length, $\rho$ is the density, $C$ is the specific heat, and $\pmb { K }$ is the thermal diffusivity of the rod. The function $r = r ( { \boldsymbol { x } } , t , { \boldsymbol { u } } )$ represents the heat generated per unit volume. Suppose that

$$
\begin{array} { r l r l } & { l = 1 . 5 \mathrm { c m } , } & & { K = 1 . 0 4 \mathrm { c a l } / \mathrm { c m } \cdot \mathrm { d e g } \cdot \mathbf { s } , } \\ & { \rho = 1 0 . 6 \mathrm { g } / \mathrm { c m } ^ { 3 } , } & & { C = 0 . 0 5 6 \mathrm { c a l } / \mathrm { g } \cdot \mathrm { d e g } , } \end{array}
$$

and

$$
r ( x , t , u ) = 5 . 0 \mathrm { c a l / c m ^ { 3 } \cdot s } .
$$

If the ends of the rod are kept at $\boldsymbol { 0 ^ { \circ } } \mathbf { C }$ ,then

$$
u ( 0 , t ) = u ( l , t ) = 0 , \quad t > 0 .
$$

Suppose the initial temperature distribution is given by

$$
u ( x , 0 ) = \sin \frac { \pi x } { l } , \quad 0 \leq x \leq l .
$$

Use the results of Exercise 9 to approximate the temperature distribution with $h = 0 . 1 5$ and $\pmb { k } = 0 . 0 2 2 5$

13. Sagar and Payne [SP] analyze the stress-strain relationships and material properties of a cylinder alternately subjected to heating and cooling and consider the equation

$$
\frac { \partial ^ { 2 } T } { \partial r ^ { 2 } } + \frac { 1 } { r } \frac { \partial T } { \partial r } = \frac { 1 } { 4 K } \frac { \partial T } { \partial t } , \quad \frac { 1 } { 2 } < r < 1 , \ 0 < T ,
$$

where $T = T ( r , t )$ is the temperature, $r$ is the radial distance from the center of the cylinder, t is time, and $\pmb { K }$ is a diffusivity coefficient.

a. Find approximations to $T ( r , 1 0 )$ for a cylinder with outside radius 1,given the initial and boundary conditions:

$$
\begin{array} { c } { { T ( 1 , t ) = 1 0 0 + 4 0 t , \quad 0 \leq t \leq 1 0 ; } } \\ { { { } } } \\ { { T \left( \displaystyle \frac { 1 } { 2 } , t \right) = t , \quad 0 \leq t \leq 1 0 ; } } \\ { { { } } } \\ { { T ( r , 0 ) = 2 0 0 ( r - 0 . 5 ) , \quad 0 . 5 \leq r \leq 1 . } } \end{array}
$$

Use a modification of the Backward-Difference method with $K = 0 . 1 , k = 0 . 5$ ，and $h = \Delta r = 0 . 1$

b. Use the temperature distribution of part (a) to calculate the strain $I$ by approximating the integral

$$
I = \int _ { 0 . 5 } ^ { 1 } \alpha T ( r , t ) r \ d r ,
$$

where $\alpha = 1 0 . 7$ and $\iota = 1 0$ . Use the Composite Trapezoidal method with $n = 5$

# 12.3 Hyperbolic Partial Differential Equations

In this section, we consider the numerical solution to the wave equation, an example of a hyperbolic partial differential equation. The wave equation is given by the differential equation

$$
\frac { \partial ^ { 2 } u } { \partial t ^ { 2 } } ( x , t ) - \alpha ^ { 2 } \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } ( x , t ) = 0 , \quad 0 < x < l , \quad t > 0 ,
$$

subject to the conditions

$$
\begin{array} { l } { { u ( 0 , t ) = u ( l , t ) = 0 , \quad \mathrm { f o r } \quad t > 0 , } } \\ { { { } } } \\ { { u ( x , 0 ) = f ( x ) , \quad \mathrm { a n d } \quad \displaystyle \frac { \partial u } { \partial t } ( x , 0 ) = g ( x ) , \quad \mathrm { f o r } \quad 0 \leq x \leq l , } } \end{array}
$$

where $\alpha$ is a constant. Select an integer $m > 0$ and time-step size $k > 0$ With $h = l / m$ the mesh points $( x _ { i } , t _ { j } )$ are defined by

$$
x _ { i } = i h \quad \mathrm { a n d } \quad t _ { j } = j k ,
$$

for each $i = 0 , 1 , \ldots , m$ and $j = 0 , 1 , \ldots$ . At any interior mesh point $( x _ { i } , t _ { j } )$ , the wave equation becomes

$$
{ \frac { \partial ^ { 2 } u } { \partial t ^ { 2 } } } ( x _ { i } , t _ { j } ) - \alpha ^ { 2 } { \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } } ( x _ { i } , t _ { j } ) = 0 .
$$

The difference method is obtained using the centered-difference quotient for the second partial derivatives given by

$$
\frac { \partial ^ { 2 } u } { \partial t ^ { 2 } } ( x _ { i } , t _ { j } ) = \frac { u ( x _ { i } , t _ { j + 1 } ) - 2 u ( x _ { i } , t _ { j } ) + u ( x _ { i } , t _ { j - 1 } ) } { k ^ { 2 } } - \frac { k ^ { 2 } } { 1 2 } \frac { \partial ^ { 4 } u } { \partial t ^ { 4 } } ( x _ { i } , \mu _ { j } ) ,
$$

where $\mu _ { j } \in ( t _ { j - 1 } , t _ { j + 1 } )$ and

$$
\frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } ( x _ { i } , t _ { j } ) = \frac { u ( x _ { i + 1 } , t _ { j } ) - 2 u ( x _ { i } , t _ { j } ) + u ( x _ { i - 1 } , t _ { j } ) } { h ^ { 2 } } - \frac { h ^ { 2 } } { 1 2 } \frac { \partial ^ { 4 } u } { \partial x ^ { 4 } } ( \xi _ { i } , t _ { j } ) ,
$$

where $\xi _ { i } \in ( x _ { i - 1 } , x _ { i + 1 } )$ . Substituting these into Eq. (12.17) gives

$$
\begin{array} { l } { \frac { u ( x _ { i } , t _ { j + 1 } ) - 2 u ( x _ { i } , t _ { j } ) + u ( x _ { i } , t _ { j - 1 } ) } { k ^ { 2 } } - \alpha ^ { 2 } \frac { u ( x _ { i + 1 } , t _ { j } ) - 2 u ( x _ { i } , t _ { j } ) + u ( x _ { i - 1 } , t _ { j } ) } { h ^ { 2 } } } \\ { = \frac { 1 } { 1 2 } \bigg [ k ^ { 2 } \frac { \partial ^ { 4 } u } { \partial t ^ { 4 } } ( x _ { i } , \mu _ { j } ) - \alpha ^ { 2 } h ^ { 2 } \frac { \partial ^ { 4 } u } { \partial x ^ { 4 } } ( \xi _ { i } , t _ { j } ) \bigg ] . } \end{array}
$$

Neglecting the error term

$$
\tau _ { i , j } = \frac { 1 } { 1 2 } \bigg [ k ^ { 2 } \frac { \partial ^ { 4 } u } { \partial t ^ { 4 } } ( x _ { i } , \mu _ { j } ) - \alpha ^ { 2 } h ^ { 2 } \frac { \partial ^ { 4 } u } { \partial x ^ { 4 } } ( \xi _ { i } , t _ { j } ) \bigg ] ,
$$

leads to the difference equation

$$
\frac { w _ { i , j + 1 } - 2 w _ { i , j } + w _ { i , j - 1 } } { k ^ { 2 } } - \alpha ^ { 2 } \frac { w _ { i + 1 , j } - 2 w _ { i , j } + w _ { i - 1 , j } } { h ^ { 2 } } = 0 .
$$

If $\lambda = \alpha k / h$ , we can write the difference equation as

$$
w _ { i , j + 1 } - 2 w _ { i , j } + w _ { i , j - 1 } - { \lambda } ^ { 2 } w _ { i + 1 , j } + 2 { \lambda } ^ { 2 } w _ { i , j } - { \lambda } ^ { 2 } w _ { i - 1 , j } = 0
$$

and solve for $w _ { i , j + 1 }$ , the most advanced time-step approximation, to obtain

$$
w _ { i , j + 1 } = 2 ( 1 - \lambda ^ { 2 } ) w _ { i , j } + \lambda ^ { 2 } ( w _ { i + 1 , j } + w _ { i - 1 , j } ) - w _ { i , j - 1 } .
$$

This equation holds for each $i = 1 , 2 , \dots , m - 1$ and $j = 1 , 2 , \dots$ . The boundary conditions give

$$
w _ { 0 , j } = w _ { m , j } = 0 , \quad \mathrm { f o r e a c h } j = 1 , 2 , 3 , \ldots ,
$$

and the initial condition implies that

$$
w _ { i , 0 } = f ( x _ { i } ) , \quad \mathrm { f o r e a c h } i = 1 , 2 , \ldots , m - 1 .
$$

Writing this set of equations in matrix form gives

$$
\begin{array} { r } { w _ { 1 , j + 1 } = \left[ \begin{array} { l } { 2 ( 1 - \lambda ^ { 2 } ) \quad \lambda ^ { 2 } \quad \quad 0 : \cdots \cdots \cdots \cdot 0 } \\ { w _ { 2 , j + 1 } } \\ { \vdots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \ddots \quad \ddots \vdots } \\ { \vdots \quad \ddots \quad \ddots \quad \ddots \ddots \quad \ddots \quad \ddots } \\ { \vdots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \ddots \quad \ddots } \\ { \vdots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots } \\ { \vdots \quad \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots } \\ { \vdots \quad \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \vdots } \end{array} \right] \left[ \begin{array} { l } { w _ { 1 , j } } \\ { w _ { 2 , j } } \\ { \vdots } \\ { w _ { m - 1 , j } } \end{array} \right] - \left[ \begin{array} { l } { w _ { 1 , j - 1 } } \\ { w _ { 2 , j - 1 } } \\ { \vdots } \\ { w _ { m - 1 , j - 1 } } \\ { \vdots } \end{array} \right] } \end{array}
$$

Equations (12.18) and (12.19) imply that the $( j \cdot + 1 ) \mathsf { s t }$ time step requires values from the $j$ th and $( j - 1 ) \mathsf { s t }$ : time steps. (See Figure 12.10.) This produces a minor starting problem since values for $j = 0$ are given by Eq. (12.20), but values for $j = 1$ , which are needed in Eq.(12.18) to compute $w _ { i , 2 }$ , must be obtained from the initial-velocity condition

$$
\frac { \partial u } { \partial t } ( x , 0 ) = g ( x ) , \quad 0 \leq x \leq l .
$$

![](images/ed125f45e6b864d2d9a21f8db680b587781daeb3887ba3c56ae429b5a94ac13d.jpg)  
Figure 12.10

One approach is to replace $\partial u / \partial t$ by a forward-difference approximation,

$$
\frac { \partial u } { \partial t } ( x _ { i } , 0 ) = \frac { u ( x _ { i } , t _ { 1 } ) - u ( x _ { i } , 0 ) } { k } - \frac { k } { 2 } \frac { \partial ^ { 2 } u } { \partial t ^ { 2 } } ( x _ { i } , \tilde { \mu } _ { i } ) ,
$$

for some $\tilde { \mu } _ { i }$ in $( 0 , t _ { 1 } )$ . Solving for $u ( x _ { i } , t _ { 1 } )$ gives

$$
\begin{array} { c } { { \displaystyle u ( x _ { i } , t _ { 1 } ) = u ( x _ { i } , 0 ) + k \frac { \partial u } { \partial t } ( x _ { i } , 0 ) + \frac { k ^ { 2 } } { 2 } \frac { \partial ^ { 2 } u } { \partial t ^ { 2 } } ( x _ { i } , \tilde { \mu } _ { i } ) } } \\ { { = u ( x _ { i } , 0 ) + k g ( x _ { i } ) + \displaystyle \frac { k ^ { 2 } } { 2 } \frac { \partial ^ { 2 } u } { \partial t ^ { 2 } } ( x _ { i } , \tilde { \mu } _ { i } ) . } } \end{array}
$$

As a consequence,

$$
w _ { i , 1 } = w _ { i , 0 } + k g ( x _ { i } ) , \quad \mathrm { f o r e a c h } i = 1 , \ldots , m - 1 .
$$

However, this gives anapproximation that has errorofonly $O ( k )$ . A beter approximation to $u ( x _ { i } , 0 )$ can be obtained. Consider the equation

$$
u ( x _ { i } , t _ { 1 } ) = u ( x _ { i } , 0 ) + k \frac { \partial u } { \partial t } ( x _ { i } , 0 ) + \frac { k ^ { 2 } } { 2 } \frac { \partial ^ { 2 } u } { \partial t ^ { 2 } } ( x _ { i } , 0 ) + \frac { k ^ { 3 } } { 6 } \frac { \partial ^ { 3 } u } { \partial t ^ { 3 } } ( x _ { i } , \hat { \mu } _ { i } ) ,
$$

for some $\hat { \mu } _ { i }$ in $( 0 , t _ { 1 } )$ , which comes from expanding $u ( x _ { i } , t _ { 1 } )$ in a second Maclaurin polynomial in t. If $f ^ { \prime \prime }$ exists, then

$$
{ \frac { \partial ^ { 2 } u } { \partial t ^ { 2 } } } ( x _ { i } , 0 ) = \alpha ^ { 2 } { \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } } ( x _ { i } , 0 ) = \alpha ^ { 2 } { \frac { d ^ { 2 } f } { d x ^ { 2 } } } ( x _ { i } ) = \alpha ^ { 2 } f ^ { \prime \prime } ( x _ { i } )
$$

and

$$
u ( x _ { i } , t _ { 1 } ) = u ( x _ { i } , 0 ) + k g ( x _ { i } ) + \frac { \alpha ^ { 2 } k ^ { 2 } } { 2 } f ^ { \prime \prime } ( x _ { i } ) + \frac { k ^ { 3 } } { 6 } \frac { \partial ^ { 3 } u } { \partial t ^ { 3 } } ( x _ { i } , \hat { \mu } _ { i } ) ,
$$

producing an approximation with error $O ( k ^ { 3 } )$ ：

$$
w _ { i 1 } = w _ { i 0 } + k g ( x _ { i } ) + { \frac { \alpha ^ { 2 } k ^ { 2 } } { 2 } } f ^ { \prime \prime } ( x _ { i } ) .
$$

f $f \in C ^ { 4 } [ 0 , 1 ]$ but $f ^ { \prime \prime } ( x _ { i } )$ is not readily available, we can use the difference equation in Eq. (4.9) to write

$$
f ^ { \prime \prime } ( x _ { i } ) = \frac { f ( x _ { i + 1 } ) - 2 f ( x _ { i } ) + f ( x _ { i - 1 } ) } { h ^ { 2 } } - \frac { h ^ { 2 } } { 1 2 } f ^ { ( 4 ) } ( \tilde { \xi } _ { i } ) ,
$$

for some $\tilde { \xi } _ { i }$ in $( x _ { i - 1 } , x _ { i + 1 } )$ . This implies that

$$
\iota ( x _ { i } , t _ { 1 } ) = u ( x _ { i } , 0 ) + k g ( x _ { i } ) + \frac { k ^ { 2 } \alpha ^ { 2 } } { 2 \hbar ^ { 2 } } [ f ( x _ { i + 1 } ) - 2 f ( x _ { i } ) + f ( x _ { i - 1 } ) ] + O ( k ^ { 3 } + \hbar ^ { 2 } k ^ { 2 } )
$$

Letting $\lambda = ( k \alpha / h )$ ,we have

$$
\begin{array} { r l r } & { } & { u ( x _ { i } , t _ { 1 } ) = u ( x _ { i } , 0 ) + k g ( x _ { i } ) + { \cfrac { \lambda ^ { 2 } } { 2 } } [ f ( x _ { i + 1 } ) - 2 f ( x _ { i } ) + f ( x _ { i - 1 } ) ] + O ( k ^ { 3 } + h ^ { 2 } k ^ { 2 } ) } \\ & { } & \\ & { } & { \qquad = ( 1 - \lambda ^ { 2 } ) f ( x _ { i } ) + { \cfrac { \lambda ^ { 2 } } { 2 } } f ( x _ { i + 1 } ) + { \cfrac { \lambda ^ { 2 } } { 2 } } f ( x _ { i - 1 } ) + k g ( x _ { i } ) + O ( k ^ { 3 } + h ^ { 2 } k ^ { 2 } ) . } \end{array}
$$

Thus, the difference equation,

$$
w _ { i , 1 } = ( 1 - \lambda ^ { 2 } ) f ( x _ { i } ) + \frac { \lambda ^ { 2 } } { 2 } f ( x _ { i + 1 } ) + \frac { \lambda ^ { 2 } } { 2 } f ( x _ { i - 1 } ) + k g ( x _ { i } ) ,
$$

can be used to find $w _ { i , 1 }$ ,for each $i = 1 , 2 , \ldots , m - 1$

Algorithm 12.4 uses Eq. (12.24) to approximate $w _ { i , 1 }$ ,although Eq.(12.23) could also be used. It is assumed that there is an upper bound for the value of $t$ to be used in the stopping technique, and that $k = T / N$ , where $N$ is also given.

# Wave Equation Finite-Difference

To approximate the solution to the wave equation

$$
\frac { \partial ^ { 2 } u } { \partial t ^ { 2 } } ( x , t ) - \alpha ^ { 2 } \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } ( x , t ) = 0 , \quad 0 < x < l , \quad 0 < t < T ,
$$

subject to the boundary conditions

$$
u ( 0 , t ) = u ( l , t ) = 0 , \quad 0 < t < T ,
$$

and the initial conditions

$$
\begin{array} { r l } { u ( x , 0 ) = f ( x ) , } & { { } \quad 0 \leq x \leq l , } \\ { { \frac { \partial u } { \partial t } } ( x , 0 ) = g ( x ) , } & { { } \quad 0 \leq x \leq l : } \end{array}
$$

INPUTendpoint $l$ ; maximum time $T$ ; constant $\pmb { \alpha }$ ; integers $m \geq 2 , N \geq 2$

OUTPUTapproximations $w _ { i , j }$ t0 $u ( x _ { i } , t _ { j } )$ for each $i = 0 , \ldots , m$ and $j = 0 , \ldots , N$

Step 1 Se $\begin{array} { c } { { \mathrm { \Delta t } h = l / m ; } } \\ { { k = T / N ; } } \\ { { \lambda = k \alpha / h . } } \end{array}$

Step 2 For $j = 1 , \dots , N$ set $w _ { 0 , j } = 0 \mathrm { . }$

$$
w _ { m , j } = 0 ;
$$

Step3 Set $w _ { 0 , 0 } = f ( 0 )$ ；$w _ { m , 0 } = f ( l ) .$

Step 4 For $i = 1 , \ldots , m - 1$ (Initialize for $t = 0$ and $t = k$ ）set $w _ { i , 0 } = f ( i h )$ ；

$$
w _ { i , 1 } = ( 1 - \lambda ^ { 2 } ) f ( i h ) + \frac { \lambda ^ { 2 } } { 2 } [ f ( ( i + 1 ) h ) + f ( ( i - 1 ) h ) ] + k g ( i h ) .
$$

Step 5For $j = 1 , \ldots , N - 1$ (Perform matrix multiplication.) for $i = 1 , \ldots , m - 1$ set $w _ { i , j + 1 } = 2 ( 1 - \lambda ^ { 2 } ) w _ { i , j } + \lambda ^ { 2 } ( w _ { i + 1 , j } + w _ { i - 1 , j } ) + w _ { i , j - 1 } .$

Step 6For $j = 0 , \ldots , N$ set $t = j k$ ； for $i = 0 , \ldots , m$ set $x = i h$ ； OUTPUT $( x , t , w _ { i , j } )$

Step 7 STOP. (The procedure is complete.)

Consider the hyperbolic problem

$$
\frac { \partial ^ { 2 } u } { \partial t ^ { 2 } } ( x , t ) - 4 \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } ( x , t ) = 0 , \quad 0 < x < 1 , \quad 0 < t ,
$$

with boundary conditions

$$
u ( 0 , t ) = u ( 1 , t ) = 0 , \quad \mathrm { f o r } \quad 0 < t ,
$$

and initial conditions

$$
u ( x , 0 ) = \sin ( \pi x ) , \quad 0 \leq x \leq 1 , \quad \mathrm { a n d } \quad { \frac { \partial u } { \partial t } } ( x , 0 ) = 0 , \quad 0 \leq x \leq 1 .
$$

It is easily verified that the solution to this problem is

$$
u ( x , t ) = \sin \pi x \cos 2 \pi t .
$$

The Finite-Difference Algorithm 12.4 is used in this example with $m = 1 0 , T = 1$ ， and $N = 2 0$ , which implies that $h = 0 . 1 , k = 0 . 0 5$ ,and $\lambda = 1$ .Table 12.6 lists the results of the approximation $w _ { i , N }$ for $i = 0 , 1 , \ldots ,$ 10.The values listed in the table are correct to the places given. ■

Table 12.6   

<table><tr><td>Xi</td><td>Wi,20</td></tr><tr><td>0.0</td><td>0.0000000000</td></tr><tr><td>0.1</td><td>0.3090169944</td></tr><tr><td>0.2</td><td>0.5877852523</td></tr><tr><td>0.3</td><td>0.8090169944</td></tr><tr><td>0.4</td><td>0.9510565163</td></tr><tr><td>0.5</td><td>1.0000000000</td></tr><tr><td>0.6</td><td>0.9510565163</td></tr><tr><td>0.7</td><td>0.8090169944</td></tr><tr><td>0.8</td><td>0.5877852523</td></tr><tr><td>0.9</td><td>0.3090169944</td></tr><tr><td>1.0</td><td>0.0000000000</td></tr></table>

The results of the example were very accurate, more so than the truncation error $O ( k ^ { 2 } + h ^ { 2 } )$ would lead us to believe.This is because the true solution to the equation is infinitely differentiable.When this is the case,using Taylor series gives

$$
\begin{array} { c l c r } { \displaystyle { \frac { u ( x _ { i + 1 } , t _ { j } ) - 2 u ( x _ { i } , t _ { j } ) + u ( x _ { i - 1 } , t _ { j } ) } { h ^ { 2 } } } } \\ { \displaystyle { \qquad = \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } ( x _ { i } , t _ { j } ) + 2 \left[ \frac { h ^ { 2 } } { 4 ! } \frac { \partial ^ { 4 } u } { \partial x ^ { 4 } } ( x _ { i } , t _ { j } ) + \frac { h ^ { 4 } } { 6 ! } \frac { \partial ^ { 6 } u } { \partial x ^ { 6 } } ( x _ { i } , t _ { j } ) + \cdots \right] } } \end{array}
$$

and

$$
\begin{array} { r l r } {  { \frac { u ( x _ { i } , t _ { j + 1 } ) - 2 u ( x _ { i } , t _ { j } ) + u ( x _ { i } , t _ { j - 1 } ) } { k ^ { 2 } } } } \\ & { } & { = \frac { \partial ^ { 2 } u } { \partial t ^ { 2 } } ( x _ { i } , t _ { j } ) + 2 [ \frac { k ^ { 2 } } { 4 ! } \frac { \partial ^ { 4 } u } { \partial t ^ { 4 } } ( x _ { i } , t _ { j } ) + \frac { h ^ { 4 } } { 6 ! } \frac { \partial ^ { 6 } u } { \partial t ^ { 6 } } ( x _ { i } , t _ { j } ) + \cdot \cdot \cdot ] . } \end{array}
$$

Since $u ( x , t )$ satisfies the partial differential equation,

$$
\begin{array} { r l } & { \frac { u ( x _ { i } , t _ { j + 1 } ) - 2 u ( x _ { i } , t _ { j } ) + u ( x _ { i } , t _ { j - 1 } ) } { k ^ { 2 } } - \alpha ^ { 2 } \frac { u ( x _ { i + 1 } , t _ { j } ) - 2 u ( x _ { i } , t _ { j } ) + u ( x _ { i - 1 } , t _ { j } ) } { h ^ { 2 } } } \\ & { \qquad = 2 \bigg [ \frac { 1 } { 4 ! } \bigg ( k ^ { 2 } \frac { \partial ^ { 4 } u } { \partial t ^ { 4 } } ( x _ { i } , t _ { j } ) - \alpha ^ { 2 } h ^ { 2 } \frac { \partial ^ { 4 } u } { \partial x ^ { 4 } } ( x _ { i } , t _ { j } ) \bigg ) } \\ & { \qquad + \frac { 1 } { 6 ! } \bigg ( k ^ { 4 } \frac { \partial ^ { 6 } u } { \partial t ^ { 6 } } ( x _ { i } , t _ { j } ) - \alpha ^ { 2 } h ^ { 4 } \frac { \partial ^ { 6 } u } { \partial x ^ { 6 } } ( x _ { i } , t _ { j } ) \bigg ) + \cdot \cdot \bigg ] . } \end{array}
$$

However, differentiating the wave equation gives

$$
\begin{array} { c } { { k ^ { 2 } \displaystyle \frac { \partial ^ { 4 } u } { \partial t ^ { 4 } } ( x _ { i } , t _ { j } ) = k ^ { 2 } \displaystyle \frac { \partial ^ { 2 } } { \partial t ^ { 2 } } \left[ \alpha ^ { 2 } \displaystyle \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } ( x _ { i } , t _ { j } ) \right] = \alpha ^ { 2 } k ^ { 2 } \displaystyle \frac { \partial ^ { 2 } } { \partial x ^ { 2 } } \left[ \displaystyle \frac { \partial ^ { 2 } u } { \partial t ^ { 2 } } ( x _ { i } , t _ { j } ) \right] } } \\ { { = \alpha ^ { 2 } k ^ { 2 } \displaystyle \frac { \partial ^ { 2 } } { \partial x ^ { 2 } } \left[ \alpha ^ { 2 } \displaystyle \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } ( x _ { i } , t _ { j } ) \right] = \alpha ^ { 4 } k ^ { 2 } \displaystyle \frac { \partial ^ { 4 } u } { \partial x ^ { 4 } } ( x _ { i } , t _ { j } ) , } } \end{array}
$$

and we see that since $\lambda ^ { 2 } = ( \alpha ^ { 2 } k ^ { 2 } / h ^ { 2 } ) = 1$ , we have

$$
\frac { 1 } { 4 ! } \left[ k ^ { 2 } \frac { \partial ^ { 4 } u } { \partial t ^ { 4 } } ( x _ { i } , t _ { j } ) - \alpha ^ { 2 } h ^ { 2 } \frac { \partial ^ { 4 } u } { \partial x ^ { 4 } } ( x _ { i } , t _ { j } ) \right] = \frac { \alpha ^ { 2 } } { 4 ! } [ \alpha ^ { 2 } k ^ { 2 } - h ^ { 2 } ] \frac { \partial ^ { 4 } u } { \partial x ^ { 4 } } ( x _ { i } , t _ { j } ) = 0 .
$$

Continuing in this manner, allthe terms on the right-hand side of (12.25) areO,implying that the local truncation error is O. The only errors in Example 1 are those due to the approximation of $w _ { i , 1 }$ and to roundoff.

As in the case of the Forward-Difference method for the heat equation, the Explicit Finite-Difference method for the wave equation has stability problems.In fact, it is necessary that $\lambda = \alpha k / h \le 1$ for the method to be stable. (See [IK, p. 489].) The explicit method given in Algorithm 12.4,with $\lambda \leq 1$ ,is $O ( h ^ { 2 } + k ^ { 2 } )$ convergent if $f$ and $g$ are sufficiently differentiable.For verification of this,see [IK,p. 491].

Although we will not discuss them, there are implicit methods that are unconditionally stable. A discussion of these methods can be found in [Am,p.199], [Mi], or $[ \bf { S m } , \bf { B } ]$

# EXERCISE SET 12.3

1. Approximate the solution to the wave equation

$$
\begin{array} { r l } & { \displaystyle \frac { \partial ^ { 2 } u } { \partial t ^ { 2 } } - \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } = 0 , \quad 0 < x < 1 , \quad 0 < t ; } \\ & { \displaystyle u ( 0 , t ) = u ( 1 , t ) = 0 , \quad 0 < t , } \\ & { \displaystyle u ( x , 0 ) = \sin \pi x , \quad 0 \leq x \leq 1 , } \\ & { \displaystyle \frac { \partial u } { \partial t } ( x , 0 ) = 0 , \quad 0 \leq x \leq 1 , } \end{array}
$$

using the Finite-Difference Algorithm 12.4 with $m = 4 , N = 4$ and $T = 1 . 0$ . Compare your results at $t = 1 . 0$ to the actual solution $u ( x , t ) = \cos \pi t$ sin $\pi x$

2.Approximate the solution to the wave equation

$$
\begin{array} { r l } & { \frac { \partial ^ { 2 } u } { \partial t ^ { 2 } } - \cfrac { 1 } { 1 6 \pi ^ { 2 } } \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } = 0 , \quad 0 < x < 0 . 5 , \ 0 < t ; } \\ & { u ( 0 , t ) = u ( 0 . 5 , t ) = 0 , \quad 0 < t , } \\ & { u ( x , 0 ) = 0 , \quad 0 \leq x \leq 0 . 5 , } \\ & { \frac { \partial u } { \partial t } ( x , 0 ) = \sin { 4 \pi x } , \quad 0 \leq x \leq 0 . 5 , } \end{array}
$$

using the Finite-Diference Algorithm with $m = 4 , N = 4$ and $T = 0 . 5$ . Compare your results at $t = 0 . 5$ to the actual solution $u ( x , t ) = \sin { t } \sin { 4 \pi x }$

3. Approximate the solution to the wave equation

$$
\begin{array} { l } { \displaystyle { \frac { \partial ^ { 2 } u } { \partial t ^ { 2 } } - \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } = 0 \mathrm { , \quad } 0 < x < \pi \mathrm { , ~ } 0 < t ; } } \\ { \displaystyle { u ( 0 , t ) = u ( \pi , t ) = 0 \mathrm { , \quad } 0 < t \mathrm { , } } } \end{array}
$$

$$
\begin{array} { r l } & { u ( x , 0 ) = \sin x , \quad 0 \leq x \leq \pi , } \\ & { } \\ & { \displaystyle \frac { \partial u } { \partial t } ( x , 0 ) = 0 , \quad 0 \leq x \leq \pi , } \end{array}
$$

using the Finite-Difference Algorithm with $h = \pi / 1 0$ and $k = 0 . 0 5$ ，with $h = \pi / 2 0$ and $k = 0 . 1$ , and then with $h = \pi / 2 0$ and $k = 0 . 0 5$ . Compare your results at $t = 0 . 5$ to the actual solution $u ( x , t ) = \cos { t } s$ in $x$

4.Repeat Exercise 3, using in Step 4 of Algorithm 12.4 the approximation

$$
w _ { i , 1 } = w _ { i , 0 } + k g ( x _ { i } ) , \quad \mathrm { f o r e a c h } i = 1 , \dots , m - 1 .
$$

5. Approximate the solution to the wave equation

$$
\begin{array} { r l } & { \displaystyle \frac { \partial ^ { 2 } u } { \partial t ^ { 2 } } - \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } = 0 , \quad 0 < x < 1 , \ 0 < t ; } \\ & { \displaystyle u ( 0 , t ) = u ( 1 , t ) = 0 , \quad 0 < t , } \\ & { \displaystyle u ( x , 0 ) = \sin 2 \pi x , \quad 0 \leq x \leq 1 , } \\ & { \displaystyle \frac { \partial u } { \partial t } ( x , 0 ) = 2 \pi \sin 2 \pi x , \quad 0 \leq x \leq 1 , } \end{array}
$$

using Algorithm 12.4 with $h = 0 . 1$ and $k = 0 . 1$ . Compare your results at $t = 0 . 3$ to the actual solution $u ( x , t ) = \sin 2 \pi x ( \cos 2 \pi t + \sin 2 \pi t )$ .

6. Approximate the solution to the wave equation

$$
\begin{array} { r l } & { \frac { \partial ^ { 2 } u } { \partial t ^ { 2 } } - \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } = 0 , \quad 0 < x < 1 , \ 0 < t ; } \\ & { u ( 0 , t ) = u ( 1 , t ) = 0 , \quad 0 < t , } \\ & { u ( x , 0 ) = \left\{ \begin{array} { l l } { 1 , } & { 0 \leq x \leq \frac { 1 } { 2 } , } \\ { - 1 , } & { \frac { 1 } { 2 } < x \leq 1 , } \\ { \frac { \partial u } { \partial t } ( x , 0 ) = 0 , } & { 0 \leq x \leq 1 . } \end{array} \right. } \end{array}
$$

using Algorithm 12.4 with $h = 0 . 1$ and $k = 0 . 1$

7.The air pressure $p ( { \boldsymbol { x } } , t )$ in an organ pipe is govermed by the wave equation

$$
\frac { \partial ^ { 2 } p } { \partial x ^ { 2 } } = \frac { 1 } { c ^ { 2 } } \frac { \partial ^ { 2 } p } { \partial t ^ { 2 } } , \quad 0 < x < l , \ 0 < t ,
$$

where $l$ is the length of the pipe, and $\pmb { c }$ is a physical constant. If the pipe is open,the boundary conditions are given by

$$
p ( 0 , t ) = p _ { 0 } \quad \mathrm { a n d } \quad p ( l , t ) = p _ { 0 } .
$$

If the pipe is closed at the end where $x = l$ , the boundary conditions are

$$
p ( 0 , t ) = p _ { 0 } \quad \mathrm { a n d } \quad \frac { \partial p } { \partial x } ( l , t ) = 0 .
$$

Assume that $c = 1 , l = 1$ , and the initial conditions are

$$
p ( x , 0 ) = p _ { 0 } \cos 2 \pi x , \quad { \mathrm { a n d } } \quad { \frac { \partial p } { \partial t } } ( x , 0 ) = 0 , \quad 0 \leq x \leq 1 .
$$

a. Approximate the pressure for an open pipe with $p _ { 0 } = 0 . 9$ at $\begin{array} { r } { x = \frac { 1 } { 2 } } \end{array}$ for $t = 0 . 5$ and $t = 1$ ， using Algorithm 12.4 with $h = k = 0 . 1$   
b. Modify Algorithm 12.4 for the closed-pipe problem with $p _ { 0 } ~ = ~ 0 . 9$ ， and approximate $p ( 0 . 5 , 0 . 5 )$ and $p ( 0 . 5 , 1 )$ using $h = k = 0 . 1$

8. In an electric transmission line of length $l$ that carries alterating current of high frequency (called a "lossless” line),the voltage $V$ and current $i$ are described by

$$
\begin{array} { l l } { \displaystyle { \frac { \partial ^ { 2 } V } { \partial x ^ { 2 } } = L C \frac { \partial ^ { 2 } V } { \partial t ^ { 2 } } , \quad 0 < x < l , 0 < t ; } } \\ { \displaystyle { \frac { \partial ^ { 2 } i } { \partial x ^ { 2 } } = L C \frac { \partial ^ { 2 } i } { \partial t ^ { 2 } } , \quad 0 < x < l , 0 < t ; } } \end{array}
$$

where $L$ is the inductance per unit length, and $C$ is the capacitance per unit length. Suppose the line is 200 ft long and the constants $C$ and $L$ are given by

$$
C = 0 . 1 \mathrm { \ f a r a d s / f t { } ~ \ a n d ~ } L = 0 . 3 \mathrm { \ h e n r i e s / f t { } . }
$$

Suppose the voltage and current also satisfy

$$
\begin{array} { l l } { { V ( 0 , t ) = V ( 2 0 0 , t ) = 0 , } } & { { 0 < t ; } } \\ { { \ } } & { { \ } } \\ { { V ( x , 0 ) = 1 1 0 \sin \displaystyle \frac { \pi x } { 2 0 0 } , \quad 0 \leq x \leq 2 0 0 ; } } \\ { { \ } } & { { \ } } \\ { { \displaystyle \frac { \partial V } { \partial t } ( x , 0 ) = 0 , \quad 0 \leq x \leq 2 0 0 ; } } \\ { { \ } } & { { \ } } \\ { { \displaystyle i ( 0 , t ) = i ( 2 0 0 , t ) = 0 , \quad 0 < t ; } } \\ { { \ } } & { { \ } } \\ { { \displaystyle i ( x , 0 ) = 5 . 5 \cos \displaystyle \frac { \pi x } { 2 0 0 } , \quad 0 \leq x \leq 2 0 0 ; } } \end{array}
$$

and

$$
\frac { \partial i } { \partial t } ( x , 0 ) = 0 , \quad 0 \leq x \leq 2 0 0 .
$$

Approximate the voltage and current at $t = 0 . 2$ and $t = 0 . 5$ using Algorithm 12.4 with $h = 1 0$ and $k = 0 . 1$

# 12.4 An Introduction to the Finite-Element Method

The Finite-Element method is similar to the Rayleigh-Ritz method for approximating the solution to two-point boundary-value problems that was introduced in Section 11.5. It was originally developed for use in civil engineering,but it is now used for approximating the solutions to partial differential equations that arise in all areas of applied mathematics.

One advantage of the Finite-Element method over finite-difference methods is the relative ease with which the boundary conditions of the problem are handled. Many physical problems have boundary conditions involving derivatives and irregularly shaped boundaries.Boundary conditions of this type are diffcult to handle using finite-difference techniques since each boundary condition involving a derivative must be approximated by a difference quotient at the grid points,and irregular shaping of the boundary makes placing the grid points diffcult. The Finite-Element method includes the boundary conditions as integrals in a functional that is being minimized,so the construction procedure is independent of the particular boundary conditions of the problem.

In our discussion, we consider the partial differential equation

$$
{ \frac { \partial } { \partial x } } \bigg ( p ( x , y ) { \frac { \partial u } { \partial x } } \bigg ) + { \frac { \partial } { \partial y } } \bigg ( q ( x , y ) { \frac { \partial u } { \partial y } } \bigg ) + r ( x , y ) u ( x , y ) = f ( x , y ) ,
$$

with $( x , y ) \in { \mathcal { D } }$ ， where $\mathscr { D }$ is a plane region with boundary $8$

Boundary conditions of the form

$$
u ( x , y ) = g ( x , y )
$$

are imposed on a portion, $\pmb { \beta } _ { 1 }$ ,of the boundary. On the remainder of the boundary, $\pmb { \beta } _ { 2 }$ ,the solution $u ( x , y )$ is required to satisfy

$$
p ( x , y ) \frac { \partial u } { \partial x } ( x , y ) \cos \theta _ { 1 } + q ( x , y ) \frac { \partial u } { \partial y } ( x , y ) \cos \theta _ { 2 } + g _ { 1 } ( x , y ) u ( x , y ) = g _ { 2 } ( x , y ) ,
$$

where $\theta _ { 1 }$ and $\theta _ { 2 }$ are the direction angles of the outward normal to the boundary at the point $( x , y )$ . (See Figure 12.11.)

![](images/df75c6a6fdcf0b737e972706d92a5ae0a1386c8f65448873b800f13cc3c54f02.jpg)  
Figure 12.11

Physical problems in the areas of solid mechanics and elasticity have associated partial differential equations similar to Eq. (l2.26).The solution to a problem of this type typically minimizes a certain functional, involving integrals,over a class of functions determined by the problem.

Suppose $p , q , r$ ,and $f$ are all continuous on $\mathcal { D } \cup \mathcal { B } , p$ and $q$ have continuous first partial derivatives, and $g _ { 1 }$ and $g _ { 2 }$ are continuous on $\pmb { \beta } _ { 2 }$ . Suppose,in addition, that $p ( x , y ) >$ $0 , q ( x , y ) > 0 , r ( x , y ) \leq 0$ ,and $g _ { 1 } ( x , y ) > 0$ Then a solution to Eq. (12.26) uniquely minimizes the functional

$$
{ \begin{array} { r l } & { { \boldsymbol { \tau } } [ w ] = \displaystyle \iint _ { \mathcal { D } } \left\{ { \frac { 1 } { 2 } } { \biggl [ } { p ( x , y ) { \biggl ( } { \frac { \partial w } { \partial x } } { \biggr ) } ^ { 2 } } + q ( x , y ) { \biggl ( } { \frac { \partial w } { \partial y } } { \biggr ) } ^ { 2 } - r ( x , y ) w ^ { 2 } { \biggr ] } + f ( x , y ) w \right\} d x } \\ & { \qquad \quad + \displaystyle \int _ { \mathcal { S } _ { 2 } } \left\{ - g _ { 2 } ( x , y ) w + { \frac { 1 } { 2 } } g _ { 1 } ( x , y ) w ^ { 2 } \right\} d S } \end{array} }
$$

over all twice continuously-differentiable functions $w$ satisfying Eq.(12.27) on $\beta _ { 1 }$ . The Finite-Element method approximates this solution by minimizing the functional $I$ over a smaller class of functions, just as the Rayleigh-Ritz method did for the boundary-value problem considered in Section 11.5.

The first step is to divide the region into a finite number of sections, or elements, of a regular shape, either rectangles or triangles. (See Figure 12.12.)

![](images/051e04694e5407cb1d84953461bc3daccc66aa85eb82961923bf9b567cbbce15.jpg)  
Figure 12.12

The set of functions used for approximation is generally a set of piecewise polynomials of fixed degree in $\pmb { x }$ and $\textbf { y }$ , and the approximation requires that the polynomials be pieced together in such a manner that the resulting function is continuous with an integrable or continuous first or second derivative on the entire region. Polynomials of linear type in $x$ and $y$ ，

$$
\phi ( x , y ) = a + b x + c y ,
$$

are commonly used with triangular elements, whereas polynomials of bilinear type in $x$ and y，

$$
\phi ( x , y ) = a + b x + c y + d x y ,
$$

are used with rectangular elements.

For our discussion, suppose that the region $\pmb { \mathcal { D } }$ has been subdivided into triangular. elements. The collection of triangles is denoted $D$ , and the vertices of these triangles are called nodes. The method seeks an approximation of the form

$$
\phi ( x , y ) = \sum _ { i = 1 } ^ { m } \gamma _ { i } \phi _ { i } ( x , y ) ,
$$

where $\phi _ { 1 } , \phi _ { 2 } , \ldots , \phi _ { m }$ are linearly independent piecewise-linear polynomials, and $\gamma _ { 1 } , \gamma _ { 2 }$ $\cdots . . , \gamma _ { m }$ are constants. Some of these constants,for example, $\gamma _ { n + 1 } , \gamma _ { n + 2 } , \ldots , \gamma _ { m }$ ,are used to ensure that the boundary condition,

$$
\phi ( x , y ) = g ( x , y ) ,
$$

is satisfied on $\pmb { \beta _ { 1 } }$ ， and the remaining constants, $\gamma _ { 1 } , \gamma _ { 2 } , \ldots , \gamma _ { n }$ , are used to minimize the functional $I \left[ \textstyle \sum _ { i = 1 } ^ { m } \gamma _ { i } \phi _ { i } \right]$

From Eq. (12.29), the functional is of the form

$$
\begin{array} { l } { { \displaystyle { I [ \phi ] = I \biggl [ \sum _ { i = 1 } ^ { m } \gamma _ { i } \phi _ { i } \biggr ] } } } \\ { { \displaystyle { \quad = \int \int _ { \partial \Omega } \left( \frac 1 2 \biggl \{ p ( x , y ) \biggl [ \sum _ { i = 1 } ^ { m } \gamma _ { i } \frac { \partial \phi _ { i } } { \partial x } ( x , y ) \biggr ] ^ { 2 } + q ( x , y ) \biggl [ \sum _ { i = 1 } ^ { m } \gamma _ { i } \frac { \partial \phi _ { i } } { \partial y } ( x , y ) \biggr ] ^ { 2 } \right. } } } \\ { { \displaystyle { \quad \left. - r ( x , y ) \biggl [ \sum _ { i = 1 } ^ { m } \gamma _ { i } \phi _ { i } ( x , y ) \biggr ] ^ { 2 } \right\} + f ( x , y ) \sum _ { i = 1 } ^ { m } \gamma _ { i } \phi _ { i } ( x , y ) \biggr ) d y d x } } } \\ { { \displaystyle { \quad \quad + \int _ { \partial \Omega } \biggl \{ - g _ { \Omega } ( x , y ) \sum _ { i = 1 } ^ { m } \gamma _ { i } \phi _ { i } ( x , y ) + \frac 1 2 g _ { 1 } ( x , y ) \biggl [ \sum _ { i = 1 } ^ { m } \gamma _ { i } \phi _ { i } ( x , y ) \biggr ] ^ { 2 } \biggr \} d S . } } } \end{array}
$$

For a minimum to occur, considering $\pmb { I }$ as a function of $\gamma _ { 1 } , \gamma _ { 2 } , \ldots , \gamma _ { n }$ , it is necessary to have

$$
{ \frac { \partial I } { \partial \gamma _ { j } } } = 0 , \quad { \mathrm { f o r } } \operatorname { e a c h } j = 1 , 2 , \ldots , n .
$$

Differentiating (12.30) gives

$$
\begin{array} { l } { \displaystyle \frac { \partial I } { \partial \gamma _ { j } } = \int \int _ { \mathcal { D } } \Bigg \{ p ( x , y ) \sum _ { i = 1 } ^ { m } \gamma _ { i } \frac { \partial \phi _ { i } } { \partial x } ( x , y ) \frac { \partial \phi _ { j } } { \partial x } ( x , y ) } \\ { \displaystyle \qquad + q ( x , y ) \sum _ { i = 1 } ^ { m } \gamma _ { i } \frac { \partial \phi _ { i } } { \partial y } ( x , y ) \frac { \partial \phi _ { j } } { \partial y } ( x , y ) } \\ { \displaystyle \qquad - r ( x , y ) \sum _ { i = 1 } ^ { m } \gamma _ { i } \phi _ { i } ( x , y ) \phi _ { j } ( x , y ) + f ( x , y ) \phi _ { j } ( x , y ) \Bigg \} d x \ d y } \\ { \displaystyle \qquad + \int _ { 4 , 2 } \Bigg \{ - g _ { 2 } ( x , y ) \phi _ { j } ( x , y ) + g _ { 1 } ( x , y ) \sum _ { i = 1 } ^ { m } \gamma _ { i } \phi _ { i } ( x , y ) \phi _ { j } ( x , y ) \Bigg \} d S , } \end{array}
$$

so

$$
\begin{array} { l } { \displaystyle 0 = \sum _ { i = 1 } ^ { m } \left[ \iint _ { \mathcal { D } } \left\{ p ( x , y ) \frac { \partial \phi _ { i } } { \partial x } ( x , y ) \frac { \partial \phi _ { j } } { \partial x } ( x , y ) + q ( x , y ) \frac { \partial \phi _ { i } } { \partial y } ( x , y ) \frac { \partial \phi _ { j } } { \partial y } ( x , y ) \right. \right. } \\ { \displaystyle \left. \qquad - r ( x , y ) \phi _ { i } ( x , y ) \phi _ { j } ( x , y ) \right\} d x d y } \end{array}
$$

$$
\begin{array} { l } { { \displaystyle + \int _ { \mathscr { s } _ { 2 } } g _ { 1 } ( x , y ) \phi _ { i } ( x , y ) \phi _ { j } ( x , y ) d S \Bigg ] \gamma _ { i } } } \\ { { \displaystyle + \iint _ { \mathscr { D } } f ( x , y ) \phi _ { j } ( x , y ) d x d y - \int _ { \mathscr { s } _ { 2 } } g _ { 2 } ( x , y ) \phi _ { j } ( x , y ) d S , } } \end{array}
$$

for each $j = 1 , 2 , \dots , n$ . This set of equations can be written as a linear system:

$$
A \mathbf { c } = \mathbf { b } ,
$$

where $\mathbf { c } = ( \gamma _ { 1 } , \ldots , \gamma _ { n } ) ^ { t }$ , and where $A = ( \alpha _ { i j } )$ and $\mathbf { b } = ( \beta _ { 1 } , \dots , \beta _ { n } ) ^ { t }$ are defined by

$$
\begin{array} { c } { { \alpha _ { i j } = \displaystyle { \iint _ { \mathcal { D } } \left[ p ( x , y ) \frac { \partial \phi _ { i } } { \partial x } ( x , y ) \frac { \partial \phi _ { j } } { \partial x } ( x , y ) + q ( x , y ) \frac { \partial \phi _ { i } } { \partial y } ( x , y ) \frac { \partial \phi _ { j } } { \partial y } ( x , y ) \right. } } } \\ { { \displaystyle { \left. - r ( x , y ) \phi _ { i } ( x , y ) \phi _ { j } ( x , y ) \right] d x d y + \int _ { \mathcal { S } _ { 2 } } g _ { 1 } ( x , y ) \phi _ { i } ( x , y ) \phi _ { j } ( x , y ) d S . } } } \end{array}
$$

for each $i = 1 , 2 , \ldots , n$ and $j = 1 , 2 , \dots , m$ ,and

$$
\beta _ { i } = - \iint _ { \mathcal { D } } f ( x , y ) \phi _ { i } ( x , y ) d x d y + \int _ { \mathcal { S } _ { 2 } } g _ { 2 } ( x , y ) \phi _ { i } ( x , y ) d S - \sum _ { k = n + 1 } ^ { m } \alpha _ { i k } \gamma _ { k } ,
$$

for each $i = 1 , \ldots , n$

The particular choice of basis functions is important since the appropriate choice can often make the matrix $A$ positive definite and banded.For the second-order problem (12.26), we assume that $\mathcal { D }$ is polygonal, so that $\mathcal { D } = D$ , and that $\pmb { \mathscr { S } }$ is a contiguous set of straight lines.

To begin the procedure, we divide the region $D$ into a collection of triangles $T _ { 1 } , T _ { 2 }$ ， ：， $T _ { M }$ , with the ith triangle having three vertices, or nodes, denoted

$$
\begin{array} { r } { V _ { j } ^ { ( i ) } = \big ( x _ { j } ^ { ( i ) } , y _ { j } ^ { ( i ) } \big ) , \quad \mathrm { f o r } j = 1 , 2 , 3 . } \end{array}
$$

To simplify the notationwe write $V _ { j } ^ { ( i ) }$ simply as $V _ { j } = ( x _ { j } , y _ { j } )$ when working with the fixed triangle $T _ { i }$ . With each vertex $V _ { j }$ we associate a linear polynomial

$$
{ \bf \Phi } _ { j } ^ { ( i ) } ( x , y ) \equiv N _ { j } ( x , y ) = a _ { j } + b _ { j } x + c _ { j } y , \quad \mathrm { w h e r e } \quad N _ { j } ^ { ( i ) } ( x _ { k } , y _ { k } ) = \left\{ { \begin{array} { l l } { { 1 , } } & { { \mathrm { i f ~ } } j = k . } \\ { { 0 , } } & { { \mathrm { i f ~ } } j \neq k . } \end{array} } \right.
$$

This produces linear systems of the form

$$
\left[ \begin{array} { l l l } { 1 } & { x _ { 1 } } & { y _ { 1 } } \\ { 1 } & { x _ { 2 } } & { y _ { 2 } } \\ { 1 } & { x _ { 3 } } & { y _ { 3 } } \end{array} \right] \left[ \begin{array} { l } { a _ { j } } \\ { b _ { j } } \\ { c _ { j } } \end{array} \right] = \left[ \begin{array} { l } { 0 } \\ { 1 } \\ { 0 } \end{array} \right] ,
$$

with the element 1 occurring in the $j$ th row in the vector on the right (here $j = 2$

Let $E _ { 1 } , \ldots , E _ { n }$ be a labeling of the nodes lying in $D \cup \beta$ . With each node $E _ { k }$ ,we associate a function $\phi _ { k }$ that is linear on each triangle, has the value $\mathbf { l }$ at $E _ { k }$ , and is O at each of the other nodes. This choice makes $\phi _ { k }$ identical to $N _ { j } ^ { ( i ) }$ on triangle $T _ { i }$ when the node $E _ { k }$ is the vertex denoted V(i).

Suppose that a finite-element_problem contains the triangles $T _ { 1 }$ and $T _ { 2 }$ shown in Figure 12.13.The linear function $N _ { 1 } ^ { ( 1 ) } ( x , y )$ that assumes the value 1 at (1,1) and the value O at both (0, 0) and $( - 1 , 2 )$ satisfies

$$
\begin{array} { r } { a _ { 1 } ^ { ( 1 ) } + b _ { 1 } ^ { ( 1 ) } ( 1 ) + c _ { 1 } ^ { ( 1 ) } ( 1 ) = 1 , } \\ { a _ { 1 } ^ { ( 1 ) } + b _ { 1 } ^ { ( 1 ) } ( - 1 ) + c _ { 1 } ^ { ( 1 ) } ( 2 ) = 0 , } \end{array}
$$

and

$$
a _ { 1 } ^ { ( 1 ) } + b _ { 1 } ^ { ( 1 ) } ( 0 ) + c _ { 1 } ^ { ( 1 ) } ( 0 ) = 0 .
$$

![](images/6f56e9fd2cb92e61be694c3429ddaba9645b90c9b2b5273768dabc3bfa0713f3.jpg)  
Figure 12.13

$\begin{array} { r } { \mathrm { S o } a _ { 1 } ^ { ( 1 ) } = 0 , b _ { 1 } ^ { ( 1 ) } = \frac { 2 } { 3 } , c _ { 1 } ^ { ( 1 ) } = \frac { 1 } { 3 } } \end{array}$ , and

$$
N _ { 1 } ^ { ( 1 ) } ( x , y ) = \frac { 2 } { 3 } x + \frac { 1 } { 3 } y .
$$

In a similar manner,the linear function $N _ { 1 } ^ { ( 2 ) } ( x , y )$ that assumes the value 1 at (1,1) and the value O at both (O, O) and (1, O) satisfies

$$
\begin{array} { r } { a _ { 1 } ^ { ( 2 ) } + b _ { 1 } ^ { ( 2 ) } ( 1 ) + c _ { 1 } ^ { ( 2 ) } ( 1 ) = 1 , } \\ { a _ { 1 } ^ { ( 2 ) } + b _ { 1 } ^ { ( 2 ) } ( 0 ) + c _ { 1 } ^ { ( 2 ) } ( 0 ) = 0 , } \end{array}
$$

and

$$
a _ { 1 } ^ { ( 2 ) } + b _ { 1 } ^ { ( 2 ) } ( 1 ) + c _ { 1 } ^ { ( 2 ) } ( 0 ) = 0 ,
$$

soa(2=O,b0dc=1.seee,N(xy）yNotete common boundary of $T _ { 1 }$ and $T _ { 2 } , N _ { 1 } ^ { ( 1 ) } ( x , y ) = N _ { 1 } ^ { ( 2 ) } ( x , y )$ since ${ \boldsymbol { y } } = { \boldsymbol { x } }$

Consider Figure 12.14, the upper left portion of the region shown in Figure 12.12 on page 728. We willgenerate the entries in the matrix A that correspond to the nodes shown in this figure.

![](images/592aa02284421256981df1f4b55ec3c90bd90fdcef21e3bf433e94ecfeafe1a6.jpg)  
Figure 12.14

For simplicity, we assume that E1 is not one of the nodes on S2. The relationship between the nodes and the vertices of the triangles for this portion is

$$
E _ { 1 } = V _ { 3 } ^ { ( 1 ) } = V _ { 1 } ^ { ( 2 ) } , ~ E _ { 4 } = V _ { 2 } ^ { ( 2 ) } , ~ E _ { 3 } = V _ { 2 } ^ { ( 1 ) } = V _ { 3 } ^ { ( 2 ) } , ~ \mathrm { a n d } ~ E _ { 2 } = V _ { 1 } ^ { ( 1 ) } .
$$

Since Φ1 and Φ3 are both nonzero on T1 and T,the entries α1,3 = α3,1 are computed by

$$
\begin{array} { c } { \displaystyle { \alpha _ { 1 , 3 } = \iint _ { } \int _ { D } \left[ p \frac { \partial \phi _ { 1 } } { \partial x } \frac { \partial \phi _ { 3 } } { \partial x } + q \frac { \partial \phi _ { 1 } } { \partial y } \frac { \partial \phi _ { 3 } } { \partial y } - r \phi _ { 1 } \phi _ { 3 } \right] d x d y } } \\ { \displaystyle { = \iint _ { T _ { 1 } } \left[ p \frac { \partial \phi _ { 1 } } { \partial x } \frac { \partial \phi _ { 3 } } { \partial x } + q \frac { \partial \phi _ { 1 } } { \partial y } \frac { \partial \phi _ { 3 } } { \partial y } - r \phi _ { 1 } \phi _ { 3 } \right] d x d y } } \\ { \displaystyle { + \iint _ { T _ { 2 } } \left[ p \frac { \partial \phi _ { 1 } } { \partial x } \frac { \partial \phi _ { 3 } } { \partial x } + q \frac { \partial \phi _ { 1 } } { \partial y } \frac { \partial \phi _ { 3 } } { \partial y } - r \phi _ { 1 } \phi _ { 3 } \right] d x d y . } } \end{array}
$$

On triangle $T _ { 1 }$ ，

$$
\phi _ { 1 } ( x , y ) = N _ { 3 } ^ { ( 1 ) } ( x , y ) = a _ { 3 } ^ { ( 1 ) } + b _ { 3 } ^ { ( 1 ) } x + c _ { 3 } ^ { ( 1 ) } y .
$$

and

$$
\phi _ { 3 } ( x , y ) = N _ { 2 } ^ { ( 1 ) } ( x , y ) = a _ { 2 } ^ { ( 1 ) } + b _ { 2 } ^ { ( 1 ) } x + c _ { 2 } ^ { ( 1 ) } y ,
$$

so for all $( x , y )$ ，

$$
\frac { \partial \phi _ { 1 } } { \partial x } = b _ { 3 } ^ { ( 1 ) } , \ \frac { \partial \phi _ { 1 } } { \partial y } = c _ { 3 } ^ { ( 1 ) } , \ \frac { \partial \phi _ { 3 } } { \partial x } = b _ { 2 } ^ { ( 1 ) } ,
$$

$$
\frac { \partial \phi _ { 3 } } { \partial y } = c _ { 2 } ^ { ( 1 ) } .
$$

Similarly, on $T _ { 2 }$ ，

$$
\phi _ { 1 } ( x , y ) = N _ { 1 } ^ { ( 2 ) } ( x , y ) = a _ { 1 } ^ { ( 2 ) } + b _ { 1 } ^ { ( 2 ) } x + c _ { 1 } ^ { ( 2 ) } y
$$

and

$$
\phi _ { 3 } ( x , y ) = N _ { 3 } ^ { ( 2 ) } ( x , y ) = a _ { 3 } ^ { ( 2 ) } + b _ { 3 } ^ { ( 2 ) } x + c _ { 3 } ^ { ( 2 ) } y ,
$$

so for all $( x , y )$ ，

$$
\frac { \partial \phi _ { 1 } } { \partial x } = b _ { 1 } ^ { ( 2 ) } , ~ \frac { \partial \phi _ { 1 } } { \partial y } = c _ { 1 } ^ { ( 2 ) } , ~ \frac { \partial \phi _ { 3 } } { \partial x } = b _ { 3 } ^ { ( 2 ) } , ~ \mathrm { a n d } ~ \frac { \partial \phi _ { 3 } } { \partial y } = c _ { 3 } ^ { ( 2 ) } .
$$

Thus,

$$
\begin{array} { l } { { \displaystyle \alpha _ { 1 , 3 } = b _ { 3 } ^ { ( 1 ) } b _ { 2 } ^ { ( 1 ) } \displaystyle \iint _ { T _ { 1 } } p ~ d x ~ d y + c _ { 3 } ^ { ( 1 ) } c _ { 2 } ^ { ( 1 ) } \displaystyle \iint _ { T _ { 1 } } q ~ d x ~ d y } } \\ { { \displaystyle \qquad - \iint _ { T _ { 1 } } r \big ( a _ { 3 } ^ { ( 1 ) } + b _ { 3 } ^ { ( 1 ) } x + c _ { 3 } ^ { ( 1 ) } y \big ) \big ( a _ { 2 } ^ { ( 1 ) } + b _ { 2 } ^ { ( 1 ) } x + c _ { 2 } ^ { ( 1 ) } y \big ) ~ d x ~ d y } } \\ { { \displaystyle \qquad + b _ { 1 } ^ { ( 2 ) } b _ { 3 } ^ { ( 2 ) } \displaystyle \iint _ { T _ { 2 } } p ~ d x ~ d y + c _ { 1 } ^ { ( 2 ) } c _ { 3 } ^ { ( 2 ) } \displaystyle \iint _ { T _ { 2 } } q ~ d x ~ d y } } \\ { { \displaystyle \qquad - \iint _ { T _ { 2 } } r \big ( a _ { 1 } ^ { ( 2 ) } + b _ { 1 } ^ { ( 2 ) } x + c _ { 1 } ^ { ( 2 ) } y \big ) \big ( a _ { 3 } ^ { ( 2 ) } + b _ { 3 } ^ { ( 2 ) } x + c _ { 3 } ^ { ( 2 ) } y \big ) ~ d x ~ d y } . } \end{array}
$$

All the double integrals over $D$ reduce to double integrals over triangles. The usual procedure is to compute all possble integrals over the triangles and accumulate them into the correct entry $\alpha _ { i j }$ in $A$ . Similarly,the double integrals of the form

$$
\iint _ { D } f ( x , y ) \dot { \phi _ { i } } ( x , y ) d x d y
$$

are computed over triangles and then accumulated into the correct entry $\beta _ { i }$ of the vector b. For example, to determine $\beta _ { 1 }$ , we need

$$
\begin{array} { r l r } & { } & { - \displaystyle { \iint _ { D } f ( x , y ) \phi _ { 1 } ( x , y ) d x d y } = - \int \int _ { T _ { 1 } } f ( x , y ) \big [ a _ { 3 } ^ { ( 1 ) } + b _ { 3 } ^ { ( 1 ) } x + c _ { 3 } ^ { ( 1 ) } y \big ] d x d y } \\ & { } & { - \displaystyle { \iint _ { T _ { 2 } } f ( x , y ) \big [ a _ { 1 } ^ { ( 2 ) } + b _ { 1 } ^ { ( 2 ) } x + c _ { 1 } ^ { ( 2 ) } y \big ] d x d y } . } \end{array}
$$

Since $E _ { 1 }$ is a vertex of both $T _ { 1 }$ and $T _ { 2 }$ , part of $\beta _ { 1 }$ is contributed by $\phi _ { 1 }$ restricted to $T _ { 1 }$ and the remainder by $\phi _ { 1 }$ restricted to $T _ { 2 }$ . In addition,nodesthat lieon $\pmb { \mathscr { s } } _ { 2 }$ have line integrals added to their entries in $A$ and $\mathbf { b }$

Algorithm 12.5 performs the Finite-Element method on a second-order eliptic differential equation. The algorithm sets all values of the matrix $A$ and vector $\mathbf { b }$ initially to 0

and,after all the integrations have been performed on al the triangles, adds these values to the appropriate entries in $A$ and b.

# Finite-Element

To approximate the solution to the partial differential equation

$$
{ \frac { \partial } { \partial x } } { \Bigl ( } p ( x , y ) { \frac { \partial u } { \partial x } } { \Bigr ) } + { \frac { \partial } { \partial y } } { \Bigl ( } q ( x , y ) { \frac { \partial u } { \partial y } } { \Bigr ) } + r ( x , y ) u = f ( x , y ) , \quad ( x , y ) \in D
$$

subject to the boundary conditions

$$
u ( x , y ) = g ( x , y ) , \quad ( x , y ) \in \mathcal { S } _ { 1 }
$$

and

$$
p ( x , y ) { \frac { \partial u } { \partial x } } ( x , y ) \cos \theta _ { 1 } + q ( x , y ) { \frac { \partial u } { \partial y } } ( x , y ) \cos \theta _ { 2 } + g _ { 1 } ( x , y ) u ( x , y ) = g _ { 2 } ( x , y ) ,
$$

$$
( x , y ) \in \mathcal { S } _ { 2 } .
$$

where $\pmb { \mathscr { s } } _ { 1 } \cup \pmb { \mathscr { s } } _ { 2 }$ is the boundary of $D$ , and $\theta _ { \mathfrak { i } }$ and $\theta _ { 2 }$ are the direction angles of the normal to the boundary:

Step O Divide the region $D$ into triangles $T _ { 1 } , \dots , T _ { M }$ such that: $T _ { 1 } , \dots , T _ { K }$ are the triangles with no edges on $\pmb { \beta } _ { 1 }$ or $\pmb { \mathscr { s } } _ { 2 }$ ； (Note: $K = 0$ implies that no triangle is interior to $D$ ） $T _ { K + 1 } , \dots , T _ { N }$ are the triangles with at least one edge on $\pmb { \beta } _ { 2 }$ ； $T _ { N + 1 } , \dots , T _ { M }$ are the remaining triangles. $( N o t e \colon M = N$ implies that all triangles have edges on $\mathbf { \mathcal { S } } _ { 2 }$ .） Label the three vertices of the triangle $T _ { i }$ by $\left( x _ { 1 } ^ { ( i ) } , y _ { 1 } ^ { ( i ) } \right) , \left( x _ { 2 } ^ { ( i ) } , y _ { 2 } ^ { ( i ) } \right)$ ，and $\left( x _ { 3 } ^ { ( i ) } , y _ { 3 } ^ { ( i ) } \right)$ Label the nodes (vertices) $E _ { 1 } , \ldots , E _ { m }$ where $E _ { 1 } , \ldots , E _ { n }$ are in $D \cup \pmb { \mathcal { B } } _ { 2 }$ and $E _ { n + 1 } , \ldots , E _ { m }$ are on $\beta _ { 1 }$ $( N o t e . n = m$ implies that $\pmb { \beta } _ { 1 }$ contains no nodes.)

INPUTintegers $K , N , M , n , m$ vertices $\left( x _ { 1 } ^ { ( i ) } , y _ { 1 } ^ { ( i ) } \right) , \left( x _ { 2 } ^ { ( i ) } , y _ { 2 } ^ { ( i ) } \right) , \left( x _ { 3 } ^ { ( i ) } , y _ { 3 } ^ { ( i ) } \right)$ for each $i = 1 , \dots , M$ ; nodes $E _ { j }$ for each $j = 1 , \ldots , m$ ·   
(NoteAlte $\left( x _ { k } ^ { \left( i \right) } , y _ { k } ^ { \left( i \right) } \right)$ to a node $E _ { j } =$ $( x _ { j } , y _ { j } ) . )$

OUTPUT constants $\gamma _ { 1 } , \dots , \gamma _ { m } ; a _ { j } ^ { ( i ) } , b _ { j } ^ { ( i ) } , c _ { j } ^ { ( i ) }$ for each $j = 1 , 2 , 3$ and $i = 1 , \dots , M$

Step 2 For $i = 1 , \ldots , n$ set $\beta _ { i } = 0$ ； for $j = 1 , \ldots , n \mathrm { s e t } \alpha _ { i , j } = 0 .$

Step 3 Fori =1,..,M

$$
\begin{array} { r } { \mathrm { s e t } ~ \Delta _ { i } = \mathrm { d e t } \left| \begin{array} { l l l } { 1 } & { x _ { 1 } ^ { ( i ) } } & { y _ { 1 } ^ { ( i ) } } \\ { 1 } & { x _ { 2 } ^ { ( i ) } } & { y _ { 2 } ^ { ( i ) } } \\ { 1 } & { x _ { 3 } ^ { ( i ) } } & { y _ { 3 } ^ { ( i ) } } \end{array} \right| ; } \end{array}
$$

$$
\begin{array} { c c c } { { a _ { 1 } ^ { ( i ) } = \displaystyle { \frac { x _ { 2 } ^ { ( i ) } y _ { 3 } ^ { ( i ) } - y _ { 2 } ^ { ( i ) } x _ { 3 } ^ { ( i ) } } { \Delta _ { i } } } ; } } & { { b _ { 1 } ^ { ( i ) } \nonumber { = \frac { y _ { 2 } ^ { ( i ) } - y _ { 3 } ^ { ( i ) } } { \Delta _ { i } } ; } } } & { { c _ { 1 } ^ { ( i ) } = \displaystyle { \frac { x _ { 3 } ^ { ( i ) } - x _ { 2 } ^ { ( i ) } } { \Delta _ { i } } } ; } } \\ { { \nonumber } } & { { } } & { { } } \\ { { a _ { 2 } ^ { ( i ) } = \displaystyle { \frac { x _ { 3 } ^ { ( i ) } y _ { 1 } ^ { ( i ) } - y _ { 3 } ^ { ( i ) } x _ { 1 } ^ { ( i ) } } { \Delta _ { i } } } ; } } & { { b _ { 2 } ^ { ( i ) } = \displaystyle { \frac { y _ { 3 } ^ { ( i ) } - y _ { 1 } ^ { ( i ) } } { \Delta _ { i } } } ; } } & { { c _ { 2 } ^ { ( i ) } = \displaystyle { \frac { x _ { 1 } ^ { ( i ) } - x _ { 3 } ^ { ( i ) } } { \Delta _ { i } } } ; } } \\ { { a _ { 3 } ^ { ( i ) } = \displaystyle { \frac { x _ { 1 } ^ { ( i ) } y _ { 2 } ^ { ( i ) } - y _ { 1 } ^ { ( i ) } x _ { 2 } ^ { ( i ) } } { \Delta _ { i } } } ; } } & { { b _ { 3 } ^ { ( i ) } = \displaystyle { \frac { y _ { 1 } ^ { ( i ) } - y _ { 2 } ^ { ( i ) } } { \Delta _ { i } } } ; } } & { { c _ { 3 } ^ { ( i ) } = \displaystyle { \frac { x _ { 2 } ^ { ( i ) } - x _ { 1 } ^ { ( i ) } } { \Delta _ { i } } } ; } } \end{array}
$$

for $j = 1 , 2 , 3$ define $N _ { j } ^ { ( i ) } ( x , y ) = a _ { j } ^ { ( i ) } + b _ { j } ^ { ( i ) } x + c _ { j } ^ { ( i ) } y .$

Step 4 For $i = 1 , \dots , M$ (The integrals in Steps 4 and 5 can be evaluated using numerical integration.) for $j = 1 , 2 , 3$ for $k = 1 , \hdots , j$ (Compute all double integrals over the triangles.)

$$
\begin{array} { r } { z _ { j , k } ^ { ( i ) } = b _ { j } ^ { ( i ) } b _ { k } ^ { ( i ) } \int \int p ( x , y ) d x d y + c _ { j } ^ { ( i ) } c _ { k } ^ { ( i ) } \int \int q ( x , y ) d x d y } \\ { T _ { i } } \end{array}
$$

$$
\begin{array} { r } { - \int \int r ( x , y ) N _ { j } ^ { ( i ) } ( x , y ) N _ { k } ^ { ( i ) } ( x , y ) d x d y ; } \end{array}
$$

Step 5For $i = K + 1 , \dots , N$ (Compute all line integrals.) for $j = 1 , 2 , 3$ for $k = 1 , \hdots , j$ $\textbf { t } J _ { j , k } ^ { ( i ) } = \int _ { \mathcal { S } _ { 2 } } g _ { 1 } ( x , y ^ { \circ } ) N _ { j } ^ { ( i ) } ( x , y ) N _ { k } ^ { ( i ) } ( x , y ) d S ;$ $\mathsf { s e t } \ I _ { j } ^ { ( i ) } = \int _ { \mathcal { S } _ { 2 } } g _ { 2 } ( x , y ) N _ { j } ^ { ( i ) } ( x , y ) d S .$

Step $\sigma$ For $i = 1$ ，·， $M$ do Steps 7-12. (Assembling the integrals over each triangle into the linear system.)

Step 7For $k = 1$ ,2, 3 do Steps 8-12.

Step 8 Find $l$ so that $E _ { l } = \left( x _ { k } ^ { \left( i \right) } , y _ { k } ^ { \left( i \right) } \right)$

Step 9 If $k > 1$ then for $j = 1 , \ldots , k - 1$ do Steps 10, 11.

Step 11 If $l \leq n$ then

$$
\begin{array} { r l r } & { - } & { \mathrm { i f } \ t \leq n \ \mathrm { t h e n ~ s e t } \alpha _ { l t } = \alpha _ { l t } + z _ { k , j } ^ { ( i ) } ; } \\ & { } & { \alpha _ { t l } = \alpha _ { t l } + z _ { k , j } ^ { ( i ) } } \\ & { } & { \mathrm { e l s e ~ s e t } \beta _ { l } = \beta _ { l } - \gamma _ { t } z _ { k , j } ^ { ( i ) } } \end{array}
$$

Step 12 If $l \leq n$ then set

$$
\begin{array} { r } { a _ { l l } = \alpha _ { l l } + z _ { k , k } ^ { ( i ) } ; } \\ { \beta _ { l } = \beta _ { l } + H _ { k } ^ { ( i ) } . } \end{array}
$$

Step 13 For $i = K + 1 , \dots , N$ do Steps 14-19. (Assembling the line integrals into the linear system.)

Step 14 For $k = 1 , 2 , 3$ do Steps 15-19.

Step 15Find $l$ so that $E _ { l } = \left( x _ { k } ^ { \left( i \right) } , y _ { k } ^ { \left( i \right) } \right)$

Step 16 If $k > 1$ then for $j = 1 , \ldots , k - 1$ do Steps 17, 18.

Step 17Find $t$ so that $E _ { t } = \left( x _ { j } ^ { ( i ) } , y _ { j } ^ { ( i ) } \right)$ ·

Step 18 If $l \leq n$ then

$$
\begin{array} { r } { \alpha _ { l t } = \alpha _ { l t } + J _ { k , j } ^ { ( i ) } , } \\ { \alpha _ { t l } = \alpha _ { t l } + J _ { k , j } ^ { ( i ) } } \\ { \beta _ { l } = \beta _ { l } - \gamma _ { t } J _ { k , j } ^ { ( i ) } } \end{array}
$$

Step 19 If $l \leq n$ then set

$$
\begin{array} { l } { \alpha _ { l l } = \alpha _ { l l } + J _ { k , k } ^ { ( i ) } ; } \\ { \beta _ { l } = \beta _ { l } + I _ { k } ^ { ( i ) } . } \end{array}
$$

Step 20 Solve the linear system Ac = b where A= (αl,t),b= (βt) and c = (vt) for $1 \leq l \leq n$ and $1 \leq t \leq n$

Step 21 OUTPUT $( \gamma _ { 1 } , \ldots , \gamma _ { m } )$ (For each $k = 1 , \ldots , m$ let $\phi _ { k } = N _ { j } ^ { ( i ) } o n T _ { i }$ if $E _ { k } = \left( x _ { j } ^ { ( i ) } , y _ { j } ^ { ( i ) } \right)$ Then $\begin{array} { r } { \phi ( x , y ) = \sum _ { k = 1 } ^ { m } \gamma _ { k } \phi _ { k } ( x , y ) } \end{array}$ approximates $u ( x , y )$ om $D \cup \ S _ { 1 } \cup \ S _ { 2 } . \qquad $

Step 22 For $i = 1 , \ldots , M$ for $j = 1 , 2 , 3$ OUTPUT $\left( a _ { j } ^ { ( i ) } , b _ { j } ^ { ( i ) } , c _ { j } ^ { ( i ) } \right)$

Step 23 STOP. (The procedure is complete.)

The temperature, $u ( x , y )$ , in a two-dimensional region $D$ satisfies Laplace's equation

$$
{ \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } } ( x , y ) + { \frac { \partial ^ { 2 } u } { \partial y ^ { 2 } } } ( x , y ) = 0 \quad { \mathrm { o n ~ } } D .
$$

![](images/c6e6f2b509fd5fa3690b40ec30c92fddad3e021257e48deb59152eefe79a6259.jpg)  
Figure 12.15

Consider the region $D$ shown in Figure 12.15 with boundary conditions given by

$$
\begin{array} { r l r l } & { u ( x , y ) = 4 , } & & { \mathrm { f o r ~ } ( x , y ) \in L _ { 6 } \mathrm { ~ a n d ~ } ( x , y ) \in L _ { 7 } ; } \\ & { \displaystyle \frac { \partial u } { \partial n } ( x , y ) = x , } & & { \mathrm { f o r ~ } ( x , y ) \in L _ { 2 } \mathrm { ~ a n d ~ } ( x , y ) \in L _ { 4 } ; } \\ & { \displaystyle \frac { \partial u } { \partial n } ( x , y ) = y , } & & { \mathrm { f o r ~ } ( x , y ) \in L _ { 5 } ; } \\ & { \displaystyle \frac { \partial u } { \partial n } ( x , y ) = \frac { x + y } { \sqrt { 2 } } , } & & { \mathrm { f o r ~ } ( x , y ) \in L _ { 1 } \mathrm { ~ a n d ~ } ( x , y ) \in L _ { 3 } ; } \end{array}
$$

where $\partial u / \partial n$ denotes the directional derivative in the direction of the normal to the bound-ary of the region $D$ at the point $( x , y )$ ·

We first subdivide $D$ into triangles with the labeling suggested in Step O of the algorithm. For this example, $\pmb { \mathscr { s } } _ { 1 } = L _ { 6 } \cup L _ { 7 }$ and $\hat { \{ }  _ { 2 } = L _ { 1 } \cup L _ { 2 } \cup L _ { 3 } \cup L _ { 4 } \cup L _ { 5 }$ . The labeling of triangles is shown in Figure 12.16.

The boundary condition $u ( x , y ) = 4$ on $L _ { 6 }$ and $L _ { 7 }$ implies that $\gamma _ { \mathrm { { / } } } = 4$ when $t \ =$ 6,7,...,11. To determine the values of $\gamma _ { l }$ for $l = 1 , 2 , \ldots , 5$ ,apply the remaining steps of the algorithm and generate the matrix

$$
A = \left[ { \begin{array} { c c c c c c } { 2 . 5 } & { 0 } & { - 1 } & { 0 } & { 0 } \\ { 0 } & { 1 . 5 } & { - 1 } & { - 0 . 5 } & { 0 } \\ { - 1 } & { - 1 } & { 4 } & { 0 } & { 0 } \\ { 0 } & { - 0 . 5 } & { 0 } & { 2 . 5 } & { - 0 . 5 } \\ { 0 } & { 0 } & { 0 } & { - 0 . 5 } & { 1 } \end{array} } \right]
$$

![](images/1cccd19867fad2bddc8b0c8f3c9de48d47dc5ab453ec6721de679cca6fb9ffc0.jpg)  
Figure 12.16

and the vector

$$
\mathbf { b } = { \left[ \begin{array} { l } { 6 . 0 6 6 { \bar { 6 } } } \\ { 0 . 0 6 3 { \bar { 3 } } } \\ { 8 . 0 0 0 0 } \\ { 6 . 0 5 6 { \bar { 6 } } } \\ { 2 . 0 3 1 { \bar { 6 } } } \end{array} \right] } .
$$

The solution to the equation $\pmb { A } \mathbf { c } = \mathbf { b }$ is

$$
\mathbf { c } = { \left[ \begin{array} { l } { \gamma _ { 1 } } \\ { \gamma _ { 2 } } \\ { \gamma _ { 3 } } \\ { \gamma _ { 4 } } \\ { \gamma _ { 5 } } \end{array} \right] } = { \left[ \begin{array} { l } { 4 . 0 3 8 3 } \\ { 4 . 0 7 8 2 } \\ { 4 . 0 2 9 1 } \\ { 4 . 0 4 9 6 } \\ { 4 . 0 5 6 5 } \end{array} \right] } ,
$$

which gives the folowing approximation to the solution of Laplace's equation and the boundary conditions on the respective triangles:

$$
\begin{array} { r l } { T _ { 1 } : } & { \phi ( x , y ) = 4 . 0 3 8 3 ( 1 - 5 x + 5 y ) + 4 . 0 2 9 1 ( - 2 + 1 0 x ) + 4 ( 2 - 5 x - 5 y ) , } \\ { T _ { 2 } : } & { \phi ( x , y ) = 4 . 0 7 8 2 ( - 2 + 5 x + 5 y ) + 4 . 0 2 9 1 ( 4 - 1 0 x ) + 4 ( - 1 + 5 x - 5 y ) , } \\ { T _ { 3 } : } & { \phi ( x , y ) = 4 ( - 1 + 5 y ) + 4 ( 2 - 5 x - 5 y ) + 4 . 0 3 8 3 ( 5 x ) , } \\ { T _ { 4 } : } & { \phi ( x , y ) = 4 . 0 3 8 3 ( 1 - 5 x + 5 y ) + 4 . 0 7 8 2 ( - 2 + 5 x + 5 y ) + 4 . 0 2 9 1 ( 2 - 1 + 2 . 0 2 5 ) , } \\ { T _ { 5 } : } & { \phi ( x , y ) = 4 . 0 7 8 2 ( 2 - 5 x + 5 y ) + 4 . 0 4 9 6 ( - 4 + 1 0 x ) + 4 ( 3 - 5 x - 5 y ) , } \\ { T _ { 6 } : } & { \phi ( x , y ) = 4 . 0 4 9 6 ( 6 - 1 0 x ) + 4 . 0 5 6 5 ( - 6 + 1 0 x + 1 0 y ) + 4 ( 1 - 1 0 y ) , } \end{array}
$$

$$
\begin{array} { r l } { T _ { 7 } : } & { \phi ( x , y ) = 4 ( - 5 x + 5 y ) + 4 . 0 3 8 3 ( 5 x ) + 4 ( 1 - 5 y ) , } \\ { T _ { 8 } : } & { \phi ( x , y ) = 4 . 0 3 8 3 ( 5 y ) + 4 ( 1 - 5 x ) + 4 ( 5 x - 5 y ) , } \\ { T _ { 9 } : } & { \phi ( x , y ) = 4 . 0 2 9 1 ( 1 0 y ) + 4 ( 2 - 5 x - 5 y ) + 4 ( - 1 + 5 x - 5 y ) , } \\ { T _ { 1 0 } : } & { \phi ( x , y ) = 4 . 0 4 9 6 ( 1 0 y ) + 4 ( 3 - 5 x - 5 y ) + 4 ( - 2 + 5 x - 5 y ) . } \end{array}
$$

The actual solution to the boundary-value problem is $u ( x , y ) = x y + 4$ .Table 12.7 compares the value of $\pmb { u }$ to the value of $\phi$ at $E _ { i }$ ,for each $i = 1 , \ldots , 5$

# Table 12.7

<table><tr><td>X y</td><td>Φ(x,y)</td><td>u(x,y）</td><td>l(x,y）-u(x,y)l</td></tr><tr><td>0.2</td><td>0.2 4.0383</td><td>4.04</td><td>0.0017</td></tr><tr><td>0.4 0.2</td><td>4.0782</td><td>4.08</td><td>0.0018</td></tr><tr><td>0.3 0.1</td><td>4.0291</td><td>4.03</td><td>0.0009</td></tr><tr><td>0.5 0.1</td><td>4.0496</td><td>4.05</td><td>0.0004</td></tr><tr><td>0.6</td><td>0.1 4.0565</td><td>4.06</td><td>0.0035</td></tr></table>

Typically, the error for elliptic second-order problems of the type (12.26) with smooth coefficient functions is $O ( h ^ { 2 } )$ ，where $h$ is the maximum diameter of the triangular elements. Piecewise bilinear basis functions on rectangular elements are also expected to give $O ( h ^ { 2 } )$ results, where $h$ is the maximum diagonal length of the rectangular elements. Other classes of basis functions can be used to give $O ( h ^ { 4 } )$ results, but the construction is more complex. Efficient error theorems for finite-element methods are dificult to state and apply because the accuracy of the approximation depends on the continuity properties of the solution and the regularity of the boundary.

The Finite-Element method can also be applied to parabolic and hyperbolic partial differential equations, but the minimization procedure is more difficult. A good survey on the advantages and techniques of the Finite-Element method applied to various physical problems can be found in a paper by [Fi]. For a more extensive discussion, refer to [SF], [ZM], or [AB].

# ExERcise Set 12.4

1. Use Algorithm 12.5 to approximate the solution to the following partial differential equation (see the figure):

$$
\frac { \partial } { \partial x } \left( y ^ { 2 } \frac { \partial u } { \partial x } ( x , y ) \right) + \frac { \partial } { \partial y } \left( y ^ { 2 } \frac { \partial u } { \partial y } ( x , y ) \right) - y u ( x , y ) = - x , \quad ( x , y ) \in D ,
$$

$$
u ( x , 0 . 5 ) = 2 x , \quad 0 \leq x \leq 0 . 5 , \quad u ( 0 , y ) = 0 , \quad 0 . 5 \leq y \leq 1 ,
$$

$$
y ^ { 2 } \frac { \partial u } { \partial x } ( x , y ) \cos { \theta _ { 1 } } + y ^ { 2 } \frac { \partial u } { \partial y } ( x , y ) \cos { \theta _ { 2 } } = \frac { \sqrt { 2 } } { 2 } ( y - x ) \quad \mathrm { f o r ~ } ( x , y ) \in \mathcal { A } _ { 2 } .
$$

![](images/f6187f8481e57379a3cf5e4f1b86f90b4dae610e38401dec81b8cbae30368088.jpg)

Let $M \ = \ 2 ; \ T _ { 1 }$ have vertices (0,0.5), (0.25,0.75), (0,1); and $T _ { 2 }$ have vertices (0,0.5), (0.5, 0.5), and (0.25, 0.75).

2. Repeat Exercise 1, using instead the triangles

$$
\begin{array} { r l } { { T _ { 1 } : } } & { { ( 0 , 0 . 7 5 ) , ( 0 , 1 ) , ( 0 . 2 5 , 0 . 7 5 ) ; } } \\ { { } } & { { } } \\ { { T _ { 2 } : } } & { { ( 0 . 2 5 , 0 . 5 ) , ( 0 . 2 5 , 0 . 7 5 ) , ( 0 . 5 , 0 . 5 ) ; } } \\ { { } } & { { } } \\ { { T _ { 3 } : } } & { { ( 0 , 0 . 5 ) , ( 0 , 0 . 7 5 ) , ( 0 . 2 5 , 0 . 7 5 ) ; } } \\ { { } } & { { } } \\ { { T _ { 4 } : } } & { { ( 0 , 0 . 5 ) , ( 0 . 2 5 , 0 . 5 ) , ( 0 . 2 5 , 0 . 7 5 ) . } } \end{array}
$$

3.Approximate the solution to the partial differential equation

$$
\frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } ( x , y ) + \frac { \partial ^ { 2 } u } { \partial y ^ { 2 } } ( x , y ) - 1 2 . 5 \pi ^ { 2 } u ( x , y ) = - 2 5 \pi ^ { 2 } \sin \frac { 5 \pi } { 2 } x \sin \frac { 5 \pi } { 2 } y , \quad 0 < x , \ y < 0 . 4 ,
$$

subject to the Dirichlet boundary condition

$$
{ \pmb u } ( { \pmb x } , { \pmb y } ) = { \pmb 0 } ,
$$

using the Finite-Element Algorithm 12.5 with the elements given in the accompanying figure. Compare the approximate solution to the actual solution,

$$
u ( x , y ) = \sin \frac { 5 \pi } { 2 } x \sin \frac { 5 \pi } { 2 } y ,
$$

at the interior vertices and at the points (0.125,0.125)，(0.125,0.25)， (0.25,0.125)，and(0.25, 0.25).

![](images/659da5881afa6bcc1b6fd64bd0807cd77b57dd0f8a5623fbe5e96ab9b3d4cf3f.jpg)

4.Repeat Exercise 3 with $\begin{array} { r } { f ( x , y ) = - 2 5 \pi ^ { 2 } \cos \frac { 5 \pi } { 2 } x \cos \frac { 5 \pi } { 2 } y } \end{array}$ , using the Neumann boundary condition

$$
{ \frac { \partial u } { \partial n } } ( x , y ) = 0 .
$$

The actual solution for this problem is

$$
u ( x , y ) = \cos \frac { 5 \pi } { 2 } x \cos \frac { 5 \pi } { 2 } y .
$$

5.A silver plate in the shape of a trapezoid (see the accompanying figure) has heat being uniformly generated at each point at the rate $q = 1 . 5 \mathrm { c a l } \mathrm { c m } ^ { 3 } \cdot \mathrm { s } .$ The steady-state temperature $u ( x , y )$ of the plate satisfies the Poisson equation

$$
\frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } ( x , y ) + \frac { \partial ^ { 2 } u } { \partial y ^ { 2 } } ( x , y ) = \frac { - q } { k } ,
$$

![](images/b8fe82d9b4e1e91e0749eebd3b9ff99a88903466d345dc6f08b9d9616ba95b85.jpg)

where $k$ ,the thermal conductivity, is 1.04 cal/cm-deg·s. Assume that the temperature is held at $1 5 \%$ on $L _ { 2 }$ , that heat is lost on the slanted edges $L _ { 1 }$ and $L _ { 3 }$ according to the boundary condition ${ \partial u } / { \partial n } = 4$ ,and that no heat is lost on $L _ { 4 }$ ; that is, $\partial u / \partial n = 0$ Approximate the temperature of the plate at (1,0), (4,O), and $\left( { \frac { 5 } { 2 } } , { \sqrt { 3 } } / 2 \right)$ by using Algorithm 12.5.

# 12.5 Survey of Methods and Software

In this chapter, methods to approximate solutions to partial differential equations were con-sidered. We restricted our atention to Poisson's equation as an example of an elliptic partial differential equation, the heat or diffusion equation as an example of a parabolic partial differential equation, and the wave equation as an example of a hyperbolic partial diferential equation. Finite-difference approximations were discussed for these three examples.

Poisson's equation on a rectangle required the solution of a large sparse linear system,for which iterative techniques,such as the SOR method, are recommended. Four finite-difference methods were presented for the heat equation. The Forward-Difference and Richardson's methods had stability problems,so the Backward-Difference method and the Crank-Nicolson methods were introduced. Although a tridiagonal linear system must be solved at each time step with these implicit methods, they are more stable than the explicit Forward-Difference and Richardson's methods. The Finite-Difference method for the wave equation is explicit and can also have stability problems for certain choice of time and space discretizations.

In the last section of the chapter, we presented an introduction to the Finite-Element method for a self-adjoint elliptic partial differential equation on a polygonal domain. Although our methods will work adequately for the problems and examples in the textbook, more powerful generalizations and modifications of these techniques are required for commercial applications.

We consider two subroutines from the IMSL Library. The subroutine MOLCH is used to solve the partial differential equation

$$
{ \frac { \partial u } { \partial t } } = F \left( x , t , { \dot { u } } , { \frac { \partial u } { \partial x } } , { \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } } \right) ,
$$

with boundary conditions

$$
\alpha ( x , t ) u ( x , t ) + \beta ( x , t ) \frac { \partial u } { \partial x } ( x , t ) = \gamma ( x , t ) .
$$

The method is based on collocation at Gaussian points on the $x$ -axis for each value of $t$ and uses cubic Hermite splines as basis functions.

The subroutine FPS2H is used to solve Poisson's equation on a rectangle. The method of solution is based on a choice of second- or fourth-order finite differences on a uniform mesh.

The NAG Library has a number of subroutines for partial differential equations. The subroutine DO3EAF is used for Laplace's equation on an arbitrary domain in the $x y$ -plane. The subroutine DO3PCF is used to solve a single parabolic partial differential equation by the method of lines.

There are specialized packages,such as NASTRAN, consisting of codes for the Finite-Element method. These packages are popular in engineering applications. The package FISHPACK in the Netlib library is used to solve separable elliptic partial differential equations.General codes for partial differential equations are difficult to write because of the problem of specifying domains other than common geometrical figures. Research in the area of solution of partial differential equations is currently very active.

We have only presented a small sample of the many techniques used for approximating the solutions to the problems involving partial differential equations.Further information on the general topic can be found in Lapidus and Pinder [LP],Twizell [Tw],and the recent book by Morton and Mayers [MM]. Software information can be found in Rice and Boisvert [RB] and in Bank [Ban].

Books that focus on finite-difference methods include Strikwerda [Strik], Thomas [Th],and Shashkov and Steinberg [ShS]. Strange and Fix [SF] and Zienkiewicz and Morgan [ZM] are good sources for information on the finite-element method. Time-dependent equations are treated in Schiesser [Schi] and in Gustafsson, Kreiss,and Oliger [GKO], and Birkhoff and Lynch [BL] and Roache [Ro] discuss the solution to elliptic problems.

Multigrid methods use coarse grid approximations and iterative techniques to provide approximations on finer grids. References on these techniques include Briggs [Brigg], Mc Cormick [Mc], and Bramble [Bram].

# Bibliography

Text pages referring to the items are given in italics at the end ofeach reference.

[AHU] Aho, A. V., J. E. Hopcroft, and J.D. Ulman, The design and analysis of computer algorithms, Addison-Wesley, Reading,MA,1974, 470 pp. QA76.6.A36546 [AG] Allgower,E.andK. Georg,Numerical continuation methods: anintroduction,Springer-Verlag,New York,1990,388 pp. QA377.A56644 [Am] Ames,W.F.,Numerical methods for partial differential equations,(Third edition), Academic Press, New York,1992,451 pp. QA374.A46724 [An] Anderson,E.,et al.,LAPACK user's guide,(Third edition),SIAM Publications,Philadelphia,PA, 1999,407 pp. QA76.73.F25 L36 44 [AS] Argyros, I. K.and F. Szidarovszky,The theory and applications of iteration methods, CRC Press, Boca Raton,FL,1993,355 pp. QA297.8.A74644   
[AMR] Ascher, U. M.,R. M. M. Mattheij,and R.B. Russel, Numerical solution of boundary value problems for ordinary differential equations,Prentice-Hal,Englewood Clifs,NJ,1988,595 pp.QA379.A83 690 [Ax] Axelsson, O. Iterative solution methods, Cambridge University Press, New York,1994, 64 pp. QA297.8.A94482 [AB] Axelsson, O. and V. A. Barker, Finite element solution of boundary value problems: theory and computation, Academic Press, Orlando,FL,1984, 432 pp. QA379.A9739   
[Ba1] Bailey,N.T.J.,The mathematical approach to biologyand medicine,John Wiley& Sons,New York, 1967,269 pp.QH324.B28 289   
[Ba2] Bailey,N.T.J.,The mathematical theory ofepidemics,Hafner, New York,1957,194 pp.RA625.B3 289   
[BSW]Bailey,P.B.,L.F. Shampine,and P.E. Waltman,Nonlinear two-point boundary-value problems, Academic Press,New York,1968,171 pp. QA372.B27 673, 690   
[Ban] Bank,R.E., PG,A software package for solving eliptic partial diferential equations: Users' Guide 7.0, SIAM Publications,Philadelphia,PA,1994,128 pp. QA377.B26742   
[Barr] Barrett,R.,etal.,Templatesfor the solution oflinear systems: building blocks foriterative methods, SIAM Publications, Philadelphia,PA,1994,112 pp. QA297.8.T45482   
[Bart]Bartle,R. G.,The elements of real analysis, (Second edition), John Wiley & Sons,New York,1976, 480 pp. QA300.B29 105,122 [Bek] Bekker, M. G., Introduction to terrain vehicle systems, University of Michigan Press,Ann Arbor, MI,1969,846 pp. TL243.B39 77, 620 [Ber] Bernadelli，H.，Population waves， Journal of the Burma Research Society 31 (1941)，1-18, DS527.B85381 [BD] Birkhoff, G. and C.De Boor, Error bounds for spline interpolation, Journal of Mathematics and Mechanics 13 (1964), 827-836, QA1.J975152 [BL] Birkhoff, G.andR. E.Lynch, Numerical solution of elliptic problems,SIAMPublications,Philadelphia,PA,1984,319 pp. QA377.B672742 [BiR] Birkhoff, G.and G.Rota,Ordinary diferential equations,(Fourth edition),John Wiley & Sons,New York,1989,399 pp. QA372.B58252, 254,313 [BP] Botha,J.F.and G.F.Pinder,Fundamental concepts in the numerical solution of differential equations,Wiley-Interscience,New York,1983,202 pp. QA374.B74343 [Brac] Bracewell,R.,The Fourier transform and itsapplication,(Third edition),McGraw-Hill,New York, 2000,616 pp.QA403.5.B7 546 [Bram] Bramble,J.H.,Multigrid methods,John Wiley & Sons,New York,1993,161 pp.QA377.B73742 [Bre] Brent,R.,Algorithms for minimization without derivatives,Prentice-Hall,Englewood Cliffs,NJ, 1973,195 pp. QA402.5.B74 102,103 [Brigg] Briggs, W.L.,A multigrid tutorial,SIAM Publications, Philadelphia,PA,1987,88 pp. QA377.B75 742 [BH] Briggs, W.L.and V.E. Henson, The DFT: an owner's manual for the discrete Fourier transform, SIAM Publications,Philadelphia, PA,1995,434 pp. QA403.5.B75 549 [Brigh] Brigham,E.O.,Thefast Fourier transform,Prentice-Hall,EnglewoodCliffs,NJ,1974,25pp. QA403.B74538   
[Brow,K] Brown, K. M., A quadratically convergent Newton-like method based upon Gaussian elimination, SIAMJournal on Numerical Analysis 6,No.4 (1969), 560-569,QA297.A1S2 626   
[Brow,W] Brown, W.S.,A simple but realistic model offloating point computation, ACM transactions of Mathematical Software 7 (1981), 445-480, QA76.A8 42, 43 [Broy] Broyden, C.G., A class of methods for solving nonlinear simultaneous equations,Mathematics of Computation 19 (1965),577-593,QA1.M4144621 [BS1] Bulirsch R.and J. Stoer, Numerical treatment of ordinary diferential equations by extrapolation methods,Numerische Mathematik 8 (1966),1-13, QA241.N9 312 [BS2] Bulirsch,R.andJ.Stoer,Fehlerabschatzungen und extrapolation mit rationalenFunktionen bei Verfahren von Richardson-typus,Numerische Mathematik 6 (1964),413-427, QA241.N9312 [BS3] Bulirsch, R.and J. Stoer,Asymptotic upper and lower bounds for results of extrapolation methods, Numerische Mathematik 8 (1966), 93--104, QA241.N9 312 [BuR] Bunch,J.R.and D. J. Rose (eds.), Sparse matrix computations (Proceedings of a conference held at Argonne National Laboratories,September 9-11,1975),Academic Press, New York,1976,453 pp. QA188.S9 414 [BFR] Burden,R.L.,J.D.Faires,and A.C.Reynolds,Numerical Analysis, (Second edition),Prindle,Weber & Schmidt, Boston, MA,1981, 598 pp. QA297.B8495

# Bibliography

[Bur]Burrage,K.,1995,Parailel and sequential methods for ordinary differential equations,Oxford Uni-versity Press, New York,446 pp. QA372.B883343

Butcher,J. C., The non-existence of ten-stage eighth-order explicit Runge-Kut methods, BIT 25 (1985),521-542,QA76.N62 279

[CF]Chaitin-Chatelin, F. and Fraysse, V.,Lectures on finite precision computations, SIAM Publications, Philadelphia,PA,1996,235 pp. QA297.C41746

[CGGG] Char, B. W. K. O. Geddes, W. M. Gentlemen, G. H. Gonnet, The design of Maple: A compact, portable, and powerful computer algebra system, Computer Algebra. Lecture Notes in Computer Science No.162,(J. A. Van Hulzen, ed.), Springer-Verlag,Berlin,1983,101-115 pp.QA155.7 E4 E85 198346

[CCR] Chiarella,C., W. Charlton, and A. W. Roberts, Optimum chute profiles in gravity flow of granular materials: a discrete segment solution method,Transactions of the ASME, Journal of Engineering for Industry Series B 97 (1975),10-13,TJ1.A712 619

Cheney, E. W., Introduction to approximation theory，McGraw-Hill, New York,1966,259 pp. QA221.C47 549

Clenshaw, C. W. and C. W. Curtis, A method for numerical integration on an automatic computer, Numerische Mathematik 2 (1960),197-205,QA241.N9 248

Cody, W. J. and W. Waite,Software manual for the elementary functions,Prentice-Hal, Englewood Cliffs, NJ,1980,269 pp.QA331.C63546

Coleman, T.F.and C.Van Loan, Handbook for matrix computations,SIAM Publications, Philadelphia,PA,1988,264 pp. QA188.C65 44,416

Cooley, J. W.and J. W. Tukey, An algorithm for the machine calculation of complex Fourier series, Mathematics of Computation 19,No.90 (1965),297-301,QA1.M4144538

[Co]Cowell,W. (ed.)， Sources and development of mathematical software,， Prentice-Hall, Englewood Cliffs, NJ,1984,404 pp. QA76.95.S6843

[DaB]Dahquist,G.andA. Bjorck (TranslatedbyN.Anderson), Numerical methods,Prentice-Hal, Englewood Cliffs,NJ, 1974, 573 pp.QA297.D331386

Davis,P. J.,Interpolation and approximation, Dover, New York,1975,393 pp. QA221.D33165, 549

R}Davis,P.J. and P. Rabinowitz,Methods ofnumerical integration,(Second edition), Academic Press, New York,1984,612 pp.QA299.3.D28 248

[Deb] De Boor, C., A practical guide to splines, Springer-Verlag, New York,1978,392 pp. QA1.A647 vol. 27 152,164,165

{DebS]De Boor, C.and B. Swartz, Collocation at Gaussian points, SIAM Journal on Numerical Analysis 10,No.4 (1973), 582-606,QA297.A1S2 687

[DM]Dennis, J.E., Jr. and J. J. Moré, Quasi-Newton methods, motivation and theory, SIAM Review19, No.1(1977),46-89,QA1.S2 622

[DenS] Dennis,J.E.,Jr.andR.B.Schnabel,Numerical methods for unconstrainedoptimizationand nonlinear equations, Prentice-Hall, Englewood Cliffs, NJ,1983,378 pp. QA402.5.D44644

[Di]Dierckx,P., Curve and surface fiting with splines,Oxford University Pres,New York,1993,285 Pp. QA297.6.D54 165

MS]Dongarr, J. J.,J. R. Bunch, C. B. Moler, and G. W. Stewart, LINPACK users guide, SIAM Publications,Philadephia, PA,1979,367 pp. QA214.L5644

[DRW]

Dongarra, J. J.,T. Rowan,and R. Wade, Software distributions using Xnetlib, ACM Transactions on Mathematical Software 21, No.1 (1995),79-88 QA76.6.A8 44

Dongarra, J.and D. W. Walker,Software libraries for linear algebra computation on high performance computers, SIAM Review 37, No. 2(1995),151-180 QA1.S2 46

Dormand, J.R., Numerical methods fordifrential equations:acompuationalapproach,CRC Press,Boca Raton,FL,1996,368 pp. QA372.D67 343

[DoB] Dorn, G.L.and A. B.Burdick, On the recombinational structure of complementation relationships in the m-dy complex of the Drosophila melanogaster, Genetics 47 (1962), 503-518, QH431.G43 418

[E]Engels, H., Numerical quadrature and cubature， Academic Press New York，1980, 441 pp.QA299.3.E5 248

[Fe]Fehlberg, E., Klassische Runge-Kutta Formeln vierter und niedrigerer Ordnung mit Schritweiten-Kontrolle und ihre Anwendung auf Warmeleitungsprobleme, Computing 6 (197O), 61-71, QA76.C777284

[Fi]Fix,G.,A survey of numerical methods for selected problems in continuum mechanics, Proceedings of a Conference on Numerical Methods of Ocean Circulation,National Academy of Sciences (1975), 268-283,Q11.N26 739

[FM]Forsythe,G.E.and C.B.Moler, Computer solution of linear algebraic systems,Prentice-Hall, Englewood Cliffs,NJ, 1967,148 pp. QA297.F57 416, 457

[Fr]Francis,J. G. F., The QR transformation,Computer Journal 4 (1961-2), Part I,265-271; Part II, 332-345,QA76.C57589

[Fu]Fulks,W., Advanced calculus,(Third edition), John Wiley & Sons,New York,1978,731 pp. QA303.F95410,272

[Gar]Garbow,B.S.,et al.,Matrix eigensystem routines: EISPACK guide extension,Springer-Verlag,New York,1977,343 pp. QA193.M38 44

[Ge1]Gear,C.W.,Numerical initial-value problems in ordinarydifferential equations,Prentice-Hall,Englewo0d Cliffs,NJ,1971,253 pp. QA372.G4 322,325,336,343

Ge2] Gear, C. W., Numerical solution of ordinary differential equations: Is there anything left to do?, SIAM Review 23,No.1 (1981),10-24,QA1.S2 340

[GL]George, A. and J. W.Liu, Computer solution of large sparse positive definite systems, Prentice-Hall, Englew0od Cliffs,NJ,1981,324 pp. QA188.G46 416

jo] Goldberg, D., What every scientist should know about floating-point arithmetic, ACM Computing Surveys 23,No.1(1991), 5-48,QA76.5.A1 46

]Golub,G. H.and Ortega,J. M.,Scientific computing: an introduction with parallel computing,Academic Press, Boston,MA,1993,442 pp. QA76.58.G64 46,343

Golub,G.H. and C.F. Van Loan, Matrix computations, (Second edition), Johns Hopkins University Press,Baltimore,MD,1989, 642 pp. QA188.G65 400, 416

[Gr]Gragg,W.B., On extrapolation algorithms for ordinary initial-value problems, SIAM Journal on Numerical Analysis 2(1965),384-403,QA297.A1S2 307,312

# Bibliography

[GKO] Gustafsson, B., H. Kreiss,and J. Oliger,Time dependent problems and diffrence methods, John Wiley & Sons, New York,1995,642 pp. QA374.G974742

[Hac]Hackbusch, W., Iterative solution of large sparse systems of equations, Springer-Verlag, New York. 1994,429 pp. QA1.A647 vol. 95482

[HY]Hageman,L. A.and D. M. Young,Applied terative methods, Academic Press,New York,1981,386 Pp.QA297.8.H34482

[HNW1]Hairer,E.,S.P.Norset,andG.Wanner,Solving ordinary differential equations. Vol.1:Nonstif equations,(Second revised edition), Springer-Verlag,Berlin,1993,519 pp.QA372.H16322,343 [HNW2]Hairer, E.，S. P. Norsett, and G. Wanner, Solving ordinary diferential equations.Vol.2: Stif and diferential-algebraic problems, (Second revised edition)，Springer, Berlin,1996,614 pp. QA372.H16 343

[Ham]Hamming,R. W.,Numerical methods for scientists and engineers, (Second edition),McGraw-Hill New York,1973,721 pp.QA297.H28546

[Hel]Henrici,P.,Discrete variable methods in ordinary diferential equations,John Wiley & Sons, New York,1962.407 pp.QA372.H48343

[He2]Henrici, P,Elements of numerical analysis, John Wiley & Sons，New York,1964,328 pp QA297.H54 90,330

[HS]Hestenes,M. R.andE. Steifel, Conjugate gradient methods in optimization, Journal of Research ol the National Bureau of Standards 49, (1952), 409-436, Q1.N34465

[Hild]Hildebrand,F.B.,Introduction to numerical analysis,(Second edition), McGraw-Hil, New York, 1974,669 pp. QA297.H54 122,124,129

[Hill]Hill,F.S.,Jr., Computer graphics:usingopenGL,(Second edition),Prentice-Hall,Englewoodlifs NJ,2001, 922 pp.T385.H549162

[Ho] Householder, A. S., The numerical treatment of a single nonlinear equation, McGraw-Hill Neu York,1970,216 pp.QA218.H68 102,103

[IK]Issacson,E. and H.B.Keller,Analysis of numerical methods,John Wiley & Sons, New York,1966, 541 pp.QA297.1890,192,193,328,331,436,563,565,652,670,707,711,713,724

[JT]Jenkins, M.A. andJ.F.Traub,A three-stage algorithmfor real polynomials using quadratic iteration. SIAM Jourmal on Numerical Analysis 7,No.4 (1970), 545-566, QA297.A1S2102

[Joh]Johnston,R.L., Numerical methods: a software approach,John Wiley & Sons,New York,1982,276 PP.QA297.J64211

[Joyl Joyce, D. C., Survey of extrapolation processes in numerical analysis, SIAM Review 13, No. 4 (1971),435-490,QA1.S2 178

Keler,H]Keller,H.B.,Numerical methods for two-point boundary-value problems,Blaisdell, Waltham,MA. 1968,184 pp. QA372.K42 659, 664, 668, 689, 690

[Keller,J]Keller,J.B.,Probabilityof a shutout in racquetball,SIAM Review 26,No.2 (1984),267-268. QA1.S277

Kelly]Kelley,C.T.,Iterative methods for linear and nonlinear equations,SIAMPublications,Philadelphia, PA,1995,165 pp. QA297.8.K45477, 482

{Ko]Kockler, N., Numerical methods and scientific computing: using software libraries for problem solving,Oxford University Press,New York,1994,328 pp. TA345.K65346

[Lam] Lambert,J.D.,The initial value problem for ordinary diferential equations.The stateof art in numerical analysis (D. Jacobs,ed.), Academic Press, New York,1977, 451-501 pp. QA297.C646 340 [LP] Lapidus,L. and G. F. Pinder, Numerical solution of partial differential equations in science and engineering,John Wiley & Sons, New York,1982,677 pp.Q172.L36742   
[Lar] Larson,H.J.,Introduction toprobabilitytheoryandstatistical inference,(Thirdedition),John Wiley & Sons,New York,1982,637 pp. QA273.L352 486   
[Lau] Laufer, H. B., Discrete mathematics and applied modern algebra, PWS-Kent Publishing, Boston, MA,1984,538 pp. QA161.L38 546   
[LH] Lawson, C.L.and Hanson,R.J., Solving least squares problems, SIAMPublications,Philadelphia, PA,1995,337 pp.QA275.L38 549   
[LR] Lucas,T. R. and G. W. Reddien, Jr.,Some collcation methods for nonlinear boundary value problems,SIAM Journal on Numerical Analysis 9,No.2 (1972),341-356, QA297.A1S2687 [Lu] Luenberger, David G.,Linear and nonlinear programming,(Second edition), Addison-Wesley,Reading,MA,1984,245 pp. T57.7L8 471   
[Ma] Mano,M. M., Computer system architecture, Prentice-Hall, Englewood Cliffs,NJ, 1982, 531 pp. QA76.9A73 M3622   
[Mc] McCormick，S.F.， Multigrid methods， SIAM Publications，Philadelphia,PA，1987，282 pp. QA374.M84742   
[Mi] Mitchell,A. R., Computation methods in partial diffrential equations, John Wiley & Sons, New York,1969,255 pp.QA374.M68724   
[Mo] Moler, C. B., Demonstration of a matrix laboratory. Lecture notes in Mathematics (J. P. Hennart, ed.), Springer-Verlag, Berlin,1982, 84-9845   
[MC] Moré J. J. and M. Y. Cosnard, Numerical solution of nonlinear equations, ACM Transactions on Mathematical Software 5, No.1 (1979), 64-85,QA76.6.A8 626   
[MM] Morton, K. W.and D.F.Mayers, Numerical solution of partial diferential equations: an introduction, Cambridge University Press,New York,1994,227 pp. QA377.M69742   
[Mu] Muller,D.E.,A method for solving algebraic equations using an automatic computer, Mathematical Tables and Other Aids to Computation 10 (1956),208-215,QA47.M2995   
[ND] Noble,B.andJ.W.Daniel,Applied linear algebra,(Third edition),Prentice-Hal,Englewood Cliffs, NJ,1988,521 pp. QA184.N6 370,384, 551   
[Or1] Ortega,J. M., Introduction to parallel and vector solution of linear systems, Plenum Press, New York,1988,305 pp. QA218.07845   
[Or2] Ortega, J. M., Numerical analysis; a second course, Academic Press, New York, 1972, 201 pp. QA297.078424,434,445, 449,461, 557,601, 604   
[OP] Ortega, J. M. and W. G. Poole, Jr., An introduction to numerical methods for diffrential equations, Pitman Publishing,Marshfield,MA,1981,329 pp. QA371.O65343   
[OR] Ortega, J. M. and W. C. Rheinboldt, Iterative solution of nonlinear equations in several variables, Academic Press,New York,1970,572 pp. QA297.8.O77 601,634, 636, 644   
[Os] Ostrowski, A.M., Solution of equations and systems of equations, (Second edition), Academic Press, New York,1966,338 pp.QA3.P8 vol.9 103

# Bibliography

[Par] Parlett,B., The symmetric eigenvalue problem,Prentice-Hall,Englewood Cliffs,NJ,1980,348 pp. QA188.P37599 [Pat] Patterson, T. N.L.,The optimum addition of points to quadrature formulae,Mathematics of Computation 22, No.104 (1968),847-856,QA1.M4144 248 [PF] Phillps,C.and T.L.Freeman, Parallel numerical algorithms,Prentice-Hall,New York,1992,315 Pp. QA76.9.A43 F7446 [Ph] Phillips，J.，The NAG Library: a beginner's guide,Clarendon Press,Oxford， 1986,245 pp. QA297.P3545 [PDUK] Piessens, R., E.de Doncker-Kapenga, C.W. Uberhuber, and D. K. Kahaner, QUADPACK: a sub-routine package for automatic integration,Springer-Verlag,New York, 1983,301 pp. QA299.3.Q36 247 [Pi] Pissanetzky，S., Sparse matrix technology,Academic Press,New York,1984, 321 pp. QA188.P57 416 [Po] Powell, M.J. D.,Approximation theory and methods,Cambridge University Press, Cambridge,1981, 339 pp. QA221.P65137,138,165,527, 549 [Pr] Pryce,I.D., Numerical solution of Sturm-Liouville problems,Oxford University Press,New York, 1993,322 pp.QA379.P79 690 [RR] Ralston, A. and P.Rabinowitz,Afirst course in numerical analysis,(Second edition),McGraw-Hill, New York,1978,556 pp.QA297.R3209,523,527,634 [Ra] Rashevsky， N., Looking at history through mathematics, Massachusets Institute of Technology Press,Cambridge,MA,1968,199 pp.D16.25.R3 268 [RB] Rice,J.R.andR.F Boisvert,Solving elliptic problems using ELLPACK,Springer-Verlag,New York, 1985,497 pp. QA377.R53 742 [RG] Richardson, L.F.and J. A. Gaunt, The deferred approach to the limit, Philosophical Transactions of the Royal Society of London 226A (1927),299-361, Q41.L82 178 [Ro] Roache,P.J.,Eliptic marching methods and domain decomposition, CRC Press, Boca Raton, FL, 1995,190 pp.QA377.R63 742 [RS] Roberts, S.and J. Shipman, Two-point boundary value problems: shooting methods,Elsevier, New York,1972,269 pp. QA372.R76690 [RW] Rose,D. J. and R.A. Wiloughby (eds.), Sparse matrices and their applications (Proceedings of a conference held at IBMResearch, New York, September 9-10,1971. 215 pp.),Plenum Press,New York,1972,QA263.S94414 [Ru] Russell,R.D.,A comparison of collocation and finite differences for two-point boundary value problems, SIAM Journal on Numerical Analysis 14,No.1 (1977),19-39,QA297.A1S2687 [Sa1] Saad, Y.,Numerical methods for large eigenvalue problems,Halsted Press,New York,1992,46 pp. QA188.S18 587 [Sa2] Saad, Y.,Iterative methods for sparse linear systems,PWs-Kent Publishing,Boston, MA,1996,447 PP. QA188.S17 481,482 [SaS] Saff,E. B. and A. D. Snider, Fundamentals of complex analysis for mathematics, science, and engineering, (Second edition),Prentice-Hall, Englewood Cliffs,NJ,1993,468 pp. QA300.S1891

[SP]Sagar, V.andD.J.Payne,Incrementalcollapse ofthick-walled circular cylinders under steady axial tension and torsion loads and cyclic transient heating,Journal of the Mechanics and Physics of Solids 21,No. 1(1975),39-54, TA350.J68 717

Sale,P.F.andR. Dybdahl,Determinants ofcommunity structure for coral-reeffishes in experimental habitat, Ecology 56 (1975),1343-1355,QH540.E3 496

Schendel, U., Introduction to numerical methods for paralel computers， (Translated by B.W. Conolly), Halsted Press,New York,1984,151 pp.QA297.S3813 46

i]Schiesser, W.E., Computational mathematics in engineering and applied science: ODE's, DAE's, and PDE's, CRC Press, Boca Raton,FL,1994,587 pp. TA347.D45 S34 742

[Scho] Schoenberg,I. J.,Contributions to the problem of approximation of equidistant data by analytic functions, Quarterly of Applied Mathematics 4,(1946),Part A,45-99; Part B,112-141,QA1.A26 165

[Schr1] Schroeder,L. A.,Energy budget of the larvae of the moth Pachysphinx modesta, Oikos 24 (1973), 278-281, QH540.035 497

[Schr2] Schroeder, L. A., Thermal tolerances and acclimation of two species of hydras, Limnology and Oceanography 26,No.4 (1981),690-696,GC1.L5 620

ulSchultz,M. H., Spline analysis,Prentice-Hall, Englewood Cliffs,NJ,1973,156 pp. QA211.S33 152,165,673,681, 686, 687

chum]Schumaker,L.L., Spline functions: basic theory, Wiley-Interscience, New York,1981,553 pp. QA224.S33165

]Searle,S.R., Matrix algebra for the biological sciences,John Wiley& Sons,New York,1966,296 Pp.QH324.S439381

[SH]Secrist,D.A.and R.W. Hormbeck,An analysis of heat transfer and fade in disk brakes,Transactions of the ASME,Journal of Engineering for Industry Series B 98 No.2 (1976),385-390,TJ1.A712 205

[Sh]Shampine,L.F.,Numerical solution ofordinary diferential equations,Chapman &Hall,New York, 1994,484 pp. QA372.S417 343

[SGe]Shampine,L.F.and C. W. Gear,A user's view of solving stiff ordinary differential equations,SIAM Review 21,No.1 (1979),1-17,QA1.S2 340

i]Shashkov, M. andS. Steinberg,Conservative finite-diference methods on general grids,CRC Press, Boca Raton,FL,1996,359 pp.QA431.S484742

]Simon, B.and R. M. Wilson, Supercalculators on the PC,Notices of the American Mathematical Society 35,No.7 (1988),978-1001,QA1.N6 46

Singh,V.P.,Investigations of atentuation and internal friction of rocks by ultrasonics,Internationa Journal of Rock Mechanics and Mining Sciences (1976), 69-72, TA706.I45496

Sloan, I. H.and S. Joe,Lattice methods for multiple integration,Oxford University Press,New York, 1994,239 pp. QA311.S56 248

$[ \mathbb { S } \mathbf { m } , \mathbf { B } ]$ Smith, B.T.,et al., Matrix eigensystem routines: EISPACK guide, (Second edition), Springer-Verlag New York,1976,551 pp.QA193.M37 44

[Sm,G] Smith,G. D.,Numerical solution of partial diferential equations, Oxford University Pres, Neu York,1965,179 pp. QA377.S59 724

# Bibliography

[So] Sorenson， Danny C.， Parallel numerical algorithms (David E. Keyes，Ahmed Sameh and V. Vankatakrishan, eds.), Kluwer Academic Publishers, Dordrecht, 1997,119 pp. QA76.9.A43 P35 599 [Stet] Steter, H. J.,Analysis of discretization methods for ordinary diferential equations. From tracts in natural philosophy, Springer-Verlag, New York,1973,388 pp. QA372.S84312   
[Stew1] Stewart, G. W.,Afternotes on numerical analysis, SIAM Publications, Philadelphia,PA,1996,200 PP.QA297.S785402,416   
[Stew2] Stewart, G. W., Introduction to matrix computations, Academic Press, New York, 1973, 441 pp. QA188.S7402,599 [SF] Strang,W. G.and G. J. Fix,An analysis of the finite element method, Prentice-Hall, Englewood Cliffs, NJ,1973,306 pp. TA335.S77687, 739, 742 [Stri] Strikwerda,J.C.,Finite difference schemes and partial diffrential equations,Brooks/Cole Publishing,Pacific Grove, CA,1989, 386 pp. QA374.S88742   
[Stro] Stroud, A. H.,Approximate calculation of multiple integrals, Prentice-Hall,Englewood Cliffs, NJ, 1971,431 pp. QA311.S85 248 [StS] Stroud,A. H.andD. Secrest, Gaussian quadrature formulas,Prentice-Hall,Englewood Clis, N, 1966,374 pp. QA299.4.G4 S7 224, 248 [Sz] Szisz,P., Math bite, Mathematics Magazine 68,No.2,1995,97, QA1.N28430 [Th] Thomas,J. W., Numerical partial differential equations,Springer-Verlag, New York,1995, 445 pp. QA377.T495742 [Tr] Traub,J. F. Iterative methods for the solution of equations, Prentice-Hall, Englewood Cliffs, NJ, 1964,310 pp.QA297.T7 103 [Tw] Twizell,E.H.,Computational methods for partial differential equations,Ellis HorwoodLtd.,Chichester, West Sussex,England,1984,276 pp. QA377.T95742 [Van] Van Loan, C. F., Computational frameworks for the fast Fourier transform, SIAM Publications, Philadelphia,PA,1992,273 pp. QA403.5.V35549 [Var] Varga,R. S.， Matrix iterative analysis, (Second edition)， Springer， New York, 2000, 358 pp. QA263.V3482,696,700,701 [We] Wendroff, B., Theoretical numerical analysis， Academic Press， New York， 1966， 239 pp. QA297.W43400,403   
[Wil1] Wilkinson,J.H.,Rounding errors inlgebraic processes,Prentice-Hall,Englewood ClisN,96, 161 pp.QA76.5.W53 462   
[Wil2] Wilkinson, J. H.， The algebraic eigenvalue problem, Clarendon Press,Oxford, 1965，662 pp. QA218.W5462,570,578,594,599 [WR] Wilkinson, J. H.and C. Reinsch (eds.), Handbook for automatic computation. Vol. 2: Linear algebra. Springer-Verlag,New York,1971,439 pp.QA251.W6743, 590,594,595,599   
[Win] Winograd,S., On computing the discrete Fourier transform, Mathematics of Computation 32 (1978), 175-199,QA1.M4144 546 [Y] Young, D. M., Iterative solution of large linear systems, Academic Press, New York,1971,570 pp. QA195.Y68445,482