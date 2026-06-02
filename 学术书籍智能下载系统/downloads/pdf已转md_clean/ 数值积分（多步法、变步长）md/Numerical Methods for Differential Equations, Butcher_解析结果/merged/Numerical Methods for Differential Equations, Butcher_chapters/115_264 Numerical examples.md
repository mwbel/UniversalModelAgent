# 264 Numerical examples

The limited numerical testing performed here does not give a great deal of support to the use of pseudo Runge–Kutta or hybrid methods. Using the Kepler problem with eccentricity $\begin{array} { r } { e = \frac { 1 } { 2 } } \end{array}$ over a half period, the pseudo Runge– Kutta method (261a) was compared with the classical Runge–Kutta method and the results are summarized in Figure 264(i). To make the comparison as fair as possible, the axis denoted by $\overline { { h } }$ shows the stepsize per function evaluation. That is, for the Runge–Kutta method, $h = 4 \overline { { h } }$ , and for the pseudo Runge–Kutta method, $h \ : = \ : 3 \overline { { h } }$ . The classical Runge–Kutta is significantly more accurate for this problem.

A similar comparison has been made between the hybrid method discussed in Subsection 262 and a fifth order Runge–Kutta method, but the results, which are not presented here, show almost identical performance for the two methods.

# Exercises 26

26.1 Find the error computed in a single step using the method (261a) for the problem

$$
y ^ { \prime } ( x ) = x ^ { 4 }
$$

and show that this is 16 times the error for the classical Runge–Kutta method.

26.2 Find a fifth order method similar to the one discussed in Subsection   
262, but with first predictor giving an approximation to $\textstyle y ( x _ { n } - { \frac { 1 } { 2 } } h )$ .

26.3 Show how to represent the PEC method based on the second order Adams–Bashforth predictor and the third order Adams–Moulton corrector as a general linear method.

26.4 Show how to represent the PECEC method based on second order Adams–Bashforth and Adams–Moulton methods as a general linear method.
