# Chapter 14 The Moon and its Rotation... 401

14.1 Cassi's Laws... ….401   
142 TheEa.Equatios....401   
14.3 The Libration in Longitude..   
14.4 Other Oscillations.... ...························ ..405   
14.5 Problems....... ...·.········.············.. ...411

# Appendix A Properties of Conics.. 413

A1 General Properties.. 413   
A2 The Elipse...... ...···························· 416   
A TheParabola... ...···..···.·····················.· 418   
A4 The Hyperbola.. ...··.·················.·····.···········. .420   
A.5 Pole......................4.22

# Appendix B The Rotation of Axes 425

# Appendix C Numerical Values. 427

OrbitalE.ementsof.Paets........... 427   
Satelies:.OrbitalandPhysicalData....430   
Physicalm.ent.sofPa.ets...........432   
The Earth......   
TheMo434   
TheS435   
PhysicalCostants 435   
Miscellaneous D.ata...... ...436

# Appendix D Miscellneous Expansions in Series... 437

D.1 f and g Series... 437   
D.2 Eliptic Motion.. 437   
Appendix E The Solution of Linear Systems... 439   
Appendix F The Generation on the Computer of   
Gaussian Deviates....... ..443   
Appendix G Some Orbits of Comets and Minor Planets.....445   
Appendix H The Greek Alphabet.... 449   
AppendixI Random Variables,and Least Squares.. ..451

# Appendix J Notes on Hamiltonian Mechanics 457

J.1 Elements of Lagrangian Mechanics. 457   
J.2 Hamilton's Equations.. 458   
J.3 Canonical Transformations.. 460   
J.4 Canonical Transformations Defined by Functions 462   
J.5 The Hamilton-Jacobi Equation...... 463   
J.6 The Problem of Two Bodies. 464   
J.7 Perturbed Motion... 465

References and Biblography. 469

Index. 477

# TheAstronomical Background

# 1.1Introduction

Much of the theory in this text is that of conventional mechanics,but since itsapplicationswillconcern celestial objects，we shall beusing terms that may notbefamiliar to readerswho lack a background in astronomy.Thischapter is intended forsuch readers.It isconfined toa bare introduction to theastronomicaltermsused in the text.Readers are stronglyadvised torefer,inaddition， tosone general text on descriptive astronomy.

The fundamental law of celestial mechanics is Newton's law of gravitation. Mostapplications concern the solar system,but the theory can be applied anywherein the universe.For very small distances,comparable with the size of the atom,and forverylargedistances,of the orderofabillionlightyears,this law may,perhaps,not be useful,but we shall not be concerned withsuch extremes hereItis important to realize that,apart from some snall modifications(as ithecase ofMercury's orbit)，Newton’slaw holds good in the sense that it givestherightanswers;furthermore it is the only reasonable law inelementary mechanics that gives the right answers.In practice,the law is used not only in work on the solar system but also in the mechanics ofmultiple star systems,of the galaxy,and even of clusters of galaxies.

Incelestial mechanics we are primarily concerned with things as we find them.Weneed to explain observed motionand to provide accurate predictions forthe future.But when a rocket is launched,some control is exercised over its orbit,even if only bya judicious choiceof the initial conditions of launching.An orbit is chosen in advance; in addition to the forces due to gravity，thrustscan beimposed;if the rocket does not follow its chosen orbit precisely,corrections must be applied.These circumstances fall into the province of astronautics (which can be said to include“experimental celestial mechanics").Actually,the methods of celestial mechanics can be applied to the problemsof astronautics, and the basic theory of the two subjects is the same.

# 1.2Some Definitions

The solar system contains one star, the Sun, and various bodies that travel in orbits around the Sun.

A star is a celestial body that provides its own light.

A planet is a body，revolving around a star, that does not provide its own light. In the solar system the planets “shine” by virtue of light reflected from the Sun. A planet is much less massive that a star. Jupiter contains more mass than the remainder of the planets in the solar system put together, but it still has only about one-thousandth of the mass of the Sun. The orbits of the planets in the solar system (excepting that of Pluto) lie very roughly in the same plane and are very approximately circular. The names of the major planets in the solar system are:Mercury，Venus,the Earth,Mars,Jupiter, Saturn,Uranus, Neptune,and Pluto,in order of increasing distance from the Sun (but a part of Pluto's orbit lies within that of Neptune).The first four and Pluto are terrestrial planets and are much smaller and less massive than the remaining four,which are the giants.Planets with orbits outside that of the Earth are superior; Mercury and Venus are inferior planets.

In addition to the major planets there are countless minor planets (also called asteroids or planetoids),most of which have orbits lying between those of Mars and Jupiter. These are very much smaller than the major planets and, with few exceptions,have diameters of the order of a few kilometers or less.

There may be a continuous gradation between the minor planets and meteorites,but the latter are usually considered to be the size of large rocks at most,and to merge into the micrometeorites,which are microscopic. Billions of these strike the Earth ina day;some of them,possibly the ones that appear as meteors (or “shooting stars"),are certainly the remains of comets.

A comet is an aggregate of rocks and ice traveling around the Sun. When observed, it is surrounded by a haze of gases that gives it a characteristically fuzzy appearance. When close to the Sun it may develop a tail which will point away from the Sun. Comets have pronouncedly elongated orbits, many being nearly parabolic; the orbits are not concentrated near any plane. Those comets with periods of the order of ten to one hundred years are called periodic comets. It is important to remember that all these objects belong to the solar system and travel in orbits that remain (by astronomical standards) close to the Sun. Occasionally, a comet is expelled from the solar system as a result of perturbations by the planets.

A satellite is a body revolving around a planet. It is normally of negligible mass compared with its parent planet. The notable exceptions to this are the Moon, which has a mass of about one-eightieth of the Earth's mass,and Charon, satellite of Pluto, which has around one tenth of Pluto's mass.

The word “revolve”will be used in this text to imply motion around a point. “Rotate”will imply motion about an axis.Thus the Earth revolves around the Sun but rotates on its axis.

The word “orbit” is sadly abused nowadays, both as a noun and as a verb.

Here it will be used only as a noun. The operative definition is no more than “the course of a planet, comet, satellite, etc.” It is entirely wrong to speak of a rocket fired from the Earth as “starting to move in orbit around the Sun a few days later.”

The Earth is nearly spherical, with a radius of about 4000 miles or 6400 km. It is fattened at the poles,the deviations from a sphere being slight (the difference between the polar and equatorial diameters is about 43 km) but important in precise work.

The fundamental problem in celestial mechanics is the two-body problem; this is concerned with the motion of two point masses which move subject only to their mutual gravitational attraction. This situation is nearly reproduced in the solar system for orbits of objects around the Sun. Deviations from it, caused, for instance, by the added attraction of Jupiter on a planet, are known asperturbations.

# 1.3Orbital Definitions

In the orbit of one body about another the least and greatest separations are indicated by applying the prefixes “peri-” and "apo-" $( \ O I ^ { 6 } \overrightarrow { a p } - \overrightarrow { 1 } )$ respectively to the Greek word for the more massive of the two bodies. For instance,in the orbit of a satellite around the Earth, these positions are called perigee and apogee; for a planet revolving around the Sun, the positions are perihelion and aphelion; for motion around any star, “-astron” is used, and for any center of force, -centron.” But the less pedantic “pericenter” and “apocenter” are preferable today. (The misbegotten word "periapsis” means, if it means anything, “near to an apsis”and is best avoided.)

The time taken for a complete revolution in an orbit, with respect to the stars is the sidereal period of that orbit. Since an orbit can itself revolve in space,the sidereal period need not be equal to the time between， say， one passage through perihelion to the next. Various qualifications of “period” will appear during the course of the text: it will only be used without qualification when all perturbations are ignored in the discussion, so that the orbit is constant and fixed in space; then the sidereal period will be implied.

Names of some of the positions with respect to the Earth in the orbits of the planets areilustrated in Figure 1.1. The reader should note the differences between the names for the orbits of the inferior and superior planets. The average time taken for a planet to return to the same position relative to the Earth (for instance, the average time between one opposition and the next） is called the mean synodic period of the planet. The relation between the sidereal and mean synodic periods of a planet is

$$
{ \frac { 1 } { \ s i d e r e a l { \mathrm { \ p e r i o d } } } } + { \frac { 1 } { \ s y n o d i c { \mathrm { ~ p e r i o d } } } } = 1
$$

for a superior planet, or

$$
\mathrm { \frac { i } { \ s i d e r e a l { \ p e r i o d } } - \frac { i } { \ s y m o d i c { \ p e r i o d } } = i }
$$

for an inferior planet, the unit of time being the sidereal year (the sidereal period of the Earth).

![](../chunks/Fundamentals of Celestial Mechanics (John M. A. Danby) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0040/ocr/images/c9766a7aa6b83cfc6a0092a28b064464462fc638003188252da5bb75b85a9e8d.jpg)  
Figure 1.1 Here the orbits are illustrated as seen from the north pole of the ecliptic.

When observed from the north, most orbits around the Sun would be described counter-clockwise; these are direct orbits. Some comets and a few satellites revolve in the opposite sense; their orbits are retrograde.

# 1.4 Kepler's Laws

The motion of the planets was found by Kepler to follow three laws:

1. The orbit of each planet is an ellipse; with the Sun at one of its foci.

2.Each planet revolves so that the line joining it to the Sun sweeps out equal areas in equal intervals of time. (This is the“law of areas.")

3. The squares of the periods of any two planets are in the same proportion as the cubes of their mean distances from the Sun. (This law requires modification;it will be described in Chapter 6.)

Motion following these laws is called “Keplerian motion,” and the planets are said to move in “Keplerian orbits.” More generally, “Keplerian motion” also includes hyperbolic orbits.

# 1.5The Astronomical Unit

Consider Kepler's third law. The sidereal period of a planet can be calculated from its mean synodic period, which can be observed. If $P$ is the sidereal period and $\pmb { \alpha }$ the mean distance from the Sun in the orbit of some planet, and if $P _ { \widehat { E } }$ and $\pmb { \mathcal { a } } \pmb { \mathcal { E } }$ are the corresponding values for the orbit of the Earth, we have

$$
\frac { \mathcal { P } ^ { 2 } } { \bar { \mathcal { P } } _ { \mathcal { E } } ^ { 2 } } = \frac { a ^ { 3 } } { a _ { \mathcal { E } } ^ { 3 } } .
$$

Let $P _ { E }$ (the sidereal year) and $a _ { E }$ be chosen as units of time and length: $a \mathbf { \delta } \mathbf { \delta }$ is the astronomical unit, it will be discussed more rigorously later. In these units

$$
P ^ { 2 } = \alpha ^ { 3 } .
$$

Hence a can be calculated for any planet,and a scale model can be constructed of the relative dimensions of the planetary orbits in the solar system. Any interplanetary distance can then be measured in terms of the astronomical unit. But if we want to find a distance in terms of some absolute unit, kilometers, say,we must first know the length of the astronomical unit in kilometers. This has been accomplished through radio communication with interplanetary spacecraft.(Efforts to measure the astronomical unit prior to the “space age” make up a fascinating chapter in the history of science.） Roughly, one astronomical unit is equal to 92,957,000 milesor 149,600,000 km.

Instead of the astronomical unit, we sometimes refer to the Sun's geocentric parallag. This is the angle subtended at the mean distance of the Sun by the Earth's equatorial radius. The value corresponding to the figures quoted above is $\ S ^ { \prime \prime }$ .794.

# 1.6.Bode's Law

Consider the sequence of numbers

where,after the start,each number is doubled to give the next one. Add 4 to each,and divide the result by 10. We have the resulting sequence

and these numbers represent, with moderate accuracy, the mean distances of the planets from the Sun, with the exception of Neptune and Pluto. The number 2.8 corresponds to the average of the system of minor planets. This rule, known as Bode's law, was actually noted earlier by Titius, in 1772. It acted as a stimulus for the search for a planet between Mars and Jupiter, although the existence of such a planet had been expected long before. It is sometimes a useful rule of thumb for recalling planetary distances. Table 1.1 indicates the degree of its success.

Table 1.1 Mean Distance from the Sun   

<table><tr><td>Name</td><td>Bode&#x27;sLaw True</td></tr><tr><td>Mercury</td><td>0.4 0.39</td></tr><tr><td>Venus</td><td>0.7 0.72</td></tr><tr><td>Earth</td><td>1.0 1.00</td></tr><tr><td>Mars</td><td>1.6 1.52</td></tr><tr><td>Minor planets （Ceres）</td><td>2.8 2.77</td></tr><tr><td>Jupiter</td><td>5.2 5.20</td></tr><tr><td>Saturn</td><td>10.0 9.54</td></tr><tr><td>Uranus</td><td>19.6 19.18</td></tr><tr><td>Neptune</td><td>38.8 30.06</td></tr><tr><td>Pluto</td><td>77.2 39.44</td></tr></table>

# 1.7Astronomical Observations

Traditional astronomical observations consist of the direction of some object and the time of the observation. Each of these quantities requires careful definition and some discussion. The direction of an object is given by two angles. To describe completely its position in space relative to the observer, its distance must also be known; this cannot normally be observed and must be found by some indirect method, although in some cases radar can be used. For spacecraft, range and range-rate can be observed, and, indeed, those observations are usually more accurate than those of direction.

# 1.8 The Celestial Sphere

The direction of an object is given by two angles that fix its position on the celestial sphere. This is a spherical shell of arbitrarily large radius on which celestial objects appear projected. Normally the center of the Earth is at the center of the celestial sphere, but it may be convenient at times to have the observer or the Sun there.The “fixed”stars occupy nearly constant positions on the celestial sphere; the reasons for their inconstancies do not concern us here, but we note in passing that every star has its individual motion in space. The planets (literally "wanderers”) and other bodies in the solar system move in paths on the celestial sphere, the most important of which is the path described by the center of the Sun, known as the ecliptic.

A great circle on the surface of a sphere is formed by the section with any plane passing through its center. Since the orbit of the Earth about the Sun takes place in a plane which contains the Sun, the ecliptic is a great circle on the celestial sphere. The line through the center of a sphere perpendicular to a great circle cuts the sphere in the poles of that great circle. If $A$ and $\mathcal { B }$ are two points on a sphere that are not at opposite ends of a diameter, there is one and only one great circle passing through them. The angle written $A B$ is the angle subtended by $A B$ at the center of the sphere.

![](../chunks/Fundamentals of Celestial Mechanics (John M. A. Danby) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0040/ocr/images/9c515662781e03596130c71e1c8c168e0fea77ea930033214c85814f8a5694d5.jpg)  
Figure 1.2

To define any coordinates, some system of reference is required. Weillustrate this for the case of the surface of a sphere by considering the familiar coordinates of longitude and latitude on the surface of the Earth. The Earth's axis of rotation cuts the surface of the Earth in the north and south poles, and the great circle corresponding to these is the equator. The latitude of a point $p$ is the angular distance of $\mathcal { P }$ measured north or south of the equator (see Figure 1.2).A great circle passing through the poles is called a meridian, and the meridian that passes through Greenwich (England) is the prime meridian. The angle between the meridian through $\mathcal { P }$ (there is only one, so long as $P$ is not at a pole) and the prime meridian is the longitude of $P$ it is measured east or west.

![](../chunks/Fundamentals of Celestial Mechanics (John M. A. Danby) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0040/ocr/images/3418d5eef1126abeb86da844075d57e13d9c79a7e4d624f4797461de32876e86.jpg)  
Figure 1.3

![](../chunks/Fundamentals of Celestial Mechanics (John M. A. Danby) (z-library.sk, 1lib.sk, z-lib.sk)_part_0001_pages_0001-0040/ocr/images/1892a044be94bc543cc2b3a8fe7169b0ae5385110a266efaf60c4eaa11ebada4.jpg)  
Figure 1.4

Similar angles are used to fix position on the celestial sphere. Various ref-erence systems are used, the most convenient of which, for practical purposes, is the equatorial system. The Earth's axis of rotation cuts the celestial sphere in the celestial north and south poles, the celestial equator being midway be tween them. The ecliptic cuts the celestial equator in two points known as the equinoxes. When the Sun crosses the equator, going north,it passes through the vernal equinoz, or frst point of Aries, written p. Great circles passing through the celestial poles are known as hour circles. The hour circle corresponding to the prime meridian passes through $r _ { \ P }$ and the angle measured eastward from this to the hour circle through some star, $X$ ,is the right ascension of $X$ written Q. $\alpha$ is usually measured in units of time such that twenty-four hours equals $3 6 0 ^ { \circ }$ 8, the declination of $X$ is the angle corresponding to latitude; it is measured positive north and negative south of the celestial equator. (See Figure 1.3.）

Celestial longitude and latitude are based on the ecliptic. Celestial latitude, $\beta$ ,is measured positive north and negative south of the ecliptic, and celestial longitude, $\lambda$ is measured eastward from the vernal equinox. (See Figure 1.4.)

Several other coordinate systems are in use, but the two described here are the only ones needed in this text.

The angle between the celestial equator and the ecliptic is known as the obliquity of the ecliptic,and denoted by e. Its value is about $2 3 ^ { \circ } 2 7 ^ { \prime }$ . The Sun passes through the vernal equinox at the beginning of spring in the northérn hemisphere and through the autumnal equinox (the corresponding point on the other side of the celestial sphere) at the beginning of autumn. The points of the ecliptic farthest north and south of the equator are the summer and winter solstices. The reader is urged to consult any standard text for a description of the connection between these points and the seasons experienced on Earth.

# 1.9Precession, Nutation, and Variation of Latitude

A disadvantage of the coordinate systems described above is that the fundamental reference systems are not fixed. The causes of this will be very briefly described.

Variation of latitude. Consider the Earth's axis of rotation as remaining fixed in space, while the Earth slips about it、The effect of this is that the geographical poles “wander” within smallareas of radius some fteen meters, causing perceptible if small changes in the latitudes of points on the Earth.

Lunisolar precession. Due to the pull of the Moon and Sun on the Earth's equatorial bulge, the Earth's axis is slowly precessing, or describing a cone in space,a complete revolution occurring in a period of about 26,0o0 years. The obliquityremains approximately constant.

Nutation. The plane of the Moon's orbit about the Earth rotates, with respect to the ecliptic, with a period of just under nineteen years. This leads to an oscillation in that component of the pull on the Earth's equatorial bulge which is due to the Moon, causing an extra oscillation or “nodding” of the Earth's axis. This nutation is superimposed on the precessional motion.

Planetary precession. Due to perturbations from the other planets on the Earth's orbit, the ecliptic is not fixed in space, but is gradually changing.

General precession is the combined effect of lunisolar and planetary precession.

A consequence of precession is that the celestial equator is not fixed on the celestial sphere, and the vernal equinox is slowly moving westward along the ecliptic (which changes much more sluggishly). It was named the “first point ofAries”when it actually lay in the constellation Aries,but it is now in Pisces. As a result of this, the coordinates of celestial objects are gradually changing: they must always be referred to some date or epoch for comparison with other observations.

Star positions are usually referred to a mean equator and mean equinox for some epoch,which are found by neglecting the periodic parts of the motion of the celestial equator. The resulting coordinates are mean coordinates.

# 1.10 The True and Apparent Places of a Celestial Object

When specifying the coordinates of a celestial object rigorously, it is necessary to make clear which point of the solar system is at the center of the celestial sphere, or the origin of coordinates.

The true place of a star is defined with the Sun at the origin and with respect to the true equator and true equinox at the instant of observation.

For the apparent place, the origin is moved to the center of the Earth. This move is bound to change the relative positions of the stars on the celestial sphere, the closer ones being affected more. These changes are ascribed to annual parallax (since they are periodic, the period of variation being the sidereal year)； they are practically negligible for all but the nearest stars. More important changes are caused by annual aberration. Since light moves with finite velocity, the direction in which an object is observed will depend not only on its true geometrical direction but also on the velocities of the object and observer and on the velocity of light. For a star, which will have constant velocity over long periods, the changes are caused by the Earth's orbital velocity around the Sun, and this gives rise to annual aberration. If the object is in the solar system, its own velocity varies and must be taken into account together with the time lag caused by the light traveling from the object to the observer; in this case we have displacements due to planetary aberration.

An actual observation is made from the surface of the Earth,and in interpreting this we have to allow for an additional aberrational efect caused by the velocity of the observer that is due to the Earth's rotation; this is diurnal aberration. In addition we must take into account the fact that the origin has been moved again, introducing a further effect due to parallax.

Formulas for these various effects are given in standard texts on spherical astronomy; they are also given in most almanacs, together with the physical constants involved.

We remark in passing that the refraction of light in the Earth's atmosphere can affect considerably the apparent angle of a celestial object above the horizon; the effect is greater near the horizon where it is of the order of half a degree.

# 1.11 The Measurement of Time

The fundamental “clock” for the measurement of time has for centuries been the Earth, rotating on its axis. One complete rotation with respect to the celestial sphere measures one sidereal day or twenty-four hours of sidereal time. Because of the Sun's motion around the celestial sphere, a complete rotation of the Earth with respect to the Sun (which measures the solar day or twenty-four hours,apparent solar time) takes about four minutes longer than the sidereal day. For obvious reasons the sidereal day is not used for civil purposes.

Since the motion of the Sun around the celestial sphere is neither uniform nor along the celestial equator, the solar day is not of constant length.A fictitious sun called the mean Sun has been invented, moving uniformly along the celestial equator, for the measurement of mean solar time.

The time measured astronomically by an observer will depend on his longitude;it will be his local time. Since it would be impractical to have civil time varying continuously with longitude or to standardize it for the whole world, the Earth is divided into twenty-four time zones, bounded by meridians at $\sum 5 ^ { \circ }$ intervals and centered on longitudes that are integral multiples of $1 5 ^ { \circ }$ ,except where civil convenience calls for slight irregularities. Within each time zone the civil time is the same,being dictated by the mean solar time at the central meridian,and the time in each zone differs from the times in its immediate neighbors by one hour. The meridian of longitude $1 8 0 ^ { \circ }$ (again with slight variations for practical convenience) is known as the international date line. When it is midnight at this longitude, the date is the same everywhere on the Earth.A traveler crossing this line experiences a discontinuity of one day in his calendar.

Astronomical observations are usually referred to universal time, or U.T., which is the mean solar time at the meridian of Greenwich.

The Julian date is the number of days,and fraction of a day, measured from mean noon on January 1 of the year 4713 B.C. It is tabulated in almanacs for every day of the year.

As a clock, the Earth does not keep accurate time. Consider the prediction from theory of the position of some celestial object at some definite time. If observation does not confirm the prediction,it is possible that either the theory or the recorded time of observation may be in error. Toward the end ofthe nineteenth century it had become increasingly probable that observed deviations between observations and the gravitational theory of the Moon's motion were not caused by imperfections in the theory but by irregularities in the Earth's rate of rotation. Proof was lacking until, during the first half of the twentieth century, it was shown conclusively that the differences between observation and theory in the mean longitudes of Mercury, Venus,and the Sun exhibit fuctuations that are identical, if expressed in seconds of time, to those in the Moon's mean longitude. Over the past three centuries these fuctuations have ranged between ±30 seconds of time. A much smaller annual variation of around one-tenth of a second in the time given by the Earth's rotation has been established with the aid of terrestrial clocks, notably the quartz crystal clock and atomic clocks. In addition ancient observations of eclipses have shown that the day is gradually becoming longer (although only by about one-thousandth of a second per day per century).

To cope with this situation， ephemeris time has been introduced. This runs on uniformly with an invariable basic unit, and so corresponds with the theoretical notion of time used in mechanics. It is this time that should be used in celestial mechanics. The difference between ephemeris time and universal time is tabulated in the standard almanacs.
