# 547 ARK methods for stiff problems

In Butcher and Rattenbury (2005), the ARK type of method was extended to the solution of stiff problems. Methods were presented with orders 3 and 4, subject to a number of criteria, and these were supported by preliminary numerical comparisons with standard methods. Because stiff ARK methods are still at an early stage of development, we will not attempt to give a full description, but will present a single third order method,

$$
{ \left[ \begin{array} { l l } { A } & { U } \\ { B } & { V } \end{array} \right] } = \left[ { \begin{array} { c c c c c c } { { \frac { 1 } { 3 } } } & { 0 } & { 0 } & { 0 } & { { \frac { 1 } { 3 } } } & { { \frac { 2 } { 6 } } } \\ { - { \frac { 1 } { 1 6 } } } & { { \frac { 1 } { 3 } } } & { 0 } & { { \frac { 1 } { 4 8 } } } & { { \frac { 1 } { 4 8 } } } \\ { - { \frac { 1 } { 6 } } } & { { \frac { 2 } { 3 } } } & { { \frac { 1 } { 3 } } } & { { \frac { 1 } { 6 } } } & { { 0 } } \\ { - { \frac { 1 } { 6 } } } & { { \frac { 2 } { 3 } } } & { { \frac { 1 } { 3 } } } & { { \frac { 1 } { 6 } } } & { { 0 } } \\ { 0 } & { 0 } & { 1 } & { 0 } & { 0 } \\ { { \frac { 1 } { 3 } } } & { - { \frac { 8 } { 3 } } } & { 2 } & { { \frac { 1 } { 3 } } } & { 0 } \end{array} } \right] ,
$$

together with a convenient starting method. This is not the most successful of the methods known so far, but it has simple coefficients and will serve for illustrative purposes.

To start the method, and simultaneously progress the method a single step forward, the starting method should be a three-output Runge–Kutta method. For input the value of $y ( x _ { 0 } )$ , the method given in the following tableau gives suitable approximations to $y ( x _ { 1 } )$ , $h y ^ { \prime } ( x _ { 1 } )$ and $h ^ { 2 } y ^ { \prime \prime } ( x _ { 1 } )$ :

$$
\begin{array}{c} \left[ \begin{array} { c c } { A } & { U } \\ { B } & { V } \end{array} \right] = \left[ \begin{array} { c c c c c c } { \frac { 1 } { 3 } } & { 0 } & { 0 } & { 0 } & { 0 } \\ { \frac { 1 } { 3 } } & { \frac { 1 } { 3 } } & { 0 } & { 0 } \\ { - \frac { 5 } { 3 } } & { \frac { 4 } { 3 } } & { \frac { 1 } { 3 } } & { 0 } \\ { \frac { 1 } { 1 } } & { - \frac { 1 } { 4 } } & { - \frac { 1 } { 1 2 } } & { \frac { 1 } { 3 } } \\ { 0 } & { 0 } & { 0 } & { 1 } \\ { - 2 } & { - 1 } & { \frac { 2 } { 3 } } & { \frac { 7 } { 3 } } \end{array} \right] 1  \end{array}
$$

For the method given by (547a), the stability function is

$$
R ( z ) = \frac { 1 - \frac { 1 } { 6 } z ^ { 2 } - \frac { 1 } { 2 7 } z ^ { 3 } } { ( 1 - \frac { 1 } { 3 } z ) ^ { 3 } } ,
$$

and it can be verified to satisfy the conditions of A-stability.

Further details concerning stiff ARK methods, and of ARK methods in general, can be found in Rattenbury (2005).

# Exercises 54

54.1 Find the stability matrix of the method given by (542b) and verify that it is RK-stable.

54.2 Does a transformation matrix exist such that the input to the transformed method approximates the two quantities $y ( x _ { n - 1 } + \theta h )$ and $h y ^ { \prime } ( x _ { n - 1 } + \theta h )$ , in each to within $O ( h ^ { 3 } )$ , for some $\theta$ ?

54.3 Show that the method given by (542c) is L-stable.

54.4 Is the same true for the method in which $\sqrt { 2 }$ is replaced by $- { \sqrt { 2 } }$ throughout?

54.5 Which of the two methods (542c) and the method where the sign of $\sqrt { 2 }$ is reversed, is likely to be more accurate?

54.6 Find a third order ARK method with $\beta _ { 3 } = 2$ and $c _ { 2 } = 1$
