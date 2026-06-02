# 103 The simple pendulum

# Formulation as a differential-algebraic equation

Consider a small mass $m$ attached to a light inelastic string of length $\it l$ , with the other end attached to the origin of coordinates, which can swing back and forth in a vertical plane. Let $X$ , measured in a rightwards direction, and $Y$ , measured in a downward direction, be the coordinates. Because the string is inelastic, the tension $T$ in the string always matches other forces resolved in the direction of the string so as to guarantee that the length does not change.

The way these forces act on the mass is shown in Figure 103(i). Also shown is the angle $\theta$ defined by $X = l \sin ( \theta )$ , $Y = l \cos ( \theta )$ .

We denote by $U$ and $V$ , respectively, the velocity components in the $X$ and

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0001_pages_0001-0070/auto/images/752c49403addb0e147f4c05423a006586ad916b4a0a2e9ab309e953a59e1b11a.jpg)  
Simple pendulum

$Y$ directions. The motion of the pendulum is governed by the equations

$$
\begin{array} { r l r } & { \frac { d X } { d x } = U , } & \\ & { \frac { d Y } { d x } = V , } & \\ & { \displaystyle { m \frac { d U } { d x } = - \frac { T X } { l } , } } & \\ & { \displaystyle { m \frac { d V } { d x } = - \frac { T Y } { l } + m g , } } & \\ & { \displaystyle { X ^ { 2 } + Y ^ { 2 } = l ^ { 2 } , } } & \end{array}
$$

where, in addition to four differential equations (103a)–(103d), the constraint (103e) expresses the constancy of the length of the string. The tension $T$ acts as a control variable, forcing this constraint to remain satisfied. By rescaling variables in a suitable way, the ‘differential-algebraic’ equation system (103a)– (103e) can be rewritten with the constants $m$ , $g$ and $\it l$ replaced by $^ { 1 }$ in each case. In the rescaled formulation write $y _ { 1 } = X$ , $y _ { 2 } = Y$ , $y _ { 3 } = U$ , $y _ { 4 } = V$ and $y _ { 5 } = T$ , and we arrive at the system

$$
\begin{array} { l } { \displaystyle { \frac { d y _ { 1 } } { d x } = y _ { 3 } , } } \\ { \displaystyle { \frac { d y _ { 2 } } { d x } = y _ { 4 } , } } \\ { \displaystyle { \frac { d y _ { 3 } } { d x } = - y _ { 1 } y _ { 5 } , } } \\ { \displaystyle { \frac { d y _ { 4 } } { d x } = - y _ { 2 } y _ { 5 } + 1 } . } \\ { \displaystyle { \frac { 2 } { d } + y _ { 2 } ^ { 2 } = 1 } . } \end{array}
$$

It will be convenient to choose initial values defined in terms of $\theta = \Theta$ , with

the velocity equal to zero. That is,

$$
y _ { 1 } ( 0 ) = \sin ( \Theta ) , \quad y _ { 2 } ( 0 ) = \cos ( \Theta ) , \quad y _ { 3 } ( 0 ) = y _ { 4 } ( 0 ) = 0 , \quad y _ { 5 } ( 0 ) = \cos ( \Theta ) .
$$

The five variables are governed by four differential equations (103f)–(103i), together with the single algebraic constraint (103j). We will say more about this below, but first we consider the classical way of simplifying the problem.

# Formulation as a single second order equation

Make the substitutions $\begin{array} { r l r } { y _ { 1 } } & { { } = } & { \sin ( \theta ) } \end{array}$ , $\begin{array} { r l r } { y _ { 2 } } & { { } = } & { \cos ( \theta ) } \end{array}$ . Because (103j) is automatically satisfied, the value of $y _ { 5 }$ loses its interest and we eliminate this by taking a linear combination of (103h) and (103i). This gives the equation system

$$
\begin{array} { c } { { \displaystyle \cos ( \theta ) \frac { d \theta } { d x } = y _ { 3 } , } } \\ { { \displaystyle - \sin ( \theta ) \frac { d \theta } { d x } = y _ { 4 } , } } \\ { { \displaystyle - \cos ( \theta ) \frac { d y _ { 3 } } { d x } + \sin ( \theta ) \frac { d y _ { 4 } } { d x } = \sin ( \theta ) . } } \end{array}
$$

Differentiate (103k) and (103l) and substitute into (103m) and we obtain the well-known single-equation formulation of the simple pendulum:

$$
{ \frac { d ^ { 2 } \theta } { d x ^ { 2 } } } + \sin ( \theta ) = 0 ,
$$

with initial values

$$
\theta ( 0 ) = \Theta , \qquad \theta ^ { \prime } ( 0 ) = 0 .
$$

It can be shown that the period of the pendulum is given by

$$
T = 4 \int _ { 0 } ^ { \pi / 2 } \frac { d \phi } { \sqrt { 1 - \sin ^ { 2 } \phi \sin ^ { 2 } \frac { \Theta } { 2 } } }
$$

and some values are given in Table 103(I).

The value for $0 ^ { \circ }$ can be interpreted as the period for small amplitudes. The fact that $T$ increases slowly as $\Theta$ increases is the characteristic property of a simple pendulum which makes it of practical value in measuring time.

Formulation as a Hamiltonian problem

In the formulation (103n), write the $H$ as the ‘Hamiltonian’

$$
\begin{array} { r } { H ( p , q ) = \frac { 1 } { 2 } p ^ { 2 } - \cos ( q ) , } \end{array}
$$

Period of simple pendulum for various amplitudes   

<table><tr><td rowspan=1 colspan=2>Θ          T</td></tr><tr><td rowspan=1 colspan=2>0°  6.2831853072</td></tr><tr><td rowspan=1 colspan=2>3°  6.2842620831</td></tr><tr><td rowspan=1 colspan=2>6° 6.2874944421</td></tr><tr><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>6.2928884880</td></tr><tr><td rowspan=1 colspan=1>12°</td><td rowspan=1 colspan=1>6.3004544311</td></tr><tr><td rowspan=1 colspan=1>15°</td><td rowspan=1 colspan=1>6.3102066431</td></tr><tr><td rowspan=1 colspan=1>18°</td><td rowspan=1 colspan=1>6.3221637356</td></tr><tr><td rowspan=1 colspan=1>21°</td><td rowspan=1 colspan=1>6.3363486630</td></tr><tr><td rowspan=1 colspan=1>24°</td><td rowspan=1 colspan=1>6.3527888501</td></tr><tr><td rowspan=1 colspan=1>27°</td><td rowspan=1 colspan=1>6.3715163462</td></tr><tr><td rowspan=1 colspan=1>30°</td><td rowspan=1 colspan=1>6.3925680085</td></tr></table>

where $q \ = \ \theta$ and $p \ = \ d \theta / d x$ . The second order equation (103n) is now equivalent to the first order system

$$
\left[ \begin{array} { c } { { p ^ { \prime } } } \\ { { q ^ { \prime } } } \end{array} \right] = \left[ \begin{array} { c c } { { 0 } } & { { - 1 } } \\ { { 1 } } & { { 0 } } \end{array} \right] \left[ \begin{array} { c } { { \frac { \partial H } { \partial p } } } \\ { { \frac { \partial H } { \partial q } } } \end{array} \right] .
$$

Differential index and index reduction

Carry out three steps, of which the first is to differentiate (103j) and substitute from (103f) and (103g) to give the result

$$
y _ { 1 } y _ { 3 } + y _ { 2 } y _ { 4 } = 0 .
$$

The second step is to differentiate (103o) and to make various substitutions from (103f)–(103i) to arrive at the equation

$$
y _ { 2 } + y _ { 3 } ^ { 2 } + y _ { 4 } ^ { 2 } - y _ { 5 } = 0 .
$$

The third and final step is to differentiate (103p) and make various substitutions to arrive at the result

$$
\frac { d y _ { 5 } } { d x } = \frac { y _ { 2 } } { d x } + 2 y _ { 3 } \frac { d y 3 } { d x } + 2 y _ { 4 } \frac { d y _ { 4 } } { d x } = y _ { 4 } + 2 y _ { 3 } ( - y _ { 1 } y _ { 5 } ) + 2 y _ { 4 } ( - y _ { 2 } y _ { 5 } + 1 ) ,
$$

which simplifies to

$$
{ \frac { d y _ { 5 } } { d x } } = 3 y _ { 4 } .
$$

Given that consistent initial values are used, it seems that the equations (103f)–(103i) together with any of (103j), (103o), (103p) or (103q) give identical solutions.

Which of the possible formulations should be used? From the point of view of physical modelling, it seems to be essential to require that the length constraint (103j) should hold exactly. On the other hand, when it comes to numerical approximations to solutions, it is found that the use of this constraint in the problem description creates serious computational difficulties. It also seems desirable from a modelling point of view to insist that (103o) should hold exactly, since this simply states that the direction of motion is tangential to the arc on which it is constrained to lie.
