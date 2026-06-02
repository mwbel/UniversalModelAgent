where $\zeta$ is a dimensionless parameter. We consider an overdamped situation with $\zeta \gg 1 , 5 0$ that the damping time scale $T _ { \mathrm { d a m p } } : = ( \zeta \omega ) ^ { - 1 }$ is very short compared with the oscillation time scale $T _ { \mathrm { i n t } }$ . The general solution to the differential equation is

$$
\begin{array} { l } { { \displaystyle x ( t ) = x ( 0 ) e ^ { - \zeta \omega t } \biggl ( \cosh \lambda \omega t + \frac { \zeta } { \lambda } \sinh \lambda \omega t \biggr ) + \frac { 1 } { \lambda \omega } \dot { x } ( 0 ) e ^ { - \zeta \omega t } \sinh \lambda \omega t } } \\ { { \displaystyle \qquad + \frac { 1 } { \lambda \omega } \int _ { 0 } ^ { t } f ( t ^ { \prime } ) e ^ { - \zeta \omega ( t - t ^ { \prime } ) } \sinh \lambda \omega ( t - t ^ { \prime } ) d t ^ { \prime } } , }  \end{array}
$$

where $\lambda : = \sqrt { \zeta ^ { 2 } - 1 } .$ Repeated integration by parts turns this into

$$
x ( t ) = { \mathrm { t r a n s i e n t } } \operatorname { t e r m s } + { \frac { 1 } { \omega ^ { 2 } } } { \big [ } f ( t ) - \tau { \dot { f } } ( t ) + \cdot \cdot \cdot { \big ] } ,
$$

where $\tau : = 2 \zeta / \omega ;$ the transient terms all decay exponentially, and the neglected terms are smaller than the leading term by a factor of order $( \tau / T _ { \mathrm { e x t } } ) ^ { 2 } \ll 1 .$ This result is analogous to Eq. (2.277), and because $f ( t ) - \tau \dot { f } ( t ) = f ( t - \tau ) + \cdot \cdot \cdot$ , we see that the effect of dissipation is to create a delay $\tau$ between the action of the force and the oscillator’s response. We have assumed that the delay is short compared with the external time scale. Because $\tau = 2 T _ { \mathrm { i n t } } ^ { 2 } / T _ { \mathrm { d a m p } } \gg T _ { \mathrm { i n t } } ,$ this can be arranged when $T _ { \mathrm { i n t } } / T _ { \mathrm { e x t } } \ll$ $T _ { \mathrm { d a m p } } / T _ { \mathrm { i n t } } \ll 1 .$ .

Equation (2.272) reveals that in the absence of viscosity, the body’s quadrupole moment is related to the tidal quadrupole moment by $\begin{array} { r } { G I _ { \langle j k \rangle } ( t ) = - \frac { 2 } { 3 } k _ { 2 } R ^ { 5 } \mathcal { E } _ { j k } ( t ) } \end{array}$ , in which $k _ { 2 }$ is the gravitational Love number and $R$ is the body’s radius; we see that the body responds instantaneously to the applied tidal field. In the presence of viscosity the relation becomes

$$
\begin{array} { l } { { G I _ { \langle j k \rangle } ( t ) = - { \displaystyle \frac { 2 } { 3 } } k _ { 2 } R ^ { 5 } \big [ \mathscr { E } _ { j k } ( t ) - \tau \dot { \mathscr { E } } _ { j k } ( t ) + \cdots \big ] } } \\ { { \mathrm { ~ } = - { \displaystyle \frac { 2 } { 3 } } k _ { 2 } R ^ { 5 } \big [ \mathscr { E } _ { j k } ( t - \tau ) + \cdot \cdot \cdot \big ] , } } \end{array}
$$

in which an overdot indicates differentiation with respect to $t$ ; as for Eq. (2.272), this equation is formulated in the body’s rotating frame. The new parameter $\tau$ has the dimension of time, and it represents a viscosity-induced delay between the action of the tidal field and the body’s response. The viscous delay must be proportional to the fluid’s kinematic viscosity, and it must be related to the body’s radius $R$ and its mass $M$ ; dimensional analysis reveals that it must be of the form $\tau \propto \bar { \nu } R / ( G M )$ , in which $\bar { \nu }$ is the averaged kinematic viscosity over the volume occupied by the fluid. The numerical coefficient will depend on the details of internal structure, and this dependence could be captured by introducing a third Love number, in addition to $k _ { 2 }$ and $h _ { 2 }$ . For our purposes it is preferable to adopt $\tau$ itself as a dimensionful “Love quantity,” a parameter that characterizes the body’s internal structure. We assume that $\tau$ is much larger than the internal time scale $T _ { \mathrm { i n t } } \sim ( G \rho ) ^ { - 1 / 2 } \sim \sqrt { R ^ { 3 } / G M }$ associated with the fluid’s dynamics, and that it is also much smaller than the external time scale $T _ { \mathrm { e x t } } \sim \sqrt { r _ { A B } ^ { 3 } / G M }$ associated with the orbital dynamics. The neglected terms in Eq. (2.277) are of order $( \tau / T _ { \mathrm { e x t } } ) ^ { 2 } \ll 1$ relative to the leading term proportional to $\mathcal { E } _ { j k }$ .

The viscous delay also appears in a modified relation between the surface deformation $\delta R$ and the applied tidal field. In this case it is possible to show that Eq. (2.274) becomes

$$
\begin{array} { l } { { \displaystyle \delta R = - \frac 1 2 h _ { 2 } \frac { R ^ { 4 } } { G M } \big [ \mathcal E _ { j k } ( t ) - \tau \dot { \mathcal E } _ { j k } ( t ) + \cdot \cdot \cdot \big ] n ^ { j } n ^ { k } } } \\ { ~ } \\ { { \displaystyle ~ = - \frac 1 2 h _ { 2 } \frac { R ^ { 4 } } { G M } \big [ \mathcal E _ { j k } ( t - \tau ) + \cdot \cdot \cdot \big ] n ^ { j } n ^ { k } } , } \end{array}
$$

and here also we see that the tidal deformation is delayed with respect to applied tidal field.

An important consequence of the inclusion of viscosity within the fluid dynamics is that it leads to energy dissipation, in the form of heat production, within the body. Another important consequence is that it gives rise to a transfer of angular momentum between the body and the remote bodies responsible for the tidal field. To calculate this effect we work initially in the non-rotating frame $x ^ { \bar { a } }$ , and we recall that the tidal potential is given by $\begin{array} { r } { U _ { \mathrm { t i d a l } } = - \frac { 1 } { 2 } \mathcal E _ { \bar { a } \bar { b } } x ^ { \bar { a } } x ^ { \bar { b } } } \end{array}$ , so that the density of tidal forces acting within the body is $f _ { \bar { a } } = \rho \partial _ { \bar { a } } U _ { \mathrm { t i d a l } } = - \rho \mathcal { E } _ { \bar { a } \bar { b } } x ^ { \bar { b } } .$ . These forces exert a torque, and integrating over the body, we find that the rate of change of the body’s angular momentum is given by

$$
\frac { d S _ { \bar { a } } } { d t } = \epsilon _ { \bar { a } \bar { b } \bar { c } } \int x ^ { \bar { b } } f ^ { \bar { c } } d ^ { 3 } \bar { x } .
$$

We obtain

$$
\frac { d S _ { \bar { a } } } { d t } = - \epsilon _ { \bar { a } \bar { b } \bar { c } } \mathcal { E } _ { \bar { p } } ^ { \bar { c } } \int \rho x ^ { \bar { b } } x ^ { \bar { p } } d ^ { 3 } \bar { x }
$$

after inserting our expression for the force density. The integral is the body’s mass quadrupole moment, which can be decomposed as $\begin{array} { r } { \bar { I } ^ { \bar { b } \bar { p } } = I ^ { \langle \bar { b } \bar { p } \rangle } + \frac { 1 } { 3 } \delta ^ { \bar { b } \bar { p } } I . } \end{array}$ . The trace term can be seen to give no contribution to the torque, and we find that

$$
\frac { d S _ { \bar { a } } } { d t } = - \epsilon _ { \bar { a } \bar { b } \bar { c } } I ^ { \langle \bar { b } \bar { p } \rangle } \mathcal { E } _ { \bar { p } } ^ { \bar { c } }
$$

gives the rate at which the body’s angular momentum changes as a result of the tidal interaction.

We next write the spin vector as $\pmb { S } = S \pmb { e }$ , in terms of a magnitude $S$ and a direction $_ e$ , and obtain an expression for $d S / d t$ by projecting $d S / d t$ in the direction of $_ e$ . Since we are now dealing with a scalar quantity, we may express each tensorial quantity in the body’s rotating frame $x ^ { j }$ . We obtain

$$
\frac { d S } { d t } = - \epsilon _ { j k n } e ^ { j } I ^ { \langle k p \rangle } \mathcal { E } _ { p } ^ { ~ n } ,
$$

in which we insert Eq. (2.277). We observe that the term proportional to $\mathcal { E } ^ { k p }$ makes no contribution to $d S / d t$ , and our final expression is

$$
\frac { d S } { d t } = \frac { 2 } { 3 } k _ { 2 } \tau R ^ { 5 } \epsilon _ { j k n } \mathcal { E } _ { ~ p } ^ { k } \dot { \mathcal { E } } ^ { p n } .
$$

We note that the effect is proportional to $\tau$ ; there is no transfer of angular momentum without viscosity.

As a concrete example we return to the discussion initiated at the end of Sec. 2.5.1. Once more we take our body to be the first member of a two-body system on a circular orbit of

radius $r$ and angular velocity $\Omega = \sqrt { G m / r ^ { 3 } }$ , in which $m = m _ { 1 } + m _ { 2 }$ . The body is rotating with an angular velocity $\omega$ , and we assume that the rotation axis $_ e$ is perpendicular to the orbital plane. In the rotating frame the tidal quadrupole moment is given by

$$
\mathcal { E } ^ { j k } = - \frac { G m _ { 2 } } { r ^ { 3 } } \big ( 3 n _ { 1 2 } ^ { j } n _ { 1 2 } ^ { k } - \delta ^ { j k } \big ) ,
$$

in which ${ \pmb n } _ { 1 2 } = [ \cos ( \Omega - \omega ) t$ , $\sin ( \Omega - \omega ) t , 0 ]$ . With $\pmb { n } = [ \sin \theta \cos \phi , \sin \theta \sin \phi , \cos \theta ]$ pointing toward a point on the surface, we have that the tidal deformation is proportional to

$$
\mathcal { E } _ { j k } ( t - \tau ) n ^ { j } n ^ { k } = - 3 \frac { G m _ { 2 } } { r ^ { 3 } } \left\{ \sin ^ { 2 } \theta \cos ^ { 2 } \left[ \phi - ( \Omega - \omega ) ( t - \tau ) \right] - \frac { 1 } { 3 } \right\} .
$$

The peak position of the tidal bulge is now given by

$$
\phi _ { \mathrm { b u l g e } } = \phi _ { 2 } - ( \Omega - \omega ) \tau ,
$$

in which $\phi _ { 2 } : = ( \Omega - \omega ) t$ is the angular position of the second body as measured in the rotating frame of the first body. We observe that the viscous delay creates a misalignment between the tidal bulge and the direction of the orbiting body. When $\omega < \Omega$ , that is, when the second body orbits faster than the first body rotates, we find that $\phi _ { \mathrm { b u l g e } } < \phi _ { 2 }$ ; the tide lags behind the orbiting body. When $\omega > \Omega$ , that is, when the first body rotates faster than the second body orbits, we find instead that $\phi _ { \mathrm { b u l g e } } > \phi _ { 2 }$ ; the tide leads in front of the orbiting body.

The viscosity-produced misalignment between the tidal bulge and the orbiting body is directly implicated in the transfer of angular momentum. When the bulge lags behind the orbiting body, the tidal forces acting on the excess mass in the bulge create a positive torque that increases the body’s angular momentum. When the bulge leads in front of the orbiting body, the torque is negative and produces a decrease in angular momentum. This intuition is confirmed with an explicit evaluation of $d S / d t$ from Eq. (2.283), making use of Eq. (2.284). After making the substitutions and simplifying, we eventually arrive at

$$
\frac { d S } { d t } = 6 k _ { 2 } \frac { G m _ { 2 } ^ { 2 } R ^ { 5 } } { r ^ { 6 } } ( \Omega - \omega ) \tau .
$$

This expression confirms that $S$ increases when $\omega < \Omega$ , and that it decreases when $\omega > \Omega$ . A consequence of this transfer of angular momentum is that the body evolves toward an equilibrium state with $\omega = \Omega$ ; eventually the body will become tidally locked, and rotate at the same frequency as the orbital motion. This phenomenon is observed everywhere in the solar system, including in our own backyard: our Moon always shows the same face (ignoring librations), and this is the result of its tidal interaction with the Earth. In fact, the moons of all planets in the solar system tend to be tidally locked, unless their orbits are too large to permit a significant tidal interaction. The Earth, however, is not yet tidally locked to the Moon’s orbital motion: the scaling of $d S / d t$ with the square of the remote mass implies that the time scale for tidal locking is much longer for the larger body than for the smaller body.

# 2.5.3 Dynamical tides

with the fluid dynamics of the deformed body. In this section we relax this condition, and consider a regime in which $T _ { \mathrm { e x t } } / T _ { \mathrm { i n t } }$ may not be large; this is the realm of dynamical tides.

As we have done previously, the body is assumed to be spherical and in hydrostatic equilibrium in the absence of a tidal interaction. To keep the problem simple we further assume that the body is non-rotating and possesses a uniform density $\rho _ { 0 }$ . The body is perturbed by external bodies which generate a tidal potential

$$
U _ { \mathrm { t i d a l } } = - \frac { 1 } { 2 } \mathcal { E } _ { j k } ( t ) x ^ { j } x ^ { k } ,
$$

in which $\mathcal { E } _ { j k } ( t )$ are time-dependent tidal moments. For an external object of mass $M _ { 2 }$ at a distance $r$ from the reference body, we have seen that $\mathcal { E } _ { j k } \sim G M _ { 2 } / r ^ { 3 }$ .

# Tidal response in the dynamical regime

The tidal forces created by $U _ { \mathrm { t i d a l } }$ produce a (small) perturbation in the fluid configuration of the body. As we shall justify below, we can think of $\mathcal { E } _ { j k } ( t )$ as a driving force, and of the fluid configuration as a harmonic oscillator of natural frequency $\omega _ { 2 }$ that responds to this driving force. The response is measured by $I ^ { \langle j k \rangle } ( t )$ , the body’s tracefree quadrupole moment, which vanishes in the unperturbed state. We shall find that

$$
G I _ { \langle j k \rangle } ( t ) = - \frac { 2 } { 5 } G M R ^ { 2 } \mathcal { F } _ { \langle j k \rangle } ( t ) ,
$$

where

$$
\mathcal { F } _ { ( j k ) } ( t ) : = \frac { 1 } { \omega _ { 2 } } \int _ { - \infty } ^ { t } \mathcal { E } _ { j k } ( t ^ { \prime } ) \sin \omega _ { 2 } ( t - t ^ { \prime } ) d t ^ { \prime }
$$

is the typical response function of a driven oscillator – refer to Box 2.4. For a body of uniform density, the natural frequency associated with a quadrupolar $\ell = 2$ ) driving force is given by

$$
\omega _ { 2 } = \sqrt { \frac { 4 } { 5 } \frac { G M } { R ^ { 3 } } } .
$$

This is comparable to the Keplerian angular velocity of an object orbiting just above the body’s surface, and therefore larger than the orbital angular velocity $\Omega$ of any one of the external objects. For a single external object of mass $M _ { 2 }$ at a distance $r$ from the reference body, we have that $\Omega ^ { 2 } \sim G M / r ^ { 3 }$ with $M : = M _ { 1 } + M _ { 2 }$ , so that $\omega _ { 2 } / \Omega \sim$ $( M _ { 1 } / M ) ^ { 1 / 2 } ( r / R ) ^ { 3 / 2 } > 1 .$ A typical situation would have $r \gg R$ and $\omega _ { 2 } / \Omega \gg 1$ , but we are interested in close encounters with $\omega _ { 2 } / \Omega$ of order unity.

When the time scale over which $\mathcal { E } _ { j k } ( t )$ varies is very long compared with $\omega _ { 2 } ^ { - 1 }$ , that is, when $\omega _ { 2 } / \Omega \gg 1$ , the integral of Eq. (2.290) can be evaluated by repeated integration by parts. This yields

$$
\mathcal { F } _ { \langle j k \rangle } = \omega _ { 2 } ^ { - 2 } \mathcal { E } _ { j k } - \omega _ { 2 } ^ { - 4 } \ddot { \mathcal { E } } _ { j k } + \omega _ { 2 } ^ { - 6 } \overset { \mathtt { ( 4 ) } } { \mathcal { E } } _ { j k } + \cdots ,
$$

in which an overdot (or a number within brackets) indicates differentiation with respect to $t$ . Inserting this and Eq. (2.291) within Eq. (2.289), we find that the quadrupole moment

becomes

$$
{ \cal G } I _ { \langle j k \rangle } = - { \frac { 1 } { 2 } } R ^ { 5 } \biggl ( { \mathcal { E } } _ { j k } - \omega _ { 2 } ^ { - 2 } { \ddot { \mathcal { E } } } _ { j k } + \omega _ { 2 } ^ { - 4 } { \stackrel { \ r { ( 4 ) } } { \mathcal { E } } } _ { j k } + \cdot \cdot \cdot \biggr ) .
$$

The leading term corresponds to the limit of static tides, and this result agrees with Eq. (2.272) when $\begin{array} { r } { k _ { 2 } = \frac { 3 } { 4 } } \end{array}$ , the value of the gravitational Love number for an incompressible fluid.

# Normal-mode analysis

To establish Eq. (2.289) we return to the formalism of fluid perturbations presented in Sec. 2.4.3 and relax the assumption that the perturbed configuration is an equilibrium state. We go back to Eq. (2.212), from which we eliminate the Coriolis term because the body is non-rotating. Recognizing that all perturbation variables depend linearly upon the displacement vector $\xi ^ { j }$ , it is useful to write the perturbed Euler equation in the abstract form

$$
\frac { \partial ^ { 2 } \xi ^ { j } } { \partial t ^ { 2 } } + \mathcal { L } _ { k } ^ { j } \xi ^ { k } = \partial ^ { j } U _ { \mathrm { t i d a l } } ,
$$

in which $\mathcal { L } _ { k } ^ { j }$ is a linear differential operator that appears in implicit form in Eq. $( 2 . 2 1 2 ) -$ it is related to the terms involving $\delta \rho , \delta p$ , and $\delta U$ . We seek to integrate Eq. (2.294) with the boundary conditions that $\xi ^ { j }$ be regular at $r = 0$ and continuous at $r = R$ . We proceed via a normal-mode analysis of the equation.

The normal modes of oscillation of a fluid configuration are solutions to the homogeneous equation $\partial _ { t t } \zeta ^ { j } + \mathcal { L } _ { k } ^ { j } \zeta ^ { k } = 0$ , which are taken to be in the form

$$
\zeta ^ { j } ( t , x ) = e ^ { - i \omega t } f ^ { j } ( x ) ,
$$

where $\omega$ is the mode frequency and $f ^ { j } ( { \pmb x } )$ its spatial profile, which is a solution to

$$
\begin{array} { r } { \mathcal { L } _ { k } ^ { j } f ^ { k } = \omega ^ { 2 } f ^ { j } . } \end{array}
$$

This is a second-order differential equation for $f ^ { j }$ , and a general solution will contain two freely-specifiable constants of integration. Since the equation is homogeneous in $f ^ { j }$ , one of these is an overall multiplicative constant, and the second constant is determined by one of the two boundary conditions that $f ^ { j }$ must satisfy. The second boundary condition will not be satisfied unless $\omega$ , the only other tunable parameter, is chosen appropriately. Equation (2.296) therefore specifies an eigenvalue problem for the frequencies $\omega$ and mode functions $f ^ { j }$ . The eigenfrequencies and eigenfunctions will be assigned an abstract label $\lambda$ , which is typically discrete. (Later on $\lambda$ will be identified with the spherical-harmonic indices $\ell m$ .)

The differential operator $\mathcal { L } _ { k } ^ { j }$ was shown by Chandrasekhar to be self-adjoint with respect to the integration measure $\rho d ^ { 3 } x$ . This fact implies a number of useful properties for the eigenvalues and eigenfunctions. First, the eigenvalues $\omega _ { \lambda } ^ { 2 }$ are real. Second, the eigenfunctions $f _ { \lambda } ^ { j }$ are orthogonal, in the sense that $\begin{array} { r } { \int f _ { \lambda } ^ { * } \cdot f _ { \lambda ^ { \prime } } \rho d ^ { 3 } x = N _ { \lambda } \delta _ { \lambda , \lambda ^ { \prime } } } \end{array}$ , where an asterisk indicates complex conjugation and $N _ { \lambda }$ is a normalization constant. Third, the eigenfunctions are (believed to be) complete, in the sense that any vectorial function $\pmb { \xi }$ admits an

expansion of the form

$$
\pmb { \xi } ( t , \pmb { x } ) = \sum _ { \lambda } a _ { \lambda } ( t ) \pmb { f } _ { \lambda } ( \pmb { x } ) ,
$$

in which the expansion coefficients are given by

$$
a _ { \lambda } ( t ) = \frac { 1 } { N _ { \lambda } } \int \boldsymbol { \xi } \cdot \boldsymbol { f } _ { \lambda } ^ { * } \rho \ : d ^ { 3 } x .
$$

These equations are the key to solving Eq. (2.294).

Assuming that the mode functions and frequencies have all been identified, we expand the displacement vector as in Eq. (2.297) and the driving force as

$$
\partial ^ { j } U _ { \mathrm { t i d a l } } = \sum _ { \lambda } u _ { \lambda } ( t ) f _ { \lambda } ^ { j } ( { \pmb x } ) ,
$$

with

$$
u _ { \lambda } = \frac { 1 } { N _ { \lambda } } \int \partial _ { j } U ^ { \mathrm { t i d a l } } f _ { \lambda } ^ { * j } \rho d ^ { 3 } x .
$$

We substitute the expansions within Eq. (2.294), make use of Eq. (2.296), and take advantage of the orthogonality of the eigenfunctions. We obtain, after simplification, a sequence of ordinary differential equations for the mode coefficients $a _ { \lambda }$ :

$$
\ddot { a } _ { \lambda } + \omega _ { \lambda } ^ { 2 } a _ { \lambda } = u _ { \lambda } .
$$

Each equation describes a harmonic oscillator of natural frequency $\omega _ { \lambda }$ subjected to a driving force $u _ { \lambda } ( t )$ . We suppose that the driving force vanishes in the distant past, and assume that each mode is quiet before the action of the force; we therefore subject Eq. (2.301) to the initial conditions $a _ { \lambda } ( t = - \infty ) = 0 = \dot { a } _ { \lambda } ( t = - \infty )$ . It is easy to check that the solution is

$$
a _ { \lambda } ( t ) = \frac { 1 } { \omega _ { \lambda } } \int _ { - \infty } ^ { t } u _ { \lambda } ( t ^ { \prime } ) \sin \omega _ { \lambda } ( t - t ^ { \prime } ) d t ^ { \prime } .
$$

At this stage the problem is formally solved. With each frequency $\omega _ { \lambda }$ and mode function $\ b { f } _ { \lambda }$ previously identified, the displacement vector can be constructed as in Eq. (2.297). The density perturbation is then given by Eq. (2.206), the pressure perturbation by Eq. (2.209), and $\delta U$ is obtained by integrating Eq. (2.213).

The normal modes of a fluid configuration depend on the unperturbed configuration. For a uniform-density model the eigenvalue problem can be shown to give rise to three separate classes of modes. In Cowling’s terminology, we have the so-called $p$ -modes, which are essentially acoustic waves driven by pressure fluctuations, the $g$ -modes, which are essentially gravity waves driven by buoyancy, and the f-modes (also known as Kelvin modes), which are essentially gravity waves confined to the surface. (Note that the term “gravity wave” designates a fluid wave whose restoring force is gravity rather than fluid pressure. The terminology is standard in atmospheric physics, for example, but gravity waves should not be confused with the “gravitational waves” of general relativity.) In the case considered here, in which the perturbation is driven by a quadrupolar tidal force, it is known that the $p$ -modes and the $g$ -modes do not get excited by the tidal interaction;

the overlap integrals of Eq. (2.300) vanish for these modes. (This was actually established by one of us back in 1983, at a time when the other had not yet started his university education.) The only modes that matter in our problem are the $f$ -modes, for which the eigenvalue equation can be integrated very easily.

# $f$ -modes

The defining property of these modes is the fact that they satisfy the divergence-free condition

$$
\partial _ { j } f ^ { j } = 0 .
$$

The eigenvalue equation is obtained from Eq. (2.212), and we have that $\partial _ { j } ( \delta p / \rho - \delta U ) =$ $\omega ^ { 2 } e ^ { - i \omega t } f _ { j }$ . The form of the equation implies that $f _ { j }$ must be the gradient of a scalar function $\psi$ ,

$$
f _ { j } = \partial _ { j } \psi .
$$

This, in turn, implies that the divergence-free condition becomes

$$
\nabla ^ { 2 } \psi = 0 ,
$$

and the mode equation simplifies to

$$
\delta p / \rho - \delta U = \omega ^ { 2 } e ^ { - i \omega t } \psi .
$$

To solve these equations we expand $\psi$ in spherical harmonics,

$$
\psi ( { \pmb x } ) = \sum _ { \ell m } g _ { \ell m } ( r ) Y _ { \ell m } ( \theta , \phi ) ,
$$

and seek to determine the radial functions $g _ { \ell m } ( r )$ . Laplace’s equation immediately implies that they must be proportional to $r ^ { \ell }$ . The mode equation will then be used to determine the eigenfrequencies $\omega _ { \ell }$ .

From Eq. (2.206) we find that the mode produces a perturbation in density given by $\delta \rho = - e ^ { - i \omega t } f ^ { j } \partial _ { j } \rho$ , while Eq. (2.209) implies that $\delta p = - e ^ { - i \omega t } f ^ { j } \partial _ { j } p$ . For the uniformdensity model under consideration, these equations become

$$
\delta \rho = \rho _ { 0 } \delta ( r - R ) \sum _ { \ell m } g _ { \ell m } ^ { \prime } ( R ) Y _ { \ell m } ( \theta , \phi ) e ^ { - i \omega t }
$$

and

$$
\delta p / \rho = \frac { 4 \pi } { 3 } G \rho _ { 0 } r \sum _ { \ell m } g _ { \ell m } ^ { \prime } ( r ) Y _ { \ell m } ( \theta , \phi ) e ^ { - i \omega t } ,
$$

in which a prime indicates differentiation with respect to $r$ . The perturbation in density gives rise to a change in the body’s gravitational potential. Expanding in spherical harmonics as in Eq. (2.219d), we find that $U _ { \ell m } \propto r ^ { \ell }$ inside the body, while $U _ { \ell m } \propto r ^ { - \ell - 1 }$ outside the body. Demanding continuity of $U _ { \ell m }$ at $r = R$ , but imposing the proper discontinuity in $U _ { \ell m } ^ { \prime }$ to account for the delta function in $\delta \rho$ , we arrive at

$$
U _ { \ell m } = \frac { 4 \pi } { 2 \ell + 1 } G \rho _ { 0 } R g _ { \ell m } ^ { \prime } ( R ) ( r / R ) ^ { \ell }
$$

inside the body. To get the solution outside the body we simply replace the last factor by $( R / r ) ^ { \ell + 1 }$ .

Collecting results, we find that the mode equation reduces to

$$
\frac { 4 \pi } { 3 } G \rho _ { 0 } r g _ { \ell m } ^ { \prime } ( r ) - \frac { 4 \pi } { 2 \ell + 1 } G \rho _ { 0 } R g _ { \ell m } ^ { \prime } ( R ) \left( r / R \right) ^ { \ell } = \omega ^ { 2 } g _ { \ell m } ( r ) .
$$

To simplify the notation we suppress the $\ell m$ label and introduce the dimensionless quantities $x , y$ , and $\epsilon$ such that $r : = R x , g : = R g ^ { \prime } ( R ) y$ , and $\omega ^ { 2 } : = ( 4 \pi / 3 ) G \rho _ { 0 } \epsilon ^ { 2 }$ . With these variables the mode equation becomes

$$
x \frac { d y } { d x } - \epsilon ^ { 2 } y = \frac { 3 } { 2 \ell + 1 } x ^ { \ell } ,
$$

which is to be integrated between $x = 0$ and $x = 1$ . The solution must be regular at $x = 0$ and satisfy the boundary condition $d y / d x = 1$ at $x = 1$ ; this follows directly from its definition in terms of $g ( r )$ . It is already known that $y$ must be proportional to $x ^ { \ell }$ , in order for $\psi$ to satisfy Laplace’s equation. The boundary condition at $x = 1$ determines the constant of proportionality: we find that $y = \ell ^ { - 1 } x ^ { \ell }$ . It then follows from the mode equation that $\epsilon ^ { 2 } = 2 \ell ( \ell - 1 ) / ( 2 \ell + 1 )$ . The modes are now completely determined.

To summarize, we have found that the $f$ -modes are labelled by the index $\lambda \equiv \ell m$ , that the eigenfrequencies are independent of $m$ and given by

$$
\omega _ { \ell } ^ { 2 } = { \frac { 8 \pi } { 3 } } G \rho _ { 0 } { \frac { \ell ( \ell - 1 ) } { 2 \ell + 1 } } ,
$$

and that the eigenfunctions are

$$
f _ { \ell m } ^ { j } = \partial ^ { j } \psi _ { \ell m } , \qquad \psi _ { \ell m } = R ^ { 2 } ( r / R ) ^ { \ell } Y _ { \ell m } ( \theta , \phi ) .
$$

The normalization is chosen so that $f _ { \ell m } ^ { j }$ has the dimension of length. It is easy to check that $\begin{array} { r } { N _ { \ell m } : = \int f _ { \ell m } ^ { * } \cdot f _ { \ell m } \rho _ { 0 } d ^ { 3 } x = \ell \rho _ { 0 } R ^ { 5 } } \end{array}$ .

# Tidal deformation

We may now involve the $f$ -modes in the solution of our problem. We first return to the overlap integral of Eq. (2.300), which becomes

$$
u _ { \ell m } = \frac { 1 } { \ell R ^ { \ell + 3 } } \int \partial ^ { j } U _ { \mathrm { t i d a l } } \partial _ { j } \left( r ^ { \ell } \bar { Y } _ { \ell m } \right) d ^ { 3 } x \ ,
$$

or

$$
u _ { \ell m } = { \frac { 1 } { \ell R ^ { \ell + 3 } } } \oint U _ { \mathrm { { t i d a l } } } \partial _ { j } \left( r ^ { \ell } { \bar { Y } } _ { \ell m } \right) d S ^ { j }
$$

after an integration by parts. Here $d S ^ { j } = R ^ { 2 } n ^ { j } d \Omega$ is the surface element on the spherical boundary of the (unperturbed) body, and the integral simplifies to

$$
u _ { \ell m } = { \frac { 1 } { R ^ { 2 } } } \oint U _ { \mathrm { t i d a l } } { \bar { Y } } _ { \ell m } d \Omega
$$

after evaluation of the radial derivative.

The tidal potential is integrated against spherical-harmonic functions on the surface of the body, and the operation is simplified by the fact that $U _ { \mathrm { t i d a l } }$ is a quadrupolar potential. We write

$$
U _ { \mathrm { t i d a l } } = - { \frac { 1 } { 2 } } { \mathcal E } _ { j k } ( t ) x ^ { j } x ^ { k } = - { \frac { 1 } { 2 } } R ^ { 2 } { \mathcal E } _ { j k } ( t ) n ^ { \langle j k \rangle } ,
$$

and to evaluate the integral we rely on the relationship between STF tensors and spherical harmonics that was uncovered back in Sec. 1.5.3. According to Eq. (1.164),

$$
n ^ { \langle j k \rangle } = \frac { 8 \pi } { 1 5 } \sum _ { m = - 2 } ^ { 2 } \mathcal { Y } _ { 2 , m } ^ { \langle j k \rangle } Y _ { 2 , m } ( \theta , \phi ) ,
$$

where $\mathcal { V } _ { \ell m } ^ { \langle L \rangle }$ is the constant STF tensor defined by $Y _ { \ell m } = { \mathcal { V } _ { \ell m } ^ { * \langle L \rangle } } n _ { \langle L \rangle }$ . Evaluation of the overlap integral yields

$$
u _ { 2 , m } ( t ) = - \frac { 4 \pi } { 1 5 } \mathcal { Y } _ { 2 , m } ^ { \langle j k \rangle } \mathcal { E } _ { j k } ( t ) ,
$$

and all other coefficients $u _ { \ell m }$ vanish. Substitution of this result into Eq. (2.302) produces

$$
a _ { 2 , m } ( t ) = - \frac { 4 \pi } { 1 5 } \mathcal { Y } _ { 2 , m } ^ { \langle j k \rangle } \mathcal { F } _ { j k } ( t ) ,
$$

where

$$
\mathcal { F } _ { j k } ( t ) : = \frac { 1 } { \omega _ { 2 } } \int _ { - \infty } ^ { t } \mathcal { E } _ { j k } ( t ^ { \prime } ) \sin \omega _ { 2 } ( t - t ^ { \prime } ) d t ^ { \prime }
$$

is the response function of Eq. (2.290). The only relevant frequency is $\omega _ { 2 }$ , and this is obtained by setting $\ell = 2$ within Eq. (2.313); the result is Eq. (2.291).

We may now construct the displacement vector. Substitution of $a _ { \ell m } ( t )$ into Eq. (2.297) produces

$$
\begin{array} { r l } {  { \xi ^ { j } = \sum _ { m } a _ { 2 , m } f _ { 2 , m } ^ { j } } } \\ & { = \sum _ { m } a _ { 2 , m } \partial ^ { j } \big ( r ^ { 2 } Y _ { 2 , m } \big ) } \\ & { = \partial ^ { j } \bigg ( { - \frac { 4 \pi } { 1 5 } r ^ { 2 } \mathcal { F } _ { p q } \sum _ { m } \mathcal { W } _ { 2 , m } ^ { ( p q ) } Y _ { 2 , m } } \bigg ) } \\ & { = \partial ^ { j } \bigg ( { - \frac { 1 } { 2 } r ^ { 2 } \mathcal { F } _ { p q } n ^ { p } n ^ { q } } \bigg ) , } \end{array}
$$

and we finally arrive at

$$
\xi ^ { j } = - \mathcal { F } _ { k } ^ { j } ( t ) x ^ { k } .
$$

The problem is now completely solved. From this we may obtain all other perturbation variables. For example, the velocity field is

$$
v ^ { j } = - \dot { \mathcal { F } } _ { k } ^ { j } ( t ) x ^ { k } ,
$$

the density perturbation is

$$
\begin{array} { r } { \delta \rho = - R \rho _ { 0 } \delta ( r - R ) \mathcal { F } _ { j k } n ^ { j } n ^ { k } , } \end{array}
$$

the pressure perturbation is

$$
\delta p = - \frac { 4 \pi } { 3 } G \rho _ { 0 } ^ { 2 } \mathcal { F } _ { j k } x ^ { j } x ^ { k } ,
$$

and the perturbation in the body’s gravitational potential is

$$
\delta U = - \frac { 4 \pi } { 5 } G \rho _ { 0 } \mathcal { F } _ { j k } x ^ { j } x ^ { k } .
$$

# Quadrupole moment

Our final task is to compute $I ^ { \langle j k \rangle } ( t )$ , the body’s quadrupole moment tensor,

$$
I ^ { \langle j k \rangle } = \int _ { V + \Delta V } ( \rho + \delta \rho ) x ^ { \langle j k \rangle } d ^ { 3 } x ,
$$

in which $V + \Delta V$ is the region of space occupied by the deformed body (while $V$ is the spherical region occupied by the unperturbed body). This can be written as

$$
I ^ { \langle j k \rangle } = \int _ { V } \rho x ^ { \langle j k \rangle } d ^ { 3 } x + \int _ { \Delta V } \rho x ^ { \langle j k \rangle } d ^ { 3 } x + \int _ { V } \delta \rho x ^ { \langle j k \rangle } d ^ { 3 } x .
$$

The first integral gives the unperturbed quadrupole moment, which vanishes. The second integral can be expressed as $\oint _ { S } \rho \boldsymbol { x } ^ { \left. j \boldsymbol { k } \right. } \boldsymbol { \xi } \cdot d \boldsymbol { S }$ , where $S$ is the boundary of the unperturbed body, and $d \pmb { S }$ is its surface element. The quadrupole moment is therefore

$$
I ^ { \langle j k \rangle } = \oint _ { S } \rho x ^ { \langle j k \rangle } { \pmb \xi } \cdot d { \pmb S } + \int _ { V } \delta \rho x ^ { \langle j k \rangle } d ^ { 3 } x .
$$

In this we insert Eq. (2.324) for $\pmb { \xi }$ , and Eq. (2.326) for $\delta \rho$ .

Our expression for $I ^ { \langle j k \rangle }$ appears to be ill defined, because it is not clear what the value of $\rho$ is on the surface, where it abruptly jumps from $\rho _ { 0 }$ to zero. If, for example, the surface integral is evaluated just below $r = R$ , then $\rho = \rho _ { 0 }$ and we obtain a non-zero value. In this case the volume integral is zero, because $\delta \rho$ is proportional to $\delta ( r - R )$ and the integral just misses the delta function. On the other hand, if the surface integral is evaluated just above $r = R$ , then $\rho = 0$ and the integral is zero. In this case the volume integral does not vanish, and fortunately, the result turns out to be the same in either case. We arrive at the unambiguous expression

$$
I ^ { \langle j k \rangle } = - \frac { 8 \pi } { 1 5 } \rho _ { 0 } R ^ { 5 } \mathcal { F } ^ { \langle j k \rangle } .
$$

This is the same statement as in Eq. (2.289). Our treatment of the tidal interaction is now complete.

# 2.6 Bibliographical notes

The physics of stellar structure described in Sec. 2.1 is covered in a lot more depth in a number of textbooks, which also discuss stellar evolution; among our favorites is the very accessible text by Hansen, Kawaler, and Trimble (2004). The phenomenon of neutrino oscillations, shown in Box. 2.1 to have essential consequences on the physics of the Sun, was first proposed by Wolfenstein (1978) and explored further by Mikheev and Smirnov (1985 and 1986). Our discussion of polytropes in Sec. 2.2.3, isothermal spheres in Sec. 2.2.4, and white dwarfs in Sec. 2.2.5 is heavily inspired by Chandrasekhar’s An introduction to the study of stellar structure (1958). Another useful reference on the astrophysics of white dwarfs and other compact bodies is Shapiro and Teukolsky (1983). The story of Chandrasekhar calculating the structure of white dwarfs and discovering the mass limit while traveling to England from India is famous; his discovery was published in Chandrasekhar (1931). Laudau’s argument in favor of neutron stars was published in Landau (1932).

Our presentation of the theory of rotating bodies in Sec. 2.3 relies heavily on the excellent treatise by Tassoul (1978). The Maclaurin spheroids and Jacobi ellipsoids of Sec. 2.3.2 are explored in much greater detail in Chandrasekhar’s Ellipsoidal figures of equilibrium (1987), a must-read for anyone interested in the structure and stability of rotating bodies. Our method to calculate the internal gravitational potential of an ellipsoid of uniform density is borrowed from Chapter IV of Moulton’s text (1984).

The general theory of deformed fluid bodies developed in Sec. 2.4 can be pieced together from a number of useful sources, including Kopal (1959 and 1978) and Cox (1980). The formalism of fluid perturbations described in Sec. 2.4.3 is borrowed directly from Chandrashekhar’s Ellipsoidal figures of equilibrium. The gravitational and surficial Love numbers were introduced by British geophysicist Augustus Edward Hough Love in his 1911 book. The Love numbers of polytropes were first computed by Brooker and Olle (1955).

The discussion of tides in Sec. 2.5 barely scratches the surface of a very rich field. A general introduction to the phenomenon can be found in Mccully (2006). Our presentation of the dynamical tides of a body of uniform density in Sec. 2.5.3 is based on Turner (1977) and Will (1983). The standard classification of fluid perturbation modes was introduced in Cowling (1941).

# 2.7 Exercises

2.1 Consider a power-series solution for the Lane–Emden equation, $\begin{array} { r } { \theta = \sum _ { p } a _ { p } \xi ^ { p } } \end{array}$ .

(a) Show that the boundary conditions at $\xi = 0$ require that $a _ { 0 } = 1$ and $a _ { 1 } = 0$ .   
(b) Show that $a _ { p } = 0$ for all odd values of $p$ .   
(c) Determine $a _ { 2 } , a _ { 4 }$ , and $a _ { 6 }$ for a general polytropic index $n$ , and reproduce the expansions displayed in Box 2.2. Show also that your expansion agrees with the exact results for $n = 0$ , $n = 1$ , and $n = 5$ .

2.2 Explain why $\Omega$ is ambiguous for a polytrope of index $n = 5$ . Show by a direct calculation that, for $n = 5$ , $\Omega = - \sqrt { 2 \pi } ( 8 1 / 1 6 ) K ^ { 5 / 2 } G ^ { - 3 / 2 }$ .

2.3 Calculate the gravitational potential energy $\Omega$ for a Maclaurin spheroid, and verify the result of Eq. (2.181).

2.4 Fill in the gaps left in the calculation of the dimensionless multipole moments $J _ { \ell }$ of a Maclaurin spheroid, and verify the result of Eq. (2.187).

2.5 Show that the surface of a rotationally deformed body can be described by

$$
r = a ( 1 - \alpha + \alpha \cos 2 L ) ,
$$

where $a$ is the equatorial radius and $L$ is the geographical latitude, which ranges from $\frac { \pi } { 2 }$ at the North Pole to $- \frac { \pi } { 2 }$ at the South Pole. Determine $\alpha$ in terms of the surficial Love number $h _ { 2 }$ and the rotational-deformation parameter $\zeta$ . Evaluate $\alpha$ for the Earth and compare with the observed value of 0.001677.

2.6 Show that for a rotationally deformed body of arbitrary composition, the body’s moment of inertia $\begin{array} { r } { I : = \int \rho ( x ^ { 2 } + y ^ { 2 } ) d ^ { 3 } x } \end{array}$ is given by $I = I _ { 0 } + \delta I$ , with

$$
I _ { 0 } = \frac { 8 \pi } { 3 } \int _ { 0 } ^ { R } \rho r ^ { 4 } d r
$$

denoting the unperturbed piece, and

$$
\delta I = \frac { 2 } { 3 } k _ { 2 } \zeta M R ^ { 2 }
$$

the perturbation. Here $k _ { 2 }$ is the gravitational Love number, and $\zeta$ is the deformation parameter. Assume that the unperturbed density goes smoothly to zero at $r = R$ .

2.7 Show that for a body with a polytropic equation of state, the function $\mathcal { D }$ behaves as

$$
\mathcal { D } = 1 - \frac { n } { 1 5 } \xi ^ { 2 } + \frac { n ( 1 9 n - 2 5 ) } { 3 1 5 0 } \xi ^ { 4 } + O ( \xi ^ { 6 } )
$$

near $\xi = 0$ . Use this expression to derive the expansion

$$
\begin{array} { c } { { \eta _ { \ell } = l - 2 + { \displaystyle \frac { 2 n ( \ell - 1 ) } { 5 ( 2 \ell + 3 ) } } \xi ^ { 2 } - { \displaystyle \frac { n ( \ell - 1 ) } { 5 2 5 } } } } \\ { { \times { \displaystyle \frac { ( 7 6 n - 1 0 0 ) \ell ^ { 2 } + ( 1 4 4 n - 3 0 0 ) \ell - ( 1 6 5 n + 2 2 5 ) } { ( 2 \ell + 3 ) ^ { 2 } ( 2 \ell + 5 ) } } \xi ^ { 4 } } } \\ { { + O ( \xi ^ { 6 } ) } } \end{array}
$$

for the Radau function.

2.8 The quadrupole moment $J _ { 2 }$ of the Sun is known from helioseismology measurements to be $2 . 2 \times 1 0 ^ { - 7 }$ . Its rotation period is approximately 25 days. From these facts, estimate $k _ { 2 }$ for the Sun and compare the result with the entry in Table 2.3 for the ideal gas equation of state $\mathrm { T } = 5 / 3$ ). From this comparison, what do you infer about the density distribution of the Sun as compared to a simple polytrope? What factors could lead to such a difference?

2.9 Consider a gravitating body with an $\ell = 2$ deformation, with $d _ { 2 m } = d _ { 2 } Y _ { 2 m } ^ { * } ( e )$ , where $_ e$ is a given direction. A gravimeter measures the acceleration of a test body on the surface of the body. Assume that the surficial Love number $h _ { 2 }$ is independent of $k _ { 2 }$ .

(a) Show that the variation in the magnitude of the acceleration over the surface is proportional to $1 + h _ { 2 } - 3 k _ { 2 }$ .   
(b) Show that the angle between the direction of the acceleration and the normal to the surface is proportional to $1 - h _ { 2 } + 2 k _ { 2 }$ .

2.10 We consider two fluid configurations, one with a homogeneous mass density $\rho _ { 0 }$ , the other with a density $\rho ( r )$ that deviates only slightly from $\rho _ { 0 }$ ; we write $\rho = \rho _ { 0 } + \delta \rho$ , and assume that $\delta \rho$ is small compared with $\rho _ { 0 }$ . We assume that the nearly homogeneous body has the same radius $R$ and the same total mass $M$ as the homogeneous body. We have seen that $\eta _ { \ell } = \ell - 2$ for the homogeneous body, and selecting $\ell = 2$ , we assume $\eta _ { 2 } ( r ) \ll 1$ for the nearly homogeneous body.

(a) Prove that under the circumstances described here, Radau’s equation for the nearly homogeneous body simplifies to

$$
r \eta _ { 2 } ^ { \prime } + 5 \eta _ { 2 } + 6 \delta { \mathcal { D } } = 0 ,
$$

where $\delta \mathcal { D } : = \mathcal { D } - 1$ is also taken to be small.

(b) Calculate $\delta \mathcal { D }$ in terms of $\delta \rho$ , and prove that

$$
\eta _ { 2 } ( R ) = - \frac { 1 5 } { \rho _ { 0 } R ^ { 5 } } \int _ { 0 } ^ { R } \delta \rho ( r ) r ^ { 4 } d r .
$$

(c) Calculate the moment of inertia $\begin{array} { r } { I : = \int \rho ( r ) ( x ^ { 2 } + y ^ { 2 } ) d ^ { 3 } x } \end{array}$ of the nearly homogeneous body, and relate it to $I _ { 0 }$ , the moment of inertia of the homogeneous body. Then show that

$$
\eta _ { 2 } ( R ) = - 3 \big ( I / I _ { 0 } - 1 \big ) .
$$

(d) Calculate $k _ { 2 }$ to first order in $( I / I _ { 0 } - 1 )$ .

In this chapter we apply the tools developed in the previous two chapters to an exploration of the orbital dynamics of bodies subjected to their mutual gravitational attractions. Many aspects of what we learned in Chapters 1 and 2 will be put to good use, and the end result will be considerable insight into the behavior of our own solar system. To be sure, the field of celestial mechanics has a rich literature that goes back centuries, and this relatively short chapter will only scrape the surface. We believe, however, that we have sampled the literature well, and selected a good collection of interesting topics. Some of the themes introduced here will be featured in later chapters, when we turn to relativistic aspects of celestial mechanics.

We begin in Sec. 3.1 with a very brief survey of celestial mechanics, from Newton to Einstein. In Sec. 3.2 we give a complete description of Kepler’s problem, the specification of the motion of two spherical bodies subjected to their mutual gravity. In Sec. 3.3 we introduce a powerful formalism to treat Keplerian orbits perturbed by external bodies or deformations of the two primary bodies; in this framework of osculating Keplerian orbits, the motion is at all times described by a sequence of Keplerian orbits, with constants of the motion that evolve as a result of the perturbation. We shall apply this formalism to a number of different situations, and highlight a number of important processes that take place in the solar system and beyond. In Sec. 3.5 we examine the three-body problem and briefly touch upon the general case of $N$ bodies. We conclude in Sec. 3.6 with a review of the Lagrangian formulation of Newtonian mechanics.

# 3.1 Celestial mechanics from Newton to Einstein

The triumph of Newton’s mechanics and universal gravitation is largely contained in the confrontation with the observed motion of celestial bodies in our solar system, which was initiated by Kepler even before Newton’s laws became available. The two-body dynamics of Newton’s theory immediately accounted for Kepler’s laws, which state that the orbits of bodies in the solar system are ellipses that trace out equal areas in equal times, with periods inversely proportional to the $3 / 2$ power of their diameters. Edmund Halley used Newton’s equations to point out that the comets that had been observed in 1531, 1607, and 1682 were actually a single object that orbits the sun with a period ranging from 75 to 76 years. Refined orbital calculations carried out by Alexis Clairaut led to the successful prediction of the comet’s return in 1759. The difficult problem of describing the detailed motion of the Moon, in particular the advance of its perigee, was successfully tackled by Clairaut using Newtonian theory; a first attempt was actually made by Newton himself, but with somewhat incorrect results that discouraged him and motivated him to start a new career at the Royal Mint. Finally, in a triumph of theoretical prediction, Urbain Jean Joseph Le Verrier in France, and independently John Couch Adams in England, pointed out that certain anomalies in the orbit of Uranus could best be explained by the existence of an additional planet, and each astronomer made a rough prediction of where such a planet might be found. In 1846, a day after receiving Le Verrier’s prediction for its position, German astronomers discovered the new planet, which is now called Neptune.

This accumulation of successes built such confidence in Newton’s theory that when the crisis occurred, the shock was almost palpable. The crisis was caused by Mercury. By the middle of the nineteenth century, astronomers had established that the perihelion of Mercury (the point of closest approach to the Sun) was advancing at a rate of 575 arcseconds per century relative to the fixed stars. Although the two-body solution of Newton’s theory requires the perihelion to be fixed in direction, it seemed clear that the advance should be caused by the gravitational influences of the other planets (mostly Venus because of its proximity, and Jupiter because of its large mass) on Mercury’s orbit. Fresh from his success with the prediction of Neptune, Le Verrier applied his methods to the problem of Mercury. He calculated the amount that each planet would contribute to Mercury’s perihelion advance (see Table 3.1), but the total fell short of the measured value, by an amount comparable to 40 arcseconds per century. The modern value of the discrepancy is $4 2 . 9 8 \pm 0 . 0 4$ arcseconds per century, based upon improved measurements of Mercury’s orbit using radar ranging, combined with improved data on the masses and orbits of the other planets, and accurate numerical ephemeris codes for calculating orbits.

The discrepancy could not be attributed to calculational errors or faulty observations, and no viable explanation could be found for the next 50 years. In the spirit of Neptune, Le Verrier and others supported the existence of another planet between Mercury and the Sun, which was given the provisional name Vulcan. But despite systematic astronomical searches, no credible evidence for such a planet was ever discovered. If changing the solar system would not do, perhaps a change of theory might fare better? Simon Newcomb proposed that all would be well with Mercury if the inverse square law of Newtonian gravity were changed to the inverse power of 2.0000001574. Such a change, however, would also contribute to the advance of the lunar perigee, and once improved data on the lunar orbit became available, Newcomb’s proposal was shown not to be viable.

The resolution of the problem of Mercury is by now legendary. The place is Berlin, the time November 1915. Albert Einstein, using the new equations of general relativity, calculates the motion of Mercury and shows that the relativistic laws of orbital motion account for the notorious discrepancy. Einstein was overjoyed, and later wrote to a friend that this discovery gave him palpitations of the heart. The modern value for the shift predicted by general relativity, using the best data for all relevant quantities, is 42.98 arcseconds per century, in perfect agreement with the measured value.

<table><tr><td rowspan=1 colspan=1>Table 3.1 Planetary contributions to Mercury&#x27;sperihelion advance (in arcseconds per century).</td></tr><tr><td rowspan=1 colspan=1> Planet                            Advance</td></tr><tr><td rowspan=1 colspan=1> Venus                               277.8 Earth                                 90.0 Mars                                   2.5 Jupiter                               153.6 Saturn                                 7.3</td></tr><tr><td rowspan=1 colspan=1>Total                                531.2 Discrepancy                          42.9</td></tr><tr><td rowspan=1 colspan=1>Modern measured value      42.98 ± 0.04General relativity prediction         42.98</td></tr></table>

# 3.2 Two bodies: Kepler’s problem

Kepler’s problem is to determine the motion of two bodies subjected to their mutual gravitational attraction, under the assumption that each body can be taken to be spherically symmetric. This is the simplest problem of celestial mechanics, but also one of the most relevant, because to a good first approximation, the motion of any planet around the Sun can be calculated while ignoring the effects of the other planets. It is also a problem that can be solved exactly and completely, in terms of simple functions.

# 3.2.1 Effective one-body description

The foundations for Kepler’s problem were provided back in Sec. 1.6.7. We have a first body of mass $m _ { 1 }$ , position $r _ { 1 }$ , velocity ${ \pmb v } _ { 1 } = d { \pmb r } _ { 1 } / d t$ , and acceleration $\pmb { a } _ { 1 } = d \pmb { v } _ { 1 } / d t$ , and a second body of mass $m _ { 2 }$ , position $r _ { 2 }$ , velocity ${ \pmb v } _ { 2 } = d { \pmb r } _ { 2 } / d t$ , and acceleration ${ \pmb a } _ { 2 } =$ $d { \pmb v } _ { 2 } / d t$ . We place the origin of the coordinate system at the system’s barycenter $\pmb { R }$ , so that $m _ { 1 } \pmb { r } _ { 1 } + m _ { 2 } \pmb { r } _ { 2 } = \pmb { 0 } .$ . The position of each body is then given by

$$
r _ { 1 } = \frac { m _ { 2 } } { m } r , \qquad r _ { 2 } = - \frac { m _ { 1 } } { m } r ,
$$

in which $m : = m _ { 1 } + m _ { 2 }$ is the total mass and $r : = r _ { 1 } - r _ { 2 }$ the separation between bodies. Similar relations hold between $\pmb { v } _ { 1 } , \pmb { v } _ { 2 }$ and the relative velocity $\pmb { v } : = \pmb { v } _ { 1 } - \pmb { v } _ { 2 } = d \pmb { r } / d t$ . The relative acceleration $\pmb { a } : = \pmb { a } _ { 1 } - \pmb { a } _ { 2 } = d \pmb { v } / d t$ is obtained from Eq. (1.220) by removing all terms that involve the multipole moments of each body (which vanish when the bodies are spherical); we have

$$
\pmb { a } = - \frac { G m } { r ^ { 2 } } \pmb { n } ,
$$

where $r : = | r |$ is the distance between bodies, and ${ \pmb n } : = { \pmb r } / r$ a unit vector that points from body 2 to body 1. This is the equation of motion for the relative orbit, and thanks to Eq. (3.1), its solution is sufficient to determine the individual motion of each body. Equation (3.2) can be interpreted as describing the motion of a fictitious particle at position $r$ in the field of a gravitating center of mass $m$ at $\mathbf { \nabla } \mathbf { r } = \mathbf { 0 }$ ; as such our two-body problem has been reformulated as an effective one-body problem. This radical simplification of the original problem, which involved six independent degrees of freedom (the three components of each position vector) instead of the current three (the three components of the separation vector), is a consequence of the conservation of total momentum, which implies that the motion of the barycenter position $\pmb { R }$ is uniform and therefore trivial.

According to Eq. (1.221), the total energy of the two-body system is given by

$$
E = \frac { 1 } { 2 } \mu v ^ { 2 } - \frac { G \mu m } { r } ,
$$

in which $\mu : = m _ { 1 } m _ { 2 } / m$ is the reduced mass of the system; to obtain this expression we once more dropped all terms involving multipole moments, and set $V = d \pmb { R } / d t = \pmb { 0 }$ in the barycentric frame. The system’s total angular momentum is given by Eq. (1.204), which reduces to

$$
L = m _ { 1 } \pmb { r } _ { 1 } \times \pmb { v } _ { 1 } + m _ { 2 } \pmb { r } _ { 2 } \times \pmb { v } _ { 2 } = \mu \pmb { r } \times \pmb { v }
$$

for a two-body system. Because the bodies are assumed to have no spin, and because the angular momentum is contained entirely in the orbital motion, we use the standard notation $\pmb { L }$ instead of $\pmb { J }$ for the angular-momentum vector. It is a simple matter to verify that $d E / d t = 0$ by virtue of Eq. (3.2), and that $d L / d t = \mathbf { 0 }$ by virtue of the sole fact that the acceleration $\pmb { a }$ is directed along $r$ .

The constancy of the angular-momentum vector has far-reaching consequences on the motion of the bodies. Because $\pmb { L }$ is a constant vector orthogonal to both $r$ and $\pmb { v }$ , the motion must take place in a fixed plane that is at all times perpendicular to $\pmb { L }$ . We therefore have achieved another radical simplification of the problem: by confining the motion to a plane we have eliminated one degree of freedom from the original three associated with the effective one-body problem.

# 3.2.2 Orbital plane

We take the orbital plane to coincide with the $x { - } y$ plane of the coordinate system, and we align $\pmb { L }$ with the $z$ -direction. To simplify the notation in subsequent developments, we write

$$
\begin{array} { r } { L = \mu h , \qquad h : = r \times v = h e _ { z } , } \end{array}
$$

with $h : = | h |$ denoting the magnitude of the constant vector $r \times v$ .

It is helpful to describe the motion with the polar coordinates $r$ and $\phi$ , defined such that the components of the separation vector are given by

$$
\boldsymbol { r } = [ r \cos \phi , r \sin \phi , 0 ] ;
$$

both $r$ and $\phi$ depend on time. A vectorial basis in the orbital plane can be built from the constant unit vectors $\boldsymbol { e } _ { x }$ and $e _ { y }$ , but it is useful to introduce also the time-dependent unit

vectors

$$
\pmb { n } : = [ \cos \phi , \sin \phi , 0 ] , \qquad \pmb { \lambda } : = [ - \sin \phi , \cos \phi , 0 ] ,
$$

which are closely tied to the description of the orbital motion. The vector ${ \pmb n } : = { \pmb r } / r$ points from body 2 to body 1, while $\gimel$ is orthogonal to it. The vectors satisfy

$$
\frac { d \pmb { n } } { d \phi } = \lambda , \qquad \frac { d \pmb { \lambda } } { d \phi } = - \pmb { n } .
$$

The basis is completed with $\boldsymbol { e } _ { z }$ , which is normal to the orbital plane and aligned with the angular-momentum vector.

The vectors $r , v$ , and $\pmb { a }$ can each be decomposed in the orbital basis. Simple computations involving Eqs. (3.8) produce

$$
\begin{array} { l } { { r = r \pmb { n } , } } \\ { { \pmb { v } = \dot { r } \pmb { n } + r \dot { \phi } \lambda , } } \\ { { \pmb { a } = \left( \ddot { r } - r \dot { \phi } ^ { 2 } \right) \pmb { n } + \cfrac { 1 } { r } \cfrac { d } { d t } \left( r ^ { 2 } \dot { \phi } \right) \lambda , } } \end{array}
$$

in which an overdot indicates differentiation with respect to $t$

# 3.2.3 First integrals

The acceleration of Eq. (3.9) may now be inserted within Eq. (3.2), and the absence of a component along $\gimel$ immediately implies that $r ^ { 2 } { \dot { \phi } }$ is a constant of the motion. Because $r ^ { 2 } { \dot { \phi } }$ is equal to the $z$ (and only non-vanishing) component of the vector $r \times v$ , we have rediscovered the statement of angular-momentum conservation. Taking Eq. (3.5) into account, we have that

$$
r ^ { 2 } { \dot { \phi } } = h .
$$

In this form we can see that conservation of angular momentum gives rise to Kepler’s second law: $r ( r d \phi )$ is twice the area swept by the orbit as it advances by an angle $d \phi$ , and $r ^ { 2 } { \dot { \phi } }$ is twice the area swept per unit time; conservation of angular momentum implies equal areas for equal times.

The radial component of the equation of motion yields $\ddot { r } - r \dot { \phi } ^ { 2 } = - G m / r ^ { 2 }$ , or

$$
{ \ddot { r } } - { \frac { h ^ { 2 } } { r ^ { 3 } } } = - { \frac { G m } { r ^ { 2 } } }
$$

after involving Eq. (3.10). This second-order differential equation for $\boldsymbol { r } ( t )$ can be integrated once by applying the $\dot { r }$ -trick: multiply the equation by $\dot { r }$ and recognize that each term is a total derivative with respect to time. Integration produces

$$
{ \frac { 1 } { 2 } } { \dot { r } } ^ { 2 } + { \frac { h ^ { 2 } } { 2 r ^ { 2 } } } - { \frac { G m } { r } } = \varepsilon ,
$$

in which $\varepsilon$ is another constant of the motion. From Eq. (3.3) it is easy to see that $E = \mu \varepsilon$ , and we have rediscovered the statement of energy conservation.

![](images/55f411323edea1292dbe5914fb86741ad97f6bbe2835d72a593520fa05283392.jpg)  
Effective potential for Kepler’s problem, together with lines of constant $\varepsilon$ . The radial variable r is presented in units of $p : = h ^ { 2 } / ( G m )$ , and $V _ { \mathrm { e f f } }$ is presented in units of $G m / p$ The regions of allowed motion correspond to $\varepsilon \ge V _ { \mathrm { e f f } } ( r )$ , and turning points occur when $\varepsilon = V _ { \mathrm { e f f } } ( r )$ . The different types of Keplerian motion (hyperbolic, parabolic, and elliptical) are shown.

It is instructive to rewrite Eq. (3.12) in the form

$$
\frac { 1 } { 2 } \dot { r } ^ { 2 } = \varepsilon - V _ { \mathrm { e f f } } ( r ) ,
$$

in which the effective radial potential is defined as

$$
V _ { \mathrm { e f f } } ( r ) : = \frac { h ^ { 2 } } { 2 r ^ { 2 } } - \frac { G m } { r } .
$$

This new form allows us to explore the qualitative features of Keplerian motion without having to perform additional calculations. In Fig. 3.1 we display a plot of $V _ { \mathrm { e f f } } ( r )$ for $h \neq 0$ , with zero on the vertical axis denoting the limiting value of the effective potential as $r  \infty$ . The potential consists of an attractive (negative) gravitational well, and a repulsive (positive) centrifugal barrier rising to infinity as $r \to 0$ . Motion is allowed when $\dot { r } ^ { 2 } \geq 0$ , that is, when $\varepsilon \ge V _ { \mathrm { e f f } } ( r )$ , and regions where this condition is met are easily identified in the figure. A turning point occurs when $\dot { r } = 0$ and $\varepsilon = V _ { \mathrm { e f f } } ( r )$ ; at such points the radial velocity changes sign, and the motion changes from incoming to outgoing, or from outgoing to incoming.

We can easily imagine how a particle would move in this effective potential. If the particle has an energy $\varepsilon > 0$ , then there is a single turning point at some innermost radius $r _ { \mathrm { m i n } }$ , and the motion takes place for √ $r \geq r _ { \operatorname* { m i n } }$ . The particle starts at infinity with a negative radial velocity $\dot { r } = - \sqrt { 2 \varepsilon }$ and a vanishing angular velocity $\dot { \phi }$ . As $r$ decreases, $\dot { r }$ becomes increasingly negative, and $\dot { \phi }$ increases to obey conservation of angular momentum, until the particle reaches the turning point at $r = r _ { \mathrm { m i n } }$ . At this point $\dot { r }$ turns positive, and the particle begins its way back to infinity. As we shall see below, the particle follows a hyperbola in the orbital plane, and motion with $\varepsilon > 0$ is known as hyperbolic motion. Such an orbit is not bound to the gravitating center, as revealed by the fact that the total energy is dominated by (positive) kinetic energy instead of (negative) gravitational potential energy. The limiting case of an unbound orbit corresponds to $\varepsilon = 0$ . Here the particle begins from rest at infinity, proceeds to a single turning point at $r = r _ { \mathrm { m i n } }$ , and returns to a state of rest at infinity. In this case the path is a parabola in the orbital plane, and motion with $\varepsilon = 0$ is known as parabolic motion.

When $\varepsilon < 0$ , that is, when gravitational potential energy dominates over kinetic energy, the diagram reveals that there are now two turning points at $r = r _ { \mathrm { m i n } }$ and $r = r _ { \operatorname* { m a x } }$ . In this case the orbital motion is bound to the gravitating center, and takes place between the innermost and outermost radii. We shall see that the bound orbit describes an ellipse, and motion with $\varepsilon < 0$ is known as elliptical motion. A special case of elliptical motion occurs when $\varepsilon$ is made equal to the minimum value of the effective potential. In this case the turning points merge to a single radius $r _ { 0 }$ , and motion proceeds at this fixed radius; this is a circular orbit with $h ^ { 2 } = G m r _ { 0 }$ , $\dot { \phi } = \sqrt { G m / r _ { 0 } ^ { 3 } }$ , and $\varepsilon = - G m / ( 2 r _ { 0 } )$ .

The preceding discussion was couched in terms of a particle moving in the effective potential $V _ { \mathrm { e f f } } ( r )$ . It is important to understand, however, that this “particle” at position $\mathbf { } r ( t )$ is in fact a fictitious representation of the relative orbit, which, as we saw back in Eq. (3.2), is subjected to a fictitious gravitating center of mass $m$ at $\mathbf { \nabla } \mathbf { r } = \mathbf { 0 }$ . The motion described previously is therefore a description of the relative orbital motion. But thanks to Eqs. (3.1), the motion of each body is merely a scaled version of the relative motion, and it can be described in the same language; the bodies move about each other on opposite sides of the barycenter. In the limit of small mass ratios, $m _ { 1 } / m _ { 2 } \ll 1$ , it becomes increasingly true that $r _ { 1 } \to r$ and $r _ { 2 } \to \mathbf { 0 }$ ; in this limiting case $m _ { 1 }$ becomes a test mass in the field of $m _ { 2 }  m$ , its orbit coincides with the relative orbit, and $m _ { 2 }$ stays put at the barycentric position.

# 3.2.4 Solution to Kepler’s problem

# Formal solution; integrable systems

Formally, a solution to Kepler’s problem can be obtained by integrating Eq. (3.13) to get

$$
t - t _ { i } = \pm \int _ { r _ { i } } ^ { r } \frac { d r ^ { \prime } } { \sqrt { 2 [ \varepsilon - V _ { \mathrm { e f f } } ( r ^ { \prime } ) ] } } ,
$$

inverting the result for $\boldsymbol { r } ( t )$ , and integrating Eq. (3.10) to get

$$
\phi - \phi _ { i } = h \int _ { t _ { i } } ^ { t } \frac { d t ^ { \prime } } { r ( t ^ { \prime } ) ^ { 2 } } ,
$$

which gives $\phi ( t )$ . In these equations, $t _ { i }$ is the time at which $r = r _ { i }$ , and $\phi _ { i }$ is the orbital angle at time $t _ { i }$ . By following this procedure we convert the task of solving the secondorder differential equations of (3.2) to the task of performing two integrations, or, to use an older but still popular terminology, evaluating two quadratures. When a dynamical problem such as this one can be reduced to doing quadratures, the problem is said to be completely integrable. A full discussion of integrable systems is beyond the scope of this book, but roughly speaking, a dynamical system is completely integrable when it possesses a sufficient number of conserved quantities. In the case of Kepler’s problem, it is the constancy of total momentum (which allowed us to eliminate the motion of the barycenter), of total angular momentum (which allowed us to restrict the motion to a plane and to reduce the angular equation to $\dot { \phi } = h / r ^ { 2 }$ ), and of energy (which resulted in an equation for $\dot { r } ^ { 2 }$ ) that make the problem completely integrable.

Completely integrable systems are mathematically elegant, and are extremely convenient when they come along, but unfortunately they are rather rare in physics. Fortunately for us, however, the Kepler problem is one of them. More generally, because Eq. (3.15) is valid for any effective potential $V _ { \mathrm { e f f } } ( r )$ , motion in any spherically symmetric, static potential is always integrable.

The formal solutions of Eqs. (3.15) and (3.16) are not very useful from a practical point of view. We could try to carry out the integrals explicitly, but the results would not be illuminating. Alternatively, we could evaluate the integrals numerically, but the resulting tables would be of limited utility, and they would provide very little insight. We shall therefore proceed differently.

# Spatial solution; conic sections

As a first step toward integrating the equations of motion, we eliminate $t$ from the system of equations (3.10), (3.11), and adopt the orbital angle $\phi$ as independent variable. This strategy allows us to unravel the spatial aspects of the orbit – its shape in the orbital plane – and we shall return to the problem of describing the motion in time at a later stage. We also adopt $u : = 1 / r$ as a convenient substitute for $r$ , and derive a differential equation for it by applying the chain rule of differential calculus. For example, we have that $\dot { r } = - u ^ { - 2 } \dot { u } =$ $- u ^ { - 2 } \dot { \phi } u ^ { \prime } = - h u ^ { \prime }$ and $\ddot { r } = - h ^ { 2 } u ^ { 2 } u ^ { \prime \prime }$ , in which a prime indicates differentiation with respect to $\phi$ . Making the substitutions within Eq. (3.11), we quickly arrive at

$$
u ^ { \prime \prime } + u = \frac { G m } { h ^ { 2 } } .
$$

The general solution to this simple equation is

$$
u = \frac { G m } { h ^ { 2 } } \big [ 1 + e \cos ( \phi - \omega ) \big ] ,
$$

in which $e$ and $\omega$ are arbitrary constants of integration.

Returning to the original radial variable, the spatial solution to Kepler’s problem is

$$
r = \frac { p } { 1 + e \cos ( \phi - \omega ) } ,
$$

in which

$$
p : = \frac { h ^ { 2 } } { G m }
$$

is a quantity known as the orbit’s semi-latus rectum. We note that a solution with $e < 0$ is equivalent to one with $e > 0$ , provided that $\omega$ is changed to $\omega + \pi$ ; we will adopt the convention that $e$ is never negative.

The curve described by Eq. (3.19) is a conic section, an ellipse when $e < 1$ , a hyperbola when $e > 1$ , and a parabola when $e = 1$ , with $r = 0$ situated at one of the curve’s foci. The parameter $e$ is called the eccentricity of the orbit. Note that $r$ achieves a minimum when $\phi = \omega$ . This is the point of closest approach in the orbit, called the periapsis or pericenter, and $\omega$ is known as the longitude of pericenter ; its role is to fix the orientation of the orbit in the orbital plane. The term pericenter is usually adapted to reflect the identity of specific astronomical bodies. For example, we have perihelion for the Sun, perigee for the Earth, perijove for Jupiter, and periastron for binary star systems. No consensus has emerged to date for the closest approach to a black hole, but the word peribothron is gaining popularity; it was crafted by our colleague Sterl Phinney from the Greek root “bothros,” which means hole or pit.

We examine first the elliptical orbits with $e < 1$ . In this case the motion described by Eq. (3.19) is periodic, with period $\Delta \phi = 2 \pi$ , and we have recovered Kepler’s first law, that planets move on elliptical paths around the Sun. We have already seen that $\phi = \omega$ describes the periapsis or pericenter, and we now see that $\phi = \omega + \pi$ describes the point of greatest separation, called apoapsis or apocenter. The pericenter and apocenter distances from the focus are given by

$$
r _ { \mathrm { p e r i } } = \frac { p } { 1 + e } , \quad r _ { \mathrm { a p o } } = \frac { p } { 1 - e } .
$$

The sum of these is the major axis of the ellipse, and we define the semi-major axis $a$ to be

$$
a : = \frac { 1 } { 2 } ( r _ { \mathrm { p e r i } } + r _ { \mathrm { a p o } } ) = \frac { p } { 1 - e ^ { 2 } } .
$$

The semi-latus rectum can also be expressed in terms of these quantities:

$$
p = { \frac { 2 r _ { \mathrm { p e r i } } r _ { \mathrm { a p o } } } { r _ { \mathrm { p e r i } } + r _ { \mathrm { a p o } } } } .
$$

A special case of elliptical motion occurs when $e = 0$ . In this case $r = p$ is constant, and the orbit is circular.

We examine next the hyperbolic and parabolic orbits with $e \geq 1 .$ . In these cases the motion is no longer periodic, and the notion of apocenter ceases to be meaningful. Similarly, while we can still define a quantity $a$ related to $p : = h ^ { 2 } / ( G m )$ by $a = p / ( 1 - e ^ { 2 } )$ , this quantity also loses its usefulness, being negative for hyperbolic orbits and formally infinite for parabolic orbits. The pericenter still occurs at $\phi = \omega$ , with $r _ { \mathrm { p e r i } } = p / ( 1 + e )$ , and $r$ approaches infinity as $\cos ( \phi - \omega )  - e ^ { - 1 }$ . It is easy to show that the net change between the asymptotic angle $\phi _ { \infty } ^ { \mathrm { i n } }$ of the incoming part of the orbit and the asymptotic angle $\phi _ { \infty } ^ { \mathrm { { o u t } } }$ of the outgoing orbit is given by

$$
\Delta \phi : = \phi _ { \infty } ^ { \mathrm { o u t } } - \phi _ { \infty } ^ { \mathrm { i n } } = 2 \operatorname { a r c c o s } ( - e ^ { - 1 } ) .
$$

This reduces to $\Delta \phi = 2 \pi$ when $e = 1$ .

Returning to the general case with any $e$ , we invoke Eqs. (3.10), (3.19), and (3.20) to derive the following useful expressions for the radial and angular velocities of a Keplerian

orbit:

$$
\begin{array} { l } { \displaystyle { \dot { r } = \sqrt { \frac { G m } { p } } e \sin ( \phi - \omega ) , } } \\ { \displaystyle { \dot { \phi } = \sqrt { \frac { G m } { p ^ { 3 } } } \big [ 1 + e \cos ( \phi - \omega ) \big ] ^ { 2 } . } } \end{array}
$$

From these we obtain

$$
v ^ { 2 } = { \frac { G m } { p } } \big [ 1 + 2 e \cos ( \phi - \omega ) + e ^ { 2 } \big ] = G m \bigg ( { \frac { 2 } { r } } - { \frac { 1 - e ^ { 2 } } { p } } \bigg )
$$

for the squared orbital velocity. From Eq. (3.12) we get an expression for the total energy $E : = \mu \varepsilon$ ,

$$
E = - G \mu m \frac { 1 - e ^ { 2 } } { 2 p } = - \frac { G \mu m } { 2 a } .
$$

We recall that $\mu : = m _ { 1 } m _ { 2 } / m$ is the system’s reduced mass, and that $a$ is related to $p$ by Eq. (3.22). And finally, from Eq. (3.5) we have that

$$
\pmb { L } = \mu \sqrt { G m p } \pmb { e } _ { z }
$$

is the system’s total angular momentum.

# Motion in time; eccentric anomaly

So far we have determined the orbit as a function of $\phi$ , and the description involves three arbitrary constants, $p , e$ , and $\omega$ , known as orbital elements. As we have seen, the semilatus rectum $p$ is a substitute for angular momentum, while the associated semi-major axis $a : = p / ( 1 - e ^ { 2 } )$ is a substitute for orbital energy. The true nature of the longitude of pericenter $\omega$ will be revealed below.

The description of the orbit is completed by giving $\phi$ as a function of time. This can be accomplished by integrating Eq. (3.25b), in the form of

$$
t - T = \sqrt { \frac { p ^ { 3 } } { G m } } \int _ { \omega } ^ { \phi } \frac { d \phi ^ { \prime } } { \left[ 1 + e \cos ( \phi ^ { \prime } - \omega ) \right] ^ { 2 } } ,
$$

where the constant $T$ , called the time of pericenter passage, is a fourth orbital element.   
This equation can be inverted to give $\phi ( t )$ , and Kepler’s problem is now solved.

There remains, however, the practical problem of evaluating the integral of Eq. (3.29). We henceforth specialize to elliptical motion, and introduce another running parameter on the orbit, known as the eccentric anomaly $u$ . This is defined by the relations

$$
\cos f = { \frac { \cos u - e } { 1 - e \cos u } } , \qquad \sin f = { \frac { \sqrt { 1 - e ^ { 2 } } \sin u } { 1 - e \cos u } } ,
$$

in which $f : = \phi - \omega$ is the true anomaly, the orbital angle as measured from the pericenter. The inverted relations are

$$
\cos u = { \frac { \cos f + e } { 1 + e \cos f } } , \qquad \sin u = { \frac { \sqrt { 1 - e ^ { 2 } } \sin f } { 1 + e \cos f } } ,
$$

and these relationships are neatly summarized by the half-angle formula

$$
\tan { \frac { 1 } { 2 } } f = \sqrt { \frac { 1 + e } { 1 - e } } \tan { \frac { 1 } { 2 } } u .
$$

These equations reveal that $u = 0$ at pericenter (where $\phi = \omega$ and $f = 0$ ), that $u = \pi$ at apocenter (where $f = \pi$ ), and that $u = 2 \pi$ at the end of a complete orbital cycle. Other useful relations are

$$
{ \frac { d f } { d u } } = { \frac { \sqrt { 1 - e ^ { 2 } } } { 1 - e \cos u } } , \qquad { \frac { d u } { d f } } = { \frac { \sqrt { 1 - e ^ { 2 } } } { 1 + e \cos f } } .
$$

The eccentric anomaly gives rise to a useful alternative description of the orbit. Making the substitutions reveals that

$$
\begin{array} { l } { r = a ( 1 - e \cos u ) , } \\ { \dot { r } = \sqrt { \frac { G m } { a } } \frac { e \sin u } { 1 - e \cos u } , } \\ { \dot { u } = \sqrt { \frac { G m } { a ^ { 3 } } } \frac { 1 } { 1 - e \cos u } , } \\ { v ^ { 2 } = \frac { G m } { a } \frac { 1 + e \cos u } { 1 - e \cos u } = G m \bigg ( \frac { 2 } { r } - \frac { 1 } { a } \bigg ) . } \end{array}
$$

The main advantage of this description resides in Eq. (3.34c), which can be immediately integrated to give

$$
t - T = { \sqrt { \frac { a ^ { 3 } } { G m } } } { \big ( } u - e \sin u { \big ) } .
$$

This is known as Kepler’s equation, which gives $t$ as a simple function of the eccentric anomaly $u$ . The equation can be inverted to yield $u ( t )$ , see $\mathrm { B o x } \ 3 . 1$ , and this can finally be inserted within Eqs. (3.30) or (3.32) to express $f$ as a function of time.

A description in terms of the eccentric anomaly is often a judicious choice when it is required to integrate over time. As a simple example, we can calculate the orbital period $P$ of an elliptical orbit using Eq. (3.35). When $u$ increases by $2 \pi$ , $t$ increases by $P$ , and with very little effort we find that

$$
P = 2 \pi { \sqrt { \frac { a ^ { 3 } } { G m } } } .
$$

While the period can also be obtained directly from Eq. (3.29), the integration is far more laborious. That $P$ is proportional to $a ^ { 3 / 2 }$ is Kepler’s third law of planetary motion.

We wish to find the eccentric anomaly $u$ that corresponds to a given time $t$ . For this purpose it is useful to rewrite Kepler’s equation as

$$
u - e \sin u = M : = \sqrt { \frac { G m } { a ^ { 3 } } } ( t - T ) = 2 \pi \frac { t - T } { P } ,
$$

and to map the mean anomaly $M$ to the interval $0 \leq M < 2 \pi$ by subtracting an appropriate multiple of $P$ from $t - T$ .

A time-honored method to solve Kepler’s equation is based on Newton’s root-finding method. It is an implementation of the iterative scheme

$$
u _ { n + 1 } = u _ { n } + \frac { M - ( u _ { n } - e \sin u _ { n } ) } { 1 - e \cos u _ { n } }
$$

until $u$ converges to the desired accuracy. The iterations are seeded with $u _ { 0 } = M$ , and the scheme typically requires a small number of iterations (fewer than six or so) for machine-precision accuracy.

# Constancy of the pericenter; Runge–Lenz vector

We have seen that Keplerian motion within a fixed orbital plane is characterized by four constants of the motion, the orbital elements $p , e , \omega$ , and $T$ . We have seen that constancy of $p$ is tied to conservation of angular momentum, and that constancy of $a : = p / ( 1 - e ^ { 2 } )$ is tied to conservation of energy (so that constancy of $e$ is also assured). In addition, the appearance of $T$ as an integration constant was expected from the fact that the gravitational potential $G m / r$ does not depend explicitly on time. Constancy of $\omega$ , however, is not related to the spherical symmetry of the potential nor its time independence; we must seek a deeper cause. It is worth emphasizing that constancy of $\omega$ is a very important property of a Keplerian orbit: It ensures that the orientation of the orbit stays fixed, that the position of the pericenter does not move, and when the orbit is bound, that the orbit retraces itself after each orbital cycle.

The constancy of $\omega$ is the result of a hidden symmetry of Kepler’s problem, associated with the specific $1 / r$ nature of the gravitational potential; the symmetry does not exist for other potentials. The symmetry gives rise to a conservation statement for the Runge–Lenz vector, defined by

$$
\boldsymbol { A } : = \frac { \pmb { v } \times \pmb { h } } { G m } - \pmb { n } ,
$$

in which $\pmb { h } : = \pmb { r } \times \pmb { v }$ and ${ \pmb n } : = { \pmb r } / r$ . A short computation using $\pmb { a } = - G m \pmb { n } / r ^ { 2 }$ and ${ \dot { r } } = \pmb { n } \cdot \pmb { v }$ shows that

$$
\frac { d A } { d t } = \bf 0 ,
$$

and the manipulations do indeed reveal that constancy of $\pmb { A }$ relies on the specific form of the gravitational acceleration. The Runge–Lenz vector can be evaluated explicitly by making use of the Keplerian results displayed previously, including Eqs. (3.5), (3.7), (3.9),

and (3.25). The result is

$$
\begin{array} { r } { \pmb { A } = e \big ( \cos \omega \pmb { e } _ { x } + \sin \omega \pmb { e } _ { y } \big ) , } \end{array}
$$

and it reveals that the vector points in the fixed direction of the pericenter. The vector has a length $e$ , and constancy of $\pmb { A }$ as a vector implies that both $e$ and $\omega$ are constants of the motion.

# 3.2.5 Keplerian orbits in space

The description of Keplerian orbits given previously achieved a remarkable degree of simplicity, thanks in part to conservation of angular momentum, which guarantees that the motion takes place in a fixed orbital plane. The description was entirely “orbit-centric,” in that the reference frame was selected specifically to give a simple description of the orbital plane; and the simplicity was achieved largely by adopting the polar coordinates $( r , \phi )$ attached to the orbital plane. In many applications this description is entirely adequate, but in many others it is necessary to provide a fuller description that is less orbit-centric. For example, one might wish to describe the motion of two or more planets around the Sun (under the assumption that the Sun’s motion and inter-planet interactions are negligible), with each planet moving in a different orbital plane; in such a case one would like to adopt the same reference frame for all the planets. Another example, which will be explored in some detail below, involves a two-body system perturbed by external bodies, or by a deformation of each body from a spherical configuration; these perturbations cause the orbital plane to move, and these motions must be described relative to a fixed reference frame. For such applications we require a fuller description of the orbital motion in space, relative to a reference frame that is not attached to the orbital plane.

We were already given an orbital frame with coordinates $( x , y , z )$ , such that the fixed orbital plane coincides with the $x { - } y$ plane, and such that the angular-momentum vector is aligned with the $z$ -direction. The orbital frame comes with the constant basis vectors $\boldsymbol { e } _ { x }$ , $e _ { y }$ , and $\boldsymbol { e } _ { z }$ , as well as the time-dependent basis ${ \mathbf { } } n , \lambda$ , and $e _ { z }$ . We now introduce a fundamental frame with coordinates $( X , Y , Z )$ , and seek to describe the orbital motion in this new frame. We adopt the $X { - } Y$ plane as a reference plane in the new frame, and the $Z$ -axis as a reference direction. The fundamental frame comes with a constant vectorial basis $e _ { X } , e _ { Y }$ , and $e _ { Z }$ . We assume that the orbital and fundamental frames share the same origin, so that $X = Y = Z = 0$ when $x = y = z = 0$ . The choice of fundamental frame is arbitrary, and is often dictated by convention or convenience. For example, in the description of planetary motion in the solar system, the reference plane is chosen to coincide with Earth’s own orbital plane (called the ecliptic). As another example, in the description of satellites orbiting the Earth, the fundamental plane is chosen to coincide with Earth’s equatorial plane. In each case the direction of the $X \cdot$ -axis is selected by convention.

The description of the orbital motion relative to the fundamental frame requires the introduction of additional orbital elements. The situation is represented in Fig. 3.2, which shows the orbital plane crossing the fundamental plane at an angle $\iota$ called the inclination; this is the angle between the $z$ -direction of the orbital frame and the $Z$ -direction of the fundamental frame. The line of intersection between the two planes is known as the line of nodes, and the point at which the orbit cuts the fundamental plane from below is the ascending node; the descending node is the point at which the orbit cuts the plane from above. The angle $\Omega$ between the $X$ -direction and the line of nodes is the longitude of the ascending node. The diagram also shows $\omega$ , the longitude of pericenter introduced previously, which is now defined specifically as the angle between the line of nodes and the direction to the pericenter, as measured in the orbital plane. In this new description of the orbital motion, it is conventional to align the $x$ -axis of the orbital plane with the direction to the pericenter, thereby deviating from our previous practice. And finally, the diagram shows the true anomaly $f$ , the angle between the separation vector $r$ and the direction to the pericenter, as measured in the orbital plane. The complete listing of orbital elements therefore consists of the principal elements $p$ and $e$ , the positional elements $\iota , \Omega$ , and $\omega$ , and the time element $T$ ; the total number of elements is six, and it is no accident that this number corresponds to the number of initial conditions required to select a unique solution to Kepler’s problem.

![](images/623758261ae5a85d1e4adb25c7df1f273a9679d8ed248ab7b983041ad7f9c52a.jpg)  
Fig. 3.2 Orbital motion viewed in the fundamental reference frame.

With these definitions and conventions, we show in $\mathrm { B o x } 3 . 2 $ that the components of the separation vector $r$ in the fundamental $( X , Y , Z )$ frame are given by

$$
\begin{array} { r l } & { r ^ { X } = r \big [ \cos \Omega \cos ( \omega + f ) - \cos \iota \sin \Omega \sin ( \omega + f ) \big ] , } \\ & { r ^ { Y } = r \big [ \sin \Omega \cos ( \omega + f ) + \cos \iota \cos \Omega \sin ( \omega + f ) \big ] , } \\ & { r ^ { Z } = r \sin \iota \sin ( \omega + f ) , } \end{array}
$$

in which $r = p / ( 1 + e \cos f )$ . Differentiation with respect to time and involvement of Eqs. (3.25) give us the components of the velocity vector,

$$
v ^ { X } = - \sqrt { \frac { G m } { p } } \Big \{ \cos \Omega \big [ \sin ( \omega + f ) + e \sin \omega \big ] + \cos \iota \sin \Omega \big [ \cos ( \omega + f ) + e \cos \omega \big ] \Big \} ,
$$

$$
v ^ { Y } = - \sqrt { \frac { G m } { p } } \Big \{ \sin \Omega \big [ \sin ( \omega + f ) + e \sin \omega \big ] - \cos \iota \cos \Omega \big [ \cos ( \omega + f ) + e \cos \omega \big ] \Big \} ,
$$

$$
s v ^ { Z } = \sqrt { \frac { G m } { p } } \sin \iota \bigl [ \cos ( \omega + f ) + e \cos \omega \bigr ] .
$$

The results of Box 3.2 also allow us to express the orbital basis vectors $\pmb { n }$ and $\gimel$ as

$$
\begin{array} { r l } & { \pmb { n } = \left[ \cos \Omega \cos ( \omega + f ) - \cos \iota \sin \Omega \sin ( \omega + f ) \right] \pmb { e } _ { X } } \\ & { \quad ~ + \left[ \sin \Omega \cos ( \omega + f ) + \cos \iota \cos \Omega \sin ( \omega + f ) \right] \pmb { e } _ { Y } } \\ & { \quad ~ + \sin \iota \sin ( \omega + f ) \pmb { e } _ { Z } } \end{array}
$$

and

$$
\begin{array} { r l } & { \lambda = \left[ - \cos \Omega \sin ( \omega + f ) - \cos \iota \sin \Omega \cos ( \omega + f ) \right] e _ { X } } \\ & { \quad \quad + \left[ - \sin \Omega \sin ( \omega + f ) + \cos \iota \cos \Omega \cos ( \omega + f ) \right] e _ { Y } } \\ & { \quad \quad + \sin \iota \cos ( \omega + f ) e _ { Z } . } \end{array}
$$

In addition, the direction to the pericenter is given by

$$
\begin{array} { r l } & { \boldsymbol { e } _ { x } = \left( \cos \Omega \cos \omega - \cos \iota \sin \Omega \sin \omega \right) \boldsymbol { e } _ { X } } \\ & { \qquad + \left( \sin \Omega \cos \omega + \cos \iota \cos \Omega \sin \omega \right) \boldsymbol { e } _ { Y } } \\ & { \qquad + \sin \iota \sin \omega \boldsymbol { e } _ { Z } , } \end{array}
$$

while the direction of the angular-momentum vector is

$$
\pmb { e } _ { z } = \sin \iota \sin \Omega \pmb { e } _ { X } - \sin \iota \cos \Omega \pmb { e } _ { Y } + \cos \iota \pmb { e } _ { Z } .
$$

In terms of these we have that $A = e \pmb { e } _ { x }$ and $\pmb { h } = h \pmb { e } _ { z }$ , with $h : = { \sqrt { G m p } }$

The description of the orbital motion in the fundamental frame allows us to provide simple definitions for the orbital elements. We have that

$$
\begin{array} { c } { \displaystyle p : = \frac { h ^ { 2 } } { G m } , } \\ { \displaystyle e : = \left| { \cal A } \right| , } \\ { \displaystyle \cos \iota : = e _ { z } \cdot e _ { Z } = \frac { h \cdot e _ { Z } } { h } , } \\ { \displaystyle \sin \iota \sin \Omega : = e _ { z } \cdot e _ { \chi } = \frac { h \cdot e _ { \chi } } { h } , } \\ { \displaystyle \sin \iota \sin \omega : = e _ { \chi } \cdot e _ { Z } = \frac { \boldsymbol A \cdot e _ { Z } } { e } . } \end{array}
$$

To this we may add $a : = p / ( 1 - e ^ { 2 } )$ and the time element $T$ , which is defined by Eq. (3.29). These definitions are elementary and fundamental, because they are formulated directly in terms of the fundamental vectors of the problem, the reduced angular-momentum vector $\pmb { h } = \pmb { r } \times \pmb { v }$ and the Runge–Lenz vector $\pmb { A }$ defined by Eq. (3.37). They will play a large role in the next section.

A close examination of Fig. 3.2 and some thought reveal that the fundamental $( X , Y , Z )$ frame can be obtained from the orbital $( x , y , z )$ frame by a sequence of three rotations. The first is a rotation $\mathsf { R } _ { 1 }$ by an angle $- \omega$ around the z-axis, to align the rotated $\chi$ -axis with the line of nodes. The second is a rotation ${ \sf R } _ { 2 }$ by an angle $- \iota$ around the new x-axis, to align the rotated z-axis with the final Z-axis. The third is a rotation ${ \sf R } _ { 3 }$ by an angle $- \Omega$ around the new z-axis, to align the rotated $\chi$ -axis with the final $\chi .$ -axis. The rotation matrices are given by

$$
\begin{array} { r } { \mathsf { R } _ { 1 } = \left( \begin{array} { c c c } { \cos \omega } & { - \sin \omega } & { 0 } \\ { \sin \omega } & { \cos \omega } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right) , \qquad \mathsf { R } _ { 2 } = \left( \begin{array} { c c c } { 1 } & { 0 } & { 0 } \\ { 0 } & { \cos \iota } & { - \sin \iota } \\ { 0 } & { \sin \iota } & { \cos \iota } \end{array} \right) , } \end{array}
$$

$$
\mathsf { R } _ { 3 } = \left( \begin{array} { c c c } { \cos \Omega } & { - \sin \Omega } & { 0 } \\ { \sin \Omega } & { \cos \Omega } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right) ,
$$

and the overall transformation between the orbital and fundamental frames is ${ \sf X } = { \sf R } _ { 3 } { \sf R } _ { 2 } { \sf R } _ { 1 } { \sf x } ,$ with x representing a column vector with components $( x , y , z )$ , and X a column vector with components $( X , Y , Z )$

The end result of the transformation is

$$
\begin{array} { r l } & { X = \big ( \cos \Omega \cos \omega - \cos \iota \sin \Omega \sin \omega \big ) x } \\ & { \mathrm { ~ \ ~ \ } - \big ( \cos \Omega \sin \omega + \cos \iota \sin \Omega \cos \omega \big ) y } \\ & { \mathrm { ~ \ ~ \ } + \big ( \sin \iota \sin \Omega \big ) z , } \\ & { Y = \big ( \sin \Omega \cos \omega + \cos \iota \cos \Omega \sin \omega \big ) x } \\ & { \mathrm { ~ \ ~ \ } - \big ( \sin \Omega \sin \omega - \cos \iota \cos \Omega \cos \omega \big ) y } \\ & { \mathrm { ~ \ ~ \ } - \big ( \sin \iota \cos \Omega \big ) z , } \\ & { Z = \big ( \sin \iota \sin \omega \big ) x + \big ( \sin \iota \cos \omega \big ) y + \big ( \cos \iota \big ) z . } \end{array}
$$

The components of $r$ displayed in Eqs. (3.40) follow from these results by inserting $x = r$ cos $f$ , $y = r$ sin $f$ , and $z = 0$ .

From the coordinate transformation we can easily obtain the old basis vectors in terms of the new:

$$
\begin{array} { l } { { e _ { x } = \displaystyle { \frac { \partial { x } } { \partial x } = \big ( \cos { \Omega } \cos { \omega } - \cos { \iota } \sin { \Omega } \sin { \omega } \big ) e _ { X } } } } \\ { { \qquad + \big ( \sin { \Omega } \cos { \omega } + \cos { \iota } \cos { \Omega } \sin { \omega } \big ) e _ { Y } } } \\ { { \qquad + \big ( \sin { \iota } \sin { \omega } \big ) e _ { Z } , } } \\ { { e _ { y } = \displaystyle { \frac { \partial { x } } { \partial y } = - \big ( \cos { \Omega } \sin { \omega } + \cos { \iota } \sin { \Omega } \cos { \omega } \big ) e _ { X } } } } \\ { { \qquad - \big ( \sin { \Omega } \sin { \omega } - \cos { \iota } \cos { \Omega } \cos { \omega } \big ) e _ { Y } } } \\ { { \qquad + \big ( \sin { \iota } \cos { \omega } \big ) e _ { Z } , } } \\ { { e _ { z } = \displaystyle { \frac { \partial { x } } { \partial z } = \big ( \sin { \iota } \sin { \Omega } \big ) e _ { X } - \big ( \sin { \iota } \cos { \Omega } \big ) e _ { Y } + \big ( \cos { \iota } \big ) e _ { Z } } . } } \end{array}
$$

in which the position vector $_ { x }$ is expressed as ${ \pmb x } = X { \pmb e } _ { X } + Y { \pmb e } _ { Y } + Z { \pmb e } _ { Z }$

The orbital vectors of Eqs. (3.42) and (3.43) are obtained by inserting these results within the relations $\pmb { n } = \cos f \pmb { e } _ { x } + \sin f \pmb { e } _ { y }$ and $\lambda = - \sin f e _ { x } + \cos f e _ { y } ,$ which are inherited from Eqs. (3.7); the new relations reflect the change of convention regarding the choice of $x$ -direction.

# 3.3 Perturbed Kepler problem

We saw in the preceding section that the motion of two spherical bodies under their mutual gravitational attraction can be solved exactly and completely. As we shall see in Sec. 3.5, the same cannot be said of the three-body problem, and in general, the $N$ -body problem does not admit an exact solution. Many situations of interest, however, involve more than two bodies. The Sun–Earth–Moon system is an extremely pertinent example, and the motion of any planet around the Sun is affected by the massive presence of Jupiter. While these systems cannot be given an exact description, we can nevertheless make progress by appealing to the fact that in many applications, the additional bodies have only a small effect on the orbital motion of a two-body system. In the Sun–Earth–Moon system, the dominant interaction is between the Sun and the Earth, and the gravitational effects of the Moon on Earth’s orbital motion are small. Similarly, while Jupiter is indeed a massive body, it is sufficiently far from the other planets that its gravity has a small effect on them. The approximate analysis of small external influences on a system dominated by an internal interaction is the realm of perturbation theory, and in this section we formulate a perturbation theory for Kepler’s problem.

# 3.3.1 Perturbing force

We return to the two-body problem of Sec. 3.2, but now suppose that the relative acceleration $\pmb { a } : = \pmb { a } _ { 1 } - \pmb { a } _ { 2 }$ between bodies is given by

$$
\pmb { a } = - \frac { G m } { r ^ { 2 } } \pmb { n } + \pmb { f } ,
$$

in which $m : = m _ { 1 } + m _ { 2 }$ , $r : = r _ { 1 } - r _ { 2 }$ , $r : = | r |$ , ${ \pmb n } : = { \pmb r } / r$ , and where $f$ is a perturbing force per unit mass, which may depend on $r$ , $\pmb { v } : = \pmb { v } _ { 1 } - \pmb { v } _ { 2 }$ , and time. The presence of the perturbing force implies that the Keplerian motion reviewed in Sec. 3.2 is no a longer a solution to the equations of motion. As a consequence we can no longer expect $\pmb { h } : = \pmb { r } \times \pmb { v }$ to be a constant vector, the orbit to be elliptical, the pericenter to stay in a fixed position, and so on. But with $f$ assumed to be small, we would expect the Keplerian description to remain approximately true. Our main goal is to find a useful way of describing the small deviations from Keplerian motion produced by the perturbing force. Below we shall follow the convention from celestial mechanics, and refer to $f$ as a perturbing force, in spite of the fact that it is really a force per unit mass.

It is helpful to introduce, as we did previously, a vectorial basis adapted to the orbital motion of the two bodies. The first member of the basis will be $\pmb { n }$ , which is already singled out in Eq. (3.47). The third member will be $\pmb { e } _ { z } : = \pmb { h } / h$ , which is necessarily orthogonal to $\pmb { n }$ ; this vector can no longer be assumed to be a constant vector. The second member of the basis is then $\gimel$ , which is defined to be orthogonal to both $\pmb { n }$ and $\boldsymbol { e } _ { z }$ . We take the triad of vectors $( n , \lambda , e _ { z } )$ to form a right-handed basis. When $\pmb { f } = \pmb { 0 }$ the vector basis reduces to the one introduced back in Sec. 3.2, but the bases are quite distinct in the presence of a perturbing force; for reasons that will become clear later, we perversely adopt the same notation in spite of this important distinction.

The vectorial basis can be used to decompose any vector relevant to the description of the perturbed orbital motion. Examples are

$$
\begin{array} { l } { r = r { \pmb n } , } \\ { \pmb { \imath } = \dot { r } { \pmb n } + v _ { \perp } { \pmb \lambda } , } \\ { { \pmb h } = h { \pmb e } _ { z } , } \end{array}
$$

in which ${ \dot { r } } : = v \cdot n$ and $v _ { \perp } : = \pmb { v } \cdot \lambda$ ; it is easy to verify that $h = r v _ { \perp }$ . Another example is the perturbing force, which is decomposed as

$$
\pmb { f } = \mathcal { R } \pmb { n } + \mathcal { S } \pmb { \lambda } + \mathcal { W } \pmb { e } _ { z } ,
$$

in terms of components $\mathcal { R } , S$ , and $\mathcal { W }$ . Yet another example is the Runge–Lenz vector

$$
A : = \frac { \pmb { v } \times \pmb { h } } { G m } - \pmb { n } = A \pmb { e } _ { x } , \qquad e _ { x } = \cos \alpha \pmb { n } - \sin \alpha \pmb { \lambda } ,
$$

which is given a component $A \cos \alpha$ along $\pmb { n }$ , and a component $- A \sin \alpha$ along $\gimel$ ; there is no component along $\scriptstyle { e _ { z } }$ because $\pmb { A }$ is orthogonal to $\pmb { h }$ . Here we have defined the Runge–Lenz vector exactly as in Sec. 3.2, but we can no longer expect $\pmb { A }$ to be a constant vector. We have given the vector a length $A$ , and Eq. (3.50) serves as a definition for the unit vector $\boldsymbol { e } _ { x }$ , which is also not a constant vector. In an unperturbed situation $A$ would be equal to $e , \alpha$ would be equal to the true anomaly $f$ , and $\boldsymbol { e _ { x } }$ would indeed be a constant vector; but none of these statements can be expected to hold when $\ b { f } \neq \mathbf { 0 }$ .

The effect of the perturbing force $f$ on the vectors $\pmb { h }$ and $\pmb { A }$ can be calculated by appealing directly to their definitions. We find that

$$
\frac { d \pmb { h } } { d t } = \pmb { r } \times \pmb { f } = - r \mathcal { W } \pmb { \lambda } + r \mathcal { S } \pmb { e } _ { z }
$$

and

$$
G m \frac { d \boldsymbol { A } } { d t } = \boldsymbol { f } \times \boldsymbol { h } + \boldsymbol { v } \times ( \boldsymbol { r } \times \boldsymbol { f } ) = 2 h \mathcal { S } \boldsymbol { n } - \left( h \mathcal { R } + r \dot { r } \boldsymbol { \mathcal { S } } \right) \boldsymbol { \lambda } - r \dot { \boldsymbol { r } } \mathcal { W } \boldsymbol { e } _ { z } .
$$

These equations imply that

$$
{ \frac { d h } { d t } } = r S
$$

and

$$
G m \frac { d \cal { A } } { d t } = h \sin \alpha \mathcal { R } + \bigl ( 2 h \cos \alpha + r \dot { r } \sin \alpha \bigr ) \mathcal { S } ,
$$

as well as

$$
h \frac { d \pmb { e } _ { z } } { d t } = - r \mathcal { W } \pmb { \lambda }
$$

and

$$
G m A \frac { d e _ { x } } { d t } = - \big [ h \cos \alpha \mathcal { R } + ( - 2 h \sin \alpha + r \dot { r } \cos \alpha ) \mathcal { S } \big ] \big ( \sin \alpha n + \cos \alpha \lambda \big ) - r \dot { r } \mathcal { W } e _ { z } .
$$

These equations tell us, for example, that $s$ produces a change in the magnitude of the angular-momentum vector, while $\mathcal { W }$ produces a change in its direction. Similarly, both $\mathcal { R }$ and $s$ produce a change in $\pmb { A }$ ’s magnitude, as well as a change of direction orthogonal to $e _ { z }$ .

# 3.3.2 Osculating orbits

How are we to solve Eq. (3.47)? A direct approach, of course, is always possible: one inserts the given expression for the external force and integrates the second-order differential equations directly, either by analytical methods when the problem is sufficiently simple (a rare occasion), or by numerical methods. The approach provides an answer, but very little insight into the effects of the perturbation on various key aspects of the orbit. We shall favor instead a clever reformulation of the perturbed problem that was initially devised by Euler and Lagrange. This reformulation, known as the method of osculating orbital elements, is an application to orbital dynamics of the well-known method of variation of arbitrary constants to integrate differential equations (reviewed in Box 3.3).

# Box 3.3

# Variation of arbitrary constants

The method of variation of arbitrary constants to integrate differential equations is best introduced by examining a simple example. Consider a simple harmonic oscillator of unit frequency driven by an external force $f ( t )$ . The system is described by the differential equation

$$
{ \ddot { x } } + x = f ,
$$

which $x$ is the displacement from equilibrium, and an overdot indicates differentiation with respect to t . To tegrate this equation we begin with the general solution to the homogeneous problem, ${ \ddot { x } } + x = 0$ . This olution can be expressed as

$$
x ( t ) = x _ { 0 } \cos t + v _ { 0 } \sin t ,
$$

in which $x _ { 0 } : = x ( t = 0 )$ and $v _ { 0 } : = \dot { x } ( t = 0 )$ are the arbitrary constants of the solution. This solution also gives us

$$
{ \dot { x } } ( t ) = v _ { 0 } \cos t - x _ { 0 } \sin t .
$$

Returning to the original differential equation with a driving force $f ( t )$ , we declare that Eqs. (2) and (3) shall also be a solution to Eq. (1), and evade the obvious contradiction by allowing $x _ { 0 }$ and $v _ { 0 }$ to become functions of

time. Equation (3) will be compatible with Eq. (2) provided that ${ \dot { x } } _ { 0 } \cos t + { \dot { v } } _ { 0 }$ sin $t = 0$ , and substitution of Eqs. (2) and (3) within Eq. (1) yields $- \dot { x } _ { 0 }$ sin $t + \dot { v } _ { 0 }$ cos $t = f$ . Solving for $\dot { x } _ { 0 }$ and $\dot { v } _ { 0 } ,$ we find that

$$
\dot { x } _ { 0 } = - f \sin t , \qquad \dot { v } _ { 0 } = f \cos t ,
$$

and these equations now replace Eq. (1). The solutions are to be inserted within Eqs. (2) and (3) for a complete solution of the original problem.

These steps define the method of variation of arbitrary constants. One begins with the general solution to a homogeneous differential equation, with the appropriate number of arbitrary constants. One next solves the inhomogeneous problem by formally adopting the functional form of the homogeneous solution, and promoting the arbitrary constants to new variables. After some manipulations, the original problem acquires a new formulation as a set of first-order differential equations for the new variables.

# The method

The starting point of the method of osculating orbital elements is to recall that the general solution to the unperturbed Kepler problem can be expressed as

$$
r ( t ) = r _ { \mathrm { K e p l e r } } ( t , \mu ^ { a } ) , \qquad v ( t ) = v _ { \mathrm { K e p l e r } } ( t , \mu ^ { a } ) ,
$$

where $r _ { \mathrm { K e p l e r } }$ and $\pmb { v } _ { \mathrm { K e p l e r } }$ are the functional forms displayed in Eqs. (3.40) and (3.41), with $\mu ^ { a }$ denoting a collection of six constants of the motion, which we take to be the orbital elements $( p , e , \iota , \Omega , \omega , T )$ . These vectors satisfy the differential equations

$$
\frac { d r _ { \mathrm { K e p l e r } } } { d t } = { \pmb v } _ { \mathrm { K e p l e r } } , \qquad \frac { d { \pmb v } _ { \mathrm { K e p l e r } } } { d t } = - G m \frac { r _ { \mathrm { K e p l e r } } } { r _ { \mathrm { K e p l e r } } ^ { 3 } } ,
$$

which define the unperturbed Kepler problem.

The vectors $r _ { \mathrm { K e p l e r } }$ and $\pmb { v } _ { \mathrm { K e p l e r } }$ can also provide a solution to the perturbed problem if we let the orbital elements $\mu ^ { a }$ become functions of time: $\mu ^ { a } \to \mu ^ { a } ( t )$ . The original mathematical problem expressed by Eq. (3.47) can then be formulated as a set of first-order differential equations for $\mu ^ { a }$ , and the solutions to these are to be inserted within Eqs. (3.57) to obtain a complete solution to the perturbed problem. The meaning of the method is that at any time $t _ { 1 }$ , the orbit is taken to be a Keplerian orbit with orbital elements $\mu ^ { a } ( t _ { 1 } )$ that refer to this time only; at another time $t _ { 2 }$ the orbit will still be Keplerian, but the orbital elements will have evolved to new values $\mu ^ { a } ( t _ { 2 } )$ . Another way of describing this is to say that at any time $t _ { 1 }$ , there exists a Keplerian orbit with elements $\mu ^ { a } ( t _ { 1 } )$ that is tangent to the perturbed orbit at that time; this is the osculating orbit, the term originating in the Latin word osculatio, which means “to kiss.”

We shall therefore express the solution to Eq. (3.47) as

$$
r ( t ) = r _ { \mathrm { K e p l e r } } \bigl ( t , \mu ^ { a } ( t ) \bigr ) , \qquad v ( t ) = v _ { \mathrm { K e p l e r } } \bigl ( t , \mu ^ { a } ( t ) \bigr ) ,
$$

with $r _ { \mathrm { K e p l e r } }$ and $\pmb { v } _ { \mathrm { K e p l e r } }$ still standing for the functional forms of Eqs. (3.40) and (3.41), but with the orbital elements $\mu ^ { a }$ now allowed to be functions of time. Differentiating $r$ with

respect to time gives

$$
\frac { d \pmb { r } } { d t } = \frac { \partial \pmb { r } _ { \mathrm { \tiny { K e p l e r } } } } { \partial t } + \sum _ { a } \frac { \partial \pmb { r } _ { \mathrm { \tiny { K e p l e r } } } } { \partial \mu ^ { a } } \frac { d \mu ^ { a } } { d t } .
$$

The left-hand side is $\pmb { v }$ , and the first term on the right-hand side is $\pmb { v } _ { \mathrm { K e p l e r } }$ , because $r _ { \mathrm { K e p l e r } }$ is differentiated with respect to $t$ while keeping the orbital elements constant, thereby defining Keplerian motion. The equation is compatible with Eq. (3.59) provided that

$$
\sum _ { a } \frac { \partial r _ { \mathrm { K e p l e r } } } { \partial \mu ^ { a } } \frac { d \mu ^ { a } } { d t } = 0 ,
$$

and we have obtained our first osculating condition. Similarly, differentiating $\pmb { v }$ with respect to $t$ gives

$$
\frac { d \pmb { v } } { d t } = \frac { \partial \pmb { v } _ { \mathrm { K e p l e r } } } { \partial t } + \sum _ { a } \frac { \partial \pmb { v } _ { \mathrm { K e p l e r } } } { \partial \mu ^ { a } } \frac { d \mu ^ { a } } { d t } .
$$

The left-hand side is $\pmb { a } = \pmb { a } _ { \mathrm { K e p l e r } } + \pmb { f }$ , and the first term on the right-hand side is the Keplerian acceleration $\pmb { a } _ { \mathrm { K e p l e r } }$ . The second osculating condition is

$$
\sum _ { a } \frac { \partial { \pmb v } _ { \mathrm { K e p l e r } } } { \partial \mu ^ { a } } \frac { d \mu ^ { a } } { d t } = { \pmb f } ,
$$

and these equations can be solved for $d \mu ^ { a } / d t$ .

# Osculating equations

The purpose of the foregoing discussion was primarily to describe the conceptual aspects of the method of osculating orbital elements. While Eqs. (3.61) and (3.63) could in principle be solved for $d \mu ^ { a } / d t$ in terms of the perturbing force, it is easier in practice to obtain $d \mu ^ { a } / d t$ directly from the definitions of the orbital elements displayed in Eqs. (3.46). The orbital elements are given explicitly in terms of the fixed vectorial basis $( e _ { X } , e _ { Y } , e _ { Z } )$ , as well as the angular-momentum vector $\pmb { h }$ and the Runge–Lenz vector $\pmb { A }$ , which change according to Eqs. (3.51)–(3.56). The method authorizes us to substitute Keplerian relations on the right-hand side of these equations, so that $h$ is at all times equal to ${ \sqrt { G m p ( t ) } } , A$ is at all times equal to $e ( t )$ , $\alpha$ is at all times equal to the true anomaly $f , r$ is at all times equal to $p / ( 1 + e \cos f )$ , and $\dot { r }$ is at all times equal to $( G m / p ) ^ { 1 / 2 } e \sin f$ .

By following this approach we quickly arrive at

$$
\begin{array} { r l } & { \frac { d p } { d t } = 2 \sqrt { \frac { p ^ { 3 } } { G m } } \frac { 1 } { 1 + e \cos f } S , } \\ & { \frac { d e } { d t } = \sqrt { \frac { p } { G m } } \bigg [ \sin f \mathcal { R } + \frac { 2 \cos f + e ( 1 + \cos ^ { 2 } f ) } { 1 + e \cos f } S \bigg ] , } \\ & { \frac { d } { d t } = \sqrt { \frac { p } { G m } } \frac { \cos ( \omega + f ) } { 1 + e \cos f } \mathcal { W } , } \\ & { \sin \iota \frac { d \Omega } { d t } = \sqrt { \frac { p } { G m } } \frac { \sin ( \omega + f ) } { 1 + e \cos f } \mathcal { W } , } \end{array}
$$

(continued overleaf)

$$
\frac { d \omega } { d t } = \frac { 1 } { e } \sqrt { \frac { p } { G m } } \bigg [ - \cos f \mathcal { R } + \frac { 2 + e \cos f } { 1 + e \cos f } \sin f \mathcal { S } - e \cot t \frac { \sin ( \omega + f ) } { 1 + e \cos f } \mathcal { W } \bigg ] ,
$$

a listing of equations that govern the behavior of the osculating orbital elements. To these we can add

$$
\frac { d a } { d t } = 2 \sqrt { \frac { a ^ { 3 } } { G m } } ( 1 - e ^ { 2 } ) ^ { - 1 / 2 } \Big [ e \sin f \mathcal { R } + ( 1 + e \cos f ) \mathcal { S } \Big ] ,
$$

in case $a : = p / ( 1 - e ^ { 2 } )$ is preferred over $p$ in the selection of orbital elements. Note that $p$ and $e$ (or $a$ and $e$ ) are affected only by components of $f$ in the orbital plane, while $\Omega$ and $\iota$ are affected only by the component out of the plane. All components of the perturbing force affect $\omega$ .

We are missing an equation for the variation of $T$ , the time of pericenter passage, which determines the true anomaly $f$ via Eq. (3.29). It is more practical, however, to close the system of equations by providing an expression for $d f / d t$ , from which the true anomaly can be obtained directly. Because $f$ is the angle between the (varying) pericenter and the position vector $r$ , we have that cos $f = r \cdot e _ { x } / r$ , and this can immediately be differentiated with respect to time. In this we insert Eq. (3.56) for $d e _ { x } / d t$ , the usual Keplerian relations for $d r / d t$ , and we obtain

$$
\frac { d f } { d t } = \sqrt { \frac { G m } { p ^ { 3 } } } ( 1 + e \cos f ) ^ { 2 } + \frac { 1 } { e } \sqrt { \frac { p } { G m } } \bigg [ \cos f \mathcal { R } - \frac { 2 + e \cos f } { 1 + e \cos f } \sin f \mathcal { S } \bigg ]
$$

after some simplification. The result can also be expressed as

$$
\frac { d f } { d t } = \left( \frac { d f } { d t } \right) _ { \mathrm { K e p l e r } } - \Bigg ( \frac { d \omega } { d t } + \cos \iota \frac { d \Omega } { d t } \Bigg ) ,
$$

which shows that $d f / d t$ differs from the usual Keplerian expression by a term $d \omega / d t +$ $\cos \iota d \Omega / d t$ which possesses a direct geometrical meaning. We recall that $\omega$ is the angle from the (varying) pericenter to the (varying) line of nodes, as measured in the orbital plane, while $\Omega$ is the angle from the line of nodes to the (fixed) $X \cdot$ -direction, as measured in the reference $X { - } Y$ plane. The combination $d \omega + \cos \iota d \Omega$ can then be seen to describe the change in the direction to the pericenter relative to the $X$ -direction, as measured entirely in the orbital plane. The non-Keplerian terms in Eqs. (3.66) and (3.67) therefore appear because the true anomaly $f$ is measured relative to a varying set of directions.

The relevance of the combination $d \omega + \cos \iota d \Omega$ can also be inferred from Eq. (3.56), which gives the rate of change of the direction to the pericenter. After inserting the appropriate Keplerian relations in this expression, we find that

$$
\frac { d e _ { x } } { d t } = \Bigg ( \frac { d \omega } { d t } + \cos \iota \frac { d \Omega } { d t } \Bigg ) \big ( \sin f n + \cos f \lambda \big ) + \Bigg ( \sin \omega \frac { d \iota } { d t } - \sin \iota \cos \Omega \frac { d \Omega } { d t } \Bigg ) e _ { z } ,
$$

which reveals that $d \omega + \cos \iota d \Omega$ does indeed describe the change of $\boldsymbol { e } _ { x }$ within the orbital plane, while $\sin \omega d \iota - \sin \iota \cos { \Omega } d \Omega$ describes the change in the orthogonal direction.

# First-order approximation

The formalism of osculating orbital elements, in the formulation of Eqs. (3.64) and (3.66), is exactly equivalent to the original formulation of the equations of motion in Eq. (3.47); no approximations have been introduced in the transcription. The usefulness of the formalism, however, is most immediate when the perturbing force is small, so that the changes in the orbital elements are small. In such a context one can achieve a very good approximation of the orbital dynamics by inserting the constant, zeroth-order values on the right-hand side of the equations, and integrating with respect to $t$ to get the first-order changes. In such applications it can be convenient to use $f$ as independent variable instead of $t$ , and in this approximate context one can neglect the non-Keplerian terms on the right-hand side of Eq. (3.66). The system of osculating equations becomes

$$
\begin{array} { r l } & { \frac { d p } { d f } \simeq 2 \frac { p ^ { 3 } } { G m } \frac { 1 } { ( 1 + e \odot s f ) ^ { \frac { 3 } { 2 } } } s , } \\ & { \frac { d e } { d f } \simeq \frac { p ^ { 2 } } { G m } \bigg [ \frac { \sin f } { ( 1 + e \odot s f ) ^ { 2 } } \mathcal { R } + \frac { 2 \cos f + e ( 1 + \cos ^ { 2 } f ) } { ( 1 + e \odot s f ) ^ { \frac { 3 } { 2 } } } s \bigg ] , } \\ & { \frac { d i } { d f } \simeq \frac { p ^ { 2 } } { G m } \frac { \cos ( \omega + f ) } { ( 1 + e \odot s f ) ^ { 3 } } w , } \\ & { \sin \frac { d \Omega } { d f } \simeq \frac { p ^ { 2 } } { G m } \frac { \sin ( \omega + f ) } { ( 1 + e \odot s f ) ^ { 3 } } w , } \\ & { \frac { d \omega } { d f } \simeq \frac { 1 } { e \bar { G } m } \bigg [ - \frac { \cos f } { ( 1 + e \odot s f ) ^ { \frac { 3 } { 2 } } } \mathcal { R } + \frac { 2 + e \odot s f } { ( 1 + e \odot s f ) ^ { 3 } } \sin f s } \\ & { \qquad - \cot ( \frac { \sin ( \omega + f ) } { ( 1 + e \odot s f ) ^ { 3 } } ) w \bigg ] , } \end{array}
$$

with

$$
\begin{array} { r l r } {  { \frac { d t } { d f } \simeq \sqrt { \frac { p ^ { 3 } } { G m } } \frac { 1 } { ( 1 + e \cos f ) ^ { 2 } } } } \\ & { } & { \times \{ 1 - \frac { 1 } { e } \frac { p ^ { 2 } } { G m } \bigg [ \frac { \cos f } { ( 1 + e \cos f ) ^ { 2 } } \mathcal { R } - \frac { 2 + e \cos f } { ( 1 + e \cos f ) ^ { 3 } } \sin f \mathcal { S } \bigg ] \} } \end{array}
$$

providing the temporal information.

In most applications of the formalism it is found that the orbital elements undergo two types of changes. The first is an oscillation with a period equal to the orbital period $P$ (or multiples of $P$ ), as given by Eq. (3.36); such changes are typically uninteresting. The second type is a steady drift that does not average out after a few orbital cycles; such changes, which are known as secular changes, are typically much more interesting, because they accumulate over time and eventually lead to large departures from the initial Keplerian orbit. The secular change of an orbital element $\mu ^ { a }$ over a complete orbit is given by

$$
\Delta \mu ^ { a } = \int _ { 0 } ^ { P } { \frac { d \mu ^ { a } } { d t } } d t = \int _ { 0 } ^ { 2 \pi } { \frac { d \mu ^ { a } } { d f } } d f ,
$$

and division by the orbital period $P$ gives a notion of average, or secular, time derivative:

$$
\left( \frac { d \mu ^ { a } } { d t } \right) _ { \mathrm { s e c } } : = \frac { \Delta \mu ^ { a } } { P } .
$$

The integrations are best carried out in the form involving the true anomaly $f$ , but the factors of $1 + e \cos f$ in the denominator can sometimes produce integrals that are difficult to evaluate. When such a situation is encountered, it is usually advantageous to make a change of variables from $f$ to the eccentric anomaly $u$ , as defined by Eqs. (3.30)–(3.33).

# 3.4 Case studies of perturbed Keplerian motion

Our purpose in this section is to explore some of the non-Keplerian aspects of celestial mechanics by working through a number of examples that are of real relevance to the solar system. We shall investigate these effects by exploiting the method of osculating orbital elements introduced in the preceding section.

# 3.4.1 Perturbations by a third body

We first examine a two-body system, such as the Sun–Mercury system, perturbed by a remote third body such as Jupiter. This is an example of a three-body problem, and we shall have occasion in Sec. 3.5 to give this problem a more complete treatment. Here we provide an approximate discussion, relying on the fact that the third body is remote, so that its gravitational influence on the two-body system is weak. This influence can be described as a perturbation, and its effects can be investigated by means of the method of osculating orbits.

To set up the problem we recall that the two-body system involves a mass $m _ { 1 }$ at position $r _ { 1 }$ and a mass $m _ { 2 }$ at position $r _ { 2 }$ . The third body has a mass $m _ { 3 }$ and a position $r _ { 3 }$ . As usual we let $m : = m _ { 1 } + m _ { 2 }$ , $r : = r _ { 1 } - r _ { 2 }$ , and we also introduce $\pmb { R } : = \pmb { r } _ { 3 } - \pmb { r } _ { 2 }$ ; note that $\pmb { R }$ no longer stands for the position of the two-body pericenter. We also have $r : = | \boldsymbol { r } | , R : = | \boldsymbol { R } |$ , ${ \pmb n } : = { \pmb r } / r$ , and $N : = R / R$ . We assume that $R \gg r$ .

From Eq. (1.202) we find that the acceleration of the first body is given by

$$
{ \pmb a } _ { 1 } = - G m _ { 2 } \frac { \pmb n } { r ^ { 2 } } - G m _ { 3 } \frac { { \pmb r } - { \pmb R } } { | { \pmb r } - { \pmb R } | ^ { 3 } } ,
$$

while

$$
{ \pmb a } _ { 2 } = G m _ { 1 } \frac { \pmb n } { r ^ { 2 } } + G m _ { 3 } \frac { \pmb N } { R ^ { 2 } }
$$

is the acceleration of the second body. The relative acceleration is $\pmb { a } : = \pmb { a } _ { 1 } - \pmb { a } _ { 2 }$ , and removal of the Keplerian term gives us the perturbing force

$$
f = - G m _ { 3 } \biggl ( \frac { r - R } { | r - R | ^ { 3 } } + \frac { N } { R ^ { 2 } } \biggr ) .
$$

Taking into account the assumption that $R$ is large compared with $r$ , we simplify this expression by expanding in powers of $r / R$ , and obtain, to leading order,

$$
{ \pmb f } = - \frac { G m _ { 3 } r } { R ^ { 3 } } \Big [ { \pmb n } - 3 ( { \pmb n } \cdot { \pmb N } ) { \pmb N } + O ( r / R ) \Big ] .
$$

We see that the ratio of $f$ to the Keplerian acceleration is of order $( m _ { 3 } / m ) ( r / R ) ^ { 3 }$ , and therefore small by virtue of our assumption that $R \gg r$ . The components of the perturbing force in the Keplerian basis $( n , \lambda , e _ { z } )$ are

$$
\begin{array} { c } { { \mathcal { R } : = f \cdot n = - \displaystyle \frac { G m _ { 3 } r } { R ^ { 3 } } \big [ 1 - 3 ( n \cdot N ) ^ { 2 } \big ] , } } \\ { { \big [ - 2 p t \big ] S : = f \cdot \lambda = 3 \displaystyle \frac { G m _ { 3 } r } { R ^ { 3 } } ( n \cdot N ) ( \lambda \cdot N ) , } } \\ { { \mathcal { W } : = f \cdot e _ { z } = 3 \displaystyle \frac { G m _ { 3 } r } { R ^ { 3 } } ( n \cdot N ) ( e _ { z } \cdot N ) , } } \end{array}
$$

and these can immediately be inserted within the equations that govern the evolution of the osculating orbital elements.

The expressions for $\mathcal { R } , { \mathcal { S } }$ , and $\mathcal { W }$ refer to any two-body system perturbed by a remote third body, but to proceed we consider the specific situation mentioned previously: We examine the orbit of a planet like Mercury around the Sun, perturbed by an outer planet such as Jupiter. For simplicity we assume that Mercury and Jupiter move in the same orbital plane (when in reality they have a relative inclination of approximately 6 degrees), and we align the reference $X { - } Y$ plane with this common orbital plane; this implies that $\iota = 0$ , and since $\Omega$ is not defined, it may be set equal to zero. Again for simplicity, we assume that Jupiter moves on a circular orbit (a good approximation), with a constant radius $R$ and angular frequency $\Omega _ { 3 } = \sqrt { G ( m _ { 2 } + m _ { 3 } ) / R ^ { 3 } }$ . Its true anomaly is given by $F = \Omega _ { 3 } t$ , and it changes very little in the course of a complete Mercury orbit; we have that

$$
\Delta F : = \Omega _ { 3 } P = 2 \pi \bigg ( \frac { m _ { 2 } + m _ { 3 } } { m _ { 1 } + m _ { 2 } } \bigg ) ^ { 1 / 2 } \bigg ( \frac { a } { R } \bigg ) ^ { 3 / 2 } \ll 1 ,
$$

with $P$ denoting Mercury’s orbital period, and $a : = p / ( 1 - e ^ { 2 } )$ its semi-major axis. The direction to Jupiter is

$$
N = \cos F e _ { X } + \sin F e _ { Y } ,
$$

and Eqs. (3.42), (3.43), and (3.45) reveal that

$$
\begin{array} { l } { { \pmb { n } = \cos ( f + \omega ) { \pmb { e } } _ { X } + \sin ( f + \omega ) { \pmb { e } } _ { Y } , } } \\ { { \pmb { \lambda } = - \sin ( f + \omega ) { \pmb { e } } _ { X } + \cos ( f + \omega ) { \pmb { e } } _ { Y } , } } \end{array}
$$

and $e _ { z } = e _ { Z }$ . From these expressions we find that $\pmb { n } \cdot \pmb { N } = \cos ( f + \omega - F )$ , $\lambda \cdot N =$ $- \sin ( f + \omega - F )$ , $\boldsymbol { e } _ { z } \cdot \boldsymbol { N } = 0$ , and the components of the perturbing force become

$$
\begin{array} { r l } & { \mathcal { R } = - \displaystyle \frac { G m _ { 3 } r } { R ^ { 3 } } \big [ 1 - 3 \cos ^ { 2 } ( f + \omega - F ) \big ] , } \\ & { \mathcal { S } = \displaystyle - 3 \frac { G m _ { 3 } r } { R ^ { 3 } } \sin ( f + \omega - F ) \cos ( f + \omega - F ) , } \\ & { \mathcal { W } = 0 , } \end{array}
$$

in which we may substitute $r = p / ( 1 + e \cos f )$ .

Mercury’s orbital evolution in response to Jupiter’s perturbation is governed by Eqs. (3.64). As we explained near the end of Sec. 3.3.2, we are primarily interested in the secular variation of the orbital elements $p , e$ , and $\omega$ , as calculated according to Eq. (3.71) using the equations listed in Eq. (3.69). The integrals over $f$ are easily evaluated by adopting the eccentric anomaly $u$ as an integration variable, and by assuming that $F$ is constant over Mercury’s orbital cycle – refer to Eq. (3.78). After some manipulations we arrive at

$$
\begin{array} { l } { \Delta p : = - 1 5 \pi \displaystyle \frac { m _ { 3 } p ^ { 4 } } { m R ^ { 3 } } e ^ { 2 } ( 1 - e ^ { 2 } ) ^ { - 7 / 2 } \sin 2 ( \omega - F ) , } \\ { \Delta e : = \displaystyle \frac { 1 5 \pi } { 2 } \displaystyle \frac { m _ { 3 } p ^ { 3 } } { m R ^ { 3 } } e ( 1 - e ^ { 2 } ) ^ { - 5 / 2 } \sin 2 ( \omega - F ) , } \\ { \Delta \omega : = \displaystyle \frac { 3 \pi } { 2 } \displaystyle \frac { m _ { 3 } p ^ { 3 } } { m R ^ { 3 } } ( 1 - e ^ { 2 } ) ^ { - 5 / 2 } \big [ 1 + 5 \cos 2 ( \omega - F ) \big ] } \end{array}
$$

for the net change in the orbital elements after a complete Mercury orbit. From these results it can be inferred that $\Delta a = 0$ : Mercury does not undergo a secular variation of its semi-major axis, and the change in $p = a ( 1 - e ^ { 2 } )$ simply reflects a change in eccentricity.

These expressions reveal that depending on Jupiter’s position on its orbit, Mercury’s eccentricity $e$ and longitude of perihelion $\omega$ either increase or decrease in the course of a complete orbit. After an extremely long time, much longer than Jupiter’s own orbital period, the change in $e$ will average out, but Mercury’s perihelion will advance at an average rate of

$$
\langle \Delta \omega \rangle = \frac { 3 \pi } { 2 } \frac { m _ { 3 } } { m } \biggl ( \frac { p } { R } \biggr ) ^ { 3 } ( 1 - e ^ { 2 } ) ^ { - 5 / 2 } = \frac { 3 \pi } { 2 } \frac { m _ { 3 } } { m } \biggl ( \frac { a } { R } \biggr ) ^ { 3 } ( 1 - e ^ { 2 } ) ^ { 1 / 2 }
$$

per orbit.

Inserting the numerical values for Mercury and Jupiter from Table 3.2, we find that $\langle \Delta \omega \rangle = 1 . 7 9 \times 1 0 ^ { - 6 }$ radians per orbit; the smallness of this effect provides ample justification for a calculation limited to first-order perturbation theory. It is customary to express the perihelion advance as a rate in units of arcseconds (as) per century. To achieve this conversion we use the fact that $1 { \mathrm { ~ r a d } } = 2 . 0 6 3 \times 1 0 ^ { 5 }$ as, and take into account the fact that Mercury’s orbital period is $P = 0 . 2 4 0 8$ yr; we obtain $\langle ( d \omega / d t ) _ { \mathrm { s e c } } \rangle = 1 5 4$ as/century. This is very close to the accurately computed value of 153.6 as/century displayed in Table 3.1. The accuracy, however, would not be as good if we applied Eq. (3.83) to the perturbation produced by Earth’s gravitational attraction; here we would get 69.2 as/century, quite a difference from the accurate value of 90 as/century. The reason for this lack of success is that $r / R \simeq 0 . 3 8$ for the Earth, so that an accurate computation of the perihelion advance requires higher-order terms in the expansion of the perturbing force in powers of $r / R$ . In addition, the approximation formulated in Eq. (3.78) is not so good in the case of the Earth, because Earth’s period is only four times longer than Mercury’s (instead of forty times longer for Jupiter). Nevertheless, the method of osculating orbital elements would allow us to incorporate such details systematically in a straightforward manner, leading to the accurately calculated planetary perturbations listed in Table 3.1.

As we have seen in Sec. 3.1, the sum total of the contributions from all the planets to Mercury’s perihelion advance does not account for the observed effect. The discrepancy, the famous 43 as/century, is accounted for by relativistic corrections to the equations of motion, which can be incorporated as additional contributions to the perturbing force. We will return to this question in Chapter 10.

<table><tr><td colspan="5">Table 3.2 Orbital elements of selected planets.The astronomical unit (AU) is the Earth-Sun distance,equal to 149.60 × 10 km.The inclination is measured indegrees,minutes of arc,and seconds ofarc.The inverse mass ismeasured inunits of the inverse solar mass,with M= = 1.9889× 1030 kg.</td></tr><tr><td>Semi-major axis Planet (AU)</td><td>Orbital period (yr)</td><td>Eccentricity</td><td>Inclination to ecliptic 。.&#x27;.&quot;</td><td>Inverse mass 1/M = 1</td></tr><tr><td>Mercury</td><td>0.387099</td><td>0.24085</td><td>0.205628</td><td>7.0.15 6010000</td></tr><tr><td>Venus</td><td>0.723332</td><td>0.61521</td><td>0.006787</td><td>3.23.40 408400</td></tr><tr><td>Earth</td><td>1.000000</td><td>1.00004</td><td>0.016722 0.0.0</td><td>328910</td></tr><tr><td>Mars</td><td>1.523691</td><td>1.88089</td><td>0.093377 1.51.0</td><td>3098500</td></tr><tr><td> Jupiter</td><td>5.202803</td><td>11.86223</td><td>0.04845</td><td>1.18.17 1047.39</td></tr><tr><td> Saturn</td><td>9.53884</td><td>29.4577</td><td>0.05565</td><td>2.29.22 3498.5</td></tr></table>

# 3.4.2 The Kozai mechanism

In 1962, the Soviet dynamicist Michael Lidov and the Japanese astronomer Yoshihide Kozai independently discovered a remarkable phenomenon that occurs when an object orbits a massive body under the perturbing influence of a distant body, when the two orbits are inclined relative to each other. As a result of the perturbed dynamics, there is a periodic exchange between the orbital eccentricity and inclination, such that when one increases, the other decreases. This effect, known as the Kozai mechanism, has important implications for the behavior of asteroids, satellites of planets, extrasolar planets, and multiple-star systems.

To study this effect we re-examine the situation of the previous section, but now allow the orbiting body $\left( m _ { 1 } \right)$ to have an inclination $\iota$ relative to the orbit of the perturbing body $\left( m _ { 3 } \right)$ , which is placed in the reference $X { - } Y$ plane. For simplicity we take the perturbing body to move on a circular orbit, and we choose the line of nodes of the inclined orbit to be situated at $\Omega = 0$ . The components of the perturbing force are still given by Eqs. (3.77), but the orbital basis vectors are now

$$
\begin{array} { r l } & { \boldsymbol { n } = \cos ( \omega + f ) \boldsymbol { e } _ { X } + \cos \iota \sin ( \omega + f ) \boldsymbol { e } _ { Y } + \sin \iota \sin ( \omega + f ) \boldsymbol { e } _ { Z } , } \\ & { \lambda = - \sin ( \omega + f ) \boldsymbol { e } _ { X } + \cos \iota \cos ( \omega + f ) \boldsymbol { e } _ { Y } + \sin \iota \cos ( \omega + f ) \boldsymbol { e } _ { Z } , } \\ & { { \boldsymbol { e } } _ { z } = - \sin \iota \boldsymbol { e } _ { Y } + \cos \iota \boldsymbol { e } _ { Z } ; } \end{array}
$$

the direction to the perturbed body is still given by Eq. (3.79). We calculate the secular variation of the orbital elements $a , e , \omega$ , and $\iota$ by inserting these expressions withinEqs. (3.69),

integrating over a complete orbital cycle, and averaging over the position of the perturbing body. The final results are

$$
\begin{array} { l } { \displaystyle \langle \Delta a \rangle = 0 , } \\ { \displaystyle \langle \Delta e \rangle = \frac { 1 5 \pi } { 2 } \frac { m _ { 3 } } { m } \bigg ( \frac { a } { R } \bigg ) ^ { 3 } e ( 1 - e ^ { 2 } ) ^ { 1 / 2 } \sin ^ { 2 } \iota \sin \omega \cos \omega , } \\ { \displaystyle \langle \Delta \omega \rangle = \frac { 3 \pi } { 2 } \frac { m _ { 3 } } { m } \bigg ( \frac { a } { R } \bigg ) ^ { 3 } ( 1 - e ^ { 2 } ) ^ { - 1 / 2 } \Big [ 5 \cos ^ { 2 } \iota \sin ^ { 2 } \omega + ( 1 - e ^ { 2 } ) ( 5 \cos ^ { 2 } \omega - 3 ) \Big ] , } \\ { \displaystyle \langle \Delta u \rangle = - \frac { 1 5 \pi } { 2 } \frac { m _ { 3 } } { m } \bigg ( \frac { a } { R } \bigg ) ^ { 3 } e ^ { 2 } ( 1 - e ^ { 2 } ) ^ { - 1 / 2 } \sin \iota \cos \iota \sin \omega \cos \omega . } \end{array}
$$

From Eqs. (3.85b) and (3.85d) we notice that $e ( 1 - e ^ { 2 } ) ^ { - 1 } \langle \Delta e \rangle + \tan \iota \langle \Delta \iota \rangle = 0 \nonumber$ , which leads to the remarkable conservation law,

$$
{ \sqrt { 1 - e ^ { 2 } } } \cos \iota = \operatorname { c o n s t a n t } ( \operatorname { o v e r } \log \operatorname { t i m e } \operatorname { s c a l e s } ) .
$$

This is actually the consequence of angular-momentum conservation. The component of the total angular-momentum vector normal to the orbital plane of the perturbing body is $L _ { Z } = L _ { Z } ^ { 1 + 2 } + L _ { Z } ^ { 3 }$ , and if we assume that $L _ { Z } ^ { 3 }$ is separately conserved (thereby ignoring the gravitational effects of √ $m _ { 1 }$ and $m _ { 2 }$ on the perturbing body), we find that $L _ { Z } ^ { 1 + 2 } = \mu \pmb { h } \cdot \pmb { e } _ { Z } =$ $\mu { \sqrt { G m p } } \cos \iota$ must be conserved. Because $a : = p / ( 1 - e ^ { 2 } )$ does not vary over long time scales, conservation of angular momentum implies that $( 1 - e ^ { 2 } ) ^ { 1 / 2 } \cos \iota$ cannot vary, in agreement with our previous statement.

When the longitude of pericenter $\omega$ lies in the first or third quadrants, we see from Eqs. (3.85) that the eccentricity increases while the inclination decreases; when $\omega$ lies instead in the second or fourth quadrants, the eccentricity decreases while the inclination increases. The equations also reveal that as long as $\cos ^ { 2 } \iota / ( 1 - e ^ { 2 } ) > 3 / 5$ , $\omega$ increases monotonically, on the same time scale as the variations in $e$ and $\iota$ . For orbits with sufficiently low inclinations, therefore, there is a periodic exchange between eccentricity and inclination as the pericenter keeps on advancing.

For high-inclination orbits, such that $\cos ^ { 2 } \iota / ( 1 - e ^ { 2 } ) < 3 / 5$ , the orbital evolution is very different. In this case, $\omega$ approaches a critical angle $\omega _ { c }$ such that $\langle \Delta \omega \rangle = 0$ , and the motion of the pericenter ceases; the critical angle is determined by

$$
\cos ^ { 2 } \omega _ { c } = \frac { 3 ( 1 - e ^ { 2 } ) - 5 \cos ^ { 2 } \iota } { 5 ( 1 - e ^ { 2 } - \cos ^ { 2 } \iota ) } .
$$

Meanwhile, if $e$ is initially in an increasing phase and $\iota$ in a decreasing phase, the ratio $\cos ^ { 2 } \iota / ( 1 - e ^ { 2 } )$ will be driven toward the limiting value of $3 / 5$ , and $\omega$ will settle to a final value of $\begin{array} { r } { \omega _ { c } = \frac { \pi } { 2 } } \end{array}$ or $\begin{array} { r } { \omega _ { c } = \frac { 3 \pi } { 2 } } \end{array}$ . The final outcome is a stationary solution of the perturbation equations with $\langle \Delta e \rangle = \langle \Delta \iota \rangle = \langle \Delta \omega \rangle = 0$ , occurring at critical values $e _ { c } , \iota _ { c }$ , and $\omega _ { c }$ constrained by

$$
\omega _ { c } = \frac { \pi } { 2 } \mathrm { o r } \frac { 3 \pi } { 2 } , \qquad \frac { \cos ^ { 2 } \iota _ { c } } { 1 - e _ { c } ^ { 2 } } = \frac { 3 } { 5 } .
$$

This equilibrium is stable; it can be shown that a perturbation away from equilibrium leads to oscillations of $e , \iota ,$ , and $\omega$ about their critical values, with a period

$$
P _ { \mathrm { K o z a i } } = \frac { 2 } { 3 \sqrt { 1 5 } } \frac { m } { m _ { 3 } } \bigg ( \frac { R } { a } \bigg ) ^ { 3 } \frac { 1 } { e _ { c } \sin \iota _ { c } } P ,
$$

where $P$ is the period of the orbiting body. This stationary solution is called the Kozai resonance. You will be asked to verify these statements in Exercise 3.7.

The Kozai mechanism can have important consequences: as the orbital eccentricity increases, the orbiting body can pass sufficiently close to the inner regions of the system at pericenter to interact with other bodies there, or even be tidally captured or disrupted by the central body. Conversely, the body could find itself sufficiently far away at apocenter to interact with more distant objects and be ejected from the system. This mechanism accounts for many observed features of the asteroid belts, of minor satellites of Jupiter, and of objects within the Kuiper belt. As an example, many high-eccentricity comets are found to be in Kozai resonances, with their longitude of pericenter in the vicinity of $\frac { \pi } { 2 }$ or $\frac { 3 \pi } { 2 }$ .

# 3.4.3 Effects of oblateness

As our next case study we examine a two-body system perturbed by the oblateness of one of its members. As we saw back in Sec. 2.3, the oblateness is most often due to rotational flattening, and here the deformed body is taken to have an axisymmetric shape; the deformation from spherical symmetry is measured by its quadrupole moment, and we neglect the gravitational influence of higher-order multipole moments. Examples of such systems abound. We could be dealing with Mercury orbiting an oblate, rotating Sun, or an artificial satellite orbiting the Earth, or else a neutron star orbiting a rotating, normal star.

The equations of motion for such a system were worked out back in Sec. 1.6.7, and according to Eq. (1.227), the perturbing force is given by

$$
f = { \frac { 3 } { 2 } } J _ { 2 } { \frac { G m R ^ { 2 } } { r ^ { 4 } } } \Big \{ \big [ 5 ( e \cdot n ) ^ { 2 } - 1 \big ] n - 2 ( e \cdot n ) e \Big \} ,
$$

with $J _ { 2 }$ denoting the dimensionless quadrupole moment of the deformed body, $R$ its radius, and the unit vector $\pmb { e }$ indicating the direction of the symmetry axis. As usual we have $m : = m _ { 1 } + m _ { 2 }$ , $r : = r _ { 1 } - r _ { 2 } , r : = | r |$ , and ${ \pmb n } : = { \pmb r } / r$ . In Eq. (3.90) we specifically identify the oblate body with $m _ { 2 }$ , and $m _ { 1 }$ is assumed to be spherical; a swap of identities involves changing the sign of $\pmb { n }$ , and therefore the sign of the perturbing force.

We choose the reference $X { - } Y$ plane to be orthogonal to the symmetry axis of $m _ { 2 }$ , so that $_ e$ is aligned with the $Z$ -direction. The orbital plane has an inclination $\iota$ relative to the reference plane, and the orbital basis is given by Eqs. (3.42)–(3.45). According to these equations, $\pmb { e } \cdot \pmb { n } = \sin \iota \sin ( \omega + f )$ , $\pmb { e } \cdot \pmb { \lambda } = \sin \iota \cos ( \omega + f )$ , $e \cdot e _ { z } = \cos \iota$ , and the components of the

perturbing force in the orbital basis are

$$
\begin{array} { r l r } {  { \mathcal { R } = \frac { 3 } { 2 } J _ { 2 } \frac { G m R ^ { 2 } } { r ^ { 4 } } \big [ 3 \sin ^ { 2 } \iota \sin ^ { 2 } ( \omega + f ) - 1 \big ] , } } \\ & { \mathcal { S } = - 3 J _ { 2 } \frac { G m R ^ { 2 } } { r ^ { 4 } } \sin ^ { 2 } \iota \sin ( \omega + f ) \cos ( \omega + f ) , } \\ & { \mathcal { W } = - 3 J _ { 2 } \frac { G m R ^ { 2 } } { r ^ { 4 } } \sin \iota \cos \iota \sin ( \omega + f ) , } \end{array}
$$

with $r = p / ( 1 + e \cos f )$ .

We calculate the secular variation of the orbital elements $p , e , \iota , \omega$ , and $\Omega$ by inserting these expressions within Eqs. (3.69), and integrating over a complete orbital cycle. (In this case there is no need to involve the eccentric anomaly $u$ in the evaluation of the integrals; the factor of $r ^ { - 4 }$ in the perturbing force ensures that there are no remaining factors of $1 + e \cos f$ in the denominators, and all integrations are elementary.) The end results are

$$
\begin{array} { r l } & { \Delta p = 0 , } \\ & { \Delta e = 0 , } \\ & { \Delta \iota = 0 , } \\ & { \Delta \omega = 6 \pi J _ { 2 } \bigg ( \displaystyle \frac { R } { p } \bigg ) ^ { 2 } \bigg ( 1 - \frac { 5 } { 4 } \sin ^ { 2 } \iota \bigg ) , } \\ & { \Delta \Omega = - 3 \pi J _ { 2 } \bigg ( \displaystyle \frac { R } { p } \bigg ) ^ { 2 } \cos \iota . } \end{array}
$$

The first two equations imply that $\Delta a = 0$ ; there is no secular change in the eccentricity, no secular change in the semi-major axis, and no secular change in the inclination. There are, however, secular changes in the line of nodes (measured by $\Delta \Omega$ ) and in the pericenter (measured relative to the line of nodes by $\Delta \omega$ ). The last two equations imply

$$
\Delta \omega + \cos \iota \Delta \Omega = 3 \pi J _ { 2 } \bigg ( \frac { R } { p } \bigg ) ^ { 2 } \bigg ( 1 - \frac { 3 } { 2 } \sin ^ { 2 } \iota \bigg ) ;
$$

as we saw back in Sec. 3.3.2, this is the pericenter advance relative to the reference $X$ - direction, as measured in the orbital plane. At zero inclination, when $e \cdot n = 0$ , the changes are produced by the $r ^ { - 4 }$ modification to the gravitational acceleration, which is still directed along $\pmb { n }$ . For inclined orbits, the angular dependence of the perturbing force produces an additional contribution. An associated effect is a precession of the angular-momentum vector $\pmb { h }$ around the symmetry axis $\pmb { e }$ , which produces a rotation of the line of nodes. The precession is predicted by Eq. (3.51), which becomes

$$
\frac { d \pmb { h } } { d t } = 3 J _ { 2 } \frac { G m R ^ { 2 } } { r ^ { 3 } } ( \pmb { e } \cdot \pmb { n } ) ( \pmb { e } \times \pmb { n } )
$$

in the case of the perturbing force of Eq. (3.90). This describes a precession because $h$ does not change on a secular time scale, and because $e \cdot h$ stays constant during the orbital evolution.

For Mercury, the perihelion advance induced by the Sun’s oblateness is negligible. Inserting the relevant orbital elements and the value $( J _ { 2 } ) _ { \odot } = 2 . 2 \times 1 0 ^ { - 7 }$ , we obtain $( d \omega / d t ) _ { \mathrm { s e c } } + \cos \iota ( d \Omega / d t ) _ { \mathrm { s e c } } = 0 . 0 3$ as/century, which is just below the observational uncertainties assigned to the measurement of the advance (refer to Table 3.1). The conclusion relies on a reliable determination of the Sun’s oblateness, something that was difficult to come by. In fact, it is extremely difficult to measure the Sun’s $J _ { 2 }$ directly, because at planetary distances, its effects are just too small to be measured. The best way to obtain a reliable estimate would be to send a spacecraft to a low solar orbit, well inside the orbit of Mercury, and to measure precisely how $J _ { 2 }$ affects its orbit; but despite a number of proposals for such a mission over the years, none has yet come to pass.

During the 1960s, Robert Dicke and Mark Goldenberg attempted to determine $J _ { 2 }$ by measuring the Sun’s visual shape. Because the surface of the Sun is an equipotential (recall the discussion in Sec. 2.3.1), its shape is affected by $J _ { 2 }$ in a way that can be directly related to the deformation of the external gravitational field. The shape was measured by inserting a circular, opaque disk in front of a telescopic image of the Sun, leaving only a thin visible ring at the edge of the Sun, and measuring the difference in brightness of the visible ring between the equator and pole of the Sun. If the Sun were oblate, the ring at the equator should extend further beyond the occulting disk, and should therefore be brighter. But many factors had to be corrected for, including the effects of atmospheric distortion on the observed shape of the Sun, and the effects of possible temperature differences between the polar and equatorial regions of the Sun, which would lead to brightness differences not associated with the shape. Dicke and Goldenberg claimed to have measured a $J _ { 2 }$ of the order of $2 . 5 \times 1 0 ^ { - 5 }$ , over 100 times larger than the currently accepted value. Dicke postulated that such a large oblateness would occur if the core of the Sun were rotating much faster than its outer layers, thereby generating more centrifugal flattening than would be expected on the basis of the observed surface rotation alone.

A value of $J _ { 2 }$ this large would mean that solar oblateness contributes as much as 4 as/century to Mercury’s perihelion advance, which would destroy the agreement of the measured advance with the prediction of general relativity. But it would have supported the scalar-tensor theory of gravity (to be presented in Chapter 13) that Dicke himself had developed with Carl Brans, whose prediction for the relativistic part of the advance could be fit to ${ 3 9 } \mathrm { a s } ,$ /century by tuning a coupling constant. (The flexibility to tune the Brans–Dicke parameter to obtain this low value was short lived; accurate observations of the relativistic light deflection eventually constrained the coupling constant to such an extent that the Brans–Dicke prediction for the perihelion advance of Mercury became only marginally different from Einstein’s.) Later observations of the visible shape of the Sun by Henry Hill and others, along with observations to try to better understand the temperature differences, did not fully resolve this controversy.

The resolution came with the advance of helioseismology. This was the discovery that the Sun vibrates in a superposition of thousands of normal modes with an array of frequencies, as could be observed by measuring the frequency spectrum of Doppler-shifted solar spectral lines. The specific pattern of frequencies depends on the Sun’s angular-velocity profile. Through a systematic program of ground-based and space-based observations of the Sun, it became possible to determine the Sun’s rotational profile over much of its interior. The conclusion was that the core does not rotate much faster than the surface, and solar models consistent with this information produced the currently accepted value of $J _ { 2 } = 2 . 2 \times 1 0 ^ { - 7 }$ ; this is approximately what one would infer from a Sun that rotates uniformly at its observed surface rate. The bottom line is that, as far as Mercury’s motion and general relativity are concerned, the solar quadrupole moment does not play a significant role.

The quadrupole moment of the Earth does play an important role in the motion of artificial satellites. The effect on the line of nodes can be examined for a satellite placed on a circular orbit with radius $a$ . Using $( J _ { 2 } ) _ { \oplus } = 1 . 0 8 \times 1 0 ^ { - 3 }$ and dividing $\Delta \Omega$ by the satellite’s orbital period $P = 2 \pi a ^ { 3 / 2 } / ( G m ) ^ { 1 / 2 } = 8 3 . 9 1 ( a / R ) ^ { 3 / 2 }$ minutes, we can show that

$$
\left( \frac { d \Omega } { d t } \right) _ { \mathrm { s e c } } = - 3 6 3 9 \left( \frac { R } { a } \right) ^ { 7 / 2 } \mathrm { c o s } \iota \quad \mathrm { d e g r e e s / y e a r } ,
$$

where $R$ is the Earth’s radius. For example, the orbit of the Laser Geodynamics Satellite (LAGEOS) I, with $a = 1 . 9 3 R$ and $\iota = 1 0 9 ^ { \circ } . 8$ , precesses at a rate of 120 degrees per year. A satellite with $a = 1 . 5 R$ and $\iota = 6 5 . 9 ^ { \circ }$ would precess at a rate of 360 degrees per year. Such an orbit is called Sun synchronous because it always presents the same face to the Sun, varying only in its inclination relative to the ecliptic because of the $2 3 . 5 ^ { \circ }$ tilt of the Earth’s spin axis.

# 3.4.4 Tidally interacting bodies

In our next case study we examine a system of two bodies that deform each other by tidal interactions. The physics of tides was reviewed in some depth in Sec. 2.5, and here we consider a situation in which the orbital period $P = 2 \pi a ^ { 3 / 2 } / ( G m ) ^ { 1 / 2 }$ is long compared with the hydrodynamical time scale $T _ { \mathrm { i n t } } \sim ( G \rho ) ^ { - 1 / 2 } \sim R ^ { 3 / 2 } / ( G m ) ^ { 1 / 2 }$ that characterizes the internal dynamics of each body; this is the realm of static tides.

We first take the bodies to be non-rotating. According to the theory developed in Sec. 2.5.1, a body of radius $R$ subjected to a tidal potential $\begin{array} { r } { U _ { \mathrm { t i d a l } } = - \frac { 1 } { 2 } \mathcal { E } _ { j k } x ^ { j } x ^ { k } } \end{array}$ acquires a mass quadrupole moment given by $\begin{array} { r } { G I _ { \langle j k \rangle } = - \frac { 2 } { 3 } k _ { 2 } R ^ { 5 } \mathcal { E } _ { j k } } \end{array}$ , with $k _ { 2 }$ denoting the body’s gravitational Love number, which depends on the details of its internal structure. In the case of a two-body system, we have a first body of mass $m _ { 1 }$ , radius $R _ { 1 }$ , Love number $( k _ { 2 } ) _ { 1 }$ , and quadrupole moment $I _ { 1 } ^ { \langle j k \rangle }$ , and a second body of mass $m _ { 2 }$ , radius $R _ { 2 }$ , Love number $( k _ { 2 } ) _ { 2 }$ , and quadrupole moment $I _ { 2 } ^ { \langle j k \rangle }$ . According to Eq. (2.275), the tidal quadrupole mo-jk ment created by and acting on $m _ { 1 }$ is given by , while the tidal moment created by $m _ { 1 }$ and acting on $m _ { 2 }$ is $\mathcal { E } _ { 2 } ^ { j k } = - ( G m _ { 1 } / r ^ { 3 } ) ( 3 n ^ { j } n ^ { k } - \delta ^ { j k } )$ ; as usual, we have that $m : = m _ { 1 } + m _ { 2 }$ , $r : = r _ { 1 } - r _ { 2 } , r : = | r |$ , and ${ \pmb n } : = { \pmb r } / r$ . From all this we find that the tidally-induced mass quadrupole moment of the first body is given by

$$
I _ { 1 } ^ { \langle j k \rangle } = \frac { 2 } { 3 } ( k _ { 2 } ) _ { 1 } \frac { m _ { 2 } R _ { 1 } ^ { 5 } } { r ^ { 3 } } \big ( 3 n ^ { j } n ^ { k } - \delta ^ { j k } \big ) ,
$$

while

$$
I _ { 2 } ^ { \langle j k \rangle } = \frac { 2 } { 3 } ( k _ { 2 } ) _ { 2 } \frac { m _ { 1 } R _ { 2 } ^ { 5 } } { r ^ { 3 } } \big ( 3 n ^ { j } n ^ { k } - \delta ^ { j k } \big )
$$

is the mass quadrupole moment of the second body.

The equations of motion for two deformed bodies were obtained back in Sec. 1.6.7, and Eq. (1.220) provides an expression for the relative acceleration $\pmb { a } : = \pmb { a } _ { 1 } - \pmb { a } _ { 2 }$ . If we remove the Keplerian term, truncate the multipole expansions to the leading, quadrupole order, and neglect the quadrupole–quadrupole interaction (which is much smaller than the monopole–quadrupole interactions that we keep), we obtain

$$
f ^ { j } = \frac 1 2 G m \biggl ( \frac { I _ { 1 } ^ { \langle k n \rangle } } { m _ { 1 } } + \frac { I _ { 2 } ^ { \langle k n \rangle } } { m _ { 2 } } \biggr ) \partial _ { j k n } \biggl ( \frac { 1 } { r } \biggr )
$$

for the perturbing force. Inserting the preceding expressions for the mass quadrupole moments, as well as Eq. (1.152) for $\partial _ { j k n } { r ^ { - 1 } }$ , we find that this becomes

$$
{ \pmb f } = - 6 \frac { G m } { r ^ { 7 } } \biggl ( ( k _ { 2 } ) _ { 1 } \frac { m _ { 2 } } { m _ { 1 } } R _ { 1 } ^ { 5 } + ( k _ { 2 } ) _ { 2 } \frac { m _ { 1 } } { m _ { 2 } } R _ { 2 } ^ { 5 } \biggr ) { \pmb n } .
$$

The perturbing force is directed along $\pmb { n }$ , and its only non-vanishing component is $\mathcal { R }$ . With $\textstyle S = \mathcal { W } = 0$ , we see that the tidal interaction has no effect on $p , \iota$ , and $\Omega$ ; the only orbital elements that can undergo a change are $e$ and $\omega$ .

We insert our expression for $\mathcal { R }$ within Eqs. (3.69), integrate over a complete orbital cycle, and obtain the secular changes $\Delta e = 0$ and

$$
\Delta \omega = 3 0 \pi \left( 1 + \frac { 3 } { 2 } e ^ { 2 } + \frac { 1 } { 8 } e ^ { 4 } \right) \Biggl [ ( k _ { 2 } ) _ { 1 } \frac { m _ { 2 } } { m _ { 1 } } \left( \frac { R _ { 1 } } { p } \right) ^ { 5 } + ( k _ { 2 } ) _ { 2 } \frac { m _ { 1 } } { m _ { 2 } } \left( \frac { R _ { 2 } } { p } \right) ^ { 5 } \Biggr ] .
$$

These results imply that $e$ (and therefore $a$ ) do not undergo a secular change, but the pericenter advances at a steady rate that depends on the orbital parameters, the body radii, and the gravitational Love numbers. Astronomers call this phenomenon the apsidal advance, and for a class of close binaries, this effect gives an important clue to the internal structure of each star, via the ability to infer $k _ { 2 }$ . These systems have masses of the order of a few solar masses, orbital periods of the order of 10 days, and modest eccentricities. The resulting apsidal advance can then be expressed as the rate

$$
\begin{array} { r } { \begin{array} { r } { \left( \frac { d \omega } { d t } \right) _ { \mathrm { s e c } } = 0 . 0 6 f ( e ) \biggl ( \frac { M _ { \odot } } { m } \biggr ) ^ { 5 / 3 } \biggl ( \frac { 1 0 \mathrm { d a y s } } { P } \biggr ) ^ { 1 3 / 3 } } \\ { \qquad \times \left[ \frac { ( k _ { 2 } ) _ { 1 } } { 0 . 0 1 } \frac { m _ { 2 } } { m _ { 1 } } \biggl ( \frac { R _ { 1 } } { R _ { \odot } } \biggr ) ^ { 5 } + \frac { ( k _ { 2 } ) _ { 2 } } { 0 . 0 1 } \frac { m _ { 1 } } { m _ { 2 } } \biggl ( \frac { R _ { 2 } } { R _ { \odot } } \biggr ) ^ { 5 } \right] \mathrm { d e g r e e s / c e n t u r y } , } \end{array} } \end{array}
$$

where $f ( e ) = ( 1 + \textstyle { \frac { 3 } { 2 } } e ^ { 2 } + \textstyle { \frac { 1 } { 8 } } e ^ { 4 } ) / ( 1 - e ^ { 2 } ) ^ { 5 } .$ . Many close binaries are eclipsing, and by combining light-curve data on the timing of eclipses with spectroscopic data on the orbital motion, it is possible to determine the masses and radii as well as the apsidal advance rate, and thereby estimate $k _ { 2 }$ for each star. In most cases, there is good agreement between the values of $k _ { 2 }$ obtained by implementing this method and those determined by stellar models for stars having the observed masses and spectra. As we shall see in Chapter 10, the general relativistic contribution to the apsidal advance is small, generally a few percent of the tidally induced advance.

# Box 3.4

DI Herculis: A tidal troublemaker There are a few systems for which the nice picture of a tidally induced apsidal advance does not work. The most famous is DI Herculis, a high eccentricity $( e \simeq 0 . 4 8 )$ , high mass $( m \simeq 1 0 M _ { \odot } )$ system with a 10.55 day period. In this case, the relativistic contribution to the apsidal advance is large, 2.34 degrees per century, while the tidal contribution is predicted to be 1.93 degrees per century, giving a total predicted advance of 4.27 degrees per century. Unfortunately, the observed apsidal advance is only $1 . 0 0 \pm . 3 0$ degrees per century. While there were a few attempts to use this discrepancy as evidence against general relativity, more conventional explanations involve purely Newtonian mechanisms. First, there could be a large misalignment between the rotation axis of each star and the orbital plane, such that the contribution of the rotationallyinduced quadrupole moments to ω would be negative, or retrograde. Second, there could be a third star in the vicinity of the system, whose perturbative effects on all the orbital elements would complicate how $\Delta \omega$ is inferred from the eclipse light-curve data, leading to a value in better agreement with the prediction. The book is not yet closed on DI Herculis.

Our discussion thus far has excluded the dissipative aspects of tidal dynamics that were reviewed in Sec. 2.5.2. To explore these effects we examine specifically the case of a moon orbiting a planet. We take the first body to be the planet, the second body to be the moon, and we place the bodies on a circular orbit of relative separation $r$ . Both bodies are now rotating, and we take the moon to be tidally locked, so that it rotates with the same angular velocity as the orbit. The planet, on the other hand, rotates with an angular velocity $\omega _ { 1 }$ that differs, in general, from the orbital angular velocity $\Omega$ .

According to Eq. (2.277), the quadrupole moment of each body is given by

$$
G I _ { \langle j k \rangle } = - \frac { 2 } { 3 } k _ { 2 } R ^ { 5 } \Big ( \mathscr { E } _ { j k } - \tau \dot { \mathscr { E } } _ { j k } \Big )
$$

in the body’s rotating frame. The effect of the first term was investigated previously, and we henceforth ignore it. We keep the second term, the one associated with the dissipative aspects of the tidal interaction; the parameter $\tau$ is the body’s viscous delay. Because the moon is co-rotating with the orbit, the tidal field measured in its rotating frame is constant, and this implies that we can set $I _ { 2 } ^ { \langle j k \rangle } = 0$ ; for our purposes here, the moon is not deformed by the tidal forces exerted by the planet. The planet, however, is deformed by the moon’s tidal field, and we find that its quadrupole moment is given by

$$
I _ { 1 } ^ { \langle j k \rangle } = - 2 ( k _ { 2 } ) _ { 1 } \frac { m _ { 2 } R _ { 1 } ^ { 5 } } { r ^ { 3 } } ( \Omega - \omega _ { 1 } ) \tau _ { 1 } \left( n ^ { j } \lambda ^ { k } + \lambda ^ { j } n ^ { k } \right)
$$

in the rotating frame. Inserting this within the perturbing force of Eq. (3.98), we find that its dissipative piece is given by

$$
\pmb { f } _ { \mathrm { d i s s } } = - 6 ( k _ { 2 } ) _ { 1 } G m \frac { m _ { 2 } } { m _ { 1 } } \frac { R _ { 1 } ^ { 5 } } { r ^ { 7 } } ( \Omega - \omega _ { 1 } ) \tau _ { 1 } \pmb { \lambda } .
$$

Its only non-vanishing component is $S _ { \mathrm { d i s s } } : = { f _ { \mathrm { d i s s } } } \cdot \lambda$ .

The dissipative piece of the perturbing force can now be inserted within the osculating equations (3.69). We find that $r$ is the only orbital element that is affected by the perturbation, and that it changes by

$$
\Delta r = - 2 4 \pi ( k _ { 2 } ) _ { 1 } \frac { m _ { 2 } } { m _ { 1 } } \frac { R _ { 1 } ^ { 5 } } { r ^ { 4 } } ( \Omega - \omega _ { 1 } ) \tau _ { 1 }
$$

in the course of a complete orbital cycle. The sign of the change is related to the sign of $\Omega - \omega _ { 1 }$ . When $\omega _ { 1 } < \Omega$ , that is, when the moon orbits faster than the planet rotates, we find that $\Delta r < 0$ , so that the moon slowly approaches the planet in a shrinking orbit; an example of such a situation is found in the Mars–Phobos system. When $\omega _ { 1 } > \Omega$ , that is, when the planet rotates faster than the moon orbits, we find instead that $\Delta r > 0$ , so that the moon recedes from the planet in an expanding orbit; the Earth–Moon system is a familiar example of such a situation. These conclusions are in accord with our discussion of angularmomentum transfer in Sec. 2.5.2. We saw that the planet gains spin angular momentum when $\omega _ { 1 } < \Omega$ , and the shrinking orbit confirms that this gain comes at the expense of the orbital angular momentum. Similarly, the planet loses its spin when $\omega _ { 1 } > \Omega$ , and this loss allows the orbit to gain angular momentum and to expand.

# 3.4.5 Luni-solar precession of the Earth

In this final case study we describe how the gravitational attraction of the Moon and the Sun on an oblate Earth causes a precession of its spin around the normal to the ecliptic plane. This is the origin of the famous precession of the equinoxes, with its period of approximately 26 000 years.

The motion of a body’s spin vector $s$ subjected to gravitational torques exerted by other bodies was determined back in Sec 1.6.8. According to Eq. (1.240), an axisymmetric body of mass $m$ , radius $R$ , and dimensionless quadrupole moment $J _ { 2 }$ , placed in the gravitational field of a first mass $m _ { 1 }$ at a distance $r _ { 1 }$ , and of a second mass $m _ { 2 }$ at a distance $r _ { 2 }$ , undergoes a spin precession described by

$$
\frac { d \pmb { S } } { d t } = - 3 G m J _ { 2 } R ^ { 2 } \bigg [ \frac { m _ { 1 } } { r _ { 1 } ^ { 3 } } ( \pmb { e } \cdot \pmb { n } _ { 1 } ) ( \pmb { e } \times \pmb { n } _ { 1 } ) + \frac { m _ { 2 } } { r _ { 2 } ^ { 3 } } ( \pmb { e } \cdot \pmb { n } _ { 2 } ) ( \pmb { e } \times \pmb { n } _ { 2 } ) \bigg ] .
$$

Here, $_ e$ is the direction of the body’s rotation axis, so that $\pmb { S } = S \pmb { e }$ , $\pmb { n } _ { 1 }$ is the direction to $m _ { 1 }$ , and $\pmb { n } _ { 2 }$ the direction to $m _ { 2 }$ . Note that in this application, $m$ stands for the body’s mass instead of the total mass of the system. It is easy to see from Eq. (3.106) that $S$ is a constant, so that $d S / d t = S d e / d t$ .

For simplicity, and as a rather good approximation, we take the Moon and the Sun to move on circular orbits in the ecliptic plane, which we identify with the reference $X { - } Y$ plane. The direction to the Moon is then

$$
{ \pmb n } _ { 1 } = \cos ( \Omega _ { 1 } t ) { \pmb e } _ { X } + \sin ( \Omega _ { 1 } t ) { \pmb e } _ { Y } ,
$$

with $\Omega _ { 1 }$ denoting the Moon’s angular velocity, while the direction to the Sun is

$$
\pmb { n } _ { 2 } = \cos ( \Omega _ { 2 } t + \psi ) \pmb { e } _ { X } + \sin ( \Omega _ { 2 } t + \psi ) \pmb { e } _ { Y } ,
$$

with $\Omega _ { 2 }$ denoting the Sun’s angular velocity, and $\psi$ representing the Sun’s initial phase on its orbit. The Earth’s rotation axis is tilted by an angle $\alpha = 2 3 . 4 ^ { \circ }$ relative to the ecliptic, and we express its direction as

$$
e = \sin \alpha \cos \beta e _ { X } + \sin \alpha \sin \beta e _ { Y } + \cos \alpha e _ { Z } ,
$$

in terms of a time-dependent precessional angle $\beta$ . As we shall see, Eq. (3.106) implies that $\alpha$ remains constant on a secular time scale.

We insert these expressions within Eq. (3.106) and average the result over a large number of orbital cycles. We obtain

$$
\left( \frac { d e } { d t } \right) _ { \mathrm { s e c } } = - \frac { 3 G m J _ { 2 } R ^ { 2 } } { 2 S } \sin \alpha \cos \alpha \Bigg ( \frac { m _ { 1 } } { r _ { 1 } ^ { 3 } } + \frac { m _ { 2 } } { r _ { 2 } ^ { 3 } } \Bigg ) \Big ( - \sin \beta e _ { X } + \cos \beta e _ { Y } \Big ) .
$$

Substitution of Eq. (3.109) on the left-hand side confirms that $( d \alpha / d t ) _ { \mathrm { s e c } } = 0$ , and gives rise to a rate of change for the precessional angle,

$$
\left( \frac { d \beta } { d t } \right) _ { \mathrm { s e c } } = - \frac { 3 G m J _ { 2 } R ^ { 2 } } { 2 S } \cos \alpha \biggl ( \frac { m _ { 1 } } { r _ { 1 } ^ { 3 } } + \frac { m _ { 2 } } { r _ { 2 } ^ { 3 } } \biggr ) .
$$

Inserting the relevant numbers, including $S = 5 . 8 6 \times 1 0 ^ { 3 3 } \mathrm { k g } \mathrm { m } ^ { 2 } / \mathrm { s }$ and $J _ { 2 } = 1 . 0 8 \times 1 0 ^ { - 3 }$ , we obtain $| ( d \beta / d t ) _ { \mathrm { s e c } } | = 7 . 7 4 \times 1 0 ^ { - 1 2 } ~ \mathrm { r a d / s }$ , or 5040 as/century, which is very close to the accepted value of 5029 as/century. The precessional period $P _ { \mathrm { p r e c } } = 2 \pi | ( d \beta / d t ) _ { \mathrm { s e c } } | ^ { - 1 }$ amounts to the previously quoted value of 26 000 years.

# 3.5 More bodies

We saw back in Sec. 3.2 that the problem of two spherical bodies moving under their mutual gravitational attraction can be solved completely and exactly. The same cannot be said, however, when the bodies have significant deformations from spherical symmetry, or when we go beyond two bodies; in such cases there are no exact solutions, except in very special situations. In this section we touch briefly on the three-body problem, and say a few words about the general $N$ -body problem; throughout this section the bodies are assumed to be spherical.

# 3.5.1 The 3-body problem

# General problem

Adding just one body to a two-body system brings a remarkable complexity to the problem of motion. The equations of motion are simple enough to write down. In the familiar

notation we have

$$
\begin{array} { r } { a _ { 1 } = - G m _ { 2 } \frac { { r _ { 1 2 } } } { { r _ { 1 2 } ^ { 3 } } } - G m _ { 3 } \frac { { r _ { 1 3 } } } { { r _ { 1 3 } ^ { 3 } } } , } \\ { a _ { 2 } = + G m _ { 1 } \frac { { r _ { 1 2 } } } { { r _ { 1 2 } ^ { 3 } } } - G m _ { 3 } \frac { { r _ { 2 3 } } } { { r _ { 2 3 } ^ { 3 } } } , } \\ { a _ { 3 } = + G m _ { 1 } \frac { { r _ { 1 3 } } } { { r _ { 1 3 } ^ { 3 } } } + G m _ { 2 } \frac { { r _ { 2 3 } } } { { r _ { 2 3 } ^ { 3 } } } , } \end{array}
$$

where, for example, $r _ { 1 2 } : = r _ { 1 } - r _ { 2 }$ . According to the discussion of Sec. 1.6.6, the equations of motion admit the conserved quantities

$$
\begin{array} { l } { P = m _ { 1 } \pmb { v } _ { 1 } + m _ { 2 } \pmb { v } _ { 2 } + m _ { 3 } \pmb { v } _ { 3 } , } \\ { \pmb { L } = m _ { 1 } \pmb { r } _ { 1 } \times \pmb { v } _ { 1 } + m _ { 2 } \pmb { r } _ { 2 } \times \pmb { v } _ { 2 } + m _ { 3 } \pmb { r } _ { 3 } \times \pmb { v } _ { 3 } , } \\ { E = \cfrac { 1 } { 2 } m _ { 1 } \pmb { v } _ { 1 } ^ { 2 } + \cfrac { 1 } { 2 } m _ { 2 } \pmb { v } _ { 2 } ^ { 2 } + \cfrac { 1 } { 2 } m _ { 1 } \pmb { v } _ { 2 } ^ { 2 } - \cfrac { G m _ { 1 } m _ { 2 } } { r _ { 1 2 } } - \cfrac { G m _ { 1 } m _ { 3 } } { r _ { 1 3 } } - \cfrac { G m _ { 2 } m _ { 3 } } { r _ { 2 3 } } . } \end{array}
$$

Momentum conservation implies that the system’s barycenter, situated at

$$
\pmb { R } : = \frac { 1 } { M } \big ( m _ { 1 } \pmb { r } _ { 1 } + m _ { 2 } \pmb { r } _ { 2 } + m _ { 3 } \pmb { r } _ { 3 } \big ) ,
$$

with $M : = m _ { 1 } + m _ { 2 } + m _ { 3 }$ , moves uniformly according to $\pmb { R } ( t ) : = \pmb { R } ( 0 ) + \pmb { P } t / M$ . We shall describe the 3-body system in the barycentric frame, and set $\pmb { R = 0 }$ at all times.

In the two-body problem it proved helpful to write the equations of motion in terms of the separation vector between the two bodies, which produces a reduction to an effective one-body problem. Here we follow Jacobi and accomplish a similar reduction to an effective two-body problem by introducing the alternative variables

$$
\begin{array} { l } { { \pmb r : = \pmb r _ { 1 } - { \pmb r } _ { 2 } , } } \\ { { \pmb \rho : = \pmb r _ { 3 } - \frac { m _ { 1 } } { m } \pmb r _ { 1 } - \frac { m _ { 2 } } { m } \pmb r _ { 2 } , } } \end{array}
$$

in which $m : = m _ { 1 } + m _ { 2 }$ ; the vector $r$ is the separation between body 1 and body 2, while $\pmb { \rho }$ is the separation between body 3 and the barycenter of the 1–2 subsystem. The barycenter condition $\pmb { R = 0 }$ can be used to express each position vector in terms of the new variables; we find that

$$
\begin{array} { l } { { \displaystyle r _ { 1 } = \frac { m _ { 2 } } { m } r - \frac { m _ { 3 } } { M } \rho , } } \\ { { \displaystyle r _ { 2 } = - \frac { m _ { 1 } } { m } r - \frac { m _ { 3 } } { M } \rho , } } \\ { { \displaystyle r _ { 3 } = \frac { m } { M } \rho . } } \end{array}
$$

Similar relations hold between the individual velocity vectors and the relative velocities $v : =$ $d r / d t$ and $V : = d \pmb { \rho } / d t$ . The separation vectors become $r _ { 1 2 } = r$ , $r _ { 1 3 } = - ( \pmb { \rho } - m _ { 2 } \pmb { r } / m )$ , and $r _ { 2 3 } = - ( \pmb { \rho } + m _ { 1 } \pmb { r } / m )$ in the Jacobi variables.

Making the substitutions, we quickly find that the equations of motion of the effective two-body problem are

$$
\begin{array} { l } { \displaystyle \frac { d ^ { 2 } { \boldsymbol { r } } } { d t ^ { 2 } } = - G m \frac { { \boldsymbol { r } } } { r ^ { 3 } } + G m _ { 3 } \bigg ( \frac { \rho - m _ { 2 } { \boldsymbol { r } } / m } { | \rho - m _ { 2 } { \boldsymbol { r } } / m | ^ { 3 } } - \frac { \rho + m _ { 1 } { \boldsymbol { r } } / m } { | \rho + m _ { 1 } { \boldsymbol { r } } / m | ^ { 3 } } \bigg ) , } \\ { \displaystyle \frac { d ^ { 2 } \rho } { d t ^ { 2 } } = - \frac { G M } { m } \bigg ( m _ { 1 } \frac { \rho - m _ { 2 } { \boldsymbol { r } } / m } { | \rho - m _ { 2 } { \boldsymbol { r } } / m | ^ { 3 } } + m _ { 2 } \frac { \rho + m _ { 1 } { \boldsymbol { r } } / m } { | \rho + m _ { 1 } { \boldsymbol { r } } / m | ^ { 3 } } \bigg ) , } \end{array}
$$

and that the conserved quantities become

$$
\begin{array} { l } { { { \cal L } = \displaystyle \frac { m _ { 1 } m _ { 2 } } { m } r \times \displaystyle v + \displaystyle \frac { m m _ { 3 } } { M } \rho \times V , } } \\ { { { \cal E } = \displaystyle \frac { 1 } { 2 } \displaystyle \frac { m _ { 1 } m _ { 2 } } { m } v ^ { 2 } + \displaystyle \frac { 1 } { 2 } \displaystyle \frac { m m _ { 3 } } { M } V ^ { 2 } - \displaystyle \frac { G m _ { 1 } m _ { 2 } } { r } - \displaystyle \frac { G m _ { 1 } m _ { 3 } } { | \rho - m _ { 2 } r / m | } - \displaystyle \frac { G m _ { 2 } m _ { 3 } } { | \rho + m _ { 1 } r / m | } } } \end{array}
$$

in the Jacobi variables.

The equations of motion (3.117) are extraordinarily complex, and in spite of massive efforts by the best physicists and mathematicians of past centuries, including Lagrange, Laplace, Jacobi, Hill, and especially Poincare, the solution space is still poorly understood´ today. Special solutions are known. For example, when the three bodies are confined to a plane it is possible to find solutions with $r _ { 1 2 } = r _ { 1 3 } = r _ { 2 3 }$ , so that the bodies form an equilateral triangle. In this configuration, each body follows its own elliptical orbit around the barycenter, with the triangle expanding and shrinking as the bodies pass simultaneously through their apocenter and pericenter; in the special case of circular orbits, the three bodies rotate as a rigid equilateral triangle around the barycenter. Another example is the “figureof-eight” solution, in which three equal-mass bodies chase each other on a closed orbit that takes the shape of the number eight; the solution has zero total angular momentum. Understanding the three-body problem is of considerable astrophysical interest, since over 500 stars in our galaxy have been identified as triple systems, including the north star Polaris and our nearest neighbor, Alpha Centauri.

# Restricted problem

There is a special case of the three-body problem that offers sufficient simplicity to permit a detailed exploration. Known as the restricted three-body problem, this is a situation in which one of the three bodies has a negligible mass compared to the others, and the other two bodies are placed on a circular orbit, undisturbed by the third body. In this case the three-body problem reduces to an independent two-body problem with a specified solution (the circular orbit), and the decoupled problem of a test body moving in the gravitational field of the orbiting bodies.

We take the light body to be $m _ { 3 }$ , and let $m _ { 3 } \ll m _ { 1 }$ and $m _ { 3 } \ll m _ { 2 }$ , so that $M \simeq m =$ $m _ { 1 } + m _ { 2 }$ . In this limit the equations of motion become $d ^ { 2 } \bar { \pmb { r } } / d t ^ { 2 } = - G m \bar { \pmb { r } } / r ^ { 3 }$ for the twobody system, and

$$
\frac { d ^ { 2 } \bar { \rho } } { d t ^ { 2 } } = - G m _ { 1 } \frac { \bar { \rho } - m _ { 2 } \bar { r } / m } { | \bar { \rho } - m _ { 2 } \bar { r } / m | ^ { 3 } } - G m _ { 2 } \frac { \bar { \rho } + m _ { 1 } \bar { r } / m } { | \bar { \rho } + m _ { 1 } \bar { r } / m | ^ { 3 } }
$$

for the third body; the reason for adorning each vector with an overbar will be revealed presently. In this limit we have $\pmb { \bar { r } } _ { 1 } = ( m _ { 2 } / m ) \pmb { \bar { r } }$ , $\bar { \pmb { r } } _ { 2 } = - ( m _ { 1 } / m ) \bar { \pmb { r } }$ , and $r _ { 3 } = \bar { \rho }$ . The circular orbit of the two-body system is described by

$$
\begin{array} { r } { \overline { { r } } = r \cos ( \Omega t ) \overline { { e } } _ { x } + r \sin ( \Omega t ) \overline { { e } } _ { y } , } \end{array}
$$

with $r =$ constant and $\Omega : = \sqrt { G m / r ^ { 3 } }$ denoting the orbital angular velocity.

The equations are presented in a frame $( { \bar { x } } , { \bar { y } } , { \bar { z } } )$ that is attached to the barycenter of the three-body system. This frame is non-rotating, and accordingly, the motion of the two-body system is described by the circular orbit of Eq. (3.120). To proceed it is helpful to switch reference frames, and to choose instead a frame $( x , y , z )$ that is co-rotating with the orbiting bodies. The tools to achieve this were developed near the end of Sec. 2.3.1, and the notation adopted here, with bars placed on the non-rotating coordinates and no decoration placed on rotating coordinates, follows the conventions adopted back in Chapter 2. The coordinate transformation is given by ${ \bar { x } } = x$ cos $\Omega t - y$ sin $\Omega t$ , ${ \bar { y } } = x$ sin $\Omega t + y$ cos $\Omega t$ , $\bar { z } = z$ , and the two-body system appears stationary in the rotating frame; the separation vector is now given by

$$
\begin{array} { r } { r = r \pmb { e } _ { x } , } \end{array}
$$

and body 1 is now fixed at coordinates $x _ { 1 } = ( m _ { 2 } / m ) r$ and $y _ { 1 } = 0$ , while body 2 is at coordinates $x _ { 2 } = - ( m _ { 1 } / m ) r$ and $y _ { 2 } = 0$ .

Simple manipulations reveal that the equations of motion of the test body become

$$
\frac { d ^ { 2 } \pmb { \rho } } { d t ^ { 2 } } + 2 \pmb { \Omega } \times \frac { d \pmb { \rho } } { d t } = \pmb { \nabla } \Phi
$$

in the rotating frame, where ${ \pmb \Omega } : = \Omega { \pmb e } _ { z }$ is the angular-velocity vector, and

$$
\Phi = \frac { 1 } { 2 } \Omega ^ { 2 } \bigl [ \rho ^ { 2 } - ( \pmb { \rho } \cdot \pmb { e } _ { z } ) ^ { 2 } \bigr ] + \frac { G m _ { 1 } } { | \pmb { \rho } - m _ { 2 } \pmb { r } / m | } + \frac { G m _ { 2 } } { | \pmb { \rho } + m _ { 1 } \pmb { r } / m | } ,
$$

a generalized potential that includes both gravitational and centrifugal terms; in Eq. (3.122) the gradient operator $\mathbf { \nabla } \nabla$ refers to the three components of the vector $\pmb { \rho }$ in the rotating frame. The equations admit a first integral, which is obtained by taking the scalar product of Eq. (3.122) with $d \pmb { \rho } / d t$ and recognizing that each term is a total derivative with respect to $t$ . Integration produces the Jacobi integral

$$
{ \frac { 1 } { 2 } } V ^ { 2 } - \Phi = C ,
$$

where $V : = | d \pmb \rho / d t |$ is the speed of the test body in the rotating frame, and $C$ is a constant of the motion, a generalized energy known as Jacobi’s constant.

# Equilibria of the restricted problem

The motions predicted by Eq. (3.122) are extremely diverse, and a complete exploration would require numerical integration of the equations. The question we shall investigate here is whether the equations admit stationary solutions with $d \pmb { \rho } / d t = \pmb { 0 } = d ^ { 2 } \pmb { \rho } / d t ^ { 2 }$ . If such solutions exist, they would occur at values of $\pmb { \rho }$ such that $\nabla \Phi = \mathbf { 0 }$ , that is, at stationary points of the generalized potential. A little thought reveals that a stationary solution requires the test body to be in the same plane as the orbiting bodies.

To simplify the analysis we adopt $r$ as a unit of length, and divide all distances by $r$ so that they become dimensionless. Similarly, we adopt $m : = m _ { 1 } + m _ { 2 }$ as a unit of mass, and divide all masses by $m$ so that they too become dimensionless. In those units, the first body is situated at $x _ { 1 } = m _ { 2 }$ , the second body at $x _ { 2 } = - m _ { 1 }$ , and the orbital angular velocity is $\sqrt { G }$ . We take the test body to have coordinates $\pmb { \rho } = ( x _ { 3 } , y _ { 3 } , 0 )$ , and let

$$
\begin{array} { l } { r _ { 1 } : = { r _ { 1 3 } } = | \rho - { m _ { 2 } } r / m | = \sqrt { ( { x _ { 3 } } - { m _ { 2 } } ) ^ { 2 } + { y _ { 3 } ^ { 2 } } } , } \\ { r _ { 2 } : = { r _ { 2 3 } } = | \rho + { m _ { 1 } } r / m | = \sqrt { ( { x _ { 3 } } + { m _ { 1 } } ) ^ { 2 } + { y _ { 3 } ^ { 2 } } } . } \end{array}
$$

With $m _ { 1 } + m _ { 2 }$ now restricted to be unity, the individual masses are determined by the mass ratio $q : = m _ { 1 } / m _ { 2 } \leq 1$ ; we have that

$$
m _ { 1 } = \frac { q } { 1 + q } , \qquad m _ { 2 } = \frac { 1 } { 1 + q } ,
$$

and we adopt the convention that the first body will be the less massive of the two main bodies.

The generalized potential is given by

$$
G ^ { - 1 } \Phi = \frac { 1 } { 2 } \bigl ( x _ { 3 } ^ { 2 } + y _ { 3 } ^ { 2 } \bigr ) + \frac { m _ { 1 } } { r _ { 1 } } + \frac { m _ { 2 } } { r _ { 2 } }
$$

in the rescaled variables, and differentiation with respect to $x _ { 3 }$ and $y _ { 3 }$ produces the equilibrium conditions $x _ { 3 } - m _ { 1 } ( x _ { 3 } - m _ { 2 } ) / r _ { 1 } ^ { 3 } - m _ { 2 } ( x _ { 3 } + m _ { 1 } ) / r _ { 2 } ^ { 3 } = 0$ and $y _ { 3 } - m _ { 1 } y _ { 3 } / r _ { 1 } ^ { 3 } -$ $m _ { 2 } y _ { 3 } / r _ { 2 } ^ { 3 } = 0$ . These can be re-expressed as

$$
\begin{array} { l } { 0 = m _ { 1 } ( x _ { 3 } - m _ { 2 } ) ( 1 - r _ { 1 } ^ { - 3 } ) + m _ { 2 } ( x _ { 3 } + m _ { 1 } ) ( 1 - r _ { 2 } ^ { - 3 } ) , } \\ { 0 = y _ { 3 } \big [ m _ { 1 } ( 1 - r _ { 1 } ^ { - 3 } ) + m _ { 2 } ( 1 - r _ { 2 } ^ { - 3 } ) \big ] , } \end{array}
$$

by exploiting the identity $m _ { 1 } + m _ { 2 } = 1$ . The existence of stationary solutions hinges on finding solutions to these algebraic equations. As we shall see below, there are five distinct solutions, which are known as the Lagrange points $L _ { 1 } , L _ { 2 } , L _ { 3 } , L _ { 4 }$ , and $L _ { 5 }$ . The first three equilibria have $y _ { 3 } = 0$ and describe co-linear configurations, with all three bodies aligned on the $x$ -axis; these equilibria are unstable. The last two equilibria have $r _ { 1 } = r _ { 2 } = 1$ and describe triangular configurations, with all three bodies equidistant from each other; these equilibria are stable for sufficiently small mass ratios. The five equilibria are represented in Fig. 3.3.

We first consider the solutions to Eqs. (3.128) with $y _ { 3 } = 0$ . In this case $r _ { 1 } = | x _ { 3 } - m _ { 2 } |$ , $r _ { 2 } = | x _ { 3 } + m _ { 1 } |$ , and we must distinguish three subcases. For $L _ { 1 }$ we take the test body to be between the other two bodies, so that $- m _ { 1 } < x _ { 3 } < m _ { 2 }$ ; in this case we have that $r _ { 1 } = m _ { 2 } - x _ { 3 } , r _ { 2 } = x _ { 3 } + m _ { 1 }$ , and Eq. (3.128a) can be expressed as

$$
q = \frac { r _ { 2 } - r _ { 2 } ^ { - 2 } } { r _ { 1 } - r _ { 1 } ^ { - 2 } } , \qquad r _ { 1 } + r _ { 2 } = 1 \qquad ( L _ { 1 } ) .
$$

![](images/d89821a00732e29474fd5656fe5d83654d813bca8d8ab9ff29fcbbe764dc9bd7.jpg)  
The five Lagrange points of a restricted three-body system with mass ratio $\begin{array} { r } { q = \frac { 1 } { 2 } } \end{array}$

# Fig. 3.3

It is easy to see that a solution exists for any value of $q \leq 1$ , with $\begin{array} { r } { r _ { 1 } \le \frac { 1 } { 2 } } \end{array}$ . For example, with $\begin{array} { r } { q = \frac { 1 } { 2 } } \end{array}$ so that $\begin{array} { r } { m _ { 1 } = \frac { 1 } { 3 } } \end{array}$ and $\begin{array} { r } { m _ { 2 } = \frac { 2 } { 3 } } \end{array}$ , the solution is $x _ { 3 } \simeq 0 . 2 3 7 4 2$ . For $L _ { 2 }$ we take the test body to be beyond body 1, so that $x _ { 3 } > m _ { 2 }$ ; in this case we have that $r _ { 1 } = x _ { 3 } - m _ { 2 }$ , $r _ { 2 } = x _ { 3 } + m _ { 1 }$ , and Eq. (3.128a) can now be expressed as

$$
q = - { \frac { r _ { 2 } - r _ { 2 } ^ { - 2 } } { r _ { 1 } - r _ { 1 } ^ { - 2 } } } , \qquad r _ { 2 } - r _ { 1 } = 1 \qquad ( L _ { 2 } ) .
$$

A solution exists for any value of $q \leq 1$ with $r _ { 1 } \leq 0 . 7$ . For example, with $\begin{array} { r } { q = \frac { 1 } { 2 } } \end{array}$ the solution is $x _ { 3 } \simeq 1 . 2 4 9 0 5$ . Finally, for $L _ { 3 }$ we take the test body to be beyond body 2, so that $x _ { 3 } < - m _ { 1 }$ ; in this case we have that $r _ { 1 } = m _ { 2 } - x _ { 3 } , r _ { 2 } = - ( x _ { 3 } + m _ { 1 } )$ , and Eq. (3.128a) yields

$$
q = - { \frac { r _ { 2 } - r _ { 2 } ^ { - 2 } } { r _ { 1 } - r _ { 1 } ^ { - 2 } } } , \qquad r _ { 1 } - r _ { 2 } = 1 \qquad ( L _ { 3 } ) .
$$

A solution exists for any value of $q \leq 1$ with $1 . 7 \leq r _ { 1 } \leq 2$ . For example, with $\begin{array} { r } { q = \frac { 1 } { 2 } } \end{array}$ the solution is $x _ { 3 } \simeq - 1 . 1 3 6 3 6$ .

We next consider the solutions to Eqs. (3.128) with $y _ { 3 } \neq 0$ . It is easy to see that a simultaneous solution to these equations requires $r _ { 1 } = r _ { 2 } = 1$ , so that the configuration is an equilateral triangle. Inserting this constraint within Eq. (3.125) reveals that there are two distinct solutions described by $\begin{array} { r } { x _ { 3 } = \frac 1 2 - m _ { 1 } = m _ { 2 } - \frac 1 2 } \end{array}$ and $y _ { 3 } = \pm \frac { 1 } { 2 } \sqrt { 3 }$ ; the solution with $y _ { 3 } > 0$ is $L _ { 4 }$ , and the one with $y _ { 3 } < 0$ is $L _ { 5 }$ . For $\begin{array} { r } { q = \frac { 1 } { 2 } } \end{array}$ , $L _ { 4 }$ is situated at $x _ { 3 } = 0 . 1 6 6 6 7$ and $y _ { 3 } = 0 . 8 6 6 0 3$ , while $L _ { 5 }$ is situated at $x _ { 3 } = 0 . 1 6 6 6 7$ and $y _ { 3 } = - 0 . 8 6 6 0 3$ .

A stability analysis reveals that $L _ { 1 } , L _ { 2 }$ , and $L _ { 3 }$ are unstable equilibria: small displacements from these points produce motions that take the test body far away. The remaining Lagrange points, however, are stable provided that (refer to Exercise 3.12)

$$
q < \frac { 1 - \frac { 1 } { 9 } \sqrt { 6 9 } } { 1 + \frac { 1 } { 9 } \sqrt { 6 9 } } \simeq 0 . 0 4 ;
$$

in this case a small displacement produces a small oscillation around the equilibrium point.

In the solar system, the stable Lagrange points of the Sun–Jupiter system are occupied by large collections of asteroids. These orbit the Sun along Jupiter’s orbital path, with one group, called the “Greek” asteroids, $6 0 ^ { \circ }$ ahead of it (at $L _ { 4 }$ ), and the other group, called the “Trojan” asteroids, $6 0 ^ { \circ }$ behind it (at $L _ { 5 }$ ). The asteroids remain in those positions because they are less disturbed by planetary perturbations, being protected by the weak potential well provided by the gravitational fields of the Sun and Jupiter combined with centrifugal forces. Similarly, there is a distribution of interplanetary dust at the Earth–Sun Lagrange points, and two small moons lie at the stable Lagrange points of the system formed by Saturn and Tethys, one of its moons.

It turns out that the $L _ { 1 }$ and $L _ { 2 }$ points of the Earth–Sun system are very useful places to park a spacecraft. Even though these equilibria are unstable, the instability is weak, and a relatively small amount of thrust is sufficient to keep the spacecraft in a small orbit around the Lagrange point. For example, the Solar and Heliospheric Observatory (SOHO) was placed at $L _ { 1 }$ , pointing continuously sunward. The Wilkinson Microwave Anisotropy Probe (WMAP) and the Planck satellite were both placed at $L _ { 2 }$ , so that they could point away from the Sun and Earth. The James Webb Space Telescope (the replacement for Hubble) is also destined for $L _ { 2 }$ .

# 3.5.2 The $N$ -body problem

Very little can be said about the detailed motion of an $N$ -body system, even when the equation of motion of each body is given by the simplest expression

$$
\pmb { a } _ { A } = - \sum _ { B \neq A } G m _ { B } \frac { \pmb { r } _ { A B } } { r _ { A B } ^ { 3 } } .
$$

General statements can still be made, but they concern only the most global and coarsegrained aspects of the motion. For example, we know from Sec. 1.6.6 that the system’s total momentum, energy, and angular momentum are conserved quantities. These, we recall, are given by $\begin{array} { r } { \pmb { P } = \sum _ { \pmb { A } } m _ { A } \pmb { v } _ { A } } \end{array}$ , $E = \mathcal { T } + \Omega$ , and $\begin{array} { r } { { \cal L } = \sum _ { \cal A } m _ { \cal A } { \cal r } _ { \cal A } \times { \pmb v } _ { \cal A } } \end{array}$ , with

$$
\mathcal { T } = \frac { 1 } { 2 } \sum _ { A } m _ { A } v _ { A } ^ { 2 }
$$

denoting the total kinetic energy, and

$$
\Omega = - \frac { 1 } { 2 } \sum _ { A } \sum _ { B \ne A } \frac { G m _ { A } m _ { B } } { r _ { A B } }
$$

the total gravitational potential energy. Another global statement is the virial theorem

$$
\frac { 1 } { 2 } \frac { d ^ { 2 } I } { d t ^ { 2 } } = 2 \mathcal { T } + \Omega ,
$$

where $\begin{array} { r } { I = \sum _ { A } m _ { A } | \pmb { r } _ { A } | ^ { 2 } } \end{array}$ is the quadrupole-moment scalar of the $N$ -body system. This version of the virial theorem is a specialization to isolated bodies of the general theorem of Sec. 1.4.3, which applies to any fluid configuration. Though they are limited in information content, the global statements are nevertheless useful because they rest upon the most fundamental aspects of Newtonian dynamics. They can, actually, be very powerful at probing the nature of complicated systems. For example, the virial theorem played an important role in deducing the existence of dark matter in the universe.

The virial theorem applies when an $N$ -body system such as a star cluster can be regarded as being isolated and gravitationally bound, and it is useful when the system can also be regarded as being in a steady state, so that $\ddot { I } \approx 0$ . In such situations the theorem implies that $\begin{array} { r } { \mathcal { T } \approx \frac { 1 } { 2 } | \Omega | } \end{array}$ . The kinetic energy of the cluster can be expressed as $\scriptstyle { \frac { 1 } { 2 } } M \langle v ^ { 2 } \rangle$ , where $M$ is the total mass of the cluster, and $\langle v ^ { 2 } \rangle$ is a suitable average of $v ^ { 2 }$ over all stars in the cluster. On the other hand, the gravitational potential energy is approximately equal to $- G M ^ { 2 } / ( 2 R )$ , where $R$ is the cluster’s radius. If the distribution of velocities is assumed to be isotropic, then $\langle v ^ { 2 } \rangle \approx 3 \langle v _ { r } ^ { 2 } \rangle$ , with $v _ { r }$ denoting the component of the stellar velocity along the line of sight, which can be measured from the Doppler shift of the spectral lines (after removing the overall shift caused by the bulk motion of the cluster relative to the Earth). The radius $R$ is determined from the cluster’s angular size combined with an estimate of its distance. With these ingredients, the “virial mass” of the cluster is given by $G M _ { \mathrm { v i r i a l } } \simeq 6 R \langle v _ { r } ^ { 2 } \rangle$ , and within a factor of order unity, we should expect this to be a reliable estimate of the cluster’s total mass. The problem is that the virial mass determined in this way turns out to be as much as 10 times larger than the “visible mass” determined by measuring the brightness of the cluster and multiplying by the mass-to-light ratio known from stellar-structure theory for the kinds of stars contained in the cluster. When the virial method was applied to clusters of galaxies (with each galaxy viewed as a point body), the discrepancy between the virial and visible masses was even larger.

One proposed explanation for the discrepancy held that star clusters are really not bound at all, so that the virial theorem does not apply to them. Another possible explanation is that the clusters are not in a steady state, so that the assumption $\ddot { I } \approx 0$ is not valid. But observations of many clusters and detailed analyses have suggested that these avenues are not promising. An alternative explanation is that there is additional mass in the system that contributes to the gravitational binding, but does not emit any light – this is the dark matter hypothesis. Eventually it was shown that the amount of dark matter implied by the virial-mass discrepancy in star clusters and galaxies is consistent with the amount required to explain the rotational properties of many spiral galaxies, the angular fluctuations in the cosmic microwave background radiation, and the growth of large-scale structure in the early universe. The dark matter hypothesis has now become a central feature of the standard cosmological model.

# 3.6 Lagrangian formulation of Newtonian dynamics

Our exploration of Newtonian gravity is coming to a close, but we would be remiss if we didn’t touch upon the wonderful developments initiated by Maupertuis and Euler and completed by Lagrange and Hamilton. Their principle of least action has become a unifying principle for all of physics, being applicable to such disparate fields as mechanics, fluid dynamics, and field theory including general relativity. Our treatment here will be extremely brief; we expect the reader to have encountered this topic in greater depth elsewhere. We include it regardless because we shall have occasion to refer to Lagrangians and action functionals in later portions of the book, and wish to provide a quick reference manual to accompany these references.

# 3.6.1 Lagrangian and action principle

We consider a dynamical system with an arbitrary number of degrees of freedom. We describe the motion of the system with generalized coordinates $q ^ { j } ( t )$ , which may be chosen arbitrarily to give the simplest description; the generalized coordinates give rise to the generalized velocities ${ \dot { q } } ^ { j } ( t ) : = d q ^ { j } / d t$ . The system possesses a kinetic energy $\tau$ and a potential energy $\Omega$ which depend upon the generalized coordinates and velocities. The system’s Lagrangian function is defined to be $L ( \dot { q } ^ { j } , q ^ { j } ) : = \mathcal { T } - \Omega$ . The system’s action functional is

$$
S [ q ] : = \int _ { t _ { 1 } } ^ { t _ { 2 } } L ( \dot { q } ^ { j } , q ^ { j } ) d t ,
$$

the integral of the Lagrangian function between two fixed times. The action can be evaluated for any path $q ^ { j } ( t )$ that joins an initial configuration $q ^ { j } ( t _ { 1 } )$ to a final configuration $q ^ { j } ( t _ { 2 } )$ , whether or not this path satisfies the equations of motion of the dynamical system.

The true path of the dynamical system – the one that satisfies the equations of motion – is identified as the one that produces an extremum of the action functional. This means the following. Suppose that the true path is $\bar { q } ^ { j } ( t )$ , and that we examine an arbitrary variation of this path described by the small displacements $\delta q ^ { j } ( t )$ , thereby constructing a trial path $q _ { \mathrm { t r i a l } } ^ { j } ( t ) = \bar { q } ^ { j } ( t ) + \delta q ^ { j } ( t )$ . We insist that the trial path should begin from the same configuration as the true path, and that it should also end in the same configuration as the true path, so that the displacements must obey $\delta q ^ { j } ( t _ { 1 } ) = 0 = \delta q ^ { j } ( t _ { 2 } )$ ; apart from this the functions $\delta q ^ { j } ( t )$ are arbitrary. The action functional can be evaluated on the true path, and it can be evaluated on the trial path; it will be an extremum when the difference $\delta S : = S [ q _ { \mathrm { t r i a l } } ] - S [ \bar { q } ]$ vanishes to first order in the displacements. As we shall see, the condition $\delta S = 0$ gives us a means to identify $\bar { q } ^ { j } ( t )$ . It can be shown that when $t _ { 2 } - t _ { 1 }$ is not too large, the extremum is in fact a minimum – the action is minimized when evaluated along the true path. When $t _ { 2 } - t _ { 1 }$ increases beyond a certain threshold (called a kinetic focus), the extremum turns into a saddle point of the action functional.

To carry out the variation of the action we write

$$
\begin{array} { l } { { \delta S = S [ q _ { \mathrm { t r i a l } } ] - S [ \bar { q } ] } } \\ { { \displaystyle \quad = \int _ { t _ { 1 } } ^ { t _ { 2 } } \left[ L \big ( \dot { q } _ { \mathrm { t r i a l } } ^ { j } , q _ { \mathrm { t r i a l } } ^ { j } \big ) - L \big ( \dot { \bar { q } } ^ { j } , \bar { q } ^ { j } \big ) \right] d t } } \end{array}
$$

and express the trial Lagrangian as a Taylor expansion about the true path, obtaining

$$
L \left( \dot { \bar { q } } ^ { j } , \bar { q } ^ { j } \right) + \frac { \partial L } { \partial \dot { q } ^ { j } } \delta \dot { q } ^ { j } + \frac { \partial L } { \partial q ^ { j } } \delta q ^ { j }
$$

to first order in the displacements; summation over the repeated index $j$ is understood. The variation of the action becomes

$$
\delta S = \int _ { t _ { 1 } } ^ { t _ { 2 } } \left( { \frac { \partial L } { \partial { \dot { q } } ^ { j } } } { \frac { d } { d t } } \delta q ^ { j } + { \frac { \partial L } { \partial q ^ { j } } } \delta q ^ { j } \right) d t ,
$$

and integration by parts of the first term produces

$$
\delta S = \frac { \partial L } { \partial \dot { q } ^ { j } } \delta q ^ { j } \bigg | _ { t _ { 1 } } ^ { t _ { 2 } } + \int _ { t _ { 1 } } ^ { t _ { 2 } } \biggl ( - \frac { d } { d t } \frac { \partial L } { \partial \dot { q } ^ { j } } + \frac { \partial L } { \partial q ^ { j } } \biggr ) \delta q ^ { j } d t .
$$

The boundary terms vanish because of the conditions $\delta q ^ { j } ( t _ { 1 } ) = 0 = \delta q ^ { j } ( t _ { 2 } )$ , and since the variations $\delta q ^ { j } ( t )$ are otherwise arbitrary, we find that $\delta S = 0$ requires

$$
\frac { d } { d t } \frac { \partial L } { \partial \dot { q } ^ { j } } - \frac { \partial L } { \partial q ^ { j } } = 0 .
$$

These are the Euler–Lagrange equations for the dynamical system, which give rise to second-order differential equations for the generalized coordinates $q ^ { j } ( t )$ . The Euler– Lagrange equations, therefore, provide the equations of motion to be satisfied by the dynamical system, as dictated by the principle of extremum action.

The Euler–Lagrange equations can be written in the form

$$
\dot { p } ^ { j } = \frac { \partial L } { \partial q ^ { j } } ,
$$

in which $p ^ { j } : = \partial L / \partial \dot { q } ^ { j }$ is the generalized momentum associated with the coordinate $q ^ { j }$ . An immediate consequence of this equation is that when $L$ does not depend explicitly on one (or more) of its generalized coordinates, say $q ^ { * }$ , then the associated momentum $p ^ { * }$ is necessarily a constant of the motion. In this way, momentum conservation is seen to arise as a consequence of a symmetry of the dynamical system.

# 3.6.2 Lagrangian mechanics of a two-body system

We apply these ideas to a system of two spherical bodies moving under their mutual gravitational attraction. We follow the description of Sec. 1.6.7 and adopt the variables $\pmb { R } : = ( m _ { 1 } / m ) \pmb { r } _ { 1 } + ( m _ { 2 } / m ) \pmb { r } _ { 2 }$ and $r : = r _ { 1 } - r _ { 2 }$ as generalized coordinates; here $m : = m _ { 1 } + m _ { 2 }$ is the total mass of the system, and $\mu : = m _ { 1 } m _ { 2 } / m$ is the reduced mass. The corresponding generalized velocities are $V : = d \pmb { R } / d t$ and ${ \pmb v } = d { \pmb r } / d t$ . The kinetic energy of the system is $\begin{array} { r } { \mathcal { T } = \frac { 1 } { 2 } m V ^ { 2 } + \frac { 1 } { 2 } \mu v ^ { 2 } } \end{array}$ , and its gravitational potential energy is $\Omega = - G \mu m / r$ . The Lagrangian of the two-body system is therefore

$$
{ \cal L } = { \frac { 1 } { 2 } } m V ^ { 2 } + { \frac { 1 } { 2 } } \mu v ^ { 2 } + { \frac { G \mu m } { r } } .
$$

We see immediately that $L$ does not depend explicitly on the coordinates $\pmb { R }$ , and this implies that the corresponding momentum $P : = \partial L / \partial V = m V$ is constant; we have recovered the fact that the total momentum of a two-body system is a conserved quantity. Taking this into account, we recognize that the first term in the Lagrangian is an irrelevant constant which plays no role in the dynamics of the relative orbit. We may remove it, and take the effective Lagrangian to be

$$
L = { \frac { 1 } { 2 } } \mu v ^ { 2 } + { \frac { G \mu m } { r } } .
$$

The reduction to an effective one-body problem has been achieved at the level of the Lagrangian, instead of at the level of the equations of motion.

The gravitational potential energy $\Omega$ is spherically symmetric, and this motivates the use of spherical polar coordinates $( r , \theta , \phi )$ instead of the original Cartesian coordinates $( x , y , z )$ associated with the separation vector $r$ . The transformation, given by $x = r \sin \theta \cos \phi$ , $y = r \sin \theta \sin \phi$ , and $z = r \cos \theta$ , can implemented directly within the Lagrangian, which becomes

$$
L = { \frac { 1 } { 2 } } \mu { \left( { \dot { r } } ^ { 2 } + r ^ { 2 } { \dot { \theta } } ^ { 2 } + r ^ { 2 } \sin ^ { 2 } \theta { \dot { \phi } } ^ { 2 } \right) } + \frac { G \mu m } { r } .
$$

Another symmetry is revealed: the Lagrangian does not depend explicitly on $\phi$ , and the generalized momentum $p _ { \phi } = \partial L / \partial _ { \phi } = \mu r ^ { 2 } \sin ^ { 2 } \theta \dot { \phi }$ is a constant of the motion. Because $\phi$ is an angular coordinate, $p _ { \phi }$ has the interpretation of an angular momentum, and it is in fact the component of the angular-momentum vector $\pmb { L } = \mu \pmb { r } \times \pmb { v }$ in the $z$ -direction. Because this direction was selected arbitrarily in the definition of the spherical coordinates, we can conclude that in fact, all components of the angular-momentum vector are conserved. This statement implies that the motion takes place in a fixed orbital plane, and this plane can be identified with the equatorial plane $\begin{array} { r } { \theta = \frac { \pi } { 2 } } \end{array}$ without loss of generality.

Setting $\begin{array} { r } { \theta = \frac { \pi } { 2 } } \end{array}$ and $\dot { \theta } = 0$ in the Lagrangian, we finally obtain

$$
L = { \frac { 1 } { 2 } } \mu { \bigl ( } { \dot { r } } ^ { 2 } + r ^ { 2 } { \dot { \phi } } ^ { 2 } { \bigr ) } + { \frac { G \mu m } { r } }
$$

for the fully reduced Lagrangian that governs the planar motion of a two-body system. At this stage it is easy to show that the Euler–Lagrange equations produce the orbital equations first obtained in Sec. 3.2.3.

# 3.6.3 Lagrangian mechanics of a test mass

To conclude this brief tour of Lagrangian mechanics, we examine the dynamics of a test body in the gravitational field of other massive bodies. In this case the dynamical system consists only of the test body, which is given a mass $m$ , position $\mathbf { } r ( t )$ , and velocity $\pmb { v } ( t )$ . The gravity of the external bodies is described by their gravitational potential $U ( t , { \boldsymbol { x } } )$ , which is supposed to be known as a function of space and time. The particle’s kinetic energy is $\scriptstyle { \frac { 1 } { 2 } } m v ^ { 2 }$ , and its potential energy – its interaction energy with the remaining bodies – is $- m U ( r )$ , in which the potential is evaluated at $\mathbf { \boldsymbol { x } } = \mathbf { \boldsymbol { r } } ( t )$ . The particle’s Lagrangian is

$$
{ \cal L } = \frac { 1 } { 2 } m v ^ { 2 } + m U ( r ) .
$$

In this case the Lagrangian possesses whatever symmetry is displayed by the gravitational potential $U$ ; in general there will be no particular symmetry.

The generalized momentum associated with $r$ is $p = \partial L / \partial v = m v$ , which is recognized as the usual momentum vector. The Euler–Lagrange equations read

$$
\frac { d \pmb { p } } { d t } = m \pmb { \nabla } U ( \pmb { r } ) ,
$$

in which the potential is differentiated with respect to $r$ . The left-hand side is $\mathbf { } m \mathbf { } a = \mathbf { }$ $m d ^ { 2 } r / d t ^ { 2 }$ , and the right-hand side is recognized as the gravitational force exerted by the external bodies. We have recovered the familiar Newtonian equations of motion, $m \pmb { a } = \pmb { F }$ with $F = m \nabla U$ .

Thus ends our survey of Newtonian gravity. Now onward with relativity!

# 3.7 Bibliographical notes

Kepler’s problem (Sec. 3.2) is a staple of Newtonian mechanics, and its solution is presented in most textbooks devoted to this topic, including French (1971). More complete presentations, including the three-dimensional aspects of Keplerian orbits (as reviewed in Sec. 3.2.5), are typically found in books on celestial mechanics; among our favorites are the old classic by Brouwer and Clemence (1961) and the more modern text by Murray and Dermott (2000).

The method of osculating orbital elements developed in Sec. 3.3 is also standard fare of books on celestial mechanics; these also contain many more applications of the formalism than the few presented in Sec. 3.4. The Kozai mechanism was discovered independently by Lidov (1962) and Kozai (1962). The first measurement of the solar oblateness by Dicke and Goldenberg is presented in their 1967 article. An accessible introduction to the rich field of helioseismology can be found in Narayanan (2012). The motion of the Moon is treated in great detail in Brown (1960). A broad overview of the gravitational $N$ -body problem (Sec. 3.5), with applications to the solar system, stellar and galactic dynamics, and cosmology, is contained in the compilation of lectures edited by Steves and Maciejewski (2001).

Our presentation of Lagrangian mechanics in Sec. 3.6 does not do justice to this most elegant formulation of the laws of mechanics, and we add insult to injury by not even mentioning the Hamiltonian and Hamilton–Jacobi versions of the theory. These topics, fortunately, are thoroughly treated in many textbooks. A very terse but elegant presentation can be found in the classic Mechanics by Landau and Lifshitz (1976), and a more leisurely treatment in Goldstein, Poole, and Safko (2001).

# 3.8 Exercises

3.1 In this problem we examine the conic sections of Kepler’s problem.

(a) For an orbit with $e \neq 1$ and $\omega = 0$ , consider a coordinate transformation to new variables $\bar { x }$ and $\bar { y }$ , of the form $\bar { x } = r \cos \phi + p \alpha$ , $\bar { y } = r \sin \phi$ , where $r =$ $p / ( 1 + e \cos \phi )$ and $\alpha$ is a constant. Find the value of $\alpha$ that converts the curve to an ellipse or hyperbola, described by the equation

$$
\frac { \bar { x } ^ { 2 } } { A ^ { 2 } } \pm \frac { \bar { y } ^ { 2 } } { B ^ { 2 } } = 1 ,
$$

where the positive and negative signs correspond to an ellipse and hyperbola, respectively. Determine $A$ and $B$ in terms of the semi-latus rectum $p$ and eccentricity $e$ .

(b) For $e = 1$ , find the transformation that converts the curve into a parabola described by $\hat { x } = C \hat { y } ^ { 2 }$ . Determine $C$ in terms of $p$ .

3.2 Suppose that the solar system is filled with a uniform distribution of dark matter with constant mass density $\rho$ . Taking this distribution into account, calculate the modified gravitational potential of the Sun, and find the perturbing force $f$ acting on a planetary orbit. Find the relation between orbital period $P$ and semi-major axis $a$ for a circular orbit, and calculate the secular changes in the planet’s orbital elements. Place a bound on $\rho$ using suitable solar-system data.

3.3 In some relativistic theories of gravity, the “graviton” is not massless as in general relativity, but possesses a mass $m _ { g }$ . In the Newtonian limit, the graviton mass gives rise to a modified Poisson equation of the form

$$
\left( \nabla ^ { 2 } + { \frac { 1 } { \lambda ^ { 2 } } } \right) U = - 4 \pi G \rho ,
$$

in which $\lambda = h / ( m _ { g } c )$ is the Compton wavelength of the graviton. Show that the spherically symmetric potential of a body of mass $m$ is given by $U = ( G m / r ) e ^ { - r / \lambda }$ . Applying this to the Sun as in the preceding problem, place a bound on $\lambda$ using solar-system data.

3.4 A test body of mass $\mu$ orbits a body of mass $m$ , radius $R$ , and dimensionless quadrupole moment $J _ { 2 }$ relative to a symmetry axis $_ e$ ; all other $J _ { \ell } \mathbf { s }$ are assumed to vanish. Prove that the following quantities are constants of the orbital motion:

(a) The total energy, given by

$$
E = { \frac { 1 } { 2 } } \mu v ^ { 2 } - { \frac { G \mu m } { r } } + { \frac { 1 } { 2 } } { \frac { G \mu m J _ { 2 } R ^ { 2 } } { r ^ { 3 } } } \bigl [ 3 ( \pmb { n } \cdot \pmb { e } ) ^ { 2 } - 1 \bigr ] .
$$

(b) The angular momentum along $_ e$ , given by $L _ { e } = \mu \mathbf { h } \cdot e$ , where $\pmb { h } : = \pmb { r } \times \pmb { v }$

(c) A third quantity, constant to first order in $J _ { 2 }$ , given by

$$
C = h ^ { 2 } + J _ { 2 } R ^ { 2 } \biggl [ ( \pmb { e } \cdot \pmb { v } ) ^ { 2 } - 2 \frac { G m } { r } ( \pmb { e } \cdot \pmb { n } ) ^ { 2 } \biggr ] ,
$$

where ${ \pmb n } : = { \pmb r } / r$ . This third constant is analogous to the “Carter constant” in the Kerr geometry of a rotating black hole.

3.5 Consider a spherical body on an inclined, circular orbit about an axisymmetric body of radius $R$ and even multipole moments $J _ { \ell }$ , with $\ell = 2$ , 4, 6, and so on. To first order in perturbation theory, calculate the secular changes in the relevant orbital elements. In particular, show that:

(a) the inclination is constant, that is, $\Delta \iota = 0$ ; (b) the line of nodes changes by an amount

$$
\Delta \Omega = - 3 \pi \cos \iota \sum _ { \ell = 2 } ^ { \infty } J _ { \ell } \left( { \frac { R } { p } } \right) ^ { \ell } C _ { \ell } ,
$$

where $C _ { 2 } = 1$ , $\begin{array} { r } { C _ { 4 } = - \frac { 5 } { 2 } ( 1 - \frac { 7 } { 4 } \sin ^ { 2 } \iota ) } \end{array}$ , and $\begin{array} { r } { C _ { 6 } = \frac { 3 5 } { 8 } ( 1 - \frac { 9 } { 2 } \sin ^ { 2 } \iota + \frac { 3 3 } { 8 } \sin ^ { 4 } \iota ) } \end{array}$

3.6 The equations that govern the evolution of the osculating orbital elements have singularities when $e = 0$ and $\iota = 0$ .

(a) Show that the bad behavior of the equations when $e = 0$ can be cured by implementing the transformation $\alpha = e \cos \omega$ and $\beta = e \sin \omega$ . Obtain the osculating equations for the new elements $\alpha$ and $\beta$ .   
(b) Show that the bad behavior of the equations when $\iota = 0$ can be cured by implementing the transformation $\mu = \tan \iota \cos \Omega$ and $\nu = \tan \iota \sin \Omega$ . Obtain the osculating equations for the new elements $\mu$ and $\nu$ .

3.7 Show that the period of oscillation of the Kozai resonance is given by Eq. (3.89), and that the orbital elements $\omega , \iota$ , and $e$ vary according to

$$
\begin{array} { l } { \omega = \displaystyle \frac { \pi } { 2 } + A \sin ( 2 \pi t / P _ { \mathrm { K o z a i } } ) , } \\ { \displaystyle \phantom { \frac { A } { A } } \iota = \iota _ { c } - \displaystyle \frac { 1 } { 2 } A e _ { c } \cos ( 2 \pi t / P _ { \mathrm { K o z a i } } ) , } \\ { \displaystyle e = e _ { c } + \displaystyle \frac { 5 } { 6 } A \sin \iota _ { c } \cos \iota _ { c } \cos ( 2 \pi t / P _ { \mathrm { K o z a i } } ) , } \end{array}
$$

on a secular time scale; here $A$ is an arbitrary amplitude for the oscillations.

3.8 From the equations for $\Delta e , \Delta \omega$ , and $\Delta \iota$ in the Kozai mechanism, show that

$$
e ^ { 2 } \cos ^ { 2 } \omega \sin ^ { 2 } \iota - \frac { 3 } { 5 } e ^ { 2 } + \cos ^ { 2 } \iota = \mathrm { c o n s t a n t } .
$$

3.9 (a) Consider a two-body system on a circular orbit with separation $r$ and angular velocity $\Omega = ( G m / r ^ { 3 } ) ^ { 1 / 2 }$ , where $m = m _ { 1 } + m _ { 2 }$ is the total mass. Body 2 may be treated as a point mass, but body 1 is tidally distorted by body 2. Because of tidal dissipation in body $1 , r$ changes over one orbit by

$$
\Delta r = - 2 4 \pi ( k _ { 2 } ) _ { 1 } \frac { m _ { 2 } } { m _ { 1 } } \frac { R _ { 1 } ^ { 5 } } { r ^ { 4 } } ( \Omega - \omega _ { 1 } ) \tau _ { 1 } ,
$$

where $R _ { 1 } , \omega _ { 1 } , ( k _ { 2 } ) _ { 1 }$ , and $\tau _ { 1 }$ are the radius, rotational angular velocity, Love number, and viscous delay of body 1, respectively – refer to Eq. (3.105). Find the rate of change of orbital angular momentum, $L = \mu r ^ { 2 } \Omega$ . Comparing your result with Eq. (2.287), what can you conclude about the total angular momentum of the system, $J = L + { S _ { 1 } } ^ { \prime }$ ?

(b) The Earth–Moon distance is known to be increasing at a rate of about $3 . 8 \mathrm { c m / y r }$ . Assuming a value $k _ { 2 } \approx 0 . 1 5$ for the Love number of the Earth, estimate the angle between the Earth’s tidal bulge and the Earth–Moon direction. Does the bulge lie ahead of or behind that line?

(b) Show that when the Earth eventually becomes tidally locked with the Moon, the length of the day (and of the month) will be about 48 current days. You may ignore the rotational angular momentum of the Moon, and you may assume that to a good approximation, the moment of inertia of the Earth about its rotation axis is given by $0 . 3 3 M _ { \oplus } R _ { \oplus } ^ { 2 }$ .

3.10 Consider a point at a position $\bar { \boldsymbol { r } } ( t )$ on a circular orbit of radius $r$ around a central body of mass $m$ , orbiting with angular velocity $\Omega$ , with $\Omega ^ { 2 } = G m / r ^ { 3 }$ . Consider also a test body moving on nearby orbit, at a position $\delta { \bar { r } } ( t )$ relative to the point on the circular orbit. Assume that $\delta r \ll r$ .

(a) In a coordinate system that rotates around the central body with angular velocity $\Omega$ , show that the equations of motion of the test body are given by

$$
\frac { d ^ { 2 } } { d t ^ { 2 } } \delta \pmb { r } + 2 \pmb { \Omega } \times \frac { d } { d t } \delta \pmb { r } = \Omega ^ { 2 } \bigg [ 3 ( \pmb { n } \cdot \delta \pmb { r } ) \pmb { n } - ( \pmb { e } _ { z } \cdot \delta \pmb { r } ) \pmb { e } _ { z } \bigg ]
$$

to first order in $\delta r$ ; here $\pmb { \Omega } : = \Omega \pmb { e } _ { z }$ is the angular-velocity vector, and ${ \pmb n } : = { \pmb r } / r$

(b) Prove that the general solution to the equations of motion takes the form of the linear superposition $\delta \pmb { r } = c _ { 1 } \delta \pmb { r } _ { 1 } + c _ { 2 } \delta \pmb { r } _ { 2 } + c _ { 3 } \delta \pmb { r } _ { 3 } + c _ { 4 } \delta \pmb { r } _ { 4 }$ , where $c _ { n }$ are arbitrary constants, and

$$
\begin{array} { r l } & { \delta r _ { 1 } = \cos ( \Omega t - \chi _ { 1 } ) { \boldsymbol n } - 2 \sin ( \Omega t - \chi _ { 1 } ) \lambda , } \\ & { \delta r _ { 2 } = { \boldsymbol n } - \frac { 3 } { 2 } \Omega t \lambda , } \\ & { \delta r _ { 3 } = \lambda , } \\ & { \delta r _ { 4 } = \cos ( \Omega t - \chi _ { 4 } ) e _ { z } , } \end{array}
$$

are the four eigenmodes of the perturbed orbit; $\chi _ { n }$ are arbitrary phases.

(c) Describe the motion that corresponds to each mode, and show that each mode is generated by a perturbation in the orbital elements $( p , e , \iota , \Omega )$ relative to the unperturbed, circular orbit. Relate the constants $c _ { n }$ to the variations of the orbital elements.

(d) Find a solution with $c _ { 2 } = c _ { 3 } = 0$ , but with $c _ { 1 } \neq 0$ and $c _ { 4 } \neq 0$ , describing a relative orbit that is circular, with a constant radius $\delta r$ . What is the angle between the plane of the relative orbit and that of the original, unperturbed orbit?

(e) Now find a solution describing three satellites that are moving on the same circular relative orbit, such that initially they are placed at the vertices of an equilateral triangle. Show that as each satellite follows its orbit, the constellation maintains the shape of an equilateral triangle. This configuration was adopted for the three satellites making up the Laser Interferometer Space Antenna (LISA), a proposed space-based gravitational-wave detector.

3.11 In this problem we explore further the general three-body problem introduced in Sec. 3.5.1.

(a) Show that there exist planar solutions for which $r _ { 1 2 } = r _ { 1 3 } = r _ { 2 3 }$ (b) Show that the general bound solution for $r : = r _ { A B }$ is given by

$$
\begin{array} { c } { { r = p / ( 1 + e \cos \phi ) , } } \\ { { \displaystyle r ^ { 2 } \frac { d \phi } { d t } = ( G M p ) ^ { 1 / 2 } , } } \\ { { \displaystyle n _ { A B } = \cos ( \phi - \psi _ { A B } ) e _ { X } + \sin ( \phi - \psi _ { A B } ) e _ { Y } , } } \end{array}
$$

with an orbital period given by $P = 2 \pi a ^ { 3 / 2 } / ( G M ) ^ { 1 / 2 }$ , where $a : = p / ( 1 - e ^ { 2 } )$ and $M : = m _ { 1 } + m _ { 2 } + m _ { 3 }$ , and where the three phases $\psi _ { A B }$ differ by $\frac { \pi } { 3 }$ .

(c) Show that $a _ { A }$ , the semi-major axes of the individual orbits, are given by

$$
a _ { 1 } = \frac { ( m _ { 2 } ^ { 2 } + m _ { 2 } m _ { 3 } + m _ { 3 } ^ { 2 } ) ^ { 1 / 2 } } { M } a ,
$$

with the others obtained by suitable permutations.

3.12 Consider a small displacement $\delta \pmb { \rho }$ about the Lagrange point $L _ { 4 }$ or $L _ { 5 }$ of the restricted three body problem. Expand $\nabla \Phi$ to first order in the displacement, and include the Coriolis term in the equations of motion. Substitute $\delta \pmb { \rho } = \delta \pmb { \rho } _ { 0 } e ^ { - i p t }$ and show that the solutions for the frequency $p$ are real, and thus that the Lagrange points are stable, if and only if the mass ratio $q$ satisfies the criterion of Eq. (3.132).

3.13 Assuming that $q : = m _ { 1 } / m _ { 2 } \ll 1$ , show that the unstable Lagrange points $L _ { 1 }$ and $L _ { 2 }$ lie on either side of body 1, at a distance $d$ given by $d \simeq r ( q / 3 ) ^ { 1 / 3 }$ , where $r$ is the distance between bodies 1 and 2. Calculate $d$ for the Earth–Sun system.

The preceding chapters were devoted to a Newtonian description of the gravitational interaction, and it is now time to embark on an exploration of its relativistic aspects. As we shall argue in the next chapter, a relativistic theory of gravity that respects the principle of equivalence reviewed in Sec. 1.2 must be a metric theory in which gravitation is a manifestation of the curvature of spacetime. The simplest metric theory of gravitation is Einstein’s general relativity, and our task in this chapter and the next is to introduce its essential elements. Subsequent chapters will develop the weak-field limit of general relativity, and in these chapters we will return to notions (such as gravitational potentials and forces) that are familiar from Newtonian physics. But a proper grounding of the weak-field limit must rest on the exact theory, and we shall now work to acquire the required knowledge. It is, of course, unlikely that a mere two chapters will suffice to introduce all relevant aspects of general relativity. What we intend to cover here is a rather minimal package, the smallest required for the development of the weak-field limit.

This chapter is devoted to a description of physics in Minkowski spacetime (also known as flat spacetime), which codifies in a particularly elegant way the kinematical rules of special relativity. We begin in Sec. 4.1 with a description of spacetime itself, and we next present the (flat) spacetime formulation of some familiar laws of physics: In Sec. 4.2 we examine the special-relativistic formulation of hydrodynamics, in Sec. 4.3 we turn to electrodynamics, and in Sec. 4.4 we consider the dynamics of point particles. These spacetime formulations of the laws of physics exclude gravitation, and the inclusion of this important interaction can only be achieved by modifying the very structure of spacetime (from flat to curved); this is the topic of Chapter 5.

# 4.1 Spacetime

# 4.1.1 Lorentz transformation and spacetime

Einstein was the first to realize that a kinematical transformation between a reference frame $S$ (believed to be “at rest”) and another reference frame $S ^ { \prime }$ (moving with a uniform speed $v$ relative to $S$ ) must be given by

$$
t ^ { \prime } = \gamma ( t - v x / c ^ { 2 } ) , \qquad x ^ { \prime } = \gamma ( x - v t ) , \qquad y ^ { \prime } = y , \qquad z ^ { \prime } = z ,
$$

where

$$
\gamma : = { \frac { 1 } { \sqrt { 1 - ( v / c ) ^ { 2 } } } } ,
$$

if it is to observe the two fundamental axioms of relativistic physics. These are that the laws of physics must take the same form in all inertial frames, and that the speed of light $c$ must be the same in all inertial frames. Einstein’s inertial frame was the same as Galileo’s: a frame in which a body freed from the action of external forces moves uniformly on a straight line. An inertial frame is a significant extrapolation from what we observe in nature, where bodies tend to slow down because of friction, and move on curved paths because of gravity. The first observation does not introduce an essential difficulty, because one can imagine reducing friction to negligible levels by various tricks (think of air hockey tables). But gravity is another matter, and Einstein soon realized that it would necessitate a radical rethinking of inertial frames and the nature of spacetime. We shall come to this in due course, but for the time being we restrict our attention to such ideal inertial frames, in the absence of gravity.

The transformation of Eq. (4.1) is known as a Lorentz transformation. It was first identified by Lorentz and Poincare to give rise to an invariance of Maxwell’s equations relative to ´ a choice of inertial frame, and then recognized to have universal validity and to apply to actual measurements of space and time by Einstein. In Eq. (4.1) it was assumed that $S ^ { \prime }$ moves with respect to $S$ in the $x$ -direction; it is straightforward to generalize the Lorentz transformation to arbitrary translational directions (see Exercise 4.1).

The Lorentz transformations have a direct impact on the very structure of space and time, and they suggest the merging of each notion into a unified spacetime. To begin this discussion, let us define an event as any recognizable phenomenon that occurs at a specific position in space and at a specific moment in time as measured by a clock at that position; in a frame $S$ an event is labeled by the three spatial coordinates $x , y$ , and $z$ , as well as a time coordinate $t$ . Suppose that two events occur at different places but at the same time when observed in the frame $S$ . These events are separated by a displacement $\Delta x$ , and they are such that $\Delta t = 0$ . When observed in $S ^ { \prime }$ , however, we have that $\Delta x ^ { \prime } = \gamma \Delta x$ and $\Delta t ^ { \prime } = - \gamma v \Delta x / c ^ { 2 } \neq 0$ ; the events are no longer simultaneous, and their spatial separation differs from $\Delta x$ by a factor of $\gamma$ . As another example, consider two other events that are seen in $S$ to occur at the same spatial position (so that $\Delta x = 0$ ), but at two different times separated by the interval $\Delta t$ . When observed in $S ^ { \prime }$ we find that $\Delta x ^ { \prime } = - \gamma v \Delta t \neq 0$ and $\Delta t ^ { \prime } = \gamma \Delta t$ ; the events are no longer in the same spatial position, and their separation in time differs from $\Delta t$ by a factor of $\gamma$ .

The message of the Lorentz transformations is that space by itself is not absolute (as it is in Newtonian mechanics), and time by itself also is not absolute. There is, nevertheless, a union of space and time – spacetime – that can be considered to be absolute. This comes about because the Lorentz transformation preserves the quadratic form $\Delta s ^ { 2 } : =$ $- ( c \Delta t ) ^ { 2 } + ( \Delta x ) ^ { 2 } + ( \Delta y ) ^ { 2 } + ( \Delta z ) ^ { 2 }$ , which takes on the same value whether evaluated in $S$ (as shown here), or evaluated in $S ^ { \prime }$ (by replacing all unprimed quantities with their primed version). This is conveniently written in the differential form

$$
d s ^ { 2 } = - ( c d t ) ^ { 2 } + d x ^ { 2 } + d y ^ { 2 } + d z ^ { 2 } ,
$$

and $\Delta s ^ { 2 }$ or $d s ^ { 2 }$ gives us an absolute, or Lorentz-invariant, notion of (squared) distance between two events in spacetime. We shall refer to $\Delta s ^ { 2 }$ or $d s ^ { 2 }$ as the spacetime interval. Two inertial observers, one attached to $S$ and another attached to $S ^ { \prime }$ , will measure the same value of $\Delta s ^ { 2 }$ for the spacetime interval between two selected events.

Note that $\Delta s ^ { 2 }$ can be either positive, negative, or zero. When two events are seen in $S$ to be mostly separated in time, so that $( c \Delta t ) ^ { 2 } > ( \Delta x ) ^ { 2 }$ , then $\Delta s ^ { 2 } < 0$ , and this conclusion is shared by any other inertial observer. Such events are said to have a timelike separation. There exists, in fact, a frame $S ^ { \prime }$ in which $\Delta x ^ { \prime } = 0$ , so that $\Delta s ^ { 2 } = - ( c \Delta t ^ { \prime } ) ^ { 2 }$ . In this frame, $\Delta t ^ { \prime }$ is the interval of time between two events at the same spatial position, as measured by a clock that sits at that position, and we define this to be the proper time interval $\Delta \tau : = \Delta t ^ { \prime } = c ^ { - 1 } ( - \Delta s ^ { 2 } ) ^ { 1 / 2 }$ between the two events. It has the same value in any inertial frame.

When, on the other hand, two events are seen in $S$ to be mostly separated in space, so that $( c \Delta t ) ^ { 2 } < ( \Delta x ) ^ { 2 }$ , then $\Delta s ^ { 2 } > 0$ , and this conclusion also is shared by any other inertial observer. Such events have a spacelike separation. There exists a frame $S ^ { \prime }$ in which $\Delta t ^ { \prime } = 0$ , so that $\Delta s ^ { 2 } = ( \Delta x ^ { \prime } ) ^ { 2 }$ . In this case $\Delta x ^ { \prime }$ gives the displacement between two simultaneous events, and this defines the proper distance $\Delta \ell : = \Delta x ^ { \prime } = ( \Delta s ^ { 2 } ) ^ { 1 / 2 }$ between the two events. This also is a Lorentz invariant.

When, finally, two events are linked by a signal propagating at the speed of light, so that $\Delta x = c \Delta t$ , then $\Delta s ^ { 2 } = 0$ ; the spacetime interval can be zero even when the events are widely separated both in time and in space. Such separations are called null, or lightlike. No Lorentz transformation can make two null-separated events occur simultaneously or at the same spatial position.

<table><tr><td>Box 4.1</td><td>Tests of special relativity</td></tr><tr><td></td><td>Special relativity,the physics built on Minkowski spacetime, has been so thoroughly integrated into the fabric of modern physics that its validity is rarelychallenged, except by cranksand crackpots.But we should remem- ber that it does rest on a strong empirical foundation, including some classc tests. In addition to the famous Michelson-Morley experiment, which failed to find evidence of a variation of the speed of light with the Earth&#x27;s velocity through aputative &quot;aether&quot; several clasic experiments have been performed to verify that the speed oflight is independent of the speed of the emiter. If the speed of light were given by c + kv,where v is the velocity of the emitter, and k is a parameter to be measured, then orbits of binary-star systems would appear to have an anomalous eccentricity unexplainable by normal New- tonian gravity.This test is not unambiguous at optical wavelengths, however,because light is absorbed and re-emitted by the intervening interstellar medium,thereby losing the memory ofthe speed ofthe source; this phenomenon is known to astronomers as extinction.Butat X-ray wavelengths,the path length of extinction is tens of kiloparsecs,so nearby X-ray binary systems in our galaxy may be used to test the velocity dependence</td></tr></table>

At the other extreme, a 1964 experiment at CERN used ultrarelativistic neutral pions moving at $v / c \geq$ 0.99975 as the source of light. Photons produced by the decay $\pi ^ { 0 }  \gamma + \gamma$ were collimated and timed over a flight path of 30 meters. The result for the speed was $2 . 9 9 7 7 \pm 0 . 0 0 0 4 \times 1 0 ^ { 8 } { \mathrm { m / s e c } } ,$ in agreement with the laboratory value. This experiment thus set a bound $| k | < 1 0 ^ { - 4 }$ for $v \approx c$ .

The observational evidence for time dilation is overwhelming. In the 1930s, Ives and Stilwell measured the frequency shifts of radiation emitted in the forward and backward direction by moving ions of $\mathsf { H } _ { 2 }$ and ${ \sf H } _ { 3 }$ molecules. The first-order Doppler shift cancels out from the sum of the forward and backward shifts, revealing the second-order time-dilation effect, which was found to agree with theory. (Ironically, Ives was a die-hard opponent of special relativity.)

A classic experiment published by Rossi and Hall in 1941 showed that the lifetime of $\mu$ -mesons was prolonged by the Lorentz factor $\gamma = ( 1 - v ^ { 2 } / c ^ { 2 } ) ^ { - 1 / 2 }$ . Muons are created in the upper atmosphere when cosmic-ray protons collide with nuclei of air, producing pions, which decay quickly to muons. With a rest halflife of $2 . 2 \times 1 0 ^ { - 6 } \mathsf { s } ,$ a muon travelling near the speed of light should travel only 2/3 of a kilometer on average before decaying to a harmless electron or positron and two neutrinos. Yet muons are the primary component of cosmic rays detected at sea level. With time dilation and a typical speed of $v / c \sim 0 . 9 9 4 ,$ their lives as seen from Earth are prolonged by a factor of nine, enough for them to reach sea level. Rossi and Hall measured the distribution of muons as a function of altitude and also measured their energies, and confirmed the time-dilation formula. In fact, since collisions between cosmic-ray muons and DNA molecules are a non-negligible source of natural genetic mutations, one could argue that special relativity plays a role in evolution!

In an experiment performed in 1966 at CERN, muons produced by collisions at one of the targets in the accelerator were deflected by magnets so that they would move on circular paths in a storage ring. Their speeds were 99.7 percent of the velocity of light, and the observed twelve-fold increase in their lifetimes agreed with the prediction with 2 percent accuracy. Also, since the storage ring was 5 meters in diameter, the muons’ accelerations were greater than the gravitational acceleration on the Earth’s surface by a factor of $1 0 ^ { 1 9 }$ ; these accelerations had no effect on their decay rates.

The incorporation of Lorentz invariance into quantum mechanics provided further support for special relativity. The first attempt at integration was the discovery of the Dirac equation, the relativistic generalization of Schrodinger’s equation, with its prediction of anti-particles and elementary particle spin. Complete inte- ¨ gration came with the development of relativistic quantum field theory, which naturally embodies the Pauli exclusion principle by demanding that the creation and annihilation operators of spinor fields satisfy anticommutation relations in order to satisfy Lorentz invariance. Because the Pauli exclusion principle explains the occupation of atomic energy levels by electrons, one could argue, with but a hint of chauvinism, that special relativity explains Chemistry! The modern incarnations of quantum field theory, such as Quantum Electrodynamics, Electroweak Theory, Quantum Chromodynamics, and String Theory, all have Lorentz invariance as foundations.

# 4.1.2 Metric tensor

It is convenient to combine the spatial coordinates $( x , y , z )$ and the time $t$ that label a spacetime event into a unified spacetime coordinate $x ^ { \alpha } = ( c t , x , y , z )$ . The Greek index $\alpha$ , and all other Greek indices that appear below, run over the values $\{ 0 , 1 , 2 , 3 \}$ ; we choose $x ^ { 0 } = c t$ to represent time (rescaled by a factor of $c$ so that all coordinates have dimensions of length), and $x ^ { 1 } = x , x ^ { 2 } = y , x ^ { 3 } = z$ to represent the spatial coordinates. We shall often represent the spatial coordinates as the three-dimensional vector $\boldsymbol { x }$ with components $x ^ { j }$ ; the Latin index $j$ (and all others like it) run over the values $\{ 1 , 2 , 3 \}$ .

In this notation Eq. (4.3) can be expressed as

$$
d s ^ { 2 } = \eta _ { \alpha \beta } d x ^ { \alpha } d x ^ { \beta } ,
$$

where $\eta _ { \alpha \beta }$ is a diagonal matrix with entries $\eta _ { 0 0 } = - 1$ , $\eta _ { 1 1 } = \eta _ { 2 2 } = \eta _ { 3 3 } = 1$ , and where (according to the Einstein summation convention introduced in Sec. 1.4.4) all repeated indices are summed over. The matrix has the purpose of converting coordinate intervals $d x ^ { \alpha }$ , which are affected by a change of reference frame, to the spacetime interval $d s ^ { 2 }$ , which is a Lorentz invariant; it is called the metric tensor of Minkowski spacetime. Below we shall distinguish very clearly between vectors and tensors (such as $d x ^ { \alpha }$ ) that are affected by a coordinate transformation, and scalar quantities (such as $d s ^ { 2 }$ ) that are spacetime invariants.

Equation (4.4) possesses the irresistible interpretation of expressing the inner product between the spacetime vector $d x ^ { \alpha }$ with itself. We shall adopt this geometric point of view, and use the metric $\eta _ { \alpha \beta }$ to define the inner product between any two vectors. If $A ^ { \alpha }$ is a spacetime vector (an object that transforms as the coordinate increments $d x ^ { \alpha }$ under a Lorentz transformation) and $B ^ { \alpha }$ is another, then by definition $\eta _ { \alpha \beta } A ^ { \alpha } B ^ { \beta }$ shall be their inner product; it may be verified that the inner product between two vectors is a Lorentz invariant. The inner product of a vector with itself, $\eta _ { \alpha \beta } A ^ { \alpha } A ^ { \beta }$ , is called the norm of the vector. Keep in mind that in Minkowski spacetime, norms are not necessarily positive: the norm of a timelike vector is always negative, and the norm of a lightlike vector is always zero.

We shall also use the Minkowski metric to raise and lower indices. Given a vector $A ^ { \alpha }$ , we define an associated quantity $A _ { \alpha }$ (known as a dual vector) by the operation

$$
{ \cal A } _ { \alpha } = \eta _ { \alpha \beta } { \cal A } ^ { \beta } .
$$

This operation is called “lowering the index,” and it produces $A _ { 0 } = - A ^ { 0 }$ , $A _ { 1 } = A ^ { 1 }$ , $A _ { 2 } =$ $A ^ { 2 }$ , and $A _ { 3 } = A ^ { 3 }$ . The operation can be inverted if we introduce the inverse Minkowski metric $\eta ^ { \alpha \beta }$ , a diagonal matrix with entries $\eta ^ { 0 0 } = - 1$ and $\eta ^ { 1 1 } = \eta ^ { 2 2 } = \eta ^ { 3 3 } = 1 .$ . The inverse metric is defined by the statement

$$
\eta ^ { \alpha \mu } \eta _ { \mu \beta } = \delta _ { \beta } ^ { \alpha } ,
$$

which is equivalent to the matrix equation $\eta ^ { - 1 } \eta = 1$ . The inverse operation is

$$
A ^ { \alpha } = \eta ^ { \alpha \beta } A _ { \beta } ,
$$

and it is called “raising the index.”

# 4.1.3 Kinematics of particles

The laws of physics must be formulated in spacetime. We begin this reformulation with an examination of the motion of particles. In Newtonian mechanics the motion of a particle is described mathematically by equations of the type $\mathbf { \boldsymbol { x } } = \mathbf { \boldsymbol { r } } ( t )$ , which assign to the particle, at any time $t$ , the position determined by the vectorial function $\mathbf { } r ( t )$ . This gives rise to a parameterized curve in three-dimensional space, and absolute time $t$ assumes the role of the parameter.

In spacetime we promote $t$ to one of the coordinates, and resist the temptation of using it also as a parameter. Instead we look for a description of the motion of the general form $x ^ { \alpha } = r ^ { \alpha } ( \lambda )$ , which assigns, for any value of the parameter $\lambda$ , the spacetime coordinates determined by the functions $r ^ { \alpha } ( \lambda )$ . We wish the parameter $\lambda$ to be a Lorentz invariant, and for this we select proper time $\tau$ , the time as measured by a standard clock that is attached to the moving particle. This is a spacetime invariant because any inertial observer will agree, irrespective of her own motion, that a clock moving with the particle marks time at precisely the rate measured by this particular clock; she will not, of course, claim that her own clock marks time at this rate. The trajectory of the particle in spacetime, therefore, will be described by the parametric equations $x ^ { \alpha } = r ^ { \alpha } ( \tau )$ , with proper time $\tau$ assuming the role of the parameter; the trajectory is known as the particle’s world line in spacetime.

The invariant $d \tau$ can be related to the spacetime interval $d s ^ { 2 }$ evaluated for two neighboring points on the world line. A central aspect of physics in flat spacetime is the statement, well supported by empirical evidence, that the rate at which a standard clock marks time may depend on its velocity, but it does not depend on its acceleration. The clock attached to the particle, therefore, marks time at precisely the same rate as a clock carried by an inertial observer, provided that the observer’s velocity matches the particle’s velocity when the measurement is carried out. To be sure, the velocities will be matched only momentarily if the particle is accelerated, but at that time the particle will be at rest relative to the observer. And at this moment, the two clocks will mark time at precisely the same rate. The observer’s inertial frame will be referred to as the particle’s momentarily comoving Lorentz frame, or MCLF. It is a most useful notion, and we will invoke it repeatedly to simplify subtle arguments.

As we have said, the particle is momentarily at rest in the comoving frame, and in this frame $S ^ { \prime }$ , proper time $\tau$ advances at the same rate as observer time $t ^ { \prime }$ ; we have $d \tau = d t ^ { \prime }$ . We also have that the (absent) spatial motion of the particle is described by $d x ^ { \prime } = d y ^ { \prime } = d z ^ { \prime } = 0$ in the comoving frame. The spacetime interval along the world line is therefore $d s ^ { 2 } = - ( c d t ^ { \prime } ) ^ { 2 } = - ( c d \tau ) ^ { 2 }$ . Because each side of the equation is a Lorentz invariant, we conclude that the relation

$$
d \tau = c ^ { - 1 } \sqrt { - d s ^ { 2 } }
$$

is valid in any reference frame. Proper time, therefore, measures the accumulation of spacetime interval along the particle’s world line.

Having selected proper time as a natural parameter on the world line, we define the particle’s velocity vector as

$$
u ^ { \alpha } = \frac { d r ^ { \alpha } } { d \tau } .
$$

Notice that this is a spacetime vector, with four components. Notice also that $u ^ { \alpha }$ , like $d r ^ { \alpha } =$ $d x ^ { \alpha }$ , does indeed transform as a vector under Lorentz transformations. The spacetime velocity vector can be related to ${ \pmb v } = d { \pmb r } / d t$ , the three-dimensional velocity vector of