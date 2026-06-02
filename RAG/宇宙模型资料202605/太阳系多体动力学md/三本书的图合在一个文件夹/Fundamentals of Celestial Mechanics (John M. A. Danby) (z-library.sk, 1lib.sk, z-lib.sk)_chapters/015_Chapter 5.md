# Chapter 5

# Some Properties of Solid Bodies

# 5.1 Center of Mass and Center of Gravity

Consider a system of point masses of which the ith has mass $\pmb { \mathcal { W } } _ { 3 }$ and position vectorr: with respect to any origin. The center of mass of the system is defined to be at the point $\pmb { \bar { \Sigma } }$ where

$$
\overline { { \mathfrak { x } } } = \frac { \sum m _ { i } \mathfrak { x } _ { i } } { \sum m _ { i } } ,
$$

and the summation extends over all members of the system. By the vector definition this point is independent of the orientation of the axes;we have to show that it is also independent of the position of the origin. Let the origin be transferred to $\pmb { \Sigma } ^ { \prime }$ ：then the position vectors with respect to the new origin are r=ri-r', so that the center of mass with respect to this new origin is at

$$
\begin{array} { c } { { \overline { { { \bf { z } } } } ^ { \prime } = \frac { { \displaystyle \sum m _ { i } ( { \bf r } _ { i } - { \bf r } ^ { \prime } ) } } { { \displaystyle \sum m _ { i } } } } } \\ { { { \overline { { { \bf { z } } } } ^ { \prime } - { \bf r } ^ { \prime } } } } \end{array}
$$

which is the same point as that found with respect to the first origin. This means that the center of mass is independent of the reference system and depends only on the configuration of the masses.

The center of gravity， $\Sigma _ { g }$ ,is defined such that the sum of the moments of the forces ${ \mathfrak { M } } _ { \mathrm { i } } { \mathfrak { E } }$ acting at $\pmb { \Sigma } _ { 2 }$ is equal to the moment of the combined masses, $\sum m _ { i }$ acting at $\pmb { \tau } _ { g } .$ i.e.,

$$
\mathbf { r } _ { g } \times \mathbf { g } \sum m _ { i } = \sum ( \mathbf { r } _ { i } \times \mathbf { g } \textcircled { n _ { i } } ) .
$$

The general solution of this equation for $\Xi _ { g }$ is

$$
{ \bf r } _ { g } = \frac { \sum \bar { \bf z } i \mathcal { M } i } { \sum \mathcal { m } _ { i } } + \bar { \bf k } { \bf g } = \bar { \bf z } + \bar { \bf k } { \bf g } ,
$$

where $\Bbbk$ is an arbitrary scalar. To be useful, this point must depend only on the configuration of the masses and not on the direction of $\pmb { \mathrm { g } }$ so that $\ k = 0$ and

$$
\pmb { \mathrm { z } } _ { g } = \pmb { \mathrm { \tilde { z } } } .
$$

These definitions are for systems of point masses. One purpose of this chapter is to break away from the use of abstract point masses so that we can apply the laws of mechanics to solid bodies. The generalization here is simple: we replace the summation signs by integral signs, to give

$$
\overline { z } = \frac { \int \pi d \gamma \pi } { \int d \gamma \pi }
$$

integrated over the whole body. If $\pmb { \rho }$ is the density and du is an element of volume, then we have ${ \vec { a } } \gamma _ { i } = \rho$ du. Provided the density is finite everywhere, there is no difficulty over the convergence of the integral.

If a solid is symmetrical about some plane (for instance if the plane is the xy-plane,the distribution of mass would be independent of the sign of $z$ ，then that plane is called a plane of symmetry. By symmetry the center of mass of the body must lie in that plane. In general, three planes meet in a point, so that if a body has three planes of symmetry,the center of mass is found. It may be that the three planes meet in a line; in this case there is still some ambiguity and integration must be used.But all the bodies considered here will be spheres or,at worst,ellipsoids,for which the center of mass is immediately seen to be the geometrical center.

# 5.2The Moments and Products of Inertia - The Inertia Tensor

In order to discuss the angular momentum of a solid body, we need some quantities known as the moments and products of inertia. In considering these, we shall, for convenience, introduce the inertia tensor. Tensor notation will be used only in this section and will be developed only as far as is needed for the purpose in hand.

Consider coordinates $\left( \mathfrak { x } _ { 1 } , \mathfrak { x } _ { 2 } , \mathfrak { x } _ { 3 } \right)$ instead of $\{ x , y , z \}$ .We shalluse the dummy $\sin \beta \pi \sqrt { \pi } x$ notation where,if a suffx appears twice in a term, then the term is summed over the (three) possible values of the suffix.Thus $a _ { i } x _ { j }$ means precisely what it says, but $a _ { i } x _ { i }$ stands for

$$
\sum _ { i = 1 , 2 , 3 } a _ { i } x _ { i } \quad \circ \dag \quad ( a _ { 1 } x _ { 1 } + a _ { 2 } x _ { 2 } + a _ { 3 } x _ { 3 } ) .
$$

Although the results will be applied to continuous solids, we shall, for convenience, continue to use summations over mass elements. These can easily be replaced by integrals.

Define the six quantities $\bar { \pmb { \mathscr { Z } } } _ { \dot { \pmb { \mathscr { Z } } } }$ by

$$
\begin{array} { r l } & { I _ { 1 1 } = \sum m x _ { i } x _ { i } - \sum m x _ { 1 } ^ { 2 } = A , } \\ & { I _ { 2 2 } = \sum m x _ { i } x _ { i } - \sum m x _ { 2 } ^ { 2 } = B , } \\ & { I _ { 3 3 } = \sum m x _ { i } x _ { i } - \sum m x _ { 3 } ^ { 2 } = C , } \\ & { I _ { 2 3 } = - \sum m x _ { 2 } x _ { 3 } \qquad = - F , } \\ & { I _ { 3 1 } = - \sum m x _ { 3 } x _ { 1 } \qquad = - G , } \\ & { I _ { 1 2 } = - \sum m x _ { 1 } x _ { 2 } \qquad = - H . } \end{array}
$$

$A , B ,$ and $\pmb { C }$ are the moments of inertia and $\pmb { \xi }$ ： $G$ and $H$ are the products of inertia of the system of masses. They can all be given by the one equation

$$
\tilde { I } { _ { \alpha \beta } } = \sum m x _ { i } x _ { i } \delta _ { \alpha \beta } - \sum m x _ { \alpha } x _ { \beta } ,
$$

where $\delta _ { \alpha \beta }$ ,called the Kronecker delta,is zero if $\pmb { \mathcal { Q } }$ and $\beta$ are unequal and is one if they are equal.

Let the system have angular velocity $\omega$ so that the velocity of the mass element $\boldsymbol { \mathcal { T } } _ { \mathcal { X } } ^ { 2 }$ at $\mathfrak { X }$ is $\omega \times \mathfrak { T }$ andits angular momentumabout the origin is $\yen 123,456$ $( \omega \times \tt { r } )$ .The total angular momentum of the system about the origin is, then,

$$
\begin{array} { l } { \frac { \kappa } { \Delta \Sigma } = \displaystyle \sum m \mathbf { r } \times \left( \boldsymbol { \omega } \times \mathbf { r } \right) } \\ { = \displaystyle \sum m [ r ^ { 2 } \boldsymbol { \omega } - ( \mathbf { r } \cdot \boldsymbol { \omega } ) \mathbf { r } ] } \\ { = \displaystyle \sum m [ x _ { i } x _ { i } \boldsymbol { \omega } - ( x _ { i } \boldsymbol { \omega } _ { i } ) \mathbf { r } ] . } \end{array}
$$

Resolving along the component directions,we see that the $\mathcal { X } 1$ component is

$$
\begin{array} { r } { \mathcal { H } _ { 1 } = \bar { j } _ { 1 1 } \omega _ { 1 } + \bar { j } _ { 1 2 } \omega _ { 2 } + \bar { j } _ { 1 3 } \omega _ { 3 } = \bar { j } _ { 1 i } \omega _ { i } . } \end{array}
$$

Then,using matrix notation, we have

$$
\{ H _ { 1 } \ H _ { 2 } \ H _ { 3 } \} = \{ \omega _ { 1 } \ \omega _ { 2 } \ \omega _ { 3 } \} \left[ \begin{array} { l } { I _ { \pm 1 } \ I _ { 1 2 } \ J _ { 1 3 } } \\ { I _ { 2 \bar { 1 } } \ I _ { 2 2 } \ I _ { 2 3 } } \\ { I _ { 3 \bar { 1 } } \ I _ { 3 2 } \ I _ { 3 3 } } \end{array} \right]
$$

where $\underline { { \vec { \imath } } } _ { \alpha \beta } = \underline { { \vec { \imath } } } _ { \beta \alpha }$

The matrix I has been defined with respect to a particular set of axes, but from(5.2.3） we might expect it to have some existence,similar to that of $\mathtt { a }$ vector,that is independent of the system of reference. This is the case. I is an example of a tensor of rank two.The operative definition (from Milne's Vectorial Mechanics,Ref.8) is as follows:

With each set of orthogonal triads of unit vectors associate a set of nine mumbers, $\ddagger _ { \flat } =$ Then the sets are said to describe a tensor, $\pmb { \Sigma }$ provided that if $\ddagger _ { \mu \vartriangle }$ isassociated with the triad $( \hat { \bf 1 } _ { 1 } , \hat { \bf 3 } _ { 2 } , \hat { \bf 3 } _ { 3 } )$ and $z _ { \mu v } ^ { \prime }$ is the set associated with $( \hat { \bf z } _ { 1 } ^ { t } , \hat { \bf z } _ { 2 } ^ { t } , \hat { \bf z } _ { 3 } ^ { t } )$ ,then

$$
\begin{array} { r } { \vec { \mathfrak { L } } _ { \beta \mathfrak { v } } ^ { \beta } = \vec { \mathfrak { L } } _ { \beta \mathfrak { e } } \vec { \mathfrak { L } } _ { \vartheta } \vec { \mathfrak { L } } _ { \alpha } \beta , } \end{array}
$$

where

$$
\begin{array} { r } { \check { \check { \iota } } _ { \rho \sigma } = \hat { \check { \mathfrak { z } } } _ { \rho } ^ { t } \cdot \hat { \check { \mathfrak { z } } } _ { \sigma } . } \end{array}
$$

[The/'s are the direction cosines of the new set of axes with respect to the old set.] According to this definition we cannot describea tensor without reference to some triad,but the tensor itself is to be distinguished from any one of its descriptions.Just as a vector may be considered as the class ofall its representations with respect to different triads,so a tensor is the class of all its descriptions.

To prove that $[ I ]$ is a tensor, use (5.2.3), written in the form

$$
\tilde { \lambda } _ { \beta } ^ { \mp } = \omega _ { \alpha } \bar { \lambda } _ { \alpha \beta } .
$$

With respect to the new triad we have

$$
\begin{array} { r } { \mathbb { H } _ { \beta } ^ { \prime } = \omega _ { \alpha ^ { \pm } \alpha \beta } ^ { \prime } . } \end{array}
$$

Now $\mathbf { \overrightarrow { x } }$ and $\omega$ are vectors.

$$
\mathbf { H } = H _ { 1 } \hat { \mathbf { i } } _ { 1 } + H _ { 2 } \hat { \mathbf { i } } _ { 2 } + H _ { 3 } \hat { \mathbf { i } } _ { 3 } = H _ { \alpha } \hat { \mathbf { i } } _ { \alpha }
$$

and

$$
\begin{array} { r } { \frac { \mp \pi ^ { \prime } } { \tilde { z } ^ { \frac { \prime } { 2 } } } = \bar { H } _ { \alpha } ^ { \prime } \hat { \bar { z } } _ { \alpha } ^ { \prime } . } \end{array}
$$

Also

$$
\hat { \bf \widehat { \bf 1 } } _ { 1 } ^ { t } = \bar { \bar { \imath } } _ { 1 1 } \hat { \bar { \bf 1 } } _ { 1 } + \bar { \bar { \imath } } _ { 1 2 } \hat { \bar { \bf 1 } } _ { 2 } + \bar { \bar { \imath } } _ { 1 3 } \hat { \bar { \bf \ k } } _ { 3 } , \quad \mathrm { e t }
$$

So we have

$$
H _ { \beta } ^ { \prime } = H _ { \beta } ; H _ { i }
$$

and similarly,

$$
\omega _ { \alpha } ^ { \prime } = \mathbb { i } _ { \alpha \mathrm { i } } \omega _ { \mathrm { i } } .
$$

Therefore

$$
\begin{array} { r l } & { \omega _ { \alpha } ^ { \prime } \bar { L } _ { \alpha \beta } ^ { \prime } = \bar { H } _ { \beta } ^ { \prime } } \\ & { \qquad = \bar { l } _ { \beta i } \bar { H } _ { i } } \\ & { \qquad = \bar { l } _ { \beta i } { \omega _ { j } } \bar { I } _ { j i } } \\ & { \qquad = \bar { l } _ { \beta i } \bar { l } _ { j k } \bar { I } _ { j i } { \omega _ { k } ^ { \prime } } } \end{array}
$$

By changing the dummy suffixes, this can be put into the form

$$
\omega _ { \alpha } ^ { i } ( \bar { i } _ { \alpha \beta } ^ { \prime } - \bar { i } _ { \beta i } \bar { i } _ { i \alpha } \bar { j } _ { \bar { 3 } \beta } ) = 0 ,
$$

and since this holds for any $\omega _ { \alpha } ^ { \beta }$ , the result is established.

It would be profitable but,unfortunately,not to the point, to devote much more space to a discussion of tensors. The interested reader will be able to find out more about tensors elsewhere. It is important to realize that tensors are quantities obeying certain laws of transformation when the reference system is changed; these are such that a tensor equation which is true in one reference system is true in any reference system.

The product $x _ { i } I _ { i j }$ will be denoted by $\mathbf { x } \cdot \mathbf { \vec { z } }$ ；it is an inner product of the vector and the tensor.Since $\underline { { \vec { \jmath } } } _ { \alpha , \beta } = \underline { { \vec { \jmath } } } _ { \beta \alpha } ,$ $\pmb { \Sigma }$ issaid to bea self-conjugate tensor.

When considering the rotation of a body about some axis,it is necessary to know the moment of inertia of the body about that axis.Let OS,the axis of rotation,pass through the origin,and let Pbea mass element m.Then the angular momentum about Os is

$$
\sum \omega m \mathcal { P } \mathcal { R } ^ { 2 } ,
$$

where $\mathcal { P R }$ is the perpendicular distance of $P$ from $o s$ and $\omega$ is the angular velocity. The moment of inertia about $o s$ is $\sum \gamma _ { i } P R ^ { 2 }$

![](../chunks/Fundamentals of Celestial Mechanics (John M. A. Danby) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0041-0080/ocr/images/8a75e7487eba91446033dd19ea4fb1103a4895b358a14ece22a097d053b69a40.jpg)  
Figure 5.1

Let usreturn for a moment to more familiar notation,such that the direction $o s$ is $\{ \vec { \mathfrak { k } } , \mathfrak { M } , \mathfrak { n } \}$ and the coordinates of $\mathcal { P }$ are $\{ x , y , z \}$ .Then

$$
\begin{array} { r l } & { P R ^ { 2 } = O P ^ { 2 } - O R ^ { 2 } } \\ & { \qquad = ( x ^ { 2 } + y ^ { 2 } + z ^ { 2 } ) - ( l x + m y + n z ) ^ { 2 } } \\ & { \qquad = ( x ^ { 2 } + y ^ { 2 } + z ^ { 2 } ) ( l ^ { 2 } + m ^ { 2 } + n ^ { 2 } ) - ( l x + m y + n z ) ^ { 2 } , } \end{array}
$$

$$
\sum m P R ^ { 2 } = A l ^ { 2 } + B m ^ { 2 } + C \boldsymbol { n } ^ { 2 } - 2 F m n - 2 G n l - 2 H l m .
$$

Consider the quadric

$$
A x ^ { 2 } + B y ^ { 2 } + C z ^ { 2 } - 2 F y z - 2 G z x - 2 H x y = \mathrm { { c o n s t a n t } } .
$$

f $P$ isa point on the quadric,the moment of inertia about the axis $O P$ is inversely proportional to the square of the distance $0 P .$ Since there isa real moment of inertia inany direction, the quadric must be an ellipsoid; it is called the momental ellipsoid, and its axes are the principal axes of inertia. If the reader does not like the abstraction of the inertia tensor,it may be helpful instead to think of the momental elipsoid;this is something that is obviously independent of its description with respect to any particular triad. (But not all tensors are amenable to this sort of parallel.）

As the body moves, the description of I with respect to a fixed reference system will vary， but it will remain constant with respect to axes fixed in the body itself. If the body is rotating about a line through the origin and is subject to external forces of moment $\Sigma$ ,then the angular momentum equation is

$$
{ \begin{array} { r l } & { \mathbf { F } = { \frac { d } { d t } } ( \omega \cdot { \bar { \mathbf { f } } } ) } \\ & { \quad = { \frac { \partial } { \partial t } } ( \omega \cdot { \bar { \mathbf { f } } } ) + \omega \times ( \omega \cdot { \bar { \mathbf { I } } } ) \quad { \mathrm { ( f r o m ~ S e c t i o n ~ 2 . 7 ) } } } \\ & { \quad = { \dot { \omega } } \cdot { \bar { \mathbf { I } } } + \omega \times ( \omega \cdot { \bar { \mathbf { I } } } ) . } \end{array} }
$$

If the axes of reference fixed in the body are chosen as the principal axes of inertia,(5.2.6) can be written as

$$
\begin{array} { r } { \Gamma _ { 1 } = A \displaystyle \frac { d \omega _ { 1 } } { d t } - ( B - C ) \omega _ { 2 } \omega _ { 3 } \Bigg ] } \\ { \Gamma _ { 2 } = B \displaystyle \frac { d \omega _ { 2 } } { d t } - ( C - A ) \omega _ { 3 } \omega _ { 1 } , } \\ { \Gamma _ { 3 } = C \displaystyle \frac { d \omega _ { 3 } } { d t } - ( A - B ) \omega _ { 1 } \omega _ { 2 } . } \end{array}
$$

These are Euler's equations of motion.

We complete this section by finding the moments of inertia of two homogeneous solids,the sphere,and the ellipsoid about its axes.For the sphere, we have, by symmetry, $A = B = C$ But

$$
A + B + C = 2 \int ( x ^ { 2 } + y ^ { 2 } + z ^ { 2 } ) d m = 2 \rho \int r ^ { 2 } d v
$$

integrated over the volume of the sphere, where $\boldsymbol { \geqslant }$ is the density and $\vec { d } \mathfrak { T }$ is the element of volume. Dividing the sphere up into thin concentric shells,we find

$$
\begin{array} { c } { { A + B + C = 2 \rho 4 \pi \displaystyle \int _ { 0 } ^ { \alpha } r ^ { 4 } \dot { d r } } } \\ { { = \displaystyle \frac { 8 \pi } { 5 } \rho a ^ { 5 } , } } \end{array}
$$

where $\pmb { \mathscr { E } }$ is the radius of the sphere. Hence

$$
A = \frac { 8 \pi } { 1 5 } \rho a ^ { 5 } = \frac { 2 } { 5 } M a ^ { 2 } ,
$$

where $\pmb { \hat { \mathit { \Omega } } } _ { \pmb { \hat { \mathcal { A } } } } ^ { \pmb { \hat { \mathcal { A } } } }$ is the mass of the sphere.

For the ellipsoid, the axes are the principal axes of inertia, and

$$
A = \int ( y ^ { 2 } + z ^ { 2 } ) d m = \rho \int ( y ^ { 2 } + z ^ { 2 } ) d x d y d z ,
$$

integrated throughout the ellipsoid

$$
{ \frac { z ^ { 2 } } { a ^ { 2 } } } + { \frac { y ^ { 2 } } { b ^ { 2 } } } + { \frac { z ^ { 2 } } { c ^ { 2 } } } = 1 .
$$

If the variables are changed to $z ^ { \prime } = x / a , y ^ { \prime } = y / b , z ^ { \prime } = z / c _ { 1 }$ then the integration reduces to an integration throughout a sphere and is performed without difficulty. The result is

$$
A = \frac { 1 } { 5 } M \{ b ^ { 2 } + c ^ { 2 } \} ,
$$

with similar expressions for $\mathcal { B }$ and $C$ ,where $\pmb { \widetilde { \it B } }$ is the mass of the ellipsoid.

(The moments of inertia about the principal axes of simple bodies are given byamnemonic known as Routh'srule. This states that they are $M s ^ { 2 } / 3$ ,where $\mathbf { s } ^ { 2 }$ is the sum of the squares of the lengths of the semiaxes of the body at right angles to the given axis,and $\mathfrak { N }$ has the values3, 4, or 5,accordingas the body is rectangular, elliptical,or ellipsoidal.)

# Problems

1.Show that the moment of inertia of a body with center of gravity $G$ about any axis is equal to the moment of inertia about a parallel axis through $\pmb { G }$ plus $\mathbb { M } p ^ { 2 }$ ,where $\mathbb { M }$ is the mass of the bodyand $p$ is the perpendicular distance from $G$ to the axis.   
2.Abody has angular velocity $\omega$ about an axis passing through the origin. Show that twice its kinetic energy is $\sum _ { i , j } w _ { i } w _ { j }$   
3.A body has symmetry about an axisisuch that $A = B$ Show that the angular velocity of the body can be expressed as

$$
n \hat { \mathbf { z } } + \hat { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \Lambda } } } } } } } } } \times \mathrm { \frac { \partial \hat { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf \Lambda } } } } } } } } } } { \partial \hat { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf \Lambda } } } } } } } } } }
$$

and that its angular momentum is

$$
C a \hat { \bf \hat { z } } + A \hat { \bf \hat { \bf \hat { \mathbf { z } } } } \times \frac { d \hat { \bf \hat { \bf \hat { z } } } } { d \hat { \bf \hat { z } } } .
$$

Interpret n.

4. Assuming them to be homogeneous bodies with constant angular rotations throughout, find the angular momenta due to axial rotation of the Sun, the Earth,the Moon,and Jupiter.

5.Find the angular momentum of each planet due to its revolution around the Sun. Hence investigate the distribution of angular momentum in the solar system.

# 5.3The Potential of a Sphere

The potential at $o$ of a solid body is

$$
V = - G \int { \frac { d x } { r } } = - G \int \rho { \frac { d x } { r } }
$$

where the integral is taken throughout the body.If $\boldsymbol { \theta }$ lies outside the body,the integrand is finite everywhere (as longas the density has no singularity),so that there is no trouble over convergence. If $o$ lies inside the body,the integrand has a singularity at $o$ ；but if we use spherical polar coordinates1, the element of volume is

$$
d v = r ^ { 2 } \sin \theta d \pi d \theta d \phi
$$

and

$$
V = - G \int \int \int \rho r \sin \theta d r d \theta d \phi
$$

and the integral converges.

Consider the attraction experienced at an internal point $o$ of a uniform spherical shell, bounded by concentric spheres. Let a cone with vertex $\pmb { \mathscr { O } }$ and small solid angle² dw cut the shell,as shown in Figure 5.2,in two frustra $P Q Q ^ { \prime } P ^ { \prime }$ and $R S S ^ { \prime } R$ .If $\beta$ is the density， the mass of $\hat { \mathbf { \alpha } }$ thin slice of the cone of thickness dr is $\rho r ^ { 2 } d \omega d r$ ,and its attraction at $o$ is $G \rho$ dw dr. So, the attractions of the two frustra are $G \beta d ^ { \prime } \sigma P Q$ and $G \rho d \omega R S$ But,since the bounding spheres are concentric, they make equal intercepts on any chord; hence $P Q = \Re S$ and the attractions at $o$ are equal and opposite. By taking cones in all directions around $o$ we see that the resultant attraction is zero. In integrating $G \rho$ dw dr with respect to $\mathfrak { T }$ , we appear to have neglected wedge-shaped elements at $\mathcal { P }$ and $Q$ but the further integration with respect to $\omega$ implies that $\check { d } \omega$ tends to zero, so that these wedge-shaped elements contribute nothing.

![](../chunks/Fundamentals of Celestial Mechanics (John M. A. Danby) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0041-0080/ocr/images/e41b0d595fa1a8b9a2e554d9917a1c06241c67a8c6476aad8bdfbda6e3d02b59.jpg)  
Figure 5.2

At this stage it is convenient to consider the internal attraction of a uniform shell bounded by two similar ellipsoids,called a homoid. (Two ellipsoids are similar if their axes are in a constant ratio).The same method is used,the relevant figure being Figure 5.3. Now this figure can be regarded as the projection ofFigure 5.2. so that we still have ${ \mathcal { P Q } } = R S$ Hence theattraction ofa homoid at an internal point is zero.

Now consider the potential of a uniform,thin spherical shell at $\hat { \pmb { c } }$ point $o$ outside the shell. Let the shell have center $C$ radius $\pmb { \alpha }$ and thickness $d a$ ,and let $O C = r$ (See Figure 5.4.）If $\mathcal { P }$ isa point on the shell, let the angle $O C P = \theta$ Divide the shell into thin rings perpendicular to $o c$ and defined by $\theta$ lying within the limits $\pmb { \hat { \theta } }$ and $\theta \neq \dot { a } \theta$ The radius of the ring is $\alpha \sin \theta$ and its mass is

$$
\rho \times 2 \pi a \sin \theta \times a \dot { a } \theta \times \dot { a } a
$$

where $\boldsymbol { \rho }$ is the density of the shell. Any element of the ring is at the distance

$$
( r ^ { 2 } + \alpha ^ { 2 } - 2 \alpha r \cos \theta ) ^ { 1 / 2 }
$$

from $\boldsymbol { \mathcal { O } }$ , so that the potential of the ring at $o$ is

$$
- G \rho 2 \pi a ^ { 2 } d \alpha \frac { \sin \theta d \theta } { ( r ^ { 2 } + a ^ { 2 } - 2 a ^ { * } \cos \theta ) ^ { 1 / 2 } }
$$

![](../chunks/Fundamentals of Celestial Mechanics (John M. A. Danby) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0041-0080/ocr/images/aa44203b1f1fc7a90bd6f60254cbc712366641936c7f7d7ae931ff6e4c4952d5.jpg)  
Figure 5.3

![](../chunks/Fundamentals of Celestial Mechanics (John M. A. Danby) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0041-0080/ocr/images/c0a1c36afc08fb2bdab9d03f420ce70f1b09a0a28586beef70353f7312383e2b.jpg)  
Figure 5.4

and the total potential at $\boldsymbol { \vartheta }$ is

$$
V = - G \rho 2 \pi a ^ { 2 } d a \int _ { 0 } ^ { \pi } \frac { \sin \theta d \theta } { ( r ^ { 2 } + a ^ { 2 } - 2 a r \cos \theta ) ^ { 1 / 2 } }
$$

where the square root must always be positive. This can be integrated at once to give

$$
\begin{array} { l } { { V = - \displaystyle \frac { 1 } { 2 } G d m \left[ \frac { 1 } { r a } ( r ^ { 2 } + a ^ { 2 } - 2 a r \cos \theta ) ^ { 1 / 2 } \right] _ { \theta = 0 } ^ { \pi } } } \\ { { ~ = - G \displaystyle \frac { d m } { r } , } } \end{array}
$$

where dm= 4πa²pda is the mass of the shell. This means that,as far as O is concerned, the shell could just as well have allits mass concentrated at C. This must also apply to a shell of finite thickness,since the result is not affected by integration over a,and it applies in particular toa solid sphere constructed out of shells of equal density (i.e., the density depends only on a),with total radius less than $\mathcal { F }$

If a sphere has total mass $M$ center $C$ anddensity that is a function only of distance from $C$ then for gravitational purposes we can treat it as a point mass $\pmb { \mathcal { M } }$ at $C$ ,aslong as we remain outside it. So,there is no difficulty in generalizing particle motion under Newton's law to apply to the motion of spheres.For much of the dynamics in the solar system it is sufficient to assume that the Sun and planets are constructed in spherical shells,so that they can be treated as point masses.

# Problems

1.A sphere of 150 kg,placed with its center 30 cm vertically below that of another sphere, is found to cause an apparent increase of the latter's weight by the $\exists . 1 4 \times \mathtt { i } \mathtt { Q } ^ { - 8 }$ part.What value does this imply for the constant of gravitation?   
2.The density of a sphere varies as the depth below the surface. Show that the resultant attraction is greatest at a depth equal to one-third of the radius,and that the value here is four-thirds of the value at the surface.   
3.A solid sphere of radius $\pmb { \alpha }$ is such that its density at any point is proportional to the $\mathfrak { P }$ th power of the distance of that point from the center of the sphere.Find the potential at any external point and show that the potential at an internal point ata distance $\mathcal { P }$ from the center is

$$
\frac { G M } { n + 2 } [ \frac { n + 3 } { a } - \frac { n + 2 } { a ^ { n + 3 } } ] ,
$$

where $\overrightarrow { i } \overrightarrow { a }$ is the total mass of the sphere.

4. Show that the initial rate of decrease of g in descending a mine shaft would be equal to g/a if the density p of the Earth (of radius a) were uniform.But if the Earth had a spherical nucleus of different density and radius b,the density of this nucleus must be

$$
\rho \left( 1 + \frac { 1 - \lambda a ^ { 3 } } { 2 + \lambda b ^ { 3 } } \right) ,
$$

where $\lambda ( g / a )$ is the initial rate of decrease of $\mathfrak { g }$ in descending the shaft.

5.Assuming the Earth to be a homogeneous sphere of density o and radius a, surrounded by a spherical shellof density p and thickness (b-a),show that the weight of a body given by a spring balance is unaltered at first on descending vertically if

$$
\rho = \sigma { \frac { 2 a ^ { 3 } } { 2 a ^ { 3 } + b ^ { 3 } } } .
$$

The rotation of the Earth may be neglected.

6.A solid sphere of radius $\pmb { \mathcal { Q } }$ and uniform density is surrounded by a concentric shell of internal radius $\pmb { a }$ and external radius $\mathfrak { z }$ in which the density is a function of the distance from the center.Find the law of density if the force of attraction is constant in the substance of the shell, and show that the mass of the shell is to the mass of the sphere as $( b ^ { 2 } - a ^ { 2 } )$ is to $a ^ { 2 }$ ·

7.The density of a sphere of radius $\pmb { \mathscr { a } }$ and mean density $\overline { { \rho } }$ is a function of thedistance from the center,such that the attraction at any point inside the sphere is proportional to the square of the distance from the center. Express the density at distance $\mathfrak { P }$ from the center in termsof ${ \overline { { \beta } } } , { \mathfrak { a } }$ and $\mathscr { r }$ and show that the potential of an internal point at a distance $\nsim$ from the center is

$$
\frac { 4 } { 9 } \pi G \frac { 4 a ^ { 3 } - r ^ { 3 } } { a } .
$$

8.A system of particles, $\mathfrak { M } _ { i }$ ,is assembled from a state of infinite diffusion. Show that the potential energy lost in the process of assembly is ${ \frac { 1 } { 2 } } \sum m _ { i } Y _ { i }$ where $V _ { i }$ is the potential at the ultimate position of $\mathfrak { W } _ { 2 } \mathfrak { W } _ { 3 }$

Assuming that the Sun remainsa homogeneous sphere, find the change in potential energy if it contracts by $\pmb { \mathcal { X } }$ per cent of its radius.If the amount of heat emitted annually by the Sun would raise the temperature of a mass of water equal to the mass of the Sun by $1 . 4 4 \div C$ and this heat were produced by a contraction of $\pmb { \mathcal { X } }$ per cent per million years, find $\pmb { \mathscr { x } }$

# 5.4The Potential of a Distant Body - MacCullagh's Formula

When we leave simple figures such as the sphere, expressions for the potentials become somewhat tiresome; this will become patently clear in the following section on the ellipsoid. However,if the point that we are considering is at a distance from the attracting body which is large compared with the body'soverall dimensions (as is often the case in astronomy),there isa simple approximate formula for the potential, due to MacCullagh.

![](../chunks/Fundamentals of Celestial Mechanics (John M. A. Danby) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0041-0080/ocr/images/32946a54a8443ee941e4d59374fce70858670a496f2ff37050669351df2d6d69.jpg)  
Figure 5.5

Let $G$ be the center of gravity of the attracting body and $\theta a$ point distant $\mathcal { R }$ from $G$ where $\mathcal { R }$ islarge compared with the dimensions of the body. If dm is the mass of an element at $P$ such that $G ^ { \mathfrak { P } } = { \mathfrak { r } }$ and $\angle O G P = \theta$ thepotential at $\boldsymbol { \vartheta }$ is

$$
\begin{array} { l } { { { \cal { Y } } = - { \cal { C } } \displaystyle \int \displaystyle \int \displaystyle \frac { d m } { D \bar { \cal { P } } } } } \\ { { \displaystyle ~ = - { \cal { C } } \displaystyle \int \displaystyle \frac { d m } { ( R ^ { 2 } + r ^ { 2 } - 2 R r \cos \theta ) ^ { 1 / 2 } } } } \\ { { \displaystyle ~ = - \displaystyle \frac { G } { R } \displaystyle \int d m \left( 1 - 2 \displaystyle \frac { r } { R } \cos \theta + \displaystyle \frac { r ^ { 2 } } { R ^ { 2 } } \right) ^ { - 1 / 2 } } } \\ { { \displaystyle ~ = - \displaystyle \frac { G } { R } \displaystyle \int d m \left\{ 1 + \displaystyle \frac { r } { R } \cos \theta - \displaystyle \frac { 1 } { 2 } \cdot \displaystyle \frac { r ^ { 2 } } { R ^ { 2 } } + \displaystyle \frac { 3 } { 2 } \cdot \displaystyle \frac { r ^ { 2 } } { R ^ { 2 } } \cos ^ { 2 } \theta + { \cal { O } } \left( \displaystyle \frac { r } { R } \right) ^ { 3 } \right\} } } \\ { { \displaystyle ~ = - \displaystyle \frac { G } { R } \left\{ \displaystyle \int d m + \displaystyle \frac { 1 } { R } \int r \cos \theta d m + \displaystyle \frac { 1 } { 2 R ^ { 2 } } \int ( 2 r ^ { 2 } - 3 r ^ { 2 } \sin ^ { 2 } \theta ) d m + { \cal { O } } \left( \displaystyle \frac { r } { R } \right) ^ { 3 } \right\} } . }  \end{array}
$$

The first integral on the right-hand side gives $\pmb { i } \pmb { i }$ ,the total mass of the body. Since $G$ is at the center of gravity of the body, the second integral is zero. Let $\pmb { \bar { \downarrow } }$ be the moment of inertia of the body about $G O ;$ then

$$
I = \int \rho ^ { 2 } \sin ^ { 2 } \theta d m .
$$

Also,if $A , B$ and $\pmb { C }$ are the principal moments of inertia,

$$
A + B + C = 2 \int r ^ { 2 } d m .
$$

Hence

$$
V = - { \frac { G M } { R } } - { \frac { G } { 2 R ^ { 3 } } } ( A \div B + C - 3 I ) ,
$$

where terms of the order (r/R)3 have been neglected. This is MacCullagh's formula.

Most celestial bodies are only slightly distorted from spherical figures,and the second term on the right-hand side of (5.4.1) is small, not only by virtue of the smallness of r/R but also because the quantity A+ B+C-3I is small. Hence (5.4.1） can be applied even for only moderately small r/R.

# 5.5The Field of a Homogeneous Ellipsoid

There are several ways of arriving at the formulas for the field of a homogeneous ellipsoid, and all depend at some stage on somewhat brutal integration. The approach given here is based on that used by Ramsey in his text Newtonian Attraction (Ref.12).It falls into several stages.

First we shall find the internal potential of a homoid.Since there is no net force inside the homoid,the potential is constant and equal to the value at the center $o$ Let the boundaries of the homoid have axes $a , b , c ,$ and $\mathcal { P } ^ { \mathcal { Q } }$ pb,pc, where p is less than one. With the center as apex,construct a cone with solid angle $d ( t )$ intercepting the homoid at distances $\Im ^ { * }$ and $p r$ from $o$ .The potential at $o$ due to the frustrum contained in this cone is

$$
- G \int _ { p r } ^ { r } \rho \tau ^ { 2 } d \omega \frac { d r } { \tau } = - \frac { 1 } { 2 } G \rho ( 1 - p ^ { 2 } ) r ^ { 2 } d \omega ,
$$

so the total potential at $o$ is

$$
\gamma _ { 0 } = - \frac { \mathbb { i } } { 2 } G \rho ( 1 - p ^ { 2 } ) \int r ^ { 2 } d \omega
$$

integrated over the outer boundary.

Now the equation of the outer boundary is

$$
{ \frac { x ^ { 2 } } { a ^ { 2 } } } + { \frac { y ^ { 2 } } { b ^ { 2 } } } \div { \frac { z ^ { 2 } } { c ^ { 2 } } } = 1 .
$$

Let a point on the boundary have coordinates $\{ r _ { i } ^ { 7 } , r \eta r , \tau \eta \}$ ，where $\vec { i } , \ m$ and $\mathbf { \Omega } _ { \mathcal { R } } ^ { \otimes }$ are direction cosines. Then

$$
\pi ^ { 2 } \left\{ { \frac { l ^ { 2 } } { a ^ { 2 } } } + { \frac { m ^ { 2 } } { b ^ { 2 } } } \div { \frac { n ^ { 2 } } { c ^ { 2 } } } \right\} = 1 .
$$

$\operatorname { I f } \ r , \theta _ { i }$ and $\phi$ are taken as spherical polar coordinates, we have $\tilde { \iota } = \sin \theta \cos \phi .$ $m = \sin \theta \sin \phi$ $\gamma _ { 2 } = \cos \theta$ Also,the element of solid angle is $\dot { a } \omega = \sin \theta \dot { a } \theta \dot { a } \phi$ Since the integrand in the expression for $\gamma _ { \Updownarrow }$ is symmetrical about each axis,its integrated value is eight times the value when integrated over one quadrant. Hence

$$
V _ { 0 } = - \frac { 1 } { 2 } G \rho ( 1 - p ^ { 2 } ) \int \frac { d \omega } { \left( \frac { l ^ { 2 } } { a ^ { 2 } } + \frac { m ^ { 2 } } { b ^ { 2 } } + \frac { n ^ { 2 } } { c ^ { 2 } } \right) }
$$

$$
= - 4 G \rho ( 1 - p ^ { 2 } ) \int _ { 0 } ^ { \pi / 2 } \int _ { 0 } ^ { \pi / 2 } \frac { \sin \theta d \theta d \phi } { \sin ^ { 2 } \theta \left( \frac { \cos ^ { 2 } \phi } { a ^ { 2 } } + \frac { \sin ^ { 2 } \phi } { b ^ { 2 } } \right) + \frac { \cos ^ { 2 } \theta } { c ^ { 2 } } } .
$$

Let $\tan \phi = { \tt t }$ Then

$$
V _ { 0 } = - 4 G \rho ( 1 - p ^ { 2 } ) \int _ { 0 } ^ { \pi / 2 } \int _ { 0 } ^ { \infty } \frac { \sin \theta d \theta d t } { \frac { \sin ^ { 2 } \theta } { a ^ { 2 } } + \frac { \cos ^ { 2 } \theta } { b ^ { 2 } } + \left( \frac { \sin ^ { 2 } \theta } { b ^ { 2 } } + \frac { \cos ^ { 2 } \theta } { c ^ { 2 } } \right) t ^ { 2 } } .
$$

Now

$$
\int _ { 0 } ^ { \infty } \frac { d t } { A ^ { 2 } + B ^ { 2 } t ^ { 2 } } = \left[ \frac { 1 } { A B } \tan ^ { - 1 } \left( \frac { B t } { A } \right) \right] _ { 0 } ^ { \infty } = \frac { 1 } { 2 } \cdot \frac { \pi } { A B } ,
$$

S0

$$
V _ { 0 } = - 2 \pi G \rho ( 1 - p ^ { 2 } ) \int _ { 0 } ^ { \pi / 2 } \frac { \sin \theta d \theta } { \left\{ \left( \frac { \sin ^ { 2 } \theta } { a ^ { 2 } } + \frac { \cos ^ { 2 } \theta } { c ^ { 2 } } \right) \left( \frac { \sin ^ { 2 } \theta } { b ^ { 2 } } + \frac { \cos ^ { 2 } \theta } { c ^ { 2 } } \right) \right\} ^ { 1 / 2 } } .
$$

Put $\mathfrak { Q } = \mathfrak { c } ^ { 2 } \tan \theta$ ； then substituting and rearranging, we eventually get

$$
\begin{array} { r } { V _ { \Updownarrow } = - \pi G \rho ( \updownarrow - p ^ { 2 } ) a b c I , } \end{array}
$$

where

$$
{ \cal I } = \int _ { 0 } ^ { \infty } \frac { d u } { \Delta } \quad \mathrm { a n d } \quad \Delta ^ { 2 } = ( a ^ { 2 } + u ) ( b ^ { 2 } + u ) ( c ^ { 2 } + u ) .
$$

If we put ${ \mathfrak { P } } = 0$ ，we have the potential at the center of a solid homogeneous ellipsoid.

Next we shall find the components of attraction at a point $P$ with coordinates $\{ x , y , z \}$ ,inside a solid ellipsoid. Since the homoid outside the similar ellipsoid passing through $\mathcal { P }$ exerts no force at $P$ ,it is suffcient to find the force exerted by an ellipsoid at a point on its surface.

From $\mathcal { P }$ let $\mathtt { a }$ line in the direction $( \vec { \emptyset } , \Re , \Re )$ meet the ellipsoid again at $a$ ， where $P Q = \uparrow$ then the coordinates of $Q$ are

$$
( x + l r , y + m r , z \div n \cdots ) .
$$

Writing down the conditions for $\mathcal { P }$ and $Q$ to lie on the ellipsoid with semiaxes $a , b .$ and $\mathfrak { c }$ and subtracting them, we get

$$
r ^ { 2 } \left( { \frac { l ^ { 2 } } { a ^ { 2 } } } + { \frac { m ^ { 2 } } { b ^ { 2 } } } + { \frac { n ^ { 2 } } { c ^ { 2 } } } \right) + 2 r \left( { \frac { l x } { a ^ { 2 } } } + { \frac { m y } { b ^ { 2 } } } + { \frac { n z } { c ^ { 2 } } } \right) = 0 .
$$

$\gamma = 0$ gives $\mathcal { P }$ the other value gives $Q$

Construct a cone with vertex P, solid angle dw, and axis lying along PQ. The force at P due to the matter in this cone is

$$
- G \rho d \omega ^ { \prime } \int _ { 0 } ^ { \mathcal { F } } d \tau = G \rho \tau d \omega .
$$

So,the components of this force at P are

$$
( - G \rho i r d \omega , \ - G \rho m i r d \omega \ - G \rho n r \ d \omega ) ,
$$

and to get the total components of force, we integrate over all possible values of w.But, since every line through P has a real intersection with the elipsoid, an integration over all w will cover the ellipsoid twice. So the x-component of force is

$$
X = - \frac { 1 } { 2 } G \rho \int l \ d { \hat { \tau } } d \omega
$$

$$
= - { \frac { 1 } { 2 } } G \rho \int { \frac { 2 i \left( { \frac { l x } { a ^ { 2 } } } + { \frac { m y } { b ^ { 2 } } } + { \frac { n z } { c ^ { 2 } } } \right) } { { \frac { l ^ { 2 } } { a ^ { 2 } } } + { \frac { m ^ { 2 } } { b ^ { 2 } } } + { \frac { n ^ { 2 } } { c ^ { 2 } } } } } d \omega .
$$

The terms in mn, nl,and lm contribute nothing to the integral, since terms in Im and l(-m), for instance, occur equally and cancel one another. So we get

$$
\begin{array} { l } { \displaystyle { \mathrm {  ~ \cdot ~ } \sum _ { X = - G \rho x \int \frac { \frac { l ^ { 2 } } { a ^ { 2 } } \dot { a } \omega } { \frac { l ^ { 2 } } { a ^ { 2 } } + \frac { m ^ { 2 } } { b ^ { 2 } } + \frac { n ^ { 2 } } { c ^ { 2 } } } } } } \end{array}
$$

$$
= - G \rho A x .
$$

There are similar expressions for $\mathbb { Y }$ and $Z$ ,functions $\mathcal { B }$ and $\boldsymbol { \mathcal { Z } }$ being similarly defined. (The notation is confusing; $A , B$ ,and $C$ must not be confused with the moments of inertia.）

To simplify the expression for A, we use the same substitutions as were used to find (5.5.1) and (5.5.2). In this case we get,eventually,

$$
A = 2 \pi a \dot { b } c \int _ { 0 } ^ { \infty } \frac { \dot { a } u } { \Delta ( a ^ { 2 } + u ) }
$$

and similar expressions for $\mathcal { B }$ and $C$

Now we are able to find the potential V at any point inside an ellipsoid. From the relation between the potential function and the feld of force,V must he of the form

$$
\gamma = - \frac { 1 } { 2 } G \rho ( D - A x ^ { 2 } - B y ^ { 2 } - C z ^ { 2 } ) .
$$

From (5.5.1) and (5.5.2) the value of $\mathfrak { D }$ is known,and we have

$$
V = - G \pi \rho a b c \int _ { 0 } ^ { \infty } \left\{ \frac { \ d z } { \ d z } - \frac { x ^ { 2 } } { a ^ { 2 } + u } - \frac { y ^ { 2 } } { b ^ { 2 } + u } - \frac { z ^ { 2 } } { e ^ { 2 } + u } \right\} \frac { d u } { \Delta } .
$$

This can also be written in the form

$$
V = - G \pi \rho a \dot { b } c \left\{ \bar { I } + \frac { x ^ { 2 } } { a } \cdot \frac { \partial \bar { I } } { \partial a } + \frac { y ^ { 2 } } { b } \cdot \frac { \partial \bar { I } } { \partial \dot { b } } + \frac { z ^ { 2 } } { c } \cdot \frac { \partial \bar { I } } { \partial c } \right\}
$$

From (5.5.4) we see that

$$
\Dot { A } \Dot { + } \ B \Dot { + } C = \int \tilde { d } \omega = \Dot { z } \pi .
$$

Also,

$$
A a ^ { 2 } + B b ^ { 2 } + C c ^ { 2 } = \int { \frac { d w } { \frac { l ^ { 2 } } { a ^ { 2 } } + { \frac { m ^ { 2 } } { b ^ { 2 } } } + { \frac { n ^ { 2 } } { c ^ { 2 } } } } } ,
$$

It should be noted that the values of $A , B ,$ and $C$ depend only on the ratios of the axes.

In general the integrals can be evaluated only in terms of elliptic functions. But,for spheroids, two axes are equal, and elementary functions can be used. Let $\alpha = \mathfrak { z }$ so that $A = B$ From (5.5.11) we have

$$
{ \begin{array} { r l } { 2 A a ^ { 2 } + C e ^ { 2 } = \displaystyle \int { \frac { \frac { d \omega } { 2 } + m ^ { 2 } } { { \frac { d ^ { 2 } } { a ^ { 2 } } } ^ { 2 } + { \frac { m ^ { 2 } } { e ^ { 2 } } } } } } & { } \\ { = \displaystyle \int _ { 0 } ^ { \pi } \int _ { \phi ^ { * } } ^ { 2 \pi } { \frac { \sin \theta d \theta d \phi } { { \frac { \sin ^ { 2 } \theta } { a ^ { 2 } } } + { \frac { \cos ^ { 2 } \theta } { c ^ { 2 } } } } } } & { } \\ { = 2 \pi \displaystyle \int _ { - 1 } ^ { + 1 } { \frac { d \pi } { { \frac { 1 } { a ^ { 2 } } } + \left( { \frac { d \pi } { c ^ { 2 } } } - { \frac { 1 } { a ^ { 2 } } } \right) u ^ { 2 } } } } \end{array} }
$$

where $z = \cos \theta$

There are two cases:

OBLATE SPHEROID, $a > c$

$$
\begin{array} { c } { { 2 A a ^ { 2 } + C c ^ { 2 } = \displaystyle \frac { 4 \pi a ^ { 2 } c } { \sqrt { a ^ { 2 } - c ^ { 2 } } } \tan ^ { - 1 } \sqrt { \displaystyle \frac { a ^ { 2 } } { c ^ { 2 } } - 1 } } } \\ { { = \displaystyle 4 \pi a ^ { 2 } \displaystyle \frac { \sqrt { 1 - e ^ { 2 } } } { e } \tan ^ { - 1 } \left( \displaystyle \frac { e } { \sqrt { 1 - e ^ { 2 } } } \right) } } \end{array}
$$

where $a ^ { 2 } \{ 1 - e ^ { 2 } \} = c ^ { 2 }$

PROLATE SPHEROID, ${ \mathfrak { a } } < c$ ·

$$
\begin{array} { c } { { 2 A a ^ { 2 } + C c ^ { 2 } = \displaystyle \frac { 2 \pi a ^ { 2 } c } { \sqrt { c ^ { 2 } - a ^ { 2 } } } \ln \left\{ \displaystyle \frac { c + \sqrt { c ^ { 2 } - a ^ { 2 } } } { c - \sqrt { c ^ { 2 } - a ^ { 2 } } } \right\} } } \\ { { = 2 \pi c ^ { 2 } \displaystyle \frac { 1 - e ^ { 2 } } { e } \ln \displaystyle \frac { 1 + e } { 1 - e } , } } \end{array}
$$

where $a ^ { 2 } = c ^ { 2 } \{ 1 - e ^ { 2 } \}$

In each case $e$ is the eccentricity of the generating ellipse. The separate values of $A$ and $C$ can be found by (5.5.10).

Consider the case of a prolate spheroid that is only slightly distorted from a sphere.Then

$$
\begin{array} { r } { c = a \{ \frac { 1 } { 2 } \ + \epsilon \} , } \end{array}
$$

where $\epsilon .$ called the ellipticity, is small. Approximately,

$$
e ^ { 2 } = 2 \varepsilon .
$$

Expanding (5.5.13) in powers of $e ,$ we have

$$
\begin{array} { c } { { 2 A c ^ { 2 } ( 1 - e ^ { 2 } ) + C c ^ { 2 } = 2 \pi c ^ { 2 } \displaystyle \frac { 1 - e ^ { 2 } } { e } \left( 2 e + \frac 2 3 e ^ { 3 } + \frac 2 5 e ^ { 5 } + \cdots \right) } } \\ { { = 4 \pi c ^ { 2 } ( 1 - \frac 2 3 e ^ { 2 } - \frac 2 { \bar { 4 } \bar { 5 } } e ^ { 4 } + \cdots ) . } } \end{array}
$$

Then,since $2 A + C = 4 \pi$ ,we find

$$
2 . 4 = 4 \pi ( \frac { 2 } { 3 } + \frac { 2 } { 1 5 } e ^ { 2 } + \cdot \cdot \cdot ) .
$$

Then,neglecting powers of $\boldsymbol { \mathscr { E } }$ we have

Then

$$
\left. \begin{array} { c } { { A = \frac 4 3 \pi \big ( 1 + \frac 2 5 \epsilon \big ) . } } \\ { { } } \\ { { } } \\ { { C = \frac 4 3 \pi \big ( 1 - \frac 4 5 \epsilon \big ) . } } \end{array} \right]
$$

These expressions will be needed later when we consider the tidal distortion of a liquid sphere. Similar expressions for the slightly distorted oblate spheroid are

$$
\begin{array} { r } { A = \frac { 4 } { 5 } \pi ( 1 - \frac { 2 } { 5 } \epsilon ) , } \\ { C = \frac { 4 } { 5 } \pi ( 1 + \frac { 4 } { 5 } \epsilon ) , } \end{array}
$$

where $c = a _ { \downarrow } ^ { \prime } - \epsilon )$

Now suppose we have a nearly spherical ellipsoid with axes $\mathfrak { a }$ ： $a _ { i } ^ { \textit { f } } \bar { \underline { { \mathbf { i } } } } - \mathfrak { P } ) \}$ and $a _ { i } ^ { \{ 1 - \varepsilon \} }$ Since we are neglecting powers of $\boldsymbol { \varepsilon }$ and $\mathfrak { P }$ the expressions for $A , B$ ，

and $C$ will be linear in $\boldsymbol { \varepsilon }$ and $\eta$ When $\eta = 0$ we have, from the results above,

$$
\begin{array} { r } { A = \frac { 4 } { 3 } \pi ( 1 - \frac { 2 } { 5 } \varepsilon ) , } \\ { B = \frac { 4 } { 3 } \pi ( 1 - \frac { 2 } { 5 } \varepsilon ) , } \\ { C = \frac { 4 } { 3 } \pi ( 1 + \frac { 4 } { 5 } \varepsilon ) . } \end{array}
$$

Similarly, if $\varepsilon = \emptyset$ ， $b$ becomes the unequal axis of $\hat { \pmb { \alpha } }$ spheroid, and we have

$$
\begin{array} { r } { A = \frac { 4 } { 3 } \pi \big ( \mathbb { 1 } - \frac { 2 } { 5 } \mathbb { 1 } \big ) , } \\ { B = \frac { 4 } { 3 } \pi \big ( \mathbb { 1 } + \frac { 4 } { 5 } \mathbb { 1 } \big ) , } \\ { C = \frac { 4 } { 3 } \pi \big ( \mathbb { 1 } - \frac { 2 } { 5 } \mathbb { 1 } \big ) . } \end{array}
$$

These two cases must be particular cases of a general formula for the potential; since this is linear in $\epsilon$ and $\boldsymbol { \mathscr { T } }$ ,we must have

$$
\begin{array} { r } { A = \frac { 4 } { 3 } \pi \big ( \mathbb { 1 } - \frac { 2 } { 5 } \boldsymbol { \epsilon } - \frac { 2 } { 5 } \boldsymbol { \eta } \big ) , } \\ { B = \frac { 4 } { 3 } \pi \big ( \mathbb { 1 } - \frac { 2 } { 5 } \boldsymbol { \epsilon } + \frac { 4 } { 5 } \boldsymbol { \eta } \big ) , } \\ { C = \frac { 4 } { 3 } \pi \big ( 1 + \frac { 4 } { 5 } \boldsymbol { \epsilon } - \frac { 2 } { 5 } \boldsymbol { \eta } \big ) . } \end{array}
$$

These results can be put into a symmetrical form if we take $k$ to be the mean radius so that

$$
3 k = a + b + c .
$$

Then

$$
\begin{array} { r } { A = \frac { 4 } { 3 } \pi \left( 1 - \frac { 6 } { 5 } \cdot \frac { a - \dot { k } } { \dot { \kappa } } \right) , } \\ { B = \frac { 4 } { 3 } \pi \left( 1 - \frac { 6 } { 5 } \cdot \frac { \dot { b } - \dot { k } } { \dot { k } } \right) , } \\ { C = \frac { 4 } { 3 } \pi \left( 1 - \frac { 6 } { 5 } \cdot \frac { c - \dot { k } } { \dot { k } } \right) . } \end{array}
$$

No direct way to find the field outside an ellipsoid is known；this must be done in two stages, usinga theorem due $\$ 0$ Ivory.

Let the boundary $\boldsymbol { s }$ of the ellipsoid have equation

$$
{ \frac { x ^ { 2 } } { a ^ { 2 } } } \div { \frac { y ^ { 2 } } { b ^ { 2 } } } \div { \frac { z ^ { 2 } } { c ^ { 2 } } } = 1 .
$$

Then an ellipsoid $S _ { \{ \lambda \} } ^ { \{ \} }$ with equation

$$
\frac { x ^ { 2 } } { a ^ { 2 } + \lambda } + \frac { y ^ { 2 } } { 3 ^ { 2 } + \lambda } + \frac { z ^ { 2 } } { c ^ { 2 } + \lambda } = 1
$$

has the same foci as $S$ and is said to be confocal with $S$ If we consider $( x , y , z )$ as any fixed point, there are three quadrics passing through it which are confocal $S$ since (5.5.18） can be considered as a cubic in $\lambda$ It is easy to show that all the roots are real; for consider

$$
\phi ( \lambda ) \equiv { \frac { x ^ { 2 } } { a ^ { 2 } + \lambda } } + { \frac { y ^ { 2 } } { b ^ { 2 } + \lambda } } + { \frac { z ^ { 2 } } { c ^ { 2 } + \lambda } } - 1 .
$$

Let (x,y,z) lie outside S； then taking a and c to represent the largest and smallest axes, respectively， we see that for

$$
\begin{array} { r l } & { \lambda = 0 , \phi ( \lambda ) > 0 \ [ \mathrm { s i n c e } \ ( x , y , x ) \ \mathrm { l i e s \ o u t s i d e } \ S ] ; } \\ & { \lambda = - c ^ { 2 } + \epsilon , \ ( \epsilon \ \mathrm { s m a l l \ a n d \ p o s i \dot { t } \mathrm { v e } } ) , \ \phi ( \lambda ) \ \mathrm { i s \ l a r g } ; } \\ & { \lambda = - c ^ { 2 } - \epsilon , \phi ( \lambda ) \ \mathrm { i s \ l a r g e \ a n d \ n e g a t i v e } ; } \end{array}
$$

and so on. The graph of $\phi ( \lambda )$ is of the form:

![](../chunks/Fundamentals of Celestial Mechanics (John M. A. Danby) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0041-0080/ocr/images/c1fd1278e7f1d741cb088c8f2ae17e55eb2cb50b30b4d07892c878e49020079f.jpg)  
Figure 5.6

The only root that interests us here is the one which keeps all the denominators in (5.5.18) positive,so that we still have an ellipsoid. There is clearly one and only one such root,and it is the largest of the three. Where $\lambda$ is mentioned, it is this root that is meant.

Let $\overline { { f } } ^ { \prime }$ ， $\{ x ^ { 3 } , y ^ { \prime } , z ^ { \prime } \}$ be a point on $S ( \lambda )$ and let $\mathcal { P }$ ， $\{ x , y , z \}$ ,be defined so that

$$
{ \frac { x } { a } } = { \frac { x ^ { \prime } } { a ^ { \prime } } } , \quad { \frac { y } { b } } = { \frac { y ^ { \prime } } { b ^ { \prime } } } , \quad { \frac { z } { c } } = { \frac { z ^ { \prime } } { c ^ { \prime } } } ,
$$

where $a ^ { \prime 2 } = a ^ { 2 } + \lambda$ etc.Then $P$ must lie on $\pmb { S }$ The points $\mathcal { P }$ and $P ^ { \prime }$ are called corresponding points, and there is a one-to-one correspondence between them.

![](../chunks/Fundamentals of Celestial Mechanics (John M. A. Danby) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0041-0080/ocr/images/4c42c5f6f63bf3b2d5049d6fe8d8ddde43c678cb6d02650505feec5cd6e2ce5a.jpg)  
Figure 5.7

Let $Q R$ be an elementary strip of $\boldsymbol { S }$ with cross-section dy $d z$ ，parallel to the $\pmb { \mathcal { x } }$ -axis, and let $Q ^ { \prime } R ^ { \prime }$ be the corresponding strip of $S ( \lambda )$ ，with cross-section $\overrightarrow { a } y ^ { \prime } \overrightarrow { a } z ^ { \prime }$ so that

$$
{ \frac { d y \ : d ^ { 2 } z } { d y ^ { \prime } \ : d z ^ { \prime } } } = { \frac { b c } { b ^ { \prime } c ^ { \prime } } } .
$$

Then if df $\{ r \} / d r$ denotes the law of force for distance $\mathfrak { P }$ (an inverse square law for Newtonian attraction) and ${ \boldsymbol \beta }$ is the density of each ellipsoid,the attraction $P ^ { \prime }$ due to the strip $Q R$ has as its $\mathscr { x }$ -component:

$$
\Delta X = - G \rho d y d z \int \frac { d f } { d x } \cos \angle P ^ { \prime } T R d x
$$

where $\mathcal { T }$ is the position of an element dx dy dz. Now

$$
x ^ { 2 } + y ^ { 2 } + z ^ { 2 } = \uparrow ^ { 2 } ;
$$

if $\mathfrak { Y }$ and $z$ are constant (as they are along the strip) then

$$
x d x = r d x
$$

S0

$$
\cos \angle P ^ { \prime } \mathcal { T } \mathcal { R } = \frac { z } { r } = \frac { \dot { d } \mathfrak { F } } { \dot { d } z }
$$

and we have

$$
\begin{array} { l } { \Delta X = - G \rho d y d z \int \frac { d \vec { f } } { d z } \frac { d \vec { r } } { d x } d x } \\ { = G \rho d y d z \left[ f ( P ^ { \prime } Q ) - f ( P ^ { \prime } R ) \right] , } \end{array}
$$

ince the limits of integration are the ends,Q and R,of the strip.

In the same way, the x-component of the attraction at P due to the strip $Q ^ { \prime } R ^ { \prime }$ is

$$
\Delta X ^ { t } = G \rho d y ^ { t } d z ^ { t } [ f ( P Q ^ { t } ) - f ( P R ^ { t } ) ] .
$$

Now,from (5.5.19),we see that for any pair of corresponding points, PQ'= PQ and PR'= P'R.So,using (5.5.20) we find

$$
{ \frac { \Delta X } { \Delta X ^ { \prime } } } = { \frac { \mathfrak { x } } { { \mathfrak { d } } ^ { \prime } c ^ { \prime } } } .
$$

Taking all strips such as $Q R$ of $S$ and $Q ^ { \prime } R ^ { \prime }$ of $S \{ \lambda \}$ ,we finally have

$$
{ \frac { X } { X ^ { \prime } } } = { \frac { b c } { b ^ { \prime } c ^ { \prime } } } ,
$$

where X is the x-component of the attraction due to the ellipsoid S at P',and X'is the similar component of S(X) at P. This result is Ivory's theorem and is true for any conservative law of force. For Newton's law we have, since Pis inside $S ( \lambda )$ ，

$$
X ^ { i } = - A ^ { t } G \rho x ,
$$

where $A ^ { \prime }$ is the same function of $a ^ { \prime } , b ^ { \prime }$ ,and $c ^ { \prime }$ as $A$ is of $a , \tilde { b }$ and $\pmb { c }$ So,

$$
X = - \frac { b c } { b ^ { \prime } c ^ { \prime } } A ^ { \prime } G \rho x = - \frac { a b c } { a ^ { \prime } b ^ { \prime } c ^ { \prime } } A ^ { \prime } G \rho x ^ { \prime } ,
$$

with similar expressions for $\mathbf { \widetilde { y } }$ and $Z$

To calculate the components of force at $p$ it isnecessary first to find the appropriate value of $\lambda$ then $a ^ { 2 } , b ^ { 4 }$ and $c ^ { \prime }$ ,and then $A ^ { \prime } , B ^ { \prime }$ ,and $C ^ { \beta }$ It is easy, if not practically useful, to find analytical expressions for the components. We have

$$
X = - { \frac { a ^ { \bar { y } c } } { a ^ { \prime } b ^ { \prime } c ^ { \prime } } } G \rho x ^ { \prime } \int _ { 0 } ^ { \infty } { \frac { 2 \pi a ^ { \prime } b ^ { \prime } c ^ { \prime } d u } { ( a ^ { \prime 2 } + u ) { \sqrt { ( a ^ { \prime 2 } + u ) ( b ^ { \prime 2 } + u ) ( c ^ { \prime 2 } + u ) } } } } .
$$

Putting $\mathfrak { U } \ne \lambda = \mathfrak { v }$

$$
\begin{array} { l } { { X = - 2 \pi G \rho a b c x ^ { \prime } \displaystyle \int _ { \lambda } ^ { \infty } \displaystyle \frac { d v } { ( a ^ { 2 } + v ) \sqrt { ( a ^ { 2 } + v ) ( b ^ { 2 } + v ) ( c ^ { 2 } + v ) } } } } \\ { { \ . } } \\ { { \ = - 2 \pi G \rho a b c x ^ { \prime } \displaystyle \int _ { \lambda } ^ { \infty } \displaystyle \frac { d v } { ( a ^ { 2 } + v ) \Delta ( v ) } , } } \end{array}
$$

with similar expressions for $\mathbb { Y }$ and $Z$

This suggests that the exterior potential should be

$$
V = - \pi G \rho a b c \int _ { \lambda } ^ { \infty } \left( 1 - \frac { x ^ { \prime 2 } } { a ^ { 2 } + v } - \frac { y ^ { \prime 2 } } { b ^ { 2 } + v } - \frac { z ^ { \prime 2 } } { c ^ { 2 } + v } \right) \frac { d v } { \Delta ( v ) } .
$$

To establish this, it is suffcient to show that $\partial V / \partial x = - X$ Differentiating (5.5.23) partially with respect to $\pmb { \mathscr { x } }$ we find

$$
\begin{array} { c } { { \displaystyle - \frac { \partial V } { \partial x } = - 2 \pi G \rho a b c x ^ { \prime } \int _ { \lambda } ^ { \infty } \frac { d v } { ( a ^ { 2 } + v ) \Delta ( v ) } } } \\ { { \displaystyle - \pi G \rho a b c \frac { \partial \lambda } { \partial x } \left\{ 1 - \frac { x ^ { \prime 2 } } { a ^ { 2 } + \lambda } - \frac { y ^ { \prime 2 } } { b ^ { 2 } + \lambda } - \frac { z ^ { \prime 2 } } { c ^ { 2 } + \lambda } \right\} \frac { 1 } { \Delta ( \lambda ) } . } } \end{array}
$$

Since $\left\{ x ^ { \prime } , y ^ { \prime } , z ^ { \prime } \right\}$ lies on $S \{ \lambda \}$ , the second term on the right-hand side vanishes, and we are left with the first,which is $X$ ； so, (5.5.23) is established.

# Problems

1. Show that if $a > b > c$ then $A < B < C$ and $A a ^ { 2 } > B b ^ { 2 } > C c ^ { 2 }$ Show also that, for points on the surface of the ellipsoid, the potential is greatest at the ends of the $\pmb { c }$ -axis.

2. Show that for a prolate spheroid where $\mathfrak { a } = \mathfrak { b } = c \sqrt { 1 - e ^ { 2 } }$

$$
C = 4 \pi \left\{ \frac { 1 } { 3 } - 2 \sum _ { n = 1 } ^ { \infty } \frac { e ^ { 2 \pi } } { ( 2 n + 1 ) ( 2 n + 3 ) } \right\} .
$$

3.Show that a spheroid of uniform density cannot have its boundary surface as one of its equipotential surfaces.

4.Find the external potential of a uniform shell bounded by two confocal ellipsoids (a focaloid).

5.Show that if a solid uniform ellipsoid of mass $\pmb { \mathcal { M } }$ is nearly spherical and has axes $\pmb { \mathcal { Q } } .$ $\sqrt { \alpha ^ { 2 } - \hslash }$ and ${ \sqrt { a ^ { 2 } - \tilde { k } } } ,$ the potential at an external point is

$$
- \frac { G M } { r } - \frac { G M } { 1 0 r ^ { 5 } } \{ x ^ { 2 } ( h + k ) + y ^ { 2 } ( - 2 h + k ) + z ^ { 2 } ( h - 2 k ) \}
$$

to the first order of small quantities. Investigate the relation between this and the approximation of MacCullagh's formula.

6.A solid of uniform density $\boldsymbol { \rho }$ is in the form of the spheroid obtained by rotating an ellipse, of latus rectum $\mathfrak { P }$ and eccentricity $^ e$ about the major axis. Show that the potential and intensity of the attracting force at a focus of the generating ellipse are

$$
2 \pi G \rho \frac { p ^ { 2 } } { \frac { 1 } { 2 } - e ^ { 2 } }
$$

and

$$
2 \pi G \rho \frac { \ p } { e ^ { 2 } } \left\{ \mathrm { i n } \frac { \mathbb { 1 } + e } { 1 - e } - 2 e \right\} .
$$

# 5.6Laplace's Equation, Legendre Polynomials, and the Potential of the Earth

Celestial bodies are not homogeneous; their internal densities are increased, owing to pressure, so that we cannot apply the results for homogeneous bodies when investigating their felds. Should some law of density be assumed, the potential can, of course, be calculated by integration. But regardless of the nature of the attracting bodies, the potential must satisfy one of the following two differential equations. For regions away from attracting matter,

$$
\nabla ^ { 2 } \mathbb { V } = 0
$$

which is Laplace's equation.

For regions within attracting matter,

$$
\nabla ^ { 2 } \mathbb { V } = 4 \pi G \rho
$$

where p is the density; this is Poisson's equation. These equations,it has been remarked,make mathematics much easier for anyone who does not have to solve them; but there are times when the solution can be expressed relatively simply. This is notably so in the investigation of the external field ofa body with axial symmetry and which is only slightly distorted from spherical symmetryassumptions that can reasonably be made about many celestial bodies. We shall not discuss Poisson's equation further,but shall consider some of the properties of solutions of Laplace's equation, which are relevant to the expression for the external potential of the Earth.

To derive Laplace's equation,consider first $\widehat { \sf a } _ { r }$ system of point masses, $\mathfrak { W } _ { 2 } \mathfrak { L } _ { 2 }$ at $( \xi _ { i } , \eta _ { i } , \zeta _ { i } )$ Ata point $( x , y , z )$ ,not in contact with a particle,the potential is

$$
V = - G \sum _ { i } \frac { m _ { i } } { \mathfrak { s } _ { i } } ,
$$

where

$$
r _ { i } ^ { 2 } = ( x - \xi _ { i } ) ^ { 2 } + ( y - \eta _ { i } ) ^ { 2 } + ( z - \zeta _ { i } ) ^ { 2 } .
$$

Then

$$
\begin{array} { c } { \displaystyle { \frac { \partial V } { \partial { x } } = G \sum _ { i } \frac { m _ { i } } { \tau _ { i } ^ { 2 } } \frac { \partial r _ { i } } { \partial { x } } } } \\ { \displaystyle { = G \sum _ { i } m _ { i } \frac { ( x - \xi _ { i } ) } { \tau _ { i } ^ { 3 } } , } } \end{array}
$$

and

$$
\frac { \partial ^ { 2 } V } { \partial x ^ { 2 } } = G \sum _ { i } \left\{ \frac { m _ { i } } { r _ { i } ^ { 3 } } - 3 m _ { i } \frac { ( x - \xi _ { i } ) ^ { 2 } } { \bar { r } _ { i } ^ { 5 } } \right\} .
$$

There are similar expressions for $\partial ^ { 2 } V / \partial y ^ { 2 }$ and $\partial ^ { 2 } V / \partial z ^ { 2 }$ , and by addition we find that

$$
\frac { \partial ^ { 2 } \Psi } { \partial x ^ { 2 } } + \frac { \partial ^ { 2 } \Psi } { \partial y ^ { 2 } } + \frac { \partial ^ { 2 } \Psi } { \partial z ^ { 2 } } = 0 ,
$$

which is Laplace's equation. The generalization for continuous attracting bodies is made by replacing the summations by integrals.

A solution of (5.6.1) that is homogeneous in $\mathcal { X } , \ \mathfrak { Y }$ ,and $z$ is called a harmonic function, or a spherical harmonic. We say that $f ( x , y , z )$ is a homogeneous function of degree $\pmb { \mathscr { n } }$ if

$$
\begin{array} { r } { f ( \lambda x , \lambda y , \lambda z ) = \lambda ^ { n } f ( x , y , z ) . } \end{array}
$$

Should $f$ be harmonic, $\pmb { \mathscr { T } }$ is its degree. Harmonic functions are immensely important, and accounts of them are given in standard works on analysis and applied mathematics；a useful introduction is given in $\Re$ amsey's Newtonian Attraction (Ref.12). In this section we consider integral values of $\mathcal { T } _ { \downarrow }$ and shall merely note some properties of immediate concern.

In spherical polar coordinates, Laplace's equation can be writen

$$
\frac { \partial } { \partial \tau } \left( \tau ^ { 2 } \frac { \partial V } { \partial r } \right) + \frac { 1 } { \sin \theta } \cdot \frac { \partial } { \partial \theta } \left( \sin \theta \frac { \partial V } { \partial \theta } \right) + \frac { 1 } { \sin ^ { 2 } \theta } \cdot \frac { \partial ^ { 2 } V } { \partial \phi ^ { 2 } } = 0 .
$$

A harmonic function of degree $\mathfrak { P e }$ will have the form

$$
r ^ { n } S _ { n } ( \theta , \phi ) ,
$$

where $S _ { \pi }$ is called a surface harmonic of order $\pmb { \mathcal { Y } }$ Substituting

$$
V = r ^ { n } S _ { \mathfrak { a } } ( \theta , \phi )
$$

into (5.6.3),we find that $\mathfrak { r } ^ { \mathfrak { n } }$ divides out,and that

$$
\frac { \partial ^ { 2 } S _ { \it \mathrm { r } } } { \partial \theta ^ { 2 } } + \cot \theta \frac { \partial S _ { \it n } } { \partial \theta } + \frac { 1 } { \sin ^ { 2 } \theta } \frac { \partial ^ { 2 } S _ { \it n } } { \partial \phi ^ { 2 } } + n ( n + 1 ) S _ { \it n } = 0 .
$$

Now let

$$
\cos \theta = \mu .
$$

Then (5.6.4) becomes

$$
\frac { \partial } { \partial \mu } \left\{ ( \mathrm { i } - \mu ^ { 2 } ) \frac { \partial S _ { n } } { \partial \mu } \right\} + \frac { 1 } { \mathrm { i } - \mu ^ { 2 } } \frac { \partial ^ { 2 } S _ { n } } { \partial \phi ^ { 2 } } + n ( n + 1 ) S _ { n } = 0 .
$$

Suppose now that the distribution of attracting matter has axial symmetry and that $\widehat { \pmb { \theta } }$ is measured from the axis of symmetry. $\phi$ no longer appears, and if

$$
q ^ { n } P _ { n } \{ \mu \}
$$

is harmonic, then $\mathbf { \mathcal { P } _ { \pi } }$ satisfies the differential equation

$$
\frac { d } { d \mu } \left\{ ( \mathtt { i } - \mu ^ { 2 } ) \frac { d P _ { n } } { d \mu } \right\} + n ( n + 1 ) \mathcal { P } _ { n } = 0 ,
$$

known as Legendre's eguation.

If(5.6.6) is solved in series, the solution takes the form

$$
P _ { n } = ( a _ { 0 } + a _ { 2 } \mu ^ { 2 } + a _ { 4 } \mu ^ { 4 } + \cdots ) + ( a _ { 1 } \mu + a _ { 3 } \mu ^ { 3 } + a _ { 5 } \mu ^ { 5 } + \cdots )
$$

where the first series terminates if n is an even integer,and the second if n is an odd integer. In each case the infinite series fails to converge in the entire range lμl ≤1,and so is of no use to us here. Hence the relevant solution for Pn is a polynomial in μ, known as the Legendre polynomial of order n. The series giving Pn is found to be

$$
\begin{array} { c } { { P _ { n } = { \cal A } _ { n } { \displaystyle \frac { ( 2 n ) ! } { 2 ^ { n } ( n ! ) ^ { 2 } } } \left\{ \mu ^ { n } - { \displaystyle \frac { n ( n - 1 ) } { 2 ( 2 n - 1 ) } } \mu ^ { n - 2 } \right. } } \\ { { \left. + { \displaystyle \frac { n ( n - 1 ) ( n - 2 ) ( n - 3 ) } { 2 \cdot 4 \cdot ( 2 n - 1 ) ( 2 n - 3 ) } } \mu ^ { n - 4 } - \cdots \right\} } } \end{array}
$$

where An,the arbitrary constant, is taken as one, for reasons which will appear shortlv. The series ends ina constant if n is even,and a term in p if n is odd.

There are many ways in which these polynomials can be considered. One, in particular,is often used for their original definition and is useful when calculating the polynomials in the absence of a reference. Consider Figure 5.8.The potential at $P$ due toa mass mat $a$ is

$$
- \frac { m G } { P Q } ,
$$

![](../chunks/Fundamentals of Celestial Mechanics (John M. A. Danby) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0041-0080/ocr/images/c98406d187c719ffe07f5ced3f12af805cdfcb1616fc6a2f3a5b9524e9825d62.jpg)  
Figure 5.8

and clearly the function

$$
\frac { 1 } { \mathcal { P Q } }
$$

is harmonic. Let $o$ be any origin; then since

$$
\begin{array} { c } { { \mathcal { P } Q ^ { 2 } = \tau ^ { 2 } - 2 r a \cos \theta + a ^ { 2 } } } \\ { { = r ^ { 2 } - 2 r a \mu + a ^ { 2 } } } \end{array}
$$

the function

$$
V = { \frac { \vec { \mathbb { 1 } } } { ( r ^ { 2 } - 2 r a \mu + a ^ { 2 } ) ^ { \frac { 1 } { 2 } } / 2 } }
$$

satisfies Laplace's equation. It can be expanded in powers of $a \beta r$ for $r > a$ ,and $r / a$ for $\gamma < a$ Denoting the coefficient of $r ^ { n } / a ^ { n + 1 } \mathrm { o r } a ^ { n } / r ^ { n + 1 }$ by $P _ { \pi }$ , we have

and

$$
\begin{array} { l l } { { V = \displaystyle \frac { 1 } { a } \left\{ 1 + \frac { r } { a } P _ { 1 } + \left( \frac { r } { a } \right) ^ { 2 } P _ { 2 } + \cdots + \left( \frac { r } { a } \right) ^ { n } P _ { n } + \cdots \right\} , } } & { { r < a , \Bigg ] } } \\ { { } } \\ { { { } } } \\ { { { } } } \\ { { { } { { \cal V } } = \displaystyle \frac { 1 } { r } \left\{ 1 + \frac { a } { r } P _ { 1 } + \left( \frac { a } { r } \right) ^ { 2 } P _ { 2 } + \cdots + \left( \frac { a } { r } \right) ^ { n } P _ { n } + \cdots \right\} , } } & { { r > a . \Bigg ] } } \end{array}
$$

The $\mathcal { P } _ { \pi }$ are polynomials in $\mathscr { f }$ and they satisfy Legendre's equation;they must therefore be given by (5.6.7) for some $A _ { \pi }$ $\mathcal { P } _ { \pi }$ is the coefficient of $\hbar ^ { \pi }$ in the expansion of

$$
( \mathtt { I } - 2 \mu \hbar + \mathtt { h } ^ { 2 } ) ^ { - \mathtt { I } / 2 }
$$

$$
( 1 - [ 2 \mu \hbar \div \hbar ^ { 2 } ] ) ^ { - 1 / 2 }
$$

0r

$$
1 + { \frac { 1 } { 2 } } ( 2 \mu \hbar - h ^ { 2 } ) + { \frac { 1 \cdot 3 } { 2 \cdot 4 } } ( 2 \mu h - h ^ { 2 } ) ^ { 2 } + \cdot \cdot \cdot
$$

We find that

$$
\begin{array} { l } { P _ { 1 } = \mu } \\ { P _ { 2 } = \displaystyle \frac { 1 } { 2 } ( 3 \mu ^ { 2 } - 1 ) } \\ { P _ { 3 } = \displaystyle \frac { 1 } { 2 } ( 5 \mu ^ { 3 } - 3 \mu ) } \\ { P _ { 4 } = \displaystyle \frac { 1 } { 8 } ( 3 5 \mu ^ { 4 } - 3 0 \mu ^ { 2 } + 3 ) , \quad \mathrm { e t c . } } \end{array}
$$

and in general $\mathcal { P } _ { \mathfrak { r } }$ is given by (5.6.7) where $A _ { \mathfrak { r } } = 1$

Let us assume that the Earth has symmetry about the north-south axis, and that $\boldsymbol { \vartheta }$ is measured from the north pole. The external potential must be of the form

$$
V = - { \frac { \bar { M } G } { r } } \left\{ \bar { 1 } - { \frac { 1 } { r ^ { 2 } } } \bar { J } _ { 2 } P _ { 2 } - { \frac { 1 } { r ^ { 3 } } } \bar { J } _ { 3 } P _ { 3 } - \cdot \cdot \cdot \right\} .
$$

where the J's are constants. Here we have neglected the term with $P _ { 1 }$ altogether, since it can be removed by a change of origin north or south so that it coincides with the center of gravity of the Earth. In the same way the term in $\Im / \Re ^ { 2 }$ in the derivation of MacCullagh's formula (Section 5.4) vanishes by virtue of the choice of the center of gravity as origin.

An advantage of (5.6.9) is that it can immediately be written down, once axial symmetry has been assumed, and any suitable experiment (such as the study of the orbit of an artificial satellite) can be used to determine the J's. For a spherical Earth allthe J's would be zero; in factJ2 is of the order of 10-3 (the unit of length being the Earth's equatorial radius),J4 is of the order of J2,and the others are smaller. The inclusion of the odd P's allows for a lack of symmetry about the equator. The harmonics just discussed are called zonal harmonics. For practical purposes it is also necessary to consider harmonics that depend on the longitude; these are tesseral and sectorial harmonics, and require associated Legendre polynomials for their expression. They will not be discussed here.

# Problems

1. If $\pmb { \ V }$ is a harmonic function of degree $\pmb { \mathcal { R } }$ ，show that

$$
\frac { \partial ^ { a } } { \partial x ^ { a } } \frac { \partial ^ { b } } { \partial y ^ { b } } \frac { \partial ^ { c } } { \partial z ^ { c } } \frac { \gamma } { \gamma }
$$

is also harmonic, of degree $( n - a - b - c )$

2.If $r ^ { n } S _ { \pi }$ is harmonic, show that $z ^ { - \gamma _ { 3 } - 1 } S _ { 3 }$ is also harmonic.

3.Solve Legendre's equation in series, justifying the comments made in the text.

4.From the formula

$$
\frac { \mathbb { i } } { \sqrt { \mathbb { i } - 2 \mu t + t ^ { 2 } } } = \sum _ { 0 } ^ { \infty } P _ { n } ( \mu ) \mathbb { i } ^ { n }
$$

derive the recursion relations

$$
P _ { n + 1 } ( \mu ) = { \frac { 2 n + 1 } { n + 1 } } \mu P _ { n } ( \mu ) - { \frac { n } { n + 1 } } \bar { P } _ { n - 1 } ( \mu ) , n = 1 , 2 , 3 , . . .
$$

and

$$
\ L _ { n + 1 } ^ { p ^ { \prime } } ( \mu ) = P _ { n - 1 } ^ { \prime } ( \mu ) = ( 2 \mu + 1 ) P _ { n } ( \mu ) , \quad n = 1 , 2 , 3 , \dots
$$

5. Show that

$$
\int \limits _ { - 1 } ^ { + \frac { 1 } { 4 } } \bar { P } _ { \pi } \bar { P } _ { m } d \mu = 0
$$

if $\pi \neq \pi$ and

$$
\int _ { - \frac { 1 } { 3 } } ^ { + \frac { 1 } { 2 } } ( P _ { \pi } ) ^ { 2 } d \mu = \frac { 2 } { 2 \pi + 1 } .
$$

6. Compare the first two terms of (5.6.9) with MacCullagh's formula.

7.A circular ring of radius $\pmb { \mathcal { a } }$ has line density $\pmb { \rho }$ Taking the origin as the center of the ring and measuring $\boldsymbol { \theta }$ from the axis perpendicular to its plane, write down the potential of the ring at points along the axis, and hence, or otherwise, show that the potential at $( r , \theta )$ is given by

$$
V _ { 1 } = - 2 \pi G \rho \left\{ 1 - \frac { 1 } { 2 } \left( \frac { r } { a } \right) ^ { 2 } P _ { 2 } + \frac { 1 \cdot 3 } { 2 \cdot 4 } \left( \frac { r } { a } \right) ^ { 4 } P _ { 4 } - \cdot \cdot \cdot \right\}
$$

for $\tau < a$ and

$$
V _ { 1 } = - 2 \pi G \rho \left\{ \frac { a } { r } - \frac { 1 } { 2 } \left( \frac { a } { r } \right) ^ { 3 } P _ { 2 } + \frac { 1 \cdot 3 } { 2 \cdot 4 } \left( \frac { a } { r } \right) ^ { 4 } P _ { 4 } - \cdot \cdot \cdot \right\}
$$

for $\gamma > \mathcal { Q }$

8.A circular disc has radius $\pmb { \mathcal { L } }$ and density $\boldsymbol { \rho }$ per unit area. Prove that its potential at $\{ \boldsymbol { \mathfrak { F } } , \boldsymbol { \widehat { \theta } } \}$ is given by

$$
\begin{array} { l } { { \displaystyle \bar { V } _ { 1 } = - 2 \pi a G \rho \left\{ \mathbb { i } - \frac { \bar { r } } { a } P _ { 1 } + \frac { 1 } { 2 } \left( \frac { \bar { r } } { a } \right) ^ { 2 } \bar { P } _ { 2 } \right. } } \\ { { \displaystyle \left. - \frac { 1 \cdot 1 } { 2 \cdot 4 } \left( \frac { \bar { r } } { a } \right) ^ { 4 } P _ { 4 } + \frac { 1 \cdot 1 \cdot 3 } { 2 \cdot 4 \cdot 6 } \left( \frac { \bar { r } } { a } \right) ^ { 6 } P _ { 6 } - \cdots \right\} } } \end{array}
$$

for $r < a$ and $0 \leq \theta \leq \pi / 2$ ,the sign of the term in $P _ { \ I }$ being changed if $\pi / 2 < \theta \leq \pi$ and

$$
V _ { 2 } = - 2 \pi a G \rho \left\{ \frac { 1 } { 2 } \cdot \frac { a } { r } - \frac { 1 \cdot 1 } { 2 \cdot 4 } \left( \frac { a } { r } \right) ^ { 3 } P _ { 2 } + \frac { 1 \cdot 1 \cdot 3 } { 2 \cdot 4 \cdot 6 } \left( \frac { a } { r } \right) ^ { 5 } P _ { 4 } - \cdot \cdot \cdot \right\}
$$

for $\tau > a$ The coordinate system is similar to that of problem 7.

9.Find, in the form of an infinite series, the potential due to a fat circular annulus (e.g., Saturn's ring) at points moderately near the center of the ring.

If a small but massive planet occupies the center of the ring, show that the maximum deflection of the plumb line on its surface (on account of theattraction of the ring) will occur in latitude $4 5 0$ ,approximately.

# 5.7 The Tidal Distortion of a Liquid Sphere Under the Action of a Distant Point Mass

The theory of this chapter will be illustrated by its application to two problems of astronomical interest: these concern the tides and possible figures of rotating fluid masses.

Consider a spherical mass M of incompressible fuid of density $\beta$ called the primary. Suppose that this is made subject to the tidal influence of a second body which is at a great distance from the primary compared with the radius of the latter,and which is such that for gravitational purposes it can be treated as a point mass M'. Let the origin be at the center of mass of the primary, and take coordinates (r,0,） in spherical polars.The potential at (r,0,） due to M'atthe point (R,0,），wherer<R,is

$$
\begin{array} { l } { { \displaystyle { V = - \frac { M ^ { \prime } G } { ( R ^ { 2 } + r ^ { 2 } - 2 R r \cos \theta ) ^ { 1 / 2 } } } } } \\ { { \displaystyle { \quad = - \frac { M ^ { \prime } G } { R } \left( 1 - 2 \frac { r } { R } \cos \theta + \frac { r ^ { 2 } } { R ^ { 2 } } \right) ^ { - 1 / 2 } } } } \\ { { \displaystyle { \quad = - \frac { M ^ { \prime } G } { R } - \frac { M ^ { \prime } G r \cos \theta } { R ^ { 2 } } - \frac { M ^ { \prime } G r ^ { 2 } ( 3 \cos ^ { 2 } \theta - 1 ) } { 2 R ^ { 3 } } + \cdots } } } \end{array}
$$

The first term is constant if $\mathcal { R }$ is constant,and so gives rise to no force on M.The second gives rise to a uniform force with intensity -(M'G/R²). This can be neutralized if the axes of reference are rotating with an acceleration M'G/R² while the center of mass of M always remains at the origin. This condition is fulfilled in the case of the Earth-Moon system if we suppose that the Moon remains at a constant distance from the Earth;the x-axis will then always point toward the Moon. We are left with the remaining terms,which constitute the tide raising potential Vr. Sincer<R,only the first term will be considered,and expressing this in cartesian coordinates,where the $\pmb { \mathscr { x } }$ -axis points toward $M ^ { f }$ ,we have

$$
V _ { \widehat { \pmb { \mathscr { T } } } } = - \mu ( x ^ { 2 } - \frac { 1 } { 2 } y ^ { 2 } - \frac { 1 } { 2 } z ^ { 2 } ) ,
$$

where

$$
\mu = \frac { M ^ { \prime } G } { R ^ { 3 } } .
$$

We have to find out what effect this will have on the shape of the primary. The condition to apply is that the free surface of $\Im \hat { \mathcal { A } }$ must be an equipotential surface in the combined fields of $\overrightarrow { i } \overrightarrow { + }$ and $\overrightarrow { M } ^ { t }$ This is reasonable,since,if possible, matter tends to move from places of higher to lower potential energy,and on the free surface of a liquid there is nothing to prevent such an adjustment.

Alternatively, consider the pressure in the liquid.Pressure is “force per unit area.” Consider an element of mass $\delta \mathfrak { m }$ with volume $\delta x \delta y \delta z$ and density $\mathscr { P }$ If Px is the pressure acting on the face Sy δz, the force acting on that face must be $\mathfrak { P } _ { z } \mathfrak { S } \mathfrak { Y } \delta z$ The difference between this force and the force acting on the opposite face is

$$
\left\{ { \frac { \partial g _ { x } } { \partial x } } \delta y \delta z \right\} \delta x .
$$

But this must be equal to the net force in the $\pmb { \mathcal { X } }$ direction which is acting on the element. This force is $\mathbb { X } \delta \pmb { \mathscr { n } }$ ,or $X _ { \beta } \delta x \delta y \delta z$ Hence

$$
\frac { \partial p _ { x } } { \partial x } \delta x = X \rho \delta x .
$$

This leads at once to the equation for the general change of pressure:

$$
\begin{array} { r } { \frac { \dot { a } \mathfrak { p } } { \rho } = \nabla V \cdot \dot { a } \mathfrak { r } . } \end{array}
$$

Now,over & free surface the pressure must be constant,so that $\pmb { \ V }$ must be constant and the surface is an equipotential.

Let us assume that $\pmb { \mathbb { M } }$ takes up the figure of an ellipsoid; then the potential at $\{ \boldsymbol { z } , \boldsymbol { y } , z \}$ is

$$
{ \scriptstyle { \frac { 1 } { 2 } } } G \rho ( A x ^ { 2 } + B y ^ { 2 } + C z ^ { 2 } ) - \mu ( x ^ { 2 } - { \scriptstyle { \frac { 1 } { 2 } } } y ^ { 2 } - { \scriptstyle { \frac { 1 } { 2 } } } z ^ { 2 } ) + \mathrm { ~ c o n s t a n t } .
$$

This must be constant over the surface

$$
{ \frac { x ^ { 2 } } { a ^ { 2 } } } + { \frac { y ^ { 2 } } { b ^ { 2 } } } + { \frac { z ^ { 2 } } { c ^ { 2 } } } = 1 ,
$$

and the condition for this is that the coefficients of $x ^ { 2 } , y ^ { 2 }$ ,and $z ^ { 2 }$ must be proportional; i.e.,

$$
a ^ { 2 } \left( A - 2 \frac { \mu } { G \rho } \right) = b ^ { 2 } \left( B + \frac { \mu } { G \rho } \right) = c ^ { 2 } \left( C + \frac { \mu } { G \rho } \right) .
$$

This provides two equations for the ratios of the axes,and (5.5.10) is a third; they can be solved, and the solutions are considered in more detail in the following section on rotating fuid masses. As in the case of the rotating fuid there are solutions with three unequal axes,but we are concerned with small distortions from spherical figures,and for these two axes are equal. This means that there are two symmetrical bulges pointing toward and away from $M ^ { t }$ ，

Let $\dot { \boldsymbol { b } } = c ;$ then if $c = a \{ 1 - \varepsilon \}$ ,we have

$$
\begin{array} { c } { { \frac 4 3 \pi \left( 1 - \frac 4 5 \epsilon \right) - 2 \frac { \mu } { G \rho } = \left( \vec { \bf i } - \epsilon \right) ^ { 2 } \left\{ \frac 4 3 \pi \left( 1 + \frac 2 5 \epsilon \right) + \frac \mu { G \rho } \right\} } } \\ { { = \frac 4 3 \pi \left( 1 - \frac 8 5 \epsilon \right) + \frac \mu { G \rho } + \cdot \cdot \cdot } } \end{array}
$$

We may neglect terms of the order $\epsilon ^ { 2 }$ and $\mu \varepsilon$ ,and solve this equation to find

$$
\epsilon = \frac { 4 5 } { 1 6 \pi } \frac { \mu } { G \rho } .
$$

If this is applied to the Earth-Moon system,and we assume that the Earth is a fuid mass with density 5.52, then we have $M ^ { \prime } = 7 . 3 8 \times 1 0 ^ { 2 5 }$ gm and $\mathcal { R } = 3 . 8 4 \times 1 0 ^ { \frac { 7 } { 4 } 0 }$ cm. Then

$$
\varepsilon = 0 . 8 4 \times \mathrm { i } \Omega ^ { - 5 } .
$$

Taking the Earth's radius as $6 . 4 \times 1 0 ^ { 8 } ~ \mathrm { c m }$ ，the difference between the axes is $5 . 4 \times \dot { \mathbb { I } } 0 ^ { 3 }$ cm.

Comparison with actuality is not profitable here. The Earth is not a fuid mass, nor is it even entirely covered with water. Also, there are complicating factors such as the friction between the water and the sea beds, which delays the tides at any place.(This friction is believed to be partly responsible for the slowing down of the Earth's rotation, mentioned in Section 1.11.） In practice the forecasting of tides is largely empirical.

# 5.8Ellipsoidal Figures of Rotating Fluid Masses

We shall consider only homogeneous fuid masses rotating uniformly as solid bodies.Then from Section 3.4 we can treat the problem as one of statics, provided we include the term

$$
- \frac { 1 } { 2 } \omega ^ { 2 } \{ x ^ { 2 } + y ^ { 2 } \}
$$

per unit mass in the potential function, where the angular velocity is w about $D z$ Here we shall consider only possible ellipsoidal forms;but it has been shown by Poincaré that thereare infinitelymany other possibilities.

For an ellipsoid a surface of constant pressure is given by

$$
( \omega ^ { 2 } - A G \rho ) x ^ { 2 } + ( \omega ^ { 2 } - B G \rho ) y ^ { 2 } - C G \rho z ^ { 2 } = \mathrm { \ c o n s t a n t { \vec { u } } } .
$$

Assuming the free surface to be

$$
{ \frac { x ^ { 2 } } { a ^ { 2 } } } + { \frac { y ^ { 2 } } { b ^ { 2 } } } + { \frac { z ^ { 2 } } { c ^ { 2 } } } = 1 ,
$$

the condition for this also to be a surface of constant pressure is

$$
a ^ { 2 } ( \omega ^ { 2 } - A G \rho ) = b ^ { 2 } ( \omega ^ { 2 } - B G \rho ) = - c ^ { 2 } C G \rho .
$$

Eliminating $\omega$ we get

$$
a ^ { 2 } b ^ { 2 } ( B - A ) = ( a ^ { 2 } - b ^ { 2 } ) c ^ { 2 } C .
$$

So,we can have $a = b$ when the figure is an oblate spheroid, known as a Maclaurin spheroid. The nearly spherical case will be discussed later in this section. If $a \neq b ,$ the substitution for $A , B$ and $C$ according to the formulas of Section 5.5, into (5.8.2) gives

$$
\int _ { 0 } ^ { \infty } \left\{ \frac { 1 } { a ^ { 2 } } + \frac { 1 } { \bar { b } ^ { 2 } } - \frac { 1 } { c ^ { 2 } } + \frac { u } { a ^ { 2 } \bar { b } ^ { 2 } } \right\} \frac { u \bar { d } u } { \Delta ^ { 2 } } = 0 .
$$

If $a$ and $\bar { \boldsymbol { b } }$ are known, this can be regarded as an equation for finding ${ \mathcal { C } } _ { \bar { \tau } } ^ { * }$ and since the left-hand side is negative for small $^ c$ and positive for large $\mathfrak { L } _ { \mathfrak { s } }$ there must be a real root.

From(5.8.1） the value of $\omega ^ { 2 }$ is found to be

$$
\begin{array} { c } { { \omega ^ { 2 } = \displaystyle \frac { ( A a ^ { 2 } - B b ^ { 2 } ) G \rho } { ( a ^ { 2 } - b ^ { 2 } ) } } } \\ { { { } } } \\ { { { } = 2 \pi G \rho a \bar { b } c \displaystyle \int _ { 0 } ^ { \infty } \displaystyle \frac { u d u } { ( a ^ { 2 } + u ) ( \bar { b } ^ { 2 } + u ) \Delta } . } } \end{array}
$$

Since the right-hand side is positive, the corresponding value of $\omega$ is real. Also from (5.8.1） we have

$$
\begin{array} { l } { { a ^ { 2 } \omega ^ { 2 } = G \rho ( A a ^ { 2 } - C c ^ { 2 } ) } } \\ { { \ } } \\ { { \qquad = 2 \pi G \rho a b c ( a ^ { 2 } - c ^ { 2 } ) \displaystyle \int _ { 0 } ^ { \infty } \displaystyle \frac { \imath d u } { ( a ^ { 2 } + u ) ( c ^ { 2 } + u ) \Delta } , } } \\ { { \ \qquad = 2 \pi G \rho a b c ( a ^ { 2 } - c ^ { 2 } ) \displaystyle \int _ { 0 } ^ { \infty } \displaystyle \frac { \imath d u } { ( a ^ { 2 } + u ) ( c ^ { 2 } + u ) \Delta } , } } \end{array}
$$

so that $c < a$ Similarly, $c < \ b$ so that the ellipsoid rotates about its shortest axis.An ellipsoid of this type is known asa Jacobi ellipsoid. There are no nearly spherical Jacobi ellipsoids,but they forma one-parameter family,branching off from the Maclaurin spheroids. The sequence of models depends on the ratio $\omega ^ { 2 } / \rho$ and not only on $\omega$ Numerical values have been found by Darwin,and have been discussed, in particular,by Jeans (Refs.13,14).

Returning to the Maclaurin spheroids,consider the case of a slightly distorted sphere. Using the formulas (5.5.15) and following the method of the preceding section, we find

$$
\epsilon = \frac { 1 5 } { 1 5 \pi } \cdot \frac { \omega ^ { 2 } } { G \rho } .
$$

Taking $\rho = 5 . 5 2 $ and $\omega = 2 \pi / 8 6 , 1 6 4$ (since there are $8 6 , 1 6 4$ seconds ina sidereal day),we find e= 4.3 ×10-3.This leads to a predicted difference of about 431 miles between the polar and equatorial diameters. This is more than the actual fattening, but the discrepancy is hardly surprising in view of the assumptions that we have made.

# Problems

1. Show that there are no Jacobi ellipsoids which are only slightly distorted spheres.

2.The polar and equatorial diameters of Jupiter are observed to be 133,200 and142,700km,respectively,and its mean density is1.34.Assuming that it isa homogeneous fuid and that its distortion is the result of a solid bodyrotation,find the predicted period ofrotation.The observed period is of the order of ten hours;what conclusions can be drawn from this？

3. The period of rotation of the Sun is of the order of 25.4 days,and its mean density is 1.41. Assuming that it is a homogeneous fuid mass and rotates as a solid body,what distortion from a spherical figure is predicted?

4.Show that for a Maclaurin spheroid:

$$
\frac { \omega ^ { 2 } } { 2 \pi G \rho } = \frac { 3 - 2 e ^ { 2 } } { e ^ { 3 } } \sqrt { 1 - e ^ { 2 } } \sin ^ { - 1 } e - 3 \left( \frac { 1 } { e ^ { 2 } } - 1 \right) ,
$$

where $c ^ { 2 } = a ^ { 2 } \{ 1 - e ^ { 2 } \}$ By expanding this for the cases e small and e nearly equal to one,show that the left-hand side is small at each extreme. Find the maximum possible value for the left-hand side.

5.Assuming that the Moon is composed of a homogeneous fluid of density 3.34 and total mass $\mathrm { 7 . 3 6 \times \vec { \mathrm { \textmd { i } } } \vec { \mathrm { U } } ^ { 2 5 } \ g i r a }$ and that it is at a constant distance $\mathfrak { 3 . 8 4 \times 1 0 ^ { 1 0 } }$ cm from the Earth, find the predicted tidal distortion of its figure.

6.A homogeneous fuid body has a slow uniform rotation；it is subject to the tidal influence of a distant body which lies in the plane of its equator. Investigate the total distortion of the body.

Apply this theory to the predicted figure of the Moon, using the data above,given that the period of rotation is 27.32 days.

7.Compare the tide-raising potentials of the Sun and Moon on the Earth. Assuming that the Earth is a homogeneous fluid (and neglecting its rotation),find approximate figures for the Earth when the three bodies are ina straight line and when the angle between the lines joining the Earth to the Sun and Moon is $9 0 ^ { \circ }$

8. Show that the potential of a plane annulus bounded by concentric circles at a point on its axis is

$$
2 \pi G \rho \{ \vec { \mathfrak { f } } ^ { \prime } - \vec { \mathfrak { f } } \} ,
$$

where $\boldsymbol { \rho }$ is the mass per unit area and $\vec { \underline { { \xi } } } , \vec { \underline { { \xi } } } ^ { \prime }$ are the distances of the point from the inner and outer edges.

A planet is at the center of a uniform plane annulus of mass M and inner and outer radii $a$ and $b$ large compared with the planet's radius. Show that to a first approximation the effect of the ring on the figure of equilibrium of the planet is equivalent to that of a rotational velocity $\omega$ where

$$
\omega ^ { 2 } = { \frac { G M } { a b ( a + b ) } } .
$$

9.A homogeneous gravitating solid is in the form of a prolate spheroid of small ellipticity $\epsilon _ { : }$ where $\epsilon = \{ \alpha - c \} / \alpha$ and $\pmb { \mathcal { a } }$ and $\pmb { \mathcal { L } }$ are the semiaxes of a meridian section. The spheroid is rotating about its axis with angular

velocity ω. Show that the direction of a plumb line at any point on the spheroid will pass through the center,provided

$$
\omega ^ { 2 } = { \frac { 6 \varepsilon g } { 5 a } } ,
$$

where g is the approximately constant value of gravity at the surface.

10.Two masses M are placed at distances c on opposite sides of the center ofa gravitating liquid sphere of radius $\pmb { \mathcal { Q } }$ and total mass $I ^ { \mu }$ .Show that, neglecting powers of a/c above the third, the liquid is deformed into a prolate spheroid, the ratio of the minor axis to the major being

$$
1 - { \frac { 1 5 } { 2 } } \cdot { \frac { M } { M ^ { \prime } } } \left( { \frac { a } { c } } \right) ^ { 3 } .
$$

If two more particles of the same mass M are placed at distances c from the center on an axis at right angles to the line joining the former pair, show that the surface becomes an oblate spheroid, the ratio of the axes being the same as in the previous case.

11.A planet consists of a point mass and an atmosphere of negligible mass. Investigate the degree of small distortions due to rotation and to tidal forces.

Assuming that Jupiter is such a planet, compare the figures for the distortion and rotation with those of problem 2. What conclusion can be drawn？
