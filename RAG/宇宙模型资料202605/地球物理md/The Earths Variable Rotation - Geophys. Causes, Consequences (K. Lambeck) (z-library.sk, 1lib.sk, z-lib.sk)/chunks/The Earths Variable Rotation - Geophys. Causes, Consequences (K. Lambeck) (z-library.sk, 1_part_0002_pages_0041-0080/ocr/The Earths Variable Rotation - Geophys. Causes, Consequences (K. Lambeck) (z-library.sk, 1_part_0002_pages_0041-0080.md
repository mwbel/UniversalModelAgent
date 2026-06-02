The potential of the free surface will be

$$
( 1 + k _ { \mathrm { f } } ) \Delta U _ { 2 } ,
$$

where $k _ { \mathrm { f } }$ (also of degree 2) is the fluid potential Love number. The free surface is raised with respect to the centre of the Earth by

$$
( 1 + k _ { \mathrm { f } } ) \Delta U _ { 2 } / g = h _ { \mathrm { f } } \Delta U _ { 2 } / g .
$$

Hence

$$
k _ { \mathrm { f } } = 0 . 9 3 4 .
$$

The observed flattening, $\pmb { F _ { \mathbf { o } } }$ ,of the equipotential surface relates to $C _ { 2 0 }$ by

$$
\begin{array} { r } { F _ { \mathrm { { o } } } = \frac { 3 } { 2 } ( - C _ { 2 0 } + \frac { 1 } { 3 } \Omega ^ { 2 } R _ { \mathrm { { e } } } / g _ { \mathrm { { e } } } ) + O ( F _ { \mathrm { { o } } } ^ { 2 } ) , } \end{array}
$$

and using this instead of $F _ { \mathsf { h } }$ in the above analysis gives

$$
k _ { \mathrm { o } } = 3 ( C - A ) G / R ^ { 5 } \Omega ^ { 2 } = 0 . 9 4 2 .
$$

Munk & MacDonald interpret $k _ { \mathbf { o } }$ as a secular Love number, the difference between $k _ { \mathrm { f } }$ and $k _ { \mathbf { o } }$ reflecting the difference between the hydrostatic flattening and the observed flattening. This difference is of the same order as the neglected terms in (2.4.9) and (2.4.13) and is not very significant. Here $k _ { \mathbf { o } }$ is merely a convenient constant.

An example of the use of the fluid Love number is the computation of the variation of the polar moment of inertia with time due to a secular change in $\pmb { \Omega }$ ， assuming that the planet remains in hydrostatic equilibrium. The potential of the deformation by the centrifugal force is

$$
\Delta U _ { 2 } { = } - \textstyle \frac { 1 } { 3 } k _ { \mathrm { o } } \Omega ^ { 2 } ( t ) R _ { \mathrm { e } } ^ { 2 } P _ { 2 0 } \left( \sin \phi \right)
$$

which may also be writen in the form (2.4.1), or

$$
\Delta U _ { 2 } { = } ( G M / R ) C _ { 2 0 } P _ { 2 0 } .
$$

Equating these two expressions,and using(2.4.5) and the definition

$$
I = \frac { 1 } { 3 } \sum _ { i } I _ { i i } = \mathrm { c o n s t a n t } ,
$$

(see Rochester & Smylie (1974) for further discussion) gives

$$
I _ { 3 3 } ( t ) = I [ 1 - { \textstyle \frac { 2 } { 9 } } k _ { \mathrm { o } } R _ { \mathrm { e } } ^ { 5 } \Omega ^ { 2 } ( t ) / G I ] .
$$

# THREE

# ROTATIONAL DYNAMICS

# 3.1 Rigid body rotation

The fundamental equations governing the rotation of a body are Euler's dynamical equations. These describe the rotational response of a body to an applied torque $\mathbf { L }$ by

$$
\begin{array} { r } { \dot { \bf H } = { \bf L } , } \end{array}
$$

where $\mathbf { H }$ is the angular momentum of the body. This equation describes the motion in an inertial reference frame X.For many problems it is more convenient to express forces, velocities and torques with respect to axes that are fixed in the rotating body. These body-fixed axes are denoted by $\pmb { \mathrm { x } }$ and their angular velocity by $\pmb { \ 6 0 }$ ； the components $\omega _ { i } ( i = 1 , 2 , 3 )$ of $\pmb { \ 6 0 }$ specify the angular velocities with which the axes $\pmb { x } _ { i }$ turn about themselves. Euler's equations, referred to these axes, are (see,for example, Goldstein 1970)

$$
\mathrm { d } { \bf H } / \mathrm { d } t + \omega \wedge { \bf H } = { \bf L } ,
$$

where the components of $\mathbf { H }$ and $\mathbf { L }$ are now along the moving axes. For a body of mass $M$

$$
\begin{array} { l } { \displaystyle { \mathbf { H } = \int _ { M } \mathbf { x } \wedge ( \boldsymbol { \mathbf { \ * } } \mathbf { \boldsymbol { \mathbf { \rho } } } \mathbf { \boldsymbol { \mathbf { \ * } } } \mathbf { x } ) \mathrm { d } M } } \\ { \displaystyle { \quad = \int _ { M } ( \mathbf { x } \cdot \mathbf { x } \mathbf { 1 } - \mathbf { x } \cdot \mathbf { x } ^ { \mathrm { T } } ) \boldsymbol { \mathbf { \ * } } \mathrm { d } M } } \\ { \displaystyle { \quad = \mathbf { I } \cdot \boldsymbol { \mathbf { \ * } } \mathbf { \boldsymbol { \mathbf { \ * } } } } , } \end{array}
$$

where $\gimel ( \equiv \delta _ { i j } ,$ with $i , j = 1 , 2 , 3 ; \delta _ { i j } = 1$ if $i = j ,$ otherwise $\delta _ { i j } = 0$ isa unit matrix, $\mathbf { x ^ { T } }$ denotes the transpose of $\pmb { \mathrm { x } }$ and

$$
\mathbf { I } = \int _ { M } \left( \mathbf { x } \cdot \mathbf { x 1 } - \mathbf { x } \cdot \mathbf { x } ^ { \mathsf { T } } \right) \mathrm { d } M
$$

is the second-degree symmetric inertia tensor. With (3.1.3) Euler's equation becomes

$$
( \mathbf { d } / \mathbf { d } t ) ( \mathbf { I } \cdot \mathbf { \omega } \omega ) + \infty \wedge ( \mathbf { I } \cdot \mathbf { \omega } \omega ) = \mathbf { L } .
$$

For axes $\pmb { x } _ { \imath }$ fixed in a rigid body,the inertia tensor does not vary with time and the axes can be chosen such that the products of inertia vanish, or

$$
I _ { i j } = - \int _ { M } x _ { i } x _ { j } \mathrm { d } M = 0 \quad \mathrm { f o r } \quad i \neq j .
$$

A further simplification results if the body is rotationally symmetric about $\pmb { x } _ { 3 }$ ,for then $I _ { 1 1 } = I _ { 2 2 } \equiv A$ ， $\cal I _ { 3 3 } \equiv C$ and

$$
\begin{array} { r } { \mathrm { d } \omega _ { 1 } / \mathrm { d } t + \big [ ( C - A ) / A \big ] \omega _ { 2 } \omega _ { 3 } = L _ { 1 } / A , } \\ { \mathrm { d } \omega _ { 2 } / \mathrm { d } t - \big [ ( C - A ) / A \big ] \omega _ { 1 } \omega _ { 3 } = L _ { 2 } / A , , } \\ { \mathrm { d } \omega _ { 3 } / \mathrm { d } t = L _ { 3 } / C . \big ) } \end{array}
$$

For zero torques, the solution of these equations is

$$
\left. \begin{array} { l } { \omega _ { 1 } = a _ { 0 } \cos \sigma _ { \mathrm { r } } t + b _ { 0 } \sin \sigma _ { \mathrm { r } } t } \\ { \omega _ { 2 } = a _ { 0 } \sin \sigma _ { \mathrm { r } } t - b _ { 0 } \cos \sigma _ { \mathrm { r } } t } \\ { \omega _ { 3 } = \cos \mathrm { c o n s t a n t } = \Omega , } \end{array} \right\}
$$

where $a _ { 0 } , b _ { 0 }$ and $\pmb { \Omega }$ are constants of integration and the frequency of the motion $\pmb { \sigma _ { \mathrm { r } } }$ is defined by

$$
\sigma _ { \mathrm { r } } = [ ( C - A ) / A ] \Omega .
$$

Thus,for a small displacement of the principal axis $x _ { 3 }$ from the rotation axis $\pmb { \ 6 0 }$ ，the latter rotates in a circular path about $x _ { 3 } ,$ according to (3.1.8) with a frequency $\pmb { \sigma _ { \tau } }$ that is a function of the mass distribution in the body, and with an amplitude and phase that are determined by the initial displacement. This motion is referred to as the free Eulerian precession or free nutationt of the rigid body. For values of $\pmb { A }$ ， $C$ and $\pmb { \Omega }$ that are appropriate to the Earth (section 2.4), σr = 1/306 rev d-l.

The equations (3.1.7) and their solution (3.1.8) provide a useful zeroth-order approximation to any discussion of the Earth's rotation. Their solution is stable if the motion of $\pmb { \ 6 0 }$ is about a principal axis that is either one of maximum or minimum inertia. If $\pmb { \omega }$ rotates about an intermediate principal axis, the motion becomes unstable; the rotation axis begins to wander away to a point diametrically opposite before returning to the original position. The Earth rotates about an axis that lies close to the mean position of the greatest principal axis and in most studies the motion can be considered as stable.

Equations (3.1.5) are valid for an instant $t$ when the inertial system Xcoincides with the moving axes x. For a subsequent instant $t ^ { \prime }$ the equations remain valid provided that a new inertial system $\mathbf { X ^ { \prime } }$ is defined that coincides with the rotating axis at this time. Thus a complete description of the motion also requires the geometric relation between the positions of the axes X, $\mathbf { X } ^ { \prime }$ ... at times $t , t ^ { \prime }$ ... This relation can be defined with the aid of the three Eulerian angles $\pmb { \alpha _ { i } }$ (Woolard 1953). The inertial system $\mathbf { X }$ is defined by the plane of the mean ecliptic (the $X _ { 1 } X _ { 2 }$ -plane) and the mean equinox $( X _ { 1 } )$ for the epoch $T _ { 0 } . X _ { 2 } { \mathrm { l i e s } } { \frac { 1 } { 2 } } \pi$ to the East of $X _ { 1 }$ ,and $X _ { 3 }$ is normal to the ecliptic; $\pmb { x _ { 3 } }$ is directed to the mean position of the rotation axis, $\pmb { x _ { 1 } }$ is directed towards the mean meridian of Greenwich,and $\pmb { x _ { 2 } }$ is $\scriptstyle { \frac { 1 } { 2 } } \pi$ East of $\pmb { x _ { 1 } }$ . Then, with Woolard's definition,

$\pmb { \alpha } _ { 1 } =$ inclination of the ${ \pmb x } _ { 1 } { \pmb x } _ { 2 }$ -plane on the mean ecliptic.

$\pmb { \alpha } _ { 2 } =$ angle in the $X _ { 1 } X _ { 2 }$ -plane between $X _ { 1 }$ and the descending node of the ${ \pmb x } _ { 1 } { \pmb x } _ { 2 }$ -plane on the ecliptic. $\pmb { \alpha _ { 2 } }$ is measured positive eastward from $X _ { 1 }$

$\pmb { \alpha _ { 3 } = }$ angle in the ${ \pmb x } _ { 1 } { \pmb x } _ { 2 }$ -plane between the descending node and the

$x _ { 1 }$ -axis. $\alpha _ { 3 } = \omega _ { 3 } T \simeq \Omega T .$

$$
\begin{array} { r } { \mathbf { X } = \mathcal { R } _ { 3 } ( - \alpha _ { 2 } ) \mathcal { R } _ { 1 } ( \alpha _ { 1 } ) \mathcal { R } _ { 3 } ( - \alpha _ { 3 } ) \mathbf { x } , } \end{array}
$$

where $\mathcal { R } _ { i } ( \alpha _ { j } )$ denotes an anti-clockwise rotation through an angle $\alpha _ { j }$ about an axis $x _ { i } .$ The time derivatives of $\alpha _ { j }$ represent the motion of the $\pmb { \mathrm { x } }$ -axes with respect to the inertial frame. Resolving these velocities into components along the $\pmb { x } _ { i }$ -axes and equating them to $\omega _ { i }$ gives (Woolard 1953; Webster 1959)

$$
\begin{array} { r } { \left( \begin{array} { c } { \dot { \alpha } _ { 1 } } \\ { \dot { \alpha } _ { 2 } \sin \alpha _ { 1 } } \\ { \dot { \alpha } _ { 3 } + \dot { \alpha } _ { 2 } \cos \alpha _ { 1 } } \end{array} \right) = R ( - \alpha _ { 3 } ) \left( \begin{array} { c } { \omega _ { 1 } } \\ { \omega _ { 2 } } \\ { \omega _ { 3 } } \end{array} \right) } \end{array}
$$

with

$$
\mathscr { R } ( - \alpha _ { 3 } ) = \left( \begin{array} { c c c } { \cos \alpha _ { 3 } } & { - \sin \alpha _ { 3 } } & { 0 } \\ { \sin \alpha _ { 3 } } & { \cos \alpha _ { 3 } } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right) .
$$

These are Euler's kinematic equations of motion. With (3.1.5) they describe completely the motion of $\pmb { \omega }$ both in space and with respect to the body. Studies of polar motion and changes in the speed of rotation usually involve (3.1.5); studies of precession and nutation usually involve (3.1.1O). The two sets of equations indicate that, for every oscillation of $\pmb { \ 6 0 }$ with respect to $\mathbf { x } .$ ，there will be an associated nutation in space. Since $\dot { \alpha } _ { 3 } \simeq \Omega$ the frequency of the nutation in space of the Eulerian motion is

$$
\pmb { \sigma } _ { \mathrm { r } } + \pmb { \Omega }
$$

and the free wobble is associated with a nearly diurnal oscillation in space. A complete discussion of the forced precession and nutations of a rigid body is given by Woolard (1953) and Kinoshita (1977). (See also Murray 1978.)

The kinematic representation of the motion of $\pmb { \omega }$ ,originally due to Poinsot in 1851, is illustrated in figure 3.1. If no torques act on the body, $\mathbf { H }$ is fixed in space and $\pmb { \ 6 0 }$ traces out a cone about the principal axis $\pmb { \mathrm { x } } _ { 3 }$ . This is the free Eulerian nutation or wobble, given by (3.1.8), with frequency $\pmb { \sigma _ { \uparrow } }$ ； $\pmb { \ 6 0 }$ also traces out a smaller cone about $\mathbf { H }$ and this is the associated nutation described by(3.1.1O). The axes $\pmb { \omega }$ , H and $\pmb { \mathrm { x } } _ { 3 }$ are coplanar, with $\mathbf { H }$ lying between the other two. The frequency (3.1.11) of this nutation is approximately diurnal. Its amplitude relative to the wobble amplitude is of the order $( C -$ $A ) / A$ or 1/300.

# 3.2 Non-rigid body rotation: general formulation

Apart from the ratios $( C - A ) / C$ or $( C - A ) / A$ ，no geophysical parameters enter into the discussion of rigid body motion and, in the absence of external torques, the motion is completely predictable once the initial conditions have been established. Such motion would be of no further geophysical interest. The Earth's actual motion differs from rigid body motion in two respects: the inertia tensor I is time dependent, and motion occurs relative to the axes $\pmb { \mathrm { x } }$ Hence the total angular momentum $\mathbf { H }$ must be written as

$$
\mathbf { H } ( t ) = \mathbf { I } ( t ) \boldsymbol { \omega } ( t ) + \mathbf { h } ( t ) ,
$$

where

$$
\mathbf { h } = \int _ { M } \left( \mathbf { x } \wedge \mathbf { u } \right) \mathrm { d } M ,
$$

is the angular momentum vector due to motion, with velocity u,

![](images/745b95d51ab053774d505f4d7746f0a7385eca933d248da45e692f19787f8569.jpg)  
Figure 3.1. The Poinsot representation of rigid body rotation. $\mathbf { H }$ is the angular momentum axis, $\pmb { \ 6 0 }$ the instantaneous rotation axis,and $\pmb { \mathrm { x } _ { 3 } }$ the principal axis. In the absence of external torques, $\mathbf { H }$ is fixed in space; $\pmb { \omega }$ describes a periodic nearly diurnal motion in space about $\mathbf { H }$ and a much larger motion, the free Eulerian nutation, about $\mathbf { x _ { 3 } }$

relative to x. Substituting (3.2.1) into (3.1.5) gives

$$
( \mathbf { d } / \mathbf { d } t ) [ \mathbf { I } ( t ) \pmb { \omega } + \mathbf { h } ( t ) ] + \pmb { \omega } \wedge \mathbf { I } ( t ) \pmb { \omega } + \mathbf { h } ( t ) = \mathbf { L } .
$$

These are the Liouville equations (Routh 1905; Munk & MacDonald 1960).

In most discussions on non-rigid rotation, the excursions from uniform rotation are small and it is convenient to write

$$
\omega _ { 1 } = \Omega m _ { 1 } , \qquad \omega _ { 2 } = \Omega m _ { 2 } , \qquad \omega _ { 3 } = \Omega ( 1 + m _ { 3 } ) ,
$$

where $\pmb { \Omega }$ is the mean angular velocity of the Earth. The $m _ { i }$ are small dimensionless quantities, of the order of $1 0 ^ { - 6 }$ or less. The $m _ { 1 } , m _ { 2 } , 1 + m _ { 3 }$ represent the direction cosines of $\pmb { \omega }$ relative to $\pmb { x _ { 3 } }$ ； $m _ { 1 }$ and $m _ { 2 }$ are the components of polar motion or wobble and $\Omega \mathrm { d } m _ { 3 } / \mathrm { d } t$ is nearly the acceleration in diurnal rotation. Changes in the inertia tensor and the relative angular momenta $h _ { i }$ are also small in most problems and it is convenient to write (3.2.3) in a pertur-

bation form. We write

$$
\begin{array} { r l r } & { I _ { 1 1 } = A + \Delta I _ { 1 1 } ( t ) \qquad I _ { 2 2 } = A + \Delta I _ { 2 2 } ( t ) , \qquad I _ { 3 3 } = C + \Delta I _ { 3 3 } ( t ) , } & \\ & { I _ { i j } = \Delta I _ { i j } ( t ) , \qquad i \ne j , } & { ( 3 . 2 5 , } \end{array}
$$

where $\Delta I _ { i j } ( t ) / C$ are small quantities. Substituting (3.2.4) and (3.2.5) into (3.2.3),and neglecting the squares and products of small quantities, the equations of motion reduce to

$$
\begin{array} { c } { { \dot { m } _ { 1 } / \sigma _ { \mathrm { r } } + m _ { 2 } = \psi _ { 2 } , \qquad \dot { m } _ { 2 } / \sigma _ { \mathrm { r } } - m _ { 1 } = - \psi _ { 1 } , } } \\ { { \dot { m } _ { 3 } = \dot { \psi } _ { 3 } , ~ } } \end{array}
$$

with

$$
\begin{array} { r l } & { \psi _ { 1 } = \big [ \Omega ^ { 2 } \Delta I _ { 1 3 } + \Omega \Delta \dot { I } _ { 2 3 } + \Omega h _ { 1 } + \dot { h } _ { 2 } - L _ { 2 } \big ] / \Omega ^ { 2 } ( C - A ) } \\ & { \psi _ { 2 } = \big [ \Omega ^ { 2 } \Delta I _ { 2 3 } - \Omega \Delta \dot { I } _ { 1 3 } + \Omega h _ { 2 } - \dot { h _ { 1 } } + L _ { 1 } \big ] / \Omega ^ { 2 } ( C - A ) } \\ & { \psi _ { 3 } = \big [ - \Omega ^ { 2 } \Delta I _ { 3 3 } - \Omega h _ { 3 } + \Omega \int _ { 0 } ^ { t } L _ { 3 } \mathrm { d } t \big ] / \Omega ^ { 2 } C , } \end{array}
$$

and

$$
\sigma _ { \mathrm { r } } = [ ( C - A ) / A ] \Omega .
$$

The omission of the squares and products of small quantities is adequate in most studies. For example, the period of the free nutation is given with a precision of about 1d by the above development and this compares with an observational precision of about 2 d (chapter 5). For other investigations,such as the ellipticity of the wobble, some of the smaller terms must be retained.

Complex notation gives a more compact form of the equations of motion. Writing

$$
\begin{array} { c } { { { \bf { m } } = m _ { 1 } + \mathrm { j } m _ { 2 } , } } \\ { { \ \Psi = \psi _ { 1 } + \mathrm { j } \psi _ { 2 } , } } \\ { { \Delta { \bf { I } } = \Delta I _ { 1 3 } + \mathrm { j } \Delta I _ { 2 3 } , } } \\ { { \ { \bf { h } } = h _ { 1 } + \mathrm { j } h _ { 2 } , } } \\ { { { \bf { L } } = L _ { 1 } + \mathrm { j } L _ { 2 } , } } \end{array}
$$

then

$$
\left. \begin{array} { r } { \mathbf j ( \dot { \mathbf m } / \sigma _ { \tau } ) + \mathbf m = \pmb { \Psi } , } \\ { \dot { m } _ { 3 } = \psi _ { 3 } , } \end{array} \right\}
$$

and

$$
\boldsymbol { \Psi } = [ 1 / \Omega ^ { 2 } ( C - A ) ] [ \Omega ^ { 2 } \Delta \mathrm { I } - \mathrm { j } \Delta \dot { \mathrm { I } } + \Omega \mathrm { h } - \mathrm { j } \dot { \mathrm { h } } + \mathrm { j } \mathrm { \mathbf { L } } ] .
$$

The solution for $\pmb { \psi } = \mathbf { 0 }$ is

$$
\mathbf { m } = \mathbf { m _ { 0 } } \mathbf { e } ^ { \mathbf { j } \sigma _ { \mathrm { r } } t } .
$$

Otherwise

$$
\mathbf { m } = e ^ { \mathrm { j } \sigma _ { 0 } \iota } \biggl [ \mathbf { m } _ { 0 } - \mathbf { j } \sigma _ { 0 } \int _ { - \infty } ^ { \iota } \boldsymbol { \Psi } ( \tau ) e ^ { - \mathrm { j } \sigma _ { r } \tau } \mathrm { d } \tau \biggr ] .
$$

The $\psi _ { i }$ are referred to as excitation functions and include all factors that perturb the rotational motion from that defined by the rigid body motion discussed above (equations 3.1.4-9). They include, for example,changes in $\Delta I _ { i j }$ and $\pmb { h } _ { i }$ arising from the atmospheric and oceanic circulation, the Earth's elastic deformation due to centrifugal and tidal forces, large-scale mass redistribution associated with mantle convection，and electromagnetic coupling of core motions to the mantle. Equations (3.2.6) clearly separate the astronomical and geophysical problems: astronomers observe the motion of the rotation axis with respect to the Earth's surface; geophysical observations and theory provide the information for evaluating the excitation functions $\psi _ { i } .$ . The problem is to explain the $m _ { i }$ in terms of the available geophysical data,or, failing that, to deduce certain geophysical properties from the observed rotation variations.

Two aspects of the choice of the terrestrial system need further elaboration. (i) The $\pmb { x _ { i } }$ are assumed to be fixed to the Earth, but this is incompatible with the notion of a non-rigid Earth. High-frequency deformations of the solid Earth occur due to tidal forces, for example,while at the other end of the spectrum, slow secular displacements occur due to tectonic upheaval and continental drift. The former can often be monitored and corrections may be applied to the observations,while the latter, being secular and slow, do not disrupt greatly the higher-frequency irregularities in rotation. A pragmatic choice of a fixed reference frame is one that is defined by the coordinates of observatories on tectonically stable continents, whose motions are partly predictable by current global plate tectonics models. Unfortunately, many of the astronomical obser-vatories have not always been placed with this condition in mind: the International Latitude Service,which has monitored polar motion since 19oo,has four of its five stations in tectonically complex areas and these stations may have been subject to important local or regional displacements (section 5.3.2).

(ii) In theoretical discussions of the excitation functions, other choices of axes are sometimes convenient. Routh (19o5) discusses some possibilities. One choice is such that $h _ { i } = 0$ at all times. These are the mean axes introduced by Tisserand in his Mécanique Celeste. Such axes are fixed in the body only when all relative motion ceases. Another choice is to select $x _ { i }$ such that $I _ { i j } = \delta _ { i j } I _ { i j }$ at all times. These axes were introduced by G. H. Darwin in his study of geological influences on the rotation axis. Choices such as these often simplify the discussion of the geophysical influences on rota-tion, but they do not permit a ready comparison of the excitation functions with the astronomical observations that relate the motion of the rotation axis with respect to the station positions.

In many studies it is possible to separate the wobble equations $( 3 . 2 . 6 a )$ from the l.o.d. equation $( 3 . 2 . 6 b )$ since the excitation functions $\psi _ { 1 }$ and $\psi _ { 2 }$ do not contain the same elements of the inertia tensor and angular momenta and torque vectors as does $\psi _ { 3 }$ . Some cross-coupling may occur in certain situations. One example is the pole tide. The periodic wobble (3.2.11) sets up an oscillation in the Oceans which, due to the continent distribution, is not symmetrical about the instantaneous rotation axis. This pole tide contributes to $\Delta I _ { 3 3 }$ and introduces a perturbation in $m _ { 3 }$ , of the same frequency as the wobble (chapter 6). But this is small and negligible. A case where the cross-coupling may be much more important is discussed in section 3.5.

# 3.3 Rotation of spheroid with fluid core

A special case of non-rigid body rotation is that of a rigid shell containing a fluid-flled cavity. In the initial state the shell and fluid rotate together about an axis ${ \mathfrak { o o } } _ { 0 }$ that is also a principal axis $\pmb { \mathrm { x } } _ { 3 }$ . The cavity is spherical and the fluid is homogeneous,incompressible and inviscid. At time $\pmb { t _ { 0 } }$ an impulse torque ${ \bf L } = { \bf L } \delta \left( t - t _ { 0 } \right)$ ， $\mathbf { \mathit { L } _ { 3 } } = \mathbf { 0 }$ acts on the shell, and the instantaneous rotation axis now wobbles about $\pmb { \mathrm { x } } _ { 3 }$ For this idealized case the core and shell are completely decoupled: the shell motion is not transmitted to the core and the latter continues to rotate as a rigid body about its original axis. The

frequency of the wobble is now

$$
\begin{array} { r } { \sigma = [ ( C _ { \mathrm { m } } - A _ { \mathrm { m } } ) / A _ { \mathrm { m } } ] \Omega , } \end{array}
$$

where $C _ { \bf m } , A _ { \bf m } , A _ { \bf m }$ are the principal moments of the shellor mantle. If $C _ { \mathrm { c } } , A _ { \mathrm { c } } , A _ { \mathrm { c } }$ denote the principal moments of the core,

$$
\sigma \simeq [ ( C - A ) / ( A - A _ { \mathrm { c } } ) ] \Omega = ( A / A _ { \mathrm { m } } ) \sigma _ { \mathrm { r } } ,
$$

and the effect of the liquid cavity is to shorten the wobble period. The frequency of the motion of $\pmb { \ 6 0 }$ in space is

$$
( A / A _ { \mathrm { m } } ) \sigma _ { \mathrm { r } } + \Omega
$$

and is almost unchanged from the value (3.1.11) for the rigid body. The axes $\pmb { \mathrm { x } } _ { 3 }$ ， $\pmb { \ 6 0 }$ and $\mathbf { H }$ remain coplanar and the ratio of the amplitudes of wobble and nearly diurnal nutation is only marginally modified: Poinsot's representation (figure 3.1) remains essentially unmodified.

For a spheroidal cavity, the interior flow field departs from a rigid body rotation. Kelvin showed that the relative motion consists of a rigid rotation and a deformational motion due to the flow of the fluid past the spheroidal boundary. This secondary flow exerts asymmetrically distributed pressures over the boundary that couple the core to the shell. This form of coupling is referred to as pressure coupling or inertial coupling and has been studied by W. Hopkins in 1839, by Kelvin, Hough and F. Sludskii in 1896 and by Poincaré in 1910. The equations of motion for the shell and the core have been derived by Lamb (1932) using the Helmholtz equations to describe the flow in the fluid of uniform vorticity. The shell motion is defined by the direction cosines $m _ { 1 } , m _ { 2 }$ , and that of the core by $n _ { 1 } , n _ { 2 }$ Both motions are with respect to axes fixed in the shell. The equations of motion now reduce to

$$
\left. \begin{array} { c } { \dot { \bf m } - \mathrm { j } \Omega [ ( C - A ) / A _ { \mathrm { m } } ] \mathbf { m } = - \mathrm { j } \Omega [ ( C - A ) / A _ { \mathrm { m } } ] \Psi , } \\ { \dot { \bf n } - \mathrm { j } \Omega ( 1 + f _ { \mathrm { c } } ) ( \mathbf { m } - \mathbf { n } ) = 0 , } \end{array} \right\}
$$

where $f _ { \mathrm { c } }$ is the flattening of the core. (See Lamb (1932) p. 726, but note that in (3.3.2) $\pmb { \mathbb { n } }$ is the motion with respect to mantle-fixed axes).For the Earth $f _ { \mathrm { c } } \simeq 1 / 4 0 0$ . The excitation function $\pmb { \psi }$ acts on the mantle only and the core responds passively. In the case $\pmb { \psi } = \pmb { 0 }$ ， the free-oscillation frequency of the system is

$$
\sigma = ( A / A _ { \mathrm { m } } ) ( 1 + f _ { \mathrm { c } } ) \sigma _ { \mathrm { r } } .
$$

The coupling is quite weak and the core mainly abstains from Eulerian nutation. The solution also points to the existence of a second free-oscillation mode or wobble whose frequency is

$$
\pmb { \sigma } = - \Omega [ 1 + ( A / A _ { \mathrm { m } } ) f _ { \mathrm { c } } ]
$$

and which represents a retrograde motion of the pole about $\pmb { x _ { 3 } }$ . Its period differs from a sidereal day by $A f _ { \mathrm { c } } / A _ { \mathrm { m } } ,$ ,or by about $4 \mathrm { m i n }$ This is the diurnal free wobble and has again been the subject of attention in the recent literature (Rochester, Jensen & Smylie 1974; Toomre 1974; M.L. Smith 1977). The associated free nutation of $\pmb { \mathfrak { o } } \mathfrak { d }$ in space about $\mathbf { H }$ has the same frequency

$$
\sigma + \Omega \simeq - ( A f _ { \mathrm { c } } / A _ { \mathrm { m } } ) \Omega
$$

and is also retrograde. H, $\pmb { \ 6 0 }$ and $\pmb { \mathrm { x } } _ { 3 }$ remain coplanar, as for the Eulerian wobble, but H and $\pmb { \ 6 0 }$ lie on opposite sides of $\pmb { \mathrm { x } } _ { 3 }$ (figure 3.2). The ratio of this wobble and associated nutation is $A f _ { \mathrm { c } } / A _ { \mathrm { m } }$ and now the nutation amplitude is much larger than the wobble amplitude, by a factor of about 4OO for the Earth. Thus, if the Earth has an observable nearly diurnal wobble - sometimes claimed to have an amplitude of $\mathbf { 0 . 0 1 }$ (see Yatskiv (1972) and Rochester et al. (1974) for a summary of results) - the associated wobble in space must have an amplitude about 4Oo times larger and a period of about $\mathbf { 4 0 0 d }$ The astronomically observed quantity would be the angle $\mathbf { \omega } _ { \mathbf { \omega } \omega } \mathbf { - } \mathbf { \mathbb { H } }$ but it is not seen in the data (Rochester et al. 1974; Capitaine 1975).

# 3.4 Rotational deformation

The Earth's principal departure from rigid body rotation is its deformation due to the variable centrifugal force,and it is convenient to describe other perturbations in the motion with respect to this deformed state. The potential of the centrifugal force at point $P ,$ distant $l$ from the instantaneous rotation axis, is

$$
U _ { \mathrm { c } } = { \textstyle \frac { 1 } { 2 } } \omega ^ { 2 } l ^ { 2 } .
$$

The direction cosines of $\pmb { \ 6 0 }$ are $m _ { i } = \omega _ { i } / \omega$ so that

$$
l ^ { 2 } = \sum _ { i } x _ { i } ^ { 2 } - \left( \sum _ { i } \frac { \omega _ { i } x _ { i } } { \omega } \right) ^ { 2 }
$$

![](images/574235f69d296e6afeafac807df71e22dd623dd830c62911dd2142a2961b143e.jpg)  
Figure 3.2. The Poinsot representation of the nearly diurnal free wobble for a body containing a spheroidal, liquid-filled cavity. The motion of $\pmb { \omega }$ about $\pmb { \mathrm { x } } _ { 3 }$ describes a nearly diurnal free wobble,and the much larger motion of $\pmb { \omega }$ about H describes the associated nutation in space.

and

$$
U _ { \mathrm { c } } { = } \frac { 1 } { 2 } { \omega } ^ { 2 } r ^ { 2 } { - } \frac { 1 } { 2 } \bigg ( \sum _ { i } { \omega } _ { i } x _ { i } \bigg ) ^ { 2 } ,
$$

with

$$
\begin{array} { l } { r ^ { 2 } = \displaystyle \sum _ { i } x _ { i } ^ { 2 } , } \\ { \omega ^ { 2 } = \displaystyle \sum _ { i } \omega _ { \ i } ^ { 2 } \simeq \Omega ^ { 2 } ( 1 + 2 m _ { 3 } ) = \Omega ^ { 2 } . } \end{array}
$$

This potential can be further arranged as

$$
\begin{array} { r } { U _ { \mathrm { c } } = \frac { 1 } { 3 } \omega ^ { 2 } r ^ { 2 } + \Delta U _ { \mathrm { c } } , } \end{array}
$$

where

$$
\Delta U _ { \mathrm { c } } = \textstyle { \frac { 1 } { 6 } } \sum _ { i } { \omega _ { i } ^ { 2 } } ( x _ { i + 1 } ^ { 2 } + x _ { i + 2 } ^ { 2 } - 2 x _ { i } ^ { 2 } ) - \sum _ { i } { \omega _ { i } } \omega _ { i + 1 } x _ { i } x _ { i + 1 } .
$$

The first term in (3.4.1) results in a small, purely radial, deformation (about $\mathbf { 0 . 0 0 4 ~ c m }$ at the Earth's surface for typical variations in $m _ { 3 }$ of ${ { 1 0 } ^ { - 8 } }$ (Lambeck 1973)). The second term is harmonic in degree 2 and can be written in terms of spherical coordinates $( r , \phi , \lambda )$ for the

point $P$ as

$$
\begin{array} { r l } & { \Delta U _ { \mathrm { c } } = ( R ^ { 2 } / 6 ) ( \omega _ { 1 } ^ { 2 } + \omega _ { 2 } ^ { 2 } - 2 \omega _ { 3 } ^ { 2 } ) ( r / R ) ^ { 2 } P _ { 2 0 } ( \sin \phi ) - ( R ^ { 2 } / 3 ) ( r / R ) ^ { 2 } } \\ & { \qquad \times \left( \omega _ { 1 } \omega _ { 3 } \cos \lambda + \omega _ { 2 } \omega _ { 3 } \sin \lambda ) P _ { 2 1 } ( \sin \phi ) + ( R ^ { 2 } / 1 2 ) ( r / R ) ^ { 2 } \right. } \\ & { \qquad \left. \times [ ( \omega _ { 2 } ^ { 2 } - \omega _ { 1 } ^ { 2 } ) \cos 2 \lambda - 2 \omega _ { 1 } \omega _ { 2 } \sin 2 \lambda ] \times P _ { 2 2 } ( \sin \phi ) . \right. } \end{array}
$$

This potential deforms the Earth and, for an elastic body, the further change can be described at the Earth's surface, $\boldsymbol r = \pmb R$ ,by

$$
\Delta U _ { \mathrm { c } } ^ { \prime } ( R ) = k _ { 2 } \Delta U _ { \mathrm { c } } ( R ) .
$$

Outside the Earth,

$$
\Delta U _ { \mathrm { c } } ^ { \prime } ( r ) = \left( R / r \right) ^ { 3 } k _ { 2 } \Delta U _ { \mathrm { c } } ( R ) .
$$

This can be written in the form (2.4.1) as

$$
\Delta U _ { \mathrm { c } } ^ { \prime } ( R ) = \frac { G M } { r } \bigg ( \frac { R } { r } \bigg ) ^ { 3 } \sum _ { m } \big ( C _ { 2 m } ^ { * } \cos m \lambda + S _ { 2 m } ^ { * } \sin m \lambda \big ) F _ { . . n } ( \sin \phi ) ,
$$

with

$$
\begin{array} { r l r } & { C _ { 2 0 } ^ { * } = ( R ^ { 3 } / 6 G M ) ( \omega _ { 1 } ^ { 2 } + \omega _ { 2 } ^ { 2 } - 2 \omega _ { 3 } ^ { 2 } ) k _ { 2 } , } & \\ & { C _ { 2 1 } ^ { * } = - ( R ^ { 3 } / 3 ) ( \omega _ { 1 } \omega _ { 3 } / G M ) k _ { 2 } , \qquad S _ { 2 1 } ^ { * } = - ( R ^ { 3 } / 3 ) ( \omega _ { 2 } \omega _ { 3 } / G M ) k _ { 2 } ; } & \\ & { C _ { 2 2 } ^ { * } = ( R ^ { 3 } / 1 2 ) [ ( \omega _ { 2 } ^ { 2 } - \omega _ { 1 } ^ { 2 } ) / G M ] k _ { 2 } , } & \\ & { } & { S _ { 2 2 } ^ { * } = - ( R ^ { 3 } / 6 ) ( \omega _ { 1 } \omega _ { 2 } / G M ) k _ { 2 } . } \end{array}
$$

Equating $C _ { 2 m } ^ { * }$ and $\pmb { S } _ { 2 m } ^ { * }$ with the appropriate elements in the second-degree inertia tensor (2.4.5) gives the following changes $\Delta I _ { i j } ( t )$ in the Earth's inertia tensor due to the rotational deformation:

$$
\begin{array} { r l } & { \Delta I _ { 1 3 } = \frac { k _ { 2 } R ^ { 5 } \omega _ { 1 } \omega _ { 3 } } { 3 G } = \frac { k _ { 2 } R ^ { 5 } \Omega ^ { 2 } m _ { 1 } ( 1 + m _ { 3 } ) } { 3 G } } \\ & { \qquad = \frac { k _ { 2 } R ^ { 5 } \Omega ^ { 2 } m _ { 1 } } { 3 G } , } \\ & { \Delta I _ { 2 3 } = \frac { k _ { 2 } R ^ { 5 } \omega _ { 2 } \omega _ { 3 } } { 3 G } = \frac { k _ { 2 } R ^ { 5 } \Omega ^ { 2 } m _ { 2 } ( 1 + m _ { 3 } ) } { 3 G } } \\ & { \qquad = \frac { k _ { 2 } R ^ { 5 } \Omega m _ { 2 } } { 3 G } . } \end{array}
$$

The excitation functions $\psi _ { 1 }$ and $\psi _ { 2 }$ become

$$
\left. \begin{array} { c } { { \psi _ { 1 } = \displaystyle \frac { \Omega ^ { 2 } } { C - A } k _ { 2 } \frac { R ^ { 5 } } { 3 G } \left( m _ { 1 } + \frac { \dot { m } _ { 2 } } { \Omega } \right) = \frac { k _ { 2 } } { k _ { \mathrm { o } } } \left( m _ { 1 } + \frac { \dot { m } _ { 2 } } { \Omega } \right) , } } \\ { { \psi _ { 2 } = \displaystyle \frac { \Omega ^ { 2 } } { C - A } k _ { 2 } \frac { R ^ { 5 } } { 3 G } \left( m _ { 2 } - \frac { \dot { m } _ { 1 } } { \Omega } \right) = \frac { k _ { 2 } } { k _ { \mathrm { o } } } \left( m _ { 2 } - \frac { \dot { m } _ { 1 } } { \Omega } \right) , } } \end{array} \right\}
$$

with

$$
k _ { \mathrm { { o } } } = 3 ( C - A ) G / \Omega ^ { 2 } R ^ { 5 } = 3 G M C _ { 2 0 } / \Omega ^ { 2 } R ^ { 3 } = 0 . 9 4 2 .
$$

The $m _ { i }$ are of the order ${ { 1 0 } ^ { - 6 } }$ with a period of about 430 d so that $\left| \dot { \mathbf { m } } \right| / \Omega \simeq 5 \times 1 0 ^ { - 9 } \ll m$ Hence $\psi _ { i } \simeq k _ { 2 } m _ { i } / k _ { \mathrm { o } }$ .Writing

$$
\sigma _ { 0 } = \sigma _ { \mathrm { r } } ( 1 - k _ { 2 } / k _ { \mathrm { o } } ) ,
$$

and substituting the excitations $\psi _ { i }$ into (3.2.6) gives (in the absence of all other excitations)

$$
\dot { m } _ { 1 } / \sigma _ { 0 } + m _ { 2 } = 0 , \qquad \dot { m } _ { 2 } / \sigma _ { 0 } - m _ { 1 } = 0 .
$$

The solution is

$$
\left. \begin{array} { c } { { m _ { 1 } = m _ { 0 } \cos { \left( \sigma _ { 0 } t + \theta \right) } , } } \\ { { } } \\ { { m _ { 2 } = m _ { 0 } \sin { \left( \sigma _ { 0 } t + \theta \right) } , } } \end{array} \right\}
$$

and the motion is circular,as for the rigid body motion, but the frequency is reduced from $\pmb { \sigma _ { \mathrm { r } } }$ to ${ \pmb \sigma } _ { \mathbf { 0 } }$ . Observations of the body tide indicate that $k _ { 2 } { \simeq } 0 . 2 9 { \mathrm { - } } 0 . 3 0$ (chapter 6) so that $\sigma _ { 0 } \simeq$ $2 \pi / 4 4 5 \mathrm { \ r e v \ d } ^ { - 1 }$ ，close to the observed frequency of about $\sigma _ { \mathbf { 0 } } \simeq$ $2 \pi / 4 3 5 \mathrm { r e v } \mathrm { d } ^ { - 1 }$ (chapter 8). Elasticity lengthens the period of the Eulerian precession from about 305 d to $\mathbf { 4 3 5 d }$

Figure $3 . 3 ( a )$ illustrates the motion m of the rotation axis and of the excitation axis $\boldsymbol { \Psi }$ relative to the body-fixed axes $\pmb { \mathrm { x } }$ Rigid body rotation is illustrated by case $( a )$ in which the $\pmb { \mathrm { x } }$ -axes are also principal axes. Initially m is aligned with $\pmb { \mathrm { x } } _ { 3 }$ and $\pmb { \psi } = \pmb { 0 }$ ， $\mathbf { m } = \mathbf { 0 }$ A disturbance shifts the excitation axis $\psi _ { \mathrm { r } }$ for this rigid body and now m turns about this new position with frequency $\pmb { \sigma _ { \mathrm { r } } }$ and with an amplitude $m _ { 0 }$ that is a function of the initial displacement. For the elastic case, the rotation axis wobbles freely about a mean position. The excitation function is given by (3.4.3) or

$$
\Psi _ { \bf D } = ( k _ { 2 } / k _ { \mathrm { o } } ) \mathbf { m }
$$

and is a consequence of the bulge adjusting itself to the continuously

![](images/0f87d42cee6bf7cb66acbdde1a4fc16196554dcc2b3597ac94b227ffe4f0acf7.jpg)  
Figure 3.3. Motion of the rotation axis with respect to Earth-fixed axes. $( a )$ The rotation for the rigid Earth. In the initial state $\mathbf { m } = \mathbf { 0 }$ ， $\pmb { \psi } = \pmb { 0 }$ A perturbation shifts the excitation pole to $\mit \Psi _ { \mathrm { ^ r } }$ and m now moves about $\psi _ { \ r }$ with frequency $\pmb { \sigma _ { \tau } }$ and amplitude ${ \bf { m _ { 0 } } }$ $( b )$ The motions for an elastic Earth. For the same initial displacement, the mean excitation pole $\pmb { \Psi }$ now moves by an amount $k _ { \mathrm { o } } / ( k _ { \mathrm { o } } - \bar { k _ { 2 } } ) \Psi$ Both $\mathbf { m }$ and the instantaneous excitation pole $\psi = \psi _ { \mathrm { r } } + \psi _ { \mathrm { D } }$ move about this position.

changing position of m. The equations of motion now are

$$
\mathbf { j } ( \mathbf { m } / \sigma _ { \mathrm { r } } ) + \mathbf { m } = \boldsymbol { \Psi } _ { \mathbf { D } }
$$

or

$$
\mathbf { j } ( \dot { \mathbf { m } } / \sigma _ { 0 } ) + \mathbf { m } = 0 ,
$$

where $\sigma _ { 0 } = \sigma _ { \mathrm { r } } ( 1 - k _ { 2 } / k _ { \mathrm { o } } )$ is the frequency of the free oscillation of the elastic Earth. From (3.4.2) it follows that $\psi _ { \mathrm { { D } } }$ represents the Orientation of the principal axis of the Earth with respect to $\pmb { \mathrm { x } }$

If the Earth is subject to a forced excitation,the total excitation $\pmb { \psi }$ is the sum of two parts: the forcing function $\psi _ { \tau }$ ,evaluated as if the Earth were rigid, and $\psi _ { \mathrm { { D } } }$ . The equations of motion are

$$
\mathrm { j } ( \dot { \bf m } / \sigma _ { \mathrm { r } } ) + \bf m = \boldsymbol \psi _ { \mathrm { r } } + \boldsymbol \psi _ { \mathrm { D } }
$$

or

$$
\mathbf { j } ( \dot { \mathbf { m } } / \sigma _ { 0 } ) + \mathbf { m } = [ k _ { \mathrm { o } } / ( k _ { \mathrm { o } } - k _ { 2 } ) ] \pmb { \| } _ { \pmb { r } } .
$$

The elastic yielding of the Earth therefore modifies the amplitude of the excitation function by a factor $k _ { \mathrm { o } } / ( k _ { \mathrm { o } } - k _ { 2 } )$ ；the rotational deformation increases the amplitude of the wobble by about 1.4 from what it would be if the Earth were rigid. If the excitation $\psi _ { \mathrm { r } }$ is due entirely to changes in the inertia tensor then the function $\psi _ { \mathrm { r } } + \psi _ { \mathrm { D } }$ defines the principal axis, while if $\psi _ { \mathrm { r } }$ is caused entirely by relative motion or by torques, the principal axis is defined by $\psi _ { \mathrm { { D } } }$

Figure $3 . 3 ( b )$ illustrates the motions of the axes in this case.The mean position of the excitation axis is given by $\Psi = k _ { \mathrm { o } } / ( k _ { \mathrm { o } } - k _ { 2 } ) \psi _ { \mathrm { r } }$ (Munk & MacDonald 1960), while the instantaneous rotation axis m moves about it with amplitude $\mathbf { m } _ { 0 } k _ { \mathrm { o } } / ( k _ { \mathrm { o } } - k _ { 2 } )$ compared with ${ \bf \ m _ { 0 } }$ if the Earth were rigid. Likewise the instantaneous excitation pole $\pmb { \psi }$ rotates about this position with an amplitude given by $\psi _ { \mathrm { { D } } }$ . The m, $\boldsymbol { \Psi }$ and $\pmb { \psi }$ are coplanar,and the separation $\mathbf { m } - \boldsymbol { \Psi }$ between m and the instantaneous excitation pole remains the same.

# 3.5Damped linear motion

The Earth's response to a disturbing potential is not purely elastic but lags it. This anelastic response can be expressed in a very general way by the complex Love number ${ \bf k } _ { 2 }$ (chapter 2). Writing ${ \bf k } _ { 2 } =$ $k _ { 2 } + \mathrm { j } \kappa ,$ the excitation functions (3.4.3) are

$$
\begin{array} { r } { \pmb { \psi } \simeq [ ( k _ { 2 } + \mathrm { j } \kappa ) / k _ { \mathrm { o } } ] \mathbf { m } , } \end{array}
$$

and the equations of motion are

$$
\mathbf { j } \mathbf { \dot { m } } / \mathbf { \sigma } \mathbf { \sigma } _ { 0 } + \mathbf { m } = 0
$$

with

$$
\begin{array} { r } { \mathbf { \sigma } \bullet _ { 0 } = \sigma _ { \mathrm { r } } ( 1 - k _ { 2 } / k _ { \mathrm { o } } ) - \mathbf { j } \sigma _ { \mathrm { r } } \kappa / k _ { \mathrm { o } } . } \end{array}
$$

That is, to allow for anelasticity it suffices to introduce the complex frequency ${ \bf \sigma } _ { 0 } = \sigma _ { 0 } + { \bf j } \alpha _ { \mathrm { { i } } }$ ,This is valid in so far as the complex form of the Love numbers is valid. The solution of these equations is, for $\pmb { \psi } = \pmb { 0 }$

$$
\mathbf { m } = \mathbf { m } _ { 0 } \mathbf { e } ^ { \mathbf { j } \pmb { \sigma } _ { 0 } t } = \mathbf { m } _ { 0 } \mathbf { e } ^ { - \alpha t } \mathbf { e } ^ { \mathbf { j } \pmb { \sigma } _ { 0 } t } ,
$$

and the amplitude of the free wobble is damped by the factor e-α. The relaxation time is

$$
{ \tau } = 1 / \alpha ,
$$

and the specific dissipation is (equation 2.2.6)

$$
1 / Q = 2 \alpha / \sigma _ { 0 } .
$$

The spectral density of the damped motion is proportional to

$$
\{ [ ( \sigma - \sigma _ { 0 } ) / \sigma _ { 0 } ] ^ { 2 } + ( 1 / 2 Q _ { 0 } ) ^ { 2 } \} ^ { - 1 } .
$$

![](images/e9b907df8fd242cad763ba70341b44ed555f9ce40bf075d695e998adfc106fd4.jpg)  
Figure 3.4. Spectral density of linearly damped oscillator with resonance frequency $\sigma _ { 0 } = 0 . 8 5$ cycles $\mathbf { y } \mathbf { r } ^ { - 1 }$ and two values of $Q _ { \mathbf { 0 } } ,$ ,10 and 30.

This is illustrated in figure 3.4 for different values of $\pmb { Q _ { 0 } }$ ; the lower $\pmb { Q _ { 0 } }$ the broader the spectral peak.

The linearly damped wobble also illustrates an interesting situation in which the wobble and l.o.d. equations (3.2.6) cannot be treated separately. Due to tidal friction (chapter 1O), the Earth undergoes a slow secular acceleration with consequence that $\pmb { \Omega }$ was greater in the past than it is now and that $\pmb { \sigma } _ { 0 }$ was also greater. This raises the possibility that at some time earlier, ${ \pmb { \sigma _ { 0 } } }$ equalled the frequency of the seasonal forcing function. At such a resonance, the spectral density of the damped motion is proportional to $( 2 Q _ { 0 } ) ^ { 2 }$ ， some 500 times larger than at present if $Q _ { 0 } \simeq 6 0$ . If the present rate of deceleration has remained constant, this resonance would have occurred some $2 \times 1 0 ^ { 8 }$ yr ago. Cannon (1974; but see Lambeck

$1 9 7 5 b )$ has speculated on possible thermal and geological consequences of such an event.

The solution (3.5.2） illustrates the three essential problems related to the interpretation of the Eulerian free precession (see chapter 8):

(i) The elongation of the period, although qualitatively explained through the use of the Love number $k _ { 2 }$ (equation 3.4.5), needs a more quantitative explanation in terms of the Earth's physical properties.   
(ii) The motion is damped and the mechanism,or mechanisms,of dissipation need investigation.   
(iii) Despite damping， the astronomical observations do not indicate a systematic decrease in amplitude of the free wobble. This is indicative of an excitation process that maintains the wobble against damping.

# FOUR

# EXCITATION FUNCTIONS

The geophysical discussion of the Earth's rotation centres around the evaluation of the excitation functions $\psi _ { i }$ defined by (3.2.7), while the astronomical discussion centres around the determination of the motion of the instantaneous rotation axis, $\omega _ { i }$ or $m _ { i }$ . A primary goal in studying these problems is to understand the geophysical processes that excite the irregular rotation and conversely, to invert the astronomical observations for geophysical parameters describing some global properties of the Earth. Two approaches are possible. One is to make a detailed evaluation of the geophysical mechanisms perturbing the rotation, and this is done in the follow-ing chapters. The other is to compare the properties of the observed time series and power spectra with those that would be expected if the excitation functions had some simple mathematical form. A number of such forms and related formulae are discussed in this chapter and from them considerable insight into the irregular rotation can already be gained.

# 4.1 Alternative formulations

The excitation functions (3.2.7) consist of contributions from (i) a redistribution of mass,(ii) relative motion of matter,and (iii) torques. Thus

$$
\psi _ { i } = \psi _ { i } ( \mathrm { m a t t e r } ) + \psi _ { i } ( \mathrm { m o t i o n } ) + \psi _ { \mathrm { i } } ( \mathrm { t o r q u e s } ) ,
$$

with

$$
\begin{array} { r l } & { \Psi ( \mathrm { m a t t e r } ) = [ 1 / ( C - A ) ] \Delta { \bf I } , } \\ & { \Psi ( \mathrm { m o t i o n } ) = ( 1 / \Omega ( C - A ) ) [ - \mathrm { j } \Delta \dot { \bf I } + { \bf h } - ( \mathrm { j } / \Omega ) \dot { \bf h } ] , } \\ & { \Psi ( \mathrm { t o r q u e } ) = \mathrm { j } { \bf L } / \Omega ^ { 2 } ( C - A ) , } \end{array}
$$

and

$$
\left. \begin{array} { c } { { \psi _ { 3 } ( \mathrm { m a t t e r } ) = - \Delta I _ { 3 3 } / C , } } \\ { { \psi _ { 3 } ( \mathrm { m o t i o n } ) = - h _ { 3 } / \Omega C , } } \\ { { \psi _ { 3 } ( \mathrm { t o r q u e } ) = \Omega \displaystyle \int _ { 0 } ^ { t } L _ { 3 } \mathrm { d } t . } } \end{array} \right\}
$$

Each of these terms is summarized in table 4.1 for both Cartesian and spherical coordinates. In these expressions $\pmb \rho ( \pmb x _ { i } , t )$ is the density of matter taking part in the motion and $\Delta \rho \left( x _ { i } , t \right)$ is the change in the density distribution. Velocities are denoted by $u _ { i }$ ，accelerations by $\dot { \pmb { u } _ { i } }$ 、In spherical coordinates, the velocities $u _ { r } , \ u _ { \phi } , \ u _ { \lambda }$ are positive radially outwards, polewards and eastwards. The torques may be of two types: torques due to a body force f, and the torque due to surface forces $p _ { n k }$ , in the direction $\mathbf { k }$ , on a unit surface whose normal is n. An example of the former is the lunar attraction on the Earth's bulge; an example of the latter is the action of surface winds. The volume integrals are over a volume $V$ enclosed by a surface S. The actual choice of this surface depends on the problem studied. $V$ could include the fluid parts of the Earth as well as the solid Earth. In this case effects of winds and ocean currents are evaluated in terms of relative motion or relative angular momenta. Alternatively, $V$ could include only the solid Earth and now wind and ocean effects are evaluated in terms of surface stresses integrated over the surface $\pmb { S }$ of the solid Earth. The choice of method is, in most cases,decided by the available observations, that is, whether it is simpler or more precise to measure relative motion or surface stresses.

The elements of the inertia tensor $\Delta I _ { i j }$ follow from (3.1.4),or they may be expressed in spherical coordinates as

$$
\Delta I _ { i j } = \int _ { V } \Delta \rho r ^ { 2 } \Pi _ { i j } \ \mathrm { d } V ,
$$

where

$$
\left. \begin{array} { l } { { \Pi _ { 1 1 } = 1 - \cos ^ { 2 } \phi \cos ^ { 2 } \lambda , } } \\ { { \Pi _ { 2 2 } = 1 - \cos ^ { 2 } \phi \sin ^ { 2 } \lambda , } } \\ { { \Pi _ { 3 3 } = \cos ^ { 2 } \phi , } } \\ { { \Pi _ { 1 2 } = - { \frac { 1 } { 2 } } \cos ^ { 2 } \phi \sin 2 \lambda = \Pi _ { 2 1 } , } } \\ { { \Pi _ { 1 3 } = - \sin \phi \cos \phi \cos \lambda = \Pi _ { 3 1 } , } } \\ { { \Pi _ { 2 3 } = - \sin \phi \cos \phi \sin \lambda = \Pi _ { 3 2 } . } } \end{array} \right\}
$$

Table 4.1. Excitation functions $\psi _ { i }$ due to a redistribution of matter, motion (velocity and acceleration),and torques in Cartesian and spherical coordinates   

<table><tr><td colspan="4"></td></tr><tr><td rowspan="2">Matter</td><td>1p x1xdV</td><td>-△p x2x3dV</td><td>（x²+x2）dv</td></tr><tr><td>C-A</td><td>C-A</td><td>C</td></tr><tr><td rowspan="2">Velocity</td><td>-2p xudV</td><td>2p x3udV</td><td>p (-xu+xu1)dV</td></tr><tr><td>(C-A)</td><td>(C-A)</td><td>nc</td></tr><tr><td rowspan="2">Acceleration</td><td>p (xu-xu）dV ²(C-A）</td><td>p (xu-xu）dV (C-A)</td><td>0</td></tr><tr><td>1 [p(x2f-x3f）dV</td><td>-1 p(xif-x2fi）dV</td><td>1 cp(x1f2-x2fi）dv</td></tr><tr><td rowspan="3">Torque</td><td>(C-A）</td><td>n²(C-A)</td><td></td></tr><tr><td>+(x2Pn3-x3Pn2)dS]</td><td>+(xiPn3-x3Pni) dS]</td><td>+(x1Pn2-x2Pn1)dS]</td></tr><tr><td colspan="2">Spherical coordinates (r,Φ,^)</td><td></td></tr><tr><td rowspan="2">Matter</td><td>-△pr² cos  sin  cos λ dV C-A</td><td>-△pr² C-A cos  sin sin λ dV</td><td>-△pr² cos²dv C</td></tr><tr><td>-2pr</td><td>+2pR sin</td><td>二</td></tr><tr><td rowspan="4">Velocity</td><td>sinΦ(u cos Ω(C-A)</td><td>-ux sin (C-A)</td><td>cos  ux dV nc</td></tr><tr><td>-uf sin  sin </td><td>-ud sin  cos 人</td><td></td></tr><tr><td>+u,cos  sin )dV</td><td>+u, cos Φ cos λ) dV</td><td></td></tr><tr><td>pr ²(C-A)(ux sin Φ sin^</td><td>pr ²(C-A)(u sin cos λ</td><td>0</td></tr><tr><td rowspan="2">Torques due to body force</td><td>-u cos 人)dV</td><td>-u sinλ)dV</td><td></td></tr><tr><td>pr</td><td>-pr</td><td>pr f cos  dv</td></tr><tr><td rowspan="2"></td><td>[fsin- ²(C-A)</td><td>-[f cos λ + ²(C-A)</td><td>n²c</td></tr><tr><td>f sin  cos ]dv</td><td>f sin sin λ]dv</td><td></td></tr></table>

# 4.2 Surface loading

In numerous instances, the excitation function is a consequence of a redistribution of mass over the Earth's surface: for example,an exchange of mass between the polar ice caps and the oceans, a redistribution of water between oceans, atmosphere and ground-water,or a redistribution of mass within the atmosphere.In all cases it is convenient to express the change in mass distribution as a surface load $q ( \phi , \lambda ; t )$ and to expand it into surface spherical harmonics. That is

$$
q ( \phi , \lambda : t ) = \sum _ { n = 0 } ^ { \infty } \sum _ { m = 0 } ^ { n } \ : ( q _ { n m } ^ { \prime } ( t ) \cos m \lambda + q _ { n m } ^ { \prime \prime } ( t ) \sin m \lambda ) P _ { n m } ( \sin \phi ) .
$$

The excitation functions are, with $\rho \mathrm { ~ d ~ } V = q$ dS (see table 4.1),

$$
\begin{array} { r l } & { \Psi ( \mathrm { m a t t e r } ) = - \cfrac { R ^ { 2 } } { C - A } \displaystyle \int _ { S } q \cos \phi \sin \phi \mathrm { e } ^ { \mathrm { i } \phi } \mathrm { d } S , } \\ & { \psi _ { 3 } ( \mathrm { m a t t e r } ) = - \cfrac { R ^ { 2 } } { C } \displaystyle \int _ { S } q \cos ^ { 2 } \phi \mathrm { d } S . } \end{array}
$$

With

$$
\begin{array} { r l } & { \cos { \phi } \sin { \phi } \mathrm { e } ^ { \mathrm { i } \lambda } = \frac { 1 } { 3 } P _ { 2 1 } ( \sin { \phi } ) \mathrm { e } ^ { \mathrm { i } \lambda } , } \\ & { \phantom { \cos { \phi } } \cos ^ { 2 } { \phi } = \frac { 2 } { 3 } ( P _ { 0 0 } - P _ { 2 0 } ) , } \end{array}
$$

and with the orthogonality properties of the surface harmonis, these excitation functions reduce to

$$
\begin{array} { r l } & { \Psi = - \frac { 4 } { 5 } \pi [ R ^ { 4 } / ( C - A ) ] ( q _ { 2 1 } ^ { \prime } + \mathrm { j } q _ { 2 1 } ^ { \prime \prime } ) , } \\ & { } \\ & { \psi _ { 3 } = - \frac { 8 } { 3 } \pi ( R ^ { 4 } / C ) ( q _ { 0 0 } ^ { \prime } - \frac { 1 } { 5 } q _ { 2 0 } ^ { \prime } ) . } \end{array}
$$

Only zeroth- and second-degree harmonics in the surface load enter into the excitations. If the mass of the load is conserved, ${ \pmb q _ { 0 0 } ^ { \prime } } = { \bf 0 }$ Under a surface load, the elastic Earth deforms and further modifies the excitation function by an amount $\psi _ { \mathrm { { L } } }$ . This is most readily accounted for with the aid of the load deformation coefficients $k _ { n } ^ { \prime } ,$ since only low-degree harmonics enter into the discussion. Then

$$
\begin{array} { r l } & { \Psi = \Psi _ { \mathrm { r } } + \Psi _ { \mathrm { L } } } \\ & { \quad = - \frac { 4 } { 5 } \pi [ R ^ { 4 } / ( C - A ) ] ( 1 + k _ { 2 } ^ { \prime } ) ( q _ { 2 1 } ^ { \prime } + \mathrm { j } q _ { 2 1 } ^ { \prime \prime } ) , } \\ & { \psi _ { 3 } = \psi _ { \mathrm { r } , 3 } - \psi _ { \mathrm { L } , 3 } } \\ & { \quad \quad = - \frac { 8 } { 3 } \pi ( R ^ { 4 } / C ) [ ( 1 + k _ { 0 } ^ { \prime } ) q _ { 0 0 } ^ { \prime } - \frac { 1 } { 5 } ( 1 + k _ { 2 } ^ { \prime } ) q _ { 2 0 } ^ { \prime } ] } \end{array}
$$

The rotational response of an excitation function $\psi _ { \tau }$ that loads the Earth therefore differs from the same function acting on a rigid Earth in that there is (i) an additional rotational deformation leading to $\psi _ { \mathrm { { D } } }$ and (ii) a load deformation leading to $\psi _ { \mathrm { { L } } }$ The effective excitation is, in consequence,

$$
\begin{array} { l } { \displaystyle \Psi = \Psi _ { \mathrm { r } } + \Psi _ { \mathrm { D } } + \Psi _ { \mathrm { L } } } \\ { \displaystyle = ( 1 + k _ { 2 } ^ { \prime } ) \Psi _ { \mathrm { r } } + ( k _ { 2 } / k _ { \mathrm { o } } ) \mathbf { m } . } \end{array}
$$

The wobble equations (3.2.6) now are

$$
\dot { \mathbf { m } } / \sigma _ { \mathrm { r } } + \mathbf { m } = \Psi
$$

or,with (4.2.3) and (3.4.5),

$$
\dot { \mathbf { m } } / \sigma _ { 0 } + \mathbf { m } = [ k _ { \mathrm { o } } / ( k _ { \mathrm { o } } - k _ { 2 } ) ] ( 1 + k _ { 2 } ^ { \prime } ) \boldsymbol { \Psi } _ { r } .
$$

Numerically $k _ { \mathrm { o } } = 0 . 9 4 2 , k _ { 2 } \simeq 0 . 3 0 , k _ { 2 } ^ { \prime } \simeq - 0 . 3 0$ and the right-hand side of (4.2.5) is approximately equal to $\psi _ { \tau }$ .To evaluate the effective wobble excitation function we first determine $\psi _ { \tau }$ as if the Earth were rigid and multiply it by

$$
X _ { \mathrm { w o b b l e } } = k _ { \mathrm { o } } / ( k _ { \mathrm { o } } - k _ { 2 } )
$$

if $\psi _ { \tau }$ does not load the Earth, or

$$
X _ { \mathrm { w o b b l e } } = [ k _ { \circ } / ( k _ { \circ } - k _ { 2 } ) ] ( 1 + k _ { 2 } ^ { \prime } )
$$

if $\psi _ { \tau }$ does load the Earth.

For $\psi _ { 3 }$ we apply the operation (4.2.2) if the excitation function loads the Earth's surface. In many problems mass will be conserved and

$$
\psi _ { 3 } = \big ( 1 + k _ { 2 } ^ { \prime } \big ) \psi _ { \mathrm { r } , 3 } \equiv X _ { \mathrm { l . o . d . } } \psi _ { \mathrm { r } , 3 } .
$$

If no loading occurs $X _ { \mathrm { l . o . d . } } = 1$ . Munk & MacDonald refer to $X _ { \mathrm { w o b b l e } }$ and $X _ { 1 . 0 . \mathbf { d } . }$ as the ‘transfer function'.

In other problems the load or stress is limited to either the oceans or the continents. Ocean tides constitute an example of the former. In situations of this type we introduce the ocean function $\mathcal { C } ( \phi , \lambda )$ ， defined such that

$$
\left. { \begin{array} { l l } { \displaystyle \mathcal { C } ( \phi , \lambda ) = 1 } & { { \mathrm { w h e r e ~ t h e r e ~ a r e ~ o c e a n s , } } } \\ { \displaystyle \mathcal { C } ( \phi , \lambda ) = 0 } & { { \mathrm { w h e r e ~ t h e r e ~ i s ~ l a n d . } } } \end{array} } \right\}
$$

Likewise a continent function $\mathcal { C } ^ { \prime } ( \phi , \lambda )$ can be introduced,such that

$$
\mathcal { C } ^ { \prime } ( \phi , \lambda ) = 1 - \mathcal { C } ( \phi , \lambda ) .
$$

In terms of spherical harmonics the ocean and continent functions are

$$
\mathcal { C } ( \phi , \lambda ) = \sum _ { n m } \big ( a _ { n m } \cos m \lambda + b _ { n m } \sin m \lambda \big ) P _ { n m } ( \sin \phi ) ,
$$

$$
\mathcal { C } ^ { \prime } ( \phi , \lambda ) = \sum _ { n m } \left( a _ { n m } ^ { \prime } \cos m \lambda + b _ { n m } ^ { \prime } \sin m \lambda \right) P _ { n m } ( \sin \phi ) ,
$$

with

$$
a _ { 0 0 } ^ { \prime } = 1 - a _ { 0 0 }
$$

and for all other $n , m$

$$
a _ { n m } ^ { \prime } = - a _ { n m } , \qquad b _ { n m } ^ { \prime } = - b _ { n m } .
$$

The ocean function coefficients $a _ { n m } , ~ b _ { n m }$ have been evaluated by Balmino,Lambeck & Kaula (1973) up to degree and order 36. Table 4.2 gives the normalized coefficients $\bar { a } _ { n m } , ~ \bar { b } _ { n m }$ for some low-degree coefcients of the spherical harmonic expansion of the topography and of the ocean function. The unnormalized coefficients are given by (equation 2.4.4)

$$
 \begin{array} { l } { { a _ { n m } } } \\ { { b _ { n m } } } \end{array} \} = N _ { n m } \{ \begin{array} { l l } { { \bar { a } _ { n m } } } \\ { { \bar { b } _ { n m } } } \end{array} .
$$

# 4.3 Schematic excitation functions

Many of the geophysical phenomena perturbing the Earth's rota-tion can be approximated by simple excitations such as step,delta, ramp or periodic functions. The general properties of the solutions for such excitations are discussed in this section, while the discussion of specific geophysical excitations is deferred to later chapters. Consider first a step function in ψ:

$$
\boldsymbol { \Psi } ( t ) = \Delta \boldsymbol { \Psi } H ( t ) ,
$$

where

$$
\begin{array} { r l } { H ( t ) = 0 } & { { } \mathrm { f o r } \ t < 0 } \\ { = 1 } & { { } \mathrm { f o r } \ t \geq 0 . } \end{array}
$$

This represents an instantaneous shift in the position of the excita-tion pole at time $\pmb { t = 0 }$ . If,at ${ \pmb t } < { \bf 0 }$ ， $m = 0$ ,the solution (3.2.12) of the

Table 4.2. Coefficients $\bar { a } _ { n m } , \ \bar { b } _ { n m }$ (normalized) for the spherical harmonic expansion of the Earth $, _ { s }$ topography and of the ocean function. (From Balmino,Lambeck & Kaula, 1973.)   

<table><tr><td colspan="6"></td></tr><tr><td>Degree</td><td>Order</td><td>anm (m)</td><td>bmm (m)</td><td>anm</td><td>bnm</td></tr><tr><td>0</td><td>0</td><td>-2300</td><td></td><td>0.697</td><td></td></tr><tr><td>1</td><td>0</td><td>639</td><td></td><td>-0.126</td><td></td></tr><tr><td>1</td><td>1</td><td>591</td><td>409</td><td>-0.108</td><td>-0.056</td></tr><tr><td>2</td><td>0</td><td>515</td><td></td><td>-0.060</td><td></td></tr><tr><td>2</td><td>1</td><td>336</td><td>306</td><td>-0.040</td><td>-0.051</td></tr><tr><td>2</td><td>2</td><td>-415</td><td>-80</td><td>0.040</td><td>0.002</td></tr><tr><td>3</td><td>0</td><td>-174</td><td></td><td>0.045</td><td></td></tr><tr><td>3</td><td>1</td><td>-135</td><td>115</td><td>0.044</td><td>-0.032</td></tr><tr><td>3</td><td>2</td><td>-446</td><td>458</td><td>0.070</td><td>-0.089</td></tr><tr><td>3</td><td>3</td><td>116</td><td>545</td><td>-0.016</td><td>-0.089</td></tr><tr><td>4</td><td>0</td><td>373</td><td>-249</td><td>-0.024</td><td></td></tr><tr><td>4</td><td>1</td><td>-222</td><td>56</td><td>0.036</td><td>0.030</td></tr><tr><td>4</td><td>2 3</td><td>-382</td><td>-118</td><td>0.090 -0.053</td><td>-0.021</td></tr><tr><td>4</td><td>4</td><td>360 -57</td><td>449</td><td>0.014</td><td>0.005 -0.101</td></tr><tr><td>4</td><td></td><td></td><td></td><td></td><td></td></tr></table>

# equations of motion becomes

$$
\begin{array} { c } { { m \left( t \right) = - { \bf j } \sigma _ { 0 } \mathrm { e } ^ { \mathrm { i } \sigma _ { 0 } t } \displaystyle \int _ { 0 } ^ { t } { \bf A } \Psi \mathrm { e } ^ { - \mathrm { j } \sigma _ { 0 } \tau } \mathrm { d } \tau } } \\ { { = \Delta \Psi ( 1 - \mathrm { e } ^ { \mathrm { j } \sigma _ { 0 } \tau } ) . } } \end{array}
$$

At time $\pmb { t = 0 }$ ,the excitation pole has jumped from $\pmb { \psi } = \mathbf { 0 }$ to a new position, $\psi = \Delta \psi$ ,about which the rotation axis now turns. If, at a later instant, the excitation pole jumps from $\Delta \psi$ to $\Delta \psi + \Delta \psi ^ { \prime }$ ，the rotation pole moves about this new position without there being a break in the pole path (figure 4.1). An excitation function that consists of a sequence of step functions can be represented as the sum of a number of rectangular functions of variable length $\pmb { a } ^ { - 1 }$

![](images/8ec1d46cc6f1c315d2f1ccd3d0aa8b43f11f6280c86d7b1041adfb27a025fd5a.jpg)  
Figure 4.1. Motion of rotation axis ω due to step function changes in $\pmb { \psi }$ At time $\pmb { T } _ { 1 }$ ,when $\pmb { \omega }$ is at $P _ { 1 }$ ,the excitation pole is shifted from $\pmb { A }$ to $\pmb { B } ; \pmb { \omega }$ now turns about $\pmb { B }$ with radius $B P _ { 1 }$ until time $\pmb { T } _ { 2 }$ ,when $\pmb { \ 6 0 }$ is at $P _ { 2 }$ ,and a second shift in the excitation pole occurs from $\pmb { B }$ to $C .$

The amplitude spectrum of one such rectangular function is

$$
\mathcal { S } _ { \psi } ( f ) = \left[ \frac { \sin \pi f / a } { \pi f / a } \right] ^ { 2 }
$$

and falls off rapidly as the frequency increases, until it becomes zero at $\pmb { f } = \pmb { a } ,$ . Beyond this point the spectrum consists of small-amplitude ripples. The longer the time constant $a ^ { - 1 }$ , the more pronounced will be the spectrum at low frequencies. If $\boldsymbol { \Psi }$ consists of a series of rectangular pulses, with variable time constants, the spectrum will be smoothed and the ripples vanish. The characteristic spectrum will be one of decreasing power with increasing frequency. This is in agreement with the result (4.3.1) that the mean excitation function shifts with each jump and the total motion after a sequence of jumps is a two-dimensional random walk.

The step function change in $\psi _ { 3 }$ likewise leads to a spectrum of $\pmb { m _ { 3 } }$ in which the signal decreases with increasing frequency. The spectrum in $\dot { m } _ { 3 }$ varies with frequency according to

$$
\mathcal { S } _ { \dot { m } _ { 3 } } ( f ) = ( 2 \pi f ) ^ { 2 } \mathcal { S } _ { \psi } ( f ) = ( 2 \pi f ) ^ { 2 } \bigg [ \frac { \sin \pi f / a } { \pi f / a } \bigg ] ^ { 2 }
$$

and vanishes at zero frequency. Astronomers do not observe $m _ { 3 }$ directly but measure the integrated amount by which the Earth is slow after an interval of afew days (chapter 5). That is, they measure

$$
{ \mathcal { I } } = - \int _ { t } m _ { 3 } \mathrm { d } t .
$$

A step function change in $\psi _ { 3 }$ therefore causes a change in slope of $\boldsymbol { \mathcal { I } }$ (figure 4.2), and the resulting spectrum of $\mathcal { I }$ is

$$
\mathcal { S } _ { \pi } ( f ) = [ 1 / ( 2 \pi f ) ^ { 2 } ] \mathcal { S } _ { \psi } ( f ) .
$$

A sudden impulse in the excitation $\pmb { \psi }$ is described by the delta function

$$
\begin{array} { c } { \displaystyle \delta \left( t \right) = 0 , \qquad t \gtrless 0 } \\ { \displaystyle \int _ { - \infty } ^ { \infty } \delta \left( t \right) \mathrm { d } t = 1 , } \end{array}
$$

as

$$
\Psi ( t ) = \Delta \Psi \delta ( t ) .
$$

In this case the partial solution of the wobble equations follows from (3.2.12) as

$$
\begin{array} { r l } & { \mathbf { m } ( t ) = - \mathbf { j } \sigma _ { 0 } \operatorname { e } ^ { \mathbf { j } \sigma _ { 0 } t } \Delta \Psi \left. \int _ { - \infty } ^ { \infty } \delta ( t ) \operatorname { e } ^ { - \mathbf { j } \sigma _ { 0 } \tau } \mathrm { d } \tau \right. } \\ & { \quad \quad = - \sigma _ { 0 } \Delta \Psi \mathrm { e } ^ { \mathbf { j } ( \sigma _ { 0 } t + \pi / 2 ) } . } \end{array}
$$

Now the instantaneous rotation pole undergoes a jump of magnitude $\pmb { \sigma } _ { 0 } \Delta \pmb { \psi }$ , while the excitation pole remains at its original position. The jump of m is shifted $\scriptstyle { \frac { 1 } { 2 } } \pi$ in phase from the direction of the impulse (figure 4.3). The power spectrum of a delta function is independent of frequency and a sequence of irregularly spaced delta functions also produces a white noise spectrum. The delta functions do not cause a shift in the position of the mean excitation pole. The corresponding spectrum of $\dot { m } _ { 3 }$ is proportional to $( 2 \pi f ) ^ { 2 }$ and vanishes at very low frequencies. For delta function impulses in $\psi _ { 3 }$ ,the changes in the observed $\mathcal { I }$ are represented by step functions, and the spectrum of $\mathcal { I }$ is enhanced at low frequencies according to $\left( 2 \pi f \right) ^ { - 2 }$ . Figure 4.4 illustrates the case when $\mathcal { I } ( t )$ is a rectangular function.

![](images/7e7220712c758b2459e699cbf1bdc1ab83a09bc783b8ca16bbeccc6f50e07b3b.jpg)  
Figure 4.2. Rectangular function change in $m _ { 3 }$ ,corresponding changes in $\pmb { \mathcal { I } }$ and $\dot { m } _ { 3 }$ ,and their power spectra.

Geophysical problems that involve step function type changes in the inertia tensor have wobble excitation functions that consist of both a step and a delta function. That is,

$$
\begin{array} { r l } & { \Delta \mathbf { I } = \Delta \mathbf { I } H ( t ) , } \\ & { \Delta \mathbf { \dot { I } } = \Delta \mathbf { I } \boldsymbol { \delta } ( t ) , } \\ & { \boldsymbol { \Psi } = \cfrac { 1 } { C - A } \bigg ( \Delta \mathbf { I } - \frac { \mathrm { \dot { J } } } { \Omega } \Delta \mathbf { \dot { I } } \bigg ) = \cfrac { \Delta \mathbf { I } } { C - A } \bigg [ H ( t ) - \frac { \mathrm { \dot { J } } } { \Omega } \boldsymbol { \delta } ( t ) \bigg ] . } \end{array}
$$

![](images/6cbc34253af0854492967e5e0fd7b8e41ccb9b24c801bbda910db2ad5c52268f.jpg)  
Figure 4.3.Motion of the rotation axis ω due to delta function changes in $\pmb { \psi }$ Initially $\mathbf { \delta \omega } _ { \mathbf { \omega } \mathbf { \omega } } \mathbf { \omega } _ { \mathbf { \omega } \mathbf { \omega } }$ ， $\pmb { \psi } = \pmb { 0 }$ . At time $T _ { 1 }$ a delta function excitation occurs and momentarily displaces $\pmb { \psi }$ from $^ o$ to A. $\pmb { \omega }$ jumps to $\pmb { B }$ ， $\scriptstyle { \frac { 1 } { 2 } } \pi$ behind $\pmb { A }$ in phase, and now rotates about $^ o$ At time $T _ { 2 }$ ， $\pmb { \omega }$ is at $C$ and a second impulse occurs in the direction $o D$ ； $\pmb { \omega }$ now moves to $\pmb { { \cal E } }$ and continues to rotate about $o$ but with a modified radius.

With (4.3.1) and (4.3.6)

$$
\mathbf { m } = \frac { \Delta \mathbf { I } } { C - A } \bigg [ \left( 1 - \mathrm { e } ^ { \mathrm { j } \sigma _ { 0 } t } \right) + \mathrm { j } \frac { \sigma _ { 0 } } { \Omega } \mathrm { e } ^ { \mathrm { j } \left( \sigma _ { 0 } t + \pi / 2 \right) } \bigg ] .
$$

But $\sigma _ { 0 } / \Omega \simeq 1 / 4 3 0$ , the last term is negligible compared with the first term,and it is the step function change that dominates Φ. An example of an excitation of this type is the mass redistribution associated with earthquakes (chapter 8).

A secular change in the excitation function can be represented by a ramp function

$$
R ( t ) = t H ( t ) ,
$$

$$
\Psi ( t ) = \Delta \Psi t H ( t ) .
$$

The solution of the equations of motion now is

$$
\begin{array} { r } { \mathbf { m } ( t ) = \left[ t - ( \mathbf { j } / \sigma _ { 0 } ) \right] \Delta \psi + ( \mathbf { j } / \sigma _ { 0 } ) \Delta \psi \mathrm { e } ^ { \mathrm { i } \sigma _ { 0 } t } . } \end{array}
$$

![](images/0f719092977f0db6ade43cc6c0eba1194e50cc1c2f6ba3f067bbf2fb107fd253.jpg)  
Fibure 4.4. Delta function changes in $m _ { 3 }$ , associated changes in $\pmb { \mathcal { I } }$ and $\dot { m } _ { 3 }$ ， and their power spectra.

This type of excitation occurs if there is a secular exchange of mass between the polar ice caps and the oceans. The observed drift of the mean pole is slow, of the order $\mathbf { 0 { : } 0 0 3 \ y r ^ { - 1 } }$ or less (chapter 5) and any excitation of the wobble, the second term in (4.3.8), is small indeed. The ramp function gives a spectrum whose power at low frequencies is much enhanced compared with the previous spectra: for a step function the power spectrum is proportional to $( { \frac { 1 } { 2 } } \pi f ) ^ { 2 }$ and the ramp function, being the integral of the former, has a spectrum that is proportional to $\left( { \scriptstyle { \frac { 1 } { 2 } } } \pi f \right) ^ { 4 }$ . A ramp function change in $\dot { m } _ { 3 }$ implies a step function change in $\dot { m } _ { 3 }$ or a quadratic variation in $\mathcal { I }$ (figure 4.5).

![](images/bbb4868656d283e936dfc406b19fbd5616e112edd50d5d65ee425c49c6038720.jpg)  
Figure 4.5. Ramp function changes in $m _ { 3 } .$ ,associated changes in $\pmb { \mathcal { I } }$ and $\dot { m } _ { 3 }$ ， and their power spectra.

Another useful model relates to the electromagnetic core-mantle coupling mechanism discussed in chapter 9. Consider an accelerat-ing torque acting on the mantle that brings into action a second torque, opposite to the first, and growing in magnitude with time until a new equilibrium state is reached. That is,

$$
\Psi = \Delta \Psi \ H ( t ) \ e ^ { - a t }
$$

and

$$
{ \bf { m } } ( t ) = \left[ { \bf { j } } { \sigma _ { 0 } } / { ( a + \bf { j } } { \sigma _ { 0 } } ) \right] \Delta \psi ( \mathrm { e } ^ { - a t } - \mathrm { e } ^ { { \mathrm { j } } { \sigma _ { 0 } } t } ) .
$$

At time $t ,$ the excitation pole jumps from $\pmb { \psi } = \pmb { 0 }$ to a new position $\mathrm { j } \sigma _ { 0 } \Delta \Psi / ( a + \mathrm { j } \sigma _ { 0 } )$ ,then it drifts back to the original position with a time constant $\pmb { a } ^ { - 1 }$ . The amplitude spectrum of $\boldsymbol { \Psi }$ is proportional to

$$
1 / [ a ^ { 2 } + ( 2 \pi f ) ^ { 2 } ] ,
$$

and approaches $1 / a ^ { 2 }$ at low frequencies. For $m _ { 3 }$ ,a torque of this

kind results in

$$
\dot { m } _ { 3 } = \Delta \psi _ { 3 } H ( t ) \mathrm { e } ^ { - a t } ,
$$

and its power spectrum lies between the cases illustrated in fgures 4.2 and 4.5.

A frequently encountered excitation function is

$$
\Psi = \Psi ^ { \mathrm { { c } } } \cos \sigma t + \Psi ^ { \mathrm { { s } } } \sin \sigma t ,
$$

which represents two simple harmonic oscillators at right angles to each other. This elliptical path can be considered as the resultant of two circular motions of opposite frequency or

$$
\Psi = \Psi ^ { + } \mathrm { e } ^ { \mathrm { i } \sigma t } + \Psi ^ { - } \mathrm { e } ^ { - \mathrm { j } \sigma t } ,
$$

where

$$
\begin{array} { r } { \| \pmb { \psi } ^ { \pm } = \frac { 1 } { 2 } ( \pmb { \psi } ^ { \mathrm { c } } \mp \mathbf { j } \pmb { \psi } ^ { \mathrm { s } } ) . } \end{array}
$$

The solution of the equations of motion consists of a free oscillation of frequency $\pmb { \sigma _ { 0 } }$ ，

$$
\mathbf { m } = \mathbf { m _ { 0 } } \thinspace \mathbf { e } ^ { \mathrm { i } \sigma _ { 0 } t } ,
$$

and a forced oscillation of frequency ${ \pmb \sigma } .$

$$
\mathbf { m } = [ \pmb { \sigma } _ { 0 } / ( \pmb { \sigma } - \pmb { \sigma } _ { 0 } ) ] \pmb { \psi } ^ { + } \mathrm { e } ^ { \mathrm { i } \sigma t } + [ \pmb { \sigma } _ { 0 } / ( \sigma _ { 0 } - \pmb { \sigma } ) ] \pmb { \psi } ^ { - } \mathrm { e } ^ { - \mathrm { j } \sigma t } .
$$

To compare the above theoretical excitations and their spectra with the astronomical results, one can either proceed as above and compute a theoretical ${ \bf m } ( t )$ for a given $\psi ( t )$ , or estimate $\psi ( t )$ from ${ \bf m } ( t )$ and compare an observed $\psi ( t )$ with the models. The solution $\mathbf { m } ( t )$ (equation 3.2.12) can be written as

$$
\begin{array} { r } { \mathbf { m } ( t ) = \displaystyle \int _ { - \infty } ^ { t } \mathrm { e } ^ { \mathrm { i } \sigma _ { 0 } ( t - \tau ) } \boldsymbol { \Psi } ( \tau ) \mathrm { d } \tau } \\ { = \displaystyle \int _ { 0 } ^ { \infty } \mathrm { e } ^ { \mathrm { i } \sigma _ { 0 } \tau } \boldsymbol { \Psi } ( t - \tau ) \mathrm { d } \tau , } \end{array}
$$

or

$$
\mathbf { m } ( t ) = \int _ { - \infty } ^ { \infty } \mathbf { g } ( \tau ) \mathbf { \dot { \psi } } ( t - \tau ) \mathbf { d } \tau ,
$$

where

$$
\mathbf { g } ( \tau ) = { \left\{ \begin{array} { l l } { 0 } & { t < 0 } \\ { \mathbf { e } ^ { \mathbf { j } \sigma _ { 0 } t } } & { t > 0 } \end{array} \right. }
$$

is the wobble impulse response function. Thus $\mathbf { m } ( t )$ is the result of a convolution of the excitation $\psi ( t )$ with this response function; the problem of deducing the excitation from the astronomically observed $\mathbf { m } ( t )$ is one of deconvolution. The essential aspects of this deconvolution process are illustrated in figure 4.6. The excitation function acts on the Earth,whose wobble response is given by ${ \pmb g } ( t )$ . The resulting wobble is ${ \bf m } ( t )$ but, in the measuring process, noise ${ \bf n } ( t )$ is added. One now seeks a deconvolution filter whose response ${ \bf h } ( t )$ is such that its output $\boldsymbol { \Psi } ^ { 0 } ( t )$ , caused by the input $\mathbf { m } ( t ) + \mathbf { n } ( t )$ ， provides a good estimate of the true excitation function. The quality of the filter approximation is given by the quantity

![](images/d3871fc72047244345ac9f97a4de35d6486240254709d630ffef270fbd37bbc9.jpg)  
Figure 4.6. Schematic representation of the deconvolution of polar motion ${ \bf m } ( t )$ for estimating the excitation function $\psi ( t )$ ：

$$
\begin{array} { r } { \mathbf { \varepsilon } ( t ) = \Psi ( t ) - \Psi ^ { 0 } ( t ) . } \end{array}
$$

Smylie, Clarke & Mansinha (197O) use the optimum Wiener flter which minimizes the mean square of ${ \pmb \varepsilon } ( t )$ ， and they discuss it in relation to the problem where the excitation function can be characterized by a two-dimensional random walk. A simpler deconvolution process that does not attempt to separate noise from signal in ${ \bf m } ( t )$ is to write, for a discrete observation series,

$$
{ \bf m } ( t ) = { \mathrm { e } } ^ { \mathrm { j } { \sigma _ { 0 } } t } \Big [ { \bf m } _ { 0 } - \mathrm { j } { \sigma _ { 0 } } \sum _ { 0 } ^ { t } \Psi ( \tau ) \mathrm { e } ^ { - \mathrm { j } { \sigma _ { 0 } } \tau } \Delta t \Big ]
$$

and for the instant $t - \Delta t$

$$
\mathbf { m } ( t - \Delta t ) = \mathrm { e } ^ { \mathrm { j } \sigma _ { 0 } ( t - \Delta t ) } \bigg [ \mathbf { m } _ { 0 } - \mathrm { j } \sigma _ { 0 } \sum _ { 0 } ^ { t - \Delta t } \Psi ( \tau ) \mathrm { e } ^ { - \mathrm { j } \sigma _ { 0 } \tau } \Delta t \bigg ] .
$$

Thus

$$
\mathbf { m } ( t ) = \mathbf { m } ( t - \Delta t ) \mathrm { e } ^ { \mathrm { j } \sigma _ { 0 } \Delta t } - \mathrm { j } \sigma _ { 0 } \boldsymbol { \Psi } ( t ) \Delta t
$$

and

$$
\Psi ( t ) = - ( 1 / \mathsf { j } \sigma _ { 0 } \Delta t ) [ \mathsf { m } ( t ) - \mathsf { e } ^ { \mathsf { j } \sigma _ { 0 } \Delta t } \mathsf { m } ( t - 1 ) ] .
$$

# FIVE

# THE ASTRONOMICAL EVIDENCE

# 5.1 Observations of the Earth's rotation

# 5.1.1 The astronomical observations

Precise measurements of the time elapsed between two consecutive transits of a star across a meridian determine the l.o.d. with respect to some uniform time scale. Measurement of l.o.d. therefore involves two processes: the astronomical observation of the star transits, and the establishment of a reference time. Changes in the l.o.d. are small, of the order of ${ 1 0 } ^ {  { - } 8 }$ ,and observations of numerous stars from a number of observatories,over several nights,are required in order that the signal rises above the noise of the measuring process. Thus,what is observed by astronomers is the integrated amount by which the Earth is in advance or behind after a number of days, compared with the uniform time scale. Time kept by the Earth is referred to as universal time (UT)). Strictly speaking, the time interval between successive star transits defines sidereal time,whereas UT is a mean solar time. The relation between these two systems is quite complex and is discussed in detail in most textbooks on spherical astronomy (see, for example, Smart 1962; Woolard & Clemence 1966). For geophysical purposes, the obser-ved quantity can be considered to be the universal time. Star transits are observed with respect to an Earth-fixed meridian,defined by the station coordinates and the body-fixed x-axes. But the rotation axis moves with respect to this system, the polar motion,and small corrections to the transit times are required in order to determine the rotation about the instantaneous axis. UT corrected for this effect is denoted by UT1. The uniform reference time $H$ can be defined and measured in several ways, but for the moment it is useful to consider it as the time that would be kept if the Earth rotated uniformly with angular velocity $\pmb { \Omega }$ equal to its mean velocity.

The observed quantity then is

$$
{ \mathcal { I } } _ { \Delta T } = - ( \mathbf { U T 1 } - H ) ,
$$

the amount by which the Earth is slow after an interval △T. Conventional usage is that $\boldsymbol { \mathcal { I } }$ is positive if the Earth is slow relative to $H .$ The change in the l.o.d., △(l.o.d.)， and the instantaneous rotational velocity $\omega _ { 3 }$ ,or the perturbation in velocity $\pmb { m _ { 3 } }$ , are related by

$$
\begin{array} { r } { m _ { 3 } = ( \omega _ { 3 } - \Omega ) / \Omega = - \Delta ( 1 . 0 . \mathrm { d } . ) / 1 . 0 . \mathrm { d } . = - \mathrm { d } \mathcal { I } / \mathrm { d } t = ( \mathrm { d } / \mathrm { d } t ) ( \mathrm { U } \mathrm { T } 1 - \boldsymbol { H } ) . } \end{array}
$$

Astronomers observe the station latitudes by measuring the zenith distances of stars crossing the meridian.For a star of declination $\delta _ { \mathfrak { p } } ,$ ,transiting at zenith distance $z _ { p }$ to the poleward side of the vertical, the astronomical latitude of the station is (figure 5.1)

$$
\phi ^ { \mathsf { a } } = \delta _ { \mathsf { p } } - z _ { \mathsf { p } } ,
$$

while for a star crossing to the equatorward side of the vertical

$$
{ \phi } ^ { \mathrm { a } } = { \delta } _ { \mathrm { e } } - z _ { \mathrm { e } } ,
$$

and

$$
\begin{array} { r } { \phi ^ { \mathsf { a } } = \frac { 1 } { 2 } ( \delta _ { \mathsf { p } } + \delta _ { \mathsf { e } } ) + \frac { 1 } { 2 } ( z _ { \mathsf { e } } - z _ { \mathsf { p } } ) . } \end{array}
$$

Thus, for two stars of known declination, the observed difference in zenith distance at meridian transit provides an estimate of the astronomical latitude. This is the basis of the Horrebow-Talcott method of positional astronomy. If, with time, the rotation axis changes its position relative to the Earth's surface, $\phi ^ { \mathbf { a } }$ also varies. Polar motion, the motion of the rotation axis with respect to the solid Earth，is therefore also referred to as the variation of (astronomical) latitude. In terms of In, the change in astronomical latitude of a station ${ \pmb P } _ { \pmb n }$ at longitude $\lambda _ { n }$ is

$$
\Delta \phi _ { n } ^ { \mathrm { { \scriptsize ~ a } } } ( t ) = m _ { 1 } ( t ) \cos \lambda _ { n } + m _ { 2 } ( t ) \sin \lambda _ { n } .
$$

Observations from two or more stations, well separated in longitude, determine the complete motion of the Earth's pole of rotation.

Latitude observations consist of measuring the positions of stars; l.o.d. measurements consist of recording the times at which stars occupy certain positions. Observations of both position and time provide all three components $m _ { 1 } , m _ { 2 }$ and $m _ { 3 }$ of the instantaneous rotation axis. Measuring these quantities is a delicate operation beset with numerous problems: instrumental limitations,atmos-pheric refraction, the definition of the meridian or vertical, and the non-uniformity and imprecision of the reference time scale all contaminate the results.

![](images/b8ca008515186446f70b1a6e57b1af7399e59707a79ec355edbef4e63953f9ac.jpg)  
Figure 5.1. Geometry of latitude observations. The observer at $o$ observes $( a )$ the zenith angle $z _ { \tt p }$ of a star transiting to the poleward side of the vertical $o v$ and $( b )$ the zenith angle $z _ { e }$ of a second star to the equatorward side of $o V .$ .These two observations determine the astronomical latitude $\phi ^ { \circ }$ of $o$ if the declinations $\delta _ { \mathfrak { p } }$ and $\delta _ { e }$ of the two stars are known.

The early astronomical observations useful for studying the Earth's rotation consisted of occultations and transits of the Moon, Sun and planets,and were carried out with telescopes not specifically designed for measuring time and latitude. Only with the discovery of polar motion, at the close of the nineteenth century, were special instruments designed for these purposes. The principal instruments are (i) zenith telescopes,with which near-vertical transits of stars are observed, and which include visual telescopes and photo-zenith tubes, and (ii) prismatic astrolabes. The visual zenith telescopes, introduced in 1899 for latitude observations,use the Horrebow-Talcott method (equation 5.1.2). Two known stars are selected which cross the meridian within a few minutes of each other on opposite sides of, and close to, the vertical. The small difference in their zenith distances is measured with the aid of a micrometer, rather than by vertical circle readings. Precise levels are mounted on the instrument to relate the telescope axis to the vertical. The precision of the latitude measurement depends on instrumental and environmental factors, on the precision and calibration of the micrometer, on the precision with which the local vertical can be defined, and on the accuracy with which the star positions are known. Most of these error sources also perturb the other observation techniques discussed below. Perhaps the most important source of error is associated with the micrometer calibration. This is not known a priori with sufficient accuracy and has to be determined from the observations themselves. Any uncertainty in its value has immediate consequences on the pole path and, in particular, may introduce large errors in the annual component of the pole path: G. Cecchini (Melchior 1957) found that the introduction of improved values for the micrometer calibration modified the annual term in the pole path by as much as O'O5,which is comparable with the amplitude of the annual term itself! Melchior (1972) dwells further on this matter. Yumi (1970) estimates that the precision of a single night's latitude observation is of the order O"2-0"3.

Photo-zenith tubes (PZT), developed in 1911,represent some important improvements over the visual telescopes. The horizontal levels of the latter have been replaced by a mercury pool from which the star images are reflected on to a photographic plate in the telescope's focal plane. The image of a star in the zenith coincides with the lens's inner nodal point and neither a tilt nor a translation of the lens will alter the position of the zenith on the plate. Neither will images near the zenith be sensibly displaced by such motions. The photographic plate can be rotated about a vertical axis, and multiple exposures are made, before and after rotating the plate through $1 8 0 ^ { \circ }$ . The relative positions of the images determine the zenith distance of the star at the moment it transits the meridian (Markowitz 1960). If the instants of exposure are recorded with precision, the times of meridian transit and UT- H are also determined. Tests from 1911 to 1914 indicated that these instruments, originally developed by the US Coast and Geodetic Survey for latitude observations, were superior to the visual telescopes already employed. In 1923 the PZT was used for time observations as well, and by 1934 the instrument was routinely used at the US Naval Observatory (USNO). At present some 10 PZT's contribute to the latitude and time determination by the Bureau International de l'Heure. Markowitz (1960) concludes that the standard deviation for one night's observations is O:0o6 in time and $\mathbf { 0 . 0 7 }$ in latitude.

An instrument widely used for latitude and time determination since its introduction in 1958 is the impersonal prismatic astrolabe of Danjon,developed at the Paris Observatory (Danjon 1958, $1 9 6 0 a )$ . The time is recorded at which a star reaches a fixed altitude, $6 0 ^ { \circ }$ in the case of Danjon's instrument. To minimize personal errors in timing this instant, an impersonal micrometer is placed in front of the focal plane. By observing transits across the $6 0 ^ { \circ }$ -altitude circle, many more stars can be observed, particularly brighter stars,which are generally known with higher accuracy than the faint stars observed in the restricted field of the zenith telescopes. Débarbat & Guinot (1970) discuss the method of observing stars at fixed altitudes. Guinot (1958) discusses in detail the observation process, reductions and early results obtained with the astrolabe at the Paris Observatory,and concludes that, from one night's observations, the standard deviation of time determination is O:0o45 and of latitude is $\mathbf { 0 . 0 5 }$ ：

# 5.1.2 Time

Until about 40 yr ago, the Earth's rotation had been assumed to be constant, apart from possible secular or very long-period accelerations， and clocks served to subdivide the Earth's time into convenient units. Pendulum clocks have been the principal time-keeping device at observatories for several centuries. Joost Bürgi,an assistant of Tycho Brahe,was apparently the first to design a pendulum clock although the invention was virtually lost and rediscovered a century later by Christiaan Huygens in 1656. Jean Ricard soon introduced regular time observations at the Paris Observatory. Pendulum clocks were brought to a high state of precision by Rieffer in about 1890 and by Shortt in 1921,and by the mid-193Os these clocks were sufficiently precise to detect seasonal changes in the l.o.d. No longer could UT be considered a uniform time.Quartz crystal clocks,with greater stability， superseded pendulum clocks by about 1940. These clocks are essentially frequency standards in which an alternating electric current is applied across a crystal and the frequency of this current is adjusted until it resonates with the crystal's natural frequency. The frequency at which this resonance occurs depends upon the ambient pressure and temperature,and upon the elastic properties and the shape and size of the crystal. Stringent environmental control of the clock is essential to maintain high stability. Ageing of the crystals results in a drift of the resonance frequency that, in the past, could be determined only by comparing it with the Earth's rotation. Thus only changes in rotation with time scales comparable with the interval over which the crystals behave normally’ can be observed with these clocks. Typically this is not much beyond a year. The dependence of the frequency and the drift rate on the crystal properties implies that no two clocks have identical natural frequencies, and no one clock can be exactly reproduced. These characteristics make the crystal clocks of only limited value in establishing a uniform time Scale over periods longer than a few years. By 195O the crystal clocks confirmed that the l.o.d. varied annually and led to the detection of a semi-annual oscillation and to suggestions of monthly and fortnightly variations in the l.o.d.

Crystal clocks do have very high stabilities over short time intervals,and they are now used in combination with stabler atomic frequency standards to provide a measure of uniform time. Atomic frequency standards use the natural vibrations of atoms or molecules: atoms in an initially excited state drop to a lower-energy state and radiate energy at a frequency that is characteristic of the atom and that defines a spectral line in the spectrum of the radiated energy. Caesium atoms provide the principal standard in defining atomic frequencies. The atoms are excited by electromagnetic energy, but only at resonance, when the frequency of the applied energy equals the frequency of the emitted energy,will the tran-sition in energy state and the emission of the characteristic spectral line occur. A quartz crystal oscillator controls the applied elec-tromagnetic field, and by regulating its frequency until emission occurs, the oscillator frequency is calibrated with respect to the standard atomic frequency. It is this combination of atomic frequency standard and quartz crystal oscillator that forms the atomic clock and defines the atomic time scale introduced in 1955. The importance of these clocks is that they are extremely stable and quite insensitive to temperature and other environmental effects. Frequency stability of caesium standards is of the order of 2 parts in $1 0 ^ { 1 3 } \mathrm { \mathbf { y r } } ^ { - 1 }$ ,and the uncertainty of the frequency is afew parts in $1 0 ^ { 1 2 }$ (Terrien 1976). These stabilities far exceed the stability of the Earth as a time keeper, and the irregularities in rotation,both at high and low frequencies, can now be observed with accuracy and reliability.

The uncertainty in the l.o.d. determination is now entirely dominated by the astronomical part of the observation.

The atomic time scale. Since 1955,a number of atomic time scales have been used, the principal ones being A1, A3 and AT. The last (or TAI, Temps Atomique International) is a scale established by the Bureau International de 'Heure (BIH) in 1969,and represents an average of standards kept at several laboratories in Western Europe and North America. Each of these stations maintains two or more caesium standards - 16 standards are kept at the US Naval Observatory in Washington alone. They are related and compared by means of the Loran C navigation system and by transporting portable standards between observatories. Guinot， Feissel & Granveaud (1971) discuss the formation of AT in detail. From 1958 to 1969 the time scale kept by the BIH was A3, of which AT is a prolongation without discontinuity. The definition of A3 is given by Guinot & Feissel (1969). A1 is a scale kept by the US Naval Observatory and is also based on numerous frequency standards kept in North America and Western Europe. A1 differs from A3 by a nearly constant amount of $- 3 4 . 4 \mathrm { m s }$ . Fluctuations between AT and A1 have not exceeded a small fraction of a millisecond since 1969.

Ephemeris time. To study the irregularities in the Earth's speed of rotation back beyond 1955 when atomic time first became available,a time scale determined from the astronomical data itself must be introduced. This is ephemeris time (ET),a uniform time scale that satisfies the Newtonian equations of motion of the Sun, Moon and planets and that is deduced from a comparison of astronomical observations with gravitational theories of these motions. Observed positions,with times measured by pendulums, refer to universal time,due to the inability of these clocks to maintain a time scale that is independent of the Earth's rotation for much longer than a year. Computed positions are based on the assumption that the Earth keeps a uniform time. Discrepancies between the two sets of positions determine the relation between the time scales, within the limitations of the observations and of the orbital theory. In principle,ET is defined in terms of the orbital motion of the Earth about