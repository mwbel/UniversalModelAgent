Definition C.2 Given a scalar-valued function of a vector, $f ( \mathbf { x } )$ , the Hessian of $f$ is a square matrix of partial derivatives given by

$$
\mathbf { H } ( f ( \mathbf { x } ) ) = \left[ \begin{array} { c c c c } { \frac { \partial ^ { 2 } f } { \partial x _ { 1 } ^ { 2 } } } & { \frac { \partial ^ { 2 } f } { \partial x _ { 1 } \partial x _ { 2 } } } & { \cdot \cdot \cdot } & { \frac { \partial ^ { 2 } f } { \partial x _ { 1 } \partial x _ { n } } } \\ { \frac { \partial ^ { 2 } f } { \partial x _ { 2 } \partial x _ { 1 } } } & { \frac { \partial ^ { 2 } f } { \partial x _ { 2 } ^ { 2 } } } & { \cdot \cdot \cdot } & { \frac { \partial ^ { 2 } f } { \partial x _ { 2 } \partial x _ { n } } } \\ { \vdots } & { \vdots } & { \cdot } & { \vdots } \\ { \frac { \partial ^ { 2 } f } { \partial x _ { n } \partial x _ { 1 } } } & { \frac { \partial ^ { 2 } f } { \partial x _ { n } \partial x _ { 2 } } } & { \cdot \cdot \cdot } & { \frac { \partial ^ { 2 } f } { \partial x _ { n } ^ { 2 } } } \end{array} \right] .
$$

If $\dot { \boldsymbol { f } }$ is twice continuously differentiable, the Hessian is symmetric. It is common in mathematics to write the Hessian using the operator $\nabla ^ { 2 }$ , but this sometimes leads to confusion with another vector calculus operator, the Laplacian.

Theorem C.1 If $f ( \mathbf { x } )$ is a twice continuously differentiable function, and $\mathbf { H } ( f ( \mathbf { x } _ { \mathrm { 0 } } ) )$ is a positive semidefinite matrix, then $f ( \mathbf { x } )$ is a convex function at $\mathbf { x } _ { \mathrm { 0 } }$ . If $\mathbf { H } ( f ( \mathbf { x } _ { \mathrm { 0 } } ) )$ is positive definite, then $f ( \mathbf { x } )$ is strictly convex at $\mathbf { x } _ { \mathrm { 0 } }$ .

This theorem can be used to check whether a critical point is a minimum of $f$ . If $\mathbf { x } ^ { * }$ is a critical point of $f$ and $\mathbf { H } ( f ( \mathbf { x } ^ { * } ) )$ is positive definite, then $f$ is convex at $\mathbf { x } ^ { * } ,$ , and $\mathbf { x } ^ { * }$ is thus a local minimum of $f$ .

It will be necessary to compute derivatives of quadratic forms.

Theorem C.2 Let $f ( \mathbf { x } ) = \mathbf { x } ^ { T } \mathbf { A } \mathbf { x }$ , where A is an n by $n$ symmetric matrix. Then

$$
\nabla f ( \mathbf { x } ) = 2 \mathbf { A } \mathbf { x }
$$

and

$$
\mathbf { H } ( f ( \mathbf { x } ) ) = 2 \mathbf { A } .
$$

Definition C.3 Given a vector-valued function of a vector, $\mathbf { F } ( \mathbf { x } )$ , where

$$
\begin{array} { r } { \mathbf { F } ( \mathbf { x } ) = \left[ \begin{array} { c } { f _ { 1 } ( \mathbf { x } ) } \\ { f _ { 2 } ( \mathbf { x } ) } \\ { \vdots } \\ { f _ { m } ( \mathbf { x } ) } \end{array} \right] , } \end{array}
$$

the Jacobian of $\mathbf { F }$ is

$$
\begin{array} { r } { \mathbf { J } ( \mathbf { x } ) = \left[ \begin{array} { c c c c c } { \frac { \partial f _ { 1 } } { \partial x _ { 1 } } } & { \frac { \partial f _ { 1 } } { \partial x _ { 2 } } } & { \cdot \cdot \cdot } & { \frac { \partial f _ { 1 } } { \partial x _ { n } } } \\ { \frac { \partial f _ { 2 } } { \partial x _ { 1 } } } & { \frac { \partial f _ { 2 } } { \partial x _ { 2 } } } & { \cdot \cdot \cdot } & { \frac { \partial f _ { 2 } } { \partial x _ { n } } } \\ { \vdots } & { \vdots } & { \ddots } & { \vdots } \\ { \frac { \partial f _ { m } } { \partial x _ { 1 } } } & { \frac { \partial f _ { m } } { \partial x _ { 2 } } } & { \cdot \cdot \cdot } & { \frac { \partial f _ { m } } { \partial x _ { n } } } \end{array} \right] . } \end{array}
$$

Some authors use the notation $\nabla \mathbf { F } ( \mathbf { x } )$ for the Jacobian. Note that the rows of J $\lceil ( \mathbf { x } )$ are the gradients (C.1) of the functions $f _ { 1 } ( { \bf x } ) , f _ { 2 } ( { \bf x } ) , \ldots . . . , f _ { m } ( { \bf x } )$ .

# C.2. TAYLOR’S THEOREM

In the calculus of single-variable functions, Taylor’s theorem produces an infinite series for $f ( x + \Delta x )$ in terms of $f ( x )$ and its derivatives. Taylor’s theorem can be extended to a function of a vector $f ( \mathbf { x } )$ , but in practice, derivatives of order higher than 2 are extremely inconvenient. The following form of Taylor’s theorem is often used in optimization theory.

Theorem C.3 Suppose that $f ( \mathbf { x } )$ and its first and second partial derivatives are continuous. For any vectors $\mathbf { x }$ and $\Delta \mathbf { x }$ , there is a vector $\mathbf { c }$ , with $\mathbf { c }$ on the line between $\mathbf { x }$ and $\mathbf { x } + \Delta \mathbf { x }$ , such that

$$
f ( \mathbf { x } + \Delta \mathbf { x } ) = f ( \mathbf { x } ) + \nabla f ( \mathbf { x } ) ^ { T } \Delta \mathbf { x } + \frac { 1 } { 2 } \Delta \mathbf { x } ^ { T } \mathbf { H } ( \mathbf { \nabla } f ( \mathbf { c } ) ) \Delta \mathbf { x } .
$$

This form of Taylor’s theorem with remainder term is useful in many proofs. However, in computational work there is no way to determine c. For that reason, when $\Delta \mathbf { x }$ is a small perturbation, we often make use of the approximation

$$
f ( \mathbf { x } + \Delta \mathbf { x } ) \approx f ( \mathbf { x } ) + \nabla f ( \mathbf { x } ) ^ { T } \Delta \mathbf { x } + \frac { 1 } { 2 } \Delta \mathbf { x } ^ { T } \mathbf { H } ( \mathbf { \nabla } f ( \mathbf { x } ) ) \Delta \mathbf { x } .
$$

An even simpler version of Taylor’s theorem, called the mean value theorem, uses only the first derivative.

Theorem C.4 Suppose that $f ( \mathbf { x } )$ and its first partial derivatives are continuous. For any vectors x and $\Delta \mathbf { x }$ there is a vector $\mathbf { c }$ , with $\mathbf { c }$ on the line between $\mathbf { x }$ and $\mathbf { x } + \Delta \mathbf { x }$ such that

$$
f ( \mathbf { x } + \Delta \mathbf { x } ) = f ( \mathbf { x } ) + \nabla f ( \mathbf { c } ) ^ { T } \Delta \mathbf { x } .
$$

We will make use of a truncated version of (C.8):

$$
f ( \mathbf { x } + \Delta \mathbf { x } ) \approx f ( \mathbf { x } ) + \nabla f ( \mathbf { x } ) ^ { T } \Delta \mathbf { x } .
$$

By applying (C.10) to each of the functions $f _ { 1 } ( { \bf x } ) , f _ { 2 } ( { \bf x } ) , \ldots . . . , f _ { m } ( { \bf x } )$ , we obtain the approximation

$$
\mathbf { F } ( \mathbf { x } + \Delta \mathbf { x } ) \approx \mathbf { F } ( \mathbf { x } ) + \mathbf { J } ( \mathbf { x } ) \Delta \mathbf { x } .
$$

# C.3. LAGRANGE MULTIPLIERS

The method of Lagrange multipliers is an important technique for solving optimization problems of the form:

$$
\begin{array} { l } { \operatorname* { m i n } { f ( \mathbf { x } ) } } \\ { g ( \mathbf { x } ) = 0 , } \end{array}
$$

where the scalar-valued function of a vector argument, $f ( \mathbf { x } )$ , is called the objective function.

Figure C.1 shows a general situation. The solid contour represents the set of points where the (nonconstant) function $g ( \mathbf { x } ) = 0$ , and the dashed contours are those of another function $f ( \mathbf { x } )$ that has a minimum as indicated. Moving along the $g ( \mathbf { x } ) = 0$ contour, we can trace out the curve ${ \mathbf x } ( t )$ , parameterized by the variable $t \geq 0$ , where $g ( \mathbf { x } ( t ) ) = 0$ and $t$ increases as we progress counter-clockwise. At any point ${ \bf x } ( t )$ on the contour, the gradient of $g ( \mathbf { x } ( t ) )$ must be perpendicular to the contour because the function is constant along this curve. Note that in Figure $\mathbf { C } . 1 , g ( \mathbf { x } )$ increases in the outward direction relative to the contour, so the gradient of $g ( \mathbf { x } )$ will be outward.

By the chain rule,

$$
f ^ { \prime } ( \mathbf { x } ( t ) ) = \mathbf { x } ^ { \prime } ( t ) ^ { T } \nabla f ( \mathbf { x } ( t ) ) ,
$$

where ${ \mathbf { x } } ^ { \prime } ( t )$ is the counter-clockwise tangent to the contour $g ( x ) = 0$ . For the point $\mathbf { x } _ { 1 } = \mathbf { x } ( t _ { 1 } )$ in Figure C.1, $\nabla f ( \mathbf { x } _ { 1 } )$ and $\mathbf { x } ^ { \prime } ( t _ { 1 } )$ are at an obtuse angle, and their dot product $f ^ { \prime } ( \mathbf { x } _ { 1 } )$ (C.13) will therefore be negative. Thus, $f ( \mathbf { x } )$ is decreasing as we move counterclockwise around the contour $g ( \mathbf { x } ) = 0$ from $\mathbf { x } _ { 1 }$ , and $\mathbf { x } _ { 1 }$ cannot satisfy (C.12).

In Figure C.2, for the point ${ \mathbf x } _ { 0 } = { \mathbf x } ( t _ { 0 } )$ , $\nabla f ( \mathbf { x } _ { \mathrm { 0 } } )$ is perpendicular to the curve $g ( \mathbf { x } ) = 0$ . In this case, by (C.13), $f ^ { \prime } ( \mathbf { x } _ { \mathrm { 0 } } ) = 0$ , and the point $\mathbf { x } _ { \mathrm { 0 } }$ may or may not be a minimum for $f ( \mathbf { x } )$ along the contour. Figure C.2 shows that a point $\mathbf { x } _ { \mathrm { 0 } }$ on the curve $g ( \mathbf { x } ) = 0$ can only be a possible minimum point for $f ( \mathbf { x } )$ if $\nabla g ( \mathbf { x } _ { \mathrm { 0 } } )$ and $\nabla f ( \mathbf { x } _ { \mathrm { 0 } } )$ are parallel or antiparallel. A point where this occurs is called a stationary point.

![](images/5c07e974532333a5095aa2e88fdb180338c20ccca4c6e36cfd31036559f60805.jpg)  
Figure C.1 The situation at a point $\mathbf { x } _ { 1 } = \mathbf { x } ( t _ { 1 } )$ along the contour $g ( \mathbf { x } ) = 0$ that is not a minimum of $f ( \mathbf { x } )$ and thus does not satisfy (C.12).

Finding a stationary point is necessary, but not sufficient, for finding a minimum of $f ( \mathbf { x } )$ along the contour $g ( \mathbf { x } ) = 0$ , because such a point may be a minimum, maximum, or saddle point. Furthermore, a problem may have several local minima. Thus it is necessary to examine the behavior of $f ( \mathbf { x } )$ at all stationary points to find a global minimum.

Theorem C.5 (C.12) can only be satisfied at a point $\mathbf { x } _ { \mathrm { 0 } }$ where

$$
\nabla f ( \mathbf { x } _ { 0 } ) + \lambda \nabla g ( \mathbf { x } _ { 0 } ) = \mathbf { 0 }
$$

for some λ. λ is called a Lagrange multiplier.

The Lagrange multiplier condition can be extended to problems of the form

$$
\begin{array} { l } { \operatorname* { m i n } { f ( \mathbf { x } ) } } \\ { g ( \mathbf { x } ) \leq 0 . } \end{array}
$$

Since points along the curve $g ( \mathbf { x } ) = 0$ are still feasible in (C.15), (C.14) must still hold true. However, there is an additional restriction. Suppose that $\nabla g ( \mathbf { x } _ { \mathrm { 0 } } )$ and $\nabla f ( \mathbf { x } _ { \mathrm { 0 } } )$ both point in the outward direction, as in Figure C.2. In this case, we can move in the opposite direction, into the feasible region to decrease $f ( \mathbf { x } )$ (e.g., in the situation depicted in Figure C.2, the solution to (C.15) is simply the indicated minimum of $f ( \mathbf { x } ) )$ . Thus, a point $\mathbf { x } _ { \mathrm { 0 } }$ satisfying (C.14) cannot satisfy (C.15) unless the gradients of $g ( \mathbf { x } _ { \mathrm { 0 } } )$ and $f ( \mathbf { x } _ { \mathrm { 0 } } )$ point in opposite directions.

Theorem C.6 (C.15) can only be satisfied at a point $\mathbf { x } _ { \mathrm { 0 } }$ where

$$
\nabla f ( \mathbf { x } _ { 0 } ) + \lambda \nabla g ( \mathbf { x } _ { 0 } ) = \mathbf { 0 }
$$

for some Lagrange multiplier $\lambda > 0$ .

![](images/2521b9c3a199f095c94eda5071a3db82804844f576553748f86ae7ac65ce5b89.jpg)  
Figure C.2 The situation at a point ${ \mathbf x } _ { 0 } = { \mathbf x } ( t _ { 0 } )$ along the contour $g ( \mathbf { x } ) = 0$ that is a minimum of $f ( \mathbf { x } )$ and thus satisfies (C.12). Note that $\nabla g ( \mathbf { x } _ { 0 } )$ and $\nabla f ( \mathbf { x } _ { \mathrm { 0 } } )$ are parallel.

# Example C.1

Consider a simple example in two variables where $f ( \mathbf { x } )$ defines linear contours and $g ( \mathbf { x } ) = 0$ defines a unit circle

$$
\begin{array} { r l } { \operatorname* { m i n } \ x _ { 1 } + x _ { 2 } } & { } \\ { \quad \quad \ d { x _ { 1 } ^ { 2 } + x _ { 2 } ^ { 2 } - 1 } \leq 0 . } \end{array}
$$

The Lagrange multiplier condition is

$$
{ \binom { 1 } { 1 } } + \lambda \left[ { 2 x _ { 1 } } \right] = \mathbf { 0 } .
$$

One stationary point solution to this nonlinear system of equations is $x _ { 1 } = 0 . 7 0 7 1$ , $x _ { 2 } = 0 . 7 0 7 1$ , with $\lambda = - 0 . 7 0 7 1 .$ . This is the maximum $\operatorname { o f } f ( \mathbf { x } )$ subject to $g ( \mathbf { x } ) \leq 0$ . The second solution to (C.18) is $x _ { 1 } = - 0 . 7 0 7 1$ , $x _ { 2 } = - 0 . 7 0 7 1$ , with $\lambda = 0 . 7 0 7 1$ . Because this is the only solution with $\lambda > 0$ , so that $\nabla f ( \mathbf { x } )$ and $\nabla g ( \mathbf { x } )$ are antiparallel, this solves the minimization problem.

Note that (C.16) is (except for the non-negativity constraint on $\lambda$ ) the necessary condition for a minimum point of the unconstrained minimization problem,

$$
\operatorname* { m i n } { f ( \mathbf { x } ) } + \lambda g ( \mathbf { x } ) .
$$

Here the parameter $\lambda$ can be adjusted so that, for the optimal solution, $\mathbf { x } ^ { * } , g ( \mathbf { x } ^ { * } ) \leq 0$ . We will make frequent use of this technique to convert constrained optimization problems into unconstrained optimization problems.

# C.4. EXERCISES

1. Let

$$
f ( { \bf x } ) = x _ { 1 } ^ { 2 } x _ { 2 } ^ { 2 } - 2 x _ { 1 } x _ { 2 } ^ { 2 } + x _ { 2 } ^ { 2 } - 3 x _ { 1 } ^ { 2 } x _ { 2 } + 1 2 x _ { 1 } x _ { 2 } - 1 2 x _ { 2 } + 6 .
$$

Find the gradient, $\nabla f ( \mathbf { x } )$ , and Hessian, $\mathbf { H } ( f ( \mathbf { x } ) )$ . What are the critical points of $\dot { \boldsymbol { f } }$ ?

Which of these are minima and maxima of $f$

2. Find a Taylor’s series approximation for $f ( \mathbf { x } + \Delta \mathbf { x } )$ , where

$$
f ( \mathbf { x } ) = e ^ { - ( x _ { 1 } + x _ { 2 } ) ^ { 2 } }
$$

is near the point

$$
\mathbf { x } = { \binom { 2 } { 3 } } .
$$

3. Use the method of Lagrange multipliers to solve the problem,

$$
\begin{array} { l } { \operatorname* { m i n } \ : 2 x _ { 1 } + x _ { 2 } \qquad } \\ { 4 x _ { 1 } ^ { 2 } + 3 x _ { 2 } ^ { 2 } - 5 \leq 0 . } \end{array}
$$

4. Derive the formula (A.89) for the 2-norm of a matrix. Begin with the maximization problem,

$$
\operatorname* { m a x } _ { \| \mathbf { x } \| _ { 2 } = 1 } ~ \| \mathbf { A x } \| _ { 2 } ^ { 2 } .
$$

Note that we have squared $\| \mathbf { A x } \| _ { 2 }$ . We will take the square root at the end of the problem.

i. Using the formula $\| \mathbf { x } \| _ { 2 } = \sqrt { \mathbf { x } ^ { T } \mathbf { x } }$ , rewrite the above maximization problem without norms.   
ii. Use the Lagrange multiplier method to find a system of equations that must be satisfied by any stationary point of the maximization problem.   
iii. Explain how the eigenvalues and eigenvectors of $\mathbf { A } ^ { T } \mathbf { A }$ are related to this system of equations. Express the solution to the maximization problem in terms of the eigenvalues and eigenvectors of $\mathbf { A } ^ { T } \mathbf { A }$ .   
iv. Use this solution to get $\| \mathbf { A } \| _ { 2 }$ .

5. Derive the normal equations (2.3) using vector calculus, by letting

$$
f ( \mathbf { m } ) = \| \mathbf { G m } - \mathbf { d } \| _ { 2 } ^ { 2 }
$$

and minimizing $f ( \mathbf { m } )$ . Note that in problems with many least squares solutions, all of the least squares solutions will satisfy the normal equations.

i. Rewrite $f ( \mathbf { m } )$ as a dot product and then expand the expression.   
ii. Find $\nabla f ( \mathbf { m } )$ .   
iii. Set $\nabla f ( \mathbf { m } ) = \mathbf { 0 }$ , and obtain the normal equations.

# C.5. NOTES AND FURTHER READING

Basic material on vector calculus can be found in many calculus textbooks. However, more advanced topics, such as Taylor’s theorem for functions of a vector, are often skipped in basic texts. The material in this chapter is particularly important in optimization, and can often be found in associated references [58, 105, 119].

# Glossary of Notation

• α, $\beta$ , γ , ...: Scalars.   
• a, b, c, ...: Scalar-valued functions or scalars.   
a, b, c, ...: Column vectors. $a _ { i }$ : ith element of vector a.   
A, B, C, ...: Scalar-valued functions or random variables.   
A, B, C, ...: Fourier transforms.   
A, B, C, ...: Vector-valued functions or matrices. $\mathbf { A } _ { i } ,$ ·: ith row of matrix A. $\mathbf { A } _ { \cdot , i }$ : ith column of matrix A. $A _ { i , j }$ : (i, $j )$ th element of matrix A. $\mathbf { A } ^ { - 1 }$ : Inverse of matrix A. $\mathbf { A } ^ { T }$ : Transpose of matrix A. $\mathbf { x } ^ { * }$ : Complex conjugate of matrix x. $\mathbf { A } ^ { H }$ : Complex conjugate transpose of matrix A. a $_ { \odot \mathbf { b } }$ : Vector constructed by element-by-element multiplication of vectors $\mathbf { a }$ and b. a $\oslash \mathbf { b }$ : Vector constructed by element-by-element division of vector a by $\mathbf { b }$ . $\mathbf { A } ^ { - T }$ : Transpose of matrix $\mathbf { A } ^ { - 1 }$ . $R ^ { n }$ : Space of $n$ -dimensional real vectors. $N ( \mathbf { A } )$ : Null space of matrix A. $R ( \mathbf { A } )$ : Range of matrix A. rank(A): Rank of matrix A. $\mathrm { T r } ( \mathbf A )$ : Trace of matrix A. $\| \mathbf { x } \|$ : Norm of vector x. A subscript is used to specify the 1-norm, 2-norm, or infinity norm. $\| \mathbf { A } \|$ : Norm of matrix A. A subscript is used to specify the 1-norm, 2-norm, or infinity norm.   
• $\mathbf { G } ^ { \dagger }$ : Generalized inverse of matrix $\mathbf { G }$ . $\mathbf { m } _ { \dagger }$ : Generalized inverse solution $\mathbf { m } _ { \dagger } = \mathbf { G } ^ { \dagger } \mathbf { d }$ . $\mathbf { G } ^ { \sharp }$ : A regularized generalized inverse of matrix $\mathbf { G }$ . $E [ X ]$ : Expected value of random variable $X$ . a¯: Mean value of elements in vector a. $N ( \mu , \sigma ^ { 2 } )$ : Normal probability distribution with expected value $\mu$ and variance $\sigma ^ { 2 }$ . $\operatorname { C o v } ( X , Y )$ : Covariance of random variables $X$ and $Y$ .   
• $\operatorname { C o v } ( \mathbf { x } )$ : Matrix of covariances of elements of vector $\mathbf { x }$ .   
• $\rho ( X , Y )$ : Correlation between random variables $X$ and $Y$ . $\mathrm { V a r } ( X )$ : Variance of random variable $X$ . $f ( \mathbf { d } | \mathbf { m } )$ : Conditional probability density for $\mathbf { d }$ , conditioned on a particular model m. $L ( \mathbf { m } | \mathbf { d } )$ : Likelihood function for a model $\mathbf { m }$ , given a particular data vector d. $\sigma$ : Standard deviation. $\sigma ^ { 2 }$ : Variance.   
. $\nabla f ( \mathbf { x } )$ : Gradient of function $f ( \mathbf { x } )$ . $\mathbf { J } ( \mathbf { x } )$ : Jacobian of vector-valued function, $\mathbf { F } ( \mathbf { x } )$ . $\mathbf { H } ( f ( \mathbf { x } ) )$ : Hessian of scalar-valued function $f ( \mathbf { x } )$ .   
[1] R. C. Aster. On projecting error ellipsoids. Bulletin of the Seismological Society of America, 78(3): 1373–1374, 1988.   
[2] G. Backus and F. Gilbert. Uniqueness in the inversion of inaccurate gross earth data. Philosophical Transactions of the Royal Society A, 266:123–192, 1970.   
[3] Z. Bai and J. W. Demmel. Computing the generalized singular value decomposition. SIAM Journal on Scientific Computing, 14:1464–1486, 1993.   
[4] L. J. Bain and M. Englehardt. Introduction to Probability and Mathematical Statistics, 2nd ed. Brooks/Cole, Pacific Grove, CA, 2000.   
[5] R. Barrett, M. Berry, T. F. Chan, J. Demmel, J. Donato, V. Eijkhout, R. Pozo, C. Romine, and H. van der Vorst. Templates for the Solution of Linear Systems: Building Blocks for Iterative Methods, 2nd Ed. SIAM, Philadelphia, 1994.   
[6] I. Barrowdale and F. D. K. Roberts. Solution of an overdetermined system of equations in the $l _ { 1 }$ norm. Communications of the ACM, 17(6):319–326, 1974.   
[7] D. M. Bates and D. G. Watts. Nonlinear Regression Analysis and Its Applications. Wiley, New York, 1988.   
[8] J. Baumeister. Stable Solution of Inverse Problems. Vieweg, Braunschweig, 1987.   
[9] C. Bekas, E. Kokiopoulou, and Y. Saad. An estimator for the diagonal of a matrix. Applied Numerical Mathematics, 57(11–12):1214–1229, 2005.   
[10] A. Ben-Israel and T. N. E. Greville. Generalized Inverses, 2nd ed. Springer-Verlag, New York, 2003.   
[11] A. Ben-Tal and A. Nemirovski. Lectures on Modern Convex Optimization: Analysis, Algorithms, and Engineering Applications. SIAM, Philadelphia, 2001.   
[12] J. G. Berryman. Analysis of approximate inverses in tomography. I. Resolution analysis. Optimization and Engineering, 1(1):87–115, 2000.   
[13] J. G. Berryman. Analysis of approximate inverses in tomography. II. Iterative inverses. Optimization and Engineering, 1(4):437–473, 2000.   
[14] M. Bertero and P. Boccacci. Introduction to Inverse Problems in Imaging. Institute of Physics, London, 1998.   
[15] J. T. Betts. Practical Methods for Optimal Control Using Nonlinear Programming. SIAM, Philadelphia, 2001.   
[16] A. Bj ˚ orck. ¨ Numerical Methods for Least Squares Problems. SIAM, Philadelphia, 1996.   
[17] C. G. E. Boender and H. E. Romeijn. Stochastic methods. In R. Horst and P. M. Pardalos, eds., Handbook of Global Optimization, pages 829–869. Kluwer Academic Publishers, Dordrecht, 1995.   
[18] P. T. Boggs, J. R. Donaldson, R. H. Byrd, and R. B. Schnabel. ODRPACK software for weighted orthogonal distance regression. ACM Transactions on Mathematical Software, 15(4):348–364, 1989. Available at http://www.netlib.org/odrpack/.   
[19] L. Boschi. Measures of resolution in global body wave tomography. Geophysical Research Letters, 30:SDE 2-1-SDE 2-4, 2003.   
[20] R. Bracewell. The Fourier Transform and Its Applications, 3rd ed. McGraw-Hill, Boston, 2000.   
[21] A. M. Bruckstein, D. L. Donoho, and M. Elad. From sparse solutions of systems of equations to sparse modeling of signals and images. SIAM Review, 51(1):34–81, 2009.   
[22] D. Calvetti and E. Somersalo. Introduction to Bayesian Scientific Computing: Ten Lectures on Subjective Computing. Springer, New York, 2007.   
[23] S. L. Campbell and C. D. Meyer, Jr. Generalized Inverses of Linear Transformations. Dover, Mineola, NY, 1991.   
[24] E. J. Candes, J. K. Romberg, and T. Tao. Robust uncertainty principles: Exact signal reconstruc- \` tion from highly incomplete frequency information. IEEE Transactions on Information Theory, 52(2): 489–509, 2006.   
[25] E. J. Candes, J. K. Romberg, and T. Tao. Stable signal recovery from incomplete and inaccurate \` measurements. Communications on Pure and Applied Mathematics, 59(8):1207–1223, 2006.   
[26] E. J. Candes and T. Tao. Near-optimal signal recovery from random projections: Universal encoding \` strategies? IEEE Transactions on Information Theory, 52(12):5406–5425, 2006.   
[27] E. J. Candes and M. B. Wakin. An introduction to compressive sampling. \` IEEE Signal Processing Magazine, 25(2):21–30, 2008.   
[28] P. Carrion. Inverse Problems and Tomography in Acoustics and Seismology. Penn, Atlanta, GA, 1987.   
[29] G. Casella and R. L. Berger. Statistical Inference, 2nd ed. Duxbury, Pacific Grove, CA, 2002.   
[30] Y. Censor and S. A. Zenios. Parallel Optimization: Theory, Algorithms, and Applications. Oxford University Press, New York, 1997.   
[31] J. F. Claerbout and F. Muir. Robust modeling with erratic data. Geophysics, 38(5):826–844, 1973.   
[32] T. F. Coleman and Y. Li. A globally and quadratically convergent method for linear $l _ { 1 }$ problems. Mathematical Programming, 56:189–222, 1992.   
[33] S. C. Constable, R. L. Parker, and C. G. Constable. Occam’s inversion: A practical algorithm for generating smooth models from electromagnetic sounding data. Geophysics, 52(3):289–300, 1987.   
[34] G. Corliss, C. Faure, A. Griewank, L. Hascoet, and U. Naumann. Automatic Differentiation of Algorithms. Springer-Verlag, Berlin, 2002.   
[35] R. T. Cox. Algebra of Probable Inference. Johns Hopkins University Press, Baltimore, 2002.   
[36] P. Craven and G. Wahba. Smoothing noisy data with spline functions: Estimating the correct degree of smoothing by the method of generalized cross-validation. Numerische Mathematik, 31:377–403, 1979.   
[37] M. M. Deal and G. Nolet. Comment on estimation of resolution and covariance for large matrix inversions by J. Zhang and G. A. McMechan. Geophysical Journal International, 127(1):245–250, 1996.   
[38] J. W. Demmel. Applied Numerical Linear Algebra. SIAM, Philadelphia, 1997.   
[39] J. E. Dennis, Jr. and R. B. Schnabel. Numerical Methods for Unconstrained Optimization and Nonlinear Equations. SIAM, Philadelphia, 1996.   
[40] N. R. Draper and H. Smith. Applied Regression Analysis, 3rd ed. Wiley, New York, 1998.   
[41] C. Eckart and G. Young. A principal axis transformation for non-Hermitian matrices. Bulletin of the American Mathematical Society, 45:118–121, 1939.   
[42] A. W. F. Edwards. Likelihood. Johns Hopkins University Press, Baltimore, 1992.   
[43] L. El Ghaoui and H. Lebret. Robust solutions to least-squares problems with uncertain data. SIAM Journal on Matrix Analysis and Applications, 18(4):1035–1064, 1997.   
[44] H. W. Engl. Regularization methods for the stable solution of inverse problems. Surveys on Mathematics for Industry, 3:71–143, 1993.   
[45] H. W. Engl, M. Hanke, and A. Neubauer. Regularization of Inverse Problems. Kluwer Academic Publishers, Boston, 1996.   
[46] R. M. Errico. What is an adjoint model? Bulletin of the American Meteorological Society, 78(11): 2577–2591, 1997.   
[47] M. Evans, N. Hasting, and B. Peacock. Statistical Distributions, 2nd ed. John Wiley & Sons, New York, 1993.   
[48] S. N. Evans and P. B. Stark. Inverse problems as statistics. Inverse Problems, 18:R1–R43, 2002.   
[49] J. G. Ferris and D. B. Knowles. The Slug-Injection Test for Estimating the Coefficient of Transmissibility of an Aquifer. In U.S. Geological Survey Water Supply Paper 1536-I, pages 299–304. U.S. Geological Survey, Washington, DC, 1963.   
[50] A. Frommer and P. Maass. Fast CG-based methods for Tikhonov-Phillips regularization. SIAM Journal on Scientific Computing, 20(5):1831–1850, 1999.   
[51] A. Gelman, J. B. Carlin, H. S. Stern, and D. B. Rubin. Bayesian Data Analysis, 2nd ed. Chapman & Hall/CRC Press, Boca Raton, FL, 2003.   
[52] M. Th. van Genuchten. A closed-form equation for predicting the hydraulic conductivity of unsaturated soils. Soil Science Society of America Journal, 44:892–898, 1980.   
[53] G. H. Golub and C. F. van Loan. Matrix Computations, 3rd ed. Johns Hopkins University Press, Baltimore, 1996.   
[54] G. H. Golub and U. von Matt. Generalized cross-validation for large-scale problems. Journal of Computational and Graphical Statistics, 6(1):1–34, 1997.   
[55] G. H. Golub and D. P. O’Leary. Some history of the conjugate gradient and Lanczos methods. SIAM Review, 31(1):50–102, 1989.   
[56] W. P. Gouveia and J. A. Scales. Resolution of seismic waveform inversion: Bayes versus Occam. Inverse Problems, 13(2):323–349, 1997.   
[57] A. Griewank. Evaluating Derivatives: Principles and Techniques of Algorithmic Differentiation. SIAM, Philadelphia, 2000.   
[58] I. Griva, S. G. Nash, and A. Sofer. Linear and Nonlinear Programming, 2nd ed. SIAM, Philadelphia, 2008.   
[59] C. W. Groetsch. Inverse Problems in the Mathematical Sciences. Vieweg, Braunschweig, 1993.   
[60] D. Gubbins. Time Series Analysis and Inverse Theory for Geophysicists. Cambridge University Press, Cambridge, 2004.   
[61] M. Hanke. Conjugate Gradient Type Methods for Ill-Posed Problems. CRC Press, New York, 1995.   
[62] P. C. Hansen. Relations between SVD and GSVD of discrete regularization problems in standard and general form. Linear Algebra and Its Applications, 141:165–176, 1990.   
[63] P. C. Hansen. Analysis of discrete ill-posed problems by means of the L-curve. SIAM Review, 34(4):561–580, 1992.   
[64] P. C. Hansen. Regularization tools: A MATLAB package for analysis and solution of discrete ill-posed problems. Numerical Algorithms, 6(I–II):1–35, 1994. http://www.imm.dtu.dk/documents/ users/pch/Regutools/regutools.html.   
[65] P. C. Hansen. Rank-Deficient and Discrete Ill-Posed Problems: Numerical Aspects of Linear Inversion. SIAM, Philadelphia, 1998.   
[66] P. C. Hansen. Deconvolution and regularization with Toeplitz matrices. Numerical Algorithms, 29:323–378, 2002.   
[67] P. C. Hansen. Discrete Inverse Problems: Insight and Algorithms. Society for Industrial and Applied Mathematics, Philadelphia, 2010.   
[68] J. M. H. Hendrickx. Bosque del Apache soil data. Personal communication, 2003.   
[69] J. M. H. Hendrickx, B. Borchers, J. D. Rhoades, D. L. Corwin, S. M. Lesch, A. C. Hilgendorf, and J. Schlue. Inversion of soil conductivity profiles from electromagnetic induction measurements: Theory and experimental verification. Soil Science Society of America Journal, 66(3):673–685, 2002.   
[70] G. T. Herman. Image Reconstruction from Projections. Academic Press, San Francisco, 1980.   
[71] M. R. Hestenes. Conjugacy and gradients. In Stephen G. Nash, ed., A History of Scientific Computing, pages 167–179. ACM Press, New York, 1990.   
[72] M. R. Hestenes and E. Stiefel. Methods of conjugate gradients for solving linear systems. Journal of Research, National Bureau of Standards, 49:409–436, 1952.   
[73] J. A. Hildebrand, J. M. Stevenson, P. T. C. Hammer, M. A. Zumberge, R. L. Parker, C. J. Fox, and P. J. Meis. A sea–floor and sea–surface gravity survey of axial volcano. Journal of Geophysical Research, 95(B8):12751–12763, 1990.   
[74] R. A. Horn and C. R. Johnson. Matrix Analysis. Cambridge University Press, Cambridge, 1985.   
[75] R. Horst and P. M. Pardalos. Handbook of Global Optimization. Kluwer Academic Publishers, Dordrecht, 1995.   
[76] R. Horst, P. M. Pardalos, and N. V. Thoai. Introduction to Global Optimization. Kluwer Academic Publishers, Dordrecht, 1995.   
[77] P. J. Huber. Robust Statistical Procedures, 2nd ed. SIAM, Philadelphia, 1996.   
[78] S. von Huffel and J. Vandewalle. The Total Least Squares Problem: Computational Aspects and Analysis. SIAM, Philadelphia, 1991.   
[79] H. Iyer and K. Hirahara (eds.). Seismic Tomography. Chapman & Hall, New York and London, 1993.   
[80] E. T. Jaynes. Probability Theory: The Logic of Science. Cambridge University Press, Cambridge, 2003.   
[81] H. Jeffreys. Theory of Probability. Oxford University Press, New York, 1998.   
[82] W. H. Jeffreys, M. J. Fitzpatrick, and B. E. McArthur. Gaussfit—a system for least squares and robust estimation. Celestial Mechanics, 41(1–4):39–49, 1987. Available at http://clyde.as.utexas.edu/ Gaussfit.html.   
[83] J. Kaipio and E. Somersalo. Statistical and Computational Inverse Problems. Springer, New York, 2004.   
[84] A. C. Kak and M. Slaney. Principles of Computerized Tomographic Imaging. SIAM, Philadelphia, 2001. Transactions on Medical Imaging, 15(3):385–389, 1996. [86] L. Kaufman and A. Neumaier. Regularization of ill-posed problems by envelope guided conjugate gradients. Journal of Computational and Graphical Statistics, 6(4):451–463, 1997. [87] C. T. Kelley. Iterative Methods for Solving Linear and Nonlinear Equations. SIAM, Philadelphia, 1995.   
[88] C. T. Kelley. Solving Nonlinear Equations with Newton’s Method. SIAM, Philadelphia, 2003.   
[89] W. J. Kennedy, Jr. and J. E. Gentle. Statistical Computing. Marcel Dekker, New York, 1980. [90] A. Kirsch. An Introduction to the Mathematical Theory of Inverse Problems. Springer-Verlag, New York, 1996.   
[91] F. J. Klopping, G. Peter, D. S. Robertson, K. A. Berstis, R. E. Moose, and W. E. Carter. Improvements in absolute gravity observations. Journal of Geophysical Research, 96(B5):8295–8303, 1991.   
[92] C. Lanczos. Solutions of systems of linear equations by minimized iterations. Journal of Research, National Bureau of Standards, 49:33–53, 1952. [93] C. Lanczos. Linear Differential Operators. Dover, Mineola, NY, 1997.   
[94] C. L. Lawson and R. J. Hanson. Solving Least Squares Problems. SIAM, Philadelphia, 1995.   
[95] D. C. Lay. Linear Algebra and Its Applications, 3rd ed. Addison-Wesley, Boston, 2003.   
[96] T. Lay and T. Wallace. Modern Global Seismology. Academic Press, San Diego, 1995. [97] J.-J. Leveque, L. Rivera, and G. Wittlinger. On the use of the checker-board test to assess the resolution of tomographic inversions. Geophysical Journal International, 115(1):313–318, 1993.   
[98] Z.-P. Liang and P. C. Lauterbur. Principles of Magnetic Resonance Imaging: A Signal Processing Perspective. IEEE Press, New York, 2000.   
[99] L. R. Lines, ed. Inversion of Geophysical Data. Society of Exploration Geophysicists, Tulsa, OK, 1988.   
[100] T.-W. Lo and P. Inderwiesen. Fundamentals of Seismic Tomography. Society of Exploration Geophysicists, Tulsa, OK, 1994.   
[101] C. F. van Loan. Generalizing the singular value decomposition. SIAM Journal on Numerical Analysis, 13:76–83, 1976.   
[102] D. G. Luenberger. Optimization by Vector Space Methods. John Wiley and Sons, New York, 1969.   
[103] J. MacCarthy, B. Borchers, and R. Aster. Estimating the model resolution matrix diagonal and generalized cross-validation for large geophysical inverse problems. Journal of Geophysical Research, 2011. In press.   
[104] D. Mackenzie. Compressed sensing makes every pixel count. In What’s Happening in the Mathematical Sciences. American Mathematical Society, Providence, RI, 2009.   
[105] W. H. Marlow. Mathematics for Operations Research. Dover, Mineola, NY, 1993.   
[106] P. J. McCarthy. Direct analytic model of the L-curve for Tikhonov regularization parameter selection. Inverse Problems, 19:643–663, 2003.   
[107] P. R. McGillivray and D. Oldenburg. Methods for calculating Frechet derivatives and sensitivities for the non-linear inverse problem: A comparative study. Geophysical Prospecting, 38:499–524, 1990.   
[108] W. Menke. Geophysical Data Analysis: Discrete Inverse Theory, volume 45 of International Geophysics Series, rev. ed. Academic Press, San Diego, 1989.   
[109] C. D. Meyer. Matrix Analysis and Applied Linear Algebra. SIAM, Philadelphia, 2000.   
[110] E. H. Moore. On the reciprocal of the general algebraic matrix. Bulletin of the American Mathematical Society, 26:394–395, 1920.   
[111] J. J. More, B. S. Garbow, and K. E. Hillstrom. User guide for MINPACK-1. Technical Report ANL-80-74, Argonne National Laboratory, 1980.   
[112] V. A. Morozov. Methods for Solving Incorrectly Posed Problems. Springer-Verlag, New York, 1984.   
[113] R. H. Myers. Classical and Modern Regression with Applications, 2nd ed. PWS Kent, Boston, 1990.   
[114] F. Natterer. The Mathematics of Computerized Tomography. SIAM, Philadelphia, 2001.   
[115] F. Natterer and F. Wubbeling. ¨ Mathematical Methods in Image Reconstruction. SIAM, Philadelphia, 2001.   
[116] A. Neumaier. Solving ill-conditioned and singular linear systems: A tutorial on regularization. SIAM Review, 40(3):636–666, 1998.   
[117] R. Neupauer, B. Borchers, and J. L. Wilson. Comparison of inverse methods for reconstructing the release history of a groundwater contamination source. Water Resources Research, 36(9):2469–2475, 2000.   
[118] I. Newton. The Principia, Mathematical Principles of Natural Philosophy, trans. by I. B. Cohen and A. Whitman. University of California Press, Berkeley, 1999.   
[120] G. Nolet. Solving or resolving inadequate and noisy tomographic systems. Journal of Computational Physics, 61(3):463–482, 1985.   
[121] G. Nolet, ed. Seismic Tomography with Applications in Global Seismology and Exploration Geophysics. D. Reidel, Boston, 1987.   
[122] S. J. Osher and R. P. Fedkiw. Level Set Methods and Dynamic Implicit Surfaces. Springer-Verlag, New York, 2002.   
[123] C. C. Paige and M. A. Saunders. Algorithm 583 LSQR: Sparse linear equations and least-squares problems. ACM Transactions on Mathematical Software, 8(2):195–209, 1982.   
[124] C. C. Paige and M. A. Saunders. LSQR: An algorithm for sparse linear equations and sparse least squares. ACM Transactions on Mathematical Software, 8(1):43–71, 1982.   
[125] R. L. Parker. A theory of ideal bodies for seamount magnetism. Journal of Geophysical Research, 96(B10):16101–16112, 1991.   
[126] R. L. Parker. Geophysical Inverse Theory. Princeton University Press, Princeton, NJ, 1994.   
[127] R. L. Parker and M. K. McNutt. Statistics for the one-norm misfit measure. Journal of Geophysical Research, 85:4429–4430, 1980.   
[128] R. L. Parker and M. A. Zumberge. An analysis of geophysical experiments to test Newton’s law of gravity. Nature, 342:29–32, 1989.   
[129] R. Penrose. A generalized inverse for matrices. Mathematical Proceedings of the Cambridge Philosophical Society, 51:406–413, 1955.   
[130] S. Portnoy and R. Koenker. The Gaussian hare and the Laplacian tortoise: Computability of squarederror versus absolute-error estimators. Statistical Science, 12:279–296, 1997.   
[131] M. B. Priestley. Spectral Analysis and Time Series. Academic Press, London, 1983.   
[132] W. Rison, R. J. Thomas, P. R. Krehbiel, T. Hamlin, and J. Harlin. A GPS-based three-dimensional lightning mapping system: Initial observations in central New Mexico. Geophysical Research Letters, 26(23):3573–3576, 1999.   
[133] C. D. Rodgers. Inverse Methods for Atmospheric Sounding: Theory and Practice. Word Scientific Publishing, Singapore, 2000.   
[134] W. Rudin. Real and Complex Analysis, 3rd ed. McGraw-Hill, New York, 1987.   
[135] Y. Saad. Iterative Methods for Sparse Linear Systems, 2nd ed. SIAM, Philadelphia, 2003.   
[136] L. J. Savage. The Foundation of Statistics, 2nd ed. Dover, Mineola, NY, 1972.   
[137] J. Scales and M. Smith. DRAFT: Geophysical inverse theory. http://landau.Mines.EDU/samizdat/ inverse theory/, 1997.   
[138] J. A. Scales, A. Gersztenkorn, and S. Treitel. Fast lp solution of large, sparse, linear systems: Application to seismic travel time tomography. Journal of Computational Physics, 75(2):314–333, 1988.   
[139] S. R. Searle. Matrix Algebra Useful for Statistics. Wiley-Interscience, New York, 2006.   
[140] M. K. Sen and P. L. Stoffa. Global Optimization Methods in Geophysical Inversion. Number 4 in Advances in Exploration Geophysics. Elsevier, New York, 1995.   
[141] C. B. Shaw, Jr. Improvement of the resolution of an instrument by numerical solution of an integral equation. Journal of Mathematical Analysis and Applications, 37:83–112, 1972.   
[142] J. R. Shewchuk. An introduction to the Conjugate Gradient Method without the agonizing pain. Technical report, School of Computer Science, Carnegie Mellon University, 1994. http://www.cs. cmu.edu/jrs/jrspapers.html.   
[143] D. S. Sivia and J. Skilling. Data Analysis: A Bayesian Tutorial, 2nd ed. Oxford University Press, New York, 2006.   
[144] T. H. Skaggs and Z. J. Kabala. Recovering the release history of a groundwater contaminant. Water Resources Research, 30(1):71–79, 1994.   
[145] T. H. Skaggs and Z. J. Kabala. Recovering the history of a groundwater contaminant plume: Method of quasi-reversibility. Water Resources Research, 31:2669–2673, 1995.   
[146] A. Van der Sluis and H. A. Van der Vorst. Numerical solution of large, sparse linear algebraic systems arising from tomographic problems. In G. Nolet, ed., Seismic Tomography, pages 49–83. D. Reidel, Hingham, MA, 1987.   
[147] W. Spakman and G. Nolet. Imaging algorithms, accuracy and resolution in delay time tomography. In M. J. R. Wortel, N. J. Vlaar, G. Nolet, and S. A. P. L. Cloetingh, eds., Mathematical Geophysics: A Survey of Recent Developments in Seismology and Geodynamics, pages 155–187. D. Reidel, Dordrecht, 1988.   
[148] P. B. Stark and R. L. Parker. Velocity bounds from statistical estimates of $\tau ( p )$ and $x ( p )$ . Journal of Geophysical Research, 92(B3):2713–2719, 1987.   
[149] P. B. Stark and R. L. Parker. Correction to “velocity bounds from statistical estimates of $\tau ( p )$ and $x ( p )$ .” Journal of Geophysical Research, 93:13821–13822, 1988.   
[150] P. B. Stark and R. L. Parker. Bounded-variable least-squares: An algorithm and applications. Computational Statistics, 10(2):129–141, 1995.   
[151] G. W. Stewart. On the early history of the singular value decomposition. SIAM Review, 35:551–566, 1993.   
[152] G. Strang. Linear Algebra and Its Applications, 3rd ed. Harcourt Brace Jovanovich, San Diego, 1988.   
[153] G. Strang and K. Borre. Linear Algebra, Geodesy, and GPS. Wellesley–Cambridge Press, Wellesley, MA, 1997.   
[154] N. Z. Sun. Inverse Problems in Groundwater Modeling. Kluwer Academic Publishers, Boston, 1984.   
[155] A. Tarantola. Inverse Problem Theory and Methods for Model Parameter Estimation. SIAM, Philadelphia, 2004.   
[156] A. Tarantola and B. Valette. Inverse problems $=$ quest for information. Journal of Geophysics, 50(3):159–170, 1982.   
[157] R. A. Thisted. Elements of Statistical Computing. Chapman and Hall, New York, 1988.   
[158] C. Thurber. Hypocenter velocity structure coupling in local earthquake tomography. Physics of the Earth and Planetary Interiors, 75(1–3):55–62, 1992.   
[159] C. Thurber and K. Aki. Three-dimensional seismic imaging. Annual Review of Earth and Planetary Sciences, 15:115–139, 1987.   
[160] C. Thurber and J. Ritsema. Theory and observations—seismic tomography and inverse methods. In Treatise on Geophysics, pages 323–360. Elsevier, Amsterdam, 2007.   
[161] A. N. Tikhonov and V. Y. Arsenin. Solutions of Ill-Posed Problems. Halsted Press, New York, 1977.   
[162] A. N. Tikhonov and A. V. Goncharsky, eds. Ill-Posed Problems in the Natural Sciences. MIR Publishers, Moscow, 1987.   
[163] J. Trampert and J.-J. Lev´ eque. Simultaneous iterative reconstruction technique: Physical interpreta- ´ tion based on the generalized least squares solution. Journal of Geophysical Research, 95(B8):12553– 12559, 1990.   
[164] L. N. Trefethen and D. Bau. Numerical Linear Algebra. SIAM, Philadelphia, 1997.   
[165] J. Tromp, C. Tape, and Q. Liu. Seismic tomography, adjoint methods, time reversal, and bananadoughnut kernels. Geophysical Journal International, 160:195–216, 2005.   
[166] S. Twomey. Introduction to the Mathematics of Inversion in Remote Sensing and Indirect Measurements. Dover, Mineola, NY, 1996.   
[167] J. Um and C. Thurber. A fast algorithm for 2-point seismic ray tracing. Bulletin of the Seismological Society of America, 77(3):972–986, 1987.   
[168] C. R. Vogel. Non-convergence of the L-curve regularization parameter selection method. Inverse Problems, 12:535–547, 1996.   
[169] C. R. Vogel. Computational Methods for Inverse Problems. SIAM, Philadelphia, 2002.   
[170] G. Wahba. Spline Models for Observational Data. SIAM, Philadelphia, 1990.   
[171] G. A. Watson. Approximation in normed linear spaces. Journal of Computational and Applied Mathematics, 121(1–2):1–36, 2000.   
[172] G. M. Wing. A Primer on Integral Equations of the First Kind: The Problem of Deconvolution and Unfolding. SIAM, Philadelphia, 1991.   
[173] H. Zhang and C. H. Thurber. Estimating the model resolution matrix for large seismic tomography problems based on Lanczos bidiagonalization with partial reorthogonalization. Geophysical Journal International, 170(1):337–345, 2007.   
[174] J. Zhang and G. A. McMechan. Estimation of resolution and covariance for large matrix inversions. Geophysical Journal International, 121(2):409–426, 1995.

Note: Bold entries signify the introduction and/or definition of a topic.

$\infty$ -norm, 305, 305–307, 313   
0-norm, 174   
1-norm, 6, 43–48, 50, 53, 305, 306, 307, 313   
2-norm, 6, 26, 59, 109, 114, 243, 298, 301, 305,   
306, 311, 345

# A

acceptance ratio, 271   
adjoint equation, 252   
advection–diffusion equation, 12–17, 170   
algebraic reconstruction technique, 146, 146–149,   
166   
aliasing, 201, 202   
ART, see algebraic reconstruction technique   
augmented matrix, 284, 285, 293   
automatic differentiation, 228   
averaging kernel, 64, 135, 135–139

# B

B-splines, 140   
Backus–Gilbert method, 64, 134–139   
basis, 58, 62, 65, 67, 70, 71, 80, 81, 113, 121, 140, 150–151, 154, 198, 199, 281, 296, 303, 314 Fourier, 196, 200, 213 orthogonal, 139, 299, 300, 301 orthonormal, 55–56, 60, 139, 297, 299, 309 standard, 22, 296   
Bayes’ theorem, 256, 327   
Bayesian statistics, 255–280, 316   
biased estimator, 19, 32, 62, 63, 99, 102, 281   
bounded variables least squares problem, 170, 170–174   
BVLS, see bounded variables least squares problem

# C

CDF, see cumulative distribution function   
central limit theorem, 30, 330   
CG, see conjugate gradient method   
CGLS, see conjugate gradient least squares method   
characteristic equation, 302   
checkerboard resolution test, 87, 91, 249   
chi–square test, 29, 34, 226, 246   
Cholesky factorization, 141, 154, 262, 278, 304, 314, 330   
circular convolution, 202   
collocation, 15, 16, 90, 103, 124, 137, 202   
column space, see range   
compact form of the singular value decomposition, 56   
complex conjugate, 310   
complex number, 310 absolute value, 310   
compressive sensing, 183   
condition number, 65, 67, 76, 81, 91, 119, 120, 139, 140, 246, 306, 307   
conditional distribution, 27, 256, 328   
conditional expected value, 328   
conditional probability, 327   
confidence ellipsoids, see confidence regions   
confidence intervals, 32, 39–41, 48–50, 102, 226, 230, 232, 234, 253, 254, 262, 281, 333, 333–334, 336, 337   
confidence regions, 34, 34–37, 39, 49, 228   
conjugate distribution, 259   
conjugate gradient least squares method, 155, 155–159, 167, 168, 254   
conjugate gradient method, 150, 150–155, 252   
continuous inverse problem, 2, 3, 91, 134, 140, 281   
contour plot, 227–228   
convex function, 45, 150, 230, 340   
convolution, 4, 8, 9, 12, 17, 76, 156, 193–203, 215   
convolution theorem, 197, 203, 213   
correlation, 35, 49, 234, 323   
covariance, 36, 262, 279, 323, 336   
covariance matrix, 31–36, 40, 48–51, 62, 101, 102, 224–226, 233, 236, 260–269, 329, 336   
critical point, 339, 340   
cross-well tomography, 13, 125, 126, 240–244, 251   
cumulative distribution function, 321, 322, 324, 326, 328, 331, 336

# D

damped least squares problem, 94, 95, 103, 124, 240, 244, 245   
damped SVD method, 97   
data kernels, see representers   
data null space, 56, 58, 61, 71, 90   
deconvolution, 4, 76–81, 84, 177, 193, 202–207, 213, 215   
delta function, 75, 135, 193, 198, 279   
denoising, 187   
dense matrix, 141, 141–142, 157   
determinant, 302   
DFT, see discrete Fourier transform   
diagonalization of a matrix, 35, 303   
discrepancy principle, 67, 77, 95, 98, 99, 102, 124, 125, 127, 156, 241, 243, 244   
discrete Fourier transform, 199, 199–216   
discrete ill-posed problem, 20, 74, 74–87, 93, 121, 156 mildly ill-posed, 74 moderately ill-posed, 74, 108 severely ill-posed, 74, 81   
discrete inverse problem, 2, 3, 19, 25, 28, 74, 91, 215, 239, 296   
distribution chi-square, 29, 34, 67, 253, 319, 329 double-sided exponential, 43, 319 exponential, 319, 328, 336, 337 Gaussian, see distribution, normal multivariate normal, 26, 28, 30–32, 34, 38, 39, 43, 47–49, 62, 145, 220, 224, 225, 232, 244, 252, 253, 257, 260–269, 281, 329, 329–330, 332–334, 336, 337 normal, 30, 32, 39, 43, 259, 317, 330–337 Student’s t, 39, 52, 319, 333 uniform, 30, 52, 232, 278, 317   
dot product, 65, 67, 298, 299, 305, 311, 342, 345   
double-sided exponential distribution, see distribution, double-sided exponential

# E

earthquake location problem, 7, 13, 235–236   
eigenvalue, 35, 56, 57, 60, 302, 302–304, 306, 313, 345   
eigenvector, 35, 56, 57, 60, 302, 302–304, 345   
elementary row operations, 284   
expected value, 31, 63, 117, 321, 322–324, 328–330, 336

exponential distribution, see distribution, exponential

# F

fast Fourier transform, 200, 202–204, 213   
Fermat’s least-time principle, 241   
FFT, see fast Fourier transform   
filter factors, 96, 100, 104, 107, 108, 113, 166, 168   
finite-difference derivatives, 104, 228, 229, 246, 252   
forward problem, 2, 4, 6, 16, 22, 27, 202, 203   
Fourier basis functions, see basis, Fourier   
Fourier transform, 4, 195, 195–216   
Frechet derivatives,´ 252   
Fredholm integral equation of the first kind, 3, 14, 74, 140   
frequency response, 196   
Frobenius norm, 306, 308   
full rank least squares problem, see matrix, full rank

# G

gamma function, 29, 34, 319   
Gauss-Newton method, 222, 222–223, 228–232, 235, 238, 240, 241, 245, 251, 252, 254   
Gaussian distribution, see distribution, normal   
Gaussian elimination, 283, 283–285   
Gaussian point spread function, 156, 167   
GCV, see generalized cross-validation   
generalized cross-validation, 115, 119, 124, 127, 162   
generalized singular value decomposition, 104, 114, 127   
Geonics EM-38 ground conductivity meter, 246–248   
global optimization, 231, 231–234, 238, 254   
GN method, see Gauss–Newton method   
Gosset, W. S., 319   
gradient, 46, 219, 221, 229, 339, 340, 342–344   
Gram matrix, 132, 139, 140, 312   
Gram-Schmidt orthogonalization process, 301, 314   
Green’s function, 194, 215   
GSVD, see generalized singular value decomposition

#

Heaviside step function, 8   
Hermitian symmetry, 200, 214   
Hermitian transpose, 310

Hessian, 219, 221, 222, 224, 237, 340, 344 higher-order Tikhonov regularization, 103, 104, 113–115, 117, 124, 125, 215, 254 histogram, 50–52, 330–332, 337

# I

identity matrix, see matrix, identity   
IDFT, see inverse Fourier transform, discrete   
IFFT, see inverse Fourier transform, fast   
IFK, 14, see Fredholm integral equation of the first kind   
ill-posed problem, see discrete ill-posed problem   
image deblurring, 156–159, 167, 168   
impulse resolution test, see spike resolution test   
impulse response, 75, 76, 194, 195, 197, 198, 202–205, 215   
indefinite matrix, see matrix, indefinite   
independent random variables, 27, 28, 30–32, 38, 39, 44, 47, 62, 88, 136, 225, 244, 252, 253, 257, 262, 320, 323, 323–326, 329, 330, 332, 333, 336   
inner product, 311   
inverse Fourier transform, 4, 195, 198, 204, 216 discrete, 200, 201, 214 fast, 200   
inverse of a matrix, 34, 58, 290, 291, 292   
IRLS, see iteratively reweighted least squares   
iterative methods, 46–47, 53, 141–168, 241, 244, 252, 254   
iteratively reweighted least squares, 46–48, 50, 53, 167

# J

Jacobian, 218, 221, 226, 240, 244, 246, 251, 269, 340   
JDF, see joint probability density function   
joint probability density function, 27, 323, 324, 326, 329

K Kaczmarz’s algorithm, 142, 142–149, 166

L   
L-curve, 95, 97, 98, 108, 119, 124–127, 156–158, 170, 241   
Lagrange multipliers, 94, 124, 132, 136, 137, 191, 341, 341–345   
Landweber iteration, 166   
Laplacian operator, 104, 126, 241, 244, 252   
law of total probability, 327, 328   
least squares problem, 26–32, 38, 40–46, 48, 49, 51, 52, 55, 58–60, 62, 68, 77, 93, 155, 157, 170, 253, 261, 278, 281, 301, 302, 305, 308, 309, 312, 345   
least squares solution, see least squares problem   
leave-one-out cross-validation, 115   
Legendre polynomials, 139   
Levenberg-Marquardt method, 222, 222–223, 228–236, 238, 240, 246, 254   
likelihood function, see maximum likelihood estimation   
line search, 219, 220   
linear combination, 19, 22, 31, 56, 59, 65, 121, 140, 200, 287, 295–298   
linear independence, 56, 95, 139, 140, 167, 292, 293, 296, 297, 302, 303, 311–313   
linear regression, 4, 25–48, 52, 127, 139, 220, 225–227   
linear systems, 3   
LM method, see Levenberg–Marquardt method   
local minimum points, 219, 230, 232, 235, 237, 240, 251, 254, 269, 282, 343

#

MAP model, see maximum a posteriori model   
Markov Chain Monte Carlo method, 270   
mathematical model, 2, 11, 12, 30, 43, 44, 49, 90, 156, 198, 214, 226, 246, 252, 253   
MATLAB commands bvls, 170 chi2pdf, 50 chol, 304 cond, 67, 308 conv, 202 dct2, 182 eig, 303 fft, 200 fftn, 216 ifft, 200 ifftn, 216 lsqnonneg, 169 lsqr, 159, 168 norm, 305 normest, 167 null, 296 orth, 297, 301 pinv, 57   
MATLAB commands (continued) qr, 308 randn, 324 rank, 81, 298 reshape, 70 rref, 285 sqrtm, 261 svd, 55 xcorr, 266   
matrix diagonal, 28, 31, 35, 46, 55, 56, 60, 100, 203, 291 full column rank, 25, 26, 58, 63, 298, 308, 309, 313 full rank, 58, 67, 95, 298, 329 full row rank, 298 identity, 31, 58, 63, 64, 67, 79, 95, 99, 104, 105, 111, 117, 187, 223, 224, 235, 240, 244, 261, 262, 289, 290, 292, 300, 302 indefinite, 304 lower-triangular, 16, 291 orthogonal, 55, 56, 58, 60, 104, 141, 300, 303, 308–309 positive definite, 34, 150, 154, 155, 167, 220, 261, 278, 304, 312, 313, 340 positive semidefinite, 304, 312, 313 rank-deficient, 18, 19, 55, 68, 71, 298 square root, 261, 278 symmetric, 34, 63, 150, 152, 154, 167, 278, 291, 303, 304, 312, 313, 340 upper-triangular, 291, 304, 308   
matrix-matrix product, 288   
matrix norm, 63, 305, 305–308, 313, 345   
matrix-vector product, 287   
maximum a posteriori model, 257, 260–269, 279   
maximum likelihood estimation, 27, 27–29, 43, 50, 51, 220, 253, 254, 257, 269, 280   
maximum likelihood principle, see maximum likelihood estimation   
MCMC, see Markov chain Monte Carlo method   
mean value theorem, 341   
measurement matrix, 183   
median, 45, 67, 322   
Metropolis-Hastings Sampler, 270   
midpoint rule, 15, 18, 76   
minimum length least squares solution, 59, 59–61   
minimum length solution, 94, 144   
mode, 322   
model identification problem, 2   
model null space, 56, 58–60, 63, 70, 90, 199   
model resolution, 19, 62, 62–64, 73–74, 207, 244, 251   
Monte Carlo error propagation, 48   
Moore-Penrose pseudoinverse, 57, 63, 66, 67, 87, 141   
MRE method, see minimum relative entropy method   
MTSVD, see modified truncated SVD   
multicollinearity, 127   
multistart method, 232, 232–234, 240   
MVN, see distribution, multivariate normal

#

Newton’s method, 218, 218–220, 237 damped, 219   
NNLS, see nonnegative least squares method   
non-negative least squares method, 169   
nonlinear least squares problem, 220, 223, 232, 236, 239–241, 246, 254, 257, 269, 281   
nonlinear regression, 220, 220–238   
nonnegative least squares method, 170, 172   
norm, see vector norm, matrix norm   
normal distribution, see distribution, normal   
normal equations, 26, 29, 33, 45, 52, 58, 59, 95, 150, 155, 168, 224, 302, 309, 345   
null space of a matrix, 19, 56, 58–61, 63, 64, 69, 104, 106, 199, 294, 294–297, 299, 309, 312, 313   
Nyquist frequency, 201

# O

objective function, 103, 223, 232, 240, 252, 341   
Occam’s inversion, 244, 244–252   
Occam’s razor, 244, 254   
ordinary cross-validation, see leave one out cross-validation   
orthogonal basis, see basis, orthogonal   
orthogonal functions, 21, 311–312   
orthogonal matrix, see matrix, orthogonal   
orthogonal polynomials, 139   
orthogonal projection, see projection   
orthogonal subspaces, 299   
orthogonal vectors, 61, 104, 151, 152, 299   
orthonormal basis, see basis, orthonormal, 132   
outliers, 6, 42, 42–45, 50   
over-fitting of data, 67

# P

$p$ -value chi–square test, 29, 29–30, 226–228, 233 t-test, 335, 336, 337   
Parseval’s theorem, 197   
PCR, see principle components regression   
PDF, see probability density function   
perpendicular, see orthogonal   
Picard condition, 67, 99   
pivot column, 285, 297, 298, 312   
point spread function, 156, 167   
poles of a transfer function, 199   
posterior distribution, 255, 255–280   
power of a hypothesis test, 335   
power of a matrix, 290   
preconditioning, 168   
principal axes, error ellipsoid, 35   
principle of indifference, 255   
prior distribution, 255, 255–280   
probability density function, 27, 29, 316, 316–320, 336   
projection, 35, 59, 62, 64, 65, 70, 142, 143, 300, 300–301, 305, 311, 312   
proportional effect, 41   
proposal distribution, 271   
pseudoinverse, see Moore–Penrose pseudoinverse

# Q

regularization parameter, 94, 98, 102, 109, 115, 117, 119, 120, 122, 124, 125, 127, 156, 243   
representers, 14, 133–134   
residual vector, 26   
residuals, 6, 26, 29, 31, 38–43, 45–47, 49, 51, 67, 98, 147, 151, 152, 154, 155, 204, 220, 225, 226, 233   
resolution, 248   
resolution kernel, see resolution matrix, model, 64   
resolution matrix data, 64, 67 model, 63, 63–64, 67, 71, 79–81, 90, 99, 101, 111, 112   
resolution test, 64, 73, 81, 91, 249   
ridge regression, 127   
Riemann-Lebesgue lemma, 21   
robust estimation, 6   
robust estimation procedures, 43, 45, 52   
robust least squares, 53   
roughening matrix, 103, 126, 216, 239, 241, 252   
row action methods, 168   
row space of a matrix, 298   
row-column expansion method, 288   
RREF, see reduced row echelon form

Q-Q plot, 51, 52, 330   
QR factorization, 141, 154, 308, 308–309   
quadratic form, 303, 303–304, 340

# S

# R

random variables, 29–31, 39, 255, 316   
range of a matrix, 25, 56, 59, 60, 121–123, 296, 298, 299, 301, 309, 312   
rank, 90   
rank deficient least squares problem, see matrix, rank deficient   
rank of a matrix, 18, 56, 60, 63, 69, 104, 298, 308, 312   
ray-paths, 7, 13, 18, 68–74, 88–91, 142, 146–149, 240–244   
reduced row echelon form, 285, 293, 295–298, 312   
regularization by discretization, 87   
regularization by truncated singular value decomposition, 68   
saddle point, 339   
sample mean, 331, 333, 334, 335, 337   
sampling rate, 199, 200–202, 204, 205, 234   
seismogram, see seismometer   
seismometer, 8, 75–81, 204–207, 214, 215   
seminorm, 103, 109, 241, 242, 305   
serial convolution, 201, 202   
Shaw problem, 11, 11–17, 81–87, 97, 99–102, 123, 166, 262–266   
sifting property of the delta function, 193, 198   
signum function, 45   
simultaneous iterative reconstruction technique, 148, 148–149, 166   
singular value decomposition, 55, 55–61, 68, 69, 89, 91, 93, 95, 99, 100, 102, 121, 141, 154, 157, 166, 167, 213, 254, 278   
singular value spectrum, 64, 67, 74   
SIRT, see simultaneous iterative reconstruction technique   
slowness, 8, 13, 16, 18, 19, 49, 69, 74, 89, 90, 108, 112, 145, 241   
slug test, 226, 226–228   
solution existence, 19, 23   
solution stability, 20, 21, 23, 64–68, 93, 136, 138, 203, 213   
solution uniqueness, 19, 20, 23, 58, 60, 296   
sparse, 157   
sparse matrix, 141, 142, 156, 254   
sparsity regularization, 174   
spectral amplitude, 196, 197, 198, 200, 201, 204, 205, 214   
spectral division, 203, 204, 205   
spectral phase, 196, 198, 200, 201, 214   
spectrum, 195, 196, 213   
spherical harmonic functions, 140   
spike resolution test, 73, 74, 91, 249   
standard basis, 229   
standard deviation, 28, 30, 31, 38, 41, 43, 44, 49, 51, 52, 88, 125, 136, 138, 145, 220, 225, 226, 232–234, 239, 244, 246, 257–259, 261, 262, 322, 324, 331–334, 337   
standard normal distribution, 317, 319, 324, 326, 330   
stationary point, 342, 345   
steepest-descent method, 223   
Student, see Gosset, W. S.   
Student’s $t$ distribution, see distribution, Student’s t   
subspace of $R ^ { m }$ , 297   
subspace of $R ^ { n }$ , 293, 293–294, 298   
SVD, see singular value decomposition   
system of equations, 283 ill-conditioned, 20, 55, 140, 308 over-determined, 286, 305 under-determined, 286 vector form, 287   
Toeplitz matrix, 91   
tomography, 12, 23, 68–74, 125, 142–149, 166, 168, 216, 240–244, 251   
total least squares problem, 53   
total variation regularization, 186, 186–191   
transfer function, see impulse response, 199   
Transition kernel, 270   
transpose of a matrix, 290, 292, 297   
truncated generalized singular value decomposition, 113, 114   
truncated singular value decomposition, 62, 67, 75, 77, 82, 84, 91, 99, 125, 145, 149, 204   
TSVD, see truncated singular value decomposition   
type I error, 335   
type II error, 335, 337

#

unbiased estimator, 32, 62, 93, 281 uncorrelated random variables, 323 uniform distribution, see distribution, uniform uninformative prior distribution, 255

#

van Genuchten, M. Th., 235   
variance, 31, 32, 62, 136, 256, 261, 322, 330, 336   
vector norm, 26, 43, 45, 59, 94, 98, 99, 103, 110, 114, 120, 122–124, 146, 204, 243, 305, 305–306, 309   
vertical seismic profiling, 8, 8–9, 107, 110, 113, 114, 117, 119   
VSP, see vertical seismic profiling

# T

t-test, 334, 335–337   
Taylor’s theorem, 217, 219, 229, 244, 341   
TGSVD, see truncated generalized singular value decomposition   
Tikhonov regularization, 94, 124–127, 141, 156, 157, 170, 223, 239, 244, 254, 255, 262, 266, 281 frequency-domain, 208

# W

water level regularization, 204, 204–213   
wavelets, 140   
wrap-around, 202, 203

Z zeros of a transfer function, 199