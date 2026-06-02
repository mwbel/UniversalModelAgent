# 463 Local error estimation

The standard estimator for local truncation error is based on the Milne device. That is, the difference between the predicted and corrected values provides an approximation to some constant multiplied by $h ^ { p + 1 } y ^ { ( p + 1 ) } ( x _ { n } )$ , and the local truncation error can be estimated by multiplying this by a suitable scale factor.

This procedure has to be interpreted in a different way if, as in some modern codes, the predictor and corrector are accurate to different orders. We no longer have an asymptotically correct approximation to the local truncation error but to the error in the predictor, assuming this has the lower order. Nevertheless, stepsize control based on this approach often gives reliable and useful performance.

To allow for a possible increase in order, estimation is also needed for the scaled derivative one order higher than the standard error estimator. It is very difficult to do this reliably, because any approximation will be based on a linear combination of $h y ^ { \prime } ( x )$ for different $x$ arguments. These quantities in turn will be of the form $h f ( x , y ( x ) + C h ^ { p + 1 } + O ( h ^ { p + 2 } ) )$ , and the terms of the form $C h ^ { p + 1 } + O ( h ^ { p + 2 } )$ will distort the result obtained. However, it is possible to estimate the scaled order $p { + 2 }$ derivative reliably, at least if the stepsize has been constant over recent steps, by forming the difference of approximations to the order $p { + 1 }$ derivative over two successive steps. If the stepsize has varied moderately, the approximation this approximation will still be reasonable. In any case, if the criterion for increasing order turns out to be too optimistic for any specific problem, then after the first step with the new order a rejection is likely to occur, and the order will either be reduced again or else the stepsize will be lowered while still maintaining the higher order.

# Exercises 46

46.1 Show how to write $y ( x _ { n } + r h )$ in terms of $y ( x _ { n } )$ , $h y ^ { \prime } ( x _ { n } )$ and $h y ^ { \prime } ( x _ { n } - h )$ , to within $O ( h ^ { 3 } )$ . Show this approximation might be used to generalize the order 2 Adams–Bashforth method to variable stepsize.

46.2 How should the formulation of Subsection 461 be modified to represent Adams–Bashforth methods?
