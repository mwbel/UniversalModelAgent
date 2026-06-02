# 224 Multistep–multistage–multiderivative methods

While multistep methods, multistage methods and multiderivative methods all exist in their own right, many attempts have been made to combine their attributes so as to obtain new methods of greater power. By introducing higher $y$ derivatives into multistep methods, a new class of methods is found. These are known as Obreshkov methods, after their discoverer Obreshkov (1940).

The best-known combination of the use of higher derivatives with Runge– Kutta methods is in Rosenbrock methods (Rosenbrock, 1963). This is actually a greater generalization, in the sense that derivatives of $f$ are used. These must be regarded as more general, because $y ^ { \prime \prime }$ can be found in the case of an autonomous problem as $y ^ { \prime \prime } ( x ) = f ^ { \prime } ( y ( x ) ) ( f ( y ( x ) ) )$ . On the other hand, it is not possible to compute $f ^ { \prime } ( y ( x ) )$ from values of the various $y$ derivatives. Rosenbrock methods have a role in the solution of stiff problems.

Other potentially useful combinations certainly exist but, in this book, we mainly confine ourselves to combinations of multistage and multiderivative methods. These we refer to as ‘general linear methods’. The various methods that come under the classifications we have discussed here can be seen in a diagrammatic representation in Figure 224(i). The Euler method can be thought of as the infimum of all the method classes, and is shown at the lowest point of this diagram. On the other hand, the class of general linear methods is the supremum of all multistage and multivalue methods. The supremum of all methods, including also those with a multiderivative nature, is represented by the highest point in Figure 224(i).

We have already seen, in Subsection 204, that the implicit Euler method has a role in the solution of stiff problems. Implicitness also exists in the case of linear multistep and Runge–Kutta methods. For example, the second order backward difference formula (also known as BDF2),

$$
y _ { n } = \frac { 2 } { 3 } h f ( x _ { n } , y _ { n } ) + \frac { 4 } { 3 } y _ { n - 1 } - \frac { 1 } { 3 } y _ { n - 2 } ,
$$

is also used for stiff problems. There are also implicit Runge–Kutta methods, suitable for the solution of stiff problems.

Another example of an implicit method is the ‘implicit trapezoidal rule’, given by

$$
y _ { n } = y _ { n - 1 } + { \frac { h } { 2 } } { \big ( } f ( x _ { n } , y _ { n } ) + f ( x _ { n - 1 } , y _ { n - 1 } ) { \big ) } .
$$

Like the Euler method itself, and its implicit variant, (225b) is, at the same time, a linear multistep method and a Runge–Kutta method. As a linear multistep method, it can be regarded as a member of the Adams–Moulton family of methods. As a Runge–Kutta method, it can be regarded as a member of the Lobatto IIIA family.

Implicit methods carry with them the need to solve the nonlinear equation on which the solution, at a new step value, depends. For non-stiff problems, this can be conveniently carried out by fixed-point iteration. For example, the solution of the implicit equation (225b) is usually found by evaluating a starting approximation $\eta ^ { [ 0 ] }$ , given as $y _ { n }$ in (222a). A sequence of approximations $\eta ^ { \left[ k \right] }$ , $k = 1 , 2 , \ldots$ , is then formed by inserting $\eta ^ { \left[ k \right] }$ in place of $y _ { n }$ on the left-hand side of (225b), and $\eta ^ { \lfloor k - 1 \rfloor }$ in place of $y _ { n }$ on the right-hand side. That is,

$$
\eta ^ { [ k ] } = y _ { n - 1 } + { \frac { h } { 2 } } \left( f \left( x _ { n } , \eta ^ { [ k - 1 ] } \right) + f ( x _ { n - 1 } , y _ { n - 1 } ) \right) , \quad k = 1 , 2 , \ldots .
$$

The value of $y _ { n }$ actually used for the solution is the numerically computed limit to this sequence.

For stiff problems, unless $h$ is chosen abnormally small, this sequence will not converge, and more elaborate schemes are needed to evaluate the solution to the implicit equations. These schemes are generally variants of the Newton– Raphson method, and will be discussed further in reference to the particular methods as they arise.
