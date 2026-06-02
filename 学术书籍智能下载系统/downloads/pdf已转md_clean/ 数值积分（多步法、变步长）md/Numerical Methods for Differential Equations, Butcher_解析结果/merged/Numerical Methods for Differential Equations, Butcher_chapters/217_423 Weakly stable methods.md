# 423 Weakly stable methods

The stability requirement for linear multistep methods specifies that all zeros of the polynomial $\rho$ should lie in the closed unit disc with only simple zeros on the boundary. There is always a zero at 1, because of consistency, and there may or may not be other zeros on the boundary. We show in Subsection 441 that for a $k$ -step method, with $k$ even, the maximum possible order is $k + 2$ . For methods with this maximal order, it turns out that all zeros of $\rho$ lie on the unit circle and we are forced to take these methods seriously. We will write methods in the $[ \alpha , \beta ]$ terminology. A classic example is

$$
\begin{array} { l } { \alpha ( z ) = 1 - z ^ { 2 } , } \\ { \beta ( z ) = 2 z } \end{array}
$$

and this is known as the ‘leapfrog method’. Methods based on Newton–Cotes formulae were promoted by Milne (1953), and these all fall into this family.

The presence of additional zeros (that is, in addition to the single zero required by consistency) on the unit circle leads to the phenomenon known as ‘weak stability’.

A characteristic property of weakly stable methods is their difficulty in dealing with the long term integration of dissipative problems. For example, if an approximation to the solution of $y ^ { \prime } = - y$ is attempted using (423a), the difference equation for the computed results is

$$
y _ { n } + 2 h y _ { n - 1 } - y _ { n - 2 } = 0 .
$$

The general solution to (423c) is

$$
y _ { n } = A \lambda ^ { n } + B \mu ^ { n } ,
$$

where

$$
\begin{array} { l r } { \lambda ~ = ~ - h + \sqrt { 1 + h ^ { 2 } } ~ \approx ~ 1 - h + \frac { 1 } { 2 } h ^ { 2 } ~ \approx ~ \exp ( - h ) , } \\ { \mu ~ = ~ - h - \sqrt { 1 + h ^ { 2 } } ~ \approx ~ - 1 - h - \frac { 1 } { 2 } h ^ { 2 } ~ \approx ~ - \exp ( h ) , } \end{array}
$$

where $A$ and $B$ depend on initial values. Substitute the approximate values of $\lambda$ and $\mu$ into (423d) and we find

$$
y _ { n } \approx A \exp ( - n h ) + B ( - 1 ) ^ { n } \exp ( n h ) .
$$

For high values of $n$ , the second term, which represents a parasitic solution, eventually dominates the solution and produces a very poor approximation. This is in contrast to what happens for the differential equation $y ^ { \prime } = y$ , for which the solution to the corresponding difference equation takes the form $y _ { n } \approx A \exp ( n h ) + B ( - 1 ) ^ { n } \exp ( - n h )$ . In this case, the first term again corresponds to the true solution, but the second term will always be less significant.
