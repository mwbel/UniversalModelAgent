# 255 Further numerical examples

We consider the solution of the same problem discussed in Subsection 252, but using the methods of Subsection 253. The two methods discussed there, for various values of $m$ , implying orders $2 m$ , attached to the curves, are used together in predictor–corrector mode in Figure 255(i). A comparison with Figure 252(i) shows the new methods to be slightly more accurate for the same stepsizes.

The final numerical result in this subsection is based on the mildly stiff problem (203a), written in the form

$$
\begin{array} { l l l } { \displaystyle { \frac { d y _ { 1 } } { d x } = - 1 6 y _ { 1 } + 1 2 y _ { 2 } + 1 6 \cos ( y _ { 3 } ) - 1 3 \sin ( y _ { 3 } ) , \quad } } & { \mathrm { ~ } y _ { 1 } ( 0 ) = 1 , } \\ { \displaystyle { \frac { d y _ { 2 } } { d x } = 1 2 y _ { 1 } - 9 y _ { 2 } - 1 1 \cos ( y _ { 3 } ) + 9 \sin ( y _ { 3 } ) , \quad } } & { \mathrm { ~ } y _ { 2 } ( 0 ) = 0 , } \\ { \displaystyle { \frac { d y _ { 3 } } { d x } = 1 , \quad } } & { \mathrm { ~ } y _ { 3 } ( 0 ) = 0 . } \end{array}
$$

The norm errors for the approximate solution at $x = \pi$ are given for various $h$ in Figure 255(ii).

# Exercises 25

25.1 Consider the function $f ( x , y ) = x ^ { 2 } + y ^ { 2 }$ and the differential equation $y ^ { \prime } ( x ) \ = \ f ( x , y ( x ) )$ . Derive formulae for the second, third and fourth derivatives.

25.2 Solve the initial value problem $y ^ { \prime } ( x ) = x ^ { 2 } + y ( x ) ^ { 2 }$ , $y ( 0 ) = 1$ by the fourth order Taylor series method using $n$ steps with constant stepsize $h = 1 / n$ to yield approximations to the solution at $x = 1$ . Use $n = 1 , 2 , 4 , \dots , 2 ^ { \mathrm { 1 0 } }$ . Are the results consistent with the order 4 nature of the method?

25.3 Use the eighth order predictor–corrector method discussed in Subsection 253 to solve this problem.

25.4 Show that the Rosenbrock method given by (254a), (254b) and (254c) has order 2.
