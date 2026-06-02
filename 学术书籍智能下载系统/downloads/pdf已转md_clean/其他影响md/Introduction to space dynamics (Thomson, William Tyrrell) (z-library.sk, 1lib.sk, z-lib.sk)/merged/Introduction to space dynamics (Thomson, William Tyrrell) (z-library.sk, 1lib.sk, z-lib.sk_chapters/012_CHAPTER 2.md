# CHAPTER 2

# 2.1 Velocity and Acceleration

The subject of kinematics is the study of motion. It is concerned with space and time, and with the time rate of change of vector quantities relating to the geometry of motion.

We consider first the motion of a point in a fixed coordinate system cyz. The position of a point $p$ which is in continuous motion along a curve such as $s$ in Fig. 2.1-1 is specified by its position vector r, the magnitude and direction of which are functions of time. In time $\Delta t _ { i }$ r changes to $\mathbf { r } + \Delta \mathbf { r } .$ and its velocity v is given by the time derivative,

$$
\mathbf { v } = \operatorname* { l i m } _ { \Delta t \to 0 } { \frac { ( \mathbf { r } + \Delta \mathbf { r } ) - \mathbf { r } } { \Delta t } } = \operatorname* { l i m } _ { \Delta t \to 0 } { \frac { \Delta \mathbf { r } } { \Delta t } } = { \frac { d \mathbf { r } } { d t } }
$$

The direction of v can be shown to coincide with the limiting direction of △r as it approaches zero, or the tangent to the curve $s$ at $P$ . By rewriting v in the form,

$$
\mathbf { v } = \operatorname* { l i m } _ { \Delta t \to 0 } { \frac { \Delta \mathbf { r } } { \Delta s } } { \frac { \Delta s } { \Delta t } }
$$

the limiting value of $\Delta \mathbf { r } / \Delta s$ is a unit vector along the tangent to the curve, so that the velocity can also be written as,

$$
\displaystyle \mathbf { v } = \frac { d s } { d t } \mathbf { 1 } _ { t }
$$

If $\mathbf { r }$ is represented in terms of its rectangular components, we obtain

$$
{ \bf r } = r _ { x } { \bf i } + r _ { y } { \bf j } + r _ { z } { \bf k }
$$

where $r _ { x } , r _ { y }$ and $r _ { z }$ are components of $\mathbf { r }$ along the fixed xyz coordinates, and i, j, and $\mathbf { k }$ are their corresponding unit vectors. Differentiating, we obtain

$$
\frac { d \mathbf { r } } { d t } = \dot { r } _ { z } \mathbf { i } + \dot { r } _ { y } \mathbf { j } + \dot { r } _ { z } \mathbf { k }
$$

where i, j, and $\mathbf { k }$ ,are treated as constants.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0001_pages_0001-0070/auto/images/047caaf2ce92d0ff6eba857568b1df678206f0b045c488a8b4ad617ca9b0bc0b.jpg)  
Fig. 2.l-l. Time rate of change of a vector r.

Aceleration is the time rate of change of velocity v,and by observing the vector change from v to $\mathbf { v } + \Delta \mathbf { v }$ in time $\Delta t$ , we obtain

$$
\mathbf { a } = \operatorname* { l i m } _ { \Delta t  0 } { \frac { ( \mathbf { v } + \Delta \mathbf { v } ) - \mathbf { v } } { \Delta t } } = \operatorname* { l i m } _ { \Delta t  0 } { \frac { \Delta \mathbf { v } } { \Delta t } } = { \frac { d \mathbf { v } } { d t } } = { \dot { v } } _ { x } \mathbf { i } + { \dot { v } } _ { y } \mathbf { j } + { \dot { v } } _ { z } \mathbf { k }
$$

# 2.2 Plane Motion (Radial and Transverse Components)

Consider a particle $p$ moving along a curve s fixed in a stationary Oxy plane, as shown in Fig. 2.2-1. The position of $p$ is established by the position vector

$$
{ \bf r } = r { \bf 1 } _ { r }
$$

where ${ \bf 1 } _ { r }$ is a unit vector which is always oriented along r.

Todeterminethevelocity of $P$ ，we differentite $\mathbf { r }$ , recognizing that $\mathbf { 1 } _ { r }$ changes in direction,

$$
{ \frac { d \mathbf { r } } { d t } } = { \dot { r } } \mathbf { 1 } _ { r } + r { \frac { d \mathbf { 1 } _ { r } } { d t } }
$$

The unit vector 1, is one of fixed magnitude which is rotating with angular velocity $\hat { \boldsymbol { \theta } }$ about an axis through the origin perpendicular to the xy plane. Its derivativeorits velocityis thecross product ofthe vectors $\varnothing$ and ${ \bf 1 } _ { r } ,$ which is a vector perpendicular to r, or

$$
\frac { d \mathbf { 1 } _ { r } } { d t } = \dot { \boldsymbol { \Theta } } \times \mathbf { 1 } _ { r } = \dot { \boldsymbol { \theta } } \mathbf { 1 } _ { \theta }
$$

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0001_pages_0001-0070/auto/images/68792365022c3c98f60a983b155262822638bf0efbbbc990cd20622e24290079.jpg)  
Fig. 2.2-1. Unit vectors ${ \bf 1 } _ { r }$ and ${ \bf \delta } _ { 1 } \ L _ { \theta }$ moving with r in the $x , y$ plane.

vhere ${ \bf 1 } _ { \theta }$ is a unit vector in the direction perpendicular to r.

Equation 2.2-2 may then be written as

$$
\begin{array} { c } { \frac { d \mathbf { r } } { d t } = \mathbf { v } = \boldsymbol { \dot { r } } \mathbf { 1 } _ { r } + \boldsymbol { \dot { \Theta } } \times \mathbf { r } } \\ { = \boldsymbol { \dot { r } } \mathbf { 1 } _ { r } + r \dot { \theta } \mathbf { 1 } _ { \theta } } \end{array}
$$

which expresses the velocity in terms of the radial and transverse components.

We can view this problem as that of a point $p$ moving along a set of rotating axes with direction ${ \bf 1 } _ { r }$ and $\mathbf { 1 } _ { \theta }$ . The point $p$ always moves along the ${ \bf 1 } _ { r }$ axis,and its relative velocity along it is $\dot { r }$ which corresponds to the first term of Eq. 2.2-4. The second term $\dot { \Theta } \times \mathbf { r }$ is the velocity of the coincident point $p$ due to rotation $\varnothing$ ·

The acceleration of $\boldsymbol { p }$ can be determined by differentiating Eq. 2.2-4.

$$
\mathbf { a } = { \ddot { \mathbf { r } } } = { \ddot { r } } \mathbf { 1 } _ { r } + { \dot { r } } { \frac { d \mathbf { 1 } _ { r } } { d t } } + ( r { \ddot { \theta } } + { \dot { r } } { \dot { \theta } } ) \mathbf { 1 } _ { \theta } + r { \dot { \theta } } { \frac { d \mathbf { 1 } _ { \theta } } { d t } }
$$

As before, the derivative of a unit vector rotates it $9 0 ^ { \circ }$ and multiplies it with its angular rate $\theta$ , so that

$$
{ \frac { d \mathbf { 1 } _ { \theta } } { d t } } = { \dot { \theta } } \times \mathbf { 1 } _ { \theta } = - { \dot { \theta } } \mathbf { 1 } _ { r }
$$

Thus Eq. 2.2-5 reduces to

$$
{ \bf a } = ( \bar { r } - r \dot { \theta } ^ { 2 } ) { \bf 1 } _ { r } + ( r \ddot { \theta } + 2 \dot { r } \dot { \theta } ) { \bf 1 } _ { \theta }
$$

which expresses the acceleration in terms of the radial and transverse components. We note here the term $2 { \dot { r } } { \dot { \theta } }$ ,which is known as the Coriolis acceleration, and which will be referred to again in the more general case.

# 2.3 Tangential and Normal Components

To resolve the acceleration into tangential and normal components, we start with Eq. 2.1-2.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0001_pages_0001-0070/auto/images/8fadbc32e22abe1c8a678fdfa0c56c7a6ab745092db3fdf53bdc33395c00f9bb.jpg)  
Fig. 2.3-l. Unit vectors ${ \bf 1 } _ { n }$ and $\mathbf { 1 } _ { t }$ moving along curve $s$ in $x , y$ plane.

$$
\mathbf { v } = \dot { s } \mathbf { 1 } _ { t }
$$

Differentiating and noting that

$$
\mathbf { i } _ { t } = \dot { \phi } \mathbf { 1 } _ { n }
$$

where ${ \bf 1 } _ { n }$ is a unit vector along the radius of curvature which is normal to the tangent to the curve $s$ at $P$ ,and $\dot { \phi }$ is the angular rate of the radius of curvature as shown in Fig. 2.3-1, we obtain

$$
\mathbf { a } = \tilde { s } \mathbf { 1 } _ { t } + \dot { s } \dot { \phi } \mathbf { 1 } _ { n }
$$

Since the length △s is related to the radius of curvature p and to the angle $\Delta \phi$ swept out by $\boldsymbol { \rho }$ ，

$$
\begin{array} { c } { \Delta s = \rho \Delta \phi } \\ { \dot { s } = \rho \dot { \phi } } \end{array}
$$

the acceleration,Eq.2.3-3caneexpresedinthefollowingaltate forms.

$$
\begin{array} { r } { \mathbf { a } = \breve { s } \mathbf { 1 } _ { t } + \frac { \breve { s } ^ { 2 } } { \rho } \mathbf { 1 } _ { n } } \\ { = \breve { s } \mathbf { 1 } _ { t } + \rho \breve { \phi } ^ { 2 } \mathbf { 1 } _ { n } } \\ { = \breve { s } \mathbf { 1 } _ { t } + \breve { \phi } \times \breve { \mathbf { \sigma } } \breve { s } } \end{array}
$$

# PROBLEMS

1. The position of a particle in a plane is given by the equations

$$
x = 6 t y = 4 t ^ { 2 }
$$

Determine the rectangular components of its velocity and acceleration as a function of time.

2.Aprojeilisdithsed $v _ { 0 }$ at an angle $\theta _ { 0 }$ above the horizon.Neglecting air friction and the rotation of the earth,the acceleration components are $a _ { y } = - g$ and $a _ { x } = 0$ Determine theequationfor its trajectory,therange $R$ ， and the maximum height $H _ { \ l }$

3. A rock is thrown at an angle of $4 5 ^ { \circ }$ with the horizontal, and it just clears a wall 24 ft high and $4 0 ~ \mathrm { f t }$ away. Determine the initial speed of the rock.

4. Find the greatest distance that a stone can be thrown inside a horizontal tunnel15fthigh withaninitial speedof 80ft/sec.Findalso thecorrespond-ing time of flight.

5. For a gun with a given muzzle speed $v _ { 0 }$ , show that a point $( x , y )$ can be hit by two different trajectories with initial elevation $\theta _ { 1 }$ and $\theta _ { 2 }$

6. Derive the equation for the envelope of a series of trajectories of a projectile fired with constant speed $v _ { 0 }$ and varying angles $\theta _ { 0 }$

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0001_pages_0001-0070/auto/images/6476ab3ae6f36a1abe281c9e6f35d4ec9d7431dd923b702d2f66a112cdfb4414.jpg)  
Prob.6

7. A point moves so that $r = 2 0 + 1 0 t$ and $\theta = 0 . 2 0 t ^ { 2 }$ Determine the radial and transverse components of the velocity and acceleration at $t = 2$ sec.

8. A spiral fixed in a plane is given by the equation r = 10eo.20. If a particle moves along the spiral according to the equation θ = 0.5t², determine the radial and transverse components of the velocity and acceleration at $t = 2 . 0$ sec.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0001_pages_0001-0070/auto/images/beffde2906e69d04f12e63d55ff79336237e70b3e756357821783308d21cfd89.jpg)  
Prob.8

9. In Prob. 8, determine the tangential and normal components of the velocity and acceleration, and compare the resultant for the two problems.

10. A particle moves along the circumference of a circle of radius $R$ at constant speed $v _ { 0 }$ ， Determine its radial and transverse velocity with respect to an origin on the circumference. Find the radial and transverse components of the acceleration and show that their resultant passes through the center of the circle.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0001_pages_0001-0070/auto/images/ca9f5b85a2f78f1bcfea0472364c21226c24a1f8349722f4c145c3b32416a60c.jpg)  
Prob.10

# 2.4 Plane Motion Along a Curve Rotating About 0 (Relative Motion)

A point $p$ moves along a curve s which is rotating with angular velocity w and angular acceleration @. We wil attach axes 1 and 2 to curve s so that 1, 2, and $s$ rotate together with ω and ω,as shown in Fig. 2.4-1.

The velocity of $p$ may be determined as follows. If the point $\boldsymbol { p }$ remained fixed on s, its velocity due to the angular velocity ω of the curve and attached coordinate axes is ω X r which is perpendicular to r. The motion of p along s results in an additional velocity dr/dt = s1t directed along the tangent to $s$ This latter component isthe velocity relative tothecurve s and can be determined as if the curve s were held stationary. Thus the sum of the above two components represents the velocity of point $p$

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0001_pages_0001-0070/auto/images/7ebb63f26d579972e0e4fa75a1e3a820cac3653b1604e8dff49418ee7bb71fe6.jpg)  
Fig. 2.4-l. Motion along a rotating curve s in a plane.

$$
\mathrm {  ~ v ~ } = \left[ \frac { d { \bf r } } { d t } \right] + \omega \times \mathrm {  ~ r ~ }
$$

$$
\mathbf { \mu } = \boldsymbol { s } \mathbf { 1 } _ { t } + \mathbf { \epsilon } \boldsymbol { \omega } \times \mathbf { r }
$$

and the above equation conforms to Eq. 1.6-3 for the derivative of a vector referenced to a rotating coordinate system.\*

The acceleration of point $p$ is determined by the derivative of v or of its two components in Eq. 2.4-1. Since the coordinates are rotating with angular speed $\boldsymbol { \omega }$ , the acceleration is given by the equation

$$
\mathbf { a } = \left[ \frac { d \mathbf { v } } { d t } \right] + \omega \times \mathbf { v }
$$

which can be interpreted in terms of the two components of v.

\* Differentiation relative to the moving coordinates is indicated by [].

Considering first the component $\dot { s } \mathbf { 1 } _ { t }$ ,if the curve is held stationary and $p$ is allowed to move along it, the acceleration relative to the curve $s$ would be

$$
\displaystyle { \bar { s } } \mathbf { 1 } _ { t } + { \frac { \dot { s } ^ { 2 } } { \rho } } \mathbf { 1 } _ { n }
$$

as in Eq. 2.3-5. The rotation of the coordinate system at a rate $\boldsymbol { \omega }$ introduces an additional term

$$
\mathbf { \omega } _ { \mathbf { \omega } } \times \mathbf { \omega } _ { i } \mathbf { 1 } _ { t }
$$

which is normal to ${ \dot { s } } \mathbf { 1 } _ { t }$ . Thus we obtain three components of acceleration from the tangential velocity vector.

The remaining velocity vector w $\times$ r is treated similarly. Relative to the coordinates we have

$$
{ \begin{array} { r } { \left[ { \frac { d } { d t } } \left( { \boldsymbol { \omega } } \times { \bf r } \right) \right] = { \boldsymbol { \omega } } \times { \dot { \bf r } } + { \dot { \boldsymbol { \omega } } } \times { \bf r } } \\ { = { \boldsymbol { \omega } } \times { \dot { s } } { \bf 1 } _ { t } + { \dot { \boldsymbol { \omega } } } \times { \bf r } } \end{array} }
$$

The rotation of the coordinates introduces the additional component

$$
\boldsymbol { \omega } \propto \left( \boldsymbol { \omega } \times \boldsymbol { \nu } \right)
$$

which is directed towards the negative r direction.

Summing all these terms, we have

$$
\begin{array} { l } { { \displaystyle { \bf { a } } = \left( { \tilde { s } } { \bf { 1 } } _ { t } + \frac { { \dot { s } } ^ { 2 } } { \rho } { \bf { 1 } } _ { n } \right) + ( { \dot { \omega } } \times { \bf { r } } + \omega \times \omega \times { \bf { r } } ) + 2 \omega \times { \dot { s } } { \bf { 1 } } _ { t } } \ ~ } \\ { { \displaystyle ~ = \left( { \tilde { s } } { \bf { 1 } } _ { t } + \frac { { \dot { s } } ^ { 2 } } { \rho } { \bf { 1 } } _ { n } \right) + ( { \dot { \omega } } r { \bf { 1 } } _ { \theta } - r \omega ^ { 2 } { \bf { 1 } } _ { \tau } ) + 2 \omega { \dot { s } } { \bf { 1 } } _ { n } } } \end{array}
$$

In this equation the first two terms represent the acceleration of $p$ relative to the curve $s$ .The next two terms represent the acceleration of the coincident point due to angular velocity and angular acceleration of the coordinate system and the curve s fixed to it. The last term is known as the Coriolis acceleration, and it is perpendicular to the relative velocity $\dot { s } \mathbf { 1 } _ { t }$ The various components of Eq. 2.4-7 are shown in Fig. 2.4-1.

# 2.5 General Case of Space Motion

We now consider the general case of the motion of a particle p moving with respect toarigid body whichis itself in motion withrespecttoafied coordinate system, as shown in Fig. 2.5-1.

We will designate the fixed coordinate system by capital lettrs X, Y,Z, and attach a set of axes x, y, z on the moving body, calling them the body axes. Thus the motion of the rigid body is established by the motion of the origin of the body axes x, y, z, and a rotation w with respect to XYZ. The vector ω will, in general, vary in magnitude and direction, both of which can be referenced with respect to the fixed X, Y, Z axes. Thus the absolute motion of the particle p, referred to the X, Y, Z axes, will be equal to the motion of the particle relative to the body axes x, y, z (or the body itself) plus the motion of the coincident point (a point on the body momentarily coinciding with $p$ ),which is further equal to the motion of the moving origin and the additional motion of the coincident point due to rotations w and ω.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0001_pages_0001-0070/auto/images/56f58fb5e95551f7b398ce314a575fff3ccf1cbd2205402c8992832c5a8cecc9.jpg)  
Fig. 2.5-l. General case of space motion in terms of body axes x, y, z, and inertial axes X, Y, Z.

To visualize the motion, let the motion of the particle $p$ with respect to the rigid body be indicated along a curve s fixed in the body. Thus, this curve is also fixed with respect to the body axes x, y,z. An observer sitting on the body would see only the motion of $p$ along the curve $s$

Let the position of $p$ relative to the $x$ ，y， $z$ axes be represented by the vector

$$
{ \bf r } = x { \bf i } + y { \bf j } + z { \bf k }
$$

wherei,j,and k are unit vectors along $x , y , z ,$ and, hence, must be treated as

variables due to their changing direction. If we differentiate r, we will obtain

$$
{ \dot { \mathbf { r } } } = [ { \dot { x } } { \dot { \mathbf { i } } } + { \dot { y } } { \dot { \mathbf { j } } } + { \dot { z } } { \mathbf { k } } ] + \left( x { \frac { d { \mathbf { i } } } { d t } } + y { \frac { d { \mathbf { j } } } { d t } } + z { \frac { d { \mathbf { k } } } { d t } } \right)
$$

Since $d \mathbf { i } / d t = \mathbf { \omega } \times \mathbf { \gamma }$ i, $d { \bf j } / d t = { \bf { \omega } } \times { \bf { \sigma } } .$ i， $d { \bf k } / d t = \omega \times { \bf k }$ ，this expression can be written as

$$
\begin{array} { l } { \dot { \mathbf { r } } = [ \dot { x } \mathbf { i } + y \mathbf { j } + \dot { z } \mathbf { k } ] + \mathbf { \omega } \times ( x \mathbf { i } + y \mathbf { j } + z \mathbf { k } ) } \\ { = [ \dot { \mathbf { r } } ] + \mathbf { \omega } \times \mathbf { \omega } \ \mathbf { r } } \end{array}
$$

Interpreting this equation,the first term[r]represents differentiation holding i, j,k cotatd,ce,is he vlityof $p$ relative to the rotating $x , y , z$ axes,or the velocity which an observer stationed on the $x$ ，y， $z$ axes is able to detect as the particle moves along the curve $s$ . The second term ω X r is the velocity of the coincident point relative to the origin, due to rotation ω. Finally, we add to the above the velocity ${ \bf { v } } _ { o }$ of the moving origin, in which case the absolute velocity of $p$ becomes

$$
\mathbf { \nabla } \mathbf { v } = \mathbf { v } _ { o } + [ \dot { \mathbf { r } } ] + \boldsymbol { \omega } \times \mathbf { r }
$$

To determine the acceleration, we start with the velocity †, of Eq. 2.5-3, relative to the moving origin, and differentiate once more

$$
{ \begin{array} { r } { { \ddot { \mathbf { r } } } = [ { \ddot { x } } \mathbf { i } + y \mathbf { j } + { \ddot { z } } \mathbf { k } ] + { \boldsymbol { \omega } } \times [ { \dot { x } } \mathbf { i } + y \mathbf { j } + { \dot { z } } \mathbf { k } ] } \\ { + { \dot { \boldsymbol { \omega } } } \times ( x \mathbf { i } + y \mathbf { j } + z \mathbf { k } ) + { \boldsymbol { \omega } } \times [ { \dot { x } } \mathbf { i } + y \mathbf { j } + { \dot { z } } \mathbf { k } ] } \\ { + { \boldsymbol { \omega } } \times { \boldsymbol { \omega } } \times ( x \mathbf { i } + y \mathbf { j } + z \mathbf { k } ) \quad \quad ( 2 . 9 \mathbf { k } + x \mathbf { i } + y \mathbf { j } ) } \end{array} }
$$

The first two terms result from the differentiation of the first term $[ \dot { x } \mathbf { i } + \mathbf { \partial }$ ${ \dot { y } } { \mathbf { j } } + { \dot { z } } { \mathbf { k } } ]$ ， whereas the differentiation of the second term w $\mathbf { \boldsymbol { \times } }$ $( x \mathbf { i } + y \mathbf { j } +$ zk)results in the remaining three terms. We can now group these terms together as

$$
\ddot { \mathbf { r } } = [ \mathbf { a } ] + \boldsymbol { \omega } \times \boldsymbol { \omega } \times \mathbf { r } + \dot { \boldsymbol { \omega } } \times \mathbf { r } + 2 \boldsymbol { \omega } \times [ \mathbf { v } ]
$$

where $[ \mathfrak { v } ] = [ \dot { \mathfrak { r } } ] = [ \dot { x } \mathfrak { i } + \dot { y } \mathfrak { j } + \dot { z } \mathbf { k } ]$ is the velocity of $p$ relative to the body axes

$[ \mathbf { a } ] = [ \ddot { x } \mathbf { i } + \ddot { y } \mathbf { j } + \ddot { z } \mathbf { k } ]$ is the acceleration of $p$ relative to the body axes

We now add the acceleration ${ \bf a } _ { 0 }$ of the origin, to $\ddot { \mathtt { r } }$ to obtain the total acceleration

$$
{ \mathrm {  ~ a ~ } } = { \mathrm {  ~ a _ { 0 } ~ } } + \left[ { \mathrm {  ~ a ~ } } \right] + { \boldsymbol { \omega } } \times { \boldsymbol { \omega } } \times { \mathrm {  ~ r ~ } } + { \dot { \boldsymbol { \omega } } } \times { \mathrm {  ~ r ~ } } + 2 { \boldsymbol { \omega } } \times \left[ { \mathrm {  ~ v ~ } } \right]
$$

The terms $\omega \times \omega \times 1$ and @ X r are the acceleration of the coincident point and $2 \infty \times$ [v] is the Coriolis acceleration which is directed normal to the plane containing the vectors ω and relative velocity [v], as given by the three-finger rule.

The vector Eqs. 2.5-4 and 2.5-7 are in the most compact form for defining the generalcase of space motion. Allspecialcasescanbededuced directly from these equations.

# PROBLEMS

1. A wheel having a 2-ft radius rolls on a belt which is moving to the right with a speed of 1 ft/sec. To an observer standing on the ground,the center of the wheel appears to move to the left with a speed of 3 ft/sec. Determine the velocity of point $P$

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0001_pages_0001-0070/auto/images/c7fbcbbef7cc4402b5e938029ddbd342abf28e367d9210749779681f11364a79.jpg)  
Prob. I

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0001_pages_0001-0070/auto/images/cf48fda42054f5142480a0c45e289a1b67163a4bb52f0864ca7b1246130fc799.jpg)  
Prob.2

2. At a given instant, bar $_ { A C }$ is horizontal and bar $\mathcal { D B }$ has an angular velocity of 3 rad/sec clockwise and angular acceleration of $2 \ r a d / \sec ^ { 2 }$ counterclockwise. Determine the velocity of the slider $B$ relative to bar $_ { A C }$ and the angular velocity and angular acceleration of $_ { A C }$   
3.Pin $P$ which slides on arm $o c$ is made to move along the slot $A B$ in a disk. If the disk is held stationary and $o c$ has an angular velocity of 3 rad/sec clockwise, when $\theta = 3 0 ^ { \circ }$ ,determine the velocity of $p$ relative to $o c$ and also its absolute velocity.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0001_pages_0001-0070/auto/images/4af94c78a2bc15eef275147f5b33118beb578aa369576b93636c9e4b99edea25.jpg)  
Prob.3

4. Determine the absolute acceleration of $p$ of Prob. 3if, in addition to the data given,the arm OC has an angular acceleration of 4 rad/sec² in the counterclockwise direction. Specify all its components.

5. If in Probs. 3 and 4 the data given are relative to the disk which is rotating with angular velocity and acceleration of 2 rad/sec and 4 rad/sec² both clock-wise, determine the absolute velocity and acceleration of $P$

6. A particle moves with velocity $k r$ outward along a spoke of a wheel rotating with angular speed $\dot { \theta }$ and angular acceleration $\ddot { \theta }$ .Determine its absolute velocity and acceleration, identifying each component by a diagram.

7. An airplane travels overhead at constant altitude $h$ and constant horizontal speed $v$ Determine the angular velocity $\dot { \theta }$ and angular acceleration $\ddot { \theta }$ of the lineof sight ofa trackingdevice on the ground,where $\theta$ is the angle measured from zenith. How fast is the distance to the plane increasing at $\theta$

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0001_pages_0001-0070/auto/images/c1e5f15716a9ccaac7f7b0ba569cabeec8f80f134b31780659893392d3589c10.jpg)  
Prob.7

8. A bomber flying at constant speed $v _ { b }$ and constant altitude $h _ { b }$ sees an enemy plane flying in the same direction with velocity $v _ { e }$ and at a lower altitude $h _ { e }$ Assuming that $v _ { b } > v _ { e }$ , show that the angle $\theta$ of the line of sight at the instant at which the bomb should be released must be

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0001_pages_0001-0070/auto/images/0821e2e314323955c1a5f3e808a8a53ad561221e9dcee7d33f327c55c335a7d2.jpg)  
Prob.8

9.An airplane traveling at constant altitude h and constant speed v is observed by a radar station a distance s from the vertical plane of travel of the airplane. Determine the angular velocity of the radar dish about the horizontal and vertical axes from the instant when the plane is closest to the station.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0001_pages_0001-0070/auto/images/e88c95ffb163b5ab680f680ada6ca88de45a55f1d0cc0cc21aaec09277cf7d3f.jpg)  
Prob.9

10. In Prob. 9 determine the angular rates if $v = 4 5 0 \mathrm { m p h }$ ， $h = 1 2 , 0 0 0 \mathrm { f } \mathrm { t } _ { ; } s =$ $\%$ mile,and $t = 1 5$ sec.

11. Fuel flows out along the impeller blade of a turbo pump at a speed of 100 ft/sec and acceleration of $1 2 0 ~ \mathrm { f t / s e c ^ { 2 } }$ relative to the blade. If the turbo wheel is running clockwise at $2 4 0 0 \mathrm { r p m }$ ,determinetheabsolutevelocityandacceleration of the fuel just before it leaves the impeller.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0001_pages_0001-0070/auto/images/37452b4660f7b8ebfc8822111eb0a58947589c2bccd03991412d95ee152863ec.jpg)  
Prob.I1

12. The large wheel of the quick-return mechanism rotates in the counterclockwise direction at a constant speed of 120 rpin. Determine the velocity of point p as a function of the angle 0 and the relative velocity of the slider $s$

13. Determine the angular acceleration of the arm $O p$ of Prob.12 when the crank arm makes an angle $3 0 ^ { \circ }$ with the horizontal in the first quadrant.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0001_pages_0001-0070/auto/images/fe371deaba91c41f30572b782a8622258f1342edb5529aaf2706abd0e52c5b94.jpg)  
Prob.12

14. A bomber traveling with constant speed v at constant altitude h spots an enemyplaneata loweraltitude $h _ { e }$ and traveling along a line perpendicular to his. Assuming $h _ { e }$ and $v _ { e }$ to be constant, determine how far ahead of the intersecting vertical and perpendicular planes the bomb should be released.   
15. A satellite ina S-to-Npolar orbit of $1 2 0 ~ \mathrm { { m i n } }$ is observed to travel from horizon to horizon in $2 5 ~ \mathrm { { m i n } }$ and pass directly over an observation station at latitude $3 5 ^ { \circ } \bf N$ . Determine the direction of the path of the satellite relative to the meridian plane passing through the station.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0001_pages_0001-0070/auto/images/ab2bc3cb0390ae4218b6e8e84dc3e019b356d3a15bac0eb66fbfd791abf419e2.jpg)  
Prob. I5

16. A satellte traveling in a circular polar orbit of altitude $h$ around the earth has a period of $1 2 0 ~ \mathrm { { \bar { m i n } } }$ .An observer on theearth'ssurface tracks the satelite and finds that it is moving at a rate of $1 5 ^ { \circ } / \mathrm { m i n }$ when directly overhead. Determine its altitude $h$

# 2.6 Motion Relative to the Rotating Earth

The center of the earth as it moves around the sun is accelerating toward the sun. We, however, neglect this acceleration and place a set of nonrotating axes with origin at the earth's centeras an inertial system.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0001_pages_0001-0070/auto/images/b964cee6a6cf8efa40b481878d2b804c52a4b985d3a67bc5b7760cc30484a409.jpg)  
Fig. 2.6-l. Motion relative to earth using axes $x$ y, z fixed to earth's surface.

We are often interested in the motion of a body relative to the earth's surface. Placing a set of axes at a given point $O$ on the earth's surface, we orient the $z$ axis along the plumb line which,for simplicity, we assume to be equal to the geocentric line. The $x$ and the $y$ axes then lie in the horizontal plane, and we orient $_ x$ along the meridian plane pointing south and y along the latitude line pointing east as shown in Fig. 2.6-1.

The acceleration of $O$ is $\Omega \times \Omega \times \mathbb { R } = - ( \Omega ^ { 2 } R$ sin λ cos λ)i - $( \Omega ^ { 2 } R \cos ^ { 2 } \lambda ) \mathbf { k }$ where the angular velocity of the earth-fixed coordinate system $_ x$ ， $_ y$ ， $z$ is $\pmb { \Omega }$ ,the earth's rotational velocity with components:

$$
\pmb { \Omega } = - ( \Omega \cos \lambda ) \mathbf { i } + ( \Omega \sin \lambda ) \mathbf { k }
$$

The acceleration relative to the inertial system is

$$
\mathbf { a } = { \frac { \mathbf { F } } { m } } = { \boldsymbol { \Omega } } \times { \boldsymbol { \Omega } } \times \mathbf { R } + [ { \boldsymbol { \mathbf { a } } } ] + { \boldsymbol { \Omega } } \times { \boldsymbol { \Omega } } \times { \boldsymbol { \mathbf { r } } } + 2 { \boldsymbol { \Omega } } \times [ { \boldsymbol { \mathbf { v } } } ]
$$

If the only force acting on the body is its weight, then $\mathbf { F } / m = - g \mathbf { k } ,$ and the

acceleration [a] relative to the rotating earth is

$$
[ \mathbf { a } ] = - g \mathbf { k } - \Omega \times \Omega \times \textrm { R } - \Omega \times \Omega \times \textrm { r } - 2 \Omega \times [ \nabla ]
$$

Since $\Omega ^ { 2 }$ is $( 0 . 7 2 9 \times 1 0 ^ { - 4 } \mathrm { r a d / s e c } ) ^ { 2 }$ , it can be neglected, leaving

$$
[ \dot { \mathbf { a } } ] = - g \mathbf { k } - 2 \boldsymbol { \Omega } \times [ \mathbf { v } ]
$$

Displacements relative to the earth can be found by two integrations of Eq. 2.6-4. expressed in terms of the $x , y ,$ and $z$ components.

# PROBLEMS

1. Determine, due to the earth's rotation, the angular deviation of a plumb line from the geocentric line at latitude $\lambda ^ { \circ } \mathbf { N }$ .At what latitude is this deviation a maximum?   
2. A particle is dropped from rest at a height of 1 mile at latitude $3 2 ^ { \circ } \bf N$ Neglecting air friction and using the $_ x$ ， $y$ , z coordinate system of Fig. 2.6-1,determine where the particle will land.   
3.A bullet is fired vertically at a latitude of ${ \bf 5 0 ^ { \circ } N }$ with a muzzle speed of 2000 ft/sec. Neglecting air friction, determine the landing point of the bullet.   
4. A rocket is fired vertically upward at a point on the earth's surface of latitude $\lambda ^ { \circ } \mathbf { N }$ Determine the Coriolis deviationat its maximum height h. What is the numerical value of this deviation if $h = 1 5 0$ miles and $\lambda = 3 5 ^ { \circ } \mathrm { ~ N ~ }$   
5. In Prob. 4, determine the Coriolis deviation during the downward flight and compare it with that at maximum height. (Caution: Initial lateral velocity for downward flight is not zero.)   
6. An airplane is traveling with speed $v$ due south with constant altitude at latitude $\lambda ^ { \circ } \mathbf { N }$ Determine the Coriolis acceleration relative to earth.   
7. At latitude $\lambda ^ { \circ } \textbf { S }$ a projectile is fired with speed $v _ { 0 }$ in the east-west vertical plane at an elevation $\theta _ { 0 }$ in the easterly direction. Determine the latitude deviation.

# Transformation of Coordinates
