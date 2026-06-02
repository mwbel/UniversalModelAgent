Chapter 8

# Nonlinear Least Squares Problems

Anyone who deals with nonlinear problems knows that everything works sometimes and nothing works every time.   
John E.Dennis, Jr.

# 8.1 - Newton-Type Methods

# 8.1.1 - Vector Space Calculus

Consider a function $f \colon X \ \to \ Y$ ，where $X$ and $Y$ are normed vector spaces. The function is continuous at the point $x _ { 0 } \in X$ if $\| f ( x ) - f ( x _ { 0 } ) \| \to 0$ as $x  x _ { 0 }$ . It satisfies a Lipschitz condition in a domain $D \subset X$ if a constant $\alpha$ ,called a Lipschitz constant, can be chosen so that

$$
\| f ( x ) - f ( y ) \| \leq \alpha \| x - y \|
$$

for all points $x$ ， $y \in D$ . The function $f$ is differentiable at $x _ { 0 }$ , in the sense of Fréchet,if there exists a linear mapping $A$ such that

$$
\| f ( x ) - f ( x _ { 0 } ) - A ( x - x _ { 0 } ) \| = o ( \| x - x _ { 0 } \| ) , \quad x \to x _ { 0 } .
$$

This linear mapping is called the Fréchet derivative of $f$ at $x _ { 0 }$ ， and we write $A = f ( x _ { 0 } )$ or $A = f _ { x } ( x _ { 0 } )$ . Similar definitions apply to infinite-dimensional spaces.In the finite-dimensional case,the Fréchet derivative is represented by the Jacobian, a matrix whose elements are the partial derivatives $\partial f ^ { i } / \partial x _ { j }$ .If vector-matrix notation is used, it is important to note that the derivative $g ^ { \prime }$ of a real-valued function $g$ is a row vector, because

$$
g ( x ) = g ( x _ { 0 } ) + g ^ { \prime } ( x _ { 0 } ) ( x - x _ { 0 } ) + o ( \| x - x _ { 0 } \| ) .
$$

The transpose of $g ^ { \prime } ( x )$ is called the gradient,or grad $g$

Many results from elementary calculus carry over to vector space calculus, such as the rules for the differentiation of products. The proofs are in principle the same. If $z = f ( x , y )$ with $\boldsymbol { x } \in \mathbb { R } ^ { k }$ ， $\boldsymbol { y } \in \mathbb { R } ^ { \ell }$ ， $z \in \mathbb { R } ^ { m }$ , then the partial derivatives $f _ { x } = \partial f / \partial x$ ， $f _ { y } = \partial f / \partial y$ with respect to the vectors $x , y$ are defined by the differential formula

$$
d z = f _ { x } d x + f _ { y } d y \quad \forall d x \in \mathbb { R } ^ { k } , \quad d y \in \mathbb { R } ^ { \ell } .
$$

If $x$ and $y$ are functions of $s \in \mathbb { R } ^ { n }$ , then a general version of the chain rule reads

$$
f ^ { \prime } ( x ( s ) , y ( s ) ) = f _ { x } x ^ { \prime } ( s ) + f _ { y } y ^ { \prime } ( s ) ,
$$

where $f ^ { \prime }$ denotes the first derivative. It can be derived in the same way as for real-valued variables,and the extension to longer chains is straightforward.

Let $f \colon \mathbb { R } ^ { k } \ \to \ \mathbb { R } ^ { k } , \ k > \ 1$ ,be a function,and consider the equation $x = f ( y )$ . By formal differentiation, $d x = f ^ { \prime } ( y ) d y$ ，and we obtain $d y = \left( f ^ { \prime } ( y ) \right) ^ { - 1 } d x$ ，provided that the Jacobian matrix $f ^ { \prime } ( y )$ with elements $( \partial x _ { i } / \partial y _ { j } )$ ， $1 \leq i , j \leq k$ ,is nonsingular. If $f ( x , y ) = 0$ ,then by (8.1.2), $f _ { x } d x + f _ { y } d y = 0$ If $f _ { y } ( x _ { 0 } , y _ { 0 } )$ is a nonsingular matrix, then $y$ becomes, under certain additional conditions,a differentiable function of $x$ in a neighborhood of $( x _ { 0 } , y _ { 0 } )$ , and we obtain $d y = - ( f _ { y } ) ^ { - 1 } f _ { x } d x$ ;hence

$$
y ^ { \prime } ( x ) = - ( f _ { y } ) ^ { - 1 } f _ { x } | _ { y = y ( x ) } .
$$

One can also show that

$$
\operatorname* { l i m } _ { \epsilon \to + 0 } { \frac { f ( x _ { 0 } + \epsilon v ) - f ( x _ { 0 } ) } { \epsilon } } = f ^ { \prime } ( x _ { 0 } ) v .
$$

There are,however, functions $f$ for which such a directional derivative exists for any $v$ ,but $f$ is not a linear function of $v$ for some $x _ { 0 }$ . An important example is $f ( x ) = \| x \| _ { \infty }$ ，where $x \in \mathbb { R } ^ { n }$ (Look at the case $n = 2 .$ ）

Consider the set of $k$ -linear mappings from vector spaces $X _ { i } = X$ ， $i = 1 , \ldots , k$ ,which we also write as $X ^ { k }$ ,to $Y$ . This is itself a linear space,which we here denote by $L _ { k } ( X , Y )$ .For $k = 1$ we write it more briefly as $L ( X , Y )$ .If $f ^ { \prime } ( x )$ is a differentiable function of $x$ at the point $x _ { 0 }$ , its derivative is denoted by $f ^ { \prime \prime } ( x _ { 0 } )$ . This is a linear function that maps $X$ into the space $L ( X , Y )$ of mappings from $X$ to $Y$ that contains $f ^ { \prime \prime } ( x _ { 0 } )$ ,i.e., $f ^ { \prime \prime } ( x _ { 0 } ) \in L ( X , L ( X , Y ) )$ . This space may be identified in a natural way with the space $L _ { 2 } ( X , Y )$ of bilinear mappings $X ^ { 2 }  Y$ If $A \in L ( X , L ( X , Y ) )$ , then the corresponding $\bar { A } \in L _ { 2 } ( X , Y )$ is defined by $( A u ) v = \bar { A } ( u , v )$ for all $u , v \in X$ . In the following it is not necessary to distinguish between $A$ and $\bar { A }$ ,S0

$$
f ^ { \prime \prime } ( x _ { 0 } ) ( u , v ) \in Y , \qquad f ^ { \prime \prime } ( x _ { 0 } ) u \in L ( X , Y ) , \qquad f ^ { \prime \prime } ( x _ { 0 } ) \in L _ { 2 } ( X , Y ) .
$$

It can be shown that $f ^ { \prime \prime } ( x _ { 0 } )$ ： $X ^ { 2 }  Y$ is a symmetric bilinear mapping, i.e, $f ^ { \prime \prime } ( x _ { 0 } ) ( u , v ) =$ $f ^ { \prime \prime } ( x _ { 0 } ) ( v , u )$ . The second-order partial derivatives are denoted $f _ { x x } , f _ { x y } , f _ { y x } , f _ { y y }$ We can show that $f _ { x y } = f _ { y x }$

If $X = \mathbb { R } ^ { n }$ ， $Y = \mathbb { R } ^ { m }$ ， $m > 1$ ，then $f ^ { \prime \prime } ( x _ { 0 } )$ reads $f _ { i j } ^ { p } ( x _ { 0 } ) = f _ { j i } ^ { p } ( x _ { 0 } )$ in tensor notation. It is thus characterized by a three-dimensional array, which one rarely needs to store or write. Fortunately,most of the numerical work can be done on a lower level,e.g.,with directional derivatives.For each fixed value of $p$ ，we obtain a symmetric $n \times n$ matrix $H ( x _ { 0 } )$ called the Hessian matrix; note that $f ^ { \prime \prime } ( x _ { 0 } ) ( u , v ) = u ^ { T } H ( x _ { 0 } ) v$ . The Hessian can be looked upon as the derivative of the gradient. An element of the Hessian is, in multilinear mapping notation, the $p$ th coordinate of the vector $f ^ { \prime \prime } ( x _ { 0 } ) ( e _ { i } , e _ { j } )$

Higher derivatives are recursively defined. If $f ^ { ( k - 1 ) } ( x )$ is differentiable at $x _ { 0 }$ , its derivative at $x _ { 0 }$ is denoted by $f ^ { ( k ) } ( x _ { 0 } )$ and called the $k$ th derivative of $f$ at $x _ { 0 }$ . One can show that $f ^ { ( k ) } ( x _ { 0 } ) :$ $X ^ { k }  Y$ is a symmetric $k$ -linear mapping. Taylor's formula then reads,when $a$ ， $u \in X$ ， $f : X \to Y$ ，

$$
\begin{array} { c } { { f ( a + u ) = f ( a ) + f ^ { \prime } ( a ) u + \displaystyle \frac { 1 } { 2 } f ^ { \prime \prime } ( a ) u ^ { 2 } + \cdots + \displaystyle \frac { 1 } { k ! } f ^ { ( k ) } ( a ) u ^ { k } + R _ { k + 1 } , } } \\ { { R _ { k + 1 } = \displaystyle \int _ { 0 } ^ { 1 } \displaystyle \frac { ( 1 - t ) ^ { k } } { k ! } f ^ { ( k + 1 ) } ( a + u t ) d t u ^ { k + 1 } . } } \end{array}
$$

Here we have used $u ^ { 2 } , u ^ { k } , \ldots$ as abbreviations for the lists ofinput vectors $( u , u ) , ( u , u , \dots , u )$ ..., etc. It follows that

$$
\left\| { R _ { k + 1 } } \right\| \le \operatorname* { m a x } _ { 0 \le t \le 1 } \left\| { f ^ { ( k + 1 ) } ( a + u t ) } \right\| \frac { \| u \| ^ { k + 1 } } { ( k + 1 ) ! } ,
$$

where norms of multilinear operators are defined analogously to subordinate matrix norms; see (4.3.37). Such simplifications are often convenient to use.The mean value theorem of differential calculus and Lagrange's form for the remainder of Taylor's formula do not hold,but in many places they can be replaced by the above integral form of the remainder. Allthis holds in complex vector spaces too.

# 8.1.2 - The Gauss-Newton Method

The unconstrained nonlinear least squares (NLS) problem is to find a global minimizer of

$$
\phi ( x ) = \frac 1 2 \sum _ { i = 1 } ^ { m } f _ { i } ^ { 2 } ( x ) = \frac 1 2 f ( x ) ^ { T } f ( x ) , \quad m \ge n ,
$$

where $f ( x ) \in \mathbb { R } ^ { m }$ and $x \in \mathbb { R } ^ { n }$ . Such problems arise, e.g.， when fiting given data $( y _ { i } , t _ { i } )$ ， $i = 1 , \ldots , m$ ，to a nonlinear model function $g ( x , t )$ .If only $y _ { i }$ are subject to errors,and the values $t _ { i }$ of the independent variable $t$ are exact, we take

$$
f _ { i } ( x ) = y _ { i } - g ( x , t _ { i } ) , \quad i = 1 , \ldots , m .
$$

The choice of the least squares measure is justified here,as for the linear case,by statistical considerations; see Bard [66,1974]. The case when there are errors in both $y _ { i }$ and $t _ { i }$ is discussed in Section 8.2.3.

The NLS problem (8.1.4) is a special case of the general unconstrained optimization problem in $\mathbb { R } ^ { n }$ . Although $\phi ( x )$ is bounded below, it is usually convex only near a local minimum. Hence, solution methods willin general not be globally convergent. The methods are iterative in nature. Starting from an initial guess $x _ { 0 }$ ，a sequence of approximations $x _ { 1 } , x _ { 2 } , \dotsc$ is generated that ideally converges to a solution. Each iteration step usually requires the solution of a related linear or quadratic subproblem.

In the following we assume that $f ( x )$ is twice continuously differentiable. Because of the special structure of $\phi ( x )$ in (8.1.4), the gradient $\nabla \phi ( x )$ of $\phi ( x )$ has the special structure

$$
\nabla \phi ( x ) = ( \partial \phi / \partial x _ { 1 } , \ldots , \partial \phi / \partial x _ { n } ) ^ { T } = J ( x ) ^ { T } f ( x ) ,
$$

where $J ( \boldsymbol { x } ) \in \mathbb { R } ^ { m \times n }$ is the Jacobian of $f ( x )$ with elements $( \partial f _ { i } ( x ) / \partial x _ { j } \partial x _ { k } )$ . Furthermore, the Hessian of $\phi ( x )$ is

$$
\nabla ^ { 2 } \phi ( x ) = J ( x ) ^ { T } J ( x ) + G ( x ) , \quad G ( x ) = \sum _ { i = 1 } ^ { m } f _ { i } ( x ) G _ { i } ( x ) ,
$$

where $G _ { i } ( x ) \in \mathbb { R } ^ { n \times n }$ ， $i = 1 , \ldots , n$ , is the Hessian of $f _ { i } ( x )$ , i.e., the symmetric matrix with elements $\left( \partial ^ { 2 } f _ { i } ( x ) / \partial x _ { j } \partial x _ { k } \right)$

A necessary condition for $x ^ { * }$ to be a local minimum of $f ( x )$ is that $\nabla \phi ( x ^ { * } ) = J ( x ^ { * } ) ^ { T } f ( x ^ { * } )$ $= 0$ . Such a point $x ^ { * }$ is called a critical point. Finding a critical point is equivalent to solving the system of nonlinear algebraic equations

$$
F ( x ) \equiv J ( x ) ^ { T } f ( x ) = 0 .
$$

The basic method for solving such a system is Newton's method for nonlinear equations:

$$
F ^ { \prime } ( x _ { k } ) p _ { k } = - F ( x _ { k } ) , \quad x _ { k + 1 } = x _ { k } + p _ { k } .
$$

Newton's method can atain a quadratic rate of convergence and is invariant under a linear transformation of variables $x = S z$ ； see Dennis and Schnabel [316,1996]).With $F ( x )$ given by (8.1.8), $p _ { k }$ solves

$$
\bigl ( J ( x _ { k } ) ^ { T } J ( x _ { k } ) + G ( x _ { k } ) \bigr ) p = - J ( x _ { k } ) ^ { T } f ( x _ { k } ) .
$$

The method can also be derived by using a quadratic approximation for the function $\phi ( x ) = $ $\textstyle { \frac { 1 } { 2 } } \parallel f ( x ) \parallel _ { 2 } ^ { 2 }$ and taking $p _ { k }$ as the minimizer of

$$
\phi _ { k } ( x _ { k } + p ) = \phi ( x _ { k } ) + \nabla \phi ( x _ { k } ) ^ { T } p + \frac { 1 } { 2 } p ^ { T } \nabla ^ { 2 } \phi ( x _ { k } ) p .
$$

This is Newton's method for unconstrained optimization. It has several atractive properties. In particular,if the Hessian $\nabla ^ { 2 } f ( x )$ is positive definite at $x _ { k }$ , then $p _ { k }$ is a descent direction for $\phi ( x )$

Newton's method is seldom used for NLS because the $m n ^ { 2 }$ second derivatives in the term $G ( x _ { k } )$ in (8.1.1O) are rarely available at a reasonable cost. An exception is in curve-fitting problems where the function values $f _ { i } ( x ) = y _ { i } - g ( x , t _ { i } )$ and derivatives can be obtained from the single function $g ( x , t )$ . If $g ( x , t )$ is composed of simple exponential and trigonometric functions, for example, then second derivatives can sometimes be computed cheaply.

In the Gauss-Newton method, $f ( x )$ is approximated in a neighborhood of $x _ { k }$ by the linear function $f ( x ) = f ( x _ { k } ) + J ( x _ { k } ) ( x - x _ { k } )$ . Then the condition that $x$ be a critical point can be written

$$
J ( x _ { k } ) ^ { T } ( f ( x _ { k } ) + J ( x _ { k } ) ( x - x _ { k } ) ) = 0 .
$$

The next approximation is taken as $x _ { k + 1 } = x _ { k } + p _ { k }$ ，where $p _ { k }$ solves the linear least squares problem

$$
\operatorname* { m i n } _ { \boldsymbol { p } } \| \boldsymbol { f } ( \boldsymbol { x } _ { k } ) + \boldsymbol { J } ( \boldsymbol { x } _ { k } ) \boldsymbol { p } \| _ { 2 } .
$$

f $J ( x _ { k } )$ has full column rank, then $p _ { k }$ is uniquely determined by the condition

$$
J ( x _ { k } ) ^ { T } ( J ( x _ { k } ) p _ { k } + f ( x _ { k } ) ) = 0 .
$$

If $x _ { k }$ is not a critical point, then $p _ { k } = - J ( x _ { k } ) ^ { \dagger } f ( x _ { k } )$ is a descent direction. Then,for sufficiently small $\tau > 0 , \| f ( x _ { k } + \alpha p _ { k } ) \| _ { 2 } < \| f ( x _ { k } ) \| _ { 2 }$ .To verify this, note that

$$
\| f ( x _ { k } + \alpha p _ { k } ) \| _ { 2 } ^ { 2 } = \| f ( x _ { k } ) \| _ { 2 } ^ { 2 } - 2 \alpha \| P _ { J _ { k } } f ( x _ { k } ) \| _ { 2 } ^ { 2 } + { \cal O } ( \alpha ^ { 2 } ) ,
$$

where $P _ { J _ { k } } = J ( x _ { k } ) J ^ { \dagger } ( x _ { k } )$ is the orthogonal projector onto the range of $J ( x _ { k } )$ . Moreover, since $x _ { k }$ is not a critical point, it follows that $P _ { J _ { k } } f ( x _ { k } ) \neq 0$

As the following simple example shows, the Gauss-Newton method may not be locally convergent. Consider minimizing $f _ { 1 } ^ { 2 } ( x ) + f _ { 2 } ^ { 2 } ( x )$ ,where

$$
f _ { 1 } ( x ) = x + 1 , \qquad f _ { 2 } ( x ) = \lambda x ^ { 2 } + x - 1 ,
$$

and $\lambda$ is a parameter. The minimizer is $x ^ { * } = 0$ . The Gauss-Newton method gives $x _ { k + 1 } =$ $\lambda x _ { k } + 0 ( x _ { k } ^ { 2 } )$ . Hence this method diverges when $| \lambda | > 1$ . To ensure global convergence, Newton's method can be used with a line search: $x _ { k + 1 } = x _ { k } + \alpha _ { k } p _ { k }$ ,where $p _ { k }$ is the Newton step (8.1.10).

The Gauss-Newton method is first-order invariant under a change of parametrization of the least squares problem

$$
\operatorname* { m i n } _ { z \in \mathbb { R } ^ { n } } \frac { 1 } { 2 } \| f ( x ( z ) ) \| _ { 2 } ^ { 2 } ,
$$

where $z$ is a function from $\mathcal { R } ^ { n }$ to $\mathcal { R } ^ { n }$ with a nonsingular Jacobian. To verify this property, note that if $p _ { x } = - J ^ { \dagger } ( x ) f ( x )$ is the Gauss-Newton step in the original variables, then $p _ { z } =$

$( J ( x ) x ^ { \prime } ) ^ { \dagger } f ( x )$ is the step after the change of variables, where $x ^ { \prime }$ is the Jacobian of $x ( z )$ . Then $p _ { x } = x ^ { \prime } p _ { z }$ ,which is the desired relation.

The Gauss-Newton method can also be thought of as arising from neglecting the term $G ( x )$ in Newton's method (8.1.1O). This term is small if the quantities

$$
| f _ { i } ( x _ { k } ) | \| G _ { i } ( x _ { k } ) \| , \quad i = 1 , \ldots , m ,
$$

are small, i.e., if either the residuals $f _ { i } ( x _ { k } )$ ， $i = 1 , \ldots , m$ ，are small or $f _ { i } ( x )$ is only mildly nonlinear at $x _ { k }$ . In this case the behavior of the Gauss-Newton method can be expected to be similar to that of Newton's method.

The Gauss-Newton method can be written as a fixed-point iteration

$$
x _ { k + 1 } = F ( x _ { k } ) , \quad F ( x ) = x - J ( x ) ^ { \dagger } f ( x ) .
$$

Assume there exists an $x ^ { * }$ such that $J ( x ^ { * } ) ^ { T } f ( x ^ { * } ) = 0$ and $J ( x ^ { * } )$ has full column rank. Then

$$
F ( x ) = x - ( J ( x ) ^ { T } J ( x ) ) ^ { - 1 } J ( x ) ^ { T } f ( x ) ,
$$

and using the chain rule gives

$$
\frac { \partial F } { \partial x _ { i } } = I - ( J ^ { T } J ) ^ { - 1 } J ^ { T } \frac { \partial f } { \partial x _ { i } } - ( J ^ { T } J ) ^ { - 1 } \frac { \partial } { \partial x _ { i } } ( J ^ { T } ) f - \frac { \partial } { \partial x _ { i } } ( ( J ^ { T } J ) ^ { - 1 } ) J ^ { T } f ,
$$

$i = 1 , \ldots , n$ Here the second and third terms cancel,and the last term vanishes at $x ^ { * }$ because $J ( x ^ { * } ) ^ { T } f ( x ^ { * } ) = 0$ .We obtain

$$
\nabla F ( x ^ { * } ) = - ( J ( x ^ { * } ) ^ { T } J ( x ^ { * } ) ) ^ { - 1 } \sum _ { i = 1 } ^ { m } f _ { i } ( x ^ { * } ) G _ { i } ( x ^ { * } ) .
$$

Sufficient conditions for local convergence and error bounds for the Gauss-Newton method can be obtained from Ostrowski's fixed-point theorem; see Pereyra [890,1967l, Ortega and Rheinboldt [845,20oo,Theorem 10.1.3],and Dennis and Schnabel [316,1996, Theorem 10.2.1].

Theorem 8.1.1. Let $f ( x )$ be a twice continuously Fréchet differentiable function. Assume there exists $x ^ { * }$ such that $J ( x ^ { * } ) ^ { T } f ( x ^ { * } ) = 0$ and the Jacobian $J ( x ^ { * } )$ has full rank. Then the Gauss-Newton iteration converges locally to $x ^ { * }$ if the spectral radius

$$
\rho = \rho ( \nabla F ( x ^ { * } ) ) < 1 .
$$

The asymptotic convergence is linear with rate bounded by $\rho$ In particular, the local convergence rate is superlinear if $f ( x ^ { * } ) = 0$

Wedin [1107,1972] gives a geometrical interpretation of this convergence result. Minimizing $\begin{array} { r } { \phi ( x ) = \frac { 1 } { 2 } \| f ( x ) \| _ { 2 } ^ { 2 } } \end{array}$ is equivalent to finding a point on the $n$ -dimensional surface $y = f ( x )$ in $\mathbb { R } ^ { m }$ closest to the origin.The normalized vector

$$
w = - f ( x ^ { * } ) / \gamma , \quad \gamma = \| f ( x ^ { * } ) \| _ { 2 } ,
$$

is orthogonal to the tangent plane of the surface $y = f ( x ^ { * } ) + J ( x ^ { * } ) h , h \in$ $\boldsymbol { h } \in \mathbb { R } ^ { n }$ ，at $x ^ { * }$ .The normal curvature matrix of the surface with respect to $w$ is the symmetric matrix

$$
K = ( J ( x ^ { * } ) ^ { \dag } ) ^ { T } G _ { w } ( x ^ { * } ) J ( x ^ { * } ) ^ { \dag } , \quad G _ { w } = \sum _ { i = 1 } ^ { m } w _ { i } G _ { i } ( x ^ { * } ) .
$$

Denote the eigenvalues of $K$ by $\kappa _ { 1 } ~ \geq ~ \kappa _ { 2 } ~ \geq ~ \cdot ~ \cdot ~ \geq ~ \kappa _ { n }$ .The quantities $1 / \kappa _ { i }$ ， $\kappa _ { i } ~ \neq ~ 0$ are the principal radii of curvature of the surface $y = f ( x )$ with respect to the normal $w$ ；see Willmore [1126,1959]. Since

$$
( J ( x ^ { * } ) ^ { T } J ( x ^ { * } ) ) ^ { - 1 } = J ( x ^ { * } ) ^ { \dag } ( J ( x ^ { * } ) ^ { \dag } ) ^ { T } ,
$$

the matrix $\nabla F ( x ^ { * } )$ has the same nonzero eigenvalues as $\gamma K$ ,where $\gamma$ is given as in (8.1.17). It follows that

$$
\rho = \rho ( \nabla F ( { x ^ { * } } ) ) = \gamma \operatorname* { m a x } ( \kappa _ { 1 } , - \kappa _ { n } ) = \gamma \| K \| _ { 2 } .
$$

This relation indicates that the local convergence of the Gauss-Newton method is invariant under a local transformation of the nonlinear least squares problem.

If $J ( x ^ { * } )$ has full column rank, then $\nabla ^ { 2 } f ( x ^ { * } ) = J ^ { T } ( I - \gamma K ) J$ is positive definite. It follows that $x ^ { * }$ is a local minimum of $\phi ( x )$ if and only if $I - \gamma K$ is positive definite at $x ^ { * }$ . This is the case when

$$
1 - \gamma \kappa _ { 1 } > 0
$$

or, equivalently, $\gamma < 1 / \kappa _ { 1 }$ . Furthermore, if $1 - \gamma \kappa _ { 1 } \leq 0$ ，then $\phi ( x )$ has a saddle point at $x ^ { * }$ ； if $1 - \gamma \kappa _ { n } < 0$ ，then $\phi ( x )$ has a local maximum at $x ^ { * }$ .If $x ^ { * }$ is a saddle point, then $\kappa _ { 1 } \geq 1$ Hence using the Gauss-Newton method,one is generally repelled from a saddle point, which is an excellent property.

$$
P _ { J } ( x ) = J ( x ) J ( x ) ^ { \dag } = J ( x ) ( J ( x ) ^ { T } J ( x ) ) ^ { - 1 } J ( x ) ^ { T }
$$

is the orthogonal projection onto the range space of $J ( x )$ . Hence at a critical point $x ^ { * }$ it holds that $P _ { J } ( x ^ { * } ) f ( x ^ { * } ) = 0$ .The rate of convergence for the Gauss-Newton method can be estimated during the iterations from

$$
\| P _ { J } ( x _ { k + 1 } ) f _ { k + 1 } \| _ { 2 } / \| P _ { J } ( x _ { k } ) f _ { k } \| _ { 2 } \leq \rho + O ( \| x _ { k } - x ^ { * } \| _ { 2 } ^ { 2 } ) ,
$$

where $\rho$ is defined as in Theorem 8.1.1. (Recall that $\begin{array} { r } { \operatorname* { l i m } _ { x _ { k } \to x ^ { * } } P _ { J } ( x _ { k } ) f _ { k } = 0 . } \end{array}$ ）Since

$$
P _ { J } ( x _ { k } ) f _ { k } = J ( x _ { k } ) J ( x _ { k } ) ^ { \dagger } f _ { k } = - J ( x _ { k } ) p _ { k } ,
$$

the cost of computing this estimate is only one matrix-vector multiplication. When the estimated $\rho$ is greater than O.5 (say),one should consider switching to a method using second-derivative information.

If the radius of curvature at a critical point satisfies $1 / | \kappa _ { i } | \ll \| f ( x ^ { * } ) \| _ { 2 }$ , the nonlinear least squares problems will be ill-behaved,and many insignificant local minima may exist. Poor performance of Gauss-Newton methods often indicates poor quality of the underlying model or insufficient accuracy in the observed data. Then it would be beter to improve the model rather than use more costly methods of solution.Wedin [1109,1974] shows that the estimate (8.1.21) of the rate of convergence of the Gauss-Newton method is often a good indication of the quality of the underlying model. Deuflhard and Apostolescu [318,198o] call problems for which divergence occurs “inadequate problems.” Many numerical examples leading to poor behavior of Gauss-Newton methods are far from realistic; see Hiebert [6O9,1981] and Fraley $[ 4 3 0 , 1 9 8 9 ]$

As the following simple example shows,the Gauss-Newton method may not even be locally convergent. Consider minimizing $f _ { 1 } ^ { 2 } ( x ) + f _ { 2 } ^ { 2 } ( x )$ ,where

$$
f _ { 1 } ( x ) = x + 1 , \qquad f _ { 2 } ( x ) = \lambda x ^ { 2 } + x - 1 ,
$$

and $\lambda$ is a parameter. The minimizer is $x ^ { * } = 0$ The Gauss-Newton method gives $x _ { k + 1 } =$ $\lambda x _ { k } + 0 ( x _ { k } ^ { 2 } )$ . Hence this method diverges when $| \lambda | > 1$

To ensure global convergence,a useful modification of the Gauss-Newton method is to use a line search in which the next approximation is taken as

$$
x _ { k + 1 } = x _ { k } + \alpha _ { k } p _ { k } ,
$$

where $\alpha _ { k } > 0$ is a step length to be determined. There are two common algorithms for choosing $\alpha _ { k }$ ; see Ortega and Rheinboldt [845, 2ooo] and Gill, Murray,and Wright [476,1981].

1. Armijo-Goldstein line search, where $\alpha _ { k }$ is taken to be the largest number in the sequence $1 , { \frac { 1 } { 2 } } , { \frac { 1 } { 4 } } , \dotsb$ for which the inequality

$$
\| f ( x _ { k } ) \| _ { 2 } ^ { 2 } - \| f ( x _ { k } + \alpha _ { k } p _ { k } ) \| _ { 2 } ^ { 2 } \geq { \frac { 1 } { 2 } } \alpha _ { k } \| J ( x _ { k } ) p _ { k } \| _ { 2 } ^ { 2 }
$$

holds (notice that $- J ( x _ { k } ) p _ { k } = P J _ { k } f ( x _ { k } ) )$

2. “Exact” line search, i.e., taking $\alpha _ { k }$ as the solution to the one-dimensional minimization problem

$$
\operatorname* { m i n } _ { \alpha > 0 } \| f ( x _ { k } + \alpha p _ { k } ) \| _ { 2 } ^ { 2 } .
$$

Note that a solution $\alpha _ { k }$ may not exist, or there may be a number of local solutions.

A theoretical analysis of the Gauss-Newton method with exact line search has been given by Ruhe [939,1979]. The asymptotic rate of convergence is shown to be

$$
\widetilde { \rho } = \gamma ( \kappa _ { 1 } - \kappa _ { n } ) / ( 2 - \gamma ( \kappa _ { 1 } + \kappa _ { n } ) ) .
$$

A comparison with (8.1.19) shows that $\widetilde { \rho } = \rho$ if $\kappa _ { n } = - \kappa _ { 1 }$ ,and $\widetilde { \rho } < \rho$ otherwise. We also have that $\gamma \kappa _ { 1 } < 1$ implies $\widetilde \rho < 1$ ,i.e.,we always get convergence close to a local minimum. This is in contrast to the Gauss-Newton method, which may fail to converge to a local minimum.

Lindstrom and Wedin [751,1984] develop an alternative line-search algorithm. In this, $\alpha$ is chosen to minimize $\| p _ { k } ( \boldsymbol { \alpha } ) \| _ { 2 }$ , where $p ( \alpha )$ approximates the curve $f ( \alpha ) = f ( x _ { k } + \alpha p _ { k } ) \in \mathbb { R } ^ { m }$ One possibility is to choose $p ( \alpha )$ to be the unique circle (in the degenerate case, a straight line) determined by the conditions

$$
\begin{array} { r } { p _ { k } ( 0 ) = f ( 0 ) , \qquad \nabla p ( 0 ) = \nabla f ( 0 ) , \qquad p _ { k } ( \alpha _ { 0 } ) = f _ { k } ( \alpha _ { 0 } ) , } \end{array}
$$

where $\alpha _ { 0 }$ is a guess of the step length.

Ruhe also develops a way to obtain second-derivative information by using a nonlinear con-jugate gradient acceleration of the Gauss-Newton method with exact line searches. This method achieves quadratic convergence and often gives much faster convergence on difficult problems. When exact line search is used,conjugate gradient acceleration amounts to a negligible amount of extra work. However, for small-residual problems,exact line search is a waste of time,and then a simpler damped Gauss-Newton method is superior.

# 8.1.3 - Regularization and Trust-Region Methods

In practice it often happens that $J ( x )$ is numerically rank-deficient at an intermediate point $x _ { k }$ Then a natural choice is to take $p _ { k }$ as the pseudoinverse solution $p _ { k } = - J ^ { \dagger } ( x _ { k } ) f ( x _ { k } )$ of (8.1.12); see Ben-Israel [99, $1 9 6 7 ]$ ,Fletcher [410,1968],and Boggs [157,1976]． Such a situation is usually complicated by the difficulty in making decisions about the rank.The following example shows that this may be critical. Let

$$
\begin{array} { r } { J = \left( \begin{array} { l l } { 1 } & { 0 } \\ { 0 } & { \epsilon } \end{array} \right) , \qquad f = \left( \begin{array} { l } { f _ { 1 } } \\ { f _ { 2 } } \end{array} \right) , } \end{array}
$$

where $0 < \epsilon \ll 1$ and $f _ { 1 }$ and $f _ { 2 }$ are of order unity. If $J$ is considered to be of rank two,then the search direction is $p _ { k } = s _ { 1 }$ ,whereas if the assigned rank is one, $p _ { k } = s _ { 2 }$ ,where

$$
s _ { 1 } = - \left( { f _ { 1 } \atop f _ { 2 } / \epsilon } \right) , \qquad s _ { 2 } = - \left( { f _ { 1 } \atop 0 } \right) .
$$

Clearly the two directions $s _ { 1 }$ and $s _ { 2 }$ are almost orthogonal, and $s _ { 1 }$ is almost orthogonal to the gradient vector $J ^ { T } f$ . A strategy for estimating the rank of $J ( x _ { k } )$ can be based on QR factorization or SVD of $J ( x _ { k } )$ ； see Section 2.5.Usually an underestimate of the rank is preferable, except when $f ( x )$ is close to an ill-conditioned quadratic function.

An alternative approach that avoids the rank determination is to take $x _ { k + 1 } = x _ { k } + p _ { k }$ ,where $p _ { k }$ is the unique solution to

$$
\operatorname* { m i n } _ { p } \left\| f ( x _ { k } ) + J ( x _ { k } ) p \right\| _ { 2 } ^ { 2 } + \mu _ { k } ^ { 2 } \| p \| _ { 2 } ^ { 2 } ,
$$

and $\mu _ { k } > 0$ is a regularization parameter. Then $p _ { k }$ is defined even when $J _ { k }$ is rank-deficient. This method was first used by Levenberg [736,1944l and later modified by Marquardt [779,1963] and is therefore called the Levenberg-Marquardt method. The solution to problem (8.1.25) satisfies

$$
\left( J ( x _ { k } ) ^ { T } J ( x _ { k } ) + \mu _ { k } ^ { 2 } I \right) p _ { k } = - J ( x _ { k } ) ^ { T } f ( x _ { k } )
$$

or, equivalently,

$$
\operatorname* { m i n } _ { p } \left\| \left( { \boldsymbol { J } } ( { \boldsymbol { x } } _ { k } ) \right) p + \left( { \boldsymbol { f } } ( { \boldsymbol { x } } _ { k } ) \right) \right\| _ { 2 } ,
$$

and can be solved stably by QR factorization (or CGLS or LSQR).

The regularized Gauss-Newton method always takes descent steps. Hence it is localy convergent on almost all nonlinear least squares problems, provided an appropriate line search is carried out. We remark that as $\mu _ { k } \to 0 ^ { + }$ ， $p _ { k } \to J ( x _ { k } ) ^ { \dagger } f _ { k }$ , the pseudoinverse step. For large values of $\mu$ the direction $p _ { k }$ becomes parallel to the steepest descent direction $- J ( x _ { k } ) ^ { T } f _ { k }$ . Hence $p _ { k }$ interpolates between the Gauss-Newton and steepest descent direction. This property makes the Levenberg-Marquardt method preferable to damped Gauss-Newton for many problems.

A useful modification of the Levenberg-Marquardt algorithm is to change the penalty term in (8.1.25) to $\| \mu _ { k } D \| _ { 2 } ^ { 2 }$ ,where $D$ is a diagonal scaling matrix. A frequently used choice is $D ^ { 2 } =$ $\mathrm { d i a g } \left( J ( x _ { 0 } ) ^ { T } J ( x _ { 0 } ) \right)$ . This choice makes the Levenberg-Marquardt algorithm scaling invariant, i.e. it generates the same iterations if applied to $f ( D x )$ for any nonsingular diagonal matrix $D$

From the discussion of problem LSQI in Section 3.5.3, it follows that the regularized least squares problem (8.1.25) is equivalent to the least squares problem with a quadratic constraint,

$$
\operatorname* { m i n } _ { p } \| f ( x _ { k } ) + J ( x _ { k } ) p \| _ { 2 } \mathrm { ~ s u b j e c t ~ t o ~ } \| D p \| _ { 2 } \leq \Delta _ { k } ,
$$

for some $\Delta _ { k } > 0$ . If the constraint in (8.1.27) is binding, then $p _ { k }$ is a solution to (8.1.25) for some $\mu _ { k } > 0$ ．The set of feasible vectors $p$ $\| D p \| _ { 2 } \le \Delta _ { k }$ in (8.1.27) can be thought of as a region of trust for the linear model $f ( x ) \approx f ( x _ { k } ) + J ( x _ { k } ) p$ ， $p = x - x _ { k }$ . There has been much research on so-called trust-region methods based on the formulation (8.1.27) as an alternative to a line-search strategy. Combined with a suitable active-set strategy, such a technique can be extended to handle problems with nonlinear inequality constraints; see Lindstrom [749,1983].

Several versions of the Levenberg-Marquardt algorithm have been proved to be globally convergent; see, e.g., Fletcher [411,1971] and Osborne [847,1976]. A general description of scaled trust-region methods for nonlinear optimization is given by Moré [806,1978],[807,1983]. Moré proves that the algorithm will converge to a critical point $x ^ { * }$ if $f ( x )$ is continuously differentiable, $J ( x )$ is uniformly continuous in a neighborhood of $x ^ { * }$ ,and $J ( x _ { k } )$ remains bounded.

# Algorithm 8.1.1 (Trust-Region Method).

Given $x _ { 0 }$ ， $D , \Delta$ and $\beta \in ( 0 , 1 )$ for $k = 0 , 1 , 2 , \ldots$ ，

1. Determine $p _ { k }$ as a solution to the subproblem

$$
\operatorname* { m i n } _ { p } \| f ( x _ { k } ) + J ( x _ { k } ) p \| _ { 2 } { \mathrm { ~ s u b j e c t ~ t o ~ } } \| D p \| _ { 2 } \leq \Delta .
$$

2. Compute the ratio between the actual and predicted reduction:

$$
\rho _ { k } = \frac { \| f ( x _ { k } ) \| _ { 2 } ^ { 2 } - \| f ( x _ { k } + p _ { k } ) \| _ { 2 } ^ { 2 } } { \| f ( x _ { k } ) \| _ { 2 } ^ { 2 } - \| f ( x _ { k } ) + J ( x _ { k } ) p _ { k } \| _ { 2 } ^ { 2 } } .
$$

3.If $\rho _ { k } > \beta$ set $x _ { k + 1 } = x _ { k } + p _ { k }$ ; otherwise, set $x _ { k + 1 } = x _ { k }$

4. Update the scaling matrix $D$ and the trust-region radius $\Delta$ $\rho _ { k } \ \ge \ 3 / 4$ ，then $\Delta$ is increased by a factor of 2; if $\rho _ { k } < 1 / 4 \Delta _ { \cdot }$ ，then $\Delta$ is reduced by a factor of 2.

To compute $\rho ( p _ { k } )$ stably in step 2, note that because $p _ { k }$ satisfies (8.1.26), the predicted reduction can be computed from

$$
\begin{array} { r l } & { \| f ( x _ { k } ) \| _ { 2 } ^ { 2 } - \| f ( x _ { k } ) + J ( x _ { k } ) p _ { k } \| _ { 2 } ^ { 2 } = - 2 p _ { k } ^ { T } J ( x _ { k } ) ^ { T } f ( x _ { k } ) - \| J ( x _ { k } ) p _ { k } \| _ { 2 } ^ { 2 } } \\ & { \qquad = 2 \mu ^ { 2 } \| D p _ { k } \| _ { 2 } ^ { 2 } + \| J ( x _ { k } ) p _ { k } \| _ { 2 } ^ { 2 } . } \end{array}
$$

The ratio $\rho _ { k }$ measures the agreement between the linear model and the nonlinear function. If $J _ { k }$ has full rank, then $\rho _ { k } \to 1$ as $\| p _ { k } \| _ { 2 } \to 0$ .The parameter $\beta$ in step 3 can be chosen quite small, e.g., $\beta = 0 . 0 0 0 1$

Assume that the Jacobian $J ( x )$ is rank-deficient with constant rank $r < n$ in a neighborhood of a local minimum $x ^ { * }$ . Then the appropriate formulation of the problem is

$$
\operatorname* { m i n } _ { x } \| x \| _ { 2 } ^ { 2 } { \mathrm { ~ s u b j e c t ~ t o ~ } } \| f ( x ) \| _ { 2 } ^ { 2 } = \operatorname* { m i n } .
$$

Boggs [157,1976] notes that the choice $p _ { k } = - J ( x _ { k } ) ^ { \dagger } f ( x _ { k } )$ gives the least-norm correction to the linearized problem. Instead, $p _ { k }$ should be taken as the least-norm solution to the linearized problem

$$
\operatorname* { m i n } _ { p } \| x _ { k } + p \| _ { 2 } ^ { 2 } \ { \mathrm { s u b j e c t ~ t o } } \ \| f ( x _ { k } ) + J ( x _ { k } ) p \| _ { 2 } ^ { 2 } = \operatorname* { m i n } .
$$

This has the solution

$$
p _ { k } = - J ( x _ { k } ) ^ { \dagger } f ( x _ { k } ) - P _ { \mathit { N } ( J _ { k } ) } x _ { k } ,
$$

where $P _ { \mathcal { N } ( J _ { k } ) } = I - J ( x _ { k } ) ^ { \dagger } J ( x _ { k } )$ is the orthogonal projector onto the nulspace of $J ( x _ { k } )$ Eriksson et al. [388,2oo5] derive necessary and sufficient optimality conditions for the above method. Applying Tikhonov regularization to problem (8.1.28) gives $\begin{array} { r } { \operatorname* { m i n } _ { x } \| f ( x ) \| _ { 2 } ^ { 2 } + \mu ^ { 2 } \| x \| _ { 2 } ^ { 2 } } \end{array}$ or, equivalently,

$$
\operatorname* { m i n } _ { x } \left\| { \binom { f ( x ) } { \mu x } } \right\| _ { 2 } ^ { 2 } .
$$

Linearization of (8.1.31) at $x _ { k }$ gives the subproblem

$$
\operatorname* { m i n } _ { p } \left\| \left( { \boldsymbol { J } } ( { \boldsymbol { x } } _ { k } ) \right) p + \left( { \boldsymbol { f } } ( { \boldsymbol { x } } _ { k } ) \right) \right\| _ { 2 } ^ { 2 } .
$$

For $\mu _ { k } > 0$ thisisafullnkastsapobqesoutio $p _ { k } = p _ { k } ^ { T i k }$ can be computed by QR factorization.

Lemma 8.1.2. The search directions pTi computedntheGuss-Newtonmethodaretedto those in (8.1.30) by

$$
\operatorname* { l i m } _ { \mu _ { k } \to 0 ^ { + } } p _ { k } ^ { \mathrm { T i k } } = p _ { k } .
$$

This result implies that if $\mu _ { k } \to 0 ^ { + }$ , the two Gauss-Newton methods have the same local convergence properties.

# 8.1.4 - Quasi-Newton Methods

Convergence of the Gauss-Newton method and trust-region methods can be slow for largeresidual problems and strongly nonlinear problems. These methods may also have difficulty at points where the Jacobian is rank-deficient. Several methods have been suggested for partially taking the second derivatives into account, either explicitly or implicitly.

In quasi-Newton methods an approximation to the second-derivative matrix is built up successively from evaluations of the gradient. Many of those methods are known to possess superlinear convergence. Let $S _ { k - 1 }$ be a symmetric approximation to the Hessian at step $k$ .The updated $S _ { k }$ is required to approximate the curvature of $f$ along $x _ { k } \mathrm { ~ - ~ } x _ { k - 1 }$ ,i.e., $S _ { k } ( x _ { k } - x _ { k - 1 } ) = y _ { k }$ ， where

$$
y _ { k } = \nabla f ( x _ { k } ) - \nabla f ( x _ { k - 1 } ) = J ( x _ { k } ) ^ { T } f ( x _ { k } ) - J ( x _ { k - 1 } ) ^ { T } f ( x _ { k - 1 } ) .
$$

This is called the quasi-Newton relation. We further require $S _ { k }$ to differ from $S _ { k - 1 }$ by a matrix of small rank. The search direction $p _ { k }$ for the next step is then computed from

$$
S _ { k } p _ { k } = - g ( x _ { k } ) , \qquad g ( x _ { k } ) = J ( x _ { k } ) ^ { T } r ( x _ { k } ) .
$$

As a starting approximation, ${ \cal S } _ { 0 } = J ( x _ { 0 } ) ^ { T } J ( x _ { 0 } )$ is usually recommended.

Ramsin and Wedin [910,1977] gave the following rule for the choice between Gauss-Newton and quasi-Newton methods based on the observed rate (8.1.21) of convergence $\rho$ for the Gauss-Newton method:

1. For $\rho \leq 0 . 5$ ,Gauss-Newton is better.   
2. For globally simple problems,quasi-Newton is better for $\rho > 0 . 5$   
3.For globally difficult problems, Gauss-Newton is much faster for $\rho \leq 0 . 7$ But for larger values of $\rho$ ,quasi-Newton is safer.

This can be used to construct a hybrid method with automatic switching between the two methods.

The application of quasi-Newton methods to the NLS problem as outlined above has not been very efcient in practice. One reason is that often $J ( x _ { k } ) ^ { T } J ( x _ { k } )$ is the dominant part of $\nabla ^ { 2 } f ( x _ { k } )$ , and this information is disregarded. A more successul approach, used by Dennis, Gay,and Welsch [315,198i], is to estimate $\nabla ^ { 2 } f ( x _ { k } )$ by $J ( x _ { k } ) ^ { T } J ( x _ { k } ) + B _ { k }$ ，where $B _ { k }$ isa symmetric quasi-Newton approximation to $B ( x _ { k } )$ . The quasi-Newton relation then becomes

$$
( J _ { k } ^ { T } J _ { k } + B _ { k } ) ( x _ { k } - x _ { k - 1 } ) = y _ { k } ,
$$

but it is preferable to use the alternative formula

$$
B _ { k } ( x _ { k } - x _ { k - 1 } ) = z _ { k } , \quad z _ { k } = ( J ( x _ { k } ) - J ( x _ { k - 1 } ) ) ^ { T } f ( x _ { k } ) .
$$

The solution to (8.1.35) that minimizes $\| B _ { k } - B _ { k - 1 } \| _ { F }$ is given by the rank-two update formula

$$
B _ { k } = B _ { k - 1 } + \frac { w _ { k } z _ { k } ^ { T } + z _ { k } w _ { k } ^ { T } } { z _ { k } ^ { T } s _ { k } } - \frac { w _ { k } ^ { T } s _ { k } z _ { k } z _ { k } ^ { T } } { ( z _ { k } ^ { T } s _ { k } ) ^ { 2 } } ,
$$

where $s _ { k } = x _ { k } - x _ { k - 1 }$ and $w _ { k } = z _ { k } - B _ { k - 1 } s _ { k }$ ; see Dennis and Schnabel [316,1996, pp. $2 3 1 -$ 232]. In some cases the update (8.1.36) gives inadequate results. This motivates the inclusion of a“sizing” in which $B _ { k }$ is replaced by $\tau _ { k } B _ { k }$ ，where $\tau _ { k } = \operatorname* { m i n } \{ | s _ { k } ^ { T } z _ { k } | / | s _ { k } ^ { T } B _ { k } s _ { k } | , 1 \}$ . This heuristic ensures that $S _ { k }$ converges to zero for zero-residual problems,which has been shown to improve the convergence behavior. Note that in the quasi-Newton step, $J _ { k } ^ { T } J _ { k } + B _ { k }$ may need to be modified to be positive so that Cholesky factorization can be used.

The update (8.1.36) is used by the popular subroutine NL2SOL by Dennis, Gay,and Welsch $[ 3 1 5 , 1 9 8 1 ]$ to maintain the approximation $B _ { k }$ and adaptively decide whether to use it or a Gauss-Newton method. In each iteration,NL2SOL computes the reduction predicted by both models and compares it with the observed actual reduction $f ( x _ { k + 1 } ) - f ( x _ { k } )$ . The next step uses the model whose predicted reduction best approximates the actual reduction. Usually this causes NL2SOL to use Gauss-Newton steps until the information in $B _ { k }$ becomes useful. To achieve global convergence, a trust-region strategy is used.

In the quasi-Newton method of Gill and Murray [474,1978], $J ( x _ { k } ) ^ { T } J ( x _ { k } )$ is regarded as a good estimate of the Hessian in the invariant subspace corresponding to the large singular values of $J ( x _ { k } )$ . The second-derivative term $B ( x _ { k } )$ is taken into account only in the complementary subspace.Let the SVD of Jacobian $J = J ( x _ { k } )$ be partitioned as

$$
\begin{array} { r } { J = \left( \begin{array} { c c } { U _ { 1 } } & { U _ { 2 } } \end{array} \right) \left( \begin{array} { c c } { \Sigma _ { 1 } } & { 0 } \\ { 0 } & { \Sigma _ { 2 } } \end{array} \right) \left( \begin{array} { c c } { V _ { 1 } ^ { T } } \\ { V _ { 2 } ^ { T } } \end{array} \right) , } \end{array}
$$

where $\Sigma _ { 1 } = \operatorname { d i a g } \left( \sigma _ { 1 } , \ldots , \sigma _ { p } \right)$ contains the large singular values of $J$ and $\Sigma _ { 2 } = \mathrm { d i a g } \left( \sigma _ { p + 1 } , \dots , \right.$ $\sigma _ { n }$ ).Set $B \ : = \ : B ( x _ { k } )$ ,and let $\bar { s }$ denote the first $n$ components of the vector $s = U ^ { T } f ( x _ { k } )$ Equation (8.1.1O) for the Newton direction can then be split into two sets.The first $p$ equations are

$$
( \Sigma _ { 1 } ^ { 2 } + V _ { 1 } ^ { T } B V _ { 1 } ) q _ { 1 } + V _ { 1 } ^ { T } B V _ { 2 } q _ { 2 } = - \Sigma _ { 1 } \bar { s } _ { 1 } .
$$

If the terms involving $B = B _ { k }$ can be neglected compared to $\Sigma _ { 1 } ^ { 2 } q _ { 1 }$ ，we get $q _ { 1 } = - \Sigma _ { 1 } ^ { - 1 } \bar { s } _ { 1 }$ Substituting this into the last $( n - p )$ equations, we obtain

$$
( \Sigma _ { 2 } ^ { 2 } + V _ { 2 } ^ { T } B V _ { 2 } ) q _ { 2 } = - \Sigma _ { 2 } \bar { s } _ { 2 } + V _ { 2 } ^ { T } B V _ { 1 } \Sigma _ { 1 } ^ { - 1 } \bar { s } _ { 1 } .
$$

The approximate Newton direction is taken to be $p _ { k } = V _ { 1 } q _ { 1 } + V _ { 2 } q _ { 2 }$ . The split of the singular values is updated at each iteration,and $p$ is maintained close to $n$ as long as sufficient progress is made.A finite-difference approximation to $V _ { 2 } ^ { T } B _ { k } V _ { 2 }$ is obtained as follows. Let $v _ { j }$ be a column of $V _ { 2 }$ and $h$ be a small positive scalar. Then, by differentiating the gradient along the columns of $V _ { 2 }$ ，

$$
( \nabla f _ { i } ( x _ { k } + h v _ { j } ) - \nabla f _ { i } ( x _ { k } ) ) / h = v _ { j } ^ { T } G _ { i } ( x _ { k } ) + O ( h ) .
$$

The vector on the left-hand side is the $i$ th row of $( J ( x _ { k } + h v _ { j } ) - J ( x _ { k } ) ) / h$ . Multiplying by $f _ { i } ( x _ { k } )$ and adding gives

$$
\begin{array} { r l r } {  { f ( x _ { k } ) ^ { T } ( J ( x _ { k } + h v _ { j } ) - J ( x _ { k } ) ) / h = v _ { j } ^ { T } \sum _ { i = 1 } ^ { m } f _ { i } ( x _ { k } ) G _ { i } ( x _ { k } ) + O ( h ) } } \\ & { } & \\ & { } & { = v _ { j } ^ { T } B _ { k } + O ( h ) , \quad j = p + 1 , \ldots , n . } \end{array}
$$

This gives an approximation for $V _ { 2 } ^ { T } B _ { k }$ , and then $( V _ { 2 } ^ { T } B _ { k } ) V _ { 2 }$ can be formed.

Various other possibilities for hybrid Gauss-Newton/quasi-Newton methods are considered by Al-Baali and Fletcher [14, $\mathbf { 1 9 8 5 } ]$ . They use an approach in which the choice of method and parameters is made by estimating the error in an inverse Hessian approximation.A Newton-like search direction is computed from (8.1.34),where $S _ { k }$ is a symmetric positive definite approximation to the Hessian. This ensures that $p _ { k }$ is a descent direction and makes it possible to use a simpler line-search technique rather than a trust-region approach.

Al-Baali and Fletcher [15,1986] determine $\alpha _ { k }$ to satisfy the conditions

$$
\begin{array} { r l } & { f ( x _ { k } + \alpha _ { k } p _ { k } ) \leq \rho \alpha _ { k } g ( x _ { k } ) ^ { T } p _ { k } , \quad \rho \in ( 0 , 1 / 2 ) , } \\ & { | g ( x _ { k } + \alpha _ { k } p _ { k } ) ^ { T } p _ { k } | \leq - \sigma g ( x _ { k } ) ^ { T } p _ { k } , \quad \sigma \in ( \rho , 1 ) , } \end{array}
$$

and suggest an algorithm to find such a point. Fletcher and $\mathrm { X u }$ [413,1987] develop a hybrid method called HY2 in which a quasi-Newton step is taken when $( f ( x _ { k } ) - f ( x _ { k + 1 } ) ) / f ( x _ { k } ) < \epsilon$ otherwise, a Gauss-Newton step is taken. The quasi-Newton step uses (8.1.36) to update the approximate Hessian but includes a safeguard to maintain positive definiteness. HY2 is superlinearly convergent under mild conditions.A review of quasi-Newton methods for nonlinear least squares is given by Eriksson [387,1999].

Extending the quasi-Newton method to large sparse optimization problems has proved to be difficult. For certain types of large,“partially separable” nonlinear least squares problems,a promising approach is suggested by Toint [1O66,1987]. A typical case is when every function $f _ { i } ( x )$ only depends on a small subset of the set of $n$ variables．Then the Jacobian $J ( x )$ and the element Hessian matrices $G _ { i } ( x )$ are sparse,and it may be possible to store approximations to all $G _ { i } ( x )$ ， $i = 1 , \ldots , m$ ．An implementation is available as the Fortran subroutine VE10 in the Harwell Software Library; see Toint [1O67,1987]. Another subroutine suitable for such problems is LANCELOT by Conn, Gould, and Toint [265,1991], [266,1992].

In a more general setting the solution to nonlinear least squares problems may be subject to nonlinear equality constraints,

$$
\operatorname* { m i n } _ { x } { \frac { 1 } { 2 } } \| f ( x ) \| _ { 2 } ^ { 2 } { \mathrm { ~ s u b j e c t ~ t o ~ } } h ( x ) = 0 ,
$$

where $x \in \mathbb { R } ^ { n } , f ( x ) \in \mathbb { R } ^ { m } , h \in \mathbb { R } ^ { p }$ ,and $p < n$ . The Gauss-Newton method can be generalized to constrained problems by linearization of (8.1.38) at a point $x _ { k }$ ．A search direction $p _ { k }$ is then computed as a solution to the linearly constrained problem

$$
\operatorname* { m i n } _ { p } \| f ( x _ { k } ) + J ( x _ { k } ) p \| _ { 2 } \ { \mathrm { s u b j e c t ~ t o } } \ h ( x _ { k } ) + C ( x _ { k } ) p = 0 ,
$$

where $J$ and $C$ are the Jacobians for $f ( x )$ and $h ( x )$ ,respectively. This problem can be solved by the methods described in Section 4.5.The search direction $p _ { k }$ obtained from (8.1.39) can be shown to be a descent direction for the merit function

$$
\psi ( x , \mu ) = \| f ( x ) \| _ { 2 } ^ { 2 } + \mu \| h ( x ) \| _ { 2 } ^ { 2 }
$$

at the point $x _ { k }$ , provided $\mu$ is chosen large enough.

# 8.1.5 - Inexact Gauss-Newton Methods

In large-scale applications, the Gauss-Newton linear subproblems

$$
\operatorname* { m i n } _ { \boldsymbol { p } } \| J ( \boldsymbol { x } _ { k } ) \boldsymbol { p } + f ( \boldsymbol { x } _ { k } ) \| _ { 2 }
$$

may be too costly to solve accurately. In any case, far from the solution $x ^ { * }$ , it may not be worth solving these subproblems to high accuracy. To solve (8.1.40) for $p _ { k }$ ,a truncated inner iterative method such as CGLS or LSQR can be applied. A class of inexact Newton methods for solving a system of nonlinear equations $F ( x ) = 0$ is studied by Dembo,Eisenstat,and Steihaug [300, 1982]. A sequence $\{ x _ { k } \}$ of approximations is generated as follows. Given an initial guess $x _ { 0 }$ ， set $x _ { k + 1 } = x _ { k } + p _ { k }$ ,where $p _ { k }$ satisfies

$$
F ^ { \prime } ( x _ { k } ) p _ { k } = - F ( x _ { k } ) + r _ { k } , \quad \frac { \| r _ { k } \| _ { 2 } } { \| F ( x _ { k } ) \| _ { 2 } } \leq \eta _ { k } < 1 .
$$

Here $\{ \eta _ { k } \}$ is a nonnegative forcing sequence used to control the level of accuracy. Taking $\eta _ { k } = 0$ gives the Newton method. Note that the requirement $\eta _ { k } < 1$ is natural because $\eta _ { k } \geq 1$ would allow $p _ { k } = 0$

Theorem 8.1.3 (Dembo,Eisenstat,and Steihaug [300,1982, Theorem 3]). Assume that there exists an $x ^ { * }$ such that $F ( x ^ { * } ) = 0$ with $F ^ { \prime } ( x ^ { * } )$ nonsingular. Let $F$ be continuously differentiable in a neighborhood of $x ^ { * }$ ，and let $\eta _ { k } \ \leq \ \hat { \eta } \ < \ t \ < \ 1 .$ ，Then there exists $\epsilon > 0$ such that if $\| x ^ { * } - x _ { 0 } \| _ { 2 } \leq \epsilon ,$ the sequence $\{ x _ { k } \}$ generated by (8.1.41) converges linearly to $x ^ { * }$ in the sense that

$$
\| x _ { k + 1 } - x _ { k } \| _ { * } \leq t \| x _ { k } - x _ { k } \| _ { * } ,
$$

where the norm is defined by $\| y \| _ { * } \equiv \| F ^ { \prime } ( x ^ { * } ) y \| _ { 2 }$

First,we note that the exact Gauss-Newton method can be considered as an incomplete Newton method for the equation $F ( x ) = J ( x ) ^ { T } f ( x ) = 0$ . This is of the form (8.1.41),where $p _ { k }$ satisfies $J ( x _ { k } ) ^ { T } J ( x _ { k } ) p _ { k } = - J ( x _ { k } ) ^ { T } f ( x _ { k } )$ and

$$
f _ { k } = ( J ( x _ { k } ) ^ { T } J ( x _ { k } ) + G ( x _ { k } ) ) p _ { k } + J ( x _ { k } ) ^ { T } f ( x _ { k } ) = G ( x _ { k } ) p _ { k } ,
$$

where $G _ { i } ( x _ { k } )$ is the Hessian of $f _ { i } ( x _ { k } )$ . By Theorem 8.1.3 a sufficient condition for convergence .s that

$$
\begin{array} { r } { \bigg \| G ( x _ { k } ) \big ( J ( x _ { k } ) ^ { T } J ( x _ { k } ) \big ) ^ { - 1 } \bigg \| _ { 2 } = t _ { k } \leq t < 1 . } \end{array}
$$

This is more restrictive than the condition given in Theorem 8.1.1.

A class of inexact Gauss-Newton methods can be defined as follows. Given an initial guess $x _ { 0 }$ ,set $x _ { k + 1 } = x _ { k } + p _ { k }$ ,where $p _ { k }$ satisfies

$$
f _ { k } = J ( \boldsymbol { x } _ { k } ) ^ { T } ( J ( \boldsymbol { x } _ { k } ) \boldsymbol { p } _ { k } + \boldsymbol { f } ( \boldsymbol { x } _ { k } ) ) , \quad \| \boldsymbol { f } _ { k } \| _ { 2 } \leq \beta _ { k } \| J ( \boldsymbol { x } _ { k } ) ^ { T } \boldsymbol { f } ( \boldsymbol { x } _ { k } ) \| _ { 2 } .
$$

The condition on $\| f _ { k } \| _ { 2 }$ is a natural stopping condition on an iterative method for solving the linear subproblem. Gratton,Lawless,and Nichols [526, 2oo7] give conditions on the sequence of tolerances $\{ \beta _ { k } \}$ needed to ensure convergence and investigate the use of such methods for variational data assimilation in meteorology.

Theorem 8.1.4 (Gratton,Lawless,and Nichols [526,2oo7,Theorem 5]). Let $f ( x )$ bea twice continuously Fréchet differentiable function. Assume that there exists an $x ^ { * }$ such that $J ^ { T } ( x ^ { * } ) f ( x ^ { * } ) = 0$ and $J ( x ^ { * } )$ has full column rank. Assume $t _ { k } < \hat { \beta } < 1$ ,where $t _ { k }$ is given as in (8.1.43). Assume $\beta _ { k }$ ， $k = 0 , 1 , \ldots$ , are chosen so that

$$
0 \leq \beta _ { k } \leq ( \hat { \beta } - t _ { k } ) / ( 1 + t _ { k } ) .
$$

Then there exists $\epsilon > 0$ such that if $\| x ^ { * } - x _ { 0 } \| _ { 2 } \leq \epsilon ,$ the sequence $\{ x _ { k } \}$ of the inexact Gauss-Newton method (8.1.44) converges linearly to $x ^ { * }$

Note that the requirement $t _ { k } < \hat { \beta } < 1$ is the sufficient condition for convergence given for the exact Gauss-Newton method. The more highly nonlinear the problem,the larger $t _ { k }$ and the more accurate the linear subproblems to be solved. Accelerated schemes for inexact Newton methods using GMRES for large systems of nonlinear equations are given by Fokkema, Sleijpen,and van der Vorst [414, 1998].

# Notes and references

Dennis [314,1977] gives an early insightful survey of methods for solving nonlinear least squares and equations. Excellent standard references on numerical methods for optimization and systems of nonlinear equations are Dennis and Schnabel [316,1996] and Nocedal and Wright [833, 2006]. Ortega and Rheinboldt [845,2ooo] give a general treatment of theory and algorithms for solving systems of nonlinear equations. General treatments of methods for nonlinear opti-mization problems are given by Gill, Murray,and Wright [476,1981] and Fletcher [412, 2000]. Schwetlick [979,1992] surveys models and algorithms for general nonlinear parameter estimation. Continuation methods are an alternative approach for solving difficult large-residual NLS problems. Salane [962,1987] develops such algorithms and shows they can be competitive with trust-region algorithms.

Methods and software for the NLS problem are described by Wedin and Lindstrom [752, 1988].A useful guide to optimization software is available at the NEOS Guide website. It is constantly updated to reflect new packages and changes to existing software. A trust-region algorithm that has proven to be very successful in practice is included in the $\mathrm { C } { + + }$ software package MINPACK available from netlib. For a user's guide,see Moré, Garbow,and Hillstrom [808, 198o]. See also the PROC NLP Library of the SAS Institute. The Ceres nonlinear least squares solver by Agarwal et al. (see http : //ceres- solver .org) has been used since 2010 by Google for the construction of three-dimensional models in its street-view sensor fusion.

# 8.2 - Separable Least Squares Problems

# 8.2.1 - Variable Projection Method

Suppose we want to solve a nonlinear least squares problem of the form

$$
\operatorname* { m i n } _ { y , z } \| g - \Phi ( z ) y \| _ { 2 } ^ { 2 } , \quad \Phi ( z ) \in \mathbb { R } ^ { m \times p } ,
$$

where $\Phi ( z ) \in \mathbb { R } ^ { m , p }$ ， $y \in \mathbb { R } ^ { p }$ ,and $z \in \mathbb { R } ^ { q }$ are unknown parameters, and $g \in \mathbb { R } ^ { m }$ are given data. For a fixed value of the nonlinear parameter $z$ , problem (8.2.1) is a linear least squares problem in $y$ .Such least squares problems are called separable and arise frequently in applications. One example is when one wants to approximate given data by a linear combination of given nonlinear functions $\phi _ { j } ( z )$ ， $j = 1 , \dotsc , p$

A simple method for solving separable problems is the alternating least squares (ALS) algorithm. Let $z _ { 1 }$ be an initial approximation, and solve the linear problem $\operatorname* { m i n } _ { y } \| g - \Phi ( z _ { 1 } ) y \| _ { 2 }$ to obtain $y _ { 1 }$ . Next, solve the nonlinear problem $\operatorname* { m i n } _ { z } \| g - \Phi ( z ) y _ { 1 } \| _ { 2 }$ to obtain $z _ { 2 }$ .Repeat both steps until convergence. The rate of convergence of ALS is linear and can be very slow. It does not always converge.

For a fixed value of $z$ , the least-norm least squares solution of (8.2.1) can be expressed as

$$
y ( z ) = \Phi ( z ) { } ^ { \dagger } g ,
$$

where $\Phi ^ { \dagger }$ is the pseudoinverse of $\Phi ( z )$ .In the variable projection method of Golub and Pereyra [5O3,1973l, this is used to eliminate the linear parameters $y$ ，giving a reduced nonlinear

least squares problem

$$
\operatorname* { m i n } _ { z } \| g - P _ { \Phi ( z ) } g \| ^ { 2 } , \quad P _ { \Phi ( z ) } = \Phi ( z ) \Phi ( z ) ^ { \dagger } ,
$$

where $P _ { \Phi ( z ) }$ is the orthogonal projector onto the column space of $\Phi ( z )$ . This is a pure nonlinear problem of reduced dimension. An important advantage is that initial values are only needed for the nonlinear parameters $z$

In order to solve (8.2.3) using a Gauss-Newton-Marquardt method,a formula for the gradient of the function $f ( z ) = ( I - P _ { \Phi ( z ) } ) g = P _ { \Phi ( z ) } ^ { \perp } g$ in (8.2.3)is neded.The following lemma giveser $P _ { \Phi ( z ) } ^ { \perp }$ . It must be assumed that the rank of $\Phi ( z )$ is locally constant, because otherwise the pseudoinverse would not be differentiable.

Lemma 8.2.1 (Golub and Pereyra [503,1973,Lemma 4.1]). Let $\Phi ( z ) \in \mathbb { R } ^ { m \times p }$ be a matrix of local constant rank $r$ and $\Phi ^ { \dagger }$ be its pseudoinverse. Denote by $P _ { \Phi } = \Phi \Phi ^ { \dagger }$ the orthogonal projector onto $\mathcal { R } ( \Phi )$ ,and set $P _ { \Phi } ^ { \bot } = 1 - P _ { \Phi }$ . Then, using the product rule for differentiation, we get

$$
\frac { d } { d z } ( P _ { \Phi } ) = - \frac { d } { d z } ( P _ { \Phi } ^ { \perp } ) = P _ { \Phi } ^ { \perp } \frac { d \Phi } { d z } \Phi ^ { \dagger } + \left( P _ { \Phi } ^ { \perp } \frac { d \Phi } { d z } \Phi ^ { \dagger } \right) ^ { T } .
$$

More generally, Golub and Pereyra show that (8.2.4) is valid for any generalized inverse that satisfies $\Phi \Phi ^ { - } \Phi = \Phi$ and $( \Phi \Phi ^ { - } ) ^ { T } = \Phi \Phi ^ { - }$ . Note that the derivative $d \Phi / d z$ in (8.2.4) is a threedimensional tensor with elements $\partial \phi _ { i j } / \partial z _ { k }$ . The transposition in (8.2.4) is done in the $( i , j )$ directions for fixed $k$

In many applications, each component function $\phi _ { j } ( z )$ depends on only a few of the parameters $z _ { 1 } , \ldots , z _ { q }$ . Hence the derivative will often contain many zeros. Golub and Pereyra develop a storage scheme that avoids waste storage and computations. Let $E = ( e _ { i j } )$ be a $q \times p$ incidence matrix such that $e _ { i j } ~ = ~ 1$ if function $\phi _ { j }$ depends on the parameter $z _ { i }$ ，and O otherwise.This incidence matrix can be retrieved from an $m \times p$ array $B$ $\begin{array} { r } { 3 , p = \sum _ { i , j } e ( i , j ) } \end{array}$ ,in which the nonzero derivatives are stored sequentially.

Example 8.2.2. A problem of great importance is the fiting of a linear combination of exponential functions with different time constants,

$$
g ( t ) = y _ { 0 } + \sum _ { j = 1 } ^ { p } y _ { j } e ^ { z _ { j } t } ,
$$

to observations $g _ { i } = g ( t _ { i } ) + \epsilon _ { i }$ ， $i = 0 { : } m$ .Since $g ( t )$ in (8.2.5) depends on $p { + 1 }$ linear parameters $y _ { j }$ and $p$ nonlinear parameters $z _ { j }$ ,at least $m = 2 p + 1$ observations for $t _ { 0 } , \ldots , t _ { m }$ are needed. Clearly this problem is separable,and $\phi _ { i , j } ( z ; t ) \ : = \ : e ^ { z _ { j } t _ { i } }$ ， $j = 1 , \dotsc , p$ .Here the number of nonvanishing derivatives is $p$

The quantities required to solve the reduced nonlinear problem can be expressed in terms of a complete QR decomposition

$$
\Phi = U \left( \begin{array} { c c } { { R } } & { { 0 } } \\ { { 0 } } & { { 0 } } \end{array} \right) V ^ { T } , \quad U = \left( U _ { 1 } \quad U _ { 2 } \right) ,
$$

where $R \in \mathbb { R } ^ { r \times r }$ $( r = \mathrm { r a n k } ( \Phi ) )$ is upper triangular and nonsingular, and $U$ and $V$ are orthogonal. The solution to the linear least squares problem (8.2.1) is then ${ y = \Phi ^ { \dag } g }$ ,where

$$
\Phi ^ { \dagger } = V \left( \begin{array} { c } { { R ^ { - 1 } } } \\ { { 0 } } \end{array} \right) U _ { 1 } ^ { T }
$$

is the generalized inverse. The orthogonal projectors onto the range of $\Phi$ and its orthogonal complement are

$$
P _ { \Phi } = \Phi \Phi ^ { \dag } = U _ { 1 } U _ { 1 } ^ { T } , \qquad P _ { \Phi } ^ { \perp } = I - P _ { \Phi } = U _ { 2 } U _ { 2 } ^ { T } .
$$

The least squares residual is $r = P _ { \Phi } ^ { \perp } g = U _ { 2 } ( U _ { 2 } ^ { T } g )$ , and its norm is

$$
\| r \| _ { 2 } = \| U _ { 2 } ( U _ { 2 } ^ { T } g ) \| _ { 2 } = \| c _ { 2 } \| _ { 2 } , \quad U ^ { T } g = { \binom { c _ { 1 } } { c _ { 2 } } } .
$$

Denote by $D _ { k }$ the $m \times n$ matrix of $\Phi$ derivatives with respect to the single parameter $z _ { k }$

$$
D _ { k } = - \left[ P _ { \Phi } ^ { \perp } \frac { d \Phi } { d z _ { k } } \Phi ^ { \dagger } + ( \Phi ^ { \dagger } ) ^ { T } \frac { d \Phi ^ { T } } { d z _ { k } } P _ { \Phi } ^ { \perp } \right] g , \quad k = 1 , \ldots , q .
$$

The $k$ th column of the first part of the Jacobian becomes

$$
- { \cal P } _ { \Phi } ^ { \perp } { \cal D } _ { k } \Phi ^ { \dagger } g = - U _ { 2 } ( U _ { 2 } ^ { T } ( { \cal D } _ { k } y ) ) , \quad k = 1 , \ldots , q .
$$

The second part becomes

$$
- ( P _ { \Phi } ^ { \perp } D _ { k } \Phi ^ { \dagger } ) ^ { T } g - ( \Phi ^ { \dagger } ) ^ { T } D _ { k } ^ { T } P _ { \Phi } ^ { \perp } g = U R ^ { - 1 } ( P ^ { T } ( D _ { k } ^ { T } r ) ) .
$$

Both columns can be computed using matrix-vector products and triangular solves. The second part is somewhat more expensive to compute.

The variable projection approach reduces the dimension of the parameter space and leads to a more well-conditioned problem. Furthermore, because no starting values have to be provided for the linear parameters, convergence to a global minimum is more likely. Krogh [7O8,1974] reports that at the Jet Propulsion Laboratory (JPL) the variable projection algorithm solved several problems that methods not using separability could not solve.

Kaufman [686,1975l gave a simplified version of the variable projection algorithm that uses an approximate Jacobian matrix obtained by dropping the second term in (8.2.4). This simplification was motivated by the observation that the second part of the Jacobian is negligible when the residual $r$ is small. Kaufman's simplification reduces the arithmetic cost per iteration by about $2 5 \%$ , with only a marginal increase in the number of iterations. Kaufman and Pereyra [688,1978] extend the simplified scheme to problems with separable equality constraints. Their approach is further refined by Corradi [270,1981].

Ruhe and Wedin [942,198o] consider variable projection methods for more general separable problems, where one set of variables can be easily eliminated. They show that the asymptotic rate of convergence of the variable projection method is essentially the same as for the Gauss-Newton method applied to the full problem.Both converge quadratically for zero-residual problems, whereas ALS always converges linearly.

Several implementations of the variable projection method are available.An improved ver-sion of the original program VARPRO was given by John Bolstad in 1977. This uses Kaufman's modification that allows for weights on the observations and also computes the covariance matrix.A version called VARP2 by LeVeque handles multiple right-hand sides. Both VARPRO and VARP2 are available in the public domain at http://www.netlib. $\mathsf { o r g } / \mathsf { o p t } /$ . Another implementation was written by Linda Kaufman and David Gay for the Port Library. A welldocumented implementation in MATLAB written by O'Leary and Rust [839,2o13] uses the full Jacobian as in the original Golub-Pereyra version.The motivation is that in many current applications,the increase in the number of function evaluations in Kaufman's version outweighs the savings gained from using an approximate Jacobian.

# Notes and references

The variable projection method is an extension of ideas first presented by Scolnik [982,1972] and Guttman,Pereyra,and Scolnik [557,1973]. Osborne [846,1975] showed how to eliminate the linear parameters in separable problems. Golub and LeVeque [497,1979] extend variable projection algorithms to the case when several data sets are to be fitted to a model with the same nonlinear parameter vector; see also Kaufman and Sylvester [689,1992]. A review of developments and applications of the variable projection approach for separable nonlinear least squares problems is given by Golub and Pereyra [5O4, 2003].

# 8.2.2 - Bilinear Least Squares Problems

Given data $A _ { i } \in \mathbb { R } ^ { p \times q }$ and $b _ { i }$ ， $i = 1 , \ldots , m$ , the bilinear least squares (BLSQ) problem is to determine parameters $x \in \mathbb { R } ^ { p }$ and $y \in \mathbb { R } ^ { q }$ that minimize

$$
\sum _ { i = 1 } ^ { m } ( x ^ { T } A _ { i } y - b _ { i } ) ^ { 2 } , \quad m \geq p + q .
$$

This is a nonlinear least squares problem with objective function

$$
f ( x , y ) = \| r ( x , y ) \| _ { 2 } ^ { 2 } , \quad r _ { i } ( x , y ) = b _ { i } - x ^ { T } A _ { i } y \in \mathbb { R } ^ { p } , \quad i = 1 , \ldots , m ,
$$

that is separable in each of the variables $x$ and $y$ .In system theory,the identification of a Hammerstein model leads to a BLSQ problem; see Wang, Zhang,and Ljung [11O0, 2oog]. Related multilinear problems are used in statistics,chemometrics,and tensor regression.

The data matrices $A _ { i }$ formathre-dimensional tensor $\mathcal { A } \in \mathbb { R } ^ { m \times p \times q }$ with elements $a _ { i , j , k }$ Slicing the tensor in the two other possible directions,we obtain matrices

$$
R _ { j } \in \mathbb R ^ { m \times q } , \quad j = 1 , \dots , p , \qquad S _ { k } \in \mathbb R ^ { m \times p } , \quad k = 1 , \dots , q .
$$

The BLSQ problem is linear in each of the variables $x$ and $y$ If $( x , y )$ is a solution to problem BLSQ, $x$ solves the linear least squares problem

$$
\operatorname* { m i n } _ { \boldsymbol { x } } \| \boldsymbol { B } \boldsymbol { x } - \boldsymbol { b } \| _ { 2 } , \quad \boldsymbol { B } = \sum _ { k = 1 } ^ { q } y _ { k } \boldsymbol { S } _ { k } \in \mathbb { R } ^ { m \times p } ,
$$

where the matrices $S _ { k }$ are given as in (8.2.14). Similarly, $y$ solves

$$
\operatorname* { m i n } _ { y } \| C y - b \| _ { 2 } , \quad C = \sum _ { j = 1 } ^ { p } x _ { j } R _ { j } \in \mathbb { R } ^ { m \times q } .
$$

We deduce that the Jacobian of $r ( x , y )$ is

$$
J ( x , y ) = ( J _ { x } \quad J _ { y } ) = ( B \quad C ) \in \mathbb { R } ^ { m \times ( p + q ) } .
$$

For $\alpha \neq 0$ , the residuals $r _ { i } ( x , y ) = b _ { i } - x ^ { T } A _ { i } y$ of the bilinear problem (8.2.12) are invariant under the scaling $( \alpha x , \alpha ^ { - 1 } y )$ of the variables. This shows that the bilinear problem(8.2.12) is singular. The singularity can be handled by imposing a quadratic constraint $\| { \boldsymbol { x } } \| _ { 2 } = 1$ . Alternatively,a linear constraint $x _ { i } = e _ { i } ^ { T } x = 1$ for some $i$ $, 1 \leq i \leq m$ can be used. For convenience, we assume in the following that $i = 1$ $\mathbf { \boldsymbol { x } } _ { 1 } = 1$ ）and use the notation

$$
x = \binom { 1 } { \bar { x } } \in \mathbb { R } ^ { p } , \quad \bar { x } \in \mathbb { R } ^ { p - 1 } .
$$


<!-- chunk 0007: pages 421-490 -->
The residual $\bar { r } ( \bar { x } , y )$ of the constrained problem is $r ( x , y )$ with $x$ given as above. The Jacobian of the constrained problem is

$$
\hat { J } = \hat { J } ( \hat { x } , y ) = \left( \begin{array} { l l } { \hat { J } _ { \hat { x } } } & { J _ { y } } \end{array} \right) \in \mathbb { R } ^ { m \times ( p + q - 1 ) } ,
$$

where ${ \bar { J } } _ { \bar { x } }$ is $J _ { x }$ , with the first column deleted. The Hessian is

$$
H ( x , y ) = \bar { J } ^ { T } \bar { J } + \left( \begin{array} { c c } { 0 } & { \bar { A } _ { r } } \\ { \bar { A } _ { r } ^ { T } } & { 0 } \end{array} \right) , \quad \bar { A } _ { r } = \sum _ { i = 1 } ^ { m } r _ { i } ( x , y ) \bar { A } _ { i } \in \mathbb { R } ^ { ( p - 1 ) \times q } ,
$$

where ${ \bar { A } } _ { i }$ is $A _ { i }$ with the first row deleted.

In some applications the following simple alternating least squares (ALS) algorithm is often used.For a chosen initial approximation $y$ ,the matrix $B$ in (8.2.15) is formed,and the subproblem for $x$ is solved and normalized by setting $\| { \boldsymbol { x } } \| _ { 2 } = 1$ . Next, using the computed approximation for $x$ , the matrix $C$ in (8.2.16) is formed,and the subproblem is solved for $y$ .This is repeated until convergence. The linear subproblems are solved by QR or SVD. The arithmetic cost per iteration for ALS is 4pqm flops for forming $B$ and $C$ ,and about $2 m ( p ^ { 2 } + q ^ { 2 } )$ flops for solving the two linear problems. In general, the ALS algorithm converges slowly and is not guaranteed to converge to a local minimizer; see Ruhe and Wedin [942,1980].

Several nonlinear least squares algorithms can be used to solve BLSQ problems,such as the damped Gauss-Newton method. There are two possible versions of the variable projection (VP) method. In $\operatorname { V P x }$ ， $x$ is eliminated,and a nonlinear least squares problem for $y$ is solved. In VPy, the roles of $x$ and $y$ are interchanged. Newton's method with the Hessian given by (8.2.18) can also be applied. The VP methods have ultimately quadratic convergence,and the arithmetic cost per iteration is about the same as for ALS.

Hybrid algorithms can also be considered. For example,because Newton's method is sen-sitive to the initial approximation, it is best used in combination with a Gauss-Newton method. Switching to Newton's method in the later stages can considerably improve the rate of conver-gence. The ALS method converges slowly but may be used to initialize other methods.

Different nonlinear least squares algorithms for solving BLSQ problems are analyzed and evaluated by Eldén and Ahmadi-Asl [377,2o18]. They note that the choice of which component of $x$ (or $y$ ） to set equal to 1 can make a significant difference in the speed of convergence, especially if the problem is ill-conditioned. Based on a perturbation analysis, they recommend that the constraint be chosen so that the condition number of the Jacobian ${ \bar { J } } _ { x }$ is minimized. Their numerical experiments indicate that the $\operatorname { V P x }$ method, possibly combined with Newton's method for problems with slower convergence rate,is the method of choice.

# 8.2.3 - Orthogonal Distance Regression

Given a curve described by the parametric function

$$
y = f ( x , \beta ) \in \mathbb { R } ^ { q } , \quad x \in \mathbb { R } ^ { n } , \quad \beta \in \mathbb { R } ^ { p } ,
$$

let $y _ { i }$ and $x _ { i }$ ， $i = 1 , \ldots , m > p$ ,be observations of points on the curve subject to independent random errors $\bar { \epsilon } _ { i }$ and ${ \bar { \delta } } _ { i }$ with zero mean and variance $\sigma ^ { 2 }$ ，

$$
y _ { i } + { \bar { \epsilon } _ { i } } = f ( x _ { i } + { \bar { \delta } _ { i } } , \beta ) , \quad i = 1 , \ldots , m .
$$

In orthogonal distance regression (ODR) the parameters $\beta$ are determined by minimizing the sum of squares of the orthogonal distances from the observations $( x _ { i } , y _ { i } )$ to the curve $y = f ( x , { \boldsymbol { \beta } } )$ ; see Figure 8.2.1. If $\delta _ { i }$ and $\epsilon _ { i }$ do not have constant covariance matrices, then weighted norms should

![](../chunks/Numerical Methods for Least Squares Problems (Åke Björck) (z-library.sk, 1lib.sk, z-lib.sk_part_0007_pages_0421-0490/auto/images/4cb4d8a4a616b7051f61bc45bb5ab8fa9f167d585465c315473e94f3db31bb3d.jpg)  
Figure 8.2.1. Orthogonal distance regression for $q = n = 1$

be substituted above. If the errors in the independent variables are small, then ignoring these errors will not seriously degrade the estimates of $x$ .Independent of statistical considerations, the orthogonal distance measure has natural applications in fiting data to geometrical elements.

In linear orthogonal distance regression one wants to ft $m \ > \ n$ given points $y _ { i } \in \mathbb { R } ^ { n }$ $i = 1 { : } m$ , to a hyperplane

$$
M = \{ z \mid c ^ { T } z = d \} , \quad z , c \in \mathbb { R } ^ { n } , \quad \| c \| _ { 2 } = 1 ,
$$

where $c$ is the unit normal vector of $M$ ,and $| d |$ is the orthogonal distance from the origin to the plane in such a way that the sum of squares of the orthogonal distances from the given points to $M$ is minimized. For $n = 1$ this problem was studied in 1878 by Adcock[7,1878]. The orthogonal projection $z _ { i }$ of the point $y _ { i }$ onto $M$ is given by

$$
z _ { i } = y _ { i } - ( c ^ { T } y _ { i } - d ) c .
$$

It is readily verified that $z _ { i }$ lies on $M$ and that the residual $z _ { i } - y _ { i }$ is parallel to $c$ and hence orthogonal to $M$ .Hence,the problem of minimizing the sum of squares of the orthogonal distances is equivalent to minimizing

$$
\sum _ { i = 1 } ^ { m } ( c ^ { T } y _ { i } - d ) ^ { 2 } \quad { \mathrm { s u b j e c t ~ t o } } \quad \| c \| _ { 2 } = 1 .
$$

If we put $Y ^ { T } = ( y _ { 1 } , \dots , y _ { m } ) \in \mathbb { R } ^ { n \times m }$ and $e = ( 1 , \ldots , 1 ) ^ { T } \in \mathbb { R } ^ { m }$ , this problem can be written in matrix form as

$$
\operatorname* { m i n } _ { c , d } \left\| ( - e \quad Y ) \binom { d } { c } \right\| _ { 2 } \quad \mathrm { s u b j e c t } \mathrm { t o } \quad \| c \| _ { 2 } = 1 .
$$

For a fixed $c$ , this expression is minimized when the residual vector $Y c - d e$ is orthogonal to $e$ ， i.e., when $e ^ { T } ( Y c - d e ) = e ^ { T } Y c - d e ^ { T } e = 0$ Since $e ^ { T } e = m$ , it follows that

$$
d = \frac { 1 } { m } c ^ { T } Y ^ { T } e = c ^ { T } \bar { y } , \qquad \bar { y } = \frac { 1 } { m } Y ^ { T } e ,
$$

where $\bar { y }$ is the mean of the given points $P _ { i }$ .Hence $d$ is determined by the condition that the mean $\bar { y }$ lies on the optimal plane $M$ .Note that this property is shared by the solution to the usual linear regression problem.

We now subtract the mean value $\bar { y }$ from each given point and form the matrix

$$
\bar { Y } ^ { T } = ( \bar { y } _ { 1 } , \dots , \bar { y } _ { m } ) , \qquad \bar { y } _ { i } = y _ { i } - \bar { y } , \quad i = 1 { : } m .
$$

From (8.2.24) it follows that

$$
\left( - e \quad Y \right) \binom { d } { c } = Y c - e \bar { y } ^ { T } c = ( Y - e \bar { y } ^ { T } ) c = \bar { Y } c .
$$

Hence problem (8.2.23) is equivalent to

$$
\operatorname* { m i n } _ { c } \| { \bar { Y } } c \| _ { 2 } \quad { \mathrm { s u b j e c t ~ t o } } \quad \| c \| _ { 2 } = 1 .
$$

By the min-max characterization of the singular values,a solution is $c = v _ { n }$ ,where $v _ { n }$ is a right singular vector of $\bar { Y }$ corresponding to the smallest singular value $\sigma _ { n }$ . We further have

$$
d = v _ { n } ^ { T } \bar { y } , \qquad \sum _ { i = 1 } ^ { m } ( v _ { n } ^ { T } y _ { i } - d ) ^ { 2 } = \sigma _ { n } ^ { 2 } .
$$

Orthogonalizing the shifted points $\bar { y } _ { i }$ against $v _ { n }$ and adding back the mean value, we get the fitted points

$$
z _ { i } = \bar { y } _ { i } - ( v _ { n } ^ { T } \bar { y } _ { i } ) v _ { n } + \bar { y } \in M .
$$

The linear orthogonal regression problem always has a solution. The solution is unique when $\sigma _ { n - 1 } ~ > ~ \sigma _ { n }$ ，and the minimum sum of squares is $\sigma _ { n } ^ { 2 }$ .Moreover, $\sigma _ { n } ~ = ~ 0$ if and only if the given points $y _ { i }$ ， $i = 1 : m$ ,all lie on the hyperplane $M$ . In the extreme case when all points coincide, then $\bar { Y } = 0$ ,and any plane going through $\bar { y }$ is a solution. The above method solves the problem of fitting an $( n - 1 )$ -dimensional linear manifold to a given set of points in $\mathbb { R } ^ { n }$ .It is readily generalized to fitting an $( n - p )$ -dimensional linear manifold by orthogonalizing the shifted points $y$ against the $p$ right singular vectors of $Y$ corresponding to the $p$ smallest singular values.

In the nonlinear case (8.2.19),we first assume that $x \in \mathbb { R } ^ { n } , y \in \mathbb { R }$ .Then the parameters $\beta \in \mathbb { R } ^ { p }$ should be chosen as the solution to

$$
\operatorname* { m i n } _ { \beta , \epsilon , \delta } \sum _ { i = 1 } ^ { m } ( \epsilon _ { i } ^ { 2 } + \delta _ { i } ^ { 2 } ) \quad \mathrm { s u b j e c t ~ t o } \quad y _ { i } + \epsilon _ { i } = f ( x _ { i } + \delta _ { i } , \beta ) , \quad i = 1 , \dots , m .
$$

This is a constrained least squares problem of special form. By using the constraints to eliminate $\epsilon _ { i }$ ,the ODR problem can be formulated as an NLS problem in the parameters $\boldsymbol { \delta } = ( \delta _ { 1 } , \dots , \delta _ { n } )$ and $\beta$ ：

$$
\operatorname* { m i n } _ { \beta , \delta } \sum _ { i = 1 } ^ { m } \Big ( ( f ( x _ { i } + \delta _ { i } , \beta ) - y _ { i } ) ^ { 2 } + \delta _ { i } ^ { 2 } \Big ) .
$$

Note that even when $f ( x , \beta )$ is a linear function of $\beta$ , this is a nonlinear least squares problem. If we define the residual vector $\boldsymbol { r } = ( r _ { 1 } ^ { T } , ~ r _ { 2 } ^ { T } ) ^ { T }$ by

$$
r _ { 1 i } ( \delta , \beta ) = f ( x _ { i } + \delta _ { i } , \beta ) - y _ { i } , \qquad r _ { 2 i } ( \delta ) = \delta _ { i } ,
$$

then (8.2.27) is a standard NLS problem of the form $\mathrm { m i n } _ { x , \delta } \| r ( x , \delta ) \| _ { 2 } ^ { 2 }$ .The corresponding Jacobian matrix has the block structure

$$
\mathcal { I } = \binom { D } { V } \begin{array} { r } { 0 } \\ { J } \end{array} ) \in \mathbb { R } ^ { 2 m n \times ( m n + p ) } .
$$

Here $\begin{array} { r l r l } { D } & { { } > } & { 0 } \end{array}$ is_a diagonal matrix of order mn reflecting the variance in $\delta _ { i }$ ， $V = \operatorname { d i a g } \left( v _ { 1 } ^ { T } , \ldots , v _ { m } ^ { T } \right) \in \mathbb { R } ^ { m \times m n }$ ,and

$$
v _ { i } ^ { T } = \frac { \partial f ( x _ { i } + \delta _ { i } , \beta ) } { \partial x _ { i } } , \qquad J _ { i j } = \frac { \partial f ( x _ { i } + \delta _ { i } , \beta ) } { \partial \beta _ { j } } , \quad i = 1 , \ldots , m , \quad j = 1 , \ldots , p .
$$

Note that $\mathcal { I }$ is sparse and highly structured. In applications, usually $m n \gg p$ ,and then accounting for the errors $\delta _ { i }$ in $x _ { i }$ will considerably increase the size of the problem.Therefore,the use of standard NLS software to solve orthogonal distance problems is not efficient or even feasible. By taking the special structure of (8.2.27) into account, the work in ODR can be reduced to only slightly more than for an ordinary least squares fit of $\beta$

In the Gauss-Newton method, corrections $\Delta \delta _ { k }$ and $\Delta \beta _ { k }$ to the current approximations $\delta _ { k }$ and $\beta _ { k }$ are obtained from the linear least squares problem

$$
\operatorname* { m i n } _ { \Delta \delta , \Delta \beta } \left\| \mathcal { I } \left( \begin{array} { c } { \Delta \delta } \\ { \Delta \beta } \end{array} \right) - \left( \begin{array} { c } { r _ { 1 } } \\ { r _ { 2 } } \end{array} \right) \right\| _ { 2 } ,
$$

where ${ \mathcal { I } } , r _ { 1 }$ ,and $r _ { 2 }$ are evaluated at $\delta _ { k }$ and $\beta _ { k }$ . A stable way to solve this problem is to compute the QR decomposition of $\mathcal { I }$ . First,a sequence of plane rotations is used to zero the (2,1) block $V$ of $\mathcal { I }$ . The rotations are also applied to the right-hand side vector. We obtain

$$
Q _ { 1 } \bar { \mathcal { I } } = \left( \begin{array} { c c } { U } & { K } \\ { 0 } & { \bar { \mathcal { I } } } \end{array} \right) , \qquad Q _ { 1 } \left( \begin{array} { c } { r _ { 1 } } \\ { r _ { 2 } } \end{array} \right) = \left( \begin{array} { c } { t } \\ { \bar { r } _ { 2 } } \end{array} \right) ,
$$

where $U$ is a block diagonal matrix with $m$ upper triangular blocks of size $n \times n$ .Problem (8.2.29) now decouples, and $\Delta \beta$ is determined as the solution to

$$
\operatorname* { m i n } _ { \Delta \beta } | | \bar { J } \Delta \beta - \bar { r } _ { 2 } | | _ { 2 } ,
$$

where $\bar { J } \in \mathbb { R } ^ { m \times n }$ . This second step has the same complexity as computing the Gauss-Newton correction in the classical NLS problem. When $\Delta \beta$ has been determined, $\Delta \delta$ is obtained by back-substitution:

$$
U \Delta \delta = u _ { 1 } , \quad u _ { 1 } = t - K \Delta \beta .
$$

More generally, when $\boldsymbol { y } \in \mathbb { R } ^ { q }$ and $x \in \mathbb { R } ^ { n }$ ,the ODR problem has the form

$$
\operatorname* { m i n } _ { \beta , \delta } \sum _ { i = 1 } ^ { m } \Big ( \| f ( x _ { i } + \delta _ { i } , \beta ) - y _ { i } \| _ { 2 } ^ { 2 } + \| \delta _ { i } \| _ { 2 } ^ { 2 } \Big ) .
$$

When $q > 1$ ,the Jacobian (8.2.28) has a similar structure with

$$
V = \operatorname { d i a g } \big ( V _ { 1 } ^ { T } , V _ { 2 } ^ { T } , \ldots , V _ { m } ^ { T } \big ) , \quad V _ { i } ^ { T } \in \mathbb { R } ^ { q \times n } .
$$

After an orthogonal reduction to upper triangular form,the reduced Jacobian has the same block structure as in (8.2.30). However, now $D \in \mathbb { R } ^ { m n _ { t } \times m n _ { t } }$ is block diagonal with upper triangular matrices of size $n _ { t } \times n _ { t }$ on the diagonal, $K \in \mathbb { R } ^ { m n _ { t } \times n }$ ,and $\bar { \boldsymbol { J } } \in \mathbb { R } ^ { m n _ { y } \times n }$

In practice a trust-region stabilization of the Gauss-Newton step should be used,and then we need to solve (8.2.29) with

$$
\mathcal { I } _ { \mu } = \left( \begin{array} { c c } { D } & { 0 } \\ { V } & { J } \\ { \mu T } & { 0 } \\ { 0 } & { \mu S } \end{array} \right) , \qquad r = \left( \begin{array} { c c } { r _ { 1 } } \\ { r _ { 2 } } \\ { 0 } \\ { 0 } \end{array} \right) ,
$$

with several different values of the parameter $\mu$ ，where $S$ and $T$ are nonsingular diagonal matrices. An orthogonal reduction to upper triangular form would result in a matrix with the same block structure as in (8.2.30), where $D \in \mathbb { R } ^ { m n \times m n }$ is block diagonal with upper triangular matrices of size $n \times n$ on the diagonal. Therefore, if done in a straightforward way, this reduction does not take full advantage of the structure in the blocks and is not efficient.

Boggs, Byrd,and Schnabel $[ 1 5 8 , 1 9 8 7 ]$ show how the computations in a trust-region step can be carried out so that the cost is of the same order as for a standard least squares fit. They claim that computing a QR factorization of $\mathcal { I } _ { \mu }$ would require $O ( ( m n + p ) ^ { 2 } )$ operations for each $\mu$ For this reason the $\Delta \delta$ variables are eliminated as outlined above by using the normal equations, combined with the Woodbury formula (3.3.9). The reduced least squares problem for $\Delta \beta$ can then be written $\operatorname* { m i n } { \lVert \tilde { J } \Delta \beta - \tilde { r } _ { 2 } \rVert _ { 2 } }$ ,where

$$
\tilde { J } = \left( \begin{array} { c } { { M J } } \\ { { \mu S } } \end{array} \right) , \qquad \tilde { r } _ { 2 } = \left( \begin{array} { c } { { - M ( r _ { 1 } - V E ^ { - 2 } D r _ { 2 } ) } } \\ { { 0 } } \end{array} \right) ,
$$

and $E ^ { 2 } = D ^ { 2 } + \mu ^ { 2 } T ^ { 2 }$ . An explicit expression for the diagonal matrix $M$ is given by Boggs, Byrd,and Schnabel [158, $\mathrm { 1 9 8 7 } ]$ in terms of $E$ and $V$

For the case $q = 1$ , Boggs,Byrd,and Schnabel [158,1987] give a more efficient algorithm to carry out elimination of the $\delta$ variables in a trust-region step so that the cost of a step is dominated by the QR factorization of $\tilde { J }$ ，This is achieved by eliminating the $\Delta \delta$ variables using the normal equations and the Woodbury formula (3.3.9). The reduced normal equations for $\Delta \beta$ is then interpreted as the normal equations for a least squares problem with matrix

$$
\tilde { J } = \left( \begin{array} { c } { { M J } } \\ { { \mu S } } \end{array} \right) , \qquad \tilde { r } _ { 2 } = \left( \begin{array} { c } { { - M ( r _ { 1 } - V E ^ { - 1 } D r _ { 2 } ) } } \\ { { 0 } } \end{array} \right) ,
$$

where $E = D ^ { 2 } + \mu ^ { 2 } T ^ { 2 }$ ,and an explicit expression for the diagonal $M$ can be given in terms of $E$ and $V$ ． A software package ODRPACK for orthogonal distance regression based on this algorithm is described in Boggs et al. [159,1989].

Schwetlick and Tiller [980,1985l, [981，198g] develop an ODR algorithm based on the Gauss-Newton method with a special Marquardt-type regularization for which similar simplifications can be achieved. The path

$$
p ( \mu ) : = - ( \Delta \delta ( \mu ) ^ { T } , \Delta x ( \mu ) ^ { T } ) ^ { T }
$$

is shown to be equivalent to a trust-region path defined by a nonstandard scaling matrix,and the step is controlled in trust-region style.

An algorithm for computing the trust-region step based on QR factorization of $\mathcal { I } _ { \boldsymbol { \mu } }$ is given by Bjorck [136, 20o2]. Because only part of $U$ and $Q _ { 1 }$ need to be computed and saved, this has the same leading arithmetic cost as the normal equation algorithm by Boggs et al. By taking advantage of the special structure of $\mathcal { I } _ { \boldsymbol { \mu } }$ ,only part of the nonzero elements in the factors $Q$ and $R$ need to be stored.In the first step of the factorization, plane rotations are used to merge the two diagonal blocks $D$ and $\mu T$ . After a permutation of the last two block rows,we obtain

$$
G ( \begin{array} { c c } { { D } } & { { 0 } } \\ { { V } } & { { J } } \\ { { 0 } } & { { \mu S } } \\ { { \mu T } } & { { 0 } } \end{array} ) \ : r _ { 1 } = ( \begin{array} { c c } { { D _ { \mu } } } & { { 0 } } \\ { { V } } & { { J } } \\ { { 0 } } & { { \mu S } } \\ { { 0 } } & { { 0 } } \end{array} ) \ : \tilde { r } _ { 2 } \ : ) ,
$$

where $D _ { \mu } = ( D ^ { 2 } + \mu ^ { 2 } T ^ { 2 } ) ^ { 1 / 2 }$ is diagonal. The rotations are also applied to the right-hand side. This step does not affect the second block column and the last block row in $\mathcal { I } _ { \boldsymbol { \mu } }$ . The key step is orthogonal triangularization of the first block column in (8.2.34). This will not affect the last two block rows and can be carried out efficiently if full advantage is taken of the structure of blocks $D _ { \mu }$ and $V$

A nonlinear least squares problem with structure similar to ODR arises in structured total least squares problems. Given the data matrix $A$ and the vector $b$ ,the TLS problem is to find $E$ and $x$ to solve

$$
\operatorname* { m i n } \| ( E \ r ) \| _ { F } \quad { \mathrm { s u c h } } \operatorname { t h a t } \quad r = b - ( A + E ) x .
$$

If $A$ is sparse, we may want $E$ to have the same sparsity structure.Rosen, Park,and Glick [936, 1996] impose an affine structure on $E$ by defining a matrix $X$ such that $X \delta = E x$ ,where $\delta \in \mathbb { R } ^ { q }$ is a vector containing the nonzero elements of $E$ ,and the elements of $\ b X \in \mathbb { R } ^ { m \times q }$ consist of the elements of the vector $x$ with a suitable repetition. Then the problem can be written as a nonlinear least squares problem

$$
\operatorname* { m i n } _ { \delta , x } \left\| \left( { \begin{array} { c } { \delta } \\ { r ( \delta , x ) } \end{array} } \right) \right\| , \quad r ( \delta , x ) = A x - b + X \delta .
$$

When $E$ is general and sparse, the structure of the Jacobian of $r$ with respect to $\delta$ will be similar to that in the ODR problem.

# 8.2.4 - Fitting of Circles and Ellipses

A special nonlinear least squares problem that often arises is to fit given data points to a geometrical element, which may be defined implicitly. We have already discussed fiting data to an affine linear manifold such as a line or a plane. Gander and von Matt [44O,1997] show how to fit rectangles and squares using simple generalizations of this algorithm. The problem of fitting circles,ellpses,spheres,and cylinders arises in applications in computer graphics,coordinate meteorology,and the aircraft industry.

Least squares algorithms to fit a curve in the $x , y$ -plane implicitly defined by the scalar function $f ( x , y , p ) ~ = ~ 0$ can be divided into two classes. In algebraic fittng,the least squares functional

$$
\phi ( p ) = \sum _ { i = 1 } ^ { m } f ( x _ { i } , y _ { i } , p ) ^ { 2 }
$$

is minimized and it directly involves the function $f ( x , y , p )$ ； see Pratt [905,1987]. In geometric fitting,a least squares functional is minimized and involves the geometric distances from the data points to the curve defined by $f ( x , y , p ) = 0$ ，

$$
\operatorname* { m i n } _ { p } \sum _ { i = 1 } ^ { m } d _ { i } ^ { 2 } ( p ) , \quad d _ { i } ^ { 2 } ( p ) = \operatorname* { m i n } _ { f ( x , y , p ) = 0 } \bigl ( ( x - x _ { i } ) ^ { 2 } + ( y - y _ { i } ) ^ { 2 } \bigr ) ,
$$

where $d _ { i } ( p )$ is the orthogonal distance from the data point $( x _ { i } , y _ { i } )$ to the curve. This is similar to orthogonal distance regression described for an explicitly defined function $y \ = \ f ( x , \beta )$ in Section 8.2.3.However,for implicitly defined functions the calculation of the distance function $d _ { i } ( p )$ is more complicated.

Algebraic fitting often leads to a simpler problem, in particular when $f$ is linear in the parameters $p$ . Methods for geometrical fitting are slower but give better results both conceptually and visually. Implicit curve fitting problems,where a model $h ( y , x , t ) = 0$ is to be fitted to observations $( y _ { i } , t _ { i } ) , i = 1 , \ldots , m$ ，can be formulated as a special least squares problem with nonlinear constraints:

$$
\operatorname* { m i n } _ { x , z } \| z - y \| _ { 2 } ^ { 2 } \quad { \mathrm { s u b j e c t ~ t o } } \quad h ( z _ { i } , x , t _ { i } ) = 0 .
$$

This is a special case of problem (8.1.38). It has $n + m$ unknowns $x$ and $z$ ,but the sparsity of the Jacobian matrices can be taken advantage of; see Lindstrom [750,1984].

We first discuss algebraic fitting of circles and ellipses in two dimensions.A circle has three degrees of freedom and can be represented algebraically by

$$
f ( x , y , p ) = a ( x ^ { 2 } + y ^ { 2 } ) + b _ { 1 } x + b _ { 2 } y - c = 0 ,
$$

where $\boldsymbol { p } = ( a b _ { 1 } b _ { 2 } c ) ^ { T } .$ Let $S$ be an $m \times 4$ matrix with rows

$$
s _ { i } ^ { T } = ( x _ { i } ^ { 2 } + y _ { i } ^ { 2 } x _ { i } y _ { i } - 1 ) , i = 1 , \ldots , m .
$$

The algebraic fiting problem (8.2.37) of a circle can then be formulated as

$$
\operatorname* { m i n } _ { \boldsymbol { p } } \| S \boldsymbol { p } \| _ { 2 } ^ { 2 } \quad \mathrm { s u b j e c t } \mathrm { t o } \quad p ^ { T } e _ { 1 } = a = 1 .
$$

The constraint is added because $p$ is only defined up to a constant multiple. This problem is equivalent to the linear least squares problem

$$
\operatorname* { m i n } _ { q } \| S _ { 2 } q - s _ { 1 } \| _ { 2 } , \quad S = \left( s _ { 1 } \quad S _ { 2 } \right) .
$$

For plotting, the circle can more conveniently be represented in parametric form,

$$
{ \binom { x ( \theta ) } { y ( \theta ) } } = { \binom { x _ { c } } { y _ { r } } } + r \left( { \binom { \cos \theta } { \sin \theta } } \right) ,
$$

where the center $( x _ { c } y _ { c } ) ^ { T }$ and radius $r$ of the circle can be expressed in terms of $p$ as

$$
\left( { \begin{array} { l } { x _ { c } } \\ { y _ { c } } \end{array} } \right) = - { \frac { 1 } { 2 a } } \left( { \begin{array} { l } { b _ { 1 } } \\ { b _ { 2 } } \end{array} } \right) , \qquad r = { \frac { 1 } { 2 a } } { \sqrt { \| b \| _ { 2 } ^ { 2 } + 4 a c } } .
$$

From this expression we see that the constraint $2 a r = 1$ can be written as a quadratic constraint $b _ { 1 } ^ { 2 } + b _ { 2 } ^ { 2 } + 4 a c = p ^ { T } C p = 1$ ,where

$$
p = \left( { \begin{array} { l } { a } \\ { b _ { 1 } } \\ { b _ { 2 } } \\ { c } \end{array} } \right) , \qquad C = \left( { \begin{array} { l l l l } { 0 } & { 0 } & { 0 } & { 2 } \\ { 0 } & { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } & { 0 } \\ { 2 } & { 0 } & { 0 } & { 0 } \end{array} } \right) .
$$

This will guarantee that a circle is fitted. (Note that equality can be used in the constraint because of the free scaling.） The matrix $C$ is symmetric but not positive definite (its eigenvalues are $- 2 , 1 , 1 , 2 )$ . We discuss the handling of such quadratic constraints later when dealing with ellipses.

An ellipse in the $x , y$ plane can be represented algebraically by

$$
f ( x , y , p ) = \left( x y A { \binom { x } { y } } A { \binom { x } { y } } + \left( b _ { 1 } b _ { 2 } \right) { \binom { x } { y } } - c = 0 , A = { \binom { a _ { 1 1 } } { a _ { 1 2 } } } A _ { 2 2 } \right) .
$$

Following Varah [1089,1996], we define

$$
p = ( a _ { 1 1 } a _ { 1 2 } a _ { 2 2 } b _ { 1 } b _ { 2 } c ) ^ { T } , \qquad s _ { i } ^ { T } = ( x _ { i } ^ { 2 } 2 x _ { i } y _ { i } y _ { i } ^ { 2 } x _ { i } y _ { i } - 1 ) .
$$

Then the objective function is $\Phi ( p ) = \| S p \| _ { 2 } ^ { 2 }$ , where $S$ is an $m \times 6$ matrix with rows $s _ { i } ^ { T }$ . Because the parameter vector $p$ is only determined up to a constant factor, the problem formulation must be completed by including some constraint on $p$ .Three such constraints have been considered.

# (a) SVD constraint:

$$
\operatorname* { m i n } _ { \boldsymbol { p } } \| S \boldsymbol { p } \| _ { 2 } ^ { 2 } \quad \mathrm { s u b j e c t t o } \quad \| \boldsymbol { p } \| _ { 2 } = 1 .
$$

The solution of this constrained problem is the right singular vector corresponding to the smallest singular value of $S$

# (b)Linear constraint:

$$
\operatorname* { m i n } _ { \boldsymbol { p } } \| \boldsymbol { S } \boldsymbol { p } \| _ { 2 } ^ { 2 } , \quad \mathrm { w h e r e } \quad \boldsymbol { d } ^ { T } \boldsymbol { p } = 1 ,
$$

where $d$ is a fixed vector with $\| d \| _ { 2 } = 1$ Let $H$ be an orthogonal matrix such that $H d = e _ { 1 }$ . Then the constraint becomes $d ^ { T } p = d ^ { T } H ^ { T } H p = e _ { 1 } ^ { T } ( H p ) = 1$ , so we can write $\begin{array} { r } { S p = ( S H ^ { T } ) ( H p ) } \end{array}$ ， where $H p = ( 1 \ : q ^ { T } ) ^ { T }$ . Now, if we form $S H ^ { \bar { T } } = \bar { \tilde { S } } = [ \tilde { s } _ { 1 } \ \tilde { S } _ { 2 } ]$ , we arrive at the unconstrained linear least squares problem

$$
\operatorname* { m i n } _ { \boldsymbol q } \| \tilde { S } _ { 2 } \boldsymbol q + \tilde { s } _ { 1 } \| _ { 2 } ^ { 2 } \quad \mathrm { s u b j e c t ~ t o } \quad p = H ^ { T } \left( \begin{array} { l } { 1 } \\ { \boldsymbol q } \end{array} \right) .
$$

# (c) Quadratic constraint:

$$
\operatorname* { m i n } _ { \boldsymbol { p } } \| S p \| _ { 2 } ^ { 2 } \quad \mathrm { s u b j e c t } \mathrm { t o } \quad \boldsymbol { p } ^ { T } C \boldsymbol { p } = 1 .
$$

For general symmetric $C$ , problem (8.2.46) reduces to the generalized eigenvalue problem

$$
( C - \lambda S ^ { T } S ) p = 0 .
$$

If $C$ is well-conditioned, this can be reformulated as a standard eigenvalue problem $C ^ { - 1 } S ^ { T } S p =$ $\lambda ^ { - 1 } p$ but can potentially result in a loss of accuracy if $S ^ { T } S$ is formed explicitly. When $C$ is positive definite, we can write $C = B ^ { T } B$ ,and the constraint becomes $\| B p \| _ { 2 } = 1$ .The solution is related to the generalized eigenvalue problem

$$
( B ^ { T } B - \lambda S ^ { T } S ) p = 0 .
$$

Since $\lambda \| S p \| _ { 2 } = \| B p \| _ { 2 } = 1$ , we want the eigenvector $p$ corresponding to the largest eigenvalue $\lambda$ or, equivalently, the largest eigenvalue of $( S ^ { T } S ) ^ { - 1 } B ^ { T } B$ If $S = Q R$ is the QR factorization of $S$ with $R$ nonsingular, the eigenvalue problem (8.2.47) can be written

$$
\lambda q = ( B R ^ { - 1 } ) ^ { T } B R ^ { - 1 } q , \quad q = R p .
$$

Hence, $q$ is the right singular vector corresponding to the largest singular value of $B R ^ { - 1 }$ .Of special interest is the choice $B = ( 0 ~ I )$ . In this case,the constraint can be written $\| p _ { 2 } \| _ { 2 } ^ { 2 } = 1$ ， where $p = \left( p _ { 1 } p _ { 2 } \right)$ . With $R$ conformally partitioned with $p$ , problem (8.2.46) is equivalent to the generalized total least squares problem

$$
\operatorname* { m i n } _ { p } \left\| \left( { \begin{array} { c c } { R _ { 1 1 } } & { R _ { 1 2 } } \\ { 0 } & { R _ { 2 2 } } \end{array} } \right) \left( { \begin{array} { c } { p _ { 1 } } \\ { p _ { 2 } } \end{array} } \right) \right\| _ { 2 } ^ { 2 } \quad { \mathrm { s u b j e c t ~ t o } } \quad \| p _ { 2 } \| _ { 2 } = 1 .
$$

For any $p _ { 2 }$ we can determine $p _ { 1 }$ so that $R _ { 1 1 } p _ { 1 } + R _ { 1 2 } p _ { 2 } = 0$ Hence $p _ { 2 }$ solves $\begin{array} { r } { \operatorname* { m i n } _ { p _ { 2 } } { \| R _ { 2 2 } p _ { 2 } \| _ { 2 } } } \end{array}$ subject to $\| p _ { 2 } \| _ { 2 } = 1$ and can be obtained from the SVD of $R _ { 2 2 }$

If $\sigma _ { \mathrm { m i n } } ( S ) = 0$ ,the data exactly fit the ellipse. If $\sigma _ { \mathrm { m i n } } ( S )$ is small,the different constraints above give similar solutions. However, when errors are large,the different constraints can lead to very different solutions; see Varah [1O89,1996].

A desirable property of a fitting algorithm is that when the data are translated and rotated, the fitted ellipse should be transformed in the same way. It can be shown that to have this invariance, the constraint must involve only symmetric functions of the eigenvalues of $A$ . The SVD constraint does not have this property. For a linear constraint, the choice $d ^ { T } = ( 1 \ 0 \ 1 \ 0 \ 0 \ 0 )$ gives the desired invariance:

$$
d ^ { T } p = a _ { 1 1 } + a _ { 2 2 } = \operatorname { t r a c e } ( A ) = \lambda _ { 1 } + \lambda _ { 2 } = 1 .
$$

The quadratic constraint proposed by Bookstein [170,1979],

$$
\| A \| _ { F } ^ { 2 } = a _ { 1 1 } ^ { 2 } + 2 a _ { 1 2 } ^ { 2 } + a _ { 2 2 } ^ { 2 } = \lambda _ { 1 } ^ { 2 } + \lambda _ { 2 } ^ { 2 } = 1 ,
$$

also leads to this kind of invariance.Note that the Bookstein constraint can be put in the form $\| B p \| _ { 2 } = 1$ ， $B = ( 0 I )$ ,by permuting the variables and scaling by $\sqrt { 2 }$ ：

$$
p = ( b _ { 1 } , b _ { 2 } , c , a _ { 1 1 } , \sqrt { 2 } a _ { 1 2 } , a _ { 2 2 } ) ^ { T } , \qquad s _ { i } ^ { T } = ( x _ { i } , y _ { i } , - 1 , x _ { i } ^ { 2 } , \sqrt { 2 } x _ { i } y _ { i } , y _ { i } ^ { 2 } ) .
$$

Another useful quadratic constraint is $p ^ { T } C p = a _ { 1 1 } a _ { 2 2 } - a _ { 1 2 } ^ { 2 } = \lambda _ { 1 } \lambda _ { 2 } = 1$ This has the advantage of guaranteeing that an ellipse is generated rather than another conic section. Note that the matrix $C$ corresponding to this constraint is not positive definite, so it leads to a generalized eigenvalue problem.

To plot the ellipse, it is convenient to convert the algebraic form (8.2.42) to the parametric form

$$
\binom { x ( \theta ) } { y ( \theta ) } = \binom { x _ { c } } { y _ { c } } + G ( \alpha ) \binom { a \cos \theta } { b \sin \theta } , \quad G ( \alpha ) = \left( \begin{array} { l l } { \cos \alpha } & { \sin \alpha } \\ { - \sin \alpha } & { \cos \alpha } \end{array} \right) ,
$$

where $G ( \alpha )$ is a rotation with angle $\alpha$ .The new parameters $( x _ { c } , y _ { c } , a , b , \alpha )$ can be obtained from the algebraic parameters $p$ by the eigenvalue decomposition $A = G ( \alpha ) \Lambda G ( \alpha ) ^ { T }$ as follows. We assume that $\boldsymbol { \Lambda } = \operatorname { d i a g } \left( \lambda _ { 1 } , \lambda _ { 2 } \right)$ .If $a _ { 1 2 } = 0$ ,take $G ( \alpha ) = I$ and $\Lambda = A$ .Otherwise,compute $t = \tan ( \alpha )$ from

$$
\tau = ( a _ { 2 2 } - a _ { 1 1 } ) / ( 2 a _ { 1 2 } ) , \qquad t = \mathrm { s i g n } ( \tau ) / \big ( | \tau | + \sqrt { 1 + \tau ^ { 2 } } \big ) .
$$

This ensures that $| \alpha | < \pi / 4$ . Then $\cos \alpha = 1 / \sqrt { 1 + t ^ { 2 } }$ ， $\sin \alpha = t \cos \alpha$ ， $\lambda _ { 1 } = a _ { 1 1 } - t a _ { 1 2 }$ ,and $\lambda _ { 2 } = a _ { 2 2 } + t a _ { 1 2 }$ . The center of the ellipse is given by

$$
\left( { \begin{array} { l } { x _ { c } } \\ { y _ { c } } \end{array} } \right) = - { \frac { 1 } { 2 } } A ^ { - 1 } b = - { \frac { 1 } { 2 } } G ( \alpha ) \Lambda ^ { - 1 } G ( \alpha ) ^ { T } b ,
$$

and the axis is $( a , \ b ) = \left( \sqrt { \tilde { c } / \lambda _ { 1 } } , \ \sqrt { \tilde { c } / \lambda _ { 2 } } \right)$ , where

$$
\tilde { c } = c - \frac { 1 } { 2 } b ^ { T } \left( \begin{array} { l } { x _ { c } } \\ { y _ { c } } \end{array} \right) = c + \frac { 1 } { 4 } b ^ { T } G ( \alpha ) \Lambda ^ { - 1 } G ( \alpha ) ^ { T } b .
$$

The algorithms described here can be generalized for fiting conic sections in three dimen-sions. In some applications,e.g.,lens-making, it is required to fit a sphere to points representing only a small patch of the sphere surface.For a discussion of this case,see Forbes [419,1989]. Other fiting problems,such as fitting a cylinder, circle,or cone in three dimensions,are considered in Forbes [418,1989].

In geometric fittng of circles and ellipses,the sum of orthogonal distances from each data point to the curve is minimized. When the curve admits a parametrization, such as in the case of fitting a circle and ellipse,this simplifies.We first consider fiting of a circle writen in parametric form as

$$
\begin{array} { r } { f ( x , y , p ) = \left( \begin{array} { l } { x - x _ { c } - r \cos \theta } \\ { y - y _ { c } - r \sin \theta } \end{array} \right) = 0 , } \end{array}
$$

where $\boldsymbol { p } = ( x _ { c } , y _ { c } , r ) ^ { T }$ . The problem can be written as a nonlinear least squares problem

$$
\operatorname* { m i n } _ { \boldsymbol { p } , \boldsymbol { \theta } } \| \boldsymbol { r } ( \boldsymbol { p } , \boldsymbol { \theta } ) \| _ { 2 } ^ { 2 } , \quad \boldsymbol { \theta } = ( \theta _ { 1 } , \ldots , \theta _ { m } ) ^ { T } ,
$$

where $r$ is a vector of length $2 m$ with components

$$
r _ { i } = \left( \begin{array} { c c } { { x _ { i } - x _ { c } - r \cos \theta _ { i } } } \\ { { y _ { i } - y _ { c } - r \sin \theta _ { i } } } \end{array} \right) , \quad i = 1 , \dots , m .
$$

As an initial approximation we can take $x _ { c } , y _ { c } , r$ from an algebraically fitted circle.We determine initial approximations for $\theta _ { i }$ from $\tan \theta _ { i } = ( y _ { i } - y _ { c } ) / ( x _ { i } - x _ { c } )$ .To apply the Gauss一 Newton method to (8.2.54), we need the Jacobian of $r$ . We get

$$
\frac { \partial r _ { i } } { \partial \theta _ { i } } = r \left( \begin{array} { c } { \sin \theta _ { i } } \\ { - \cos \theta _ { i } } \end{array} \right) , \qquad \frac { \partial r _ { i } } { \partial r } = - \left( \begin{array} { c } { \cos \theta _ { i } } \\ { \sin \theta _ { i } } \end{array} \right) , \qquad \left( \frac { \partial r _ { i } } { \partial x _ { c } } , \quad \frac { \partial r _ { i } } { \partial y _ { c } } \right) = - \left( \begin{array} { c c } { 1 } & { 0 } \\ { 0 } & { 1 } \end{array} \right) .
$$

After reordering of rows,the Jacobian associated with this problem has the form

$$
J = \left( \begin{array} { c c } { { r S } } & { { A } } \\ { { - r C } } & { { B } } \end{array} \right) ,
$$

where $S = \mathrm { d i a g } \left( \sin \theta _ { 1 } , \dots , \sin \theta _ { m } \right)$ and $C = \operatorname { d i a g } \left( \cos \theta _ { 1 } , \dots , \cos \theta _ { m } \right)$ . The first $m$ columns of $J$ correspond to the parameters $\theta$ and are mutually orthogonal. Multiplying from the left with the orthogonal matrix $\overset { \cdot } { Q ^ { T } } = \left( \begin{array} { c c } { S } & { - C } \\ { C } & { S } \end{array} \right)$ , we obtain

$$
\begin{array} { r } { Q ^ { T } J = \left( \begin{array} { c c } { r I } & { S A - C B } \\ { 0 } & { C A + S B } \end{array} \right) . } \end{array}
$$

Hence to compute the QR factorization of $J$ and the Gauss-Newton search direction for problem (8.2.54),we only need to compute the QR factorization of the $m \times 3$ matrix $C A + S B$ A trust-region stabilization can easily be added.

For the geometrical fiting of an elipse we proceed similarly. We now have the parametric form (8.2.51),

$$
f ( x , y , p ) = \left( { x - x _ { c } } \right) - G ( \alpha ) \left( { a \cos \theta } \atop { b \sin \theta } \right) , \qquad G ( \alpha ) = \left( { \begin{array} { l l } { \cos \alpha } & { \sin \alpha } \\ { - \sin \alpha } & { \cos \alpha } \end{array} } \right) ,
$$

where $p = ( x _ { c } , y _ { c } , a , b , \alpha ) ^ { T }$ . The problem can be writen as a nonlinear least squares problem (8.2.54) if we define $r$ as a vector of length $2 m$ with

$$
r _ { i } = \binom { x _ { i } - x _ { c } } { y _ { i } - y _ { c } } - G ( \alpha ) \binom { a \cos \theta _ { i } } { b \sin \theta _ { i } } .
$$

As for the circle,we can take as initial approximation for $p$ the values for an algebraically fitted ellipse. To obtain initial values for $\theta _ { i }$ we note that for a point $( x ( \theta ) , y ( \theta ) )$ on the ellipse, we have from (8.2.51)

$$
\binom { a \cos { \theta } } { b \sin { \theta } } = G ^ { T } ( \alpha ) \left( { x ( \theta ) - x _ { c } \atop y ( \theta ) - y _ { c } } \right) .
$$

As an initial approximation one can take $\theta _ { i } = \arctan ( v _ { i } / u _ { i } )$ ,where

$$
\begin{array} { r } { \left( \begin{array} { l } { u _ { i } } \\ { v _ { i } } \end{array} \right) = G ^ { T } ( \alpha ) \left( \begin{array} { l } { ( x _ { i } - x _ { c } ) / a } \\ { ( y _ { i } - y _ { c } ) / b } \end{array} \right) , \quad i = 1 , \dots , m . } \end{array}
$$

To evaluate the Jacobian we need the partial derivatives

$$
\frac { \partial r _ { i } } { \partial \theta _ { i } } = G ( \alpha ) \left( \begin{array} { c } { { a \sin \theta _ { i } } } \\ { { - b \cos \theta _ { i } } } \end{array} \right) , \qquad \left( \frac { \partial r _ { i } } { \partial a } , \frac { \partial r _ { i } } { \partial b } \right) = - G ( \alpha ) \left( \begin{array} { c c } { { \cos \theta _ { i } } } & { { 0 } } \\ { { 0 } } & { { \sin \theta _ { i } } } \end{array} \right) ,
$$

and

$$
\frac { \partial r _ { i } } { \partial \alpha } = - G ^ { \prime } ( \alpha ) \left( { { a } \atop { b \sin { \theta _ { i } } } } \right) , \qquad G ^ { \prime } ( \alpha ) = \left( { - \sin \alpha } \quad { \cos \alpha } \atop { - \cos \alpha }  \right) .
$$

To simplify,multiply the Jacobian from the left by the $2 m \times 2 m$ block diagonal orthogonal matrix $\mathrm { d i a g } \left( G ^ { T } ( \alpha ) , \ldots , G ^ { T } ( \alpha ) \right)$ , noting that

$$
G ( \alpha ) ^ { T } \frac { \partial r _ { i } } { \partial \alpha } = \left( \begin{array} { l } { - b \sin \theta _ { i } } \\ { a \cos \theta _ { i } } \end{array} \right) , \qquad G ( \alpha ) ^ { T } G ( \alpha ) ^ { \prime } = \left( \begin{array} { l l } { 0 } & { 1 } \\ { - 1 } & { 0 } \end{array} \right) .
$$

With rows reordered, the structure of the transformed Jacobian is similar to the circle case,

$$
\begin{array} { r } { J = \left( \begin{array} { c c } { a S } & { A } \\ { - b C } & { B } \end{array} \right) , \quad S = \mathrm { d i a g } ( \sin \theta _ { i } ) , \quad C = \mathrm { d i a g } ( \cos \theta _ { i } ) , } \end{array}
$$

where $A$ and $B$ are now $m \times 5$ matrices. The first block column can easily be triangularized using the diagonal form of $S$ and $C$ . The main work is the final triangularization of the resulting (2,2) block. If $a = b$ ,the sum of the first $m$ columns of $J$ is zero.In this case the parameter $\alpha$ is not well determined,and it is essential to use some kind of regularization of $\alpha$

The fitting of a sphere or an elipsoid can be treated analogously. The sphere can be represented in parametric form as

$$
\begin{array} { r } { f ( x , y , z , p ) = \left( \begin{array} { c } { x - x _ { \mathrm { c } } - r \cos \theta \cos \phi } \\ { y - y _ { \mathrm { c } } - r \cos \theta \sin \phi } \\ { z - z _ { \mathrm { c } } - r \sin \theta } \end{array} \right) = 0 , } \end{array}
$$

where $p = ( x _ { c } , y _ { c } , z _ { c } , r ) ^ { T }$ . We get $3 m$ nonlinear equations in $2 m + 4$ unknowns. The first $2 m$ columns of the Jacobian can easily be brought into upper triangular form.

When the data cover only a small arc of the circle or a small patch of the sphere, the fitting problem can be il-conditioned. An important application involving this type of data is the fitting of a spherical lens. Likewise,the fiting of a sphere or an ellipsoid to near planar data is an ill-conditioned problem.For a more detailed description and tests of algorithms,see Gander, Golub,and Strebel [439,1994l. Algorithms for three-dimensional fitting of surfaces are treated by Sourlier [1013,1995]. Tests and comparisons of the software packages Funke and ODRPACK are given by Strebel, Sourlier, and Gander [1O45,1997].

# 8.3 - Nonnegativity Constrained Problems

# 8.3.1 - Gradient Projection Methods for NNLS

The active-set algorithms given in Section 3.5.2 for the NNLS (nonnegative least squares) problem

$$
\operatorname* { m i n } _ { { \boldsymbol x } \geq 0 } \| { \boldsymbol A } { \boldsymbol x } - { \boldsymbol b } \| _ { 2 }
$$

are competitive for problems of small to medium size.For applications where $A$ is large and/or sparse,other algorithms are to be preferred. For example,consider calculating the optimal amount of material to be removed in the polishing of large optics. Here the nonnegativity constraints come in because polishing can only delete material from the surface.A typical problem might have 8,0oO to 20,0oO rows and the same number of unknowns,with only a small percentage of the matrix elements being nonzero. In general, the problem is rank-deficient,and the nonnegativity constraints are active for a significant fraction of the elements of the solution vector. Applications in data mining and machine learning (where the given data, such as images and text,are required to be nonnegative) give rise to problems of even larger size.

In gradient projection methods for problem BLS (bound-constrained least squares), a step in the direction of the negative gradient is followed by projection onto the feasible set. For example,the projected Landweber method for an NNLS problem is

$$
x ^ { ( k + 1 ) } = \mathcal { P } ( x ^ { k } + \omega A ^ { T } ( b - A x ^ { ( k ) } ) ) , \quad 0 \leq \omega \leq 2 / \sigma _ { 1 } ( A ) ^ { 2 } ,
$$

where $\mathcal { P }$ is the projection onto the set $x \ge 0$ . These simple methods have the disadvantage of slow convergence, and $\sigma _ { 1 } ( A )$ may not be known.

For problem NNLS,an equivalent unconstrained problem can be obtained by introducing the parametrization $x _ { i } = e ^ { z _ { i } }$ ， $i = 1 , \ldots , n$ .In image restoration, this has a physical interpretation— see Hanke, Nagy,and Vogel [571,2ooo]. By the chain rule, the gradient $g$ of $\begin{array} { r } { \Phi ( x ) = \frac { \bar { 1 } } { 2 } \| A x - b \| _ { 2 } } \end{array}$ with respect to $z$ is

$$
X = \operatorname { d i a g } \left( \boldsymbol { x } \right) \geq 0 , \quad \boldsymbol { y } = \boldsymbol { A } ^ { T } ( \boldsymbol { A x } - \boldsymbol { b } ) \geq 0 , \quad g _ { z } = X \boldsymbol { y } .
$$

Setting $g _ { z } = 0$ , we recover the KKT first-order optimality conditions for NNLS.The correspond-ing modified residual norm steepest descent iterative method is

$$
\begin{array} { r } { x ^ { ( k + 1 ) } = x ^ { ( k ) } + \alpha _ { k } X _ { k } A ^ { T } ( b - A x ^ { ( k ) } ) , \quad X _ { k } = \mathrm { d i a g } ( x ^ { ( k ) } ) , } \end{array}
$$

where the step is in the direction of the negative gradient.This iteration can be interpreted as a nonlinearLandweber method in which $X _ { k }$ acts as a(variable) preconditioner. The step length $\alpha _ { k }$ in (8.3.2) is restricted to ensure nonnegativity of the $x ^ { ( k + 1 ) }$

In certain problems in astronomy and medical imaging,such as positron emission tomography (PET),data is subject to noise with a Poisson distribution. Statistical considerations justify computing a nonnegative minimizer of the maximum likelihood functional

$$
\Psi ( x ) = \sum _ { i = 1 } ^ { n } y _ { i } - \sum _ { i = 1 } ^ { n } b _ { i } \log y _ { i } , \qquad y \equiv A x ;
$$

see Kaufman [687,1993]. With the same parametrization $\scriptstyle x \ = \ e ^ { z }$ as above,the gradient of $\Phi$ with respect to $z$ is

$$
g _ { z } = X g _ { x } = X A ^ { T } Y ^ { - 1 } ( A x - b ) ,
$$

where $X = \arg \left( x \right)$ and $Y = \arg \left( y \right)$ . Assume now that $A$ is nonnegative and all column sums of $A$ are 1, i.e., $A ^ { T } e = e$ ，where $e = ( 1 , 1 , \ldots , 1 ) ^ { T }$ . This assumption can be interpreted as an energy conservation property of $A$ and can always be satisfied by an initial scaling of the columns. Then $X A ^ { T } Y ^ { - 1 } A x = X A ^ { T } e = x$ ,and the gradient becomes $g _ { z } = x - X A ^ { T } Y ^ { - 1 } b$ Setting the gradient equal to zero leads to the fixed-point iteration

$$
\begin{array} { r } { \boldsymbol { x } ^ { ( k + 1 ) } = \boldsymbol { X } _ { k } \boldsymbol { A } ^ { T } \boldsymbol { Y } _ { k } ^ { - 1 } \boldsymbol { b } , \quad \boldsymbol { X } _ { k } = \mathrm { d i a g } ( \boldsymbol { x } ^ { ( k ) } ) , \quad \boldsymbol { Y } _ { k } = \mathrm { d i a g } ( \boldsymbol { A } \boldsymbol { x } ^ { ( k ) } ) . } \end{array}
$$

This is the basis for the expectation maximization (EM) algorithm, which is popular in astronomy. Note that nonnegativity of the iterates in (8.3.4) is ensured if $b \geq 0$

The choice of starting point is important in iterative NNLS algorithms. Typical applications require the solution of an underdetermined linear system, which has no unique solution. Different initial points willconverge to different local optima. The EM algorithm is very sensitive to the initial guess and does not allow $x ^ { ( 0 ) } = 0$ .Dax [294,1991] shows that the use of Gauss-Seidel iterations to obtain a good initial point is likely to give large gains in efficiency.

Steepest descent methods for nonnegative least squares have only a linear rate of conver-gence,even when a line search is used. They tend to take very small steps whenever the level curves are elipsoidal. Kaufman [687,1993l considers acceleration schemes based on the conju-gate gradient (CG) method. In the inner iterations of CG, the scaling matrix $X$ is kept fixed. CG is restarted with a new scaling matrix $X _ { k }$ whenever a new constraint becomes active.Nagy and and Strakos [819,2ooo] consider a variant of this algorithm and show that it is more accurate and efficient than unconstrained Krylov subspace methods.

# 8.3.2 - Interior Methods for NNLS

The KKT first-order optimality conditions for problem NNLS can be writen as a system of nonlinear equations

$$
F _ { 1 } ( x , y ) = X y = 0 , \quad X = \mathrm { d i a g } ( x ) \geq 0 , \quad y = A ^ { T } ( A x - b ) \geq 0 .
$$

This is the basis of a primal-dual interior method. It uses the Newton directions for the nonlinear system

$$
F _ { 2 } ( x , y ) = \binom { X y } { A ^ { T } ( A x - b ) - y } = 0 ,
$$

where the iterands are not forced to satisfy the linear constraints $y = A ^ { T } ( A x - b )$ . A sequence of points $\{ x _ { k } > 0 \}$ is computed by

$$
( x _ { k + 1 } , y _ { k + 1 } ) = ( x _ { k } , y _ { k } ) + \theta _ { k } ( u _ { k } , v _ { k } ) ,
$$

where $\theta _ { k }$ is a positive step size, and $( u _ { k } , v _ { k } )$ satisfies the linear system

$$
\left( \begin{array} { c c } { Y _ { k } } & { X _ { k } } \\ { A ^ { T } A } & { - I } \end{array} \right) \left( \begin{array} { c } { u _ { k } } \\ { v _ { k } } \end{array} \right) = \left( \begin{array} { c } { - X _ { k } y _ { k } + \mu _ { k } e } \\ { A ^ { T } r _ { k } + y _ { k } } \end{array} \right) ,
$$

where $r _ { k } = b - A x _ { k } , X _ { k } = \operatorname { d i a g } \left( x _ { k } \right) , Y _ { k } = \operatorname { d i a g } \left( y _ { k } \right)$ ,and $\mu _ { k } \geq 0$ is a centralization parameter; see Lustig,Marsden,and Shanno [764,1991]. The step size $\theta _ { k }$ is chosen to satisfy

$$
\theta _ { k } \leq \left\{ \begin{array} { l l } { \theta _ { k } ^ { \operatorname* { m a x } } } & { \mathrm { i f } u _ { k } ^ { T } v _ { k } \leq 0 , } \\ { \operatorname* { m i n } ( \theta _ { k } ^ { \operatorname* { m a x } } , \hat { \theta } _ { k } ) } & { \mathrm { i f } u _ { k } ^ { T } v _ { k } > 0 , } \end{array} \right.
$$

$\theta _ { k } ^ { \mathrm { { m a x } } }$ is he largest value such hat $x _ { k + 1 } \geq 0 , y _ { k + 1 } \geq 0$

$$
\hat { \theta } _ { k } = ( x _ { k } ^ { T } y _ { k } - n \mu _ { k } ) / ( u _ { k } ^ { T } v _ { k } ) .
$$

Choosing $\theta _ { k }$ in this way can be shown to guarantee a monotonic decrease of $g ( x , y ) = x ^ { T } y$ in each iteration. Computational experience has shown that the condition $\theta _ { k } ^ { \mathrm { m a x } } < \hat { \theta } _ { k } / 2$ is usually satisfied,and in practice one takes $\theta _ { k } = 0 . 9 9 9 9 5 { \cdot } \theta _ { k } ^ { \mathrm { m a x } }$

From (8.3.6) it can be seen that $u _ { k }$ solves the least squares problem

$$
\operatorname* { m i n } _ { u _ { k } } \left\| \left( \begin{array} { c } { { A } } \\ { { ( X _ { k } Y _ { k } ) ^ { - 1 / 2 } } } \end{array} \right) u _ { k } - \left( \begin{array} { c } { { r _ { k } } } \\ { { ( X _ { k } Y _ { k } ) ^ { - 1 / 2 } \mu _ { k } e } } \end{array} \right) \right\| _ { 2 } .
$$

After $u _ { k }$ has been calculated, $v _ { k }$ is determined from the first block equation in (8.3.6):

$$
v _ { k } = - y _ { k } + X _ { k } ^ { - 1 } ( \mu _ { k } e - Y _ { k } u _ { k } ) .
$$

This approach can be improved by using a predictor-corrector scheme that determines a first direction $( u _ { k } , v _ { k } )$ by taking $\mu _ { k } = 0$ in (8.3.6). This direction is corrected by $( z _ { k } , w _ { k } ) =$ $( u _ { k } , v _ { k } ) + ( \bar { u } _ { k } , \bar { v } _ { k } )$ ,where $( \bar { u } _ { k } , \bar { v } _ { k } )$ satisfies

$$
\left( \begin{array} { c c } { Y _ { k } } & { X _ { k } } \\ { A ^ { T } A } & { - I } \end{array} \right) \left( \begin{array} { c } { \bar { u } _ { k } } \\ { \bar { v } _ { k } } \end{array} \right) = \left( \begin{array} { c } { - U _ { k } V _ { k } e + \mu _ { k } e } \\ { 0 } \end{array} \right) ,
$$

with $U _ { k } = \mathrm { d i a g } \left( u _ { k } \right)$ and $V _ { k } = \mathrm { d i a g } \left( v _ { k } \right)$ When $u _ { k }$ and $v _ { k }$ have been computed, $z _ { k }$ can be found as the solution of the least squares problem

$$
\operatorname* { m i n } _ { z _ { k } } \left\| \left( \begin{array} { c } { { A } } \\ { { ( X _ { k } Y _ { k } ) ^ { - 1 / 2 } } } \end{array} \right) u _ { k } - \left( \begin{array} { c } { { r _ { k } } } \\ { { ( X _ { k } Y _ { k } ) ^ { - 1 / 2 } ( \mu _ { k } - U _ { k } V _ { k } ) e } } \end{array} \right) \right\| _ { 2 } .
$$

Finally, $w _ { k }$ is found from

$$
w _ { k } = - y _ { k } + X _ { k } ^ { - 1 } \big ( \mu _ { k } e - Y _ { k } z _ { k } - U _ { k } v _ { k } \big ) .
$$

Following [764,1991], the parameter $\mu _ { k }$ is taken as

$$
\mu _ { k } = ( x _ { k } + \theta _ { k } u _ { k } ) ^ { T } ( y _ { k } + \theta _ { k } v _ { k } ) / n ^ { 2 }
$$

with $\theta _ { k }$ as above. This choice does not guarantee a decrease in $g ( x , y )$ but seems to work well in practice. Subproblems (8.3.7) and (8.3.8) must be solved from scratch at each iteration because no reliable updating methods are available.

Portugal, Judice,and Vicente [900,1994] discuss implementation issues and present computational experience with a predictor-corrector algorithm for problem NNLS. They find this method gives high accuracy even when the subproblems are solved by forming the normal equation.

An interior method for large-scale nonnegative regularization is given by Rojas and Steihaug [933, 20o2]. Surveys of interior methods are given by Wright [1133,1997] and Forsgren, Gill,and Wright [421, 2oo2]. The theory of interior methods for convex optimization is developed in the monumental work by Nesterov and Nemirovski [828,1994]. The state of the art of interior methods for optimization is surveyed by Nemirovski and Todd [825,2008].

# 8.3.3 - Nonnegative Matrix Factorization

An important application of NNLS occurs in nonnegative matrix factorization (NNMF). Given a nonnegative matrix $A \in \mathbb { R } ^ { m \times n }$ , we want to find nonnegative factors $W \in \mathbb { R } ^ { m \times k }$ and $H \in$ $\mathbb { R } ^ { n \times k }$ that solve

$$
\operatorname* { m i n } _ { W , H } \lVert A - W H ^ { T } \rVert _ { F } ^ { 2 } \mathrm { ~ s u b j e c t ~ t o ~ } W \geq 0 , \quad H \geq 0 .
$$

The NNMF problem has received much attention; see Kim and Park [697,2oo8]. Applications include analysis of image databases,data mining, machine learning,and other retrieval and clustering operations. Vavasis [1092, 2oo9] shows that the NNMF problem is equivalent to a problem in polyhedral combinatorics and is NP-hard.

If either of factors $H$ or $W$ is kept fixed, then computing the other factor in problem NNMF is a standard NNLS problem with multiple right-hand sides. It can be solved independently by an NNLS algorithm. For example, if $H$ is fixed, then

$$
\operatorname* { m i n } _ { W \geq 0 } \| \boldsymbol { H } \boldsymbol { W } ^ { T } - \boldsymbol { A } ^ { T } \| _ { F } ^ { 2 } = \sum _ { i = 1 } ^ { m } \operatorname* { m i n } _ { w _ { i } \geq 0 } \| \boldsymbol { H } \boldsymbol { w } _ { i } ^ { T } - \boldsymbol { a } _ { i } ^ { T } \| _ { 2 } ^ { 2 } ,
$$

where $w _ { i }$ and $a _ { i }$ are the $i$ th rows of $W$ and $A$ ，respectively. Given an initial guess $H ^ { ( 1 ) }$ ,the alternating NNLS method (ANLS) is

$$
\begin{array} { r l } & { \mathrm { f o r } \ k = 1 , 2 , \ldots , } \\ & { \qquad \underset { W \geq 0 } { \operatorname* { m i n } } \ \lVert H ^ { ( k ) } W ^ { T } - A ^ { T } \rVert _ { F } ^ { 2 } , \mathrm { g i v i n g } W ^ { ( k ) } , } \\ & { \qquad \underset { H \geq 0 } { \operatorname* { m i n } } \lVert W ^ { ( k ) } H ^ { T } - A \rVert _ { F } ^ { 2 } , \mathrm { g i v i n g } H ^ { ( k + 1 ) } . } \end{array}
$$

The two NNLS subproblems are solved alternately until a convergence criterion is satisfied. It can be shown that every limit point attained by ANLS is a stationary point of (8.3.9). If $A$ is rank-deficient, a unique least-norm solution is computed in a second stage.

A problem with the ANLS method is that convergence is often slow,and the solution reached is not guaranteed to be a global optimum. Finding a good initial approximation is important. We know that the best rank- $k$ approximation of $A$ can be found from the frst $k$ singular triplets $\sigma _ { i } u _ { i } v _ { i } ^ { T }$ of $A$ .How to obtain these triplets is discussed in Section 7.3.3. Boutsides and Gallopoulus [172, 2oo8] show that good initial values for ANLS can be obtained by replacing all negative elements in the product $u _ { i } v _ { i } ^ { T }$ by zeros.

Surveys of algorithms for nonnegative matrix factorizations are given by Berry et al. [116, 2007] and Kim, He,and Park [699,2o14]. Nonnegative tensor factorizations are studied by $\mathrm { K i m }$ ， Park,and Eldén [698,2007].

# Notes and references

For large-scale NNLS problems, modern optimization algorithms for minimizing a general ob-jective function $f ( x )$ subject to bound-constraints often outperform older specialized algorithms. In the gradient projection algorithm L-BFGS-B by Byrd et al.[197,1995l, a limited-memory BFGS approximation to the Hessian of $f$ is updated at each iteration and used to define a quadratic model of $f$ . A search direction is then computed by the gradient projection method with a line search. For an open source Fortran implementation,see Zhu et al.[1150,1997]. Some improvements are given by Morales and Nocedal [805,2o11]. Algorithms that combine the standard active-set strategy with the gradient projection method are given by Bierlaire, Toint, and Tuytens [119,1991] and Moré and Toraldo [809,198g]. In these,the number of active constraints can change significantly at each iteration.

# 8.4 - Robust Regression and Related Topics

There are several alternative statistical models to least squares fitting such as maximum likelihood methods and other Bayesian models. These often lead to nonlinear least squares problems but lie outside the main scope of this book. A good overview of these and other alternative models for learning from data is given in the book by Hastie,Tibshirani,and Friedman [595, 2009]. In this section we discuss a selection of interesting recent developments.

# 8.4.1 - Minimizing the $\ell _ { 1 }$ and $\ell _ { \infty }$ Residual Norm

In some applications it might be appropriate to minimize the $\ell _ { p }$ -norm $\| r \| _ { p }$ of the residual vector $r = b - A x$ ， $A \in \mathbb { R } ^ { m \times n }$ for some $p \neq 2$ . This problem has the same solution as

$$
\operatorname* { m i n } _ { x } \psi _ { p } ( x ) , \quad \psi _ { p } ( x ) = \| r ( x ) \| _ { p } ^ { p } ,
$$

and the latter expression is easier to use. For $1 \leq p < \infty$ ,problem (8.4.1) is strictly convex if $\operatorname { r a n k } ( A ) = n$ and therefore has a unique solution. For $0 < p < 1$ ， $\psi _ { p } ( x )$ is not convex, and $\| \cdot \| _ { p }$ is not actually a norm, though $d ( x , y ) = \| x - y \| _ { p }$ is a metric. For $p = 1$ and $p  \infty$ ,where

$$
\| r \| _ { 1 } = \sum _ { i = 1 } ^ { m } | r _ { i } | , \qquad \| r \| _ { \infty } = \operatorname* { m a x } _ { 1 \leq i \leq m } | r _ { i } | ,
$$

the minimization is complicated by the fact that these norms are only piecewise differentiable. Already in 1799,Laplace was using the principle of minimizing the sum of the absolute errors with the added condition that the sum of the errors be zero.He showed that this implies that the solution $x$ must satisfy exactly $n$ out of the $m$ equations.The effect on errors of using different $\ell _ { p }$ -norms is visualized in Figure 8.4.1.

![](../chunks/Numerical Methods for Least Squares Problems (Åke Björck) (z-library.sk, 1lib.sk, z-lib.sk_part_0007_pages_0421-0490/auto/images/d6487cb1dfe36b18e0719a6f9585925484cf07877ff2f07d4ab606376a561f2f.jpg)  
Figure 8.4.1. The penalizing effect using the $\ell _ { p }$ -norm for $p = 0 . 1 , 1 , 2 , 1 0$

Example 8.4.1. Consider the problem of estimating the scalar $\gamma$ from $m$ observations $y \in \mathbb { R } ^ { m }$ This is equivalent to

$$
\operatorname* { m i n } _ { \gamma _ { p } } \| e ^ { T } \gamma _ { p } - y \| _ { p } ^ { p } , \quad e = ( 1 , 1 , \ldots , 1 ) ^ { T } .
$$

If $y _ { 1 } \geq y _ { 2 } \geq \cdot \cdot \cdot \geq y _ { m }$ , the solutions for some different values $p$ are

$$
\begin{array} { c } { { \gamma _ { 1 } = y _ { ( m + 1 ) / 2 } , \quad ( m \mathrm { o d d } ) , } } \\ { { \gamma _ { 2 } = ( y _ { 1 } + y _ { 2 } + \cdot \cdot \cdot + y _ { m } ) / m , } } \\ { { \gamma _ { \infty } = ( y _ { 1 } + y _ { m } ) / 2 . } } \end{array}
$$

These estimates correspond to the median, mean,and midrange,respectively. Note that the estimate $\gamma _ { 1 }$ is insensitive to extreme values of $y _ { i }$ . A small number of isolated large errors usually will not change the $\ell _ { 1 }$ solution. This property carries over to general $\ell _ { 1 }$ problems.On the other hand, the estimate $\gamma _ { \infty }$ only depends on the two extreme observations.

Minimization in the $\ell _ { 1 }$ and $\ell _ { \infty }$ norms can be posed as linear programs. For the $\ell _ { 1 }$ -norm, define nonnegative variables $r ^ { + }$ ， $r ^ { - } \in \mathbb { R } ^ { m }$ such that $r = r ^ { + } - r ^ { - }$ .Let $e ^ { T } = ( 1 , 1 , \dots , 1 )$ be a row vector of all ones. Then (8.4.1) is equivalent to

$$
\operatorname* { m i n } { \big ( } e ^ { T } r ^ { + } + e ^ { T } r ^ { - } { \big ) } \ \mathrm { s u b j e c t } \ \mathrm { t o } \ A x + r ^ { + } - r ^ { - } = b , \quad r ^ { + } , r ^ { - } \geq 0 .
$$

The matrix $\left( \begin{array} { l l l } { A } & { I } & { - I } \end{array} \right)$ has rank $m$ and column dimension $n + 2 m$ . From standard results in linear programming theory it follows that there exists an optimal $\ell _ { 1 }$ solution such that at least $m$ $r _ { i } ^ { + }$ or $\boldsymbol { r } _ { i } ^ { - }$ are zero and at least $n - \operatorname { r a n k } ( A ) \ x _ { : }$ are zero; see Barrodale and Roberts [86,1970]. An initial feasible basic solution is available immediately by setting $x = 0$ and $r _ { i } ^ { + } = b _ { i }$ or $r _ { i } ^ { - } = - b _ { i }$

Barrodale and Roberts [87,1973l use a modified simplex method to solve linear program (8.4.4). It takes advantage of the fact that the variables $r _ { i } ^ { + }$ and $r _ { i } ^ { - }$ cannot simultaneously be in the basis. The simplex iterations can be performed within a condensed simplex array of dimensions $( m + 2 ) \times ( n + 2 )$ . Implementions of this algorithm are given in Barrodale and Roberts [88,1974] and Bartels and Conn [89,1g8o]. The latter can handle additional linear equality and inequality constraints.An alternative algorithm by Abdelmalek [5,198o],[6,1g8o] is based on the dual of linear program (8.4.4).

The $\ell _ { \infty }$ problem，also called Chebyshev or minimax approximation, is to minimize $\operatorname* { m a x } _ { i = 1 } ^ { m } | r _ { i } |$ or, equivalently,

$$
\operatorname* { m i n } \zeta \quad { \mathrm { s u b j e c t } } \operatorname { t o } \quad - \zeta e \leq A x - b \leq \zeta e , \quad \zeta \geq 0 .
$$

Stiefel [1036,1959] gave a so-called exchange algorithm for Chebyshev approximation. This is based on the following property of the optimal solution: the maximum error is attained at $n + 1$ points if $\operatorname { r a n k } ( A ) = n$ . In a later paper he showed his algorithm to be equivalent to the simplex method applied to a suitable linear program.Problem (8.4.5) can be formulated as

$$
\operatorname* { m i n } \zeta { \mathrm { ~ } } { \mathrm { s u b j e c t ~ t o ~ } } \left( { \begin{array} { l l } { A } & { e } \\ { - A } & { e } \end{array} } \right) \left( { \begin{array} { l } { x } \\ { \zeta } \end{array} } \right) \geq \left( { \begin{array} { l } { b } \\ { - b } \end{array} } \right) , \quad \zeta \geq 0 .
$$

This linear program has $2 m$ linear constraints in $n + 1$ variables,and only $\zeta$ has a finite simple bound. Osborne and Watson [850,1967] recommended the dual program of (8.4.6),

$$
\operatorname* { m a x } \left( { b } ^ { T } - { b } ^ { T } \right) w \mathrm { ~ s u b j e c t ~ t o ~ } \left( \begin{array} { l l } { A ^ { T } - A ^ { T } } \\ { e ^ { T } } & { e ^ { T } } \end{array} \right) w = \binom { 0 } { 1 } , \quad w \geq 0 ,
$$

which has only $n { \mathrel { + { 1 } } }$ rows. To use a modern mathematical programming system, such as CPLEX or Gurobi (especially when $A$ is sparse), problem (8.4.6) can be rewritten as

$$
\operatorname* { m i n } \zeta { \mathrm { ~ s u b j e c t ~ t o ~ } } \left( { \begin{array} { l } { b } \\ { 0 } \\ { - \infty } \end{array} } \right) \leq \left( { \begin{array} { l l l } { A } & { I } & \\ & { I } & { e } \\ & { I } & { - e } \end{array} } \right) \left( { \begin{array} { l } { x } \\ { r } \\ { \zeta } \end{array} } \right) \leq \left( { \begin{array} { l } { b } \\ { \infty } \\ { 0 } \end{array} } \right) , \quad \zeta \geq 0 ,
$$

which is larger but has only one $A$ and is very sparse.

If the assumptions in a regression model are violated and data are contaminated with outliers, these can have a large efect on the solution. In robust regression, possble outliers among the data points are identified and given less weight. Huber's M-estimator (Huber [648,1981]) is a compromise between $\ell _ { 2 }$ and $\ell _ { 1 }$ estimations.It uses the least squares estimator for“normal" data but the $\ell _ { 1 }$ -norm estimator for data points that disagree more with the normal picture. More precisely, Huber's M-estimate minimizes the objective function

$$
\psi _ { H } ( x ) = \sum _ { i = 1 } ^ { m } \rho ( r _ { j } ( x ) / \sigma ) ,
$$

where $\sigma$ is a scaling factor that depends on the data,and

$$
\rho ( t ) = { \left\{ \begin{array} { l l } { { \frac { 1 } { 2 } } t ^ { 2 } } & { { \mathrm { i f ~ } } | t | \leq \gamma , } \\ { \gamma | t | - { \frac { 1 } { 2 } } \gamma ^ { 2 } } & { { \mathrm { i f ~ } } | t | > \gamma } \end{array} \right. }
$$

for some threshold parameter $\gamma > 0$ . In the following we assume $\sigma = 1$ in (8.4.9). For large values of $\gamma$ ,Huber's M-estimator will be close to the least squares estimator,and for small values of $\gamma$ it is close to the $\ell _ { 1 }$ estimator. The statistical model behind this estimate is that the errors come from a distribution of the form $( 1 - \epsilon ) N + \epsilon P$ ，where $N$ denotes the standard normal distribution, and $P$ is an unknown symmetric perturbing distribution with the same center as $N$ For a general treatment of robust statistical procedures, see Huber $[ 6 4 8 , 1 9 8 1 ]$

The Newton step $s$ for minimizing the $\psi _ { H }$ -norm (8.4.9) satisfies $A ^ { T } D A s = A ^ { T } y .$ ，where

$$
y _ { i } = \rho ^ { \prime } ( r _ { i } ) , \qquad D = \mathrm { d i a g } ( \rho ^ { \prime \prime } ( r _ { i } ) ) , \quad i = 1 , \ldots , m .
$$

This is similar to (8.4.15) for $\ell _ { p }$ approximation. It is advantageous to start the iterations with a large value of the threshold parameter $\gamma$ and then decrease it to the desired value. This helps prevent the occurrence of rank-deficient Hessians $H$

A finite algorithm for $\ell _ { 1 }$ estimation is given by Madsen and Nielsen [767,1993l. At each iteration the nondifferentiable function $\| r \| _ { 1 }$ is replaced by the Huber function (8.4.9) for some parameter $\gamma$ . The parameter is successively reduced until it is small enough for the $\ell _ { 1 }$ solution to be detected. The method is significantly faster than the simplex-type method of Barrodale and Roberts [88,1974].

# Notes and references

Späth [1014,1992l gives Fortran programs implementing several of the early algorithms cited above for computing $\ell _ { 1 }$ and $\ell _ { \infty }$ estimators. For $\ell _ { 1 }$ approximation the Barrodale-Roberts algorithm uses the least storage and is among the fastest. For $\ell _ { \infty }$ approximation the Barrodale-Philips algorithm is the fastest and has the best reliability.Bartels and Golub [91,1968],[92, 1968] give a more stable implementation of Stiefel's exchange algorithm for $\ell _ { \infty }$ minimization. The algorithm of Barrodale and Philips [85,1975l is based on the dual linear program (8.4.7). Bartels, Conn,and Sinclair [90,1978] give algorithms based on projected gradient techniques. They use a descent method to explicitly find the correct subset of zero residuals when $p = 1$ and maximum residuals when $p = \infty$ .Coleman and Li [260,1992], [261,1992] propose a globally convergent Newton algorithm for the $\ell _ { 1 }$ and the $\ell _ { \infty }$ problems.

# 8.4.2 - Iteratively Reweighted Least Squares

The method of Iteratively Reweighted Least Squares (IRLS) is based on the observation that the minimization problem minx $\| r ( x ) \| _ { p } ^ { p }$ ， $r ( x ) = b - A x$ ,can be rewritten as

$$
\| r ( x ) \| _ { p } ^ { p } = \sum _ { i = 1 } ^ { m } | r _ { i } ( x ) | ^ { p } = \sum _ { i = 1 } ^ { m } | r _ { i } ( x ) | ^ { p - 2 } r _ { i } ( x ) ^ { 2 } .
$$

This is a weighted linear least squares problem

$$
\operatorname* { m i n } _ { x } \| W ( | r | ) r \| _ { 2 } ^ { 2 } , \quad W ( | r | ) = \mathrm { d i a g } \left( | r | \right) ^ { ( p - 2 ) / 2 } ,
$$

where $\mathrm { d i a g } \left( \left| \boldsymbol { r } \right| \right)$ denotes the diagonal matrix with ith component $| r _ { i } |$ . Here the diagonal weight matrix $W$ depends on $r$ and hence on the unknown $x$

In IRLS a sequence of weighted least squares problems is solved, where the weights for the next iteration are obtained from the current solution. The iterations are initialized by computing the unweighted least squares solution $x ^ { ( 1 ) }$ and setting $W _ { 1 } = W _ { 1 } ( | r ^ { ( 1 ) } | )$ ,where $r ^ { ( 1 ) } \stackrel { \textstyle ^ { . } } { = } b - \stackrel { \textstyle ^ { . } } { A } x ^ { ( 1 ) }$ In step $k$ ,one solves

$$
\operatorname* { m i n } _ { \delta x } \| W _ { k } ( r ^ { ( k ) } - A \delta x ) \| _ { 2 } , \quad W _ { k } = \mathrm { d i a g } ( ( | r _ { i } ^ { ( k ) } | ) ^ { ( p - 2 ) / 2 } ) ,
$$

and sets $x ^ { ( k + 1 ) } = x ^ { ( k ) } + \delta x ^ { ( k ) }$ . It can be shown that any fixed point of the IRLS iteration satisfies the necessary conditions for a minimum of $\psi ( x ) = \| r ( x ) \| _ { p } ^ { p }$

The first study of IRLS appeared in Lawson [725,1g6i], where it was applied with $p = 1$ for $\ell _ { 1 }$ minimization. It was extended to $1 \leq p \leq \infty$ by Rice and Usow [927,1968]. Cline [252,1972] proved that the local rate of convergence of IRLS is linear. Osborne [848, $\mathrm { 1 9 8 5 } ]$ gives a comprehensive analysis of IRLS and proves convergence of the basic IRLS method for $1 < p < 3$ .For $p = 1$ ,his main conclusion is that IRLS converges with linear rate provided the $\ell _ { 1 }$ approximation problem has a unique nondegenerate solution. More recently, IRLS has been used with $p < 1$ for computing sparse solutions.

The IRLS method is attractive because methods for solving weighted least squares are generally available. In the simplest implementations the Cholesky factorization of $A ^ { T } W ^ { 2 } A$ or the QR factorization of $W A$ is recomputed in each step. IRLS is closely related to Newton's method for minimizing the nonlinear function $\psi ( x ) = \| b - A x \| _ { p } ^ { p }$ . The first and second derivatives of $\psi ( x )$ are

$$
\frac { \partial \psi ( x ) } { \partial x _ { j } } = - p \sum _ { i = 1 } ^ { m } a _ { i j } | r _ { i } | ^ { p - 2 } r _ { i } , \qquad \frac { \partial ^ { 2 } \psi ( x ) } { \partial x _ { j } \partial x _ { k } } = p ( p - 1 ) \sum _ { i = 1 } ^ { m } a _ { i j } | r _ { i } | ^ { p - 2 } a _ { i k } .
$$

Hence the gradient and Hessian of $\psi ( x )$ can be written

$$
\nabla \psi = g ( x ) = - p A ^ { T } W ^ { 2 } r , \qquad \nabla ^ { 2 } \psi = H ( x ) = p ( p - 1 ) A ^ { T } W ^ { 2 } A ,
$$

where $W = W ( | \boldsymbol { r } | )$ is given as in (8.4.12). Newton's method for solving the nonlinear equation $g ( x ) = 0$ becomes

$$
x ^ { ( k + 1 ) } = x ^ { ( k ) } + \delta x ^ { ( k ) } , \quad A ^ { T } W ^ { 2 } A \delta x = q A ^ { T } W ^ { 2 } r , \quad q = 1 / ( p - 1 ) .
$$

These equations are the normal equations for the weighted linear least squares problem

$$
\operatorname* { m i n } _ { \delta x } \| W A \delta x - q W r \| _ { 2 } .
$$

It follows that the Newton step $s$ for minimizing $\psi _ { p } ( x )$ differs from the IRLS step only by the factor $q = 1 / ( p - 1 )$ . It follows that the IRLS step is a descent direction provided the Hessian is positive definite.

Since IRLS does not take a full Newton step, it is at best only linearly convergent. Taking the full Newton step gives asymptotic quadratic convergence but makes the initial convergence less robust when $p < 2$ . In the implementation below, the full Newton step is taken only when $p > 2$ For $p < 2$ ， $( p - 2 ) / 2 < 0$ and a zero residual $| r _ { i } ^ { ( k ) } | = 0$ will give an ifinite weight $w _ { i }$ Then $r _ { i } = 0$ also in the next step,and the zero residual will persist in all subsequent steps. Therefore, when $p < 2$ it is customary to modify the weights by adding a small number:

$$
w _ { i } = | r _ { i } | ^ { ( p - 2 ) / 2 } + \epsilon , \quad i = 1 , \ldots , m ;
$$

see Merle and Späth [790, 1974]. Below, we take $\epsilon = 1 0 ^ { - 6 }$ initially and halve its value at each iteration.We remark that $x$ can be eliminated from the loop by using $r = ( I - P _ { A } ) b$ ,where $P _ { A }$ is the orthogonal projector onto the column space of $A$

# Algorithm 8.4.1 (IRLS for Overdetermined Systems).

function $[ \mathrm { x } , \mathrm { r } , \mathrm { N r m } ] = \mathrm { i } \mathrm { r } 1 \mathrm { s } \left( \mathrm { A } , \mathrm { b } , \mathrm { p } , \mathrm { k m a x } \right)$ $\%$ IRLS for minimizing $| \mathbf { \nabla } | \ A \mathbf { x } \ \texttt { - } \texttt { b } | \ | \mathbf { \Pi } _ { - } \texttt { p }$ ，where $\% 0 < \texttt { p } < \mathtt { i n f t y }$ ，and A is m by n, $\texttt { m } > \texttt { n }$ · %--- $[ { \mathfrak { m } } , { \mathfrak { n } } ] \ =$ size(A); $\texttt { x } = \texttt { A } \backslash \mathtt { b }$ ； $\mathrm { ~ \bf ~ r ~ } = \mathrm { ~ \bf ~ b ~ } - \mathrm { ~ \bf ~ A * x ~ }$ $\begin{array} { l } { \mathsf { w e p s } = 1 . 0 { \mathsf { e } } - 6 * \mathsf { o n e s } \left( \mathsf { s i z e } \left( { \mathbf { x } } \right) \right) ; } \end{array}$ $\mathtt { N r m } \ = \ \mathtt { n o r m } ( \mathtt { r } , \mathtt { p } )$ ； for $\texttt { k } = \texttt { 1 }$ : kmax ${ \mathfrak { w } } = { \mathfrak { a } } \mathbf { b } \mathbf { s } \left( \mathbf { r } \right) . { \widehat { \mathbf { \xi } } } ( \left( \mathbf { p } \mathbf { - } 2 \right) / 2 ) ;$ $\begin{array} { r } { \mathsf { w e p s } = \mathsf { w e p s } / 2 ; } \end{array}$ if $\tt { p } < 2$ ， $\begin{array} { r } { \texttt { w } = \texttt { w } + \texttt { w e p s } ; } \end{array}$ % Sort weights and reorder rows ${ \begin{array} { l } { [ { \mathrm { w } } , \mathrm { p e r m } ] \ = \ \mathbf { s o r t } ( { \mathrm { w } } ) ; } \\ { { \mathrm { A } } \ = \ { \mathrm { A } } ( \mathrm { p e r m } , : ) ; \ { \mathrm { ~ b ~ } } = \ { \mathrm { b } } ( \mathrm { p e r m } , : ) ; } \\ { [ { \mathrm { w } } \ = \ { \mathrm { d i a g } } ( { \mathrm { w } } ) ; \ \qquad } \\ { { \mathrm { d } } \mathbf { x } \ = \ ( { \mathrm { W } } * { \mathrm { A } } ) \setminus ( { \mathrm { W } } * \mathbf { r } ) ; } \end{array} }$ i ${ \texttt { f p } } < { \texttt { 2 } } , { \texttt { x } } = { \texttt { x } } + { \texttt { d x } } ;$ else $\textbf { x } = \textbf { x } + \mathbf { \beta } \mathrm { d } { \bf x } / \left( \mathtt { p } - 1 \right)$ ;end end $\begin{array} { r c l } { \displaystyle \mathtt { r } ~ = ~ \mathtt { b } ~ - ~ \mathtt { A } \ast \mathtt { x } \mathrm { ; } } \\ { \displaystyle \mathtt { N r m } ~ = ~ } & { \displaystyle [ \mathtt { N r m } , \mathtt { n o r m } ( \mathtt { r } , \mathtt { p } ) ] \mathrm { ; } } \end{array}$ end

The global convergence of IRLS can be improved by using a line search. O'Leary [838, 1990] compares several strategies for implementing an efficient and reliable line search.

A useful modification of IRLS is to apply continuation. Starting with $p = 2$ ， $p$ is successively increased or decreased for a number of iterations until the desired value is reached.This improves the range of values of $p$ that give convergence and also significantly improves the rate of conver-gence.A similar idea is to use a large initial value of $\epsilon$ in (8.4.16) and reduce it successively in later iterations.

When $p$ is close to unity, the convergence of the IRLS method can be extremely slow. This is related to the fact that for $p = 1$ the solution has zero residuals.Li [744,745,1993] develops a globalized Newton algorithm using the complementary slackness condition for the $\ell _ { 1 }$ problem. Far from the solution it behaves like IRLS with line search,but close to the solution it is similar to Newton's method for an extended nonlinear system of equations.The problem of unbounded second derivatives is handled by a simple technique connected to the line search.

# Notes and references

Ekblom [363,1973] uses IRLS with a damped least squares method for $\ell _ { p }$ minimization. IRLS has been used extensively in signal processing for filter design; see Burrus,Barreto,and Selesnick [191,1994]. Newton-like methods for computing Huber's M-estimator are given by Clark and Osborne [251,1986], Ekblom [364,1988], Ekblom and Madsen [365,1989],and Madsen and Nielsen [766,199o]. A comparison of some of these implementations is given by O'Leary [838,199o]. Daubechies et al. [286, 201o] outline a reweighting scheme for IRLS $\ell _ { 1 }$ approximation that avoids infinite weights. The rate of convergence of their algorithm is similar to that for interior-point algorithms for direct $\ell _ { 1 }$ minimization.

# 8.4.3 - LASSO and Least-Angle Regression

The minimization problem

$$
\operatorname* { m i n } _ { x } \left\{ \| A x - b \| _ { 2 } ^ { 2 } + \mu \| x \| _ { 1 } \right\} ,
$$

where $\mu > 0$ is a regularization parameter,is similar to Tikhonov regularization,except for using the $\ell _ { 1 }$ -norm instead of the $\ell _ { 2 }$ -norm. The objective function in (8.4.17) is convex but not differentiable. Hence this problem always has a solution,although it need not be unique. The use of the $\ell _ { 1 }$ -norm in the regularization term has a big influence on the character of the solution. In contrast to standard Tikhonov regularization, the solution is not a linear function of $b$ ,and there is no analytic formula for the solution.In the limit when $\mu \to 0$ ,it is the least squares solution of the minimum $\ell _ { 1 }$ -norm. The related $\ell _ { 1 }$ trust-region problem,

$$
\operatorname* { m i n } _ { x } \| A x - b \| _ { 2 } \quad { \mathrm { s u b j e c t ~ t o } } \quad \| x \| _ { 1 } \leq \mu ,
$$

was proposed for variable selection in least squares problems by Tibshirani [1O61,1996]. He gave it the colorful name LASSO,which stands for“Least Absolute Shrinkage and Selection Operator.”For a fixed value of the regularization parameter $\mu > 0$ ，the objective function in LASSO is strictly convex over a convex feasible region. Therefore problem (8.4.18) has a unique minimizer. Let $\mu _ { \mathrm { L S } } = \Vert x _ { \mathrm { L S } } \Vert _ { 1 }$ , where $x _ { \mathrm { L S } }$ is the unconstrained least squares solution. The trajectory of the LASSO solution for $\mu \in [ 0 , \mu _ { \mathrm { L S } } ]$ is a piecewise linear function of $\mu$ An algorithm for computing the LASSO trajectory based on standard methods for convex programming is given by Osborne,Presnell,and Turlach [849, 2000].

Efron et al. [359, 2Oo4l gave a more intuitive algorithm called Least-Angle Regression (LARS). By construction, the trajectory of the solution in LARS is piecewise linear with $n$ break points. In many cases,this trajectory coincides with that of the $\ell _ { 1 }$ constrained least squares problem. Indeed, with the following small modification the LARS algorithm can be used for solving the LASSO problem: When a nonzero variable becomes zero and is about to change sign, the variable is removed from the active set,and the least squares direction of change is recomputed.

Theorem 8.4.2. Let $x ( \mu )$ be the solution of the $\ell _ { 1 }$ constrained least squares problem (8.4.18). Then there exists a finite set of break points $0 = \mu _ { 0 } \leq \mu _ { 1 } \leq \cdot \cdot \cdot \leq \mu _ { p } = \mu _ { \mathrm { L S } }$ such that $x ( \mu )$ is $a$ piecewise linear function

$$
x ( \mu ) = x ( \mu _ { k } ) + ( \mu - \mu _ { k } ) ( x ( \mu _ { k + 1 } ) - x ( \mu _ { k } ) ) , \quad \mu _ { k } \leq \mu \leq \mu _ { k + 1 } .
$$

The $\ell _ { 1 }$ -constrained least squares solution can be computed with about the same arithmetic cost as a single least squares problem. As in stepwise regression, the QR factorization of the columns in the active set is modified in each step.When a new variable is added,the factorization is updated by adding the new column. In the case when a variable becomes zero,the factorization is downdated by deleting a column. Although unlikely,the possibility of a multiple change in the active set cannot be excluded.A crude method for coping with this is to make a small random change in the right-hand side.It follows from continuity that no index set $\sigma$ can be repeated in the algorithm. There are only a finite number of steps in the algorithm,usually not much more than $\operatorname* { m i n } \{ m , n \}$

Statistical aspects of variable selection in least squares problems using LASSO and related techniques are discussed by Hastie, Tibshirani, and Friedman [595, 2oo9]. In image processing a related technique has been used,where the $\ell _ { 1 }$ -norm inLASSO is replaced by the Total-Variation (TV) norm, giving in one dimension the related problem

$$
\operatorname* { m i n } _ { x } \| A x - b \| _ { 2 } ^ { 2 } + \mu \| L x \| _ { 1 }
$$

where $( L x ) _ { i } = | x _ { i + 1 } - x _ { i } |$ . For a two-dimensional $N \times N$ array $x _ { i , j }$ ， $1 \leq i , j \leq n$ , the TV norm is defined as

$$
\| x \| _ { T V } = \sum _ { i = 1 } ^ { N - 1 } \sum _ { j = 1 } ^ { N } \bigl | x _ { i + 1 , j } - x _ { i , j } \bigr | + \sum _ { i = 1 } ^ { N } \sum _ { j = 1 } ^ { N - 1 } \big | x _ { j + 1 , j } - x _ { i , j } \big | .
$$

# 8.4.4 - Basis Pursuit and Compressed Sensing

Let $A x \ = \ b$ $A \in \mathbb { R } ^ { m \times n }$ ， $m \ll n$ ,be a consistent underdetermined linear system. Such a system does not allow the determination of $x$ unless some additional information on $x$ is utilized. In many applications,such as medical image reconstruction,machine learning,and artificial intellgence,the desired solution is known to be sparse,i.e., $x$ has at most $s \ll n$ nonzero components. For example, in a biology experiment, one may measure changes of expressions in 30,00O genes and expect at most a few hundred genes with a different expression level. Note that, after a transformation of variables,this includes cases where the solution can be expressed by a few Fourier components or a few wavelets. For such problems,we would like to minimize the number of nonzero elements in $x$ ,which is formally equivalent to minimizing the $\ell _ { 0 }$ "norm”

$$
\| x \| _ { 0 } = \dim \{ i \mid x _ { i } \neq 0 \} .
$$

This is a nonconvex optimization problem that is known to be computationally intractable, because it usually requires a combinatorial search. In the Basis Pursuit (BP) problem,sparse solutions are constructed by solving the $\ell _ { 1 }$ minimization problem

$$
\operatorname* { m i n } _ { x } \| x \| _ { 1 } \quad { \mathrm { s u b j e c t ~ t o } } \quad A x = b ,
$$

The BP objective can be interpreted as the closest convex approximation to (8.4.22). The region $\| x \| _ { 1 } \leq \mu$ is a diamond-shaped polyhedron with many sharp corners, edges,and faces at which one or several parameters are zero.This structure favors solutions with few nonzero coeficients. Chen,Donoho,and Saunders [241, 2oo1] use BP to decompose a signal into a sparse combination of elements of a highly overcomplete dictionary, e.g. consisting of wavelets. To allow for noise in the signal $b$ , they also propose the BP Denoising (BPDN) problem

$$
\operatorname* { m i n } _ { x } \lambda \| x \| _ { 1 } + \frac { 1 } { 2 } r ^ { T } r \quad \mathrm { s u b j e c t ~ t o } \quad A x + r = b ,
$$

where $\lambda > 0$ again encourages sparsity in $x$ .BPDN is solved by the primal-dual interior method PDCO [887,2o18] using LSMR to compute search directions (because $A$ is a fast linear operator rather than an explicit matrix).

Compressed sensing is a term coined by Donoho [329,2oo6] for the problem of recovering a signal from a small number of compressive measurements. Candes, Romberg,and Tao [206, 2006] prove that sparse solutions can with high probability be reconstructed exactly from remarkably few measurements by compressed sensing, provided these satisfy a certain coherence property. It has been established that compressed sensing is robust in the sense that it can deal with measurements noise and cases where the signal is only approximately sparse. One of several important applications is Magnetic Resonance Imaging (MRI),for which the use of compressed sensing has improved performance by a factor of 10.

The convex optimization problem for a consistent underdetermined linear system $A x = b$ is

$$
\operatorname* { m i n } _ { x } \| x \| _ { p } ^ { p } \quad { \mathrm { s u b j e c t ~ t o } } \quad A x = b , \quad 1 \leq p \leq 2 ,
$$

and can be solved by IRLS. For $p = 2$ ,the solution of (8.4.25) is the pseudoinverse solution $x = A ^ { \dagger } b$ For $1 \le p \le 2$ ,the $\ell _ { p }$ is rewritten as a weighted $\ell _ { 2 }$ -norm

$$
\| x \| _ { p } ^ { p } = \sum _ { i = 1 } ^ { n } ( | x _ { i } | / w _ { i } ) ^ { 2 } , \quad w _ { i } = | x _ { i } | ^ { ( 1 - p / 2 ) } .
$$

With $W = \mathrm { d i a g } \left( w _ { i } \right)$ , problem (8.4.25) is equivalent to the weighted least-norm problem

$$
\operatorname* { m i n } \| W ^ { - 1 } x \| _ { 2 } ^ { 2 } \quad { \mathrm { s u b j e c t ~ t o } } \quad A x = b .
$$

From the weighted normal equations of the second kind, we obtain

$$
x = W ^ { 2 } A ^ { T } ( A W ^ { 2 } A ^ { T } ) ^ { - 1 } b .
$$

A more stable alternative is to use the (compact) QR factorization

$$
W A ^ { T } = Q R , \qquad x = W Q ( R ^ { - T } b ) .
$$

If possible, the rows in $W A$ should be presorted by decreasing row norms of $W A ^ { T }$ ; see Section 3.2.2.

Since the weights $w _ { i }$ are well defined for any $x _ { i }$ ,in principle no regularization is needed. However, to prevent the matrix being inverted in (8.4.28) from becoming too ill-conditioned, the weights should be regularized as

$$
w _ { i } = | x _ { i } | ^ { ( 1 - p / 2 ) } + \epsilon ,
$$

where $\epsilon = 1 0 ^ { - 6 }$ initially, and each iteration decreases $\epsilon$ by a factor of 2.

The MATLAB implementation below follows Burrus [190,2o12]. The iterations are started with the least squares solution, corresponding to $p _ { 1 } = 2$ . A continuation strategy is used for $p$ ， where the current value $p _ { k }$ is decreased by a fixed amount $d p$ at each iteration until the target $p$ is reached.

# Algorithm 8.4.2 (Compressed Sensing by IRLS).

function $[ \mathrm { x } , \mathrm { n r m } ] = \mathrm { i } \mathrm { r } 1 \mathrm { s } \left( \mathrm { A } , \mathrm { b } , \mathrm { p } , \mathrm { d } \mathrm { p } , \mathrm { k m a x } \right)$ $\%$ IRLS for minimizing $| \mathbf { \nabla } | \ A \mathbf { x } \ \texttt { - b } | \ | \mathbf { \Pi } _ { - \mathbf { p } }$ ，where $\% 0 < \texttt { p } < 2$ ，and A is m by n, $\texttt { m } < \texttt { n }$ % $\texttt { x } = \texttt { A } ^ { \prime } \backslash \mathtt { b }$ ； epsw = 1.0e-6\*ones(size(b)); $\mathtt { N r m } \ = \ \mathtt { n o r m } ( \mathbf { x } , \mathtt { p } ) \ ; \quad \mathtt { p k } \ = \ 2 ;$ for $\texttt { k } = \texttt { 1 }$ : kmax $\begin{array} { r l } & { \mathrm { p k \ = \ \operatorname* { m a x } \left( \left[ p , p k \_ - \ d p \right] \right) ; } } \\ & { \mathrm { w \ = \ \left( x \cdot \hat { \Phi } 2 \ + \ \varphi p s w \right) \cdot \hat { \Phi } \left( 1 \ - \ p k / 2 \right) ; } } \\ & { \mathrm { e p s w \ = \ \varphi p s w / 2 ; } } \end{array}$ % Sort weights and reorder columns $\begin{array} { r c l } { { } } & { { } } & { { \mathsf { W \ = \ d i a g ( u ) \ ; A \ = \ A ( : , j ) \ ; } } } \\ { { } } & { { } } & { { \left[ \bar { \mathbf { w } } \ , \mathbf { j } \ \right] \ \ = \ \mathsf { s o r t ( \bar { \mathbf { w } } ) \ ; } } } \\ { { } } & { { } } & { { \mathbf { x ( j ) } \ = \ \mathsf { ( A { * } W ) \ ^ { \alpha } \setminus b } \ ; } } \\ { { } } & { { } } & { { \mathrm { N r m \ = \ \left[ N r m , n o r m \left( x \ , p \right) \right] ; } } } \end{array}$ end   
end

It is possible to improve the ability of $\ell _ { 1 }$ minimization to recover sparse solutions by choosing $p = 0$ as target value in IRLS; see Chartrand [237, 2oo7], Chartrand and Yin [238,2oo8],and Yagle[1135, 2oo8]. Each iteration solves a convex optimization problem, but overall the iterative algorithm attempts to find a local minimum of the nonconvex problem

$$
\operatorname* { m i n } _ { x } \| x \| _ { 0 } \quad { \mathrm { s u b j e c t ~ t o } } \quad A x = b .
$$

Candes，Wakin,and Boyd [2O7, 2oo8] propose an iterative algorithm similar to IRLS in which each iteration solves the weighted $\ell _ { 1 }$ problem

$$
\operatorname* { m i n } _ { x } \| W ^ { - 1 } x \| _ { 1 } { \mathrm { ~ s u b j e c t ~ t o ~ } } A x = b ,
$$

and the weights are updated. This problem can be rewritten as a linear program like the unweighted $\ell _ { 1 }$ problAsieeht $w _ { i } ^ { ( 1 ) } = 1$ and then updated as

$$
w _ { i } ^ { ( k + 1 ) } = | x _ { i } ^ { ( k ) } | + \epsilon .
$$

The weighted $\ell _ { 1 }$ minimization problem (8.4.31) is viewed as a relaxation of the weighted $\ell _ { 0 }$ minimization problem

$$
\operatorname* { m i n } _ { x } \| W ^ { - 1 } x \| _ { 0 } { \mathrm { ~ s u b j e c t ~ t o ~ } } A x = b .
$$

Solving the weighted $\ell _ { 1 }$ problem(8.4.31） is more complex than solving the weighted least squares problems by IRLS. Candes, Wakin,and Boyd [2O7,2oo8] use the primal-dual log-barrier interior software package $\ell _ { 1 }$ -MAGIC. There is a marked improvement in the recovery of sparse signal compared to unweighted $\ell _ { 1 }$ minimization. The number of iterations needed is typically less than ten, but each iteration is computationally more costly than for IRLS.The primal-dual interior method PDCO [887,2o18] can also be applied as for Basis Pursuit or Basis Pursuit Denoising.

# Notes and references

An early use of reweighted $\ell _ { 1 }$ minimization was for matrix rank minimization and portfolio op-$\textstyle \sum _ { i = 1 } ^ { \operatorname* { m i n } \{ m , n \} } \sigma _ { i } ( A )$ $\ell _ { 1 }$ $\| A \| _ { * } =$ was suggested by Rao and Kreutz-Delgado [911, 1999]. Nesterov and Nemirovski [827, 2013] review first-order methods for $\ell _ { 1 }$ - and nuclear norm minimization. They show that such methods can have only sublinear convergence but that the rate of convergence is nearly dimensionindependent.

Algorithms for computing sparse solutions of underdetermined linear systems with applications to matrix completion, graph clustering,and phase retrieval are given by Lai and Wang in the book [710].

# Bibliography

[1] Ahmad Abdelfattah,Hartwig Anzt,Erik G.Boman,Erin Carson,Terry Cojean, Jack Dongarra, Alyson Fox,Mark Gates,Nicolas J. Higham, Xiaoye S.Li, Jennifer Loe,Piotr Luszczek, Srikara Pranesh,SivaRajamanickam,Tobias Ribizel,BarryF.Smith,Kasia Swirydowicz,Stephen Thomas, Stanimire Tomov, Yaohung M. Tsai,and Ulrike Meier Yang.A survey of numerical linear algebra methods utilizing mixed-precision arithmetic. Internat. J. High Performance Comput. Appl., 35:344-369,2021. (Cited on p. 114.) [2] Ahmad Abdelfattah, Hartwig Anzt, Jack Dongarra,Mark Gates,Azzam Haidar, Jakub Kurzak, Piotr Luszczek,Stanimire Tomov,Ichitaro Yamazaki,and A.YarKhan.Linear algebra software for large-scale accelerated multicore computing. Acta Numer.,25:1-160,2016.(Cited on pp.112, 114.)   
[3] N.N.Abdelmalek. On the solution of the linear least squares problems and pseudoinverses. Computing,13:215-228,1971. (Cited on p. 31.)   
[4] N.N. Abdelmalek. Roundof error analysis for Gram-Schmidt method and solution of linear least squares problems. BIT Numer Math.,11:345-368,1971. (Cited on p. 71.)   
[5] N.N. Abdelmalek．Algorithm 551:A Fortran subroutine for the $l _ { 1 }$ solution of overdetermined linear systems of equations.ACM Trans.Math.Softw.,6:228-230,1980.(Cited on p. 421.) [6] N.N. Abdelmalek. $l _ { 1 }$ solution of overdetermined linear systems of equations.ACM Trans.Math. Softw.,6:220-227,1980. (Cited on p. 421.)   
[7] R.J. Adcock.A problem in least squares. The Analyst, 5:53-54,1878. (Cited on p. 407.)   
[8] Mikael Adlers and Ake Bjorck. Matrix stretching for sparse least squares problem. Numer. Linear Algebra Appl.,7:51-65,2000. (Cited on p. 263.)   
[9] S.N.Afriat. Orthogonal and oblique projectors and the characteristics of pairs of vector spaces. Proc. Cambridge Philos. Soc.,53:800-816,1957. (Cited on p.119.)   
[10] E. Agullo,James W. Demmel, Jack Dongarra,B.Hadri, Jakub Kurzak Julien Langou, H.Ltaief, P.Luszczek,and S. Tomov. Numerical linear algebra on emerging architectures: The PLASMA and MAGMA projects.J. Phys. Conf. Ser.,180:012037,2009. (Cited on p.114.)   
[11] N. Ahmed,T. Natarajan,and K.R. Rao. Discrete cosine transform. IEEE Trans. Comput., C23:90- 93,1974. (Cited on p. 237.)   
[12] Alexander Craig Aitken. On least squares and linear combinations of observations. Proc. Roy. Soc. Edinburgh,55:42-48,1934/1936. (Cited on p. 5.)   
[13] M.A. Ajiz and Alan Jennings.A robust incomplete Cholesky-conjugate gradient algorithm. Int. J. Numer Meth. Eng.,20:949-966,1984. (Cited on pp.310,310.)   
[14] M.Al-Baali and Roger Fletcher. Variational methods for non-linear least squares.J. Oper: Res. Soc.,36:405-421,1985. (Cited on p. 400.)   
[15]M. Al-Baali and R.Fletcher. An efcient line search for nonlinear least-squares.J. Optim. Theory Appl.,48:359-377,1986. (Cited on p. 400.)   
[16] S.T. Alexander, Ching-Tsuan Pan,and Robert J. Plemmons.Analysis of a recursive least squares hyperbolic rotation algorithm for signal processing.Linear Algebra Appl., 98:3-40,1988. (Cited on p. 137.)   
[17] D.M. Allen. The relationship between variable selection and data augmentation and a method for prediction. Technometrics,16:125-127,1974. (Cited on p.178.)   
[18]Patrick R. Amestoy, Timothy A.Davis,and Iain S.Duf. Algorithm 837: AMD,an an approximate minimum degree ordering algorithm. ACM Trans. Math. Softw., 30:381-388,2004. (Cited on p. 252.)   
[19] Patrick R. Amestoy, I. S. Duff,and C. Puglisi. Multifrontal QR factorization in a multiprocessor environment. Numer Linear Algebra Appl.,3:275-300,1996.(Cited on p.258.)   
[20] Greg S. Ammar and William B. Gragg. Superfast solution of real positive definite Toeplitz systems. SIAM J. Matrix Anal. Appl., 9:61-76,1988. (Cited on p. 241.)   
[21] A.A. Anda and Haesun Park. Fast plane rotations with dynamic scaling. SIAM J. Matrix Anal. Appl.,15:162-174,1994. (Cited on p. 51.)   
[22] A.Anda and Haesun Park. Self-scaling fast rotations for stiff least squares problems.Linear Algebra Appl.,234:137-162,1996. (Cited on p. 132.)   
[23] Bjarne S.Andersen, Jerzy Wasniewski, and Fred G. Gustavson.A recursive formulation of Cholesky factorization for a packed matrix. ACM Trans. Math. Softw.,27:214-244,2001.(Cited on p. 112.)   
[24] R.S.Andersen and Gene H.Golub.Richardson's Non-stationary Matrix Iterative Procedure.Tech. Report STAN-CS-72-304, Computer Science Department, Stanford University, CA,1972.(Cited on p. 326.)   
[25] Edward Anderssn, Zhaojun Bai, and Jack J.Dongarra. Generalized QR factorization and its applications. Linear Algebra Appl.,162/164:243-271,1992. (Cited on pp.124,128.)   
[26] E. Anderson, Z. Bai, C. Bischof,J. Demmel, J. Dongarra, J.Du Croz,A. Greenbaum, S.Hammar-ling, A. McKenney, S. Ostrouchov,and D.Sorensen. LAPACK Users' Guide. SIAM, Philadelphia, second edition,1995. (Cited on p. 97.)   
[27]E. Anderson, Z.Bai, C.Bischof,L. S. Blackford,J. W. Demmel,J.Dongarra,J.Du Croz,A. Greenbaum,S. Hammarling,A. McKenney,and D.Sorensen. LAPACK Users' Guide. SIAM,Philadelphia, third edition,1999. (Cited on p. 114.)   
[28] Claus A.Andersson and Rasmus Bro. The $N$ way toolbox for MATLAB. Chemom. Intell. Lab. Syst.,52:1-4,2000. (Cited on p. 218.)   
[29] Martin Andersson. A comparison of nine PLS1 algorithms. J. Chemometrics,23:518-529,2009. (Cited on pp.202,203.)   
[30] Peter Arbentz and Gene H. Golub. Matrix shapes invariant under symmetric QR algorithm. Numer: Linear Algebra Appl.,2:87-93,1995. (Cited on p. 341.)   
[31] M. Arioli. Generalized Golub-Kahan bidiagonalization and stopping criteria. SIAM J. Matrix Anal. Appl.,34:571-592,2013. (Cited on pp. 331, 331.)   
[32]Mario Arioli, Marc Baboulin,and Serge Gratton. A partial condition number for linear least squares problems. SIAM J. Matrix Anal. Appl.,29:413-433,2007. (Cited on p.29.)   
[33] M. Arioli, J. W. Demmel,and I. S. Duff. Solving sparse linear systems with sparse backward error. SIAM J. Matrix Anal. Appl.,10:165-190,1989. (Cited on pp.97,104.)   
[34] Mario Arioli and Iain S.Duf. Preconditioning linear least-squares problems by identifying a basis matrix. SIAM J. Sci. Comput.,37:S544-S561,2015. (Cited on p. 319.)   
[35] Mario Arioli, Iain Duf, Joseph Noailles,and Daniel Ruiz.A block projection method for sparse matrices. SIAM J. Sci. Comput.,13:47-70,1992. (Cited on p. 275.)   
[36] Mario Arioli, Iain S. Duff,and Peter P.M. de Rijk. On the augmented system approach to sparse least-squares problems. Numer Math.,55:667-684,1989. (Cited on pp.31,104.)   
[37] Mario Arioli, Iain Duf,and Daniel Ruiz. Stopping criteria for iterative solvers.SIAM J. Matrix Anal. Appl.,13:138-144,1992. (Cited on p. 299.)   
[38]Mario Arioli,Iain S.Duff,Daniel Ruiz,and Miloud Sadkane.Block Lanczos techniques for accelerating the block Cimmino method. SIAM J. Sci. Comput.，16:1478-1511,1995.(Cited on p. 275.)   
[39] W.E.Arnoldi. The principle of minimized iteration in the solution of the matrix eigenvalue problem. Quart Appl. Math., 9:17-29,1951. (Cited on p. 301.)   
[40] Stephen F. Ashby,Thomas A. Manteuffel,and Paul E. Saylor. A taxonomy for conjugate gradient methods. SIAM J. Numer Anal.,27:1542-1568,1990. (Cited on p. 336.)   
[41] Leon Autonne. Sur les groupes lineaires réels et orthogonaux. Bull Soc. Math. France,30:121-134, 1902.(Cited on p. 383.)   
[42] Leon Autonne.Sur les matrices hypohermitiennes et les unitaires.C.R.Acad.Sci.Paris,156:858- 860,1913. (Cited on p. 13.)   
[43] Leon Autonne. Sur les matrices hypohermitiennes et sur les matrices unitaires. Ann. Univ. Lyon (N.S.),38:1-77,1915. (Cited on p. 13.)   
[44] J. K. Avila and J.A. Tomlin. Solution of very large least squares problems by nested dissection on a parallel processor.In J.F.Gentleman, editor,Proceedings of the Computer Science and Statistics 12th Annual Symposium on the Interface. University of Waterloo,Canada,1979.(Cited on p. 209.)   
[45] Haim Avron, Esmond $\mathrm { N g }$ ，and Sivan Toledo. Using perturbed QR factorizations to solve linear least-squares problems. SIAM J. Matrix Anal. Appl.,31:674-693,2009. (Cited on p. 263.)   
[46] H. Avron, P. Maymounkov, and S. Toledo. Blendenpik: Supercharging LAPACK's least squares solver. SIAM J. Sci. Comput.,32:1217-1236,2010. (Cited on p.320.)   
[47] Owe Axelsson. A generalized SSOR method. BIT Numer Math.,12:443-467,1972. (Cited on p.308.)   
[48] Owe Axelsson. Iterative Solution Methods.Cambridge University Press,Cambridge,1994.(Cited on pp.269,275,281,295.)   
[49] Marc Baboulin,Luc Giraud, Serge Graton,and Julien Langou.Parallel tools for solving incremental dense least squares. Applications to space geodesy. J. Algorithms Comput. Tech., 3:117-133, 2009.(Cited on pp.3,112.)   
[50] Marc Baboulin and Serge Graton.Computing the conditioning of the components of a linear least-squares solution. Numer. Linear Algebra Appl.,16:517-533,2009. (Cited on p. 31.)   
[51] Marc Baboulin and Serge Gratton.A contribution to the conditioning of the total least squares problem. SIAM J. Matrix Anal. Appl., 32:685-699,2011. (Cited on p. 226.)   
[52] Brett W. Bader and Tamara G. Kolda. Algorithm 862: MATLAB tensor classes for fast algorithm prototyping. ACM Trans. Math. Softw.,32:455-500,2006. (Cited on p. 218.)   
[53] Brett W. Bader and Tamara G. Kolda. Efcient MATLAB computations with sparse and factored tensors. SIAM J. Sci. Comput.,30:205-231,2007. (Cited on p. 218.)   
[54] J. Baglama,D. Calveti,and L. Reichel. IRBL: An implicitly restarted block-Lanczos method for large-scale Hermitian eigenproblems. SIAM J. Sci. Comput.,24:1650-1677,2003．(Cited on pp.370,372.)   
[55] James Baglama,Daniela Calvet,and Lothar Reichel.Algorithm 827:irbleigs:A MATLAB program for computing a few eigenpairs of a large sparse Hermitian matrix. ACM Trans. Math. Softw.,29:337-348,2003. (Cited on p. 374.)   
[56] James Baglama and Lothar Reichel. Augmented implicitly restarted Lanczos bidiagonalization methods. SIAM J. Sci. Comput.,27:19-42,2005. (Cited on pp.373,374.)   
[57] James Baglama and Lothar Reichel.Restarted block Lanczos bidiagonalization methods. Numer: Algor,43:251-272,2006. (Cited on p. 374.)   
[58] James Baglama, Lothar Reichel, and Daniel J. Richmond. An augmented LSQR method. Numer: Algor.,64:263-293,2013. (Cited on p. 337.)   
[59] Zhaojun Bai and James W. Demmel. Computing the generalized singular value decomposition. SIAM J. Sci. Comput.,14:1464-1486,1993. (Cited on pp.125, 356.)   
[60] Zhaojun Bai and James Demmel. Using the matrix sign function to compute invariant subspaces. SIAM J. Matrix Anal. Appl.,19:205-225,1998. (Cited on pp.380, 382.)   
[61] Zhaojun Bai,James Demmel, Jack Dongarra,Axel Ruhe,and Henk van der Vorst, editors.Tem-plates for the Solution of Algebraic Eigenvalue Problems: A Practical Guide. SIAM,Philadelphia, 2000.(Cited on pp.349,375.)   
[62] Zhaojun Bai, James W. Demmel, and Ming Gu. An inverse free paralel spectral divide and conquer algorithm for nonsymmetric eigenproblems. Numer: Math.,76:279-308,1997. (Cited on p. 382.)   
[63] Zhaojun Bai and Hongyuan Zha. A new preprocessing algorithm for the computation of the generalized singular value decomposition. SIAM J. Sci. Comput.，14:1007-1012,1993．(Cited on p. 125.)   
[64] Zhong-Zhi Bai, Iain S. Duff,and Andrew J. Wathen. A class of incomplete orthogonal factorization methods I: Methods and theories. BIT Numer: Math.,41:53-70,2001. (Cited on p. 315.)   
[65] Grey Balard, James Demmel, Olga Holtz, and Oded Schwartz. Minimizing communication in numerical linear algebra. SIAM J. Matrix Anal. Appl.,32:866-901,2011. (Cited on p. 114.)   
[66] Y.Bard. Nonlinear Parameter Estimation. Academic Press,New York,1974. (Cited on p. 391.)   
[67] Jesse L. Barlow. Modification and maintenance of ULV decompositions. In Zlatko Drmac, Vjeran Hari,Luka Sopta, Zvonimir Tutek,and Kresimir Veselic,editors,Applied Mathematics and Scientific Computing, pages 31-62. Springer, Boston,MA,2003. (Cited on p. 155.)   
[68] Jesse L. Barlow. Reorthogonalization for the Golub-Kahan-Lanczos bidiagonal reduction. Numer: Math.,124:237-278,2013. (Cited on p. 298.)   
[69] Jesse L. Barlow. Block Gram-Schmidt downdating. ETNA,43:163-187,2014. (Cited on p. 152.)   
[70] Jesse L. Barlow. Block modified Gram-Schmidt algorithm and their analysis. SIAM J. Matrix Anal. Appl.,40:1257-1290,2019. (Cited on p. 152.)   
[71] Jesse L. Barlow, Nela Bosner, and Zlatko Drmac. A new stable bidiagonal reduction algorithm. Linear Algebra Appl.,397:35-84,2005. (Cited on p. 194.)   
[72] Jesse L.Barlow and Hasan Erbay. A modifiable low-rank approximation of a matrix. Numer Linear Algebra Appl.,16:833-860,2009. (Cited on p.155.)   
[73] Jesse L. Barlow, Hasan Erbay,and Ivan Slapnicar. An alternative algorithm for the refinement of ULV decompositions. SIAM J. Matrix Anal. Appl.,27:198-211, 2005. (Cited on p. 155.)   
[74] Jesse L. Barlow and Susan L. Handy. The direct solution of weighted and equality constraned least-squares problems. SIAM J. Sci. Statist. Comput., 9:704-716,1988. (Cited on p.160.)   
[75] J.L. Barlow,N.K. Nichols,and R.J. Plemmons. Iterative methods for equality-constrained least squares problems. SIAM J. Sci. Statist. Comput., 9:892-906,1988. (Cited on p. 319.)   
[76] Jesse L. Barlow and Alicja Smoktunowicz. Reorthogonalized block classical Gram-Schmidt. Numer Math.,123:395-423,2013. (Cited on pp.109,152.)   
[77] Jesse L. Barlow, Alicja Smoktunowicz, and Hasan Erbay. Improved Gram-Schmidt downdating methods.BIT Numer. Math.,45:259-285,2005. (Cited on p.152.)   
[78] Jesse L. Barlow and Udaya B. Vemulapati. A note on deferred correction for equality constrained least squares problems.SIAM J. Numer Anal.,29:249-256,1992. (Cited on p. 160.)   
[79] JesseL.Barlow, P.A. Yoon,and Hongyuan Zha. An algorithm and a stability theory for downdating the ULV decomposition. BIT Numer Math.,36:14-40,1996. (Cited on p. 155.)   
[80] Jesse L. Barlow, Hongyuan Zha, and P.A. Yoon. Stable Chasing Algorithms for Modifying Com-plete and Partial Singular Value Decompositions. Tech. Report CSE-93-19, Department of Com-puter Science,The Pennsylvania State University, State College,PA,1993. (Cited on p. 363.) [81] S.T. Barnard,Alan Pothen,and Horst D. Simon.A spectral algorithm for envelope reduction of sparse matrices.Numer. Algor,2:317-334,1995. (Cited on p. 251.) [82] Richard Barret,Michael Berry, Tony F. Chan, James Demmel, June Donato,Jack Dongarra, Victor Eijkhout,Roldan Pozo,Charles Romine,and Henk van der Vorst. Templates for the Solution of Linear Systems:Building Blocks for Iterative Methods.SIAM,Philadelphia,1994.(Cited on p. 269.) [83] Anders Barlund. Perturbation bounds on the polar decomposition. BITNumer: Math.,3O:101-113, 1990. (Cited on p. 385.) [84] Anders Barrlund. Eficient solution of constrained least squares problems with Kronecker product structure.SIAMJ. Matrix Anal. Appl.,19:154-160,1998. (Cited on p.211.)   
[85] Ian Barrodale and C. Phillips.Algorithm 495: Solution of an overdetermined system of linear equations in the Chebyshev norm. ACM Trans. Math. Softw.,1:264-270,1975.(Cited on p. 423.)   
[86] Ian Barrodale and F. D. K. Roberts. Applications of mathematical programming to $l _ { p }$ approximation.In J. B.Rosen,O.L Mangasarian,and K. Riter,editors,Nonlinear Programming,pages 447-464.Academic Press,New York,1970. (Cited on p. 421.)   
[87] I. Barrodale and F. D.K. Roberts. An improved algorithm for discrete $l _ { 1 }$ linear approximation. SIAM J. Numer: Anal.,10:839-848,1973. (Cited on p. 421.) [88] Ian Barrodale and F. D.K.Roberts.Algorithm 478: Solution of an overdetermined system of equations in the $\ell _ { 1 }$ norm. Comm. ACM,17:319-320,1974. (Cited on pp.421,422.)   
[89] Richard H. Bartels and Andrew R. Conn. Algorithm 563:A program for linearly constrained discrete $\ell _ { 1 }$ problems. ACM Trans. Math. Softw., 6:609-614,1980. (Cited on p. 421.)   
[90] Richard H. Bartels,Andrew R. Conn,and J. W. Sinclair. Minimization techniques for piecewise differentiable functions: The $l _ { 1 }$ solution to an overdetermined linear system. SIAM J. Numer. Anal., 15:224-241,1978. (Cited on p. 423.)   
[91] Richard H. Bartels and Gene H. Golub. Chebyshev solution to an overdetermined system. Algorithm 328. Comm. ACM,11:428-430,1968. (Cited on p. 423.) [92] Richard H. Bartels and Gene H. Golub. Stable numerical methods for obtaining the Chebyshev solution to an overdetermined system. Comm.ACM,11:401-406,1968.(Cited on p. 423.) [93] W.Barth,R.S.Martin,and James H.Wilkinson. Calculation of the eigenvalues of a symmetric tridiagonal matrix by the method of bisection. InF.L. Bauer et al.,editors, Handbook for Automatic Computation.Vol. I,Linear Algebra, pages 249-256.Springer,New York,1971. Prepublished in Numer. Math.,9:386-393,1967． (Cited onp. 350.)   
[94] Friedrich L. Bauer. Das Verfahren der Treppeniteration und verwandte Verfahren zur Losung algebraischer Eigenwertprobleme. Z. Angew. Math. Phys.,8:214-235,1957. (Cited on p.367.)   
[95] Friedrich L. Bauer. Genauigkeitsfragen bei der Losung linearer Gleichungssysteme. Z. Angew. Math. Mech.,46:409-421,1966. (Cited on pp. 31,44.)   
[96] Amir Beck and Aharon Ben-Tal. On the solution of the Tikhonov regularization of the total least squares problem. SIAM J. Optim.,17:98-118,2006. (Cited on p. 226.)   
[97] Stefania Bellavia, Jacek Gondzio,and Benedetta Morino.A matrix-free preconditioner for sparse symmetric positive definite systems and least-squares problems. SIAM J. Sci. Comput.,35:A192- A211,2013. (Cited on p. 311.)   
[98] Eugenio Beltrami. Sulle funzioni bilineari.Giorn. Mat.ad Uso degli Studenti Delle Universita, 11:98-106,1873. (Cited on p. 13.)   
[99] Adi Ben-Israel. On iterative methods for solving non-linear least squares problems over convex sets. Israel J. Math.,5:211-224,1967. (Cited on p. 395.)   
[100] Adi Ben-Israel. The Moore of the Moore-Penrose inverse. Electronic J. Linear Algebra,9:150- 157,2002. (Cited on p. 16.)   
[101] Adi Ben-Israel and Thomas N. E. Greville. Generalized Inverses:Theory and Applications. Springer-Verlag, New York,second edition,2003.(Cited on p.16.)   
[102] Adi Ben-Israel and S. J. Wersan. An elimination method for computing the generalized inverse of an arbitrary matrix. J. Assoc. Comput. Mach.,10:532-537,1963. (Cited on p. 88.)   
[103] Aharon Ben-Tal and Marc Teboulle. A geometric property of the least squares solution of linear equations. Linear Algebra Appl.,139:165-170,1990. (Cited on p. 132.)   
[104] Steven J. Benbow. Solving generalized least-squares problems with LSQR. SIAM J. Matrix Anal. Appl.,21:166-177,1999. (Cited on pp.291,331.)   
[105] Commandant Benoit. Note sur une methode de résolution des équations normales provenant de l'application de la méthode des moindres carrés a un systeme d'équations linéaires en nombre inferieur a celui des inconnues.Application de la méthode a la résolution d'un systeme defini d'équations lineaires. (Procedé du Commandant Cholesky.） Bull. Geodésique,2:67-77,1924. (Cited on p. 41.)   
[106] Michele Benzi. Preconditioning techniques for large linear systems: A survey. J. Comput. Phys., 182:418-477,2002. (Cited on pp. 287, 314.)   
[107] Michele Benzi. Gianfranco Cimmino's contribution to Numerical Mathematics.In Ciclo di Conferenze in Ricordo di Gianfranco Cimmino, pages 87-109,Bologna, 20o5. Tecnoprint. (Cited on p. 273.)   
[108] Michele Benzi, Gene H. Golub,and Jorg Liesen. Numerical solution of saddle point problems. Acta Numer.,14:1-138,2005. (Cited on p. 117.)   
[109] Michele Benzi, Carl D. Meyer,and Miroslav Tüma. A sparse approximate inverse preconditioner for the conjugate gradient method. SIAM J. Sci. Comput.,17:1135-1149,1995. (Cited on p. 315.)   
[110] Michele Benzi and Miroslav Tüma. A robust incomplete factorization preconditioner for positive definite matrices. Numer Linear Algebra Appl.,10:385-400,2003.(Cited on p.315.)   
[111] Michele Benzi and Miroslav Tüma. A robust preconditioner with low memory requirements for large sparse least squares problems. SIAM J.Sci. Comput., 25:499-512, 2003. (Cited on p. 315.)   
[112] Abraham Berman and Robert J. Plemmons.Cones and iterative methods for best least squares solutions of linear systems. SIAM J. Numer. Anal.,11:145-154,1974. (Cited on p. 270.)   
[113] Michael W. Berry. A Fortran-77 Software Library for the Sparse Singular Value Decomposition. Tech.Report CS-92-159, Universityof Tennessee,Knoxville,TN,1992.(Cited on p. 376.)   
[114] Michael W.Berry. SVDPACKC: Version 1.0 User's Guide. Tech.Report CS-93-194, University of Tennessee,Knoxville, TN,1993.(Cited on p. 376.)   
[115] Michael W. Berry. A survey of public-domain Lanczos-based software. In J. D.Brown, M.T. Chu, D.C.Ellison,and Robert J. Plemmons, editors,Proceedings of the Cornelius Lanczos International Centenary Conference,Raleigh,NC,Dec.1993, pages 332-334.SIAM,Philadelphia,1994. (Cited on p. 376.)   
[116] Michael W. Berry, M. Browne,A. Langville, V. C. Pauca, and Robert J. Plemmons. Algorithms and applications for approximate nonnegative matrix factorizations. Comput. Data Statist. Anal., 21:155-173,2007. (Cited on p. 420.)   
[117] Rajendra Bhatia and Kalyan K. Mukherjea. On weighted Lowdin orthogonalization. Int. J. Quantum Chemistry,29:1775-1778,1986. (Cited on p. 383.)   
[118] I. J. Bienaymé. Remarques sur les différences qui distinguent I'interpolation de M. Cauchy de la methode des moindre carrés et qui assurent la supériorité de cette méthode. C. R. Acad. Sci. Paris, 37:5-13,1853. (Cited on p. 64.)   
[119] M. Bierlair,Philippe Toint, and D. Tuytens. On iterative algorithms for linear least-squares problems with bound constraints.Linear Algebra Appl.,143:111-143,1991. (Cited on p. 420.)   
[120] David Bindel, James W.Demmel, Wiliam M. Kahan,and Osni Marques.On computing Givens rotations reliably and effciently. ACM Trans. Math. Softw.,28:206-238,2002. (Cited on p. 50.)   
[121] Christian H. Bischof and Gregorio Quintana-Orti.Algorithm 782: Codes for rank-revealing QR factorizations of dense matrices. ACM Trans. Math. Softw.,24:254-257,1998.(Cited on p.109.)   
[122] Christian H. Bischof and Gregorio Quintana-Orti. Computing rank-revealing QR factorizations of dense matrices.ACMTrans.Math.Softw.,24:226-253,1998.(Cited on p.109.)   
[123] Christian Bischof and Charles Van Loan．The WY representation for products of Householder matrices. SIAM J. Sci. Statist. Comput., 8:s2-s13,1987. (Cited on p. 106.)   
[124] Ake Bjorck. Iterative refinement of linear least squares solutions I. BIT Numer: Math.,7:257-278, 1967. (Cited on pp. 93,101.)   
[125] Ake Bjorck.Solving linear least squares problems by Gram-Schmidt orthogonalization. BIT Numer Math.,7:1-21,1967. (Cited on pp. 28, 62,70,108.)   
[126] Ake Bjorck. Iterative refinement of linear least squares solutions II. BIT Numer. Math., 8:8-30, 1968.(Cited on pp.103,160.)   
[127] Ake Bjorck. Methods for sparse least squares problems.In J.R. Bunch and D. J. Rose, editors, Sparse Matrix Computations, pages 177-199. Academic Pres,New York,1976. (Cited on p. 317.)   
[128] Ake Bjorck． SSOR preconditioning methods for sparse least squares problems.In J. F. Gentleman, editor, Proceedings of the Computer Science and Statistics 12th Annual Symposium on the Interface,pages 21-25.University of Waterloo,Canada,1979. (Cited on pp.307,309.)   
[129] Ake Bjorck. Use of conjugate gradients for solving linear least squares problems. In I. S. Duff, editor, Conjugate Gradient Methods and Similar Techniques, pages 49-71. Computer Science and Systems Division, Harwell,AERE- R 9636,1979. (Cited on p. 294.)   
[130] Ake Bjorck. Stability analysis of the method of semi-normal equations for least squares problems. Linear Algebra Appl.,88/89:31-48,1987. (Cited on pp.105,105.)   
[131] Ake Bjorck.A bidiagonalization algorithm for solving il-posed systems of linear equations.BIT Numer: Math.,28:659-670,1988. (Cited on p. 332.)   
[132] Ake Bjorck. Component-wise perturbation analysis and error bounds for linear least squares solutions. BIT Numer: Math.,31:238-244,1991. (Cited on pp. 31, 99.)   
[133] Ake Bjorck. Pivoting and stability in the augmented system method. In D.F. Griffiths and G. A. Watson, editors,Numerical Analysis 1991: Proceedings of the 14th Dundee Biennal Conference, June 1991, Pitman Research Notes Math. Ser. 260, pages 1-16.Longman Scientific and Technical, Harlow, UK,1992. (Cited on p. 93.)   
[134] Ake Bjorck. Numerics of Gram-Schmidt orthogonalization. Linear Algebra Appl.,197/198:297- 316,1994.(Cited on pp. 67,108.)   
[135] Ake Bjorck. Numerical Methods for Least Squares Problems. SIAM,Philadelphia,1996.(Cited on p. 131.)   
[136] Ake Bjorck. QR factorization of the Jacobian in some structured nonlinear least squares problem. In Sabine Van Hufel and Philippe Lemmerling,editors,Total Least Squares and Errors-in-Variables Modeling. Analysis, Algorithms and Applications, pages 225-234. Kluwer Academic Publishers, Dordrecht, 2002. (Cited on p. 410.)   
[137] Ake Bjorck. Stability of two direct methods for bidiagonalization and partial least squares. SIAM J. Matrix Anal. Appl.,35:279-291,2014. (Cited on pp.200,201.)   
[138] Ake Bjorck and C. Bowie. An iterative algorithm for computing the best estimate of an orthogonal matrix. SIAM J. Numer Anal.,8:358-364,1971. (Cited on p. 383.)   
[139] Ake Bjorck and Iain S. DufA direct method for the solution of sparse linear least squares problems. Linear Algebra Appl.,34:43-67,1980. (Cited on p. 88.)   
[140] Ake Bjorck and Tommy Elfving. Algorithms for confluent Vandermonde systems. Numer Math., 21:130-137,1973. (Cited on p. 238.)   
[141] Ake Bjorck and Tommy Elfving.Accelerated projection methods for computing pseudoinverse solutions of inear systems.BITNumer Math.,19:145-163,1979.(Cited on pp.273,308.)   
[142] Ake Bjorck, Tommy Elfving,and Zdenek Strakos.Stability of conjugate gradient and Lanczos methods for linear least squares problems. SIAM J. Matrix Anal. Appl.,19:720-736,1998. (Cited on p. 294.)   
[143] Ake Bjorck and Gene H. Golub. Iterative refinement of linear least squares solution by Householder transformation. BIT Numer Math.,7:322-337,1967． (Cited on pp.101,102,157.)   
[144] Ake Bjorck and Gene H. Golub. Numerical methods for computing angles between subspaces. Math. Comp.,27:579-594,1973. (Cited on pp.17,19.)   
[145] Ake Bjorck,Eric Grimme,and Paul Van Dooren. An implicit shift bidiagonalization algorithm for ill-posed systems.BIT Numer: Math.,34:510-534,1994.(Cited on pp.332,373.)   
[146] Ake Bjorck and Sven J. Hammarling.A Schur method for the square root of a matrix. Linear Algebra Appl.,52/53:127-140,1983. (Cited on p. 378.)   
[147] Ake Bjorck, Pinar Heggernes, and Pontus Matstoms.Methods for large scale total least squares problems. SIAM J. Matrix Anal. Appl.,22:413-429,2000. (Cited on p. 224.)   
[148] Ake Bjorck and Ulf G. Indahl. Fast and stable partial least squares modelling: A benchmark study with theoretical comments. J. Chemom.,31:e2898,2017. (Cited on pp.202,203,203.)   
[149] A. Bjorck and C. C. Paige.Loss and recapture of orthogonality in the modified Gram-Schmidt algorithm. SIAM J. Matrix Anal. Appl.,13:176-190,1992. (Cited on pp. 66,70.)   
[150] Ake Bjorck and Christopher C. Paige. Solution of augmented linear systems using orthogonal factorizations.BIT Numer. Math.,34:1-26,1994.(Cited on pp.68,68.)   
[151] A. Bjorck, H. Park,and L. Elden. Accurate downdating of least squares solutions. SIAM J. Matrix Anal. Appl.,15:549-568,1994. (Cited on p. 147.)   
[152] Ake Bjorck and Victor Pereyra. Solution of Vandermonde system of equations. Math. Comp., 24:893-903,1970. (Cited on p. 238.)   
[153] Ake Bjorck and Jin Yun Yuan. Preconditioners for least squares problems by LU factorization. ETNA,8:26-35,1999. (Cited on p. 318.)   
[154] L. S.Blackford,J. Choi,A. Cleary,E. D'Azevedo,J.W. Demmel, I. Dhilon,J. Dongarra,S. Hammarling, G. Henry, A. Petitet, K. Stanley,D.Walker, and R. C. Whaley. ScaLAPACK Users' Guide. SIAM,Philadelphia,1997. ISBN 0-89871-397-8. (Cited on p. 114.)   
[155] L. Susan Blackford, James W. Demmel, Jack Dongarra,Iain Duff, Sven J. Hammarling, Greg Henry,Michael Heroux, Linda Kaufman,Andrew Lumsdaine,Antoine Petitet, Roldan Pozo, Karin Remington,and R. Clint Whaley. An updated set of Basic Linear Algebra Subprograms (BLAS). ACM Trans. Math. Softw.,28:135-151,2002. (Cited on p. 114.)   
[156] Elena Y. Bobrovnikova and Stephen A. Vavasis.Accurate solution of weighted least squares by iterative methods. SIAM J. Matrix Anal. Appl.,22:1153-1174,2001. (Cited on p. 133.)   
[157] Paul T.Boggs.The convergence of the Ben-Israel iteration for nonlinear least squares problems. Math. Comp.,30:512-522,1976. (Cited on pp. 395,397.)   
[158] Paul T. Boggs,Richard H. Byrd,and Robert B. Schnabel.A stable and efcient algorithm for nonlinear orthogonal distance regression. SIAM J. Sci. Statist. Comput.,8:1052-1078,1987. (Cited on pp.410,410,410.)   
[159]P.T.Boggs,J.R.Donaldson,R.H.Byrd,and R.B.Schnabel. ODRPACK software for weighted orthogonal distance regression. ACM Trans. Math. Softw.,15:348-364,1989. (Cited on p. 410.)   
[160] R.F. Boisvert, Roldan Pozo, K. Remington,R. Barret,and Jack J. Dongarra.Matrix Market: A web resource for test matrix collections. In R.F. Boisvert, editor, Quality of Numerical Software, Assessment and Enhancement, pages 125-137. Chapman & Hall, London, UK,1997. (Cited on pp. 244,295.)   
[161] Adam W. Bojanczyk and Richard P. Brent. Paralel solution of certain Toeplitz least-squares problems. Linear Algebra Appl.,77:43-60,1986. (Cited on p. 241.)   
[162] Adam W. Bojanczyk, Richard P. Brent,and Frank R. de Hoog. QR factorization of Toeplitz matrices. Numer Math.,49:81-94,1986. (Cited on p. 239.)   
[163] Adam W.Bojanczyk,Richard P.Brent,and Frank R.de Hoog. A Weakly Stable Algorithm for General Toeplitz Matrices. Tech.Report TR-CS-93-15, Cornell University, Ithaca, NY,1993.(Cited on p. 241.)   
[164] A. W. Bojanczyk,R.P.Brent, P.van Dooren,andF.de Hoog. A note on downdating the Cholesky factorization. SIAM J. Sci. Statist. Comput., 8:210-221,1987. (Cited on p.135.)   
[165] Adam W. Bojanczyk, Nicholas J. Higham,and Harikrishna Patel. The equality constrained indefinite least squares problem: Theory and algorithms. BIT Numer. Math.,43:505-517,2003.(Cited on p. 136.)   
[166] Adam Bojanczyk,Nicholas J. Higham,and Harikrishna Patel. Solving the indefinite least squares problem by hyperbolic QR factorization. SIAM J. Matrix Anal. Appl.,24:914-931,2003．(Cited on pp.133,134,135.)   
[167] Adam W. Bojanczyk and Adam Lutoborski. Computation of the Euler angles of a symmetric $3 \times 3$ matrix. SIAM J. Matrix Anal. Appl.,12:41-48,1991. (Cited on p. 51.)   
[168] Adam W. Bojanczyk and Alln O. Steinhardt. Stability analysis of a Householder-based algorithm for downdating the Cholesky factorization. SIAM J. Sci. Statist. Comput.,12:1255-1265,1991. (Cited on p. 148.)   
[169] D.Boley and Gene H. Golub. A survey of matrix inverse eigenvalue problems.Inverse Problems, 3:595-622,1987. (Cited on p. 230.)   
[170] F.L. Bookstein. Fitting conic sections to scatered data. Comput. Graphics Image Process., 9:56- 71,1979. (Cited on p. 414.)   
[171] Tibor Boros,Thomas Kailath,and Vadim Olshevsky. A fast paralel Bjorck-Pereyra-type algorithm for parallel solution of Cauchy linear systems.Linear Algebra Appl.,302/303:265-293,1999. (Cited on p. 239.)   
[172] C. Boutsidis and E. Gallopoulus. SVD-based initialization: A head start for nonnegative matrix factorization. Pattern Recognition,41:1350-1362,2008.(Cited on p.420.)   
[173] David W. Boyd. The power method for $\ell ^ { p \ }$ norms. Linear Algebra Appl., 9:95-101,1974. (Cited on p. 95.)   
[174] R.N.Bracewell The fast Hartley transform. Proc. IEEE.,72:1010-1018,1984.(Cited on p.320.)   
[175] R. Bramley and A. Sameh. Row projection methods for large nonsymmetric linear systems. SIAM J. Sci. Statist. Comput.,13:168-193,1992. (Cited on p. 275.)   
[176] Matthew Brand.Fast low-rank modification of the thin singular value decomposition．Linear Algebra Appl.,415:20-30,2006. (Cited on p. 363.)   
[177] Richard P. Brent. Algorithm 524: A Fortran multiple-precision arithmetic package. ACM Trans. Math. Softw.,4:71-81,1978. (Cited on p.33.)   
[178] Richard P. Brent. A Fortran multiple-precision arithmetic package. ACM Trans. Math. Softw., 4:57-70,1978. (Cited on p. 33.)   
[179] Richard P.Brent. Old and new algorithms for Toeplitz systems.InFranklin T.Luk,editor, Advanced Algorithms and ArchitecturesforSignal Processing II,SPIE Proceeding Series, Washington,pages 2-9,1988. (Cited on p. 241.)   
[180] Rasmus Bro.PARAFAC.Tutorial and applications. Chemom. Intell.Lab. Syst.,38:149-171,1997. Special Issue: 2nd International Conference in Chemometrics (INCINC'96). (Cited on pp. 216, 218.)   
[181] Rasmus Bro and Sijmen de Jong.A fast non-negativity-constrained least squares algorithm. J. Chemometrics,11:393-401,1997. (Cited on p. 167.)   
[182] Peter N. Brown and Homer F. Walker. GMRES on (nearly) singular systems. SIAM J. Matrix Anal. Appl.,18:37-51,1997. (Cited on p. 334.)   
[183] Rafael Bru,José Marin,José Mas,and Miroslav Tuma. Preconditioned iterative methods for solving linear least squares problems. SIAM J. Sci. Comput.,36:A2002-A2022,2014. (Cited on pp. 306, 312.)   
[184] Zvonimir Bujanovic and Zlatko Drmac.A contribution to the theory and practice of the block Kogbetliantz method for computing the SVD. BIT Numer: Math., 52:827-849,2012. (Cited on p. 357.)   
[185] J. R. Bunch.The weak and strong stability of algorithms in numerical linear algebra.Linear Algebra Appl.,88/89:49-66,1987. (Cited on p. 37.)   
[186] James R. Bunch.Stability of methods for solving Toeplitz systems of equations.SIAM J. Sci. Statist. Comput., 6:349-364,1985. (Cited on p. 241.)   
[187] James R. Bunch and Linda Kaufman. Some stable methods for calculating inertia and solving symmetric linear systems. Math. Comp.,31:163-179,1977. (Cited on p. 92.)   
[188] James R. Bunch and C.P. Nielsen. Updating the singular value decomposition. Numer: Math., 31:111-129,1978. (Cited on pp.361,363.)   
[189] Angelika Bunse-Gerstner,Valia Guerra-Ones,and Humberto Madrid de La Vega.An improved preconditioned LSQR for discrete ill-posed problems. Math. Comput. Simul.,73:65-75,2006. (Cited on p. 322.)   
[190] C. S. Burrus.Iterative Reweighted Least Squares. OpenStax-CNX Module m45285,2012. (Cited on p. 427.)   
[191] C. S. Burrus,J.A. Barreto,and I. W. Selesnick. Iterative reweighted least-squares design of FIR filters.IEEE Trans. Signal Process.,42:2926-2936,1994. (Cited on p. 425.)   
[192] Peter Businger. Updating a singular value decomposition. BIT Numer: Math.,10:376-385,1970. (Cited on p. 361.)   
[193] P.Businger and G. H. Golub. Linear least squares solutions by Householder transformations. Numer: Math.,7:269-276,1965. Also published as Contribution I/8 in Handbook for Automatic Computation, Vol.2,F.L. Bauer, ed.,Springer,Berlin,1971.(Cited on pp.56,101.)   
[194] Peter Businger and Gene H. Golub. Algorithm 358: Singular value decomposition of a complex matrix.Comm. ACM,12:564-565,1969. (Cited on p.349.)   
[195] Alfredo Buttari. Fine-grained multithreading for the multifrontal QR factorization of sparse matrices. SIAM J. Sci. Comput., 35:C323-C345,2013. (Cited on pp. 112, 258.)   
[196] Alfredo Buttari, Julien Langou, Jakub Kurzak,and Jack Dongarra.Parallel tiled QR factorization for multicore architectures. Concurrency and Computation: Practice and Experience,20:1573- 1590,2008．(Cited on p. 112.)   
[197] Richard H. Byrd, Peihuang Lu,Jorge Nocedal,and Ciyou Zhu. A limited memory algorithm for bound constrained optimization. SIAM J. Sci. Comput.,16:1190-1208,1995. (Cited on p. 420.)   
[198] Henri Calandra,Serge Gratton, Elisa Riccieti,and Xavier Vasseur. On iterative solution of the extended normal equations. SIAM J. Matrix Anal. Appl.,41:1571-1589,2020. (Cited on p. 331.)   
[199] Daniela Calveti, Per Christian Hansen,and Lothar Reichel. L-curve curvature bounds via Lanczos bidiagonalization. ETNA,14:20-35,2002.(Cited on p.178.)   
[200] Daniela Calvetti, Bryan Lewis,and Lothar Reichel. GMRES-type methods for inconsistent systems. Linear Algebra Appl.,316:157-169,2000. (Cited on p. 334.)   
[201] Daniela Calveti, Bryan Lewis,and Lothar Reichel. On the choice of subspace for iterative methods for linear discrete ill-posed problems.Int.J.Appl. Math. Comput. Sci.,11:1060-1092,2001.(Cited on p. 334.)   
[202] Daniela Calvetti, Bryan Lewis,and Lothar Reichel. On the regularization properties of the GMRES method. Numer Math.,91:605-625,2002. (Cited on p. 333.)   
[203] Daniela Calveti,Serena Morigi,Lothar Reichel,and Fiorella Sgallari.Tikhonov regularization and the L-curve for large discrete il-posed problems. J. Comput. Appl. Math.,123:423-446,2000. (Cited on p. 333.)   
[204] Daniela Calveti and Lothar Reichel. Tikhonov regularization of large linear problems.BIT Numer. Math.,43:283-484,2003. (Cited on p.335.)   
[205] Emmanuel J. Candes, Xiadong Li, Yi Ma,and John Wright. Robust principal component analysis? J. ACM,58:11,2011. (Cited on p. 212.)   
[206] Emmanuel J. Candes,J. Romberg,and T.Tao.Robust uncertainty principles: Exact signal reconstruction from highly incomplete frequency information. IEEE Trans. Inform. Theory,52:335-371, 2006. (Cited on p. 427.)   
[207] Emmanuel J. Candes, M. B. Wakin,and S.P.Boyd. Enhancing sparsity by reweighted $l _ { 1 }$ minimization. J. Fourier Anal. Appl.,14:877-905,2008. (Cited on pp. 428,428.)   
[208] Jesus Cardenal, Iain S.Duff,and José M. Jimenez.Solution of sparse quasi-square rectangular systems by Gaussian elimination. IMA J. Numer. Anal.,18:165-177,1998. (Cited on pp. 86, 87.)   
[209] Erin Carson and Nicholas J. Higham.Accelerating the solution of linear systems by iterative refinement in three precisions. SIAM J. Sci. Comput., 40:A817-A847,2018. (Cited on p.104.)   
[210] Erin Carson,Nicholas J. Higham,and Srikara Pranesh. Three-precision GMRES-based iterative refinement for least squares problems. SIAM J. Sci. Comput., 42:A4063-A4083,2020. (Cited on p. 104.)   
[211] Erin Carson,Kathryn Lund,Miroslav Rozloznik,and Stephen Thomas.Block Gram-Schmidt algorithms and their stability properties. Linear Algebra Appl., 638:150-195, 2022.(Cited on p.109.)   
[212] A. Cauchy. Mémoire sur P'interpolation. J. Math. Pures Appl.,2:193-205,1837. (Cited on p. 64.)   
[213] Yair Censor. Row-action methods for huge and sparse systems and their applications. SIAM Rev., 23:444-466,1981. (Cited on p. 274.)   
[214] Yair Censor and S.A. Zenios. Paralel Optimization. Theory,Algorithms,and Applications. Oxford University Press, Oxford,1997. (Cited on p. 274.)   
[215] Ales Cerny. Characterization of the oblique projector $U ( V U ) ^ { \dagger } V$ with applications to constrained least squares. Linear Algebra Appl., 431:1564-1570,2009. (Cited on p.119.)   
[216] Francoise Chaitin-Chatelin and Serge Gratton. On the condition numbers associated with the polar factorization of a matrix. Numer: Linear Algebra Appl.,7:337-354,2000. (Cited on p. 385.)   
[217] J. M. Chambers.Regresson updating. J. Amer: Statist. Assoc., 66:744-748,1971.(Cited on p. 135.)   
[218] Raymond H. Chan, James G. Nagy，and Robert J. Plemmons.FFT-based preconditioners for Toeplitz-block least squares problems. SIAM J. Numer. Anal., 30:1740-1768,1993．(Cited on p. 324.)   
[219] Raymond H. Chan, James G. Nagy,and Robert J. Plemmons. Circulant preconditioned Toeplitz least squares iterations. SIAM J. Matrix Anal. Appl.,15:80-97,1994. (Cited on p. 324.)   
[220] Raymond H. Chan and Michael K. Ng. Conjugate gradient methods for Toeplitz systems. SIAM Rev.,38:427-482,1996. (Cited on p. 325.)   
[221] Raymond H.-F. Chan and Xiao-Qing Jin. An Introduction to Iterative Toeplitz Solvers. SIAM, Philadelphia, 2007. (Cited on p. 325.)   
[222] Tony F. Chan． An improved algorithm for computing the singular value decomposition. ACM Trans. Math. Softw.,8:72-83,1982. (Cited on pp.192,193,347.)   
[223] Tony F. Chan.On the existence and computation of LU factorizations with small pivots. Math. Comput.,42:535-547,1984. (Cited on p. 89.)   
[224] Tony F. Chan. Rank revealing QR factorizations. Linear Algebra Appl.,88/89:67-82,1987. (Cited on pp. 76,81,82.)   
[225] Tony F. Chan. An optimal circulant preconditioner for Toeplitz systems. SIAM J. Sci. Statist. Comput., 9:766-771,1988. (Cited on p. 324.)   
[226] Tony F. Chan and D.E.Foulser. Effectively well-conditioned linear systems.SIAM J. Sci. Statist. Comput.,9:963-969,1988. (Cited on p. 172.)   
[227] Tony F. Chan and Per Christian Hansen. Computing truncated singular value decomposition least squares solutions by rank revealing QR-factorizations. SIAM J. Sci. Statist. Comput.,11:519-530, 1990. (Cited on pp. 83,174.)   
[228] Tony F. Chan and Per Christian Hansen. Some applications of the rank revealing QR factorization. SIAM J. Sci. Statist. Comput.,13:727-741,1992. (Cited on p. 174.)   
[229] Tony F. Chan and Per Christian Hansen. Low-rank revealing QR factorizations. Numer: Linear Algebra Appl.,1:33-44,1994. (Cited on p. 83.)   
[230] W. M. Chan and Alan George. A linear time implementation of the reverse Cuthill-McKee algorithm. BIT,20:1:8-14,1980. (Cited on p.251.)   
[231] Shivkumar Chandrasekaran and Ilse C.F. Ipsen. On rank-revealing factorizations. SIAM J. Matrix Anal. Appl.,15:592-622,1994. (Cited on pp.77,83.)   
[232] S. Chandrasekaran,M. Gu,and A.H. Sayed. A stable and efcient algorithm for the indefinite linear least-squares algorithm. SIAM J. Matrix Anal. Appl.,20:354-362,1998. (Cited on pp. 133, 133.)   
[233] S. Chandrasekaran and I. C.F. Ipsen. Analysis of a QR algorithm for computing singular values. SIAM J. Matrix Anal. Appl.,16:520-535,1995. (Cited on p. 343.)   
[234] Xiao-Wen Chang and Christopher C.Paige.Perturbation analysis for the Cholesky downdating problem. SIAM J. Matrix Anal. Appl.,19:429-443,1998. (Cited on p. 148.)   
[235] X.-W. Chang, C. C. Paige,and D. Titley-Peloquin. Stopping criteria for the iterative solution of linear least squares problems. SIAM J. Matrix Anal. Appl.,31:831-852,2009.(Cited on p. 299.)   
[236] J. Charlier,M. Vanbegin,and P. Van Dooren. On efficient implementations of Kogbetliantz's algorithm for computing the singular value decomposition. Numer: Math., 52:279-300,1988. (Cited on p. 357.)   
[237] Rick Chartrand. Exact reconstruction of sparse signals via nonconvex minimization. IEEE Proc. Lett,14:707-710,2007. (Cited on p. 428.)   
[238] R. Chartrand and Wotao Yin. Iteratively reweighted algorithms for compressive sensing. In Proceedings IEEE Int. Conf. Acoustics, Speech, Signal Processing (ICAsSP), pages 3869-3872,2008. (Cited on p. 428.)   
[239] Danghui Chen and Robert J. Plemmons. Nonnegativity constraints in numerical analysis. In Proceedings of the Symposium on the Birth of Numerical Analysis,pages 109-140,Katholieke Universiteit,Leuven,2007.(Cited on p. 167.)   
[240] Haibin Chen,Guoyin Li,and Liqun Qi. Further results on Cauchy tensors and Hankel tensors. Appl. Math. Comput.,275:50-62,2016. (Cited on p. 218.)   
[241] Scot Shaobing Chen, DavidL. Donoho,and Michael A.Saunders.Atomic decomposition by basis pursuit. SIAM Rev.,43:129-159,2001. (Cited on p. 427.)   
[242] Y. T. Chen. Iterative Methods for Linear Least Squares Problems. Tech. Report CS-75-04,Department of Computer Science,University of Waterloo,Waterloo, Ontario, Canada,1975.(Cited on p. 285.)   
[243] J.Choi, James W.Demmel,I. Dhillon,J. Dongara,S.Oustrouchov,A.Petitet,K.Stanley, D.Walker,and R.C.Whaley. ScaLAPACK: A portable linear algebra library for distributed memory computers—Design issues and performance. Comput. Phys. Comm.,97:1-15,1996. (Cited on p. 114.)   
[244] Sou-Cheng T.Choi. Iterative Methods for Singular Linear Equations and Least Squares Problems. Ph.D. thesis,ICME, Stanford University, Stanford, CA,2006.(Cited on p.283.)   
[245] Sou-Cheng T. Choi, Christopher C. Paige, and Michael A. Saunders. MINRES-QLP: A Krylov subspace method for indefinite or singular symmetric matrices. SIAM J. Sci. Comput., 33:1810- 1836,2011.(Cited on pp.300,300.)   
[246] Sou-Cheng T. Choi and Michael A. Saunders. Algorithm 937: MINRES-QLP for symmetric and Hermitian linear equations and least-squares problems. ACM Trans. Math. Softw.，40:16:1-12, 2014.(Cited on p. 300.)   
[247] Edmond Chow and Yousef Saad. Approximate inverse preconditioners via sparse-sparse iterations. SIAM J. Sci. Comput.,19:995-1023,1998. (Cited on p. 314.)   
[248] Moody T. Chu,Robert E.Funderlic,and Gene H. Golub.A rank-one reduction formula and its application to matrix factorization. SIAM Review,37:512-530,1995.(Cited on p. 139.)   
[249] J. Chun,T. Kailath,and H. Lev-Ari. Fast parallel algorithms for QR and triangular factorizations. SIAM J. Sci. Statist. Comput., 8:899-913,1987. (Cited on p. 240.)   
[250] Gianfranco Cimmino. Calcolo aprossimato per le soluzioni dei sistemi di equazioni lineari. Ricerca Sci. II, 9:326-333,1938. (Cited on p. 273.)   
[251] D. I. Clark and M. R. Osborne. Finite algorithms for Hubers's $M$ estimator. SIAM J. Sci. Statist. Comput.,7:72-85,1986. (Cited on p. 425.)   
[252] Alan K. Cline. Rate of convergence of Lawson's algorithm. Math. Comp.,26:167-176,1972. (Cited on p. 423.)   
[253] A. K. Cline.An elimination method for the solution of linear least squares problems. SIAM J. Numer: Anal.,10:283-289,1973. (Cited on pp. 88,130.)   
[254] Alan K. Cline. The Transformation of a Quadratic Programming Problem into Solvable Form. Tech. Report ICASE 75-14,NASA,Langley Research Center, Hampton,VA,1975.(Cited on p. 162.)   
[255] Alan K. Cline,A. R. Conn,and Charles F. Van Loan. Generalizing the LINPACK condition estimator. In J.P. Hennart, editor, Numerical Analysis,volume 909 of Lecture Notes in Mathematics, pages 73-83. Springer-Verlag,Berlin,1982. (Cited on p. 95.)   
[256] A. K. Cline, C.B.Moler, G. W. Stewart,and J. H. Wilkinson. An estimate for the condition number of a matrix. SIAM J. Numer. Anal.,16:368-375,1979. (Cited on pp. 95, 95.)   
[257] Randell E. Cline. Representations for the generalized inverse of sums of matrices. SIAM J. Numer. Anal.,2:99-114,1965. (Cited on p. 139.)   
[258] R. E.Cline and R. J. Plemmons. $l _ { 2 }$ -solutions to underdetermined linear systems. SIAM Rev., 18:92-106,1976. (Cited on p. 88.)   
[259] E. S. Coakley,V. Rokhlin,and M. Tygert. A fast randomized algorithm for orthogonal projection. SIAM J. Sci. Comput.,33:849-868,2011. (Cited on p.319.)   
[260] T.F. Coleman and Y.Li. A global and quadratically convergent affine scaling method for linear $l _ { 1 }$ problems. Math. Program.,56:189-222,1992. (Cited on p. 423.)   
[261] Thomas F. Coleman and Yuying Li. A global and quadratically convergent method for linear $l _ { \infty }$ problems. SIAM J. Numer Anal.,29:1166-1186,1992. (Cited on p. 423.)   
[262] Tom F. Coleman,Alan Edenbrandt,and John R.Gilbert.Predicting fillfor sparse orthogonal factorization. J. Assoc. Comput. Mach.,33:517-532,1986. (Cited on pp. 253,264.)   
[263] Pierre Comon, Gene H. Golub,Lek-Heng Lim,and Bernard Mourrain.Symmetric tensors and symmetric rank. SIAM J. Matrix Anal. Appl.,30:1254-1279,2008. (Cited on p.214.)   
[264] P. Comon, J.M.F. ten Berge,Lieven De Lathauwer,and J. Castaing. Generic and typical ranks of multiway arrays. Linear Algebra Appl.,430:2997-3007,2009. (Cited on p. 218.)   
[265] Andrew R. Conn, Nicholas I. M. Gould,and Philippe L. Toint. A globally convergent augmented Lagrangian algorithm for optimization with general constraints and simple bounds. SIAM J. Numer. Anal.,28:545-572,1991. (Cited on p. 400.)   
[266] Andy R. Conn, Nick I. M. Gould,and PhilippeL. Toint. LANCELOT: A Fortran Package for Large-Scale Nonlinear Optimization. (Release A). Springer-Verlag, Berlin,1992. (Cited on p. 400.)   
[267] J. W. Cooley.How the FFT gained acceptance.In S. G. Nash,editor, A History of Scientific Computing, pages 133-140. Addison-Wesley, Reading,MA,1990. (Cited on p. 237.) [268] J. W.Cooley,P.A.W.Lewis,and P.D.Welsh.The fast Fourier transform and its application. IEEE Trans. Education,E-12:27-34,1969. (Cited on p.237.) [269] James W. Cooley and John W. Tukey. An algorithm for machine calculation of complex Fourier series.Math. Comp.,19:297-301,1965.(Cited on p. 235.) [270] Corrado Corradi. A note on the solution of separable nonlinear least-squares problems with separable nonlinear equality constraints. SIAM J. Numer: Anal.,18:1134-1138,1981. (Cited on p. 404.) [271] A.J. Cox and Nicholas J. Higham. Backward error bounds for constrained least squares problems. BITNumer Math.,39:210-227,1999.(Cited on pp.99,157.) [272] Anthony J. Cox. Stability of Algorithms for Solving Weighted and Constrained Least Squares Problems.Ph.D. thesis, University of Manchester,Department of Mathematics,Manchester, UK,   
1997. (Cited on p. 131.) [273] Anthony J. Cox and Nicholas J. Higham.Stability of Householder QR factorization for weighted least squares problems. In D.F. Grifths,D.J. Higham,and G.A.Watson,editors,Numerical Analysis 1997: Proceedings ofthe 17th Dundee Biennial Conference,Pitman Research Notes Math. Ser. 380, pages 57-73.Longman Scientific and Technical, Harlow, UK,1998.(Cited on p.131.) [274] Anthony J. Cox and Nicholas J. Higham.Accuracy and stability of the null space method for solving the equality constrained least squares problem. BITNumer Math.,39:34-50,1999.(Cited on pp.157,160.) [275] Maurice G. Cox.The least-squares solution of linear equations with block-angular observation matrix. In Maurice G. Cox and Sven J. Hammarling,editors, Reliable Numerical Computation, pages 227-240. Oxford University Press,UK,1990. (Cited on pp.208,209.) [276] Trevor F. Cox and Michael A. A. Cox. Multidimensional Scaling. Chapman and Hall, London,   
1994.(Cited on p. 386.) [277]E.J.Craig. The $N$ -step iteration procedure.J.Math.Phys.,34:65-73,1955.(Cited onp. 284.) [278] P.Craven and Grace Wahba. Smoothing noisy data with spline functions. Numer: Math.,31:377-   
403,1979. (Cited on pp.178,189.) [279] Jane Cullum,Ralph A. Willoughby,and Mark Lake.A Lanczos algorithm for computing singular values and vectors of large matrices. SIAM J. Sci. Statist. Comput.,4:197-215,1983.(Cited on p. 376.) [280] J. J. M. Cuppen. A divide and conquer method for the symmetric tridiagonal eigenproblem. Numer. Math.,36:177-195,1981. (Cited on p. 358.) [281] E. Cuthil and J. McKee. Reducing the bandwidth of sparse symmetric matrices. In ACM '69: Proc. 24th Nat. Conf.,pages 157-172, New York,1969.ACM. (Cited on p. 251.) [282] George Cybenko. Fast Toeplitz orthogonalization using inner products. SIAM J. Sci. Statist. Comput., 8:734-740,1987. (Cited on p. 241.) [283] Germund Dahlquist and Ake Bjorck. Numerical Methods.Prentice-Hall Inc., Englewood Cliffs, NJ,1974. Reprinted in 2003 by Dover Publications,Mineola,NJ.(Cited on p. 231.) [284] Germund Dahlquist and Ake Bjorck. Numerical Methods in Scientific Computing, Volume I. SIAM, Philadelphia,2008.(Cited on pp.33,378.) [285] James W. Daniel, Wiliam B. Gragg,Linda Kaufman, and G. W. Stewart. Reorthogonalization and stable algorithms for updating the Gram-Schmidt QR factorization. Math. Comp.,3O:772-795,   
1976.(Cited on pp. 69,150.) [286] Ingrid Daubechies,Ronald DeVore,Massimo Fornasier,and C. Sinan Güntirk. Iteratively reweighted least squares minimization for sparse recovery. Comm. Pure Appl. Math., 63:1-38,2010. (Cited on p. 425.) [287]E. R. Davidson.The iterative calculation of a few of the lowest eigenvalues and corresponding eigenvectors of large real symmetric matrices. J. Comput.Phys.,17:87-94,1975.(Cited on p. 374.)   
[288] Chandler Davis and W. M. Kahan. The rotation of eigenvectors by a perturbation. II. SIAM J. Numer. Anal.,7:1-46,1970. (Cited on p. 19.)   
[289] Timothy A. Davis. Direct Methods for Sparse Linear Systems, volume 2 of Fundamental of Algorithms. SIAM, Philadelphia, 2006. (Cited on p. 244.)   
[290]Timothy_A.Davis.Algorithm915,SuiteSparseQR: Multifrontal multithreaded rank-revealing sparse QR factorization. ACM Trans. Math. Softw.,38:8:1-8:22,2011. (Cited on p. 258.)   
[291] Timothy A. Davis and Yifan Hu. The University of Florida sparse matrix collection. ACM Trans. Math. Softw.,38:1:1-1:25,2011. (Cited on pp. 244,297.)   
[292] Timothy A. Davis, Sivasankaran Rajamanickam,and Wissam M. Sid-Lakhdar. A survey of direct methods for sparse linear systems. Acta Numer,25:383-566,2016. (Cited on p. 244.)   
[293] Achiya Dax. The convergence of linear stationary iterative processes for solving singular unstructured systems of linear equations. SIAM Rev.,32:611-635,1990. (Cited on p. 270.)   
[294] Achiya Dax. On computational aspects of bounded linear least squares problems. ACM Trans. Math. Softw.,17:64-73,1991. (Cited on p. 417.)   
[295] Sijmen de Jong.SIMPLS: An alternative approach to partial least squares regression. Chemom. Intell.Lab. Syst.,18:251-263,1993. (Cited on p. 203.)   
[296] Lieven De Lathauwer, Bart De Moor, and Joos Vandewalle. A multilinear singular value decomposition. SIAM J. Matrix Anal. Appl.,21:1253-1278,2000. (Cited on p. 217.)   
[297] Bart De Moor. Structured total least squares and $l _ { 2 }$ approximation problems. Linear Algebra Appl., 188/189:163-206,1993.(Cited on p. 226.)   
[298] Bart De Moor and Paul Van Dooren. Generalizations of the singular value and QR decompositions. SIAM J. Matrix Anal. Appl.,13:993-1014,1992. (Cited on p. 128.)   
[299] Bart De Moor and H. Zha. A tree of generalizations of the ordinary singular value decomposition. Linear Algebra Appl.,147:469-500,1991. (Cited on p.128.)   
[300] Ron S.Dembo,Stanley C.Eisenstat,and Trond Steihaug.Inexact Newton methods. SIAM J. Numer. Anal.,19:400-408,1982. (Cited on pp. 401, 401.)   
[301] C. J. Demeure.Fast QR factorization of Vandermonde matrices.Linear Algebra Appl., 122/123/124:165-194,1989. (Cited on p. 239.)   
[302] C.J. Demeure. QR factorization of confluent Vandermonde matrices. IEEE Trans. Acoust. Speech Signal Process.,38:1799-1802,1990. (Cited on p. 239.)   
[303] James W.Demmel.On Floating Point Errors in Cholesky.Tech. Report CS-89-87,Department of Computer Science, University of Tennessee, Knoxville, TN,1989. LAPACK Working Note 14. (Cited on p. 43.)   
[304] James W. Demmel. The componentwise distance to the nearest singular matrix. SIAM J. Matrix Anal. Appl.,13:10-19,1992. (Cited on p. 31.)   
[305] James W.Demmel,Laura Grigori, Ming Gu,and Hua Xiang. Communication avoiding rank reveal-ing QR factorization with column pivoting. SIAM J. Matrix Anal. Appl.,36:55-89,2015. (Cited on p. 112.)   
[306] James W. Demmel, Laura Grigori, Mark Hoemmen, and Julien Langou. Communication-optimal parallel and sequential QR and LU factorizations. SIAM J. Sci. Comput., 34:A206-A239,2012. (Cited on p. 212.)   
[307] James W. Demmel, Ming Gu, Stanley Eisenstat, Ivan Slapnicar,Kresimir Veselic,and Zlatko Drmac. Computing the singular value decomposition with high relative accuracy. Linear Algebra Appl.,299:21-80,1999. (Cited on p. 344.)   
[308] James W.Demmel, Yozo Hida,E.Jason Riedy,and Xiaoye S.Li.Extra-precise iterative refinement for overdetermined least squares problems. ACM Trans. Math. Softw.,35:29:1-32,2009.(Cited on p. 103.)   
[309] James W. Demmel, Mark Hoemmen, Yozo Hida,and E. Jason Riedy. Non-negative Diagonals and High Performance on Low-Profile Matrices from Householder QR.LAPACK Working Note 203, Tech.Report UCB/EECS-2008-76, UCB/EECS,Berkeley, CA,2008.(Cited on p. 47.)   
[310] James Demmel and W. Kahan. Accurate singular values of bidiagonal matrices. SIAM J. Sci. Statist. Comput.,11:873-912,1990. (Cited on pp.343,343,348,356.)   
[311] James Demmel and Plamen Koev. The accurate and eficient solution of a totally positive generalized Vandermonde linear system. SIAM J. Matrix Anal. Appl.,27:142-152,2005.(Cited on p. 238.)   
[312] James Demmel and Kresimir Veselic. Jacobi's method is more accurate than QR. SIAM J. Matrix Anal. Appl.,13:1204-1245,1992. (Cited on p. 353.)   
[313] Eugene D. Denman and Alex N. Beavers. The matrix sign function and computations in systems. Appl. Math. Comput., 2:63-94,1976. (Cited on p. 379.)   
[314] John E.Dennis.Nonlinear least squares and equations.In D.A.H.Jacobs,editor,The State of the Art in Numerical Analysis, pages 269-312. Academic Press,New York,1977. (Cited on p. 402.)   
[315] John E. Dennis, David M. Gay,and R. E. Welsh. An adaptive nonlinear least-squares algorithm. ACM. Trans. Math. Softw.,7:348-368,1981. (Cited on pp. 398, 399.)   
[316] John E.Dennis, Jr.and Robert B.Schnabel. Numerical Methods for Unconstrained Optimization and Nonlinear Equations,volume 16 of Classics in Applied Math.， SIAM, Philadelphia, 1996. Originally published in 1983by Prentice-Hall,Englewood Cliffs,NJ.(Cited on pp.392,393, 399,402.)   
[317] J. E. Dennis, Jr. and Trond Steihaug.On the successive projections approach to least-squares problems. SIAM J. Numer. Anal.,23:717-733,1986. (Cited on p. 309.)   
[318] Peter Deuflhard and V. Apostolescu.A study of the Gauss-Newton algorithm for the solution of nonlinear least squares problems.In J.Frehse,D.Pallschke,and U.Trottenberg,editors,Special Topics of Applied Mathematics, pages 129-150. North-Hollnd,Amsterdam,1980.(Cited on p. 394.)   
[319] Peter Deuflhard and W. Sauter. On rank-deficient pseudoinverses.Linear Algebra Appl.,29:91- 111,1980. (Cited on p. 73.)   
[320] Inderjit S. Dhillon. A New $O ( n ^ { 2 } )$ Algorithm for the Symmetric Tridiagonal Eigenvalue/Eigenvector Problem.Ph.D. thesis,University of California, Berkeley, CA,1997. (Cited on p. 352.)   
[321] Inderjit S. Dhillon and Beresford N. Parlett. Orthogonal eigenvectors and relative gaps. SIAM J. Matrix Anal. Appl.,25:858-899,2004. (Cited on p. 352.)   
[322] J. J.Dongarr,J.R. Bunch, C.B. Moler, and G.W. Stewart.LINPACK Users’ Guide. SIAM, Philadelphia,1979.(Cited on pp.113,140,184,349.)   
[323] Jack Dongarra, Mark Gates,Azzam Haidar, Jakub Kurzak,Piotr Luszczek, Stanimire Tomov,and Ichitaro Yamazaki. The singular values decomposition: Anatomy of optimizing an algorithm for extreme scale. SIAM Rev.,60:808-865,2018. (Cited on pp.112,194,360.)   
[324] J. J.Dongarra and D.C.Sorensen. A fully parallel algorithmic for the symmetric eigenvalue problem. SIAM J. Sci. Statist. Comput., 8:s139-s154,1987. (Cited on p. 35.)   
[325] Jack Dongarra, Jeremy Du Croz, Sven J. Hammarling,and Richard J. Hanson. Algorithm 656. An extended set of FORTRAN Basic Linear Algebra Subprograms: Model implementation and test programs. ACM Trans. Math. Softw.,14:18-32,1988. (Cited on p. 113.)   
[326] Jack Dongarra, Jeremy Du Croz, Sven J. Hammarling,and Richard J. Hanson. An extended set of FORTRAN Basic Linear Algebra Subprograms. ACM Trans. Math. Softw.,14:1-17,1988.(Cited on p. 113.)   
[327] Jack Dongarra, Danny Sorensen,and Sven J. Hammarling.Block reduction of matrices to condensed form for eigenvalue computation. J. Comput. Appl. Math.,27:215-227,1989.(Cited on p. 194.)   
[328] Jack J.Dongarra,Jeremy Du Croz,Iain S.Duff,and S.Hammarling.A set of level 3 basic linear algebra subprograms.ACM Trans. Math. Softw.,16:1-17,1990. (Cited on p. 257.)   
[329] D.L. Donoho. For most large underdetermined systems of linear equations the minimal 1-norm solution is also the sparsest solution. Comm.Pure. Appl. Math., 59:797-829,2006．(Cited on p. 427.)   
[330] Froilan M.Dopico,Plamen Koev,and Juan M. Molera. Implicit standard Jacobi gives high relative accuracy. Numer Math.,113:519-553,2009. (Cited on p. 353.)   
[331] N.R. Draper and H. Smith. Applied Regression Analysis.Wiley,New York,third edition,1998. (Cited on p. 205.)   
[332] Petros Drineas, Michael W. Mahoney,S. Muthukrishnan,and Tamas Sarl6s.Faster least squares approximation. Numer Math.,117:219-249,2011. (Cited on p. 319.)   
[333] Zlatko Drmac. Implementation of Jacobi rotations for accurate singular value computation in floating point arithmetic. SIAM J. Sci. Comput.,18:1200-1222,1997. (Cited on p. 356.)   
[334] Zlatko Drmac. On principal angles between subspaces of Euclidean space.SIAM J. Matrix Anal. Appl.,22:173-194,2000. (Cited on p. 17.)   
[335] Zlatko Drmac.A QR-preconditioned QR SVD method for computing SVD with high accuracy. ACM Trans. Math. Softw.,44:11:1-11:30,2017. (Cited on p. 341.)   
[336] Zlatko Drmac and Kresimir Veselic. New fast and accurate Jacobi SVD algorithm. I. SIAM J. Matrix Anal. Appl.,29:1322-1342,2008. (Cited on p. 356.)   
[337] Zlatko Drmac and Kresimir Veselic. New fast and accurate Jacobi SVD algorithm. II. SIAM J. Matrix Anal. Appl.,29:1343-1362,2008.(Cited on p. 356.)   
[338] A.A. Dubrull. Householder transformations revisited. SIAM J. Matrix Anal. Appl.,22:33-40, 2000. (Cited on p. 51.)   
[339]F. Duchin and Daniel B. Szyld.Application of sparse matrix techniques to inter-regional inputoutput analysis. Econ.Planning,15:147-167,1979. (Cited on p. 206.)   
[340] Iain S.Duf. Pivot selection and row orderings in Givens reduction on sparse matrices. Computig, 13:239-248,1974. (Cited on p. 255.)   
[341] Iain S. Duff. On permutations to block triangular form.J. Inst. Math. Appl.,19:339-342,1977. (Cited on p. 264.)   
[342] Iain S. Duff. On algorithms for obtaining a maximum transversal. ACM Trans. Math. Softw., 7:315-330,1981. (Cited on p. 264.)   
[343] Iain S.Duff Parallel implementation of multifrontal schemes.Parallel Comput., 3:193-204,1986. (Cited on p. 255.)   
[344] Iain S.Duff,A.M. Erisman,and John K. Reid. Direct Methods for Sparse Matrices. Oxford University Press,London,1986.(Cited on pp.185,252.)   
[345] Iain S. Duff,A. M. Erisman,and John K. Reid. Direct Methods for Sparse Matrices. Oxford University Press,London,second edition,2O17.(Cited on p. 244.)   
[346] Iain S.Duf,Roger G. Grimes,and John G.Lewis. Sparse matrix test problems.ACM Trans. Math. Softw.,15:1-14,1989. (Cited on pp.244,265.)   
[347] Iain S. Duff,Michael A. Heroux,and Roldan Pozo.An overview of the sparse basic linear algebra subprograms: The new standard from the BLAS technical forum.ACM Trans. Math. Softw., 28:239-257,2002. (Cited on p. 247.)   
[348] Iain S.Duff and J. Koster. On algorithms for permuting large entries to the diagonal of a sparse matrix. SIAM J.Matrix Anal. Appl.,22:973-996,2001. (Cited on p. 317.)   
[349] Iain S. Duff, M. Marrone, G. Radicati, and C. Vittoli. Level 3 Basic Linear Algebra Subprograms for sparse matrices: A user level interface.ACM Trans. Math. Softw.,23:379-401,1997. (Cited on p. 247.)   
[350] Iain S.Duff and Gerard A. Meurant. The effect of ordering on preconditioned conjugate gradients. BIT Numer. Math.,29:635-657,1989. (Cited on p. 310.)   
[351] Iain S.Dufand John K.Reid.An implementation of Tarjan's algorithm for the block triangularization of a matrix. ACM Trans. Math. Softw.,4:137-147,1978. (Cited on p. 265.)   
[352] Iain S. Duff and John K. Reid. The multifrontal solution of indefinite sparse symmetric linear systems. ACM Trans. Math. Softw., 9:302-325,1983. (Cited on p. 255.)   
[353] A.L.Dulmage and N. S.Mendelsohn. Coverings of bipartite graphs. Canad. J. Math.,10:517-534, 1958.(Cited on p. 263.)   
[354] A.L. Dulmage and N. S. Mendelsohn. A structure theory of bipartite graphs of finite exterior dimension. Trans. Roy. Soc. Canada Sect. II,53:1-13,1959. (Cited on p. 263.)   
[355] A.L. Dulmage and N. S. Mendelsohn. Two algorithms for bipartite graphs. J. Soc. Indust. Appl. Math.,11:183-194,1963. (Cited on p. 263.)   
[356] P.J.Eberlein and Haesun Park.Efcient implementation of Jacobi algorithms and Jacobi sets on distributed memory machines. J. Parallel Distrib. Comput., 8:358-366,1990. (Cited on p. 354.)   
[357] Carl Eckart and Gale Young. The approximation of one matrix by another of lower rank. Psychometrika,1:211-218,1936. (Cited on p. 24.)   
[358] A. Edelman, T.A. Arias,and S.T. Smith. The geometry of algorithms with orthogonality constraints. SIAM J. Matrix Anal. Appl.,20:303-353,1998. (Cited on p.169.)   
[359] Bradley Efron, Trevor Hastie,Iain Johnston, and Robert Tibshirani. Least angle regression. Ann. Statist.,32:407-499,2004. (Cited on p. 425.)   
[360] M. A. Efroymson.Multiple regresson analysis.In Anthony Ralston and Herbert S. Wilf, editors, Mathematical Methods for Digital Computers. Volume I, pages 191-203.Wiley,New York,1960. (Cited on p. 140.)   
[361]E.Egervary.Onrank-diminishing operators and their applications to thesolutionof linear equations. Z. Angew. Math. Phys.,11:376-386,1960. (Cited on p. 139.)   
[362] Stanley C.Eisenstat, M. C. Gursky,Martin H. Schultz,and Andrew H. Sherman. The Yale sparse matrix package,1. The symmetric code. Internat J. Numer. Methods Engrg.,18:1145-1151,1982. (Cited on p. 258.)   
[363]Hakan Ekblom. Calculation of linear best $l _ { p }$ -approximation.BITNumer Math.,13:292-300,1973. (Cited on p. 425.)   
[364] Hakan Ekblom．A new algorithm for the Huber estimator in linear models.BIT Numer Math., 28:123-132,1988. (Cited on p. 425.)   
[365] Hakan Ekblom and Kaj Madsen. Algorithms for nonlinear Huber estimation. BIT Numer. Math., 29:60-76,1989. (Cited on p. 425.)   
[366] Lars Elden. Stepwise Regression Analysis with Orthogonal Transformations.Tech. Report LiTH-MAT-R-1972-2, Department of Mathematics, Linkoping University,Sweden,1972.(Cited on p. 140.)   
[367] Lars Elden.Algorithms for the regularization of il-conditioned least squares problems.BITNumer. Math.,17:134-145,1977. (Cited on pp.170,171,180.)   
[368] Lars Elden. Perturbation theory for the least squares problem with linear equality constraints. SIAM J. Numer. Anal.,17:338-350,1980. (Cited on p. 158.)   
[369] Lars Eldén.A weighted pseudoinverse,generalized singular values,and constrained least squares problems.BIT Numer Math.,22:487-502,1982.(Cited on pp.158,158,159,181.)   
[370]Lars Elden.An efficient algorithm for the regularization of il-conditioned least squares problems with triangular Toeplitz matrix.SIAM J. Sci. Statist.Comput.,5:229-236,1984. (Cited on pp.176, 241.)   
[371] Lars Elden.A note on the computation of the generalized cross-validation function for ilconditioned least squares problems. BITNumer Math.,24:467-472,1984.(Cited on p. 179.)   
[372] Lars Elden. Algorithms for the computation of functionals defined on the solution of a discrete ill-posed problem.BIT Numer Math.,30:466-483,1990.(Cited on p. 29.)   
[373] Lars Elden.Numerical solution of the sideways heat equation. In H.W.Engl and W.Rundell, editors,Inverse Problems in Diffusion Processes,pages 130-150.SIAM,Philadelphia,PA,1995. (Cited on p. 173.)   
[374] Lars Elden. Solving quadratically constrained least squares problems using a differential-geometric approach.BIT Numer: Math.,42:323-335,2002.(Cited on p.169.)   
[375] Lars Elden. Partial least-squares vs.Lanczos bidiagonalization—I: Analysis of a projection method for multiple regression. Comput. Statist. Data Anal., 46:11-31,2004. (Cited on p. 201.)   
[376] Lars Elden. Matrix Methods in Data Mining and Patern Recognition. Fundamentals of Algorithms. SIAM,Philadelphia,second edition,2O19.(Cited on p.216.)   
[377] Lars Elden and Salman Ahmadi-Asl. Solving bilinear tensor least squares problems and application to Hammerstein identification. Numer Linear Algebra Appl., 26:e2226,2019. (Cited on p. 406.)   
[378] L. Elden and H. Park.Block downdating of least squares solutions.SIAM J. Matrix Anal. Appl., 15:1018-1034,1994. (Cited on p. 148.)   
[379] Lars Elden and Haesun Park. A Procrustes problem on the Stiefel manifold. Numer Math,82:599- 619,1999. (Cited on p. 387.)   
[380] Lars Elden and Berkant Savas.A Newton-Grassman method for computing the best multilinear rank- $( r _ { 1 } , r _ { 2 } , r _ { 3 } )$ approximation of a tensor. SIAM J. Matrix Anal. Appl.,31:248-271,2009. (Cited on pp. 215,217.)   
[381] Lars Elden and Valeria Simoncini. Inexact Rayleigh quotient-type methods for eigenvalue computations.BIT Numer Math..,42:159-182,2002.(Cited on p. 375.)   
[382] Lars Elden and Valeria Simoncini. Solving il-posed linear systems with GMRES and a singular preconditioner. SIAM J. Matrix Anal. Appl.,33:1369-1394,2012. (Cited on p. 334.)   
[383] T.Elfving. Block-iterative methods for consistent and inconsistent linear equations. Numer. Math., 35:1-12,1980.(Cited on p. 308.)   
[384] Tommy Elfving and Ingegerd Skoglund. A direct method for a regularized least-squares problem. Numer: Linear Algebra Appl.,16:649-675,2009. (Cited on p. 259.)   
[385] Erik Elmroth and Fred G. Gustavson. Applying recursion to serial and parallel QR factorization leads to better performance. IBM J. Res. Develop.,44:605-624,2004.(Cited on p. 112.)   
[386] Heinz W. Engl, Martin Hanke,and Andreas Neubauer. Regularization of Inverse Problems.Dordrecht, The Netherlands. Kluwer Academic Pres,1996. (Cited on p. 182.)   
[387] Jerry Eriksson. Quasi-Newton methods for nonlinear least squares focusing on curvature. BIT Numer: Math.,39:228-254,1999. (Cited on p. 400.)   
[388] Jerry Eriksson,Per-Ake Wedin,Märten E.Gulliksson,and Inge Soderkvist.Regularization methods for uniformly rank-deficient nonlinear least squares methods.J. Optim. Theory Appl.,127:1-26, 2005. (Cited on p. 397.)   
[389] D.J. Evans. The use of pre-conditioning in iterative methods for solving linear systems with symmetric positive definite matrices. J. Inst. Math. Appl., 4:295-314,1968. (Cited on p. 306.)   
[390] Nicolaas M.Faber and Joan Ferré.On the numerical stability of two widely used PLS algorithms. J. Chemom.,22:101-105,2008. (Cited on p. 203.)   
[391] D.K.Faddeev, V.N. Kublanovskaya,and V.N.Faddeeva. Solution of linear algebraic systems with rectangular matrices.Proc. Steklov Inst. Math., 96:93-111,1968. (Cited on p. 76.)   
[392] D.K. Faddeev, V.N. Kublanovskaya,and V.N. Faddeeva. Sur les systemes lineaires algebriques de matrices rectangularies et malconditionees. In Programmation en Mathematiques Numériques, pages 161-170.Editions Centre Nat. Recherche Sci., Paris VII,1968.(Cited on p. 343.)   
[393] Shaun M.Fallat. Bidiagonal factorizations of totally nonnegative matrices.Amer Math. Monthly, 108:697-212,2001. (Cited on p. 239.)   
[394] Ky Fan. On a theorem by Weyl concerning the eigenvalues of linear transformations. Proc. Nat. Acad. Sci. USA,35:652-655,1949. (Cited on p. 22.)   
[395] KyFan and Alan J.Hoffman. Some metric inequalities in the space of matrices.Proc. Amer Math. Soc.,6:111-116,1955. (Cited on p. 383.)   
[396] R. W. Farebrother. Linear Least Squares Computations. Marcel Dekker, New York,1988.(Cited on p. 64.)   
[397] Richard W. Farebrother. Fitting Linear Relationships.A History of the Calculus of Observations 1750-1900. Springer Series in Statistics. Springer,Berlin,1999.(Cited on pp.2,139.)   
[398] Dario Fasino and Antonio Fazzi. A Gauss-Newton iteration for total least squares problems.BIT Numer Math.,58:281-299,2018. (Cited on p. 224.)   
[399] Donald W. Fausett and Charles T. Fulton. Large least squares problems involving Kronecker products.SIAM J. Matrix Anal. Appl.,15:219-227,1994. (Cited on p. 209.)   
[400] M.Fazel.Matrix Rank Minimization with Applications.Ph.D.thesis,Stanford University,Stanford, CA,2002. (Cited on p. 429.)   
[401] K. Vince Fernando.Linear convergence of the row cyclic Jacobi and Kogbetliantz methods.Numer. Math.,56:73-91,1989. (Cited on pp.357,357.)   
[402] K. V. Fernando. Accurately counting singular values of bidiagonal matrices and eigenvalues of skew-symmetric tridiagonal matrices. SIAM J. Matrix Anal. Appl.,20:2:373-399,1998. (Cited on pp.350,351.)   
[403]K. Vince Fernando and Beresford N.Parlett. Accurate singular values and differential qd algorithms.Numer Math.,67:191-229,1994. (Cited on pp.343,351,352.)   
[404] R.D. Fierro, G.H. Golub,P.C. Hansen,and D. P. O'Leary. Regularization by truncated total least squares. SIAM J. Sci. Comput.,18:1223-1241,1997. (Cited on pp. 225, 335.)   
[405] Ricardo D.Fierro and James R. Bunch. Collinearity and total least squares.SIAM J. Matrix Anal. Appl.,15:1167-1181,1994. (Cited on p. 225.)   
[406] Ricardo D.Fierro and James R.Bunch. Perturbation theory for orthogonal projection methods with applications to least squares and total least squares. Linear Algebra Appl.,234:71-96,1996. (Cited on p. 225.)   
[407] Ricardo D.Fierro and Per Christian Hansen. UTV Expansion Pack: Special-purpose rank-revealing algorithms. Numer. Algorithms,40:47-66,2005. (Cited on p. 155.)   
[408] Ricardo D.Fierro,Per Christian Hansen,and Peter Spren Kirk Hansen.UTV Tools: MATLAB templates for rank-revealing UTV decompositions.Numer. Algorithms,20:165-194,1999.(Cited on p. 155.)   
[409] B.Fischer, A. Ramage,D.J. Silvester, and A. J. Wathen. Minimum residual methods for augmented systems.BIT Numer. Math.,38:527-543,1998.(Cited on pp.300,330.)   
[410] Roger Fletcher. Generalized inverse methods for the best least squares solution of systems of nonlinear equations. Comput. J.,10:392-399,1968. (Cited on p. 395.)   
[411] Roger Fletcher. A Modified Marquardt Subroutine for Nonlinear Least Squares. Tech. Report R6799,Atomic Energy Research Establishment,Harwell, UK,1971. (Cited on p. 396.)   
[412] RogerFletcher. Practical Methods of Optimization.Wiley, New York,second edition,20oo.(Cited on p. 402.)   
[413] Roger Fletcher and C.Xu. Hybrid methods for nonlinear least squares. IMA J. Numer. Anal., 7:371-389,1987. (Cited on p. 400.)   
[414] Diederik R.Fokkema, Gerard L.G. Sleijpen,and Henk A.van der Vorst.Accelerated inexact Newton schemes for large systems of nonlinear equations. SIAM J. Sci. Comput.，19:657-674, 1998.(Cited on p. 402.)   
[415] Diederik R.Fokkema,Gerard L.G. Sleijpen,and Henk A.van der Vorst.Jacobi-Davidson style QR and QZ algorithms for the reduction of matrix pencils. SIAM J. Sci. Comput.,20:94-125,1998. (Cited on p. 375.)   
[416] David Chin-Lung Fong. Minimum-Residual Methods for Sparse Least-Squares Using Golub-Kahan Bidiagonalization.Ph.D.thesis,Stanford University,Stanford,CA,2O11. (Cited on p.294.)   
[417] David Chin-Lung Fong and Michael Saunders.LSMR: An iterative algorithm for sparse leastsquares problems. SIAM J. Sci. Comput.,33:2950-2971,2011．(Cited on pp.292，294,297, 298.)   
[418] A. B. Forbes. Least-Squares Best-Fit Geometric Elements. Tech. Report NPL DITC 140/89, National Physical Laboratory, Teddington, UK,1989.(Cited on p. 414.)   
[419] A. B.Forbes. Robust Circle and Sphere Fiting by Least Squares. Tech. Report NPL DITC 153/89, National Physical Laboratory, Teddington,UK,1989.(Cited on p. 414.)   
[420] Anders Forsgren.On linear least-squares problems with diagonally dominant weight matrices. SIAM J. Matrix Anal. Appl.,17:763-788,1996. (Cited on p.132.)   
[421] Anders Forsgren,Philip E. Gill,and Margaret H. Wright. Interior methods for nonlinear optimization. SIAM Rev.,44:525-597,2002. (Cited on p. 419.)   
[422] George E.Forsythe. Generation and use of orthogonal polynomials for data-fiting with a digital computer.J. Soc.Indust. Appl. Math.,5:74-88,1957． (Cited on p.237.)   
[423] George E.Forsythe and Peter Henrici.The cyclic Jacobi method for computing the principal values of a complex matrix. Trans. Amer Math. Soc., 94:1-23,1960. (Cited on p. 354.)   
[424] Leslie Foster. Rank and null space calculations using matrix decomposition without column interchanges. Linear Algebra Appl.,74:47-71,1986. (Cited on pp. 82, 261.)   
[425] Leslie Foster. The growth factor and efficiency of Gaussian elimination with rook pivoting.J. Comp. Appl. Math.,86:177-194,1997. (Cited on p. 86.)   
[426] Leslie Foster and Rajesh Kommu.Algorithm 853.An efficient algorithm for solving rank-deficient least squares problems. ACM Trans. Math. Softw.,32:157-165,2006. (Cited on p. 79.)   
[427]Leslie V.Foster. Modifications of the normal equations method that are numerically stable.In Gene H. Golub and P. Van Dooren, editors, Numerical Linear Algebra, Digital Signal Processing and Parallel Algorithms,NATO ASI Series,pages 501-512. Springer-Verlag,Berlin,1991.(Cited on p. 204.)   
[428] Leslie V. Foster. Solving rank-deficient and ill-posed problems using UTV and QR factorizations. SIAM J. Matrix Anal. Appl.,25:582-600,2003. (Cited on p. 79.)   
[429] Leslie Fox.An Introduction to Numerical Linear Algebra. Clarendon Press,Oxford,1964. xi+328 pp. (Cited on p. 314.)   
[430] C. Fraley. Computational behavior of Gauss-Newton methods. SIAM J. Sci. Statist. Comput., 10:515-532,1989. (Cited on p. 394.)   
[431] John G.F. Francis. The QR transformation: A unitary analogue to the LR transformation.I. Computer J.,4:265-271,1961. (Cited on p. 344.)   
[432] John G.F. Francis. The QR transformation. II. Computer J.,4:332-345,1961. (Cited on p. 344.)   
[433] Roland W.Freund. A note on two block SOR methods for sparse least squares problems. Linear Algebra Appl.,88/89:211-221,1987. (Cited on p. 316.)   
[434] M. P.Friedlander and Dominique Orban.A primal-dual regularized interior-point method for convex quadratic programs. Math. Prog. Comput., 4:71-107,2012. (Cited on p. 331.)   
[435] Takeshi Fukaya, Ramaseshan Kannan, Yuji Nakatsukasa, Yasaku Yamamoto,and Yuka Yanagi-sawa. Shifted Cholesky QR for computing the QR factorization of ill-conditioned matrices. SIAM J. Sci. Comput., 42:A477-A503,2020. (Cited on p. 213.)   
[436] Martin J. Gander and Gerhard Wanner. From Euler,Ritz,and Galerkin to modern computing. SIAM Rev.,54:627-666,2012. (Cited on p. 375.)   
[437] Walter Gander. Algorithms for the QR-Decomposition. Research Report 80-O2, Seminar fur Angewandte Mathematik,ETHZ, Zurich, Switzerland,1980.(Cited on pp. 62, 62,70.)   
[438] Walter Gander. Least squares with a quadratic constraint. Numer Math.,36:291-307,1981.(Cited on p. 168.)   
[439] Walter Gander, Gene H. Golub,and Rolf Strebel. Least squares fiting of circles and ellpses. BIT Numer: Math.,34:558-578,1994. (Cited on p. 416.)   
[440] Walter Gander and Urs von Matt. Some least squares problems. In W. Gander and J. Hrbicek, edi-tors,Solving Problems inScientific Computing Using Mapleand MATLAB,pages 83-102.Springer-Verlag,Berlin,third edition,1997. (Cited on p. 411.)   
[441] B. S. Garbow, J. M. Boyle, Jack J. Dongarra, and G.W. Stewart. Matrix Eigensystems Routines: EISPACKGuide Extension,volume 51 of Lecture Notes in Computer Science. Springer,New York, 1977. (Cited on p. 113.)   
[442] A. de la Garza. An Iterative Method for Solving Systems of Linear Equations. Report K-731, Oak Ridge Gaseous Difusion Plant, Oak Ridge, TN,1951.(Cited on p. 273.)   
[443] André Gaul, Martin H. Gutknecht, Jorg Liesen,and Reinhard Nabben.A framework for deflated and augmented Krylov subspace methods. SIAM J. Matrix Anal. Appl.,34:495-518,2013. (Cited on p. 337.)   
[444] C.F. Gauss. Theory ofthe Motion of the Heavenly Bodies Moving about the Sun in Conic Sections, C.H. Davis,translator,Dover,New York,1963.First published in 1809.(Cited on p. 2.)   
[445] Carl Friedrich Gauss. Theoria combinationis observationum eroribus minimis obnoxiae, pars prior. In Werke, IV, pages 1-26. Koniglichen Gesellschaft der Wissenschaften zu Gottingen,1880. First published in 1821. (Cited on p. 3.)   
[446] Carl Friedrich Gauss. Theoria combinationis observationum erroribus minimis obnoxiae, pars posterior.In Werke,IV, pages 27-53. Koniglichen Gesellschaft der Wissenschaften zu Gottingen, 1880.First published in 1823．(Cited on p. 3.)   
[447] Carl Friedrich Gauss.Theory of the Combination of Observations Least Subject to Erors.Part 1, Part 2, Supplement, G.W. Stewart, Translator, volume 11 of Classcs in Applied Math.， SIAM, Philadelphia,1995.(Cited on p. 3.)   
[448] Silvia Gazzola, Per Christian Hansen,and James G. Nagy. IR Tools: A MATLAB package of iterative regularization methods and large-scale test problems. Numer: Algorithms,81:773-811, 2018.(Cited on p. 335.)   
[449] Silvia Gazzola, Paolo Novati,and Maria Rosario Russo.On Krylov projection methods and Tikhonov regularization. ETNA,44:83-123,2015. (Cited on p. 335.)   
[450] W. Morven Gentleman.Least squares computations by Givens transformations without square roots.J. Inst. Math. Appl.,12:329-336,1973. (Cited on pp.50,255.)   
[451] W. Morven Gentleman. Error analysis of QR decompositions by Givens transformations. Linear Algebra Appl.,10:189-197,1975.(Cited on p.56.)   
[452] W. Morven Gentleman. Row elimination for solving sparse linear systems and least squares problems. In G. A. Watson, editor,Proceedings of the Dundee Conference on Numerical Analysis 1975,volume 506 of Lecture Notes in Mathematics, pages 122-133.Springer-Verlag, Berlin,1976. (Cited on p. 254.)   
[453] Alan George. Computer Implementation of the Finite-Element Method.Ph.D.thesis, Stanford University, CA,1971. (Cited on p. 251.)   
[454] Alan George, John R. Gilbert,and Joseph W. H. Liu, editors. Graph Theory and Sparse Matrix Computation, volume 56 of The IMA Volumes in Mathematics and Applications. Springer,1993. (Cited on p. 244.)   
[455] Alan George and Michael T. Heath. Solution of sparse linear least squares problems using Givens rotations.Linear Algebra Appl.,34:69-83,1980. (Cited on pp. 253,254.)   
[456] Alan George, Kh. D. Ikramov, and A. B. Kucherov. Some properties of symmetric quasi-definite matrices. SIAM J. Matrix Anal. Appl.,21:1318-1323,2000. (Cited on p. 329.)   
[457] Alan George and Joseph W.H.Liu. Computer Solution of Large Sparse Positive Definite Systems. Prentice-Hall, Englewood Cliffs,NJ,1981. (Cited on pp.244,245,251,256.)   
[458] Alan George and Joseph W. H. Liu. Householder reflections versus Givens rotations in sparse orthogonal decomposition. Linear Algebra Appl.,88/89:223-238,1987. (Cited on p. 256.)   
[459] Alan George and Joseph W.H. Liu. The evolution of the minimum degree ordering algorithm. SIAM Rev.,31:1-19,1989. (Cited on p.252.)   
[460] Alan George and Esmond Ng. On row and column orderings for sparse least squares problems. SIAM J. Numer. Anal.,20:326-344,1983. (Cited on pp.255,256.)   
[461] Alan George and Esmond G.Ng. On the complexity of sparse QR and LU factorization of finiteelement matrices. SIAM J. Sci. Statist. Comput.,9:849-861,1988. (Cited on p.258.)   
[462] Alan George, William G.Poole,Jr.,and Robert G. Voigt. Incomplete nested dissection for solving $_ n$ by $n$ grid problems. SIAM J. Numer: Anal.,15:662-673,1978. (Cited on p. 256.)   
[463] J. A. George and E. G. Ng. SPARSPAK: Waterloo Sparse Matrix Package User's Guide for SPARSPAK-B. Res. Report CS-84-37, Department of Computer Science, University of Waterloo, Canada,1984. (Cited on p. 258.)   
[464] J. A. George, M. T. Heath, and R. J. Plemmons. Solution of large-scale sparse least squares problems using auxiliary storage. SIAM J. Sci. Statist. Comput., 2:416-429,1981. (Cited on p. 256.)   
[465] J. Alan George, Joseph W. H. Liu, and Esmond G. Ng. Row-ordering schemes for sparse Givens transformations I. Bipartite graph model. Linear Algebra Appl., 61:55-81,1984. (Cited on p. 253.)   
[466] Tomas Gergelits and Zdenek Strakos. Composite convergence bounds based on Chebyshev polynomials and finite precision conjugate gradient computations. Numer Algorithms, 65:759-782, 2014. (Cited on p. 299.)   
[467] Norman E.Gibbs,William G.Poole,Jr.,and Paul K. Stockmeyer. An algorithm for reducing the bandwidth and profile of a sparse matrix. SIAM J. Numer. Anal.,13:236-250,1976.(Cited on p. 251.)   
[468] John R. Gilbert, Xiaoye S.Li, Esmond G.Ng,and Barry W. Peyton. Computing row and column counts for sparse QR and LU factorization. BIT Numer: Math.，41:693-710, 2001.(Cited on p. 255.)   
[469] John R. Gilbert, Cleve Moler, and Robert Schreiber. Sparse matrices in MATLAB: Design and implementation. SIAM J. Matrix Anal. Appl.,13:333-356,1992. (Cited on pp. 250,258.)   
[470] John R. Gilbert, Esmond $\mathrm { N g }$ ，and B. W. Peyton. Separators and structure prediction in sparse orthogonal factorization. Linear Algebra Appl.,262:83-97,1997. (Cited on p. 105.)   
[471] M. B. Giles and E. Suli. Adjoint methods for PDEs: A posteriori error analysis and postprocessing by duality. Acta Numer.,11:145-236,2002. (Cited on p. 304.)   
[472] Philip E. Gil, Gene H. Golub, Walter Murray,and Michael A. Saunders.Methods for modifying matrix factorizations. Math. Comp.,28:505-535,1974. (Cited on p. 139.)   
[473] Philip E. Gill,Sven J. Hammarling, Walter Murry, Michael A. Saunders,and Margaret H. Wright. User's Guide for LSSOL (Version 1.0): A Fortran Package for Constrained Linear Least-Squares and Convex Quadratic Programming.Report SOL, Department of Operations Research, Stanford University, CA,1986. (Cited on p.165.)   
[474] Philip E. Gill and Walter Murray. Algorithms for the solution of the nonlinear least-squares problem. SIAM J. Numer Anal.,15:977-992,1978. (Cited on p. 399.)   
[475] Philip E. Gill, Walter Murray,and Michael A. Saunders. SNOPT: An SQP algorithm for large-scale constrained optimization. SIAM Rev.,47:99-131,2005.(Cited on p. 318.)   
[476] Philip E. Gill, Walter Murray, and Margaret H. Wright. Practical Optimization. Academic Press, London, UK,1981. (Cited on pp.395,402.)   
[477] Philip E.Gill,Michael A. Saunders,and Joseph R.Shinnerl.On the stabilityof Cholesky factorization for symmetric quasi-definite systems. SIAM J. Matrix Anal. Appl.,17:35-46,1996.(Cited on p. 329.)   
[478] Luc Giraud, Serge Gratton, and Julien Langou. A rank $k$ update procedure for reorthogonalizing the orthogonal factor from modified Gram-Schmidt. SIAM J. Matrix Anal. Appl.,25:1163-1177, 2004. (Cited on p. 71.)   
[479] Luc Giraud and Julien Langou. When modified Gram-Schmidt generates a well-conditioned set of vectors. IMA J. Numer. Anal.,22:4:521-528,2002. (Cited on p. 70.)   
[480] Wallace Givens. Computation of plane unitary rotations transforming a general matrix to triangular form. J. Soc. Indust. Appl. Math., 6:26-50,1958. (Cited on pp. 47, 51.)   
[481] J. Gluchowska and Alicja Smoktunowicz. Solving the linear least squares problem with very high relative accuracy. Computing,45:345-354,1990. (Cited on p.104.)   
[482] Sergei K. Godunov. Problem of the dichotomy of the spectrum of a matrix. Siberian Math. J., 27:649-660,1986. (Cited on p. 382.)   
[483] Israel Gohberg,Peter Lancaster,and Leiba Rodman. Indefinite Linear Algebra and Applications. Birkhäuser, Boston,2005.(Cited on p.137.)   
[484] Herman H. Goldstine. A History of Numerical Analysis from the 16th through the 19th Century. Stud. Hist. Math. Phys.Sci. Vol.2. Springer-Verlag,New York,1977.(Cited on p. 2.)   
[485] G. H. Golub and Peter Businger. Least Squares, Singular Values and Matrix Approximations; an ALGOL Procedure for Computing the Singular Value Decomposition. Tech. Report CS-73, Computer Science Department, Stanford University,CA,1967.(Cited on p. 349.)   
[486] G. H. Golub and C. F. Van Loan. Unsymmetric positive definite linear systems. Linear Algebra Appl.,28:85-97,1979. (Cited on p. 329.)   
[487] Gene H. Golub. Numerical methods for solving least squares problems. Numer: Math.,7:206-216, 1965.(Cited on pp.56,75,169,177.)   
[488] Gene H. Golub. Least squares, singular values and matrix approximations. Apl. Mat.,13:44-51, 1968. (Cited on p. 348.)   
[489] Gene H. Golub. Matrix decompositions and statistical computing. In Roy C.Milton and John A. Nelder,editors,Statistical Computation, pages 365-397.Academic Press,New York,1969. (Cited on p. 137.)   
[490] Gene H.Golub. Some modified matrix eigenvalue problems. SIAMRev.,15:318-334,1973.(Cited on p. 360.)   
[491] Gene H. Golub and Chen Greif. On solving block-structured indefinite linear systems. SIAM J. Sci. Comput.,24:2076-2092,2003. (Cited on p. 117.)   
[492] Gene H. Golub,Per Christian Hansen,and Dianne P.O'Leary. Tikhonov regularization and total least squares. SIAM J. Matrix Anal. Appl.,21:185-194,1999. (Cited on p. 225.)   
[493] Gene H. Golub,Micheal T.Heath,and Grace Wahba. Generalized cross-validation as a method for choosing a good ridge parameter. Technometrics,21:215-223,1979. (Cited on p. 178.)   
[494] Gene H. Golub, Alan Hoffman,and G. W. Stewart. A generalization of the Eckart-Young matrix approximation theorem. Linear Algebra Appl.,88/89:317-327,1987. (Cited on p. 24.)   
[495] Gene H. Golub and William Kahan. Calculating the singular values and pseudo-inverse of a matrix. SIAM J. Numer Anal.,2:205-224,1965. (Cited on pp. 191, 196, 342.)   
[496] Gene H. Golub, Virginia Klema,and G. W. Stewart. Rank Degeneracy and Least Squares Problems. Tech.Report STAN-CS-76-559, Computer Science Department, Stanford University, Stanford, CA, 1976. (Cited on p. 80.)   
[497] Gene H. Golub and Randall J.LeVeque. Extensions and uses of the variable projection algorithm for solving nonlinear least squares problems. In Proceedings of the 1979 Army Numerical Analysis and Computers Conf.,ARO Report 79-3, pages 1-12. White Sands Missile Range, White Sands, NM,1979. (Cited on p. 405.)   
[498] Gene H. Golub,Franklin T.Luk,and Michael L. Overton. A block Lanczos method for computing the singular values and corresponding singular vectors of a matrix. ACM Trans. Math. Softw., 7:149-169,1981. (Cited on pp.193,376.)   
[499] Gene H. Golub,Franklin T.Luk, and M. Pagano. A sparse least squares problem in photogrammetry. In J. F. Gentleman, editor,Proceedings of the Computer Science and Statistics: 12th Annual Symposium on the Interface,pages 26-30. University of Waterloo, Ontario, Canada,1979. (Cited on pp.206,208.)   
[500] Gene H. Golub,P.Manneback,and Ph.L.Toint.A comparison between some direct and iterative methods for large scale geodetic least squares problems. SIAM J. Sci. Statist. Comput., 7:799-816, 1986.(Cited on pp.209,308,309.)   
[501] Gene H. Golub and Gerard Meurant. Matrices, moments and quadrature. In D.F. Grifths and G. A. Watson,editors,Numerical Analysis 1993: Proceedings of the 13th Dundee Biennial Conference, volume 228 of Pitman Research Notes Math., pages 105-156.Longman Scientific and Technical, Harlow, UK,1994. (Cited on p. 289.)   
[502] Gene H. Golub and Dianne P. O'Leary. Some history of the conjugate gradient and Lanczos algorithms: 1948-1976. SIAM Review,31:50-102,1989. (Cited on p. 285.)   
[503]Gene H. Golub and Victor Pereyra.The differentiation of pseudo-inverses and nonlinear least squares problems whose variables separate. SIAM J. Numer. Anal.,10:413-432,1973. (Cited on pp.26,402,403.)   
[504] Gene H. Golub and Victor Pereyra. Separable nonlinear least squares: The variable projection method and its application.Inverse Problems,19:R1-R26,2003.(Cited on p.405.)   
[505] Gene H. Golub and R. J. Plemmons.Large-scale geodetic least-squares adjustment by dissection and orthogonal decomposition. Linear Algebra Appl.,34:3-28,1980.(Cited on pp.187，206, 209.）   
[506] Gene H. Golub,Robert J. Plemmons,and Ahmed H. Sameh.Paralel block schemes for largescale least-squares computations.In High-Speed Computing, Scientific Applications and Algorithm Design, pages 171-179. University of Ilinois Press,1988. (Cited on p. 208.)   
[507] Gene H. Golub and C. Reinsch. Singular value decomposition and least squares solutions.In F.L. Bauer et al.,editors,Handbook for Automatic Computation. Vol. I, Linear Algebra, pages 134-151. Springer, New York,1971. Prepublished in Numer: Math.,14:403-420,1970. (Cited on pp.11, 349.)   
[508] Gene H. Golub,Knut Splna,and Paul Van Dooren. Computing the SVD of a general matrix product/quotient. SIAM J. Matrix Anal. Appl.,22:1-19,2000. (Cited on p. 127.)   
[509] Gene H. Golub, Martin Stoll,and Andy Wathen.Approximation of the scatering amplitude and linear systems.ETNA,31:178-203,2008.(Cited on p. 304.)   
[510] Gene H. Golub and Frank Uhlig. The QR algorithm: 5O years later its genesis by John Francis and Vera Kublanovskaya and subsequent developments. IMA J. Numer Anal.,29:467-485,2009. (Cited on p. 348.)   
[511] Gene H. Golub and Charles F. Van Loan. An analysis of the total least squares problem. SIAM J. Numer Anal.,17:883-893,1980.(Cited on pp.218, 220.)   
[512] Gene H. Golub and Charles F. Van Loan. Matrix Computations.Johns Hopkins University Press, Baltimore,MD,third edition,1996.(Cited on pp.17,80,157,179,355,368.)   
[513] Gene H. Golub and Richard S.Varga.Chebyshev semi-iteration and second-order Richardson iterative methods. Parts Iand II. Numer Math.,3:147-168,1961. (Cited on p. 277.)   
[514] Gene H. Golub and James H. Wilkinson. Note on the iterative refinement of least squares solutions. Numer: Math.,9:139-148,1966. (Cited on p. 27.)   
[515] Gene H. Golub and Hongyuan Zha. Perturbation analysis of the canonical correlation of matrix pairs. Linear Algebra Appl.,210:3-28,1994. (Cited on p. 17.)   
[516] Gene H. Golub and Hongyuan Zha. The canonical correlations of matrix pairs and their numerical computation. In A. Bojanczyk and G. Cybenko,editors, Linear Algebra for Signal Processing, volume 9 ofThe IMA Volumes in Mathematicsand ItsApplications,pages27-49.Springer-Verlag, 1995. (Cited on p. 17.)   
[517]Dan Gordon and Rachel Gordon.CGMN revisited: Robust and efcient solution of stiff linear systems derived from elliptic partial differential equations. ACM Trans.Math. Softw.，35:18:1- 18:27,2008. (Cited on p. 275.)   
[518] Rachel Gordon,R. Bender,and Gabor T. Herman. Algebraic reconstruction techniques (ART) for three-dimensional electron microscopy and X-ray photography. J. Theor: Biology,29:471-481, 1970. (Cited on p. 274.)   
[519] S. A. Goreinov,E.E. Tyrtyshnikov, and N.L. Zamarashkin. A theory of pseudo-skeleton approximations. Linear Algebra Appl.,261:1-21,1997. (Cited on p. 90.)   
[520] Nicholas I. M. Gould and Jennifer A. Scott. The state-of-the-art of preconditioners for sparse leastsquares problems. ACM Trans. Math. Softw.,43:36-1-36-35,2017. (Cited on pp.297,306.)   
[521] John C. Gower and Garmt B.Dijksterhuis. Procrustes Problems. Oxford University Press, Oxford, UK,2004. (Cited on p. 387.)   
[522] William B. Gragg, Randall J. LeVeque, and John A. Trangenstein. Numerically stable methods for updating regressions. J. Amer: Statist. Org.,74:161-168,1979. (Cited on p. 140.)   
[523] Wiliam H. Gragg and W. J. Harrod. The numerically stable reconstruction of Jacobi matrices from spectral data. Numer Math.,44:317-335,1984. (Cited on pp.230, 239.)   
[524] S.L. Graham, M. Snir,and C.A.Paterson, editors. Getting up to Speed. The Future of Supercomputing. The National Academies Press,Washington,DC,2OO4.(Cited on p. 114.)   
[525] Jprgen. P. Gram. Ueber die Entwickelung reeller Functionen in Reihen mitelst der Methode der kleinsten Quadrate. J. Reine Angew. Math.,94:41-73,1883. (Cited on p. 63.)   
[526] S. Gratton, A. S.Lawless,and N. K. Nichols. Approximate Gauss-Newton methods for nonlinear least squares problems. SIAM J. Optim.,18:106-132,2007. (Cited on pp. 401,401.)   
[527] Serge Gratton. On the condition number of the least squares problem in a weighted Frobenius norm. BIT Numer Math.,36:523-530,1996. (Cited on p. 31.)   
[528] Serge Gratton,Pavel Jiranek,and David Titley-Peloquin. On the accuracy of the Karlson-Walden estimate of the backward error for linear least squares problems. SIAM J. Matrix Anal. Appl., 33:822-836,2012. (Cited on p. 99.)   
[529] Serge Gratton,David Titley-Peloquin, and Jean Tshimanga Ilunga. Sensitivity and conditioning of the truncated total least squares solution. SIAM J. Matrix Anal. Appl.,34:1257-1276,2013. (Cited on p. 226.)   
[530] Joseph F. Grcar. Matrix Stretching for Linear Equations. Tech. Report SAND 90-8723, Sandia National Laboratories,Albuquerque, NM,199o.(Cited on p. 263.)   
[531] Joseph F. Grcar. Spectral condition numbers of orthogonal projections and full rank linear least squares residuals. SIAM J. Matrix Anal. Appl.,31:2934-2949,2010. (Cited on p. 31.)   
[532] Joseph F. Grcar, Michael A.Saunders,and Z. Su. Estimates of Optimal Backward Perturbations for Linear Least Squares Problems. Tech. Report SOL 2O07-1, Department of Management Science and Engineering, Stanford University, Stanford, CA, 2O07. (Cited on pp.99,299.)   
[533] Anne Greenbaum.Behavior of slightly perturbed Lanczos and conjugate-gradient recurrences. Linear Algebra Appl.,113:7-63,1989. (Cited on p. 295.)   
[534] Anne Greenbaum. Iterative Methods for Solving Linear Systems,volume 17of Frontiers in Applied Mathematics. SIAM, Philadelphia,1997. (Cited on pp.269,285,294.)   
[535] Anne Greenbaum,Miroslav Rozloznik,and Zdenek Strakos.Numerical behavior of the modified Gram-Schmidt GMRES process and related algorithms.BIT Numer. Math.,37:706-719,1997. (Cited on p. 302.)   
[536] T.N.E. Greville. Note on the generalized inverse of a matrix product. SIAMRev.,8:518-521,1966. (Cited on p. 15.)   
[537] T.N.E. Greville. Solutions of the matrix equation $X A X = X$ ,and relations between oblique and orthogonal projectors. SIAM J. Appl. Math.,26:828-832,1974. (Cited on p.119.)   
[538] Roger G. Grimes, John G.Lewis,and Horst D. Simon.A shifted block Lanczos algorithm for solving sparse symmetric generalized eigenproblems. SIAM J. Matrix Anal. Appl.,15:228-272, 1994. (Cited on p. 375.)   
[539] C.W. Groetsch.The Theory of Tikhonov Regularization for Fredholm Integral Equations of the First Kind.Pitman,Boston,MA,1984.(Cited on pp.171,177.)   
[540] Eric Grosse. Tensor spline approximations.Linear Algebra Appl.,34:29-41,1980.(Cited on p. 209.)   
[541] Benedikt GroBer and Bruno Lang. Eficient parallelreductionto bidiagonal form. Parallel Comput., 25:969-986,1999. (Cited on p. 348.)   
[542] Benedikt GroBer and Bruno Lang. An $O ( n ^ { 2 } )$ algorithm for the bidiagonal SVD. Linear Algebra Appl.,358:45-70,2003. (Cited on p. 352.)   
[543] Benedikt Grosser and Bruno Lang. On symmetric eigenproblems induced by the bidiagonal SVD. SIAM J. Matrix Anal. Appl.,26:599-620,2005. (Cited on p. 352.)   
[544] Marcus J. Grote and Thomas Huckle. Parallel preconditioning with sparse approximate inverses. SIAM J. Sci. Comput.,18:838-853,1997. (Cited on p. 314.)   
[545] Ming Gu and Stanley C.Eisenstat. A Stable and Fast Algorithm for Updating the Singular Value Decomposition. Tech. Report RR-939, Department of Computer Science, Yale University, New Haven, CT,1993.(Cited on p. 363.)   
[546] Ming Gu and Stanley C.Eisenstat. A divide-and-conquer algorithm for the bidiagonal SVD. SIAM J. Matrix Anal. Appl.,16:79-92,1995. (Cited on pp. 358,359.)   
[547] Ming Gu and Stanley C. Eisenstat. A divide-and-conquer algorithm for the symmetric tridiagonal eigenproblem. SIAM J. Matrix Anal. Appl.,16:172-191,1995. (Cited on p. 358.)   
[548] Ming Gu and Stanley C.Eisenstat. Downdating the singular value decomposition. SIAM J. Matrix Anal. Appl.,16:793-810,1995. (Cited on p. 363.)   
[549] Ming Gu and Stanley C.Eisenstat. Efficient algorithms for computing a strong rank-revealing QR factorization. SIAM J. Sci. Comput.,17:848-869,1996. (Cited on p. 84.)   
[550] Marten E. Gulliksson. On the modified Gram-Schmidt algorithm for weighted and constrained linear least squares problems. BIT Numer Math.,35:453-468,1995. (Cited on p.160.)   
[551] Marten Gulliksson and Per-Ake Wedin. Modifying the QR-decomposition to constrained and weighted linear least squares.SIAM J. Matrix Anal. Appl.,13:1298-1313,1992. (Cited on p. 121.)   
[552]Marten E. Gulliksson and Per-Ake Wedin. Perturbation theory for generalized and constrained linear least squares. Numer: Linear Algebra Appl.,7:181-196,2000. (Cited on p.158.)   
[553] B.C. Gunter and Robert A. Van de Geijn. Parallel out-of-core computation and updating of the QR factorization. ACM Trans. Math. Softw.,31:60-78,2005.(Cited on p. 112.)   
[554] Hongbin Guo and Rosemary A. Renaut. A regularized total least squares algorithm. In Sabine Van Huffel and P.Lemmerling,editors,Total Least Squaresand Errors-in-Variables Modeling,pages 57-66. Kluwer Academic Publishers,Dordrecht, 2002.(Cited on p. 226.)   
[555] Fred G. Gustavson. Finding the block lower triangular form of a matrix. In J. R.Bunch and D.J. Rose,editors,Sparse Matrix Computations,pages 275-289.Academic Press,New York,1976. (Cited on p. 264.)   
[556] Martin H. Gutknecht. Block Krylov space methods for linear systems with multiple right handsides: An introduction. In A. H. Siddiqi,I. S. Duff, and O. Christensen,editors, Modern Mathematical Models, Methods, and Algorithms for Real World Systems, pages 420-447. Anarnaya Publishers,New Dehli,India,2007.(Cited on p. 299.)   
[557] Irwin Guttman, Victor Pereyra,and Hugo D. Scolnik.Least squares estimation for a class of nonlinear models. Technometrics,15:309-318,1973. (Cited on p. 405.)   
[558] L.A. Hageman,Franklin T.Luk,and David M. Young.On the equivalence of certain iterative acceleration methods. SIAM J. Numer Anal.,17:852-873,1980. (Cited on p. 308.)   
[559] Louis A. Hageman and David M. Young. Applied Iterative Methods.Dover, Mineola,NY,2004. Unabridged republication of the work first published by Academic Press,New York,1981.(Cited on p. 269.)   
[560] Wiliam W. Hager. Condition estimates. SIAM J. Sci. and Statist. Comput.，5:311-316,1984. (Cited on pp. 96, 97.)   
[561] Arne Hald. Statistical Theory with Engineering Applications.Wiley, New York,1952. Translated by G. Seidelin. (Cited on p. 205.)   
[562]N. Halko,P. G. Martinsson,and J.A. Tropp.Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions. SIAM Rev., 53:217-288, 2011. (Cited on p. 319.)   
[563] Sven J. Hammarling. A note on modifications to the Givens plane rotations. J. Inst. Math. Appl., 13:215-218,1974. (Cited on p. 50.)   
[564] Sven J. Hammarling.The numerical solution of the general Gauss-Markoff linear model. In T. S.Durrani et al., editors,Mathematics in Signal Processing. Clarendon Press, Oxford University Press,New York,pages 441-456,1987. (Cited on p.123.)   
[565] Sven J. Hammarling,Nicholas J. Higham,and Craig Lucas.LAPACK-style codes for pivoted Cholesky and QR updating. In Bo Kagstrom, Erik Elmroth, Jack J. Dongarra, and J. Wasniewski, editors,Applied Parallel Computing: State of the Art in Scientific Computing. Proceedings from the Eighth International Workshop,PARA 2006,pages 137-146,2006.(Cited on p. 148.)   
[566] Martin Hanke.Accelerated Landweber iteration for the solution of il-osed equations.Numer. Math.,60:341-373,1991. (Cited on p. 326.)   
[567] Martin Hanke. Conjugate Gradient Type Methods for Ill-Posed Problems,volume 327 of Pitman Research Notes in Math. Longman Scientific and Technical, Harlow, UK,1995. (Cited on p. 334.)   
[568] Martin Hanke. On Lanczos based methods for the regularization of discrete ill-posed problems. BIT Numer: Math.,41:1008-1018,2001. (Cited on pp.332,334.)   
[569]Martin Hanke.A Taste of Inverse Problems:Basic Theory and Examples.SIAM,Philadelphia, 2017. (Cited on p.182.)   
[570] Martin Hanke and Per Christian Hansen. Regularization methods for large-scale problems. Surveys Math.Indust.,3:253-315,1993.(Cited on pp.175,177,182,182,333,334.)   
[571] Martin Hanke, James G. Nagy, and Curtis Vogel. Quasi-Newton approach to nonnegative image restorations. Linear Algebra Appl.,316:223-236,2000. (Cited on p. 417.)   
[572] Martin Hanke and Curtis R. Vogel. Two-level preconditioners for regularized inverse problems I. Theory.Numer. Math.,83:385-402,1999.(Cited on p. 321.)   
[573] Per Christian Hansen.The discrete Picard condition for discrete ill-posed problems.BIT Numer. Math.,30:658-672,1990. (Cited on p. 172.)   
[574] Per Christian Hansen. Analysis of discrete il-osed problems by means of the L-curve. SIAM Rev., 34:561-580,1992. (Cited on p. 178.)   
[575] Per Christian Hansen． Regularization tools:A MATLAB package for analysis and solution of discrete ill-posed problems. Numerical Algorithms,46:1-35,1994. (Cited on p.182.)   
[576] Per Christian Hansen.Rank-Deficient and Discrete Ill-Posed Problems.Numerical Aspects of Linear Inversion. SIAM,Philadelphia,1998.(Cited on pp.174,178,182,182,322.)   
[577] Per Christian Hansen. Deconvolution and regularization with Toeplitz matrices. Numer Algorithms, 29:323-378,2002. (Cited on p. 173.) [578] Per Christian Hansen. Regularization tools version 4.O for MATLAB 7.3. Numer. Algorithms,   
46:189-194,2007. (Cited on p. 182.) [579] Per Christian Hansen. Discrete Inverse Problems. Insight and Algorithms,volume 7of Fundamentals of Algorithms.SIAM,Philadelphia,2010.(Cited on pp.175,182,334.) [580] Per Christian Hansen. Oblique projections and standard form transformations for discrete inverse problems. Numer Linear Algebra Appl.,20:250-258,2013. (Cited on p. 182.) [581] Per Christian Hansen and H. Gesmar. Fast orthogonal decomposition of rank deficient Toeplitz matrices. Numer Algorithms,4:151-166,1993. (Cited on p. 241.) [582]PerChristian HansenandToke Koldborg Jensen. Smoothing-normpreconditioning forregularizing minimum-residual methods. SIAM J. Matrix Anal. Appl.,29:1-14,2006. (Cited on p. 322.) [583] Per Christian Hansen, James G.Nagy,and Dianne P.O'Leary. Deblurring Images. Matrices, Spectra,and Filtering. SIAM,Philadelphia,2006.(Cited on pp.182,239.) [584] Per Christian Hansen and Dianne Prost O'Leary. The use of the L-curve in the regularization of discrete il-posed problems. SIAM J. Sci. Comput.,14:1487-1503,1993.(Cited on p.178.) [585] Per Christian Hansen, T. Seki, and H. Shibahashi. The modified truncated SVD method for regularization in general form. SIAM J. Statist. Comput.,13:1142-1150,1992.(Cited on pp.174,   
174.) [586] Per Christian Hansen and Plamen Y. Yalamov. Computing symmetric rank-revealing decompo-sitions via triangular factorizations. SIAM J. Matrix Anal. Appl.,23:443-458,2001.(Cited on p. 79.) [587] Richard J. Hanson. Linear least squares with bounds and linear constraints.SIAM J. Sci. Statist. Comput.,7:826-834,1986. (Cited on p. 162.) [588] Richard J. Hanson and K. H. Haskell. Algorithm 587: Two algorithms for the linearly constrained least squares problem. ACM Trans. Math. Softw.,8:323-333,1982. (Cited on p. 162.) [589] Richard J. Hanson and Charles L.Lawson．Extensions and applications of the Householder al-gorithm for solving linear least squares problems. Math. Comp., 23:787-812,1969.(Cited on p. 77.) [590] Richard J. Hanson and Michael J. Noris.Analysis of measurements based on the singular value decomposition. SIAM J. Sci. Statist. Comput.,2:363-373,1981. (Cited on pp.51, 386.) [591] Vjeran Hari and Kresimir Veselic. On Jacobi's methods for singular value decompositions. SIAM J. Sci. Statist. Comput., 8:741-754,1987. (Cited on p. 357.) [592] R. V.L. Hartley. A more symmetrical Fourier analysis applied to transmisson problems. Proc. IRE,30:144-150,1942. (Cited on p. 320.) [593] K.H. Haskell and Richard J. Hanson.Selected Algorithm for the Linearly Constrained Least Squares Problem-A User's Guide. Tech. Report SAND78-1290, Sandia National Laboratories, Albuquerque,NM,1979. (Cited on p. 162.) [594]K.H. Haskelland Richard J. Hanson. An algorithm for linear least squares problems with equality and nonnegativity constraints. Math. Prog.,21:98-118,1981. (Cited on pp. 162,162.) [595] Trevor Hastie,Robert Tibshirani, and Jerome Friedman.The Elements of Statistical Learning. Data Mining,Inference,and Prediction.Springer-Verlag,Berlin,second edition,2Oo9.(Cited on pp. 420,426.) [596] Michael T. Heath. Some extensions of an algorithm for sparse linear least squares problems. SIAM J. Sci. Statist. Comput.,3:223-237,1982. (Cited on pp.261,262,263.) [597] M. T. Heath, A. J. Laub, C. C. Paige,and R. C. Ward. Computing the singular value decomposition of a product of two matrices. SIAM J. Sci. Statist. Comput.,7:1147-1149,1986. (Cited on pp.128,   
349.) [598] M.D.Hebden. An Algorithm for Minimization Using Exact Second Derivatives. Tech.Report T.P.   
515,Atomic Energy Research Establishment,Harwell, UK,1973.(Cited on p.169.)   
[599] I. S. Helland. On the structure of partial least squares regression. Comm. Statist. Theory Methods Ser B,17:581-607,1988. (Cited on p. 203.)   
[600] F.R.Helmert. Die Mathematischen und Physikalischen Theorieen der hoheren Geodäsie. Einleitungund1Teil:DiemathematischenTheorieen.Druckund VerlagvonB.G.Teuber,Leipzig, 1880.(Cited on p. 206.)   
[601] H. V. Henderson and S.R. Searle. On deriving the inverse of a sum of matrices. SIAM Review, 23:53-60,1981. (Cited on p. 139.)   
[602] H. V. Henderson and S. R. Searle. The vec-permutation matrix,the vec operator and Kronecker products: A review. Linear Multilinear Algebra, 9:271-288,1980/1981. (Cited on p. 210.)   
[603] Peter Henrici. The quotient-difference algorithm.Nat. Bur: Standards Appl. Math. Ser.,49:23-46, 1958. (Cited on p. 351.)   
[604] Peter Henrici. Fast Fourier methods in computational complex analysis. SIAM Rev.,21:481-527, 1979. (Cited on p. 237.)   
[605]V. Hernandez,J.E.Roman,and A.Tomas.A parallel variant of the Gram-Schmidt process with reorthogonalization. In G.R. Joubert,W. E. Nagel, F. J. Peters, O. G. Plata,and E.L. Zapata, editors,Parallel Computing: Current & Future Issues in High-End Computing,volume33 of John von Neumann Institute for Computing Series, pages 221-228. Central Institute for Applied Mathematics, Julich, Germany,2006.(Cited on p.109.)   
[606] Magnus R. Hestenes. Inversion of matrices by biorthogonalization and related results.J. Soc. Indust. Appl. Math.,6:51-90,1958. (Cited on p.355.)   
[607] Magnus R. Hestenes. Conjugacy and gradients.In Stephen G. Nash, editor,A History of Scientific Computing,volume 60 of IMA Series in Mathematicsand Its Applications, pages 167-179.ACM Press,New York,1990. (Cited on p. 285.)   
[608] Magnus R. Hestenes and Eduard Stiefel. Methods of conjugate gradients for solving linear systems. J.Res.Nat.Bur: Standards,Sect.B,49:409-436,1952. (Cited on pp.278,280,281,285.)   
[609] K.L. Hiebert. An evaluation of mathematical software that solves nonlinear least squares problems. ACM Trans. Math. Softw.,7:1-16,1981. (Cited on p. 394.)   
[610] Nicholas J. Higham. Computing the polar decomposition—with applications. SIAM J. Sci. Statist. Comput.,7:1160-1174,1986. (Cited on pp. 379,383, 384.)   
[611] Nicholas J. Higham. Computing real square roots of a real matrix. Linear Algebra Appl., 88/89:405-430,1987. (Cited on p. 379.)   
[612] Nicholas J. Higham．Error analysis of the Bjorck-Pereyra algorithm for solving Vandermonde systems. Numer Math.,50:613-632,1987. (Cited on pp. 95, 97,238.)   
[613] Nicholas J. Higham. Fast solution of Vandermonde-like systems involving orthogonal polynomials. IMA J. Numer Anal.,8:473-486,1988. (Cited on p. 238.)   
[614] Nicholas J. Higham. Fortran codes for estimating the one-norm of a real or complex matrix, with applications to condition estimation. ACM Trans. Math. Sofw.,14:381-396,1988.(Cited on p. 97.)   
[615] Nicholas J. Higham. The accuracy of solutions to triangular systems. SIAM J. Numer: Anal., 26:1252-1265,1989. (Cited on p. 43.)   
[616] Nicholas J. Higham. Analysis of the Cholesky decomposition of a semi-definite matrix. In Maurice G. Cox and Sven J. Hammarling, editors, Reliable Numerical Computation, pages 161-185. Clarendon Press, Oxford, UK,1990. (Cited on p. 97.)   
[617] Nicholas J. Higham. How accurate is Gaussian elimination?_In D. F. Grifiths and G. A. Watson, editors,Numerical Analysis 1989:Proceedings of the 13th Dundee Biennial Conference,volume 228 of Pitman Research Notes Math. pages 137-154.Longman Scientific and Technical, Harlow, UK,1990. (Cited on pp. 72, 96.)   
[618] Nicholas J. Higham. Iterative refinement enhances the stability of QR factorization methods for solving linear equations. BIT Numer. Math.,31:447-468,1991. (Cited on pp.59,103,103.)   
[619] Nicholas J. Higham.The matrix sign decomposition and its relation to the polar decomposition. Linear Algebra Appl.,212/213:3-20,1994. (Cited onp. 380.)   
[620] Nicholas J. Higham. A survey of componentwise perturbation theory in numerical linear algebra. In Walter Gautschi, editor, Mathematics of Computation 1943-1953: A Half-Centuryof Computational Mathematics.Mathematics of Computation, 5Oth Anniversary Symposium,August 9-13, 1993,Vancouver, BC,volume 48 of Proceedings of Symposia in Applied Mathematics, pages 49- 78.AMS,Providence,RI,1994. (Cited on pp.29, 31.)   
[621] Nicholas J. Higham. Stable iterations for the matrix square root. Numer Algorithms,15:227-242, 1997. (Cited on p. 93.)   
[622] Nicholas J. Higham．QR factorization with complete pivoting and accurate computation of the SVD. Linear Algebra Appl.,309:153-174,2000. (Cited on p. 341.)   
[623] Nicholas J. Higham. Accuracy and Stability of Numerical Algorithms. SIAM,Philadelphia,second edition,2002. (Cited on pp.34,37,39,44,54,57,58,65,72,96,98,101,239.)   
[624] Nicholas J. Higham. $J$ -orthogonal matrices: Properties and generation. SIAM Rev., 45:504-519, 2003.(Cited on pp.19,137.)   
[625] Nicholas J.Higham.Functions of Matrices.Theory and Computation.SIAM,Philadelphia,2008. (Cited on pp.378,383,384,384.)   
[626] Nicholas J. Higham. The world's most fundamental matrix equation decomposition. SIAM News, Dec.:1-3,2017. (Cited on p. 138.)   
[627] Nicholas J. Higham and Theo Mary. Mixed precision algorithms in numerical linear algebra. Acta Numer.,31:347-414,2022. (Cited on p. 104.)   
[628] Christopher J. Hillar and Lek-Heng Lim. Most tensor problems are NP-hard. J. ACM, 6O:Article 45,2013. (Cited on p. 216.)   
[629] F.L. Hitchcock. The expression of a tensor or a polyadic as a sum of products. J. Math. Phys., 7:164-189,1927. (Cited on p. 216.)   
[630] Iveta Hnetynkova,Martin Plesinger,Diana Maria Sima,Zdenek Strakos,and Sabine Van Huffel. The total least squares problem in $A X \approx B$ ：A new classification with the relationship to the classical works. SIAM J. Matrix Anal. Appl.,32:748-770,2011. (Cited on p. 196.)   
[631] Iveta Hnetynkova, Martin Plesinger,and Zdenek Strakos. The regularization effect of the Golub-Kahan iterative bidiagonalization and revealing the noise level in the data.BIT Numer: Math., 49:669-696,2009. (Cited on p. 335.)   
[632] Iveta Hnetynkova,Martin Plesinger,and Zdenek Strakos. The core problem within a linear approximation problem $A X \approx B$ with multiple right-hand sides.SIAMJ.Matrix Anal.Appl.,34:917-931, 2013.(Cited on p. 196.)   
[633] Iveta Hnetynkova,Martin Plesinger,and Zdenek Strakos.Band generalization of the Golub-Kahan bidiagonalization, generalized Jacobi matrices,and the core problem. SIAM J. Matrix Anal. Appl., 36:417-434,2015. (Cited on pp. 196,305.)   
[634] Michiel E. Hochstenbach. A Jacobi-Davidson type SVD method. SIAM J. Sci. Comput.,23:606- 628,2001. (Cited on p. 376.)   
[635] Michiel E.Hochstenbach. Harmonic and refined extraction methods for the singular value problem, with applications in least squares problems.BIT Numer Math.,44:721-754,2004.(Cited on pp. 371,371.)   
[636] Michiel E. Hochstenbach and Y.Notay. The Jacobi-Davidson method. GAMM Mit.,29:368-382, 2006.(Cited on p. 375.)   
[637] Walter Hoffmann. Iterative algorithms for Gram-Schmidt orthogonalization. Computing,41:335- 348,1989. (Cited on p. 69.) [638] Y.P. Hong and C.-T.Pan. Rank revealing QR decompositions and the singular value decomposition. Math. Comp.,58:213-232,1992. (Cited on pp.80,80,81.) [639] Roger A. Horn and Charles R. Johnson. Matrix Analysis. Cambridge University Pres,Cambridge, UK,1985. (Cited on pp.116,350,377.) [640] Roger A. Horn and Charles R. Johnson. Topics in Matrix Analysis.Cambridge University Press, Cambridge, UK,1991. (Cited on pp.13,210.) [641] Roger A. Horn and Charles R.Johnson. Matrix Analysis. Cambridge University Pres, Cambridge, UK,second edition,2012. (Cited on pp.12,20.) [642] H.Hotelling.Relation between two sets of variables.Biometrica,28:322-377,1936.(Cited on p. 19.) [643] Patricia D.Hough and Stephen A. Vavasis. Complete orthogonal decomposition for weighted least squares. SIAM J. Matrix Anal. Appl.,18:369-392,1997. (Cited on p. 133.) [644] Alston S. Householder. Unitary triangularization of a nonsymmetric matrix. J. Assoc. Comput. Mach.,5:339-342,1958. (Cited on pp. 46,51.) [645] Alston S.Householder. The Theory of Matrices in Numerical Analysis. Dover,Mineola, NY,1975. Corrected republication of work first published in 1964 by BlaisdellPubl. Co.,New York.（Cited on pp.139,281.) [646]Alston S.Householder and Friedrich L.Bauer.On certain iterative methods for solving linear systems. Numer Math.,2:55-59,1960. (Cited on p.273.) [647] Gary W. Howelland Marc Baboulin. LU preconditioning for overdetermined sparse least squares problems. InR.Wyrzykowski,E.Deelman, J.Dongarra, K. Kurczewiski, J. Kitowski,and K. Wiatr, editors,11th Internat. Conf.Parallel Proc.and Appl. Math.,2015,Krakow,Poland,volume 9573 of Lecture Notes in Computer Science,pages 128-137, Springer, Heidelberg,2016.(Cited on p. 318.) [648] P.J. Huber.Robust Statistics.Wiley,New York,1981. (Cited on pp. 422,422.) [649] M.F Hutchinson and F.R.de Hoog. Smoothing noisy data with spline functions.Numer Math.,   
47:99-106,1985. (Cited on p. 180.) [650] M.F. Hutchinson and F R. de Hoog. A fast procedure for calculating minimum cross-validation cubic smoothing splines. ACM Trans. Math. Softw.,12:150-153,1986. (Cited on p. 180.) [651] Tsung-Min Hwang,Wen-Wei Lin,and Dan Pierce. Improved bounds for rank revealing LU factorizations. Linear Algebra Appl.,261:173-186,1997. (Cited on p. 91.) [652] Tsung-Min Hwang, Wen-Wei Lin, and Eugene K. Yang. Rank revealing LU factorizations. Linear Algebra Appl.,175:115-141,1992. (Cited on p. 91.) [653] Bruno Iannazzo. A note on computing the matrix square root. Calcolo,40:273-283,2003.(Cited on p. 379.) [654] Bruno Iannazzo. On the Newton method for the matrix pth root. SIAM J. Matrix Anal. Appl.,   
28:503-523,2006. (Cited on p. 379.) [655] IEEE Standard for Floating-Point Arithmetic.In IEEE Standard 754-2019 (Revision of IEEE Standard 754-2008), pages 1-84,2019. (Cited on p. 32.) [656] Akira Imakura and Yusaka Yamamoto.Efcient implementations of the modified Gram-Schmidt orthogonalization with a non-standard inner product. Japan J. Indust. Appl. Math.,36:619-641,   
2019.(Cited on p. 122.) [657] D. Irony,Sivan Toledo,and A. Tiskin. Using perturbed QR factorizations to solve linear leastsquares problems. J. Paralel Distrib. Comput., 64:1017-1026,2004. (Cited on p. 114.) [658] Carl Gustav Jacob Jacobi. Uber eine neue Auflosungsart der beider Methode der kleinsten Quadrate vorkommenden lineären Gleichungen. Astron. Nachr.,22:297-306,1845. (Cited on p. 51.)   
[722] Rasmus Munk Larsen. Lanczos Bidiagonalization with Partial Reorthogonalization. Tech. Report DAIMI PB-357,Department of Computer Science,Aarhus University, Denmark,1998. (Cited on p. 373.)   
[723] Rasmus Munk Larsen. PROPACK: A Software Package for the Singular Value Problem Based on Lanczos Bidiagonalization with Partial Reorthogonalization. http://soi.stanford .edu/ \~rmunk/PROP ACK/,SCCM, Stanford University, Stanford,CA,20O0. (Cited on p. 374.)   
[724] Peter Lauchli. Jordan-Elimination und Ausgleichung nach kleinsten Quadraten. Numer Math., 3:226-240,1961. (Cited on pp.40, 316.)   
[725] Charles L. Lawson. Contributions to the Theory of Linear Least Maximum Approximation. Ph.D. thesis,University of California,Los Angeles,1961. (Cited on p. 423.)   
[726] Charles L.Lawson. Sparse Matrix Methods Based on Orthogonality and Conjugacy. Tech. Mem. 33-627,Jet Propulsion Laboratory,Cal.Inst. of Tech.,Pasadena, CA,1973.(Cited on p.285.)   
[727] Charles L.Lawson and Richard J. Hanson. Solving Least Squares Problems, volume 15 of Classics in Applied Math.,SIAM,Philadelphia,1995.Unabridged,revised republication of the work first published by Prentice-Hall, Inc., Englewood Cliffs,NJ,1974.(Cited on pp.137,157,160,162, 167,167,178,189,192.)   
[728] Charles L.Lawson,Richard J. Hanson,D.R. Kincaid,and Fred T. Krogh.Basic Linear Algebra Subprograms for Fortran usage. ACM Trans. Math. Softw.,5:308-323,1979. (Cited on p. 113.)   
[729] Adrien-Marie Legendre. Nouvelles methodes pour la détermination des orbites des cometes. Courcier,Paris,1805. (Cited on p. 2.)   
[730] R. B.Lehoucq. Implicitly restarted Arnoldi methods and subspace iteration. SIAM J. Matrix Anal. Appl.,23:551-562,2001.   
[731] R. B. Lehoucq, D.C. Sorensen, and C. Yang. ARPACK Users' Guide: Solution of Large-Scale Eigenvalue Problems with Implicitly RestartedArnoldi Methods.SIAM,Philadelphia,1998.(Cited on pp. 373,375.)   
[732] Richard B.Lehoucq. The computations of elementary unitary matrices.ACM Trans. Math. Softw., 22:393-400,1996. (Cited on p. 47.)   
[733] Steven J. Leon, Ake Bjorck, and Walter Gander. Gram-Schmidt orthogonalization: 1OO years and more. Numer. Linear Algebra Appl.,20:492-532,2013. (Cited on p. 63.)   
[734] O.Leringe and Per-A. Wedin. A Comparison between Diferent Methods to Compute a Vector x Which Minimizes $\| A x - b \| _ { 2 }$ When $G x = h$ . Tech. Report, Department of Computer Science, Lund University,Lund, Sweden,1970. (Cited on p.158.)   
[735] S.E.Leurgans,R.T. Ross,and R.B. Abel. A decomposition for three-way arrays. SIAM J. Matrix Anal. Appl.,14:1064-1083,1993. (Cited on pp. 217, 373.)   
[736] K. Levenberg. A method for the solution of certain non-linear problems in least squares. Quart. Appl. Math.,2:164-168,1944. (Cited on pp.169,175,396.)   
[737] J. G. Lewis. Algorithm 582: The Gibbs-Poole-Stockmeyer and Gibbs-King algorithms for reordering sparse matrices. ACM Trans. Math. Softw.,8:190-194,1982. (Cited on p. 251.)   
[738] J.G.Lewis.Implementation of The Gibbs-Poole-Stockmeyer and Gibbs-King algorithms.ACM Trans. Math. Softw.,8:180-189,1982. (Cited on p. 251.)   
[739] J.G.Lewis,D.J.Pierce,and D. K. Wah. Multifrontal Householder QR Factorization. Tech. Report ECA-TR-127-Revised, Boeing Computer Services,Seatle, WA,1989. (Cited on p. 258.)   
[740] Chi-Kwong Li and Gilbert Strang. An elementary proof of Mirsky's low rank approximation theorem.Electronic J. Linear Algebra,36:347-414,2020. (Cited on p. 24.)   
[741] Na Li and Yousef Saad. MIQR: A multilevel incomplete QR preconditioner for large sparse leastsquares problems. SIAM J. Matrix Anal. Appl.,28:524-550,2006. (Cited on pp. 313, 318.)   
[742] Ren-Cang Li. Bounds on perturbations of generalized singular values and of associated subspaces. SIAM J. Matrix Anal. Appl.,14:195-234,1993. (Cited on p. 125.)   
[743] Ren-Cang Li. Solving Secular Equations Stably and Efciently. Tech.Report UCB/CSD-94-851, Computer Science Department, University of California, Berkeley, CA,1994.(Cited on pp. 359, 361.)   
[744] Yuying Li.A globally convergent method for $l _ { p }$ problems．SIAMJ.Optim.,3:609-629,1993. (Cited on p. 425.)   
[745] Yuying Li. Solving $l _ { p }$ Problems and Applications.Tech. Report CTC93TR122, 03/93,Advanced Computing Research Institute, Cornell University, Ithaca, NY,1993. (Cited on p. 425.)   
[746] Jorg Liesen and Zdenek Strakos.Krylov Subspace Methods;Principles and Analysis. Oxford University Press, Oxford,UK,2012.(Cited on pp.285,289.)   
[747] Lek-Heng Lim. Tensor and hypermatrices. In Leslie Hogben, editor, Handbook of Linear Algebra, pages_15.1-15.30. Chapman & Hal/CRC Press, Boca Raton,FL,second edition, 2013. (Cited on p. 217.)   
[748] Chih-Jen Lin and Jorge J. Moré.Newton's method for large bound-constrained optimization problems. SIAM J.Optim. Theory Appl.,9:1100-1127,1999.(Cited on p. 310.)   
[749] Per Lindstrom.A General Purpose Algorithm for Nonlinear Least Squares Problems with Nonlinear Constraints. Tech. Report UMINF-102.83,Institute of Information Processing, University of Umea, Sweden,1983. (Cited on p. 396.)   
[750] Per Lindstrom. Two User Guides, One (ENLSIP) for Constrained- One (ELSUNC) for Unconstrained Nonlinear Least Squares Problems. Tech. Report UMINF-109.82 and 110.84, Institute of Information Processing, University of Umea, Sweden,1984. (Cited on p. 411.)   
[751] Per Lindstrom and Per-A.Wedin. A new linesearch algorithm for unconstrained nonlinear least squares problems. Math. Program.,29:268-296,1984. (Cited on p.395.)   
[752] Per Lindstrom and Per-A. Wedin. Methods and Software for Nonlinear Least Squares Problems. Tech.Report UMINF-133.87, Institute of Information Processing, University of Umea, Sweden, 1988.(Cited on p. 402.)   
[753] Richard J.Lipton,Donald J.Rose,and Robert E.Tarjan. Generalized nested dissection. SIAM J. Numer Anal.,16:346-358,1979. (Cited on p. 256.)   
[754] Joseph W. H.Liu. On general row merging schemes for sparse Givens transformations. SIAM J. Sci. Statist. Comput.,7:1190-1211,1986. (Cited on pp.255,256.)   
[755] Joseph W.H. Liu. The role of elimination trees in sparse factorization. SIAM J. Matrix Anal. Appl., 11:134-172,1990. (Cited on pp.250, 250,256,258.)   
[756] Qiaohua Liu. Modified Gram-Schmidt-based methods for block downdating the Cholesky factorization. J. Comput. Appl. Math.,235:1897-1905,2011. (Cited on p. 148.)   
[757] James W. Longley. Modified Gram-Schmidt process Vs.classical Gram-Schmidt. Comm. Statist. Simulation Comput.,10:517-527,1981. (Cited on p. 62.)   
[758] Per Lotstedt.Perturbation bounds for the linear least squares problem subject to linear inequality constraints. BIT Numer: Math.,23:500-519,1983. (Cited on p. 167.)   
[759] Per Lotstedt.Solving the minimal least squares problem subject to bounds on the variables. BIT Numer Math.,24:206-224,1984. (Cited on p.167.)   
[760] P.-O.Lowdin. On the non-orthogonality problem. Adv. Quantum Chemistry,5:185-199,1970. (Cited on p. 383.)   
[761] Szu-Min Lu and Jesse L. Barlow. Multifrontal computation with the orthogonal factors of sparse matrices. SIAM J. Matrix Anal. Appl.,17:658-679,1996. (Cited on p. 258.)   
[762] Franklin T.Luk.A rotation method for computing the QR-decomposition. SIAM J. Sci. Statist. Comput.,7:452-459,1986. (Cited on p. 357.)   
[763] Franklin T. Luk and S. Qiao. A new matrix decomposition for signal processing. Automatica, 30:39-43,1994. (Cited on p. 128.)   
[764] I. Lustig,R.Marsten,and D. Shanno. Computational experience with a primal-dual interior point method for linear programming. Linear Algebra Appl.,152:191-222,1991. (Cited on pp. 418, 419.)   
[765] D.Ma,L. Yang,R.M.T. Fleming,I. Thiele,B.O.Palsson,and M.A. Saunders.Reliable and effcient solution of genome-scale models of metabolism and macromolecular expression. Sci. Rep.,36:40863,2017． (Cited on p.101.)   
[766]Kaj Madsen and Hans Bruun Nielsen.Finite algorithms for robust linear regression.BIT Numer. Math.,30:682-699,1990. (Cited on p. 425.)   
[767] Kaj Madsen and Hans Bruun Nielsen. A finite smoothing algorithm for linear $\ell _ { 1 }$ estimation. SIAM J. Optim.,3:223-235,1993. (Cited on p. 422.)   
[768] N. Mahdavi-Amiri. Generally Constrained Nonlinear Least Squares and Generating Test Problems:Algorithmic Approach.Ph.D.thesis,The John Hopkins University,Baltimore,MD,1981. (Cited on p. 162.)   
[769] Alexander N. Malyshev. Parallel algorithms for solving spectral problems of linear algebra. Linear Algebra Appl.,188:489-520,1993. (Cited on p. 382.)   
[770] Alexander N. Malyshev and Miloud Sadkane. Computation of optimal backward perturbation bounds for large sparse linear least squares problems. BIT Numer Math.,41:739-747,2001. (Cited on p. 99.)   
[771] Rolf Manne. Analysis of two partial-least-squares algorithms for multivariate calibration. Chemom. Intell.Lab.Syst.,2:187-197,1987. (Cited on pp. 202, 203.)   
[772] P.Manneback. On Some Numerical Methods for Solving Large Sparse Linear Least Squares Problems.Ph.D.thesis,Facultés Universitaires Notre-Dame de la Paix,Namur,Belgium,1985.(Cited on pp.254,308.)   
[773] P.Manneback, C. Murigande,and Philippe L. Toint. A modification of an algorithm by Golub and Plemmons for large linear least squares in the context of Doppler positioning. IMA J. Numer. Anal., 5:221-234,1985. (Cited on p. 206.)   
[774] Thomas A.Manteuffel. An incomplete factorization technique for positive definite linear systems. Math. Comp.,34:473-497,1980. (Cited on p.309.)   
[775] A.A. Markov.Wahrscheinlichkeitsrechnung. Liebmann,Leipzig,second edition,1912.(Cited on p. 3.)   
[776] Ivan Markovsky. Bibliography on total least-squares and related methods. Statist. Interface,3:1-6, 2010.(Cited on p. 226.)   
[77] Ivan Markovsky and Sabine Van Hufel. Overview of total least-squares methods. Signal Process., 87:2283-2302,2007. (Cited on p. 226.)   
[778] Harry M. Markowitz.The elimination form of the inverse and its application to linear programming. Management Sci.,3:255-269,1957. (Cited on p. 251.)   
[779] Donald W. Marquardt. An algorithm for least-squares estimation of nonlinear parameters.J. Soc. Indust. Appl. Math.,11:431-441,1963. (Cited on p. 396.)   
[780] J. J. Martinez and J. M. Pena. Fast paralel algorithmof Bjorck-Pereyra type for solving Cauchy-Vandermonde linear systems. Appl. Numer: Math.,26:343-352,1998. (Cited on p. 239.)   
[781] W.F. Massy. Principal components regression in exploratory statistical research. J. Amer: Statist. Assoc., 60:234-246,1965. (Cited on p. 174.)   
[782] Nicola Mastronardi and Paul Van Dooren. The antitriangular factorization of symmetric matrices. SIAM J. Matrix Anal. Appl.,34:173-196,2013. (Cited on p. 137.)   
[783] Nicola Mastronardi and Paul Van Dooren. An algorithm for solving the indefinite least squares problem with equality constraints. BIT Numer Math.,54:201-218,2014. (Cited on p. 137.)   
[784] Pontus Matstoms. QR27-Specification Sheet. Tech. Report， Department of Mathematics, Linkoping University, Sweden,1992. (Cited on p. 258.)   
[785] Pontus Matstoms. Sparse QR factorization in MATLAB. ACM Trans. Math. Softw.,2O:136-159, 1994.(Cited on p. 258.)   
[786] J.A.Meijerink and Henk A.van der Vorst.An iterative solution method for linear systems of which the coefficient matrix is a symmetric M-matrix. Math. Comp.,31:148-162,1977. (Cited on p. 309.)   
[787] Beatrice Meini. The matrix square root from a new functional perspective: Theoretical results and computational issues. SIAM J. Matrix Anal. Appl.,26:362-376,2004. (Cited on p. 379.)   
[788] Xiangrui Meng. Randomized Algorithms for Large-Scale Strongly Over-Determined Linear Regression Problems.Ph.D.thesis, Stanford University, Stanford, CA,2014.(Cited on p.212.)   
[789] Xiangrui Meng, Michael A. Saunders,and Michael W. Mahoney. LSRN: A paralel iterative solver for strongly over- or underdetermined systems. SIAM J. Sci. Comput., 36:C95-C118,2014. (Cited on pp. 320,321.)   
[790] G. Merle and Helmut Spath. Computational experience with discrete $L _ { p }$ approximation. Computing,12:315-321,1974. (Cited on p. 424.)   
[791] Gérard Meurant. The Lanczos and Conjugate Gradient Algorithms: From Theory to Finite Precision Computations,volume 19 of Software,Environments,and Tools. SIAM,Philadelphia,2006. (Cited on p. 285.)   
[792] Gerard Meurant and Zdenek Strakos.The Lanczos and conjugate gradient algorithms in finite precision arithmetic. Acta Numer.,15:471-542,2006. (Cited on pp. 285,299.)   
[793] Carl D. Meyer, Jr. Generalized inversion of modified matrices. SIAM J. Appl. Math.,24:315-323, 1973.(Cited on p. 139.)   
[794] Alan J.Miller. Subset Selection in Regression,volume 25 of Monograph on Statistics and Applied Probability. Chapman & Hall/CRC Press, Boca Raton,FL,second edition,2002. (Cited on p.140.)   
[795] Kenneth S.Miller. Complex linear least squares. SIAM Rev.,15:706-726,1973. (Cited on p. 5.)   
[796] Luiza Miranian and Ming Gu. Strong rank-revealing LU factorizations. Linear Algebra Appl., 367:1-16,2003. (Cited on p. 91.)   
[797] L. Mirsky. Symmetric gauge functions and unitarily invariant norms. Quart. J. Math. Oxford, 11:50-59,1960. (Cited on p. 24.)   
[798] S. K. Mitra and C. R. Rao. Projections under seminorms and generalized Moore-Penrose inverses. Linear Algebra Appl., 9:155-167,1974. (Cited on p. 158.)   
[799] Cleve B.Moler. Iterative refinement in floating point. J. Assoc. Comput. Mach.,14:316-321,1967. (Cited on p. 101.)   
[800] Alexis Montoison and Dominique Orban.BILQ: An iterative method for nonsymmetric linear systems with a quasi-minimum error property. SIAM J. Matrix Anal. Appl., 41:1145-1166, 2020. (Cited on p. 304.)   
[801] Alexis Montoison and Dominique Orban. TRICG and TRIMR: Two iterative methods for symmetric quasi-definite systems. SIAM J. Sci. Comput., 43:A2502-A2525,2021. (Cited on p. 331.)   
[802] Alexis Montoison,Dominique Orban,and Michael Saunders.MINARES:An Iterative Solver for Symmetric Linear Systems. Tech.Report GERARD G-2023-40,Ecole Polytechnique Montreal, 2023.(Cited on p. 300.)   
[803]Marc Moonen, Paul Van Dooren, and Joos Vandewalle.A singular value decomposition updating algorithm for subspace tracking.SIAM J. Matrix Anal. Appl.，13:1015-1038,1992.(Cited on pp.360,363.)   
[804] E.H.Moore. On the reciprocal of the general algebraic matrix. Bull Amer Math. Soc.,26:394-395, 1920. (Cited on p. 16.)   
[805] José Morales and Jorge Nocedal. Remark on Algorithm 778: L-BFGS-B:Fortran subroutines for large-scale bound-constrained optimization. ACM Tran. Math. Softw.,38:Article 7,2011. (Cited on p. 420.)   
[806] Jorge J. Moré.The Levenberg-Marquardt algorithm: Implementation and theory. In G.A.Watson, editor, Numerical Analysis Proceedings Biennial Conference Dundee 1977,volume 630 of Lecture Notes in Mathematics, pages 105-116. Springer-Verlag,Berlin,1978. (Cited on p. 396.)   
[807] Jorge J. Moré.Recent developments in algorithms and software for trust region-methods. In A.Bachem, M. Grotchel,and B.Korte,editors, Mathematical Programming. The State of the Art, Proceedings Bonn 1982,pages 258-287. Springer-Verlag,Berlin,1983. (Cited on p. 396.)   
[808] Jorge J. More,B.S. Garbow,and K.E.Hilstrom. Users’ Guide for MINPACK-1. Tech. Report ANL-80-74,Applied Math. Div.,Argonne National Laboratory, Argonne, IL,1980.(Cited on p. 402.)   
[809] Jorge J. Moré and G.Toraldo. Algorithms for bound constrained quadratic programming problems. Numer: Math.,55:377-400,1989. (Cited on p. 420.)   
[810] Ronald B.Morgan.A restarted GMRES method augmented with eigenvectors. SIAM J.Matrix Anal. Appl.,16:1154-1171,1995. (Cited on p. 337.)   
[811] Daisuke Mori, Yusaku Yamamoto,Shao-Liang Zhang,and Takeshi Fukaya. Backward error analysis of the AllReduce algorithm for Householder QR decomposition. Japan J. Indust. Appl. Math., 29:111-130,2012. (Cited on p. 213.)   
[812]Keiichi Morikuni and Ken Hayami.Inner-iteration Krylov subspace methods for least squares problems. SIAM J. Matrix Anal. Appl.,34:1-22,2013. (Cited on p. 309.)   
[813] Keiichi Morikuni and Ken Hayami. Convergence of inner-iteration GMRES methods for rankdeficient least squares problems. SIAM J. Matrix Anal. Appl.,36:225-250,2015. (Cited on p. 309.)   
[814] V.A. Morozov. Methods for Solving Incorrectly Posed Problems. Springer, New York,1984. (Cited on p. 177.)   
[815] N. Munksgaard. Solving sparse symmetric sets of linear equations by preconditioned conjugate gradients. ACM Trans. Math. Softw., 6:206-219,1980. (Cited on p. 310.)   
[816] Joseph M. Myre,Erich Frahm,David J.Lilja,and Martin O.Saar.TNT: A solver for large dense least-squares problems that takes conjugate gradient from bad in theory,to good in practice. In Proceedings ofthe 2018 IEEE International Parallel and Distributed Processing Symposium Workshops,pages 987-995. IEEE,2018. (Cited on p. 312.)   
[817] J. G. Nagy. Toeplitz Least Squares Computations. Ph.D. thesis, North Carolina State University, Raleigh,NC,1991. (Cited on p. 324.)   
[818] James G.Nagy.Fast inverse QR factorization for Toeplitz matrices.SIAM J. Sci. Comput.,14:1174- 1193,1993. (Cited on pp.240,240.)   
[819] James G. Nagy and Zdenek Strakos. Enforcing nonnegativity in image reconstruction algorithms. In Mathematical Modeling, Estimation,and Imaging, pages182-190. Proc. SPIE 4121, Bellingham, WA,2000. (Cited on p. 417.)   
[820] Yuji Nakatsukasa, Zhaojun Bai, and Frangoise Gygi. Optimizing Halley's iteration for computing the matrix polar decomposition. SIAM J. Matrix Anal. Appl.,31:2700-2720,2010.(Cited on pp.385,385.)   
[821] Yuji Nakatsukasa and Roland W. Freund. Computing fundamental matrix decompositions accurately via the matrix sign function in two iterations: The power of Zolotarev's functions. SIAM Rev.,58:461-493,2016. (Cited on p. 382.)   
[822] Yuji Nakatsukasa and Nicholas J. Higham. Stable and eficient spectral divide and conquer algorithms for the symmetric eigenvalue decomposition and the SVD. SIAM J. Sci. Comput.,35:A1325- A1349,2013. (Cited on pp. 381,385.)   
[823] M. Zuhair Nashed. Generalized Inverses and Applications. Academic Press, New York,1976. (Cited on pp.15,16.)   
[824] Larry Neal and George Poole.A geometric analysis of Gaussian elimination.ii. Linear Algebra Appl.,173:239-264,1992. (Cited on p. 86.)

[825] Arkadi Nemirovski and Michael J. Todd. Interior point methods for optimization. Acta Numer., 17:191-234,2008. (Cited on p. 419.)

[826] A. S.Nemirovskii. The regularization properties of the adjoint gradient method in il-posed problems.USSR Comput. Math. Math. Phys.,26:7-16,1986. (Cited on p. 334.)   
[827] Yurii Nesterov and Arkadi Nemirovski. On first-order algorithms for $\ell _ { 1 }$ /nuclear norm minimization. Acta Numer,22:509-575,2013. (Cited on p. 429.)   
[828] Yurii Nesterov and Arkadi Nemirovskii. Interior Point Polynomial Algorithms in Convex Program-ming, volume 13 of Studies in Applied Mathematics.SIAM, Philadelphia,1994. (Cited on p. 419.)   
[829] Olavi Nevanlinna. Convergence of Iterations for Linear Equations. Lectures in Mathematics ETH Zürich.Birkhäuser,Basel,1993.(Cited on p.295.)   
[830] R.A. Nicolaides. Deflation of conjugate gradients with applications to boundary values problems. SIAM J. Numer Anal.,24:355-365,1987. (Cited on p. 337.)   
[831] Ben Noble,editor. Applied Linear Algebra. Prentice-Hall,Englewood Clifs,NJ,1969.(Cited on p.88.)   
[832] Ben Noble.Method for computing the Moore-Penrose generalized inverse and related maters. In M. Zuhair Nashed,editor, Generalized Inverses and Applications,Proceedings of an Advanced Seminar,The University of Wisconsin-Madison,October 8-10,1973,Publication of the Mathematics Research Center,No.32, pages 245-302,Academic Press,New York,1976.(Cited on p. 85.)   
[833] Jorge Nocedal and Stephen J.Wright. Numerical Optimization. Springer Series in Operations Research and Financial Engineering. Springer, New York,second edition,2Oo6.(Cited on p. 402.)   
[834] Paolo Novati and Maria Rosario Russo.A GCV based Arnoldi-Tikhonov regularization method. BIT Numer Math.,54:501-521,2014. (Cited on p. 335.)   
[835] W. Oettli and W.Prager. Compatibility of approximate solution of linear equations with given error bounds for coeffcients and right-hand sides.Numer: Math.,6:404-409,1964. (Cited on p. 99.)   
[836] Gabriel Oksa, Yusaku Yamamoto,and Marian Vajtersic. Convergence to singular triplets in the twosided block-Jacobi's svd algorithm with dynamic ordering. SIAM J. Matrix Anal. Appl.,43:1238- 1262,2022. (Cited on p. 376.)   
[837] Dianne P. O'Leary. The block conjugate gradient algorithm and related methods. Linear Algebra Appl.,29:293-322,1980. (Cited on p. 95.)   
[838] Dianne P. O'Leary. Robust regression computation using iteratively reweighted least squares. SIAM J. Matrix Anal. Appl.,11:466-480,1990. (Cited on pp. 425,425.)   
[839] Dianne P. O'Leary and Bert W. Rust. Variable projection for nonlinear least squares problems. Comput. Optim. Appl.,54:579-593,2013. (Cited on p. 404.)   
[840] Dianne P.O'Leary and John A. Simmons.A bidiagonalization-regularization procedure for large scale discretizations of il-posed problems. SIAM J. Sci. Statist. Comput.,2:474-489,1981. (Cited on p. 332.)   
[841] Dianne P. O'Leary and P. Whitman. Paralel QR factorization by Householder and modified Gram-Schmidt algorithms.Parallel Comput.,16:99-112,1990. (Cited on p.112.)   
[842] S. Oliveira,L.Borges,M. Holzrichter,and T. Soma.Analysis of different partitioning schemes for parallel Gram-Schmidt algorithms. Internat.J.Parallel Emergent Distrib. Syst.,14:293-320, 2000.(Cited on p.109.)   
[843] Serge J. Olszanskyj,James M. Lebak,and Adam W. Bojanczyk. Rank- $k$ modification methods for recursive least squares problems. Numer Algorithms,7:325-354,1994. (Cited on p. 148.)   
[844] Dominique Orban and Mario Arioli. Iterative Solution of Symmetric Quasi-Definite Linear Systems. SIAM, Philadelphia, 2017. (Cited on p. 331.)   
[845] James M. Ortega and Werner C. Rheinboldt. Iterative Solution of Nonlinear Equations in Several Variables,volume 30 of Classics in Applied Math.,SIAM,Philadelphia,20oo.Unabridged republication of the work first published by Academic Press,New York and London,197o.(Cited on pp. 393,395,402.)   
[846] M.R. Osborne. Some special nonlinear least squares problems. SIAM J. Numer Anal.,12:571-592, 1975. (Cited on p. 405.)   
[847] Michael R. Osborne.Nonlinear least squares—the Levenberg algorithm revisited. J. Austr: Math. Soc. Series B,19:342-357,1976. (Cited on p. 396.)   
[848] Michael R. Osborne. Finite Algorithms in Optimization and Data Analysis.John Wiley & Sons, New York,1985. (Cited on p. 423.)   
[849] Michael R. Osborne,Brett Presnell,and B.A. Turlach.A new approach to variable selection in least squares problems. IMA J. Numer Anal.,20:389-404,2000. (Cited on p.425.)   
[850] Michael R. Osborne and G. Alistair Watson. On the best linear Chebyshev approximation. Computer J.,10:172-177,1967. (Cited on p. 422.)   
[851] George Ostrouchov. Symbolic Givens reduction and row-ordering in large sparse least squares problems. SIAM J. Sci. Statist. Comput., 8:248-264,1987. (Cited on p. 253.)   
[852] C. C.Paige. Bidiagonalization of matrices and solution of linear equations. SIAM J. Numer Anal., 11:197-209,1974. (Cited on p. 291.)   
[853] C. C. Paige. Fast numerically stable computations for generalized least squares problems. SIAM J. Numer: Anal.,16:165-171,1979. (Cited on p. 122.)   
[854] C. C.Paige. Computing the generalized singular value decomposition. SIAM J. Sci. and Statist. Comput.,7:1126-1146,1986. (Cited on p. 126.)   
[855] C. C.Paige and M. A. Saunders. Solution of sparse indefinite systems of linear equations. SIAM J. Numer Anal.,12:617-629,1975. (Cited on p. 299.)   
[856] C. C. Paige and M. A. Saunders. Towards a generalized singular value decomposition. SIAM J. Numer Anal.,18:398-405,1981. (Cited on pp.18,19,124,125.)   
[857] Christopher C. Paige. The Computation of Eigenvalues and Eigenvectors of Very Large Sparse Matrices.Ph.D. thesis, University of London, UK,1971. (Cited on p. 294.)   
[858] Christopher C.Paige.Computer solution and perturbation analysis of generalized linear least squares problems.Math. Comp.,33:171-184,1979. (Cited on pp.122,123.)   
[859] Christopher C.Paige.Error analysis of some techniques for updating orthogonal decompositions. Math. Comp.,34:465-471,1980. (Cited on p. 144.)   
[860] Christopher C.Paige. The general linear model and the generalized singular value decomposition. Linear Algebra Appl.,70:269-284,1985. (Cited on p. 126.)   
[861] Christopher C.Paige. Some aspects of generalized QR factorizations.In M.G.Cox and Sven J. Hammarling,editors,Reliable Numerical Computation,pages 71-91. Clarendon Press, Oxford, UK,1990. (Cited on pp. 124,128.)   
[862] Christopher C.Paige. A useful form of a unitary matrix obtained from any sequence of unit 2-norm $_ n$ -vectors. SIAM J. Matrix Anal. Appl.,31:565-583,2009. (Cited on p. 65.)   
[863] Christopher C.Paige. Accuracy of the Lanczos process for the eigenproblem and solution of equations. SIAM J. Matrix Anal. Appl.,40:1371-1398,2019. (Cited on p. 299.)   
[864] Christopher C. Paige, Beresford N. Parlet, and Henk A. van der Vorst. Approximate solutions and eigenvalue bounds from Krylov subspaces. Numer. Linear Algebra Appl.,2:115-133,1995. (Cited on p. 370.)   
[865] Christopher C.Paige,Miroslav Rozloznik,and Zdenek Strakos. Modified Gram-Schmidt (MGS), least squares,and backward stability of MGS-GMRES. SIAM J. Matrix Anal. Appl.,28:264-284, 2006. (Cited on p. 302.)   
[887] PDCO: MATLAB Convex Optimization Software. http://stanford.edu/group/SOL/ software/pdco,2018. (Cited on pp. 427, 428.)   
[888] John W.Pearson and Jennifer Pestana. Preconditioners for Krylov subspace methods: An overview. GAMM Mitt.,43:1-35,2020. (Cited on p. 287.)   
[889] Roger Penrose.A generalized inverse for matrices. Proc.Cambridge Philos. Soc.,51:406-413, 1955. (Cited on p. 14.)   
[890] Victor Pereyra. Iterative methods for solving nonlinear least squares problems. SIAM J. Numer. Anal., 4:27-36,1967. (Cited on p. 393.)   
[891] G.Peters and J.H.Wilkinson.Inverse iteration,il-conditioned equations and Newton's method. SIAM Rev.,21:339-360,1979. (Cited on p. 224.)   
[892] G. Peters and James H. Wilkinson.The least squares problem and pseudo-inverses. Comput. J., 13:309-316,1970. (Cited on pp. 84,88.)   
[893] Emile Picard. Quelques remarques sur les équations integrales de premiére espéce et sur certains problemes de physique mathématique. C.R. Acad. Sci. Paris,148:1563-1568,1909. (Cited on p. 13.)   
[894] Daniel J. Pierce and John G.Lewis. Sparse multifrontal rank revealing QR factorization. SIAM J. Matrix Anal. Appl.,18:159-180,1997. (Cited on pp.258,261.)   
[895]R.L.Plackett.The discoveryof the method of least squares. Biometrika,59:239-251,1972.(Cited on p. 2.)   
[896] Robert J. Plemmons.Monotonicity and iterative approximations involving rectangular matrices. Math. Comp.,26:853-858,1972. (Cited on p. 270.)   
[897] Robert J. Plemmons.Linear least squares by elimination and MGS. J. Assoc. Comput. Mach., 21:581-585,1974. (Cited on p. 88.)   
[898] Robert J. Plemmons.Adjustment by least squares in geodesy using block iterative methods for sparse matrices. In Proceedings of the 1979 Army Numerical Analysis and Computer Conference, pages 151-186,El Paso,TX,1979.(Cited on p. 317.)   
[899]Martin Plesinger. The Total Least SquaresProblem and Reduction of Data in $A X \approx B$ Ph.D. thesis,Technical University of Liberec, Czech Republic,2008.(Cited on pp.196,305.)   
[900] L.F. Portugal, J. J. Judice,and L. N. Vicente. A comparison of block pivoting and interior-point algorithms for linear least squares problems with nonnegative variables. Math. Comp., 63:625-643, 1994.(Cited on p. 419.)   
[901] A. Pothen. Sparse Nul Bases and Marriage Theorems.Ph.D. thesis, Cornell University, Ithaca, NY,1984. (Cited on p. 265.)   
[902] Alan Pothen and C.J. Fan. Computing the block triangular form of a sparse matrix. ACM Trans. Math. Softw.,16:303-324,1990. (Cited on pp.265,265.)   
[903] M. J. D.Powelland J. K. Reid. On applying Householder's method to linear least squares problems. In A. J. H. Morell, editor,Proceedings of the IFIP Congress 68,pages 122-126. North-Hollnd, Amsterdam,1969.(Cited on p. 130.)   
[904] Srikara Pranesh．Low precision floating-point formats: The wild west of computer arithmetic. SIAM News,52:12,2019. (Cited on p. 32.)   
[905] Vaughan Pratt. Direct least-squares fiting of algebraic surfaces. ACM SIGGRAPH Comput. Graphics,21:145-152,1987. (Cited on p. 411.)   
[906] Chiara Puglisi. Modification of the Householder method based on the compact WY representation. SIAMJ. Sci. Statist. Comput.,13:723-726,1992.(Cited on p. 109.)   
[907] Chiara Puglisi. QR Factorization of Large Sparse Overdetermined and Square Matrices with the Multifrontal Method in a Multiprocessing Environment.Ph.D.thesis,Institut National Polytechnique de Toulouse, Toulouse,France,1993.(Cited on p. 258.)   
[908] Charles M. Rader and Allen O. Steinhardt. Hyperbolic Householder transforms. SIAM J. Matrix Anal. Appl.,9:269-290,1988. (Cited on p. 137.)   
[909] Rui Ralha. One-sided reduction to bidiagonal form. Linear Algebra Appl., 358:219-238,2003. (Cited on p. 194.)   
[910] Hakan Ramsin and Per-A. Wedin. A comparison of some algorithms for the nonlinear least squares problem.BIT Numer. Math.,17:72-90,1977. (Cited on p.398.)   
[911] Bhaskar D.Rao and Kenneth Kreutz-Delgado.An affine scaling methodology for best basis selection. IEEE Trans. Signal Process,47:187-200,1999. (Cited on p. 429.)   
[912] R.C.Rao.Linear Statistical Inference and Its Applications,John Wiley,New York,second edition, 1973.(Cited on p. 128.)   
[913] R. K.Rao and P. Yip.Discrete Cosine Transforms.Academic Press,New York,1990. (Cited on p. 237.)   
[914] Lord Rayleigh. On the calculation of the frequency of vibration of a system in its gravest mode with an example from hydrodynamics.Philos Mag.,47:556-572,1899. (Cited on p. 376.)   
[915] Shaked Regev and Michael A. Saunders. Ssai: A Symmetric Approximate Inverse Preconditioner for the Conjugate Gradient Methods PCG and PCGLS. Tech. Report,Working Paper, SOL and ICME, Stanford University, Stanford, CA,2022. (Cited on p. 314.)   
[916] Lothar Reichel.Fast QR decomposition of Vandermonde-like matrices and polynomial least squares approximation. SIAM J. Matrix Anal. Appl.,12:552-564, 1991. (Cited on pp. 230, 238, 239.）   
[917] Lothar Reichel and William B. Gragg. FORTRAN subroutines for updating the QR decomposition. ACM Trans.Math. Softw.,16:369-377,1990. (Cited on p. 150.)   
[918] Lothar Reichel and Qiang Ye.A generalized LSQR algorithm. Numer: Linear Algebra Appl., 15:643-660,2008. (Cited on p. 305.)   
[919] John K. Reid. A note on the least squares solution of a band system of linear equations by Householder reductions. Comput J.,10:188-189,1967. (Cited on p. 188.)   
[920] John K. Reid. A note on the stability of Gaussian elimination. J. Inst. Math. Appl., 8:374-375, 1971. (Cited on p. 281.)   
[921] John K. Reid. Implicit scaling of linear least squares problems. BIT Numer Math., 40:146-157, 2000.(Cited on p. 160.)   
[922] Christian H.Reinsch. Smoothing by spline functions. Numer Math.,10:177-183,1967. (Cited on p. 189.)   
[923] Christian H. Reinsch. Smoothing by spline functions II. Numer: Math.,16:451-454,1971. (Cited on pp. 169,176.)   
[924] Rosemary A.Renaut and Hongbin Guo.Eficient algorithms for solution of regularized total least squares problems. SIAM J. Matrix Anal. Appl.,26:457-476,2005. (Cited on p. 226.)   
[925] J. R. Rice. PARVEC Workshop on Very Large Least Squares Problems and Supercomputers. Tech. Report CSD-TR 464,Purdue University,West Lafayette,IN,1983.(Cited on p. 206.)   
[926] John R. Rice.A theory of condition. SIAM J. Numer. Anal.,3:287-310,1966. (Cited on p. 62.)   
[927] John R. Rice and Karl H. Usow. The Lawson algorithm and extensions. Math. Comp.,24:118-127, 1968. (Cited on p. 423.)   
[928] J.L. Rigal and J. Gaches. On the compatibilityof a given solution with the data of a linear system. J. Assoc. Comput. Mach.,14:543-548,1967. (Cited on p. 97.)   
[929] J. D. Riley. Solving systems of linear equations with a positive definite symmetric but posibly ill-conditioned matrix. Math.Tables Aids. Comput.,9:96-101,1956.(Cited on pp.177,326.)   
[930] Walter Ritz. Uber eine neue Methode zur Losung gewisser Variationsprobleme der mathematischen Physik. J. Reine Angew. Math.,136:1-61,1908. (Cited on p. 376.)


<!-- chunk 0008: pages 491-510 -->
[931] Marielba Rojas, Sandra A. Santos,and Danny C.Sorensen. Algorithm 873:LSTRS: MATLAB software for large-scale trust-region subproblems and regularization. ACM Trans. Math. Softw., 24:11:1-11.28,2008. (Cited on pp. 182,375.)   
[932]Marielba Rojas and Danny C. Sorensen.A trust-region approach to the regularization of largescale discrete forms of ill-posed problems. SIAM J. Sci. Comput.,23:1842-1860,2002.(Cited on p. 182.)   
[933] Marielba Rojas and Trond Steihaug. An interior-point trust-region-based method for large-scale non-negative regularization. Inverse Problems,18:1291-1307,2002. (Cited on p. 419.)   
[934] Vladimir Rokhlin and Mark Tygert.A fast randomized algorithm for overdetermined linear least squares regresson. Proc. Natl. Acad. Sci. USA,105:13212-13217,2008.(Cited on p. 319.)   
[935] D.J. Rose. A graph-theoretic study of the numerical solution of sparse positive definite systems of linear equations. In R. C. Read, editor, Graph Theory and Computing, pages 183-217, Academic Press,New York,1972. (Cited on pp. 249, 251.)   
[936] J. Ben Rosen, Haesun Park,and John Glick.Total least norm problems formulation and solution for structured problems. SIAM J. Matrix Anal. Appl.,17:110-126,1996. (Cited on pp. 227,411.)   
[937] Roman Rosipal and Nicole Krämer. Overview and recent advances in partial least squares. In C. Saunders et al.,eds.,Proceedings of International Statistics and Optimization Perspectives Workshop,“Subspace,Latent Structure and Feature Selection,”volume 394O of Lecture Notes in Computer Science, pages 34-51. Springer, Berlin, 2006. (Cited on p. 203.)   
[938] Miroslav Rozloznik,Alicja Smoktunowicz, Miroslav Tüma, and Jiri Kopal. Numerical stability of orthogonalization methods with a non-standard inner product. BIT Numer. Anal., 52:1035-1058, 2012. (Cited on p. 122.)   
[939] Axel Ruhe.Accelerated Gauss-Newton algorithms for nonlinear least squares problems. BIT Numer Math.,19:356-367,1979. (Cited on p. 395.)   
[940] Axel Ruhe.Numerical aspects of Gram-Schmidt orthogonalization of vectors.Linear Algebra Appl.,52/53:591-601,1983. (Cited on p. 71.)   
[941] Axel Ruhe. Rational Krylov: A practical algorithms for large sparse nonsymmetric matrix pencils. SIAM J. Sci. Comput.,19:1535-1551,1998. (Cited on p. 376.)   
[942] Axel Ruhe and Per Ake Wedin. Algorithms for separable nonlinear least squares problems. SIAM Rev.,22:318-337,1980. (Cited on pp. 404,406.)   
[943] Siegfried M. Rump. INTLAB - INTerval LABoratory. In Tibor Csendes, editor, Developments in Reliable Computing, pages 77-104. Kluwer Academic Publishers, Dordrecht,1999.(Cited on p. 34.)   
[944] Siegfried M. Rump.Fast and parallel interval arithmetic. BIT Numer: Math.,39:534-554,1999. (Cited on p. 34.)   
[945] Siegfried M. Rump. Il-conditioned matrices are componentwise near to singularity. SIAM Review, 41:102-112,1999. (Cited on p. 31.)   
[946] Heinz Rutishauser. Der Quotienten-Diferenzen-Algorithmus. Z. Angew. Math. Phys.,5:233-251, 1954. (Cited on p. 351.)   
[947] Heinz Rutishauser. Solution of eigenvalue problems with the LR-transformation.Nat. Bur: Standards Appl. Math. Ser,49:47-81,1958. (Cited on p. 339.)   
[948]Heinz Rutishauser. Theory of gradient methods. In M.Engeli, Th. Ginsburg,H. Rutishauser, and E. Stiefel, editors, Refined Methods for Computation of the Solution and the Eigenvalues of Self-Adjoint Boundary Value Problems,pages 24-50. Birkhäuser, Basel/Stuttgart,1959. (Cited on p. 326.)   
[949] Heinz Rutishauser. On Jacobi rotation patterns. In Proceedings of Symposia in Applied Mathematics,Vol. XV: Experimental Arithmetic,High Speed Computing and Mathematics.American Mathematical Society,Providence,RI, pages 219-239,1963. (Cited on p.341.)   
[950] Heinz Rutishauser. The Jacobi method for real symmetric matrices. In F.L. Bauer et al., editors, Handbook for Automatic Computation. Vol. II, Linear Algebra,pages 2O1-211. Springer, New York,1971. Prepublished in Numer Math.,9:1-10,1966. (Cited on p. 353.)   
[951] Heinz Rutishauser. Description of ALGOL 60. Handbook for Automatic Computation. Vol. I, Part a. Springer-Verlag, Berlin,1967. (Cited on p. 69.)   
[952] Heintz Rutishauser. Once again: The least squares problem. Linear Algebra Appl.,1:479-488, 1968. (Cited on p. 177.)   
[953] Yousef Saad. Preconditioning techniques for nonsymmetric and indefinite linear systems. J. Comput. Appl. Math.,24:89-105,1988. (Cited on p. 313.)   
[954] Yousef Saad. Numerical Methods for Large Eigenvalue Problems.Halstead Press,New York,1992. (Cited on p. 375.)   
[955] Yousef Saad.A flexible inner-outer preconditioned GMRES algorithm.SIAM J. Sci. Statist. Comput.,14:461-469,1993.(Cited on pp.303,304.)   
[956] Yousef Saad. Iterative Methods for Sparse Linear Systems. PVS Publishing Company, Boston, MA,1996. (Cited on pp.281,284.)   
[957] Yousef Saad. Iterative Methods for Sparse Linear Systems. SIAM, Philadelphia, second edition, 2003.(Cited on p. 269.)   
[958] Yousef Saad. Numerical Methods for Large Eigenvalue Problems,volume 66of Classics in Applied Math.,SIAM,Philadelphia,revised edition,2O11. Updated edition of the work first published by Manchester University Press,1992. (Cited on p. 375.)   
[959] Youcef Saad and Martin H Schultz. GMRES: A generalized minimal residual algorithm for solving nonsymmetric linear systems. SIAM J. Sci. Statist. Comput.,7:856-869,1986. (Cited on p. 301.)   
[960] Yousef Saad and Henk A.van der Vorst. Iterative solution of linear systems in the 2Oth century. J. Comput. Appl. Math.,123:1-33,2000. (Cited on p. 269.)   
[961] Y. Saad, M. Yeung, J. Erhel,and F. Guyomarc'h.A deflated version of the conjugate gradient algorithm. SIAM J. Sci. Comput.,21:1909-1926,2000. (Cited on pp.312,336, 336.)   
[962] Douglas E. Salane.A continuation approach for solving large-residual nonlinear least squares problems. SIAM J. Sci. Statist. Comput., 8:655-671,1987. (Cited on p. 402.)   
[963] Michael A. Saunders. Large-Scale Linear Programming Using the Cholesky Factorization. Tech. Report CS252, Computer Science Department, Stanford University, Stanford,CA,1972.(Cited on pp. 146,146.)   
[964] Michael A. Saunders. Sparse least squares by conjugate gradients: A comparison of preconditioning methods. InJ.F. Gentleman, editor, Proc.Computer Science and Statistics 12th Annual Sym-posium on the Interface, pages 15-20. University of Waterloo, Canada,1979. (Cited on p. 317.)   
[965] Michael A. Saunders. Solution of sparse rectangular systems using LSQR and Craig. BIT Numer. Math.,35:588-604,1995. (Cited on pp. 292,328.)   
[966] M. A. Saunders,H.D. Simon,and E.L. Yip. Two conjugate-gradient-type methods for unsymmetric systems. SIAM J. Numer. Anal.,25:927-940,1988. (Cited on pp. 305,331.)   
[967] Werner Sautter. Error analysis of Gauss elimination for the best least squares solution. Numer: Math.,30:165-184,1978. (Cited on p. 85.)   
[968] Berkant Savas and Lek-Heng Lim. Quasi-Newton methods on Grassmannians and multilinear approximations of tensors. SIAM J. Sci. Comput.,32:3352-3393,2010. (Cited on p. 217.)   
[969] Robert Schaten.Norm Ideals of Completely Continuous Operators.Ergebnisse der Mathematik und ihrer Grenzgebiete,Neue Folge. Springer Verlag,Berlin,1960. (Cited on p. 22.)   
[970] K. Schittkowski. Solving constrained nonlinear least squares problems by a general purpose SQPmethod. In K.-H. Hoffmann,J.B. Hiriart-Urruty, C.Lemaréchal,and J. Zowe,editors,Trends in Mathematical Optimization,volume 84 of International Series of Numerical Mathematics,pages 49-83.Birkhäuser-Verlag,Basel, Switzerland,1985.(Cited on p.162.)   
[971] Erhard Schmidt. Zur Theorie der linearen und nichtlinearen Integralgleichungen.1 Teil.Entwicklung willkurlicher Funktionen nach Systemen vorgeschriebener. Math. Ann., 63:433-476,1907. (Cited on p. 63.)   
[972] Erhard Schmidt. Uber die Auflösung linearer Gleichungen mit unendlich vielen Unbekannten. Rend. Circ. Mat. Palermo. Ser.1,25:53-77,1908. (Cited on p. 63.)   
[973] W. Schonemann. A generalized solution of the orthogonal Procrustes problem． Psychometrica, 31:1-10,1966. (Cited on p. 386.)   
[974] Robert S. Schreiber. A new implementation of sparse Gaussian elimination. ACM Trans. Math. Softw.,8:256-276,1982. (Cited on p. 250.)   
[975] Robert Schreiber and Charles Van Loan.A storage efcient WY representation for products of Householder transformations. SIAM J. Sci. Statist. Comput.,10:53-57,1989. (Cited on p.106.)   
[976] Guinther Schulz. Iterative Berechnung der reziproken Matriz. Z. Angew. Math. Mech.,13:57-59, 1933.(Cited on p. 379.)   
[977] H. R. Schwarz. Tridiagonalization of a symmetric band matrix. Numer. Math.,12:231-241,1968. Also appears in [1123, pp.273-283]. (Cited on p. 341.)   
[978] H.R.Schwarz, Hans Rutishauser,and Eduard Stiefel. Matrizen-Numerik.Teubner Verlag,Stuttgart, 1986. (Cited on p. 62.)   
[979] Hubert Schwetlick.Nonlinear parameter estimation: Models,criteria and estimation.In D.F. Griffths and G.A.Watson, editors,Numerical Analysis 1991. Proceedings of the 14th Dundee Conference on Numerical Analysis, volume 260 of Pitman Research Notes in Mathematics, pages 164-193.Longman Scientific and Technical, Harlow, UK,1992.(Cited on p. 402.)   
[980] Hubert Schwetlick and V. Tiler. Numerical methods for estimating parameters in nonlinear models with errors in the variables. Technometrics,27:17-24,1985. (Cited on p. 410.)   
[981] Hubert Schwetlick and Volker Tiler. Nonstandard scaling matrices for trust region Gauss-Newton methods. SIAMJ. Sci. Statist. Comput.,10:654-670,1989.(Cited on p. 410.)   
[982] Hugo D. Scolnik. On the solution of non-linear least squares problems. In C. V.Freiman, J.E. Griffith,and J.L.Rosenfeld,editors,Proc. IFIP Congress 71. Vol.2,pages1258-1265.North-Holland, Amsterdam,1972.(Cited on p. 405.)   
[983] Jennifer Scot. On using Cholesky-based factorizations and regularization for solving rank-deficient sparse linear least-squares problems. SIAM J. Sci. Comput., 39:C319-C339,2017. (Cited on p. 315.)   
[984] Jennifer A. Scott and Miroslav Tuma.The importance of structure in incomplete factorization preconditioners. BIT Numer: Math.,51:385-404,2011. (Cited on p. 310.)   
[985] Jennifer A. Scottand Miroslav Tuma.HSL_MI28:An efficient and limited-memory incomplete Cholesky factorization code.ACM Trans. Math. Softw.,40:Article 24,2014. (Cited on pp. 311, 315.)   
[986] Jennifer Scot and Miroslav Tuma. On positive semidefinite modification schemes for incomplete Cholesky factorization. SIAM J. Sci. Comput.,36:A609-A633,2014. (Cited on p. 311.)   
[987] Jennifer Scott and Miroslav Tüma.Preconditioning of linear least squares by robust incomplete factorization for implicitly held normal equations. SIAM J. Sci. Comput.,38:C603-C623,2016. (Cited on p. 315.)   
[988] Jennifer Scott and Miroslav Tuma. Solving mixed sparse-dense linear least-squares problems by preconditioned iterative methods. SIAM J. Sci. Comput.,39:A2422-A2437,2017．(Cited on p. 263.)   
[989] Jennifer A. Scott and Miroslav Tüma.A Schur complement approach to preconditioning sparse least squares with some dense rows. Numer: Algor,79:1147-1168,2018. (Cited on p.263.)   
[990] Jennifer A. Scott and Miroslav Tima. Sparse stretching for solving sparse-dense linear leastsquares problems. SIAM J. Sci. Comput., 41:A1604-A1625,2019. (Cited on p. 263.)

[9y1] jenner A. Scou and Miroslav iuma. Aigorunms jor Sparse Linear Systems. Necas Center Series. Birkhäuser, Cham,2023.(Cited on p. 244.)   
[992] Shayle R. Searle.Extending some results and proofs for the singular linear model. Linear Algebra Appl.,210:139-151,1994. (Cited on p.128.)   
[993] V.de Silva and Lek-Heng Lim. Tensor rank and the il-osedness of the best low rank approximation.SIAM J. Matrix Anal. Appl.,30:1084-1127,2008. (Cited on pp.215,216,218.) [994] Diana Sima,Sabine Van Huffel,and Gene H.Golub.Regularized total least squares based on quadratic eigenvalue solvers. Linear Algebra Appl.,44:793-812, 2004. (Cited on p. 225.)   
[995] Horst D. Simon. Analysis of the symmetric Lanczos algorithm with reorthogonalization methods. Linear Algebra Appl.,61:101-131,1984. (Cited on p. 298.)   
[996] Horst D.Simon and Hongyuan Zha.Low-rank matrix approximation using the Lanczos bidiagonalization process with applications. SIAM J. Sci. Comput.,21:2257-2274,2000. (Cited on pp. 203, 298, 371.)   
[997] Valeria Simoncini and Daniel B.Szyld. On the occurrence of superlinear convergence of exact and inexact Krylov subspace methods. SIAM Rev.,47:247-272,2005. (Cited on p. 299.)   
[998] Valeria Simoncini and Daniel B. Szyld. Recent computational developments in Krylov subspace methods for linear systems. Numer: Linear Algebra Appl.,14:1-59,2007. (Cited on p. 337.)   
[999] Lennart Simonsson. Subspace Computations via Matrix Decompositions and Geometric Optimization.Ph.D.thesis,Linkoping Studies in Science and Technology No.1052,Linkoping, Sweden, 2006.(Cited on p.155.)   
[1000] Robert D.Skeel. Scaling for numerical stability in Gaussian elimination. J. Assoc. Comput. Mach., 26:494-526,1979. (Cited on p. 31.)   
[1001]Robert D.Skeel. Iterative refinement implies numerical stability for Gaussian elimination. Math. Comp.,35:817-832,1980. (Cited on p. 103.)   
[1002] Gerard L.G. Sleijpen and Henk A.van der Vorst.A Jacobi-Davidson iteration method for linear eigenvalue problems. SIAM J. Matrix Anal. Appl.,17:401-425,1996.(Cited on pp.374,375, 376.)   
[1003] Gerard L. G. Sleijpen and Henk A.van der Vorst.A Jacobi-Davidson iteration method for linear eigenvalue problems.SIAM Rev.,42:267-293,2000. (Cited on p. 375.)   
[1004] S.W. Sloan. An algorithm for profile and wavefront reduction of sparse matrices. Int.J. Numer. Methods Eng.,23:239-251,1986. (Cited on p. 251.)   
[1005]B.T.Smith,J.M. Boyle, Jack J. Dongarra,B.S. Garbow, Y. Ikebe,Virginia C. Klema,and Cleve B. Moler. Matrix Eigensystems Routines-EISPACK Guide, volume 6 of Lecture Notes in Computer Science. Springer,New York,second edition,1976.(Cited on p. 113.)   
[1006] Alicja Smoktunowicz, Jesse L. Barlow,and Julien Langou.A note on the error analysis of the classical Gram-Schmidt. Numer. Math.,105:299-313,2006. (Cited on p. 63.)   
[1007] Inge Soderkvist.Perturbation analysis of the orthogonal Procrustes problem.BIT Numer. Math., 33:687-694,1993. (Cited on p. 387.)   
[1008] Inge Soderkvist and Per-Ake Wedin.Determining the movements of the skeleton using welconfigured markers. J. Biomech.,26:1473-1477,1993. (Cited on p. 386.)   
[1009] Inge Soderkvist and Per-Ake Wedin. On condition numbers and algorithms for determining a rigid body movement. BIT Numer: Math.,34:424-436,1994. (Cited on p. 386.)   
[1010] Torsten Soderstrom and G. W. Stewart. On the numerical properties of an iterative method for computing the Moore-Penrose generalized inverse. SIAM J. Numer Anal.,11:61-74,1974. (Cited on p. 380.)   
[1011]D.C.Sorensen.Implicit application of polynomial filters in a $k$ -step Arnoldi method.SIAMJ. Matrix Anal. Appl.,13:357-385,1992. (Cited on pp. 372,373.)   
[1056] Kunio Tanabe.Projection method for solving a singular system of linear equations and its applications. Numer Math.,17:203-214,1971. (Cited on p. 270.)   
[1057] Robert Tarjan. Depth-first search and linear graph algorithms.SIAM J. Comput.,1:146-160,1972. (Cited on p. 264.)   
[1058] R.P. Tewarson. A computational method for evaluating generalized inverses. Comput. J.,10:411- 413,1968. (Cited on pp. 88, 88.)   
[1059] Stephen J. Thomas and R. V. M.Zahar. Efcient orthogonalization in the $M$ norm. Congr. Numer., 80:23-32,1991. (Cited on p. 122.)   
[1060] Stephen J. Thomas andR. V.M. Zahar. An analysis of orthogonalization in eliptic norms.Congr: Numer,86:193-222,1992. (Cited on p. 122.)   
[1061] Robert Tibshirani. Regresson shrinkage and selection via the LASSO.Royal Statist. Soc. B, 58:267-288,1996. (Cited on p. 425.)   
[1062] A. N. Tikhonov and V.Y Arsenin. Solutions of Ill-Posed Problems.Winston, Washington D.C., 1977. (Cited on p. 175.)   
[1063] Andrei N. Tikhonov. Solution of incorrectly formulated problems and the regularization method. Soviet Math. Dokl.,4:1035-1038,1963. (Cited on p. 175.)   
[1064] W. F. Tinney and J. W. Walker. Direct solution of sparse network equations by optimally ordered triangular factorization. Proc.IEEE,55:1801-1809,1967. (Cited on p.251.)   
[1065] M. Tismenetsky. A new preconditioning technique for solving large sparse linear systems.Linear Algebra Appl.,154/156:331-353,1991. (Cited on p. 310.)   
[1066] Ph.L. Toint. On large scale nonlinear least squares calculations. SIAM J. Sci. Statist. Comput., 8:416-435,1987. (Cited on p. 400.)   
[1067] Philippe L.Toint. VE10AD a Routine for Large-Scale Nonlinear Least Squares. Harwell Subroutine Library,AERE Harwell, Oxfordshire,UK,1987.(Cited on p. 400.)   
[1068] Lloyd N. Trefethen and David Bau,II. Numerical Linear Algebra.SIAM,Philadelphia,1997. (Cited on p. 60.)   
[1069] Michael J. Tsatsomeros.Principal pivot transforms.Linear Algebra Appl.,307:151-165,2000. (Cited on p. 136.)   
[1070] L.R.Tucker. Some mathematical notes on three-mode factor analysis.Psychometrica,31:279-311, 1966.(Cited on pp. 216, 217.)   
[1071]Madelaine Udel and Alex Townsend. Why are big data matrices approximately low rank? SIAM J. Math. Data Sci.,1:144-160,2019. (Cited on p. 24.)   
[1072] M. H. van Benthem and M.R. Keenan. A fast non-negativity-constrained least squares algorithm. J.Chemometrics,18:441-450,2004. (Cited on p. 168.)   
[1073]A.van der Sluis. Stability of the solutions of linear least squares problems.Numer Math.,23:241- 254,1975. (Cited on p. 27.)   
[1074] A.van der Sluis and G. Veltkamp.Restoring rank and consistency by orthogonal projection. Linear Algebra Appl.,28:257-278,1979. (Cited on p. 26.)   
[1075] Henk A.van der Vorst. Iterative Krylov Methods for Large Linear Systems. Number 13 in Cambridge Monographs on Applied and Computational Mathematics.Cambridge University Press, Cambridge,UK,2003.(Cited on pp.269,285.)   
[1076] Sabine Van Hufel,Haesun Park,and J. Ben Rosen. Formulation and solution of structured total least norm problems for parameter estimation. IEEE Trans. Signal Process.,44:2464-2474,1996. (Cited on p. 227.)   
[1077] Sabine Van Huffel and Joos Vandewalle. The Total Least Squares Problem: Computational Aspects and Analysis. SIAM,Philadelphia,1991. (Cited on pp.218,220,222,223,223.)   
[1101] Xiaoge Wang. Incomplete Factorization Preconditioning for Least Squares Problems. Ph.D.thesis, Department of Mathematics, University of Illinois at Urbana-Champaign, Urbana, IL,1993.(Cited on p. 312.)   
[1102] Xiaoge Wang, Kyle A. Gallivan, and Randall Bramley. CIMGS: An incomplete orthogonal factorization preconditioner. SIAM J. Sci. Comput.,18:516-536,1997. (Cited on p. 312.)   
[1103] David S. Watkins.Understanding the QR algorithm． SIAM Rev.,24:427-440,1982.(Cited on p. 368.)   
[1104] David S.Watkins.Francis's algorithm.Amer: Math. Monthly,118:387-403,2011．(Cited on p. 348.)   
[1105] Joseph Henry Maclagan Wedderburn. Lectures on Matrices,Dover Publications, Inc., New York, 1964. Unabridged and unaltered republication of the work first published by the American Mathematical Society,New York,1934 as volume XVII in their Colloquium Publications.(Cited on p. 139.)   
[1106] Per-Ake Wedin. On Pseudo-Inverses of Perturbed Matrices.Tech. Report,Department of Computer Science,Lund University, Sweden,1969. (Cited on p. 26.)   
[1107] Per-Ake Wedin. Perturbation bounds in connection with the singular value decomposition. BIT Numer: Math.,12:99-111,1972. (Cited on pp.22,393.)   
[1108] Per-Ake Wedin. Perturbation theory for pseudo-inverses.BIT Numer: Math.,13:217-232,1973. (Cited on pp. 26, 27, 28.)   
[1109] Per-Ake Wedin. On the Gauss-Newton Methodfor the Nonlinear Least Squares Problems. Working Paper 24, Institute for Applied Mathematics, Stockholm, Sweden,1974. (Cited on p. 394.)   
[1110] Per-Ake Wedin. Perturbation Theory and Condition Numbers for Generalized and Constrained Linear Least Squares Problems. Tech. Report UMINF-125.85, Institute of Information Processing, University of Umea, Sweden,1985.(Cited on pp.119,119,128,160.)   
[1111] Musheng Wei. Algebraic relations between the total least squares and least squares problems with more than one solution. Numer: Math.,62:123-148,1992. (Cited on p.226.)   
[1112] Musheng Wei. The analysis for the total least squares problem with more than one solution. SIAM J. Matrix Anal. Appl.,13:746-763,1992. (Cited on p. 222.)   
[113]Musheng Wei. Perturbation theory for the rank-deficient equality constrained least squares problem. SIAM J. Numer: Anal.,29:1462-1481, 1992. (Cited on p. 160.)   
[1114] Yimin Wei and Weiyang Ding. Theory and Computation of Tensors: Multi-Dimensional Arrays. Academic Press,New York,2016. (Cited on p. 218.)   
[1115] Yimin Wei, Pengpeng Xie,and Liping Zhang. Tikhonov regularization and randomized GSVD. SIAM J. Matrix Anal. Appl.,37:649-675,2016. (Cited on p. 334.)   
[1116] P. R. Weil and P. C. Kettler. Rearranging matrices to block-angular form for decomposition (and other) algorithms.Management Sci.,18:98-108,1971. (Cited on p.209.)   
[1117] Helmut Wielandt. Das Iterationsverfahren bei nicht selbstadjungierten linearen Eigenwertaufgaben. Math. Z.,50:93-143,1944. (Cited on p. 365.)   
[118] James H.Wilkinson.Rounding Errors in Algebraic Processes.Prentice-Hall,Englewood Clifs, NJ, 1963. (Cited on p.101.)   
[1119] James H. Wilkinson.The Algebraic Eigenvalue Problem. Clarendon Press, Oxford, UK,1965. (Cited on p. 47.)   
[1120] James H. Wilkinson. Error analysis of transformations based on the use of matrices of the form $I - 2 x x ^ { \mathrm { H } }$ InL.B.Rall,editor,ErrorinDigitalComputation,pages77-101.John Wiley,New York,1965.(Cited on pp.34,51,350.)   
[1121] James H.Wilkinson.A priori error analysis of algebraic processes.In Proc.Internat. Congr Math. (Moscow,1966),Izdat.“Mir”,Moscow,1968, pp. 629-640. (Cited on pp. 43,345.)   
[1122] James H. Wilkinson. Modern error analysis. SIAM Rev.,13:548-568,1971. (Cited on p. 62.)   
[1123] James H. Wilkinson and C.Reinsch,eds. Handbook for Automatic Computation. Volume I: Linear Algebra.Springer,Berlin,1971.(Cited on pp.56,113,184,478.)   
[1124] Paul R. Willems and Bruno Lang. The ${ \bf M R } ^ { 3 }$ GK algorithm for the bidiagonal SVD. ETNA,39:1-21, 2012.(Cited on p. 352.)   
[1125] Paul R. Willems, Bruno Lang,and Christof Vomel. Computing the bidiagonal SVD using multiple relatively robust representations. SIAM J. Matrix Anal.Appl.,28:907-926,2006.(Cited onp. 352.)   
[1126]T.J. Willmore.An Introduction to Differential Geometry.Clarendon Press,Oxford, UK,1959. (Cited on p. 394.)   
[1127] Herman Wold. Estimation of principal components and related models by iterative least squares. In P. R. Krishnaiah, editor, Multivariate Analysis, pages 391-420.Academic Press, New York,1966. (Cited on p. 200.)   
[1128] S. Wold, A. Ruhe,H. Wold,and W. J. Dunn.The colinearity problem in linear regression. The partial least squares (PLS) approach to generalized inverses. SIAM J. Sci. Statist. Comput.,5:735- 743,1984. (Cited on p. 200.)   
[1129] Svante Wold,Michael Sjostrom,and Lennart Eriksson.PLS-regression: A basic tool ofchemometrics. Chemom. Intell.Lab. Syst.,58:109-130,2001. (Cited on p. 203.)   
[1130] Y. K. Wong. An application of orthogonalization process to the theory of lest squares. Ann. Math. Statist., 6:53-75,1935. (Cited on p. 64.)   
[1131] Max A.Woodbury. Inverting Modified Matrices. Memorandum Report 42, Statistical Research Group,Princeton,1950. (Cited on p. 138.)   
[1132] Stephen J. Wright. Stability of linear equation solvers in interior-point methods. SIAM J. Matrix Anal. Appl.,16:1287-1307,1995. (Cited on p. 129.)   
[1133] Stephen J.Wright.Primal-Dual Interior-Point Methods.SIAM,Philadelphia,1997．(Cited on p. 419.)   
[1134] Pengpeng Xie, Hua Xiang,and Yimin Wei. A contribution to perturbation analysis for total least squares problems. Numer Algorithms,75:381-395,2017. (Cited on p. 226.)   
[1135] Andrew E.Yagle.Non-iterative Reweighted-Norm Least-Squares Local $\ell _ { 0 }$ Minimization for Sparse Solution to Underdetermined Linear Systems of Equations. Tech. Report Preprint, Department of EECS,The University of Michigan,Ann Arbor,2008. (Cited on p. 428.)   
[1136] Yusaku Yamamoto,Yuji Nakatsukasa, Yuka Yanagisawa,and Takeshi Fukaya.Roundoff error analysis of the Cholesky QR2 algorithm. ETNA,44:306-326,2015.(Cited on p.213.)   
[1137] Ichitaro Yamazaki,Stanimire Tomov,and Jack Dongarra.Mixed-precision Cholesky QR factorization and its case studies on multicore CPU with multiple GPUs. SIAM J. Sci. Comput., 37:C307- C330,2015. (Cited on p. 213.)   
[1138] L. Minah Yang,Alyson Fox,and Geoffrey Sanders.Rounding error analysis of mixed precision block Householder QR algorithm. ETNA,44:306-326,2020.(Cited on p.109.)   
[1139] Sencer Nuri Yeralan, Timothy A.Davis,Wissam M. Sid-Lakhdar,and Sanjay Ranka.Algorithm 980: Sparse QR factorization on the GPU. ACM Trans. Math. Softw.,44:Article 17,2017.(Cited on p. 112.)   
[1140] K. Yoo and Haesun Park. Accurate downdating of a modified Gram-Schmidt QR decomposition. BIT Numer Math.,36:166-181,1996. (Cited on pp.151,152.)   
[1141]David M. Young.Iterative Solution of Large Linear Systems. Dover, Mineola, NY, 2003. Unabridged republication of the work first published by Academic Press,New York-London,1971. (Cited on pp.270, 275,277,278.)   
[1142] Jin Yun Yuan.Iterative Methods for the Generalized Least Squares Problem.Ph.D.thesis, Instituto de Matematica Pure e Aplicada, Rio de Janeiro, Brazil,1993.(Cited on p. 318.)   
[1143] M. Zelen. Linear estimation and related topics. In John Todd,editor, Survey of Numerical Analysis, pages 558-584.McGraw-Hill,New York,1962. (Cited on p. 4.)   
[1144] Hongyuan Zha. A two-way chasing scheme for reducing a symmetric arowhead matrix to tridiagonal form. J. Num. Linear Algebra Appl.,1:49-57,1992. (Cited on p. 362.)   
[1145]Hongyuan Zha. Computing the generalized singular values/vectors of large sparse or structured matrix pairs. Numer: Math.,72:391-417,1996. (Cited on p. 333.)   
[1146] Hongyuan Zha and Horst D. Simon. On updating problems in latent semantic indexing. SIAM J. Sci. Comput.,21:782-791,1999． (Cited on p. 360.)   
[1147] Shaoshuai Zhang and Panruo Wu. High Accuracy Low Precision QR Factorization and Least Squares Solver on GPU with TensorCore.Preprint. https://arxiv.org/abs/1912 .05508, 2019. (Cited on p. 311.)   
[1148] Zhenyue Zhang,Hongyuan Zha, and Wenlong Ying. Fast parallelizable methods for computing invariant subspaces of Hermitian matrices.J. Comput. Math.,25:583-594,2007. (Cited on p. 382.)   
[1149]Liangmin Zhou,Lijing Lin, Yimin Wei,and Sangzheng Qiao. Perturbation analysis and condition number of scaled total least squares problems.Numer. Algorithms,51:381-399,2009.(Cited on p. 226.)   
[1150] Ciyou Zhu,Richard H. Byrd,Peihuang Lu,and Jorge Nocedal. Algorithm 778: L-BFGS-B: Fortran subroutines for large-scale bound-constrained optimization.ACM Tran. Math. Softw.,23:550-560, 1997. (Cited on p. 420.)   
[1151] Zahari Zlatev. Comparison of two pivotal strategies in sparse plane rotations. Comput. Math. Appl, 8:119-135,1982. (Cited on p. 255.)   
[1152] Zahari Zlatev and H.Nielsen. LLSSOl-A Fortran Subroutine for Solving Least Squares Problems (User's Guide). Tech.Report 79-O7,Institute of Numerical Analysis, Technical University of Denmark,Lyngby,Denmark,1979. (Cited on p. 258.)   
[1153] Zahari Zlatev and Hans Bruun Nielsen. Solving large and sparse linear least-squares problems by conjugate gradient algorithms. Comput. Math. Appl.,15:185-202,1988. (Cited on p. 313.)   
[1154]E.I. Zolotarev.Application of eliptic functions to questions of functions deviating least and most from zero.Zap.Imp.Akad. Nauk St.Petersburg,30,1877.Reprinted in his Collected Works,Vol. II, Izdat. Akad. Nauk SSSR,Moscow,1932, pp.1-59 (in Russian). (Cited on p. 382.)

# Index

active-set methods,162-168   
acute perturbation, 25   
adjacency graph of matrix, 247   
adjacency set, 247   
algebraic reconstruction technique, 274   
algorithm band Cholesky,187 Bidiag2-PLS, 202 CGLS,282, 327 CGME,283 CGS2, 70 Cholesky, 42 conjugate gradient method, 280 elliptic MGS QR,120 extended CGLS,330 FGMRES with variable right preconditioning, 303 GCGLS,282 GMRES with right preconditioning,303 Gram-Schmidt classical, 60 modified, 61, 62 Hager's condition estimation, 96 Householder QR,53,54 Householder reflector, 47 IMGS factorization,312 IRLS for compressed sensing,428 IRLS for overdetermined systems,424 iterative refinement,100, 102,105 least-norm by MGS,68 least squares by Householder QR,57 least squares by MGS, 67 left-looking,107 LSME,292 LSQI, 170 LSQR,291 MGS,62 NIPALS-PLS,200,201 plane rotation, 48 preconditioned CGLS,286 preconditioned CGME,287 Rayleigh-quotient iteration, 366 Rayleigh-Ritz procedure, 369 RCGME,328 recursive CGS QR, 111 recursive Cholesky,110 recursive Householder QR, 112 right-looking,107 secular equation,170 sequential Givens QR,190 singular values by bisection, 351 SVD of $2 \times 2$ ,356 zero-shift QRSVD, 343   
ALS,see alternating least squares   
alternating least squares, 402, 406   
angles between subspaces,16-17   
arithmetic floating-point,32-33 standard model, 33   
Arnoldi decomposition,301   
Arnoldi process, 301   
Arnoldi-Tikhonov method, 335   
ART, see algebraic reconstruction technique   
augmented system,8,268 generalized,116-117

optimal scaling, 93   
solution by LDLT,91-94   
solution by QR,58-59,117

backward error, 34 analysis, 36 componentwise,99 normwise,97 optimal, 97   
band matrix augmented,204 Cholesky factorization, 186-187 properties,183-186 QR factorization,188-191 standard form,189   
bandwidth of LU factors,185   
bandwidth reduction,193   
basis pursuit, 426   
Bauer-Skeel condition number, 30   
BBH algorithm, 239   
best linear unbiased estimate,4, 127,218   
biconjugation algorithm, 314-315   
bidiagonal decomposition, 191-196 Householder algorithm, 194-196 one-sided algorithm,194   
bidiagonal matrix,183 graded, 348 unreduced, 194   
bilinear least squares,405-406   
bipartite graph,253   
bisection method, 349-352   
BLAS,112-114 sparse,247   
Blendenpik,320   
block algorithms,106-112   
block-angular form,309   
block-angular problem, 206-209 covariance matrix,208 doubly bordered,207 QR algorithm,208-209   
BLS,see bounded least squares   
BLUE,see best linear unbiased estimate   
bounded least squares,161   
BP, see basis pursuit   
Bunch-Kaufman pivoting,92   
CANDECOMP, 217   
canonical correlation,19   
Cauchy matrix, 239   
Cauchy-Schwarz inequality,2( generalized, 119   
centering data,205   
CG method, see conjugate gradient method   
CGLS,281-285,317, 327 semidefinite case, 282 termination,284-285   
CGNR, see CGLS   
CGS,see classical Gram-Schmidt   
Chambers’ downdating algorithm,135   
characteristic equation, 359   
chasing, 345   
Chebyshev abscissae,231 interpolation, 232 polynomials,231-233   
Cholesky factorization,8-10, 41-43 band,186-187 downdating,145-148 extended matrix, 9 graph model, 249-250 incomplete,309-312 QR,10 QR2 algorithm,213 semidefinite matrix,71-73   
Cimmino's method, 273-274   
circulant matrix,322-324   
classical Gram-Schmidt, 63   
Clenshaw's formula, 229   
clique, 248   
column ordering minimum degree,251-252 nested dissection,206-209   
column pivoting in QR factorization,73-76 reverse,83   
column scaling, optimal, 44   
column subset selection, 80   
compact SVD, 11   
complementary subspace,118   
complex arithmetic, 33   
compressed sensing,426-429   
condition estimation LINPACK,94-95   
condition number, 29 Bauer-Skeel, 30 effective, 172 estimation of, 94-97 of matrix,24-25   
conjugate gradient method, 278-280   
contraction product, 214   
core problem,194-196   
corrected seminormal equations,104-105   
Courant-Fischer theorem,12   
covariance matrix,3,115,122 band matrix,187-188 block-angular problem, 208 computing, 45 generalized least squares,115 method,149 sparse matrix,187-188   
cross-validation,178-180,332   
CS decomposition,18-19   
CSNE,see corrected seminormal equations   
curvature radius, 394   
curve fitting,411-416   
Cuthill-McKee algorithm, 251   
Cuthill-McKee ordering,251   
cyclic pivoting, 83   
damped least squares,168   
data least squares problem, 219   
DCT, see discrete cosine transform   
decomposition complete orthogonal,77-79 CS,18-19 GSVD, 124 SVD,11-13,339-382 URV,78   
deconvolution problem,173   
derivative directional, 390 of inverse,169 of orthogonal projector, 403   
Dill, tt uisviviv liuucy transform   
differential qd algorithm, 351-352   
discrepancy principle,177   
discrete cosine transform, 320   
discrete Hartley transform, 320   
distance between subspaces, 17,368   
distance to singular matrices, 25   
distribution function,3   
divide and conquer for SVD, 358-382   
downdating, 144 by hyperbolic rotation,137 by seminormal equations, 147-148 Cholesky factorization, 145-148 Saunders algorithm,145-147   
dqds algorithm,see differential qd algorithm   
dual norm, 20   
Eckart-Young-Mirsky theorem,23   
eigenvalue problem projected, 368 symmetric 2by 2,353   
EISPACK,113   
elimination tree,249-250 postordering,250 topological ordering,250 transitive reduction,250   
elliptic Gram-Schmidt QR,119-122 norm,119,329 singular values,331   
EM algorithm,417   
empty matrix,18,125   
error analysis backward, 36 forward,36 inner product, 34   
error estimation a posteriori, 97-100 Cholesky, 44 forward,27-31 optimal backward,97-100   
errors-in-variable model, 218   
Euler angles, 51   
exchange operator,136

expected value, 3   
exponential fitting,403   
extended matrix,57, 66,121

fast cosine transform, 322   
fast Fourier transform,235-237   
FFT, see fast Fourier transform   
fill, in sparse matrix,243   
filter factor, 176,325   
fitting exponentials, 403   
flexible GMRES,303   
floating-point IEEE 754 standard,32 number, 32 precision, 32 rounding error, 33   
flop count band Cholesky,187 bidiagonal decomposition, 192 Gram-Schmidt,61 QR factorization, 53 tridiagonal system,186   
forward error, 34 analysis,36 of inner product, 35   
Fourier analysis butterfly relations,236 coefficients, 228 discrete,233-237 matrix, 235   
Fourier synthesis,235   
Fréchet derivative,389   
Fredholm integral equation,171   
Frobenius norm,21   
fundamental matrix,128 subspace,6,15,28   
Galerkin condition, 288,368   
Galerkin method,172   
gap in spectrum,369   
Gauss-Markov linear model, 4-5 theorem,4   
Gauss-Newton direction, 392   
Gauss-Newton method, 224, 391-395 inexact,400-402 line-search,394-395 local convergence,393-394 regularized, 396 trust-region,396-398   
Gauss-Seidel's method, 272   
generalized

augmented system, I16-11/ inverse,15 least squares,115-133 normal equations,115,283 of second kind, 116 QR factorization,122-124 SVD,124-128 geodetic measurements, 3 Givens QR factorization, 55-5 Givens rotation, 47-51 GKL bidiagonalization, 196-199 GMRES,301-304 flexible,303 range-restricted, 334 GQR, see generalized QR factorization grade of vector, 198 gradient projection methods, 416-417 Gragg-Harrod procedure, 230 Gram polynomials,230-231 Gram-Schmidt orthogonalization,198 Gram-Schmidt QR,59-63 classical, 60 elliptic,119-122 modified, 61 modifying,150-152 reorthogonalization, 68-71 graph bipartite,253,264 matching, 264 clique in, 248 connected, 248 directed, 247 edges, 247 elimination,249-252 filled,249, 250 nodes,247 of matrix,247-250 planar,256 separator, 248 strongly connected, 248 subgraph of, 247 undirected, 247 gravitational field model, 3 GSVD, 159 Hadamard transform, 319 Hall property, 253 Hankel least squares problem, 241 harmonic Ritz value,370

Harwell-Boeing collection, 265   
Harwel Software Library,87, 400   
Hessenberg matrix,55   
Hessian matrix, 390,391   
Hestenes method, 352-356   
hierarchical memory,114   
Holder inequality,20   
Holder norm,20   
HOSVD, 217   
Householder reflector, 46-47 elliptic,121-122 unitary, 47   
Huber's M-estimator, 422   
hyperbolic rotation,134   
hypermatrix,214-218 unfolding, 215   
IC,see incomplete Cholesky   
ill-posed problem,171-182   
ILS,see indefinite least square!   
IMGS,see incomplete MGS   
implicit Q theorem, 344   
implicit shift QR algorithm, 344-345   
incomplete factorization,309-314 QR factorization, 312-314   
incomplete Cholesky higher-level,310 preconditioner,309-312 threshold, 310 zero-fill, 309   
incomplete MGS,312   
indefinite least squares, 133-137   
inner inverse,15   
interior method, 419 primal-dual,418   
interior-point method,427   
interval arithmetic,33-34   
INTLAB, 34   
invariant subspace,dominant, 368   
inverse function, 390 generalized,15 inner, 15 iteration,224,365-367 simultaneous, 83 least-norm,16 least squares, 16 Moore-Penrose,13 of band matrix,185 outer,1) power method,365 problem,171-182 Schulz iteration, 379   
inverse iteration, 81   
IRLS,see iteratively reweighted least squares   
irreducible matrix,185,264   
iterative method CGLS,281-285 convergence asymptotic rate,270 average rate, 270 conditions for, 269 error-reducing, 273 Gauss-Seidel, 272 Jacobi, 272 LSME,291-292 LSMR,292-294 LSQR,289-291 preconditioned,285-287 residual-reducing, 273 SOR,274-275 block,307 splitting,270 SSOR,274-275 stationary,269-274 symmetrizable,270 Toeplitz system,322-325 two-block,308-309   
iterative refinement,100-106, 114,131, 159 in three precisions,104 for linear systems,100-101 for sparse problem,104-106 in fixed precision,103-105 in mixed precision,100-103   
iterative regularization, 325-335   
iteratively reweighted least squares,423-425   
Jacobi's method,272   
Jacobi's method for SVD, 352-357 classical, 354 cyclic,354 sweep,354 threshold, 354   
Jacobi-Davidson's method, 374-375   
Jacobian matrix,389,391   
Jordan-Wielandt matrix,12, 342   
$J .$ orthogonal matrices,134-136   
Kaczmarz's method,273   
Kalman gain vector, 149   
Khatri-Rao product, 216   
KKT conditions,161   
Kogbetliantz's method, 356-357   
Kronecker product, 209 least squares problem, 209-211 pseudoinverse, 210 QR factorization, 211 SVD,211   
Krylov subspace,198 augmented,335-337 deflated,335-337 methods,196-200,278-305 in finite precision,294-305   
$\ell _ { 1 }$ and $\ell _ { \infty }$ approximation, 420-423   
Lagrangian function, 161   
LANCELOT, 400   
Lanczos CG method,288-289 decomposition,288 process,287-288,370   
Landweber's method,325-326   
LAPACK, 114   
LARS,425-426   
LASSO, 425-426   
latent root regression, 218   
Lauchli problem, 40,130   
least-angle regression, 425-426   
least-norm inverse,16   
least-norm problem,7   
least squares $\ell _ { 1 }$ -regularized, 425 damped, 168 derivative of solution,26 history of,1-2   
inverse,16 iteratively reweighted, 423-425 recursive,148-149 regularized,294,327-331   
least squares fitting algebraic,411-414 discrete,229-231 geometric, 414-416 of circle,411-416 of ellipse, 411-416 of geometric elements, 411-416

band, 183-191 bilinear, 405-406 constrained, 155-168 generalized,5,115-133 indefinite,133-137 Kronecker, 209-211 nearly square,86-88 nonnegative,416-420 separable,402-406 sequential, 155 statistical aspects,230-231 stiff, 129 strongly rectangular, 212-213 Toeplitz,239-241 weighted, 128-133 least squares solution characterization of, 5-8 updating of, 263 left-looking algorithm, 60 Levenberg-Marquardt method, 396 linear complementarity problem,162 linear equality constraints by weighting,159-160 linear inequality constraints classification,160-162 linear model errors-in-variables,218-219 Gauss-Markov, 4 LINPACK, 113 Lipschitz condition, 389 low-rank approximation,23-24 Lowdin orthogonalization, 383 $\ell _ { p }$ approximation, 420-423 LSQR stopping criteria, 296 LSRN, 320-321 LU factorization partial, 88 rank-revealing,88-91 LU preconditioner for CGLS,316 rate of convergence, 318 Lyapunov's equation, 210

matrix band,183-191 bidiagonal, 183 consistently ordered, 275 elementary, 46 envelope, 251 idempotent, 6

irreducible, 185 Jordan-Wielandt,12 nonnegative, 29 norm,19-22 positive definite, 8 random orthogonal, 63 reducible, 185 sign function,380-382 sparse,243 spectral norm, 21 square root of,378-380 stretching, 263 tall-and-skinny,212 tridiagonal, 183 two-cyclic, 13 well-conditioned, 24   
matrix function,376-382 primary, 377   
matrix test collection Harwell-Boeing, 244 Matrix Market, 244 SuiteSparse, 244   
mean,421   
median, 421   
medical imaging, 417   
merit function, 400   
MGS,see modified Gram-Schmidt   
midrange, 421   
MINARES,300   
minimal residual algorithm, 299-300   
minimum degree ordering, 252   
MINRES,see minimal residual algorithm   
MINRES-QLP,300   
mixed sparse-dense problems, 262-263   
modified Gram-Schmidt as a Householder method, 64-66 backward stability, 65 least-norm solution, 67 least squares solution,121   
modifying Gram-Schmidt QR,150-152   
Moore-Penrose inverse,13   
MRRR algorithm, see multiple relatively robust representation algorithm   
multicore processor, 114   
multifrontal method, 255-258 for NR fartnri7atinn update matrix,256   
multilinear function, 213   
multilinear operator, 391   
multiple relatively robust representation algorithm, 352   
multiprecision algorithm,104   
multirank of tensor, 215   
nested dissection, 206   
netlib,375   
Newton's interpolation formula, 378   
NIPALS-PLS algorithm, 200-203   
NNLS,see nonnegative least squares   
NNMF, see nonnegative matrix factorization   
no-cancellation assumption, 245   
node(s) adjacent, 247 amalgamation of, 258 connected, 248 degree,247 eccentricity of, 251 indistinguishable,252 supernode,252,258   
nonlinear least squares Ceres solver,258,402 constrained, 400   
nonnegative least squares,161-168, 416-420 gradient projection methods,416-417 interior methods,418-420 matrix, 29 matrix factorization,419-420   
norm dual,20 elliptic, 119 Frobenius,21,24 Holder, 20 nuclear, 429 of matrix,19-22 of vector,19-22 Schatten, 22 spectral, 21 total-variation, 426 unitarily invariant,21   
normal curvature matrix, 393

forming of, 39 generalized, 5 information loss,40 method,39-45 scaling of, 43-44 normalized residuals, 45 nullspace method, 157-158 numerical, 173 from RRQR,83 from SVD, 173 from ULV,79 from URV, 78 of matrix, 6 numerical cancellation, 253 ill-determined rank,172 nullspace, 27 rank,26-27 numerical rank, 22 oblique projector, 118-119 ODR,se orthogonal distance regression ODRPACK, 410 Oettli-Prager bound, 99-100 optimal backward error, 97-100,296 orthogonal basis problem,68,109 coefficients, 228 complement, 12 distance regression, 408-411 iteration,367 projection, 15 derivative of, 26 regression,406-408 systems,227-231 orthogonal polynomials Chebyshev,231-233 general theory,227-229 trigonometric,233-235 orthogonal transformation elementary,46-51 Givens,47-51 Householder, 46-47 orthogonal tridiagonalization, 304-305 orthogonality,loss of,68-71 outer inverse,15 Padé approximation, 381-382 Paige's method,122-123 PARAFAC, 217

partial least squares,191-203   
partial SVD of sparse matrix,376   
partitioned algorithms,106-112   
PCR,see principal components regression   
Penrose conditions,14,182   
permutation bit-reversal, 236 matrix, 73   
perturbation analysis bounds for QR factorization, 54 componentwise,29-31 least squares solutions, 27-31 pseudoinverse,25-26   
PET, see positron emission tomography   
Peters-Wilkinson method, 84-86,129,317   
pivoted magnitude,83   
pivoting cyclic,83 reverse,76 rook,85   
plane reflector, 49   
plane rotation,47-51 algorithm,48 fast, 50-51 self-scaling,51,132 storage of, 49 unitary, 49   
PLS,see partial least squares, 202   
polar decomposition, 382-386   
polynomial approximation,227-233 triangle family, 227   
positive definite matrix, 6   
positron emission tomography, 417   
power method,339,363-367   
preconditioner approximate inverse, 314-315 block column,306-308 block SSOR, 307 by submatrix,316-321 cyclic Jacobi, 308 diagonal scaling,286,306 for Toeplitz systems, 324-325 IMGS,312 least squares,306-325 LU,316-319 reduced system, 308 SSOR,306-309 two-level,321-322   
predicting fill, 247-250   
principal angle,17,308 components regression,174 vector, 17   
Procrustes problem, 383, 385-387   
product SVD,126   
projector, 6-7 oblique,118-119 orthogonal, 6-7   
pseudoinverse,13-16 derivative of, 26 from QR,52-74 from SVD,14 of Kronecker product, 210 solution, 8 from LU,84-86 Wedin's identity, 26   
pseudoskeleton approximation, 90   
PSVD algorithm, 223   
qd algorithm, see quotient difference algorithm   
QL algorithm,347-348   
QR algorithm convergence criteria,347 implicit shift,344-345 operation count, 347 perfect shifts, 347 real symmetric matrices, 344-345 zero-shift, 342-344   
QR factorization, 52-84 appending a column, 143-145 appending a row, 141 backward stability, 54,131 column pivoting,73-76,131 deleting a column,142 deleting a row, 144 flop count, 53 generalized,122-124 Givens,55-56 Hessenberg, 55 incomplete,312-314 modifying,139-145 multifrontal,255-258

partial, 204 pivoted, 140 rank-one change,141-142 rank-revealing,79-84 Chan's algorithm, 82 recursive,111 row ordering,254-255 row pivoting,131 row sequential,254-255 row sorting, 131 Vandermonde matrix,238 weighted,130-132 QRSVD algorithm, 345-348 quadratic inequality constraints, 168-169 quasi-definite system,319 quasi-Newton method,398-400 quotient difference algorithm, 351 quotient SVD, 126

radius of convergence, 376   
random errors,4 normal projection, 319 orthogonal matrix, 63 sampling,319   
randomized algorithms, 319-321   
range space of matrix,6   
rank numerical, 26-27 structural, 245   
rank of tensor, 216   
rank-revealing QR,79-84 modifying,152-155 sparse,259-261   
Rayleigh quotient iteration,224,365-367 matrix, 369   
Rayleigh-quotient,224,365   
Rayleigh-Ritz procedure, 368-376 implicit restarts,372   
recursive least squares, 148-149   
reduced gradient method,158   
reduced-order model, 23   
reducible matrix,185,264   
reduction to bidiagonal form, 341-342 to symmetric tridiagonal form,340-341

least-angle,425-426 linear, 40 principal components,174 robust, 422 stepwise,140 regularization,173-182 filter factor, 325 hybrid method,332-333 iterative,325-335 Krylov subspace methods, 331-335 Landweber, 325 parameter, 177 PLS,202 semiconvergence, 326 Tikhonov, 175 trust-region method,182 regularized CGLS,327-329 CGME,328-329 least squares,294,327-331 relaxation parameter, 274 optimal, 308 optimal for SOR, 275 reorthogonalization, 68-71, 297 selective, 69, 371 residual polynomial, 284 reverse pivoting,76,83 Richardson's method,271-272 second order, 278 ridge regression,175 right-looking algorithm, 61 rigid body movements,386 Riley's method,177 Ritz value, 369 harmonic, 370 Ritz vector, 369 refined, 370 RLS, see recursive least squares rook pivoting, 85 rotation, three-dimensional, 49 rounding error analysis,34-36 row-action methods, 274 RQI, see Rayleigh-quotient iteration RRQR,see rank-revealing QR RRQR factorization Chan's algorithm,82 strong,84 Rutishauser's qd algorithm, 351 saddle point svstem. 116

ScaLAPACK, 114   
scaled total least squares, 218   
scaling of columns optimal, 44   
Schatten norms, 22   
Schulz iteration, 379   
Schur-Banachiewicz formula, 137   
Schur complement, 89,136, 137   
Schur decomposition,378,379   
secular equation,168-171,360   
selective reorthogonalization, 69   
semi-iterative method,275-78 Chebyshev, 277   
seminormal equations,104-106 for downdating,147-148   
separable least squares problem, 402-406 VARPRO algorithm, 404   
Sherman-Morrison formula, 138   
shift matrix, 323   
signature matrix,133   
singular value decomposition, 11-13 compact, 11 computation,339-352 generalized,124-128 Kronecker product, 211 modifying,360-363 of tensor, 217 of two by two, 356 related eigenvalue problems, 12 truncated solution,173-175   
singular values,12 absolute gap, 22 by bisection,349-352 elliptic, 331 interlacing property,22 min-max property,12,22 of bidiagonal matrix,343 relative gap, 343 sensitivity,22-23   
singular vectors,12 of bidiagonal matrix, 343 uniqueness,12   
smoothing-norm operator, 175   
SNE,see seminormal equations   
SOR,274-275,308 hlnck 307 inverse   
sparse approximate inverse, 314-315   
sparse least squares problem updating,262-263   
sparse matrix block triangular form, 263-265 column ordering,250-252 irreducible, 264 reducible, 264 row ordering for QR, 254-255 structural cancellation, 253 structural rank, 245   
sparse matrix-vector product, 245-247   
spectral norm,21 projector, 380 radius,269 transformation, 365   
splitting of matrix, 270 proper, 270   
SQD system, see symmetric quasi-definite system   
square root of matrix,378-380   
SSOR,274-275   
SSOR preconditioner,307,308   
stability of algorithm,36-37   
stepwise regression,140   
Stieltjes procedure,229,230   
stopping criteria for LSQR,296   
storage scheme compressed form,245 row,246,247 coordinate scheme, 245 dynamic, 245 general sparse,245-246 static, 245   
Sturm sequence,350   
submatrix preconditioner, 316-321 rate of convergence,316   
subspace complementary, 118 iteration, 367-368   
SuiteSparseQR,258   
sum convention, 213   
sunerlinear convergence. 295   
SVD, see singular value decomposition   
Sylvester's criterion,10 equation,379   
symmetric gauge functions, 22   
symmetric quasi-definite system,329-331   
symmetrizable,270   
tall-and-skinny matrix, 212   
Taylor's formula,391   
tensor, 214 CP decomposition, 217 decompositions,216-217 multirank, 215 operations,214-215 SVD,217   
Tikhonov regularization, 175-182 iterated, 177, 326 standard form, 176 transformation to,180-182   
TLS, see total least squares   
Toeplitz least squares problem, 239-241   
Toeplitz matrix, 239 fast multiplication, 324 QR factorization,239-241 upper triangular, 240   
Toeplitz systems circulant preconditioner, 324 iterative solvers,322-325 preconditioner, 324-325   
tomography,161 positron emission, 417 seismic, 363   
total least squares,218-226 by inverse iteration,223-224 by SVD,219-221 conditioning,220,221 generalized,221-223 generic problem, 219 mixed,220 multidimensional, 221-223 scaled,218   
total-variation norm, 426   
tridiagonal matrix,183 unreduced, 194   
trigonometric polynomials, 233   
truncated SVD,173-175   
truncated TLS, 225   
trust-region methods,396-398   
TSVD,see truncated SVD   
TV-norm,see total-variation norm   
two-block methods,204-206   
two-cyclic matrix,13   
two-level preconditioner, 321-322   
ULV decomposition, 77-79 modifying,152-155   
unbiased estimate,4,174 best linear, 127 of variance, 45   
underdetermined linear system, 7,88,99,116,128

by Gram-Schmidt,67 by Householder,58 by normal equations,8 unit roundoff, 32 unitarily invariant norm, 21 updating least squares solution, 263 QR factorization,141-145 URV decomposition, 78

Vandermonde matrix QR factorization of, 238   
Vandermonde systems, 237-239 fast algorithm,238   
variable projection method, 402-405   
VARPRO algorithm, 404   
vector space calculus,389-391   
Volterra integral equation, 240   
wavelet transform, 322   
weighted problem by LU factorization,129-130 by QR factorization,130-132 condition number, 132 stiff,129   
Wielandt-Hoffman theorem, 22   
Wilkinson matrix, 94   
Wilkinson shift, 345   
Woodbury formula,138   
wrapping effect, 34

The method of least squares,discovered by Gauss in 1795,is a principal tool for reducing the influence of errors when fiting a mathematical model to given observations.Applications arise in many areas of science and engineering. The increased use of automatic data capturing frequently leads to large-scale least squares problems. Such problems can be solved by using recent developments in preconditioned iterative methods and in sparse QR factorization.

The first edition of Numerical Methods for Least Squares Problems was the leading reference on this topic for many years.The updated second edition stands out compared to other books on the topic because it

provides an in-depth and up-to-date treatment of direct and iterative methods for solving different types of least squares problems and for computing the singular value decomposition;   
· covers generalized, constrained,and nonlinear least squares problems as well as partial least squares and regularization methods for discrete ill-posed problems; and   
· contains a bibliography of over 1,l00 historical and recent references, providing a comprehensive survey of past and present research in the field.

# Audience

This book will be of interest to graduate students and researchers in applied mathematics and to researchers working with numerical linear algebra applications.

![](../chunks/Numerical Methods for Least Squares Problems (Åke Björck) (z-library.sk, 1lib.sk, z-lib.sk_part_0008_pages_0491-0510/auto/images/e68893c93b94ed275ca7c9125e9a1f587e4effa7c632fbdb587fd9294ac37a6e.jpg)

Ake Bjorck is a professor emeritus at Linkoping University, Sweden. He is the author of many research papers and books on numerical analysis and matrix computations.He served as managing editor of the journal BIT Numerical Mathematics from 1993 to 2003 and has been a SIAM Fellow since 2014.
