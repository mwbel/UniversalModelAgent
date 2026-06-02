# 238 Stability characteristics

In Subsection 216, we discussed the stability of the Euler method when solving a linear problem of the form

$$
y ^ { \prime } ( x ) = q y ( x ) .
$$

If $z = h q$ , then in a single step of length $h$ , the exact solution will be multiplied by the factor $\exp ( z )$ . In the same time interval the approximate solution computed using a Runge–Kutta method will be multiplied by a function of $z$ , specific to the particular Runge–Kutta method. As in Subsection 216, we denote this ‘stability function’ by $R ( z )$ . The ‘stability region’, defined as $\{ z \in \mathbb { C } : | R ( z ) | \leq 1 \}$ , is the set of points in the complex plane such that the computed solution remains bounded after many steps of computation. There is special interest in values of $z$ in the left half-plane, because in this case the exact solution is bounded and good modelling of the problem would require the computed solution to behave in a similar manner.

For an $s$ -stage Runge–Kutta method, defined by the tableau

$$
\frac { c \mid A } { b ^ { \intercal } }
$$

the vector $Y$ , made up from the $s$ stage values, satisfies

$$
Y = \mathbf { 1 } y _ { 0 } + h A q Y = \mathbf { 1 } y _ { 0 } + z A Y ,
$$

where $y _ { 0 }$ is the incoming approximation. It follows that

$$
Y = ( I - z A ) ^ { - 1 } \mathbf { 1 } y _ { 0 } .
$$

Substitute this into the solution approximation found at the end of the step, and we find

$$
y _ { 1 } = y _ { 0 } + h b ^ { \intercal } q Y = y _ { 0 } + z b ^ { \intercal } ( I - z A ) ^ { - 1 } { \mathbf 1 } y _ { 0 } = R ( z ) y _ { 0 } ,
$$

where

$$
R ( z ) = 1 + z b ^ { \top } ( I - z A ) ^ { - 1 } \mathbf { 1 } .
$$

If (238a) represents an explicit Runge–Kutta method with order $p = s = 1 , 2 , 3$ or 4, then we can evaluate $R ( z )$ very simply as the exponential series truncated

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0002_pages_0071-0140/auto/images/18736941ee2bb85e725152cb0eaffe8d962a456eb25233ca806693eb885447ae.jpg)  
Stability regions for some explicit Runge–Kutta methods

at the $z ^ { s }$ term. To see why this should be the case, expand $( I - z A ) ^ { - 1 }$ by the geometric series and evaluate the terms using the order condition

$$
b ^ { \top } A ^ { k - 1 } \mathbf { 1 } = b ^ { \top } A ^ { k - 2 } c = { \frac { 1 } { k ! } } , \qquad k = 1 , 2 , \ldots , p .
$$

Hence, we have for the four cases for which $s = p$ is possible,

$$
R ( z ) = \left\{ \begin{array} { l l } { 1 + z , } & { p = 1 , } \\ { ] 1 + z + \frac { 1 } { 2 } z ^ { 2 } , } & { p = 2 , } \\ { 1 + z + \frac { 1 } { 2 } z ^ { 2 } + \frac { 1 } { 6 } z ^ { 3 } , } & { p = 3 , } \\ { 1 + z + \frac { 1 } { 2 } z ^ { 2 } + \frac { 1 } { 6 } z ^ { 3 } + \frac { 1 } { 2 4 } z ^ { 4 } , } & { p = 4 . } \end{array} \right.
$$

The boundaries of the stability regions defined by these functions are shown in Figure 238(i). In each case the stability region is the bounded set enclosed by these curves.

For explicit methods with $s = 6$ and $p = 5$ , the stability function takes the form

$$
\begin{array} { r } { R ( z ) = 1 + z + \frac { 1 } { 2 } z ^ { 2 } + \frac { 1 } { 6 } z ^ { 3 } + \frac { 1 } { 2 4 } z ^ { 4 } + \frac { 1 } { 1 2 0 } z ^ { 5 } + C z ^ { 6 } , } \end{array}
$$

where $C$ depends on the particular method. In the case of the method given by the tableau (236a), $\begin{array} { r } { C = \frac { 1 } { 1 2 8 0 } } \end{array}$ 11280 , and the stability region for this is also shown in Figure 238(i). In each case, the value of $p$ is attached to the curve.

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0002_pages_0071-0140/auto/images/5c68e9b1d738346ad122a7e308cc25c37692bda298eadd23b0fe70cad3e5df53.jpg)  
Stability regions for some implicit Runge–Kutta methods

It is never possible, even by the addition of extra stages, to devise explicit methods with order at least 1, which have unbounded stability regions, because $R ( z )$ is always a polynomial equal to $1 + z + O ( z ^ { 2 } )$ . However, as we saw in the case of the implicit Euler method, there is no such barrier for implicit Runge–Kutta methods.

For the three methods quoted in Subsection 237, the stability functions are found to be

$$
\begin{array} { r l r } & { } & { R ( z ) = \left\{ \begin{array} { l l } { \displaystyle 1 + \frac { 2 z } { 3 } + \frac { z ^ { 2 } } { 6 } , } & { \mathrm { m e t h o d ~ ( 2 3 7 a ) } , } \\ { \displaystyle 1 - \frac { z } { 3 } } & { \mathrm { m e t h o d ~ ( 2 3 7 a ) } , } \end{array} \right. } \\ & { } & { R ( z ) = \left\{ \begin{array} { l l } { \displaystyle 1 + ( \sqrt { 2 } - 1 ) z } & { \mathrm { m e t h o d ~ ( 2 3 7 b ) } , } \\ { \displaystyle \left( 1 - \left( 1 - \frac { 1 } { 2 } \sqrt { 2 } \right) z \right) ^ { 2 } , } & { \mathrm { m e t h o d ~ ( 2 3 7 b ) } , } \\ { \displaystyle \frac { 1 + \frac { z } { 2 } + \frac { z ^ { 2 } } { 1 2 } } { 1 - \frac { z ^ { 2 } } { 2 } + \frac { z ^ { 2 } } { 1 2 } } , } & { \mathrm { m e t h o d ~ ( 2 3 7 c ) } , } \end{array} \right. } \end{array}
$$

and the three stability regions are shown in Figure 238(ii). Note that for the fourth order method (237c), the stability region is exactly the closed left half-plane. The method (237a) shares the property of explicit Runge– Kutta methods of having a bounded stability region, whereas (237b) has an unbounded stability region which includes the left half-plane.

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0002_pages_0071-0140/auto/images/66dcd513a0cb28090850e59777de8eb64e9ca4d378f756739cf94f8a54478101.jpg)  
Orbital calculations for various Runge–Kutta methods
