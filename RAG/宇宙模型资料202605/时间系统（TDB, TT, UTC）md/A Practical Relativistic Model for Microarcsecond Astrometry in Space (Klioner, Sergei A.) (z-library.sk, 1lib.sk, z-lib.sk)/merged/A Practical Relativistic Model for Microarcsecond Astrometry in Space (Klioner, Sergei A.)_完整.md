<!-- source: A Practical Relativistic Model for Microarcsecond Astrometry in Space (Klioner, Sergei A.) (z-library.sk, 1lib.sk, z-lib.sk).pdf -->

<!-- pdf_type: normal; pages: 18; chunk_pages: 70 -->


<!-- chunk 0001: pages 1-18 -->
# A PRACTICAL RELATIVISTIC MODEL FOR MICROARCSECOND ASTROMETRY IN SPACE

Sergei A. Klioner Lohrmann-Observatorium, Institut fu¨r Planetare Geoda¨sie, Technische Universita¨t Dresden, Mommsenstrasse 13, D-01062 Dresden, Germany; klioner@rcs.urz.tu-dresden.de Received 2001 September 12; accepted 2002 November 25

# ABSTRACT

We develop a practical model for relativistic reduction of positional observations with an accuracy of 1 las, which is expected to be attained in future space astrometry missions. All relativistic effects that are caused by the gravitational field of the solar system and are of practical importance for this accuracy level are thoroughly calculated and discussed. The model includes relativistic modeling of the motion of the observer and modeling of relativistic aberration and gravitational light deflection, as well as a relativistic treatment of parallax and proper motion suitable for the accuracy of 1 las. The model is formulated both for remote sources (stars, quasars, etc.) and for solar system objects (asteroids, etc.). The suggested model is formulated within the framework of the parameterized post-Newtonian formalism, with parameters $\beta$ and $\gamma$ . However, for general relativity $\beta = \gamma = 1$ ) the model is fully compatible with the year 2000 IAU resolutions on relativity in celestial mechanics, astrometry, and metrology. The model is presented in a form suitable for implementation in a software system for data processing or simulation. The changes that should be applied to the model to attain an accuracy of 0.1 las are reviewed. Potentially important relativistic effects caused by additional gravitational fields that are generated outside of the solar system are also briefly discussed.

Key words: astrometry — reference systems — relativity

# 1. INTRODUCTION

Within the next decade, the accuracy of space-based astrometric positional observations is expected to attain a level of 1 microarcsecond (las). The problem of relativistic modeling of positional observations with microarcsecond accuracy has become quite a practical one recently, with a number of astrometric space projects having been approved by NASA, ESA, and other boards and selected for launch in the next several years: the Global Astrometric Interferometer for Astrophysics (GAIA; ESA 2000; Perryman et al. 2001; Bienayme´ & Turon 2002) and the Space Interferometry Mission (SIM; Shao 1998), for example. Following this practical trend, this paper describes a practical relativistic model of space-based positional observations that is valid at a level of 1 las and can be readily implemented in the corresponding software.

Relativistic effects in positional observations have been studied by many authors in many different aspects. Needless to say, the deflection of light in the gravitational field of the Sun, being one of the most important constituents of the relativistic model of positional observations, was one of the first experimental tests of general relativity. By the time of Hipparcos, it was already realized that relativity must play an important role in the formulation of the transformation between the observed positions of a star and what should be included in the resulting catalog (Walter et al. 1986). However, it was a relatively uncomplicated task to formulate such a transformation for Hipparcos, which was aimed at a final accuracy of 1 mas. A model of positional observations suitable for an accuracy of 1 las is much more intricate. It is clear, since in this case typical relativistic effects exceed the required accuracy by several orders of magnitude, that the whole concept of the modeling should be reformulated in the framework of general relativity. Besides, at such a high level of accuracy many additional, more subtle relativistic effects should be taken into account.

The first complete general relativistic model of positional observations at the microarcsecond level of accuracy was formulated by Klioner & Kopeikin (1992). That work was stimulated by POINTS, an early project for microarcsecond astrometry in space (Reasenberg et al. 1988). The model was formulated in a rather general form and was primarily intended for a satellite on a geocentric orbit (geostationary or lower). The model described in this paper is based on the same general post-Newtonian approximation scheme used in the model of Klioner & Kopeikin, but it differs from the latter in several important aspects: (1) the Geocentric Celestial Reference System (see below) is used only as an intermediate reference system to model Earth-based observations of the satellite itself (orbit determination) and not to process the astrometric observations produced by the satellite; (2) the model contains a refined treatment of several relativistic effects (primarily aberration and some subtle effects in the gravitational light deflection); (3) the model is formulated in the framework of the so-called parameterized post-Newtonian (PPN) formalism (Will 1993), which makes it possible to use the positional observations to test the general theory of relativity; (4) the present model is suitable both for remote sources located outside of the solar system and for solar system objects, the coupling between the finite distance to the object and the gravitational light deflection being properly treated; (5) the model is supplemented with a set of simple formulae allowing one to judge whether a particular gravitational light deflection effect due to a particular gravitating body must be taken into account or can be neglected for a particular mutual disposition of the source, the observer, and the gravitating body; and (6) the model is optimized and simplified as much as possible for the target accuracy of 1 las, which makes it straightforward to implement the model in the corresponding software.

Since practical interest in microarcsecond astrometry was revived in recent years, a number of numerical simulations of astrometric missions have appeared. De Felice et al.

1998, 2000, 2001) used a simplified relativistic model (the Schwarzschild field of the Sun) in an end-to-end simulation of the $G A I A$ mission to demonstrate its capability and investigate various statistical properties of the solution in different cases. Simulations based on more realistic models are in progress (Kopeikin et al. 2000; de Felice et al. 2001). The model represented in this paper can be used to facilitate further investigations of this kind.

It is clear that the model given below is not all that is needed for practical processing of the data produced by an astrometric satellite such as GAIA (or for corresponding data simulations). The full model of observables should contain not only the idealized relativistic part given below, but also a detailed instrumental model describing observables from the ‘‘ technical ’’ point of view. The ‘‘ technical ’’ model heavily depends on the particular design of the satellite and should relate theoretical ‘‘ observable direction ’’ toward a source to the technical observational data provided by the particular satellite design. This ‘‘ technical ’’ model may contain parameters of the satellite’s hardware, various calibration parameters, parameters describing the attitude of the satellite, etc. Besides that, the mathematical and statistical details of the data processing of the future astrometric missions represent an important research topic in itself. All these aspects of practical data processing are beyond the scope of the present paper.

Let us summarize the most important notation used throughout the paper:

1. $G$ is the Newtonian constant of gravitation. 2. The velocity of light is $c$ . 3. The quantities $\beta$ and $\gamma$ are the parameters of the PPN   
formalism that characterize possible deviations of physical   
reality from general relativity theory ( $\beta = \gamma = 1$ in general   
relativity). 4. Lowercase latin indices $i , j , k , \dots$ , take values 1, 2, 3. 5. The lowercase latin indices are lowered and raised by   
means of the unit matrix $\delta _ { i j } = \delta ^ { i j } = \mathrm { d i a g } ( 1 , 1 , 1 ) .$ , and there  
fore the disposition of such indices plays no role: $a ^ { i } = a _ { i }$ . 6. Repeated indices imply the Einsteinian summation   
convention irrespective of their positions (e.g., $a ^ { i } b ^ { i } =$   
$a ^ { 1 } b ^ { 1 } + a ^ { 2 } b ^ { 2 } + a ^ { 3 } \hat { b ^ { 3 } } )$ . 7. A dot over any quantity designates the total derivative   
with respect to the coordinate time of the corresponding   
reference system (e.g., $\dot { \boldsymbol { a } } = d \boldsymbol { a } / d t )$ ). 8. The three-dimensional coordinate quantities (‘‘ 3-   
vectors ’’) referred to the spatial axes of the corresponding   
reference system are set in boldface italic: $\mathbf { a } = a ^ { i }$ . 9. The absolute value (Euclidean norm) of a 3-vector $\pmb { a }$   
is denoted $| \pmb { a } |$ and can be computed as $| \pmb { a } | = ( a ^ { 1 } a ^ { 1 } +$   
$a ^ { 2 } a ^ { 2 } + a ^ { 3 } a ^ { 3 } ) ^ { \dot { 1 } / 2 }$ . 10. The scalar product of any two 3-vectors $\mathbf { \pmb { a } }$ and $\pmb { b }$ with   
respect to the Euclidean metric $\delta _ { i j }$ is denoted by ${ \pmb a } \cdot { \pmb b }$ and can   
be computed as $\mathbf { \delta } a \cdot \mathbf { \delta } b = \delta _ { i j } a ^ { i } b ^ { j } = { \overset { , } { a ^ { i } b ^ { i } } }$ . 11. The vector product of any two 3-vectors $\mathbf { \pmb { a } }$ and $\pmb { b }$   
is designated by $\mathbf { \nabla } _ { \mathbf { \mu } \mathbf { \Lambda } } ^ { a \times b }$ and can be computed as   
$( { \pmb a } \times { \pmb b } ) ^ { i } = \epsilon _ { i j k } a ^ { j } b ^ { k }$ , where $\epsilon _ { i j k } = ( i - j ) ( j - k ) ( k - \bar { i } ) / 2$ is the   
fully antisymmetric Levi-Civita symbol. 12. The capital subscripts $A , B , C , \ldots ( = 1 , \ldots , N )$ , refer   
to the gravitating bodies of the solar system; as a special   
case, subscript E designates quantities related to Earth. 13. The subscript $o$ denotes quantities related to the   
observer (satellite): for example, $x _ { o }$ denotes the position of   
the observer and $t _ { o }$ is the coordinate time of observation   
with respect to the Barycentric Celestial Reference System   
(BCRS) of the IAU (see below). 14. The subscript $p$ denotes quantities related to the light   
ray (photon): for example, $\boldsymbol { x } _ { p } ( t )$ denotes the BCRS position   
of the light ray at some moment of time $t$ . 15. The subscript $s$ denotes quantities related to the   
source: for example, $\mathbf { x } _ { s }$ denotes the BCRS position of the   
source. 16. The subscript $e$ denotes quantities related to the   
moment of emission of the light ray by the source: for ex  
ample, $t _ { e }$ is the BCRS coordinate time of emission of the   
signal by the source.

Section 2 is devoted to a general scheme of relativistic modeling of astronomical observations of any kind in the framework of general relativity or the PPN formalism. The overall structure of the specific modeling scheme for positional observations made from a space station is described in $\ S \ S$ . Modeling of the motion of the observer (satellite) and that of its proper time are discussed in $\ S 4$ . Section 5 deals with the relativistic description of aberration. Gravitational light deflection is discussed in $\ S 6$ . Parallax and proper motion are analyzed in $\ S \ S 7$ and 8, respectively. Section 9 summarizes the suggested relativistic model. Section 10 contains a short discussion of the changes that should be applied to the model to attain an accuracy of 0.1 las. In $\ S 1 1$ , several known relativistic effects beyond the given model are described.

# 2. GENERAL SCHEME OF RELATIVISTIC MODELING OF ASTRONOMICAL OBSERVATIONS

Let us first outline the general principles of relativistic modeling of astronomical observations. The general scheme is represented in Figure 1. Starting from the general theory of relativity, any other metric theory of gravity, or the PPN formalism, one should define at least one relativistic fourdimensional reference system covering the region of spacetime where all the processes constituting the particular kind of astronomical observation are located. The typical astronomical observation depicted in Figure 2 has four constituents: motion of an observer, motion of an observed object, light propagation, and the process of observation. Each of these four constituents should be modeled in the relativistic framework. The equations of motion of both the observed object and the observer relative to the chosen reference system should be derived, and a method to solve these equations should be found. Typically, the equations of motion are second-order ordinary differential equations, and numerical integration with suitable initial or boundary conditions can be used to solve them. Astrometric information on the object can be read off the electromagnetic signals propagating from the object to the observer. Therefore, the corresponding equations of light propagation relative to the chosen reference system should be derived and solved. The equations of motion of the object and the observer and the equations of light propagation enable one to compute positions and velocities of the object, observer, and the photon (light ray) with respect to the particular reference system at a given moment of its coordinate time, provided that the positions and velocities at some initial epoch are known. However, these positions and velocities obviously depend on the reference system used. On the other hand, the results of observations cannot depend on the reference system used to theoretically model the observations. Therefore, it is clear that one more step in the modeling is needed: a relativistic description of the process of observation. This part of the model allows one to compute a coordinate-independent theoretical prediction of the observables starting from the coordinate-dependent position and velocity of the observer and, in some cases, the coordinate velocity of the electromagnetic signal at the point of observation.

![](images/dead2f342b813e80587d4d5d3af665abb01c47b8175e9fbccdfabce9b967865e.jpg)  
Fig. 1.—General principles of relativistic modeling of astronomical observations

![](images/61337eedde7212bdb187e3edb88e17cf1db1d12204f9d0a06c3907fdb4f3baa6.jpg)  
Fig. 2.—Four constituents of an astronomical event: (1) motion of the observed object, (2) motion of the observer, (3) propagation of an electromagnetic signal from the observed object to the observer, and (4) the process of observation.

Mathematical techniques to derive the equations of motion of the observed object and the observer, to formulate the equations of light propagation, and to find the description of the process of observation in the relativistic framework are well known and will be discussed below. These three parts can now be combined into relativistic models of observables. The models give an expression for each observable under consideration as a function of a set of parameters. These parameters can then be fitted to observational data using some kind of parameter estimation scheme (e.g., least squares or other estimators). The sets of certain estimated parameters appearing in the relativistic models of observables represent astronomical reference frames.

Note that a reference system is a purely mathematical construction (a chart) giving ‘‘ names ’’ to spacetime events.

In contrast, a reference frame is some materialization of a reference system. In astronomy, the materialization is usually realized in a form of a catalog (or ephemeris) containing positions of some celestial objects relative to the reference system under consideration. Any reference frame (a catalog, an ephemeris, etc.) is defined only through the reference system or systems used to construct physical models of observations.

It is very important to understand at this point that the relativistic models contain parameters that are defined only in the chosen reference system or systems and are thus coordinate dependent. A good example of such coordinatedependent parameters are the coordinates and velocities of various objects (e.g., major planets or the satellite) at some epoch. On the other hand, from the physical point of view any reference system covering the region of spacetime under consideration can be used to describe physical phenomena within that region, and we are free to choose the reference system to be used to model the observations. However, reference systems in which the mathematical description of physical laws is simpler than in others are more convenient for practical calculations. Therefore, one can use the freedom to choose the reference system to make the parameterization as convenient and reasonable as possible (e.g., one prefers the parameters to have a simpler time dependence).

For modeling of physical phenomena localized in some sufficiently small region of space (e.g., in the vicinity of a massless observer or a gravitating body), one can construct a so-called local reference system in which the gravitational influence of the outer world is effaced as much as possible in accordance with the Einstein equivalence principle. In the local reference system of a material system, the gravitational field of the outer matter manifests itself in the form of a tidal gravitational potential. First, the solar system as a whole can be considered as a single body, and a reference system can be constructed in which the gravitational influence of the matter situated outside of the solar system can be described by a tidal potential. That tidal potential (mainly due to the influence of the Galaxy) is utterly small and can then be neglected for most purposes. Such a reference system is often called a barycentric reference system of the solar system. It can be used far beyond the solar system and is suitable to describe the dynamics of the solar system (motion of planets and spacecraft relative to the barycenter of the solar system), as well as to model the influence of the gravitational field of the solar system on the light rays propagating from remote sources to an observer. Second, the corresponding local reference system can be constructed for Earth. Such a geocentric reference system is convenient for modeling the geocentric motion of Earth satellites, the rotational motion of Earth itself, etc. The underlying theory and technical details concerning local reference systems have been discussed in a series of papers by Brumberg and Kopeikin (Kopeikin 1988; Brumberg & Kopeikin 1989a, 1989b; Brumberg 1991; see also Klioner & Voinov 1993), and by Damour, Soffel, & Xu (1991, 1992, 1993, 1994). The IAU (2001) has recently recommended the use of a particular form of the barycentric and local geocentric reference systems for the modeling of astronomical observations. These two standard relativistic reference systems are called the Barycentric Celestial Reference System (BCRS) and the Geocentric Celestial Reference System (GCRS). The coordinate time $t$ of the BCRS is called Barycentric Coordinate Time, or TCB. The coordinate time $T$ of the GCRS is called Geocentric Coordinate Time, or

TCG. According to the IAU notation, throughout this paper the spatial coordinates of the BCRS will be designated $\mathbf { \nabla } _ { \mathbf { x } }$ and those of the GCRS as $X$ .

Both the Brumberg-Kopeikin and Damour-Soffel-Xu theories are based on Einstein’s general relativity theory. It is clear, however, that one of the important goals of the future astrometric missions will be to test general relativity. The model presented in this paper will be given in the framework of the PPN formalism (see, e.g., Will 1993) including two main parameters $\beta$ and $\gamma$ , which characterize possible deviations of physical reality from general relativity. Both parameters are equal to unity in general relativity. A theory of local reference systems with parameters $\beta$ and $\gamma$ has been constructed by Klioner & Soffel (1998b, 2000). Both that theory of local PPN reference systems and the model given in the present paper are constructed in such a way that for $\beta = \gamma = 1$ , all the formulae coincide with those that can be derived directly from the general relativistic versions of the BCRS and GCRS recommended by the IAU (2001).

# 3. GENERAL STRUCTURE OF THE RELATIVISTIC MODEL OF POSITIONAL OBSERVATIONS

The relativistic model of positional observations relates the observed direction of the light coming from a source to the coordinates of that source at the moment of emission. A set of the coordinate directions toward the source for different moments of time can then be used to obtain further parameters of the source describing its spatial position and spatial motion with respect to the BCRS (parallax and proper motion or barycentric orbital elements). It is convenient to divide the conversion of the observed directions into the coordinate ones into several steps. Let us introduce five vectors that will be used below: $\pmb { S }$ is the unit observed direction (the word ‘‘ unit ’’ means here and below that the formally Euclidean scalar product $s \bullet s = s ^ { i } s ^ { i }$ is equal to unity), $\pmb { n }$ is the unit tangent vector to the light ray at the moment of observation, $\pmb { \sigma }$ is the unit tangent vector to the light ray at $t = - \infty$ , $\pmb { k }$ is the unit coordinate vector from the source to the observer, and $\iota$ is the unit vector from the barycenter of the solar system to the source (see Fig. 3). Note that the last four vectors are defined formally in the coordinate space of the BCRS and should not be interpreted as ‘‘ Euclidean ’’ vectors in some ‘‘ Newtonian physical space.’’ For the same physical situation, these vectors are different if different reference systems are used instead of the BCRS. The word ‘‘ vector ’’ is used here to refer to a set of three real numbers defined in the coordinate space of the BCRS, rather than to a geometric object. A slightly different meaning of $\pmb { S }$ is discussed in $\ S 5$ below.

Apart from the modeling of the motion of the observer, which will be considered in the next section, the model consists in subsequent transformations of these five vectors. Namely, the following effects should subsequently be considered:

Aberration (effects related to the motion of the observer with respect to the barycenter of the solar system).—This converts the observed direction to the source $\pmb { S }$ into the unit BCRS coordinate direction of the light ray $\pmb { n }$ at the point of observation.

Gravitational light deflection for the source at infinity.— This step converts $\pmb { n }$ into the unit direction of propagation $\pmb { \sigma }$ of the light ray infinitely far from the solar system for $t \to - \infty$ .

![](images/b4ec83122b9dab90390e4524589f9283688aa1c08c8073a8d83add151cf840d0.jpg)  
Fig. 3.—Five principal vectors used in the model: $s , n , \sigma , k$ , and $\iota .$ See text for further details.

Coupling of the finite distance to the source and the gravitational light deflection in the gravitational field of the solar system.—This step converts $\pmb { \sigma }$ into the unit BCRS vector $\pmb { k }$ going from the source to the observer (note that, as discussed below, this step should be combined with the previous one for sources situated within the solar system).

Parallax.—This step converts $\pmb { k }$ into the unit vector l going from the barycenter of the solar system to the source.

Proper motion.—This step provides a reasonable parameterization of the time dependence of l caused by the motion of the source with respect to the BCRS.

All these steps will be specified in detail in the following sections. However, let us first clarify the question of timescales that should be used in the model. There are four timescales that appear:

1. Proper time of the observer (satellite), $\tau _ { o ; . }$ 2. Proper time of the ith tracking station, $\stackrel { o } { \tau _ { \mathrm { s t a t i o n } } ^ { ( i ) } }$ ; 3. Coordinate time $t = \mathrm { T C B }$ of the BCRS [alternatively, a scaled version of TCB called TDB can be used: $\mathrm { T D B } = ( 1 - { \cal L } _ { B } ) \mathrm { T C B }$ , with the current best estimate of the scaling constant $L _ { B } \approx ( 1 . 5 5 0 5 1 9 7 6 7 7 2 \times 1 0 ^ { - 8 } ) \pm$ $( 2 \times 1 0 ^ { - 1 7 } )$ (Irwin & Fukushima 1999; IAU 2001)]; and 4. Coordinate time $T = \mathrm { T C G }$ of the GCRS [alternatively, a scaled version of TCG called TT can be used: $\mathrm { T T } = ( 1 - L _ { G } ) \mathrm { T C G }$ , $L _ { G } \equiv 6 . 9 6 9 2 9 0 1 3 4 \times 1 0 ^ { - 1 0 }$ being a defining constant (IAU 2001)].

It is clear that the observational data (e.g., in the case of the scanning satellites such as Hipparcos, GAIA, and DIVA, these are the projections of the vector $\pmb { S }$ on a local reference system of the satellite that rotates together with the satellite) are parameterized by the proper time of the satellite $\tau _ { o }$ . It is also clear that the final catalog containing positions, parallaxes, and proper motions of the sources relative to the BCRS should be parameterized by TCB. Thetimescales (proper times of the tracking stations $\tau _ { \mathrm { s t a t i o n } } ^ { ( i ) }$ twoand TCG) are used exclusively for orbit determination.

The transformation between the proper time of the satellite $\tau _ { o }$ and TCB can be done by integrating the equation

$$
{ \frac { d \tau _ { o } } { d t } } = 1 - { \frac { 1 } { c ^ { 2 } } } \left[ { \frac { 1 } { 2 } } \dot { \pmb x } _ { o } ^ { 2 } + w ( { \pmb x } _ { o } ) \right] + { \cal O } ( c ^ { - 4 } ) ,
$$

where $x _ { o }$ and $\dot { \mathbf { x } } _ { o }$ are the BCRS position and velocity of the satellite and $w ( \pmb { x } _ { o } )$ is the gravitational potential of the solar system, which can be approximated by

$$
w ( \mathbf { x } _ { o } ) \approx \sum _ { A } \frac { G M _ { A } } { | \boldsymbol { r } _ { o A } | }
$$

with $\pmb { r } _ { o A } = \pmb { x } _ { o } - \pmb { x } _ { A }$ , $M _ { A }$ the mass of body $A$ , and ${ \pmb x } _ { A } = { \pmb x } _ { A } ( t )$ its barycentric position. Both higher order multipole moments of all the bodies and additional relativistic terms are neglected in equation (2). The transformation between the proper time of a tracking station and TCG can be performed in a similar way. The transformation between TCG and TCB is given by IAU Resolutions B1.3 (general post-Newtonian expression) and B1.5 (an expression for an accuracy of $5 \times 1 0 ^ { - 1 8 }$ in rate and $0 . 2 \mathrm { p s }$ in the amplitude of periodic effects) in IAU (2001). There are several analytical and numerical formulae for the position-independent part of the transformation (see, e.g., Fukushima 1995; Irwin & Fukushima 1999; references therein).

Although the use of the relativistic timescales described above is indispensable from the theoretical and conceptual points of view, from a purely practical point of view considerations of accuracy can be used here to simplify the model. However, this depends on the particular parameters of the mission and will be not analyzed here. In the following, it is assumed that the observed directions $\pmb { S }$ are given together with the corresponding epochs of observation $t _ { o }$ on the TCB scale.

# 4. MOTION OF THE SATELLITE

It is well known that in order to compute the Newtonian aberration with an accuracy of 1 las, one needs to know the velocity of the observer with an accuracy of ${ \sim } 1 0 ^ { - 3 } \mathrm { ~ m ~ } \mathrm { s } ^ { - 1 }$ (see, e.g., ESA 2000). This is a rather stringent requirement, and special care must be taken to attain such accuracy. Modeling of the satellite’s motion with such accuracy is a difficult task involving complicated equations of motion that take into account various nonrelativistic (Newtonian $N -$ -body force, radiation pressure, active satellite thrusters, etc.) and relativistic effects. Here a general recipe concerning the relativistic part of the modeling will be given. Both the nonrelativistic parts of the model and a detailed study of the relativistic effects in the satellite’s motion are beyond the scope of the present paper.

In the relativistic model of positional observations developed in the following sections, it is assumed that the observations are performed from a space station or an Earth satellite whose position $x _ { o }$ relative to the BCRS is known for any moment of barycentric coordinate time t. For satellites whose orbits are not located in the vicinity of Earth (this is the case for both $G A I A$ and SIM), it is advantageous to model their motion directly in the BCRS. Since the mass of the satellite is too small to noticeably affect the motion of other bodies of the solar system, the equations of geodetic motion in the BCRS can be used as equations of motion of the satellite. It is sufficient (at least in the relativistic part of the equations) to neglect the multipole structure of the gravitating bodies, as well as the gravitational field produced by the rotational motion of these bodies. Therefore, considering a system of $N$ bodies, each of which can be characterized by position $x _ { A }$ , velocity ${ \dot { \mathbf { x } } } _ { A }$ , and mass $M _ { A }$ , the equations of motion of the satellite read

$$
\begin{array} { r l } { \varepsilon _ { x } , } \\ { d t ^ { ( 2 ) } } \\ { d t ^ { ( 4 ) } } \\ { = } & { - \displaystyle \sum _ { s } \delta \bar { d } u _ { s } \frac { P _ { x , s } ( u _ { s } ) } { | u _ { s } | ^ { 2 } } + \frac { 1 } { s ^ { 2 } } \sum _ { s } \bar { d } u _ { s } \frac { P _ { x , s } ( u _ { s } ) } { P _ { x , s } ( u _ { s } ) } } \\ & { \times \left( | 2 \delta - \bar { d } \cdot \frac { 1 } { s ^ { 2 } } - \frac { 1 } { s ^ { 2 } } - \frac { \bar { d } \cdot N } { s ^ { 2 } } | u _ { s } | ^ { 2 } \right) \frac { \bar { d } \bar { d } u _ { s } } { P _ { x , s } ( u _ { s } ) } } \\ & { \quad + \frac { 1 } { s ^ { 2 } } \frac { \bar { d } ( \varepsilon _ { x } - \varepsilon _ { x } ) - \frac { 1 } { s } } { | u _ { s } | ^ { 2 } } - \frac { 1 } { 2 s ^ { 2 } } \frac { \bar { d } ( \varepsilon _ { x } ) \bar { d } u _ { s } \bar { d } \bar { d } u _ { s } ^ { ( 2 ) } } { | u _ { s } | ^ { 2 } } } \\ & { \quad - ( 1 + \gamma \frac { 1 } { s ^ { 2 } } \varepsilon _ { x } + \bar { d } \cdot \bar { d } u _ { s } - \bar { d } u _ { s } - \bar { d } \cdot \bar { d } u _ { s } ) } \\ & { \quad + \frac { 1 } { s ^ { 2 } } \sum _ { s } \bar { d } M _ { s } \frac { \bar { d } ( \varepsilon _ { x } - \varepsilon _ { x } ) } { | u _ { s } | ^ { 2 } } } \\ & { \quad \times \left[ \left( 1 + \gamma \frac { 1 } { s ^ { 2 } } \varepsilon _ { x } - \varepsilon _ { x } ^ { 2 } + \gamma _ { s } + 1 \right) \varepsilon _ { x } \varepsilon _ { x } \right] } \\ & { \quad - \frac { 1 } { s ^ { 2 } } \left( 2 \tau + \frac { 3 } { s ^ { 2 } } \right) \sum _ { s } \frac { \bar { d } ( \varepsilon _ { x } - \varepsilon _ { x } ) } { | u _ { s } | ^ { 2 } } + \mathcal { O } ( \varepsilon ^ { - 4 } ) . } \end{array}
$$

(Will 1993; Klioner & Soffel 2000), where $\pmb { r } _ { o A } = \pmb { x } _ { o } - \pmb { x } _ { A }$ , $\pmb { r } _ { A B } = \pmb { x } _ { A } - \pmb { x } _ { B } ,$ and an overdot denotes the total time derivative with respect to $t = \mathrm { T C B }$ : for example, $\dot { \mathbf { x } } _ { o } = d \mathbf { x } _ { o } ( t ) / d t$ .

The observations of the satellite itself performed to determine its orbit (typically range and Doppler tracking) should be also modeled in the relativistic framework: (1) the positions of the observing stations should be defined in the GCRS and then transformed into the BCRS, (2) the description of the signal propagation between the satellite and the observing stations must take into account the corresponding relativistic effects in the BCRS (the Shapiro effect, relativistic Doppler effects, etc.), and (3) the difference between the proper timescales of the satellite and the observing sites and the coordinate time of the BCRS must also be taken into account. A detailed description of these steps is beyond the scope of the present paper. The final result of the orbit determination procedure is the BCRS position $x _ { o }$ and velocity $\dot { \mathbf { x } } _ { o }$ of the satellite as a function of $t = \mathrm { T C B }$ .

If the satellite is close enough to Earth (geostationary or lower), it is advantageous to model its motion in the GCRS. The structure of the equations of motion of a satellite with respect to the GCRS can be written as

$$
\frac { d ^ { 2 } X _ { o } } { d T ^ { 2 } } = \Phi _ { \mathrm { E } } + \Phi _ { \mathrm { e l } } + \frac { 1 } { c ^ { 2 } } \big ( \Phi _ { \mathrm { c o u p } } + \Phi _ { \mathrm { m g } } + \Phi _ { \mathrm { S E P } } \big ) + { \cal O } ( c ^ { - 4 } ) ,
$$

where $\Phi _ { \mathrm { E } }$ is the acceleration due to the gravitational field of Earth, $\Phi _ { \mathrm { c o u p } }$ is the Earth–third-body coupling term, $\Phi _ { \mathrm { e l } }$ is the ‘‘ gravito-electric ’’ part (independent of the velocity of the satellite) of the tidal influence of external bodies (this formally includes the Newtonian tidal force), $\Phi _ { \mathrm { m g } }$ is the purely relativistic ‘‘ gravitomagnetic ’’ part (depending on the velocity of the satellite) of the tidal influence of external bodies, and, finally, $\Phi _ { \mathrm { S E P } }$ is the additional acceleration due to possible violation of the strong equivalence principle in alternative theories of gravity $( \Phi _ { \mathrm { S E P } } \equiv 0$ in general relativity, where the PPN parameters $\beta = \gamma = 1$ ). The main relativistic terms in $\Phi _ { \mathrm { E } }$ come from the spherically symmetric part of Earth’s gravitational field and can be formally derived in the framework of the Schwarzschild solution for Earth considered to be isolated. This main relativistic effect is recommended to be taken into account by the IERS Conventions (McCarthy 1996). Explicit formulae for the righthand side of equation (4) can be found in $\ S 7$ of Klioner & Soffel (2000) in the framework of the PPN formalism with parameters $\beta$ and $\gamma$ . The same equations in the framework of general relativity have been derived by Klioner & Voinov (1993), Damour et al. (1994), and Brumberg & Kopeikin (1989b).

If equation (4) is used to represent the motion of the satellite, the whole process of orbit determination can be performed directly in the GCRS. Again, the orbit determination observations should be consistently modeled in the relativistic framework: both the coordinates of the stations and the position of the satellite should be described in the GCRS, the propagation of the electromagnetic signals should be adequately modeled in the GCRS, and the proper time of the satellite, that of the tracking stations, and TCG should be properly converted into each other when needed. The result of the orbit determination process is the GCRS coordinates of the satellite $X _ { o }$ and its velocity $d X _ { o } / d t$ as a function of $T = \mathrm { T C G }$ . In order to be used in the model of positional observations given below, these coordinates must be transformed into the corresponding BCRS coordinates:

$$
\begin{array} { r l } & { X _ { o } = r _ { \mathrm { o E } } + c ^ { - 2 } \bigg [ \frac { 1 } { 2 } \pmb { v } _ { \mathrm { E } } ( \pmb { v } _ { \mathrm { E } } \bullet r _ { \mathrm { o E } } ) + \gamma w _ { \mathrm { e x t } } ( \pmb { x } _ { \mathrm { E } } ) \pmb { r } _ { \mathrm { o E } } } \\ & { \qquad + \gamma r _ { \mathrm { o E } } ( \pmb { a } _ { \mathrm { E } } \bullet r _ { \mathrm { o E } } ) - \frac { 1 } { 2 } \gamma \pmb { a } _ { \mathrm { E } } \big \vert r _ { \mathrm { o E } } \big \vert ^ { 2 } \bigg ] + O ( c ^ { - 4 } ) } \end{array}
$$

(see IAU 2001; Klioner & Soffel 2000), where $\pmb { r } _ { 0 \mathrm { E } } = \pmb { x } _ { o } - \pmb { x } _ { \mathrm { E } }$ and $\scriptstyle x _ { \mathrm { E } } , \ v _ { \mathrm { E } }$ , and $\pmb { a } _ { \mathrm { E } }$ are the BCRS position, velocity, and acceleration of Earth and $w _ { \mathrm { e x t } } ( \mathbf { x } _ { \mathrm { E } } )$ is the gravitational potential of the solar system except for that of Earth evaluated at the geocenter. It is easy to estimate that the relativistic effects in equation (5) may amount to $\sim 1 ~ \textrm { m }$ for $| r _ { \mathrm { o E } } | \sim 5 0 { , } 0 0 0 \mathrm { \bar { k m } }$ . The GCRS velocity of the satellite can be transformed into the corresponding BCRS velocity as

$$
\begin{array} { r l } { \frac { d X _ { o } } { d T } = \delta v _ { o } } & { } \\ { + c ^ { - 2 } \Big ( \delta v _ { o } \Big \{ \frac { 1 } { 2 } | v _ { \mathrm { E } } | ^ { 2 } } & { } \\ { + \left( 1 + \gamma \right) \big [ w _ { \mathrm { e x t } } ( x _ { \mathrm { E } } ) + a _ { \mathrm { E } } \cdot r _ { \mathrm { o E } } \big ] + v _ { \mathrm { E } } \cdot \delta v _ { o } \Big \} } & { } \\ { + \frac { 1 } { 2 } v _ { \mathrm { E } } ( v _ { \mathrm { E } } \cdot \delta v _ { o } ) + \gamma r _ { \mathrm { o E } } ( a _ { \mathrm { E } } \cdot \delta v _ { o } ) } & { } \\ { - \gamma a _ { \mathrm { E } } ( r _ { \mathrm { o E } } \cdot \delta v _ { o } ) + \frac { 1 } { 2 } a _ { \mathrm { E } } ( v _ { \mathrm { E } } \cdot r _ { \mathrm { o E } } ) } & { } \\ { + \frac { 1 } { 2 } v _ { \mathrm { E } } ( a _ { \mathrm { E } } \cdot r _ { \mathrm { o E } } ) - \gamma \dot { \gamma } _ { \mathrm { e x t } } ( x _ { \mathrm { E } } ) r _ { \mathrm { E } } } & { } \\ { + \gamma r _ { \mathrm { o E } } ( \hat { a } _ { \mathrm { E } } \cdot r _ { \mathrm { o E } } ) - \frac { 1 } { 2 } \dot { \gamma } \dot { a } _ { \mathrm { E } } | r _ { \mathrm { o E } } | ^ { 2 } \Big ) + O ( c ^ { - 4 } ) } & { ( 6 ) } \end{array}
$$

(this formula can be obtained by taking the time derivative of eq. [5] and using the TCG-TCB transformation; IAU 2001; Klioner $\&$ Soffel 2000), where $\delta \pmb { v } _ { o } = \dot { \pmb { x } } _ { o } - \pmb { v } _ { \mathrm { E } }$ and $\dot { \pmb { a } } = d \pmb { a } _ { \mathrm { E } } / d t$ . It is easy to see from equation (6) that for a geostationary satellite, the numerical difference between $d X _ { o } / d t$ and $\delta \pmb { v } _ { o }$ is less than $1 0 ^ { - 4 } \mathrm { m } \mathrm { s } ^ { - 1 }$ . Therefore, for a model with a final accuracy of ${ \sim } 1$ las the relativistic terms in equation (6) can be neglected, and one can use $d X _ { o } / d t = \delta \pmb { v } _ { o }$ .

Note that probably even for the target accuracy of $1 0 ^ { - 3 }$ $\mathrm { ~ m ~ s ^ { - 1 } ~ }$ in the velocity of the satellite, one can significantly simplify both the BCRS equations of motion (eq. [3]) and those in the GCRS (eq. [4]). However, this crucially depends on the particular orbit of the satellite, and such an analysis will not be given here.

Let us also note that the rotational motion of the satellite should also be carefully modeled (for some missions the attitude of the satellite will be determined from the observational data produced by the satellite, but a kind of theoretical modeling is nevertheless necessary). From the theoretical point of view, in order to model the rotational motion of the satellite it is convenient to introduce a local kinematically nonrotating reference system for the satellite with coordinates $( \tau _ { o } , \xi )$ , where $\tau _ { o }$ is the proper time of the satellite, related to $t$ by equation (1), and $\xi$ are the spatial coordinates of the reference system, related to those of the BCRS by a transformation analogous to equation (5) (for details on the local reference system of the satellite, see Brumberg & Kopeikin $1 9 8 9 \mathrm { a }$ ; Klioner 1993; Klioner & Soffel 1998a). The rotational motion of the satellite with respect to the axes $\xi$ is described by the post-Newtonian rotational equations of motion, discussed by Damour et al. (1993) for the case of general relativity and by Klioner & Soffel (1998b, 2000) in the framework of the PPN formalism. From the practical point of view, it is however clear that the largest relativistic effect on the rotational motion of the satellite with respect to remote stars is due to the geodetic (de Sitter) precession, which amounts to ${ \sim } 2$ las $\mathrm { h r } ^ { - 1 }$ ${ \sim } 2 ^ { \prime \prime }$ per century) for a satellite on a heliocentric orbit with semimajor axis close to 1 AU (such as GAIA or SIM) and ${ \sim } 1 4 0 \ \mu \mathrm { a s \ h r ^ { - 1 } }$ ${ \sim } 1 { : } 2$ per year) for satellites on geostationary orbits (such as Hipparcos and DIVA). Taking into account that the satellites will typically monitor and verify their attitude with the help of onboard gyroscopes and observations of specially selected stars, and that the precise attitude with respect to remote stars will be determined a posteriori from the processing of observational data, it is unlikely that such small relativistic effects could be of practical importance.

The rest of the relativistic model of positional observations is totally independent of the GCRS. It is only the orbit determination process (or at least a part of that process) that involves the use of the GCRS coordinates and concepts.

# 5. ABERRATION

The first step of the model is to eliminate the aberrational effects induced by the barycentric velocity of the observer. Let $\pmb { S }$ denote the unit direction $\begin{array} { r } { s \cdot s = 1 } \end{array}$ ) toward the source as observed by the observer (satellite). Let $\pmb { p }$ be the BCRS coordinate velocity of the photon at the point of observation. Note that $\pmb { p }$ is directed roughly from the source to the observer. The unit BCRS coordinate velocity of the light ray $\pmb { n } = \pmb { p } / | \pmb { p } |$ (which implies $\pmb { n } \cdot \pmb { n } = 1$ ) can then be computed as

$$
\begin{array} { l } { s = - \pmb { n } + c ^ { - 1 } \pmb { n } \times ( \pmb { \dot { x } } _ { o } \times \pmb { n } ) } \\ { \quad \quad + c ^ { - 2 } [ ( \pmb { n } \cdot \dot { \pmb { x } } _ { o } ) \pmb { n } \times ( \dot { \pmb { x } } _ { o } \times \pmb { n } ) + \frac { 1 } { 2 } \dot { \pmb { x } } _ { o } \times ( \pmb { n } \times \dot { \pmb { x } } _ { o } ) ] } \\ { \quad \quad + c ^ { - 3 } \{ [ ( \pmb { n } \cdot \dot { \pmb { x } } _ { o } ) ^ { 2 } + ( 1 + \gamma ) w ( \pmb { x } _ { o } ) ] \pmb { n } \times ( \dot { \pmb { x } } _ { o } \times \pmb { n } ) } \\ { \quad \quad \qquad + \frac { 1 } { 2 } ( \pmb { n } \cdot \dot { \pmb { x } } _ { o } ) \dot { \pmb { x } } _ { o } \times ( \pmb { n } \times \dot { \pmb { x } } _ { o } ) \} + O ( c ^ { - 4 } ) } \end{array}
$$

(Klioner 1991b; Klioner & Kopeikin 1992), where $w ( \pmb { x } _ { o } )$ is the gravitational potential of the solar system at the point of observation. This formula contains relativistic aberrational effects up to third order with respect to $1 / c$ . One can check from equation (7) that the condition $\pmb { n } \cdot \pmb { n } = 1$ implies $s \cdot s = \hat { O ( c ^ { - 4 } ) }$ . Because of the first-order aberrational terms (classical aberration), in order to attain an accuracy of 1 las the BCRS coordinate velocity of the satellite must be known to an accuracy of ${ \sim } 1 0 ^ { - 3 }$ $\mathrm { ~ m ~ } \mathrm { ~ s ^ { - 1 } ~ }$ . For a satellite with BCRS velocity $| \dot { \pmb x } _ { o } | \sim 4 0 ~ \mathrm { k m }$ $\mathbf { s } ^ { - 1 }$ , the first-order aberration is on the order of $2 8 ^ { \prime \prime }$ , the second-order one may amount to 3.6 mas, and the thirdorder effects are ${ \sim } 1$ las. Note also that the higher order aberrational effects are nonlinear with respect to the velocity of the satellite and cannot be divided into additive pieces like ‘‘ annual ’’ and ‘‘ diurnal ’’ aberrations as can be done with the first-order aberration for an Earthbound observer. This is the reason why it is advantageous to directly use the BCRS velocity of the satellite.

The vector $\pmb { S }$ is defined in the kinematically nonrotating local satellite reference system $( \tau _ { o } , \xi )$ mentioned in the previous section. As discussed in $\ S ~ 7 . 1$ of Klioner & Kopeikin (1992), this point of view is equivalent to the standard tetrad approach discussed, for example, by Brumberg (1986). The same form of equation (7) can be derived both from the standard tetrad formalism (e.g., Brumberg 1986; Klioner 1991b) and from considerations related to the local reference system of the satellite (Klioner & Kopeikin 1992). Actual observations of a scanning astrometric satellite are referred to a reference system the spatial axes of which rotate rigidly with respect to $\xi$ , so that the satellite’s attitude remains fixed in the rotating axes. The rotating axes $\bar { \boldsymbol { \xi } }$ are related to the kinematically nonrotating axes $\xi$ as

$$
\bar { \xi } ^ { a } = { \cal P } ^ { a b } ( \tau _ { o } ) \xi ^ { b } ,
$$

where $P ^ { a b }$ is a time-dependent orthogonal matrix, which can be parameterized, for example, by three Euler angles. These Euler angles define the attitude of the satellite with respect to the kinematically nonrotating axis and should be determined from observations and the corresponding modeling. Depending on the particular optical scheme of the scanning satellite, its rotational motion can produce an additional measurable aberrational effect. A detailed analysis of this additional effect will be published elsewhere.

To clarify the origin of the terms in equation (7) proportional to the gravitational potential $w$ , let us consider a fictitious observer whose position coincides with that of the satellite at the moment of observation and whose velocity with respect to the BCRS is zero. The direction toward the source observed by this fictitious observer is

$$
\pmb { s } ^ { \prime } = - \pmb { n } + O ( c ^ { - 4 } ) ,
$$

as can be calculated from equation (7) for $\dot { \mathbf { x } } _ { o } = 0$ . On the other hand, the transformation between the directions toward the source observed by the two observers located at the same point of spacetime can be derived from the usual Lorentz transformation, which can be used in its closed form to speed up the practical calculations (F. Mignard 2000, private communication). The Lorentz transformation depends only on the velocity of one observer as seen by the other, $v$ . Hence, using the Lorentz transformation in its closed form one obtains

$$
\begin{array} { c } { { s = \left\{ s ^ { \prime } + \left[ \displaystyle \frac { \Gamma } { c } + \left( \Gamma - 1 \right) \displaystyle \frac { v \cdot s ^ { \prime } } { \left| v \right| ^ { 2 } } \right] v \right\} \displaystyle \frac { 1 } { \Gamma ( 1 + v \cdot s ^ { \prime } / c ) } \ , \ } } \\ { { \Gamma = \displaystyle \frac { 1 } { \sqrt { 1 - \left| v \right| ^ { 2 } / c ^ { 2 } } } \ . \ } } \end{array}
$$

It is easy to show from equation (10) that $\pmb { s } ^ { \prime } \pmb { \cdot } \pmb { s } ^ { \prime } = 1$ implies $s \cdot s = 1$ . The velocity of the satellite as measured by the fictitious observer, $v$ , can again be calculated either with the help of the tetrad formalism (e.g., Brumberg 1986) or by considering the local reference system for the fictitious observer (Klioner & Kopeikin 1992; Klioner 1993). The latter line of arguments leads to an equation similar to equation (6) in which one should set the BCRS velocity of the fictitious observer to zero (this corresponds to $\pmb { v } _ { \mathrm { E } } = 0$ in eq. [6]), its BCRS acceleration ( $\mathbf { \boldsymbol { a } } _ { \mathrm { E } } = 0$ in eq. [6]), as well as the position of the satellite relative to the local reference system ( $r _ { \mathrm { o E } } = 0$ in eq. [6]). Therefore, one finds

$$
{ \pmb v } = \dot { { \pmb x } } _ { o } [ 1 + c ^ { - 2 } ( 1 + \gamma ) w ( { \pmb x } _ { o } ) ] + O ( c ^ { - 4 } ) .
$$

It is this renormalization of the velocity of the satellite that leads to the $w$ -dependent terms in equation (7). It is easy to check that equations (9)–(12) are equivalent to equation (7).

Alternatively, it is easy to calculate a formula relating the observed angular distance $\varphi _ { 1 2 } ^ { \mathrm { o b s } }$ (cos $\varphi _ { 1 2 } ^ { \mathrm { o b s } } = s _ { 1 } \cdot s _ { 2 } )$ ) between two given sources to the coordinate angular distance coord $\varphi _ { 1 2 } ^ { \mathrm { c o o r d } }$ between them (cos ):

$$
\begin{array} { c } { { \cos \varphi _ { 1 2 } ^ { \mathrm { o s s } } = \cos \varphi _ { 1 2 } ^ { \mathrm { c o s s } } + ( \cos \varphi _ { 1 2 } ^ { \mathrm { c o s s } 2 } - 1 ) } } \\ { { \times \left\{ - \left[ 1 + \frac { 1 + \gamma } { c ^ { 2 } } w ( { \boldsymbol x } _ { o } ) \right] \frac { \left. \lambda _ { o } \right. } { c } ( \cos \theta _ { 1 } + \cos \theta _ { 2 } ) \right. } } \\ { { \left. + \frac { \left. \dot { \lambda } _ { o } \right. ^ { 2 } } { c ^ { 2 } } ( \cos ^ { 2 } \theta _ { 1 } + \cos ^ { 2 } \theta _ { 2 } + \cos \theta _ { 1 } \cos \theta _ { 2 } - 1 ) \right. } } \\ { { \left. - \frac { \left. \dot { \lambda } _ { o } \right. ^ { 3 } } { c ^ { 3 } } ( \cos \theta _ { 1 } + \cos \theta _ { 2 } ) ( \cos ^ { 2 } \theta _ { 1 } + \cos ^ { 2 } \theta _ { 2 } - 1 ) \right\} } } \\ { { \left. + O ( c ^ { - 4 } ) , \right. } } \end{array}
$$

where the $\theta _ { i }$ are the angles between the direction toward the ith source and the direction of the velocity $\dot { \mathbf { x } } _ { o }$ :

$$
\cos \theta _ { i } = - | \dot { \pmb x } _ { o } | ^ { - 1 } { \pmb n } _ { i } \cdot \dot { \pmb x } _ { o } ~ , ~ i = 1 , 2 ~ .
$$

The terms in equations (7) and (13) proportional to $w$ are the largest terms of third order. These are on the order of 1 las, and therefore the potential $w$ can be approximated here by the potential of the spherically symmetric Sun:

$$
w ( \mathbf { x } _ { o } ) \approx G M _ { \mathrm { S u n } } / | \mathbf { x } _ { o } - \mathbf { x } _ { \mathrm { S u n } } | .
$$

A closed-form expression equivalent to equation (13) can be derived from equation (10):

$$
\begin{array} { r l r } {  { 1 - \cos \varphi _ { 1 2 } ^ { \mathrm { o b s } } = ( 1 - \cos \varphi _ { 1 2 } ^ { \mathrm { c o o r d } } ) } } \\ & { } & { \qquad \times \frac { 1 - | \pmb { v } | ^ { 2 } / c ^ { 2 } } { [ 1 + ( | \pmb { v } | / c ) \cos \theta _ { 1 } ] [ 1 + ( | \pmb { v } | / c ) \cos \theta _ { 2 } ] } , } \end{array}
$$

where $v$ is defined by equation (12).

For order-of-magnitude estimates, it is also useful to derive a formula for the angular shift $\delta \theta$ of the source toward the apex of the satellite’s motion:

$$
\begin{array} { c } { \displaystyle \delta \theta = \displaystyle \frac 1 c | \dot { \pmb x } _ { o } | \sin \theta \left[ 1 + \frac 1 { c ^ { 2 } } ( 1 + \gamma ) w ( { \pmb x } _ { o } ) + \frac 1 4 \frac { | \dot { \pmb x } _ { o } | ^ { 2 } } { c ^ { 2 } } \right] } \\ { \displaystyle - \frac 1 4 \frac { | \dot { \pmb x } _ { o } | ^ { 2 } } { c ^ { 2 } } \sin 2 \theta + \frac 1 { 1 2 } \frac { | \dot { \pmb x } _ { o } | ^ { 3 } } { c ^ { 3 } } \sin 3 \theta + O ( c ^ { - 4 } ) } \end{array}
$$

or, in closed form,

$$
\cos { \left( \theta - \delta \theta \right) } = \frac { \cos { \theta } + | \pmb { v } | / c } { 1 + ( | \pmb { v } | / c ) \cos { \theta } } .
$$

Here $\theta$ is the angle between the direction toward the source and the direction of the satellite’s velocity, cos $\theta = - \pmb { n } \cdot \pmb { v } / | \pmb { v } |$ $= - \pmb { n } \cdot \dot { \pmb { x } } _ { o } / | \dot { \pmb { x } } _ { o } |$ .

# 6. GRAVITATIONAL LIGHT DEFLECTION

The next step is to account for the gravitational deflection of light, that is, to convert $\pmb { n }$ into the corresponding unit coordinate direction $\pmb { k }$ from the observed source at the moment of emission to the observer at the moment of observation. Here two different cases should be distinguished: (1) objects outside of the solar system, whose finite distance from the origin of the BCRS plays (almost) no role in this step of the reduction scheme, and (2) solar system objects, the finite distance of which must be taken into account. Let us first relate $\pmb { n }$ to the unit coordinate direction $\pmb { \sigma }$ of the light propagation infinitely far from the gravitating sources for $t \to - \infty$ and then consider the influence of the finite distance to the objects on the gravitational light deflection separately for these two classes of objects $\mathrm { ~ \normalfont ~ \ S \ S ~ 6 . 1 ~ }$ and 6.2 below).

The solar system is assumed here to be isolated. This means that the gravitational field produced by matter outside of the solar system is neglected. This assumption is well founded if the time dependence of the gravitational field produced outside of the solar system is negligible. Otherwise, the external gravitational field must be explicitly taken into account (e.g., for observations of edge-on binary stars, where the gravitational field of the companion can cause an additional time-dependent light deflection, or for astrometric microlensing events). Some such cases will be discussed below in $\ S 1 1$ .

The equations of light propagation can be derived from the general relativistic Maxwell equations (Misner, Thorne, & Wheeler 1973). It is sufficient, however, to consider only the limit of geometric optics. The relativistic effects depending on wavelength (and therefore representing deviations from geometric optics) are much smaller than 1 las in the solar system (see, e.g., Mashhoon 1974). In the limit of geometric optics, the relativistic equations of light propagation

can be written in the form

$$
\begin{array} { r } { \mathbf { x } _ { p } ( t ) = \mathbf { x } _ { p } ( t _ { o } ) + c \pmb { \sigma } ( t - t _ { o } ) + \Delta \mathbf { x } _ { p } ( t ) \ , } \end{array}
$$

where $t _ { o }$ is the moment of observation, $\boldsymbol { x } _ { p } ( t _ { o } )$ is the position of the photon at the moment of observation [this position obviously coincides with the position of the satellite at that moment, $\mathbf { \boldsymbol { x } } _ { p } ( t _ { o } ) = \mathbf { \boldsymbol { x } } _ { o } ( t _ { o } ) ]$ , $\pmb { \sigma }$ is the unit coordinate direction of the light propagation at the past null infinity ${ \boldsymbol { \sigma } } \cdot { \boldsymbol { \sigma } } = 1$ ),

$$
{ \pmb \sigma } = \operatorname* { l i m } _ { t  - \infty } \dot { \pmb x } _ { p } ( t ) / c ,
$$

and $\Delta \ v { x } _ { p }$ is the sum of all gravitational effects in the light propagation, which satisfies the conditions

$$
\Delta { \bf x } _ { p } ( t _ { o } ) = 0 \ , \quad \operatorname * { l i m } _ { t  - \infty } \Delta \dot { { \bf x } } _ { p } ( t ) = 0 \ .
$$

From the BCRS metric (IAU 2001), one can easily see that $\Delta \mathbf { x } _ { p } ( t ) \sim O ( c ^ { - 2 } )$ and $c ^ { - 1 } \Delta \dot { \mathbf { x } } _ { p } ( t ) \sim O ( c ^ { - 2 } )$ .

Several effects in $\Delta \ v { x } _ { p }$ should be a priori considered at the level of 1 las: (1) the effects of the spherically symmetric part of the gravitational field of each sufficiently large gravitating body, (2) the effects of the asphericity (mainly due to the quadrupole moments) of the bodies, (3) the effects caused by the gravitomagnetic field due to the translational motion of the bodies, and (4) the effects caused by the gravitomagnetic field due to the rotational motion of the bodies. The reduction formulae for all these effects have been derived and discussed in detail by Brumberg, Klioner, & Kopeikin (1990), Klioner (1991a, 1991b), and Klioner & Kopeikin (1992).

Table 1 illustrates the maximal magnitudes of the various gravitational effects due to the solar system bodies and the maximal angular distances between the source and the body at which the gravitational light deflection from that body should still be accounted for to attain a final accuracy of 1 las. Note that the values in Table 1 are slightly different from those published by Brumberg et al. (1990) and Klioner (2000). The reason for this discrepancy is that for Table 1 the best current estimates for the physical parameters of the solar system bodies were taken from Weissman, McFadden, & Johnson (1999), whereas the 1976 IAU system of astronomical constants (Fricke et al. 1977) was used for the previous publications.

One can see that the post–post-Newtonian terms attain 1 las only within $5 3 ^ { \prime }$ from the Sun and can currently be neglected in the case of space astrometry, since none of the proposed satellites could observe so close to the Sun. For the same reason the effect due to the rotational motion of the Sun, amounting to 0.7 las for a grazing ray, is unobservable. The largest observable effect due to rotational motion is 0.2 las for a light ray grazing Jupiter. Therefore, the effects due to the rotational motion of the bodies are also too small to be taken into account.

TABLE 1 Various Gravitational Effects on Light Propagation   

<table><tr><td>Body</td><td>SpN (μas)</td><td>max(1 μas)</td><td>max(10 μas)</td><td>80 (uas)</td><td>max(1 μas)</td><td>8R (uas)</td><td>8T* (μas)</td><td>SPpN (μas)</td><td>max(1 μas)</td></tr><tr><td>Sun ...</td><td>1.75 ×106</td><td>180°</td><td>180°</td><td>~1</td><td></td><td>0.7</td><td>0.1</td><td>11</td><td>53&#x27;</td></tr><tr><td>Mercury..</td><td>83</td><td>9</td><td>54&quot;</td><td>…</td><td></td><td></td><td>：</td><td></td><td></td></tr><tr><td>Venus...</td><td>493</td><td>45</td><td>27&#x27;</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Earth..</td><td>574</td><td>178°/123°</td><td>154°/21°</td><td>0.6</td><td></td><td>·</td><td></td><td>·</td><td></td></tr><tr><td>Moon.......</td><td>26</td><td>9/5°</td><td>49&#x27;/26&#x27;</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Mars..</td><td>116</td><td>25&#x27;</td><td>2.5</td><td>0.2</td><td>：</td><td>：</td><td>：</td><td></td><td></td></tr><tr><td>Jupiter....</td><td>16270</td><td>90°</td><td>11:3</td><td>240</td><td>152&quot;</td><td>0.2</td><td>0.8</td><td></td><td></td></tr><tr><td>Saturn...</td><td>5780</td><td>17°</td><td>17</td><td>95</td><td>46&quot;</td><td>·</td><td>0.2</td><td></td><td></td></tr><tr><td>Uranus... ....</td><td>2080</td><td>71&#x27;</td><td>71</td><td>8</td><td>4&quot;</td><td></td><td></td><td></td><td></td></tr><tr><td>Neptune...</td><td>2533</td><td>51&#x27;</td><td>5&#x27;</td><td>10</td><td>3&quot;</td><td></td><td></td><td></td><td></td></tr><tr><td>Ganymede.</td><td>35</td><td>32″</td><td>4″</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Titan...</td><td>32</td><td>14&quot;</td><td>2&quot;</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Io..</td><td>31</td><td>19&quot;</td><td>2&quot;</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Callist....</td><td>28</td><td>23″</td><td>3&quot;</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Europa...</td><td>19</td><td>11&quot;</td><td>1&quot;</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Triton.... .....···...·.</td><td>10</td><td>07</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Pluto.....</td><td>7</td><td>04</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Titania...</td><td>2.8</td><td>0&quot;2</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Oberon..... ..</td><td>2.4</td><td>0&quot;2</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Rhea...</td><td>1.9</td><td>03</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Charon</td><td>1.7</td><td>0&#x27;05</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Iapetus.......</td><td>1.6</td><td>0&quot;2</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Ariel..</td><td>1.4</td><td>01</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Ceres...</td><td>1.2</td><td>03</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Dione ...</td><td>1.2</td><td>0&quot;2</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Umbriel</td><td>1.2</td><td>0&#x27;1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Notes.—Here $ { \delta _ { \mathrm { p N } } }$ and $ { \delta _ { \mathrm { p p N } } }$ are the post-Newtonian and post–post-Newtonian effects due to the spherically symmetric field of each body, $\delta _ { Q }$ is the effect due to quadrupole gravitational fields, and $\delta _ { R }$ and $\delta _ { T ^ { * } }$ are the effects due to the gravitomagnetic fields caused by the rotational and translational motions of the bodies, respectively. The estimates of $\delta _ { T ^ { * } }$ are given for the case in which the coordinates of the gravitating bodies are taken at the moment of the closest approach of the body and the photon (see text). Blank entries indicate that the corresponding effect is smaller than $0 . 1 \mu \mathrm { a s }$ . Physical parameters of the bodies are taken from Weissman et al. 1999. Because of the minimal Sun avoidance angle, the influence of some bodies can neglected for certain missions (e.g., for GAIA, Mercury is too close to the Sun and can be neglected). The angle $\psi _ { \mathrm { m a x } } ( \delta )$ is the maximal angular distance between the body and the source at which the corresponding effect still attains $\delta$ [the smallest possible distance between the observer and each body is taken here; $\psi _ { \mathrm { m a x } } ( \delta )$ is smaller for larger distances]. For these estimates, the observer is supposed to be within a few million kilometers of Earth orbit. For Earth and the Moon, two estimates are given: for a geostationary satellite and for a satellite at a distance of $1 0 ^ { 6 } \mathrm { k m }$ from Earth.

The largest contribution to $\Delta \ v { x } _ { p }$ for solar system applications comes from the spherically symmetric components of the gravitational fields of the massive bodies and can be calculated as

$$
\Delta _ { \mathrm { p N } } \mathbf { x } _ { p } ( t ) = - \sum _ { A } \frac { ( 1 + \gamma ) G M _ { A } } { c ^ { 2 } } ( \pmb { d } _ { A } \mathcal { I } _ { A } + \pmb { \sigma } \mathcal { J } _ { A } ) ,
$$

$$
\pmb { d } _ { A } = \pmb { \sigma } \times ( \pmb { r } _ { o A } \times \pmb { \sigma } ) \mathrm { ~ , ~ }
$$

$$
\mathcal { I } _ { A } = \frac { 1 } { \left| \boldsymbol { r } _ { A } \right| - \boldsymbol { \sigma } \cdot \boldsymbol { r } _ { A } } - \frac { 1 } { \left| \boldsymbol { r } _ { o A } \right| - \boldsymbol { \sigma } \cdot \boldsymbol { r } _ { o A } } \ ,
$$

$$
\mathcal { J } _ { A } = \log \frac { | \boldsymbol { r } _ { A } | + \pmb { \sigma } \cdot \boldsymbol { r } _ { A } } { | \boldsymbol { r } _ { o A } | + \pmb { \sigma } \cdot \boldsymbol { r } _ { o A } } \ ,
$$

$$
\mathbf { \boldsymbol { r } } _ { A } = \mathbf { \boldsymbol { x } } _ { p } ( t ) - \mathbf { \boldsymbol { x } } _ { A } ~ ,
$$

$$
\mathbf { \boldsymbol { r } } _ { o A } = \mathbf { \boldsymbol { x } } _ { p } ( t _ { o } ) - \mathbf { \boldsymbol { x } } _ { A } = \mathbf { \boldsymbol { x } } _ { o } ( t _ { o } ) - \mathbf { \boldsymbol { x } } _ { A } ~ ,
$$

so that

$$
\frac { 1 } { c } \Delta _ { \mathrm { p N } } \dot { \pmb x } _ { p } ( t ) = - \sum _ { A } \frac { ( 1 + \gamma ) G M _ { A } } { c ^ { 2 } } \bigg ( d _ { A } \frac { 1 } { c } \dot { \pmb x } _ { A } + \sigma \frac { 1 } { c } \dot { \pmb \mathscr { g } } _ { A } \bigg ) ,
$$

$$
{ \frac { 1 } { c } } { \dot { \mathcal { G } } } _ { A } = { \frac { 1 } { | { \boldsymbol { r } } _ { A } | ( | { \boldsymbol { r } } _ { A } | - { \boldsymbol { \sigma } } \cdot { \boldsymbol { r } } _ { A } ) } } \ , { \frac { 1 } { c } } { \dot { \mathcal { L } } } _ { A } = { \frac { 1 } { | { \boldsymbol { r } } _ { A } | } } \ ,
$$

where $x _ { A }$ is the position and $M _ { A }$ is the mass of body A.

The positions of the bodies $x _ { A }$ are supposed to be constant in equations (22)–(29). In reality, however, the bodies are moving, and this motion cannot be neglected in the calculation of light deflection. It is hardly possible to calculate analytically the light path in the gravitational field of an arbitrarily moving body without resorting to some approximations (but see Kopeikin $\&$ Scha¨fer 1999). On the other hand, numerical integration of the equations of light propagation, which could be used here as a remedy, is too impractical for the massive calculations necessary in astrometry. Let us therefore consider a Taylor expansion of $x _ { A }$ :

$$
\begin{array} { r } { \pmb { x } _ { A } ( t ) = \pmb { x } _ { A } ^ { \mathrm { e p h } } ( t _ { A , 0 } ) + \dot { \pmb { x } } _ { A } ^ { \mathrm { e p h } } ( t _ { A , 0 } ) ( t - t _ { A , 0 } ) + O ( \ddot { \pmb { x } } _ { A } ^ { \mathrm { e p h } } ) . } \end{array}
$$

Note that here $x _ { A } ^ { \mathrm { e p h } } ( t _ { A , 0 } )$ and $\dot { \mathbf { x } } _ { A } ^ { \mathrm { e p h } } ( t _ { A , 0 } )$ are the actual position and velocity of body A taken from an ephemeris for some moment $t _ { A , 0 }$ , while $\mathbf { \boldsymbol { x } } _ { A } ( t )$ is the model for the position of body A to be used in the approximate calculation of the light propagation. One can integrate the equations of motion for a light ray using equation (30) for the coordinates of the gravitating body. The solution was first derived in Klioner (1989) and describes the light propagation in the post-Newtonian approximation under the assumption that the gravitating bodies move with constant velocity [only the effects that are linear with respect to the velocity ${ \dot { \mathbf { x } } } _ { A }$ were taken into account, since formally the terms quadratic in ${ \dot { \mathbf { x } } } _ { A }$ are of post–post-Newtonian order $O ( c ^ { - 4 } ) ]$ . However, this expansion has a free parameter, $t _ { A , 0 }$ , that can be used to minimize the error in the light propagation equations caused by the higher order terms neglected in equation (30). From an analysis of the residual terms in the equations of light propagation that are proportional to the accelerations of the bodies, Klioner & Kopeikin (1992) have shown that one reasonable choice that guarantees the residual effects to be negligible within the chosen approximation scheme is to set $t _ { A , 0 }$ equal to the moment of the closest approach $t _ { A , 0 } ^ { \mathrm { c a } }$ of the body and the photon:

$$
t _ { A , 0 } ^ { \mathrm { c a } } = \operatorname* { m a x } \left( t _ { e } , t _ { o } - \operatorname* { m a x } \left\{ 0 , \frac { \pmb { g } \bullet \left[ \pmb { x } _ { o } ( t _ { o } ) - \pmb { x } _ { A } ^ { \mathrm { e p h } } ( t _ { o } ) \right] } { c \left. \pmb { g } \right. ^ { 2 } } \right\} \right) ,
$$

$$
\pmb { g } = \pmb { \sigma } - c ^ { - 1 } \pmb { \dot { x } } _ { A } ^ { \mathrm { e p h } } ( t _ { o } ) \ ,
$$

where $t _ { e }$ is the time of emission of the light ray by the source (for sources located outside of the solar system, one can set $t _ { e } = - \infty$ , so that the outer maximum in eq. [32] can be omitted).

Recently, an advanced formalism to integrate the equations of light propagation in the field of arbitrarily moving gravitating bodies has been developed by Kopeikin & Scha¨fer (1999) and Kopeikin & Mashhoon (2002). The authors suggest using the solution of the Einstein field equations in the form of retarded potentials so that the positions of the gravitating bodies are computed for the retarded moment of time

$$
t _ { A , 0 } ^ { \mathrm { r } } = t _ { o } - c ^ { - 1 } \Big | \pmb { x } _ { o } \big ( t _ { o } \big ) - \pmb { x } _ { A } ^ { \mathrm { e p h } } \big ( t _ { A , 0 } ^ { \mathrm { r } } \big ) \Big | \ ,
$$

and they derive rigorous laws of the light propagation in the gravitational field of arbitrarily moving point masses in the first post-Minkowskian approximation [i.e., all the terms of order $O ( G ^ { 2 } )$ are neglected]. Using this rigorous approach, it is proved, however, that if the positions and velocities of the bodies are calculated at $t _ { A , 0 } ^ { \mathrm { r } }$ , the effects due to the accelerations of the gravitating bodies, as well as those proportional to the second and higher orders of the velocities ${ \dot { \mathbf { x } } } _ { A }$ , are much smaller than 1 las for solar system applications and, thereby, completely negligible for our model. On the other hand, if the effects due to the accelerations and those of the second and higher orders with respect to the velocities are neglected, so that each body is supposed to move with a constant velocity, the formulae for $\Delta x _ { p } ( t )$ derived by Klioner (1989) and Klioner & Kopeikin (1992) and those derived by Kopeikin & Scha¨fer (1999) coincide. If the bodies are supposed to move uniformly and rectilinearly and only the first-order terms with respect to the velocities are taken into account, the resulting solution for the light propagation can be considered a numerical approximation to the rigorous solution derived by Kopeikin & Scha¨fer. The quantity $t _ { A , 0 }$ remains a free parameter of this approximate solution. The approach due to Kopeikin & Scha¨fer does not prove that the choice $t _ { A , 0 } = t _ { A , 0 } ^ { \mathrm { r } }$ yields minimal residual terms in such A;0 an approximate solution. It is not clear which moment, $t _ { . A , 0 } ^ { \mathrm { r } }$ or $t _ { A , \underline { { 0 } } } ^ { \mathrm { c a } }$ , is numerically more advantageous to use in equation (30). However, if the effects explicitly proportional to $\dot { \mathbf { x } } _ { A }$ are taken into account to compute the light path, the difference between the solutions for $t _ { A , 0 } = t _ { A , 0 } ^ { \mathrm { c a } }$ and for $t _ { A , 0 } = t _ { A , 0 } ^ { \mathrm { r } }$ in the gravitational field of the solar system is several orders of magnitude lower than 1 las.

The effect explicitly proportional to ${ \dot { \mathbf { x } } } _ { A }$ has been investigated in detail by Klioner (1989), Klioner & Kopeikin (1992), and Kopeikin & Scha¨fer (1999). If the position of the body is taken for $t _ { A , 0 } = t _ { A , 0 } ^ { \mathrm { c a } }$ or $t _ { A , 0 } = t _ { A , 0 } ^ { \mathrm { r } }$ , this effect in the light deflection can be estimated as $\delta _ { T ^ { * } } \sim c ^ { - 1 } | \dot { \mathbf { x } } _ { A } | \delta _ { \mathrm { p N } }$ , where $ { \delta _ { \mathrm { p N } } }$ is the deflection induced by the spherically symmetric field of the body. According to Table 1, $\delta _ { T ^ { * } }$ may amount to 0.8 las for a light ray grazing Jupiter, and only 0.1 las in the case of the Sun. However, $ { \delta _ { \mathrm { p N } } }$ attains its maximal value when the impact parameter of the light ray is much smaller than the distances between the gravitating body and the points of emission and observation. For this case, one can prove that $\delta _ { T ^ { * } } \sim c ^ { - 1 } ( \pmb { \sigma } \cdot \pmb { \dot { x } } _ { A } ) \delta _ { \mathrm { p N } }$ . For the special case of an observer situated near Earth orbit, the cosine factor in ${ \pmb \sigma } \cdot \dot { \pmb x } _ { A }$ reduces the effects produced by Jupiter and Saturn in their orbital motion by factors of at least 4 and 6, respectively. Therefore, the effects explicitly proportional to the velocities of the bodies can be neglected in our model.

If the effects due to the velocities of the bodies are completely neglected, we effectively use a constant value

$$
\mathbf { x } _ { A } ( t ) = \mathbf { x } _ { A } ( t _ { A , 0 } )
$$

for the coordinates of the bodies. Numerical simulations show that in the gravitational field of the solar system, the difference between the light deflection angle calculated using $t _ { A , 0 } = t _ { A , 0 } ^ { \mathrm { c a } }$ and that using $t _ { A , 0 } = t _ { A , 0 } ^ { \mathrm { r } }$ in equation (34) does not exceed 0.01 las. Therefore, for practical purposes both $t _ { A , 0 } ^ { \mathrm { c a } }$ $\boldsymbol { x } _ { A } ( t _ { A , 0 } ^ { \mathrm { c a } } )$ and or $t _ { A , 0 } ^ { \mathrm { r } }$ $\ddot { \mathbf { \Omega } } _ { A } ( t _ { A , 0 } ^ { \mathrm { r } } )$ can be used, and A  in equations (26)–(27) and all related for- should be taken to be mulae. Note however that, for example, the use of the moment of reception $t _ { o }$ instead of $t _ { A , 0 } ^ { \mathrm { c a } }$ or $t _ { A , 0 } ^ { \mathrm { r } }$ in equation (34) may lead to a significant error in the calculated gravitational light deflection. The maximal error of this kind can be roughly estimated as $( | r _ { o A } | / L ) ( | \dot { \mathbf { x } } _ { A } | / c ) \delta _ { \mathrm { p N } }$ , where $L$ is the radius of the body, and may amount to ${ \sim } 1 0$ mas in the case of Jupiter.

Note that a number of smaller bodies should be also taken into account. For a spherical body with mean density $\rho$ , the light deflection is larger than $\delta$ if its radius

$$
L \ge \left( \frac { \rho } { 1 \mathrm { \ g \ c m ^ { - 3 } } } \right) ^ { - 1 / 2 } \left( \frac { \delta } { 1 \mu \mathrm { a s } } \right) ^ { 1 / 2 } 6 2 4 \mathrm { \ k m } \ .
$$

Therefore, at the level of 1 las (and even $1 0 \mu \mathrm { a s } )$ , one should in addition account for the several largest satellites of the giant planets, Pluto and Charon, and also Ceres. The maximal values of the effects produced by these bodies are evaluated in Table 1. It is clear, however, that the gravitational light deflection due to these small bodies could be larger than 1 las only if a source were observed very close to the corresponding body. The maximal angular distances at which this additional gravitational deflection should be taken into account are also given in Table 1.

Finally, the effects of the quadrupole fields of the giant planets should be taken into account if the angular distance between the planet and the object is smaller than the value given in the sixth column of Table 1. The corresponding reduction formulae for $\Delta _ { Q } \pmb { x } _ { p } ( t )$ and $\Delta _ { Q } \dot { \pmb x } _ { p } ( t )$ derived by Klioner (1991a) and Klioner & Kopeikin (1992) read

$$
\begin{array} { r l r } {  { \Delta _ { \mathcal { Q } } \pmb { x } _ { p } ( t ) = \frac { 1 } { 2 c ^ { 2 } } ( 1 + \gamma ) G } } \\ & { } & { \times \sum _ { A } ( \pmb { a } _ { A } \mathcal { U } _ { A } + \pmb { \beta } _ { A } \mathcal { E } _ { A } + \gamma _ { A } \mathcal { F } _ { A } + \pmb { \delta } _ { A } \mathcal { V } _ { A } ) , } \\ & { } & { \mathcal { U } _ { A } = \frac { 1 } { | \pmb { d } _ { A } | } ( \frac { 1 } { | \pmb { r } _ { A } | } \frac { | \pmb { r } _ { A } | + \pmb { \sigma } \cdot \pmb { r } _ { A } } { | \pmb { r } _ { A } | - \pmb { \sigma } \cdot \pmb { r } _ { A } } - \frac { 1 } { | \pmb { r } _ { o A } | } \frac { | \pmb { r } _ { o A } | + \pmb { \sigma } \cdot \pmb { r } _ { o A } } { | \pmb { r } _ { o A } | - \pmb { \sigma } \cdot \pmb { r } _ { o A } } ) , } \end{array}
$$

$$
\begin{array} { r l } { \displaystyle \xi _ { d } ^ { \alpha } = \frac { \sigma \cdot r _ { A } } { \left| r _ { A } \right| ^ { 3 } } - \frac { \sigma \cdot r _ { \alpha 4 } } { \left| r _ { \alpha d } \right| ^ { 3 } } , } & { \mathcal { F } _ { d } = \left| d _ { A } \right| \left( \frac { 1 } { \left| r _ { A } \right| ^ { 3 } } - \frac { 1 } { \left| r _ { \alpha A } \right| ^ { 3 } } \right) , } \\ { \displaystyle \mathcal { V } _ { A } = - \frac { 1 } { \left| d _ { A } \right| ^ { 2 } } \left( \frac { \sigma \cdot r _ { A } } { \left| r _ { A } \right| } - \frac { \sigma \cdot r _ { \alpha 4 } } { \left| r _ { \alpha A } \right| } \right) , } \\ { \displaystyle a _ { A } = 2 f _ { A } - 2 ( f _ { A } \cdot \sigma ) \sigma - ( g _ { A } \cdot \sigma + 4 f _ { A } \cdot h _ { A } ) h _ { A } , } \\ { \displaystyle \beta _ { A } = 2 ( f _ { A } \cdot \sigma ) h _ { A } + ( g _ { A } \cdot \sigma - f _ { A } \cdot h _ { A } ) \sigma , } \\ { \displaystyle \gamma _ { A } = 2 ( f _ { A } \cdot \sigma ) \sigma - ( g _ { A } \cdot \sigma - f _ { A } \cdot h _ { A } ) h _ { A } , } \\ { \displaystyle \delta _ { A } = 2 g _ { A } - 4 ( f _ { A } \cdot \sigma ) h _ { A } - ( g _ { A } \cdot \sigma - 2 f _ { A } \cdot h _ { A } ) \sigma , } \end{array}
$$

$$
\begin{array} { l } { \displaystyle \frac 1 c \Delta _ { \mathcal { Q } } \dot { x } _ { p } ^ { i } ( t ) = \frac 1 { 2 c ^ { 2 } } ( 1 + \gamma ) G } \\ { \displaystyle \qquad \times \sum _ { A } \left( \frac { \alpha _ { A } } { c } \dot { \mathcal { U } } _ { A } + \frac { \beta _ { A } } { c } \dot { \mathcal { E } } _ { A } + \frac { \gamma _ { A } } { c } \dot { \mathcal { F } } _ { A } + \frac { \delta _ { A } } { c } \dot { \mathcal { V } } _ { A } \right) , } \end{array}
$$

$$
\begin{array} { c } { { \displaystyle \frac { 1 } { c } \dot { \mathcal { U } } _ { d } = | d _ { A } | \frac { 2 | \boldsymbol { r } _ { A } | - \sigma \cdot \boldsymbol { r } _ { A } } { | \boldsymbol { r } _ { A } | ^ { 3 } \left( | \boldsymbol { r } _ { A } | - \sigma \cdot \boldsymbol { r } _ { A } \right) ^ { 2 } } ~ , } } \\ { { \displaystyle \frac { 1 } { c } \dot { \mathcal { E } } _ { d } = \frac { | \boldsymbol { r } _ { A } | ^ { 2 } - 3 ( \sigma \cdot \boldsymbol { r } _ { A } ) ^ { 2 } } { | \boldsymbol { r } _ { A } | ^ { 5 } } ~ , ~ \frac { 1 } { c } \dot { \mathcal { F } } _ { A } = - 3 | d _ { A } | \frac { \sigma \cdot \boldsymbol { r } _ { A } } { | \boldsymbol { r } _ { A } | ^ { 5 } } ~ , } } \\ { { \displaystyle \frac { 1 } { c } \dot { \mathcal { V } } _ { A } = - \frac { 1 } { | \boldsymbol { r } _ { A } | ^ { 3 } } ~ , } } \end{array}
$$

where ${ \pmb h } _ { A _ { . } } = { \pmb d } _ { A } / | { \pmb d } _ { A } | , f _ { A } ^ { i } = M _ { i j } ^ { A } h _ { A } ^ { j }$ , $g _ { A } ^ { i } = M _ { i j } ^ { A } \sigma ^ { j }$ , and $M _ { i j } ^ { A }$ is the symmetric trace-free quadrupole moment of body A. From the point of view of the theory of relativistic local reference systems, the multipole structure of the gravitational field of a body is defined in the corresponding local reference system of that body. However, for the calculation of the gravitational light deflection due to the quadrupole field, the relativistic effects in $M _ { i j } ^ { A }$ can be neglected. The matrix $M _ { i j } ^ { A }$ is symmetric and trace-free and therefore has five independent components that can be calculated from the second zonal harmonic coefficient $J _ { 2 } ^ { A }$ (in the case of the giant planets, other second-order coefficients are negligible), the mass $M _ { A }$ and the equatorial radius $L _ { A }$ of the planet, and the equatorial coordinates $( \alpha _ { \mathrm { p o l e } } ^ { A } , \delta _ { \mathrm { p o l e } } ^ { A } )$ of the north pole of its figure axis:

$$
M _ { i j } ^ { A } = M _ { A } L _ { A } ^ { 2 } J _ { 2 } ^ { A } \left( \begin{array} { c c c } { { A } } & { { B } } & { { C } } \\ { { B } } & { { D } } & { { E } } \\ { { C } } & { { E } } & { { - A - D } } \end{array} \right) ,
$$

Various post-Newtonian gravitational effects in the light propagation (e.g., $\Delta _ { \mathrm { p N } } \pmb { x } _ { p }$ and $\Delta _ { Q } \pmb { x } _ { p }$ ) are additive, and one can set

$$
\Delta \mathbf { x } _ { p } = \Delta _ { \mathrm { p N } } \mathbf { x } _ { p } + \Delta _ { \boldsymbol { Q } } \mathbf { x } _ { p } \ .
$$

Note that any additional post-Newtonian effects can be added to equation (54) if needed (e.g., the effects of the rotational or translational motion of the gravitating bodies).

As first discussed in Klioner (1991a), the higher order multipole moments of Jupiter and Saturn may produce a deflection larger than 1 las, provided that the source is observed very close to the surfaces of the planets. It is easy to see that the maximal gravitational light deflection produced by the zonal spherical harmonics $J _ { n }$ (all other harmonics are utterly small for the giant planets) can be estimated as $\delta _ { J _ { n } } \sim J _ { n } \delta _ { \mathrm { p N } }$ . Using modern values for the $J _ { n }$ of Jupiter and Saturn (Weissman et al. 1999, p. 342), one can check that it is only the effects of $J _ { 4 }$ of Jupiter and Saturn that may exceed 1 las. Namely, the effect of $J _ { 4 }$ of Jupiter may amount to $1 0 \mu \mathrm { a s }$ and that of Saturn is not greater than $6 \mu \mathrm { a s }$ . The effect of $J _ { n }$ decreases as $\mathsf { c o t } ^ { n + 1 }$ $\psi$ with the angular distance $\psi$ between the gravitating body and the source. Therefore, the effect of $J _ { 4 }$ of Jupiter exceeds 1 las only if the angular distance $\psi$ between the center of Jupiter and the source is smaller than 1.6 times the apparent angular radius of Jupiter (i.e., smaller than $2 4 ^ { \prime \prime } { - } 3 9 ^ { \prime \prime }$ depending on the mutual configuration of Jupiter and the observer). For Saturn’s $J _ { 4 } , \psi$ should be less than 1.4 times the apparent radius (less than $1 0 ^ { \prime \prime } – 1 4 ^ { \prime \prime }$ , depending on the configuration). The influence of $J _ { 6 }$ of Jupiter and Saturn also may exceed 1 las if the real values of $J _ { 6 }$ (which are known with a large uncertainty for both planets) are larger than the values given by Weissman et al. (1999). If the observations so close to Jupiter and Saturn are to be processed, the reduction formulae for the effect of $J _ { 4 }$ can be derived from formulae given by Kopeikin (1997).

Let us also note that, generally speaking, the standard expansion of the gravitational potential of a body in terms of spherical functions (with harmonic coefficients such as $J _ { n }$ ) converges only outside of the sphere encompassing the body. Therefore, in the general case the calculation of the gravitational light deflection for a light ray passing between the encompassing sphere and the surface of a body requires some other representation of the body’s gravitational potential. As discussed above, for an accuracy level of 1 las the asphericity of the gravitational field must be taken into account for the giant planets only. Since the polar radii of the giant planets are significantly smaller than their equatorial radii, the impact parameter may be smaller than the equatorial radius of the body and, therefore, smaller than the radius of the encompassing sphere. However, the gravitational fields of the giant planets are close to that of a homogeneous axisymmetric ellipsoid, $( x ^ { 2 } + y ^ { 2 } ) / a ^ { 2 } + z ^ { 2 } / c ^ { 2 } \bar { \leq } 1$ with $c < a$ , for which the gravitational potential can be expanded as

$$
\begin{array} { l } { { \displaystyle { \cal U } ( r , \vartheta ) = \frac { G M } { r } \left[ 1 - \sum _ { n = 1 } ^ { \infty } ( a / r ) ^ { 2 n } J _ { 2 n } ^ { \mathrm { e l } } P _ { 2 n } ( \cos \vartheta ) \right] , } } \\ { { \displaystyle { \cal J } _ { 2 n } ^ { \mathrm { e l } } = ( - 1 ) ^ { n + 1 } \frac { 3 } { ( 2 n + 1 ) ( 2 n + 3 ) } \left( 1 - \frac { c ^ { 2 } } { a ^ { 2 } } \right) ^ { n } } } \end{array}
$$

(Antonov, Timoshkova, & Kholshevnikov 1988, p. 187), where $M$ is the mass of the ellipsoid, $P _ { n } ( x )$ is the Legendre polynomial of order $n$ , and $r$ and $\vartheta$ are the radial distance and the colatitude, respectively. It is easy to see that this expansion converges for $r \ge ( a ^ { 2 } - c ^ { 2 } ) ^ { 1 / 2 }$ . Therefore, this expansion converges everywhere outside of thep ellipsoid (i.e., for p $r \geq c )$ if $c \geq \dot { a } / \sqrt { 2 }$ . The inequality $c \geq a / \sqrt { 2 }$ is true for all the giant planets of the solar system. Moreover, since the density of the giant planets is not constant but becomes larger for smaller $r$ , one should expect that the actual values of $J _ { 2 n }$ are smaller than those ‘‘ predicted ’’ by equation (56). For the few first coefficients $J _ { 2 n }$ this can be seen explicitly: the actual values of $J _ { 2 } , \ J _ { 4 } .$ , and $J _ { 6 }$ given by Weissman et al. (1999) are a factor of 1.7–3.3 smaller than the corresponding coefficients from equation (56). This means that the expansion (eq. [55]) with the actual zonal harmonics $J _ { 2 n }$ of a giant planet converges everywhere outside of that planet. Therefore, for the giant planets, for any light-ray impact parameter it is sufficient to consider the standard expansion of the gravitational potential in terms of spherical harmonics (or, equivalently, multipole moments) and take into account the first few coefficients as discussed above.

The coordinate velocity of the photon can be obtained by taking the time derivative of equation (19):

$$
\pmb { p } \equiv c ^ { - 1 } \pmb { \dot { x } } _ { p } ( t _ { o } ) = \pmb { \sigma } + c ^ { - 1 } \Delta \pmb { \dot { x } } _ { p } ( t _ { o } ) .
$$

The unit coordinate direction of the light propagation at the moment of observation is

$$
\pmb { n } = \pmb { p } / | \pmb { p } | \ .
$$

Equations (57)–(58) are more convenient for numerical calculations than an analytical expansion of $\pmb { n }$ in terms of $\pmb { \sigma }$ and $\Delta \dot { \mathbf { x } } _ { p }$ , which can be derived by substituting equation (57) into equation (58) and expanding in powers of $c ^ { - 1 }$ . However, an accuracy of 1 las can be attained with the simplified firstorder expansion of equations (57)–(58),

$$
\pmb { n } = \pmb { \sigma } + c ^ { - 1 } \pmb { \sigma } \times [ \Delta \dot { \pmb { x } } _ { p } ( t _ { o } ) \times \pmb { \sigma } ] ,
$$

if the distance from the observer to the Sun (all other bodies play no role here) is larger than 0.035 AU, which is the case for all currently proposed astrometric missions. Therefore,

$$
\begin{array} { c } { { \pmb { n } = \pmb { \sigma } + \delta \pmb { \sigma } _ { \mathrm { p N } } + \delta \pmb { \sigma } _ { Q } \mathrm { ~ , ~ } } } \\ { { \delta \pmb { \sigma } _ { \mathrm { p N } } = c ^ { - 1 } \pmb { \sigma } \times \left[ \pmb { \Delta } _ { \mathrm { p N } } \dot { \pmb { x } } _ { p } ( t _ { o } ) \times \pmb { \sigma } \right] \mathrm { ~ , ~ } } } \\ { { \delta \pmb { \sigma } _ { Q } = c ^ { - 1 } \pmb { \sigma } \times \left[ \pmb { \Delta } _ { Q } \dot { \pmb { x } } _ { p } ( t _ { o } ) \times \pmb { \sigma } \right] \mathrm { ~ . ~ } } } \end{array}
$$

Using equation (28), one obtains

$$
\delta \pmb { \sigma } _ { \mathrm { p N } } = - \sum _ { A } \frac { ( 1 + \gamma ) G M _ { A } } { c ^ { 2 } } \frac { { d } _ { A } } { \left| { d } _ { A } \right| ^ { 2 } } \bigg ( 1 + \pmb { \sigma } \cdot \frac { { \pmb { r } } _ { o A } } { \left| { \pmb { r } } _ { o A } \right| } \bigg ) .
$$

Hence, the post-Newtonian deflection angle due to the spherically symmetric part of the gravitational field of body A reads

$$
\delta _ { \mathrm { p N } } = { \frac { ( 1 + \gamma ) G M _ { A } } { c ^ { 2 } | { \bf r } _ { o A } | } } \cot { \frac { \psi _ { A } } { 2 } } \ ,
$$

where $\psi _ { A }$ is the angular distance between body A and the source. It is this formula that was used to compute the data in the third column of Table 1. The effect of the quadrupole field $\delta \pmb { \sigma } _ { Q }$ can be calculated by substituting equations (44)– (47) and (40)–(43) with equations (48)–(53) into equation (62).

# 6.1. Coupling of the Finite Distance to the Source and the Gravitational Deflection: Solar System Objects

The next step is to convert $\pmb { \sigma }$ into the unit vector $\pmb { k }$ directed from the point of emission to the point of observation. Let $\mathbf { \boldsymbol { x } } _ { o } ( t _ { o } )$ be the coordinate of the observer (satellite) at the moment of observation $t _ { o }$ and $\boldsymbol { x } _ { s } ( t _ { e } )$ be the position of the source at the moment of emission $t _ { e }$ of the signal, which was observed at $\boldsymbol { x } _ { o } ( t _ { o } )$ . The moment of emission $t _ { e }$ is considered a function of the moment of observation $t _ { o }$ (see $\ S \ 8$ for further discussion). Let us denote

$$
R = { \bf { x } } _ { o } ( t _ { o } ) - { \bf { x } } _ { s } ( t _ { e } ) , \quad k ( t _ { o } ) = R / | R | .
$$

It is easy to see that the vector $\pmb { k }$ is related to $\pmb { \sigma }$ as

$$
\pmb { \sigma } = \pmb { k } + | \pmb { R } | ^ { - 1 } \pmb { k } \times [ \Delta \pmb { x } _ { p } ( t _ { e } ) \times \pmb { k } ] + O ( c ^ { - 4 } )
$$

(Klioner 1991a). In the case of a solar system object, equation (66) can be combined with equation (59) to obtain

$$
\begin{array} { r } { \pmb { n } = \pmb { k } + \delta \pmb { k } _ { \mathrm { p N } } + \delta \pmb { k } _ { Q } , \qquad } \\ { \delta \pmb { k } _ { \mathrm { p N } } = \pmb { k } \times \left\{ \left[ \left| R \right| ^ { - 1 } \Delta _ { \mathrm { p N } } \pmb { x } _ { p } ( t _ { e } ) + c ^ { - 1 } \Delta _ { \mathrm { p N } } \pmb { \dot { x } } _ { p } ( t _ { o } ) \right] \times \pmb { k } \right\} , } \\ { \delta \pmb { k } _ { Q } = \pmb { k } \times \left\{ \left[ \left| R \right| ^ { - 1 } \Delta _ { Q } \pmb { x } _ { p } ( t _ { e } ) + c ^ { - 1 } \Delta _ { Q } \pmb { \dot { x } } _ { p } ( t _ { o } ) \right] \times \pmb { k } \right\} . } \end{array}
$$

Hence,

$$
\delta k _ { \mathrm { p N } } = - \sum _ { A } \left[ \frac { ( 1 + \gamma ) G M _ { A } } { c ^ { 2 } } \frac { R \times ( r _ { e A } \times r _ { o A } ) } { | R | | r _ { o A } | ( | r _ { e A } | | r _ { o A } | + r _ { o A } \cdot r _ { e A } ) } \right] ,
$$

$$
\pmb { r } _ { e A } = \pmb { x } _ { s } ( t _ { e } ) - \pmb { x } _ { A } ~ .
$$

The angle between vectors $\pmb { k }$ and $\pmb { n }$ due to $\delta \boldsymbol { k } _ { \mathrm { p N } }$ can be calculated as

$$
\frac { ( 1 + \gamma ) G M _ { A } } { c ^ { 2 } | \boldsymbol r _ { o A } | } \mathrm { t a n } \frac { \phi } { 2 } ,
$$

where $\phi$ is the angle between vectors $r _ { e A }$ and $r _ { o A }$ . Note that the angle given by equation (72) depends on the distance $| r _ { o A } |$ between the gravitating body and the point of observation and on $\phi$ but does not depend on the distance $| r _ { e A } |$ between the point of emission and the gravitating body. For a remote source $| r _ { e A } | \to \infty$ and one has $\phi = \pi - \psi _ { A }$ , so that equation (72) coincides with equation (64).

The effect of the quadrupole field $\delta k _ { Q }$ can be calculated by substituting equations (36)–(53) into equation (69). For an object located in the solar system, a set of vectors $\pmb { k }$ calculated from the observed directions $\pmb { S }$ for several different moments of time $t _ { o }$ allows one to determine the barycentric orbit of that object. Therefore, vector $\pmb { k }$ is the final result of the model for the solar system objects.

# 6.2. Coupling of the Finite Distance to the Source and the Gravitational Deflection: Objects Outside of the Solar System

The only effect on $\Delta \ v { x } _ { p }$ that should be taken into account here for objects located outside of the solar system (with $| x _ { s } | > 1 0 0 0$ AU) is the post-Newtonian gravitational deflection from the spherically symmetric part of the gravitational field of the Sun. In this case, from equation (66) one obtains

$$
\begin{array} { r l r } {  { \pmb { \sigma } = \pmb { k } - \frac { ( 1 + \gamma ) G M _ { \mathrm { S u n } } } { c ^ { 2 } | \pmb { R } | } \frac { | \pmb { R } | + | \pmb { r } _ { \mathrm { o S } } | - | \pmb { r } _ { \mathrm { e S } } | } { | \pmb { r } _ { \mathrm { o S } } \times \pmb { r } _ { \mathrm { e S } } | ^ { 2 } } \pmb { R } \times ( \pmb { r } _ { \mathrm { o S } } \times \pmb { r } _ { \mathrm { e S } } ) } } \\ & { } & { +  O ( c ^ { - 4 } ) \ , \qquad } \\ & { } & {  \pmb { r } _ { \mathrm { e S } } = \pmb { x } _ { s } ( t _ { e } ) - \pmb { x } _ { \mathrm { S u n } } , \quad \pmb { r } _ { \mathrm { o S } } = \pmb { x } _ { o } ( t _ { o } ) - \pmb { x } _ { \mathrm { S u n } } \ .  } \end{array}
$$

The angle between $\pmb { \sigma }$ and $\pmb { k }$ can be calculated as

$$
\begin{array} { r l r } {  { \frac { ( 1 + \gamma ) G M _ { \mathrm { S u n } } } { c ^ { 2 } | r _ { \mathrm { o S } } | \sin \psi _ { \mathrm { S u n } } } ( 1 + a - \sqrt { 1 - 2 a \cos \psi _ { \mathrm { S u n } } + a ^ { 2 } } ) } } \\ & { } & { \approx \frac { ( 1 + \gamma ) G M _ { \mathrm { S u n } } } { c ^ { 2 } | R | } [ \cot \frac { \psi _ { \mathrm { S u n } } } { 2 } + O ( a ) ] , } \end{array}
$$

where $a = | r _ { \mathrm { o S } } | / | R |$ and $\psi _ { \mathrm { S u n } }$ is the angular distance between the source and the Sun. The effect reaches 8.5 las for a source situated at a distance of 1 pc and observed at the limb of the Sun. One can check that the angle between $\pmb { k }$ and $\pmb { \sigma }$ is larger than 1 las if $| x _ { s } | \leq 8 . 5$ pc and the source is observed within 2=3 of the Sun. If at least one of these conditions is violated (which is really the case for all currently proposed astrometric missions, since no observations can be done so close to the Sun), one can set

$$
{ \pmb \sigma } = { \pmb k } \mathrm { ~ . ~ }
$$

Let us note that the requirement of calculating the gravitational effects with an accuracy of 1 las places a constraint on the accuracy of the planetary ephemerides (roughly speaking, one has to be able to calculate the impact parameter of the light ray with respect to each gravitating body with sufficient accuracy). The required accuracy of the ephemerides also depends on the minimal allowed angular distance between the source and the gravitating body. For a grazing ray, the barycentric position of Jupiter should be known with an accuracy of $4 ~ \mathrm { k m }$ , and those of the other planets with slightly lower accuracy. The barycentric position of the Sun should be known with an accuracy of about $4 0 0 \mathrm { ~ m ~ }$ for a grazing ray, and with an accuracy of ${ \sim } 6 0 0 0 ~ \mathrm { k m }$ for the minimal allowed angular distance of $3 5 ^ { \circ }$ as adopted for $G A I A$ . Note that since the model involves the relative positions of the satellite and the gravitating bodies, the barycentric position of the satellite must be known with at least the same accuracy, that is, ${ \sim } 4 \ \mathrm { k m }$ (see $\ S \ S . 4$ of ESA 2000 for other accuracy constraints).

# 7. PARALLAX

Only the sources situated outside of the solar system will be considered below. For these objects, the next step of the model is to eliminate the parallax, that is, to transform $\pmb { k }$ into the unit vector $\iota$ directed from the barycenter of the solar system to the source:

$$
\begin{array} { r } { \pmb { l } ( t ) = \pmb { x } _ { s } ( t _ { e } ) / | \pmb { x } _ { s } ( t _ { e } ) | \ . } \end{array}
$$

Note that, starting from this point, further parameterization of vectors $\pmb { k }$ and $\imath$ formally coincides with what one could expect in the Newtonian framework. From the formal mathematical point of view, these vectors may be considered ‘‘ Euclidean vectors ’’ in the three-dimensional coordinate space formed by the spatial coordinates of the BCRS. It is important to understand, however, that this interpretation is only formal and that those vectors are not Euclidean vectors in some ‘‘ underlying Euclidean physical space,’’ but rather integration constants for the equations of light propagation in the BCRS. These vectors are defined by the entire preceding model of relativistic reduction and would change if the model were changed (e.g., if another relativistic reference system were used instead of the BCRS).

Here definitions of the parallax, proper motion, and radial velocity compatible with general relativity at a level of 1 las (or better) are suggested. Although the definitions are quite simple and straightforward, their interpretation at such a high level of accuracy is rather unusual from the point of view of classical Newtonian astrometry. As will become clear below, parallax and proper motion are no longer two separate effects that can be considered independently of each other. The second-order parallaxes and proper motions, as well as the effects resulting from the interaction between these two effects, are important. Moreover, parallax, proper motion, and other astrometric parameters are coordinate-dependent parameters defined in the BCRS, which is used as the relativistic reference system where the position and motion of the sources are described. Therefore, these parameters have some meaning only within a particular chosen model of relativistic reductions. That is why the whole relativistic model of positional observations must be considered to define these parameters and clarify their meaning.

Let us define several parameters. The parallax of the source is defined as

$$
\pi ( t _ { o } ) = \frac { 1 \mathrm { \ A U } } { | \boldsymbol { x } _ { s } ( t _ { e } ) | } \ ,
$$

the parallactic parameter $\mathbf { I I }$ is given by

$$
\Pi ( t _ { o } ) = \pi ( t _ { o } ) \frac { { \bf x } _ { o } ( t _ { o } ) } { 1 \mathrm { ~ A U } } ,
$$

and finally the observed parallactic shift of the source is defined as

$$
\pmb { \pi } ( t _ { o } ) = \pmb { l } ( t _ { o } ) \times \left[ \pmb { \Pi } ( t _ { o } ) \times \pmb { l } ( t _ { o } ) \right] .
$$

With these definitions, to sufficient accuracy one has

$$
{ \pmb k } = - l ( 1 - \textstyle { \frac { 1 } { 2 } } | { \pmb \pi } | ^ { 2 } ) + { \pmb \pi } ( 1 + l \cdot \pmb { \Pi } ) + O ( \pi ^ { 3 } ) .
$$

The second-order effects in equation (81) proportional to $\pi ^ { 2 }$ are less than 3 las if $\left| x _ { s } \right| \geq 1$ pc. For an accuracy of $1 ~ \mu \mathrm { { a s } }$ , the second-order terms can be safely neglected if $| \pmb { x } _ { s } | \geq 2 \mathrm { p c }$ .

# 8. PROPER MOTION

The last step of the algorithm is to provide a reasonable parameterization of the time dependence of $\iota$ and $\pi$ caused by the motion of the source relative to the barycenter of the solar system.

It is commonly known that in order to convert an observed proper motion and an observed radial velocity into true tangential and radial velocities of the observed object, additional information is required. Since that information is not always available, the concepts of ‘‘ apparent proper motion,’’ ‘‘ apparent tangential velocity,’’ and ‘‘ apparent radial velocity ’’ are suggested below. These concepts represent useful information about the observed object and should be distinguished from the ‘‘ true tangential velocity ’’ and ‘‘ true radial velocity.’’ Definitions of all these concepts are discussed below.

In the present paper, the following simple model for the coordinates of the source is adopted:

$$
\begin{array} { r } { \pmb { x } _ { s } ( t _ { e } ) = \pmb { x } _ { s } ( t _ { e } ^ { 0 } ) + V \Delta t _ { e } + \frac { 1 } { 2 } A \Delta t _ { e } ^ { 2 } + O ( \Delta t _ { e } ^ { 3 } ) . } \end{array}
$$

Here $\Delta t _ { e } = t _ { e } - t _ { e } ^ { 0 }$ and $V$ and $\pmb { A }$ are the BCRS velocity and acceleration of the source evaluated at the moment of emission $t _ { e } ^ { 0 }$ , corresponding to the initial epoch of observation $t _ { o } ^ { 0 }$ . This model allows one to consider single stars or components of gravitationally bounded systems, the periods of which are much larger than the time span covered by observations. Depending on the particular properties of the source and on the time span of observations, higher order terms in equation (82) can also be considered. It is also clear that in more complicated cases special solutions for binary stars, etc., should be considered. For objects in double or multiple systems for which it is possible to determine the orbit, equation (82) gives the coordinates of the center of mass of the system. The obvious correction should be added to the right-hand side of equation (82) in order to account for the orbital motion of the object. This case will not be considered here. In this paper we confine ourselves to equation (82) only.

Substituting equation (82) into the definitions of $\imath$ and $\pi$ one obtains

$$
\begin{array} { l } { { \pi ( t _ { o } ) = \pi _ { 0 } + \dot { \pi } _ { 0 } \Delta t _ { e } + \frac { 1 } { 2 } \dot { \pi } _ { 0 } \Delta t _ { e } ^ { 2 } + O ( \Delta t _ { e } ^ { 3 } ) , } } \\ { { \dot { \pi } _ { 0 } = - \pi _ { 0 } \frac { { \cal I } _ { 0 } \cdot { \cal F } } { | x _ { s } ( t _ { e } ^ { 0 } ) | } , } } \\ { { \dot { \pi } _ { 0 } = - \pi _ { 0 } \frac { { \cal I } _ { 0 } \cdot { \cal A } } { | x _ { s } ( t _ { o } ^ { 0 } ) | } - \pi _ { 0 } | \dot { \cal I } _ { 0 } | ^ { 2 } + 2 \frac { \dot { \pi } _ { 0 } ^ { 2 } } { \pi _ { 0 } } , } } \\ { { \dot { \pi } ( t _ { o } ) = { \cal I } _ { 0 } + \dot { \cal I } _ { 0 } \Delta t _ { e } + \frac { 1 } { 2 } \dot { \pi } _ { 0 } \Delta t _ { e } ^ { 2 } + O ( \Delta t _ { e } ^ { 3 } ) , } } \\ { { \dot { \cal I } _ { 0 } = \frac { 1 } { | x _ { s } ( t _ { e } ^ { 0 } ) | } { | x _ { s } ( t _ { o } ^ { 0 } ) | } { \cal I } _ { 0 } \times \left( { \cal V } \times { \cal I } _ { 0 } \right) , } } \\ { { \dot { \cal I } _ { 0 } = \frac { 1 } { | x _ { s } ( t _ { e } ^ { 0 } ) | } { \cal I } _ { 0 } \times \left( 4 \times { \cal I } _ { 0 } \right) - \left| \dot { \cal I } _ { 0 } \right| ^ { 2 } { \cal I } _ { 0 } + 2 \frac { \dot { \pi } _ { 0 } } { \pi _ { 0 } } \dot { \cal I } _ { 0 } , } } \end{array}
$$

where $\pi _ { 0 } = \pi ( t _ { o } ^ { 0 } ) = ( 1 \mathrm { A U } ) / | x _ { s } ( t _ { e } ^ { 0 } ) |$ and $\begin{array} { r } { l _ { 0 } = I ( t _ { o } ^ { 0 } ) = } \end{array}$ $\pmb { x } _ { s } ( t _ { e } ^ { 0 } ) / | \pmb { x } _ { s } ( t _ { e } ^ { 0 } ) |$ are the parameters at the initial epoch of observation $t _ { o } ^ { 0 }$ .

The signals emitted at moments $t _ { e } ^ { 0 }$ and $t _ { e }$ are received by the observer at moments $t _ { o } ^ { 0 }$ and $t _ { o }$ , respectively. The corresponding moments of emission and reception are related by

$$
c ( t _ { o } - t _ { e } ) = | { \pmb x } _ { o } ( t _ { o } ) - { \pmb x } _ { s } ( t _ { e } ) | - { \pmb k } ( t _ { o } ) \bullet \Delta { \pmb x } _ { p } ( t _ { o } ) ,
$$

and by a similar equation for the moments $t _ { o } ^ { 0 }$ and $t _ { e } ^ { 0 }$ . The term proportional to $\Delta \ v { x } _ { p }$ represents the gravitational signal retardation (the Shapiro effect) due to the gravitational field of the solar system. For any source in the observed part of the universe, the Shapiro effect due to the gravitational field of the solar system is less than $1 0 ^ { - 3 } \mathrm { ~ s ~ }$ and can be safely neglected here. Let us denote by $\Delta t _ { o } = t _ { o } - t _ { o } ^ { 0 }$ the time span of observations corresponding to the time span $\begin{array} { r } { \dot { \Delta t } _ { e } = t _ { e } - t _ { e } ^ { 0 } } \end{array}$ of emission. These two time intervals are related by

$$
\begin{array} { l } { \displaystyle \Delta t _ { e } = \left( 1 + \frac { 1 } { c } { \boldsymbol l } _ { 0 } \cdot { \boldsymbol V } \right) ^ { - 1 } \Delta t _ { o } } \\ { \displaystyle \quad \quad + \frac { 1 } { c } { \boldsymbol l } _ { 0 } \bullet [ { \boldsymbol x } _ { o } ( t _ { o } ) - { \boldsymbol x } _ { o } ( t _ { o } ^ { 0 } ) ] \biggl ( 1 + \frac { 1 } { c } { \boldsymbol l } _ { 0 } \cdot { \boldsymbol V } \biggr ) ^ { - 1 } } \\ { \displaystyle \quad - \frac { 1 } { 2 c } \biggl ( { \boldsymbol l } _ { 0 } \bullet { \boldsymbol A } + \frac { | { \boldsymbol l } _ { 0 } \times { \boldsymbol V } | ^ { 2 } } { | { \boldsymbol x } _ { s } ( t _ { e } ^ { 0 } ) | } \biggr ) \Delta t _ { o } ^ { 2 } + \cdots ~ . } \end{array}
$$

Equation (90) results from a double Taylor expansion of the first term on the right-hand side of equation (89) in powers of the parallax $\pi$ and $\Delta t _ { e }$ . Many terms have been neglected here because they were estimated to produce negligible observable effects. Which terms of such an expansion are important depends on many factors. The constraints used here to derive equation (90) are $\pi _ { 0 } \leq 1 ^ { \prime \prime }$ , proper motion $| \dot { \pmb { l } } | \le 1$ las $\mathrm { s } ^ { - 1 } \approx \hat { 3 } 2 ^ { \prime \prime } \ \mathrm { y r } ^ { - 1 }$ , accuracy of position determination for a single observation not better than 1 las, and lifetime of the mission not longer than 5 yr; the effects of the acceleration $\pmb { A }$ of the object were supposed to be smaller than those of the velocity $V$ (i.e., $A < 2 V / \Delta t _ { e } )$ . For other constraints, other terms in the expansion may become important.

The second term in equation (90) represents a quasiperiodic effect with amplitude ${ \sim } | \mathbf { x } _ { o } | / c \approx 5 0 0$ s for a satellite located not too far from Earth orbit. Below it will be shown that this term produces a significant periodic term in the apparent proper motion of sources with sufficiently large proper motions.

It is easy to see from equations (83)–(88) that the time dependence of parallax and proper motion characterized by the parameters $\dot { \pi } _ { 0 }$ and $\ddot { \boldsymbol { l } } _ { 0 }$ can be used to determine the radial velocity of the source. This question has recently been investigated in full detail and applied to Hipparcos data by Dravins, Lindegren, & Madsen (1999). The tangential and radial components of the barycentric velocity $V$ of the source can be defined as

$$
V _ { \mathrm { t a n } } = l _ { 0 } \times ( V \times l _ { 0 } ) , \quad V _ { \mathrm { r a d } } = l _ { 0 } \cdot V .
$$

Equations (83)–(88) can be combined with equation (90) to find the time dependence of $\iota$ and $\pi$ . Collecting the terms linear with respect to $\Delta t _ { o }$ , we get the definition of the appagential velocity rent proper motion $V _ { \mathrm { t a n } } ^ { \mathrm { a p } }$ ${ \pmb { \mu } } _ { \mathrm { a p } }$ as appeared in the linear term in and the corresponding apparent tan- $\boldsymbol { l } ( t _ { o } )$ and the definition of the apparent radial velocity V ap as appeared in the linear term in $\pi ( t _ { o } )$ :

$$
\begin{array} { r l r } { \displaystyle { \boldsymbol { V } } _ { \mathrm { t a n } } ^ { \mathrm { a p } } = { \boldsymbol { l } } _ { 0 } \times ( { \boldsymbol { V } } \times { \boldsymbol { l } } _ { 0 } ) ( 1 + c ^ { - 1 } { \boldsymbol { l } } _ { 0 } \cdot { \boldsymbol { V } } ) ^ { - 1 } } & \\ { \displaystyle = { \boldsymbol { V } } _ { \mathrm { t a n } } ( 1 + c ^ { - 1 } V _ { \mathrm { r a d } } ) ^ { - 1 } ~ , } & { ( 9 } \\ { \displaystyle { \boldsymbol { \mu } } _ { \mathrm { a p } } = \frac { 1 } { \left| { \boldsymbol { x } } _ { s } \left( { \boldsymbol { t } } _ { e } ^ { 0 } \right) \right| } { \boldsymbol { l } } _ { 0 } \times ( { \boldsymbol { V } } \times { \boldsymbol { l } } _ { 0 } ) \left( 1 + \frac { { \boldsymbol { l } } _ { 0 } } { c } \cdot { \boldsymbol { V } } \right) ^ { - 1 } = \pi _ { 0 } \frac { V _ { \mathrm { t a n } } ^ { \mathrm { a p } } } { 1 ~ \mathrm { A U } } ~ , } & \end{array}
$$

$$
V _ { \mathrm { r a d } } ^ { \mathrm { a p } } = l _ { 0 } \bullet V ( 1 + c ^ { - 1 } l _ { 0 } \bullet V ) ^ { - 1 } = V _ { \mathrm { r a d } } ( 1 + c ^ { - 1 } V _ { \mathrm { r a d } } ) ^ { - 1 } .
$$

With these definitions, the simplest possible models for $\pi ( t _ { o } )$ and $\boldsymbol { l } ( t _ { o } )$ read (the higher order terms are neglected here in order to make this example more transparent):

$$
\begin{array} { r l r } & { } & { \pi ( t _ { o } ) = \pi _ { 0 } - \pi _ { 0 } ^ { 2 } \frac { V _ { \mathrm { r a d } } ^ { \mathrm { a p } } } { 1 \mathrm { \ A U } } \Delta t _ { o } + \cdots , \qquad ( 9 \le \Delta \xi \le 1 ) , } \\ & { } & { l ( t _ { o } ) = l _ { 0 } + \mu _ { \mathrm { a p } } \Delta t _ { o } + \mu _ { \mathrm { a p } } c ^ { - 1 } \{ [ { \pmb x } _ { o } ( t ) - { \pmb x } _ { o } ( t _ { 0 } ) ] \bullet l _ { 0 } \} + \cdots . } \end{array}
$$

The factor of $( 1 + c ^ { - 1 } l _ { 0 } \cdot V ) ^ { - 1 }$ in equations (92)–(94) has been discussed by, for example, Stumpff (1985) and Klioner & Kopeikin (1992). If vectors $\boldsymbol { l } _ { 0 }$ and $V$ are nearly antiparallel and $\vert V \vert$ is large, this factor may become large enough that the apparent tangential and radial velocities may even exceed light velocity. This phenomenon is one of the wellknown possible explanations of apparent superluminal motions.

The amplitude of the third term in equation (96) is about 150 las for Barnard’s star, with its proper motion of $1 0 _ { \cdot } ^ { \prime \prime } 4 \mathrm { y r } ^ { - 1 }$ (see Brumberg et al. 1990; Klioner & Kopeikin 1992). In general, the amplitude of this effect is approximately equal to the proper motion of the source during the time interval ${ \sim } | \mathbf { x } _ { o } | / c$ required for the light to propagate from the observer to the barycenter of the solar system, multiplied by cosine of the ecliptic latitude of the source. Therefore, for a satellite not too far from Earth orbit, where $| \boldsymbol { x } _ { o } | /$ $c \sim 5 0 0 ~ \mathrm { s }$ , this effect exceeds 1 las for all stars with proper motions larger than ${ \sim } 6 3 \mathrm { \ m a s } \mathrm { \ y r } ^ { - 1 }$ . This effect is closely related to the Roemer effect used in the 17th century to measure the velocity of light. Its potential importance for astrometry was recognized by Schwarzschild (1894) and later discussed in detail by Stumpff (1985). The Roemer effect is a standard part of typical relativistic models for pulsar timing (see, e.g., Doroshenko & Kopeikin 1990).

The apparent radial velocity $V _ { \mathrm { r a d } } ^ { \mathrm { a p } }$ can be immediately used to calculate the true radial velocity $V _ { \mathrm { r a d } }$ . Therefore, if both the apparent tangential and apparent radial velocities are determined from observations, one can immediately restore the true tangential velocity $V _ { \mathrm { t a n } }$ . However, even if this is not the case, the apparent velocity $V _ { \mathrm { t a n } } ^ { \mathrm { a p } }$ can be useful by itself. Note that the radial velocities measured by Doppler (spectral) observations are neither true nor apparent radial velocity in our terminology. The shift of spectral lines is affected by a number of factors that do not appear in positional observations (various gravitational redshifts and Doppler effects; see, e.g., the detailed discussion by Kopeikin & Ozernoy 1999). The relativistic effects induced by the motion of the satellite and by the gravitational field of the solar system in the Doppler measurements are typically on the order of a few centimeters per second, which is probably too small to be detectable by space astrometry missions (e.g., GAIA will measure the Doppler shift of spectral lines with an accuracy of about $1  { \mathrm { k m } }  { \mathrm { s } } ^ { - 1 }$ ). Therefore, it is only the intrinsic redshift due to local physics of the object that should be considered (see, e.g., Reid 1996).

# 9. SUMMARY OF THE MODEL

A practical implementation of the model can be summarized as follows:

A. Determine the orbit (the position $x _ { o }$ and the velocity $\dot { \mathbf { x } } _ { o } )$ of the satellite with respect to the BCRS $( \ S 4 )$ . B. Reparameterize the observed directions $\pmb { S }$ by the coordinate time t of the BCRS (to this end, eq. [1] should be numerically integrated along the orbit of the satellite). C. Use equations (9)–(12) to convert the observed direction $\pmb { S }$ to the source into the unit BCRS direction $\pmb { n }$ of the light ray at the point of observation.

$\mathrm { D } _ { 1 }$ . For objects situated outside of the solar system, use equations (60), (63), and (62) with equations (44)–(47), (40)–(43) and (48)–(53), and (76) to convert $\pmb { n }$ into the unit BCRS direction $\pmb { k }$ from the source to the observer at the moment of observation; in order to judge whether the light deflection due to a particular gravitating body should be considered here, one can use equation (64) and the maximal angular distances given in Table 1.

$\mathrm { D } _ { 2 }$ . For solar system objects, use equations (67), (70), and (69) with equations (36)–(53) to convert $\pmb { n }$ into $\pmb { k }$ (a set of vectors $\pmb { k }$ for several moments of time can be used to determine the BCRS orbit of the object, which represents the final outcome for a solar system body); equations (64), (72), and the maximal angular distances given in Table 1 can again be used to judge whether a particular gravitating body should be taken into account here.

![](images/ef562b5c2a0a6ec3179307f87ef9fb99d4b212604245e2aa603f58ab5cbfe310.jpg)  
Fig. 4.—Structure of the model for different kinds of objects (see text).

E. Use equation (81) with equations (78)–(80) to take into account the parallax of the object and to convert $\pmb { k }$ into the unit BCRS direction $\imath$ from the barycenter of the solar system to the source.

F. Use an appropriate model for the time dependence of l and, possibly, that of the parallactic parameter $\pi$ to account for the proper motion of the source (a reasonable model for single sources is given in $\ S 8$ ).

The sequence of the steps of the model is depicted in Figure 4.

# 10. THE MODEL FOR 0.1 las

Since the technical accuracy of GAIA is expected to reach 4 las for 12th magnitude stars and brighter, and the technical accuracy of SIM is also expected to attain a level of 3–4 las, it is interesting to look at the relativistic model with an accuracy of 0.1 las, which guarantees that all systematic effects at the level of 1 las are properly taken into account. The relativistic effects related to the gravitational potential of the solar system bodies and to the motion of the observer with respect to the barycenter of the solar system can be modeled with an accuracy of 0.1 las within the same scheme discussed above and summarized in the previous section. The necessary changes to attain 0.1 las accuracy are as follows:

Step $A .$ .—The barycentric velocity of the satellite should be known with an accuracy of $1 0 ^ { - 4 } \dot { \mathrm { m } } \mathrm { s } ^ { - 1 }$ . This also requires the use of equation (6) if the GCRS is used for orbit determination.

Step $D$ .—Some additional effects should be taken into account in the gravitational light deflection (see also Table 1):

1. The effect explicitly proportional to the velocity of the bodies should be taken into account when observing within 8 angular radii of Jupiter or 2 angular radii of Saturn. As discussed in $\ S \ O 6$ , the difference between $t _ { A , 0 } ^ { \mathrm { r } }$ and $t _ { A , 0 } ^ { \mathrm { c a } }$ A;0 still plays no role at this level of accuracy. The explicit formulae have been published in Klioner (1989), Klioner & Kopeikin (1992), and Kopeikin & Scha¨fer (1999).

2. The effect of the rotational motion of Jupiter should be taken into account when observing within 1.4 times its apparent radius (i.e., within $4 2 ^ { \prime \prime } { - } 6 9 ^ { \prime \prime }$ of Jupiter’s center). Explicit formulae for this effect have been published in Klioner (1991a) and Klioner & Kopeikin (1992).

3. The effect of the $J _ { 4 }$ of Jupiter exceeds 0.1 las within 2.5 times its apparent radius $( \bar { 3 } 7 ^ { \prime \prime }  – 6 1 ^ { \prime \prime }$ from Jupiter’s center); the same effect for Saturn exceeds 0.1 las within 2.2 times its apparent radius $1 5 ^ { \prime \prime } – 2 2 ^ { \prime \prime }$ from its center). The effect of $J _ { 6 }$ (Weissman et al. 1999, p. 342) of both Jupiter and Saturn may exceed 0.1 las within 1.3 times the apparent radius of each planet. Explicit formulae for the influence of $J _ { 4 }$ and $J _ { 6 }$ have been published by Kopeikin (1997).

4. All the bodies with radii $L$ such that

$$
L \geq \left( \frac { \rho } { 1 \mathrm { ~ g ~ c m } ^ { - 3 } } \right) ^ { - 1 / 2 } 1 9 7 \mathrm { ~ k m } ,
$$

where $\rho$ is the mean density of the body, can produce light deflection on the order of 0.1 las and should be taken into account. This makes it quite difficult to reduce the observations near the ecliptic, where a large number of small bodies satisfying this condition can be expected.

5. The maximal angular distances at which the influence of a gravitating body should be taken into account should be increased as compared with Table 1 to meet the goal accuracy of 0.1 las. The post–post-Newtonian light deflection reaches 0.1 las only for observations within 2=3 of the Sun and therefore can be neglected for the currently planned space missions.

6. Coupling of the finite distance to the source and the gravitational deflection for sources located outside of the solar system $( \ S \ : \ : 6 . 2 )$ should be taken into account if $\left| x _ { s } \right| \leq 8 5$ pc and the source is observed within 22=7 of the Sun. Although the effect can be neglected for the current technical specifications of the planned space missions, it may become important because a Sun avoidance angle of ${ \sim } 2 \bar { 3 } ^ { \circ }$ is not technically impossible.

Step $E .$ —The second-order parallactic effects should be taken into account if $| x _ { s } | \le 5 . 5$ pc.

Step $F .$ —The model for the proper motion $( \ S \ 8 )$ should be correspondingly refined. In particular, the third term in equation (96) becomes important for all stars with proper motions larger than ${ \sim } 0 . { } ^ { \prime \prime } 6 2 \bar { \mathrm { y r } } ^ { - 1 }$ .

Note also that additional relativistic effects due to various gravitational fields generated outside of the solar system (see $\ S$ 11 below and Kopeikin & Gwinn 2000) become even more important at the level of 0.1 las and should be thoroughly taken into account.

# 11. WHAT IS BEYOND THE MODEL

The relativistic model proposed above can be considered a ‘‘ standard ’’ model suitable for all sources. This model allows one to reduce the observational data with an accuracy of 1 las and restore positions and other parameters of the objects (e.g., their velocities) defined in the BCRS. The model properly takes into account the gravitational field of the solar system, but it ignores a number of possible effects that may be caused by gravitational fields produced outside of the solar system. Let us review some of these effects (see also Kopeikin & Gwinn 2000).

The first additional effect to mention here is so-called weak microlensing, which is simply an additional gravitational deflection of the light coming from a distant source that is produced by the gravitational field of a visible or invisible object situated near the light path between the observed source and the observer. For applications in highprecision astrometry, one should distinguish between microlensing events and microlensing noise. A microlensing event is a time-dependent change of the source’s position (and possibly its brightness) that is large and clear enough to be identified as such. Microlensing events can be used to determine physical properties of the lens, so that the unperturbed path of the source can be restored at the end (e.g., Hosokawa et al. 1993, 1995; Høg, Novikov, & Polnarev 1995; Belokurov & Evans 2002). In this sense, microlensing events represent no fundamental problem for future astrometric missions. On the other hand, microlensing noise comes from unidentified microlensing events (which are too weak or too fast to be detected as such). The number of such unidentified microlensing events will clearly be much higher than the number of identified ones. The microlensing noise results in stochastic changes in the positions of the observed sources with unpredictable (but generally small) amplitude and at unpredictable moments of time. Therefore, microlensing noise can spoil the determination of positions, parallaxes, and proper motions of the objects (Zhdanov 1995; Zhdanov & Zhdanova 1995; Hosokawa, Ohnishi, & Fukushima 1997; Sazhin et al. 1998; Sazhin, Zharov, & Kalinina 2001; Belokurov & Evans 2002). It is currently not quite clear to what extent the microlensing noise produced by the objects of the Galaxy can deteriorate the catalogs resulting from future astrometric missions. To clarify this question, data simulations similar to those described by de Felice et al. (2000) but involving a model for microlensing with a realistic model for the Galaxy would be of much help. The first simulation of this kind has been performed by Belokurov & Evans (2002), who conclude that microlensing noise presents no problem for GAIA. On the other hand, the level of ${ \sim } 1$ las seems to be close to a fundamental limit of astrometric accuracy, since at much higher accuracies the stochastic influence of microlensing noise becomes so strong that, in too many cases, measurable relativistic deflection effects cannot be properly taken into account (Sazhin et al. 1998, 2001).

In edge-on binary (or multiple) systems, the gravitational light deflection due to the gravitational field of the companion may be observable. In the case of timing observations of binary pulsars, this question has been thoroughly investigated by Doroshenko & Kopeikin (1995). It is clear that for companions with stellar masses, the inclination of the orbit should be very close to $9 0 ^ { \circ }$ for the effect to be observable at a level of 1 las. The formulae of $\ S \ G . 1$ can be directly used here to calculate the effect in the first post-Newtonian approximation. If the lensing companion is a neutron star or a black hole, it is necessary to investigate the lensing effect in the strong-field regime and also to consider secondary images (a detailed study of the appearance of a star orbiting a Kerr black hole in the strong-field regime is given by Cunningham & Bardeen 1972, 1973). Further investigation is necessary to estimate the probability of observing a binary system for which the gravitational lensing of the companion is important at the 1 las level.

Gravitational waves can in principle produce gravitational light deflection. Two cases should be distinguished here: (1) gravitational waves from binary stars and other compact sources and (2) stochastic primordial gravitational waves from the early universe. Gravitational waves from a single compact source have been shown to produce an utterly small deflection that is hardly observable at the level of 1 las (Kopeikin et al. 1999). However, the ensemble of compact sources of gravitational waves in the Galaxy (e.g., binary stars) may produce a larger cumulative effect, which should be thoroughly estimated (see, e.g., Kopeikin 1999 for an attempt of such an estimation in pulsar timing measurements). The influence of primordial gravitational waves was analyzed by Pyne et al. (1996) and Gwinn et al. (1997). Although initially applied to very long baseline interferometry, these authors’ method can be used directly for optical astrometry.

Finally, cosmological effects should be accounted for to interpret the derived parameters of the objects (e.g., a parallax accuracy of $\sigma _ { \pi } = 1$ las allows one to measure the distance to objects as far as ${ \sim } 1 \ \mathrm { M p c }$ away from the solar system; see, e.g., Kristian & Sachs 1966 for a discussion of astrometric consequences of cosmology). It may be interesting here to construct the metric tensor of the BCRS with a cosmological solution as a background and analyze the effects of the background cosmology in such a reference system.

Last but not least, an observational accuracy of 1 las, together with a mission lifetime of at least 5 years, allows one to see the apparent proper motions of quasars and other remote sources due to the acceleration of the solar system barycenter relative to the center of the Galaxy (ESA 2000, $\ S \ 1 . 8 . 1 0 )$ . These proper motions should be on the order of ${ \sim } 4 \mu { \mathrm { a s } } \mathrm { y r } ^ { - 1 }$ , if one assumes the solar system to be on a circular orbit around the Galactic center.

The author is grateful to F. Mignard, M. Soffel, S. Kopeikin, and M. Lattanzi for fruitful discussions and suggestions.

# REFERENCES

Antonov, V. A., Timoshkova, E. I., & Kholshevnikov, K. V. 1988, Vvedenie v teoriiu n’iutonovskogo potentsiala (Moscow: Nauka)   
Bienayme´, O., & Turon, C., eds. 2002, GAIA: A European Space Project (Les Ulis: EDP Sci.)   
Belokurov, V. A., & Evans, N. W. 2002, MNRAS, 331, 649   
Brumberg, V. A. 1986, in IAU Symp. 109, Astrometric Techniques, ed. H. K. Eichhorn & R. J. Leacock (Dordrecht: Reidel), 19 . 1991, Essential Relativistic Celestial Mechanics (Bristol: Hilger)   
Brumberg, V. A., Klioner, S. A., & Kopeikin, S. M. 1990, in IAU Symp. 141, Inertial Coordinate System on the Sky, ed. J. H. Lieske & V. K. Abalakin (Dordrecht: Kluwer), 229   
Brumberg, V. A., & Kopeikin, S. M. 1989a, in Reference Frames in Astronomy and Geophysics, ed. J. Kovalevsky, I. I. Mueller, & B. Kooaczek (Dordrecht: Kluwer), 115 . 1989b, Nuovo Cimento B, 103, 63   
Cunningham, C. T., & Bardeen, J. M. 1972, ApJ, 173, L137 . 1973, ApJ, 183, 237   
Damour, T., Soffel, M., & Xu, C. 1991, Phys. Rev. D, 43, 3273 Damour, T., Soffel, M., & Xu, C. 1992, Phys. Rev. D, 45, 1017 . 1993, Phys. Rev. D, 47, 3124 . 1994, Phys. Rev. D, 49, 618 de Felice, F., Bucciarelli, B., Lattanzi, M. G., & Vecchiato, A. 2001, A&A,   
373, 336 de Felice, F., Lattanzi, M. G., Vecchiato, A., & Bernacca, P. L. 1998, A&A,   
332, 1133 de Felice, F., Vecchiato, A., Bucciarelli, B., Lattanzi, M. G., & Crosta, M.   
2000, in Towards Models and Constants for Sub-Microarcsecond Astrometry, ed. K. J. Johnston, D. D. McCarthy, B. J. Luzum, & G. H. Kaplan (Washington: US Nav. Obs.), 314 Doroshenko, O. V., & Kopeikin, S. M. 1990, AZh, 67, 986 (English transl. Soviet Astron., 34, 496) . 1995, MNRAS, 274, 1029 Dravins, D., Lindegren, L., & Madsen, S. 1999, A&A, 348, 1040 ESA. 2000, GAIA: Composition, Formation and Evolution of the Galaxy, Concept and Technology Study Report (ESA-SCI[2000]4) (Noordwijk: ESA) Fricke, W., Duncombe, R. L., Seidelmann, P. K., & Wilins, G. A. 1977, Trans. IAU, 16B, 56 Fukushima, T. 1995, A&A, 294, 895 Gwinn, C. R., Eubanks, T. M., Pyne, T., Birkinshaw, M., & Matsakis, D. N. 1997, ApJ, 485, 87 Høg, E., Novikov, I. D., & Polnarev, A. G. 1995, A&A, 294, 287 Hosokawa, M., Ohnishi, K., & Fukushima, T. 1997, AJ, 114, 1508 Hosokawa, M., Ohnishi, K., Fukushima, T., & Takeuti, M. 1993, A&A,   
278, L27   
1995, in IAU Symp. 166, Astronomical and Astrophysical Objectives of Sub-Milliarcsecond Optical Astrometry, ed. E. Høg & P. K. Seidelmann (Dordrecht: Kluwer), 305 IAU. 2001, IAU Inf. Bull., No. 88, 29 (erratum No. 89, 4 [2002]) Irwin, A. W., & Fukushima, T. 1999, A&A, 348, 642 Klioner, S. A. 1989, Soobschch. Inst. Prikl. Astron., No. 6 . 1991a, AZh, 68, 1046 (English transl. Soviet Astron., 35, 523) . 1991b, Ph.D. thesis, St. Petersburg State Univ. . 1993, A&A, 279, 273 . 2000, in Towards Models and Constants for Sub-Microarcsecond Astrometry, ed. K. J. Johnston, D. D. McCarthy, B. J. Luzum, & G. H. Kaplan (Washington: US Nav. Obs.), 308 Klioner, S. A., & Kopeikin, S. M. 1992, AJ, 104, 897 Klioner, S. A., & Soffel, M. 1998a, A&A, 334, 1123 . 1998b, Phys. Rev. D, 58, No. 84023 Klioner, S. A., & Soffel, M. H. 2000, Phys. Rev. D, 62, No. 24019 Klioner, S. A., & Voinov, A. V. 1993, Phys. Rev. D, 48, 1451 Kopeikin, S., & Mashhoon, B. 2002, Phys. Rev. D, 65, No. 64025 Kopeikin, S. M. 1988, Celest. Mech., 44, 87 . 1997, J. Math. Phys., 38, 2587 . 1999, preprint (gr-qc/9903070) Kopeikin, S. M., & Gwinn, C. 2000, in Towards Models and Constants for Sub-Microarcsecond Astrometry, ed. K. J. Johnston, D. D. McCarthy, B. J. Luzum, & G. H. Kaplan (Washington: US Nav. Obs.), 303 Kopeikin, S. M., & Ozernoy, L. M. 1999, ApJ, 523, 771   
Kopeikin, S. M., & Scha¨fer, G. 1999, Phys. Rev. D, 60, No. 124002   
Kopeikin, S. M., Scha¨fer, G., Gwinn, C. R., & Eubanks, T. M. 1999, Phys. Rev. D, 59, No. 84023   
Kopeikin, S. M., Shuygina, N., Vasiliev, M., Yagudina, E., & Yagudin, L. 2000, in Towards Models and Constants for Sub-Microarcsecond Astrometry, ed. K. J. Johnston, D. D. McCarthy, B. J. Luzum, & G. H. Kaplan (Washington: US Nav. Obs.), 320   
Kristian, J., & Sachs, R. K. 1966, ApJ, 143, 379   
Mashhoon, B. 1974, Nature, 250, 316   
McCarthy, D. D., ed. 1996, IERS Conventions (1996) (IERS Tech. Note 21) (Paris: Obs. Paris), chap. 11   
Misner, C. W., Thorne, K. S., & Wheeler, J. A. 1973, Gravitation (San Francisco: Freeman)   
Perryman, M. A. C., et al. 2001, A&A, 369, 339   
Pyne, T., Gwinn, C. R., Birkinshaw, M., Eubanks, T. M., & Matsakis, D. N. 1996, ApJ, 465, 566   
Reasenberg, R. D., et al. 1988, AJ, 96, 1731   
Reid, I. N. 1996, AJ, 111, 2000   
Sazhin, M. V., Zharov, V. E., & Kalinina, T. A. 2001, MNRAS, 323, 952   
Sazhin, M. V., Zharov, V. E., Volynkin, A. V., & Kalinina, T. A. 1998, MNRAS, 300, 287   
Schwarzschild, K. 1894, Astron. Nachr., 136, 81   
Shao, M. 1998, Proc. SPIE, 3350, 536   
Stumpff, P. 1985, A&A, 144, 232   
Walter, H. G., Mignard, F., Hering, R., Froeschle´, M., & Falin, J. L. 1986, Manuscripta Geod., 11, 103   
Weissman, P. R., McFadden, L.-A., & Johnson, T. V., eds. 1999, Encyclopedia of the Solar System (San Diego: Academic)   
Will, C. M. 1993, Theory and Experiment in Gravitational Physics (rev. ed.; Cambridge: Cambridge Univ. Press)   
Zhdanov, V. I. 1995, in IAU Symp. 166, Astronomical and Astrophysical Objectives of Sub-Milliarcsecond Optical Astrometry, ed. E. Høg & P. K. Seidelmann (Dordrecht: Kluwer), 295   
Zhdanov, V. I., & Zhdanova, V. V. 1995, A&A, 299, 321
