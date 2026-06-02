# 231 Second order methods

In Subsection 221, a method was introduced based on the trapezoidal rule quadrature formula. It turns out that for any non-zero choice of a parameter $\theta$ , it is possible to construct a method with two stages and this same order. All that is required is a first partial step to form an approximation a distance $\theta h$ into the step. Using the derivative at this point, together with the derivative at the beginning of the step, the solution at the end of the step is then found using the second order quadrature formula

$$
\int _ { 0 } ^ { 1 } \phi ( x ) d x \approx \left( 1 - \frac { 1 } { 2 \theta } \right) \phi ( 0 ) + \frac { 1 } { 2 \theta } \phi ( \theta ) .
$$

Thus, to advance the solution from $x _ { n - 1 }$ to $x _ { n } = x _ { n - 1 } + h$ , the result is found from

$$
\begin{array} { l } { { Y = y _ { n - 1 } + \theta h f ( x _ { n - 1 } , y _ { n - 1 } ) , } } \\ { { \displaystyle y _ { n } = y _ { n - 1 } + \left( 1 - \frac { 1 } { 2 \theta } \right) h f ( x _ { n - 1 } , y _ { n - 1 } ) + \frac { 1 } { 2 \theta } h f ( x _ { n - 1 } + \theta h , Y ) . } } \end{array}
$$

Note that the intermediate stage value $Y$ is an approximation to the solution at the ‘off-step’ point $x _ { n - 1 } + \theta h$ , and is equal to $y _ { n } ^ { * }$ , in the special case we have already considered, given by (221a) and (221b), in which $\theta = 1$ . The other most commonly used value is $\begin{array} { r } { \theta = \frac { 1 } { 2 } } \end{array}$ , as in the ‘mid-point rule’.
