# 274 Experiments with a discontinuous problem

The stepsize control mechanism, coded into Algorithm $2 7 1 \alpha$ , contains upper and lower bounds on the stepsize ratios. The choice of these bounds acquires crucial importance when low order discontinuities arise in the solution. When a step straddles a point at which there is a sudden change in one of the low order derivatives, this will be recognized by the solver as a massive error estimate, unless the stepsize is abnormally short. Consider, for example, the two-dimensional problem

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0003_pages_0141-0210/auto/images/981ce10db140f26c18dfa65271bcb20a8d0328e89cfe766ec637b5a0664d3732.jpg)  
Errors and number of rejections for (274a)

$$
\begin{array} { r } { y ^ { \prime } ( x ) = \left\{ \begin{array} { l l } { \left[ \begin{array} { l } { 0 } \\ { 1 } \end{array} \right] , } & { y _ { 1 } > y _ { 2 } , } \\ { \left[ \begin{array} { l } { - 1 } \\ { 0 } \end{array} \right] , } & { y ( 0 ) = \left[ \begin{array} { l } { 1 } \\ { \pi / 6 } \end{array} \right] . } \end{array} \right. } \end{array}
$$

The solution to this problem is very simple: $y ( x ) = [ 1 , x + \pi / 6 ] ^ { 1 }$ for $x < 1 - \pi / 6$ and $y ( x ) = [ 2 - \pi / 6 - x , 1 ] ^ { \mathfrak { l } }$ for $x > 1 - \pi / 6$ . Because we are interested in how well the method deals with discontinuous behaviour, we will not take into account our knowledge of where this point is located. What should we expect to happen? We would expect the first step, which jumps over $x = 1 - \pi / 6$ , to fail and for the stepsize to be reduced as much as the stepsize controller permits. There will then be a sequence of successes (followed by step increases), or failures (followed by step decreases). This sequence will terminate only when the stepsize is small enough for the quantity used as the error estimate to be less than $T$ . Numerical results for this problem using Algorithm $2 7 1 \alpha$ are presented in Figure $2 7 4 ( \mathrm { i } )$ .

These show the dependence on the accuracy achieved, measured in terms of the error in the component of $y _ { 2 }$ after the trajectory has turned the corner at $y = [ 1 , 1 ] ^ { \scriptscriptstyle 1 }$ , together with the number of steps rejected in the whole process of locating the discontinuity in $y ^ { \prime }$ and getting past it.

The results will be sensitive to the initial stepsize and, to guarantee we have represented typical and representative behaviour, a large number of initial stepsizes were used with each tolerance. For both the error calculations and the rejected step totals, the results indicate mean values over this range of initial $h$ with shading showing the mean values plus or minus the standard deviation and plus or minus twice the standard deviations. The results suggest that, for this and similar problems, we should expect the error to have a similar magnitude to the tolerance and the number of rejections to be proportional to the logarithm of the tolerance.

# Exercises 27

27.1 By computing the scaled derivative of the output from the classical fourth order Runge–Kutta method RK41 (235i), within the current step, rather than from the first stage of the following step, show that the method becomes the general linear method

$$
\begin{array}{c} [ { \begin{array} { l l l l } { 0 } & { 0 } & { 0 } & { 0 } \\ { { \frac { 1 } { 2 } } } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } & { 0 } \\ { { \frac { 1 } { 3 } } } & { { \frac { 1 } { 3 } } } & { { \frac { 1 } { 6 } } } & { 0 } \end{array} } ] { \mathrm { ~ 1 ~ } } { \mathrm { ~ \frac { 1 } { 2 } ~ } }  \\ { { [ { \begin{array} { l l l l l } { { \frac { 1 } { 3 } } } & { { \frac { 1 } { 3 } } } & { { \frac { 1 } { 6 } } } & { 0 } & { { | { \begin{array} { l l } { 1 } & { { \frac { 1 } { 6 } } } \\ { 0 } & { 0 } & { 0 } & { 1 } \end{array} } | } } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 1 } \end{array} } ] } } \end{array} ] ~ .
$$

27.2 Write a fourth order method, with stepsize control, based on the method in Exercise 27.1 which is equivalent to two steps of RK41, each with stepsize $h$ , combined with a single step from the same input, with stepsize $2 h$ . Use the difference between the two-step result and the double-step result as an error estimator.

27.3 Denote the starting point in Exercise 27.2 as $x _ { - 1 }$ so that the results are computed at $x _ { 0 } = x _ { - 1 } + h$ and $x _ { 1 } = x _ { 0 } + h$ . Find a suitable interpolator for this method based on approximations to $y ( x _ { - 1 } )$ , $h y ^ { \prime } ( x _ { - 1 } )$ , $y ( x _ { 0 } )$ , $y ( x _ { 1 } )$ , $h y ^ { \prime } ( x _ { 1 } )$ to yield an approximation to $y ( x _ { 0 } + h t )$ , for $t \in [ - 1 , 1 ]$ . Add this interpolator to the variable step method discussed in Exercise 27.2.
