# CHAPTER 5

# 5.l Displacement of a Rigid Body

A rigid body can be viewed as a system of particles where the relative distances between particles are fixed. The position ofa rigid body is defined by any three points on it, not in the same straight line.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0002_pages_0071-0140/auto/images/f79c1c9cf02de9c8dd6297f991fca4f63dce3b6ae9d0df7fdfcd6f0d3b4bd707.jpg)  
Fig. 5.l-l. Displacement of a rigid body.

The motion of a rigid body can be described by a translation of some reference point O, plus a rotation about some axis through O. Consider three arbitrary noncolinear points 1, 2, 3,in the initial and final positions $1 ^ { \prime }$ ， $2 ^ { \prime }$ ， $3 ^ { \prime }$ , as shown in Fig. 5.1-1. The first point 1 can be brought to $1 ^ { \prime }$ by a translation so that the new position is $1 ^ { \prime } , 2 ^ { \prime \prime } , 3 ^ { \prime \prime }$ . Next, rotate about an axis through $1 ^ { \prime }$ which is perpendicular to the plane $1 ^ { \prime }$ ， $2 ^ { \prime \prime }$ ， $2 ^ { \prime }$ ,bringing $2 ^ { \prime \prime }$ to coincide with $2 ^ { \prime }$ . Finally,rotate about anaxis through $1 ^ { \prime }$ and $2 ^ { \prime }$ ,tobring $3 ^ { \prime \prime \prime }$ to $3 ^ { \prime }$

We will now show Euler's proof that the two individual rotations can be replaced by a single rotation. Draw a unit sphere about point $1 ^ { \prime }$ and where the two rotation axes pierce it, connect the points by a great circle as shown in Fig. 5.1-2. Measure off $\mathcal { Y } _ { 2 } \boldsymbol { \theta } _ { 1 }$ on each side of the great circle at axis 1,drawing two other great circles,and do likewise with angle $\theta _ { 2 }$ at axis 2. Now a rotation of $\theta _ { 1 }$ about axis 1 will bring point $a$ to $b$ ,and a rotation $\theta _ { 2 }$ about axis 2 will bring $b$ back to $a$ .Thus $1 ^ { \prime } a$ is an undisturbed line during rotation $\theta _ { 1 }$ and $\theta _ { 2 }$ ,and therefore it must be the resultant axis of rotation. Note that $1 ^ { \prime } a$ is not in the plane containing the axes of rotation $\theta _ { 1 }$ and $\theta _ { 2 }$ , which again points out the fact that finite rotations do not possess the properties of vectors.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0002_pages_0071-0140/auto/images/ae77387e45a2928da4600b2beec121d400c7ee139135a42b215cebae61c3ab24.jpg)  
Fig. 5.l-2. Resultant rotation axis by Euler's proof.

# 5.2 Moment of Momentum of a Rigid Body (About a Fixed Point or the Moving Center of Mass)

Let body axes $x$ ， $y , z$ be attached tothebody with the origin $O$ at any point. The velocity of any point $i$ on the body is then,

$$
\mathbf { v } _ { i } = \mathbf { v } _ { 0 } + { \boldsymbol { \omega } } \times \mathbf { r } _ { i }
$$

where ω is the angular velocity of the body.

The moment of momentum about the origin $O$ of the $_ x$ ， $y$ ， $_ { z }$ ,system is,

$$
\begin{array} { l } { { \displaystyle { \tt h } _ { 0 } = \sum _ { i } { \tt r } _ { i } \times m _ { i } ( { \tt v } _ { 0 } + \omega \times { \tt r } _ { i } ) } } \\ { { \displaystyle \quad = \sum _ { i } { \tt r } _ { i } \times ( \omega \times { \bf r } _ { i } ) m _ { i } - { \tt v } _ { 0 } \times \sum _ { i } m _ { i } { \tt r } _ { i } } } \end{array}
$$

If the reference point $O$ is stationary, $\mathbf { v } _ { 0 } = 0$ ,whereas if $O$ coincides with the center of mass, $\begin{array} { r } { \sum _ { i } m _ { i } \mathbf { r } _ { i } = 0 } \end{array}$ Thus,if $O$ is fixed,oeteoss, the angular momentum is given by the first term of the above equation, which can be expressed by the following integral,

$$
\mathbf { h } _ { 0 } = \int \mathbf { r } \times \left( { \boldsymbol { \omega } } \times \mathbf { r } \right) d m
$$

To evaluate this integral, we note that the first cross product $\omega \times \textbf { r }$ is

$$
\begin{array} { r } { \mathfrak { \omega } \times \mathfrak { r } = \left| \begin{array} { l l l } { \mathbf { i } } & { \mathbf { j } } & { \mathbf { k } } \\ { \omega _ { x } } & { \omega _ { y } } & { \omega _ { z } } \\ { x } & { y } & { z } \end{array} \right| = ( \omega _ { y } z - \omega _ { z } y ) \mathbf { i } + ( \omega _ { z } x - \omega _ { x } z ) \mathbf { j } } \end{array}
$$

Multiplying by dm, we have the $_ { x }$ ， y, z, components of the momentum of dm, as shown in Fig. 5.2-1.

The cross product r X (ω X r) dm is,

$$
\begin{array} { r } { \mathrm {  ~ { \widetilde { \ x } ~ } } ( \omega \times \mathrm {  ~ r ~ } ) d m = \left| \begin{array} { c c c } { \mathrm {  ~ i ~ } } & { \mathrm { \bf j ~ } } & { \mathrm { \bf k } } \\ { x } & { y } & { z } \\ { ( \omega _ { y } z - \omega _ { z } y ) } & { ( \omega _ { z } x - \omega _ { x } z ) } & { ( \omega _ { x } y - \omega _ { y } x ) } \end{array} \right| d m } \\ { = \mathrm { i } [ \omega _ { x } ( y ^ { 2 } + z ^ { 2 } ) - \omega _ { y } ( x y ) - \omega _ { z } ( x z ) ] d m } \\ { + \mathrm { j } [ - \omega _ { x } ( x y ) + \omega _ { y } ( x ^ { 2 } + z ^ { 2 } ) - \omega _ { z } ( y z ) ] d m } \\ { + \mathrm { \bf ~ k } [ - \omega _ { x } ( x z ) - \omega _ { y } ( y z ) + \omega _ { z } ( x ^ { 2 } + y ^ { 2 } ) ] d m } & { ( \mathcal { S } . 2 } \end{array}
$$

which represent the moment about the $_ { x }$ ， y, z, axes of the momentum vectors shown in Fig. 5.2-1. Integrating over the body, we arrive at the x, y, z, components of the moment of momentum of the body.

$$
\mathbf { h } _ { 0 } = h _ { x } \mathbf { i } + h _ { y } \mathbf { j } + h _ { z } \mathbf { k }
$$

We now define the moment of inertia of the body about the $_ { x }$ y,z,axes S

$$
I _ { x } = \int ( y ^ { 2 } + z ^ { 2 } ) d m \quad I _ { y } = \int ( x ^ { 2 } + z ^ { 2 } ) d m \quad I _ { z } = \int ( x ^ { 2 } + y ^ { 2 } ) d m
$$

and the products of inertia as,

$$
I _ { x y } = \int x y d m \quad I _ { x z } = \int x z d m \quad I _ { y z } = \int y z d m
$$

in which case the moment of momentum components along the x, y, z, axes become,

$$
\begin{array} { r l } & { h _ { x } = I _ { x } \omega _ { x } - I _ { x y } \omega _ { y } - I _ { x z } \omega _ { z } } \\ & { h _ { y } = - I _ { x y } \omega _ { x } + I _ { y } \omega _ { y } - I _ { y z } \omega _ { z } } \\ & { h _ { z } = - I _ { x z } \omega _ { x } - I _ { y z } \omega _ { y } + I _ { z } \omega _ { z } } \end{array}
$$

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0002_pages_0071-0140/auto/images/b77adea2fc333b56a0cd2bf0e367e8af521c64fc3197664d0acbb03565f923b5.jpg)  
Fig. 5.2-l. Components of momentum (w X r) dm.

The moments and products of inertia can beconcisely presented by an inertia dyadic as follows:\*

$$
\mathcal { I } = \left| \begin{array} { r r r } { \mathbf { i } \mathbf { i } I _ { x } } & { - \mathbf { i j } I _ { x y } } & { - \mathbf { i k } I _ { x z } } \\ { - \mathbf { j i } I _ { x y } } & { \mathbf { j j } I _ { y } } & { - \mathbf { j k } I _ { y z } } \\ { - \mathbf { k i } I _ { x z } } & { - \mathbf { k j } I _ { y z } } & { \mathbf { k k } I _ { z } } \end{array} \right|
$$

If we form the dot product of the inertia dyadic with the angular velocity vector

$$
\mathbf { \omega } \omega = \omega _ { x } \mathbf { i } + \omega _ { y } \mathbf { j } + \omega _ { z } \mathbf { k }
$$

we would obtain the moment of momentum

$$
\mathbf { h } = \mathcal { F } \cdot \mathbf { \omega } \mathbf { \omega }
$$

The orderofthe dot product must bepreserved with thefollowing interpretation,

\* See Appendix B.

$$
{ \begin{array} { r c l } { \mathbf { i j } \cdot \mathbf { i } = \mathbf { i } ( \mathbf { j } \cdot \mathbf { i } ) = 0 } \\ { \mathbf { j i } \cdot \mathbf { i } = \mathbf { j } ( \mathbf { i } \cdot \mathbf { i } ) = \mathbf { j } } \end{array} }
$$

# 5.3 Kinetic Energy of a Rigid Body

Consider a rigid body moving through space, and attach to it a set of bodyaxesx,y,z,withitsoiginconciding withitscenterofasen any point r will have a velocity equal to,

$$
\mathbf { v } = \mathbf { v } _ { 0 } + \mathbf { \omega } \times \mathbf { r }
$$

The square of the velocity is obtained by the dot product of its vector,

$$
v ^ { 2 } = \mathbf { v } \cdot \mathbf { v } = v _ { 0 } ^ { ~ 2 } + ( \boldsymbol { \omega } \times \mathbf { r } ) \cdot ( \boldsymbol { \omega } \times \mathbf { r } ) + 2 \mathbf { v } _ { 0 } \cdot ( \boldsymbol { \omega } \times \mathbf { r } )
$$

Thus, the kinetic energy of the body is given as,

$$
\begin{array} { r } { r = \frac { 1 } { 2 } \int v ^ { 2 } d m = \frac { 1 } { 2 }  m v _ { 0 } { } ^ { 2 } + \frac { 1 } { 2 } \int ( \omega \times \mathbf { r } ) \cdot ( \omega \times \mathbf { r } ) d m + \mathbf { v } _ { 0 } \cdot \omega \times \int \mathbf { r } d m  } \\ {  \qquad = \frac { 1 } { 2 }  m v _ { 0 } { } ^ { 2 } + \frac { 1 } { 2 } \int ( \omega \times \mathbf { r } ) \cdot ( \omega \times \mathbf { r } ) d m  \qquad ( 5 . 3 - 2 ) \cdot \mathbf { r } e l l \cdot \mathbf { r }  } \end{array}
$$

where Sr $d m = 0$ for the origin of the body axes coinciding with thecenter of mass. We have thus found that the kinetic energy of translation is determined as if the entire mass is concentrated at the center of mass as a particle, and the second term is the kinetic energy of rotation about an axis ω through the center of mass.

Focusing our attention to the kinetic energy of rotation, we examine the quantity $( \omega \times \bf { \delta r } ) \cdot ( \omega \times \bf { \delta r } )$ . Resolving ω X r into components along the body axes, the dot product is given by the square of the i, j, k components.

$$
\begin{array} { r l } & { ( \omega \times \mathrm {  ~ r ~ } ) \cdot ( \omega \times \mathrm {  ~ r ~ } ) = ( \omega _ { y } z - \omega _ { z } y ) ^ { 2 } + ( \omega _ { z } x - \omega _ { x } z ) ^ { 2 } + ( \omega _ { x } y - \omega _ { y } x ) ^ { 2 } } \\ & { \qquad = \omega _ { \mathrm { { z } } } { } ^ { 2 } ( y ^ { 2 } + z ^ { 2 } ) + \omega _ { y } { } ^ { 2 } ( x ^ { 2 } + z ^ { 2 } ) + \omega _ { z } { } ^ { 2 } ( x ^ { 2 } + y ^ { 2 } ) } \\ & { \qquad - 2 \omega _ { x } \omega _ { z } x z - 2 \omega _ { y } \omega _ { z } y z - 2 \omega _ { x } \omega _ { y } x y } \end{array}
$$

Thus

$$
\begin{array} { r l } & { 2 T _ { \mathrm { r o t . } } = \omega _ { x } ^ { 2 } I _ { x } + \omega _ { y } ^ { 2 } I _ { y } + \omega _ { z } ^ { 2 } I _ { z } - 2 \omega _ { x } \omega _ { z } I _ { x z } - 2 \omega _ { y } \omega _ { z } I _ { y z } } \\ & { \qquad - \ 2 \omega _ { x } \omega _ { y } I _ { x y } } \end{array}
$$

# 5.4 Moment of Inertia about a Rotated Axis

If $I _ { \xi \xi }$ is the moment of inertia of a body about any axis $\xi$ , with angular velocity ω,we can write

$$
2 T _ { \mathrm { r o t . } } = I _ { \xi \xi } \omega ^ { 2 }
$$

Substituting Eq. 5.3-3 into the above equation, we have

$$
\begin{array} { r l } & { I _ { \xi \xi } = \left( \frac { \omega _ { x } } { \omega } \right) ^ { 2 } I _ { x } + \left( \frac { \omega _ { y } } { \omega } \right) ^ { 2 } I _ { y } + \left( \frac { \omega _ { z } } { \omega } \right) ^ { 2 } I _ { z } } \\ & { \phantom { I I } - 2 \left( \frac { \omega _ { x } } { \omega } \right) \left( \frac { \omega _ { z } } { \omega } \right) I _ { x z } - 2 \Big ( \frac { \omega _ { y } } { \omega } \Big ) \left( \frac { \omega _ { z } } { \omega } \right) I _ { y z } - 2 \Big ( \frac { \omega _ { x } } { \omega } \Big ) \left( \frac { \omega _ { y } } { \omega } \right) I _ { x y } } \end{array}
$$

By letting $l _ { \xi x }$ ， $l _ { \xi y }$ ， $l _ { \xi { z } }$ be direction cosines of the vector w or axis $\xi$ with respect to the $_ { x }$ ， $y$ ， $z$ axes, the above equation can be written as

$$
I _ { \xi \xi } = { l _ { \xi x } } ^ { 2 } I _ { x } , + { l _ { \xi y } } ^ { 2 } I _ { y } + { l _ { \xi z } } ^ { 2 } I _ { z } - 2 l _ { \xi x } l _ { \xi z } I _ { x z } - 2 l _ { \xi y } l _ { \xi z } I _ { y z } - 2 l _ { \xi x } l _ { \xi y } I _ { x y }
$$

Equation 5.4-3 can be concisely written in terms of a double summation as follows

$$
I _ { \xi \xi } = \sum _ { \alpha } \sum _ { \beta } l _ { \xi \alpha } l _ { \xi \beta } I _ { \alpha \beta }
$$

where $\propto$ and $\beta$ take on the letters $x$ ， $y , z$ with $I _ { x x }$ interpreted as $I _ { x x } = I _ { x } , I _ { y y } ,$ etc.,and $I _ { \alpha \beta }$ as $- I _ { x y } , - I _ { y z } , - I _ { x z }$ In fact Eq.5.4-4can bechanged slightly to apply to products of inertia as well by the equation

$$
- I _ { \xi \eta } = \sum _ { \alpha } \sum _ { \beta } l _ { \xi \alpha } l _ { \eta \beta } I _ { \alpha \beta }
$$

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0002_pages_0071-0140/auto/images/5c473864b97f713125536f9f71eca72a72c136d4ba57760bcd747658205f24a4.jpg)  
Fig. 5.4-l. Components of r in two coordinate systems.

The direction cosines l5x to be used in Eq. 5.4-4 or 5.4-5 can be formed most conveniently from the transformation matrix between the two coordinate systems. If the two coordinate systems are x, y, z and x', y', z' with unit vectors i, j, k and i’, j', k',a point in space can be expressed in terms of either coordinate system as

$$
\mathbf { r } = x \mathbf { i } + y \mathbf { j } + z \mathbf { k } = x ^ { \prime } \mathbf { i } ^ { \prime } + y ^ { \prime } \mathbf { j } ^ { \prime } + z ^ { \prime } \mathbf { k } ^ { \prime }
$$

as shown in Fig. 5.4-1.

Scalar multiplication of Eq. 5.4-6 by i, j, and k results in

$$
\begin{array} { r l } & { x = ( \mathbf { i } ^ { \prime } \cdot \mathbf { i } ) x ^ { \prime } + ( \mathbf { j } ^ { \prime } \cdot \mathbf { i } ) y ^ { \prime } + ( \mathbf { k } ^ { \prime } \cdot \mathbf { i } ) z ^ { \prime } } \\ & { y = ( \mathbf { i } ^ { \prime } \cdot \mathbf { j } ) x ^ { \prime } + ( \mathbf { j } ^ { \prime } \cdot \mathbf { j } ) y ^ { \prime } + ( \mathbf { k } ^ { \prime } \cdot \mathbf { j } ) z ^ { \prime } } \\ & { z = ( \mathbf { i } ^ { \prime } \cdot \mathbf { k } ) x ^ { \prime } + ( \mathbf { j } ^ { \prime } \cdot \mathbf { k } ) y ^ { \prime } + ( \mathbf { k } ^ { \prime } \cdot \mathbf { k } ) z ^ { \prime } } \end{array}
$$

which, in matrix notation, is

$$
{ \left[ \begin{array} { l } { x } \\ { y } \\ { y } \\ { z } \end{array} \right] } = { \left[ \begin{array} { l l l } { l _ { x x ^ { \prime } } } & { l _ { x y ^ { \prime } } } & { l _ { x z ^ { \prime } } } \\ { l _ { y x ^ { \prime } } } & { l _ { y y ^ { \prime } } } & { l _ { y z ^ { \prime } } } \\ { l _ { z x ^ { \prime } } } & { l _ { z y ^ { \prime } } } & { l _ { z z ^ { \prime } } } \end{array} \right] } { \left[ \begin{array} { l } { x ^ { \prime } } \\ { y ^ { \prime } } \\ { z ^ { \prime } } \end{array} \right] }
$$

Thus when the transfer matrix between the two coordinates is known, the elements of the matrix are the direction cosines.

We note further that the equation for the kineticenergy can beexpressed by the dot product of the angular velocity and the moment of momentum,

$$
2 T = \mathbf { \boldsymbol { \omega } } \cdot \mathbf { \boldsymbol { h } } _ { 0 }
$$

Since $\mathbf { h } _ { 0 }$ can be expressed in terms of the momental dyadic (see Eq.5.2-9), the above equation becomes

$$
2 T = \infty \cdot \mathcal { I } \cdot \omega
$$

Again letting ${ \mathcal { I } } = \mathbf { A B }$ , the above double dot product is interpreted as

$$
( { \bf \omega } \circ \cdot { \bf A } ) ( { \bf B } \cdot { \bf \omega } \omega )
$$

which is a product of two scalars and, therefore, a pure number.

# 5.5 Principal Axes

We define the principal axes of the body, 1, 2, 3, as those about which the products of inertia vanish, and let $A$ ， $B$ $C$ ,be the moment of inertia about the 1, 2, 3 axes respectively. The moment of inertia about the instantaneous axes of rotation $\xi ,$ in terms of $A$ ， $B$ ， $C$ then becomes,

$$
{ I _ { \xi } = A { l _ { \xi 1 } } ^ { 2 } + B { l _ { \xi 2 } } ^ { 2 } + C { l _ { \xi 3 } } ^ { 2 } }
$$

where lg1,ls2, l are the direction cosines of the vector $\boldsymbol { \omega }$ ,oraxis $\xi$ and the principal axes 1, 2,3. Since the axes 1,2, 3 are fixed in the body, $A$ ， $B$ ， $C$ are constants. However,as the instantaneous axis $\xi$ is moved, $l _ { \xi 1 }$ ， $l _ { \xi 2 }$ ， $l _ { \xi 3 }$ change, and so will the value of $\mathbf { \Omega } _ { \mathcal { L } }$ about the $\xi$ axis.

If we let $\rho = 1 / \sqrt { I _ { \xi } } ,$ and lay off $\boldsymbol { \rho }$ and $\xi$ ,and do this for every orientation of the instantaneous axis $\xi$ ， we would obtain an ellipsoid of inertia.

Dividing the above equation by $I _ { \xi }$ and noting that $l _ { \xi 1 } / \sqrt { I _ { \xi } } = l _ { \xi 1 } \rho = x$ l2p=y,lp =z are theprincipal coordinates of theequation for the ellipsoid of inertia,Eq.5.5-1 becomes

$$
A x ^ { 2 } + B y ^ { 2 } + C z ^ { 2 } = 1
$$

# PROBLEMS

1. For the slender uniform bar of length / and mass $m$ oriented in the position shown, determine the moment and product of inertia about each of the axes.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0002_pages_0071-0140/auto/images/bcfbd68fd8489a963a973d28f65b35301fb09f4ca1a8ab919913d0119e1ac74b.jpg)  
Prob.1

2. If the barof Prob.1isrotated about the $z$ axis with angular velocity $\omega$ ， determine the angular momentum about the three axes.

3. While getting into position for takeoff, a small aeroplane with two bladed propellers turns about its vertical axis as shown.Determine the x,y， z components of the angular momentum of the left propeller. Assume the propeller to be a uniform slender rod of length l.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0002_pages_0071-0140/auto/images/b827d08b72e53be6f88ddddcb5a20ecbfb0d275d5600c3cd79ca0646747088b0.jpg)  
Prob. 3

4. Find the moments of inertia of six 10-1b weights arranged symmetrically on the x, y, z axes as follows: $x = \pm 5 , y = \pm 2 , z = \pm \bar { 6 }$ 5.Find the moment of inertia of the configuration of Prob.4 about an axis through the origin and the point (1,2, 2).

6. A thin disk of radius R is mounted on a shaft which deviates by an angle α from the normal. Choose orthogonal axes through the shaft and disk and determine the moment and product of inertia about each axis.   
7. Determine the moment of inertia about the $\xi$ ， $\eta$ ， $\zeta$ axes for a cube of sides $c$ ， if $\zeta$ is placed along the diagonal and the $\xi$ $\eta$ axes normal to $\zeta$ are rotated into a position such that $I _ { \xi } = I _ { \eta }$ What will be the direction cosines of $\xi$ and $\eta$ so placed ?   
8. Determine the length of a uniform cylinder of radius R such that its principal moments of inertia are equal.   
9. If $A$ ， $_ B$ $C$ are principal moments of inertia of a given body, show that $A + B$ is larger than $C$   
10. A space vehicle makes a landing on a hillside with velocities $v _ { z }$ and $v _ { x }$ just before impact as shown. If a leg strikes a boulder and the vehicle pivots about this point, show that the angular velocities immediately after impact are

$$
\begin{array} { l } { { \dot { \theta } _ { x } = - \frac { m \bar { y } } { { I _ { x } } } v _ { z } } } \\ { { \dot { \theta } _ { y } = \frac { m \bar { y } { I _ { y z } } - m \bar { z } { I _ { z } } } { { I _ { y } I _ { z } } - { I _ { y z } } ^ { 2 } } v _ { x } } } \\ { { \dot { \theta } _ { z } = \frac { m \bar { y } } { { I _ { z } } } v _ { x } + \frac { { I _ { y z } } } { { I _ { z } } } \frac { m \bar { y } { I _ { y z } } - m \bar { z } { I _ { z } } } { { I _ { y } I _ { z } } - { I _ { y z } } ^ { 2 } } v _ { x } } } \end{array}
$$

where the $_ x$ y， $z$ coordinates are oriented with $z$ vertical, $x$ parallel to the horizontal velocity $v _ { x } ,$ and $y$ horizontal.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0002_pages_0071-0140/auto/images/99bc44e8e0ffa2f5523bfc8c95406cee5617ff37f49de427687ef8f20c64aa48.jpg)  
Prob.10

11. Assume that the moments and products of inertia about the x, y, z axes are known. Determine the equation for the inoment of inertia about the 5,n,5axes by noting that p²=p²-2 =p² -(p·i）,=i +/j +zk, and $\begin{array} { r } { I _ { \xi \xi } = \mathrm { ~ f ~ } \rho _ { \xi } ^ { 2 } \ d m , } \end{array}$ etc.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0002_pages_0071-0140/auto/images/a7affed094ca790ba54ff2b1e0db19f1412703235af813c4939d6ac497d6d3f2.jpg)  
Prob. Il

12. In the same manner as in Prob. 11, determine the equation for the product of inertia $I _ { \xi \eta } , I _ { \xi \zeta } ,$ and $I _ { \eta \zeta }$ 。

13. An airplane of mass $M$ and moments of inertia $A$ ， $B$ ， $C$ about principal axes drops at a uniform rate of $V$ ft/sec,and at the same time spins at the rate of $\mathrm { i 0 ~ \ r p m }$ about an axis which makes equal angles with the three principal axes.Determine its total kinetic energy.

14. Show that the moment of inertia of three equal masses $1 2 0 ^ { \circ }$ apart as shown in the sketch is equal to $\% m l ^ { 2 }$ about any axis in its plane.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0002_pages_0071-0140/auto/images/ec4305885404b96a2017f679a50e9d6d7fb2b7eb03a3ea23f6deea648cc90a60.jpg)  
Prob.14

15.With the $_ { x }$ ， $y$ , z axes passing through the center of massof a body shown in the sketch, prove that the moment of inertia about any axis n through the origin is

$$
\begin{array} { c } { { I _ { n } = \displaystyle \sum _ { i } m _ { i } [ x _ { i } { } ^ { 2 } ( 1 - n _ { x } ^ { 2 } ) + y _ { i } { } ^ { 2 } ( 1 - n _ { y } ^ { 2 } ) + z _ { i } { } ^ { 2 } ( 1 - n _ { z } ^ { 2 } ) } } \\ { { \nonumber } } \\ { { - \ 2 ( x _ { i } y _ { i } n _ { x } n _ { y } + x _ { i } z _ { i } n _ { x } n _ { z } + y _ { i } z _ { i } n _ { y } n _ { z } ) ] } } \end{array}
$$

where ${ \bf { n } } = n _ { x } { \bf { i } } + n _ { y } { \bf { j } } + n _ { z } { \bf { k } }$ is a unit vector along the axis $\mathbf { n }$ Hint: Start

$$
I _ { n } = \sum _ { i } m _ { i } ( \mathbf { r } _ { i } \times \mathbf { n } ) \cdot ( \mathbf { r } _ { i } \times \mathbf { n } ) = \sum _ { i } m _ { i } [ r _ { i } ^ { 2 } - ( \mathbf { r } _ { i } \cdot \mathbf { n } ) ^ { 2 } ]
$$

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0002_pages_0071-0140/auto/images/04f312fdde6b6343fa628a38fffaa4f6e17bcf30b21d2660aed2140384f7a2f0.jpg)  
Prob.15

16. Starting with $I _ { n ^ { \prime } } = \sum _ { i } m _ { i } [ ( \mathbf { r } _ { 0 } + \mathbf { r } _ { i } ) \times \mathbf { n } ] \cdot [ ( \mathbf { r } _ { 0 } + \mathbf { r } _ { i } ) \times \mathbf { n } ]$ derive the equation for the moment of inertia about an axis $n ^ { \prime }$ parallel to $n$ ， and displaced by the vector $\mathbf { r } _ { 0 }$

17. By actually multiplying, using the rule ij $\mathbf { \nabla } \cdot \mathbf { i } = 0$ ij $\begin{array} { r } { { \bf \nabla } \cdot \bf j = i , } \end{array}$ etc., show that $\boldsymbol { \mathsf { h } } = \mathcal { I } \cdot \boldsymbol { \mathsf { \omega } }$

18. Show that

$$
\dot { \boldsymbol { \mathcal { I } } } = [ \dot { \boldsymbol { \mathcal { I } } } ] + \omega \times \boldsymbol { \mathcal { I } } + \left| \begin{array} { c c } { \mathbf { i } \omega \times \mathbf { i } I _ { x } } & { - \mathbf { i } \omega \times \mathbf { j } I _ { x y } - \mathbf { i } \omega \times \mathbf { k } I _ { x y } } \\ { - \mathbf { j } \omega \times \mathbf { i } I _ { x y } } & { \mathbf { j } \omega \times \mathbf { j } I _ { y } } & { - \mathbf { j } \omega \times \mathbf { k } I _ { y z } } \end{array} \right|
$$

where

$$
[ \dot { \mathcal { I } } ] = \left| \begin{array} { c c c } { \mathfrak { i } \dot { \mathfrak { i } } I _ { x } } & { - \mathfrak { i } \dot { \mathfrak { j } } I _ { x y } } & { - \mathfrak { i } \mathbf { k } I _ { x z } } \\ { - \mathfrak { j } \mathfrak { i } I _ { x y } } & { \mathfrak { j } \dot { \mathfrak { j } } I _ { y } } & { - \mathfrak { j } \mathbf { k } \dot { I } _ { y z } } \\ { - \mathbf { k } \mathfrak { i } \dot { I } _ { x z } } & { - \mathbf { k } \mathfrak { j } I _ { y z } } & { \mathbf { k } \mathbf { k } \dot { I } _ { z } } \end{array} \right|
$$

19.Determine the total time derivative

$$
\frac { d \mathbf { h } } { d t } = \boldsymbol { \mathcal { S } } \cdot \dot { \boldsymbol { \omega } } + \dot { \boldsymbol { \mathcal { S } } } \cdot \boldsymbol { \omega }
$$

with respect to inertial coordinates,and show that it is equal to

$$
\frac { d \mathbf { h } } { d t } = \mathcal { I } \cdot \dot { \boldsymbol { \omega } } + [ \dot { \mathcal { I } } ] \cdot \boldsymbol { \omega } + \boldsymbol { \omega } \times \mathbf { h }
$$

# 5.6 Euler's Moment Equation

We have shown previously that the moment about the mass center is equal to the time derivative of the moment of momentum about this point. With $\mathbf h _ { c } = h _ { x } \mathbf i + h _ { y } \mathbf j + h _ { z } \mathbf k$ ，we can differentiate, noting that i, j,k rotate with the body.

$$
\begin{array} { r l } & { \mathbf { M } _ { c } = [ \dot { \mathbf { h } } _ { c } ] + \boldsymbol { \omega } \times \mathbf { h } _ { c } } \\ & { \qquad = ( \dot { h } _ { c a } \dot { \mathbf { i } } + h _ { v } \mathbf { j } + h _ { z } \mathbf { k } ) + \boldsymbol { \omega } \times \mathbf { h } _ { c } } \end{array}
$$

The cross product ω X h can easily be visualized as the rotation of the vectors hi, hj, hk,due to ωx, W, ω,as shown in Fig. 5.6-1. Thus,by adding vectors along the x,y,z directions,the above equation becomes,

$$
\begin{array} { c } { { { \bf M } _ { o } = M _ { x } { \bf i } + M _ { v } { \bf j } + M _ { z } { \bf k } } } \\ { { { \mathrm { } } } } \\ { { = ( h _ { x } + \omega _ { y } h _ { z } - \omega _ { z } h _ { y } ) { \bf i } + ( h _ { y } + \omega _ { z } h _ { x } - \omega _ { x } h _ { z } ) { \bf j } + ( h _ { z } + \omega _ { x } h _ { y } - \omega _ { y } { \bf k } ) } } \end{array}
$$

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0002_pages_0071-0140/auto/images/f58faf695f9226c62f6b5d843b1c88d8393dea8a7a76228116a61eacff9f28a9.jpg)  
Fig. 5.6-l. Components of moment of momentum and their rate of change.

The component equations,known as Euler's moment equations,are

$$
\begin{array} { r } { M _ { x } = h _ { x } + \omega _ { y } h _ { z } - \omega _ { z } h _ { y } } \\ { M _ { y } = h _ { y } + \omega _ { z } h _ { x } - \omega _ { x } h _ { z } } \\ { M _ { z } = h _ { z } + \omega _ { x } h _ { y } - \omega _ { y } h _ { x } } \end{array}
$$

where the $_ x$ y, $z$ axes with the origin coinciding with the center of mass rotate with angular velocity $\boldsymbol { \omega }$

Equation $5 . 6 \AA - 1$ or 5.6-3 for the moment is applicable to any coordinate system with a fixed origin or a moving origin coinciding with the center of mass. The angular velocity $\boldsymbol { \omega }$ is that of the coordinate stemand the axes are fixed in the body, the moments and products of inertia are constant.

For a body of revolution with moments of inertia $A$ ， $A$ ， $C$ about principal axes, $A$ about any transverse axis is the same, and so we might choose a set of transverse axes rotating at a speed different from that of the body without introducing a variable moment of inertia with time. We can for instance use the node axis system 5, n, &,in which case the moments are,

$$
\begin{array} { r } { M _ { \xi } = h _ { \xi } + h _ { \zeta } \omega _ { \eta } - h _ { \eta } \omega _ { \xi } } \\ { M _ { \eta } = h _ { \eta } + h _ { \xi } \omega _ { \zeta } - h _ { \zeta } \omega _ { \xi } } \\ { M _ { \zeta } = h _ { \zeta } + h _ { \eta } \omega _ { \xi } - h _ { \xi } \omega _ { \eta } } \end{array}
$$

These equations are known as Euler's modified equations.

# 5.7 Euler’s Equation for Principal Axes

With the origin of the body axes coinciding with the center of mass, we can orient the $_ x$ ， $y$ ， $z$ axes to coincide with the principal axes 1,2,3 of the body to eliminate the products of inertia terms in the moment of momentum expressions. We then have,

$$
h _ { 1 } = A \omega _ { 1 } \qquad h _ { 2 } = B \omega _ { 2 } \qquad h _ { 3 } = C \omega _ { 3 }
$$

where $A , B , C ,$ , are principal moments of inertia which are constant since 1,2, 3 are fixed in the body. The moment equations are then,

$$
\begin{array} { r } { M _ { 1 } = A \dot { \omega } _ { 1 } + \omega _ { 2 } \omega _ { 3 } ( C - B ) } \\ { M _ { 2 } = B \dot { \omega } _ { 2 } + \omega _ { 1 } \omega _ { 3 } ( A - C ) } \\ { M _ { 3 } = C \dot { \omega } _ { 3 } + \omega _ { 1 } \omega _ { 2 } ( B - A ) } \end{array}
$$

which are called the Euler's equations for principal axes. The general solution of these equations is diffcult, and in the sections to follow we will consider some special cases which enable an analytical solution.

# 5.8 Body with $A \ = \ B$ and Zero External Moment (Body Coordinates)

We will consider here a cylindrical disk with axis 3 normal to the circular face, as shown in Fig. 5.8-1.

The moment of inertia about the three body axes are,

Euler's equation then becomes,

$$
\begin{array} { r } { A \dot { \omega } _ { 1 } + ( C - A ) \omega _ { 2 } \omega _ { 3 } = 0 } \\ { A \dot { \omega } _ { 2 } - ( C - A ) \omega _ { 1 } \omega _ { 3 } = 0 } \\ { C \dot { \omega } _ { 3 } = 0 } \end{array}
$$

From the third of these equations, we conclude that $\omega _ { 3 }$ must be a constant.

$$
\omega _ { 3 } = n
$$

Making the substitution,

$$
n \left( { \frac { C - A } { A } } \right) = \lambda
$$

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0002_pages_0071-0140/auto/images/8216a55ac69ab918bd7be64b132f812971a67df27095a994133a0b5420d98d79.jpg)  
Fig. 5.8-l. Body of revolution with principal axes 1, 2, 3.

the first two equations can be written as,

$$
\begin{array} { r l r } { \dot { \omega } _ { 1 } + \lambda \omega _ { 2 } = 0 } & { { } } & { } \\ { \dot { \omega } _ { 2 } - \lambda \omega _ { 1 } = 0 } \end{array}
$$

Multiplying the first equation by $\omega _ { 1 }$ and the second by ${ \boldsymbol { \omega } } _ { 2 }$ ,and adding, we obtain the equation,

or

$$
\begin{array} { r l } { { \omega _ { 1 } \dot { \omega } _ { 1 } + \omega _ { 2 } \dot { \omega } _ { 2 } = 0 } } & { { } } \\ { { } } & { { } } \\ { { \omega _ { 1 } { } ^ { 2 } + \omega _ { 2 } { } ^ { 2 } = { \omega _ { 1 2 } } ^ { 2 } = \mathrm { c o n s t a n t } } } \end{array}
$$

Thus the magnitude of the resultant angular velocity vector w is a constant.

$$
\omega = \sqrt { { \omega _ { 1 } } ^ { 2 } + { \omega _ { 2 } } ^ { 2 } + { \omega _ { 3 } } ^ { 2 } } = \sqrt { { \omega _ { 1 2 } } ^ { 2 } + n ^ { 2 } } = \mathrm { c o n s t a n t }
$$

Since there is no moment acting on the body, we have,

$$
\mathbf { M } = \dot { \mathbf { h } } = 0
$$

which requires that the angular momentum vector h be a constant, fixed in


<!-- chunk 0003: pages 141-210 -->
space. It is evident that h must lie in the plane containing axis 3 and w, since the component ofhin the1,-plane is

$$
A ( \omega _ { 1 } \mathbf { i } + \omega _ { 2 } \mathbf { j } ) = A \omega _ { 1 2 } \mathbf { 1 } _ { 1 2 }
$$

which has the same direction as the component of ω in the 1,2-plane. Thus,the plane containing axis 3 and the $\boldsymbol { \omega }$ vector rotates about thefixed h vector,as shown in Fig.5.8-2. The motion can be visualized by the rollng of the body cone on the space cone, which is fixed in space by the vector h.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0003_pages_0141-0210/auto/images/f93a9f899cc74c1b38601e14ac354bdebb8f21d281cf9483abebb7a6fc00f529.jpg)  
Fig. 5.8-2. Body cone rolls on space cone.

The speed of rotation of the plane containing ω and axis 3 about the line h can be found as follows. Differentiating the first of Eq. 5.8-4, and substituting from the second, we have,

$$
\ddot { \omega } _ { 1 } + \lambda ^ { 2 } \omega _ { 1 } = 0
$$

Letting ω1(O) and ω1(O) be the initial conditions at t = 0, the solution of this equation is,

$$
\omega _ { 1 } = \omega _ { 1 } ( 0 ) \cos \lambda t + { \frac { { \dot { \omega } } _ { 1 } ( 0 ) } { \lambda } } \sin \lambda t
$$

Also, from this set of equations,

$$
\omega _ { 2 } = - \frac { \dot { \omega } _ { 1 } } { \lambda } = \omega _ { 1 } ( 0 ) \sin \lambda t - \frac { \dot { \omega } _ { 1 } ( 0 ) } { \lambda } \cos \lambda t
$$

From the last equation we obtain for $t = 0$ ，

$$
\omega _ { 2 } ( 0 ) = - \frac { \dot { \omega } _ { 1 } ( 0 ) } { \lambda }
$$

We note further that

$$
\omega _ { 1 2 } = \omega _ { 1 } + i \omega _ { 2 }
$$

where $i = \sqrt { - 1 }$ so that, another form of the solution is obtained by adding $\omega _ { 1 }$ and $\omega _ { 2 }$ in quadrature

$$
\begin{array} { l } { { \omega _ { 1 2 } = \Big [ \omega _ { 1 } ( 0 ) - i \frac { \dot { \omega } _ { 1 } ( 0 ) } { \lambda } \Big ] ( \cos \lambda t + i \sin \lambda t ) } } \\ { { \qquad = [ \omega _ { 1 } ( 0 ) + i \omega _ { 2 } ( 0 ) ] e ^ { i \lambda t } } } \\ { { \qquad = \omega _ { 1 2 } ( 0 ) e ^ { i \lambda t } } } \end{array}
$$

These equations all indicate that the vector $\omega _ { 1 2 } = \sqrt { \omega _ { 1 } { ^ 2 } + \omega _ { 2 } { ^ 2 } }$ in the 1,2-plane, rotates at a speed equal to $\lambda$ rad/sec, with respect to the rotating body axes 1,2, 3. λ is then the angular velocity of the w vector as viewed by an observer stationed on the body at the axis of symmetry.

The angle $\theta$ between h and axis 3 is,

$$
\tan \theta = \frac { A \omega _ { 1 2 } } { C n }
$$

The angle $\gamma$ between ω and axis 3 is,

$$
\tan \gamma = { \frac { \omega _ { 1 2 } } { n } }
$$

By comparison we have,

$$
\tan \theta = { \frac { A } { C } } \tan \gamma
$$

If $C > A$ ,then $\gamma$ will be greater than $\theta$ ,as shown in Fig. 5.8-2, and h will lie between axis 3 and $\pmb { \omega }$ .If $C < A .$ $\gamma$ will be smaller than θ and ω will lie between h and axis 3.

The equations derived in this section all refer to the body axes which are in motion with the body. They do not tell us how the body moves in space. However, the following conclusions were obtained.

1. The vectors w, h, and axis 3 lie in the same plane. 2. In the plane of $\boldsymbol { \mathfrak { \omega } }$ , h and axis 3, the angle $\theta$ between O3 and h is constant. 3. The angle y between O3 and ω is constant. 4. The vector h is constant or fixed in direction and magnitude. 5.Thevectorasostantmagitude $\sqrt { \omega _ { 1 2 } } ^ { 2 } + n ^ { 2 }$ 6. The plane containing the three vectors rotates relative to the body axes at an angular speed $\lambda$

# 5.9 Body of Revolution with Zero Moment, in Terms of Euler's Angles

We will consider the previous problem of Section 5.8, by introducing the Euler angles γ, 0, 𝜑, in order to establish the motion with respect to fixed axes. Since h is fixed in space, we will orient it along the OZ axis,in which case φ becomes the angular velocity of the node line and the spin axis about the OZ direction. We also hadθ = O from the previous section, so that Eq. 3.5-1 becomes,

$$
\begin{array} { r l } & { \omega _ { 1 } = \dot { \psi } \sin \theta \sin \varphi } \\ & { \omega _ { 2 } = \dot { \psi } \sin \theta \cos \varphi } \\ & { \omega _ { 3 } = \dot { \varphi } + \dot { \psi } \cos \theta = n } \end{array}
$$

Differentiating with $\dot { \theta } = 0$ , the angular accelerations are,

$$
\begin{array} { r l } & { \dot { \omega } _ { 1 } = \dot { \psi } \dot { \varphi } \sin \theta \cos \varphi } \\ & { \dot { \omega } _ { 2 } = - \dot { \psi } \dot { \varphi } \sin \theta \sin \varphi } \\ & { \dot { \omega } _ { 3 } = 0 } \end{array}
$$

Substituting into the first of Eq. 5.8-1, we obtain,

Aj sin $\theta$ cos $\varphi + \mathrm { ( } \dot { \varphi } \dot { \psi }$ sin $\theta$ cos $\varphi + \dot { \psi } ^ { 2 }$ sin 0 cos 0 cos 𝜑)(C - A) = 0

Thus, the precession velocity in terms of the spin velocity ${ \dot { \varphi } } , C , A$ ,and $\theta$ becomes,

$$
{ \dot { \psi } } = { \frac { C { \dot { \varphi } } } { ( A - C ) \cos \theta } }
$$

Equation 5.9-4 states that the roll axis (also plane containing $\boldsymbol { z }$ and ω) rotates about a fixed $O Z$ or h axis with a speed of $\dot { \psi }$ proportional to the angular velocity of spin $\dot { \varphi }$ .If $C > A$ , the spin must be negative, since $\dot { \psi }$ was drawn in the positive direction. Thus if $C > A$ , the spin is opposite in sense to the precession,and we call the case retrograde precession. If $C < A$ ,then $\dot { \varphi }$ and $\dot { \psi }$ have the same sense, and we have direct precession. Thus a flat disk spinning about an axis perpendicular to its plane will have retrograde precession, whereas a slender rod spinning about its longitudinal axis will have direct precession. The space and body cones for the two cases are shown in Figs. 5.9-1 and 5.9-2. It should be noted also that, when $C > A$ ，

$$
\left| { \frac { C } { ( A - C ) \cos \theta } } \right| > 1
$$

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0003_pages_0141-0210/auto/images/59327e2cefbdc39edd5feb8fbce20da0399a803c915a11e993772c140d7ce48f.jpg)  
Fig.5.9-l. Retrograde precession $C > A$

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0003_pages_0141-0210/auto/images/eb0f03c30c248ac651535b3898c38079a7d11b4a072cdbbc4d0fcc2f62e51da0.jpg)  
Fig. 5.9-2. Direct precession $C < A$

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0003_pages_0141-0210/auto/images/8fbf4682e859102a571ec547dbf276e61a33ff2c14e5fa3c3126eeed4f6274f0.jpg)  
Fig. 5.9-3. For steady precession w is the vector sum of $\dot { \psi }$ and $\dot { \varphi }$ ·

Therefore,

$$
\dot { \psi } > \dot { \varphi }
$$

As $\theta \to 9 0 ^ { \circ }$ ， $\dot { \psi }$ becomes very large compared to $\dot { \varphi }$ Since $\dot { \theta } = 0$ ，the resultant angular velocity $\boldsymbol { \omega }$ is the vector sum of $\dot { \psi }$ and $\dot { \varphi }$ ,as shown in Fig. 5.9-3.

# PROBLEMS

1. Show that a thin disk thrown spinning with its plane nearly parallel will make two wobbles to every cycle of spin.   
2. A thin disk thrown into the air is seen to wobble so that its normal generates a cone of $2 0 ^ { \circ }$ twice per second. Determine the rate of spin and the total angular velocity vector with respect to the inertial coordinates.   
3. A thin disk is spun about an axis making an angle $\gamma$ with the normal to the disk and then released. Assuming the disk to be moment free, find the half-angle of the cone generated by the disk normal, and the time required for one complete rotation of the normal around the cone. Is the precession direct or retrograde?   
4. A cylindrical disk has a thickness equal to $R / 2$ where $R$ is the radius. If it is spinning and precessing with its normal generating a cone angle of $1 5 ^ { \circ }$ with a fixed direction in space, determine the cone angle in space generated by the angular velocity vector. If the magnitude of $\omega$ is $1 0 \pi$ rad/sec, determine its component $\omega _ { \tt I 2 }$ in the plane of the disk.   
5.In Prob. 2, determine the equations for the angular velocities about the body axes 1,2, 3,where 1 and 2 are in the plane of the disk and 3 is normal to it.   
6. In Prob. 2, determine the equations for the angular acceleration about the axes 1, 2, and 3.   
7. Letting $m$ be the mass of the disk of Prob. 4, write the equations for the vectors ω and h,and determine the kinetic energy of rotation.   
8. A uniform disk of radius $R$ and mass $m$ is mounted through its center to a shaft so that its normal makes an angle $\propto$ with the shaft. If the shaft rotates at speed ω between bearings a distance $l$ apart, determine the bearing reactions.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0003_pages_0141-0210/auto/images/7596eb8fa663a85802640fb62180a8c3d5f93b35761fb393441236ce36af1da4.jpg)  
Prob.8

9.A thin rectangular plate of sides $^ a$ and $b$ is mounted on a shaft in the plane of the plate through its center. The shaft makes an angle $\propto$ with the long side $b$ . Determine the bearing reactions when the shaft rotates at speed ω. The distance between bearings is $l ,$

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0003_pages_0141-0210/auto/images/4357a90adc55e4fd161b1e5b72ad18ba1458b27e0913b732a21c695d500bce20.jpg)  
Prob.9

10. Let $_ x$ ，y, $z$ be the principal axes through the center of gravity of an airplane, with $A$ ， $B$ $\mathbf { C }$ as principal moments of inertia. Show that in order for the airplane to make a turn of radius $R$ about a vertical line, with speed $V ,$ it must bank at an angle $\theta = \tan ^ { - 1 } { V ^ { 2 } / R g }$ and supply a rolling moment in the same direction as $\theta$ ,equal to

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0003_pages_0141-0210/auto/images/b1afa920ee3fa0257f901170e25fa69c3dff30fed2e7b989887d016e300c0342.jpg)  
Prob.10

11. Determine the gyroscopic moment necessary for the airplane of Prob. 10 to spin with speed $\dot { \psi }$ about the vertical $O Z$ axis, when the nose of the air-plane is inclined at an angle $\propto$ below the horizontal.   
12. If the spin $\dot { \psi }$ takes place about an axis through the center of gravity making angles $\propto$ ， $\beta$ ,y, with respect to the $x$ , y, z axes of the airplane,write the diferential equations for the moments $M _ { x }$ $M _ { y s }$ and $M _ { z }$ ·   
13. A slender rod of mass $m$ and length $l$ is welded to a shaft at its $\%$ point at an angle 0. Determine the bearing reactions when the shaft rotates with speed $\omega _ { s }$ and the distance between bearings is $_ { 2 c }$

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0003_pages_0141-0210/auto/images/1c21c2162e0948e3cc5698462ce6a0aaea801f8713be5ebfd637e19869bc9839.jpg)  
Prob.13

14. A missile with $C / A = \text{‰}$ is spinning at speed $n = 1 0 \pi$ rad/sec and precess-ing at an angle $\theta \ : = \ : 5 ^ { \circ }$ witha fixed direction in space.Determinethe precession speed $\dot { \psi }$ and the angle between the resultant angular velocity vector and the longitudinal axis. Draw the body and space cones. What can you conclude regarding the precessional speed of slender bodies ?

# 5.10 Unsymmetrical Body with Zero External Moment (Poinsot's Geometric Solution)

In the general case ofa body without an axis of revolution,the principal moments of inertia are unequal, so that Euler's equations for no external torque become,

$$
\begin{array} { r } { A \dot { \omega } _ { 1 } + ( C - B ) \omega _ { 2 } \omega _ { 3 } = 0 } \\ { B \dot { \omega } _ { 2 } + ( A - C ) \omega _ { 1 } \omega _ { 3 } = 0 } \\ { C \dot { \omega } _ { 3 } + ( B - A ) \omega _ { 1 } \omega _ { 2 } = 0 } \end{array}
$$

where 1,2,3 are body-fixed axes coinciding with the principal axis. The solution of these equations involve elliptic functions,and is taken up in Sec. 5.11. The following is a geometric discussion of the solution due to Poinsot.

With no external torque, the kinetic energy and the moment of momentum about the center of mass $C$ are constants.

$$
\mathbf { h } = { \mathrm { c o n s t a n t } }
$$

No work is done on the body, therefore,

$$
T = { \tt c o n s t a n t }
$$

The expression for w and h are,

$$
\begin{array} { l } { \omega = \omega _ { 1 } \mathbf { i } + \omega _ { 2 } \mathbf { j } + \omega _ { 3 } \mathbf { k } } \\ { \qquad } \\ { \mathbf { h } = A \omega _ { 1 } \mathbf { i } + B \omega _ { 2 } \mathbf { j } + C \omega _ { 3 } \mathbf { k } } \end{array}
$$

from which we obtain,

$$
\omega \cdot \mathbf { h } = A \omega _ { 1 } ^ { 2 } + B \omega _ { 2 } ^ { 2 } + C \omega _ { 3 } ^ { 2 } = 2 T = \mathrm { c o n s t a n t }
$$

$$
h ^ { 2 } = A ^ { 2 } { \omega _ { 1 } } ^ { 2 } + B ^ { 2 } { \omega _ { 2 } } ^ { 2 } + C ^ { 2 } { \omega _ { 3 } } ^ { 2 } = \mathrm { c o n s t a n t }
$$

With h drawn in a specified direction, its unit vector is $\mathbf { h } / h$ ,and the component of $\boldsymbol { \mathfrak { o } }$ along h will be given by

$$
O N = \omega \cdot { \frac { \mathbf { h } } { \mathit { h } } } = { \frac { 2 T } { \mathit { h } } } = { \mathrm { c o n s t a n t } }
$$

Thus $N$ is a fixed point along the direction of h,as shown in Fig. 5.10-1, and the end of the ω vector must lie in a plane through $N$ perpendicular to ON. The line $O N$ is referred to as the invariable line,and the perpendicular plane the invariable plane. Thus the end of the vector w must move in this invariable plane.

Letting the coordinates of $\omega$ be $\xi ^ { \prime }$ ， $\eta ^ { \prime }$ ， $\zeta ^ { \prime }$ ,we have $\omega _ { 1 } = \xi ^ { \prime }$ ， $\omega _ { 2 } = \eta ^ { \prime }$ ,and $\omega _ { 3 } = \zeta ^ { \prime }$ . The equation for $2 T$ may then be writen as

$$
\frac { \xi ^ { \prime 2 } } { ( \sqrt { 2 T / A } ) ^ { 2 } } + \frac { \eta ^ { \prime 2 } } { ( \sqrt { 2 T / B } ) ^ { 2 } } + \frac { \zeta ^ { \prime 2 } } { ( \sqrt { 2 T / C } ) ^ { 2 } } = 1
$$

which is called the Poinsot ellipsoid. Figure 5.10-2 is an illustration of the ellipsoid.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0003_pages_0141-0210/auto/images/807737925d8b0cd18716608fb63c527ba27d806e8314320e9dd6ebcfb6b2f2e1.jpg)  
Fig. 5.l0-l. Invariable line $O N$ and invariable plane $s$

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0003_pages_0141-0210/auto/images/9b1650d5f961dfac3f4679b346c7b35ddaeb5bf9effa12abb7861ee881f6573d.jpg)  
Fig. 5.10-2. Poinsot ellipsoid.

We next examine the inertia ellipsoid which was previously described as thelocusof p =1/√I laidoffalong thew vector. Letingthecoordinates of $\rho$ be $\xi$ ， $\eta$ ， $\zeta$ ,theeqatielrE.

$$
\frac { \xi ^ { 2 } } { ( \sqrt { 1 / A } ) ^ { 2 } } + \frac { \eta ^ { 2 } } { ( \sqrt { 1 / B } ) ^ { 2 } } + \frac { \zeta ^ { 2 } } { ( \sqrt { 1 / C } ) ^ { 2 } } = 1
$$

# GYRODYNAMICS

We thus see that the Poinsot ellipsoid is proportional to the inertia ellpsoid with its coordinates equal to√2T times the coordinates of the inertia ellipsoid.

The Poinsot ellipsoid can be shown to roll on the invariable plane with its center a distance $O N = 2 T / h$ from it. Starting with the equation,

$$
2 T = \mathbf { \omega } _ { \mathbf { { u } } } \cdot \mathbf { \mathbf { h } }
$$

and remembering that h and T are constant, we can obtain the following differential relationship.

$$
d ( 2 T ) = d { \pmb { \omega } } \cdot { \bf h } = 0
$$

Since the vanishing of the dot product of two vectors $d \omega$ and h requires that the cosine of the angle between them be zero, we conclude that dw and h are perpendicular to each other. With the end point of w moving in the invariable plane, any change dw of $\mathbf { \omega } _ { \omega }$ is perpendicular to h,and since the locus ofw $( \xi ^ { \prime } , \eta ^ { \prime } , \zeta ^ { \prime } )$ corresponds to the Poinsot ellipsoid,it must be tangent to the invariable plane. Thus to an observer stationed to a fixed coordinate system, the motion of the body is described by the rolling of the Poinsot ellipsoid (or inertia ellipsoid with $\xi$ $\eta$ ， $\zeta$ coordinates increased by $\sqrt { 2 T } )$ on the invariable plane.

If we wish to examine the motion from the point of view of an observer stationed on the moving body, the invariable plane will now appear to move with respect to the body. From the angular momentum equation, Eq. 5.10-7, we can rearrange the terms to form the angular momentum ellipsoid as follows.

$$
\frac { \xi ^ { \prime 2 } } { ( h / A ) ^ { 2 } } + \frac { \eta ^ { \prime 2 } } { ( h / B ) ^ { 2 } } + \frac { \zeta ^ { \prime 2 } } { ( h / C ) ^ { 2 } } = 1
$$

The curve traced by the end of the ω vector is then defined by the intersection of the Poinsot, ellipsoid Eq. 5.10-9, and the angular momentum Eq. 5.10-13, ellipsoid.

The instantaneous axis ω passes through the point of contact between the Poinsot ellipsoid and the invariable plane. It therefore generates simultaneously two cones, one in the fixed space,and the other in the body or the Poinsot ellipsoid. These cones， called the herpolhode and the polhode cones respectively, are shown in Fig. 5.10-3.

Since ω is common to both the Poinsot ellipsoid and the momentum ellipsoid, the equation for the body cone can be obtained by subtracting Eq. 5.10-9 from 5.10-13 and multiplying by $h ^ { 2 } ,$

$$
A \left( A - { \frac { h ^ { 2 } } { 2 T } } \right) \xi ^ { \prime 2 } + B \left( B - { \frac { h ^ { 2 } } { 2 T } } \right) \eta ^ { \prime 2 } + C \left( C - { \frac { h ^ { 2 } } { 2 T } } \right) \zeta ^ { \prime 2 } = 0
$$

This equation indicates that for the body cone to be real, h2/2T must lie between the greatest and least values of A, B,and C. For instance, if we let $A > B > C ,$ then $h ^ { 2 } / 2 T$ must satisfy the relation,

$$
A \geq { \frac { h ^ { 2 } } { 2 T } } \geq C
$$

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0003_pages_0141-0210/auto/images/59cdae4cb9f8af874a25a86fb32c2c2365874325e3480605df475a144c731d77.jpg)  
Fig. 5.10-3. Poinsot ellipsoid rols on the invariable plane s.

To find the polhode curves, we let the Poinsot elipsoid intersect the polhode cone. The form of these curves is best visualized by looking at their principal plane projections, obtained by eliminating in turn one of the coordinates between Eqs.5.10-14 and 5.10-9. The three equations so obtained are,

$$
\begin{array} { r l r } & { } & { A ( A - C ) \xi ^ { \prime 2 } + B ( B - C ) \eta ^ { \prime 2 } = 2 T \Big ( \frac { h ^ { 2 } } { 2 T } - C \Big ) } \\ & { } & \\ & { } & { A ( A - B ) \xi ^ { \prime 2 } - C ( B - C ) \zeta ^ { \prime 2 } = 2 T \Big ( \frac { h ^ { 2 } } { 2 T } - B \Big ) } \\ & { } & \\ & { } & { B ( A - B ) \eta ^ { \prime 2 } + C ( A - C ) \zeta ^ { \prime 2 } = 2 T \Big ( A - \frac { h ^ { 2 } } { 2 T } \Big ) } \end{array}
$$

If $h ^ { 2 } / 2 T = C$ , the first equation can be satisfied for $\xi ^ { \prime } = \eta ^ { \prime } = 0$ .The polhode curve then degenerates to a point on the $\zeta ^ { \prime }$ axis.

If $h ^ { 2 } / 2 T = B$ ,we obtain from the second of the three equations

$$
{ \frac { \zeta ^ { \prime } } { \xi ^ { \prime } } } = \sqrt { \frac { A ( A - B ) } { C ( B - C ) } }
$$

whichindicatestwoplanespasingthrough $\eta ^ { \prime }$ axis. The $\xi ^ { \prime } \eta ^ { \prime }$ and the $\eta ^ { \prime } \zeta ^ { \prime }$ projections from the other two equations,are elipses.

If h2/2T = A,the third of the three equations can only be satisfied if $\eta ^ { \prime } = \zeta ^ { \prime } = 0$ ,andthe polhodecurvedegenerates toapoint onthe $\xi ^ { \prime }$ axis. If h²/2T lies between B and C, the polhodes lie between the planes of Eq. 5.10-16 and the $\zeta ^ { \prime }$ axis.Their $\xi ^ { \prime } \eta ^ { \prime }$ projections are ellipses.

If $h ^ { 2 } / 2 T$ lies between $A$ and $B$ , the polhodes lie in the central part of the ellipsoid between the planes of Eq.5.10-16.Their $\eta ^ { \prime } \zeta ^ { \prime }$ projections are ellipses and their $\xi ^ { \prime } \zeta ^ { \prime }$ projections are hyperbolas. The general nature of the polhode curve for the various cases are shown in Fig. 5.10-4.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0003_pages_0141-0210/auto/images/de3910739837fb0d6424556bba728de9f1cabf118934c2c92ab457316e35ab37.jpg)  
Fig. 5.10-4. Polhode curves.

If we write Eqs. 5.10-6 and 5.10-7 in terms of momentum components, $h _ { 1 } ,$ ${ \bf \Phi } _ { 1 } , h _ { 2 } , h _ { 3 } ,$ they become

$$
\begin{array} { c } { { \frac { { h _ { 1 } } ^ { 2 } } { A } + \frac { { h _ { 2 } } ^ { 2 } } { B } + \frac { { h _ { 3 } } ^ { 2 } } { C } = 2 T } } \\ { { \mathrm { } } } \\ { { { h _ { 1 } } ^ { 2 } + { h _ { 2 } } ^ { 2 } + { h _ { 3 } } ^ { 2 } = h ^ { 2 } } } \end{array}
$$

and their simultaneous solution give the intersection of the Poinsot ellipsoid, Eq. 5.10-17, and the momentum sphere, Eq. 5.10-18, in terms of the momentum coordinates. Since Eqs. 5.10-14 and 5.10-15 are also solutions to the same problem, we need only to rewrite these equations in terms of h1, h2,and hg. Thus Eq. 5.10-14 rewritten in terms of momentum coordinates is

$$
\left( 1 - \frac { 1 } { A } \frac { h ^ { 2 } } { 2 T } \right) { h _ { 1 } } ^ { 2 } + \left( 1 - \frac { 1 } { B } \frac { h ^ { 2 } } { 2 T } \right) { h _ { 2 } } ^ { 2 } + \left( 1 - \frac { 1 } { C } \frac { h ^ { 2 } } { 2 T } \right) { h _ { 3 } } ^ { 2 } = 0
$$

Figure 5.10-5 is a plot of Eq. 5.10-19 showing the locus of the h vector on the momentum sphere for various values of $h ^ { 2 } / 2 T$ where $A > B > C$ ,and $A \geq h ^ { 2 } / 2 T \geq C .$

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0003_pages_0141-0210/auto/images/8d5eba1c1b68f023addc30eff78f71a3cbc1f524a93fa38b2912ba9d4e329594.jpg)  
Fig. 5.10-5. Locus of h on momentum sphere.

# 5.ll Unequal Moments of Inertia with Zero Moment (Analytic Solution)

When the moments of inertia $A$ ， $B$ ， $C$ are unequal, the general solution of Eqs. 5.10-1 results in eliptic functions. We take advantage of Eqs. 5.10-6 and 5.10-7 which are integrals of the Euler equations, and obtain

$$
{ \begin{array} { r l } { h ^ { 2 } - 2 T A = B ( B - A ) { \omega _ { 2 } } ^ { 2 } + C ( C - A ) { \omega _ { 3 } } ^ { 2 } } \\ { h ^ { 2 } - 2 T B = A ( A - B ) { \omega _ { 1 } } ^ { 2 } + C ( C - B ) { \omega _ { 3 } } ^ { 2 } } \\ { h ^ { 2 } - 2 T C = A ( A - C ) { \omega _ { 1 } } ^ { 2 } + B ( B - C ) { \omega _ { 2 } } ^ { 2 } } \end{array} }
$$

If we assume $A > B > C$ ,Eq. 5.11-1 is always negative, Eq. 5.11-3 is always positive,and Eq.5.11-2 maybe either positive or negative. From Eqs. 5.11-1 and 3, we write

$$
\begin{array} { l } { { { \omega _ { 1 } } ^ { 2 } = \displaystyle \frac { h ^ { 2 } - 2 T C } { A ( A - C ) } \left\{ 1 - \displaystyle \frac { B ( B - C ) } { h ^ { 2 } - 2 T C } { { \omega _ { 2 } } ^ { 2 } } \right\} } } \\ { { { \omega _ { 3 } } ^ { 2 } = \displaystyle \frac { 2 T A - h ^ { 2 } } { C ( A - C ) } \left\{ 1 - \left( \displaystyle \frac { A - B } { B - C } \right) \left( \displaystyle \frac { h ^ { 2 } - 2 T C } { 2 T A - h ^ { 2 } } \right) \displaystyle \frac { B ( B - C ) } { ( h ^ { 2 } - 2 T C ) } { { \omega _ { 2 } } ^ { 2 } } \right\} } } \end{array}
$$

We now let

$$
\begin{array} { l l l } { { y = \displaystyle \sqrt { \frac { B ( B - C ) } { h ^ { 2 } - 2 T C } } \omega _ { 2 } } } & { { } } & { { } } \\ { { k = \displaystyle \sqrt { \left( \frac { A - B } { B - C } \right) \left( \frac { h ^ { 2 } - 2 T C } { 2 T A - h ^ { 2 } } \right) } \quad } } & { { 0 \leq k \leq 1 } } \end{array}
$$

so that

$$
\omega _ { 1 } = \sqrt { \frac { h ^ { 2 } - 2 T C } { A ( A - C ) } } \sqrt { 1 - y ^ { 2 } }
$$

$$
\omega _ { 3 } = \sqrt { \frac { 2 T A - h ^ { 2 } } { C ( A - C ) } } \sqrt { 1 - k ^ { 2 } y ^ { 2 } }
$$

Substituting these into the second of Eq. 5.10-1, we obtain

$$
\begin{array} { l } { \displaystyle { { \dot { \omega } } _ { 2 } = \sqrt { \frac { \hbar ^ { 2 } - 2 T C } { B ( B - C ) } } \ j } } \\ { \displaystyle { = \frac { ( C - A ) } { B } \sqrt { \frac { ( h ^ { 2 } - 2 T C ) ( 2 T A - h ^ { 2 } ) } { A C ( C - A ) ^ { 2 } } } \sqrt { ( 1 - y ^ { 2 } ) ( 1 - k ^ { 2 } y ^ { 2 } ) } } } \end{array}
$$

which is recognized as an elliptic integral of the first kind,

$$
N t = u = \sqrt { \frac { ( B - C ) ( 2 T A - h ^ { 2 } ) } { A B C } } t = \int _ { 0 } ^ { y } \frac { d y } { \sqrt { ( 1 - y ^ { 2 } ) ( 1 - k ^ { 2 } y ^ { 2 } ) } }
$$

where $t$ is measured from the instant when $\omega _ { 2 } = 0$ . On leting $y = \sin \phi$

$$
u = \int _ { 0 } ^ { \phi } \frac { d \phi } { \sqrt { 1 - k ^ { 2 } \sin ^ { 2 } \phi } } = F ( \phi , k )
$$

and $u$ becomes a function of the modulus $k$ and the amplitude $\phi$ . Conversely, $_ y$ is a function of $u = N t$ and $k$ ，and is available as a tabulated function for $0 \le k \le 1$ ,where $N$ is defined by Eq. 5.11-9.

$$
y = \mathcal { S } n ( u , k )
$$

Thus from Eq. 5.11-5 the solution for $\omega _ { 2 }$ is

$$
\omega _ { 2 } = \sqrt { \frac { h ^ { 2 } - 2 T C } { B ( B - C ) } } \mathcal { S } n ( N t . k )
$$

Likewise, it can be shown that the solution for the angular velocities about the other two axes are

$$
\begin{array} { l } { \omega _ { 1 } = \sqrt { \displaystyle \frac { h ^ { 2 } - 2 T C } { A ( A - C ) } } \mathcal { C } n ( N t , k ) } \\ { \omega _ { 3 } = - \sqrt { \displaystyle \frac { 2 T A - h ^ { 2 } } { C ( A - C ) } } \mathcal { D } n ( N t , k ) } \end{array}
$$

where the $\mathcal { C } n$ and $\mathcal { D } n$ functions are related to the $\mathcal { S } n$ function by the equations,

$$
\begin{array} { l } { { \mathcal { C } } { \mathrm { { } } n } ^ { 2 } x = 1 - { \mathcal { S } } { \mathrm { { } } n } ^ { 2 } x } \\ { { \mathcal { D } } { \mathrm { { } } n } ^ { 2 } x = 1 - k ^ { 2 } { \mathcal { S } } { \mathrm { { } } n } ^ { 2 } x } \end{array}
$$

These solutions correspond to the case $h ^ { 2 } < 2 T B$ which is required for $0 \le k \le 1$ ·

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0003_pages_0141-0210/auto/images/143a39ee31d2fc09ebfc76011e3e17cc5157ecb6ee806d5b1c132e567e152cf6.jpg)  
Fig.5.11-1. Plot of elliptic functions. Fig. 5.l1-2. Plot of elliptic functions.

For small values of $k  0$ (i.e., $A$ approaching $B$ ), the elliptic functions approach the trigonometric functions,

$$
\begin{array} { l } { { \mathcal { S } n ( N t , 0 ) = \sin \left( N t \right) } } \\ { { \mathcal { C } n ( N t , 0 ) = \cos \left( N t \right) } } \\ { { \mathcal { D } n ( N t , 0 ) = 1 . 0 } } \end{array}
$$

Thus when $A = B$ , the angular velocities reduce to the form:

$$
\begin{array} { l } { \omega _ { 2 } = \beta \sin \left( N t \right) } \\ { \omega _ { 1 } = \beta \cos \left( N t \right) } \\ { \omega _ { 3 } = n } \end{array}
$$

which agree with the results of Sec. 5.8.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0003_pages_0141-0210/auto/images/901b8f62f3cb2a163fef3ae0e4b416ec2b5f82e5c4c0062e1c16ccfce5b14221.jpg)

Table of $y = \sin { \phi } = \mathcal { S } n ( u , k )$ Taken from Peirce's Table of Integrals 3rd Revised Ed. p. 122

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0003_pages_0141-0210/auto/images/0203222f72aa3948eaf3416fc35abc60e90cf22991a429018fd98b2b87474189.jpg)  
Fig. 5.11-3. Plot of elliptic function $\mathcal { S } n ( u , k )$

To show the effect of $A \neq B ,$ a plot of the elliptic function for $k = \%$ is compared to the trigonometric functions in Fig. 5.11-1. If y = sin \$ = $\mathcal { S } n ( u , k )$ is plotted against $u = N t$ for various values of $k$ ，with $\boldsymbol { u }$ normalized to unity at $\phi = 9 0 ^ { \circ }$ , the plot of $\mathcal { S } n ( u , k )$ will appear as in Figs. 5.11-2 and 5.11-3.

# 5.12 Stability of Rotation about Principal Axes

If we write Euler's equations for no external moment in the form,

$$
\begin{array} { r } { A \dot { \omega } _ { 1 } = ( B - C ) \omega _ { 2 } \omega _ { 3 } } \\ { B \dot { \omega } _ { 2 } = ( C - A ) \omega _ { 1 } \omega _ { 3 } } \\ { C \dot { \omega } _ { 3 } = ( A - B ) \omega _ { 1 } \omega _ { 2 } } \end{array}
$$

we find that,

$$
\begin{array} { c c c } { \omega _ { 1 } = \mathrm { c o n s t a n t } } & { \mathrm { i f } } & { \omega _ { 2 } = \omega _ { 3 } = 0 } \\ { \omega _ { 2 } = \mathrm { c o n s t a n t } } & { \mathrm { i f } } & { \omega _ { 1 } = \omega _ { 3 } = 0 } \\ { \omega _ { 3 } = \mathrm { c o n s t a n t } } & { \mathrm { i f } } & { \omega _ { 1 } = \omega _ { 2 } = 0 } \end{array}
$$

indicating that permanent rotations are possible about each of the principal axes. We will now show that these permanent rotations are stable about the axes of maximum and minimum moments of inertia, and unstable about the axis of intermediate moment of inertia.

We will assume constant rotation about one of the axes, say axis 1, and allow a small perturbation to determine its stability. We then have an initial condition $\omega _ { 1 } = \omega _ { 0 } , \ \omega _ { 2 } = \omega _ { 3 } = 0$ ， and a perturbed condition, $\omega _ { 1 } = \omega _ { 0 } + \epsilon$ with $\omega _ { 2 }$ and $\omega _ { 3 }$ small. The linearized equations are,

$$
\begin{array} { c } { A \dot { \epsilon } = 0 } \\ { B \dot { \omega } _ { 2 } = ( C - A ) \omega _ { 0 } \omega _ { 3 } } \\ { C \dot { \omega } _ { 3 } = ( A - B ) \omega _ { 0 } \omega _ { 2 } } \end{array}
$$

Differentiating the second and third of Eq. 5.12-2, we obtain,

$$
\begin{array} { l } { { \displaystyle { \ddot { \omega } } _ { 2 } + \frac { ( A - B ) ( A - C ) } { B C } \omega _ { 0 } { } ^ { 2 } \omega _ { 2 } = 0 } } \\ { { \displaystyle { \ddot { \omega } } _ { 3 } + \frac { ( A - B ) ( A - C ) } { B C } \omega _ { 0 } { } ^ { 2 } \omega _ { 3 } = 0 } } \end{array}
$$

which are stable provided $( A - B ) ( A - C )$ is positive. We see that this condition is satisfied provided $A > B$ ,and $A > C$ $A$ a major principal axis), or $B > A$ ,and $C > A$ $A$ a minor principal axis). When $A$ is an intermediate value between B and C, (A - B)(A - C) is negative, and small values of ωz and ωg will increase. The first of Eq. 5.12-2 requires that the small perturbation e remain constant, and, hence, if axis 1 is either a major or minor principal axis, the rotation is stable. If axis l is an intermediate axis, $\omega _ { 2 }$ and $\omega _ { 3 }$ will increase,resulting in an unstable oscillation. The above conclusions can be simply demonstrated by dropping an eraser spinning about each of the principal axes. Situations requiring modification of these conclusions are discussed in Sec. 7.6.

# PROBLEMS

1. Determine the ellipsoid of inertia for the configuration of Prob. 5.5-4.   
2. Determine the elipsoid of inertia for a solid uniform cylinder of radius $R$ and length $2 R$ What is its moment of inertia about a line passing through its geometric center and the perifery of one end.   
3. Consider a spinning body with $A > B > C$ With initial conditions $\omega _ { 1 } = p _ { 0 }$ $\omega _ { 2 } = 0 , \omega _ { 3 } \doteq r _ { 0 } ,$ find $\omega _ { 1 } , \omega _ { 2 } ,$ and $\omega _ { 3 }$ for a motion characterized by one of the plane polhodes

$$
{ \frac { r _ { 0 } } { p _ { 0 } } } = \pm { \sqrt { \frac { A ( A - B ) } { C ( B - C ) } } }
$$

Show that, with $t$ approaching $\infty$ , the motion tends to a permanent rotation about axis 2

4. Show that, for a body with principal moments of inertia $A$ ， $B$ $C .$ the polhodes are closed curves while the herpolhodes generated on the invariable plane are generally open curves.   
5. Derive the equations for $\omega _ { 1 }$ $\omega _ { 2 } , \mathrm { ~ } \omega _ { 3 } ,$ when $h ^ { 2 } > 2 T B$ and $A > B > C$   
6. Discuss the stability of rotation of an unsymmetric body in the moment-free case in terms of the polhode curves of Fig. 5.10-4.   
7. Solve for the exact solution of a simple pendulum oscillating through large amplitudes. Express the equation for the period in terms of an elliptical integral and its series approximation.   
8. For $h ^ { 2 } / 2 T < B$ ,where $A > B > C$ , the angle $\theta _ { 3 }$ made by the h vector and the $h _ { 3 }$ axis is defined by the equation (see Fig. 5.10-5)

$$
\sin \theta _ { 3 } = \frac { 1 } { h } \ \sqrt { \overline { { { h _ { 1 } } ^ { 2 } + h _ { 2 } ^ { 2 } } } }
$$

Show that the value of $\theta _ { 3 }$ varies between

$$
\begin{array} { r } { \sin \theta _ { \mathfrak { z } _ { \operatorname* { m a x } } } = \sqrt { \frac { B C } { B - C } \left( \frac { 1 } { C } - \frac { 1 } { h ^ { 2 } / 2 T } \right) } } \\ { \sin \theta _ { \mathfrak { z } _ { \operatorname* { m i n } } } = \sqrt { \frac { A C } { A - C } \left( \frac { 1 } { C } - \frac { 1 } { h ^ { 2 } / 2 T } \right) } } \end{array}
$$

Hint: Rewrite Eqs. 5.10-15 in terms of $h _ { 1 } , h _ { 2 } , h _ { 3 } ,$

9.Derive the equations for $\omega _ { 1 } , \omega _ { 2 }$ $\omega _ { 3 }$ when $C > B > A$ and examine the conditions $h ^ { 2 } < \bar { 2 } T B$ and $h ^ { 2 } > 2 T B$ 。

# 5.13 General Motion of a Symmetric Gyro or Top

Figure 5.13-1 shows a symmetric gyro spinning about axis $\zeta$ and supported by two gimbals. The inner gimbal allows a pitching rotation of the spin axis about the horizontal bearings $\xi$ , while the outer gimbal is free to rotate about the vertical $Z$ axis. The gyro is then pivoted about the stationary geometric center of the gimbal system, and the center of mass does not coincide with the fixed center $o$ ·

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0003_pages_0141-0210/auto/images/ff976ab17b5c24e3e663f420bd113d15c163adfdda06464c6ff3ade00486c2e0.jpg)  
Fig. 5.l3-1. Symmetric gyro-angular momentum about gimbal axes.

We will now define precession and nutation in the following manner. The rotation $\dot { \psi }$ of the horizontal axis $\xi$ (node axis) about the vertical $Z$ axis is called precession. If the angle $\theta$ is held constant, the spin axis will generate a cone due to precession. The rotation $\dot { \theta }$ of the inner gimbal about the node axis $\xi$ is called nutation. The term signifies a nodding of the spin axis. In the general case, both precession and nutation may exist simultaneously.

We will at first neglect the mass of the gimbals,in which case we would have only the spinning wheel free to rotate in any manner about the stationary geometric center $o$ , as shown in Fig. $5 . 1 3 \mathrm { - } 1 \ : b$ The system is then identical to that of a spinning top pivoted about a fixed point $o$ ， and subject to a gravity torque $W l$ sin $\theta$ about the axis $\xi$ If $l = 0$ we have the special case of a gyro free to rotate about the center of gravity.

It is convenient here to write the moment equations about the cartesian coordinates through the geometric center with the line of nodes $\xi$ as one of the axes. We will let the moment of inertia of the wheel about the node axis system axes and the angular momentum about them are, $\xi$ $\gamma _ { j }$ ,and $\zeta$ be $A$ ， $A$ ， $C$ Theangularvelocitiesofthe $\xi$ ， $\eta$ ， $\zeta$

$$
\begin{array} { r l r l } & { \omega _ { \xi } = \dot { \theta } \qquad } & & { h _ { \xi } = A \dot { \theta } } \\ & { \omega _ { \eta } = \dot { \psi } \sin \theta \qquad } & & { h _ { \eta } = A \dot { \psi } \sin \theta } \\ & { \omega _ { \zeta } = \dot { \psi } \cos \theta \qquad } & & { h _ { \zeta } = C ( \dot { \varphi } + \dot { \psi } \cos \theta ) } \end{array}
$$

where $\varphi$ is the spin angle of the body axes 1,2,referenced to the node axis $\xi$ The components of the moment equation,

$$
\mathbf { M } = [ \dot { \mathbf { h } } ] + \mathbf { \omega } \times \mathbf { h }
$$

can be immediately written down by examination of Fig. 5.13-1c.

$$
\begin{array} { r l } & { M _ { \xi } = h _ { \xi } + h _ { \zeta } \dot { \psi } \sin \theta - h _ { \eta } \dot { \psi } \cos \theta } \\ & { M _ { \eta } = h _ { \eta } + h _ { \xi } \dot { \psi } \cos \theta - h _ { \zeta } \dot { \theta } } \\ & { M _ { \zeta } = h _ { \zeta } + h _ { \eta } \dot { \theta } - h _ { \xi } \dot { \psi } \sin \theta } \end{array}
$$

Substituting for the components of h and M, these equations become,

$$
\begin{array} { c } { { \sin \theta = { \cal A } \ddot { \theta } + C ( \dot { \varphi } + \dot { \psi } \cos \theta ) \dot { \psi } \sin \theta - { \cal A } \dot { \psi } ^ { 2 } \sin \theta \cos \theta } } \\ { { 0 = { \cal A } \displaystyle \frac { d } { d t } \left( \dot { \psi } \sin \theta \right) + { \cal A } \dot { \theta } \dot { \psi } \cos \theta - C \dot { \theta } ( \dot { \varphi } + \dot { \psi } \cos \theta ) } } \\ { { 0 = C \displaystyle \frac { d } { d t } \left( \dot { \varphi } + \dot { \psi } \cos \theta \right) } } \end{array}
$$

The last equation indicates that $\dot { \varphi } + \dot { \psi }$ cos $\theta$ is a constant, and we will let it equal $_ { n }$

$$
\boldsymbol { n } = \dot { \varphi } + \dot { \psi } \cos \theta
$$

With this substitution, the first two equations of Eq. 5.13-4 can be integrated with proper integrating factors. We will, however, consider an alternative approach based on certain integrals of the equations of motion which are constant. These are the conservation of total energy, and the conservation of angular momentum about the vertical Z axis which is moment-free.

If we examine the equations for the angular velocities about the hody axes,

$$
\begin{array} { r l } & { \omega _ { 1 } = \dot { \theta } \cos \varphi + \dot { \psi } \sin \theta \sin \varphi } \\ & { \omega _ { 2 } = - \dot { \theta } \sin \varphi + \dot { \psi } \sin \theta \cos \varphi } \\ & { \omega _ { 3 } = \dot { \varphi } + \dot { \psi } \cos \theta = n } \end{array}
$$

we would find that by adding the squares of the first two, that the square of the resultant velocity in the equatorial plane, in terms of Euler's angles is

$$
{ \omega _ { 1 } } ^ { 2 } + { \omega _ { 2 } } ^ { 2 } = { \dot { \theta } } ^ { 2 } + { \dot { \psi } } ^ { 2 } \sin ^ { 2 } \theta
$$

Since $\omega _ { 3 }$ is constant and equal to $n$ , the kinetic energy can now be written as,

$$
T = { \textstyle \frac { 1 } { 2 } } C n ^ { 2 } + { \textstyle \frac { 1 } { 2 } } A ( \dot { \theta } ^ { 2 } + \dot { \psi } ^ { 2 } \sin ^ { 2 } \theta )
$$

Referencing the potential energy to the level of the origin of the coordinate syst Lem

$$
U = W l \cos { \theta }
$$

and the total energy $E$ , which must be a constant, becomes

$$
E = { \textstyle \frac { 1 } { 2 } } C n ^ { 2 } + { \textstyle \frac { 1 } { 2 } } A ( \dot { \theta } ^ { 2 } + \dot { \psi } ^ { 2 } \sin ^ { 2 } \theta ) + { \cal W } l \cos \theta
$$

which is one of the first integrals of the differential equations of motion.

With the moment about the $Z$ axis equal to zero, the momentum $h _ { Z } = h _ { \zeta }$ cos $\theta + h _ { \eta } \sin \theta$ must be a constant,

$$
h _ { Z } = C n \cos \theta + A \dot { \psi } \sin ^ { 2 } \theta
$$

This equation could also be obtained from the Lagrangian approach since the generalized coordinate $\psi$ is a cyclic coordinate with $M _ { Z } = 0$ (see Chap. 9) Solving for $\dot { \psi }$ from the above equation,

$$
\dot { \psi } = \frac { h _ { Z } - C n \cos \theta } { A \sin ^ { 2 } \theta }
$$

and substituting into Eq. 5.13-10, we obtain the following form of the energy equation,

$$
E - { \frac { C n ^ { 2 } } { 2 } } = { \frac { A { \dot { \theta } } ^ { 2 } } { 2 } } + { \frac { ( h _ { z } - C n \cos \theta ) ^ { 2 } } { 2 A \sin ^ { 2 } \theta } } + W l \cos \theta
$$

Equation 5.13-13 is entirely in terms of $\theta$ , and its solution substituted into Eq.5.13-10 completely describes the motion of the system.

We now make the following substitution of symbols :

$$
{ \begin{array} { r l r } { \alpha = { \cfrac { 2 } { A } } { \Bigl ( } E - { \cfrac { C n ^ { 2 } } { 2 } } { \Bigr ) } } & { { \mathrm { a ~ c o n s t a n t } } } \\ { \beta = { \cfrac { 2 W l } { A } } } & { { \mathrm { a ~ c o n s t a n t } } } \\ { \gamma = { \cfrac { h _ { Z } } { A } } } & { { \mathrm { a ~ c o n s t a n t } } } \\ { N = { \cfrac { C n } { A } } } & { { \mathrm { a ~ c o n s t a n t } } } \\ { u = \cos \theta } & { { \mathrm { a ~ v a r i a b l e } } } \end{array} }
$$

which enables Eq. 5.13-13 to be writen as,

$$
\propto \sin ^ { 2 } \theta = \dot { \theta } ^ { 2 } \sin ^ { 2 } \theta + ( \gamma - N \cos \theta ) ^ { 2 } + \beta \cos \theta \sin ^ { 2 } \theta
$$

In terms of $\boldsymbol { u }$ ,the equation becomes,

$$
\dot { u } ^ { 2 } = ( \alpha - \beta u ) ( 1 - u ^ { 2 } ) - ( \gamma - N u ) ^ { 2 }
$$

The solution of theabove equation is given bythefollowing integral which can be evaluated in terms of elliptic functions.

$$
t = \int _ { u ( 0 ) } ^ { u ( t ) } \frac { d u } { \sqrt { ( \alpha - \beta u ) ( 1 - u ^ { 2 } ) - ( \gamma - N u ) ^ { 2 } } }
$$

The mathematical solution resulting from the above eliptical integral is difficult to interpret, however; fortunately it is not necessary tocarryout the above solution to evaluate the behavior of the gyro. If we let,

$$
{ \dot { u } } ^ { 2 } = f ( u )
$$

Equation 5.13-15 can be written as,

$$
f ( u ) = ( \alpha - \beta u ) ( 1 - u ^ { 2 } ) - ( \gamma - N u ) ^ { 2 }
$$

and the roots of this equation willtell us a great deal about the motion of the gyro.

Although $u = \cos \theta$ is limited between $\pm 1$ for the physical problem, mathematically $u$ can extend outside this region. For large values of $u$ ,the dominant term $\mathrm { i n } f ( u )$ is $\beta u ^ { 3 }$ ,thus $f ( u )$ must be positive for large positive $u$ , and negative for large negative $u$ ,as shown in Fig. 5.13-2. Also at $u = 1$ ， the first term drops out, leaving,

$$
f ( \pm 1 ) = - ( \gamma \mp N ) ^ { 2 }
$$

It is evident then that $f ( u )$ at $u = \pm 1$ must always be negative. Looking at the expression for $f ( u )$ in terms of $\theta$ ，

$$
f ( u ) = \dot { u } ^ { 2 } = \dot { \theta } ^ { 2 } \sin ^ { 2 } \theta
$$

we find that, for real values of $\theta$ and $\theta , f ( u )$ must be positive. We therefore conclude that,for the physical problem, u = cos $\theta$ , must always lie between $u _ { 1 }$ and $u _ { 2 }$ for which $f ( u )$ is positive.

We note next that for $\theta > 0$ ， $\dot { \theta }$ must be zero at $u _ { 1 }$ and $u _ { 2 }$ ,which requires that the spin axis Og move between the bounding circles u1 = cos θ1 and $u _ { 2 } = \cos \theta _ { 2 } ,$ as shown in Fig. 5.13-3.

The type of curve traced by the spin axis in the region $\theta _ { 1 }$ and $\theta _ { 2 } ,$ depends on the relative values of $\gamma$ and $N$ For example, Eq. 5.13-12 can be written as,

$$
\dot { \psi } = \frac { \gamma - \mathcal { N } u } { 1 - u ^ { 2 } }
$$

and since $\boldsymbol { u }$ is less than 1 between $u _ { 1 }$ and $u _ { 2 }$ ,the sign of $\dot { \psi }$ depends on γ - Nu. If γ = Nu1,then γ must be zero at the upper bounding circle and positive for θ greater than 01, as shown in Fig. 5.13-4. To obtain the curve of Fig. 5.13-5, $\dot { \psi }$ must change sign for some value of $\boldsymbol { u }$ between $u _ { 1 }$ and $u _ { 2 }$ ，Thus for this case, $\gamma - N u _ { i } = 0$ for $u _ { 2 } < u _ { i } < u _ { 1 }$

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0003_pages_0141-0210/auto/images/091348303ae2b48feeda64661754aefc4752185c7a870d77ab183aca0fe67243.jpg)  
Fig. 5.13-2. Cubic equation representing motion of symmetric gyro.

# Initial conditions

If a gyro or top is started at $t = 0$ with $\theta = \theta _ { 0 }$ and $\dot { \theta } = \dot { \psi } = 0$ ,the values of the two constants of the system, E and hz are found from Eqs. 5.13-12 and 5.13-13, to be,

$$
\begin{array} { r } { h _ { Z } = C n \cos \theta _ { 0 } } \\ { E - \frac { 1 } { 2 } C n ^ { 2 } = W l \cos \theta _ { 0 } } \end{array}
$$

SubstitutingintoEqs.5.13-12and5.13-13,theequationsforthepreceion and nutation are,

$$
\begin{array} { l } { { \dot { \psi } = \displaystyle \frac { N ( \cos \theta _ { 0 } - \cos \theta ) } { \sin ^ { 2 } \theta } } } \\ { { \dot { \theta } ^ { 2 } = ( \cos \theta _ { 0 } - \cos \theta ) \bigg [ \beta - \frac { N ^ { 2 } } { \sin ^ { 2 } \theta } ( \cos \theta _ { 0 } - \cos \theta ) \bigg ] } } \end{array}
$$

These equations both agree with the initial conditions imposed on the system. The second of the above equations indicates that the right side of the equationmustalways bepositive,therefore $\theta _ { 0 }$ must correspond to the

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0003_pages_0141-0210/auto/images/fe63d0a11b61daf7732fc4abfd71918ddde94093b99b9cd56510da5240b234cf.jpg)  
Fig. 5.l3-3. Oscillation bounded between $\theta _ { 1 }$ and $\theta _ { 2 }$ with $\gamma > N u _ { 1 } ,$

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0003_pages_0141-0210/auto/images/12cac5760c2ac42ac7d1c296b0e253dc8a6bd14e4049da785d0df78258f68fcb.jpg)  
Fig. 5.I3-4. Oscillation bounded between $\theta _ { 1 }$ and $\theta _ { 2 }$ with $\gamma = N u _ { 1 }$

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0003_pages_0141-0210/auto/images/65ea1b71d6b3d9afc510b97724dce4ddd76e7eb6e9a89318a59c2b98c9aac433.jpg)  
Fig. 5.l3-5. Oscillation bounded between $\theta _ { 1 }$ and $\theta _ { 2 }$ with $\gamma = N u _ { i } ,$ where $u _ { 2 } < u _ { i } < u _ { 1 }$

highest elevation of the spin axis, or the upper bounding circle. The lower bounding circle is found by letting $\dot { \theta } = 0$ and solving for cos $\theta$ . The result is

$$
\cos \theta = \frac { N ^ { 2 } } { 2 \beta } \pm \sqrt { 1 - \frac { N ^ { 2 } } { \beta } \cos \theta _ { 0 } + \left( \frac { N ^ { 2 } } { 2 \beta } \right) ^ { 2 } }
$$

It can be shown that the sign before the radical must be negative. For instance, since cos $\theta _ { 0 }$ is less than 1, the radical is greater than

$$
\sqrt { 1 - \frac { N ^ { 2 } } { \beta } + \left( \frac { N ^ { 2 } } { 2 \beta } \right) ^ { 2 } } = 1 - \frac { N ^ { 2 } } { 2 \beta } < \sqrt { 1 - \frac { N ^ { 2 } } { \beta } \cos \theta _ { 0 } + \left( \frac { N ^ { 2 } } { 2 \beta } \right) ^ { 2 } } = \cos \theta - \frac { N ^ { 2 } } { 2 }
$$

Thus if the positive sign is used, this would require that,

$$
\cos \theta > 1
$$

which is an impossibilty. Thus $\theta _ { 2 }$ corresponding to the lower bounding circle is given by the equation

$$
\cos \theta _ { 2 } = \frac { N ^ { 2 } } { 2 \beta } - \sqrt { 1 - \frac { N ^ { 2 } } { \beta } \cos \theta _ { 0 } + \left( \frac { N ^ { 2 } } { 2 \beta } \right) ^ { 2 } }
$$

# 5.14 Steady Precession of a Symmetric Gyro or Top

In the previous section it was shown that the spinning top pivoted about afixed point is able to movein such a manner that its axis of symmetry $O \zeta$ occupies a zone between $\theta _ { 1 }$ and $\theta _ { 2 }$ corresponding to the roots of $\begin{array} { r } { \nabla { f } ( u ) = 0 } \end{array}$ at $u _ { 1 }$ and $u _ { 2 }$ It is evident then that as $u _ { 1 }$ and $u _ { 2 }$ approach each other, the annular zone between $\theta _ { 1 }$ and $\theta _ { 2 }$ will narrow until eventually they merge to a single value $\theta _ { s } ,$ as shown inFig.5.14-1. Physically,this is the angleof steady precession which can be initiated by the initial conditions, $\theta = \theta _ { s }$ $\dot { \theta } = 0$ ,and $\dot { \psi } = \dot { \psi } _ { s }$

The analysis for this special case is probably one of the simplest cases of the spinning top, which willnow be investigated. Although the problem can be approached mathematically from the two equations,

$$
\begin{array} { l } { f ( u ) = 0 } \\ { \frac { d f ( u ) } { d u } = 0 } \end{array}
$$

it will be more instructive to examine the problem from a physical basis as follows.

For steady precession,θ = 0,and the angular velocities about the 5,n, $\zeta$ axes, shown in Fig. 5.13-1c,are

$$
\begin{array} { r } { \omega _ { \xi } = 0 } \\ { \omega _ { \eta } = \dot { \psi } \sin \theta } \\ { \omega _ { \zeta } = \dot { \psi } \cos \theta } \end{array}
$$

The angular momentum about the corresponding axes are,

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0003_pages_0141-0210/auto/images/3eef27e0c709d1581f62505a5dbce9461cc75beedd42fa7fbbad84383cb5a4c3.jpg)  
Fig. 5.l4-I. Steady precession corresponding to $u _ { 1 } = u _ { 2 } = u _ { g }$

$$
\begin{array} { r l } & { h _ { \xi } = 0 } \\ & { h _ { \eta } = A \dot { \psi } \sin \theta } \\ & { h _ { \zeta } = C ( \dot { \varphi } + \dot { \psi } \cos \theta ) = C n } \end{array}
$$

and the moment about the $\xi$ axis becomes

$$
\begin{array} { r } { M _ { \xi } = h _ { \zeta } \dot { \psi } \sin \theta - h _ { \eta } \dot { \psi } \cos \theta \ } \\ { = C n \dot { \psi } \sin \theta - A \dot { \psi } ^ { 2 } \sin \theta \cos \theta = W l \sin \theta , } \end{array}
$$

$$
{ \dot { \psi } } ^ { 2 } - \left( { \frac { C n } { A \cos \theta } } \right) { \dot { \psi } } + { \frac { W l } { A \cos \theta } } = 0
$$

The two precessional speeds are then given by the equation,

$$
\dot { \psi } _ { 1 , 2 } = \frac { C n } { 2 A \cos \theta } \pm \sqrt { \left( \frac { C n } { 2 A \cos \theta } \right) ^ { 2 } - \frac { W l } { A \cos \theta } }
$$

provided the spin is great enough to keep the radical of the above equation positive. This requirement is satisfied if,

$$
n ^ { 2 } > { \frac { ' 4 A W l \cos \theta } { C ^ { 2 } } }
$$

Further insight to the problem is obtained by plotting $M _ { \xi }$ versus $\dot { \psi }$ from Eq. 5.14-2,as shown in Fig.5.14-2. The curve is a parabola and for any value of M there correspond two precessional speeds. When M = 0, the precessional speeds are zero and γo. This value of the precessional speed is given by the equation,

$$
{ \dot { \psi } } _ { 0 } = { \frac { C n } { A \cos \theta } } = { \frac { C \dot { \varphi } } { ( A - C ) \cos \theta } }
$$

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0003_pages_0141-0210/auto/images/eb54f99167952cfc0120ceab33b09c0e3e30b56fb4b0e62eba1fee535dbf007c.jpg)  
Fig. 5.l4-2. Constant moment $M _ { \xi }$ results in two possible precessional speeds $\dot { \psi } _ { 1 }$ and $\dot { \psi } _ { 2 }$

which agree with that of the moment-free gyro (see Eq. 5.9-4). The precessional speed corresponding to the peak moment is

$$
{ \dot { \psi } } _ { p } = { \frac { C n } { 2 A \cos \theta } }
$$

and the corresponding peak moment is

$$
M _ { \xi _ { \mathrm { m a x } } } = { \frac { 1 } { 4 } } { \frac { C ^ { 2 } n ^ { 2 } } { A } } \tan \theta
$$

For intermediate moment M, the two precessional speeds 1 and γ2 are referred to as the slow and the fast precession. In general, the fast precession is not attained due to the high kinetic energy required,and the precession of a spinning top is usually slow precession.

# Limiting cases

For $\dot { \psi }$ to be real,itis ncessaryfortheterms under theradical of Eq. 5.14-4 to be greater than zero, or,

$$
C ^ { 2 } n ^ { 2 } \geq 4 W l A \cos { \theta }
$$

If $\theta = 9 0 ^ { \circ }$ ，Eq. 5.14-5 indicates that the minimum required $n$ is zero. However,Eq.5.4 $\dot { \psi }$ thenis indeterminate.Thislimiting

case can be resolved for n greater than zero by the elementary consideration of Fig. 5.14-3. Therate of change of the angular momentum vector ht = $C n ,$ is equal to the moment $M _ { \xi } = W l$

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0003_pages_0141-0210/auto/images/f78a8aa67377cdb7a74676d14c4e8e9a16b6bba86bc4c6e9184a90abfe80e1ae.jpg)  
Fig. 5.14-3. Limiting case $\theta = 9 0 ^ { \circ }$

The whirling speed $\dot { \psi }$ for $\theta = 9 0 ^ { \circ }$ is therefore equal to,

$$
\dot { \psi } = \frac { W l } { C n }
$$

and as long as $_ { n }$ is finite, $\dot { \psi }$ will also remain finite.

The same result can also be obtained from Eq. 5.14-3, for as $\cos  0$ ， the term $\dot { \psi } ^ { 2 }$ is negligible compared to the other two.

For $\theta = 0 ^ { \circ }$ , the required value of $n$ from Eq. 5.14--5 must satisfy the equation,

$$
n \geq { \frac { 2 } { C } } { \sqrt { W l A } }
$$

in which case we have the sleeping top. Equation 5.14-10 is often used to determine the spin of a missile or a projectile necessary for stability. Referring to Fig. 5.14-4, as long as the spin axis $O \zeta$ coincides with the velocity vector of the missile, the drag force will also coincide with $O \zeta$ However, if the spin axis deviates slightly from the velocity vector by a small angle $\theta$ ,the drag force, which acts at the center of pressure,a distance l ahead of the center of mass, will have a moment $R l$ sin $\theta$ about the center of mass. Thus this problem is identical to that of the sleeping top with $W l$ replaced by $R l$ .The missile or projectile will hence be stable if the spin is great enough as established by,

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0003_pages_0141-0210/auto/images/0ea4515fb91c08290667dbd22ffb1177c7382a8ca9433167b999e4078da49d4a.jpg)  
Fig. 5.I4-4. Spin stabilization of missiles and projectiles.

# PROBLEMS

1. A symmetrical gyro is mounted on two weightless gimbals. What are the expressions for the moment of momentum about the $\xi$ ， $\eta , ~ \zeta$ ,and $Z$ axes. Write the differential equation for the moment about the above axes.

2. For the symmetrical gyro or top, with moment due to gravity,determine the equation for the phase plane plot $\dot { u }$ versus $u$ , and express the equation for the period of nutation in terms of $f ( u )$ ·

3. The condition for the sleeping top, $u = \cos 0 ^ { \circ } = 1$ , can be satisfied by either of the curves shown below. Show that $( a )$ is stable and $( b )$ is unstable by considering a smallvariation of the curves as indicated by the dotted lines.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0003_pages_0141-0210/auto/images/6b5db2ac312135ee8cef15da68335578e5b309f39e1383d8ff2a049c5cdd52d4.jpg)  
Prob.3

4. If the stability of the sleping top is indicated by $( a )$ in the Fig. for Prob. 3, deduce the relationship $n \geq ( 2 / C ) \sqrt { \overline { { W l A } } }$ by noting that,

$$
\begin{array} { r l r l r l } & { u = 1 } & & { } & & { f ( u ) = ( - \dot { \theta } \sin \theta ) ^ { 2 } = 0 } \\ & { \frac { d f ( u ) } { d u } = 0 } & & { \mathrm { a n d } } & & { \frac { d ^ { 2 } f ( u ) } { d u ^ { 2 } } = \mathrm { n e g a t i v e } } \end{array}
$$

5. Show that the equation for the steady precesson of a top can be written as

$$
\dot { \psi } _ { 1 , 2 } = \frac { h _ { Z } } { 2 A } \pm \sqrt { \bigg ( \frac { h _ { Z } } { 2 A } \bigg ) ^ { 2 } - \frac { W l \cos \theta } { A } }
$$

6. Show that for large $^ n$ , the lower and higher precessional speeds become

$$
\dot { \psi } _ { 1 } = { \frac { W l } { C n } } \qquad \dot { \psi } _ { 2 } = { \frac { C n } { A \cos \theta } }
$$

Why is the lower precessional speed independent of $\theta$ ？

7. For steady precession, show that the angle between the momentum vector h and the spin axis is given by the equation,

$$
\tan \alpha _ { 1 , 2 } = { \frac { 1 } { 2 } } \tan \theta \left[ 1 \pm { \sqrt { 1 - { \frac { 4 W A l \cos \theta } { C ^ { 2 } n ^ { 2 } } } } } \right]
$$

where the minus sign must be used for the slow precession.

8. Show that for large $n$ , the angle $\propto$ corresponding to the slow and fast preces. sional speeds are,

$$
\tan \alpha _ { 1 } = { \frac { A W l \sin \theta } { C ^ { 2 } n ^ { 2 } } } \qquad \tan \alpha _ { 2 } = \tan \theta
$$

9. What is the expression for $\alpha$ corresponding to the minimum value of $n$ consistent with steady precession？

10.Determine the conditions necessary for small oscillation of the spin axis of a gyro, between two annular circles $\theta _ { 1 }$ and $\theta _ { 2 }$ , such that $\dot { \psi }$ is the same at the two circles.

11. The end of the spin axis of a top spinning about a fixed pivot describes on a sphere the curve shown. If $C n / A = N$ is given, determine the following quantities in terms of $N _ { i }$

$$
\gamma = \frac { h _ { Z } } { A }
$$

$$
\beta = { \frac { 2 W l } { A } }
$$

$$
\alpha = \frac { 2 } { A } \left( E - \textstyle { \frac { 1 } { 2 } } C n ^ { 2 } \right)
$$

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0003_pages_0141-0210/auto/images/6696094ade79c6feb8ad6534a8a685967fa615f7f7b2787669a87af1b2bb0a66.jpg)  
Prob.11

Show in general that a motion with the sharp cusp at 02 > 01 cannot take place.

12.A thin disk of radius $r$ and mass $m$ has a stem of length $^ a$ which is pinned to a vertical shaft as shown. Show that if r <2a,it will be unstable if $\dot { \psi } ^ { 2 } > \frac { 4 g a } { 4 a ^ { 2 } - r ^ { 2 } }$ Show also that it will be stable at all $\dot { \psi }$ if $r > 2 a$

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0003_pages_0141-0210/auto/images/64e7e9ea575afd70b8ed81c56c85b312e85a5a7e42192f3d55234b8a1fa3faf8.jpg)  
Prob.I2

13. A flywheel with axes $x$ y, $z$ has moment of inertia $I _ { x } , I _ { y } = I _ { z } ,$ and is spinning with high speed $\omega$ .If it is oscillating in pitch and yaw with the center of gravity stationary, set up the equations of motion with restraining moments equal to $K _ { p } \theta$ in pitch and $K _ { y } \psi$ in yaw.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0003_pages_0141-0210/auto/images/9205f25df3944297c9b737aa2f8927873358ec9515c3733d0267e33c5b2cf54e.jpg)  
Prob. 13

14. The ore crusher whel of weight $W$ and radius $R$ has moments of inertia $C$ and $A$ about its polar axis and an axis through $o$ parallel to the diametric axes. The spin axis $_ z$ on which thecrusher wheel isfree torotate,precesses at speed $\dot { \psi }$ about the vertical $o z$ axis.

(a) show that the spin velocity of the wheel with respect to the axle is

$$
{ \dot { \varphi } } = - { \frac { 1 } { R } } ( l \sin \theta + R \cos \theta ) { \dot { \psi } }
$$

(b) Show that the velocity of the center of the whel is equal to

$$
v _ { c } = - R ( \dot { \varphi } + \dot { \psi } \cos \theta )
$$

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0003_pages_0141-0210/auto/images/b5694df2ced3689c85a58045db80ba2b2e5c06711f826b02cc3631e7b822a46d.jpg)  
Prob.14

15. For the ore crusher of Prob. 14, write the equation for the moment about the_pin $o$ ，and show that the normal force between the wheel and the inclined track is

$$
F = W \sin \theta + \frac { 1 } { 2 } \ : \psi ^ { 2 } \biggl [ \frac { C } { R } \left( 1 - \cos 2 \theta \right) + \frac { A } { l } \sin 2 \theta \biggr ]
$$

16. From the result of Prob.15, show that the crushing force $F$ has a maximum or minimum between $\theta \ : = \ : 4 5 ^ { \circ }$ and $9 0 ^ { \circ }$ ,or between $\bar { \theta } = 1 3 5 ^ { \circ }$ and $1 8 0 ^ { \circ }$ Since the force due to gravity is a maximum at $\theta \ : = \ : 9 0 ^ { \circ }$ ,we can reason that the maximum occurs for $\theta \ : = 4 5 ^ { \circ }$ to $9 0 ^ { \circ }$ ,or actually between $0 ^ { \circ }$ and $4 5 ^ { \circ }$ with the horizontal. Determine the optimum axle tilt above the horizontal for a crusher of the following dimensions.

$$
\begin{array} { r l } { R = 1 8 \ \mathrm { i n } . \quad } & { l = 3 \ \mathrm { f t } \ ( \mathrm { f r o m \ c e n t e r \ p l a n e \ o f \ w h e e l } } \\ { \qquad \mathrm { t o \ p i n \ } O ) } \\ { b = 1 2 \ \mathrm { i n } . \quad } & { \dot { \psi } = 1 0 0 \ \mathrm { r p m } } \end{array}
$$

17. Determine the velocity and acceleration of the top of the crusher wheel for the dimensions given in Prob. 16.

18. The general equation for the symmetrical gyro is given by Eq. 5.13-18. Show that

$$
f ^ { \prime } ( u ) = \frac { d f ( u ) } { d u } = 2 \ddot { u } = - 2 ( \dot { \theta } ^ { 2 } \cos \theta - \ddot { \theta } \sin \theta )
$$

19. For steady precession $\Dot { \theta } \ = \Ddot { \theta } \ = 0$ ， which requires that $f ( u ) = f ^ { \prime } ( u ) = 0$ From these two equations show that the steady precession is defined by the quadratic,

$$
\dot { \psi } ^ { 2 } - \frac { N } { u } \dot { \psi } + \frac { \beta } { 2 u } = 0
$$

with the following restriction

$$
N \geq \sqrt { 2 \beta u }
$$

20. A gyro of weight mg, spinning with angular speed $n$ is tied to a string of length $l _ { 1 }$ and precesses around the vertical axis with constant speed $\Omega$ If $C$ and $A$ are moments of inertia about the spin axis and its normal through the center of mass, determine the three equations of motion

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0003_pages_0141-0210/auto/images/2bea88b69ae5d773490fe7ab25d76affae3fa3aec0c4ad54598aca348ff83fab.jpg)  
Prob.20

21. The outer frame of a toy gyro is symmetric about the three axes through its geometric center, and has a moment of inertia $C _ { 2 }$ . If when the rotor is spinning with speed $\dot { \varphi }$ , the outer frame also spins at a different speed $\dot { \varphi } _ { 2 }$ in the same direction, write the new momentum and moment equations for steady precession.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0003_pages_0141-0210/auto/images/7499f6ee957f5be8a5cc97ba37201433a35baea3a1630b0df459b1b9a78b20b7.jpg)  
Prob. 21

22. If the outer frame of the toy gyro is a single ring in one plane, the moment of inertia about an axis normal to the plane of the ring will be $2 C _ { 2 }$ How does this affect the equations of Prob. 21?

# 5.l5 Precession and Nutation of the Earth's Polar Axis

In Sec. 4.18, we derived the equations for the moment exerted by the earth,due to its oblateness, on a satellite revolving around the earth. According to Newton’s third law,the satellite must exert an equal and

opposite moment on the earth, but, due to the large mass of the earth in comparison to that of the satellite, its effect is measurable only on the satellite motion.

The moment equations from Sec. 4.18, with opposite signs for moment exerted by the satellite on earth,are,

$$
{ \begin{array} { r l } & { M _ { x } = - { \cfrac { 3 K m _ { s } } { m a ^ { 3 } } } ~ ( C - A ) \sin ^ { 2 } \varphi \sin \theta \cos \theta } \\ & { } \\ & { M _ { y } = { \cfrac { 3 K m _ { s } } { m a ^ { 3 } } } ( C - A ) \sin \theta \sin \varphi \cos \varphi } \\ & { } \\ & { M _ { z } = 0 } \end{array} }
$$

These equations apply to any two bodies oriented as in Sec. 4.18, and, therefore, are applicable to the sun and earth, or the moon and earth. The fact that the earth's polar axis is inclined from the normal to the plane of the ecliptic by $2 3 ^ { \circ } 2 7 ^ { \prime }$ results in a moment exerted by the sun on the earth as shown in Fig. 5.15-1.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0003_pages_0141-0210/auto/images/b1c468245873c2d97cfe2ffe29b45e47103dd5a5a67a385f9932cff320359540.jpg)  
Fig. 5.15-l. Moments $M _ { x }$ and $M _ { y }$ exerted by sun on earth.

The angular momentum vector of the spinning earth is $C \Omega$ ,and the moment M, causes the end of the vector CΩ to move in the same direction and, therefore, change the angle $\theta$ . Since $M _ { y }$ is oscillatory with net result per cycle equal to zero, its effect is to produce an oscillatory nutation of zero net angle per cycle.

The moment $M _ { x }$ is oscillatory but cumulative along the negative $\boldsymbol { x }$ axis, which requires a net precession per cycle. Letting  be the precession rate normal to the plane of the ecliptic, the component $\dot { \psi } \sin \theta$ along the negative y direction will rotate the angular momentum vector CΩ in the direction $M _ { x }$ to give

$$
C \Omega \dot { \psi } \sin \theta = M _ { x }
$$

The precession rate from Eq. 5.15-1 is then

$$
{ \dot { \psi } } = - { \frac { 3 K m _ { s } } { m \Omega a ^ { 3 } } } \left( { \frac { C - A } { C } } \right) \cos \theta \ \sin ^ { 2 } \varphi
$$

The quantity $K m _ { s } / m = G m _ { s }$ in this equation, where $m _ { s }$ and $m$ are the mass of the sun and earth respectively, can be eliminated from the equation of the central force between the sun and the earth as follows.

$$
\frac { G m _ { s } m } { a ^ { 2 } } = \frac { K m _ { s } } { a ^ { 2 } } = m a \Big ( \frac { 2 \pi } { \tau } \Big ) ^ { 2 }
$$

Also the average value of $\sin ^ { 2 } \varphi$ for $0 \leq \varphi \leq 2 \pi$ is $\%$ , so that the average precession rate per year due to the sun is given by the equation,

$$
{ \dot { \psi } } _ { \mathrm { a v } } = - \frac { 3 } { 2 \Omega } \bigg ( \frac { 2 \pi } { \tau } \bigg ) ^ { 2 } \bigg ( \frac { C - A } { C } \bigg ) \cos \theta
$$

where $\Omega$ is the spin rate (relative to inertial space) of the earth, $\tau$ is the period of the earth around the sun, $\theta = 2 3 ^ { \circ } 2 7 ^ { \prime }$ ,and $( C - A ) / C = 0 . 0 0 3 2$ for the oblateness of the earth.

Equation 5.15-3 applies also to the earth-moon system, where $m _ { s }$ now becomes the mass of the moon. However, in eliminating the quantity $K m _ { s } / m a ^ { 3 }$ , the attractive force between the earth and moon given by Eq. 4.6-4 must be used as follows.

$$
\frac { G m m _ { s } } { a ^ { 2 } } = \left( \frac { m m _ { s } } { m + m _ { s } } \right) a \left( \frac { 2 \pi } { \tau } \right) ^ { 2 }
$$

Thus $( K m _ { s } / m a ^ { 3 } ) = [ m _ { s } / ( m + m _ { s } ) ] ( 2 \pi / \tau ) ^ { 2 }$ and the equation for the average precession rate of the earth's polar axis per revolution of the moon around the earth becomes,

$$
\dot { \psi } _ { \mathrm { a v } } = - \frac { 3 } { 2 \Omega } \frac { m _ { s } } { m + m _ { s } } \bigg ( \frac { 2 \pi } { \tau } \bigg ) ^ { 2 } \bigg ( \frac { C - A } { C } \bigg ) \cos { \theta }
$$

# PROBLEMS

1. The earth's spin rate is $\Omega = 2 \pi \times 3 6 6 . 2 5$ rad/year. Show that the earth's polar axis precesses 0.00o0765 rad/year due to the sun.

2. The mass of the moon is 11 that of earth, and its period is 27.32 days. Its orbit plane θ varies between $1 8 ^ { \circ } 1 9 ^ { \prime }$ and $2 8 ^ { \circ } 3 5 ^ { \prime }$ ,with an average value of $2 3 ^ { \circ } 2 \widehat { 7 } ^ { \prime }$ Determine theprecession of the earths polaraxisper yeardueto the moon. Determine the combined precession due to the sun and moon and show that the period of the precession of the earth's axis is approximately 26,000 years.

3. Consider the earth and moon alone with the moon's orbit plane inclined from the Earth's equatorial plane by an average of $2 3 ^ { \circ } 2 7 ^ { \prime }$ Determine the period of regression of the moon's node and show that its period is approximately 18 yrs.

# 5.16 General Motion of a Rigid Body

So far we have considered problems in which the motion about the center of mass or a fixed point can be determined independently by the moment equation

$$
\mathbf { M } = \dot { \mathbf { h } } + \mathbf { \omega } \times \mathbf { h }
$$

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0003_pages_0141-0210/auto/images/579b89b8220538d52aef6a86e6aaed45a4d411cf404ddfed0f68d3cec2dedafe.jpg)  
Fig. 5.l6-l. Rolling of a thin disk on a plane.

However in the more general type of motion the force

$$
{ \bf { F } } = m ( \dot { \bf { v } } + { \bf { \omega } } \cup \times \bf { \omega } \mathrm { { v } ) }
$$

may contribute to the moment M and the two equations are no longer independent. With each of the above equations resolved into three components, we have in general six interrelated equations which must be solved simultaneously. Such problems are, of course, more difficult to solve； however, the general procedure can be illustrated by the following simple problems.

# Rolling of a thin circular disk on a rough horizontal plane

The configuration of the rolling disk is shown in Fig. 5.16-1. We will use two sets of axes with origin coinciding with the center ofi the disk; the $X , Y , Z$ axes with fixed direction,and the 5,m, $\zeta$ axes moving with the disk.

The $\zeta$ axis is normal to the plane of the disk, and the $\xi$ ， $\eta$ axes are in the plane of the disk with $\xi$ along the horizontal. It is convenient to introduce the $\eta ^ { \prime }$ axis so that $\xi$ ， $\eta ^ { \prime }$ ， $Z$ form a third set rotated from the $X _ { i }$ ，Y, $Z$ axes about the $Z$ axis. The $\eta ^ { \prime }$ axis so defined is the horizontal projection of axis $\eta$ . The orientation of the $\zeta$ and $\xi$ axes are defined by the rotation $\theta$ about the $\xi$ axis for $\zeta$ ,and a rotation $\psi$ about the $Z$ axis for $\xi$

The constraint force of the floor consists of the normal reaction $f _ { Z }$ ,and a friction force f, which is resolved into components $f _ { \xi }$ and $f _ { \eta ^ { \prime } }$ parallel and perpendicular to the $\xi$ axis.

With $A$ ， $A$ ， $C$ as moments of inertia about the $\xi$ ， $\eta$ ， $\zeta$ , axes respectively, and $R$ as the radius of the disk, the moment equations are;

$$
\begin{array} { r l } & { M _ { \zeta } = - C \dot { \omega } _ { \zeta } = - f _ { \xi } R } \\ & { M _ { \eta } = A ( \ddot { \psi } \sin \theta + \dot { \psi } \dot { \theta } \cos \theta ) + A \dot { \theta } \dot { \psi } \cos \theta + C \omega _ { \zeta } \dot { \theta } = 0 } \\ & { M _ { \xi } = A \ddot { \theta } - C \omega _ { \zeta } \dot { \psi } \sin \theta - A \dot { \psi } ^ { 2 } \sin \theta \cos \theta = - f _ { Z } R \cos } \end{array}
$$

where $\omega _ { \zeta } = \dot { \varphi } - \dot { \psi }$ cos $\theta$ in the negative $\zeta$ direction.

Equation 5.16-4 can be rearranged as follows,

$$
A \ddot { \psi } \sin \theta = - \dot { \theta } ( C \omega _ { \zeta } + 2 A \dot { \psi } \cos \theta )
$$

which indicates that, if $\dot { \theta }$ is negative(i.disllin $\ddot { \psi }$ increases, or the spin about the vertical $\angle$ axis increases,and thedisk rolls intoatighter circle.

We assume no slipping of the disk relative to the floor, in which case the velocity of the disk center has the following components.

$$
\begin{array} { r l } & { v _ { \xi } = R \omega _ { \zeta } } \\ & { v _ { \zeta } = R \dot { \theta } } \\ & { v _ { Z } = R \dot { \theta } \cos \theta } \\ & { v _ { \eta \prime } = - R \dot { \theta } \sin \theta } \end{array}
$$

which are shown in Fig. 5.16-2. The force equation can then be written as,

$$
\begin{array} { c } { { f _ { \xi } = - m ( R \dot { \omega } _ { \zeta } + R \dot { \theta } \dot { \psi } \sin \theta ) } } \\ { { f _ { \eta ^ { \prime } } = - m ( R \ddot { \theta } \sin \theta + R \dot { \theta } ^ { 2 } \cos \theta - R \omega _ { \zeta } \dot { \psi } ) } } \\ { { f _ { z } - m g = m ( R \ddot { \theta } \cos \theta - R \dot { \theta } ^ { 2 } \sin \theta ) } } \end{array}
$$

Equations 5.16-3,5.16-4, 5.16-5 and 5.16-11,5.16-12, 5.16-13 are the six component equations which must be solved simultaneously. However

these equations have simple solutions only for certain special conditions which are;

$$
\begin{array} { l l } { { \theta \cong 9 0 ^ { \circ } } } & { { \mathrm { a n d } \omega _ { \zeta } \mathrm { l a r g e } } } \\ { { \theta \cong 9 0 ^ { \circ } } } & { { \mathrm { a n d } \omega _ { \zeta }  0 , \dot { \psi } \mathrm { l a r g e } } } \\ { { \theta \cong \ 0 ^ { \circ } } } & { { \mathrm { a n d } \omega _ { \zeta } \mathrm { s m a l l } , \dot { \psi } \mathrm { l a r g e } } } \end{array}
$$

The first case represents a rolling of the disk with its plane nearly vertical; the second case corresponds to the upright spinning of the disk about its vertical diameter; and the last case represents the disk spinning with its face nearly horizontal.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0003_pages_0141-0210/auto/images/32f706d302a6f60a8e001fa115601ea11175827f7598d8f5db3c89b74353a85b.jpg)  
Fig. 5.16-2. Components of velocity.

Rolling of a disk with plane of the disk nearly vertical

Consider the disk rolling with the plane of the disk nearly vertical. Here the angular velocities $\dot { \theta }$ and $\dot { \psi }$ will be small in comparison with $\omega _ { \zeta }$ Also sin $\theta \simeq 1$ ,and cos $\theta = \alpha$ ,where $\propto$ is the complimentary angle $\alpha = ( \pi / 2 ) -$ $\theta$ . We can therefore replace $\dot { \theta }$ and $\ddot { \theta }$ by $- \dot { \alpha }$ and $- \ddot { \alpha }$ respectively. The force and moment equations can then be written as,

$$
\begin{array} { c } { f _ { \xi } R = C \dot { \omega } _ { \zeta } } \\ { A \ddot { \psi } = C \omega _ { \zeta } \dot { \hat { z } } } \\ { - A \ddot { \alpha } - C \omega _ { \zeta } \dot { \psi } = - f _ { Z } R \alpha + f _ { \eta ^ { \prime } } R } \\ { - f _ { \xi } = m R \dot { \omega } _ { \zeta } } \\ { f _ { \eta ^ { \prime } } = m R ( \ddot { \alpha } + \omega _ { \zeta } \dot { \psi } ) } \\ { f _ { Z } - m g = 0 } \end{array}
$$

From Eqs. 5.16-14 and 5.16-17, we have,

$$
( C + m R ^ { 2 } ) { \dot { \omega } } _ { \zeta } = 0
$$

Therefore,

$$
\omega _ { \zeta } = n = \mathrm { c o n s t a n t }
$$

With the initial conditions $\dot { \psi } = 0$ ,and $\alpha = 0$ (i.e., disk started in a straight path with its plane vertical), we integrate Eq. 5.16-15 to obtain,

$$
A { \dot { \psi } } = C n \alpha
$$

We next substitute Eqs. 5.16-18, 5.16-19, and 5.16-21 into Eq. 5.16-16 and obtain,

$$
( A + m R ^ { 2 } ) \ddot { \alpha } + \biggl [ \frac { C n ^ { 2 } ( C + m R ^ { 2 } ) } { A } - m g R \biggr ] \alpha = 0
$$

This equation indicates that the plane of the disk wobbles in and out of the vertical, provided the spin is great enough to satisfy the inequality,

$$
n ^ { 2 } > \frac { m g A R } { C ( C + m R ^ { 2 } ) }
$$

Equation 5.16-21 also indicates that $\dot { \psi }$ is proportional to $\propto$ ,and hence the precession also wobbles sinusoidally. The disk then rolls in a wavy line which is nearly straight.

# Upright spinning of the disk

We next consider the case where the main motion of the disk is a spin about the vertical axis. Due to some disturbance, the disk will move in a small circle, but it is evident that $\omega _ { \zeta }$ will be small and $\dot { \psi }$ large. $\theta$ will, however,remain nearly $9 0 ^ { \circ }$ , so that again sin $\theta \cong 1$ and cos $\theta \cong \alpha$ ,where $\propto$ is a small angle.

With these approximations, the moment and force equations become,

$$
\begin{array} { c } { { f _ { \xi } R = C { \dot { \omega } } _ { \xi } } } \\ { { { \ A } { \ddot { \psi } } = 0 } } \end{array}
$$

Therefore $\dot { \psi } =$ constant.

$$
\begin{array} { r } { - A \ddot { \alpha } - C \omega _ { \zeta } \dot { \psi } - A \dot { \psi } ^ { 2 } \alpha = - f _ { Z } R \alpha + f _ { \eta ^ { \prime } } R } \\ { - f _ { \xi } = m R ( \dot { \omega } _ { \zeta } - \dot { \alpha } \dot { \psi } ) } \\ { f _ { \eta ^ { \prime } } = m R ( \omega _ { \zeta } \dot { \psi } + \ddot { \alpha } ) } \\ { f _ { z } - m g = 0 \ ~ } \end{array}
$$

From Eqs. 5.16-24 and 5.16-27, we have,

$$
( C + m R ^ { 2 } ) \dot { \omega } _ { \xi } = m R ^ { 2 } \dot { \alpha } \dot { \psi }
$$

With initial values of ω and α equal to zero, we integrate the above equation,

$$
( C + m R ^ { 2 } ) \omega _ { \xi } = m R ^ { 2 } \dot { \psi } \alpha
$$

Substituting Eqs.5.16-28,5.16-29,and 5.16-31into Eq.5.16-26,the final equation becomes,

$$
( A + m R ^ { 2 } ) \ddot { \alpha } + [ ( A + m R ^ { 2 } ) \dot { \psi } ^ { 2 } - m g R ] \alpha = 0
$$

Interpreting this equation, the spinning motion is stable as long as,

$$
\dot { \psi } ^ { 2 } > \frac { m g R } { A + m R ^ { 2 } }
$$

With this inequality satisfied,the disk oscilates sinusoidally with a small angle $\propto$ about the $\xi$ axis which is spinning around the vertical axis with speed $\dot { \psi }$ ·

# Disk spinning nearly horizontally

Spin a coin about a vertical line and watch its final stages when the plane of the coin is nearly horizontal. You will be able to detect from the sound that the frequency increases very rapidly during the last stage of oscillation. You can also observe that the point of contact with the table spins around a circle of diameter nearly equal to that of the coin, and that $\omega _ { \zeta }$ is very small (i.e., the face on the coin is rotating very slowly). The $\zeta$ axis is nearly vertical so that $\theta$ is very small. However, the end of the $\zeta$ axis is precessing around the vertical very rapidly so that $\dot { \psi }$ is very large.

With these assumptions, the moment and force equations become,

$$
\begin{array} { c } { f _ { \xi } R = C \dot { \omega } _ { \zeta } } \\ { { } } \\ { { { \cal A } \ddot { \psi } \dot { \theta } + 2 A \dot { \psi } \dot { \theta } = 0 } } \\ { { { \cal A } \ddot { \theta } - A \dot { \psi } ^ { 2 } \dot { \theta } = - f _ { Z } R + f _ { \eta ^ { \prime } } R \dot { \theta } } } \\ { { - f _ { \xi } = m R \dot { \omega } _ { \zeta } } } \\ { { f _ { \eta ^ { \prime } } = m R \omega _ { \zeta } \dot { \psi } } } \\ { { f _ { Z } - m g = m R \dot { \theta } } } \end{array}
$$

From Eqs. 5.16-34 and 5.16-37 we find that $\omega _ { \zeta }$ must be a constant.

$$
\begin{array} { c } { { ( C + m R ^ { 2 } ) \dot { \omega } _ { \zeta } = 0 } } \\ { { \omega _ { \zeta } = n = \mathrm { c o n s t a n t } } } \end{array}
$$

From Eq. 5.16-35 we obtain,

$$
\frac { \ddot { \psi } } { \dot { \psi } } = - 2 \frac { \dot { \theta } } { \dot { \theta } }
$$

Integrating with initial conditions $\dot { \psi } _ { 0 }$ and $\theta _ { 0 }$ ,we obtain

$$
\ln { \frac { \dot { \psi } } { \dot { \psi } _ { 0 } } } = - 2 \ln { \frac { \theta } { \theta _ { 0 } } }
$$

Therefore,

$$
\dot { \psi } = \dot { \psi } _ { 0 } \left( \frac { \theta } { \theta _ { 0 } } \right) ^ { - 2 }
$$

Substituting Eqs. 5.16-38, 5.16-39, and 5.16-42 into Eq. 5.16-36, we arrive at the differential equation for $\theta$

$$
( \varLambda + m R ^ { 2 } ) \ddot { \theta } = \frac { A \dot { \psi } _ { 0 } { } ^ { 2 } \theta _ { 0 } { } ^ { 4 } } { \theta ^ { 3 } } + \Bigl ( - m g R + m R ^ { 2 } n \dot { \psi } _ { 0 } \frac { \theta _ { 0 } { } ^ { 2 } } { \theta } \Bigr )
$$

Due to $\theta$ and $\theta ^ { 3 }$ in the denominator, the acceleration $\ddot { \theta }$ increases as 0 approaches zero. Equation 5.16-42 indicates that the precession also increases to infinity as $\theta$ goes to zero.

# PROBLEMS

1. Determine the least spin about a vertical axis for a 50-cent coin by making the necessary measurements.   
2. Determine the equation for the least spin about the vertical diameter of a circular hoop of radius $R$ . Compare with that of a solid disk of same radius.   
3. Determine the least rolling velocity of a 50-cent coin.   
4. Determine the least rolling velocity of a circular hoop of radius $R$   
5.With $v _ { \xi } , v _ { \eta ^ { \prime } } ,$ $v _ { Z }$ given as in Fig.5.16-2,verify theaccelerations of Eqs.5.16-1, 5.16-12,5.16-13 as $\bf { a } _ { \tau } = [ \dot { \bf { v } } ] + \boldsymbol { \omega } \times \bf { v }$ where the components of $\boldsymbol { \omega }$ are $\omega _ { \xi } = \theta$ $\omega _ { \eta ^ { \prime } } = 0$ and $\omega _ { Z } = \dot { \psi }$

# Dynamics of Gyroscopic Instruments
