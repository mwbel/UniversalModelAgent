# 505 Some recently discovered general linear methods

The methods already introduced in this section were inspired as modifications of Runge–Kutta or linear multistep methods. We now consider two example methods motivated not by either of the classical forms, but by the general linear structure in its own right.

The first of these is known as an ‘Almost Runge–Kutta’ method. That is, although it uses three input and output approximations, it behaves like a Runge–Kutta method from many points of view. The input vectors can be thought of as approximations to $y ( x _ { n - 1 } )$ , $h y ^ { \prime } ( x _ { n - 1 } )$ and $h ^ { 2 } y ^ { \prime \prime } ( x _ { n - 1 } )$ and the output vectors are intended to be approximations to these same quantities, but evaluated at $x _ { n }$ rather than at $x _ { n - 1 }$ :

$$
\left[ { \begin{array} { c c c c c c c } { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { { \frac { 1 } { 1 6 } } } & { 0 } & { 0 } & { 0 } & { 0 } \\ { - { \frac { 1 } { 4 } } } & { 2 } & { 0 } & { 0 } & { 1 } & { - { \frac { 3 } { 4 } } } & { - { \frac { 1 } { 4 } } } \\ { 0 } & { { \frac { 2 } { 3 } } } & { { \frac { 1 } { 6 } } } & { 0 } & { 1 } & { { \frac { 1 } { 6 } } } & { 0 } \\ { 0 } & { { \frac { 2 } { 3 } } } & { { \frac { 1 } { 6 } } } & { 0 } & { 1 } & { { \frac { 1 } { 6 } } } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 1 } & { 0 } & { 0 } & { 0 } \\ { { - { \frac { 1 } { 3 } } } } & { 0 } & { - { \frac { 2 } { 3 } } } & { 2 } & { 0 } & { - 1 } & { 0 } \end{array} } \right] .
$$

The particular example given here has order 4, in contrast to the third order method introduced in Section 27 to illustrate implementation principles. Further details concerning Almost Runge–Kutta methodsare presented in Subsection 543.

The second example is given by the coefficient matrix

<table><tr><td>0 0 1 0 1</td><td>0</td><td>0 0</td><td>1 0 0 1</td><td>0 0 1</td></tr><tr><td>1 1</td><td>1</td><td>1</td><td>0</td><td>0 1</td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>1</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>0</td><td></td><td>R</td><td>N-</td></tr></table>

In the case of (505b), the input values are given respectively as approximations to

$$
\begin{array} { l c l } { y ( x _ { n - 1 } ) , } \\ { y ( x _ { n - 1 } + \frac { 1 } { 2 } h ) + h y ^ { \prime } ( x _ { n - 1 } ) } \end{array}
$$

and to

and the output consists of the same three quantities, to within $O ( h ^ { 4 } )$ , with $x _ { n - 1 }$ advanced one step to $x _ { n }$ . Thus the method has order 3. This is an example of a ‘type 1 DIMSIM method’, to be introduced in Subsection 541.

Both (505a) and (505b) possess the property of RK stability, which guarantees that the method behaves, at least in terms of linear stability, like a Runge–Kutta method. While their multivalue structure is a disadvantage compared with Runge–Kutta methods, they have some desirable properties. For (505a) the stage order is 2, and for (505b) the stage order is 3.

# Exercises 50

50.1 Write the general linear method given by (503a) in transformed form using the matrix

$$
T = \left[ { \begin{array} { r r r r r } { 1 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } & { 0 } \\ { 0 } & { { \frac { 3 } { 4 } } } & { - 1 } & { { \frac { 1 } { 4 } } } \\ { 0 } & { { \frac { 1 } { 6 } } } & { - { \frac { 1 } { 3 } } } & { { \frac { 1 } { 6 } } } \end{array} } \right] .
$$

Note that this converts the method into Nordsieck form.

50.2 Write the general linear method given by (502a) in transformed form using the matrix

$$
T = \left[ \begin{array} { l l } { 1 } & { \frac { 1 } { 6 } } \\ { 0 } & { 1 } \end{array} \right] .
$$

50.3 Write the implicit Runge–Kutta method

$$
\frac { 1 \ { \left| \begin{array} { l l } { 0 } & { 0 } \\ { { \frac { 1 } { 2 } } } & { { \frac { 1 } { 2 } } } \\ { { \frac { 1 } { 2 } } } & { { \frac { 1 } { 2 } } } \end{array} \right| } } { { \left| \begin{array} { l l } { { \frac { 1 } { 2 } } } & { { \frac { 1 } { 2 } } } \end{array} \right| } }
$$

as a general linear method with $r = 2$ , $s = 1$ , by taking advantage of the FSAL property.

50.4 Show that it is possible, by using a suitable transformation, to reduce the general linear method derived in Exercise 50.3 to an equivalent method with $r = s = 1$ . Show that this new method is equivalent to the implicit mid-point rule Runge–Kutta method.

50.5 Write the PEC predictor–corrector method based on the order 2 Adams– Bashforth method and the order 2 Adams–Moulton method in general linear form.

50.6 The following two methods were once popular, but are now regarded as flawed because they are ‘weakly stable’:

$$
\begin{array} { l } { y _ { n } = y _ { n - 2 } + 2 h f ( x _ { n - 1 } , y _ { n - 1 } ) , } \\ { y _ { n } = y _ { n - 3 } + \frac { 3 } { 2 } h ( f ( x _ { n - 1 } , y _ { n - 1 } ) + f ( x _ { n - 2 } , y _ { n - 2 } ) ) . } \end{array}
$$

This means that, although the methods are stable, the polynomial $\alpha$ for each of them has more than one zero on the unit circle. Show how to write them as a cyclic composite pair, using general linear formulation, and that they no longer have such a disadvantage.

50.7 Consider the Runge–Kutta method

Modify this method in the same way as was proposed for (502b), and write the resulting two-value method in general linear form.
