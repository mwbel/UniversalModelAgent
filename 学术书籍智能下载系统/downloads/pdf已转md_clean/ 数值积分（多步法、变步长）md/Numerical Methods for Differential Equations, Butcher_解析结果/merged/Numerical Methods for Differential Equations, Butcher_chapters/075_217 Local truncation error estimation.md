# 217 Local truncation error estimation

We recall from Subsection 202 that stepsize control based on a local error estimate was useful in forcing the Euler method to devote computational effort to those parts of the trajectory where it is most needed. We discuss here the principles behind this idea.

Let $y _ { 1 }$ , $y _ { 2 }$ , . . . , $y _ { n - 1 }$ , $y _ { n }$ , . . . denote a sequence of approximations to the solution to an initial value problem, computed using the Euler method. For our present purposes, we can assume that the stepsize takes a constant value $h$ , since we are discussing the estimation of the local truncation error only over a single interval. Because we are considering the local error, we treat the incoming approximation for step $n$ as though it were exact. That is, we introduce a solution $\hat { y }$ to the initial value problem

$$
\widehat { y } ^ { \prime } ( x ) = f ( x , \widehat { y } ( x ) ) , \qquad \widehat { y } ( x _ { n - 1 } ) = y _ { n - 1 } .
$$

We can then interpret ${ \widehat { y } } ( x _ { n } ) - y _ { n }$ as the error introduced in step $n$ alone.

Although it is not feasible to obtain convenient and useful bounds on this quantity, it is possible to obtain asymptotically correct approximations without additional cost. These will often be useful for the purpose of controlling the stepsize, to produce efficient numerical algorithms, although they cannot be used to obtain rigorous error bounds.

An approximation for ${ \widehat { y } } ( x _ { n } )$ , to within $O ( h ^ { 3 } )$ , is found using a truncated Taylor series

$$
\widehat { y } ( x _ { n - 1 } + h ) \approx \widehat { y } ( x _ { n - 1 } ) + h \widehat { y } ^ { \prime } ( x _ { n - 1 } ) + \frac { h ^ { 2 } } { 2 ! } \widehat { y } ^ { \prime \prime } ( x _ { n - 1 } ) ,
$$

and the first two terms are

$$
{ \widehat { y } } ( x _ { n - 1 } ) + h { \widehat { y } } ^ { \prime } ( x _ { n - 1 } ) = y _ { n - 1 } + h f ( x _ { n - 1 } , y _ { n - 1 } ) = y _ { n } .
$$

Hence, we see that the truncation error is approximately

$$
\frac { h ^ { 2 } } { 2 ! } \widehat { y } ^ { \prime \prime } ( x _ { n - 1 } ) .
$$

An alternative interpretation of this quantity, at least asymptotically, with terms involving third and higher powers of $h$ ignored, is as the difference

between the result computed by the Euler method and a result computed, at least for the current step, using a method which has a higher order.

As we will see in Section 22, there are many ways in which such a higher order method can be found. One method is to evaluate $h f ( x _ { n } , y _ { n } )$ , and to recompute the step as

$$
y _ { n - 1 } + { \frac { 1 } { 2 } } { \Big ( } h f ( x _ { n } , y _ { n } ) + h f ( x _ { n - 1 } , y _ { n - 1 } ) { \Big ) } .
$$

If we were intending to actually use this more accurate approximation, then the second computation of the function $f$ in each step would approximately double the work that needs to be done to complete each step. However, all we intend to do is to estimate the error and, for this reason, the cost is unchanged, because we need the value of $h f ( x _ { n } , y _ { n } )$ to proceed to the next step in any case.

Thus, we see that a convenient, and essentially cost-free, method for estimating local truncation errors is as the difference of the result found by the Euler method itself, and the result found from (217a). This leads to the error estimate

$$
{ \frac { 1 } { 2 } } { \Big ( } h f ( x _ { n } , y _ { n } ) - h f ( x _ { n - 1 } , y _ { n - 1 } ) { \Big ) } .
$$

We already know this estimate can be used, quite satisfactorily, to control stepsize, because of its evident success in Subsection 202.
