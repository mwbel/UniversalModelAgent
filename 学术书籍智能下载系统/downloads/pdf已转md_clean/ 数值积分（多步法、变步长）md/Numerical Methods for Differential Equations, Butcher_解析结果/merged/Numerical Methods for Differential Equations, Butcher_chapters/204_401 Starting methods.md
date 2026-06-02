# 401 Starting methods

As we pointed out in Subsection 246, linear multistep methods require starting methods even to carry out a single step. We consider, in general terms, some of the procedures used to obtain starting values; we then discuss any unifying characteristics they might have.

One obvious approach to starting a $k$ -step method is to carry out $k - 1$ steps with a Runge–Kutta method, preferably of the same order as the linear multistep method itself. An interesting variation of this standard procedure is to use specially constructed Runge–Kutta methods which make it possible to move forward several steps at a time (Gear, 1980).

A second approach, which fits naturally into the style of linear multistep methods, is to solve a system of equations representing the integrals of $y ^ { \prime } ( x )$ from $x _ { 0 }$ to each of $x _ { 1 }$ , $x _ { 2 }$ , . . . , $x _ { k - 1 }$ written, in each case, as a quadrature formula with abscissae at these same points. We illustrate this in the case of the third order Adams–Bashforth method

$$
y _ { n } = y _ { n - 1 } + { \frac { h } { 1 2 } } { \bigl ( } 2 3 f ( x _ { n - 1 } , y _ { n - 1 } ) - 1 6 f ( x _ { n - 2 } , y _ { n - 2 } ) + 5 f ( x _ { n - 3 } , y _ { n - 3 } ) { \bigr ) } ,
$$

for which appropriate quadrature formulae, adapted to a differential equation, are

$$
\begin{array} { l } { { y _ { 1 } = y _ { 0 } + \displaystyle \frac { h } { 1 2 } \big ( 5 f ( x _ { 0 } , y _ { 0 } ) + 8 f ( x _ { 1 } , y _ { 1 } ) - f ( x _ { 2 } , y _ { 2 } ) \big ) , } } \\  { \big \} _ { 2 } = y _ { 0 } + \displaystyle \frac { h } { 3 } \big ( f ( x _ { 0 } , y _ { 0 } ) + 4 f ( x _ { 1 } , y _ { 1 } ) + f ( x _ { 2 } , y _ { 2 } ) \big ) . } \end{array}
$$

These equations are solved by functional iteration to yield approximations $y _ { 1 } \approx y ( x _ { 1 } )$ and $y _ { 2 } \approx y ( x _ { 2 } )$ .

In modern variable order codes, it is usual to start with order 1 or order 2, and to adapt to higher orders when this becomes possible and when it becomes advantageous from an efficiency point of view. This means that order $k$ may be reached after many steps with varying stepsize.

The common feature of these approaches to starting a linear multistep method is that each is, in reality, a Runge–Kutta method possessing multiple outputs, to furnish approximations at a number of equally spaced points. For example, the iteration scheme given by (401a) and (401b) can be represented by the Runge–Kutta scheme

<table><tr><td>：</td><td>0</td><td>0 0</td></tr><tr><td></td><td>中</td><td>1 12</td></tr><tr><td></td><td>G</td><td></td></tr><tr><td></td><td></td><td>1</td></tr><tr><td></td><td></td><td></td></tr><tr><td rowspan="3"></td><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td>中立</td></tr></table>

in which the two output approximations are for $y _ { 1 }$ and $y _ { 2 }$ , respectively. This scheme, like any starting procedure of Runge–Kutta type, has a property we assume for starting schemes used for the definition of convergence. This is that the quantities computed as approximations to $y _ { i }$ , $i = 1 , 2 , \ldots , k - 1$ , all converge to $y ( x _ { 0 } )$ as $h  0$ .
