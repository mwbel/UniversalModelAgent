# 202 Calculations with stepsize control

The use of the Euler method, with constant stepsize, may not be efficient for some problems. For example, in the case of the eccentric orbits, discussed in the previous subsection, a small step should be taken for points on the orbit, close to the attracting force, and a larger step for points remote from the attracting force. In deciding how we might attempt to control the stepsize for a general problem, we need to consider how the error committed in each step can be estimated. First, however, we consider how the stepsize in a step should be chosen, to take account of this error estimate.

Because the total error is approximately the sum of the errors committed in the individual steps, at least for a limited number of steps, we look at a simple model in which the interval of integration is divided up into $m$ subintervals, with lengths ${ \delta _ { 1 } , \delta _ { 2 } , \dots , \delta _ { m } }$ . We assume that the norms of the errors in steps carried out in these intervals are $C _ { 1 } h _ { 1 } ^ { 2 } , C _ { 2 } h _ { 2 } ^ { 2 } , \ldots , C _ { m } h _ { m } ^ { 2 }$ , respectively, where $h _ { 1 } , h _ { 2 } , \ldots , h _ { m }$ are the constant stepsizes in these subintervals. Assume that a total of $N$ steps of integration by the Euler method are carried out and that a fraction $t _ { i }$ of these are performed in subinterval $i = 1 , 2 , \dots , m$ . This means that $t _ { i } N$ steps are carried out in subinterval $i$ and that $h _ { i } = \delta _ { i } / t _ { i } N$ . The total error committed, which we assume, in the absence of further information, to be the sum of the individual errors, is approximately

$$
E = \sum _ { i = 1 } ^ { m } ( t _ { i } N ) C _ { i } \left( \frac { \delta _ { i } } { t _ { i } N } \right) ^ { 2 } = \frac { 1 } { N } \sum _ { i = 1 } ^ { m } \delta _ { i } ^ { 2 } C _ { i } t _ { i } ^ { - 1 } ,
$$

where $\delta _ { i } / t _ { i } N$ is the stepsize used for every step in subinterval number $i$ . By the Cauchy–Schwarz inequality, the minimum value of (202a) is achieved by

$$
t _ { i } = \frac { \delta _ { i } \sqrt { C _ { i } } } { \sum _ { j = 1 } ^ { m } \delta _ { j } \sqrt { C _ { j } } }
$$

and it follows that optimality occurs when $C _ { i } h _ { i } ^ { 2 }$ is maintained constant over every subinterval. We interpret this result to mean that the estimated values of the error should be kept as close as possible to some pre-assigned value.

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0002_pages_0071-0140/auto/images/e91c8200d4af0f1ff8adae2902d909284f67d0b2726bbc386215fd366a6bea55.jpg)  
Constant (◦) and variable (•) step for orbit with eccentricities $\begin{array} { r } { e = \frac { 1 } { 2 } } \end{array}$ $( - \cdot - )$ and $\textstyle e = { \frac { 3 } { 4 } }$ (· · · )

This pre-assigned value, which is under control of the user, will be regarded as the user-imposed tolerance.

To actually estimate the error committed in each step, we have a natural resource at our disposal; this is the availability of approximations to $h y ^ { \prime } ( x )$ at the beginning and end of every step. At the beginning of step $n$ , it is, of course, the value of $h f ( x _ { n - 1 } , y _ { n - 1 } )$ used in the computation of the Euler step itself. At the end of this step we can calculate $h f ( x _ { n } , y _ { n } )$ . This might seem to be an additional calculation of the function $f$ , but this computation needs to be done anyway, since it is needed when the following step is eventually carried out. From these approximations to $h y ^ { \prime } ( x _ { n - 1 } )$ and $h y ^ { \prime } ( x _ { n } )$ we can recalculate the step from $y _ { n - 1 }$ using the more accurate trapezoidal rule to yield the improved approximation to $y ( x _ { n } )$ , given by

$$
y ( x _ { n } ) \approx y ( x _ { n - 1 } ) + { \frac { 1 } { 2 } } { \big ( } h y ^ { \prime } ( x _ { n - 1 } ) + h y ^ { \prime } ( x _ { n } ) { \big ) } ,
$$

and we can use the difference between this approximation to $y ( x _ { n } )$ , and the result computed by the Euler step, as our local error estimate.

Hence we have, as an estimate of the norm of the error,

$$
\frac 1 2 \| h f ( x _ { n - 1 } , y ( x _ { n - 1 } ) ) - h f ( x _ { n } , y ( x _ { n } ) ) \| .
$$

As an illustration of how variable stepsize works in practice, the calculations of gravitational orbits with eccentricities 0.5 and 0.75 have been repeated using variable stepsize, but with the tolerances set at values that will give a total number of steps approximately the same as for the constant stepsize cases already investigated. A summary of the results is shown in Figure 202(i). To make the comparisons straightforward, only norms of errors are plotted against stepsize (or mean stepsize in the variable stepsize cases).

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0002_pages_0071-0140/auto/images/cb7e396e6d14461e335427110fe36a8bdc1059bd4be610ee21829d26ce48a5a8.jpg)  
Norm error against $n ^ { - 1 }$ for the ‘mildly stiff’ problem (203a)

203 Calculations with mildly stiff problems

Consider the initial value problem

$$
\begin{array} { l l l } { \displaystyle \frac { d y _ { 1 } } { d x } = - 1 6 y _ { 1 } + 1 2 y _ { 2 } + 1 6 \cos ( x ) - 1 3 \sin ( x ) , } & { y _ { 1 } ( 0 ) = 1 , } \\ { \displaystyle \frac { d y _ { 2 } } { d x } = 1 2 y _ { 1 } - 9 y _ { 2 } - 1 1 \cos ( x ) + 9 \sin ( x ) , } & { y _ { 2 } ( 0 ) = 0 , } \end{array}
$$

for which the exact solution is $y _ { 1 } ( x ) = \cos ( x )$ , $y _ { 2 } ( x ) = \sin ( x )$ . We attempt to solve this problem using the Euler method. First, we use constant stepsize. Specifically, we perform $n$ steps with $h = \pi / n$ and with $n$ taking on various integer values. This yields a sequence of approximations to $y ( \pi )$ , and results for the norm of the error are given in Figure 203(i).

The results shown here have a disturbing feature. Even though the asymptotic first order behaviour is clearly seen, this effect is recognizable only below a certain threshold, corresponding to $n = 3 8$ . For $h$ above the corresponding value of $\pi / 3 8$ , the errors grow sharply, until they dominate the solution itself. We consider what can be done to avoid this extreme behaviour and we turn to variable stepsize as a possible remedy. We need to be more precise than in Subsection 202, in deciding how we should apply this approach. After a step has been completed, we have to either accept or reject the step, and rejecting requires us to repeat the step, but with a scaled-down stepsize. In either case we need a policy for deciding on a stepsize to use in the new attempt at the failed step, or to use in the succeeding new step.

Because the local truncation error is asymptotically proportional to the square of $h$ , it makes sense to scale the stepsize in the ratio $\sqrt { T / \| E \| }$ , where $E$ is the error estimate and $T$ is the maximum permitted value of $\| E \|$ . However, it is essential to insert a ‘safety factor’ $S$ , less than $^ { 1 }$ , into the computation, to guard against a rejection in a new step, because of slight variations in the magnitude of the error estimate from step to step. It is also wise to use two further design parameters, $M$ and $m$ , representing the maximum and minimum stepsize ratios that will be permitted. Typically $M \ = \ 2$ , $m = \textstyle { \frac { 1 } { 2 } }$ and $S = 0 . 9$ , and we adopt these values. Fortunately, this experiment of using variable stepsize is successful, as is seen from Figure 203(ii).

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0002_pages_0071-0140/auto/images/fb9432b310ee636ef36e76450bcbb193c0afa071c2ab8b8bc782a7c64dfa4bcf.jpg)  
Norm error against tolerance $T$ for the ‘mildly stiff’ problem (203a) with variable stepsize

There is a loss of efficiency, in that unstable behaviour typically results in wide variations of stepsize, in sequences of adjacent steps. However, there are relatively few steps rejected, because of excessive error estimates. For the special choice of the tolerance $T = 0 . 0 2$ , 38 successful steps were taken, in addition to 11 failed steps. The value of the stepsize $h$ as a function of the value of $x$ , at the beginning of each of the steps, is shown in Figure 203(iii).

The phenomenon experienced with this example goes under the name of ‘stiffness’. To understand why this problem is stiff, and why there seems to be a value of $h$ such that, for values of the stepsize above this, it cannot be solved by the Euler method, write $v _ { 1 } ( x )$ and $v _ { 2 } ( x )$ for the deviations of $y _ { 1 } ( x )$ and $y _ { 2 } ( x )$ from the exact solution. That is, $y _ { 1 } ( x ) = \cos ( x ) + v _ { 1 } ( x )$ and $y _ { 2 } ( x ) = \sin ( x ) + v _ { 2 } ( x )$ . Because the system is linear, it reduces in a simple way to

$$
\left[ \begin{array} { r } { \frac { d v _ { 1 } } { d x } } \\ { \frac { d v _ { 2 } } { d x } } \end{array} \right] = \left[ \begin{array} { r r } { - 1 6 } & { 1 2 } \\ { 1 2 } & { - 9 } \end{array} \right] \left[ \begin{array} { r } { v _ { 1 } } \\ { v _ { 2 } } \end{array} \right] .
$$

To simplify the discussion further, find the eigenvalues, and corresponding eigenvectors, of the matrix $A$ occurring in (203b), where

$$
A = \left[ \begin{array} { r r } { { - 1 6 } } & { { 1 2 } } \\ { { 1 2 } } & { { - 9 } } \end{array} \right] .
$$

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0002_pages_0071-0140/auto/images/e5ec87d24fe6f6a58f63268602770b722684a1ae4cbdbad83f361e189ae8e4fa.jpg)  
Stepsize $h$ against $_ { x }$ for the ‘mildly stiff’ problem (203a) with variable stepsize for $T = 0 . 0 2$

The eigenvalues of $A$ are $\lambda _ { 1 } = 0$ and $\lambda _ { 2 } = - 2 5$ and the eigenvectors are the columns of the matrix

$$
T = \left[ \begin{array} { r r } { { 3 } } & { { 4 } } \\ { { 4 } } & { { - 3 } } \end{array} \right] .
$$

By substituting $v = T w$ , that is,

$$
\left[ \begin{array} { l } { v _ { 1 } } \\ { v _ { 2 } } \end{array} \right] = \left[ \begin{array} { l l } { 3 } & { 4 } \\ { 4 } & { - 3 } \end{array} \right] \left[ \begin{array} { l } { w _ { 1 } } \\ { w _ { 2 } } \end{array} \right] ,
$$

we find that

$$
\left[ \begin{array} { r } { \left[ \frac { d w _ { 1 } } { d x } \right] } \\ { \frac { d w _ { 2 } } { d x } } \end{array} \right] = \left[ \begin{array} { r r } { 0 } & { 0 } \\ { 0 } & { - 2 5 } \end{array} \right] \left[ \begin{array} { r } { w _ { 1 } } \\ { w _ { 2 } } \end{array} \right] .
$$

The components of $w$ each have bounded solutions, and thus the original differential equation is stable. In particular, any perturbation in $w _ { 2 }$ will lead to very little change in the long term solution, because of the quickly decaying exponential behaviour of this component. On the other hand, when the equation for $w _ { 2 }$ is solved numerically, difficulties arise. In a single step of size $h$ , the exact solution for $w _ { 2 }$ should be multiplied by $\exp ( - 2 5 h )$ , but the numerical approximation is multiplied by $1 - 2 5 h$ . Even though $| \exp ( - 2 5 h ) |$ is always less than 1 for positive $h$ , $| 1 - 2 5 h |$ is greater than 1, so that its powers form an unbounded sequence, unless $h \leq \frac { 2 } { 2 5 }$ .

This, then, is the characteristic property of stiffness: components of the solution that should be stable become unstable when subjected to numerical approximations in methods like the Euler method.

Comparison of explicit and implicit Euler methods: problem (201a)   

<table><tr><td>n</td><td>Explicit error</td><td>Implicit error</td><td>Iterations</td></tr><tr><td>5</td><td>0.03719000</td><td>-0.03396724</td><td>28</td></tr><tr><td>10</td><td>0.01817489</td><td>-0.01737078</td><td>47</td></tr><tr><td>20</td><td>0.00898483</td><td>-0.00878393</td><td>80</td></tr><tr><td>40</td><td>0.00446704</td><td>-0.00441680</td><td>149</td></tr><tr><td>80</td><td>0.00222721</td><td>-0.00221462</td><td>240</td></tr><tr><td>160</td><td>0.00111203</td><td>-0.00110889</td><td>480</td></tr><tr><td>320</td><td>0.00055562</td><td>-0.00055484</td><td>960</td></tr><tr><td>640</td><td>0.00027771</td><td>-0.00027762</td><td>1621</td></tr></table>
