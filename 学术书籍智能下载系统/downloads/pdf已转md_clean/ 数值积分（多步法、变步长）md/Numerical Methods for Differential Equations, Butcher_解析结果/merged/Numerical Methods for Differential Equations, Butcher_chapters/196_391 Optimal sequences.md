# 391 Optimal sequences

Consider an integration over an interval $[ a , b ]$ . We can interpret $a$ as the point $x _ { 0 }$ at which initial information $y ( x _ { 0 } ) = y _ { 0 }$ is given and $b$ as a final point, which we have generally written as $\overline { { x } }$ where we are attempting to approximate $y ( { \overline { { x } } } )$ . As steps of a Runge–Kutta method are carried out we need to choose $h$ for a new step starting at a point $x \in [ a , b ]$ , assuming previous steps have taken the solution forward to this point. From information gleaned from details of the computation, it will be possible to obtain some sort of guide as to what the truncation error is likely to do in a step from $x$ to $x + h$ and, assuming that the method has order $p$ , the norm of this truncation error will be approximately like $C ( \boldsymbol { x } ) h ^ { p + 1 }$ , where $C$ is some positively valued function. Write the choice of $h$ for this step as $H ( x )$ . Assuming that all stepsizes are sufficiently small, we can write the overall error approximately as an integral

$$
E ( H ) = \int _ { a } ^ { b } C ( x ) H ( x ) ^ { p } d x .
$$

The total work carried out will be taken to be the simply the number of steps. For classical Runge–Kutta methods the cost of carrying out each step will be approximately the same from step to step. However, the number of steps is approximately equal to the integral

$$
W ( H ) = \int _ { a } ^ { b } H ( x ) ^ { - 1 } d x .
$$

To obtain an optimal rule for defining values of $H ( x )$ , as $x$ varies, we have to ensure that it is not possible, by altering $H$ , to obtain, at the same time, lower values of both $E ( H )$ and $W ( H )$ . This means that the optimal choice is the same as would be obtained by minimizing $E ( H )$ , for a specified upper bound on $W ( H )$ , or, dually, minimizing $W ( H )$ , subject to an upper bound on $E ( H )$ . Thus we need to optimize the value of $E ( H ) + T W ( H )$ for some positive value of the Lagrange multiplier $T$ .

From calculus of variation arguments, the optimal is achieved by setting to zero the expression $( d / d H ) ( E ( H ) + T W ( H ) )$ . Assuming that $W ( H )$ has the constant value $p$ , chosen for convenience, this means that

$$
p C ( x ) H ( x ) ^ { p - 1 } = p T H ( x ) ^ { - 2 } ,
$$

for all $x$ . Hence, $C ( x ) H ( x ) ^ { p + 1 }$ should be kept equal to the constant value $T$ . In other words, optimality is achieved by keeping the magnitude of the local truncation error close to constant from step to step. In practice, the truncation error associated with a step about to be carried out is not known. However, an estimation of the error in the last completed step is usually available, using techniques such as those described in Section 33, and this can be taken as a usable guide. On the other hand, if a previous attempt to carry out this step has been rejected, because the truncation error was regarded as excessive, then this gives information about the correct value of $h$ to use in a second attempt.

For robustness, a stepsize controller has to respond as smoothly as possible to (real or apparent) abrupt changes in behaviour. This means that the stepsize should not decrease or increase from one step to the next by an excessive ratio. Also, if the user-specified tolerance, given as a bound on the norm of the local truncation error estimate, is ever exceeded, recomputation and loss of performance will result. Hence, to guard against this as much as possible, a ‘safety factor’ is usually introduced into the computation. If $h$ is the estimated stepsize to give a predicted truncation error equal to the tolerance, then some smaller value, such as $0 . 9 h$ , is typically used instead. Combining all these ideas, we can give a formula for arriving at a factor $r$ , to give a new stepsize $r h$ , following a step for which the error estimate is est. The tolerance is written as tol, and it is assumed that this previous step has been accepted. The ratio $r$ is given by

$$
r = \operatorname* { m a x } { \left( 0 . 5 , \operatorname* { m i n } { \left( 2 . 0 , 0 . 9 { \left( \frac { \mathrm { t o l } } { \mathrm { e s t } } \right) } ^ { 1 / ( p + 1 ) } \right) } \right) } .
$$

The three constants, given here with values 0.5, 2.0 and 0.9, are all somewhat arbitrary and have to be regarded as design parameters.
