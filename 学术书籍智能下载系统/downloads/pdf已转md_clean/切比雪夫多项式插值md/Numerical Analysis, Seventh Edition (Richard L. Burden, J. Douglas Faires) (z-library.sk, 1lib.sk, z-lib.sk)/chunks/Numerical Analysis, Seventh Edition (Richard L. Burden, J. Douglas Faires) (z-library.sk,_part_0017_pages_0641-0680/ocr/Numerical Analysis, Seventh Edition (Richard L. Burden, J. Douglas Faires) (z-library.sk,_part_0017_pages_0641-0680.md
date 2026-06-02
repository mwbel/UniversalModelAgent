and

$$
g \left( { \bf x } ^ { ( 1 ) } \right) = 2 . 3 2 7 6 2 .
$$

Table 10.5 contains the remainder of the results.A true solution to the nonlinear system is $( 0 . 5 , 0 , - 0 . 5 2 3 5 9 8 8 ) ^ { t }$ ,so $\mathbf { x } ^ { ( 2 ) }$ would likely be adequate as an initial approximation for Newton's method or Broyden's method. One of these quicker converging techniques would be appropriate at this stage, since 7O iterations of the Steepest Descent method are required to find $\| \mathbf { x } ^ { ( k ) } - \mathbf { x } \| _ { \infty } < 0 . 0 1$ ■

Table 10.5

<table><tr><td>k</td><td>海</td><td>新</td><td>珍</td><td>（k） (k） (k） g(x ，x2 X3</td></tr><tr><td>2</td><td>0.137860</td><td>--0.205453</td><td>-0.522059</td><td>1.27406</td></tr><tr><td>3</td><td>0.266959</td><td>0.00551102</td><td>-0.558494</td><td>1.06813</td></tr><tr><td>4</td><td>0.272734</td><td>-0.00811751</td><td>-0.522006</td><td>0.468309</td></tr><tr><td>5</td><td>0.308689</td><td>-0.0204026</td><td>-0.533112</td><td>0.381087</td></tr><tr><td>6</td><td>0.314308</td><td>-0.0147046</td><td>-0.520923</td><td>0.318837</td></tr><tr><td>7</td><td>0.324267</td><td>--0.00852549</td><td>-0.528431</td><td>0.287024</td></tr></table>

Algorithm 10.3 applies the method of Steepest Descent to approximate the minimal value of $g ( \mathbf { x } )$ . To begin an iteration, the value O is assigned to $\pmb { \alpha } _ { 1 }$ and the value 1 is assigned to $\alpha _ { 3 }$ . If $h ( \alpha _ { 3 } ) \geq h ( \alpha _ { 1 } )$ ,then successive divisions of $\pmb { \alpha } _ { 3 }$ by 2 are performed and the value of $\alpha _ { 3 }$ is reassigned until $h ( \alpha _ { 3 } ) < h ( \alpha _ { 1 } )$ and $\alpha _ { 3 } = 2 ^ { - k }$ for some value of $k$

To employ the method to approximate the solution to the system

$$
\begin{array} { r } { f _ { 1 } ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } ) = 0 , } \\ { f _ { 2 } ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } ) = 0 , } \\ { \vdots \qquad \vdots } \\ { f _ { n } ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } ) = 0 , } \end{array}
$$

we simply replace the function $\pmb { g }$ with $\sum _ { i = 1 } ^ { n } f _ { i } ^ { 2 }$

# Steepest Descent

To approximate a solution p to the minimization problem

$$
g ( { \bf p } ) = \operatorname* { m i n } _ { { \bf x } \in { \mathbb R } ^ { n } } g ( { \bf x } )
$$

given an initial approximation x:

INPUT number $\pmb { n }$ of variables; initial approximation $\mathbf { x } = ( x _ { 1 } , \ldots , x _ { n } ) ^ { t }$ ; tolerance TOL; maximum number of iterations $N$

OUTPUT approximate solution $\mathbf { x } = ( x _ { 1 } , \ldots , x _ { n } ) ^ { t }$ or a message of failure. Step 1 Set $k = 1$

Step 2 While $( k \leq N )$ do Steps 3-15.

Step 3Set $\begin{array} { r l } & { g _ { 1 } = g ( x _ { 1 } , \ldots , x _ { n } ) ; \quad \left( N o t e \colon g _ { 1 } = g \left( \mathbf { x } ^ { ( k ) } \right) . \right) } \\ & { \mathbf { z } = \nabla g ( x _ { 1 } , \ldots , x _ { n } ) ; \quad \left( N o t e \colon \mathbf { z } = \nabla g \left( \mathbf { x } ^ { ( k ) } \right) . \right) } \\ & { z _ { 0 } = | | \mathbf { z } | | _ { 2 } . } \end{array}$

Step 4 If $z _ { 0 } = 0$ then OUTPUT (\*Zero gradient'); OUTPUT $( x _ { 1 } , \ldots , x _ { n } , g _ { 1 } )$ ； (The procedure completed, may have a minimum.) STOP.

Step 5Se $\begin{array} { r l } & { \mathrm { \bf ~ t } \mathbf { z } = \mathbf { z } / z _ { 0 } ; \quad ( M a k e \mathrm { \bf ~ z } a u n i t \nu e c t o r . ) } \\ & { \alpha _ { 1 } = 0 ; } \\ & { \alpha _ { 3 } = 1 ; } \\ & { g _ { 3 } = g ( \mathbf { x } - \alpha _ { 3 } \mathbf { z } ) . } \end{array}$

Step 6 While $\left( g _ { 3 } \geq g _ { 1 } \right)$ do Steps 7 and 8.

$$
\begin{array} { r l } { { 9 } p 7 } & { \operatorname { S e t } \alpha _ { 3 } = \alpha _ { 3 } / 2 ; } \\ & { \qquad g _ { 3 } = g ( \mathbf x - \alpha _ { 3 } \mathbf z ) . } \end{array}
$$

Step 8If $\alpha _ { 3 } < T O L / 2$ then OUTPUT ( $\mathbf { \sigma } ^ { \prime } \mathbf { N o }$ likely improvement'); OUTPUT $( x _ { 1 } , \ldots , x _ { n } , g _ { 1 } )$ ； (The procedure completed, may have a minimum.) STOP.

Step 9 Set $\alpha _ { 2 } = \alpha _ { 3 } / 2$ $g _ { 2 } = g ( \mathbf { x } - \alpha _ { 2 } \mathbf { z } ) .$

Step 10 Set $h _ { 1 } = ( g _ { 2 } - g _ { 1 } ) / \alpha _ { 2 } ;$ $h _ { 2 } = ( g _ { 3 } - g _ { 2 } ) / ( \alpha _ { 3 } - \alpha _ { 2 } ) ;$ $h _ { 3 } = ( h _ { 2 } - h _ { 1 } ) / \alpha _ { 3 } .$ (Note: Newton's forward divided-difference formula is used to find the quadratic $P ( \alpha ) = g _ { 1 } + h _ { 1 } \alpha + h _ { 3 } \alpha ( \alpha - \alpha _ { 2 } )$ that interpolates $h ( \alpha )$ at ${ \pmb { \alpha } } = { \bf 0 }$ ， ${ \pmb { \alpha } } = { \pmb { \alpha } } _ { 2 } ^ { \prime }$ ， ${ \pmb { \alpha } } = { \pmb { \alpha } } _ { 3 }$ .）

Step 11 Set $\alpha _ { 0 } = 0 . 5 ( \alpha _ { 2 } - h _ { 1 } / h _ { 3 } )$ ；(The critical point of $P$ occurs at $\alpha _ { 0 }$ ）$g _ { 0 } = g ( \mathbf { x } - \alpha _ { 0 } \mathbf { z } )$

Step 12 Find $\pmb { \alpha }$ from $\left\{ \alpha _ { 0 } , \alpha _ { 3 } \right\}$ so that $g = g ( \mathbf x - \alpha \mathbf z ) = \operatorname* { m i n } \{ g _ { 0 } , g _ { 3 } \}$

Step 13 Set $\mathbf { x } = \mathbf { x } - \alpha \mathbf { z }$

Step 14 If $| g - g _ { 1 } | < T O L$ then OUTPUT $( x _ { 1 } , \ldots , x _ { n } , g )$ ； (The procedure was successful.) STOP.

Step 15 Set $k = k + 1$

Step 16OUTPUT(‘Maximum iterations exceeded'); (The procedure was unsuccessful.) STOP.

There are many variations of the method of Steepest Descent, some of which involve more intricate methods for determining the value of $\pmb { \alpha }$ that will produce a minimum for the single-variable function $h$ defined in Eq. (10.18). Other techniques use a multidimen-sional Taylor polynomial to replace the original multivariable function $\pmb { g }$ and minimize the polynomial instead of $g$ . Although there are advantages to some of these methods over the procedure discussed here, all the Steepest Descent methods are, in general, linearly convergent and converge independent of the starting approximation. In some instances, however, the methods may converge to something other than the absolute minimum of the function $g$

A more complete discussion of Steepest Descent methods can be found in [OR] or [RR].

1. Use the method of Steepest Descent with $T O L = 0 . 0 5$ to approximate the solutions of the following nonlinear systems.

$$
\begin{array} { r l r } { \quad } & { } & { 4 x _ { 1 } ^ { 2 } - 2 0 x _ { 1 } + \frac { 1 } { 4 } x _ { 2 } ^ { 2 } + 8 = 0 , } \\ { \quad } & { } & { \frac { 1 } { 2 } x _ { 1 } x _ { 2 } ^ { 2 } + 2 x _ { 1 } - 5 x _ { 2 } + 8 = 0 , } \\ { \quad } & { } & { \ln ( x _ { 1 } ^ { 2 } + x _ { 2 } ^ { 2 } ) - \sin ( x _ { 1 } x _ { 2 } ) = \ln 2 + \ln \pi , } \\ { \quad } & { } & { e ^ { \varepsilon _ { 1 } - x _ { 2 } } + \cos ( x _ { 1 } x _ { 2 } ) = 0 . } \\ { \quad } & { } & { \sin ( 4 \pi x _ { 1 } x _ { 2 } ) - 2 x _ { 2 } - x _ { 1 } = 0 , } \\ { \quad } & { } & { \left( \frac { 4 \pi - 1 } { 4 \pi } \right) ( e ^ { 2 x _ { 1 } } - e ) + 4 e x _ { 2 } ^ { 2 } - 2 e x _ { 1 } = 0 . } \end{array}
$$

2. Use the results in Exercise 1 and Newton's method to approximate the solutions of the nonlinear systems in Exercise 1 to within $1 0 ^ { - 6 }$

Use the method of Steepest Descent with $T O L = 0 . 0 5$ to approximate the solutions of the following nonlinear systems.

a. $\begin{array} { c } { { 1 5 x _ { 1 } + x _ { 2 } ^ { 2 } - 4 x _ { 3 } = 1 3 , } } \\ { { x _ { 1 } ^ { 2 } + 1 0 x _ { 2 } - x _ { 3 } = 1 1 , } } \\ { { x _ { 2 } ^ { 3 } - 2 5 x _ { 3 } = - 2 2 . } } \end{array}$ $\begin{array} { r l r } { \mathbf { b } . } & { } & { 1 0 x _ { 1 } - 2 x _ { 2 } ^ { 2 } + x _ { 2 } - 2 x _ { 3 } - 5 = 0 , } \\ & { } & { 8 x _ { 2 } ^ { 2 } + 4 x _ { 3 } ^ { 2 } - 9 = 0 , } \\ & { } & { 8 x _ { 2 } x _ { 3 } + 4 = 0 . } \end{array}$   
c. $x _ { 1 } ^ { 3 } + x _ { 1 } ^ { 2 } x _ { 2 } - x _ { 1 } x _ { 3 } + 6 = 0 ,$ $e ^ { x _ { 1 } } + e ^ { x _ { 2 } } - x _ { 3 } = 0 ,$ x²-2x1x=4.   
d. $\begin{array} { r } { x _ { 1 } + \cos ( x _ { 1 } x _ { 2 } x _ { 3 } ) - 1 = 0 , } \\ { ( 1 - x _ { 1 } ) ^ { 1 / 4 } + x _ { 2 } + 0 . 0 5 x _ { 3 } ^ { 2 } - 0 . 1 5 x _ { 3 } - 1 = 0 , } \\ { - x _ { \mathrm { I } } ^ { 2 } - 0 . 1 x _ { 2 } ^ { 2 } + 0 . 0 1 x _ { 2 } + x _ { 3 } - 1 = 0 . } \end{array}$

3.Use the results of Exercise 3 and Newton's method to approximate the solutions to within $1 0 ^ { - 6 }$ for the nonlinear systems in Exercise 3.

4.Use the method of Steepest Descent to approximate minima to within 0.005 forthe following functions.

$$
\begin{array} { l } { g ( x _ { 1 } , x _ { 2 } ) = \cos ( x _ { 1 } + x _ { 2 } ) + \sin x _ { 1 } + \cos x _ { 2 } } \\ { g ( x _ { 1 } , x _ { 2 } ) = 1 0 0 ( x _ { 1 } ^ { 2 } - x _ { 2 } ) ^ { 2 } + ( 1 - x _ { 1 } ) ^ { 2 } } \\ { g ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) = x _ { 1 } ^ { 2 } + 2 x _ { 2 } ^ { 2 } + x _ { 3 } ^ { 2 } - 2 x _ { 1 } x _ { 2 } + 2 x _ { 1 } - 2 . 5 x _ { 2 } - x _ { 3 } + 2 } \\ { g ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) = x _ { 1 } ^ { 4 } + 2 x _ { 2 } ^ { 4 } + 3 x _ { 3 } ^ { 4 } + 1 . 0 1 } \end{array}
$$

5．a.Show that the quadratic polynomial

$$
P ( \alpha ) = g _ { 1 } + h _ { 1 } \alpha + h _ { 3 } \alpha ( \alpha - \alpha _ { 2 } )
$$

interpolates the function $h$ defined in (10.18):

$$
h ( \alpha ) = g \left( \mathbf { x } ^ { ( 0 ) } - \alpha \nabla g ( \mathbf { x } ^ { ( 0 ) } ) \right)
$$

at $\alpha = 0 , \alpha _ { 2 }$ ,and $\pmb { \alpha } _ { 3 }$

b.Show that a critical point of $P$ occurs at

$$
\alpha _ { 0 } = \frac { 1 } { 2 } \left( \alpha _ { 2 } - \frac { h _ { 1 } } { h _ { 3 } } \right) .
$$

# 10.5Homotopy and Continuation Methods

Homotopy,or continuation, methods for nonlinear systems embed the problemto be solved within a collection of problems. Specifically, to solve a problem of the form

$$
\mathbf { F } ( \mathbf { x } ) = \mathbf { 0 } ,
$$

which has the unknown solution $\mathbf { x } ^ { \ast }$ , we consider a family of problems described using a parameter $\lambda$ that assumes values in [O,1]. A problem with a known solution ${ \bf x } ( 0 )$ corresponds to $\lambda = 0$ ,and the problem with the unknown solution $\mathbf { x } ( 1 ) \equiv \mathbf { x } ^ { * }$ corresponds to $\lambda = 1$

For example, suppose ${ \bf x } ( 0 )$ is an initial approximation to the solution of $\mathbf { F ( x ^ { * } ) } = \mathbf { 0 }$ Define

$$
\mathbf { G } : [ 0 , 1 ] \times \mathbb { R } ^ { n }  \mathbb { R } ^ { n }
$$

by

$$
\mathbf { G } ( \lambda , \mathbf { x } ) = \lambda \mathbf { F } ( \mathbf { x } ) + ( 1 - \lambda ) \left[ \mathbf { F } ( \mathbf { x } ) - \mathbf { F } ( \mathbf { x } ( 0 ) ) \right] = \mathbf { F } ( \mathbf { x } ) + ( \lambda - 1 ) \mathbf { F } ( \mathbf { x } ( 0 ) ) .
$$

We will determine, for various values of $\lambda$ , a solution to

$$
\mathbf { G } ( { \boldsymbol { \lambda } } , \mathbf { x } ) = \mathbf { 0 } .
$$

When $\lambda = 0$ ,this equation assumes the form

$$
\mathbf { 0 } = \mathbf { G } ( 0 , \mathbf { x } ) = \mathbf { F } ( \mathbf { x } ) - \mathbf { F } ( \mathbf { x } ( 0 ) ) ,
$$

and ${ \bf x } ( 0 )$ is a solution. When $\lambda = 1$ , the equation assumes the form

$$
\mathbf { 0 } = \mathbf { G } ( 1 , \mathbf { x } ) = \mathbf { F } ( \mathbf { x } ) ,
$$

and $\mathbf { x } ( 1 ) = \mathbf { x } ^ { * }$ is a solution.

The function $\mathbf { G }$ , with the parameter $\lambda$ , provides us with a family of functions that can lead from the known value ${ \bf x } ( 0 )$ to the solution $\mathbf { x } ( 1 ) = \mathbf { x } ^ { * }$ . The function $\mathbf { G }$ is called a homotopy between the function $\mathbf { G } ( 0 , \mathbf { x } ) = \mathbf { F } ( \mathbf { x } ) - \mathbf { F } ( \mathbf { x } ( 0 ) )$ and the function $\mathbf { G } ( 1 , \mathbf { x } ) =$ $\mathbf { F } ( \mathbf { x } )$

The continuation problem is to:

Determine a way to proceed from the known solution ${ \bf x } ( 0 )$ of $\mathbf G ( 0 , \mathbf x )$ to the unknown solution $\mathbf { x } ( 1 ) = \mathbf { x } ^ { * }$ of $\mathbf { G } ( 1 , \mathbf { x } ) = \mathbf { 0 }$ that solves $\mathbf { F } ( \mathbf { x } ) = \mathbf { 0 }$

We first assume that $\mathbf { x } ( \lambda )$ is the unique solution to the equation

$$
\begin{array} { r } { { \bf G } ( \boldsymbol { \lambda } , { \bf x } ) = { \bf 0 } , } \end{array}
$$

for each $\lambda \in [ 0 , 1 ]$ . The set $\{ \mathbf { x } ( \lambda ) \mid 0 \leq \lambda \leq 1 \}$ can be viewed as a curve in $\textstyle { \mathbb { R } } ^ { n }$ from ${ \bf x } ( 0 )$ to $\mathbf { x } ( 1 ) = \mathbf { x } ^ { * }$ parameterized by $\lambda$ . A continuation method finds a sequence of steps along this curve corresponding to $\{ \mathbf { x } ( \lambda _ { k } ) \} _ { k = 0 } ^ { m }$ , where $\lambda _ { 0 } = 0 < \lambda _ { 1 } < \cdot \cdot \cdot < \lambda _ { m } = 1$

If the functions $\lambda  \mathbf { x } ( \lambda )$ and $\mathbf { G }$ are differentiable, then differentiating Eq.(10.20) with respect to $\lambda$ gives

$$
\mathbf { \boldsymbol { \mathfrak { 0 } } } = \frac { \partial \mathbf { G } ( \lambda , \mathbf { x } ( \lambda ) ) } { \partial \lambda } + \frac { \partial \mathbf { G } ( \lambda , \mathbf { x } ( \lambda ) ) } { \partial \mathbf { x } } \mathbf { \boldsymbol { x } } ^ { \prime } ( \lambda ) ,
$$

and solving for $\mathbf { x } ^ { \prime } ( \lambda )$ gives

$$
\mathbf { x } ^ { \prime } ( \lambda ) = - \left[ \frac { \partial \mathbf { G } ( \lambda , \mathbf { x } ( \lambda ) ) } { \partial \mathbf { x } } \right] ^ { - 1 } \frac { \partial \mathbf { G } ( \lambda , \mathbf { x } ( \lambda ) ) } { \partial \lambda } .
$$

This is a a system of differential equations with the initial condition ${ \bf x } ( 0 )$

Since

$$
\mathbf { G } ( \lambda , \mathbf { x } ( \lambda ) ) = \mathbf { F } ( \mathbf { x } ( \lambda ) ) + ( \lambda - 1 ) \mathbf { F } ( \mathbf { x } ( 0 ) ) ,
$$

we can determine both

$$
\frac { \partial \mathbf { G } } { \partial \mathbf { x } } ( \lambda , \mathbf { x } ( \lambda ) ) = \left[ \begin{array} { l l l l } { \frac { \partial f _ { 1 } } { \partial x _ { 1 } } ( \mathbf { x } ( \lambda ) ) } & { \frac { \partial f _ { 1 } } { \partial x _ { 2 } } ( \mathbf { x } ( \lambda ) ) } & { \dots } & { \frac { \partial f _ { 1 } } { \partial x _ { n } } ( \mathbf { x } ( \lambda ) ) } \\ { \frac { \partial f _ { 2 } } { \partial x _ { 1 } } ( \mathbf { x } ( \lambda ) ) } & { \frac { \partial f _ { 2 } } { \partial x _ { 2 } } ( \mathbf { x } ( \lambda ) ) } & { \dots } & { \frac { \partial f _ { 2 } } { \partial x _ { n } } ( \mathbf { x } ( \lambda ) ) } \\ { \vdots } & & & \\ { \frac { \partial f _ { n } } { \partial x _ { 1 } } ( \mathbf { x } ( \lambda ) ) } & { \frac { \partial f _ { n } } { \partial x _ { 2 } } ( \mathbf { x } ( \lambda ) ) } & { \dots } & { \frac { \partial f _ { n } } { \partial x _ { n } } ( \mathbf { x } ( \lambda ) ) } \end{array} \right] = J ( \mathbf { x } ( \lambda ) ) ,
$$

the Jacobian matrix, and

$$
\frac { \partial \mathbf { G } ( \boldsymbol { \lambda } , \mathbf { x } ( \boldsymbol { \lambda } ) ) } { \partial \boldsymbol { \lambda } } = \mathbf { F } ( \mathbf { x } ( 0 ) ) .
$$

Therefore, the system of differential equations becomes

$$
\mathbf { x } ^ { \prime } ( \lambda ) = - [ J ( \mathbf { x } ( \lambda ) ) ] ^ { - 1 } \mathbf { F } ( \mathbf { x } ( 0 ) ) , \quad \mathrm { f o r } \quad 0 \leq \lambda \leq 1 ,
$$

with the initial condition ${ \bf x } ( 0 )$ ，

The following theorem (see [OR,pp. 230-231l) gives conditions under which the continuation method is feasible.

Theorem 10.10 Let $\mathbf { F } ( \mathbf { x } )$ be continuously differentiable for $\mathbf { x } \in \mathbb { R } ^ { n }$ . Suppose that the Jacobian matrix $J ( \mathbf { x } )$ is nonsingular for all $\mathbf { x } \in \mathbb { R } ^ { n }$ and that a constant $M$ exists with $\| J ( \mathbf { x } ) ^ { - 1 } \| \leq M$ ,for all $\mathbf { x } \in \mathbb { R } ^ { n }$ . Then, for any ${ \bf x } ( 0 )$ in $\mathbb { R } ^ { n }$ , there exists a unique function $\mathbf { x } ( \lambda )$ ,such that

$$
\mathbf { G } ( \lambda , { \mathbf { x } ( \lambda ) } ) = \mathbf { 0 } ,
$$

for all $\lambda$ in [0,1]. Moreover, $\mathbf { x } ( \lambda )$ is continuously differentiable and

$$
\mathbf { x } ^ { \prime } ( \lambda ) = - J ( \mathbf { x } ( \lambda ) ) ^ { - 1 } \mathbf { F } ( \mathbf { x } ( 0 ) ) , \quad \mathrm { f o r } \operatorname { e a c h } \lambda \in [ 0 , 1 ] .
$$

The following example shows the form of the system of differential equations associated with a nonlinear system of equations.

EXAMPLE 1 Consider the nonlinear system

$$
\begin{array} { l } { f _ { 1 } ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) = 3 x _ { 1 } - \cos ( x _ { 2 } x _ { 3 } ) - 0 . 5 = 0 , } \\ { f _ { 2 } ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) = x _ { 1 } ^ { 2 } - 8 1 ( x _ { 2 } + 0 . 1 ) ^ { 2 } + \sin x _ { 3 } + 1 . 0 6 = 0 , } \\ { f _ { 3 } ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) = e ^ { - x _ { 1 } x _ { 2 } } + 2 0 x _ { 3 } + \displaystyle \frac { 1 0 \pi - 3 } { 3 } = 0 . } \end{array}
$$

The Jacobian matrix is

$$
\begin{array} { r } { J \left( \mathbf { x } \right) = \left[ \begin{array} { c c c } { 3 } & { x _ { 3 } \sin x _ { 2 } x _ { 3 } } & { x _ { 2 } \sin x _ { 2 } x _ { 3 } } \\ { 2 x _ { 1 } } & { - 1 6 2 ( x _ { 2 } + 0 . 1 ) } & { \cos x _ { 3 } } \\ { - x _ { 2 } e ^ { - x _ { 1 } x _ { 2 } } } & { - x _ { 1 } e ^ { - x _ { 1 } x _ { 2 } } } & { 2 0 } \end{array} \right] . } \end{array}
$$

Let $\mathbf { x } ( 0 ) = ( 0 , 0 , 0 ) ^ { t }$ ,so that

$$
\mathbf { F } ( \mathbf { x } ( 0 ) ) = \left[ \begin{array} { c } { - 1 . 5 } \\ { 0 . 2 5 } \\ { 1 0 \pi / 3 } \end{array} \right] .
$$

The system of differential equations is

$$
\left[ { x _ { 1 } ^ { \prime } ( \lambda ) } \atop { x _ { 2 } ^ { \prime } ( \lambda ) } \right] = - \left[ \begin{array} { c c c } { 3 } & { x _ { 3 } \sin x _ { 2 } x _ { 3 } } & { x _ { 2 } \sin x _ { 2 } x _ { 3 } } \\ { 2 x _ { 1 } } & { - 1 6 2 ( x _ { 2 } + 0 . 1 ) } & { \cos x _ { 3 } } \\ { - x _ { 2 } e ^ { - x _ { 1 } x _ { 2 } } } & { - x _ { 1 } e ^ { - x _ { 1 } x _ { 2 } } } & { 2 0 } \end{array} \right] ^ { - 1 } \left[ \begin{array} { c } { - 1 . 5 } \\ { 0 . 2 5 } \\ { 1 0 \pi / 3 } \end{array} \right] .
$$

In general, the system of diffrential equations that we need to solve for our continuation problem has the form

$$
\begin{array} { l } { \displaystyle \frac { d x _ { 1 } } { d \lambda } = \phi _ { 1 } ( \lambda , x _ { 1 } , x _ { 2 } , \dots , x _ { n } ) , } \\ { \displaystyle \frac { d x _ { 2 } } { d \lambda } = \phi _ { 2 } ( \lambda , x _ { 1 } , x _ { 2 } , \dots , x _ { n } ) , } \\ { \vdots } \\ { \displaystyle \frac { d x _ { n } } { d \lambda } = \phi _ { n } ( \lambda , x _ { 1 } , x _ { 2 } , \dots , x _ { n } ) , } \end{array}
$$

where

$$
\begin{array} { r } { \left[ \begin{array} { c } { \phi _ { 1 } ( \lambda , x _ { 1 } , \dots , x _ { n } ) } \\ { \phi _ { 2 } ( \lambda , x _ { 1 } , \dots , x _ { n } ) } \\ { \vdots } \\ { \phi _ { n } ( \lambda , x _ { 1 } , \dots , x _ { n } ) } \end{array} \right] = - J ( x _ { 1 } , \dots , x _ { n } ) ^ { - 1 } \left[ \begin{array} { c } { f _ { 1 } ( \mathbf { x } ( 0 ) ) } \\ { f _ { 2 } ( \mathbf { x } ( 0 ) ) } \\ { \vdots } \\ { f _ { n } ( \mathbf { x } ( 0 ) ) } \end{array} \right] . } \end{array}
$$

To use the Runge-Kutta method of order four to solve this system, we first choose an integer $N > 0$ and let $h = ( 1 - 0 ) / N$ . Partition the interval [0,1] into $N$ subintervals with the mesh points

$$
\lambda _ { j } = j h , \quad { \mathrm { f o r } } \operatorname { e a c h } \quad j = 0 , 1 , \ldots , N .
$$

We use the notation $w _ { i j }$ , for each $j = 0 , 1 , \ldots , N$ and $i = 1 , \ldots , n$ , to denote an approximation to $x _ { i } ( \lambda _ { j } )$ . For the initial conditions,set

$$
w _ { 1 , 0 } = x _ { 1 } ( 0 ) , \quad w _ { 2 , 0 } = x _ { 2 } ( 0 ) , \quad \ldots , \quad w _ { n , 0 } = x _ { n } ( 0 ) .
$$

Suppose $w _ { 1 , j } , w _ { 2 , j } , \ldots , w _ { n , j }$ have been computed. We obtain $w _ { 1 , j + 1 } , \ w _ { 2 , j + 1 } , \ \dotsc ,$ $w _ { n , j + 1 }$ using the equations

$$
\begin{array} { l } { { k _ { 1 , i } = h \phi _ { i } ( \lambda _ { j } , w _ { 1 , j } , w _ { 2 , j } , \ldots , w _ { n , j } ) , \quad \mathrm { f o r e a c h } \quad i = 1 , 2 , \ldots , n ; } } \\ { { k _ { 2 , i } = h \phi _ { i } \left( \lambda _ { j } + \displaystyle \frac { h } { 2 } , w _ { 1 , j } + \displaystyle \frac { 1 } { 2 } k _ { 1 , 1 } , w _ { 2 , j } + \displaystyle \frac { 1 } { 2 } k _ { 1 , 2 } , \ldots , w _ { n , j } + \displaystyle \frac { 1 } { 2 } k _ { 1 , n } \right) . } } \end{array}
$$

for each $i = 1 , 2 , \dots , n ;$

$$
k _ { 3 , i } = h \phi _ { i } \left( \lambda _ { j } + \frac { h } { 2 } , w _ { 1 , j } + \frac { 1 } { 2 } k _ { 2 , 1 } , w _ { 2 , j } + \frac { 1 } { 2 } k _ { 2 , 2 } , \ldots , w _ { n , j } + \frac { 1 } { 2 } k _ { 2 , n } \right) ,
$$

for each $i = 1 , 2 , \dots , n ;$

$$
k _ { 4 , i } = h \phi _ { i } ( \lambda _ { j } + h , w _ { 1 , j } + k _ { 3 , 1 } , w _ { 2 , j } + k _ { 3 , 2 } , \ldots , w _ { n , j } + \dot { k } _ { 3 , n } ) ,
$$

for each $i = 1 , 2 , \dots , n ;$

and, finally

$$
w _ { i , j + 1 } = w _ { i , j } + \frac { 1 } { 6 } \left( k _ { 1 , i } + 2 k _ { 2 , i } + 2 k _ { 3 , i } + k _ { 4 , i } \right) , \quad \mathrm { f o r e a c h } i = 1 , 2 , \dots , n .
$$

We use the vector notation

$$
\mathbf { k } _ { 1 } = \left[ \begin{array} { c } { k _ { 1 , 1 } } \\ { k _ { 1 , 2 } } \\ { \vdots } \\ { k _ { 1 , n } } \end{array} \right] , \ \mathbf { k } _ { 2 } = \left[ \begin{array} { c } { k _ { 2 , 1 } } \\ { k _ { 2 , 2 } } \\ { \vdots } \\ { k _ { 2 , n } } \end{array} \right] , \ \mathbf { k } _ { 3 } = \left[ \begin{array} { c } { k _ { 3 , 1 } } \\ { k _ { 3 , 2 } } \\ { \vdots } \\ { k _ { 3 , n } } \end{array} \right] , \ \mathbf { k } _ { 4 } = \left[ \begin{array} { c } { k _ { 4 , 1 } } \\ { k _ { 4 , 2 } } \\ { \vdots } \\ { k _ { 4 , n } } \end{array} \right] ,
$$

$$
\begin{array} { r } { \mathbf { w } _ { j } = \left[ \begin{array} { c } { w _ { 1 , j } } \\ { w _ { 2 , j } } \\ { \vdots } \\ { w _ { n , j } } \end{array} \right] } \end{array}
$$

to simplify the presentation.

Eq. (10.22) gives us ${ \bf x } ( 0 ) = { \bf x } ( \lambda _ { 0 } ) = { \bf w } _ { 0 }$ , and for each $j = 0 , 1 , \ldots , N ,$

$$
\begin{array} { r l } & { \mathbf { k } _ { 1 } = \hbar \left[ \begin{array} { l l l } { \phi _ { 1 } ( \lambda _ { j } , w _ { 1 , j } , \ldots , w _ { n , j } ) } \\ { \phi _ { 2 } ( \lambda _ { j } , w _ { 1 , j } , \ldots , w _ { n , j } ) } \\ { \vdots } \\ { \phi _ { n } ( \lambda _ { j } , w _ { 1 , j } , \ldots , w _ { n , j } ) } \\ { \vdots } \\ { \phi _ { n } ( \lambda _ { j } , w _ { 1 , j } , \ldots , w _ { n , j } ) } \end{array} \right] = \hbar \left[ - \mathcal { I } ( \mathbf { w } _ { 1 , j } , \ldots , \ , w _ { n , j } ) \right] ^ { - 1 } \mathbf { F } ( \mathbf { x } ( 0 ) ) } \\ & { } \\ & { \quad = \hbar \left[ - \mathcal { I } ( \mathbf { w } _ { j } ) \right] ^ { - 1 } \mathbf { F } ( \mathbf { x } ( 0 ) ) ; } \\ & { \mathbf { k } _ { 2 } = \hbar \left[ - \mathcal { I } \left( \mathbf { w } _ { j } + \frac { 1 } { 2 } \mathbf { k } _ { 1 } \right) \right] ^ { - 1 } \mathbf { F } ( \mathbf { x } ( 0 ) ) ; } \\ & { \mathbf { k } _ { 3 } = \hbar \left[ - \mathcal { I } \left( \mathbf { w } _ { j } + \frac { 1 } { 2 } \mathbf { k } _ { 2 } \right) \right] ^ { - 1 } \mathbf { F } ( \mathbf { x } ( 0 ) ) ; } \\ & { \mathbf { k } _ { 4 } = \hbar \left[ - \mathcal { I } \left( \mathbf { w } _ { j } + \mathbf { k } _ { 3 } \right) \right] ^ { - 1 } \mathbf { F } ( \mathbf { x } ( 0 ) ) ; } \end{array}
$$

and

$$
\mathbf { x } ( \lambda _ { j + 1 } ) = \mathbf { x } ( \lambda _ { j } ) + { \frac { 1 } { 6 } } \left( \mathbf { k } _ { 1 } + 2 \mathbf { k } _ { 2 } + 2 \mathbf { k } _ { 3 } + \mathbf { k } _ { 4 } \right) = \mathbf { w } _ { j } + { \frac { 1 } { 6 } } \left( \mathbf { k } _ { 1 } + 2 \mathbf { k } _ { 2 } + 2 \mathbf { k } _ { 3 } + \mathbf { k } _ { 4 } \right) .
$$

Finally, $\mathbf { x } ( \lambda _ { n } ) = \mathbf { x } ( 1 )$ is our approximation to $\pmb { \chi } ^ { * }$

# EXAMPLE 2

We will approximate the solution to

$$
\begin{array} { l l } { f _ { 1 } ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) = 3 x _ { 1 } - \cos ( x _ { 2 } x _ { 3 } ) - 0 . 5 = 0 , } \\ { f _ { 2 } ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) = x _ { 1 } ^ { 2 } - 8 1 ( x _ { 2 } + 0 . 1 ) ^ { 2 } + \sin x _ { 3 } + 1 . 0 6 = 0 , } \\ { f _ { 3 } ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) = e ^ { - x _ { 1 } , x _ { 2 } } + 2 0 x _ { 3 } + \displaystyle \frac { 1 0 \pi - 3 } { 3 } = 0 . } \end{array}
$$

The Jacobian matrix is

$$
\begin{array} { r } { J ( { \bf x } ) = \left[ { \begin{array} { c c c } { 3 } & { x _ { 3 } \sin x _ { 2 } x _ { 3 } } & { x _ { 2 } \sin x _ { 2 } x _ { 3 } } \\ { 2 x _ { 1 } } & { - 1 6 2 ( x _ { 2 } + 0 . 1 ) } & { \cos x _ { 3 } } \\ { - x _ { 2 } e ^ { - x _ { 1 } x _ { 2 } } } & { - x _ { 1 } e ^ { - x _ { 1 } x _ { 2 } } } & { 2 0 } \end{array} } \right] . } \end{array}
$$

Let $\mathbf { x } ( 0 ) = ( 0 , 0 , 0 ) ^ { t }$ , so that

$$
F ( \mathbf { x } ( 0 ) ) = ( - 1 . 5 , 0 . 2 5 , 1 0 \pi / 3 ) ^ { t } .
$$

With $N = 4$ and $h = 0 . 2 5$ , we have

$$
{ \bf k } _ { 1 } = h [ - J ( { \bf x } ^ { ( 0 ) } ) ] ^ { - 1 } F ( { \bf x } ( 0 ) ) = 0 . 2 5 \left[ \begin{array} { c c c } { { 3 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { - 1 6 . 2 } } & { { 1 } } \\ { { 0 } } & { { 0 } } & { { 2 0 } } \end{array} \right] ^ { - 1 } \left[ \begin{array} { c } { { - 1 . 5 } } \\ { { 0 . 2 5 } } \\ { { 1 0 \pi / 3 } } \end{array} \right]
$$

= (0.125,-0.004222203325,--0.1308996939)';

k $\tiny  \begin{array} { l } { \displaystyle { \mathrm { ~  ~ \psi ~ } _ { 2 } = h [ - J ( 0 . 0 6 2 5 , - 0 . 0 0 2 1 1 1 1 0 1 6 6 3 , - 0 . 0 6 5 4 4 9 8 4 6 9 5 ) ] ^ { - 1 } ( - 1 . 5 , 0 . 2 5 , 1 0 \pi / 3 ) ^ { t } } \end{array} }$   
$\begin{array} { r l } & { \kappa _ { 2 }                  \ r {  \ r {  \ r {  \ r {  \ r { \operatorname* { \Theta } } } } } } , } \\ & { \quad = 0 . 2 5 [ \begin{array} { c c c } { 3 } & { - 0 . 9 0 4 3 2 8 9 1 4 9 \times 1 0 ^ { - 5 } } & { - 0 . 2 9 1 6 9 3 6 1 9 6 \times 1 0 ^ { - 6 } } \\ { 0 . 1 2 5 } & { - 1 . 5 8 5 8 0 0 1 5 3 } & { 0 . 9 9 7 8 5 8 9 2 3 2 } \\ { 0 . 0 0 2 1 1 1 3 8 0 2 2 9 } & { - 0 . 0 6 2 5 0 8 2 4 7 0 6 } & { 2 0 } \end{array} ] ^ { - 1 } [ \begin{array} { l } { - 0 . 1 5 7 2 3 5 1 4 9 8 5 7 6 8 7 7 6 } \\ { 0 . 1 0 5 8 5 4 8 7 5 7 7 6 } \\ { 1 0 . 0 5 8 5 8 5 4 8 1 9 6 \times 1 0 ^ { - 6 } } \\ { 0 . 9 9 7 8 5 8 9 2 3 2 } \\ { 1 0 . 0 0 2 1 1 1 3 8 0 2 2 9 } \end{array} ] ^ { - 1 } [ \begin{array} { l } { - 0 . 1 5 7 2 3 5 1 4 9 8 5 7 6 } \\ { 0 . 1 0 5 8 5 4 8 1 5 0 8 2 5 2 5 } \\ { 0 . 1 0 5 8 5 4 8 1 5 0 8 2 5 2 5 } \\ { 1 0 . 0 0 2 1 1 3 1 2 5 1 } \end{array} ] ^ { - 1 } = [ \begin{array} { l } { - 0 . 1 8 5 2 3 5 1 4 9 8 5 1 2 0 8 5 1 0 8 5 } \\ { 0 . 1 4 8 5 3 0 8 5 2 5 4 2 0 } \\ { 0 . 0 2 1 4 8 5 3 0 2 5 2 5 } \\ { 0 . 0 0 2 1 1 2 5 1 } \end{array} ] ^ { - 1 } = [ \begin{array} { l } { 0 . 1 8 5 2 3 5 0 8 7 6 8 7 5 } \\ { 0 . 0 2 4 8 5 1 4 0 8 5 2 5 } \\ { 0 . 0 2 4 8 5 0 8 2 4 7 0 6 } \\ { 0 . 0 2 4 8 5 4 8 5 2 5 } \end{array} ] } \end{array}$ -1.5 0.25 π/3] = (0.1249999773,-0.003311761993,-0.1309232406);   
$\mathbf { k } _ { 3 } = h [ - J ( 0 . 0 6 2 4 9 9 9 8 8 6 5 , - 0 . 0 0 1 6 5 5 8 8 0 9 9 7 , - 0 . 0 6 5 4 6 1 6 2 0 3 ) ] ^ { - 1 } ( - 1 . 5 , 0 . 2 5 , 0 . 2 5 , 0 , 0 . 3 2 , 0 , 0 . 5 )$ 10π /3)t = (0.1249999844，-0.003296244825，-0.130920346);   
k4 = h[-J(0.1249999844,-0.003296244825,-0.130920346)]-1(-1.5,0.25,10π /3)t = (0.1249998945，-0.00230206762，-0.1309346977);

and

$$
\begin{array} { l } { { \displaystyle { \bf x } ( \lambda _ { 1 } ) = { \bf w } _ { 1 } = { \bf w } _ { 0 } + \frac { 1 } { 6 } [ { \bf k } _ { 1 } + 2 { \bf k } _ { 2 } + 2 { \bf k } _ { 3 } + { \bf k } _ { 4 } ] } \ ~ } \\ { { \displaystyle ~ = ( 0 . 1 2 4 9 9 9 6 9 7 , - 0 . 0 0 3 2 9 0 0 4 7 4 3 , - 0 . 1 3 0 9 2 0 2 6 0 8 ) ^ { t } } . } \end{array}
$$

Continuing, we have

$$
\begin{array} { r l } & { \mathbf { x } ( \lambda _ { 2 } ) = \mathbf { w } _ { 2 } = ( 0 . 2 4 9 9 9 9 7 6 7 9 , - 0 . 0 0 4 5 0 7 4 0 0 1 2 8 , - 0 . 2 6 1 8 5 5 7 6 1 9 ) ^ { t } , } \\ & { \mathbf { x } ( \lambda _ { 3 } ) = \mathbf { w } _ { 3 } = ( 0 . 3 7 4 9 9 9 6 9 5 6 , - 0 . 0 0 3 4 3 0 3 5 2 1 0 3 , - 0 . 3 9 2 7 6 3 4 4 2 3 ) ^ { t } , } \end{array}
$$

and

$$
\mathbf { x } ( \lambda _ { 4 } ) = \mathbf { x } ( 1 ) = \mathbf { w } _ { 4 } = ( 0 . 4 9 9 9 9 9 9 5 4 , 0 . 1 2 6 7 8 2 \times 1 0 ^ { - 7 } , - 0 . 5 2 3 5 9 8 7 7 5 8 ) ^ { t } .
$$

The results obtained here are very accurate, since the actual solution is approximately $( 0 . 5 , 0 , - 0 . 5 2 3 5 9 8 7 7 ) ^ { t }$

In the Runge-Kutta method of order four, the calculation of each $\mathbf { w } _ { j }$ requires four matrix inversions, one each when computing $\mathbf { k } _ { 1 }$ ${ \mathbf { \mathbf { \mathbf { 1 } } } } , { \mathbf { \mathbf { \mathbf { k } } } } _ { 2 } , { \mathbf { \mathbf { \mathbf { k } } } } _ { 3 }$ ,and $\mathbf { k } _ { 4 }$ . Thus,using $N$ steps requires 4N matrix inversions.By comparison, Newton's method requires one matrix inversion per iteration. Therefore, the work involved for the Runge-Kuta method is roughly equivalent to 4N iterations of Newton's method.

An alternative is to use a Runge-Kutta method of order two, such as the modified Euler method or even Euler's method, to decrease the number of inversions. Another possibility is to use smaller values of $N$ . The following example illustrates these ideas.

Table 10.6 summarizes a comparison of Euler's method, the Midpoint method, and the Runge-Kutta method of order four applied to the problem in Example 2 with initial approximation $\mathbf { x } ( 0 ) = ( 0 , 0 , 0 ) ^ { t }$ ·

The continuation method can be used as a stand-alone method not requiring a particularly good choice of ${ \bf x } ( 0 )$ . However, the method can also be used to give an initial approximation for Newton's or Broyden's method. For example, the result obtained in Example 2 using Euler's method and $N = 2$ might easily be sufficient to start the more efficient Newton's or Broyden's methods and be better for this purpose than the continuation methods, which require more calculation.

Table 10.6   

<table><tr><td>Method</td><td>N</td><td>x(1)</td><td>Number of Inversions</td></tr><tr><td>Euler</td><td>1</td><td>(0.5,-0.0168888133, -0.5235987755)&#x27;</td><td>1</td></tr><tr><td>Euler</td><td>4</td><td>(0.499999379,-0.004309160698,-0.523679652)t</td><td>4</td></tr><tr><td>Midpoint</td><td>1</td><td>(0.4999966628, -0.00040240435, -0.523815371)</td><td>2</td></tr><tr><td>Midpoint</td><td>4</td><td>(0.500000066,-0.00001760089,-0.5236127761)t</td><td>8</td></tr><tr><td>Runge-Kutta</td><td>1</td><td>(0.4999989843,-0.1676151 × 10-5, -0.5235989561)t</td><td>4</td></tr><tr><td>Runge-Kutta</td><td>4</td><td>(0.4999999954,0.126782 × 10-7, --0.5235987758)</td><td>16</td></tr></table>

We note that in the Runge-Kutta methods, the steps similar to

$$
\mathbf { k } _ { i } = h [ - J ( \mathbf { x } ( \lambda _ { i } ) + \alpha _ { i - 1 } \mathbf { k } _ { i - 1 } ) ] ^ { - 1 } \mathbf { F } ( \mathbf { x } ( 0 ) )
$$

can be written as solving the linear system

$$
J \left( \mathbf { x } ( \lambda _ { i } ) + \alpha _ { i - 1 } \mathbf { k } _ { i - 1 } \right) \mathbf { k } _ { i } = - h \mathbf { F } ( \mathbf { x } ( 0 ) ) ,
$$

for $\mathbf { k } _ { i }$

# Continuation Algorithm

To approximate the solution of the nonlinear system $\mathbf { F } ( \mathbf { x } ) = \mathbf { 0 }$ given an initial approximation x:

INPUT number $\pmb { n }$ of equations and unknowns; integer $N \ > \ 0$ ； initial approximation $\mathbf { x } = ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } ) ^ { t }$

OUTPUT approximate solution $\mathbf { x } = ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } ) ^ { t }$

Step1 Set $\begin{array} { l } { { \displaystyle h = 1 / N ; } } \\ { { \displaystyle { \bf b } = - h { \bf F } ( { \bf x } ) . } } \end{array}$

Step2 For $i = 1 , 2 , \dots , N$ do Steps 3-7.

Step 3 Set $A = J ( \mathbf { x } )$ ； Solve the linear system $A \mathbf { k } _ { 1 } = \mathbf { b }$   
Step 4 Set $\begin{array} { r } { A = J ( \mathbf { x } + \frac { 1 } { 2 } \mathbf { k } _ { 1 } ) } \end{array}$ ； Solve the linear system $A { \bf k } _ { 2 } = { \bf b }$   
Step 5Set $\begin{array} { r } { { \cal A } = { \cal J } ( { \bf x } + \frac { 1 } { 2 } { \bf k } _ { 2 } ) } \end{array}$ ； ·Solve the linear system $A \mathbf { k } _ { 3 } = \mathbf { b }$   
Step 6 Set $A = J ( \mathbf { x } + \mathbf { k } _ { 3 } )$ ； Solve the linear system $A \mathbf { k } _ { 3 } = \mathbf { b }$

Step 8OUTPUT $( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } )$ ； STOP.

# ExErcisE SEt 10.5

1. The nonlinear system

$$
\begin{array} { l } { { f _ { 1 } ( x _ { 1 } , x _ { 2 } ) = x _ { 1 } ^ { 2 } - x _ { 2 } ^ { 2 } + 2 x _ { 2 } = 0 , } } \\ { { \nonumber } } \\ { { f _ { 2 } ( x _ { 1 } , x _ { 2 } ) = 2 x _ { 1 } + x _ { 2 } ^ { 2 } - 6 = 0 } } \end{array}
$$

has two solutions, (0.625204094,2.179355825)' and (2.109511920,-1.334532188)r. Use the continuation method and Euler's method with $N = 2$ to approximate the solutions where

a. $\mathbf { x } ( 0 ) = ( 0 , 0 ) ^ { t }$ $\begin{array} { r } { 0 ) ^ { t } \qquad \mathbf { b } _ { } * { } \qquad \mathbf { x } ( 0 ) = ( 1 , 1 ) ^ { t } \qquad \mathbf { c } _ { } * { } \quad \mathbf { x } ( 0 ) = ( 3 , - 2 ) ^ { t } } \end{array}$

2.Repeat Exercise 1 using the Runge-Kutt method of order four with $N = 1$ ·

3. Use the continuation method and Euler's method with $N = 2$ on the following nonlinear systems.

a. $\begin{array} { l } { { \displaystyle 4 x _ { 1 } ^ { 2 } - 2 0 x _ { 1 } + \frac { 1 } { 4 } x _ { 2 } ^ { 2 } + 8 = 0 , \qquad \mathrm { ~ b . ~ } \qquad \sin ( 4 \pi x _ { 1 } x _ { 2 } ) - 2 x _ { 2 } - x _ { 1 } = 0 , } } \\ { { \displaystyle \frac { 1 } { 2 } x _ { 1 } x _ { 2 } ^ { 2 } + 2 x _ { 1 } - 5 x _ { 2 } + 8 = 0 . \qquad \left( \frac { 4 \pi - 1 } { 4 \pi } \right) ( e ^ { 2 x _ { 1 } } - e ) + 4 e x _ { 2 } ^ { 2 } - 2 e x _ { 1 } = 0 . } } \end{array}$ c. $\begin{array} { r l r } { { 3 } x _ { 1 } - \cos ( x _ { 2 } x _ { 3 } ) - \displaystyle \frac { 1 } { 2 } = 0 , } & { \qquad } & { \mathbf { d } , \qquad x _ { 1 } ^ { 2 } + x _ { 2 } - 3 7 = 0 , } \\ { 4 x _ { 1 } ^ { 2 } - 6 2 5 x _ { 2 } ^ { 2 } + 2 x _ { 2 } - 1 = 0 , } & { \qquad } & { x _ { 1 } - x _ { 2 } ^ { 2 } - 5 = 0 , } \\ { e ^ { - x _ { 1 } x _ { 2 } } + 2 0 x _ { 3 } + \displaystyle \frac { 1 0 \pi - 3 } { 3 } = 0 . } & { } & \end{array}$

4. Use the continuation method and the Runge-Kutta method of order four with $N . = 1$ on Exercise 4 of Section 10.2 using $\mathbf { x } ( 0 ) = \mathbf { 0 }$ . Are the answers here comparable to the results of Exercise 4 of Section 10.2,or are they suitable initial approximations for Newton's method?

;.Repeat Exercise 4 using the initial approximation obtained in Exercise 2 of Section 10.2.

6. Use the continuation method and the Runge-Kutta method of order four with $N = 1$ on Exercise 3 of Section 10.2. Are the results as good as those obtained.there?

7. Repeat Exercise 5using $N = 2$

8.Repeat Exercise 6of Section 10.2 using the continuation method and the Runge-Kutta method of order four with $N = 1$

9. Repeat Exercise 5of Section 10.2 using the continuation method and the Runge-Kuta method of order four with $N = 2$

l0.Show that the continuation method and Euler's method with $N = 1$ gives the same result as Newton's method for the first iteration; that is, with $\mathbf { x } ( 0 ) = \mathbf { x } ^ { ( 0 ) }$ we always obtain $\mathbf { x } ( 1 ) = \mathbf { x } ^ { ( 1 ) }$ ，

11.Show that the homotopy

$$
G ( \lambda , \mathbf { x } ) = F ( \mathbf { x } ) - e ^ { - \lambda } F ( \mathbf { x } ( 0 ) )
$$

used in the continuation method with Euler's method and $h \ = \ 1$ also duplicates Newton's method for any $\mathbf { x } ^ { ( 0 ) }$ ; that is, with $\mathbf { x } ( 0 ) = \mathbf { x } ^ { ( 0 ) }$ , we have $\mathbf { x } ( 1 ) = \mathbf { x } ^ { ( 1 ) }$

12.Let the continuation method with the Runge-Kuta method of order four be abbreviated CMRK4. After completing Exercises 4, 5,6,7, 8, and 9,answer the following questions.

a. Is CMRK4 with $N = 1$ comparable to Newton's method? Support your answer with the results of earlier exercises.   
b. Should CMRK4 with $N = 1$ be used as a means to obtain an initial approximation for Newton's method? Support your answer with the results of earlier exercises.   
c. Repeat part (a) for CMRK4 with $N = 2$   
d. Repeat part (b) for CMRK4 with $N = 2$

# 10.6 Survey of Methods and Software

In this chapter we considered methods to approximate solutions to nonlinear systems

$$
\begin{array} { r } { f _ { 1 } ( x _ { 1 } , x _ { 2 } , \dots , x _ { n } ) = 0 , } \\ { f _ { 2 } ( x _ { 1 } , x _ { 2 } , \dots , x _ { n } ) = 0 , } \end{array}
$$

$$
f _ { n } ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } ) = 0 .
$$

Newton's methodforsystemsrequiresa good initial approximation $( x _ { 1 } ^ { ( 0 ) } , x _ { 2 } ^ { ( 0 ) } , \ldots , . . . ) ^ { t }$ and generates a sequence

$$
\mathbf { x } ^ { ( k ) } = \mathbf { x } ^ { ( k - 1 ) } - J ( \mathbf { x } ^ { ( k - 1 ) } ) ^ { - 1 } \mathbf { F } ( \mathbf { x } ^ { ( k - 1 ) } ) ,
$$

that converges rapidly to a solution $\mathbf { x }$ if $\mathbf { x } ^ { ( 0 ) }$ is sufficiently close to p. However, Newton's method requires evaluating, or approximating, $n ^ { 2 }$ partial derivatives and solving an $n$ by $n$ linear system at each step, which requires $O ( n ^ { 3 } )$ computations.

Broyden's method reduces the amount of computation at each step without significantly degrading the speed of convergence. This technique replaces the Jacobian matrix $J$ with a matrix $A _ { k - 1 }$ whose inverse is directly determined at each step. This reduces the arithmetic computations from $O ( n ^ { 3 } )$ to $O ( n ^ { 2 } )$ . Moreover, the only scalar function evaluations required are in evaluating the $f _ { i }$ ,saving $n ^ { 2 }$ scalar function evaluations per step. Broyden's method also requires a good initial approximation.

The Steepest Descent method was presented as a way to obtain good initial approximations for Newton's and Broyden's methods. Although Steepest Descent does not give a rapidly convergent sequence,it does not require a good initial approximation. The Steepest Descent method approximates a minimum of a multivariable function $g$ . For our application we choose

$$
g ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } ) = \sum _ { i = 1 } ^ { n } [ f _ { i } ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } ) ] ^ { 2 } .
$$

The minimum value of $g$ is O, which occurs when the functions $f _ { i }$ are simultaneously 0.

Homotopy and continuation methods are also used for nonlinear systems and are the subject of current research (see [AG]). In these methods,a given problem

$$
\mathbf { F } ( \mathbf { x } ) = \mathbf { 0 }
$$

is embedded in a one-parameter family of problems using a parameter $\lambda$ that assumes values in [0,1]. The original problem corresponds to $\lambda = 1$ , and a problem with a known solution corresponds to $\lambda = 0$ . For example, the set of problems

$$
G ( \lambda , \mathbf { x } ) = \lambda \mathbf { F } ( \mathbf { x } ) + ( 1 - \lambda ) ( \mathbf { F } ( \mathbf { x } ) - \mathbf { F } ( \mathbf { x } _ { 0 } ) ) = \mathbf { 0 } , \quad \mathrm { f o r } 0 \leq \lambda \leq 1 ,
$$

with fixed $\mathbf { x } _ { 0 } ~ \in ~ \mathbb { R } ^ { n }$ forms a homotopy.When $\lambda = 0$ , the solution is ${ \bf x } ( \lambda = 0 ) = { \bf x } _ { 0 }$ The solution to the original problem corresponds to $\mathbf { x } ( \lambda = 1 )$ . A continuation method attempts to determine $\mathbf { x } ( \lambda = 1 )$ by solving the sequence of problems corresponding to $\lambda _ { 0 } = 0 < \lambda _ { 1 } < \lambda _ { 2 } < \dots < \lambda _ { m } = 1$ . The initial approximation to the solution of

$$
\lambda _ { i } \mathbf { F } ( \mathbf { x } ) + ( 1 - \lambda _ { i } ) ( \mathbf { F } ( \mathbf { x } ) - \mathbf { F } ( \mathbf { x _ { 0 } } ) ) = \mathbf { 0 }
$$

would be the solution, $\mathbf { x } ( \lambda = \lambda _ { i - 1 } )$ , to the problem

$$
\lambda _ { i - 1 } \mathbf { F } ( \mathbf { x } ) + ( 1 - \lambda _ { i - 1 } ) ( \mathbf { F } ( \mathbf { x } ) - \mathbf { F } ( \mathbf { x } _ { 0 } ) ) = \mathbf { 0 } .
$$

The package Hompack in Netlib solves a system of nonlinear equations by using various 1omotopy methods.

The nonlinear systems methods in the IMSL and NAG libraries are based on two subroutines, HYBRD and HYBRJ, contained in MINPACK,a public-domain package. Both methods use the Levenberg-Marquardt method, which is a weighted average of Newton's method and the Steepest Descent method.The weight is biased toward the Steepest Descent method until convergence is detected, at which time the weight is shifted toward the more rapidly convergent Newton's method. The subroutine HYBRD uses a finite-difference ap-proximation to the Jacobian, and HYBRJ requires a user-supplied subroutine to compute the Jacobian.

The IMSL subroutine NEQNF solves a nonlinear system without a user-supplied Jacobian. The subroutine NEQNJ is similar to NEQNF, except that the user must supply a subroutine to calculate the Jacobian.

In the NAG library, C05NBF is similar to HYBRD.The subroutine CO5PBF is similar to CO5NBF, except that the user must supply a subroutine to compute the Jacobian. The subroutine CO5PBF is based on HYBRJ in the MINPACK package.NAG also contains other modifications of the Levenberg-Marquardt method.

A comprehensive treatment of methods for solving nonlinear systems of equations can be found in Ortega and Rheinbolt [OR] and in Dennis and Schnabel [DenS]. Recent developments on iterative methods can be found in Argyros and Szidarovszky [AS],and information on the use of continuation methods is available in Allgower and Georg [AG].

CHAPTER

#

# Boundary-Value Problems for Ordinary Differential Equations

A beam of rectangular cross section subject to uniform loading while the ends of the beam are supported so that they undergo no deflection.

![](images/d18d5fdc55ccfd02cec12df03fd89ba02058f76ce9a10b739f3e4256b3ac7b2a.jpg)

The differential equation approximating the physical situation is of the form

$$
\frac { d ^ { 2 } w } { d x ^ { 2 } } ( x ) = \frac { S } { E I } w ( x ) + \frac { q x } { 2 E I } ( x - l ) ,
$$

where $\ w ( x )$ is the deflection a distance $\pmb { x }$ from the left end of the beam, and l $, q , E , S ,$ and $\pmb { I }$ represent, respectively, the length of the beam, the intensity of the uniform load, the modulus of elasticity, the stress at the endpoints, and the central moment of inertia. Since no deflection occurs at the ends.of the beam, we also have the two boundary conditions

$$
w ( 0 ) = w ( l ) = 0 .
$$

![](images/44a632bc353eb94e6b60986682c44fa2e644fbaa26de13ad0dc7fcd1cf9b31ff.jpg)

When the beam is of uniform thickness, the product EI is constant, and the exact solution is easily obtained. When the thickness is not uniform, the moment of inertia I is a function of x, and approximation techniques are required. Problems of this type are considered in Exercises 7 of Section 11.3 and 6 of Section 11.4.

The differential equations in Chapter 5 are of first order and have one initial condi-tion to satisfy.Later in the chapter we saw that the techniques could be extended to systems of equations and then to higher-order equations,but all the specified conditions are on the same endpoint. These are initial-value problems.In this chapter we show how to approximate the solution to boundary-value problems, differential equations with conditions imposed at different points. For first-order differential equations,only one condition is specified, so there is no distinction between initial-value and boundary-value problems. We will be considering second-order equations with two boundary values.

Physical problems that are position-dependent rather than time-dependent are often described in terms of differential equations with conditions imposed at more than one point. The two-point boundary-value problems in this chapter involve a second-order differential equation of the form

$$
y ^ { \prime \prime } = f ( x , y , y ^ { \prime } ) , \quad a \leq x \leq b ,
$$

together with the boundary conditions

$$
y ( a ) = \alpha \quad { \mathrm { a n d } } \quad y ( b ) = \beta .
$$

# 11.1 The Linear Shooting Method

The following theorem gives general conditions that ensure that the solution to a secondorder boundary value problem exists and is unique. The proof of this theorem can be found in [Keller, H].

# Theorem 11.1

Suppose the function $f$ in the boundary-value problem

$$
y ^ { \prime \prime } = f ( x , y , y ^ { \prime } ) , \quad a \leq x \leq b , \quad y ( a ) = \alpha , \quad y ( b ) = \beta ,
$$

is continuous on the set

$$
D = \{ ( x , y , y ^ { \prime } ) ~ | ~ a \leq x \leq b , - \infty < y < \infty , - \infty < y ^ { \prime } < \infty \} ,
$$

and that the partial derivatives $f _ { y }$ and $f _ { y ^ { \prime } }$ are also continuous on $D$ . If

i） $f _ { y } ( x , y , y ^ { \prime } ) > 0$ ,for all $( x , y , y ^ { \prime } ) \in D$ ,and (ii) a constant $M$ exists, with

$$
\left| f _ { y ^ { \prime } } ( x , y , y ^ { \prime } ) \right| \leq M , \quad { \mathrm { ~ f o r ~ a l l ~ } } ( x , y , y ^ { \prime } ) \in D ,
$$

then the boundary-value problem has a unique solution.

# EXAMPLE 1

The boundary-value problem

$$
y ^ { \prime \prime } + e ^ { - x y } + \sin y ^ { \prime } = 0 , \quad 1 \leq x \leq 2 , \quad y ( 1 ) = y ( 2 ) = 0 ,
$$

has

$$
f ( x , y , y ^ { \prime } ) = - e ^ { - x y } - \sin y ^ { \prime } .
$$

Since

$$
f _ { y } ( x , y , y ^ { \prime } ) = x e ^ { - x y } > 0 \quad \mathrm { a n d } \quad \left| f _ { y ^ { \prime } } ( x , y , y ^ { \prime } ) \right| = | - \cos y ^ { \prime } | \leq 1 ,
$$

this problem has a unique solution.

When $f ( x , y , y ^ { \prime } )$ has the form

$$
\begin{array} { r } { f ( x , y , y ^ { \prime } ) = p ( x ) y ^ { \prime } + q ( x ) y + r ( x ) , } \end{array}
$$

the differential equation

$$
y ^ { \prime \prime } = f ( x , y , y ^ { \prime } )
$$

is linear. Problems of this type frequently occur,and in this situation, Theorem 11.1 can be simplified.

# Corollary 11.2

If the linear boundary-value problem

$$
y ^ { \prime \prime } = p ( x ) y ^ { \prime } + q ( x ) y + r ( x ) , \quad a \leq x \leq b , \quad y ( a ) = \alpha , \quad y ( b ) = \beta ,
$$

satisfies

(i $p ( x ) , q ( x )$ ,and $r ( x )$ are continuous on $[ a , b ]$ ，(ii） $q ( x ) > 0 \mathrm { o n } [ a , b ] ,$

then the problem has a unique solution.

To approximate the unique solution guaranteed by the satisfaction of the hypotheses of Corollary 11.2,let us first consider the initial-value problems

$$
y ^ { \prime \prime } = p ( x ) y ^ { \prime } + q ( x ) y + r ( x ) , \quad a \leq x \leq b , \quad y ( a ) = \alpha , \quad y ^ { \prime } ( a ) = 0 ,
$$

and

$$
y ^ { \prime \prime } = p ( x ) y ^ { \prime } + q ( x ) y , \quad a \leq x \leq b , \quad y ( a ) = 0 , \quad y ^ { \prime } ( a ) = 1 .
$$

Theorem 5.16 in Section 5.9 ensures that under the hypotheses in Corollary 11.2,both problems have a unique solution. Let $y _ { 1 } ( x )$ denote the solution to (11.3), $y _ { 2 } ( x )$ denote the solution to (11.4), and let

$$
y ( x ) = y _ { 1 } ( x ) + { \frac { \beta - y _ { 1 } ( b ) } { y _ { 2 } ( b ) } } y _ { 2 } ( x ) .
$$

Then

$$
y ^ { \prime } ( x ) = y _ { 1 } ^ { \prime } ( x ) + { \frac { \beta - y _ { 1 } ( b ) } { y _ { 2 } ( b ) } } y _ { 2 } ^ { \prime } ( x )
$$

and

$$
y ^ { \prime \prime } ( x ) = y _ { 1 } ^ { \prime \prime } ( x ) + { \frac { \beta - y _ { 1 } ( b ) } { y _ { 2 } ( b ) } } y _ { 2 } ^ { \prime \prime } ( x ) .
$$

So

$$
\begin{array} { l } { { \displaystyle y ^ { \prime \prime } = p ( x ) y _ { 1 } ^ { \prime } + q ( x ) y _ { 1 } + r ( x ) + \frac { \beta - y _ { 1 } ( b ) } { y _ { 2 } ( b ) } \left( p ( x ) y _ { 2 } ^ { \prime } + q ( x ) y _ { 2 } \right) } } \\ { { \displaystyle \quad = p ( x ) \left( y _ { 1 } ^ { \prime } + \frac { \beta - y _ { 1 } ( b ) } { y _ { 2 } ( b ) } y _ { 2 } ^ { \prime } \right) + q ( x ) \left( y _ { 1 } + \frac { \beta - y _ { 1 } ( b ) } { y _ { 2 } ( b ) } y _ { 2 } \right) + r ( x ) } } \\ { { \displaystyle \quad = p ( x ) y ^ { \prime } ( x ) + q ( x ) y ( x ) + r ( x ) } . } \end{array}
$$

Moreover,

$$
y ( a ) = y _ { 1 } ( a ) + { \frac { \beta - y _ { 1 } ( b ) } { y _ { 2 } ( b ) } } y _ { 2 } ( a ) = \alpha + { \frac { \beta - y _ { 1 } ( b ) } { y _ { 2 } ( b ) } } \cdot 0 = \alpha
$$

and

$$
y ( b ) = y _ { 1 } ( b ) + \frac { \beta - y _ { 1 } ( b ) } { y _ { 2 } ( b ) } y _ { 2 } ( b ) = y _ { 1 } ( b ) + \beta - y _ { 1 } ( b ) = \beta .
$$

Hence, $y ( x )$ is the unique solution to the linear boundary-value problem, provided, of course, that $y _ { 2 } ( b ) \neq 0$ .(That $y _ { 2 } ( b ) = 0$ is in conflict with the hypotheses of Corollary 11.2 is considered in Exercise 8.)

The Shooting method for linear equations is based on the replacement of the linear boundary-value problem by the two initial-value problems (11.3） and (11.4). Numerous methods are available from Chapter 5 for approximating the solutions $y _ { \mathrm { l } } \left( x \right)$ and $y _ { 2 } ( x )$ ， and once these approximations are available, the solution to the boundary-value problem is approximated using Eq. (11.5). Graphically, the method has the appearance shown in Figure 11.1.

![](images/558bbd24ce269818eb65211013bf61e2fe3ec5cd6416c6c1189911fa33e01697.jpg)  
Figure 11.1

Algorithm 11.1 uses the fourth-order Runge-Kutta technique to find the approximations to $y _ { 1 } ( x )$ and $y _ { 2 } ( x )$ , but another technique for approximating the solutions to initialvalue problems can be substituted into Step 4.

The algorithm has the additional feature of obtaining approximations for the derivative of the solution to the boundary-value problem as well as to the solution of the problem itself.The use of the algorithm is not restricted to those problems for which the hypotheses of Corollary 11.2 can be verified; it will work for many problems that do not satisfy these hypotheses.

# Linear Shooting

To approximate the solution of the boundary-value problem

$$
\begin{array} { r } { - y ^ { \prime \prime } + p ( x ) y ^ { \prime } + q ( x ) y + r ( x ) = 0 , \quad a \leq x \leq b , \quad y ( a ) = \alpha , \quad y ( b ) = \beta : } \end{array}
$$

(Note: Equations (11.3) and (11.4) are written as first-order systems and solved.)

INPUTendpoints $a , b$ ; boundary conditions $\alpha , \beta$ ; number of subintervals $N$

OUTPUTapproximations $w _ { 1 , i }$ to $y ( x _ { i } ) ; w _ { 2 , i }$ to $y ^ { \prime } ( x _ { i } )$ for each $i = 0 , 1 , \ldots , N$

Step 1 Set $h = ( b - a ) / N$ $\begin{array} { r } { u _ { 1 , 0 } = \alpha ; } \\ { u _ { 2 , 0 } = 0 ; } \\ { v _ { 1 , 0 } = 0 ; } \\ { v _ { 2 , 0 } = 1 . } \end{array}$

Step 2 For $i = 0 , \ldots , N - 1$ do Steps 3 and 4. (The Runge-Kutta method for systems is used in Steps 3 and 4.)

Step 3Set $x = a + i h$

Step 4 Set $k _ { 1 , 1 } = h u _ { 2 , i }$ ；

$$
\begin{array} { r l } & { k _ { 1 , 2 } = h ( p ( \lambda ) u _ { \lambda } , e _ { \lambda } + q ( \lambda ) \lambda \nu _ { \lambda , i } + q ( \lambda ) \lambda \nu _ { \lambda , i } ) ; } \\ & { k _ { 2 , 1 } = h [ k _ { 1 } z _ { 1 } + \frac { 1 } { 2 } k _ { 1 } z _ { 1 } ] ; } \\ & { k _ { 2 , 2 } = h [ p ( \lambda ) e _ { \lambda } + b ( \lambda / 2 ) ( z _ { 1 } + \frac { 1 } { 2 } k _ { 1 } z _ { 1 } ) ] } \\ & { \qquad + q ( \lambda - h / 2 ) ( k _ { 1 } z _ { 1 } + \frac { 1 } { 2 } k _ { 1 } z _ { 1 } ) + \nu ( \lambda + h / 2 ) \lambda \nu _ { \lambda } } \\ & { k _ { 1 , 1 } = h [ a _ { \lambda } , i + \frac { 1 } { 2 } k _ { 2 } z _ { 1 } ] ; } \\ & { k _ { 2 , 2 } = h [ p ( \lambda + h / 2 ) ( z _ { 1 } + \frac { 1 } { 2 } k _ { 2 } z _ { 2 } )  } \\ & { \qquad + q ( \lambda + h / 2 ) ( z _ { 1 } + \frac { 1 } { 2 } k _ { 2 } z _ { 1 } )  + \nu ( \lambda + h / 2 ) \lambda \nu _ { \lambda } } \\ & { \qquad \lambda + \mu [ z _ { 1 } + h / 2 ] ( z _ { 1 } + k _ { 2 } z _ { 1 } ) ] ; } \\ & { k _ { 3 , 1 } = h [ p ( \lambda + h / 2 ) ( z _ { 1 } + k _ { 3 } z _ { 2 } ) + q ( \lambda + h ) ( a _ { 1 , i } + k _ { 3 } z _ { 1 } ) - r ( \lambda + h / 2 ) \nu _ { \lambda } ] } \\ & {  + a _ { \lambda } - \lambda e _ { \lambda } + \frac { 1 } { 2 } [ k _ { 1 } z _ { 1 } + 2 k _ { 2 } z _ { 1 } - 2 k _ { 3 } z _ { 1 } + k _ { 4 } z _ { 1 } ] ; } \\ & {  a _ { 2 , 2 1 } = a _ { 2 , 2 } + \frac { 1 } { \mu } [ k _ { 1 } z _ { 2 } + 2 k _ { 2 } z _ { 2 } + 2 k _ { 3 } z _ { 1 } + k _ { 4 } z _ { 1 } ] ; } \\ &  k _ { 1 , 1 } = h [ a _ { \lambda } , i + \frac { 1 }  \end{array}
$$

$$
\begin{array} { r l } & { k _ { 1 , 2 } ^ { \prime } = h \left[ p ( x ) v _ { 2 , i } + q ( x ) v _ { 1 , i } \right] ; } \\ & { k _ { 2 , 1 } ^ { \prime } = h \left[ v _ { 2 , i } + \frac { 1 } { 2 } k _ { 1 , 2 } ^ { \prime } \right] ; } \\ & { k _ { 2 , 2 } ^ { \prime } = h \left[ p ( x + h / 2 ) \left( v _ { 2 , i } + \frac { 1 } { 2 } k _ { 1 , 2 } ^ { \prime } \right) + q ( x + h / 2 ) \left( v _ { 1 , i } + \frac { 1 } { 2 } k _ { 1 , 1 } ^ { \prime } \right) \right] ; } \\ & { k _ { 3 , 1 } ^ { \prime } = h \left[ v _ { 2 , i } + \frac { 1 } { 2 } k _ { 2 , 2 } ^ { \prime } \right] ; } \\ & { k _ { 3 , 2 } ^ { \prime } = h \left[ p ( x + h / 2 ) \left( v _ { 2 , i } + \frac { 1 } { 2 } k _ { 2 , 2 } ^ { \prime } \right) + q ( x + h / 2 ) \left( v _ { 1 , i } + \frac { 1 } { 2 } k _ { 2 , 1 } ^ { \prime } \right) \right] ; } \\ & { k _ { 4 , 1 } ^ { \prime } = h \left[ v _ { 2 , i } + k _ { 3 , 2 } ^ { \prime } \right] ; } \\ & { k _ { 4 , 2 } ^ { \prime } = h \left[ p ( x + h ) \left( v _ { 2 , i } + k _ { 3 , 2 } ^ { \prime } \right) + q ( x + h ) ( v _ { 1 , i } + k _ { 3 , 1 } ^ { \prime } ) \right] ; } \\ & { v _ { 1 , i + 1 } = v _ { 1 , i } + \frac { 1 } { 6 } \left[ k _ { 1 , 1 } ^ { \prime } + 2 k _ { 2 , 1 } ^ { \prime } + 2 k _ { 3 , 1 } ^ { \prime } + k _ { 4 , 1 } ^ { \prime } \right] ; } \\ & { v _ { 2 , i + 1 } = v _ { 2 , i } + \frac { 1 } { 6 } \left[ k _ { 1 , 2 } ^ { \prime } + 2 k _ { 2 , 2 } ^ { \prime } + 2 k _ { 3 , 2 } ^ { \prime } + k _ { 4 , 2 } ^ { \prime } \right] . } \end{array}
$$

Step 5 Set $w _ { 1 , 0 } = \alpha$ ； β-u1,N. W2.0 = V1,N OUTPUT $( a , w _ { 1 , 0 } , w _ { 2 , 0 } )$

$$
\begin{array} { r l } & { \mathrm { \cdot } \mathrm { t } \ W 1 = u _ { 1 , i } + w _ { 2 , 0 } v _ { 1 , i } ; } \\ & { \mathrm { \phantom { = } } W 2 = u _ { 2 , i } + w _ { 2 , 0 } v _ { 2 , i } ; } \\ & { \mathrm { \phantom { = } } x = a + i h ; } \\ & { \mathrm { \mathrm { U T P U T } } \left( x , W 1 , W 2 \right) . \quad ( O u t p u t i s x _ { i } , w _ { 1 , i } , w _ { 2 , i } . ) } \end{array}
$$

Step 7 STOP.(The process is complete.)

The boundary-value problem

$$
y ^ { \prime \prime } = - \frac { 2 } { x } y ^ { \prime } + \frac { 2 } { x ^ { 2 } } y + \frac { \sin ( \ln x ) } { x ^ { 2 } } , \quad 1 \leq x \leq 2 , \quad y ( 1 ) = 1 , \quad y ( 2 ) = 2 ,
$$

has the exact solution

$$
y = c _ { 1 } x + \frac { c _ { 2 } } { x ^ { 2 } } - \frac { 3 } { 1 0 } \sin ( \ln x ) - \frac { 1 } { 1 0 } \cos ( \ln x ) ,
$$

where

$$
c _ { 2 } = { \frac { 1 } { 7 0 } } [ 8 - 1 2 \sin ( \ln 2 ) - 4 \cos ( \ln 2 ) ] \approx - 0 . 0 3 9 2 0 7 0 1 3 2 0
$$

and

$$
c _ { 1 } = { \frac { 1 1 } { 1 0 } } - c _ { 2 } \approx 1 . 1 3 9 2 0 7 0 1 3 2 .
$$

Applying Algorithm 111 to this problem requires approximating the solutions to the initial-value problems

$$
y _ { 1 } ^ { \prime \prime } = - \frac { 2 } { x } y _ { 1 } ^ { \prime } + \frac { 2 } { x ^ { 2 } } y _ { 1 } + \frac { \sin ( \ln x ) } { x ^ { 2 } } , \quad 1 \leq x \leq 2 , \quad y _ { 1 } ( 1 ) = 1 , \quad y _ { 1 } ^ { \prime } ( 1 ) = 0 ,
$$

and

$$
y _ { 2 } ^ { \prime \prime } = - \frac { 2 } { x } y _ { 2 } ^ { \prime } + \frac { 2 } { x ^ { 2 } } y _ { 2 } , \quad 1 \leq x \leq 2 , \quad y _ { 2 } ( 1 ) = 0 , \quad y _ { 2 } ^ { \prime } ( 1 ) = 1 .
$$

The results of the calculations, using Algorithm 11.1 with $N = 1 0$ and $h = 0 . 1$ ,are given in Table 11.1. The value listed as $\boldsymbol { u } _ { 1 , i }$ approximates $y _ { \mathrm { I } } ( x _ { i } )$ , the value $v _ { 1 , i }$ approximates $y _ { 2 } ( x _ { i } )$ ,and $w _ { i }$ approximates

$$
y ( x _ { i } ) = y _ { 1 } ( x _ { i } ) + { \frac { 2 - y _ { 1 } ( 2 ) } { y _ { 2 } ( 2 ) } } y _ { 2 } ( x _ { i } ) .
$$

# Table 11.1

<table><tr><td>Xi</td><td>u1.i</td><td>V1.i</td><td>Wi</td><td>y(xi）</td><td>ly(xi）-wil</td></tr><tr><td>1.0</td><td>1.00000000</td><td>0.00000000</td><td>1.00000000</td><td>1.00000000</td><td></td></tr><tr><td>1.1</td><td>1.00896058</td><td>0.09117986</td><td>1.09262917</td><td>1.09262930</td><td>1.43 × 10-7</td></tr><tr><td>1.2</td><td>1.03245472</td><td>0.16851175</td><td>1.18708471</td><td>1.18708484</td><td>1.34 × 10-7</td></tr><tr><td>1.3</td><td>1.06674375</td><td>0.23608704</td><td>1.28338227</td><td>1.28338236</td><td>9.78 × 10-8</td></tr><tr><td>1.4</td><td>1.10928795</td><td>0.29659067</td><td>1.38144589</td><td>1.38144595</td><td>6.02×10-8</td></tr><tr><td>1.5</td><td>1.15830000</td><td>0.35184379</td><td>1.48115939</td><td>1.48115942</td><td>3.06 × 10-8</td></tr><tr><td>1.6</td><td>1.21248372</td><td>0.40311695</td><td>1.58239245</td><td>1.58239246</td><td>1.08× 10-8</td></tr><tr><td>1.7</td><td>1.27087454</td><td>0.45131840</td><td>1.68501396</td><td>1.68501396</td><td>5.43×10-10</td></tr><tr><td>1.8</td><td>1.33273851</td><td>0.49711137</td><td>1.78889854</td><td>1.78889853</td><td>5.05× 10-9</td></tr><tr><td>1.9</td><td>1.39750618</td><td>0.54098928</td><td>1.89392951</td><td>1.89392951</td><td>4.41 × 10-9</td></tr><tr><td>2.0</td><td>1.46472815</td><td>0.58332538</td><td>2.00000000</td><td>2.00000000</td><td></td></tr></table>

The accurate results in this example are due to the fact that the fourth-order Runge-Kutta method gives ${ \cal O } ( h ^ { 4 } )$ approximations to the solutions of the initial-value problems. Unfortunately, because of roundoff errors, there can be problems hidden in this technique. f $y _ { 1 } ( x )$ rapidly increases as $\pmb { x }$ goes from $a$ to $b$ ,then $u _ { 1 , N } \approx y _ { 1 } ( b )$ will be large. If $\beta$ is small in magnitude compared to ${ \pmb u } _ { 1 , N }$ , the term $w _ { 2 , 0 } = ( \beta - u _ { 1 , N } ) / v _ { 1 , N }$ will be approximately $- u _ { 1 , N } / v _ { 1 , N }$ . The computations in Step 6 then become

$$
\begin{array} { r l } & { W 1 = u _ { 1 , i } + w _ { 2 , 0 } v _ { 1 , i } \approx u _ { 1 , i } - \left( \frac { u _ { 1 , N } } { v _ { 1 , N } } \right) v _ { 1 , i } , } \\ & { } \\ & { W 2 = u _ { 2 , i } + w _ { 2 , 0 } v _ { 2 , i } \approx u _ { 2 , i } - \left( \frac { u _ { 1 , N } } { v _ { 1 , N } } \right) v _ { 2 , i } , } \end{array}
$$

which allows a possibility of a loss of significant digits due to cancellation. However, since $u _ { 1 , i }$ is an approximation to $y _ { 1 } ( x _ { i } )$ ,the behavior of $y _ { 1 }$ can easily be monitored,and if $u _ { 1 , i }$ increases rapidly from $a$ t0 $b$ , the shooting technique can be employed backward from $x _ { 0 } = b$ to $x _ { N } = a$ ; that is,solving instead the initial-value problems

$$
y ^ { \prime \prime } = p ( x ) y ^ { \prime } + q ( x ) y + r ( x ) , \quad a \leq x \leq b , \quad y ( b ) = \beta , \quad y ^ { \prime } ( b ) = 0 ,
$$

and

$$
y ^ { \prime \prime } = p ( x ) y ^ { \prime } + q ( x ) y , \quad a \leq x \leq b , \quad y ( b ) = 0 , \quad y ^ { \prime } ( b ) = 1 .
$$

If this reverse shooting technique still gives cancellation of significant digits and if increased precision does not yield greater accuracy, other techniques must be used, such as those presented later in this chapter. In general,however,if $u _ { 1 , i }$ and $v _ { 1 , i }$ are $O ( h ^ { n } )$ approximations to $y _ { 1 } ( x _ { i } )$ and $y _ { 2 } ( x _ { i } )$ ,respectively, for each $i = 0 , 1 , \dots , N$ , then $w _ { 1 , i }$ will be an $O ( h ^ { n } )$ approximation to $y ( x _ { i } )$ . In particular,

$$
\begin{array} { r } { | w _ { 1 , i } - y ( x _ { i } ) | \leq K h ^ { n } \left| 1 + \frac { v _ { 1 , i } } { \upsilon _ { 1 , N } } \right| , } \end{array}
$$

for some constant $K$ (see [IK, p. 426]).

1. The boundary-value problem

$$
y ^ { \prime \prime } = 4 ( y - x ) , \quad 0 \leq x \leq 1 , \quad y ( 0 ) = 0 , \quad y ( 1 ) = 2 ,
$$

has the solution $y ( x ) = e ^ { 2 } ( e ^ { 4 } - 1 ) ^ { - 1 } ( e ^ { 2 x } - e ^ { - 2 x } ) + x$ . Use the Linear Shooting method to approximate the solution,and compare the results to the actual solution.

a. With $\begin{array} { r } { h = \frac { 1 } { 2 } } \end{array}$ ： $\begin{array} { r } { \mathbf { b } . \quad \mathrm { W i t h } \ h = \frac { 1 } { 4 } . } \end{array}$

2. The boundary-value problem

$$
\begin{array} { r } { y ^ { \prime \prime } = y ^ { \prime } + 2 y + \cos x , \quad 0 \leq x \leq \frac { \pi } { 2 } , \quad y ( 0 ) = - 0 . 3 , \quad y \left( \frac { \pi } { 2 } \right) = - 0 . 1 } \end{array}
$$

has the solution $\begin{array} { r } { y ( x ) = - \frac { 1 } { 1 0 } ( \sin x + 3 \cos x ) } \end{array}$ . Use the Linear Shooting method to approximate the solution,and compare the results to the actual solution.

a.With $\begin{array} { r } { h = \frac { \pi } { 4 } } \end{array}$ ； $\begin{array} { r } { \mathbf { b } . \quad \mathbf { W } \mathbf { i } \mathrm { t h } \ h = \frac { \pi } { 8 } . } \end{array}$

3.Use the Linear Shooting method to approximate the solution to the folowing boundary-value problems.

a. $y ^ { \prime \prime } = - 3 y ^ { \prime } + 2 y + 2 x + 3 , \quad 0 \leq x \leq 1 , \ y ( 0 ) = 2 , \ y ( 1 ) = 1 ; \ { \mathrm { u s e } } \ h = 0 . 1 .$ b. $\begin{array} { r } { y ^ { \prime \prime } = - \frac { 4 } { r } y ^ { \prime } + \frac { 2 } { r ^ { 2 } } y - \frac { 2 } { r ^ { 2 } } \ln x , \quad 1 \leq x \leq 2 , ~ y ( 1 ) = - \frac { 1 } { 2 } , ~ y ( 2 ) = \ln 2 ; ~ \mathrm { u s e } ~ h = 1 . } \end{array}$ $h = 0 . 0 5$ c. $y ^ { \prime \prime } = - ( x + 1 ) y ^ { \prime } + 2 y + ( 1 - x ^ { 2 } ) e ^ { - x } , \quad 0 \leq x \leq 1 , \ y ( 0 ) = - 1 , \ y ( 1 ) = 0 ;$ use $h = 0 . 1$ ， d. $\begin{array} { r } { y ^ { \prime \prime } = { \frac { y ^ { \prime } } { x } } + { \frac { 3 } { x ^ { 2 } } } y + { \frac { \ln x } { x } } - 1 , \quad 1 \leq x \leq 2 , \ y ( 1 ) = y ( 2 ) = 0 ; \ { \mathrm { u s e } } } \end{array}$ $h = 0 . 1$

4. Although $q ( x ) \ < \ 0$ in the following boundary-value problems,unique solutions exist and are given. Use the Linear Shooting Algorithm to approximate the solutions to the following problems,and compare the results to the actual solutions.

a. $\begin{array} { r l } & { y ^ { \prime \prime } + y = 0 , \quad 0 \leq x \leq \frac { \pi } { 4 } , y ( 0 ) = 1 , y ( \frac { \pi } { 4 } ) = 1 ; \mathrm { u s e } h = \frac { \pi } { 2 0 } ; } \\ & { } \\ & { y ( x ) = \cos x + ( \sqrt { 2 } - 1 ) \sin x . } \end{array}$ actual solution   
b. $\begin{array} { r } { y ^ { \prime \prime } + 4 y = \cos x , \quad 0 \leq x \leq \frac { \pi } { 4 } , \ y ( 0 ) = 0 , \ y ( \frac { \pi } { 4 } ) = 0 ; \ \mathrm { u s e } } \end{array}$ $h \ : = \ : \frac { \pi } { 2 0 }$ ； actual solution $\begin{array} { r } { y ( x ) = - \frac { 1 } { 3 } \cos 2 x - \frac { \sqrt { 2 } } { 6 } \sin 2 x + \frac { 1 } { 3 } \cos x } \end{array}$   
c. $\begin{array} { r } { y ^ { \prime \prime } = - \frac { 4 } { x } y ^ { \prime } - \frac { 2 } { x ^ { 2 } } y + \frac { 2 } { x ^ { 2 } } \ln x , \quad 1 \leq x \leq 2 , ~ y ( 1 ) = \frac { 1 } { 2 } , ~ y ( 2 ) = \ln 2 ; } \end{array}$ use $h = 0 . 0 5$ ; actual solution $\begin{array} { r } { y ( x ) = \frac { 4 } { x } - \frac { 2 } { x ^ { 2 } } + \ln x - \frac { 3 } { 2 } } \end{array}$   
d $y ^ { \prime \prime } = 2 y ^ { \prime } - y + x e ^ { x } - x , \quad 0 \leq x \leq 2 , ~ y ( 0 ) = 0 , ~ y ( 2 ) = - 4$ use $h = 0 . 2$ ; actual solution $\begin{array} { r } { y ( x ) = \frac { 1 } { 6 } x ^ { 3 } e ^ { x } - \frac { 5 } { 3 } x e ^ { x } + 2 e ^ { x } - x - 2 } \end{array}$

5. Use the Linear Shooting Algorithm to approximate the solution y = e-10x to the boundaryvalue problem

$$
y ^ { \prime \prime } = 1 0 0 y , \quad 0 \leq x \leq 1 , \quad y ( 0 ) = 1 , \quad y ( 1 ) = e ^ { - 1 0 } .
$$

Use $h = 0 . 1$ and 0.05.

6. Write the second-order initial-value problems (11.3） and (11.4） as first-order systems,and derive the equations necessary to solve the systems using the fourth-order Runge-Kuta method for systems.

7.Let u represent the electrostatic potential between two concentric metal spheres of radii R and R2 (R < R2). The potential of the inner sphere is kept constant at Vi volts,and the potential of the outer sphere is O volts. The potential in the region between the two spheres is governed by Laplace's equation, which,in this particular application,reduces to

$$
\frac { d ^ { 2 } u } { d r ^ { 2 } } + \frac { 2 } { r } \frac { d u } { d r } = 0 , { R } _ { 1 } \leq r \leq { R } _ { 2 } , { u } ( { R } _ { 1 } ) = V _ { 1 } , u ( { R } _ { 2 } ) = 0 .
$$

Suppose R = 2 in. R2 = 4 in.,and V = 110 volts.

Approximate $u ( 3 )$ using the Linear Shooting Algorithm.

b.Compare the results of part (a) with the actual potential u(3), where

$$
u ( r ) = { \frac { V _ { 1 } R _ { 1 } } { r } } \left( { \frac { R _ { 2 } - r } { R _ { 2 } - R _ { 1 } } } \right) .
$$

8.Show that, under the hypothesis of Corollary 11.2,if $y _ { 2 }$ is the solution to $y ^ { \prime \prime } = p ( x ) y ^ { \prime } + q ( x ) y$ and $y _ { 2 } ( a ) = y _ { 2 } ( b ) = 0$ ,then $y _ { 2 } \equiv 0$ ·

9. Consider the boundary-value problem

$$
y ^ { \prime \prime } + y = 0 , \quad 0 \leq x \leq b , \quad y ( 0 ) = 0 , \quad y ( b ) = B .
$$

Find choices for $b$ and $B$ so that the boundary-value problem has

a. No solution;   
b. Exactly one solution;   
c. Infinitely many solutions.

10.Attempt to apply Exercise 9 to the boundary-value problem

$$
y ^ { \prime \prime } - y = 0 , \quad 0 \leq x \leq b , \quad y ( 0 ) = 0 , \quad y ( b ) = B .
$$

What happens? How do both problems relate to Corollary 11.2?

# 11.2 The Shooting Method for Nonlinear Problems

The shooting technique for the nonlinear second-order boundary-value problem

$$
y ^ { \prime \prime } = f ( x , y , y ^ { \prime } ) , \quad a \leq x \leq b , \quad y ( a ) = \alpha , \quad y ( b ) = \beta ,
$$

is similar to the linear technique, except that the solution to a nonlinear problem cannot be expressed as a linear combination of the solutions to two initial-value problems. Instead, we approximate the solution to the boundary-value problem by using the solutions to a

sequence of initial-value problems involving a parameter $t$ . These problems have the form

$$
y ^ { \prime \prime } = f ( x , y , y ^ { \prime } ) , \quad a \leq x \leq b , \quad y ( a ) = \alpha , \quad y ^ { \prime } ( a ) = t .
$$

We do this by choosing the parameters $t = t _ { k }$ in a manner to ensure that

$$
\operatorname* { l i m } _ { k \to \infty } y ( b , t _ { k } ) = y ( b ) = \beta ,
$$

where $y ( x , t _ { k } )$ denotes the solution to the initial-value problem (11.7) with $t = t _ { k }$ , and $y ( x )$ denotes the solution to the boundary-value problem (11.6).

![](images/717c4ebe530ae7f5e54c9b5ffe435ab509d4d440963dc2ab88c2f1be767f1fba.jpg)  
Figure 11.2

This technique is called a “shooting" method, by analogy to the procedure of firing objects at a stationary target. (See Figure 11.2.) We start with a parameter $t _ { 0 }$ that determines the initial elevation at which the object is fired from the point $( a , \alpha )$ and along the curve described by the solution to the initial-value problem:

$$
y ^ { \prime \prime } = f ( x , y , y ^ { \prime } ) , \quad a \leq x \leq b , \quad y ( a ) = \alpha , \quad y ^ { \prime } ( a ) = t _ { 0 } .
$$

If $y ( b , t _ { 0 } )$ is not sufficiently close to $\beta$ ， we correct our approximation by choosing elevations $t _ { 1 } , t _ { 2 }$ ,and so on, until $y ( b , t _ { k } )$ is sufficiently close to “hiting” $\beta$ . (See Figure 11.3.)

To determine the parameters $t _ { k }$ , suppose a boundary-value problem of the form (11.6) satisfies the hypotheses of Theorem 11.1. If $y ( x , t )$ denotes the solution to the initial-value problem (11.7), we next determine $t$ with

$$
y ( b , t ) - \beta = 0 .
$$

This is a nonlinear equation of the type considered in Chapter 2, so a number of methods are available.

To use the Secant method to solve the problem, we need to choose initial approximations $t _ { 0 }$ and $t _ { \downarrow }$ , and then generate the remaining terms of the sequence by

$$
t _ { k } = t _ { k - 1 } - \frac { ( y ( b , t _ { k - 1 } ) - \beta ) ( t _ { k - 1 } - t _ { k - 2 } ) } { y ( b , t _ { k - 1 } ) - y ( b , t _ { k - 2 } ) } , \quad k = 2 , 3 , \ldots .
$$

![](images/3e9588c5f584db3a87a80d8e5225c92d554d7f3863f6f24cc967b60cc5a42c96.jpg)  
Figure 11.3

To use the more powerful Newton's method to generate the sequence $\left\{ t _ { k } \right\}$ ,only one initial approximation, $t _ { 0 } ,$ ,is needed. However,the iteration has the form

$$
t _ { k } = t _ { k - 1 } - \frac { y ( b , t _ { k - 1 } ) - \beta } { \frac { d y } { d t } ( b , t _ { k - 1 } ) } ,
$$

and it requires the knowledge of $( d y / d t ) ( b , t _ { k - 1 } )$ . This presents a difficulty since an explicit representation for ${ \boldsymbol { y } } ( { \boldsymbol { b } } , t )$ is not known; we know only the values $y ( b , t _ { 0 } ) , y ( b , t _ { 1 } )$ ， $\dots , y ( b , t _ { k - 1 } )$

Suppose we rewrite the initial-value problem (11.7),emphasizing that the solution depends on both $\pmb { x }$ and the parameter $\pmb { t }$ ：

$$
y ^ { \prime \prime } ( x , t ) = f ( x , y ( x , t ) , y ^ { \prime } ( x , t ) ) , \quad a \leq x \leq b , \quad y ( a , t ) = \alpha , \quad y ^ { \prime } ( a , t ) = t .
$$

We have retained the prime notation to indicate diferentiation with respect to $x$ . Since we need to determine $( d y / d t ) ( b , t )$ when $t = t _ { k - 1 }$ , we first take the partial derivative of (11.10) with respect to $\pmb { t }$ . This implies that

$$
\begin{array} { l } { \displaystyle \frac { \partial y ^ { \prime \prime } } { \partial t } ( x , t ) = \frac { \partial f } { \partial t } ( x , y ( x , t ) , y ^ { \prime } ( x , t ) ) } \\ { \displaystyle = \frac { \partial f } { \partial x } ( x , y ( x , t ) , y ^ { \prime } ( x , t ) ) \frac { \partial x } { \partial t } + \frac { \partial f } { \partial y } ( x , y ( x , t ) , y ^ { \prime } ( x , t ) ) \frac { \partial y } { \partial t } ( x , t ) } \\ { \displaystyle ~ + \frac { \partial f } { \partial y ^ { \prime } } ( x , y ( x , t ) , y ^ { \prime } ( x , t ) ) \frac { \partial y ^ { \prime } } { \partial t } ( x , t ) . } \end{array}
$$

Since $x$ and $t$ are independent, $\partial x / \partial t = 0$ and

$$
\frac { \partial y ^ { \prime \prime } } { \partial t } ( x , t ) = \frac { \partial f } { \partial y } ( x , y ( x , t ) , y ^ { \prime } ( x , t ) ) \frac { \partial y } { \partial t } ( x , t ) + \frac { \partial f } { \partial y ^ { \prime } } ( x , y ( x , t ) , y ^ { \prime } ( x , t ) ) \frac { \partial y ^ { \prime } } { \partial t } ( x , t ) ,
$$

for $a \leq x \leq b$ . The initial conditions give

$$
{ \frac { \partial y } { \partial t } } ( a , t ) = 0 \qquad { \mathrm { a n d } } \qquad { \frac { \partial y ^ { \prime } } { \partial t } } ( a , t ) = 1 .
$$

If we simplify the notation by using $z ( x , t )$ to denote $( \partial y / \partial t ) ( x , t )$ and assume that the order of differentiation of $x$ and $t$ can be reversed,(11.11） with the initial conditions becomes the initial-value problem

$$
\begin{array} { r l r } { z ^ { \prime \prime } ( x , t ) = \displaystyle \frac { \partial f } { \partial y } ( x , y , y ^ { \prime } ) z ( x , t ) + \displaystyle \frac { \partial f } { \partial y ^ { \prime } } ( x , y , y ^ { \prime } ) z ^ { \prime } ( x , t ) , } & { } & \\ { a \leq x \leq b , \quad z ( a , t ) = 0 , \quad z ^ { \prime } ( a , t ) = 1 . } & { } & \end{array}
$$

Newton's method therefore requires that two initial-value problems be solved for each iteration,(11.10) and (11.12). Then from Eq. (11.9),

$$
t _ { k } = t _ { k - 1 } - { \frac { y ( b , t _ { k - 1 } ) - \beta } { z ( b , t _ { k - 1 } ) } } .
$$

Of course, none of these initial-value problems is solved exactly; the solutions are approximated by one of the methods discussed in Chapter 5. Algorithm 11.2 uses the Runge-Kutta method of order four to approximate both solutions required by Newton's method. A similar procedure for the Secant method is considered in Exercise 4.

![](images/b1725d7c20c33885322995c1f0527283b026f6870727e53e4e3e6eae1a6a46ab.jpg)

# Nonlinear Shooting with Newton's Method

To approximate the solution of the nonlinear boundary-value problem

$$
y ^ { \prime \prime } = f ( x , y , y ^ { \prime } ) , \quad a \leq x \leq b , \quad y ( a ) = \alpha , \quad y ( b ) = \beta \ ;
$$

(Note: Equations (11.10) and (11.12) are written as frst-order systems and solved.)

INPUT endpoints $a , b$ ; boundary conditions $\alpha , \beta$ ; number of subintervals $N \ge 2$ ; toler-ance TOL; maximum number of iterations $M$ .

OUTPUTapproximations $\boldsymbol { w } _ { 1 , i }$ to $y ( x _ { i } ) ; w _ { 2 , i }$ to $y ^ { \prime } ( x _ { i } )$ for each $i = 0 , 1 , \dots , N$ ora message that the maximum number of iterations was exceeded.

Step 1 Set $h = ( b - a ) / N$ $k = 1$ ； TK = (β -α)/(b -a). (Note: TK could also be input.)

Step 2 While $( k \le M )$ do Steps 3-10.

Step3 Se $\begin{array} { c } { { : w _ { 1 , 0 } = \alpha ; } } \\ { { w _ { 2 , 0 } = T K ; } } \\ { { u _ { 1 } = 0 ; } } \\ { { u _ { 2 } = 1 . } } \end{array}$

Step 4For $i = 1 , \dots , N$ do Steps 5 and 6. (The Runge-Kutta method for systems is used in Steps 5 and 6.)

Step5Set $x = a + ( i - 1 ) h$

$$
\begin{array} { r l } { \mathbb { E } _ { \lambda \geq - 1 } ^ { n } - \mathbb { E } ( \lambda \leq r _ { + + } , 1 ) ^ { 2 } \mathbb { E } _ { \lambda \geq 1 } } & { \mathrm { ~ i ~ f ~ } } \\ { \mathbb { E } _ { \lambda \geq - 1 } ^ { n } - \mathbb { E } ( \lambda \leq r _ { + } , 1 ) ^ { 2 } \mathbb { E } _ { \lambda \geq 1 } } & { \mathrm { ~ i ~ f ~ } } \\ { \mathbb { E } _ { \lambda \geq - 1 } ^ { n } - \mathbb { E } _ { \lambda \geq 1 } ^ { n } - \mathbb { E } _ { \lambda \geq 1 } ^ { n } - \mathbb { E } _ { \lambda \geq 1 } ^ { n } - \mathbb { E } _ { \lambda \geq 1 } ^ { n } } & { \mathrm { ~ i ~ f ~ } } \\ { \mathbb { E } _ { \lambda \geq - 1 } ^ { n } - \mathbb { E } _ { \lambda \geq 1 } ^ { n } - \mathbb { E } _ { \lambda \geq 1 } ^ { n } - \mathbb { E } _ { \lambda \geq 1 } ^ { n } - \mathbb { E } _ { \lambda \geq 1 } ^ { n } } & { \mathrm { ~ i ~ f ~ } } \\ { \mathbb { E } _ { \lambda \leq - 1 } ^ { n } - \mathbb { E } _ { \lambda \geq 1 } ^ { n } - \mathbb { E } _ { \lambda \geq 1 } ^ { n } - \mathbb { E } _ { \lambda \geq 1 } ^ { n } - \mathbb { E } _ { \lambda \geq 1 } ^ { n } } & { \mathrm { ~ i ~ f ~ } } \\ { \mathbb { E } _ { \lambda \geq - 1 } ^ { n } - \mathbb { E } _ { \lambda \geq 1 } ^ { n } - \mathbb { E } _ { \lambda \geq 1 } ^ { n } - \mathbb { E } _ { \lambda \geq 1 } ^ { n } - \mathbb { E } _ { \lambda \geq 1 } ^ { n } } & { \mathrm { ~ i ~ f ~ } } \\ { \mathbb { E } _ { \lambda \geq - 1 } ^ { n } - \mathbb { E } _ { \lambda \geq 1 } ^ { n } - \mathbb { E } _ { \lambda \geq 1 } ^ { n } - \mathbb { E } _ { \lambda \geq 1 } ^ { n } - \mathbb { E } _ { \lambda \geq 1 } ^ { n } } & { \mathrm { ~ i ~ f ~ } } \\  \mathbb { E } _ { \lambda \geq - 1 } ^ { n } - \mathbb { E } _ { \lambda \geq 1 } ^ { n } - \mathbb { E } _ { \lambda \geq 1 } ^ { n } + \mathbb { E } _ { \lambda \geq 1 } ^ { n } - \mathbb { E } _ { \lambda \geq 1 } ^ { n } - \mathbb { E } _  \lambda \geq  \end{array}
$$$$
\begin{array} { r l } & { V _ { \mathrm { t } , 1 } ^ { \prime } = N H _ { 0 } ; } \\ & { \quad V _ { \mathrm { t } , 2 } ^ { \prime } = N H _ { 0 } ; } \\ & { \quad - \phi \langle \phi ( x , y _ { 0 } ) , . . . y _ { 0 } , z _ { 0 } , z _ { 0 } \rangle \lambda _ { 0 } , } \\ & { \quad V _ { \mathrm { t } , 3 } ^ { \prime } = N \langle x , y _ { 0 } , . . . y _ { 0 } , z _ { 0 } \rangle , } \\ & { V _ { \mathrm { t } , 4 } ^ { \prime } = N \langle x , y _ { 0 } , . . . y _ { 0 } \rangle \lambda _ { 0 } , } \\ & { V _ { \mathrm { t } , 4 } ^ { \prime } = N \langle x , y _ { 0 } , . . . y _ { 0 } \rangle \lambda _ { 1 } , \quad \mathrm { w } _ { 0 , 2 } \quad \mathrm { w } _ { 1 } \quad \mathrm { i } _ { \mathrm { R } } ; \lambda _ { 1 } \rangle , } \\ & { V _ { \mathrm { t } , 5 } ^ { \prime } = N H _ { 0 } ; } \\ & { V _ { \mathrm { t } , 5 } ^ { \prime } = N H _ { 0 } ; } \\ & { \quad V _ { \mathrm { t } , 5 } ^ { \prime } = N H _ { 0 } ; } \\ & { \quad V _ { \mathrm { t } , 6 } ^ { \prime } = N H _ { 0 } ; } \\ & { \quad V _ { \mathrm { t } , 7 } ^ { \prime } = N H _ { 0 } ; } \\ & { \quad V _ { \mathrm { t } , 7 } ^ { \prime } = N H _ { 0 } ; } \\ & { \quad V _ { \mathrm { t } , 8 } ^ { \prime } = N H _ { 0 } ; } \\ & { \quad V _ { \mathrm { t } , 7 } ^ { \prime } = N H _ { 0 } ; } \\ & { \quad V _ { \mathrm { t } , 7 } ^ { \prime } = N H _ { 0 } ; } \\ & { \quad V _ { \mathrm { t } , 8 } ^ { \prime } = N H _ { 0 } ; } \\ & { \quad V _ { \mathrm { t } , 7 } ^ { \prime } = N H _ { 0 } ; } \\ & { \quad V _ { \mathrm { t } , 8 } ^ { \prime } = N \langle x , y _ { 0 } \rangle \lambda _ { 0 } + V _ { \mathrm { t } , 7 } ^ { \prime } \rangle , } \\ & { \quad V _ { \mathrm { t } , 7 } ^ { \prime } = N \langle x , y _ { 0 } \rangle \lambda _ { 0 } + V _ { \mathrm { t } , 7 } ^ { \prime } , } \\  \end{array}
$$

Step 7If $| w _ { 1 , N } - \beta | \le T O L$ then do Steps 8 and 9.

$$
\begin{array} { r l } { S t e p \ 8 } & { \mathrm { F o r } \ i = 0 , 1 , \dots , N } \\ & { \qquad \mathrm { s e t } \ x = a + i h ; } \\ & { \qquad \mathrm { O U T P U T } \ ( x , w _ { 1 , i } , w _ { 2 , i } ) . } \end{array}
$$

Step 9 (The procedure is complete.) STOP.

![](images/1986ff8e0e15a85e43db8028c12f3acd7af8bcbb7131739e5b9c31a0ebc086e0.jpg)

Step 10 Set $T K = T K - \frac { w _ { 1 , N } - \beta } { u _ { 1 } } ;$ (Newton's method is used to compute TK.) $k = k + 1$ .

# Step 11 OUTPUT(‘Maximum number of iterations exceeded'); (The procedure was unsuccesful.) STOP.

The value $t _ { 0 } = T K$ selected in Step 1 is the slope of the straightline through $( a , \alpha )$ and $( b , \beta )$ . If the problem satisfies the hypotheses of Theorem 11.1,any choice of $t _ { 0 }$ will give convergence, but a good choice of $t _ { 0 }$ will improve convergence,and the procedure will work for many problems that do not satisfy these hypotheses.

# EXAMPLE 1

Consider the boundary-value problem

$$
y ^ { \prime \prime } = { \frac { 1 } { 8 } } ( 3 2 + 2 x ^ { 3 } - y y ^ { \prime } ) , \quad 1 \leq x \leq 3 , \quad y ( 1 ) = 1 7 , \quad y ( 3 ) = { \frac { 4 3 } { 3 } } ,
$$

which has the exact solution $y ( x ) = x ^ { 2 } + 1 6 / x$

Applying theShootingmethod giveninAlgorithm11.2tothisproblemrequiresapproximating solutions to the initial-value problems

$$
y ^ { \prime \prime } = { \frac { 1 } { 8 } } ( 3 2 + 2 x ^ { 3 } - y y ^ { \prime } ) , \quad 1 \leq x \leq 3 , \quad y ( 1 ) = 1 7 , \quad y ^ { \prime } ( 1 ) = t _ { k } ,
$$

and

$$
z ^ { \prime \prime } = \frac { \partial f } { \partial y } z + \frac { \partial f } { \partial y ^ { \prime } } z ^ { \prime } = - \frac { 1 } { 8 } ( y ^ { \prime } z + y z ^ { \prime } ) , \quad 1 \leq x \leq 3 , \quad z ( 1 ) = 0 , \quad z ^ { \prime } ( 1 ) = 1 ,
$$

# Table 11.2

<table><tr><td>Xi</td><td>W1,i</td><td>y(xi）</td><td>|w1.i-y(xi）</td></tr><tr><td>1.0</td><td>17.000000</td><td>17.000000</td><td></td></tr><tr><td>1.1</td><td>15.755495</td><td>15.755455</td><td>4.06 × 10-5</td></tr><tr><td>1.2</td><td>14.773389</td><td>14.773333</td><td>5.60 × 10-5</td></tr><tr><td>1.3</td><td>13.997752</td><td>13.997692</td><td>5.94 × 10-5</td></tr><tr><td>1.4</td><td>13.388629</td><td>13.388571</td><td>5.71 × 10-5</td></tr><tr><td>1.5</td><td>12.916719</td><td>12.916667</td><td>5.23 × 10-5</td></tr><tr><td>1.6</td><td>12.560046</td><td>12.560000</td><td>4.64 × 10-5</td></tr><tr><td>1.7</td><td>12.301805</td><td>12.301765</td><td>4.02 × 10-5</td></tr><tr><td>1.8</td><td>12.128923</td><td>12.128889</td><td>3.14 × 10-5</td></tr><tr><td>1.9</td><td>12.031081</td><td>12.031053</td><td>2.84 × 10-5</td></tr><tr><td>2.0</td><td>12.000023</td><td>12.000000</td><td>2.32 × 10-5</td></tr><tr><td>2.1</td><td>12.029066</td><td>12.029048</td><td>1.84 × 10-5</td></tr><tr><td>2.2</td><td>12.112741</td><td>12.112727</td><td>1.40 × 10-5</td></tr><tr><td>2.3</td><td>12.246532</td><td>12.246522</td><td>1.01 × 10-5</td></tr><tr><td>2.4</td><td>12.426673</td><td>12.426667</td><td>6.68×10-6</td></tr><tr><td>2.5</td><td>12.650004</td><td>12.650000</td><td>3.61 × 10-6</td></tr><tr><td>2.6</td><td>12.913847</td><td>12.913845</td><td>9.17 × 10-7</td></tr><tr><td>2.7</td><td>13.215924</td><td>13.215926</td><td>1.43 × 10-6</td></tr><tr><td>2.8</td><td>13.554282</td><td>13.554286</td><td>3.46 × 10-6</td></tr><tr><td>2.9</td><td>13.927236</td><td>13.927241</td><td>5.21 × 10-6</td></tr><tr><td>3.0</td><td>14.333327</td><td>14.333333</td><td>6.69 × 10-6</td></tr></table>

at each step in the iteration. If the stopping technique requires

$$
| w _ { 1 , N } ( t _ { k } ) - y ( 3 ) | \leq 1 0 ^ { - 5 } ,
$$

then we need four iterations and $t _ { 4 } = - 1 4 . 0 0 0 2 0 3$ . The results obtained for this value of t are shown in Table 11.2.

Although Newton's method used with the shooting technique requires the solution of an additional initial-value problem,it will generally give faster convergence than the Secant method. Both methods are only locally convergent since they require good initial approximations. For a general discussion of the convergence of the shooting techniques for nonlinear problems,the reader is referred to the excellent book by Keller [Keller, H]. In that reference, more general boundary conditions are discussed.It is also noted that the shooting technique for nonlinear problems is sensitive to roundoff errors, especially if the solution $y ( x )$ and $z ( x , t )$ are rapidly increasing functions of $x$ on $[ a , b ]$

1．Use the Nonlinear Shooting Algorithm with $h \ = \ 0 . 5$ to approximate the solution to the boundary-value problem

$$
y ^ { \prime \prime } = - ( y ^ { \prime } ) ^ { 2 } - y + \ln x , \quad 1 \leq x \leq 2 , \quad y ( 1 ) = 0 , \quad y ( 2 ) = \ln 2 .
$$

Compare your results to the actual solution $y = \ln x$

2. Use the Nonlinear Shooting Algorithm with $h \ = \ 0 . 2 5$ to approximate the solution to the boundary-value problem

$$
y ^ { \prime \prime } = 2 y ^ { 3 } , \quad - 1 \leq x \leq 0 , \quad y ( - 1 ) = { \frac { 1 } { 2 } } , \quad y ( 0 ) = { \frac { 1 } { 3 } } .
$$

Compare your results to the actual solution $y ( x ) = 1 / ( x + 3 )$

3. Use the Nonlinear Shooting method with $T O L = 1 0 ^ { - 4 }$ to approximate the solution to the following boundary-value problems. The actual solution is given for comparison to your results.

a. $y ^ { \prime \prime } = y ^ { 3 } - y y ^ { \prime } , \quad 1 \leq x \leq 2 , y ( 1 ) = { \textstyle { \frac { 1 } { 2 } } } , y ( 2 ) = { \textstyle { \frac { 1 } { 3 } } }$ use $h \ = \ 0 . 1$ ； actual solution $y ( x ) = ( x + 1 ) ^ { - 1 }$ ，   
b. $\begin{array} { r } { y ^ { \prime \prime } = 2 y ^ { 3 } - 6 y - 2 x ^ { 3 } , \quad 1 \leq x \leq 2 , y ( 1 ) = 2 , y ( 2 ) = \frac { 5 } { 2 } ; } \end{array}$ use $h = 0 . 1$ ; actual solution $y ( x ) = x + x ^ { - 1 }$   
c. $y ^ { \prime \prime } = y ^ { \prime } + 2 ( y - \ln x ) ^ { 3 } - x ^ { - 1 } , \quad 2 \leq x \leq 3 , y ( 2 ) = { \textstyle { \frac { 1 } { 2 } } } + \ln 2 , y ( 3 ) = { \textstyle { \frac { 1 } { 3 } } } + \ln 3 ;$ use $h = 0 . 1$ ; actual solution $\mathfrak { y } ( { \mathfrak { x } } ) = { \mathfrak { x } } ^ { - 1 } + \ln x$   
d. $y ^ { \prime \prime } = [ x ^ { 2 } ( y ^ { \prime } ) ^ { 2 } - 9 y ^ { 2 } + 4 x ^ { 6 } ] / x ^ { 5 } , \quad 1 \leq x \leq 2 , y ( 1 ) = 0 , y ( 2 ) = \ln 2 5 6 ; \mathrm { u }$ se $h = 0 . 0 5$ ； actual solution $y ( x ) = x ^ { 3 } \ln x$

4. Change Algorithm 11.2 to incorporate the Secant method instead of Newton's method. Use $t _ { 0 } = ( \beta - \alpha ) / ( b - a )$ and $t _ { 1 } = t _ { 0 } + ( \beta - y ( b , t _ { 0 } ) ) / ( b - a )$

5.Repeat Exercise 3(a)and 3(c) using the Secant algorithm derived in Exercise 4,and compare the number of iterations required for the two methods.

6. The Van der Pol equation,

$$
y ^ { \prime \prime } - \mu ( y ^ { 2 } - 1 ) y ^ { \prime } + y = 0 , \quad \mu > 0 ,
$$

governs the fow of current in a vacuum tube with thre intemal elements. Let $\begin{array} { r } { \mu = \frac { 1 } { 2 } } \end{array}$ ， $y ( 0 ) =$ 0,and $y ( 2 ) = 1$ . Approximate the solution $y ( t )$ for $t = 0 . 2 i$ , where $1 \leq i \leq 9$

# 11.3 Finite-Difference Methods for Linear Problems

The linear and nonlinear Shooting methods for boundary-value problems can present prob-lems of instability.The methods inthissectionhavebeter stabilitycharacteristics,butthey generally require more computation to obtain a specified accuracy.

Methods involving finite differences for solving boundary-value problems replace each of the derivatives in the differential equation with an appropriate difference-quotient approximation of the type considered in Section 4.1. The particular diference quotient and step size $h$ are chosen to maintain a specified order of truncation error. However, $h$ cannot be chosen too smal because of the instability of the derivative approximations.

The finite diference method for the linear second-order boundary-value problem,

$$
y ^ { \prime \prime } = p ( x ) y ^ { \prime } + q ( x ) y + r ( x ) , \quad a \leq x \leq b , \quad y ( a ) = \alpha , \quad y ( b ) = \beta ,
$$

requires that difference-quotient approximations be used to approximate both $y ^ { \prime }$ and $y ^ { \prime \prime }$ First, we select an integer $N > 0$ and divide the interval $[ a , b ]$ into $( N + 1 )$ equal subintervals whose endpoints are the mesh points $x _ { i } = a + i h$ ,for $i = 0$ ， $1 , \ldots , N + 1$ ,where $h = ( b - a ) / ( N + 1 )$ . Choosing the step size $h$ in this manner facilitates the application of a matrix algorithm from Chapter 6,which solves a linear system involving an $N \times N$ matrix.

At the interior mesh points, $x _ { i }$ ,for $i = 1 , 2 , \dots , N$ , the differential equation to be approximated is

$$
y ^ { \prime \prime } ( x _ { i } ) = p ( x _ { i } ) y ^ { \prime } ( x _ { i } ) + q ( x _ { i } ) y ( x _ { i } ) + r ( x _ { i } ) .
$$

Expanding $y$ in a third Taylor polynomial about $x _ { i }$ evaluated at $x _ { i + 1 }$ and $x _ { i - 1 }$ , we have, assuming that $y \in C ^ { 4 } \{ x _ { i - 1 } , x _ { i + 1 } \}$ ，

$$
y ( x _ { i + 1 } ) = y ( x _ { i } + h ) = y ( x _ { i } ) + h y ^ { \prime } ( x _ { i } ) + { \frac { h ^ { 2 } } { 2 } } { \dot { y } } ^ { \prime \prime } ( x _ { i } ) + { \frac { h ^ { 3 } } { 6 } } y ^ { \prime \prime \prime } ( x _ { i } ) + { \frac { h ^ { 4 } } { 2 4 } } y ^ { ( 4 ) } ( \xi _ { i } ^ { + } ) ,
$$

for some ${ \boldsymbol { \xi } } _ { i } ^ { + }$ in $( x _ { i } , x _ { i + 1 } )$ ,and

$$
y ( x _ { i - 1 } ) = y ( x _ { i } - h ) = y ( x _ { i } ) - h y ^ { \prime } ( x _ { i } ) + { \frac { h ^ { 2 } } { 2 } } y ^ { \prime \prime } ( x _ { i } ) - { \frac { h ^ { 3 } } { 6 } } y ^ { \prime \prime \prime } ( x _ { i } ) + { \frac { h ^ { 4 } } { 2 4 } } y ^ { ( 4 ) } ( \xi _ { i } ^ { - } ) ,
$$

for some ${ \xi } _ { i } ^ { - }$ in $( x _ { i - 1 } , x _ { i } )$ . If these equations are added, we have

$$
y ( x _ { i + 1 } ) + y ( x _ { i - 1 } ) = 2 y ( x _ { i } ) + h ^ { 2 } y ^ { \prime \prime } ( x _ { i } ) + \frac { h ^ { 4 } } { 2 4 } [ y ^ { ( 4 ) } ( \xi _ { i } ^ { + } ) + y ^ { ( 4 ) } ( \xi _ { i } ^ { - } ) ] ,
$$

and solving for $y ^ { \prime \prime } ( x _ { i } )$ gives

$$
y ^ { \prime \prime } ( x _ { i } ) = \frac { 1 } { h ^ { 2 } } [ y ( x _ { i + 1 } ) - 2 y ( x _ { i } ) + y ( x _ { i - 1 } ) ] - \frac { h ^ { 2 } } { 2 4 } [ y ^ { ( 4 ) } ( \xi _ { i } ^ { + } ) + y ^ { ( 4 ) } ( \xi _ { i } ^ { - } ) ] .
$$

The Intermediate Value Theorem can be used to simplify this to

$$
y ^ { \prime \prime } ( x _ { i } ) = { \frac { 1 } { h ^ { 2 } } } [ y ( x _ { i + 1 } ) - 2 y ( x _ { i } ) + y ( x _ { i - 1 } ) ] - { \frac { h ^ { 2 } } { 1 2 } } y ^ { ( 4 ) } ( \xi _ { i } ) ,
$$

for some $\xi _ { i }$ in $( x _ { i - 1 } , x _ { i + 1 } )$ . This is called the centered-difference formula for ${ \bf y } ^ { \prime \prime } ( x _ { i } )$

A centered-difference formula for $y ^ { \prime } ( x _ { i } )$ is obtained in a similar manner (the details were considered in Section 4.1), resulting in

$$
y ^ { \prime } ( x _ { i } ) = { \frac { 1 } { 2 h } } [ y ( x _ { i + 1 } ) - y ( x _ { i - 1 } ) ] - { \frac { h ^ { 2 } } { 6 } } y ^ { \prime \prime \prime } ( \eta _ { i } ) ,
$$

for some $\eta _ { i }$ in $( x _ { i - 1 } , x _ { i + 1 } )$

The use of these centered-difference formulas in Eq. (11.15) results in the equation

$$
\begin{array} { r l r } & { } & { \frac { y ( x _ { i + 1 } ) - 2 y ( x _ { i } ) + y ( x _ { i - 1 } ) } { h ^ { 2 } } = p ( x _ { i } ) \bigg [ \frac { y ( x _ { i + 1 } ) - y ( x _ { i - 1 } ) } { 2 h } \bigg ] + q ( x _ { i } ) y ( x _ { i } ) } \\ & { } & { \qquad + r ( x _ { i } ) - \displaystyle \frac { h ^ { 2 } } { 1 2 } \left[ 2 p ( x _ { i } ) y ^ { \prime \prime } ( \eta _ { i } ) - y ^ { ( 4 ) } ( \xi _ { i } ) \right] . } \end{array}
$$

A Finite-Difference method with truncation error of order $O ( h ^ { 2 } )$ results by using this equation together with the boundary conditions $y ( a ) = \alpha$ and $y ( b ) = \beta$ to define

$$
w _ { 0 } = \alpha , \qquad w _ { N + 1 } = \beta
$$

and

$$
\left( \frac { - w _ { i + 1 } + 2 w _ { i } - w _ { i - 1 } } { h ^ { 2 } } \right) + p ( x _ { i } ) \left( \frac { w _ { i + 1 } - w _ { i - 1 } } { 2 h } \right) + q ( x _ { i } ) w _ { i } = - r ( x _ { i } ) ,
$$

for each $i = 1 , 2 , \dots , N$

In the form we will consider,Eq. (11.18) is rewritten as

$$
- \left( 1 + \frac { h } { 2 } p ( x _ { i } ) \right) w _ { i - 1 } + \left( 2 + h ^ { 2 } q ( x _ { i } ) \right) w _ { i } - \left( 1 - \frac { h } { 2 } p ( x _ { i } ) \right) w _ { i + 1 } = - h ^ { 2 } r ( x _ { i } ) ,
$$

and the resulting system of equations is expressed in the tridiagonal $N \times N$ matrix form

$$
A \mathbf { w } = \mathbf { b } , \quad \quad \mathbf { w } \mathbf { h e r e }
$$

$$
A = \left[ { \begin{array} { c c c c c c c c c } { 2 + h ^ { 2 } q ( x _ { 1 } ) } & { - 1 + { \frac { h } { 2 } } p ( x _ { 1 } ) } & { 0 : \underbrace { \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots } } & { 0 } & { 0 } & { \cdots } & { \cdots } & { \cdots } & { \cdots } & { 0 } \\ { \displaystyle - 1 - { \frac { h } { 2 } } p ( x _ { 2 } ) } & { 2 + h ^ { 2 } q ( x _ { 2 } ) } & { - 1 + { \frac { h } { 2 } } p ( x _ { 2 } ) } & { \cdots } & { \cdots } & { \cdots } & { \cdots } & { \cdots } & { \cdots } \\ { \displaystyle { \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots } } & { \cdots \cdots \cdots } & { \cdots } & { \cdots } & { \cdots } & { \cdots } & { \cdots } & { \cdots } \\ { \displaystyle { \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots } } & { \cdots \cdots \cdots \cdots \cdots \cdots } & { \cdots } & { \cdots } & { \cdots } & { \cdots } \\ { \displaystyle { \vdots } } & { \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots } & { \cdots \cdots \cdots \cdots \cdots } & { \cdots } & { \cdots } & { \cdots } & { \cdots } \\ { \displaystyle { \partial } \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots } & { \cdots } & { - 1 - { \frac { h } { 2 } } p ( x _ { N } ) } & { \cdots } & { \cdots } & { \cdots } & { \cdots } & { \cdots } \end{array} } \right] ,
$$

$$
\mathbf { w } = \left[ \begin{array} { c } { w _ { 1 } } \\ { w _ { 2 } } \\ { \vdots } \\ { w _ { N - 1 } } \\ { w _ { N } } \end{array} \right] , \quad \mathrm { a n d } \quad \mathbf { b } = \left[ \begin{array} { c } { - h ^ { 2 } r ( x _ { 1 } ) + \left( 1 + \displaystyle \frac { h } { 2 } p ( x _ { 1 } ) \right) w _ { 0 } } \\ { - h ^ { 2 } r ( x _ { 2 } ) } \\ { \vdots } \\ { - h ^ { 2 } r ( x _ { N - 1 } ) } \\ { - h ^ { 2 } r ( x _ { N } ) + \left( 1 - \displaystyle \frac { h } { 2 } p ( x _ { N } ) \right) w _ { N + 1 } } \end{array} \right] .
$$

The following theorem gives conditions under which the tridiagonal linear system (11.19) has a unique solution. Its proof is a consequence of Theorem 6.29 and is considered in Exercise 9.

# Theorem 11.3

Suppose that $p , q$ ,and $r$ are continuous on $[ a , b ]$ .If $q ( x ) \geq 0$ on $[ a , b ]$ , then the tridi-agonal linear system (11.19) has a unique solution provided that $h \ < \ 2 / L$ ，where $L =$ $\mathrm { m a x } _ { a \leq x \leq b } \mid p ( x ) \mid$

It should be noted that the hypotheses of Theorem 11.3 guarantee a unique solution to the boundary-value problem (11.14), but they do not guarantee that $y \in C ^ { 4 } [ a , b ]$ . We need to establish that $y ^ { ( 4 ) }$ is continuous on $[ a , b ]$ to ensure that the truncation error has order $O ( h ^ { 2 } )$

Algorithm 11.3 implements the Linear Finite-Diference method.

# Linear Finite-Difference

To approximate the solution of the boundary-value problem

$$
y ^ { \prime \prime } = p ( x ) y ^ { \prime } + q ( x ) y + r ( x ) , \quad a \leq x \leq b , \quad y ( a ) = \alpha , \quad y ( b ) = \beta :
$$

INPUTendpoints $a , b$ ; boundary conditions $\alpha , \beta$ ; integer $N \geq 2$

OUTPUTapproximations $w _ { i }$ t0 $y ( x _ { i } )$ for each $i = 0 , 1 , \ldots , N + 1$

$$
\begin{array} { l } { t h = ( b - a ) / ( N + 1 ) ; } \\ { \ x = a + h ; } \\ { a _ { 1 } = 2 + h ^ { 2 } q ( x ) ; } \\ { b _ { 1 } = - 1 + ( h / 2 ) p ( x ) ; } \\ { d _ { 1 } = - h ^ { 2 } r ( x ) + ( 1 + ( h / 2 ) p ( x ) ) \alpha . } \end{array}
$$

Step 2For $i = 2 , \ldots , N - 1$ set $x = a + i h$ ；$\begin{array} { l } { { a _ { i } = 2 + h ^ { 2 } q ( x ) ; } } \\ { { b _ { i } = - 1 + ( h / 2 ) p ( x ) ; } } \\ { { c _ { i } = - 1 - ( h / 2 ) p ( x ) ; } } \\ { { d _ { i } = - h ^ { 2 } r ( x ) . } } \end{array}$

Step3 Set $x = b - h$

$$
\begin{array} { l } { { a _ { N } = 2 + h ^ { 2 } q ( x ) ; } } \\ { { c _ { N } = - 1 - ( h / 2 ) p ( x ) ; } } \\ { { d _ { N } = - h ^ { 2 } r ( x ) + ( 1 - ( h / 2 ) p ( x ) ) \beta . } } \end{array}
$$

Step 4 Set $l _ { 1 } = a _ { 1 }$ ;  (Steps 4-8 solve a tridiagonal linear system using Algorithm 6.7.) $\begin{array} { l } { { u _ { 1 } = b _ { 1 } / a _ { 1 } ; } } \\ { { z _ { 1 } = d _ { 1 } / l _ { 1 } . } } \end{array}$

Step 5For $i = 2$ ,...,N -1 set

$$
\begin{array} { l } { { : l _ { i } = a _ { i } - c _ { i } u _ { i - 1 } ; } } \\ { { u _ { i } = b _ { i } / l _ { i } ; } } \\ { { z _ { i } = ( d _ { i } - c _ { i } z _ { i - 1 } ) / l _ { i } . } } \end{array}
$$

Step 6 Set $l _ { N } = a _ { N } - c _ { N } u _ { N - 1 }$

$$
z _ { N } = ( d _ { N } - c _ { N } z _ { N - 1 } ) / l _ { N } .
$$

Step 7 Set $w _ { 0 } = \alpha$

$$
\begin{array} { l } { { w _ { N + 1 } = \beta . } } \\ { { w _ { N } = z _ { N } . } } \end{array}
$$

Step 8For $i = N - 1 , \dots , 1$ set $w _ { i } = z _ { i } - u _ { i } w _ { i + 1 }$

Step 9For $i = 0$ ，..， $N + 1$ set $x = a + i h$ ； OUTPUT $( x , w _ { i } )$

Step 10 STOP.(The procedure is complete.)

Algorithm 11.3 willbe used to approximate the solution to the linear boundary-value problem

$$
y ^ { \prime \prime } = - \frac { 2 } { x } y ^ { \prime } + \frac { 2 } { x ^ { 2 } } y + \frac { \sin ( \ln x ) } { x ^ { 2 } } , \quad 1 \leq x \leq 2 , \quad y ( 1 ) = 1 , \quad y ( 2 ) = 2 ,
$$

which was also approximated by the Shooting method in Example 2 of Section 11.1. For this example, we will use $N = 9$ ， $\ s 0 \ h = 0 . 1$ , and we have the same spacing as in Example 2 of Section 11.1. The complete results are listed in Table 11.3 on page 664.

These results are considerably less accurate than those obtained in Example 2 of Section 11.1. This is because the method used in that example involved a Runge-Kutta technique with local truncation error of order $O ( h ^ { 4 } )$ ， whereas the difference method used here has local truncation error of order $O ( h ^ { 2 } )$ □

To obtain a diference method with greater accuracy， we can proceed in a number of ways. Using fifth-order Taylor series for approximating $y ^ { \prime \prime } ( x _ { i } )$ and $y ^ { \prime } ( x _ { i } )$ results in a truncation error term involving $h ^ { 4 }$ . However, this process requires using multiples not only of $y \left( x _ { i + 1 } \right)$ and $y ( x _ { i - 1 } )$ , but also of $y ( x _ { i + 2 } )$ and $y ( x _ { i - 2 } )$ in the approximation formulas for $y ^ { \prime \prime } ( x _ { i } )$ and $y ^ { \prime } ( x _ { i } )$ .This leads to difficulty at $i \ = 0$ and $i = N$ . Moreover, the resulting system of equations analogous to (11.19) is not in tridiagonal form, and the solution to the system requires many more calculations.

Table 11.3   

<table><tr><td>xi</td><td>Wi</td><td>y(xi)</td><td>w；-y(xi）</td></tr><tr><td>1.0</td><td>1.00000000</td><td>1.00000000</td><td></td></tr><tr><td>1.1</td><td>1.09260052</td><td>1.09262930</td><td>2.88× 10-5</td></tr><tr><td>1.2</td><td>1.18704313</td><td>1.18708484</td><td>4.17 × 10-5</td></tr><tr><td>1.3</td><td>1.28333687</td><td>1.28338236</td><td>4.55 × 10-5</td></tr><tr><td>1.4</td><td>1.38140205</td><td>1.38144595</td><td>4.39 × 10-5</td></tr><tr><td>1.5</td><td>1.48112026</td><td>1.48115942</td><td>3.92 × 10-5</td></tr><tr><td>1.6</td><td>1.58235990</td><td>1.58239246</td><td>3.26 × 10-5</td></tr><tr><td>1.7</td><td>1.68498902</td><td>1.68501396</td><td>2.49 × 10-5</td></tr><tr><td>1.8</td><td>1.78888175</td><td>1.78889853</td><td>1.68 × 10-5</td></tr><tr><td>1.9</td><td>1.89392110</td><td>1.89392951</td><td>8.41 × 10-6</td></tr><tr><td>2.0</td><td>2.00000000</td><td>2.00000000</td><td></td></tr></table>

Instead of attempting to obtain a difference method with a higher-order truncation error in this manner, it is generally more satisfactory to consider a reduction in step size. In addition, Richardson's extrapolation technique can be used effectively for this method since the error term is expressed in even powers of $h$ with coeficients independent of $h$ ， provided $y$ is sufficiently differentiable (see,for example,[Keller,H, p. 81]).

EXAMPLE 2 Applying Richardson's extrapolation to approximate the solution to the boundary-value problem

$$
y ^ { \prime \prime } = - \frac { 2 } { x } y ^ { \prime } + \frac { 2 } { x ^ { 2 } } y + \frac { \sin ( \ln x ) } { x ^ { 2 } } , \quad 1 \leq x \leq 2 , \quad y ( 1 ) = 1 , \quad y ( 2 ) = 2 ,
$$

with $h = 0 . 1$ ,0.05,and O.025,gives the results listed in Table 11.4.The first extrapolation is

Table 11.4   

<table><tr><td>xi</td><td>wi(h = 0.1)</td><td>wi(h = 0.05)</td><td>wi(h = 0.025)</td><td>Ext1i</td><td>Ext2i</td><td>Ext3i</td></tr><tr><td>1.0</td><td>1.00000000</td><td>1.00000000</td><td>1.00000000</td><td>1.00000000</td><td>1.00000000</td><td>1.00000000</td></tr><tr><td>1.1</td><td>1.09260052</td><td>1.09262207</td><td>1.09262749</td><td>1.09262925</td><td>1.09262930</td><td>1.09262930</td></tr><tr><td>1,2</td><td>1.18704313</td><td>1.18707436</td><td>1.18708222</td><td>1.18708477</td><td>1.18708484</td><td>1.18708484</td></tr><tr><td>1.3</td><td>1.28333687</td><td>1.28337094</td><td>1.28337950</td><td>1.28338230</td><td>1.28338236</td><td>1.28338236</td></tr><tr><td>1.4</td><td>1.38140205</td><td>1.38143493</td><td>1.38144319</td><td>1.38144589</td><td>1.38144595</td><td>1.38144595</td></tr><tr><td>1.5</td><td>1.48112026</td><td>1.48114959</td><td>1.48115696</td><td>1.48115937</td><td>1.48115941</td><td>1.48115942</td></tr><tr><td>1.6</td><td>1.58235990</td><td>1.58238429</td><td>1.58239042</td><td>1.58239242</td><td>1.58239246</td><td>1.58239246</td></tr><tr><td>1.7</td><td>1.68498902</td><td>1.68500770</td><td>1.68501240</td><td>1.68501393</td><td>1.68501396</td><td>1.68501396</td></tr><tr><td>1.8</td><td>1.78888175</td><td>1.78889432</td><td>1.78889748</td><td>1.78889852</td><td>1.78889853</td><td>1.78889853</td></tr><tr><td>1.9</td><td>1.89392110</td><td>1.89392740</td><td>1.89392898</td><td>1.89392950</td><td>1.89392951</td><td>1.89392951</td></tr><tr><td>2.0</td><td>2.00000000</td><td>2.00000000</td><td>2.00000000</td><td>2.00000000</td><td>2.00000000</td><td>2.00000000</td></tr></table>

$$
\mathtt { E x t } _ { 1 i } = \frac { 4 w _ { i } ( h = 0 . 0 5 ) - w _ { i } ( h = 0 . 1 ) } { 3 } ;
$$

the second extrapolation is

$$
\mathsf { E x t } _ { 2 i } = \frac { 4 w _ { i } ( h = 0 . 0 2 5 ) - w _ { i } ( h = 0 . 0 5 ) } { 3 } ;
$$

and the final extrapolation is

$$
\mathrm { E x t } _ { 3 i } = \frac { 1 6 \mathrm { E x t } _ { 2 i } - \mathrm { E x t } _ { 1 i } } { 1 5 } .
$$

All the results of ${ \mathrm { E x t } } _ { 3 i }$ are correct to the decimal places listed. In fact, if sufficient digits had been used, this approximation would agree with the exact solution with maximum error of $6 . 3 \times 1 0 ^ { - 1 1 }$ at the mesh points, an impressive improvement. □

# 1. The boundary-value problem

$$
y ^ { \prime \prime } = 4 ( y - x ) , \quad 0 \leq x \leq 1 , \quad y ( 0 ) = 0 , \quad y ( 1 ) = 2
$$

has the solution $y ( x ) = e ^ { 2 } ( e ^ { 4 } - 1 ) ^ { - 1 } ( e ^ { 2 x } - e ^ { - 2 x } ) + x$ . Use the Linear Finite-Difference Algorithm to approximate the solution, and compare the results to the actual solution.

a. With $\begin{array} { r } { h = { \frac { 1 } { 2 } } } \end{array}$ ; $\begin{array} { r } { \mathbf { b } . \quad \mathrm { W i t h } \ h = \frac { 1 } { 4 } . } \end{array}$ c. Use extrapolation to approximate $y ( 1 / 2 )$

2. The boundary-value problem

$$
\begin{array} { r } { y ^ { \prime \prime } = y ^ { \prime } + 2 y + \cos x , \quad 0 \leq x \leq \frac { \pi } { 2 } , \quad y ( 0 ) = - 0 . 3 , \quad y \left( \frac { \pi } { 2 } \right) = - 0 . 1 } \end{array}
$$

has the solution $y ( x ) = - { \textstyle { \frac { 1 } { 1 0 } } } ( \sin x + 3 \cos x )$ . Use the Linear Finite-Difference Algorithm to approximate the solution, and compare the results to the actual solution.

a. With $\begin{array} { r } { h = \frac { \pi } { 4 } } \end{array}$ ； $\begin{array} { r } { \mathbf { b } . \quad \mathrm { W i t h } \ : h = \frac { \pi } { 8 } . } \end{array}$   
c. Use extrapolation to approximate $y ( \pi / 4 )$ .

3.Use the Linear Finite-Difference Algorithm to approximate the solution to the following boundary-value problems.

a.y"= -3y′+2y+2x +3， $0 \leq x \leq 1 , y ( 0 ) = 2 , y ( 1 ) = 1 ; \mathrm { u s e } h = 0 . 1 .$ b. $\begin{array} { r } { y ^ { \prime \prime } = - \frac { 4 } { r } y ^ { \prime } + \frac { 2 } { r ^ { 2 } } y - \frac { 2 } { r ^ { 2 } } \ln x , \quad 1 \leq x \leq 2 , y ( 1 ) = - \frac { 1 } { 2 } , y ( 2 ) = \ln 2 ; \mathrm { u s e } \ h = 0 . 0 3 . } \end{array}$ c. $y ^ { \prime \prime } = - ( x + 1 ) y ^ { \prime } + 2 y + ( 1 - x ^ { 2 } ) e ^ { - x } , \quad 0 \leq x \leq 1 , y ( 0 ) = - 1 , y ( 1 ) = 0 ; { \mathrm { u s e ~ } } h = 0$ ， d. $\begin{array} { r } { y ^ { \prime \prime } = \frac { y ^ { \prime } } { x } + \frac { 3 } { x ^ { 2 } } y + \frac { \ln x } { x } - 1 , \quad 1 \leq x \leq 2 , y ( 1 ) = y ( 2 ) = 0 ; \mathrm { u s e } h = 0 . } \end{array}$

4.Although $q ( x ) < 0$ in the following boundary-value problems, unique solutions exist and are given. Use the Linear Finite-Difference Algorithm to approximate the solutions, and compare the results to the actual solutions.

a.y"+y=0，0≤x≤, $y ( 0 ) = 1$ ， $\begin{array} { r } { y ( \frac { \pi } { 4 } ) = 1 } \end{array}$ ; use $\begin{array} { r } { h = \frac { \pi } { 2 0 } } \end{array}$ ; actual solution $y ( x ) =$ cos x + (√2-1) sin x.

b.y"+4y = cosx，0≤x≤, $y ( 0 ) = 0$ ， $\begin{array} { r } { y ( \frac { \pi } { 4 } ) = 0 } \end{array}$ ; use $\begin{array} { r } { h \ = \ \frac { \pi } { 2 0 } } \end{array}$ ; actual solution $\begin{array} { r } { y ( x ) = - \frac { 1 } { 3 } \cos 2 x - \frac { \sqrt { 2 } } { 6 } \sin 2 x + \frac { 1 } { 3 } \cos x . } \end{array}$   
c. $\begin{array} { r } { y ^ { \prime \prime } = - { \frac { 4 } { x } } y ^ { \prime } - { \frac { 2 } { x ^ { 2 } } } y + { \frac { 2 \ln x } { x ^ { 2 } } } } \end{array}$ ， 1≤x≤2,y(1）=↓, $y ( 2 ) = \ln 2$ ; use $h = 0 . 0 5$ ; actual solution $y ( x ) = { \textstyle { \frac { 4 } { x } } } - { \frac { 2 } { x ^ { 2 } } } + \ln x - { \frac { 3 } { 2 } }$   
d. $y ^ { \prime \prime } = 2 y ^ { \prime } - y + x e ^ { x } - x$ ， $0 \leq x \leq 2 , y ( 0 ) = 0 , y ( 2 ) = - 4$ use $h = 0 . 2$ ; actual solution $\begin{array} { r } { y ( x ) = \frac { 1 } { 6 } x ^ { 3 } e ^ { x } - \frac { 5 } { 3 } x e ^ { x } + 2 e ^ { x } - x - 2 . } \end{array}$

5. Use the Linear Finite-Difference Algorithm to approximate the solution $\begin{array} { r } { y \ = \ e ^ { - 1 0 x } } \end{array}$ to the boundary-value problem

$$
y ^ { \prime \prime } = 1 0 0 y , \quad 0 \leq x \leq 1 , \quad y ( 0 ) = 1 , \quad y ( 1 ) = e ^ { - 1 0 } .
$$

Use $h = 0 . 1$ and 0.05. Can you explain the consequences?

.Repeat Exercise 3(a)and (b) using the extrapolation discussed in Example 2.

7.The lead example of this chapter concerned the deflection of a beam with supported ends subject to uniform loading. The boundary-value problem governing this physical situation is

$$
\frac { d ^ { 2 } w } { d x ^ { 2 } } = \frac { S } { E I } w + \frac { q x } { 2 E I } ( x - l ) , \quad 0 < x < l ,
$$

with boundary conditions $w ( 0 ) = 0$ and $w ( l ) = 0$

Suppose the beam is a W1O-type steel I-beam with the following characteristics: length $l = 1 2 0$ in., intensity of uniform load $q = 1 0 0$ Ib/ft,modulus of elasticity $E = 3 . 0 \times 1 0 ^ { 7 }$ Ib/in.2, stress at ends $S = 1 0 0 0 1 { \mathrm { b } }$ , and central moment of inertia $I = 6 2 5 \mathrm { i n } . ^ { 4 }$

a. Approximate the deflection $w ( x )$ of the beam every 6 in. b. The actual relationship is given by

$$
w ( x ) = c _ { 1 } e ^ { a x } + c _ { 2 } e ^ { - a x } + b ( x - l ) x + c ,
$$

where $c _ { 1 } = 7 . 7 0 4 2 5 3 7 \times 1 0 ^ { 4 }$ ， $c _ { 2 } = 7 . 9 2 0 7 4 6 2 \times 1 0 ^ { 4 }$ ， $a = 2 . 3 0 9 4 0 1 0 \times 1 0 ^ { - 4 }$ $b =$ $- 4 . 1 6 6 6 6 6 6 \times 1 0 ^ { - 3 }$ ,and $c = - 1 . 5 6 2 5 \times 1 0 ^ { 5 }$ . Is the maximum error on the interval within 0.2 in.?

c.State law requires that $\operatorname* { m a x } _ { 0 < x < l } w ( x ) < 1 / 3 0 0$ . Does this beam meet state code?

8.The deflection of a uniformly loaded, long rectangular plate under an axial tension force is governed by a second-order differential equation. Let $\boldsymbol { s }$ represent the axial force and $q$ the intensity of the uniform load. The deflection $W$ along the elemental length is given by

$$
W ^ { \prime \prime } ( x ) - \frac { S } { D } W ( x ) = \frac { - q l } { 2 D } x + \frac { q } { 2 D } x ^ { 2 } , \quad 0 \leq x \leq l , \ W ( 0 ) = W ( l ) = 0 ,
$$

where $l$ is the length of the plate and $D$ is the flexual rigidity of the plate. Let $q \ = \ 2 0 0$ 1b/in.2, $S = 1 0 0$ lb/in., $D = 8 . 8 \times 1 0 ^ { 7 }$ lb/in., and $l = 5 0$ in.Approximate the deflection at 1-in. intervals.

9.Prove Theorem 11.3.[Hint: To use Theorem 6.29,first show that $| { \frac { h } { 2 } } p ( x _ { i } ) \big | \ < \ 1$ implies that $\begin{array} { r } { \left| - 1 - \frac { \hbar } { 2 } p ( x _ { i } ) \right| + \left| - 1 + \frac { \hbar } { 2 } p ( x _ { i } ) \right| = 2 . ] } \end{array}$

10.Show that if $y \in C ^ { 6 } \{ a , b \}$ and if $w _ { 0 } , w _ { 1 } , \ldots , w _ { N + 1 }$ satisfy Eq. (11.18), then

$$
w _ { i } - y ( x _ { i } ) = A h ^ { 2 } + O ( h ^ { 4 } ) ,
$$

where $A$ is independent of $h$ , provided $q ( x ) \geq w > 0$ on $[ a , b ]$ for some $w$

# 11.4 Finite-Difference Methods for Nonlinear Problems

For the general nonlinear boundary-value problem

$$
y ^ { \prime \prime } = f ( x , y , y ^ { \prime } ) , \quad a \leq x \leq b , \quad y ( a ) = \alpha , \quad y ( b ) = \beta ,
$$

the difference method is similar to the method applied to linear problems in Section 11.3. Here, however, the system of equations willnot be linear,so an iterative process is required to solve it.

For the development of the procedure, we assume throughout that $f$ satisfies the following conditions:

1. $f$ and the partial derivatives $f _ { y }$ and $f _ { y ^ { \prime } }$ are all continuous on

$$
D = \{ ( x , y , y ^ { \prime } ) \mid a \leq x \leq b , \quad - \infty < y < \infty , - \infty < y ^ { \prime } < \infty \} ;
$$

2. $f _ { y } ( x , y , y ^ { \prime } ) \ge \delta$ on $D$ ,for some $\delta > 0$ ；

3.Constants $k$ and $L$ exist, with

$$
k = \operatorname* { m a x } _ { ( x , y , y ^ { \prime } ) \in D } | f _ { y } ( x , y , y ^ { \prime } ) | \quad \mathrm { a n d } \quad L = \operatorname* { m a x } _ { ( x , y , y ^ { \prime } ) \in D } | f _ { y ^ { \prime } } ( x , y , y ^ { \prime } ) | .
$$

This ensures, by Theorem 11.1, that a unique solution exists.

As in the linear case, we divide $[ a , b ]$ into $( N + 1 )$ equal subintervals whose endpoints are at $x _ { i } = a + i h$ ,for $i = 0$ ,1，..., $N + 1$ . Assuming that the exact solution has a bounded fourth derivative allows us to replace $y ^ { \prime \prime } ( x _ { i } )$ and $y ^ { \prime } ( x _ { i } )$ in each of the equations

$$
y ^ { \prime \prime } ( x _ { i } ) = f ( x _ { i } , y ( x _ { i } ) , y ^ { \prime } ( x _ { i } ) )
$$

by the appropriate centered-difference formula given in Eqs. (11.16) and (11.17). This gives, for each $i = 1 , 2 , \dots , N$ ，

$$
\frac { 1 ) - 2 y ( x _ { i } ) + y ( x _ { i - 1 } ) } { h ^ { 2 } } = f \bigg ( x _ { i } , y ( x _ { i } ) , \frac { y ( x _ { i + 1 } ) - y ( x _ { i - 1 } ) } { 2 h } - \frac { h ^ { 2 } } 6 y ^ { \prime \prime \prime } ( \eta _ { i } ) \bigg ) + \frac { h ^ { 2 } } { 1 2 } y ^ { ( 4 ) } ( \xi _ { i } ) ,
$$

for some $\xi _ { i }$ and $\eta _ { i }$ in the interval $( x _ { i - 1 } , x _ { i + 1 } )$

As in the linear case,the difference method results when the error terms are deleted and the boundary conditions are employed:

$$
w _ { 0 } = \alpha , \quad w _ { N + 1 } = \beta ,
$$

and

$$
- { \frac { w _ { i + 1 } - 2 w _ { i } + w _ { i - 1 } } { h ^ { 2 } } } + f \left( x _ { i } , w _ { i } , { \frac { w _ { i + 1 } - w _ { i - 1 } } { 2 h } } \right) = 0 ,
$$

for each $i = 1 , 2 , \dots , N$

The $N \times N$ nonlinear system obtained from this method,

$$
\begin{array} { r } { 2 w _ { 1 } - w _ { 2 } + h ^ { 2 } f \bigg ( x _ { 1 } , w _ { 1 } , \frac { w _ { 2 } - \alpha } { 2 h } \bigg ) - \alpha = 0 , } \\ { - w _ { 1 } + 2 w _ { 2 } - w _ { 3 } + h ^ { 2 } f \bigg ( x _ { 2 } , w _ { 2 } , \frac { w _ { 3 } - w _ { 1 } } { 2 h } \bigg ) = 0 , } \\ { \vdots } \\ { - w _ { N - 2 } + 2 w _ { N - 1 } - w _ { N } + h ^ { 2 } f \bigg ( x _ { N - 1 } , w _ { N - 1 } , \frac { w _ { N } - w _ { N - 2 } } { 2 h } \bigg ) = 0 , } \\ { - w _ { N - 1 } + 2 w _ { N } + h ^ { 2 } f \bigg ( x _ { N } , w _ { N } , \frac { \beta - w _ { N - 1 } } { 2 h } \bigg ) - \beta = 0 } \end{array}
$$

has a unique solution provided that $h < 2 / L$ , as shown in [Keller, H, p. 86].

We use Newton's method for nonlinear systems,discussed in Section 10.2, to ap-proximate the solution to this system. A sequence of iterates $\big \{ \big ( \boldsymbol { w } _ { 1 } ^ { ( k ) } , \boldsymbol { w } _ { 2 } ^ { ( k ) } , \ldots , \boldsymbol { w } _ { N } ^ { ( k ) } \big ) ^ { t } \big \}$ ）is $\big ( w _ { 1 } ^ { ( 0 ) } , w _ { 2 } ^ { ( 0 ) } , \dots , w _ { N } ^ { ( 0 ) } \big ) ^ { t }$ $( w _ { 1 } , w _ { 2 } , \dots , w _ { N } ) ^ { t }$ rand that the Jacobian matrix for the system is nonsingular.For system (11.2O), the Jacobian matrix $J ( w _ { 1 } , \dots , w _ { N } )$ is tridiagonal with $i j$ -th entry

$$
\begin{array} { r } { \langle - \boldsymbol { \textbf { \ i } } , w _ { N } \rangle _ { i j } = \left\{ \begin{array} { l l } { \displaystyle - 1 + \frac { h } { 2 } f _ { y ^ { \prime } } \left( x _ { i } , w _ { i } , \frac { w _ { i + 1 } - w _ { i - 1 } } { 2 h } \right) , } & { \mathrm { f o r } i = j - 1 \mathrm { ~ a n d ~ } j = 2 , \dots } \\ { \displaystyle 2 + h ^ { 2 } f _ { y } \left( x _ { i } , w _ { i } , \frac { w _ { i + 1 } - w _ { i - 1 } } { 2 h } \right) , } & { \mathrm { f o r } i = j \mathrm { ~ a n d ~ } j = 1 , \dots , N , } \\ { \displaystyle - 1 - \frac { h } { 2 } f _ { y ^ { \prime } } \left( x _ { i } , w _ { i } , \frac { w _ { i + 1 } - w _ { i - 1 } } { 2 h } \right) , } & { \mathrm { f o r ~ } i = j + 1 \mathrm { ~ a n d ~ } j = 1 , \dots } \end{array} \right. } \end{array}
$$

where $w _ { 0 } = \alpha$ and $w _ { N + 1 } = \beta$

Newton's method for nonlinear systems requires that at each iteration the $N \times N$ linear system

$$
\begin{array} { r l } & { J ( w _ { 1 } , \ldots , w _ { N } ) ( v _ { 1 } , \ldots , v _ { n } ) ^ { t } } \\ & { \qquad = - \bigg ( 2 w _ { 1 } - w _ { 2 } - \alpha + h ^ { 2 } f \left( x _ { 1 } , w _ { 1 } , \frac { w _ { 2 } - \alpha } { 2 h } \right) , } \\ & { \qquad - w _ { 1 } + 2 w _ { 2 } - w _ { 3 } + h ^ { 2 } f \left( x _ { 2 } , w _ { 2 } , \frac { w _ { 3 } - w _ { 1 } } { 2 h } \right) , \ldots , } \\ & { \qquad - w _ { N - 2 } + 2 w _ { N - 1 } - w _ { N } + h ^ { 2 } f \left( x _ { N - 1 } , w _ { N - 1 } , \frac { w _ { N } - w _ { N - 2 } } { 2 h } \right) , } \\ & { \qquad - w _ { N - 1 } + 2 w _ { N } + h ^ { 2 } f \left( x _ { N } , w _ { N } , \frac { \beta - w _ { N - 1 } } { 2 h } \right) - \beta \bigg ) ^ { t } } \end{array}
$$

be solved for $\upsilon _ { 1 } , \upsilon _ { 2 } , \ldots , \upsilon _ { N }$ , since

$$
{ w _ { i } ^ { ( k ) } = w _ { i } ^ { ( k - 1 ) } + v _ { i } , \quad \mathrm { f o r e a c h } i = 1 , 2 , \dots , N } .
$$

Since $J$ is tridiagonal,this is not as formidable a problem as it might at first appear. The Crout Factorization Algorithm (6.7) can be applied. The process is detailed in Algorithm 11.4.

# Nonlinear Finite-Difference

To approximate the solution to the nonlinear boundary-value problem

$$
y ^ { \prime \prime } = f ( x , y , y ^ { \prime } ) , \quad a \leq x \leq b , \quad y ( a ) = \alpha , \quad y ( b ) = \beta :
$$

INPUTendpoints $a , b$ ; boundary conditions $\alpha , \beta$ ; integer $N \geq 2$ ; tolerance TOL; maximum number of iterations $M$

OUTPUTapproximations $w _ { i }$ to $y ( x _ { i } )$ for each $i = 0 , 1 , \ldots , N + 1$ or a message that the maximum number of iterations was exceeded.

Step 1 Set $\begin{array} { r l } & { h = ( b - a ) / ( N + 1 ) ; } \\ & { w _ { 0 } = \alpha ; } \\ & { w _ { N + 1 } = \beta . } \end{array}$

$$
S t e p 2 \mathrm { F o r } i = 1 , \ldots , N \mathrm { s e t } w _ { i } = \alpha + i \left( \frac { \beta - \alpha } { b - a } \right) h .
$$

Step 3 Set $k = 1$

Step 4 While $k \leq M$ do Steps 5-16.

Step 5 Set $x = a + h$ ；$\begin{array} { r l } & { \ddot { } t = ( w _ { 2 } - \alpha ) / ( 2 h ) ; } \\ & { { a } _ { 1 } = 2 + h ^ { 2 } f _ { y } ( x , w _ { 1 } , t ) ; } \\ & { { b } _ { 1 } = - 1 + ( h / 2 ) f _ { y ^ { \prime } } ( x , w _ { 1 } , t ) ; } \\ & { { d } _ { 1 } = - \big ( 2 w _ { 1 } - w _ { 2 } - \alpha + h ^ { 2 } f ( x , w _ { 1 } , t ) \big ) . } \end{array}$

Step 6For $i = 2 , \ldots , N - 1$

$$
\begin{array} { r l } & { t = ( w _ { i + 1 } - w _ { i - 1 } ) / ( 2 h ) ; } \\ & { a _ { i } = 2 + h ^ { 2 } f _ { y } ( x , w _ { i } , t ) ; } \\ & { b _ { i } = - 1 + ( h / 2 ) f _ { y ^ { \prime } } ( x , w _ { i } , t ) ; } \\ & { c _ { i } = - 1 - ( h / 2 ) f _ { y ^ { \prime } } ( x , w _ { i } , t ) ; } \\ & { d _ { i } = - \big ( 2 w _ { i } - w _ { i + 1 } - w _ { i - 1 } + h ^ { 2 } f ( x , w _ { i } , t ) \big ) . } \end{array}
$$

Step 7 Set $x = b - h$

$$
\begin{array} { r l } & { t = ( \beta - w _ { N - 1 } ) / ( 2 h ) ; } \\ & { a _ { N } = 2 + h ^ { 2 } f _ { y } ( x , w _ { N } , t ) ; } \\ & { c _ { N } = - 1 - ( h / 2 ) f _ { y ^ { \prime } } ( x , w _ { N } , t ) ; } \\ & { d _ { N } = - \big ( 2 w _ { N } - w _ { N - 1 } - \beta + h ^ { 2 } f ( x , w _ { N } , t ) \big ) . } \end{array}
$$

Step 8 Set $l _ { 1 } = a _ { 1 }$ ； (Steps 8-12 solve $\pmb { a }$ tridiagonal linear system using Algorithm 6.7.)

$$
\begin{array} { r } { u _ { \mathrm { 1 } } = b _ { \mathrm { 1 } } / a _ { \mathrm { 1 } } ; } \\ { z _ { \mathrm { 1 } } = d _ { \mathrm { 1 } } / l _ { \mathrm { 1 } } . } \end{array}
$$

$$
\begin{array} { r l } { { S t e p ~ g } } & { { } { \mathrm { F o r } ~ i = 2 , \ldots , N - 1 ~ \mathrm { s e t } ~ l _ { i } = a _ { i } - c _ { i } u _ { i - 1 } ; } } \\ { { } } & { { } { u _ { i } = b _ { i } / l _ { i } ; } } \\ { { } } & { { } { z _ { i } = ( d _ { i } - c _ { i } z _ { i - 1 } ) / l _ { i } . } } \end{array}
$$

Step 10 Set $l _ { N } = a _ { N } - c _ { N } u _ { N - 1 }$

$$
z _ { N } = ( d _ { N } - c _ { N } z _ { N - 1 } ) / l _ { N } .
$$

Step 11 Set $v _ { N } = z _ { N }$

$$
w _ { N } = w _ { N } + v _ { N } .
$$

Step 12 Fori = N-1,...,1 set $\boldsymbol { v } _ { i } = z _ { i } - u _ { i } \boldsymbol { v } _ { i + 1 } ;$

$$
w _ { i } = w _ { i } + v _ { i } .
$$

Step 13If $\| \mathbf { v } \| \leq T O L$ then do Steps 14 and 15.

Step 14 For $i = 0$ ，..， $N + 1$ set $x = a + i h$ ； OUTPUT $( x , w _ { i } )$

Step 15STOP. (The procedure was successful.)

Step 16 Set $k = k + 1$

Step 17OUTPUT('Maximum number of iterations exceeded'); (The procedure was unsuccessful.) STOP.

It can be shown (see [IK, p. 433]) that this Nonlinear Finite-Difference method is of order $O ( h ^ { 2 } )$

Since a good initial approximation is required when the satisfaction of conditions (1), (2),and (3) given at the beginning of this presentation cannot be verified,an upper bound for the number of iterations should be specified and, if exceeded,a new initial approximation or areduction in step size considered.The initial approximations ${ w _ { i } ^ { ( 0 ) } }$ to $w _ { i }$ , for each $i = 1 , 2 , \dots , N$ ,are obtained in Step 2 by passing a straight line through $( a , a )$ and $( b , \beta )$ and evaluating at $x _ { i }$

EXAMPLE 1 We apply Algorithm 11.4, with $h = 0 . 1$ , to the nonlinear boundary-value problem

$$
y ^ { \prime \prime } = { \frac { 1 } { 8 } } ( 3 2 + 2 x ^ { 3 } - y y ^ { \prime } ) , \quad 1 \leq x \leq 3 , \quad y ( 1 ) = 1 7 , \quad y ( 3 ) = { \frac { 4 3 } { 3 } } ,
$$

giving the results in Table 11.5. The stopping procedure used in this example was to iterate until values of successive iterates differed by less than $1 0 ^ { - 8 }$ . This was accomplished with four iterations.The problem in this example is the same as that considered for the Nonlinear Shooting method, Example 1 of Section 11.2.

Richardson's extrapolation procedure can also be used for the Nonlinear Finite-Difference method. Table 11.6 lists the results when this method is applied to our example using $h = 0 . 1$ , 0.05,and 0.O25,with four iterations in each case. The notation is the same as in Example 2 of Section 11.3,and the values of $\mathbf { E x t } _ { 3 i }$ are all accurate to the places listed, with an actual maximum error of $3 . 6 8 \times 1 0 ^ { - 1 0 }$ . The values of ${ w _ { i } } ( h = 0 . 1 )$ are omitted from the table, since they were listed previously.

Table 11.5   

<table><tr><td>Xi</td><td>Wi</td><td>y(xi)</td><td>|wi-y(xi）l</td></tr><tr><td>1.0</td><td>17.000000</td><td>17.000000</td><td></td></tr><tr><td>1.1</td><td>15.754503</td><td>15.755455</td><td>9.520 × 10-4</td></tr><tr><td>1.2</td><td>14.771740</td><td>14.773333</td><td>1.594 × 10-3</td></tr><tr><td>1.3</td><td>13.995677</td><td>13.997692</td><td>2.015 × 10-3</td></tr><tr><td>1.4</td><td>13.386297</td><td>13.388571</td><td>2.275 × 10-3</td></tr><tr><td>1.5</td><td>12.914252</td><td>12.916667</td><td>2.414×10-3</td></tr><tr><td>1.6</td><td>12.557538</td><td>12.560000</td><td>2.462 × 10-3</td></tr><tr><td>1.7</td><td>12.299326</td><td>12.301765</td><td>2.438 × 10-3</td></tr><tr><td>1.8</td><td>12.126529</td><td>12.128889</td><td>2.360 ×10-3</td></tr><tr><td>1.9</td><td>12.028814</td><td>12.031053</td><td>2.239 × 10-3</td></tr><tr><td>2.0</td><td>11.997915</td><td>12.000000</td><td>2.085 × 10-3</td></tr><tr><td>2.1</td><td>12.027142</td><td>12.029048</td><td>1.905 × 10-3</td></tr><tr><td>2.2</td><td>12.111020</td><td>12.112727</td><td>1.707 × 10-3</td></tr><tr><td>2.3</td><td>12.245025</td><td>12.246522</td><td>1.497 × 10-3</td></tr><tr><td>2.4</td><td>12.425388</td><td>12.426667</td><td>1.278 × 10-3</td></tr><tr><td>2.5</td><td>12.648944</td><td>12.650000</td><td>1.056 10-3 ×</td></tr><tr><td>2.6</td><td>12.913013</td><td>12.913846</td><td>8.335 × 10-4</td></tr><tr><td>2.7</td><td>13.215312</td><td>13.215926</td><td>6.142 × 10-4</td></tr><tr><td>2.8</td><td>13.553885</td><td>13.554286</td><td>4.006 × 10-4</td></tr><tr><td>2.9</td><td>13.927046</td><td>13.927241</td><td>1.953× 10-4</td></tr><tr><td>3.0</td><td>14.333333</td><td>14.333333</td><td></td></tr></table>

Table 11.6   

<table><tr><td>xi</td><td>wi(h = 0.05)</td><td>wi(h = 0.025)</td><td>Ext1i</td><td>Ext2i</td><td>Ext3i</td></tr><tr><td>1.0</td><td>17.00000000</td><td>17.00000000</td><td>17.00000000</td><td>17.00000000</td><td>17.00000000</td></tr><tr><td>1.1</td><td>15.75521721</td><td>15.75539525</td><td>15.75545543</td><td>15.75545460</td><td>15.75545455</td></tr><tr><td>1.2</td><td>14.77293601</td><td>14.77323407</td><td>14.77333479</td><td>14.77333342</td><td>14.77333333</td></tr><tr><td>1.3</td><td>13,99718996</td><td>13.99756690</td><td>13.99769413</td><td>13.99769242</td><td>13.99769231</td></tr><tr><td>1.4</td><td>13.38800424</td><td>13.38842973</td><td>13.38857346</td><td>13.38857156</td><td>13.38857143</td></tr><tr><td>1.5</td><td>12.91606471</td><td>12.91651628</td><td>12.91666881</td><td>12.91666680</td><td>12.91666667</td></tr><tr><td>1.6</td><td>12.55938618</td><td>12.55984665</td><td>12.56000217</td><td>12.56000014</td><td>12.56000000</td></tr><tr><td>1.7</td><td>12.30115670</td><td>12.30161280</td><td>12.30176684</td><td>12.30176484</td><td>12.30176471</td></tr><tr><td>1.8</td><td>12.12830042</td><td>12.12874287</td><td>12.12899094</td><td>12.12888902</td><td>12.12888889</td></tr><tr><td>1.9</td><td>12.03049438</td><td>12.03091316</td><td>12.03105457</td><td>12.03105275</td><td>12.03105263</td></tr><tr><td>2.0</td><td>11.99948020</td><td>11.99987013</td><td>12.00000179</td><td>12.00000011</td><td>12.00000000</td></tr><tr><td>2.1</td><td>12.02857252</td><td>12.02892892</td><td>12.02902924</td><td>12.02904772</td><td>12.02904762</td></tr><tr><td>2.2</td><td>12.11230149</td><td>12.11262089</td><td>12.11272872</td><td>12.11272736</td><td>12.11272727</td></tr><tr><td>2.3</td><td>12.24614846</td><td>12.24642848</td><td>12.24652299</td><td>12.24652182</td><td>12.24652174</td></tr><tr><td>2.4</td><td>12.42634789</td><td>12.42658702</td><td>12.42666773</td><td>12.42666673</td><td>12.42666667</td></tr><tr><td>2.5</td><td>12.64973666</td><td>12.64993420</td><td>12.65000086</td><td>12.65000005</td><td>12.65000000</td></tr><tr><td>2.6</td><td>12.91362828</td><td>12.91379422</td><td>12.91384683</td><td>12.91384620</td><td>12.91384615</td></tr><tr><td>2.7</td><td>13.21577275</td><td>13.21588765</td><td>13.21592641</td><td>13.21592596</td><td>13.21592593</td></tr><tr><td>2.8</td><td>13.55418579</td><td>13.55426075</td><td>13.55428603</td><td>13.55428573</td><td>13.55428571</td></tr><tr><td>2.9</td><td>13.92719268</td><td>13.92722921</td><td>13.92724153</td><td>13.92724139</td><td>13.92724138</td></tr><tr><td>3.0</td><td>14.33333333</td><td>14.33333333</td><td>14.33333333</td><td>14.33333333</td><td>14.33333333</td></tr></table>