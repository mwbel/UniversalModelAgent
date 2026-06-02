# 554 Methods with property $F ^ { \prime }$

There is a practical advantage for methods in which

$$
\begin{array} { r l } & { e _ { 1 } ^ { \top } B = e _ { p + 1 } ^ { \top } A , } \\ & { e _ { 2 } ^ { \top } B = e _ { p + 1 } ^ { \top } . } \end{array}
$$

A consequence of these assumptions is that $\beta _ { p } = 0$ .

For this subclass of IRKS methods, in addition to the existence of reliable approximations

$$
h F _ { i } = h y ^ { \prime } ( x _ { n - 1 } + h c _ { i } ) + O ( h ^ { p + 2 } ) , \qquad i = 1 , 2 , \ldots , p + 1 ,
$$

where $y ( x )$ is the trajectory such that $y ( x _ { n - 1 } ) = y _ { 1 } ^ { [ n - 1 ] }$ , the value of $y _ { 2 } ^ { \lfloor n - 1 \rfloor }$ provides an additional approximation

$$
h F _ { 0 } = h y ^ { \prime } ( x _ { n - 1 } ) + O ( h ^ { p + 2 } ) ,
$$

which can be used together with the $p + 1$ scaled derivative approximations given by (554a).

This information makes it possible to estimate the values of

$$
h ^ { p + 1 } y ^ { ( p + 1 ) } ( x _ { n } ) \quad \mathrm { a n d } \quad h ^ { p + 2 } y ^ { ( p + 2 ) } ( x _ { n } ) ,
$$

which are used for local error estimation purposes both for the method currently in use as well as for a possible method of one higher order. Thus we can find methods which provide rational criteria for stepsize selection as well as for order selection.

Using terminology established in Butcher (2006), we will refer to methods with this special property as possessing property F. They are an extension of FSAL Runge–Kutta methods.

The derivation of methods based on the ideas in Subsections 553 and 554 is joint work with William Wright and is presented in Wright (2002) and Butcher and Wright (2003, 2003a).
