Table 4.1 Angular units in position astronomy with an illustration by apparent diameter of a 1 euro coin. The last column indicates the epoch at which the given accuracy was achieved-  

<table><tr><td>Angle</td><td>Radians</td><td>1 euro coin at distance</td><td>Epoch</td></tr><tr><td>1 degree</td><td>~10-2</td><td>1m</td><td>Hipparchos</td></tr><tr><td>1</td><td>~2×10-4</td><td>100m</td><td>Tycho Brahe</td></tr><tr><td>1&quot;</td><td>~10-5</td><td>4km</td><td>1900</td></tr><tr><td>1 mas</td><td>~1018</td><td>4000km</td><td>Hipparcos</td></tr><tr><td>10 μas</td><td>~10-10</td><td>4 × 105 km (on the Moon)</td><td>Gaia</td></tr><tr><td>1 μas</td><td>~10-11</td><td>1 hair at 4 000 km</td><td>SIM</td></tr></table>

relativistic formulation of aberration for astrometry to arcsec accuracy, but it is essential to do so for accuracies of millisecond (mas) order. Typical angular values for astronomical positions are given in Table 4.1, with an estimate of the epoch at which this accuracy was (or will be) attained.

# 4.1 Spatial Reference Systems

# 4.1.1 Definitions of Spatial Frames

The determination of coordinates for astronomical events is closely connected to the gathering of information carried by photons. Fixing the position of celestial objects, such as planets, stars, galaxies, quasars, and so on, is an essential step towards identifying and cataloguing them, so that they can be found for further observation, or used for statistical studies on the distribution of matter in the Universe. But far more than being a mere list, this information about the positions and motions of objects is as important scientifically as information about their specific physical properties.

Throughout this chapter, space will be referred to an origin $o$ and three fundamental directions $O x _ { 1 } , O x _ { 2 } , O x _ { 3 }$ defined by unit orthogonal vectors $\boldsymbol { e } _ { 1 } , \boldsymbol { e } _ { 2 } , \boldsymbol { e } _ { 3 }$ . The triad will be taken to be right-handed, that is $\pmb { e } _ { 3 } = \pmb { e } _ { 1 } \times \pmb { e } _ { 2 }$ (vector product). A point $M$ is fixed either by its Cartesian coordinates $( x _ { 1 } , x _ { 2 } , x _ { 3 } )$ , or by its spherical coordinates $( r , \theta , \phi )$ with

$$
\begin{array} { l } { x _ { 1 } = r \cos \phi \cos \theta , } \\ { x _ { 2 } = r \sin \phi \cos \theta , } \\ { x _ { 3 } = r \sin \theta , } \end{array}
$$

where $r > 0$ , $0 \leq \phi < 2 \pi$ , $- \pi / 2 \leq \theta \leq \pi / 2$ . We shall call $\phi$ the longitude and $\theta$   the latitude (see Fig. 4.2), but it should be noted that the definition of latitude as the angle above the equator is common usage in astronomy, whereas physicists prefer to use the colatitude measured from the polar direction. This should be borne in mind when using tangent frames that are not oriented in the same way.

![](images/4badd87d02736a8bbebee5559a67bf7448005e3f0ef990b7521d434a4c18a29b.jpg)  
Fig. 4.2 Reference triad and spherical coordinates, with astronomers’ conventions

The definition and the practical application of such a frame require a choice of fundamental plane normal to $e _ { 3 }$ , and some practical realisation of these directions in the sky.

The Cartesian coordinates $( x _ { 1 } , x _ { 2 } , x _ { 3 } )$ of the point $M$ can be calculated using the above formulas, given its spherical coordinates $( r , \theta , \phi )$ . Care should be taken over the inverse transformation. Indeed, determination of an angle in $[ 0 , 2 \pi ]$ requires knowledge of both its sine and its cosine, or at least one of the trigonometric lines and the sign of the other. Many disagreements and errors in automated calculations can be traced to the neglect of this rule. But, bearing this in mind, the following formulas allow transformation from the normalised Cartesian components of $^ { o M }$ to its spherical coordinates:

$$
\begin{array} { c } { \theta = \arcsin x _ { 3 } , } \\ { \phi = \operatorname { a n g l e } ( x _ { 1 } , x _ { 2 } ) = \arctan 2 , ( x _ { 2 } , x _ { 1 } ) , } \end{array}
$$

where the function $\alpha = \mathrm { a n g l e } ( x , y ) \iff x = \cos \alpha$ and $y = \sin \alpha$

D ” D DIn order to avoid tests in programs and to use only the function arctan $x$ , which is available in all programming languages, the longitude can be determined more directly by

$$
\tan { \frac { \phi } { 2 } } = { \frac { \sin \phi } { 1 + \cos \phi } } = { \frac { x _ { 2 } } { r \cos \theta + x _ { 1 } } } ,
$$

and

$$
\phi = 2 \arctan \left( \frac { x _ { 2 } } { r \cos \theta + x _ { 1 } } \right) ,
$$

which automatically gives an angle $\phi$ between $- \pi$ and $+ \pi$ , without any ambiguity as to the quadrant. The angle $\theta$ lies between $- \pi / 2$ and $+ \pi / 2$ and is thus completely  Cdetermined by its sine. These formulas are easily adapted when the position vector is not unit length.

# 4.1.2 Astronomical Reference Frames

# Characteristics of the Reference Frames

In order to study the positions and motions of celestial bodies (planets, satellites, stars, galaxies, etc.), spatial reference frames must be defined and constructed practically. A major part of astronomical activity in the past was devoted to such constructions, and it is only in the last 150 years that the physical study of these bodies has taken an important place in astronomical research. The triads used in astronomy can be distinguished from one another by the features listed in Table 4.2.

The vertical and the celestial pole correspond to ideal physical definitions which we try to realise materially as best as we can from observations, whereas poles by convention are just defined by a set of numbers which allow us to attach them to physical systems. For example, the plane of the solar equator used to fix the positions of sunspots is inclined by definition at an angle of 7.2 degrees to the ecliptic of 1850. The origin in the equatorial plane is determined by the ascending node of the solar equator on the ecliptic at noon on 1/1/1854. The meridian origin makes one sidereal revolution every 25.38 mean solar days. Since the ecliptic plane of 1850 can be linked to the equatorial plane at any date by the theory of the Earth’s motion, the heliographic frame can be defined at any moment by a few numerical constants. The accuracy of the definition is compatible with the accuracy to which the system can be observed: there is no point trying to locate a sunspot, with its uncertain contours, to a greater accuracy than a few seconds of arc.

# The Horizontal Frame

This is the most natural reference frame for recording the positions of celestial bodies and their apparent motion during the diurnal cycle. We consider a triad with origin at the position of the observer. At each point and at any moment, there exists a natural and easily determined direction, namely the local vertical specified by the weight (resultant of the gravitational attraction and the centrifugal force due to the Earth’s rotation). The plane normal to the vertical is the horizon, or horizontal plane. The point on the celestial sphere associated with the ascendant vertical is the zenith, and the opposite point is the nadir. The plane containing the local vertical and the direction of the celestial pole (this plane may well not contain the axis of rotation of the Earth, but we shall ignore this slight difference in what follows) is the local meridian plane, and its intersection with the horizon defines the origin for longitude in the horizontal frame. The intersection of the local meridian plane with the celestial sphere is called the astronomical meridian. This is indeed an astronomical notion and not a geographical one, for the latter would be fixed relative to terrestrial points of given longitude on Earth. The exact shape of the Earth and the complexity of its gravitational field do not enter directly into the definition. Only the notion of local vertical is important, and it can be materialised by means of a plumb line, or by the surface of a liquid at rest, whose plane will be normal to the vertical.

Table 4.2 Standard reference frames for position astronomy   

<table><tr><td>Origin of coordinates</td><td></td></tr><tr><td>Place of observation</td><td>Topocentric frame</td></tr><tr><td>Centre of the Earth Centre of the Sun</td><td>Geocentric frame Heliocentric frame</td></tr><tr><td>A centre of mass</td><td>Barycentric frame</td></tr><tr><td>Choice of fundamental directions</td><td></td></tr><tr><td colspan="2"></td></tr><tr><td>The local vertical</td><td>Horizontal system</td></tr><tr><td>The celestial pole</td><td>Equatorial system</td></tr><tr><td>The normal to the ecliptic</td><td>Ecliptic system</td></tr><tr><td>A pole by convention</td><td></td></tr><tr><td></td><td>Galactic system,heliographic system</td></tr></table>

The two spherical angles determining a direction relative to this triad are the azimuthal angle $A$ and the height $h$ . The azimuthal angle is measured in the horizontal plane using various conventions of orientation, depending on whether the application is in astronomy, geodesy, sea navigation, or space geodesy. There are four possible conventions, depending on the origin (north or south), and the orientation (left- or right-handed). Following common usage in astronomy, we take the south as origin. Astronomers used to measure azimuthal angles in the retrograde direction (so that angles increase for a typical body in its daily motion and for an inhabitant of the northern hemisphere). Today, with the advent of automatic computation and matrix formulas, a right-handed or direct triad orientation is much preferred, so that calculations can be made using rotation operators without the need to be over-concerned with the orientation of the angles. Hence, in the following formulas, azimuthal angles increase from 0 to $9 0 ^ { \circ }$ toward the east. Note, however, that it is not uncommon to find slightly different formulas in works on spherical astronomy, especially in older editions.

In the horizontal system (Fig. 4.3), the unit vector in the direction $^ { o M }$ takes the form

$$
U ( A , h ) = { \left[ \begin{array} { l } { x _ { 1 } } \\ { x _ { 2 } } \\ { x _ { 3 } } \end{array} \right] } = { \left[ \begin{array} { l } { \cos A \cos h } \\ { \sin A \cos h } \\ { \sin h } \end{array} \right] } .
$$

Note. The fundamental direction of the horizontal system is the vertical of the point in question. This is the direction of a plumb line, viz., the resultant of the Earth’s Newtonian attraction, the inertial force, at the place of observation, due to the Earth’s rotation relative to an inertial system, attractions of the Moon and the Sun (tidal forces), and, to a lesser extent, the attraction of the planets. As the intensity and direction of tidal forces vary in time, so therefore does the local vertical relative to tangible reference points (walls, telegraph poles, rocks, buildings, and so on). The local astronomical triad is thus slightly variable in relation to any terrestrial frame, with an amplitude of the order of $0 . 0 1 5 ^ { \prime \prime }$ , and monthly and annual periods.

![](images/dc1b83c9094797ce5f11ee801302751b8d29288eeb520a9850c86dbc85207abd.jpg)  
Fig. 4.3 Definition of the horizontal reference system

# The Hour Frame

As a result of diurnal motion, the coordinates of a star in the horizontal frame are variable, and subject to rather complicated laws. This renders the frame impractical for the cataloguing of celestial objects. Such a system is just adapted to the instantaneous description of the positions of objects in the sky for an observer at the Earth’s surface. The situation is improved by choosing the celestial equator as the fundamental plane, and thereby placing $\boldsymbol { e } _ { 3 }$ in the direction of the celestial pole. In this plane, the origin for longitudes is given by the intersection of the celestial equator with the local celestial meridian (see Fig. 4.4). There are two such intersections and the standard choice has been the direction in which the Sun culminates, i.e., the south for inhabitants of the Mediterranean region or China. The associated spherical coordinates are respectively:

• The declination $\delta$ for the angle of latitude, that is, the height of the star above the celestial equator. This takes values between $- \pi / 2$ and $+ \pi / 2$ and, for a given  Cstar, varies slightly in time due to the precession of the celestial equator and the proper motion of the star itself. This precession, i.e., the systematic motion of the celestial pole about the pole of the ecliptic, produces an annual variation in the declinations of stars equal to at most $2 0 ^ { \prime \prime }$ per year, whereas the true motion of the star in space leads to proper motions of 10 mas/year, except in exceptional cases. Precession is a motion of the frame relative to sources and not a true motion of the sources.

• The hour angle $H$ is the dihedral angle between the local meridian and the plane containing the directions of both the star and the celestial pole. For historical reasons connected with techniques for determining time, the convention fixing the orientation of $H$ is $\mathrm { d } H / \mathrm { d } t$ , which gives $H$ a left-handed orientation. Great care is therefore needed when applying rotation matrices in the hour frame. In contrast to the orientation of the azimuthal angle, the convention for orientating the hour angle involves no exceptions and we shall stick with it, despite the resulting mathematical drawback.

![](images/836f665531ba7337c864ec677a4d3f9229a722d39db68c610ace34ab5c24c8df.jpg)  
Fig. 4.4 The hour system of coordinates

The hour angle is traditionally expressed in units of time (hours, minutes, seconds), although it would be more appropriate to use units of angle (decimal degrees, radians) to carry out calculations:

$$
U ( H , \delta ) = { \left[ \begin{array} { l } { x _ { 1 } } \\ { x _ { 2 } } \\ { x _ { 3 } } \end{array} \right] } = { \left[ \begin{array} { l } { \cos H \cos \delta } \\ { - \sin H \cos \delta } \\ { \sin \delta } \end{array} \right] } .
$$

# The Equatorial Frame

The hour frame is still not perfectly adapted to a description of the sky which is independent of the observer, since it refers to the observer’s local meridian. This limitation is overcome by removing the large component of motion due to the Earth’s rotation (a period of 24 hours, to be compared with the small components due to nutation, period 18 years, and precession, period 26 000 years). The celestial pole still defines the direction $\boldsymbol { e } _ { 3 }$ , and declination is therefore the angle of latitude (see Fig. 4.5). In the equatorial plane, a non-rotating point is chosen as longitudinal origin, namely the intersection between the mean orbital plane of the Earth and the instantaneous celestial equator. This point is traditionally known as the vernal equinox and denoted $\gamma$ . The longitude in this system is called right ascension and is measured anti-clockwise as viewed from the celestial pole, so that the unit vector in the direction $o M$ becomes

$$
U ( \alpha , \delta ) = { \left[ \begin{array} { l } { x _ { 1 } } \\ { x _ { 2 } } \\ { x _ { 3 } } \end{array} \right] } = { \left[ \begin{array} { l } { \cos \alpha \cos \delta } \\ { \sin \alpha \cos \delta } \\ { \sin \delta } \end{array} \right] } .
$$

Star, galaxy, and radio-source catalogues use this system, specifying precisely the date corresponding to the choice of equator and the epoch at which the positions of the objects in the catalogue are given. There are, in fact, two main causes of variation in the equatorial coordinates of stars:

![](images/6ba78667ba04555cf4a3f2aaeb2eb97fd2038732c52dcd9da2230b991f5fe0e4.jpg)  
Fig. 4.5 The equatorial reference system

On the one hand, the change of frame which, through precession and nutation, modifies the position of the celestial equator relative to the stars and thus leads to variation of their coordinates, even if they have no real motion with respect to an inertial frame. The annual changes in coordinate values due to precession are of the order of $5 0 ^ { \prime \prime }$ . On the other hand, the stars are not fixed in space but rotate with the Galaxy, and each has its own proper displacement in time, leading to a change of equatorial coordinates, even in a fixed frame. This is manifested, in the sky, by a relative displacement of the stars with respect to each other, and by a slow evolution in the shapes of the constellations. The proper motions are generally very small, only 100 stars having an annual displacement greater than $0 . 1 { ^ { \prime \prime } }$ , and the most rapid amongst these, Barnard’s star,3 a proper motion of $1 0 ^ { \prime \prime }$ per year.

A stellar catalogue referred to the equatorial system is supplied with an equinox, i.e., a date corresponding to the orientation of the chosen equatorial systems, and an epoch, i.e., a date at which star positions are specified. In general the equinox is a neat conventional date (see Sect. 4.3.6), whereas the epoch of the catalogue is close to the median date of the observations used to compile it. Since the introduction of the ICRS reference system, the equatorial system is no longer formally attached to the celestial equator (although it is, by construction, very close to the celestial equator of 1 January 2000 at $1 2 \mathrm { h }$ ) and must be considered as fixed in the future. Its relationship with the equator at the given date is very complex for high accuracy observations (typically better than the millisecond of arc), but for the kind of accuracies discussed in this introduction, the classical precession and nutation transformations are largely sufficient.

# The Ecliptic Frame

The fundamental plane is the orbital plane of the Earth about the Sun, with origin at the vernal equinox (see Fig. 4.6). The whole problem here is to give a precise definition of the ecliptic and its relation to the equatorial system. If the Solar System contained only the Earth and the Sun, the orbital motion of the Earth would take place in a fixed plane which could be used as a definition and would be accessible to observation. The instantaneous orbital plane, containing the vector Sun–Earth (Sun–centre-of-mass of the Earth–Moon system would be a better definition) and the velocity vector, is not fixed because of planetary perturbations. It oscillates with amplitude $1 ^ { \prime \prime }$ of arc about a mean plane, on a time scale of several years. In other words, the ecliptic latitude of the Sun is not zero, but can reach $1 ^ { \prime \prime }$ . A very slow evolution of amplitude $\pm 1 . 3$ degrees on a time scale of 100 000 years ˙is superposed on this periodic motion, and this is one of the factors contributing to climatic oscillations. Over short periods, the ecliptic is defined by the mean plane with the rapid oscillations removed, and this rotates by about $4 7 ^ { \prime \prime }$ per century relative to an inertial frame.

The mean ecliptic at date $T$ is inclined to the reference ecliptic at epoch J2000 (see Sect. 4.3.6) at an angle

$$
\pi = 4 7 . 0 0 2 9 ^ { \prime \prime } T - 0 . 0 3 3 ^ { \prime \prime } T ^ { 2 } ,
$$

where $T$ is measured in Julian centuries of 36 525 days.

![](images/efc2223674df3ba35b7b1cbff5efb17510d019d0fbfe619e7d9731029fd5cb57.jpg)  
Fig. 4.6 Position of the ecliptic in relation to the celestial equator

The inclination $\varepsilon _ { 0 }$ of the ecliptic to the celestial equator (called the obliquity of the ecliptic) at the epoch J2000 is one of the constants in the system of astronomical constants. It is given by

$$
\varepsilon _ { 0 } = 2 3 ^ { \circ } 2 6 ^ { \prime } 2 1 . 4 0 6 ^ { \prime \prime } \approx 2 3 . 4 3 9 2 7 9 ^ { \circ } ,
$$

and its value at another epoch $T$ is given by

$$
\varepsilon ( T ) = \varepsilon _ { 0 } + a T = 2 3 . 4 3 9 2 7 9 ^ { \circ } - 4 6 . 8 1 5 ^ { \prime \prime } T + O ( T ^ { 2 } ) ,
$$

where $T$ is measured in Julian centuries from J2000. (Note here that the rate of change is given in seconds of arc, not degrees.) This secular decrease, due to the movement of the ecliptic, has been exposed through obliquity measurements made from the time of Hipparchos in the second century BC. We know that Eratosthenes obtained $\varepsilon = 2 3 ^ { \circ } 5 0 ^ { \prime }$ in the second century BC, i.e., a difference of just $7 ^ { \prime }$ from the Dvalue given by the above formula.

Many periodic oscillations are superposed on this regular variation of the obliquity, the largest resulting from the nutation of the Earth’s axis, with a period of 18.6 years and an amplitude of $9 . 2 0 ^ { \prime \prime }$ . However, this is a motion of the celestial equator relative to the ecliptic, and not a true motion of the ecliptic relative to the stars.

# The Galactic Frame

A system of galactic coordinates is also required for studies in which the galactic plane enters as the natural plane of symmetry, e.g., when studying the spatial distribution of different populations of stars, and for kinematic or dynamic studies of the Galaxy. The galactic plane is thus used as the fundamental reference plane. Since no precise physical definition exists for the latter, a plane is chosen by convention, close to the plane perpendicular to the rotation vector of the Galaxy, which is determined by observation of the hydrogen $2 1 \mathrm { c m }$ line. Although equivalence with some physical definition is not essential in defining this frame (there is no accurate access to the system), it is of the utmost importance that astronomers should agree on a common definition. In order to orient the galactic triad with respect to the equatorial triad (see p. 134), three parameters are required, corresponding to the three degrees of freedom of a solid rotating about a fixed point, e.g., the three Euler angles shown in Fig. 4.7.

With sufficient accuracy for calculation purposes, we can use

$$
\psi = 2 8 2 . 8 6 \deg , \theta = 6 2 . 8 7 \deg , \phi = 3 2 7 . 0 6 \deg ,
$$

which gives for the coordinates of the galactic pole (direction of $z _ { 2 }$ ) and the galactic centre (direction of $y _ { 1 }$ ) in J2000

$$
\alpha _ { \mathrm { p } } = 1 2 \mathrm { h } 5 1 \mathrm { m } 2 6 \mathrm { s } = 1 9 2 . 8 5 9 \mathrm { d e g } , \delta _ { \mathrm { p } } = 2 7 ^ { \circ } 0 7 ^ { \prime } 4 1 ^ { \prime \prime } = 2 7 . 1 2 8 \mathrm { d e }
$$

![](images/4b0c4f9baa08439f6c54dd33000f508578ad8a6d9beae647e45f3585ca589fed.jpg)  
Fig. 4.7 The galactic coordinate system

Note that the usual definition through the coordinates of the pole and the centre makes use of four parameters instead of three. The four coordinates are not independent since the galactic centre lies in the plane normal to the direction defined by the galactic pole.

# 4.1.3 Change of Frame

In every case, changing from one celestial frame to another means finding the rotation matrix which transforms the vector basis of one frame into that of the other. The vectorial approach is far better adapted to modern calculation techniques than the traditional method based on trigonometric relations in spherical triangles, and naturally it leads to exactly the same analytical formulas. However, as far as computation time is concerned, linear transformations are much more efficient for numerical computations than evaluating trigonometric lines occurring in the full formulas, and the programming aspect is more straightforward, too. While it should not be forgotten that the trigonometric calculations are embodied by the rotation operators, the latter become tools and their calculation can be optimised once and for all.

Given the vector $o M$ , let $x _ { 1 }$ ; $x _ { 2 }$ ; $x _ { 3 }$ be its Cartesian components in frame $R$ , and $x _ { 1 } ^ { \prime }$ ; $x _ { 2 } ^ { \prime }$ ; $x _ { 3 } ^ { \prime }$ its components in frame $R ^ { \prime }$ . We transform from $R$ to $R ^ { \prime }$ by rotating the triad through an angle $\phi$ about a direction $\pmb { I }$ . The transformation is parametrised by a $3 \times 3$ orthogonal matrix $\mathsf { R }$ .

![](images/5768890b8fb2e0a6cf32a090600f9698ea56f8e22afab73692f1294f089cb835.jpg)  
Fig. 4.8 Elementary rotations about coordinate axes

Thus,

$$
{ \left[ \begin{array} { l } { x _ { 1 } ^ { \prime } } \\ { x _ { 2 } ^ { \prime } } \\ { x _ { 3 } ^ { \prime } } \end{array} \right] } = \left[ \mathsf { R } \right] { \left[ \begin{array} { l } { x _ { 1 } } \\ { x _ { 2 } } \\ { x _ { 3 } } \end{array} \right] } .
$$

In the elementary case of rotations about coordinate axes, which are the most important in practice, the matrices $\mathsf { R }$ have the following form (see Fig. 4.8):

$$
\mathsf { R } _ { 1 } ( \alpha ) = \left[ \begin{array} { c c c } { 1 } & { 0 } & { 0 } \\ { 0 } & { \cos \alpha } & { \sin \alpha } \\ { 0 } & { \sin \alpha } & { \cos \alpha } \end{array} \right] , \quad \mathsf { R } _ { 2 } ( \beta ) = \left[ \begin{array} { c c c } { \cos \beta } & { 0 } & { - \sin \beta } \\ { 0 } & { 1 } & { 0 } \\ { \sin \beta } & { 0 } & { \cos \beta } \end{array} \right] ,
$$

$$
{ \sf R } _ { 3 } ( \gamma ) = \left[ \begin{array} { c c c } { { \cos \gamma } } & { { \sin \gamma } } & { { 0 } } \\ { { - \sin \gamma \cos \gamma } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 1 } } \end{array} \right] .
$$

Note. The above rotation matrices correspond to passive rotations. It is the axes that rotate and not the source. When applied to a vector, the components of the vector relative to the first system are transformed to the components of the same vector relative to the second system.

# Transformation from Horizontal to Hour Frame $( A , h ) \longleftrightarrow ( H , \delta )$

The two triads have a common vector $e _ { 2 }$ , hence the transformation is just a rotation about axis $O x _ { 2 }$ . The angle between the vectors $e _ { 3 }$ of each system is equal to the co-latitude at the point, that is, $\pi / 2 - \phi$ , where $\phi$ is the latitude of the observer. The transformation between the unit vectors is thus

$$
U ( A , h ) = { \sf R } _ { 2 } ( \pi / 2 - \phi ) { \cal U } ( H , \delta ) .
$$

So, applying the rotation matrix to the Cartesian components, we obtain the transformation of the spherical coordinates directly:

cos h cos $A = - \cos \phi$ $\sin \delta + \sin \phi$ cos ı cos $H$ ; cos h sin $A = - \cos \delta$ sin $H$ C; D sin h sin  sin ı cos  cos ı cos $H$ :

The last equation in this group, giving the height of a body as a function of time via $H$ , is the fundamental equation of diurnal motion, used to calculate risings and settings, the height at culmination, the duration of a sunset, and so on.

Likewise for the inverse transformation,

$$
U ( H , \delta ) = \mathsf { R } _ { 2 } ( - \pi / 2 + \phi ) U ( A , h ) ,
$$

which gives

$$
\begin{array} { r } { \boxed { \begin{array} { l } { \cos \delta \cos H = \cos \phi \sin h + \sin \phi \cos h \cos A , } \\ { \cos \delta \sin H = - \cos h \sin A , } \\ { \sin \delta = \sin \phi \sin h - \cos \phi \cos h \cos A . } \end{array} } } \end{array}
$$

Note. The trigonometric formulas are given here for reference. It is always preferable to work with Cartesian components and the rotation matrices for numerical computations, only bringing in angles as intermediate quantities between input and output. Nevertheless, qualitative and analytic studies are more easily handled using the angular expressions.

# Transformation from Hour to Equatorial Frame $( H , \delta ) \longleftrightarrow ( \alpha , \delta )$

These two systems, described in Sect. 4.1.2, share the axis $\boldsymbol { e } _ { 3 }$ which corresponds to the orientation of the Earth in space, and only differ through their rotation about this axis. This rotation positions the observer’s astronomical meridian relative to the vernal equinox. Denote the dihedral angle between this meridian and the plane $\alpha = 0$ passing through the vernal equinox by $\alpha _ { \mathrm { z } }$ . It is also the right ascension of the Dobserver’s zenith at the instant of observation. It varies with time, increasing by 360 degrees for each sidereal rotation of the Earth, that is, every $8 6 1 6 4 . 1 0 \mathrm { s }$ . With the help of Fig. 4.9, we observe that this angle is numerically equal to the hour angle of the vernal equinox, otherwise known as the local sidereal time. This terminology, which has its origins in the meridian observations practised in all observatories since the seventeenth century, should be avoided. The quantity in question is an angle, not a time, and relating its definition to an hour angle orientates it in the retrograde direction. Moreover, time measurement today has no connection with the rotation of the Earth. Use of the right ascension of the zenith instead of sidereal time confirms this separation, avoiding confusion and returning the question to the realm of geometry. When the rotational state of the Earth is specified by the hour angle of the vernal equinox, i.e., the sidereal time, we are thinking of the skies as in motion around the Earth, since the hour angle increases with time. It is therefore a description of the apparent motion as it would be perceived by an Earth-based observer. Using the right ascension of the local zenith, it is the Earth that rotates relative to the stars, and this sidereal angle is also an increasing function of time. Its interpretation conforms better to true motions.

![](images/fed72ef8ae87d1cd680a4d9f6f073266f31a9b69966be53c86d9c909007009b1.jpg)  
Fig. 4.9 Relation between hour and equatorial systems

In fact, the transformations between hour and equatorial coordinates are very simple, reducing to

$$
U ( H , \delta ) = \mathsf { R } _ { 3 } ( \alpha _ { \mathrm { z } } ) \ U ( \alpha , \delta ) ,
$$

which gives for the spherical coordinates

$$
\boxed { H = \alpha _ { \mathrm { z } } - \alpha , \quad \delta = \delta . }
$$

In order to carry out this transformation in practice, we need to know $\alpha _ { \mathrm { z } }$ . Since this angle describes the Earth’s rotation relative to the celestial sphere, we must have recourse either to observation, or to a theory of the Earth’s rotation accurate enough for the purpose in hand. At the introductory level supposed in the present book, it is sufficient to consider the Earth as rotating uniformly about its axis once every sidereal day, with angular speed

$$
\omega = \frac { 3 6 0 } { 8 6 1 6 4 . 1 0 } \times 3 6 0 0 \sim 1 5 . 0 4 1 0 7 \mathrm { d e g h ^ { - 1 } } .
$$

The deviation from uniformity amounts to about $0 . 0 3 ^ { \prime \prime }$ on a time scale of several years. Over periods of several centuries, the secular slowing of the Earth’s rotation has to be taken into account. The latter effect, although very slight regarding the speed of rotation, is nevertheless cumulative on the phase, increasing as the square of the time. In practice, the precise orientation of the Earth in space can only be obtained to a very high level of accuracy by regular observation using space geodesy techniques and very long baseline interferometry. The measured orientation and angular velocity parameters are available online, almost in real time, and always accompanied by predicted values for the coming months.

The right ascension at Greenwich is given in the astronomical almanacs in the form of a table, for each day at 0 hours $\mathrm { ( 0 h ) }$ , and from this the value of $\alpha _ { \mathrm { z } }$ at the same instant of time can be calculated at any longitude $\lambda$ (measured positively towards the east) by

$$
\alpha _ { \mathrm { z } } ( 0 \mathrm { h } ) = \alpha _ { \mathrm { G } } ( 0 \mathrm { h } ) + \lambda ,
$$

and at any time $t$ during the day by

$$
\alpha _ { \mathrm { z } } ( t ) = \alpha _ { \mathrm { z } } ( 0 \mathrm { h } ) + \omega t .
$$

To an accuracy of about 0.005 degrees, $\alpha _ { \mathrm { G } } ( 0 \hbar )$ can be calculated directly, without reference to the almanacs, using the formula

$$
\alpha _ { \mathrm { G } } ( 0 \mathrm { h } ) = 1 0 0 . 4 6 0 6 + 0 . 9 8 5 6 4 7 3 d ,
$$

where $d$ is the number of days between J2000 (JD 2 451 545, where JD is discussed later) and the day under consideration at $_ { \mathrm { 0 h } }$ UT. Since the reference epoch J2000 begins at $1 2 \mathrm { h }$ , in the above expression, $d$ takes values $\pm 0 . 5 , \pm 1 . 5$ , and so on, ˙ ˙rather than continuous or integer values. This is a stroboscopic expression, in which we remove multiples of 360 degrees corresponding to integer numbers of rotations of the Earth about its axis. Since TU is very close to mean solar time, the numerical coefficient in the formula for $\alpha _ { \mathrm { G } } ( 0 \hbar )$ is nothing else but the mean displacement of the (tropical) Sun in right ascension per day, namely $3 6 0 / 3 6 5 . 2 4 2 2 = 0 . 9 8 5 6 4 7$ deg. For example, for the sidereal angle of Greenwich Don 01/01/2007 at $_ { \mathrm { 0 h } }$ UT, we have $\mathrm { J D } ~ = ~ 2 4 5 4 1 0 1 . 5$ , $\begin{array} { r l r } { d } & { { } = } & { 2 5 5 6 . 5 } \end{array}$ , and $\alpha _ { \mathrm { G } } ~ = ~ 1 0 0 . 2 6 7 9 ^ { \circ }$ D D. The value given by a high accuracy astronomical almanac is $6 \mathrm { h } 4 1 \mathrm { m } 4 . 5 5 \mathrm { s } = 1 0 0 . 2 6 8 9 6 ^ { \circ }$ . The discrepancy comes from the nutation effect on Dlongitude, of the order of 0.001 deg, or $0 . 2 \mathrm { s }$ .

# Transformation from Equatorial to Ecliptic Frame $( \alpha , \delta ) \longleftrightarrow ( l , b )$

This is another trivial case, being simply a rotation through angle $\varepsilon$ about the axis $e _ { 1 }$ which is common to the two frames:

$$
U ( l , b ) = \mathsf { R } _ { 1 } ( \varepsilon ) ~ U ( \alpha , \delta ) ,
$$

$$
\begin{array} { r } { \boxed { \cos b \cos l = \cos \alpha \cos \delta , } } \\ { \cos b \sin l = \sin \varepsilon \sin \delta + \cos \varepsilon \cos \delta \sin \alpha , } \\ { \sin b = \cos \varepsilon \sin \delta - \sin \varepsilon \cos \delta \sin \alpha , } \end{array}
$$

and for the inverse transformation

$$
U ( \alpha , \delta ) = \mathsf { R } _ { 1 } ( - \varepsilon ) \ U ( l , b ) ,
$$

$$
\left| \begin{array} { l } { { \cos \delta \cos \alpha = \cos l \cos b , } } \\ { { \cos \delta \sin \alpha = - \sin \varepsilon \sin b + \cos \varepsilon \cos b \sin l , } } \\ { { \sin \delta = \cos \varepsilon \sin b + \sin \varepsilon \cos b \sin l . } } \end{array} \right.
$$

It is interesting to specialise the second group for the Sun, i.e., when $b = 0$ :

$$
\begin{array} { l } { \cos \delta \cos \alpha = \cos l , } \\ { \cos \delta \sin \alpha = \sin l \cos \varepsilon , } \\ { \sin \delta = \sin l \sin \varepsilon , } \end{array}
$$

which gives the equatorial coordinates of the Sun as a function of its ecliptic longitude l. The longitudinal motion is very easy to calculate from Kepler’s equations, with an accuracy of $\sim 1 0 ^ { \prime \prime }$ , so it is a straightforward matter to write a little auto-nomous program a few lines long that gives a low accuracy ephemeris for the Sun. Eliminating the declination between the first two equations, this yields

$$
\tan \alpha = \cos \varepsilon \tan l ,
$$

whence it is possible to express the right ascension as a function of longitude using a rapidly converging expansion, viz.,

$$
\alpha = l - \tan ^ { 2 } { \frac { \varepsilon } { 2 } } \sin 2 l + { \frac { 1 } { 2 } } \tan ^ { 4 } { \frac { \varepsilon } { 2 } } \sin 4 l - { \frac { 1 } { 3 } } \tan ^ { 6 } { \frac { \varepsilon } { 2 } } \sin 6 l + \cdots ,
$$

or numerically in degrees:

$$
\alpha = l - 2 . 4 6 5 8 \sin 2 l + 0 . 0 5 3 1 \sin 4 l - 0 . 0 0 1 5 \sin 6 l + \cdots .
$$

The quantity $\alpha - l$ is usually called the reduction at the equator. It is important in the definition of the mean solar time, or when reading a sundial.

# Transformation from Equatorial to Galactic Frame $( \alpha , \delta ) \longleftrightarrow ( \lambda , \beta )$

This last case is the most general, requiring a complete rotation matrix, composed of three elementary rotations through each of the three Euler angles $\psi , \theta , \phi$ , whose numerical values were given in Sect. 4.1.2:

$$
U ( \lambda , \beta ) = { \mathsf { R } } _ { 3 } \left( \phi \right) { \mathsf { R } } _ { 1 } \left( \theta \right) { \mathsf { R } } _ { 3 } \left( \psi \right) U ( \alpha , \delta ) .
$$

Calculation of the product of the three above matrices is straightforward but tedious. Numerically, the Cartesian coordinates $( x _ { 1 } ^ { \prime } , x _ { 2 } ^ { \prime } , x _ { 3 } ^ { \prime } )$ of $^ { o M }$ in the galactic frame can be calculated from its Cartesian coordinates $( x _ { 1 } , x _ { 2 } , x _ { 3 } )$ in the equatorial frame by

$$
{ \left[ \begin{array} { l } { x _ { 1 } ^ { \prime } } \\ { x _ { 2 } ^ { \prime } } \\ { x _ { 3 } ^ { \prime } } \end{array} \right] } = { \left[ \begin{array} { l l } { - 0 . 0 5 4 8 8 - 0 . 8 7 3 4 4 - 0 . 4 8 3 8 4 } \\ { 0 . 4 9 4 1 1 - 0 . 4 4 4 8 3 } & { 0 . 7 4 6 9 8 } \\ { - 0 . 8 6 7 6 7 - 0 . 1 9 8 0 8 } & { 0 . 4 5 5 9 8 } \end{array} \right] } { \left[ \begin{array} { l } { x _ { 1 } } \\ { x _ { 2 } } \\ { x _ { 3 } } \end{array} \right] } .
$$

For example, the Crab Nebula has equatorial coordinates $\alpha = 5 { \mathrm { h } } 3 1 { \mathrm { m } } \approx 8 2 . 7 5$ deg, $\delta = 2 1 ^ { \circ } 5 9 ^ { \prime } \approx 2 1 . 9 8$ deg. The vector $^ { o M }$ D thus has the Cartesian coordinate rep-D resentation (0.11702, 0.91990, 0.37428). Applying the above matrix, its Cartesian coordinates in the galactic frame are $( - 0 . 9 9 1 0 0 , - 0 . 0 7 1 8 6 , - 0 . 1 1 3 0 3 )$ which gives angular coordinates $\lambda ~ = ~ 1 8 4 . 1 4 ($ deg; $\beta ~ = ~ - 6 . 4 9$ deg, implying a location very Dclose to the galactic plane.

# 4.2 Practical Realisation of Spatial Frames

# 4.2.1 Celestial Reference Systems

From the moment astronomers wished to record their observations in the form of catalogues or charts, either to be able to describe the sky, or just to remember them, they had to choose a reference system by defining a fundamental plane and an origin for longitudes. They then defined a frame, that is, a system of coordinates, and, finally, some practical realisation of those coordinates in space, in order to be able to determine them by measurement. It is no easy task, while making the first observations of some new body, or following the path of an asteroid, to establish the coordinates of such an object lost in the heavens. An idea which comes immediately to mind would be to measure its position relative to known neighbouring objects and to determine its coordinates from the coordinates of these nearby stars, either by direct micrometric measurement, or by means of photographic plates or CCD images. But, as in every system of standards, there then arises the problem of fixing the coordinates of those reference objects themselves by some other method, and indeed with great care, given their prior position in the order of things.

The aim of these reference catalogues, the counterpart of standards in physical metrology, is to place markers of known position across the sky, not only at the precise date when the catalogue is made, but also at other times both before and after that date, which involves determining the motion of these markers. The transition from a theoretical reference system to its practical realisation in the sky amounts to establishing by convention a system of reference as close as possible to the ideal one, as it was conceived by its inventors. In practice, the difference between the two may be obscured, but, on a conceptual level, it remains fundamental. The same distinction could be made between the first definition of the metre as being a certain fraction of the terrestrial meridian, and its realisation in the form of a standard metre stored in the archives. The latter was indeed the standard, an accessible material realisation, and not the metre by definition, a situation to be contrasted with the case of the kilogram even today.

Astronomical reference frames, unlike milestones along a main road, are more than just kinematic reference points. It is required of these frames that the laws of dynamics should hold in them without recourse to any other forces than gravity and, in certain cases, well-understood dissipative forces. This implies that the frames should be inertial, and therefore non-rotating. Once again, the problems posed by this ideal go outside the realm of the present text, and we shall merely assume the absence of any rotation relative to the general distribution of extragalactic matter beyond a distance of $1 0 0 \mathrm { M p c }$ .

# 4.2.2 Fundamental Catalogues

By definition, these catalogues, which contain only a small number of stars, represent the inertial system by convention. In the case of the equatorial system, the position and proper motion of the stars, i.e., their right ascension and declination at different epochs, must be determined. To this end, the declinations present no difficulty in principle, using the right meridian instrumentation. With a good model of the Earth’s precession, values measured at different dates can be related to a unique reference equator. Concerning right ascension, however, a major difficulty arises because the vernal equinox is not accessible by observation of the stars. Only the difference between the right ascensions of two stars can be easily obtained by means of a clock and a meridian circle, which constitutes only a relative observation and not a fundamental one. This difficulty was to be expected, for the definition of the vernal equinox refers to the annual motion of the Earth and not to the stars. The solution to the problem lies in simultaneous observation of both the Sun and the stars, with a view to linking the right ascension of each star to that of the Sun, and thus to the vernal equinox.

In this sense, these fundamental catalogues are realisations of a dynamical reference system. The point is crucial, demonstrating the great difference between the celestial reference systems, based on fundamental catalogues, and the extragalactic system which has replaced them as the conventional system. Nevertheless, once a fundamental catalogue is available, it is the right ascensions and declinations taken as a whole which define in practical terms the equator and the equinox. Only further observations of the Sun (or the planets) and the stars allow the relation between the definition of the reference system and its practical realisation to be checked, and only then can any correction to the equinox be published, if necessary, and applied to the stars.

Table 4.3 The main star catalogues   

<table><tr><td>Catalogue</td><td>Number of stars</td><td>Mean epoch</td><td>Accuracy of 1990 positions</td><td>Accuracy of proper motions</td></tr><tr><td>FK4</td><td>1500</td><td>1949</td><td>0.1&quot;</td><td></td></tr><tr><td>FK5</td><td>1500</td><td>1949</td><td>0.05&quot;</td><td>0.0008&quot;/year</td></tr><tr><td>FK5 extended</td><td>3000</td><td></td><td>0.08&quot;</td><td>0.002&quot;/year</td></tr><tr><td>Hipparcos</td><td>120000</td><td>1991.25</td><td>0.001&quot;</td><td>0.001&quot;/year</td></tr><tr><td>Tycho-2</td><td>2 000000</td><td>1991.25</td><td>0.03&quot;</td><td>0.003&quot;/year</td></tr><tr><td>PPM</td><td>380000</td><td></td><td>0.3&quot;</td><td>0.006&quot;/year</td></tr><tr><td>SAO</td><td>250000</td><td></td><td>1.5&quot;</td><td></td></tr><tr><td>GSC</td><td>20000 000</td><td></td><td>1.5&quot;</td><td></td></tr><tr><td>UCAC</td><td>50000 000</td><td>2001</td><td>0.02-0.07&quot;</td><td></td></tr></table>

The first fundamental system was devised by F.W. Bessel4 who, in the nineteenth century, used J. Bradley $\mathrm { ^ { 5 } s ^ { 5 } }$ observations to link 14 bright stars directly to the Sun. A few years later the system was extended to 36 stars and thereafter remained the basis for determining all right ascensions until the beginning of the twentieth century. The number of fundamental stars increased gradually up until the publication of the FK4 (Vierter Fundamental Katalog) in 1963, with its 1 535 stars. Then came a further revision, the FK5, in 1986, with the same stars but a new determination of the equinox and the constant of precession, and a correction to the proper motions.

Between the two catalogues, right ascensions differ systematically according to the relation

$$
\alpha _ { \mathrm { F K } 5 } = \alpha _ { \mathrm { F K } 4 } + 1 . 1 6 3 ^ { \prime \prime } + 1 . 2 7 5 ^ { \prime \prime } T ,
$$

where $T$ is the time in Julian centuries measured from J2000 (see Sect. 4.3.6). Consequently, the proper motions in right ascension given in the two systems differ by $1 . 2 7 5 ^ { \prime \prime }$ per century.

By 1990, the accuracy was $0 . 0 5 ^ { \prime \prime }$ on the positions, and $0 . 0 0 1 ^ { \prime \prime }$ per year on the proper motions. Comparison with recent observations and, in particular, with the Hipparcos catalogue also reveal systematic errors of amplitude around $0 . 1 ^ { \prime \prime }$ . A further 3 000 stars, measured to an accuracy of $0 . 0 8 ^ { \prime \prime }$ and $0 . 0 0 2 ^ { \prime \prime }$ per year, had been added.

All other high-quality determinations of stellar position are based on extensions of the fundamental catalogue, either through relative meridian observations, which are so much easier than absolute observations, or through photographic compilations of relatively low accuracy $( \approx ~ 1 ^ { \prime \prime } )$ . General catalogues of position and/or proper motion include between $1 0 ^ { 4 }$ and $1 0 ^ { 7 }$ stars, extending the fundamental catalogues in terms of both spatial density and magnitude, to varying degrees of accuracy. A short list of these catalogues and their features is given in Table 4.3.

# 4.2.3 The Extragalactic System

# A Kinematic Reference System

Up until now we have been trying to give the inertial reference system a practical realisation in terms of sources in perpetual movement relative to each other and only indirectly related to the theoretical frame (in this case, the equator and the equinox). But there exists a much more geometrical alternative. If the stars had no relative motion, one relative to the other, they would constitute a set of luminous points on the sky, globally unchanging, which could be used to mark positions. The purely kinematic aspect of the reference frame would be satisfied by this solution.

Now, there would be nothing to guarantee that the whole system were not rotating relative to some inertial system. But if this were the case, it would be possible to demonstrate the fact, by comparing the motion of the planets relative to this framework with their theoretically predicted motion deduced from Newton’s law in the absence of any inertial forces. By applying this global rotational correction, i.e., attributing a suitable proper motion to each star to ensure that the resulting system were inertial, one would then be able to materialise a reference frame with the fundamental features. Unfortunately, the stars in the Galaxy (the only stars we can actually see individually) have relative motions, and the constellations are not unchanging patterns.

Such a reference system, determined by the relative positions of sources, is described as a geometric system or kinematic system, given the absence of any dynamical criteria in its definition.

For the straightforward task of locating objects not in the original catalogue, the fact that the frame is not inertial presents no great difficulty, and a system as arbitrary as this might be sufficient to build up a catalogue of positions. But from the moment dynamical studies are envisaged (rotation of the Earth, Solar System, rotational movements of the Galaxy, and so on), this problem must be faced. The most satisfying way of fulfilling the two requirements (no relative motion and no global rotation) is to use extragalactic quasi-stellar objects (QSO) which are virtually fixed relative to each other. The idea is not new, having been proposed by both Herschel6 and Laplace7 over 200 years ago. The fact that extragalactic objects constitute a non-rotating sphere cannot be demonstrated in itself, but rests on a series of assumptions which are confirmed by observation. The most distant galaxies have an isotropic distribution and the radial components of their velocities increase systematically with their distances. The $3 \mathrm { K }$ background, uniform to a very high degree, supports the idea that the Universe as a whole has no rotation.

The physical significance of this declaration of faith nevertheless leaves the way open to several interpretations. This choice must be viewed in the light of Mach’s principle,8 which attributes inertia to the general distribution of mass in the Universe, but is independent of relativity theories. Experimentally, comparison of the most accurate measurements of a dynamical system, namely those obtained by laser telemetry of the Moon, with those of a kinematic system, based on radio interferometry observations, has not revealed any rotation between the two systems. Moreover, if we suppose that the tangential speeds of quasars are statistically comparable to their recession speeds, then their proper motion would be

$$
\alpha = H < 0 . 0 2 \mathrm { m a s } / \mathrm { y e a r } ,
$$

where $H$ is Hubble’s constant9 and $1 \mathrm { { m a s } = 0 . 0 0 1 ^ { \prime \prime } }$ . It is reasonable to suppose Dthat the actual speeds are much less than this value and that, up to a few $\mu { } \mathrm { a s }$ $( = 1 0 ^ { - 6 }$ seconds of arc), quasars show no systematic movement. At the 1991 DGeneral Assembly of the International Astronomical Union, it was recommended that the future conventional inertial reference system should from that time comprise a set of distant radio sources referred to the barycenter of the Solar System. The system specified in this way is called the International Celestial Reference System (ICRS). The basic principle is quite general and says nothing about the list of sources or observational techniques to be used to observe them. A practical realisation of this system will involve physical construction of the reference frame materialised by a highly accurate list of extragalactic sources accompanied by their coordinates. The sources must therefore be selected and observed in a consistent way, so that the angular distances between pairs of sources on the sky are in perfect agreement with a calculation based on their coordinates. This realisation is called the International Celestial Reference Frame (ICRF).

The difference between the words ‘system’ and ‘frame’ is fundamental: a system is above all a set of principles and prescriptions specifying the concepts to be used to construct the frame, i.e., the practical realisation of the system. These principles must be sufficient to specify the origin and orientation of the reference triad at any given epoch. There is only one system (here the ICRS), which can have different realisations, even if, at a given epoch, only one of these can be qualified as reference frame (here the ICRF). The current primary reference frame is based on very long baseline interferometry (VLBI) observations, but in the future, optical observations by the Gaia mission will provide a new realisation.

# Observational Methods

In order to construct a kinematic frame, a reference plane and origin for longitudes must once again be defined. There is no a priori natural definition since the system is geometric. It is the coordinates themselves of the objects which both define the frame and realise it physically. The declinations of two objects are sufficient to construct the pole (with a discrete choice between two possibilities), and the longitude of any particular object defines the origin of longitude. For reasons of continuity, one ensures that the frame thereby constructed remains very close to the equatorial frame (see Sect. 4.1.2), previously materialised by FK5, and the origin of longitudes is chosen as close as possible to the dynamical equinox of J2000. We then speak of declinations and right ascensions, even though the latter owe nothing to the definiton of the equinox, but rather to a conventional origin in the fundamental plane.

The radio source observations are made by very long baseline interferometry (VLBI) to an accuracy better than one millisecond of arc (see Fig. 4.10). In contrast with the case of connected interferometers, correlation of signals received in each radiotelescope is delayed, bearing in mind that the very high stability of the local oscillators and the possibility of a posteriori synchronisation of the signals allows for digital rather than analogical phasing of the two signals (see Sect. 6.5.1). The observable quantity is not the phase of the fringes but rather the delay between arrivals at the two antennas, together with its derivative. For a wavelength $\lambda$ of several centimetres and a base line length $B$ of several thousand kilometres, a resolution of the order of

$$
\lambda / B \approx 1 \mathrm { m a s }
$$

can be achieved. If $r _ { 1 }$ and $r _ { 2 }$ are the radius vectors from the centre of the Earth to the two stations, the base line is $B = r _ { 2 } - r _ { 1 }$ . Calling the unit vector in the direction of the source $\pmb { S }$ D , we obtain the fundamental relation of a VLBI observation:

![](images/ffd3679aaad0d5a9b2bb8930182898b7f7cd4fa668dbe7681977b7f885bccdf0.jpg)  
Fig. 4.10 Geometry of VLBI observations

$$
\tau = \frac { B \cdot s } { c } ,
$$

where $\tau$ is the delay between wavefront arrivals and $c$ is the speed of light in vacuum. Letting $\delta$ and $H$ be the declination and hour angle, respectively, of the source, and $d$ and $h$ the corresponding quantities for the unit vector of the base line $\pmb { B }$ , the delay is given by

$$
\tau = \frac { B } { c } \left[ \sin d \sin \delta + \cos d \cos \delta \cos ( H - h ) \right] .
$$

The observation thus reveals the position of the base line relative to the celestial reference system, as well as the direction of the source. For base lines known in the terrestrial frame, we can determine parameters describing the orientation of the Earth and also the coordinates of the sources in the celestial reference system. Conversely, observation of known sources can be used to follow the rotation of the Earth and locate the stations on the various continents. The implication is thus that we have a global treatment of the observations made by a network of radiotelescopes.

At present, the VLBI astrometry program comprises about twenty antennas, most of these being located in the northern hemisphere. Analysis of the data has created a fundamental catalogue, the observations relating to the whole of the sky, object by object, without any need to link those objects progressively to each other. The set of arcs joining the sources into pairs constitutes the reference system, although, in practice, because of the choice of origin for right ascensions, the actual coordinates of the sources constitute the system.

# Properties of the ICRF

The first ICRF solution was officially published in 1998 and formally adopted as reference frame replacing the FK5 on 1 January 1998, following an IAU resolution during the general assembly of August 1997. In order to keep the orientation as close as possible to that defined by the FK5, the optical coordinates of the radiosource 3C273 have been determined, by lunar occultation, in the dynamical reference system. The right ascension $( \alpha = 1 2 \mathrm { h } \ 2 9 \mathrm { m } \ 6 . 6 9 9 7 \mathrm { s }$ in J2000) of 3C273 was thus Dfixed initially in the treatment of data, imposing a constraint on the origin of the kinematic reference system. In the final version of the reference system, this origin was actually set by imposing mean difference of zero on a set of 23 sources. This version of the ICRF (known as ICRF1) was followed by two extensions, with slightly more sources. The last extension of the ICRF1 released in 2004 (denoted ICRF1-Ext.2) contained 717 sources (compared with 608 in the initial version of 1998), including 212 defining sources, 294 candidate sources, and 211 other sources.

A new version was adopted by the IAU in August 2009 (the ICRF2) as the current official primary realisation of the celestial reference frame. It contains precise positions of 3414 compact radio astronomical sources, with a noise floor of $4 0 ~ \mu$ as and a stability in its orientation of $1 0 ~ \mu$ as. The ICRF2 axes rest upon a set of 295 new defining sources selected on the basis of positional stability and the absence of extensive intrinsic source structure. It is complemented by another set of 922 sources observed in VLBI, with good distribution over the sky and a larger set of 2197 sources used as calibrators for the radio astronomical community. They have also been included in the ICRF2, given their high astrometric quality. The distributions of the three categories of sources are shown in Fig. 4.11.

![](images/2cb39f026ad46a468aac31b9e70e5293823181b29170d0a83e5e2682c02bc12a.jpg)  
Fig. 4.11 Distribution of ICRF2 sources in equatorial coordinates. Black circles: the 295 defining sources. White circles: the 922 additional VLBI sources. Stars: the remaining 2197 sources, from the calibration sessions.

The ICRF pole (and hence also the reference equator) do not coincide exactly with the celestial pole (and celestial equator) at the epoch J2000, but every effort has been made to ensure that it is as close as possible. The discrepancy is $- 1 7 \pm 0 . 2$ mas in the direction $\alpha = 0$ deg and $- 5 . 1 \pm 0 . 2$ mas in the direction $\alpha = 9 0$ ˙deg. DFor calculations of medium accuracy $\mathrm { \Lambda } ( > 1 0 0 \mathrm { \ m a s } )$ D), it can be taken to coincide with the celestial pole at J2000. The origin in the ICRF equator is shifted by $+ 5 5 . 4$ mas Crelative to the inertial equinox (intersection of the ecliptic with the ICRF equator), and is also located at 22:9 mas from the origin of the FK5 right ascension.

# 4.2.4 The Hipparcos Frame

Various extensions of the extragalactic system are necessary, in the first place because of the small number of reference sources $( \sim 2 0 0 )$ , but also because stellar astronomy has a strong preference for optical and infrared wavelengths. The optical counterparts of the ICRF sources are all faint in the visible and difficult to observe. Since the density is very low (one source corresponds on average to ${ \sim } 7 0$ square degrees), direct use of these sources would be impossible, even in wide-field astronomy. As far as optical sources are concerned, only the Hipparcos catalogue can link them accurately to the extragalactic system. Before explaining how the Hipparcos system can be attached to the radiosource system, we describe some of the technical details of this space mission, and present the main properties of the results.

# The Hipparcos Mission

Hipparcos is an acronym for HIgh Precision PARallax COllecting Satellite. The Hipparcos satellite was launched by Ariane, from the Kourou launch pad, on 8 August 1989. Owing to failure of the apogee boost motor, it proved impossible to place the satellite on the circular geostationary orbit of radius $4 2 0 0 0 \mathrm { k m }$ for which the mission had been planned. A few weeks later the mission had been adapted to the new environment, and the satellite began operation, working correctly until 25 August 1993 when the mission controllers in the ESA command centre at Darmstadt decided to put it out of action after a series of problems with the guidance system and on-board computer.

Aim of the Mission

The objective of the mission was to carry out a very high precision survey of the celestial sphere, involving observation of around 120 000 carefully selected stars spread evenly across the sky, with an accuracy for position measurements of $0 . 0 0 2 ^ { \prime \prime }$ . Apart from positions, the parallax of the stars on the programme was also to be obtained to a high degree of accuracy. Indeed, because of the importance of this parameter in relation to theories of stellar evolution, and in understanding the history of the Universe, these results were considered by many astronomers to be the most interesting. The main features of the results of the Hipparcos mission are summarised in Table 4.4, together with those of the complementary mission Tycho, which included a greater number of stars but with measurements to a lesser degree of accuracy.

The Hipparcos satellite was equipped with a modestly sized telescope, $3 0 \mathrm { c m }$ in diameter, which was nevertheless sufficient to observe stars down to magnitude

Table 4.4 Main features of the Hipparcos mission   

<table><tr><td></td><td>Main mission Hipparcos</td><td>Complementary mission Tycho</td></tr><tr><td>Number of stars</td><td>120000</td><td>1000 000</td></tr><tr><td>Maximum magnitude</td><td>12.4</td><td>11.0</td></tr><tr><td>Accuracy of positions</td><td>0.001&quot;</td><td>0.02&quot;</td></tr><tr><td>Accuracy of speeds</td><td>0.001&quot; per year</td><td>二</td></tr><tr><td>Accuracy of parallax</td><td>0.001&quot;</td><td>1</td></tr><tr><td>Accuracy of magnitude</td><td>0.001 mag</td><td>0.01 mag</td></tr></table>

12.5. Stars were observed simultaneously in two directions at an angle of 58 degrees to each other, and their images formed in the focal plane of the instrument on an analysing grating composed of 2 688 slits of period $1 . 2 0 8 ^ { \prime \prime }$ , the transparent part comprising $39 \%$ . The field of view was $0 . 9 ^ { \circ } \times \ : 0 . 9 ^ { \circ }$ and, on average, two stars were visible in each of the two directions. The detector located behind the grating analysed the intensity fluctuations recorded when the stellar images were displaced across the grating, these displacements being the result of an extremely regular rotational movement of 167 degrees per hour imposed on the satellite.

Hipparcos was a scanning satellite whose mission had been completely planned and optimised before the launch. In order to ensure that the survey would cover the whole sky, observing all 120 000 stars on the programme and each of those at thirty different epochs, the exploration of the celestial sphere had to follow a welldefined rule. Owing to its rotation, the stellar images moved across the analysis grating, thereby modulating the light received by the detector placed just behind the grating.

By analysing the signal received when a star crossed the grating, the position of the centre of the image could be determined within a slit of the grating, at any precise moment (at least, in the case of a non-multiple star). This was an entirely local measurement within the reference system of the instrument. It was already very accurate, to around $0 . 0 1 5 ^ { \prime \prime }$ for a magnitude 9 star.

The signal was then expanded in two harmonics

$$
I ( t ) = I + B + I \left[ M \cos ( \omega t + \phi ) + N \cos ( 2 \omega t + \psi ) \right] ,
$$

where $I$ is the intensity in $\mathrm { H z }$ and $B$ is the non-modulated part of the signal, including, among other things, the stellar background noise. $M$ and $N$ are the modulation parameters with typical values, for a non-multiple star, of 0.7 and 0.25, respectively. The phases $\phi$ and $\psi$ of the two harmonics characterised the position of the image on the grating at the moment under consideration. The positions on the grating were determined, every $2 . 1 3 \mathrm { s } .$ , for all stars within the field of view of the instrument. The determination was repeated for each star during the $1 9 \mathrm { s }$ it took for its image to cross the grating. The two amplitudes were used for the photometric catalogue and variable star survey.

As a consequence of the way the satellite scanned the sky, all the information collected over a period of $1 0 \mathrm { h }$ (approximately one orbit) relates to stars very close to a single great circle of the celestial sphere. As a result, the abscissæ of around 1 500 stars were determined on the circle. Repeating the operation for each orbit of $1 0 . 7 \mathrm { h }$ , over a period of 37 months, produced 2 500 circles of 1 500 stars, and hence an average of $( 2 5 0 0 { \times } 1 5 0 0 ) / 1 2 0 0 0 0 { = } 3 1$ observation epochs per star.

 DAfter processing, this delivered an astrometric solution giving the position, parallax, and two components of the proper motion of each star on the programme. About 20 000 objects were detected as multiple systems and further processing was carried out to resolve the components whenever possible. The final accuracy for a star of magnitude 8.5 of the Hipparcos catalogue is $0 . 0 0 1 ^ { \prime \prime }$ for position and parallax and $0 . 0 0 1 ^ { \prime \prime }$ per year for proper motions, and about twice these values for stars of magnitude 11. The catalogue was published by the ESA in 1996, with all its appendices relating to multiple systems and photometry. Fifteen years on, Hipparcos remains the ultimate reference among fundamental catalogues in astronomy and has been used, with its complement Tycho covering some 2 million stars, as a reference to construct fainter and denser catalogues.

In particular, the CCD Astrograph Catalog of the US Naval Observatory in Washington (UCAC), complete up to magnitude $R ~ = ~ 1 6$ , gives the astrometric Dpositions in the Hipparcos system of more than 50 million stars with accuracies ranging from 20 to 70 mas depending on the magnitude. It is without doubt the most important recent contribution to astrometry since Hipparcos and the first CCD survey in this domain. It was achieved in a few years using an astrograph placed for three years in the southern hemisphere, then two years in the northern hemisphere to complete the programme based on observations made between 1998 and 2004. The latest version, UCAC-3, has been released in 2009 and a new version (UCAC-4) is in its final stage for a release in 2012.

# Relating to the Kinematic Reference System

As a consequence of the observation method, the solution is invariant under rotation, and the Hipparcos system would be rotating freely relative to the inertial system if this were not avoided by attaching it to the inertial system. This can be visualised by considering the Hipparcos catalogue as being made up of a very large number of arcs, of perfectly determined dimensions, joining all 120 000 stars on the programme. Clearly, there will be only one way to position the stars relative to each other whilst satisfying all the constraints imposed by these arcs, and this will leave just the degrees of freedom for the rotation of a solid. As the stars have proper motion, the rotation mentioned will be variable in time, and this implies a total of six parameters required to fix the Hipparcos sphere relative to the extragalactic system of reference.

At any moment $t$ , consider a source common to the two systems, with unit vector $X ( t )$ in the kinematic system and $X ^ { \prime } ( t )$ in the Hipparcos system. Then there exists some rotation $\mathsf { R } ( t )$ such that

$$
X ^ { \prime } = [ \mathsf { R } ] X .
$$

This equation holds for all $t$ and, when linearized in this variable, breaks into two subsystems for values of $t$ near the reference epoch $t _ { 0 }$ :

$$
\begin{array} { r l } & { X ( t ) = X _ { 0 } + V ( t - t _ { 0 } ) , } \\ & { X ^ { \prime } ( t ) = X ^ { \prime } \circ + V ^ { \prime } ( t - t _ { 0 } ) , } \\ & { \mathsf { R } = \mathsf { R } _ { 0 } + \mathsf { S } ( t - t _ { 0 } ) , } \end{array}
$$

whence, by identification,

$$
\begin{array} { l } { { X ^ { \prime } \mathrm { _ 0 = \left[ R _ { 0 } \right] } X \mathrm { _ 0 , } } } \\ { { V ^ { \prime } = \left[ \mathsf { R } \mathrm { _ 0 } \right] V + \left[ \mathsf { S } \right] X \mathrm { _ 0 . } } } \end{array}
$$

As the rotation $\mathsf { R }$ is through only a few tens of mas, it can be decomposed in terms of three infinitesimal rotations $( \alpha , \beta , \gamma )$ about the coordinate axes:

$$
\mathsf { R } _ { 0 } = \left[ \begin{array} { c c } { 1 } & { \gamma } & { - \beta } \\ { - \gamma } & { 1 } & { \alpha } \\ { \beta } & { - \alpha } & { 1 } \end{array} \right] , \qquad \mathsf { S } = \left[ \begin{array} { c c c } { 0 } & { \dot { \gamma } } & { - \dot { \beta } } \\ { - \dot { \gamma } } & { 0 } & { \dot { \alpha } } \\ { \dot { \beta } } & { - \dot { \alpha } } & { 0 } \end{array} \right] .
$$

Knowing the values of $X ^ { \prime } { } _ { 0 }$ ; $V ^ { \prime }$ and $X _ { 0 }$ ; $V$ , the values of the six rotation parameters can be found by a method of least squares, so that the Hipparcos solution can finally be expressed in the extragalactic frame.

In the case of Hipparcos, the objects common to the two systems were not the quasars of the kinematic system, too faint to be observed by Hipparcos, but rather a dozen or so compact radio stars that were sufficiently bright at both optical and radio wavelengths. A specific VLBI observation programme, over a period of nearly ten years, has made it possible to fix these objects in the kinematic system, and to measure their proper motion in that system. Moreover, these stars were high priority candidates of the Hipparcos programme, and were observed as often as possible. Once the residual rotation had been calculated, it only had to be applied to the whole solution to produce the final catalogue. This optical realisation of the celestial reference system was adapted by the IAU in 2000 and called the Hipparcos Celestial Reference Frame (HCRF). It contains all the non-multiple stars of the Hipparcos catalogue.

# 4.2.5 The Near Future: The Gaia Mission

# Introduction

Hipparcos was related to the ICRF but was not itself able to produce an independent realisation since it could not observe sources fainter than $V ~ \simeq ~ 1 3$ , i.e., it was 'only able to observe a single ICRF source. Following the success of this mission, many similar projects were put forward. The simple fact of replacing a photoelectric detector with total efficiency of the order of 0.004 by a CCD led to a gain of several magnitudes and considerably increased the size of the catalogue. In every case, the missions, proposed by American, German, or European scientists in the ESA, opted for the Hipparcos two-field observation principle with a scanning satellite. This was necessary in order to achieve absolute astrometry, even if the priorities for these missions were astrophysical.

In the end, only the Gaia mission stood out, and was finally selected by the European Space Agency for launch in 2013. The scientific objectives are very broad in the areas of stellar and galactic physics, fundamental physics, and detection of exoplanets, and in addition to astrometry, a complete photometric study over about thirty spectral bands and spectral measurements for objects with $V ~ < ~ 1 6$ . Considering only the astrometry, Gaia should carry out a full survey of the sky up to magnitude 20 with an astrometric accuracy of $2 5 \mu \mathrm { a s }$ at $V = 1 5$ . The number of objects surveyed will be of the order of $1 0 ^ { 9 }$ Dover the 5 years of the mission. Concerning the astrometric aspects of the mission, there is no great difference with the principles underlying Hipparcos. However, the following points should be noted:

There is no observation programme based on a previously established star list, as was done for Hipparcos. Gaia has its own autonomous system for detecting sources passing through the field of the instrument, and every detected source is observed and recorded on CCDs.   
There are two large telescopes $( 1 . 4 5 \times 0 . 5 0 \mathrm { m } ^ { 2 }$ ) and the beams are combined before focusing on a single focal plane. Detection and measurements occur on about 110 CCDs $( 4 . 5 \mathrm { k } \times 2 \mathrm { k } )$ with a pixel $1 0 \mu \mathrm { m }$ long in the scanning direction. The angle between the two fields is $1 0 6 . 5 ^ { \circ }$ as compared with $5 8 ^ { \circ }$ for Hipparcos. In practice, this difference is of no particular importance, provided that the angle is large enough and bears no simple ratio with 360. Gaia will be placed at the L2 point of the Sun–Earth system, at a distance of 1.5 million km from Earth in the Sun–Earth direction.

# Realisation of the Reference System

In contrast with Hipparcos, Gaia will be able to observe the extragalactic sources of the ICRF and many other quasars. The typical density of quasars brighter than $V = 2 0$ in the visible is of the order of 20 sources per square degree. That gives Dabout 800 000 sources across the whole sky, of which half are well outside the galactic plane. This is roughly the number of sources that Gaia should detect and measure. By restricting to sources brighter than $V \sim 1 8$ , that gives about 30 000 extragalactic sources that can be used to build up a realisation of the reference system.

Most of these sources are not identified as quasars today, and a recognition system will combine photometric and astrometric properties (there is no significant parallax for a quasar and its proper motion should be very small or non-existent). It will be possible to produce a sample without stellar contamination. The astrometric solution will be constrained to have no overall rotation (ICRS paradigm) and the origin of the system will be fixed on the basis of the present ICRF solution, still with the aim of ensuring continuity with metrological references.

If the set of quasars has an overall rotation $\omega$ in the initial Gaia solution (this will occur because the observing system is invariant under rotation, exactly as for Hipparcos), this will be reflected in a systematic proper motion of the sources given by

$$
\begin{array} { c } { { \mu _ { \alpha } \cos \delta = \omega _ { x } \sin \delta \cos \alpha + \omega _ { y } \sin \delta \sin \alpha - \omega _ { z } \cos \delta , } } \\ { { \nonumber } } \\ { { \mu _ { \delta } = - \omega _ { x } \sin \alpha + \omega _ { y } \cos \alpha . } } \end{array}
$$

The observed proper motions can therefore be adjusted to recover this rotation and eliminate it from the solution.

The system provided by Gaia will constitute a new primary realisation of an ICRF satisfying the specifications of the ICRS and directly accessible in the visible for optical and near infrared astronomy. It is estimated that the residual rotation relative to the diffuse cosmic background will not exceed $0 . 3 \mu \mathrm { a s } / \mathrm { y r }$ , whereas for Hipparcos the uncertainty is 0.25 mas/yr. Note that, when eliminating the overall rotation, one must simultaneously determine the acceleration of the Solar System as a whole relative to distant sources, and this will reveal the rotation of the Galaxy.

# 4.3 Temporal Reference Systems

# 4.3.1 Time Scales

Constructing a temporal reference system, that is, a time scale together with a basic unit, involves the same steps as for spatial frames: to begin with, the idea of quantifying which, applied to time, has provoked much discussion between scientists, philosophers, and psychologists; then the definition based on the laws of physics and observable quantities; and, finally, the practical realisation of one or several concrete systems, subject to revision and improvement. It is paradoxical that, although the first step, establishing the very concept itself, remains in an unsatisfactory state — What is time?10 — the measurement of time and frequencies should have become, in a few decades, the most precise in the whole of physics and continues to improve rapidly with the advent of cold atomic clocks on the one hand and optical standards on the other (Table 4.5).

Since 1967, the definition of time has been in the hands of physicists rather than astronomers, thus ending a tradition many centuries long. However, one of the two major astronomical almanacs, published by the Institut de M´ecanique C´eleste et de Calcul des Eph´em´erides (IMCCE) under the auspices of the Bureau des Longitudes in Paris, still has the same name that it has carried since its foundation: La Connaissance des Temps. This should serve to remind us that, even though astronomers are no longer the keepers of the unit of time, the definition and practical realisations of this quantity are still of the utmost importance to them. There are at least two reasons:

Table 4.5 The evolution of time scales   

<table><tr><td>Epoch</td><td>Physical phenomenon</td><td>Definition of the second</td><td>Scale of time</td></tr><tr><td>Before 1960</td><td>Rotation of the Earth</td><td>1/86 400 of the mean solar day</td><td>Universal Time (UT)</td></tr><tr><td>1960-1967</td><td>Orbital motion of the Earth</td><td>1/31 556 925.974 7 of the 1900.0 tropical year</td><td>Ephemeris Time (ET)</td></tr><tr><td>1967</td><td>Transition between two atomic levels</td><td>9 192 631 770 transition periods of Cs 133</td><td>Atomic time scale</td></tr><tr><td>1971</td><td></td><td></td><td>Atomic time scale of BIH (then BIPM) becomes International Atomic</td></tr></table>

• In every step of its development, celestial mechanics has used the uniform time of Newton, or one of its close relatives imposed by a choice of coordinates in the relativistic theory of gravitation, as argument for its theories; and it is indeed the same argument which is found in the tables of the almanacs. Given that the latter will be used either to compare observation with calculation, or to prepare for further observation, this argument must be defined as fittingly as possible, and its relations with commonly-used time scales determined. The SI second and the international atomic time scale were only introduced in 1967. The first caesium clocks date from the 1950s. Before these times, it is not possible to date events relative to the new scales and one must resort to some sort of astronomical time scale. The earliest observations were expressed in solar time, whence the need to keep some trace of this time scale, and its relation to the time of the almanacs, which is, so it would seem, a good extrapolation of international atomic time into the past.

Until the beginning of the twentieth century, the determination of time was entirely based on the assumption that the Earth’s rotation rate about its axis was constant. The second was by definition a perfectly specified fraction of the mean solar day. However, observations of the Moon and planets, together with studies of past eclipses, threw doubt on the principle of invariability of the Earth’s rotational speed. In the 1930s, seasonal variations were found and also apparently unpredictable periods of acceleration and deceleration, reaching several thousandths of a second per day.

As a consequence, astronomers gradually abandoned the Earth’s rotation as fundamental standard, switching to the motion of the Earth around the Sun and hence redefining the second, although maintaining continuity with the old definition as far as possible. The new scale of time, ephemeris time, had all the qualities of uniformity required, but it was less accessible, due to the apparent slowness of the Sun’s motion and the difficulty of the measurements involved. Very soon, it was realised physically by the motion of the Moon, theoretical constants being adjusted to ephemeris time. Unfortunately, the theory for the Moon is much more complicated than for the Sun, including dissipative terms which we are still unable to model correctly.

By the middle of the 1950s, the first laboratory frequency standards had appeared, based on very high frequency atomic transitions which, because of their stability and accessibility, were soon adopted in favour of astronomical phenomena as the more suitable for the construction of a uniform time scale. Finally, in 1976, with the guidance of the International Astronomical Union, several scales of time were defined, taking into account relativistic effects on clocks due to position and motion of the observer in the neighbourhood of the Earth or the centre of mass of the Solar System. The relation between these scales and atomic time is still the subject of much discussion, although it is generally agreed that they are necessary. The history of the successive definitions of the second is summarised in Table 4.5.

At this point we define some standard terms used when speaking about time scales.

# Apparent Solar Time and Mean Solar Time

The apparent solar time at a given place and a given instant, is the hour angle of the Sun at that place and time. When compared to the uniform time of the mechanical model, it manifests periodic variations included in the so-called equation of time. The latter contains the equation of centre describing the effects of eccentricity of the terrestrial orbit, the reduction at the equator due to the inclination of the ecliptic to the equator, and variations in sidereal time due to precession and nutation. During the year, its amplitude never increases beyond $2 0 \mathrm { { m i n } }$ .

Mean solar time is the apparent solar time with adjustment made for all the periodic terms affecting the motion of the Sun in right ascension. It would be a linear function of the uniform time of mechanics, were it not for variations in the Earth’s rotation.

Let $t$ be ideal Newtonian time and $T$ and $T _ { \mathrm { t r u e } }$ its realisations by mean solar time and true solar time, respectively. By definition, $T _ { \mathrm { t r u e } } = H _ { \odot }$ with a scale factor to transfer angles to units of time. We then have

$$
\begin{array} { r } { H _ { \odot } = \alpha _ { z } - \alpha _ { \odot } , } \end{array}
$$

and for the average values with periodic effects removed,

$$
\begin{array} { r } { \langle H _ { \odot } \rangle = \alpha _ { z } - \langle \alpha _ { \odot } \rangle , } \end{array}
$$

or again,

$$
\begin{array} { r } { H _ { \odot } - \langle H _ { \odot } \rangle = \langle \alpha _ { \odot } \rangle - \alpha _ { \odot } . } \end{array}
$$

So the differences appearing in the true solar time are exactly those featuring in the motion of the Sun in right ascension. Let

$$
E = \alpha _ { \odot } - \langle \alpha _ { \odot } \rangle = \langle H _ { \odot } \rangle - H _ { \odot }
$$

denote all the periodic terms in the right ascension of the Sun. This expression has been called the equation of time for more than two centuries, a name that aptly expresses its origin (see Fig. 4.12).

From the properties of the elliptical motion and the reduction at the equator discussed above, we find

$$
E = 2 e \ \sin \ M - \tan ^ { 2 } { \frac { \varepsilon } { 2 } } \sin 2 ( \varpi + M ) + O ( e ^ { 2 } , \varepsilon ^ { 4 } ) ,
$$

where $e ~ = ~ 0 . 0 1 6 7$ is the eccentricity of the Earth’s orbit, $M \ = \ n t$ the mean Danomaly throughout the orbit, and $\varpi \ : = \ : 2 8 2 ^ { \circ }$ Dthe longitude of the periastron of the orbit. Finally, $n = 0 . 9 8 5 6 ^ { \circ } / \mathrm { d a y }$ D is the mean motion of the Sun. The equation Dof time thus includes an annual term and a term of period six months. Taking into account higher order terms for the amplitudes, we have in minutes

$$
E = 7 . 7 \sin { M } - 9 . 8 \sin ( 2 0 4 + 2 M ) .
$$

With the sign convention adopted for $E$ (there is no commonly accepted convention and the sign depends on the source and national preferences), if $E > 0$ , the true Sun is ahead of the mean Sun in right ascension, whence true noon (when the Sun passes the local meridian, i.e., noon for a sundial) occurs later than $1 2 \mathrm { h }$ mean time for this location. Since our official time is close to the mean time of a reference meridian, there is still one correction to be made to the longitude in order to read official time from a sundial.

![](images/0a2332fa1b38fba8b085f3a35842d9573f235c14b60a2f6363a3258fea261245.jpg)  
Fig. 4.12 Values of the equation of time and its two main components during the year

# Civil Time and Universal Time (UT)

The civil time in a certain place is the mean solar time plus twelve hours which are added so that the day begins at midnight and not at midday. Universal time is the civil time of the international meridian. The civil time in a given place should not be confused with the official time in the corresponding country. This official time is fixed by the administration of the country and, in general, differs from universal time by a whole number of hours (except in a few cases where there may be a difference of half an hour).

# 4.3.2 Atomic Time

# Frequency Standards

During the second world war, the development of radars led to considerable improvements in the technology of microwave circuits and high-frequency cavities. These cavities could be controlled sufficiently accurately to correspond to atomic and molecular transition frequencies in the centimetre range. In 1948, the U.S. Bureau of Standards was able to use a cavity adjusted to the transition frequency of ammonia. The ammonia molecules were excited and returned to the ground state by emission of a photon; the intensity of the observed signal increased as the cavity frequency approached the transition frequency of the ammonia molecule.

It thus became possible to tune the cavity to the ammonia transition frequency by a feedback loop, thereby creating a frequency regulator: if the radiofrequency of excitation of the cavity differed somewhat from the absorption frequency of the ammonia molecule, the output signal would weaken. The excitation frequency of the cavity was then altered until it approached the transition frequency of $2 3 8 7 0 \mathrm { M H z }$ .

It turns out that the transition resonance of ammonia molecules is extremely narrow compared with those of classical oscillators, and therefore, it is only for an excitation radiofrequency almost exactly equal to the ammonia transition frequency that any significant number of molecules will undergo stimulated transition. This is one of the main features contributing to the success of atomic frequency standards.

# The Caesium Clock

The same principles were applied to atoms, and in particular, to $\mathrm { C s } \ 1 3 3$ . This atom contains 55 protons, 78 neutrons and, of course, 55 electrons. The outer electron is not paired and has zero orbital angular momentum. The ground state of $\mathrm { C s } \ 1 3 3$ has a two-state hyperfine structure coming from the interaction of the spin of the outer electron $S = 1 / 2  ,$ with the angular momentum $( J = 7 / 2 )$ ) of the nucleus. D DThe angular momentum addition rule is straightforward in this case, leaving only two possibilities: if the angular momenta are parallel, the total angular momentum is $F = 4$ , and if they are anti-parallel, it has value $F = 3$ . A photon of frequency $\nu _ { 0 } \sim 9 \mathrm { G H z }$ D is emitted when spontaneous transition from $F = 4  F = 3$ occurs.

 D ! DIn 1950, H. Lyons and his colleagues at the National Bureau of Standards measured the frequency of the $F = 4  F = 3$ transition of $^ { 1 3 3 } \mathrm { C s }$ (in terms D ! Dof the SI second as it was then defined) to a relative accuracy of $1 0 ^ { - 7 }$ . This was still not precise enough to challenge the astronomical standards. Then, in June 1955, L. Essen and J.V.L. Parry of the National Physical Laboratory in the UK produced the first caesium frequency standard worthy of the name, reaching an accuracy of order $1 0 ^ { - 1 0 }$ . From 1955 to 1958, the National Physics Laboratory and the Naval Observatory in Washington carried out a joint experiment to determine the relation between the transition frequency of caesium and the second of ephemeris time. They found a value of $9 1 9 2 6 3 1 7 7 0 { \pm } 2 0 \mathrm { H z }$ (in ephemeris seconds), the error originating ˙rather from the quality of the determination of ephemeris time than from inability to read the frequency. From then on, it became possible to compare two frequencies with an accuracy of $1 0 ^ { - 1 2 }$ . The moment had come to consider replacing celestial standards in favour of some system based on laboratory clocks.

At the thirteenth General Conference on Weights and Measures (Conf´erence G´en´erale des Poids et Mesures CGPM), a new definition of the second was adopted, which became the SI unit in 1967:

One second is the duration of 9 192 631 770 periods of the radiation corresponding to the transition between the two hyperfine levels of the ground state of the $^ { 1 3 3 } \mathrm { C s }$ atom.

The practical realisation of the international second by means of an atomic standard turned the latter into a frequency standard, whereas previously it had only been a frequency generator. It became a time standard through the counting of periods. Figure 4.13 shows how an atomic standard works. A source, heated to around $1 0 0 ^ { \circ } \mathrm { C }$ , produces a beam of caesium atoms about equally distributed between the $F \ = \ 4$ and $F ~ = ~ 3$ states. An intense inhomogeneous magnetic field removes Datoms in the $F = 3$ state, so that only those in the $F = 4$ state enter the cavity. DA hyperfrequency field at frequency $\nu$ very close to $\nu _ { 0 }$ Dcauses stimulated emission, returning atoms to their $F ~ = ~ 3$ ground state and emitting photons at frequency $\nu ~ = ~ \nu _ { 0 }$ D. At the other end of the cavity, a second magnetic sorting once again Dseparates those atoms remaining in the $F = 4$ state from those having undergone a transition to the $F = 3$ Dstate. After ionisation, the current obtained is used to control Dthe cavity frequency, via a quartz oscillator and a feedback mechanism.

Specialised laboratories construct caesium frequency standards with a view to improving the realisation of the second, that is, aiming to establish ever greater accuracy. These standards, realised today by means of cooled caesium and rubidium atomic fountains, are accurate to within $1 0 ^ { - 1 6 }$ . Standards of this type are developed at the Paris Observatory and at the NIST laboratories in Boulder. Furthermore, slightly less accurate caesium jet clocks available from manufacturers are nevertheless accurate to between 1 and $2 \times 1 0 ^ { - 1 2 }$ , which is quite remarkable.

![](images/7f5f9f42be0f66445ac89a284d738dde968624a1489352ecf8ea252803e3df6a.jpg)  
Fig. 4.13 Operating principle of the caesium frequency standard

# Definition of International Atomic Time (Temps Atomique International TAI)

The frequency standard can be used cumulatively to construct a continuous scale of time, insofar as the clock or clocks which realise this scale operate continuously. A definition was proposed in 1970 by the Consultative Committee for the Definition of the Second (Comit´e Consultatif pour la D´efinition de la Seconde CCDS) and approved in the same year by the International Committee for Weights and Measures (Comit´e Internationale des Poids et Mesures CIPM). Finally, in October 1971, the 14th General Conference on Weights and Measures (Conf´erence G´en´erale des Poids et Mesures CGPM) defined the new temporal reference system, international atomic time:

International atomic time is the temporal reference coordinate established by the Bureau International de l’Heure on the basis of the indications of atomic clocks operating in various establishments in conformity with the definition of the second, unit of time of the Syst\`eme International d’Unit´es.

The Bureau International de l’Heure applied this definition and constructed a time scale cumulatively from SI seconds. Unlike the dynamical scales based on arbitrary division of the scale associated with some flow of events, the TAI is an integrated time scale.

There were at least two possible ways of achieving this international atomic time scale:

• Select one particular clock, a very high quality caesium standard clock, in permanent operation, whose readings would be, by definition, the practical realisation of the TAI.   
Establish the TAI scale by coordinating, in one centre, the readings of a wideranging network of clocks in several laboratories. The TAI is then calculated from this data using a well-defined algorithm.

The first solution, although simple (TAI fixed by one clock, in one place), was obviously open to the risk of a discontinuity, in the event of operating problems or even total failure of the standard clock, which could never guarantee anything like the immutability of the celestial movements. The second solution, which was finally the one adopted, almost completely eliminates this risk, and furthermore, the large set of readings provides for a statistical improvement. The readings of the 260 participating clocks are weighted according to the quality of each clock and submitted to an algorithm.

Today, production of the TAI is handled by the International Bureau of Weights and Measures (Bureau International des Poids et Mesures BIPM), following the transfer, in 1985, of the time section of the Bureau International de l’Heure (BIH) from the Paris Observatory to the BIPM. (In 1987, the BIH was split into two organisations: the International Earth Rotation Service (IERS), which is still at the Paris Observatory; and the Time Section of the BIPM in Sevres, near Paris, which\` deals with construction of the TAI scale and maintenance of the SI second.)

Given the TAI scale, we might be tempted to speak of a TAI second which, if we were not careful, could differ from the second of the Syst\`eme International d’Unit´es (SI second). In order to deal with this potential weak point, the frequency of the TAI is determined from primary frequency standards at the National Research Council (Canada) and at the Physikalisch-Technische Bundesanstalt (Germany). To give an example, the relative value of the frequency of the TAI was reduced by $1 \times 1 0 ^ { - 1 2 }$ on 1 January 1977. With these precautions, the stability of the TAI lies somewhere between 1 and $5 \times 1 0 ^ { - 1 4 }$ over periods of one month to several years. The TAI second is coherent with the SI second at the level of $2 \times 1 0 ^ { - 1 4 }$ .

# 4.3.3 Coordinated Universal Time (CUT or UTC)

As the atomic time scale is quite independent of the celestial movements, it follows that the mean solar day is not exactly 86 400 TAI seconds. The length of the mean solar day was equal to approximately 86 400 SI seconds in 1820. It was shorter before, and since then has been increasing all the time to reach 86 400.0025 SI seconds around 1980. These $\approx 2 . 5$ ms per day accumulate during the year to give a typical annual shift of approximately 1 s between a uniform scale and a scale constructed on the basis of the Earth’s rotation. It is this second that is adjusted from time to time to maintain the relationship with the Earth’s rotation. Even if the duration of the second in the definition had been adjusted, agreement at one particular instant would soon be lost as a result of irregularities in, and the secular slowing of, the Earth’s rotation. It was indeed this very same phenomenon, and in particular its unpredictability, which led to the abandoning of the Earth’s motion as a source for a uniform time.

However, when the transition was made from astronomical standards of time to atomic standards, it was considered useful not to completely forego the close connection between time and the Earth’s orientation in space. For this reason, a scale of time called coordinated universal time was created (officially denoted UTC). This is a hybrid, possessing the uniformity of atomic time, at least, piecewise, but undergoing one second discontinuities whenever necessary in order to keep the Earth’s rotation in phase with laboratory clocks. In brief, UTC is an approximation to mean solar time, but read on a much better time-keeper than the Earth’s rotation (see Fig. 4.14).

Having converted the Earth’s rotation into a time scale known as UT1, the following relations hold after 1 January 1972:

$$
\mathrm { T A I } - \mathrm { U T C } = n \mathrm { ~ s ~ } \quad ( n \in \mathbb { Z } ) ,
$$

$$
| \mathrm { U T 1 - U T C } | \leq 0 . 9 \mathrm { s } .
$$

![](images/2ac76b5158c0b0732a8575b9711bf228fb3eabe8eae9e2f04e26ecf507b2937a.jpg)  
Fig. 4.14 Difference between TAI and UTC from 1972 to 2011

Depending on how urgent it is, the leap second is placed at the end of December or June, or at the end of any month, and announced at least eight weeks beforehand. The exact relation between UT1 and UTC can only be known after the event, when measurements of the Earth’s rotation, using space geodesy, laser–Moon telemetry, and very long baseline interferometry, have been published. The question here is no longer one of time metrology, but rather a study of the Earth’s orientation in space, a prerequisite for the preparation and processing of these observations since the time scale available in an observatory is usually UTC. The decision to introduce a leap second is taken by the central office of the International Earth Rotation Service (IERS).

# 4.3.4 GPS Time

Although this time scale does not enjoy a fully official existence in the world of metrology, it is nevertheless of considerable practical importance by virtue of its accessibility. Each satellite of the GPS constellation (Global Positioning System) carries one caesium and one rubidium atomic clock. The constellation comprises 28 operational satellites of the second generation. The network distributes a continuous time scale (the GPS time scale) which follows UTC to within $1 \mu \mathrm { s }$ , but without the leap seconds. It is the computational algorithm or software of the receiver that ensures the correct UTC display. GPS time coincides with UTC at the origin of its definition at $_ { \mathrm { 0 h } }$ on 6 January 1980. At this instant, TAI was ahead of UTC by $1 9 \mathrm { s }$ , and hence ahead of $T _ { \mathrm { G P S } }$ , as can be seen in Fig. 4.14. This value remains constant due to the servocontrol on TAI through a continuous UTC. Hence,

$$
\mathrm { T A I } - T _ { \mathrm { G P S } } = 1 9 \mathrm { s } .
$$

In 2011, the deviation from UTC reached 15 s (see Fig. 4.14), with

$$
T _ { \mathrm { G P S } } - \mathrm { U T C } = 1 5 \mathrm { s } \sin 2 0 1 1 .
$$

Galileo time should follow the same convention and deliver a continuous time that is rigidly linked to TAI. For the Russian system GLONASS, the leap seconds are included in the primary scale of the system, which is therefore tied to UTC (in fact, $\mathrm { U T C } + 3 \mathrm { h }$ , i.e., Moscow time).

# The Future of UTC

The future of UTC as a widely distributed and accessible time scale for civilian needs is under discussion by the relevant international bodies, including astronomers and geophysicists, and telecommunications and navigation organisations. The main problem with this time scale is the presence of discontinuities due to unpredictable leap seconds, requiring the tables to be updated in computer programs. Furthermore, some automatic systems are unable to integrate such leaps, and there are many problems relating to the dating of events that arrive during the leap second, with a non-negligible risk of ambiguity in the coding of the exact date.

Various solutions are under examination by working groups, including:

• maintenance of the current system, with an increasing number of leap seconds in the future owing to the lengthening of the day, suppression of the leap seconds which would allow the UTC scale to drift away from UT1, greater tolerance, leading to bigger but less frequent leaps, possibly combined with regular and predetermined leaps, a shift to another time scale which could be TAI or another scale linked to the GPS or Galileo.

But the most spectacular possibility arising during these discussions (with absolutely no chance of being realised) would be to change the definition of the second to maintain the approximate agreement of 86 400 seconds per mean solar day.

The secular relationship between civil time and the apparent motion of the Sun is a feature that few would be ready to abandon, and the groups supporting this point of view have certainly made themselves heard during the discussions. However, extrapolating into the future, what we know about the secular slowing down of the Earth’s rotation indicates that it would take over 2 000 years before the discrepancy between solar time and a uniform time without leap seconds reached one hour. It would then be easy to reset the clocks if that were judged necessary by means of a leap hour. This would not then be totally unlike the Gregorian reform of the calendar which removed 10 days between 4 and 15 October 1582.

At the time of writing (2011), the result of these discussions is not yet known, but it seems that the most likely outcome will be that leap seconds will be abandoned, and that the time distributed will be a scale strictly related to TAI, with a constant shift of a few tens of seconds. Another possibility is that the GPS or Galileo time scales will win through for purely practically reasons, with a constant relationship to TAI (which is already the case for all intents and purposes). After the transition from the astronomical definition of the second to the physical one in 1967, a new page in the measurement of time and its relationship with the celestial world will then be turned.

# 4.3.5 Dynamical Time Scales

# Ephemeris Time

Newton’s law and its application to the dynamics of the Solar System assume the existence of a uniform and absolute time at the very outset of the physical theory. Motion only being uniform relative to some particular time scale, it is clear that we cannot define uniform motion without first being in possession of some time scale which itself bears no relation to motion. The alternative adopted by Newton, and thereafter by the astronomical community, as a way of realising a dynamical time scale recognises uniform motion a priori by the absence of force, or a complete modelling of the forces in an inertial system. Thus, the choice of a theory of motion, and of the numerical constants required to completely define initial conditions, leads to an ephemeris, that is, a position vector $\mathbf { \boldsymbol { r } } \left( t \right)$ . Observation of the body gives the position $^ { o M }$ and the value of the parameter $t$ is found by solving the equation in $t$ , $O M = r ( t )$ . The definition of the unit is then some fraction of a well-defined Dinterval, such as the day or the year. This is quite the opposite of what happens for atomic time, where the scale is constructed by cumulating units, by integration, in some sense, whilst the unit of the dynamical scale is obtained by derivation.

Solar time and its close relative universal time are dynamical times based on a very simple model of the Earth’s rotational movement: $\omega =$ constant, which gives for the phase, the observable quantity, $\phi = \omega t$ D. This equation is so simple Dto invert that the nature of its terms (the angle as configuration parameter and time as independent variable) has become somewhat obscured, rather as happens in thermodynamics with temperature and energy, or in nuclear physics with the mass and energy of particles.

More important is ephemeris time (ET) and its modern derivatives, temps dynamique terrestre (TDT), temps terrestre (TT), temps dynamique barycentrique (TDB), and temps-coordon´ees barycentrique (TCB). Ephemeris time is realised practically by adopting a motion of the Sun by convention, such as the motion of the mean geometric longitude of the Sun, given by

$$
\langle L \rangle = 2 7 9 ^ { \circ } 4 1 ^ { \prime } 4 8 . 0 4 ^ { \prime \prime } + 1 2 9 6 0 2 7 6 8 . 1 3 ^ { \prime \prime } t _ { \mathrm { E } } + 1 . 0 8 9 ^ { \prime \prime } t _ { \mathrm { E } } ^ { 2 } ,
$$

where $t _ { \mathrm { E } }$ is measured in Julian centuries of 36 525 ephemeris days. The above expression was obtained using the best available theories and observations, with a time scale coming from the Earth’s rotation. Relative to the latter scale, the numbers appearing in the longitude expression are only known to a certain degree of accuracy. But as the source for a new time scale, the mean longitude is exact by definition, despite the experimental origin of its coefficients. Time $t = 0$ is defined as 0.5 January 1900 (31 December 1899 at $1 2 \mathrm { h }$ D), and the unit of time is a fraction of the tropical year at the same date, deduced from the value of the coefficient of $t _ { \mathrm { E } }$ . The observable event corresponding to $t _ { \mathrm { E } } ~ = ~ 0$ is $\langle L \rangle \ = \ 2 7 9 ^ { \circ } 4 1 ^ { \prime } 4 8 . 0 4 ^ { \prime \prime } \ =$ D h i D D279:696 678 deg and can be reconstructed from later measurements using the theory of the Sun.

As mentioned earlier, the practical realisation of this scale proved difficult and it was rapidly superseded when atomic time arrived on the scene. However, it remains an important scale for two reasons:

• Comparison with the TAI scale since 1955 has revealed no systematic difference between the two scales. This agreement is quite remarkable, relating a scale of time based on the laws of quantum mechanics, to another depending only on the laws of gravity. The discrepancy between the two scales is constant and given experimentally by

$$
\mathrm { E T } \approx \mathrm { T A I } + 3 2 . 1 8 4 \mathrm { s } .
$$

• Astronomical observations pre-dating the TAI (1955) are still much in use and can be dated with ET. Therefore, ET can be considered as an extrapolation into the past of the present scale of uniform time.

# Coordinated Time Scales

In 1976 and 1991, the International Astronomical Union made decisions leading to the introduction of other time scales based on the TAI but maintaining continuity with ET. Up until 1991, these scales went by the unfortunate names terrestrial dynamical time (temps dynamique terrestre TDT) and centre-of-mass dynamical time (temps dynamique barycentrique TDB), whereas their definition linked them to TAI without any reference to a dynamical ephemeris. In 1991, the time scales TT (temps terrestre or terrestrial time) and TCB (temps-coordonn´ees barycentriques or centre-of-mass coordinated times) were introduced. The following relations hold to a very high degree of accuracy:

$$
\begin{array} { c } { { \mathrm { T T } = \mathrm { T D T } = \mathrm { T A I } + 3 2 . 1 8 4 \mathrm { s } , } } \\ { { } } \\ { { \mathrm { T D B } = \mathrm { T D T } + \mathrm { P } , } } \end{array}
$$

where $\mathrm { P }$ is a series of about 500 periodic terms of amplitude greater than 0.1 ns describing relativistic differences between the running of a clock at the centre of mass of the Solar System and another in orbital motion on the orbit of the Earth. The main term has period one year and amplitude $1 . 6 5 6 \mathrm { m s }$ , whilst the second has amplitude $2 2 \mu \mathrm { s } .$ . Note that all these terms are essential in order to handle, without loss of accuracy relative to the measurements, the timing of millisecond pulsars.

These new definitions are justified by the requirements of a metrology of space and time conceived within the framework of relativistic gravitational theories, but also by the exceptional stability of atomic clocks and the availability of cold atom standards with stabilities on the ground of $1 0 ^ { - 1 6 }$ .

# 4.3.6 Dates and Epochs. Dealing with Long Periods

The system of astronomical constants fixed by the International Astronomical Union introduces a fundamental epoch to which all other events are related, using multiples or submultiples of a time unit.

Concerning time, the unit is the SI second, defined from the transition of $\mathrm { C s } 1 3 3$ and explained in Sect. 4.3.2. One day is $8 6 4 0 0 \mathrm { s }$ , one Julian year is $3 6 5 . 2 5 \mathrm { d }$ , and one Julian century is $3 6 5 2 5 \mathrm { d } .$ . These derived units are thus rigidly fixed relative to the SI second and depend in no way on the motions of celestial bodies, even though obviously chosen with reference to the solar day and the year of the seasons. Recall that the basic unit was, previously, the mean solar day divided into $8 6 4 0 0 \mathrm { s }$ , and later, some fraction of the tropical year 1900. The year was then the tropical year of 365.2422 d, which was the year of the seasons, bearing no relation to the Julian year.

Starting from these relatively short durations, ways have to be found to mark off the epochs over longer periods, thus making the calendar we are familiar with in everyday life to follow the years. However, this calendar, even though based on a very precise algorithm relating a calendar date with a precise day, does not allow for simple calculation of the time interval between two events such as $1 5 . 0 0 \mathrm { h }$ on 12 February 1853 and $8 . 0 0 \mathrm { h }$ on 15 January 2007. For the observation of many events such as eclipses, planetary motions, variable stars, supernovæ, and so on, not to mention the exploitation of archives from previous centuries, the astronomer requires a continuous reckoning of time which simplifies the evaluation of time intervals in the decimal system.

The solution consists in counting days on a counter which has sufficiently many digits to cover several thousand years. The method was suggested in 1606 by J. Scaliger who devised the term Julian period in memory of his father, Julius, and not through any connection with the Julian calendar. At each instant, the Julian date of an event is the number of days (including the decimal part) since midday on 1 January $- 4 7 1 2$ (4713 BC), the beginning of the Julian period. This origin results from Scaliger’s desire to return to the instant of time when the three fundamental cycles (the 15 year Roman indiction, the 19 year Meton cycle, and the 28 year Julian cycle) were simultaneously equal to 1. In this system for counting days, 1.5 January $2 0 0 0 = \mathrm { J D } 2 4 5 1 5 4 5$ and 1 January 2007 at $0 \mathrm { h } = \mathrm { J D } 2 4 5 4 1 0 1 . 5$ . For recent epochs, the modified Julian day is commonly used, $\mathrm { M J D } = \mathrm { J D } - 2 4 0 0 0 0 0 . 5 .$ , for which the origin is $_ { \mathrm { 0 h } }$ D on 17 November 1858. It should be remembered that the Julian day begins at $1 2 \mathrm { h }$ and not $_ { \mathrm { 0 h } }$ . The fraction 0.5 in the definition of the MJD is there precisely so that modified Julian days begin at $_ { \mathrm { 0 h } }$ . We can check that $1 5 . 0 0 \mathrm { h }$ on 12 February 1853 is JD 2 397 897.125 and that $8 . 0 0 \mathrm { h }$ on 15 January 2007 is JD 2 454 115.833, so that the time interval between the two epochs is $5 6 2 1 7 . 7 0 8 \mathrm { d }$ .

Even though the definition is clear, it assumes that we know how to count the days after a reference date, and also that the definition of the day throughout this period is unchanging. In practice, it is more convenient to work with a reference epoch called J2000, which corresponds to 1 January 2000 at $1 2 . 0 0 \mathrm { h }$ TDB (where $\mathrm { T D B } \approx \mathrm { T A I } + 3 2 . 1 8 4 s )$ and whose Julian date is $2 4 5 1 5 4 5 . 0 \mathrm { T D B }$ . Then every  Cevent is given by a Julian Epoch (JE) expressed by its Julian date (JED) as follows:

$$
\mathrm { J E } = 2 0 0 0 . 0 + \frac { \mathrm { J E D } - 2 4 5 1 5 4 5 . 0 } { 3 6 5 . 2 5 } .
$$

This date is written Jaaaa.aa, where aaaa.aa denotes the year in decimals. For example, 1 January 2007 at $0 . 0 0 \mathrm { h } = \mathrm { J D } 2 4 5 4 1 0 1 . 5$ gets transformed to Julian Depoch J2006.999315. Conversely, J2007.0 gives JD 2 454 101.75, i.e., 1 January 2007 at $^ { 6 \mathrm { h } }$ in the morning. An ordinary calendar date is transformed to its Julian date, or vice versa, by fairly simple algorithms available in basic astronomical works and computer libraries. In order to extend the validity of these algorithms to dates before the Gregorian reform, we must introduce the discontinuity in the calendar for the year of 1582 and take into account the change in the definition of leap years. The extension of the Gregorian calendar to a date prior to the reform is called the proleptic Gregorian calendar. In general, all historical dates are given relative to the calendar that was valid at the given date, so it is important to make clear mention if a date refers to the proleptic Gregorian calendar. Furthermore, since the date when the Gregorian calendar was adopted depends on the country (December 1582 in France), there are some uncertainties over dates coming from England, the United Provinces, and Germany up until the eighteenth century, and dates are often given in both forms.

Table 4.6 Correspondence between epochs, Julian dates, and calendar dates   

<table><tr><td>Besselian epoch</td><td>Julian epoch</td><td>Julian date</td><td>Calendar date</td></tr><tr><td>B1900.0</td><td>J1900.000857</td><td>2 415 020.3135</td><td>31/12/1899 19h31m 26s</td></tr><tr><td>B1950.0</td><td>J1949.999789</td><td>2433 282.4235</td><td>31/12/1949</td></tr><tr><td>B2000</td><td>J1999.998722</td><td>2 451544.4334</td><td>22h09 m 50s 31/12/1999</td></tr><tr><td>B1950.000210</td><td>J1950.0</td><td>2433 282.5</td><td>22h24m06s 1/01/1950</td></tr><tr><td></td><td></td><td></td><td>0h</td></tr><tr><td>B2000.001278</td><td>J2000</td><td>2 451545.0</td><td>1/01/2000</td></tr></table>

The reader may encounter other epochs in the literature, particularly in slightly older sources. These are reviewed in Table 4.6 to an accuracy of $\pm 2 \ : s$ . The epoch Bxxxx refers to a year equal to the tropical year of $3 6 5 . 2 4 2 1 9 8 7 8 1 \mathrm { d }$ , used in the astronomical constants until 1976, in particular for the theory of precession. For example, $0 . 0 0 \mathrm { { h } }$ on 1 January $1 9 9 5 = \mathrm { J D } 2 4 4 9 7 1 8 . 5$ corresponds to the Besselian epoch B1995.00048.

# Part II Data Collection

# Chapter 5 Telescopes and Images

The telescope is so often considered as the astronomical tool par excellence that it would be easy to forget that it is just one of the components of an observing system, and that it would serve no purpose without spectrometers or detectors. The aim of this chapter is first of all to examine the double function of the telescope: it must collect, then form an image of the source of that radiation. Naturally, these two aspects are very closely connected. It is to improve the performance of both that astronomers have always striven, and still strive, to build telescopes of ever increasing size, freeing them if necessary from the constraints of the Earth atmosphere by placing them in space. The close relationship between these functions means that the telescope stricto sensu is considered as just one element of an integrated system, whence the design of the telescope is intimately bound to the design of focal instruments such as cameras, spectrometers, and so on.

Image formation is such a central issue when using a telescope that we shall treat it here from the relatively simple viewpoint of geometrical optics, then discuss the limitations of this picture. This elementary approach will suffice to present the main features of instruments (telescopes) comprising a single primary mirror. Even though most of the ideas are quite general and presented, according to the basic principle of this book, independently of the wavelength under consideration, actual realisations of instruments are in fact highly dependent on the wavelength. We shall attempt to give as complete a presentation as possible of this rapidly evolving area, covering the full extent of the electromagnetic spectrum currently accessible to astronomical observation.

The study of the spatial coherence of radiation will be reserved for Chap. 6, along with the resulting theory of diffraction and image formation in the presence of diffraction. Several major applications will be described: the ultimate angular resolution of telescopes, aperture synthesis or coherent combination of several telescopes to form an array, and image degradation by the Earth atmosphere and ways of overcoming it.

Gravitational optics has recently become a promising branch of astrophysics. Although it does not involve the construction of optical systems in the classical sense of the term, the idea of a gravitational telescope rests upon principles which, at least in the simple cases, are very close to those of geometrical optics. This rapidly moving area will thus be included along with discussion of the more conventional aspects of geometrical optics.

# 5.1 Image and Object in Astronomy

The telescope is the instrument which produces an ‘image of the sky’ in order to identify and measure the energy received from space. But what exactly do we mean by this word ‘image’? Indeed, despite the three-dimensional structure of space, the terrestrial observer can only ever perceive a two-dimensional projection of it on the celestial ‘sphere’. The received intensity is the integral of the locally emitted energy, integrated along the line of sight. Unfolding the measured information, in order to reconstruct the local conditions at each point of the line of sight, involves the delicate operation of inverting the integral, an operation included within the more general category of inverse problems.

Throughout this chapter, the 2-component vector quantity $\pmb \theta$ denotes a point of the celestial sphere, which is to say, a direction characterised by two angles. Different reference frames can be used (horizontal, equatorial, galactic, etc.), and these are discussed in Chap. 8. It serves no purpose, in the present context, to specify the particular frame chosen to represent $\pmb \theta$ .

As seen by the observer, each angular direction $\pmb \theta$ in the sky is associated with a monochromatic flux (defined in Chap. 2) of frequency $\nu$ received by the observer:

$$
\begin{array} { r l } { I _ { \nu } ( \pmb \theta ) } & { { } \left[ \mathrm { W } \mathrm { m } ^ { - 2 } \mathrm { s r } ^ { - 1 } \mathrm { H z } ^ { - 1 } \right] , } \end{array}
$$

which can also be expressed in terms of a number of photons using

$$
N _ { \nu } ( \pmb \theta ) = \frac { I _ { \nu } ( \pmb \theta ) } { h \nu } \quad \left[ \mathrm { p h o t o n s ~ s ^ { - 1 } ~ m ^ { - 2 } ~ s r ^ { - 1 } ~ H z ^ { - 1 } } \right] .
$$

The distribution $I _ { \nu } ( \pmb \theta )$ is the monochromatic image or map of the observed region of the celestial sphere. The $\nu$ -dependence of this map describes numerous physical properties of the source: opacities responsible for absorption or emission by the source, correlation between phenomena of differing energies, excitation of atoms or molecules in the source, magnetic fields, and many others. The flux $I _ { \nu } ( \pmb \theta )$ may also depend on time (variable source) and the detected polarisation (polarised sources).

The observation process degrades $I _ { \nu } ( \pmb \theta )$ in at least four ways:

1. Through imperfections in the realisation of optical surfaces, which leads to geometrical aberrations, and the finite size of telescopes, antennas, and light gatherers used to collect the incident flux, which leads to diffraction. 2. Through the finite number of photons incident during the measurement time, which introduces measurement noise, and leads to imperfect restitution of $I _ { \nu } ( \pmb \theta )$ , relative to a measurement of infinite signal-to-noise ratio.

3. In the case of ground-based observations, through the consequences of crossing the Earth’s heterogeneous and turbulent atmosphere.

4. Through the existence of a finite spectral resolution $8 \nu _ { 0 }$ and a finite angular resolution $\ S \theta _ { 0 }$ , thereby mixing up radiation coming from different directions and having different frequencies.

In the case where $I _ { \nu } ( \pmb { \theta } ) = \delta ( \pmb { \theta } )$ , an intensity distribution characterising a point source, the domain $| \pmb { \theta } | < \ 8 \theta _ { 0 }$ in which the intensity is actually received determines j jthe angular resolution $\ S \theta _ { 0 }$ of the instrument. This notion of resolution, which is so important in analysing the capacities of an instrument, can also be defined when $I _ { \nu } ( \pmb \theta )$ is no longer studied in the space of values of $\pmb \theta$ , but rather in the Fourier conjugate space $w$ . Such is the case for the large group of instruments known as telescope arrays or interferometers (see Chap. 6).

# 5.1.1 The Telescope and Geometrical Optics

Geometrical optics provides the first approximation in telescope design.1 However many mirrors or lenses are used, the maximum energy collecting capacity is always determined by the aperture of the primary mirror or lens, the first optical element encountered by light from the source. This first element is generally followed by other optical elements (secondary or tertiary) which modify the position, the scale, or the quality of the primary image. At the end of the optical path is the focal plane of the telescope, where the final image is formed. This is the image which will be analysed by spectrometers, polarimeters, and other analysis systems, and/or light detection systems.

The aim of this optical configuration is to obtain, for a source located at infinity and for a given aperture, an image that is as anastigmatic as possible, over as wide a field as possible. The system is perfectly anastigmatic when all rays from a direction $\pmb \theta$ converge exactly to a single point $A ( \pmb \theta )$ in the focal plane of the telescope. If a system is approximately anastigmatic, the image is spread out, rays converging to some neighbourhood of $A ( \pmb \theta )$ whose dimension determines the quality of the image at $A$ . The field of the telescope is the region of the focal plane in which the image is sufficiently bright and sufficiently anastigmatic to fulfil the requirements of the instrument. It is clear that the larger the field, the better will be the use of the available photons and the observation time, with the proviso that the analysis and detection systems be capable of fully exploiting all points of this field.

The perfect anastigmatic surface for producing the image of a point at infinity on its axis, is the paraboloid of revolution. It is natural, therefore, that this should be the surface the most commonly used as primary mirror in telescopes. However, this surface used in isolation is not anastigmatic for any points off its axis, and therefore has no field, so it is equally natural that optical systems should be designed which incorporate more than one mirror. By increasing the number of degrees of freedom of the optical combination, these composite systems offer the best compromise possible between the approximately anastigmatic quality of the image, and the field, bearing in mind the requirements of the user. Nevertheless, it is much more expensive to polish a paraboloid than to polish a sphere, so spherical primary mirrors are sometimes used, with the unavoidable extra cost of then correcting for their aberrations.

![](images/d4bbdd3da77086aa47cfa360c4ab24c151fb73ceb3218ebc68c26b83d41fdd5a.jpg)  
Fig. 5.1 (a) Different focal configurations. Pointing of (b) equatorial and (c) altazimuth groundbased telescopes

# Optical Configuration of Telescopes

Figure 5.1 shows some of the most common configurations, used for both groundbased and spaceborne telescopes, and in very varied wavelength domains, whose design specifications will be described later. The figure shows the single mirror configuration (image at the prime focus), and configurations using two or more components (Cassegrain, Nasmyth, and Coude).´

The off-axis configuration is not shown in Fig. 5.1. In this setup, an aspherical primary mirror forms an image outside the incident beam, a method which avoids any obstruction by secondary or tertiary elements, but which is more complex and more costly to construct. We shall see interesting applications of this in Chap. 6.

The focal ratio, aperture ratio, or numerical aperture $f / D$ , where $f$ is the focal length (or equivalent focal length in the case of a combination of several mirrors) and $D$ the diameter of the pupil, is an important parameter in the design and use of a telescope. The prime focus configuration gives a small focal ratio (1.2–2.5), the Cassegrain and Nasmyth configurations give intermediate focal ratios (7–30), and the Coude configuration gives the largest focal ratios´ $( > 5 0 )$ .

The focal ratio of a single spherical mirror is directly related to its radius of curvature $R$ , since $f = R / 2$ . The construction of mirrors of comparable quality Dand large curvature, possessing values of $f / D$ only just greater than unity, leads to technical difficulties in polishing very open mirrors, but is nevertheless the result sought after. Indeed, for equal values of $D$ , smaller values of $f$ mean less cumbersome lengths, less couple on guiding equipment, reduced mechanical inertia, and a more favourable design generally.

The equivalent focal length, obtained after crossing or being reflected by all the optical surfaces in the system, also governs the scale of the image in the final focal plane. This scale, measured in millimetres per second of arc, is directly proportional to the value of $f$ :

$$
\mathrm { f o c a l ~ s c a l e } = 4 . 8 5 \times 1 0 ^ { - 6 } ~ f \quad \mathrm { m m a r c s e c ^ { - 1 } } ,
$$

where $f$ is in millimetres.

Optimal sampling of images aims to match the detector pixel size $a$ to the size of the element of angular resolution $\delta \theta$ :

$$
f 8 \theta \approx a ~ .
$$

Detectors with small pixels (e.g., photographic plates, or CCD with $a < 1 0 \mu \mathrm { m } ,$ ) can thus easily be placed at the prime focus. Even in this case, increasing diameters and the constant decrease in CCD pixel size often lead to oversampling. When the detector system requires or tolerates narrower beams, or accepts the use of an optical annex to modify the magnification of the image (focal reducer), the detector can be inserted at the Cassegrain or Nasmyth focus. This is the case for photometers, echelle spectrographs, or even Fourier transform spectrometers.

# Optical Aberrations

The compromise between image quality and field means that the image of a geometric point on the source is not a point. This phenomenon is called optical aberration. There are several methods for determining the aberrations of an optical system. In the light ray approximation (geometrical optics), computer ray tracing methods assume some shape for the optical surface (spherical, parabolic, or other aspherical surfaces, such as ellipsoids, hyperboloids or higher order surfaces), and then numerically simulate illumination from a point source $S$ in a given direction $\pmb \theta$ . The distribution of the impact points of the rays in the focal plane represents the energy distribution in the astigmatic image of $S$ , and can be assessed with respect to the allowed tolerance.2

A detailed analysis of aberration, or the methods developed by opticians to overcome it, will not be given here. These are classical topics which can be found in Born and Wolf, Principles of Optics, and also in Lunettes et T´elescopes by Danjon and Couder (Blanchard, Paris, 1983) (see the bibliography). A few remarks will suffice to illustrate the problem. Considering a set of rays coming from a point $A$ of the object and reaching the focal plane after passing through the telescope optics, they will be distributed about some point $A ^ { \prime }$ which would be the ideal image in the absence of any aberration. This scatter of a given ray around $A ^ { \prime }$ is basically a function of two variables. The first is the angular distance $\alpha$ between $A$ and the optical axis; the larger the angle $\alpha$ , which ranges over the field of the instrument, the greater will be the scatter. The second variable is the distance $r$ between the point of impact of the ray on the pupil and the centre of the pupil: the larger this distance is, the greater will be the scatter about $A ^ { \prime }$ . The parameter $\alpha _ { \mathrm { m a x } }$ thus determines the field of the instrument, whilst the maximal value of $r$ in keeping with the required image quality at $A ^ { \prime }$ will determine the maximal diameter $D$ .

The term field refers to the range of values of $\alpha$ such that the image quality there is acceptable. The fully illuminated field refers to that region over which the source $A$ can be displaced without the intensity of the image $A ^ { \prime }$ being reduced by obstructions due to intermediate diaphragms of the optical system. Beyond the fully illuminated field is a region known as the vignetted field, across which the illumination of the focal plane progressively decreases.

When a telescope is being designed, the problem is approached from the other end: first, $D$ and $\alpha _ { \mathrm { m a x } }$ are fixed, and then the optical arrangement (the shape and number of reflecting surfaces, etc.) is sought which best maintains the quality of the images $A ^ { \prime }$ within the angle $\alpha _ { \mathrm { m a x } }$ .

The five primary or Seidel aberrations are:

• Spherical aberration, which only depends on the value $r$ , that is, on the aperture $D$ . In other words, it only depends on the focal ratio $f / D$ of the focal length to the diameter, and is smaller as this ratio is greater, thus favouring narrow optical systems.   
Coma, which depends only on $\alpha$ and occurs even for very small values of $D$ , if $\alpha$ is non-zero.   
• Astigmatism and field curvature, which involve the values of both $f / D$ and $\alpha$ .   
• Distortion, which destroys geometrical similarity between object and image, whilst nevertheless maintaining a one-to-one correspondence between points of the object and points of the image.

Although useful, a study based upon geometrical optics is not sufficient to completely determine the image quality of an optical system, neglecting as it does the phenomenon of diffraction, caused mainly by the finite dimension of the pupils.

It should be added that the anastigmatic character of perfect optical surfaces is not the only factor bearing on image quality. Diffraction comes in again, since mirrors and lenses can never be perfectly polished, and this introduces a further cause of image degradation. This is observed when the size of irregularities on the optical surface becomes comparable with the wavelength of the light in the transverse direction, i.e., along the mirror surface, or in the perpendicular direction. This effect can be measured by quantifying the residual phase perturbations produced on the reflected or refracted wave. Suffice it to say in the present context that polishing defects smaller than the wavelength by a factor of 20 or more have a negligible effect on image quality. Such demanding criteria are commonplace in astronomy, so that only the five main types of aberration mentioned above need be taken into consideration.

One particular case is worth mentioning, however. A telescope, for example, at radiofrequencies, may have been optimised for observation at a certain wavelength $\lambda _ { 0 }$ , maybe in the decimetre or centimetre range. A later use at much shorter wavelengths $\lambda$ , maybe in the centimetre or millimetre range, will generally produce less good images, flaws in the optical path or phase with root mean square deviation $\sigma _ { \phi }$ , induced by reflecting surfaces, notably on the primary mirror, no longer satisfying the condition $\sigma _ { \phi } < \lambda / 2 0$ .

Constructing an instrument always involves a compromise between image quality (approximately anastigmatic) and the field within which this quality will be preserved. The right compromise can be found by taking the following steps: firstly, choosing the geometry of the surfaces (spherical, thus less costly, or aspherical); secondly, choosing the combination of individual components, a larger number offering more degrees of freedom and better optimisation, although at the risk of greater light loss, only partially compensated for by optimal treatment of the surfaces (high reflectivity of mirrors, anti-reflection dioptrics).

These considerations are illustrated in Fig. 5.2, which shows ray tracing by numerical simulation, a method universally used in studying the properties of optical systems. This is the result for a parabolic primary mirror with opening $f / 2$ , slightly deformed in a controlled manner (active optics), associated with an arrangement of three lenses (triplet corrector) close to its prime focus.

The description and analysis of optical aberrations, and likewise, the consequences of inadequately polished optical surfaces, provide a particularly convenient way of introducing a presentation of the local phase errors produced on a wavefront. This analysis cannot, of course, come from the theory of geometrical optics. The formalism of Zernike polynomials is invaluable in the study of general perturbations on wavefronts. In the present case, these perturbations are caused by imperfect or astigmatic optical surfaces, but they may well also be produced when a wave crosses some non-homogeneous medium, and indeed, it is in this context that they will be discussed (see Sect. 6.2).

# The Main Features of a Telescope and Its Optics

The principal parameters characterising a telescope and its optics are as follows:

1. The focal arrangement, illustrated in Fig. 5.1. Note that a single instrument can have several focal points; transformation from one to another simply requires insertion or removal of a mirror. The great advantage of such an arrangement is that focal instrumentation can be located in several different places at any one time, each place having its own focal ratio, or other characteristics.

![](images/6017674c5cc2421e5e853d14f8194d0173f2f4311a78defe8aedb04ad04e163c.jpg)  
Fig. 5.2 Ray tracing by computer. A point source at infinity, placed at various angular distances from the optical axis, illuminates the pupil of a telescope. Each elementary point represented here in the focal plane corresponds to the impact of a ray coming from the same point source but passing through a different point of the pupil. As the calculations also take into account the effects of diffraction, which is a chromatic phenomenon, the final result depends on the wavelength, given on the horizontal axis. The number next to each image gives the radius in arcsec of the disk containing $80 \%$ of the light energy. The scale is given by the circle at the bottom which has radius $0 . 5 { ^ { \prime \prime } }$ . The linear scale in the focal plane is $2 9 2 \ \mathrm { m m } \ \mathrm { d e g r e e } ^ { - 1 }$ . (Simulation by Enard D., Feasibility Study for the $^ { 8 \mathrm { ~ m ~ } }$ European VLT. European Southern Observatory)

2. The scale of the image in each focal plane, generally given in mm per arcsec. This scale has to be adapted to the choice of detector pixel size, unless the instrument placed at the focus itself modifies the scale through a further optical transformation.

3. The focal ratio of the beam, given by the ratio $f / D$ between the equivalent focal length and the primary mirror diameter.

4. The field, in the two senses of the term. Firstly, the area of the focal plane in which the image quality remains acceptable according to whatever criteria have been predefined; and secondly, the area over which the illumination remains uniform (fully illuminated field), or partial (vignetted field).

5. The image quality, which can be quantified in various ways: using the modulation transfer function (MTF, defined in Sect. 6.1.4) at each point; observing the angular diameter of the circle in which a certain fraction $5 0 \%$ or $80 \%$ ) of the energy from a conjugate point source is concentrated around its ideal image; or, finally, by ray tracing (Fig. 5.2). The image quality that is finally achieved is governed by optical design, quality of optical surfaces, diffraction, and also external factors, such as the presence of a medium upstream whose refractive index is not homogeneous (Earth atmosphere).

6. The curvature of the focal plane, which is not necessarily a plane surface, but may indeed produce the best anastigmatic approximation by being curved. This is the case of the Schmidt telescope, whose field can thereby attain several degrees, an unusually large value.

Further specifications could be added to this list, depending on the wavelength region under observation. We return to this in Sect. 5.2, which deals with specific realisations of telescopes.

# 5.1.2 Gravitational Optics

In empty Euclidean space, light rays are described by the geometrical approximation and follow straight lines. When the refractive index $n ( r )$ depends on the space variable, the trajectories are curved, as illustrated by the simple example of atmospheric refraction (see Sect. 2.5).

In general relativity the geometry of space is curved by the distribution of matter, and the trajectories of light rays, or geodesics, are curves which always traverse the local minimal distance.3 Such effects are present in the Universe on different scales, but especially in the vicinity of a black hole, or on the very large scale of clusters of galaxies. A given mass distribution thus produces convergence or divergence effects in light beams, in a way exactly analogous to the effects of variable refractive index in refracting media. The generic term for these effects is gravitational optics. By extension, a gravitational telescope refers to any mass distribution producing this kind of image.

Without going too deeply into the problem, we may consider the simple case of a light ray passing in the vicinity of some mass $M$ . Recall first Fermat’s principle, in differential form:

$$
\delta \int \boldsymbol { n } ( \boldsymbol { r } ) \mathrm { d } \xi = 0 ,
$$

where $\mathrm { d } \xi$ is the length element along the light path. The equation of the trajectory in a medium with variable index follows from Lagrange’s equation,

$$
\frac { \mathrm { d } } { \mathrm { d } \xi } \left[ n ( \boldsymbol { r } ) \frac { \mathrm { d } \boldsymbol { x } } { \mathrm { d } \xi } \right] = \boldsymbol { \nabla } n ( \boldsymbol { r } ) ,
$$

where $x$ is the space coordinate.

In a gravitational field, the condition $\mathrm { d } s ^ { 2 } = 0$ on the generalised distance $s$ is Dsatisfied by the propagation of the light along its trajectory. In a simple metric of

![](images/d3c5652f0edd1844bc0b7ed6bc9dbde6be505f325f4f6c5a2e3d4270735e7210.jpg)  
Fig. 5.3 Gravitational lens effect due to the cluster of galaxies MS $0 4 4 0 + 0 2 0 3$ , redshift $z = 0 . 1 9$ . C DThe approximately concentric arclets are ‘gravitational images’, created by the cluster of galaxies located beyond it. Left: Image obtained by the Hubble telescope, with a six hour integration time (six orbits), and resolution $0 . 1 { ^ { \prime \prime } }$ (camera WFPC2), sufficient to resolve the thickness of the arclets. Right: Image obtained from ground level by the $3 . 6 \mathrm { ~ m ~ }$ CFH telescope (Hawaii), with angular resolution $0 . 5 { ^ { \prime \prime } }$ and limited by seeing. (Document kindly provided by Hammer F. et al., 1995)

general relativity, the space and time differentials, ${ \mathrm { d } } r$ and $\mathrm { d } t$ , respectively, at distance $r$ from the mass $M$ , are related by the equation

$$
c { \frac { \mathrm { d } t } { \mathrm { d } r } } = 1 + { \frac { G M } { r } } = { \frac { c } { \nu ( r ) } } ,
$$

which thus gives a value $\nu ( r )$ for the apparent speed, in perfect analogy with the effect of a refractive index. This value can be put into Lagrange’s equation, which, upon integration, yields the light paths.

It can thus be understood how a sufficiently large mass distribution may act as a lens, forming an image for the Earth-based observer of some very distant object (Fig. 5.3).

# 5.2 Telescopes

In this section, covering the whole electromagnetic spectrum, we shall examine the specific features of telescopes designed for each given wavelength range. The concept4 was of course first developed for the visible region (by Galileo and Newton in the seventeenth century, Foucault in the nineteenth century, George Hale, Aden Meinel, Raymond Wilson, and others in the twentieth century), then extended to the radio region after 1945. And finally after 1960, it was extended to cover the whole spectrum, observed from the Earth’s surface but also from space.

The discovery or prediction of other information carriers (gravitational waves and neutrinos) has opened the way to speculation about the possibility of building systems, detecting these forms of energy, which fulfil the same role as the classical telescope. This would be an abuse of language at the present rudimentary stage of technical development, in which the tasks of collecting energy, detecting sources, and localising sources in space cannot yet be approached separately. These questions will be approached in Chap. 7, in the context of detection, which remains the main obstacle to observing such signals.

Returning to optical instruments, the quest for maximal collecting area is the common preoccupation in all spectral regions. The limitations, apart from cost, are usually of technological origin. Three basic points are worth remembering:

• The departure of actual optical surfaces from the ideal must remain small compared to the relevant wavelength, in order to obtain the best anastigmatic approximation.   
. When the angular resolution is determined in the most favourable case by diffraction (see Chap. 6), it varies as $\lambda / D$ , where $D$ is the dimension of the primary mirror (or first optical collecting surface). In a global strategy, astronomers of different countries aim in the long term to obtain a uniform angular resolution on the sky, e.g., 0.1 arcsec, in order to be able to compare the properties and morphology of a given object on the same scale and at various wavelengths. However, actually making these different instruments involves a very wide range of sizes and technologies, and the aim of a uniform resolution is almost never achieved.   
The nature of the detection process, which takes place at the focal point of the telescope, determines to a certain extent the design of the telescope.

Because of all these wavelength dependencies, telescope design will be discussed here primarily in terms of the main spectral regions, but distinguishing Earth-based from space observation when necessary. The design of telescope arrays, which significantly improve angular resolutions, will be discussed in Chap 6.

# 5.2.1 Radiotelescopes

Telescopes designed to receive radiofrequency radiation $( 0 . 5 \ \mathrm { m m } \ \lesssim \ \lambda \ \lesssim \ 1 \ \mathrm { k m } )$ are called radiotelescopes or radio dishes. However, the boundary between radio wavelengths (from kilometres to submillimetre) and far infrared wavelengths is not well defined, being somewhere around $0 . 5 \mathrm { m m }$ . Since it does not correspond to any fundamental property, this transition arises rather because of a change in the type of detector from heterodyne detectors to another kind used at shorter wavelengths, i.e., bolometers, then photoconductors, as will be explained in Chap. 7. The transition from one type to the other requires certain modifications in the design and use of the resulting telescopes, so it is logical enough to describe here some of the key features of instruments operating in the radio region.

These radiotelescopes comprise a very big primary mirror $1 0 { - } 1 0 0 \mathrm { m }$ ). It is usually parabolic and the surface accuracy is determined by the operating wavelength. The surface is made from a grid for long wavelengths and continuous panels for shorter wavelengths, with increasing accuracy (/20 environ) for decreasing $\lambda$ . The growing importance of the submillimetre region has led to the construction of better quality mirrors, and even the boundary between radiotelescopes and optical instruments is growing fuzzy. The $1 5 \mathrm { ~ m ~ }$ JCMT radiotelescope (James Clerk Maxwell Telescope) is thus described as the biggest optical telescope in the world (in 2007). The receivers, which also mix strictly radiofrequency detection techniques with optical techniques at the shortest wavelengths (see Sect. 7.4), are placed either directly at the primary focus or at a secondary focus in a Cassegrain setup.

On Earth, the telescope is generally mounted on an altazimuth mount and follows the source in its diurnal motion. At these wavelengths, since sky emission does not vary between day and night, these instruments can operate at all times, whether the sky is cloudy or not. Since the mirrors on these telescopes are robust, they can be built outdoors without a protective dome, which reduces the cost.

More than 20 instruments of this kind with diameters greater than $1 5 \mathrm { ~ m ~ }$ are currently planned or operating around the world (Fig. 5.4). A rather special radiotelescope is the Arecibo radiotelescope in Puerto Rico, which has a primary mirror $3 0 0 \mathrm { ~ m ~ }$ in diameter with a fixed vertical axis. This is a zenith telescope in which the image forms at the focus, but the focus moves as time goes by, so that the receiver must follow the source. The primary mirror of the decimeter wavelength radiotelescope in Nanc¸ay (France), dating from 1961–1964, is rectangular $( 3 0 0 \times 3 5 \mathrm { m } )$ , vertical, but also fixed. It is preceded by a moving plane mirror, which allows a given source to be monitored for longer, and followed by a moving carriage house carrying the receiver.

At radiofrequencies, there are very few multipixel receivers, like photographic plates or CCDs. Obtaining an image of a source with only one pixel available usually means 2D scanning of the source (raster or TV-type scanning), with each pointing direction sampling one pixel of the image. However, at the time of writing (2007), multipixel receivers are being developed, although their capabilities remain modest as yet, both for millimeter wave incoherent imaging (with $1 2 \times 1 2$ bolometer arrays), and for heterodyne detection with a focal plane paved with an array of $5 \times 5$ receiver horns (see Sect. 7.5).

Note also that propagative perturbations in the Earth atmosphere (turbulence in the troposphere or ionosphere), which alters the phase of the waves, only affects observation at wavelengths less than the centimetre.

The angular resolution of radiotelescopes is generally diffraction limited, i.e., at the value $\lambda / D$ , where $D$ is the diameter of the primary mirror (see Sect. 6.1). With $D = 5 0 \mathrm { m }$ , for example, this leads to rather mediocre resolutions, namely 4 arcsec at $\lambda = 1 \mathrm { m m }$ to more than one degree at $\lambda = 1 \mathrm { m }$ . To improve these values, coupled D Darrays of radiotelescopes have been constructed since the 1950s, as discussed in Sect. 6.5.1.

![](images/220b9e755909607da4ae1c2a5dae3e116a99767a4459a44fa8d31156608256c3.jpg)  
Fig. 5.4 (a) Large steerable single-dish radiotelescopes around the world. Existing instruments are plotted against the shortest wavelengths for which they will operate at normal efficiency. Limits imposed by considerations of structural rigidity, and thermal or gravitational distortion, are indicated. These perturbations limit the accuracy with which the desired parabolic shape can be achieved. (Updated version of Blum E.J., Adv. Electron. Electr. Phys. 56, 97, 1981. With the kind permission of the editor.) (b) The Effelsberg radiotelescope (Max Planck Institute, Bonn). The usable part of the mirror is $1 0 0 \mathrm { m }$ in diameter

![](images/158d7688d891ee599542c3958a261ae63afb13bedce97cdf9ad60a44424c1b5d.jpg)  
Fig. 5.5 Map of one of the regions of intense star formation in Orion, including the Becklin–Neugbauer (BN) object. The map was made in the ammonia $\left( \mathrm { N H } _ { 3 } \right)$ band $\lambda = 1 . 3 \mathrm { c m }$ ) with the DEffelsberg radiotelescope (Germany). The $4 ^ { \prime \prime }$ lobe is shown (half width beam HWB). (a) Constant intensity contours superposed on a photograph. (b) 3D intensity plot. See also the infrared image of the same region in Chap. 7, Fig. 7.35. (After Batrla W. et al., Astr. Ap. 128, 279, 1983. With the kind permission of Astronomy and Astrophysics)

The Effelsberg Radiotelescope (Germany)

The largest steerable dish in existence, this $1 0 0 \mathrm { ~ m ~ }$ diameter instrument has a sufficient surface quality (using metal plates) to operate at wavelengths $\lambda \gtrsim 7 \mathrm { m m }$ . At shorter wavelengths, the energy concentration in the diffracted image becomes inadequate (Fig. 5.4b).

The $3 0 \mathrm { m }$ Millimetre Radiotelescope at Pico Veleta (Spain)

This is a steel structure supporting aluminium panels machined to a nominal precision of $3 5 ~ { \mu \mathrm { m } }$ rms, and which can produce images limited by diffraction to wavelengths in the range 0.87 to $4 \mathrm { m m }$ .

# 5.2.2 Ground-Based Optical Telescopes: Visible and Near Infrared

Telescopes operating in the visible region are the oldest imaging instruments used in astronomy, apart from the human eye, of course. Diameters grew in stages, depending on technological progress made with materials. With the gradual disappearance of the refracting telescope, which effectively ceased to play any important role during the twentieth century, instruments with 5 to $6 \textrm { m }$ mirrors began to appear in the first half of that century, followed by instruments up to $1 0 \mathrm { m }$ in the second half. By 2020–2030, we shall no doubt see instruments reaching $3 0 { - } 5 0 \ \mathrm { m }$ in diameter. The extension to the near and mid-infrared $( \lambda ~ < ~ 3 0 ~ \mu \mathrm { m }$ , approximately) was made in the 1970s, as sensitive detectors became available, and sites were discovered which could provide good atmospheric transmission windows. Tables 5.1 and 5.2 list all visible and infrared optical telescopes on the Earth’s surface with diameter greater than $3 . 5 \mathrm { ~ m ~ }$ at the time of writing (2007), specifying their location.5

It is interesting to invoke several recent developments profoundly affecting some concepts which appeared to have reached their limits. Indeed, the technological difficulties, degradation of images by atmospheric turbulence, and the advent of space travel, seemed for a while at the end of the 1970s to make the further construction of large ground-based telescopes, with diameters greater than $5 { - } 6 \mathrm { m }$ , somewhat improbable. But this point of view rapidly became outdated, for a number of reasons:

• The technological limitations on the construction of very large mirrors have been largely overcome by the use of new materials (e.g., ceramics) and the possibilities of active control leading to a substantial decrease in weight, by building mirrors with segmented surfaces. Methods correcting for the effects of atmospheric turbulence appeared at the end of the 1980s (adaptive optics), preceded by numerical methods correcting images a posteriori (speckle interferometry) developed in the 1970s. Overcoming the effects of turbulence (see Sect. 6.2) meant that full advantage could be taken of improved angular resolution, proportional to the diameter $D$ of the telescope.

Table 5.1 Large ground-based optical telescopes in the northern hemisphere   

<table><tr><td>Latitude</td><td>Altitude [m]</td><td>Site</td><td>Country</td><td>Diameter [m]</td><td>Remarks</td><td>Date</td></tr><tr><td>47N</td><td>2070</td><td>Zelenchuskaya (Caucasus)</td><td>Russia</td><td>6</td><td>Altazimuth mount</td><td>1972</td></tr><tr><td>42°N</td><td>2500</td><td>Xing Long</td><td>China</td><td>4</td><td>LAMOST siderostat</td><td>2007</td></tr><tr><td>37N</td><td>2160</td><td>Calar Alto (Spain)</td><td>Germany and Spain</td><td>3.5</td><td></td><td>1981</td></tr><tr><td>34N</td><td>1706</td><td>Palomar (California)</td><td>USA</td><td>5</td><td>First VLT</td><td>1948</td></tr><tr><td>32°N</td><td>2130</td><td>Kitt Peak, Arizona</td><td>USA</td><td>3.8</td><td>Mayall</td><td>1974</td></tr><tr><td></td><td>3266</td><td>Mt. Graham, Arizona</td><td>USA,Italy, Germany</td><td>2×8.2</td><td>LBT</td><td>2007</td></tr><tr><td>30N</td><td>2076</td><td>Mt.Locke (Texas)</td><td>USA</td><td>9.2</td><td>Hobby-Eberly fixed elevation</td><td>1997</td></tr><tr><td>28N</td><td>2370</td><td>La Palma (Canaries)</td><td>UK</td><td>4.2</td><td>WHT (Herschel)</td><td>1984</td></tr><tr><td></td><td></td><td>Mauna Kea</td><td>Spain</td><td>10.4</td><td>GranTeCan</td><td>2008</td></tr><tr><td>19N</td><td>4200</td><td>(Hawaii)</td><td>UK</td><td>3.8</td><td>Infrared UKIRT</td><td>1979</td></tr><tr><td></td><td></td><td></td><td>Canada, France, Hawaii</td><td>3.6</td><td>CFHT</td><td>1974</td></tr><tr><td></td><td></td><td></td><td>USA (CalTech)</td><td>2×10</td><td>Keck Iand II</td><td>1994</td></tr><tr><td></td><td></td><td></td><td>Japan</td><td>8.4</td><td>Subaru</td><td>1999</td></tr><tr><td></td><td></td><td></td><td>USA (NSF)</td><td>8.0</td><td>Gemini N</td><td>1999</td></tr></table>

Table 5.2 Large ground-based optical telescopes in the southern hemisphere   

<table><tr><td>Latitude</td><td>Altitude [m]</td><td>Site</td><td>Country</td><td>Diameter [m]</td><td>Remarks</td><td>Date</td></tr><tr><td>23°S</td><td>2 650</td><td>C. Paranal (Chile)</td><td>Europe</td><td>4×8.2</td><td>VLT</td><td>1998</td></tr><tr><td rowspan="2">29°S</td><td rowspan="2">2280</td><td rowspan="2">Las Campanas</td><td rowspan="2">USA</td><td>4</td><td>VISTA</td><td>2008</td></tr><tr><td>2×6</td><td>Magellan</td><td>2002</td></tr><tr><td>29°S</td><td>2430</td><td>(Chile) La Silla (Chile)</td><td>Europe (ESO)</td><td>3.6</td><td></td><td>1977</td></tr><tr><td rowspan="3">30°S</td><td rowspan="3">2700</td><td rowspan="3">C.Tololo (Chile)</td><td></td><td>3.5</td><td>NTT</td><td>1989</td></tr><tr><td>USA</td><td>4</td><td>Blanco</td><td>1974</td></tr><tr><td>C.Pachon (Chile) USA</td><td>8.1</td><td>Gemini S</td><td>2001</td></tr><tr><td>32°S</td><td>1500</td><td>Sutherland</td><td>Brazil and USA South Africa</td><td>4.1 11</td><td>SOAR</td><td>2005</td></tr><tr><td>34°S</td><td>1165</td><td>(South Africa) Siding Springs</td><td>and others Australia</td><td>3.9</td><td>SALT AAT</td><td>2005 1974</td></tr></table>

• In high resolution spectrography (Chap. 8), sensitivity depends critically on the diameter $D$ , whilst the luminosity contribution from the sky background is a nuisance but remains acceptable. The need to observe from space is thus less acute than in the case of low resolution photometric or spectral measurements.   
. The cost of space missions is still at least one order of magnitude greater than the cost of building a comparable instrument at ground level. Following the beautiful results of the Hubble telescope, it has now become clear that ground-based and spaceborne observation are complementary and essential. The design of specialised telescopes, e.g., for spectroscopy, results in the development of less costly instruments, but without the flexibility of a conventional telescope. This is the case for the Large Sky Area Multi-Object Fiber Spectroscopic Telescope (LAMOST) at Xing Long in China (2007), which has a fixed primary mirror like the decimetre wavelength radiotelescope in Nanc¸ay, France, or the South African Large Telescope (SALT), which has fixed elevation (2005).

# Construction of Very Large Mirrors

The strategy adopted for constructing very large mirrors (with diameters greater than $2 { - } 3 \ \mathrm { m }$ is now to make them lighter, i.e., thinner. Whatever technical solution is used, the primary becomes too light to ensure its own rigidity. Deformation of the mirror under its own weight would lead to significant and unacceptable aberration, and worse, it would vary with the pointing direction.

Two main technological choices have come to the fore:

• Thin single-piece mirrors, e.g., the European $8 . 2 \mathrm { ~ m ~ V L T }$ , or thick but lightened mirrors, e.g., the $8 . 2 \mathrm { m }$ Large Binocular Telescope in Arizona. Segmented mirrors, i.e., made up of small optical surfaces (around $1 \mathrm { m }$ ), arranged side by side and polished in such a way as to reconstitute the desired paraboloid, e.g., the $1 0 \mathrm { m } \mathrm { K e c k }$ Telescope in Hawaii.

Beyond diameters of $8 { - } 1 0 \mathrm { m }$ , for the generation of extremely large telescopes (ELT) of the years 2005–2040, only the segmented solution is considered.

In both cases, the deformation is accepted but corrected in real time by means of mechanical control from behind the monolithic mirror or the segments making up the mirror. These corrections can in part be programmed as a function of temperature, and also the altitude of the mirror, for gravitational effects, but they are mainly deduced from real time analysis of the image of a star, as given by the mirror. This is the principle of active optics (Fig. 5.6). Benefiting from all the resources of real time control provided by computer science, it underpins the development of mirrors for all the large Earth-based optical telescopes both now and in the future, until new, more effective technologies are devised for lightening these structures (perhaps membrane mirrors).

Ground-based telescopes were traditionally mounted on equatorial mounts, but these have now been practically abandoned, being both cumbersome and heavy, and hence expensive. Today they have been replaced by the altazimuth mount, which uses two axes to compensate for diurnal motion and is computer driven. A pointing accuracy of the order of 0.1 arcsec rms is achieved. The disadvantage with this arrangement is that it creates a rotation of the field which must be compensated for by a field derotator.

![](images/39fdbfc0e4c01183c90fbb4d0ca65b08ac8d948e0363a62a7943b43a201b4b12.jpg)  
Fig. 5.6 An example of active optics. The New Technology Telescope (NTT) at the European Southern Observatory, opened in 1989, has a thin, actively supported primary mirror of diameter $3 . 5 \mathrm { { m } }$ . Shown here is the model used to finalise the dorsal assemblage of jacks which control the shape. These act in such a way as to correct for any mechanical (e.g., gravitational, wind) or thermal deformations of frequency less than $1 \ : \mathrm { H z }$ . (Document R. Wilson, European Southern Observatory)

# Features Specific to the Infrared

At ground level, telescopes can be used indifferently in the visible or the infrared. Note that some large instruments have been built specially for the infrared, an example being the $3 . 8 \mathrm { ~ m ~ U K }$ telescope at Mauna Kea (Hawaii), known as UKIRT. Two factors distinguish the optimal design of an infrared instrument, and the same factors are relevant in the submillimetre region:

• A chopping secondary mirror, usually vibrating at a frequency less than $5 0 \mathrm { H z }$ , makes it possible to alternate very quickly between source and sky background as imaged at the detector, and thus to make a differential measurement. This technique, well adapted to single pixel detectors, has developed hand in hand with more sophisticated background subtraction methods, as described in Sects. 2.3.3 and 9.4. It is nevertheless true to say that the chopping frequency should be as high as possible owing to the rapid time evolution of atmospheric emissions. Low thermal pollution. The optics are designed so that the detector receives as little radiation as possible from sources other than the optical surfaces themselves. This aim is achieved by using suitable arrangements of diaphragms and baffles. In addition, the optical surfaces are treated to reduce emissivity, and a good telescope should not have an emissivity greater than a few percent, taking into account all its surfaces. These considerations apply equally to submillimetre and millimetre telescopes, for the same reason, namely, to avoid drowning out the astronomical signal by the thermal background emitted from the optical system itself.

The New Generation of Optical Telescopes

We shall describe several examples out of the dozen or so new generation telescopes going into operation around the year 2000, and one project for the next generation.

The two Keck telescopes, built in 1992, have diameter $1 0 \mathrm { m }$ , the primary mirrors each consisting of 36 independent and actively supported hexagonal segments of $1 . 8 \mathrm { ~ m ~ }$ , separated by $3 \ \mathrm { m m }$ spaces. The focal ratio $f / D$ is equal to 1.75. Several focal points are available: primary, Cassegrain, and Nasmyth. The two telescopes are $B = 7 5 \mathrm { ~ m ~ }$ apart at the summit of Mauna Kea (Hawaii). They can be coupled Dcoherently (interferometry), and the resulting diameter will lead to great sensitivity, and a large angular resolution $( \lambda / B = 2 . 7 5 \times 1 0 ^ { - 3 }$ arcsec at $\lambda = 1 \mu \mathrm { m }$ ).

D  DThe European Very Large Telescope, or VLT, went into operation in 1998. It consists of four independent telescopes with thin single-piece primary mirrors of effective diameter $8 . 2 \mathrm { m }$ . Each is mounted on active supports, $f / D = 1 . 8 \ \mathrm { m }$ , and DNasmyth, Coude, and Cassegrain focal points are available. The four telescopes´ (Fig. 5.7) are located at the corners of a trapezoid at Cerro Paranal (Chile), and this arrangement allows either an independent use or a coherent combination (interferometry). In the latter case, the resolution is determined by the largest possible separation, $B = 1 2 0 \mathrm { m }$ . Four smaller movable telescopes $( 1 . 8 \mathrm { m } )$ complete Dthe interferometric system, providing bases of variable length and orientation up to $2 0 0 \mathrm { m }$ long.

![](images/8dd78344b5a0f53978dc86a185694b262369eb606ae8eb910f09b3fda10a37ca.jpg)  
Fig. 5.7 The European Very Large Telescope (VLT), Cerro Paranal, ( $2 6 3 5 \mathrm { ~ m ~ }$ , Chile). The VLT consists of four $8 . 2 \textrm { m }$ telescopes, and also a complementary network of mobile interferometric telescopes (foreground). Channels allow transportation of light for recombination at a common focal point. (Drawing kindly supplied by the European Southern Observatory)

The Large Binocular Telescope (LBT or Magellan) is based on a hybrid technology, since it uses thick but lightened single-piece active mirrors of $8 . 4 \mathrm { ~ m ~ }$ forming a binocular pair on the same altazimuth mounting. As in the original MultiMirror Telescope (Mount Hopkins, Arizona), which was its predecessor, built in 1976 and including six mirrors on the same mounting, the beams of light can be either coherently or incoherently superposed. The LBT was set up on Mount Graham (Arizona) and saw its first light in 2005.

The Thirty Meter Telescope (TMT) project results from a joint effort by private and public institutions in Canada and the United States. At the time of writing (2006), this planned $3 0 ~ \mathrm { m }$ telescope is the most advanced of a new generation that will no doubt become a reality in the first half of the twenty-first century. Equipped with a primary mirror of diameter $D \ = \ 3 0 \ \mathrm { m }$ comprising 492 individual $1 . 4 ~ \mathrm { m }$ hexagonal mirrors $4 . 5 \mathrm { c m }$ thick, open at $f / 1$ , it will be set up at the Mauna Kea site in Hawaii. As for all instruments in this category, the construction is only justified if the ultimate angular resolution $\lambda / D$ can be achieved, and this will require an extraordinarily high-performance adaptive optics system (see Sect. 6.3).

Europe (European Southern Observatory ESO) has also been studying the idea of a comparable project, namely the European Extremely Large Telescope (E-ELT) of diameter $4 2 \mathrm { m }$ , and this was approved in 2006.

# 5.2.3 Space Telescopes, from Ultraviolet to Submillimetre

By placing a telescope in space, all the obstacles to astronomical observation caused by the day–night cycle and the Earth atmosphere can be entirely avoided, while covering a very broad region of the electromagnetic spectrum from the ultraviolet to the submillimetre.

Space travel offers possibilities ranging from the use of aeroplanes and stratospheric balloons, to space shuttles, low-orbiting space stations (altitude 400– $5 0 0 \mathrm { k m } , \quad$ ), satellites orbiting the Earth at various distances and sometimes stabilised at Lagrange points, probes investigating objects in the Solar System (planets, moons, comets, asteroids, the Sun, etc.), and instruments on or around the Moon.

Onboard telescopes observe deep space, beyond the confines of the Solar System. Apart from the possibilities of in situ investigation, more specific instruments can also provide images of objects, e.g., mapping the surface of Mars from an instrument in Martian orbit. The quest for large diameters, usually justified by the increased sensitivity required of instruments, is limited by technological and economic issues, just as it is for ground-based instruments. These telescopes are remote controlled and highly reliable both for control of acquisition and pointing, for example, and for reception, processing, and transmission of measurement data. For deep space observation, operational and planned missions are genuine space observatories, specifically designed for a given spectral region.

# Ultraviolet

In the ultraviolet, the spectral limits are rather clear. The atmosphere blocks wavelengths below $3 5 0 ~ \mathrm { { n m } }$ (or $3 2 0 ~ \mathrm { { n m } }$ at high altitude sites), and this has made space observation unavoidable, using balloons and rockets in the 1960s and 1970s, and orbiting observatories thereafter. UV space telescopes are distinguished from visible telescopes only by the quality of their optical surfaces (flaws $< \ \lambda / 2 0$ , approximately), and the need for efficient reflecting surfaces $( \mathrm { M g } \mathrm { F } _ { 2 }$ layers). The production of reflecting layers by means of multiple coatings gives acceptable reflectivity (10 to $20 \%$ ) down to near X ray wavelengths $( 1 0 \ \mathrm { n m } )$ , and thus avoids the constraints imposed in the latter spectral region by the need to use grazing incidence devices.

The Orbiting Astronomical Observatory (OAO) satellites provided the first mapping and photometry of the UV sky in the 1970s. They were followed, in 1978, by the remarkably fertile International Ultraviolet Explorer (IUE) (see Fig. 8.9). This instrument remained active for almost 20 years (1978–1996), equipped with a spectrophotometer in the region $1 1 5 { - } 3 2 0 \mathrm { n m }$ .

In the near ultraviolet region, the main project of the 1990s and 2000s has been the Hubble Space Telescope, launched in 1989 and expected to remain in operation up until 2010. With a diameter of $2 . 4 ~ \mathrm { m }$ and angular resolution $0 . 1 ^ { \prime \prime }$ (after a few initial difficulties), it covers all wavelengths between 110 and $7 0 0 ~ \mathrm { n m }$ . In 2002, during a visit by NASA astronauts, it was equipped with a new instrument, the Advanced Camera for Surveys (ACS), able to provide images and spectra from the ultraviolet to the very near infrared $( 1 1 5 - 1 1 0 0 \mathrm { n m } )$ ).

Among more specialised missions, we should mention:

• The Far Ultraviolet Spectroscopic Explorer (FUSE) run by NASA and other countries, launched in 1999 but affected by a serious failure in 2006, and covering the region $9 0 . 5 \mathrm { - } 1 1 8 . 7 \mathrm { n m }$ .   
• The Galaxy Evolution Explorer (GALEX), a $3 5 \mathrm { c m }$ telescope launched by NASA in 2003, and covering the region $1 3 5 { - } 2 8 0 \mathrm { n m }$ .

The extraordinary results harvested by the Hubble telescope stimulated the preparation of a successor, namely the James Webb Space Telescope (JWST).6 This observatory will be placed at Lagrange point L2 and carry a $6 . 5 \mathrm { ~ m ~ }$ telescope equipped with a segmented mirror deployed in space (see Fig. 5.8). It will cover the region $0 . 6 { - } 2 7 ~ { \mu \mathrm { m } }$ , so is designed rather as a near infrared telescope than an ultraviolet telescope. However, it will be observing the very remote Universe, where spectral shifts due to expansion $( z \gtrsim 1 )$ ) will bring radiation emitted in the ultraviolet into the visible and near infrared range. Launch is planned for 2013.

![](images/43b719ea3936894918706a1287ab24e0b97cde68eefc9d0ee7c5661d7ca27e20.jpg)  
Fig. 5.8 Artist’s impression of the future $6 . 5 \mathrm { ~ m ~ }$ James Webb Space Telescope, to be placed at Lagrange point L2. The figure shows the alignment of the telescope with the Earth and Sun, and a screen protecting the optical system. Credit NASA

Infrared and Submillimetre

The infrared refers to $1 { - } 1 0 0 \ \mu \mathrm { m }$ and the submillimetre to $0 . 1 { - } 1 ~ \mathrm { m m }$ . Although the near and mid-infrared (up to about $3 0 ~ { \mu \mathrm { m } } ,$ ) can in part be observed from the Earth’s surface, space observation is inevitable beyond that. And even below, certain spectral regions absorbed by the Earth atmosphere (e.g., between 5 and $9 ~  { \mu \mathrm { m } } )$ contain emissions of considerable importance (e.g., the spectra emitted by aggregates of aromatic hydrocarbons). Beyond $3 0 ~ { \mu \mathrm { m } }$ , some useful transmission windows exist at ground level in several exceptional sites, such as the Antarctic, but only space observation can provide systematic and precise data. Nevertheless, the concentration of absorbing molecules (mainly $\mathrm { H } _ { 2 } 0$ ) at low altitudes means that aeroplanes and balloons are less costly for observation than a deep space instrument.

During 1980–2010, a considerable wealth of discoveries has been made by infrared observation in this vast spectral region: emission by cold objects in galaxies, but also the intense radiation associated with star formation, the spectra of primordial galaxies shifted toward the infrared by cosmic expansion, the $2 . 7 ~ \mathrm { K }$ cosmic background radiation, and many others. This success justifies a major effort to prepare space observatories covering the whole of this spectral region. But one of the main difficulties with these instruments comes from the need to cool the telescopes, essential for improving sensitivity and reducing the associated background signal and thermal noise (see Chap. 9). In an aircraft or balloon, this cooling remains modest $- 3 0$ to $- 5 0 ^ { \circ } \mathrm { C } )$ ) given the presence of residual atmosphere.  It will be pushed as far as possible in satellites.

Aircraft. An example here is the telescope of the Kuiper Airborne Observatory (KAO), named after the Dutch astronomer G. Kuiper (1906–1973), which had a diameter of $0 . 9 \mathrm { ~ m ~ }$ , and was carried on an aeroplane (USA). It operated in the stratosphere in a very similar way to a ground-based observatory. Its successor aboard a Boeing 747SP (collaboration between NASA and Germany, flown in 2008) is the Stratospheric Observatory for Infrared Astronomy (SOFIA) shown in Fig. 5.9, equipped with $2 . 5 \mathrm { m }$ mirror and flown at an altitude of $1 4 \mathrm { k m }$ .

![](images/edab198dc1590e0d9fd43a710737c20364ee82f54a05836f8a66db34ad322d37.jpg)  
Fig. 5.9 The $2 . 5 \mathrm { m }$ submillimeter telescope of the NASA’s Stratospheric Observatory for Infrared Astronomy SOFIA on its Boeing 747-SP aircraft. Insert: The 747-SP flying with the telescope open, during its final tests over California in August 2010 (NASA). Drawing kindly provided by Max Planck Institut f¨ur Extraterrestrische Physik, Garching. Photo NASA

Balloons. Many instruments have been carried aboard stratospheric balloons since the beginning of the 1960s, some reaching diameters of around $1 \textrm { m }$ . Among these missions, one of the most remarkable is BOOMERANG, run by NASA in partnership with many other countries since 1998 and designed to study the cosmological background radiation (imaging and polarisation). The cooled telescope has a $1 . 3 ~ \mathrm { m }$ primary mirror and observes wavelengths7 in the range $1 { - } 2 . 1 ~ \mathrm { m m }$ from a stratospheric balloon flying at an altitude of $4 2 \mathrm { k m }$ above the Antarctic continent.

Satellites. On board a satellite, passive cooling by radiation into space leads to temperatures around 80 or $1 0 0 \mathrm { ~ K ~ }$ . The use of cryogenic fluids or closed circuit refrigerators allows for cooling of optical parts and detectors down to 10 or $2 0 ~ \mathrm { K }$ , sometimes even much lower ( $0 . 1 \mathrm { ~ K ~ }$ for dilution refrigerators), and this totally removes the instrumental background.

The InfraRed Astronomy Satellite (IRAS), launched in 1983, included a $0 . 6 \mathrm { m }$ telescope completely cooled by liquid helium. The Infrared Space Observatory (ISO), which operated from 1995 to 1998, had the same diameter and was cooled in the same way. The optics of the COsmic Background Explorer (COBE), launched in 1992, were also cooled, during the first part of the mission, by liquid helium, whose gradual evaporation limited the period of operation.

Let us briefly describe three major missions over the period 2000–2020, the first two (Spitzer and Herschel) dedicated to a wide range of galactic and extragalactic observations and the third (Planck) specifically designed for detailed observation of the cosmological background:

• The Spitzer observatory8 (a mission originally called SIRTF) includes a cooled $0 . 8 5 \mathrm { m }$ telescope operating in the region $3 { - } 1 8 0 \mu \mathrm { m }$ . It was launched by NASA in 2003 with an expected lifetime of 5 years. It is more sensitive than all previous missions (IRAS, ISO). The Herschel observatory9 (a mission originally called the Far InfraRed Space Telescope FIRST) includes a cooled $3 . 5 \mathrm { ~ m ~ }$ telescope designed to carry out galactic and extragalactic observations in the range $6 0 { - } 6 7 0 ~ { \mu \mathrm { m } }$ , with a lifetime of 3 to 4 years (ESA, launch in 2008). It will be placed at Lagrange point L2. Its focal instruments combine detection techniques specific to the infrared (photoconductors) with others for the radio region (heterodyne, see Sect. 7.5). The Planck observatory10 is mainly designed to study the cosmological background radiation, but its extreme sensitivity means it should be able to address many issues of galactic and extragalactic astronomy. Equipped with a telescope cooled to $2 0 \mathrm { ~ K ~ }$ and detectors operating at $0 . 1 \mathrm { ~ K ~ }$ , covering frequencies $3 0 -$ $8 6 0 ~ \mathrm { G H z }$ in fields of 30 to 5 arcmin, this observatory, also placed at Lagrange point L2, should operate for at least 21 months (launch 2008).

Infrared and submillimetre instrumentation on the surface of the Moon would benefit from the very low temperatures (about $1 0 0 ~ \mathrm { K }$ at the bottom of permanently shaded craters in the polar regions), a natural cryogenic source for cooling the optics. This option is still not seriously envisaged (see Sect. 2.10).

![](images/c123eed9443b5a4d3782405dec760d0791f2ee6e976f8ae5f204dd3b1abcb914.jpg)  
Fig. 5.10 X-ray sky in galactic coordinates. Upper: X-ray survey by HEAO-I, covering $2 { - } 2 0 \mathrm { k e V }$ (Boldt, 1987). Middle: Survey by ROSAT. Dots denote the brightest of the 100 000 point X-ray sources detected (Voges et al., 2000). Lower: ROSAT survey of diffuse X-ray emission. Energies are colour coded, from red $( 0 . 1 \mathrm { - } 0 . 5 \ \mathrm { k e V } )$ to blue $( 0 . 9 { - } 2 . 4 \ \mathrm { k e V } )$ ) (Snowden et al., 1997). (Figure kindly communicated by G. Hasinger, Garching)

# 5.2.4 X-Ray Telescopes

This concerns photons with energies in the range $( 0 . 1 \mathrm { - } 1 0 \mathrm { k e V } )$ . Since the discovery in 1962 of the first $\mathrm { X }$ -ray source outside the Solar System, X-ray astronomy has progressed enormously, observations being made almost exclusively by instruments in orbit. In 1978, the launch of the Einstein satellite (HEAO-II) resulted in a large quantity of data and, notably, X-ray images (Fig. 7.27). Figure 5.10 gives some idea of the progress that has been made.

![](images/d3567fe48bbec13069966e042135c5a139f6ea1f945d1443309f18604d761234.jpg)  
Fig. 5.11 Side and front views of a Wolter X-ray telescope. $P$ and $H$ denote parabolic and hyperbolic surfaces of revolution, whose common axis points to the source. See also Fig. 5.12

![](images/6542b4b3ead1ed1a40a61e444f03419144cad4f6d96c682f29ede6b38c2f8c03.jpg)  
Fig. 5.12 Aperture of the 7 convergent X-ray telescopes planned for the E-ROSITA mission (launch 2015). Each telescope, with entry diameter $1 6 \mathrm { { c m } }$ , consists of 27 nested mirrors. (Source Max Planck Institute f¨ur Extraterrestrische Physik)

Grazing Incidence Telescopes

As metallic surfaces absorb $\mathrm { X }$ -rays at all but very high incidence angles, the Wolter telescope uses grazing incidence $( \approx ~ 8 9 ^ { \circ }$ ) (Figs. 5.11 and 5.12). Two confocal segments of a paraboloid $P$ and a hyperboloid $H$ form, after two reflections, an image of a source at infinity at their common focus.

To increase the effective area presented to the incident radiation, several mirrors are nested together. The system is perfectly anastigmatic on the axis, has no spherical aberration, and satisfies Abbe’s condition (aplanetism), which means that an image formed from paraxial rays has no coma.

In the Einstein telescope, the collecting area is $3 0 0 ~ \mathrm { c m } ^ { 2 }$ for energies less than $2 \mathrm { k e V } ,$ and decreases to $5 0 \mathrm { c m } ^ { 2 }$ at $3 . 5 \mathrm { k e V } ,$ since only those parts of the mirror at the greatest incidence angles play any role at higher energies. The image quality, greatly inferior to the one which would be imposed by diffraction, is limited by defects in the crystalline structure of the metallic mirror surfaces. These defects disturb the periodicity of the crystalline lattice and cause phase errors at the pupil, and hence a deviation from the ideal image in the focal plane (see Sect. 6.2).