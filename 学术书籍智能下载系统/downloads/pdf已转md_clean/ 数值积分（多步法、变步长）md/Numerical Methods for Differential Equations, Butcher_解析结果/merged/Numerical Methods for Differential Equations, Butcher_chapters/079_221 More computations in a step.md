# 221 More computations in a step

Instead of computing $f$ only once in each time step, as in the Euler method, we might look for methods which evaluate $f$ (with different arguments, of course) two or more times. We consider a single example of this idea in which $f$ is evaluated twice.

Since the Euler method is based on a left-hand quadrature rule, we might ask how it is possible to base a method on the trapezoidal rule. The difficulty with this is that the derivative at the beginning of the step is known, but at the end it is not known. To overcome this difficulty, one of the two $f$ evaluations can be used to approximate the solution value at the end of the step, using the same approximation that is used in the Euler method. From this first order approximation, an approximation to the derivative at the end of the step is computed. The quota of two $f$ evaluations has now been exhausted, but there is now data available to apply the trapezoidal rule formula.

Putting all these stages of the computation together, we write the algorithm for computing $y _ { n }$ in the form

$$
\begin{array} { l } { { \displaystyle y _ { n } ^ { * } = y _ { n - 1 } + h f \big ( x _ { n - 1 } , y _ { n - 1 } \big ) , } } \\ { { \displaystyle y _ { n } = y _ { n - 1 } + \frac { h } { 2 } \big ( f \big ( x _ { n } , y _ { n } ^ { * } \big ) + f \big ( x _ { n - 1 } , y _ { n - 1 } \big ) \big ) . } } \end{array}
$$

This is an example of a Runge–Kutta method.

As an example of the use of this method, refer to Table 221(I), where the Kepler problem (201d), with zero eccentricity, is integrated through a half period. The number of steps, $n$ , takes on successive values $2 ^ { i }$ , $i = 5 , 6 , \ldots , 1 0$ , so that $h$ takes on values $\pi 2 ^ { - i }$ , $i = 5 , 6 , \ldots , 1 0$ , respectively. The second order nature of the approximations is suggested by the rate at which errors decrease in each of the four components, as $n$ is repeatedly doubled.
