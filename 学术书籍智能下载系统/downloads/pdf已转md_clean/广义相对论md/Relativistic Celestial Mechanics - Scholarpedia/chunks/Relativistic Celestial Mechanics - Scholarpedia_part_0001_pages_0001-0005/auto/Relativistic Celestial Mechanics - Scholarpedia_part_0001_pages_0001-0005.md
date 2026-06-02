# Relativistic Celestial Mechanics

Victor A. Brumberg (2010), Scholarpedia, 5(8):10669.

doi:10.4249/scholarpedia.10669

Prof. Victor A. Brumberg, Institute of Applied Astronomy RAS (Russia)

Relativistic celestial mechanics (RCM) refers to a science to study the motion of celestial bodies within the framework of general relativity theory (GRT) by Einstein. Being a straightforward successor of Newtonian celestial mechanics RCM embraces all aspects of motion of celestial bodies including (1) physics of motion, i.e. investigation of the physical nature of all effects influencing the motion of celestial bodies and formulation of a physical model for a specific problem; (2) mathematics of motion, i.e. investigation of the mathematical characteristics of the solutions of the differential equations of motion of celestial bodies; (3) computation of motion, i.e. the actual determination of the quantitative characteristics of motion; (4) astronomy of motion, i.e. application of mathematical solution of a problem to a specific celestial body, comparison with the results of observations, determination of initial values and parameters of motion, and checking the physical and mathematical models employed for a given problem.

# Contents

1 Relativistic celestial mechanics and general relativity   
2 Relativistic celestial mechanics vs Newtonian celestial mechanics   
3 Quasi–Galilean coordinates   
4 The Schwarzschild problem   
5 The problem of coordinate–dependent quantities in RCM   
6 The post–Newtonian approximations   
7 The hierarchy of reference systems in RCM   
8 RCM status   
9 References   
10 See also

# Relativistic celestial mechanics and general relativity

The birthdate of relativistic celestial mechanics practically coincides with the birthdate of GRT (1915). Indeed, the solution of the GRT one–body problem (the Schwarzschild problem) and the confirmation of the relativistic advance of the perihelion of Mercury were the first immediate application of GRT to astronomy. The main effect of relativistic astrometry, the gravitational deflection of light by the Sun, was also calculated from the very start of GRT although its experimental confirmation was delayed until 1919. Since then many problems of Newtonian celestial mechanics have been re–formulated and studied within the GRT framework. Just as Newtonian celestial mechanics is indebted to contributions by great mathematicians RCM is indebted to contributions by great physicists including Einstein, Infeld, Fock and many others. By the end of the last century GRT became a working framework for RCM to produce highly accurate dynamical theories and to discuss high–precision observations. Using the well–known saying by Poincare concerning Newtonian celestial mechanics, the final theoretical goal of RCM is to answer the question if GRT alone is capable to explain all observed motions of celestial bodies. So far there are no fixed facts to doubt the role of GRT as the physical foundation of celestial mechanics.

# Relativistic celestial mechanics vs Newtonian celestial mechanics

RCM is based theoretically on Einstein field equations enabling one to determine all compound parts of RCM including time and space characteristics, gravitational field, equations of motion and rotation of bodies as well as equations of light propagation. This logically extremely simple and compact basis of RCM cannot be compared with Newtonian celestial mechanics where all these four parts related to time, space, field equations, and equations of motion are postulated independently of one another.

From the operational point of view RCM differs from its Newtonian counterpart in two aspects, i.e. (1) mathematical structure of the relevant equations of motion, and (2) the manner to compare the solutions of these equations with observations. The first part demands the derivation and solution of the equations of motion and rotation of bodies (dynamical part of a problem) while the second part involves the solution of the equations of light propagation and description of the procedure of observations (kinematical part of a problem). Both parts should be investigated in the same coordinates to exclude unmeasurable coordinate–dependent quantities and to present the results in terms of measurable quantities.

# Quasi–Galilean coordinates

The problem of coordinate–dependent quantities is in fact the main qualitative new problem of RCM. In Newtonian mechanics one can also use curvilinear coordinates (e.g., trying to mathematically facilitate the investigation of the equations of dynamics) but due to the Euclidean character of the Newtonian space it is always possible to convert the results into the inertial coordinates to be regarded as measurable quantities. This is not possible in the pseudo–Riemannian four–dimensional space–time of GRT with the metric

$$
\mathsf { d } \mathsf { s } ^ { 2 } = \mathsf { g } _ { \mathrm { a } \beta } \mathsf { d } \mathsf { x } ^ { \alpha } \mathsf { d } \mathsf { x } ^ { \beta }
$$

with Einstein summation rule over repeated indices, Greek indices taking values 0, 1, 2, 3, Latin indices taking values 1, 2, 3. In the flat space–time of special relativity theory (SRT) the components of the metric tensor take constant values providing Galilean metric

$$
\mathsf { g } _ { \mathtt { a } \mathtt { b } } = \mathsf { \Pi } \mathsf { \Pi } _ { \mathtt { a } \mathtt { b } } , \qquad \mathsf { \Pi } \mathsf { \Pi } _ { 0 0 } = 1 , \mathsf { \Pi } \mathsf { \Pi } _ { \mathtt { 0 } \mathtt { i } } = 0 , \mathsf { \Pi } \mathsf { \Pi } _ { \mathsf { 1 } \mathtt { i } } = - \bar { \mathtt { b } } _ { \mathtt { i } \mathtt { j } } ,
$$

$\bar { \delta } _ { \mathfrak { i } } |$ being the Kronecker symbol (1 for i=j and 0 otherwise). The coordinates providing the Minkowski metric tensor $\boldsymbol \eta _ { \mathrm { a } \beta }$ are called Galilean (inertial coordinates of Newtonian mechanics). Such coordinates cannot be introduced globally in GRT. Instead, it is possible to use in RCM quasi–Galilean coordinates such that

$$
g _ { \mathrm { a \beta } } = \eta _ { \mathrm { a \beta } } + \mathsf { h } _ { \mathrm { a \beta } }
$$

$\hslash _ { \mathsf { a } \beta }$ being functions of coordinates with $\left| \mathsf { h } _ { \mathsf { G } \beta } \right| \ll 1$ The use of such coordinates facilitates the treatment of . practical astronomical problems. The coordinates $\dot { \mathsf { x } } ^ { 0 } , \mathsf { x } ^ { 1 } , \mathsf { x } ^ { 2 } , \mathsf { x } ^ { 3 }$ are treated therewith as being ct , x , y , z , c the light velocity in vacuum, and are considered conventionally as time and spatial coordinates,t x , y , z respectively, without attributing to them any physical meaning.

# The Schwarzschild problem

The simplest example of this kind is the Schwarzschild problem, i.e. the metric of the gravitational field due to one spherical mass The most frequently used quasi–Galilean coordinates for this problem result inM .

$$
\mathsf { o } 0 = - \frac { 2 \mathsf { m } } { \mathsf { r } } + 2 ( 1 - \alpha ) \frac { \mathsf { m } ^ { 2 } } { \mathsf { r } ^ { 2 } } + \ldots , \mathsf { h } _ { 0 \mathrm { i } } = 0 , \mathsf { h } _ { \mathrm { i j } } = - \frac { 2 \mathsf { m } } { \mathsf { r } } [ ( 1 - \alpha ) \delta _ { \mathrm { i j } } + \alpha \frac { \mathsf { x } ^ { \mathrm { i } } \times \mathrm { j } } { \mathsf { r } ^ { 2 } } ] + \ldots |
$$

with $\mathsf { r } ^ { 2 } = \mathsf { x } ^ { \mathrm { i } } \mathsf { x } ^ { \mathrm { i } } \mathsf { \Omega } , \mathsf { m } = \mathsf { G M } / \mathsf { c } ^ { 2 }$ and coordinate parameter to specify the chosen quasi–Galilean coordinates., α The most popular choices are 0 (harmonic coordinates), 1 (standard Schwarzschild coordinates), 2 (Painlevé coordinates), and so on. The solutions of the equations of motion of a test particle and of light propagation depend on demonstrating that the coordinates of a test particle and a photon have nothing to do withα measurable quantities. But in describing the observation procedure for optical or radio observations with the use of these coordinate–dependent solutions the dependence on disappears resulting to measurable effects.α

# The problem of coordinate–dependent quantities in RCM

There are three main possibilities to overcome the problem of coordinate–dependent quantities in RCM:

1. to avoid coordinates completely by constructing the solutions for the solar system body motion and light propagation in terms of measurable quantities alone (involving the removal of all coordinate–dependent quantities from the system of astronomical constants);   
2. to use any coordinates to solve dynamical problems and to describe observational procedures, provided that one and the same coordinates be used for both the dynamics and kinematics of a specific problem;   
3. to forget about the GRT arbitrariness in the coordinate conditions and to adopt one specific type of coordinates for RCM and relativistic astrometry once and forever.

In 1991 IAU (International Astronomical Union) adopted a third way, recommending the use of the harmonic coordinates (harmonic coordinates are determined by four specific non–tensorial differential relations to be added to the GRT tensorial field equations). This third option greatly simplifies the use of GRT in practical problems of ephemeris astronomy demanding high–level standardization.

# The post–Newtonian approximations

The most common tools of modern RCM are PNA (post–Newtonian approximation) expansions, EIH (Einstein– Infeld–Hoffman) equations of motion in the N–body problem and relativistic hierarchy of reference systems including relativistic time scales. For the N–body problem the GRT field equations are solved by means of the PNA expansions

$$
\mathsf { h } _ { 0 0 } = \mathsf { c } ^ { - 2 } \mathsf { h } _ { 0 0 } ^ { ( 2 ) } + \mathsf { c } ^ { - 4 } \mathsf { h } _ { 0 0 } ^ { ( 4 ) } + \mathsf { c } ^ { - 5 } \mathsf { A } _ { 0 0 } ^ { ( 5 ) } + \mathsf { c } ^ { - 6 } \mathsf { h } _ { 0 0 } ^ { ( 6 ) } + \mathsf { c } ^ { - 7 } \mathsf { A } _ { 0 0 } ^ { ( 7 ) } + \mathsf { O } ( \mathsf { c } ^ { - 8 } ) , \mathsf { I } ,
$$

$$
\mathsf { h } _ { 0 \mathsf { i } } = \mathsf { c } ^ { - 3 } \mathsf { h } _ { 0 \mathsf { i } } ^ { ( 3 ) } + \mathsf { c } ^ { - 5 } \mathsf { h } _ { 0 \mathsf { i } } ^ { ( 5 ) } + \mathsf { c } ^ { - 6 } \mathsf { A } _ { 0 \mathsf { i } } ^ { ( 6 ) } + \mathsf { O } ( \mathsf { c } ^ { - 7 } ) ,
$$

$$
\mathsf { h } _ { \mathsf { i } \mathsf { j } } = \mathsf { c } ^ { - 2 } \mathsf { h } _ { \mathsf { i } \mathsf { j } } ^ { ( 2 ) } + \mathsf { c } ^ { - 4 } \mathsf { h } _ { \mathsf { i } \mathsf { j } } ^ { ( 4 ) } + \mathsf { c } ^ { - 5 } \mathsf { A } _ { \mathsf { i } \mathsf { j } } ^ { ( 5 ) } + \mathsf { O } ( \mathsf { c } ^ { - 6 } ) .
$$

The $\mathsf { A } _ { \mu \nu }$ terms are due to gravitational radiation of the $\mathbf { N } .$ –body system presenting a qualitative difference from the Newtonian N–body problem. Such advanced expansions are needed in studying the motion in a strong gravitational field (e.g., the gravitational radiation in a binary pulsar problem, the motion of a test particle in the gravitational field of a binary pulsar, etc.).

Newtonian approximation up to the terms inclusively. This accuracy corresponds to the h , , , (4) 00 h (3) 0i h (2) ij presently used EIH equations of motion to study the motion of the solar system bodies in RCM. Moreover, as was shown long ago by Infeld, eventhe GRT field equations. It mea $\mathsf { h } _ { 0 0 } ^ { ( 4 ) }$ is not needed to derive the EIH equations frat the linearized GRT metric with the terms principle for is sufficient to $\mathsf { h } _ { 0 0 } ^ { ( 2 ) } , \mathsf { h } _ { 0 \mathrm { i } } ^ { ( 3 ) } , \mathsf { h } _ { \mathrm { i j } } ^ { ( 2 ) } ,$ treat the problems of motion and rotation of the solar system bodies within present (i.e. post-Newtonian) level of accuracy.

# The hierarchy of reference systems in RCM

The EIH equations are derived in a barycentric (with respect to the solar system) reference system (BRS). The four–dimensional reference (coordinate) system (RS) is given in RCM by a metric form. A BRS is quite adequate for description of the solar system bodies considered as point masses. For treating the problems related with the proper rotation of a planet and the motion of its satellites a corresponding planetocentric RS may be more suitable. To treat observations made from the surface of a planet or from its satellite the third RS with a spatial origin at the point of observation (point of the surface of a planet or its satellite) may be very useful. Thus, in application to the Earth one gets three-level hierarchy BRS, GRS (geocentric RS) and TRS or SRS (topocentric or satellite RS) interrelated by four–dimensional space–time transformations generalizing the Lorentz transformation for inertial systems of SRT. GRS is suitable to study the motion of the Moon and Earth’s artificial satellites whereas TRS or SRS are suitable for describing an observation procedures. For example, the coordinate time of TRS or SRS at the spatial origin of these RSs coincides with the proper time of an observer at this spatial point enabling one to relate coordinate times of BRS and GRS with the measurable proper time of an observer.

Generally speaking, it is possible to use any coordinates in constructing a RS in RCM. But at the same time for each specific problem there may exist a RS dynamically adequate for solving this problem. For example, the dynamical adequacy of GRS, TRS and SRS means that the influence of the external masses manifests in these systems as the tidal terms (plus the linear terms due to the non–geodesic acceleration of the motion of the RS origin) vanishing at the spatial origins of these RSs. There are two main advantages in using dynamically adequate RSs. First, the coordinate–dependent solutions in these RSs do not contain extra large terms caused by the inadequate choice of RSs. For example, the BRS relativistic perturbations in the problem of the Earth’s rotation and the Moon’s motion contain the small parameter of the order $1 0 ^ { - 8 }$ while the GRS relativistic perturbations for the same problems contain the small parameter of the order $1 0 ^ { - 1 0 }$ Second, the physical. characteristics of a non–point celestial body related with its figure and proper rotation should be expressed just in a body–related system. These factors make a relativistic hierarchy of RSs one of the most efficient tools to treat the RCM problems. It does not mean that local RS treating enables one to get the measurable effects. This goal is achieved by relativistic reduction of observations in local RS but this reduction deals with the quantities of much lesser magnitude than in the global RS reduction.

# RCM status

The main problems of contemporary RCM are concerned with the motion of the major planets and the Moon as well as the Earth’s rotation. The techniques of RCM are also required for objects outside the solar system, e.g. the motion of binary pulsars. Space research is becoming an important applied area of RCM. RCM is also used to test various alternative gravitation theories and empirical models with parameters that must be determined from observations (PPN formalism). In this respect, the present situation resembles the numerous attempts in the past to modify the laws of gravitation. Occasionally modern results seem to conflict with RCM, just as they have in the past. Such cases demand a thorough investigation of all physical aspects of the problem before claiming any disagreement between theory and observation.

Interested readers will find more profound insight into RCM from the bibliography and references below.

# References

Brumberg V.A.: Relativistic celestial mechanics on the verge of its 100 year anniversary (Brouwer Award lecture). Cel. Mech.&Dyn. Astron., 106, 209–234, 2010 (DOI 10.1007/s10569-009-9237-y).   
Infeld L., Plebanski J.: Motion and Relativity. Pergamon Press, N.Y. (1960)   
Soffel M., Klioner S.A., Petit G., Wolf P., Kopeikin S.M. et al.: The new IAU 2000 resolutions for astrometry, celestial mechanics and metrology in the relativistic framework: explanatory supplement. Astron. J. 126, No. 6, 2687–2706 (2003)

# Internal references

Norbert Zacharias (2010) Astrometry. Scholarpedia, 5(2):5267.   
Sylvio Ferraz-Mello (2009) Celestial mechanics. Scholarpedia, 4(1):4416.   
James Meiss (2007) Dynamical systems. Scholarpedia, 2(2):1629.

# See also

Soffel M.: Relativity in Astrometry, Celestial Mechanics and Geodesy, Berlin, Springer (1989) Special relativity , General relativity

Sponsored by: Prof. Alessandra Celletti, Dipartimento di Matematica, Universita' di Roma (Tor Vergata), Italy Reviewed by (//www.scholarpedia.org/w/index.php?title $: =$ Relativistic_Celestial_Mechanics&oldid $\equiv$ 79537) : Anonymous

Accepted on: 2010-08-02 18:23:45 GMT (//www.scholarpedia.org/w/index.php? title $: =$ Relativistic_Celestial_Mechanics&oldid $. =$ 79537)

Categories: Celestial mechanics Space-Time and Gravitation Physics General relativity Astrophysics

This page was last modified on 28 October 2013, at 14:08.   
This page has been accessed   
46,042 times.   
"Relativistic Celestial Mechanics" by Victor A. Brumberg is licensed under a Creative Commons   
Attribution-NonCommercial-  
ShareAlike 3.0 Unported License. Permissions beyond the scope of this license are described in the Terms of Use