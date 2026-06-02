![](images/97f1af241706966536b2465ef71f590782242cb6d671661bfe9cc2e7ee9543a6.jpg)  
Fig. 4.1 Instantaneous rest frame of a particle moving on a timelike world line in spacetime.

Suppose that we follow the motion of a particle with velocity vector $u ^ { \alpha }$ . At any point on the world line we may employ the unit vector $e _ { ( 0 ) } ^ { \alpha } : = u ^ { \alpha } / c$ to define a preferred (timelike) direction in spacetime; this is a unit vector because the norm of $u ^ { \alpha }$ is equal to $- c ^ { 2 }$ . This direction and the three (spatial) directions orthogonal to it define the particle’s rest frame at this moment (see Fig. 4.1). The spatial directions are spanned by three unit vectors $e _ { ( 1 ) } ^ { \alpha }$ , $e _ { ( 2 ) } ^ { \alpha }$ , and $e _ { ( 3 ) } ^ { \alpha }$ ; these are chosen to be mutually orthogonal, and they are also orthogonal to $e _ { ( 0 ) } ^ { \alpha }$ .

Any vector field $A ^ { \alpha } ( \tau )$ on the world line can be decomposed in the vectorial basis just defined. We have

$$
A ^ { \alpha } = A ^ { ( 0 ) } e _ { ( 0 ) } ^ { \alpha } + A ^ { ( 1 ) } e _ { ( 1 ) } ^ { \alpha } + A ^ { ( 2 ) } e _ { ( 2 ) } ^ { \alpha } + A ^ { ( 3 ) } e _ { ( 3 ) } ^ { \alpha } ,
$$

and $A ^ { ( 0 ) } = - A _ { \alpha } e _ { ( 0 ) } ^ { \alpha }$ , $A ^ { ( j ) } = A _ { \alpha } e _ { ( j ) } ^ { \alpha }$ are the projections of the vector onto the selected basis.

For concreteness, suppose that the particle is momentarily moving in the $x$ -direction when viewed in a frame $S$ . Then $e _ { ( 0 ) } ^ { \alpha } = u ^ { \alpha } / c = \gamma ( 1 , \upsilon / c , 0 , 0 )$ , and an appropriate spatial basis is given by $e _ { ( 1 ) } ^ { \alpha } = \gamma ( v / c , 1 , 0 , 0 )$ , $e _ { ( 2 ) } ^ { \alpha } = ( 0 , 0 , 1 , 0 )$ , and $e _ { ( 3 ) } ^ { \alpha } = ( 0 , 0 , 0 , 1 )$ . It is easy to verify that these vectors are all of unit length and mutually orthogonal. We observe that when $v = 0$ , the vector $e _ { ( 1 ) } ^ { \alpha }$ points in the $x$ -direction; in a frame $S ^ { \prime }$ momentarily comoving with the particle, the vector points in the $x ^ { \prime }$ -direction. (We shall make use of this observation in the following subsection.)

Given a vector field $A ^ { \alpha } ( \tau )$ on the world line, its component along the timelike direction $e _ { ( 0 ) } ^ { \alpha }$ can easily be extracted by acting with the longitudinal projection operator $- e _ { ( 0 ) } ^ { \alpha } e _ { ( 0 ) \beta }$ ;

we get

$$
\left( - e _ { ( 0 ) } ^ { \alpha } e _ { ( 0 ) \beta } \right) A ^ { \beta } = A ^ { ( 0 ) } e _ { ( 0 ) } ^ { \alpha } .
$$

On the other hand, the components orthogonal to $u ^ { \alpha }$ can be extracted by acting with the transverse projection operator

$$
P _ { \beta } ^ { \alpha } : = \delta _ { \beta } ^ { \alpha } + e _ { ( 0 ) } ^ { \alpha } e _ { ( 0 ) \beta } = \delta _ { \beta } ^ { \alpha } + u ^ { \alpha } u _ { \beta } / c ^ { 2 } ;
$$

simple manipulations do indeed reveal that

$$
P _ { \beta } ^ { \alpha } A ^ { \beta } = A ^ { ( j ) } e _ { ( j ) } ^ { \alpha } .
$$

The projection operator satisfies the identities

$$
P _ { \beta } ^ { \alpha } u ^ { \beta } = 0 = u _ { \alpha } P _ { \beta } ^ { \alpha } , \qquad P _ { \mu } ^ { \alpha } P _ { \beta } ^ { \mu } = P _ { \beta } ^ { \alpha } , \qquad P _ { \alpha } ^ { \alpha } = 3 ,
$$

and it can be expanded as $P ^ { \alpha \beta } = e _ { ( 1 ) } ^ { \alpha } e _ { ( 1 ) } ^ { \beta } + e _ { ( 2 ) } ^ { \alpha } e _ { ( 2 ) } ^ { \beta } + e _ { ( 3 ) } ^ { \alpha } e _ { ( 3 ) } ^ { \beta }$ in terms of the transverse basis $e _ { ( j ) } ^ { \alpha }$ .

# 4.1.6 Photons

A particle moving with the speed of light traces a world line along which $d s ^ { 2 }$ vanishes everywhere. According to Eq. (4.8), this implies that $d \tau = 0$ along the world line, and we conclude that the proper time of a photon is not defined. This, finally, implies that the photon’s velocity vector $u ^ { \alpha }$ also is not defined.

Nevertheless, the momentum vector of a photon is well defined, in spite of the fact that $m = 0$ and $u ^ { \alpha }$ is not defined. It can be obtained by a limiting procedure in which the speed of the particle is taken to reach $c$ , with $d \tau$ and $m$ each taken to approach zero while keeping their ratio $d \tau / m$ fixed. In other words, the momentum vector is defined as the limit

$$
p ^ { \alpha } = \operatorname* { l i m } \frac { d r ^ { \alpha } } { d ( \tau / m ) } ,
$$

in which the particle’s speed approaches the speed of light. In the limit the rescaled worldline parameter $\tau / m$ becomes $\lambda$ , the photon’s world line is represented by the parametric relations $r ^ { \alpha } ( \lambda )$ , and we have $p ^ { \alpha } = d r ^ { \alpha } / d \lambda$ . The momentum of a photon satisfies the null condition

$$
p _ { \alpha } p ^ { \alpha } = 0 ,
$$

which states that the photon’s rest-mass $m$ is zero. The time component of the momentum vector (the photon’s energy $\hbar \omega$ as measured by an observer attached to the frame $S$ , divided by the speed of light) is not independent of the spatial components. If we write $p ^ { \alpha } = ( \hbar \omega / c , \hbar k )$ , with the spatial components expressed in terms of a wave vector $\pmb { k }$ , then Eq. (4.24) gives rise to the well-known dispersion relation $\omega ^ { 2 } = c ^ { 2 } k ^ { 2 }$ , where $k ^ { 2 } = \pmb { k } \cdot \pmb { k }$ . This allows us to express the momentum vector as

$$
p ^ { \alpha } = \frac { \hbar \omega } { c } ( 1 , \hat { k } ) ,
$$

where $\hat { k }$ is a unit vector (in the three-dimensional, Newtonian sense) that indicates the photon’s direction of propagation, so that $\pmb { k } = ( \omega / c ) \pmb { \hat { k } }$ .

<table><tr><td>Box 4.3</td><td>Photons: An alternative viewpoint</td></tr><tr><td></td><td>The reader might object to the limiting procedure used in Eq. (4.23),because it is not a physicall realizable procedure. The deeper justification for Eqs. (4.24)and (4.25) comes from Maxwel&#x27;s equations and quantum mechanics.In the limit where the wavelength of light is short compared to allother scales of variation in the problem (the geometrical optics limit), Maxwel&#x27;s equations require that the spacetime wave vector K := δαS be null,where S is the phase ofthe wave. Quantization ofMaxwell&#x27;s equations then reveals that h kα = (hω/c)(1, k) = p&amp;.The geometrical optics imit is discussed further in Box 5.6, in the context of curved spacetime.</td></tr></table>

The argument that leads to Eq. (4.16) applies just as well to photons, and we may immediately state that

$$
\hbar \omega _ { \mathrm { o b s } } = - p _ { \alpha } u _ { \mathrm { o b s } } ^ { \alpha }
$$

is the photon’s energy as measured by an observer moving with a velocity $u _ { \mathrm { o b s } } ^ { \alpha }$ . With $u _ { \mathrm { 0 b s } } ^ { \alpha } = \gamma ( c , \pmb { v } _ { \mathrm { 0 b s } } )$ , this is

$$
\hbar \omega _ { \mathrm { o b s } } = \hbar \omega \frac { 1 - \hat { \pmb { k } } \cdot \pmb { v } _ { \mathrm { o b s } } / c } { \sqrt { 1 - ( v _ { \mathrm { o b s } } / c ) ^ { 2 } } } ,
$$

and we have obtained the well-known formula for the Doppler effect applied to light and other forms of radiation. Although we derived Eq. (4.27) using relativistic methods, it is good to remember that it is really a mixture of the non-relativistic, first-order Doppler effect caused by the piling up or stretching out of the waves as seen by the moving observer – the $- \hat { \pmb { k } } \cdot \pmb { v } _ { \mathrm { o b s } } / c$ term, which can be applied to any type of wave by replacing $c$ by the actual wave speed – and the relativistic time dilation of the observer’s clock compared to the laboratory clock – the usual $\gamma$ factor.

Another interesting phenomenon involving light is its aberration, the observed property that the apparent position of an astronomical body depends on the velocity of the observer. This phenomenon was first discovered by James Bradley in 1725, and a few years later he developed a theory of aberration based on Newton’s corpuscular model for light. The explanation was simple: the apparent position shifts for the same reason that you have to tilt your umbrella forward when walking through an otherwise vertical rainfall. Bradley’s theory did not survive the transition to a wave theory of light, but it is interesting to note that the wave theory could not account for the aberration until various ad hoc models of a dragged aether were concocted precisely to save the phenomenon. It was Einstein, finally, who showed how to reconcile aberration with Maxwell’s theory in his famous 1905 paper on the electrodynamics of moving bodies.

Suppose that in a frame $S$ , a photon with frequency $\omega$ is moving in the direction of the unit vector $\hat { k }$ . We align our coordinates so that $\pmb { \hat { k } } = ( \cos \alpha _ { \mathrm { r e s t } }$ , $\sin \alpha _ { \mathrm { r e s t } } , 0$ ); the photon moves in the $x - y$ plane, and its trajectory makes an angle $\alpha _ { \mathrm { r e s t } }$ with respect to the $x$ -axis.

This is the angle that is measured by an observer at rest in the frame $S$ , and we can derive a formula for $\cos \alpha _ { \mathrm { r e s t } }$ that involves spacetime invariants only. For this purpose we reintroduce the photon’s momentum vector $p ^ { \alpha } = c ^ { - 1 } \hbar \omega ( 1 , \hat { k } )$ , the observer’s velocity vector $u _ { \mathrm { r e s t } } ^ { \alpha } = \left( c , 0 , 0 , 0 \right)$ , and the spatial vector $e _ { \mathrm { r e s t } } ^ { \alpha } = ( 0 , 1 , 0 , 0 )$ that points in the $x$ -direction; this vector is orthogonal to $u ^ { \alpha }$ , and is one of the three spatial vectors that span the rest frame of our observer. It is easy to verify that

$$
\cos \alpha _ { \mathrm { { r e s t } } } = c { \frac { p _ { \alpha } e _ { \mathrm { { r e s t } } } ^ { \alpha } } { - p _ { \beta } u _ { \mathrm { { r e s t } } } ^ { \beta } } }
$$

is the desired formula.

We next introduce another observer – let’s call her Leslie – moving relative to $S$ with a velocity $u ^ { \alpha }$ . We assume that at the time Leslie encounters the photon, she is momentarily moving in the $x$ -direction, so that $u ^ { \alpha } = \gamma ( c , v , 0 , 0 )$ . At this moment Leslie is at rest relative to the comoving frame $S ^ { \prime }$ , which moves uniformly with speed $v$ with respect to $S$ . For an observer (a third!) at rest in this frame, Eq. (4.28) applies, because it is expressed in terms of spacetime invariants. Because the angle $\alpha$ measured by Leslie is the same as the angle measured by the third observer (the one at rest in $S ^ { \prime }$ ), we can immediately state that

$$
\cos \alpha = c \frac { p _ { \alpha } e ^ { \alpha } } { - p _ { \beta } u ^ { \beta } } ,
$$

where $e ^ { \alpha }$ is a spatial vector that points in the direction of the $x ^ { \prime }$ -axis. An expression for this was worked out in the preceding subsection; we have that $e ^ { \alpha } = \gamma ( v / c , 1 , 0 , 0 )$ . Making the substitutions for $p ^ { \alpha } , u ^ { \alpha }$ , and $e ^ { \alpha }$ in Eq. (4.29) returns

$$
\cos \alpha = \frac { \cos \alpha _ { \mathrm { { r e s t } } } - { v } / { c } } { 1 - ( { v } / { c } ) \cos \alpha _ { \mathrm { { r e s t } } } } .
$$

This gives the photon’s angle $\alpha$ , as measured by an observer moving with speed $v$ , in terms of the angle $\alpha _ { \mathrm { r e s t } }$ measured by an observer at rest. Equation (4.30) is the mathematical description of the aberration of light. Like the Doppler effect, this is a mixture of nonrelativistic and relativistic effects. To first order in $v / c$ , the effect can be derived simply by calculating the angle between the vector $\boldsymbol { c } \hat { \boldsymbol { k } } - \boldsymbol { v }$ (light’s velocity as seen in $S ^ { \prime }$ ) and the vector $\pmb { v }$ . Relativistic effects occur at order $( v / c ) ^ { 2 }$ . The first-order effect applies just as well to raindrops, provided that you replace $c$ by the appropriate speed of the projectile.

# 4.1.7 Particle dynamics

Our considerations so far have been entirely kinematical, and in the next three sections we will examine some dynamical aspects of physics in Minkowski spacetime. As a warm-up exercise we describe here what would be required of a dynamics of (massive) particles.

The acceleration vector of a particle with world line $r ^ { \alpha } ( \tau )$ and velocity $u ^ { \alpha } ( \tau ) = d r ^ { \alpha } / d \tau$ is defined as

$$
a ^ { \alpha } : = { \frac { d u ^ { \alpha } } { d \tau } } .
$$

It is an important fact that in spacetime, the acceleration is everywhere orthogonal to the velocity:

$$
{ a _ { \alpha } } { u } ^ { \alpha } = 0 ;
$$

this is an immediate consequence of the normalization condition $\eta _ { \alpha \beta } u ^ { \alpha } u ^ { \beta } = - c ^ { 2 }$ . (To see this, differentiate with respect to $\tau$ , and use the symmetry of the metric tensor.) Equation (4.32) implies that the four components of the vector $a ^ { \alpha }$ are not all independent. If we write $u ^ { \alpha } = \gamma ( c , \pmb { v } )$ and $a ^ { \alpha } = ( a ^ { 0 } , { \pmb a } )$ , then Eq. (4.32) implies that $a ^ { 0 } = ( { \pmb a } \cdot { \pmb v } ) / c$ . Note that while ${ \pmb v } = d { \pmb r } / d t$ is the Newtonian velocity vector, $\pmb { a }$ is not equal to the Newtonian acceleration; we have $\pmb { a } = d ^ { 2 } \pmb { r } / d \tau ^ { 2 }$ instead of $d ^ { 2 } r / d t ^ { 2 }$ .

A dynamical law will relate the acceleration of a particle to the forces acting upon it. A relativistic version of Newton’s second law must take a vectorial form in spacetime, and we therefore write

$$
F ^ { \alpha } = m a ^ { \alpha } ,
$$

where $m$ is the particle’s rest mass and $F ^ { \alpha }$ is a force vector supplied by the dynamical theory. To be consistent with the basic kinematical constraint of Eq. (4.32), the force vector must be everywhere orthogonal to the velocity vector. If we write $F ^ { \alpha } = ( F ^ { 0 } , F )$ , then $F ^ { 0 } = ( F \cdot v ) / c$ . Apart from the factor of $c$ , we recognize on the right-hand side the relativistic generalization of the rate at which the spatial components of the force do work on the particle. The zeroth component of Eq. (4.33), therefore, is a relativistic statement of the work–energy theorem.

# 4.1.8 Free particle motion and maximum proper time

A freely-moving particle is one on which no forces act. For such a particle, $a ^ { \alpha } = 0$ , $u ^ { \alpha } = u _ { 0 } ^ { \alpha } = \operatorname { c o n s t a n t } , x ^ { \alpha } = x _ { 0 } ^ { \alpha } + u _ { 0 } ^ { \alpha } \tau$ , and the particle moves on a straight line in spacetime. This motion, as trivial as it may seem, arises from an action principle, just as in Newtonian dynamics.

In Newtonian dynamics the action functional of a free particle is given by $\textstyle S = \int _ { 1 } ^ { 2 } L d t$ , with a Lagrangian function $\begin{array} { r } { L = { \frac { 1 } { 2 } } m v ^ { 2 } } \end{array}$ . In relativistic dynamics the action must be a Lorentz invariant, and it must have the dimension of an energy multiplied by time. We adopt

$$
S = - m c ^ { 2 } \int _ { 1 } ^ { 2 } d \tau
$$

as a suitable candidate with the required properties, and show that it leads to sensible results.

We saw back in Sec. 4.1.3 that the interval of proper time $d \tau$ along any world line is related to the spacetime interval $d s ^ { 2 }$ by $d \tau = c ^ { - 1 } \sqrt { - d s ^ { 2 } }$ . Writing this in full, we have

$$
{ \begin{array} { c } { d \tau = { \frac { 1 } { c } } { \sqrt { - \eta _ { \alpha \beta } d r ^ { \alpha } d r ^ { \beta } } } } \\ { = { \frac { 1 } { c } } { \sqrt { - \eta _ { \alpha \beta } { \cfrac { d r ^ { \alpha } } { d t } } { \cfrac { d r ^ { \beta } } { d t } } } } d t , } \end{array} }
$$

where, in the second step, we divided the coordinate interval $d r ^ { \alpha }$ along the world line by the coordinate-time interval $d t$ . These manipulations reveal that the action of Eq. (4.34) can be expressed in the standard form $\textstyle S = { \int _ { 1 } ^ { 2 } L d t }$ , with a relativistic Lagrangian

$$
L = - m c \sqrt { - \eta _ { \alpha \beta } \frac { d r ^ { \alpha } } { d t } \frac { d r ^ { \beta } } { d t } } .
$$

A more explicit form is

$$
L = - m c ^ { 2 } { \sqrt { 1 - v ^ { 2 } / c ^ { 2 } } } ,
$$

where $\scriptstyle v ^ { 2 } : = v \cdot v$ . To see that the action of Eq. (4.34) is in fact a sensible choice, we expand the Lagrangian in powers of $v / c$ and examine the non-relativistic limit. We get $L =$ $- m c ^ { 2 } + { \textstyle \frac { 1 } { 2 } } m v ^ { 2 } + { \textstyle \frac { 1 } { 8 } } m v ^ { 4 } / c ^ { 2 } + \cdot \cdot \cdot$ , and we see that up to the irrelevant constant $- m c ^ { 2 }$ , the Lagrangian is equal to the Newtonian kinetic energy $\scriptstyle { \frac { 1 } { 2 } } m v ^ { 2 }$ to leading order; the additional terms are relativistic corrections to the kinetic energy.

The particle’s dynamics is obtained by demanding that the action of Eq. (4.34) be stationary under arbitrary variations of the world line, with the usual provision that all world lines must link the same initial event 1 to the same final event 2. The calculus of variations implies that the Lagrangian of Eq. (4.36) must satisfy the Euler–Lagrange equations

$$
\frac { d } { d t } \frac { \partial L } { \partial v ^ { \alpha } } - \frac { \partial L } { \partial r ^ { \alpha } } = 0 ,
$$

where $v ^ { \alpha } : = d r ^ { \alpha } / d t$ . The Lagrangian is actually independent of $r ^ { \alpha }$ , and we obtain

$$
\eta _ { \alpha \beta } \frac { d } { d t } \biggl ( \frac { v ^ { \beta } } { \sqrt { - \eta _ { \mu \nu } v ^ { \mu } v ^ { \nu } } } \biggr ) = 0 .
$$

This implies that

$$
\frac { d } { d t } \bigg ( \frac { d r ^ { \alpha } / d t } { d \tau / d t } \bigg ) = \frac { d } { d t } \bigg ( \frac { d r ^ { \alpha } } { d \tau } \bigg ) = 0 ,
$$

and converting the coordinate-time derivative to a proper-time derivative, we arrive at

$$
a ^ { \alpha } = \frac { d u ^ { \alpha } } { d \tau } = \frac { d ^ { 2 } r ^ { \alpha } } { d \tau ^ { 2 } } = 0 ,
$$

which indeed corresponds to free particle motion.

The action functional of a relativistic particle is directly related to the elapsed proper time between the events 1 and 2. An extremum of the action is therefore an extremum of proper time, and it can be verified that the uniform motion of a free particle actually maximizes the elapsed proper time between the two events. This conclusion is a feature of timelike curves in spacetime; for spacelike curves we would find instead that a straight line minimizes the proper distance between two events.

# 4.2 Relativistic hydrodynamics

# 4.2.1 Fluid variables

In Chapter 1 we introduced a number of variables that describe the physical state of a Newtonian fluid. These were the velocity field $\pmb { v }$ , the mass density $\rho$ , the pressure $p$ , the internal energy density $\epsilon$ , the rate of heat generation $q$ , and the heat flux $\pmb { H }$ ; all of these are functions of time $t$ and position $_ x$ within the fluid. A spacetime formulation of the laws of hydrodynamics also involves such quantities, and it is straightforward, for example, to promote the Newtonian velocity field $\pmb { v }$ to a relativistic velocity field $u ^ { \alpha } = \gamma ( c , \pmb { v } )$ . It is more delicate, however, to generalize the densities $\rho$ and $\epsilon$ , because of issues of frame dependence that arise in special relativity. In which frame is the mass density to be defined? An answer is required, because Lorentz contraction implies that a density measured in one frame $S$ will differ by a factor of $\gamma$ from a density measured in another frame $S ^ { \prime }$ . The most useful answer turns out to be: Measure all densities at an event $x ^ { \alpha } = ( c t , x )$ in spacetime in the Lorentz frame that is momentarily comoving with the fluid element at that event. Thus, the fluid’s proper mass density $\rho ( x ^ { \alpha } )$ shall be the mass per unit volume as measured in the MCLF of a fluid element at $x ^ { \alpha }$ ; as such $\rho$ is a spacetime invariant whose value does not depend on the Lorentz frame. Similarly, we define $\epsilon ( x ^ { \alpha } )$ to be the proper density of internal (thermodynamic) energy contained in a fluid element at $x ^ { \alpha }$ , as measured in the comoving Lorentz frame. These quantities combine naturally into

$$
\mu : = \rho c ^ { 2 } + \epsilon ,
$$

the total energy density (including rest-mass energy and internal energy) of the fluid element. Like $\rho$ and $\epsilon , \mu$ is a spacetime invariant.

We shall also agree that the fluid’s pressure $p ( x ^ { \alpha } )$ is to be measured in the momentarily comoving Lorentz frame at $x ^ { \alpha }$ , and like the densities considered previously, $p$ also is a spacetime invariant. Our list of fluid variables is now complete; for our purposes in this book we shall not require relativistic generalizations of the heat variables $q$ and $\pmb { H }$ .

# 4.2.2 Mass current

Having introduced the proper mass density $\rho ( x ^ { \alpha } )$ , which refers to an infinite number of momentarily comoving frames spread out throughout the fluid, we now wish to introduce quantities that describe the fluid’s mass distribution as seen in a single (and global) Lorentz frame $S$ ; we shall think of this as the “laboratory frame.” We define

$$
\begin{array} { r l } & { c ^ { - 1 } j ^ { 0 } : = \mathrm { H u i d ~ m a s s ~ d e n s i t y } , \mathrm { a s ~ m e a s u r e d ~ i n ~ } S , } \\ & { \qquad j ^ { k } : = \mathrm { m a s s ~ f l u x ~ i n ~ t h e ~ } x ^ { k } \mathrm { - d i r e c t i o n } , \mathrm { a s ~ m e a s u r e d ~ i n ~ } S ; } \end{array}
$$

the mass flux $j$ is defined so that ${ \boldsymbol { j } } \cdot d { \boldsymbol { S } } = j ^ { k } d S _ { k }$ is the mass crossing an element of surface $d S _ { k }$ per unit time. These quantities combine to form a spacetime vector $j ^ { \alpha }$ (which transforms appropriately under a Lorentz transformation), and the factor of ${ { c } ^ { - 1 } }$ was inserted to ensure that all components of $j ^ { \alpha }$ have a dimension of (mass)(velocity)/(volume). We shall call this vector the mass current.

The quantity $c ^ { - 1 } j ^ { 0 }$ is the fluid’s mass density as measured in the laboratory frame $S$ . This differs from the proper density $\rho$ by a factor of $\gamma$ , which takes into account the Lorentz contraction of a moving fluid element along its direction of motion. We have $c ^ { - 1 } j ^ { 0 } = \gamma \rho$ , and we see that $j ^ { 0 } = \rho u ^ { 0 }$ . The mass flux $j ^ { k }$ is the mass density of a fluid element multiplied by its velocity (all measured in $S$ ), and we have $j ^ { k } = ( \gamma \rho ) v ^ { k } = \rho u ^ { k }$ . We conclude that the mass-current vector can be related to the proper density $\rho$ and the velocity field $u ^ { \alpha }$ by

$$
\begin{array} { r } { j ^ { \alpha } = \rho u ^ { \alpha } . } \end{array}
$$

This equation reveals very clearly that $j ^ { \alpha }$ is indeed a spacetime vector, because it is the product of a scalar $\rho$ and a vector $u ^ { \alpha }$ .

Conservation of (rest-)mass is a very important property of a fluid, and we next work on a mathematical formulation of this property. We examine a three-dimensional volume $V$ of the fluid, bounded by a two-dimensional surface $\Sigma$ ; the volume is arbitrarily large or small, and is taken to be in a fixed position in the laboratory frame $S$ . The fluid flows freely in and out of the volume, and

$$
- \frac { d } { d t } \int _ { V } c ^ { - 1 } j ^ { 0 } d ^ { 3 } x = - \int _ { V } \frac { \partial j ^ { 0 } } { \partial x ^ { 0 } } d ^ { 3 } x
$$

is the amount of mass that leaves $V$ per unit time. On the other hand,

$$
\oint _ { \Sigma } j ^ { k } d S _ { k } = \int _ { V } { \frac { \partial j ^ { k } } { \partial x ^ { k } } } d ^ { 3 } x
$$

is the amount of mass that crosses the surface $\Sigma$ per unit time; we use the divergence theorem to convert the surface integral into a volume integral. Conservation of mass dictates a strict equality between the two results, and the arbitrariness of $V$ implies that

$$
\partial _ { \alpha } j ^ { \alpha } = 0 .
$$

This equation is the mathematical expression of local mass conservation; the mass-current vector is divergence-free in spacetime. We shall explore the consequences of this equation below.

# 4.2.3 Energy-momentum tensor

Having introduced the proper energy density $\mu$ in Eq. (4.42), we next turn to a description of energy density, energy flux, momentum density, and momentum flux as viewed in the laboratory frame S. But instead of defining a vector field, as we did for the mass current, we are forced here to define a tensor field. This can be seen most easily by considering the energy density of a fluid element that moves through the laboratory with speed $v$ . The energy contained in the fluid element is increased by the relativistic factor $\gamma$ , while its volume is decreased by the Lorentz contraction factor $1 / \gamma$ . Its energy density is therefore equal to $\mu \gamma ^ { 2 } = \mu u ^ { 0 } u ^ { 0 } / c ^ { 2 }$ , and this suggests that we need a tensor to properly describe this quantity.

We define

$$
\begin{array} { c } { { T ^ { 0 0 } : = \mathrm { e n e r g y ~ d e n s i t y } , } } \\ { { { } } } \\ { { c T ^ { 0 j } : = \mathrm { e n e r g y ~ f l u x ~ i n ~ t h e ~ } x ^ { j } \ – \mathrm { d i r e c t i o n } , } } \\ { { { } c ^ { - 1 } T ^ { j 0 } : = \mathrm { d e n s i t y ~ o f ~ } j \mathrm { - c o m p o n e n t ~ o f ~ m o m e n t u m } , } } \\ { { { } } } \\ { { T ^ { j k } : = \mathrm { H u x ~ o f ~ } j \mathrm { - m o m e n t u m ~ i n ~ t h e ~ } x ^ { k } \mathrm { - d i r e c t i o n } ; } } \end{array}
$$

these quantities are all measured in $S$ . The fluxes are defined so that $c T ^ { 0 j } d S _ { j }$ is the energy crossing an element of surface $d S _ { j }$ per unit time, while $T ^ { j k } d S _ { k }$ is the $j$ -component of the momentum vector crossing the element $d S _ { k }$ per unit time. The quantities defined above combine to form the energy-momentum tensor $T ^ { \alpha \beta }$ , and each component of this tensor has a dimension of (energy)/(volume).

The argument that led to Eq. (4.47) can easily be adapted to describe the local conservation of energy and momentum. In this way we find that $\partial _ { \beta } T ^ { 0 \beta } = 0$ is a statement of energy conservation, while $\partial _ { \beta } T ^ { j \beta } = 0$ is a statement of momentum conservation (one for each spatial direction labeled by $j$ ). All together, these give rise to the tensorial statement

$$
\partial _ { \beta } T ^ { \alpha \beta } = 0
$$

of energy-momentum conservation. The energy-momentum tensor is divergence-free when energy and momentum are locally conserved.

Our considerations thus far have been general, and we next specialize them to the case at hand, that of a perfect fluid. We wish to relate $T ^ { \alpha \beta }$ to other fluid variables such as $\mu , p$ , and $u ^ { \alpha }$ . To begin we consider the special case of a fluid at rest, without pressure. In this case the fluid’s energy density in $S$ is the same as its proper density, and we have that $T ^ { 0 0 } = \mu$ . In addition, the fluid’s momentum is zero, and all fluxes vanish, so that $T ^ { 0 0 }$ is the only non-vanishing component of the energy-momentum tensor. On the other hand, the fluid’s velocity field is $u ^ { \alpha } = ( c , 0 , 0 , 0 )$ , and we deduce the equality $T ^ { \alpha \beta } = \mu u ^ { \alpha } u ^ { \beta } / c ^ { 2 }$ .

We next consider the case of a moving fluid, still without pressure. We select a fluid element and a moment of time, and we let $u ^ { \alpha } = \gamma ( c , \pmb { v } )$ be the velocity vector of the fluid element at that time. The energy density of the fluid element as measured in $S$ differs from $\mu$ by two factors of $\gamma$ , as we discussed previously; we have $T ^ { 0 0 } = \mu \gamma ^ { 2 }$ . The energy flux is this multiplied by the velocity of the fluid element: $c T ^ { 0 j } = ( \mu \gamma ^ { 2 } ) v ^ { j } .$ . The density of momentum can be expressed as (energy density)(momentum/energy), and since the momentum per energy of a fluid element is $p ^ { j } / ( c p ^ { 0 } ) = v ^ { j } / c ^ { 2 }$ , this is $c ^ { - 1 } T ^ { j 0 } = ( \mu \gamma ^ { 2 } ) ( v ^ { j } / c ^ { 2 } )$ . And finally, the momentum flux is $T ^ { j k } = ( \mu \gamma ^ { 2 } ) ( v ^ { j } v ^ { k } / c ^ { 2 } )$ . Once more we find that these results are summarized by the equation $T ^ { \alpha \beta } = \mu u ^ { \alpha } u ^ { \beta } / c ^ { 2 }$ .

This expression must be altered to account for the fluid’s pressure. We return to the fluid at rest and re-examine the spatial components of the energy-momentum tensor. By definition we have that $T ^ { j k } d S _ { k }$ is the rate of momentum transfer across an element of surface $d S _ { k }$ . This is also, by Newton’s second law, the force acting on the surface element (directed out of the surface). In the case of a perfect fluid, for which there are no shear forces generated by viscosity, the only such force is created by pressure, and the pressure necessarily acts in the surface’s normal direction. From this we conclude that for a perfect fluid at rest, $T ^ { j k }$ must be equal to $p \delta ^ { j k }$ . The result remains valid for a moving fluid, provided that the equality is stated in the MCLF of each fluid element. A more general statement must involve a tensor $P ^ { \alpha \beta }$ that replaces $\delta ^ { j k }$ and reduces to it in the comoving Lorentz frame. This tensor must be orthogonal to $u ^ { \alpha } u ^ { \beta } / c ^ { 2 }$ , and it was identified back in Eq. (4.20) as the transverse projection operator $P ^ { \alpha \beta } = \eta ^ { \alpha \beta } + u ^ { \alpha } u ^ { \beta } / c ^ { 2 }$ . We conclude, finally, that the pressure contribution to the energy-momentum tensor must be $p P ^ { \alpha \beta }$ .

All in all we have obtained the following expression for the energy-momentum tensor of a perfect fluid:

$$
T ^ { \alpha \beta } = \mu u ^ { \alpha } u ^ { \beta } / c ^ { 2 } + p \big ( \eta ^ { \alpha \beta } + u ^ { \alpha } u ^ { \beta } / c ^ { 2 } \big ) = ( \mu + p ) u ^ { \alpha } u ^ { \beta } / c ^ { 2 } + p \eta ^ { \alpha \beta } ,
$$

where, we recall, $\mu = \rho c ^ { 2 } + \epsilon$ is the fluid’s proper energy density.

We note that according to Eq. (4.50), the energy-momentum tensor is symmetric under an exchange of indices,

$$
T ^ { \beta \alpha } = T ^ { \alpha \beta } .
$$

This property is in fact very general, and not restricted to the specific case of a perfect fluid.

# 4.2.4 Fluid dynamics

All of fluid mechanics is contained in the conservation statements $\partial _ { \alpha } j ^ { \alpha } = 0 = \partial _ { \beta } T ^ { \alpha \beta }$ , along with the assignments of Eqs. (4.44) and (4.50).

We first examine the consequences of Eq. (4.47), in which we substitute $j ^ { \alpha } = \rho u ^ { \alpha }$ . If we also write $u ^ { \alpha } = \gamma ( c , \pmb { v } )$ , then the equation of mass conservation states that

$$
\begin{array} { r } { \partial _ { t } ( \gamma \rho ) + \partial _ { j } ( \gamma \rho v ^ { j } ) = 0 . } \end{array}
$$

This is the relativistic generalization of Eq. (1.26), the Eulerian version of the continuity equation first encountered in Chapter 1; the relativistic equation reduces to the Newtonian version when $v / c \ll 1$ and $\gamma \simeq 1$ . The equation of mass conservation can also be expressed in Lagrangian form, if we write it first in the form $u ^ { \alpha } \partial _ { \alpha } \rho + \rho \partial _ { \alpha } u ^ { \alpha } = 0$ . The first term is the derivative of the proper density in the direction of the velocity field; if we focus our attention on a selected fluid element moving on a world line $r ^ { \alpha } ( \tau )$ , and write $u ^ { \alpha } =$ $d r ^ { \alpha } / d \tau$ for its velocity vector, then $u ^ { \alpha } \partial _ { \alpha } \rho$ is recognized as $d \rho / d \tau$ , the change in proper density as we follow the world line of the fluid element. Equation (4.47) can therefore be expressed as

$$
\frac { d \rho } { d \tau } + \rho \partial _ { \alpha } u ^ { \alpha } = 0 ,
$$

and this is the relativistic generalization of Eq. (1.25). This equation informs us that $\partial _ { \alpha } u ^ { \alpha } = - \rho ^ { - 1 } d \rho / d \tau = \mathcal { V } ^ { - 1 } d \mathcal { V } / d \tau$ , where $\mathcal { V } = \delta m / \rho$ is the volume of a fluid element of mass $\delta m$ .

We next work on Eq. (4.49), in which we substitute Eq. (4.50). Simple manipulations first return

$$
0 = u ^ { \alpha } \bigg ( \frac { d \mu } { d \tau } + ( \mu + p ) \partial _ { \beta } u ^ { \beta } \bigg ) + ( \mu + p ) \frac { d u ^ { \alpha } } { d \tau } + c ^ { 2 } P ^ { \alpha \beta } \partial _ { \beta } p ,
$$

in which we have written $d \mu / d \tau$ for $u ^ { \beta } \partial _ { \beta } \mu$ and $d u ^ { \alpha } / d \tau$ for $u ^ { \beta } \partial _ { \beta } u ^ { \alpha }$ , adopting the Lagrangian point of view that these derivatives follow the world line of a selected fluid element. The first set of terms in this expression is directed along $u ^ { \alpha }$ , while the remaining terms are orthogonal to $u ^ { \alpha }$ – refer to Eqs. (4.22) and (4.32). We set each orthogonal piece of this equation to zero, and obtain

$$
\frac { d \mu } { d \tau } + ( \mu + p ) \partial _ { \beta } u ^ { \beta } = 0
$$

and

$$
( \mu + p ) \frac { d u ^ { \alpha } } { d \tau } + c ^ { 2 } P ^ { \alpha \beta } \partial _ { \beta } p = 0 .
$$

To elucidate the meaning of Eq. (4.55) we make the substitutions $\mu = \rho c ^ { 2 } + \epsilon$ and $\partial _ { \alpha } u ^ { \alpha } =$ $- \rho ^ { - 1 } d \rho / d \tau$ . After some cancellations we obtain

$$
\frac { d \epsilon } { d \tau } - \frac { \epsilon + p } { \rho } \frac { d \rho } { d \tau } = 0 .
$$

This is precisely the same equation, Eq. (1.29), that was recognized in Chapter 1 as expressing the first law of thermodynamics for isentropic flows. To see this clearly, replace $\rho$ by $\delta m / \nu$ and write Eq. (4.57) as $d ( \epsilon \mathcal { V } ) = - p d \mathcal { V }$ , which is a more recognizable form of the first law. It is a remarkable fact that the laws of thermodynamics do not require modifications in the transition from Newtonian physics to Minkowski spacetime, mainly because they are formulated in the momentarily comoving Lorentz frame of each fluid element.

Equation (4.56) is the relativistic generalization of Euler’s equation, which was first displayed in Eq. (1.23); it involves the acceleration $d u ^ { \alpha } / d \tau = u ^ { \beta } \partial _ { \beta } u ^ { \alpha }$ of a fluid element and the (spatially projected) pressure gradient $\partial _ { \beta } p$ . Note that the presence of the projection operator $P ^ { \alpha \beta }$ in this equation guarantees that the acceleration $d u ^ { \alpha } / d \tau$ is orthogonal to the velocity $u ^ { \alpha }$ .

A more explicit statement of Euler’s equation is

$$
( \rho + \epsilon / c ^ { 2 } + p / c ^ { 2 } ) \frac { d u ^ { \alpha } } { d \tau } = - \big ( \eta ^ { \alpha \beta } + u ^ { \alpha } u ^ { \beta } / c ^ { 2 } \big ) \partial _ { \beta } p .
$$

An even more explicit version is obtained when we write $u ^ { \alpha } = \gamma ( c , \pmb { v } )$ for the velocity field and focus on the spatial components of Eq. (4.58); this yields

$$
\gamma ( \rho + \epsilon / c ^ { 2 } + p / c ^ { 2 } ) ( \partial _ { t } + \pmb { v } \cdot \pmb { \nabla } ) ( \gamma \pmb { v } ^ { j } ) = - \partial _ { j } p - \gamma ^ { 2 } \nu ^ { j } ( \partial _ { t } + \pmb { v } \cdot \pmb { \nabla } ) p / c ^ { 2 } .
$$

This differs from the non-relativistic version in a number of places. First, the quantity that multiplies the Lagrangian derivative $d ( \gamma v ^ { j } ) / d t$ on the left-hand side is $\rho + \epsilon / c ^ { 2 } + p / c ^ { 2 }$ instead of just $\rho$ ; this tells us that in special relativity, the internal energy $\epsilon$ and the pressure $p$ participate in the fluid’s inertial response. Second, the Newtonian velocity $v ^ { j }$ is multiplied by $\gamma$ to convert it to a relativistic velocity, and the whole equation is multiplied by $\gamma$ to convert the time derivative $d / d t$ to a proper-time derivative $d / d \tau$ . Third, the right-hand side is modified by a term involving $d p / d t$ , the Lagrangian derivative of the pressure. All modifications become small when $v / c \ll 1$ , and in the limit we recover $\rho ( \partial _ { t } + \pmb { v } \cdot \nabla ) \pmb { v } = - \nabla p$ , the non-relativistic version of Euler’s equation.

# 4.3 Electrodynamics

# 4.3.1 Maxwell’s equations

The spacetime formulation of Maxwell’s theory involves an electromagnetic field tensor $F ^ { \alpha \beta }$ whose components are defined, in a frame $S$ , in terms of the electric field $E$ and the magnetic field $\pmb { B }$ . The tensor is antisymmetric, $F ^ { \beta \alpha } = - F ^ { \alpha \beta }$ , and it therefore contains six independent components. We make the assignments

$$
F ^ { 0 1 } = c ^ { - 1 } E ^ { x } , \qquad F ^ { 0 2 } = c ^ { - 1 } E ^ { y } , \qquad F ^ { 0 3 } = c ^ { - 1 } E ^ { z } ,
$$

as well as

$$
F ^ { 1 2 } = B ^ { z } , \qquad F ^ { 2 3 } = B ^ { x } , \qquad F ^ { 3 1 } = B ^ { y } .
$$

These equations are summarized by $F ^ { 0 j } = c ^ { - 1 } E ^ { j }$ and $F ^ { i j } = \epsilon ^ { i j k } B _ { k }$ , where $\epsilon _ { i j k }$ is the permutation symbol introduced in Sec. 1.4.4. The field $F ^ { \alpha \beta }$ transforms as a tensor under a Lorentz transformation, and this gives rise to the well-known transformation rules for $E$ and $\pmb { B }$ (see Exercise 4.8).

The spacetime formulation of electrodynamics must also involve a source for the electromagnetic field, and we take this to be a charged fluid. We introduce the proper charge density $\rho _ { e } ( x ^ { \alpha } )$ as the charge per unit volume that is measured by an observer momentarily comoving with the fluid element at $x ^ { \alpha }$ ; as such $\rho _ { e }$ , like the proper mass density $\rho$ introduced in Sec. 4.2, is a spacetime invariant whose value does not depend on the Lorentz frame. We introduce also a charge-current vector $j _ { e } ^ { \alpha }$ whose definition is very close to that of the mass-current vector of Eq. (4.44). We have that $c ^ { - 1 } j _ { e } ^ { 0 }$ is the charge density as measured in the laboratory frame $S$ , while $j _ { e } ^ { k }$ is the charge flux (or current) in the $x ^ { k }$ -direction. If $u ^ { \alpha }$ is the fluid’s velocity field, then

$$
j _ { e } ^ { \alpha } = \rho _ { e } u ^ { \alpha } .
$$

The local statement of charge conservation is $\partial _ { \alpha } j _ { e } ^ { \alpha } = 0$ .

The spacetime formulation of Maxwell’s equations is

$$
\partial _ { \beta } F ^ { \alpha \beta } = \mu _ { 0 } j _ { e } ^ { \alpha } , \qquad \partial _ { \alpha } F _ { \beta \gamma } + \partial _ { \gamma } F _ { \alpha \beta } + \partial _ { \beta } F _ { \gamma \alpha } = 0 ,
$$

where $\mu _ { 0 }$ is a constant (known as the permeability of vacuum) that determines the units of the theory. It is connected to another constant $\epsilon _ { 0 }$ (known as the permittivity of vacuum, or the dielectric constant) by the relation $\epsilon _ { 0 } \mu _ { 0 } = c ^ { - 2 }$ . The first four equations are known as the inhomogeneous (or sourced) Maxwell equations; the remaining equations are known as the homogeneous (or source-free) Maxwell equations. It is easy to verify, for example, that when $\alpha = 0$ , the first equation returns $\nabla \cdot { \boldsymbol E } = ( c ^ { - 1 } j _ { e } ^ { 0 } ) / \epsilon _ { 0 }$ , which is the usual statement of Gauss’s law. As another example, setting $\alpha = 0$ , $\beta = 1$ , and $\gamma = 2$ in the second equation returns the $z$ -component of $\begin{array} { r } { \partial _ { t } \pmb { B } + \pmb { \nabla } \times \pmb { E } = 0 } \end{array}$ , the usual statement of Faraday’s law.

Note that by antisymmetry of the electromagnetic field tensor, $\partial _ { \alpha \beta } F ^ { \alpha \beta }$ vanishes identically. This implies, together with the inhomogeneous Maxwell equations, that $\partial _ { \alpha } j _ { e } ^ { \alpha }$ is necessarily zero in Maxwell’s theory; charge conservation is automatically enforced.

# 4.3.2 Vector potential

The scalar potential $\Phi$ and the vector potential $\pmb { A }$ of the conventional formulation of electrodynamics can be combined into a spacetime vector $A ^ { \alpha } = ( \Phi / c , A )$ . The electromagnetic field can then be expressed in terms of the potential:

$$
F _ { \alpha \beta } = \partial _ { \alpha } A _ { \beta } - \partial _ { \beta } A _ { \alpha } .
$$

These relations reproduce the familiar $\pmb { { \cal E } } = - \partial _ { t } \pmb { { \cal A } } - \nabla \Phi$ and $\pmb { { \cal B } } = \pmb { { \nabla } } \times \pmb { { \cal A } }$ . Their main virtue is that once $F _ { \alpha \beta }$ is expressed in this way, the homogeneous Maxwell equations are automatically satisfied.

The remaining (inhomogeneous) equations can then be recast as differential equations for the potentials. These, however, cannot be uniquely determined, because Eq. (4.64) is unaffected by a gauge transformation of the form

$$
A _ { \alpha }  A _ { \alpha } + \partial _ { \alpha } \chi ,
$$

in which $\chi$ is any function of the spacetime coordinates $x ^ { \alpha }$ . This gauge freedom can be exploited to simplify the equations to be satisfied by the potentials. A popular and useful choice for the gauge function $\chi$ enforces the Lorenz-gauge condition

$$
\partial _ { \alpha } A ^ { \alpha } = 0 .
$$

With this choice of gauge, the inhomogeneous Maxwell equations are readily shown to take the form of a wave equation for the vector potential:

$$
\begin{array} { r } { \Pi \boldsymbol { A } ^ { \alpha } = - \mu _ { 0 } \boldsymbol { j } _ { e } ^ { \alpha } , } \end{array}
$$

where

$$
\boldsymbol { \Pi } : = \eta ^ { \alpha \beta } \partial _ { \alpha } \partial _ { \beta } = - \frac { 1 } { c ^ { 2 } } \frac { \partial ^ { 2 } } { \partial t ^ { 2 } } + \nabla ^ { 2 }
$$

is the wave operator in Minkowski spacetime. The Lorenz gauge is named after Ludvig Lorenz (1829–1891), a Danish mathematician and physicist. He is often confused with his more famous Dutch colleague Hendrik Lorentz (1853–1928), and in the past the Lorenz gauge was almost universally known as the Lorentz gauge. This, however, is a historical slight that we do not wish to propagate.

Equations (4.67) and (4.68) indicate that the electromagnetic field propagates as a wave, and that the speed of propagation is $c$ , the speed of light. This conclusion is not just an artifact of our choice of gauge: the electromagnetic field tensor itself can be shown to satisfy a wave equation. Simple manipulations starting from Eq. (4.63) do indeed reveal that $F ^ { \alpha \beta }$ must be a solution to $\boxed { 1 } F ^ { \alpha \beta } = - \mu _ { 0 } ( \partial ^ { \alpha } j _ { e } ^ { \beta } - \partial ^ { \beta } j _ { e } ^ { \alpha } )$ .

# 4.3.3 Energy-momentum tensor

The electromagnetic field carries energy and momentum, and it exerts forces (and does work) on a charged fluid. These aspects of Maxwell’s theory are encoded in the field’s

energy-momentum tensor

$$
T ^ { \alpha \beta } = \frac { 1 } { \mu _ { 0 } } \Big ( F ^ { \alpha \mu } F _ { \mu } ^ { \beta } - \frac { 1 } { 4 } \eta ^ { \alpha \beta } F _ { \mu \nu } F ^ { \mu \nu } \Big ) .
$$

In terms of $E$ and $\pmb { B }$ we have that $F _ { \mu \nu } F ^ { \mu \nu } = - 2 ( E ^ { 2 } / c ^ { 2 } - B ^ { 2 } ) , T ^ { 0 0 } = ( E ^ { 2 } / c ^ { 2 } + B ^ { 2 } ) / ( 2 \mu _ { 0 } )$ , $c T ^ { 0 j } = ( { \boldsymbol { E } } \times { \boldsymbol { B } } ) ^ { j } / \mu _ { 0 }$ , and

$$
T ^ { j k } = - \frac { 1 } { \mu _ { 0 } c ^ { 2 } } \Big ( E ^ { j } E ^ { k } - \frac { 1 } { 2 } \delta ^ { j k } E ^ { 2 } \Big ) - \frac { 1 } { \mu _ { 0 } } \Big ( B ^ { j } B ^ { k } - \frac { 1 } { 2 } \delta ^ { j k } B ^ { 2 } \Big ) ,
$$

where we write $E ^ { 2 } : = \boldsymbol { E } \cdot \boldsymbol { E }$ and $B ^ { 2 } : = \pmb { B } \cdot \pmb { B }$ . We recognize in $T ^ { 0 0 }$ the energy density of the electromagnetic field (as measured in the laboratory frame $S$ ), in $c T ^ { 0 j }$ the $j$ -component of the energy flux (also known as the Poynting vector), and $T ^ { j k }$ is the Maxwell stress tensor. To illustrate its meaning we consider a field configuration such that $E = 0$ and $\pmb { B }$ points in the $x$ -direction at some selected position in the laboratory frame. For this configuration $T ^ { x x } = - B ^ { 2 } / ( 2 \mu _ { 0 } )$ , and this represents a tension (negative pressure) along the magnetic field lines. We also have $T ^ { y y } = T ^ { z z } = B ^ { 2 } / ( 2 \mu _ { 0 } )$ , and this represents a pressure in the directions perpendicular to the field lines.

The field’s energy and momentum are not conserved in general, because of the fact (pointed out previously) that the field exerts forces and does work. Straightforward manipulations starting from Eq. (4.69) reveal that

$$
\partial _ { \beta } T ^ { \alpha \beta } = \frac { 1 } { \mu _ { 0 } } \biggl [ - F _ { \mu } ^ { \alpha } \bigl ( \partial _ { \beta } F ^ { \mu \beta } \bigr ) - \frac { 1 } { 2 } F ^ { \mu \nu } \bigl ( \partial ^ { \alpha } F _ { \mu \nu } + \partial _ { \nu } F _ { \mu } ^ { \alpha } + \partial _ { \mu } F _ { \nu } ^ { \alpha } \bigr ) \biggr ] ,
$$

and substitution of Maxwell’s equations (4.63) simplifies this to

$$
\partial _ { \beta } T ^ { \alpha \beta } = - F _ { \mu } ^ { \alpha } j _ { e } ^ { \mu } .
$$

This equation states that there is indeed an exchange of energy and momentum between the field and the charged fluid. The spatial components of the right-hand side of Eq. (4.72) become $- \gamma \rho _ { e } ( { \pmb E } + { \pmb v } \times { \pmb B } )$ when Eq. (4.62) is used and $F ^ { \alpha \beta }$ is expressed in terms of $E$ and $\pmb { B }$ . We recognize this as (minus) the Lorentz-force density acting on a fluid with proper charge density $\rho _ { e }$ and (Newtonian) velocity field $\pmb { v }$ .

The total energy-momentum tensor of the system fluid $^ +$ field includes a contribution $T _ { \mathrm { f i e l d } } ^ { \alpha \beta }$ from the field and a contribution $T _ { \mathrm { f l u i d } } ^ { \alpha \beta }$ from the fluid (as described in Sec. 4.2). The total energy and momentum are conserved when the system is isolated, and we then have

$$
\partial _ { \beta } \big ( T _ { \mathrm { f l u i d } } ^ { \alpha \beta } + T _ { \mathrm { f i e l d } } ^ { \alpha \beta } \big ) = 0 .
$$

This equation gives rise to a charged version of the relativistic Euler equation:

$$
( \rho + \epsilon / c ^ { 2 } + p / c ^ { 2 } ) \frac { d u ^ { \alpha } } { d \tau } = - \big ( \eta ^ { \alpha \beta } + u ^ { \alpha } u ^ { \beta } / c ^ { 2 } \big ) \partial _ { \beta } p + \rho _ { e } F _ { \~ \beta } ^ { \alpha } u ^ { \beta } .
$$

The first term on the right-hand side describes the familiar pressure forces acting within the fluid; the second term represents the electromagnetic forces. The Euler equation is to be supplemented by the mass-conservation equation (4.53), the first law of thermodynamics (4.57), and Maxwell’s equations (4.63).

# 4.4 Point particles in spacetime

Before moving on to general relativity and curved spacetimes, we return briefly to the description of point particles in Minkowski spacetime. Our goal here is to incorporate the point particle within the fluid language developed in the preceding sections.

A point particle can be viewed as a singular distribution of fluid, with non-vanishing mass $m$ (and possibly charge $q$ ) but infinite mass density $\rho$ (and possibly infinite charge density $\rho _ { e }$ ). A point particle has no internal degrees of freedom, and therefore no internal energy density $\epsilon$ and no pressure $p$ . In Newtonian mechanics the particle would move on a trajectory described by $\mathbf { \boldsymbol { x } } = \mathbf { \boldsymbol { r } } ( t )$ . In spacetime it moves on a world line $x ^ { \alpha } = r ^ { \alpha } ( \tau )$ , and its velocity vector is $u ^ { \alpha } = d r ^ { \alpha } / d \tau$ .

In a frame $S ^ { \prime }$ that is momentarily comoving with the particle, the proper mass density $\rho$ can be written as $m \delta _ { 3 } ( { \pmb x } ^ { \prime } - { \pmb r } ^ { \prime } ( t ^ { \prime } ) )$ , in terms of a three-dimensional delta function evaluated on the world line. This expression, however, is not Lorentz invariant, because the delta function, like the volume element $d ^ { 3 } x ^ { \prime }$ , is affected by a Lorentz transformation.

In an effort to replace the three-dimensional delta function with an invariant quantity, we examine the four-dimensional version

$$
\delta \bigl ( x ^ { \mu } - r ^ { \mu } ( \tau ) \bigr ) : = \delta \bigl ( c t - r ^ { 0 } ( \tau ) \bigr ) \delta _ { 3 } \bigl ( x - r ( \tau ) \bigr ) ,
$$

which is a spacetime invariant. Its defining property is that the integral

$$
\int f ( x ^ { \alpha } ) \delta ( x ^ { \mu } - r ^ { \mu } ) d ^ { 4 } x
$$

returns $f ( r ^ { \alpha } )$ if the four-dimensional domain of integration includes the event $r ^ { \alpha }$ , and zero if the domain excludes it; here $f ( x ^ { \alpha } )$ is an arbitrary test function of the spacetime coordinates. The spacetime volume element $d ^ { 4 } x = d ( c t ) d ^ { 3 } x$ is a Lorentz invariant, and this ensures that the delta function itself is a Lorentz invariant.

The four-dimensional delta function is a good starting point to define a proper mass density $\rho$ , but the definition cannot simply be $m \delta ( x ^ { \mu } - r ^ { \mu } )$ . This is wrong for two reasons. First, the delta function has a dimension of inverse length raised to the fourth power, and this would not give rise to the expected dimension of (mass)/(volume) for the mass density. Second, the delta function is “on” for a single moment of time only, when $t = r ^ { 0 } ( \tau ) / c$ ; we would expect instead the mass density to be “on” at all times. The way out of these difficulties is to integrate the four-dimensional delta function with respect to proper time $\tau$ , and to define the particle’s proper mass density as

$$
\rho ( x ^ { \alpha } ) = m c \int \delta \big ( x ^ { \mu } - r ^ { \mu } ( \tau ) \big ) d \tau .
$$

We shall see presently that this is indeed a well-motivated definition. For now we may observe that $\rho$ is dimensionally correct, and that it is constructed entirely from scalar quantities (the rest-mass $m$ , the delta function, and proper time) and operations (the integration over proper time).

To see what Eq. (4.76) implies, it is useful to change the variable of integration from $\tau$ to $r ^ { 0 } ( \tau )$ and to rewrite the integral as

$$
\rho = m c \int { \frac { \delta ( x ^ { 0 } - r ^ { 0 } ) } { u ^ { 0 } } } \delta _ { 3 } ( { \pmb x } - { \pmb r } ) d r ^ { 0 } ,
$$

where $u ^ { 0 } = d r ^ { 0 } / d \tau$ . Integration is immediate, and we find

$$
\rho ( t , \boldsymbol { x } ) = \frac { m c } { u ^ { 0 } } \delta _ { 3 } \big ( \boldsymbol { x } - \boldsymbol { r } ( t ) \big ) ,
$$

where the time $t$ is in principle determined by $t = r ^ { 0 } ( \tau ) / c$ . This expression for the mass density is valid in any Lorentz frame. In the comoving frame $S ^ { \prime }$ of the particle we have that $u ^ { \prime 0 } = c$ , and $\rho$ reduces to $m \delta _ { 3 } ( { \pmb x } ^ { \prime } - { \pmb r } ^ { \prime } )$ , the expected expression. In another frame $S$ , the factor $u ^ { 0 } / c = \gamma$ accounts for the Lorentz contraction of three-dimensional volume elements. We conclude that Eq. (4.76) is indeed a sensible, Lorentz-invariant definition of the proper mass density of a point particle.

The mass current $j ^ { \alpha }$ of a point particle is $\rho u ^ { \alpha }$ , and this can be written either as $( m c u ^ { \alpha } / u ^ { 0 } ) \delta _ { 3 } ( { \pmb x } - { \pmb r } )$ , or more elegantly as

$$
j ^ { \alpha } = m c \int u ^ { \alpha } \delta \bigl ( x ^ { \mu } - r ^ { \mu } ( \tau ) \bigr ) d \tau ,
$$

in which the vector $u ^ { \alpha } ( \tau )$ was inserted within the integral. Similarly, the energy-momentum tensor of a point particle can be shown to be given by

$$
T ^ { \alpha \beta } = m c \int u ^ { \alpha } u ^ { \beta } \delta \bigl ( x ^ { \mu } - r ^ { \mu } ( \tau ) \bigr ) d \tau ,
$$

in which two factors of the velocity vector are inserted within the integral.

A charged particle possesses also a proper charge density $\rho _ { e }$ and a charge current $j _ { e } ^ { \alpha } = \rho _ { e } u ^ { \alpha }$ . These can be expressed as

$$
\rho _ { e } = q c \int \delta { \bigl ( } x ^ { \mu } - r ^ { \mu } ( \tau ) { \bigr ) } d \tau
$$

and

$$
j _ { e } ^ { \alpha } = q c \int u ^ { \alpha } \delta \bigl ( x ^ { \mu } - r ^ { \mu } ( \tau ) \bigr ) d \tau ,
$$

where $q$ is the particle’s electric charge.

To explore the consequences of these results we rely on the distributional identity

$$
u ^ { \alpha } \partial _ { \alpha } \delta \bigl ( x ^ { \mu } - r ^ { \mu } ( \tau ) \bigr ) = - \frac { d } { d \tau } \delta \bigl ( x ^ { \mu } - r ^ { \mu } ( \tau ) \bigr ) ,
$$

which can be established by acting separately on the delta function with the differential operators $u ^ { \alpha } \partial _ { \alpha }$ and $d / d \tau$ , and comparing the results. Using this identity, we find that the conservation statements $\partial _ { \alpha } j ^ { \alpha } = 0 = \partial _ { \alpha } j _ { e } ^ { \alpha }$ follow automatically. For example,

$$
\partial _ { \alpha } j ^ { \alpha } = m c \int u ^ { \alpha } \partial _ { \alpha } \delta ( x ^ { \mu } - r ^ { \mu } ) d \tau = - m c \int { \frac { d } { d \tau } } \delta ( x ^ { \mu } - r ^ { \mu } ) d \tau = 0 .
$$

On the other hand, we have

$$
\begin{array} { c } { { \partial _ { \beta } T ^ { \alpha \beta } = m c \displaystyle \int u ^ { \alpha } u ^ { \beta } \partial _ { \beta } \delta ( x ^ { \mu } - r ^ { \mu } ) d \tau } } \\ { { = - m c \displaystyle \int u ^ { \alpha } \displaystyle \frac { d } { d \tau } \delta ( x ^ { \mu } - r ^ { \mu } ) d \tau , } } \end{array}
$$

and this becomes

$$
\partial _ { \beta } T ^ { \alpha \beta } = m c \int \frac { d u ^ { \alpha } } { d \tau } \delta ( x ^ { \mu } - r ^ { \mu } ) d \tau
$$

after an integration by parts. The energy and momentum of a point particle are conserved when no forces are acting upon it; under these circumstances $\partial _ { \beta } T ^ { \alpha \beta } = 0$ and Eq. (4.86) implies that $d u ^ { \alpha } / d \tau = 0 .$ . In general, however, the energy and momentum are not conserved, $\partial _ { \beta } T ^ { \alpha \beta } \neq 0$ , and the particle is accelerated.

As an example of a non-trivial dynamics, consider a situation in which a point particle carries a charge $q$ and interacts with an electromagnetic field $F ^ { \alpha \beta }$ . The total system is isolated, and in this case we have

$$
\begin{array} { r } { \partial _ { \beta } \big ( T _ { \mathrm { p a r t i c l e } } ^ { \alpha \beta } + T _ { \mathrm { f i e l d } } ^ { \alpha \beta } \big ) = 0 . } \end{array}
$$

We have seen in Eq. (4.72) that $\partial _ { \beta } T _ { \mathrm { f i e l d } } ^ { \alpha \beta } = - F _ { \beta } ^ { \alpha } j _ { e } ^ { \beta }$ , which can be written as

$$
\partial _ { \beta } T _ { \mathrm { f i e l d } } ^ { \alpha \beta } = - q c \int F _ { \beta } ^ { \alpha } ( \tau ) u ^ { \beta } \delta ( x ^ { \mu } - r ^ { \mu } ) d \tau
$$

if we make use of Eq. (4.82); here the field tensor $F _ { \beta } ^ { \alpha }$ was inserted within the integral, where it is evaluated at $x ^ { \alpha } = r ^ { \alpha } ( \tau )$ . Combining this result with Eq. (4.86), we arrive at

$$
m \frac { d u ^ { \alpha } } { d \tau } = q F _ { \beta } ^ { \alpha } u ^ { \beta } .
$$

This is the relativistic expression of the Lorentz-force law. Equation (4.89) becomes $m d ( \gamma \pmb { v } ) / d \tau = q \gamma ( \pmb { E } + \pmb { v } \times \pmb { B } )$ when expressed in a frame $S$ ; the factor of $\gamma$ converts the proper-time derivative to a coordinate-time derivative, and we recover the usual statement of the Lorentz-force equation.

The equations of motion of Eq. (4.89) can also be derived on the basis of an action principle. The action functional of a free particle can be generalized to include an interaction with an electromagnetic field. It is given by

$$
S = - m c ^ { 2 } \int _ { 1 } ^ { 2 } d \tau + q \int _ { 1 } ^ { 2 } A _ { \alpha } d x ^ { \alpha } ,
$$

and it is easy to show – refer to Exercise 4.10 – that the Euler–Lagrange equations derived from $S$ reproduce Eq. (4.89).

# 4.5 Bibliographical notes

Our survey of special relativity and Minkowski spacetime is based on standard presentations found in a number of textbooks, including French (1968) and Rindler (1991), and the introductory texts on general relativity listed in the bibliographical notes of Chapter 5.

The experimental tests of special relativity reviewed in $\mathrm { B o x } ~ 4 . 1$ are described in the following papers. The X-ray tests of the frame-independence of the speed of light are published in Brecher (1977), and the pion experiments were carried out by Alvager ¨ et al. (1964). The time-dilation experiments involving the motion of $\mathrm { H } _ { 2 }$ and $\mathrm { H } _ { 3 }$ molecules are described in Ives and Stilwell (1938), and the lifetime of muons was measured by Rossi and Hall (1941) and Farley et al. (1966). For a survey of classic and modern tests of special relativity and Lorentz invariance, see Will’s (2006a) review, written on the occasion of the centenary of special relativity.

# 4.6 Exercises

4.1 The Lorentz transformation for an arbitrary velocity whose components in $S$ are $v ^ { j }$ is given by

$$
x ^ { \prime \alpha } = \Lambda _ { \beta } ^ { \alpha } x ^ { \beta } ,
$$

where the components of $\Lambda _ { \beta } ^ { \alpha }$ are given by

$$
\begin{array} { r c l } { { } } & { { } } & { { \Lambda _ { 0 } ^ { 0 } = \gamma , } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { \Lambda _ { j } ^ { 0 } = - \gamma v _ { j } / c , } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { \Lambda _ { 0 } ^ { j } = - \gamma v ^ { j } / c , } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { \Lambda _ { k } ^ { j } = \delta _ { k } ^ { j } + ( \gamma - 1 ) n ^ { j } n _ { k } , } } \end{array}
$$

where $n ^ { j } = v ^ { j } / | \pmb { v } |$

(a) Show that this reduces to Eq. (4.1) when $\pmb { v }$ is aligned with the $x$ -direction. (b) By considering the invariance of the interval $d s ^ { 2 }$ , show that the Minkowski metric in $S ^ { \prime }$ is related to the Minkowski metric in $S$ by

$$
\eta _ { \alpha \beta } = \eta _ { \gamma \delta } ^ { \prime } \Lambda _ { \alpha } ^ { \gamma } \Lambda _ { \beta } ^ { \delta } .
$$

(c) Verify using the general Lorentz transformation that $\eta _ { \alpha \beta }$ has the same diagonal form with entries $( - 1 , 1 , 1 , 1 )$ as it had in $S ^ { \prime }$ . You can do this using matrix multiplication by recognizing that the transformation of the metric can be expressed as the matrix equation $\eta = \Lambda ^ { \mathrm { T } } \eta ^ { \prime } \Lambda$ .

4.2 Show that the composition of two Lorentz transformations $\Lambda _ { 1 \beta } ^ { \alpha } \Lambda _ { 2 \gamma } ^ { \beta }$ is also a Lorentz transformation, (a) by verifying that the Minkowski metric $\eta _ { \alpha \beta }$ is unchanged under the combined transformation, and (b) by calculating the combined transformation explicitly for boosts in the $x$ -direction with velocity $v _ { 1 }$ and $v _ { 2 }$ respectively.

4.3 Consider the three events in spacetime described in the inertial frame $S$ by

$$
A : \left( 1 , 1 , 0 , 0 \right) , \quad B : \left( 2 , 3 , 0 , 0 \right) , \quad C : \left( 3 , 2 , 0 , 0 \right) ,
$$

where the notation is $( c t , x , y , z )$ , all in some arbitrary units of length. For each pair of events $A B , A C$ , and $B C$ , determine if the interval is timelike, spacelike, or null. Find the proper distance or time between the events, as appropriate, and find the velocity of a moving frame $S ^ { \prime }$ in which the two events are simultaneous or at the same location, as appropriate.

4.4 Given a particle with momentum $p ^ { \alpha }$ and an observer with velocity $u _ { \mathrm { o b s } } ^ { \alpha }$ , define the vector

$$
V _ { \mathrm { o b s } } ^ { \alpha } = c \frac { P _ { \mathrm { o b s } \beta } ^ { \alpha } p ^ { \beta } } { E _ { \mathrm { o b s } } } ,
$$

where $E _ { \mathrm { o b s } } = - p _ { \alpha } u _ { \mathrm { o b s } } ^ { \alpha }$ and $P _ { \mathrm { o b s } \beta } ^ { \alpha } = \delta _ { \beta } ^ { \alpha } + u _ { \mathrm { o b s } } ^ { \alpha } u _ { \mathrm { o b s } \beta } / c ^ { 2 }$

(a) Show that $V _ { \mathrm { o b s } } ^ { \alpha }$ is a genuine four-dimensional vector, and that it represents the three-dimensional velocity vector $\pmb { v }$ of the particle as measured by the observer.   
(b) Calculate the invariant quantity $\eta _ { \alpha \beta } V _ { \mathrm { o b s } } ^ { \alpha } V _ { \mathrm { o b s } } ^ { \beta }$ , and use it to show that for an observer and particle moving in the $x$ -direction with velocities $v _ { 1 }$ and $v _ { 2 }$ , respectively,

$$
| \vec { V } _ { \mathrm { o b s } } | = \frac { v _ { 2 } - v _ { 1 } } { 1 - v _ { 1 } v _ { 2 } / c ^ { 2 } } .
$$

This is the standard formula for the addition of velocities in special relativity.

4.5 Show that

$$
\eta ^ { \alpha \beta } = - e _ { ( 0 ) } ^ { \alpha } e _ { ( 0 ) } ^ { \beta } + e _ { ( 1 ) } ^ { \alpha } e _ { ( 1 ) } ^ { \beta } + e _ { ( 2 ) } ^ { \alpha } e _ { ( 2 ) } ^ { \beta } + e _ { ( 3 ) } ^ { \alpha } e _ { ( 3 ) } ^ { \beta }
$$

by checking its components (a) in a frame where the basis vectors are attached to a particle at rest, and (b) in a frame where the vectors are attached to a particle moving in the $x$ -direction with velocity $v$ .

4.6 A particle emits radiation isotropically in its own rest frame. As seen from a frame $S ^ { \prime }$ in which the particle moves with a speed $v \approx c$ such that $\gamma \gg 1$ , show that the forward hemisphere of radiation in its rest frame is seen in $S ^ { \prime }$ to be beamed into a forward cone of opening angle $\theta \approx 1 / \gamma$ .

4.7 Three spaceships take off simultaneously from planet Earth, and head for the planet Romulus. An important meeting to discuss the borders of the Neutral Zone is scheduled to begin in exactly 15 years, Earth time. The planets are 12 light years apart. The ships travel according to precise flight plans issued by the dreaded Romulans:

Ship #1, the USS Enterprise, captained by Jean-Luc Picard, travels on a straight line with a uniform speed $0 . 8 c$ for the entire trip.

• Ship #2, the USS Voyager, captained by Kathryn Janeway, travels in a straight line, but with a varying speed, half the time (Earth time) at speed $0 . 7 c$ , and the other half of the time at speed $_ { 0 . 9 c }$ .

Ship #3, captained by the evil Romulan General Maldor, travels at constant speed $_ { 0 . 9 c }$ , arriving early at Romulus, where the General hatches devious plots with his advisors while awaiting the start of the meeting.

Calculate the proper time elapsed between take-off and the start of the meeting according to the clocks carried by each of the three travelers, and point out the significance of the traveller with the largest elapsed proper time. What is the minimum possible proper time between take-off and the start of the meeting?

4.8 Using the general Lorentz transformation of Exercise 4.1, show that the electric and magnetic fields transform according to

$$
\begin{array} { r l } & { \boldsymbol { E } ^ { \prime } = \gamma \boldsymbol { E } + ( 1 - \gamma ) \boldsymbol { n } ( \boldsymbol { n } \cdot \boldsymbol { E } ) + \gamma \boldsymbol { v } \times \boldsymbol { B } , } \\ & { \boldsymbol { B } ^ { \prime } = \gamma \boldsymbol { B } + ( 1 - \gamma ) \boldsymbol { n } ( \boldsymbol { n } \cdot \boldsymbol { B } ) - \gamma \frac { \boldsymbol { v } } { c ^ { 2 } } \times \boldsymbol { E } . } \end{array}
$$

4.9 Using the fact that a coordinate transformation induces a change in the volume element $d ^ { 4 } x$ given by $d ^ { 4 } x ^ { \prime } = J ( x ^ { \prime } , x ) d ^ { 4 } x$ , where $J : = \operatorname* { d e t } ( \partial x ^ { \prime \alpha } / \partial x ^ { \beta } )$ is the Jacobian of the transformation, show that $d ( c t ) d ^ { 3 } x$ is a Lorentz invariant.

4.10 Verify that the Euler–Lagrange equations derived from the action

$$
S = - m c ^ { 2 } \int _ { 1 } ^ { 2 } d \tau + q \int _ { 1 } ^ { 2 } A _ { \alpha } d x ^ { \alpha } ,
$$

yield the relativistic form of the Lorentz-force law.

The relativistic formulation of the laws of physics developed in Chapter 4 excluded gravitation, and our task in this chapter is to complete the story by incorporating this all-important interaction (our personal favorite!). In Sec. 5.1 we explain why relativistic gravitation must be thought of as a theory of curved spacetime. In Sec. 5.2 we develop the elementary aspects of differential geometry that are required in a study of curved spacetime, and in Sec. 5.3 we show how the special-relativistic form of the laws of physics can be generalized to incorporate gravitation in a curved-spacetime formulation. We describe the Einstein field equations in Sec. 5.4, and in Sec. 5.5 we show how to solve them in the restricted context of small deviations from flat spacetime. We conclude in Sec. 5.6 with a description of spherical bodies in hydrostatic equilibrium, featuring the most famous (and historically the first) exact solution to the Einstein field equations; this is the Schwarzschild metric, which describes the vacuum exterior of any spherical distribution of matter (including a black hole).

# 5.1 Gravitation as curved spacetime

# 5.1.1 Principle of equivalence

# Relativistic gravity

The relativistic Euler equation (4.59), unlike its Newtonian version of Eq. (1.23), does not contain a term that describes a gravitational force acting on the fluid. To insert such a term requires an understanding of how the Newtonian theory of gravitation can be generalized to a relativistic setting. It is tempting to attempt such a generalization by simply replacing the Poisson equation $\nabla ^ { 2 } U = - 4 \pi G \rho$ with a Lorentz-invariant generalization such as $\begin{array} { r } { \boxed { \ d \Pi } U = 4 \pi G T _ { \mu } ^ { \mu } / c ^ { 2 } = - 4 \pi G ( \rho + \epsilon / c ^ { 2 } - 3 p / c ^ { 2 } ) } \end{array}$ , and replacing the term $\partial _ { j } U$ in the Newtonian Euler equation by something like $P ^ { \alpha \beta } \partial _ { \beta } U$ . This attempt, however, would be unsuccessful. It would lead to inconsistencies – why, for example, is the gravitational piece of the stress tensor, $\begin{array} { r } { T _ { j k } = ( \partial _ { j } U \partial _ { k } U - \frac { 1 } { 2 } \delta _ { j k } \nabla U \cdot \nabla U ) / ( 4 \pi G ) } \end{array}$ , absent from the right-hand side of the wave equation? And historically, such attempts have led to incorrect empirical consequences, such as no bending of light, or the wrong value for the perihelion advance of Mercury. Similar attempts to formulate a relativistic theory of gravitation based on a vector potential $A ^ { \alpha }$ have also failed.

What about a tensor theory? Our experience with Minkowski spacetime has revealed the important role of a tensor – the Minkowski metric $\eta _ { \alpha \beta }$ . In Minkowski spacetime, however, $\eta _ { \alpha \beta }$ is a rather inert, somewhat boring object, merely providing the fixed arena in which special relativistic dynamics takes place. But if we open our minds to the possibility that $\eta _ { \alpha \beta }$ could be an approximation to something more general – a spacetime metric $g _ { \alpha \beta }$ – that could itself participate in the dynamics, then the possibility of a tensor theory of gravity emerges. We will therefore follow Einstein and argue in favor of a connection between gravitation and the curvature of spacetime.

# Principles of equivalence

The key observation that leads to this connection is known as the principle of equivalence, which we state as:

If a test body is placed at an initial event in spacetime and given an initial velocity there, and if the body subsequently moves freely, then its world line will be independent of its mass, internal structure, and composition.

Here, a “test body” is one that does not modify the gravitational field created by other (non-test) bodies, and a “freely-moving” body is one on which no forces are acting, except for the gravitational force; the test body, for example, is not allowed to possess an electric charge when an electromagnetic field is present. The principle of equivalence states that all test bodies move with the same acceleration in a gravitational field, irrespective of their mass or internal composition. This statement is known more precisely as the “weak equivalence principle,” and in Newtonian theory it holds as a consequence of the equality between inertial mass and passive gravitational mass. This property is only accidental in Newtonian theory; it is a foundational axiom of relativistic gravitation. As we discussed in Box 1.1, there is ample, high-precision experimental support for the weak equivalence principle.

A stronger formulation of the principle of equivalence, known as “Einstein’s equivalence principle,” states that the weak version holds, and that, in addition:

The outcome of any local, non-gravitational test experiment performed by a freely-moving apparatus is independent of the velocity of the apparatus and independent of when and where the experiment is carried out.

Here, a “local, non-gravitational test experiment” is any measurement that does not probe gravitational effects directly; this could be, for example, a measurement of the fine-structure constant, or a measurement of the critical temperature in a phase transition to a Bose– Einstein condensate. The measuring apparatus is assumed to be moving freely, in the sense provided previously: no forces other than gravity are acting on the apparatus.

An even stronger statement of the principle of equivalence, known as the “strong equivalence principle,” states that the weak version holds even when the body is self-gravitating, and that the Einstein version holds even when local test experiments are allowed to probe gravitational effects. As we shall see, the Einstein equivalence principle implies that gravitation must be a manifestation of the curvature of spacetime, and that relativistic gravity must be formulated as a metric theory. The strong equivalence principle, however, is not valid for all metric theories of gravitation, but it is satisfied in Einstein’s theory. We will see the strong equivalence principle in action in later chapters, particularly in Chapter 9, and will witness its failure when we turn to alternative theories of gravity in Chapter 13.

An important aspect of the principles of equivalence, which we have not yet stated, is that the spatial dimensions of the test body and the spatial dimensions of the freely-moving apparatus must be small compared with the length scale over which the gravitational field varies. The test body and the apparatus must not be allowed to probe the inhomogeneities of the gravitational field. Thus, all statements made with regard to the principles of equivalence are local in nature. With this important restriction in place, a succinct summary of the Einstein equivalence principle is:

No measurement carried out in a suitably small laboratory moving freely in a gravitational field can reveal the existence of gravity locally, within the confines of the laboratory.

If all objects within the laboratory fall with the same acceleration, then all local measurements reveal a vanishing acceleration relative to a standard, freely-moving object, and no local measurement can reveal the presence of a gravitational field. In other words, all local aspects of gravity can be turned off by doing physics in a freely-moving frame of reference.

This statement is powerful. It implies, in particular, that the special-relativistic formulation of the laws of physics continues to hold locally in the freely-moving frames; gravity is not present in these frames, and there is no need to modify the laws of physics to account for it. And it follows that the inertial frames of special relativity must be identified with the freely-moving frames of observers in a gravitational field. In the old Newtonian language we would say that a freely-moving observer is accelerated (relative, say, to an observer at rest on the surface of the Earth), and that his reference frame is not inertial. In the new relativistic language we say instead that it is the freely-moving observer who is inertial, while the observer at rest on Earth is not; the freely-moving observer is not accelerated, while the observer at rest on the ground is. In everyday life we tend not to think in this way, but consider the following comparison: A person stands still in a long line for two hours waiting for admission to a rock concert, while an astronaut on the International Space Station works for two hours installing some equipment; which person ends up with sore feet? In relativistic gravitation, acceleration measures a departure from free motion produced by non-gravitational forces. A freely-moving observer is unaccelerated, and his reference frame is inertial.

# The tale of Cliff and Eric

As we can now appreciate, all local aspects of gravitation are purely relative, and they can be turned off by adopting a freely-moving frame of reference. But as we shall now discuss, aspects of gravitation that probe inhomogeneities of the gravitational field are absolute; these can never be turned off.

Consider two remote observers in outer space, falling freely toward Earth. The first observer – let’s call him Cliff – performs local measurements in his spacecraft, and infers the complete absence of gravity in his immediate vicinity. The second observer – Eric – also infers, on the basis of local measurements, the local absence of gravity. Cliff and Eric are both inertial observers (in the relativistic sense described previously). Their reference frames are distinct, however, and they are in fact accelerated with respect to each other. This relative acceleration is revealed by the fact that as Cliff and Eric both fall toward Earth, their spacecraft are slowly converging toward each other. The relative acceleration is caused by inhomogeneities in the gravitational field: the gravitational force is pulling the spacecraft in different directions. Cliff and Eric must agree that while gravity is absent locally, an interaction must be responsible for the relative acceleration of their inertial frames. This is gravity; absolute gravity is inhomogeneous gravity.

It is instructive to provide a mathematical description of the tale of Cliff and Eric. Cliff ’s trajectory toward Earth is described by $r _ { \mathrm { C } } ( t )$ , and this is a solution to

$$
\frac { d ^ { 2 } { \pmb r } _ { \mathrm { C } } } { d t ^ { 2 } } = { \pmb g } ( { \pmb r } _ { \mathrm { C } } ) ,
$$

in which the (Newtonian, as opposed to relativistic) gravitational acceleration $\mathbf { \Delta } _ { \mathbf { \mathbf { \vec { g } } } } = \nabla U$ is evaluated at Cliff’s position. Assuming that the spacecraft is sufficiently small that variations in ${ \pmb g } ( { \pmb x } )$ are negligible within it, all objects in Cliff ’s spacecraft move with this acceleration. Suppose that a selected object is at a position $r _ { \mathrm { C } } + \xi _ { \mathrm { C } }$ within the spacecraft, where $\pmb { \xi } _ { \mathrm { C } }$ is the object’s position relative to Cliff. Then $\pmb { \xi } _ { \mathrm { C } } ( t )$ is a solution to $d ^ { 2 } \pmb { \xi } _ { \mathrm { C } } / d t ^ { 2 } =$ $\pmb { g } ( \pmb { r } _ { \mathrm { C } } + \pmb { \xi } _ { \mathrm { C } } ) - \pmb { g } ( \pmb { r } _ { \mathrm { C } } ) \simeq \mathbf { 0 }$ . Relative to Cliff, the object moves on a straight line with a uniform velocity, and Cliff sees no local manifestation of gravity.

On the other hand, Eric’s trajectory toward Earth is described by $r _ { \mathrm { E } } ( t )$ , a solution to

$$
\frac { d ^ { 2 } { \pmb r } _ { \mathrm { E } } } { d t ^ { 2 } } = { \pmb g } ( { \pmb r } _ { \mathrm { E } } ) ,
$$

in which $\pmb { g }$ is now evaluated at Eric’s position. Assuming that Eric’s spacecraft is sufficiently small, all objects within it move with this acceleration, and a selected object at a relative position $\pmb { \xi } _ { \mathrm { E } }$ moves on a straight line with a constant relative velocity $d \pmb { \xi } _ { \mathrm { E } } / d t$ . Eric also sees no local manifestation of gravity.

Let now $\pmb { \xi } _ { \mathrm { E C } } ( t ) : = \pmb { r } _ { \mathrm { E } } ( t ) - \pmb { r } _ { \mathrm { C } } ( t )$ be Eric’s position relative to Cliff. This is a solution to

$$
\frac { d ^ { 2 } \pmb { \xi } _ { \mathrm { E C } } } { d t ^ { 2 } } = \pmb { g } ( \pmb { r } _ { \mathrm { E } } ) - \pmb { g } ( \pmb { r } _ { \mathrm { C } } ) ,
$$

and because the displacement is now large, the right-hand side of this equation can no longer be approximated by zero. The gravitational accelerations at Eric’s and Cliff ’s positions are different, and we can express this difference by means of a Taylor expansion:

$$
g _ { j } ( \pmb { r } _ { \mathrm { E } } ) = g _ { j } ( \pmb { r } _ { \mathrm { C } } + \pmb { \xi } _ { \mathrm { E C } } ) = g _ { j } ( \pmb { r } _ { \mathrm { C } } ) + \xi _ { \mathrm { E C } } ^ { k } \partial _ { k } g _ { j } ( \pmb { r } _ { \mathrm { C } } ) + \cdots .
$$

Combining this with $g _ { j } = \partial _ { j } U$ , we arrive at

$$
\frac { d ^ { 2 } \xi _ { \mathrm { E C } } ^ { j } } { d t ^ { 2 } } = { \left( \partial _ { j k } U \right) } \xi _ { \mathrm { E C } } ^ { k } ,
$$

where the Newtonian potential $U ( { \pmb x } )$ is evaluated at $x = r _ { \mathrm { C } } ( t )$ after differentiation, and where we have neglected quadratic and higher-order terms in the Taylor expansion of $g _ { j }$ . The left-hand side of the equation gives the relative acceleration between Cliff and Eric, and the right-hand side measures the inhomogeneities of the gravitational field, the failure of $\pmb { g }$ to be a constant vector field. It is this failure that gives rise to the relative acceleration, and it is the homogeneities in $\pmb { g }$ that produce an absolute manifestation of the gravitational interaction. The tidal distortions of the Earth by the Moon and the Sun are caused by precisely these relative accelerations, and so one frequently hears the statement that absolute gravity is tidal gravity.

We should be more honest and point out that even within Cliff’s frame or Eric’s frame, an object does not move precisely on a straight line. Had we expanded the acceleration of the object, $g ( r _ { \mathrm { C } } + \xi _ { \mathrm { C } } )$ , to higher order in $\pmb { \xi } _ { \mathrm { C } }$ , we would have discovered that its acceleration relative to Cliff is actually given by

$$
\frac { d ^ { 2 } \xi _ { \mathrm { C } } ^ { j } } { d t ^ { 2 } } = { \left( \partial _ { j k } U \right) } \xi _ { \mathrm { C } } ^ { k } .
$$

So the inhomogeneity of the gravitational field can manifest itself even within Cliff’s or Eric’s freely-moving frame. This is why we insist that the frame be local in order to apply the Einstein equivalence principle: It must be small enough that the effects of the relative acceleration described by Eq. (5.6) are negligible.

<table><tr><td>Box 5.1</td><td>Uniform gravitational fields</td></tr><tr><td></td><td>The principles of equivalence enunciated above are not what Einstein first named the principle of equiva- lence.Einstein&#x27;s original formulation stated that physics in astaticanduniform gravitationalfield is equivalent to physics without gravity inauniformly accelerated frame ofreference.This formulationplayedan essential role in guiding him toward general relativity.By considering the propagation ofa light ray in an accelerating frame, and equating thattoits behavior inauniform gravitationalfield,he was led to the gravitational redshift efect in 1907 (his &quot;happiest thought&quot; as he later recounted) and to the deflection oflight in 1911.These insights then led him to consider gravity as being linked to the geometry of curved spacetime, which was the critical step he needed to develop the full theory.</td></tr></table>

But his formulation is deeply flawed when taken literally. First, a uniform gravitational field does not exist in nature; in Newtonian gravity it would require as a source an infinite plane of matter in an otherwise empty universe. Second, static fields do not exist in the real world: stars rotate, planets orbit, supernovae explode, the universe expands. Third, the strict adoption of his principle has led to a pointless literature of apparent paradoxes, debates, and conundra.

The bottom line is that a uniform gravitational field is not a gravitational field at all. It is the “field” experienced by an observer undergoing constant acceleration in Minkowski spacetime, and nothing else. (See Misner, Thorne, and Wheeler’s Gravitation or other books for a mathematical discussion of the accelerating frame, sometimes called a Rindler spacetime after Wolfgang Rindler, who elucidated many of its properties. See also Exercise 5.1.) From our point of view, it is not a gravitational field precisely because it is uniform. It possesses no inhomogeneities, and therefore is not gravity. Einstein’s original formulation is not an equivalence, but a tautology.

It is possible, however, to restore respectability to Einstein’s original version of the equivalence principle: simply insert the adjective “local” in suitable places. Any gravitational field is approximately uniform in a local region, and therefore Einstein’s insights work equally well in a locally uniform field. But the use of “local” now permits the gravitational field to be a truly physical, inhomogeneous field on larger scales.

# 5.1.2 Metric theory of gravitation

As we have seen in the preceding subsection, the adoption of Einstein’s equivalence principle produces a number of powerful statements. These include:

• gravity couples universally to matter, in a manner that is independent of mass, structure, and composition of small bodies;   
• all local aspects of gravity are eliminated in freely-moving frames;   
• freely-moving frames are inertial frames, and all special-relativistic formulations of the laws of physics continue to hold in freely-moving frames; freely-moving frames are unaccelerated; acceleration measures departures from free motion produced by non-gravitational forces;   
• freely-moving frames extend over small regions only, and inhomogeneities in the gravitational field prevent their extension beyond these small regions;   
• absolute aspects of gravity are revealed in the field inhomogeneities, which forbid a smooth meshing of inertial frames that are widely separated.

The first four statements imply that there must exist a tensor field in spacetime that couples universally to all forms of matter and reduces, in each local inertial frame attached to a freely-moving observer, to the Minkowski metric $\eta _ { \mu \nu }$ of special relativity. This tensor field is denoted $g _ { \alpha \beta }$ and named the metric tensor of the (now curved) spacetime. A relativistic theory of gravity shall be a theory of a dynamical metric tensor in spacetime. The last two statements imply that while the spacetime metric $g _ { \alpha \beta }$ can be reduced locally to the Minkowski metric $\eta _ { \mu \nu }$ , it must differ from it in its global aspects.

Suppose that $\xi ^ { \mu }$ is a local Lorentzian coordinate system that covers a small inertial frame $S$ attached to a freely-moving observer in a gravitational field. In these coordinates, the spacetime interval between two neighboring events within $S$ is given by $d s ^ { 2 } = \eta _ { \mu \nu } d \xi ^ { \mu } d \xi ^ { \nu }$ . The local coordinates $\xi ^ { \mu }$ are related to a global coordinate system $x ^ { \alpha }$ that covers a portion of spacetime that is much larger than the small neighborhood of the inertial observer. These global coordinates are a priori arbitrary, merely providing labels to spacetime events, and they will not be Lorentzian in the presence of field inhomogeneities. The relation can be expressed as $\xi ^ { \mu } = f ^ { \mu } ( x ^ { \alpha } )$ , where $f ^ { \mu }$ are functions of the global coordinates. By differentiation we have $d \xi ^ { \mu } = ( \partial _ { \alpha } f ^ { \mu } ) d x ^ { \alpha }$ , and the spacetime interval can be expressed as $d s ^ { 2 } = ( \eta _ { \mu \nu } \partial _ { \alpha } f ^ { \mu } \partial _ { \beta } f ^ { \nu } ) d x ^ { \alpha } d x ^ { \beta }$ in terms of the global coordinates. The quantity within brackets converts a coordinate increment $d x ^ { \alpha }$ to the spacetime interval $d s ^ { 2 }$ , which is absolute, independent of the choice of reference frame and coordinate system. This conversion is precisely the role of a metric tensor, and we conclude that the spacetime interval is given by

$$
d s ^ { 2 } = g _ { \alpha \beta } d x ^ { \alpha } d x ^ { \beta }
$$

in the global coordinate system. This defines $g _ { \alpha \beta }$ , and the association $g _ { \alpha \beta } = \eta _ { \mu \nu } \partial _ { \alpha } f ^ { \mu } \partial _ { \beta } f ^ { \nu }$ is the statement that, locally, the spacetime metric can be obtained from the Minkowski metric by a transformation from local coordinates $\xi ^ { \mu }$ attached to an inertial frame to the global coordinates $x ^ { \alpha }$ . As we shall see in Sec. 5.2.5, the reverse statement is also true: It is always possible to reduce the global metric $g _ { \alpha \beta }$ to a local Minkowski form by implementing a coordinate transformation $x ^ { \alpha } = F ^ { \alpha } ( \xi ^ { \mu } )$ from the global coordinates $x ^ { \alpha }$ to the local Lorentzian coordinates $\xi ^ { \mu }$ .

# 5.1.3 Newtonian gravity as warped time

The connection between gravitation and curved spacetime can be revealed vividly through the following argument, which is limited in scope to Newtonian situations – weak fields and slow motions. We begin with a thought experiment.

Suppose that a particle of mass $m$ is initially at rest at a position $x _ { 0 }$ in a gravitational field. Its total energy is initially equal to $m c ^ { 2 }$ . The particle is released, and it falls freely toward a new position $_ x$ . In the course of its motion the particle acquires a kinetic energy $\scriptstyle { \frac { 1 } { 2 } } m v ^ { 2 }$ , which is equal to the difference between the gravitational potential energies at the initial and final positions: ${ \scriptstyle { \frac { 1 } { 2 } } } m v ^ { 2 } = m U ( { \pmb x } ) - m U ( { \pmb x } _ { 0 } )$ . Its total energy becomes $m c ^ { 2 } [ 1 + U ( \mathbf { x } ) / c ^ { 2 } -$ $U ( x _ { 0 } ) / c ^ { 2 } ]$ . In this Newtonian context, $v$ is small compared with $c$ , and $U / c ^ { 2 } \ll 1$ .

At this stage of the experiment, all of the particle’s energy is converted into a photon of energy $\hbar \omega ( \mathbf { x } ) = m c ^ { 2 } [ 1 + U ( \mathbf { x } ) / c ^ { 2 } - U ( \mathbf { x } _ { 0 } ) / c ^ { 2 } ]$ . The photon climbs back toward $x _ { 0 }$ , and it arrives there with an energy $\hbar \omega ( \pmb { x } _ { 0 } )$ . In the final step of the experiment, the photon is converted into a particle that will remain at rest at $x _ { 0 }$ ; its mass $m ^ { \prime }$ is such that $m ^ { \prime } c ^ { 2 } = \hbar \omega ( { \pmb x } _ { 0 } )$ .

Energy conservation demands that $m ^ { \prime } = m$ ; a different outcome would imply that energy has been created or lost in a cyclic process that could be repeated any number of times. The photon must therefore lose energy to the gravitational field as it makes its way from $_ { x }$ to $\scriptstyle x _ { 0 }$ , and we set $\hbar \omega ( { \boldsymbol { x } } _ { 0 } ) = m c ^ { 2 }$ . These results imply that

$$
\frac { \omega ( x ) } { \omega ( x _ { 0 } ) } = 1 + U ( { \bf x } ) / c ^ { 2 } - U ( x _ { 0 } ) / c ^ { 2 } .
$$

This simplifies when $x _ { 0 }$ is taken to be at infinity, where $U ( { \pmb x } _ { 0 } ) = 0$ . We have then Einstein’s redshift formula,

$$
\frac { \omega ( \mathbf { x } ) } { \omega _ { \infty } } = 1 + U ( \mathbf { x } ) / c ^ { 2 } .
$$

As a photon climbs out of a gravitational field, it loses energy, and its frequency decreases, so that $\omega _ { \infty } / \omega ( \pmb { x } ) \approx 1 - U ( \pmb { x } ) / c ^ { 2 } < 1$ . The photon’s wavelength increases, and its color is shifted toward the red end of the spectrum.

We next turn this thought experiment, and the redshift formula, into a conclusion about the very structure of spacetime in the presence of gravitation. We take the bold point of view that the frequency shift described by Eq. (5.9) is a manifestation of the fact that time flows at a rate that depends on position within a gravitational field. And we describe this phenomenon mathematically by the equation

$$
\frac { d t ( x ) } { d t _ { \infty } } = 1 - U ( { \bf x } ) / c ^ { 2 } ,
$$

which is obtained from the redshift formula by letting $\omega ( { \pmb x } ) / \omega _ { \infty } \equiv d t _ { \infty } / d t ( { \pmb x } )$ . Here $d t ( \boldsymbol { x } )$ i s the increment of time between a given number of oscillations of the photon’s electromagnetic wave, as measured by a static observer at position $_ x$ in the gravitational field (this observer is not moving freely, and therefore not inertial), while $d t _ { \infty }$ is the increment of time between the same number of oscillations as measured by a static observer at infinity (because there is no gravity there, this observer is inertial). The fact that $d t ( \pmb { x } ) \neq d t _ { \infty }$ implies that the spacetime metric at position $_ x$ cannot be equal to the Minkowski metric. If it were, then $d s ^ { 2 } = - d ( c t ) ^ { 2 } + d x ^ { 2 } + d y ^ { 2 } + d z ^ { 2 }$ and a measurement of proper time by a static observer at $\boldsymbol { x }$ would be equal to $\sqrt { - d s ^ { 2 } } / c = d t \equiv d t _ { \infty }$ , in contradiction with Eq. (5.10). We must have, instead,

$$
d s ^ { 2 } = g _ { 0 0 } d ( c t ) ^ { 2 } + d x ^ { 2 } + d y ^ { 2 } + d z ^ { 2 } ,
$$

so that a measurement of proper time now gives $\sqrt { - g _ { 0 0 } } d t$ . If we identify this with $d t ( \boldsymbol { x } )$ and use Eq. (5.10), we conclude that $\sqrt { - g _ { 0 0 } } = 1 - U ( { \bf { x } } ) / c ^ { 2 }$ .

The metric associated with a Newtonian gravitational field is therefore given approximately by

$$
d s ^ { 2 } = - \big [ 1 - 2 U ( x ) / c ^ { 2 } \big ] d ( c t ) ^ { 2 } + d x ^ { 2 } + d y ^ { 2 } + d z ^ { 2 } .
$$

This assignment encodes the fact that time flows at a rate that depends on position within a gravitational field, a postulated physical phenomenon that naturally explains the redshift of photons. We call attention to the fact that in Eq. (5.12), $d t \equiv d t _ { \infty }$ represents the increment of time as measured by an observer at rest at infinity, where $U = 0$ .

The metric of Eq. (5.12) does more than just explain the gravitational redshift of light. It also produces all phenomena associated with Newtonian gravity. To prove this point it will suffice to examine the motion of a test body in a spacetime with this metric.

As we saw back in Chapter 4, the free motion of a test body in Minkowski spacetime is determined by the vanishing of its acceleration, $\boldsymbol { a } ^ { \alpha } = 0$ , or equivalently by the extremum of its action $S : = - m c ^ { 2 } \int d \tau = \int L d t$ , with associated Lagrangian

$$
L = - m c \sqrt { - \eta _ { \alpha \beta } \frac { d r ^ { \alpha } } { d t } \frac { d r ^ { \beta } } { d t } } .
$$

But if we now use the metric of Eq. (5.12) instead of the Minkowski metric, we find that the Lagrangian becomes

$$
L = - m c ^ { 2 } \sqrt { 1 - 2 U / c ^ { 2 } - v ^ { 2 } / c ^ { 2 } } ,
$$

with $\scriptstyle v ^ { 2 } : = v \cdot v$ and ${ \pmb v } = d { \pmb r } / d t$ . Expanding this to first order in the small quantities $( v / c ) ^ { 2 }$ and $U / c ^ { 2 }$ , the Lagrangian simplifies to

$$
L = - m c ^ { 2 } + { \frac { 1 } { 2 } } m v ^ { 2 } + m U .
$$

The first term is an irrelevant constant, the second term is the body’s kinetic energy, and the third term is the gravitational potential energy. Substitution of this Lagrangian into the Euler–Lagrange equations gives rise to the familiar equations of motion of Newtonian gravity: $d ^ { 2 } \boldsymbol { r } / d t ^ { 2 } = \boldsymbol { \nabla } U$ , in which $U$ is evaluated at $\mathbf { \boldsymbol { x } } = \mathbf { \boldsymbol { r } } ( t )$ after differentiation. Newtonian gravity, therefore, is a manifestation of the fact that time flows at a rate that depends on position within a gravitational field.

# 5.2 Mathematics of curved spacetime

# 5.2.1 Metric

The lesson of the Einstein equivalence principle is that we must move from flat spacetime to curved spacetime to incorporate gravity into the laws of relativistic physics. Accordingly we must replace the Minkowski metric $\eta _ { \alpha \beta }$ with a more general metric tensor $g _ { \alpha \beta }$ . This tensor is still symmetric under an exchange of its indices, but it is no longer diagonal; in general it possesses ten independent components, which are all functions of the spacetime coordinates $x ^ { \alpha }$ . The metric plays the same role as in Minkowski spacetime: it converts coordinate displacements $d x ^ { \alpha }$ , which evidently depend on the choice of coordinates, to an invariant spacetime interval $d s ^ { 2 }$ . The formula is

$$
d s ^ { 2 } = g _ { \alpha \beta } d x ^ { \alpha } d x ^ { \beta } .
$$

The metric therefore achieves two purposes: it encodes geometrical information about the coordinate system, and it encodes physical information about the gravitational field. It is usually not easy to distinguish between these different aspects of the metric.

Under a change of coordinates described by $x ^ { \alpha } = f ^ { \alpha } ( x ^ { \prime \mu } )$ , where $f ^ { \alpha }$ are functions of the new coordinates $x ^ { \prime \mu }$ , the coordinate displacements change according to

$$
d x ^ { \alpha } = { \frac { \partial f ^ { \alpha } } { \partial x ^ { \prime \mu } } } d x ^ { \prime \mu }
$$

and the spacetime interval becomes

$$
d s ^ { 2 } = g _ { \alpha \beta } { \frac { \partial f ^ { \alpha } } { \partial x ^ { \prime \mu } } } { \frac { \partial f ^ { \beta } } { \partial x ^ { \prime \nu } } } d x ^ { \prime \mu } d x ^ { \prime \nu } .
$$

This expression shows that the metric is replaced by

$$
g _ { \mu \nu } ^ { \prime } = g _ { \alpha \beta } \frac { \partial f ^ { \alpha } } { \partial x ^ { \prime \mu } } \frac { \partial f ^ { \beta } } { \partial x ^ { \prime \nu } }
$$

in the new coordinate system, so that $d s ^ { 2 } = g _ { \mu \nu } ^ { \prime } d x ^ { \prime \mu } d x ^ { \prime \nu }$ . The coordinate displacements change, and the metric also changes, but $d \boldsymbol { s } ^ { 2 }$ remains the same during a coordinate transformation.

The coordinate systems considered here are completely general, and the transformations between them are not limited to linear transformations, as they were for Lorentz transformations. It would not do to restrict our attention to Lorentzian coordinates, because although these can always be installed locally in an inertial frame attached to a freely-moving observer, in general they cannot be extended globally to cover a large portion of the spacetime; and a system of locally Lorentzian coordinates installed in one inertial frame would not mesh smoothly with another system installed in another inertial frame. In this new setting, therefore, vectors (such as $d x ^ { \alpha }$ ) and tensors (such as $g _ { \alpha \beta }$ ) must be allowed to transform under a completely general class of coordinate transformations.

The metric $g _ { \alpha \beta }$ is still used to define the inner product between two vectors. If $A ^ { \alpha }$ and $B ^ { \alpha }$ are vectors in a curved spacetime (so that they transform like $d x ^ { \alpha }$ under a general coordinate transformation), then their inner product is defined to be $g _ { \alpha \beta } A ^ { \alpha } B ^ { \beta }$ . It is easy to show that the inner product is invariant under a general coordinate transformation; the changes in the vectors are compensated for by the changes in the metric tensor.

We still use the metric to lower indices on vectors. Given a vector $A ^ { \alpha }$ , we define its dual $A _ { \alpha }$ by

$$
A _ { \alpha } : = g _ { \alpha \beta } A ^ { \beta } .
$$

It is important to appreciate that in curved spacetime, this operation involves more than a mere change of sign; in general the functions $A _ { \alpha }$ will be very different from $A ^ { \alpha }$ . The raising operation can also be defined, if we first introduce the inverse metric $g ^ { \alpha \beta }$ . This is the inverse to the matrix formed by all the components of the metric $g _ { \alpha \beta }$ ; its defining relation is

$$
g ^ { \alpha \gamma } g _ { \gamma \beta } = \delta _ { \beta } ^ { \alpha } ,
$$

which is equivalent to the matrix equation $g ^ { - 1 } g = 1$ . If $A _ { \alpha }$ is a dual vector, then

$$
A ^ { \alpha } : = g ^ { \alpha \beta } A _ { \beta }
$$

is its associated vector.

# 5.2.2 Tensor calculus

# Vectors and components

In flat spacetime the preferred coordinate systems are Lorentzian, and those are characterized by straight coordinate lines. The basis vectors associated with these coordinate systems are constant, and under these conditions there is no need to distinguish between the derivative of a vector and the derivative of its components. In a curved spacetime the situation is very different: the coordinate lines are no longer straight, the basis vectors change in length and direction from place to place, and these changes produce an important distinction between the derivative of a vector and that of its components. (This situation is not limited to curved spacetimes. It is familiar also in three-dimensional flat space, when we choose to work in curvilinear coordinates instead of Cartesian coordinates.)

As we develop this idea we shall have to distinguish carefully between a geometric vector $\vec { A }$ and its components $A ^ { \alpha }$ in a selected coordinate system $x ^ { \alpha }$ . While the components change under a coordinate transformation, the geometric vector (which would be represented as an arrow in familiar vector calculus) does not. A geometric vector is related to its components via a set of basis vectors $\vec { e } _ { \alpha }$ that also depend on the coordinate system. These are defined so that the vector $d \vec { x }$ that describes an infinitesimal displacement from one event in spacetime to another is given by

$$
d \vec { x } = \vec { e } _ { \alpha } d x ^ { \alpha } ,
$$

in terms of the basis vectors and the coordinate displacements. An equivalent way of stating this is that $\vec { e } _ { \alpha } = \partial \vec { x } / \partial x ^ { \alpha }$ . An arbitrary vector $\vec { A }$ can then be expressed as

$$
\vec { A } = A ^ { \alpha } \vec { e } _ { \alpha }
$$

in terms of the basis vectors and its components $A ^ { \alpha }$ .

The inner product between $d \vec { x }$ and itself is the spacetime invariant $d s ^ { 2 }$ . We have $d s ^ { 2 } = { }$ $d \vec { x } \cdot d \vec { x } = ( \vec { e } _ { \alpha } \cdot \vec { e } _ { \beta } ) d x ^ { \alpha } d x ^ { \beta }$ , and comparing this with Eq. (5.16) reveals that

$$
g _ { \alpha \beta } = \vec { e } _ { \alpha } \cdot \vec { e } _ { \beta } ;
$$

the metric can be obtained by computing the inner products between all pairs of basis vectors. From this it follows that if $\vec { A } = A ^ { \alpha } \vec { e } _ { \alpha }$ and $\vec { B } = B ^ { \beta } \vec { e } _ { \beta }$ are vectors, then their inner product is $\vec { A } \cdot \vec { B } = A ^ { \alpha } B ^ { \beta } ( \vec { e } _ { \alpha } \cdot \vec { e } _ { \beta } ) = g _ { \alpha \beta } A ^ { \alpha } B ^ { \beta }$ , as expected.

# Covariant differentiation of vectors

Suppose now that $\vec { A }$ is a vector field in spacetime. Its derivative with respect to coordinate $x ^ { \beta }$ is

$$
\partial _ { \beta } { \vec { A } } = ( \partial _ { \beta } A ^ { \alpha } ) { \vec { e } } _ { \alpha } + A ^ { \alpha } ( \partial _ { \beta } { \vec { e } } _ { \alpha } ) ,
$$

in which the first term accounts for the variation of the components, while the second accounts for the variation of the basis vectors. We write

$$
\partial _ { \beta } \vec { e } _ { \alpha } = \Gamma _ { \alpha \beta } ^ { \mu } \vec { e } _ { \mu } ,
$$

which states the obvious fact that a change in basis vector induced by a coordinate displacement is itself a vector that can be decomposed in terms of basis vectors. Equation (5.27) provides a definition for the quantities $\Gamma _ { \alpha \beta } ^ { \mu }$ , which are known as Christoffel symbols. Because $\partial _ { \beta } { \vec { e } } _ { \alpha } = \partial ^ { 2 } { \vec { x } } / \partial x ^ { \alpha } \partial x ^ { \beta } = \partial _ { \alpha } { \vec { e } } _ { \beta }$ , we have that

$$
\Gamma _ { \beta \alpha } ^ { \mu } = \Gamma _ { \alpha \beta } ^ { \mu } ;
$$

the Christoffel symbols are symmetric in their lower indices.

With Eq. (5.27) our previous expression for $\partial _ { \beta } \vec { A }$ becomes $\partial _ { \beta } \vec { A } = ( \nabla _ { \beta } A ^ { \mu } ) \vec { e } _ { \mu }$ , where

$$
\nabla _ { \beta } A ^ { \mu } : = \partial _ { \beta } A ^ { \mu } + \Gamma _ { \alpha \beta } ^ { \mu } A ^ { \alpha }
$$

is known as the covariant derivative of the vector components $A ^ { \mu }$ . The covariant derivative accounts for the changes in the components as well as the changes in the basis vectors as the vector field is moved from one event in spacetime to the next. Note the distinction between the covariant derivative of a component, symbolized by $\nabla _ { \beta }$ , and the partial derivative, symbolized by $\partial _ { \beta }$ .

The Christoffel symbols can be expressed neatly in terms of the metric. To produce this expression we differentiate the relation $g _ { \alpha \beta } = \vec { e } _ { \alpha } \cdot \vec { e } _ { \beta }$ with respect to $x ^ { \gamma }$ and substitute Eq. (5.27); this yields

$$
\partial _ { \gamma } g _ { \alpha \beta } = g _ { \alpha \mu } \Gamma _ { \beta \gamma } ^ { \mu } + g _ { \beta \mu } \Gamma _ { \alpha \gamma } ^ { \mu } .
$$

By permuting the indices we can produce two alternative versions of this equation,

$$
\partial _ { \alpha } g _ { \gamma \beta } = g _ { \gamma \mu } \Gamma _ { \beta \alpha } ^ { \mu } + g _ { \beta \mu } \Gamma _ { \gamma \alpha } ^ { \mu }
$$

and

$$
\partial _ { \beta } g _ { \gamma \alpha } = g _ { \gamma \mu } \Gamma _ { \alpha \beta } ^ { \mu } + g _ { \alpha \mu } \Gamma _ { \gamma \beta } ^ { \mu } .
$$

We next add the last two equations, subtract the first, and make use of Eq. (5.28). We arrive at

$$
\partial _ { \alpha } g _ { \gamma \beta } + \partial _ { \beta } g _ { \gamma \alpha } - \partial _ { \gamma } g _ { \alpha \beta } = 2 g _ { \gamma \mu } \Gamma _ { \alpha \beta } ^ { \mu } ,
$$

and solve for $\Gamma _ { \alpha \beta } ^ { \mu }$ by multiplying both sides of this equation by the inverse metric $g ^ { \gamma \nu }$ . The end result is

$$
\Gamma _ { \alpha \beta } ^ { \mu } = \frac { 1 } { 2 } g ^ { \mu \nu } \bigl ( \partial _ { \alpha } g _ { \nu \beta } + \partial _ { \beta } g _ { \nu \alpha } - \partial _ { \nu } g _ { \alpha \beta } \bigr ) .
$$

This formula gives rise to a practical method to compute the Christoffel symbols, starting from the metric tensor gαβ .

# Box 5.2

# Vector calculus in polar coordinates

As a simple illustration of the formalism developed so far, we consider a two-dimensional flat plane charted by polar coordinates $( r , \phi )$ . These are defined in terms of the original Cartesian coordinates $( x , y ) { \mathsf { b } } y x =$ $r$ cos $\phi$ and $y = r \sin \phi$ .

The position vector of a point in the plane is given by $\vec { x } = ( r \cos \phi ) \vec { e } _ { x } + ( r \sin \phi ) \vec { e } _ { y } ,$ where the Cartesian basis vectors $\vec { e } _ { x }$ and $\vec { e } _ { y }$ are constant. The polar basis $\vec { e } _ { r }$ and $\vec { e } _ { \phi }$ is given by

$$
\begin{array} { l } { { \displaystyle { \vec { e } } _ { r } = \frac { \partial \vec { x } } { \partial r } = \cos \phi \vec { e } _ { x } + \sin \phi \vec { e } _ { y } , } } \\ { { \displaystyle { \vec { e } } _ { \phi } = \frac { \partial \vec { x } } { \partial \phi } = - r \sin \phi \vec { e } _ { x } + r \cos \phi \vec { e } _ { y } . } } \end{array}
$$

The metric on the plane is calculated either by substituting the relations $d x = \cos \phi d r - r \sin \phi d \phi ,$ $d y = \sin \phi d r + r \cos \phi d \phi$ into $d s ^ { 2 } = d x ^ { 2 } + d y ^ { 2 }$ , or by computing the inner products between the basis vectors $\vec { e } _ { r }$ and $\vec { e } _ { \phi }$ . In both cases we get the non-vanishing components $g _ { r r } = 1$ and $g _ { \phi \phi } = r ^ { 2 } $ , so that

$$
d s ^ { 2 } = d r ^ { 2 } + r ^ { 2 } d \phi ^ { 2 } .
$$

The Christoffel symbols are calculated either by differentiating the basis vectors, or by employing Eq. (5.34).   
In both cases we get the non-vanishing components $\Gamma _ { \phi \phi } ^ { r } = - r$ and $\Gamma _ { r \phi } ^ { \phi } = \Gamma _ { \phi r } ^ { \phi } = r ^ { - 1 }$ .

# Covariant differentiation of tensors

The action of the covariant-derivative operator $\nabla _ { \beta }$ can be extended to tensors. We postulate that: (i) when $\nabla _ { \beta }$ acts on a scalar field, it produces the same result as the partial-derivative operator $\partial _ { \beta }$ ; and (ii) the covariant-derivative operator obeys the product rule of differential calculus, $\nabla _ { \beta } ( A B ) = ( \nabla _ { \beta } A ) B + A ( \nabla _ { \beta } B )$ , in which $A$ and $B$ are any tensorial quantities (with indices suppressed).

The action of $\nabla _ { \beta }$ on a tensor $A ^ { \mu \nu }$ can be determined if we examine the special case $A ^ { \mu \nu } = A ^ { \mu } B ^ { \nu }$ . By invoking the product rule we quickly arrive at $\nabla _ { \beta } ( A ^ { \mu } B ^ { \nu } ) = \partial _ { \beta } ( A ^ { \mu } B ^ { \nu } ) +$ $\Gamma _ { \alpha \beta } ^ { \mu } ( A ^ { \alpha } B ^ { \nu } ) + \Gamma _ { \alpha \beta } ^ { \nu } ( A ^ { \mu } B ^ { \alpha } )$ . The generalization to arbitrary tensors is immediate:

$$
\nabla _ { \beta } A ^ { \mu \nu } = \partial _ { \beta } A ^ { \mu \nu } + \Gamma _ { \alpha \beta } ^ { \mu } A ^ { \alpha \nu } + \Gamma _ { \alpha \beta } ^ { \nu } A ^ { \mu \alpha } .
$$

This rule can easily be extended to tensors with an arbitrary number of indices; there is one Christoffel symbol per tensorial index.

To determine the action of $\nabla _ { \beta }$ on a dual vector $A _ { \mu }$ we examine $\nabla _ { \beta } ( A _ { \mu } B ^ { \mu } )$ , in which $B ^ { \mu }$ is an arbitrary vector. Here the covariant derivative acts on a scalar quantity, and $\nabla _ { \beta } ( A _ { \mu } B ^ { \mu } ) = \partial _ { \beta } ( A _ { \mu } B ^ { \mu } ) = ( \partial _ { \beta } A _ { \mu } ) B ^ { \mu } + A _ { \mu } ( \partial _ { \beta } B ^ { \mu } )$ . On the other hand, the product rule implies $\nabla _ { \beta } ( A _ { \mu } B ^ { \mu } ) = ( \nabla _ { \beta } A _ { \mu } ) B ^ { \mu } + A _ { \mu } ( \nabla _ { \beta } B ^ { \mu } )$ . If we equate these results and use Eq. (5.29) to express $\nabla _ { \beta } B ^ { \mu }$ in terms of partial derivatives and Christoffel symbols, we get $( \nabla _ { \beta } A _ { \mu } ) B ^ { \mu } = ( \partial _ { \beta } A _ { \mu } - \Gamma _ { \mu \beta } ^ { \alpha } A _ { \alpha } ) B ^ { \mu }$ . Since $B ^ { \mu }$ is arbitrary, we must have

$$
\nabla _ { \beta } A _ { \mu } = \partial _ { \beta } A _ { \mu } - \Gamma _ { \mu \beta } ^ { \alpha } A _ { \alpha } .
$$

From this we easily obtain the action of $\nabla _ { \beta }$ on a tensor $A _ { \mu \nu }$ ,

$$
\nabla _ { \beta } A _ { \mu \nu } = \partial _ { \beta } A _ { \mu \nu } - \Gamma _ { \mu \beta } ^ { \alpha } A _ { \alpha \nu } - \Gamma _ { \nu \beta } ^ { \alpha } A _ { \mu \alpha } ,
$$

and the extension of this rule to tensors of arbitrary ranks is immediate.

Comparison of Eqs. (5.30) with (5.37) reveals that

$$
\nabla _ { \gamma } g _ { \alpha \beta } = 0 .
$$

The metric tensor is covariantly constant, and this important fact is often described by the statement that the covariant-derivative operator $\nabla _ { \beta }$ is compatible with the metric. Equation (5.38) implies that the covariant derivative of the inverse metric vanishes also: $\begin{array} { r } { \nabla _ { \gamma } g ^ { \alpha \beta } = 0 } \end{array}$ . These results imply that the operations of index raising and lowering, and covariant differentiation, commute with each other. For example, $\nabla _ { \beta } A _ { \mu } = \nabla _ { \beta } ( g _ { \mu \nu } A ^ { \nu } ) =$ $g _ { \mu \nu } \nabla _ { \beta } A ^ { \nu }$ . This observation is very powerful and produces helpful simplifications in long calculations.

# Metric determinant and volume elements

We conclude this subsection with some results involving the metric determinant $g : =$ $\operatorname* { d e t } [ g _ { \alpha \beta } ]$ . First we mention the identity

$$
\Gamma _ { \mu \beta } ^ { \mu } = \frac { 1 } { 2 } g ^ { \mu \nu } \partial _ { \beta } g _ { \mu \nu } = \frac { 1 } { \sqrt { - g } } \partial _ { \beta } \sqrt { - g } ,
$$

which involves the contraction of the Christoffel symbol over two of its indices. This is established by calculating the change in $g$ that is induced by a change in each component of the metric tensor. It gives rise to a convenient expression for the covariant divergence of a vector field $A ^ { \alpha }$ :

$$
\nabla _ { \alpha } { \cal A } ^ { \alpha } = { \frac { 1 } { \sqrt { - g } } } \partial _ { \alpha } \bigl ( \sqrt { - g } { \cal A } ^ { \alpha } \bigr ) ;
$$

this result follows by direct computation.

Our final observation is that in a curved spacetime, the invariant four-dimensional volume element is

$$
d V = \sqrt { - g } d ^ { 4 } x ,
$$

where $d ^ { 4 } x = d x ^ { 0 } d x ^ { 1 } d x ^ { 2 } d x ^ { 3 }$ is the element of coordinate volume. This result is a consequence of two facts. The first is that the metric determinant changes according to $g ^ { \prime } = g J ^ { 2 }$ under a coordinate transformation $x ^ { \alpha } = f ^ { \alpha } ( x ^ { \prime \mu } )$ , where $J : = \operatorname* { d e t } [ \partial { f ^ { \alpha } } / \partial { x ^ { \prime } } ^ { \mu } ]$ is the Jacobian of the transformation; this property follows directly from Eq. (5.19). The second is that $d ^ { 4 } x$ changes also, but in a subtle way because it is not simply an algebraic string of differentials, but an oriented string. In fact, its proper definition is $d ^ { 4 } x : = d x ^ { 0 } \wedge d x ^ { 1 } \wedge d x ^ { 2 } \wedge d x ^ { 3 }$ , where the wedge operation indicates that interchanging any pair of differentials produces a minus sign. The volume element becomes

$$
d ^ { 4 } x = { \frac { \partial f ^ { 0 } } { \partial x ^ { \prime \mu } } } { \frac { \partial f ^ { 1 } } { \partial x ^ { \prime \nu } } } { \frac { \partial f ^ { 2 } } { \partial x ^ { \prime \rho } } } { \frac { \partial f ^ { 3 } } { \partial x ^ { \prime \omega } } } d x ^ { \prime \mu } \wedge d x ^ { \prime \nu } \wedge d x ^ { \prime \rho } \wedge d x ^ { \prime \omega }
$$

under a coordinate transformation. The indices $\mu , \nu , \rho$ and $\omega$ must all be different, and in the sum over all repeated indices, there will be a plus or minus sign depending on the number of permutations required to get the wedge product into the canonical order $( 0 , 1 , 2 , 3 )$ corresponding to $d ^ { 4 } x ^ { \prime }$ . This yields

$$
d ^ { 4 } x = J d ^ { 4 } x ^ { \prime } .
$$

Combining these facts, we find that ${ \sqrt { - g } } d ^ { 4 } x = { \sqrt { - g ^ { \prime } } } d ^ { 4 } x ^ { \prime }$ , and we verify the statement of Eq. (5.41).

An elementary example of Eq. (5.41) involves the polar coordinates $( r , \phi )$ introduced in Box 5.2. Here we are talking about an element of two-dimensional surface area, and $d ^ { 2 } x = d r d \phi$ . The metric determinant is positive and given by $g = r ^ { 2 }$ . The surface element is therefore ${ \sqrt { g } } d ^ { 2 } x = r d r d \phi$ , the familiar result from elementary calculus.

# 5.2.3 Parallel transport and geodesic equation

# Covariant differentiation on a world line

We examine a timelike world line $x ^ { \alpha } = r ^ { \alpha } ( \tau )$ in a curved spacetime, parameterized by proper time $\tau$ , the time measured by a clock moving on this world line; as before this is defined by $d \tau = \sqrt { - d s ^ { 2 } } / c$ . The world line’s tangent vector is $u ^ { \alpha } = d r ^ { \alpha } / d \tau$ , and this satisfies the normalization condition

$$
g _ { \alpha \beta } u ^ { \alpha } u ^ { \beta } = - c ^ { 2 } ,
$$

which replaces Eq. (4.11). On this world line there exists a vector field $\vec { A } ( \tau )$ , and we wish to evaluate the derivative of this vector with respect to $\tau$ .

We proceed much as in the preceding subsection. We decompose $\vec { A }$ in terms of basis vectors $\vec { e } _ { \alpha }$ and we differentiate:

$$
\frac { d \vec { A } } { d \tau } = \frac { d A ^ { \alpha } } { d \tau } \vec { e } _ { \alpha } + A ^ { \alpha } \frac { d \vec { e } _ { \alpha } } { d \tau } .
$$

Because $d \vec { e } _ { \alpha } / d \tau = ( \partial _ { \beta } \vec { e } _ { \alpha } ) ( d r ^ { \beta } / d \tau ) = u ^ { \beta } \Gamma _ { \alpha \beta } ^ { \mu } \vec { e } _ { \mu }$ , this is

$$
\frac { d \vec { A } } { d \tau } = \biggl ( \frac { d A ^ { \mu } } { d \tau } + \Gamma _ { \alpha \beta } ^ { \mu } A ^ { \alpha } u ^ { \beta } \biggr ) \vec { e } _ { \mu } .
$$

The quantity within brackets is the covariant derivative of $A ^ { \mu }$ along the world line. We denote this

$$
\frac { D A ^ { \mu } } { d \tau } : = \frac { d A ^ { \mu } } { d \tau } + \Gamma _ { \alpha \beta } ^ { \mu } A ^ { \alpha } u ^ { \beta } ,
$$

so that $d \vec { A } / d \tau = ( D A ^ { \mu } / d \tau ) \vec { e } _ { \mu }$ . When the vector field $\vec { A }$ is defined also in the neighborhood of the world line (and not just directly on the world line), it becomes a function of all the spacetime coordinates $x ^ { \alpha }$ (instead of just proper time $\tau$ ); then $d A ^ { \mu } / d \tau = u ^ { \beta } \partial _ { \beta } A ^ { \mu }$ and the covariant derivative can expressed as $D A ^ { \mu } / d \tau = u ^ { \beta } \nabla _ { \beta } A ^ { \mu }$ .

# Parallel transport and geodesics

The vector $\vec { A }$ is parallel-transported along the world line when it stays constant in both direction and magnitude. The mathematical statement of this is $d \vec { A } / d \tau = 0$ , or

$$
{ \frac { D A ^ { \mu } } { d \tau } } = 0 \qquad \mathrm { ( p a r a l l e l ~ t r a n s p o r t ) . }
$$

A timelike world line $r ^ { \alpha } ( \tau )$ is a geodesic of the curved spacetime when its own tangent vector $\vec { u }$ is parallel-transported along the world line. A geodesic, defined in this way, is everywhere locally straight. The mathematical statement of the geodesic equation is

$$
{ \frac { D u ^ { \mu } } { d \tau } } = 0 ,
$$

or

$$
{ \frac { d u ^ { \mu } } { d \tau } } + \Gamma _ { \alpha \beta } ^ { \mu } u ^ { \alpha } u ^ { \beta } = 0 ,
$$

or else

$$
\frac { d ^ { 2 } r ^ { \mu } } { d \tau ^ { 2 } } + \Gamma _ { \alpha \beta } ^ { \mu } \frac { d r ^ { \alpha } } { d \tau } \frac { d r ^ { \beta } } { d \tau } = 0 .
$$

This last form is a system of second-order differential equations for the functions $r ^ { \mu } ( \tau )$ . These equations admit a unique solution given initial conditions $r ^ { \mu } ( 0 )$ and $u ^ { \mu } ( 0 )$ at some initial time $\tau = 0$ .

The definition of a geodesic – a world line that parallel-transports its own tangent vector – is very fundamental and nicely geometrical. It applies just as well to spacelike and null geodesics. It applies to many kinds of spaces or manifolds. It applies to the two-dimensional surface of a sphere, where the geodesics are known as “great circles.” It also applies to very abstract spaces, such as the space defined by the operations of the rotation group.

To illustrate the physical meaning of the geodesic equation we return to the Newtonian metric of Eq. (5.12) and calculate its geodesics. It is a simple exercise to show that for this spacetime, the non-vanishing Christoffel symbols are $\Gamma _ { 0 j } ^ { 0 } = \Gamma _ { 0 0 } ^ { j } = - \partial _ { j } ( U / c ^ { 2 } )$ . It follows that in Newtonian situations, the spatial components of Eq. (5.51) reduce to ${ d ^ { 2 } } { \boldsymbol { r } } / { d t ^ { 2 } } - \nabla U = 0$ . These are the Newtonian equations of motion, and this result provides a suggestion that a freely-moving body in curved spacetime moves on a geodesic.

This connection between the geodesic equation and the dynamics of a freely-moving body is confirmed when we recognize that Eq. (5.49) looks a lot like the vanishing of the acceleration of a free particle in Minkowski space. Indeed, in a local inertial frame in which the Christoffel symbols vanish (whose existence will be justified in Sec. 5.2.5), the equation is precisely ${ d u ^ { \mu } } / { d \tau } = a ^ { \mu } = 0$ . There is therefore a direct link between the straight-line motion of a free particle in a local inertial frame and geodesic motion.

Another way to see the connection is to observe that the geodesic equation (5.51) can be obtained on the basis of a variational principle, in which the action functional is the elapsed proper time $\textstyle { \int _ { 1 } ^ { 2 } d \tau }$ along a parameterized curve $r ^ { \alpha } ( \tau )$ linking the fixed events 1 and 2. If, as we proposed in Sec. 5.1.3, the particle action introduced back in Sec. 4.1.8 is generalized to

$$
S = - m c ^ { 2 } \int _ { 1 } ^ { 2 } d \tau = - m c \int _ { 1 } ^ { 2 } { \sqrt { - g _ { \alpha \beta } { \frac { d r ^ { \alpha } } { d t } } { \frac { d r ^ { \beta } } { d t } } } } d t
$$

in curved spacetime, then its extremization with respect to world-line variations returns the geodesic equation. (You will be asked to prove this statement in Exercise 5.8.) These considerations, therefore, strongly point to the geodesic equation as a description of free particle motion in curved spacetime.

Another useful statement of the geodesic equation is

$$
\frac { d u _ { \mu } } { d \tau } = \frac { 1 } { 2 } u ^ { \alpha } u ^ { \beta } \partial _ { \mu } g _ { \alpha \beta } ,
$$

which can be obtained by lowering the index on Eq. (5.50) and simplifying the result. This form of the geodesic equation reveals immediately that when the metric does not depend on one (or more) of its coordinates $x ^ { \mu }$ , then the corresponding component $u _ { \mu }$ of the velocity (dual) vector is a constant of the motion.

# Null geodesics

Our considerations thus far have been limited to timelike world lines. As we shall see below in $\operatorname { B o x } 5 . 6 $ , photons also move on geodesics of a curved spacetime. These geodesics, however, are such that $d s ^ { 2 } = 0$ , and these cannot be parameterized by proper time $\tau$ . A lightlike geodesic is instead parameterized by $\lambda = \operatorname* { l i m } ( \tau / m )$ , and its tangent vector is identified with the photon’s momentum vector $p ^ { \mu }$ , which satisfies the null condition $g _ { \mu \nu } p ^ { \mu } p ^ { \nu } = 0$ . We have that $p ^ { \mu } = d r ^ { \mu } / d \lambda$ , and this satisfies the geodesic equation

$$
\frac { d p ^ { \mu } } { d \lambda } + \Gamma _ { \alpha \beta } ^ { \mu } p ^ { \alpha } p ^ { \beta } = 0 .
$$

A variant of Eq. (5.53) is also valid: $d p _ { \mu } / d \lambda = { \textstyle { \frac { 1 } { 2 } } } p ^ { \alpha } p ^ { \beta } \partial _ { \mu } g _ { \alpha \beta }$ , so that $p _ { \mu }$ is a constant of the motion when the metric does not depend on coordinate $x ^ { \mu }$ . The geodesic equation for photons can also be derived from a variational principle, but with a twist. One uses the

action

$$
S = \int _ { 1 } ^ { 2 } \left( g _ { \alpha \beta } \frac { d r ^ { \alpha } } { d \lambda } \frac { d r ^ { \beta } } { d \lambda } \right) d \lambda ,
$$

where we have dropped the mass (which is zero), some minus signs and factors of $c$ (which are now irrelevant), and the square root, which has the desirable effect of avoiding the presence of zeros in the denominator when applying the Euler–Lagrange equations. We observe that the photon action is identically zero when the action is evaluated on a null geodesic. But it deviates from zero when evaluated on displaced paths, and its extremization is a well-defined procedure. It is interesting to note that the extremum giving a null geodesic between events 1 and 2 is neither a maximum nor a minimum, but a saddle point.

# 5.2.4 Curvature tensors

# Riemann tensor

The symmetry of the Christoffel symbols in the lower indices implies that the action of two covariant derivatives on a scalar field $f$ is independent of their order:

$$
\nabla _ { \alpha } \nabla _ { \beta } f - \nabla _ { \beta } \nabla _ { \alpha } f = 0 .
$$

The same is not true, however, when the covariant derivatives act on a vector field $A ^ { \mu }$ ; in this case

$$
\nabla _ { \alpha } \nabla _ { \beta } A ^ { \mu } - \nabla _ { \beta } \nabla _ { \alpha } A ^ { \mu } = R ^ { \mu } { } _ { \nu \alpha \beta } A ^ { \nu } ,
$$

and the operations do not commute. This equation defines the Riemann curvature tensor $R _ { \nu \alpha \beta } ^ { \mu }$ . A lengthy evaluation of the left-hand side of Eq. (5.57) shows that the Riemann tensor is given explicitly by

$$
R _ { \beta \gamma \delta } ^ { \alpha } = \partial _ { \gamma } \Gamma _ { \beta \delta } ^ { \alpha } - \partial _ { \delta } \Gamma _ { \beta \gamma } ^ { \alpha } + \Gamma _ { \mu \gamma } ^ { \alpha } \Gamma _ { \beta \delta } ^ { \mu } - \Gamma _ { \mu \delta } ^ { \alpha } \Gamma _ { \beta \gamma } ^ { \mu } .
$$

The Riemann tensor is evidently antisymmetric in its last two indices. It also possesses additional symmetries that are not immediately revealed by Eqs. (5.57) and (5.58). These are

$$
\begin{array} { r l } & { R _ { \alpha \beta \delta \gamma } = - R _ { \alpha \beta \gamma \delta } , } \\ & { R _ { \beta \alpha \gamma \delta } = - R _ { \alpha \beta \gamma \delta } , } \\ & { R _ { \gamma \delta \alpha \beta } = + R _ { \alpha \beta \gamma \delta } , } \\ & { R _ { \mu \alpha \beta \gamma } + R _ { \mu \gamma \alpha \beta } + R _ { \mu \beta \gamma \alpha } = 0 . } \end{array}
$$

By virtue of these symmetries, the Riemann tensor possesses 20 independent components in a four-dimensional spacetime.

Another important set of identities satisfied by the Riemann tensor is

$$
\nabla _ { \alpha } R _ { \mu \nu \beta \gamma } + \nabla _ { \gamma } R _ { \mu \nu \alpha \beta } + \nabla _ { \beta } R _ { \mu \nu \gamma \alpha } = 0 .
$$

These are known as the Bianchi identities, and as we shall see, they play a fundamental role in Einstein’s general relativity.

![](images/ae8a8cbf78e2089d6259973de94eab36407cf937e744a7be976a9e2918187b72.jpg)

Congruence of timelike geodesics. The vector $u ^ { \alpha }$ is tangent to each geodesic $\mu =$ constant. The deviation vector $\xi ^ { \alpha }$ is tangent to each curve $\tau =$ constant, and points from geodesic to geodesic.

# Geodesic deviation

The geometrical meaning of the Riemann tensor is revealed most vividly by the equation of geodesic deviation, which governs the behavior of neighboring geodesics. We consider a continuous sequence of timelike geodesics parameterized by proper time $\tau$ , with each geodesic labelled by a parameter $\mu$ (refer to Fig. 5.1). This is sometimes called a congruence of timelike geodesics, and the entire congruence can be described by the parametric equations $x ^ { \alpha } = r ^ { \alpha } ( \tau , \mu )$ . When $\mu$ is kept fixed and $\tau$ varied in these equations, the displacement is along a selected geodesic within the congruence, and the geodesic’s tangent vector is $u ^ { \alpha } = \partial r ^ { \alpha } / \partial \tau$ . When, on the other hand, $\tau$ is kept fixed and $\mu$ varied, the displacement is across geodesics, and the vector $\xi ^ { \alpha } : = \partial r ^ { \alpha } / \partial \mu$ is a deviation vector that points from geodesic to geodesic. We wish to derive an evolution equation for this deviation vector.

To begin we note that since $u ^ { \alpha }$ is defined as a vector field within the entire congruence, the geodesic equation can be expressed as $u ^ { \beta } \nabla _ { \beta } u ^ { \alpha } = 0$ . We note also that the definitions of $u ^ { \alpha }$ and $\xi ^ { \alpha }$ imply

$$
\xi ^ { \beta } \partial _ { \beta } u ^ { \alpha } - u ^ { \beta } \partial _ { \beta } \xi ^ { \alpha } = \frac { \partial } { \partial \mu } \bigg ( \frac { \partial r ^ { \alpha } } { \partial \tau } \bigg ) - \frac { \partial } { \partial \tau } \bigg ( \frac { \partial r ^ { \alpha } } { \partial \mu } \bigg ) = 0 ,
$$

and the equation can be re-expressed in covariant form as

$$
\xi ^ { \beta } \nabla _ { \beta } u ^ { \alpha } = u ^ { \beta } \nabla _ { \beta } \xi ^ { \alpha }
$$

by exploiting the symmetries of the Christoffel symbols. We next invoke Eq. (5.57) and write

$$
\xi ^ { \gamma } u ^ { \delta } \left( \nabla _ { \gamma } \nabla _ { \delta } u ^ { \alpha } - \nabla _ { \delta } \nabla _ { \gamma } u ^ { \alpha } \right) = R _ { \beta \gamma \delta } ^ { \alpha } u ^ { \beta } \xi ^ { \gamma } u ^ { \delta } .
$$

We rewrite the first term on the left-hand side as

$$
\xi ^ { \gamma } u ^ { \delta } \nabla _ { \gamma } \nabla _ { \delta } u ^ { \alpha } = \xi ^ { \gamma } \nabla _ { \gamma } \left( u ^ { \delta } \nabla _ { \delta } u ^ { \alpha } \right) - \xi ^ { \gamma } \left( \nabla _ { \gamma } u ^ { \delta } \right) \left( \nabla _ { \delta } u ^ { \alpha } \right) ,
$$

and note that the first term on the right-hand side vanishes by virtue of the geodesic equation. Similarly, we rewrite the second term as

$$
\xi ^ { \gamma } u ^ { \delta } \nabla _ { \delta } \nabla _ { \gamma } u ^ { \alpha } = u ^ { \delta } \nabla _ { \delta } \big ( \xi ^ { \gamma } \nabla _ { \gamma } u ^ { \alpha } \big ) - u ^ { \delta } \big ( \nabla _ { \delta } \xi ^ { \gamma } \big ) \big ( \nabla _ { \gamma } u ^ { \alpha } \big ) ,
$$

and make use of Eq. (5.62) in the first term on the right-hand side. All of this produces

$$
- \ R _ { \beta \gamma \delta } ^ { \alpha } u ^ { \beta } \xi ^ { \gamma } u ^ { \delta } = u ^ { \delta } \nabla _ { \delta } \big ( u ^ { \gamma } \nabla _ { \gamma } \xi ^ { \alpha } \big ) - \big ( u ^ { \delta } \nabla _ { \delta } \xi ^ { \gamma } - \xi ^ { \delta } \nabla _ { \delta } u ^ { \gamma } \big ) \big ( \nabla _ { \gamma } u ^ { \alpha } \big ) ,
$$

and we see that the second term vanishes when we invoke Eq. (5.62) once more. The first term is recognized as $D ^ { 2 } \xi ^ { \alpha } / d \tau ^ { 2 }$ , the second covariant derivative of the deviation vector along each geodesic within the congruence.

We have obtained the equation of geodesic deviation,

$$
\frac { D ^ { 2 } \xi ^ { \alpha } } { d \tau ^ { 2 } } = - R _ { ~ \beta \gamma \delta } ^ { \alpha } u ^ { \beta } \xi ^ { \gamma } u ^ { \delta } ,
$$

which states that there is a relative acceleration between geodesics whenever the spacetime is curved, that is, whenever the Riemann curvature tensor is non-zero. To reflect on this we examine the situation in flat spacetime. Here the geodesics must be straight lines, and while these can diverge away from each other when they are not parallel, the rate at which they do so is necessarily constant. In this case the relative acceleration is zero, and this is compatible with Eq. (5.67) because the Riemann tensor vanishes in Minkowski spacetime. In a curved spacetime the situation is different: geodesics that start parallel to each other will eventually converge or diverge (think of two great circles on the surface of a sphere, starting parallel at the equator but converging together at both poles), and this effect is associated with a non-zero relative acceleration $D ^ { 2 } \xi ^ { \alpha } / d \tau ^ { 2 }$ . Equation (5.67) then implies that the Riemann tensor cannot vanish when neighboring geodesics behave in this manner. We conclude that it is the Riemann tensor that measures the curvature of a four-dimensional spacetime.

Equation (5.67) is the precise statement of Eq. (5.6). The approximate version can be recovered by inserting $u ^ { \alpha } \simeq ( c , \mathbf { 0 } )$ , and $\xi ^ { \alpha } \simeq ( 0 , \pmb \xi )$ into Eq. (5.67), thus putting us in Cliff ’s momentary rest frame, and by using the Newtonian metric of Eq. (5.12) to show that $R _ { 0 j 0 k } \simeq - \partial _ { j k } ( U / c ^ { 2 } )$ . The spatial components of Eq. (5.67) reduce to

$$
\frac { d ^ { 2 } \xi ^ { j } } { d t ^ { 2 } } \simeq - c ^ { 2 } R _ { \ : 0 k 0 } ^ { j } \xi ^ { k } \simeq ( \partial _ { j k } U ) \xi ^ { k } ,
$$

and this equation describes the action of tidal gravitational forces in Cliff ’s laboratory.

The equation of geodesic deviation, in its exact formulation, carries the same interpretation: it describes the effects of tidal forces on neighboring observers that move freely in a gravitational field. The observers move on neighboring geodesics, their separation is described by the vector $\xi ^ { \alpha }$ , the tidal forces produce a relative acceleration $D ^ { 2 } \xi ^ { \alpha } / d \tau ^ { 2 }$ , and since the tidal forces are caused by inhomogeneities in the gravitational field, we conclude that these are measured by the Riemann tensor. Note that a non-zero Riemann tensor unambiguously reveals the existence of a gravitational field; a non-trivial metric tensor does not, because the complexity of the metric could come entirely from the coordinates used to chart a flat spacetime. The Riemann tensor, therefore, is of fundamental importance in general relativity.

# Ricci and Einstein tensors

Other curvature tensors can be obtained from the Riemann tensor. By contracting the first and third indices of the Riemann tensor we obtain the Ricci tensor

$$
R _ { \alpha \beta } : = R _ { \alpha \mu \beta } ^ { \mu } .
$$

The symmetries of the Riemann tensor imply that $R _ { \beta \alpha } = R _ { \alpha \beta }$ , and the Ricci tensor possesses ten independent components. By contracting its indices we obtain the Ricci scalar

$$
R : = R _ { \mu } ^ { \mu } = g ^ { \alpha \beta } R _ { \alpha \beta } .
$$

Closely related to the Ricci tensor is the Einstein tensor

$$
G _ { \alpha \beta } : = R _ { \alpha \beta } - \frac { 1 } { 2 } g _ { \alpha \beta } R ,
$$

which is also symmetric in its indices: $G _ { \beta \alpha } = G _ { \alpha \beta }$ . The Einstein tensor possesses ten independent components, and its trace is given by ${ \cal G } : = g ^ { \alpha \beta } { \cal G } _ { \alpha \beta } = - R$ , because $g ^ { \alpha \beta } g _ { \alpha \beta } =$ $\delta _ { \alpha } ^ { \alpha } = 4$ .

The Bianchi identities of Eq. (5.60) give rise to

$$
\nabla _ { \beta } G ^ { \alpha \beta } = 0
$$

after two contractions of their indices. Equation (5.72) is known as the contracted Bianchi identities, and as we shall see, it plays a fundamental role in general relativity.

# 5.2.5 Curvature and the local inertial frame

Back in Sec. 5.1.2 we asserted that it is always possible to find a coordinate transformation $x ^ { \alpha } = F ^ { \alpha } ( \xi ^ { \mu } )$ that puts the metric $g _ { \alpha \beta }$ into a local Minkowski form. We return to this issue here, and explicitly construct the coordinates that achieve this important goal. In fact, we shall construct two such coordinate systems. The first system, the Riemann normal coordinates $\zeta ^ { \mu }$ , is such that at a selected event $\mathcal { O }$ in spacetime, the metric is equal to the Minkowski metric $\eta _ { \mu \nu }$ and the Christoffel symbols $\Gamma _ { \nu \lambda } ^ { \mu }$ vanish. The second system, the Fermi normal coordinates $\xi ^ { \mu }$ , is such that everywhere on a timelike geodesic $\gamma$ , the metric is equal to the Minkowski form and the Christoffel symbols vanish. The Fermi coordinates are the mathematical embodiment of a local inertial frame in general relativity.

# Riemann normal coordinates

We begin with the Riemann normal coordinates. The strategy we adopt to construct this coordinate system is very similar to what we might do in three-dimensional flat space to construct Cartesian coordinates. One way to proceed would involve the following steps. First, we select an origin $\mathcal { O }$ . Second, we erect at $\mathcal { O }$ a set of three unit vectors $e _ { ( j ) }$ that point in mutually orthogonal directions; here the bracketed index serves to label each basis vector. Third, we select a point $\mathcal { P }$ and draw the straight line segment that links it to $\mathcal { O }$ ; the segment points in the direction of the unit vector $\pmb { n }$ , and $\mathcal { P }$ is at a distance $r$ from the origin. Fourth, we decompose the vector $\pmb { n }$ into the vector basis and express it as $\pmb { n } = \pmb { n } ^ { j } \pmb { e } _ { ( j ) }$ .

![](images/98661bd2d85b5742457361c539b4c0ce543bcf39be3320bca958085a46ef930f.jpg)  
Fig. 5.2 Riemann normal coordinates about an event $\mathcal { O }$ in spacetime. The construction involves a geodesic segment $\beta$ to which $\eta ^ { \alpha }$ is tangent.

And fifth, we assign to $\mathcal { P }$ the coordinates $x ^ { j } = r n ^ { j }$ and show that in these coordinates, the metric of three-dimensional flat space is given by $\delta _ { j k }$ . The key features of this construction are that the coordinates are anchored to straight lines emanating from $\mathcal { O }$ , and that they are defined directly in terms of the direction of each line and the distance measured along it. The generalization to curved spacetime suggests itself: use geodesics instead of straight lines, and define the coordinates in exactly the same way.

So let us now consider a curved spacetime with a metric $g _ { \alpha \beta }$ initially expressed in an arbitrary coordinate system $x ^ { \alpha }$ . We select an event $\mathcal { O }$ in this spacetime, and at $\mathcal { O }$ we erect a set of four unit vectors $e _ { ( \mu ) } ^ { \alpha }$ that point in mutually orthogonal directions (refer to Fig. 5.2); here the index $\alpha$ is the usual vector index that refers to the coordinates $x ^ { \alpha }$ , while the bracketed index $( \mu )$ is a label that allows us to distinguish each vector. The vector $e _ { ( 0 ) } ^ { \alpha }$ is timelike, while the remaining vectors $e _ { ( j ) } ^ { \alpha }$ are spacelike; the orthonormality condition can be compactly expressed by

$$
g _ { \alpha \beta } e _ { ( \mu ) } ^ { \alpha } e _ { ( \nu ) } ^ { \beta } = \eta _ { \mu \nu } ,
$$

in which $\eta _ { \mu \nu } : = \mathrm { d i a g } ( - 1 , 1 , 1 , 1 )$ is the Minkowski metric of flat spacetime.

We now select another event $\mathcal { P }$ in spacetime, and draw the geodesic segment $\beta$ that links $\mathcal { P }$ to $\mathcal { O }$ ; this geodesic is assumed to be unique, and this usually requires $\mathcal { P }$ to be in a sufficiently close neighborhood of $\mathcal { O }$ . The geodesic is parameterized by proper distance $s$ if it is spacelike, so that $s = 0$ at $\mathcal { O }$ and $s = s p$ at $\mathcal { P }$ , and by (rescaled) proper time $c \tau$ if it is timelike (with similar assignments at $\mathcal { O }$ and $\mathcal { P }$ ). Its tangent vector is the unit vector $n ^ { \alpha }$ , and at $\mathcal { O }$ this can be decomposed in the basis $e _ { ( \mu ) } ^ { \alpha }$ ; we write

$$
n ^ { \alpha } ( { \mathcal O } ) = n ^ { \mu } e _ { ( \mu ) } ^ { \alpha } ,
$$

in which $n ^ { \mu }$ is a set of four coefficients that specify the direction of $\beta$ relative to the vector basis. The Riemann normal coordinates of $\mathcal { P }$ are defined to be $\zeta ^ { \mu } : = s _ { \mathcal P } n ^ { \mu }$ when $\beta$ is spacelike, and $\zeta ^ { \mu } : = ( c \tau _ { \mathcal P } ) n ^ { \mu }$ when $\beta$ is timelike. As we show in Box 5.3, the construction

implies that the spacetime metric near $\mathcal { O }$ becomes

$$
g _ { \mu \nu } = \eta _ { \mu \nu } - \frac { 1 } { 3 } R _ { \mu \lambda \nu \rho } ( \mathcal { O } ) \zeta ^ { \lambda } \zeta ^ { \rho } + O ( \zeta ^ { 3 } ) ,
$$

when expressed in Riemann normal coordinates. Because $\zeta ^ { \mu } = 0$ at $\mathcal { O }$ , we see that $g _ { \mu \nu } ( \mathcal { O } ) = \eta _ { \mu \nu }$ so that as promised, the metric assumes the Minkowski form at the event $\mathcal { O }$ . But we have more: because the expansion of the metric in powers of $\zeta ^ { \mu }$ does not include linear terms, we find that $\partial _ { \lambda } g _ { \mu \nu } ( \mathcal { O } ) = 0$ , which implies that all Christoffel symbols vanish at $\mathcal { O }$ . This is an important property of the Riemann normal coordinates, and we have obtained a constructive proof that it is always possible to find coordinates that enforce the properties

$$
g _ { \mu \nu } ( \mathcal { O } ) = \eta _ { \mu \nu } , \qquad \Gamma _ { \nu \lambda } ^ { \mu } ( \mathcal { O } ) = 0 ,
$$

at a selected event $\mathcal { O }$ in spacetime. The construction also shows that it is not possible to set the second derivatives of the metric tensor to zero at $\mathcal { O }$ unless the Riemann tensor vanishes there; a second-order deviation of the metric relative to the Minkowski values therefore signals the presence of curvature.

We wish to show that the construction of Riemann normal coordinates (RNC) detailed in the text leads to the metric of Eq. (5.75). The construction implies that the geodesic $\beta$ that links $\mathcal { P }$ to $\mathcal { O }$ is described by

$$
\zeta ^ { \mu } = s n ^ { \mu }
$$

n RNC, and that $n ^ { \mu } = d \zeta ^ { \mu } / d s$ is a constant tangent vector on $\beta$ . (To simplify the language we take $\beta$ to be a spacelike geodesic.) When we vary the directions $n ^ { \mu }$ in these equations, we obtain other geodesics that also originate from $\mathcal { O }$ , and

$$
\eta _ { ( \nu ) } ^ { \mu } : = \frac { \partial \zeta ^ { \mu } } { \partial n ^ { \nu } } = s \delta _ { \nu } ^ { \mu }
$$

is a set of deviation vectors (one for each direction $n ^ { \nu }$ ) that point from $\beta$ to the displaced geodesics.

To show that $g _ { \mu \nu } = \eta _ { \mu \nu }$ at $\mathcal { O }$ we use the fact that $n ^ { \mu }$ is a unit vector. In RNC the mathematical statement of this is $g _ { \mu \nu } n ^ { \mu } n ^ { \nu } = 1$ , which is valid everywhere on $\beta$ . In the original coordinates $x ^ { \alpha }$ we have instead $g _ { \alpha \beta } n ^ { \alpha } n ^ { \beta } = 1 \ /$ , in which we may insert Eqs. (5.73) and (5.74) to obtain $\eta _ { \mu \nu } n ^ { \mu } n ^ { \nu } = 1$ at $\mathcal { O }$ . Because the metric $g _ { \mu \nu }$ at $\mathcal { O }$ must be independent of the directions $n ^ { \mu }$ , and because these are arbitrary, we conclude that $g _ { \mu \nu } ( \mathcal { O } ) = \eta _ { \mu \nu }$ .

To show that the Christoffel symbols vanish at $\mathcal { O }$ we insert Eq. (1) within the geodesic equation and obtain $\Gamma _ { \nu \lambda } ^ { \mu } n ^ { \nu } n ^ { \lambda } = 0$ , which is valid everywhere on $\beta$ . But because the Christoffel symbols at $\mathcal { O }$ must be independent of the directions $n ^ { \mu }$ , and because these are arbitrary, we conclude that $\Gamma _ { \nu \lambda } ^ { \mu } ( { \mathcal O } ) = 0$ . This, in turn, implies that $\partial _ { \lambda } g _ { \mu \nu } ( \mathcal { O } ) = 0$ .

To relate the second derivatives of the metric at $\mathcal { O }$ to the Riemann tensor we apply the equation of geodesic deviation, Eq. (5.67), to each one of the deviation vectors of Eq. (2). Because the Christoffel symbols vanish at $\mathcal { O }$ , we have that $\Gamma _ { \nu \lambda } ^ { \mu } = \partial _ { \rho } \Gamma _ { \nu \lambda } ^ { \mu } ( \mathcal { O } ) \zeta ^ { \rho } + \cdot \cdot \cdot .$ , and the covariant derivative of the deviation vectors along

$\beta$ is given by

$$
\frac { D \eta _ { ( \nu ) } ^ { \mu } } { d s } = \delta _ { \nu } ^ { \mu } + s ^ { 2 } \partial _ { \rho } \Gamma _ { \nu \lambda } ^ { \mu } ( \mathcal { O } ) n ^ { \lambda } n ^ { \rho } + O ( s ^ { 3 } ) .
$$

The second covariant derivative is

$$
\frac { D ^ { 2 } \eta _ { ( \nu ) } ^ { \mu } } { d s ^ { 2 } } = 3 s \ \partial _ { \rho } \Gamma _ { \nu \lambda } ^ { \mu } ( \mathcal { O } ) n ^ { \lambda } n ^ { \rho } + O ( s ^ { 2 } ) ,
$$

and the equation of geodesic deviation becomes

$$
\biggl [ 3 \partial _ { \rho } \Gamma _ { \nu \lambda } ^ { \mu } ( \mathcal { O } ) + R _ { \lambda \nu \rho } ^ { \mu } ( \mathcal { O } ) \biggr ] n ^ { \lambda } n ^ { \rho } + O ( s ) = 0 .
$$

Evaluating this at $\mathcal { O }$ , and appealing once more to the arbitrariness of the directions $n ^ { \mu }$ , we arrive at

$$
\partial _ { \lambda } \Gamma _ { \nu \rho } ^ { \mu } + \partial _ { \rho } \Gamma _ { \nu \lambda } ^ { \mu } = - \frac { 1 } { 3 } \Big ( R _ { \lambda \nu \rho } ^ { \mu } + R _ { \rho \nu \lambda } ^ { \mu } \Big )
$$

after properly symmetrizing the expression with respect to the indices $\lambda$ and $\rho$ . By permuting the indices we produce two alternative versions of this equation, which we add to and subtract from the original equation – refer to Eq. (5.30) for similar manipulations. This allows us to solve for the derivatives of the Christoffel symbols,

$$
\partial _ { \rho } \Gamma _ { \nu \lambda } ^ { \mu } ( \mathcal { O } ) = - \frac { 1 } { 3 } \big ( R _ { \nu \lambda \rho } ^ { \mu } + R _ { \lambda \nu \rho } ^ { \mu } \big ) ,
$$

in which the Riemann tensor is evaluated at $\mathcal { O }$ . From this and Eq. (5.30) it is a simple matter to obtain

$$
\partial _ { \lambda \rho } g _ { \mu \nu } ( \mathcal { O } ) = - \frac { 1 } { 3 } \big ( R _ { \mu \lambda \nu \rho } + R _ { \mu \rho \nu \lambda } \big ) .
$$

The metric of Eq. (5.75) is finally recovered by expanding $g _ { \mu \nu }$ in powers of $\zeta ^ { \mu }$ and inserting the expressions obtained here for the partial derivatives.

# Fermi normal coordinates

We next turn to the Fermi normal coordinates. Instead of a single event $\mathcal { O }$ we now select an entire timelike geodesic $\gamma$ in spacetime. The geodesic is parameterized by proper time $\tau$ , and everywhere on $\gamma$ we erect a vector basis $e _ { ( \mu ) } ^ { \alpha }$ that satisfies Eq. (5.73). We take $e _ { ( 0 ) } ^ { \alpha }$ to be aligned with $\gamma$ ’s tangent vector, and we assume that all vectors are parallel-transported along $\gamma$ .

We next select an event $\mathcal { P }$ in spacetime, away from $\gamma$ , and draw a spacelike geodesic $\beta$ that passes through $\mathcal { P }$ and intersects $\gamma$ orthogonally at $\mathcal { Q }$ (see Fig. 5.3); the requirement of orthogonality ensures that $\beta$ is unique. The geodesic is parameterized by proper distance $s$ , so that $s = 0$ at $\mathcal { Q }$ and $s = s _ { \mathcal { P } }$ at $\mathcal { P }$ , and its tangent vector is the unit vector $n ^ { \alpha }$ . At $\mathcal { Q }$ the vector can be decomposed as

$$
n ^ { \alpha } ( \mathcal { Q } ) = n ^ { j } e _ { ( j ) } ^ { \alpha } ,
$$

where $e _ { ( j ) } ^ { \alpha }$ are the spatial members of the vector basis; the temporal member $e _ { ( 0 ) } ^ { \alpha }$ is not involved because $\beta$ is orthogonal to $\gamma$ . The Fermi normal coordinates of $\mathcal { P }$ are defined to

![](images/a8c90f82f8baafd4978c971690009f2b3791d183c7df38d7cef46ab352e0cdff.jpg)  
Fermi normal coordinates about a timelike geodesic $\gamma$ in spacetime. The construction involves a spacelike geodesic segment $\beta$ which is orthogonal to $\gamma$ , and to which $\eta ^ { \alpha }$ is tangent.

be $\xi ^ { 0 } : = c \tau _ { \mathcal { Q } }$ and $\xi ^ { j } : = s _ { \mathcal { P } } n ^ { j }$ . As we show in Box 5.4, the construction implies that the spacetime metric near $\gamma$ becomes

$$
\begin{array} { l } { { g _ { 0 0 } = - 1 - R _ { 0 p 0 q } ( \gamma ) \xi ^ { p } \xi ^ { q } + { \cal O } ( \xi ^ { 3 } ) , } } \\ { { \displaystyle g _ { 0 j } = \frac { 2 } { 3 } R _ { j p q 0 } ( \gamma ) \xi ^ { p } \xi ^ { q } + { \cal O } ( \xi ^ { 3 } ) , } } \\ { { \displaystyle g _ { j k } = \delta _ { j k } - \frac { 1 } { 3 } R _ { j p k q } ( \gamma ) \xi ^ { p } \xi ^ { q } + { \cal O } ( \xi ^ { 3 } ) , } } \end{array}
$$

when expressed in Fermi normal coordinates; here the Riemann tensor is evaluated on $\gamma$ and expressed as a function of $\tau : = \xi ^ { 0 } / c$ . Because $\xi ^ { j } = 0$ everywhere on $\gamma$ , we see that $g _ { \mu \nu } ( \gamma ) = \eta _ { \mu \nu }$ , so that the metric assumes the Minkowski form on the entire timelike geodesic. Because the metric is constant on $\gamma$ , and because its expansion away from $\gamma$ does not include terms linear in $\xi ^ { j }$ , we find that all first derivatives of the metric vanish on $\gamma$ , which implies that the Christoffel symbols also vanish on $\gamma$ . This amounts to a constructive proof that it is always possible to find coordinates that enforce the properties

$$
g _ { \mu \nu } ( \gamma ) = \eta _ { \mu \nu } , \qquad \Gamma _ { \nu \lambda } ^ { \mu } ( \gamma ) = 0 ,
$$

everywhere along a selected timelike geodesic $\gamma$ in spacetime. The Fermi normal coordinates provide the best mathematical realization of our notion of a freely-moving frame, in which gravity can be removed locally, up to effects associated with field inhomogeneities described by the Riemann tensor.

The significance of the Riemann tensor in Eq. (5.78) is clearly revealed when we work out the expression of the geodesic equation in Fermi normal coordinates. We examine a free particle moving on a world line $\xi ^ { j } = r ^ { j } ( t )$ in a neighborhood of the reference geodesic $\gamma$ ; we adopt $t : = \xi ^ { 0 } / c$ as the world-line parameter, and use the symbol $t$ to emphasize the fact that while $t$ is proper time on $\gamma$ , it is not proper time on the particle’s world line. The easiest way to obtain the geodesic equation is to insert the metric within ${ \cal L } = - m c \sqrt { - g _ { \mu \nu } \dot { r } ^ { \mu } \dot { r } ^ { \nu } }$ , the Lagrangian of Eq. (5.52). When we work consistently to second order in the spatial displacements $r ^ { j }$ and velocities ${ \dot { r } } ^ { j } : = d r ^ { j } / d t$ , we find that the Lagrangian simplifies to

$$
L = - m c ^ { 2 } + \frac { 1 } { 2 } m v ^ { 2 } - \frac { 1 } { 2 } m c ^ { 2 } R _ { 0 j 0 k } r ^ { j } r ^ { k } + { \cal O } ( r ^ { 3 } ) ,
$$

where $v ^ { 2 } : = \delta _ { j k } \dot { r } ^ { j } \dot { r } ^ { k }$ . Substitution within the Euler–Lagrange equations produces

$$
\frac { d ^ { 2 } r ^ { j } } { d t ^ { 2 } } = - c ^ { 2 } R _ { 0 j 0 k } r ^ { k } ,
$$

the statement of the geodesic equation in Fermi normal coordinates. Because $r ^ { j } ( t )$ describes the displacement of the particle’s world line relative to $\gamma$ , it is not surprising that this takes the form of the equation of geodesic deviation, in the approximate version that was first displayed in Eq. (5.68). And this, of course, tells us once more that the Riemann tensor measures the inhomogeneities of the gravitational field, which prevent the metric of Eq. (5.78) from being constant beyond first order in the displacements $\xi ^ { j }$ , and which prevent the particle’s relative acceleration from vanishing in $\gamma$ ’s inertial frame.

<table><tr><td>Box 5.4</td><td>Fermi normal coordinates</td></tr><tr><td></td><td>We wish to show that the construction of Fermi normal coordinates (FNC) detailed in the text leads to the metric of Eq. (5.78). We employ the Riemann normal coordinates (RNC),and rely on the metric of Eq. (5.75). Our strategy is to work out the transformation between the coordinate systems,and then to calculate how the metric changes under this transformation. We suppose thatthe timelike geodesic y passes through the origin Oofthe RNC,and thatthe basis vector @ at Ois aligned with y&#x27;stangent vector.The vector basis at any other event ony is then obtained by parallel transport,and our first task is to solve the equations of parallel transport for allfour basis vectors. Setting τ = O at O, we expand the basis vectors in powers of τ, 1 τ²e(）+0(（t3）, e)(τ)=e′ω)(0)+ τ é)(0) + in which an overdot indicates diferentiation with respect to t.We invoke the definition of the RNC to set e(v)(O)= δ,nsert the expansions within the equation ofparalel transport, dsp</td></tr></table>

and solve order-by-order in $\tau$ . Because $\gamma$ is described by $\zeta ^ { 0 } = c \tau$ and $\zeta ^ { j } = 0$ in and because the Christoffel symbols are given by $\Gamma _ { \nu \lambda } ^ { \mu } = - { \textstyle { \frac { 1 } { 3 } } } ( R _ { \nu \lambda \rho } ^ { \mu } + R _ { \lambda \nu \rho } ^ { \mu } ) \zeta ^ { \rho } + O ( \zeta ^ { 2 } ) ,$ we find that $\dot { e } _ { ( \nu ) } ^ { \mu } ( 0 ) = 0$

and $\begin{array} { r } { \ddot { e } _ { ( \nu ) } ^ { \mu } ( 0 ) = \frac { 1 } { 3 } c ^ { 2 } R _ { 0 \nu 0 } ^ { \mu } , } \end{array}$ so that

$$
e _ { ( \nu ) } ^ { \mu } ( \tau ) = \delta _ { \nu } ^ { \mu } + \frac { 1 } { 6 } ( c \tau ) ^ { 2 } R _ { 0 \nu 0 } ^ { \mu } + O ( \tau ^ { 3 } ) .
$$

This equation allows us to obtain the basis vectors at $\mathcal { Q }$ .

Our next task is to launch a geodesic $\beta$ that passes through the event $\mathcal { P }$ and intersects $\gamma$ orthogonally at $\mathcal { Q }$ . This geodesic is described by relations $\zeta ^ { \mu } ( s )$ that can be obtained by integrating the geodesic equation,

$$
\frac { d ^ { 2 } \zeta ^ { \mu } } { d s ^ { 2 } } + \Gamma _ { \nu \lambda } ^ { \mu } \frac { d \zeta ^ { \nu } } { d s } \frac { d \zeta ^ { \lambda } } { d s } = 0 .
$$

Once more we express the solution as a Taylor expansion,

$$
\zeta ^ { \mu } ( s ) = \zeta ^ { \mu } ( 0 ) + s \dot { \zeta } ^ { \mu } ( 0 ) + \frac { 1 } { 2 } s ^ { 2 } \ddot { \zeta } ^ { \mu } ( 0 ) + \frac { 1 } { 6 } s ^ { 3 } \ddot { \zeta } ^ { \mu } ( 0 ) + O ( s ^ { 3 } ) ,
$$

and determine the various coefficients by inserting the expansion within the geodesic equation and solving order-by-order in $s$ . The first two coefficients, actually, are determined by the boundary conditions at $\mathcal { Q }$ : we must have that $\zeta ^ { 0 } ( 0 ) = c \tau _ { \mathcal { Q } }$ and $\zeta ^ { j } ( 0 ) = 0$ , and $\dot { \zeta } ^ { \mu } ( 0 ) \equiv n ^ { \mu } ( \mathcal { Q } )$ is given by Eq. (5.77) in terms of the direction coefficients $n ^ { j }$ and the basis vectors $e _ { ( j ) } ^ { \mu }$ obtained previously.

After some algebra we find that the solution to the geodesic equation can be expressed as

$$
\begin{array} { l } { { \displaystyle { \zeta ^ { 0 } ( s ) = ( c \tau _ { \cal Q } ) + \frac { 1 } { 3 } ( c \tau _ { \cal Q } ) R _ { 0 p 0 q } ( s n ^ { p } ) ( s n ^ { q } ) + \cdots , } } } \\ { { \displaystyle { \zeta ^ { j } ( s ) = ( s n ^ { j } ) + \frac { 1 } { 6 } ( c \tau _ { \cal Q } ) ^ { 2 } R _ { 0 p 0 } ^ { j } ( s n ^ { p } ) + \frac { 1 } { 3 } ( c \tau _ { \cal Q } ) R _ { p q 0 } ^ { j } ( s n ^ { p } ) ( s n ^ { q } ) + \cdots . } } } \end{array}
$$

This, without further ado, gives us the coordinate transformation, because the $\mathsf { F N C }$ of an event on $\beta$ are given $\mathfrak { b } y \xi ^ { 0 } = c \tau _ { \mathcal { Q } }$ and $\xi ^ { j } = s n ^ { j }$ . We have

$$
\begin{array} { l } { { \displaystyle { \zeta ^ { 0 } = \xi ^ { 0 } + \frac { 1 } { 3 } \xi ^ { 0 } R _ { 0 p 0 q } \xi ^ { p } \xi ^ { q } + \cdots , } } } \\ { { \displaystyle { \zeta ^ { j } = \xi ^ { j } + \frac { 1 } { 6 } ( \xi ^ { 0 } ) ^ { 2 } R _ { 0 p 0 } ^ { j } \xi ^ { p } + \frac { 1 } { 3 } \xi ^ { 0 } R _ { p q 0 } ^ { j } \xi ^ { p } \xi ^ { q } + \cdots , } } } \end{array}
$$

and the metric of Eq. (5.78) is obtained by inserting these expressions within

$$
g _ { \mu \nu } ( \mathsf { F N C } ) = g _ { \lambda \rho } ( \mathsf { R N C } ) \frac { \partial \zeta ^ { \lambda } } { \partial \xi ^ { \mu } } \frac { \partial \zeta ^ { \rho } } { \partial \xi ^ { \nu } } ,
$$

the standard transformation law for the components of the metric tensor. The manipulations that lead to Eq. (5.78) are slightly tedious, but perfectly straightforward. A point of subtlety concerns the components of the Riemann tensor, which are evaluated at $\mathcal { O }$ in both the coordinate transformation and the RNC form of the metric. It is easy to see, however, that a displacement to $\mathcal { Q }$ does not change the metric components to second order in $\zeta ^ { \mu }$ , nor the coordinate transformation to third order in $\xi ^ { \mu }$ . The Riemann tensor, therefore, can be safely evaluated at $\mathcal { Q }$ instead of $\mathcal { O }$ , and because $\mathcal { Q }$ is an arbitrary event $0 \mathsf { n } \gamma$ , we conclude that the Riemann tensor is in fact a function of $\tau : = \xi ^ { 0 } / c$ on the world line.

# 5.3 Physics in curved spacetime

# 5.3.1 From flat to curved spacetime

The rules to modify the laws of physics from their flat-spacetime formulation so that they hold in curved spacetime are exceedingly simple: start from a tensorial equation valid in any Lorentz frame, replace all occurrences of the Minkowski metric by $g _ { \alpha \beta }$ , and replace all partial derivatives by covariant derivatives; the result is a tensorial law valid in curved spacetime. The key to these rules is the important fact that according to the Einstein equivalence principle, the special-relativistic formulation of any law of physics is valid locally in any inertial frame attached to a freely-moving observer. All the hard work goes into rewriting this law in a form that is valid in any other reference frame, and in any coordinate system. And as we just saw, this work is really not that hard.

We prepare the way for this reformulation by recalling some useful mathematics from the preceding section. As we have seen, in the local (Fermi) coordinates $\xi ^ { \mu }$ , the metric on a timelike geodesic $\gamma$ is equal to the Minkowski metric $\eta _ { \mu \nu }$ and the Christoffel symbols $\Gamma _ { \mu \nu } ^ { \lambda }$ vanish. There exists a transformation between the local coordinates $\xi ^ { \mu }$ and any system of global coordinates $x ^ { \alpha }$ ; we write it as $\xi ^ { \mu } = f ^ { \mu } ( x ^ { \alpha } )$ , and these relations imply $d \xi ^ { \mu } =$ $( \partial f ^ { \mu } / \partial x ^ { \alpha } ) d x ^ { \alpha }$ . The inverse transformation is $x ^ { \alpha } = F ^ { \alpha } ( \xi ^ { \mu } )$ , and these relations imply $d x ^ { \alpha } = ( \partial F ^ { \alpha } / \partial \xi ^ { \mu } ) d \xi ^ { \mu }$ . It is easy to verify that

$$
\frac { \partial F ^ { \alpha } } { \partial \xi ^ { \mu } } \frac { \partial f ^ { \mu } } { \partial x ^ { \beta } } = \delta _ { \beta } ^ { \alpha } , \qquad \frac { \partial f ^ { \mu } } { \partial x ^ { \alpha } } \frac { \partial F ^ { \alpha } } { \partial \xi ^ { \nu } } = \delta _ { \nu } ^ { \mu } ,
$$

follows from the preceding equations.

Up to terms involving the Riemann tensor, the spacetime interval in $\gamma$ ’s immediate vicinity is given by $d s ^ { 2 } = \eta _ { \mu \nu } d \xi ^ { \mu } d \xi ^ { \nu }$ in the local coordinates. In the global coordinates it is $d s ^ { 2 } = g _ { \alpha \beta } d x ^ { \alpha } d x ^ { \beta }$ , where

$$
g _ { \alpha \beta } = \eta _ { \mu \nu } { \frac { \partial f ^ { \mu } } { \partial x ^ { \alpha } } } { \frac { \partial f ^ { \nu } } { \partial x ^ { \beta } } }
$$

is an expression for the metric tensor. It is easy to verify that

$$
g ^ { \alpha \beta } = \eta ^ { \mu \nu } { \frac { \partial { \cal F } ^ { \alpha } } { \partial \xi ^ { \mu } } } { \frac { \partial { \cal F } ^ { \beta } } { \partial \xi ^ { \nu } } }
$$

is an appropriate expression for the inverse metric. We can compute the Christoffel symbols $\Gamma _ { \beta \gamma } ^ { \alpha }$ by differentiating $g _ { \alpha \beta }$ and inserting the result into Eq. (5.34). After simplification we obtain

$$
\Gamma _ { \beta \gamma } ^ { \alpha } = \frac { \partial F ^ { \alpha } } { \partial \xi ^ { \mu } } \frac { \partial ^ { 2 } f ^ { \mu } } { \partial x ^ { \beta } \partial x ^ { \gamma } } .
$$

To motivate the rules listed at the beginning of this section we examine the simple case of a particle moving freely in a curved spacetime. We already know the final outcome: this particle will move on a geodesic of the spacetime. We shall deduce this on the basis that in flat spacetime, a particle moving freely does so on a straight path. In special relativity, therefore, the particle’s velocity vector $u ^ { \mu }$ satisfies ${ d u ^ { \mu } } / { d \tau } = 0$ .

To generalize this law to curved spacetime we invoke the principle of equivalence and affirm that ${ d u ^ { \mu } } / { d \tau } = 0$ continues to apply locally in an inertial frame attached to any freelymoving observer. (This observer may or may not be moving together with the particle; we merely require that particle and observer come together at least once, at some selected event in spacetime.) In this frame $u ^ { \mu } = d \xi ^ { \mu } / d \tau$ , and proper time $\tau$ continues to be defined in terms of the spacetime interval $d s ^ { 2 } \colon d \tau = \sqrt { - d s ^ { 2 } } / c$ . We next carry out a transformation to the global coordinates $x ^ { \alpha }$ . We have that

$$
u ^ { \mu } = { \frac { \partial f ^ { \mu } } { \partial x ^ { \alpha } } } u ^ { \alpha } ,
$$

where $u ^ { \alpha } = d x ^ { \alpha } / d \tau$ are the components of the velocity vector in the global coordinates. Differentiation with respect to $\tau$ gives

$$
\begin{array} { c } { \displaystyle \frac { d u ^ { \mu } } { d \tau } = \frac { \partial f ^ { \mu } } { \partial x ^ { \alpha } } \frac { d u ^ { \alpha } } { d \tau } + \frac { \partial ^ { 2 } f ^ { \mu } } { \partial x ^ { \beta } \partial x ^ { \gamma } } u ^ { \beta } u ^ { \gamma } } \\ { = \displaystyle \frac { \partial f ^ { \mu } } { \partial x ^ { \alpha } } \bigg ( \frac { d u ^ { \alpha } } { d \tau } + \frac { \partial F ^ { \alpha } } { \partial \xi ^ { \nu } } \frac { \partial ^ { 2 } f ^ { \nu } } { \partial x ^ { \beta } \partial x ^ { \gamma } } u ^ { \beta } u ^ { \gamma } \bigg ) , } \end{array}
$$

where we used Eq. (5.82) in the second step. Invoking now Eq. (5.85), we recognize

$$
{ \frac { d u ^ { \alpha } } { d \tau } } + \Gamma _ { \beta \gamma } ^ { \alpha } u ^ { \beta } u ^ { \gamma } = { \frac { D u ^ { \alpha } } { d \tau } }
$$

within the brackets, and we conclude that $d u ^ { \mu } / d \tau = 0$ in the local coordinates becomes $D u ^ { \alpha } / d \tau = 0$ in the global coordinates. As expected, the particle moves on a geodesic of the curved spacetime.

The generalization of any other law of physics from flat to curved spacetime can always be accomplished by systematically running through the steps outlined in the preceding paragraph. The outcome is always the set of rules listed at the beginning of the section:

$$
\eta _ { \mu \nu }  g _ { \alpha \beta } , \qquad \partial _ { \mu }  \nabla _ { \alpha } .
$$

One can, in fact, obtain the rules without calculation. Instead of the route adopted previously, we could have started from the statement that $d u ^ { \mu } / d \tau = 0$ holds in the local coordinates $\xi ^ { \mu }$ when the particle encounters the observer on the reference geodesic $\gamma$ . We could have modified this immediately to $D u ^ { \mu } / d \tau = 0$ , observing that the two forms differ by Christoffel symbols that vanish on $\gamma$ . But this equation is in proper tensorial form in curved spacetime, and a transformation to any other coordinates system $x ^ { \alpha }$ will preserve its form; the equation becomes $D u ^ { \alpha } / d \tau = 0$ in the new coordinates, and once more we recover the geodesic equation.

As another application of the rules we may generalize Eq. (4.16) from flat to curved spacetime. The result is immediate, and we obtain the statement that

$$
E _ { \mathrm { o b s } } = - g _ { \alpha \beta } p ^ { \alpha } u _ { \mathrm { o b s } } ^ { \beta }
$$

is the energy of a particle with momentum $p ^ { \alpha }$ as measured by an observer moving with velocity $u _ { \mathrm { o b s } } ^ { \alpha }$ . This equation applies to massive particles as well as photons. In the case of a massive particle, the momentum vector is defined as in flat spacetime, $p ^ { \alpha } = m u ^ { \alpha }$ , where $m$ is the particle’s rest-mass and $u ^ { \alpha }$ is its own velocity vector. In the case of a photon, Eq. (5.90) generalizes Eq. (4.26).

It should be noted that the rule $\partial _ { \mu } \to \nabla _ { \alpha }$ always works when one generalizes a law of physics that involves first derivatives only. When second derivatives are involved, however, the rule can lead to ambiguities. This is because covariant derivatives do not commute when they act on vectors and tensors. Different orderings of $\partial _ { \mu \nu }$ will therefore lead to different prescriptions that differ from each other by terms involving the Riemann tensor. Such ambiguities can usually be resolved by retreating to a more fundamental, first-order formulation of the law under consideration. When such a formulation does not exist, however, the ambiguity must be resolved differently, and this may require experimental input.

# 5.3.2 Hydrodynamics in curved spacetime

The curved-spacetime formulation of the laws of fluid mechanics involves the same variables as in flat spacetime, and most of these are defined in precisely the same way. Going through the list, we have the velocity field $u ^ { \alpha }$ , proper mass density $\rho$ , proper density of internal (thermodynamic) energy $\epsilon$ , proper density of total energy $\mu = \rho c ^ { 2 } + \epsilon$ , pressure $p$ , and mass current $j ^ { \alpha } = \rho u ^ { \alpha }$ . The densities are all measured in an inertial frame that is momentarily comoving with a selected fluid element; this frame is attached to an observer moving freely in the gravitational field. We also have the fluid’s energy-momentum tensor $T ^ { \alpha \beta }$ , but its relation to the other fluid variables must be modified from Eq. (4.50) according to the rules of Eq. (5.89). We now have

$$
T ^ { \alpha \beta } = ( \mu + p ) u ^ { \alpha } u ^ { \beta } / c ^ { 2 } + p g ^ { \alpha \beta } ,
$$

which features the spacetime metric $g _ { \alpha \beta }$ instead of $\eta _ { \mu \nu }$ .

The statement of mass conservation now takes the form

$$
\nabla _ { \alpha } j ^ { \alpha } = 0 ,
$$

the curved-spacetime generalization of Eq. (4.47). Using Eq. (5.40) this can also be expressed as

$$
\partial _ { \alpha } \bigl ( \sqrt { - g } j ^ { \alpha } \bigr ) = 0 ,
$$

and the factor of $\scriptstyle { \sqrt { - g } }$ accounts for the dependence of volume elements on the metric determinant. Substitution of $j ^ { \alpha } = \rho u ^ { \alpha }$ into Eq. (5.92) yields

$$
\frac { d \rho } { d \tau } + \rho \nabla _ { \alpha } u ^ { \alpha } = 0 ,
$$

which is the generalization of Eq. (4.53). Here, $d \rho / d \tau = u ^ { \alpha } \nabla _ { \alpha } \rho$ is the (Lagrangian) derivative of the mass density along the world line of a selected fluid element.

The equation of energy-momentum conservation becomes

$$
\begin{array} { r } { \nabla _ { \beta } T ^ { \alpha \beta } = 0 , } \end{array}
$$

the generalization of the flat-spacetime version of Eq. (4.49). Insertion of Eq. (5.91) produces

$$
\frac { d \mu } { d \tau } + ( \mu + p ) \nabla _ { \beta } u ^ { \beta } = 0
$$

and

$$
( \mu + p ) \frac { D u ^ { \alpha } } { d \tau } + c ^ { 2 } \big ( g ^ { \alpha \beta } + u ^ { \alpha } u ^ { \beta } / c ^ { 2 } \big ) \nabla _ { \beta } p = 0 .
$$

The first equation gives rise to

$$
\rho \frac { d \epsilon } { d \tau } - ( \epsilon + p ) \frac { d \rho } { d \tau } = 0
$$

if we make use of Eq. (5.92), and we recognize this from Eq. (4.57) as a statement of the first law of thermodynamics for isentropic flows. The second equation is the curvedspacetime version of Euler’s equation. In the first term we recognize $D u ^ { \alpha } / d \tau = u ^ { \beta } \nabla _ { \beta } u ^ { \alpha }$ as the covariant acceleration of a selected fluid element, which would be zero if the fluid element were moving on a geodesic of the curved spacetime. This, however, is prevented by the pressure forces acting within the fluid; the fluid element is not moving freely in the gravitational field.

<table><tr><td>Box 5.5</td><td>Hydrostatic equilibrium</td></tr></table>

As a simple application of the laws of fluid mechanics in curved spacetime, we examine a static fluid configuration in a static spacetime. This fluid is in hydrostatic equilibrium, and we wish to find the relationship between the fluid’s variables and the gravitational potential.

The metric of a static spacetime can always be put in the form

$$
d s ^ { 2 } = - e ^ { - 2 \Phi / c ^ { 2 } } d ( c t ) ^ { 2 } + g _ { j k } d x ^ { j } d x ^ { k } ,
$$

in terms of a gravitational potential $\Phi ( { \boldsymbol { x } } ^ { j } )$ and a spatial metric $g _ { j k }$ that also depends on the spatial coordinates $x ^ { j }$ . The metric, and all the fluid variables, do not depend on the time coordinate $t$ . In a weak-field situation we would have $\Phi / c ^ { 2 } \ll 1$ , and we would approximate $g _ { 0 0 }$ by $- 1 + 2 \Phi / c ^ { 2 } + \cdots ;$ if we set $\Phi = U$ and $g _ { j k } = \delta _ { j k }$ we recover the Newtonian metric of Eq. (5.12).

In a static configuration the fluid elements do not move in the spatial directions, and the only nonvanishing component of the fluid’s velocity field is $u ^ { 0 }$ . The normalization condition $g _ { \alpha \beta } u ^ { \alpha } u ^ { \beta } = - c ^ { 2 }$ implies that $u ^ { 0 } = c e ^ { \Phi / c ^ { 2 } }$ . This velocity field is not geodesic. It is easy to verify that the covariant acceleration is given by $D u ^ { \alpha } / d \tau = c ^ { 2 } e ^ { 2 \Phi / c ^ { 2 } } \Gamma _ { 0 0 } ^ { \alpha } ,$ and a computation of the Christoffel symbols shows that $\Gamma _ { 0 0 } ^ { j } = - c ^ { - 2 } e ^ { - 2 \Phi / c ^ { 2 } } g ^ { j k } \partial _ { k } \Phi$ 00are the relevant, non-vanishing components. From this we obtain

$$
\frac { D u ^ { j } } { d \tau } = - g ^ { j k } \partial _ { k } \Phi
$$

for the spatial components of the covariant acceleration.

The fluid elements are accelerated because they are are not moving freely in the gravitational field. Instead they are kept in place by the pressure forces acting within the fluid, which support it against gravity. The equation of hydrostatic equilibrium follows as a direct consequence of Euler’s equation (5.97), which reduces, in our case, to $- ( \mu + p ) g ^ { j k } \partial _ { k } \Phi + c ^ { 2 } g ^ { j k } \partial _ { k } p = 0 .$ After lowering the $j$ index, we arrive at

$$
( \rho + p / c ^ { 2 } + \epsilon / c ^ { 2 } ) \partial _ { j } \Phi = \partial _ { j } p .
$$

This is the (exact) relativistic statement of hydrostatic equilibrium. In Newtonian situations we may identify $\Phi$ with the Newtonian potential $U$ and neglect the $p / c ^ { 2 } \mathsf { a n d } \epsilon / c ^ { 2 }$ terms on the left-hand side; this gives rise to the familiar $\rho \nabla U = \nabla p$ .

# 5.3.3 Electrodynamics in curved spacetime

The curved-spacetime formulation of Maxwell’s theory involves an electromagnetic field tensor $F ^ { \alpha \beta }$ and a charge-current vector $j _ { e } ^ { \alpha }$ . The statement of local charge conservation is $\nabla _ { \alpha } j _ { e } ^ { \alpha } = 0$ , and Maxwell’s equations take the form

$$
\nabla _ { \beta } F ^ { \alpha \beta } = \mu _ { 0 } j _ { e } ^ { \alpha } , \qquad \nabla _ { \alpha } F _ { \beta \gamma } + \nabla _ { \gamma } F _ { \alpha \beta } + \nabla _ { \beta } F _ { \gamma \alpha } = 0 .
$$

The field tensor can be expressed in terms of a vector potential $A ^ { \alpha }$ . The relation is

$$
F _ { \alpha \beta } = \nabla _ { \alpha } A _ { \beta } - \nabla _ { \beta } A _ { \alpha } ,
$$

and this assignment ensures that the homogeneous Maxwell equations are automatically satisfied. The field tensor is left invariant under a gauge transformation of the form $A _ { \alpha } $ $A _ { \alpha } + \nabla _ { \alpha } \chi$ , where $\chi$ is any scalar function of the spacetime coordinates $x ^ { \alpha }$ .

We may turn the inhomogeneous Maxwell equations into a set of wave equations for the vector potential. To achieve this we adopt the curved-spacetime version of the Lorenz gauge, in which the potential is required to satisfy the condition

$$
\nabla _ { \alpha } A ^ { \alpha } = 0 .
$$

We first insert Eq. (5.100) into the first of Eqs. (5.99) and get

$$
\nabla _ { \beta } \nabla ^ { \alpha } A ^ { \beta } - \nabla _ { \beta } \nabla ^ { \beta } A ^ { \alpha } = \mu _ { 0 } j _ { e } ^ { \alpha } .
$$

The second term on the left-hand side involves the differential operator $\nabla _ { \beta } \nabla ^ { \beta } = g ^ { \beta \gamma } \nabla _ { \beta } \nabla _ { \gamma }$ , which reduces to $\eta ^ { \mu \nu } \partial _ { \mu } \partial _ { \nu } = - c ^ { - 2 } \partial ^ { 2 } / \partial t ^ { 2 } + \nabla ^ { 2 }$ in flat spacetime; this is the curvedspacetime version of the wave operator, which we denote $\ \sqsubseteq _ { g }$ . The first term can be simplified if we switch the order of the covariant derivatives, using the Riemann-tensor identity of Eq. (5.57). We have $\nabla _ { \beta } \nabla _ { \alpha } A ^ { \beta } = \nabla _ { \alpha } \nabla _ { \beta } A ^ { \beta } + R _ { \nu \beta \alpha } ^ { \beta } A ^ { \nu }$ , and the first term can be eliminated by virtue of the Lorenz-gauge condition. The second term involves the contraction of the Riemann tensor, which gives rise to the Ricci tensor $R _ { \nu \alpha } = R _ { \alpha \nu }$ . All in all we have obtained

$$
\begin{array} { r } { \bigsqcup _ { g } \mathcal { A } ^ { \alpha } - R _ { \beta } ^ { \alpha } \mathcal { A } ^ { \beta } = - \mu _ { 0 } j _ { e } ^ { \alpha } , } \end{array}
$$

which is the desired set of (coupled) wave equations for $A ^ { \alpha }$ . We recall that $\begin{array} { r } { \begin{array} { r } { \boxed { \begin{array} { r l } \end{array} } : = g ^ { \beta \gamma } \nabla _ { \beta } \nabla _ { \gamma } } \end{array} } \end{array}$ is the covariant wave operator in curved spacetime.

We observe that Eq. (5.103) cannot be obtained directly from Eq. (4.67) by applying the rules of Eq. (5.89). The reason for this was already stated: the wave equation is a second-order differential equation, and the rules are ambiguous for such equations; different orderings of the derivatives lead to equations that differ from each other by Riemann-tensor terms. In the present case the ambiguity was resolved because the path leading to Eq. (5.103) originated from the first-order formulation of Maxwell’s equations.

The energy-momentum tensor of the electromagnetic field is now

$$
T ^ { \alpha \beta } = \frac { 1 } { \mu _ { 0 } } \Big ( F ^ { \alpha \mu } F _ { \mu } ^ { \beta } - \frac { 1 } { 4 } g ^ { \alpha \beta } F _ { \mu \nu } F ^ { \mu \nu } \Big ) ,
$$

and the exchange of energy and momentum between the field and the charge distribution is described by

$$
\nabla _ { \beta } T ^ { \alpha \beta } = - F _ { \beta } ^ { \alpha } j _ { e } ^ { \beta } .
$$

This equation follows as a consequence of Maxwell’s equations; the term on the right-hand side is (minus) the force density exerted on the charged fluid by the field.

<table><tr><td>Box 5.6</td><td>Geometric optics</td></tr><tr><td></td><td>Maxwells equations imply that photons move on geodesics of a curved spacetime.In this context the term &quot;photon&quot; is employed in a classical sense,and designates a fictitious particle that follows the path of light rays.This is the domain of te geometric-optics approximation to Maxwel&#x27;s theory, which is applicable when the characteristic wavelength associated with a field configuration is much smaller than any other scale of relevance,including the curvature scale set by the Riemann tensor. In our analysis we take these external scales to be of order unity while the wavelength is taken to be much smaller than this.</td></tr></table>

The geometric-optics approximation is built into the following ansatz for the vector potential:

$$
{ \cal A } ^ { \alpha } = \big [ a ^ { \alpha } + i \epsilon b ^ { \alpha } + O ( \epsilon ^ { 2 } ) \big ] e ^ { i S / \epsilon } .
$$

The prefactor within square brackets is a slowly-varying, complex amplitude, while the exponential factor contains a rapidly-varying, real phase $S / \epsilon$ . The constant $\epsilon$ is a book-keeping parameter that we take to be small during our manipulations; at the end of our calculations we reset it to $\epsilon = 1$ , so that $S$ becomes the actual phase function. The amplitudes $a ^ { \alpha }$ and $b ^ { \alpha }$ , and the phase $S ,$ all depend on the spacetime coordinates $x ^ { \alpha }$ . It is understood that only the real part of $A ^ { \alpha }$ is physically significant.

In a local inertial frame attached to a freely-moving observer, the electromagnetic wave represented by $A ^ { \alpha }$ looks like a plane wave, and the phase function can be locally approximated by $S =$ $- ( \omega / c ) \xi ^ { 0 } + { \pmb k } \cdot { \pmb \xi } = k _ { \mu } \xi ^ { \mu }$ , where $k ^ { \mu } = ( \omega / c , k ) = p ^ { \mu } / \hbar$ is the wave vector, related to the photon’s momentum $p ^ { \mu }$ by a factor of $\hbar$ . The wave vector may be defined by $k _ { \mu } = \partial _ { \mu } S$ in the local coordinates, and in the global coordinates $x ^ { \alpha }$ we shall have

$$
k _ { \alpha } = \partial _ { \alpha } S .
$$

The vector $k ^ { \alpha }$ is tangent to light rays, and we wish to show that it satisfies the null condition $k _ { \alpha } k ^ { \alpha } = 0$ as well as the geodesic equation $k ^ { \beta } \nabla _ { \beta } k ^ { \alpha } = 0$ .

Differentiation of the vector potential gives

$$
\nabla _ { \beta } A ^ { \alpha } = \Biggl [ \frac { i } { \epsilon } k _ { \beta } a ^ { \alpha } - k _ { \beta } b ^ { \alpha } + \nabla _ { \beta } a ^ { \alpha } + O ( \epsilon ) \Biggr ] e ^ { i S / \epsilon } .
$$

At order $\epsilon ^ { - 1 }$ the Lorenz-gauge condition of Eq. (5.101) implies that $k _ { \alpha } a ^ { \alpha } = 0$ , and at order $\epsilon ^ { 0 }$ we find that $k _ { \alpha } b ^ { \alpha } = \nabla _ { \alpha } a ^ { \alpha }$ ; the potential is orthogonal to the wave vector at leading-order only. A second differentiation reveals that

$$
\begin{array} { l } { \displaystyle \Xi _ { g } A ^ { \alpha } = \left\{ - \frac { 1 } { \epsilon ^ { 2 } } ( k _ { \beta } k ^ { \beta } ) a ^ { \alpha } + \frac { i } { \epsilon } \Big [ ( k _ { \beta } k ^ { \beta } ) b ^ { \alpha } + 2 k ^ { \beta } \nabla _ { \beta } a ^ { \alpha } + ( \nabla _ { \beta } k ^ { \beta } ) a ^ { \alpha } \Big ] + O ( \epsilon ^ { 0 } ) \right\} e ^ { i S / \epsilon } . } \end{array}
$$

On the other hand, $R _ { \beta } ^ { \alpha } A ^ { \beta } = O ( \epsilon ^ { 0 } )$ , and Maxwell’s equations in the absence of charges imply that $\Pi _ { g } A ^ { \alpha }$ must vanish at orders $\epsilon ^ { - 2 } \mathsf { a n d } \epsilon ^ { - 1 }$ . At order $\epsilon ^ { - 2 }$ we obtain our null condition

$$
k _ { \alpha } k ^ { \alpha } = 0 ,
$$

and at order $\epsilon ^ { - 1 }$ we get a differential equation for the amplitude $\begin{array} { r } { a ^ { \alpha } { : } k ^ { \beta } \nabla _ { \beta } a ^ { \alpha } = - \frac { 1 } { 2 } ( \nabla _ { \beta } k ^ { \beta } ) a ^ { \alpha } } \end{array}$ .

The geodesic equation follows immediately from the definition of $k _ { \alpha }$ and the null condition. Differentiation of the null condition yields $0 = \nabla _ { \beta } ( k _ { \alpha } k ^ { \alpha } ) = 2 k ^ { \alpha } \nabla _ { \beta } k _ { \alpha } = 2 k ^ { \alpha } \nabla _ { \beta } \nabla _ { \alpha } S .$ We next use the fact that two covariant derivatives commute when they act on a scalar function $S ,$ and rewrite our result as $0 = 2 k ^ { \alpha } \nabla _ { \alpha } \nabla _ { \beta } S = 2 k ^ { \alpha } \nabla _ { \alpha } k _ { \beta }$ . This is

$$
k ^ { \alpha } \nabla _ { \alpha } k ^ { \beta } = 0 ,
$$

the statement of the geodesic equation for light rays.

Very little needs to be changed when we generalize the description of point particles from Minkowski spacetime to curved spacetime. In the global coordinates $x ^ { \alpha }$ a particle moves on a world line $r ^ { \alpha } ( \tau )$ parameterized by proper time $\tau$ , its velocity vector is $u ^ { \alpha } = d r ^ { \alpha } / d \tau$ , and its mass density $\rho$ continues to be represented by a Dirac delta function. This, however, must now come with an additional factor of $\sqrt { - g }$ , to ensure that integrals such as

$$
\int f ( x ^ { \alpha } ) { \frac { \delta ( x ^ { \mu } - r ^ { \mu } ) } { \sqrt { - g } } } d V
$$

involve the correct, invariant volume element $d V : = { \sqrt { - g } } d ^ { 4 } x$ . The integral, we recall, returns $f ( r ^ { \alpha } )$ if the event $r ^ { \mu }$ is contained within the domain of integration, and zero otherwise.

The mass density of a point particle of mass $m$ is therefore given by

$$
\rho ( x ^ { \alpha } ) = m c \int { \frac { \delta \big ( x ^ { \mu } - r ^ { \mu } ( \tau ) \big ) } { \sqrt { - g } } } d \tau ,
$$

its mass current by

$$
j ^ { \alpha } = m c \int u ^ { \alpha } \frac { \delta \bigl ( x ^ { \mu } - r ^ { \mu } ( \tau ) \bigr ) } { \sqrt { - g } } d \tau ,
$$

and its energy-momentum tensor by

$$
T ^ { \alpha \beta } = m c \int u ^ { \alpha } u ^ { \beta } { \frac { \delta { \bigl ( } x ^ { \mu } - r ^ { \mu } ( \tau ) { \bigr ) } } { \sqrt { - g } } } d \tau .
$$

The delta function satisfies the distributional identity

$$
u ^ { \alpha } \partial _ { \alpha } \delta \bigl ( x ^ { \mu } - r ^ { \mu } ( \tau ) \bigr ) = - \frac { d } { d \tau } \delta \bigl ( x ^ { \mu } - r ^ { \mu } ( \tau ) \bigr ) ,
$$

which was first established in Sec. 4.4.

With simple manipulations we can verify that the mass current has a vanishing divergence:

$$
\begin{array} { l } { { \displaystyle \nabla _ { \alpha } j ^ { \alpha } = \frac { 1 } { \sqrt { - g } } \partial _ { \alpha } \big ( \sqrt { - g } j ^ { \alpha } \big ) } } \\ { { \displaystyle \quad = \frac { m c } { \sqrt { - g } } \int u ^ { \alpha } \partial _ { \alpha } \delta ( x ^ { \mu } - r ^ { \mu } ) d \tau } } \\ { { \displaystyle \quad = - \frac { m c } { \sqrt { - g } } \int \frac { d } { d \tau } \delta ( x ^ { \mu } - r ^ { \mu } ) d \tau } } \\ { { \displaystyle \quad = 0 . } } \end{array}
$$

For the divergence of the energy-momentum tensor we get

$$
\begin{array} { l } { { \nabla _ { \beta } T ^ { \alpha \beta } = \partial _ { \beta } T ^ { \alpha \beta } + \Gamma _ { \gamma \beta } ^ { \beta } T ^ { \alpha \gamma } + \Gamma _ { \gamma \beta } ^ { \alpha } T ^ { \gamma \beta } } } \\ { { \ = { \frac { 1 } { \sqrt { - g } } } \partial _ { \beta } \big ( \sqrt { - g } T ^ { \alpha \beta } \big ) + \Gamma _ { \beta \gamma } ^ { \alpha } T ^ { \beta \gamma } } } \\ { { \ = { \frac { m c } { \sqrt { - g } } } \displaystyle \int u ^ { \alpha } u ^ { \beta } \partial _ { \beta } \delta ( x ^ { \mu } - r ^ { \mu } ) d \tau + m c \int \Gamma _ { \beta \gamma } ^ { \alpha } u ^ { \beta } u ^ { \gamma } { \frac { \delta ( x ^ { \mu } - r ^ { \mu } ) } { \sqrt { - g } } } d \tau ; } } \end{array}
$$

this becomes

$$
\nabla _ { \beta } T ^ { \alpha \beta } = m c \int \left( { \frac { d u ^ { \alpha } } { d \tau } } + \Gamma _ { \beta \gamma } ^ { \alpha } u ^ { \beta } u ^ { \gamma } \right) { \frac { \delta ( x ^ { \mu } - r ^ { \mu } ) } { \sqrt { - g } } } d \tau
$$

when we use the distributional identity within the first integral and integrate by parts. We recognize $D u ^ { \alpha } / d \tau$ within the integral, and deduce that $D u ^ { \alpha } / d \tau = 0$ when the particle does not exchange energy and momentum with an external agent (through the action of a force). In other words, the statement $\nabla _ { \beta } T ^ { \alpha \beta } = 0$ implies that the particle is moving freely, and under these circumstances we recover the fact that the particle moves on a geodesic of the curved spacetime.

# 5.4 Einstein field equations

The Einstein field equations relate the curvature of spacetime to the distribution of matter within spacetime. They read

$$
G ^ { \alpha \beta } = { \frac { 8 \pi G } { c ^ { 4 } } } T ^ { \alpha \beta } ,
$$

with the Einstein curvature tensor, Eq. (5.71), on the left-hand side, and the total energymomentum tensor of all forms of matter (and fields) on the right-hand side. Taking into account the symmetries of the Einstein and energy-momentum tensors, the Einstein field equations are a set of ten second-order, partial differential equations for the metric tensor $g _ { \alpha \beta }$ . The equations are all coupled, and they are highly non-linear in the metric and its first derivatives; they are, however, linear in the second derivatives of the metric tensor.

A naive counting of the number of equations might suggest that, given suitable initial and boundary conditions for the metric, the solution to the Einstein field equations should be unique. This suggestion, however, is false, as the freedom to perform coordinate transformations must be retained; two metrics $g _ { \alpha \beta }$ and $g _ { \mu \nu } ^ { \prime }$ related to each other by a coordinate transformation should both be valid solutions to the field equations. This freedom is guaranteed by the contracted Bianchi identities,

$$
\nabla _ { \beta } G ^ { \alpha \beta } = 0 ,
$$

which reveal that of the ten field equations, only six are truly independent from each other. The Bianchi identities, together with the field equations, imply that

$$
\begin{array} { r } { \nabla _ { \beta } T ^ { \alpha \beta } = 0 ; } \end{array}
$$

the energy-momentum tensor must have a vanishing divergence. This is a local statement of energy-momentum conservation for the matter (and field) distribution. This equation is of fundamental importance, because it determines (partially, if not fully) the equations of motion for the matter variables that make up the energy-momentum tensor. We witnessed this connection in the specific context of fluid mechanics in Sec. 5.3: we saw that the relativistic Euler equation (5.97) follows directly from Eq. (5.114).

The Einstein field equations have a fascinating structure. In the famous words of John Wheeler, the field equations (5.112) tell spacetime how to curve, given a description of the matter distribution through its energy-momentum tensor. At the same time, Eq. (5.114) tells matter how to move in a specified spacetime. But these equations are not independent, for they are intimately connected through the contracted Bianchi identities. Matter has no latitude: it must move in accordance to the spacetime that it produces.

This structure is unique to general relativity. In Maxwell’s electrodynamics, for example, one can prescribe the motion of charges and determine the electromagnetic field that corresponds to this assumed distribution; no equations are violated when the charges do not respond to the field in a self-consistent manner, because external agents can always be introduced with the specific purpose of keeping the charges on their prescribed trajectories. In general relativity the motion of masses cannot be prescribed; it is necessarily dictated by the Einstein field equations. Any attempt to keep the masses on prescribed trajectories would involve external agents that are themselves a significant source of mass and energy; their contribution to the total $T ^ { \alpha \beta }$ would necessarily modify the spacetime in which the masses are moving.

In Einstein’s theory the local statement of energy-momentum conservation, Eq. (5.114), is a consequence of the field equations, and the behavior of matter is intimately tied to the spacetime that the matter generates. Equation (5.114), however, should be expected to hold also in alternative theories of gravitation, in which the relationship between matter and curvature might involve additional mediators (such as a scalar field, in the case of scalar–tensor theories). The reason for this, as we shall elaborate below, resides in the fact that Eq. (5.114) is a direct consequence of the invariance of the matter action under general coordinate transformations. Because this principle of general covariance is a central aspect of any metric theory of gravitation (not just Einstein’s), $\nabla _ { \beta } T ^ { \alpha \beta } = 0$ is a fundamental equation that transcends its connection to the Einstein field equations and the Bianchi identities.

The equations of general relativity can be derived from an action principle. The total action $S$ involves a gravitational piece given by the Hilbert action

$$
S _ { \mathrm { g r a v } } = { \frac { c ^ { 3 } } { 1 6 \pi G } } \int R d V ,
$$

where $R$ is the Ricci scalar and $d V = { \sqrt { - g } } d ^ { 4 } x$ is the invariant volume element, as well as a matter piece given by

$$
S _ { \mathrm { m a t t e r } } = \int { \mathcal { L } } d V ,
$$

where $\mathcal { L }$ is the Lagrangian density for all matter (and field) variables. The Einstein tensor results from the functional variation of the gravitational action:

$$
\frac { \delta S _ { \mathrm { g r a v } } } { \delta g _ { \alpha \beta } } = - \frac { c ^ { 3 } } { 1 6 \pi G } G ^ { \alpha \beta } .
$$

The energy-momentum tensor, on the other hand, is defined by

$$
\frac { \delta S _ { \mathrm { m a t t e r } } } { \delta g _ { \alpha \beta } } = \frac { 1 } { 2 c } T ^ { \alpha \beta } .
$$

The Einstein field equations then follow from the requirement that $\delta ( S _ { \mathrm { g r a v } } + S _ { \mathrm { m a t t e r } } ) = 0$ under an arbitrary variation of the metric tensor. However, when we consider a specific variation $\delta g _ { \alpha \beta }$ induced by a coordinate transformation, $\delta S _ { \mathrm { g r a v } } = 0$ must follow as a matter of identity; it can be shown that the invariance of $S _ { \mathrm { g r a v } }$ under such a variation gives rise to the Bianchi identities $\nabla _ { \beta } G ^ { \alpha \beta } = 0$ . And similarly, the invariance of $S _ { \mathrm { m a t t e r } }$ under such a variation gives rise to Eq. (5.114). This result is the source of our earlier claim that $\nabla _ { \beta } T ^ { \alpha \beta } = 0$ must hold in any metric theory of gravitation; it is a direct consequence of the principle of general covariance.

# 5.5 Linearized theory

The field equations of general relativity are exceedingly complicated, and it is a genuine miracle that so many exact solutions have been found over the years; but it is perhaps not a surprise that so few of these solutions possess an immediate physical significance. In the next section we shall explore the most famous of these exact solutions, the Schwarzschild metric, which describes the vacuum exterior to any spherical mass distribution. In this section we examine an approximate version of Einstein’s theory, which applies when gravity is everywhere weak. As we shall see, there is more to weak-field gravity than was uncovered by Newton, and this exploration of the linearized theory will help us gain insight into the dynamical structure of general relativity. We warn the reader that our emphasis here is on conceptual matters; in the next chapters we develop more efficient ways of solving the Einstein field equations in weak-field situations, and we revisit topics introduced here with more depth and precision.

# 5.5.1 Metric and coordinate freedom

We consider a spacetime with a metric that can be expressed in the form

$$
g _ { \alpha \beta } = \eta _ { \alpha \beta } + p _ { \alpha \beta } ,
$$

where $\eta _ { \alpha \beta }$ is the Minkowski metric, and where $p _ { \alpha \beta }$ is a collection of ten independent fields that are each assumed to be small compared with unity. To keep track of the order of smallness we introduce the parameter $\epsilon \ll 1$ , and we write $p _ { \alpha \beta } = O ( \epsilon )$ . Equation (5.119) states that the spacetime metric deviates only slightly from the Minkowski metric, and this serves as our definition of a weakly-curved spacetime. This spacetime contains weak gravitational fields, and everywhere in this section we shall be working consistently to first order in $\epsilon$ , neglecting all terms of order $\epsilon ^ { 2 }$ and higher. We shall refer to $\eta _ { \alpha \beta }$ as the “background metric,” and to $p _ { \alpha \beta }$ as the “metric perturbation.”

Equation (5.119) imposes a severe restriction on the coordinate freedom that is normally unlimited in the exact formulation of general relativity. We must restrict the coordinate transformations $x ^ { \prime \mu } = F ^ { \mu } ( x ^ { \alpha } )$ to those that preserve the decomposition of the metric into a dominant Minkowski piece and a small perturbation. The remaining coordinate freedom includes Lorentz transformations, which leave $\eta _ { \alpha \beta }$ unchanged but alter $p _ { \alpha \beta }$ as if it were a tensor field in flat spacetime, and small coordinate deformations of the form

$$
x ^ { \prime \alpha } = x ^ { \alpha } + \zeta ^ { \alpha } ( x ^ { \beta } ) ,
$$

where $\zeta ^ { \alpha }$ is a vector field of order $\epsilon$ . Large coordinate transformations are excluded from our considerations.

To first order in $\epsilon$ the inverse to Eq. (5.120) is $x ^ { \alpha } = x ^ { \prime \alpha } - \zeta ^ { \alpha } ( x ^ { \prime \beta } )$ , because the difference between $\zeta ^ { \alpha } ( x ^ { \prime \beta } )$ and $\zeta ^ { \alpha } ( x ^ { \beta } )$ is approximately $\zeta ^ { \beta } \partial _ { \beta } \zeta ^ { \alpha }$ , which is of order $\epsilon ^ { 2 }$ . This implies that $d x ^ { \alpha } = ( \delta _ { \beta } ^ { \alpha } - \partial _ { \beta } \zeta ^ { \alpha } ) d x ^ { \prime \beta }$ , and substitution into $d s ^ { 2 } = g _ { \alpha \beta } d x ^ { \alpha } d x ^ { \beta }$ reveals that the metric is given by

$$
g _ { \alpha \beta } ^ { \prime } = \eta _ { \alpha \beta } + p _ { \alpha \beta } - \partial _ { \alpha } \bigl ( \eta _ { \beta \mu } \zeta ^ { \mu } \bigr ) - \partial _ { \beta } \bigl ( \eta _ { \alpha \mu } \zeta ^ { \nu } \bigr ) + O ( \epsilon ^ { 2 } )
$$

in the primed coordinates. This shows that the decomposition of Eq. (5.119) is indeed preserved, and that the perturbation becomes

$$
p _ { \alpha \beta } ^ { \prime } = p _ { \alpha \beta } - \partial _ { \alpha } \zeta _ { \beta } - \partial _ { \beta } \zeta _ { \alpha } , \qquad \zeta _ { \alpha } : = \eta _ { \alpha \mu } \zeta ^ { \mu } ,
$$

in the new coordinates. Here we allow ourselves to lower the index on $\zeta ^ { \mu }$ with the Minkowski metric $\eta _ { \alpha \mu }$ instead of the full metric $g _ { \alpha \mu }$ , because the difference is of order $\epsilon ^ { 2 }$ ; we shall make repeated use of this convention in what follows.

It is noteworthy that Eq. (5.122) looks like a natural tensorial generalization of $A _ { \alpha } $ $A _ { \alpha } ^ { \prime } = A _ { \alpha } - \partial _ { \alpha } \chi$ , which is a gauge transformation of a vector potential $A _ { \alpha }$ generated by a scalar field $\chi$ . For this reason the transformation of the metric perturbation under a small coordinate deformation is often referred to as a gauge transformation generated by the vector field $\zeta _ { \alpha }$ . We shall adopt this attractive terminology, but it is important to understand that the gauge freedom of the linearized theory is not a new symmetry of general relativity; it is simply the general covariance of the full theory restricted to the small coordinate deformations of Eq. (5.120).

# 5.5.2 Curvature and field equations

We next calculate the Christoffel symbols and curvature tensors associated with the metric of Eq. (5.119), working consistently to first order in $\epsilon$ . It is useful here to recall our previous convention that when an index is lowered on a quantity of order $\epsilon$ , the lowering can be accomplished with the Minkowski metric $\eta _ { \alpha \beta }$ ; the same is true of index raising, which can be accomplished with $\eta ^ { \alpha \beta }$ . This convention allows us to introduce

$$
p ^ { \alpha \beta } : = \eta ^ { \alpha \mu } \eta ^ { \beta \nu } p _ { \mu \nu } , \qquad p : = \eta ^ { \alpha \beta } p _ { \alpha \beta } ,
$$

as convenient notations.

It is easy to verify that the inverse metric must be given by

$$
g ^ { \alpha \beta } = \eta ^ { \alpha \beta } - p ^ { \alpha \beta } ,
$$

if $g ^ { \alpha \beta }$ is to respect its defining relation $g ^ { \alpha \mu } g _ { \mu \beta } = \delta _ { \beta } ^ { \alpha }$ up to terms of order $\epsilon ^ { 2 }$ . The Christoffel symbols are

$$
\Gamma _ { \beta \gamma } ^ { \alpha } = \frac { 1 } { 2 } \big ( \partial _ { \beta } p _ { \gamma } ^ { \alpha } + \partial _ { \gamma } p _ { \beta } ^ { \alpha } - \partial ^ { \alpha } p _ { \beta \gamma } \big ) ,
$$

and the Riemann tensor is

$$
R _ { \alpha \beta \gamma \delta } = { \frac { 1 } { 2 } } \big ( \partial _ { \beta \gamma } p _ { \alpha \delta } - \partial _ { \beta \delta } p _ { \alpha \gamma } - \partial _ { \alpha \gamma } p _ { \beta \delta } + \partial _ { \alpha \delta } p _ { \beta \gamma } \big ) .
$$

Under a gauge transformation we find that $\Gamma _ { \beta \gamma } ^ { \alpha }$ changes by terms that depend on second derivatives of $\zeta _ { \alpha }$ , but the Riemann tensor is invariant:

$$
R _ { \alpha \beta \gamma \delta } ^ { \prime } = R _ { \alpha \beta \gamma \delta } .
$$

This result illustrates the important fact that while the metric simultaneously encodes information about gravity and the adopted coordinate system, the Riemann tensor is all about gravitation.

From Eq. (5.126) we may form the Ricci tensor, Ricci scalar, and Einstein tensor, which are all gauge-invariant quantities. We obtain

$$
\begin{array} { c } { { R _ { \alpha \beta } = - \displaystyle \frac 1 2 \big ( \sqcap p _ { \alpha \beta } + \partial _ { \alpha \beta } p - \partial _ { \alpha \mu } p _ { ~ \beta } ^ { \mu } - \partial _ { \beta \mu } p _ { ~ \alpha } ^ { \mu } \big ) , } } \\ { { R = - \sqcup p + \partial _ { \mu \nu } p ^ { \mu \nu } , } } \end{array}
$$

and

$$
G _ { \alpha \beta } = - \frac { 1 } { 2 } \big ( \ d \Omega p _ { \alpha \beta } + \partial _ { \alpha \beta } p - \partial _ { \alpha \mu } p _ { \beta } ^ { \mu } - \partial _ { \beta \mu } p _ { \alpha } ^ { \mu } \big ) + \frac { 1 } { 2 } \eta _ { \alpha \beta } \big ( \ d \Omega p - \partial _ { \mu \nu } p ^ { \mu \nu } \big ) .
$$

Here we let $\begin{array} { r } { \Pi : = \eta ^ { \alpha \beta } \partial _ { \alpha \beta } } \end{array}$ denote the flat-spacetime wave operator.

The form of the Einstein tensor can be simplified slightly if, instead of $p _ { \alpha \beta }$ , we express it in terms of the trace-reversed perturbation

$$
\bar { p } _ { \alpha \beta } : = p _ { \alpha \beta } - \frac { 1 } { 2 } \eta _ { \alpha \beta } p .
$$

The expression “trace-reversed” follows from the property that ${ \bar { p } } = - p$ , so that $p _ { \alpha \beta } =$ $\begin{array} { r } { \bar { p } _ { \alpha \beta } - \frac { 1 } { 2 } \eta _ { \alpha \beta } \bar { p } } \end{array}$ . Making the substitution yields

$$
G _ { \alpha \beta } = - \frac { 1 } { 2 } \big ( \ d \Omega \bar { p } _ { \alpha \beta } - \partial _ { \alpha \mu } \bar { p } ^ { \mu } _ { \beta } - \partial _ { \beta \mu } \bar { p } ^ { \mu } _ { \alpha } + \eta _ { \alpha \beta } \partial _ { \mu \nu } \bar { p } ^ { \mu \nu } \big ) .
$$

The Einstein field equations are

$$
G ^ { \alpha \beta } = { \frac { 8 \pi G } { c ^ { 4 } } } T ^ { \alpha \beta } ,
$$

in which $T ^ { \alpha \beta }$ , like $p _ { \alpha \beta }$ and $G ^ { \alpha \beta }$ , is imagined to be of order $\epsilon$ . The appropriate statement of the contracted Bianchi identities, to order $\epsilon$ , is

$$
\partial _ { \beta } G ^ { \alpha \beta } = 0 ,
$$

and it is easy to verify that this does indeed follow automatically from Eqs. (5.130) or (5.132). Also to order $\epsilon$ , the appropriate statement of energy-momentum conservation is

$$
\partial _ { \beta } T ^ { \alpha \beta } = 0 .
$$

Physically, this equation implies that the matter fields that produce $T ^ { \alpha \beta }$ are allowed to exchange energy and momentum between themselves, but not with the gravitational field; such an exchange would be described by the exact equation $\nabla _ { \beta } T ^ { \alpha \beta } = 0$ , which differs from Eq. (5.135) by terms of order $\epsilon ^ { 2 }$ . Thus, in the linearized theory the dynamics of the matter fields cannot include gravity, and the theory cannot be applied to systems (like stars) that are bound together by gravitational forces. The dynamics must instead be dominated by non-gravitational forces. This is an important, and often unappreciated, limitation of the approximation.

# 5.5.3 Lorenz gauge

A substantial simplification of the Einstein tensor results when we exploit the coordinate freedom of Eq. (5.122) and impose the conditions

$$
\partial ^ { \beta } \bar { p } _ { \alpha \beta } = 0
$$

on the (trace-reversed) metric perturbation. This equation is a natural tensorial generalization of the Lorenz-gauge condition of electrodynamics, as expressed in Eq. (4.66); we therefore refer to Eq. (5.136) as the Lorenz-gauge condition for the gravitational potentials $p _ { \alpha \beta }$ . This choice of gauge can always be enforced. If we are presented with a $\bar { p } _ { \alpha \beta } ^ { \mathrm { o l d } }$ that does not satisfy the Lorenz-gauge conditions, a gauge transformation will produce $\bar { p } _ { \alpha \beta } ^ { \mathrm { n e w } } = \bar { p } _ { \alpha \beta } ^ { \mathrm { o l d } } - \partial _ { \alpha } \zeta _ { \beta } - \partial _ { \beta } \zeta _ { \alpha } + \eta _ { \alpha \beta } \partial _ { \mu } \zeta ^ { \mu }$ , and this will satisfy the gauge conditions when $0 \stackrel { \cdot } { = } \partial ^ { \beta } \bar { p } _ { \alpha \beta } ^ { \mathrm { n e w } } = \partial ^ { \beta } \bar { p } _ { \alpha \beta } ^ { \mathrm { o l d } } - \Pi \zeta _ { \alpha }$ . We see that the generator of the gauge transformation must

satisfy the wave equation

$$
\begin{array} { r } { \boxed { \varPsi _ { \alpha } } = \partial ^ { \beta } \bar { p } _ { \alpha \beta } ^ { \mathrm { o l d } } , } \end{array}
$$

and solutions to this equation can always be found. The solution, in fact, is not unique; to any solution $\zeta _ { \alpha }$ one can add the vector $\zeta _ { \alpha } ^ { \mathrm { h o m } }$ provided that this satisfies the homogeneous version of the wave equation, $\bigtriangledown \zeta _ { \alpha } ^ { \mathrm { h o m } } = 0$ . So while the Lorenz-gauge conditions can always be enforced, they do not completely specify the coordinate system. The conditions of Eq. (5.136) imply that of the ten original fields $p _ { \alpha \beta }$ , only six are independent.

With Eq. (5.136) the Einstein tensor becomes $\begin{array} { r } { G _ { \alpha \beta } = - \frac { 1 } { 2 } \sharp \bar { p } _ { \alpha \beta } } \end{array}$ , and the field equations take the form of a wave equation for the trace-reversed potentials:

$$
\boxed { \bar { p } _ { \alpha \beta } } = - \frac { 1 6 \pi G } { c ^ { 4 } } T _ { \alpha \beta } .
$$

Solutions to this equation are easily obtained (the relevant techniques will be introduced in Chapter 6), and the metric is easily reconstructed from the potentials: $g _ { \alpha \beta } = \eta _ { \alpha \beta } + \bar { p } _ { \alpha \beta } -$ $\frac { 1 } { 2 } \eta _ { \alpha \beta } \bar { p }$ .

Because of its simplicity, Eq. (5.138) is an excellent starting point to an investigation of the nature of gravity in weak-field situations. In fact, in Chapter 6 we will recover the wave equation in an improved formulation of the theory, which involves a systematic expansion of the Einstein and energy-momentum tensors in powers of $\epsilon$ . So there is a lot that is good about Eq. (5.138), but one aspect that requires scrutiny is the suggested notion that all six independent degrees of freedom contained in $p _ { \alpha \beta }$ are radiative degrees of freedom. If weak-field gravity is at all analogous to electrodynamics, we would expect instead that some degrees of freedom are non-radiative, and bound to the distribution of mass-energy (just as the Coulomb piece of the electric field is directly tied to the distribution of charge). A deeper analysis of the field equations will reveal that such is indeed the case: Of the six degrees of freedom, only two are radiative, while the remaining four are bound to the matter distribution. The suggestion from Eq. (5.138) that all degrees of freedom are radiative is merely an artifact of the choice of gauge.

# 5.5.4 Decomposition of the metric into irreducible pieces

We require a sophisticated decomposition of the metric perturbation $p _ { \alpha \beta }$ that allows a clear identification of the degrees of freedom. To accomplish this we shall follow a nice treatment of the linearized theory that we learned from our friends Eanna Flanagan and Scott Hughes ´ in their 2005 publication.

We first recall that under a Lorentz transformation, $p _ { \alpha \beta }$ transforms as a tensor field in Minkowski spacetime. The general transformation includes a boost, in which the new frame moves with speed $v$ relative to the old frame, and a rotation, in which the new spatial axes are rotated relative to the old frame. Here we are not interested in the boosts, and shall instead restrict our attention to pure rotations. The important observation for our purposes is that under a rotation of the spatial axes, $p _ { 0 0 }$ transforms as a scalar, $p _ { 0 j }$ transforms as a (Cartesian) vector, and $p _ { j k }$ transforms as a (Cartesian) tensor. We shall use this observation to decompose these quantities into their irreducible pieces $( \mathrm { B o x } ~ 5 . 7 )$ ). Thus, $p _ { 0 j }$ will be decomposed into longitudinal and transverse pieces, while $p _ { j k }$ will be decomposed into trace, longitudinal-tracefree, longitudinal-transverse, and transverse-tracefree pieces. As we shall see, this decomposition clearly delineates the degrees of freedom contained in each component of $p _ { \alpha \beta }$ .

<table><tr><td>Box 5.7</td><td>Decomposition of vectors and tensors into irreducible pieces</td></tr><tr><td></td><td>We aim to show that a Cartesian vector field Aj can always be decomposed as Aj =əjA+Aγ，djAγ =0, (1)</td></tr><tr><td></td><td> in terms ofa longitudinal piece dj A and a transverse piece A&#x27;. Under some conditions that willbe stated</td></tr><tr><td></td><td> in a moment, this decomposition is unique. The origin of the terms &quot;longitudinal&quot; and &quot;transverse&quot; in this</td></tr><tr><td></td><td>context will be clarified below.The longitudinal piece of Aj contains one independent component (the scalar</td></tr><tr><td></td><td>A),andthe transverse piece,byvirtueof theconditiondjA = O,containstwo independent components; these sum up to three independent components, the appropriate number for a vector field.</td></tr></table>

We shall show also that a symmetric tensor field $B ^ { j k }$ can always be decomposed as

$$
B ^ { j k } = \frac { 1 } { 3 } \delta ^ { j k } B + \Big ( \partial ^ { j k } - \frac { 1 } { 3 } \delta ^ { j k } \nabla ^ { 2 } \Big ) C + \partial ^ { j } C _ { \mathrm { T } } ^ { k } + \partial ^ { k } C _ { \mathrm { T } } ^ { j } + C _ { \mathrm { T T } } ^ { j k } ,
$$

with the conditions

$$
\partial _ { j } C _ { \mathrm { T } } ^ { j } = 0 , \qquad \partial _ { k } C _ { \mathrm { T T } } ^ { j k } = 0 = \delta _ { j k } C _ { \mathrm { T T } } ^ { j k } .
$$

The decomposition involves a trace piece ${ \scriptstyle { \frac { 1 } { 3 } } } \delta ^ { j k } B$ , a longitudinal-tracefree piece $\begin{array} { r } { ( \partial ^ { j k } - \frac { 1 } { 3 } \delta ^ { j k } \nabla ^ { 2 } ) C , } \end{array}$ a longitudinal-transverse piece $\partial ^ { j } C _ { \mathrm { T } } ^ { k } + \partial ^ { k } C _ { \mathrm { T } } ^ { j } ,$ and a transverse-tracefree piece $C _ { \mathrm { T T } } ^ { j k }$ . The six independent components of $B ^ { j k }$ are contained in $B : = \delta _ { j k } B ^ { j k }$ (one component), $C$ (one component), $C _ { \mathrm { T } } ^ { j }$ (two components, by virtue of the divergence-free condition), and $C _ { \mathrm { T T } } ^ { j k }$ (two components, by virtue of the three divergence-free conditions and the additional tracefree condition).

The uniqueness of the vector decomposition is established by noting that $\partial _ { j } A ^ { j } = \nabla ^ { 2 } A .$ This is a Poisson equation for $A$ , and the solution is unique, given $A ^ { j }$ , provided that $A$ goes to zero at infinity; this requires $A ^ { j }$ to fall off sufficiently rapidly when $r : = | { \boldsymbol { x } } |  \infty$ . Once $A$ is found, Eq. (1) immediately gives $A _ { \mathrm { T } } ^ { j }$ .

The uniqueness of the tensor decomposition follows from similar considerations. We note first that $B =$ $\delta _ { j k } B ^ { j k }$ is obviously unique. Next we derive the equations $\begin{array} { r } { \partial _ { k } B ^ { j k } = \frac { 1 } { 3 } \partial ^ { j } B + \frac { 2 } { 3 } \nabla ^ { 2 } \partial ^ { j } C + \nabla ^ { 2 } C _ { \mathrm { T } } ^ { j } } \end{array}$ and $\begin{array} { r } { \partial _ { j k } B ^ { j k } = \frac { 1 } { 3 } \nabla ^ { 2 } B + \frac { 2 } { 3 } \nabla ^ { 4 } C } \end{array}$ . With $B$ determined, the second equation is a Poisson equation for $\nabla ^ { 2 } C$ , and the solution is unique provided that $\nabla ^ { 2 } C \to 0$ when $r  \infty$ . With $\nabla ^ { 2 } C$ known, $C$ can be determined, and once more the solution is unique provided that $C  0$ when $r  \infty$ . Finally, the first equation is a Poisson equation for $C _ { \mathrm { T } } ^ { j }$ , and the solution is unique provided that $C _ { \mathrm { T } } ^ { j }  0$ when $r  \infty$ . With $B , C$ , and $C _ { \mathrm { T } } ^ { j }$ Tdetermined, Eq. (2) gives $C _ { \mathrm { T T } } ^ { j k }$ .

To explain where Eqs. (1)–(3) and the associated terminology come from, we appeal to the Fourier transform. A vector field that is sufficiently well-behaved at infinity can always be decomposed as

$$
{ \cal A } ^ { j } ( { \bf x } ) = \int \tilde { \cal A } ^ { j } ( k ) e ^ { i k \cdot x } d ^ { 3 } k ,
$$

in terms of plane waves $e ^ { i \boldsymbol { k \cdot x } }$ with amplitudes $\tilde { A } ^ { j } ( \pmb { k } )$ . For each value of $\pmb { k }$ in the domain of integration we can write $\tilde { A } ^ { j } = i \tilde { A } k ^ { j } + \tilde { A } _ { \mathrm { T } } ^ { j } ,$ , thereby decomposing the vector into a piece aligned with $k ^ { j }$ – the longitudinal piece – and another piece orthogonal to $k ^ { j }$ – the transverse piece; we demand that $i k _ { j } \tilde { A } _ { \mathrm { T } } ^ { j } = 0$ . Substitution into the Fourier integral gives

$$
\begin{array} { l } { { \displaystyle { \cal A } ^ { j } = \int i k ^ { j } \tilde { \cal A } e ^ { i k \cdot x } d ^ { 3 } k + \int \tilde { \cal A } _ { \mathrm { T } } ^ { j } e ^ { i k \cdot x } d ^ { 3 } k } } \\ { { \displaystyle ~ = \partial ^ { j } { \cal A } + { \cal A } _ { \mathrm { T } } ^ { j } } , } \end{array}
$$

where $\begin{array} { r } { A ( { \bf x } ) = \int \tilde { A } ( { \bf k } ) e ^ { i { \bf k } \cdot { \bf x } } d ^ { 3 } k } \end{array}$ . Note that the condition $i k _ { j } \tilde { A } _ { \mathrm { T } } ^ { j } = 0$ becomes $\partial _ { j } A _ { \mathrm { T } } ^ { j } = 0$ after evaluation of the Fourier integral. We have obtained the decomposition of Eq. (1) and clarified the meaning of the terms “longitudinal” and “transverse.”

For a symmetric tensor field we begin with

$$
B ^ { j k } ( { \pmb x } ) = \int \tilde { B } ^ { j k } ( { \pmb k } ) e ^ { i { \pmb k } \cdot { \pmb x } } d ^ { 3 } k
$$

and first decompose $\tilde { B } ^ { j k }$ into trace and tracefree pieces:

$$
\tilde { B } ^ { j k } = \frac 1 3 \delta ^ { j k } \tilde { B } + \tilde { C } ^ { j k } ,
$$

where $\delta _ { j k } \tilde { C } ^ { j k } = 0$ . We next write $\tilde { C } ^ { j k } = - k ^ { j } k ^ { k } \tilde { C } + i k ^ { j } \tilde { C } _ { \mathrm { T } } ^ { k } + i k ^ { k } \tilde { C } _ { \mathrm { T } } ^ { j } + \tilde { C } _ { \mathrm { T } } ^ { j k }$ and impose the conditions $i k _ { j } \tilde { C } _ { \mathrm { T } } ^ { j } = 0$ and $i k _ { k } \tilde { C } _ { \mathrm { T } } ^ { j k } = 0$ ; this provides a decomposition of $\tilde { C } ^ { j k }$ into a longitudinal piece $- k ^ { j } k ^ { k } \tilde { C }$ , a longitudinal-transverse piece $i k ^ { j } \tilde { C } _ { \mathrm { T } } ^ { k } + i k ^ { k } \tilde { C } _ { \mathrm { T } } ^ { j } ,$ , and a transverse piece $\tilde { C } _ { \mathrm { T } } ^ { j k }$ . This last T Ttensor can still be decomposed into trace and tracefree pieces; we have $\begin{array} { r } { \tilde { C } _ { \mathrm { T } } ^ { j k } = \frac { 1 } { 3 } \delta ^ { j k } \tilde { C } _ { \mathrm { T } } + \tilde { C } _ { \mathrm { T T } } ^ { j k } , } \end{array}$ , with $\delta _ { j k } \tilde { C } _ { \mathrm { T T } } ^ { j k } = 0 .$ . Because must itself be tracefree, we find that $\tilde { C } _ { \mathrm { T } } = k ^ { 2 } \tilde { C }$ , where $k ^ { 2 } = \pmb { k } \cdot \pmb { k } .$ . All in all this gives us

$$
\tilde { C } ^ { j k } = - \Big ( k ^ { j } k ^ { k } - { \frac { 1 } { 3 } } \delta ^ { j k } k ^ { 2 } \Big ) \tilde { C } + i k ^ { j } \tilde { C } _ { \mathrm { T } } ^ { k } + i k ^ { k } \tilde { C } _ { \mathrm { T } } ^ { j } + \tilde { C } _ { \mathrm { T T } } ^ { j k }
$$

for the tracefree piece of $\tilde { B } ^ { j k }$ . Evaluating the Fourier integrals returns Eq. (2) for $B ^ { j k }$ and the conditions of Eq. (3) for $C _ { \mathrm { T } } ^ { j }$ and $C _ { \mathrm { T T } } ^ { j k }$ .

Following the rules of Box 5.7, the decomposition of the metric perturbation is accomplished by

$$
\begin{array} { l } { p _ { 0 0 } = 2 U / c ^ { 2 } , } \\ { p _ { 0 j } = - 4 U _ { j } / c ^ { 3 } - \partial _ { j } A / c , } \\ { p _ { j k } = 2 \delta _ { j k } V / c ^ { 2 } + \Big ( \partial _ { j k } - \frac { 1 } { 3 } \delta _ { j k } \nabla ^ { 2 } \Big ) B + \big ( \partial _ { j } B _ { k } + \partial _ { k } B _ { j } \big ) / c ^ { 2 } + h _ { j k } ^ { \operatorname { T } } , } \end{array}
$$

along with the conditions

$$
\partial _ { j } U ^ { j } = 0 , \qquad \partial _ { j } B ^ { j } = 0 , \qquad \partial _ { k } h _ { \mathrm { T T } } ^ { j k } = 0 = \delta _ { j k } h _ { \mathrm { T T } } ^ { j k } .
$$

The ten independent components of $p _ { \alpha \beta }$ are contained in the potentials $U$ (one component), $U _ { j }$ (two components), $A$ (one component), $V$ (one component), $B$ (one component), $B _ { j }$ (two components), and $h _ { j k } ^ { \mathrm { T T } }$ (two components). The various factors of 2, $^ { - 4 }$ , and $c$ that appear in Eq. (5.139) were inserted for later convenience.

We next figure out how the ten gravitational potentials that are contained in $p _ { \alpha \beta }$ change under a gauge transformation. To achieve this we first decompose the generator $\zeta _ { \alpha }$ of the transformation into its own irreducible pieces. We write

$$
\begin{array} { l l } { { \zeta _ { 0 } = \alpha / c , } } & { { \mathrm { ~ } } } \\ { { \zeta _ { j } = 4 \beta _ { j } / c ^ { 2 } + \partial _ { j } \gamma , \qquad \partial ^ { j } \beta _ { j } = 0 , } } \end{array}
$$

again inserting factors of $c$ for convenience. Substitution of Eqs. (5.139) and (5.141) into Eq. (5.122) eventually returns

$$
\begin{array} { r l } & { U ^ { \prime } = U - \partial _ { t } \alpha , } \\ & { U _ { j } ^ { \prime } = U _ { j } + \partial _ { t } \beta _ { j } , } \\ & { V ^ { \prime } = V - \frac { 1 } { 3 } c ^ { 2 } \nabla ^ { 2 } \gamma , } \\ & { h _ { j k } ^ { \mathrm { H T } } = h _ { j k } ^ { \mathrm { H T } } , } \\ & { \boldsymbol { A } ^ { \prime } = \boldsymbol { A } + \boldsymbol { \alpha } + \partial _ { t } \gamma , } \\ & { \boldsymbol { B } ^ { \prime } = \boldsymbol { B } - 2 \gamma , } \\ & { \boldsymbol { B } _ { j } ^ { \prime } = \boldsymbol { B } _ { j } - 4 \beta _ { j } . } \end{array}
$$

We recall that $t : = x ^ { 0 } / c$ , and note that unlike all other gravitational potentials, the transverse-tracefree piece $h _ { j k } ^ { \mathrm { T T } }$ is gauge-invariant.

# 5.5.5 Coulomb gauge and gauge-invariant potentials

Inspection of Eqs. (5.142) reveals that the variables

$$
\begin{array} { l } { \displaystyle \Phi : = U + \partial _ { t } A + \frac 1 2 \partial _ { t t } \lambda } \\ { \displaystyle \Phi _ { j } : = U _ { j } + \frac 1 4 \partial _ { t } B _ { j } , } \\ { \displaystyle \Psi : = V - \frac 1 6 c ^ { 2 } \nabla ^ { 2 } B , } \end{array}
$$

as well as $h _ { j k } ^ { \mathrm { T T } }$ , are all gauge-invariant. As such these potentials encode information that concerns the gravitational field only, and this information does not depend at all on the choice of coordinate system. The gauge-invariant potentials, therefore, represent the true degrees of freedom of the gravitational field. We have two scalar potentials $\Phi$ and $\Psi$ , a vector potential $\Phi _ { j }$ that contains two independent components (by virtue of the transverse condition $\partial ^ { j } \Phi _ { j } =$ 0), and a tensor potential $h _ { j k } ^ { \mathrm { T T } }$ that also contains two independent components; the total number of degrees of freedom is six, and we have eliminated the four components of $p _ { \alpha \beta }$ that encode coordinate information.

There exists a choice of gauge for which

$$
A = B = B _ { j } = 0 \qquad \mathrm { ( C o u l o m b g a u g e ) } ,
$$

so that

$$
p _ { 0 0 } = 2 U / c ^ { 2 } , \quad p _ { 0 j } = - 4 U _ { j } / c ^ { 3 } , \quad p _ { j k } = 2 \delta _ { j k } V / c ^ { 2 } + h _ { j k } ^ { \mathrm { T I } }
$$

The potentials are constrained by the transverse condition $\partial _ { j } U ^ { j } = 0$ and the transversetracefree conditions on $h _ { j k } ^ { \mathrm { T T } }$ . The condition $\partial _ { j } U ^ { j } = 0$ is analogous to the choice of gauge defined by $\nabla \cdot A = 0$ in electrodynamics, and for this reason we call the conditions of Eq. (5.144) the Coulomb-gauge conditions. We note the important property that in the Coulomb gauge, the gravitational potentials are equal to the gauge-invariant potentials:

$$
{ \Phi } = U , \qquad \Phi _ { j } = U _ { j } , \qquad \Psi = V
$$

This property makes the Coulomb gauge especially meaningful and convenient.

It is easy to see that the conditions of Eq. (5.144) can always be enforced. Suppose that we are presented with a $p _ { \alpha \beta } ^ { \mathrm { o l d } }$ , decomposed as in Eqs. (5.139), that does not satisfy the Coulombgauge conditions. A gauge transformation, decomposed as in Eqs. (5.141), produces a new perturbation $p _ { \alpha \beta } ^ { \mathrm { n e w } }$ , and the complete listing of changes is given by Eqs. (5.142). We have, in particular, $B _ { j } ^ { \mathrm { { \scriptsize { ' } n e w } } } = B _ { j } ^ { \mathrm { { \scriptsize { o l d } } } } - 4 \beta _ { j }$ , and $\beta _ { j }$ can be chosen so as to set $B _ { j } ^ { \mathrm { n e w } } = 0$ . Similarly, $B ^ { \mathrm { n e w } } = B ^ { \mathrm { o l d } } - \mathrm { \dot { 2 } } \gamma$ , and $\gamma$ can be chosen so that $B ^ { \mathrm { n e w } } = 0$ . Finally, $A ^ { \mathrm { n e w } } = A ^ { \mathrm { o l d } } + \alpha + \partial _ { t } \gamma$ , and the condition $A ^ { \mathrm { n e w } } = 0$ determines $\alpha$ . We see that the Coulomb gauge can indeed be imposed, and moreover, we see that it completely specifies the coordinate system: $\zeta _ { \alpha }$ is completely determined by the gauge conditions.

# 5.5.6 Curvature and field equations (revisited)

It is a straightforward matter to insert Eqs. (5.145) into Eq. (5.126) and calculate the components of the Riemann tensor in the Coulomb gauge. But since the Riemann tensor is gauge-invariant, and the Coulomb-gauge potentials are equal to their gauge-invariant counterparts, one may simply make the substitutions $U  \Phi$ , $U _ { j } \to \Phi _ { j }$ , and $V  \Psi$ at the end of the calculation to obtain the general expression for the Riemann tensor, valid in any choice of gauge. This procedure yields

$$
\begin{array} { l } { { R _ { 0 j \theta k } = \displaystyle - \frac { 1 } { c ^ { 2 } } \partial _ { j k } \Phi - \frac { 1 } { c ^ { 4 } } \delta _ { j k } \partial _ { t t } \Psi - \frac { 2 } { c ^ { 4 } } \big ( \partial _ { t j } \Phi _ { k } + \partial _ { t k } \Phi _ { j } \big ) - \frac { 1 } { 2 c ^ { 2 } } \partial _ { t t } h _ { j k } ^ { \Gamma T } , } }  \\ { { R _ { 0 j k m } = \displaystyle \frac { 1 } { c ^ { 3 } } \big ( \delta _ { j k } \partial _ { m } \Psi - \delta _ { j m } \partial _ { t k } \Psi \big ) - \frac { 2 } { c ^ { 3 } } \big ( \partial _ { j k } \Phi _ { m } - \partial _ { j m } \Phi _ { k } \big ) } } \\ { { { } ~ - \displaystyle \frac { 1 } { 2 c } \big ( \partial _ { t k } h _ { j m } ^ { \Gamma T } - \partial _ { t m } h _ { j k } ^ { \Gamma T } \big ) , } } \\ { { R _ { j k m n } = \displaystyle \frac { 1 } { c ^ { 2 } } \big ( \delta _ { k m } \partial _ { j n } \Psi - \delta _ { k n } \partial _ { j m } \Psi - \delta _ { j m } \partial _ { k n } \Psi + \delta _ { j n } \partial _ { k m } \Psi \big ) } } \\ { { { } ~ + \displaystyle \frac { 1 } { 2 } \big ( \partial _ { k m } h _ { j n } ^ { \Gamma T } - \partial _ { k n } h _ { j m } ^ { \Gamma T } - \partial _ { j m } h _ { k n } ^ { \Gamma T } + \partial _ { j m } h _ { k n } ^ { \Gamma T } \big ) . } } \end{array}
$$

From this we next obtain the Einstein tensor, which is given by

$$
\begin{array} { l } { { G _ { 0 0 } = - { \displaystyle \frac { 2 } { c ^ { 2 } } } \nabla ^ { 2 } \Psi , } } \\ { { G _ { 0 j } = - { \displaystyle \frac { 2 } { c ^ { 3 } } } \partial _ { t j } \Psi + { \displaystyle \frac { 2 } { c ^ { 3 } } } \nabla ^ { 2 } \Phi _ { j } , } } \\ { { G _ { j k } = - { \displaystyle \frac { 2 } { 3 c ^ { 2 } } } \delta _ { j k } \nabla ^ { 2 } ( \Phi - \Psi ) - { \displaystyle \frac { 2 } { c ^ { 4 } } } \delta _ { j k } \partial _ { t t } \Psi + { \displaystyle \frac { 1 } { c ^ { 2 } } } \Bigl ( \partial _ { j k } - { \displaystyle \frac { 1 } { 3 } } \delta _ { j k } \nabla ^ { 2 } \Bigr ) ( \Phi - \Psi ) } } \\ { { \displaystyle ~ + ~ { \displaystyle \frac { 2 } { c ^ { 4 } } } \bigl ( \partial _ { t j } \Phi _ { k } + \partial _ { t k } \Phi _ { j } \bigr ) - { \displaystyle \frac { 1 } { 2 } } \Sigma h _ { j k } ^ { \mathrm { T } } . } } \end{array}
$$

We recall that $\begin{array} { r } { \boldsymbol { \Pi } : = \eta ^ { \alpha \beta } \partial _ { \alpha \beta } } \end{array}$ is the wave operator in flat spacetime. We recognize in Eq. (5.148) that the Einstein tensor is fully decomposed into its irreducible pieces, with $G _ { 0 j }$ containing longitudinal and transverse pieces, and $G _ { j k }$ containing trace, longitudinaltracefree, longitudinal-transverse, and transverse-tracefree pieces.

Before we write down the Einstein field equations we should also decompose the energymomentum tensor $T _ { \alpha \beta }$ into its own irreducible pieces. We write

$$
\begin{array} { l } { { T ^ { 0 0 } = \varrho c ^ { 2 } , } } \\ { { T ^ { 0 j } = ( s ^ { j } + \partial ^ { j } s ) c , } } \\ { { T ^ { j k } = \tau \delta ^ { j k } + \Big ( \partial ^ { j k } - \displaystyle \frac { 1 } { 3 } \delta ^ { j k } \nabla ^ { 2 } \Big ) \sigma + \partial ^ { j } \sigma ^ { k } + \partial ^ { k } \sigma ^ { j } + \sigma ^ { j k } , } } \end{array}
$$

and impose the conditions

$$
\partial _ { j } s ^ { j } = 0 , \qquad \partial _ { j } \sigma ^ { j } = 0 , \qquad \partial _ { k } \sigma ^ { j k } = 0 = \delta _ { j k } \sigma ^ { j k } .
$$

Here $\varrho$ is the mass density of the matter distribution as measured by an observer at rest relative to the coordinate frame $x ^ { \alpha }$ ; this should not be confused with $\rho$ , the proper mass density of a perfect fluid. The vector $s ^ { j } + \partial ^ { j } s$ is the momentum density of the matter distribution, and $T ^ { j k }$ is its stress tensor.

The decomposition of $T ^ { \alpha \beta }$ involves ten irreducible variables, but these cannot all be independent. A simple calculation reveals that $\partial _ { \beta } T ^ { \alpha \beta } = 0$ , the statement of energy-momentum conservation in the linearized theory, gives rise to the relations

$$
\nabla ^ { 2 } s = - \partial _ { t } \varrho , \qquad \nabla ^ { 2 } \sigma ^ { j } = - \partial _ { t } s ^ { j } , \qquad \nabla ^ { 2 } \sigma = - \frac { 3 } { 2 } ( \partial _ { t } s + \tau ) .
$$

These imply that only $\varrho , s ^ { j } , \tau$ , and $\sigma _ { j k } - \mathrm { s i x }$ independent variables in all – can be specified freely; the other four $( s , \sigma _ { j }$ , and $\sigma$ ) are determined by them.

Each irreducible piece of the Einstein tensor can be set equal to each irreducible piece of the energy-momentum tensor (multiplied by $8 \pi G / c ^ { 4 }$ ). The independent pieces of the Einstein field equations are thus revealed to be

$$
\begin{array} { c } { { \displaystyle \nabla ^ { 2 } \Psi = - 4 \pi G \varrho , } } \\ { { \displaystyle \nabla ^ { 2 } ( \Phi - \Psi ) = - \frac { 1 2 \pi G } { c ^ { 2 } } ( \partial _ { t } s + \tau ) , } } \\ { { \displaystyle \nabla ^ { 2 } \Phi _ { j } = - 4 \pi G s _ { j } , } } \\ { { \displaystyle \Pi _ { j k } ^ { \mathrm { T T } } = - \frac { 1 6 \pi G } { c ^ { 4 } } \sigma _ { j k } . } } \end{array}
$$

We also find the additional equations $\partial _ { t } \Psi = 4 \pi G s$ , $\Phi - \Psi = 8 \pi G \sigma / c ^ { 2 }$ , and $\partial _ { t } \Phi _ { j } =$ $4 \pi G \sigma _ { j }$ , which are redundant by virtue of Eqs. (5.151).

Equations (5.152) are the culminating point of our considerations. They carry important insights into the nature of relativistic gravity. We note first that of the six degrees of freedom of the gravitational field, the four represented by $\Phi$ , $\Phi _ { j }$ , and $\Psi$ obey Poisson equations. Solutions for these potentials at a time $t$ depend on the state of the matter variables at precisely the same time; the potentials march in step with the matter, much in the same way that the Newtonian potential $U$ depends on the instantaneous profile of the mass density $\rho$ . The remaining degrees of freedom, those represented by $h _ { j k } ^ { \mathrm { T T } }$ , behave very differently. These potentials obey wave equations, and their expression at a time $t$ depends on the state of the matter variables at an earlier time $t ^ { \prime }$ ; the delay allows for the propagation of a light signal from the source point $\mathbf { \Delta } _ { \mathbf { { x } ^ { \prime } } }$ to the field point $\boldsymbol { x }$ . The main message is this: of the six degrees of freedom of the gravitational field, only two are radiative; the remaining four are not, and are directly tied to the matter distribution.

The gauge-invariant formulation of the linearized field equations is conceptually powerful because it cleanly separates the radiative from the non-radiative degrees of freedom. It does not, however, give rise to a practical method to integrate the field equations. Two difficulties arise. The first is that even if Eqs. (5.152) could be integrated explicitly for the gaugeinvariant potentials $\Phi , \Phi _ { j } , \Psi ,$ and $h _ { j k } ^ { \mathrm { T T } }$ , the problem would not be completely solved until all the gravitational potentials $- U$ , $U _ { j }$ , $V , h _ { j k } ^ { \mathrm { T T } } , A , B$ , and $B _ { j }$ – are determined; this requires a choice of gauge and the integration of Eqs. (5.143). This first difficulty can be simply dealt with by adopting the Coulomb gauge and invoking Eqs. (5.146). The second difficulty is much more serious: to integrate Eqs. (5.152) one must first determine $\varrho , s ^ { j } , \tau$ , and $\sigma ^ { j k }$ , the relevant irreducible pieces of the energy-momentum tensor. While this can always be done in principle, in most applications it is difficult and impractical. For this reason, the Lorenz-gauge formulation of the Einstein field equations, summarized by Eq. (5.138) on page 256, provides a much more user-friendly method of finding solutions.

# 5.5.7 Newtonian limit

The linearized theory developed in the preceding subsections possesses a rich dynamical structure. The theory features two scalar potentials $\Phi$ and $\Psi$ , one transverse vector potential $\Phi _ { j }$ , and a transverse-tracefree tensor potential $h _ { j k } ^ { \mathrm { T T } }$ . This is quite a bit more than in Newton’s theory, and in this subsection we show how the Newtonian description (with its single scalar potential) emerges in an appropriate limit.

The Newtonian limit of linearized theory is defined by the statement that any speed $v$ that characterizes the matter distribution must be small compared with the speed of light: $v / c \ll 1$ . This inequality implies the existence of a hierarchy in the components of the energy-momentum tensor. We recall that $T ^ { 0 0 }$ is a mass density multiplied by $c ^ { 2 }$ , that $T ^ { 0 j }$ is a mass flux multiplied by $c$ , and that $T ^ { j k }$ describes the stresses within the matter distribution. We expect the ratio $T ^ { 0 j } / T ^ { 0 0 }$ to be of order $v / c$ , and $T ^ { j k } / T ^ { 0 0 }$ to be of order $( v / c ) ^ { 2 }$ . We therefore have $T ^ { j k } \ll T ^ { 0 j } \ll T ^ { 0 0 }$ , and in the Newtonian limit we ignore $T ^ { 0 j }$ and $T ^ { j k }$ while we retain the services of $T ^ { 0 0 } = \varrho c ^ { 2 }$ .

We formally define the Newtonian limit by setting $s ^ { j } = s = \tau = \sigma = \sigma ^ { j } = \sigma ^ { j k } = 0$ . The field equations of Eqs. (5.152) imply that $\Psi = \Phi$ and $\Phi _ { j } = 0$ . The remaining field equations are

$$
\nabla ^ { 2 } \Phi = - 4 \pi G \varrho
$$

and $\bigtriangledown h _ { j k } ^ { \mathrm { T T } } = 0$ . We recognize the first equation as Poisson’s equation of Newton’s theory, with $\Phi$ playing the role of the Newtonian potential $U$ . The second equation describes the propagation of a free gravitational wave; this can be turned off by adopting a zero-wave initial condition.

If we next adopt the Coulomb gauge, then $U = V = \Phi$ , and according to Eq. (5.145), the metric takes the form of

$$
d s ^ { 2 } = - ( 1 - 2 U / c ^ { 2 } ) d ( c t ) ^ { 2 } + ( 1 + 2 U / c ^ { 2 } ) ( d x ^ { 2 } + d y ^ { 2 } + d z ^ { 2 } ) ,
$$

with a potential $U$ that satisfies $\nabla ^ { 2 } U = - 4 \pi G \varrho$ . This is the Newtonian limit of general relativity.

We encountered a slightly different metric, given by $d s ^ { 2 } = - ( 1 - 2 U / c ^ { 2 } ) d ( c t ^ { 2 } ) + d x ^ { 2 } +$ $d y ^ { 2 } + d z ^ { 2 }$ , back in Eq. (5.12). In the earlier context of Sec. 5.1, this metric was arrived at on the basis of a thought experiment involving a photon climbing up a Newtonian gravitational field. The argument was based entirely on the principle of equivalence, and did not refer at all to the Einstein field equations. As a result, the argument produced the correct expression for $g _ { 0 0 }$ , but it did not produce the corrections to the spatial portion of the metric. Nevertheless, the metric of Eq. (5.12) was seen to give rise to the correct equations of motion for a test body moving in a Newtonian gravitational field. Do the spatial terms in Eq. (5.154) spoil this earlier, successful result?

The answer is no. To see this, we construct the Lagrangian that governs geodesic motion in our improved version of the Newtonian metric. This is $L = - m c \sqrt { - g _ { \alpha \beta } \dot { r } ^ { \alpha } \dot { r } ^ { \beta } }$ with $\dot { r } ^ { \alpha } : = d r ^ { \alpha } / d t$ , which evaluates to

$$
\begin{array} { l } { { L = - m c ^ { 2 } \sqrt { 1 - 2 U / c ^ { 2 } - ( 1 + 2 U / c ^ { 2 } ) ( v ^ { 2 } / c ^ { 2 } ) } } } \\ { { \ = - m c ^ { 2 } \sqrt { 1 - 2 U / c ^ { 2 } - v ^ { 2 } / c ^ { 2 } + O ( U v ^ { 2 } / c ^ { 4 } ) } } } \\ { { \ = - m c ^ { 2 } + \displaystyle \frac { 1 } { 2 } m v ^ { 2 } + m U + O ( m U v ^ { 2 } / c ^ { 2 } ) , } } \end{array}
$$

where $v ^ { 2 } : = \delta _ { j k } \dot { r } ^ { j } \dot { r } ^ { k }$ . This computation reveals that the spatial terms in the metric are multiplied by $( v / c ) ^ { 2 }$ in the Lagrangian, producing a contribution that is smaller than the Newtonian terms by a factor of $( v / c ) ^ { 2 }$ . This relativistic correction must be neglected in the Newtonian limit, and we conclude that the timelike geodesics of a spacetime with the metric of Eq. (5.154) are described by $\pmb { a } = \pmb { \nabla } U$ . These, of course, are the Newtonian equations of motion.

The spatial terms in Eq. (5.154) do have a significant effect on the motion of light, because in this case a correction of order $( v / c ) ^ { 2 }$ is actually a correction of order unity. We explore the relativistic deflection of light and its observable implications in Chapter 10.

# 5.6 Spherical bodies and Schwarzschild spacetime

We conclude this chapter with an exploration of spherical bodies in exact general relativity. While the internal description of such a body is necessarily complicated and requires detailed information about the matter content, the external description is exceptionally simple and provided by the most famous metric of all, the one associated with Karl Schwarzschild’s name. The Schwarzschild metric is an exact solution to the Einstein field equations that describes the vacuum region exterior to any spherical distribution of matter. The matter distribution can be static (in the case, for example, of a star in hydrostatic equilibrium) or time-dependent (in the case, for example, of a star undergoing gravitational collapse). As long as the configuration is spherically symmetric, the external, vacuum gravitational field is static and described by the Schwarzschild metric. (There is actually a second solution discovered by Schwarzschild, which describes the gravitational field inside a spherical body in hydrostatic equilibrium, under the assumption that its mass density is constant.)

In the case of a complete gravitational collapse, there is no stellar interior, the vacuum region extends everywhere, and the vacuum Schwarzschild solution describes a non-rotating black hole. By virtue of Israel’s uniqueness theorem, an isolated, stationary, non-rotating black hole must be spherical (regardless of the shape of its progenitor), and its metric must be the Schwarzschild vacuum metric.

Schwarzschild discovered his solutions in 1915, a few months before the formal publication by Einstein of the final form of the field equations. At the time Einstein had been able to obtain approximate solutions to his equations in weak-field situations, and it came as a surprise to him that an exact solution could be found, and that it could be expressed in such a simple form. Schwarzschild was a well-known German astronomer, and he was working at the Potsdam Observatory when World War I broke out. He carried out his famous work on general relativity while in hospital being treated for a rare auto-immune skin disease, which he had contracted while stationed at the Russian front; he died a few months later at the age of 42.

In this section we derive the Einstein field equations for a spherically-symmetric spacetime, and apply them to the vacuum exterior of any body, and to the interior of a static star. We will describe the exterior metric in a number of coordinate systems, work out the motion of a test mass, and consider the trajectory of a photon. We shall not be concerned here with the black-hole aspects of the spacetime, which are treated in detail in numerous textbooks.

# 5.6.1 Spherically symmetric spacetimes

Spherical symmetry encourages the use of spherical polar coordinates $( r , \theta , \phi )$ , in terms of which the metric of flat spacetime takes the form of $d s ^ { 2 } = - d ( c t ) ^ { 2 } + d r ^ { 2 } + r ^ { 2 } ( d \theta ^ { 2 } +$ $\sin ^ { 2 } \theta d \phi ^ { 2 } )$ . Generalizing to curved spacetime, we assert that the metric of any sphericallysymmetric spacetime can always be written in the form

$$
d s ^ { 2 } = - e ^ { - 2 \Phi / c ^ { 2 } } d ( c t ) ^ { 2 } + e ^ { 2 \Lambda / c ^ { 2 } } d r ^ { 2 } + r ^ { 2 } ( d \theta ^ { 2 } + \sin ^ { 2 } \theta d \phi ^ { 2 } ) ,
$$

in which $\Phi ( t , r )$ and $\Lambda ( t , r )$ are arbitrary functions of the coordinates $t$ and $r$ . While this may seem like a natural assumption, there are a number of subtle issues that must be addressed to justify it.

First, the assumed spherical symmetry implies that there exists in the spacetime a continuous sequence of concentric spheres, with the property that the spatial geometry on each sphere is the same everywhere. (By “sphere” we mean the two-dimensional surface of a sphere, not the three-dimensional interior.) The coordinate $r$ is nothing but a label of each sphere, with the property that it increases monotonically outwards. On each sphere we lay down a standard grid based on polar coordinates $\theta$ and $\phi$ , in such a way that the proper distance between two neighboring points on the sphere is given by $d \ell ^ { 2 } = r ^ { 2 } ( d \theta ^ { 2 } + \sin ^ { 2 } \theta d \phi ^ { 2 } )$ . The line element informs us that $r$ possesses two additional properties: $2 \pi r$ is the circumference of a great circle on the sphere (take $\textstyle \theta = { \frac { \pi } { 2 } }$ so that $d \ell = r d \phi$ ), and $4 \pi r ^ { 2 }$ is the sphere’s surface area (the surface element on the sphere is $d S = { \sqrt { g } } d \theta d \phi = r ^ { 2 } \sin \theta d \theta d \phi )$ .

Second, the absence of $d r d \theta$ and $d r d \phi$ terms in Eq. (5.156) results from the fact that spherical symmetry allows us to orient successive spheres so that the radial direction – the direction connecting points with the same value of $\theta$ and $\phi$ on successive spheres – is everywhere orthogonal to the $\theta$ and $\phi$ directions. It also allows us to orient a sphere at one instant of time with the same sphere at a later instant of time, so that the time direction also is orthogonal to the $\theta$ and $\phi$ directions; this property explains the absence of dtdθ and dtdφ terms. A term that cannot be removed by appealing to spherical symmetry is the $d ( c t ) d r$ term, which is nevertheless absent from Eq. (5.156). This reflects a choice of time coordinate: one can always transform from a generic coordinate $t ^ { \prime }$ to a new coordinate $t = t ( t ^ { \prime } , r )$ so as to eliminate an offending metric component $g _ { 0 r } ^ { \prime }$ . The remaining metric components are $g _ { 0 0 }$ and $g _ { r r }$ , and for these we employ the functions $\Phi ( t , r )$ and $\Lambda ( t , r )$ as suitable substitutes (the exponential forms are chosen for convenience).

We assume that we are dealing with a single isolated body, so that the spacetime becomes asymptotically flat in the limit $r  \infty$ . This leads to the requirements that

$$
\operatorname * { l i m } _ { r \to \infty } \Phi ( t , r ) = 0 , \qquad \operatorname * { l i m } _ { r \to \infty } \Lambda ( t , r ) = 0 ,
$$

and these boundary conditions ensure that the metric reduces to the Minkowski metric when $r \to \infty$ . With these conditions we now recognize from Eq. (5.156) that the time coordinate $t$ is proper time as measured by an observer at rest at infinity; for an observer at rest at position $r$ in the gravitational field, proper time $\tau$ is related to coordinate time $t$ by $\begin{array} { r } { \tau = \int e ^ { - \Phi ( t , r ) / c ^ { 2 } } d t } \end{array}$ . The metric allows us to make another observation: while $2 \pi r$ measures the circumference of great circles and $4 \pi r ^ { 2 }$ measures the area of spheres, we see that $r$ is not a measure of proper distance away from a center at $r = 0$ ; this is given instead by $\textstyle \int _ { 0 } ^ { r } e ^ { \Lambda ( t , r ^ { \prime } ) / c ^ { 2 } } d r ^ { \prime }$ .

In place of $\Lambda ( t , r )$ it is helpful to employ instead a relativistic mass-energy function $m ( t , \boldsymbol { r } )$ defined by

$$
e ^ { - 2 \Lambda / c ^ { 2 } } : = f ( t , r ) : = 1 - \frac { 2 G m ( t , r ) } { c ^ { 2 } r } .
$$

As we shall see, this bizarre substitution produces a substantial simplification of the field equations, and the name “mass-energy function” will be motivated shortly. Notice the minus sign within the exponential: the mass function is related to $g _ { r r }$ by $1 - 2 G m / ( c ^ { 2 } r ) =$ $( g _ { r r } ) ^ { - 1 } = g ^ { r r }$ .

It is straightforward, though tedious, to calculate the Christoffel symbols, Riemann tensor, Ricci tensor, and Einstein tensor for the metric of Eq. (5.156). (We cheat: we use computers to perform such computations.) The results for the relevant components of the Einstein tensor are

$$
\begin{array} { l } { { { \cal G } _ { 0 } ^ { 0 } = - \displaystyle \frac { 2 G } { c ^ { 2 } r ^ { 2 } } \partial _ { r } m , } } \\ { { { \cal G } _ { r } ^ { 0 } = - \displaystyle \frac { 2 G } { c ^ { 3 } r ^ { 2 } } e ^ { 2 \Phi / c ^ { 2 } } f ^ { - 1 } \partial _ { t } m , } } \\ { { { \cal G } _ { r } ^ { r } = - \displaystyle \frac { 2 } { c ^ { 2 } r } f \partial _ { r } \Phi - \displaystyle \frac { 2 G m } { c ^ { 2 } r ^ { 3 } } . } } \end{array}
$$

The remaining non-vanishing components of the Einstein tensor, $G _ { \theta } ^ { \theta }$ and $G _ { \phi } ^ { \phi }$ , will not be required. They are in fact redundant, because they are related to those of Eq. (5.159) by the Bianchi identities $\nabla _ { \beta } G ^ { \alpha \beta } = 0$ .

The Einstein field equations $G _ { \beta } ^ { \alpha } = ( 8 \pi G / c ^ { 4 } ) T _ { \beta } ^ { \alpha }$ take the explicit form

$$
\begin{array} { l } { { \partial _ { r } m = 4 \pi r ^ { 2 } ( - T _ { 0 } ^ { 0 } / c ^ { 2 } ) , } } \\ { { \partial _ { t } m = 4 \pi r ^ { 2 } e ^ { - 2 \Phi / c ^ { 2 } } f ( - T _ { r } ^ { 0 } / c ) , } } \\ { { \partial _ { r } \Phi = - \displaystyle \frac { G } { r ^ { 2 } } f ^ { - 1 } \big [ m + 4 \pi r ^ { 3 } ( T _ { r } ^ { r } / c ^ { 2 } ) \big ] , } } \end{array}
$$

for a spherically-symmetric spacetime. The first two equations are first-order, partial differential equations for the mass function $m ( t , \boldsymbol { r } )$ . The first equation bears a striking resemblance to Eq. (2.14), which determines the mass function in Newtonian gravity; it is this resemblance that motivates us to attach the name “mass” to this function. One difference, however, is that $- T _ { 0 } ^ { 0 }$ must be interpreted as the total energy density of the matter distribution, with the factor of $c ^ { - 2 }$ converting it into a mass density; the relativistic mass function, therefore, accounts for all forms of energy (including rest-mass energy, kinetic energy, and thermodynamic internal energy) within the spacetime. With this interpretation in place, the second equation also takes a suggestive form: $\partial _ { t } ( m c ^ { 2 } )$ is equal, up to relativistic corrections involving $\Phi$ and $f$ , to the flux of energy crossing a sphere of constant $r$ . The third member of Eq. (5.160) is an equation for the potential $\Phi$ involving the radial pressure $T _ { r } ^ { r }$ ; note that there is no equation for $\partial _ { t } \Phi$ .

# 5.6.2 The vacuum Schwarzschild metric

# Solution

In vacuum the energy-momentum tensor $T _ { \beta } ^ { \alpha }$ vanishes, and the equations for the mass function immediately give

$$
m ( t , r ) = M = { \mathrm { c o n s t a n t } } .
$$