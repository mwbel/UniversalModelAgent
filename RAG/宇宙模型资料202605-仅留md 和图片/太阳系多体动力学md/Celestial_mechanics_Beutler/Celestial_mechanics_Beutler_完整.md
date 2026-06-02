<!-- source: Celestial_mechanics_Beutler.pdf -->

<!-- pdf_type: normal; pages: 80; chunk_pages: 70 -->


<!-- chunk 0001: pages 1-70 -->
# Localisation précise par moyens spatiaux

# Astrodynamics: the bare necessities

Gerhard Beutler

# Astrodynamics

According to the Encyclopedia of Astronomy and Astrophysics Astrodynamics means the study of the motion of bodies in gravitational fields，with particular reference to the motions ot artificial satelites and space probes.

Astrodynamics thus deals with the motion of - Point masses (minor planets, comets, natural and artifical satellites) - Extended celestial bodies (planets, natural satelites (moons)).

Astrodynamics in the broadest sense also deals with the rotational motion (e.g., of planets).

This lecture is based on the two-volume monograph

G.Beutler: Methods of Celestial Mechanics:

Vol 1: Physical, mathematical,and Numerical Principles,

Vol Il: Application to Planetary System, geodynamics, and Satellite Geodesy

Springer-Verlag 2005

# Astrodynamics

The focus of this lecture uniquely is on the orbital motion of point masses orbiting around the Sun or the Earth as primary gravitational attractors.

The illustrations were

either generated with MatLab or   
or extracted from Beutler (2005).   
or generated with CelMech, a menu-driven program system,which allows it, e.g., to numerically integrate the planetary system or to solve the equation of motion of artificial Earth satellites.

CelMech consists of eight eight programs and has a very useful helpsystem.

# Table of Contents

1.The equations of motion (Vol.1, Chapter 3)

Planetary system Artificial Earth satellites

2. Orbit parameterization (Vol.1, Chapter 4)

Kepler elements   
Orbital coordinate system   
Transformation orbital system quasi-IS

3． Perturbation equations (Vol. 1, Chapter 6)

Principles   
Perturbation equations in rectangular coordinates   
Perturbation equations in Keplerian elements: Gaussian version of   
equations of motion of motion

4． Perturbing forces acting on an artificial Earth satelite (Vol Il, Chapter 3)

AM(V) Angular momentum (vector)   
CB(s) Celestial bodies   
CM Celestial Mechanics   
CoM Center of mass   
CS (Cartesian) Coordinate System   
EQ(s) Equations   
DEQ(s) Differential Equation (system)   
IGS International GNSS Service   
IS Inertial System   
JD Julian Date   
LEO Low Earth Orbiter   
LHS Left-hand side (of an EQ)   
MJD Modified Julian Date   
MP Minor planet

# Abbreviations

<table><tr><td>n-g IS LEO LHS NEQs RHS</td><td>non-gravitational Inertial System Low Earth Orbiter Left-hand side (of an EQ) Normal EQuation System</td></tr></table>

# Equations of Motion: Planetary System

For our purpose it is sufficient to say that an inertial system (lS) consists of a time scale and a Cartesian coordinate system in the three-dimensional Euclidian space E3.We assume the system to be rigidly attached to the rest system of quasars.

Celestial Mechanics (CM) of the planetary system uses TDB, barycentric dynamic time,which is derived from atomic time throuah:

TDB = TT + 0.001658 sin g +0.000014 sin 2g where g= 357.53+0.9856003 (JD-2451545) and TT is the terrestrial time,which in turn follows from TAl.We use the ecliptical system J20o0.0, defined through the mean Earth equator and the mean ecliptic of January 1, 2000, $0 ^ { \mathfrak { h } }$ TBD. In the planetary system we will uniquely take into account Newton's law of universal gravitation specifying the attractive force between point masses m and M at a distance $r$ (e is the unit vector between m and $M _ { ☉ }$ ：

$$
\pmb { f } = \pmb { G } \frac { m M } { r ^ { 2 } } \pmb { e }
$$

# Equations of Motion: Planetary System

![](images/0e9c568cbdf5e7f7f0f3e276d96f3e29dcccd840a82e961127fbb26a9fd89f86.jpg)

The trajectory of the point mass m is known, if its position vector x(t) is known in the IS as a function of time t.

# Equations of Motion: Planetary System

![](images/449b872e3b3a7938cb2987d9ff1e2039ef747f879438357d74090ac5f48aa3fe.jpg)

When dealing with celestial bodies of finite dimensions the position vector $\pmb { x } ( \mathbf { t } )$ of the body's center of mass and its attitude w.r.t. the IS have to be known.

This implies that a body-fixed reference frame has to be known at each epoch t.

# Equations of Motion: Planetary System

The EQs of motion of the planetary system are those of the N-body problem:

$$
\frac { d \left( m _ { i } \dot { \pmb x } _ { i } \right) } { d t } = - k ^ { 2 } m _ { i } \sum _ { j = 0 , j \not = i } ^ { n } m _ { j } \ \frac { { \pmb x } _ { i } - { \pmb x } _ { j } } { | { \pmb x } _ { i } - { \pmb x } _ { j } | ^ { 3 } } , \quad i = 0 , 1 , 2 , . . .
$$

Dividing this EQbv m: we obtain:

$$
\ddot { \pmb { x } } _ { i } = - k ^ { 2 } \sum _ { j = 0 , j \neq i } ^ { n } m _ { j } \ \frac { \pmb { x } _ { i } - \pmb { x } _ { j } } { | \pmb { x } _ { i } - \pmb { x } _ { j } | ^ { 3 } } \ , \quad i = 0 , 1 , 2 , \ldots , n
$$

Subtracting from the above Eqs for $I \neq O$ the equation for the central body (Sun) with $i { = } 0$ we obtain the heliocentric equations of motion:

$$
\vdots _ { i } = - k ^ { 2 } ( m _ { 0 } + m _ { i } ) \frac { r _ { i } } { r _ { i } ^ { 3 } } - k ^ { 2 } \sum _ { j = 1 , j \neq i } ^ { n } m _ { j } \left\{ \frac { r _ { i } - r _ { j } } { | r _ { i } - r _ { j } | ^ { 3 } } + \frac { r _ { j } } { r _ { j } ^ { 3 } } \right\}
$$

The first term on the r.h.s. is the two-body term: The second is the perturbation term.Excluding close encounters $i { = } 1 , 2 , \ldots , n$ and assuming that the masses maresignificantlysmaller than the mass. $m _ { a }$ of the central body,the absolute value of the perturbation term is Significantly smaller than that of the two-body term,aswell.

# Equations of Motion: Planetary System

The planetary system, consisting of the Sun, the planets, the moons of the planets,minor planets,comets,with all in all $N = n + 1$ celestial bodies,is mathematically described by a system of ordinary differential equations (DEQs) of second order and $3 . n$ (scalar) equations.

If the initial state vectors of all CBs (position- and velocity- vectors of all CBs) are known, the DEQs can be solved, e.g., with the methods of numerical analysis.

Minor planets and comets usually are assumed to have negligible masses. Their EQs of motion therefore may be solved separately from the EQs of motion of the CBs with finite masses. The corresponding DEQs,where the $m _ { j }$ und die $r _ { j }$ may be assumed as known, read as:

$$
\ddot { r } = - k ^ { 2 } m _ { 0 } \ \frac { r } { r ^ { 3 } } \ - \ k ^ { 2 } \sum _ { j = 1 } ^ { n } m _ { j } \left\{ \frac { r - r _ { j } } { \vert r - r _ { j } \vert ^ { 3 } } + \frac { r _ { j } } { r _ { j } ^ { 3 } } \right\}
$$

# Equations of Motion: Planetary System

The RHS of the EQs of motion of the planetary system may be written as gradients of (scalar) potentials:

$$
\pmb { \ddot { r } } _ { i } = \nabla _ { i } \left\{ U _ { i } + R _ { i } \right\} , \quad i = 1 , 2 , \ldots , n
$$

$$
U _ { i } = \frac { k ^ { 2 } \left( m _ { 0 } + m _ { i } \right) } { r _ { i } }
$$

$$
R _ { i } = k ^ { 2 } \sum _ { j = 1 , j \neq i } ^ { n } m _ { j } \left\{ \frac { 1 } { | { \pmb r } _ { i } - { \pmb r } _ { j } | } - \frac { { \pmb r } _ { i } { \pmb r } _ { j } } { r _ { j } ^ { 3 } } \right\}
$$

irst Integrals: Ten functions of the position and velocity vectors are constant (time independent). Six are due to the fact that the center of mass (CoM) of the planetary system moves with constant velocity on a straight line in each IS. One function exploits the fact that the total energy of the system is constant. Three functions express the preservatior of the total angular momentum.

# Equations of Motion: Planetary System

Votion of the CoM: The CoM of a system of point masses is defined as:

$$
X _ { 0 } \ { \stackrel { \mathrm { d e f } } { = } } \ { \frac { 1 } { M } } \sum _ { i = 0 } ^ { n } m _ { i } \ x _ { i }
$$

From the EQs of motion we obtain directly:

$$
{ \frac { 1 } { M } } \sum _ { i = 0 } ^ { n } m _ { i } \ { \ddot { \pmb { x } } } _ { i } = { \ddot { \pmb { X } } } _ { 0 } = \mathbf { 0 }
$$

Integrating this EQ twice in time we obtain:

$$
X _ { 0 } ( t ) = X _ { 0 0 } + V _ { 0 0 } ( t - t _ { 0 } )
$$

where the two vectors on the RHS may be interpreted as the (time-independent position- and velocity-vectors) of the CoM of the planetary system.

# Equations of Motion: Planetary System

Preservation of angular momentum (AM): AM is defined by:

$$
h \ { \stackrel { \mathrm { d e f } } { = } } \ \sum _ { i = 0 } ^ { n } m _ { i } \ x _ { i } \times { \dot { \pmb x } } _ { i }
$$

We multiply EQ of motion i with $m _ { i }$ ， multiply by $x _ { i } x$ (cross product) and sum over all CB:

$$
\sum _ { i = 0 } ^ { n } m _ { i } \ { \pmb x } _ { i } \times { \ddot { \pmb x } } _ { i } \qquad = - k ^ { 2 } \sum _ { i = 0 } ^ { n } \sum _ { j = 1 , j \neq i } ^ { n } m _ { i } \ m _ { j } \ { \frac { { \pmb x } _ { i } \times ( { \pmb x } _ { i } - { \pmb x } _ { j } ) } { | { \pmb x } _ { i } - { \pmb x } _ { j } | ^ { 3 } } }
$$

$$
{ \frac { d } { d t } } \left[ \sum _ { i = 0 } ^ { n } m _ { i } \ \mathbf { x } _ { i } \times { \dot { \mathbf { x } } } _ { i } \right] = k ^ { 2 } \sum _ { i = 0 } ^ { n } \sum _ { j = 0 , j \neq i } ^ { n } m _ { i } \ m _ { j } \ { \frac { \mathbf { x } _ { i } \times \mathbf { x } _ { j } } { | \mathbf { x } _ { i } - \mathbf { x } _ { j } | ^ { 3 } } } = \mathbf { 0 } \ .
$$

The preservation of the AM vector follows by integration over time t.

# Equations of Motion: Planetary System

Preservation of Energy: The energy is defined by:

$$
E = T - U \ ,
$$

$$
T = { \textstyle { \frac { 1 } { 2 } } } \sum _ { i = 0 } ^ { n } m _ { i } \ { \dot { x } } _ { i } ^ { 2 }
$$

$$
U = k ^ { 2 } \sum _ { i = 0 } ^ { n } \sum _ { j = i + 1 } ^ { n } { \frac { m _ { i } m _ { j } } { | r _ { i } - r _ { j } | } }
$$

Energy_preservation follows by multiplication of EQ iby $m _ { i } \pmb { X } _ { i }$ and by subsequent summation over i:

$$
\begin{array} { r l r l } { \displaystyle \sum _ { i = 0 } ^ { n } m _ { i } \ \dot { \mathbf { x } } _ { i } \cdot \ddot { \mathbf { x } } _ { i } } & { } & & { = - k ^ { 2 } \displaystyle \sum _ { i = 0 } ^ { n } \displaystyle \sum _ { j = 1 , j \neq i } ^ { n } m _ { i } m _ { j } \ \frac { \dot { \mathbf { x } } _ { i } \cdot ( \mathbf { x } _ { i } - \mathbf { x } _ { j } ) } { | \mathbf { x } _ { i } - \mathbf { x } _ { j } | ^ { 3 } } } \\ & { } & & { = - k ^ { 2 } \displaystyle \sum _ { j = 0 } ^ { n } \displaystyle \sum _ { i = 0 , i \neq j } ^ { n } m _ { i } m _ { j } \ \frac { \dot { \mathbf { x } } _ { j } \cdot ( \mathbf { x } _ { j } - \mathbf { x } _ { i } ) } { | \mathbf { x } _ { i } - \mathbf { x } _ { j } | ^ { 3 } } } \\ & { } & & { = - \frac { 1 } { 2 } k ^ { 2 } \displaystyle \sum _ { i = 0 } ^ { n } \displaystyle \sum _ { j = 1 , j \neq i } ^ { n } m _ { i } m _ { j } \ \frac { ( \dot { \mathbf { x } } _ { i } - \dot { \mathbf { x } } _ { j } ) \cdot ( \mathbf { x } _ { i } - \mathbf { x } _ { j } ) } { | \mathbf { x } _ { i } - \mathbf { x } _ { j } | ^ { 3 } } } \end{array}
$$

# Equations of Motion: Planetary System

The preservation of the AMV allows it to define a CS well suited for studying the dynamics of the PS. Its fundamental plane is heliocentric and perpendicular to the AMV. (The fundamental plane of a CS is the plane defined by its first two coordinate axes).

The heliocentric plane perpendicular to the AMV is called the invariable plane or Laplace plane (in honor of Pierre Simon de Laplace 1749-1827).

Its Euler angles w.r.t. J2000.0 are1 $i = 1 . 5 8 ^ { o }$ ， $\mathcal { Q } = 1 0 7 . 6 ^ { o }$

With the exception of the inner- and outermost planets, the inclination angles of the planetary orbits are small w.r.t. the Laplace plane.

Table 4.1. Properties of the planetary system   

<table><tr><td>Planet</td><td>Axis a [AU]</td><td>Ecc.e</td><td>Period P [Years]</td><td>Mass m -1 [m11</td><td>Incl. i [deg]</td></tr><tr><td>Mercury</td><td>0.39</td><td>0.206</td><td>0.24</td><td>6023600.00</td><td>7.0</td></tr><tr><td>Venus</td><td>0.72</td><td>0.007</td><td>0.62</td><td>408523.50</td><td>3.4</td></tr><tr><td>Earth</td><td>1.00</td><td>0.017</td><td>1.00</td><td>328900.55</td><td>0.0</td></tr><tr><td>Mars</td><td>1.52</td><td>0.093</td><td>1.88</td><td>3098710.00</td><td>1.8</td></tr><tr><td>Jupiter</td><td>5.20</td><td>0.048</td><td>11.86</td><td>1047.35</td><td>1.3</td></tr><tr><td>Saturn</td><td>9.54</td><td>0.056</td><td>29.42</td><td>3498.00</td><td>2.5</td></tr><tr><td>Uranus</td><td>19.19</td><td>0.046</td><td>83.75</td><td>22960.00</td><td>0.8</td></tr><tr><td>Neptune</td><td>30.06</td><td>0.009</td><td>163.72</td><td>19314.00</td><td>1.8</td></tr><tr><td>Pluto</td><td>39.53</td><td>0.249</td><td>248.02</td><td>130000000.00</td><td>17.1</td></tr></table>

Seven out of eight planets have small eccentricities and inclinations.

The distinction is made between the inner and outer system. IAU's wisdom named Pluto as a dwarf planet. Minor planets are found “adjacent to the boundaries” of the newly defined outer system.

# Equations of Motion: Planetary System

If the revolution periods of Jupiter and a MP may be expressed as the quotient of two small integer numbers, the revolution periods are said to be commensurable:

$$
{ \frac { P _ { 4 } } { P } } = { \frac { n } { n _ { 4 } } } = { \frac { k _ { 1 } } { k _ { 2 } } }
$$

Disregarding perturbations the motion of the two CBs is periodic, where the period is called resonance period

$$
P _ { \mathrm { r e s } } = k _ { 1 } P = k _ { 2 } P _ { 4 }
$$

The mean synodic period of a planet (from conjunction to coniunction) is obtained as"

$$
P _ { \mathrm { s y n } } = { \frac { 2 \pi } { n - n _ { 4 } } } = { \frac { P P _ { 4 } } { P _ { 4 } - P } }
$$

Resonance and synodic periods are related by:

$$
P _ { \mathrm { r e s } } = \left( k _ { 1 } - k _ { 2 } \right) P _ { \mathrm { s y n } }
$$

# Equations of Motion: Artificial Earth Satellites

# Preamble:

The following derivations are in principle applicable to any satellites (with negligible mass) orbiting about any planet or moon of a planet. The following formulas, taken from Beutler (20o5),do for simplicity always refer to the Earth as central body.   
We are thus deriving the Eqs of motion of an artificial Earth satelite. In order to somewhat simplify the theory，we treat the Earth as a rigid body of finite dimensions. Through this assumption we avoid the introduction of Tisserand coordinate systems, Beutler (2005),Vol I, Section 3.3.7, p. 91ff.   
The derivation of the EQs of motion of artificial satellites follows the scheme of the derivation laid down in the previous section.

# Equations of Motion: Artificial Earth Satellites

# Characterization of the problem:

The mass of the satelite may be neglected w.r.t. mass of the planet (the Earth); it is thus assumed that the artificial Earth satelites do not influence the Earth's orbital and rotational motion.

- Orbits and masses of other CBs are assumed as known.

The Earth is treated as a CB with finite dimensions.The other CBs involved usually are treated as point masses (with the possible exception of the Moon).

- As opposed to the EQs of motion of the planetary system, nongravitational forces (actually perturbing accelerations of the satellite due to non-gravitational forces) have to be included as well.

- The satellite mass and its surface properties are of paramount importance for modeling non-gravitational forces.

Relativistic effects are small and may be treated as perturbations. The key-word is “parameterized Post-Newtonian” equations (see Beutler (2005), Vol I, Sections 3.5 and 4.4).

# Equations of Motion: Artificial Earth Satellites

The EQs of motion for a satelite of mass m are first set up in an IS. In the non-relativistic approximation we have the change of linear momentum on the LHS of the EQs,the sum of the forces on the RHS:

$$
\begin{array} { l } { { \displaystyle m \ddot { \pmb { x } } = - G m \int \rho _ { p _ { r } } \ \frac { \pmb { x } - \pmb { x } _ { p } } { | \pmb { x } - \pmb { x } _ { p } | ^ { 3 } } \ d V _ { \pmb { \mathscr { s } } } } } \\ { { \displaystyle ~ - G m \sum _ { j = 1 } ^ { n } m _ { j } \frac { \pmb { x } - \pmb { x } _ { j } } { | \pmb { x } - \pmb { x } _ { j } | ^ { 3 } } \ + \ \sum \pmb { f } _ { \mathrm { n g } } } } \end{array}
$$

The first term on the RHS represents the gravitational atraction by the Earth, where $\rho _ { p }$ is the density at $\pmb { X _ { p } }$ in the Earth's interior.

The second term represents the sum of the gravitational atractions of all CBs included.

The third term stands for the sum of all non-gravitational forces.

# Equations of Motion: Artificial Earth Satellites

Dividing both sides of the EQs of motion by the satellite mass m we obtain the usual version of the EQs of motion in the IS:

$$
: M \int _ { V _ { \delta } } \rho _ { p _ { r } } \frac { x - x _ { p } } { | x - x _ { p } | ^ { 3 } } ~ d V _ { \delta } - G \sum _ { j = 1 } ^ { n } m _ { j } \frac { x - x _ { j } } { | x - x _ { j } | ^ { 3 } } + \sum _ { \delta = 1 } a _ { \mathrm { n n } }
$$

where $\textcircled { \scriptsize { \mathsf { G } } }$ is the gravity constant, $M$ the total mass of the Earth (including oceans and atmosphere).

$\rho _ { p r }$ is the density at $\boldsymbol { x } _ { p } ,$ expressed in units of M.

$a _ { n g }$ are the non-gravitational forces per mass m of the satellite, often somewhat incorrectly expressed as non-g accelerations.

The EQ of motion acting on the Earth's CoM simply is:

$$
\ddot { \pmb { x } } _ { \updownarrow } = - G \sum _ { j = 1 } ^ { n } m _ { j } \frac { \pmb { x } _ { \updownarrow } - \pmb { x } _ { j } } { | \pmb { x } _ { \updownarrow } - \pmb { x } _ { j } | ^ { 3 } }
$$

# Equations of Motion: Artificial Earth Satellites

Subtracting the EQ of motion for the CoM of the Earth from the EQ of motion of the satelite (both EQs referring to an IS) we obtain the geocentric EQs of motion of the satellite.

The resulting reference system is quasi-inertial: It is for each epoch t parallel to the IS, but as it is geocentric, it contains the nonlinear motion of Earth's orbital motion:

$$
\ddot { r } = - G M \int _ { V _ { \pm } } \rho _ { p _ { r } } \frac { r - r _ { p } } { | r - r _ { p } | ^ { 3 } } d V _ { \pm }
$$

$$
{ \begin{array} { l } { \displaystyle - G \sum _ { j = 1 } ^ { n } m _ { j } \left\{ { \frac { r - r _ { j } } { \vert r - r _ { j } \vert ^ { 3 } } } + { \frac { r _ { j } } { r _ { j } ^ { 3 } } } \right\} \ \mathrm { ~ + ~ } \sum a _ { \mathrm { n g } } } \\ { r \ { \stackrel { \mathrm { d e f } } { = } } \ x - x _ { \delta } } \end{array} }
$$

where:

In satellite geodesy we use the equatorial system J20o0.0 to express the above equations in coordinates.

# Equations of Motion: Artificial Earth Satellites

All gravitational contributions on the RHS of the EQs of motion may be expressed as gradients of a potential:

$$
\begin{array} { l } { { \displaystyle { G M \nabla \int _ { V _ { \delta } } \frac { \rho _ { p _ { r } } } { | r - r _ { p } | } d V _ { \delta } } } } \\ { ~ } \\ { { \displaystyle ~ + G \nabla \left[ \sum _ { j = 1 } ^ { n } m _ { j } \left\{ \frac { 1 } { | r - r _ { j } | } + \frac { r _ { j } \cdot r } { r _ { j } ^ { 3 } } \right\} \right] + \sum a _ { \mathrm { n } } } } \end{array}
$$

The above integral is evaluated in an Earth-fixed system - alternatively one would have to perform the integration over a time-varying Earth-body,a true nightmare.

# Equations of Motion: Artificial Earth Satellites

The EQs of motion were derived as vector equations. We may, however, also understand/interpret them as coordinate EQs in the quasi-inertial equatorial system.

To evaluate the Earth's potential in the Earth-fixed system, the first term has to be transformed back from the Earth-fixed system to the /S.

$$
{ \bf \cal T } _ { \delta } ~ \nabla V ( { \boldsymbol r } ) ~ + ~ G \nabla \left[ \sum _ { j = 1 } ^ { n } m _ { j } \left\{ \frac { 1 } { | { \boldsymbol r } - { \boldsymbol r } _ { j } | } + \frac { { \boldsymbol r } _ { j } \cdot { \boldsymbol r } } { r _ { j } ^ { 3 } } \right\} \right] + \sum
$$

T Is the transformation matrix form the Earth-fixed system to the quasi-inertial system.

The above equation refers to the quasi-inertial geocentric system.

The gradient operation in the first term on the RHS must be performed in the Earth-fixed system.

# Equations of Motion: Artificial Earth Satellites

In the Earth-fixed svstem the botential function of the Earth reads as:

$$
V ( \pmb { r } ) = G M \int _ { V _ { \pmb { \imath } } } \frac { \rho _ { p _ { r } } } { | \pmb { r } - \pmb { r } _ { p } | } \ d V _ { \pmb { \imath } }
$$

Using the Laplace equation (which holds in the exterior of the mass distribution),one eventually obtains the following representation (for details we refer to Beutler, Vol. I, Section 3.4.2):

$$
\it { \dot { \ s } ) = \frac { { G M } } { r } \sum _ { i = 0 } ^ { \infty } \left( \frac { a _ { \delta } } { r } \right) ^ { i } \sum _ { k = 0 } ^ { i } P _ { i } ^ { k } ( \sin \phi ) \big \{ C _ { i k } \cos k \lambda + S _ { i k } \sin }
$$

where $r$ is the satelite's distance from the Earth's CoM, $\lambda$ is the satellites spherical longitude, $\phi$ its spherical latitude.

$P .$ .(sin $\phi$ ）are the associated Legendre functions of degree iand order k.

$C _ { i k }$ and $S _ { i k }$ are the coefficients of the development of the potential into spherical harmonic functions.

# Equations of Motion: Artificial Earth Satellites

The coefficients may be expressed as functions of the Earth's density:

$$
\begin{array} { l } { { \displaystyle \mathcal { T } _ { i 0 } = \frac { 1 } { a _ { \delta } ^ { i } } \int \rho _ { p _ { r } } r ^ { i } P _ { i } ( { \sin \phi } _ { p } ) ~ d V ~ ; ~ i \ge 0 } } \\ { { \displaystyle \mathcal { T } _ { i k } = \frac { 2 } { a _ { \delta } ^ { i } } \frac { ( i - k ) ! } { ( i + k ) ! } \int \rho _ { p _ { r } } r ^ { i } P _ { i } ^ { k } ( { \sin \phi } _ { p } ) { \cos k \lambda } _ { p } ~ d V ~ ; ~ i , k \ge 0 ~ , } } \\ { { \displaystyle \mathrm { S } _ { i k } = \frac { 2 } { a _ { \delta } ^ { i } } \frac { ( i - k ) ! } { ( i + k ) ! } \int \rho _ { p _ { r } } r ^ { i } P _ { i } ^ { k } ( { \sin \phi } _ { p } ) { \sin k \lambda } _ { p } ~ d V ~ ; ~ i , k > 0 ~ , } } \end{array}
$$

The coefficients might be calculated, if the density function in the Earth's interior were known.

As this is not the case, the C., S..are the parameters of gravity field estimation.

# Equations of Motion: Artificial Earth Satellites

The terms of the degrees $i { = } 0$ und $j { = } 1$ assume simple values:

$$
\begin{array} { l } { { C _ { 0 0 } = \displaystyle \int \rho _ { p _ { r } } r _ { p _ { j } } ^ { 0 } d V = 1 } } \\ { { \ } } \\ { { { V _ { 3 } } } } \\ { { C _ { 1 0 } = \displaystyle \frac { 1 } { a _ { 5 } } \displaystyle \int \rho _ { p _ { r } } r _ { p } \sin \phi _ { p } d V = \displaystyle \frac { 1 } { a _ { 5 } } \displaystyle \int \rho _ { p _ { r } } r _ { p _ { 3 } } d V = \displaystyle \frac { r _ { 3 } } { a _ { 5 } } = 0 } } \\ { { { V } _ { 5 } } } \\ { { C _ { 1 1 } = \displaystyle \frac { 1 } { a _ { 5 } } \displaystyle \int \rho _ { p _ { r } } r _ { p } \cos \phi _ { p } \cos \lambda _ { p } d V = \displaystyle \frac { 1 } { a _ { 5 } } \displaystyle \int \rho _ { p _ { r } } { } _ { , } { r _ { p _ { 1 } } } d V = \displaystyle \frac { r _ { 7 } } { a _ { 5 } } } } \\ { { { V } _ { 5 } } } \\ { { S _ { 1 1 } = \displaystyle \frac { 1 } { a _ { 5 } } \displaystyle \int \rho _ { p _ { r } } r \cos \phi _ { p } \sin \lambda _ { p } d V = \displaystyle \frac { 1 } { a _ { 5 } } \displaystyle \int \rho _ { p _ { r } } { r _ { p _ { 2 } } } d V = \displaystyle \frac { r _ { 2 } } { a _ { 3 } } } } \end{array}
$$

provided we adopt the Earth's CoM as the origin of the Earthfixed coordinate system.

# Equations of Motion: Artificial Earth Satellites

The terms of degree $\scriptstyle { j = 2 }$ may be interpreted in a simple way, provided the coordinate axes are selected as the axes of principal inertia:

$$
\begin{array} { l } { { \displaystyle C _ { 2 0 } = \frac { 1 } { a _ { \updownarrow } ^ { 2 } } \int \rho _ { p r } r _ { p } ^ { 2 } \big [ \sin ^ { 2 } \phi _ { p } - \frac { 1 } { 2 } \cos ^ { 2 } \phi _ { p } \big ] d V } } \\ { { \displaystyle \ } } \\ { { \ = \frac { 1 } { a _ { \updownarrow } ^ { 2 } } \int \rho _ { p r } \big [ r _ { p 3 } ^ { 2 } - \frac { 1 } { 2 } \left( r _ { p 1 } ^ { 2 } + r _ { p 2 } ^ { 2 } \right) \big ] d V } } \\ { { \displaystyle \ } } \\ { { \displaystyle = \frac { 1 } { M a _ { \updownarrow } ^ { 2 } } \left[ \frac { 1 } { 2 } \left( I _ { \updownarrow \cdotp _ { 1 1 } } + I _ { \xi _ { \it g _ { 2 2 } } } \right) - I _ { \xi _ { \it g _ { 3 3 } } } \right] = \frac { 1 } { M a _ { \updownarrow } ^ { 2 } } \left[ \frac { 1 } { 2 } \left( A _ { \updownarrow } + B _ { \delta } \right) - C _ { \xi } \right] } } \end{array}
$$

$$
\left. \begin{array} { l } { \displaystyle \frac { 1 } { a _ { \delta } ^ { 2 } } \displaystyle \int \rho _ { p _ { r } } r _ { p } ^ { 2 } \cos \lambda _ { p } \cos \phi _ { p } \sin \phi _ { p } d V } \\ { \displaystyle \frac { 1 } { a _ { \delta } ^ { 2 } } \displaystyle \int \rho _ { p _ { r } } r _ { p _ { 1 } } r _ { p _ { 3 } } d V = - \frac { 1 } { M a _ { \delta } ^ { 2 } } I _ { \delta _ { \mathcal F _ { 1 3 } } } = 0 } \\ { \displaystyle \frac { V _ { \delta } } { V _ { \delta } } } \end{array} \right| _ { V _ { \delta } } = \frac { 1 } { a _ { \delta } ^ { 2 } } \displaystyle \int \rho _ { p _ { r } } r _ { p _ { 2 } } ^ { 2 } \sin \lambda _ { p } \cos \lambda _ { p } ^ { 2 } ,
$$

C2o represents the flattening of the Earth. A.., B..,and C.. are the Earth's three principal moments of inertia.

# Equations of Motion: Artificial Earth Satellites

The development of the Earth's potential into spherical harmonics:

- Each solution of the Laplace-EQ is called a harmonic function.

- When expressed in spherical coordinates,one also speaks of sphericalharmonic functions, or simply of spherical harmonics.

- The potential function of the Earth has terms of the following kind:

Zonal terms, not depending on $\lambda$ (but only of r und $\phi )$ ，

， sectorial terms, not\*) depending on $\phi$ (but only on $\lambda$ and r), as well as

Tesseral terms, depending on all three spherical coordinates.

\*) Apart from the weighting factor lcos $\phi ^ { k }$ for terms of degree and order k

The following pictures represent the three different kinds of terms - on a unit sphere. Zones where the potential function has a positive sign are marked in white, those with a negative sign in black.

# Equations of Motion: Artificial Earth Satellites

![](images/661524a0e841507b791df46dee13929574e7d202d28e8390981b0d0052ef78a9.jpg)

From left to right: Zonal (6,O), sectorial (7,7) and tesseral harmonic (13,7) functions.

# Equations of Motion: Artificial Earth Satellites

Using fully normalized Legendre functions， the corresponding harmonics are normalized for $r { = } a$ and the coefficients $C _ { i k } , S _ { i k }$ are a measure for the corresponding terms.

The first few coefficients of the potential are (model JGM3):

<table><tr><td>Coefficient</td><td>Value</td><td>Coefficient</td><td>Value</td></tr><tr><td>GM</td><td>398.60044150 -1012 ms-2</td><td>a</td><td>6378136.30 m</td></tr><tr><td>C20</td><td>-0.48416954845647 · 10-3</td><td>S20</td><td></td></tr><tr><td>C21</td><td>-0.18698764000000 · 10-9</td><td>S21</td><td>+0.11952801000000 · 10-8</td></tr><tr><td>C22</td><td>0.24392607486563 · 10-5</td><td>S22</td><td>-0.14002663975880 ·10-5</td></tr><tr><td>C30</td><td>+0.95717059088800 · 10-6</td><td>S30</td><td></td></tr><tr><td>C31</td><td>+0.20301372055530 ·10-5</td><td>S31</td><td>+0.24813079825561 · 10-6</td></tr><tr><td>C32</td><td>+0.90470634127291 ·10-6</td><td>S32</td><td>-0.61892284647849 ·10-6</td></tr><tr><td>C33</td><td>+0.72114493982309 ·10-6</td><td>S33</td><td>+0.14142039847354 · 10-5</td></tr><tr><td>C40</td><td>+0.53977706835730 ·10-6</td><td>S40</td><td></td></tr><tr><td>C41</td><td>-0.53624355429851 · 10-6</td><td>S41</td><td>-0.47377237061597 · 10-6</td></tr><tr><td>C42</td><td>+0.35067015645938 ·10-6</td><td>S42</td><td>+0.66257134594268 · 10-6</td></tr><tr><td>C43</td><td>+0.99086890577441 ·10-6</td><td>S43</td><td>-0.20098735484731·10-6</td></tr><tr><td>C44</td><td>-0.18848136742527 · 10-6</td><td>S44</td><td>+0.30884803690355 ·10-6</td></tr></table>

# Equations of Motion: Artificial Earth Satellites

We know that ${ C _ { 0 0 } } \mathrm { { = } } 1$ .We may thus summarize:

The term $C _ { 2 0 }$ is small compared to the main term (factor of 2000). The term $C _ { 2 0 }$ is the largest perturbation terms, by three orders of magnitude larger than all the others. The term is caused by the difference of the equatorial and polar moments of inertia (A & B and $\complement$ ,respectively).   
The other perturbation terms are of a similar order of magnitude, butabout 200-1000 timessmalerthan $C _ { 2 0 }$ ·

We may thus conclude that the that an accurate description of the Earth potential becomes relatively complicated for degrees $n >$ 2-

Kaula's rule of thumb gives an approximate “law" for the order of magnitude of the fully normalized geopotential terms as a function of the degree i:

$$
\begin{array} { l l } { { \displaystyle { \frac { \imath \mathrm { ~ d e f ~ } } { = } \sum _ { k = 0 } ^ { i } \left[ \bar { C } _ { i k } ^ { 2 } + \bar { S } _ { i k } ^ { 2 } \right] } \quad \quad \quad } } & { { \displaystyle { \sigma _ { i } ^ { 2 } = \frac { 1 6 0 \cdot 1 0 ^ { - 1 2 } } { i ^ { 3 } } } } } \end{array}
$$

# Equations of Motion: Artificial Earth Satellites

![](images/4af982409e15f2e47abf4eeefb653fa0d4ae5fe250d999803d6aefa49d437b34.jpg)

Kaula's,,rule of thumb" and the ,true" degree amplitudes of degree i of the JGM3.

# Orbit Parameterization

The EQs of motion of an artificial Earth satelite moving under the gravitational attraction of Earth, Moon, Sun, planets and of nongravitational forces may be written as:

$$
\ddot { \mathbf { r } } = - G M \frac { \mathbf { r } } { r ^ { 3 } } + \delta \mathbf { f } \left( t , \mathbf { r } , \dot { \mathbf { r } } \right)
$$

If the state vector $( r ( t _ { O } ) , v ( t _ { O } ) )$ is known at an initial epoch $t _ { O } ,$ a particular solution of the above DEQ is defined.

There is a one-to-one relationship between the state vector and the socalled osculating orbital elements of an epoch t:

$$
r ( t ) , \dot { r } ( t ) \Leftrightarrow a ( t ) , e ( t ) , i ( t ) , \Omega ( t ) , \omega ( t ) , T _ { 0 } ( t )
$$

where a stands for the semi-major axis, e for the numerical eccentricity, ifor the inclination w.r.t. the equator, $\varOmega$ for the right ascension of the ascending node, $\omega$ for the distance of the preigee from the node, and $\tau _ { o }$ for perigee passing time.

# Orbital Coordinate System $( x , y , z ( = 0 ) )$ 1

$\pmb { \ 6 } _ { x }$ axis: geocentric direction to perigee, z-axis: $\pmb { \mathrm { e } } _ { z } = \left( r \times \pmb { v } / \vert \ r \times \pmb { v } \vert \right)$ , y-axis: $\pmb { \mathrm { e } } _ { y } = \pmb { \mathrm { e } } _ { z } \times \pmb { \mathrm { e } } _ { x }$

![](images/2f04751038d97f5105424019b8ae1ed2f971b8ecab2e46de0c22ae712db3e4f4.jpg)

v is the so-called true anomaly

Coordinates in orbital system:

n=mean motion (rad/s) $\scriptstyle n ^ { 2 } a ^ { 3 } = G M$

$$
\sigma ( t ) = n \ ( t { - } T _ { o } ) \ ( { \tt { = } } \mathsf { { m e a n \ a n o m a l y } } )
$$

Kepler's equation: $E ( t ) = \sigma ( t ) + e s i n E ( t )$ $E ( t ) =$ eccentric anomaly

$x = a ( \cos E - e )$ $y = a { \sqrt { 1 - e ^ { 2 } } } \sin E$

# Orbit Transformation Orbital → IS

![](images/41fad15f8f9a4477ce9d80d8e1ffab7e636b08fa868eda16408b0a87e2ac9319.jpg)

X and y are the coordinates in the orbital system.

$X _ { a } , Y _ { a } , Z _ { a }$ the coordinates in the IS (equatorial system J2000.0).

$\mathsf { R } _ { \mathrm { i } } ( \mathrm { \alpha } )$ is the rotation matrix about axis iand around the angle $\alpha$

The transformation from the orbital system to the IS then reads as (dotted quantities stand for the time derivatives):

$$
\left( \begin{array} { l } { x _ { a } } \\ { y _ { a } } \\ { z _ { a } } \end{array} \right) = \mathbf { R } _ { 3 } ( - \Omega ) \cdot \mathbf { R } _ { 1 } ( - i ) \cdot \mathbf { R } _ { 3 } ( - \omega ) \cdot \left( \begin{array} { l } { x } \\ { y } \\ { 0 } \end{array} \right)
$$

$$
\left( \begin{array} { l } { \dot { x } _ { a } } \\ { \dot { y } _ { a } } \\ { \dot { z } _ { a } } \end{array} \right) = \mathbf { R } _ { 3 } ( - \Omega ) \cdot \mathbf { R } _ { 1 } ( - i ) \cdot \mathbf { R } _ { 3 } ( - \omega ) \cdot \left( \begin{array} { l } { \dot { x } } \\ { \dot { y } } \\ { 0 } \end{array} \right)
$$

# Orbital Coordinate Systems

Table 4.3. Orbital coordinate systems   

<table><tr><td></td><td></td><td>System First unit vectorTransformation from Inertial SystemI</td></tr><tr><td>Ω</td><td>eΩ=exh h</td><td>rn= R1(i)R3(Ω) r</td></tr><tr><td>Ⅱ</td><td>en= q</td><td>rⅡ= R3(ω)R1(i)R3()r</td></tr><tr><td>R</td><td>1 eR=</td><td>rR= R3(u)R1(i) R3(Ω) r</td></tr><tr><td></td><td></td><td>rT= R3(ξ)R3(ω）R1(i)R(）r</td></tr></table>

Beutler (2005), Vol.1,Table 4.3 makes the distinction of four orbital systems The one we defined previously is the second one of the above table. In perturbation theory we will need the third or the fourth of these systems.

# Elements of perturbation theory: Contents

1.Osculating and mean orbital elements   
2. Motivation and classification   
3. Gaussian perturbation equations   
4．Perturbations of the first order

# Osculating and mean elements

The two-body problem allows it to calculate for each epoch $t$ the state vector $( r ( t ) , v ( t ) )$ using a set of orbital elements $( a , e , i , \varOmega , \omega , T _ { o } )$

Vice-versa this (time-independent) set of elements may be calculated from the state vector of each epoch $t$ ：

$$
t : \{ { \pmb r } ( t ) , { \pmb \dot { r } } ( t ) \}  \{ a , e , i , \Omega , \omega , T _ { 0 } \}
$$

For a perturbed trajectory solving the DEQ on page 34 one may assign a set of osculating element to each epoch $t$ by calculating orbital elements from the corresponding state vector using the formulas of the two-body problem. Such elements are called osculating orbital elements (at osculation epoch $t )$ ：

$$
: \{ \pmb { r } ( t ) , \pmb { \dot { r } } ( t ) \}  \{ a ( t ) , \pmb { e } ( t ) , i ( t ) , \Omega ( t ) , \omega ( t ) , T _ { 0 } ( t ) \}
$$

# Osculating and mean elements

![](images/9dfc675018af5bf21758ef387d1ac8549fc536d96783416f3a663385e41cfa70.jpg)

![](images/32bdbe8769d133be04a864f403481ab8d2506d717372b29f4b342ff7b8a9cc5a.jpg)

Osculating elements are unsuitable to describe the development of an orbit over long time intervals (hundreds of revolutions). The above Figure (left) shows the development of Jupiter's semi-major axis over 120 years (when integrating the outer planetary system). The figure shows a prominent_periods of about 60 years ( $\sqsupseteq$ five revolutions of Jupter, 2 of Saturn).

The above Figure (right), showing the development of Jupiter's osculating semi-major axis years over 20o0 years,motivates the definition of mean orbital elements.

# Osculating and mean elements

Let $I ( t ) \in \{ a ( t ) , \Theta ( t ) , i ( t ) , \varOmega ( t ) , \omega ( t ) , T _ { o } ( t ) \}$ one of the osculating orbital elements. A mean orbital element at epoch $t$ is defined by:

$$
\bar { I } ( t ; \Delta t ( t ) ) = \frac { 1 } { \Delta t } \int _ { t - \Delta t / 2 } ^ { t + \Delta t / 2 } I ( t ^ { \prime } ) ~ d t ^ { \prime }
$$

By construction the mean elements are analytical functions of timet.Theaveraging period△tshould eitherbe very long ora multiple of the prevailing short periods.

The following example meets this requirement..

Unskilfully selected △t may result in the generation of alias periods.

# Osculating and mean elements

![](images/6b53af4b36aedf9d430c502abd764c6946d94a68e17fadf0df9fc99c5e3caa2b.jpg)

![](images/c6c2a36dd067e82436bef99bb59886a4e21b51f2688a862e1fbb402e620a1109.jpg)

Osculating (eft) und mean (right) semi-major axis a of Jupiter over 2000 years. $\varDelta t = 5$ revs of Jupiter $= 2$ revs of Saturn.

The period of 9oo is called the great inequality. It was detected in the early $1 7 ^ { \mathrm { t h } }$ century (Kepler era) as excursions in the longitudes of the planets Jupiter and Saturn, not in the semimajor axes.

The effect was correctly explained by Pierre-Simon de Laplace in 1787.

# Perturbations: Classification

The expression perturbed motion implies that an unperturbed motion exists. In CM the unperturbed motion is the two-body motion.

The perturbed motion is defined by the EQs of motion (in this context called perturbation equation) and the associated state vector at $t _ { \mathrm { } \mathrm { } \mathrm { } \mathrm { } } .$

$$
\ddot { r } = - \mu { \frac { r } { r ^ { 3 } } } + \delta f ( t , r , \dot { r } ) ,
$$

$$
r ( t _ { 0 } ) = r _ { \mathrm { 0 } } \quad \mathrm { a n d } \quad \pmb { \dot { r } } ( t _ { 0 } ) = { \pmb v } _ { \mathrm { 0 } }
$$

The first term on the RHS of the above DEQ may be calld two-body term, the second perturbation term. The terminology makes sense, provided:

$$
\mid \delta f \mid \ll { \Big | } - \mu { \frac { r } { r ^ { 3 } } } { \Big | }
$$

# Perturbations: Classification

All methods to solve the perturbation equations are called

Methods of perturbation theory or simply perturbation method.

In CM we make the distiction between

General perturbation methods, if the solution is sought in terms of elementary inegrable functions

Special perturbation methods, if the solution is generated numerically.

General perturbation theory played a preeminent role in CM and in the context of the development of analytical mechanics..

With the advent of electronic computers in the 2nd half of the 20th century special perturbation methods replaced the general methods for most applications.

General perturbation methods are important today for studies trying to understand particular perturbed motions.

# Gaussian Perturbation Equations

Let $I ( t ) \in \{ a ( t ) , \Theta ( t ) , i ( t ) , \varOmega ( t ) , \omega ( t ) , T _ { o } ( t ) \}$ an osculating element.

By construction their time dependence is given by that of the state vector:

$$
I ( t ) \stackrel { \mathrm { d e f } } { = } I ( \boldsymbol { r } ( t ) , \dot { \boldsymbol { r } } ( t ) )
$$

The time development of $I ( t )$ is obtained by taking the the time derivative of the above EQ:

$$
\dot { I } = \sum _ { l = 1 } ^ { 3 } \left\{ \frac { \partial I } { \partial r _ { l } } \dot { r } _ { l } + \frac { \partial I } { \partial \dot { r } _ { l } } \ddot { r } _ { l } \right\} = \nabla _ { r } I \cdot \dot { r } + \nabla _ { v } I \cdot \ddot { r }
$$

The second time derivative of $r$ in the second term on the RHS may be replaced by using the perturbation EQ in rectangular coordinates:

$$
\dot { I } = \nabla _ { r } I \cdot \dot { r } + \nabla _ { v } I \cdot \left\{ - \mu \frac { r } { r ^ { 3 } } + \delta f \right\}
$$

# Gaussian Perturbation Equations

As I(t)=constin the two-body motion,we obtain the remarkably simple Gaussian perturbation equations:

$$
\dot { I } = \nabla _ { v } I \cdot \delta f
$$

The six perturbation equations in the osculating elements may thus be written as a systems of 6 coupled DEQs of order 1:

$$
\dot { I } _ { k } = \nabla _ { v } I _ { k } \cdot \delta \mathbf { \boldsymbol { f } } \ , \quad k = 1 , 2 , \ldots , 6
$$

The DEQ system is mathematically equivalent to the perturbation EQs in rectangular coordinates (3 DEQs of second order).

The alternative formulation is attractive, as the RHS are small quantities.

To obtain the Gaussian perturbation equations in explicit form for a particular perturbation $\delta { \pmb f } ,$ one merely has to calculate the scalar products on the RHS.

# Gaussian Perturbation Equations

Let us directly derive the perturbation equation for a from energy preservation of the two-body motion:

$$
\frac { \mu } { a } = \frac { 2 \mu } { r } - \dot { r } ^ { 2 }
$$

Taking the gradient (in velocity space) on both sides of the Eq we obtain:

$$
\frac { \ d s ^ { \prime } } { \ d t } \bigg ) = - \frac { \mu } { a ^ { 2 } } \nabla _ { \boldsymbol { v } } a = - 2 \dot { \boldsymbol { r } } \qquad \mathrm { o r : } \qquad \nabla _ { \boldsymbol { v } } a = \frac { 2 a ^ { 2 } } { \mu } \dot { \boldsymbol { r } }
$$

The Gaussian perturbation EQ for the semi-major axis a thus reads as:

$$
\dot { a } = \frac { 2 a ^ { 2 } } { \mu } \dot { r } \cdot \delta f
$$

# Gaussian Perturbation Equations

![](images/7d034d53db7b32e06734631a3b01106d13ac604c08b11ff76fbab7650a7ede39.jpg)

Scalar products are invariant under rotation. Therefore one may use particularly well suited decompositions of the forces.

The figure illustrates the $( R , S , W )$ and die $( T , N , W )$ -decomposition. $R$ stands for the radial, S for normal to $R$ in the orbital plane (close to along-track). W is parallel to ${ \tt e } _ { R } X { \tt e } _ { S } ,$ i.e., normal to the orbital plane.

Tis the along-track component, $N$ is normal to Tpointing into the interior of the ellipse.

Many perturbations may be particularly simply represented in one of the two decompositions (e.g., drag and radiation pressure).

# Gaussian Perturbation Equations

Using the $( R , S , W )$ -decomposition the Gaussian perturbation equations for the six classical osculating elements read as:

$$
\begin{array} { r l } { \dot { \alpha } } & { = \sqrt { \frac { \mathcal { P } } { \mu } } \frac { 2 \alpha } { 1 - e ^ { 2 } } \left\{ \epsilon \sin \pi ^ { \mu } + \frac { p } { r } S ^ { \mu } \right\} } \\ { \dot { \boldsymbol { z } } } & { = \sqrt { \frac { \mathcal { P } } { \mu } } \left\{ \sin \pi { \cal R } ^ { \mu } + \left( \cos \pi + \cos \mathcal { E } \right) S ^ { \nu } \right\} } \\ { \dot { T } _ { \mathrm { n } } = - \frac { 1 - e ^ { 2 } } { n ^ { 2 } } \Bigg \{ \left( \cos \nu - 2 \epsilon \frac { \gamma } { p } \right) { \cal R } ^ { \mu } - \left( 1 + \frac { r } { p } \right) \sin \pi S ^ { \nu } \Bigg \} - \frac { 1 } { 2 } } \\ { \dot { \alpha } } & { = \frac { r \cos \alpha } { n \alpha ^ { 2 } \sqrt { 1 - e ^ { 2 } } } { \cal W } ^ { \mu } } \\ { \dot { \mathcal { Q } } } & { = \frac { r \sin \alpha } { n \alpha ^ { 2 } \sqrt { 1 - e ^ { 2 } } \sin \alpha ^ { 4 } } { \cal W } ^ { \mu } } \\ { \dot { \alpha } } & { = \frac { 1 } { \epsilon } \sqrt { \frac { \mathcal { P } } { \mu } } \left\{ - \cos \alpha { \cal R } ^ { \mu } + \left( 1 + \frac { r } { \dot { \rho } } \right) \sin \nu S ^ { \nu } \right\} - \cos \delta \dot { \mathcal { Q } } . } \end{array}
$$

The Gaussian perturbation equations hold for al types of forces (conservative or non-conservative).

# Gaussian Perturbation Equations

The Gaussian perturbation equations may be solved approximately making use of the fact that the RHS of the Gaussian perturbation EQs are small quantities.

Perturbation methods of first order result, if the RHS of the EQs are approximated with the two-body approximation (keeping the osculating elements constant).

In this case the coupled system of six first-order DEQs becomes decomposed into six mutually independent integrals,which may be solved independently.

The scalar products on the RHS of the perturbation equations are thus calculated with the two-body approximation.

Perturbation methods of the first order are very eficient. Note, however, that the results are approximate and should not be used over more than a few revolutions.

# Perturbations due to C20

Let us assume that:

- only the terms $C _ { O O }$ and $C _ { 2 0 }$ are different from zero - the Earth's rotation axis coincides with the Earth's axis of maximum inertia - Precession, nutation,and polar motion are neglected.

Under these assumptions we may write:

$$
, \phi ) = \frac { G M } { r } + G M a _ { \delta } ^ { 2 } C _ { 2 0 } \frac { 1 } { r ^ { 3 } } \biggl ( \frac { 3 } { 2 } \sin ^ { 2 } \phi -
$$

Note that

- the Earth's potential is longitude-independent the transformation between the IS and the Earth-fixed system may be set to the unit matrix.

# Perturbations due to C20

The perturbations were provided in the equatorial system. They may be easily transformed into the $( R , S , W )$ -system:

$$
\begin{array}{c} \begin{array}{c} \begin{array} { c c c } { { \displaystyle { \begin{array} { l } { R ^ { \prime } } \\ { S ^ { \prime } } \\ { W ^ { \prime } } \end{array} } } } \end{array} = { \bf R } _ { 3 } ( u ) ~ { \bf R } _ { 1 } ( i ) ~ { \bf R } _ { 3 } ( \Omega ) ~ \frac { 3 } { 2 } \frac { \tilde { C } _ { 2 0 } } { r ^ { 5 } } \left( \begin{array} { l } { { r _ { 1 } \left( 1 - 5 \frac { r _ { 3 } ^ { 2 } } { r ^ { 2 } } \right. } } \\ { { r _ { 2 } \left( 1 - 5 \frac { r _ { 3 } ^ { 2 } } { r ^ { 2 } } \right. } } \\ { { \left. \left. r _ { 3 } \left( 3 - 5 \frac { r _ { 3 } ^ { 2 } } { r ^ { 2 } } \right. \right. \right.} } \end{array}  \right.   \\ { { \left. \left. r _ { 3 } \left( 3 - 5 \frac { r _ { 3 } ^ { 2 } } { r ^ { 2 } } \right. \right. \right.} } \end{array}    \end{array}
$$

Putting $\scriptstyle u = \omega + V$ the result is (see Beutler (2005), Vol. 2, Sect 3.1.2):

$$
\left( \begin{array} { c } { { R ^ { \prime } } } \\ { { S ^ { \prime } } } \\ { { W ^ { \prime } } } \end{array} \right) = \frac { 3 } { 2 } ~ \frac { \tilde { C } _ { 2 0 } } { r ^ { 4 } } ~ \left( \begin{array} { c c } { { 1 - \frac { 3 } { 2 } \sin ^ { 2 } i + \frac { 3 } { 2 } \sin ^ { 2 } i ~ \cos 2 u } } \\ { { \sin ^ { 2 } i ~ \sin 2 u } } \\ { { \sin 2 i ~ \sin u } } \end{array} \right)
$$

# Perturbations due to C20

The previous expressions may be introduced into the RHS of the Gaussian perturbation EQs .

Assuming the orbital elements on the RHS of these EQs as constant, the EQs may be solved in an elementary way.

Assume circular motion, adapt the Gaussian perturbation EQs to this case and solve them!

$$
{ \begin{array} { l } { { \displaystyle { \begin{array} { r l } { { \boldsymbol { \imath } } } & { { = { \sqrt { \frac { p } { \mu } } } { \frac { \strut } 2 a } { 1 - e ^ { 2 } } } \left\{ e \sin v R ^ { \prime } + { \frac { p } { r } } { \sin } { \boldsymbol { \ell } } \right. } \\ { { \dot { \boldsymbol { \jmath } } } } & { { = { \frac { \strut r \sin u } { n a ^ { 2 } { \sqrt { 1 - e ^ { 2 } } \sin i } } } W ^ { \prime } } \end{array} } } } \end{array} } } 
$$

# Perturbations due to C20

Subsequently the perturbation EQs will be solve without approximat-ions and the resulting osculating elements will be discussed. The osculating elements at $t _ { o } = \mathscr { s } a n ~ 1$ ,2001, $O ^ { h }$ are:

<table><tr><td>Element</td><td>Value</td><td>Element</td><td>Value</td></tr><tr><td>a</td><td>8000 km</td><td>e</td><td>0.07</td></tr><tr><td>i</td><td>35°</td><td>Ω</td><td>0°</td></tr><tr><td>8</td><td>00</td><td>T</td><td>to</td></tr></table>

a and e show only short-period variations.

![](images/efb7f22f4a8470d4cec15a420a30c1e2c41a432d902e09d6b63b04609d508b0d.jpg)

![](images/7547e72d973b9722408425ccb672be60ad13302ad45415b015356373b5df7d9a.jpg)

# Perturbations due to C20

![](images/50ab44f14bc9b0bfd5af53cfcb5dcb72f52e0ab248e02c4e00d32e8e0a91b31b.jpg)

The perturbations in the R.A. of the ascending node Ωand in the argument ωof perigee also show secular perturbations (the node rotates clockwise, the perigee ant-clockwise - for the initial conditions used).

# Perturbations due to C20

node (5 days)

![](images/9429e19f53fd2ca3727fa86651d7cd055abb32fe1e8742ab980fe476a7c1bc1d.jpg)

Rotation of the node for $I = 3 5 ^ { o }$ 63. $\pmb { 4 } ^ { o }$ and $90 \text{‰}$ .The node does not rotate for $\pmb { I } = 9 0 ^ { o }$ (and $i = O ^ { o } ,$ ).For $i > 9 0 ^ { o }$ ,the node progresses anti-clockwise.

# Perturbations due to C20

<table><tr><td>Height h [km]</td><td>Inclination i []</td><td>Revolution Period 1U [min]</td></tr><tr><td>400</td><td>97.03</td><td>92.6</td></tr><tr><td>600</td><td>97.79</td><td>96.7</td></tr><tr><td>800</td><td>98.61</td><td>100.9</td></tr><tr><td>1000</td><td>99.48</td><td>105.1</td></tr><tr><td>1200</td><td>100.42</td><td>109.4</td></tr></table>

Sun-synchronous orbits for different sm-axes (heights): The orbital plane must rotate anti-clockwise with 1°/ day, to keep the orientation of the orbital plane (approximately) constant w.r.t. the Sun. The above table gives the inclinations as a function of the orbit height, for which this the case.

The anti-clockwise motion of the node for $i { > } O ^ { o }$ may thus be used for LEOs to generate Sun-synchronous orbits (the GOCE orbit, e.g., lies approximately in the terminator plane).

# Perturbations due to C20

![](images/c40f506f5d428778220c13af4c837330847924203c0148c0d239d5c94267f888.jpg)

Rotation of perigee distance @for inclinations $\dot { I } = 3 5 ^ { \circ } .$ ,63.4°, 90°. For $i { = } 6 3 . 4 ^ { o }$ the perigee stands still. For $i < 6 3 . 4 ^ { o }$ the perigee moves ant-clockwise, for i>63.4° clockwise.

The inclination $\scriptstyle { j = 6 3 } .$ .4 is called critical inclination.

# Perturbations due to C20

The standstill of the perigee for $\scriptstyle { I = 6 3 }$ .4° may be used to keep the perigee (or apogee) at a particular latitude.

Russia developed a system of telecommunication satellites (Molnja-type). The satellite orbits have

- Eccentricities of about $e { = } O . 7 2$ ， SM axes of about 26550 km, - A perigee distance of about $\omega { = } 2 7 0 ^ { o }$ and - An inclination of $i { = } 6 3 . 4 ^ { o } ,$

The satellites thus have their apogees at a Northern latitude of $i { = } 6 3 . 4 ^ { o }$ and a height of $h _ { a p o } { = } 3 9 ^ { \prime } 3 6 0 k m$

As the satellites move much slower near apogee than near perigee, the satelites spend about 8-10 above Northern iatitudes (the revolution period is $1 2 \mathsf { h } )$

The Russian Tundra satellites (with $\scriptstyle { \mathtt { e } } = 0 . 2 7$ und and a revolution period of 1 day) also make use of the critical inclination. A permanent survey of the Northern hemisphere may be achieved with only three satellites.

# Non-gravitational forces

As opposed to natural CB of the planetary system non-gravitational forces are much more important when dealing with artificial satellites.

The area/mass-ratio A/m of a satelite is te most important parameter to characterize the non-gravitational forces.

A is the cross section of the satellite for the perturbation considered (for drag normal to the velocity vector, for radiation pressure normal to the direction Sun $\mid >$ satellite),mis the satellite mass.

For the first generation of Earth science satelites the attempt was made to render A/m as small as possible..

A/m-ratios of a few important satellites:

<table><tr><td>A/m[m²/kg] Satellite</td></tr><tr><td>Lageos and 2 0.0007</td></tr><tr><td>Starlette 0.001</td></tr><tr><td>GPS(Block II) 0.02</td></tr><tr><td>Moon 1.3 : 10-10</td></tr><tr><td></td></tr></table>

# Non-gravitational forces

<table><tr><td colspan="3">LAGEOS Parameters</td></tr><tr><td></td><td>LAGEOS-1</td><td>LAGEOS-2</td></tr><tr><td>Sponsor:</td><td>United States</td><td>United States &amp; Italy</td></tr><tr><td>Expected Life:</td><td>many decades</td><td>many decades</td></tr><tr><td>Primary Applications:</td><td>geodesy</td><td>geodesy</td></tr><tr><td>COSPAR ID:</td><td>7603901</td><td>9207002</td></tr><tr><td>SIC Code:</td><td>1155</td><td>5986</td></tr><tr><td>NORAD SSC Code:</td><td>8820</td><td>22195</td></tr><tr><td>Launch Date:</td><td>May 4, 1976</td><td>October 22,1992</td></tr><tr><td>RRA Diameter:</td><td>60 cm</td><td>60 cm</td></tr><tr><td>RRA Shape:</td><td>sphere</td><td>sphere</td></tr><tr><td>Reflectors:</td><td>426 corner cubes</td><td>426 corner cubes</td></tr><tr><td>Orbit:</td><td>circular</td><td>circular</td></tr><tr><td>Inclination:</td><td>109.84 degrees</td><td>52.64 degrees</td></tr><tr><td>Eccentricity:</td><td>0.0045</td><td>0.0135</td></tr><tr><td>Perigee:</td><td>5,860 km</td><td>5,620 km</td></tr><tr><td>Period:</td><td>225 minutes</td><td>223 minutes</td></tr><tr><td>Weight:</td><td>406.965 Kg</td><td>405.38 kg</td></tr></table>

Left: Characteristics of LAGEOS-1 und -2. Right:,Artist's view" of Lageos-2. Our knowledge of the Earth's gravity field stems in essence of these two satellites ...where admittedly remarkable contributions go back to the times of Newton ...).

# Non-gravitational forces

Left: Principles of satellite accelerometry.The motion of a test mass in the shielded interior is measured (kept in place through electrostatic forces). Right: real satellite accelerometer.

Stability in time is critical in any case one has to solve for one offset and one drift parameter per day (usually many more fudge parameters).

# Non-gravitational forces: drag

Above a height of about 50 km the atmospheric density is sufficiently small to ignore turbulence.

Assuming that Earth's atmosphere rotates with the solid Earth, the perturbation due to drag may be calculated in a simple way - provided the atmospheric density $\rho ( r )$ at the satellite position $r$ is known.

Assuming furthermore that the satellite absorbs all molecules hitting it in $[ t , t { + } \Delta t ]$ , the change of impuse $\varDelta p$ is calculated in the Earth-fixed system as:

$$
\Delta p = - \rho ( \pmb { r } ) A \dot { r } ^ { \prime 2 } \varDelta t \frac { \dot { \pmb { r } } ^ { \prime } } { | \dot { \pmb { r } } ^ { \prime } | }
$$

=rom where we obtain the perturbing acceleration due to drag as:

$$
\mathbf { \delta } \mathbf { a } _ { d } = - \rho ( r ) \frac { A } { m } \dot { r } ^ { \prime 2 } \frac { \dot { r } ^ { \prime } } { | \dot { r } ^ { \prime } | }
$$

# Non-gravitational forces: drag

Real satellite is more complicated because not all molecules are absorbed by the satelite,but reflected from its surface,which implies:

- The resulting acceleration must not be precisely anti-parallel to the velocity vector. For the resulting acceleration we introduce an empirical pre-factor C, accounting approximately for the difference between absorbed and reflected molecules.

C may be calculated for special satelites (for spherically symmetric satellites we have $\complement = 2$ ,i.e.,drag is independent of the fraction absorbed/reflected molecules.

The general formula for drag reads as:

$$
- \frac { C } { 2 } \rho ( \pmb { r } ) \frac { A } { m } \pmb { \dot { r } } ^ { \prime 2 } \frac { \pmb { \dot { r } } ^ { \prime } } { | \pmb { \dot { r } } ^ { \prime } | } \mathrm { w h e r e } . 2 \leq C \leq
$$

# Non-gravitational forces: drag

Locally, the density $\rho ( h )$ of the atmosphere may be approximated by the barometric height formula:

$$
\rho ( h ) = \rho _ { 0 } \ e ^ { - \frac { h - h _ { 0 } } { H _ { 0 } } }
$$

$h _ { o }$ is reference height, $H _ { o }$ the scale height.

Even for low eccentricity orbits the difference $h _ { a p o } - h _ { p e r } > > H _ { o }$ ， implying that usually one cannot work with one barometric formula over one revolution of the satellite motion.

Moreover $\rho ( h )$ is latitude- and longitude-dependent and has seasonal and Sun-cycle variations.

Even detailed models do not allow it to introduce drag as a,,known" force.For high-accuracy applications one has to solve at least for a scaling factor.

# Non-gravitational forces: drag

![](images/cf7e5925268d0f63969d9ae48c31a1461ff7ef99a7cf15cce46960fa96cff9cb.jpg)  
CODEGIM time series from 01-Jan-1995 to 03-Jul-2012

Mean electron content in the upper atmosphere as estimated by CODE (Center for Orbit Determination in Europe). Note the length of the most recent solar cycle.

# Non-gravitational forces: drag

![](images/1486fd924d1c5e928326ed866f5abd28d278a23b4c2e423b9137f63d1151caf7.jpg)

Mean atmospheric density from the MSIS-model.   
Drag may be neglected above a height of about 2000 km.

# Non-gravitational forces: drag

Let us use the orbit characteristics of GPS/MET,a test satellite of the mid 1990s to study atmosphere sounding with GPS, to study the impact of drag.

The orbit characteristics and the A/m ratio for GPS/MET are:

Table 3.5. Characteristics of GPS/MET in 1995   

<table><tr><td>Satellite/Orbit Property</td><td>Numerical Value</td></tr><tr><td>a</td><td>7100 km</td></tr><tr><td>e</td><td>0.0</td></tr><tr><td>i</td><td>70°</td></tr><tr><td>A/m</td><td>0.02</td></tr></table>

# Non-gravitational forces: drag

![](images/a05ed02e7abb3957fb937b11865fbdcd29ef815a9106904d25d430d20006f98f.jpg)

Decay of the semi-major -axis a of GPS/MET making different (but realistic) assumptions concerning the atmospheric density. Bottom line: The sm-axis decreases by several m/day.


<!-- chunk 0002: pages 71-80 -->
# Non-gravitational forces: drag

Semi-major axis a

![](images/6b4d56ae8a18bb18fc6792eadfda7765365c904a49282eb015f35dac821ed83d.jpg)

With a n ecce nt ri city of $\scriptstyle \mathtt { e = } 0 .$ 05 i nstead of $e { = } 0 . 0 2$ , t h e s ate l l i te wo u l d have penetrated mo re deeply i nto the atmosphe re and the pe rtu rbation wou ld have been m u ch stronge r!

Fo r sate l l ites with “h ig he r” eccentricities , d rag outside the pe rigee is a l m ost i rre l eva nt .

# Non-gravitational forces: drag

![](images/72551ee90993999b9f3eaf0bfde62f5c29c2f1cc6eac0f7f8f2883d5a3d543a5.jpg)

Decrease of Pe rigee and Apogee of G PS/M ET (with $e { = } O . O 5 )$ over one day:

There perigee barely changes , whereas the apogee decreases by seve ral h u nd red m pe r day!    
O rb its a re g ett i n g m o re ci rcu l a r d u e to d rag .   
D rag cleans the atmosphe re $<$ 1 000 km from LE Os and space debris !

# Non-gravitational forces: rpr

Q uantu m theo ry says that a photon with freq u ency ν and wavelength $\lambda { = } 0 / \nu$ carries an ene rgy $E { = } h \nu$ and a momentu m of $p { = } h { \nu } / c$ e, where $h { = } 6 .$ 62 $1 0 ^ { - 3 4 }$ Js is P lan ck’s constant , e is th e u n it vecto r of p ropagation of the photon .

I n p ract i ce i t i s a d i ff i c u l t tas k to ca l c u l ate t h e t ra n sfe r of m o m e n t u m on sate l l ite with com p l icated shape i n a gene ral rad iation fie ld .

The p ri nci p les u nde rlyi ng the task are , howeve r, si m p le :

– The satel l ite su rface is su bd ivi ded i nto smal l su rface elem e nts . Fo r each su rface eleme nt and fo r each freq uency on e calcu lates the n u m be r of i nci dent photons and the associ ated momentu m . If al l photons a re abso rbed , the resu lti n g momentu m eq u als the su m of al l i nci dent p hoton mome ntu ms . Fo r the fraction of the photons reflected , the resu lti n g mome ntu m is the d iffe rence of the photon momentu ms of al l reflected and al l i ncident photons .

# Non-gravitational forces: rpr

U nde r the fol lowi ng assu m ptions rpr acti ng on a sate l l ite may be calcu lated easi ly:

– The S u n is the on ly rad iation sou rce – The rad iation is assu med to be paral lel at th e satel l ite – The enti re rad i ation is abso rbed by th e satel l ite :

$$
{ \pmb a } _ { \mathrm { r a d } } = \frac { \tilde { C } } { 2 } \frac { A _ { \pm } ^ { 2 } } { | { \pmb r } - { \pmb r } _ { \odot } | ^ { 2 } } \frac { S } { c } \frac { A } { m } \frac { { \pmb r } - { \pmb r } _ { \odot } } { | { \pmb r } - { \pmb r } _ { \odot } | }
$$

Where

S i s t h e s o l a r co n sta n t ( at 1 A U ) ( $=$ i ncident E ne rgy on an area of 1 $m ^ { 2 }$ pe r s no rmal to the d i rection S u n  area) .

A . . I s th e Ast ro n o m i ca l U n it ,   
$r$ is the geocentric position vecto r of the sate l l ite , and   
$\pmb { r _ { \circ } }$ is the geocentric position vecto r of the S u n .   
The facto r wou ld be $\complement = 2$ , if al l photons we re abso rbed . U s ual ly one has $2 < C < 2 . 5$ .

# Non-gravitational forces: rpr

![](images/bd9f2e40cc350afa7c0aa6b2c4df41c6b6154c7c76d421a402c95798bc1d492c.jpg)

Mode l i ng rpr is encu m be red by the fact that rp r has to be switched of, when the sate l l ite ente rs the E arth ’s shadow.

Th e t ra n s iti o n l i g ht $< - >$ shadow is re lative ly rap id . Th is is a p roblem fo r analytical and n u me rical p roced u res .

# Non-gravitational forces: rpr

On the ave rage ove r one revol ution rpr bare ly changes the elements i and Ω (except i n shadow pe riods) .

E ccentricity e and perigee d istance $\omega$ are effected heavi ly. On ly when ave rag i ng ove r the d racon itic year of a particu lar sate l l ite , the i m pact is ave raged out.

Depend i ng on the A/m- ratio ve ry large long-period effects may resu lt. S uch effects occu rred for Space Debris. Pe riod ic changes u p to $\varDelta e = 0 . 7$ occu r.

The d u ration of shadow pe riods heavi ly depends on the orbit characte ristics . U p to half of the o rb it may be i n shadow fo r L E O s ate l l i te s , fo r h i g h - o rb i t i n g s ate l l i te s ( e . g . , g e ostat i o n a ry o r G N SS-type sate l l ites the shadow pe riod is of the orde r of a few pe rce nt of th e revo l uti o n ti m e) .

Fo r G N SS sate l l ites , o rb iti ng the E arth at a he ig ht of about 20 ‘000 km , the maxi m u m shadow d u ration is about one hou r.

# Non-gravitational forces: rpr

![](images/48111a8b3a4d3e4b1d5d1ab04bb2aa530689ff3a1e66009d09bad08d3f69d45c.jpg)

I m pact of rpr on the sm-axis a and on the eccentricity e of a G PSs ate l l i te (ove r t h e p e r i od of o n e ye a r) .

Ave raged ove r one o rbital pe riod the rpr pe rtu rbations i n a are ze ro (except d u ri ng the shadow pe riods) .

The eccentricity e changes smooth ly ove r the year.

# Non-gravitational forces: rpr

Apa rt fro m so l a r (o r d i rect) rpr th e fo l l owi n g effects h ave to be take n i nto accou nt fo r accu rate o rb its :

– rpr d ue to solar rad iation reflected/re-em itted by the E arth (Al bedo- rp r) as we l l as – rpr d ue to solar rad iation reflected/re-em itted by the M oon .

With i n the I G S one has even been ab le to identify (m issi ng) rpr effects d u ri ng l u nar ecl i pses !

I n su m mary one may say that rpr m ust be carefu l ly modeled for LE Os , M EOs , G EOs.

P recise rpr mode l i ng cu rrently is the most i m po rtant accu racy- l i m iti ng effe ct fo r G N S S o rb i ts . I t wo u l d b e i n te rest i n g to s e e a f u t u re generation of G N SS with accele rometers .

# Forces acting satellites in overview

<table><tr><td>Perturbation</td><td>Acceleration</td><td colspan="3">Orbit Error after one Day</td></tr><tr><td></td><td>[m/s²]</td><td>Radial [m]</td><td>Along Track Out ofPlane [m]</td><td>[m]</td></tr><tr><td>-Term</td><td>8.42</td><td>“0”</td><td>“0”</td><td>“8”</td></tr><tr><td>Oblateness</td><td>1.5· 10-2</td><td>60000</td><td>400000</td><td>900000</td></tr><tr><td>Atmospheric Drag</td><td>7.9·10-7</td><td>150</td><td>8900</td><td>1.5</td></tr><tr><td>Higher Terms of the</td><td>2.5: 10-4</td><td>550</td><td>3400</td><td>820</td></tr><tr><td>Earth&#x27;s Grav.Field Lunar Attraction</td><td>5.4·10-6</td><td>2</td><td>45</td><td>2</td></tr><tr><td>Solar Attraction</td><td>5.0·10-7</td><td>1</td><td>38</td><td>15</td></tr><tr><td>Direct Rad.Pressure</td><td>9.7 ·10-8</td><td>10</td><td>24</td><td>0</td></tr><tr><td>Solid Earth Tides</td><td>1.1 · 10-7</td><td>0.2</td><td>13</td><td>1</td></tr><tr><td>y-bias</td><td>1.0· 10-9</td><td>0.1</td><td>4.7</td><td>0.0</td></tr></table>

# LE O O rb its : O rb it e rro rs afte r one day when not taki ng i nto accou nt particu lar pe rtu rbations .

# Forces acting satellites in overview

<table><tr><td>Perturbation</td><td>Acceleration</td><td colspan="3">Orbit Error after one Day</td></tr><tr><td></td><td>[m/s²]</td><td>Radial [m]</td><td>Along Track Out of Plane [m]</td><td>[m]</td></tr><tr><td>-Term</td><td>0.57</td><td>“0”</td><td>“0”</td><td>“0”</td></tr><tr><td>Oblateness</td><td>5.1·10-5</td><td>2750</td><td>32000</td><td>15000</td></tr><tr><td>Lunar Attraction</td><td>4.5· 10-6</td><td>400</td><td>1800</td><td>30</td></tr><tr><td>Solar Attraction</td><td>2·10-6</td><td>200</td><td>1200</td><td>400</td></tr><tr><td>Higher Terms of the</td><td>4.2· 10-7</td><td>60</td><td>440</td><td>10</td></tr><tr><td>Earth&#x27;s Grav.Field Direct Rad.Pressure</td><td>9.7 · 10-8</td><td>75</td><td>180</td><td>5</td></tr><tr><td></td><td>1.0·10-9</td><td></td><td></td><td></td></tr><tr><td>y-bias</td><td>5.0·10-9</td><td>0.9</td><td>8.1</td><td>0.3</td></tr><tr><td>SolidEarth Tides Atmospheric Drag</td><td></td><td>0.0</td><td>0.4</td><td>0.0</td></tr></table>

G N SS O rb its : O rb it e rro rs afte r one day when not taki ng i nto accou nt particu lar pe rtu rbations .
