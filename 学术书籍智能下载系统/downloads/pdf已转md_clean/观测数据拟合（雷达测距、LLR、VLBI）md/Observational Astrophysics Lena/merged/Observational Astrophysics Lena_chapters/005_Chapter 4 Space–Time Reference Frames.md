# Chapter 4 Space–Time Reference Frames

An essential part of astrophysical observation and data analysis consists in measuring the positions of astronomical objects and in dating events. Obtaining the photometric magnitudes of the emitted radiation is not enough. The source must be identified in catalogues or data bases, and the position must be determined to great accuracy, since spatial resolutions of the order of several tenths of a millisecond of arc can now be attained in images, and this trend is certain to continue. Concerning the absolution positioning accuracies of celestial objects, over the past 20 years or so, these have gone from a few hundredths of a second of arc before the Hipparcos satellite was launched to about ten microseconds of arc with the Gaia mission. In terms of sensitivity, detectors can now measure the characteristics of phenomena whose time of variation is less than one millisecond. And further, extremely accurate time scales, taking into account the effects of general relativity, are required for space travel and exploration of specific sites in the Solar System.

This chapter treats the recent progress in astronomical reference systems, first for space and then for time, even though the primary source for time scales is now linked to a phenomenon quite distinct from the Earth’s movement. The notions involved also have important applications for the everyday life of Earthlings like ourselves, e.g., with the advent of GPS or the synchronisation of clocks in transport and telecommunications. The objective is to provide a basis for the space and time coordinates needed in practical calculations that do not aim for accuracies better than a few $0 . 0 1 ^ { \prime \prime }$ for absolute positions. To compare this requirement with past and current performance in astrometry, we need only examine the way accuracies in position and parallax measurements have evolved over time, as shown in Fig. 4.1.

The Hipparchos–Ptolemy catalogue1 as transmitted in the Almagest can be used to calculate true star positions relative to the equator or the ecliptic of that epoch and thereby determine the statistical quality of the measurements. The result is an accuracy of the order of 0.3–0.5 degrees. Figure 4.1 shows a very slow improvement in the accuracy of astronomical pointing. There is a very slight inflexion with the advent of optical instruments toward the end of the seventeenth century. The refracting telescope became available with Galileo2 in 1610, but its use as a sighting instrument came rather later, coinciding with the foundation of the observatories in Paris and Greenwich. Refracting telescopes were above all used to observe faint objects, but that step forward did not necessarily improve direction measurements. Later, progress in mechanical construction and clock-making proved to be just as important in this respect as developments in optics.

![](../chunks/Observational Astrophysics Lena_part_0002_pages_0071-0140/auto/images/d4f00879cb93dc58529edfea761c65425230d47fb6f835d28e0b0910a106477e.jpg)  
Fig. 4.1 Improving astrometric accuracy in the observations of stars and planets at different epochs

However, the most recent part of the curve is highly instructive and illustrates the significant progress made in astrometry (measurement of positions, proper motions, and parallaxes of heavenly bodies) by virtue of space techniques. While it took about 20 centuries to improve astrometric accuracy by 4 to 5 orders of magnitude, it subsequently took a mere 20 years with Hipparcos, Gaia, and SIM to achieve a similar leap forward. In the end, the DIVA and FAME projects in Germany and the USA, respectively, put forward just after the success of the Hipparcos mission, were never funded.

Modelling requirements depend significantly on the level of accuracy one hopes to achieve, and the degree of difficulty grows rapidly with this accuracy. It is thus essential to adopt the right tools for each situation. It is pointless to use the


<!-- chunk 0003: pages 141-210 -->
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

where $r > 0$ , $0 \leq \phi < 2 \pi$ , $- \pi / 2 \leq \theta \leq \pi / 2$ . We shall call $\phi$ the longitude and $\theta$  
 
the latitude (see Fig. 4.2), but it should be noted that the definition of latitude as the angle above the equator is common usage in astronomy, whereas physicists prefer to use the colatitude measured from the polar direction. This should be borne in mind when using tangent frames that are not oriented in the same way.

![](../chunks/Observational Astrophysics Lena_part_0003_pages_0141-0210/auto/images/4badd87d02736a8bbebee5559a67bf7448005e3f0ef990b7521d434a4c18a29b.jpg)  
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

![](../chunks/Observational Astrophysics Lena_part_0003_pages_0141-0210/auto/images/dc1b83c9094797ce5f11ee801302751b8d29288eeb520a9850c86dbc85207abd.jpg)  
Fig. 4.3 Definition of the horizontal reference system

# The Hour Frame

As a result of diurnal motion, the coordinates of a star in the horizontal frame are variable, and subject to rather complicated laws. This renders the frame impractical for the cataloguing of celestial objects. Such a system is just adapted to the instantaneous description of the positions of objects in the sky for an observer at the Earth’s surface. The situation is improved by choosing the celestial equator as the fundamental plane, and thereby placing $\boldsymbol { e } _ { 3 }$ in the direction of the celestial pole. In this plane, the origin for longitudes is given by the intersection of the celestial equator with the local celestial meridian (see Fig. 4.4). There are two such intersections and the standard choice has been the direction in which the Sun culminates, i.e., the south for inhabitants of the Mediterranean region or China. The associated spherical coordinates are respectively:

• The declination $\delta$ for the angle of latitude, that is, the height of the star above the celestial equator. This takes values between $- \pi / 2$ and $+ \pi / 2$ and, for a given  Cstar, varies slightly in time due to the precession of the celestial equator and the proper motion of the star itself. This precession, i.e., the systematic motion of the celestial pole about the pole of the ecliptic, produces an annual variation in the declinations of stars equal to at most $2 0 ^ { \prime \prime }$ per year, whereas the true motion of the star in space leads to proper motions of 10 mas/year, except in exceptional cases. Precession is a motion of the frame relative to sources and not a true motion of the sources.

• The hour angle $H$ is the dihedral angle between the local meridian and the plane containing the directions of both the star and the celestial pole. For historical reasons connected with techniques for determining time, the convention fixing the orientation of $H$ is $\mathrm { d } H / \mathrm { d } t$ , which gives $H$ a left-handed orientation. Great care is therefore needed when applying rotation matrices in the hour frame. In contrast to the orientation of the azimuthal angle, the convention for orientating the hour angle involves no exceptions and we shall stick with it, despite the resulting mathematical drawback.

![](../chunks/Observational Astrophysics Lena_part_0003_pages_0141-0210/auto/images/836f665531ba7337c864ec677a4d3f9229a722d39db68c610ace34ab5c24c8df.jpg)  
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

![](../chunks/Observational Astrophysics Lena_part_0003_pages_0141-0210/auto/images/6ba78667ba04555cf4a3f2aaeb2eb97fd2038732c52dcd9da2230b991f5fe0e4.jpg)  
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

![](../chunks/Observational Astrophysics Lena_part_0003_pages_0141-0210/auto/images/efc2223674df3ba35b7b1cbff5efb17510d019d0fbfe619e7d9731029fd5cb57.jpg)  
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

![](../chunks/Observational Astrophysics Lena_part_0003_pages_0141-0210/auto/images/4b0c4f9baa08439f6c54dd33000f508578ad8a6d9beae647e45f3585ca589fed.jpg)  
Fig. 4.7 The galactic coordinate system

Note that the usual definition through the coordinates of the pole and the centre makes use of four parameters instead of three. The four coordinates are not independent since the galactic centre lies in the plane normal to the direction defined by the galactic pole.

# 4.1.3 Change of Frame

In every case, changing from one celestial frame to another means finding the rotation matrix which transforms the vector basis of one frame into that of the other. The vectorial approach is far better adapted to modern calculation techniques than the traditional method based on trigonometric relations in spherical triangles, and naturally it leads to exactly the same analytical formulas. However, as far as computation time is concerned, linear transformations are much more efficient for numerical computations than evaluating trigonometric lines occurring in the full formulas, and the programming aspect is more straightforward, too. While it should not be forgotten that the trigonometric calculations are embodied by the rotation operators, the latter become tools and their calculation can be optimised once and for all.

Given the vector $o M$ , let $x _ { 1 }$ ; $x _ { 2 }$ ; $x _ { 3 }$ be its Cartesian components in frame $R$ , and $x _ { 1 } ^ { \prime }$ ; $x _ { 2 } ^ { \prime }$ ; $x _ { 3 } ^ { \prime }$ its components in frame $R ^ { \prime }$ . We transform from $R$ to $R ^ { \prime }$ by rotating the triad through an angle $\phi$ about a direction $\pmb { I }$ . The transformation is parametrised by a $3 \times 3$ orthogonal matrix $\mathsf { R }$ .

![](../chunks/Observational Astrophysics Lena_part_0003_pages_0141-0210/auto/images/5768890b8fb2e0a6cf32a090600f9698ea56f8e22afab73692f1294f089cb835.jpg)  
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

![](../chunks/Observational Astrophysics Lena_part_0003_pages_0141-0210/auto/images/fed72ef8ae87d1cd680a4d9f6f073266f31a9b69966be53c86d9c909007009b1.jpg)  
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

![](../chunks/Observational Astrophysics Lena_part_0003_pages_0141-0210/auto/images/ffd3679aaad0d5a9b2bb8930182898b7f7cd4fa668dbe7681977b7f885bccdf0.jpg)  
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

![](../chunks/Observational Astrophysics Lena_part_0003_pages_0141-0210/auto/images/2cb39f026ad46a468aac31b9e70e5293823181b29170d0a83e5e2682c02bc12a.jpg)  
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

![](../chunks/Observational Astrophysics Lena_part_0003_pages_0141-0210/auto/images/0a2332fa1b38fba8b085f3a35842d9573f235c14b60a2f6363a3258fea261245.jpg)  
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

![](../chunks/Observational Astrophysics Lena_part_0003_pages_0141-0210/auto/images/7f5f9f42be0f66445ac89a284d738dde968624a1489352ecf8ea252803e3df6a.jpg)  
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

![](../chunks/Observational Astrophysics Lena_part_0003_pages_0141-0210/auto/images/2ac76b5158c0b0732a8575b9711bf228fb3eabe8eae9e2f04e26ecf507b2937a.jpg)  
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
