<!-- source: The IAU 2000 Resolutions for Astrometry_AJ 2003.pdf -->

<!-- pdf_type: normal; pages: 45; chunk_pages: 70 -->


<!-- chunk 0001: pages 1-45 -->
# The IAU 2000 resolutions for astrometry, celestial mechanics and metrology in the relativistic framework: explanatory supplement

M. Soffel $^ { - 1 }$ , S.A. Klioner $^ { 1 }$ , G. Petit $^ 2$ , P. Wolf $^ 2$ , S.M. Kopeikin $^ 3$ , P. Bretagnon $^ { \dag 4 }$ , V.A. Brumberg $^ { 5 }$ , N. Capitaine $6$ , T. Damour $^ 7$ , T. Fukushima $^ 8$ , B. Guinot $_ 6$ , T. Huang $^ { 9 }$ , L. Lindegren $^ { 1 0 }$ , C. Ma $_ { 1 1 }$ , K. Nordtvedt $^ { 1 2 }$ , J. Ries $^ { 1 3 }$ , P.K. Seidelmann $^ { 1 4 }$ , D. Vokrouhlick´y $^ { 1 5 }$ , C. Will $^ { 1 6 }$ , Ch. Xu $^ { 1 7 }$

# ABSTRACT

This paper discusses the IAU Resolutions B1.3, B1.4, B1.5 and B1.9 (2000) that were adopted during the 24th General Assembly in Manchester, 2000 and provides details and explanations for these Resolutions. It is explained why they present significant progress over the corresponding IAU 1991 Resolutions and why they are necessary in the light of present accuracies in astrometry, celestial mechanics and metrology. In fact most of these Resolutions are consistent with astronomical models and software already in use.

The metric tensors and gravitational potentials of both the Barycentric Celestial Reference System and Geocentric Celestial Reference System are defined and discussed. The necessity and relevance of the two celestial reference systems are explained. The transformations of coordinates and gravitational potentials are discussed. Potential coefficients parameterizing the post-Newtonian gravitational potentials are expounded. Simplified versions of the time transformations suitable for modern clock accuracies are elucidated. Various approximations used in the Resolutions are explicated and justified. Some models (e.g. for higher spin moments) that serve the purpose for estimating orders of magnitude have actually never been published before.

Subject headings: relativity, astrometry, celestial mechanics, reference systems, time

# 1. Introduction

It is clear that, beyond some threshold of accuracy, any astronomical problem has to be formulated within the framework of Einstein’s theory of gravity (General Relativity Theory, GRT). Many high precision astronomical techniques have already passed this threshold. For example, Lunar Laser Ranging (LLR) measures the distance to the Moon with a precision of a few cm, thereby operating at the $1 0 ^ { - 1 0 }$ level. At this level several relativity effects are significant and observable. Relativity effects related with the motion of the Earth-Moon system about the Sun are of the order $( v _ { \mathrm { o r b i t a l } } / c ) ^ { 2 } \simeq 1 0 ^ { - 8 }$ . The Lorentz contraction of the lunar orbit about the Earth that appears in barycentric coordinates has an amplitude of about $1 0 0 \mathrm { c m }$ whereas in some suitably chosen (local) coordinate system that moves with the Earth-Moon barycenter the dominant relativistic range oscillation reduces to a few cm only (Mashhoon 1985; Soffel et al. 1986).

The situation is even more critical in the field of astrometry. It is well known that the gravitational light deflection at the limb of the Sun amounts to $1 . 7 5 ^ { \prime \prime }$ and decreases only as $1 / r$ with increasing impact parameter $r$ of a light ray to the solar center. Thus, for light rays incident at about $9 0 ^ { \circ }$ from the Sun the angle of light deflection still amounts to 4 mas. To describe the accuracy of astrometric measurements it is useful to make use of the parameter $\gamma$ of the parameterized post-Newtonian (PPN) formalism. We would like to emphasize that this paper deals solely with Einstein’s theory of gravity, where $\gamma = 1$ , and not with the PPN formalism. Nevertheless, the introduction of $\gamma$ is useful if one talks about measuring accuracies. In the PPN formalism, the angle of light deflection is proportional to $( \gamma + 1 ) / 2$ so that astrometric measurements might be used for a precise determination of the parameter $\gamma$ . Meanwhile, VLBI has achieved accuracies of better than 0.1 mas, and regular geodetic VLBI measurements have frequently been used to determine the space curvature parameter. A detailed analysis of VLBI data from the projects MERIT and POLARIS/IRIS gave $\gamma = 1 . 0 0 0 \pm 0 . 0 0 3$ , (Robertson et al. 1984; Carter et al. 1985) where a formal standard error is given. Recently an advanced processing of VLBI data provided the best current estimates $\gamma = 0 . 9 9 9 6 \pm 0 . 0 0 1 7$ (Lebach et al. 1995) and $\gamma = 0 . 9 9 9 9 4 \pm 0 . 0 0 0 3 1$ (Eubanks et al. 1997). Current accuracy of modern optical astrometry as represented by the HIPPARCOS catalog is about 1 milliarcsecond, which gave a determination of $\gamma$ at the level of $0 . 9 9 7 \pm 0 . 0 0 3$ (Froeschl´e, Mignard & Arenou 1997). Future astrometric missions such as SIM and especially GAIA will push the accuracy to the level of a few microarcseconds (µas), and the expected accuracy of determinations of $\gamma$ will be $1 0 ^ { - 6 } - 1 0 ^ { - 7 }$ . The accuracy of 1 $\mu$ as should be compared with the maximal possible light deflection due to various parts of the gravitation field: the post-Newtonian effect of $1 . 7 5 ^ { \prime \prime }$ due to the mass of the Sun, $2 4 0 \mu \mathrm { a s }$ caused by the oblateness of Jupiter, $J _ { 2 }$ (10 µas due to Jupiter’s $J _ { 4 }$ ), the post-post-Newtonian effect of $1 1 \mu \mathrm { a s }$ due to the Sun, etc. This illustrates how complicated the relativistic modeling of future astrometric observations will be. It is clear that for such high accuracy the corresponding model must be formulated in a self-consistent relativistic framework.

Another problem worth mentioning is that of time measurement. The realization of the SI second (the unit of proper time) has improved by one order of magnitude in the last few years with the advent of laser cooled atomic clocks (Lemonde et al. 2001; Weyers et al. 2001, and references therein), and is now below two parts in $1 0 ^ { 1 5 }$ . This should be compared with the dimensionless quantity $U _ { E } / c ^ { 2 } \simeq 7 \times 1 0 ^ { - 1 0 }$ , which gives the order of magnitude of relativistic effects produced by the gravity field of the Earth itself in the vicinity of its surface. In the near future, laser cooled atomic clocks in micro-gravity are expected to lead to a further improvement by at least one order of magnitude. At present several clock experiments in terrestrial orbit are planned, such as the Atomic Clock Ensemble in Space project (ACES, Lemonde et al. 2001). These in turn are likely to lead to clock experiments in solar orbits like the Solar Orbit Relativity Test (SORT) project. All of these experiments require a detailed account of many subtle relativistic effects.

Finally we would like to mention the problem of geodesic precession-nutation (a relativistic effect that is discussed in more detail below, Misner, Thorne & Wheeler 1973; Soffel 1989) and the description of Earth’s rotation in a suitably chosen Geocentric Celestial Reference System (GCRS). Geodesic precession amounts to 1.9”/century and geodesic nutation is dominated by an annual term with amplitude 0.15 mas. Since the GCRS is chosen to be kinematically non-rotating geodesic precession-nutation should be contained in the model describing the relation between the GCRS and the International Terrestrial Reference System (ITRS). According to the IAU 2000 Resolution B1.6 this relativistic precession-nutation is indeed contained in the present IAU precession-nutation model.

These examples show clearly that high-precision modern astronomical observations can no longer be described by Newtonian theory, but require Einstein’s theory of gravity.

The consequences of this are profound for the basic formalism to be used since one often tends to express it in terms of “small relativistic corrections” to Newtonian theory. This can lead to misconceptions and mistakes. One central point is that in Newton’s theory, globally preferred coordinate systems exist that have a direct physical meaning. In the Newtonian framework, idealized clocks show absolute time everywhere in the universe at all times, and global spatial inertial coordinates exist in which dynamical equations of motion show no inertial forces. This is no longer true in GRT. Usually space-time coordinates have no direct physical meaning and it is essential to construct the observables as coordinate independent quantities, i.e., scalars, in mathematical language. This construction usually occurs in two steps: first one formulates a coordinate picture of the measurement procedure and then one derives the observable out of it. This leads us to the problem of defining useful and adequate coordinate systems in astronomy. The underlying concept in relativistic modeling of astronomical observations is a relativistic four-dimensional reference system (RS). By reference system we mean a purely mathematical construction (a chart or a coordinate system) giving “names” to space-time events. In contrast to this a reference frame is some materialization of a reference system. In astronomy the materialization is usually realized by means of a catalog or ephemeris, containing positions of some celestial objects relative to the reference system under consideration. Hence it is very important to understand that any reference frame is defined only through a well-defined reference system, which has been used to construct physical models of observations.

In the following, a 4-dimensional space-time reference system will be described by four coordinates $x ^ { \alpha } = ( x ^ { 0 } , x ^ { i } ) = ( x ^ { 0 } , x ^ { 1 } , x ^ { 2 } , x ^ { 3 } )$ . Here and below the greek indices (e.g., $\alpha$ ) take the values $0 , 1 , 2 , 3$ and the latin ones (e.g., $i$ ) take the values $1 , 2 , 3$ . The index 0 refers to the time variable and the indices $1 , 2 , 3$ refer to the three spatial coordinates. For dimensional reasons one usually writes $x ^ { 0 } = c t$ where $c$ is the speed of light and $t$ a time variable. According to the mathematical formalism of General Relativity, a particular reference system is fixed by the specific form of the metric tensor $g _ { \alpha \beta } ( t , x ^ { i } )$ , which allows one to compute the 4-distance $d s$ between any two events $x ^ { \alpha }$ and $x ^ { \alpha } + d x ^ { \alpha }$ according to the rule

$$
d s ^ { 2 } = g _ { \alpha \beta } ( t , x ^ { i } ) d x ^ { \alpha } d x ^ { \beta } \equiv g _ { 0 0 } c ^ { 2 } d t ^ { 2 } + 2 g _ { 0 i } c d t d x ^ { i } + g _ { i j } d x ^ { i } d x ^ { j } ,
$$

where Einstein’s summation convention (summation over two equal indices) is implied. The metric tensor allows one to derive translational and rotational equations of motion of bodies, to describe the propagation of light, and to model the process of observation. Examples of such modeling include relating the observed (proper) time of an observer to the coordinate time $t$ , or relating the angles between two incident light rays as observed by that observer to the corresponding coordinate directions. All of these components can be combined into a single relativistic model for a particular kind of observations. Such a model contains a certain set of parameters describing various properties of the objects participating in the process of observations. These parameters should be determined from observations. Many of these parameters crucially depend on the reference system used to formulate the model of observations (e.g., the initial positions and velocities of certain bodies). Some other parameters might not depend at all on the reference system (e.g., the speed of light in vacuum). On the other hand, according to the principle of covariance different reference systems covering the region of space-time under consideration are mathematically equivalent in the sense that any such system can be used to model the observations. This freedom to choose the reference system can be used to simplify the models or to make the resulting parameters more physically adequate.

It is widely accepted that in order to describe adequately modern astronomical observations one has to use several relativistic reference systems. The solar system Barycentric Celestial Reference System (BCRS) can be used to model light propagation from distant celestial objects as well as the motion of bodies within the solar system. The Geocentric Celestial Reference System is physically adequate to describe processes occurring in the vicinity of the Earth (Earth’s rotation, motion of Earth’s satellites etc.). The introduction of further local systems (selenocentric, martian etc.) might be of relevance for specific applications, where physical phenomena in the vecinity of the corresponding body play a role.

The necessity to use several reference systems can be understood from the following example. If we were to characterize terrestrial observers by the difference between their BCRS coordinates and the BCRS coordinates of the geocenter, the positions of the observers relative to the geocenter would be altered by time-dependent, relativistic coordinate effects (such as Lorentz contraction) which have nothing to do with the Earth’s rotation or with geophysical factors and which would vanish if one employs suitable GCRS coordinates instead. On the other hand, the coordinate positions derived with VLBI observations are used to investigate local geophysical processes and some adequate geocentric reference system allows one to simplify their description.

The basic idea is to construct a special local reference system for each material subsystem, where relativistic equations of motion of a test body inside the considered subsystem take a particularly simple form. In such a local reference system the influence of external matter, in accordance with the equivalence principle, should be given by tidal potentials only, that is, by potentials whose expansions in powers of local spatial coordinates in the vicinity of the origin of the corresponding reference system starts with the second order (the linear terms representing inertial forces may also exist, but can be eliminated if desired by a suitable choice of the origin of the local coordinates).

Two advanced relativistic formalisms have been worked out to tackle this problem in the first post-Newtonian approximation of General Relativity. One formalism is due to Brumberg and Kopeikin (Brumberg & Kopeikin 1989; Kopeikin 1988, 1990; Brumberg 1991; Klioner & Voinov 1993) and another one is due to Damour, Soffel and Xu (Damour, Soffel & Xu 1991, 1992, 1993, 1994), frequently called the DSX framework. The IAU 2000 Resolutions B1.3-B1.5 are based on these approaches. These Resolutions extend corresponding older ones that are reconsidered in the next section. From a mathematical point of view Resolution B1.3 recommends the use of certain coordinates and the way of writing the metric tensor. Clearly one might use any coordinate system that might be well adapted to the specific problem of interest. Nevertheless because of the high risk of possible confusion the strategy of recommending special coordinate systems (to fix the gauge completely in the mathematical language) has significant advantages. If different coordinates are employed to derive certain results this should be stressed explicitly so that they can be transformed into the reference systems recommended by the IAU and can be compared with the results derived in the IAU framework.

The organisation of the present paper is as follows (see also Figure 1). In Section 2 the principal content of the IAU 1991 recommendations on relativity (Section 2.1) and the further related IAU and IUGG resolutions (Section 2.2) are repeated. The IAU 2000 resolutions on relativity (Resolutions B1.3, B1.4, B1.5 and B1.9) are discussed in Section 3. The full text of the IAU 2000 resolutions on relativity is given in Appendix A. Section 3.1 briefly clarifies the necessity and the role of the two celestial reference systems defined by the IAU resolutions. The Barycentric Celestial Reference System (BCRS) defined by Resolution B1.3 is discussed in Section 3.2. Section 3.3 is devoted to a discussion of the Geocentric Celestial Reference System (GCRS) as well as the definition of the geocentric gravitational potentials also defined by Resolution B1.3. The coordinate transformations between the BCRS and GCRS, also fixed by Resolution B1.3, are explained in Section 3.4. Potential coefficients which can be used to represent in a meaningful way the post-Newtonian geocentric gravitational potential of the Earth in its immediate vicinity are fixed by Resolution B1.4 and explained in Section 3.5. As an illustration the gravitational potentials of the BCRS are calculated in Section 3.6 for the simplified case when all gravitating bodies of the solar system can be characterized by their masses only (no further structure of the gravitational field of the bodies is considered). A similar form of the barycentric gravitational potentials is used in Resolution B1.5 where a practical relativistic framework for time and frequency applications in the solar system is formulated. This practical relativistic framework is discussed in Section 4. The practical transformation between the coordinate times of the BCRS and GCRS is explained in Section 4.1 while the transformations between various kinds of the time scales appropriate for the Earth’s vicinity are discussed in Section 4.2. Appendix B contains an explicit proof that the BCRS metric coincides with well-known results from the literature.

# 2. The IAU 1991 framework and previous recommendations

# 2.1. The IAU 1991 recommendations

The IAU Resolution A4 (1991) contains nine recommendations, the first five of which are directly relevant to our discussion.

In the first recommendation, the metric tensor for space-time coordinate systems $( t , \mathbf { x } )$ centered at the barycenter of an ensemble of masses is recommended in the form

$$
g _ { 0 0 } = - 1 + \frac { 2 U ( t , { \bf x } ) } { c ^ { 2 } } + \mathcal { O } ( c ^ { - 4 } ) ,
$$

![](images/8e7ead0fbb2e0cecb5257eb86d6f19f93163cc4c60df6ded53b2416819024e96.jpg)  
Fig. 1.— Notations used for quantities of the Barycentric and Geocentric Celestial Reference Systems (coordinates, metric, potentials, and multipole moments) with references to the Sections and Resolutions where they appear.

$$
\begin{array} { l } { { g _ { 0 i } = \mathcal { O } ( c ^ { - 3 } ) , } } \\ { { \displaystyle } } \\ { { g _ { i j } = \delta _ { i j } \left( 1 + \frac { 2 U ( t , { \bf x } ) } { c ^ { 2 } } \right) + \mathcal { O } ( c ^ { - 4 } ) , } } \end{array}
$$

where $c$ is the speed of light in vacuum ( $c = 2 9 9 7 9 2 4 5 8 \mathrm { m } / \mathrm { s }$ ) and $U$ is the Newtonian gravitational potential (here a sum of the gravitational potentials of the ensemble of masses, and of an external potential generated by bodies external to the ensemble, the latter potential vanishing at the origin). The algebraic sign of $U$ is taken to be positive and it satisfies the Poisson equation

$$
\Delta U = - 4 \pi G \rho .
$$

Here, $G$ is the gravitational constant, $\rho$ is the matter density and $\Delta$ is the usual Laplacian $\Delta \equiv$ $\partial ^ { 2 } / \partial x ^ { 2 } + \partial ^ { 2 } / \partial y ^ { 2 } + \partial ^ { 2 } / \partial z ^ { 2 }$ , $\mathbf { x } = ( x , y , z )$ . This recommendation recognizes also that space-time cannot be described by a single coordinate system. The recommended form of the metric tensor can be used not only to describe the barycentric reference system of the whole solar system, but also to define the geocentric reference system centered in the center of mass of the Earth with a suitable function instead of $U$ , now depending upon geocentric coordinates. In analogy to the geocentric reference system a corresponding reference system can be constructed for any other body of the solar system.

In the second recommendation, the origin and orientation of the spatial coordinate grids for the barycentric and geocentric reference systems are defined. Notably it is specified that the spatial coordinates of these systems should show no global rotation with respect to a set of distant extragalactic objects. It also specifies that the SI (International System of Units) second and the SI meter should be the units of time and length in all coordinate systems. It states in addition that the time coordinates should be derived from an Earth atomic time scale.

The third recommendation defines $T C B$ (Barycentric Coordinate Time) and $T C G$ (Geocentric Coordinate Time) as the time coordinates of the BCRS and GCRS, respectively. Here we write $( t \ : = \ : T C B , x ^ { i } )$ and ( $T = T C G , X ^ { \iota } )$ for the respective coordinates. The recommendation also defines the origin of the times scales in terms of International Atomic Time $( T A I )$ . The reading of the coordinate time scales on 1977 January 1, $0 ^ { \mathrm { h } } 0 ^ { \mathrm { m } } 0 ^ { \mathrm { s } } \ T A I$ $J D = 2 4 4 3 1 4 4 . 5 T A I$ ) must be 1977 January 1, $0 ^ { \mathrm { h } } 0 ^ { \mathrm { m } } 3 2 . 1 8 4 ^ { \mathrm { s } }$ ). Finally, the recommendation declares that the units of measurements of the coordinate times of all reference systems are chosen so that they are consistent with the SI second. The relationship between $T C B$ and $T C G$ is then given by the time part of the full 4-dimensional transformation between the barycentric and geocentric reference systems

$$
T C B - T C G = c ^ { - 2 } \left[ \int _ { t _ { 0 } } ^ { t } \left( \frac { v _ { E } ^ { 2 } } { 2 } + U _ { \mathrm { e x t } } ( \mathbf { x } _ { E } ) \right) d t + v _ { E } ^ { i } r _ { E } ^ { i } \right] + \mathcal { O } ( c ^ { - 4 } ) ,
$$

where $x _ { E } ^ { i }$ and $v _ { E } ^ { i }$ are the barycentric coordinate position and velocity of the geocenter, $r _ { E } ^ { i } = x ^ { i } - x _ { E } ^ { i }$

with $x ^ { i }$ the barycentric position of some observer, and $U _ { \mathrm { e x t } } ( \mathbf { x } _ { E } )$ is the Newtonian potential of all solar system bodies apart from the Earth evaluated at the geocenter.

In the fourth recommendation another coordinate time, Terrestrial Time ( $T T$ ), is defined. It differs from $T C G$ by a constant rate only

$$
T C G - T T = L _ { G } \times ( J D - 2 4 4 3 1 4 4 . 5 ) \times 8 6 4 0 0 , L _ { G } \approx 6 . 9 6 9 2 9 1 \times 1 0 ^ { - 1 0 } ,
$$

where $J D$ is $T A I$ measured in Julian days, so that the mean rate of $' L " L "$ agrees with that of the proper time of an observer situated on the geoid up to a certain accuracy limit. Up to a constant shift of 32.184 s, $x \ i { 1 } \ i$ represents an ideal form of $T A I$ , the divergence between them being a consequence of the physical defects of atomic clocks. It is also recognized that $T T$ is nothing but a rescaling of the geocentric coordinate time $T C G$ .

The fifth recommendation states that the old barycentric time $T D B$ may still be used where discontinuity with previous work is deemed to be undesirable. Let us note, however, that $T D B$ was never defined in a self-consistent and exact manner. For that reason it cannot be used in theoretical considerations. In the notes to the third recommendation the relation of the $T C B$ with $T D B$ is given as

$$
T C B - T D B = L _ { B } \times ( J D - 2 4 4 3 1 4 4 . 5 ) \times 8 6 4 0 0 , \qquad L _ { B } \approx 1 . 5 5 0 5 0 5 \times 1 0 ^ { - 8 } .
$$

Note, however, according to the IAU Resolution C7 (see Section 2.2) $J D$ is defined in Terrestrial Time $( T T )$ which makes this formula problematic.

# 2.2. Further resolutions

Resolution 2 (1991) of the International Union of Geodesy and Geophysics (IUGG) defined a Conventional Terrestrial Reference System (CTRS) as a reference system resulting from a [timedependent] spatial rotation of the geocentric reference system defined by the IAU 1991 Recommendations, the spatial rotation being chosen such that the CTRS has no global residual rotation with respect to horizontal motions at the Earth’s surface. The coordinate time of the CTRS coincides with $T C G$ .

IAU Resolution C7 (1994) recommends that the epoch J2000 as well as the Julian (ephemeris) day are defined in $T T$ .

IAU Resolution B6 (1997) has supplemented the framework by one more recommendation stating that no scaling of spatial axes should be applied in any reference system (even if a scaled time coordinate like $T T$ is used). Note, however, that this Resolution has been ignored in the construction of the International Terrestrial Reference Frame (ITRF) which is defined not with the

GCRS spatial coordinates $\mathbf { X }$ but with scaled coordinates $\mathbf { X } _ { T T } = \left( 1 - L _ { G } \right) \mathbf { X }$ .

# 3. The IAU 2000 Resolutions on relativity

The IAU 1991 framework is unsatisfactory from many points of view. The Einstein-Infeld-Hoffmann equations of motion which have been used since the 70s to construct the JPL numerical ephemerides of planetary motion cannot be derived from the metric (2). In other words for the motion of massive solar system bodies metric (2) is not the post-Newtonian metric of Einstein’s theory of gravity. In the years prior to the XXIII General Assembly in Kyoto (1997) it became obvious that the IAU 1991 set of recommendations concerning relativity in astrometry, celestial mechanics and metrology is not sufficient for achievable accuracies. Especially with respect to planned astrometric missions with microarcsecond accuracies extended and improved resolutions became indispensable. For that reason the IAU Working Group “Relativity for astrometry and celestial mechanics” together with the BIPM/IAU Joint Committee on relativity for space-time reference systems and metrology suggested such an extended set of Resolutions (B1.3 - B1.5 and B1.9) that was finally adopted at the IAU General Assembly in Manchester in the year 2000. The relevant Resolutions can be found in Appendix A. It is clear that because of their brevity they need additional explanations and one has to show how they work in practice. This paper now presents a detailed explanatory supplement for these IAU 2000 Resolutions.

# 3.1. The role of the two Celestial Reference Systems, BCRS and GCRS

Some of the reasons why two different celestial astronomical reference systems have to be introduced have already been mentioned in the introduction. Here we would like to deepen this discussion in several respects. It is clear that for many applications in the fields of astrometry, celestial mechanics, geodynamics, geodesy etc. some quasi-inertial or ’space-fixed’ reference system has to be introduced. Resolution B1.3 defines actually two different Celestial Reference Systems: the Barycentric Celestial Reference System (BCRS) and the Geocentric Celestial Reference System (GCRS).

In Newtonian theory one can easily introduce inertial space-time coordinates that cover the entire universe. Such inertial coordinates in Newton’s theory are unique up to the choice of origin, scales, the orientation of spatial axes and up to a constant velocity of origin. In astronomy conceptually we may talk about two different relevant celestial systems: a barycentric and a geocentric one that basically serve different purposes. The barycentric celestial system is considered to be inertial (external galactic and extragalactic matter being normally neglected) and is used for solar system ephemerides, for concepts such as an ecliptic, for interplanetary spacecraft navigation etc. The positions of remote objects can be defined in that system. The barycentric celestial system presents the fundamental astrometric system where concepts as ’proper motion’ or ’radial velocity’

can be defined.

On the other side the geocentric celestial system might be called quasi-inertial since the spatial axes are non-rotating in the Newtonian absolute sense whereas the geocenter is accelerated. It is employed for the description of physical processes in the vicinity of the Earth, for satellite theory, the dynamics of the Earth including Earth’s rotation, etc. It is also used for the introduction of concepts like equator and the ITRS. Let us denote the time and space coordinates of the barycentric celestial system by $( t , \mathbf { x } )$ , those of the geocentric celestial system by $( T , \mathbf { X } )$ . In Newton’s framework the relation between these two sets of coordinates is trivial

$$
T = t , \qquad { \bf X } = { \bf x } - { \bf x } _ { E } ( t ) ,
$$

where ${ \bf x } _ { E } ( t )$ denotes the barycentric position of the geocenter. Because these relations are so trivial for some purposes the barycentric and the geocentric celestial systems are not always clearly distinguished in the Newtonian framework.

Of course for astrometric problems one always distinguished between the two celestial systems and apparent places of stars from true (barycentric) places. However, annual parallax and aberration were merely understood as correction terms that have to be applied to get the ’true’ positions for the realization of the astronomical quasi-inertial, space-fixed celestial system. Note that the definition of the classical astronomical $( \alpha , \delta )$ system uses concepts from both systems: some ecliptic from the barycentric celestial system and some Earth’s rotation pole, Celestial Ephemeris Pole (CEP) or Celestial Intermediate Pole (CIP), and its corresponding equator from the geocentric celestial system.

In Relativity theory the situation is actually more complicated. Even in the absence of gravitational fields and a uniformly moving geocenter the two coordinate systems are related by a 4-dimensional Lorentz transformation of Special Relativity. In our solar system BCRS and GCRS coordinates are related by a complicated 4-dimensional space-time transformation (a generalized Lorentz transformation) that also contains acceleration terms and gravitational potentials. This implies that the two astronomical Reference Systems, the BCRS and the GCRS are actually quite different. This has profound consequences for a lot of classical astronomical concepts.

The BCRS is the basic astrometric celestial reference system. Usually one considers the solar system to be isolated, i.e., one ignores all matter and fields outside the system and assumes the gravitational potentials to vanish far from the system. It is obvious that ignoring the Galaxy and extragalactic objects is an unphysical idealization for several specific questions that, however, will not be touched here. If the solar system is considered to be isolated we might follow light-rays from some very remote source back in time to the region $| \mathbf { x } | \to \infty$ that might be called the celestial sphere. In the vicinity of the celestial sphere a certain light ray defines spherical angles that might appear as catalog values. Actually for reference stars the physical distance from the Earth usually plays a role. In that case we might associate any star with a corresponding BCRS coordinate position $^ { \mathbf { x } _ { * } }$ that will be a function of $T C B$ . From this position vector spherical angles $( \alpha _ { * } , \delta _ { * } )$ can be introduced in a very simple manner by

$$
\frac { { \bf x } _ { * } } { | { \bf x } _ { * } | } = \left( \begin{array} { c } { { \cos \alpha _ { * } \cos \delta _ { * } } } \\ { { \sin \alpha _ { * } \cos \delta _ { * } } } \\ { { \sin \delta _ { * } } } \end{array} \right)
$$

that can be considered as catalog values. If the coordinate distance of some source tends to infinity the two constructions for an astrometric position will coincide. From ${ \bf x } _ { * } ( t )$ quantities such as ’proper motion’ or ’radial velocity’ can be defined as coordinate quantities in the BCRS. Note that the problem of ’radial velocity’ has exhaustively been discussed by Lindegren & Dravins (2003) (see also IAU 2000 Resolutions C1 and C2 (Rickman 2001)). Other fields of application of the BCRS are solar system ephemerides, interplanetary navigation, etc.

The definitions of the BCRS given by the IAU 2000 Resolution B1.3 do not fix the orientation of spatial axes uniquely but only up to some constant, time independent rotation matrix about the origin. One natural choice of orientation is provided by the International Celestial Reference System (ICRS). Actually for the construction of the International Celestial Reference Frame (ICRF) and its optical counterpart, the Hipparcos catalog, the recommended form of the barycentric metric tensor has already been used explicitly in the underlying models. This implies that a set of definitions that fix the ICRS completely contains the BCRS definitions.

There might be other useful possibilities for the orientation of barycentric spatial coordinates. One possibility is the orientation according to some ecliptic $\mathcal { E } _ { 0 }$ at a certain epoch $t _ { 0 }$ defined by corresponding solar system ephemerides. Such an ecliptic would coincide with the $x$ - $y$ plane of a $\mathrm { B C R S } [ \mathcal { E } _ { 0 } ]$ that might be useful for reasons of historical continuity.

On the other hand quantities and concepts related with the physics in the immediate vicinity of the Earth should be formulated in the GCRS. This concerns the gravity field of the Earth itself, satellite theory and especially applies to theories of Earth’s rotation and their parameters. Clearly the spatial GCRS coordinates $\mathbf { X }$ can be used to define corresponding unit vectors at the geocenter that might be employed to compute spherical angles $( \alpha _ { \mathrm { G C R S } } , \delta _ { \mathrm { G C R S } } )$ which might be called ’geocentric places’. Note, however, that the coordinates of the remote astronomical sources are defined in the BCRS only. The calculated GCRS places $( \alpha _ { \mathrm { G C R S } } , \delta _ { \mathrm { G C R S } } )$ are determined by incident light rays at the geocenter. They differ from corresponding ICRS $( \alpha , \delta )$ values because of annual aberration, annual parallax and gravitational light deflection due to the gravitational fields of the solar system bodies (apart from the Earth) and are independent of Earth’s rotation. If these GCRS places, however, will ever play a role in practice is not clear.

In the past apparent places of stars that were annually published e.g., in the ’Apparent Places of Fundamental Stars’ played a role for certain problems. These places are related with the old traditional astronomical reference system, i.e., with some equator and equinox of date. Now with the ICRS we have a highly precise astronomical reference system that is basically independent of Earth’s rotation parameters and their determination. For several applications, however, the introduction of quantities like apparent places might still be useful especially if there is a reference to the local plumb line, i.e., to the zenith and the astronomical (or nautical) triangle can be employed. In that case Resolutions B1.7 and B1.8 (IAU 2001; Rickman 2001) come into play. These two Resolutions define some intermediate system that can be used for the definition of an intermediate position $( \alpha _ { \mathrm { i n t e r } } , \delta _ { \mathrm { i n t e r } } )$ by the Celestial Intermediate Pole (CIP) and the Celestial Ephemeris Origin (CEO). Such intermediate position can be considered as modern version of the apparent place, defined in the GCRS.

For astrometry at microarcsecond accuracies neither GCRS places nor intermediate places likely will play a role. To avoid problems related with non-linearities it is simpler to use an overall BCRS picture to describe not only the light-rays and the motion of gravitating bodies but also the trajectory of an observer. In that case only catalog and observed positions will be of importance.

# 3.2. The Barycentric Celestial Reference System

Resolution B1.3 concerns the definition of Barycentric Celestial Reference System (BCRS) and Geocentric Celestial Reference System (GCRS). The BCRS is defined with coordinates $( c t , x ^ { i } ) = x ^ { \mu }$ where $t = T C B$ . The BCRS is a particular version of the barycentric reference system of the solar system. The Resolution recommends to write the metric tensor of the BCRS in the form

$$
\begin{array} { l } { { \displaystyle g _ { 0 0 } = - 1 + \frac { 2 w } { c ^ { 2 } } - \frac { 2 w ^ { 2 } } { c ^ { 4 } } + \mathcal { O } ( c ^ { - 5 } ) } , }  \\ { { \displaystyle g _ { 0 i } = - \frac { 4 } { c ^ { 3 } } w ^ { i } + \mathcal { O } ( c ^ { - 5 } ) , } } \\ { { \displaystyle g _ { i j } = \delta _ { i j } \left( 1 + \frac { 2 } { c ^ { 2 } } w \right) + \mathcal { O } ( c ^ { - 4 } ) . } } \end{array}
$$

A comparison reveals that this form of the metric presents an extension of (2). Whereas the old form contains only, the Newtonian potential $U$ the new one contains a scalar potential $w$ and a vector potential $w ^ { i }$ .

Actually the equations for $g _ { 0 0 }$ and $g _ { 0 i }$ from (8) without the order symbols $\mathcal { O } ( c ^ { - 5 } )$ are always correct and can be simply considered as definitions of $w$ and $w ^ { i }$ in terms of $g _ { 0 0 }$ and $g _ { 0 i }$ . In contrast to the concrete form of the resolution we have added order symbols in (8). E.g., for $g _ { 0 0 }$ the order symbol indicates that terms of order $c ^ { - 5 }$ will systematically be neglected as stated in the notes to the Resolution. With these forms for $g _ { 0 0 }$ and $g _ { 0 i }$ one finds that spatially isotropic coordinates $x ^ { i }$ exist such that $g _ { i j }$ from equation (8) with the potential $w$ from $g _ { 0 0 }$ solves Einstein’s field equations to first post-Newtonian order. Note that the form of (8) implies the barycentric spatial coordinates $x ^ { i }$ satisfy the harmonic gauge condition (see e.g. Brumberg & Kopeikin 1989; Damour, Soffel $\&$ Xu 1991). At this point, because of the freedom in the time coordinate, many different ’time gauge conditions’ are still possible. The Resolution proceeds by recommending a specific kind of space and time harmonic gauge. One argument in favor of the harmonic gauge is that tremendous work on General Relativity has been done with the harmonic gauge that was found to be a useful and simplifying gauge for many kinds of applications. Moreover, the harmonic gauge condition (e.g., Weinberg 1972; Fock 1959)

$$
g ^ { \mu \nu } \Gamma _ { \mu \nu } ^ { \lambda } = 0 ,
$$

where $\Gamma _ { \mu \nu } ^ { \lambda }$ are the Christoffel-symbols of the metric tensor, is not restricted to some post-Newtonian approximation, but can be defined in Einstein’s theory of gravity without any approximations. This may be important for future refinements of the IAU framework. With the harmonic gauge condition the post-Newtonian Einstein field equations take the form

$$
\begin{array} { r } { \left( - \frac { 1 } { c ^ { 2 } } \frac { \partial ^ { 2 } } { \partial t ^ { 2 } } + \Delta \right) w = - 4 \pi G \sigma + \mathcal { O } ( c ^ { - 4 } ) , } \\ { \Delta w ^ { i } = - 4 \pi G \sigma ^ { i } + \mathcal { O } ( c ^ { - 2 } ) . } \end{array}
$$

Here $\sigma$ and $\sigma ^ { i }$ are the gravitational mass and mass current density, respectively. Mathematically they are related to the energy-momentum tensor $T ^ { \mu \nu }$ by

$$
\sigma = \frac { 1 } { c ^ { 2 } } \left( T ^ { 0 0 } + T ^ { s s } \right) , \quad \sigma ^ { i } = \frac { 1 } { c } T ^ { 0 i } .
$$

The energy-momentum tensor $T ^ { \mu \nu }$ generalizes the density $\rho$ of the Poisson equation (3). In relativity, energy density, pressure and stresses all act as source of the gravitational field. This implies that different kinds of energy contribute to the gravitational sources: kinetic energy, gravitational potential energy, energy of deformation etc., but since the kinetic energy depends upon the state of motion of the matter, the energy-momentum tensor that really acts as gravitational source shows a nontrivial transformation behaviour if we go from one reference system to another. In practice, however, the energy-momentum tensor will usually not appear explicitly. This is because the gravitational potentials $w$ and $w ^ { i }$ from (10)–(11) are completely determined by $\sigma$ and $\sigma ^ { i }$ which can be considered as primary quantities. If we deal with problems where gravitational fields play a role only outside of astronomical bodies and admit a useful convergent expansion in terms of multipole moments (potential coefficients) only corresponding integral characteristics of the bodies like masses, quadrupole moments etc. show up explicitly, which are defined in terms of $\sigma$ and $\sigma ^ { \ i }$ and whose numerical values will be fixed by observations. Because of (11) $w ^ { \ i }$ is sometimes called the gravitomagnetic potential since it results from mass currents (moving or rotating masses) just as the electromagnetic vector potential results from electric currents in Maxwell’s theory of electromagnetism.

Equation (10) generalizes the Poisson equation (3), hence the scalar potential $w$ presents a relativistic generalization of the Newtonian potential $U$ . Because of problems related with homogeneous solutions and boundary conditions mathematically it is clear that these differential equations do not fix the harmonic solutions uniquely. Assuming space-time to be asymptotically flat (no gravitational fields far from the system), i.e.,

$$
\operatorname* { l i m } _ { r \to \infty \atop t = \mathrm { c o n s t } } g _ { \mu \nu } = \mathrm { d i a g } ( - 1 , + 1 , + 1 , + 1 )
$$

the recommended solution reads

$$
\begin{array} { l } { { \displaystyle w ( t , { \bf x } ) = G \int d ^ { 3 } x ^ { \prime } { \frac { \sigma ( t , { \bf x } ^ { \prime } ) } { | { \bf x } - { \bf x } ^ { \prime } | } } + { \frac { 1 } { 2 c ^ { 2 } } } G { \frac { \partial ^ { 2 } } { \partial t ^ { 2 } } } \int d ^ { 3 } x ^ { \prime } \sigma ( t , { \bf x } ^ { \prime } ) | { \bf x } - { \bf x } ^ { \prime } | , } } \\ { { \displaystyle w ^ { i } ( t , { \bf x } ) = G \int d ^ { 3 } x ^ { \prime } { \frac { \sigma ^ { i } ( t , { \bf x } ^ { \prime } ) } { | { \bf x } - { \bf x } ^ { \prime } | } } . } } \end{array}
$$

It is obvious that the second time derivative term in (14) results from the corresponding operator in the field equation (10). This operator modifies the Laplacian from the Newtonian Poisson equation to the d’Alembertian and the similarity between the harmonic post-Newtonian field equations and Maxwell’s equations of electromagnetism in the Lorentz gauge becomes obvious (actually one might replace the Laplacian by the d’Alembertian in (11) to post-Newtonian accuracy). From Maxwell’s theory it is well known that the retarded potential solves the corresponding field equation

with

$$
\begin{array} { c } { { \displaystyle w _ { \mathrm { r e t } } ( t , x ^ { i } ) = G \int d ^ { 3 } x ^ { \prime } \frac { \sigma \big ( t _ { \mathrm { r e t } } , \mathbf { x } ^ { \prime } \big ) } { \vert \mathbf { x } - \mathbf { x } ^ { \prime } \vert } } } \\ { { \displaystyle t _ { \mathrm { r e t } } = t - \frac { \vert \mathbf { x } - \mathbf { x } ^ { \prime } \vert } { c } . } } \end{array}
$$

One might then expand the retarded potential in terms of $1 / c$ . Note, that such an expansion also yields a term proportional to $1 / c$ . If we stay within the first post-Newtonian approximation these $1 / c$ terms vanish due to the Newtonian mass conservation law. Such odd powers of $1 / c$ indicate time asymmetric terms, i.e., they break time reversal symmetry. It is well known that such time asymmetric terms appear only to higher post-Newtonian order and will not be considered here. For that reason the retarded potential (16) leads to the recommended solution above.

Comparing the form of the metric tensor in (8) with other forms that can be found in the literature (e.g., Will 1993) one might get the erroneous impression that something is missing in (8), which is not the case. If matter is discribed by some fluid model then formally $( w , w ^ { i } )$ might be split into various pieces resulting from kinetic energy, gravitational potential energy, specific internal energy density, pressure etc. and the equivalence of our form of the metric tensor e.g. with that given in Will (1993) can be shown. This is explicitly demonstrated in Appendix B.

The point, however, is that a split of $( \sigma , \sigma ^ { i } )$ of our metric potentials $( w , w ^ { \imath } )$ or of the metric tensor itself into various pieces is usually unnecessary. If only gravitational fields outside the relevant bodies play a role (as is typically the case in celestial mechanics and astrometry) it is advantageous to keep such pieces together, since it will be the sum that determines the observables. One might argue, $U$ is the ’Newtonian potential’ and the rest can be identified as ’relativistic corrections’. This way of thinking, however, can be very misleading and presents a source of errors. As has been shown in the literature (e.g., Damour, Soffel & Xu 1991, 1993) suitably defined potential coefficients based upon $w$ (not $U$ ) and $w ^ { i }$ can be introduced that can be determined from satellite data. From a more theoretical point of view the introduction of $( w , w ^ { i } )$ has the advantage that the field equations (10)–(11) are formally linear, although the corresponding metric is not (because of the $w ^ { 2 }$ -term). We used the word ’formally’ since $\sigma$ depends upon $w$ implicitly. This nonlinearity has been explicitly treated, e.g., by Brumberg & Kopeikin (1989), but this dependence becomes practically irrelevant if the fields outside of some matter distribution are parametrized by means of potential coefficients. This linearity implies that for an ensemble of $N$ -bodies

$$
w ( t , { \mathbf { x } } ) = \sum _ { A = 1 } ^ { N } w _ { A } ( t , { \mathbf { x } } ) , \qquad w ^ { i } ( t , { \mathbf { x } } ) = \sum _ { A = 1 } ^ { N } w _ { A } ^ { i } ( t , { \mathbf { x } } ) ,
$$

where the index $A$ indicates the contribution related with body $A$ where the integrals have to be taken over the support of body $A$ only. This linearity, however, does not imply that body-body interaction terms have been neglected. If written explicitly $w _ { A }$ will in general contain contributions from bodies $B \neq A$ (see e.g., Eq. (54)).

The BCRS metric tensor from the IAU 2000 Resolution B1.3 extends the form of the metric tensor given in the IAU 1991 Resolutions such that its accuracy is sufficient for most applications in the next years. Note that an extension of the old metric (2) is necessary (and has been in use for decades) for the derivation of the relativistic equations that form the basis of any modern solar system ephemeris (such as the JPL DE ephemerides). Resolution B1.3 formalises this extension.

# 3.3. The Geocentic Celestial Reference System

Resolution B1.3 continues to define the GCRS which represents a particular version of the local geocentric reference system for the Earth. Its spatial coordinates $X ^ { a }$ are kinematically non-rotating with respect to the barycentric ones (see e.g., Brumberg $\&$ Kopeikin 1989; Klioner & Soffel 1998). The geocentric coordinates are denoted by $( T , \mathbf { X } )$ , where $T = T C G$ . In the relation between $x ^ { \ i }$ and $X ^ { a }$ from Resolution B1.3 let us replace the unit matrix $\delta _ { a i }$ by a general rotation matrix $R _ { a i }$

$$
X ^ { a } = R _ { a i } \left[ r _ { E } ^ { i } + \frac { 1 } { c ^ { 2 } } \left( \ldots \right) \right] + { \mathcal O } ( c ^ { - 4 } ) ,
$$

where $\mathbf { r } _ { E } = \mathbf { x } - \mathbf { x } _ { E }$ . If the two sets of spatial coordinates are aligned for all times, i.e., if $R _ { a i } = \delta _ { a i }$ as is the case for the GCRS spatial coordinates, then $X ^ { a }$ is defined to be kinematically non-rotating with respect to the barycentric spatial coordinates $x ^ { i }$ . The Resolution recommends writing the metric tensor of the GCRS in the same form as the barycentric one but with potentials $W ( T , \mathbf { X } )$ and $W ^ { a } ( T , \mathbf { X } )$ . Explicitly,

$$
\begin{array} { l } { { \displaystyle G _ { 0 0 } = - 1 + \frac { 2 W } { c ^ { 2 } } - \frac { 2 W ^ { 2 } } { c ^ { 4 } } + \mathcal { O } ( c ^ { - 5 } ) , } } \\ { { \displaystyle G _ { 0 a } = - \frac { 4 } { c ^ { 3 } } W ^ { a } + \mathcal { O } ( c ^ { - 5 } ) , } } \\ { { \displaystyle G _ { a b } = \delta _ { a b } \left( 1 + \frac { 2 } { c ^ { 2 } } W \right) + \mathcal { O } ( c ^ { - 4 } ) } } \end{array}
$$

and the geocentric field equations formally look the same as the barycentric ones (10)–(11) but with all variables referred to the GCRS. Again one decisive advantage of this recommendation is the formal linearity of the field equations. This linearity admits a unique split of the geocentric metric into a part coming from the Earth itself and a remaining part resulting from inertial and tidal forces. Therefore it is recommended to split the potentials $W$ and $W ^ { a }$ according to

$$
{ \cal W } ( T , { \bf X } ) = W _ { E } ( T , { \bf X } ) + W _ { \mathrm { e x t } } ( T , { \bf X } ) , \qquad { \cal W } ^ { a } ( T , { \bf X } ) = W _ { E } ^ { a } ( T , { \bf X } ) + W _ { \mathrm { e x t } } ^ { a } ( T , { \bf X } ) .
$$

The Earth’s potentials $W _ { E }$ and $W _ { E } ^ { a }$ are defined in the same way as $w _ { E }$ and $w _ { E } ^ { u }$ , (i.e., equations (14)–(15) with integrals taken over the volume of the whole Earth) but with quantities calculated in the GCRS. Outside the Earth the potentials $( W , W ^ { a } )$ admit a power series expansion in terms of $R \equiv | \mathbf { X } |$ and all negative powers of $R$ are contained in $W _ { E }$ and $W _ { E } ^ { a }$ . For that reason the Earth’s potentials admit multipole expansions that look very similar to the Newtonian ones. This point will be discussed below in more detail.

It is useful to split the external potentials $W _ { \mathrm { e x t } }$ and $W _ { \mathrm { e x t } } ^ { a }$ further. They can be written in the form

$$
W _ { \mathrm { e x t } } = W _ { \mathrm { t i d a l } } + W _ { \mathrm { i n e r } } , \qquad W _ { \mathrm { e x t } } ^ { a } = W _ { \mathrm { t i d a l } } ^ { a } + W _ { \mathrm { i n e r } } ^ { a } ,
$$

where the tidal terms are at least quadratic in $X ^ { a }$ and the inertial contributions $W _ { \mathrm { i n e r } }$ and $W _ { \mathrm { i n e r } } ^ { a }$ are just linear in $X ^ { a }$ . Explicitly,

$$
\begin{array} { l } { { { \cal W } _ { \mathrm { i n e r } } { = } Q _ { a } X ^ { a } , } } \\ { { { \cal W } _ { \mathrm { i n e r } } ^ { a } { = } { - } { \frac { 1 } { 4 } } c ^ { 2 } \epsilon _ { a b c } \Omega _ { \mathrm { i n e r } } ^ { b } X ^ { c } . } } \end{array}
$$

Mathematically the $Q _ { a }$ term is related with the 4-acceleration of the geocenter in the external gravitational field, a quantity that vanishes for a purely spherical and non-rotating Earth (for a mass monopole more precisely) that moves along a geodesic in the external gravitational field. The $Q _ { a }$ term therefore results from the coupling of higher order multipole moments of the Earth to the external tidal gravitational fields (to the external curvature tensor of space-time in mathematical language). $Q _ { a }$ characterizes the deviation of the actual worldline of the origin of the GCRS from a geodesic in the external gravitational field. With

$$
w _ { \mathrm { e x t } } ( t , \mathbf { x } ) = \sum _ { A \neq E } w _ { A } ( t , \mathbf { x } ) , \qquad w _ { \mathrm { e x t } } ^ { i } ( t , \mathbf { x } ) = \sum _ { A \neq E } w _ { A } ^ { i } ( t , \mathbf { x } )
$$

to Newtonian order $Q _ { a }$ is given by

$$
Q _ { a } = \delta _ { a i } \left( \frac { \partial } { \partial x ^ { i } } w _ { \mathrm { e x t } } ( { \bf x } _ { E } ) - a _ { E } ^ { i } \right) .
$$

Here, $x _ { E } ^ { i } ( t ) , v _ { E } ^ { i } ( t ) = d x _ { E } ^ { i } / d t$ and $a _ { E } ^ { i } = d v _ { E } ^ { i } / d t$ are the barycentric coordinate position, velocity and acceleration of the origin of the GCRS (geocenter). The appearance of $\delta _ { a i }$ results from the fact that the GCRS is defined as kinematically non-rotating with respect to the BCRS. The reason to retain $\delta _ { a i }$ in the transformations here and below results from the desire to distinguish between BCRS (spatial indices taken from the second part of the latin alphabet, starting with the letter $i$ ) and GCRS quantities (spatial indices taken from the first part of the alphabet).

The full post-Newtonian expression for $Q _ { a }$ (denoted by $G _ { a } ( T )$ in the Damour-Soffel-Xu papers) can be derived from (6.30a) of Damour, Soffel $\&$ Xu (1991). To get an idea about orders of magnitude the absolute value of $Q _ { a }$ due to the action of the Moon is of order $4 \times 1 0 ^ { - 1 1 } \mathrm { m / s ^ { 2 } }$ (Kopeikin 1991).

The term $W _ { \mathrm { i n e r } } ^ { a }$ describes a relativistic Coriolis force due to the rotation of the GCRS with respect to a dynamically non-rotating geocentric reference system. Such a rotation has several components, often referred to as geodesic, Lense-Thirring and Thomas precessions

$$
\Omega _ { \mathrm { i n e r } } = \Omega _ { \mathrm { G P } } + \Omega _ { \mathrm { L T P } } + \Omega _ { \mathrm { T P } }
$$

with

$$
\Omega _ { \mathrm { G P } } = - \frac { 3 } { 2 c ^ { 2 } } { \bf v } _ { E } \times \nabla w _ { \mathrm { e x t } } ( { \bf x } _ { E } ) ,
$$

$$
\Omega _ { \mathrm { L T P } } = - \frac { 2 } { c ^ { 2 } } \nabla \times { \bf w } _ { \mathrm { e x t } } ( { \bf x } _ { E } ) ,
$$

$$
\Omega _ { \mathrm { T P } } { = } { - \frac { 1 } { 2 c ^ { 2 } } } { \bf v } _ { E } \times { \bf Q } ,
$$

in obvious notation. As a relativistic precession, the geodesic precession, $\Omega _ { \mathrm { G P } }$ , is proportional to $1 / c ^ { 2 }$ . It is also proportional to the barycentric coordinate velocity $v _ { E }$ and the gradient of the external gravitational scalar potential $w _ { \mathrm { e x t } }$ at the geocenter (the barycentric coordinate acceleration of the geocenter to sufficient accuracy). The order of magnitude is given by $| \Omega _ { \mathrm { G P } } | \sim$ $1 . 5 ( v _ { E } / c ) ( G M _ { S } / c ^ { 2 } A U ) ( c / A U ) \sim 3 \times 1 0 ^ { - 1 5 } \mathrm { s ^ { - 1 } \sim 2 ^ { \prime \prime } } _ { / }$ /century. Thomas precession is also proportional to $1 / c ^ { 2 }$ and the barycentric coordinate velocity of the geocenter but also to the geodesic deviation term $Q _ { a }$ . The order of magnitude of Thomas precession is $| \Omega _ { \mathrm { T P } } | \sim 0 . 5 ( v _ { E } / c ) | \mathbf { Q } | / c \sim$ $7 \times 1 0 ^ { - 2 4 } \mathrm { s } ^ { - 1 } \sim 4 \times 1 0 ^ { - 9 \prime \prime } ,$ /century, i.e., negligible with respect to geodesic precession.

Finally the Lense-Thirring precession results from the gradient of the external gravitomagnetic potential at the geocenter. If we consider some spherically symmetric solar system body $A$ , then the gravitomagnetic potential $W _ { A } ^ { a }$ of it is given by (see (49) below)

$$
W _ { A } ^ { a } = \frac { G } { 2 } \frac { ( \mathbf { S } _ { A } \times \mathbf { X } ) ^ { a } } { R ^ { 3 } }
$$

in its own local rest frame. Transformation into the BCRS according to the rule indicated below in (31) leads to

$$
w _ { A } ^ { i } ( t , \mathbf { x } ) = G \left[ \frac { ( \mathbf { S } _ { A } \times \mathbf { r } _ { A } ) ^ { i } } { 2 r _ { A } ^ { 3 } } + \frac { M _ { A } } { r _ { A } } v _ { A } ^ { i } \right] ,
$$

where $\mathbf { r } _ { A } \equiv \mathbf { x } - \mathbf { x } _ { A }$ and $\mathbf { v } _ { A }$ is the barycentric velocity of body $A$ . In our case the spin and motion of our Sun and Moon will give the dominant contributions to $\Omega _ { \mathrm { L T P } }$ : $| \Omega _ { \mathrm { L T P } } | \sim 2 \times 1 0 ^ { - 3 \prime \prime } / \mathrm { c }$ entury.

The definition of the GCRS implies that the spatial GCRS coordinates $\mathbf { X }$ are kinematically non-rotating with respect to the BCRS ones, $\mathbf { x }$ (as indicated by the $\delta _ { a i }$ -term in Resolution B1.3). Because of geodesic precession locally inertial coordinates precess with respect to the GCRS by an amount of $| \Omega _ { \mathrm { i n e r } } | = 1 . 9 1 9 8 ^ { \prime \prime }$ /century (Brumberg et al. 1992). Let us forget about the mass of the Earth and imagine a torque free gyroscope at the geocenter, moving along the actual trajectory of the geocenter. It will precess by this amount in our GCRS. Since the GCRS does not present a locally inertial reference system Coriolis forces caused by geodesic precession-nutation appear in every GCRS dynamical equation of motion, e.g., of Earth’s satellites. As recommended by IERS Conventions (2003) these additional forces should be taken into account. Moreover, geodesic precession-nutation has to be considered in the precession-nutation model formulated in the GCRS. E.g., the basic post-Newtonian equation of Earth’s intrinsic angular momentum $\mathbf { s }$ reads

$$
\frac { d \bf S } { d T } + \Omega _ { \mathrm { i n e r } } \times { \bf S } = { \bf D } ,
$$

where $\mathbf { D }$ is the external torque (Damour, Soffel & Xu 1993). As long as observations of Earth’s orientation parameters are referred to the GCRS they will contain geodesic precession-nutation automatically.

Because of the eccentricity of the Earth orbit the leading term in $\Omega _ { \mathrm { G P } }$ has an annual and a semi-annual part that leads to geodesic nutation in longitude with

$$
\Delta \psi _ { \mathrm { G P } } = 0 . 1 5 3 \sin l ^ { \prime } + 0 . 0 0 2 \sin 2 l ^ { \prime } ,
$$

where the amplitudes are in mas and $l ^ { \prime }$ is the mean anomaly of the Earth-Moon barycenter (Fukushima 1991; Brumberg et al. 1992; Bois $\&$ Vokrouhlick´y 1995).

$W _ { \mathrm { t i d a l } }$ is a generalization of the Newtonian tidal potential

$$
W _ { \mathrm { t i d a l } } ^ { \mathrm { N e w t o n } } ( T , { \mathbf { X } } ) = w _ { \mathrm { e x t } } ( { \mathbf { x } } _ { E } + { \mathbf { X } } ) - w _ { \mathrm { e x t } } ( { \mathbf { x } } _ { E } ) - { \mathbf { X } } \cdot \nabla w _ { \mathrm { e x t } } ( { \mathbf { x } } _ { E } ) .
$$

Full post-Newtonian expressions for $W _ { \mathrm { t i d a l } }$ and $W _ { \mathrm { t i d a l } } ^ { a }$ can be found in Damour, Soffel & Xu (1992). There $W _ { \mathrm { e x t } }$ is denoted by $\overline { W }$ and a tidal expansion in powers of local spatial coordinates by means of suitably defined tidal moments is given in (4.15) of Damour, Soffel $\&$ Xu (1992). Expressions for $W _ { \mathrm { t i d a l } }$ and $W _ { \mathrm { t i d a l } } ^ { a }$ in closed form are given in (Klioner $\&$ Voinov 1993). The quadratic term as dominant term of $W _ { \mathrm { t i d a l } }$ reads

$$
{ \cal W } _ { \mathrm { t i d a l } } \bigg | _ { l = 2 } = { \frac { 1 } { 2 } } G _ { a b } ^ { \mathrm { t i d a l } } X ^ { a } X ^ { b } .
$$

If the external bodies are taken as mass monopoles the explicit expression for $G _ { a b } ^ { \mathrm { t i d a l } }$ (not to be confused with the GCRS metric tensor) is given in (3.23) of Damour, Soffel $\&$ Xu (1994). Higherorder terms in this approximation can be found in Klioner, Soffel, Xu, Wu (2000).

Finally, the local gravitational potentials $W _ { E }$ and $W _ { E } ^ { a }$ of the Earth are related to the barycentric gravitational potentials $w _ { E }$ and $w _ { E } ^ { i }$ by $\delta _ { i } ^ { a } = \delta _ { a } ^ { i } = \delta _ { a i }$ )

$$
\begin{array} { l } { { \displaystyle W _ { E } ( T , { \bf X } ) = w _ { E } ( t , { \bf x } ) \left( 1 + \frac { 2 } { c ^ { 2 } } v _ { E } ^ { 2 } \right) - \frac { 4 } { c ^ { 2 } } v _ { E } ^ { i } w _ { E } ^ { i } ( t , { \bf x } ) + { \cal O } ( c ^ { - 4 } ) , } } \\ { { \displaystyle W _ { E } ^ { a } ( T , { \bf X } ) = \delta _ { i } ^ { a } \left( w _ { E } ^ { i } ( t , { \bf x } ) - v _ { E } ^ { i } w _ { E } ( t , { \bf x } ) \right) + { \cal O } ( c ^ { - 2 } ) } } \end{array}
$$

or by the inverse transformation

$$
\begin{array} { l } { { \displaystyle w _ { E } ( t , { \bf x } ) = W _ { E } ( T , { \bf X } ) \left( 1 + \frac { 2 } { c ^ { 2 } } v _ { E } ^ { 2 } \right) + \frac { 4 } { c ^ { 2 } } \delta _ { i a } v _ { E } ^ { i } W _ { E } ^ { a } ( T , { \bf X } ) + \mathcal { O } ( c ^ { - 4 } ) , } } \\ { { \displaystyle w _ { E } ^ { i } ( t , { \bf x } ) = \delta _ { a } ^ { i } W _ { E } ^ { a } ( T , { \bf X } ) + v _ { E } ^ { i } W _ { E } ( T , { \bf X } ) + \mathcal { O } ( c ^ { - 2 } ) . } } \end{array}
$$

The relations between the geocentric gravitational potentials $W$ and $W ^ { a }$ , and the barycentric ones $w$ and $w ^ { i }$ follow from the coordinate transformations between the BCRS and GCRS discussed below.

# 3.4. Coordinate transformations

The metric tensors in the BCRS and GCRS allow one to derive the rules for the transformations between the BCRS coordinates $x ^ { \mu }$ and the GCRS ones $X ^ { \alpha }$ from the tensorial transformation rules. It is obvious that these transformations can be written in two equivalent forms: i) as $x ^ { \mu } ( T , X ^ { a } )$ or ii) as $X ^ { \alpha } ( t , x ^ { i } )$ . Whereas the first form was used in the Damour-Soffel-Xu formalism (Damour, Soffel & Xu 1991, 1992, 1993, 1994), the second one was presented in the Brumberg-Kopeikin formalism (Brumberg & Kopeikin 1989; Kopeikin 1988; Brumberg 1991; Klioner & Voinov 1993). It should be pointed out that the transformation from one version to the other is not so trivial because of the barycentric coordinate position of the geocenter that appears in the first form as function of $T C G$ and as function of $T C B$ in the second one. In Resolution B1.3 $T = T C G$ and $X ^ { a }$ are presented as functions of $t = T C B$ and $x ^ { i }$ . The explicit form of the transformations is given in the text of Resolution B1.3 (see, Appendix A below). Apart from the terms of order $\mathcal { O } ( | \mathbf { X } | ^ { 3 } )$ that appear in the time transformation of order $\mathcal { O } ( c ^ { - 4 } )$ all terms can be obtained from the results derived by Kopeikin (1988) and Damour, Soffel $\&$ Xu (1991). The cubic and higher order terms in $| \mathbf { X } |$ as represented by the function $C$ have been derived by Kopeikin (1988) and analyzed in full detail by Klioner & Voinov (1993). As is also clear from Klioner & Voinov (1993) the expression for $C$ is not unique, but only constrained by the gauge and field equations so that the simplest possibility is an expression for $C$ containing cubic terms only. It is this simplest expression that is recommended in Resolution B1.3.

The full 4-dimensional coordinate transformation is just an extension of the usual Lorentz transformation. Indeed, if we neglect all gravitational fields and acceleration terms then the coordinate transformation in Resolution B1.3 can be written in the form ( ${ \bf r } = { \bf x } - { \bf x } _ { E } ( t )$ , $\beta = v / c = \mathrm { c o n s t } .$ )

$$
\begin{array} { l } { { \displaystyle T = t \left( 1 - \frac { 1 } { 2 } \beta ^ { 2 } - \frac { 1 } { 8 } \beta ^ { 4 } \right) - \left( 1 + \frac { 1 } { 2 } \beta ^ { 2 } \right) \frac { \bf v \cdot r } { c ^ { 2 } } + \mathcal { O } ( c ^ { - 6 } ) , } } \\ { { \displaystyle { \bf X } = { \bf r } + \frac { 1 } { 2 } ( { \bf v } \cdot { \bf r } ) \frac { \bf v } { c ^ { 2 } } + \mathcal { O } ( c ^ { - 4 } ) . } } \end{array}
$$

If we now write $\mathbf { x } _ { E } ( t ) = \mathbf { v } t$ we obtain

$$
\begin{array} { l } { { \displaystyle T = t \left( 1 + \frac { 1 } { 2 } \beta ^ { 2 } + \frac { 3 } { 8 } \beta ^ { 4 } \right) - \left( 1 + \frac { 1 } { 2 } \beta ^ { 2 } \right) \frac { { \bf v } \cdot { \bf x } } { c ^ { 2 } } + \mathcal { O } ( c ^ { - 6 } ) , } } \\ { { \displaystyle { \bf X } = { \bf x } - \left( 1 + \frac { 1 } { 2 } \beta ^ { 2 } \right) { \bf v } t + \frac { 1 } { 2 } ( { \bf v } \cdot { \bf x } ) \frac { { \bf v } } { c ^ { 2 } } + \mathcal { O } ( c ^ { - 4 } ) . } } \end{array}
$$

which is nothing but a Lorentz tranformation from Special Relativity Theory

$$
T = \gamma \left( t - { \frac { \mathbf { v } \cdot \mathbf { x } } { c ^ { 2 } } } \right) , \qquad \mathbf { X } = \mathbf { x } - \gamma \mathbf { v } t + { \frac { ( \gamma - 1 ) } { v ^ { 2 } } } ( \mathbf { v } \cdot \mathbf { x } ) \mathbf { v }
$$

in the corresponding approximation since

$$
\gamma \equiv ( 1 - \beta ^ { 2 } ) ^ { - 1 / 2 } = 1 + \frac { 1 } { 2 } \beta ^ { 2 } + \frac { 3 } { 8 } \beta ^ { 4 } + { \cal O } ( c ^ { - 6 } ) .
$$

Note that the inverse transformations are obtained simply by replacing $( t , \mathbf { x } )$ by $( T , \mathbf { X } )$ and the velocity $\mathbf { v }$ by $- \mathbf { v }$ .

Neglecting the $1 / c ^ { 4 }$ terms in the $T - t$ relation given in Resolution B1.3 one gets

$$
T = t - \frac { 1 } { c ^ { 2 } } \left( \int _ { t _ { 0 } } ^ { t } \left( \frac { v _ { E } ^ { 2 } } { 2 } + w _ { \mathrm { e x t } } ( \mathbf { x } _ { E } ) \right) d t + v _ { E } ^ { i } r _ { E } ^ { i } \right) + \mathcal { O } ( c ^ { - 4 } )
$$

which reduces to the old recommendation (4) since $t = T C B$ , $T = T C G$ and $w _ { \mathrm { e x t } } ( \mathbf { x } _ { E } ( t ) )$ reduces to $U _ { \mathrm { e x t } } ( t , \mathbf { x } _ { E } ( t ) )$ in the Newtonian limit. The more accurate version of this transformation will be discussed below.

Let us also note that the BCRS, GCRS and the transformation between them have been discussed by Klioner & Soffel (2000) in the framework of the PPN formalism with parameters $\beta$ and $\gamma$ . For the limit of General Relativity $\beta = \gamma = 1$ all the formulas given in that publication become equal to those derived in the framework of the new IAU Resolutions that refer solely to Einstein’s theory of gravity.

# 3.5. Potential coefficients

# 3.5.1. General post-Newtonian multipole moments

For many problems it is advantageous to present the local gravitational potentials of the Earth as multipole series that usually converge everywhere outside the Earth. To this end one has to introduce a certain set of multipole moments or potential coefficients for the Earth. A certain set of potential coefficients, called Blanchet-Damour (BD) moments (Blanchet & Damour 1986; Damour, Soffel & Xu 1991) defined to first post-Newtonian order has especially attractive features. Moreover, by using such Blanchet-Damour moments we get a very simple form of the multipole expansion of the post-Newtonian potentials (these expansions have almost Newtonian form). Basically two sets of BD moments occur in the formalism: mass multipole moments and spin multipole moments. Theoretically these moments can be derived from the distribution of mass and matter currents inside the body but for an observer they simply present parameters which can be directly estimated from observations.

Expressed in terms of symmetric and trace-free Cartesian tensors the BD moments are denoted by $\mathcal { M } _ { L }$ and $S _ { L }$ . Here, $L$ is a multi-index of $l$ different indices all taking the values $1 , 2 , 3$ , i.e., $L = i _ { 1 } i _ { 2 } \dots i _ { l }$ and every index $i = 1 , 2 , 3$ . Explicit expressions for $\mathcal { M } _ { L }$ and $S _ { L }$ as integrals over the Earth can be found in, e.g., Blanchet & Damour (1986); Damour, Soffel & Xu (1991)

$$
\begin{array} { l } { { \displaystyle { \mathcal M } _ { L } ( T ) \equiv \int d ^ { 3 } X \hat { X } ^ { L } \Sigma + \frac { 1 } { 2 ( 2 l + 3 ) c ^ { 2 } } \frac { d ^ { 2 } } { d T ^ { 2 } } \left[ \int d ^ { 3 } X \hat { X } ^ { L } { \bf X } ^ { 2 } \Sigma \right] } } \\ { { \displaystyle ~ - \frac { 4 ( 2 l + 1 ) } { ( l + 1 ) ( 2 l + 3 ) c ^ { 2 } } \frac { d } { d T } \left[ \int d ^ { 3 } X \hat { X } ^ { a L } \Sigma ^ { a } \right] , l \geq 0 , } } \end{array}
$$

$$
S _ { L } ( T ) \equiv \int \ d ^ { 3 } X \epsilon ^ { a b < c _ { l } } \hat { X } ^ { L - 1 > a } \Sigma ^ { b } , \quad l \geq 1 ,
$$

where the integrations extend over the body under consideration and

$$
\Sigma ( T , { \bf X } ) = \frac { 1 } { c ^ { 2 } } \left( { \cal T } ^ { 0 0 } + { \cal T } ^ { s s } \right) , \qquad \Sigma ^ { a } ( T , { \bf X } ) = \frac { 1 } { c } { \cal T } ^ { 0 a } .
$$

Here ${ \mathcal { T } } ^ { \mu \nu } = { \mathcal { T } } ^ { \mu \nu } ( T , X ^ { a } )$ are the components of the energy-momentum tensor in the GCRS. Both the caret and the sharp brackets indicate the symmetric and trace-free (STF) part of the object or of the indices enclosed by the brackets (see, e.g. Damour, Soffel & Xu (1991) p. 3277 for the explicit definition of the STF part of an object). Some basic information on the operations with the STF objects can be found, e.g. in Blanchet $\&$ Damour (1986); Damour, Soffel & Xu (1992).

For practical applications, however, their explicit form will not be needed, since these quantities are parameters characterizing the gravitational field of the corresponding body which are fitted to observations. The set $\mathcal { M } _ { L }$ is equivalent to a set of potential coefficients $C _ { l m }$ and $S _ { l m }$ that appear in a much more familiar spherical harmonic expansion of $W _ { E }$ . The first non-vanishing spin moment (the spin dipole) of a body agrees with its spin vector (total intrinsic angular momentum). The multipole expansion of $W _ { E }$ and $W _ { E } ^ { a }$ reads

$$
W _ { E } = G \sum _ { l = 0 } ^ { \infty } \frac { ( - 1 ) ^ { l } } { l ! } \left[ \mathcal { M } _ { L } \partial _ { L } \frac { 1 } { | \mathbf { X } | } + \frac { 1 } { 2 c ^ { 2 } } \ddot { \mathcal { M } } _ { L } \partial _ { L } | \mathbf { X } | \right] + \frac { 4 } { c ^ { 2 } } \Lambda _ { , T } + \mathcal { O } ( c ^ { - 4 } ) ,
$$

$$
W _ { E } ^ { a } = - G \sum _ { l = 1 } ^ { \infty } \frac { ( - 1 ) ^ { l } } { l ! } \left[ \dot { \mathcal { M } } _ { a L - 1 } \partial _ { L - 1 } \frac { 1 } { | \mathbf { X } | } + \frac { l } { l + 1 } \epsilon _ { a b c } S _ { c L - 1 } \partial _ { b L - 1 } \frac { 1 } { | \mathbf { X } | } \right] - \Lambda _ { , a } + \mathcal { O } ( c ^ { - 2 } ) ,
$$

where

$$
\Lambda { = } G \sum _ { l = 0 } ^ { \infty } \frac { ( - 1 ) ^ { l } } { ( l + 1 ) ! } \frac { 2 l + 1 } { 2 l + 3 } \mathcal { P } _ { L } \partial _ { L } \frac { 1 } { | \mathbf { X } | } ,
$$

$$
{ \mathcal { P } } _ { L } = \int _ { V } \Sigma ^ { a } { \hat { X } } ^ { a L } d ^ { 3 } X .
$$

Here the dot stands for $\partial / \partial T$ and $\partial _ { L }$ for $\partial ^ { l } / \partial x ^ { i _ { 1 } } \dots \partial x ^ { i _ { l } }$ . Also the comma denotes partial differentiation, $\Lambda _ { , T } \equiv \partial \Lambda / \partial T$ and $\Lambda _ { , a } \equiv \partial \Lambda / \partial X ^ { a }$ .

The gauge function $\Lambda$ does not enter the post-Newtonian equations of motion. The latter contains only the BD multipole moments $\mathcal { M } _ { L }$ and $S _ { L }$ . The only place where the function $\Lambda$ should be accounted for is in the transformation between the various time scales. However, these gauge terms are of order $1 / c ^ { 4 }$ in the metric tensor so for the problem of clock rates they are basically of second post-Newtonian order. These terms are much less than $1 0 ^ { - 1 8 }$ in the geocentric metric tensor and will be neglected. For that reason the $\Lambda$ -terms are not mentioned in Resolution B1.4.

3.5.2. Approximate expansion of the scalar gravitational potential

A spherical harmonic expansion of $W _ { E }$ equivalent to (38) without the $\Lambda$ term reads ( $R = | \mathbf { X } |$

$$
\begin{array} { l } { { \displaystyle { \cal N } _ { E } ( T , { \bf X } ) = \frac { G M _ { E } } { R } \Big [ 1 + \sum _ { l = 2 } ^ { \infty } \sum _ { m = 0 } ^ { + l } \left( \frac { R _ { E } } { R } \right) ^ { l } P _ { l m } ( \cos \theta ) ( \mathcal { C } _ { l m } ( T , R ) \cos m \phi + \mathcal { S } _ { l m } ( T , R ) \sin m \theta + \mathcal { S } _ { l m } ( T , R ) \cos m \theta + \mathcal { S } _ { l m } ( T , R ) \cos m \theta } } \\ { { \displaystyle ~ + \mathcal { O } ( c ^ { - 4 } ) } } \end{array}
$$

with

$$
\begin{array} { l } { { \displaystyle { \mathcal C } _ { l m } ^ { E } ( T , R ) { = } C _ { l m } ^ { E } ( T ) - \frac { 1 } { 2 ( 2 l - 1 ) } \frac { R ^ { 2 } } { c ^ { 2 } } \frac { d ^ { 2 } } { d T ^ { 2 } } C _ { l m } ^ { E } ( T ) } } \\ { { \displaystyle { \mathcal S } _ { l m } ^ { E } ( T , R ) { = } S _ { l m } ^ { E } ( T ) - \frac { 1 } { 2 ( 2 l - 1 ) } \frac { R ^ { 2 } } { c ^ { 2 } } \frac { d ^ { 2 } } { d T ^ { 2 } } S _ { l m } ^ { E } ( T ) . } } \end{array}
$$

Let us stress that as stated in Resolution B1.4 $C _ { l m } ^ { E } ( T )$ and $S _ { l m } ^ { E } ( T )$ refer to the GCRS coordinates and are related with approximately constant potential coefficents in a terrestrial system that is rotating with the Earth (i.e. those from an Earth’s model) by time-dependent transformations. For a rigid axially symmetric body rotating about its symmetry axis with angular velocity $\Omega _ { E }$ the second time derivative terms will vanish. Let us estimate these terms for the Earth. From the order of magnitude of the $l = m = 2$ terms in the reference system corotating with the Earth one finds $C _ { 2 2 } ^ { E }$ and $S _ { 2 2 } ^ { E }$ of order $1 0 ^ { - 6 }$ . The expected order of magnitude of the second time derivative terms is $( \Omega _ { E } R _ { E } / c ) ^ { 2 } \simeq 1 0 ^ { - 1 2 }$ times smaller than the corresponding ’Newtonian terms’ from $C _ { 2 2 } ^ { E }$ or $S _ { 2 2 } ^ { E }$ . The Newtonian terms lead to contributions in $G _ { 0 0 }$ of order $1 0 ^ { - 1 5 }$ and hence the second time derivative terms to contributions of order $1 0 ^ { - 2 7 }$ . This is about nine orders of magnitude less than the $2 W ^ { 2 } / c ^ { 4 }$ term in $G _ { 0 0 }$ which is of order $1 0 ^ { - 1 8 }$ . For that reason these second time derivative terms in the Earth’s metric can safely be neglected at present. They are not mentioned in Resolution B1.4.

# 3.5.3. Approximate expansion of the vector gravitational potential

Let us now come to the gravitomagnetic vector potential of the Earth, $W _ { E } ^ { a }$ . As can be seen from (39) this potential is determined by the set of spin moments and the first time derivative of the mass moments. As already mentioned, to characterize the gravitational field outside of some matter distribution in GRT two independent sets of multipole moments have to be used that in principle should be determined from observational data. So far the spin moments of some astronomical body have not been studied and more work is needed here. Formally the spin moments of the Earth are given by expression (36) above. Since for the post-Newtonian metric we need these spin moments only to Newtonian order we might proceed with a simple Newtonian model of a rigidly rotating Earth with

$$
\boldsymbol { \Sigma } = \boldsymbol { \Sigma } \left( \boldsymbol { \Omega } \times \mathbf { X } \right) ,
$$

where $\Sigma$ is the gravitational mass-energy density in the GCRS and $\Omega$ is the angular velocity of rotation that at this place has to be defined only to Newtonian order. Under this assumption all spin moments are proportional to the angular velocity and one might define a set of Cartesian tensors $C _ { L d }$ such that

$$
\begin{array} { r } { S _ { L } = C _ { L d } \Omega ^ { d } . } \end{array}
$$

These tensors $C _ { L d }$ obey the following Newtonian relations

$$
C _ { L d } = - M _ { L d } + { \frac { l + 1 } { 2 l + 1 } } \delta _ { d < a _ { l } } N _ { L - 1 > } ,
$$

where

$$
M _ { L } \equiv \int _ { E } \Sigma \hat { X } ^ { L } d ^ { 3 } X , \qquad N _ { L } \equiv \int _ { E } \Sigma { \bf X } ^ { 2 } \hat { X } ^ { L } d ^ { 3 } X .
$$

Note that $C _ { L d }$ is symmetric and trace-free only in the first $L$ indices. Moreover, for the Newtonian mass moments $M _ { L }$ one has

$$
M _ { L } = - C _ { < L > } .
$$

For a homogeneous ( $\Sigma = \mathrm { c o n s t }$ .) and spherical Earth with radius $R _ { E }$ one finds for $l = 1$ the usual expression for the moment of inertia tensor

$$
C _ { a b } = \delta _ { a b } \left( \frac { 2 } { 5 } M R _ { E } ^ { 2 } \right)
$$

that yields the total intrinsic angular momentum (spin) vector of the Earth according to $\textstyle S _ { a } =$ $C _ { a b } \Omega ^ { b }$ . For a spherically symmetric and mass centered Earth all mass moments $M _ { L }$ with $l \geq 1$ vanish and also all quantities $N _ { L }$ with $l > 0$ . Hence in such a simple model only the spin vector is different from zero and all higher spin moments vanish. For that reason we also considered a rigidly rotating homogeneous oblate spheroid with equatorial radius $A$ and polar radius $C$ . For such a model all even spin moments vanish since they are proportional to $C _ { L }$ with odd $l$ . On the contrary, odd spin moments proportional to $C _ { L }$ with even $l$ are nonzero. For the spin dipole the usual result $C _ { X X } = C _ { Y Y } = M ( A ^ { 2 } + C ^ { 2 } ) / 5$ and $C _ { Z Z } = 2 M A ^ { 2 } / 5$ for the moment of inertia tensor is found. By means of computer algebra all components $C _ { L }$ can be found for any value of $l$ . Let $\eta = ( 4 M A ^ { 4 } / 5 2 5 ) \epsilon ^ { 2 }$ with $\epsilon ^ { 2 } = ( A ^ { 2 } - C ^ { 2 } ) / A ^ { 2 } \simeq 2 f$ , where $f$ is the usual flattening. Assuming $\Omega ^ { d } = ( 0 , 0 , \Omega )$ we found all non-vanishing $l = 3$ terms, up to symmetries and terms of order $f ^ { 2 }$ : $S _ { X X Z } = S _ { Y Y Z } = 3 \eta \Omega$ and $S _ { Z Z Z } = - 6 \eta \Omega$ . This implies that the metric term resulting from the spin octupole of the Earth near the Earth’s surface is about $1 0 ^ { 4 }$ times smaller than the one from the spin dipole. In the following the contributions of higher spin moments will be neglected.

Besides the spin moments the first time derivative of the mass moments contribute to the gravitomagnetic field of the Earth. For $l = 0$ we encounter a $\dot { \mathcal { M } } _ { a }$ term that vanishes if the post-Newtonian center of mass condition $\mathcal { M } _ { a } = 0$ is imposed. The next term is given by $\dot { \mathcal { M } } _ { a b }$ that is of order $| C _ { 2 2 } ^ { E } | M R _ { E } ^ { 2 } \Omega$ and would vanish for an axially symmetric rigid body rotating about its symmetry axis as well as the time derivative of all higher mass moments. For the Earth the $\dot { \mathcal { M } } _ { a b }$ term is smaller than the spin term (which is of order $2 M R _ { E } ^ { 2 } \Omega / 5$ ) by a factor determined by $C _ { 2 2 } ^ { E } \simeq 1 . 6 \times 1 0 ^ { - 6 }$ and hence negligible. On the other hand, the vector potential $W _ { E } ^ { a } ( T , { \bf X } )$ is employed only in the calculations of small relativistic effects (e.g. Lense-Thirring effects, higherorder relativistic effects in the time transformations). This implies that the expansion (39) for $W _ { E } ^ { a } ( T , { \bf X } )$ can be truncated to the approximate expression

$$
{ \cal W } _ { E } ^ { a } ( T , { \bf X } ) = - \frac { G } { 2 } \frac { ( { \bf X } \times { \bf S } _ { E } ) ^ { a } } { R ^ { 3 } } ,
$$

where $\mathbf { S } _ { E }$ is a vector with components $S _ { a }$ . This expression can be found in many standard textbooks on GRT (Weinberg 1972; Will 1993) and is usually related with Lense-Thirring effects resulting from the Earth’s rotational motion.

The reason why to characterize $W _ { E } ^ { a }$ by the spin vector and not by the angular velocity vector of the Earth is a conceptual one since usually it is advantageous to characterize the gravitational field of the Earth in the outside region by multipole moments. To get $W _ { E } ^ { a }$ the Earth’s spin vector is needed only to Newtonian order and can be taken from current precession-nutation models. Although one might use Newtonian concepts to relate the gravitomagnetic field of the Earth with some Earth’s angular velocity, we prefer to employ the well-defined concept of multipole moments here which are independent of any theoretical assumptions on the rotational motion of the Earth.

# 3.6. The barycentric metric in the mass monopole approximation

In the gravitational N-body problem the potential coefficents of a body $A$ are defined in its corresponding local reference system (analogous to the GCRS for the Earth). For many applications it is sufficient to keep only the mass monopoles of the solar system bodies, i.e., to put

$$
\mathcal { M } _ { L } = 0 \quad \mathrm { f o r } \quad l \geq 1 , \qquad \mathcal { S } _ { L } = 0 \quad \mathrm { f o r } \quad l \geq 1
$$

for all bodies and to keep the masses only, i.e., each body $A$ is characterized by the value for its post-Newtonian mass $\mathcal { M } _ { A }$ (we also put $P _ { L } = 0$ ). In the following we will use the symbol $M _ { A }$ instead of $\mathcal { M } _ { A }$ to be compatible with the text of the IAU 2000 Resolutions.

From the transformation rules for the metric potentials (31), expansions (38)–(39) and formula (18) one derives the metric in the barycentric coordinate system in the form (8) with

$$
w = w _ { 0 } - \frac { 1 } { c ^ { 2 } } \Delta
$$

where

$$
w _ { 0 } ( t , \mathbf { x } ) \equiv \sum _ { A } \frac { G M _ { A } } { r _ { A } }
$$

and

$$
\Delta ( t , \mathbf { x } ) = \sum _ { A } \Delta _ { A } ( t , \mathbf { x } )
$$

with ( $\mathbf { r } _ { B A } = \mathbf { x } _ { B } - \mathbf { x } _ { A }$ and $\mathbf { a } _ { A } = d \mathbf { v } _ { A } / d t$ )

$$
\begin{array} { l } { \displaystyle \Delta _ { A } ( t , { \bf x } ) = \frac { G M _ { A } } { r _ { A } } \left( - \frac { 3 } { 2 } v _ { A } ^ { 2 } + \sum _ { B \ne A } \frac { G M _ { B } } { r _ { B A } } \right) - \frac { 1 } { 2 } G M _ { A } r _ { A , t t } } \\ { \displaystyle \qquad = \frac { G M _ { A } } { r _ { A } } \left[ - 2 v _ { A } ^ { 2 } + \sum _ { B \ne A } \frac { G M _ { B } } { r _ { B A } } + \frac { 1 } { 2 } \left( \frac { ( r _ { A } ^ { k } v _ { A } ^ { k } ) ^ { 2 } } { r _ { A } ^ { 2 } } + r _ { A } ^ { k } a _ { A } ^ { k } \right) \right] . } \end{array}
$$

Furthermore, in our approximation

$$
w ^ { i } ( t , { \bf x } ) = \sum _ { A } \frac { G M _ { A } } { r _ { A } } v _ { A } ^ { i } .
$$

Note, that we have chosen the minus sign in front of $\Delta$ to have a plus sign in the $c ^ { - 4 }$ part of $g _ { 0 0 }$ (see Resolution B1.5). Note furthermore, that the post-Newtonian Einstein-Infeld-Hoffmann equations of motion for a system of mass monopoles, that form the basis of modern solar system ephemerides, can be derived from that form of the barycentric metric (for details see Damour, Soffel & Xu 1991). Thus, the barycentric mass monopole metric given above is already in use for the description of the solar system dynamics.

One improvement of this simple mass monopole model is to consider the spin dipoles of the various bodies as well (that is, to consider also $\mathbf { S } _ { A }$ to be non-zero). Actually Resolution B1.5 is based upon such a mass monopole spin dipole model where modifications from the simple mass monopole model are indicated explicitly.

# 4. Time and frequency applications in the solar system

For practical applications concerning time and frequency measurements in the solar system it is necessary to consider a conventional model for the realization of time coordinates and time transformations. This model should be chosen so that i) its accuracy is significantly better than the expected performance of clocks and time transfer techniques, ii) it is consistent with the general framework of Section 3 and iii) it may readily be used with existing astrometric quantities, e.g. solar systems ephemerides.

Regarding item (i), we may derive reasonable accuracy limits for such a model in a straightforward way. At present the best accuracies are reached by Cs-fountain clocks operating at less than two parts in $1 0 ^ { 1 5 }$ in fractional frequency (Lemonde et al. 2001; Weyers et al. 2001). Their frequency stability for time spans up to a few days characterized by a standard Allan deviation is of order $\sigma _ { y } ( \tau ) = 4 \times 1 0 ^ { - 1 4 } \tau ^ { - 1 / 2 }$ , for an integration time $\tau$ in seconds. In the near future, high accuracy laser cooled Rb clocks (Bize et al. 1999) and space-borne Cs clocks (Lemonde et al. 2001) are expected to reach accuracies of a few parts in $1 0 ^ { 1 7 }$ in fractional frequency and stabilities of order $\sigma _ { y } ( \tau ) = 1 \times 1 0 ^ { - 1 4 } \tau ^ { - 1 / 2 }$ . The uncertainty in the time transformations should induce errors that are always lower than the expected performance of these future clocks. Including a factor 2 as safety margin, we therefore conclude that time coordinates and time transformations should be realized with an uncertainty not larger than $5 \times 1 0 ^ { - 1 8 }$ in rate or, for quasi-periodic terms, not larger than $5 \times 1 0 ^ { - 1 8 }$ in rate and 0.2 ps in amplitude.

For the spatial domain of validity of the transformations, we note that projects like SORT (Solar Orbit Relativity Test) plan to fly highly accurate clocks to within 0.25 AU of the Sun, which is therefore the lower limit for the distance to the barycenter that we will consider. In the geocentric system we will consider locations from the Earth’s surface up to geostationary orbits ( $| \mathbf { X } | < 5 0 0 0 0 \ \mathrm { k m }$ ).

To comply with item (ii), we render the developments following the general framework outlined in Section 3 and we show (iii) how the time transformations, e.g., $T C B - T C G$ , may be performed with the existing astrometric quantities and tools.

# 4.1. Barycentric reference system

Let us write the barycentric metric potential $w ( t , \mathbf { x } )$ in the form

$$
w = w _ { 0 } + w _ { L } - \frac { 1 } { c ^ { 2 } } \Delta ,
$$

where $w _ { L }$ contains contributions from higher potential coefficients with $l \geq 1$ and can be determined from equation (38) and the transformation rules of the metric potentials. Evaluating the $\Delta _ { A }$ terms from Resolution B1.5 (equation (54) plus spin terms) for all bodies of the solar system, we find that in the metric tensor $| \Delta _ { A } ( t , { \bf x } ) | / c ^ { 4 }$ may reach at most a few parts in $1 0 ^ { 1 7 }$ in the vicinity of Jupiter and about $1 0 ^ { - 1 7 }$ close to the Earth. Presently, however, for all planets except the Earth, the magnitude of $\Delta _ { A } ( t , { \bf x } ) / c ^ { 4 }$ in the vicinity of the planet is smaller than the uncertainty in $w _ { 0 } / c ^ { 2 }$ or $w _ { L } / c ^ { 2 }$ originating from the uncertainties in its mass multipole moments so that it is practically not needed to account for these terms. Nevertheless, when new astrometric observations allow to derive the moments with adequate uncertainty, it will be necessary to do so. In any case, for the vicinity of a given body $A$ , only the effect of $\Delta _ { A } ( t , { \bf x } )$ is needed in practice, i.e., the effect of $\textstyle \sum _ { B \neq A } \Delta _ { B } ( t , \mathbf { x } )$ is smaller than our accuracy specifications. For the comparison of proper time of a clock in the vicinity of the Earth with that of other clocks in the solar system or with $T C B$ it may thus be needed to account for $\Delta _ { E } ( t , { \bf x } ) / c ^ { 4 }$ .

From (8) and (56) the transformation between proper time of some observer and $T C B$ may be derived within our accuracy limit

$$
\mathrm { d } \tau / \mathrm { d } T C B = 1 - \frac { 1 } { c ^ { 2 } } \left( w _ { 0 } + w _ { L } + \frac { v ^ { 2 } } { 2 } \right) + \frac { 1 } { c ^ { 4 } } \left( - \frac { 1 } { 8 } v ^ { 4 } - \frac { 3 } { 2 } v ^ { 2 } w _ { 0 } + 4 v ^ { i } w ^ { i } + \frac { 1 } { 2 } w _ { 0 } ^ { 2 } + \Delta \right) ,
$$

where $v ^ { i }$ is the BCRS coordinate velocity of the observer. Similarly, the transformation between $T C B$ and $T C G$ in the immediate vicinity of the Earth, accurate to the limits as specified above can be derived from the general post-Newtonian $T C B - T C G$ transformation from Resolution B1.3 as

$$
T C B - T C G = c ^ { - 2 } \left[ \int _ { t _ { 0 } } ^ { t } \left( \frac { v _ { E } ^ { 2 } } { 2 } + w _ { 0 , \mathrm { e x t } } ( \mathbf { x } _ { E } ) \right) d t + v _ { E } ^ { i } r _ { E } ^ { i } \right]
$$

$$
\begin{array} { l } { { \displaystyle - c ^ { - 4 } [ \int _ { t _ { 0 } } ^ { t } \left( - \frac { 1 } { 8 } v _ { E } ^ { 4 } - \frac { 3 } { 2 } v _ { E } ^ { 2 } w _ { 0 , \mathrm { e x t } } ( { \bf x } _ { E } ) + 4 v _ { E } ^ { i } w _ { \mathrm { e x t } } ^ { i } ( { \bf x } _ { E } ) + \frac { 1 } { 2 } w _ { 0 , \mathrm { e x t } } ^ { 2 } ( { \bf x } _ { E } ) \right) d t } } \\ { { \displaystyle ~ - ( 3 w _ { 0 , \mathrm { e x t } } ( { \bf x } _ { E } ) + v _ { E } ^ { 2 } / 2 ) v _ { E } ^ { i } r _ { E } ^ { i } ] , } } \end{array}
$$

where $t$ is $T C B$ . Here $w _ { \mathrm { 0 , e x t } }$ is defined by (52) with summation over all solar system bodies expect the Earth. Note that $t _ { 0 }$ was not explicitly defined in Resolution B1.5 (2000). It is the origin of $T C B$ and $T C G$ , defined in Resolution A4 (1991) (see Section 2.1). The external contributions to $w _ { L }$ and $\Delta$ are beyond our accuracy limit and can be neglected here.

This equation is composed of terms evaluated at the geocenter (the two integrals) and of position dependent terms linear in $\left| \mathbf { r } _ { E } \right|$ , terms with higher powers of $\left| \mathbf { r } _ { E } \right|$ having been found to be negligible. The integrals may be computed from existing planetary ephemerides (Fukushima 1995; Irwin $\&$ Fukushima 1999). Since, in general, the planetary ephemerides are expressed in terms of a time argument $T _ { \mathrm { e p h } } = ( 1 - L _ { B } ) T C B + T _ { \mathrm { e p h } } ^ { \mathrm { 0 } }$ (Standish 1998; Irwin & Fukushima 1999), the first integral will be computed as

$$
\int _ { t _ { 0 } } ^ { t } \left( \frac { v _ { E } ^ { 2 } } { 2 } + w _ { 0 , \mathrm { e x t } } ( \mathbf { x } _ { E } ) \right) d t = \left[ \int _ { T _ { \mathrm { e p h } _ { 0 } } } ^ { T _ { \mathrm { e p h } } } \left( \frac { v _ { E } ^ { 2 } } { 2 } + w _ { 0 , \mathrm { e x t } } ( \mathbf { x } _ { E } ) \right) d T _ { \mathrm { e p h } } \right] / \left( 1 - L _ { B } \right) .
$$

Terms in the second integral of (58) are secular and quasi periodic. They amount to $\sim$ $1 . 1 \times 1 0 ^ { - 1 6 }$ in rate $( \mathrm { d } T C B / \mathrm { d } T C G )$ and primarily a yearly term of $\sim 3 0$ ps in amplitude (i.e. corresponding to periodic rate variations of amplitude $\sim 6 \times 1 0 ^ { - 1 8 }$ ). Position-dependent terms in $c ^ { - 4 }$ are not negligible and reach, for example, an amplitude of 0.4 ps ( $\sim 3 \times 1 0 ^ { - 1 7 }$ in rate) in geostationary orbit.

# 4.2. Geocentric reference system

Evaluating the contributions of the different terms in the metric tensor of the GCRS given in Resolution B1.3 to the $\mathrm { d } { \tau } / \mathrm { d } ( T C G )$ transformation on the Earth’s surface and up to geostationary orbit we find that terms of order $c ^ { - 2 }$ reach 7 parts in $1 0 ^ { 1 0 }$ while the contributions from $W ^ { 2 }$ and $W ^ { a }$ do not exceed 5 parts in $1 0 ^ { 1 9 }$ . Also, the terms from $W _ { \mathrm { i n e r } }$ in $W$ remain below $2 \times 1 0 ^ { - 2 0 }$ . Therefore, the terms given in the IAU 1991 framework with the metric of the form (2) are sufficient for time and frequency applications in the GCRS in the region $| \mathbf { X } | < 5 0 0 0 0 \mathrm { k m }$ for present and foreseeable future clock accuracies. Note, some care needs to be taken when evaluating the potential $W$ at the location of the clock which is not trivial when accuracies of order $1 0 ^ { - 1 8 }$ are required (Klioner 1992; Petit & Wolf 1994; Wolf & Petit 1995).

Presently, the time scale of reference for all practical issues on Earth is Terrestrial Time $( T T )$ or one of the scales realizing it and differing by some time offset (e.g., T AI, $U T C$ , $G P S$ time). $x \ i { 1 } \ i$ was defined in IAU Resolution A4 (1991) as: ”a time scale differing from the Geocentric Coordinate

Time $T C G$ by a constant rate, the unit of measurement of $T T$ being chosen so that it agrees with the SI second on the geoid”. According to the transformation between proper and coordinate time, this constant rate is given by $\mathrm { d } ( T T ) / \mathrm { d } ( T C G ) = 1 - U _ { g } / c ^ { 2 } = 1 - L _ { G }$ , where $U _ { g }$ is the gravity (gravitational $^ +$ rotational) potential on the geoid (this notation is used instead of the usual ${ \mathcal { W } } _ { 0 }$ ’ to avoid confusion with GCRS gravitational potential $W$ used throughout the paper).

Some shortcomings appeared in this definition of $T T$ when considering accuracies below $1 0 ^ { - 1 7 }$ . First, the uncertainty in the determination of $U _ { g }$ is of order $1 \mathrm { m } ^ { 2 } \mathrm { s } ^ { - 2 }$ or slightly better (Burˇsa 1995; Groten 1999). Second, even if it is expected that the uncertainty in $U _ { g }$ improves with time the surface of the geoid is difficult to realize (so that it is difficult to determine the potential difference between the geoid and the location of a clock). Third, the geoid is, in principle, variable with time. Therefore it was decided to desociate the definition of $T T$ from the geoid while maintaining continuity with the previous definition. The constant $L _ { G }$ was turned into a defining constant with its value fixed to $6 . 9 6 9 2 9 0 1 3 4 \times 1 0 ^ { - 1 0 }$ (Resolution B1.9, see Appendix A). This removes the limitations mentioned above when realizing $' L " L "$ from clocks on board of terrestrial satellites (such as in the GPS). In Table 1 we present numerical values for the constants $L _ { C }$ , $L _ { G }$ and $L _ { B }$ relating the mean rates of different relativistic timescales.

# 5. Final remarks

The relativistic Resolutions of the IAU represent a post-Newtonian framework allowing one to model any kind of astronomical observations in a rigorous, self-consistent manner with accuracies that are sufficient for the next decades. They replace the old IAU relativistic framework that was insufficient for many reasons discussed above. These new Resolutions, however, are not expected to lead to dramatic changes. In fact in many fields of application the models presently in use are already fully compatible with the new IAU Resolutions and in this sense the IAU Resolutions officially fix the status quo. Let us give some examples for that.

The metric tensor of the BCRS allows one to derive the Einstein-Infeld-Hoffman equations

<table><tr><td>IAU 1991</td><td>s/s</td><td>IAU 2000 s/s</td><td>）IAU 2000 ms/yr</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td>Lc</td><td>1.480813 × 10-8</td><td>1.48082686741 × 10-8</td><td>467.313</td></tr><tr><td>LG</td><td>6.969291 × 10-10</td><td>6.969290134 × 10-10</td><td>21.993</td></tr><tr><td>Lb = Lc+Lg -Lc Lg</td><td>1.550505 × 10-8</td><td>1.55051976772 × 10-8</td><td>489.307</td></tr></table>

Table 1: The constants relating the mean rates of different relativistic timescales. Both the values adopted by the IAU 1991 recommendations and the IAU 2000 resolutions are given. As an illustration the IAU 2000 values are also given in milliseconds per Julian year.

which have been used since the 70s to construct the JPL numerical ephemerides of planetary motion (Newhall, Standish & Williams 1983). The BCRS is the basic astrometric reference system where concepts such as ’radial velocity’ or ’proper motion’ are defined (Lindegren & Dravins 2003). The metric tensors of both GCRS and BCRS and the transformation between corresponding coordinates were used to formulate the VLBI model employed by the IERS since 1992 (IERS Standards 1992; IERS Conventions 1996, 2003). The equations of motion of the Earth’s satellites recommended by the IERS (IERS Standards 1992; IERS Conventions 1996, 2003) are compatible with the new IAU framework and can be derived from the given metric tensor of the GCRS.

The models used for costructing the HIPPARCOS catalog make it clear that this catalog represents a materialization of the BCRS. The full power of the new IAU theoretical framework will be needed to construct the model for astrometric positional observations with an accuracy of 1 microarcsecond which will be necessary for future astrometric missions. Work in this direction has already started (Klioner 2003).

It is obvious that this explanatory supplement presents only a first step to show how the new IAU Resolutions concerning relativity should be employed in practice. Much more work will be necessary to reach that goal.

The anonymous referee is thanked for his valuable suggestions to improve the text and to make it more readable.

# A. IAU Resolutions concerning Relativity Adopted at the 24th General Assembly Resolution B1.3: Definition of Barycentric Celestial Reference System and Geocentric Celestial Reference System

The XXVIth International Astronomical Union General Assembly

# Considering

1. that the Resolution A4 of the XXIst General Assembly (1991) has defined a system of spacetime coordinates for (a) the solar system (now called the Barycentric Celestial Reference System, (BCRS)) and (b) the Earth (now called the Geocentric Celestial Reference System (GCRS)), within the framework of General Relativity,

2. the desire to write the metric tensors both in the BCRS and in the GCRS in a compact and self-consistent form, and

3. the fact that considerable work in General Relativity has been done using the harmonic gauge that was found to be a useful and simplifying gauge for many kinds of applications,

# Recommends

1. the choice of harmonic coordinates both for the barycentric and for the geocentric reference systems,

2. writing the time-time component and the space-space component of the barycentric metric $g _ { \mu \nu }$ with barycentric coordinates $( t , \mathbf { x } )$ ( $t =$ Barycentric Coordinate Time $( T C B ) _ { , }$ ) with a single scalar potential $w ( t , \mathbf { x } )$ that generalizes the Newtonian potential, and the space-time component with a vector potential $w ^ { i } ( t , \mathbf { x } )$ ; as a boundary condition it is assumed that these two potentials vanish far from the solar system,

explicitly,

$$
\begin{array} { l } { { g _ { 0 0 } = - 1 + \displaystyle \frac { 2 w } { c ^ { 2 } } - \displaystyle \frac { 2 w ^ { 2 } } { c ^ { 4 } } , } } \\ { { g _ { 0 i } = - \displaystyle \frac { 4 } { c ^ { 3 } } w ^ { i } , } } \\ { { g _ { i j } = \delta _ { i j } \left( 1 + \displaystyle \frac { 2 } { c ^ { 2 } } w \right) , } } \end{array}
$$

with

$$
\begin{array} { l } { { \displaystyle w ( t , { \bf x } ) = G \int d ^ { 3 } x ^ { \prime } \frac { \sigma ( t , { \bf x } ^ { \prime } ) } { | { \bf x } - { \bf x } ^ { \prime } | } + \frac { 1 } { 2 c ^ { 2 } } G \frac { \partial ^ { 2 } } { \partial t ^ { 2 } } \int d ^ { 3 } x ^ { \prime } \sigma ( t , { \bf x } ^ { \prime } ) | { \bf x } - { \bf x } ^ { \prime } | } } \\ { { \displaystyle w ^ { i } ( t , { \bf x } ) = G \int d ^ { 3 } x ^ { \prime } \frac { \sigma ^ { i } ( t , { \bf x } ^ { \prime } ) } { | { \bf x } - { \bf x } ^ { \prime } | } . } } \end{array}
$$

Here, $\sigma$ and $\sigma ^ { i }$ are the gravitational mass and current densities, respectively.

3. writing the geocentric metric tensor $G _ { \alpha \beta }$ with geocentric coordinates $( T , \mathbf { X } )$ ( $T =$ Geocentric Coordinate Time $( T C G )$ ) in the same form as the barycentric one but with potentials $W ( T , \mathbf { X } )$ and $W ^ { a } ( T , { \bf X } )$ ; these geocentric potentials should be split into two parts — potentials $W _ { E }$ and $W _ { E } ^ { a }$ arising from the gravitational action of the Earth and external parts $W _ { \mathrm { e x t } }$ and $W _ { \mathrm { e x t } } ^ { a }$ due to tidal and inertial effects; the external parts of the metric potentials are assumed to vanish at the geocenter and admit an expansion into positive powers of $\mathbf { X }$ ,

explicitly,

$$
\begin{array} { l } { \displaystyle { G _ { 0 0 } = - 1 + \frac { 2 W } { c ^ { 2 } } - \frac { 2 W ^ { 2 } } { c ^ { 4 } } , } } \\ { \displaystyle { G _ { 0 a } = - \frac { 4 } { c ^ { 3 } } W ^ { a } , } } \\ { \displaystyle { G _ { a b } = \delta _ { a b } \left( 1 + \frac { 2 } { c ^ { 2 } } W \right) . } } \end{array}
$$

The potentials $W$ and $W ^ { a }$ should be split according to

$$
\begin{array} { r } { W ( T , { \mathbf X } ) = W _ { E } ( T , { \mathbf X } ) + W _ { \mathrm { e x t } } ( T , { \mathbf X } ) , } \\ { W ^ { a } ( T , { \mathbf X } ) = W _ { E } ^ { a } ( T , { \mathbf X } ) + W _ { \mathrm { e x t } } ^ { a } ( T , { \mathbf X } ) . } \end{array}
$$

The Earth’s potentials $W _ { E }$ and $W _ { E } ^ { a }$ are defined in the same way as $w$ and $w ^ { a }$ but with quantities calculated in the GCRS with integrals taken over the whole Earth.

4. using, if accuracy requires, the full post-Newtonian coordinate transformation between the BCRS and the GCRS as induced by the form of the corresponding metric tensors,

explicitly, for the kinematically non-rotating GCRS ( $T = T C G$ , $t = T C B$ , $r _ { E } ^ { i } \equiv x ^ { i } - x _ { E } ^ { i } ( t )$ and a summation from 1 to 3 over equal indices is implied),

$$
\begin{array} { l } { { \displaystyle T = t - \frac { 1 } { c ^ { 2 } } \bigg [ A ( t ) + v _ { E } ^ { i } r _ { E } ^ { i } \bigg ] + \frac { 1 } { c ^ { 4 } } \bigg [ B ( t ) + B ^ { i } ( t ) r _ { E } ^ { i } + B ^ { i j } ( t ) r _ { E } ^ { i } r _ { E } ^ { j } + C ( t , { \bf x } ) \bigg ] + { \cal O } ( c ^ { - 5 } ) , } } \\ { { \displaystyle Y ^ { a } = \delta _ { a i } \bigg [ r _ { E } ^ { i } + \frac { 1 } { c ^ { 2 } } \bigg ( \frac { 1 } { 2 } v _ { E } ^ { i } v _ { E } ^ { j } r _ { E } ^ { j } + w _ { \mathrm { e x t } } ( { \bf x _ { E } } ) r _ { E } ^ { i } + r _ { E } ^ { i } a _ { E } ^ { j } r _ { E } ^ { j } - \frac { 1 } { 2 } a _ { E } ^ { i } r _ { E } ^ { 2 } \bigg ) \bigg ] + { \cal O } ( c ^ { - 4 } ) , } } \end{array}
$$

where

$$
\begin{array} { l } { { \displaystyle \frac { d } { d t } A ( t ) = \frac { 1 } { 2 } v _ { E } ^ { 2 } + w _ { \mathrm { e x t } } ( { \bf x _ { E } } ) , } } \\ { { \displaystyle \frac { d } { d t } B ( t ) = - \frac { 1 } { 8 } v _ { E } ^ { 4 } - \frac { 3 } { 2 } v _ { E } ^ { 2 } w _ { \mathrm { e x t } } ( { \bf x _ { E } } ) + 4 v _ { E } ^ { i } w _ { \mathrm { e x t } } ^ { i } ( { \bf x _ { E } } ) + \frac { 1 } { 2 } w _ { \mathrm { e x t } } ^ { 2 } ( { \bf x _ { E } } ) , } } \\ { { \displaystyle B ^ { i } ( t ) = - \frac { 1 } { 2 } v _ { E } ^ { 2 } v _ { E } ^ { i } + 4 w _ { \mathrm { e x t } } ^ { i } ( { \bf x _ { E } } ) - 3 v _ { E } ^ { i } w _ { \mathrm { e x t } } ( { \bf x _ { E } } ) , } } \\ { { \displaystyle B ^ { i j } ( t ) = - v _ { E } ^ { i } \delta _ { a j } Q ^ { a } + 2 \frac { \partial } { \partial x ^ { j } } w _ { \mathrm { e x t } } ^ { i } ( { \bf x _ { E } } ) - v _ { E } ^ { i } \frac { \partial } { \partial x ^ { j } } w _ { \mathrm { e x t } } ( { \bf x _ { E } } ) + \frac { 1 } { 2 } \delta ^ { i j } \dot { w } _ { \mathrm { e x t } } ( { \bf x _ { E } } ) , } } \\ { { \displaystyle C ( t , { \bf x } ) = - \frac { 1 } { 1 0 } r _ { E } ^ { 2 } ( \dot { a } _ { E } ^ { i } r _ { E } ^ { i } ) . } } \end{array}
$$

Here $x _ { E } ^ { i }$ , $v _ { E } ^ { i }$ , and $a _ { E } ^ { i }$ are the barycentric position, velocity and acceleration vectors of the Earth, the dot stands for the total derivative with respect to $t$ , and

$$
Q ^ { a } = \delta _ { a i } \left[ \frac { \partial } { \partial x _ { i } } w _ { \mathrm { e x t } } ( \mathbf { x _ { E } } ) - a _ { E } ^ { i } \right] .
$$

The external potentials, $w _ { \mathrm { e x t } }$ and $w _ { \mathrm { e x t } } ^ { i }$ , are given by

$$
w _ { \mathrm { e x t } } = \sum _ { A \neq E } w _ { A } , \quad w _ { \mathrm { e x t } } ^ { i } = \sum _ { A \neq E } w _ { A } ^ { i } ,
$$

where $E$ stands for the Earth and $w _ { A }$ and $w _ { A } ^ { i }$ are determined by the expressions for $w$ and $w ^ { i }$ with integrals taken over body $A$ only.

# Notes

It is to be understood that these expressions for w and $w ^ { i }$ give $g _ { 0 0 }$ correct up to $\mathcal { O } ( c ^ { - 5 } )$ , $g _ { 0 i }$ up to   
$\mathcal { O } ( c ^ { - 5 } )$ , and $g _ { i j }$ up to $\mathcal { O } ( c ^ { - 4 } )$ . The densities $\sigma$ and $\sigma ^ { i }$ are determined by the components of the   
energy momentum tensor of the matter composing the solar system bodies as given in the references.   
Accuracies for $G _ { \alpha \beta }$ in terms of $c ^ { - n }$ correspond to those of . $g _ { \mu \nu }$

The external potentials $W _ { \mathrm { e x t } }$ and $W _ { \mathrm { e x t } } ^ { a }$ can be written in the form

$$
\begin{array} { r } { W _ { \mathrm { e x t } } = W _ { \mathrm { t i d a l } } + W _ { \mathrm { i n e r } } , } \\ { W _ { \mathrm { e x t } } ^ { a } = W _ { \mathrm { t i d a l } } ^ { a } + W _ { \mathrm { i n e r } } ^ { a } . } \end{array}
$$

$W _ { \mathrm { t i d a l } }$ generalizes the Newtonian expression for the tidal potential. Post-Newtonian expressions for $W _ { \mathrm { t i d a l } }$ and $W _ { \mathrm { t i d a l } } ^ { a }$ can be found in the references. The potentials $W _ { \mathrm { i n e r } }$ , $W _ { \mathrm { i n e r } } ^ { a }$ are inertial contributions that are linear in $X ^ { a }$ . The former is determined mainly by the coupling of the Earth’s nonsphericity to the external potential. In the kinematically non-rotating Geocentric Celestial Reference System, $W _ { \mathrm { i n e r } } ^ { a }$ describes the Coriolis force induced mainly by geodesic precession.

Finally, the local gravitational potentials $W _ { E }$ and $W _ { E } ^ { a }$ of the Earth are related to the barycentric gravitational potentials $w _ { E }$ and $w _ { E } ^ { i }$ by

$$
\begin{array} { l } { { \displaystyle W _ { E } ( T , { \bf X } ) = w _ { E } ( t , { \bf x } ) \left( 1 + \frac { 2 } { c ^ { 2 } } v _ { E } ^ { 2 } \right) - \frac { 4 } { c ^ { 2 } } v _ { E } ^ { i } w _ { E } ^ { i } ( t , { \bf x } ) + { \cal O } ( c ^ { - 4 } ) , } } \\ { { \displaystyle W _ { E } ^ { a } ( T , { \bf X } ) = \delta _ { a i } ( w _ { E } ^ { i } ( t , { \bf x } ) - v _ { E } ^ { i } w _ { E } ( t , { \bf x } ) ) + { \cal O } ( c ^ { - 2 } ) . } } \end{array}
$$

Brumberg, V.A., Kopeikin, S.M., 1989, Nuovo Cimento, B 103, 63.   
Brumberg, V.A., 1991, Essential Relativistic Celestial Mechanics, Hilger, Bristol.   
Damour, T., Soffel, M., Xu, C., Phys. Rev. D, 43, 3273 (1991); 45, 1017 (1992); 47, 3124 (1993);   
49, 618 (1994).   
Klioner, S. A., Voinov, A.V., 1993, Phys Rev. D, 48, 1451.   
Kopeikin, S.M., 1988, Celest. Mech., 44, 87.

# Resolution B1.4: Post-Newtonian Potential Coefficients

The XXVIth International Astronomical Union General Assembly,

# Considering

1. that for many applications in the fields of celestial mechanics and astrometry a suitable parametrization of the metric potentials (or multipole moments) outside the massive solarsystem bodies in the form of expansions in terms of potential coefficients are extremely useful, and

2. that physically meaningful post-Newtonian potential coefficients can be derived from the literature,

# Recommends

1. expansion of the post-Newtonian potential of the Earth in the Geocentric Celestial Reference System (GCRS) outside the Earth in the form

$$
{ \mathrm { \mathrm { \Sigma } } } _ { E } ( T , \mathbf { X } ) = { \frac { G M _ { E } } { R } } \left[ 1 + \sum _ { l = 2 } ^ { \infty } \sum _ { m = 0 } ^ { + l } \left( { \frac { R _ { E } } { R } } \right) ^ { l } P _ { l m } ( \cos \theta ) ( C _ { l m } ^ { E } ( T ) \cos m \phi + S _ { l m } ^ { E } ( T ) \sin m \phi ) \right] .
$$

Here $C _ { l m } ^ { E }$ and $S _ { l m } ^ { E }$ are, to sufficient accuracy, equivalent to the post-Newtonian multipole moments introduced by Damour et al. (Damour et al., Phys. Rev. D, 43, 3273, 1991). $\theta$ and $\phi$ are the polar angles corresponding to the spatial coordinates $\mathrm { X } ^ { a }$ of the GCRS and $R = | X |$ , and

2. expression of the vector potential outside the Earth, leading to the well-known Lense-Thirring effect, in terms of the Earth’s total angular momentum vector $\mathbf { S _ { E } }$ in the form

$$
{ \cal W } _ { E } ^ { a } ( T , { \bf X } ) = - \frac { G } { 2 } \frac { ( { \bf X } \times { \bf S _ { E } } ) ^ { a } } { R ^ { 3 } } .
$$

# Resolution B1.5: Extended relativistic framework for time transformations and realization of coordinate times in the solar system

The XXVIth International Astronomical Union General Assembly,

# Considering

1. that the Resolution A4 of the XXIst General Assembly(1991) has defined systems of spacetime coordinates for the solar system (Barycentric Reference System) and for the Earth (Geocentric Reference System), within the framework of General Relativity,

2. that Resolution B1.3 entitled “Definition of Barycentric Celestial Reference System and Geocentric Celestial Reference System” has renamed these systems the Barycentric Celestial Reference System (BCRS) and the Geocentric Celestial Reference System (GCRS), respectively, and has specified a general framework for expressing their metric tensor and defining coordinate transformations at the first post-Newtonian level,

3. that, based on the anticipated performance of atomic clocks, future time and frequency measurements will require practical application of this framework in the BCRS, and

4. that theoretical work requiring such expansions has already been performed,

# Recommends

that for applications that concern time transformations and realization of coordinate times within the solar system, Resolution B1.3 be applied as follows:

1. the metric tensor be expressed as

$$
\begin{array} { l } { \displaystyle g _ { 0 0 } = - \bigg ( 1 - \frac { 2 } { c ^ { 2 } } \big ( w _ { 0 } ( t , { \mathbf x } ) + w _ { L } ( t , { \mathbf x } ) \big ) + \frac { 2 } { c ^ { 4 } } \big ( w _ { 0 } ^ { 2 } ( t , { \mathbf x } ) + \Delta ( t , { \mathbf x } ) \big ) \bigg ) } \\ { \displaystyle g _ { 0 i } = - \frac { 4 } { c ^ { 3 } } w ^ { i } ( t , { \mathbf x } ) , } \\ { \displaystyle g _ { i j } = \bigg ( 1 + \frac { 2 w _ { 0 } ( t , { \mathbf x } ) } { c ^ { 2 } } \bigg ) \delta _ { i j } , } \end{array}
$$

where ( $t \equiv$ Barycentric Coordinate Time $( T C B ) , { \bf x } )$ are the barycentric coordinates, $w _ { 0 } =$ $G \sum _ { A } M _ { A } / r _ { A }$ with the summation carried out over all solar system bodies $A$ , $\mathbf { r } _ { A } = \mathbf { x } - \mathbf { x } _ { A } , \mathbf { x } _ { A }$ are the coordinates of the center of mass of body $A$ , $r _ { A } = | \mathbf { r } _ { \mathbf { A } } |$ , and where $w _ { L }$ contains the expansion in terms of multipole moments [see their definition in the Resolution B1.4 entitled “Post-Newtonian Potential Coefficients”] required for each body. The vector potential $\begin{array} { r } { w ^ { i } ( t , \mathbf { x } ) = \sum _ { A } w _ { A } ^ { i } ( t , \mathbf { x } ) } \end{array}$ and the function $\begin{array} { r } { \Delta ( t , \mathbf { x } ) = \sum _ { A } \Delta _ { A } ( t , \mathbf { x } ) } \end{array}$ are given in note 2.

2. the relation between $T C B$ and Geocentric Coordinate Time $( T C G )$ can be expressed to sufficient accuracy by

$$
\begin{array} { l } { \displaystyle { { \bf \Pi } ^ { \prime } - T C G = c ^ { - 2 } \left[ \int _ { t _ { 0 } } ^ { t } \left( \frac { v _ { E } ^ { 2 } } { 2 } + w _ { 0 , \mathrm { e x t } } ( { \bf x } _ { E } ) \right) d t + v _ { E } ^ { i } r _ { E } ^ { i } \right] } } \\ { \displaystyle \left[ \int _ { t _ { 0 } } ^ { t } \left( - \frac { 1 } { 8 } v _ { E } ^ { 4 } - \frac { 3 } { 2 } v _ { E } ^ { 2 } w _ { 0 , \mathrm { e x t } } ( { \bf x } _ { E } ) + 4 v _ { E } ^ { i } w _ { \mathrm { e x t } } ^ { i } ( { \bf x } _ { E } ) + \frac { 1 } { 2 } w _ { 0 , \mathrm { e x t } } ^ { 2 } ( { \bf x } _ { E } ) \right) d t - \left( 3 w _ { 0 , \mathrm { e x t } } ( { \bf x } _ { E } ) + \frac { v _ { E } ^ { 2 } } { 2 } w _ { 0 , \mathrm { e x t } } ( { \bf x } _ { E } ) \right) d t \right] . } \end{array}
$$

where $v _ { E }$ is the barycentric velocity of the Earth and where the index ext refers to summation over all bodies except the Earth.

# Notes

1. This formulation will provide an uncertainty not larger than $5 \times 1 0 ^ { - 1 8 }$ in rate and, for quasiperiodic terms, not larger than $5 \times 1 0 ^ { - 1 8 }$ in rate amplitude and 0.2 ps in phase amplitude, for locations farther than a few solar radii from the Sun. The same uncertainty also applies to the transformation between T CB and T CG for locations within 50 000 km of the Earth. Uncertainties in the values of astronomical quantities may induce larger errors in the formulas.

2. Within the above mentioned uncertainties, it is sufficient to express the vector potential $w _ { A } ^ { i } ( t , { \bf x } )$ of body $A$ as

$$
w _ { A } ^ { i } ( t , \mathbf { x } ) = G \left[ \frac { - ( \mathbf { r } _ { A } \times \mathbf { S } _ { A } ) ^ { i } } { 2 r _ { A } ^ { 3 } } + \frac { M _ { A } v _ { A } ^ { i } } { r _ { A } } \right] ,
$$

where $\mathbf { S } _ { A }$ is the total angular momentum of body $A$ and $v _ { A } ^ { i }$ is the barycentric coordinate velocity of body $A$ . As for the function $\Delta _ { A } ( t , { \bf x } )$ it is sufficient to express it as

$$
\boldsymbol { \beth } _ { \boldsymbol { A } } ( t , \mathbf { x } ) = \frac { G M _ { \boldsymbol { A } } } { r _ { A } } \left[ - 2 v _ { a } ^ { 2 } + \sum _ { B \neq A } \frac { G M _ { B } } { r _ { B A } } + \frac { 1 } { 2 } \left( \frac { ( r _ { A } ^ { k } v _ { A } ^ { k } ) ^ { 2 } } { r _ { A } ^ { 2 } } + r _ { A } ^ { k } a _ { A } ^ { k } \right) \right] + \frac { 2 G v _ { A } ^ { k } ( \mathbf { r } _ { A } \times \mathbf { S } _ { A } ) ^ { k } } { r _ { A } ^ { 3 } } ,
$$

where $r _ { B A } = \left| \mathbf { x } _ { B } - \mathbf { x } _ { A } \right|$ and $a _ { A } ^ { k }$ is the barycentric coordinate acceleration of body $A$ . In these formulas, the terms in $\mathbf { S } _ { A }$ are needed only for Jupiter $^ { \prime } S \approx 6 . 9 \times 1 0 ^ { 3 8 } m ^ { 2 } s ^ { - 1 } k g )$ and Saturn ( $S \approx$ $1 . 4 \times 1 0 ^ { 3 8 } \ : m ^ { 2 } s ^ { - 1 } k g )$ , in the immediate vicinity of these planets.

3. Because the present recommendation provides an extension of the IAU 1991 recommendations valid at the full first post-Newtonian level, the constants $L _ { C }$ and $L _ { B }$ that were introduced in the IAU 1991 recommendations should be defined $a s < T C G / T C B > = 1 - L _ { C }$ and $< T T / T C B > =$ $1 - L _ { B }$ , where T T refers to Terrestrial Time and $< >$ refers to a sufficiently long average taken at the geocenter. The most recent estimate of $L _ { C }$ is (Irwin, $A$ . and Fukushima, $T .$ , 1999, Astron. Astroph., 348, 642–652)

$$
L _ { C } = 1 . 4 8 0 8 2 6 8 6 7 4 1 \times 1 0 ^ { - 8 } \pm 2 \times 1 0 ^ { - 1 7 } .
$$

From Resolution B1.9 on “Redefinition of Terrestrial Time $T T ^ { s }$ , one infers $L _ { B } = 1 . 5 5 0 5 1 9 7 6 7 7 2$ $\times 1 0 ^ { - 8 } \pm 2 \times 1 0 ^ { - 1 7 }$ by using the relation $1 - L _ { B } = ( 1 - L _ { C } ) ( 1 - L _ { G } )$ . $L _ { G }$ is defined in Resolution B1.9.

Because no unambiguous definition may be provided for $L _ { B }$ and $L _ { C }$ , these constants should not be used in formulating time transformations when it would require knowing their value with an uncertainty of order $1 \times 1 0 ^ { - 1 6 }$ or less.

4. If $T C B - T C G$ is computed using planetary ephemerides which are expressed in terms of a time argument (noted $T _ { \mathrm { e p h } }$ ) which is close to Barycentric Dynamical Time $( T D B )$ , rather than in terms of $T C B$ , the first integral in Recommendation $\mathcal { Z }$ above may be computed as

$$
\int _ { t _ { 0 } } ^ { t } \biggl ( \frac { v _ { E } ^ { 2 } } { 2 } + w _ { 0 , \mathrm { e x t } } ( \mathbf { x } _ { E } ) \biggr ) d t = \left[ \int _ { T _ { \mathrm { e p h } _ { 0 } } } ^ { T _ { \mathrm { e p h } } } \biggl ( \frac { v _ { E } ^ { 2 } } { 2 } + w _ { 0 , \mathrm { e x t } } ( \mathbf { x } _ { E } ) \biggr ) d t \right] / ( 1 - L _ { B } ) .
$$

# Resolution B1.9: Re-definition of Terrestrial Time T T

The XXVIth International Astronomical Union General Assembly,

# Considering

1. that IAU Resolution A4 (1991) has defined Terrestrial Time ( $' L " L "$ ) in its Recommendation 4, and

2. that the intricacy and temporal changes inherent to the definition and realization of the geoid are a source of uncertainty in the definition and realization of $T T$ , which may become, in the near future, the dominant source of uncertainty in realizing $T Y ^ { \prime }$ from atomic clocks,

# Recommends

that $' L " L "$ be a time scale differing from $T C G$ by a constant rate: $d T T / d T C G = 1 - L _ { G }$ , where $L _ { G } = 6 . 9 6 9 2 9 0 1 3 4 \times 1 0 ^ { - 1 0 }$ is a defining constant,

# Note

$L _ { G }$ was defined by the IAU Resolution A4 (1991) in its Recommendation 4 as equal to $U _ { G } / c ^ { 2 }$ where $U _ { G }$ is the geopotential at the geoid. $L _ { G }$ is now used as a defining constant.

# B. Comparison of the IAU metric with versions given in the literature

In this Appendix we will compare the metric (8) with well-known results from the literature. Only for this purpose we will consider the material composing the various bodies of the system to behave like an ideal fluid (for the IAU 2000 Resolutions this is not assumed). In the ideal fluid case the energy-momentum tensor can be written in the form

$$
\begin{array} { l } { { \displaystyle T ^ { 0 0 } = \rho c ^ { 2 } \left( 1 + \frac { 1 } { c ^ { 2 } } \left[ \Pi + { \bf v } ^ { 2 } + 2 U \right] \right) + \mathcal { O } ( c ^ { - 2 } ) } , } \\ { { \displaystyle T ^ { 0 i } = \rho c v ^ { i } + \mathcal { O } ( c ^ { - 1 } ) , } } \\ { { \displaystyle T ^ { i j } = \rho v ^ { i } v ^ { j } + p \delta _ { i j } + \mathcal { O } ( c ^ { - 2 } ) . } } \end{array}
$$

Here, $\rho$ denotes the rest-mass density, $p$ is the pressure, $\Pi$ is the specific internal energy (e.g., Will 1993), $v ^ { \imath } ( t , { \bf x } )$ is the velocity of the corresponding material element and

$$
U ( t , { \bf x } ) \equiv G \int \frac { \rho ( t , { \bf x } ^ { \prime } ) } { | { \bf x } - { \bf x } ^ { \prime } | } d ^ { 3 } x ^ { \prime } .
$$

From (12) and (B1) we derive

$$
\begin{array} { l } { { \displaystyle \sigma = \rho \left( 1 + \frac { 1 } { c ^ { 2 } } \left[ \Pi + 2 { \bf v } ^ { 2 } + 2 { \cal U } \right] \right) + 3 \frac { p } { c ^ { 2 } } + \mathcal { O } ( c ^ { - 4 } ) , } } \\ { { \displaystyle \sigma ^ { i } = \rho v ^ { i } + \mathcal { O } ( c ^ { - 2 } ) . } } \end{array}
$$

Introducing the metric potentials

$$
\begin{array} { l } { { \Phi _ { 1 } \equiv \displaystyle \int \frac { \rho ^ { \prime } v ^ { \prime 2 } } { | { \bf x } - { \bf x } ^ { \prime } | } d ^ { 3 } x ^ { \prime } , \qquad \Phi _ { 2 } \equiv \displaystyle \int \frac { \rho ^ { \prime } U ^ { \prime } } { | { \bf x } - { \bf x } ^ { \prime } | } d ^ { 3 } x ^ { \prime } , } } \\ { { \Phi _ { 3 } \equiv \displaystyle \int \frac { \rho ^ { \prime } \Pi ^ { \prime } } { | { \bf x } - { \bf x } ^ { \prime } | } d ^ { 3 } x ^ { \prime } , \qquad \Phi _ { 4 } \equiv \displaystyle \int \frac { p ^ { \prime } } { | { \bf x } - { \bf x } ^ { \prime } | } d ^ { 3 } x ^ { \prime } , } } \end{array}
$$

we obtain from (14) and (15)

$$
\begin{array} { l } { { w { = } U + 2 \Phi _ { 1 } + 2 \Phi _ { 2 } + \Phi _ { 3 } + 3 \Phi _ { 4 } - \displaystyle \frac { 1 } { 2 c ^ { 2 } } \chi _ { , t t } + { \cal O } ( c ^ { - 4 } ) , } } \\ { { w ^ { i } { = } V _ { i } + { \cal O } ( c ^ { - 2 } ) , } } \end{array}
$$

with

$$
V _ { i } \equiv \int \frac { \rho ^ { \prime } v _ { i } ^ { \prime } } { | { \bf x } - { \bf x } ^ { \prime } | } d ^ { 3 } x ^ { \prime } , \qquad \chi \equiv - G \int \rho ^ { \prime } | { \bf x } - { \bf x } ^ { \prime } | d ^ { 3 } x ^ { \prime } ,
$$

and the comma denotes partial differentiation as in

$$
\chi _ { , t t } \equiv \frac { \partial ^ { 2 } \chi } { \partial t ^ { 2 } } .
$$

The post-Newtonian metric (in harmonic gauge) can then be written as

$$
\begin{array} { l } { { g _ { 0 0 } = - 1 + \displaystyle \frac { 1 } { c ^ { 2 } } \left[ 2 U + 4 \Phi _ { 1 } + 4 \Phi _ { 2 } + 2 \Phi _ { 3 } + 6 \Phi _ { 4 } \right] - \displaystyle \frac { 2 } { c ^ { 4 } } U ^ { 2 } + \displaystyle \frac { 1 } { c ^ { 4 } } \chi _ { , t t } , } } \\ { { g _ { 0 i } = - \displaystyle \frac { 4 } { c ^ { 3 } } V _ { i } , } } \\ { { g _ { i j } = \delta _ { i j } \left( 1 + \displaystyle \frac { 2 U } { c ^ { 2 } } \right) . } } \end{array}
$$

To compare, e.g., with the metric in (Will 1993) we transform from harmonic coordinates, used in the present paper and recommended by the IAU, to standard post-Newtonian (SPN) coordinates used by several authors including Will. This is achieved by a gauge transformation of the form (e.g., Eq. (3.12) of Damour, Soffel & Xu (1991)),

$$
w _ { \mathrm { S P N } } = w - \frac { 1 } { c ^ { 2 } } \lambda _ { , t } , \qquad w _ { \mathrm { S P N } } ^ { i } = w ^ { i } + \frac { 1 } { 4 } \lambda _ { , i }
$$

with

$$
\lambda = - \frac { 1 } { 2 } \chi _ { , t } .
$$

This implies that the $\chi$ -term disappears from $w$ and hence from $g _ { 0 0 }$ when standard post-Newtonian coordinates are employed, but the $g _ { 0 i }$ term gets affected by this transformation. Using the relation

$$
\chi _ { , t i } = V _ { i } - W _ { i }
$$

with

$$
W _ { i } \equiv \int \frac { \rho ^ { \prime } \left[ \mathbf { v } ^ { \prime } \cdot \left( \mathbf { x } - \mathbf { x } ^ { \prime } \right) \right] \left( x ^ { i } - x ^ { \prime i } \right) } { | \mathbf { x } - \mathbf { x } ^ { \prime } | ^ { 3 } } d ^ { 3 } x ^ { \prime }
$$

one verifies that the metric induced by the potentials (14) and (15) agrees in General Relativity with (5.28) of (Will 1993).

# REFERENCES

Bize, S., Sortais, Y., Santos, M.S., Mandache, C., Clairon, A., & Salomon, C. 1999, Europhys. Lett., 45, 558   
Blanchet, L., & Damour, T. 1989, Ann. Inst. H. Poincar´e, 50, 377   
Bois, E., & Vokrouhlick´y, D. 1995, A&A, 300, 559   
Brumberg, V.A. 1991, Essential Relativistic Celestial Mechanics (Bristol: A. Hilder)   
Brumberg, V.A., & Kopeikin, S.M. 1989, in Reference Frames, ed. J. Kovalevsky et al. (Dordrecht: Kluwer), 115   
Brumberg, V.A., Bretagnon, P., & Francou, G. 1992, in Les Journ´ees 1991, ed. N. Capitaine (Paris: Observatoire de Paris), 141   
Burˇsa, M. 1995, Report of the IAG SC3 Fundamental Constants, XXI IAG General Assembly   
Carter, W., Robertson, D., & MacKay, J. 1985, JGR, 90, 4577   
Damour, T., Soffel, M., & Xu, C. 1991, Phys. Rev. D, 43, 3273   
Damour, T., Soffel, M., & Xu, C. 1992, Phys. Rev. D, 45, 1017   
Damour, T., Soffel, M., & Xu, C. 1993, Phys. Rev. D, 47, 3124   
Damour, T., Soffel, M., & Xu, C. 1994, Phys. Rev. D, 49, 618   
Eubanks T.M., Matsakis D.N., Martin J.O., Archinal B.A., McCarthy D.D., Klioner S.A., Shapiro S., & Shapiro I.I. 1997, Advances in Solar System Tests of Gravity, in Proceedings of The Joint APS/AAPT 1997 Meeting, 18-21 April 1997, Washington D.C. (available at http://flux.aps.org/meetings/YR97/BAPSAPR97/abs/S1280005.html)   
Fock, V.A. 1959, The Theory of Space, Time and Gravitation (Oxford: Pergamon Press)   
Froeschl´e, M., Mignard, F., & Arenou, F. 1997, Determination of the PPN Parameter $\gamma$ with the Hipparcos Data, in Proceedings of the ESA Symposium “Hipparcos - Venice 97”, 13-16 May 1997, Venus, Italy, ESA SP-402, 49   
Fukushima, T. 1991, A&A, 244, L11   
Fukushima, T. 1995, A&A, 294, 895   
Groten, E. 1999, Report of the IAG SC3 Fundamental Constants, XXII IAG General Assembly   
IAU 2001, Information Bulletin, 88 (errata in IAU Information Bulletin, 89)   
IERS 1992, IERS Standards, International Earth Rotation Service Technical Note 13, ed. D.D. Mc-Carthy (Paris: Observatoire de Paris)   
IERS 1996, IERS Conventions, International Earth Rotation Service Technical Note 21, ed. D.D. McCarthy (Paris: Observatoire de Paris)   
IERS 2003, IERS Conventions 2000, available at http://maia.usno.navy.mil/conv2000.html, to be published   
Irwin, A., & Fukushima, T. 1999, A&A, 348, 642   
Klioner, S.A. 1992, Celest. Mech. Dyn. Astr., 53, 81   
Klioner, S.A. 2003, AJ, 125, 1580   
Klioner, S.A., & Soffel, M. 1998, A&A, 334, 1123   
Klioner, S.A., & Soffel, M. 2000, Phys. Rev. D, 62, ID 024019   
Klioner, S.A., Soffel, M., Xu, Ch., Wu, X. (2003) Earth’s rotation in the framework of general relativity: rigid multipole moments. in Proceedings of Les Journ´ees’2001, ed. N. Capitaine, in press   
Klioner, S.A., & Voinov, A.V. 1993, Phys. Rev. D, 48, 1451   
Kopeikin, S.M. 1988, Celest. Mech. Dyn. Astr., 44, 87   
Kopeikin, S.M. 1990, Soviet Astronomy, 34, 5   
Kopeikin, S.M. 1991, Manuscripta Geodetica, 16, 301   
Lebach, D.E., Corey, B.E., Shapiro. I.I., Ratner, M.I., Webber, J.C., Rogers, A.E.E., Davis, J.L., & Herring, T.A. 1995, Phys. Rev. Lett., 75, 1439   
Lemonde, P. et al. 2001, in Frequency Measurement and Control, ed. A.N. Luiten (Berlin: Springer)   
Lindegren, L., & Dravins, D. 2003, A&A, in press   
Mashhoon, B. 1985, Found. Phys., 15, 497   
Misner, C., Thorne, K., & Wheeler, J.A. 1973, Gravitation (San Francisco: Freeman)   
Newhall, X.X., Standish, E.M., & Williams, J.G. 1983, A&A, 125, 150   
Petit, G., & Wolf, P. 1994, A&A, 286, 971   
Rickman, H. 2001, Reports on Astronomy, Trans. IAU, XXIV B   
Robertson, D., & Carter, W. 1984, Nature, 310, 572   
Soffel, M. 1989, Relativity in Astrometry, Celestial Mechanics and Geodesy (Berlin: Springer-Verlag)   
Soffel, M., Ruder, H., & Schneider, M. 1986, A&A, 157, 357   
Standish, M. 1998, A&A, 336, 381   
Weinberg, S. 1972, Gravitation and Cosmology: Principles and Applications of the General Theory of Relativity (New York: J. Wiley & Sons)   
Weyers, S., H¨ubner, U., Schr¨oder, R., Tamm, C., & Bauch, A. 2001, Metrologia, 38(4), 343   
Will, C.M. 1993, Theory and Experiment in Gravitational Physics. (Cambridge: Cambridge University Press)   
Wolf, P., & Petit, G. 1995, A&A, 304, 654
