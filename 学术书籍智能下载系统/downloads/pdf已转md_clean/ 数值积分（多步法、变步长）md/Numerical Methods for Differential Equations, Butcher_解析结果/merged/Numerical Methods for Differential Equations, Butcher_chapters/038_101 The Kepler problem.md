# 101 The Kepler problem

The problems discussed in this section are selected from the enormous range of possible scientific applications. The first example problem describes the motion of a single planet about a heavy sun. By this we mean that, although the sun exerts a gravitational attraction on the planet, we regard the corresponding attraction of the planet on the sun as negligible, and that the sun will be treated as being stationary. This approximation to the physical system can be interpreted in another way: even though both bodies are in motion about their centre of mass, the motion of the planet relative to the sun can be modelled using the simplification we have described. We also make a further assumption, that the motion of the planet is confined to a plane.

Let $y _ { 1 } ( x )$ and $y _ { 2 } ( x )$ denote rectangular coordinates centred at the sun, specifying at time $x$ the position of the planet. Also let $y _ { 3 } ( x )$ and $y _ { 4 } ( x )$ denote the components of velocity in the $y _ { 1 }$ and $y _ { 2 }$ directions, respectively. If $M$ denotes the mass of the sun, $\gamma$ the gravitational constant and $m$ the mass of the planet, then the attractive force on the planet will have magnitude

$$
\frac { \gamma M m } { y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } } .
$$

Resolving this force in the coordinate directions, we find that the components of acceleration of the planet, due to this attraction, are $- \gamma M y _ { 1 } ( y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } ) ^ { - 3 / 2 }$ and $- \gamma M y _ { 2 } ( y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } ) ^ { - 3 / 2 }$ , where the negative sign denotes the inward direction of the acceleration.

We can now write the equations of motion:

$$
\begin{array} { l } { \displaystyle \frac { d y _ { 1 } } { d x } = y _ { 3 } , } \\ { \displaystyle \frac { d y _ { 2 } } { d x } = y _ { 4 } , } \\ { \displaystyle \frac { d y _ { 3 } } { d x } = - \frac { \gamma M y _ { 1 } } { ( y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } ) ^ { 3 / 2 } } , } \\ { \displaystyle \frac { d y _ { 4 } } { d x } = - \frac { \gamma M y _ { 2 } } { ( y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } ) ^ { 3 / 2 } } . } \end{array}
$$

By adjusting the scales of the variables, the factor $\gamma M$ can be removed from the formulation, and we arrive at the equations

$$
\begin{array} { l } { \displaystyle \frac { d y _ { 1 } } { d x } = y _ { 3 } , } \\ { \displaystyle \frac { d y _ { 2 } } { d x } = y _ { 4 } , } \\ { \displaystyle \frac { d y _ { 3 } } { d x } = - \frac { y _ { 1 } } { ( y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } ) ^ { 3 / 2 } } , } \\ { \displaystyle \frac { d y _ { 4 } } { d x } = - \frac { y _ { 2 } } { ( y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } ) ^ { 3 / 2 } } . } \end{array}
$$

The solutions of this system are known to be conic sections, that is, ellipses, parabolas or hyperbolas, if we ignore the possibility that the trajectory is a straight line directed either towards or away from the sun. We investigate this further after we have shown that two ‘first integrals’, or invariants, of the solution exist.

Theorem 101A The quantities

$$
\begin{array} { l } { { H = \displaystyle \frac { 1 } { 2 } \left( y _ { 3 } ^ { 2 } + y _ { 4 } ^ { 2 } \right) - ( y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } ) ^ { - 1 / 2 } , } } \\ { { A = y _ { 1 } y _ { 4 } - y _ { 2 } y _ { 3 } } } \end{array}
$$

are constant.

Proof. We verify that the values of $d H / d x$ and $d A / d x$ are zero if $y$ satisfies (101a)–(101d). We have

$$
{ \begin{array} { r l } & { { \cfrac { d H } { d x } } = y _ { 3 } { \cfrac { d y _ { 3 } } { d x } } + y _ { 4 } { \cfrac { d y _ { 4 } } { d x } } + y _ { 1 } { \cfrac { d y _ { 1 } } { d x } } ( y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } ) ^ { - 3 / 2 } + y _ { 2 } { \cfrac { d y _ { 2 } } { d x } } ( y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } ) ^ { - 3 / 2 } } \\ & { \qquad = - { \cfrac { y _ { 1 } y _ { 3 } } { ( y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } ) ^ { 3 / 2 } } } - { \cfrac { y _ { 2 } y _ { 4 } } { ( y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } ) ^ { 3 / 2 } } } + { \cfrac { y _ { 1 } y _ { 3 } } { ( y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } ) ^ { 3 / 2 } } } + { \cfrac { y _ { 2 } y _ { 4 } } { ( y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } ) ^ { 3 / 2 } } } } \\ & { \qquad = 0 } \end{array} }
$$

and

$$
\begin{array} { r c l } { { } } & { { } } & { { \displaystyle { \frac { d A } { d x } } = y _ { 1 } \displaystyle { \frac { d y _ { 4 } } { d x } } + \frac { d y _ { 1 } } { d x } y _ { 4 } - y _ { 2 } \displaystyle { \frac { d y _ { 3 } } { d x } } - \frac { d y _ { 2 } } { d x } y _ { 3 } } } \\ { { } } & { { } } & { { = - \displaystyle { \frac { y _ { 1 } y _ { 2 } } { ( y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } ) ^ { 3 / 2 } } } + y _ { 3 } y _ { 4 } + \frac { y _ { 2 } y _ { 1 } } { ( y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } ) ^ { 3 / 2 } } - y _ { 4 } y _ { 3 } } } \\ { { } } & { { } } & { { = 0 . } } \end{array}
$$

The quantities $H$ and $A$ are the ‘Hamiltonian’ and ‘angular momentum’, respectively. Note that $H = T + V$ , where $T = \textstyle { \frac { 1 } { 2 } } \left( y _ { 3 } ^ { 2 } + y _ { 4 } ^ { 2 } \right)$ is the kinetic energy and $V = - ( y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } ) ^ { - 1 / 2 }$ is the potential energy.

A further property of this problem is its invariance under changes of scale of the variables:

$$
\begin{array} { r l } & { y _ { 1 } = \alpha ^ { - 2 } \overline { { y } } _ { 1 } , } \\ & { y _ { 2 } = \alpha ^ { - 2 } \overline { { y } } _ { 2 } , } \\ & { y _ { 3 } = \alpha \overline { { y } } _ { 3 } , } \\ & { y _ { 4 } = \alpha \overline { { y } } _ { 4 } , } \\ & { x = \alpha ^ { - 3 } \overline { { x } } . } \end{array}
$$

The Hamiltonian and angular momentum get scaled to

$$
\begin{array} { l l l } { { \overline { { { H } } } = \displaystyle \frac { 1 } { 2 } \left( \overline { { { y } } } _ { 3 } ^ { 2 } + \overline { { { y } } } _ { 4 } ^ { 2 } \right) - ( \overline { { { y } } } _ { 1 } ^ { 2 } + \overline { { { y } } } _ { 2 } ^ { 2 } ) ^ { - 1 / 2 } = \alpha ^ { - 2 } H , } } \\ { { \overline { { { A } } } = \overline { { { y } } } _ { 1 } \overline { { { y } } } _ { 4 } - \overline { { { y } } } _ { 2 } \overline { { { y } } } _ { 3 } } } & { { = \alpha A . } } \end{array}
$$

A second type of transformation is based on a two-dimensional orthogonal transformation (that is, a rotation or a reflection or a composition of these) $Q$ , where $Q ^ { - 1 } = Q ^ { \ i } .$ The time variable $x$ is invariant, and the position and velocity variables get transformed to

$$
\left[ \begin{array} { l } { y _ { 1 } } \\ { y _ { 2 } } \\ { y _ { 3 } } \\ { y _ { 4 } } \end{array} \right] = \left[ \begin{array} { l l } { Q } & { 0 } \\ { 0 } & { Q } \end{array} \right] \left[ \begin{array} { l } { \overline { { y } } _ { 1 } } \\ { \overline { { y } } _ { 2 } } \\ { \overline { { y } } _ { 3 } } \\ { \overline { { y } } _ { 4 } } \end{array} \right] .
$$

It is easy to see that $A = 0$ implies that the trajectory lies entirely in a subspace defined by $\cos ( \theta ) y _ { 1 } = \sin ( \theta ) y _ { 2 }$ , $\cos ( \theta ) y _ { 3 } = \sin ( \theta ) y _ { 4 }$ for some fixed angle $\theta$ . We move on from this simple case and assume that $A \neq 0$ . The sign of $H$ is of crucial importance: if $H \geq 0$ then it is possible to obtain arbitrarily high values of $y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 }$ without $y _ { 3 } ^ { 2 } + y _ { 4 } ^ { 2 }$ vanishing. We exclude this case for the present discussion and assume that $H \ < \ 0$ . Scale $H$ so that it has a value $- \frac { 1 } { 2 }$ and at the same time $A$ takes on a positive value. This value cannot exceed $1$ because we can easily verify an identity involving the derivative of $r = \sqrt { y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } }$ . This identity is

$$
\left( r \frac { d r } { d x } \right) ^ { 2 } = 2 H r ^ { 2 } + 2 r - A ^ { 2 } = - r ^ { 2 } + 2 r - A ^ { 2 } .
$$

Since the left-hand side cannot be negative, the quadratic function in $r$ on the right-hand side must have real roots. This implies that $A \ \leq \ 1$ . Write $A = { \sqrt { 1 - e ^ { 2 } } }$ , for $e \geq 0$ , where we see that $e$ is the eccentricity of an ellipse on which the orbit lies. The minimum and maximum values of $r$ are found to be $1 - e$ and $1 + e$ , respectively. Rotate axes so that when $r = 1 - e$ , which we take as the starting point of time, $y _ { 1 } = 1 - e$ and $y _ { 2 } = 0$ . At this point we find that $y _ { 3 } = 0$ and $y _ { 4 } = \sqrt { ( 1 + e ) / ( 1 - e ) }$ .

Change to polar coordinates by writing $y _ { 1 } = r \cos ( \theta )$ , $y _ { 2 } = r \sin ( \theta )$ . It is found that

$$
\begin{array} { l } { { y _ { 3 } = \displaystyle \frac { d y _ { 1 } } { d x } = \displaystyle \frac { d r } { d x } \cos ( \theta ) - r \displaystyle \frac { d \theta } { d x } \sin ( \theta ) , } } \\ { { y _ { 4 } = \displaystyle \frac { d y _ { 2 } } { d x } = \displaystyle \frac { d r } { d x } \sin ( \theta ) + r \displaystyle \frac { d \theta } { d x } \cos ( \theta ) , } } \end{array}
$$

so that, because $y _ { 1 } y _ { 4 } - y _ { 2 } y _ { 3 } = { \sqrt { 1 - e ^ { 2 } } }$ , we find that

$$
r ^ { 2 } { \frac { d \theta } { d x } } = { \sqrt { 1 - e ^ { 2 } } } .
$$

From (101e) and (101f) we find a differential equation for the path traced out by the orbit

$$
\left( \frac { d r } { d \theta } \right) ^ { 2 } = \frac { 1 } { 1 - e ^ { 2 } } r ^ { 2 } \left( e ^ { 2 } - ( 1 - r ) ^ { 2 } \right) ,
$$

and we can verify that this is satisfied by

$$
\frac { 1 - e ^ { 2 } } { r } = 1 + e \cos ( \theta ) .
$$

If we change back to Cartesian coordinates, we find that all points on the trajectory lie on the ellipse

$$
( y _ { 1 } + e ) ^ { 2 } + \frac { y _ { 2 } ^ { 2 } } { 1 - e ^ { 2 } } = 1 ,
$$

with centre $( - e , 0 )$ , eccentricity $e$ , and major and minor axis lengths 1 and $\sqrt { 1 - e ^ { 2 } }$ respectively.

As we have seen, a great deal is known about this problem. However, much less is known about the motion of a many-body gravitational system.

One of the aims of modern numerical analysis is to understand the behaviour of various geometrical properties. In some cases it is possible to preserve the value of quantities that are invariant in the exact solution. In other situations, such as problems where the Hamiltonian is theoretically conserved, it may be preferable to conserve other properties, such as what is known as ‘symplectic behaviour’.

We consider further gravitational problems in Subsection 120.
