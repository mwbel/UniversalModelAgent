# 330 Introduction

Practical computations with Runge–Kutta methods usually require a means of local error estimation. This is because stepsizes are easy to adjust so as to follow the behaviour of the solution, but the optimal sequence of stepsizes depends on the local truncation error. Of course, the exact truncation error cannot realistically be found, but asymptotically correct approximations to it can be computed as the integration proceeds. One way of looking at this is that two separate approximations to the solution at a step value $x _ { n }$ are found. Assuming that the solution value at the previous point is regarded as exact, because it is the local error that is being approximated, denote the two solutions found at the current point by $y _ { n }$ and ${ \hat { y } } _ { n }$ . Suppose the two approximations have orders $p$ and $q$ , respectively, so that

$$
y _ { n } = y ( x _ { n } ) + O ( h ^ { p + 1 } ) , \qquad { \widehat { y } } _ { n } = y ( x _ { n } ) + O ( h ^ { q + 1 } ) .
$$

Then, if $q > p$

$$
{ \widehat { y } } _ { n } - y _ { n } = y ( x _ { n } ) - y _ { n } + O ( h ^ { p + 2 } ) ,
$$

which can be used as an approximation to the error committed in the step. Furthermore, the approximation becomes increasingly accurate as $h$ becomes small. Thus ${ \widehat { y } } _ { n } - y _ { n }$ is used as the error estimator.

Even though we emphasize the construction of method pairs for which $q = p + 1$ , and for which it is $y _ { n }$ (rather than the asymptotically more accurate approximation ${ \widehat { y } } _ { n }$ ) that is propagated as the numerical approximation at $x _ { n }$ , customary practice is to use the higher order as the propagated value. This is sometimes interpreted as ‘local extrapolation’, in the sense that the error estimate is added to the approximate solution as a correction. While the estimator is still used as a stepsize controller, it is now no longer related asymptotically to the local truncation error.

We review the ‘deferred approach to the limit’ of Richardson (1927) and then consider specially constructed Runge–Kutta tableaux, which combine two methods, with orders one apart, built into one. The classical method of this type is due to Merson (1957), but we also consider built-in estimators due to Fehlberg (1968, 1969), Verner (1978) and Dormand and Prince (1980). Some of the methods derived for the author’s previous book (Butcher, 1987) will also be recalled.
