# 120 Many-body gravitational problems

We consider a more general gravitational problem involving $_ { n }$ mutually attracting masses $M _ { 1 } , M _ { 2 } , \ldots , M _ { n }$ at position vectors $y _ { 1 } ( x ) , y _ { 2 } ( x ) , \dots , y _ { n } ( x )$ , satisfying the $_ { 3 n }$ -dimensional second order differential equation system

$$
y _ { i } ^ { \prime \prime } ( x ) = - \sum _ { j \neq i } { \frac { \gamma M _ { j } ( y _ { i } - y _ { j } ) } { \| y _ { i } - y _ { j } \| ^ { 3 } } } , \qquad i = 1 , 2 , \ldots , n .
$$

Reformulated as a first order system, the problem is $6 n$ -dimensional because each of the $y _ { i }$ has three components and the velocity vectors $y _ { i } ^ { \prime }$ also have three components.

To reduce this problem to a manageable level in situations of practical interest, some simplifications can be made. For example, in models of the solar system, the most massive planets, Jupiter, Uranus, Neptune and Saturn, are typically regarded as the only bodies capable of influencing the motion of the sun and of each other. The four small planets closest to the sun, Mercury, Venus, Earth and Mars, are, in this model, regarded as part of the sun in the sense that they add to its mass in attracting the heavy outer planets towards the centre of the solar system. To study the motion of the small planets or of asteroids, they can be regarded as massless particles, moving in the gravitation fields of the sun and the four large planets, but not at the same time influencing their motion.

Another model, involving only three bodies, is useful for studying the motion of an Earth–Moon satellite or of an asteroid close enough to the Earth to be strongly influenced by it as well as by the Sun. This system, known as the restricted three–body problem, regards the two heavy bodies as revolving in fixed orbits about their common centre of mass and the small body as attracted by the two larger bodies but not affecting their motion in any way. If it is possible to approximate the large-body orbits as circles, then a further simplification can be made by working in a frame of reference that moves with them. Thus, we would regard the two large bodies as being fixed in space with their rotation in the original frame of reference translated into a modification of the equations of gravitational motion.

To simplify this discussion, we use units scaled to reduce a number of constants to unit value. We scale the masses of the two larger bodies to $1 - \mu$ and $\mu$ and their positions relative to the moving reference frame by the vectors $( \mu - 1 ) e _ { 1 }$ and $\mu e _ { 1 }$ , so that their centre of mass is at the origin of coordinates. Write $y _ { 1 }$ , $y _ { 2 }$ and $y _ { 3 }$ as the scalar variables representing the position coordinates of the small body and $y _ { 4 }$ , $y _ { 5 }$ and $y _ { 6 }$ as the corresponding velocity coordinates. Under these assumptions, the equations of motion become

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0001_pages_0001-0070/auto/images/930f4d2a1612a67d13ed6e9bdb6b9e75b0bb8c729f031ebc133da1960b39358a.jpg)  
A solution to the restricted three-body problem

$$
\begin{array} { r l } & { y _ { 1 } ^ { \prime } = y _ { 4 } , } \\ & { y _ { 2 } ^ { \prime } = y _ { 5 } , } \\ & { y _ { 3 } ^ { \prime } = y _ { 6 } , } \\ & { y _ { 4 } ^ { \prime } = 2 y _ { 5 } + y _ { 1 } - \frac { \mu \left( y _ { 1 } + \mu - 1 \right) } { \left( y _ { 2 } ^ { 2 } + y _ { 3 } ^ { 2 } + \left( y _ { 1 } + \mu - 1 \right) ^ { 2 } \right) ^ { 3 / 2 } } - \frac { \left( 1 - \mu \right) \left( y _ { 1 } + \mu \right) } { \left( y _ { 2 } ^ { 2 } + y _ { 3 } ^ { 2 } + \left( y _ { 1 } + \mu \right) ^ { 2 } \right) ^ { 3 / 2 } } , } \\ & { y _ { 5 } ^ { \prime } = - 2 y _ { 4 } + y _ { 2 } - \frac { \mu y _ { 2 } } { \left( y _ { 2 } ^ { 2 } + y _ { 3 } ^ { 2 } + \left( y _ { 1 } + \mu - 1 \right) ^ { 2 } \right) ^ { 3 / 2 } } - \frac { \left( 1 - \mu \right) y _ { 2 } } { \left( y _ { 2 } ^ { 2 } + y _ { 3 } ^ { 2 } + \left( y _ { 1 } + \mu \right) ^ { 2 } \right) ^ { 3 / 2 } } } \\ & { y _ { 6 } ^ { \prime } = - \frac { \mu y _ { 3 } } { \left( y _ { 2 } ^ { 2 } + y _ { 3 } ^ { 2 } + \left( y _ { 1 } + \mu - 1 \right) ^ { 2 } \right) ^ { 3 / 2 } } - \frac { \left( 1 - \mu \right) y _ { 3 } } { \left( y _ { 2 } ^ { 2 } + y _ { 3 } ^ { 2 } + \left( y _ { 1 } + \mu \right) ^ { 2 } \right) ^ { 3 / 2 } } . } \end{array}
$$

Planar motion is possible; that is, solutions in which $y _ { 3 } = y _ { 6 } = 0$ at all times. One of these is shown in Figure $1 2 0 ( \mathrm { i } )$ , with the values of $( y _ { 1 } , y _ { 2 } )$ plotted as the orbit evolves. The heavier mass is at the point $( \mu , 0 )$ and the lighter mass is at $( 1 - \mu , 0 )$ , where $( 0 , 0 )$ is marked 0 and $( 1 , 0 )$ is marked $^ { 1 }$ . For this calculation the value of $\mu = 1 / 8 1 . 4 5$ was selected, corresponding to the Earth-Moon system. The initial values for this computation were $\begin{array} { c c l } { { ( y _ { 1 } , y _ { 2 } , y _ { 3 } , y _ { 4 } , y _ { 5 } , y _ { 6 } ) } } & { { = } } & { { ( 0 . 9 9 4 , 0 , 0 , 0 , - 2 . 0 0 1 5 8 5 1 0 6 3 7 9 0 8 2 5 2 2 4 , 0 ) } } \end{array}$ and the period was 17.06521656015796.

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0001_pages_0001-0070/auto/images/ac27af0624e5d41c865c35f221fb73ac279a0bb1b9dfc6891cd3ce66c0fbed63.jpg)  
A second solution to the restricted three-body problem

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0001_pages_0001-0070/auto/images/5d87e128594947b12440fc27b1b2e878d9230caf38c4456f39efa69733c0c93b.jpg)  
A figure-of-eight orbit for three equal masses

A second solution, identical except for the initial value $\left( y _ { 1 } , y _ { 2 } , y _ { 3 } , y _ { 4 } , y _ { 5 } , y _ { 6 } \right)$ $= ( 0 . 8 7 9 7 8 , 0 , 0 , 0 , - 0 . 3 7 9 7 , 0 )$ ) and a period 19.14045706162071, is shown in Figure 120(ii).

If the three masses are comparable in value, then the restriction to a simpler system that we have considered is not available. However, in the case of a number of equal masses, other symmetries are possible. We consider just a single example, in which three equal, mutually attracting masses move in a figure-of-eight orbit. This is shown in Figure 120(iii).

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0001_pages_0001-0070/auto/images/66accfeec67fab96b5f831d1d86131268b2cdc28faf615ce7657237c200587ee.jpg)  
Solution to delay differential equation (121b)

121 Delay problems and discontinuous solutions

A functional differential equation is one in which the rate of change of $y ( x )$ depends not just on the values of $y$ for the same time value, but also on time values less than $x$ . In the simplest case, this has the form

$$
y ^ { \prime } ( x ) = f ( x , y ( x ) , y ( x - \tau ) ) ,
$$

where $^ { - }$ is a constant delay. Note that this cannot be cast as an initial value problem with the hope of actually defining a unique solution, because at an initial point $x _ { 0 }$ , the derivative depends on the value of $y ( x _ { 0 } - \tau )$ . What we will need to do in the case of (121a) is to specify the value of $y$ on an initial interval $[ x _ { 0 } - \tau , x _ { 0 } ]$ .

A linear delay differential equation

We consider the problem given by

$$
\begin{array} { r } { y ^ { \prime } ( x ) = - y ( x - \frac { \pi } { 2 } ) , \quad x > 0 , \qquad y ( x ) = x , \quad x \in [ - \frac { \pi } { 2 } , 0 ] . } \end{array}
$$

For $x$ in the interval $[ 0 , \frac { \pi } { 2 } ]$ we find

$$
y ( x ) = - \int _ { 0 } ^ { x } ( x - { \textstyle \frac { \pi } { 2 } } ) d x = { \textstyle \frac { 1 } { 2 } } x ( \pi - x ) ,
$$

with $\begin{array} { r } { y ( \frac { \pi } { 2 } ) = \frac { 1 } { 8 } \pi ^ { 2 } } \end{array}$ . This process can be repeated over the sequence of intervals $[ \frac { \pi } { 2 } , \pi ]$ , $[ \pi , { \textstyle \frac { 3 \pi } { 2 } } ]$ , $\cdot \cdot \cdot$ to obtain values of $y ( x )$ shown in Figure 121(i) for $x \leq 4 \pi$ .

It appears that the solution is attempting to approximate sinusoidal behaviour as time increases. We can verify this by estimating a local amplitude defined by

$$
A ( x ) = ( y ( x ) ^ { 2 } + y ^ { \prime } ( x ) ^ { 2 } ) ^ { \frac { 1 } { 2 } } .
$$

This function is also shown in Figure $\mathrm { 1 2 1 ( i ) }$ and we note the discontinuity at $x \ = \ 0$ , corresponding to the discontinuity in the value of $y ^ { \prime } ( x )$ . Such discontinuities are to be expected because the right-derivative is given by the formula for $y ^ { \prime } ( x )$ for $x$ positive and the left-derivative is found from the derivative of the initial function. For each positive integral multiple of $\scriptstyle { \frac { 1 } { 2 } } \pi$ , there will always be an inherited non-smooth behaviour but this will be represented by a discontinuity in increasingly higher derivatives.

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0001_pages_0001-0070/auto/images/db14b96a7e562ed9350742357a0ab32dc9586a0a1247cd5b36edc95694748014.jpg)  
Solution to neutral delay differential equation (121c)

We will now consider a problem with two delays.

# An example with persistent discontinuities

A delay differential equation of ‘neutral type’ is one in which delayed values of $y ^ { \prime }$ also occur in the formulation. An example of this type of problem is

$$
\begin{array} { r l r l } & { y ^ { \prime } ( x ) = \frac { 1 } { 2 } y ^ { \prime } ( x - 1 ) + a y ( x - \sqrt { 2 } ) , } & & { x > 0 , } \\ & { y ( x ) = 1 , } & & { x \in [ - \sqrt { 2 } , 0 ] , } \end{array}
$$

where the constant is given by $\begin{array} { r } { a = \exp ( \sqrt { 2 } ) - \frac { 1 } { 2 } \exp ( \sqrt { 2 } - 1 ) } \end{array}$ and was contrived to ensure that $\exp ( x )$ would have been a solution, if the initial information had been defined in terms of that function.

The solution is shown in Figure 121(ii) and we see that it seems to be approximating exponential behaviour more and more closely as $x$ increases. However, there is a discontinuity in $y ^ { \prime } ( x )$ at every positive integer value of $x$ . Specifically, for each $n$ there is a jump given by

$$
\operatorname* { l i m } _ { x \to n + } y ^ { \prime } ( x ) - \operatorname* { l i m } _ { x \to n - } y ^ { \prime } ( x ) = 2 ^ { - n } a .
$$
